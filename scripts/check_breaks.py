r"""Check the Break Box sheets (data/closet/breaks/<id>.md) against docs/BREAK-BOX-PLAN.md.

    python scripts/check_breaks.py              check every grade, exit 1 on any problem
    python scripts/check_breaks.py k 3 12       check some grades

A sheet file is "key: value" header lines (title, grade, order, kind, time, where, mess, grownup, players, materials,
then nice and night_before when the sheet has them), a blank line, then the ## parts in plan order. Each grade has 30
sheets, ordered 1 to 30. build_site.py uses load() for /closet/break-box/ and runs problems() and grade_problems() so a
bad sheet stops a closet build. The sheets were first drafted in docs/break-box/grade-<g>.md.
"""
import re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BREAKS = ROOT / 'data' / 'closet' / 'breaks'
GRADES = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
K2 = {'k', '1', '2'}
HEADER = ['title', 'grade', 'order', 'kind', 'time', 'where', 'mess', 'grownup', 'players', 'materials']
OPTIONAL = ['nice', 'night_before']
PARTS = ['The big idea', 'Goals', 'Objectives', 'Get ready', 'Steps', 'Make it yours', 'Stuck?', 'Show it off',
         'Clean up', 'For the grown-up']
KINDS = {'Build', 'Story', 'Art', 'Pretend', 'Science', 'Game', 'Puzzle', 'Music', 'Move', 'Outside', 'Kitchen',
         'Kindness'}
WHERE = {'Indoors', 'Outdoors', 'Either'}
MESS = {'Low', 'Medium', 'High'}
GROWN = {'With you', 'Nearby', 'On your own'}
PLAYERS = {'1', '1+', '2+'}
WORDS = (180, 750)  # per sheet


def idea(big):
    """One line for the shelf card: the big idea's first sentence (two when the first is very short)."""
    s = re.sub(r'^Read aloud:\s*', '', ' '.join(big.split())).strip('"“” ')
    parts = [p.strip() for p in re.findall(r'.+?[.!?]["”]?(?=\s|$)', s)] or [s]
    line = parts[0]
    if len(line.split()) < 7 and len(parts) > 1:
        line += ' ' + parts[1]
    line = line.strip('“” ')
    if line.startswith('"') and line.endswith('"') and line.count('"') == 2:
        line = line[1:-1]
    return line + '"' if line.count('"') % 2 else line


