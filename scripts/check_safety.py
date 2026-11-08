"""Kid-safety scan for built tools: no outside servers, no tracking, no code from strings.

Runs on its own (python scripts/check_safety.py, also on every pull request via .github/workflows/safety.yml)
and inside scripts/check_tools.py. Pure standard library, so it needs no setup.

A tool may use a risky browser API only when its notes.md has a line starting "Safety:" that says why
(for example a bundled library that contains fetch code the tool never calls). Every such line is read
by Cory at review, so a contributor cannot quietly opt out.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Loading anything from another server, in markup or CSS.
OUTSIDE = [
    (r'<(?:script|img|iframe|audio|video|source|embed|track|object)\b[^>]*\s(?:src|data)\s*=\s*["\']?(?:https?:)?//', 'loads a file from another server'),
    (r'<link\b[^>]*\shref\s*=\s*["\']?(?:https?:)?//', 'external <link>'),
    (r'@import\s+(?:url\()?["\']?(?:https?:)?//', 'external @import'),
    (r'url\(\s*["\']?(?:https?:)?//', 'external url()'),
    (r'<form\b[^>]*\saction\s*=\s*["\']?(?:https?:)?//', 'form that posts to another server'),
    (r'<meta\b[^>]*http-equiv\s*=\s*["\']?refresh', 'meta refresh (redirect)'),
    (r'\bimport\s*\(?\s*["\'`](?:https?:)?//', 'imports code from another server'),
    (r'importScripts\s*\(', 'importScripts'),
]

# Talking to a server, tracking, or running code built from strings. Allowed only with a "Safety:" note.
RISKY = [
    (r'\bfetch\s*\(', 'fetch()'),
    (r'\bXMLHttpRequest\b', 'XMLHttpRequest'),
    (r'\bnew\s+WebSocket\b', 'WebSocket'),
    (r'\bnew\s+EventSource\b', 'EventSource'),
    (r'\bsendBeacon\b', 'navigator.sendBeacon'),
    (r'\bRTCPeerConnection\b', 'WebRTC connection'),
    (r'\bdocument\.cookie\b', 'cookies'),
    (r'(?<![\w.])eval\s*\(', 'eval()'),
    (r'(?-i:\bnew\s+Function\s*\()', 'new Function()'),  # capital F only: "new function(){}" is ordinary JS
    (r'\bnavigator\.geolocation\b', 'location'),
    (r'(?:googletagmanager|google-analytics|(?-i:\bgtag\s*\(|\bfbq\s*\()|hotjar|mixpanel|segment\.com|clarity\.ms|doubleclick)', 'analytics or ad tracker'),
]

# Fine for a kids' tool when it stays on the device; printed so a reviewer sees it.
NOTICE = [
    (r'\bgetUserMedia\b', 'uses the camera or microphone'),
]


def safety_note(folder):
    notes = folder / 'notes.md'
    return bool(notes.exists() and re.search(r'^Safety:', notes.read_text(encoding='utf-8'), re.M))


def scan(text, folder):
    """Return (problems, notices) for one built tool's HTML."""
    problems, notices = [], []
    for rx, label in OUTSIDE:
        for m in re.finditer(rx, text, re.I):
            problems.append(f'{label}: {text[m.start():m.start() + 90]!r}')
    if not safety_note(folder):
        for rx, label in RISKY:
            m = re.search(rx, text, re.I)
            if m:
                problems.append(f'{label} with no "Safety:" line in notes.md saying why: {text[m.start():m.start() + 70]!r}')
    for rx, label in NOTICE:
        if re.search(rx, text, re.I):
            notices.append(label)
    return problems, notices


def main():
    bad = 0
    for folder in sorted(p for p in (ROOT / 'tools').iterdir() if p.is_dir()):
        html = folder / f'{folder.name}.html'
        if not html.exists():
            continue
        problems, notices = scan(html.read_text(encoding='utf-8', errors='replace'), folder)
        for n in notices:
            print(f'note  {folder.name}: {n}')
        if problems:
            bad += 1
            print(f'FAIL  {folder.name}')
            for p in problems:
                print('      ', p)
    print(f'{bad} tool(s) failed the safety scan' if bad else 'safety scan: all tools clean')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
