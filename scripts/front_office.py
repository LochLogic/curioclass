r"""The Front Office and Show Your Work: the whole curriculum, top to bottom, for leaders (DRAFT, Cory 2026-11-17).

    python -X utf8 scripts/front_office.py check          build into a scratch folder and run the copy checks
    python -X utf8 scripts/front_office.py build [DIR]    write the pages into DIR (default: CURIO_DIST or dist/)
    python scripts/build_site.py                          also builds them, inside every whole-site build

Writes /front-office/ (the map, one page), /front-office/show-your-work/ (the method, one page),
/front-office/data/<subject>.json and <subject>-ladder.json, and through scripts/front_office_docs.py one
docs/<course>/course.json plus one docs/<course>/u<NN>.json per unit with documents (docs/SITE-DESIGN.md). Every
course, unit, section and day opens in the map's reader from that data, so no page is made per layer.

A DRAFT: noindex, out of the sitemap and search, linked only from the site footer (2026-11-19). Who did the work is never said either way
(no tool or model names, no "expert" or "teacher" readers implied); the checks are described, not the checkers.

Reads: data/plans/frames.csv and the frames (through course_pages.load, which already drops planning language),
data/progressions/<subject>.csv, data/plans/<course>/days.csv (day, unit, section, kind, goal only),
docs/courses/<course>/ (which layers exist), courses/<course>/ (days written), data/plans/flow-results.csv
(review summaries, cleaned below). Never reads the blind paths (docs/courses/math-4/, data/plans/math-4/, ela-6).
"""
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import course_pages as cp  # noqa: E402
import front_office_docs as fod  # noqa: E402

from pathlib import Path
ROOT = Path(cp.ROOT)
BLIND = re.compile(r'math-4|ela-6')
PROG_FILE = {'ela': 'ela', 'math': 'math', 'science': 'science', 'social-studies': 'social-studies'}
# Words that must never reach these pages: who did the work, and internal machinery.
FORBIDDEN = re.compile(r'\b(?:AI|A\.I\.|Claude|Codex|GPT|Sonnet|Opus|Haiku|Gemini|agents?|model(?:s)? (?:wrote|read)|'
                       r'LLM|Cory|Sara|Desk|card q-|later\.csv|BASELINE)\b|\.md\b|\.csv\b|—|\bCurio\b(?! Class)')
STRAND_LABEL = {}
fod.FORBIDDEN = FORBIDDEN


def clean_goal(g):
    s = cp.plain(g or '')
    s = re.sub(r'\s*\((?:[^()]*(?:\.md|\.csv|card q-|Desk|L\d\d)[^()]*)\)', '', s)
    s = re.sub(r'\b[a-z]{2,4}\d{0,2}-[a-z0-9-]+\b', '', s)          # skill ids like ss5-revolution-causes
    s = re.sub(r'\s{2,}', ' ', s).strip(' ,;')
    if FORBIDDEN.search(s):
        return ''
    return s[:1].upper() + s[1:]


def review_summary(text):
    """A flow-results line, cleaned for the public: counts kept, readers unnamed, anything internal dropped."""
    s = re.sub(r'Expert (\d+) findings?, Codex (\d+)(?: \(overlapping\))?',
               lambda m: 'Two separate reads raised %s and %s findings' % (m.group(1), m.group(2)), text)
    s = re.sub(r'Expert (\d+) findings?', r'The first read raised \1 findings', s)
    s = re.sub(r'Codex (\d+) findings?', r'a second read raised \1', s)
    out = []
    for x in re.split(r'(?<=[.!?])\s+', s):
        x = re.sub(r'\s*\([^()]*(?:Desk|card|\.md|\.csv|L\d+)[^()]*\)', '', x)
        if re.match(r'(?:To Cory|Nothing (?:new )?for Cory|Old grade 4)', x) or FORBIDDEN.search(x):
            continue
        out.append(x.strip())
    return ' '.join(x for x in out if x)


def layer_status(slug):
    d = ROOT / 'docs' / 'courses' / slug
    units = sorted(d.glob('s[0-9][0-9].md')) if d.is_dir() else []
    days_dir = ROOT / 'courses' / slug
    written = sorted({p.stem for p in days_dir.glob('*/d[0-9][0-9][0-9].md')}) if days_dir.is_dir() else []
    return dict(frame=(d / 'frame.md').exists(), scope=(d / 'scope-and-sequence.md').exists(), unit_plans=len(units),
                written=[int(w[1:]) for w in written])


def days_for(slug):
    p = ROOT / 'data' / 'plans' / slug / 'days.csv'
    if BLIND.search(slug) or not p.exists():
        return []
    out, last_unit = [], 1
    for r in sorted(csv.DictReader(open(p, encoding='utf-8')), key=lambda r: int(r['day']) if r['day'].isdigit() else 0):
        if not r['day'].isdigit():
            continue
        if (r['stretch'] or '').isdigit():
            last_unit = int(r['stretch'])
            out.append(dict(d=int(r['day']), u=last_unit, s=r['unit'], k=r['kind'], g=clean_goal(r['goal'])))
        else:   # a course-level check day ("C"): shown after the unit it follows
            out.append(dict(d=int(r['day']), u=last_unit, s='Course-level check', k='Check', g=clean_goal(r['goal'])))
    return out


