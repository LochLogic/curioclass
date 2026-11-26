"""A written plan's facts, rendered from data, beside its prose (consolidation 4.E2 step 4).

    python -X utf8 scripts/plan_facts.py <course> <sNN.md | uNN-N.md> [--facts]
    python -X utf8 scripts/plan_facts.py links [--write]    each plan's Front Office link line under its title
    python -X utf8 scripts/plan_facts.py --self-test

Written plans (docs/courses/<course>/sNN.md unit plans, uNN-N.md section plans) hold judgment prose only. The
mechanical fields (codes, own-word lines, weights, source rows, minutes, the section header and so on) live in data
and are rendered here, never stored in the plan. Every reader that needs a plan's facts reads `merged()`: the plan's
prose with any old `<!-- skel -->` blocks taken out and today's blocks from data put at the top of each field. The
merged view of a plan is the same before and after its stored blocks are stripped, which is what proves the strip
lost nothing.

The command prints the merged view (the writer's read view); --facts prints only the rendered facts.
Blocks in the merged view keep their markers, so word caps that leave them out work unchanged.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs' / 'courses'
OPEN, CLOSE = '<!-- skel -->', '<!-- /skel -->'
BLOCK = re.compile(r'[ \t]*<!-- skel -->.*?<!-- /skel -->[ \t]*(\n|\Z)', re.S)
HEAD = re.compile(r'^## .*$', re.M)
PLAN = re.compile(r's\d+\.md|u\d+-\d+\.md')
LEFT = '## Facts from data with no matching field in the plan'   # a plan with no heading at all for a field
FROM_DATA = ' <!-- from data -->'   # ends a heading the merged view adds (word caps never count it)

_cache = {}


LINK_MARK = '<!-- facts link -->'
LINK_LINE = re.compile(r'^[^\n]*' + re.escape(LINK_MARK) + r'[ \t]*\n(?:[ \t]*\n)?', re.M)
SITE = 'https://curioclass.org/front-office/'


def strip(text):
    """The plan with every stored block and its facts link line taken out, and nothing else changed."""
    return LINK_LINE.sub('', BLOCK.sub('', text.replace('\r\n', '\n')))


def link_line(course, name, subject):
    """The line under a plan's title that opens it with its facts on the Front Office, for a reader on GitHub, where
    the stripped plan shows prose only (close review, "what got worse" (a); 4.L row 8). The merged view drops it."""
    m = re.fullmatch(r's(\d+)\.md', name)
    if m:
        where = '%d/plan' % int(m.group(1))
    else:
        m = re.fullmatch(r'u(\d+)-(\d+)\.md', name)
        where = '%d/s/%d.%s' % (int(m.group(1)), int(m.group(1)), m.group(2))
    return ('Read this plan with its facts from data (days, codes, minutes): [the Front Office](%s#%s/%s/%s), or '
            '`python -X utf8 scripts/plan_facts.py %s %s`. %s' % (SITE, subject, course, where, course, name, LINK_MARK))


def subject(course):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import course_pages
    return {c['slug']: c['subject'] for c in course_pages.load()}[course]


def with_link(course, name, text, subj=None):
    """The plan text with its one facts link line right under the title (what a writer of a new plan stores)."""
    body = LINK_LINE.sub('', text.replace('\r\n', '\n'))
    title, sep, rest = body.partition('\n')
    if not title.startswith('# '):
        title, rest = '', body
    want = link_line(course, name, subj or subject(course))
    return (title + '\n\n' if title else '') + want + '\n\n' + rest.lstrip('\n')


def links(write=False):
    """Lines for each written plan whose facts link line is missing or out of date; --write puts it right."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import course_pages
    import safe_write
    subj = {c['slug']: c['subject'] for c in course_pages.load()}
    out = []
    for course in sorted(subj):
        d = DOCS / course
        for p in sorted(d.glob('s[0-9][0-9].md')) + sorted(d.glob('u[0-9][0-9]-[0-9]*.md')):
            if not PLAN.fullmatch(p.name):
                continue
            raw = p.read_bytes().decode('utf-8')
            nl = '\r\n' if '\r\n' in raw else '\n'
            text = raw.replace('\r\n', '\n')
            want = link_line(course, p.name, subj[course])
            have = [m.group(0).rstrip('\n').rstrip() for m in LINK_LINE.finditer(text)]
            if have == [want]:
                continue
            out.append('plan-link docs/courses/%s/%s: %s (plan_facts.py links --write)'
                       % (course, p.name, 'no Front Office link line' if not have else 'link line out of date'))
            if write:
                new = with_link(course, p.name, text, subj[course])
                with safe_write.lock(p):
                    safe_write.replace(p, new.replace('\n', nl))
    return out


def key(heading):
    m = re.match(r'## (U?\d+)\.', heading)
    return m.group(1) if m else heading.strip()


def split(text):
    """[(heading or '' for the part before the first heading, body)], in order."""
    out, last, head = [], 0, ''
    for m in HEAD.finditer(text):
        out.append((head, text[last:m.start()]))
        head, last = m.group(0), m.end()
    out.append((head, text[last:]))
    return out


