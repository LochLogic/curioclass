r"""Worksheets (docs/WORKSHEETS-PLAN.md): parse the built sheets in data/closet/worksheets/<unit-id>.md, render each one
to an HTML fragment for the shared viewer, and check every answer key.

    python scripts/worksheets.py            check every built sheet, exit 1 on any problem
    python scripts/worksheets.py math-3     check one unit's file

A unit file holds the built sheets of one class, each matching its row in the concept list (docs/worksheets/):

    # 7. Times Table Cross-Number          the number and title from the concept list
    minutes: 20
    materials: pencil
    ican: I can multiply within 100.
    directions: Solve each clue. Write one digit in each box.
    pairs: array-builder                   optional: a tool id it goes with
    mistakes: What to watch for.           teacher page
    notes: Anything else for the teacher.  teacher page

    ## Warm up                             a part; "## Main", "## Stretch", or any name
    fill: 3 x 4 = {12}                      a block: "kind: text", with indented lines (two spaces) as its body

Text anywhere may hold {answer} blanks (a line on the student copy, the answer on the key) and **bold**.
The block kinds are the KINDS below; each renderer's docstring shows its body.
"""
import html, random, re, sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / 'data' / 'closet' / 'worksheets'
ICONS = ROOT / 'site' / 'assets' / 'ws-icons.svg'
HEAD_KEYS = {'minutes', 'materials', 'ican', 'directions', 'pairs', 'mistakes', 'notes'}
NEED = {'minutes', 'materials', 'ican', 'directions'}
ROMAN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Word pieces a child sees on their own (the rest of a word after a blank) must not read as a rude word: "{gr}ass".
UNSAFE = re.compile(r'(?i)^\W*(ass|asses|butt|hell|damn|crap|sex|piss|poo|poop|pee|tit|tits|fart|dick|cock|cum|fag|nazi|kill|die|dumb|stupid|hate)\W*$')


class SheetError(Exception):
    pass


def esc(s):
    return html.escape(str(s), quote=True)


