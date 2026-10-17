"""pkg_templates.py — 标准目录模板：asset/ ＋ dependence/（deps.json·source_url 必填）＋ planned_tasks/。
新增：支持双指向依赖（远端 URL + 本地路径），推送时移除本地路径。
"""
import json, os, datetime

DEPS = json.dumps({"dependencies": []}, ensure_ascii=False, indent=2) + "\n"

ASSET = ("# asset（技能包资产）\n\n随技能包分发的模板、样例、素材等非脚本资产文件目录；"
 "SMS 包管理器安装技能包时，本目录与技能包本体一并接受检查与净化。\n")
DEP = ("# dependence（依赖声明）\n\n声明本技能包依赖的技能包/软件/仓库地址：每行一条 `名称 | 类型 | 来源`，"
 "类型为 skill|software|repo。\n\n**每条依赖必须附原始链接**：机器可读清单 `deps.json`，条目字段 "
 "`name / source_url / license / version / install / checked_at`；`source_url` 为 GitHub/GitLab/官方仓库或发布页"
 "原始链接（本地技能用 `local://<skill-id>`）。缺 `source_url` 即判不合格，`python scripts/lint-deps.py` 报错退出。"
 "SMS 据该链接联网检索/下载到技能目录（须网络授权）。\n\nSMS 安装时本目录条目与本体接受同样检查与净化"
 "（trust 标注·未审/隔离拒装·仓库下载须网络授权·见 skill_manage_system pkg_deps.py）。\n")
PT = ("# planned_tasks（计划任务）\n\n一任务一文件 `pt-<skill>-<slug>.json`；schema 与 SMS 读取端一致"
 "（见 `template.json`，字段名不得改动）。到期由 SMS 调度器读取执行并把记录挂到 `session.key` 关联链，"
 "**技能自身不得自行执行计划任务**；原子写（临时文件+替换）；status 仅 pending/running/done/paused/failed；"
 "时间一律本地 ISO；删除即注销。\n")
TPL = json.dumps({"id": "pt-<skill>-<slug>", "title": "", "skill": "<技能id>",
 "input": "到期要执行的诉求文本",
 "schedule": {"mode": "at|cron|interval", "at": "2026-09-30T08:00", "cron": "0 8 * * *", "every_min": 60},
 "session": {"kind": "cron", "key": "<skill>:<id>"}, "status": "pending", "created": "<ISO本地>",
 "next_run": "<ISO本地>", "last_run": None, "runs": 0, "notify": "shell", "depends": []},
 ensure_ascii=False, indent=2) + "\n"

def ptext(n):
    a = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "asset", "planned_tasks", n)
    return open(a, encoding="utf-8").read() if os.path.exists(a) else (PT if n == "README.md" else TPL)

def planned(t):
    d = os.path.join(t, "planned_tasks"); os.makedirs(d, exist_ok=True)
    for n in ("README.md", "template.json"):
        f = os.path.join(d, n)
        if not os.path.exists(f): open(f, "w", encoding="utf-8").write(ptext(n))

def pkg_dirs(t):
    for d, s in (("asset", ASSET), ("dependence", DEP)):
        p = os.path.join(t, d); os.makedirs(p, exist_ok=True); f = os.path.join(p, d + ".md")
        if not os.path.exists(f): open(f, "w", encoding="utf-8").write(s)
    j = os.path.join(t, "dependence", "deps.json")
    if not os.path.exists(j): open(j, "w", encoding="utf-8").write(DEPS)

def add_local_deps(deps_path, skill_name, local_paths=None):
    """添加本地依赖条目（同时保留远端 source_url）。
    参数:
        deps_path: deps.json 文件路径
        skill_name: 技能名称
        local_paths: 本地路径列表，如 ["C:\\Users\\User\\AppData\\Local\\SMS\\skills"]
    返回: 是否成功
    """
    if not os.path.exists(deps_path):
        return False
    
    with open(deps_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    dependencies = data.get("dependencies", [])
    
    # 检查是否已有本地依赖
    local_exists = any(d.get("source_url", "").startswith("local://") for d in dependencies)
    
    if not local_exists:
        # 添加本地技能依赖
        dependencies.append({
            "name": skill_name,
            "source_url": f"local://{skill_name}",
            "license": "MIT",
            "version": "0.1.0",
            "install": "sms-local",
            "checked_at": datetime.datetime.now().isoformat()[:19],
            "source_url_status": "verified"
        })
        data["dependencies"] = dependencies
        with open(deps_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    
    return False

def strip_local_urls(deps_path):
    """移除本地路径，只保留远端 URL（用于推送前的准备）。
    参数:
        deps_path: deps.json 文件路径
    返回: 清理后的依赖列表
    """
    if not os.path.exists(deps_path):
        return []
    
    with open(deps_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    dependencies = data.get("dependencies", [])
    cleaned = [d for d in dependencies if not d.get("source_url", "").startswith("local://")]
    
    # 如果有本地依赖被移除，更新文件
    if len(cleaned) != len(dependencies):
        data["dependencies"] = cleaned
        with open(deps_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    return cleaned
