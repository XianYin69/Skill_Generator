# RULE_EDIT（编辑规则）

> 本项目规范与文档的编辑规则；Agent 与贡献者必须遵守。
> 适用边界：本文件管 **skill 本体的编辑**（`SKILL.md`、`references/`、`scripts/`、`branch/`、`update/`、`CHANGELOG.md`）；执行期在工程工作区创建文件与目录的范围与权限，管在 [`FILE_CREATION_POLICY.md`](FILE_CREATION_POLICY.md) 与 [`resistance/约束部分/约束部分.md`](resistance/约束部分/约束部分.md)。

## 一、约束

- 约束文本（markdown）长度 ≤ 50 行；脚本 `.py/.ps1/.sh/.cmd` 不受 50 行限制。
- 使用自然语言
- 文件夹名为流程名
- markdown名和其他文件名为 流程名 + 扩展名
- 流程名文件夹下必须包含流程名markdown
- script脚本使用英文名称 + 拓展名

## 二、编辑流程

1. 识别要编辑或新建的规范、文档。
2. 询问用户：需要预留哪些部分？
3. 判断该 markdown 部分是否过长（超过 50 行）：过长则用「总索引 + 子文件」拆分，否则跳过拆分（脚本不限行数，按职责拆分即可）。
4. 询问用户：是否需要新建文件或文件夹？
5. 将变更在 `tmp/` 镜像中执行（遵守「markdown 文本 ≤ 50 行 + 自然语言」，脚本不限行数）；禁止直接写入 skill 本体目录。
6. 运行 `python scripts/check-links.py --root tmp`（全树悬空链接必须为 0，孤立文档需接链或说明）。
7. 执行 `python scripts/self_update.py compare --tmp tmp --target <skill根目录>`；有差异则修正 tmp/ 后重跑步骤 5–6 直至无差异。
8. 执行 `python scripts/self_update.py release --tmp tmp --target <skill根目录>` 将 tmp/ 释放到目标 skill。
9. 更新 CHANGELOG.md（记录本次变更）。
10. 提交 git。

## 三、变更日志规范

**每次修改/新增/删除操作完成后，必须在根目录 `CHANGELOG.md` 记录变更**：

- **记录内容**：日期、改动范围、涉及文件、违反后果。
- `CHANGELOG.md` 本身也是变更产物，写入时需同步更新本条规范（本条除外）。
- **审核流程**：`compare` 差异列明 → `release` 覆盖本体 → `git commit -m "docs: changelog update"`。
- **约束红线**：变更日志不可缺失、不可跳过、不可事后补录（漏记视为违规）。

---
*最后更新：2026-10-17 | 新增「变更日志」规范*
