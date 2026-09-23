"""knowledge_browser.py — 抓取开放网页文献（标准库实现，无第三方依赖，天然满足 MIT 约束）。
用途：知识库构建时抓取「开放文献数据库 / 百科 / 权威论坛·博客 / MIT 仓库」页面，
     记录来源与版权信息，保留原始 HTML 供解析器转换。
输出：tmp/downloads/<id>.html + <id>.provenance.json（含 source/license/copyright）。
"""
import json, os, sys, time, hashlib, re
from urllib.request import Request, urlopen
from urllib.error import URLError
if os.path.exists("SKILL.md"): raise SystemExit("拒绝：tmp 缓存不得写入 skill 目录（cwd 位于 skill 内）")

ALLOWED_HOST = re.compile(
    r"(wikipedia\.org|arxiv\.org|pubmed|doi\.org|"
    r"stackoverflow\.com|github\.com|gitlab\.com|[^/]*\.org)$")

def fetch(url, outdir="tmp/downloads"):
    if not ALLOWED_HOST.search(url):
        sys.stderr.write(f"[拒绝] 非白名单来源：{url}\n")
        return None
    os.makedirs(outdir, exist_ok=True)
    req = Request(url, headers={"User-Agent": "SkillGenerator/1.0"})
    try:
        with urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
    except URLError as e:
        sys.stderr.write(f"[抓取失败] {e}\n"); return None
    rid = hashlib.sha1(url.encode()).hexdigest()[:12]
    open(os.path.join(outdir, f"{rid}.html"), "w", encoding="utf-8").write(html)
    title = re.search(r"<title>(.*?)</title>", html, re.S)
    prov = {
        "id": rid, "source": url, "retrieved": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "title": re.sub(r"\s+", " ", title.group(1)).strip() if title else "",
        "license": "需人工确认页面/仓库声明的许可证", "copyright": "保留原文版权，禁止改写署名",
    }
    json.dump(prov, open(os.path.join(outdir, f"{rid}.provenance.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"[OK] {rid} <- {url}")
    return rid

if __name__ == "__main__":
    for u in sys.argv[1:]:
        fetch(u)