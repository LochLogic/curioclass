"""Subject ids and grade bands, one place for the curriculum scripts (consolidation 4.H).

The four core subjects keep three names: the subject id (course-list.csv `subject`, ledger and progression file
name), the course id prefix, and the words used in prose. Grade bands come from data/bands.csv.

    import subjects
    subjects.CORE                      ('ela', 'social-studies', 'math', 'science')
    subjects.PREFIX['ela']             'english-language-arts'
    subjects.progression_file('ela')   Path to data/progressions/ela.csv
    subjects.ladder('science')         the subject's courses in teaching order (course-list.csv row order, not shelved)
    subjects.band_of('4')              '35' (a band_id of data/bands.csv; grades k, 1 ... 12)

Readers: ledger.py (LADDER), coursegen.py (SUBJECTS), plan_flow.py (PFILE), front_office.py (PROG_FILE).
"""
import csv
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / 'data' / 'plans'

CORE = ('ela', 'social-studies', 'math', 'science')
PREFIX = {'ela': 'english-language-arts', 'social-studies': 'social-studies', 'math': 'math', 'science': 'science'}
WORDS = {'ela': 'English language arts', 'social-studies': 'social studies', 'math': 'math', 'science': 'science'}


def progression_file(subject):
    return ROOT / 'data' / 'progressions' / ('%s.csv' % subject)


def ladder(subject):
    return ladders((subject,))[subject]


def ladders(subjects=CORE):
    """Each subject's courses in teaching order: the row order of data/plans/course-list.csv (kept in grade order,
    and within a grade in the order the courses are taken), shelved courses left out."""
    out = {s: [] for s in subjects}
    with open(PLANS / 'course-list.csv', encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            if r['subject'] in out and r['status'] != 'shelved':
                out[r['subject']].append(r['id'])
    return out


@lru_cache(None)
def bands():
    """band_id -> list of grades (k, 1 ... 12), from data/bands.csv."""
    with open(ROOT / 'data' / 'bands.csv', encoding='utf-8', newline='') as f:
        return {r['band_id']: [g.strip().lower() for g in r['grades'].split(';')] for r in csv.DictReader(f)}


def band_of(grade):
    g = str(grade).strip().lower()
    for b, gs in bands().items():
        if g in gs:
            return b
    return None
