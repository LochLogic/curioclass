"""Rename planned tools after a spec wave: the id is the title slug, so the folder and every id list follow the title.

    python scripts/rename_tools.py old-id="New Title" [old-id="New Title" ...]

Changes the title on the concept line in data/concepts/*.txt, moves tools/<old-id>/ to tools/<new-id>/, and swaps the
id in data/waves.csv, docs/agents/overlap/tags.csv (id and title) and the wave notes (docs/agents/BATCH-*.md tables), and records the move in docs/agents/overlap/renamed.json.
Live tools need a redirect too (data/redirects.csv); this refuses them. Run `python scripts/check_concepts.py --write`
after it. Past review records (choices.json, review.json, clusters.md) keep the old ids on purpose.
"""
import csv, json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slug(title):
    tid = ''.join(ch if ch.isalnum() else '-' for ch in title.lower()).strip('-')
    while '--' in tid:
        tid = tid.replace('--', '-')
    return tid


def main():
    todo = dict(a.split('=', 1) for a in sys.argv[1:])
    new_ids = {old: slug(t) for old, t in todo.items()}
    for old, new in new_ids.items():
        if (ROOT / 'tools' / old / 'tool.json').exists():
            raise SystemExit(f'{old} is live: add a redirect and rename it by hand')
        if (ROOT / 'tools' / new).exists():
            raise SystemExit(f'tools/{new} already exists')

    done = set()
    for path in sorted((ROOT / 'data' / 'concepts').glob('*.txt')):
        lines = path.read_text(encoding='utf-8').splitlines()
        for n, line in enumerate(lines):
            if not line.strip() or line.startswith('#'):
                continue
            f = line.split('|')
            if slug(f[1]) in todo:
                old = slug(f[1])
                f[1] = todo[old]
                lines[n] = '|'.join(f)
                done.add(old)
        path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    missing = set(todo) - done
    if missing:
        raise SystemExit(f'not found in concepts: {sorted(missing)}')

    for old, new in new_ids.items():
        if (ROOT / 'tools' / old).exists():
            shutil.move(str(ROOT / 'tools' / old), str(ROOT / 'tools' / new))

    waves = ROOT / 'data' / 'waves.csv'
    rows = list(csv.DictReader(open(waves, encoding='utf-8')))
    for r in rows:
        r['tool_id'] = new_ids.get(r['tool_id'], r['tool_id'])
    with open(waves, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['tool_id', 'wave'], lineterminator=chr(10))
        w.writeheader()
        w.writerows(rows)

    tags = ROOT / 'docs' / 'agents' / 'overlap' / 'tags.csv'
    rows = list(csv.DictReader(open(tags, encoding='utf-8')))
    fields = list(rows[0])
    for r in rows:
        if r['tool_id'] in todo:
            r['title'] = todo[r['tool_id']]
            r['tool_id'] = new_ids[r['tool_id']]
    with open(tags, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=chr(10))
        w.writeheader()
        w.writerows(rows)

    log = ROOT / 'docs' / 'agents' / 'overlap' / 'renamed.json'  # every rename so far, old id -> new id
    renamed = json.loads(log.read_text(encoding='utf-8'))
    for k, v in list(renamed.items()):
        renamed[k] = new_ids.get(v, v)
    renamed.update(new_ids)
    log.write_text(json.dumps(renamed, indent=1) + '\n', encoding='utf-8')

    for note in (ROOT / 'docs' / 'agents').glob('BATCH-*.md'):
        text = new_text = note.read_text(encoding='utf-8')
        for old, new in new_ids.items():
            new_text = re.sub(rf'^\|\s*{re.escape(old)}\s*\|', f'| {new} |', new_text, flags=re.M)
        if new_text != text:
            note.write_text(new_text, encoding='utf-8')

    for old, new in new_ids.items():
        print(f'{old} -> {new}')


if __name__ == '__main__':
    main()
