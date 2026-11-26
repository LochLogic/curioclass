"""US spelling sweep over the course homes (later.csv L126; Cory 2026-11-25 reversed Desk q-fix-health-2 for these words).

    python -X utf8 scripts/us_spelling.py --dry-run [--course <course>]   counts per word and file, writes nothing
    python -X utf8 scripts/us_spelling.py [--course <course>]             writes
    --skip <course,course>   leaves those courses out (lanes running on them)

Fixes the UK spellings in WORDS, and only those, in what Curio Class writes itself:
- docs/courses/<course>/**/*.md and courses/<course>/**/*.md (skeletons are generated and skipped);
- the text cells of data/plans/<course>/*.csv, except columns that name someone else's work (sources.csv title and
  citation; url and text_ref anywhere) and key columns.
Skipped, as lint.py skips them: quoted text ("..." and curly quotes), inline code and fenced code, link targets,
urls, `[[...]]` markers, html tags, file names (four course files keep a UK word in their names; their names
are not prose), and a path or slug (a token with both a slash and a hyphen, such as u03-1/labelled-note-page).
Proper names in KEEP are never changed (Open Government Licence). Paths data/homes.csv marks never-touch, state or
generated are skipped. Changed CSV records are rewritten one record at a time (rows.records/line); every other record
and every line ending stays byte for byte. Writes go through scripts/safe_write.py.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import homes  # noqa: E402
import rows  # noqa: E402
import safe_write  # noqa: E402

WORDS = {'labelled': 'labeled', 'licence': 'license', 'practise': 'practice', 'recognise': 'recognize',
         'practised': 'practiced', 'practises': 'practices', 'modelled': 'modeled', 'modelling': 'modeling',
         'colour': 'color',
         # L123 (2026-11-26): the other UK spellings written plan prose still held
         'centimetre': 'centimeter', 'centimetres': 'centimeters', 'millimetre': 'millimeter',
         'millimetres': 'millimeters', 'metre': 'meter', 'metres': 'meters', 'kilometre': 'kilometer',
         'kilometres': 'kilometers', 'litre': 'liter', 'litres': 'liters', 'millilitre': 'milliliter',
         'millilitres': 'milliliters', 'mould': 'mold', 'moulds': 'molds', 'behaviour': 'behavior',
         'behaviours': 'behaviors', 'favourite': 'favorite', 'favourites': 'favorites', 'colours': 'colors',
         'coloured': 'colored', 'organise': 'organize', 'organised': 'organized', 'organising': 'organizing',
         'recognised': 'recognized', 'recognising': 'recognizing', 'analyse': 'analyze', 'analysed': 'analyzed',
         'neighbour': 'neighbor', 'neighbours': 'neighbors', 'labelling': 'labeling', 'practising': 'practicing'}
WORD = re.compile(r'(?<!\w)(' + '|'.join(sorted(WORDS, key=len, reverse=True)) + r')(?!\w)', re.I)
PATHLIKE = r'[\w.-]*-[\w.-]*/[\w./-]*|[\w./-]*/[\w.]*-[\w./-]*'   # a/b-c or a-b/c: a folder or slug, not prose
KEEP = re.compile(r'Government Licence', re.I)


def _file_stems():
    """Names of course files that hold a WORDS spelling (script-in-colours-day-124): a bare reference to one is a
    name, not prose (L123, 2026-11-26: the sweep had renamed two such references)."""
    out = set()
    for p in (ROOT / 'courses').rglob('*.md'):
        if WORD.search(p.stem):
            out.add(re.escape(p.stem))
    return out


STEMS = _file_stems()
PROTECT = re.compile(r'"[^"\n]*"|“[^”\n]*”|`[^`\n]*`|\[\[[^\]\n]*\]\]|\]\([^)\n]*\)|https?://\S+|'
                     r'<[^>\n]*>|[\w./-]+\.(?:md|csv|pdf|png|svg|jpe?g|html|json|txt)\b|' + PATHLIKE + '|' +
                     KEEP.pattern + ''.join(r'|(?<![\w-])' + x + r'(?![\w-])' for x in sorted(STEMS, key=len, reverse=True)),
                     re.I)
SKIP_COLS = {'sources.csv': {'title', 'citation', 'url'}, '': {'url', 'text_ref'}}   # sources.csv names real works
SKIP_KINDS = {'never-touch', 'state', 'blind', 'generated-ignored', 'generated'}


def case_like(src, new):
    if src.isupper():
        return new.upper()
    if src[0].isupper():
        return new[0].upper() + new[1:]
    return new


def fix(text, counts):
    """text with WORDS fixed outside protected spans."""
    out, at = [], 0
    for m in PROTECT.finditer(text):
        out.append(_fix_bare(text[at:m.start()], counts))
        out.append(m.group(0))
        at = m.end()
    out.append(_fix_bare(text[at:], counts))
    return ''.join(out)


def _fix_bare(s, counts):
    def rep(m):
        w = m.group(1)
        counts[w.lower()] = counts.get(w.lower(), 0) + 1
        return case_like(w, WORDS[w.lower()])
    return WORD.sub(rep, s)


def fix_md(text, counts):
    out, fence = [], False
    for ln in text.splitlines(keepends=True):
        if ln.lstrip().startswith('```'):
            fence = not fence
            out.append(ln)
            continue
        out.append(ln if fence else fix(ln, counts))
    return ''.join(out)


def fix_csv(text, counts, name=''):
    recs = rows.records(text)
    if not recs:
        return text
    head = recs[0][1]
    cols = SKIP_COLS.get(name, set()) | SKIP_COLS['']
    skip = {i for i, c in enumerate(head) if c in cols or c == 'id' or c.endswith('_id') or c == 'key'}
    out = [recs[0][0]]
    for raw, fields in recs[1:]:
        new = [f if i in skip else fix(f, counts) for i, f in enumerate(fields)]
        if new == fields:
            out.append(raw)
        else:
            nl = '\r\n' if raw.endswith('\r\n') else '\n' if raw.endswith('\n') else ''
            out.append(rows.line(new, nl or '\n')[:None if nl else -1])
    return ''.join(out)


def targets(course):
    for base in (ROOT / 'docs' / 'courses' / course, ROOT / 'courses' / course):
        if base.is_dir():
            yield from (p for p in sorted(base.rglob('*.md')) if 'skeletons' not in p.parts)
    d = ROOT / 'data' / 'plans' / course
    if d.is_dir():
        yield from sorted(d.glob('*.csv'))


def shared_targets(cl):
    """The living rule docs beside the courses: docs/courses/*.md and the subject folders (APPROACH.md, STANDARD.md)."""
    d = ROOT / 'docs' / 'courses'
    yield from sorted(d.glob('*.md'))
    for sub in sorted(p for p in d.iterdir() if p.is_dir() and p.name not in cl):
        yield from (p for p in sorted(sub.rglob('*.md')) if 'skeletons' not in p.parts)


def courses():
    import gate
    return gate.courses()


def main(a):
    dry = '--dry-run' in a
    scope = [a[a.index('--course') + 1]] if '--course' in a else courses()
    skip = set(a[a.index('--skip') + 1].split(',')) if '--skip' in a else set()   # courses another worker holds
    scope = [c for c in scope if c not in skip]
    total, files = {}, 0
    groups = [targets(c) for c in scope] + ([] if '--course' in a else [shared_targets(set(courses()))])
    for g in groups:
        for p in g:
            rel = p.relative_to(ROOT).as_posix()
            r = homes.row_of(rel)
            if r is None or r['kind'] in SKIP_KINDS:
                continue
            text = p.read_bytes().decode('utf-8')
            counts = {}
            new = fix_csv(text, counts, p.name) if p.suffix == '.csv' else fix_md(text, counts)
            if new == text:
                continue
            files += 1
            for k, v in counts.items():
                total[k] = total.get(k, 0) + v
            print('%s %s: %s' % ('would fix' if dry else 'fixed', rel,
                                 ', '.join('%s x%d' % kv for kv in sorted(counts.items()))))
            if not dry:
                with safe_write.lock(p):
                    safe_write.replace(p, new)
    print('us_spelling: %s %d words in %d files: %s' % ('would fix' if dry else 'fixed', sum(total.values()), files,
                                                       ', '.join('%s %d' % kv for kv in sorted(total.items()))))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
