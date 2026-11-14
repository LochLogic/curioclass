r"""Course and unit pages from the course frames (docs/SITE-DESIGN.md, approved 2026-11-14, Desk card q-baseline-1).

    python -X utf8 scripts/course_pages.py check            read every frame and run the copy checks; writes nothing
    python -X utf8 scripts/course_pages.py build [DIR]      write the pages into DIR (default: CURIO_DIST or dist/)
    python scripts/build_site.py --courses                  the same pages inside a whole-site build

Reads data/plans/frames.csv (course, subject, grade, days, minutes, days a week, weeks, term) and each
docs/courses/<slug>/frame.md through scripts/frame.py (the Units table, the Course-level checks table, the calendar
of unit and check days). Writes, under /courses/:
    /courses/                   every core course by subject and grade
    /courses/<slug>/            the course page (the year at a glance, before, after and alongside, credits)
    /courses/<slug>/unit-<n>/   one page per unit (question, days and weeks, what students learn, standards)
Sections and days are not built yet: they come with each course's scope and sequence and day writing.

HIDDEN until Cory says (Desk card q-baseline-1). Every page carries <meta name="robots" content="noindex,nofollow">,
none goes in the sitemap or search index, no menu or find page links to them, the build adds an X-Robots-Tag header
for /courses/*, and dist/.assetsignore gets `courses/*`, so even a deploy of a --courses build uploads none of them.
To show them later: set SHOWN = True below (drops the noindex, the header and the .assetsignore line, and lets
build_site.py add them to the sitemap, search and the find pages), then build with --courses.

Frame cells are planning documents. Only the public columns are read (unit and question, days, what students learn,
why this unit here, owned standards, teacher notes), and inside them any sentence in planning language (base text,
agents, rows, card ids, file paths, candidate check sets) or naming a company or a standards document is dropped
(PRIVATE and NAMES below). `check` prints what was dropped per column and fails on an em dash, "Curio" alone or a
name in what is left.
"""
import csv
import os
import re
import shutil
import sys
from collections import defaultdict
from html import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frame  # noqa: E402

ROOT = frame.ROOT
SHOWN = False   # Cory's switch. False: hidden (noindex, not uploaded, not linked). See the module docstring.

SUBJECTS = [('ela', 'English Language Arts', 'ela'), ('math', 'Math', 'math'), ('science', 'Science', 'science'),
            ('social-studies', 'Social Studies', 'social')]
SUBJECT_LABEL = {s: l for s, l, _ in SUBJECTS}
SUBJECT_COLOR = {s: c for s, _, c in SUBJECTS}
GRADE_ORDER = ['K'] + [str(i) for i in range(1, 13)]
WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# Planning language: a sentence holding any of these is not for a teacher, student or family page.
PRIVATE = re.compile(
    r"base text|base unit|base lesson|base module|base's|\bthe base\b(?! of|-ten| ten)|\b\d\.\d's\b|candidate|desk card|card q-|"
    r'BASELINE|PRODUCTION|docs/|data/|\.md\b|\.csv\b|\.txt\b|S:\\|\bagents?\b|sensitivity read|text agent|text spec|'
    r'pre-work|rubric|bar item|adoption bar|check set|unit plan|section plan|scope and sequence|progression row|'
    r"(?<!by )\brows?\b(?!\s+(?:and|of|in a|in the|on|or|by)\b)|\b(?:grade \w+|ELA|unit \d+|course|it) owns\b|"
    r"(?:^|\. )Owns\b|\bcycles? \d+|Skills Block|\b(?:optional )?lessons? \d+|brief below|shared brief|sits? here|"
    r"\bCory\b|\bprobe\b|\bguard\b|\bthe Desk\b|hard weeks|"
    r'\bframe\b|the lead\b|flagged|source map|source store|gateway|\bleans?\b|if later|'
    r'\btilde\b|~|\bP\d\b|\bstep \d|\brule \d|\bspec\b|to list\b|reference only|reference-only|NonCommercial|'
    r'store folder|\bmodules? \d|this course owns|the course owns|\bowned (?:here|in|by)\b|placed (?:here|in)\b|'
    r'availability|concurrent|skill_id|hands_on|cross_subject|\bnote \d|next course, direct|recall required', re.I)
