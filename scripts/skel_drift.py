"""Report-only drift check for the <!-- skel --> blocks in written plans (consolidation step 4.E).

    python -X utf8 scripts/skel_drift.py [<course> ...] [--out FILE]

A written unit plan (docs/courses/<course>/sNN.md) or section plan (uNN-S.md) carries copies of data between
<!-- skel --> and <!-- /skel --> markers. Those blocks feed every new skeleton below them, so a stale block spreads.
This re-renders the plan's skeleton from today's data (unit_skeleton.build or section_skeleton.build, in memory, no
file written) and compares the blocks in order. It changes nothing; Cory picks the fix from the count. Prints one line
per drifted plan and a summary; --out also writes a CSV (plan, blocks, drifted, first drifted block's first line).
"""
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unit_skeleton as u          # noqa: E402
import section_skeleton as sk      # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs' / 'courses'
BLOCK = re.compile(r'<!-- skel -->\n?(.*?)<!-- /skel -->', re.S)


def blocks(text):
    return [b.strip() for b in BLOCK.findall(text.replace('\r\n', '\n'))]


def fresh(course, name):
    m = re.fullmatch(r's(\d+)\.md', name)
    if m:
        subj = u.subject_of(course)
        u.set_subject(subj)
        return u.build(course, int(m.group(1)))
    m = re.fullmatch(r'u(\d+)-(\d+)\.md', name)
    return sk.build(course, '%d.%s' % (int(m.group(1)), m.group(2)))


def main(a):
    out = None
    if '--out' in a:
        i = a.index('--out')
        out, a = a[i + 1], a[:i] + a[i + 2:]
    cs = a or sorted(p.name for p in DOCS.iterdir() if p.is_dir())
    rows, counts = [], {'plans': 0, 'drifted': 0, 'errors': 0, 'blocks': 0, 'blocks_drifted': 0}
    for c in cs:
        for p in sorted((DOCS / c).glob('*.md')):
            if not re.fullmatch(r's\d+\.md|u\d+-\d+\.md', p.name):
                continue
            have = blocks(p.read_text(encoding='utf-8'))
            if not have:
                continue
            counts['plans'] += 1
            try:
                want = blocks(fresh(c, p.name))
            except Exception as e:                                   # report, never stop the census
                counts['errors'] += 1
                rows.append([str(p.relative_to(ROOT)).replace('\\', '/'), len(have), 'error', str(e)[:160]])
                print('ERROR %s: %s' % (p.relative_to(ROOT).as_posix(), str(e)[:160]))
                continue
            n = max(len(have), len(want))
            bad = [i for i in range(n) if (have[i] if i < len(have) else None) != (want[i] if i < len(want) else None)]
            counts['blocks'] += len(have)
            counts['blocks_drifted'] += len(bad)
            if bad:
                counts['drifted'] += 1
                i = bad[0]
                h = (have[i] if i < len(have) else '(missing)').splitlines() or ['']
                w = (want[i] if i < len(want) else '(missing)').splitlines() or ['']
                diff = next((x for x, y in zip(h + ['(end)'] * len(w), w + ['(end)'] * len(h)) if x != y), h[0])
                note = '%d of %d blocks; block %d count %d, fresh %d; first differing line: %s' % (
                    len(bad), n, i + 1, len(have), len(want), diff[:120])
                rows.append([str(p.relative_to(ROOT)).replace('\\', '/'), len(have), len(bad), note])
                print('DRIFT %s: %s' % (p.relative_to(ROOT).as_posix(), note))
    print('skel drift: %(plans)d plans with skel blocks, %(drifted)d drifted, %(errors)d could not be rendered; '
          '%(blocks_drifted)d of %(blocks)d blocks differ' % counts)
    if out:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        with open(out, 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f, lineterminator='\n')
            w.writerow(['plan', 'blocks', 'drifted', 'note'])
            w.writerows(rows)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
