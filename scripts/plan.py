"""Course plans as data: gates, generated tables, reading packs, defect ledger.

    python -X utf8 scripts/plan.py check  [course]            gates; exit 1 on any failure
    python -X utf8 scripts/plan.py tables [course]            rewrite the generated blocks in the plan files
    python -X utf8 scripts/plan.py pack   <course> <stretch>  print one agent's reading pack
    python -X utf8 scripts/plan.py defect <course> <artifact> <layer> <found_by> <kind> "<summary>" [ref]
    python -X utf8 scripts/plan.py defects                    counts by reader and layer

Facts live in data/plans/<course>/ (parts, days, items, wrongs, errors). The plan files in
docs/courses/<course>/ keep prose for judgment; their tables are generated between
<!-- gen:NAME --> and <!-- /gen --> markers. See data/plans/README.md.
"""
import ast, csv, io, re, sys, datetime
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / 'data' / 'plans'
DOCS = ROOT / 'docs' / 'courses'
LESSON_MIN = 50          # the lesson part of a 60 minute day (spine: warm-up 5, lesson about 50, exit 5)
DAY_MIN = 60
KINDS = {'Understanding', 'Fluency', 'Use', 'Check', 'Respond'}
MARKS = {'key', 'light'}
READERS = {'script', 'expert', 'sara', 'teacher', 'student', 'cory', 'writer'}


def rows(course, name):
    p = PLANS / course / (name + '.csv')
    if not p.exists():
        return []
    with io.open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def courses():
    return sorted(d.name for d in PLANS.iterdir() if d.is_dir())


# ------------------------------------------------------------------ recomputing a key
class _Frac(ast.NodeTransformer):
    def visit_Constant(self, n):
        if isinstance(n.value, int) and not isinstance(n.value, bool):
            return ast.copy_location(ast.Call(ast.Name('F', ast.Load()), [n], []), n)
        return n


def compute(expr):
    """Evaluate one expression exactly. ';' stands for ',' so cells stay simple. Only arithmetic,
    comparisons, and/or, F(a;b) fractions, len and set literals are allowed."""
    tree = ast.parse(expr.replace(';', ','), mode='eval')
    for n in ast.walk(tree):
        if isinstance(n, (ast.Attribute, ast.Subscript, ast.Lambda, ast.Import, ast.ImportFrom)):
            raise ValueError('not allowed in a compute cell: ' + type(n).__name__)
        if isinstance(n, ast.Call) and not (isinstance(n.func, ast.Name) and n.func.id in ('F', 'len')):
            raise ValueError('only F() and len() may be called')
        if isinstance(n, ast.Name) and n.id not in ('F', 'len', 'True', 'False'):
            raise ValueError('unknown name ' + n.id)
    tree = ast.fix_missing_locations(_Frac().visit(tree))
    return eval(compile(tree, '<compute>', 'eval'), {'__builtins__': {}}, {'F': Fraction, 'len': len})


def parse_value(v):
    v = v.strip().replace(',', '')
    if v in ('True', 'False'):
        return v == 'True'
    m = re.fullmatch(r'(\d+) (\d+)/(\d+)', v)
    if m:
        return int(m[1]) + Fraction(int(m[2]), int(m[3]))
    return Fraction(v)


def split(cell):
    return [c.strip() for c in cell.split('|')] if cell.strip() else []


def check_key(label, comp, val, fails):
    cs, vs = split(comp), split(val)
    if len(cs) != len(vs):
        fails.append('%s: %d compute parts but %d values' % (label, len(cs), len(vs))); return
    for c, v in zip(cs, vs):
        try:
            got, want = compute(c), parse_value(v)
        except Exception as e:
            fails.append('%s: cannot evaluate "%s" (%s)' % (label, c, e)); continue
        if got != want:
            fails.append('%s: key says %s but %s = %s' % (label, v, c, got))


def numbers(text):
    """The set of numbers in a stem or example: used for the no-reuse rule."""
    t = re.sub(r'\b(?:MP|E|day|Day|stretch|lesson|unit)\.? ?\d+', ' ', text)
    t = re.sub(r'\((?:a|b|c|d|e|f)\)', ' ', t)
    return frozenset(re.findall(r'\d+(?: \d+/\d+)?(?:,\d{3})*', t))


