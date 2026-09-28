"""add-mit-license.py — 初始化写入 MIT 协议 LICENSE（工作区根＋tmp 镜像）；默认预览，`--yes` 才写盘；已有 LICENSE 不覆盖，替换须 `--replace --yes` 并经用户确认。"""
import argparse, datetime, json, os

MIT = """MIT License

Copyright (c) {year} {holder}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def spots(t):
    tmp = os.path.join(t, "tmp")
    return [os.path.join(t, "LICENSE")] + ([os.path.join(tmp, "LICENSE")] if os.path.isdir(tmp) else [])

def run(target, holder, year, replace, yes):
    out = []
    for p in spots(target):
        if os.path.exists(p) and not replace:
            out.append({"path": p, "action": "skip", "why": "已有 LICENSE"})
        elif not yes:
            out.append({"path": p, "action": "preview", "hint": "--yes 写入"})
        else:
            open(p, "w", encoding="utf-8").write(MIT.format(year=year, holder=holder))
            out.append({"path": p, "action": "written"})
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="加入 MIT 协议 LICENSE")
    ap.add_argument("--target", required=True); ap.add_argument("--holder")
    ap.add_argument("--year", default=str(datetime.date.today().year))
    ap.add_argument("--replace", action="store_true"); ap.add_argument("--yes", action="store_true")
    a = ap.parse_args()
    h = a.holder or (os.path.basename(os.path.normpath(a.target)) + " authors")
    print(json.dumps({"holder": h, "items": run(a.target, h, a.year, a.replace, a.yes)}, ensure_ascii=False))
