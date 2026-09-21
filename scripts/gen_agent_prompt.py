"""gen_agent_prompt.py — 生成四格式agent提示词+SKILL.md（KiloCode格式）。"""
import os, time, argparse
FZ = "初始化→需求确认→经验查询→大纲构建→分支分析→脚本构建→知识库构建→约束编写→整体审查→收尾→完成"
FE = "init→requirement→research→outline→analyze→scripts→kb→constraints→review→wrapup→done"
DEF = "knowledge_browser,knowledge_download,knowledge_convert,gen_agent_prompt,logic_chain,process_chain,garbage_collect,context_compress,penalty,self_update,check-links"
def _tools(t):
    d = os.path.join(t, "scripts"); fs = [os.path.splitext(f)[0] for f in sorted(os.listdir(d)) if f.endswith(".py")] if os.path.isdir(d) else []
    return ", ".join(f"`scripts/{x}.py`" for x in (fs or DEF.split(",")))
def _p(t):
    s = os.path.join(t, "SKILL.md")
    if not os.path.exists(s): return "Auto-generates and iterates Agent Skills"
    body = s and open(s, encoding="utf-8").read().split("---")
    for l in (body[1].splitlines() if len(body) > 2 else []):
        if l.strip().startswith("description:"):
            val = l.split(":", 1)[1].strip()
            if val and val != ">": return val[:80]
    return "Auto-generates and iterates Agent Skills"
def _zh(n, p, d, T):
    return (f"# {n} · {d}\n\n## 角色\n你是{n}——自动生成与迭代 Agent Skill 的智能体。目标：{p}\n\n"
            f"## 可用工具\n{T}\n\n## 工作流\n创建：{FZ} | 修改：初始化→修改流程→完成\n\n"
            f"## 机制\n逻辑链（双链辩论）/过程链（interrupt/resume）/惩罚熔断/上下文压缩/垃圾回收\n\n"
            f"## 红线\n不得跳过初始化；不得静默写盘（--dry-run默认）；不得删除resistance/约束；悬空链接必须为0；文件≤50行\n\n"
             f"## 调用与开始\n通过 skill 工具调用本技能（name: {n}）加载其 SKILL.md；随后等待用户需求，从初始化开始执行。")
def _en(n, p, d, T):
    return (f"# {n} Agent Rules · {d}\n\n## Role\nYou are {n}. Purpose: {p}\n\n"
            f"## Tools\n{T}\n\n## Workflow\nCreate: {FE} | Modify: init→modify→done\n\n"
            f"## Mechanisms\nLogic chain (pro/con debate) / Process chain (interrupt/resume) / Penalty circuit-breaker / Context compression / GC\n\n"
            f"## Red Lines\nNever skip init; never write to disk silently (--dry-run default); never delete resistance/ constraints; check-links must be 0; files ≤50 lines\n\n"
             f"## Invoke & Start\nInvoke this skill via the skill tool (name: {n}) to load SKILL.md; then wait for user requirements and begin at initialization.")
def _detail(t):
    cand = [("- 流程节点：[branch/流程/](branch/流程/流程.md)", os.path.join(t, "branch", "流程", "流程.md")),
            ("- 约束兜底：[resistance/](resistance/resistance.md)", os.path.join(t, "resistance", "resistance.md"))]
    c = [a for a, b in cand if os.path.exists(b)]
    return ("\n\n## 详细流程\n" + "\n".join(c)) if c else ""
def gen(target, name=None):
    os.makedirs(target, exist_ok=True); n = name or os.path.basename(os.path.normpath(target)); p = _p(target)
    d = time.strftime("%Y-%m-%d"); T = _tools(target); z, e = _zh(n, p, d, T), _en(n, p, d, T)
    open(os.path.join(target, "SKILL.md"), "w", encoding="utf-8").write(
        f"---\nname: {n}\ndescription: >\n  {p}\nlicense: MIT\nmetadata:\n  category: development\n---\n\n"
        + z + _detail(target) + "\n")
    out = os.path.join(target, "agent"); os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "CLAUDE.md"), "w", encoding="utf-8").write(z); open(os.path.join(out, ".cursorrules"), "w", encoding="utf-8").write(e); open(os.path.join(out, "instructions.md"), "w", encoding="utf-8").write(e)
    open(os.path.join(out, "agent_prompt.md"), "w", encoding="utf-8").write(
        f"# {n} — System Prompt (Universal)\n\n> {d} | Four formats in agent/\n\n" + z
        + "\n\n## Cross-Tool Mapping\n| Tool | File | Entry |\n|---|---|---|\n"
        f"| Claude Code | `CLAUDE.md` | `# {n}` role block |\n| Cursor/Windsurf | `.cursorrules` | `## Rules` |\n"
        "| OpenAI Assistants | `instructions.md` | `## Goal` |\n| General | `agent_prompt.md` | This file |\n" f"| Skill-aware clients | `SKILL.md` frontmatter | call skill `{n}` via the skill tool |")
    print("[OK] SKILL.md + agent/ 已生成")
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--target", required=True); ap.add_argument("--name"); a = ap.parse_args(); gen(a.target, a.name)
