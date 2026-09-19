"""process_chain.py — 过程链存取机制（标准库）。
把流程执行状态按步存档、可回溯恢复，并支持审查失败后的「中断—返回」定位。
规则见 resistance/过程链存取.md。数据 tmp/state/*.json。
命令：
  save --step S --data JSON     存档某步状态并置 latest
  load [--step S]               恢复到指定/最新步
  interrupt --step S            记录审查中断点（返回机制目标）
  resume                        读取中断点并恢复（返回中断步骤）
"""
import json, os, argparse
STATE = os.path.join("tmp", "state")

def _w(name, val):
    os.makedirs(STATE, exist_ok=True)
    open(os.path.join(STATE, name), "w", encoding="utf-8").write(val)

def save(step, payload):
    _w(f"{step}.json", json.dumps(payload, ensure_ascii=False, indent=2))
    _w("latest", step); print(f"[过程链] 存档步骤 {step}")

def load(step=None):
    step = step or (open(os.path.join(STATE, "latest"), encoding="utf-8").read()
                    if os.path.exists(os.path.join(STATE, "latest")) else None)
    if not step:
        print("[过程链] 无存档"); return None
    d = json.load(open(os.path.join(STATE, f"{step}.json"), encoding="utf-8"))
    print(f"[过程链] 恢复到步骤 {step}"); return d

def interrupt(step):
    _w("interrupt", step); print(f"[过程链] 记录中断步骤 {step}")

def resume():
    p = os.path.join(STATE, "interrupt")
    if not os.path.exists(p):
        print("[过程链] 无中断记录"); return None
    step = open(p, encoding="utf-8").read()
    print(f"[过程链] 返回中断步骤 {step}"); return step

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); g = ap.add_subparsers(dest="cmd", required=True)
    s = g.add_parser("save"); s.add_argument("--step", required=True); s.add_argument("--data", default="{}")
    l = g.add_parser("load"); l.add_argument("--step", default=None)
    i = g.add_parser("interrupt"); i.add_argument("--step", required=True)
    g.add_parser("resume")
    a = ap.parse_args()
    {"save": lambda: save(a.step, json.loads(a.data)), "load": lambda: load(a.step),
     "interrupt": lambda: interrupt(a.step), "resume": resume}[a.cmd]()