"""Load counts per band: actions, setting groups, formats and repeated title words. Usage: python scripts/overlap/stats.py [--after]"""
import collections, re, sys
from common import load, BANDS

rows = load(after='--after' in sys.argv)
STOP = {'the', 'of', 'and', 'a', 'to', 'or', 'my', 'in', 'on', 'me', 'it', 'i', 'is', 'for', 'what', 'how', 'who', 'from', 'your', 's', 'vs', 'el', 'la', 'de', 'en'}
for b in BANDS:
    rs = [r for r in rows if b in r['bands']]
    print(f'== {b}: {len(rs)} tools (K-12 and 6-12 tools included)')
    print('  actions :', collections.Counter(r['action'] for r in rs).most_common(8))
    print('  formats :', collections.Counter(r['format'] for r in rs).most_common(6))
    sg = collections.Counter(r['setting_group'] for r in rs if r['setting_group'] != 'generic')
    print('  settings 4+:', [(k, v) for k, v in sg.most_common() if v >= 4])
    tw = collections.defaultdict(list)
    for r in rs:
        for w in set(re.findall(r"[a-z]+", r['title'].lower())) - STOP:
            tw[w].append(r['tool_id'])
    print('  title words 2+:', {w: v for w, v in sorted(tw.items()) if len(v) >= 2})
