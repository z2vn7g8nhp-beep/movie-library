"""数据源：IMDb（GraphQL 详情 + 搜索建议）、豆瓣（rexxar 接口）、烂番茄（网页）、Wikidata（编号互查）。

都不是开放给第三方的正式接口，改版后可能失效；只做个人低频使用。
"""
import json
import random
import re
import time

import requests

UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
POSTER_PREFIX = "https://m.media-amazon.com/images/M/"


class SourceError(Exception):
    pass


def norm(s):
    s = re.sub(r"[​-‏‪-‮⁠﻿]", "", (s or "")).lower()
    s = s.replace("&", "and")
    return re.sub(r"[\s:：·・,，.。!！?？'\"“”‘’《》()（）\[\]【】\-—_/、~～]", "", s)


SEASON_RE = re.compile(r"\s*(第[一二三四五六七八九十百\d]+季|Season\s*\d+)\s*$", re.I)


def strip_season(s):
    return SEASON_RE.sub("", s or "")


def nap(a=0.3, b=0.9):
    time.sleep(random.uniform(a, b))


def img_key(url):
    """IMDb 图片只存中间那段，前端按需要的尺寸拼回去。"""
    if url and url.startswith(POSTER_PREFIX):
        return re.sub(r"\._V1_.*$", "", url[len(POSTER_PREFIX):])
    return ""


