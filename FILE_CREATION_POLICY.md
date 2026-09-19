# FILE_CREATION_POLICY（文件创建策略）

> **状态：规划中，尚未实现。**

本文件将规定 Skill_Generator 在执行期对工程工作区创建文件与目录的权限边界：
- 允许创建的文件类型与位置。
- 需要询问用户的场景（根目录、敏感路径）。
- 禁止创建或需审批的场景。

预期结构：
- 创建权限白名单。
- 命名规则与冲突处理。
- 与 `resistance/约束库` 的关联。

详见 [`resistance/`](resistance/) 与 [`rule_edit.md`](rule_edit.md)。
