"""lint-deps.py — 校验 dependence/deps.json：每条依赖必须附原始链接 source_url，缺项即判不合格并报错退出。"""
import argparse, json, os, sys

REQ = ("name", "source_url", "license", "version", "install", "checked_at")
SCHEME = ("http://", "https://", "local://", "file://")

def load(path):
    if not os.path.exists(path): return None, [f"{path}: 缺失（每条依赖须登记 deps.json）"]
    try:
        d = json.load(open(path, encoding="utf-8-sig"))
    except Exception as e:
        return None, [f"{path}: JSON 解析失败 {e}"]
    if isinstance(d, dict): d = d.get("dependencies") or d.get("deps") or []
    if not isinstance(d, list): return None, [f"{path}: 顶层须为数组或 {{dependencies:[...]}}"]
    return d, []

def lint(root, strict_url=True):
    path = os.path.join(root, "dependence", "deps.json")
    deps, errs = load(path)
    if deps is None: return errs
    if not deps: return []
    for i, e in enumerate(deps):
        tag = f"{path}[{i}] {e.get('name', '?') if isinstance(e, dict) else '?'}"
        if not isinstance(e, dict): errs.append(f"{tag}: 条目须为对象"); continue
        for k in REQ:
            if k not in e: errs.append(f"{tag}: 缺字段 {k}")
        u = (e.get("source_url") or "").strip()
        if not u: errs.append(f"{tag}: 缺 source_url（原始链接·缺即不合格）")
        elif strict_url and not u.startswith(SCHEME):
            errs.append(f"{tag}: source_url 非原始链接 {u}")
        if e.get("source_url_status") not in (None, "verified", "unverified"):
            errs.append(f"{tag}: source_url_status 仅 verified/unverified")
    return errs

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="依赖原始链接 lint")
    ap.add_argument("--root", default=os.getcwd()); ap.add_argument("--allow-any-url", action="store_true")
    a = ap.parse_args(); r = lint(a.root, not a.allow_any_url)
    if r:
        print(f"依赖 lint 不合格（{len(r)} 项）："); [print("  " + x) for x in r]; sys.exit(1)
    print("依赖 lint 通过：每条依赖均附 source_url 原始链接。")
