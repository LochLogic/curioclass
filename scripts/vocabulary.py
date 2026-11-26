"""The word table: student-facing definitions by sense and grade band (consolidation 4.I, Desk card q-word-names-1).

The chain is stated once in docs/CONSOLIDATION-PLAN.md ("Words: from the days"): a word is planned by skill in the
progressions, introduced on a day in the course ledger (`term` rows), and defined for students here.

    data/plans/vocabulary.csv   sense, word, band, definition, fun_fact, fun_fact_source, status, from
        sense            the word plus a meaning tag, lower case with hyphens: cell-biology, cell-table, family-arts
        word             the word as shown (cell)
        band             a band_id of data/bands.csv (k2, 35, 68, 912); one row per sense and band
        fun_fact_source  the source for the fun fact's claim (a URL or a citation), required when there is a fun fact
        status           candidate | written | read | live (only "read" and "live" rows print)
        from             where the row came from: a writer, a day, or "Word Wall <file> <topic>" for an import

A day file marks a word with [[word:<sense>]] or [[word:<sense>|shown form]]. The mark only places the highlight: a
mark with no printable row for the day's band prints as plain text, so it never breaks a page. The day's band is its
own grade through data/bands.csv (Desk answer 4): the course's grade, or, for a course whose grades span two bands, a
`grade` column in days.csv.

    python -X utf8 scripts/vocabulary.py check            the table's own rules (gate: vocabulary-check)
    python -X utf8 scripts/vocabulary.py report [course]  introduced but undefined (the backlog), defined but never used
    python -X utf8 scripts/vocabulary.py --self-test
"""
import csv
import re
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import subjects  # noqa: E402

TABLE = ROOT / 'data' / 'plans' / 'vocabulary.csv'
PLANS = ROOT / 'data' / 'plans'
COLS = ['sense', 'word', 'band', 'definition', 'fun_fact', 'fun_fact_source', 'status', 'from']
STATUS = ('candidate', 'written', 'read', 'live')
PRINTS = ('read', 'live')
SENSE = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*$')
WORD = re.compile(r'\[\[word:([a-z0-9-]+)(?:\|([^\]\n]+))?\]\]')


def rows(path=TABLE):
    if not path.exists():
        return []
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


@lru_cache(None)
def table():
    """(sense, band) -> row."""
    return {(r['sense'], r['band']): r for r in rows()}


@lru_cache(None)
def course_rows():
    with open(PLANS / 'course-list.csv', encoding='utf-8', newline='') as f:
        return {r['id']: r for r in csv.DictReader(f)}


def grades(spec):
    """'K' -> ['k']; '6-8' -> ['6', '7', '8']; 'k-2' -> ['k', '1', '2']."""
    order = ['k'] + [str(n) for n in range(1, 13)]
    s = (spec or '').strip().lower()
    if '-' in s:
        a, b = s.split('-', 1)
        if a in order and b in order:
            return order[order.index(a):order.index(b) + 1]
    return [s] if s in order else []


@lru_cache(None)
def day_grades(course):
    p = PLANS / course / 'days.csv'
    if not p.exists():
        return {}
    with open(p, encoding='utf-8', newline='') as f:
        return {r.get('day', ''): r.get('grade', '') for r in csv.DictReader(f)}


def band(course, day=None):
    """The band a day of the course prints definitions for, or None when it cannot be told (a course spanning two
    bands with no days.csv grade for that day)."""
    gs = grades(course_rows().get(course, {}).get('grade', ''))
    bs = {subjects.band_of(g) for g in gs} - {None}
    if len(bs) == 1:
        return bs.pop()
    if day is not None:
        g = day_grades(course).get(str(day).lstrip('0') or '0', '')
        return subjects.band_of(g) if g else None
    return None


def definition(sense, band_id):
    """The printable row for a sense in a band, or None."""
    r = table().get((sense, band_id))
    return r if r and r['status'] in PRINTS else None


