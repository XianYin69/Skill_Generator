"""knowledge_convert.py — 二进制/文档 → markdown/json/svg 解析器。
MIT 依赖：pdfplumber、python-docx、markdownify（pip install 之）。
行为：转换→清洗元数据→保留来源 .provenance.json→输出目标 skill 适配条目。
"""
import os, sys, json, re, hashlib
MIT = ("pdfplumber", "python-docx", "markdownify")

def _try(mod):
    try: return __import__(mod)
    except Exception: return None

def to_markdown(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        if open(path, "rb").read(5) != b"%PDF-" or not (pl := _try("pdfplumber")):
            raise SystemExit("[pdf\u4e0d\u53ef\u7528]\u975ePDF/\u9b54\u6570\u7f3a\u5931/\u7f3a pdfplumber: " + path)
        with pl.open(path) as d:
            md = "\n".join((pg.extract_text() or "") for pg in d.pages)
        if not md.strip():
            raise SystemExit("[pdf\u626b\u63cf\u4ef6]\u65e0\u6587\u672c\u5c42\uff0c\u6539\u7528\u591a\u6a21\u6001\u8bfb\u53d6: " + path)
        return md
    if ext == ".docx":
        d = _try("docx")
        if d: return "\n".join(x.text for x in d.Document(path).paragraphs)
    if ext in (".html", ".htm"):
        m = _try("markdownify")
        if m: return m.markdownify(open(path, encoding="utf-8", errors="replace").read())
    return open(path, encoding="utf-8", errors="replace").read()

def clean_meta(text):
    text = re.sub(r"https?://\S*[?&](?:utm_[^&\s]+|fbclid|ref=\S+)", lambda m: m.group(0).split("?")[0], text)
    return re.sub(r"[ \t]+", " ", text).strip()

def to_item(path):
    md = clean_meta(to_markdown(path))
    pj = path + ".provenance.json"
    prov = json.load(open(pj, encoding="utf-8")) if os.path.exists(pj) else {}
    item = {"id": hashlib.sha1(md.encode()).hexdigest()[:10],
            "source": prov.get("source", os.path.basename(path)),
            "content_md": md, "license": prov.get("license", "未知"),
            "copyright": prov.get("copyright", "")}
    base = os.path.splitext(path)[0]
    open(base + ".knowledge.json", "w", encoding="utf-8").write(json.dumps(item, ensure_ascii=False, indent=2))
    open(base + ".knowledge.md", "w", encoding="utf-8").write(md)
    print(f"[OK] 转换+清洗+保留许可：{base}.knowledge.*")
    return item

if __name__ == "__main__":
    for p in sys.argv[1:]:
        to_item(p)