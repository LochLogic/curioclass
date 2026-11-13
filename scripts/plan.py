"""Course plans as data: gates, generated tables, reading packs, defect ledger.

    python -X utf8 scripts/plan.py check  [course]            gates; exit 1 on any failure
    python -X utf8 scripts/plan.py tables [course]            rewrite the generated blocks in the plan files
    python -X utf8 scripts/plan.py pack   <course> <unit>     print one agent's reading pack
    python -X utf8 scripts/plan.py defect <course> <artifact> <layer> <found_by> <kind> "<summary>" [ref]
    python -X utf8 scripts/plan.py defects                    counts by reader and layer
    python -X utf8 scripts/plan.py reserve <course> <unit>    write the unit's fact triples into its generator

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
LESSON_MIN = 50          # the lesson part of a 60 minute day (scope and sequence: warm-up 5, lesson about 50, exit 5)
DAY_MIN = 60
KINDS = {'Understanding', 'Fluency', 'Application', 'Check', 'Respond'}
MARKS = {'key', 'light'}
LESSON_KINDS = {'example', 'tool', 'fix', 'practice', 'challenge'}   # rows a lesson day adds; all count as taught
CHECKS = {'readiness', 'end', 'exit'} | LESSON_KINDS
READERS = {'script', 'expert', 'cheap', 'sara', 'teacher', 'student', 'cory', 'writer'}


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


def partset(i):
    """The parts one item tests: a cell may name several, "f, g", when one printed item checks two verbs."""
    return {x.strip() for x in i['part'].split(',') if x.strip()}


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


def step_results(i):
    """What a row's student works out: the result of every multiplication and division in its compute cells, and
    its values, as canon() strings (63 / 9 + 48 gives 7 and 55)."""
    out = set()
    for c in split(i['compute']):
        try:
            tree = ast.parse(c.replace(';', ','), mode='eval')
        except SyntaxError:
            continue
        for n in ast.walk(tree):
            if isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Mult, ast.Div)):
                try:
                    out.add(canon(compute(ast.unparse(n))))
                except Exception:
                    pass
    for v in split(i['value']):
        try:
            out.add(canon(parse_value(v)))
        except (ValueError, ZeroDivisionError):
            pass
    return out


def left_to_right(expr):
    """Every running value of an expression of whole numbers and + - * / worked strictly left to right, ignoring
    the order of operations: '18+7*7' gives [18, 25, 175]. None if it has brackets or anything else."""
    toks = re.findall(r'\d+|[-+*/]', expr.replace(' ', ''))
    if not toks or ''.join(toks) != expr.replace(' ', '') or not toks[0].isdigit():
        return None
    acc, out = Fraction(int(toks[0])), [Fraction(int(toks[0]))]
    for op, n in zip(toks[1::2], toks[2::2]):
        n = Fraction(int(n))
        acc = acc + n if op == '+' else acc - n if op == '-' else acc * n if op == '*' else acc / n if n else acc
        out.append(acc)
    return out


GRADE_MULT = {'4': (9999, 9, 99)}   # grade 4: four digits by one digit, or two digits by two digits


def over_limit(expr, course):
    """True when the expression multiplies past what the course's grade multiplies (for a wrong answer's sign)."""
    lim = GRADE_MULT.get(course.rsplit('-', 1)[-1])
    if not lim:
        return False
    try:
        tree = ast.parse(expr.split('|')[0].replace(';', ','), mode='eval')
    except SyntaxError:
        return False
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult):
            try:
                a, b = sorted(abs(compute(ast.unparse(x))) for x in (n.left, n.right))
            except Exception:
                continue
            if a == int(a) and b == int(b) and a % 10 and b % 10:   # multiples of 10 are inside the rule
                if not ((a <= lim[1] and b <= lim[0]) or (a <= lim[2] and b <= lim[2])):
                    return True
            elif a == int(a) and b == int(b) and a > lim[2] and b > lim[2]:
                return True
    return False


def numbers(text):
    """The set of numbers in a stem or example: used for the no-reuse rule."""
    t = re.sub(r'\b(?:MP|E|day|Day|unit|section|lesson|item|items)\.? ?\d+', ' ', text)
    t = re.sub(r'\b\d+ min\b', ' ', t)   # minutes in a day row are time, not taught numbers
    t = re.sub(r'\((?:a|b|c|d|e|f)\)', ' ', t)
    # a fraction is one number (unit 3: 2/3 is not the numbers 2 and 3); a mixed number stays one too
    return frozenset(re.findall(r'\d+(?: \d+/\d+|/\d+)?(?:,\d{3})*', t))



# ------------------------------------------------------------------ reserved numbers
RESERVED = {('math-4', '11'): 'site/assets/gen/measure-shapes.js'}   # (course, unit): the generator that serves it


def canon(v):
    """One number as the generator writes it: a whole number, or a fraction in lowest terms ("27/2")."""
    v = Fraction(v)
    return str(v.numerator) if v.denominator == 1 else '%d/%d' % (v.numerator, v.denominator)


def facts(i, stem=True):
    """The fact triples a row teaches or checks, as sorted tuples of canon() strings, matched in any order:
    (side, side, area) for an area or a side from an area, (side, side, perimeter) for a perimeter or a side from
    a perimeter. Read from the compute cell, plus both measures of any rectangle the stem names by two numbers."""
    out = set()
    # a fraction rule ("2/3 = (2 x 4)/(3 x 4) = 8/12") multiplies top and bottom by one number: its products are
    # not facts a row teaches (unit 3 reads), so its Mult and Div terms add nothing
    rule = bool(re.search(r'\d+/\d+\s*=\s*(?:\(|\d+/\d+)', i.get('answer', '')))

    def add(*xs):
        if rule:
            return
        if all(isinstance(x, Fraction) and x > 0 for x in xs):
            out.add(tuple(sorted(canon(x) for x in xs)))

    def is_add(n):
        return isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add)

    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant):
            return Fraction(n.value) if isinstance(n.value, int) and not isinstance(n.value, bool) else None
        if isinstance(n, ast.Call) and getattr(n.func, 'id', '') == 'F' and len(n.args) == 2:
            a, b = ev(n.args[0]), ev(n.args[1])
            return a / b if a is not None and b else None
        if isinstance(n, ast.BinOp):
            a, b = ev(n.left), ev(n.right)
            if a is None or b is None:
                return None
            if isinstance(n.op, ast.Add):
                r = a + b
                if is_add(n.left) and ast.dump(n.left) == ast.dump(n.right):   # (l + w) + (l + w)
                    add(ev(n.left.left), ev(n.left.right), r)
                return r
            if isinstance(n.op, ast.Sub):
                return a - b
            if isinstance(n.op, ast.Mult):
                r = a * b
                dbl = n.right if a == 2 else n.left if b == 2 else None
                if dbl is not None and is_add(dbl):
                    add(ev(dbl.left), ev(dbl.right), r)          # 2 × (l + w)
                else:
                    add(a, b, r)
                return r
            if isinstance(n.op, ast.Div) and b:
                r = a / b
                L = n.left
                if (b == 2 and isinstance(L, ast.BinOp) and isinstance(L.op, ast.Sub) and isinstance(L.right, ast.BinOp)
                        and isinstance(L.right.op, ast.Mult)):   # (P - 2 × l) ÷ 2
                    m = L.right
                    add(ev(L.left), ev(m.right) if ev(m.left) == 2 else ev(m.left), r)
                else:
                    add(a, b, r)
                return r
            return None
        for c in ast.iter_child_nodes(n):
            ev(c)
        return None

    for c in split(i['compute']):
        try:
            ev(ast.parse(c.replace(';', ','), mode='eval'))
        except SyntaxError:
            pass
    ns = [parse_value(x) for x in numbers(i['stem'])] if stem else []
    if len(ns) == 2:
        add(ns[0], ns[1], ns[0] * ns[1])
        add(ns[0], ns[1], 2 * (ns[0] + ns[1]))
    return out


def reserved_js(items, st):
    """Every fact triple the unit teaches or checks, as a JS array literal, sorted for a stable diff."""
    ts = sorted({t for i in items if i['stretch'] == st and i['check'] in CHECKS for t in facts(i)})
    return '[' + ', '.join('[' + ', '.join("'%s'" % n for n in t) + ']' for t in ts) + ']'


def reserve(course, st):
    if (course, st) not in RESERVED:   # a unit with no generator: the no-reuse gates in check() guard it
        print('%s unit %s: no generator to write; plan.py check guards its reserved numbers' % (course, st))
        return
    js = ROOT / RESERVED[(course, st)]
    t = js.read_text(encoding='utf-8')
    new = re.sub(r'const RESERVED_S%s = .*?;' % st, lambda m: 'const RESERVED_S%s = %s;' % (st, reserved_js(rows(course, 'items'), st)), t, count=1, flags=re.S)
    js.write_text(new, encoding='utf-8')
    print('%s: RESERVED_S%s %s' % (js.relative_to(ROOT), st, 'rewritten' if new != t else 'already current'))

# ------------------------------------------------------------------ the gates
def one_ungrouping(a, b):
    """For a - b with exactly one place that must ungroup (and no zero to cross): the answers of error F (the smaller
    digit from the larger in each place) and of error G (the small 1 written, the next place left as it was).
    None for any other difference."""
    da, db = [int(c) for c in reversed(str(a))], [int(c) for c in reversed(str(b))]
    db += [0] * (len(da) - len(db))
    if len(db) > len(da) or a <= b:
        return None
    need = [j for j in range(len(da)) if da[j] < db[j]]
    if len(need) != 1 or need[0] + 1 >= len(da) or da[need[0] + 1] == 0 or da[need[0] + 1] - 1 < db[need[0] + 1]:
        return None
    f = sum(abs(x - y) * 10 ** j for j, (x, y) in enumerate(zip(da, db)))
    return f, a - b + 10 ** (need[0] + 1)


def trade_places(m):
    """The places (ones 0) that carry in a sum, or that must ungroup in a difference, from a match of a+b or a-b."""
    a, b = int(m[1]), int(m[3])
    da, db = [int(c) for c in reversed(str(a))], [int(c) for c in reversed(str(b))]
    n = max(len(da), len(db))
    da += [0] * (n - len(da)); db += [0] * (n - len(db))
    out, c = set(), 0
    for j in range(n):
        if m[2] == '+':
            c = (da[j] + db[j] + c) // 10
            if c:
                out.add(j)
        else:
            t = da[j] - c
            c = 1 if t < db[j] else 0
            if c:
                out.add(j)
    return out


def first_days():
    """Each grade 4 standard's first day in the scope and sequence (docs/courses/math-4-spine.md)."""
    out, p = {}, DOCS / 'math-4-spine.md'
    if not p.exists():
        return out
    for ln in p.read_text(encoding='utf-8').splitlines():
        m = re.match(r'\|\s*\d+\s*\|[^|]*\|[^|]*\|\s*(\d+) to \d+\s*\|([^|]*)\|', ln)
        if m:
            for code in re.findall(r'4\.[A-Z]+\.[A-Z]\.\d+', m[2]):
                out[code] = min(out.get(code, 999), int(m[1]))
    return out


