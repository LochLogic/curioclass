"""Candidate concept rows a Worksheet Generator might make (docs/WORKSHEETS-PLAN.md, "generator first").

    python scripts/ws_gen_propose.py <out-dir>        one CSV per subject file: the unwritten rows whose type and words
                                                      suggest a generator, with the suggested generator id

A crude first sift for the reviewers who fill data/closet/worksheets/generated.csv: it only narrows the list. A
reviewer reads each row's Students line against docs/agents/GEN-OPTIONS.md and keeps a row only when a generator
really does what the line asks, with the right settings. Rows already written, and the types a generator cannot make
(Read and respond, Source analysis, Lab, Critique, Diagram, most Puzzles), are left out.
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import check_worksheets as cw  # noqa: E402
import worksheets as ws  # noqa: E402
import ws_generated  # noqa: E402

KW = {
    'number-ops': r'\b(add|subtract|multipl|divid|division|regroup|facts?\b|sums?\b|difference|product|quotient)',
    'fractions': r'\bfraction|mixed number|numerator|denominator|equivalent',
    'equations': r'\bequation|expression|inequalit|solve for|variable|linear|slope|intercept',
    'measure-shapes': r'\barea\b|perimeter|volume|surface area|circumference',
    'word-problems': r'\bword problem|story problem|elapsed time|money|coins|make change|how many',
    'science-calc': r'\bdensity|speed|velocity|acceleration|ohm|momentum|kinetic|work and power|formula',
    'punnett': r'\bpunnett|monohybrid|dihybrid|genotype|phenotype|allele',
    'graph-reading': r'\bbar graph|line graph|pictograph|line plot|data table|histogram|scatter|read (a|the) (table|graph|chart)',
    'vocabulary': r'\bvocab|word wall|words? in context|definitions?|word map|key terms',
    'word-puzzles': r'\bcrossword|word search',
    'map-skills': r'\bmap\b|compass|grid|map key|legend|cardinal',
    'timeline': r'\btimeline|chronolog|order the events|sequence of events',
    'organizer': r'\bvenn|organizer|t-chart|kwl|cause and effect|compare and contrast|story map|frayer|concept web',
    'writing-frame': r'\bparagraph|sentence starters?|writing frame|outline|frame\b',
    'planner-log': r'\bplanner|\blog\b|reflection|goal|journal|self-assess|checklist|plan a',
}
BY_TYPE = {'Organizer': 'organizer', 'Writing frame': 'writing-frame', 'Planner': 'planner-log', 'Log': 'planner-log',
           'Reflection': 'planner-log', 'Timeline': 'timeline', 'Map': 'map-skills', 'Vocabulary': 'vocabulary',
           'Data and graphs': 'graph-reading'}
NEVER = {'Read and respond', 'Source analysis', 'Lab', 'Critique', 'Diagram'}


def main(out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    U = cw.units()
    built = {u: {s['n'] for s, _ in ws.load(u)[1]} for u in ws.built_units()}
    backed = ws_generated.load()
    total = 0
    for f in cw.FILES:
        rows = cw.rows(f)
        cands = []
        for u, rs in rows.items():
            for r in rs:
                if r['n'] in built.get(u, ()) or r['n'] in backed.get(u, {}) or r['type'] in NEVER:
                    continue
                text = (r['title'] + ' ' + r['does']).lower()
                gen = BY_TYPE.get(r['type'])
                if not gen:
                    hits = [g for g, k in KW.items() if re.search(k, text)]
                    if r['type'] == 'Puzzle':
                        hits = [h for h in hits if h == 'word-puzzles']
                    gen = hits[0] if hits else None
                if gen:
                    cands.append(dict(unit=u, label=U[u]['label'], n=r['n'], title=r['title'], type=r['type'], module=r['module'],
                                      does=r['does'], suggested=gen))
        if cands:
            with (out_dir / f'{f}.csv').open('w', encoding='utf-8', newline='') as fh:
                w = csv.DictWriter(fh, fieldnames=list(cands[0]))
                w.writeheader()
                w.writerows(cands)
            print(f'{f}: {len(cands)} candidates')
            total += len(cands)
    print(f'{total} candidate rows -> {out_dir}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'docs' / 'agents' / 'gen-candidates')
