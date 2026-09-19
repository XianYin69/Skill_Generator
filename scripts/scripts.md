# scripts（脚本库）

本目录存放可执行的辅助脚本：校验、迁移、生成、格式化工具等。

## 应存什么

- 独立运行的 Python / Shell / PowerShell 脚本。
- 工具本身 ≤ 50 行（超则拆为「入口脚本 + 模块」）。
- 以 `.py` / `.ps1` / `.sh` 为扩展名，文件名小写、中横线分隔。

## 当前内容

- [`check-links.py`](check-links.py)：悬空链接校验器（rule_edit.md 要求）。
- [`create-tmp.ps1`](create-tmp.ps1)：建立 tmp 目录及初始结构（Windows）。
- [`create-tmp.sh`](create-tmp.sh)：建立 tmp 目录及初始结构（macOS / Linux）。

## 运行约定

1. 使用项目的默认 Python。
2. 任何可能写入磁盘的脚本必须加 `--dry-run` 默认模式。
3. 运行前先看 [resistance](../resistance/resistance.md) 确认权限与回滚策略。