def inline(s, answers=None):
    """Escape text, then turn {answer} into a blank and **x** into bold. answers collects the blanks."""
    out = []
    for i, part in enumerate(re.split(r'\{([^{}]*)\}', s)):
        if i % 2:
            if answers is not None:
                answers.append(part)
            w = max(2.2, min(10, 0.62 * len(part) + 1.4))
            out.append(f'<span class="ws-blank" style="min-width:{w:.1f}em"><span class="ws-ans">{esc(part)}</span></span>')
        else:
            out.append(re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', esc(part)))
    return ''.join(out)


def icon(name, cls='ws-icon'):
    return f'<svg class="{cls}" aria-hidden="true"><use href="/assets/ws-icons.svg#i-{esc(name)}"></use></svg>'


def lines(n, cls='ws-lines'):
    return f'<div class="{cls}">' + '<span></span>' * int(n) + '</div>'


def key(text):
    return f'<p class="ws-keyonly"><b>Answer:</b> {inline(text)}</p>' if text else ''


def items(body):
    """'- a' / '* a' lines -> [(marked, text)]"""
    out = []
    for l in body:
        m = re.match(r'([-*])\s+(.*)', l)
        if not m:
            raise SheetError(f'expected "- item" or "* item", got {l!r}')
        out.append((m.group(1) == '*', m.group(2)))
    return out


def opts(body):
    """'key: value' body lines -> dict, others -> list"""
    d, rest = {}, []
    for l in body:
        m = re.match(r'([a-z]+):\s*(.*)', l)
        if m:
            d[m.group(1)] = m.group(2)
        else:
            rest.append(l)
    return d, rest


# ---------- block renderers: (args, body, ctx) -> html; ctx has rng, answers, checks ----------

def b_text(a, body, c):
    """text: A paragraph, with {blanks} if you like."""
    return f'<p class="ws-text">{inline(" ".join([a] + body), c["answers"])}</p>'


def b_example(a, body, c):
    """example: Worked example, shown in a box. More lines follow, indented."""
    rows = ''.join(f'<p>{inline(l)}</p>' for l in [a] + body if l)
    return f'<div class="ws-example"><p class="ws-tag">Example</p>{rows}</div>'


def b_fill(a, body, c):
    """fill: 3 x 4 = {12}      one numbered item; or "fill:" with "- item" lines for a list"""
    rows = [a] if a else [t for _, t in items(body)]
    lis = ''.join(f'<li>{inline(t, c["answers"])}</li>' for t in rows)
    cls = ' ws-cols' if len(rows) > 5 and max(len(t) for t in rows) < 28 else ''
    return f'<ol class="ws-fill{cls}" start="{c["n"]}">{lis}</ol>', len(rows)


def b_choice(a, body, c):
    """choice: Question?   then "- wrong" and "* right" option lines (exactly one *)"""
    its = items(body)
    right = [i for i, (m, _) in enumerate(its) if m]
    if len(right) != 1:
        raise SheetError(f'choice {a!r} needs exactly one * option')
    c['answers'].append(ROMAN[right[0]])
    lis = ''.join(f'<li class="{"ws-right" if m else ""}"><span class="ws-bubble">{ROMAN[i]}</span> {inline(t)}</li>'
                  for i, (m, t) in enumerate(its))
    return f'<div class="ws-q"><p><span class="ws-num">{c["n"]}.</span> {inline(a)}</p><ul class="ws-choice">{lis}</ul></div>', 1


def b_write(a, body, c):
    """write: Prompt   then "lines: 3" and "key: a model answer" (the key shows on the teacher copy)"""
    d, rest = opts(body)
    if 'key' not in d:
        raise SheetError(f'write {a!r} needs a key: line (a model answer)')
    starter = f'<p class="ws-starter">{inline(d["starter"])}</p>' if 'starter' in d else ''
    return (f'<div class="ws-q"><p><span class="ws-num">{c["n"]}.</span> {inline(" ".join([a] + rest))}</p>{starter}'
            f'{lines(d.get("lines", 3))}{key(d["key"])}</div>'), 1


def b_lines(a, body, c):
    """lines: 4   blank writing lines"""
    return lines(a or 3)


def b_draw(a, body, c):
    """draw: Label for the box | 2.2   an empty box to draw in, height in inches"""
    label, _, h = a.partition('|')
    return f'<div class="ws-draw" style="height:{float(h or 2):.2f}in"><span>{inline(label.strip())}</span></div>'


def b_trace(a, body, c):
    """trace: 1 2 3 4 5   big dotted numerals or letters to trace, each with a box to write it after"""
    cells = ''.join(f'<span class="ws-trace-cell"><span class="ws-trace">{esc(t)}</span><span class="ws-trace-try"></span></span>'
                    for t in a.split())
    return f'<div class="ws-trace-row">{cells}</div>'


def b_chain(a, body, c):
    """chain: 1 2 {3} 4   a caterpillar of circles, one number or blank in each (a head starts it)"""
    toks = a.split()
    nums = []
    for t in toks:
        m = re.fullmatch(r'\{(.+)\}|(.+)', t)
        nums.append(m.group(1) or m.group(2))
    try:
        vals = [Fraction(x) for x in nums]
        steps = {vals[i + 1] - vals[i] for i in range(len(vals) - 1)}
        if len(steps) != 1:
            raise SheetError(f'chain {a!r} does not count by one step')
    except ValueError:
        pass
    head = ('<svg class="ws-chain-head" viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="34" r="22" fill="none" '
            'stroke="#222" stroke-width="2.5"/><circle cx="22" cy="30" r="3"/><circle cx="38" cy="30" r="3"/>'
            '<path d="M21 42 q9 7 18 0" fill="none" stroke="#222" stroke-width="2.5"/><path d="M22 13 l-6 -10 M38 13 l6 -10" '
            'stroke="#222" stroke-width="2.5"/></svg>')
    seg = ''.join(f'<span class="ws-seg">{inline(t, c["answers"]) if t.startswith("{") else esc(t)}</span>' for t in toks)
    return f'<div class="ws-chain">{head}{seg}</div>'


def b_picword(a, body, c):
    """picword:   then "- star | {st}ar" lines: a picture from the icon set and the word with a blank"""
    cells = []
    for _, t in items(body):
        name, _, word = (x.strip() for x in t.partition('|'))
        if not re.search(rf'id="i-{re.escape(name)}"', ICONS.read_text()):
            raise SheetError(f'no icon {name!r} in ws-icons.svg')
        for piece in re.split(r'\{[^{}]*\}', word):
            if UNSAFE.search(piece):
                raise SheetError(f'picword {word!r}: the part students see, {piece!r}, reads as a rude word; pick another word')
        cells.append(f'<div class="ws-pic">{icon(name)}<p>{inline(word, c["answers"])}</p></div>')
        c['words'].append(re.sub(r'[{}]', '', word))
    return f'<div class="ws-pics">{"".join(cells)}</div>'


def b_sort(a, body, c):
    """sort: Title   then "- Column: card, card" lines. Students get empty columns and shuffled cards to cut."""
    cols = [(h.strip(), [x.strip() for x in cards.split(',')]) for _, t in items(body) for h, _, cards in [t.partition(':')]]
    if 'words' in c and c['words']:
        missing = {w for h, cs in cols for w in cs} ^ set(c['words'])
        if missing:
            raise SheetError(f'sort cards and picture words differ: {sorted(missing)}')
    heads = ''.join(f'<div class="ws-sort-col"><p class="ws-sort-head">{esc(h)}</p><div class="ws-sort-drop">'
                    f'<span class="ws-keyonly">{esc(", ".join(cs))}</span></div></div>' for h, cs in cols)
    cards = [x for _, cs in cols for x in cs]
    c['rng'].shuffle(cards)
    strip = ''.join(f'<span class="ws-card">{esc(x)}</span>' for x in cards)
    title = f'<p class="ws-sub">{inline(a)}</p>' if a else ''
    return (f'{title}<div class="ws-sort" style="--cols:{len(cols)}">{heads}</div>'
            f'<div class="ws-cut"><p class="ws-tag">Cut out the cards</p><div class="ws-cards">{strip}</div></div>')


def b_table(a, body, c):
    """table: Head | Head | Head   then "- cell | {answer} | cell" rows (empty cells are blank boxes)"""
    heads = [h.strip() for h in a.split('|')]
    rows = [[x.strip() for x in t.split('|')] for _, t in items(body)]
    if any(len(r) != len(heads) for r in rows):
        raise SheetError(f'table {a!r} has rows of the wrong width')
    th = ''.join(f'<th>{esc(h)}</th>' for h in heads)
    tr = ''.join('<tr>' + ''.join(f'<td>{inline(x, c["answers"]) if x else ""}</td>' for x in r) + '</tr>' for r in rows)
    return f'<table class="ws-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def b_graph(a, body, c):
    """graph: x label | 0 10 1 | y label | 0 100 10   then optional "key: x,y x,y ..." points drawn on the key only"""
    xl, xr, yl, yr = (p.strip() for p in a.split('|'))
    x0, x1, xs = (float(v) for v in xr.split())
    y0, y1, ys = (float(v) for v in yr.split())
    d, _ = opts(body)
    nx, ny = round((x1 - x0) / xs), round((y1 - y0) / ys)
    W, H, L, B, sub = 600, 330, 56, 40, 2
    cw, ch = (W - L - 14) / (nx * sub), (H - B - 10) / (ny * sub)
    g = [f'<svg class="ws-graph" viewBox="0 0 {W} {H}" role="img" aria-label="Graph grid">']
    for i in range(nx * sub + 1):
        x = L + i * cw
        g.append(f'<line x1="{x:.1f}" y1="10" x2="{x:.1f}" y2="{H - B}" stroke="#999" stroke-width="{0.9 if i % sub == 0 else 0.4}"/>')
        if i % sub == 0:
            g.append(f'<text x="{x:.1f}" y="{H - B + 15}" font-size="12" text-anchor="middle">{x0 + i // sub * xs:g}</text>')
    for j in range(ny * sub + 1):
        y = H - B - j * ch
        g.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W - 14}" y2="{y:.1f}" stroke="#999" stroke-width="{0.9 if j % sub == 0 else 0.4}"/>')
        if j % sub == 0:
            g.append(f'<text x="{L - 6}" y="{y + 4:.1f}" font-size="12" text-anchor="end">{y0 + j // sub * ys:g}</text>')
    g.append(f'<text x="{(L + W) / 2:.0f}" y="{H - 6}" font-size="13" text-anchor="middle" font-weight="700">{esc(xl)}</text>')
    g.append(f'<text x="14" y="{(H - B) / 2:.0f}" font-size="13" text-anchor="middle" font-weight="700" '
             f'transform="rotate(-90 14 {(H - B) / 2:.0f})">{esc(yl)}</text>')
    if 'key' in d:
        pts = [tuple(float(v) for v in p.split(',')) for p in d['key'].split()]
        xy = [(L + (px - x0) / xs * sub * cw, H - B - (py - y0) / ys * sub * ch) for px, py in pts]
        g.append('<g class="ws-keyonly">' + f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in xy)}" fill="none" '
                 'stroke="#c0392b" stroke-width="2"/>' + ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="#c0392b"/>'
                                                                 for x, y in xy) + '</g>')
    g.append('</svg>')
    return ''.join(g)


