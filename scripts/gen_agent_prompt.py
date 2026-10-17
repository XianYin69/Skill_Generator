"""gen_agent_prompt.py — 生成四格式agent提示词+SKILL.md（KiloCode格式）+asset/、dependence/、planned_tasks/ 标准目录。
提示词精简为一句话：使用 skill{name} 来完成用户请求。
新增：git 初始化并提交到功能分支，推送前询问用户确认。
"""
import argparse, os, sys, subprocess, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pkg_templates import planned, pkg_dirs, add_local_deps, strip_local_urls

def _p(t):
    s = os.path.join(t, "SKILL.md")
    if not os.path.exists(s): return "Auto-generates and iterates Agent Skills"
    body = open(s, encoding="utf-8").read().split("---")
    for l in (body[1].splitlines() if len(body) > 2 else []):
        if l.strip().startswith("description:"):
            val = l.split(":", 1)[1].strip()
            if val and val != ">": return val[:80]
    return "Auto-generates and iterates Agent Skills"

def _zh(n):
    return f"# {n}\n\n使用 `{n}` skill 来完成用户请求。"

def _en(n):
    return f"# {n} Agent Rules\n\n使用 `{n}` skill 来完成用户请求。"

def _detail(t):
    cand = [("- 流程节点：[branch/流程/](branch/流程/流程.md)", os.path.join(t, "branch", "流程", "流程.md")),
            ("- 约束兜底：[resistance/](resistance/resistance.md)", os.path.join(t, "resistance", "resistance.md"))]
    c = [a for a, b in cand if os.path.exists(b)]
    return ("\n\n## 详细流程\n" + "\n".join(c)) if c else ""

def _git(cmd, cwd=None):
    """执行 git 命令，返回 (returncode, stdout, stderr)。"""
    try:
        p = subprocess.run(
            ["git", *cmd],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30,
            encoding="utf-8",
            errors="replace"
        )
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, "", str(e)

def _init_git(target):
    """初始化 git 仓库，创建功能分支，添加文件并提交。"""
    # 检查是否已初始化
    git_dir = os.path.join(target, ".git")
    if not os.path.exists(git_dir):
        rc, _, err = _git(["init"], cwd=target)
        if rc != 0:
            print(f"[WARN] git init 失败: {err}")
            return False
    
    # 设置 git 用户信息（如果未设置）
    _git(["config", "user.name", "Skill_Generator"], cwd=target)
    _git(["config", "user.email", "skill-generator@sms.local"], cwd=target)
    
    # 创建 .gitignore（如果不存在）
    gitignore = os.path.join(target, ".gitignore")
    if not os.path.exists(gitignore):
        with open(gitignore, "w", encoding="utf-8") as f:
            f.write("tmp/\n.idea/\n.vscode/\n.kilo/\n__pycache__/\n*.pyc\n")
    
    # 创建功能分支
    name = os.path.basename(os.path.normpath(target))
    branch = f"feature/{name}"
    rc, stdout, err = _git(["checkout", "-b", branch], cwd=target)
    if rc != 0:
        # 分支可能已存在，切换到它
        rc, stdout, err = _git(["checkout", branch], cwd=target)
        if rc != 0:
            print(f"[WARN] checkout 失败: {err}")
            return False
    
    # 添加所有文件并提交
    _git(["add", "."], cwd=target)
    rc, stdout, err = _git([
        "commit",
        "-m", f"feat({name}): initial skill structure",
        "--author", f"Skill_Generator <skill-generator@sms.local>"
    ], cwd=target)
    
    if rc != 0:
        print(f"[WARN] git commit 失败: {err}")
        return False
    
    print(f"[OK] git 初始化完成，已提交到分支 {branch}")
    return True

def _ask_push(target, name):
    """询问用户是否推送到远端。"""
    print(f"\n技能 '{name}' 已创建并本地提交。")
    print("远端仓库: https://github.com/XianYin69/Skill_Generator.git")
    answer = input("是否推送到远端？(yes/no): ").strip().lower()
    return answer in ("yes", "y", "是")

def gen(target, name=None, version="0.1.0", push_remote=False):
    """批29 P3-11：version 为必填元数据（缺省 0.1.0）——巡检据此做「本地版本 vs 上游版本」比对。
    参数 push_remote: 是否自动推送到远端（默认 False，需用户确认）
    """
    os.makedirs(target, exist_ok=True)
    n = name or os.path.basename(os.path.normpath(target))
    p = _p(target)
    v = str(version or "0.1.0")
    z, e = _zh(n), _en(n)
    open(os.path.join(target, "SKILL.md"), "w", encoding="utf-8").write(
        f"---\nname: {n}\nversion: {v}\ndescription: >\n  {p}\nlicense: MIT\nmetadata:\n  category: development\n---\n\n"
        + z + _detail(target) + "\n")
    out = os.path.join(target, "agent"); os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "CLAUDE.md"), "w", encoding="utf-8").write(z)
    open(os.path.join(out, "agent_prompt.md"), "w", encoding="utf-8").write(z)
    open(os.path.join(out, ".cursorrules"), "w", encoding="utf-8").write(e)
    open(os.path.join(out, "instructions.md"), "w", encoding="utf-8").write(e)
    pkg_dirs(target); planned(target)
    print("[OK] SKILL.md + agent/ + asset/ + dependence/ + planned_tasks/ 已生成（提示词一句话：使用 skill名 来完成用户请求）")
    
    # 添加本地依赖
    deps_path = os.path.join(target, "dependence", "deps.json")
    add_local_deps(deps_path, n)
    print(f"[OK] 已添加本地依赖: local://{n}")
    
    # 执行 git 操作
    _init_git(target)
    
    if push_remote or _ask_push(target, n):
        # 推送前移除本地依赖
        strip_local_urls(deps_path)
        _git(["add", "."], cwd=target)
        _git(["commit", "-m", f"chore({n}): remove local deps before push"], cwd=target)
        
        # 添加远端（如果未配置）
        rc, stdout, err = _git(["remote", "get-url", "origin"], cwd=target)
        if rc != 0:
            default_remote = "https://github.com/XianYin69/Skill_Generator.git"
            _git(["remote", "add", "origin", default_remote], cwd=target)
        
        # 推送到远端
        rc, stdout, err = _git(["push", "-u", "origin", "HEAD"], cwd=target)
        if rc != 0:
            print(f"[WARN] git push 失败: {err}")
        else:
            print(f"[OK] 已推送到远端")
            # 恢复本地依赖
            add_local_deps(deps_path, n)
            print(f"[OK] 已恢复本地依赖: local://{n}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--name")
    ap.add_argument("--version", default="0.1.0")
    ap.add_argument("--push", action="store_true", help="自动推送到远端（跳过确认）")
    a = ap.parse_args()
    gen(a.target, a.name, a.version, push_remote=a.push)
