"""Write docs/courses/<course>/DEFAULTS.md, what holds every day of a course, from band and subject blocks.

    python -X utf8 scripts/defaults.py <course>|all [--force] [--dry]

Built 2026-11-18 for later.csv L76 (science and math probe: neither course had a DEFAULTS.md, so caps and "what holds
every day" fell back to general defaults; docs/reviews/probe-science-math-2026-11-18.md). The day length comes from
data/plans/frames.csv; the rest from the blocks below: one per grade band, one per subject, and the probe rules every
course shares. A section plan or day writes only what differs. Never overwrites a DEFAULTS.md without --force: a
course's own file (kindergarten social studies, written at its probe) is the course's, and edits made to a generated
file by hand are kept. Grade 4 math and grade 6 ELA's older folders are never touched.

The numbers marked "ours, untested" are starting caps, to be moved by the first probe in that band.
"""
import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAMES = ROOT / 'data' / 'plans' / 'frames.csv'
BLIND = ('math-4', 'ela-6')
SUBJECT = {'math': 'math', 'science': 'science', 'ela': 'English', 'social-studies': 'social studies'}


def band(g):
    n = 0 if g == 'K' else int(g)
    return 'K2' if n <= 2 else '35' if n <= 5 else '68' if n <= 8 else 'HS'


STUDENT_CAP = {'K': 60, '1': 100, '2': 150}   # words a student reads; grades 3 to 5 350 (LESSON-DAY), then below
BAND_CAP = {'35': 350, '68': 400, 'HS': 450}

BAND = {
    'K2': [
        '**Children read little or not at all.** The student page is pictures, boxes to draw in and short labels; a '
        'line on the teacher page says what to read aloud (in English, the text the day teaches children to read is '
        'printed for them). 18 point type.',
        '**Stems are spoken.** An exit or end item asks one thing, aloud, in a child\'s words; three asks in one stem '
        'are three items. Exit and end items have `path` spoken in items.csv unless the plan names a drawing or a '
        'written word the child can make.',
        '**Turns are counted.** A part where each child takes a turn is children times turn length. The teacher hears '
        'a rotating six a day and the record sheet has a column naming who was heard.',
        '**One marking scale:** shown, shown with help, not yet seen.',
        '**Stories:** one actor per scene, so a child can say who did what; practice cases are invented and the '
        'teacher says so aloud.',
        '**At home.** 15 to 30 minutes, one grown-up or older child, any day skippable; the exit is asked aloud.',
    ],
    '35': [
        '14 point type; no sentence over 15 words.',
        '**At home.** 30 to 40 minutes, one parent and one child, at most 170 words; no timer, grade or score.',
    ],
    '68': [
        '12 point type.',
        '**At home.** 30 to 40 minutes, one parent and one student, at most 170 words; no timer, grade or score.',
    ],
    'HS': [
        '12 point type.',
        '**At home.** 30 to 40 minutes, a student working alone or with anyone at home, at most 170 words; no timer, '
        'grade or score.',
    ],
}

SUBJ = {
    'science': [
        '**Shared equipment fits the minutes.** Groups times minutes a turn fits inside the part, or the reading is a '
        'demonstration with readings shared. Field 8 of the unit plan sets supply and safety limits; a task they forbid '
        'is not written.',
        '**Real readings, with a fallback.** The class measures where it can; an invented record is the named fallback, '
        'said aloud to be invented, and the plan says what happens when a reading fails. Safety notes name the '
        'equipment actually used.',
        '**Set-ups for later units** take at most 5 minutes of a day and are named as set-ups.',
    ],
    'math': [
        '**Notation is taught before it is tested,** across section edges too. The key opens with the line lesson.py '
        'picks by standard.',
        '**Every tool has a paper path,** and every question is an items.csv row with a computed key.',
    ],
    'ela': [
        '**Core texts are written or checked before days.** A text still "to write" stops the day skeleton; the day '
        'writer never writes one.',
        '**A cold check reads a new text,** not one taught, and does not restate the taught text\'s central idea.',
    ],
    'social-studies': [
        '**Sources are free and checked once for the course** at plan data (status `checked: <date>`); a passage that '
        'cannot be checked is cut. A reserved source is never named before its day.',
        '**Sensitive topics** follow the frame\'s lines; no student reports on home, family, money, bodies or religion.',
    ],
}

COMMON = [
    '**Repair slots fit what is routed to them.** Every hand-back lands in a named part of its day (handbacks.csv '
    '`where`) that holds its minutes; a warm-up holds one repair of at most 5 minutes (plan.py checks).',
    '**Exits ask a transfer:** a new case that needs the day\'s idea, not the worked example in new numbers.',
    '**Talk.** Every student may pass in public talk; no one is the example of a mistake.',
]


def frames():
    with open(FRAMES, encoding='utf-8', newline='') as f:
        return [r for r in csv.DictReader(f) if not any(b in r['course'] for b in BLIND)]


def text(r):
    g, b = r['grade'], band(r['grade'])
    lo, hi = int(r['minutes_min']), int(r['minutes_max'])
    mins = '%d minutes' % lo if lo == hi else '%d to %d minutes' % (lo, hi)
    cap = 'at most {:,} words of teacher prose (15 a minute of the day)'.format(15 * hi) if lo == hi else \
        'teacher prose at most 15 words a minute of the day\'s own length (%d at %d minutes)' % (15 * hi, hi)
    student = STUDENT_CAP.get(g) or BAND_CAP[b]
    grade = 'Kindergarten' if g == 'K' else 'Grade %s' % g
    generic = r['title'].lower().startswith(('math', 'science', 'english', 'social', 'grade', 'kindergarten'))
    L = ['# %s: what holds every day' % (('%s %s' % (grade, SUBJECT[r['subject']])) if generic else r['title']),
         '',
         'Generated %s by scripts/defaults.py (later.csv L76) from its band and subject blocks; edit any line that '
         'differs for this course and it is kept. A section plan or day writes only what differs from this.'
         % date.today().isoformat(),
         '',
         '- **The day.** %s (frames.csv); %s.' % (mins, cap),
         '- **Student page:** at most %d words a student reads, everything printed included (ours, untested)%s' % (
             student, '.' if b == 'K2' else '; ' + BAND[b][0])]
    L += ['- ' + x for x in (BAND[b] if b == 'K2' else BAND[b][1:]) + SUBJ[r['subject']] + COMMON]
    return '\n'.join(L).replace('#  ', '# ').replace('  :', ':') + '\n'


def main(a):
    force, dry = '--force' in a, '--dry' in a
    a = [x for x in a if not x.startswith('--')]
    if not a:
        print(__doc__)
        return 2
    rows = frames()
    if a[0] != 'all':
        rows = [r for r in rows if r['course'] == a[0]]
        if not rows:
            print('%s is not a course in data/plans/frames.csv (or is held)' % a[0])
            return 1
    for r in rows:
        p = ROOT / 'docs' / 'courses' / r['course'] / 'DEFAULTS.md'
        if dry:
            print('---- %s\n%s' % (p, text(r)))
            continue
        if p.exists() and not force:
            print('%s: kept (exists)' % p.relative_to(ROOT))
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text(r), encoding='utf-8')
        print('%s: written' % p.relative_to(ROOT))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
