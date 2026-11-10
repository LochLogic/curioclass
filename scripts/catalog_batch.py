r"""Catalog review: write the packet an extract agent works from (docs/agents/CATALOG-REVIEW.md, step 1).

    python scripts/catalog_batch.py <name> <subject> <grade> [<subject> <grade> ...] [--size 12] [--live]

Writes docs/agents/catalog/batches/<name>-<n>.md: for each tool its catalog line, module, the module's standards,
its stage, its old overlap tags (for house style) and the files to read. One packet holds at most --size tools.
"""
import csv, os, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
args = sys.argv[1:]
size = 12
if '--size' in args:
    i = args.index('--size'); size = int(args[i + 1]); del args[i:i + 2]
live_only = '--live' in args
if live_only: args.remove('--live')
name, pairs = args[0], list(zip(args[1::2], args[2::2]))
rd = lambda p: list(csv.DictReader(open(ROOT / p, encoding='utf-8')))
mods = {r['module_id']: r for r in rd('data/modules.csv')}
tags = {r['tool_id']: r for r in rd('docs/agents/overlap/tags.csv')}
def stage(t):
    d = ROOT / 'tools' / t
    for f, s in (('tool.json', 'live'), ('src.html', 'built'), ('spec.md', 'spec'), ('idea.md', 'idea')):
        if (d / f).exists(): return s
    return 'concept'
tools = [t for t in rd('data/tools-concepts.csv') if (mods[t['module_id']]['subject'], mods[t['module_id']]['grade']) in pairs]
if live_only: tools = [t for t in tools if stage(t['tool_id']) == 'live']
out = ROOT / 'docs/agents/catalog/batches'
for n in range(0, len(tools), size):
    lines = [f'# Catalog extract packet: {name}-{n // size + 1}', '']
    for t in tools[n:n + size]:
        m, g, s = mods[t['module_id']], tags.get(t['tool_id'], {}), stage(t['tool_id'])
        files = [f for f in ('spec.md', 'notes.md', 'tool.json', 'plan.md') if (ROOT / 'tools' / t['tool_id'] / f).exists()]
        lines += [f"## {t['tool_id']}", f"- title: {t['title']} | format: {t['format']} | family: {t['family'] or 'none'} | stage: {s}",
                  f"- module: {m['module_id']} ({m['subject']} {m['grade']}, {m['strand']}): {m['title']}. {m['description']}",
                  f"- module standards: {m['standards']}",
                  f"- concept line: {t['concept']}",
                  f"- old tags: skill_key={g.get('skill_key','')} | action={g.get('action','')} | setting_group={g.get('setting_group','')}",
                  f"- read: " + ', '.join(f"tools/{t['tool_id']}/{f}" for f in files), '']
    p = out / f'{name}-{n // size + 1}.md'
    p.write_text('\n'.join(lines), encoding='utf-8'); print(p.relative_to(ROOT), len(tools[n:n + size]))
