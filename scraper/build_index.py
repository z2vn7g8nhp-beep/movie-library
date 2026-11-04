"""用 IMDb 官方数据集生成手机端的离线片库索引。

输出到 out/idx/：
  s1.txt s2.txt 搜索用：编号、类型、年份、片名、中文名、类型、评分（s1 是最热门的一批，先加载）
  names.txt    可搜索的影人
  p/N.txt      海报、片长、主创（按编号分 512 片，打开详情时按需加载）
  n/N.txt      影人作品（分 256 片，打开影人页时加载）
  info.json    生成时间、数量

数据集说明：https://developer.imdb.com/non-commercial-datasets/ （仅限个人非商业使用）
"""
import argparse
import gzip
import json
import os
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

DS = "https://datasets.imdbws.com/"
TYPES = {"movie": "m", "tvMovie": "tm", "tvSeries": "s", "tvMiniSeries": "ms", "tvSpecial": "sp", "video": "v"}
GENRES = ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama",
          "Family", "Fantasy", "Film-Noir", "Game-Show", "History", "Horror", "Music", "Musical", "Mystery",
          "News", "Reality-TV", "Romance", "Sci-Fi", "Short", "Sport", "Talk-Show", "Thriller", "War", "Western"]
GBIT = {g: 1 << i for i, g in enumerate(GENRES)}
ZH_REGIONS = {"CN", "TW", "HK", "SG", "MO"}
ZH_LANGS = {"zh", "cmn", "yue", "zh-Hans", "zh-Hant"}
SHARDS = 512
NSHARDS = 256
TIER1 = 40000          # 最热门的这些先加载，搜索马上能用
POSTER_PREFIX = "https://m.media-amazon.com/images/M/"


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def ds_lines(src, name):
    path = Path(src) / f"{name}.tsv.gz"
    if not path.exists():
        log("下载", name)
        path.parent.mkdir(parents=True, exist_ok=True)
        with requests.get(DS + f"{name}.tsv.gz", stream=True, timeout=120) as r:
            r.raise_for_status()
            with open(path, "wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
    f = gzip.open(path, "rt", encoding="utf-8", newline="\n")
    next(f)
    return f


def clean(s):
    return (s or "").replace("\t", " ").replace("\n", " ").strip()


def has_cjk(s):
    return bool(re.search(r"[㐀-鿿]", s or ""))


def hotness(r):
    """排序用：打分人数，和热度排名换算的分数，取大的。"""
    return max(r["v"], 3_000_000 // (r["h"] + 10) if r["h"] != "" else 0)


def build(src, out, min_votes, min_votes_zh, poster_cache, no_posters, hot_n=3000):
    t0 = time.time()
    posters = {}
    import opencc
    t2s = opencc.OpenCC("t2s")

    # 0. 近期和待映的热门片（上映前 IMDb 不让打分，按打分人数会漏掉，所以按热度另取）
    hot = fetch_hot(hot_n) if hot_n else {}
    log("近期热门", len(hot))

    # 1. 评分
    votes, rating = {}, {}
    for l in ds_lines(src, "title.ratings"):
        t, r, v = l.rstrip("\n").split("\t")
        votes[t] = int(v)
        rating[t] = r
    log("评分", len(votes))

    # 2. 中文片名（先扫 akas：门槛对有中文名的片子放宽）
    zh = defaultdict(dict)   # tt -> {"cn": 大陆名, "alt": set(其他中文名)}
    for l in ds_lines(src, "title.akas"):
        p = l.rstrip("\n").split("\t")
        tid, title, region, lang, types = p[0], p[2], p[3], p[4], p[5]
        if votes.get(tid, 0) < min_votes_zh and tid not in hot:
            continue
        if region not in ZH_REGIONS and lang not in ZH_LANGS:
            continue
        if not has_cjk(title) or "working" in types:
            continue
        d = zh[tid]
        title = clean(title)
        if region == "CN" and ("cn" not in d or "imdbDisplay" in types):
            d["cn"] = t2s.convert(title)
        d.setdefault("alt", set()).add(t2s.convert(title))
    log("中文名", len(zh))

    # 3. 片目
    rows = {}
    for l in ds_lines(src, "title.basics"):
        p = l.rstrip("\n").split("\t")
        tid, ttype, primary, original, adult, sy, ey, rt, genres = p
        if ttype not in TYPES or adult == "1":
            continue
        v = votes.get(tid, 0)
        need = min_votes * {"tvSeries": .75, "tvMiniSeries": .75, "tvSpecial": 4, "video": 1.5}.get(ttype, 1)
        if v < need and not (tid in zh and v >= min_votes_zh) and tid not in hot:
            continue
        gm = 0
        for g in genres.split(","):
            gm |= GBIT.get(g, 0)
        d = zh.get(tid, {})
        cn = d.get("cn", "")
        alt = sorted(a for a in d.get("alt", ()) if a != cn)
        if not cn and alt:          # 没有大陆译名就用台港译名（已转简体）
            cn, alt = alt[0], alt[1:]
        rows[tid] = {
            "t": TYPES[ttype], "y": sy if sy != "\\N" else "", "ey": ey if ey != "\\N" else "",
            "n": clean(primary), "o": clean(original) if original != primary else "",
            "cn": cn, "alt": "|".join(alt[:2]), "g": gm, "r": rating.get(tid, ""), "v": v,
            "rt": rt if rt != "\\N" else "", "d": [], "c": [], "h": hot[tid]["rank"] if tid in hot else "",
        }
    # 数据集里还没有的新条目，直接用接口拿到的信息
    for tid, h in hot.items():
        if tid not in rows and h["type"] in TYPES:
            gm = 0
            for g in h["genres"]:
                gm |= GBIT.get(g, 0)
            d = zh.get(tid, {})
            rows[tid] = {"t": TYPES[h["type"]], "y": str(h["year"] or ""), "ey": "", "n": clean(h["title"]),
                         "o": clean(h["orig"]) if h["orig"] != h["title"] else "", "cn": d.get("cn", ""),
                         "alt": "|".join(sorted(d.get("alt", ()))[:2]), "g": gm, "r": str(h["rating"] or ""),
                         "v": h["votes"] or 0, "rt": str(h["runtime"] or ""), "d": [], "c": [], "h": h["rank"]}
        if h.get("poster"):
            posters.setdefault(tid, h["poster"])
    del zh
    log("收录", len(rows))

    # 4. 主创：导演 / 主创（剧集）+ 前 4 位演员
    for l in ds_lines(src, "title.principals"):
        tid = l[:l.index("\t")]
        row = rows.get(tid)
        if row is None:
            continue
        p = l.split("\t", 4)
        cat = p[3]
        if p[2] in row["d"] or p[2] in row["c"]:
            continue
        if cat == "director" and len(row["d"]) < 2:
            row["d"].append(p[2])
        elif cat in ("actor", "actress", "self") and len(row["c"]) < 4:
            row["c"].append(p[2])
    if True:  # 剧集的导演是分集导演，没意义；用 crew 里的 writer 也不准，剧集只留演员
        for row in rows.values():
            if row["t"] in ("s", "ms"):
                row["d"] = []
    log("主创完成")

    # 5. 影人名
    need = set()
    for row in rows.values():
        need.update(row["d"])
        need.update(row["c"])
    names = {}
    for l in ds_lines(src, "name.basics"):
        nid = l[:l.index("\t")]
        if nid in need:
            p = l.split("\t", 3)
            names[nid] = clean(p[1])
    log("影人", len(names))

    # 6. 海报（IMDb 接口批量查，只查缓存里没有的）
    if poster_cache and Path(poster_cache).exists():
        for f in Path(poster_cache).glob("*.txt"):
            for line in f.read_text(encoding="utf-8").splitlines():
                p = line.split("\t")
                if len(p) > 1 and p[1]:
                    posters["tt" + p[0]] = p[1]
        log("已有海报缓存", len(posters))
    if not no_posters:
        fetch_posters([t for t in rows if t not in posters], posters)

    # 7. 写出
    out = Path(out)
    for sub in ("p", "n"):
        (out / sub).mkdir(parents=True, exist_ok=True)
    order = sorted(rows, key=lambda t: -hotness(rows[t]))   # 热门在前，搜索同分时自然靠前
    tier1 = {t for t in order[:TIER1]}
    with open(out / "s1.txt", "w", encoding="utf-8") as f1, open(out / "s2.txt", "w", encoding="utf-8") as f2:
        for tid in order:
            r = rows[tid]
            (f1 if tid in tier1 else f2).write("\t".join([
                tid[2:], r["t"], r["y"], r["ey"], r["n"], r["o"], r["cn"], r["alt"],
                format(r["g"], "x"), r["r"], str(r["v"]), str(r["h"])]) + "\n")

    def ppl(ids):
        return "|".join(f"{x[2:]}:{names[x]}" for x in ids if x in names)
    shards = defaultdict(list)
    for tid, r in rows.items():
        shards[int(tid[2:]) % SHARDS].append("\t".join([tid[2:], posters.get(tid, ""), r["rt"], ppl(r["d"]), ppl(r["c"])]))
    for i in range(SHARDS):
        (out / "p" / f"{i}.txt").write_text("\n".join(sorted(shards.get(i, []))) + "\n", encoding="utf-8")

    # 影人：作品倒排（分片）+ 可搜索的名单（至少 3 部作品）
    directed, acted = defaultdict(list), defaultdict(list)
    for tid in order:
        r = rows[tid]
        for x in r["d"]:
            directed[x].append(tid[2:])
        for x in r["c"]:
            acted[x].append(tid[2:])
    nshards = defaultdict(list)
    searchable = []
    for nid, name in names.items():
        d, a = directed.get(nid, []), acted.get(nid, [])
        nshards[int(nid[2:]) % NSHARDS].append(f"{nid[2:]}\t{name}\t{'|'.join(d)}\t{'|'.join(a)}")
        if len(d) + len(a) >= 3:
            searchable.append((len(d) + len(a), nid[2:], name))
    for i in range(NSHARDS):
        (out / "n" / f"{i}.txt").write_text("\n".join(sorted(nshards.get(i, []))) + "\n", encoding="utf-8")
    searchable.sort(reverse=True)
    with open(out / "names.txt", "w", encoding="utf-8") as f:
        for c, nid, name in searchable:
            f.write(f"{nid}\t{name}\t{c}\n")
    info = {"built": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "titles": len(rows), "tier1": len(tier1),
            "names": len(searchable), "posters": sum(1 for t in rows if posters.get(t)),
            "shards": SHARDS, "nshards": NSHARDS, "genres": GENRES, "posterPrefix": POSTER_PREFIX}
    (out / "info.json").write_text(json.dumps(info, ensure_ascii=False), encoding="utf-8")
    log("完成", {k: v for k, v in info.items() if k != "genres"}, f"{time.time() - t0:.0f}s")


GQL = "https://api.graphql.imdb.com/"
GQL_HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
                  "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "content-type": "application/json", "x-imdb-client-name": "imdb-web-next-localized",
    "x-imdb-user-language": "en-US", "x-imdb-user-country": "US",
}


def fetch_hot(n):
    """IMDb 按热度排的近期 / 待映电影和剧集（前 n 部）。"""
    from datetime import date, timedelta
    start = (date.today() - timedelta(days=540)).isoformat()
    end = (date.today() + timedelta(days=3 * 365)).isoformat()
    q = """query($after:String,$start:Date,$end:Date){ advancedTitleSearch(first:250, after:$after,
      constraints:{ titleTypeConstraint:{anyTitleTypeIds:["movie","tvSeries","tvMiniSeries"]},
                    releaseDateConstraint:{releaseDateRange:{start:$start, end:$end}} },
      sort:{sortBy:POPULARITY, sortOrder:ASC}){ pageInfo{hasNextPage endCursor} edges{ node{ title{
        id titleText{text} originalTitleText{text} releaseYear{year} titleType{id} runtime{seconds}
        genres{genres{text}} ratingsSummary{aggregateRating voteCount} primaryImage{url} } } } } }"""
    s = requests.Session()
    s.headers.update(GQL_HEADERS)
    out, after = {}, None
    while len(out) < n:
        try:
            r = s.post(GQL, json={"query": q, "variables": {"after": after, "start": start, "end": end}}, timeout=40)
            a = r.json()["data"]["advancedTitleSearch"]
        except (requests.RequestException, ValueError, KeyError, TypeError) as e:
            log("热门片获取中断", e.__class__.__name__)
            break
        for e in a["edges"]:
            t = e["node"]["title"]
            rs = t.get("ratingsSummary") or {}
            url = (t.get("primaryImage") or {}).get("url") or ""
            out[t["id"]] = {
                "rank": len(out), "type": (t.get("titleType") or {}).get("id", ""),
                "title": (t.get("titleText") or {}).get("text", ""), "orig": (t.get("originalTitleText") or {}).get("text", ""),
                "year": (t.get("releaseYear") or {}).get("year"), "votes": rs.get("voteCount") or 0,
                "rating": rs.get("aggregateRating") or "", "runtime": round(t["runtime"]["seconds"] / 60) if (t.get("runtime") or {}).get("seconds") else "",
                "genres": [g["text"] for g in ((t.get("genres") or {}).get("genres") or [])],
                "poster": url[len(POSTER_PREFIX):-len("._V1_.jpg")] if url.startswith(POSTER_PREFIX) and url.endswith("._V1_.jpg") else "",
            }
        if not a["pageInfo"]["hasNextPage"]:
            break
        after = a["pageInfo"]["endCursor"]
        time.sleep(0.5)
    return out


def fetch_posters(ids, posters, batch=200, workers=4):
    if not ids:
        return
    log("查海报", len(ids))
    q = "query($ids:[ID!]!){ titles(ids:$ids){ id primaryImage{url} } }"
    s = requests.Session()
    s.headers.update(GQL_HEADERS)
    chunks = [ids[i:i + batch] for i in range(0, len(ids), batch)]
    fails = 0

    def one(chunk):
        for attempt in range(3):
            try:
                r = s.post(GQL, json={"query": q, "variables": {"ids": chunk}}, timeout=40)
                if r.status_code == 200:
                    out = {}
                    for t in (r.json().get("data") or {}).get("titles") or []:
                        url = ((t or {}).get("primaryImage") or {}).get("url") or ""
                        if url.startswith(POSTER_PREFIX) and url.endswith("._V1_.jpg"):
                            out[t["id"]] = url[len(POSTER_PREFIX):-len("._V1_.jpg")]
                        elif t:
                            out[t["id"]] = ""
                    return out
            except (requests.RequestException, ValueError):
                pass
            time.sleep(2 + attempt * 3)
        return None

    done = 0
    with ThreadPoolExecutor(workers) as ex:
        for res in ex.map(one, chunks):
            done += 1
            if res is None:
                fails += 1
                continue
            for k, v in res.items():
                if v:
                    posters[k] = v
            if done % 50 == 0:
                log(f"  海报 {done}/{len(chunks)}")
    log("海报完成，失败批次", fails)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="ds", help="数据集缓存目录")
    ap.add_argument("--out", default="out/idx")
    ap.add_argument("--min-votes", type=int, default=400)
    ap.add_argument("--min-votes-zh", type=int, default=40, help="有中文译名的片子门槛放宽")
    ap.add_argument("--poster-cache", default="", help="上一次的 p/ 目录，已有的海报不再查")
    ap.add_argument("--no-posters", action="store_true")
    ap.add_argument("--hot", type=int, default=3000, help="另外收录近期 / 待映最热门的多少部")
    a = ap.parse_args()
    build(a.src, a.out, a.min_votes, a.min_votes_zh, a.poster_cache, a.no_posters, a.hot)