def b_passage(a, body, c):
    """passage: Title   then the text, one paragraph per indented line; lines are numbered for citing"""
    paras = ''.join(f'<p>{inline(p)}</p>' for p in body)
    words = sum(len(p.split()) for p in body)
    c['passage_words'].append(words)
    return f'<div class="ws-passage"><h3>{inline(a)}</h3>{paras}</div>'


def b_source(a, body, c):
    """source: Who, what, where, when (the citation)   then the excerpt, one paragraph per line, with [1] markers"""
    paras = ''.join(f'<p>{re.sub(r"\[(\d+)\]", r"<sup class=\"ws-mark\">\1</sup>", inline(p))}</p>' for p in body)
    return f'<figure class="ws-source"><blockquote>{paras}</blockquote><figcaption>{inline(a)}</figcaption></figure>'


def b_colorcode(a, body, c):
    """colorcode: Title
      code: y = yellow: odd | b = light blue: even          a picture character, its color, and which answers get it
      problems: A 3 x 5, B 4 x 6, ...                     letter, then a whole-number expression (x or * for times)
      picture rows, one character per square (each character a code above)
    Every square gets a problem letter whose answer belongs to that square's color, so the key is computed."""
    d, rows = opts(body)
    code = {}
    for part in d['code'].split('|'):
        ch, color, rule = (x.strip() for x in part.split(':')[0].split('=') + [part.split(':', 1)[1]])
        code[ch] = (color, rule)
    probs = []
    for p in d['problems'].split(','):
        letter, expr = p.strip().split(' ', 1)
        val = Fraction(evaluate(expr))
        probs.append((letter, expr.strip(), val))

    def fits(val, rule):
        if rule == 'odd':
            return val.denominator == 1 and val.numerator % 2 == 1
        if rule == 'even':
            return val.denominator == 1 and val.numerator % 2 == 0
        return val in {Fraction(x) for x in rule.split()}
    pools = {ch: [l for l, _, v in probs if fits(v, rule)] for ch, (_, rule) in code.items()}
    for ch, pool in pools.items():
        if not pool:
            raise SheetError(f'colorcode: no problem answers fit {code[ch]}')
    for l, e, v in probs:
        n = sum(fits(v, r) for _, r in code.values())
        if n != 1:
            raise SheetError(f'colorcode: problem {l} ({e} = {v}) fits {n} colors')
    width = len(rows[0])
    if any(len(r) != width for r in rows) or set(''.join(rows)) - set(code):
        raise SheetError('colorcode: picture rows must be the same width and use only code characters')
    fill = {'yellow': '#f6d743', 'light blue': '#a9d4f5', 'red': '#e05a47', 'green': '#6cbf5a', 'brown': '#9a6a3c',
            'orange': '#f39c3d', 'gray': '#b9b9b9', 'black': '#333', 'purple': '#9b6bc6', 'pink': '#f4a6c0', 'blue': '#3a6ea5'}
    s = 28
    svg = [f'<svg class="ws-cbc" viewBox="0 0 {width * s + 2} {len(rows) * s + 2}" role="img" aria-label="Color by code grid">']
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            letter = c['rng'].choice(pools[ch])
            svg.append(f'<rect x="{x * s + 1}" y="{y * s + 1}" width="{s}" height="{s}" fill="#fff" stroke="#555" stroke-width="1"/>'
                       f'<rect class="ws-keyonly" x="{x * s + 1}" y="{y * s + 1}" width="{s}" height="{s}" fill="{fill[code[ch][0]]}" '
                       f'stroke="#555" stroke-width="1"/>'
                       f'<text x="{x * s + 1 + s / 2}" y="{y * s + 1 + s / 2 + 5}" font-size="13" text-anchor="middle">{letter}</text>')
    svg.append('</svg>')
    legend = ''.join(f'<li><span class="ws-swatch" style="--sw:{fill[col]}"></span><b>{esc(col)}</b>: {esc(rule)} answers</li>'
                     for col, rule in code.values())
    plist = ''.join(f'<li><b>{l}</b> {esc(e.replace("*", "×").replace(" x ", " × "))} = <span class="ws-blank" style="min-width:2.4em">'
                    f'<span class="ws-ans">{v}</span></span></li>' for l, e, v in probs)
    c['answers'] += [str(v) for _, _, v in probs]
    return (f'<p class="ws-sub">{inline(a)}</p><div class="ws-cbc-wrap"><div><ol class="ws-cbc-probs">{plist}</ol>'
            f'<p class="ws-tag">Color key</p><ul class="ws-legend">{legend}</ul></div>{"".join(svg)}</div>')