# Company, product and standards-document names (AGENTS.md: no company names on a reader's page; the science 6 to 12
# frames: the standards document is never named in student, teacher or family copy).
NAMES = re.compile(
    r'Illustrative Math|Kendall|OpenSciEd|EL Education|OpenStax|Oak National|Khan|CK-12|Student Achievement|'
    r'Desmos|GeoGebra|Google|Microsoft|Apple\b|Amazon|YouTube|PhET|Lego|LEGO|Play-Doh|Post-it|Velcro|Slinky|'
    r'Scholastic|Pearson|McGraw|Houghton|Savvas|Newsela|CommonLit|Quizlet|Kahoot|Canva|Padlet|Flip\b|Seesaw|'
    r'Next Generation|NGSS|Common Core|CCSS|Massachusetts 2018|C3 Framework|OSPI|Since Time Immemorial|'
    r'East Tennessee State|ETSU|Kendall Hunt', re.I)
SKILL_IDS = set()
for _p in ('ela', 'math', 'science', 'social-studies'):
    with open(os.path.join(ROOT, 'data', 'progressions', _p + '.csv'), encoding='utf-8') as _f:
        SKILL_IDS.update(r['skill_id'] for r in csv.DictReader(_f) if r.get('skill_id'))
SKILL_RE = re.compile(r'(?<![\w-])(%s)(?![\w-])' % '|'.join(sorted(map(re.escape, SKILL_IDS), key=len, reverse=True)))
INTERNAL_PAREN = re.compile(r'\s*\((?:[^()]*(?:docs/|data/|Desk|BASELINE|card q-|\.md|\.csv|rule \d|step \d|'
                            r'base text|base lesson|frame|row)[^()]*)\)', re.I)
POSITION_PAREN = re.compile(r'\s*\((?:about |weeks? |days? |about days )[^()]*\)', re.I)
dropped = defaultdict(lambda: [0, 0])   # column -> [sentences kept, sentences dropped], for `check`
drop_log = defaultdict(list)


def plain(s):
    s = re.sub(r'\*\*|__|`', '', s or '')
    s = re.sub(r'(?<!\w)\*(?!\s)([^*]+?)\*(?!\w)', r'\1', s)
    s = s.replace('\u2014', ', ').replace('\u2013', ' to ')
    return re.sub(r'\s+', ' ', s).strip()


def sentences(s):
    return [x for x in re.split(r'(?<=[.!?"])\s+(?=[A-Z"(\u201c])', s) if x.strip()]


MODEL_IDS = set()   # the frames' model ids (map-key, food-web): shown as words on a page
for _s in frame.found():
    _, _models = frame.table(frame.section(frame.parse(_s)['text'], 'Models carried'))
    MODEL_IDS.update(m.get('Model', '').strip('` ') for m in _models if '-' in m.get('Model', ''))


def unhyphen_models(s):
    return re.sub(r'\b[a-z]+(?:-[a-z]+)+\b', lambda m: m.group(0).replace('-', ' ') if m.group(0) in MODEL_IDS
                  else m.group(0), s)


def _bad(x):
    return PRIVATE.search(x) or NAMES.search(x) or SKILL_RE.search(x)


def public(text, column):
    """The reader-safe part of a frame cell: internal asides, then planning sentences or clauses, and names dropped."""
    s = unhyphen_models(POSITION_PAREN.sub('', INTERNAL_PAREN.sub('', plain(text))))
    for _ in range(2):   # an aside in parentheses that holds planning language goes, the sentence stays
        s = re.sub(r'\s*\(([^()]*)\)', lambda m: '' if _bad(m.group(1)) else m.group(0), s)
    keep = []
    for x in sentences(s):
        if not _bad(x):
            dropped[column][0] += 1
            keep.append(x)
            continue
        parts = [c for c in re.split(r';\s+', x.rstrip('.')) if not _bad(c)]
        if parts and len(' '.join(parts)) > 25:
            dropped[column][0] += 1
            keep.append('; '.join(parts).rstrip(',:; ') + '.')
            drop_log[column].append('PART ' + x)
        else:
            dropped[column][1] += 1
            drop_log[column].append(x)
    out = ' '.join(keep).strip()
    return out if out.endswith(('.', '?', '!', '"', ')')) or not out else out + '.'


