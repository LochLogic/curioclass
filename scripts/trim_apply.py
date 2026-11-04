r"""Apply the worksheet backlog trim (docs/agents/trim/<subject>.csv, approved by Cory 2026-11-04).

    python scripts/trim_apply.py      drop the cut rows from the concept lists in docs/worksheets/

Row numbers are ids: a built sheet's link is /closet/worksheets/sheet/#<unit>/<n>, and generated.csv and the built
files name rows by n, so nothing is renumbered and a unit's numbers may have gaps (the class page shows 1..N by
position). Only `open` rows are cut (scripts/trim_check.py checks that). A second run changes nothing.
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRIM = ROOT / 'docs' / 'agents' / 'trim'
LISTS = ROOT / 'docs' / 'worksheets'
ROW = re.compile(r'^\|\s*(\d+)\s*\|(.+)\|\s*$')
HEAD = re.compile(r'^## ([a-z0-9-]+): ')


def main():
    cuts = {}
    for f in sorted(TRIM.glob('*.csv')):
        for r in csv.DictReader(open(f, encoding='utf-8')):
            cuts.setdefault(r['unit'], {})[int(r['n'])] = r['title']
    removed = 0
    for f in sorted(LISTS.glob('*.md')):
        text = f.read_bytes().decode('utf-8')
        nl = '\r\n' if '\r\n' in text else '\n'
        out, unit = [], None
        for line in text.split(nl):
            h = HEAD.match(line)
            if h:
                unit = h.group(1)
            m = ROW.match(line)
            if m and unit and int(m.group(1)) in cuts.get(unit, {}):
                title = m.group(2).split('|')[0].strip()
                if cuts[unit][int(m.group(1))] != title:
                    sys.exit(f'{unit} #{m.group(1)}: cut list says {cuts[unit][int(m.group(1))]!r}, list has {title!r}')
                removed += 1
                continue
            out.append(line)
        f.write_bytes(nl.join(out).encode('utf-8'))
    print(f'{removed} rows removed')


if __name__ == '__main__':
    main()
