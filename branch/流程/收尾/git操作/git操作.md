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

## 决策分支

- → [完成skill开发](../完成skill开发/完成skill开发.md)
- → [收尾操作](../收尾操作/收尾操作.md)

---
