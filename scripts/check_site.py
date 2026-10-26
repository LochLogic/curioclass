"""Check the built site in dist/: every internal link resolves, and no page loads anything from another host."""
import re, sys
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent / 'dist'
broken, external, pages = {}, set(), 0
for page in DIST.rglob('*.html'):
    if page.parent.name == page.stem:  # a tool file itself; check_tools.py covers those
        continue
    pages += 1
    html = page.read_text(encoding='utf-8')
    for m in re.finditer(r'<(?:script|img|iframe|link)\b[^>]*\s(?:src|href)="(https?:)?//[^"]+"', html):
        if 'rel="canonical"' not in m.group(0):
            external.add(m.group(0)[:120])
    for url in re.findall(r'(?:href|src)="(/[^"#?]*)', html):
        target = DIST / url.lstrip('/')
        # Cloudflare serves x.html at x (html_handling: auto-trailing-slash)
        if not (target.is_file() or (target / 'index.html').is_file() or target.with_name(target.name + '.html').is_file()):
            broken.setdefault(url, page.relative_to(DIST).as_posix())
files = [f for f in DIST.rglob('*') if f.is_file()]
big = [f.relative_to(DIST).as_posix() for f in files if f.stat().st_size > 25 * 2 ** 20]  # Cloudflare's asset limits
print(f'{pages} pages checked, {len(broken)} broken internal links, {len(external)} external loads, '
      f'{len(files)} files (limit 20000), {len(big)} over 25 MiB')
for f in big:
    print('  too big', f)
for url, where in list(broken.items())[:20]:
    print('  broken', url, 'on', where)
for e in external:
    print('  external', e)
sys.exit(1 if broken or external or big or len(files) > 20000 else 0)