def load(grades=None):
    """{sheet_id: sheet dict} for every sheet file (or the sheets of some grades)."""
    out = {}
    for f in sorted(BREAKS.glob('*.md')):
        text = f.read_text(encoding='utf-8')
        head, _, body = text.partition('\n\n')
        s = {'id': f.stem, 'file': f.name, 'url': f'/closet/break-box/{f.stem}/', 'bad_lines': [], 'body': body}
        for line in head.splitlines():
            k, sep, v = line.partition(':')
            if sep:
                s[k.strip()] = v.strip()
            else:
                s['bad_lines'].append(line)
        if grades and s.get('grade') not in grades:
            continue
        s['parts'] = [(m.group(1).strip(), m.group(2).strip())
                      for m in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', body, re.M | re.S)]
        s['idea'] = idea(dict(s['parts']).get('The big idea', ''))
        s['solo'] = s.get('players') in ('1', '1+')
        s['outside'] = s.get('where') in ('Outdoors', 'Either')
        out[f.stem] = s
    return out


def problems(s):
    out = []
    say = lambda msg: out.append(f"{s['file']} (grade {s.get('grade')} #{s.get('order')} {s.get('title')}): {msg}")
    for line in s['bad_lines']:
        say(f'header line {line!r}')
    keys = [k for k in s if k in HEADER + OPTIONAL]
    for k in HEADER:
        if not s.get(k):
            say(f'no {k}')
    grade = s.get('grade')
    if grade not in GRADES:
        say(f'grade {grade!r}')
    if s.get('kind') not in KINDS:
        say(f"kind {s.get('kind')!r}")
    t = re.fullmatch(r'(\d+)-(\d+) min', s.get('time', ''))
    if not t:
        say(f"time {s.get('time')!r}")
    else:
        lo, hi = int(t.group(1)), int(t.group(2))
        if not (45 <= lo < hi <= 120 and 60 <= (lo + hi) / 2 <= 120):
            say(f"time {s['time']!r} out of range")
    if s.get('where') not in WHERE:
        say(f"where {s.get('where')!r}")
    if s.get('mess') not in MESS:
        say(f"mess {s.get('mess')!r}")
    if s.get('grownup') not in GROWN:
        say(f"grown-up {s.get('grownup')!r}")
    elif grade in K2 and s['grownup'] != 'With you':
        say('K-2 sheets need "With you"')
    if s.get('players') not in PLAYERS:
        say(f"players {s.get('players')!r}")
    found = [name for name, _ in s['parts']]
    if found != PARTS:
        say(f'parts {found}')
    secs = dict(s['parts'])
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
    text = ' '.join(s.get(k, '') for k in keys if k not in ('title', 'grade', 'order')) + '\n' + s['body']
    words = len(re.findall(r"[A-Za-z0-9']+", text))
    if not WORDS[0] <= words <= WORDS[1]:
        say(f'{words} words')
    whole = s['title'] + '\n' + text if s.get('title') else text
    if '\u2014' in whole or ' -- ' in whole:
        say('em dash')
    if re.search(r'\bCurio\b(?! Class)', whole):
        say('"Curio" alone')
    return out


def grade_problems(sheets):
    """Balance rules for each grade's 30 sheets, plus titles that repeat across grades."""
    out, seen = [], {}
    for g in GRADES:
        rows = sorted((s for s in sheets.values() if s.get('grade') == g), key=lambda s: int(s.get('order') or 0))
        if not rows:
            continue
        if [s.get('order') for s in rows] != [str(i) for i in range(1, 31)]:
            out.append(f"grade {g}: sheets ordered {[s.get('order') for s in rows]}, want 1-30")
        kinds = Counter(s.get('kind') for s in rows)
        need = {('Build',): 3, ('Story',): 3, ('Art',): 3, ('Science',): 3, ('Pretend',): 3, ('Game', 'Puzzle'): 3,
                ('Move', 'Outside'): 3, ('Music',): 2, ('Kitchen',): 1, ('Kindness',): 1}
        for ks, n in need.items():
            if sum(kinds[k] for k in ks) < n:
                out.append(f'grade {g}: fewer than {n} {"/".join(ks)}')
        if sum(s['solo'] for s in rows) < 20:
            out.append(f'grade {g}: fewer than 20 solo sheets')
        if sum(s['outside'] for s in rows) < 6:
            out.append(f'grade {g}: fewer than 6 outdoor sheets')
        if sum(s.get('mess') in ('Low', 'Medium') for s in rows) < 18:
            out.append(f'grade {g}: fewer than 18 low or medium mess')
        for s in rows:
            t = s.get('title', '')
            key = re.sub(r'[^a-z0-9]+', ' ', t.lower().replace("'s ", ' ').replace("'", '')).strip()
            if key in seen:
                out.append(f'title {t!r} in grade {g} repeats grade {seen[key]}')
            seen.setdefault(key, g)
    return out


def main(args):
    grades = args or GRADES
    sheets = load(grades)
    problems_ = [p for s in sheets.values() for p in problems(s)] + grade_problems(sheets)
    for g in grades:
        if not any(s.get('grade') == g for s in sheets.values()):
            problems_.append(f'grade {g}: no sheets in {BREAKS.relative_to(ROOT)}')
    for p in problems_:
        print(p)
    print(f'{len(sheets)} sheets checked, {len(problems_)} problems')
    return 1 if problems_ else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
