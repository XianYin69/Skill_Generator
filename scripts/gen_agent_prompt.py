"""gen_agent_prompt.py — 生成四格式agent提示词+SKILL.md（KiloCode格式）+asset/、dependence/ 标准目录。提示词精简为一句话：使用 skill{name} 来完成用户请求。"""
import os, argparse

def _p(t):
    s = os.path.join(t, "SKILL.md")
    if not os.path.exists(s): return "Auto-generates and iterates Agent Skills"
    body = open(s, encoding="utf-8").read().split("---")
    for l in (body[1].splitlines() if len(body) > 2 else []):
        if l.strip().startswith("description:"):
            val = l.split(":", 1)[1].strip()
            if val and val != ">": return val[:80]
    return "Auto-generates and iterates Agent Skills"

def _zh(n):
    return f"# {n}\n\n使用 `{n}` skill 来完成用户请求。"

def _en(n):
    return f"# {n} Agent Rules\n\n使用 `{n}` skill 来完成用户请求。"

def _detail(t):
    cand = [("- 流程节点：[branch/流程/](branch/流程/流程.md)", os.path.join(t, "branch", "流程", "流程.md")),
            ("- 约束兜底：[resistance/](resistance/resistance.md)", os.path.join(t, "resistance", "resistance.md"))]
    c = [a for a, b in cand if os.path.exists(b)]
    return ("\n\n## 详细流程\n" + "\n".join(c)) if c else ""

ASSET = "# asset（技能包资产）\n\n随技能包分发的模板、样例、素材等非脚本资产文件目录；SMS 包管理器安装技能包时，本目录与技能包本体一并接受检查与净化。\n"
DEP = "# dependence（依赖声明）\n\n声明本技能包依赖的技能包/软件/仓库地址：每行一条 `名称 | 类型 | 来源`，类型为 skill|software|repo：\n\n```\nsafe-mouse-automation | skill | gh:owner/repo\npandas | software | pip\n```\n\nSMS 包管理器安装技能包时，本目录条目与技能包本体接受同样的检查与净化（trust 标注·未审/隔离拒装·仓库下载须网络授权·见 skill_manage_system pkg_deps.py），审过后方可下载安装执行。\n"

def _pkg_dirs(t):
    for d, s in (("asset", ASSET), ("dependence", DEP)):
        p = os.path.join(t, d); os.makedirs(p, exist_ok=True); f = os.path.join(p, d + ".md")
        if not os.path.exists(f): open(f, "w", encoding="utf-8").write(s)

def gen(target, name=None):
    os.makedirs(target, exist_ok=True); n = name or os.path.basename(os.path.normpath(target)); p = _p(target)
    z, e = _zh(n), _en(n)
    open(os.path.join(target, "SKILL.md"), "w", encoding="utf-8").write(
        f"---\nname: {n}\ndescription: >\n  {p}\nlicense: MIT\nmetadata:\n  category: development\n---\n\n"
        + z + _detail(target) + "\n")
    out = os.path.join(target, "agent"); os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "CLAUDE.md"), "w", encoding="utf-8").write(z)
    open(os.path.join(out, "agent_prompt.md"), "w", encoding="utf-8").write(z)
    open(os.path.join(out, ".cursorrules"), "w", encoding="utf-8").write(e)
    open(os.path.join(out, "instructions.md"), "w", encoding="utf-8").write(e)
    _pkg_dirs(target)
    print("[OK] SKILL.md + agent/ + asset/ + dependence/ 已生成（提示词一句话：使用 skill名 来完成用户请求）")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--target", required=True); ap.add_argument("--name")
    a = ap.parse_args(); gen(a.target, a.name)
