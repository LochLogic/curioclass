r"""A deeper review of the Word Wall text than check_words.py (which gates the build). Review only: it changes nothing.

    python scripts/check_words_review.py            write docs/agents/audit/wordwall-text-review.md
    python scripts/check_words_review.py --print    also print every finding

Checks, per card (data/closet/words/<subject>.txt):
  dup        the same word, slug or definition twice in a module
  root-def   the word's root (or, for a phrase, one of its main words) inside its own definition; same for Spanish
  example    the example sentence has no form of the word; same for es_example and es_word
  empty      an empty field (9-12 pictures and K-2 examples may be empty by design; counted apart)
  spanish    a Spanish field identical to the English one, or reading as English
  long       a definition far too long or too hard for its grade band (near the word cap and a high reading level,
             or long words for K-2)
  spec       an "svg:" card with no line in data/closet/words/diagrams.py, or a spec line with no svg card
  house      an em dash, or "Curio" without "Class"
The findings are heuristics: the report lists them for a person to judge, most are worth a look, some are fine.
"""
import csv, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_words as cw  # noqa: E402

ROOT = cw.ROOT
OUT = ROOT / 'docs' / 'agents' / 'audit' / 'wordwall-text-review.md'
STOP_EN = set('a an the of to in on for and or with by at from as is are be it its that this into than then your you '
              'they their them we our one two how what when'.split())
STOP_ES = set('el la los las un una unos unas de del al a en con por para y o que se es son su sus lo le como mas más '
              'sin muy'.split())
EN_MARK = set('the and of is with that this are which when where what from'.split())
ES_MARK = set('el la los las de que y en un una es con por para del se'.split())
SUFFIX_EN = ('ations', 'ation', 'ements', 'ement', 'ments', 'ment', 'nesses', 'ness', 'ities', 'ity', 'ions', 'ion',
             'ings', 'ing', 'ers', 'er', 'ies', 'ied', 'ed', 'es', 'ly', 'al', 'ive', 'ous', 'ful', 'ic', 's', 'e', 'y')
SUFFIX_ES = ('aciones', 'ación', 'acion', 'mientos', 'miento', 'idades', 'idad', 'ciones', 'ción', 'cion', 'mente',
             'ar', 'er', 'ir', 'os', 'as', 'es', 'o', 'a', 'e', 's')
SYL = {'k2': 1.5, '35': 1.7, '68': 1.9, '912': 2.1}  # syllables a word above which a long definition reads hard


