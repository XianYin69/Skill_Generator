"""flowchart_editor.py — 本地网页流程图编辑器（零依赖标准库）。
用法：python flowchart_editor.py --out <目标skill的tmp目录> [--port 8765]
启动后浏览器打开；导出 JSON 写入 --out/flowchart.json，格式与 flowchart/*.json 一致。
"""
import os, sys, json, argparse, threading, webbrowser, socketserver, http.server
_DIR = os.path.dirname(os.path.abspath(__file__))
_HTML = os.path.join(_DIR, "flowchart_editor.html")
class _H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers()
        with open(_HTML, "rb") as f: self.wfile.write(f.read())
    def do_POST(self):
        if self.path == "/save":
            ln = int(self.headers.get("Content-Length", 0)); data = json.loads(self.rfile.read(ln))
            fp = os.path.join(_OUT, "flowchart.json")
            with open(fp, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=2)
            self.send_response(200); self.send_header("Content-Type", "text/plain"); self.end_headers()
            self.wfile.write(f"已保存到 {fp}".encode())
        else: self.send_error(404)
class _S(socketserver.ThreadingMixIn, http.server.HTTPServer): pass
def _run(port):
    s = _S(("127.0.0.1", port), _H); print(f"[流程图编辑器] http://127.0.0.1:{port}/"); s.serve_forever()
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="目标 skill 的 tmp 目录")
    ap.add_argument("--port", type=int, default=8765)
    a = ap.parse_args(); _OUT = os.path.abspath(a.out); os.makedirs(_OUT, exist_ok=True)
    t = threading.Thread(target=_run, args=(a.port,), daemon=True); t.start()
    webbrowser.open(f"http://127.0.0.1:{a.port}/"); t.join()
