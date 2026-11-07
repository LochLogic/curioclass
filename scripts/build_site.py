"""Build the Curio Class static site into dist/ from the catalog data and tools/.

Run from the repo root:  python scripts/build_site.py
Needs Jinja2 and Markdown (pip install jinja2 markdown). No other dependencies.
"""
import base64, csv, json, random, re, shutil, sys
from collections import defaultdict
from datetime import date
from html import escape as html_escape
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
DATA, SITE, TOOLS = ROOT / 'data', ROOT / 'site', ROOT / 'tools'
DIST = Path(__import__('os').environ.get('CURIO_DIST') or ROOT / 'dist')  # CURIO_DIST: build somewhere else (tests)
BASE_URL = 'https://curioclass.org'
sys.path.insert(0, str(Path(__file__).parent))
from standards import validate  # noqa: E402
from bundle_tool import bundle_all  # noqa: E402
import check_plans  # noqa: E402
import check_words  # noqa: E402
import check_games  # noqa: E402
import check_breaks  # noqa: E402
import qr  # noqa: E402
import check_charts  # noqa: E402
import check_worksheets  # noqa: E402
import worksheets as ws  # noqa: E402
import gen_links  # noqa: E402
import ws_generated  # noqa: E402
import charts as chart_svg  # noqa: E402
import teaching_map as tmap  # noqa: E402

bundle_all()  # tools with src.html get their art inlined first

GRADES = ['k'] + [str(i) for i in range(1, 13)]
SUBJECT_COLOR = {'math': 'math', 'ela': 'ela', 'science': 'science', 'social-studies': 'social', 'arts': 'arts',
                 'health-pe': 'health', 'computer-science': 'cs', 'world-languages': 'lang', 'cte': 'cte',
                 'sel': 'sel', 'eld': 'eld', 'library': 'library'}
SUBJECT_SHORT = {'world-languages': 'World Languages and ASL', 'cte': 'Careers and Finance', 'sel': 'Social and Emotional',
                 'eld': 'English Learners', 'library': 'Library and Research', 'health-pe': 'Health and PE'}
FREE_FORMATS = {'explorer', 'sandbox', 'studio', 'simulator', 'map', 'timeline'}