def b_binary(a, body, c):
    """binary: Title   then "bits: 5" and "numbers: 4 14 31 ..." : one row per number to write in binary and shade"""
    d, _ = opts(body)
    bits = int(d.get('bits', 5))
    nums = [int(x) for x in d['numbers'].split()]
    if max(nums) >= 2 ** bits:
        raise SheetError(f'binary: {max(nums)} needs more than {bits} bits')
    places = [2 ** i for i in reversed(range(bits))]
    th = '<th>Number</th>' + ''.join(f'<th>{p}</th>' for p in places)
    tr = ''
    for n in nums:
        cells = ''.join(f'<td class="ws-bit{" ws-one" if n & p else ""}"><span class="ws-ans">{1 if n & p else 0}</span></td>'
                        for p in places)
        tr += f'<tr><th>{n}</th>{cells}</tr>'
        c['answers'].append(format(n, f'0{bits}b'))
    return f'<p class="ws-sub">{inline(a)}</p><table class="ws-table ws-binary"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


SHAPES = {  # name -> (points on a 0..100 square, lines of symmetry as point pairs)
    'square': ([(15, 15), (85, 15), (85, 85), (15, 85)], [((50, 5), (50, 95)), ((5, 50), (95, 50)), ((8, 8), (92, 92)), ((92, 8), (8, 92))]),
    'rectangle': ([(5, 25), (95, 25), (95, 75), (5, 75)], [((50, 15), (50, 85)), ((0, 50), (100, 50))]),
    'equilateral triangle': ([(50, 10), (93, 85), (7, 85)], [((50, 2), (50, 92)), ((7, 85), (78.6, 44.2)), ((93, 85), (21.4, 44.2))]),
    'isosceles triangle': ([(50, 8), (78, 90), (22, 90)], [((50, 2), (50, 96))]),
    'regular hexagon': ([(27.5, 11), (72.5, 11), (95, 50), (72.5, 89), (27.5, 89), (5, 50)],
                        [((27.5, 11), (72.5, 89)), ((72.5, 11), (27.5, 89)), ((0, 50), (100, 50)), ((50, 2), (50, 98)),
                         ((16.25, 30.5), (83.75, 69.5)), ((83.75, 30.5), (16.25, 69.5))]),
    'parallelogram': ([(25, 25), (95, 25), (75, 75), (5, 75)], []),
    'kite': ([(50, 5), (80, 40), (50, 95), (20, 40)], [((50, 0), (50, 100))]),
    'scalene triangle': ([(15, 85), (90, 85), (35, 20)], []),
    'heart': ([(50, 92), (12, 52), (10, 30), (22, 15), (38, 14), (50, 28), (62, 14), (78, 15), (90, 30), (88, 52)], [((50, 5), (50, 98))]),
    'arrow': ([(50, 5), (85, 45), (62, 45), (62, 95), (38, 95), (38, 45), (15, 45)], [((50, 0), (50, 100))]),
}


