#!/usr/bin/env python3
"""check-links.py — 校验项目内所有 markdown 链接是否有效。
用法: python scripts/check-links.py [--root DIR]
返回 0 表示无悬空链接，返回 1 表示存在悬空链接。
"""

import argparse
import os
import re
import sys


def find_markdown_files(root):
    """递归查找所有 .md 文件，排除 tmp/ 与 .git/。"""
    md_files = []
    for dirpath, dirs, files in os.walk(root):
        # 跳过敏感目录
        dirs[:] = [d for d in dirs if d not in ('tmp', '.git', '__pycache__', '.kilo')]
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return md_files


def extract_links(content, base_dir):
    """从 markdown 内容中提取所有相对路径链接。"""
    links = []
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        target = m.group(2)
        # 跳过 URL、锚点、协议
        if target.startswith('http') or target.startswith('#'):
            continue
        if '://' in target:
            continue
        # 解析相对路径
        full = os.path.normpath(os.path.join(base_dir, target))
        links.append((target, full))
    return links


def check_links(root):
    """检查所有链接，返回悬空链接列表。"""
    orphans = []
    md_files = find_markdown_files(root)
    for fpath in md_files:
        base_dir = os.path.dirname(fpath)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        for target, full in extract_links(content, base_dir):
            if not os.path.exists(full):
                rel = os.path.relpath(fpath, root)
                orphans.append((rel, target))
    return orphans


def main():
    parser = argparse.ArgumentParser(description='检查 markdown 链接有效性')
    parser.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = parser.parse_args()

    orphans = check_links(args.root)
    if orphans:
        print(f'发现 {len(orphans)} 个悬空链接：')
        for f, t in orphans:
            print(f'  {f} -> {t}')
        sys.exit(1)
    else:
        print('无悬空链接，校验通过。')
        sys.exit(0)


if __name__ == '__main__':
    main()
