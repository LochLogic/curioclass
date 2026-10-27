"""Write the group sections of a spec wave's batch note: one table per group plus the overlap pass's notes per tool.

    python scripts/overlap/wave_note.py GROUPS.txt > sections.md

GROUPS.txt has one group per line: `key|Heading|id id id ...` (tool ids as in data/tools-concepts.csv). Per-tool notes
come from Cory's overlap decisions (docs/agents/overlap/review.json and choices.json, matched by id or by the
decided title) and from the gap fill (tools added there point to their staging notes). Paste the output under the
note's own rules section.
"""
import csv, io, json, os, sys
from common import ROOT, OUT


def main():
    concepts = {r['tool_id']: r for r in csv.DictReader(io.open(os.path.join(ROOT, 'data', 'tools-concepts.csv'), encoding='utf-8'))}
    review = {x['id']: x for x in json.load(io.open(os.path.join(OUT, 'review.json'), encoding='utf-8'))}
    choices = {x['id']: x for x in json.load(io.open(os.path.join(OUT, 'choices.json'), encoding='utf-8'))}
    by_title = {(c.get('new_title') or c['title']): c['id'] for c in choices.values()}
    gapfill = {}
    for d in os.listdir(os.path.join(ROOT, 'docs', 'agents', 'gapfill')):
        p = os.path.join(ROOT, 'docs', 'agents', 'gapfill', d, 'concepts.txt')
        if os.path.exists(p):
            for l in io.open(p, encoding='utf-8'):
                if l.strip() and not l.startswith('#'):
                    gapfill[l.split('|')[1].strip()] = d
    for line in io.open(sys.argv[1], encoding='utf-8'):
        if not line.strip() or line.startswith('#'): continue
        key, head, ids = [x.strip() for x in line.split('|')]
        ids = ids.split()
        print(f'### {head} (`{key}`, {len(ids)})\n')
        print('| Id | Title | Grade | Format | Family |\n|---|---|---|---|---|')
        for i in ids:
            c = concepts[i]
            print(f"| {i} | {c['title']} | {c['grade']} | {c['format']} | {c['family'] or '-'} |")
        print()
        for i in ids:
            note = tool_note(concepts[i], review, choices, by_title, gapfill)
            if note: print(f'- **{i}:** {note}\n')


def tool_note(c, review, choices, by_title, gapfill):
    rid = c['tool_id'] if c['tool_id'] in choices else by_title.get(c['title'])
    parts = []
    if c['title'] in gapfill:
        parts.append(f"New in the gap fill (docs/agents/gapfill/{gapfill[c['title']]}/notes.md).")
    if not rid:
        return ' '.join(parts)
    r, ch = review[rid], choices[rid]
    if r.get('line'):
        parts.append(f'Topic line under the title on the tool page: "{r["line"]}".')
    why = r['why'].removeprefix('Spec check: ').rstrip('.')
    fam = next((x for x in r.get('rules', []) if x.startswith('Family:')), '')
    if ch['choice'] in ('accept', 'now') and r['fix'] in ('reshape', 'rename', 'merge', 'move'):
        verb = {'reshape': 'Reshaped', 'rename': 'Renamed'}.get(r['fix'], 'Changed')
        parts.append(f'{verb} by the overlap pass (Cory accepted; the title and concept above are the new ones). '
                     f'The clash it fixed: {why}.')
    elif ch['choice'] == 'later':
        sug = f'"{r["new_title"]}"' + (f': {r["new_concept"]}' if r['fix'] == 'reshape' and r.get('new_concept') else '')
        parts.append(f'Overlap note (left for you to settle in the spec): {why}. Suggested fix ({r["fix"]}): {sug.rstrip(".")}. '
                     'Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.')
    elif r['fix'] == 'spec-note':
        parts.append(f'Spec note from the overlap pass: {why}.')
    elif r['fix'] == 'keep':
        parts.append(f'Kept as written in the overlap pass ({why}).')
    elif r['fix'] == 'add-standard':
        parts.append(f'The overlap pass added standards to its module; the concept above already covers them ({why}).')
    if fam:
        parts.append(fam)
    return ' '.join(parts)


if __name__ == '__main__':
    main()
