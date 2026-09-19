# references（知识库）

本目录存放 Skill 运行与生成的参考内容：文档、数据、流程图等。

## 应存什么

- 只读或低频更新的素材，不属于代码、不属于约束红线。
- 以「主题」命名子目录，保持平铺或一层树。
- 单文件 ≤ 50 行（超则拆为「总索引 + 子文件」）。

## 当前内容

- [`flowchart/`](../flowchart/)：整个 Skill_Generator 流程图的链表 JSON，由 `Skill_Generator_stream.html` 转换而来。入口 [`flowchart/index.json`](../flowchart/index.json)。
- [`流程/`](../branch/流程/流程.md)：各阶段执行流程（已移至 branch/）。
- [`约束部分/`](../resistance/约束部分/约束部分.md)：约束区域（已移至 resistance/）。

## 编辑约定

1. 新建子目录或大文件前，先在本文件登记一行。
2. 删除或重命名现有内容后同步更新本文件。
3. 本目录不参与 `scripts/check-links.py` 的逻辑校验，但请确保文件名在 `SKILL.md` 索引里能找到。
