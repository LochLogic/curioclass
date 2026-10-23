"""Serve dist/ locally the way Cloudflare does: /tools/x/x also finds /tools/x/x.html, and 404s use 404.html.

python scripts/serve.py [port]   (default 8411)
"""
import http.server, sys
from functools import partial
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent / 'dist'


class Handler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = Path(self.translate_path(self.path))
        if not path.exists() and path.with_name(path.name + '.html').is_file():
            self.path = self.path.split('?')[0] + '.html'
        return super().send_head()

    def send_error(self, code, message=None, explain=None):
        page = DIST / '404.html'
        if code == 404 and page.exists():
            body = page.read_bytes()
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            super().send_error(code, message, explain)


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8411
http.server.ThreadingHTTPServer(('127.0.0.1', port), partial(Handler, directory=str(DIST))).serve_forever()
