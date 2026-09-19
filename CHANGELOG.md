# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Initial project setup
- `flowchart/`：由 `Skill_Generator_stream.html` 转换而来的链表 JSON，含 `index.json` 总索引与按 mxCell 前缀拆分的 3 个子文件。
- `SKILL.md`：项目入口，含子模块索引与阅读顺序。
- `references/`、`scripts/`、`branch/`、`update/`、`resistance/`：最小骨架，各含占位 README。
- `FILE_CREATION_POLICY.md`：文件创建策略占位（状态：规划中）。
- `references/约束部分/约束部分.md`：约束区域说明占位（状态：规划中）。
- `README.md`：根目录索引，覆盖新增子模块与约束说明。
- `scripts/check-links.py`：链接校验脚本，运行时全树悬空链接为 0。
- `references/流程/`：SKILL.md 拆分为 10 个阶段子文件（01–10），各 ≤ 50 行，覆盖创建流程与修改流程全部步骤。
- `SKILL.md` 重写为总索引版（31 行），原 101 行内容拆分至 `references/流程/` 各子文件。
- `references/流程/` 重构：每个步骤独立成文件夹（含 README.md），新增 `初始化/` 步骤作为创建与修改两条路径的共同入口。