# ------------------------------------------------------------------ the gates
def check(course):
    fails, notes = [], []
    parts, days, items = rows(course, 'parts'), rows(course, 'days'), rows(course, 'items')
    wrongs, errors = rows(course, 'wrongs'), rows(course, 'errors')
    subj, grade = course.rsplit('-', 1)
    with io.open(ROOT / 'data' / 'units.csv', encoding='utf-8', newline='') as f:
        units = [u for u in csv.DictReader(f) if u['subject'] == subj and u['grade'] == grade]
    codes = set()
    std = ROOT / 'data' / 'standards' / 'ccss-math-standards.txt'
    if subj == 'math' and std.exists():
        codes = {l.split('\t')[0] for l in std.read_text(encoding='utf-8').splitlines() if l and not l.startswith('#')}
    ids = {i['item_id'] for i in items}
    if len(ids) != len(items):
        fails.append('items.csv: duplicate item_id')
    letters = {(e['stretch'], e['letter']) for e in errors}
    stretches = sorted({d['stretch'] for d in days} | {i['stretch'] for i in items}, key=int)

    # 1. keys: every key-marked item is recomputed; teacher-judged items too where a value is given
    for i in items:
        if codes and i['code'] not in codes:
            fails.append('%s: standard code %s is not in the standards file' % (i['item_id'], i['code']))
        if i['judged'] not in ('key', 'teacher'):
            fails.append('%s: judged must be key or teacher' % i['item_id'])
        if i['judged'] == 'key' and not i['compute'].strip():
            fails.append('%s: marked against a key but has no compute cell' % i['item_id'])
        if i['compute'].strip():
            check_key(i['item_id'], i['compute'], i['value'], fails)
            for v in split(i['value']):
                if v not in ('True', 'False') and v not in i['answer'].replace(',', ''):
                    fails.append('%s: value %s is not in the printed answer "%s"' % (i['item_id'], v, i['answer']))
    for w in wrongs:
        lab = '%s wrong answer "%s"' % (w['item_id'], w['shown'])
        if w['item_id'] not in ids:
            fails.append(lab + ': no such item')
        if w['compute'].strip():
            check_key(lab, w['compute'], w['value'], fails)
        st = next((i['stretch'] for i in items if i['item_id'] == w['item_id']), None)
        if w['error'] and (st, w['error']) not in letters:
            fails.append(lab + ': error letter %s is not in the error register' % w['error'])

    for s in stretches:
        sp = [p for p in parts if p['stretch'] == s]
        end = [i for i in items if i['stretch'] == s and i['check'] == 'end']
        # 2. every part of every standard has an end-check item
        for p in sp:
            if not any(i['code'] == p['code'] and i['part'] == p['part'] for i in end):
                fails.append('stretch %s: %s part (%s) "%s" has no end-check item' % (s, p['code'], p['part'], p['text']))
        for i in end:
            if sp and not any(i['code'] == p['code'] and i['part'] == p['part'] for p in sp):
                fails.append('%s: part (%s) of %s is not listed in parts.csv' % (i['item_id'], i['part'], i['code']))
        if codes:
            for p in sp:
                if p['code'] not in codes:
                    fails.append('parts.csv: %s is not in the standards file' % p['code'])
        # 3. no end-check item or exit question reuses the numbers of a taught example or of another item
        taught = [('error %s example' % e['letter'], numbers(e['example'])) for e in errors if e['stretch'] == s]
        taught += [('day %s' % d['day'], numbers(d['opens'] + ' ' + d['by_hand'])) for d in days if d['stretch'] == s]
        asked = [(i['item_id'], numbers(i['stem'])) for i in items if i['stretch'] == s and i['check'] in ('end', 'exit')]
        for k, (a, na) in enumerate(asked):
            if len(na) < 2:
                continue
            for b, nb in taught:
                if len(nb) >= 2 and na <= nb:
                    fails.append('%s reuses the numbers of %s: %s' % (a, b, ', '.join(sorted(na))))
            for b, nb in asked[k + 1:]:
                if na == nb:
                    fails.append('%s and %s use the same numbers: %s' % (a, b, ', '.join(sorted(na))))
        # 4. days
        sd = sorted((d for d in days if d['stretch'] == s), key=lambda d: int(d['day']))
        nums = [int(d['day']) for d in sd]
        if nums and nums != list(range(nums[0], nums[0] + len(nums))):
            fails.append('stretch %s: day numbers are not consecutive: %s' % (s, nums))
        for u in sorted({d['unit'] for d in sd}):
            uid = '%s-u%02d-%s' % (course, int(u.split('.')[0]), u.split('.')[1])
            row = next((x for x in units if x['unit_id'] == uid), None)
            n = sum(1 for d in sd if d['unit'] == u)
            if row is None:
                fails.append('unit %s (%s) is not in data/units.csv' % (u, uid))
            elif int(row['days']) != n:
                fails.append('unit %s: data/units.csv says %s days, days.csv has %d' % (u, row['days'], n))
        for d in sd:
            lab = 'day %s' % d['day']
            if d['kind'] not in KINDS:
                fails.append('%s: kind "%s" is not one of %s' % (lab, d['kind'], ', '.join(sorted(KINDS))))
            used = int(d['opens_min'] or 0) + int(d['tool_min'] or 0)
            if used > LESSON_MIN:
                fails.append('%s: opening %s + tool %s minutes is more than the %d minute lesson'
                             % (lab, d['opens_min'], d['tool_min'], LESSON_MIN))
            if d['tool']:
                if d['mark'] not in MARKS:
                    fails.append('%s: tool %s is not marked key or light' % (lab, d['tool']))
                if not (ROOT / 'tools' / d['tool']).is_dir():
                    fails.append('%s: no folder tools/%s' % (lab, d['tool']))
                stated = sum(int(m) for m in re.findall(r'(\d+) min', d['tool_use']))
                if stated != int(d['tool_min'] or 0):
                    fails.append('%s: tool minutes in words add to %d, tool_min says %s' % (lab, stated, d['tool_min']))
            if d['kind'] == 'Check':
                tot = sum(int(m) for m in re.findall(r'\d+', d['check_min']))
                if tot != DAY_MIN:
                    fails.append('%s: check day parts add to %d minutes, not %d' % (lab, tot, DAY_MIN))
                if not any(i['check'] == 'end' and i['day'] == d['day'] for i in items):
                    fails.append('%s: a check day with no end-check items' % lab)
            elif not any(i['check'] == 'exit' and i['day'] == d['day'] for i in items):
                fails.append('%s: no exit question in items.csv' % lab)
        # 5. the error register is shown inside the stretch
        for e in errors:
            if e['stretch'] == s and nums and int(e['day']) not in nums:
                fails.append('error %s: its example day %s is outside stretch %s' % (e['letter'], e['day'], s))
            if e['stretch'] == s and 'memory' in e['source'].lower():
                notes.append('stretch %s error %s rests on memory, not a source' % (s, e['letter']))
        # prose weight, outside the generated blocks
        f = DOCS / course / ('s%02d.md' % int(s))
        if f.exists():
            t = re.sub(r'<!-- gen:.*?<!-- /gen -->', '', f.read_text(encoding='utf-8'), flags=re.S)
            notes.append('stretch %s: %d words of prose outside the generated tables (%s)' % (s, len(t.split()), f.name))

    planned = sorted({int(m[1]) for f in (DOCS / course).glob('s[0-9][0-9].md') for m in [re.match(r's(\d+)', f.name)]})
    missing = [n for n in planned if str(n) not in stretches]
    if missing:
        notes.append('stretches planned in prose but not yet in data: %s' % ', '.join(map(str, missing)))
    return fails, notes, len(items), len(wrongs)


