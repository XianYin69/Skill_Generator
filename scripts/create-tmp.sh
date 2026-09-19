#!/usr/bin/env bash
# 建立 tmp 目录及初始结构（macOS / Linux）
set -e

TARGET="${1:-.}"
TMP="$TARGET/tmp"

# 1. 建立 tmp 及初始文件夹
mkdir -p "$TMP"/branch "$TMP"/flowchart "$TMP"/references "$TMP"/resistance "$TMP"/update

# 2. 写入 rule_edit.md 占位内容
cat > "$TMP/rule_edit.md" <<'EOF'
# RULE_EDIT（编辑规则）

> 待补充本 Skill 的编辑规则。
EOF

# 3. 写入 .gitignore
printf './tmp\n' > "$TMP/.gitignore"

# 4. 初始化 git 仓库
git -C "$TMP" init -q

echo "tmp 目录已建立：$TMP"