def progressions(subject):
    p = ROOT / 'data' / 'progressions' / ('%s.csv' % PROG_FILE[subject])
    rows = list(csv.DictReader(open(p, encoding='utf-8')))
    grades = cp.GRADE_ORDER
    strands = defaultdict(Counter)
    for r in rows:
        strands[r['strand']][r['grade']] += 1
    return dict(skills=len(rows), grades=grades,
                strands=[dict(name=k.replace('-', ' ').capitalize(), by_grade=[v.get(g, 0) for g in grades])
                         for k, v in sorted(strands.items(), key=lambda kv: -sum(kv[1].values()))])


def build_data(docdir=None):
    courses = cp.load()
    out = {}
    totals = Counter()
    for subj, label, color in cp.SUBJECTS:
        cs = []
        for c in [c for c in courses if c['subject'] == subj]:
            st = layer_status(c['slug'])
            days = days_for(c['slug'])
            written = set(st['written'])
            have = fod.course_docs(ROOT, c['slug'], days, docdir) if docdir and not BLIND.search(c['slug']) else None
            hu = (have or {}).get('units', {})
            by_unit = defaultdict(lambda: defaultdict(list))
            for d in days:
                by_unit[d['u']][d['s']].append(dict(d=d['d'], k=d['k'], g=d['g'], w=d['d'] in written))
            units = []
            for u in c['units']:
                secs = by_unit.get(u['n'], {})
                hx = hu.get(u['n'], {})
                units.append(dict(n=u['n'], t=u['title'], q=u['question'], days=u['days'],
                                  plan=hx.get('plan', False), sp=hx.get('sections', []),
                                  weeks=list(u['weeks']) if u['weeks'] else None, learn=u['learn'], why=u['why'],
                                  std=[s['code'] for s in u['standards']],
                                  checks=[x['label'] for x in u['checks']],
                                  sections=[dict(id=k, days=v) for k, v in sorted(
                                      secs.items(), key=lambda kv: kv[1][0]['d'])]))
            n_sections = sum(1 for u in units for s in u['sections'] if s['id'] != 'Course-level check')
            plan_state = ('written' if subj == 'social-studies' else 'outlined') if st['unit_plans'] else 'none'
            cs.append(dict(slug=c['slug'], t=c['title'], g=c['grade'], term=c['term'], days=c['days'],
                           n_units=c['n_units'], lede=c['lede'], shape=c['shape'],
                           before=[x['slug'] for x in c['before']], after=[x['slug'] for x in c['after']],
                           docs=dict(frame=bool(have and have['frame']), scope=bool(have and have['scope'])),
                           status=dict(frame=st['frame'], scope=st['scope'], unit_plans=st['unit_plans'],
                                       unit_state=plan_state, sections=n_sections, planned=len(days),
                                       written=len(st['written'])),
                           units=units))
            totals['courses'] += 1
            totals['frames'] += st['frame']
            totals['scopes'] += st['scope']
            totals['units'] += c['n_units']
            totals['unit_plans'] += st['unit_plans']
            totals['unit_written'] += st['unit_plans'] if plan_state == 'written' else 0
            totals['sections'] += n_sections
            totals['days'] += len(days)
            totals['written'] += len(st['written'])
        prog = progressions(subj)
        if docdir:
            rows = list(csv.DictReader(open(ROOT / 'data' / 'progressions' / ('%s.csv' % PROG_FILE[subj]),
                                            encoding='utf-8')))
            (docdir.parent / 'data' / ('%s-ladder.json' % subj)).write_text(json.dumps(
                fod.ladder(rows, cp.GRADE_ORDER), ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
        totals['skills'] += prog['skills']
        out[subj] = dict(subject=subj, label=label, color=color, progressions=prog, courses=cs)
    return out, totals


def reviews():
    rows = list(csv.DictReader(open(ROOT / 'data' / 'plans' / 'flow-results.csv', encoding='utf-8')))
    names = {c['slug']: c['title'] for c in cp.load()}
    groups = defaultdict(list)
    for r in rows:
        kind, _, what = r['node'].partition(':')
        text = review_summary(r['result'])
        if not text:
            continue
        if kind == 'prog-review':
            title = 'All four subjects together' if what == 'all' else cp.SUBJECT_LABEL.get(
                what if what != 'english-language-arts' else 'ela', what.replace('-', ' ').title())
            groups['Progressions'].append(dict(t=title, s=text))
        elif kind == 'frame':
            groups['Course frames'].append(dict(t=names.get(what, what), s=text))
    for v in groups.values():
        v.sort(key=lambda x: x['t'])
    return [dict(layer=k, items=groups[k]) for k in ['Progressions', 'Course frames'] if groups.get(k)]


def base_texts():
    """The base texts and the open references, with their licences (docs/sources/BASE-TEXTS.md)."""
    by = 'https://creativecommons.org/licenses/by/4.0/'
    return [
        dict(name='Illustrative Mathematics K-12 Math', ed='1st edition, 2019 to 2021', lic='CC BY 4.0', url=by,
             use='Math, kindergarten to grade 8, Algebra I, Geometry and Algebra II'),
        dict(name='OpenSciEd Middle School', ed='2022 standard units', lic='CC BY 4.0', url=by,
             use='Science, grades 6 to 8'),
        dict(name='EL Education K-5 Language Arts Curriculum', ed='2017 edition', lic='CC BY 4.0', url=by,
             use='English language arts, kindergarten to grade 5'),
        dict(name='OpenStax, Precalculus', ed='1st edition', lic='CC BY 4.0', url=by, use='Precalculus'),
        dict(name='OpenStax, Statistics and Introductory Statistics', ed='2020 and 1st edition', lic='CC BY 4.0',
             url=by, use='Statistics'),
        dict(name='Online Statistics Education (David M. Lane, project leader)', ed='Online edition',
             lic='Public domain', url='', use='Statistics, where the main text leaves a gap'),
        dict(name='Dale Hoffman, Contemporary Calculus', ed='2016 archive edition', lic='CC BY 3.0 US',
             url='https://creativecommons.org/licenses/by/3.0/us/', use='Calculus'),
        dict(name='Steven Earle, Physical Geology', ed='2nd edition, 2019', lic='CC BY 4.0', url=by,
             use='Earth and Space Science, units 1 to 4 and 7'),
        dict(name='OpenStax, Astronomy', ed='1st edition', lic='CC BY 4.0', url=by,
             use='Earth and Space Science, units 8 and 9'),
        dict(name='JetStream, An Online School for Weather (National Weather Service)', ed='Online lessons',
             lic='Public domain', url='', use='Earth and Space Science, units 5 to 7'),
        dict(name='Emily P. Harris, Introduction to Environmental Sciences and Sustainability', ed='2023',
             lic='CC BY 4.0', url=by, use='Environmental Science'),
    ]


def build(dist, env=None, render=None):
    from pathlib import Path
    dist = Path(dist)
    ddir = dist / 'front-office' / 'data'
    ddir.mkdir(parents=True, exist_ok=True)
    data, totals = build_data(dist / 'front-office' / 'docs')
    for subj, d in data.items():
        (ddir / ('%s.json' % subj)).write_text(json.dumps(d, separators=(',', ':'), ensure_ascii=False),
                                               encoding='utf-8')
    subjects = [dict(id=s, label=l, color=c, courses=len(data[s]['courses']),
                     skills=data[s]['progressions']['skills']) for s, l, c in cp.SUBJECTS]
    # One hash of every document: the page asks for /front-office/docs/...?v=<hash>, so the Worker and browsers may
    # cache each document for a year and a new build is never served stale (worker/index.js, scripts/sync_media.py).
    import hashlib
    h = hashlib.sha1()
    for p in sorted((dist / 'front-office' / 'docs').rglob('*.json')):
        h.update(p.relative_to(dist).as_posix().encode())
        h.update(p.read_bytes())
    ctx = dict(totals=dict(totals), subjects=subjects, reviews=reviews(), base_texts=base_texts(), docv=h.hexdigest()[:12])
    if render is None:
        env = env or cp.make_env()
        out = dist / 'front-office'
        for tpl, path in [('front-office/index.html', '/front-office/'),
                          ('front-office/show-your-work.html', '/front-office/show-your-work/')]:
            p = dist / path.strip('/') / 'index.html'
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(env.get_template(tpl).render(path=path, **ctx), encoding='utf-8')
    else:
        render('front-office/index.html', '/front-office/', index=False, **ctx)
        render('front-office/show-your-work.html', '/front-office/show-your-work/', index=False, **ctx)
    return totals


def check(dist):
    totals = build(dist)
    bad = []
    for p in sorted((dist / 'front-office').rglob('*')):
        if p.is_file():
            text = p.read_text(encoding='utf-8')
            visible = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', '', text, flags=re.S)
            for m in FORBIDDEN.finditer(visible if p.suffix == '.html' else text):
                bad.append('%s: %r' % (p.relative_to(dist), text[max(0, m.start() - 40):m.end() + 40]))
    n = sum(1 for p in (dist / 'front-office').rglob('*') if p.is_file())
    print('front office: %d files; %s' % (n, dict(totals)))
    for b in bad[:40]:
        print('FAIL', b)
    return 1 if bad else 0


def main(argv):
    from pathlib import Path
    cmd = argv[1] if len(argv) > 1 else 'check'
    if cmd == 'build':
        dist = Path(argv[2] if len(argv) > 2 else os.environ.get('CURIO_DIST', ROOT / 'dist'))
        print(dict(build(dist)))
        return 0
    import tempfile
    return check(Path(tempfile.mkdtemp(prefix='front-office-')))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
