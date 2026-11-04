"""后台主流程：读私有仓库里的标记，补全详情，定期刷新三家评分，处理在线搜索。

私有数据仓库（data/）里的文件：
  marks.json     你的标记（网页写，这里只读）
  requests.json  网页提交的待办：要补全的片子、在线搜索（这里处理完清空）
  meta.json      每部片子的详情和评分（这里写）
  people.json    影人的中文名和头像（这里写）
  lookup.json    最近一次在线搜索的结果（这里写）
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
from sources import IMDb, Wikidata, Douban, RottenTomatoes, SourceError, norm  # noqa: E402

CST = timezone(timedelta(hours=8))
DAY = 86400
SEASON_RE = re.compile(r"\s*第[一二三四五六七八九十百\d]+季\s*$")
CN_NUM = "零一二三四五六七八九十"


def now():
    return time.time()


def iso():
    return datetime.now(CST).isoformat(timespec="seconds")


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
        self.follows = load(self.dir / "marks.json", {}).get("follows", {})
        self.reqs = load(self.dir / "requests.json", {})
        self.status = load(self.dir / "status.json", {"sources": {}})
        self.idx_cn = load_index_cn(idx) if idx else {}
        self.budget = budget          # 每次最多访问豆瓣 / 烂番茄多少部，别太频繁
        self.imdb, self.wd, self.db, self.rt = IMDb(), Wikidata(), Douban(), RottenTomatoes()
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
                and ("dbid" not in self.meta[i] or "rtslug" not in self.meta[i])]
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
        if d:
            x["db"] = d
            rec = self.people.setdefault(nm, {})
            if d.get("cn"):
                rec["cn"] = d["cn"]
            if d.get("cover") and "default" not in d["cover"]:
                rec["dimg"] = d["cover"]
        # 作品配上中文片名：离线索引 / 已补全的详情 / 豆瓣作品表
        dw = {norm(w["cn"]): w for w in (d or {}).get("works") or []}
        for c in x["credits"]:
            cn = (self.meta.get(c["id"]) or {}).get("cn") or (self.idx_cn.get(c["id"]) or [""])[0]
            if cn:
                c["cn"] = cn
                w = dw.get(norm(cn))
                if w and w.get("role"):
                    c["role_cn"] = w["role"]
        self.persons[nm] = x
        self.changed = True

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
        stale = [n for n in follows if n not in want and now() - (self.persons.get(n) or {}).get("at", 0) > 7 * DAY]
        for nm in list(dict.fromkeys(want + stale))[:len(want) + 6]:
            self.refresh_person(nm)
        self.refresh_base(priority, force=True)
        self.refresh_base(ids)
        self.resolve_ids(ids)

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

        # 不在库里、也很久没看的详情清掉，免得 meta.json 越来越大
        keep = set(self.active()) | set(priority)
        for tid in list(self.meta):
            if tid not in keep and now() - (self.meta[tid].get("at") or {}).get("base", 0) > 60 * DAY:
                del self.meta[tid]
                self.changed = True

        save(self.dir / "meta.json", self.meta)
        save(self.dir / "people.json", self.people)
        keep_p = set(follows) | set(want)
        for nm in list(self.persons):
            if nm not in keep_p and now() - self.persons[nm].get("at", 0) > 60 * DAY:
                del self.persons[nm]
        save(self.dir / "persons.json", self.persons)
        self.status["updated"] = iso()
        save(self.dir / "status.json", self.status)
        if self.reqs:
            save(self.dir / "requests.json", {})
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
