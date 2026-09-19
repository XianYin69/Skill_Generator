"""logic_chain.py — 逻辑链机制（标准库）。
用途：记录“前提→推理→结论”链并校验连续性，防止跳步。规则见 resistance/逻辑链机制.md。
数据：JSONL，每行一步 {step, from, to, why}。校验：前一步 to 必须与后一步 from 相容。
"""
import json, sys, argparse

def append(chain_file, frm, to, why):
    with open(chain_file, "a", encoding="utf-8") as f:
        f.write(json.dumps({"from": frm, "to": to, "why": why}, ensure_ascii=False) + "\n")

def verify(chain_file):
    steps = [json.loads(l) for l in open(chain_file, encoding="utf-8") if l.strip()]
    issues = []
    for a, b in zip(steps, steps[1:]):
        if b["from"] != a["to"]:
            issues.append((a["to"], b["from"]))
    for i in issues:
        print(f"[逻辑链断裂] {i[0]} -> {i[1]}")
    print(f"[逻辑链] 共 {len(steps)} 步，断裂 {len(issues)} 处")
    return not issues

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("chain_file")
    g = ap.add_subparsers(dest="cmd", required=True)
    a1 = g.add_parser("add"); a1.add_argument("--from", dest="frm", required=True)
    a1.add_argument("--to", required=True); a1.add_argument("--why", required=True)
    g.add_parser("verify")
    a = ap.parse_args()
    (append(a.chain_file, a.frm, a.to, a.why) if a.cmd == "add" else verify(a.chain_file))