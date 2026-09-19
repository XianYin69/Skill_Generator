# Skill_Generator — Agent Prompt Reference

> Generated 2026-09-19. Covers CLAUDE.md, .cursorrules, instructions.md, and this cross-reference.

## Purpose
本 Skill 用于自动生成与迭代 Agent Skill。读本目录下的子模块即可按需取用。

## Tool Index
- scripts/：可执行工具（Skill_Generator 自动生成）
- resistance/：约束与兜底
- branch/流程/：各阶段分支

## Cross-Tool Mapping
| Tool | File | Entry |
|---|---|---|
| Claude Code | `CLAUDE.md` | `# Skill_Generator` role block |
| Cursor / Windsurf | `.cursorrules` | `## Rules` section |
| OpenAI Assistants | `instructions.md` | `## Goal` block |
| General | `agent_prompt.md` | This file |

## Common Protocol
Initialize → 初始化 → 需求确认 → … → 收尾 (release+clean+gen_prompt) → AGENTS.md complete.