def read(name):
    with open(DATA / name, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def expand(span):
    a, _, b = span.partition('-')
    return GRADES[GRADES.index(a):GRADES.index(b or a) + 1]


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def grade_label(g):
    if g == 'k':
        return 'Kindergarten'
    if '-' in g:
        a, b = g.split('-')
        return f'Grades {a.upper()}-{b}'
    return f'Grade {g}'


def grade_href(g):
    """Grade or band page for a module's grade span, or None when no such page exists."""
    if g in GRADES:
        return f'/grades/{g}/'
    return f'/grades/{g}/' if g in ('k-2', '3-5', '6-8', '9-12') else None


def grade_short(g):
    return g.upper() if g == 'k' else g


# ---------- load catalog ----------
subjects = {s['subject_id']: dict(s, color=SUBJECT_COLOR[s['subject_id']], short=SUBJECT_SHORT.get(s['subject_id'], s['label']))
            for s in read('subjects.csv')}
grades = {g['grade_id']: g for g in read('grades.csv')}
bands = {b['band_id']: dict(b, grade_list=b['grades'].split(';')) for b in read('bands.csv')}
BAND_SLUG = {'k2': 'k-2', '35': '3-5', '68': '6-8', '912': '9-12'}
formats = {f['format_id']: f for f in read('formats.csv')}
courses = {c['course_id']: c for c in read('courses.csv')}
modules = {m['module_id']: dict(m, grades=expand(m['grade']), codes=m['standards'].split(';'), url=f'/modules/{m["module_id"]}/')
           for m in read('modules.csv')}

tools = []
for c in read('tools-concepts.csv'):
    m = modules[c['module_id']]
    t = dict(c, module=m, subject_info=subjects[m['subject']], format_info=formats[c['format']],
             url=f'/tools/{c["tool_id"]}/', built=False, meta=None)
    folder = TOOLS / c['tool_id']
    if (folder / 'tool.json').exists():
        t['built'] = True
        t['meta'] = json.loads((folder / 'tool.json').read_text(encoding='utf-8'))
        t['file'] = f'{c["tool_id"]}.html'
        t['size_kb'] = round((folder / t['file']).stat().st_size / 1024)
        notes = folder / 'notes.md'
        t['notes_html'] = markdown.markdown(notes.read_text(encoding='utf-8')) if notes.exists() else ''
        t['preview'] = (folder / 'preview.svg').exists()
        t['plan'] = check_plans.parse(c['tool_id'])
        bad = check_plans.problems(c['tool_id'], m) + check_plans.exit_problems(c['tool_id'], m)
        t['exit'] = check_plans.parse_exit(c['tool_id']) if t['plan'] else None
        if bad:
            sys.exit(f"{c['tool_id']}/plan.md: " + '; '.join(bad) + ' (python scripts/check_plans.py)')
        span = re.search(r'(K|\d+)(?:-(\d+))?$', t['meta'].get('grades_label', ''))
        t['fit'] = expand(f'{span[1]}-{span[2] or span[1]}'.lower()) if span else m['grades']
    tools.append(t)
by_module = defaultdict(list)
for t in tools:
    by_module[t['module_id']].append(t)
built = [t for t in tools if t['built']]
bench = [t for t in tools if not t['built']]

families = defaultdict(list)
for t in tools:
    if t['family']:
        families[t['family']].append(t)
families = {k: sorted(v, key=lambda t: GRADES.index(t['module']['grades'][0])) for k, v in families.items() if len(v) > 1}

standards = defaultdict(list)
for m in modules.values():
    for code in m['codes']:
        standards[code].extend(by_module[m['module_id']])
std_framework = {code: validate(code) for code in standards}
CSS_HEX = dict(re.findall(r'--([a-z]+): (#[0-9a-f]{6});', (ROOT / 'site' / 'assets' / 'curio.css').read_text(encoding='utf-8')))

# The Map (docs/SUPPLY-CLOSET-PLAN.md, Phase F): stops in teaching order per subject-grade region, from data/sequence.csv.
# Upkeep is one sequence.csv row per new module; a missing row only warns (the module joins the end of its region).
map_regions, map_warn = tmap.load(modules, GRADES)
for _w in map_warn:
    print('Map warning:', _w)
map_at = {}
for _k, _stops in map_regions.items():
    for _s in _stops:
        _s['ready'] = any(t['built'] for t in by_module[_s['m']['module_id']])
        map_at[_s['m']['module_id']] = _k


def map_url(k):
    return f'/map/{k[0]}/{k[1]}/'


def map_title(k):
    return f"{grade_label(k[1])} {subjects[k[0]]['short']}"


def map_spots(mods):
    """Where a standard's modules sit on the Map: a small strip per region, its stops filled."""
    hits, spots = {m['module_id'] for m in mods}, []
    for k in dict.fromkeys(map_at[m['module_id']] for m in mods):
        stops = map_regions[k]
        nums = [s['n'] for s in stops if s['m']['module_id'] in hits]
        label = f"{map_title(k)}: stop{'s' if len(nums) > 1 else ''} {', '.join(map(str, nums))} of {len(stops)}"
        spots.append(dict(title=map_title(k), url=map_url(k), label=label,
                          svg=tmap.strip(stops, hits, CSS_HEX[subjects[k[0]]['color']], label)))
    return spots


def module_groups(mods):
    """Order modules by subject then grade, attaching tools."""
    out = defaultdict(list)
    for m in mods:
        out[m['subject']].append(dict(m, tools=by_module[m['module_id']]))
    return [(subjects[s], out[s]) for s in subjects if s in out]


# ---------- render ----------
env = Environment(loader=FileSystemLoader(SITE / 'templates'), autoescape=select_autoescape(['html', 'xml']),
                  trim_blocks=True, lstrip_blocks=True)
env.globals.update(subjects=subjects, formats=formats, grade_label=grade_label, grade_short=grade_short, grade_href=grade_href,
                   slug=slug, std_framework=std_framework, year=date.today().year, n_tools=len(tools),
                   n_built=len(built), n_bench=len(bench), BAND_SLUG=BAND_SLUG, FREE_FORMATS=FREE_FORMATS)
# The Reading Room stays out of deploy builds until its pilot stories are ready (Cory, 2026-10-25).
# --library builds it; --preview builds it plus the made-up fixture story.
LIBRARY_LIVE = bool({'--library', '--preview'} & set(sys.argv))
env.globals['library_live'] = LIBRARY_LIVE
# The Supply Closet (docs/SUPPLY-CLOSET-PLAN.md) stays out of deploy builds until Sub Day ships; --closet builds it.
CLOSET_LIVE = bool({'--closet', '--preview'} & set(sys.argv))
env.globals['closet_live'] = CLOSET_LIVE
pages, sitemap = 0, []


def render(template, path, index=True, **ctx):
    global pages
    out = DIST / path.strip('/') / 'index.html' if not path.endswith('.html') else DIST / path.strip('/')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(env.get_template(template).render(path=path, **ctx), encoding='utf-8')
    pages += 1
    if index:
        sitemap.append(path)


if DIST.exists():
    shutil.rmtree(DIST)
ABOUT = 'about-plain'  # temporary (2026-11-07): no family photo or names. To restore: copy drafts/private/about-original/about.html to site/templates/pages/ and cory.webp to site/assets/, then set this to 'about'
shutil.copytree(SITE / 'assets', DIST / 'assets', ignore=None if ABOUT == 'about' else shutil.ignore_patterns('cory.webp'))

# Home shows a small rotating pick, one tool per subject in turn, reshuffled each build (Cory, 2026-11-03).
_rng = __import__('random').Random(date.today().toordinal())
_by_subj = {}
_pool = [t for t in built if t.get('preview')] or built
for _t in _rng.sample(_pool, len(_pool)):
    _by_subj.setdefault(_t['module']['subject'], []).append(_t)
picks = []
while len(picks) < 8 and any(_by_subj.values()):
    for _k in list(_by_subj):
        if _by_subj[_k] and len(picks) < 8:
            picks.append(_by_subj[_k].pop())
render('home.html', '/', built=built, bands=bands, picks=picks)


def browse_page(path, title, lede, trail, sections, nav_label, fit=(), **extra):
    """Grade, band and subject pages: sticky section nav, modules in two columns, ready tools first.
    fit: grades of the page; built tools labelled for any of them join Ready now even when filed under another grade."""
    seen, ready = set(), []
    for s in sections:
        s['ready'] = any(t['built'] for m in s['mods'] for t in m['tools'])
        for m in s['mods']:
            for t in m['tools']:
                if t['built'] and t['tool_id'] not in seen:
                    seen.add(t['tool_id'])
                    ready.append(t)
    ready += [t for t in built if t['tool_id'] not in seen and set(t['fit']) & set(fit)]
    count = sum(len(m['tools']) for s in sections for m in s['mods'])
    render('browse.html', path, title=title, lede=lede.format(count=count, n=len(sections)), trail=trail,
           sections=sections, nav_label=nav_label, ready=ready, count=count, **extra)


def subject_sections(mods):
    return [dict(id=s['subject_id'], label=s['short'], color=s['color'], href=f'/subjects/{s["subject_id"]}/',
                 note=s['primary_standards'], mods=ms) for s, ms in module_groups(mods)]


RESEARCH = json.loads((DATA / 'research-cards.json').read_text(encoding='utf-8'))
_rc_dir = SITE / 'assets' / 'research'
_rc_credits = json.loads((_rc_dir / 'CREDITS.json').read_text(encoding='utf-8')) if (_rc_dir / 'CREDITS.json').exists() else {}
for _c in RESEARCH['cards']:  # a public-domain photo when one is on file, else the emoji
    if (_rc_dir / f"{_c['id']}.jpg").exists() and _c['id'] in _rc_credits:
        _c['photo'] = dict(_rc_credits[_c['id']], src=f"/assets/research/{_c['id']}.jpg")
# Read to me: a recorded voice with word times (scripts/research_voice.py); cards without one use the browser's voice
_rc_voice = json.loads((DATA / 'research-voice.json').read_text(encoding='utf-8')) if (DATA / 'research-voice.json').exists() else {'cards': {}}
for _c in RESEARCH['cards']:
    if _c['id'] in _rc_voice['cards'] and (_rc_dir / 'voice' / f"{_c['id']}.mp3").exists():
        _c['voice'] = {'src': f"/assets/research/voice/{_c['id']}.mp3", 'blocks': _rc_voice['cards'][_c['id']]['blocks']}
# Browse: one page that picks a grade, a subject, or both (replaces the separate Grades and Subjects pages)
mx = {g: {sid: 0 for sid in subjects} for g in GRADES}
for m in modules.values():
    for g in m['grades']:
        mx[g][m['subject']] += len(by_module[m['module_id']])
mxb = {bid: {sid: sum(len(by_module[m['module_id']]) for m in modules.values() if m['subject'] == sid and set(m['grades']) & set(b['grade_list']))
              for sid in subjects} for bid, b in bands.items()}
render('find.html', '/classrooms/', bands=bands, subjects=subjects, mx=mx, mxb=mxb,
       subject_total={sid: sum(mx[g][sid] for g in GRADES) for sid in subjects}, grade_total={g: sum(mx[g].values()) for g in GRADES})
# grades and bands
for g in GRADES:
    lede = ('Teacher-led on the big screen. ' if grades[g]['band'] == 'k2' else '') + '{count} tools across {n} subjects.'
    browse_page(f'/grades/{g}/', grade_label(g), lede, [('Classrooms', '/classrooms/'), (grade_label(g), None)],
                subject_sections([m for m in modules.values() if g in m['grades']]), 'Subjects',
                fit=[g], subtitle='for every subject')
for bid, b in bands.items():
    browse_page(f'/grades/{BAND_SLUG[bid]}/', b['label'], b['blurb'] + ' {count} tools across {n} subjects.',
                [('Classrooms', '/classrooms/'), (b['label'], None)],
                subject_sections([m for m in modules.values() if set(m['grades']) & set(b['grade_list'])]), 'Subjects',
                fit=b['grade_list'], subtitle='for every subject', show_grade=True)

# subjects
for sid, s in subjects.items():
    by_grade = defaultdict(list)
    for m in modules.values():
        if m['subject'] == sid:
            by_grade[m['grade']].append(dict(m, tools=by_module[m['module_id']]))
    order = sorted(by_grade, key=lambda g: (GRADES.index(g.split('-')[0]), -len(expand(g))))
    sections = [dict(id=f'grade-{g}', label=grade_label(g), color=s['color'], href=grade_href(g), note='', mods=by_grade[g])
                for g in order]
    # World languages: one course per language (ASL, Spanish, ...), so the page gets a language picker
    used = {m['course_id'] for ms in by_grade.values() for m in ms}
    langs = [(c, courses[c]['title'].split(' (')[0]) for c in courses if c in used] if sid == 'world-languages' else []
    browse_page(f'/subjects/{sid}/', s['label'], s['covers'] + '. Aligned to ' + s['primary_standards'] + '. {count} tools.',
                [('Classrooms', '/classrooms/'), (s['label'], None)], sections, 'Grades', subtitle='K-12', color=s['color'],
                langs=langs if len(langs) > 1 else [])

# play styles and collections
render('styles.html', '/styles/', counts={f: sum(1 for t in tools if t['format'] == f) for f in formats})
for fid, f in formats.items():
    render('list.html', f'/styles/{fid}/', title=f['label'], lede=f['what_it_feels_like'] + '.',
           items=[t for t in tools if t['format'] == fid], crumb=('Play styles', '/styles/'))
render('collections.html', '/collections/', families=sorted(families.items(), key=lambda kv: -len(kv[1])))
for fam, items in families.items():
    render('list.html', f'/collections/{fam}/', title=fam.replace('-', ' ').title(),
           lede='A family of tools that share one engine and grow with students across grades.',
           items=items, crumb=('Collections', '/collections/'))

# Word Wall cards (docs/SUPPLY-CLOSET-PLAN.md, Phase C); a bad word list stops a closet build.
# Loaded before the standard pages, which link each module to its cards
words = check_words.load() if CLOSET_LIVE else {}
for mid, cards in words.items():
    bad = check_words.problems(mid, cards, modules)
    if bad:
        sys.exit('; '.join(bad) + ' (python scripts/check_words.py)')

# standards
by_fw = defaultdict(list)
for code in sorted(standards):
    by_fw[std_framework[code]].append(code)
render('standards.html', '/standards/', by_fw=sorted(by_fw.items()))
code_modules = defaultdict(list)
for m in modules.values():
    for code in m['codes']:
        code_modules[code].append(m)
for code, items in standards.items():
    seen, uniq = set(), []
    for t in items:
        if t['tool_id'] not in seen:
            seen.add(t['tool_id'])
            uniq.append(t)
    render('standard.html', f'/standards/{slug(code)}/', code=code, framework=std_framework[code], items=uniq,
           mods=sorted(code_modules[code], key=lambda m: GRADES.index(m['grades'][0])), walls=words, index=False,
           map_spots=map_spots(code_modules[code]))

# Family Game Night (Phase E): each game links to its modules, and to their built tools as "Loved it at school?"
games = check_games.load() if CLOSET_LIVE else {}
games_by_module = defaultdict(list)
for g in games.values():
    bad = check_games.problems(g, modules)
    if bad:
        sys.exit('; '.join(bad) + ' (python scripts/check_games.py)')
    g['mods'] = [modules[mid] for mid in g['module_ids']]
    g['tools'] = [t for mid in g['module_ids'] for t in by_module[mid] if t['built']]
    for mid in g['module_ids']:
        games_by_module[mid].append(g)
# Break Box (docs/BREAK-BOX-PLAN.md): projects for a school break, one printed sheet each; a bad sheet stops a closet build
breaks = check_breaks.load() if CLOSET_LIVE else {}
_bad = [p for b in breaks.values() for p in check_breaks.problems(b)] + check_breaks.grade_problems(breaks)
if _bad:
    sys.exit('; '.join(_bad[:5]) + ' (python scripts/check_breaks.py)')
for b in breaks.values():
    b['html'] = {name: markdown.markdown(text) for name, text in b['parts']}

# Posters and Anchor Charts (Phase D): a chart per module, and posters by band; a bad or overfull chart stops the build
charts = check_charts.load('chart') if CLOSET_LIVE else {}
posters = check_charts.load('poster') if CLOSET_LIVE else {}
for c in list(charts.values()) + list(posters.values()):
    bad = check_charts.problems(c, modules)
    if bad:
        sys.exit('; '.join(bad) + ' (python scripts/check_charts.py)')


def chart_page(c, color, **ctx):
    """/modules/<id>/chart/ or a poster page: a symbol per version, language and ink, and chart.svg for the shelf."""
    symbols, versions = [], []
    for v in ['done', 'fill'] if c['layout'] != 'grid' else ['done']:
        for lang in ['en', 'es']:
            for ink in ['color', 'ink']:
                sid = f'c-{v}-{lang}-{ink}'
                sym, fits = chart_svg.symbol(c, sid, lang, v == 'fill', color, ink == 'ink')
                if not fits:
                    sys.exit(f"{c['file']}: too long to fit on one page ({lang}); cut words (python scripts/charts.py {c['id']})")
                symbols.append(sym)
                versions.append(dict(id=sid, key=f'{v}-{lang}-{ink}', label=f"{c['title'][0 if lang == 'en' else 1]}, "
                                     f"{'fill-in' if v == 'fill' else 'finished'}, {'English' if lang == 'en' else 'Spanish'}"
                                     f"{', ink saver' if ink == 'ink' else ''}"))
    w, h = chart_svg.dims(c)
    render('closet/chart.html', c['url'], c=c, symbols=symbols, versions=versions, w=w, h=h,
           tilings=[(n, chart_svg.tiles(n, c)) for n in (2, 3)], **ctx)
    (DIST / c['url'].strip('/') / 'chart.svg').write_text(chart_svg.svg(c, 'en', False, color), encoding='utf-8')


def word_gap(word, text):
    """(before, after) around the word in its example sentence, for the Word check fill-in; None if it is not there.
    Spanish words change form (varía for variar), so a long one-word entry also matches its stem."""
    hit = re.search(r'(?i)\b' + re.escape(word) + r'\w*', text)
    if not hit and ' ' not in word and len(word) >= 5:
        hit = re.search(r'(?i)\b' + re.escape(word[:-2]) + r'\w*', text)
    return (text[:hit.start()], text[hit.end():]) if hit else None


def word_check(seed, cards):
    """Letters for the Word check matching: the meanings in a fixed shuffle (never the card order), letter A first."""
    order = list(range(len(cards)))
    random.Random(seed).shuffle(order)
    if order == sorted(order):
        order = order[1:] + order[:1]
    for pos, i in enumerate(order):
        cards[i]['letter'] = 'ABCDEFGHIJ'[pos]
    fill = list(range(len(cards)))  # the fill-in sentences in their own shuffle, so the answers do not run in word order
    random.Random(seed + '/fill').shuffle(fill)
    if fill == sorted(fill):
        fill.reverse()
    for pos, i in enumerate(fill):
        cards[i]['fill_rank'] = pos


# Worksheets (docs/WORKSHEETS-PLAN.md): a page per class listing its year of sheets from the concept lists, one data file
# per class holding its built sheets as HTML fragments, and one viewer page that shows a sheet (#unit/n) and its key.
ws_units = check_worksheets.units()
ws_rows = {u: r for f in check_worksheets.FILES for u, r in check_worksheets.rows(f).items()}
ws_bad = ws.icon_problems() + [p for u in ws.built_units() for p in ws.problems(u)]
(DIST / 'assets' / 'ws-icons.svg').write_text(ws.sprite(), encoding='utf-8')
if ws_bad:
    sys.exit('Worksheets: ' + '; '.join(ws_bad[:5]))
tool_titles = {t['tool_id']: t['title'] for t in tools}
mod_by_title = {(m['course_id'], m['title']): m for m in modules.values()}
ws_built, ws_index = {}, []
for u in ws.built_units():
    label, sheets = ws.load(u)
    data = {}
    for sh, row in sheets:
        mod = mod_by_title.get((ws_units[u]['course'], row['module']))
        frag, _ = ws.build(u, sh, row, label, mod, tool_titles)
        data[sh['n']] = dict(title=sh['title'], type=row['type'], minutes=sh['minutes'], html=frag)
        ws_index.append(dict(t=f"Worksheet: {sh['title']}", u=f'/closet/worksheets/sheet/#{u}/{sh["n"]}', g=label, s='Supply Closet',
                             f='Worksheet', m=row['module'], c=' '.join(mod['codes']) if mod else '', d=row['does'], b=True))
    ws_built[u] = data
    out = DIST / 'closet' / 'worksheets' / 'data' / f'{u}.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(dict(unit=u, label=label, url=f'/closet/worksheets/{u}/', order=[r['n'] for r in ws_rows[u]],
                                  sheets=data), ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
