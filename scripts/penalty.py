"""penalty.py — 惩罚机制（标准库）。
用途：对重复失败/越权/违反约束的行为计分并在超阈值时熔断，强制回退或求助用户。
     规则见 resistance/惩罚机制.md；阈值与各 skill 的重试上限挂钩。
数据：tmp/penalty.json {name: score}。
"""
import json, os, argparse

FILE = os.path.join("tmp", "penalty.json")

def _load():
    return json.load(open(FILE, encoding="utf-8")) if os.path.exists(FILE) else {}

def hit(name, limit=10):
    s = _load(); s[name] = s.get(name, 0) + 1
    json.dump(s, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if s[name] >= limit:
        print(f"[惩罚] {name} 计 {s[name]} 次，达阈值 -> 熔断：回退或询问用户")
        return False
    print(f"[惩罚] {name} 累计 {s[name]} 次")
    return True

def reset(name):
    s = _load(); s.pop(name, None)
    json.dump(s, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"[惩罚] 已清零 {name}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); g = ap.add_subparsers(dest="cmd", required=True)
    h = g.add_parser("hit"); h.add_argument("--name", required=True); h.add_argument("--limit", type=int, default=10)
    r = g.add_parser("reset"); r.add_argument("--name", required=True)
    a = ap.parse_args()
    hit(a.name, a.limit) if a.cmd == "hit" else reset(a.name)