# ---------------------------------------------------------------- IMDb
class IMDb:
    GQL = "https://api.graphql.imdb.com/"
    HEADERS = {"User-Agent": UA, "content-type": "application/json",
               "x-imdb-client-name": "imdb-web-next-localized",
               "x-imdb-user-language": "en-US", "x-imdb-user-country": "US"}
    DETAIL = """query($ids:[ID!]!){ titles(ids:$ids){
      id titleText{text} originalTitleText{text} releaseYear{year endYear}
      releaseDate{year month day} titleType{id} runtime{seconds} genres{genres{text}}
      ratingsSummary{aggregateRating voteCount} plot{plotText{plainText}}
      primaryImage{url} countriesOfOrigin{countries{id text}} spokenLanguages{spokenLanguages{id text}}
      episodes{ seasons{number} episodes(first:1){total} }
      directors: credits(first:3, filter:{categories:["director"]}){edges{node{name{id nameText{text} primaryImage{url}}}}}
      creators: credits(first:3, filter:{categories:["creator"]}){edges{node{name{id nameText{text} primaryImage{url}}}}}
      cast: credits(first:18, filter:{categories:["actor","actress","self"]}){edges{node{
        name{id nameText{text} primaryImage{url}} ... on Cast { characters{name} } }}}
    } }"""

    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update(self.HEADERS)

    def _gql(self, query, variables):
        for attempt in range(3):
            try:
                r = self.s.post(self.GQL, json={"query": query, "variables": variables}, timeout=40)
            except requests.RequestException as e:
                err = f"IMDb 连接失败：{e.__class__.__name__}"
            else:
                if r.status_code == 200:
                    d = r.json()
                    if d.get("data"):
                        return d["data"]
                    err = "IMDb 返回错误：" + json.dumps(d.get("errors"), ensure_ascii=False)[:200]
                else:
                    err = f"IMDb 返回 HTTP {r.status_code}"
            time.sleep(2 + attempt * 3)
        raise SourceError(err)

    TIMG = """query($ids:[ID!]!){ titles(ids:$ids){ id
      images(first:100){ edges{ node{ url width height type names{id} } } } } }"""

    def title_images(self, ids):
        """片子的图片：{tt: [[图片编号, 宽, 高, 类型, [图里的人]], ...]}（宇宙专题的角色剧照用）"""
        out = {}
        for i in range(0, len(ids), 8):
            data = self._gql(self.TIMG, {"ids": ids[i:i + 8]})
            for t in data.get("titles") or []:
                if not t:
                    continue
                nodes = ((e or {}).get("node") or {} for e in ((t.get("images") or {}).get("edges") or []))
                out[t["id"]] = [[img_key(n.get("url")), n.get("width") or 0, n.get("height") or 0, n.get("type") or "",
                                 [x["id"] for x in (n.get("names") or []) if x and x.get("id")]]
                                for n in nodes if img_key(n.get("url"))]
        return out

    def details(self, ids):
        out = {}
        for i in range(0, len(ids), 25):
            data = self._gql(self.DETAIL, {"ids": ids[i:i + 25]})
            for t in data.get("titles") or []:
                if t:
                    out[t["id"]] = self._shape(t)
        return out

    @staticmethod
    def _people(block, with_role=False):
        res, seen = [], set()
        for e in ((block or {}).get("edges") or []):
            n = (e.get("node") or {}).get("name") or {}
            if not n.get("id") or n["id"] in seen:
                continue
            seen.add(n["id"])
            p = {"id": n["id"], "n": (n.get("nameText") or {}).get("text", ""),
                 "img": img_key((n.get("primaryImage") or {}).get("url"))}
            if with_role:
                ch = e["node"].get("characters") or []
                if ch:
                    p["role"] = ch[0].get("name", "")
            res.append(p)
        return res

    def _shape(self, t):
        ry, rd = t.get("releaseYear") or {}, t.get("releaseDate") or {}
        rs = t.get("ratingsSummary") or {}
        ep = t.get("episodes") or {}
        ttype = (t.get("titleType") or {}).get("id", "")
        series = ttype in ("tvSeries", "tvMiniSeries")
        rt = (t.get("runtime") or {}).get("seconds")
        d = {
            "id": t["id"], "type": ttype,
            "title": (t.get("titleText") or {}).get("text", ""),
            "orig": (t.get("originalTitleText") or {}).get("text", ""),
            "year": ry.get("year"), "ey": ry.get("endYear"),
            "date": "-".join(f"{x:02d}" if i else str(x) for i, x in enumerate(
                v for v in (rd.get("year"), rd.get("month"), rd.get("day")) if v)) or None,
            "runtime": round(rt / 60) if rt and not series else (round(rt / 60) if rt and rt < 4 * 3600 else None),
            "genres": [g["text"] for g in ((t.get("genres") or {}).get("genres") or [])],
            "plot": ((t.get("plot") or {}).get("plotText") or {}).get("plainText", ""),
            "poster": img_key((t.get("primaryImage") or {}).get("url")),
            "countries": [c["text"] for c in ((t.get("countriesOfOrigin") or {}).get("countries") or [])],
            "langs": [c["text"] for c in ((t.get("spokenLanguages") or {}).get("spokenLanguages") or [])],
            "directors": self._people(t.get("creators") if series else t.get("directors")),
            "cast": self._people(t.get("cast"), True),
            "imdb": {"v": rs.get("aggregateRating"), "c": rs.get("voteCount")},
        }
        if series:
            seasons = sorted({s["number"] for s in (ep.get("seasons") or []) if isinstance(s.get("number"), int)
                              and 0 < s["number"] < 100})
            d["seasons"] = seasons[-1] if seasons else None
            d["episodes"] = ((ep.get("episodes") or {}).get("total"))
        if d["orig"] == d["title"]:
            d["orig"] = ""
        return d

    PERSON = """query($id:ID!){ name(id:$id){ id nameText{text} birthDate{dateComponents{year month day}}
      birthLocation{text} deathDate{dateComponents{year month day}} bio{text{plainText}} primaryImage{url}
      images(first:250){edges{node{url width height type titles{id} names{id}}}}
      knownFor(first:6){edges{node{title{id}}}}
      credits(first:250, filter:{categories:["actor","actress","director","self"]}){ edges{node{ category{id}
        title{id titleText{text} originalTitleText{text} releaseYear{year endYear} titleType{id} primaryImage{url}
              ratingsSummary{aggregateRating voteCount} genres{genres{text}}}
        ... on Cast{ characters{name} episodeCredits(first:1){total} } }}} } }"""
    KEEP_TYPES = {"movie", "tvMovie", "tvSeries", "tvMiniSeries", "tvSpecial", "video", "short"}

    def person(self, nm):
        n = self._gql(self.PERSON, {"id": nm}).get("name")
        if not n:
            return None

        def date(x):
            c = (x or {}).get("dateComponents") or {}
            return "-".join(f"{v:02d}" if i else str(v) for i, v in enumerate(
                v for v in (c.get("year"), c.get("month"), c.get("day")) if v)) or None
        credits = {}
        for e in ((n.get("credits") or {}).get("edges") or []):
            node = e.get("node") or {}
            t = node.get("title") or {}
            ty = (t.get("titleType") or {}).get("id")
            if not t.get("id") or ty not in self.KEEP_TYPES:
                continue
            cat = (node.get("category") or {}).get("id", "")
            cat = "self" if cat == "self" else "director" if cat == "director" else "actor"
            c = credits.get(t["id"])
            if c:      # 同一部又演又导
                if cat == "director" and "director" not in c["cats"]:
                    c["cats"].append("director")
                continue
            ry, rs = t.get("releaseYear") or {}, t.get("ratingsSummary") or {}
            ch = node.get("characters") or []
            credits[t["id"]] = {
                "id": t["id"], "n": (t.get("titleText") or {}).get("text", ""), "ty": ty, "cats": [cat],
                "y": ry.get("year"), "ey": ry.get("endYear"), "role": ch[0].get("name", "") if ch else "",
                "eps": ((node.get("episodeCredits") or {}).get("total")) or None,
                "img": img_key((t.get("primaryImage") or {}).get("url")),
                "r": rs.get("aggregateRating"), "v": rs.get("voteCount") or 0,
                "g": [g["text"] for g in ((t.get("genres") or {}).get("genres") or [])][:3],
            }
        return {
            "id": n["id"], "n": (n.get("nameText") or {}).get("text", ""),
            "birth": date(n.get("birthDate")), "death": date(n.get("deathDate")),
            "place": (n.get("birthLocation") or {}).get("text", ""),
            "bio": (((n.get("bio") or {}).get("text") or {}).get("plainText") or "").strip(),
            "img": img_key((n.get("primaryImage") or {}).get("url")),
            "photos": [img_key((e.get("node") or {}).get("url")) for e in ((n.get("images") or {}).get("edges") or [])
                       if img_key((e.get("node") or {}).get("url"))][:16],
            # 全部图片：[图片编号, 宽, 高, 类型(p 写真 / e 活动 / s 剧照 / o 其他), 关联作品, 图里有几个人]
            "imgs": [[img_key(x.get("url")), x.get("width") or 0, x.get("height") or 0,
                      {"publicity": "p", "event": "e", "still_frame": "s"}.get(x.get("type"), "o"),
                      ((x.get("titles") or [{}])[0] or {}).get("id", ""), len(x.get("names") or [])]
                     for x in ((e.get("node") or {}) for e in ((n.get("images") or {}).get("edges") or []))
                     if img_key(x.get("url"))],
            "known": [e["node"]["title"]["id"] for e in ((n.get("knownFor") or {}).get("edges") or []) if e.get("node")],
            "credits": list(credits.values()),
        }

    def suggest(self, q):
        q = q.strip()
        if not q:
            return []
        slug = re.sub(r"\s+", "_", q.lower())
        try:
            r = self.s.get(f"https://v3.sg.media-imdb.com/suggestion/x/{requests.utils.quote(slug)}.json",
                           timeout=15)
            items = r.json().get("d") or []
        except (requests.RequestException, ValueError) as e:
            raise SourceError(f"IMDb 搜索失败：{e.__class__.__name__}")
        out = []
        for x in items:
            if not str(x.get("id", "")).startswith("tt"):
                continue
            if x.get("qid") not in ("movie", "tvMovie", "tvSeries", "tvMiniSeries", "tvSpecial", "video", "short"):
                continue
            out.append({"id": x["id"], "n": x.get("l", ""), "y": x.get("y"), "ty": x.get("qid"),
                        "yr": x.get("yr") or "", "s": x.get("s", ""),
                        "img": img_key((x.get("i") or {}).get("imageUrl"))})
        return out

    EPS = """query($id:ID!,$after:ID){ title(id:$id){ episodes{ episodes(first:250, after:$after){
      pageInfo{hasNextPage endCursor} edges{ node{ id titleText{text}
        series{ displayableEpisodeNumber{ displayableSeason{text} episodeNumber{text} } }
        releaseDate{year month day} primaryImage{url} ratingsSummary{aggregateRating} } } } } } }"""

    def episodes(self, tt, max_pages=4):
        """剧集的分集表：[[季, 集, 编号, 标题, 首播日期, 剧照, IMDb 分], ...]（按集打卡用）"""
        out, after = [], None
        for _ in range(max_pages):
            t = (self._gql(self.EPS, {"id": tt, "after": after}).get("title") or {})
            block = ((t.get("episodes") or {}).get("episodes")) or {}
            for e in block.get("edges") or []:
                n = e.get("node") or {}
                num = ((n.get("series") or {}).get("displayableEpisodeNumber")) or {}
                try:
                    s = int(((num.get("displayableSeason") or {}).get("text") or "").strip())
                    ep = int(((num.get("episodeNumber") or {}).get("text") or "").strip())
                except ValueError:
                    continue          # 没编号的特别篇、未知季
                if not (0 < s < 100 and 0 < ep < 1000):
                    continue
                d = n.get("releaseDate") or {}
                date = "-".join(f"{x:02d}" if i else str(x) for i, x in enumerate(
                    v for v in (d.get("year"), d.get("month"), d.get("day")) if v))
                r = (n.get("ratingsSummary") or {}).get("aggregateRating")
                out.append([s, ep, n.get("id", ""), (n.get("titleText") or {}).get("text", ""), date,
                            img_key((n.get("primaryImage") or {}).get("url")), r])
            pi = block.get("pageInfo") or {}
            if not pi.get("hasNextPage"):
                break
            after = pi.get("endCursor")
        out.sort(key=lambda x: (x[0], x[1]))
        seen, uniq = set(), []
        for x in out:
            if (x[0], x[1]) not in seen:
                seen.add((x[0], x[1]))
                uniq.append(x)
        return uniq