# rows a generator makes (data/closet/worksheets/generated.csv): ready on the class page, link opens the generator preset
ws_gen = ws_generated.load()
ws_gen_bad = ws_generated.problems(ws_rows, ws_built)
if ws_gen_bad:
    sys.exit('Worksheets: ' + '; '.join(ws_gen_bad[:5]))

# worksheets of a module: the concept rows naming it, in the units of its course, with a link when the sheet is built
ws_by_module = defaultdict(list)
for u, rows_ in ws_rows.items():
    cid = ws_units[u]['course']
    for row in rows_:
        mod = mod_by_title.get((cid, row['module']))
        if mod:
            g = ws_gen.get(u, {}).get(row['n'])
            ws_by_module[mod['module_id']].append(dict(row, unit=u, label=ws_units[u]['label'], built=row['n'] in ws_built.get(u, {}) or bool(g), gen=g,
                                                       url=f'/closet/worksheets/sheet/#{u}/{row["n"]}' if row['n'] in ws_built.get(u, {}) else g['url'] if g else f'/closet/worksheets/{u}/'))

# modules: the hub for everything one module has (tools, then Supply Closet shelves as they ship)
for m in modules.values():
    mt = by_module[m['module_id']]
    plans = [t for t in mt if t['built'] and t['plan']]
    cards = words.get(m['module_id'], [])
    rcards = [c for c in RESEARCH['cards'] if m['module_id'] in c['modules']] or (RESEARCH['cards'] if m['module_id'] in RESEARCH['for_all'] else [])
    render('module.html', m['url'], m=m, items=mt, plans=plans, words=cards, subject=subjects[m['subject']], rcards=rcards, rc_all=m['module_id'] in RESEARCH['for_all'],
           games=games_by_module.get(m['module_id'], []), course=courses.get(m['course_id']), chart=charts.get(m['module_id']),
           sheets=ws_by_module.get(m['module_id'], []) if CLOSET_LIVE else [], gens=gen_links.links(m, bool(cards)) if CLOSET_LIVE else [],
           index=any(t['built'] for t in mt) or bool(cards))
    if m['module_id'] in charts:
        chart_page(charts[m['module_id']], CSS_HEX[subjects[m['subject']]['color']], m=m, subject=subjects[m['subject']],
                   tools=[t for t in mt if t['built']])
    if cards:
        dest = DIST / 'modules' / m['module_id'] / 'words'
        for c in cards:
            c['src'] = ''
            if c['art'].exists():
                (dest / 'art').mkdir(parents=True, exist_ok=True)
                shutil.copy2(c['art'], dest / 'art' / c['art'].name)
                c['src'] = 'art/' + c['art'].name
            c['gap_en'], c['gap_es'] = word_gap(c['word'], c['example']), word_gap(c['es_word'], c['es_example'])
        word_check(m['module_id'], cards)
        dest.mkdir(parents=True, exist_ok=True)
        with open(dest / f"{m['module_id']}-words.csv", 'w', encoding='utf-8-sig', newline='') as f:  # BOM so Excel reads the Spanish
            out = csv.writer(f)
            out.writerow(['word', 'definition', 'example', 'palabra', 'definición', 'ejemplo'])
            out.writerows([c['word'], c['definition'], c['example'], c['es_word'], c['es_definition'], c['es_example']] for c in cards)
        render('closet/words.html', m['url'] + 'words/', m=m, cards=cards, subject=subjects[m['subject']],
               band=check_words.band(m['grade']), tools=[t for t in mt if t['built']])