SPEECH = re.compile(r'\b(?:says|said|wrote|writes|asks|asked|thinks|claims|answers|answered|reads)[,:]?\s*$', re.I)
DIRECTION = re.compile(r'^\s*No (?:drawing|line(?: given)?|strips?|grid)\b')


def stray_quote(stem):
    """A stem that wraps its student text in quote marks after (or before) plan words: the marks and the plan words
    print on the student page (unit 3 reads, days 23 and 24). A whole-stem quote is stripped by lesson.py, and a
    quote after "says" or inside a sentence ("Say it with "factor"") is a word or a voice, so both pass."""
    s = stem.strip()
    if s.startswith('"') and s.endswith('"') and s.count('"') == 2:
        return None
    for m in re.finditer(r'"([^"]*)"', s):
        pre = s[:m.start()]
        if not SPEECH.search(pre) and (not pre.strip() or re.search(r'[.?!:]\s*$', pre) and not pre.rstrip().endswith(':')):
            return m[1]
    return None


def fractions_of(i):
    """The fractions a row names: in its stem, its answer and the F(a;b) terms of its compute cell."""
    t = i['stem'] + ' ' + i.get('answer', '')
    out = {(int(a), int(b)) for a, b in re.findall(r'(?<![\d/])(\d+)/(\d+)(?![\d/])', t) if int(b)}
    out |= {(int(a), int(b)) for a, b in re.findall(r'F\((\d+);(\d+)\)', i.get('compute', '')) if int(b)}
    return out


