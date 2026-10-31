r"""Check the Break Box draft sheets (docs/break-box/grade-<g>.md) against docs/BREAK-BOX-PLAN.md.

    python scripts/check_breaks.py              check every grade, exit 1 on any problem
    python scripts/check_breaks.py k 3 12       check some grades

A grade file is a "# Break Box: ..." title, an index, then 30 sheets. Each sheet starts "## N. Title", then the info
row table (Kind, Time, Where, Mess, Grown-up, Players), a **Materials:** line, then the ### parts in plan order.
"""
import re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / 'docs' / 'break-box'
GRADES = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
K2 = {'k', '1', '2'}
PARTS = ['The big idea', 'Goals', 'Objectives', 'Get ready', 'Steps', 'Make it yours', 'Stuck?', 'Show it off',
         'Clean up', 'For the grown-up']
KINDS = {'Build', 'Story', 'Art', 'Pretend', 'Science', 'Game', 'Puzzle', 'Music', 'Move', 'Outside', 'Kitchen',
         'Kindness'}
WHERE = {'Indoors', 'Outdoors', 'Either'}
MESS = {'Low', 'Medium', 'High'}
GROWN = {'With you', 'Nearby', 'On your own'}
PLAYERS = {'1', '1+', '2+'}
WORDS = (180, 750)  # per sheet
SHEET = re.compile(r'^## (\d+)\. (.+)$', re.M)
ROW = re.compile(r'^\|\s*Kind\s*\|.*\n\|[-| ]+\|\n\|(.+)\|\s*$', re.M)


def sheets(text):
    heads = list(SHEET.finditer(text))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        yield int(m.group(1)), m.group(2).strip(), text[m.end():end]


def check_sheet(grade, n, title, body):
    out = []
    say = lambda msg: out.append(f'grade {grade} #{n} {title}: {msg}')
    row = ROW.search(body)
    if not row:
        say('no info row')
        cells = None
    else:
        cells = [c.strip() for c in row.group(1).split('|')]
        if len(cells) != 6:
            say(f'info row has {len(cells)} cells')
            cells = None
    if cells:
        kind, time, where, mess, grown, players = cells
        if kind not in KINDS:
            say(f'kind {kind!r}')
        t = re.fullmatch(r'(\d+)-(\d+) min', time)
        if not t:
            say(f'time {time!r}')
        else:
            lo, hi = int(t.group(1)), int(t.group(2))
            if not (45 <= lo < hi <= 120 and 60 <= (lo + hi) / 2 <= 120):
                say(f'time {time!r} out of range')
        if where not in WHERE:
            say(f'where {where!r}')
        if mess not in MESS:
            say(f'mess {mess!r}')
        if grown not in GROWN:
            say(f'grown-up {grown!r}')
        elif grade in K2 and grown != 'With you':
            say('K-2 sheets need "With you"')
        if players not in PLAYERS:
            say(f'players {players!r}')
    if '**Materials:**' not in body:
        say('no **Materials:** line')
    found = re.findall(r'^### (.+?)\s*$', body, re.M)
    if found != PARTS:
        say(f'parts {found}')
    secs = dict(zip(found, re.split(r'^### .+$', body, flags=re.M)[1:]))
    goals = re.findall(r'^- ', secs.get('Goals', ''), re.M)
    if not 2 <= len(goals) <= 3:
        say(f'{len(goals)} goals')
    obj = re.findall(r'^- (.*)', secs.get('Objectives', ''), re.M)
    lead = 'Your child can' if grade in K2 else 'I can'
    if len(obj) != 3 or not all(o.startswith(lead) for o in obj):
        say(f'objectives must be 3 lines starting "{lead}"')
    steps = re.findall(r'^\d+\. ', secs.get('Steps', ''), re.M)
    if not 5 <= len(steps) <= 9:
        say(f'{len(steps)} steps')
    twists = re.findall(r'^- ', secs.get('Make it yours', ''), re.M)
    if len(twists) != 3:
        say(f'{len(twists)} twists')
    flat = lambda part: ' '.join(secs.get(part, '').split())
    if 'Ask at dinner' not in flat('For the grown-up'):
        say('no "Ask at dinner" question')
    if grade in K2 and 'Read aloud' not in flat('The big idea'):
        say('K-2 big idea needs "Read aloud"')
    words = len(re.findall(r"[A-Za-z0-9']+", body))
    if not WORDS[0] <= words <= WORDS[1]:
        say(f'{words} words')
    if '—' in body or ' -- ' in body:
        say('em dash')
    if re.search(r'\bCurio\b(?! Class)', body):
        say('"Curio" alone')
    return out, cells


def check_grade(grade):
    path = DIR / f'grade-{grade}.md'
    if not path.exists():
        return [f'grade {grade}: missing {path.relative_to(ROOT)}'], []
    text = path.read_text()
    problems, titles, rows = [], [], []
    found = list(sheets(text))
    if [n for n, _, _ in found] != list(range(1, 31)):
        problems.append(f'grade {grade}: sheets numbered {[n for n, _, _ in found]}, want 1-30')
    for n, title, body in found:
        p, cells = check_sheet(grade, n, title, body)
        problems += p
        titles.append(title)
        if cells:
            rows.append(cells)
    if rows:
        kinds = Counter(r[0] for r in rows)
        need = {('Build',): 3, ('Story',): 3, ('Art',): 3, ('Science',): 3, ('Pretend',): 3, ('Game', 'Puzzle'): 3,
                ('Move', 'Outside'): 3, ('Music',): 2, ('Kitchen',): 1, ('Kindness',): 1}
        for ks, n in need.items():
            if sum(kinds[k] for k in ks) < n:
                problems.append(f'grade {grade}: fewer than {n} {"/".join(ks)}')
        if sum(r[5] in ('1', '1+') for r in rows) < 20:
            problems.append(f'grade {grade}: fewer than 20 solo sheets')
        if sum(r[2] in ('Outdoors', 'Either') for r in rows) < 6:
            problems.append(f'grade {grade}: fewer than 6 outdoor sheets')
        if sum(r[3] in ('Low', 'Medium') for r in rows) < 18:
            problems.append(f'grade {grade}: fewer than 18 low or medium mess')
    return problems, titles


def main(args):
    grades = args or GRADES
    problems, seen = [], {}
    for g in grades:
        p, titles = check_grade(g)
        problems += p
        for t in titles:
            key = re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()
            if key in seen:
                problems.append(f'title {t!r} in grade {g} repeats grade {seen[key]}')
            seen.setdefault(key, g)
    for p in problems:
        print(p)
    print(f'{len(seen)} sheets checked, {len(problems)} problems')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
