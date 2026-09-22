# 生成agent工具提示词

释放完成后调用 `gen_agent_prompt.py --target <目标skill>`，自动生成：
1. **SKILL.md**（目标 skill 根）— KiloCode 兼容格式（YAML frontmatter + 系统提示词），≤50 行。
2. **agent/** 四格式提示词（`CLAUDE.md`/`.cursorrules`/`instructions.md`/`agent_prompt.md`）。

description 从用户提供的 SKILL.md frontmatter 读取；缺失时回退默认值。

## 决策分支

-  [沙盒交付](../沙盒交付/沙盒交付.md)

---