def toks(s):
    s = unicodedata.normalize('NFD', s.lower())
    return re.findall(r"[a-zñ]+", ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn' or ch == '̃'))


def variants(r):
    """A root and its Spanish stem-change forms (medir: mid-, resolver: resuelv-, cerrar: cierr-, jugar: jueg-)."""
    out = {r}
    for i in range(len(r) - 1, 0, -1):
        if r[i] in 'eo' and r[i - 1] not in 'aeiou':
            out |= {r[:i] + v + r[i + 1:] for v in (('i', 'ie') if r[i] == 'e' else ('ue',))}
            break
    if r.startswith('ju'):
        out.add('jue' + r[2:])
    return out


def root(w, suffixes):
    for s in suffixes:
        if w.endswith(s) and len(w) - len(s) >= 4:
            return w[:-len(s)]
    return w


def main_words(term, stop):
    return [t for t in toks(term) if t not in stop and len(t) >= 3]


def has_form(text, term, stop, suffixes, minroot=4):
    """True if text has some form of the term: every main word of a phrase is not needed, one is enough."""
    ws = main_words(term, stop) or toks(term)
    tt = toks(text)
    for w in ws:
        r = root(w, suffixes)
        r = r if len(r) >= minroot else w[:max(len(w) - 1, 3)] if len(w) > 3 else w
        rs = variants(r) if stop is STOP_ES else {r}
        if any(t.startswith(v) for v in rs for t in tt) or any(len(w) >= 5 and t.startswith(w[:5]) for t in tt):
            return True
        # irregular-ish: drop the last letter for short words (run/ran is not caught, that is fine)
    return False


def root_in(text, term, stop, suffixes, head=-1):
    """Main words of the term whose root shows up in text: [(word, matched token)]. For a phrase, reusing only its head
    noun is fine ("a note that lasts one beat" for quarter note), so the head (last word in English, first in Spanish)
    counts only when every main word is reused."""
    out, tt = [], toks(text)
    ws = main_words(term, stop)
    for w in ws:
        r = root(w, suffixes)
        if len(r) < 4:
            if w in tt:
                out.append((w, w))
            continue
        for t in tt:
            if t.startswith(r):
                out.append((w, t))
                break
    if len(ws) > 1 and len(out) < len(ws):
        out = [(w, t) for w, t in out if w != ws[head]]
    return out


def syllables(w):
    w = w.lower()
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and not w.endswith(('le', 'ee')) and n > 1:
        n -= 1
    return max(n, 1)


def lang_score(text):
    tt = toks(text)
    return sum(t in EN_MARK for t in tt), sum(t in ES_MARK for t in tt)


def review():
    mods = {m['module_id']: m for m in csv.DictReader(open(ROOT / 'data' / 'modules.csv', encoding='utf-8'))}
    words = cw.load()
    F = defaultdict(list)  # check -> [(where, note)]
    allowed_empty = Counter()
    for mid, cards in words.items():
        b = cw.band(mods[mid]['grade']) if mid in mods else '912'
        seen_w, seen_s, seen_d = {}, {}, {}
        for c in cards:
            where = f"{c['file'].removesuffix('.txt')}:{c['line']} {mid} / {c['word']}"
            c['where'], c['band'] = where, b
            # dup
            for key, seen, what in ((c['word'].lower(), seen_w, 'word'), (c['slug'], seen_s, 'slug'),
                                    (c['definition'].lower().strip(' .'), seen_d, 'definition')):
                if key and key in seen:
                    F['dup'].append((where, f'same {what} as line {seen[key]}'))
                elif key:
                    seen[key] = c['line']
            # empty
            for k in cw.FIELDS:
                if not c[k]:
                    if (k == 'picture' and b in ('68', '912')) or (k in ('example', 'es_example') and b == 'k2'):
                        allowed_empty[k] += 1
                    else:
                        F['empty'].append((where, f'{k} is empty'))
            if not c['word']:
                continue
            # root in definition
            hit = root_in(c['definition'], c['word'], STOP_EN, SUFFIX_EN)
            if hit:
                F['root-def'].append((where, f'"{c["definition"]}" uses ' + ', '.join(f'{t} (from {w})' for w, t in hit)))
            if c['es_word']:
                hit = root_in(c['es_definition'], c['es_word'], STOP_ES, SUFFIX_ES, head=0)
                if hit:
                    F['root-def-es'].append((where, f'{c["es_word"]}: "{c["es_definition"]}" uses ' + ', '.join(t for w, t in hit)))
            # example
            if c['example'] and not has_form(c['example'], c['word'], STOP_EN, SUFFIX_EN):
                F['example'].append((where, f'"{c["example"]}"'))
            if c['es_example'] and c['es_word'] and not has_form(c['es_example'], c['es_word'], STOP_ES, SUFFIX_ES):
                F['example-es'].append((where, f'{c["es_word"]}: "{c["es_example"]}"'))
            # spanish
            for en, es in (('word', 'es_word'), ('definition', 'es_definition'), ('example', 'es_example')):
                if c[en] and c[es] and c[en].strip().lower() == c[es].strip().lower():
                    if en == 'word':
                        F['spanish-same-word'].append((where, f'"{c[es]}"'))
                    elif re.search(r'[a-z]{3}', c[en].lower()):
                        F['spanish'].append((where, f'{es} identical to English: "{c[es]}"'))
            for es in ('es_definition', 'es_example'):
                e, s = lang_score(c[es])
                if e >= 2 and e > s:
                    F['spanish'].append((where, f'{es} reads as English: "{c[es]}"'))
            # long or hard
            n = len(c['definition'].split())
            cap = cw.DEF_CAP[b]
            ws = re.findall(r"[A-Za-z]+", c['definition'])
            syl = sum(map(syllables, ws)) / max(len(ws), 1)
            long_words = [w for w in ws if syllables(w) >= 4 and w.lower() not in c['word'].lower()]
            why = []
            if n >= cap - 1 and syl > SYL[b]:
                why.append(f'{n} words (cap {cap}), {syl:.1f} syllables a word')
            elif n >= 6 and syl > SYL[b] + 0.4:
                why.append(f'{syl:.1f} syllables a word')
            if b == 'k2' and long_words:
                why.append('long words: ' + ', '.join(long_words))
            if why:
                F['long'].append((where, f'[{b}] "{c["definition"]}": ' + '; '.join(why)))
            # house rules
            text = ' '.join(c[k] for k in cw.FIELDS)
            if '\u2014' in text:
                F['house'].append((where, 'em dash'))
            if re.search(r'\bCurio\b(?! Class)', text):
                F['house'].append((where, '"Curio" without "Class"'))
    # specs
    lines = (ROOT / 'data' / 'closet' / 'words' / 'diagrams.py').read_text(encoding='utf-8').splitlines()
    spec = {}
    for n, l in enumerate(lines, 1):
        if l.strip() and not l.lstrip().startswith('#') and ' = ' in l:
            spec[l.partition(' = ')[0].strip()] = n
    cards = {f"{c['module_id']}/{c['slug']}": c for cs in words.values() for c in cs}
    for k, c in cards.items():
        if c['picture'].startswith('svg:') and k not in spec:
            F['spec'].append((c['where'], f'svg card with no spec ({c["picture"]})'))
    for k, n in spec.items():
        if k not in cards:
            F['spec'].append((f'diagrams.py:{n} {k}', 'spec with no card'))
        elif not cards[k]['picture'].startswith('svg:'):
            F['spec'].append((f'diagrams.py:{n} {k}', f'spec for a card whose picture is not svg: ({cards[k]["picture"][:50]})'))
    return F, allowed_empty, sum(len(v) for v in words.values())


TITLES = {
    'dup': 'Duplicates within a module',
    'root-def': 'Word or its root inside its own definition (English)',
    'root-def-es': 'Word or its root inside its own definition (Spanish)',
    'example': 'Example sentence without a form of the word (English)',
    'example-es': 'Example sentence without a form of the word (Spanish)',
    'empty': 'Empty fields (not counting empties allowed by band)',
    'spanish': 'Spanish identical to English, or reading as English',
    'spanish-same-word': 'Spanish word spelled the same as the English word (often a true cognate; listed for a skim)',
    'long': 'Definitions too long or too hard for the grade band',
    'spec': 'Diagram specs and svg cards that do not match',
    'house': 'House rules (em dash, "Curio" alone)',
}


def main():
    F, allowed, total = review()
    out = ['# Word Wall text review', '',
           f'Made by `python scripts/check_words_review.py` over {total} cards (English and Spanish). Review only, no card was '
           'changed. These are heuristics for a person to judge: root and example checks catch real problems but also '
           'some fine cards (a phrase whose main word is ordinary, an irregular form such as ran for run).', '',
           '## Counts', '', '| Check | Findings |', '|---|---|']
    for k, t in TITLES.items():
        out.append(f'| {t} | {len(F[k])} |')
    out += ['', f'Empty by design and not counted: ' + ', '.join(f'{k} {v}' for k, v in sorted(allowed.items())) + '.', '']
    for k, t in TITLES.items():
        out += [f'## {t} ({len(F[k])})', '']
        if not F[k]:
            out += ['None.', '']
            continue
        out += [f'- `{w}`: {n}' for w, n in F[k]] + ['']
    OUT.write_text('\n'.join(out), encoding='utf-8')
    for k, t in TITLES.items():
        print(f'{len(F[k]):5}  {t}')
        if '--print' in sys.argv:
            for w, n in F[k]:
                print('       ', w, ':', n)
    print('wrote', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
