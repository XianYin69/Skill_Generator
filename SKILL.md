# SKILL_Generator 入口

本 Skill 用于自动生成与迭代 Agent Skill。读本目录下的子模块即可按需取用。

## 子模块索引

| 模块 | 用途 | 说明 |
|---|---|---|
| [`references/`](references/) | 知识库 | 文档、素材、流程图等只读或低频更新内容 |
| [`scripts/`](scripts/) | 脚本库 | 可执行校验、迁移、格式化工具 |
| [`branch/`](branch/) | 分支库 | 各阶段的备选路径与实验性方案 |
| [`update/`](update/) | 自更新组件 | 本 Skill 自身的升级触发与回滚逻辑 |
| [`resistance/`](resistance/) | 约束库 / 兜底 | 规则边界、不可逾越的红线、异常降级策略 |

## 执行流程

创建与修改是两条独立路径，各自从「初始化」开始。

### 创建路径

[`初始化/`](references/流程/初始化/) → [`需求确认/`](references/流程/需求确认/) → [`经验查询/`](references/流程/经验查询/) → [`大纲构建/`](references/流程/大纲构建/) → [`分支分析/`](references/流程/分支分析/) → [`脚本构建/`](references/流程/脚本构建/) → [`知识库构建/`](references/流程/知识库构建/) → [`约束编写/`](references/流程/约束编写/) → [`整体审查/`](references/流程/整体审查/) → [`收尾/`](references/流程/收尾/) → **完成**

### 修改路径

[`初始化/`](references/流程/初始化/) → [`修改流程/`](references/流程/修改流程/) → **完成**

> 两条路径各自独立，完成收尾后不会进入修改流程。

## 阅读顺序

1. 先看本文件（SKILL.md）了解结构。
2. 有具体需求时，根据上表跳转到对应子模块。
3. 修改规范/脚本前必读 [`resistance/`](resistance/)，防止越界。

## 编辑规范

本项目遵循 [`rule_edit.md`](rule_edit.md)。
