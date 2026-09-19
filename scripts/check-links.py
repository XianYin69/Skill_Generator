#!/usr/bin/env python3
"""check-links.py — 校验项目内所有 markdown 链接是否有效。"""
import argparse, os, re, sys

def find_md(root):
    files = []
    for dpath, dirs, fs in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ('tmp', '.git', '__pycache__', '.kilo')]
        files += [os.path.join(dpath, f) for f in fs if f.endswith('.md')]
    return files

def links(content, base_dir):
    out = []
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        t = m.group(2)
        if t.startswith('http') or t.startswith('#') or '://' in t:
            continue
        out.append((t, os.path.normpath(os.path.join(base_dir, t))))
    return out

def check(root):
    orphans = []
    for f in find_md(root):
        try:
            c = open(f, encoding='utf-8').read()
        except Exception:
            continue
        for t, full in links(c, os.path.dirname(f)):
            if not os.path.exists(full):
                orphans.append((os.path.relpath(f, root), t))
    return orphans

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    a = ap.parse_args()
    o = check(a.root)
    if o:
        print(f'发现 {len(o)} 个悬空链接：')
        for f, t in o:
            print(f'  {f} -> {t}')
        sys.exit(1)
    print('无悬空链接，校验通过。')