def b_symmetry(a, body, c):
    """symmetry: Title   then "- shape name" lines from SHAPES; students draw every line of symmetry, the key shows them"""
    cells = []
    for _, name in items(body):
        if name not in SHAPES:
            raise SheetError(f'symmetry: no shape {name!r}')
        pts, axes = SHAPES[name]
        ax = ''.join(f'<line class="ws-keyonly" x1="{p[0]}" y1="{p[1]}" x2="{q[0]}" y2="{q[1]}" stroke="#c0392b" '
                     f'stroke-width="1.6" stroke-dasharray="5 3"/>' for p, q in axes)
        poly = ' '.join(f'{x},{y}' for x, y in pts)
        cells.append(f'<div class="ws-shape"><svg viewBox="-4 -4 108 108" aria-hidden="true"><polygon points="{poly}" fill="none" '
                     f'stroke="#222" stroke-width="2.2"/>{ax}</svg><p>Lines: <span class="ws-blank" style="min-width:2em">'
                     f'<span class="ws-ans">{len(axes)}</span></span></p></div>')
        c['answers'].append(str(len(axes)))
    return f'<p class="ws-sub">{inline(a)}</p><div class="ws-shapes">{"".join(cells)}</div>'


def b_halves(a, body, c):
    """halves: Title   then "- x,y x,y ..." lines: the left half of a design on a 6 x 8 dot grid with the mirror line at x = 6.
    Students finish the right half; the key draws it."""
    cells = []
    for _, t in items(body):
        pts = [tuple(int(v) for v in p.split(',')) for p in t.split()]
        if any(x > 6 or x < 0 or y < 0 or y > 8 for x, y in pts):
            raise SheetError('halves: points must sit on the left half, x 0..6 and y 0..8')
        s, ox, oy = 18, 12, 12
        dots = ''.join(f'<circle cx="{ox + x * s}" cy="{oy + y * s}" r="1.8" fill="#666"/>' for x in range(13) for y in range(9))
        half = ' '.join(f'{ox + x * s},{oy + y * s}' for x, y in pts)
        mirror = ' '.join(f'{ox + (12 - x) * s},{oy + y * s}' for x, y in pts)
        cells.append(f'<svg class="ws-half" viewBox="0 0 {24 + 12 * s} {24 + 8 * s}" aria-hidden="true">{dots}'
                     f'<line x1="{ox + 6 * s}" y1="2" x2="{ox + 6 * s}" y2="{22 + 8 * s}" stroke="#222" stroke-width="1.2" stroke-dasharray="6 4"/>'
                     f'<polyline points="{half}" fill="none" stroke="#222" stroke-width="2.4"/>'
                     f'<polyline class="ws-keyonly" points="{mirror}" fill="none" stroke="#c0392b" stroke-width="2.4"/></svg>')
    return f'<p class="ws-sub">{inline(a)}</p><div class="ws-halves">{"".join(cells)}</div>'


