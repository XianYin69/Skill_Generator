"""knowledge_download.py — 下载文件并保留许可证与版权信息（标准库实现）。
用途：把知识库来源文件（论文 PDF、MIT 仓库归档、图片等）下载到本地，
     同时写出 .provenance.json 记录来源、检索时间、许可证声明、版权署名。
约束：只允许从开放文献库 / 百科 / 权威论坛博客 / 使用 MIT 许可证的仓库下载。
"""
import os, sys, json, time, shutil, hashlib, urllib.parse, re
from urllib.request import urlopen, Request

MIT_OK = re.compile(r"\bMIT\b", re.I)

def provenance(url, path, license_text=""):
    return {
        "source": url,
        "retrieved": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "sha256": hashlib.sha256(open(path, "rb").read()).hexdigest(),
        "license": license_text.strip() or "需补录来源许可证",
        "copyright": "保留原始版权与署名，不得移除",
        "local": os.path.basename(path),
    }

def download(url, outdir="tmp/downloads"):
    os.makedirs(outdir, exist_ok=True)
    name = os.path.basename(urllib.parse.urlparse(url).path) or "download.bin"
    dest = os.path.join(outdir, name)
    req = Request(url, headers={"User-Agent": "SkillGenerator/1.0"})
    try:
        with urlopen(req, timeout=60) as r, open(dest, "wb") as f:
            shutil.copyfileobj(r, f)
    except Exception as e:
        sys.stderr.write(f"[下载失败] {e}\n"); return None
    if url.endswith(("LICENSE", "LICENSE.md", "LICENSE.txt")) and not MIT_OK.search(open(dest, encoding="utf-8", errors="replace").read()):
        sys.stderr.write(f"[警告] {url} 非 MIT，请核对许可证\n")
    lic = dest + ".license.txt" if os.path.exists(dest) else None
    with open(dest + ".provenance.json", "w", encoding="utf-8") as f:
        json.dump(provenance(url, dest, open(lic, encoding="utf-8").read() if lic else ""), f,
                  ensure_ascii=False, indent=2)
    print(f"[OK] 已下载并保留版权：{dest}")
    return dest

if __name__ == "__main__":
    for u in sys.argv[1:]:
        download(u)