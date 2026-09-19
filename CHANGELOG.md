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
- `references/流程/README.md`、`SKILL.md` 更正：明确创建流程与修改流程为两条独立路径，完成「收尾」后不进入修改流程。
- `references/流程/` 重命名：去掉所有步骤文件夹前的序号前缀（`01_需求确认/` → `需求确认/` 等），同步更新各文件内部链接。
- `references/流程/初始化/` 细化：每个初始化节点独立成文件，`README.md` 作为根节点，拆分出 01_读取目录 至 09_标记完成 共 9 个节点文件，并通过「上一步/下一步」链接串联。
- 全项目命名修正：所有 `README.md` 改为「流程名.md」；`branch/`、`references/`、`scripts/`、`update/`、`resistance/` 及 `references/流程/` 下每个步骤文件夹的 markdown 均与文件夹同名；`初始化/` 下编号子节点改为子文件夹（文件夹=流程名，内含同名 markdown）。
- 目录归属修正：`references/流程/` → `branch/流程/`（流程属于分支库）；`references/约束部分/` → `resistance/约束部分/`（约束属于约束库）；同步更新 rule_edit.md、SKILL.md、references.md、branch.md、resistance.md 等交叉引用。
- `branch/流程/初始化/建立tmp/`：新增 `建立tmp.ps1`（Windows）与 `建立tmp.sh`（macOS/Linux）脚本，用于建立 `tmp/` 目录及初始结构（`.git`、`.gitignore`、`rule_edit.md`、`branch/`、`flowchart/`、`references/`、`resistance/`、`update/`）；`建立tmp.md` 补充各系统指令与目录结构说明。

