"""The curriculum index and its five reports (consolidation 4.F).

    python -X utf8 scripts/index.py                      build data/index.db (git-ignored, seconds)
    python -X utf8 scripts/index.py --csv DIR            build, then dump nodes.csv and edges.csv into DIR
    python -X utf8 scripts/index.py --resolve | --orphans | --layout | --status | --drift | --reports
    python -X utf8 scripts/index.py <report flag> --baseline     rewrite that report's known misses
    python -X utf8 scripts/index.py --self-test

The index reads curriculum sources only: data/plans/course-list.csv, the standards files (through unit_skeleton.py),
data/progressions/<subject>.csv, data/plans/frames.csv, each course's plan CSVs and ledger (data/plans/<course>/),
day and piece frontmatter under courses/<course>/ (`leans_on:`, `version:`), `[[...]]` item links, and the written
plans under docs/courses/<course>/. It never reads a tool catalog file (modules, sequence, coverage, concepts).

Node key: type, course and local id (`item:english-language-arts-grade-1:s01-X2`, `day:math-grade-3:d042`,
`unit:algebra-i:3`, `section:algebra-i:3.2`, `piece:math-grade-3:u02-1/opener.md`, `code:3.OA.A.1`,
`prog:science:sk-push-pull`, `file:<path>`). The type column is free text, so step 5 adds `tool` nodes with no change.
Edges are hard (they must resolve) or soft (`mentions`: "day N" in a course's own plans, days and pieces, bare item ids in prose;
shown by uses.py, never failing).

Reports (one flag each; each starts from the known misses in data/index-baseline.csv, so a new miss fails from day one
and the old ones are worked off by course; a miss that is gone is reported once and dropped with --baseline):
- resolve: every leans_on path, CSV id and `[[...]]` link resolves ("when it exists: <path>" is the one allowed
  unresolved form).
- orphans: day files with no days.csv row, pieces no day leans on, days.csv rows with no frame unit.
- layout: every tracked file has a row in data/homes.csv, nothing generated-and-ignored is tracked, and nothing
  stray sits in a course home (scripts/homes.py check).
- status: one answer per object. A plan's own file wins; a flow-status.csv row that contradicts the file fails; a
  row that only restates the file is counted (flow-status keeps only what no file shows).
- drift: a stored `<!-- skel -->` block in a written plan, and the two allowed in-file copies of a unit plan (the
  header's "**Days A to B**" and the "Day list (from days.csv, do not edit)" kinds) against days.csv.

Course folders come from course-list.csv; the math-4 pilot is skipped by name and the subject folders under
docs/courses (arts, health and the rest) are known, not courses.
"""
import csv
import io
import os
import re
import sqlite3
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = ROOT / 'data' / 'plans'
PIECES = ROOT / 'courses'
DOCS = ROOT / 'docs' / 'courses'
DB = ROOT / 'data' / 'index.db'
BASE = ROOT / 'data' / 'index-baseline.csv'
PILOT = {'math-4'}
SUBJECT_FOLDERS = {'arts', 'career-education', 'computer-science', 'eld', 'health', 'library', 'physical-education',
                   'sel', 'social-studies', 'world-languages'}
REPORTS = ('resolve', 'orphans', 'layout', 'status', 'drift')
WHEN = 'when it exists:'
LINK = re.compile(r'\[\[(?:(steps|note|fig):)?([A-Za-z0-9-]+)\]\]')
BARE_ITEM = re.compile(r'(?<![\w\[:/-])(s\d{2}-[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*)(?![\w\]])')
DAY_MENTION = re.compile(r'\b[Dd]ays? (\d{1,3})\b')
FRONT = re.compile(r'---\r?\n(.*?)\r?\n---\r?\n', re.S)
MARK = '<!-- skel'

sys.path.insert(0, str(ROOT / 'scripts'))


def rows_of(path):
    if not path.exists():
        return []
    with io.open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(line for line in f if not line.startswith('#')))


def ids(s):
    return [x.strip() for x in re.split(r'[;,]', s or '') if x.strip()]


def day_nums(s):
    """Day numbers in a CSV cell: 12; 12, 14; 12 to 15; 12-15."""
    out = []
    for a, b in re.findall(r'(\d+)(?:\s*(?:to|-)\s*(\d+))?', s or ''):
        lo, hi = int(a), int(b or a)
        out.extend(range(lo, hi + 1) if hi >= lo and hi - lo < 200 else [lo])
    return out


def courses():
    return [r['id'] for r in rows_of(PLANS / 'course-list.csv')
            if r['id'] not in PILOT and (PLANS / r['id']).is_dir()]


def front(text):
    m = FRONT.match(text)
    head = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(':')
            head[k.strip()] = v.strip()
    return head, (text[m.end():] if m else text)


def rel(p):
    return Path(p).resolve().relative_to(ROOT).as_posix()


class Index:
    def __init__(self):
        self.nodes = {}             # key -> (type, course, local, path, line, state)
        self.edges = []             # (src, dst, kind, hard, path, line, course, day)

    def node(self, key, typ, course, local, path='', line=0, state=''):
        if key not in self.nodes:
            self.nodes[key] = (typ, course, local, path, line, state)

    def edge(self, src, dst, kind, hard, path, line=0, course='', day=None):
        self.edges.append((src, dst, kind, 1 if hard else 0, path, line, course, day))


