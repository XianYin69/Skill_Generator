"""gen_agent_prompt.py — 生成四种主流 agent/CLI 工具格式提示词（存于 agent/）。
命令：python gen_agent_prompt.py --target <目标skill目录> [--name <skill名>]
格式：CLAUDE.md（Claude Code）、.cursorrules（Cursor/Windsurf）、
      instructions.md（OpenAI Assistants）、agent_prompt.md（通用参考）。
"""
import os, time, argparse

def _read_first_para(path):
    if not os.path.exists(path): return "（用途待补充）"
    for l in open(path, encoding="utf-8"):
        s = l.strip()
        if s and not s.startswith(("#", "|", ">", "[", "-")): return s[:120]
    return "（用途待补充）"

def gen(target, name=None):
    name = name or os.path.basename(os.path.normpath(target))
    purpose = _read_first_para(os.path.join(target, "SKILL.md"))
    date = time.strftime("%Y-%m-%d")
    base = f"{name} · {date}"
    agent_dir = os.path.join(target, "agent")
    os.makedirs(agent_dir, exist_ok=True)
    tools = f"- scripts/：可执行工具（{name} 自动生成）\n- resistance/：约束与兜底\n- branch/流程/：各阶段分支"
    TPLS = {
        "CLAUDE.md": f"# {base}\n\n## 角色\n{purpose}\n\n## 可用工具\n{tools}\n\n## 调用约定\n1. 读 SKILL.md 进入「初始化」。\n2. 推理时记逻辑链；审核用正方/反方双链辩论。\n3. 异常记中断步骤，修复后 resume 返回重评。",
        ".cursorrules": f"# {name} Agent Rules\n\n## Purpose\n{purpose}\n\n## Tools\n{tools}\n\n## Rules\n- 先读 SKILL.md 再执行任何步骤。\n- 所有决策节点须记录逻辑链；审查须正反双链辩论。\n- 失败记录中断点（process_chain interrupt），修复后 resume 返回。",
        "instructions.md": f"# {base}\n\n## Goal\n{purpose}\n\n## Capabilities\n{tools}\n\n## Operating Procedure\n1. Read SKILL.md → navigate to 初始化.\n2. Chain logic at each decision; debate pro/contra at review gates.\n3. On failure: record interrupt point; after fix: resume to that step.",
        "agent_prompt.md": f"# {name} — Agent Prompt Reference\n\n> Generated {date}. Covers CLAUDE.md, .cursorrules, instructions.md, and this cross-reference.\n\n## Purpose\n{purpose}\n\n## Tool Index\n{tools}\n\n## Cross-Tool Mapping\n| Tool | File | Entry |\n|---|---|---|\n| Claude Code | `CLAUDE.md` | `# {name}` role block |\n| Cursor / Windsurf | `.cursorrules` | `## Rules` section |\n| OpenAI Assistants | `instructions.md` | `## Goal` block |\n| General | `agent_prompt.md` | This file |\n\n## Common Protocol\nInitialize → 初始化 → 需求确认 → … → 收尾 (release+clean+gen_prompt) → AGENTS.md complete.",
    }
    for fn, content in TPLS.items():
        open(os.path.join(agent_dir, fn), "w", encoding="utf-8").write(content)
    print(f"[agent提示词] 已写入 {agent_dir}/（CLAUDE.md/.cursorrules/instructions.md/agent_prompt.md）")
    return agent_dir

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--target", required=True); ap.add_argument("--name")
    a = ap.parse_args(); gen(a.target, a.name)