# ------------------------------------------------------------------ generated tables
def cell(t):
    return t.replace('|', '\\|')


def table(head, body):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    out += ['| ' + ' | '.join(cell(c) for c in r) + ' |' for r in body]
    return '\n'.join(out)


def wrong_text(ws):
    out = []
    for w in ws:
        t = w['shown']
        if w['error']:
            t += ' (%s)' % w['error']
        if w['note']:
            t += (': ' if not w['error'] else '. ') + w['note']
        out.append(t)
    return '; '.join(out)


def blocks(course, s):
    items = [i for i in rows(course, 'items') if i['stretch'] == s]
    wrongs = rows(course, 'wrongs')
    W = lambda i: wrong_text([w for w in wrongs if w['item_id'] == i['item_id']])
    b = {}
    b['readiness'] = table(['#', 'Code', 'The item', 'Key', 'Serves unit'],
        [[i['n'], i['code'], i['stem'], i['answer'], i['unit']] for i in items if i['check'] == 'readiness'])
    b['end-check'] = table(['#', 'Practice', 'Part', 'The item', 'Answer', 'Wrong answers (error)'],
        [[i['n'], i['practice'] + (', teacher judged' if i['judged'] == 'teacher' else ''), '(%s)' % i['part'],
          i['stem'], i['answer'], W(i)] for i in items if i['check'] == 'end'])
    b['errors'] = table(['', 'The error', 'What it shows', 'Source', 'Wrong example beside a right one; day', 'If many made it'],
        [[e['letter'], e['error'], e['shows'], e['source'], '%s. Day %s' % (e['example'], e['day']), e['if_many']]
         for e in rows(course, 'errors') if e['stretch'] == s])
    ex = []
    for d in sorted({i['day'] for i in items if i['check'] == 'exit'}, key=int):
        its = [i for i in items if i['check'] == 'exit' and i['day'] == d]
        ex.append('- **E%s.** ' % d + ' '.join(i['stem'] for i in its) + ' Answers: ' + '; '.join(i['answer'] for i in its)
                  + '. Wrong: ' + '; '.join(x for x in (W(i) for i in its) if x) + '.')
    b['exits'] = '\n'.join(ex)
    b['days'] = table(['Day', 'Goal, in student words', 'Kind', 'Opens', 'Who holds it', 'Tool: part, mark, job, minutes', 'By hand', 'Exit'],
        [[d['day'], d['goal'], d['kind'] + (' (%s)' % d['check_min'].replace(';', ',') if d['check_min'] else ''), d['opens'], d['holds'],
          ('%s (%s): %s' % (d['tool'], d['mark'], d['tool_use'])) if d['tool'] else 'None', d['by_hand'],
          'The end check' if d['exit'] == 'END' else d['exit']]
         for d in sorted((d for d in rows(course, 'days') if d['stretch'] == s), key=lambda d: int(d['day']))])
    b['parts'] = table(['Code', 'Part', 'Verb', 'What it is'],
        [[p['code'], '(%s)' % p['part'], p['verb'], p['text']] for p in rows(course, 'parts') if p['stretch'] == s])
    return b


