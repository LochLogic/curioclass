r"""The spec fix list (docs/spec-fixes/): what every spec needs before it meets the teaching test. No tokens.

    python scripts/spec_fixes.py

Run scripts/coverage_ledger.py and scripts/catalog_maps.py first. Reads every extract row
(docs/agents/catalog/rows/*.jsonl), the spec sort (docs/agents/catalog/tables/spec-sort.csv) and the hand-kept
docs/spec-fixes/done.txt, and writes:

  docs/spec-fixes/courses/<subject>-<grade>.md   one file per course: every tool, the kinds of fix it needs, and
                                                 the exact parts the read found missing, code by code
  docs/spec-fixes/fix-list.csv                   one row per tool, one column per kind of fix, plus its status
  docs/spec-fixes/INDEX.md                       one line per course, with counts and how many are done

README.md, FINAL-REVIEW.md and done.txt in that folder are written by hand and never touched here.
done.txt lines: `<tool-id> fixed|reviewed <date> <note>`. The last line for a tool wins.
"""
import csv, glob, io, json, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, 'docs', 'agents', 'catalog')
OUT = os.path.join(ROOT, 'docs', 'spec-fixes')
os.makedirs(os.path.join(OUT, 'courses'), exist_ok=True)

def rd(path):
    with io.open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return list(csv.DictReader(f))

ORDER = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'k-2', '3-5', '6-8', '6-12', '9-12', 'k-12']
gkey = lambda g: ORDER.index(g) if g in ORDER else 99
KINDS = [('write_spec', 'Write the spec'), ('key_step', 'Hand the key step to the student'),
         ('guessable_check', 'Close the guessable check'), ('missing_part', 'Add the missing part'),
         ('model_or_guide', 'Add a model or a guide'), ('add_check', 'Add a check'),
         ('more_items', 'Reach five items that differ'), ('main_path', 'Put it on the main path'),
         ('claimed', 'Teach the code or drop it'), ('sensitive', 'Sensitivity read'), ('sources', 'Source the facts')]
NAME = dict(KINDS)
PROVE = {('math', '4'), ('ela', '6')}

modules = {m['module_id']: m for m in rd('data/modules.csv')}
concepts = {c['tool_id']: c for c in rd('data/tools-concepts.csv')}
sort = {r['tool']: r for r in rd('docs/agents/catalog/tables/spec-sort.csv')}
rows = {}
for f in sorted(glob.glob(os.path.join(CAT, 'rows', '*.jsonl'))):
    for ln in io.open(f, encoding='utf-8'):
        if ln.strip():
            r = json.loads(ln); rows[r['id']] = r
done = {}
dp = os.path.join(OUT, 'done.txt')
if os.path.exists(dp):
    for ln in io.open(dp, encoding='utf-8'):
        p = ln.split(None, 3)
        if len(p) >= 2 and not ln.startswith('#') and p[1] in ('fixed', 'reviewed'):
            done[p[0]] = (p[1], ' '.join(p[2:]))

def fixes(r):
    """-> (set of kinds, list of per-code lines)"""
    k, lines = set(), []
    flags = r.get('flags') or []
    if 'spec-thin' in flags or r.get('stage') == 'idea': k.add('write_spec')
    if r.get('beatable'): k.add('guessable_check')
    if 'sensitive' in flags: k.add('sensitive')
    if 'facts-unsourced' in flags: k.add('sources')
    for c in r.get('codes', []):
        d, todo = c.get('depth'), []
        if d == 'claimed': k.add('claimed'); todo.append('nothing the student does matches this code: teach it or drop it')
        elif d == 'touched' or c.get('on_path') is False: k.add('main_path'); todo.append('off the main path or can be skipped: put it on the path')
        if d == 'shown' or c.get('key_step') == 'tool':
            k.add('key_step'); todo.append('the tool does the "%s" step: the student must do it' % (c.get('verb') or 'key'))
        if d == 'practiced':
            if c.get('support') == 'none': k.add('model_or_guide'); todo.append('no model or guide: add one')
            if c.get('check') == 'none': k.add('add_check'); todo.append('no check: add one where thinking is cheaper than guessing')
        if d in ('taught', 'practiced', 'shown') and 0 < (c.get('items') or 0) < 5:
            k.add('more_items'); todo.append('only %d items: reach five or more that differ' % c['items'])
        parts = [p for p in (c.get('parts_missing') or []) if p]
        if parts and c.get('missing_weight') == 'core' and d != 'claimed': k.add('missing_part')
        if d == 'explored' and c.get('unit_adds'): todo.append('see-why code, fine here; the unit must add: ' + c['unit_adds'])
        if not todo and not parts: continue
        lines.append((c['code'], d, c.get('activity', ''), c.get('where', ''), todo, parts, c.get('missing_weight', '')))
    return k, lines

by_course = collections.defaultdict(list)
out_rows = []
for t, r in rows.items():
    c = concepts[t]; m = modules[c['module_id']]
    k, lines = fixes(r)
    s = sort[t]
    st = done.get(t, ('', ''))
    has_spec = os.path.exists(os.path.join(ROOT, 'tools', t, 'spec.md'))
    if not has_spec: k.add('write_spec')
    e = {'tool': t, 'title': c['title'], 'subject': m['subject'], 'grade': m['grade'], 'module': c['module_id'], 'stage': r.get('stage', ''),
         'sort': s['sort'], 'kinds': k, 'lines': lines, 'row': r, 'status': st[0], 'note': st[1], 'has_spec': has_spec}
    by_course[(m['subject'], m['grade'])].append(e)
    o = {'tool': t, 'title': c['title'], 'subject': m['subject'], 'grade': m['grade'], 'module': c['module_id'], 'stage': e['stage'], 'sort': s['sort']}
    for key, _ in KINDS: o[key] = 'x' if key in k else ''
    o['status'] = st[0]; o['note'] = st[1]
    out_rows.append(o)