def listing():
    """The tracked and new files the index is built from (data/, docs/, courses/)."""
    import subprocess
    out = subprocess.run(['git', 'ls-files', '-co', '--exclude-standard', 'data', 'docs', 'courses'], cwd=ROOT,
                         capture_output=True, text=True).stdout
    return sorted(set(out.splitlines()))


def build():
    import unit_skeleton as u
    ix = Index()
    ix.started, ix.files = time.time(), listing()   # stale() reads both: a save during the build, a file gone
    keep = u.SUBJ
    try:
        _build(ix, u)
    finally:
        u.set_subject(keep)
    return ix


def _build(ix, u):
    cl = courses()
    frames = {r['course']: r for r in rows_of(PLANS / 'frames.csv')}
    for c in cl:
        ix.node('course:' + c, 'course', c, c, 'data/plans/course-list.csv')
    # progressions
    for p in sorted((ROOT / 'data' / 'progressions').glob('*.csv')):
        if p.stem.endswith('-excluded'):
            continue
        for i, r in enumerate(rows_of(p), 2):
            if r.get('skill_id'):
                ix.node('prog:%s:%s' % (p.stem, r['skill_id']), 'prog', '', r['skill_id'], rel(p), i)
        for i, r in enumerate(rows_of(p), 2):
            sk = 'prog:%s:%s' % (p.stem, r.get('skill_id'))
            for a in ids(r.get('assumes')):
                ix.edge(sk, 'prog:%s:%s' % (p.stem, a), 'assumes', True, rel(p), i)
            # the skill owns its standard codes (review change 5); a cell that is not a code is soft, shown by trace
            for code in ids(r.get('standard')):
                code = code.strip().lstrip('~')
                known = code in all_codes()
                if known:
                    ix.node('code:' + code, 'code', '', code)
                ix.edge(sk, 'code:' + code, 'owns', known, rel(p), i)
            # cross_subject: "math:K.MD.A.2 (why)"; the subject's code or skill it leans on, soft
            for m in re.finditer(r'\b([a-z][a-z-]*):\s*([A-Za-z0-9][\w.-]*[\w])', r.get('cross_subject') or ''):
                tgt = m.group(2)
                if m.group(1) not in CROSS:
                    continue
                dst = ('code:' + tgt) if tgt in all_codes() else 'prog:%s:%s' % (m.group(1), tgt)
                if tgt in all_codes():
                    ix.node(dst, 'code', '', tgt)
                ix.edge(sk, dst, 'leans-cross', False, rel(p), i)
    for c in cl:
        _course(ix, c, frames.get(c), u.subject_of(c) or '')
        _frame_units(ix, c, u.subject_of(c) or '')
    _ledger_reviews(ix)
    _tools(ix, cl)


def _frame_units(ix, c, subj):
    """unit teaches skill (review change 5): the frame's Units table, column Skills, through frame.py."""
    try:
        import frame
        f = frame.parse(c)
    except Exception:                      # a course with no frame file yet
        return
    path = 'docs/courses/%s/frame.md' % c
    for r in f.get('table') or []:
        n = (r.get('#') or '').strip()
        if not n.isdigit():
            continue
        for sid in ids(r.get('Skills')):
            ix.edge('unit:%s:%d' % (c, int(n)), skill_key(ix, subj, sid) or 'prog:%s:%s' % (subj, sid), 'teaches',
                    True, path, 0, c)


def ledger_key(r):
    return 'row:%s:%s:%s:%s:%s' % (r['course'], r['where'], r['day'] or '-', r['kind'], (r['entry'] or '')[:60])


def _ledger_reviews(ix):
    """row reviews row (review change 5): every ledger "review of ..." citation, resolved by ledger.py as the recheck
    does. Soft: the recheck is the gate on them; the index lets trace.py walk them."""
    import ledger
    for subj in ('math', 'ela', 'science', 'social-studies'):
        try:
            rs = ledger.rows(subj)
        except Exception:
            continue
        lix = ledger.index(rs)
        key, seen = {}, {}
        for row in rs:                         # every row is a node, reviewed or not (trace lists a day's rows)
            k = ledger_key(row)
            seen[k] = seen.get(k, 0) + 1
            if seen[k] > 1:                    # two rows can share course, place, kind and 60 characters
                k = '%s#%d' % (k, seen[k])
            key[id(row)] = k
            ix.node(k, 'row', row['course'], k[4:], 'data/plans/%s/ledger.csv' % row['course'], 0, row['stage'])
        for r, ts in ledger.claims(subj, rs):
            src = key.get(id(r)) or ledger_key(r)
            for t in ts:
                st, hit = ledger.resolve(t, lix)
                for h in hit[:4]:
                    d = int(r['day']) if (r['day'] or '').isdigit() else None
                    ix.edge(src, key.get(id(h)) or ledger_key(h), 'reviews', False,
                            'data/plans/%s/ledger.csv' % r['course'], 0, r['course'], d)