def grade_name(g):
    return 'Kindergarten' if g == 'K' else 'Grade %s' % g


def split_unit_cell(cell):
    """'**Title** (weeks 1 to 3). Anchor: ... Question?' or 'Title. Question?' or 'Title: Question?' ->
    (title, question, rest)."""
    raw = re.sub(r'\s+', ' ', cell or '').strip()
    m = re.match(r'\*\*(.+?)\*\*\s*(.*)$', raw)
    if m:
        title, rest = m.group(1), m.group(2)
    else:
        m = re.match(r'(.+?(?:[.:?]))\s+(?=["*\u201cA-Z])(.*)$', raw)
        title, rest = (m.group(1), m.group(2)) if m else (raw, '')
        title = title.rstrip('.:') if not title.endswith('?') else title
    rest = POSITION_PAREN.sub('', plain(rest)).lstrip('.: ').strip()
    title = plain(title)
    question, other = '', []
    for x in sentences(rest):
        if not question and x.rstrip('"\u201d').endswith('?'):
            question = x.strip('"\u201c\u201d ')
        else:
            other.append(x)
    return title, question, ' '.join(other)


def codes(cell):
    out = []
    for c in re.split(r'[;,]', re.sub(r'\([^()]*\)', '', plain(cell))):
        c = c.strip().lstrip('~').strip()
        if c and re.match(r'^[A-Za-z0-9][\w.\-]*$', c) and not SKILL_RE.fullmatch(c):
            out.append(c)
    return list(dict.fromkeys(out))


def std_slug(code):
    return re.sub(r'[^a-z0-9]+', '-', code.lower()).strip('-')


