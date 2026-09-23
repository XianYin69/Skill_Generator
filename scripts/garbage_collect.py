"""garbage_collect.py — 垃圾回收机制（标准库）。
用途：回收工作区临时产物，避免污染目标 skill。规则见 resistance/垃圾回收机制/垃圾回收机制.md。
操作：删除 tmp 内 .tmp/.bak/.log/.part、空目录、超过保留期的下载；干跑预览用 --dry-run。
"""
import os, sys, time, argparse
if os.path.exists("SKILL.md"): raise SystemExit("拒绝：tmp 缓存不得写入 skill 目录（cwd 位于 skill 内）")

EXT = (".tmp", ".bak", ".log", ".part", ".download")

def collect(root, max_age_days=3, dry=False):
    freed = 0
    for r, dirs, fs in os.walk(root, topdown=False):
        for fn in fs:
            p = os.path.join(r, fn)
            if fn.endswith(EXT) or (time.time() - os.path.getmtime(p)) / 86400 > max_age_days:
                sz = os.path.getsize(p)
                if not dry:
                    os.remove(p)
                freed += sz
        if not os.listdir(r) and r.rstrip("\\/") != root:
            if not dry:
                os.rmdir(r)
    return freed

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--path", default="tmp")
    ap.add_argument("--age", type=int, default=3); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    n = collect(a.path, a.age, a.dry_run)
    print(f"[GC] {'预览' if a.dry_run else '已回收'} {n} 字节 <- {a.path}")