# ---------------------------------------------------------------- Pinterest（冷门角色的图）
class Pinterest:
    """IMDb 上没有单人剧照、也没有漫画原型的角色，去 Pinterest 搜。
    搜的是网页自己用的接口，不用登录；国内看不了 pinimg，所以挑中的图由后台下载、缩小后存进私有数据仓库。"""
    UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/124.0 Safari/537.36")

    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": self.UA, "Accept-Language": "en-US,en;q=0.9"})
        self.warm = False

    def search(self, q, n=25):
        if not self.warm:
            try:
                self.s.get("https://www.pinterest.com/", timeout=20)
            except requests.RequestException:
                pass
            self.warm = True
        src = f"/search/pins/?q={requests.utils.quote(q)}&rs=typed"
        data = {"options": {"query": q, "scope": "pins", "auto_correction_disabled": False, "rs": "typed", "page_size": n},
                "context": {}}
        try:
            r = self.s.get("https://www.pinterest.com/resource/BaseSearchResource/get/",
                           params={"source_url": src, "data": json.dumps(data, separators=(",", ":"))},
                           headers={"X-Requested-With": "XMLHttpRequest", "Accept": "application/json, text/javascript, */*; q=0.01",
                                    "X-Pinterest-AppState": "active", "X-Pinterest-Source-Url": src,
                                    "X-Pinterest-PWS-Handler": "www/search/[scope].js"}, timeout=25)
            res = (((r.json().get("resource_response") or {}).get("data")) or {}).get("results") or []
        except (requests.RequestException, ValueError) as e:
            raise SourceError(f"Pinterest 搜索失败：{e.__class__.__name__}")
        if r.status_code != 200:
            raise SourceError(f"Pinterest 返回 HTTP {r.status_code}")
        out = []
        for x in res:
            if not isinstance(x, dict) or x.get("type") not in (None, "pin") or x.get("videos") or x.get("is_video"):
                continue
            im = x.get("images") or {}
            big, orig = im.get("736x") or {}, im.get("orig") or {}
            if not big.get("url"):
                continue
            text = " ".join(str(x.get(k) or "") for k in ("title", "grid_title", "description", "auto_alt_text"))
            out.append({"id": str(x.get("id", "")), "url": big["url"], "w": orig.get("width") or big.get("width") or 0,
                        "h": orig.get("height") or big.get("height") or 0, "t": re.sub(r"\s+", " ", text).strip()[:160]})
        return out

    def fetch(self, url):
        try:
            r = self.s.get(url, timeout=30)
        except requests.RequestException as e:
            raise SourceError(f"Pinterest 图片下载失败：{e.__class__.__name__}")
        if r.status_code != 200 or not r.content:
            raise SourceError(f"Pinterest 图片 HTTP {r.status_code}")
        return r.content