# tools
render('list.html', '/tools/', title='Ready to use', lede='Every built tool. Each one is a single file that works offline.',
       items=built, crumb=None)
# The /bench/ list page was retired 2026-11-03 (Cory): sketched tools still show on their module pages.
for t in tools:
    related = [x for x in tools if x['module']['subject'] == t['module']['subject'] and x is not t
               and set(x['module']['grades']) & set(t['module']['grades'])][:3]
    collection = families.get(t['family'])
    if t['built']:
        dest = DIST / 'tools' / t['tool_id']
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(TOOLS / t['tool_id'] / t['file'], dest / t['file'])
        if t['preview']:
            shutil.copy2(TOOLS / t['tool_id'] / 'preview.svg', dest / 'preview.svg')
        render('tool.html', t['url'], t=t, related=related, collection=collection,
               home=games_by_module.get(t['module']['module_id'], []), cards=words.get(t['module']['module_id'], []))
        if t['plan']:
            plan = t['plan']
            render('plan.html', t['url'] + 'plan/', t=t, meta=plan['meta'], arc=check_plans.ARCS[plan['meta']['arc']],
                   cards=words.get(t['module']['module_id'], []),
                   sections=[(title, mins, markdown.markdown(text)) for title, mins, text in plan['sections']])
            if t['exit'] and CLOSET_LIVE:  # Sub Day packet (Phase B): cover, plan, notes, exit tickets, backup sheet
                render('subday.html', t['url'] + 'sub/', index=False, t=t, ex=t['exit'],
                       qr=qr.svg('https://curioclass.org' + t['url'], f'QR code for curioclass.org{t["url"]}'),
                       sections=[(title, mins, markdown.markdown(text)) for title, mins, text in plan['sections']],
                       band=check_words.band(t['module']['grade']), words=words.get(t['module']['module_id'], []),
                       gens=gen_links.links(t['module'], bool(words.get(t['module']['module_id']))))
    else:
        render('bench.html', t['url'], t=t, related=related, collection=collection, index=False)

# ---------- supply closet ----------
# Shelves fill in phase by phase (docs/SUPPLY-CLOSET-PLAN.md). Until a shelf has items its page says what is coming.
CLOSET = [  # slug, label, what it holds
    ('sub-day', 'Sub Day', 'A print-ready packet for a substitute: cover page, lesson plan, teacher notes, exit tickets '
     'and a backup sheet for when the tech fails.'),
    ('word-wall', 'Word Wall', 'Vocabulary cards for every module, with pictures for the younger grades, plus a student glossary.'),
    ('anchor-charts', 'Posters and Anchor Charts', 'The big idea of each module on one page, finished or fill-in, and posters '
     'that stay up all year. Print on one page or tile them big.'),
    ('game-night', 'Family Game Night', 'Games to play at home with paper, pencils, cards or dice. Nothing to buy.'),
    ('break-box', 'Break Box', 'Projects for a school break, K to 12: build, make, cook, play or explore for an hour or two. '
     'One printed sheet each, written for the child, with a note for the grown-up.'),
    ('worksheets', 'Worksheets', 'Printable practice sheets for every class, K-12: 40 to 50 a year per class, each with '
     'an answer key and a teacher page.'),
    ('printables', 'Printables', 'Everyday paper for the classroom: handwriting and graph paper, graphic organizers, '
     'number lines, hundreds charts, name plates and certificates.'),
    ('research-cards', 'Research Cards', 'A first taste of research for grades K to 2: a person, place, thing or animal '
     'on two printed pages, a short read with facts on the first and a page for the young researcher on the second.'),
    ('teacher-desk', 'Teacher Desk', 'Helpers for running the room, made for the projector: a timer, classroom sounds, a '
     'noise meter and a group maker.'),
]
# Printables shelf: each item is one page drawn by site/assets/printables.js (data-kind = id). Add a kind there first.
PRINTABLES = [  # heading, blurb, [(id, title, blurb)]
    ('Paper', 'Plain paper with the lines your class needs.', [
        ('handwriting', 'Handwriting Paper', 'Solid top and bottom lines with a dashed middle line, in three sizes for K to grade 2. Add a picture box for draw-and-write.'),
        ('lined', 'Lined Paper', 'Extra wide, wide or college ruled, with a margin line and a name and date line.'),
        ('graph', 'Graph Paper', 'Quarter inch, half inch, centimeter or 5 millimeter squares, with darker lines every five if you want them.'),
        ('dots', 'Dot Paper', 'Square or isometric dot grids for geometry, area, arrays and drawing 3D shapes.'),
    ]),
    ('Math and letters', 'Charts and strips for counting, number sense and the alphabet.', [
        ('numberline', 'Number Lines', 'Pick the start, end and count-by. Show every number, only the ends, or none for students to fill in.'),
        ('hundreds', 'Hundreds Chart', '1 to 100, 0 to 99 or 1 to 120. Full, partly filled, or blank.'),
        ('alphabet', 'Alphabet Strips and Cards', 'Desk strips, three to a page, or a full page of letter cards. Uppercase, lowercase or both.'),
    ]),
    ('Graphic organizers', 'Thinking on paper, for any subject. English, Spanish or both.', [
        ('venn', 'Venn Diagram', 'Two or three circles for comparing. Type the labels or leave them blank.'),
        ('kwl', 'KWL Chart', 'What I know, what I want to know and what I learned, with an optional "how I will find out" column.'),
        ('storymap', 'Story Map', 'Title, characters, setting, problem, beginning, middle, end and solution.'),
        ('causeeffect', 'Cause and Effect', 'One cause with three effects, or a chain of four.'),
        ('mainidea', 'Main Idea and Details', 'A main idea on top with three or four details below.'),
        ('tchart', 'T-Chart', 'Two columns with your own headings: facts and opinions, before and after, pros and cons.'),
        ('sequence', 'Sequence Chart', 'First, next, then, last, or six numbered steps, with room to draw.'),
        ('frayer', 'Word Map (Frayer Model)', 'A word in the middle with definition, characteristics, examples and non-examples.'),
    ]),
    ('Classroom', 'For the first day and the good days.', [
        ('nameplate', 'Name Plates', 'Type your class list for desk plates with the alphabet and a 0 to 20 number line, or folded tent cards.'),
        ('certificate', 'Certificates', 'An award with your own heading, name, reason and signature line. Print in color or black.'),
    ]),
]
DESK_COMING = [  # planned Teacher Desk pieces (docs/ROADMAP.md, Track 2 item 7)
    ('Quiz Show Board', 'A projector game board for review games: teams, points and a big reveal for each question.'),
]
# Word Wall: one page per grade span a module is written for (K to 12, and spans like 3-5 or K-12), grouped by subject.
# The shelf page is a grade picker: a card per band with its grades and its whole-band span, then a card for World Languages.
wall = defaultdict(list)
for mid in words:
    wall[modules[mid]['grade']].append(modules[mid])


def mods_tally(mods):
    return f'{len(mods)} modules, {sum(len(words[m["module_id"]]) for m in mods)} words'


# A module written across bands (like ELD for 6-12) also sits on the whole-band page of every band it reaches, so a
# teacher finds it under their grade. World languages run by level, not grade: they get one page per language instead.
fold = defaultdict(list)
for g, mods in wall.items():
    if g in GRADES or g in BAND_SLUG.values():
        continue
    for m in mods:
        if m['subject'] != 'world-languages':
            for bid, b in bands.items():
                if set(m['grades']) & set(b['grade_list']):
                    fold[BAND_SLUG[bid]].append(dict(m, wall_note=grade_label(m['grade'])))
wall_langs = defaultdict(list)  # course_id -> modules, like the language picker on /subjects/world-languages/
for mods in wall.values():
    for m in mods:
        if m['subject'] == 'world-languages':
            wall_langs[m['course_id']].append(m)
