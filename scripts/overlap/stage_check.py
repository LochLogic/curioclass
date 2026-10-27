"""Check gap-fill staging folders before they are merged into data/, and show the coverage they would reach.

    python scripts/overlap/stage_check.py [docs/agents/gapfill/<domain> ...] [--missing] [--quiet]

With no folder, every folder under docs/agents/gapfill/ is checked together. A staging folder holds:
- codes.txt     codes for EXISTING or staged modules, add_codes.py format: `module_id: CODE; CODE  # reason`
- modules.txt   NEW modules, one per line: `source.txt|grade|course|strand|title|description|standards`
                (source.txt is the data/modules file the line will go in; the rest is that file's format)
- concepts.txt  one tool per new module, data/concepts format: `module_id|title|format|family|concept`
- tags.csv      one row per new tool, docs/agents/overlap/tags.csv columns (tool_id,title,band,subject,live,...)

It checks codes against the official lists (standards.validate), courses and grade spans, unique module ids, tool
ids and titles, formats, tag rows and actions, then runs the clash rule (common.pairs) for every pair that includes a
staged tool, flags title words already used 5 or more times, and prints coverage.measure with everything merged.
Exit code 1 when there are errors; clashes and title words are warnings for a person to judge.
"""
import csv, glob, io, os, re, sys, collections
from common import ROOT, OUT, load, pairs, coarse, bands

sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from standards import validate
from coverage import measure

ACTIONS = set('count-along move-along predict-reveal sort match order build compose manipulate simulate-tune experiment '
              'explore hunt solve fix investigate annotate drill choose-path debate converse manage care-for analyze-data '
              'locate discuss rehearse trace plan program compare'.split())
STOP = {'the', 'a', 'an', 'of', 'and', 'in', 'on', 'to', 'for', 'my', 'your', 'it', 'at', 'with', 'what', 'from'}
GRADES = ['k'] + [str(i) for i in range(1, 13)]


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def expand(span):
    a, _, b = span.partition('-')
    return GRADES[GRADES.index(a):GRADES.index(b or a) + 1]


def band_label(grade):
    """The tags.csv band for a module grade span: K-2, 3-5, 6-8, 9-12, K-12, 6-12, or the bands joined by '/'."""
    of = {'k': 'K-2', '1': 'K-2', '2': 'K-2', '3': '3-5', '4': '3-5', '5': '3-5', '6': '6-8', '7': '6-8', '8': '6-8'}
    bs = list(dict.fromkeys(of.get(g, '9-12') for g in expand(grade)))
    if len(bs) == 4: return 'K-12'
    if bs == ['6-8', '9-12']: return '6-12'
    return '/'.join(bs)


