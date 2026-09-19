# update（自更新接口）

本目录定义 Skill 的**自更新接口**。自更新严格意义上只用于「使用或测试中发现问题、纠正 skill 错误」，不是任意改写。

## 接口契约（供外部 skill 调用）

外部 skill 通过 [`scripts/self_update.py`](../scripts/self_update.py) 调用四个动作：

| 动作 | 作用 |
|---|---|
| `report` | 登记发现的使用/测试错误（含复现） |
| `compare` | 比对 `tmp/` 与目标 skill 的差异 |
| `release` | 比对通过后把 `tmp/` 释放进目标 skill |
| `clean` | 释放后删除 `tmp/` |

## 初始化即挂载

初始化完成后（见 [标记完成](../branch/流程/初始化/标记完成/标记完成.md)）即写入过程链首快照并暴露本接口，供后续自更新调用。

## 收尾比对—释放—删除

收尾流程结束前：`compare` 列差异 → 修正 → `release` 覆盖到目标 skill → `clean` 删除 `tmp/`。详见 [收尾](../branch/流程/收尾/收尾.md)。

## 运行约定

1. 自更新不得改动 [`resistance/`](../resistance/resistance.md) 中的约束红线。
2. 每次 `release` 前须冻结过程链快照，失败可回滚。
3. 纠正类更新须经 [整体审查](../branch/流程/整体审查/整体审查.md) 九项标准复核。