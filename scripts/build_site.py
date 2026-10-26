"""Build the Curio Class static site into dist/ from the catalog data and tools/.

Run from the repo root:  python scripts/build_site.py
Needs Jinja2 and Markdown (pip install jinja2 markdown). No other dependencies.
"""
import base64, csv, json, re, shutil, sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
DATA, SITE, TOOLS, DIST = ROOT / 'data', ROOT / 'site', ROOT / 'tools', ROOT / 'dist'
BASE_URL = 'https://curioclass.org'
sys.path.insert(0, str(Path(__file__).parent))
from standards import validate  # noqa: E402
from bundle_tool import bundle_all  # noqa: E402

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
modules = {m['module_id']: dict(m, grades=expand(m['grade']), codes=m['standards'].split(';')) for m in read('modules.csv')}

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
shutil.copytree(SITE / 'assets', DIST / 'assets')

render('home.html', '/', built=built, bench_sample=[t for t in bench if t['title'] in
       ('Bug Hunt', 'Balance the Beam', 'Fed Chair', 'Fair Use Court')], bands=bands)

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


# grades and bands
render('grades.html', '/grades/', bands=bands, grades=grades)
for g in GRADES:
    lede = ('Teacher-led on the big screen. ' if grades[g]['band'] == 'k2' else '') + '{count} tools across {n} subjects.'
    browse_page(f'/grades/{g}/', grade_label(g), lede, [('Grades', '/grades/'), (grade_label(g), None)],
                subject_sections([m for m in modules.values() if g in m['grades']]), 'Subjects',
                fit=[g], subtitle='for every subject')
for bid, b in bands.items():
    browse_page(f'/grades/{BAND_SLUG[bid]}/', b['label'], b['blurb'] + ' {count} tools across {n} subjects.',
                [('Grades', '/grades/'), (b['label'], None)],
                subject_sections([m for m in modules.values() if set(m['grades']) & set(b['grade_list'])]), 'Subjects',
                fit=b['grade_list'], subtitle='for every subject', show_grade=True)

# subjects
render('subjects.html', '/subjects/', counts={s: sum(1 for t in tools if t['module']['subject'] == s) for s in subjects})
for sid, s in subjects.items():
    by_grade = defaultdict(list)
    for m in modules.values():
        if m['subject'] == sid:
            by_grade[m['grade']].append(dict(m, tools=by_module[m['module_id']]))
    order = sorted(by_grade, key=lambda g: (GRADES.index(g.split('-')[0]), -len(expand(g))))
    sections = [dict(id=f'grade-{g}', label=grade_label(g), color=s['color'], href=grade_href(g), note='', mods=by_grade[g])
                for g in order]
    browse_page(f'/subjects/{sid}/', s['label'], s['covers'] + '. Aligned to ' + s['primary_standards'] + '. {count} tools.',
                [('Subjects', '/subjects/'), (s['label'], None)], sections, 'Grades', subtitle='K-12', color=s['color'])

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

# standards
by_fw = defaultdict(list)
for code in sorted(standards):
    by_fw[std_framework[code]].append(code)
render('standards.html', '/standards/', by_fw=sorted(by_fw.items()))
for code, items in standards.items():
    seen, uniq = set(), []
    for t in items:
        if t['tool_id'] not in seen:
            seen.add(t['tool_id'])
            uniq.append(t)
    render('list.html', f'/standards/{slug(code)}/', title=code, lede=f'Tools aligned to {code} ({std_framework[code]}).',
           items=uniq, crumb=('Standards', '/standards/'), index=False)

# tools
render('list.html', '/tools/', title='Ready to use', lede='Every built tool. Each one is a single file that works offline.',
       items=built, crumb=None)
render('list.html', '/bench/', title='On the bench',
       lede=f'{len(bench)} tools sketched but not built yet. They move to the shelf one at a time.',
       items=bench, crumb=None, index=False)
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
        render('tool.html', t['url'], t=t, related=related, collection=collection)
    else:
        render('bench.html', t['url'], t=t, related=related, collection=collection, index=False)

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
        words = meta.get('words') or len(GLOSS.sub(r'\1', text).split())
        s.update(ready=True, meta=meta, html=html, words=words, minutes=max(1, round(words / 200)),
                 summary=meta.get('summary', s.get('summary', '')), art=(folder / 'art').is_dir())
    return s


stories = [lib_story(r, 'stories') for r in read('library/stories-pd.csv') + read('library/stories-sw.csv')
           if r['decision'] != 'reserve']
speeches = [lib_story(r, 'speeches') for r in read('library/speeches.csv') if r['decision'] != 'reserve']
if '--preview' in sys.argv:  # local check of the reader with a made-up story; never part of a deploy build
    stories.append(lib_story(dict(id='reader-preview', title='The Lion and the Mouse', author='after Aesop', source='aesop-winter',
                                  grades='K-3', kind='fable', origin='Greece', decision='in', folder=SITE / 'fixtures' / 'reader-preview'), 'stories'))
stories.sort(key=lambda s: (not s['ready'], s['title'].removeprefix('The ')))
lib_ready = [s for s in stories + speeches if s['ready']]


def lib_sections(items):
    """Stories grouped by shelf, in shelf order, for the listing pages."""
    return [dict(id=sid, label=lab, blurb=blurb, href=f'/library/kind/{sid}/', items=[s for s in items if s['shelf'] == sid])
            for sid, (lab, blurb, _) in SHELVES.items() if any(s['shelf'] == sid for s in items)]


lib_trail = ('Reading Room', '/library/')
render('library/home.html', '/library/', n=len(stories), shelves=lib_sections(stories), speeches=speeches, ready=lib_ready[:8],
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
for s in stories + speeches:
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

# search index and static pages
index = [{'t': t['title'], 'u': t['url'], 'g': grade_label(t['module']['grade']), 's': t['subject_info']['short'],
          'f': t['format_info']['label'], 'm': t['module']['title'], 'c': ' '.join(t['module']['codes']),
          'd': t['concept'], 'b': t['built']} for t in tools]
index += [{'t': s['title'], 'u': s['url'], 'g': grade_label(s['grades']), 's': 'Reading Room', 'f': s['kind'],
           'm': s.get('author', ''), 'c': '', 'd': s.get('summary', ''), 'b': s['ready']} for s in stories + speeches]
(DIST / 'search-index.json').write_text(json.dumps(index, separators=(',', ':')), encoding='utf-8')
render('search.html', '/search/', index=False)
for name in ['about', 'teachers', 'privacy', 'accessibility', 'license']:
    render(f'pages/{name}.html', f'/{name}/')
render('404.html', '/404.html', index=False)

(DIST / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{BASE_URL}{p}</loc></url>\n' for p in sitemap) + '</urlset>\n', encoding='utf-8')
# Cloudflare Pages headers. No X-Frame-Options: embedding tools in an LMS is a feature.
(DIST / '_headers').write_text(
    '/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n'
    '  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()\n'
    '/assets/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n', encoding='utf-8')
(DIST / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n', encoding='utf-8')
print(f'{pages} pages, {len(built)} built tools, {len(bench)} on the bench, {len(sitemap)} in sitemap -> dist/')
