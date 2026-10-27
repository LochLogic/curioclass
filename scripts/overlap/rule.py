"""Run the clash rule. Usage: python scripts/overlap/rule.py [--after]   (writes docs/agents/overlap/pairs.csv or pairs-after.csv)"""
import csv, io, os, sys
from common import load, pairs, OUT

after = '--after' in sys.argv
rows = load(after=after)
out = pairs(rows)
name = 'pairs-after.csv' if after else 'pairs.csv'
with io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['band', 'tool_a', 'live_a', 'tool_b', 'live_b', 'matched', 'skill_key_a', 'skill_key_b', 'action_a', 'action_b', 'setting_group_a', 'setting_group_b'])
    for band, a, b, m in sorted(out, key=lambda x: (x[0], x[1]['tool_id'], x[2]['tool_id'])):
        w.writerow([band, a['tool_id'], a['live'], b['tool_id'], b['live'], '+'.join(m), a['skill_key'], b['skill_key'],
                    a['action'], b['action'], a['setting_group'], b['setting_group']])
print(f'{len(out)} rule hits -> {name}')
if after:
    new = [p for p in out if p[1]['changed'] or p[2]['changed']]
    print(f'{len(new)} involve a changed tool:')
    for band, a, b, m in new:
        print(' ', band, a['tool_id'], '<>', b['tool_id'], '+'.join(m))