def known_standards():
    out = set()
    with open(os.path.join(ROOT, 'data', 'modules.csv'), encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            out.update(std_slug(c) for c in r['standards'].split(';') if c)
    return out


def load():
    """Every core course, in subject then grade order, with its units, checks and neighbours."""
    rows = list(csv.DictReader(open(frame.FRAMES_CSV, encoding='utf-8')))
    stds = known_standards()
    courses = []
    for r in rows:
        slug = r['course']
        f = frame.parse(slug)
        cal = frame.calendar(slug) or []
        span = {(k, n, lab): (a, b) for k, n, lab, a, b in cal}
        def weeks(a, b):
            return frame.week(frame.school_day(slug, f, a)), frame.week(frame.school_day(slug, f, b))
        units = []
        for i, u in enumerate(f['table']):
            n = int((re.match(r'\s*(\d+)', u.get('#', '')) or [0, i + 1])[1])
            title, question, rest = split_unit_cell(u.get('Unit and compelling question', ''))
            days = int((re.match(r'\s*(\d+)', u.get('Days', '')) or [0, 0])[1])
            a, b = next(((a, b) for (k, nn, _), (a, b) in span.items() if k == 'unit' and nn == n), (None, None))
            std = [dict(code=c, href='/standards/%s/' % std_slug(c) if std_slug(c) in stds else None)
                   for c in codes(u.get('Owned standards', ''))]
            units.append(dict(n=n, title=title, question=question, anchor=public(rest, 'anchor'), days=days,
                              first=a, last=b, weeks=weeks(a, b) if a else None,
                              learn=public(u.get('What students learn', ''), 'What students learn'),
                              why=public(u.get('Why this unit, here', ''), 'Why this unit, here'),
                              notes=public(u.get('Sensitive topics and teacher notes', ''), 'teacher notes'),
                              standards=std, url='/courses/%s/unit-%d/' % (slug, n), checks=[]))
        _, ctab = frame.table(frame.section(f['text'], 'Course-level checks'))
        what = [public(c.get('What it checks', ''), 'What it checks') for c in ctab]
        checks, by_label = [], {}
        for i, c in enumerate(f['checks']):
            label = plain(c['label'])
            label = re.sub(r'^(\d+)\b', r'Course-level check \1', label)
            item = dict(label=label, after=c['after'], check=c['check'], respond=c['respond'], review=c['review'],
                        what=what[i] if i < len(what) else '', first=None, last=None, weeks=None)
            by_label[c['label']] = item
            checks.append(item)
        # the timeline: units, then each check (review, check and respond days) where the calendar puts it
        year, seen = [], set()
        for kind, n, lab, a, b in cal:
            if kind == 'unit':
                year.append(dict(kind='unit', unit=next(u for u in units if u['n'] == n)))
                continue
            item = by_label.get(lab)
            if item is None:
                continue
            item['first'] = a if item['first'] is None else min(item['first'], a)
            item['last'] = b if item['last'] is None else max(item['last'], b)
            item['weeks'] = weeks(item['first'], item['last'])
            if id(item) not in seen:
                seen.add(id(item))
                year.append(dict(kind='check', check=item))
                u = next((u for u in units if u['n'] == n), None)
                if u:
                    u['checks'].append(item)
        base = plain(frame.bullet(frame.section(f['text'], 'The course in brief'), 'Base text'))
        courses.append(dict(slug=slug, title=plain(r['title']), subject=r['subject'], grade=r['grade'],
                            subject_label=SUBJECT_LABEL[r['subject']], color=SUBJECT_COLOR[r['subject']],
                            units=units, checks=checks, year=year, days=int(r['days']), n_units=int(r['units']),
                            minutes=(int(r['minutes_min']), int(r['minutes_max'])), per_week=int(r['per_week']),
                            weeks=int(r['weeks']), term=r['term'], adapted=not re.match(r'None\b', base),
                            url='/courses/%s/' % slug, placed=bool(cal)))
    order = {g: i for i, g in enumerate(GRADE_ORDER)}
    courses.sort(key=lambda c: ([s for s, _, _ in SUBJECTS].index(c['subject']), order[c['grade']], c['term'] != 'year',
                                c['term'] == 'spring', c['slug']))
    by_subject = defaultdict(list)
    for c in courses:
        by_subject[c['subject']].append(c)
    for c in courses:
        same = by_subject[c['subject']]
        lower = [x for x in same if order[x['grade']] < order[c['grade']]]
        higher = [x for x in same if order[x['grade']] > order[c['grade']]]
        c['before'] = [x for x in lower if x['grade'] == lower[-1]['grade']] if lower else []
        c['after'] = [x for x in higher if x['grade'] == higher[0]['grade']] if higher else []
        c['alongside'] = [x for x in courses if x['grade'] == c['grade'] and x is not c]
        c['lede'] = lede(c)
        c['shape'] = shape(c)
    return courses


def lede(c):
    subj = 'English language arts' if c['subject'] == 'ela' else c['subject_label'].lower()
    return '%s %s: %d units over %d days, from "%s" to "%s".' % (
        grade_name(c['grade']), subj, c['n_units'], c['days'], c['units'][0]['title'], c['units'][-1]['title'])


def shape(c):
    lo, hi = c['minutes']
    mins = '%d to %d minutes' % (lo, hi) if lo != hi else '%d minutes' % lo
    term = {'year': 'the whole school year' if c['weeks'] >= 32 else 'weeks 1 to %d of the school year' % c['weeks'],
            'fall': 'the fall half of the year', 'spring': 'the spring half of the year'}
    pw = 'every school day' if c['per_week'] == 5 else '%s days a week' % WORDS.get(c['per_week'], c['per_week'])
    return dict(minutes=mins, per_week=pw, days=c['days'], weeks=c['weeks'], term=term[c['term']])


# ------------------------------------------------------------------ writing the pages
def make_env():
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    env = Environment(loader=FileSystemLoader(os.path.join(ROOT, 'site', 'templates')),
                      autoescape=select_autoescape(['html', 'xml']), trim_blocks=True, lstrip_blocks=True)
    env.globals.update(library_live=False, closet_live=False, recess_live=False, map_live=False)
    return env


def build(dist, env=None, render=None):
    """Write the course pages into dist. From build_site.py, pass its env and render (render(template, path,
    index=..., **ctx)); alone, the site's templates are loaded here and the pages are written directly."""
    courses = load()
    env = env or make_env()
    n = 0
    def page(template, path, **ctx):
        nonlocal n
        n += 1
        ctx.update(shown=SHOWN, grade_name=grade_name)
        if render:
            render(template, path, index=SHOWN, **ctx)
            return
        out = os.path.join(dist, path.strip('/'), 'index.html')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='utf-8') as f:
            f.write(env.get_template(template).render(path=path, **ctx))
    if os.path.isdir(os.path.join(dist, 'courses')):
        shutil.rmtree(os.path.join(dist, 'courses'))
    grid = {g: {s: [c for c in courses if c['grade'] == g and c['subject'] == s] for s, _, _ in SUBJECTS}
            for g in GRADE_ORDER}
    page('courses/index.html', '/courses/', courses=courses, grid=grid, grades=GRADE_ORDER, subjects=SUBJECTS)
    for c in courses:
        page('courses/course.html', c['url'], c=c)
        for i, u in enumerate(c['units']):
            page('courses/unit.html', u['url'], c=c, u=u, prev=c['units'][i - 1] if i else None,
                 next=c['units'][i + 1] if i + 1 < len(c['units']) else None)
    hide(dist)
    return courses, n