def b_comic(a, body, c):
    """comic: Strip title   then "- A: words" / "- B: words" speech lines for the first panels (one line per panel),
    then "* reply" (the reply that shows listening) and "- reply" options. The last panel is a box to glue a reply in;
    the replies go in a cut-out strip lettered across the whole sheet."""
    its = items(body)
    talk = [(m, t) for m, t in its if re.match(r'[AB]:', t)]
    replies = [(m, t) for m, t in its if not re.match(r'[AB]:', t)]
    if sum(m for m, _ in replies) != 1 or len(replies) < 2:
        raise SheetError(f'comic {a!r} needs 2 or more replies with exactly one *')
    c['comic'] = c.get('comic', 0) + 1
    panels = []
    for _, t in talk:
        who, words = t.split(':', 1)
        left = who == 'A'
        panels.append(f'<div class="ws-panel"><p class="ws-bubble-talk {"left" if left else "right"}">{inline(words.strip())}</p>'
                      f'{person(left)}</div>')
    panels.append('<div class="ws-panel ws-glue"><span>Glue the best reply here</span><span class="ws-keyonly ws-glue-key"></span></div>')
    letters = c.setdefault('reply_letters', [])
    order = list(range(len(replies)))
    c['rng'].shuffle(order)
    for i in order:
        letters.append((c['comic'], replies[i][0], replies[i][1]))
    right = next(i for i, (k, m, _) in enumerate(letters) if k == c['comic'] and m)
    c['answers'].append(ROMAN[right])
    glue = panels[-1].replace('<span class="ws-keyonly ws-glue-key"></span>', f'<span class="ws-keyonly ws-glue-key">{ROMAN[right]}</span>')
    panels[-1] = glue
    return f'<div class="ws-comic"><p class="ws-sub"><span class="ws-num">{c["comic"]}.</span> {inline(a)}</p><div class="ws-panels">{"".join(panels)}</div></div>'


def person(left):
    """A simple line-art kid for comic panels: one faces right (A), one faces left (B)."""
    hair = 'M30 30 q10 -14 22 -2' if left else 'M34 28 q8 -10 16 0 l2 6'
    return ('<svg class="ws-kid" viewBox="0 0 80 110" aria-hidden="true"><g fill="none" stroke="#222" stroke-width="2.4" '
            f'stroke-linecap="round"><circle cx="40" cy="34" r="16"/><path d="{hair}"/><path d="M40 50 v32 M40 60 l-14 14 M40 60 l14 14 '
            'M40 82 l-10 24 M40 82 l10 24"/><path d="M34 41 h12"/></g><circle cx="34" cy="31" r="2"/><circle cx="46" cy="31" r="2"/></svg>')


def b_replies(a, body, c):
    """replies:   (no body) the cut-out strip of every comic reply on the sheet, lettered"""
    cards = ''.join(f'<span class="ws-card ws-reply"><b>{ROMAN[i]}</b> {inline(t)}</span>' for i, (_, _, t) in enumerate(c.get('reply_letters', [])))
    return f'<div class="ws-cut"><p class="ws-tag">{inline(a or "Cut out the replies")}</p><div class="ws-cards">{cards}</div></div>'


def b_fixit(a, body, c):
    """fixit: 3(x - 2) = 12   a worked solution with one wrong step
      - step lines, in order (the first wrong one is marked with *)
      answer: 6   the right solution; the checker substitutes it into the equation"""
    d, rest = opts(body)
    steps = items(rest)
    wrong = [i for i, (m, _) in enumerate(steps) if m]
    if len(wrong) != 1:
        raise SheetError(f'fixit {a!r} needs exactly one * step')
    if not re.fullmatch(r'x\s*(=|<|>|<=|>=)\s*-?[\d/]+', d['answer']):
        raise SheetError(f'fixit {a!r}: answer must read like "x = 6" or "x < -3"')
    c['checks'].append(('equation', a, d['answer']))
    lis = ''.join(f'<li class="{"ws-wrong" if m else ""}">{inline(t)}</li>' for m, t in steps)
    return (f'<div class="ws-q ws-fixit"><p><span class="ws-num">{c["n"]}.</span> Solve <b>{esc(a)}</b></p><ol class="ws-steps">{lis}</ol>'
            f'<p class="ws-fixline">Wrong step: <span class="ws-blank" style="min-width:2em"><span class="ws-ans">{wrong[0] + 1}</span></span> '
            f'Correct answer: <span class="ws-blank" style="min-width:5em"><span class="ws-ans">{esc(d["answer"])}</span></span></p>'
            f'<p class="ws-explain">What went wrong?</p>{lines(1)}{key(d.get("why", ""))}</div>'), 1


def b_rate(a, body, c):
    """rate: I can ...   the check-yourself strip (one is added at the end of every sheet automatically)"""
    return rate(a)


def rate(text):
    return (f'<div class="ws-rate"><p><b>Check yourself:</b> {inline(text)}</p><p class="ws-rate-opts">'
            '<span>On my own</span><span>With a little help</span><span>Not yet</span></p></div>')


KINDS = {'text': b_text, 'example': b_example, 'fill': b_fill, 'choice': b_choice, 'write': b_write, 'lines': b_lines,
         'draw': b_draw, 'trace': b_trace, 'chain': b_chain, 'picword': b_picword, 'sort': b_sort, 'table': b_table,
         'graph': b_graph, 'passage': b_passage, 'source': b_source, 'colorcode': b_colorcode, 'binary': b_binary,
         'symmetry': b_symmetry, 'halves': b_halves, 'comic': b_comic, 'replies': b_replies, 'fixit': b_fixit, 'rate': b_rate}