out_rows.sort(key=lambda x: (x['subject'], gkey(x['grade']), x['module'], x['tool']))
with io.open(os.path.join(OUT, 'fix-list.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, list(out_rows[0].keys()), lineterminator='\n'); w.writeheader(); w.writerows(out_rows)

BANDTOOLS = collections.defaultdict(list)          # course -> [(title, band grade)], from the shape pass
sp = os.path.join(CAT, 'shape', 'shape.csv')
if os.path.exists(sp):
    for x in csv.DictReader(io.open(sp, encoding='utf-8')):
        if x['band']: BANDTOOLS[x['course']].append((x['title'], modules[x['module']]['grade']))
STAGE = {'spec': 'spec only', 'built': 'built (the code changes after the spec)', 'live': 'LIVE (the code changes after the spec)', 'idea': 'idea only'}
index = ['# The spec fix list, by course\n',
         'Built by scripts/spec_fixes.py. Start with README.md. The two proving courses come first, then every other '
         'course by subject and grade.\n',
         '| Course | Tools | Fine | Small addition | Rework | Write the spec | Live | Fixed | Reviewed |', '|---|---|---|---|---|---|---|---|---|']
courses = sorted(by_course, key=lambda c: (c not in PROVE, c[0], gkey(c[1])))
tot = collections.Counter()
for (s, g) in courses:
    es = sorted(by_course[(s, g)], key=lambda e: ({'rework': 0, 'small addition': 1, 'fine': 2}[e['sort']], e['module'], e['tool']))
    n = collections.Counter(e['sort'] for e in es)
    kc = collections.Counter(k for e in es for k in e['kinds'])
    P = ['# Spec fixes: %s, grade %s\n' % (s, g),
         '%d tools: %d rework, %d small addition, %d fine. How to use this file: ../README.md. '
         'When a spec is fixed, add a line to ../done.txt.\n' % (len(es), n['rework'], n['small addition'], n['fine']),
         'Kinds of fix in this course: ' + (', '.join('%s (%d)' % (NAME[key], kc[key]) for key, _ in KINDS if kc[key]) or 'none') + '.\n']
    bt = BANDTOOLS.get('%s-%s' % (s, g))
    P.append('Shape for this course: ../../agents/catalog/shape/%s-%s.md.%s\n' % (s, g, (' Band tools that are also part of this course, with their fix lists in ' + ', '.join(sorted({'%s-%s.md' % (s, b) for _, b in bt})) + ': ' + ', '.join(t for t, _ in bt) + '.') if bt else ''))
    for e in es:
        r = e['row']
        P.append('## %s%s\n' % (e['title'], '  [%s]' % e['status'].upper() if e['status'] else ''))
        P.append('- Spec: `tools/%s/%s` . Module: %s. Stage: %s. Sort: **%s**.' % (
            e['tool'], 'spec.md' if e['has_spec'] else '(no spec.md yet)', e['module'], STAGE.get(e['stage'], e['stage']), e['sort']))
        P.append('- Fixes: ' + (', '.join(NAME[key] for key, _ in KINDS if key in e['kinds']) or 'none found; confirm at final review') + '.')
        if e['note']: P.append('- Note: ' + e['note'])
        if r.get('beatable'):
            P.append('- Checks a student can pass by guessing:')
            P += ['  - ' + ' '.join(b.split()) for b in r['beatable']]
        for code, d, act, where, todo, parts, wt in e['lines']:
            P.append('- **%s** (%s%s): %s' % (code, d, ', in ' + where if where else '', act))
            P += ['  - To do: ' + x for x in todo]
            if parts:
                P.append('  - Parts of the standard the student never does (%s):' % ('must add' if wt == 'core' else 'small, add if cheap'))
                P += ['    - ' + ' '.join(p.split()) for p in parts]
        if r.get('module_codes_untaught'):
            P.append('- The module also lists codes this tool does not carry: ' + ', '.join(r['module_codes_untaught']) + '.')
        if r.get('unsure'):
            P.append('- The read was unsure about (check these against the spec; the read may be wrong):')
            P += ['  - ' + ' '.join(u.split()) for u in r['unsure']]
        P.append('')
    io.open(os.path.join(OUT, 'courses', '%s-%s.md' % (s, g)), 'w', encoding='utf-8', newline='\n').write('\n'.join(P) + '\n')
    fx = sum(1 for e in es if e['status'] == 'fixed'); rv = sum(1 for e in es if e['status'] == 'reviewed')
    index.append('| [%s %s](courses/%s-%s.md)%s | %d | %d | %d | %d | %d | %d | %d | %d |' % (
        s, g, s, g, ' (proving course)' if (s, g) in PROVE else '', len(es), n['fine'], n['small addition'], n['rework'],
        kc['write_spec'], sum(1 for e in es if e['stage'] == 'live'), fx, rv))
    tot.update(k for e in es for k in e['kinds']); tot['tools'] += len(es); tot['fixed'] += fx; tot['reviewed'] += rv
index.append('\n%d tools in %d courses; %d fixed, %d reviewed. By kind of fix: ' % (tot['tools'], len(courses), tot['fixed'], tot['reviewed'])
             + ', '.join('%s %d' % (NAME[key], tot[key]) for key, _ in KINDS) + '.')
io.open(os.path.join(OUT, 'INDEX.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(index) + '\n')
print(index[-1]); print(len(courses), 'course files')
