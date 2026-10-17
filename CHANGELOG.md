# CHANGELOG（变更日志）

> 本文件遵循 [rule_edit.md](rule_edit.md) 编辑规则；变更须先走 `tmp/` 镜像 + `compare → release`，禁止直接写本体。

## [2026-10-17]
### Added
- 新增变更日志规范：每次修改/新增/删除操作完成后必须在根目录 `CHANGELOG.md` 记录变更（日期、改动范围、涉及文件、违反后果）；变更日志不可缺失、不可跳过、不可事后补录（漏记视为违规）。
- 同步更新 `rule_edit.md`（新增三、变更日志规范）、`SKILL.md`（红线新增变更日志规范）、`scripts/scripts.md`（新增 pkg_templates.py / init-planned-tasks.py / lint-deps.py 索引）、`scripts/pkg_templates.py`（确保双指向依赖逻辑完整）。

---
*最后更新：2026-10-17 | 新增「变更日志」规范*
