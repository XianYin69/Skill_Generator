# git操作

约束：[git 工作流约束](../../../../resistance/git工作流约束/git工作流约束.md)

操作节点。

## 操作要点

1. 工作前 `git fetch`，远端有更新先 `git pull --ff-only`。
2. 若仓库未 `git init`（无 `.git/`），则自动执行 `git init`。
3. 核对 `.gitignore`：必含 `tmp/` 与 IDE 文件夹（`.idea/`、`.vscode/`、`.kilo/` 等）。
4. 每步完成后提交到非 main/dev 的功能分支（`feature/<topic>`）。
5. 功能审核通过 → 合并 dev；整体审核通过 → dev 合入 main。
6. 推送前询问用户是否推送至远端：是 → `git push`；否 → 仅保留本地提交。
7. 建仓/推送前判定仓库可见性（见约束第 10 条）：疑似违规或含保密内容 → PRIVATE，否则 PUBLIC；判定不了问用户。
8. 附属/私有子技能（`software_use_only-*` 等）走双仓模型（见约束第 11 条）：本体仓 PUBLIC 且 ignore `private/`，附属内容进 `private/` 独立私有伴生仓（PRIVATE），禁止不入库、禁止误推公开仓。

## 决策分支

- → [完成skill开发](../完成skill开发/完成skill开发.md)
- → [收尾操作](../收尾操作/收尾操作.md)

---
