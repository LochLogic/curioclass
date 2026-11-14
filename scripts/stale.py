"""Stale-note catch (added 2026-11-13): notes that say a piece of work is not done yet go stale the moment it is.

    python -X utf8 scripts/stale.py check [file ...]

A note that waits on other work carries a marker the checker can test:

    Pending(<what>): <the note>

where <what> is one of
- a file path from the repository root: resolved once the file exists;
- path#text: resolved once that file contains the text (Pending(data/standards/x.txt#RST.11-12.8));
- a plan-flow node id (frame:science:5, prog-review:all): resolved once data/plans/flow-status.csv marks it done.

FAIL: a Pending marker whose work has landed (the note is stale: rewrite it to say what is now true and drop the
marker); a Pending marker naming no file, text or node the checker knows the form of; a work-status phrase
("not yet placed", "until it is added", "to come", "TBD", "placeholder" and the like) outside a Pending marker
(mark it so the checker can follow it, or reword it).
Teaching boundaries ("not yet describe", "not yet measured with a ruler") are about the student, not the work, and
are not flagged. With no files, checks the four progressions and the course frames (docs/courses/**/*.md,
data/frames/*.csv when they exist).
"""
import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARK = re.compile(r'Pending\(([^)]*)\)\s*:')
# Work-status wording: says something about our own unfinished work. Kept narrow so a student boundary
# ("not yet describe") never trips it.
WORK = re.compile(
    r"not yet (in the|placed|written|built|added|loaded|in a curio class|named by|decided|chosen)"
    r"|until (it|they|this|that|the [\w ,'-]{1,40}) (is|are) (added|written|built|loaded|placed|decided|chosen)"
    r"|once (it|they|the [\w ,'-]{1,40}) (is|are|exists?) (added|written|built|loaded|placed|decided)"
    r"|\b(?:yet|still|is|are) to come\b|\bTBD\b|\bTODO\b|placeholder|will be (placed|written|added|decided)"
    r"|held here in words", re.I)
_done = None


def done_nodes():
    global _done
    if _done is None:
        _done = set()
        p = os.path.join(ROOT, 'data', 'plans', 'flow-status.csv')
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding='utf-8')):
                if r.get('state') == 'done':
                    _done.add(r['node'])
    return _done


def resolved(what):
    """True if landed, False if still waiting, None if the target is not a form the checker knows."""
    what = what.strip()
    path, _, text = what.partition('#')
    if '/' in path or '.' in os.path.basename(path):
        f = os.path.join(ROOT, path)
        if not os.path.exists(f):
            return False
        if not text:
            return True
        return text in open(f, encoding='utf-8', errors='replace').read()
    if ':' in what or re.fullmatch(r'P\d+[a-z]?', what):
        return what in done_nodes()
    return None


def check_text(label, text):
    """Fails for one note. Work-status wording inside a Pending clause (up to the next sentence end) is fine."""
    fails = []
    covered = []
    for m in MARK.finditer(text):
        r = resolved(m.group(1))
        if r is None:
            fails.append('%s: Pending(%s) names no file, file#text or plan node' % (label, m.group(1)))
        elif r:
            fails.append('%s: STALE, Pending(%s) has landed; rewrite the note to say what is now true' % (label, m.group(1)))
        end = text.find('. ', m.end())
        covered.append((m.start(), len(text) if end < 0 else end + 1))
    for m in WORK.finditer(text):
        if not any(a <= m.start() < b for a, b in covered):
            fails.append('%s: work-status wording %r outside a Pending(...) marker' % (label, m.group(0)))
    return fails


def check_file(path):
    rel = os.path.relpath(path, ROOT).replace('\\', '/')
    fails = []
    if path.endswith('.csv'):
        rows = list(csv.DictReader(open(path, encoding='utf-8')))
        for i, r in enumerate(rows, 2):
            key = r.get('skill_id') or r.get('id') or r.get('node') or 'line %d' % i
            for col in ('notes', 'note', 'detail'):
                if r.get(col):
                    fails += check_text('%s %s' % (rel, key), r[col])
    else:
        for i, line in enumerate(open(path, encoding='utf-8'), 1):
            fails += check_text('%s:%d' % (rel, i), line)
    return fails


def default_files():
    pats = ['data/progressions/social-studies.csv', 'data/progressions/science.csv', 'data/progressions/ela.csv',
            'data/progressions/math.csv', 'data/frames/*.csv', 'docs/courses/*/frame.md']
    out = []
    for p in pats:
        out += sorted(glob.glob(os.path.join(ROOT, p)))
    return out


def main(a):
    if not a or a[0] != 'check':
        raise SystemExit(__doc__)
    files = [os.path.join(ROOT, f) for f in a[1:]] or default_files()
    fails = []
    for f in files:
        fails += check_file(f)
    print('stale: %d file(s), %d failure(s)' % (len(files), len(fails)))
    for x in fails:
        print('  FAIL', x)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
