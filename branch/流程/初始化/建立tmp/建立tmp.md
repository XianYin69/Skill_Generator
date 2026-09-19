# 建立tmp

用对应系统的脚本，在当前工作空间建立 `tmp/` 目录及初始结构。

## tmp 目录结构

以下项目均为 `tmp/` 的直接子项（内容与当前项目根目录同名项一致）：

| 项目 | 完整路径 | 类型 | 作用 |
|---|---|---|---|
| `.git/`、`.gitignore` | `tmp/.git/`、`tmp/.gitignore` | git 文件 | 版本仓库 |
| `rule_edit.md` | `tmp/rule_edit.md` | 文件 | 编辑规则（内容与根目录 rule_edit.md 一致） |
| `branch/` | `tmp/branch/` | 子目录 | 分支库 |
| `flowchart/` | `tmp/flowchart/` | 子目录 | 流程图数据 |
| `references/` | `tmp/references/` | 子目录 | 知识库 |
| `resistance/` | `tmp/resistance/` | 子目录 | 约束库 / 兜底 |
| `update/` | `tmp/update/` | 子目录 | 自更新组件 |

## 系统指令

- **Windows（PowerShell）**：`pwsh ./scripts/create-tmp.ps1`
- **macOS / Linux（bash）**：`bash ./scripts/create-tmp.sh`

脚本核心操作：

1. 在目标工作空间建立 `tmp/` 目录。
2. 在 `tmp/` 下建立五个子目录：`branch/`、`flowchart/`、`references/`、`resistance/`、`update/`。
3. 在 `tmp/` 下写入 `rule_edit.md`（内容与项目根目录 `rule_edit.md` 完全一致）。
4. 在 `tmp/` 下写入 `.gitignore`（忽略 `./tmp`）。
5. 在 `tmp/` 内执行 `git init` 初始化仓库。

## 脚本文件

- [`create-tmp.ps1`](../../../../scripts/create-tmp.ps1)（Windows）
- [`create-tmp.sh`](../../../../scripts/create-tmp.sh)（macOS / Linux）

## 下一步

进入 [标记完成](../标记完成/标记完成.md)