def tables(course):
    changed = 0
    for f in sorted((DOCS / course).glob('*.md')):
        m = re.match(r'[su](\d+)', f.name)
        if not m:
            continue
        raw = io.open(f, encoding='utf-8', newline='').read()
        nl = '\r\n' if '\r\n' in raw else '\n'
        b = blocks(course, str(int(m[1])))
        def sub(mm):
            name = mm.group(1)
            if name not in b:
                raise SystemExit('%s: unknown generated block "%s"' % (f.name, name))
            return '<!-- gen:%s (from data/plans/%s; do not edit here) -->%s%s%s<!-- /gen -->' % (
                name, course, nl, b[name].replace('\n', nl), nl)
        new = re.sub(r'<!-- gen:([a-z-]+)[^>]*-->.*?<!-- /gen -->', sub, raw, flags=re.S)
        if new != raw:
            io.open(f, 'w', encoding='utf-8', newline='').write(new); changed += 1
            print('rewrote', f.relative_to(ROOT))
    print('%d file(s) changed' % changed)


# ------------------------------------------------------------------ reading pack
def pack(course, s):
    out = ['# Reading pack: %s, stretch %s' % (course, s), '',
           'Built by scripts/plan.py on %s. Everything a writer or reader of this stretch needs, and nothing else.' % datetime.date.today(),
           'Read in full first: docs/FOUNDATION.md, docs/courses/UNIT-PLAN.md (the rules), and for a lesson writer',
           'docs/courses/LESSON-DAY.md.', '']
    parts = [p for p in rows(course, 'parts') if p['stretch'] == s]
    items = [i for i in rows(course, 'items') if i['stretch'] == s]
    wanted = sorted({p['code'] for p in parts} | {i['code'] for i in items})
    std = ROOT / 'data' / 'standards' / 'ccss-math-standards.txt'
    out.append('## The standards, in their own words\n')
    if std.exists():
        for l in std.read_text(encoding='utf-8').splitlines():
            if l.split('\t')[0] in wanted:
                out.append('- **%s** %s' % tuple(l.split('\t')[:2]))
    b = blocks(course, s)
    for title, k in [('Parts of each standard this stretch must teach and check', 'parts'), ('Days', 'days'),
                     ('Readiness check', 'readiness'), ('End check', 'end-check'), ('Exit questions', 'exits'),
                     ('Error register', 'errors')]:
        out += ['', '## ' + title, '', b[k]]
    tools = sorted({d['tool'] for d in rows(course, 'days') if d['stretch'] == s and d['tool']})
    asks = DOCS / course / 'TOOL-ASKS.md'
    if tools and asks.exists():
        text = asks.read_text(encoding='utf-8')
        for t in tools:
            name = t.replace('-', ' ').title()
            m = re.search(r'^## %s.*?(?=^## |\Z)' % re.escape(name), text, flags=re.S | re.M)
            out += ['', '## Tool asks: ' + name, '', m.group(0).split('\n', 1)[1].strip() if m else '(no section in TOOL-ASKS.md)',
                    '', 'Spec: tools/%s/spec.md' % t]
    f = DOCS / course / ('s%02d.md' % int(s))
    if f.exists():
        prose = re.sub(r'<!-- gen:.*?<!-- /gen -->', '(table above)', f.read_text(encoding='utf-8'), flags=re.S)
        out += ['', '## The plan\'s prose (%s)' % f.name, '', prose]
    open_d = [d for d in rows_defects() if d['course'] == course and d['status'] == 'open' and ('s%02d' % int(s)) in d['artifact']]
    if open_d:
        out += ['', '## Open defects on this stretch', ''] + ['- %s (%s, %s): %s' % (d['artifact'], d['found_by'], d['date'], d['summary']) for d in open_d]
    print('\n'.join(out))


