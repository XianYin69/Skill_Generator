# references（知识库）

本目录存放 Skill 运行与生成的参考内容：文档、数据、流程图等。

## 应存什么

- 只读或低频更新的素材，不属于代码、不属于约束红线。
- 以「主题」命名子目录，保持平铺或一层树。
- 单文件 ≤ 50 行（超则拆为「总索引 + 子文件」）。

## 当前内容

- [`flowchart/`](../flowchart/)：整个 Skill_Generator 流程图的链表 JSON，由 `Skill_Generator_stream.html` 转换而来。入口 [`flowchart/index.json`](../flowchart/index.json)。
- [`流程/`](流程/)：SKILL.md 拆分的各阶段执行细则，含初始化及 01–10 共 11 个独立步骤文件夹。
- [`流程/`](流程/)：SKILL.md 拆分的各阶段执行细则，按 01–10 编号。

## 编辑约定

1. 新建子目录或大文件前，先在本 README 登记一行。
2. 删除或重命名现有内容后同步更新本 README。
3. 本目录不参与 `scripts/check-links.py` 的逻辑校验，但请确保文件名在 `SKILL.md` 索引里能找到。
