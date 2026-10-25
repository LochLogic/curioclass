"""Check every built tool against docs/TOOL-CONTRACT.md. Exit 1 on any must-rule failure."""
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bundle_tool import bundle_all  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 2 * 1024 * 1024
REQUIRED_JSON = ['id', 'status', 'hook', 'outcome', 'driver', 'minutes', 'modes', 'grades_label', 'sources', 'third_party', 'updated']
NETWORK = [
    (r'<(?:script|img|iframe|audio|video|source|embed)\b[^>]*\ssrc\s*=\s*["\']?(?:https?:)?//', 'external src'),
    (r'<link\b[^>]*\shref\s*=\s*["\']?(?:https?:)?//', 'external <link>'),
    (r'@import\s+(?:url\()?["\']?(?:https?:)?//', 'external @import'),
    (r'url\(\s*["\']?(?:https?:)?//', 'external url()'),
]


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
    return problems


bundle_all()
bad = 0
for folder in sorted(p for p in (ROOT / 'tools').iterdir() if p.is_dir()):
    if (folder / 'tool.draft.json').exists():  # waiting for art: not on the site yet
        print(f'draft {folder.name}')
        continue
    problems = check(folder)
    print(f'{"FAIL" if problems else "ok  "} {folder.name}')
    for p in problems:
        print('     ', p)
    bad += bool(problems)
sys.exit(1 if bad else 0)
