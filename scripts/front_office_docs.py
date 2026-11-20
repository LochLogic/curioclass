r"""The Front Office reader: every planning document, cleaned for the public and rendered to HTML.

Called by front_office.build. Writes, under /front-office/:
    data/<subject>-ladder.json      the full skill ladder (standard, words, what it builds on, notes)
    docs/<course>/course.json       the course frame and the scope and sequence
    docs/<course>/u<NN>.json        one unit: its unit plan, its section plans and its written days

Cleaning, in order: drop internal sections by heading; drop day front matter (materials and print kept);
unwrap planning markers; remove parentheticals, sentences and list items that name files, people, dates of
production or internal steps; remove skill and item ids; render; then a last gate drops any line that still
matches front_office.FORBIDDEN, and front_office.check fails the build on any leak that gets past it.
Never reads the blind paths (math-4, ela-6).
"""
import csv
import json
import re
from collections import defaultdict

import markdown

SKILL_ID = re.compile(r'\b(?:e(?:k|\d{1,2})|m(?:k|\d)|s(?:k|\d)|ss(?:k|\d)|calc|alg[12]|geo|pc|stat|bio|chem|phys|env|'
                      r'ess|wh[12]|psy|us[12]|econ|gov)-[a-z0-9]+(?:-[a-z0-9]+)*\b')
ITEM_ID = re.compile(r'\b[su]\d\d(?:-\d+)?-[A-Z]+\d+[a-z]?(?:-\d+)?\b')
INTERNAL = re.compile(
    r'\b(?:AI|A\.I\.|Claude|Codex|GPT|Sonnet|Opus|Haiku|Gemini|agents?|LLM|Cory|Sara|Desk|BASELINE)\b'
    r'|\bmodels? (?:wrote|read)\b|\bcard q-|\.(?:md|csv|txt|py|json)\b|\b(?:data|docs|courses|scripts|closet)/'
    r'|\b20\d\d-\d\d-\d\d\b|\bfix pass|\bcatalogue id|\bskel(?:eton)?s?\b|\bfields? \d+\b|\bfields follow\b'
    r'|\bvalues rule\b|\blead (?:rule|decision|note|ruling)s?\b|\b[Ff]or the lead\b|\bthe gates?\b|\bgate (?:says|fails?|passes)'
    r'|\bspec\b|\bExit check\b|\bthe probe\b|\bexpert read|\bcheap read|\bwrite brief|\bbrief\b(?= says)'
    r'|\bL\d\d\b|\bsource (?:id|row)s?\b|\bsources? [A-Z]\d+\b|\bblind list\b|\bthe ledger\b'
    r'|\bhand-?off\b|\bqueue\b|\bdraft frame\b|\bplanning language\b|\bthe frame keeps\b|\b[Vv]alues rule'
    r'|\b[A-Z]{3,}(?:-[A-Z]{2,})+\b(?!-?\d)|\b[Tt]he CSV\b|\b[Ff]ields? \d|\bpre-work\b|\bthe writer\b'
    r'|\bPRODUCTION\b|\bwrite pass\b|\bthe builder\b')
FORBIDDEN = None   # set by front_office at import, so both files share one list

DROP_HEAD = re.compile(
    r'^(?:(?:for the lead|for cory|course text record|remaining (?:production|planning) limits|source decisions|'
    r'candidate cells settled|header|source map|sources and what is still to make|what is still to make|'
    r'change log|fix log|open questions|tokens?)\b.*|day list\b.*|.*skeleton.*|.*for the writer.*|'
    r'.*writer notes.*)', re.I)


def front_matter(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).split('\n'):
        k, _, v = line.partition(':')
        meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def _paren_pass(s):
    while True:
        t = re.sub(r'\s*\(([^()]*)\)', lambda m: '' if INTERNAL.search(m.group(1)) or SKILL_ID.search(m.group(1))
                   and not re.search(r'[A-Za-z]{4,} [A-Za-z]{4,}', SKILL_ID.sub('', m.group(1))) else m.group(0), s)
        if t == s:
            return t
        s = t