def _tools(ix, cl):
    """Tool nodes (consolidation step 5 item 1): one per data/tool-stages.csv row, its stage as state and its record as
    path. Each course's TOOL-ASKS.md heading is an `ask` node, with a hard edge to the unit it names ("[unit N](sNN.md)")
    and to any tool it names by folder (tools/<id>). Asks are the curriculum's side: a tool answers an ask, never
    the other way round, and no catalog list is read."""
    for i, r in enumerate(rows_of(ROOT / 'data' / 'tool-stages.csv'), 2):
        ix.node('tool:' + r['tool_id'], 'tool', '', r['tool_id'], r.get('record', ''), 0, r.get('stage', ''))
    for c in cl:
        p = DOCS / c / 'TOOL-ASKS.md'
        if c in PILOT or not p.exists():
            continue
        ask = ''
        for i, ln in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            h = re.match(r'## (.+)', ln)
            if h:
                ask = 'ask:%s:%s' % (c, re.sub(r'[^a-z0-9]+', '-', h.group(1).lower()).strip('-'))
                ix.node(ask, 'ask', c, h.group(1).strip(), rel(p), i)
                continue
            if not ask:
                continue
            for m in re.finditer(r'\[unit (\d+)\]\(s(\d+)\.md\)', ln):
                ix.edge(ask, 'unit:%s:%d' % (c, int(m.group(2))), 'asked-by', True, rel(p), i, c)
            for m in re.finditer(r'(?<![\w/])tools/([a-z0-9][a-z0-9-]*)', ln):
                ix.edge(ask, 'tool:' + m.group(1), 'answered-by', True, rel(p), i, c)


CODES = set()
CROSS = {'lit', 'ela', 'math', 'science', 'social-studies', 'health', 'sel', 'physical-education', 'computer-science',
         'library', 'arts', 'cte', 'eld', 'spanish'}    # cross_subject prefixes (lit: the literacy codes)


def skill_key(ix, subj, sid):
    """The progression node of a skill id: the course's own subject first, then any subject (cross-subject rows)."""
    if 'prog:%s:%s' % (subj, sid) in ix.nodes:
        return 'prog:%s:%s' % (subj, sid)
    if not hasattr(ix, 'skills'):
        ix.skills = {v[2]: k for k, v in ix.nodes.items() if v[0] == 'prog'}
    return ix.skills.get(sid, '')


def all_codes():
    """Every code in every standards file (data/standards/*.txt, code then a tab), so electives and course-own
    outcome lists (curio-math-electives.txt) resolve as well as the four core subjects."""
    if not CODES:
        for p in (ROOT / 'data' / 'standards').glob('*.txt'):
            for line in io.open(p, encoding='utf-8'):
                if line.strip() and not line.startswith('#'):
                    CODES.add(line.split('	', 1)[0].strip())
    return CODES


def _code(ix, std, code, src, path, line, c, day):
    """A code cell: a standard code, or (items may cite one) a progression skill id of the course's subject."""
    code = code.strip().lstrip('~')
    if not code:
        return
    if code not in all_codes() and skill_key(ix, std, code):
        ix.edge(src, skill_key(ix, std, code), 'skill', True, path, line, c, day)
        return
    if code in all_codes():
        ix.node('code:' + code, 'code', '', code)
    ix.edge(src, 'code:' + code, 'code', True, path, line, c, day)


