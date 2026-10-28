"""Apply the idea pass: proposed concept lines, formats and families from tools/<id>/idea.md go into data/concepts/*.txt.

    python scripts/apply_ideas.py [--write]

Reads each idea card's "Proposed concept line" (anything but "keep"), "Fit: change to <format>" and "change family to
none", finds the tool's line in data/concepts/*.txt by its title slug, and prints the changes; --write saves them.
Titles are not touched here: run scripts/rename_tools.py with the list this prints, then check_concepts.py --write and
build_db.py.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from rename_tools import slug


def field(text, name):
    m = re.search(rf'^- {name}:\s*(.+)$', text, re.M)
    return m.group(1).strip() if m else ''


def main():
    cards = {p.parent.name: p.read_text(encoding='utf-8') for p in ROOT.glob('tools/*/idea.md')}
    renames, changed = [], 0
    for f in sorted((ROOT / 'data' / 'concepts').glob('*.txt')):
        out = []
        for line in f.read_text(encoding='utf-8').splitlines():
            parts = line.split('|')
            if line.startswith('#') or len(parts) != 5 or slug(parts[1]) not in cards:
                out.append(line)
                continue
            tid, card = slug(parts[1]), cards[slug(parts[1])]
            concept = field(card, 'Proposed concept line')
            if concept and not concept.lower().startswith('keep'):
                parts[4] = concept.replace('|', '/')
            fit = field(card, r'Format / family')
            m = re.search(r'Fit: change to (\w+)', fit)
            if m:
                parts[2] = m.group(1)
            if 'change family to none' in fit:
                parts[3] = ''
            title = field(card, 'Proposed title')
            if title and not title.lower().startswith('keep'):
                renames.append((tid, re.sub(r'\s*\(.*$', '', title).strip().strip('"')))
            new = '|'.join(parts)
            if new != line:
                changed += 1
            out.append(new)
        if '--write' in sys.argv:
            f.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(f'{len(cards)} cards, {changed} concept lines changed' + ('' if '--write' in sys.argv else ' (dry run)'))
    print('Renames:\n' + '\n'.join(f'  {a}="{b}"' for a, b in renames))


if __name__ == '__main__':
    main()
