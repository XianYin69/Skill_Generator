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
- 脚本归位：`建立tmp.ps1`、`建立tmp.sh` 移至 `scripts/`（脚本库）；`建立tmp.md` 与 `scripts.md` 同步更新引用。
- 脚本英文命名：`scripts/建立tmp.ps1` → `create-tmp.ps1`、`scripts/建立tmp.sh` → `create-tmp.sh`（依 rule_edit.md「脚本使用英文名称 + 扩展名」）；同步更新 `scripts.md`、`建立tmp.md` 引用。
- `branch/流程/大纲构建/`：按 flowchart 构建大纲构建分支流程，拆出 14 个节点子文件夹（建立大纲、审阅大纲、检查可执行、检查可达性、检查兜底、记录错误、搜索方案、检查方案、询问方案、修改大纲、询问接受、询问修改点、生成大纲、标记完成），含 3 类循环修复路径；`大纲构建.md` 重写为根索引。
- 依据 `flowchart/` 填充其余全部步骤分支：`需求确认(8)/经验查询(13)/分支分析(60)/脚本构建(15)/知识库构建(12)/约束编写(13)/整体审查(15)/收尾(19)/修改流程(4)`，共 159 个节点子文件夹（每个含同名 markdown，按流程图决策分支互相链接、跨步骤跳转正确）；各步骤根 `.md` 重写为含入口节点与后继步骤的索引。
- 知识库构建增强：限定来源（开放文献库/百科/权威论坛博客/MIT 仓库）、保留许可版权、元数据清洗改造为目标 skill 形态；新增 `references/知识库信用评级/` 评级标准。
- 新增 scripts：`knowledge_browser.py`、`knowledge_download.py`、`knowledge_convert.py`（MIT 依赖，留证清洗）；`self_update.py`（report/compare/release/clean 接口）。
- 自更新重构为接口：`update/update.md` 定义外部 skill 可调契约；初始化[标记完成]挂载接口+冻结过程链快照；收尾新增「比对 tmp → 释放到目标 skill → 删除 tmp」。
- 五大机制（垃圾回收/上下文压缩/逻辑链/过程链存取/惩罚）：`resistance/` 约束文档 + `scripts/` 实现脚本，并接入相关流程步骤根与 SKILL/流程索引。
- 收尾自动生成 agent 工具提示词：新增 scripts/gen_agent_prompt.py（写 AGENTS.md 到目标 skill 根）；收尾「收尾操作」接「生成agent工具提示词」→「完成skill开发」。
- 审核正反双链辩论：resistance/逻辑链机制 增加「正反双链辩论」规则；整体审查新增 正方逻辑链/反方逻辑链/辩论裁决（辩论闸口）；收尾「审核提示词」新增 提示词正方链/提示词反方链/提示词辩论裁决。
- 返回机制：resistance/过程链存取 增加「中断—返回」规则；整体审查新增 记录中断步骤/返回中断步骤，与 process_chain.py interrupt/resume 配合，审查修复后必须回到中断步骤重评。
- logic_chain.py 增加 `debate` 命令；process_chain.py 增加 `interrupt`/`resume` 命令（均 ≤ 50 行）。
- 分支分析 / 脚本构建阶段新增「视觉 / 听觉交互」约束：用户如需视觉或听觉输入/交互，必须创建对应 `scripts/` 脚本（如 `vision_input.py`、`audio_input.py`）并在流程节点中显式调用。
- 以整体审查分支实测本项目 → 固化 `resistance/审查约束/审查约束.md`；修正 `check-links.py`、`knowledge_convert.py` 超 50 行。
- `tmp/` 建目录新增 `agent/`：`create-tmp.ps1`/`create-tmp.sh` 追加该目录，`建立tmp.md` 同步更新；`gen_agent_prompt.py` 重写为输出四格式（`agent/CLAUDE.md`、`agent/.cursorrules`、`agent/instructions.md`、`agent/agent_prompt.md`），覆盖 Claude Code / Cursor / OpenAI Assistants / 通用参考。
- 为本项目执行 `gen_agent_prompt.py` 生成四份 agent 提示词（`agent/` 目录提交至项目）。
- `gen_agent_prompt.py` 重写为**系统提示词格式**（角色定义 + 工具列表 + 工作流 + 核心机制 + 红线 + 开始），输出四格式均可直接注入 agent；脚本压缩至 44 行；各生成文件 ≤ 50 行。
- `SKILL.md` 适配 KiloCode skill 格式：YAML frontmatter（name/description/license/metadata）+ 可直接注入 agent 的系统提示词（工作原则/执行路径/可用工具/红线/开始），49 行。

