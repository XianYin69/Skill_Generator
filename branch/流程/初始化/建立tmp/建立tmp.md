# 建立tmp

用对应系统的脚本，在当前工作空间建立 `tmp/` 目录及初始结构。

## tmp 目录结构

`tmp/` 目录下应包含（作用与当前项目下同名文件夹一致）：

| 项目 | 类型 | 作用 |
|---|---|---|
| `.git/`、`.gitignore` | git 文件 | 版本仓库 |
| `rule_edit.md` | 文件 | 编辑规则 |
| `branch/` | 文件夹 | 分支库 |
| `flowchart/` | 文件夹 | 流程图数据 |
| `references/` | 文件夹 | 知识库 |
| `resistance/` | 文件夹 | 约束库 / 兜底 |
| `update/` | 文件夹 | 自更新组件 |

## 系统指令

- **Windows（PowerShell）**：`pwsh ./scripts/create-tmp.ps1`
- **macOS / Linux（bash）**：`bash ./scripts/create-tmp.sh`

脚本核心操作：

1. 建立 `tmp/` 及 `branch flowchart references resistance update` 五个文件夹。
2. 写入 `rule_edit.md` 占位内容。
3. 写入 `.gitignore`（忽略 `./tmp`）。
4. 在 `tmp/` 内执行 `git init`。

## 脚本文件

- [`create-tmp.ps1`](../../../../scripts/create-tmp.ps1)（Windows）
- [`create-tmp.sh`](../../../../scripts/create-tmp.sh)（macOS / Linux）

## 下一步

进入 [标记完成](../标记完成/标记完成.md)