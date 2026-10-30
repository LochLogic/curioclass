r"""Everything a spec agent needs about one tool concept and the tools around it, so it can stand apart from them.

    python scripts/neighbors.py <tool-id>

Prints the concept, its module (description and standards), its format, its family siblings and the other tools in
the same subject and grade (with neighboring grades), each with its stage: built, draft, spec or concept.
A sibling that has a spec.md also shows its "One idea" line, so overlap is easy to spot.
"""
import csv, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'
GRADES = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


def load(name):
    return list(csv.DictReader(open(ROOT / 'data' / name, encoding='utf-8')))


def stage(tid):
    f = TOOLS / tid
    if (f / 'tool.json').exists():
        return 'built'
    if (f / 'tool.draft.json').exists():
        return 'draft'
    if (f / 'spec.md').exists():
        return 'spec'
    return 'concept'


def idea(tid):
    s = TOOLS / tid / 'spec.md'
    if not s.exists():
        return ''
    m = re.search(r'^## One idea\s*\n+(.+)', s.read_text(encoding='utf-8'), re.M)
    return m.group(1).strip() if m else ''


def near(g, other):
    if g not in GRADES or other not in GRADES:
        return g == other
    return abs(GRADES.index(g) - GRADES.index(other)) <= 1


def line(r, me):
    st = stage(r['tool_id'])
    s = f"- {r['title']} ({r['tool_id']}) [{r['format']}, grade {r['grade']}, {st}]: {r['concept']}"
    i = idea(r['tool_id'])
    return s + (f"\n    One idea: {i}" if i else '')


def main():
    tid = sys.argv[1]
    rows = load('tools-concepts.csv')
    me = next((r for r in rows if r['tool_id'] == tid), None)
    if not me:
        sys.exit(f'no concept with id {tid}')
    mod = next((m for m in load('modules.csv') if m['module_id'] == me['module_id']), {})
    fmt = next((f for f in load('formats.csv') if f['format_id'] == me['format']), {})
    print(f"# {me['title']} ({tid})  stage: {stage(tid)}\n")
    print(f"Concept: {me['concept']}")
    print(f"Subject {me['subject']}, grade {me['grade']}, format {me['format']}, family {me['family'] or 'none'}")
    if fmt:
        print(f"Format {fmt['label']}: {fmt['what_it_feels_like']} (good for {fmt['good_for']})")
    if mod:
        print(f"\nModule: {mod['title']} ({mod.get('strand', '')})\n  {mod['description']}\n  Standards: {mod['standards'].replace(';', ', ')}")
    if me['family']:
        fam = [r for r in rows if r['family'] == me['family'] and r['tool_id'] != tid]
        print(f"\n## Family {me['family']} ({len(fam)} siblings): share the engine, differ in content and framing")
        for r in sorted(fam, key=lambda r: GRADES.index(r['grade']) if r['grade'] in GRADES else 99):
            print(line(r, me))
    same = [r for r in rows if r['subject'] == me['subject'] and near(me['grade'], r['grade']) and r['tool_id'] != tid
            and r['family'] != me['family'] or (r['subject'] == me['subject'] and not me['family'] and near(me['grade'], r['grade']) and r['tool_id'] != tid)]
    seen = set()
    print(f"\n## Same subject, grade {me['grade']} and next to it: don't repeat their idea or mechanic")
    for r in same:
        if r['tool_id'] in seen:
            continue
        seen.add(r['tool_id']); print(line(r, me))
    fmt_rows = [r for r in rows if r['format'] == me['format'] and r['subject'] == me['subject'] and r['tool_id'] != tid and stage(r['tool_id']) != 'concept']
    if fmt_rows:
        print(f"\n## Same format and subject, already specced or built: vary the look and the play")
        for r in fmt_rows:
            print(line(r, me))


if __name__ == '__main__':
    main()