def hide(dist):
    """Keep the course pages out of any upload and away from search engines until SHOWN (see the docstring)."""
    if SHOWN:
        return
    ignore = os.path.join(dist, '.assetsignore')
    lines = open(ignore, encoding='utf-8').read().splitlines() if os.path.exists(ignore) else ['.assetsignore']
    if 'courses/*' not in lines:
        lines.append('courses/*')
    with open(ignore, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    headers = os.path.join(dist, '_headers')
    text = open(headers, encoding='utf-8').read() if os.path.exists(headers) else ''
    if '/courses/*' not in text:
        with open(headers, 'a', encoding='utf-8') as f:
            f.write('/courses/*\n  X-Robots-Tag: noindex, nofollow\n')


# ------------------------------------------------------------------ the check
def check():
    courses = load()
    fails = []
    for c in courses:
        if not c['placed']:
            fails.append('%s: frame.py could not place its course-level checks; the year at a glance has no check rows'
                         % c['slug'])
        for u in c['units']:
            if not u['question']:
                fails.append('%s unit %d: no compelling question found' % (c['slug'], u['n']))
            if not u['learn']:
                fails.append('%s unit %d: nothing left of "What students learn" after the planning sentences went'
                             % (c['slug'], u['n']))
            for k in ('title', 'question', 'anchor', 'learn', 'why', 'notes'):
                v = u[k]
                if '\u2014' in v:
                    fails.append('%s unit %d %s: an em dash' % (c['slug'], u['n'], k))
                if re.search(r'\bCurio\b(?! Class)', v):
                    fails.append('%s unit %d %s: "Curio" alone' % (c['slug'], u['n'], k))
                if NAMES.search(v):
                    fails.append('%s unit %d %s: a name (%s)' % (c['slug'], u['n'], k, NAMES.search(v).group(0)))
        for ch in c['checks']:
            if NAMES.search(ch['what']) or '\u2014' in ch['what']:
                fails.append('%s %s: a name or em dash in What it checks' % (c['slug'], ch['label']))
    pages = 1 + len(courses) + sum(len(c['units']) for c in courses)
    print('%d courses, %d units, %d pages' % (len(courses), sum(len(c['units']) for c in courses), pages))
    for col, (k, d) in sorted(dropped.items()):
        print('  %-22s %4d sentences kept, %4d dropped as planning language or names' % (col, k, d))
    if '--dropped' in sys.argv:
        for col, xs in drop_log.items():
            print('\n== dropped from', col)
            for x in xs:
                print('  -', x[:220])
    for x in fails:
        print('FAIL', x)
    return 1 if fails else 0


def main(argv):
    if not argv or argv[0] == 'check':
        return check()
    if argv[0] == 'build':
        dist = argv[1] if len(argv) > 1 and not argv[1].startswith('--') else \
            os.environ.get('CURIO_DIST') or os.path.join(ROOT, 'dist')
        if not os.path.isdir(os.path.join(dist, 'assets')):
            sys.exit('%s has no built site (assets/); run scripts/build_site.py first, or name a built copy' % dist)
        courses, n = build(dist)
        print('%d course pages and unit pages for %d courses -> %s/courses/ (%s)'
              % (n, len(courses), dist, 'shown' if SHOWN else 'hidden: noindex, not uploaded, not linked'))
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
