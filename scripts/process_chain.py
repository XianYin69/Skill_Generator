"""process_chain.py — 过程链存取机制（标准库）。
用途：把流程执行状态按步骤存档并可回溯恢复（进度、快照、回滚）。规则见 resistance/过程链存取.md。
数据：tmp/state/<step>.json；latest 指针指向当前步。
"""
import json, os, argparse

STATE = os.path.join("tmp", "state")

def save(step, payload):
    os.makedirs(STATE, exist_ok=True)
    json.dump(payload, open(os.path.join(STATE, f"{step}.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    open(os.path.join(STATE, "latest"), "w", encoding="utf-8").write(step)
    print(f"[过程链] 已存档步骤 {step}")

def load(step=None):
    step = step or (open(os.path.join(STATE, "latest"), encoding="utf-8").read()
                    if os.path.exists(os.path.join(STATE, "latest")) else None)
    if not step:
        print("[过程链] 无存档"); return None
    d = json.load(open(os.path.join(STATE, f"{step}.json"), encoding="utf-8"))
    print(f"[过程链] 恢复到步骤 {step}"); return d

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); g = ap.add_subparsers(dest="cmd", required=True)
    s = g.add_parser("save"); s.add_argument("--step", required=True); s.add_argument("--data", default="{}")
    l = g.add_parser("load"); l.add_argument("--step", default=None)
    a = ap.parse_args()
    save(a.step, json.loads(a.data)) if a.cmd == "save" else load(a.step)