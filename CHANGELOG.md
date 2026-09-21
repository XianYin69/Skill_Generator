# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Initial project setup
- `flowchart/`：由 `Skill_Generator_stream.html` 转换而来的链表 JSON。
- `SKILL.md`：KiloCode 格式入口（YAML frontmatter + 系统提示词，48 行）。
- `branch/流程/`：11 步骤（初始化/需求确认/经验查询/大纲构建/分支分析/脚本构建/知识库构建/约束编写/整体审查/收尾/修改流程），共 163 个节点子文件夹。
- `scripts/`：11 个工具脚本（gen_agent_prompt/knowledge_*/logic_chain/process_chain/garbage_collect/context_compress/penalty/self_update/check-links/create-tmp），均 ≤ 50 行、英文名、MIT 依赖声明。
- `resistance/`：5 大机制约束文档（垃圾回收/上下文压缩/逻辑链/过程链存取/惩罚）+ 审查约束 + 约束部分 + git工作流约束。
- `update/update.md`：自更新接口定义（report/compare/release/clean）。
- `agent/`：四格式 agent 提示词（CLAUDE.md/.cursorrules/instructions.md/agent_prompt.md）。
- `gen_agent_prompt.py`：自动生成目标 skill 的 KiloCode 格式 SKILL.md + agent/ 四格式提示词。
- 需求确认新增「判断是否需要物理输入交互」节点（视觉/听觉/网页交互检测）。
- 脚本构建新增「物理输入网页交互脚本构建」节点（vision_input.py/audio_input.py/browser_interaction.py）。
- `resistance/git工作流约束/`：每步功能分支提交、双链辩论→合入 dev、九项审查通过→合入 main 并推送的分支策略。
- git操作节点：补充操作要点（fetch/pull、`.gitignore` 必含 tmp/ 与 IDE 文件夹、功能分支→dev→main 流转）。
- 初始化新增「git操作」节点；初始化/收尾 git操作 均加入「未 git init 则自动 init」与「推送前询问用户是否推送至远端」。
- `gen_agent_prompt.py`：agent 四格式与 SKILL.md 增写「调用与开始」——通过 skill 工具按 name 调用本技能加载 SKILL.md；`agent_prompt.md` 跨工具映射新增 skill-aware 客户端入口行。

### Fixed
- README：同步现状——补执行路径、agent/ 四格式、自更新接口写盘通道、resistance 新约束与 Git 工作流红线摘要。
- `gen_agent_prompt.py`：可用工具清单动态枚举目标 `scripts/*.py`；SKILL.md 仅链接目标内存在路径；目标目录缺失自动创建。
- SKILL.md：红线增加 agent/ 生成约束；压缩至 48 行。
- 五个机制脚本 docstring 的 resistance 引用补全目录层级。
- rule_edit.md 适用边界修正；SKILL.md 惩罚阈值口径与 penalty.py 一致。
- `self_update.py` compare/release 增加对过程工件目录剪枝。
- `flowchart_editor.html`：连线端点按形状真实边界计算，箭头不再被节点遮挡；点选/双击命中改为形状感知且顶层优先；新建/双击节点自动聚焦改名；节点 ID 去重。