def render(text, course, day=None, html=True):
    """Replace each [[word:...]] mark: a printable row gives a highlighted word, anything else the plain word."""
    b = band(course, day)

    def one(m):
        sense, shown = m[1], m[2]
        r = definition(sense, b) if b else None
        word = (shown or (r['word'] if r else None) or shown_from(sense)).strip()
        if not (r and html):
            return word
        return '<b class="word" data-sense="%s">%s</b>' % (sense, word)
    return WORD.sub(one, text)


def shown_from(sense):
    """A sense id with no row and no shown form prints its word part: cell-biology -> cell. A sense id is the word
    plus one meaning tag, so the last part is the tag; a one-part id is the word itself."""
    parts = sense.split('-')
    return ' '.join(parts[:-1] if len(parts) > 1 else parts)


# ---- the ledger side: what a day introduces

def heads(entry):
    """The word or words a ledger term entry introduces: the part before any '(' or ':', split on commas and
    semicolons, lower case. 'runoff (rain that runs ...)' -> ['runoff']; 'downhill, lower, higher (...)' -> three."""
    h = re.split(r'[(:]', entry, maxsplit=1)[0]
    return [w.strip().lower() for w in re.split(r'[,;]', h) if w.strip()]


def forms(w):
    w = w.lower().strip()
    out = {w}
    for suf in ('es', 's'):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            out.add(w[:-len(suf)])
    out.add(w + 's')
    return out


@lru_cache(None)
def ledger_terms(course, student_only=False):
    """[(where, day, entry, heads)] for the course's term rows; student_only keeps the rows marked student_word yes
    (the backlog, close review finding 4). A [[word:...]] mark may name any term row."""
    p = PLANS / course / 'ledger.csv'
    if not p.exists():
        return []
    with open(p, encoding='utf-8', newline='') as f:
        return [(r['where'], r['day'], r['entry'], heads(r['entry'])) for r in csv.DictReader(f) if r['kind'] == 'term'
                and (not student_only or r.get('student_word') == 'yes')]


def in_ledger(course, word):
    """True when the course's ledger has a term row naming the word (a head, or the word as a whole word inside the
    entry, plurals either way)."""
    fs = forms(word)
    rx = re.compile(r'\b(?:%s)\b' % '|'.join(re.escape(x) for x in sorted(fs, key=len, reverse=True)), re.I)
    return any(fs & set(h) or rx.search(e) for _, _, e, h in ledger_terms(course))


def lint_marks(course, text, lab=''):
    """Lines for a day or piece text: each marked word must have a ledger term row in the course."""
    out = []
    for m in WORD.finditer(text):
        sense, shown = m[1], m[2]
        if not SENSE.match(sense):
            out.append('%s: [[word:%s]] is not a sense id (word plus meaning tag, lower case with hyphens)' % (lab, sense))
            continue
        rs = [r for (s, _), r in table().items() if s == sense]
        word = rs[0]['word'] if rs else (shown or shown_from(sense))
        if not in_ledger(course, word) and not (shown and in_ledger(course, shown)):
            out.append('%s: [[word:%s]] marks "%s", which no ledger term row of %s introduces' % (lab, sense, word, course))
    return out


# ---- checks and reports

