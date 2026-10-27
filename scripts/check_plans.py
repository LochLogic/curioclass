r"""Check every tool's lesson plan (tools/<id>/plan.md) against docs/LESSON-PLANS.md.

    python scripts/check_plans.py            check all plans, exit 1 on any problem
    python scripts/check_plans.py <id>...    check some

build_site.py uses parse() to render /tools/<id>/plan/ and runs problems() so a bad plan stops the build.
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'
ARCS = {
    'explore-first': ('Explore first', ['Hook', 'Explore', 'Make sense', 'Apply', 'Exit check']),
    'teach-then-practice': ('Teach, then practice', ['Hook', 'Teach', 'Practice', 'Apply', 'Exit check']),
    'model-then-make': ('Model, then make', ['Hook', 'Model', 'Make', 'Share', 'Exit check']),
}
KEYS = ['arc', 'minutes', 'focus', 'goal', 'materials', 'grouping']
UNTIMED = ['Before class', 'Support and stretch', 'Short on time']
TIMED = re.compile(r'^(.+?) \((\d+) min\)$')
MAX_WORDS = 850


def parse(tid):
    """Header dict plus sections [(title, minutes or None, markdown body)], or None if the tool has no plan."""
    p = TOOLS / tid / 'plan.md'
    if not p.exists():
        return None
    head, _, body = p.read_text(encoding='utf-8').partition('\n---\n')
    meta = dict(line.split(':', 1) for line in head.strip().splitlines() if ':' in line)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    sections = []
    for chunk in re.split(r'^## ', body, flags=re.M)[1:]:
        title, _, text = chunk.partition('\n')
        m = TIMED.match(title.strip())
        sections.append((m[1], int(m[2]), text.strip()) if m else (title.strip(), None, text.strip()))
    return {'meta': meta, 'sections': sections, 'body': body}


def focus(meta):
    """The plan's focus codes: semicolon separated, like modules.csv (some codes have spaces)."""
    return [c.strip() for c in meta.get('focus', '').split(';') if c.strip()]


def problems(tid, module=None):
    plan = parse(tid)
    if plan is None:
        return []
    meta, secs, out = plan['meta'], plan['sections'], []
    out += [f'header is missing {k}' for k in KEYS if not meta.get(k)]
    arc = ARCS.get(meta.get('arc'))
    if not arc:
        out.append(f"unknown arc {meta.get('arc')!r} (one of {', '.join(ARCS)})")
    timed = [(t, m) for t, m, _ in secs if m is not None]
    if arc:
        want = UNTIMED[:1] + [f'{t} (min)' for t in arc[1]] + UNTIMED[1:]
        have = [t if m is None else f'{t} (min)' for t, m, _ in secs]
        if have != want:
            out.append(f"sections are {have}, the {meta['arc']} arc needs {want}")
    total = sum(m for _, m in timed)
    if meta.get('minutes', '').isdigit() and total != int(meta['minutes']):
        out.append(f"parts add up to {total} min, header says {meta['minutes']}")
    if module:
        k2 = all(g in ('k', '1', '2') for g in module['grade'].split('-'))
        if not (30 <= total <= (40 if k2 else 50)):
            out.append(f'{total} min is outside {"30-40 (K-2)" if k2 else "30-50"}')
        if k2 and any(m > 15 for _, m in timed):
            out.append('K-2 parts are 15 min at most')
        codes = module['standards'].split(';')
        out += [f'focus {c} is not one of this module\'s standards {codes}' for c in focus(meta) if c not in codes]
    words = len(re.findall(r"[\w']+", plan['body'] + ' '.join(meta.values())))
    if words > MAX_WORDS:
        out.append(f'{words} words, the limit is {MAX_WORDS}')
    src = TOOLS / tid / 'src.html'
    if src.exists():
        text = src.read_text(encoding='utf-8').lower()
        bold = {b.strip(' .,!?:;').lower() for b in re.findall(r'\*\*(.+?)\*\*', plan['body'])}
        found = {b for b in bold if b and b in text}
        if len(found) < 4:
            out.append(f'only {len(found)} bold names found in the tool ({sorted(found)}); name at least 4 real buttons, items or labels')
    raw = (TOOLS / tid / 'plan.md').read_text(encoding='utf-8')
    if '\u2014' in raw:
        out.append('em dash')
    if re.search(r'\bCurio\b(?! Class)', raw):
        out.append('"Curio" without "Class"')
    return out


EXIT_LABELS = ['Show me', 'Explain', 'Rate it']
EXIT_ITEM = re.compile(r'^(\d+)\.\s+(.+)$')
EXIT_WORDS = {'ticket': 45, 'checklist': 10}  # per item; checklist items are column headings
STOP = {'about', 'after', 'again', 'because', 'before', 'cards', 'child', 'children', 'class', 'could', 'every', 'first',
        'needs', 'other', 'partner', 'point', 'right', 'shows', 'their', 'there', 'these', 'thing', 'think', 'three',
        'which', 'where', 'while', 'would', 'write', 'student', 'students'}


