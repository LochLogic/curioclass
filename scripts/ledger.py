"""The subject ledger: what each grade of a subject actually taught, carried up the ladder.

    python -X utf8 scripts/ledger.py add <subject> <course> <where> <day> <kind> "<entry>" ["<note>"]
    python -X utf8 scripts/ledger.py show <subject> [--before <course>] [--kind <kind>]
    python -X utf8 scripts/ledger.py check <subject>

Built 2026-11-18 for the science kindergarten to grade 3 ladder test (later.csv L81,
docs/reviews/assessment-dirty-fill-2026-11-18.md). One file per subject, data/plans/ledgers/<subject>.csv. Every
section writer and day writer in a ladder run reads it (`show`, everything below its own course plus its own course so
far) and adds what it teaches (`add`). Writers never edit the CSV by hand.

Columns: course, where (u01-2, a section, or s01 for a unit-level entry), day (the day number, or blank when planned
for the whole section), kind, entry, note, stage (planned when a section plan adds it, written when a day adds it).

Kinds:
- term: a word students are taught to use;
- notation: a symbol or written form;
- model: a picture, diagram or explanation students build;
- case: a phenomenon, example or story used to teach (later grades may revisit it, never as an exit);
- investigation: a hands-on test or observation;
- material: equipment or supplies students handle;
- routine: a classroom routine students learn (a notebook page, a talk move);
- text: a read-aloud, passage or sheet text;
- skill: a practice students do (measure with a ruler, sort by one property).
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / 'data' / 'plans' / 'ledgers'
COLS = ['course', 'where', 'day', 'kind', 'entry', 'note', 'stage']
KINDS = ('term', 'notation', 'model', 'case', 'investigation', 'material', 'routine', 'text', 'skill')
LADDER = {'science': ['science-kindergarten', 'science-grade-1', 'science-grade-2', 'science-grade-3',
                      'science-grade-4', 'science-grade-5', 'science-grade-6', 'science-grade-7',
                      'science-grade-8', 'biology', 'chemistry', 'physics']}


def path(subject):
    return DIR / ('%s.csv' % subject)


def rows(subject):
    p = path(subject)
    if not p.exists():
        return []
    with open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def add(subject, course, where, day, kind, entry, note=''):
    if subject not in LADDER or course not in LADDER[subject]:
        sys.exit('ledger: %s is not on the %s ladder' % (course, subject))
    if kind not in KINDS:
        sys.exit('ledger: kind must be one of %s' % ', '.join(KINDS))
    if day and not day.isdigit():
        sys.exit('ledger: day is a number or blank')
    if not entry.strip():
        sys.exit('ledger: entry is empty')
    p = path(subject)
    p.parent.mkdir(parents=True, exist_ok=True)
    new = not p.exists()
    stage = 'written' if day else 'planned'
    with open(p, 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        if new:
            w.writerow(COLS)
        w.writerow([course, where, day, kind, entry.strip(), note.strip(), stage])
    print('added: %s %s day %s %s: %s' % (course, where, day or '-', kind, entry.strip()))


def show(subject, before=None, kind=None):
    order = LADDER[subject]
    stop = order.index(before) if before in order else len(order)
    keep = set(order[:stop + 1]) if before else set(order)
    out = [r for r in rows(subject) if r['course'] in keep and (not kind or r['kind'] == kind)]
    if not out:
        print('(the %s ledger is empty so far)' % subject)
        return
    cur = None
    for r in sorted(out, key=lambda r: (order.index(r['course']), r['where'], int(r['day'] or 0))):
        if r['course'] != cur:
            cur = r['course']
            print('\n## %s' % cur)
        print('- %s %s %s: %s%s' % (r['where'], ('day ' + r['day']) if r['day'] else '(planned)', r['kind'],
                                     r['entry'], (' (' + r['note'] + ')') if r['note'] else ''))


def check(subject):
    bad = 0
    for i, r in enumerate(rows(subject), 2):
        if None in r or set(r) != set(COLS):
            print('line %d: wrong cell count' % i)
            bad += 1
        elif r['kind'] not in KINDS or r['course'] not in LADDER[subject]:
            print('line %d: unknown kind or course' % i)
            bad += 1
    print('%s ledger: %d rows, %d problems' % (subject, len(rows(subject)), bad))
    return 1 if bad else 0


def main(a):
    if not a or a[0] not in ('add', 'show', 'check'):
        print(__doc__)
        return 2
    if a[0] == 'add':
        if len(a) < 7:
            sys.exit('ledger add: subject course where day kind entry [note]')
        add(*a[1:9])
        return 0
    flags = dict(zip(a[2::2], a[3::2])) if len(a) > 2 else {}
    if a[0] == 'show':
        show(a[1], flags.get('--before'), flags.get('--kind'))
        return 0
    return check(a[1])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
