r"""Check the Word Wall (data/closet/words/<subject>.txt) against docs/SUPPLY-CLOSET-PLAN.md, Phase C.

    python scripts/check_words.py            check every word file, exit 1 on any problem
    python scripts/check_words.py math ela   check some subjects

One line per card: module_id|word|definition|example|picture|es_word|es_definition|es_example
picture is what to draw (an "svg:" prefix means a diagram drawn in code, not a painting); the drawn file goes in
closet/words/art/<module_id>/<slug(word)>.webp. build_site.py uses load() for /modules/<id>/words/ and runs
problems() so a bad word list stops a closet build.
"""
import csv, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORDS = ROOT / 'data' / 'closet' / 'words'
ART = ROOT / 'closet' / 'words' / 'art'
FIELDS = ['module_id', 'word', 'definition', 'example', 'picture', 'es_word', 'es_definition', 'es_example']
PER_MODULE = (5, 8)
# definition word caps by band (Spanish gets five more words: it runs longer)
DEF_CAP = {'k2': 12, '35': 15, '68': 20, '912': 20}
EXAMPLE_CAP = 22


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def band(grade):
    first = grade.split('-')[0]
    return 'k2' if first in ('k', '1', '2') else '35' if first in ('3', '4', '5') else '68' if first in ('6', '7', '8') else '912'


def load(subjects=None):
    """{module_id: [card dict]} from every word file (or just some subjects)."""
    out = defaultdict(list)
    for f in sorted(WORDS.glob('*.txt')):
        if subjects and f.stem not in subjects:
            continue
        for n, line in enumerate(f.read_text(encoding='utf-8').splitlines(), 1):
            if not line.strip() or line.startswith('#'):
                continue
            parts = [p.strip() for p in line.split('|')]
            card = dict(zip(FIELDS, parts + [''] * (len(FIELDS) - len(parts))), file=f.name, line=n, extra=len(parts) - len(FIELDS))
            card['slug'] = slug(card['word'])
            card['art'] = ART / card['module_id'] / f"{card['slug']}.webp"
            out[card['module_id']].append(card)
    return dict(out)


def has_word(text, word):
    return re.search(r'\b' + re.escape(word.lower()) + r'\b', text.lower()) is not None


def problems(module_id, cards, modules):
    m = modules.get(module_id)
    if not m:
        return [f'{module_id}: not a module in data/modules.csv']
    out, b, seen = [], band(m['grade']), set()
    where = lambda c: f"{c['file']}:{c['line']} {c['word'] or '?'}"
    if not PER_MODULE[0] <= len(cards) <= PER_MODULE[1]:
        out.append(f'{module_id}: {len(cards)} words, needs {PER_MODULE[0]} to {PER_MODULE[1]}')
    for c in cards:
        if c['extra']:
            out.append(f"{where(c)}: {len(FIELDS) + c['extra']} fields, needs {len(FIELDS)}")
        for k in FIELDS:
            if not c[k] and not (k == 'picture' and b in ('68', '912')) and not (k in ('example', 'es_example') and b == 'k2'):
                out.append(f'{where(c)}: {k} is empty')
        if c['word'].lower() in seen:
            out.append(f'{where(c)}: repeated in this module')
        seen.add(c['word'].lower())
        n = len(c['definition'].split())
        if n > DEF_CAP[b]:
            out.append(f'{where(c)}: definition is {n} words, the cap is {DEF_CAP[b]}')
        n = len(c['es_definition'].split())
        if n > DEF_CAP[b] + 5:
            out.append(f'{where(c)}: es_definition is {n} words, the cap is {DEF_CAP[b] + 5}')
        for k in ('example', 'es_example'):
            if len(c[k].split()) > EXAMPLE_CAP:
                out.append(f'{where(c)}: {k} is over {EXAMPLE_CAP} words')
        if c['word'] and has_word(c['definition'], c['word']):
            out.append(f'{where(c)}: the definition uses the word itself')
        if c['example'] and not re.search(r'\b' + re.escape(c['word'].lower().rstrip('e')), c['example'].lower()):
            out.append(f'{where(c)}: the example does not use the word')
        text = ' '.join(c[k] for k in FIELDS)
        if '—' in text:
            out.append(f'{where(c)}: em dash')
        if re.search(r'\bCurio\b(?! Class)', text):
            out.append(f'{where(c)}: "Curio" without "Class"')
    return out


def main():
    modules = {m['module_id']: m for m in csv.DictReader(open(ROOT / 'data' / 'modules.csv', encoding='utf-8'))}
    words = load(sys.argv[1:] or None)
    bad = [p for mid, cards in words.items() for p in problems(mid, cards, modules)]
    for p in bad:
        print('  -', p)
    cards = sum(len(c) for c in words.values())
    drawn = sum(c['art'].exists() for cs in words.values() for c in cs)
    print(f'{len(words)} modules, {cards} cards, {drawn} pictures drawn, {len(bad)} problems')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