# ---------------------------------------------------------------- Wikidata（IMDb ↔ 豆瓣 / 烂番茄）
class Wikidata:
    URL = "https://query.wikidata.org/sparql"

    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": "movie-library/1.0 (personal, non-commercial)",
                               "Accept": "application/sparql-results+json"})

    def _q(self, q):
        try:
            r = self.s.get(self.URL, params={"query": q}, timeout=40)
            return r.json()["results"]["bindings"]
        except (requests.RequestException, ValueError, KeyError) as e:
            raise SourceError(f"Wikidata 查询失败：{e.__class__.__name__}")

    def by_imdb(self, imdb_ids):
        out = {}
        ids = [i for i in imdb_ids if re.fullmatch(r"tt\d+", i or "")]
        for i in range(0, len(ids), 100):
            values = " ".join(f'"{x}"' for x in ids[i:i + 100])
            rows = self._q("SELECT ?imdb ?rt ?db ?zh ?tw WHERE { VALUES ?imdb { %s } ?f wdt:P345 ?imdb . "
                           "OPTIONAL { ?f wdt:P1258 ?rt } OPTIONAL { ?f wdt:P4529 ?db } "
                           'OPTIONAL { ?f rdfs:label ?zh FILTER(lang(?zh) IN ("zh-cn","zh-hans")) } '
                           'OPTIONAL { ?f rdfs:label ?tw FILTER(lang(?tw) IN ("zh","zh-tw","zh-hant","zh-hk")) } }' % values)
            for row in rows:
                d = out.setdefault(row["imdb"]["value"], {})
                if "zh" in row:          # 中文片名：豆瓣找不到条目的老剧、冷门片，至少有个中文名
                    d.setdefault("zh", row["zh"]["value"])
                if "tw" in row:
                    d.setdefault("tw", row["tw"]["value"])
                if "rt" in row and re.match(r"(m|tv)/", row["rt"]["value"]):
                    d.setdefault("rt", row["rt"]["value"])
                if "db" in row:
                    d.setdefault("douban", row["db"]["value"])
        return out

    def series_of(self, imdb_ids):
        """片子属于哪些系列（P179）：{tt: [Q...]}，问过但不属于任何系列的给空列表。"""
        ids = [i for i in imdb_ids if re.fullmatch(r"tt\d+", i or "")]
        out = {i: [] for i in ids}
        for i in range(0, len(ids), 80):
            values = " ".join(f'"{x}"' for x in ids[i:i + 80])
            for row in self._q("SELECT DISTINCT ?imdb ?s WHERE { VALUES ?imdb { %s } ?f wdt:P345 ?imdb . ?f wdt:P179 ?s . "
                               "FILTER NOT EXISTS { ?s wdt:P31 wd:Q13406463 } FILTER NOT EXISTS { ?s wdt:P31 wd:Q12139612 } }" % values):
                q = row["s"]["value"].rsplit("/", 1)[-1]
                lst = out.setdefault(row["imdb"]["value"], [])
                if q not in lst:
                    lst.append(q)
        return out

    def series_members(self, qids):
        """系列的名字和成员：{Q: {"zh", "en", "items": [[tt, 序号, 年份], ...]}}"""
        out = {}
        qids = [q for q in qids if re.fullmatch(r"Q\d+", q)]
        for i in range(0, len(qids), 20):
            values = " ".join("wd:" + q for q in qids[i:i + 20])
            for row in self._q("""SELECT ?s ?zh ?tw ?en WHERE { VALUES ?s { %s }
                OPTIONAL { ?s rdfs:label ?zh FILTER(lang(?zh) IN ("zh-cn","zh-hans")) }
                OPTIONAL { ?s rdfs:label ?tw FILTER(lang(?tw) IN ("zh","zh-tw","zh-hant")) }
                OPTIONAL { ?s rdfs:label ?en FILTER(lang(?en) = "en") } }""" % values):
                q = row["s"]["value"].rsplit("/", 1)[-1]
                d = out.setdefault(q, {"zh": "", "tw": "", "en": "", "items": []})
                d["zh"] = d["zh"] or (row.get("zh") or {}).get("value", "")      # 只放大陆简体名
                d["tw"] = d["tw"] or (row.get("tw") or {}).get("value", "")      # 台港名另放，网页没有大陆名时再用
                d["en"] = d["en"] or (row.get("en") or {}).get("value", "")
            seen = {}
            for row in self._q("""SELECT ?s ?imdb ?ord ?y WHERE { VALUES ?s { %s } ?m p:P179 ?st . ?st ps:P179 ?s .
                ?m wdt:P345 ?imdb . FILTER(STRSTARTS(?imdb, "tt"))
                OPTIONAL { ?st pq:P1545 ?ord } OPTIONAL { ?m wdt:P577 ?d BIND(YEAR(?d) AS ?y) } }""" % values):
                q = row["s"]["value"].rsplit("/", 1)[-1]
                tt = row["imdb"]["value"]
                o = (row.get("ord") or {}).get("value", "")
                y = int(float((row.get("y") or {}).get("value", 0) or 0))
                k = (q, tt)
                if k in seen:
                    it = seen[k]
                    if y and (not it[2] or y < it[2]):
                        it[2] = y
                    if o and not it[1]:
                        it[1] = o
                    continue
                it = seen[k] = [tt, o, y]
                out.setdefault(q, {"zh": "", "en": "", "items": []})["items"].append(it)
        return out

    def series_chars(self, imdb_ids):
        """系列里每部片子的角色（演员 P161 + 角色限定 P453）：
        {角色Q: {"zh", "en", "a": {演员nm: [英文名, 次数]}, "w": {tt: 排序}}}"""
        out = {}
        ids = [i for i in imdb_ids if re.fullmatch(r"tt\d+", i or "")]
        for i in range(0, len(ids), 12):
            values = " ".join(f'"{x}"' for x in ids[i:i + 12])
            rows = self._q("""SELECT ?imdb ?ord ?anm ?an ?char ?zh ?tw ?en WHERE { VALUES ?imdb { %s } ?f wdt:P345 ?imdb .
                ?f p:P161 ?st . ?st ps:P161 ?actor . ?st pq:P453 ?char . OPTIONAL { ?st pq:P1545 ?ord }
                OPTIONAL { ?actor wdt:P345 ?anm } OPTIONAL { ?actor rdfs:label ?an FILTER(lang(?an) = "en") }
                OPTIONAL { ?char rdfs:label ?zh FILTER(lang(?zh) IN ("zh-cn","zh-hans")) }
                OPTIONAL { ?char rdfs:label ?tw FILTER(lang(?tw) IN ("zh","zh-tw","zh-hant","zh-hk")) }
                OPTIONAL { ?char rdfs:label ?en FILTER(lang(?en) = "en") } }""" % values)
            for r in rows:
                q = r["char"]["value"].rsplit("/", 1)[-1]
                if not re.fullmatch(r"Q\d+", q):
                    continue
                c = out.setdefault(q, {"zh": "", "tw": "", "en": "", "a": {}, "w": {}})
                c["zh"] = c["zh"] or (r.get("zh") or {}).get("value", "")
                c["tw"] = c["tw"] or (r.get("tw") or {}).get("value", "")
                c["en"] = c["en"] or (r.get("en") or {}).get("value", "")
                tt = r["imdb"]["value"]
                try:
                    o = int((r.get("ord") or {}).get("value") or 999)
                except ValueError:
                    o = 999
                c["w"][tt] = min(o, c["w"].get(tt, 999))
                nm = (r.get("anm") or {}).get("value", "")
                if re.fullmatch(r"nm\d+", nm):
                    a = c["a"].setdefault(nm, [(r.get("an") or {}).get("value", ""), set()])
                    a[1].add(tt)
        for c in out.values():
            c["a"] = {nm: [n, len(ts)] for nm, (n, ts) in c["a"].items()}
        return out

    def by_douban(self, did):
        rows = self._q('SELECT ?imdb WHERE { ?f wdt:P4529 "%s" . ?f wdt:P345 ?imdb }' % re.sub(r"\D", "", did))
        return rows[0]["imdb"]["value"] if rows else None