def evaluate(expr, x=None):
    """A whole-number or fraction expression with + - * / ( ), 'x' or '×' for times, implicit products like 3(x - 2)."""
    e = expr.replace('×', '*').replace('−', '-').replace('÷', '/')
    e = re.sub(r'(?<=\d)\s*x\s*(?=\d)', '*', e) if x is None else e
    e = re.sub(r'(\d)\s*\(', r'\1*(', e)
    e = re.sub(r'(\d|\))\s*(x)\b', r'\1*\2', e)
    e = re.sub(r'\)\s*\(', ')*(', e)
    if not re.fullmatch(r'[\d\s+\-*/().x]+', e):
        raise SheetError(f'cannot evaluate {expr!r}')
    e = re.sub(r'(\d+)', r'Fraction(\1)', e)
    return eval(e, {'Fraction': Fraction, '__builtins__': {}}, {'x': x})


RELS = {'=': lambda a, b: a == b, '<': lambda a, b: a < b, '>': lambda a, b: a > b, '<=': lambda a, b: a <= b, '>=': lambda a, b: a >= b}


def check_equation(eq, answer):
    """True when answer ("x = 6", "x < -3") is exactly the solution set of eq, an equation or inequality in x."""
    rel = re.search(r'<=|>=|=|<|>', eq).group(0)
    lhs, rhs = eq.split(rel)
    op, val = re.fullmatch(r'x\s*(<=|>=|=|<|>)\s*(.+)', answer).groups()
    b = Fraction(val)
    f = lambda x: RELS[rel](evaluate(lhs, x), evaluate(rhs, x))
    if rel == '=':
        return op == '=' and f(b)
    # the boundary must make both sides equal, and each side of it must match the answer's direction
    edge = evaluate(lhs, b) == evaluate(rhs, b)
    return edge and all(f(x) == RELS[op](x, b) for x in (b - 1, b + 1, b)) 


# ---------- parsing ----------

def parse(text, unit):
    """-> [sheet dict]: n, title, head keys, parts [(name, [(kind, args, body)])]"""
    sheets, cur, part, block = [], None, None, None
    for ln, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if m := re.match(r'# (\d+)\. (.+)$', line):
            cur = dict(n=int(m.group(1)), title=m.group(2).strip(), parts=[], line=ln)
            sheets.append(cur)
            part = block = None
        elif cur is None or not line.strip():
            continue
        elif m := re.match(r'## (.+)$', line):
            part = (m.group(1).strip(), [])
            cur['parts'].append(part)
            block = None
        elif line.startswith('  ') and block is not None:
            block[2].append(line.strip())
        elif m := re.match(r'([a-z]+):\s*(.*)$', line):
            k, v = m.groups()
            if part is None:
                if k not in HEAD_KEYS:
                    raise SheetError(f'{unit} line {ln}: unknown header {k!r}')
                cur[k] = v
            else:
                if k not in KINDS:
                    raise SheetError(f'{unit} line {ln}: unknown block {k!r}')
                block = (k, v, [])
                part[1].append(block)
        else:
            raise SheetError(f'{unit} line {ln}: cannot read {line!r}')
    return sheets


def render(sheet, unit):
    """-> (student html with key-only parts marked, answers list, checks list, passage word counts)"""
    c = dict(rng=random.Random(f'{unit}/{sheet["n"]}'), answers=[], checks=[], words=[], passage_words=[], n=1)
    out = []
    for name, blocks in sheet['parts']:
        body = []
        for kind, args, lines_ in blocks:
            try:
                r = KINDS[kind](args, lines_, c)
            except SheetError as e:
                raise SheetError(f'{unit} #{sheet["n"]} {kind}: {e}')
            if isinstance(r, tuple):
                r, used = r
                c['n'] += used
            body.append(r)
        label = name.split(':', 1)
        head = f'<h2 class="ws-part"><span>{esc(label[0])}</span>{(" " + esc(label[1].strip())) if len(label) > 1 else ""}</h2>'
        out.append(f'<section class="ws-section">{head}{"".join(body)}</section>')
    out.append(rate(sheet['ican'].removeprefix('I can ').rstrip('.').join(['I can ', '.'])))
    return ''.join(out), c


