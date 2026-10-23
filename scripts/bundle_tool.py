"""Bundle tools that have a src.html: inline every `art:<name>` reference as a data URI.

    python scripts/bundle_tool.py [tool-id ...]     (no ids = every tool with a src.html)

Write and edit tools/<id>/src.html; tools/<id>/<id>.html is generated and stays one offline file.
"""
import base64, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def bundle(folder):
    src = folder / 'src.html'
    if not src.exists():
        return None
    html = src.read_text(encoding='utf-8')

    def data_uri(m):
        f = folder / 'art' / f'{m.group(1)}.webp'
        if not f.exists():
            raise FileNotFoundError(f'{folder.name}: missing art/{f.name} (run scripts/art.py {folder.name})')
        return 'data:image/webp;base64,' + base64.b64encode(f.read_bytes()).decode()

    out = re.sub(r'art:([a-z0-9-]+)', data_uri, html)
    # data files: the token "json:<name>" becomes the contents of tools/<id>/<name>.json
    out = re.sub(r'"json:([a-z0-9-]+)"', lambda m: (folder / f'{m.group(1)}.json').read_text(encoding='utf-8').strip(), out)
    if '"voice:*"' in out:  # recorded speech from scripts/voice.py, keyed by the exact line text
        import json
        sys.path.insert(0, str(ROOT / 'scripts'))
        from voice import clip_name
        lines = json.loads((folder / 'voice' / 'lines.json').read_text(encoding='utf-8'))['lines']
        clips = {}
        for text in lines:
            f = folder / 'voice' / clip_name(text)
            if not f.exists():  # not recorded yet: the tool falls back to the browser's voice for this line
                print(f'  {folder.name}: no recording yet for "{text[:40]}" (run scripts/voice.py {folder.name})')
                continue
            clips[text] = 'data:audio/mpeg;base64,' + base64.b64encode(f.read_bytes()).decode()
        out = out.replace('"voice:*"', json.dumps(clips, ensure_ascii=False))
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