def _course(ix, c, frame, std):
    d = PLANS / c
    p = d / 'days.csv'
    units = int(frame['units']) if frame and (frame.get('units') or '').isdigit() else 0
    for n in range(1, units + 1):
        ix.node('unit:%s:%d' % (c, n), 'unit', c, str(n), 'data/plans/frames.csv')
    days = set()
    for i, r in enumerate(rows_of(p), 2):
        if not (r.get('day') or '').isdigit():
            continue
        n = int(r['day'])
        days.add(n)
        k = 'day:%s:d%03d' % (c, n)
        ix.node(k, 'day', c, 'd%03d' % n, rel(p), i)
        un = (r.get('unit') or '').strip()
        if un:
            top = un.split('.')[0]
            if '.' in un:
                ix.node('section:%s:%s' % (c, un), 'section', c, un, rel(p), i)
            if top.isdigit():
                ix.edge(k, 'unit:%s:%s' % (c, top), 'in-unit', True, rel(p), i, c, n)
        for code in ids(r.get('codes')):
            _code(ix, std, code, k, rel(p), i, c, n)
        for sk_ in ids(r.get('skills')):
            ix.edge(k, skill_key(ix, std, sk_) or 'prog:%s:%s' % (std, sk_), 'skill', True, rel(p), i, c, n)
    # plan CSVs
    for i, r in enumerate(rows_of(d / 'items.csv'), 2):
        k = 'item:%s:%s' % (c, r['item_id'])
        dy = int(r['day']) if (r.get('day') or '').isdigit() else None
        ix.node(k, 'item', c, r['item_id'], 'data/plans/%s/items.csv' % c, i)
        if dy is not None:
            ix.edge(k, 'day:%s:d%03d' % (c, dy), 'on-day', True, 'data/plans/%s/items.csv' % c, i, c, dy)
        for code in ids(r.get('code')):
            _code(ix, std, code, k, 'data/plans/%s/items.csv' % c, i, c, dy)
    for i, r in enumerate(rows_of(d / 'wrongs.csv'), 2):
        it = 'item:%s:%s' % (c, r.get('item_id', ''))
        ix.edge('file:data/plans/%s/wrongs.csv' % c, it, 'wrong-of', True, 'data/plans/%s/wrongs.csv' % c, i, c)
    for t, cols in (('handbacks', ('from_day', 'to_day')), ('errors', ('day',)), ('materials', ('made_day', 'used_days')),
                    ('sources', ('days',)), ('source-map', ('days',)), ('ledger', ('day',))):
        f = d / ('%s.csv' % t)
        for i, r in enumerate(rows_of(f), 2):
            for col in cols:
                for n in day_nums(r.get(col)):
                    ix.edge('file:' + rel(f), 'day:%s:d%03d' % (c, n), t, True, rel(f), i, c, n)
            if t == 'sources' and r.get('source_id'):
                ix.node('source:%s:%s' % (c, r['source_id']), 'source', c, r['source_id'], rel(f), i)
    # words a day (or a section, when the ledger row names no day) introduces: ledger term rows (4.I)
    import vocabulary
    lf = d / 'ledger.csv'
    for i, r in enumerate(rows_of(lf), 2):
        if r.get('kind') != 'term':
            continue
        ns = day_nums(r.get('day'))
        m = re.fullmatch(r'u(\d+)-(\d+)', r.get('where', ''))
        srcs = ['day:%s:d%03d' % (c, n) for n in ns] or (['section:%s:%d.%d' % (c, int(m[1]), int(m[2]))] if m else
                                                        ['file:' + rel(lf)])
        for w in vocabulary.heads(r.get('entry', '')):
            ix.node('word:' + w, 'word', '', w)
            for src in srcs:
                ix.edge(src, 'word:' + w, 'introduces', False, rel(lf), i, c, ns[0] if ns else None)
    for i, r in enumerate(rows_of(d / 'parts.csv'), 2):
        _code(ix, std, r.get('code', ''), 'file:data/plans/%s/parts.csv' % c, 'data/plans/%s/parts.csv' % c, i, c, None)
    # days and pieces
    folder = PIECES / c
    if folder.is_dir():
        for f in sorted(folder.rglob('*.md')):
            _piece(ix, c, f, days)
    # written plans: soft mentions
    pd = DOCS / c
    if pd.is_dir():
        for f in sorted(pd.glob('*.md')):
            if re.fullmatch(r's\d+\.md|u\d+-\d+\.md|scope-and-sequence\.md|frame\.md', f.name):
                k = 'file:' + rel(f)
                ix.node(k, 'plan', c, f.name, rel(f))
                _mentions(ix, c, k, f, f.read_text(encoding='utf-8'), days)


def _mentions(ix, c, k, f, text, days, links=False, day=None):
    """Item links (hard when links=True, in days and pieces), bare item ids and "day N" mentions (soft). A day file's
    mention of its own day is not an edge (close review finding 5)."""
    for i, ln in enumerate(text.splitlines(), 1):
        for m in LINK.finditer(ln):
            ix.edge(k, 'item:%s:%s' % (c, m.group(2)), 'link', links, rel(f), i, c, day)
        bare = LINK.sub(' ', ln)
        for m in BARE_ITEM.finditer(bare):
            ix.edge(k, 'item:%s:%s' % (c, m.group(1)), 'mentions', False, rel(f), i, c, day)
        for m in DAY_MENTION.finditer(bare):
            n = int(m.group(1))
            if n in days and n != day:
                ix.edge(k, 'day:%s:d%03d' % (c, n), 'mentions', False, rel(f), i, c, n)


def _piece(ix, c, f, days):
    text = f.read_text(encoding='utf-8')
    head, _ = front(text)
    r = rel(f)
    m = re.fullmatch(r'd(\d{3})\.md', f.name)
    if m:
        n = int(m.group(1))
        k = 'file:' + r
        ix.node(k, 'day-file', c, f.name, r, 0, head.get('version', ''))
        ix.edge(k, 'day:%s:d%03d' % (c, n), 'is-day', True, r, 1, c, n)
        for x in [x.strip() for x in head.get('leans_on', '').split(';')]:
            if not x or x == 'nothing':
                continue
            soft = x.lower().startswith(WHEN)
            path = x[len(WHEN):].strip() if soft else x
            ix.edge(k, 'path:' + path, 'leans_on', not soft, r, 1, c, n)
        _mentions(ix, c, k, f, text, days, links=True, day=n)
    else:
        local = f.relative_to(PIECES / c).as_posix()
        k = 'piece:%s:%s' % (c, local)
        ix.node(k, 'piece', c, local, r, 0, head.get('version', ''))
        _mentions(ix, c, k, f, text, days, links=True)


def resolved(ix):
    """dst keys that exist: nodes, plus path:<p> for files on disk."""
    ok = set(ix.nodes)
    for e in ix.edges:
        if e[1].startswith('path:') and (ROOT / e[1][5:]).exists():
            ok.add(e[1])
    return ok