def build(unit, sheet, row, label, module, tool_titles):
    """The fragment the viewer shows: student pages (key parts hidden unless the key is on) and the teacher page."""
    body, c = render(sheet, unit)
    head = (f'<header class="ws-head"><div class="ws-name"><span>Name</span><span>Date</span><span>Class</span></div>'
            f'<p class="ws-eyebrow">{esc(label)} · {esc(row["type"])}</p><h1>{esc(sheet["title"])}</h1>'
            f'<p class="ws-ican">{inline(sheet["ican"])}</p><p class="ws-directions"><b>Directions:</b> {inline(sheet["directions"])}</p></header>')
    foot = f'<p class="ws-foot">{esc(sheet["title"])} · Curio Class, curioclass.org/closet/worksheets/{esc(unit)}/ · free under CC BY 4.0</p>'
    codes = ', '.join(module.get('codes', [])) if module else ''
    pairs = sheet.get('pairs')
    teacher = [f'<p class="ws-eyebrow">Teacher page · answer key above</p><h2>{esc(sheet["title"])}</h2><dl class="ws-facts">',
               f'<dt>Class</dt><dd>{esc(label)}</dd>']
    if module:
        teacher.append(f'<dt>Module</dt><dd>{esc(module["title"])}{f" ({esc(codes)})" if codes else ""}</dd>')
    teacher.append(f'<dt>Time</dt><dd>{esc(sheet["minutes"])} minutes</dd><dt>Materials</dt><dd>{esc(sheet["materials"])}</dd>')
    if pairs:
        teacher.append(f'<dt>Goes with</dt><dd>{esc(tool_titles.get(pairs, pairs))} (curioclass.org/tools/{esc(pairs)}/)</dd>')
    teacher.append(f'<dt>Students</dt><dd>{esc(row["does"])}</dd></dl>')
    if sheet.get('mistakes'):
        teacher.append(f'<h3>Watch for</h3><p>{inline(sheet["mistakes"])}</p>')
    if sheet.get('notes'):
        teacher.append(f'<h3>Notes</h3><p>{inline(sheet["notes"])}</p>')
    html_ = (f'<article class="ws-sheet">{head}{body}{foot}</article>'
             f'<article class="ws-teacher">{"".join(teacher)}{foot}</article>')
    return html_, c


# ---------- checking ----------

def concept_rows(unit):
    """The unit's rows from docs/worksheets/<file>.md -> {n: dict(title, type, module, does)}"""
    import check_worksheets as cw
    U = cw.units()
    if unit not in U:
        raise SheetError(f'unknown unit {unit}')
    text = (cw.DIR / f'{U[unit]["file"]}.md').read_text()
    sec = re.search(rf'^## {re.escape(unit)}: .+?(?=^## |\Z)', text, re.M | re.S).group(0)
    rows = {}
    for m in re.finditer(r'^\|\s*(\d+)\s*\|(.+)\|\s*$', sec, re.M):
        title, kind, mod, does = (x.strip() for x in m.group(2).split('|'))
        rows[int(m.group(1))] = dict(title=title, type=kind, module=mod, does=does)
    return rows, U[unit]['label']


def load(unit):
    """-> (label, [(sheet, row)])  raising SheetError on a bad file"""
    sheets = parse((DIR / f'{unit}.md').read_text(), unit)
    rows, label = concept_rows(unit)
    out = []
    for s in sheets:
        if s['n'] not in rows:
            raise SheetError(f'{unit} #{s["n"]}: no such row in the concept list')
        if s['title'] != rows[s['n']]['title']:
            raise SheetError(f'{unit} #{s["n"]}: title {s["title"]!r} differs from the concept list {rows[s["n"]]["title"]!r}')
        missing = NEED - set(s)
        if missing:
            raise SheetError(f'{unit} #{s["n"]}: missing {sorted(missing)}')
        if not s['ican'].startswith('I can '):
            raise SheetError(f'{unit} #{s["n"]}: ican must start "I can "')
        out.append((s, rows[s['n']]))
    return label, out


PASSAGE = {'k': (30, 90), '1': (40, 90), '2': (40, 120), '3': (100, 260), '4': (120, 260), '5': (120, 280),
           '6': (200, 420), '7': (220, 420), '8': (220, 450)}


def problems(unit):
    out = []
    try:
        label, sheets = load(unit)
    except SheetError as e:
        return [str(e)]
    grade = re.search(r'-(k|\d+)$', unit)
    for s, row in sheets:
        try:
            html_, c = build(unit, s, row, label, None, {})
        except SheetError as e:
            out.append(str(e))
            continue
        except Exception as e:  # a malformed block: report it, don't crash the build
            out.append(f'{unit} #{s["n"]}: {type(e).__name__}: {e}')
            continue
        for kind, eq, ans in c['checks']:
            if kind == 'equation' and not check_equation(eq, ans):
                out.append(f'{unit} #{s["n"]}: x = {ans} does not solve {eq}')
        if not c['answers'] and 'ws-keyonly' not in html_:
            out.append(f'{unit} #{s["n"]}: no answer key at all')
        if grade and grade.group(1) in PASSAGE:
            lo, hi = PASSAGE[grade.group(1)]
            for w in c['passage_words']:
                if not lo <= w <= hi:
                    out.append(f'{unit} #{s["n"]}: passage of {w} words, want {lo}-{hi} for this grade')
    if '—' in (DIR / f'{unit}.md').read_text():
        out.append(f'{unit}: em dash')
    return out


def built_units():
    return sorted(p.stem for p in DIR.glob('*.md')) if DIR.exists() else []


def main(args):
    sys.path.insert(0, str(Path(__file__).parent))
    units = args or built_units()
    errs, n = [], 0
    for u in units:
        errs += problems(u)
        try:
            n += len(load(u)[1])
        except SheetError:
            pass
    for e in errs:
        print(e)
    print(f'{n} built worksheets in {len(units)} units checked, {len(errs)} problems')
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