LANG_CHIP = {'asl': 'ASL'}  # chip text when the language's full name is too long for a chip
wall_bands, reached = [], set()
for bid, b in bands.items():
    spans = [g for g in b['grade_list'] + [BAND_SLUG[bid]] if g in wall or g in fold]
    mods = [m for g in spans for m in wall.get(g, []) + fold.get(g, [])]
    reached |= {m['module_id'] for m in mods}
    wall_bands.append(dict(label=b['label'], tally=mods_tally({m['module_id']: m for m in mods}.values()),
                           chips=[dict(href=f'/closet/word-wall/{g}/', text=('All ' if '-' in g else '') + g.upper(),
                                       aria=grade_label(g), span='-' in g) for g in spans]))
lang_list = [(c, courses[c]['title'].split(' (')[0]) for c in courses if c in wall_langs]
if lang_list:
    mods = [m for c, _ in lang_list for m in wall_langs[c]]
    reached |= {m['module_id'] for m in mods}
    wall_bands.append(dict(label='World Languages', tally=mods_tally(mods),
                           chips=[dict(href=f'/closet/word-wall/{c}/', text=LANG_CHIP.get(c, name), aria=name, span=True)
                                  for c, name in lang_list]))
lost = [mid for mid in words if mid not in reached]
if lost:
    sys.exit(f'Word Wall index misses {len(lost)} modules, like {lost[0]}')
for g, mods in wall.items():
    mods = mods + fold.get(g, [])
    by_sub = defaultdict(list)
    for m in mods:
        by_sub[m['subject']].append(m)
    sections = [dict(id=sid, label=s['label'], color=s['color'], mods=sorted(by_sub[sid], key=lambda m: m['title']))
                for sid, s in subjects.items() if sid in by_sub]
    also = [x for x in wall if x != g and set(expand(x)) & set(expand(g)) and (len(expand(x)) > len(expand(g)))]
    render('closet/word-grade.html', f'/closet/word-wall/{g}/', g=g, title=grade_label(g), sections=sections, words=words,
           tally=mods_tally(mods), also=sorted(also, key=lambda x: len(expand(x))))
for c, name in lang_list:  # a page per language, its modules by grade span
    by_span = defaultdict(list)
    for m in wall_langs[c]:
        by_span[m['grade']].append(m)
    sections = [dict(id=f'grade-{g}', label=grade_label(g), color=subjects['world-languages']['color'],
                     mods=sorted(by_span[g], key=lambda m: m['title']))
                for g in sorted(by_span, key=lambda g: (GRADES.index(g.split('-')[0]), -len(expand(g))))]
    render('closet/word-grade.html', f'/closet/word-wall/{c}/', g=c, title=name, sections=sections, words=words,
           tally=mods_tally(wall_langs[c]), also=[], nav_label='Grades')
sub_tools = [t for t in built if t['exit']] if CLOSET_LIVE else []
sub_sections = []
for gr in GRADES:  # a tool sits under the first grade it is written for
    ts = sorted((t for t in sub_tools if t['module']['grades'][0] == gr), key=lambda t: (list(subjects).index(t['module']['subject']), t['title']))
    if ts:
        sub_sections.append(dict(id=f'grade-{gr}', label=grade_label(gr), tools=ts))
for c in posters.values():
    chart_page(c, CSS_HEX[c.get('color', 'teal')], band_label=bands[c['band']]['label'])
chart_sections = [dict(id=f'posters-{bid}', label=f"Posters: {b['label']}", items=sorted((c for c in posters.values() if c['band'] == bid), key=lambda c: c['title'][0]))
                  for bid, b in bands.items()]
for gr in GRADES:  # a chart sits under the first grade its module is written for
    cs = sorted((c for c in charts.values() if modules[c['id']]['grades'][0] == gr),
                key=lambda c: (list(subjects).index(modules[c['id']]['subject']), c['title'][0]))
    chart_sections.append(dict(id=f'grade-{gr}', label=grade_label(gr), items=cs))
chart_sections = [s for s in chart_sections if s['items']]
counts = {'anchor-charts': f'{len(charts)} charts, {len(posters)} posters' if charts else '', 'sub-day': f'{len(sub_tools)} packets' if sub_tools else '', 'word-wall': mods_tally([m for ms in wall.values() for m in ms]) if words else '', 'game-night': f'{len(games)} games' if games else ''}
# Game Night: one shelf page with a section per grade (games in subject order), and a print page per game
SUBJECT_ES = {'math': 'Matemáticas', 'ela': 'Lectura y escritura', 'science': 'Ciencias', 'social-studies': 'Estudios sociales'}
game_sections = []
for gr in GRADES:
    gs = sorted((g for g in games.values() if g['grade'] == gr), key=lambda g: (list(subjects).index(g['subject']), g['title']))
    if gs:
        game_sections.append(dict(id=f'grade-{gr}', label=grade_label(gr), games=gs))
# Break Box: one shelf page with a section per grade (sheets in plan order), a print page per sheet and a blank one
break_sections = [dict(id=f'grade-{gr}', g=gr, label=grade_label(gr),
                       sheets=sorted((b for b in breaks.values() if b['grade'] == gr), key=lambda b: int(b['order'])))
                  for gr in GRADES]
break_sections = [s for s in break_sections if s['sheets']]
if breaks:
    counts['break-box'] = f'{len(breaks)} projects and a blank one'
for g in games.values():
    render('closet/game.html', g['url'], g=g, subject=subjects[g['subject']], subject_es=SUBJECT_ES[g['subject']],
           tools=[t for mid in g['module_ids'] for t in by_module[mid] if t['built']])
def ws_grade_key(u):
    g = str(ws_units[u]['grade']).split('-')[0]
    return GRADES.index(g) if g in GRADES else 99


ws_sections = []
for gr in GRADES:  # a class sits under its grade; a high school course under its usual grade
    us = [u for u, d in ws_units.items() if 'level' not in d and ws_grade_key(u) == GRADES.index(gr)]
    if us:
        ws_sections.append(dict(id=f'grade-{gr}', label=grade_label(gr), units=us))
ws_sections.append(dict(id='languages', label='World Languages', units=[u for u, d in ws_units.items() if 'level' in d]))
for u, d in ws_units.items():
    groups = []
    for r in ws_rows[u]:
        if not groups or groups[-1]['module'] != r['module']:
            groups.append(dict(module=r['module'], mod=mod_by_title.get((d['course'], r['module'])), rows=[]))
        groups[-1]['rows'].append(dict(r, pos=sum(len(g['rows']) for g in groups) + 1, built=r['n'] in ws_built.get(u, {}), gen=ws_gen.get(u, {}).get(r['n'])))
    render('closet/ws-unit.html', f'/closet/worksheets/{u}/', u=u, d=d, groups=groups, rows=ws_rows[u], ready=len(ws_built.get(u, {})) + len(ws_gen.get(u, {})))
