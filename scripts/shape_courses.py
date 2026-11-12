r"""Shape, the rule-only parts, for every course (path step 3). No tokens.

    python scripts/shape_courses.py            write shape files, shape.csv, cards.json, docs/spec-fixes/NEXT.md
    python scripts/shape_courses.py --apply    also spell out math module standards in data/modules.csv

Run scripts/coverage_ledger.py and scripts/catalog_maps.py first (and spec_fixes.py after, so its files agree).
Reads the extract rows, data/coverage.csv, data/modules.csv, data/tools-concepts.csv, the spec sort,
docs/spec-fixes/done.txt and the two hand-kept files in docs/agents/catalog/shape/:

  hand.txt        courses shaped by hand; their .md files are never overwritten
  decisions.csv   course,tool,call,date,note : Cory's Desk answers and hand overrides, one line per tool.
                  call = approved (second tool approved: the spec can be fixed on the split),
                         asked (on the Desk, wait), hold (looked at by hand: no second tool), declined

A course is its own modules plus every band module that carries one of its standards (computer science, which has
no filed standard text here, takes every band module whose band holds the grade).

What the script decides by rule, and nothing more:
  load        a tool's codes in this course (lettered parts counted, claimed codes left out) against its minutes;
              loaded = over four codes; long = over 35 minutes
  second tool a loaded tool whose codes fall into a group that reads as taught and a group that does not, when
              giving each weak code a model and five items (about five minutes each) would pass one sitting
              (20 minutes in K and grade 1, 25 in grade 2, 35 from grade 3) by more than five minutes: the tool keeps the first group, a
              new lesson tool in the same module takes the second. A band tool is never split from a grade file:
              its spec gets a path for each grade first.
  two topics  a math module holding standards from two domains (or two measurement clusters): two tools when
              giving the weaker topic a model and five items would pass about 35 minutes, else one
  spell-out   math modules that list clusters get their own standards; a cluster shared by two modules goes to
              the module whose tool carries each standard
Everything else in a shape file (what a spec read would show, whether a setting suits a class) is not judged here.
"""
import csv, glob, io, json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, 'docs', 'agents', 'catalog')
SHAPE = os.path.join(CAT, 'shape')
TODAY = '2026-11-11'
APPLY = '--apply' in sys.argv

def rd(path):
    with io.open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return list(csv.DictReader(f))
