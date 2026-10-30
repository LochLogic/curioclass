r"""Tool counts for the Review Desk's stats panel: every catalog tool by subject and by grade band, per pipeline stage.

    python scripts/desk_stats.py <out.json>     write the stats document (then ArtifactData set stats/board)

Stages come from board.py (worked out from each tool's files), so the panel and docs/BUILD-BOARD.md always agree.
Planned (the total) is every row in data/tools-concepts.csv; each stage column counts the tools that are at that stage
now, so a row adds up to it. The first stage, noidea, counts tools on the plan whose catalog line has no idea written
yet, so the desk shows at a glance that every planned tool has been ideated (0). `where` maps each tool to its subject, band and stage, so the page can move the tools waiting
on Cory (desk items marked ready) out of their stage into its own "Your review" column, and the row still adds up.
"""
import csv, json, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from board import ORDER, row  # noqa: E402

STAGES = ['noidea'] + ORDER

BANDS = {'k': 'K-2', '1': 'K-2', '2': 'K-2', 'k-2': 'K-2', '3': '3-5', '4': '3-5', '5': '3-5', '3-5': '3-5',
         '6': '6-8', '7': '6-8', '8': '6-8', '6-8': '6-8', '9': '9-12', '10': '9-12', '11': '9-12', '12': '9-12',
         '9-12': '9-12'}
BAND_ORDER = ['K-2', '3-5', '6-8', '9-12', 'Across bands']


def table(rows, key, order):
    out = []
    for k in order:
        rs = [r for r in rows if key(r) == k]
        if rs:
            out.append({'name': k, 'planned': len(rs), **{s: sum(r['stage'] == s for r in rs) for s in STAGES}})
    return out


def main():
    rows = list(csv.DictReader(open(ROOT / 'data' / 'tools-concepts.csv', encoding='utf-8')))
    for r in rows:
        r['stage'] = row(r['tool_id'])['stage'] if (r.get('concept') or '').strip() else 'noidea'
    labels = {s['subject_id']: s['label'] for s in csv.DictReader(open(ROOT / 'data' / 'subjects.csv', encoding='utf-8'))}
    subj = table(rows, lambda r: labels.get(r['subject'], r['subject']), list(labels.values()))
    subj.sort(key=lambda t: -t['planned'])
    band = table(rows, lambda r: BANDS.get(r['grade'], 'Across bands'), BAND_ORDER)
    total = {'name': 'All tools', 'planned': len(rows), **{s: sum(r['stage'] == s for r in rows) for s in STAGES}}
    # where each tool sits, so the page can count the desk's own items (waiting on Cory) under the same rows
    where = {r['tool_id']: [labels.get(r['subject'], r['subject']), BANDS.get(r['grade'], 'Across bands'), r['stage']] for r in rows}
    doc = {'stages': STAGES, 'subjects': subj, 'bands': band, 'total': total, 'where': where,
           'at': datetime.now(timezone.utc).isoformat(timespec='seconds')}
    Path(sys.argv[1]).write_text(json.dumps(doc, indent=1), encoding='utf-8')
    print('  '.join(f'{s} {total[s]}' for s in STAGES), f'total {len(rows)}')


if __name__ == '__main__':
    main()
