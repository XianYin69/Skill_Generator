"""gen_agent_prompt.py — 生成四格式agent提示词+SKILL.md（KiloCode格式）。提示词精简为一句话：使用 skill{name} 来完成用户请求。"""
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
    print("[OK] SKILL.md + agent/ 已生成（提示词一句话：使用 skill名 来完成用户请求）")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--target", required=True); ap.add_argument("--name")
    a = ap.parse_args(); gen(a.target, a.name)
