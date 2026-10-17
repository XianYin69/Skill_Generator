#!/usr/bin/env python3
"""self_update.py — 自更新接口（标准库，供外部 skill 调用）。
定位：自更新仅用于「使用/测试中发现并纠正 skill 错误」，不是任意改写。
外部 skill 调用契约（CLI）：
    python self_update.py report  --skill <名> --error <错误描述> [--repro <复现>]
    python self_update.py compare --tmp <tmp目录> --target <目标skill目录>
    python self_update.py release --tmp <tmp目录> --target <目标skill目录>   # 比对通过后释放
    python self_update.py clean   --tmp <tmp目录>                            # 释放后删除 tmp
    python self_update.py push    --tmp <tmp目录> --target <目标skill目录> --branch <分支名>  # 推送到远端
约束见 resistance/惩罚机制、resistance/垃圾回收机制。
"""
import os, sys, json, time, argparse, shutil, filecmp, subprocess

_SKIP = ("state", "updates", ".git", "__pycache__", ".pytest_cache")

def _log(entry):
    assert not os.path.exists("SKILL.md"), "拒绝：tmp 缓存不得写入 skill 目录（cwd 位于 skill 内）"
    os.makedirs("tmp/updates", exist_ok=True)
    with open("tmp/updates/updates.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def report(a):
    _log({"t": time.time(), "type": "error", "skill": a.skill, "error": a.error, "repro": a.repro})
    print("[自更新] 错误已登记，等待纠正流程")

def compare(a):
    diff = []
    for root, ds, fs in os.walk(a.tmp):
        ds[:] = [d for d in ds if d not in _SKIP]
        for fn in fs:
            s = os.path.join(root, fn)
            rel = os.path.relpath(s, a.tmp)
            d = os.path.join(a.target, rel)
            if not os.path.exists(d) or not filecmp.cmp(s, d, shallow=False):
                diff.append(rel)
    _log({"t": time.time(), "type": "compare", "diff": diff})
    print(f"[自更新] 差异 {len(diff)} 项：", ", ".join(diff[:10]))
    return diff

def release(a):
    if compare(a) is None:
        return
    shutil.copytree(a.tmp, a.target, dirs_exist_ok=True, ignore=shutil.ignore_patterns(*_SKIP))
    _log({"t": time.time(), "type": "release", "to": a.target})
    print("[自更新] tmp 已释放到目标 skill")

def push(a):
    # 切换到目标 skill 目录并推送
    os.chdir(a.target)
    branch = a.branch if a.branch else "feature/update-push-and-deps"
    cmds = [
        ["git", "add", "-A"],
        ["git", "commit", "-m", "docs: update self_update interface with push support"],
        ["git", "push", "origin", branch],
    ]
    for cmd in cmds:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[自更新] 推送失败: {result.stderr}")
            return False
    _log({"t": time.time(), "type": "push", "branch": branch})
    print(f"[自更新] 已成功推送到远端分支: {branch}")
    return True

def clean(a):
    if os.path.isdir(a.tmp):
        shutil.rmtree(a.tmp)
        _log({"t": time.time(), "type": "clean", "path": a.tmp})
        print(f"[自更新] 已删除 {a.tmp}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    
    r = sub.add_parser("report")
    r.add_argument("--skill")
    r.add_argument("--error")
    r.add_argument("--repro")
    
    for name in ("compare", "release"):
        s = sub.add_parser(name)
        s.add_argument("--tmp", required=True)
        s.add_argument("--target", required=True)
    
    p = sub.add_parser("push")
    p.add_argument("--tmp", required=True)
    p.add_argument("--target", required=True)
    p.add_argument("--branch", default="feature/update-push-and-deps")
    
    c = sub.add_parser("clean")
    c.add_argument("--tmp", required=True)
    
    a = ap.parse_args()
    {"report": report, "compare": compare, "release": release, "push": push, "clean": clean}[a.cmd](a)