def equal_pairs(fr):
    """Pairs of different fractions with the same value, each as a sorted pair of 'a/b' strings."""
    fr = sorted(fr)
    return {tuple(sorted(('%d/%d' % x, '%d/%d' % y))) for k, x in enumerate(fr) for y in fr[k + 1:]
            if x != y and Fraction(*x) == Fraction(*y)}


def register_letters(course, st):
    """The letters each section opener of a unit names in its error table, as {section folder: set of letters}."""
    out = {}
    for op in sorted((ROOT / 'courses' / course).glob('u%02d-*/opener.md' % int(st))):
        t = op.read_text(encoding='utf-8')
        m = re.search(r'## The errors to expect[^\n]*\n(.*?)(?=\n## |\Z)', t, re.S)
        if m:
            out[op.parent.name] = set(re.findall(r'^\|\s*([A-Z])\s*\|', m[1], re.M))
    return out


def check(course):
    global FIRST_DAY
    FIRST_DAY = first_days() if course == 'math-4' else {}
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
    wordrules = [(w['pattern'], w['use'], w['reason']) for w in rows(course, 'words')]   # settled wording, per course
    letters = {(e['stretch'], e['letter']) for e in errors}
    stretches = sorted({d['stretch'] for d in days} | {i['stretch'] for i in items}, key=int)

    # 1. keys: every key-marked item is recomputed; teacher-judged items too where a value is given
    for i in items:
        if codes and i['code'] not in codes:
            fails.append('%s: standard code %s is not in the standards file' % (i['item_id'], i['code']))
        if i['check'] not in CHECKS:
            fails.append('%s: check "%s" is not one of %s' % (i['item_id'], i['check'], ', '.join(sorted(CHECKS))))
        if i['judged'] not in ('key', 'teacher'):
            fails.append('%s: judged must be key or teacher' % i['item_id'])
        # lesson-day columns (docs/courses/LESSON-DAY.md): an exit names its path; an adapted item carries its credit
        # an exit's path is tool or paper; a practice row written on the board when the sheet is not printed is board
        pth = i.get('path', '')
        # spare: a lesson row kept in data for a later day to cite, printed on no page
        if not (pth == '' or (pth in ('tool', 'paper') and i['check'] == 'exit') or (pth == 'board' and i['check'] == 'practice')
                or (pth == 'spare' and i['check'] in LESSON_KINDS)):
            fails.append('%s: path must be tool or paper on an exit, board on a practice row, or spare on a lesson row' % i['item_id'])
        # a teacher-judged row carries its look-fors (steps) and its samples (meets | partly | not), so the key holds them
        if i['judged'] == 'teacher' and not i.get('steps', '').strip():
            fails.append('%s: judged by the teacher but has no look-fors in its steps cell' % i['item_id'])
        if i['judged'] == 'teacher' and not i.get('samples', '').strip():
            fails.append('%s: judged by the teacher but has no samples cell (meets | partly | not)' % i['item_id'])
        # plan words printed to students (unit 3 reads, days 23 and 24): a condition for the page ("No drawing.",
        # "No line given.") belongs in the teacher page or a column, and student text is not wrapped in quotes
        if DIRECTION.match(i['stem']):
            fails.append('%s: stem starts with a direction for the page ("%s"); put it in the teacher page and drop it '
                         'from the stem' % (i['item_id'], DIRECTION.match(i['stem'])[0].strip()))
        q = stray_quote(i['stem'])
        if q is not None:
            fails.append('%s: stem wraps student text in quote marks beside other words ("%s..."); the marks print'
                         % (i['item_id'], q[:30]))
        for pat, use, why in wordrules:
            if re.search(pat, i['stem'], re.I):
                fails.append('%s: stem breaks a settled word rule (%s): use %s' % (i['item_id'], why, use))
        src = i.get('source', '')
        if src and (re.search(r'\bnc\b|noncommercial|sharealike|-sa\b|\bnd\b|-nd\b|noderivatives', src, re.I)
                    or 'http' not in src or not re.search(r'cc by|cc0|public domain', src, re.I)):
            fails.append('%s: source must be CC BY, CC0 or public domain, with a licence link' % i['item_id'])
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
        it = next((i for i in items if i['item_id'] == w['item_id']), None)
        st = it['stretch'] if it else None
        if w['error'] and (st, w['error']) not in letters:
            fails.append(lab + ': error letter %s is not in the error register' % w['error'])
        # a "left to right" error's wrong answer is what the item's expression gives worked strictly left to right
        # (or a first step of that); expert, day 88: Ravi's 175 was not left to right at all
        reg = next((e for e in errors if (e['stretch'], e['letter']) == (st, w['error'])), None)
        if it and reg and 'left to right' in reg['error'].lower() and w['value'].strip() and it['compute'].strip():
            want = left_to_right(split(it['compute'])[0])
            if want and parse_value(split(w['value'])[0]) not in want:
                fails.append(lab + ': error %s is left to right, but %s worked left to right gives %s'
                             % (w['error'], split(it['compute'])[0], ', '.join(str(x) for x in want)))
        # a wrong answer that needs multiplying beyond the grade's limit is one a child cannot reach (expert, day 87)
        if w['compute'].strip() and over_limit(w['compute'], course):
            notes.append(lab + ': its compute multiplies beyond the grade limit; read it (day 87 read)')
    # an exit whose wrong answers are sentences asks for a sentence, or the sign cannot show (expert, day 85)
    for i in items:
        if i['check'] == 'exit':
            ws = [w['shown'] for w in wrongs if w['item_id'] == i['item_id']]
            if any(re.search(r'[A-Za-z]+ (?:\w+ )?(?:read|has|have|is|picked|weighs) \d+ times as', x) for x in ws) and \
                    not re.search(r'sentence|say|finish', i['stem'], re.I):
                fails.append('%s: a wrong answer is a sentence, but the stem never asks for one' % i['item_id'])

    for s in stretches:
        sp = [p for p in parts if p['stretch'] == s]
        end = [i for i in items if i['stretch'] == s and i['check'] == 'end']
        # 2. every part of every standard has a unit assessment item
        for p in sp:
            if not any(i['code'] == p['code'] and p['part'] in partset(i) for i in end):
                fails.append('unit %s: %s part (%s) "%s" has no unit assessment item' % (s, p['code'], p['part'], p['text']))
        for i in end:
            for pt in sorted(partset(i)):
                if sp and not any(i['code'] == p['code'] and pt == p['part'] for p in sp):
                    fails.append('%s: part (%s) of %s is not listed in parts.csv' % (i['item_id'], pt, i['code']))
        if codes:
            for p in sp:
                if p['code'] not in codes:
                    fails.append('parts.csv: %s is not in the standards file' % p['code'])
        # 3. no unit assessment item or exit question reuses the numbers of a taught example or of another item
        taught = [('error %s example' % e['letter'], numbers(e['example'])) for e in errors if e['stretch'] == s]
        taught += [('day %s' % d['day'], numbers(d['opens'] + ' ' + d['by_hand'])) for d in days if d['stretch'] == s]
        # lesson-day rows (docs/courses/LESSON-DAY.md, rule 3): worked examples, tool notes, fixes, practice
        taught += [(i['item_id'], numbers(i['stem'])) for i in items if i['stretch'] == s and i['check'] in LESSON_KINDS]
        asked = [(i['item_id'], numbers(i['stem'])) for i in items if i['stretch'] == s and i['check'] in ('end', 'exit')]
        # a fraction item is held to each taught example on a day, one clause at a time (unit 3: a day row names a
        # dozen fractions, and rule 4 forbids reusing a taught pair, not two fractions met in different examples)
        clauses = [('day %s' % d['day'], numbers(c)) for d in days if d['stretch'] == s
                   for c in re.split(r'[;:]\s|\.\s', d['opens'] + '; ' + d['by_hand'])]
        taught_f = [t for t in taught if not t[0].startswith('day ')] + clauses
        for k, (a, na) in enumerate(asked):
            if len(na) < 2:
                continue
            for b, nb in (taught_f if any('/' in x for x in na) else taught):
                if len(nb) >= 2 and na <= nb:
                    fails.append('%s reuses the numbers of %s: %s' % (a, b, ', '.join(sorted(na))))
            for b, nb in asked[k + 1:]:
                if na == nb:
                    fails.append('%s and %s use the same numbers: %s' % (a, b, ', '.join(sorted(na))))
        # 3a. a fact turned round: a check or exit item that shares a taught row's multiplication or division fact
        # (a, b, a x b from the compute cells, any order) and prints that row's answer as a given number fails, so a
        # taught answer reused as a factor is caught (expert, day 88: 63 = 7 x 9 was day 87's 63 / 9 = 7; day 85:
        # 27 / 9 = 3 against 27 / 3 = 9). Sharing a fact alone is allowed: unit 10's one-digit facts are all used
        tf = {}
        for i in items:
            if i['stretch'] == s and i['check'] in LESSON_KINDS:
                for t in facts(i, stem=False):
                    tf.setdefault(t, []).append(i)
        for i in items:
            if i['stretch'] == s and i['check'] in ('end', 'exit'):
                given = {canon(parse_value(x)) for x in numbers(i['stem'])}
                for t in sorted(facts(i, stem=False)):
                    for x in tf.get(t, []):
                        if i['check'] == 'exit' and int(x['day']) > int(i['day']):
                            continue   # not taught yet when the exit is asked
                        ans = step_results(x)
                        own = {canon(parse_value(y)) for y in numbers(x['stem'])}
                        turned = (ans & given & set(t)) - own
                        if turned:
                            fails.append('%s gives %s, the answer of the taught row %s on the same fact %s'
                                         % (i['item_id'], ', '.join(sorted(turned)), x['item_id'], ' '.join(t)))
        # 3a for fractions (day 16 read): a check or exit stem that prints both fractions of an equality a taught row
        # names (a/b = c/d from its stem, answer or F() terms, either order, by the exit's day) gives the answer away
        tp = {}
        for x in items:
            if x['stretch'] == s and x['check'] in LESSON_KINDS:
                for pr in equal_pairs(fractions_of(x)):
                    tp.setdefault(pr, []).append(x)
        for i in items:
            if i['stretch'] == s and i['check'] in ('end', 'exit'):
                # within one part: (b)'s 1/3 and (c)'s 2/6 are two questions, not a pair given away
                shown = [{'%s/%s' % (a, b) for a, b in re.findall(r'(?<![\d/])(\d+)/(\d+)(?![\d/])', pt)}
                         for pt in re.split(r'\((?:[a-h]|i{1,3}|iv)\)', i['stem'])]
                for pr in sorted(tp):
                    # by the exit's own day; before an end item's day (that day's rows come after the assessment)
                    xs = [x for x in tp[pr] if int(x['day']) < int(i['day']) + (i['check'] == 'exit')]
                    if xs and any(set(pr) <= sh for sh in shown):
                        fails.append('%s prints %s and %s, an equality taught in %s'
                                     % (i['item_id'], pr[0], pr[1], xs[0]['item_id']))
        # taught against taught, across days: allowed for practice, but counted so a writer sees it
        cross = sorted(t for t, xs in tf.items() if len({x['day'] for x in xs}) > 1)
        if cross:
            notes.append('unit %s: %d taught facts recur on more than one day (allowed for practice), e.g. %s'
                         % (s, len(cross), '; '.join(' '.join(t) for t in cross[:4])))
        # an exit whose answer is a taught answer on the same part of its own day can be copied (lesson-day read, day 85)
        for i in items:
            # a comparison computes to True: matching truth values say nothing (day 17 read)
            if i['stretch'] == s and i['check'] == 'exit' and i['value'].strip() and \
                    not all(v in ('True', 'False') for v in split(i['value'])):
                same = [x['item_id'] for x in items if x['day'] == i['day'] and x['check'] in ('example', 'fix')
                        and partset(x) & partset(i) and split(x['value'])[:1] == split(i['value'])[:1]]
                if same:
                    notes.append('%s: its answer %s is the answer of %s on the same part' % (i['item_id'], i['value'], same[0]))
        # 3b. no two rows of a unit share a stem, and no two challenges share their numbers under new ids
        sr = [i for i in items if i['stretch'] == s]
        for k, a in enumerate(sr):
            for b in sr[k + 1:]:
                if a['stem'].strip() == b['stem'].strip():
                    fails.append('%s and %s have the same stem' % (a['item_id'], b['item_id']))
                elif (a['check'] == b['check'] == 'challenge'   # one fraction is enough to compare (day 16 read)
                      and (len(numbers(a['stem'])) >= 2 or any('/' in x for x in numbers(a['stem'])))
                      and numbers(a['stem']) == numbers(b['stem'])):
                    fails.append('%s and %s are challenges with the same numbers' % (a['item_id'], b['item_id']))
        # a comparing end item's wrong rows cover each letter its section's register names (day 24 read, note)
        cmp_end = [i for i in end if re.search(r'[<>]', i['compute'])]
        if cmp_end:
            have = {w['error'] for w in wrongs if any(w['item_id'] == i['item_id'] for i in cmp_end)}
            for sec, ls in register_letters(course, s).items():
                sx = [x for x in items if x['check'] == 'exit' and x['stretch'] == s and any(
                    d['day'] == x['day'] and d['unit'] == '%s.%s' % (int(sec[1:3]), sec.split('-')[1]) for d in days)]
                # a comparing section: every exit of it compares
                if sx and all(re.search(r'[<>]', x['compute']) for x in sx) and ls - have:
                    notes.append('unit %s: %s register names %s, but no comparing end item (%s) has a wrong row for it'
                                 % (s, sec, ', '.join(sorted(ls - have)), ', '.join(i['item_id'] for i in cmp_end)))
        # one shown value under two letters on a check item sorts a student into two groups (day 24 read; a note:
        # a digit can be right under two errors in other units, so the reader judges it)
        for i in end + [x for x in items if x['stretch'] == s and x['check'] == 'exit']:
            seen = {}
            for w in wrongs:
                if w['item_id'] == i['item_id'] and w['error'] and not re.search(
                        r'\([a-h]\)|\((?:i|ii|iii|iv)\)|\b(?:first|second|third|fourth|top|bottom)\b', w['shown'], re.I):
                    for v in re.split(r',\s+|\s+or\s+', w['shown'].strip()):
                        if re.fullmatch(r'[\d/,. ]+', v):
                            seen.setdefault(v, set()).add(w['error'])
            two = sorted(v for v, ls in seen.items() if len(ls) > 1)
            if two:
                notes.append('%s: wrong answer %s sits under two letters (%s); say which blank or part each is'
                             % (i['item_id'], ', '.join(two), ', '.join(sorted(seen[two[0]]))))
        # 4. days
        sd = sorted((d for d in days if d['stretch'] == s), key=lambda d: int(d['day']))
        nums = [int(d['day']) for d in sd]
        if nums and nums != list(range(nums[0], nums[0] + len(nums))):
            fails.append('unit %s: day numbers are not consecutive: %s' % (s, nums))
        for u in sorted({d['unit'] for d in sd}):
            # a teaching section is "9.2"; a cumulative check or its respond day is named as in units.csv ("check-2")
            uid = '%s-u%02d-%s' % (course, int(u.split('.')[0]), u.split('.')[1]) if '.' in u else '%s-%s' % (course, u)
            row = next((x for x in units if x['unit_id'] == uid), None)
            n = sum(1 for d in sd if d['unit'] == u)
            if row is None:
                fails.append('section %s (%s) is not in data/units.csv' % (u, uid))
            elif int(row['days']) != n:
                fails.append('section %s: data/units.csv says %s days, days.csv has %d' % (u, row['days'], n))
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
                # the tool's problems are rows, so the no-reuse gates see them (expert, day 86)
                if int(d['tool_min'] or 0) and not any(i['day'] == d['day'] and (i['check'] == 'tool' or i.get('path') == 'tool')
                                                       for i in items):
                    fails.append('%s: names the tool %s but has no tool rows in items.csv' % (lab, d['tool']))
                stated = sum(int(m) for m in re.findall(r'(\d+) min', d['tool_use']))
                if stated != int(d['tool_min'] or 0):
                    fails.append('%s: tool minutes in words add to %d, tool_min says %s' % (lab, stated, d['tool_min']))
            if d['kind'] == 'Check':
                tot = sum(int(re.findall(r'\d+', re.sub(r'\(.*?\)', '', s))[-1]) for s in d['check_min'].split(';') if re.findall(r'\d+', re.sub(r'\(.*?\)', '', s)))   # the last number of each part, notes in brackets aside
                if tot != DAY_MIN:
                    fails.append('%s: assessment day parts add to %d minutes, not %d' % (lab, tot, DAY_MIN))
                if not any(i['check'] == 'end' and i['day'] == d['day'] for i in items):
                    fails.append('%s: an assessment day with no unit assessment items' % lab)
            elif not any(i['check'] == 'exit' and i['day'] == d['day'] for i in items):
                fails.append('%s: no exit question in items.csv' % lab)
        # 3c. a reserved number (a unit assessment stem's number) made by a product in a taught row's answer or in the
        # day's prose; the compute-only gate cannot see it (expert, day 4: 4 x 20 = 80 taught, 80 an end number)
        resv = {int(x) for i in end for x in numbers(i['stem']) if x.isdigit() and int(x) >= 12}
        prod = re.compile(r'\b(\d+) [×x] (\d+)\b')
        srcs = [(i['item_id'], i['answer']) for i in items if i['stretch'] == s and i['check'] in LESSON_KINDS]
        sdays = {d['day'] for d in days if d['stretch'] == s and d['kind'] != 'Check'}
        for f in sorted((ROOT / 'courses' / course).glob('u*/d[0-9][0-9][0-9].md')):
            m = re.search(r'^day: (\d+)', f.read_text(encoding='utf-8'), re.M)
            if m and m[1] in sdays:
                srcs.append((f.name, f.read_text(encoding='utf-8')))
        for who, txt in srcs:
            hit = sorted({int(a) * int(b) for a, b in prod.findall(txt)} & resv)
            if hit:
                notes.append('unit %s: %s shows a product equal to reserved %s; rule on it (day 4 read)'
                             % (s, who, ', '.join(map(str, hit))))
        # 3d. every registered error can be shown by an exit or unit assessment wrong answer (expert, day 6: error G)
        checked = {w['error'] for w in wrongs for i in items if i['item_id'] == w['item_id'] and i['stretch'] == s
                   and i['check'] in ('exit', 'end')}
        for e in errors:
            if e['stretch'] == s and e['letter'] not in checked:
                notes.append('unit %s: error %s has no wrong-answer row on any exit or unit assessment item (day 6 read)'
                             % (s, e['letter']))
        # 3e. a difference with one ungrouping must tell the smaller-from-larger error from the small-1-only error:
        # they give the same answer when the digits of the ungrouped place are 5 apart (s09 expert, day 74), and a
        # row past the day both are taught keys both (unit 9 reads, 2026-11-12)
        se = {e['letter']: e for e in errors if e['stretch'] == s}
        fl = next((L for L, e in se.items() if 'smaller digit from the larger' in e['error']), None)
        gl = next((L for L, e in se.items() if 'small 1' in e['error'] and 'leaves' in e['error']), None)
        if fl and gl:
            both = max(int(se[fl]['day']), int(se[gl]['day']))
            for i in items:
                said = {x.replace(',', '') for x in numbers(i['stem'])}
                m = next((mm for c in (split(i['compute']) if i['compute'] else [])
                          for mm in [re.fullmatch(r'(\d+)-(\d+)', c)] if mm and {mm[1], mm[2]} <= said), None)
                if i['stretch'] != s or not m:
                    continue
                fg = one_ungrouping(int(m[1]), int(m[2]))
                if not fg:
                    continue
                if fg[0] == fg[1]:
                    fails.append('%s: %s gives %d both ways (smaller digit from the larger, error %s; the small 1 '
                                 'only, error %s): change a digit of the ungrouped place' % (i['item_id'], i['compute'],
                                                                                         fg[0], fl, gl))
                keyed = {w['error'] for w in wrongs if w['item_id'] == i['item_id']}
                if int(i['day']) >= both and len(keyed & {fl, gl}) == 1:
                    fails.append('%s: one ungrouping, past day %d, but its wrong answers key only error %s; key %s (%d) '
                                 'too' % (i['item_id'], both, ''.join(keyed & {fl, gl}),
                                          gl if fl in keyed else fl, fg[1] if fl in keyed else fg[0]))
        # 3f. notes from the unit 9 reads: an exit or fix that rehearses a worked example of its own day
        ex_rows = [x for x in items if x['stretch'] == s and x['check'] == 'example']
        for i in items:
            if i['stretch'] != s or i['check'] not in ('exit', 'fix') or not i['compute']:
                continue
            ops = re.fullmatch(r'(\d{3,})([+-])(\d{3,})', split(i['compute'])[0])
            for x in ex_rows:
                xo = re.fullmatch(r'(\d{3,})([+-])(\d{3,})', split(x['compute'])[0]) if x['compute'] else None
                if x['day'] != i['day'] or not (ops and xo) or ops[2] != xo[2]:
                    continue
                if i['check'] == 'fix' and {ops[1], ops[3]} == {xo[1], xo[3]}:
                    notes.append('%s: a fix on the numbers of the worked example %s; students copy, not find (day 73 read)'
                                 % (i['item_id'], x['item_id']))
                if i['check'] == 'exit' and trade_places(ops) == trade_places(xo):
                    notes.append('%s: carries or ungroupings in the same places as the worked example %s (day 72 read)'
                                 % (i['item_id'], x['item_id']))
        # 3g. a row coded to a standard the scope and sequence first teaches on a later day (day 73 read: 4 x 600 on day 73)
        for i in items:
            fd = FIRST_DAY.get(i['code'])
            if i['stretch'] == s and fd and i['day'].isdigit() and int(i['day']) < fd:
                notes.append('%s: coded %s, which the scope and sequence first teaches on day %d' % (i['item_id'], i['code'], fd))
        # 5. the error register is shown inside the unit
        for e in errors:
            if e['stretch'] == s and nums and int(e['day']) not in nums:
                fails.append('error %s: its example day %s is outside unit %s' % (e['letter'], e['day'], s))
            if e['stretch'] == s and 'memory' in e['source'].lower():
                notes.append('unit %s error %s rests on memory, not a source' % (s, e['letter']))
        # prose weight, outside the generated blocks
        f = DOCS / course / ('s%02d.md' % int(s))
        if f.exists():
            t = re.sub(r'<!-- gen:.*?<!-- /gen -->', '', f.read_text(encoding='utf-8'), flags=re.S)
            notes.append('unit %s: %d words of prose outside the generated tables (%s)' % (s, len(t.split()), f.name))

    planned = sorted({int(m[1]) for f in (DOCS / course).glob('s[0-9][0-9].md') for m in [re.match(r's(\d+)', f.name)]})
    missing = [n for n in planned if str(n) not in stretches]
    if missing:
        notes.append('units planned in prose but not yet in data: %s' % ', '.join(map(str, missing)))
    # 9. a generator that serves a unit refuses the numbers the unit teaches or checks; its list must be current
    for (c, st), js in RESERVED.items():
        if c == course and (ROOT / js).exists():
            have = re.search(r'const RESERVED_S%s = (.*?);' % st, (ROOT / js).read_text(encoding='utf-8'), re.S)
            if not have or have.group(1) != reserved_js(items, st):
                fails.append('%s: RESERVED_S%s is out of date; run plan.py reserve %s %s' % (js, st, c, st))
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


