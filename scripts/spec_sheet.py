"""One page per spec wave for the spec check: each spec's one idea, accent, voice, art and open questions.

    python scripts/spec_sheet.py docs/agents/BATCH-W1.md [out.md]

Reads the tool ids from the batch note's group tables, then flags what the spec check looks for across the wave:
the same bank voice or accent used twice in one group, and art names asked for by more than one tool.
"""
import re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sections(text):
    out, name = {}, None
    for line in text.splitlines():
        m = re.match(r'##\s+(.+)', line)
        if m and not line.startswith('###'):
            name = m.group(1).strip().lower()
            out[name] = []
        elif name:
            out[name].append(line)
    return {k: '\n'.join(v).strip() for k, v in out.items()}


def groups(note):
    gs, cur = [], None
    for line in note.read_text(encoding='utf-8').splitlines():
        m = re.match(r'###\s+(.+)', line)
        if m:
            cur = [m.group(1), []]
            gs.append(cur)
        m = re.match(r'\|\s*([a-z][a-z0-9-]*)\s*\|', line)
        if cur and m and m.group(1) not in ('id',):
            cur[1].append(m.group(1))
    return gs


def main():
    note = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    lines, art_by, flags = [], defaultdict(list), []
    for gname, ids in groups(note):
        lines.append(f'\n## {gname}\n')
        seen_voice, seen_accent = defaultdict(list), defaultdict(list)
        for tid in ids:
            p = ROOT / 'tools' / tid / 'spec.md'
            if not p.exists():
                lines.append(f'- **{tid}:** NO SPEC')
                flags.append(f'{tid}: no spec')
                continue
            text = p.read_text(encoding='utf-8')
            s = sections(text)
            title = re.search(r'^#\s+(.+)', text, re.M).group(1).strip()
            voice = re.search(r'\b([a-z]+-[a-z]+(?:-[a-z]+)?)\b', s.get('voice', '')) if s.get('voice', '').lower() != 'none' else None
            voice = voice.group(1) if voice else 'none'
            accent = re.search(r'#[0-9a-fA-F]{6}\b', s.get('look', ''))
            accent = accent.group(0).lower() if accent else '?'
            art = [m.group(1).strip().lower() for m in re.finditer(r'^\s*[-*]?\s*`?([a-z0-9][a-z0-9_-]+)`?\s*:', s.get('art', ''), re.M)]
            for a in art:
                art_by[a].append(tid)
            seen_voice[voice].append(tid)
            seen_accent[accent].append(tid)
            open_q = s.get('open questions', '')
            n = len(text.splitlines())
            lines.append(f'- **{tid}** ({title}, {n} lines; voice {voice}; accent {accent}; art {len(art)})')
            lines.append(f'  - One idea: {" ".join(s.get("one idea", "").split())}')
            if art:
                lines.append(f'  - Art: {", ".join(art)}')
            if open_q and open_q.lower() not in ('none', 'none.'):
                lines.append('  - Open: ' + ' '.join(open_q.split())[:600])
            if n > 300:
                flags.append(f'{tid}: {n} lines (over about 250)')
            if '—' in text:
                flags.append(f'{tid}: em dash')
        for v, t in seen_voice.items():
            if v != 'none' and len(t) > 1:
                flags.append(f'{gname}: voice {v} used by {", ".join(t)}')
        for a, t in seen_accent.items():
            if a != '?' and len(t) > 1:
                flags.append(f'{gname}: accent {a} used by {", ".join(t)}')
    generic = {'background', 'bg', 'none', 'icon', 'icons'}
    for a, t in art_by.items():
        if len(t) > 1 and a not in generic:
            flags.append(f'art "{a}" asked for by {", ".join(t)}')
    page = '# Spec sheet: ' + note.stem + '\n\n## Flags\n\n' + ('\n'.join(f'- {f}' for f in flags) or '- none') + '\n' + '\n'.join(lines) + '\n'
    if out:
        out.write_text(page, encoding='utf-8')
        print(f'wrote {out}: {len(flags)} flags')
    else:
        sys.stdout.reconfigure(encoding='utf-8')
        print(page)


if __name__ == '__main__':
    main()
