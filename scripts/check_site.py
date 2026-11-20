"""Check the built site in dist/: every internal link and redirect resolves, and no page loads anything from another host."""
import re, sys
from pathlib import Path

DIST = Path(__import__('os').environ.get('CURIO_DIST') or Path(__file__).resolve().parent.parent / 'dist')
broken, external, pages = {}, set(), 0


def resolves(url):
    target = DIST / url.lstrip('/')
    # Cloudflare serves x.html at x (html_handling: auto-trailing-slash)
    return target.is_file() or (target / 'index.html').is_file() or target.with_name(target.name + '.html').is_file()


for page in DIST.rglob('*.html'):
    if page.parent.name == page.stem:  # a tool file itself; check_tools.py covers those
        continue
    pages += 1
    html = page.read_text(encoding='utf-8')
    for m in re.finditer(r'<(?:script|img|iframe|link)\b[^>]*\s(?:src|href)="(https?:)?//[^"]+"', html):
        if 'rel="canonical"' not in m.group(0):
            external.add(m.group(0)[:120])
    for url in re.findall(r'(?:href|src)="(/[^"#?]*)', html):
        if not resolves(url):
            broken.setdefault(url, page.relative_to(DIST).as_posix())
# _redirects (from data/redirects.csv): every target must exist, and no old path may still be built as a page.
# A splat rule (/modules/* /topics/:splat) moves a whole folder: its target folder must be built and hold pages, and
# nothing may still be built under the old folder (a link to the old folder already shows up above as broken).
rfile = DIST / '_redirects'
redirects = [l.split() for l in rfile.read_text(encoding='utf-8').splitlines() if l.strip()] if rfile.exists() else []
splats = 0
for old, new, *_ in redirects:
    if old.endswith('/*'):
        splats += 1
        src, dst = DIST / old[:-1].strip('/'), DIST / new.split(':splat')[0].strip('/')
        if not new.endswith('/:splat'):
            broken.setdefault(new + ' (a splat target ends in /:splat)', '_redirects')
        elif not dst.is_dir() or not next(dst.rglob('index.html'), None):
            broken.setdefault(new, '_redirects')
        if src.exists() and any(f.is_file() for f in src.rglob('*')):
            broken.setdefault(old + ' (redirected, but still built)', '_redirects')
        continue
    if not resolves(new.split('#')[0]):
        broken.setdefault(new, '_redirects')
    if resolves(old):
        broken.setdefault(old + ' (redirected, but still built)', '_redirects')
# Hidden course pages (scripts/course_pages.py, SHOWN = False): while .assetsignore keeps courses/* out of the upload,
# no other page, the sitemap or the search index may point into /courses/.
ignore = DIST / '.assetsignore'
if ignore.exists() and 'courses/*' in ignore.read_text(encoding='utf-8').split():
    for page in DIST.rglob('*.html'):
        rel = page.relative_to(DIST).as_posix()
        if not rel.startswith('courses/') and page.parent.name != page.stem and 'href="/courses/' in page.read_text(encoding='utf-8'):
            broken.setdefault('/courses/ (hidden, but linked)', rel)
    for name in ('sitemap.xml', 'search-index.json'):
        if (DIST / name).exists() and '/courses/' in (DIST / name).read_text(encoding='utf-8'):
            broken.setdefault('/courses/ (hidden, but listed)', name)
# Count what a deploy uploads: files matched by .assetsignore stay on disk but never reach the host's 20000 cap.
import fnmatch  # noqa: E402
skip = [p for p in (ignore.read_text(encoding='utf-8').split() if ignore.exists() else []) if p]
files = [f for f in DIST.rglob('*') if f.is_file()
         and not any(fnmatch.fnmatchcase(f.relative_to(DIST).as_posix(), p) for p in skip)]
big = [f.relative_to(DIST).as_posix() for f in files if f.stat().st_size > 25 * 2 ** 20]  # Cloudflare's asset limits
print(f'{pages} pages checked, {len(redirects)} redirects ({splats} splat), {len(broken)} broken internal links, {len(external)} external loads, '
      f'{len(files)} files (limit 20000), {len(big)} over 25 MiB')
for f in big:
    print('  too big', f)
for url, where in list(broken.items())[:20]:
    print('  broken', url, 'on', where)
for e in external:
    print('  external', e)
sys.exit(1 if broken or external or big or len(files) > 20000 else 0)