def clean_text(s):
    s = re.sub(r'\s*[,:]?\s*\[\[[^\]]+\]\]', '', s)                           # item references
    s = re.sub(r'\bCurio\b(?! Class)', 'Curio Class', s)
    s = re.sub(r'Course\s+`[^`]+`\s*\(((?:[^()]|\([^()]*\))+)\)', r'\1', s)
    s = re.sub(r'Course\s+`[^`]+`,?\s*', '', s)
    s = re.sub(r'^skill\s+\S+\s*\([^()]*\)\s*$', '', s)
    s = re.sub(r'\[([^\]]+)\]\((?![a-z]+://)[^)]*\)', r'\1', s)               # internal links keep their text
    s = s.replace('—', ', ').replace('–', ' to ') if '—' in s else s
    s = re.sub(r'`([^`]*)`', lambda m: '' if re.search(r'[-/._]', m.group(1)) and ' ' not in m.group(1)
               else m.group(1), s)
    s = _paren_pass(s)
    s = ITEM_ID.sub('', s)
    if SKILL_ID.search(s):
        s = SKILL_ID.sub('', s)
        s = re.sub(r'(?:\s*[;,]\s*){2,}', '; ', s)
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z*"“(])', s)
    s = ' '.join(p for p in parts if not INTERNAL.search(p) and not FORBIDDEN.search(p))
    s = re.sub(r'\(\s*[;,]?\s*\)', '', s)
    s = re.sub(r'\s+([,.;:!?])', r'\1', s)
    s = re.sub(r'([,;:])(?:\s*[,;:])+', r'\1', s)
    s = re.sub(r':\s*([.;])', r'\1', s)
    s = re.sub(r'([(\s])[;,]\s*', r'\1', s)
    s = re.sub(r'[ \t]{2,}', ' ', s)
    return s.strip()


def _words(s):
    return len(re.findall(r'[A-Za-z]{2,}', re.sub(r'\*\*[^*]+\*\*', '', s)))


BLOCK_START = re.compile(r'\s*(?:#|\||>|[-*+]\s|\d+[.)]\s|```|<)')


def _join_wrapped(lines):
    """Join hard-wrapped paragraph and list lines, so a sentence is cleaned whole, never half a line."""
    out = []
    for line in lines:
        if (out and line.strip() and out[-1].strip() and not BLOCK_START.match(line)
                and not re.match(r'\s*(?:#|\|)', out[-1])):
            out[-1] = out[-1].rstrip() + ' ' + line.strip()
        else:
            out.append(line)
    return out


def clean_markdown(text):
    """Cleaned markdown for one planning document."""
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    out, drop_level = [], 0
    for line in _join_wrapped(text.split('\n')):
        h = re.match(r'(#{1,6})\s+(.*)', line)
        if h:
            level = len(h.group(1))
            if drop_level and level > drop_level:
                continue
            drop_level = 0
            title = re.sub(r'^[\dA-Z]{1,3}[.)]\s+', '', h.group(2).strip())
            if level > 1 and DROP_HEAD.match(title):
                drop_level = level
                continue
            t = clean_text(h.group(2))
            if t and not INTERNAL.search(t):
                out.append(h.group(1) + ' ' + t)
            continue
        if drop_level:
            continue
        m = re.match(r'(\s*(?:>\s*)*(?:[-*+]\s+|\d+[.)]\s+)?)(.*)', line)
        prefix, body = m.group(1), m.group(2)
        if not body.strip():
            out.append(line.rstrip())
            continue
        if body.lstrip().startswith('|'):
            cells = body.strip().strip('|').split('|')
            if all(re.fullmatch(r'\s*:?-+:?\s*', c) for c in cells):
                out.append(line)
                continue
            cells = [clean_text(c) for c in cells]
            if not any(_words(c) for c in cells):
                continue
            out.append(prefix + '| ' + ' | '.join(cells) + ' |')
            continue
        t = clean_text(body)
        if not t:
            continue
        if t != body.strip() and (_words(t) < 3 or re.search(r'[:;]\s*$', t) and _words(t) < 6):
            continue
        if re.match(r'\*\*[^*]+\*\*[:.]?\s*$', t):   # a bold label left with nothing after it
            continue
        out.append(prefix + t)
    # drop headings left with nothing under them
    res = []
    for i, line in enumerate(out):
        h = re.match(r'(#{1,6})\s', line)
        if h:
            nxt = next((x for x in out[i + 1:] if x.strip()), '')
            nh = re.match(r'(#{1,6})\s', nxt)
            if not nxt or (nh and len(nh.group(1)) <= len(h.group(1))):
                continue
        res.append(line)
    md = '\n'.join(res)
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = '\n'.join(x for x in md.split('\n') if not FORBIDDEN.search(x))   # the last gate
    return md


