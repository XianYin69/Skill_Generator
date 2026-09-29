"""init-planned-tasks.py — 初始化写入 planned_tasks/（README.md＋template.json）；默认预览，`--yes` 写盘；已有文件不覆盖。"""
import argparse, json, os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "asset", "planned_tasks")
FILES = ("README.md", "template.json")
MIN = {"README.md": "# planned_tasks（计划任务）\n\n一任务一文件 `pt-<skill>-<slug>.json`；由 SMS 调度器到期执行，技能自身不得执行；删除即注销。\n",
       "template.json": json.dumps({"id": "pt-<skill>-<slug>", "title": "", "skill": "<技能id>",
        "input": "到期要执行的诉求文本",
        "schedule": {"mode": "at|cron|interval", "at": "2026-09-30T08:00", "cron": "0 8 * * *", "every_min": 60},
        "session": {"kind": "cron", "key": "<skill>:<id>"}, "status": "pending", "created": "<ISO本地>",
        "next_run": "<ISO本地>", "last_run": None, "runs": 0, "notify": "shell", "depends": []},
        ensure_ascii=False, indent=2) + "\n"}

def spots(t):
    tmp = os.path.join(t, "tmp")
    return [os.path.join(t, "planned_tasks")] + ([os.path.join(tmp, "planned_tasks")] if os.path.isdir(tmp) else [])

def text(name):
    src = os.path.join(SRC, name)
    return open(src, encoding="utf-8").read() if os.path.exists(src) else MIN[name]

def run(target, yes):
    if not os.path.isdir(target): return [{"path": target, "action": "error", "why": "目标工作空间不存在"}]
    out = []
    for d in spots(target):
        os.makedirs(d, exist_ok=True) if yes else None
        for n in FILES:
            p = os.path.join(d, n)
            if os.path.exists(p): out.append({"path": p, "action": "skip", "why": "已有计划任务模板"})
            elif not yes: out.append({"path": p, "action": "preview", "hint": "--yes 写入"})
            else:
                tmpf = p + ".tmp"; open(tmpf, "w", encoding="utf-8").write(text(n)); os.replace(tmpf, p)
                out.append({"path": p, "action": "written"})
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="建立 planned_tasks/ 计划任务目录")
    ap.add_argument("--target", required=True); ap.add_argument("--yes", action="store_true")
    a = ap.parse_args()
    print(json.dumps({"items": run(a.target, a.yes)}, ensure_ascii=False))
