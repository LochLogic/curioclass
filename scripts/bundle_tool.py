"""Bundle tools that have a src.html: inline every `art:<name>` reference as a data URI (and json:, voice:, lib: tokens).

    python scripts/bundle_tool.py [tool-id ...]     (no ids = every tool with a src.html)

CURIO_DRAFT=1 stands in a labeled circle for art that isn't painted yet (never deploy a draft build).
A tool still waiting for art keeps tool.draft.json instead of tool.json (rename it when the art is in): the site
leaves it on the bench, check_tools skips it, and it is bundled only with CURIO_DRAFT set.

Write and edit tools/<id>/src.html; tools/<id>/<id>.html is generated and stays one offline file.
"""
import base64, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def bundle(folder):
    src = folder / 'src.html'
    if not src.exists():
        return None
    if (folder / 'tool.draft.json').exists() and not os.environ.get('CURIO_DRAFT'):
        return None
    html = src.read_text(encoding='utf-8')

    def data_uri(m):
        f = folder / 'art' / f'{m.group(1)}.webp'
        if not f.exists() and os.environ.get('CURIO_DRAFT'):  # draft build: a labeled stand-in until the art is painted
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400"><circle cx="200" cy="200" r="190" fill="#9aa7b4" '
                   f'stroke="#fff" stroke-width="6" stroke-dasharray="18 12"/><text x="200" y="215" font-size="46" text-anchor="middle" '
                   f'font-family="sans-serif" fill="#fff">{m.group(1)}</text></svg>')
            return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()
        if not f.exists():
            raise FileNotFoundError(f'{folder.name}: missing art/{f.name} (run scripts/art.py {folder.name})')
        return 'data:image/webp;base64,' + base64.b64encode(f.read_bytes()).decode()

    out = re.sub(r'(?<![\w-])art:([a-z0-9-]+)', data_uri, html)  # a whole token, so a CSS .part:hover is left alone
    # data files: the token "json:<name>" becomes the contents of tools/<id>/<name>.json
    out = re.sub(r'"json:([a-z0-9-]+)"', lambda m: (folder / f'{m.group(1)}.json').read_text(encoding='utf-8').strip(), out)
    if '"voice:*"' in out:  # recorded speech from scripts/voice.py, keyed by the exact line text
        import json
        sys.path.insert(0, str(ROOT / 'scripts'))
        from voice import clip_name
        spec = json.loads((folder / 'voice' / 'lines.json').read_text(encoding='utf-8'))
        lines = [*spec['lines'], *(t for g in spec.get('groups', []) for t in g)]
        clips = {}
        for text in lines:
            f = folder / 'voice' / clip_name(text)
            if not f.exists():  # not recorded yet: the tool falls back to the browser's voice for this line
                print(f'  {folder.name}: no recording yet for "{text[:40]}" (run scripts/voice.py {folder.name})')
                continue
            clips[text] = 'data:audio/mpeg;base64,' + base64.b64encode(f.read_bytes()).decode()
        out = out.replace('"voice:*"', json.dumps(clips, ensure_ascii=False))
    # libraries last, so their code is never scanned for the tokens above: <script src="lib:three"></script> inlines lib/three.min.js
    out = re.sub(r'<script src="lib:([a-z0-9.-]+)"></script>', lambda m: '<script>' + (folder / 'lib' / f'{m.group(1)}.min.js').read_text(encoding='utf-8').strip() + '</script>', out)
    # the shared kit (kit/<name>.js and .css, docs/KIT.md): <script src="kit:curio"></script>, <link rel="stylesheet" href="kit:curio">
    out = re.sub(r'<script src="kit:([a-z0-9-]+)"></script>', lambda m: '<script>\n' + (ROOT / 'kit' / f'{m.group(1)}.js').read_text(encoding='utf-8').strip() + '\n</script>', out)
    out = re.sub(r'<link rel="stylesheet" href="kit:([a-z0-9-]+)">', lambda m: '<style>\n' + (ROOT / 'kit' / f'{m.group(1)}.css').read_text(encoding='utf-8').strip() + '\n</style>', out)
    out = out.replace('<!--', '<!-- GENERATED from src.html by scripts/bundle_tool.py; edit src.html, not this file.\n', 1)
    (folder / f'{folder.name}.html').write_text(out, encoding='utf-8')
    return len(out)


def bundle_all(ids=None):
    for folder in sorted(p for p in (ROOT / 'tools').iterdir() if p.is_dir()):
        if ids and folder.name not in ids:
            continue
        size = bundle(folder)
        if size:
            print(f'bundled {folder.name}: {size // 1024} KB')


if __name__ == '__main__':
    bundle_all(sys.argv[1:])
