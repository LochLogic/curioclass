"""Which Worksheet Generators fit a module, with their settings filled in (docs/SUPPLY-CLOSET-PLAN.md, Generators).

    links(module, has_words) -> [dict(id, title, url, note)]

Module pages show these as "Make a sheet" links (site/templates/module.html). A link opens the generator with the
grade, skill or word list already chosen; the generator falls back to its defaults for any setting it does not have,
so a slightly off grade is harmless. Rules go by subject, strand and grade, the same three fields every module has in
data/modules.csv. Keep them few: a module page should offer the two or three generators a teacher would really use,
not the whole shelf.
"""
import json
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parent.parent
REG = {g['id']: g for g in json.loads((ROOT / 'data/closet/generators.json').read_text(encoding='utf-8'))['generators']}
BASE = '/closet/worksheets/make/'


def grade_num(grade):
    """'k' -> 0, '3' -> 3, '6-8' -> 6 (the low end), 'k-12' -> 0."""
    g = str(grade).lower().split('-')[0]
    return 0 if g == 'k' else int(g) if g.isdigit() else None


def clamp(n, lo, hi):
    return max(lo, min(hi, n))


def band_of(grade):
    n = grade_num(grade)
    return 'k2' if n is None or n <= 2 else '35' if n <= 5 else '68' if n <= 8 else '912'


def link(gid, note='', **params):
    g = REG[gid]
    q = urlencode({k: v for k, v in params.items() if v not in (None, '')})
    return dict(id=gid, title=g['title'], url=f'{BASE}{gid}/' + (f'?{q}' if q else ''), note=note or g['blurb'])


def links(m, has_words):
    subj, strand, title = m['subject'], m.get('strand', ''), m['title']
    n = grade_num(m['grade'])
    g = str(n) if n else 'k'
    out = []
    if subj == 'math' and n is not None:
        if n <= 5 and strand in ('Counting and Cardinality', 'Number and Operations in Base Ten', 'Operations and Algebraic Thinking'):
            out.append(link('number-ops', 'Facts and column work for this grade, with or without regrouping.', grade=g if n else 'k'))
            if n >= 1:
                out.append(link('word-problems', 'Story problems at this grade, answers worked on the key.', grade=str(clamp(n, 1, 6))))
        if 'Fractions' in strand or (strand == 'The Number System' and n <= 7):
            out.append(link('fractions', 'Fraction practice for this grade, from naming parts to operations.', grade=str(clamp(n, 3, 7))))
        if strand in ('Expressions and Equations', 'Algebra') or (strand == 'Functions' and n <= 9):
            out.append(link('equations', 'Expressions and equations at this grade, every answer checked.', grade=str(clamp(n, 6, 9))))
        if strand in ('Measurement and Data', 'Geometry') and 2 <= n <= 8:
            out.append(link('measure-shapes', 'Perimeter, area and volume problems drawn to scale.', grade=str(clamp(n, 2, 8))))
        if strand in ('Statistics and Probability', 'Measurement and Data') and 1 <= n <= 8 and ('Data' in strand or 'Statistics' in strand):
            out.append(link('graph-reading', 'Tables, bar graphs, line graphs and plots to read.', grade=str(clamp(n, 1, 8))))
        if strand == 'Ratios and Proportional Relationships':
            out.append(link('word-problems', 'Rate and percent story problems.', grade='6', topic='rates'))
    if subj == 'science' and n is not None:
        if strand in ('Physical Science', 'Energy') and n >= 6:
            out.append(link('science-calc', 'Formula practice with units and the worked answer.', grade=str(clamp(n, 6, 12))))
        if strand == 'Life Science' and n >= 7:
            out.append(link('punnett', 'Monohybrid and dihybrid crosses with the ratios worked out.', grade=str(clamp(n, 7, 12))))
        if strand in ('Earth and Space Science', 'Life Science', 'Physical Science') and 1 <= n <= 8:
            out.append(link('graph-reading', 'Data tables and graphs to read, science settings.', grade=str(clamp(n, 1, 8))))
    if subj == 'social-studies' and n is not None:
        if strand == 'Geography' and n <= 6:
            out.append(link('map-skills', 'Compass, grid and key practice on a drawn map.', grade=str(clamp(n, 1, 6))))
        if strand == 'History' and n >= 2:
            out.append(link('timeline', 'Timelines to build and read.', grade=str(clamp(n, 2, 12))))
    if has_words:
        band = band_of(m['grade'])
        out.append(link('vocabulary', "This module's Word Wall words: match, fill in, sort and use.", subject=subj, band=band, mod=m['module_id']))
        if band != 'k2':
            out.append(link('word-puzzles', "Crosswords and word searches from this module's words.", subject=subj, band=band, mod=m['module_id']))
    out.append(link('organizer', 'A graphic organizer with this module as the title.', band=band_of(m['grade']), topic=title))
    if subj in ('ela', 'social-studies', 'science', 'eld') and n is not None and n >= 1:
        out.append(link('writing-frame', 'Sentence starters and paragraph frames for a write-up.', grade=str(clamp(n, 1, 12)), topic=title))
    # at most four: the skill generators first, then the words, then the thinking pages; puzzles and frames fill in
    skills = [g for g in out if g['id'] not in ('vocabulary', 'word-puzzles', 'organizer', 'writing-frame')]
    rest = [g for g in out if g not in skills]
    order = ['vocabulary', 'organizer', 'word-puzzles', 'writing-frame']
    rest.sort(key=lambda g: order.index(g['id']))
    return (skills + rest)[:4]
