"""后台主流程：读私有仓库里的标记，补全详情，定期刷新三家评分，处理在线搜索。

私有数据仓库（data/）里的文件：
  marks.json     你的标记（网页写，这里只读）
  requests.json  网页提交的待办：要补全的片子、在线搜索（这里处理完清空）
  meta.json      每部片子的详情和评分（这里写）
  people.json    影人的中文名和头像（这里写）
  lookup.json    最近一次在线搜索的结果（这里写）
  series.json    看过的片子属于哪些系列（Wikidata），网页用来自动生成系列专题（这里写）
  chars.json     宇宙专题里每部片子的角色剧照（IMDb），网页拿来当角色卡面（这里写）
  status.json    各数据源最近是否正常（这里写）
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from sources import IMDb, Wikidata, Douban, RottenTomatoes, Comics, Pinterest, SourceError, norm, nap  # noqa: E402

CST = timezone(timedelta(hours=8))
DAY = 86400
SEASON_RE = re.compile(r"\s*第[一二三四五六七八九十百\d]+季\s*$")
CN_NUM = "零一二三四五六七八九十"


def now():
    return time.time()


try:
    import opencc
    _t2s = opencc.OpenCC("t2s")
    t2s = _t2s.convert
except Exception:      # 没装 opencc 也能跑，繁体就照原样
    def t2s(x):
        return x


def iso():
    return datetime.now(CST).isoformat(timespec="seconds")


def iso_days_ago(n):
    return (datetime.now(CST) - timedelta(days=n)).isoformat(timespec="seconds")


def load(p, default):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def save(p, data):
    Path(p).write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")


def cn_season(n):
    if n <= 10:
        return CN_NUM[n] if n < 10 else "十"
    if n < 20:
        return "十" + CN_NUM[n - 10]
    return CN_NUM[n // 10] + "十" + (CN_NUM[n % 10] if n % 10 else "")


def role_intro(intro, cn_name, role, en_name=""):
    """从豆瓣简介里挑出写到 TA 的句子；挑不到就给作品简介的第一句。"""
    intro = re.sub(r"\s+", " ", intro.replace("\u3000", " ")).strip()
    if not intro:
        return "", ""
    # "（凯尔·钱德勒 Kyle Chandler 饰）" 里的英文名去掉，读起来短一点
    intro = re.sub(r"[（(]([^（）()]*?[\u4e00-\u9fff·]+)\s+[A-Za-z][^（）()]*?饰[）)]", r"（\1 饰）", intro)
    sents = [x.strip() for x in re.findall(r"[^。！？!?]+[。！？!?]?", intro) if x.strip()]
    role_cjk = "".join(re.findall(r"[\u4e00-\u9fff·]+", role or "")).strip("·")
    keys = [k for k in [cn_name, cn_name.split("·")[-1] if "·" in cn_name else "", en_name, role_cjk] if k and len(k) >= 2]
    hit = [x for x in sents if any(k in x for k in keys)]
    if hit:
        out = hit[0] if len(hit[0]) >= 40 or len(hit) == 1 else hit[0] + hit[1]
        return out[:180], ""
    return "", (sents[0] if sents else "")[:120]


def load_index_cn(idx_dir):
    """从离线索引里拿中文译名，豆瓣按名字找条目时用。"""
    cn = {}
    for f in ("s1.txt", "s2.txt"):
        p = Path(idx_dir) / f
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            x = line.split("\t")
            if len(x) > 7 and (x[6] or x[7]):
                cn["tt" + x[0]] = [x[6]] + [a for a in x[7].split("|") if a]
    return cn


class Sync:
    def __init__(self, data, idx, budget):
        self.dir = Path(data)
        self.marks = load(self.dir / "marks.json", {}).get("items", {})
        self.meta = load(self.dir / "meta.json", {})
        self.people = load(self.dir / "people.json", {})
        self.persons = load(self.dir / "persons.json", {})
        mk = load(self.dir / "marks.json", {})
        self.follows = mk.get("follows", {})
        self.roles = {k: v for k, v in (mk.get("roles") or {}).items() if not v.get("del")}   # 本命角色：{"nm~tt": {...}}
        self.reqs = load(self.dir / "requests.json", {})
        self.status = load(self.dir / "status.json", {"sources": {}})
        self.series = load(self.dir / "series.json", {})
        self.chars = load(self.dir / "chars.json", {})
        self.idx_cn = load_index_cn(idx) if idx else {}
        self.budget = budget          # 每次最多访问豆瓣 / 烂番茄多少部，别太频繁
        self.imdb, self.wd, self.db, self.rt, self.comics = IMDb(), Wikidata(), Douban(), RottenTomatoes(), Comics()
        self.pin = Pinterest()
        self.changed = False

    # ------------------------------------------------------------ 工具
    def ok(self, src, msg="正常"):
        self.status["sources"][src] = {"ok": True, "msg": msg, "at": iso()}

    def fail(self, src, e):
        print(f"[{src}] {e}")
        prev = self.status["sources"].get(src) or {}
        self.status["sources"][src] = {"ok": False, "msg": str(e), "at": iso(),
                                       "since": prev.get("since") if not prev.get("ok", True) else iso()}

    def active(self):
        return [k for k, v in self.marks.items() if not v.get("del")]

    @staticmethod
    def released_days(m):
        d = m.get("date") or (f"{m['year']}-07-01" if m.get("year") else None)
        try:
            return (datetime.now() - datetime.fromisoformat(d)).days
        except (TypeError, ValueError):
            return 9999

    def stale(self, m, key):
        """评分多久刷新一次：新片勤一点，老片很少变。"""
        age = self.released_days(m)
        every = 1 if age < 120 else 7 if age < 730 else 30
        if m.get("type") in ("tvSeries", "tvMiniSeries") and not m.get("ey"):
            every = min(every, 7)     # 还在播的剧
        return now() - (m.get("at") or {}).get(key, 0) > every * DAY

    # ------------------------------------------------------------ IMDb 基本信息
    def refresh_base(self, ids, force=False):
        todo = [i for i in ids if force or i not in self.meta
                or now() - (self.meta[i].get("at") or {}).get("base", 0) > 30 * DAY]
        # 评分每 2 天跟着刷新（批量查很便宜）
        todo += [i for i in ids if i not in todo and i in self.meta
                 and now() - (self.meta[i].get("at") or {}).get("imdb", 0) > 2 * DAY]
        if not todo:
            return
        try:
            got = self.imdb.details(todo)
            self.ok("imdb")
        except SourceError as e:
            self.fail("imdb", e)
            return
        for tid, d in got.items():
            m = self.meta.setdefault(tid, {})
            keep = {k: m[k] for k in ("douban", "rt", "cn", "intro", "dgenres", "dcountries", "dpic",
                                       "dbid", "rtslug", "seasons_db", "at") if k in m}
            m.clear()
            m.update(d)
            m.update(keep)
            m.setdefault("at", {})
            m["at"]["base"] = m["at"]["imdb"] = now()
            self.changed = True
        for tid in todo:
            if tid not in got and tid not in self.meta:
                self.meta[tid] = {"id": tid, "missing": True, "at": {"base": now()}}

    # ------------------------------------------------------------ 豆瓣 / 烂番茄编号
    def resolve_ids(self, ids):
        need = [i for i in ids if i in self.meta and not self.meta[i].get("missing")
                and ("dbid" not in self.meta[i] or "rtslug" not in self.meta[i] or not self.meta[i].get("cn"))]
        if not need:
            return
        try:
            got = self.wd.by_imdb(need)
            self.ok("wikidata")
        except SourceError as e:
            self.fail("wikidata", e)
            return
        for tid in need:
            m, w = self.meta[tid], got.get(tid, {})
            if "dbid" not in m and w.get("douban"):
                m["dbid"] = w["douban"]
            if "rtslug" not in m and w.get("rt"):
                m["rtslug"] = w["rt"]
            if not m.get("cn") and (w.get("zh") or w.get("tw")):    # 豆瓣补全后会换成豆瓣的片名
                m["cn"] = t2s(w.get("zh") or w["tw"])
                self.changed = True

    # ------------------------------------------------------------ 系列（Wikidata P179）
    def refresh_series(self, priority=()):
        """标记过的片子属于哪些系列；系列的成员两周刷新一次（新作官宣、续集上映）。"""
        by = self.series.setdefault("by", {})      # tt -> {"s": [Q...], "at": 时间}
        ser = self.series.setdefault("s", {})      # Q -> {"zh", "en", "items", "at"}
        mine = set(self.active())
        ask = [t for t in dict.fromkeys(list(priority) + sorted(mine))
               if t in mine and now() - (by.get(t) or {}).get("at", 0) > 45 * DAY][:400]
        try:
            if ask:
                got = self.wd.series_of(ask)
                for t in ask:
                    by[t] = {"s": got.get(t, []), "at": now()}
            for d in ser.values():      # 旧数据：中文名混着台湾译名，挪到 tw 里，网页优先用大陆片名推
                if "tw" not in d:
                    z = d.get("zh") or ""
                    d["tw"], d["zh"] = (t2s(z), "") if t2s(z) != z else ("", z)
            used = {q for t in mine for q in (by.get(t) or {}).get("s", [])}
            stale = [q for q in used if now() - (ser.get(q) or {}).get("at", 0) > 14 * DAY][:60]
            if stale:
                got = self.wd.series_members(stale)
                for q in stale:
                    d = got.get(q) or {"zh": "", "tw": "", "en": "", "items": []}
                    d["tw"] = t2s(d.get("tw") or "")
                    d["items"] = sorted(d["items"], key=lambda x: (x[2] or 9999, x[1]))[:120]
                    d["at"] = now()
                    ser[q] = d
            # 系列的角色：Wikidata 里“谁演了哪个角色”，成员刷新时一起刷新
            want = [q for q in used if q in ser and "c" not in ser[q] and 2 <= len(ser[q].get("items") or []) <= 60][:12]
            for q in want:
                ser[q]["c"] = self.series_chars([it[0] for it in ser[q]["items"]])
            for q in [q for q in ser if q not in used]:
                del ser[q]
            if ask or stale:
                self.ok("wikidata")
        except SourceError as e:
            self.fail("wikidata", e)

    def series_chars(self, tts):
        """整理成网页用的角色表：出场越多越靠前，最多 60 位。中文名先用 Wikidata，没有再用豆瓣演职员表里的角色名。"""
        raw = self.wd.series_chars(tts)
        out = []
        for q, c in raw.items():
            actors = sorted(c["a"].items(), key=lambda x: -x[1][1])
            w = sorted(c["w"], key=lambda t: tts.index(t) if t in tts else 999)
            if not (c["zh"] or c["tw"] or c["en"]):
                continue
            out.append({"k": q, "zh": c["zh"] or t2s(c["tw"]), "en": c["en"], "a": [[nm, n] for nm, (n, _) in actors[:3]],
                        "w": w, "o": min(c["w"].values())})
        out.sort(key=lambda c: (-len(c["w"]), c["o"]))
        return out[:60]

    def enrich_series_chars(self):
        """没有中文名的角色，用豆瓣演职员表里的中文角色名；再从豆瓣简介里挑一句写到 TA 的话当介绍。"""
        for d in (self.series.get("s") or {}).values():
            for c in d.get("c") or []:
                nms = {a[0] for a in c["a"]}
                for tt in c["w"]:
                    m = self.meta.get(tt) or {}
                    hit = next((p for p in m.get("cast") or [] if p.get("id") in nms), None)
                    if not hit:
                        continue
                    role = re.split(r"\s*[/／]\s*", hit.get("role_cn") or "")[0].strip()
                    if role and not c.get("db"):
                        c["db"] = role
                    if not c.get("i") and m.get("intro"):
                        who = (self.people.get(hit["id"]) or {}).get("cn", "")
                        rintro, _ = role_intro(m["intro"], c.get("zh") or role, role, c.get("en") or "")
                        if rintro and (c.get("zh") or role or "") and any(k and k in rintro for k in (c.get("zh"), role, who)):
                            c["i"] = rintro
                if c.get("i") and c.get("db"):
                    continue

    # ------------------------------------------------------------ 自动系列：漫画原型
    def refresh_comics(self, limit=15):
        """后台自动找到的系列（X 战警、蜘蛛侠三部曲……）给角色配漫画原型，存在 series.json 的 cm 里：
        {角色 Q 号: 漫画原型}，{"at": 时间} 表示找过、没有。系列出了新人只查新人；没找到的 30 天后再试。"""
        ser = self.series.get("s") or {}
        cmap = self.series.setdefault("cm", {})
        found = lambda v: v.get("s") or v.get("img")
        todo = []
        for q, d in ser.items():
            cs = d.get("c") or []
            if len(cs) < 3:
                continue
            new = {c["k"] for c in cs if c["k"] not in cmap or (not found(cmap[c["k"]]) and now() - cmap[c["k"]].get("at", 0) > 30 * DAY)}
            if new:
                todo.append((cs, new))
        if not todo:
            return
        try:
            for cs, new in todo[:limit]:
                r = self.comics.series(cs, only=new)
                for k in new:
                    v = r.get(k) if r else None
                    cmap[k] = {**v, "at": now()} if v else {"at": now()}
            self.ok("comics", f"已配 {sum(1 for v in cmap.values() if found(v))} 位")
        except SourceError as e:
            self.fail("comics", e)
        # 系列刷新后不再出现的角色，记录清掉
        live = {c["k"] for d in ser.values() for c in d.get("c") or []}
        for k in [k for k in cmap if k not in live]:
            del cmap[k]

    # ------------------------------------------------------------ 宇宙专题：角色剧照
    def refresh_chars(self, limit=100):
        """宇宙专题（docs/universes.json）里每部片子的图：只留单人、且是这部里某个角色演员的图
        （角色海报、剧照），网页按角色挑一张当卡面。看过的片子先做，45 天刷新一次。"""
        try:
            U = json.loads((Path(__file__).resolve().parent.parent / "docs" / "universes.json")
                           .read_text(encoding="utf-8"))["universes"]
        except (OSError, ValueError, KeyError):
            return
        T = self.chars.setdefault("t", {})
        actors = {}
        for u in U:
            wk = {w["k"]: w["id"] for w in u["works"] if w.get("id")}
            for c in u["chars"]:
                nms = {a[0] for a in c.get("a") or [] if a and a[0]}
                for k in c["w"]:
                    if wk.get(k) and nms:
                        actors.setdefault(wk[k], set()).update(nms)
        for d in (self.series.get("s") or {}).values():
            for c in d.get("c") or []:
                nms = {a[0] for a in c.get("a") or [] if a and a[0]}
                for t in c.get("w") or []:
                    if nms:
                        actors.setdefault(t, set()).update(nms)
        mine = set(self.active())
        need = sorted([t for t in actors if now() - (T.get(t) or {}).get("at", 0) > 45 * DAY], key=lambda t: t not in mine)[:limit]
        if not need:
            return
        try:
            got = self.imdb.title_images(need)
            self.ok("imdb")
        except SourceError as e:
            self.fail("imdb", e)
            return
        kind = {"poster": "P", "still_frame": "s", "publicity": "p"}
        for t in need:
            keep = []
            for k, w, h, ty, names in got.get(t) or []:
                if len(names) == 1 and names[0] in actors[t]:
                    keep.append([k, w, h, kind.get(ty, "o"), names[0]])
            T[t] = {"at": now(), "i": keep[:30]}
        self.changed = True

    # ------------------------------------------------------------ 剧集分集（按集打卡）
    def refresh_eps(self, ids, priority=(), limit=12):
        """标记过的剧集拉分集表：还在播的每周刷新，播完的四个月一次。点名要的先做。"""
        def due(t):
            m = self.meta.get(t) or {}
            if m.get("missing") or m.get("type") not in ("tvSeries", "tvMiniSeries"):
                return False
            age = now() - (m.get("at") or {}).get("eps", 0)
            return age > (7 if not m.get("ey") else 120) * DAY
        todo = [t for t in dict.fromkeys(list(priority) + list(ids)) if due(t)]
        todo.sort(key=lambda t: (t not in priority, "eps" in (self.meta.get(t) or {})))
        for t in todo[:limit]:
            try:
                eps = self.imdb.episodes(t)
                self.ok("imdb")
            except SourceError as e:
                self.fail("imdb", e)
                return
            m = self.meta[t]
            if eps:
                m["eps"] = eps
            m.setdefault("at", {})["eps"] = now()
            self.changed = True

    # ------------------------------------------------------------ 冷门角色的图（Pinterest → 存进数据仓库 img/）
    def _web_targets(self, force=()):
        """要找图的角色：本命角色；点亮了、但 IMDb 没有像样单人剧照也没有漫画原型的专题角色。
        返回 [(key, [搜索词...], 优先级)]，key 和网页一致：本命 r:nm:tt；专题 专题id:角色key"""
        mine = {t for t, v in self.marks.items() if not v.get("del") and v.get("s") in ("done", "doing")}
        T = (self.chars.get("t") or {})
        fol = {n for n, f in self.follows.items() if not f.get("del")}
        recent = lambda tts: max([self.marks.get(t, {}).get("t") or 0 for t in tts] or [0])
        # 排序：本命 > 追的人演的角色 > 最近看的片子里的角色
        # 自动去找的只有：本命、追的人演的角色、看过两部以上都有 TA 的角色；其他的等网页上点「去 Pinterest 找」
        rank = lambda pri, nms, tts: (pri if (pri == 0 or nms & fol or sum(1 for t in tts if t in mine) >= 2) else 9, 0 if nms & fol else 1, -recent(tts))

        def good_still(tts, nms):
            for t in tts:
                for k, w, h, ty, nm in (T.get(t) or {}).get("i") or []:
                    if nm in nms and ty in ("P", "s") and min(w, h) >= 400:
                        return True
            return False

        def title_of(t, fallback=""):
            m = self.meta.get(t) or {}
            return m.get("title") or fallback

        out = []
        roles = dict(self.roles)
        for k in force:   # 追的人换卡面时点了「再找找」：按演员名搜，图说明里要有 TA 的名字
            m = re.fullmatch(r"p:(nm\d+)", k or "")
            if m:
                n = (self.persons.get(m.group(1)) or {}).get("n") or ""
                if n:
                    out.append((k, [n, f"{n} photoshoot", f"young {n}", f"{n} actor"], (0, 0, 0), [n, "", ""]))
        # 漫画原型的角色点了「找更多漫画图」：按漫画里的名字搜漫画图（cm:专题id:角色）
        cm_force = [k for k in force if (k or "").startswith("cm:")]
        if cm_force:
            try:
                U0 = json.loads((Path(__file__).resolve().parent.parent / "docs" / "universes.json").read_text(encoding="utf-8"))["universes"]
            except (OSError, ValueError, KeyError):
                U0 = []
            hand = {f"{u['id']}:{c['k']}": c for u in U0 for c in u["chars"]}
            auto = {f"{q}:{c['k']}": c for q, d in (self.series.get("s") or {}).items() for c in d.get("c") or []}
            cmap0 = self.series.get("cm") or {}
            for k in cm_force:
                ck = k[3:]
                c = hand.get(ck) or auto.get(ck)
                if not c:
                    continue
                cm = c.get("cm") or cmap0.get(c["k"]) or {}
                name = re.sub(r"\s*\(.*?\)", "", cm.get("n") or cm.get("pg") or c.get("en") or "").strip()
                if not name:
                    continue
                pub = "DC" if ck.startswith("dc:") or "dc.fandom" in (cm.get("img") or "") else "Marvel"
                qs = [f"{name} comic art", f"{name} {pub} comics", f"{name} comic book panel"]
                fn = (cm.get("fn") or "").strip()
                if fn and fn.lower() != name.lower():
                    qs.insert(2, f"{fn} {pub} comics")
                out.append((k, qs, (0, 0, 0), [name, "", "comic comics"]))
        for k in force:   # 没设本命的角色，在网页上点了「去 Pinterest 找」也要找
            m = re.fullmatch(r"r:(nm\d+):(tt\d+)", k or "")
            if m and f"{m.group(1)}~{m.group(2)}" not in roles:
                roles[f"{m.group(1)}~{m.group(2)}"] = {}
        for key, r in roles.items():
            nm, _, tt = key.partition("~")
            P = self.persons.get(nm) or {}
            c = next((c for c in P.get("credits") or [] if c.get("id") == tt), {})
            role = re.sub(r"\s*\(.*?\)", "", c.get("role") or r.get("n") or "").strip()
            title = title_of(tt, c.get("n", ""))
            actor = P.get("n") or ""
            if role and title:
                out.append((f"r:{nm}:{tt}", self._queries(role, actor, title), rank(0, {nm}, [tt]), [role, actor, title]))
        try:
            U = json.loads((Path(__file__).resolve().parent.parent / "docs" / "universes.json").read_text(encoding="utf-8"))["universes"]
        except (OSError, ValueError, KeyError):
            U = []
        for u in U:
            wk = {w["k"]: w for w in u["works"]}
            for c in u["chars"]:
                ws = [wk[k] for k in c["w"] if k in wk and wk[k].get("id")]
                seen = [w for w in ws if w["id"] in mine]
                nms = {a[0] for a in c.get("a") or [] if a and a[0]}
                key = f"{u['id']}:{c['k']}"
                # 没有演员的生物（破胸者、猫鹅……）和配音角色也找：搜词用角色名 + 作品名，图说明里要有角色名
                if key not in force and (not seen or c.get("cm") or (nms and good_still([w["id"] for w in ws], nms))):
                    continue
                seen = seen or ws
                w0 = seen[0]
                title = w0.get("en") or title_of(w0["id"])
                actor = "" if c.get("vo") else (c.get("a") or [["", ""]])[0][1]
                out.append((key, self._queries(c["en"], actor, title), rank(1, nms, [w["id"] for w in ws]), [c["en"], actor, title]))
        cmap = self.series.get("cm") or {}
        for q, d in (self.series.get("s") or {}).items():
            for c in d.get("c") or []:
                seen = [t for t in c.get("w") or [] if t in mine]
                nms = {a[0] for a in c.get("a") or [] if a and a[0]}
                cm = cmap.get(c["k"]) or {}
                key = f"{q}:{c['k']}"
                if not nms or not c.get("en") or (key not in force and (not seen or cm.get("s") or cm.get("img") or good_still(c["w"], nms))):
                    continue
                seen = seen or c["w"]
                title = title_of(seen[0])
                actor = (c.get("a") or [["", ""]])[0][1]
                if title:
                    out.append((key, self._queries(c["en"], actor, title), rank(1, nms, c["w"]), [c["en"], actor, title]))
        return out

    @staticmethod
    def _queries(role, actor, title):
        """名字短、常见（Peter、Vandal）的角色先带上演员名搜，不然会搜到别的同名角色"""
        role = re.sub(r"\s*\(.*?\)|[\"“”]", "", role or "").strip()
        title = re.sub(r"\s*\(.*?\)", "", title or "").strip()
        plain = len(role.split()) < 2 or len(role) < 8
        qs = [f"{actor} {role} {title}", f"{role} {title}"] if plain and actor else [f"{role} {title}", f"{actor} {role} {title}"]
        if actor:
            qs.append(f"{actor} as {role}")
        else:
            qs.append(f"{role} movie")
        out = []
        for q in qs:
            q = re.sub(r"\s+", " ", q).strip()
            if q and q not in out:
                out.append(q)
        return out

    @staticmethod
    def _name_keys(names):
        """判断一张图是不是这个角色：说明里有角色名的词；或者同时有演员的姓和作品名（只有演员名的多半是现在的本人照）"""
        stop = {"the", "and", "mr", "mrs", "dr", "sr", "jr", "of", "von", "van", "de", "la", "le", "da", "a", "an", "in", "on"}
        role, actor, title = (list(names) + ["", "", ""])[:3]
        words = lambda x: {w for w in re.findall(r"[a-z]{3,}", (x or "").lower()) if w not in stop}
        last = [w for w in re.findall(r"[a-z]{3,}", (actor or "").lower()) if w not in stop]
        return {"role": words(role), "actor": set(last[-1:]), "title": words(title)}

    @staticmethod
    def _match(keys, text):
        t = (text or "").lower()
        r = sum(1 for w in keys["role"] if w in t)
        a = any(w in t for w in keys["actor"])
        ti = sum(1 for w in keys["title"] if w in t)
        ok = r > 0 or (a and ti > 0)
        return ok, r * 2 + ti + (1 if a else 0)

    def _save_img(self, raw):
        """缩到 560 宽的 JPEG，按内容起名存进 img/；返回 [路径, 宽, 高]"""
        import hashlib
        import io
        from PIL import Image
        im = Image.open(io.BytesIO(raw))
        im = im.convert("RGB")
        if im.width > 560:
            im = im.resize((560, round(im.height * 560 / im.width)), Image.LANCZOS)
        if im.height > 1000:
            im = im.crop((0, 0, im.width, 1000))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=80, optimize=True, progressive=True)
        data = buf.getvalue()
        name = f"img/{hashlib.sha1(data).hexdigest()[:16]}.jpg"
        (self.dir / "img").mkdir(exist_ok=True)
        (self.dir / name).write_bytes(data)
        return [name, im.width, im.height]

    def refresh_web(self, budget=14, seconds=120):
        W = self.chars.setdefault("w", {})
        deadline = now() + seconds
        want = [k for k in (self.reqs.get("imgs") or []) if isinstance(k, str) and 3 < len(k) < 80][:8]
        targets = {k: (qs, pri, names) for k, qs, pri, names in self._web_targets(set(want))}
        # 旧规则（只要提到演员名）找的图再筛一遍：只有演员本人、没提角色也没提作品的去掉；都去掉了就重新找
        for k, rec in list(W.items()):
            if rec.get("v") == 2 or k not in targets:
                continue
            keys = self._name_keys(targets[k][2])
            rec["i"] = [x for x in rec["i"] if len(x) < 5 or self._match(keys, x[4])[0]]
            rec["v"] = 2
            if not rec["i"]:
                del W[k]
            self.changed = True
        jobs = [k for k in want if k in targets] + sorted(
            [k for k in targets if k not in want and not W.get(k) and targets[k][1][0] < 9], key=lambda k: targets[k][1])
        jobs = jobs[:len([k for k in want if k in targets]) + budget]
        if not jobs:
            return
        got_any = False
        for key in jobs:
            if now() > deadline and key not in want:
                break
            qs, _, names = targets[key]
            rec = W.get(key) or {"i": [], "q": [], "v": 2}
            have = {x[3] for x in rec["i"] if len(x) > 3}
            more = key in want
            keys = self._name_keys(names)
            goal = 8 if more else 4
            added, tries, failed = 0, 0, False
            # 第一次从第一个词搜起；网页点了“再找找”就换没用过的词。图说明里得提到角色名或演员的姓才要
            for q in [q for q in qs if q not in rec["q"]]:
                if added >= (2 if not more else goal) or tries >= 2:
                    break
                tries += 1
                try:
                    res = self.pin.search(q)
                    nap(1.0, 2.2)
                except SourceError as e:
                    self.fail("pinterest", e)
                    failed = True
                    break
                rec["q"].append(q)
                def score(x):
                    return (-self._match(keys, x["t"])[1], 0 if 0.9 <= x["h"] / max(1, x["w"]) <= 1.9 else 1)
                cands = [x for x in res if x["id"] not in have and x["w"] >= 250 and x["h"] >= 250
                         and 0.5 <= x["h"] / max(1, x["w"]) <= 2.4 and self._match(keys, x["t"])[0]]
                cands.sort(key=score)
                for x in cands:
                    if added >= goal:
                        break
                    try:
                        path, w, h = self._save_img(self.pin.fetch(x["url"]))
                    except (SourceError, OSError, ValueError):
                        continue
                    have.add(x["id"])
                    if any(i[0] == path for i in rec["i"]):
                        continue
                    rec["i"].append([path, w, h, x["id"], x["t"][:60]])
                    added += 1
                    nap(0.2, 0.5)
            if failed and not rec["q"]:
                break             # Pinterest 连不上：这轮先不做了，下次再试
            rec["at"] = now()
            W[key] = rec
            got_any = True
            self.changed = True
        if got_any:
            self.ok("pinterest", f"{len(W)} 位角色有网图")

    # ------------------------------------------------------------ 豆瓣
    def refresh_douban(self, tid, force=False):
        m = self.meta[tid]
        if not force and not self.stale(m, "douban"):
            return False
        series = m.get("type") in ("tvSeries", "tvMiniSeries")
        try:
            if not m.get("dbid"):
                names = self.idx_cn.get(tid, []) + [m.get("title"), m.get("orig")]
                did = self.db.find(names, [m.get("year")])
                m["dbid"] = did or ""     # 没找到的过一阵再找（豆瓣搜索偶尔限流会返回空）
            if not m["dbid"]:
                m.setdefault("at", {})["douban"] = now()
                self.ok("douban")
                return True
            x = self.db.subject(m["dbid"])
        except SourceError as e:
            self.fail("douban", e)
            return True
        title = x["title"]
        m["cn"] = SEASON_RE.sub("", title) if series else title
        m["intro"] = x["intro"]
        m["dgenres"], m["dcountries"], m["dpic"] = x["genres"], x["countries"], x["pic"]
        m["douban"] = {"v": x["v"], "c": x["c"], "reason": x["reason"], "id": x["id"]}
        if series:
            mm = SEASON_RE.search(title)
            m["douban"]["season"] = mm.group(0).strip() if mm else ""
        self.match_people(m, x["people"])
        if series and (m.get("seasons") or 0) > 1:
            self.douban_seasons(m)
        m.setdefault("at", {})["douban"] = now()
        self.changed = True
        self.ok("douban")
        return True

    def douban_seasons(self, m):
        """剧集每一季在豆瓣是单独的条目，逐季找评分（最多 12 季）。"""
        base = m.get("cn") or ""
        if not base:
            return
        old = {s["n"]: s for s in m.get("seasons_db") or []
               if s.get("id") or now() - s.get("miss", 0) < 7 * DAY}
        out = []
        for n in range(1, min(m["seasons"], 12) + 1):
            s = old.get(n) or {"n": n}
            try:
                if "id" not in s:
                    want = norm(f"{base} 第{cn_season(n)}季")
                    hit = None
                    if n == 1 and m.get("douban", {}).get("id") and m["douban"].get("season") in ("", "第一季"):
                        hit = {"id": m["douban"]["id"]}
                    if not hit:
                        hit = next((x for x in self.db.suggest(f"{base} 第{cn_season(n)}季")
                                    if norm(x.get("title")) == want or (n == 1 and norm(x.get("title")) == norm(base))), None)
                    s["id"] = hit["id"] if hit else ""
                    if not hit:
                        s["miss"] = now()
                if s["id"]:
                    if s["id"] == (m.get("douban") or {}).get("id"):
                        s["v"], s["c"] = m["douban"]["v"], m["douban"]["c"]
                    else:
                        x = self.db.subject(s["id"])
                        s["v"], s["c"] = x["v"], x["c"]
            except SourceError as e:
                self.fail("douban", e)
                out.append(s)
                continue
            out.append(s)
        m["seasons_db"] = out

    def match_people(self, m, dpeople):
        """豆瓣的演职员表按英文名对上 IMDb 的人，拿中文名和头像。"""
        if not dpeople:
            return
        by = {}
        for p in dpeople:
            if p.get("en"):
                by.setdefault(norm(p["en"]), p)
        for p in (m.get("directors") or []) + (m.get("cast") or []):
            hit = by.get(norm(p["n"]))
            if hit:
                if hit.get("role") and p in (m.get("cast") or []):
                    p["role_cn"] = hit["role"]       # 豆瓣的中文角色名（宇宙 / 系列的角色卡用）
                rec = self.people.setdefault(p["id"], {})
                if hit["cn"] and hit["cn"] != p["n"]:
                    rec["cn"] = hit["cn"]
                if hit["img"] and "default" not in hit["img"]:
                    rec["dimg"] = hit["img"]

    # ------------------------------------------------------------ 烂番茄
    def refresh_rt(self, tid, force=False):
        m = self.meta[tid]
        if not force and not self.stale(m, "rt"):
            return False
        series = m.get("type") in ("tvSeries", "tvMiniSeries")
        try:
            if not m.get("rtslug"):
                m["rtslug"] = self.rt.find(m.get("title") or "", [m.get("year")], tv=series) or ""
            sc = self.rt.scores(m["rtslug"]) if m["rtslug"] else None
            self.ok("rt")
        except SourceError as e:
            self.fail("rt", e)
            return True
        m["rt"] = {k: sc[k] for k in ("critics", "cc", "audience")} if sc else None
        m.setdefault("at", {})["rt"] = now()
        self.changed = True
        return True

    def img_ok(self, url):
        try:
            r = self.db.s.get(url, timeout=12, stream=True,
                              headers={"Referer": "https://github.io/", "User-Agent": self.db.s.headers["User-Agent"]})
            ok = r.status_code == 200 and r.headers.get("content-type", "").startswith("image")
            r.close()
            return ok
        except Exception:
            return True       # 网络问题不算图坏

    # ------------------------------------------------------------ 推送（Bark，可选：仓库 Secrets 里加 BARK_KEY 才会推）
    def push(self, key, title, body):
        """同一件事只推一次（记在 status.json 的 pushed 里）。"""
        import os
        bark = (os.environ.get("BARK_KEY") or "").strip()
        sent = self.status.setdefault("pushed", {})
        if not bark or key in sent:
            return
        try:
            import requests
            from urllib.parse import quote
            base = bark if bark.startswith("http") else f"https://api.day.app/{bark}"
            r = requests.get(f"{base.rstrip('/')}/{quote(title, safe='')}/{quote(body, safe='')}",
                             params={"group": "影库", "icon": "https://z2vn7g8nhp-beep.github.io/movie-library/icon-192.png"}, timeout=15)
            if r.ok:
                sent[key] = iso()
        except Exception as e:      # 推送失败不影响补全
            print("推送失败", e)
        for k in [k for k, v in sent.items() if v < iso_days_ago(400)]:
            del sent[k]

    def push_birthdays(self, follows):
        """追的人今天生日（北京时间 8 点以后的那一轮推）。"""
        bj = datetime.now(timezone(timedelta(hours=8)))
        if bj.hour < 8:
            return
        for nm in follows:
            P = self.persons.get(nm) or {}
            b = (P.get("birth") or "").split("-")
            if len(b) == 3 and not P.get("death") and int(b[1]) == bj.month and int(b[2]) == bj.day:
                name = (self.people.get(nm) or {}).get("cn") or P.get("n") or nm
                age = bj.year - int(b[0]) if b[0].isdigit() else 0
                self.push(f"bday:{nm}:{bj.year}", f"🎂 今天是{name}的生日", f"{name} {age} 岁啦，去影库重温一部 TA 的作品吧")

    def dedupe_imgs(self, imgs, old_hash):
        """IMDb 相册里常有同一张图传了好几次（海报、剧照），按缩略图的指纹去重。没装 Pillow 就原样返回。"""
        try:
            from io import BytesIO
            from PIL import Image
        except ImportError:
            return imgs, old_hash
        hashes, keep, out = {}, [], []
        for it in imgs:
            k = it[0]
            hv = old_hash.get(k)
            if hv is None:
                try:
                    r = self.db.s.get(f"https://m.media-amazon.com/images/M/{k}._V1_UX64_.jpg", timeout=12)
                    im = Image.open(BytesIO(r.content)).convert("L").resize((9, 8))
                    px = im.tobytes()
                    hv = sum(1 << i for i in range(64) if px[i // 8 * 9 + i % 8] > px[i // 8 * 9 + i % 8 + 1])
                except Exception:
                    hv = -1
            hashes[k] = hv
            if hv >= 0 and any(bin(hv ^ o).count("1") <= 5 for o in keep):
                continue          # 和前面某张几乎一样
            if hv >= 0:
                keep.append(hv)
            out.append(it)
        return out, hashes

    # ------------------------------------------------------------ 影人（追的人：完整作品表、照片、简介、获奖）
    def refresh_person(self, nm):
        try:
            x = self.imdb.person(nm)
            self.ok("imdb")
        except SourceError as e:
            self.fail("imdb", e)
            return
        if not x:
            return
        old = self.persons.get(nm) or {}
        x["at"] = now()
        d = None
        try:
            pid = old.get("db", {}).get("pid")
            d = self.db.personage(pid) if pid else self.db.find_person(x["n"], nm)
            self.ok("douban")
        except SourceError as e:
            self.fail("douban", e)
            d = old.get("db")
        if d and d.get("cover") and not self.img_ok(d["cover"]):
            d["cover"] = ""          # 豆瓣有些照片不让外站用，用不了就不存，网页会用 IMDb 的
        if d:
            x["db"] = d
            rec = self.people.setdefault(nm, {})
            if d.get("cn"):
                rec["cn"] = d["cn"]
            if d.get("cover") and "default" not in d["cover"]:
                rec["dimg"] = d["cover"]
        # 之前补过的角色信息（中文片名、中文角色名、角色介绍）原样带过来
        oldc = {c["id"]: c for c in old.get("credits") or []}
        if oldc and nm in {n for n, f in self.follows.items() if not f.get("del")}:     # 作品表里多出来的新片 = 新作官宣
            year = datetime.now().year
            name = (self.people.get(nm) or {}).get("cn") or x.get("n") or nm
            for c in x["credits"]:
                if c["id"] not in oldc and (not c.get("y") or c["y"] >= year) and c.get("ty") in ("movie", "tvSeries", "tvMiniSeries"):
                    t = (self.meta.get(c["id"]) or {}).get("cn") or (self.idx_cn.get(c["id"]) or [""])[0] or c.get("n") or ""
                    self.push(f"new:{nm}:{c['id']}", f"✨ {name} 有新作", f"《{t}》{c.get('y') or '待定'}" + (f" · 饰 {c['role']}" if c.get("role") else ""))
        for c in x["credits"]:
            for k in ("cn", "role_cn", "rintro", "wintro", "dbid", "rat"):
                if k in oldc.get(c["id"], {}) and k not in c:
                    c[k] = oldc[c["id"]][k]
        if old.get("wdat"):
            x["wdat"] = old["wdat"]
        if x.get("imgs"):
            x["imgs"], x["ih"] = self.dedupe_imgs(x["imgs"], old.get("ih") or {})
        # 作品配上中文片名：离线索引 / 已补全的详情 / 豆瓣作品表
        dw = {norm(w["cn"]): w for w in (d or {}).get("works") or []}
        for c in x["credits"]:
            cn = c.get("cn") or (self.meta.get(c["id"]) or {}).get("cn") or (self.idx_cn.get(c["id"]) or [""])[0]
            if cn:
                c["cn"] = cn
                w = dw.get(norm(cn))
                if w and w.get("role") and not c.get("role_cn"):
                    c["role_cn"] = w["role"]
        self.persons[nm] = x
        self.changed = True

    # ------------------------------------------------------------ 追的人：每个角色的中文名和介绍
    def enrich_roles(self, nm, limit):
        """按作品去豆瓣找：中文片名、TA 演的角色中文名、简介里写到这个角色的那一两句。
        每次只做几部（豆瓣不能访问太快），重要的作品先做，几轮之后就齐了。"""
        P = self.persons.get(nm)
        if not P:
            return 0
        cs = [c for c in P.get("credits") or [] if c.get("cats") != ["self"]]
        # 豆瓣编号：已补全的详情里有就用，没有就批量问 Wikidata（30 天内问过的不再问）
        for c in cs:
            if "dbid" not in c and (self.meta.get(c["id"]) or {}).get("dbid"):
                c["dbid"] = self.meta[c["id"]]["dbid"]
        need = [c["id"] for c in cs if "dbid" not in c]
        if need and now() - P.get("wdat", 0) > 30 * DAY:
            try:
                got = self.wd.by_imdb(need)
                self.ok("wikidata")
                for c in cs:
                    if c["id"] in need:
                        c["dbid"] = (got.get(c["id"]) or {}).get("douban", "")
                P["wdat"] = now()
                self.changed = True
            except SourceError as e:
                self.fail("wikidata", e)
        known = set(P.get("known") or [])
        todo = [c for c in cs if c.get("dbid") and now() - c.get("rat", 0) > 120 * DAY]
        todo.sort(key=lambda c: (c["id"] not in known, bool(c.get("eps") and c["eps"] <= 2), -(c.get("v") or 0)))
        cn_name = ((P.get("db") or {}).get("cn") or self.people.get(nm, {}).get("cn") or "").strip()
        done = 0
        for c in todo[:limit]:
            try:
                x = self.db.subject(c["dbid"])
                self.ok("douban")
            except SourceError as e:
                self.fail("douban", e)
                if "限流" in str(e):
                    break
                c["rat"] = now()
                continue
            done += 1
            series = c.get("ty") in ("tvSeries", "tvMiniSeries")
            if x.get("title"):
                c["cn"] = SEASON_RE.sub("", x["title"]) if series else x["title"]
            me = next((p for p in x.get("people") or [] if norm(p.get("en")) == norm(P.get("n"))
                       or (cn_name and p.get("cn") == cn_name)), None)
            role = (me or {}).get("role") or ""
            if role and role not in ("导演", "演员", "编剧"):
                c["role_cn"] = role
            c["rintro"], c["wintro"] = role_intro(x.get("intro") or "", cn_name, c.get("role_cn") or "", P.get("n") or "")
            c["rat"] = now()
            self.changed = True
        return done

    # ------------------------------------------------------------ 在线搜索
    def lookup(self, q):
        q = (q or "").strip()
        res, err = [], ""
        try:
            m = re.search(r"douban\.com/(?:movie/)?subject/(\d+)|^douban:(\d+)$", q)
            if m:
                did = m.group(1) or m.group(2)
                tid = self.wd.by_douban(did)
                if not tid:
                    x = self.db.subject(did)
                    for c in self.imdb.suggest(x.get("orig") or x["title"]):
                        res.append(c)
                else:
                    res = [{"id": tid}]
            else:
                res = self.imdb.suggest(q)
                if re.search(r"[㐀-鿿]", q):
                    # 中文片名：豆瓣找到条目，再用原名去 IMDb 搜
                    for x in self.db.suggest(q)[:3]:
                        for c in self.imdb.suggest(x.get("sub_title") or x.get("title") or "")[:2]:
                            if c["id"] not in {r["id"] for r in res}:
                                c["cn"] = x.get("title")
                                res.append(c)
            self.ok("search")
        except SourceError as e:
            err = str(e)
            self.fail("search", e)
        # 结果补上基本信息
        ids = [r["id"] for r in res][:12]
        self.refresh_base(ids)
        out = []
        for r in res[:12]:
            m = self.meta.get(r["id"]) or {}
            out.append({**r, "n": r.get("n") or m.get("title", ""), "y": r.get("y") or m.get("year"),
                        "img": r.get("img") or m.get("poster", "")})
        save(self.dir / "lookup.json", {"q": q, "at": iso(), "err": err, "results": out})
        self.changed = True

    def clean_imgs(self):
        """img/ 里没有被任何角色用到的图删掉（网图记录被清掉之后留下的）"""
        d = self.dir / "img"
        if not d.is_dir():
            return
        used = {x[0] for r in (self.chars.get("w") or {}).values() for x in r.get("i") or []}
        for f in d.iterdir():
            if f.is_file() and f"img/{f.name}" not in used:
                f.unlink()

    # ------------------------------------------------------------ 主流程
    def run(self, force_ids=(), query=None):
        reqs_ids = [i for i in (self.reqs.get("ids") or []) if re.fullmatch(r"tt\d+", i)]
        # 手动指定豆瓣条目：{"fix": {"tt123": "豆瓣编号或链接"}}
        for tid, did in (self.reqs.get("fix") or {}).items():
            did = re.sub(r"\D", "", re.search(r"(\d{5,})", str(did)).group(1)) if re.search(r"\d{5,}", str(did)) else ""
            if tid in self.meta and did:
                self.meta[tid]["dbid"] = did
                self.meta[tid].pop("seasons_db", None)
                reqs_ids.append(tid)
        query = query or self.reqs.get("q")
        priority = list(dict.fromkeys(list(force_ids) + reqs_ids))
        ids = list(dict.fromkeys(priority + self.active()))

        if query:
            self.lookup(query)
        # 影人：网页点名要的先做，追的人每周刷新一次（看有没有新作官宣）
        want = [n for n in (self.reqs.get("people") or []) if re.fullmatch(r"nm\d+", n)]
        follows = [n for n, f in self.follows.items() if not f.get("del")]
        stale = [n for n in follows if n not in want and (now() - (self.persons.get(n) or {}).get("at", 0) > 7 * DAY
                                                          or "imgs" not in (self.persons.get(n) or {}))]
        for nm in list(dict.fromkeys(want + stale))[:len(want) + 6]:
            self.refresh_person(nm)
        self.push_birthdays(follows)
        # 角色中文名和介绍：点名要的人先多做一些，其余追的人每轮做几部
        left = 36
        for nm in list(dict.fromkeys([n for n in want if n in follows] + follows)):
            if left <= 0:
                break
            left -= self.enrich_roles(nm, min(left, 18 if nm in want else 10))
        self.refresh_base(priority, force=True)
        self.refresh_base(ids)
        self.resolve_ids(ids)
        self.refresh_series(priority)
        self.refresh_comics()
        self.refresh_chars()
        self.refresh_eps(ids, priority)

        budget = self.budget
        for tid in priority + [i for i in ids if i not in priority]:
            m = self.meta.get(tid)
            if not m or m.get("missing"):
                continue
            first = tid in priority or "douban" not in m
            if budget <= 0 and not first:
                break
            used = self.refresh_douban(tid, force=tid in priority)
            used |= self.refresh_rt(tid, force=tid in priority)
            budget -= 1 if used else 0

        # 冷门角色的网图放在最后做（不耽误刚标记的片子补详情），每轮限时
        self.refresh_web()

        # 不在库里、也很久没看的详情清掉，免得 meta.json 越来越大
        keep = set(self.active()) | set(priority)
        for tid in list(self.meta):
            if tid not in keep and now() - (self.meta[tid].get("at") or {}).get("base", 0) > 60 * DAY:
                del self.meta[tid]
                self.changed = True

        save(self.dir / "meta.json", self.meta)
        save(self.dir / "people.json", self.people)
        if self.series:
            self.enrich_series_chars()
            save(self.dir / "series.json", self.series)
        if self.chars:
            save(self.dir / "chars.json", self.chars)
        self.clean_imgs()
        keep_p = set(follows) | set(want)
        for nm in list(self.persons):
            if nm not in keep_p and now() - self.persons[nm].get("at", 0) > 60 * DAY:
                del self.persons[nm]
        save(self.dir / "persons.json", self.persons)
        self.status["updated"] = iso()
        save(self.dir / "status.json", self.status)
        if self.reqs:
            # 不在这里清空 requests.json：跑的这几分钟里网页可能又加了新请求，推送时会被覆盖掉。
            # 记下这次处理了哪些，推送完数据后由 clear_requests.py 对着最新的 requests.json 只删这些
            save(self.dir.parent / "processed_requests.json", self.reqs)
        print(f"库里 {len(self.active())} 部，详情 {len(self.meta)} 部，影人中文名 {len(self.people)} 位")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data", help="私有数据仓库的本地目录")
    ap.add_argument("--idx", default="idx", help="离线索引目录（可选，用来找中文名）")
    ap.add_argument("--ids", default="", help="逗号分隔，强制刷新这些片子")
    ap.add_argument("--query", default="", help="在线搜索")
    ap.add_argument("--budget", type=int, default=30)
    a = ap.parse_args()
    Sync(a.data, a.idx, a.budget).run([x.strip() for x in a.ids.split(",") if x.strip()], a.query or None)
