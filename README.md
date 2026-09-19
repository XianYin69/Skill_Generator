# Skill_Generator

Agent 级 Skill 生成工具。用于自动生成与迭代 Agent Skill。

## 结构

- [`SKILL.md`](SKILL.md)：入口，子模块索引与阅读顺序。
- [`references/`](references/)：知识库（文档、素材、流程图）。
- [`scripts/`](scripts/)：脚本库（校验、迁移、生成工具）。
- [`branch/`](branch/)：分支库（实验性方案、备选路径）。
- [`update/`](update/)：自更新组件（升级触发、回滚逻辑）。
- [`resistance/`](resistance/)：约束库 / 兜底（红线、降级策略）。
- [`flowchart/`](flowchart/)：项目流程图链表 JSON（源于 `Skill_Generator_stream.html`）。

## 约束

本项目遵循 [`rule_edit.md`](rule_edit.md)。所有编辑操作需满足 ≤ 50 行 + 自然语言 + 悬空链接为 0。
