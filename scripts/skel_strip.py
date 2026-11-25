"""Take the stored fact blocks out of every written plan (consolidation 4.E2 step 5).

    python -X utf8 scripts/skel_strip.py [--apply] [--moves FILE]
    python -X utf8 scripts/skel_strip.py --guard

Each `<!-- skel -->` ... `<!-- /skel -->` block in a written plan (docs/courses/<course>/sNN.md, uNN-N.md) is removed.
A line inside a block that the signed hand list marks `move` (FILE, default
docs/reviews/consolidation/step4-E2/hand-list.csv, column `final`) stays where it was, as plan prose. Nothing else in
the file changes. The facts render from data (scripts/plan_facts.py).

Without --apply nothing is written: the count of blocks, lines removed and lines kept is printed. With --apply each
file is written and then proved: its new text equals its old text with the block spans removed except the kept lines,
and its merged view (plan_facts.merged) holds every kept line. Line endings are kept.

--guard (a consolidation gate) exits 1 if any written plan holds a stored block marker again: plans keep judgment
prose only, and facts are never stored in them.
"""
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import plan_facts as pf   # noqa: E402

ROOT = pf.ROOT
DOCS = pf.DOCS
BLOCK = re.compile(r'([ \t]*<!-- skel -->[ \t]*\n?)(.*?)([ \t]*<!-- /skel -->[ \t]*(?:\n|\Z))', re.S)


def norm(s):
    return ' '.join(s.split())


def moves(path):
    keep = {}
    with open(path, encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            if r.get('final') == 'move':
                keep.setdefault(r['plan'], set()).add(r['line'])
    return keep


def strip_keep(text, keep):
    """(new text, blocks, lines removed, lines kept)."""
    nb = gone = kept = 0
    out, last = [], 0
    for m in BLOCK.finditer(text):
        nb += 1
        out.append(text[last:m.start()])
        for ln in m.group(2).splitlines(True):
            if ln.strip() and norm(ln) in keep:
                out.append(ln if ln.endswith('\n') else ln + '\n')
                kept += 1
            elif ln.strip():
                gone += 1
        last = m.end()
    out.append(text[last:])
    return ''.join(out), nb, gone, kept


def guard():
    bad = [p for p in sorted(DOCS.glob('*/*.md')) if pf.PLAN.fullmatch(p.name)
           and '<!-- skel' in p.read_text(encoding='utf-8')]
    for p in bad:
        print('FAIL %s: holds a stored <!-- skel --> block; facts render from data, never stored in a plan'
              % p.relative_to(ROOT).as_posix())
    print('skel guard: %d plan(s) with stored blocks' % len(bad))
    return 1 if bad else 0


def main(a):
    if a == ['--guard']:
        return guard()
    apply_ = '--apply' in a
    mf = ROOT / 'docs' / 'reviews' / 'consolidation' / 'step4-E2' / 'hand-list.csv'
    if '--moves' in a:
        mf = Path(a[a.index('--moves') + 1])
    keep = moves(mf)
    files = sorted(p for p in DOCS.glob('*/*.md') if pf.PLAN.fullmatch(p.name))
    tot = [0, 0, 0, 0]
    bad = []
    for p in files:
        raw = p.read_bytes().decode('utf-8')
        crlf = '\r\n' in raw
        text = raw.replace('\r\n', '\n')
        if '<!-- skel -->' not in text:
            continue
        rel = p.relative_to(ROOT).as_posix()
        k = keep.get(rel, set())
        new, nb, gone, kept = strip_keep(text, k)
        tot[0] += 1
        tot[1] += nb
        tot[2] += gone
        tot[3] += kept
        missing = k - {norm(x) for x in new.splitlines()}
        if missing:
            bad.append('%s: %d marked move line(s) not found in a block: %s' % (rel, len(missing), sorted(missing)[0][:80]))
        if '<!-- skel' in new or '<!-- /skel' in new:
            bad.append('%s: a marker is left (unbalanced block)' % rel)
        if apply_ and not bad:
            out = new.replace('\n', '\r\n') if crlf else new
            p.write_bytes(out.encode('utf-8'))
            # proof: the same as the old text with the spans removed, kept lines in place
            again, _, _, _ = strip_keep(text, k)
            if p.read_bytes().decode('utf-8').replace('\r\n', '\n') != again:
                bad.append('%s: written text differs from the planned strip' % rel)
    print('%s: %d plans, %d blocks, %d block lines removed, %d kept as prose' % (
        'stripped' if apply_ else 'would strip', *tot))
    for b in bad:
        print(b)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
