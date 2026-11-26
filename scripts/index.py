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
Edges are hard (they must resolve) or soft (`mentions`: "day N" in a course's own plans, bare item ids in prose;
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


def build():
    import unit_skeleton as u
    ix = Index()
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
            for a in ids(r.get('assumes')):
                ix.edge('prog:%s:%s' % (p.stem, r.get('skill_id')), 'prog:%s:%s' % (p.stem, a), 'assumes', True,
                        rel(p), i)
    for c in cl:
        _course(ix, c, frames.get(c), u.subject_of(c) or '')
    _tools(ix, cl)


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
            _piece(ix, c, f)
    # written plans: soft mentions
    pd = DOCS / c
    if pd.is_dir():
        for f in sorted(pd.glob('*.md')):
            if re.fullmatch(r's\d+\.md|u\d+-\d+\.md|scope\.md|frame\.md', f.name):
                k = 'file:' + rel(f)
                ix.node(k, 'plan', c, f.name, rel(f))
                _mentions(ix, c, k, f, f.read_text(encoding='utf-8'), days)


def _mentions(ix, c, k, f, text, days, links=False, day=None):
    for i, ln in enumerate(text.splitlines(), 1):
        for m in LINK.finditer(ln):
            ix.edge(k, 'item:%s:%s' % (c, m.group(2)), 'link', links, rel(f), i, c, day)
        bare = LINK.sub(' ', ln)
        for m in BARE_ITEM.finditer(bare):
            ix.edge(k, 'item:%s:%s' % (c, m.group(1)), 'mentions', False, rel(f), i, c, day)
        if not links:
            for m in DAY_MENTION.finditer(bare):
                n = int(m.group(1))
                if n in days:
                    ix.edge(k, 'day:%s:d%03d' % (c, n), 'mentions', False, rel(f), i, c, n)


def _piece(ix, c, f):
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
        _mentions(ix, c, k, f, text, set(), links=True, day=n)
    else:
        local = f.relative_to(PIECES / c).as_posix()
        k = 'piece:%s:%s' % (c, local)
        ix.node(k, 'piece', c, local, r, 0, head.get('version', ''))
        _mentions(ix, c, k, f, text, set(), links=True)


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
    con.commit()
    con.close()
    for i in range(20):                               # another process may have the db open for a moment
        try:
            tmp.replace(DB)
            return
        except PermissionError:
            time.sleep(0.5)
    tmp.unlink()                                      # the other process's fresh build stands


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
    print('index self-test: %s' % ('all passed' if ok else 'FAILED'))
    return 0 if ok else 1


def main(a):
    if a == ['--self-test']:
        return self_test()
    flags = [x[2:] for x in a if x[2:] in REPORTS]
    if '--reports' in a:
        flags = list(REPORTS)
    ix = build()
    save(ix)
    hard = sum(e[3] for e in ix.edges)
    print('index: %d nodes, %d edges (%d hard) -> %s' % (len(ix.nodes), len(ix.edges), hard, rel(DB)))
    if '--csv' in a:
        dump(ix, a[a.index('--csv') + 1])
    load_days()
    rc = 0
    for name in flags:
        rc |= run_report(ix, name, '--baseline' in a)
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