def rows(path):
    if not os.path.exists(path): return []
    return [(n, l.rstrip('\r\n')) for n, l in enumerate(io.open(path, encoding='utf-8'), 1)
            if l.strip() and not l.startswith('#')]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dirs = args or sorted(d for d in glob.glob(os.path.join(ROOT, 'docs', 'agents', 'gapfill', '*')) if os.path.isdir(d))
    D = os.path.join(ROOT, 'data')
    courses = {c['course_id']: c for c in csv.DictReader(io.open(os.path.join(D, 'courses.csv'), encoding='utf-8'))}
    formats = {r['format_id'] for r in csv.DictReader(io.open(os.path.join(D, 'formats.csv'), encoding='utf-8'))}
    mods = {m['module_id']: dict(m) for m in csv.DictReader(io.open(os.path.join(D, 'modules.csv'), encoding='utf-8'))}
    concepts = list(csv.DictReader(io.open(os.path.join(D, 'tools-concepts.csv'), encoding='utf-8')))
    titles = {c['title'].lower() for c in concepts}
    tids = {c['tool_id'] for c in concepts}
    errors, warns = [], []
    new_mods, new_concepts, new_tags = {}, [], []

    for d in dirs:
        name = os.path.basename(d.rstrip('/\\'))
        for n, line in rows(os.path.join(d, 'modules.txt')):
            where = f'{name}/modules.txt:{n}'
            p = [x.strip() for x in line.split('|')]
            if len(p) != 7:
                errors.append(f'{where}: expected 7 fields, got {len(p)}'); continue
            src, grade, course, strand, title, desc, std = p
            if not os.path.exists(os.path.join(D, 'modules', src)):
                errors.append(f'{where}: unknown source file {src}')
            if course not in courses:
                errors.append(f'{where}: unknown course {course}'); continue
            try:
                if not set(expand(grade)) <= set(expand(courses[course]['grades'])):
                    errors.append(f'{where}: grade {grade} outside course {course} ({courses[course]["grades"]})')
            except ValueError:
                errors.append(f'{where}: bad grade {grade}'); continue
            codes = [c.strip() for c in std.split(';') if c.strip()]
            bad = [c for c in codes if validate(c) is None]
            if bad or not codes:
                errors.append(f'{where}: invalid or missing codes {bad}')
            mid = f'{courses[course]["subject"]}-{grade}-{slug(title)}'
            if mid in mods or mid in new_mods:
                errors.append(f'{where}: duplicate module id {mid}')
            new_mods[mid] = dict(module_id=mid, subject=courses[course]['subject'], grade=grade, course_id=course,
                                 standards=';'.join(codes), src=src, dir=name)
        for n, line in rows(os.path.join(d, 'concepts.txt')):
            where = f'{name}/concepts.txt:{n}'
            p = [x.strip() for x in line.split('|')]
            if len(p) != 5:
                errors.append(f'{where}: expected 5 fields, got {len(p)}'); continue
            mid, title, fmt, fam, concept = p
            if mid not in new_mods:
                errors.append(f'{where}: module {mid} is not a staged new module')
            if fmt not in formats:
                errors.append(f'{where}: unknown format {fmt}')
            tid = slug(title)
            if title.lower() in titles or tid in tids:
                errors.append(f'{where}: title or id already used: {title}')
            if '—' in line or '–' in line:
                errors.append(f'{where}: em or en dash')
            titles.add(title.lower()); tids.add(tid)
            new_concepts.append(dict(tool_id=tid, title=title, module_id=mid, format=fmt, family=fam, concept=concept,
                                     stage='planned', dir=name))
        tag_path = os.path.join(d, 'tags.csv')
        if os.path.exists(tag_path):
            for r in csv.DictReader(io.open(tag_path, encoding='utf-8')):
                r = dict(r); r['dir'] = name
                new_tags.append(r)

    # every staged module has exactly one concept, every concept one tag row
    per_mod = collections.Counter(c['module_id'] for c in new_concepts)
    errors += [f'{m["dir"]}: module {mid} has {per_mod[mid]} concepts (needs 1)' for mid, m in new_mods.items() if per_mod[mid] != 1]
    by_tid = {c['tool_id']: c for c in new_concepts}
    tagged = {t.get('tool_id') for t in new_tags}
    errors += [f'{c["dir"]}: no tag row for {c["tool_id"]}' for c in new_concepts if c['tool_id'] not in tagged]
    for t in new_tags:
        c = by_tid.get(t.get('tool_id'))
        if not c:
            errors.append(f'{t["dir"]}/tags.csv: {t.get("tool_id")} is not a staged tool'); continue
        if t.get('action') not in ACTIONS:
            errors.append(f'{t["dir"]}/tags.csv: {t["tool_id"]} action {t.get("action")!r} not in the fixed list')
        want = band_label(new_mods[c['module_id']]['grade'])
        if t.get('band') != want:
            errors.append(f'{t["dir"]}/tags.csv: {t["tool_id"]} band {t.get("band")} should be {want}')
        for k in ('skill_key', 'skill', 'setting_group', 'setting'):
            if not t.get(k):
                errors.append(f'{t["dir"]}/tags.csv: {t["tool_id"]} missing {k}')

    # codes for existing or staged modules
    all_mods = dict(mods); all_mods.update(new_mods)
    for d in dirs:
        name = os.path.basename(d.rstrip('/\\'))
        for n, line in rows(os.path.join(d, 'codes.txt')):
            body = line.split('#', 1)[0].strip()
            if not body: continue
            mid, _, codes = body.partition(':')
            mid = mid.strip()
            if mid not in all_mods:
                errors.append(f'{name}/codes.txt:{n}: unknown module {mid}'); continue
            cur = [c for c in all_mods[mid]['standards'].split(';') if c]
            for c in (c.strip() for c in codes.split(';') if c.strip()):
                if validate(c.lstrip('-')) is None:
                    errors.append(f'{name}/codes.txt:{n}: invalid code {c}')
                elif c.startswith('-'):
                    cur = [x for x in cur if x != c[1:]]
                elif c not in cur:
                    cur.append(c)
            all_mods[mid] = dict(all_mods[mid], standards=';'.join(cur))

    # clash rule with staged tools joined to the catalog tags
    cat = load(after=True)
    for t in new_tags:
        if t.get('tool_id') not in by_tid: continue
        r = dict(t); c = by_tid[t['tool_id']]
        r.update(bands=bands(t['band']), grade=new_mods[c['module_id']]['grade'], module_id=c['module_id'],
                 concept=c['concept'], setting_group=coarse(t['setting_group']), changed=True)
        cat.append(r)
    hits = [p for p in pairs(cat) if p[1]['tool_id'] in by_tid or p[2]['tool_id'] in by_tid]
    for band, a, b, m in hits:
        warns.append(f'clash {band}: {a["tool_id"]} <> {b["tool_id"]} ({"+".join(m)})')
    # setting groups crowded in a band
    crowd = collections.Counter((b, r['setting_group']) for r in cat for b in r['bands'] if r['setting_group'] != 'generic')
    for t in new_tags:
        if t.get('tool_id') not in by_tid: continue
        for b in bands(t['band']):
            k = (b, coarse(t['setting_group']))
            if k[1] != 'generic' and crowd[k] >= 6:
                warns.append(f'crowded setting: {t["tool_id"]} adds to {k[1]} in {b} ({crowd[k]} tools)')
    # title words already common across the catalog
    words = collections.Counter(w for c in concepts for w in set(slug(c['title']).split('-')) if w not in STOP)
    for c in new_concepts:
        common = [w for w in slug(c['title']).split('-') if w not in STOP and words[w] >= 5]
        if common:
            warns.append(f'title word: {c["title"]} uses {", ".join(f"{w} ({words[w]})" for w in common)}')

    print(f'{len(dirs)} folders: {len(new_mods)} new modules, {len(new_concepts)} new tools, '
          f'{sum(1 for d in dirs for _ in rows(os.path.join(d, "codes.txt")))} code lines')
    for e in errors: print('ERROR', e)
    if '--quiet' not in sys.argv:
        for w in warns: print('warn ', w)
    else:
        print(f'{len(warns)} warnings (rerun without --quiet to see them)')
    print()
    merged = [dict(c) for c in concepts] + new_concepts
    measure(merged, all_mods, '--missing' in sys.argv)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
