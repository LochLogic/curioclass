"""Check every built tool against docs/TOOL-CONTRACT.md. Exit 1 on any must-rule failure."""
import json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bundle_tool import bundle_all  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 2 * 1024 * 1024
NOTES_SECTIONS = ['## What it teaches', '## Key skills', '## Support at home']
BACKFILL = set((ROOT / 'docs/agents/notes-backfill.txt').read_text(encoding='utf-8').split())
REQUIRED_JSON = ['id', 'status', 'hook', 'outcome', 'driver', 'minutes', 'modes', 'grades_label', 'sources', 'third_party', 'updated']
NETWORK = [
    (r'<(?:script|img|iframe|audio|video|source|embed)\b[^>]*\ssrc\s*=\s*["\']?(?:https?:)?//', 'external src'),
    (r'<link\b[^>]*\shref\s*=\s*["\']?(?:https?:)?//', 'external <link>'),
    (r'@import\s+(?:url\()?["\']?(?:https?:)?//', 'external @import'),
    (r'url\(\s*["\']?(?:https?:)?//', 'external url()'),
]


def notes_sections(folder):
    """New tools must carry the three family-and-teacher sections; older ones wait in BACKFILL (docs/ROADMAP.md)."""
    if folder.name in BACKFILL:
        return []
    notes = folder / 'notes.md'
    text = notes.read_text(encoding='utf-8') if notes.exists() else ''
    return [f'notes.md missing "{h}"' for h in NOTES_SECTIONS if not re.search(rf'^{h}\s*$', text, re.M)]


def check(folder):
    tid = folder.name
    problems = []
    html = folder / f'{tid}.html'
    meta = folder / 'tool.json'
    if not html.exists():
        return [f'missing {tid}.html']
    if not meta.exists():
        problems.append('missing tool.json')
    else:
        data = json.loads(meta.read_text(encoding='utf-8'))
        problems += [f'tool.json missing "{k}"' for k in REQUIRED_JSON if k not in data]
        if data.get('id') != tid:
            problems.append(f'tool.json id {data.get("id")!r} does not match folder')
        if data.get('status') not in ('beta', 'ready'):
            problems.append('status must be beta or ready')
        if data.get('driver') not in ('teacher', 'students', 'students or teacher'):
            problems.append('driver must be teacher, students, or "students or teacher"')
    text = html.read_text(encoding='utf-8', errors='replace')
    if html.stat().st_size > MAX_BYTES:
        problems.append(f'{html.stat().st_size / 1e6:.1f} MB is over the 2 MB limit')
    for rx, label in NETWORK:
        for m in re.finditer(rx, text, re.I):
            problems.append(f'{label}: {text[m.start():m.start() + 90]!r}')
    for rx, label in [(r'<html[^>]*\slang=', '<html lang>'), (r'<meta[^>]*charset', 'meta charset'),
                      (r'<meta[^>]*name=["\']viewport', 'meta viewport'), (r'<title>[^<]+</title>', '<title>'),
                      (r'<meta[^>]*name=["\']description', 'meta description')]:
        if not re.search(rx, text, re.I):
            problems.append(f'missing {label}')
    problems += syntax(text)
    return problems


NODE = shutil.which('node')


def syntax(text):
    """Each inline script must parse: a stray comment once cut off half a line and the tool never loaded (2026-10-27)."""
    if not NODE:
        return []
    out = []
    for i, m in enumerate(re.finditer(r'<script\b([^>]*)>(.*?)</script>', text, re.S | re.I)):
        attrs, code = m.group(1), m.group(2)
        kind = re.search(r'''type\s*=\s*["']?([^"'\s>]+)''', attrs, re.I)
        kind = kind.group(1).lower() if kind else ''
        if 'src=' in attrs.lower() or kind not in ('', 'text/javascript', 'module') or not code.strip():
            continue
        with tempfile.NamedTemporaryFile('w', suffix='.mjs' if kind == 'module' else '.js', delete=False, encoding='utf-8') as f:
            f.write(code)
        r = subprocess.run([NODE, '--check', f.name], capture_output=True, text=True)
        Path(f.name).unlink()
        if r.returncode:
            err = next((l for l in r.stderr.splitlines() if 'Error' in l), r.stderr.strip()[:120])
            out.append(f'script {i + 1} does not parse: {err}')
    return out


bundle_all()
bad = 0
for folder in sorted(p for p in (ROOT / 'tools').iterdir() if p.is_dir()):
    if (folder / 'tool.draft.json').exists():  # waiting for art: not on the site yet
        problems = notes_sections(folder)
        print(f'{"FAIL" if problems else "draft"} {folder.name}')
        for p in problems:
            print('     ', p)
        bad += bool(problems)
        continue
    if not (folder / 'tool.json').exists() and (folder / 'spec.md').exists():  # specced, not built yet
        print(f'spec  {folder.name}')
        continue
    problems = check(folder) + (notes_sections(folder) if (folder / 'tool.json').exists() else [])
    print(f'{"FAIL" if problems else "ok  "} {folder.name}')
    for p in problems:
        print('     ', p)
    bad += bool(problems)
sys.exit(1 if bad else 0)