def lines(path):
    for ln in io.open(os.path.join(ROOT, path), encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.strip() and not ln.startswith('#'): yield ln
def short(code):
    code = code.strip(); p = code.split('.')
    i = 1 if '-' in p[0] else 2
    if len(p) > i + 1 and re.match(r'^[A-Z]$', p[i]) and p[i + 1][:1].isdigit(): del p[i]
    return re.sub(r'(\d)\.([a-z])$', r'\1\2', '.'.join(p))
def split(code):
    m = re.match(r'^(.*\d)([a-z])$', code)
    return (m.group(1), m.group(2)) if m else (code, '')
def base(code): return split(short(code))[0]

# ---- filed standards ------------------------------------------------------------------------------------------
long_of, text_of, letters, by_cluster, cluster_of = {}, {}, collections.defaultdict(set), collections.defaultdict(list), {}
for ln in lines('data/standards/ccss-math-standards.txt'):
    sid, _, txt = ln.partition('\t')
    b, let = split(short(sid))
    if let: letters[b].add(let); continue
    long_of[b] = sid; text_of[b] = txt
    by_cluster[sid.rsplit('.', 1)[0]].append(b); cluster_of[b] = sid.rsplit('.', 1)[0]
for ln in lines('data/standards/ccss-ela-standards-full.txt'):
    sid, _, txt = ln.partition('\t')
    b, let = split(short(sid))
    if let: letters[b].add(let); continue
    text_of[b] = txt
focus_of = {}
for r in csv.DictReader(lines('data/standards/ccss-math-focus.csv')):
    for b in by_cluster.get(r['cluster'], []): focus_of[b] = r['focus']

# ---- catalog --------------------------------------------------------------------------------------------------
modules = rd('data/modules.csv'); mod = {m['module_id']: m for m in modules}
concepts = rd('data/tools-concepts.csv'); title = {c['tool_id']: c['title'] for c in concepts}
tools_of = collections.defaultdict(list)
for c in concepts: tools_of[c['module_id']].append(c['tool_id'])
sort = {r['tool']: r for r in rd('docs/agents/catalog/tables/spec-sort.csv')}
cov = rd('data/coverage.csv')
rows = {}
for f in sorted(glob.glob(os.path.join(CAT, 'rows', '*.jsonl'))):
    for ln in io.open(f, encoding='utf-8'):
        if ln.strip():
            r = json.loads(ln); rows[r['id']] = r
done = {}
dp = os.path.join(ROOT, 'docs', 'spec-fixes', 'done.txt')
if os.path.exists(dp):
    for ln in io.open(dp, encoding='utf-8'):
        p = ln.split(None, 3)
        if len(p) >= 2 and not ln.startswith('#') and p[1] in ('fixed', 'reviewed'): done[p[0]] = p[1]
HAND = set(l.split()[0] for l in lines('docs/agents/catalog/shape/hand.txt'))
DEC = {}
for r in csv.DictReader(lines('docs/agents/catalog/shape/decisions.csv')): DEC[(r['course'], r['tool'])] = r

ORDER = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
BANDS = ['k-2', '3-5', '6-8', '6-12', '9-12', 'k-12']
gkey = lambda g: (ORDER + BANDS).index(g) if g in ORDER + BANDS else 99
SUBJ = ['math', 'ela', 'science', 'social-studies', 'computer-science', 'arts', 'health-pe', 'eld', 'world-languages',
        'library', 'cte', 'sel']
NAME = {'math': 'math', 'ela': 'ELA', 'science': 'science', 'social-studies': 'social studies',
        'computer-science': 'computer science', 'arts': 'the arts', 'health-pe': 'health and PE', 'eld': 'ELD',
        'world-languages': 'world languages', 'library': 'library', 'cte': 'CTE', 'sel': 'SEL'}
TRUST = {'math': 'The math reads are a floor: a standard marked taught is taught, and some marked lower may be better than they read.',
         'ela': 'The ELA reads are a floor: a standard marked taught is taught, and some marked lower may be better than they read.',
         'science': 'Rough. The science reads are within one step of right, and the standard texts are not wired in yet, so "all the standards" here means only the codes the modules list. Treat every call below as a candidate.',
         'social-studies': 'Rough. The standard texts are not wired in yet, so "all the standards" here means only the codes the modules list. Treat every call below as a candidate.'}
ROUGH = 'Rough. This subject was read without its standard text, the codes are umbrella codes, and each "taught" needs a check by hand. Load is counted, but no second tool is proposed from it.'
def gname(g): return 'kindergarten' if g == 'k' else ('grade ' + g) if g in ORDER else 'grades ' + g.upper().replace('-', ' to ').replace('K', 'K')
def cname(s, g): return '%s %s' % (gname(g), NAME[s])
def in_band(g, band):
    if '-' not in band or g not in ORDER: return False
    a, b = band.split('-'); return ORDER.index(a) <= ORDER.index(g) <= ORDER.index(b)

cov_by = collections.defaultdict(list)
for r in cov: cov_by[(r['subject'], r['grade'])].append(r)
courses = sorted(cov_by, key=lambda c: (SUBJ.index(c[0]), gkey(c[1])))

def course_modules(s, g):
    own = [m for m in modules if m['subject'] == s and m['grade'] == g]
    ids = {m['module_id'] for m in own}; band = []
    if g in ORDER:
        if s in ('math', 'ela'):
            for r in cov_by[(s, g)]:
                for mid in [x.strip() for x in r['modules'].split(';') if x.strip()]:
                    if mid not in ids and mid in mod: ids.add(mid); band.append(mod[mid])
        else:
            band = [m for m in modules if m['subject'] == s and in_band(g, m['grade'])]
    return own, band

def mod_bases(m):
    out = []
    for c in m['standards'].split(';'):
        c = c.strip()
        if c: out += by_cluster[c] if c in by_cluster else [base(c)]
    return out

WEAK = ('practiced', 'shown', 'touched', 'claimed')
def fmt(codes):
    """3.OA.A.1, 3.OA.A.2, 3.OA.A.3 -> 3.OA.A.1 to 3 where the run is plain"""
    codes = list(dict.fromkeys(codes)); out = []; i = 0
    while i < len(codes):
        j = i
        m = re.match(r'^(.*\.)(\d+)$', codes[i])
        while m and j + 1 < len(codes):
            n = re.match(r'^(.*\.)(\d+)$', codes[j + 1])
            if n and n.group(1) == m.group(1) and int(n.group(2)) == int(re.match(r'^(.*\.)(\d+)$', codes[j]).group(2)) + 1: j += 1
            else: break
        out.append(codes[i] if j == i else '%s to %s' % (codes[i], codes[j].rsplit('.', 1)[1]) if j - i > 1 else codes[i] + ', ' + codes[j])
        i = j + 1
    return ', '.join(out)
def L(b): return long_of.get(b, b)
def topic(b):
    t = text_of.get(b, '')
    t = re.split(r'[.;:(]', t)[0].strip().rstrip(',')
    return (t[:1].lower() + t[1:]) if len(t) <= 90 else (t[:1].lower() + t[1:88].rsplit(' ', 1)[0] + ' ...')

# ---- spell out math module standards --------------------------------------------------------------------------
carriers = collections.defaultdict(set)          # base -> modules whose tools carry it (not merely claim it)
for t, r in rows.items():
    for c in r.get('codes', []):
        if c.get('depth') != 'claimed': carriers[base(c.get('code', ''))].add(r.get('module') or '')
spell, shared_notes = {}, collections.defaultdict(list)
listers = collections.defaultdict(list)
for m in modules:
    if m['subject'] == 'math':
        for b in mod_bases(m): listers[(m['grade'], b)].append(m['module_id'])
for m in modules:
    if m['subject'] != 'math': continue
    keep = []
    for c in [x.strip() for x in m['standards'].split(';') if x.strip()]:
        if c not in by_cluster: keep.append(c); continue
        for b in by_cluster[c]:
            ls = listers[(m['grade'], b)]          # only modules of the same course share a cluster out
            if len(ls) == 1: keep.append(L(b)); continue
            mine = m['module_id'] in carriers[b]; others = [x for x in ls if x != m['module_id'] and x in carriers[b]]
            if mine and not others: keep.append(L(b))
            elif others and not mine: shared_notes[m['module_id']].append('%s goes to %s' % (L(b), mod[others[0]]['title']))
            else: keep.append(L(b)); shared_notes[m['module_id']].append('%s is still listed by %d modules: a hand call' % (L(b), len(ls)))
    new = ';'.join(dict.fromkeys(keep))
    if keep and new != m['standards']: spell[m['module_id']] = new
if APPLY and spell:
    p = os.path.join(ROOT, 'data', 'modules.csv')
    raw = io.open(p, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in raw else '\n'
    rs = list(csv.DictReader(io.StringIO(raw)))
    for r in rs:
        if r['module_id'] in spell: r['standards'] = spell[r['module_id']]
    out = io.StringIO(); w = csv.DictWriter(out, list(rs[0].keys()), lineterminator=nl); w.writeheader(); w.writerows(rs)
    io.open(p, 'w', encoding='utf-8', newline='').write(out.getvalue())
    print('spelled out', len(spell), 'math modules in data/modules.csv')
def standards_of(m):
    s = spell.get(m['module_id'], m['standards'])
    return [x.strip() for x in s.split(';') if x.strip()]

# ---- one course -----------------------------------------------------------------------------------------------
def shape(s, g):
    key = '%s-%s' % (s, g)
    own, band = course_modules(s, g)
    cr = cov_by[(s, g)]
    exp = {base(r['standard']) for r in cr}
    status = {base(r['standard']): r['status'] for r in cr}
    filt = s in ('math', 'ela')
    isband = g not in ORDER
    T = []                                             # one dict per tool in the course
    for m in own + band:
        for t in tools_of[m['module_id']]:
            r = rows.get(t, {})
            cs = [c for c in r.get('codes', []) if (not filt or base(c.get('code', '')) in exp)]
            live = [c for c in cs if c.get('depth') != 'claimed']
            n = len(live)
            if isband and s == 'ela':                  # a band tool teaches one grade at a time
                per = collections.Counter((re.findall(r'\.(K|\d+(?:-\d+)?)\.', c['code']) or ['?'])[0] for c in live)
                n = max(per.values()) if per else 0
            d = {'tool': t, 'title': title.get(t, t), 'module': m, 'band': m in band, 'codes': cs, 'n': n,
                 'minutes': r.get('minutes') or 0, 'use': r.get('use', ''), 'stage': r.get('stage', ''),
                 'sort': (sort.get(t) or {}).get('sort', ''), 'done': done.get(t, ''), 'call': 'keep', 'why': '', 'keep': [], 'move': []}
            d['flag'] = n > 4; d['long'] = d['minutes'] > 35
            T.append(d)
    # second tools: split a loaded tool between what reads as taught and what does not
    for d in T:
        if not d['flag'] or not filt or isband or key in HAND: continue
        groups = collections.OrderedDict()
        for c in d['codes']:
            if c.get('depth') == 'claimed': continue
            groups.setdefault(base(c['code']), []).append(c)
        strong = [b for b, cs in groups.items() if sum(1 for c in cs if c.get('depth') in ('taught', 'explored')) * 2 >= len(cs)]
        weak = [b for b in groups if b not in strong]
        if s == 'math' and weak and strong:            # keep clusters whole where that is possible
            wc = {cluster_of.get(b) for b in weak}; sc = {cluster_of.get(b) for b in strong}
            if len(groups) > 2 and wc & sc and len(wc | sc) > 1:
                both = wc & sc
                tally = {cl: sum(1 for b in strong if cluster_of.get(b) == cl) - sum(1 for b in weak if cluster_of.get(b) == cl) for cl in both}
                strong2 = [b for b in groups if (cluster_of.get(b) in both and tally[cluster_of.get(b)] > 0) or (cluster_of.get(b) not in both and b in strong)]
                weak2 = [b for b in groups if b not in strong2]
                if strong2 and weak2: strong, weak = strong2, weak2
        d['keep'], d['move'] = strong, weak
        major = s == 'ela' or any(focus_of.get(b) == 'major' for b in weak)
        nweak = sum(1 for c in d['codes'] if c.get('depth') in WEAK[:3] and base(c['code']) in weak)
        cap = 20 if g in ('k', '1') else 25 if g == '2' else 35
        d['est'] = d['minutes'] + 5 * nweak
        if not weak: d['call'], d['why'] = 'holds', 'every code reads as taught'
        elif d['band']: d['call'], d['why'] = 'fix first', 'a band tool: its spec gets a path for this grade first, and it is judged again after the re-read'
        elif d['est'] <= cap + 5 and d['est'] > cap: d['call'], d['why'] = 'room', '%d weak codes at about five minutes each bring it to about %d minutes against a sitting of %d: too close to call from the rows, so fix it inside the tool and judge again at the re-read' % (nweak, d['est'], cap)
        elif d['est'] <= cap: d['call'], d['why'] = 'room', '%d weak codes at about five minutes each bring it to about %d minutes, inside one sitting of %d: fix it inside the tool' % (nweak, d['est'], cap)
        elif not strong: d['call'], d['why'] = 'fix first', 'nothing reads as taught yet, so there is no line to split along: fix the spec, then judge again'
        elif s == 'math' and g in ('9', '10', '11', '12'): d['call'], d['why'] = 'later', 'high school math waits until grade 4 math is proved'
        elif not major: d['call'], d['why'] = 'later', 'supporting or additional work: a second tool waits until the major modules are built'
        else: d['call'] = 'ask'
    # two-topic math modules
    two = []
    if s == 'math':
        for m in own:
            bs = [b for b in (base(x) for x in standards_of(m)) if b in cluster_of]
            def dom(b):
                cl = cluster_of[b]; p = cl.split('.')
                return cl if (len(p) > 2 and p[1] == 'MD') else (p[0] if '-' in p[0] else p[1])
            doms = list(dict.fromkeys(dom(b) for b in bs))
            if len(doms) < 2: continue
            for d in [x for x in T if x['module'] is m]:
                per = {}
                for dm in doms:
                    cs = [c for c in d['codes'] if base(c['code']) in bs and dom(base(c['code'])) == dm and c.get('depth') != 'claimed']
                    per[dm] = cs
                if sum(1 for v in per.values() if v) < 2: continue
                weakest = min((dm for dm in per if per[dm]), key=lambda dm: (max(1 if c.get('depth') == 'taught' else 0 for c in per[dm]), sum(c.get('items') or 0 for c in per[dm])))
                short_ = not any(c.get('depth') == 'taught' for c in per[weakest]) or sum(c.get('items') or 0 for c in per[weakest]) < 5
                est = d['minutes'] + (10 if short_ else 0)
                wb = list(dict.fromkeys(base(c['code']) for c in per[weakest]))
                two.append((m, d, wb, est, est > 35))
                if est > 35 and d['call'] in ('keep', 'holds') and key not in HAND:
                    d['keep'] = [b for b in dict.fromkeys(base(c['code']) for c in d['codes'] if c.get('depth') != 'claimed') if b not in wb]
                    d['move'] = wb
                    if g in ('9', '10', '11', '12'): d['call'], d['why'] = 'later', 'high school math waits until grade 4 math is proved'
                    elif any(focus_of.get(b) == 'major' for b in wb): d['call'] = 'ask'
                    else: d['call'], d['why'] = 'later', 'two topics, and by the rule two tools; supporting or additional work, so the second tool waits until the major modules are built'
    # decisions on file win
    for d in T:
        x = DEC.get((key, d['tool']))
        if x:
            d['call'] = {'approved': 'approved', 'asked': 'ask', 'hold': 'holds', 'declined': 'holds'}.get(x['call'], d['call'])
            if x['call'] in ('hold', 'declined'): d['why'] = x.get('note') or d['why']
            d['note'] = x.get('note', '')
    return {'key': key, 's': s, 'g': g, 'own': own, 'band': band, 'cov': cr, 'T': T, 'two': two, 'isband': isband, 'filt': filt}

def depth_words(d, bs):
    out = []
    for b in bs:
        ds = [c.get('depth') for c in d['codes'] if base(c['code']) == b]
        it = sum(c.get('items') or 0 for c in d['codes'] if base(c['code']) == b)
        w = 'practice only' if 'practiced' in ds and not {'taught', 'explored'} & set(ds) else 'only shown' if not {'taught', 'explored', 'practiced'} & set(ds) else 'partly taught'
        out.append('%s %s (%d item%s)' % (L(b), w, it, '' if it == 1 else 's'))
    return '; '.join(out)

def write(C):
    s, g, T = C['s'], C['g'], C['T']
    P = []
    P.append('# Shape: %s\n' % cname(s, g))
    P.append('Written %s by scripts/shape_courses.py from the ledger, the rows and the spec sort. Only the rule-based parts of '
             'Shape are here: load, where a second tool is called for, modules with two topics, and the spec work that '
             'follows. No spec was read for this file. Nothing is built, cut or split by it.\n' % TODAY)
    P.append(TRUST.get(s, ROUGH) + '\n')
    st = collections.Counter(r['status'] for r in C['cov'])
    stages = collections.Counter(d['stage'] for d in T)
    sorts = collections.Counter(d['sort'] for d in T)
    P.append('## Where the course stands\n')
    line = '%d modules of its own' % len(C['own'])
    if C['band']: line += ' and %d band modules that carry its standards' % len(C['band'])
    line += ', %d tools (%s). ' % (len(T), ', '.join('%d %s' % (v, k) for k, v in stages.most_common()))
    line += 'Of %d standards: %s. ' % (len(C['cov']), ', '.join('%d %s' % (st[k], {'full': 'taught in full', 'nearly': 'nearly', 'part': 'part', 'practice': 'practice only', 'shown': 'shown', 'none': 'not taught'}.get(k, k)) for k in ('full', 'nearly', 'part', 'practice', 'shown', 'none', 'not read', 'no module') if st[k]))
    line += 'Specs: %s. ' % ', '.join('%d %s' % (v, k) for k, v in sorts.most_common() if k)
    nd = sum(1 for d in T if d['done'])
    if nd: line += '%d already fixed by Sara. ' % nd
    tot = sum(d['n'] for d in T)
    line += 'Counting lettered parts, the tools carry %d codes between them.' % tot
    P.append(line + '\n')
    if C['isband'] and s == 'ela':
        P.append('This is a band: each tool here serves three or four grades, and belongs to each of those grade courses. The '
                 'shape calls for these tools are made in the grade files, one grade at a time. The load column counts the '
                 'most codes a tool carries for any one grade.\n')
    # module table
    P.append('## Modules, standards and load\n')
    P.append('| Module | Standards | %sTool | Codes, minutes | Reads as |' % ('Weight | ' if s == 'math' else ''))
    P.append('|---|---|%s---|---|---|' % ('---|' if s == 'math' else ''))
    exp = {base(r['standard']) for r in C['cov']}
    stat = {base(r['standard']): r['status'] for r in C['cov']}
    for d in T:
        m = d['module']
        stds = [x for x in standards_of(m) if not C['filt'] or base(x) in exp or base(x) not in text_of]
        w = ''
        if s == 'math':
            fs = list(dict.fromkeys(focus_of.get(base(x), '') for x in stds)); fs = [f for f in fs if f]
            w = ', '.join('widely needed' if f == 'wap' else f for f in fs) + ' | '
        rd_ = collections.Counter(stat.get(base(x), '') for x in stds); rd_.pop('', None)
        reads = ', '.join('%d %s' % (v, k) for k, v in rd_.most_common())
        P.append('| %s%s | %s | %s%s%s | %d in %s%s | %s |' % (m['title'], ' (band %s)' % m['grade'] if d['band'] else '', fmt(stds), w,
                 d['title'], '' if d['stage'] == 'spec' else ' (%s)' % d['stage'], d['n'], d['minutes'] or '?', ' **loaded**' if d['flag'] else ' (long)' if d['long'] else '', reads))
    P.append('')
    notes = [(m, shared_notes[m['module_id']]) for m in C['own'] if shared_notes.get(m['module_id'])]
    if s == 'math':
        sp = [m for m in C['own'] if m['module_id'] in spell]
        if sp: P.append('%d modules listed whole clusters; each now lists its own standards%s.' % (len(sp), ' (applied to data/modules.csv)' if True else ''))
        for m, ns in notes: P.append('- %s: %s.' % (m['title'], '; '.join(ns)))
        if sp or notes: P.append('')
    if s in ('math', 'ela'):
        seen = collections.defaultdict(list)
        for m in C['own'] + C['band']:
            for x in standards_of(m):
                if base(x) in exp: seen[x].append(m['title'])
        dup = {x: v for x, v in seen.items() if len(v) > 1}
        if dup:
            P.append('Standards listed by two modules (each needs one home, or its lettered parts shared out, when the specs are re-read): '
                     + '; '.join('%s (%s)' % (x, ' and '.join(v)) for x, v in dup.items()) + '.\n')
    # calls
    ask = [d for d in T if d['call'] == 'ask']; appr = [d for d in T if d['call'] == 'approved']
    later = [d for d in T if d['call'] == 'later']; fixf = [d for d in T if d['call'] == 'fix first']; holds = [d for d in T if d['call'] == 'holds']
    P.append('## Second tools\n')
    if not C['filt']:
        loaded = [d for d in T if d['flag']]
        if loaded:
            P.append('Loaded tools (over four codes): ' + ', '.join('%s (%d in %d)' % (d['title'], d['n'], d['minutes']) for d in loaded)
                     + '. No second tool is proposed from a rough read. These are the first tools to look at when this subject\'s standard text is wired in and the specs are fixed.\n')
        else: P.append('No tool carries more than four codes. Nothing to propose.\n')
    elif C['isband']:
        P.append('Made in the grade files.\n')
    else:
        room = [d for d in T if d['call'] == 'room']
        if not (ask or appr or later or fixf or holds or room): P.append('No tool carries more than four codes. Every tool keeps its load.\n')
        for i, d in enumerate(ask, 1):
            P.append('%d. **%s (Desk).** %s carries %d codes in %d minutes: %s. Fixing those inside the tool puts it at about %d minutes. Shape: %s keeps %s; a new lesson tool in the same module takes %s (%s).'
                     % (i, d['module']['title'], d['title'], d['n'], d['minutes'], depth_words(d, d['move']), d.get('est', d['minutes'] + 10), d['title'], fmt([L(b) for b in d['keep']]),
                        fmt([L(b) for b in d['move']]), topic(d['move'][0])))
        for d in appr:
            P.append('- **%s: decided.** %s' % (d['module']['title'], d.get('note', '')))
        for d in later:
            P.append('- %s (%s, %d codes in %d minutes): would keep %s and hand %s to a second tool. Not asked: %s.'
                     % (d['title'], d['module']['title'], d['n'], d['minutes'], fmt([L(b) for b in d['keep']]), fmt([L(b) for b in d['move']]), d['why']))
        for d in fixf:
            P.append('- %s (%s, %d codes in %d minutes): %s.' % (d['title'], d['module']['title'], d['n'], d['minutes'], d['why']))
        for d in room:
            P.append('- %s (%s, %d codes in %d minutes): no second tool. %s.' % (d['title'], d['module']['title'], d['n'], d['minutes'], d['why'][:1].upper() + d['why'][1:]))
        for d in holds:
            P.append('- %s (%s, %d codes in %d minutes): holds. %s.' % (d['title'], d['module']['title'], d['n'], d['minutes'], d['why'][:1].upper() + d['why'][1:]))
        lg = [d for d in T if d['long'] and not d['flag']]
        if lg: P.append('\nLong sittings (over 35 minutes, four codes or fewer): ' + ', '.join('%s (%d)' % (d['title'], d['minutes']) for d in lg)
                        + '. Not a second-tool question: each spec says where the sitting breaks in two.')
        P.append('')
    if C['two']:
        P.append('## Modules with two topics\n')
        P.append('The rule: one module, two tools when the topics sit in separate modes or cannot both be taught in one sitting of about 35 minutes; otherwise one tool. Separate modes need a spec read, so only the time test is applied here.\n')
        for m, d, wb, est, over in C['two']:
            P.append('- %s: the weaker topic is %s. Giving it a model and five items puts %s at about %d minutes: %s.'
                     % (m['title'], fmt([L(b) for b in wb]), d['title'], est, 'two tools' if over else 'one tool holds'))
        P.append('')
    # practice
    P.append('## Practice\n')
    stn = [d for d in T if d['use'] in ('station', 'ongoing')]
    fl = [L(base(r['standard'])) for r in C['cov'] if re.search(r'\b[Ff]luen', text_of.get(base(r['standard']), ''))] if s == 'math' else []
    line = ('Stations and ongoing tools: ' + ', '.join(d['title'] for d in stn) + '. ') if stn else 'No station or practice tool. '
    line += 'Practice otherwise comes from worksheets and Recess. '
    if fl: line += 'Standards that ask for fluency by name, which get worksheet presets first: ' + fmt(fl) + '.'
    P.append(line + '\n')
    # spec work
    P.append('## Spec work this leaves (for Sara)\n')
    fixfile = 'docs/spec-fixes/courses/%s.md' % C['key']
    wait = [d for d in T if d['call'] == 'ask']
    now = [d for d in T if d['call'] != 'ask' and not d['done']]
    grp = collections.OrderedDict((k, [d for d in now if d['sort'] == k]) for k in ('rework', 'small addition', 'fine'))
    P.append('Fix lists: %s%s.\n' % (fixfile, (' and, for band tools, ' + ', '.join(sorted({'docs/spec-fixes/courses/%s-%s.md' % (s, d['module']['grade']) for d in T if d['band']}))) if C['band'] else ''))
    for k, ds in grp.items():
        if ds: P.append('- %s (%d): %s.' % ({'rework': 'Rework', 'small addition': 'Small addition', 'fine': 'Sorts fine, confirm only'}[k], len(ds), ', '.join(d['title'] + (' (band)' if d['band'] else '') for d in ds)))
    if appr: P.append('- Fix on the approved split: ' + ', '.join(d['title'] for d in appr if not d['done']) + '.')
    if wait: P.append('- Wait for Cory\'s answer on the Desk: ' + ', '.join(d['title'] for d in wait) + '.')
    dn = [d for d in T if d['done']]
    if dn: P.append('- Already logged in done.txt: ' + ', '.join(d['title'] for d in dn) + '.')
    if C['band'] and s == 'ela': P.append('- Each band spec gives %s its own path: its texts, its wording of the standard, five or more items.' % gname(g))
    P.append('')
    # build order
    P.append('## Build order by value\n')
    if s == 'math':
        def rank(d):
            fs = {focus_of.get(base(x), '') for x in standards_of(d['module'])}
            return 0 if 'major' in fs or 'wap' in fs else 1 if 'supporting' in fs else 2 if 'additional' in fs else 1
        for i, lab in enumerate(('Major work' if g not in ('9', '10', '11', '12') else 'Widely needed', 'Supporting', 'Additional' if g not in ('9', '10', '11', '12') else 'The rest')):
            ds = [d for d in T if rank(d) == i]
            if g in ('9', '10', '11', '12') and i == 1: lab = 'The rest'
            if ds: P.append('%d. %s: %s' % (len([1 for j in range(i + 1) if [d for d in T if rank(d) == j]]), lab, ', '.join(d['title'] + (' and its second tool' if d['call'] in ('ask', 'approved') else '') for d in ds)))
    elif s == 'ela':
        def strand(d):
            xs = [x for x in standards_of(d['module']) if base(x) in exp] or standards_of(d['module'])
            p = xs[0].split('.')[0] if xs else ''
            return {'RL': 0, 'RI': 0, 'RF': 0, 'W': 1, 'L': 2, 'SL': 3}.get(p, 3)
        for i, lab in enumerate(('Reading', 'Writing', 'Language', 'Speaking and listening')):
            ds = [d for d in T if strand(d) == i]
            if ds: P.append('%d. %s: %s' % (i + 1, lab, ', '.join(d['title'] + (' and its second tool' if d['call'] in ('ask', 'approved') else '') for d in ds)))
    else:
        P.append('Not ordered. This subject has no weight data on file; the order is set when its standard text is wired in.')
    P.append('')
    if ask: P.append('Exceptions for Cory are on Desk card q-shape-%s.\n' % C['key'])
    else: P.append('No exception for Cory in this course: no Desk card.\n')
    io.open(os.path.join(SHAPE, C['key'] + '.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(P).rstrip('\n') + '\n')

ALL = [shape(s, g) for s, g in courses]
for C in ALL:
    if C['key'] not in HAND: write(C)

# ---- shape.csv: one row per tool per course -------------------------------------------------------------------
with io.open(os.path.join(SHAPE, 'shape.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['course', 'tool', 'title', 'module', 'band', 'stage', 'codes', 'minutes', 'loaded', 'call', 'keeps', 'second_tool_takes', 'sort', 'done'])
    for C in ALL:
        for d in C['T']:
            w.writerow([C['key'], d['tool'], d['title'], d['module']['module_id'], 'band' if d['band'] else '', d['stage'], d['n'], d['minutes'],
                        'yes' if d['flag'] else '', d['call'], ' '.join(L(b) for b in d['keep']), ' '.join(L(b) for b in d['move']), d['sort'], d['done']])

# ---- Desk cards -----------------------------------------------------------------------------------------------
cards = []
for C in ALL:
    if C['key'] in HAND: continue
    ask = [d for d in C['T'] if d['call'] == 'ask']
    if not ask: continue
    st = collections.Counter(r['status'] for r in C['cov'])
    qs = []
    for d in ask:
        qs.append({'q': '%s carries %d codes in %d minutes (%s). Let it keep %s, and add a lesson tool in the same module for %s (%s)?'
                        % (d['title'], d['n'], d['minutes'], depth_words(d, d['move']), fmt([L(b) for b in d['keep']]), fmt([L(b) for b in d['move']]), topic(d['move'][0])),
                   'pick': 'Yes.' + (' Major work.' if C['s'] == 'math' else '') + ' Fixing it inside the tool would run to about %d minutes.' % d.get('est', d['minutes'] + 10)})
    cards.append({'id': 'q-shape-' + C['key'], 'title': 'Shape: ' + cname(C['s'], C['g']), 'subject': '%s, %s' % (NAME[C['s']][:1].upper() + NAME[C['s']][1:], gname(C['g'])),
                  'status': 'question', 'built': 'Nov 11',
                  'changed': '%s is shaped by rule (docs/agents/catalog/shape/%s.md): %d tools, %d of %d standards read as taught in full. No tool is cut or merged. '
                             'Each question is a second lesson tool in the same module, no split, proposed because one tool carries more than a sitting can teach and part of its load does not read as taught. '
                             'These come from the catalog rows, not from a fresh read of each spec.' % (cname(C['s'], C['g'])[:1].upper() + cname(C['s'], C['g'])[1:], C['key'], len(C['T']), st['full'], len(C['cov'])),
                  'questions': qs})
json.dump(cards, io.open(os.path.join(SHAPE, 'cards.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---- summary --------------------------------------------------------------------------------------------------
tally = collections.Counter(d['call'] for C in ALL for d in C['T'] if not C['isband'] or C['s'] not in ('math', 'ela'))
print('courses', len(ALL), 'cards', len(cards), 'questions', sum(len(c['questions']) for c in cards))
print('calls', dict(tally))
if '--list' in sys.argv:
    for C in ALL:
        for d in C['T']:
            if d['call'] in ('ask', 'later', 'room'):
                print('%-10s %-9s %-28s %d/%d keep[%s] move[%s]' % (C['key'], d['call'], d['tool'][:28], d['n'], d['minutes'], fmt([L(b) for b in d['keep']]), fmt([L(b) for b in d['move']])))

# ---- docs/spec-fixes/NEXT.md: what Sara works next --------------------------------------------------------------
BY = {C['key']: C for C in ALL}
seen = set(done)                      # a tool is listed once, in the first course of the order that holds it
def left(key):
    out = [d for d in BY[key]['T'] if d['tool'] not in seen]
    seen.update(d['tool'] for d in out)
    return out
def names(ds): return ', '.join('%s (`%s`)' % (d['title'], d['tool']) for d in ds) or 'none'
N = []
N.append('# What Sara works next\n')
N.append('Rebuilt %s by scripts/shape_courses.py; do not edit by hand. How to fix a spec: README.md. What each spec needs: '
         'courses/<course>.md. What Shape decided for a course: ../agents/catalog/shape/<course>.md. Log every spec you finish '
         'in done.txt.\n' % TODAY)
total = len(rows); fine_left = sum(1 for t in rows if t not in done and (sort.get(t) or {}).get('sort') == 'fine')
appr_all = [(C['key'], d) for C in ALL for d in C['T'] if d['call'] == 'approved']
ask_all = [(C['key'], d) for C in ALL for d in C['T'] if d['call'] == 'ask']
N.append('## Where things stand\n')
N.append('- %d specs in the catalog. %d are logged fixed in done.txt (grade 4 math and grade 6 ELA), none reviewed yet. %d remain, and %d of those sort fine and only need confirming.'
         % (total, len(done), total - len(done), fine_left))
N.append("- **Spec fixing has stopped** (Cory, 2026-11-11 night, accepting the cold strategic review; it had been set to stop after batch 4). Do not work the batches below. Old tools and specs are now sorted by demand (BASELINE rule 26): a spec gets work only when a unit plan names its tool. Sara's work is docs/courses/NEXT-SPINES.md.")
N.append('- From now on every spec you touch also carries the three hooks in README.md ("The end standard"): an unaided check the teacher can see, English learner supports, and access. The 22 specs already logged get them in batch 1.')
N.append('- Cory approved %d second lesson tools. Each one takes codes away from an existing tool, so that tool\'s spec gets lighter. The new tools are not written yet and are not your work now: each gets an idea and a spec when its course is built.' % len(appr_all))
N.append(('- %d more second tools are on the Desk waiting for Cory. Leave those specs until he answers.' % len(ask_all)) if ask_all else '- No second tool is waiting on the Desk: every one proposed so far is approved.')
N.append('- A sitting of 10 to 14 specs is a good batch. One course at a time, and finish a course before starting the next.\n')
N.append('## Batch 1: close the two proving courses (11 specs)\n')
N.append('These stand between the two courses and their final review.\n')
N.append('- Re-read found still open: Argument X-Ray (`argument-x-ray`: add a model, reach five arguments, make a rerun of the scan cost something), Unit Ladder (`unit-ladder`: the spec is too thin to judge; write it out in full), Skate Park Angles (`skate-park-angles`: bring 4.MD.C.5b to five items; the line plot lesson goes to a new tool Cory approved, so Jump Log stays as it is and the spec calls it practice for 4.MD.B.4).')
N.append('- Fix again on the approved split, dropping the codes the new tool takes and using the room for more items: Recipe Scaler (`recipe-scaler`, keeps 4.NF.B.3), Area Model Builder (`area-model-builder`, keeps 4.NBT.B.5), Debate Prep Desk (`debate-prep-desk`, keeps W.6.1a and b).')
N.append('- Small parts the re-read still found: Stadium Count (`stadium-count`: 4.NBT.A.3, rounds to the ten and to the million), Quilt Block Studio (`quilt-block-studio`: 4.G.A.1, points, rays and lines), Plot Rollercoaster (`plot-rollercoaster`) and Book Group Table (`book-group-table`): see courses/ela-6.md.')
N.append('- Then Claude re-reads both courses and you run FINAL-REVIEW.md on them, starting with Argument X-Ray, Skate Park Angles and Unit Ladder.\n')
b2 = [d for d in BY['ela-6']['T'] if d['band'] and d['tool'] not in seen]; seen.update(d['tool'] for d in b2)
N.append('## Batch 2: the grade 6 to 8 ELA band (%d specs)\n' % len(b2))
N.append('Fix lists: courses/ela-6-8.md. These are the whole gap left in grade 6 ELA. Each tool serves grades 6, 7 and 8, so give each '
         'spec three paths in one pass (grade 6, grade 7, grade 8): that grade\'s texts, that grade\'s wording of the standard, five '
         'or more items each. Doing all three now closes the band for grades 7 and 8 as well.\n')
N.append(names(b2) + '.\n')
for i, (key, lab) in enumerate((('math-5', 'grade 5 math'), ('math-3', 'grade 3 math')), 3):
    ds = left(key)
    N.append('## Batch %d: %s (%d specs)\n' % (i, lab, len(ds)))
    N.append('Fix list: courses/%s.md. Shape: ../agents/catalog/shape/%s.md.\n' % (key, key))
    ap = [d for d in ds if d['call'] == 'approved']; rest = [d for d in ds if d['call'] != 'approved']
    N.append('- On the approved split: ' + '; '.join('%s (`%s`): %s' % (d['title'], d['tool'], d.get('note', '')) for d in ap))
    N.append('- Fix: ' + names([d for d in rest if d['sort'] != 'fine']) + '.')
    N.append('- Confirm only: ' + names([d for d in rest if d['sort'] == 'fine']) + '.\n')
N.append('## After batch 4\n')
N.append('Specs stay stopped. Your work moves to drafts of the layers under a course (Cory, 2026-11-11): the grade 3 and grade 5 math spines, the rubric files and approach pages for science and English language arts, the grade 6 ELA text plan, then more math spines. The list, the order and how each piece is made: [../courses/NEXT-SPINES.md](../courses/NEXT-SPINES.md). It can start before batch 4 ends if a batch is waiting on something. Unit pieces (teacher pages, checks with their keys, sentence frames) come after the unit plan fields are fixed.\n')
N.append('## On hold: every other course\n')
N.append('Do not start these. They open, in this order, once grade 4 math is proved. The table is here so the size of what is left stays in view. A band tool is counted once, with the first course that uses it. "Wait" means a Desk card is open on that tool.\n')
N.append('| Order | Course | Specs left | Rework | Small addition | Confirm only | Wait | Shape file |')
N.append('|---|---|---|---|---|---|---|---|')
order = ['math-6', 'math-2', 'math-7', 'math-1', 'math-8', 'math-k', 'ela-7', 'ela-8', 'ela-5', 'ela-4', 'ela-3', 'ela-2', 'ela-1', 'ela-k',
         'ela-9', 'ela-10', 'ela-11', 'ela-12', 'math-9', 'math-10', 'math-11', 'math-12']
order += [C['key'] for C in ALL if C['s'] in ('science', 'social-studies')]
rough_from = len(order)
order += [C['key'] for C in ALL if C['key'] not in order and C['key'] not in HAND]
n = 0
for key in order:
    ds = left(key)
    if not ds: continue
    n += 1
    if order.index(key) >= rough_from and not rough_from < 0:
        rough_from = -1
        N.append('| | **Below this line: parked. These subjects stay in the end goal, but nothing is spent on them until the core courses are proved.** | | | | | | |')
    c = collections.Counter(d['sort'] for d in ds if d['call'] != 'ask')
    N.append('| %d | %s | %d | %d | %d | %d | %s | [%s](../agents/catalog/shape/%s.md) |' % (n, cname(BY[key]['s'], BY[key]['g']), len(ds), c['rework'], c['small addition'], c['fine'],
             ', '.join(d['title'] for d in ds if d['call'] == 'ask') or '', key, key))
N.append('')
N.append('High school math sits after ELA on purpose: it waits until grade 4 math is proved.\n')
N.append('## How the total changed\n')
N.append('- Before Shape the plan was 800 specs in catalog order, live rework tools first. Now it is four batches (about 46 specs), then a stop until one course is proved, with %d specs reopened on a lighter load and %d on hold for a Desk answer.' % (len(appr_all), len(ask_all)))
N.append('- New specs that Shape adds for later: %d approved, up to %d more if Cory says yes on the Desk. None is yours to write yet.' % (len(appr_all), len(ask_all)))
N.append('- Approved: ' + '; '.join('%s' % d.get('note', d['title']) for _, d in appr_all))
N.append('- On the Desk: ' + ('; '.join('%s (%s)' % (d['title'], k) for k, d in ask_all) or 'nothing') + '.')
io.open(os.path.join(ROOT, 'docs', 'spec-fixes', 'NEXT.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(N).rstrip('\n') + '\n')
