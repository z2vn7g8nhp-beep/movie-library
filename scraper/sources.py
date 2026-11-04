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
            rows = self._q("SELECT ?imdb ?rt ?db WHERE { VALUES ?imdb { %s } ?f wdt:P345 ?imdb . "
                           "OPTIONAL { ?f wdt:P1258 ?rt } OPTIONAL { ?f wdt:P4529 ?db } }" % values)
            for row in rows:
                d = out.setdefault(row["imdb"]["value"], {})
                if "rt" in row and re.match(r"(m|tv)/", row["rt"]["value"]):
                    d.setdefault("rt", row["rt"]["value"])
                if "db" in row:
                    d.setdefault("douban", row["db"]["value"])
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
                              "img": ((c.get("avatar") or {}).get("normal") or "")}
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