# ---------------------------------------------------------------- 豆瓣
class Douban:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": UA, "Referer": "https://m.douban.com/movie/"})

    def _json(self, url, params=None):
        nap(0.8, 1.6)
        try:
            r = self.s.get(url, params=params, timeout=15)
        except requests.RequestException as e:
            raise SourceError(f"豆瓣连接失败：{e.__class__.__name__}")
        if r.status_code in (403, 418, 429):
            raise SourceError(f"豆瓣返回 HTTP {r.status_code}（被限流）")
        if r.status_code == 404:
            return None
        try:
            return r.json()
        except ValueError:
            raise SourceError("豆瓣返回的不是数据（可能要求登录或验证）")

    def suggest(self, q):
        """先用搜索建议接口；它常被限流返回空，空了就改用网页版搜索。"""
        nap(0.4, 1.0)
        try:
            items = self._json("https://movie.douban.com/j/subject_suggest", {"q": q})
        except SourceError:
            items = None
        if isinstance(items, list) and items:
            return items
        return self.web_search(q)

    def web_search(self, q):
        nap(0.8, 1.6)
        try:
            r = self.s.get("https://www.douban.com/search", params={"cat": "1002", "q": q}, timeout=15,
                           headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 "
                                                  "(KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                                    "Referer": "https://www.douban.com/"})
        except requests.RequestException as e:
            raise SourceError(f"豆瓣搜索失败：{e.__class__.__name__}")
        if r.status_code != 200:
            raise SourceError(f"豆瓣搜索返回 HTTP {r.status_code}")
        out = []
        for b in r.text.split('<div class="result">')[1:]:
            sid = re.search(r"sid: (\d+)", b)
            t = re.search(r"<h3>.*?<a [^>]*>\s*([^<]+?)\s*</a>", b, re.S)
            cast = re.search(r'<span class="subject-cast">([^<]*)</span>', b)
            if not sid or not t:
                continue
            c = cast.group(1) if cast else ""
            orig = re.match(r"原名:([^/]+)", c)
            year = re.search(r"(\d{4})\s*$", c)
            out.append({"id": sid.group(1), "title": re.sub(r"\s+", " ", t.group(1)).strip(),
                        "sub_title": orig.group(1).strip() if orig else "", "year": year.group(1) if year else ""})
        return out

    def find(self, names, years):
        """按片名（中文或英文）+ 年份找豆瓣条目，片名要一致，年份差不超过 1 年。
        剧集在豆瓣按季分条目，"第一季" / "Season 1" 去掉后再比。"""
        for name in list(dict.fromkeys(n for n in names if n))[:4]:
            target = norm(name)
            for x in self.suggest(name):
                t, st = norm(strip_season(x.get("title"))), norm(strip_season(x.get("sub_title")))
                if target not in (t, st):
                    continue
                y = int(x["year"]) if str(x.get("year", "")).isdigit() else None
                if years and y and min(abs(y - yy) for yy in years if yy) > 1:
                    continue
                return x["id"]
        return None

    def find_person(self, name, nm):
        """按英文名搜豆瓣影人，逐个核对资料里的 IMDb 编号，对上才算。"""
        nap(0.8, 1.6)
        try:
            r = self.s.get("https://www.douban.com/search", params={"cat": "1065", "q": name}, timeout=15,
                           headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 "
                                                  "(KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                                    "Referer": "https://www.douban.com/"})
        except requests.RequestException as e:
            raise SourceError(f"豆瓣影人搜索失败：{e.__class__.__name__}")
        ids = re.findall(r"sid: (\d+)", r.text)
        for pid in list(dict.fromkeys(ids))[:3]:
            d = self.personage(pid)
            if d and d.get("imdb") == nm:
                return d
        return None

    def personage(self, pid):
        d = self._json(f"https://m.douban.com/rexxar/api/v2/elessar/subject/{pid}", {"ck": "", "for_mobile": 1})
        if not d or not d.get("title"):
            return None
        info = {k: v for k, v in ((d.get("extra") or {}).get("info") or []) if isinstance(k, str)}
        desc = d.get("desc") or ""
        m = re.search(r'<div class="content">(.*?)</div>', desc, re.S)
        bio = re.sub(r"<[^>]+>", "", re.sub(r"</p>\s*<p>", "\n", m.group(1))).strip() if m else ""
        mods = {x.get("type"): x.get("payload") or {} for x in d.get("modules") or []}
        works = []
        for c in (mods.get("work_collections") or {}).get("collections") or []:
            for w in c.get("works") or []:
                sub = w.get("subject") or {}
                role = (w.get("roles") or [""])[0]
                rm = re.search(r"饰\s*([^)）]+)", role)
                works.append({"cn": sub.get("title", ""), "role": rm.group(1).strip() if rm else "", "id": sub.get("id")})
        photos = [((p.get("image") or {}).get("large") or {}).get("url") for p in (mods.get("photos") or {}).get("photos") or []]
        awards = []
        for a in (mods.get("award_result_collection") or {}).get("awards") or []:
            cer = a.get("ceremony") or {}
            awards.append({"won": bool(a.get("is_won")), "ceremony": cer.get("title", ""), "year": cer.get("year"),
                           "cat": (a.get("category") or {}).get("title", ""), "work": (a.get("subject") or {}).get("title", "")})
        return {"pid": str(d.get("id")), "cn": d.get("title", ""), "en": d.get("latin_title", ""),
                "imdb": (info.get("IMDb编号") or "").strip(), "birth": info.get("出生日期", ""), "place": info.get("出生地", ""),
                "family": info.get("家庭成员", ""), "bio": bio, "cover": ((d.get("cover") or {}).get("large") or {}).get("url", ""),
                "photos": [p for p in photos if p][:16], "awards": awards, "works": works,
                "awardsTotal": (mods.get("award_result_collection") or {}).get("total")}

    def subject(self, did):
        """电影、剧集共用：先按电影查，没有再按剧集查。"""
        for kind in ("movie", "tv"):
            d = self._json(f"https://m.douban.com/rexxar/api/v2/{kind}/{did}", {"ck": "", "for_mobile": 1})
            if d and d.get("title"):
                break
        else:
            raise SourceError(f"豆瓣条目 {did} 无数据")
        rt = d.get("rating") or {}
        out = {
            "id": str(did), "kind": kind, "title": d.get("title", ""), "orig": d.get("original_title", ""),
            "genres": d.get("genres") or [], "countries": d.get("countries") or [],
            "intro": (d.get("intro") or "").strip(), "pic": ((d.get("pic") or {}).get("large") or ""),
            "v": float(rt.get("value") or 0) or None, "c": int(rt.get("count") or 0),
            "reason": d.get("null_rating_reason") or "", "eps": d.get("episodes_count") or None,
        }
        try:
            cel = self._json(f"https://m.douban.com/rexxar/api/v2/{kind}/{did}/celebrities",
                             {"ck": "", "for_mobile": 1}) or {}
            out["people"] = [{"cn": c.get("name", ""), "en": c.get("latin_name", ""),
                              "img": ((c.get("avatar") or {}).get("normal") or ""),
                              "role": re.sub(r"^饰\s*", "", (c.get("character") or "").strip())}
                             for k in ("directors", "actors") for c in (cel.get(k) or [])]
        except SourceError:
            out["people"] = []
        return out


# ---------------------------------------------------------------- 烂番茄
class RottenTomatoes:
    BASE = "https://www.rottentomatoes.com"

    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 "
                                             "(KHTML, like Gecko) Version/17.0 Safari/605.1.15"})

    def _html(self, url, params=None):
        nap(0.6, 1.2)
        try:
            r = self.s.get(url, params=params, timeout=20)
        except requests.RequestException as e:
            raise SourceError(f"烂番茄连接失败：{e.__class__.__name__}")
        if r.status_code == 404:
            return None
        if r.status_code != 200:
            raise SourceError(f"烂番茄返回 HTTP {r.status_code}")
        return r.text

    def find(self, title, years, tv=False):
        html = self._html(self.BASE + "/search", {"search": title})
        if not html:
            return None
        target = norm(title)
        kind = "tv" if tv else "m"
        for attrs, body in re.findall(r"<search-page-media-row([^>]*)>(.*?)</search-page-media-row>", html, re.S):
            a = dict(re.findall(r'([a-z-]+)="([^"]*)"', attrs))
            url = re.search(r'href="https://www\.rottentomatoes\.com/(%s/[^"/?]+)' % kind, body)
            name = re.search(r'data-qa="info-name"[^>]*>\s*([^<]+?)\s*<', body)
            if not url or not name or norm(name.group(1)) != target:
                continue
            y = a.get("release-year") or (a.get("start-year") if tv else None)
            if years and y and y.isdigit() and min(abs(int(y) - yy) for yy in years if yy) > 1:
                continue
            return url.group(1)
        return None

    def scores(self, slug):
        html = self._html(f"{self.BASE}/{slug}")
        if html is None:
            return None
        m = re.search(r'<script[^>]*id="media-scorecard-json"[^>]*>(.*?)</script>', html, re.S)
        if not m:
            raise SourceError("烂番茄页面结构变了")
        d = json.loads(m.group(1))

        def pct(x):
            v = str((x or {}).get("scorePercent") or "")
            return int(v.rstrip("%")) if v.rstrip("%").isdigit() else None
        cs, aus = d.get("criticsScore") or {}, d.get("audienceScore") or {}
        return {"critics": pct(cs), "cc": cs.get("reviewCount") or cs.get("ratingCount"),
                "audience": pct(aus), "slug": slug}