render('closet/ws-sheet.html', '/closet/worksheets/sheet/', index=False)
# Worksheet Generators (data/closet/generators.json): one page each, drawn by site/assets/gen/<id>.js, plus the word
# list the vocabulary and puzzle generators read (every Word Wall module with its words and meanings).
gidx = lambda g: next((GRADES.index(x) for x in expand(g) if x in GRADES), 99)
GENS = json.loads((ROOT / 'data' / 'closet' / 'generators.json').read_text(encoding='utf-8'))
if CLOSET_LIVE:
    render('closet/gens.html', '/closet/worksheets/make/', groups=GENS['groups'], gens=GENS['generators'])
    for g in GENS['generators']:
        if not (SITE / 'assets' / 'gen' / f"{g['id']}.js").exists():
            sys.exit(f"Generators: site/assets/gen/{g['id']}.js is missing")
        g['data_js'] = (SITE / 'assets' / 'gen' / f"{g['id']}-data.js").exists()   # an optional word or fact bank, loaded first
        render('closet/gen.html', f"/closet/worksheets/make/{g['id']}/", g=g,
               more=[m for m in GENS['generators'] if m['group'] == g['group'] and m['id'] != g['id']])
    gen_words = [dict(id=mid, title=modules[mid]['title'], subject=modules[mid]['subject'], s=subjects[modules[mid]['subject']]['label'],
                      grade=modules[mid]['grade'], band=check_words.band(modules[mid]['grade']),
                      words=[[c['word'], c['definition']] for c in cards if c['word'] and c['definition']])
                 for mid, cards in words.items() if mid in modules]
    gen_words.sort(key=lambda m: (m['s'], gidx(m['grade']), m['title']))
    (DIST / 'closet' / 'worksheets' / 'make' / 'words.json').write_text(json.dumps(dict(modules=gen_words), ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
counts['teacher-desk'] = 'Desk Dock and Classroom Music ready'
counts['research-cards'] = f"{len(RESEARCH['cards'])} cards and a blank one"
counts['printables'] = f"{sum(len(x[2]) for x in PRINTABLES)} printables"
counts['worksheets'] = f"{sum(len(v) for v in ws_built.values()) + sum(len(v) for v in ws_gen.values())} ready of {sum(len(v) for v in ws_rows.values()):,} planned"
render('closet/home.html', '/closet/', shelves=CLOSET, counts=counts)
for sid, label, what in CLOSET:
    if sid == 'word-wall' and wall:
        render('closet/word-wall.html', '/closet/word-wall/', label=label, what=what, wall_bands=wall_bands)
    elif sid == 'sub-day' and sub_tools:
        render('closet/sub-day.html', '/closet/sub-day/', label=label, what=what, sections=sub_sections)
    elif sid == 'anchor-charts' and charts:
        render('closet/anchor-charts.html', '/closet/anchor-charts/', label=label, what=what, sections=chart_sections, modules=modules)
    elif sid == 'worksheets':
        render('closet/worksheets.html', '/closet/worksheets/', label=label, what=what, sections=ws_sections, units=ws_units,
               rows=ws_rows, built={u: {**ws_built.get(u, {}), **ws_gen.get(u, {})} for u in ws_units})
    elif sid == 'printables':
        render('closet/printables.html', '/closet/printables/', label=label, what=what,
               groups=[(h, bl, [dict(id=i, title=ti, blurb=b) for i, ti, b in items]) for h, bl, items in PRINTABLES])
        for h, bl, items in PRINTABLES:
            for i, ti, b in items:
                render('closet/printable.html', f'/closet/printables/{i}/', p=dict(id=i, title=ti, blurb=b))
    elif sid == 'research-cards':
        kinds = dict(RESEARCH['kinds'])
        render('closet/research-cards.html', '/closet/research-cards/', label=label, what=what,
               groups=[(name, sorted((c for c in RESEARCH['cards'] if c['kind'] == k), key=lambda c: c['title'].removeprefix('The ').lower()))
                       for k, name in sorted(RESEARCH['kinds'], key=lambda kn: kn[1])])  # A to Z, ignoring a leading 'The'
        for c in RESEARCH['cards'] + [dict(id='my-own', kind='', title='', emoji='', read=[], facts=[], words=[], questions=[])]:
            render('closet/research-card.html', f"/closet/research-cards/{c['id']}/", c=c, kind=kinds.get(c['kind'], ''))
    elif sid == 'teacher-desk':
        render('closet/teacher-desk.html', '/closet/teacher-desk/', label=label, what=what, coming=DESK_COMING)
        render('closet/desk-dock.html', '/closet/teacher-desk/dock/')
        render('closet/music.html', '/closet/teacher-desk/music/')
    elif sid == 'game-night' and games:
        render('closet/game-night.html', '/closet/game-night/', label=label, what=what, sections=game_sections)
    elif sid == 'break-box' and breaks:
        render('closet/break-box.html', '/closet/break-box/', label=label, what=what, sections=break_sections)
        for b in breaks.values():
            render('closet/break.html', b['url'], b=b)
        render('closet/break.html', '/closet/break-box/my-own-idea/', b=dict(id='my-own-idea', url='/closet/break-box/my-own-idea/'))
    else:
        render('closet/shelf.html', f'/closet/{sid}/', label=label, what=what, groups=[], index=False)

# ---------- the map ----------
# Drawn here, once the closet shelves are loaded, so each stop's pins show what a teacher can pick up for it.
map_rows = []
for sid, subj in subjects.items():
    keys = [k for k in map_regions if k[0] == sid]
    lanes, regs = [], []
    for k in sorted(keys, key=lambda k: (GRADES.index(expand(k[1])[0]), -len(expand(k[1])))):
        x0, x1 = GRADES.index(expand(k[1])[0]), GRADES.index(expand(k[1])[-1])
        lane = next((i for i, end in enumerate(lanes) if end < x0), len(lanes))
        lanes[lane:lane + 1] = [x1]
        stops = map_regions[k]
        regs.append(dict(x0=x0, x1=x1, lane=lane, url=map_url(k), title=map_title(k), short=grade_label(k[1]),
                         ready=sum(s['ready'] for s in stops), total=len(stops)))
    if regs:
        map_rows.append((sid, subj['short'], regs))
for k, stops in map_regions.items():
    for s in stops:
        mid = s['m']['module_id']
        s['tools'] = [t for t in by_module[mid] if t['built']]
        s['planned'] = len(by_module[mid]) - len(s['tools'])
        sub = [t for t in s['tools'] if t.get('exit')] if CLOSET_LIVE else []
        s['closet'] = (([('Word Wall', s['m']['url'] + 'words/')] if words.get(mid) else [])
                       + ([('Anchor chart', charts[mid]['url'])] if mid in charts else [])
                       + [(f"Game: {g['title']}", g['url']) for g in games_by_module.get(mid, [])]
                       + [(f"Sub Day: {t['title']}", t['url'] + 'sub/') for t in sub])
        s['pins'] = [p for p, on in (('tool', s['tools']), ('words', words.get(mid)), ('chart', mid in charts),
                                     ('game', games_by_module.get(mid)), ('sub', sub)) if on]
        s['links'] = [dict(m=b, region=map_title(map_at[b['module_id']])) for b in s['builds_on']]
render('map.html', '/map/', rows=map_rows, basis=tmap.BASIS,
       grid=tmap.overview(map_rows, [grade_short(g) for g in GRADES], lambda sid: CSS_HEX[subjects[sid]['color']],
                          'Every subject and grade, shaded by how many stops have a tool ready'),
       n_regions=len(map_regions), n_stops=sum(len(v) for v in map_regions.values()),
       n_ready=sum(s['ready'] for v in map_regions.values() for s in v))
for sid, _, regs in map_rows:
    keys = [k for k in map_regions if k[0] == sid]
    keys.sort(key=lambda k: (GRADES.index(expand(k[1])[0]), -len(expand(k[1]))))
    for i, k in enumerate(keys):
        stops, color = map_regions[k], CSS_HEX[subjects[sid]['color']]
        label = f'{map_title(k)}: {len(stops)} stops in teaching order'
        render('map-region.html', map_url(k), title=map_title(k), subject=subjects[sid], g=k[1], stops=stops,
               wide=tmap.trail(stops, color, label), phone=tmap.trail(stops, color, label, phone=True),
               ready=sum(s['ready'] for s in stops), color=color,
               bases=[(b, tmap.BASIS[b]) for b in tmap.BASIS if any(s['basis'] == b for s in stops)],
               prev=(map_title(keys[i - 1]), map_url(keys[i - 1])) if i else None,
               next=(map_title(keys[i + 1]), map_url(keys[i + 1])) if i + 1 < len(keys) else None)

# ---------- reading room ----------
# Rows come from data/library/*.csv (reserve rows stay off the site). A story is ready once library/<id>/text.md exists;
# until then its page says it is on the reading desk. docs/LIBRARY-PLAN.md has the story.json and text.md format.
LIB = ROOT / 'library'
SHELVES = {  # shelf slug -> (label, blurb, kinds)
    'picture-books': ('Picture books', 'Short, illustrated, made for reading together.', ['picture book']),
    'short-stories': ('Short stories', 'One sitting, one story.', ['short story']),
    'poems': ('Poems', 'Read them out loud. Then read them again.', ['poem']),
    'tales': ('Myths, fables and folk tales', 'Stories people told long before anyone wrote them down.',
              ['folk tale', 'fairy tale', 'fable', 'myth', 'legend', 'epic']),
    'chapter-books': ('Chapter books and novels', 'Longer reads, chapter by chapter.', ['chapter book', 'chapter set', 'novel']),
    'plays': ('Plays', 'Parts for the whole class.', ['play']),
    'true-stories': ('True stories', 'Memoir, essays and real lives.', ['memoir', 'nonfiction', 'essay']),
}
KIND_SHELF = {k: sid for sid, (_, _, kinds) in SHELVES.items() for k in kinds}
BASIS = {'pd-1930': 'Public domain in the United States (first published {year}).',
         'not-renewed': 'Public domain in the United States (published {year}, copyright not renewed).',
         'us-gov': 'A work of the U.S. government, in the public domain.'}
GLOSS = re.compile(r'\{([^{}|\n]+)\|([^{}\n]+)\}')
lib_sources = {s['key']: s for s in read('library/sources.csv')}


def lib_story(r, collection):
    g = r['grades'].lower()
    s = dict(r, collection=collection, grades=g, fit=expand(g), url=f'/library/{r["id"]}/', shelf=KIND_SHELF.get(r['kind']),
             band=next(b for b in bands if expand(g)[0] in bands[b]['grade_list']), ready=False, meta={})
    if 'sw_id' in r:  # StoryWeaver: names and blurb come from the saved export
        sw = LIB / '_sources' / 'storyweaver' / f'{r["sw_id"]}.json'
        book = json.loads(sw.read_text(encoding='utf-8')) if sw.exists() else {}
        s.update(author=book.get('authors') or r['publisher'], summary=' '.join(book.get('description', '').split()),
                 credit=f'{r["license"]}. Published by {r["publisher"]} on StoryWeaver.', source_url=book.get('url', ''))
    else:
        src = lib_sources[r['source']]
        s['credit'] = BASIS.get(src['basis'], src['license'] + '.').format(year=src['year'])
        s['source_url'] = f'https://www.gutenberg.org/ebooks/{src["pg"].split()[0]}' if src['pg'] else ''
    folder = Path(r['folder']) if r.get('folder') else LIB / r['id']
    if (folder / 'text.md').exists():
        text = (folder / 'text.md').read_text(encoding='utf-8')
        meta = json.loads((folder / 'story.json').read_text(encoding='utf-8')) if (folder / 'story.json').exists() else {}
        html = GLOSS.sub(lambda m: f'<button type="button" class="gloss" data-gloss="{m[2].replace(chr(34), "&quot;")}">{m[1]}</button>',
                         markdown.markdown(text))
        heads = re.findall(r'<h2>(.*?)</h2>', html)
        toc = [(f'part-{i}', re.sub(r'<[^>]+>', '', h)) for i, h in enumerate(heads, 1)] if len(heads) >= 3 else []
        if toc:  # long works get a contents list; each part heading gets an anchor
            n = iter(range(1, len(heads) + 1))
            html = re.sub(r'<h2>', lambda m: f'<h2 id="part-{next(n)}">', html)
        words = meta.get('words') or len(GLOSS.sub(r'\1', text).split())
        note = re.sub(r',? ?teacher note( required)?', '', r.get('note', '')).replace('check for', 'may have')
        warn = [p for p in re.split(r';\s*', note)  # the curator's shorthand, minus its working notes
                if p and not re.match(r'(chapter )?set\b|picked in|whole|complete|newbery|cc by|outside review|discuss', p, re.I)]
        if r['decision'] == 'note' and warn and not meta.get('teacher_note'):  # the curation pass's content flags
            meta = dict(meta, teacher_note=f'<p><strong>Content note:</strong> {html_escape("; ".join(warn))}. '
                                           'Read it first and decide how to set it up for your class.</p>')
        first = next((p for p in text.split('\n\n') if p.strip() and not re.match(r'\s*(#|!\[|---|<)', p)), '')
        first = re.sub(r'[*_\\]', '', GLOSS.sub(r'\1', first)).split()  # the opening words, for search
        s.update(first=' '.join(first[:14]) + (' ...' if len(first) > 14 else ''))
        s.update(ready=True, meta=meta, html=html, toc=toc, words=words, minutes=max(1, round(words / 200)),
                 summary=meta.get('summary', s.get('summary', '')), art=(folder / 'art').is_dir())
    return s


stories = [lib_story(r, 'stories') for r in read('library/stories-pd.csv') + read('library/stories-sw.csv')
           if r['decision'] != 'reserve']
speeches = [lib_story(r, 'speeches') for r in read('library/speeches.csv') if r['decision'] != 'reserve']
sacred = sorted((lib_story(r, 'sacred') for r in read('library/sacred-texts.csv') if r['decision'] != 'reserve'),
                key=lambda s: re.sub(r'^the ', '', s['title'].lower()))  # alphabetical, ignoring a leading "The"
if '--preview' in sys.argv:  # local check of the reader with a made-up story; never part of a deploy build
    stories.append(lib_story(dict(id='reader-preview', title='The Lion and the Mouse', author='after Aesop', source='aesop-winter',
                                  grades='K-3', kind='fable', origin='Greece', decision='in', folder=SITE / 'fixtures' / 'reader-preview'), 'stories'))
stories.sort(key=lambda s: (not s['ready'], s['title'].removeprefix('The ')))
# Mythology: its own rows plus rows from other collections cross-listed by id alone (blank title).
MYTH = {  # tradition -> (label, blurb)
    'greek': ('Greek myths', 'Gods of Olympus, monsters and the heroes who faced them.'),
    'roman': ('Roman myths and legends', 'The founding of Rome, its early heroes, and the myths Ovid and Virgil retold.'),
    'homer': ('The Odyssey and the Iliad', "Homer's two epics, in full translations and in retellings for younger readers."),
    'beowulf': ('Beowulf', 'The Old English epic of a hero, a monster, a mother and a dragon.'),
    'norse': ('Norse myths', 'Odin, Thor, Loki and the end of the world, from the Eddas and the sagas.'),
    'celtic': ('Celtic myths and legends', 'Irish and Scottish gods, Finn and the Fianna, and Cuchulain.'),
    'egyptian': ('Ancient Egypt', 'Ra, Osiris, Isis and the stories of the Nile.'),
    'mesopotamian': ('Gilgamesh and Mesopotamia', 'The oldest written stories: Gilgamesh, the flood and the making of the world.'),
    'native': ('Native American stories', 'Each story is credited to the nation it comes from, and told by Native writers where we can. '
               'Some, like Lakota and Dakota Iktomi stories, are traditionally told only in winter, and teachers may want to honor that.'),
    'african': ('African folklore', 'Anansi, Cunnie Rabbit and the stories of West, Central and Southern Africa.'),
    'south-asian': ('South Asian epics and fables', 'The Ramayana, the Jataka tales and Indian folk tales.'),
    'east-asian': ('Chinese and Japanese myths', "P'an Ku, the Monkey King, Izanagi and Izanami."),
    'mesoamerican': ('Maya, Aztec and Inca', "The Popol Vuh, Quetzalcoatl and the myths of the Andes, plus Brazil's how-and-why tales."),
    'pacific': ('Hawaiian and Maori', 'Pele, Maui and the stories of the Pacific.'),
}
by_lib_id = {x['id']: x for x in stories + speeches + sacred}
mythology = []
for r in read('library/mythology.csv'):
    if r['decision'] == 'reserve':
        continue
    x = by_lib_id[r['id']] if not r['title'] else lib_story(r, 'mythology')
    mythology.append(dict(x, tradition=r['tradition']) if r['title'] else x)
    if not r['title']:
        x.setdefault('traditions', []).append(r['tradition'])
myth_own = [x for x in mythology if x['collection'] == 'mythology']
myth_trad = {t: [x for x in mythology if x.get('tradition') == t or t in x.get('traditions', [])] for t in MYTH}
lib_ready = [s for s in stories + speeches + myth_own + sacred if s['ready']]


def lib_sections(items):
    """Stories grouped by shelf, in shelf order, for the listing pages."""
    return [dict(id=sid, label=lab, blurb=blurb, href=f'/library/kind/{sid}/', items=[s for s in items if s['shelf'] == sid])
            for sid, (lab, blurb, _) in SHELVES.items() if any(s['shelf'] == sid for s in items)]


lib_trail = ('Reading Room', '/library/')
render('library/home.html', '/library/', n=len(stories), shelves=lib_sections(stories), speeches=speeches, ready=lib_ready[:8],
       n_myth=len(mythology), n_trad=len(MYTH), sacred=sacred,
       bands=bands, band_counts={b: sum(1 for s in stories if s['band'] == b) for b in bands},
       grade_counts={g: sum(1 for s in stories if g in s['fit']) for g in GRADES})
for g in GRADES:
    items = [s for s in stories if g in s['fit']]
    render('library/list.html', f'/library/grade/{g}/', title=grade_label(g), trail=[lib_trail, (grade_label(g), None)],
           lede=f'{len(items)} stories, poems and plays that fit {grade_label(g).lower()}.', sections=lib_sections(items))
for bid, b in bands.items():
    items = [s for s in stories if s['band'] == bid]
    render('library/list.html', f'/library/grade/{BAND_SLUG[bid]}/', title=b['label'], trail=[lib_trail, (b['label'], None)],
           lede=f'{len(items)} stories that start in {b["label"].lower()}.', sections=lib_sections(items), show_grades=True)
for sid, (lab, blurb, _) in SHELVES.items():
    items = [s for s in stories if s['shelf'] == sid]
    by_band = [dict(id=BAND_SLUG[b], label=bands[b]['label'], blurb='', href=f'/library/grade/{BAND_SLUG[b]}/',
                    items=[s for s in items if s['band'] == b]) for b in bands]
    render('library/list.html', f'/library/kind/{sid}/', title=lab, trail=[lib_trail, (lab, None)],
           lede=f'{blurb} {len(items)} in the Reading Room.', sections=[x for x in by_band if x['items']], show_grades=True)
render('library/list.html', '/library/speeches/', title='Speeches and Documents', trail=[lib_trail, ('Speeches and Documents', None)],
       lede='Founding documents and the speeches that moved the country, in their own words. Never adapted.',
       sections=[dict(id='collection', label='The collection', blurb='', href=None, items=speeches)], show_grades=True)
myth_sections = [dict(id=t, label=lab, blurb=blurb, href=f'/library/mythology/{t}/', items=myth_trad[t])
                 for t, (lab, blurb) in MYTH.items() if myth_trad[t]]
render('library/list.html', '/library/mythology/', title='Mythology', trail=[lib_trail, ('Mythology', None)],
       lede=f'{len(mythology)} myths, epics and legends from {len(myth_sections)} traditions around the world.',
       sections=myth_sections, show_grades=True)
for sec in myth_sections:
    render('library/list.html', sec['href'], title=sec['label'], trail=[lib_trail, ('Mythology', '/library/mythology/'), (sec['label'], None)],
           lede=f"{sec['blurb']} {len(sec['items'])} titles.", sections=[dict(sec, href=None, blurb='')], show_grades=True)
render('library/sacred.html', '/library/sacred-texts/', trail=[lib_trail, ('Sacred Texts', None)], items=sacred)
LIB_COLL = {'stories': '', 'speeches': 'Speeches and Documents', 'mythology': 'Mythology', 'sacred': 'Sacred Texts'}
lib_index = [{'t': s['title'], 'a': s.get('author', ''), 'k': s['kind'], 's': SHELVES[s['shelf']][0] if s['shelf'] else '',
              'c': LIB_COLL[s['collection']], 'o': s.get('origin', ''), 'g': grade_label(s['grades']), 'f': s['fit'],
              'u': s['url'], 'r': s['ready'], 'l': s.get('first', ''),
              'x': ' '.join(MYTH[t][0] for t in [s.get('tradition')] + s.get('traditions', []) if t in MYTH)}
             for s in stories + speeches + myth_own + sacred]
(DIST / 'library' / 'search-index.json').write_text(json.dumps(lib_index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
render('library/search.html', '/library/search/', index=False, trail=[lib_trail, ('Search', None)], n=len(lib_index))
for s in stories + speeches + myth_own + sacred:
    if not s['ready']:
        render('library/story.html', s['url'], s=s, index=False)
        continue
    dest = DIST / 'library' / s['id']
    if s['art']:
        shutil.copytree(Path(s.get('folder') or LIB / s['id']) / 'art', dest / 'art')
    render('library/story.html', s['url'], s=s)
    bundle = env.get_template('library/bundle.html').render(s=s, path=s['url'])
    for img in set(re.findall(r'src="(art/[^"]+)"', bundle)):  # the download is one offline file, so the art goes inline
        f = Path(s.get('folder') or LIB / s['id']) / img
        mime = {'.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp'}.get(f.suffix, 'image/jpeg')
        bundle = bundle.replace(f'src="{img}"', f'src="data:{mime};base64,{base64.b64encode(f.read_bytes()).decode()}"')
    (dest / f'{s["id"]}.html').write_text(bundle, encoding='utf-8')

if not LIBRARY_LIVE:
    shutil.rmtree(DIST / 'library')
    sitemap[:] = [p for p in sitemap if not p.startswith('/library/')]
if not CLOSET_LIVE:
    shutil.rmtree(DIST / 'closet')
    sitemap[:] = [p for p in sitemap if not p.startswith('/closet/')]

# search index and static pages
index = [{'t': t['title'], 'u': t['url'], 'g': grade_label(t['module']['grade']), 's': t['subject_info']['short'],
          'f': t['format_info']['label'], 'm': t['module']['title'], 'c': ' '.join(t['module']['codes']),
          'd': t['concept'], 'b': t['built']} for t in tools]
index += [{'t': m['title'], 'u': m['url'], 'g': grade_label(m['grade']), 's': subjects[m['subject']]['short'], 'f': 'Module',
           'm': m['strand'], 'c': ' '.join(m['codes']), 'd': m['description'],
           'b': any(t['built'] for t in by_module[m['module_id']])} for m in modules.values()]
index += [{'t': s['title'], 'u': s['url'], 'g': grade_label(s['grades']), 's': 'Reading Room', 'f': s['kind'],
           'm': s.get('author', ''), 'c': '', 'd': s.get('summary', ''), 'b': s['ready']} for s in stories + speeches + myth_own + sacred if LIBRARY_LIVE]
if CLOSET_LIVE:  # Supply Closet items, so "fractions vocabulary" or "photosynthesis chart" finds them
    for m in modules.values():
        mod = dict(g=grade_label(m['grade']), s=subjects[m['subject']]['short'], m=m['title'], c=' '.join(m['codes']), b=True)
        if words.get(m['module_id']):
            index.append(dict(mod, t=f"Word Wall: {m['title']}", u=m['url'] + 'words/', f='Word Wall',
                              d='Vocabulary cards: ' + ', '.join(c['word'] for c in words[m['module_id']])))
        if m['module_id'] in charts:
            ch = charts[m['module_id']]
            index.append(dict(mod, t=f"Anchor chart: {ch['title'][0]}", u=ch['url'], f='Anchor chart', d=f"The big idea of {m['title']} on one page"))
    index += [{'t': f"Poster: {p['title'][0]}", 'u': p['url'], 'g': bands[p['band']]['label'], 's': 'Supply Closet', 'f': 'Poster', 'm': '', 'c': '',
               'd': p['for'][0], 'b': True} for p in posters.values()]
    index += [{'t': f"Family game: {g['title']}", 'u': g['url'], 'g': grade_label(g['grade']), 's': subjects[g['subject']]['short'],
               'f': 'Game Night', 'm': ', '.join(x['title'] for x in g['mods']), 'c': '', 'd': g['learn'], 'b': True}
              for g in games.values()]
    index += [{'t': f"Break Box: {b['title']}", 'u': b['url'], 'g': grade_label(b['grade']), 's': 'Supply Closet',
               'f': 'Break Box', 'm': b['kind'], 'c': '', 'd': b['idea'], 'b': True} for b in breaks.values()]
    index += ws_index
(DIST / 'search-index.json').write_text(json.dumps(index, separators=(',', ':')), encoding='utf-8')
render('search.html', '/search/', index=False)
render(f'pages/{ABOUT}.html', '/about/')
for name in ['teachers', 'privacy', 'accessibility', 'license']:
    render(f'pages/{name}.html', f'/{name}/')
render('404.html', '/404.html', index=False)

(DIST / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{BASE_URL}{p}</loc></url>\n' for p in sitemap) + '</urlset>\n', encoding='utf-8')
# Cloudflare Pages headers. microphone=(self): the Desk Dock noise meter and Beat Lab ask for it (the browser still
# asks the person first); other sites framing us cannot. No X-Frame-Options: embedding tools in an LMS is a feature.
(DIST / '_headers').write_text(
    '/*\n  Link: </sitemap.xml>; rel="sitemap"\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n'
    '  Permissions-Policy: camera=(), microphone=(self), geolocation=(), interest-cohort=()\n'
    '/assets/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n', encoding='utf-8')
# Renamed or moved pages (data/redirects.csv: old,new) become permanent redirects; Workers static assets read _redirects.
(DIST / '_redirects').write_text(''.join(f"{r['old']} {r['new']} 301\n" for r in read('redirects.csv')), encoding='utf-8')
# Content Signals (contentsignals.org): Cory allows search, AI answers and AI training (2026-10-28).
(DIST / 'robots.txt').write_text(f'User-agent: *\nContent-Signal: search=yes, ai-input=yes, ai-train=yes\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n', encoding='utf-8')
# Pictures are served from R2 by worker/index.js (the static-asset file limit); keep them out of the asset upload.
# scripts/sync_media.py uploads the same two patterns. Keep the patterns here, there and in the Worker in step.
(DIST / '.assetsignore').write_text('.assetsignore\nlibrary/*/art/*.jpg\nmodules/*/words/art/*.webp\n', encoding='utf-8')
print(f'{pages} pages, {len(built)} built tools, {len(bench)} on the bench, {len(sitemap)} in sitemap -> dist/')