def blocks(course, s, unit=None):
    """The generated tables of one unit; a section plan (uNN-N.md) gets its own section's days, exits and parts."""
    U = lambda r: unit is None or r.get('unit') == unit
    items = [i for i in rows(course, 'items') if i['stretch'] == s and (i['check'] != 'exit' or U(i))]
    wrongs = rows(course, 'wrongs')
    W = lambda i: wrong_text([w for w in wrongs if w['item_id'] == i['item_id']])
    b = {}
    b['readiness'] = table(['#', 'Code', 'The item', 'Key', 'Serves section'],
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
          'The end-of-unit assessment' if d['exit'] == 'END' else d['exit']]
         for d in sorted((d for d in rows(course, 'days') if d['stretch'] == s and U(d)), key=lambda d: int(d['day']))])
    b['parts'] = table(['Code', 'Part', 'Verb', 'What it is'],
        [[p['code'], '(%s)' % p['part'], p['verb'], p['text']] for p in rows(course, 'parts') if p['stretch'] == s and U(p)])
    return b


def tables(course):
    changed = 0
    for f in sorted((DOCS / course).glob('*.md')):
        m = re.match(r'([su])(\d+)(?:-(\d+))?', f.name)
        if not m:
            continue
        raw = io.open(f, encoding='utf-8', newline='').read()
        nl = '\r\n' if '\r\n' in raw else '\n'
        b = blocks(course, str(int(m[2])), '%d.%s' % (int(m[2]), m[3]) if m[1] == 'u' and m[3] else None)
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
    out = ['# Reading pack: %s, unit %s' % (course, s), '',
           'Built by scripts/plan.py on %s. Everything a writer or reader of this unit needs, and nothing else.' % datetime.date.today(),
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
    for title, k in [('Parts of each standard this unit must teach and check', 'parts'), ('Days', 'days'),
                     ('Readiness check', 'readiness'), ('End-of-unit assessment', 'end-check'), ('Exit questions', 'exits'),
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
    for f in [DOCS / course / ('s%02d.md' % int(s))] + sorted((DOCS / course).glob('u%02d-*.md' % int(s))):
        if f.exists():   # the unit plan, then each section plan: a day writer needs the section's prose too
            prose = re.sub(r'<!-- gen:.*?<!-- /gen -->', '(table above)', f.read_text(encoding='utf-8'), flags=re.S)
            out += ['', '## The plan\'s prose (%s)' % f.name, '', prose]
    open_d = [d for d in rows_defects() if d['course'] == course and d['status'] == 'open' and ('s%02d' % int(s)) in d['artifact']]
    if open_d:
        out += ['', '## Open defects on this unit', ''] + ['- %s (%s, %s): %s' % (d['artifact'], d['found_by'], d['date'], d['summary']) for d in open_d]
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
    elif cmd == 'reserve':
        reserve(rest[0], str(int(rest[1])))
    elif cmd == 'defects':
        defects()
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
