# 加入MIT协议

操作节点。初始化阶段为工作空间写入 **MIT 协议**许可，使技能包从建立起就带 license，交付/安装方无需再补。

## 操作要点

1. 写入位置：工作空间根 `LICENSE`；存在 `tmp/` 时同步镜像 `tmp/LICENSE`（收尾释放到目标 skill）。
2. 版权方：`--holder` 由用户指定；未指定时取 `<技能名> authors`，年份取当年。
3. 已有 `LICENSE` → 跳过不覆盖；确需替换须 `--replace --yes`，并先向用户预览确认。
4. 默认预览（dry-run），仅 `--yes` 写盘，与「不得静默写盘」红线一致。
5. 口径一致：SKILL.md frontmatter 的 `license: MIT` 由 [gen_agent_prompt.py](../../../../scripts/gen_agent_prompt.py) 写入，本节点负责协议全文。

## 命令

```
python scripts/add-mit-license.py --target <工作空间> [--holder 版权方] [--yes]
```

脚本：[`add-mit-license.py`](../../../../scripts/add-mit-license.py)（MIT 全文模板，≤50 行）

## 分支

- **成功（写入/跳过）** → [建立计划任务](../建立计划任务/建立计划任务.md)
- **目标工作空间不存在** → 脚本报 `action=error` 不写盘，回 [判断目录](../判断目录/判断目录.md) 确认路径
- **根目录不可写** → 记录错误并转 [沙盒机制约束](../../../../resistance/沙盒机制/沙盒机制.md) 降级确认目标目录