def save(ix):
    DB.parent.mkdir(parents=True, exist_ok=True)
    tmp = DB.with_suffix('.%d.tmp' % os.getpid())   # per process: gates in different courses may build at once
    if tmp.exists():
        tmp.unlink()
    con = sqlite3.connect(tmp)
    con.execute('create table nodes (key text primary key, type text, course text, local text, path text, '
                'line int, state text)')
    con.execute('create table edges (src text, dst text, kind text, hard int, path text, line int, course text, '
                'day int)')
    con.executemany('insert into nodes values (?,?,?,?,?,?,?)', [(k,) + v for k, v in ix.nodes.items()])
    con.executemany('insert into edges values (?,?,?,?,?,?,?,?)', ix.edges)
    con.execute('create index e_dst on edges (dst)')
    con.execute('create index e_path on edges (path)')
    con.execute('create table meta (files text)')
    con.execute('insert into meta values (?)', ('\n'.join(getattr(ix, 'files', [])),))
    con.commit()
    con.close()
    for i in range(20):                               # another process may have the db open for a moment
        try:
            tmp.replace(DB)
            if getattr(ix, 'started', None):          # dated from the build's start, not its save (Fable 4.L)
                os.utime(DB, (ix.started, ix.started))
            return
        except PermissionError:
            time.sleep(0.5)
    tmp.unlink()                                      # the other process's fresh build stands


def stale():
    """True when data/index.db is missing or older than any file it is built from: the tracked and new files under
    data/, docs/ and courses/, or this script (a stat of each, about a second)."""
    if not DB.exists():
        return True
    built = DB.stat().st_mtime
    if Path(__file__).stat().st_mtime > built:
        return True
    files = listing()
    try:
        con = sqlite3.connect(DB)
        try:
            saved = con.execute('select files from meta').fetchone()[0].split('\n')
        finally:
            con.close()
    except sqlite3.Error:
        return True       # an index saved before the file list was kept
    if saved != files:
        return True       # a file added or gone since the build
    for f in files:
        try:
            if (ROOT / f).stat().st_mtime > built:
                return True
        except OSError:
            return True   # a file gone since the build
    return False


def load():
    """The index as saved in data/index.db."""
    ix = Index()
    con = sqlite3.connect(DB)
    try:
        for k, *v in con.execute('select key, type, course, local, path, line, state from nodes'):
            ix.nodes[k] = tuple(v)
        ix.edges = [tuple(r) for r in con.execute('select src, dst, kind, hard, path, line, course, day from edges')]
    finally:
        con.close()
    return ix