def render(course, name):
    """Today's skeleton for this plan, from data (and, for a section plan, the merged unit plan)."""
    k = (course, name)
    if k not in _cache:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import unit_skeleton as u
        keep = u.SUBJ
        try:
            m = re.fullmatch(r's(\d+)\.md', name)
            if u.subject_of(course) is None:
                _cache[k] = ''      # a folder that is not a course of frames.csv (math-4, arts) has no facts to render
            elif m:
                u.set_subject(u.subject_of(course))
                _cache[k] = u.build(course, int(m.group(1)))
            else:
                import section_skeleton as sk
                m = re.fullmatch(r'u(\d+)-(\d+)\.md', name)
                _cache[k] = sk.build(course, '%d.%s' % (int(m.group(1)), m.group(2)))
        finally:
            u.set_subject(keep)
    return _cache[k]


def facts(course, name):
    """{field key: [block, ...]} in render order; a block keeps its markers."""
    out = {}
    for head, body in split(render(course, name).replace('\r\n', '\n')):
        bl = [m.group(0).strip() for m in BLOCK.finditer(body)]
        if bl:
            out.setdefault(key(head) if head else '', []).extend(bl)
    return out


def merged(course, name, text=None):
    """The plan's prose with today's facts at the top of each field (the read view every reader uses)."""
    if text is None:
        p = DOCS / course / name
        text = p.read_text(encoding='utf-8') if p.exists() else ''
    f = facts(course, name)
    heads = {key(h) if h else '' for h, _ in split(text)}
    if '## Header' in f and '## Header' not in heads:      # older section plans keep the header before any heading
        f.setdefault('', [])[:0] = f.pop('## Header')
    parts = []
    for head, body in split(strip(text)):
        bl = f.pop(key(head) if head else '', [])
        if not bl:
            parts.append((head + '\n' if head else '') + body if head else body)
            continue
        if head:
            parts.append(head + '\n\n' + '\n\n'.join(bl) + '\n\n' + body.lstrip('\n'))
        else:                                  # the part before the first heading: facts after the title line
            lines = body.split('\n', 1) if body.startswith('# ') else ['', body]
            parts.append((lines[0] + '\n\n' if lines[0] else '') + '\n\n'.join(bl) + '\n\n'
                         + (lines[1] if len(lines) > 1 else '').lstrip('\n'))
    for k_, bl in f.items():           # a field the plan has no heading for: under its own heading, at the end
        parts.append('\n' + (k_ if k_.startswith('## ') else LEFT) + FROM_DATA + '\n\n' + '\n\n'.join(bl) + '\n')
    return ''.join(parts)


def read(path):
    """Read a written plan through the merged view; any other file as it is."""
    path = Path(path)
    if not path.is_absolute() and not path.exists():
        path = ROOT / path
    path = path.resolve()
    text = path.read_text(encoding='utf-8')
    if PLAN.fullmatch(path.name) and path.parent.parent == DOCS.resolve():
        return merged(path.parent.name, path.name, text)
    return text


def self_test():
    ok = True

    def check(name, cond):
        nonlocal ok
        ok = ok and cond
        print('  %s %s' % ('ok    ' if cond else 'FAILED', name))
    t = '# T\n\nintro\n<!-- skel -->\nold\n<!-- /skel -->\n## 2. Standards\n\nprose a\n<!-- skel -->\nx\n<!-- /skel -->\nprose b\n'
    check('strip takes out the blocks and nothing else', strip(t) == '# T\n\nintro\n## 2. Standards\n\nprose a\nprose b\n')
    check('split keeps every character', ''.join(h + ('\n' if h else '') + b if h else b for h, b in split(strip(t)))
          .replace('\n\n', '\n') != '' and len(split(t)) == 2)
    check('field keys', key('## 2. Standards, limits') == '2' and key('## U3. Section') == 'U3' and key('## Day list') == '## Day list')
    # a real plan: merged is the same with the stored blocks and without them
    c, n = 'math-grade-3', 's02.md'
    p = DOCS / c / n
    if p.exists():
        raw = p.read_text(encoding='utf-8')
        a, b = merged(c, n, raw), merged(c, n, strip(raw))
        check('merged view is the same before and after the strip (%s %s)' % (c, n), a == b)
        check('merged view carries today\'s facts', all(x in a for bl in facts(c, n).values() for x in bl))
        check('merged view keeps every prose line', all(ln in a for ln in strip(raw).splitlines() if ln.strip()))
    print('plan_facts self-test: %s' % ('all passed' if ok else 'FAILED'))
    return 0 if ok else 1


def main(a):
    if a == ['--self-test']:
        return self_test()
    if a[:1] == ['links']:
        lines = links('--write' in a)
        print('\n'.join(lines))
        print('plan links: %d plan(s) %s' % (len(lines), 'put right' if '--write' in a else 'missing or out of date'))
        return 1 if lines and '--write' not in a else 0
    only = '--facts' in a
    a = [x for x in a if x != '--facts']
    if len(a) != 2 or not PLAN.fullmatch(a[1]):
        print(__doc__)
        return 2
    if only:
        print('\n\n'.join(b for bl in facts(a[0], a[1]).values() for b in bl))
    else:
        sys.stdout.write(merged(a[0], a[1]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
