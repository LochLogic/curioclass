"""Build decisions.json, the decision table and the kept-hits list. Usage: python scripts/overlap/build_decisions.py
Reads decisions_src.py and clusters_meta.py; fills the marked blocks in docs/agents/overlap/clusters.md."""
import io, json, os, re, collections
from common import load, pairs, OUT
from decisions_src import D
from clusters_meta import CLUSTERS, KEEP_REASONS

rows = {r['tool_id']: r for r in load()}
FIXLABEL = {'reshape': 'reshape', 'rename': 'rename (title only)', 'move-to-gap': 'move-to-gap', 'add-standard': 'add a standard to its module',
            'spec-note': 'keep, spec note', 'keep': 'keep'}

def status(r):
    return 'live' if r['live'] == 'y' else 'planned'

# decisions.json
out = []
for d in D:
    r = rows[d['id']]
    out.append(dict(tool_id=d['id'], title=r['title'], band=r['band'], status=status(r), cluster=d['c'], cluster_title=CLUSTERS[d['c']],
                    fix=d['fix'], new_title=d.get('title', ''), new_concept=d.get('concept', ''), options=d.get('options', []), why=d['why']))
io.open(os.path.join(OUT, 'decisions.json'), 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')

def cell(s):
    return s.replace('|', '/').replace('\n', ' ')

def ckey(c):
    return (0 if c.startswith('W') else 1, int(c[1:]))

# decision table
t = ['| tool_id | title | band | status | cluster | suggested fix | new title | new concept line | options |', '|---|---|---|---|---|---|---|---|---|']
for d in sorted(D, key=lambda d: ckey(d['c'])):
    r = rows[d['id']]
    fix = FIXLABEL[d['fix']]
    concept = d.get('concept', '')
    if d['fix'] in ('spec-note', 'keep', 'add-standard', 'rename') and not concept:
        concept = '(unchanged) ' + d['why'] if d['fix'] in ('spec-note', 'add-standard') else '(unchanged)'
    opts = ' OR '.join(d.get('options', []))
    t.append(f"| {d['id']} | {cell(r['title'])} | {r['band']} | {status(r)} | {d['c']} | {fix} | {cell(d.get('title', ''))} | {cell(concept)} | {cell(opts)} |")
table = '\n'.join(t)

# kept rule hits after the fixes
hits = pairs(load(after=True))
lines = []
by_reason = collections.OrderedDict()
unreasoned = []
for band, a, b, m in sorted(hits, key=lambda x: (x[0], x[1]['tool_id'], x[2]['tool_id'])):
    ids = {a['tool_id'], b['tool_id']}
    reason = None
    for e in KEEP_REASONS:
        if ids <= e[0] and (len(e) < 3 or e[2] in ids):
            reason = e[1]; break
    tag = f"{a['tool_id']}{' (live)' if a['live'] == 'y' else ''} and {b['tool_id']}{' (live)' if b['live'] == 'y' else ''} ({band}, {'+'.join(m)})"
    if reason is None:
        unreasoned.append(tag)
    else:
        by_reason.setdefault(reason, []).append(tag)
for reason, tags in by_reason.items():
    lines.append(f"- **{reason}** {'; '.join(tags)}.")
for tag in unreasoned:
    lines.append(f"- **NO REASON YET:** {tag}")
kept = f"After the fixes, the rule finds {len(hits)} pairs. Every one is kept, grouped here by reason:\n\n" + '\n'.join(lines)

NL = chr(10)
# per-cluster fix bullets
VERB = {'reshape': 'reshape', 'rename': 'rename', 'move-to-gap': 'move-to-gap', 'add-standard': 'add a standard',
        'spec-note': 'keep, spec note', 'keep': 'keep'}
fixes = collections.defaultdict(list)
for d in D:
    r = rows[d['id']]
    head = f"- **{d['id']}** ({VERB[d['fix']]})"
    if d.get('title'): head += f": **{d['title']}**."
    elif d['fix'] in ('reshape',): head += ':'
    body = d.get('concept', '')
    if not body: body = d['why']
    line = f"{head} {body}"
    for o in d.get('options', []):
        line += NL + "  - Option: " + o
    fixes[d['c']].append(line)

p = os.path.join(OUT, 'clusters.md')
if os.path.exists(p):
    s = io.open(p, encoding='utf-8').read()
    blocks = [('decision-table', table), ('kept-hits', kept)] + [(f'fixes:{c}', NL.join(v)) for c, v in fixes.items()]
    for name, body in blocks:
        s = re.sub(rf'(<!-- {name}:start -->\n).*?(<!-- {name}:end -->)', lambda m: m.group(1) + body + NL + m.group(2), s, flags=re.S)
    io.open(p, 'w', encoding='utf-8').write(s)

c = collections.Counter(d['fix'] for d in D)
print('decisions:', len(D), dict(c), '| open calls:', sum(1 for d in D if d.get('options')))
print('kept hits:', len(hits), '| without a reason:', len(unreasoned))
for u in unreasoned: print('  ', u)