# ------------------------------------------------------------------ defect ledger
DEF = PLANS / 'defects.csv'
DEF_COLS = ['date', 'course', 'artifact', 'layer', 'found_by', 'kind', 'summary', 'status', 'ref']


def rows_defects():
    with io.open(DEF, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def defect_add(a):
    if len(a) < 6:
        raise SystemExit(__doc__)
    if a[3] not in READERS:
        raise SystemExit('found_by must be one of: ' + ', '.join(sorted(READERS)))
    row = [str(datetime.date.today())] + a[:6] + ['open', a[6] if len(a) > 6 else '']
    with io.open(DEF, 'a', encoding='utf-8', newline='') as f:
        csv.writer(f, lineterminator='\n').writerow(row)
    print('logged:', row)


def defects():
    d = rows_defects()
    print('%d defects logged, %d open' % (len(d), sum(1 for x in d if x['status'] == 'open')))
    tally = {}
    for x in d:
        tally[(x['found_by'], x['layer'])] = tally.get((x['found_by'], x['layer']), 0) + 1
    for (who, layer), n in sorted(tally.items(), key=lambda t: -t[1]):
        print('  %-8s layer %-12s %d' % (who, layer, n))


def main(a):
    if not a:
        raise SystemExit(__doc__)
    cmd, rest = a[0], a[1:]
    if cmd == 'check':
        bad = 0
        for c in (rest[:1] or courses()):
            fails, notes, ni, nw = check(c)
            print('%s: %d items and %d wrong answers checked, %d failure(s)' % (c, ni, nw, len(fails)))
            for x in fails:
                print('  FAIL', x)
            for x in notes:
                print('  note', x)
            bad += len(fails)
        sys.exit(1 if bad else 0)
    elif cmd == 'tables':
        for c in (rest[:1] or courses()):
            tables(c)
    elif cmd == 'pack':
        pack(rest[0], str(int(rest[1])))
    elif cmd == 'defect':
        defect_add(rest)
    elif cmd == 'defects':
        defects()
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
