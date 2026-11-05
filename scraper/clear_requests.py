"""从最新的 requests.json 里删掉这次已经处理过的请求，网页在后台运行期间新加的保留。
用法：python clear_requests.py requests.json processed_requests.json"""
import json
import sys


def load(p):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f) or {}
    except (OSError, ValueError):
        return {}


cur, done = load(sys.argv[1]), load(sys.argv[2])
out = {}
ids = [i for i in cur.get("ids") or [] if i not in set(done.get("ids") or [])]
if ids:
    out["ids"] = ids
if cur.get("q") and cur.get("q") != done.get("q"):
    out["q"] = cur["q"]
fix = {k: v for k, v in (cur.get("fix") or {}).items() if (done.get("fix") or {}).get(k) != v}
if fix:
    out["fix"] = fix
people = [n for n in cur.get("people") or [] if n not in set(done.get("people") or [])]
if people:
    out["people"] = people
with open(sys.argv[1], "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False)
print("剩下的请求：", out or "无")
