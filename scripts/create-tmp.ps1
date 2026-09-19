# 建立 tmp 目录及初始结构（Windows PowerShell）
param(
    [string]$Target = "."
)

$tmp = Join-Path $Target "tmp"
$folders = @("branch", "flowchart", "references", "resistance", "update")

# 1. 建立 tmp 及初始文件夹
New-Item -ItemType Directory -Path $tmp -Force | Out-Null
foreach ($f in $folders) {
    New-Item -ItemType Directory -Path (Join-Path $tmp $f) -Force | Out-Null
}

# 2. 写入 rule_edit.md 占位内容
$rule = @"
# RULE_EDIT（编辑规则）

> 待补充本 Skill 的编辑规则。
"@
Set-Content -Path (Join-Path $tmp "rule_edit.md") -Value $rule -Encoding UTF8

# 3. 写入 .gitignore
Set-Content -Path (Join-Path $tmp ".gitignore") -Value "./tmp" -Encoding UTF8

# 4. 初始化 git 仓库
Push-Location $tmp
git init 2>&1 | Out-Null
Pop-Location

Write-Output "tmp 目录已建立：$tmp"