def check():
    lines, seen = [], set()
    bands = set(subjects.bands())
    if TABLE.exists():
        with open(TABLE, encoding='utf-8', newline='') as f:
            head = next(csv.reader(f), [])
        if head != COLS:
            lines.append('FAIL data/plans/vocabulary.csv: columns are %s, want %s' % (','.join(head), ','.join(COLS)))
            return lines
    else:
        lines.append('FAIL data/plans/vocabulary.csv is missing')
        return lines
    for i, r in enumerate(rows(), 2):
        at = 'data/plans/vocabulary.csv:%d' % i
        if not SENSE.match(r['sense']):
            lines.append('FAIL %s: sense "%s" is not word plus meaning tag in lower case with hyphens' % (at, r['sense']))
        if r['band'] not in bands:
            lines.append('FAIL %s: band "%s" is not in data/bands.csv' % (at, r['band']))
        if (r['sense'], r['band']) in seen:
            lines.append('FAIL %s: %s in band %s twice' % (at, r['sense'], r['band']))
        seen.add((r['sense'], r['band']))
        if r['status'] not in STATUS:
            lines.append('FAIL %s: status "%s" (want %s)' % (at, r['status'], ', '.join(STATUS)))
        if not r['word'].strip():
            lines.append('FAIL %s: no word' % at)
        if r['status'] in PRINTS and not r['definition'].strip():
            lines.append('FAIL %s: a %s row needs a definition' % (at, r['status']))
        if r['fun_fact'].strip() and not r['fun_fact_source'].strip():
            lines.append('FAIL %s: the fun fact needs a claim-level source' % at)
        if not r['from'].strip():
            lines.append('FAIL %s: no from' % at)
    return lines


def report(only=None):
    """Two lists: student words (ledger term rows marked student_word yes) with no row for the course's band (the
    backlog), and rows no student word in their band introduces. Counts per course; the full lists go to build/vocabulary-report.csv."""
    cl = [c for c, r in course_rows().items() if r.get('status') != 'shelved' and (not only or c == only)]
    defined = {}
    for (s, b), r in table().items():
        defined.setdefault(b, set()).update(forms(r['word']))
    out, used = [], {}
    for c in cl:
        b = band(c)
        for where, day, entry, hs in ledger_terms(c, student_only=True):
            for h in hs:
                used.setdefault(b, set()).add(h)
                if not (forms(h) & defined.get(b, set())):
                    out.append(('undefined', c, b or '?', where, day, h))
    for (s, b), r in sorted(table().items()):
        if not (forms(r['word']) & used.get(b, set())):
            out.append(('unused', '', b, '', '', s))
    path = ROOT / 'build' / 'vocabulary-report.csv'
    path.parent.mkdir(exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['list', 'course', 'band', 'where', 'day', 'word_or_sense'])
        w.writerows(out)
    per = {}
    for k, c, *_ in out:
        per[(k, c)] = per.get((k, c), 0) + 1
    for (k, c), n in sorted(per.items()):
        print('%-9s %-45s %d' % (k, c or '(table)', n))
    print('vocabulary: %d introduced but undefined, %d defined but never used -> %s'
          % (sum(1 for x in out if x[0] == 'undefined'), sum(1 for x in out if x[0] == 'unused'),
             path.relative_to(ROOT).as_posix()))
    return 0


def self_test():
    assert heads('runoff (rain that runs over the ground)') == ['runoff']
    assert heads('downhill, lower, higher (water runs to lower ground)') == ['downhill', 'lower', 'higher']
    assert shown_from('cell-biology') == 'cell' and shown_from('photosynthesis') == 'photosynthesis'
    assert grades('k-2') == ['k', '1', '2'] and grades('6-8') == ['6', '7', '8'] and grades('K') == ['k']
    assert band('science-grade-2') == 'k2' and band('math-grade-4') == '35'
    assert 'cells' in forms('cell') and 'cell' in forms('cells')
    t = 'Plants are made of [[word:cell-biology|cells]] and [[word:root-plant]].'
    assert render(t, 'science-grade-2') == 'Plants are made of cells and root.'   # no rows yet: plain text
    assert not SENSE.match('Cell_biology') and SENSE.match('cell-biology')
    print('vocabulary self-test: all passed')
    return 0


def main(a):
    if a[:1] == ['--self-test']:
        return self_test()
    if a[:1] == ['check']:
        lines = check()
        print('\n'.join(lines))
        print('vocabulary: %d row(s) checked, %d line(s)' % (len(rows()), len(lines)))
        return 1 if any(x.startswith('FAIL') for x in lines) else 0
    if a[:1] == ['report']:
        return report(a[1] if len(a) > 1 else None)
    raise SystemExit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
