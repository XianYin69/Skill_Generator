# Skill_Generator

Agent 级 Skill 生成工具：自动生成与迭代 Agent Skill，创建/修改双路径，内容修改一律走 tmp 镜像 + 自更新接口。

## 执行路径

- **创建**：初始化 → 需求确认 → 经验查询 → 大纲构建 → 分支分析 → 脚本构建 → 知识库构建 → 约束编写 → 整体审查 → 收尾
- **修改**：初始化 → 修改流程 → 完成

## 结构

- [`SKILL.md`](SKILL.md)：入口（YAML frontmatter，可直接注入 agent），子模块索引与阅读顺序。
- [`agent/`](agent/)：四格式提示词（CLAUDE.md / .cursorrules / instructions.md / agent_prompt.md），由 `gen_agent_prompt.py` 生成。
- [branch](branch/branch.md)：分支库；主干为 [`branch/流程/`](branch/流程/流程.md) 11 步骤、164 个节点（初始化含「加入MIT协议」）。
- [scripts](scripts/scripts.md)：脚本库（logic_chain / process_chain / self_update / check-links 等，英文名；脚本不限行数，建议按职责拆分）。
- [dependence](dependence/dependence.md)：依赖清单＋`deps.json`（每条依赖必附 `source_url` 原始链接，`python scripts/lint-deps.py` 校验）。
- [planned_tasks](planned_tasks/README.md)：计划任务声明目录（一任务一文件 `pt-<skill>-<slug>.json`，到期由 SMS 调度器执行）。
- [references](references/references.md)：知识库（文档、素材、流程图、信用评级）。
- [resistance](resistance/resistance.md)：约束库/兜底（红线、降级策略、[git工作流约束](resistance/git工作流约束/git工作流约束.md)）。
- [update](update/update.md)：自更新接口（report / compare / release / clean），本 skill 本体唯一写盘通道。
- [flowchart](flowchart/index.json)：项目流程图链表 JSON（源于 `Skill_Generator_stream.html`，flowchart_editor 可编辑）。
- [`CHANGELOG.md`](CHANGELOG.md) / [`CONTRIBUTORS.md`](CONTRIBUTORS.md) / [`LICENSE`](LICENSE)：版本记录、贡献者、MIT 许可。

## 红线摘要

- 悬空链接必须为 0（增删移后运行 `python scripts/check-links.py`）；所有 .md ≤ 50 行（50 行红线只约束 markdown 文本；脚本 .py/.ps1/.sh/.cmd 不限行数，但仍禁裸 except、print 调试残留、>100 字符长行、超长函数）。
- 不得静默写盘：先在 `tmp/` 镜像变更，再 compare → release 释放；禁止删除 resistance/ 约束。
- 审查节点运行正反双链辩论（logic_chain.py debate）；重试达 10 次触发惩罚熔断。
- Git 工作流：每步提交到非 main/dev 的功能分支；功能审核通过→dev；整体审核通过→main 并推送；远端有更新先 pull；推送前判定可见性（疑似违规/涉密须 PRIVATE，详见 [git工作流约束](resistance/git工作流约束/git工作流约束.md)第 10 条）。

## 编辑规则

遵循 [`rule_edit.md`](rule_edit.md)、[`FILE_CREATION_POLICY.md`](FILE_CREATION_POLICY.md)：markdown 编辑操作 ≤ 50 行 + 自然语言 + 悬空链接为 0（脚本 .py/.ps1/.sh/.cmd 不限行数）。
