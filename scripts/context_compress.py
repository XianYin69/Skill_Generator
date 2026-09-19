"""context_compress.py — 上下文压缩机制（标准库）。
用途：把长文本压缩为要点提纲，控制送入模型的上下文长度。规则见 resistance/上下文压缩机制.md。
策略：按句切分→保留含关键词/数字句→截断为不超过 ratio 的摘要，原文哈希留档可回溯。
"""
import re, sys, hashlib, argparse

STOP = re.compile(r"[。！？；;.\n]")

def compress(text, ratio=0.3, keywords=()):
    sents = [s.strip() for s in STOP.split(text) if len(s.strip()) > 4]
    if not sents:
        return text
    def score(s):
        return sum(1 for k in keywords if k in s) * 2 + (1 if re.search(r"\d", s) else 0)
    keep = max(1, int(len(sents) * ratio))
    top = sorted(sents, key=score, reverse=True)[:keep]
    out = "\n".join(sorted(top, key=sents.index))
    print(f"# 原文{len(text)}字→摘要{len(out)}字 原档hash={hashlib.sha1(text.encode()).hexdigest()[:10]}")
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--ratio", type=float, default=0.3)
    ap.add_argument("--kw", default="")
    a = ap.parse_args()
    data = sys.stdin.read() if len(sys.argv) < 2 else open(sys.argv[1], encoding="utf-8").read()
    sys.stdout.write(compress(data, a.ratio, tuple(k for k in a.kw.split(",") if k)))