# ---------------------------------------------------------------- 漫画原型（自动系列用）
class Comics:
    """给后台自动找到的系列（X 战警、蜘蛛侠三部曲……）里的角色配漫画原型。
    先按名字对 SuperHero API（图 + 六维数值），对不上的再去 Marvel / DC 维基（fandom）找主宇宙那一页的图。"""
    ALL = ["https://akabab.github.io/superhero-api/api/all.json",
           "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"]
    # 不是漫威 / DC 的出版方（这些角色一律不要）；其余奇怪的出版方字段多半是漫威 / DC 角色的别名，算“不确定”
    NOT_MD = {"Dark Horse Comics", "George Lucas", "NBC - Heroes", "Star Trek", "SyFy", "", None, "Icon Comics", "ABC Studios",
              "IDW Publishing", "Shueisha", "Image Comics", "Sony Pictures", "Wildstorm", "South Park", "Universal Studios",
              "J. K. Rowling", "Titan Books", "Rebellion", "Microsoft", "J. R. R. Tolkien"}
    WIKI = {"M": ("https://marvel.fandom.com/api.php", ["Earth-616"]),
            "D": ("https://dc.fandom.com/api.php", ["Prime Earth", "New Earth"])}

    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": "movie-library/1.0 (personal film log)"})
        self.idx = None

    @staticmethod
    def nz(s):
        import unicodedata
        s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
        s = re.sub(r"\(.*?\)", " ", s).strip()
        s = re.sub(r"^(dr|doctor|professor|prof|mr|mrs|ms|miss)\.?\s+", "", s)   # 只去称呼；Captain / Lady 是名字的一部分
        return re.sub(r"[^a-z0-9]+", "", s)

    def load(self):
        if self.idx is not None:
            return
        data = None
        for u in self.ALL:
            try:
                r = self.s.get(u, timeout=40)
                if r.status_code == 200:
                    data = r.json()
                    break
            except (requests.RequestException, ValueError):
                continue
        if data is None:
            raise SourceError("SuperHero API 连不上")
        clean = lambda x: "" if (not x or x in ("-", "null", "No alter egos found.", "0 cm", "0 kg")) else x
        self.idx = {}
        for h in data:
            b, a, ps = h["biography"], h["appearance"], h["powerstats"]
            pub = b.get("publisher")
            if pub in self.NOT_MD:
                continue
            g = "M" if pub == "Marvel Comics" else "D" if pub == "DC Comics" else "?"
            cm = {"s": h["slug"], "n": h["name"],
                  "ps": [ps[x] for x in ("intelligence", "strength", "speed", "durability", "power", "combat")],
                  "fn": clean(b.get("fullName")), "fa": clean(b.get("firstAppearance")), "al": clean(b.get("alignment")),
                  "race": clean(a.get("race")), "h": clean((a.get("height") or ["", ""])[1]), "wt": clean((a.get("weight") or ["", ""])[1])}
            full = b.get("fullName") or ""
            # 真名对上了、但这张是以 TA 命名的平行宇宙变体（Gwen Stacy → Spider-Gwen）：先去维基找本人
            first = (full.split() or [""])[0].lower()
            variant = bool(first) and len(first) >= 3 and first in h["name"].lower()
            keys = [(0, h["name"]), (3 if variant else 1, full)]
            fn = re.sub(r"\(.*?\)", "", full).split()
            if len(fn) >= 2 and not re.search(r"['\"“”‘’]", full):   # Charles Francis Xavier → Charles Xavier；Jean Grey-Summers → Jean Grey
                keys += [(3 if variant else 1.5, f"{fn[0]} {fn[-1]}"), (3 if variant else 1.5, f"{fn[0]} {fn[-1].split('-')[0]}")]
            keys += [(2, x) for x in (b.get("aliases") or []) if x and " " not in x.strip()]   # 别名只认单个词（多词别名常是冒充过的人）
            for pri, nm in keys:
                k = self.nz(nm)
                if len(k) >= 4:
                    self.idx.setdefault(k, []).append((pri, h["id"], g, cm))

    def cands(self, c):
        out = []
        for nm in (c.get("en"), c.get("db")):
            k = self.nz(nm)
            if len(k) >= 4:
                out += self.idx.get(k, [])
        numbered = lambda x: bool(re.search(r"\s(II|III|IV|V)$", x[3]["n"]))   # Batman II、Flash IV 往后放
        return sorted(out, key=lambda x: (x[0], numbered(x), x[1]))

    def wiki(self, g, names):
        """维基上主宇宙那一页的配图（只认 “真名 (Earth-616)” 这种页，不搜，免得拿到电影版剧照）"""
        api, earths = self.WIKI[g]
        titles = [f"{n} ({e})" for n in names for e in earths if n and re.fullmatch(r"[A-Za-z][A-Za-z .'\-]+", n)]
        if not titles:
            return None
        try:
            r = self.s.get(api, params={"action": "query", "titles": "|".join(titles[:6]), "prop": "pageimages", "piprop": "thumbnail",
                                        "pithumbsize": 480, "redirects": 1, "format": "json"}, timeout=25)
            qd = r.json().get("query") or {}
        except (requests.RequestException, ValueError) as e:
            raise SourceError(f"漫画维基连不上：{e.__class__.__name__}")
        pages = qd.get("pages") or {}
        by = {p.get("title"): p for p in pages.values()}
        hop = {x["from"]: x["to"] for x in (qd.get("normalized") or []) + (qd.get("redirects") or [])}   # Betty Brant → Elizabeth Brant
        for t in titles:
            u = t
            for _ in range(3):
                u = hop.get(u, u)
            p = by.get(u)
            if p and (p.get("thumbnail") or {}).get("source"):
                th = p["thumbnail"]
                return {"img": th["source"], "pg": p["title"], "w": th.get("width"), "h": th.get("height")}
        return None

    def series(self, chars, only=None):
        """一个系列的角色表 → {角色 Q 号: 漫画原型 or None}；不像漫威 / DC 系列的整组返回空。
        only：只给这些角色查维基（别的已经查过了）"""
        self.load()
        picks = {c["k"]: self.cands(c) for c in chars}
        firm = [p[0] for p in picks.values() if p and p[0][0] <= 1.5]
        votes = {"M": 0, "D": 0}
        for p in firm:
            if p[2] in votes:
                votes[p[2]] += 1
        g = "M" if votes["M"] >= votes["D"] else "D"
        n_hit = sum(1 for p in picks.values() if any(x[2] in (g, "?") for x in p))
        if votes[g] < 2 or n_hit < 3 or n_hit < len(chars) * .2:
            return {}
        out = {}
        for c in chars:
            ok = [x for x in picks[c["k"]] if x[2] in (g, "?")]
            out[c["k"]] = dict(ok[0][3]) if ok and ok[0][0] < 3 else None
            if out[c["k"]] is None and (only is None or c["k"] in only):   # 对不上的：去维基按真名找（变体卡不拿来顶替本人）
                out[c["k"]] = self.wiki(g, [c.get("en"), c.get("db")])
                time.sleep(.3)
        return out
