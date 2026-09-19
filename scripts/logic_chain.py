"""logic_chain.py — 逻辑链机制（标准库）：记录链、校验连续性、正反双链辩论。
规则见 resistance/逻辑链机制/逻辑链机制.md。数据 JSONL {from,to,why}。
命令：
  add <chain_file> --from A --to B --why R
  verify <chain_file>
  debate --pro <f> --con <f>   正方链与反方链各自校验后按有效步数裁决（审核辩论用）
"""
import json, os, argparse

def _read(f):
    return [json.loads(l) for l in open(f, encoding="utf-8") if l.strip()]

def append(f, frm, to, why):
    d = os.path.dirname(f)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(f, "a", encoding="utf-8") as h:
        h.write(json.dumps({"from": frm, "to": to, "why": why}, ensure_ascii=False) + "\n")

def breaks(steps):
    return [(a["to"], b["from"]) for a, b in zip(steps, steps[1:]) if b["from"] != a["to"]]

def verify(f):
    s = _read(f); br = breaks(s)
    for x in br:
        print(f"[断裂] {x[0]} -> {x[1]}")
    print(f"[逻辑链] {f}: {len(s)} 步 / {len(br)} 断裂")
    return not br

def debate(pro, con):
    okp = verify(pro); okc = verify(con)
    p, c = len(_read(pro)), len(_read(con))
    if not okp and not okc: v = "双方链均断裂 → 回退修链"
    elif not okp: v = "正方链断裂 → 反方胜：不通过"
    elif not okc: v = "反方链断裂 → 正方胜：通过"
    else: v = "正方有效步多 → 通过" if p > c else "反方有效步多 → 不通过" if c > p else "平链 → 转人工/惩罚计数"
    print(f"[辩论裁决] {v} (正方{p}/反方{c})")
    return v

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); g = ap.add_subparsers(dest="cmd", required=True)
    a1 = g.add_parser("add"); a1.add_argument("chain_file")
    a1.add_argument("--from", dest="frm", required=True); a1.add_argument("--to", required=True); a1.add_argument("--why", required=True)
    v = g.add_parser("verify"); v.add_argument("chain_file")
    d = g.add_parser("debate"); d.add_argument("--pro", required=True); d.add_argument("--con", required=True)
    a = ap.parse_args()
    if a.cmd == "add": append(a.chain_file, a.frm, a.to, a.why)
    elif a.cmd == "verify": verify(a.chain_file)
    else: debate(a.pro, a.con)