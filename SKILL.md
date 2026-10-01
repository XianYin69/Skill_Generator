---
name: Skill_Generator
description: >
  自动生成与迭代 Agent Skill 的智能体。创建路径覆盖初始化（含加入MIT协议、建立计划任务）→需求确认→经验查询→大纲构建→分支分析→脚本构建→知识库构建（穷尽至不可再拓扑）→约束编写→整体审查→收尾；修改路径覆盖初始化→修改流程；生成 KiloCode YAML frontmatter 的 SKILL.md、agent/ 四格式提示词与 asset/＋dependence/＋planned_tasks/ 标准目录，五机制（垃圾回收/上下文压缩/逻辑链/过程链/惩罚）+沙盒兜底，未指定目录时固定路径沙盒作业。
license: MIT
metadata:
  category: development
---

# Skill_Generator

使用 `Skill_Generator` skill 来完成用户请求。自动生成与迭代 Agent Skill 的智能体。

## 工作原则

1. **按流程执行**：不跳步、不静默越权；决策节点须留逻辑链。
2. **双链辩论**：审查节点运行正反双链（logic_chain.py debate）。
3. **返回机制**：审查失败记中断（process_chain.py interrupt），修复后 resume 返回；任一路径完成（创建收尾「完成」/修改「完成项目修改」）＝收口子会话返回 SMS 主流程由其整合续排，不得以子技能完成结束整段对话。
4. **惩罚熔断**：重试达 10 次即熔断，强制回退或求助用户。
5. **垃圾回收**：tmp 收尾后释放到目标 skill 并删除；未指定目标目录时在固定路径沙盒作业，交付后删除沙盒。

## 执行路径

**创建路径**：初始化→需求确认→经验查询→大纲构建→分支分析→脚本构建→知识库构建（穷尽至知识树不可再拓扑新领域）→约束编写→整体审查→收尾→**完成**
**修改路径**：初始化→修改流程→**完成**

> 完成收尾后不会进入修改流程。

## 可用工具（scripts/）

scripts/gen_agent_prompt.py / scripts/knowledge_browser.py / scripts/knowledge_download.py / scripts/knowledge_convert.py / scripts/logic_chain.py / scripts/process_chain.py / scripts/garbage_collect.py / scripts/context_compress.py / scripts/penalty.py / scripts/self_update.py / scripts/check-links.py / scripts/flowchart_editor.py / scripts/sandbox.py / scripts/add-mit-license.py / scripts/init-planned-tasks.py / scripts/lint-deps.py

> `scripts/gen_agent_prompt.py` 同时生成目标 skill 的 `SKILL.md`（KiloCode YAML frontmatter）+ `agent/` 四格式提示词 + `asset/`（技能包资产）与 `dependence/`（依赖的技能包/软件/仓库地址·每条依赖 deps.json 必附 `source_url` 原始链接）与 `planned_tasks/`（计划任务声明·到期由 SMS 调度器执行）标准目录；`scripts/gen_agent_prompt.py` 同时落 `dependence/deps.json` 骨架。

## 红线

- 不得跳过初始化（含「加入MIT协议」写入工作区根与 tmp 的 MIT `LICENSE`、「建立计划任务」写入 `planned_tasks/`（README.md＋template.json），已有则不覆盖）；不得静默写盘（`--dry-run` 默认）；不得删除 resistance/ 约束。
- 悬空链接必须为 0；所有 .md / 脚本 ≤ 50 行；缓存文件不得写入 skill 目录（一律落用户缓存目录）。
- 文件夹名=流程名；脚本使用英文名称。
- 依赖必须附原始链接：`dependence/deps.json` 每条字段 `name/source_url/license/version/install/checked_at`，`source_url` 为 GitHub/GitLab/官方仓库或发布页原始链接（本地技能 `local://<skill-id>`）；缺 `source_url` 即判不合格，`lint-deps.py` 报错退出；先网页检索定位原始链接再写清单。
- 计划任务：一任务一文件 `pt-<skill>-<slug>.json`，schema 字段名与 SMS 读取端一致不得改动；原子写；`status` 仅 pending/running/done/paused/failed；时间一律本地 ISO；到期由 SMS 调度器读取执行并挂 session 关联链，**技能自身不得自行执行计划任务**；删除文件即注销。
- 生成的 SKILL.md 必须含 YAML frontmatter；提示词（SKILL.md 与 agent/ 四格式）一句话精简：使用 skill名 来完成用户请求；新技能标准目录含 asset/（技能包资产）与 dependence/（依赖的技能包/软件/仓库地址·SMS 安装时同检同净化）。
- Git 工作流：每步完成后提交到非 main/dev 的功能分支；功能审核通过→合并到 dev；整体审查通过→dev 合入 main 并推送；详见 [git工作流约束](resistance/git工作流约束/git工作流约束.md)。

## 详细流程

- 流程节点：[branch/流程/](branch/流程/流程.md)；约束兜底：[resistance/](resistance/resistance.md)
