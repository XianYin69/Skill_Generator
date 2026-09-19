"""gen_agent_prompt.py — 收尾后在目标 skill 根生成简要 AGENTS.md（agent 工具提示词）。
用途：Skill_Generator 收尾完成、tmp 释放到目标 skill 后，自动产出一份简明提示词，
     让加载该 skill 的 agent 快速知道「能做什么、怎么用工具」。
命令：python gen_agent_prompt.py --target <目标skill目录> [--name <skill名>]
约束：内容简要；用途优先取自目标 SKILL.md 首段；不写入敏感信息。
"""
import os, time, argparse
TPL = """# AGENTS — {name}

> 由 Skill_Generator 收尾自动生成（简要 agent 工具提示词）·{date}

## 用途
{purpose}

## 结构速览
- `SKILL.md`：入口与流程索引。
- `references/`：知识库；`scripts/`：可执行工具（英文名、MIT 依赖）。
- `resistance/`：约束与兜底；`branch/流程/`：各流程分支；`tmp/`：暂存（收尾后清理）。

## 调用方式
1. 先读 `SKILL.md` 判断创建/修改路径，从「初始化」进入。
2. 推理步骤记逻辑链；审核用正方/反方双链辩论；失败记录中断点、修复后返回该步骤。
3. 长上下文先压缩；过程链可存档/恢复；异常按惩罚机制熔断。
"""

def purpose_of(target):
    sk = os.path.join(target, "SKILL.md")
    if os.path.exists(sk):
        for l in open(sk, encoding="utf-8"):
            s = l.strip()
            if s and not s.startswith(("#", "|", ">", "[", "-")):
                return s[:80]
    return "（请补充本 skill 用途）"

def gen(target, name=None):
    name = name or os.path.basename(os.path.normpath(target))
    out = os.path.join(target, "AGENTS.md")
    open(out, "w", encoding="utf-8").write(
        TPL.format(name=name, date=time.strftime("%Y-%m-%d"), purpose=purpose_of(target)))
    print(f"[agent提示词] 已生成 {out}")
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--target", required=True); ap.add_argument("--name")
    a = ap.parse_args(); gen(a.target, a.name)