def to_html(md):
    html = markdown.markdown(md, extensions=['tables', 'sane_lists'])
    html = re.sub(r'<table>', '<div class="fo-tw"><table>', html).replace('</table>', '</table></div>')
    return html


def doc_html(path, strip_title=True):
    text = path.read_text(encoding='utf-8')
    meta, text = front_matter(text)
    md = clean_markdown(text)
    title = ''
    m = re.match(r'\s*#\s+(.*)\n', md)
    if m and strip_title:
        title, md = m.group(1).strip(), md[m.end():]
    return title, meta, to_html(md)


def day_doc(path):
    title, meta, html = doc_html(path)
    box = []
    for key, label in [('materials', 'Materials'), ('print', 'To print')]:
        v = clean_text(meta.get(key, ''))
        if v and not FORBIDDEN.search(v):
            box.append('<p><b>%s.</b> %s</p>' % (label, markdown.markdown(v)[3:-4]))
    if box:
        html = '<div class="fo-mat">' + ''.join(box) + '</div>' + html
    return dict(t=title, h=html)


def ladder(rows, grades):
    """The full skill ladder, by grade and strand, ids replaced by what they point to."""
    by_id = {r['skill_id']: r for r in rows}

    def ref(sid):
        r = by_id.get(sid.strip())
        if not r:
            return None
        return dict(std=r['standard'], g=r['grade'], s=r['strand'].replace('-', ' ').capitalize())

    out = defaultdict(lambda: defaultdict(list))
    for r in rows:
        notes = clean_text(r['notes'])
        if FORBIDDEN.search(notes):
            notes = ''
        out[r['grade']][r['strand'].replace('-', ' ').capitalize()].append(dict(
            std=r['standard'], words=clean_text(r['words']),
            on=[x for x in (ref(i) for i in re.split(r'[;,]\s*', r['assumes'] or '') if i.strip()) if x],
            notes=notes))
    return [dict(g=g, strands=[dict(name=k, skills=v) for k, v in out[g].items()]) for g in grades if g in out]


def course_docs(root, slug, days, ddir):
    """Write docs/<slug>/course.json and one u<NN>.json per unit. Returns which documents exist."""
    d = root / 'docs' / 'courses' / slug
    cdir = ddir / slug
    cdir.mkdir(parents=True, exist_ok=True)
    have = dict(frame=False, scope=False, units={})
    course = {}
    for key, name in [('frame', 'frame.md'), ('scope', 'scope-and-sequence.md')]:
        if (d / name).exists():
            t, _, h = doc_html(d / name)
            course[key] = dict(t=t, h=h)
            have[key] = True
    (cdir / 'course.json').write_text(json.dumps(course, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    day_files = {int(p.stem[1:]): p for p in (root / 'courses' / slug).glob('*/d[0-9][0-9][0-9].md')}
    unit_of = defaultdict(list)
    for x in days:
        unit_of[x['u']].append(x['d'])
    units = sorted(set(unit_of) | {int(p.stem[1:]) for p in d.glob('s[0-9][0-9].md')})
    for n in units:
        u = dict(plan=None, sections={}, days={})
        p = d / ('s%02d.md' % n)
        if p.exists():
            t, _, h = doc_html(p)
            u['plan'] = dict(t=t, h=h)
        for sp in sorted(d.glob('u%02d-*.md' % n)):
            sid = '%d.%s' % (n, sp.stem.split('-')[1])
            t, _, h = doc_html(sp)
            u['sections'][sid] = dict(t=t, h=h)
        for dn in unit_of.get(n, []):
            if dn in day_files:
                u['days'][str(dn)] = day_doc(day_files[dn])
        have['units'][n] = dict(plan=bool(u['plan']), sections=sorted(u['sections']), days=sorted(
            int(k) for k in u['days']))
        if u['plan'] or u['sections'] or u['days']:
            (cdir / ('u%02d.json' % n)).write_text(json.dumps(u, ensure_ascii=False, separators=(',', ':')),
                                                    encoding='utf-8')
    return have