def dump(ix, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    with io.open(out / 'nodes.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['key', 'type', 'course', 'local', 'path', 'line', 'state'])
        w.writerows([(k,) + v for k, v in sorted(ix.nodes.items())])
    with io.open(out / 'edges.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['src', 'dst', 'kind', 'hard', 'path', 'line', 'course', 'day'])
        w.writerows(ix.edges)


# ---- reports: each returns [(key, message)]; key is stable (no line numbers) so the baseline survives edits

def r_resolve(ix):
    ok = resolved(ix)
    out = []
    for src, dst, kind, hard, path, line, c, day in ix.edges:
        if hard and dst not in ok:
            what = dst[5:] if dst.startswith('path:') else dst
            out.append(('%s|%s|%s' % (path, kind, what), '%s:%s: %s %s does not resolve' % (path, line, kind, what)))
    return out


def r_orphans(ix):
    out = []
    leaned = {e[1][5:] for e in ix.edges if e[2] == 'leans_on'}
    for k, (typ, c, local, path, line, state) in ix.nodes.items():
        if typ == 'piece' and local.endswith('.md') and '/' in local and path not in leaned:
            out.append(('piece|' + path, '%s: a piece no day leans on (an orphan, or a day misses it in leans_on)'
                        % path))
    ok = set(ix.nodes)
    for src, dst, kind, hard, path, line, c, day in ix.edges:
        if kind == 'is-day' and dst not in ok:
            out.append(('dayfile|' + path, '%s: a day file with no days.csv row' % path))
        if kind == 'in-unit' and dst not in ok:
            out.append(('unit|%s|%s' % (c, dst), '%s:%s: day %s sits in %s, which the frame does not have'
                        % (path, line, day, dst)))
    return out


def r_layout(ix):
    import homes
    out = []
    for ln in homes.check():
        path = ln.split(' ', 1)[1].split(': ', 1)[0]
        out.append(('home|' + path, ln))
    return out


def plan_state(p):
    if not p.exists():
        return 'none'
    t = p.read_text(encoding='utf-8')
    return 'skeleton' if 'TODO(writer)' in t else 'written'


def r_status(ix):
    out = []
    same = 0
    for i, r in enumerate(rows_of(PLANS / 'flow-status.csv'), 2):
        node, state = r.get('node', ''), r.get('state', '')
        m = re.fullmatch(r'unit:([a-z0-9-]+):(\d+)', node)
        s = re.fullmatch(r'section:([a-z0-9-]+):(\d+)\.(\d+)', node)
        if m:
            p = DOCS / m.group(1) / ('s%02d.md' % int(m.group(2)))
        elif s:
            p = DOCS / s.group(1) / ('u%02d-%d.md' % (int(s.group(2)), int(s.group(3))))
        else:
            continue
        if m and m.group(1) in PILOT or s and s.group(1) in PILOT:
            continue
        f = plan_state(p)
        if state == 'done' and f != 'written':
            out.append(('flow|' + node, 'data/plans/flow-status.csv:%d: %s is done, but %s is %s'
                        % (i, node, rel(p) if p.exists() else p.relative_to(ROOT).as_posix(), f)))
        elif state == 'done':
            same += 1
    print('status: %d flow-status done rows sit on a written plan; they stay: plan_flow reads them as "done to the '
          'stage 4 bar", which the file alone does not show (only "on file")' % same)
    for c in sorted(COURSE_SET):
        have = {}
        for f in sorted((PIECES / c).glob('*/d*.md')):
            m = re.fullmatch(r'd(\d{3})[a-z]?\.md', f.name)
            if m:
                v = re.search(r'^version:[ \t]*(.*)$', f.read_text(encoding='utf-8')[:1500], re.M)
                have.setdefault(int(m.group(1)), []).append((rel(f), v.group(1).strip() if v else ''))
        out += day_status(c, rows_of(PLANS / c / 'ledger.csv'), have)
        plans = {p.name for p in (DOCS / c).glob('*.md')} if (DOCS / c).is_dir() else set()
        items = rows_of(PLANS / c / 'items.csv')
        out += order_status(c, DAYS.get(c) or rows_of(PLANS / c / 'days.csv'), items, set(have), plans)
        out += upstream_status(c, DAYS.get(c) or rows_of(PLANS / c / 'days.csv'), items)
    return out


def upstream_status(c, days, items):
    """A day read at a gate whose days.csv row or items (keys too) changed since (review change 6; marks stored by
    scripts/day_version.py in data/plans/<course>/day-marks.csv). Look at the day against the new data, then stamp
    it again (`day_version.py <course> stamp <date>` after a full read). The key carries the stored mark's hash, so a
    baselined miss stays known only until the next stamp: a later change to a restamped day shows as new."""
    import day_version
    return [('upstream|%s|d%03d|%s' % (c, d, r['hash'][:8]), 'data/plans/%s/days.csv: day %d changed upstream (its days.csv row or '
             'items) since its %s mark of %s; re-read the day against it' % (c, d, r['stage'], r['date']))
            for d, r in day_version.changed(c, days, items)]


def _sections(cell):
    return ['u%02d-%d.md' % (int(a), int(b)) for a, b in re.findall(r'(\d+)\.(\d+)', cell or '')]


def order_status(c, days, items, have, plans):
    """Build order (pedagogy-architecture review change 1, 2026-11-25): nothing is made before the plan above it.
    - a day file needs its section plan (uNN-S.md); a course-level day (stretch C) needs the scope and sequence;
    - a section plan needs its unit plan (sNN.md), and a unit plan needs the scope and sequence;
    - a section's items.csv rows need its section plan (a row's section is its `unit` cell, else its day's section);
      a unit-level row (stretch N, no section) needs the unit plan, a course-level row (stretch C) the scope.
    One miss per (course, kind, missing parent), so a whole unshaped section is one line, not twenty.
    `days` and `items` are CSV rows, `have` the day numbers with a day file, `plans` the file names in docs/courses/<c>/."""
    scope = 'scope-and-sequence.md'
    of_day = {int(r['day']): r for r in days if (r.get('day') or '').isdigit()}
    miss = {}

    def need(kind, parent, what):
        if parent not in plans:
            miss.setdefault((kind, parent), []).append(what)

    for d in sorted(have):
        r = of_day.get(d)
        if not r:
            continue                              # a day file with no row is the orphans report's
        secs = _sections(r.get('unit'))
        if secs:
            for p in secs:
                need('day', p, 'day %d' % d)
        elif (r.get('stretch') or '').strip() == 'C':
            need('day', scope, 'day %d' % d)
        elif (r.get('stretch') or '').strip().isdigit():
            need('day', 's%02d.md' % int(r['stretch']), 'day %d' % d)
    for p in sorted(plans):
        m = re.fullmatch(r'u(\d+)-\d+\.md', p)
        if m:
            need('section', 's%02d.md' % int(m.group(1)), p)
        elif re.fullmatch(r's\d+\.md', p):
            need('unit', scope, p)
    for r in items:
        secs = _sections(r.get('unit'))
        if not secs and (r.get('day') or '').isdigit() and int(r['day']) in of_day:
            secs = _sections(of_day[int(r['day'])].get('unit'))
        st = (r.get('stretch') or '').strip()
        for p in secs or ([scope] if st == 'C' else ['s%02d.md' % int(st)] if st.isdigit() else []):
            need('items', p, r.get('item_id', ''))
    out = []
    words = {'day': 'day file', 'section': 'section plan', 'unit': 'unit plan', 'items': 'items.csv row'}
    for (kind, parent), what in sorted(miss.items()):
        out.append(('order|%s|%s|%s' % (c, kind, parent),
                    'docs/courses/%s/%s is missing, but %d %s(s) under it exist (%s%s): write the plan above first'
                    % (c, parent, len(what), words[kind], ', '.join(what[:6]), ', ...' if len(what) > 6 else '')))
    return out


def day_status(c, ledger, have):
    """A day's status has two homes: its file (frontmatter `version:`, which exists only once the day is written) and
    the ledger stage (`written` only when a day adds the row, ledger.py add). They must agree both ways (close review,
    goal test 10; later L133):
    - a written row with no day, or naming a day with no day file, contradicts the files;
    - a day file with no written ledger row for its day contradicts the ledger (a day that introduces nothing new says
      so with one `none` row, ledger.py add ... none "<why>");
    - a day file with no `version:` line has no status of its own.
    `have` is {day number: [(path, version line), ...]} (a plain set of day numbers is read as files with versions)."""
    if not isinstance(have, dict):
        have = {d: [('', 'draft')] for d in have}
    out = []
    led = set()
    for r in ledger:
        if r.get('stage') == 'written':
            led.update(int(d) for d in re.findall(r'\d+', r.get('day') or ''))
    for d in sorted(have):
        if d not in led:
            out.append(('dayfile|%s|d%03d' % (c, d), '%s: day %d has a day file but no written ledger row in '
                        'data/plans/%s/ledger.csv (add what it introduces, or one `none` row)'
                        % (have[d][0][0] or c, d, c)))
        for path, v in have[d]:
            if not v:
                out.append(('version|%s|d%03d' % (c, d), '%s: day %d has no version: line' % (path or c, d)))
    for i, r in enumerate(ledger, 2):
        if r.get('stage') != 'written':
            continue
        days = [int(d) for d in re.findall(r'\d+', r.get('day') or '')]
        where = 'data/plans/%s/ledger.csv:%d' % (c, i)
        if not days:
            out.append(('ledger|%s|%d' % (c, i), '%s: stage written but no day named' % where))
        for d in days:
            if d not in have:
                out.append(('ledger|%s|d%03d|%s' % (c, d, (r.get('entry') or '')[:40]),
                            '%s: stage written for day %d, which has no day file' % (where, d)))
    return out


def r_drift(ix):
    import unit_skeleton as u
    out = []
    for p in sorted(DOCS.glob('*/*.md')):
        if not re.fullmatch(r's\d+\.md|u\d+-\d+\.md', p.name) or p.parent.name in PILOT | SUBJECT_FOLDERS:
            continue
        t = p.read_text(encoding='utf-8')
        if MARK in t:
            out.append(('skel|' + rel(p), '%s: holds a stored <!-- skel --> block' % rel(p)))
        m = re.fullmatch(r's(\d+)\.md', p.name)
        if not m or p.parent.name not in COURSE_SET:
            continue
        unit = int(m.group(1))
        rows = [r for r in DAYS[p.parent.name] if (r.get('unit') or '').split('.')[0] == str(unit)]
        if not rows:
            continue
        days = {int(r['day']): r['kind'] for r in rows if r['day'].isdigit()}
        lines = t.splitlines()
        mh = re.search(r'\*\*Days ([^*]+)\*\*', ' '.join(lines[:12]))
        if mh:
            got = set()
            for tok in re.split(r'\s*,\s*|\s+and\s+', mh.group(1).strip()):
                m3 = re.fullmatch(r'(\d+)(?: to (\d+))?', tok.strip())
                if m3:
                    got.update(range(int(m3.group(1)), int(m3.group(2) or m3.group(1)) + 1))
            if got != set(days):
                out.append(('head|' + rel(p), '%s: header says days %s, days.csv has %s'
                            % (rel(p), mh.group(1), u.runs_text(sorted(days)))))
        dl = [i for i, ln in enumerate(lines) if re.match(r'^## Day list\b', ln)]
        if dl:
            for ln in lines[dl[0] + 1:]:
                if ln.startswith('## '):
                    break
                c = [x.strip() for x in ln.strip().strip('|').split('|')] if ln.startswith('|') else []
                if len(c) >= 3 and c[0].isdigit() and int(c[0]) in days and c[2] != days[int(c[0])]:
                    out.append(('list|%s|%s' % (rel(p), c[0]), '%s: day list says day %s is "%s", days.csv says "%s"'
                                % (rel(p), c[0], c[2], days[int(c[0])])))
    return out


COURSE_SET = set()
DAYS = {}


def load_days():
    COURSE_SET.update(courses())
    for c in COURSE_SET:
        DAYS[c] = rows_of(PLANS / c / 'days.csv')


def baseline():
    return {(r['report'], r['key']) for r in rows_of(BASE)}


def write_baseline(report, misses):
    keep = [r for r in rows_of(BASE) if r['report'] != report]
    keep += [dict(report=report, key=k) for k in sorted({k for k, _ in misses})]
    keep.sort(key=lambda r: (r['report'], r['key']))
    with io.open(BASE, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, ['report', 'key'], lineterminator='\n')
        w.writeheader()
        w.writerows(keep)


def run_report(ix, name, rebase=False):
    misses = globals()['r_' + name](ix)
    known = {k for r, k in baseline() if r == name}
    keys = {k for k, _ in misses}
    new = [(k, msg) for k, msg in misses if k not in known]
    gone = sorted(known - keys)
    for _, msg in new:
        print('FAIL %s: %s' % (name, msg))
    for k in gone[:20]:
        print('fixed %s (known miss no longer seen; --baseline drops it): %s' % (name, k))
    if len(gone) > 20:
        print('fixed %s: ... and %d more' % (name, len(gone) - 20))
    print('%s: %d new, %d known, %d fixed' % (name, len(new), len(keys & known), len(gone)))
    if rebase:
        write_baseline(name, misses)
        print('%s: baseline rewritten (%d known misses)' % (name, len(keys)))
        return 0
    return 1 if new else 0


def self_test():
    ok = True

    def check(name, cond):
        nonlocal ok
        ok = ok and bool(cond)
        print('  %s %s' % ('ok    ' if cond else 'FAILED', name))
    check('day numbers', day_nums('3; 5 to 7, 9') == [3, 5, 6, 7, 9])
    check('front matter', front('---\nday: 4\nleans_on: a; b\n---\n# T\n')[0] == {'day': '4', 'leans_on': 'a; b'})
    check('links', [m.group(2) for m in LINK.finditer('[[s01-X2]] and [[steps:s01-Q3]]')] == ['s01-X2', 's01-Q3'])
    check('bare item ids', BARE_ITEM.findall('see `s08-G145-1` and s01-P2-RM, not [[s01-X]]') ==
          ['s08-G145-1', 's01-P2-RM'])
    ix = Index()
    ix.node('day:c:d001', 'day', 'c', 'd001')
    ix.edge('file:x', 'day:c:d001', 'is-day', True, 'x', 1, 'c', 1)
    ix.edge('file:x', 'item:c:s01-Z', 'link', True, 'x', 2, 'c', 1)
    ix.edge('file:x', 'path:courses/none.md', 'leans_on', True, 'x', 1, 'c', 1)
    ix.edge('file:x', 'path:courses/later.md', 'leans_on', False, 'x', 1, 'c', 1)
    miss = [k for k, _ in r_resolve(ix)]
    check('resolve finds a missing item and path, not a "when it exists" one',
          sorted(miss) == ['x|leans_on|courses/none.md', 'x|link|item:c:s01-Z'])
    led = [{'day': '3', 'stage': 'written', 'entry': 'a'}, {'day': '', 'stage': 'written', 'entry': 'b'},
           {'day': '9', 'stage': 'planned', 'entry': 'c'}, {'day': '4', 'stage': 'written', 'entry': 'd'}]
    check('day status: a written ledger row with no day, or a day with no file, fails (goal test 10)',
          len(day_status('c', led, {4})) == 2 and not day_status('c', led[2:], {4}))
    check('day status: a day file with no written ledger row, or no version line, fails (L133)',
          [k for k, _ in day_status('c', led[3:], {4: [('p', 'draft 1')], 5: [('q', '')]})]
          == ['dayfile|c|d005', 'version|c|d005']
          and not day_status('c', led[3:] + [{'day': '5', 'stage': 'written', 'kind': 'none'}], {4: [('p', 'x')],
                                                                                             5: [('q', 'y')]}))
    days = [{'day': '1', 'stretch': '1', 'unit': '1.1'}, {'day': '2', 'stretch': '1', 'unit': '1.2'},
            {'day': '3', 'stretch': 'C', 'unit': ''}]
    items = [{'item_id': 's01-X2', 'stretch': '1', 'unit': '', 'day': '2'}, {'item_id': 's01-E1', 'stretch': '1',
                                                                            'unit': '', 'day': ''}]
    got = sorted(k for k, _ in order_status('c', days, items, {1, 2, 3}, {'u01-1.md', 'u02-1.md'}))
    check('order: a day, a section plan and items need the plan above them (review change 1)',
          got == ['order|c|day|scope-and-sequence.md', 'order|c|day|u01-2.md',
                  'order|c|items|s01.md', 'order|c|items|u01-2.md', 'order|c|section|s01.md',
                  'order|c|section|s02.md']
          and not order_status('c', days, items, {1, 2, 3}, {'u01-1.md', 'u01-2.md', 's01.md',
                                                               'scope-and-sequence.md'}))
    print('index self-test: %s' % ('all passed' if ok else 'FAILED'))
    return 0 if ok else 1


def main(a):
    if a == ['--self-test']:
        return self_test()
    flags = [x[2:] for x in a if x[2:] in REPORTS]
    if '--reports' in a:
        flags = list(REPORTS)
    if '--rebuild' not in a and not stale():      # nothing it reads changed: the saved index stands (4.L row 8 (b))
        ix, how = load(), 'fresh, loaded'
    else:
        ix, how = build(), 'built'
        save(ix)
    hard = sum(e[3] for e in ix.edges)
    print('index: %d nodes, %d edges (%d hard) -> %s' % (len(ix.nodes), len(ix.edges), hard, rel(DB)))
    print('index %s' % how)
    if '--csv' in a:
        dump(ix, a[a.index('--csv') + 1])
    load_days()
    rc = 0
    for name in flags:
        rc |= run_report(ix, name, '--baseline' in a)
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