def is_k2(module):
    return all(g in ('k', '1', '2') for g in module['grade'].split('-'))


def parse_exit(tid):
    """{'kind', 'items': [(label or None, prompt, answer or None)]} from tools/<id>/exit.md, or None."""
    p = TOOLS / tid / 'exit.md'
    if not p.exists():
        return None
    head, _, body = p.read_text(encoding='utf-8').partition('\n---\n')
    meta = {k.strip(): v.strip() for k, _, v in (line.partition(':') for line in head.strip().splitlines())}
    items = []
    for line in body.strip().splitlines():
        m = EXIT_ITEM.match(line.strip())
        if not m:
            continue
        text, _, answer = m[2].partition('|')
        label, sep, prompt = text.partition(':')
        if not sep or label.strip() not in EXIT_LABELS:
            label, prompt = None, text
        answer = answer.strip()
        items.append((label and label.strip(), prompt.strip(), answer[1:-1].strip() if answer.startswith('(') and answer.endswith(')') else (answer or None)))
    return {'kind': meta.get('kind'), 'items': items}


def keywords(text):
    return {w for w in re.findall(r'[a-z]{5,}', text.lower()) if w not in STOP}


def exit_problems(tid, module=None):
    """exit.md against docs/LESSON-PLANS.md, Sub Day: kind, 1 to 3 items, a key for tickets, and the same ask as the plan's Exit check."""
    ex = parse_exit(tid)
    if ex is None:
        return []
    out, kind, items = [], ex['kind'], ex['items']
    if kind not in EXIT_WORDS:
        out.append(f'exit.md kind {kind!r} must be ticket or checklist')
    elif module and kind != ('checklist' if is_k2(module) else 'ticket'):
        out.append(f"exit.md kind is {kind}, but grade {module['grade']} needs {'checklist' if is_k2(module) else 'ticket'}")
    if not 1 <= len(items) <= 3:
        out.append(f'exit.md has {len(items)} items, needs 1 to 3')
    for i, (label, prompt, answer) in enumerate(items, 1):
        if kind == 'ticket':
            if not label:
                out.append(f'exit.md item {i} needs a label: {", ".join(EXIT_LABELS)}')
            elif label == 'Rate it' and answer:
                out.append(f'exit.md item {i} is a self-rating and takes no answer')
            elif label != 'Rate it' and not answer:
                out.append(f'exit.md item {i} needs an answer for the teacher key: "| (answer)"')
        if kind in EXIT_WORDS and len(prompt.split()) > EXIT_WORDS[kind]:
            out.append(f'exit.md item {i} is {len(prompt.split())} words, the cap is {EXIT_WORDS[kind]}')
    if kind == 'ticket' and items and items[-1][0] != 'Rate it':
        out.append('exit.md tickets end with a "Rate it:" self-rating')
    plan = parse(tid)
    check = ' '.join(t for title, _, t in plan['sections'] if title == 'Exit check') if plan else ''
    if check and not keywords(check) & keywords(' '.join(f'{p} {a or ""}' for _, p, a in items)):
        out.append("exit.md shares no key word with the plan's Exit check; they must ask the same thing")
    raw = (TOOLS / tid / 'exit.md').read_text(encoding='utf-8')
    if '—' in raw:
        out.append('exit.md: em dash')
    if re.search(r'\bCurio\b(?! Class)', raw):
        out.append('exit.md: "Curio" without "Class"')
    return out


def modules_by_tool():
    mods = {m['module_id']: m for m in csv.DictReader(open(ROOT / 'data' / 'modules.csv', encoding='utf-8'))}
    return {c['tool_id']: mods[c['module_id']] for c in csv.DictReader(open(ROOT / 'data' / 'tools-concepts.csv', encoding='utf-8'))}


def main():
    mods = modules_by_tool()
    ids = sys.argv[1:] or sorted(p.parent.name for p in TOOLS.glob('*/plan.md'))
    bad = 0
    for tid in ids:
        found = problems(tid, mods.get(tid)) + exit_problems(tid, mods.get(tid))
        if (TOOLS / tid / 'plan.md').exists() and not (TOOLS / tid / 'exit.md').exists():
            found.append('no exit.md, so no Sub Day packet (docs/LESSON-PLANS.md, Sub Day)')
        bad += bool(found)
        print(f"{tid}: {'ok' if not found else ''}" + ''.join(f'\n  - {p}' for p in found))
    print(f'{len(ids)} plans, {bad} with problems')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
