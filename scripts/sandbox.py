#!/usr/bin/env python3
"""sandbox.py — 固定路径沙盒：SG_SANDBOX_HOME→缓存目录→根目录建临时工作区；create/list/deliver/clean（交付与删除默认预览，--yes 执行）。"""
import os, sys, time, shutil, json


def base():
    if os.environ.get("SG_SANDBOX_HOME"):
        return os.path.join(os.environ["SG_SANDBOX_HOME"], "sandbox")
    home = os.path.expanduser("~")
    if sys.platform == "win32":
        cache = os.environ.get("LOCALAPPDATA") or home
    elif sys.platform == "darwin":
        cache = os.path.join(home, "Library", "Caches")
    else:
        cache = os.environ.get("XDG_CACHE_HOME") or os.path.join(home, ".cache")
    return os.path.join(cache, "Skill_Generator", "sandbox")


def create(name):
    p = os.path.join(base(), time.strftime("%Y-%m-%d") + "-" + (name or "skill"))
    os.makedirs(p, exist_ok=True)
    return p


def deliver(sb, to, yes):
    if not os.path.isdir(sb): return {"error": "沙盒不存在: " + sb}
    if not to: return {"error": "须由用户指定目标工作区路径 --to"}
    if os.path.isdir(to) and os.listdir(to): return {"error": "目标路径非空，拒绝覆盖: " + to}
    if not yes: return {"preview": True, "copy": sb + " -> " + to, "hint": "--yes 执行复制"}
    shutil.copytree(sb, to, dirs_exist_ok=True)
    return {"copied": to, "files": sum(len(f) for _, _, f in os.walk(to))}


def clean(sb, yes):
    if not os.path.isdir(sb): return {"error": "沙盒不存在: " + sb}
    if not yes: return {"preview": True, "remove": sb, "hint": "仅 deliver 成功后删除；--yes 执行"}
    shutil.rmtree(sb)
    return {"removed": sb}


if __name__ == "__main__":
    a = sys.argv[1:]
    def _f(flag): return a[a.index(flag) + 1] if flag in a and a.index(flag) + 1 < len(a) else ""
    cmd = a[0] if a else "list"
    if cmd == "create": print(create(_f("--name") or "skill"))
    elif cmd == "list": print(json.dumps(sorted(os.listdir(base())) if os.path.isdir(base()) else [], ensure_ascii=False))
    elif cmd == "deliver": print(json.dumps(deliver(_f("--id"), _f("--to"), "--yes" in a), ensure_ascii=False))
    elif cmd == "clean": print(json.dumps(clean(_f("--id"), "--yes" in a), ensure_ascii=False))
    else: print("用法: create --name N | list | deliver --id P --to T [--yes] | clean --id P [--yes]")
