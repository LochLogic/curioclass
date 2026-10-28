r"""Draw the Word Wall's diagram pictures (the "svg:" cards, docs/SUPPLY-CLOSET-PLAN.md, Phase C) in code.

    python scripts/wordsvg.py                  draw every diagram that is missing
    python scripts/wordsvg.py --force          draw them all again
    python scripts/wordsvg.py --only <key>...  draw some (key = <module_id>/<slug>)
    python scripts/wordsvg.py --sheets [N]     contact sheets of the drawn diagrams in closet/words/art/_raw/ (from the Nth)
    python scripts/wordsvg.py --status         how many are drawn, how many have no spec

Image models cannot spell, count or plot, so a card whose picture is letters, numbers, a graph, a staff or a map is
drawn here from a spec in data/closet/words/diagrams.py (one line per card, built from the small parts below:
row(), col(), T() for text, F() for fractions, numberline(), plot(), staff(), icons...). A spec of paint('prompt')
hands the card to the image model instead (scripts/wordart.py), for plain objects it draws well.
Each spec becomes a 512 x 512 SVG; headless Chrome rasterizes a sheet of them at a time and the sheet is cut into
closet/words/art/<module_id>/<slug>.webp, the same file a painted picture would be.
"""
import json, math, re, subprocess, sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from charts import measure  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SIZE, PAD = 512, 34
DARK, GRAY, LIGHT = '#1f2430', '#8a8f9c', '#e6e8ee'
BLUE, ORANGE, GREEN, YELLOW, PURPLE, RED, TEAL, PINK, BROWN = (
    '#3a7bd5', '#f08a24', '#2f9e5b', '#f5c33b', '#8e5bc4', '#e04848', '#1d9a9a', '#f28bb3', '#a0673a')
SOFT = {BLUE: '#d6e6fb', ORANGE: '#fde3c8', GREEN: '#d3f0de', YELLOW: '#fdf0c4', PURPLE: '#e8dcf5', RED: '#f9d4d4',
        TEAL: '#cfeeee', PINK: '#fbe0ea', BROWN: '#efdccb', DARK: '#d9dbe2', GRAY: '#eceef2'}
SANS = "'Segoe UI', Arial, sans-serif"
MATHF = "'Cambria Math', Cambria, 'Segoe UI', serif"
SW = 5  # outline width


def soft(c):
    return SOFT.get(c, '#eef0f4')


# ---------- layout: an Item is a box of w x h with its SVG drawn from (0, 0) ----------

class Item:
    def __init__(self, w, h, svg):
        self.w, self.h, self.svg = w, h, svg


def g(item, x, y, k=1.0):
    t = f'translate({x:.1f} {y:.1f})' + (f' scale({k:.4f})' if k != 1 else '')
    return f'<g transform="{t}">{item.svg}</g>'


def it(x):
    """Strings and numbers become text."""
    return x if isinstance(x, Item) else T(str(x))


def row(*items, gap=26, align='c'):
    items = [it(i) for i in items if i is not None]
    w = sum(i.w for i in items) + gap * (len(items) - 1)
    h = max(i.h for i in items)
    out, x = [], 0
    for i in items:
        y = (h - i.h) / 2 if align == 'c' else (h - i.h if align == 'b' else 0)
        out.append(g(i, x, y))
        x += i.w + gap
    return Item(w, h, ''.join(out))


def col(*items, gap=22, align='c'):
    items = [it(i) for i in items if i is not None]
    w = max(i.w for i in items)
    h = sum(i.h for i in items) + gap * (len(items) - 1)
    out, y = [], 0
    for i in items:
        x = (w - i.w) / 2 if align == 'c' else 0
        out.append(g(i, x, y))
        y += i.h + gap
    return Item(w, h, ''.join(out))


def grid(items, cols, gap=18):
    items = [it(i) for i in items]
    rows = [items[k:k + cols] for k in range(0, len(items), cols)]
    return col(*[row(*r, gap=gap) for r in rows], gap=gap)


def over(base, top, dx=0, dy=0, k=1.0):
    """top drawn over the middle of base (moved by dx, dy; scaled by k)."""
    base, top = it(base), it(top)
    x, y = (base.w - top.w * k) / 2 + dx, (base.h - top.h * k) / 2 + dy
    return Item(base.w, base.h, base.svg + g(top, x, y, k))


def sized(item, w=None, h=None):
    """item scaled to a width or height."""
    item = it(item)
    k = min(w / item.w if w else 9e9, h / item.h if h else 9e9)
    return Item(item.w * k, item.h * k, g(item, 0, 0, k))


def pad(item, p=10):
    item = it(item)
    return Item(item.w + 2 * p, item.h + 2 * p, g(item, p, p))


def raw(w, h, svg):
    return Item(w, h, svg)


# ---------- text ----------

def tw(s, size, bold=False):
    return measure(s, size, bold)


def T(s, size=72, color=DARK, bold=True, hl=None, circle=None, box=None, strike=None, under=None, font=SANS, italic=False):
    """Text. hl: {substring: color} recolors; circle/box/strike/under: a substring (or list) to mark."""
    s = str(s)
    w = max(tw(s, size, bold), size * 0.4)
    h = size * 1.25
    base = size * 0.95
    marks = []
    spans, pos = [], 0
    hl = hl or {}
    if hl:
        pat = '|'.join(re.escape(k) for k in sorted(hl, key=len, reverse=True))
        for m in re.finditer(pat, s):
            spans.append((escape(s[pos:m.start()]), None))
            spans.append((escape(m[0]), hl[m[0]]))
            pos = m.end()
    spans.append((escape(s[pos:]), None))
    body = ''.join(f'<tspan fill="{c}">{t}</tspan>' if c else t for t, c in spans)

    def where(sub):
        i = s.find(sub)
        return tw(s[:i], size, bold), tw(sub, size, bold)
    for kind, subs in (('circle', circle), ('box', box), ('strike', strike), ('under', under)):
        for sub in ([subs] if isinstance(subs, str) else subs or []):
            x0, sw = where(sub)
            if kind == 'circle':
                marks.append(f'<ellipse cx="{x0 + sw / 2:.1f}" cy="{base - size * 0.36:.1f}" rx="{sw / 2 + size * 0.28:.1f}" ry="{size * 0.62:.1f}" fill="none" stroke="{RED}" stroke-width="{max(4, size / 14):.1f}"/>')
            elif kind == 'box':
                marks.append(f'<rect x="{x0 - size * 0.12:.1f}" y="{base - size * 0.92:.1f}" width="{sw + size * 0.24:.1f}" height="{size * 1.18:.1f}" rx="8" fill="none" stroke="{ORANGE}" stroke-width="{max(4, size / 14):.1f}"/>')
            elif kind == 'strike':
                marks.append(f'<line x1="{x0 - 6:.1f}" y1="{base - size * 0.1:.1f}" x2="{x0 + sw + 6:.1f}" y2="{base - size * 0.62:.1f}" stroke="{RED}" stroke-width="{max(5, size / 10):.1f}" stroke-linecap="round"/>')
            else:
                marks.append(f'<line x1="{x0:.1f}" y1="{base + size * 0.14:.1f}" x2="{x0 + sw:.1f}" y2="{base + size * 0.14:.1f}" stroke="{color}" stroke-width="{max(4, size / 12):.1f}"/>')
    pad_ = size * 0.35 if circle or box else 0
    txt = (f'<text x="{pad_:.1f}" y="{base + pad_ / 2:.1f}" font-family="{font}" font-size="{size:.1f}" fill="{color}"'
           f'{" font-weight=\"700\"" if bold else ""}{" font-style=\"italic\"" if italic else ""}>{body}</text>')
    marks = f'<g transform="translate({pad_:.1f} {pad_ / 2:.1f})">' + ''.join(marks) + '</g>'
    return Item(w + 2 * pad_, h + pad_, txt + marks)


OPS = set('=+−-×÷·<>≤≥≠≈→')


def M(s, size=72, **k):
    """Math text in a math font. An operator at either end gets room on that side, so it never runs into a fraction bar,
    a boxed term or a word next to it (the math font draws = + x wider than the measured width)."""
    t = T(s, size, font=MATHF, **k)
    s = str(s).strip()
    if not s:
        return t
    lead, trail = s[0] in OPS, s[-1] in OPS
    if not (lead or trail):
        return t
    pl, pr = (size * 0.26 if lead else 0), (size * 0.26 if trail else 0)
    return Item(t.w + pl + pr, t.h, g(t, pl, 0))


def F(n, d, size=64, color=DARK, hn=None, hd=None):
    """A stacked fraction; hn / hd recolor the numerator / denominator."""
    n, d = str(n), str(d)
    w = max(tw(n, size, True), tw(d, size, True)) * 1.08 + size * 0.3
    num = T(n, size, hn or color, font=MATHF)
    den = T(d, size, hd or color, font=MATHF)
    h = num.h + den.h + 8
    return Item(w, h, g(num, (w - num.w) / 2, 0) + f'<line x1="0" y1="{num.h + 2:.1f}" x2="{w:.1f}" y2="{num.h + 2:.1f}" stroke="{color}" stroke-width="{size / 14:.1f}"/>'
                + g(den, (w - den.w) / 2, num.h + 8))


def eq(*parts, size=64, gap=16):
    """A row of math: strings become math text (operators padded by M), tuples (n, d) become fractions."""
    return row(*[F(p[0], p[1], size) if isinstance(p, tuple) else (p if isinstance(p, Item) else M(p, size)) for p in parts], gap=max(gap, size * 0.22))


def mark(item, kind='circle', color=RED):
    """A ring or box drawn around any item."""
    item = it(item)
    p = 14
    w, h = item.w + 2 * p, item.h + 2 * p
    shape = (f'<ellipse cx="{w / 2:.1f}" cy="{h / 2:.1f}" rx="{w / 2 - 3:.1f}" ry="{h / 2 - 3:.1f}" fill="none" stroke="{color}" stroke-width="6"/>' if kind == 'circle'
             else f'<rect x="3" y="3" width="{w - 6:.1f}" height="{h - 6:.1f}" rx="12" fill="none" stroke="{color}" stroke-width="6"/>')
    return Item(w, h, g(item, p, p) + shape)


def hlbg(item, color=YELLOW):
    """A highlighter band behind an item."""
    item = it(item)
    return Item(item.w + 16, item.h, f'<rect x="0" y="{item.h * 0.12:.1f}" width="{item.w + 16:.1f}" height="{item.h * 0.8:.1f}" rx="8" fill="{soft(color) if color != YELLOW else "#fde97a"}"/>' + g(item, 8, 0))


def tile(s, color=BLUE, size=70, w=None, text=None, dashed=False, fill=None):
    """A letter or word tile."""
    s = str(s)
    tw_ = tw(s, size * 0.62, True)
    w = w or max(size, tw_ + size * 0.5)
    t = T(s, size * 0.62, text or DARK)
    return Item(w, size, f'<rect x="2.5" y="2.5" width="{w - 5:.1f}" height="{size - 5:.1f}" rx="{size * 0.16:.1f}" fill="{fill or soft(color)}" stroke="{color}" stroke-width="5"'
                f'{" stroke-dasharray=\"10 7\"" if dashed else ""}/>' + g(t, (w - t.w) / 2, (size - t.h) / 2 + 2))


def tiles(*ss, color=BLUE, size=70, gap=10, colors=None):
    return row(*[tile(s, (colors[i] if colors else color), size) for i, s in enumerate(ss)], gap=gap)


def card(content=None, w=150, h=190, color=BLUE, fill='#fff'):
    """A flash card (or picture card) holding an item."""
    out = f'<rect x="2.5" y="2.5" width="{w - 5}" height="{h - 5}" rx="16" fill="{fill}" stroke="{color}" stroke-width="5"/>'
    if content is not None:
        c = sized(content, w - 36, h - 36) if (it(content).w > w - 36 or it(content).h > h - 36) else it(content)
        out += g(c, (w - c.w) / 2, (h - c.h) / 2)
    return Item(w, h, out)


def label(item, s, size=30, color=DARK, above=False):
    s = T(s, size, color)
    return col(s, item, gap=8) if above else col(item, s, gap=8)


# ---------- arrows and lines ----------

def arrow(length=90, color=DARK, dir='right', sw=8, text=None, double=False, dashed=False):
    """A straight arrow (right, left, up, down, ur, dr) with an optional label above it."""
    ang = {'right': 0, 'left': 180, 'up': -90, 'down': 90, 'ur': -40, 'dr': 40, 'ul': -140, 'dl': 140}[dir] if isinstance(dir, str) else dir
    a = math.radians(ang)
    dx, dy = math.cos(a) * length, math.sin(a) * length
    w, h = abs(dx) + 30, abs(dy) + 30
    x0, y0 = (15 if dx >= 0 else w - 15), (15 if dy >= 0 else h - 15)
    x1, y1 = x0 + dx, y0 + dy
    hx, hy = math.cos(a), math.sin(a)
    hl_, hw = max(22, sw * 2.3), max(13, sw * 1.5)
    head = lambda x, y, ux, uy: (f'<path d="M{x:.1f} {y:.1f} L{x - ux * hl_ - uy * hw:.1f} {y - uy * hl_ + ux * hw:.1f} L{x - ux * hl_ + uy * hw:.1f} {y - uy * hl_ - ux * hw:.1f} z" fill="{color}"/>')
    svg = (f'<line x1="{x0 + (hx * 14 if double else 0):.1f}" y1="{y0 + (hy * 14 if double else 0):.1f}" x2="{x1 - hx * hl_ * 0.7:.1f}" y2="{y1 - hy * hl_ * 0.7:.1f}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"'
           f'{" stroke-dasharray=\"14 10\"" if dashed else ""}/>' + head(x1, y1, hx, hy) + (head(x0, y0, -hx, -hy) if double else ''))
    item = Item(w, h, svg)
    return col(T(text, 34, color), item, gap=0) if text else item


def harrows(color=DARK, length=80):
    """Two arrows, one each way (back and forth)."""
    return col(arrow(length, color), arrow(length, color, 'left'), gap=4)


def curve_arrow(r=60, color=DARK, start=-60, end=230, sw=8, cw=True, text=None, inner=None):
    """A circular arrow (a loop); inner is drawn in the middle."""
    a0, a1 = math.radians(start), math.radians(end)
    pts = [(r + 16 + r * math.cos(a0 + (a1 - a0) * t / 40), r + 16 + r * math.sin(a0 + (a1 - a0) * t / 40)) for t in range(41)]
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts[:-3])
    (x2, y2), (x1, y1) = pts[-1], pts[-4]
    ux, uy = x2 - x1, y2 - y1
    n = math.hypot(ux, uy) or 1
    ux, uy = ux / n, uy / n
    svg = (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
           f'<path d="M{x2 + ux * 8:.1f} {y2 + uy * 8:.1f} L{x2 - ux * 18 - uy * 14:.1f} {y2 - uy * 18 + ux * 14:.1f} L{x2 - ux * 18 + uy * 14:.1f} {y2 - uy * 18 - ux * 14:.1f} z" fill="{color}"/>')
    item = Item(2 * r + 32, 2 * r + 32, svg)
    if not cw:
        item = Item(item.w, item.h, f'<g transform="translate({item.w} 0) scale(-1 1)">{svg}</g>')
    if inner is not None:
        item = over(item, sized(inner, r * 1.1, r * 1.1))
    if text:
        item = over(item, T(text, r * 0.8, color))
    return item


def connect(a, b, gap=0, color=DARK, length=70, dir='right', text=None):
    return row(a, arrow(length, color, dir, text=text), b, gap=12)


def flow(*items, color=DARK, length=60, gap=10):
    """items joined by arrows in a row."""
    out = []
    for i, x in enumerate(items):
        if i:
            out.append(arrow(length, color))
        out.append(it(x))
    return row(*out, gap=gap)


def vflow(*items, color=DARK, length=40):
    out = []
    for i, x in enumerate(items):
        if i:
            out.append(arrow(length, color, 'down'))
        out.append(it(x))
    return col(*out, gap=6)


def box(content=None, w=None, h=None, color=BLUE, fill=None, rx=14, dashed=False, sw=5, p=22):
    c = it(content) if content is not None else None
    w = w or (c.w + 2 * p if c else 120)
    h = h or (c.h + 2 * p if c else 90)
    out = (f'<rect x="{sw / 2}" y="{sw / 2}" width="{w - sw:.1f}" height="{h - sw:.1f}" rx="{rx}" fill="{fill or soft(color)}" stroke="{color}" stroke-width="{sw}"'
           f'{" stroke-dasharray=\"12 8\"" if dashed else ""}/>')
    if c:
        out += g(c, (w - c.w) / 2, (h - c.h) / 2)
    return Item(w, h, out)


def boxes(*labels, color=BLUE, size=36, w=None, h=None, colors=None, arrows=False, vertical=False):
    bs = [box(T(l, size) if l != '' else None, w=w, h=h, color=(colors[i] if colors else color)) for i, l in enumerate(labels)]
    if arrows:
        return (vflow if vertical else flow)(*bs)
    return (col if vertical else row)(*bs, gap=16)


def cycle(labels, r=150, color=BLUE, size=30, icons=None, colors=None):
    """Labels (or items) on a ring joined by clockwise arrows."""
    n = len(labels)
    W = 2 * r + 200
    cx = cy = W / 2
    out = []
    for k in range(n):
        a0, a1 = 2 * math.pi * (k + 0.28) / n - math.pi / 2, 2 * math.pi * (k + 0.72) / n - math.pi / 2
        pts = [(cx + r * math.cos(a0 + (a1 - a0) * t / 20), cy + r * math.sin(a0 + (a1 - a0) * t / 20)) for t in range(21)]
        out.append('<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts[:-2]) + f'" fill="none" stroke="{DARK}" stroke-width="6"/>')
        (x2, y2), (x1, y1) = pts[-1], pts[-3]
        ux, uy = x2 - x1, y2 - y1
        nn = math.hypot(ux, uy) or 1
        ux, uy = ux / nn, uy / nn
        out.append(f'<path d="M{x2:.1f} {y2:.1f} L{x2 - ux * 18 - uy * 11:.1f} {y2 - uy * 18 + ux * 11:.1f} L{x2 - ux * 18 + uy * 11:.1f} {y2 - uy * 18 - ux * 11:.1f} z" fill="{DARK}"/>')
    for k, l in enumerate(labels):
        a = 2 * math.pi * k / n - math.pi / 2
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        c = colors[k] if colors else color
        node = sized(l, 120, 100) if isinstance(l, Item) else box(T(l, size), color=c, p=12)
        if isinstance(l, Item):
            node = Item(node.w, node.h, f'<circle cx="{node.w / 2:.1f}" cy="{node.h / 2:.1f}" r="{max(node.w, node.h) / 2 + 8:.1f}" fill="#fff"/>' + node.svg)
        out.append(g(node, x - node.w / 2, y - node.h / 2))
    return Item(W, W, ''.join(out))


def venn(n=2, labels=None, shade=None, color=(BLUE, ORANGE, GREEN), sep=False):
    """Two or three overlapping circles; shade: 'both', 'A', 'B', 'outside', 'Aonly'."""
    r = 110
    cs = [(150, 150), (290, 150)] if n == 2 else [(150, 140), (270, 140), (210, 240)]
    if sep:
        cs = [(130, 150), (370, 150)]
    W, H = (cs[-1][0] + r + 20 if n == 2 else 400), (300 if n == 2 else 380)
    out = []
    if shade == 'outside':
        out.append(f'<rect x="4" y="4" width="{W - 8}" height="{H - 8}" rx="14" fill="{soft(BLUE)}" stroke="{DARK}" stroke-width="4"/>')
        out.append(f'<circle cx="{cs[0][0]}" cy="{cs[0][1]}" r="{r}" fill="#fff" stroke="{DARK}" stroke-width="5"/>')
        return Item(W, H, ''.join(out) + (g(T(labels[0], 40), cs[0][0] - 14, cs[0][1] - 30) if labels else ''))
    out.append('<defs><clipPath id="vA"><circle cx="%s" cy="%s" r="%s"/></clipPath></defs>' % (cs[0][0], cs[0][1], r))
    for i, (x, y) in enumerate(cs):
        fill = soft(color[i]) if shade in (None, 'both') or shade == 'AB'[i] else '#fff'
        if shade == 'Aonly':
            fill = soft(color[i]) if i == 0 else '#fff'
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" fill-opacity="{0.85 if shade is None else 1}" stroke="{color[i]}" stroke-width="6"/>')
    if shade == 'both' and n == 2:
        out.append(f'<circle cx="{cs[1][0]}" cy="{cs[1][1]}" r="{r}" clip-path="url(#vA)" fill="{color[0]}" opacity="0.55"/>')
    if shade in ('A', 'B') or shade == 'Aonly':
        pass
    if n == 2 and not sep:
        out.append(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{color[i]}" stroke-width="6"/>' for i, (x, y) in enumerate(cs)))
    for i, l in enumerate(labels or []):
        t = T(l, 40, color[i])
        x, y = cs[i]
        x = x - t.w / 2 + (-40 if i == 0 and n == 2 and not sep else 40 if i == 1 and n == 2 and not sep else 0)
        out.append(g(t, x, y - t.h / 2))
    return Item(W, H, ''.join(out))


# ---------- icons (each drawn in its own box; size scales it) ----------

def _icon(w, h, svg, size):
    k = size / max(w, h)
    return Item(w * k, h * k, f'<g transform="scale({k:.4f})">{svg}</g>')


def star(size=90, color=YELLOW):
    pts = ' '.join(f'{50 + (46 if i % 2 == 0 else 20) * math.sin(math.pi * i / 5):.1f},{52 - (46 if i % 2 == 0 else 20) * math.cos(math.pi * i / 5):.1f}' for i in range(10))
    return _icon(100, 100, f'<polygon points="{pts}" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)


def heart(size=90, color=RED):
    return _icon(100, 92, f'<path d="M50 86 C20 64 4 46 4 28 C4 12 16 4 29 4 C39 4 46 10 50 18 C54 10 61 4 71 4 C84 4 96 12 96 28 C96 46 80 64 50 86 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)


def check(size=90, color=GREEN):
    return _icon(100, 100, f'<path d="M12 54 L40 82 L90 18" fill="none" stroke="{color}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>', size)


def cross(size=90, color=RED):
    return _icon(100, 100, f'<path d="M16 16 L84 84 M84 16 L16 84" stroke="{color}" stroke-width="16" stroke-linecap="round"/>', size)


def qmark(size=100, color=BLUE):
    return T('?', size, color)


def bang(size=100, color=ORANGE):
    return T('!', size, color)


def bulb(size=100, color=YELLOW):
    return _icon(80, 110, f'<path d="M40 4 C18 4 4 20 4 40 C4 56 14 64 22 74 L22 84 L58 84 L58 74 C66 64 76 56 76 40 C76 20 62 4 40 4 Z" fill="{color}" stroke="{DARK}" stroke-width="5"/>'
                 f'<rect x="24" y="84" width="32" height="18" rx="4" fill="#b8bcc6" stroke="{DARK}" stroke-width="5"/><path d="M30 60 L40 44 L50 60" fill="none" stroke="{DARK}" stroke-width="4"/>', size)


def magnifier(size=110, inner=None):
    svg = (f'<line x1="66" y1="66" x2="100" y2="100" stroke="{BROWN}" stroke-width="16" stroke-linecap="round"/>'
           f'<circle cx="42" cy="42" r="36" fill="#dff0ff" fill-opacity="0.8" stroke="{DARK}" stroke-width="7"/>')
    m = _icon(108, 108, svg, size)
    if inner is not None:
        m = over(m, sized(inner, size * 0.42, size * 0.42), dx=-size * 0.12, dy=-size * 0.12)
    return m


def key(size=110, color=YELLOW):
    return _icon(120, 60, f'<circle cx="28" cy="30" r="22" fill="{color}" stroke="{DARK}" stroke-width="5"/><circle cx="28" cy="30" r="8" fill="#fff" stroke="{DARK}" stroke-width="4"/>'
                 f'<path d="M50 24 H114 V36 H104 V48 H94 V36 H86 V46 H76 V36 H50 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)


def lock(size=100, color=YELLOW, open_=False):
    sh = 'M28 44 V28 C28 12 72 12 72 28 V30' if open_ else 'M28 44 V28 C28 8 72 8 72 28 V44'
    return _icon(100, 110, f'<path d="{sh}" fill="none" stroke="{DARK}" stroke-width="9"/><rect x="12" y="44" width="76" height="60" rx="10" fill="{color}" stroke="{DARK}" stroke-width="5"/>'
                 f'<circle cx="50" cy="68" r="8" fill="{DARK}"/><rect x="47" y="70" width="6" height="18" fill="{DARK}"/>', size)


def shield(size=120, color=BLUE, inner=None):
    s = _icon(100, 116, f'<path d="M50 4 L94 18 V54 C94 82 74 100 50 112 C26 100 6 82 6 54 V18 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)
    if inner is not None:
        s = over(s, sized(inner, size * 0.48, size * 0.48), dy=-size * 0.04)
    return s


def book(size=130, color=BLUE, open_=True, inner=None, hl=None):
    if open_:
        lines = ''.join(f'<line x1="{x0}" y1="{30 + i * 12}" x2="{x0 + 46}" y2="{30 + i * 12}" stroke="{GRAY}" stroke-width="4"/>' for x0 in (14, 70) for i in range(5))
        hls = ''.join(f'<rect x="{12 if p == 0 else 68}" y="16" width="52" height="70" fill="#fde97a" opacity="0.8"/>' for p in (hl or []))
        svg = (f'<path d="M4 14 Q32 6 62 14 Q90 6 120 14 V90 Q90 82 62 90 Q32 82 4 90 Z" fill="#fff" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>' + hls + lines
               + f'<line x1="62" y1="14" x2="62" y2="90" stroke="{DARK}" stroke-width="4"/><path d="M4 90 Q32 82 62 90 Q90 82 120 90 V98 Q90 90 62 98 Q32 90 4 98 Z" fill="{color}" stroke="{DARK}" stroke-width="4"/>')
        b = _icon(124, 100, svg, size)
    else:
        b = _icon(90, 116, f'<rect x="8" y="4" width="78" height="108" rx="6" fill="{color}" stroke="{DARK}" stroke-width="5"/><rect x="8" y="4" width="14" height="108" rx="4" fill="{DARK}" opacity="0.25"/>'
                  f'<rect x="32" y="22" width="44" height="12" rx="3" fill="#fff" opacity="0.85"/>', size)
    if inner is not None:
        b = over(b, sized(inner, size * 0.4, size * 0.4), dy=-size * 0.05)
    return b


def page(size=170, lines=7, hl=(), bold=(), boxed=(), indent=(), title=False, color=BLUE, cross=(), short=(), paras=None, pic=None, w_ratio=0.78, tags=None):
    """A page of text lines. hl/bold/boxed/indent/cross/short: line numbers (0-based); paras: blocks of lines."""
    W, H = 100 * w_ratio, 100
    out = [f'<rect x="3" y="3" width="{W - 6:.1f}" height="{H * 1.0 - 6:.1f}" rx="5" fill="#fff" stroke="{DARK}" stroke-width="4"/>']
    y = 14
    if title:
        out.append(f'<rect x="12" y="{y}" width="{W * 0.6:.1f}" height="9" rx="3" fill="{color}"/>')
        y += 18
    if pic:
        out.append(f'<rect x="12" y="{y}" width="{W - 24:.1f}" height="26" rx="3" fill="{soft(color)}" stroke="{color}" stroke-width="2"/>')
        y += 33
    blocks = paras or [lines]
    n = 0
    step = min(10, (H - y - 8) / (sum(blocks) + len(blocks) - 1)) if blocks else 10
    for b in blocks:
        top = y
        for i in range(b):
            x0 = 12 + (8 if n in indent else 0)
            x1 = W - 12 - (W * 0.32 if n in short or i == b - 1 and paras else 0)
            if n in hl:
                out.append(f'<rect x="{x0 - 3:.1f}" y="{y - 4:.1f}" width="{x1 - x0 + 6:.1f}" height="8" fill="#fde97a"/>')
            out.append(f'<line x1="{x0:.1f}" y1="{y:.1f}" x2="{x1:.1f}" y2="{y:.1f}" stroke="{DARK if n in bold else GRAY}" stroke-width="{5 if n in bold else 2.6}" stroke-linecap="round"/>')
            if n in cross:
                out.append(f'<line x1="{x0 - 4:.1f}" y1="{y - 5:.1f}" x2="{x1 + 4:.1f}" y2="{y + 5:.1f}" stroke="{RED}" stroke-width="3"/>')
            if n in boxed:
                out.append(f'<rect x="{x0 - 5:.1f}" y="{y - 6:.1f}" width="{x1 - x0 + 10:.1f}" height="12" rx="3" fill="none" stroke="{ORANGE}" stroke-width="2.5"/>')
            y += step
            n += 1
        if paras and ('p' + str(blocks.index(b))) in [str(t) for t in boxed]:
            pass
        y += step * 0.8
    return _icon(W, H, ''.join(out), size)


def para_page(size=180, paras=(3, 3, 3), box_para=(), hl_para=(), color=ORANGE, title=False, bold_first=False):
    """A page of paragraphs; box_para / hl_para: paragraph numbers to box or highlight."""
    W, H = 80, 100
    out = [f'<rect x="3" y="3" width="{W - 6}" height="{H - 6}" rx="5" fill="#fff" stroke="{DARK}" stroke-width="4"/>']
    y = 14
    if title:
        out.append(f'<rect x="12" y="{y - 4}" width="{W * 0.6:.1f}" height="9" rx="3" fill="{BLUE}"/>')
        y += 16
    step = min(8.5, (H - y - 6) / (sum(paras) + 0.9 * (len(paras) - 1) + 0.3))
    for p, n in enumerate(paras):
        top = y
        for i in range(n):
            x1 = W - 12 - (22 if i == n - 1 else 0)
            out.append(f'<line x1="{12 + (6 if i == 0 else 0)}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{DARK if (bold_first and p == 0 and i == 0) else GRAY}" stroke-width="{4.5 if (bold_first and p == 0 and i == 0) else 2.6}" stroke-linecap="round"/>')
            y += step
        if p in hl_para:
            out.insert(1, f'<rect x="8" y="{top - 5:.1f}" width="{W - 16}" height="{y - top:.1f}" fill="#fde97a"/>')
        if p in box_para:
            out.append(f'<rect x="7" y="{top - 6:.1f}" width="{W - 14}" height="{y - top + 2:.1f}" rx="3" fill="none" stroke="{color}" stroke-width="2.6"/>')
        y += step * 0.9
    return _icon(W, H, ''.join(out), size)


def screen(size=170, inner=None, laptop=False, color=BLUE, bar=False):
    if laptop:
        svg = (f'<rect x="14" y="4" width="112" height="76" rx="6" fill="#fff" stroke="{DARK}" stroke-width="5"/><path d="M2 84 H138 L128 96 H12 Z" fill="#c4c8d0" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>')
        s, (iw, ih, ix, iy) = _icon(140, 98, svg, size), (100, 64, 20, 10)
    else:
        svg = (f'<rect x="4" y="4" width="132" height="88" rx="8" fill="#fff" stroke="{DARK}" stroke-width="5"/>'
               f'<rect x="60" y="92" width="20" height="14" fill="#c4c8d0" stroke="{DARK}" stroke-width="4"/><rect x="36" y="104" width="68" height="8" rx="3" fill="#c4c8d0" stroke="{DARK}" stroke-width="4"/>')
        s, (iw, ih, ix, iy) = _icon(140, 114, svg, size), (116, 72, 12, 12)
    k = size / 140
    if bar:
        s = Item(s.w, s.h, s.svg + f'<rect x="{(ix + 2) * k:.1f}" y="{(iy) * k:.1f}" width="{(iw - 4) * k:.1f}" height="{10 * k:.1f}" fill="{LIGHT}"/>')
    if inner is not None:
        c = sized(inner, iw * k * 0.8, ih * k * 0.8)
        s = Item(s.w, s.h, s.svg + g(c, (ix + iw / 2) * k - c.w / 2, (iy + ih / 2 + (4 if bar else 0)) * k - c.h / 2))
    return s


def phone(size=170, inner=None, color=DARK):
    s = _icon(60, 110, f'<rect x="3" y="3" width="54" height="104" rx="9" fill="#fff" stroke="{color}" stroke-width="5"/><rect x="22" y="9" width="16" height="4" rx="2" fill="{GRAY}"/>', size)
    if inner is not None:
        k = size / 110
        c = sized(inner, 44 * k, 80 * k)
        s = Item(s.w, s.h, s.svg + g(c, 30 * k - c.w / 2, 56 * k - c.h / 2))
    return s


def bubble(inner=None, size=170, color=BLUE, tail='left', think=False, w=None, h=None, fill='#fff', crack=False):
    """A speech (or thought) bubble holding an item or text."""
    c = it(inner) if inner is not None else None
    if c is not None and not isinstance(inner, Item) and c.w > 200:
        c = sized(c, 200)
    W = w or max(size, (c.w + 50) if c else size)
    Hh = h or max(size * 0.65, (c.h + 40) if c else size * 0.65)
    tx = W * 0.25 if tail == 'left' else W * 0.75
    if think:
        svg = (f'<ellipse cx="{W / 2:.1f}" cy="{Hh / 2:.1f}" rx="{W / 2 - 4:.1f}" ry="{Hh / 2 - 4:.1f}" fill="{fill}" stroke="{color}" stroke-width="5"/>'
               f'<circle cx="{tx:.1f}" cy="{Hh + 10:.1f}" r="9" fill="{fill}" stroke="{color}" stroke-width="4"/><circle cx="{tx - (12 if tail == "left" else -12):.1f}" cy="{Hh + 28:.1f}" r="5" fill="{fill}" stroke="{color}" stroke-width="4"/>')
    else:
        d = 1 if tail == 'left' else -1
        svg = (f'<path d="M{tx - d * 4:.1f} {Hh - 6:.1f} L{tx - d * 26:.1f} {Hh + 30:.1f} L{tx + d * 26:.1f} {Hh - 6:.1f}" fill="{fill}" stroke="{color}" stroke-width="5" stroke-linejoin="round"/>'
               f'<rect x="3" y="3" width="{W - 6:.1f}" height="{Hh - 6:.1f}" rx="{min(36, Hh / 2.5):.1f}" fill="{fill}" stroke="{color}" stroke-width="5"/>'
               f'<rect x="{tx - 22:.1f}" y="{Hh - 12:.1f}" width="40" height="9" fill="{fill}"/>')
    if crack:
        svg += f'<path d="M{W * 0.55:.1f} 3 L{W * 0.48:.1f} {Hh * 0.35:.1f} L{W * 0.58:.1f} {Hh * 0.55:.1f} L{W * 0.5:.1f} {Hh - 3:.1f}" fill="none" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
    if c is not None:
        svg += g(c, (W - c.w) / 2, (Hh - c.h) / 2)
    return Item(W, Hh + 34, svg)


def cloud(size=140, color='#fff', stroke=DARK, inner=None):
    c = _icon(120, 74, f'<path d="M26 70 C8 70 2 56 8 46 C2 32 18 20 32 26 C36 8 62 2 74 18 C88 8 108 18 104 34 C118 38 120 62 102 70 Z" fill="{color}" stroke="{stroke}" stroke-width="5" stroke-linejoin="round"/>', size)
    if inner is not None:
        c = over(c, sized(inner, size * 0.55, size * 0.3), dy=size * 0.05)
    return c


def raincloud(size=150, color='#c9ced8', drops=6):
    c = cloud(size, color)
    k = size / 120
    ds = ''.join(f'<path d="M{(22 + i * 15) * k:.1f} {80 * k:.1f} q-{4 * k:.1f} {9 * k:.1f} 0 {12 * k:.1f} q{4 * k:.1f} -{3 * k:.1f} 0 -{12 * k:.1f}z" fill="{BLUE}" transform="translate(0 {(i % 2) * 8 * k:.1f})"/>' for i in range(drops))
    return Item(c.w, c.h + 26 * k, c.svg + ds)


def sun(size=120, color=YELLOW):
    rays = ''.join(f'<line x1="{50 + 30 * math.cos(a):.1f}" y1="{50 + 30 * math.sin(a):.1f}" x2="{50 + 46 * math.cos(a):.1f}" y2="{50 + 46 * math.sin(a):.1f}" stroke="{ORANGE}" stroke-width="6" stroke-linecap="round"/>' for a in [k * math.pi / 4 for k in range(8)])
    return _icon(100, 100, rays + f'<circle cx="50" cy="50" r="24" fill="{color}" stroke="{DARK}" stroke-width="5"/>', size)


def moon(size=100, phase=None):
    """A crescent, or a phase 0..7 (0 new, 4 full)."""
    if phase is None:
        return _icon(100, 100, f'<path d="M62 8 A44 44 0 1 0 92 70 A34 34 0 1 1 62 8 Z" fill="{YELLOW}" stroke="{DARK}" stroke-width="5"/>', size)
    f = phase / 8
    lit = math.cos(2 * math.pi * f)  # 1 new .. -1 full
    rx = abs(lit) * 40
    right = f < 0.5
    sweep_outer = 1 if right else 0
    inner_sweep = (1 if lit < 0 else 0) if right else (0 if lit < 0 else 1)
    d = f'M50 10 A40 40 0 0 {sweep_outer} 50 90 A{rx:.1f} 40 0 0 {inner_sweep} 50 10 Z'
    lit_path = '' if phase == 0 else (f'<circle cx="50" cy="50" r="40" fill="{YELLOW}"/>' if phase == 4 else f'<path d="{d}" fill="{YELLOW}"/>')
    return _icon(100, 100, f'<circle cx="50" cy="50" r="40" fill="#3b4256"/>' + lit_path + f'<circle cx="50" cy="50" r="40" fill="none" stroke="{DARK}" stroke-width="4"/>', size)


def tree(size=140, color=GREEN):
    return _icon(100, 130, f'<rect x="42" y="78" width="16" height="48" fill="{BROWN}" stroke="{DARK}" stroke-width="5"/><circle cx="50" cy="50" r="42" fill="{color}" stroke="{DARK}" stroke-width="5"/>', size)


def pine(size=140, color=GREEN):
    return _icon(80, 120, f'<rect x="33" y="92" width="14" height="26" fill="{BROWN}" stroke="{DARK}" stroke-width="5"/><path d="M40 4 L76 94 H4 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)


def house(size=140, color=RED, inner=None, door=True):
    h = _icon(100, 100, f'<path d="M8 48 L50 8 L92 48" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/><rect x="18" y="44" width="64" height="52" fill="#fff" stroke="{DARK}" stroke-width="5"/>'
              + (f'<rect x="42" y="66" width="18" height="30" fill="{BROWN}" stroke="{DARK}" stroke-width="4"/>' if door and inner is None else ''), size)
    if inner is not None:
        h = over(h, sized(inner, size * 0.36, size * 0.3), dy=size * 0.17)
    return h


def door(size=140, color=BROWN, sign=None):
    d = _icon(70, 110, f'<rect x="6" y="4" width="58" height="104" rx="3" fill="{color}" stroke="{DARK}" stroke-width="5"/><circle cx="50" cy="58" r="5" fill="{YELLOW}" stroke="{DARK}" stroke-width="3"/>', size)
    if sign is not None:
        d = over(d, sized(sign, size * 0.35, size * 0.35), dy=-size * 0.15)
    return d


def flag(size=120, color=RED, white=False):
    return _icon(90, 110, f'<line x1="10" y1="6" x2="10" y2="106" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/>'
                 f'<path d="M12 10 C34 0 52 20 84 10 V52 C52 62 34 42 12 52 Z" fill="{"#fff" if white else color}" stroke="{DARK}" stroke-width="5"/>', size)


def gear(size=110, color=GRAY):
    teeth = ''.join(f'<rect x="43" y="2" width="14" height="18" rx="2" fill="{color}" stroke="{DARK}" stroke-width="4" transform="rotate({a} 50 50)"/>' for a in range(0, 360, 45))
    return _icon(100, 100, teeth + f'<circle cx="50" cy="50" r="34" fill="{color}" stroke="{DARK}" stroke-width="5"/><circle cx="50" cy="50" r="12" fill="#fff" stroke="{DARK}" stroke-width="4"/>', size)


def chain(n=3, size=200, broken=None, color=GRAY):
    out = []
    for i in range(n):
        x = 10 + i * 46
        if broken == i:
            out.append(f'<path d="M{x + 26} 12 H{x + 18} A18 18 0 0 0 {x + 18} 48 H{x + 26}" fill="none" stroke="{color}" stroke-width="10" stroke-linecap="round"/>'
                       f'<path d="M{x + 40} 12 H{x + 48} A18 18 0 0 1 {x + 48} 48 H{x + 40}" fill="none" stroke="{color}" stroke-width="10" stroke-linecap="round"/>'
                       f'<path d="M{x + 33} 6 L{x + 29} 22 L{x + 37} 32 L{x + 31} 54" fill="none" stroke="{RED}" stroke-width="4"/>')
        else:
            out.append(f'<rect x="{x}" y="{12 if i % 2 == 0 else 20}" width="66" height="{36 if i % 2 == 0 else 20}" rx="{18 if i % 2 == 0 else 10}" fill="none" stroke="{color}" stroke-width="10"/>')
            out.append(f'<rect x="{x}" y="{12 if i % 2 == 0 else 20}" width="66" height="{36 if i % 2 == 0 else 20}" rx="{18 if i % 2 == 0 else 10}" fill="none" stroke="{DARK}" stroke-width="2" opacity="0.5"/>')
    return _icon(20 + (n - 1) * 46 + 66, 60, ''.join(out), size)


def puzzle(size=140, color=BLUE, color2=ORANGE, fits=True, apart=False):
    p1 = f'<path d="M4 20 H40 C34 6 58 6 52 20 H70 V82 H4 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
    if fits:
        p2 = f'<path d="M70 20 H130 V82 H70 V62 C84 66 84 40 70 44 Z" fill="{color2}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
        p1 = f'<path d="M4 20 H70 V44 C84 40 84 66 70 62 V82 H4 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
        tx = 16 if apart else 0
        return _icon(134 + tx, 86, p1 + f'<g transform="translate({tx} 0)">{p2}</g>', size)
    p1 = f'<path d="M4 20 H60 V44 C74 40 74 66 60 62 V82 H4 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
    p2 = f'<path d="M80 20 H140 V82 H80 V44 L94 38 L94 68 L80 62 Z" fill="{color2}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round" transform="rotate(12 110 50)"/>'
    return _icon(146, 96, p1 + p2, size)


def target(size=140, arrow_=True, off=0):
    rings = ''.join(f'<circle cx="50" cy="50" r="{r}" fill="{c}" stroke="{DARK}" stroke-width="3"/>' for r, c in ((46, RED), (34, '#fff'), (22, RED), (10, '#fff')))
    ar = (f'<line x1="{50 + off}" y1="{50 - off}" x2="{94 + off}" y2="{6 - off}" stroke="{DARK}" stroke-width="5"/><path d="M{88 + off} {2 - off} l10 -2 l-2 10 z M{86 + off} {14 - off} l-6 -6" fill="{YELLOW}" stroke="{DARK}" stroke-width="3"/>'
          f'<circle cx="{50 + off}" cy="{50 - off}" r="4" fill="{DARK}"/>') if arrow_ else ''
    return _icon(104, 104, rings + ar, size)


def trophy(size=120, color=YELLOW):
    return _icon(100, 110, f'<path d="M28 10 H72 V40 C72 58 62 66 50 66 C38 66 28 58 28 40 Z" fill="{color}" stroke="{DARK}" stroke-width="5"/><path d="M28 18 H12 C10 36 20 44 30 44 M72 18 H88 C90 36 80 44 70 44" fill="none" stroke="{DARK}" stroke-width="5"/>'
                 f'<rect x="44" y="66" width="12" height="18" fill="{color}" stroke="{DARK}" stroke-width="4"/><rect x="28" y="84" width="44" height="18" rx="3" fill="{BROWN}" stroke="{DARK}" stroke-width="5"/>', size)


def footprint(size=70, color=DARK, angle=0):
    toes = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>' for x, y, r in ((14, 14, 7), (26, 8, 6), (37, 9, 5.5), (46, 14, 5), (52, 22, 4.5)))
    return _icon(64, 100, f'<g transform="rotate({angle} 32 50)">{toes}<path d="M18 30 C40 24 58 34 52 60 C48 80 46 96 30 96 C16 96 14 80 14 64 C14 50 8 34 18 30 Z" fill="{color}"/></g>', size)


def footprints(n=4, size=70, color=DARK, numbered=False, path='row'):
    items = []
    for i in range(n):
        f = footprint(size, color)
        if i % 2:
            f = Item(f.w, f.h, f'<g transform="translate({f.w} 0) scale(-1 1)">{f.svg}</g>')
        if numbered:
            f = col(f, T(i + 1, size * 0.4), gap=4)
        items.append(f)
    out = []
    for i, f in enumerate(items):
        out.append(g(f, i * size * 0.75, (0 if i % 2 else size * 0.5)))
    return Item(size * 0.75 * (n - 1) + items[0].w, items[0].h + size * 0.5, ''.join(out))


def ear(size=120, waves=True):
    e = _icon(80, 110, f'<path d="M20 50 C14 20 40 4 58 10 C78 16 80 42 68 58 C60 68 56 74 58 88 C60 104 40 108 32 96" fill="#f6d6bd" stroke="{DARK}" stroke-width="6" stroke-linecap="round"/>'
              f'<path d="M36 50 C34 34 46 26 56 32 C64 38 58 50 52 54" fill="none" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>', size)
    if waves:
        k = size / 110
        wv = ''.join(f'<path d="M{(84 + i * 14) * k:.1f} {(36 - i * 8) * k:.1f} Q{(98 + i * 16) * k:.1f} {55 * k:.1f} {(84 + i * 14) * k:.1f} {(74 + i * 8) * k:.1f}" fill="none" stroke="{BLUE}" stroke-width="6" stroke-linecap="round"/>' for i in range(3))
        e = Item(e.w + 50 * k, e.h, e.svg + wv)
    return e


def eye(size=120, pupil=0.32, color=BLUE, look=0):
    return _icon(120, 70, f'<path d="M4 35 C30 0 90 0 116 35 C90 70 30 70 4 35 Z" fill="#fff" stroke="{DARK}" stroke-width="5"/>'
                 f'<circle cx="{60 + look}" cy="35" r="22" fill="{color}" stroke="{DARK}" stroke-width="4"/><circle cx="{60 + look}" cy="35" r="{22 * pupil * 1.9:.1f}" fill="{DARK}"/><circle cx="{66 + look}" cy="29" r="4" fill="#fff"/>', size)


SKIN = '#f9d77e'  # a neutral cartoon hand color (no one skin tone)


def _fingers(spec, st, fill):
    """Fingers as separate rounded rods: spec = [(x, top, bottom, width)]; each joins the palm with no seam."""
    out = ''.join(f'<rect x="{x:.1f}" y="{t:.1f}" width="{w:.1f}" height="{b - t:.1f}" rx="{w / 2:.1f}" {st}/>' for x, t, b, w in spec)
    return out


def hand(size=150, kind='open', color=None, hl=False):
    """A cartoon hand with separate fingers and a thumb, palm toward the viewer.
    kind: open (fingers spread), flat (fingers together, thumb across the palm: ASL B), fist (thumb across the fingers: ASL S),
    a (fist, thumb up the side: ASL A), point (index up), l (index up, thumb out: ASL L), c (curved hand: ASL C)."""
    fill = soft(YELLOW) if hl else (color or SKIN)
    st = f'fill="{fill}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"'
    pf = f'fill="{fill}"'
    crease = lambda x1, y1, x2, y2: f'<path d="M{x1} {y1} Q{(x1 + x2) / 2} {max(y1, y2) + 3} {x2} {y2}" fill="none" stroke="{DARK}" stroke-width="2.5" stroke-linecap="round"/>'
    palm = f'<path d="M24 56 H80 V92 C80 104 72 112 64 116 V124 H40 V116 C30 112 24 104 24 92 Z" {st}/>'
    if kind == 'c':
        tube = lambda d, w, c: f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
        top, low = 'M70 34 C50 6 14 14 14 48', 'M70 90 C52 104 28 98 24 80'
        svg = (tube(top, 27, DARK) + tube(low, 25, DARK)
               + f'<path d="M62 26 H84 C92 26 94 34 94 42 V96 C94 104 90 110 84 112 V124 H58 V108 C56 100 56 92 58 84 Z" {st}/>'
               + tube(top, 17, fill) + tube(low, 15, fill)
               + ''.join(f'<path d="M{x} {y} l9 -5" stroke="{DARK}" stroke-width="2.5" stroke-linecap="round"/>' for x, y in ((14, 40), (20, 28))))
        return _icon(100, 128, svg, size)
    if kind in ('fist', 'a'):
        knuckles = _fingers([(24 + i * 14, 40, 70, 14) for i in range(4)], st, fill)
        cover = f'<rect x="26.5" y="62.5" width="51" height="10" {pf}/>'
        if kind == 'fist':
            thumb = f'<rect x="20" y="64" width="50" height="16" rx="8" {st}/>'
        else:
            thumb = f'<rect x="12" y="40" width="16" height="44" rx="8" {st}/>'
        svg = palm.replace('M24 56', 'M24 60') + knuckles + cover + thumb
        return _icon(100, 128, svg, size)
    if kind == '3':
        curled = _fingers([(52 + i * 14, 46, 68, 14) for i in range(2)], st, fill)
        up = _fingers([(24, 6, 68, 14), (38, 2, 68, 14)], st, fill)
        cover = f'<rect x="26.5" y="58.5" width="51" height="12" {pf}/>'
        thumb = f'<g transform="rotate(-50 26 86)"><rect x="18" y="44" width="16" height="44" rx="8" {st}/></g>'
        return _icon(100, 128, thumb + palm + curled + up + cover, size)
    if kind in ('point', 'l'):
        curled = _fingers([(38 + i * 14, 46, 68, 14) for i in range(3)], st, fill)
        index = _fingers([(24, 6, 68, 14)], st, fill)
        cover = f'<rect x="26.5" y="58.5" width="51" height="12" {pf}/>'
        thumb = (f'<rect x="-14" y="62" width="44" height="16" rx="8" {st}/>' if kind == 'l'
                 else f'<rect x="30" y="66" width="44" height="15" rx="7.5" {st}/>')
        svg = (thumb if kind == 'l' else '') + palm + curled + index + cover + (thumb if kind != 'l' else '')
        if kind == 'l':
            return _icon(118, 128, f'<g transform="translate(18 0)">{svg}</g>', size)
        return _icon(100, 128, svg, size)
    if kind == 'flat':
        fing = _fingers([(24 + i * 14, t, 66, 14) for i, t in enumerate((16, 8, 12, 22))], st, fill)
        cover = f'<rect x="26.5" y="58.5" width="51" height="10" {pf}/>'
        thumb = f'<g transform="rotate(-24 34 92)"><rect x="18" y="80" width="46" height="16" rx="8" {st}/></g>'
        svg = palm + fing + cover + thumb
        return _icon(100, 128, svg, size)
    # open: fingers spread, thumb out to the side
    spec = [(19, 18, 66, 14), (35.5, 8, 66, 14), (52, 12, 66, 14), (68, 26, 68, 13)]
    fing = ''.join(f'<g transform="rotate({r} {x + w / 2:.1f} 66)"><rect x="{x:.1f}" y="{t}" width="{w}" height="{b - t}" rx="{w / 2}" {st}/></g>'
                   for (x, t, b, w), r in zip(spec, (-10, -3, 4, 12)))
    thumb = f'<g transform="rotate(-48 26 86)"><rect x="18" y="44" width="16" height="44" rx="8" {st}/></g>'
    cover = f'<rect x="26.5" y="58.5" width="51" height="12" {pf}/>'
    svg = thumb + palm + fing + cover
    return _icon(100, 128, svg, size)


def wave_hand(size=150):
    h = hand(size)
    k = h.h / 128
    lines = ''.join(f'<path d="M{x * k:.1f} {y * k:.1f} q{-8 * k:.1f} {14 * k:.1f} 0 {28 * k:.1f}" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>' for x, y in ((-4, 20), (-16, 14)))
    lines += ''.join(f'<path d="M{x * k:.1f} {y * k:.1f} q{8 * k:.1f} {14 * k:.1f} 0 {28 * k:.1f}" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>' for x, y in ((102, 20), (114, 14)))
    return Item(h.w, h.h, f'<g transform="rotate(-12 {h.w / 2:.1f} {h.h / 2:.1f})">{h.svg}</g>' + lines)


def face(size=110, mood='happy', color=YELLOW, brows=None, outline=False):
    mouths = {'happy': 'M30 62 Q50 82 70 62', 'sad': 'M30 74 Q50 56 70 74', 'flat': 'M32 68 H68', 'o': None, 'big': 'M28 58 Q50 92 72 58 Z',
              'angry': 'M32 72 Q50 62 68 72', 'tired': 'M36 70 Q50 64 64 70', 'proud': 'M30 60 Q50 80 70 60', 'scared': None, 'calm': 'M34 64 Q50 74 66 64', 'wink': 'M30 62 Q50 82 70 62'}
    fill = '#fff' if outline else color
    svg = f'<circle cx="50" cy="50" r="44" fill="{fill}" stroke="{DARK}" stroke-width="5"/>'
    if mood == 'tired':
        svg += f'<path d="M28 42 Q36 48 44 42 M56 42 Q64 48 72 42" fill="none" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>'
    elif mood == 'wink':
        svg += f'<circle cx="36" cy="40" r="6" fill="{DARK}"/><path d="M56 41 Q64 34 72 41" fill="none" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>'
    elif mood in ('calm',):
        svg += f'<path d="M28 42 Q36 36 44 42 M56 42 Q64 36 72 42" fill="none" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>'
    else:
        svg += f'<circle cx="36" cy="40" r="{7 if mood == "scared" else 6}" fill="{DARK}"/><circle cx="64" cy="40" r="{7 if mood == "scared" else 6}" fill="{DARK}"/>'
    if mood in ('o', 'scared'):
        svg += f'<ellipse cx="50" cy="68" rx="9" ry="12" fill="{DARK}"/>'
    else:
        m = mouths.get(mood, mouths['happy'])
        svg += f'<path d="{m}" fill="{"#fff" if mood == "big" else "none"}" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>'
    b = brows or ('angry' if mood == 'angry' else 'up' if mood == 'scared' else None)
    if b == 'angry' or b == 'down':
        svg += f'<path d="M26 26 L44 32 M74 26 L56 32" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>'
    elif b == 'up':
        svg += f'<path d="M26 26 Q35 16 44 24 M56 24 Q65 16 74 26" fill="none" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>'
    return _icon(100, 100, svg, size)


def faces(*moods, size=100):
    return row(*[face(size, m) for m in moods], gap=18)


def head_outline(size=150, dot=None, brows=None, tilt=0, motion=False):
    """A simple head and shoulders outline (signed language cards): dot at 'chin', 'forehead', 'cheek'."""
    svg = (f'<g transform="rotate({tilt} 60 60)"><ellipse cx="60" cy="52" rx="34" ry="42" fill="#fff" stroke="{DARK}" stroke-width="5"/>'
           f'<circle cx="47" cy="50" r="4" fill="{DARK}"/><circle cx="73" cy="50" r="4" fill="{DARK}"/><path d="M50 74 Q60 80 70 74" fill="none" stroke="{DARK}" stroke-width="4" stroke-linecap="round"/>')
    if brows == 'up':
        svg += f'<path d="M38 36 Q47 26 55 34 M65 34 Q73 26 82 36" fill="none" stroke="{DARK}" stroke-width="4.5" stroke-linecap="round"/>'
    elif brows == 'down':
        svg += f'<path d="M38 36 L55 42 M82 36 L65 42" stroke="{DARK}" stroke-width="4.5" stroke-linecap="round"/>'
    svg += '</g>'
    svg += f'<path d="M10 140 C14 108 34 100 60 100 C86 100 106 108 110 140" fill="#fff" stroke="{DARK}" stroke-width="5"/>'
    pos = {'chin': (60, 92), 'forehead': (60, 22), 'cheek': (84, 64)}
    if dot:
        x, y = pos[dot]
        svg += f'<circle cx="{x}" cy="{y}" r="9" fill="{RED}"/>'
    if motion:
        svg += f'<path d="M4 40 q-6 12 0 24 M116 40 q6 12 0 24" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>'
    return _icon(120, 142, svg, size)


def apple(size=60, color=RED):
    return _icon(60, 64, f'<path d="M30 16 C18 8 4 14 4 32 C4 50 16 62 30 58 C44 62 56 50 56 32 C56 14 42 8 30 16 Z" fill="{color}" stroke="{DARK}" stroke-width="4"/>'
                 f'<path d="M30 16 C30 10 32 6 36 3" fill="none" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/><path d="M34 10 C40 2 50 4 50 6 C46 12 38 12 34 10 Z" fill="{GREEN}"/>', size)


def banana(size=60):
    return _icon(70, 50, f'<path d="M6 10 C10 40 40 52 66 30 C46 38 22 32 14 8 Z" fill="{YELLOW}" stroke="{DARK}" stroke-width="4" stroke-linejoin="round"/>', size)


def dot(size=40, color=BLUE, fill=None, outline=True):
    return _icon(40, 40, f'<circle cx="20" cy="20" r="16" fill="{fill or color}" stroke="{DARK if outline else fill or color}" stroke-width="3"/>', size)


def cube_icon(size=40, color=GREEN):
    return _icon(40, 40, f'<rect x="3" y="3" width="34" height="34" rx="4" fill="{color}" stroke="{DARK}" stroke-width="3"/>', size)


def duck(size=60):
    return _icon(70, 56, f'<path d="M8 30 C8 44 22 52 40 52 C58 52 64 40 60 30 C52 34 44 32 40 26 C46 8 30 2 22 10 C16 16 18 24 22 28 C14 26 8 26 8 30 Z" fill="{YELLOW}" stroke="{DARK}" stroke-width="4"/>'
                 f'<path d="M22 14 L8 16 L20 20" fill="{ORANGE}" stroke="{DARK}" stroke-width="3"/><circle cx="28" cy="13" r="2.5" fill="{DARK}"/>', size)


def balloon(size=60, color=RED):
    return _icon(40, 80, f'<ellipse cx="20" cy="22" rx="17" ry="20" fill="{color}" stroke="{DARK}" stroke-width="3.5"/><path d="M17 42 h6 l-3 4 z" fill="{color}"/><path d="M20 46 q-6 10 0 18 q6 8 0 14" fill="none" stroke="{DARK}" stroke-width="2"/>', size)


def cookie(size=50):
    return _icon(50, 50, f'<circle cx="25" cy="25" r="21" fill="#e2b06a" stroke="{DARK}" stroke-width="3.5"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="{BROWN}"/>' for x, y in ((18, 16), (30, 20), (22, 32), (34, 32))), size)


def car(size=70, color=RED):
    return _icon(80, 44, f'<path d="M6 30 V22 L18 20 L26 8 H54 L64 20 L74 22 V30 Z" fill="{color}" stroke="{DARK}" stroke-width="4" stroke-linejoin="round"/><circle cx="22" cy="32" r="8" fill="{DARK}"/><circle cx="58" cy="32" r="8" fill="{DARK}"/>'
                 f'<path d="M30 12 H40 V20 H24 Z M44 12 H52 L58 20 H44 Z" fill="#dff0ff"/>', size)


def bear(size=60):
    return _icon(60, 56, f'<circle cx="12" cy="12" r="9" fill="{BROWN}" stroke="{DARK}" stroke-width="3"/><circle cx="48" cy="12" r="9" fill="{BROWN}" stroke="{DARK}" stroke-width="3"/><circle cx="30" cy="30" r="22" fill="{BROWN}" stroke="{DARK}" stroke-width="3.5"/>'
                 f'<ellipse cx="30" cy="38" rx="9" ry="7" fill="#e8c9a6"/><circle cx="22" cy="26" r="2.6" fill="{DARK}"/><circle cx="38" cy="26" r="2.6" fill="{DARK}"/><circle cx="30" cy="35" r="3" fill="{DARK}"/>', size)


def bird(size=60, color=BLUE):
    return _icon(64, 50, f'<ellipse cx="30" cy="28" rx="22" ry="16" fill="{color}" stroke="{DARK}" stroke-width="3.5"/><circle cx="48" cy="18" r="10" fill="{color}" stroke="{DARK}" stroke-width="3.5"/>'
                 f'<path d="M56 16 L64 19 L56 22 Z" fill="{ORANGE}"/><circle cx="50" cy="16" r="2" fill="{DARK}"/><path d="M14 26 Q26 36 36 26" fill="none" stroke="{DARK}" stroke-width="3"/>', size)


def fish(size=60, color=ORANGE):
    return _icon(70, 40, f'<path d="M8 20 C20 2 46 2 56 20 C46 38 20 38 8 20 Z" fill="{color}" stroke="{DARK}" stroke-width="3.5"/><path d="M56 20 L68 8 V32 Z" fill="{color}" stroke="{DARK}" stroke-width="3.5" stroke-linejoin="round"/><circle cx="20" cy="17" r="2.6" fill="{DARK}"/>', size)


def cat_icon(size=60, color=ORANGE):
    return _icon(60, 56, f'<path d="M8 22 L10 4 L22 14 H38 L50 4 L52 22 C56 42 44 52 30 52 C16 52 4 42 8 22 Z" fill="{color}" stroke="{DARK}" stroke-width="3.5" stroke-linejoin="round"/>'
                 f'<circle cx="22" cy="28" r="3" fill="{DARK}"/><circle cx="38" cy="28" r="3" fill="{DARK}"/><path d="M27 36 L30 39 L33 36" fill="none" stroke="{DARK}" stroke-width="2.5"/>', size)


def dog_icon(size=60, color=BROWN):
    return _icon(64, 56, f'<ellipse cx="10" cy="22" rx="8" ry="16" fill="{DARK}" opacity="0.8"/><ellipse cx="54" cy="22" rx="8" ry="16" fill="{DARK}" opacity="0.8"/><circle cx="32" cy="28" r="22" fill="{color}" stroke="{DARK}" stroke-width="3.5"/>'
                 f'<circle cx="24" cy="24" r="3" fill="{DARK}"/><circle cx="40" cy="24" r="3" fill="{DARK}"/><ellipse cx="32" cy="36" rx="6" ry="4.5" fill="{DARK}"/>', size)


def frog(size=80):
    return _icon(80, 60, f'<ellipse cx="40" cy="38" rx="32" ry="20" fill="{GREEN}" stroke="{DARK}" stroke-width="4"/><circle cx="24" cy="18" r="11" fill="{GREEN}" stroke="{DARK}" stroke-width="4"/><circle cx="56" cy="18" r="11" fill="{GREEN}" stroke="{DARK}" stroke-width="4"/>'
                 f'<circle cx="24" cy="17" r="4" fill="{DARK}"/><circle cx="56" cy="17" r="4" fill="{DARK}"/><path d="M28 42 Q40 50 52 42" fill="none" stroke="{DARK}" stroke-width="3.5"/>', size)


def grape(size=40):
    return dot(size, PURPLE)


def egg(size=40):
    return _icon(34, 42, f'<ellipse cx="17" cy="22" rx="14" ry="18" fill="#fff8ec" stroke="{DARK}" stroke-width="3"/>', size)


def bag(size=110, color=BROWN, inner=None):
    b = _icon(100, 100, f'<path d="M14 30 H86 L94 96 H6 Z" fill="{soft(color)}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/><path d="M34 30 C34 8 66 8 66 30" fill="none" stroke="{DARK}" stroke-width="5"/>', size)
    if inner is not None:
        b = over(b, sized(inner, size * 0.7, size * 0.5), dy=size * 0.12)
    return b


def plate(size=120, inner=None):
    p = _icon(120, 40, f'<ellipse cx="60" cy="20" rx="56" ry="16" fill="#fff" stroke="{DARK}" stroke-width="5"/><ellipse cx="60" cy="20" rx="38" ry="9" fill="none" stroke="{LIGHT}" stroke-width="3"/>', size)
    if inner is not None:
        c = sized(inner, size * 0.7, size * 0.3)
        return Item(p.w, p.h + c.h * 0.6, g(p, 0, c.h * 0.6) + g(c, (p.w - c.w) / 2, 0))
    return p


def cup(size=90, inner=None, color=BLUE):
    c = _icon(70, 80, f'<path d="M6 8 H64 L56 76 H14 Z" fill="{soft(color)}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)
    if inner is not None:
        c = over(c, sized(inner, size * 0.55, size * 0.6), dy=size * 0.04)
    return c


def basket(size=150, inner=None, color=BROWN):
    b = _icon(120, 70, f'<path d="M4 20 H116 L104 66 H16 Z" fill="#e8c597" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
              + ''.join(f'<line x1="{14 + i * 18}" y1="22" x2="{20 + i * 15}" y2="64" stroke="{BROWN}" stroke-width="3"/>' for i in range(6)), size)
    if inner is not None:
        c = sized(inner, size * 0.75, size * 0.4)
        return Item(b.w, b.h + c.h * 0.7, g(c, (b.w - c.w) / 2, 0) + g(b, 0, c.h * 0.7))
    return b


def clipboard(size=170, inner=None):
    c = _icon(80, 104, f'<rect x="4" y="10" width="72" height="90" rx="6" fill="{BROWN}" stroke="{DARK}" stroke-width="5"/><rect x="12" y="20" width="56" height="74" fill="#fff" stroke="{DARK}" stroke-width="3"/>'
              f'<rect x="26" y="4" width="28" height="14" rx="4" fill="#b8bcc6" stroke="{DARK}" stroke-width="4"/>', size)
    if inner is not None:
        k = size / 104
        x = sized(inner, 48 * k, 62 * k)
        c = Item(c.w, c.h, c.svg + g(x, 40 * k - x.w / 2, 57 * k - x.h / 2))
    return c


def calendar(size=170, circled=None, checks=(), cross_=None, cells=28, cols=7, header=True):
    out = [f'<rect x="4" y="8" width="112" height="100" rx="8" fill="#fff" stroke="{DARK}" stroke-width="5"/>']
    if header:
        out.append(f'<rect x="4" y="8" width="112" height="22" rx="8" fill="{RED}" stroke="{DARK}" stroke-width="5"/>')
        out.append(''.join(f'<rect x="{26 + i * 64}" y="2" width="8" height="16" rx="3" fill="{GRAY}" stroke="{DARK}" stroke-width="3"/>' for i in range(2)))
    rows = math.ceil(cells / cols)
    cw, ch = 104 / cols, (72 if header else 92) / rows
    y0 = 34 if header else 14
    for i in range(cells):
        x, y = 8 + (i % cols) * cw, y0 + (i // cols) * ch
        out.append(f'<rect x="{x + 1:.1f}" y="{y + 1:.1f}" width="{cw - 2:.1f}" height="{ch - 2:.1f}" rx="2" fill="{LIGHT}"/>')
        if i in checks:
            out.append(f'<path d="M{x + cw * 0.2:.1f} {y + ch * 0.5:.1f} l{cw * 0.2:.1f} {ch * 0.25:.1f} l{cw * 0.4:.1f} -{ch * 0.5:.1f}" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round"/>')
        if i == circled:
            ring = f'<circle cx="{x + cw / 2:.1f}" cy="{y + ch / 2:.1f}" r="{max(cw, ch) * 0.62:.1f}" fill="none" stroke="{RED}" stroke-width="3.5"/>'
        if i == cross_:
            out.append(f'<path d="M{x + 2:.1f} {y + 2:.1f} L{x + cw - 2:.1f} {y + ch - 2:.1f} M{x + cw - 2:.1f} {y + 2:.1f} L{x + 2:.1f} {y + ch - 2:.1f}" stroke="{RED}" stroke-width="3"/>')
    if circled is not None:
        out.append(ring)
    return _icon(120, 110, ''.join(out), size)


def clock(size=180, h=3, m=0, sweep=None, numbers=True, hl=None):
    """An analog clock at h:m; sweep shades the minutes from m to sweep; hl: 'hour'/'h' or 'minute'/'m' hand in color
    (hour orange, minute blue). Both hands stop inside the numeral ring so no number is covered."""
    hl = {'h': 'hour', 'm': 'minute'}.get(hl, hl)
    out = [f'<circle cx="60" cy="60" r="54" fill="#fff" stroke="{DARK}" stroke-width="6"/>']
    if sweep is not None:
        a0, a1 = math.radians(m * 6 - 90), math.radians(sweep * 6 - 90)
        out.append(f'<path d="M60 60 L{60 + 50 * math.cos(a0):.1f} {60 + 50 * math.sin(a0):.1f} A50 50 0 {1 if (sweep - m) % 60 > 30 else 0} 1 {60 + 50 * math.cos(a1):.1f} {60 + 50 * math.sin(a1):.1f} Z" fill="{soft(ORANGE)}"/>')
    for k in range(60):
        a = math.radians(k * 6)
        r0 = 45 if k % 5 == 0 else 48
        out.append(f'<line x1="{60 + r0 * math.sin(a):.1f}" y1="{60 - r0 * math.cos(a):.1f}" x2="{60 + 51 * math.sin(a):.1f}" y2="{60 - 51 * math.cos(a):.1f}" stroke="{DARK}" stroke-width="{2.5 if k % 5 == 0 else 1}"/>')
    if numbers:
        for n in range(1, 13):
            a = math.radians(n * 30)
            out.append(f'<text x="{60 + 37 * math.sin(a):.1f}" y="{60 - 37 * math.cos(a) + 4.5:.1f}" font-family="{SANS}" font-size="12.5" font-weight="700" text-anchor="middle" fill="{DARK}">{n}</text>')
    ha = math.radians((h % 12) * 30 + m * 0.5)
    ma = math.radians(m * 6)
    hr, mr = (17, 28) if numbers else (26, 42)
    hc, mc = (ORANGE if hl == 'hour' else DARK), (BLUE if hl == 'minute' else DARK)
    out.append(f'<line x1="60" y1="60" x2="{60 + mr * math.sin(ma):.1f}" y2="{60 - mr * math.cos(ma):.1f}" stroke="{mc}" stroke-width="{5 if hl == "minute" else 4}" stroke-linecap="round"/>')
    out.append(f'<line x1="60" y1="60" x2="{60 + hr * math.sin(ha):.1f}" y2="{60 - hr * math.cos(ha):.1f}" stroke="{hc}" stroke-width="7.5" stroke-linecap="round"/>')
    out.append(f'<circle cx="60" cy="60" r="4.5" fill="{DARK}"/>')
    return _icon(120, 120, ''.join(out), size)


def digital(s='4:30', size=200):
    t = T(s, 64, '#ff5a3c', font="'Consolas', 'Courier New', monospace")
    return box(t, color=DARK, fill='#23262e', p=20)


def envelope(size=120, color='#fff'):
    return _icon(110, 74, f'<rect x="4" y="4" width="102" height="66" rx="5" fill="{color}" stroke="{DARK}" stroke-width="5"/><path d="M6 8 L55 44 L104 8" fill="none" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)


def pencil(size=150, color=YELLOW, angle=-35):
    return _icon(140, 140, f'<g transform="rotate({angle} 70 70)"><rect x="20" y="58" width="90" height="24" fill="{color}" stroke="{DARK}" stroke-width="5"/><path d="M110 58 L134 70 L110 82 Z" fill="#f2d2a2" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
                 f'<path d="M127 66.5 L134 70 L127 73.5 Z" fill="{DARK}"/><rect x="6" y="58" width="16" height="24" rx="3" fill="{PINK}" stroke="{DARK}" stroke-width="5"/></g>', size)


def scale_icon(size=200, left=None, right=None, tilt=0, base_color=GRAY):
    """A balance scale; tilt > 0 drops the left pan. left/right items sit on the pans."""
    a = math.radians(tilt)
    cx, cy, L = 100, 40, 76
    lx, ly = cx - L * math.cos(a), cy + L * math.sin(a)
    rx, ry = cx + L * math.cos(a), cy - L * math.sin(a)
    out = [f'<path d="M84 150 H116 L108 140 H92 Z" fill="{base_color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/><line x1="100" y1="40" x2="100" y2="142" stroke="{DARK}" stroke-width="8"/>',
           f'<line x1="{lx:.1f}" y1="{ly:.1f}" x2="{rx:.1f}" y2="{ry:.1f}" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/><circle cx="100" cy="40" r="7" fill="{YELLOW}" stroke="{DARK}" stroke-width="4"/>']
    for px, py in ((lx, ly), (rx, ry)):
        out.append(f'<path d="M{px:.1f} {py:.1f} L{px - 28:.1f} {py + 46:.1f} M{px:.1f} {py:.1f} L{px + 28:.1f} {py + 46:.1f}" stroke="{DARK}" stroke-width="3"/>')
        out.append(f'<path d="M{px - 36:.1f} {py + 46:.1f} H{px + 36:.1f} Q{px:.1f} {py + 66:.1f} {px - 36:.1f} {py + 46:.1f} Z" fill="{YELLOW}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>')
    s = Item(200, 156, ''.join(out))
    for item, (px, py) in ((left, (lx, ly)), (right, (rx, ry))):
        if item is not None:
            c = sized(item, 78, 52) if (it(item).w > 78 or it(item).h > 52) else it(item)
            s = Item(s.w, s.h, s.svg + g(c, px - c.w / 2, py + 44 - c.h))
    return sized(s, size)


def seesaw(size=240, left=None, right=None, tilt=0):
    a = math.radians(tilt)
    cx, cy, L = 120, 90, 110
    lx, ly = cx - L * math.cos(a), cy + L * math.sin(a)
    rx, ry = cx + L * math.cos(a), cy - L * math.sin(a)
    svg = f'<path d="M100 130 L120 90 L140 130 Z" fill="{GRAY}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/><line x1="{lx:.1f}" y1="{ly:.1f}" x2="{rx:.1f}" y2="{ry:.1f}" stroke="{BROWN}" stroke-width="10" stroke-linecap="round"/>'
    s = Item(240, 134, svg)
    for item, (px, py) in ((left, (lx + 24 * math.cos(a), ly - 24 * math.sin(a))), (right, (rx - 24 * math.cos(a), ry + 24 * math.sin(a)))):
        if item is not None:
            c = sized(item, 60, 60)
            s = Item(s.w, s.h, s.svg + g(c, px - c.w / 2, py - c.h - 6))
    return sized(s, size)


def pillars(n=3, size=220, roof=True, color=GRAY, inner=None):
    out = []
    if roof:
        out.append(f'<path d="M6 34 L100 4 L194 34 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>')
    for i in range(n):
        x = 30 + i * (140 / max(1, n - 1)) if n > 1 else 100
        out.append(f'<rect x="{x - 12:.1f}" y="40" width="24" height="90" fill="#fff" stroke="{DARK}" stroke-width="5"/>')
    out.append(f'<rect x="10" y="130" width="180" height="14" fill="{color}" stroke="{DARK}" stroke-width="5"/>')
    return _icon(200, 148, ''.join(out), size)


def bridge(size=240, a=None, b=None):
    svg = f'<path d="M50 70 Q120 10 190 70" fill="none" stroke="{BROWN}" stroke-width="10"/><line x1="50" y1="70" x2="190" y2="70" stroke="{BROWN}" stroke-width="10"/>' + ''.join(f'<line x1="{x}" y1="{70 - 60 * (1 - ((x - 120) / 70) ** 2) * 0.9:.1f}" x2="{x}" y2="70" stroke="{BROWN}" stroke-width="4"/>' for x in range(70, 180, 20))
    svg += f'<rect x="4" y="60" width="50" height="60" rx="6" fill="{soft(BLUE)}" stroke="{BLUE}" stroke-width="5"/><rect x="186" y="60" width="50" height="60" rx="6" fill="{soft(ORANGE)}" stroke="{ORANGE}" stroke-width="5"/>'
    return _icon(240, 124, svg, size)


def stairs(n=4, size=220, labels=None, color=BLUE, hl=None):
    out = []
    sw_, sh = 200 / n, 150 / n
    for i in range(n):
        out.append(f'<rect x="{i * sw_:.1f}" y="{150 - (i + 1) * sh:.1f}" width="{sw_:.1f}" height="{(i + 1) * sh:.1f}" fill="{soft(color) if hl != i else color}" stroke="{DARK}" stroke-width="4"/>')
        if labels:
            out.append(f'<text x="{i * sw_ + sw_ / 2:.1f}" y="{150 - (i + 1) * sh + sh * 0.7:.1f}" font-family="{SANS}" font-size="{min(sh * 0.6, sw_ * 0.5):.1f}" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(str(labels[i]))}</text>')
    return _icon(200, 152, ''.join(out), size)


def mountain(size=220, flag_=False, path=False):
    svg = f'<path d="M4 120 L80 20 L120 70 L140 50 L196 120 Z" fill="#9aa5b8" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/><path d="M64 41 L80 20 L96 41 L88 36 L80 44 L72 36 Z" fill="#fff"/>'
    if flag_:
        svg += f'<line x1="80" y1="20" x2="80" y2="-6" stroke="{DARK}" stroke-width="4"/><path d="M80 -6 L100 0 L80 6 Z" fill="{RED}"/>'
    if path:
        svg += f'<path d="M20 116 Q50 100 46 86 Q42 70 66 52 Q78 40 80 22" fill="none" stroke="{ORANGE}" stroke-width="5" stroke-dasharray="8 6"/>'
    return _icon(200, 128, f'<g transform="translate(0 8)">{svg}</g>', size)


def fork(size=220):
    return _icon(200, 160, f'<path d="M100 156 V90 L40 10 M100 90 L160 10" fill="none" stroke="#c9b28a" stroke-width="34" stroke-linejoin="round"/><path d="M100 156 V90 L40 10 M100 90 L160 10" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="12 10"/>', size)


def compass(size=200, hl=None, labels=('N', 'E', 'S', 'W')):
    out = [f'<circle cx="100" cy="100" r="62" fill="#fff" stroke="{DARK}" stroke-width="5"/>']
    for i, (ang, lab) in enumerate(zip((0, 90, 180, 270), labels)):
        a = math.radians(ang)
        dx, dy = math.sin(a), -math.cos(a)
        c = RED if (hl and lab in hl) else (DARK if not hl else GRAY)
        out.append(f'<path d="M100 100 L{100 + dx * 54 - dy * 12:.1f} {100 + dy * 54 + dx * 12:.1f} L{100 + dx * 78:.1f} {100 + dy * 78:.1f} L{100 + dx * 54 + dy * 12:.1f} {100 + dy * 54 - dx * 12:.1f} Z" fill="{c if (hl and lab in hl) or (not hl and i == 0) else "#fff"}" stroke="{DARK}" stroke-width="4" stroke-linejoin="round"/>')
        out.append(f'<text x="{100 + dx * 94:.1f}" y="{100 + dy * 94 + 9:.1f}" font-family="{SANS}" font-size="{30 if (hl and lab in hl) else 24}" font-weight="700" text-anchor="middle" fill="{c}">{lab}</text>')
    return _icon(200, 200, ''.join(out), size)


def pin(size=90, color=RED):
    return _icon(60, 86, f'<path d="M30 84 C20 64 4 50 4 30 C4 14 16 4 30 4 C44 4 56 14 56 30 C56 50 40 64 30 84 Z" fill="{color}" stroke="{DARK}" stroke-width="5"/><circle cx="30" cy="30" r="10" fill="#fff" stroke="{DARK}" stroke-width="4"/>', size)


def warning(size=120, color=YELLOW, inner='!'):
    w = _icon(110, 100, f'<path d="M55 6 L106 94 H4 Z" fill="{color}" stroke="{DARK}" stroke-width="6" stroke-linejoin="round"/>', size)
    return over(w, T(inner, size * 0.48), dy=size * 0.06)


def stop_hand(size=150):
    o = ' '.join(f'{50 + 46 * math.cos(math.radians(22.5 + 45 * k)):.1f},{50 + 46 * math.sin(math.radians(22.5 + 45 * k)):.1f}' for k in range(8))
    s = _icon(100, 100, f'<polygon points="{o}" fill="{RED}" stroke="{DARK}" stroke-width="5"/>', size)
    return over(s, hand(size * 0.55))


def funnel(size=150, color=BLUE):
    return _icon(100, 110, f'<path d="M4 10 H96 L60 56 V100 L40 108 V56 Z" fill="{soft(color)}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)


def magnet(size=150, flip=False, angle=0):
    a, b = (('S', BLUE), ('N', RED)) if flip else (('N', RED), ('S', BLUE))
    return _icon(160, 50, f'<g transform="rotate({angle} 80 25)"><rect x="4" y="6" width="76" height="40" fill="{a[1]}" stroke="{DARK}" stroke-width="5"/><rect x="80" y="6" width="76" height="40" fill="{b[1]}" stroke="{DARK}" stroke-width="5"/>'
                 f'<text x="42" y="37" font-family="{SANS}" font-size="26" font-weight="700" fill="#fff" text-anchor="middle">{a[0]}</text><text x="118" y="37" font-family="{SANS}" font-size="26" font-weight="700" fill="#fff" text-anchor="middle">{b[0]}</text></g>', size)


def battery(size=120):
    return _icon(110, 50, f'<rect x="4" y="6" width="90" height="40" rx="6" fill="{GREEN}" stroke="{DARK}" stroke-width="5"/><rect x="94" y="16" width="10" height="20" fill="{GRAY}" stroke="{DARK}" stroke-width="4"/>'
                 f'<text x="78" y="36" font-family="{SANS}" font-size="26" font-weight="700" fill="#fff">+</text><text x="12" y="36" font-family="{SANS}" font-size="26" font-weight="700" fill="#fff">−</text>', size)


def lightbulb_on(size=100):
    b = bulb(size)
    k = size / 110
    rays = ''.join(f'<line x1="{(40 + 48 * math.cos(a)) * k:.1f}" y1="{(40 + 48 * math.sin(a)) * k:.1f}" x2="{(40 + 60 * math.cos(a)) * k:.1f}" y2="{(40 + 60 * math.sin(a)) * k:.1f}" stroke="{ORANGE}" stroke-width="5" stroke-linecap="round"/>' for a in [math.radians(d) for d in (-160, -125, -90, -55, -20)])
    return Item(b.w, b.h, rays + b.svg)


def thermometer(size=180, level=0.5, label=None, color=RED):
    h = 20 + (1 - level) * 100
    t = _icon(60, 160, f'<rect x="20" y="6" width="20" height="124" rx="10" fill="#fff" stroke="{DARK}" stroke-width="5"/><circle cx="30" cy="138" r="18" fill="{color}" stroke="{DARK}" stroke-width="5"/>'
              f'<rect x="25" y="{h:.1f}" width="10" height="{132 - h:.1f}" fill="{color}"/>' + ''.join(f'<line x1="40" y1="{20 + i * 20}" x2="48" y2="{20 + i * 20}" stroke="{DARK}" stroke-width="3"/>' for i in range(6)), size)
    return row(t, T(label, size * 0.2)) if label else t


def flask(size=160, color=BLUE, label=None, level=0.5, beaker=False, dots=0):
    if beaker:
        svg = f'<path d="M14 6 H86 V110 Q86 116 80 116 H20 Q14 116 14 110 Z" fill="#fff" stroke="{DARK}" stroke-width="5"/><rect x="17" y="{116 - 106 * level:.1f}" width="66" height="{106 * level - 3:.1f}" fill="{soft(color)}"/>'
        rnd = __import__('random').Random(dots)
        svg += ''.join(f'<circle cx="{rnd.uniform(24, 76):.1f}" cy="{rnd.uniform(116 - 100 * level, 108):.1f}" r="4" fill="{color}"/>' for _ in range(dots))
        f = _icon(100, 120, svg, size)
    else:
        svg = f'<path d="M38 6 H62 V44 L94 108 Q96 116 88 116 H12 Q4 116 6 108 L38 44 Z" fill="#fff" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/><path d="M{50 - 40 * level - 4:.1f} {116 - 70 * level:.1f} H{50 + 40 * level + 4:.1f} L91 110 H9 Z" fill="{soft(color)}"/>'
        f = _icon(100, 120, svg, size)
    if label:
        f = over(f, T(label, size * 0.15), dy=size * 0.25)
    return f


def cylinders(n=3, size=150, color=BLUE):
    out = []
    for i in range(n):
        y = 10 + i * 32
        out.append(f'<path d="M6 {y} V{y + 28} A44 12 0 0 0 94 {y + 28} V{y}" fill="{soft(color)}" stroke="{DARK}" stroke-width="5"/><ellipse cx="50" cy="{y}" rx="44" ry="12" fill="{color if i == 0 else soft(color)}" stroke="{DARK}" stroke-width="5"/>')
    return _icon(100, 20 + n * 32 + 12, ''.join(reversed(out)), size)


def globe(size=150, lines=True, color=BLUE, land=GREEN, lat=False, grid_=False):
    svg = f'<circle cx="50" cy="50" r="44" fill="{soft(color)}" stroke="{DARK}" stroke-width="5"/>'
    svg += f'<path d="M24 26 C34 22 40 30 36 38 C30 46 20 44 18 36 Z M54 18 C66 14 78 22 76 32 C72 44 62 40 58 52 C56 62 64 70 60 80 C52 82 48 70 50 58 C52 46 44 40 46 30 Z" fill="{land}" stroke="{DARK}" stroke-width="2.5"/>'
    if lat or grid_:
        svg += ''.join(f'<ellipse cx="50" cy="50" rx="44" ry="{abs(y)}" fill="none" stroke="{DARK}" stroke-width="1.5" opacity="0.5"/>' if False else f'<line x1="{50 - math.sqrt(max(0, 44 ** 2 - y ** 2)):.1f}" y1="{50 + y}" x2="{50 + math.sqrt(max(0, 44 ** 2 - y ** 2)):.1f}" y2="{50 + y}" stroke="{DARK}" stroke-width="2" opacity="0.7"/>' for y in (-30, -15, 0, 15, 30))
    if grid_:
        svg += ''.join(f'<ellipse cx="50" cy="50" rx="{rx}" ry="44" fill="none" stroke="{DARK}" stroke-width="2" opacity="0.7"/>' for rx in (15, 32))
    return _icon(100, 100, svg, size)


def atom(size=180, shells=(2, 4), protons=0, neutrons=0, hl_outer=False, nucleus_label=None):
    out = []
    n = len(shells)
    for i, e in enumerate(shells):
        r = 34 + i * 26
        out.append(f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="{GRAY}" stroke-width="3"/>')
        for k in range(e):
            a = 2 * math.pi * k / e + i * 0.4
            hl = hl_outer and i == n - 1
            out.append(f'<circle cx="{100 + r * math.cos(a):.1f}" cy="{100 + r * math.sin(a):.1f}" r="{8 if hl else 6.5}" fill="{ORANGE if hl else BLUE}" stroke="{DARK}" stroke-width="2.5"/>')
    balls = [('p', RED)] * protons + [('n', GRAY)] * neutrons
    if not balls:
        balls = [('p', RED), ('n', GRAY), ('p', RED), ('n', GRAY)]
    rnd = __import__('random').Random(len(balls))
    for i, (k, c) in enumerate(balls):
        a, rr = i * 2.4, 4 + 3.2 * math.sqrt(i)
        x, y = 100 + rr * math.cos(a), 100 + rr * math.sin(a)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{c}" stroke="{DARK}" stroke-width="2"/>')
        if k == 'p' and protons:
            out.append(f'<text x="{x:.1f}" y="{y + 4:.1f}" font-family="{SANS}" font-size="11" font-weight="700" text-anchor="middle" fill="#fff">+</text>')
    R = 34 + (n - 1) * 26 + 12 if shells else 30
    return _icon(200, 200, f'<g transform="translate({100 - 100 * 1:.0f} 0)">' + ''.join(out) + '</g>', size) if R > 0 else None


def nucleus(protons=3, neutrons=3, size=120, plus=True):
    balls = []
    for i in range(protons + neutrons):
        balls.append('p' if (i % 2 == 0 and balls.count('p') < protons) or balls.count('n') >= neutrons else 'n')
    out = []
    for i, k in enumerate(balls):
        a, rr = i * 2.4, 3 + 9 * math.sqrt(i)
        x, y = 60 + rr * math.cos(a), 60 + rr * math.sin(a)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{RED if k == "p" else GRAY}" stroke="{DARK}" stroke-width="3"/>')
        if k == 'p' and plus:
            out.append(f'<text x="{x:.1f}" y="{y + 7:.1f}" font-family="{SANS}" font-size="20" font-weight="700" text-anchor="middle" fill="#fff">+</text>')
    return _icon(120, 120, ''.join(out), size)


def molecule(size=140, atoms=(('O', RED, 0, 0, 30), ('H', '#fff', -36, 26, 20), ('H', '#fff', 36, 26, 20)), bonds=((0, 1), (0, 2)), labels=True):
    out = []
    for a, b in bonds:
        out.append(f'<line x1="{100 + atoms[a][2]}" y1="{80 + atoms[a][3]}" x2="{100 + atoms[b][2]}" y2="{80 + atoms[b][3]}" stroke="{DARK}" stroke-width="6"/>')
    for s, c, x, y, r in atoms:
        out.append(f'<circle cx="{100 + x}" cy="{80 + y}" r="{r}" fill="{c}" stroke="{DARK}" stroke-width="4"/>')
        if labels:
            out.append(f'<text x="{100 + x}" y="{80 + y + r * 0.4:.1f}" font-family="{SANS}" font-size="{r * 1.05:.1f}" font-weight="700" text-anchor="middle" fill="{DARK if c in ("#fff", YELLOW) else "#fff"}">{s}</text>')
    xs = [a[2] for a in atoms]
    ys = [a[3] for a in atoms]
    rs = max(a[4] for a in atoms)
    x0, x1, y0, y1 = 100 + min(xs) - rs - 4, 100 + max(xs) + rs + 4, 80 + min(ys) - rs - 4, 80 + max(ys) + rs + 4
    return _icon(x1 - x0, y1 - y0, f'<g transform="translate({-x0:.1f} {-y0:.1f})">' + ''.join(out) + '</g>', size)


def water(size=120):
    return molecule(size)


def cell(size=180, nucleus_=True, color=GREEN, membrane_hl=False, plant=False, parts=(), labels=None, organelles=True, rod=False, focus=None):
    if rod:
        svg = f'<rect x="8" y="30" width="184" height="80" rx="40" fill="{soft(color)}" stroke="{DARK}" stroke-width="5"/><path d="M50 70 C70 50 90 90 110 70 C130 50 150 90 160 70" fill="none" stroke="{PURPLE}" stroke-width="4"/>'
        return _icon(200, 140, svg, size)
    if plant:
        svg = f'<rect x="8" y="8" width="184" height="144" rx="10" fill="{soft(GREEN)}" stroke="{DARK}" stroke-width="7"/><rect x="18" y="18" width="164" height="124" rx="6" fill="#fbfff4" stroke="{GREEN}" stroke-width="3"/>'
        svg += f'<rect x="90" y="40" width="70" height="76" rx="14" fill="#d8ecff" stroke="{DARK}" stroke-width="3"/>'
        cx, cy = 56, 80
    else:
        svg = f'<ellipse cx="100" cy="80" rx="92" ry="72" fill="{soft(color)}" stroke="{ORANGE if membrane_hl else DARK}" stroke-width="{10 if membrane_hl else 5}"/>'
        cx, cy = 100, 80
    if organelles:
        svg += ''.join(f'<ellipse cx="{x}" cy="{y}" rx="13" ry="7" fill="{ORANGE}" stroke="{DARK}" stroke-width="2.5" transform="rotate({r} {x} {y})"/>' for x, y, r in ((48 if not plant else 40, 50, 20), (150 if not plant else 140, 128, -15), (56, 120, 40)))
        if plant:
            svg += ''.join(f'<ellipse cx="{x}" cy="{y}" rx="11" ry="7" fill="{GREEN}" stroke="{DARK}" stroke-width="2.5"/>' for x, y in ((36, 36), (70, 132), (170, 30)))
        svg += ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="{DARK}"/>' for x, y in ((130, 40), (140, 52), (60, 100), (150, 90), (120, 120)))
    if nucleus_:
        svg += f'<circle cx="{cx}" cy="{cy}" r="{26 if nucleus_ != "dark" else 30}" fill="{PURPLE if nucleus_ != "dark" else "#4a2d6e"}" stroke="{DARK}" stroke-width="4"/>'
    if focus == 'chloroplast' and plant:
        svg = (f'<g opacity="0.35">{svg}</g><ellipse cx="70" cy="132" rx="15" ry="10" fill="{GREEN}" stroke="{DARK}" stroke-width="3"/>'
               f'<circle cx="70" cy="132" r="25" fill="none" stroke="{RED}" stroke-width="5"/>')
    return _icon(200, 160, svg, size)


def dna(size=200, hl=None, changed=None, horizontal=True, rungs=10):
    out = []
    L = 220
    for i in range(rungs):
        x = 10 + i * L / (rungs - 1)
        y1 = 50 + 34 * math.sin(i * 0.75)
        y2 = 100 - y1 + 50
        c = ORANGE if (hl and hl[0] <= i <= hl[1]) else (RED if changed == i else GRAY)
        out.append(f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{7 if c != GRAY else 5}"/>')
    for ph in (0, math.pi):
        pts = [(10 + t * L / 80, 75 + 34 * math.sin(t * 0.75 * (rungs - 1) / 80 + ph) * (1 if ph == 0 else 1)) for t in range(81)]
        pts = [(x, 75 + (y - 75)) for x, y in pts]
        out.append('<path d="M' + ' L'.join(f'{x:.1f} {y - 25 if ph == 0 else 150 - (y - 25) - 50:.1f}' for x, y in pts) + f'" fill="none" stroke="{BLUE if ph == 0 else PURPLE}" stroke-width="8" stroke-linecap="round"/>')
    return _icon(240, 110, f'<g transform="translate(0 -20)">' + ''.join(out) + '</g>', size)


def chromosome(size=130, color=PURPLE):
    return _icon(100, 120, f'<path d="M14 6 C30 0 46 40 50 60 C46 80 30 120 14 114 C2 108 38 74 40 60 C38 46 2 12 14 6 Z" fill="{color}" stroke="{DARK}" stroke-width="4"/>'
                 f'<path d="M86 6 C70 0 54 40 50 60 C54 80 70 120 86 114 C98 108 62 74 60 60 C62 46 98 12 86 6 Z" fill="{color}" stroke="{DARK}" stroke-width="4"/><circle cx="50" cy="60" r="8" fill="{YELLOW}" stroke="{DARK}" stroke-width="3"/>', size)


def neuron(size=220):
    svg = f'<circle cx="50" cy="60" r="24" fill="{soft(PURPLE)}" stroke="{DARK}" stroke-width="5"/><circle cx="50" cy="60" r="9" fill="{PURPLE}"/>'
    svg += ''.join(f'<path d="M{50 + 22 * math.cos(a):.1f} {60 + 22 * math.sin(a):.1f} L{50 + 46 * math.cos(a):.1f} {60 + 46 * math.sin(a):.1f} l{8 * math.cos(a + 0.6):.1f} {8 * math.sin(a + 0.6):.1f} M{50 + 46 * math.cos(a):.1f} {60 + 46 * math.sin(a):.1f} l{8 * math.cos(a - 0.6):.1f} {8 * math.sin(a - 0.6):.1f}" fill="none" stroke="{DARK}" stroke-width="4" stroke-linecap="round"/>' for a in [math.radians(d) for d in (100, 150, 200, 250, 300)])
    svg += f'<path d="M74 60 H210" stroke="{DARK}" stroke-width="6"/>' + ''.join(f'<rect x="{x}" y="53" width="22" height="14" rx="7" fill="{YELLOW}" stroke="{DARK}" stroke-width="3"/>' for x in (90, 122, 154))
    svg += ''.join(f'<path d="M210 60 l16 {d}" stroke="{DARK}" stroke-width="4" stroke-linecap="round"/><circle cx="226" cy="{60 + d}" r="5" fill="{DARK}"/>' for d in (-18, 0, 18))
    return _icon(240, 120, svg, size)


def brain(size=180, hl=False, color=PINK, cortex=False):
    if cortex:
        d = 'M30 90 C6 86 4 56 20 46 C16 22 44 8 64 18 C80 2 112 4 122 20 C146 14 166 34 156 56 C172 70 160 98 136 96 C126 112 96 112 86 100 C70 112 40 108 30 90 Z'
        svg = (f'<path d="{d}" fill="{PURPLE}" stroke="{DARK}" stroke-width="5"/>'
               f'<path d="{d}" fill="#fbeef3" stroke="none" transform="translate(85 58) scale(0.8) translate(-85 -58)"/>'
               + ''.join(f'<path d="{p}" fill="none" stroke="#d9b8c6" stroke-width="3" stroke-linecap="round"/>' for p in ('M60 60 C70 54 80 66 92 60', 'M96 44 C104 54 114 48 120 56', 'M70 80 C80 74 96 86 106 78')))
        return _icon(170, 116, svg, size)
    svg = f'<path d="M30 90 C6 86 4 56 20 46 C16 22 44 8 64 18 C80 2 112 4 122 20 C146 14 166 34 156 56 C172 70 160 98 136 96 C126 112 96 112 86 100 C70 112 40 108 30 90 Z" fill="{color}" stroke="{DARK}" stroke-width="5"/>'
    svg += ''.join(f'<path d="{d}" fill="none" stroke="{DARK}" stroke-width="3.5" stroke-linecap="round"/>' for d in ('M40 50 C56 44 60 62 76 56', 'M84 28 C92 44 110 34 118 48', 'M60 80 C70 70 90 86 100 74', 'M120 66 C132 60 140 74 150 66', 'M90 54 C96 60 104 58 108 64'))
    if hl:
        svg += f'<circle cx="92" cy="74" r="12" fill="{RED}" stroke="{DARK}" stroke-width="3"/>'
    return _icon(170, 116, svg, size)


def lungs(size=170):
    return _icon(140, 120, f'<path d="M70 6 V40 M70 40 L52 52 M70 40 L88 52" fill="none" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/>'
                 f'<path d="M50 30 C24 34 8 64 10 96 C12 112 30 116 48 106 C58 100 60 84 60 60 V40 C60 32 56 30 50 30 Z" fill="{PINK}" stroke="{DARK}" stroke-width="5"/>'
                 f'<path d="M90 30 C116 34 132 64 130 96 C128 112 110 116 92 106 C82 100 80 84 80 60 V40 C80 32 84 30 90 30 Z" fill="{PINK}" stroke="{DARK}" stroke-width="5"/>', size)


def heart_organ(size=150, vessels=False):
    svg = f'<path d="M60 112 C30 92 8 70 12 44 C16 20 42 14 58 30 C66 10 96 6 106 30 C114 52 96 84 60 112 Z" fill="{RED}" stroke="{DARK}" stroke-width="5"/>'
    svg += f'<path d="M50 30 V4 M70 26 C72 12 84 6 96 8" fill="none" stroke="{DARK}" stroke-width="8" stroke-linecap="round"/>'
    if vessels:
        art = (f'<path d="M70 26 C76 2 104 -4 122 4 M96 8 C112 10 124 24 132 40 M104 2 C118 -14 130 -16 140 -14" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>'
               f'<path d="M50 30 C46 4 22 -6 -2 2 M38 10 C22 14 8 30 0 46 M24 2 C14 -14 2 -18 -8 -16" fill="none" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/>')
        heart_ = svg.replace(f'<path d="M50 30 V4 M70 26 C72 12 84 6 96 8" fill="none" stroke="{DARK}" stroke-width="8" stroke-linecap="round"/>', '')
        svg = art + heart_ + (f'<text x="128" y="64" font-family="{SANS}" font-size="15" font-weight="700" fill="{RED}">arteries</text>'
                              f'<text x="-10" y="70" font-family="{SANS}" font-size="15" font-weight="700" text-anchor="end" fill="{BLUE}">veins</text>')
        return _icon(280, 136, f'<g transform="translate(90 20)">{svg}</g>', size)
    return _icon(120, 120, svg, size)


def stomach(size=170):
    return _icon(140, 150, f'<path d="M48 6 C48 24 30 30 32 52 C34 72 56 78 74 66 C88 56 90 40 78 34 C70 30 64 36 62 28 V6" fill="{PINK}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
                 f'<path d="M70 72 C100 74 110 90 100 100 C88 110 46 96 36 108 C26 120 40 132 60 130 C84 128 104 124 112 136 C116 142 108 148 100 146" fill="none" stroke="{ORANGE}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>'
                 f'<path d="M70 72 C100 74 110 90 100 100 C88 110 46 96 36 108 C26 120 40 132 60 130 C84 128 104 124 112 136 C116 142 108 148 100 146" fill="none" stroke="{DARK}" stroke-width="2" opacity="0.5"/>', size)


def torso(size=200, inner=None):
    t = _icon(120, 160, f'<circle cx="60" cy="24" r="20" fill="#fff" stroke="{DARK}" stroke-width="5"/><path d="M14 156 V74 C14 54 30 46 60 46 C90 46 106 54 106 74 V156 Z" fill="#fff" stroke="{DARK}" stroke-width="5"/>', size)
    if inner is not None:
        t = over(t, sized(inner, size * 0.4, size * 0.45), dy=size * 0.15)
    return t


def skeleton(size=200):
    st = f'stroke="{DARK}" stroke-width="5" stroke-linecap="round"'
    return _icon(100, 180, f'<circle cx="50" cy="18" r="14" fill="#fff" {st}/><line x1="50" y1="32" x2="50" y2="104" {st}/>' + ''.join(f'<path d="M30 {50 + i * 12} Q50 {44 + i * 12} 70 {50 + i * 12}" fill="none" {st}/>' for i in range(4))
                 + f'<path d="M50 44 L22 92 M50 44 L78 92 M50 104 L34 172 M50 104 L66 172" fill="none" {st}/><ellipse cx="50" cy="106" rx="18" ry="7" fill="#fff" {st}/>', size)


def arm_muscle(size=180):
    return _icon(170, 90, f'<path d="M10 70 H70 L120 20" fill="none" stroke="#e9e4da" stroke-width="12" stroke-linecap="round"/><path d="M10 70 H70 L120 20" fill="none" stroke="{DARK}" stroke-width="2"/>'
                 f'<path d="M14 64 C30 30 62 34 74 60 C60 66 36 70 14 64 Z" fill="{RED}" stroke="{DARK}" stroke-width="4"/>', size)


def bars(values, labels=None, color=BLUE, size=280, hl=None, star_=None, colors=None, axis=True, maxv=None, ticks=False, w=None, cut=False, title=False, touch=False):
    """A bar graph; hl: a bar index drawn in orange; star_: a bar index with a star over it."""
    n = len(values)
    W, H = (w or 300), 220
    maxv = maxv or max(values) or 1
    bw = (W - 50) / n * (1 if touch else 0.66)
    step = (W - 50) / n
    out = []
    top = 40 if title else 20
    for i, v in enumerate(values):
        h = (H - top - 30) * (v / maxv if not cut else max(0.05, (v - maxv * 0.8) / (maxv * 0.2)))
        x = 40 + i * step + (0 if touch else (step - bw) / 2)
        c = (colors[i] if colors else ORANGE if hl == i else color)
        out.append(f'<rect x="{x:.1f}" y="{H - 30 - h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{c}" stroke="{DARK}" stroke-width="3"/>')
        if star_ == i:
            out.append(g(star(30), x + bw / 2 - 15, H - 30 - h - 34))
        if labels:
            out.append(f'<text x="{x + bw / 2:.1f}" y="{H - 8}" font-family="{SANS}" font-size="16" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(str(labels[i]))}</text>')
    if axis:
        out.append(f'<path d="M34 {top - 10} V{H - 30} H{W - 4}" fill="none" stroke="{DARK}" stroke-width="4"/>')
    if ticks:
        for k in range(5):
            y = H - 30 - (H - top - 30) * k / 4
            out.append(f'<line x1="28" y1="{y:.1f}" x2="34" y2="{y:.1f}" stroke="{DARK}" stroke-width="3"/><text x="24" y="{y + 5:.1f}" font-family="{SANS}" font-size="14" text-anchor="end" fill="{DARK}">{ticks[k] if isinstance(ticks, (list, tuple)) else k * 5}</text>')
    if cut:
        out.append(f'<path d="M26 {H - 46} l16 -6 M26 {H - 38} l16 -6" stroke="{DARK}" stroke-width="3"/>')
    if title:
        out.append(f'<rect x="80" y="4" width="{W - 160}" height="16" rx="4" fill="{DARK}"/>')
    return _icon(W, H, ''.join(out), size)


def pie(frac=1 / 3, size=180, color=BLUE, parts=None, colors=None, label=None):
    out = [f'<circle cx="60" cy="60" r="54" fill="#fff" stroke="{DARK}" stroke-width="5"/>']
    if parts:
        a = -math.pi / 2
        tot = sum(parts)
        for i, p in enumerate(parts):
            b = a + 2 * math.pi * p / tot
            out.append(f'<path d="M60 60 L{60 + 54 * math.cos(a):.1f} {60 + 54 * math.sin(a):.1f} A54 54 0 {1 if b - a > math.pi else 0} 1 {60 + 54 * math.cos(b):.1f} {60 + 54 * math.sin(b):.1f} Z" fill="{(colors or [BLUE, ORANGE, GREEN, YELLOW, PURPLE])[i]}" stroke="{DARK}" stroke-width="4"/>')
            a = b
    else:
        b = -math.pi / 2 + 2 * math.pi * frac
        out.append(f'<path d="M60 60 L60 6 A54 54 0 {1 if frac > 0.5 else 0} 1 {60 + 54 * math.cos(b):.1f} {60 + 54 * math.sin(b):.1f} Z" fill="{color}" stroke="{DARK}" stroke-width="4"/>')
    p = _icon(120, 120, ''.join(out), size)
    return over(p, T(label, size * 0.16, DARK)) if label else p


def frac_circle(d=4, n=1, size=170, color=BLUE, shaded=None):
    """A circle cut into d equal parts, n of them shaded (or the parts listed in shaded)."""
    out = [f'<circle cx="60" cy="60" r="54" fill="#fff"/>']
    sh = set(shaded if shaded is not None else range(n))
    for k in range(d):
        a, b = -math.pi / 2 + 2 * math.pi * k / d, -math.pi / 2 + 2 * math.pi * (k + 1) / d
        if d == 1:
            out.append(f'<circle cx="60" cy="60" r="54" fill="{color if 0 in sh else "#fff"}"/>')
        else:
            out.append(f'<path d="M60 60 L{60 + 54 * math.cos(a):.1f} {60 + 54 * math.sin(a):.1f} A54 54 0 0 1 {60 + 54 * math.cos(b):.1f} {60 + 54 * math.sin(b):.1f} Z" fill="{color if k in sh else "#fff"}" stroke="{DARK}" stroke-width="4"/>')
    out.append(f'<circle cx="60" cy="60" r="54" fill="none" stroke="{DARK}" stroke-width="5"/>')
    return _icon(120, 120, ''.join(out), size)


def frac_bar(d=4, n=1, w=320, h=60, color=BLUE, shaded=None, labels=False, hl_part=None):
    sh = set(shaded if shaded is not None else range(n))
    out = []
    for k in range(d):
        x = k * w / d
        out.append(f'<rect x="{x + 2.5:.1f}" y="2.5" width="{w / d:.1f}" height="{h - 5}" fill="{color if k in sh else "#fff"}" stroke="{DARK}" stroke-width="4"/>')
        if labels:
            out.append(g(F(1, d, min(26, w / d * 0.4)), x + w / (2 * d) - F(1, d, min(26, w / d * 0.4)).w / 2 + 2.5, (h - F(1, d, min(26, w / d * 0.4)).h) / 2))
    return Item(w + 5, h, ''.join(out))


def grid_shade(n=10, m=10, shaded=0, size=220, color=BLUE, cells=None, hl_row=None, hl_col=None, dots=False):
    """An n x m grid with the first `shaded` cells colored (row by row)."""
    out = []
    cs = size / max(n, m)
    for r in range(n):
        for c in range(m):
            i = r * m + c
            on = (cells and (r, c) in cells) or (not cells and i < shaded) or hl_row == r or hl_col == c
            if dots:
                out.append(f'<circle cx="{c * cs + cs / 2:.1f}" cy="{r * cs + cs / 2:.1f}" r="{cs * 0.32:.1f}" fill="{color if on else DARK}"/>')
            else:
                out.append(f'<rect x="{c * cs + 1.5:.1f}" y="{r * cs + 1.5:.1f}" width="{cs:.1f}" height="{cs:.1f}" fill="{(ORANGE if (hl_row == r or hl_col == c) else color) if on else "#fff"}" stroke="{DARK}" stroke-width="{2 if n > 6 else 3.5}"/>')
    return Item(m * cs + 3, n * cs + 3, ''.join(out))


def dots(n, cols=None, size=34, color=BLUE, gap=10, colors=None, circle_idx=(), extra=0, extra_color=ORANGE):
    """n dots in rows of cols (all in one row by default)."""
    cols = cols or n
    items = [dot(size, (colors[i] if colors else color)) for i in range(n)] + [dot(size, extra_color) for _ in range(extra)]
    rows = [items[k:k + cols] for k in range(0, len(items), cols)]
    return col(*[row(*r, gap=gap, align='t') for r in rows], gap=gap)


def objects(n, icon=dot, cols=None, size=44, gap=10, **kw):
    cols = cols or n
    items = [icon(size, **kw) for _ in range(n)]
    rows = [items[k:k + cols] for k in range(0, len(items), cols)]
    return col(*[row(*r, gap=gap) for r in rows], gap=gap)


def groups(n, k, icon=dot, container='circle', size=40, color=BLUE, per_row=None, gap=22, leftover=0):
    """n groups of k things (in circles, bags, plates or cups)."""
    out = []
    per = per_row or min(k, 3 if k > 4 else k)
    for _ in range(n):
        inner = objects(k, icon, cols=per, size=size, gap=6) if icon is not dot else dots(k, per, size, color, gap=6)
        if container == 'bag':
            out.append(bag(max(130, inner.w + 40), inner=inner))
        elif container == 'plate':
            out.append(plate(max(120, inner.w + 40), inner=inner))
        elif container == 'cup':
            out.append(cup(100, inner=inner))
        else:
            r = max(inner.w, inner.h) / 2 + 18
            out.append(over(Item(2 * r, 2 * r, f'<circle cx="{r:.1f}" cy="{r:.1f}" r="{r - 3:.1f}" fill="#fff" stroke="{DARK}" stroke-width="4" stroke-dasharray="10 6"/>'), inner))
    if leftover:
        out.append(dots(leftover, leftover, size, ORANGE, gap=6))
    return row(*out, gap=gap)


def tenframe(n, size=300, color=RED, extra=0, extra_color=BLUE, full=False):
    cs = size / 5
    out = [f'<rect x="2" y="2" width="{size:.1f}" height="{2 * cs:.1f}" fill="#fff" stroke="{DARK}" stroke-width="5"/>']
    for i in range(10):
        r, c = divmod(i, 5)
        out.append(f'<rect x="{2 + c * cs:.1f}" y="{2 + r * cs:.1f}" width="{cs:.1f}" height="{cs:.1f}" fill="none" stroke="{DARK}" stroke-width="4"/>')
        if i < n:
            out.append(f'<circle cx="{2 + c * cs + cs / 2:.1f}" cy="{2 + r * cs + cs / 2:.1f}" r="{cs * 0.34:.1f}" fill="{color}" stroke="{DARK}" stroke-width="3"/>')
        elif i < n + extra:
            out.append(f'<circle cx="{2 + c * cs + cs / 2:.1f}" cy="{2 + r * cs + cs / 2:.1f}" r="{cs * 0.34:.1f}" fill="{extra_color}" stroke="{DARK}" stroke-width="3"/>')
    return Item(size + 4, 2 * cs + 4, ''.join(out))


def rod(n=10, size=22, color=GREEN, vertical=True, hl=None):
    items = [cube_icon(size, ORANGE if hl and i in hl else color) for i in range(n)]
    return (col if vertical else row)(*items, gap=0)


def flat(size=150, color=GREEN):
    return grid_shade(10, 10, 100, size, color)


def base10(h=0, t=0, o=0, size=26, color=GREEN):
    parts = [flat(size * 7.5, color) for _ in range(h)] + [rod(10, size * 0.75, BLUE) for _ in range(t)]
    ones = objects(o, cube_icon, cols=min(o, 3) or 1, size=size * 0.75, gap=4, color=ORANGE) if o else None
    return row(*parts, ones, gap=14, align='b')


def tally(n, size=120, color=DARK):
    out = []
    x = 0
    for grp in range(math.ceil(n / 5)):
        k = min(5, n - grp * 5)
        for i in range(min(k, 4)):
            out.append(f'<line x1="{x + i * 18:.1f}" y1="6" x2="{x + i * 18:.1f}" y2="94" stroke="{color}" stroke-width="7" stroke-linecap="round"/>')
        if k == 5:
            out.append(f'<line x1="{x - 10:.1f}" y1="78" x2="{x + 64:.1f}" y2="20" stroke="{color}" stroke-width="7" stroke-linecap="round"/>')
        x += 100
    return _icon(max(x - 30, 60), 100, f'<g transform="translate(12 0)">' + ''.join(out) + '</g>', size)


def table(rows=3, cols=3, cells=None, size=260, hl_row=None, hl_col=None, header=True, cw=None, color=BLUE, fs=26):
    """A table; cells: list of rows of strings."""
    if cells:
        rows, cols = len(cells), len(cells[0])
    cw = cw or 260 / cols
    ch = 52
    out = []
    for r in range(rows):
        for c in range(cols):
            fill = (soft(ORANGE) if (r == hl_row or c == hl_col) else (soft(color) if header and r == 0 else '#fff'))
            out.append(f'<rect x="{2 + c * cw:.1f}" y="{2 + r * ch}" width="{cw:.1f}" height="{ch}" fill="{fill}" stroke="{DARK}" stroke-width="3"/>')
            if cells:
                s = str(cells[r][c])
                fsz = min(fs, (cw - 10) / max(0.5, measure(s, 1, True)))
                out.append(f'<text x="{2 + c * cw + cw / 2:.1f}" y="{2 + r * ch + ch / 2 + fsz * 0.36:.1f}" font-family="{SANS}" font-size="{fsz:.1f}" font-weight="{700 if (header and r == 0) else 500}" text-anchor="middle" fill="{DARK}">{escape(s)}</text>')
            elif not (header and r == 0):
                out.append(f'<line x1="{12 + c * cw:.1f}" y1="{2 + r * ch + ch / 2}" x2="{c * cw + cw - 8:.1f}" y2="{2 + r * ch + ch / 2}" stroke="{GRAY}" stroke-width="3"/>')
    return sized(Item(cols * cw + 4, rows * ch + 4, ''.join(out)), size)


def place_chart(labels, digits=None, size=320, hl=None, colors=(GREEN, BLUE, ORANGE, PURPLE, RED, TEAL), point=None):
    """A place value chart. hl: a column picked out (the other digits fade); point: a decimal point after that column."""
    cw = 130
    out = []
    for i, l in enumerate(labels):
        c = colors[i % len(colors)]
        fs = min(23, (cw - 22) / measure(l, 1, True))
        on = hl in (None, i)
        pick = hl is not None and on
        out.append(f'<rect x="{2 + i * cw}" y="2" width="{cw}" height="44" fill="{c}" stroke="{DARK}" stroke-width="3"/>'
                   f'<text x="{2 + i * cw + cw / 2}" y="{31}" font-family="{SANS}" font-size="{fs:.1f}" font-weight="700" text-anchor="middle" fill="#fff">{escape(l)}</text>'
                   f'<rect x="{2 + i * cw}" y="46" width="{cw}" height="90" fill="{soft(c) if pick else "#fff"}" stroke="{DARK}" stroke-width="3"/>')
        if digits:
            out.append(f'<text x="{2 + i * cw + cw / 2}" y="112" font-family="{SANS}" font-size="64" font-weight="700" text-anchor="middle" fill="{DARK if on else "#b4b8c2"}">{escape(str(digits[i]))}</text>')
    if hl is not None:
        out.append(f'<rect x="{3.5 + hl * cw}" y="3.5" width="{cw - 3}" height="131" fill="none" stroke="{RED}" stroke-width="6"/>')
    if point is not None:
        out.append(f'<circle cx="{2 + (point + 1) * cw}" cy="118" r="10" fill="{DARK}" stroke="#fff" stroke-width="3"/>')
    return sized(Item(len(labels) * cw + 4, 140, ''.join(out)), size)


def numberline(a=0, b=10, size=420, step=1, labels=None, marks=None, hops=None, open_=None, closed=None, ray=None, seg=None,
               hl=None, bracket=None, color=BLUE, every=1, fracs=None, hop_label=None, bold=None, arrow_ends=True, dots_=None, xs=None, to=None):
    """A number line. marks: {value: color} dots; hops: [(from, to)] arcs; open_/closed: a ray start (ray='right'/'left');
    seg: (from, to) shaded; bracket: (from, to, text); fracs: denominator for fraction labels; dots_: {value: count} stacks
    (xs=True stacks X marks, as a line plot does); hl: a value whose label is circled; to: (from, to) a red arrow, as in rounding."""
    W = 500
    x0, x1 = 30, W - 30
    vals = []
    v = a
    while v <= b + 1e-9:
        vals.append(round(v, 6))
        v += step
    X = lambda v: x0 + (v - a) / (b - a) * (x1 - x0)
    y = 120
    out = [f'<line x1="{x0 - 18}" y1="{y}" x2="{x1 + 18}" y2="{y}" stroke="{DARK}" stroke-width="5"/>']
    if arrow_ends:
        out.append(f'<path d="M{x1 + 26} {y} l-16 -9 v18 z M{x0 - 26} {y} l16 -9 v18 z" fill="{DARK}"/>')
    if seg:
        out.append(f'<line x1="{X(seg[0]):.1f}" y1="{y}" x2="{X(seg[1]):.1f}" y2="{y}" stroke="{color}" stroke-width="12" stroke-linecap="round"/>')
    if ray:
        start = open_ if open_ is not None else closed
        end = x1 + 18 if ray == 'right' else x0 - 18
        out.append(f'<line x1="{X(start):.1f}" y1="{y}" x2="{end:.1f}" y2="{y}" stroke="{color}" stroke-width="10"/>')
        out.append(f'<path d="M{end + (10 if ray == "right" else -10):.1f} {y} l{-20 if ray == "right" else 20} -14 v28 z" fill="{color}"/>')
    fs = min(28, (x1 - x0) / max(1, len(vals)) * 0.62 * every)
    for i, v in enumerate(vals):
        out.append(f'<line x1="{X(v):.1f}" y1="{y - 12}" x2="{X(v):.1f}" y2="{y + 12}" stroke="{DARK}" stroke-width="3.5"/>')
        if i % every == 0 and labels is not False:
            if fracs:
                k = round((v - a) * fracs)
                lab = F(k, fracs, 20) if 0 < k < fracs * (b - a) and k % fracs else T(str(int(round(v))), 24, bold=True)
                out.append(g(lab, X(v) - lab.w / 2, y + 18))
            else:
                s = (labels[i] if labels else (str(int(v)) if float(v).is_integer() else str(v))).replace('-', '−')
                big = (bold and v in bold)
                out.append(f'<text x="{X(v):.1f}" y="{y + 44}" font-family="{SANS}" font-size="{fs * (1.3 if big else 1):.1f}" font-weight="700" text-anchor="middle" fill="{RED if big else DARK}">{escape(s)}</text>')
                if hl is not None and abs(v - hl) < 1e-9:
                    out.append(f'<ellipse cx="{X(v):.1f}" cy="{y + 35}" rx="{max(fs * 0.4 * len(s), fs * 0.8) + 8:.1f}" ry="{fs * 0.75 + 4:.1f}" fill="none" stroke="{RED}" stroke-width="5"/>')
    if to:
        xa, xb = X(to[0]), X(to[1])
        hgt = min(60, abs(xb - xa) * 0.5 + 24)
        out.append(f'<path d="M{xa:.1f} {y - 16} Q{(xa + xb) / 2:.1f} {y - 16 - hgt * 1.5:.1f} {xb + (8 if xb < xa else -8):.1f} {y - 20}" fill="none" stroke="{RED}" stroke-width="6" stroke-linecap="round"/>'
                   f'<path d="M{xb:.1f} {y - 12} l{12 if xb < xa else -12} -20 l{10 if xb < xa else -10} 10 z" fill="{RED}" stroke="{RED}" stroke-width="3" stroke-linejoin="round"/>')
    for v, c in (marks or {}).items():
        out.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="11" fill="{c}" stroke="{DARK}" stroke-width="3"/>')
    if open_ is not None:
        out.append(f'<circle cx="{X(open_):.1f}" cy="{y}" r="11" fill="#fff" stroke="{color}" stroke-width="5"/>')
    if closed is not None:
        out.append(f'<circle cx="{X(closed):.1f}" cy="{y}" r="11" fill="{color}" stroke="{DARK}" stroke-width="3"/>')
    for i, (p, q) in enumerate(hops or []):
        xa, xb = X(p), X(q)
        hgt = min(70, abs(xb - xa) * 0.6 + 20)
        out.append(f'<path d="M{xa:.1f} {y - 10} Q{(xa + xb) / 2:.1f} {y - 10 - hgt * 1.4:.1f} {xb:.1f} {y - 10}" fill="none" stroke="{ORANGE}" stroke-width="5"/>'
                   f'<path d="M{xb:.1f} {y - 8} l{-12 if xb > xa else 12} -8 l{2 if xb > xa else -2} 12 z" fill="{ORANGE}"/>')
        if hop_label:
            out.append(f'<text x="{(xa + xb) / 2:.1f}" y="{y - hgt * 0.75 - 18:.1f}" font-family="{SANS}" font-size="20" font-weight="700" text-anchor="middle" fill="{ORANGE}">{escape(hop_label)}</text>')
    lift = 0
    if bracket:
        p, q, s = bracket
        tall = max((dots_ or {0: 0}).values())
        bot = y - 26 if not tall else y - 24 - (tall - 1) * (26 if xs else 22) - 18
        lift = max(0, 30 - (bot - 38))
        out.append(f'<path d="M{X(p):.1f} {bot} v-14 H{X(q):.1f} v14" fill="none" stroke="{RED}" stroke-width="4"/>'
                   f'<text x="{(X(p) + X(q)) / 2:.1f}" y="{bot - 24}" font-family="{SANS}" font-size="26" font-weight="700" text-anchor="middle" fill="{RED}">{escape(s)}</text>')
    for v, cnt in (dots_ or {}).items():
        for k in range(cnt):
            if xs:
                cx_, cy_ = X(v), y - 30 - k * 26
                out.append(f'<path d="M{cx_ - 9:.1f} {cy_ - 9:.1f} L{cx_ + 9:.1f} {cy_ + 9:.1f} M{cx_ + 9:.1f} {cy_ - 9:.1f} L{cx_ - 9:.1f} {cy_ + 9:.1f}" stroke="{color}" stroke-width="5" stroke-linecap="round"/>')
            else:
                out.append(f'<circle cx="{X(v):.1f}" cy="{y - 24 - k * 22}" r="9" fill="{color}"/>')
    if lift:
        return sized(Item(W, 180 + lift, f'<g transform="translate(0 {lift:.1f})">' + ''.join(out) + '</g>'), size)
    return sized(Item(W, 180, ''.join(out)), size)


def _sharp(x, y, k=1.0):
    """A sharp sign drawn centered on (x, y) (a line or a space of the staff)."""
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({k})" stroke="{DARK}" stroke-linecap="round">'
            f'<line x1="-4" y1="-17" x2="-4" y2="15" stroke-width="3"/><line x1="4" y1="-15" x2="4" y2="17" stroke-width="3"/>'
            f'<line x1="-10" y1="-3" x2="10" y2="-8" stroke-width="5.5"/><line x1="-10" y1="8" x2="10" y2="3" stroke-width="5.5"/></g>')


def staff(notes=(), size=420, clef=True, bars_=(), time=None, sharps=0, rest=False, chord=False, kinds=None, labels=None, colors=None, bracket=None, w=None, shade=None):
    """A five-line staff. notes: staff steps (0 = bottom line, 1 = first space, ...); a tuple is a chord.
    sharps: a treble-clef key signature (F#, C#, G#, D#); shade: (a, b) the space between two bar positions shaded (one measure)."""
    W = w or 440
    out = [''.join(f'<line x1="10" y1="{40 + i * 20}" x2="{W - 10}" y2="{40 + i * 20}" stroke="{DARK}" stroke-width="3"/>' for i in range(5))]
    x = 30
    if clef:
        out.append(f'<text x="{x - 6}" y="{126}" font-family="\'Segoe UI Symbol\', \'Cambria Math\', serif" font-size="118" fill="{DARK}">𝄞</text>')
        x += 70
    for s in range(sharps):
        out.append(_sharp(x + 10 + s * 22, 120 - [8, 5, 9, 6][s] * 10))
    x += sharps * 22 + (14 if sharps else 0)
    if time:
        out.append(f'<text x="{x}" y="78" font-family="{MATHF}" font-size="46" font-weight="700" fill="{DARK}">{time[0]}</text><text x="{x}" y="118" font-family="{MATHF}" font-size="46" font-weight="700" fill="{DARK}">{time[1]}</text>')
        x += 50
    if rest:
        out.append(f'<text x="{x + 30}" y="104" font-family="\'Segoe UI Symbol\', serif" font-size="70" fill="{DARK}">𝄽</text>')
    n = len(notes)
    span = (W - x - 30) / max(1, n)
    if shade:
        out.insert(0, f'<rect x="{x + span * shade[0]:.1f}" y="40" width="{span * (shade[1] - shade[0]):.1f}" height="80" fill="{soft(BLUE)}"/>')
    for i, nt in enumerate(notes):
        nx = x + span * (i + 0.5)
        steps = nt if isinstance(nt, tuple) else (nt,)
        kind = (kinds[i] if kinds else 'q')
        c = colors[i] if colors else DARK
        for st in steps:
            ny = 120 - st * 10
            if st < -1 or st > 9:
                for ly in range(-2, st - 1, -2) if st < 0 else range(10, st + 1, 2):
                    out.append(f'<line x1="{nx - 18:.1f}" y1="{120 - ly * 10}" x2="{nx + 18:.1f}" y2="{120 - ly * 10}" stroke="{DARK}" stroke-width="3"/>')
            if st == -2:
                out.append(f'<line x1="{nx - 18:.1f}" y1="140" x2="{nx + 18:.1f}" y2="140" stroke="{DARK}" stroke-width="3"/>')
            out.append(f'<ellipse cx="{nx:.1f}" cy="{ny}" rx="12" ry="9" fill="{"#fff" if kind in ("h", "w") else c}" stroke="{c}" stroke-width="3.5" transform="rotate(-20 {nx:.1f} {ny})"/>')
        if kind != 'w':
            top = 120 - max(steps) * 10
            out.append(f'<line x1="{nx + 11:.1f}" y1="{120 - min(steps) * 10:.1f}" x2="{nx + 11:.1f}" y2="{top - 58:.1f}" stroke="{c}" stroke-width="3.5"/>')
        if labels:
            out.append(f'<text x="{nx:.1f}" y="200" font-family="{SANS}" font-size="24" font-weight="700" text-anchor="middle" fill="{c}">{escape(str(labels[i]))}</text>')
    for bx in bars_:
        out.append(f'<line x1="{x + span * bx:.1f}" y1="40" x2="{x + span * bx:.1f}" y2="120" stroke="{DARK}" stroke-width="{8 if shade else 6}"/>')
    if bracket:
        i0, i1 = bracket
        out.append(f'<path d="M{x + span * (i0 + 0.5):.1f} 12 v-8 H{x + span * (i1 + 0.5):.1f} v8" fill="none" stroke="{RED}" stroke-width="4"/>')
    out.append(f'<line x1="{W - 10}" y1="40" x2="{W - 10}" y2="120" stroke="{DARK}" stroke-width="3"/>')
    return sized(Item(W, 210 if labels else 160, f'<g transform="translate(0 {20 if not labels else 20})">' + ''.join(out) + '</g>'), size)


def note(kind='q', size=120):
    """A single note: q (quarter), h (half), e (eighth)."""
    fill = '#fff' if kind == 'h' else DARK
    svg = f'<ellipse cx="30" cy="96" rx="20" ry="14" fill="{fill}" stroke="{DARK}" stroke-width="6" transform="rotate(-20 30 96)"/><line x1="48" y1="92" x2="48" y2="8" stroke="{DARK}" stroke-width="6"/>'
    if kind == 'e':
        svg += f'<path d="M48 8 C56 30 76 34 70 58" fill="none" stroke="{DARK}" stroke-width="6"/>'
    return _icon(80, 116, svg, size)


def quarter_rest(size=120):
    return _icon(50, 110, f'<path d="M14 6 L34 30 L18 50 L36 74 C24 70 14 76 22 100 C4 88 8 70 22 72 L8 54 L24 32 L12 18 Z" fill="{DARK}" stroke="{DARK}" stroke-width="3" stroke-linejoin="round"/>', size)


# ---------- plots ----------

def plot(*fns, size=320, xr=(-5, 5), yr=(-5, 5), axes=True, grid_=False, colors=(BLUE, ORANGE, GREEN, PURPLE, RED), shade=None, points=(),
         open_points=(), hlines=(), vlines=(), dashed=(), segs=(), labels=None, arrows_=(), scatter=(), axis_hl=None, tri=None, box_=False,
         ticks=False, fill_between=None, rects=None, sw=6, curves=(), texts=(), regions=()):
    """Graphs on a square plane. fns: callables y = f(x) (or None). shade: (f, a, b) area under f; fill_between: (f, g, a, b);
    points/open_points: (x, y); hlines/vlines: values drawn dashed; segs: ((x1, y1), (x2, y2), color, dashed);
    scatter: list of (x, y); tri: ((x1, y1), (x2, y2)) slope triangle; rects: (f, a, b, n) Riemann rectangles; curves: (xs, ys) param lists."""
    W = 300
    X = lambda x: 10 + (x - xr[0]) / (xr[1] - xr[0]) * (W - 20)
    Y = lambda y: 10 + (yr[1] - y) / (yr[1] - yr[0]) * (W - 20)
    out = [f'<defs><clipPath id="pc"><rect x="10" y="10" width="{W - 20}" height="{W - 20}"/></clipPath></defs>']
    if grid_:
        for v in range(math.ceil(xr[0]), math.floor(xr[1]) + 1):
            out.append(f'<line x1="{X(v):.1f}" y1="10" x2="{X(v):.1f}" y2="{W - 10}" stroke="#d5d8df" stroke-width="1.5"/>')
        for v in range(math.ceil(yr[0]), math.floor(yr[1]) + 1):
            out.append(f'<line x1="10" y1="{Y(v):.1f}" x2="{W - 10}" y2="{Y(v):.1f}" stroke="#d5d8df" stroke-width="1.5"/>')
    if box_:
        out.append(f'<rect x="10" y="10" width="{W - 20}" height="{W - 20}" fill="none" stroke="{DARK}" stroke-width="3"/>')

    def path(f, a=None, b=None, n=160):
        a = xr[0] if a is None else a
        b = xr[1] if b is None else b
        pts, d = [], ''
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError, OverflowError):
                y = None
            if y is None or not math.isfinite(y) or abs(y) > 1e4:
                pts.append(None)
                continue
            pts.append((X(x), Y(max(min(y, yr[1] + 20), yr[0] - 20))))
        pen = False
        for p in pts:
            if p is None:
                pen = False
                continue
            d += (' L' if pen else ' M') + f'{p[0]:.1f} {p[1]:.1f}'
            pen = True
        return d

    if shade:
        f, a, b = shade[:3]
        c = shade[3] if len(shade) > 3 else BLUE
        out.append(f'<path d="{path(f, a, b)} L{X(b):.1f} {Y(0):.1f} L{X(a):.1f} {Y(0):.1f} Z" fill="{soft(c)}" stroke="none" clip-path="url(#pc)"/>')
    if fill_between:
        f, f2, a, b = fill_between
        top = [(X(a + (b - a) * i / 80), Y(f(a + (b - a) * i / 80))) for i in range(81)]
        bot = [(X(a + (b - a) * i / 80), Y(f2(a + (b - a) * i / 80))) for i in range(80, -1, -1)]
        out.append('<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in top + bot) + f' Z" fill="{soft(ORANGE)}" clip-path="url(#pc)"/>')
    for pts_, c_, op_ in regions:
        out.append('<path d="M' + ' L'.join(f'{X(x):.1f} {Y(y):.1f}' for x, y in pts_) + f' Z" fill="{c_}" opacity="{op_}" clip-path="url(#pc)"/>')
    if rects:
        f, a, b, n = rects
        for i in range(n):
            xa = a + (b - a) * i / n
            hgt = f(xa + (b - a) / n / 2)
            out.append(f'<rect x="{X(xa):.1f}" y="{min(Y(hgt), Y(0)):.1f}" width="{X(xa + (b - a) / n) - X(xa):.1f}" height="{abs(Y(hgt) - Y(0)):.1f}" fill="{soft(ORANGE)}" stroke="{ORANGE}" stroke-width="2.5"/>')
    if axes:
        hx = axis_hl == 'x'
        hy = axis_hl == 'y'
        if yr[0] <= 0 <= yr[1]:
            out.append(f'<line x1="10" y1="{Y(0):.1f}" x2="{W - 10}" y2="{Y(0):.1f}" stroke="{RED if hx else DARK}" stroke-width="{7 if hx else 3.5}"/>')
        if xr[0] <= 0 <= xr[1]:
            out.append(f'<line x1="{X(0):.1f}" y1="10" x2="{X(0):.1f}" y2="{W - 10}" stroke="{RED if hy else DARK}" stroke-width="{7 if hy else 3.5}"/>')
        if ticks:
            for v in range(math.ceil(xr[0]), math.floor(xr[1]) + 1):
                if v and yr[0] <= 0 <= yr[1]:
                    out.append(f'<line x1="{X(v):.1f}" y1="{Y(0) - 5:.1f}" x2="{X(v):.1f}" y2="{Y(0) + 5:.1f}" stroke="{DARK}" stroke-width="2"/>')
    for v in hlines:
        out.append(f'<line x1="10" y1="{Y(v):.1f}" x2="{W - 10}" y2="{Y(v):.1f}" stroke="{GRAY}" stroke-width="3.5" stroke-dasharray="10 7"/>')
    for v in vlines:
        out.append(f'<line x1="{X(v):.1f}" y1="10" x2="{X(v):.1f}" y2="{W - 10}" stroke="{GRAY}" stroke-width="3.5" stroke-dasharray="10 7"/>')
    for i, f in enumerate(fns):
        if f is None:
            continue
        if isinstance(f, tuple):  # (f, a, b) a piece of a function
            d = path(f[0], f[1], f[2])
        else:
            d = path(f)
        out.append(f'<path d="{d}" fill="none" stroke="{colors[i % len(colors)]}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" clip-path="url(#pc)"'
                   f'{" stroke-dasharray=\"12 8\"" if i in dashed else ""}/>')
    for i, (xs, ys) in enumerate(curves):
        out.append('<path d="M' + ' L'.join(f'{X(x):.1f} {Y(y):.1f}' for x, y in zip(xs, ys)) + f'" fill="none" stroke="{colors[(i + len(fns)) % len(colors)]}" stroke-width="{sw}" stroke-linejoin="round" clip-path="url(#pc)"/>')
    for p in segs:
        (x1, y1), (x2, y2) = p[0], p[1]
        c = p[2] if len(p) > 2 else RED
        dsh = len(p) > 3 and p[3]
        out.append(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2):.1f}" y2="{Y(y2):.1f}" stroke="{c}" stroke-width="5" stroke-linecap="round"{" stroke-dasharray=\"10 7\"" if dsh else ""}/>')
    if tri:
        (x1, y1), (x2, y2) = tri
        out.append(f'<path d="M{X(x1):.1f} {Y(y1):.1f} H{X(x2):.1f} V{Y(y2):.1f}" fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="9 6"/>')
    for (x, y) in scatter:
        out.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="6.5" fill="{BLUE}" stroke="{DARK}" stroke-width="2"/>')
    for p in points:
        x, y = p[0], p[1]
        c = p[2] if len(p) > 2 else RED
        out.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="10" fill="{c}" stroke="{DARK}" stroke-width="3"/>')
    for (x, y) in open_points:
        out.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="10" fill="#fff" stroke="{DARK}" stroke-width="4"/>')
    for (x1, y1, x2, y2, c) in arrows_:
        dx, dy = X(x2) - X(x1), Y(y2) - Y(y1)
        n = math.hypot(dx, dy) or 1
        ux, uy = dx / n, dy / n
        out.append(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2) - ux * 14:.1f}" y2="{Y(y2) - uy * 14:.1f}" stroke="{c}" stroke-width="6" stroke-linecap="round"/>'
                   f'<path d="M{X(x2):.1f} {Y(y2):.1f} L{X(x2) - ux * 22 - uy * 12:.1f} {Y(y2) - uy * 22 + ux * 12:.1f} L{X(x2) - ux * 22 + uy * 12:.1f} {Y(y2) - uy * 22 - ux * 12:.1f} Z" fill="{c}"/>')
    for (x, y, s, c) in texts:
        out.append(f'<text x="{X(x):.1f}" y="{Y(y):.1f}" font-family="{MATHF}" font-size="26" font-weight="700" text-anchor="middle" fill="{c}">{escape(s)}</text>')
    return sized(Item(W, W, ''.join(out)), size)


def bell(mu=0, s=1):
    return lambda x: 4.2 * math.exp(-((x - mu) / s) ** 2 / 2)


def coord(size=320, points=(), quad=None, star_at=None, n=5, first=False, hl_axis=None, origin=False, labels=True, guides=False):
    """A coordinate grid (first quadrant with first=True); points: (x, y) dots; quad: quadrant to shade;
    guides: dashed lines from each point (and the star) to both axes, with its (x, y) written beside it;
    hl_axis: 'x' or 'y' drawn thick red and named at its end."""
    xr = (0, n + 1) if first else (-n - 1, n + 1)
    p = plot(size=size, xr=xr, yr=xr, grid_=True, points=[(x, y, RED) for x, y in points], axis_hl=hl_axis, ticks=True)
    if quad or star_at or origin or (first and labels) or guides or hl_axis in ('x', 'y'):
        W = 300
        X = lambda x: 10 + (x - xr[0]) / (xr[1] - xr[0]) * (W - 20)
        Y = lambda y: 10 + (xr[1] - y) / (xr[1] - xr[0]) * (W - 20)
        extra = ''
        if quad:
            qx, qy = {1: (0, 0), 2: (xr[0], 0), 3: (xr[0], xr[0]), 4: (0, xr[0])}[quad]
            extra += f'<rect x="{X(qx):.1f}" y="{Y(qy + (xr[1] - 0)):.1f}" width="{X(xr[1]) - X(0):.1f}" height="{Y(0) - Y(xr[1]):.1f}" fill="{BLUE}" opacity="0.25"/>'
        if star_at:
            st = star(36)
            extra += g(st, X(star_at[0]) - 18, Y(star_at[1]) - 18)
        if origin:
            extra += f'<circle cx="{X(0):.1f}" cy="{Y(0):.1f}" r="12" fill="{RED}" stroke="{DARK}" stroke-width="3"/>'
        if guides:
            for (px, py) in list(points) + ([star_at] if star_at else []):
                extra = f'<path d="M{X(px):.1f} {Y(0):.1f} V{Y(py):.1f} H{X(0):.1f}" fill="none" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="9 6"/>' + extra
                extra += (f'<rect x="{X(px) + 14:.1f}" y="{Y(py) - 44:.1f}" width="78" height="32" rx="6" fill="#fff" stroke="{RED}" stroke-width="2"/>'
                          f'<text x="{X(px) + 53:.1f}" y="{Y(py) - 20:.1f}" font-family="{MATHF}" font-size="24" font-weight="700" text-anchor="middle" fill="{RED}">({px}, {py})</text>')
        if hl_axis == 'x':
            extra += f'<text x="{W - 14:.1f}" y="{Y(0) - 12:.1f}" font-family="{MATHF}" font-size="36" font-style="italic" font-weight="700" text-anchor="end" fill="{RED}">x</text>'
        if hl_axis == 'y':
            extra += f'<text x="{X(0) + 14:.1f}" y="40" font-family="{MATHF}" font-size="36" font-style="italic" font-weight="700" fill="{RED}">y</text>'
        if first and labels:
            extra += ''.join(f'<text x="{X(v):.1f}" y="{Y(0) + 24:.1f}" font-family="{SANS}" font-size="16" font-weight="700" text-anchor="middle" fill="{DARK}">{v}</text>' for v in range(1, n + 1))
            extra += ''.join(f'<text x="{X(0) - 10:.1f}" y="{Y(v) + 6:.1f}" font-family="{SANS}" font-size="16" font-weight="700" text-anchor="end" fill="{DARK}">{v}</text>' for v in range(1, n + 1))
        k = size / W
        p = Item(p.w, p.h, p.svg + f'<g transform="scale({k:.4f})">{extra}</g>')
    return p


# ---------- shapes and solids ----------

def poly(n=6, size=170, color=BLUE, fill=None, rot=0, marks=False, dots_=False, hl_sides=False, numbered=False):
    pts = [(50 + 44 * math.cos(math.radians(rot - 90 + 360 * k / n)), 52 + 44 * math.sin(math.radians(rot - 90 + 360 * k / n))) for k in range(n)]
    svg = f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill or soft(color)}" stroke="{ORANGE if hl_sides else DARK}" stroke-width="{8 if hl_sides else 5}" stroke-linejoin="round"/>'
    if dots_:
        svg += ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{RED}"/>' for x, y in pts)
    if numbered:
        for k in range(n):
            (xa, ya), (xb, yb) = pts[k], pts[(k + 1) % n]
            mx, my = (xa + xb) / 2, (ya + yb) / 2
            ox, oy = (mx - 50) * 0.28, (my - 52) * 0.28
            svg += f'<text x="{mx + ox:.1f}" y="{my + oy + 5:.1f}" font-family="{SANS}" font-size="14" font-weight="700" text-anchor="middle" fill="{RED}">{k + 1}</text>'
    return _icon(100, 100, svg, size)


def shape(kind, size=150, color=BLUE, fill=None, **kw):
    """circle, square, rectangle, triangle, right, parallelogram, rhombus, trapezoid, kite, oval, heart, star, octagon, pentagon, hexagon."""
    st = f'fill="{fill or color}" stroke="{kw.get("stroke", DARK)}" stroke-width="5" stroke-linejoin="round"'
    if kind == 'circle':
        return _icon(100, 100, f'<circle cx="50" cy="50" r="45" {st}/>', size)
    if kind == 'oval':
        return _icon(140, 90, f'<ellipse cx="70" cy="45" rx="66" ry="40" {st}/>', size)
    if kind == 'square':
        return _icon(100, 100, f'<rect x="5" y="5" width="90" height="90" {st}/>', size)
    if kind == 'rectangle':
        return _icon(150, 90, f'<rect x="5" y="5" width="140" height="80" {st}/>', size)
    if kind == 'triangle':
        return _icon(110, 96, f'<path d="M55 5 L105 91 H5 Z" {st}/>', size)
    if kind == 'right':
        return _icon(110, 96, f'<path d="M5 5 V91 H105 Z" {st}/><path d="M5 73 H23 V91" fill="none" stroke="{DARK}" stroke-width="3"/>', size)
    if kind == 'parallelogram':
        return _icon(150, 90, f'<path d="M35 5 H145 L115 85 H5 Z" {st}/>', size)
    if kind == 'rhombus':
        return _icon(120, 120, f'<path d="M60 5 L115 60 L60 115 L5 60 Z" {st}/>', size)
    if kind == 'trapezoid':
        return _icon(150, 90, f'<path d="M40 5 H110 L145 85 H5 Z" {st}/>', size)
    if kind == 'kite':
        return _icon(100, 130, f'<path d="M50 5 L95 45 L50 125 L5 45 Z" {st}/>', size)
    if kind == 'heart':
        return heart(size, color)
    if kind == 'star':
        return star(size, color)
    n = {'pentagon': 5, 'hexagon': 6, 'octagon': 8}[kind]
    return poly(n, size, color, fill, rot=22.5 if n == 8 else 0)


def triangle(size=200, pts=((10, 150), (190, 150), (70, 20)), color=BLUE, sides=None, angles=(), ticks=None, right_at=None, height=False, labels=None, hl_side=None, base_lab=None, fill=None, theta=None):
    """A triangle; sides: labels per side (side k joins point k and k+1); angles: corners to arc; ticks: tick count per side;
    theta: a corner marked as the reference angle (arc and the letter theta)."""
    svg = f'<polygon points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="{fill or soft(color)}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
    for k in range(3):
        (xa, ya), (xb, yb) = pts[k], pts[(k + 1) % 3]
        if hl_side is not None and k in (hl_side if isinstance(hl_side, (list, tuple)) else (hl_side,)):
            svg += f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="{RED}" stroke-width="10" stroke-linecap="round"/>'
        mx, my = (xa + xb) / 2, (ya + yb) / 2
        cx, cy = sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3
        if sides and sides[k]:
            ux_, uy_ = -(yb - ya), xb - xa  # the side's normal, turned away from the middle of the triangle
            n = math.hypot(ux_, uy_) or 1
            ux_, uy_ = ux_ / n, uy_ / n
            if ux_ * (mx - cx) + uy_ * (my - cy) < 0:
                ux_, uy_ = -ux_, -uy_
            anc = 'start' if ux_ > 0.55 else 'end' if ux_ < -0.55 else 'middle'
            d_ = 12 if anc != 'middle' else 18
            if anc == 'middle' and uy_ < 0:
                d_ = 14
            svg += f'<text x="{mx + ux_ * d_:.1f}" y="{my + uy_ * d_ + 9:.1f}" font-family="{MATHF}" font-size="28" font-weight="700" text-anchor="{anc}" fill="{RED}">{escape(str(sides[k]))}</text>'
        if ticks and ticks[k]:
            dx, dy = xb - xa, yb - ya
            n = math.hypot(dx, dy)
            ux, uy = dx / n, dy / n
            for t in range(ticks[k]):
                off = (t - (ticks[k] - 1) / 2) * 8
                px, py = mx + ux * off, my + uy * off
                svg += f'<line x1="{px - uy * 10:.1f}" y1="{py + ux * 10:.1f}" x2="{px + uy * 10:.1f}" y2="{py - ux * 10:.1f}" stroke="{DARK}" stroke-width="3.5"/>'
    for k in tuple(angles) + ((theta,) if theta is not None and theta not in angles else ()):
        (x, y) = pts[k]
        a1 = math.atan2(pts[(k + 1) % 3][1] - y, pts[(k + 1) % 3][0] - x)
        a2 = math.atan2(pts[(k + 2) % 3][1] - y, pts[(k + 2) % 3][0] - x)
        r = 26
        da = (a2 - a1) % (2 * math.pi)
        sweep = 1 if da < math.pi else 0
        svg += f'<path d="M{x + r * math.cos(a1):.1f} {y + r * math.sin(a1):.1f} A{r} {r} 0 0 {sweep} {x + r * math.cos(a2):.1f} {y + r * math.sin(a2):.1f}" fill="none" stroke="{ORANGE}" stroke-width="5"/>'
        if k == theta:
            am = a1 + (da / 2 if sweep else -((2 * math.pi - da) / 2))
            svg += f'<text x="{x + 46 * math.cos(am):.1f}" y="{y + 46 * math.sin(am) + 9:.1f}" font-family="{MATHF}" font-size="28" font-weight="700" text-anchor="middle" fill="{ORANGE}">θ</text>'
    if right_at is not None:
        (x, y) = pts[right_at]
        p1, p2 = pts[(right_at + 1) % 3], pts[(right_at + 2) % 3]
        u1 = ((p1[0] - x) / math.hypot(p1[0] - x, p1[1] - y), (p1[1] - y) / math.hypot(p1[0] - x, p1[1] - y))
        u2 = ((p2[0] - x) / math.hypot(p2[0] - x, p2[1] - y), (p2[1] - y) / math.hypot(p2[0] - x, p2[1] - y))
        s = 18
        svg += f'<path d="M{x + u1[0] * s:.1f} {y + u1[1] * s:.1f} L{x + u1[0] * s + u2[0] * s:.1f} {y + u1[1] * s + u2[1] * s:.1f} L{x + u2[0] * s:.1f} {y + u2[1] * s:.1f}" fill="none" stroke="{DARK}" stroke-width="3"/>'
    if height:
        (x, y) = pts[2]
        svg += f'<line x1="{x}" y1="{y}" x2="{x}" y2="{pts[0][1]}" stroke="{RED}" stroke-width="4" stroke-dasharray="8 6"/><path d="M{x} {pts[0][1] - 14} h14 v14" fill="none" stroke="{RED}" stroke-width="3"/>'
    if labels:
        for (x, y), l in zip(pts, labels):
            cx, cy = sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3
            ox, oy = x - cx, y - cy
            n = math.hypot(ox, oy) or 1
            svg += f'<text x="{x + ox / n * 24:.1f}" y="{y + oy / n * 24 + 9:.1f}" font-family="{MATHF}" font-size="28" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(l)}</text>'
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return _icon(200, 180, f'<g transform="translate(0 6)">{svg}</g>', size)


def rect_dims(w_=4, h_=3, size=260, units=True, labels=None, color=BLUE, partial=None, hl_row=None, trace=False, arrow_w=False):
    out = []
    cs = 220 / max(w_, h_)
    for r in range(h_):
        for c in range(w_):
            on = units and (partial is None or r * w_ + c < partial)
            out.append(f'<rect x="{20 + c * cs:.1f}" y="{20 + r * cs:.1f}" width="{cs:.1f}" height="{cs:.1f}" fill="{(ORANGE if hl_row == r else soft(color)) if on else "#fff"}" stroke="{DARK if on else LIGHT}" stroke-width="{3 if on else 1.5}"/>')
    out.append(f'<rect x="20" y="20" width="{w_ * cs:.1f}" height="{h_ * cs:.1f}" fill="none" stroke="{RED if trace else DARK}" stroke-width="{8 if trace else 5}"/>')
    if labels:
        out.append(f'<text x="{20 + w_ * cs / 2:.1f}" y="{20 + h_ * cs + 34:.1f}" font-family="{MATHF}" font-size="28" font-weight="700" text-anchor="middle" fill="{RED}">{escape(labels[0])}</text>')
        out.append(f'<text x="{20 + w_ * cs + 12:.1f}" y="{20 + h_ * cs / 2 + 10:.1f}" font-family="{MATHF}" font-size="28" font-weight="700" fill="{RED}">{escape(labels[1])}</text>')
    if arrow_w:
        out.append(f'<line x1="{20 + w_ * cs + 18:.1f}" y1="24" x2="{20 + w_ * cs + 18:.1f}" y2="{16 + h_ * cs:.1f}" stroke="{RED}" stroke-width="5"/><path d="M{20 + w_ * cs + 18:.1f} 20 l-8 14 h16 z M{20 + w_ * cs + 18:.1f} {20 + h_ * cs:.1f} l-8 -14 h16 z" fill="{RED}"/>')
    return sized(Item(20 + w_ * cs + 60, 20 + h_ * cs + 46, ''.join(out)), size)


def circle_parts(size=200, radius=False, diameter=False, chord=False, arc=False, sector=False, tangent=False, inscribed=False, trace=False, center=True, deg=None, radian=False):
    out = [f'<circle cx="100" cy="100" r="80" fill="{soft(BLUE)}" stroke="{RED if trace else DARK}" stroke-width="{9 if trace else 5}"/>']
    if sector:
        out.append(f'<path d="M100 100 L180 100 A80 80 0 0 0 {100 + 80 * math.cos(math.radians(-60)):.1f} {100 + 80 * math.sin(math.radians(-60)):.1f} Z" fill="{ORANGE}" stroke="{DARK}" stroke-width="4"/>')
    if arc or radian:
        a = 57.3 if radian else 70
        out.append(f'<path d="M180 100 A80 80 0 0 0 {100 + 80 * math.cos(math.radians(-a)):.1f} {100 + 80 * math.sin(math.radians(-a)):.1f}" fill="none" stroke="{RED}" stroke-width="10" stroke-linecap="round"/>')
        if radian:
            out.append(f'<line x1="100" y1="100" x2="180" y2="100" stroke="{ORANGE}" stroke-width="6"/><line x1="100" y1="100" x2="{100 + 80 * math.cos(math.radians(-a)):.1f}" y2="{100 + 80 * math.sin(math.radians(-a)):.1f}" stroke="{ORANGE}" stroke-width="6"/>'
                       f'<text x="140" y="125" font-family="{MATHF}" font-size="26" font-weight="700" text-anchor="middle" fill="{ORANGE}">r</text><text x="196" y="50" font-family="{MATHF}" font-size="26" font-weight="700" fill="{RED}">r</text>')
    if radius:
        out.append(f'<line x1="100" y1="100" x2="{100 + 80 * math.cos(math.radians(-35)):.1f}" y2="{100 + 80 * math.sin(math.radians(-35)):.1f}" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>')
    if diameter:
        out.append(f'<line x1="20" y1="100" x2="180" y2="100" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>')
    if chord:
        out.append(f'<line x1="{100 + 80 * math.cos(math.radians(200)):.1f}" y1="{100 + 80 * math.sin(math.radians(200)):.1f}" x2="{100 + 80 * math.cos(math.radians(-30)):.1f}" y2="{100 + 80 * math.sin(math.radians(-30)):.1f}" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>')
    if tangent:
        out.append(f'<line x1="10" y1="20" x2="190" y2="20" stroke="{RED}" stroke-width="7" stroke-linecap="round"/><circle cx="100" cy="20" r="7" fill="{DARK}"/>')
    if inscribed:
        p = [(100 + 80 * math.cos(math.radians(a)), 100 + 80 * math.sin(math.radians(a))) for a in (100, -30, 210)]
        out.append(f'<path d="M{p[1][0]:.1f} {p[1][1]:.1f} L{p[0][0]:.1f} {p[0][1]:.1f} L{p[2][0]:.1f} {p[2][1]:.1f}" fill="none" stroke="{RED}" stroke-width="6" stroke-linejoin="round"/><circle cx="{p[0][0]:.1f}" cy="{p[0][1]:.1f}" r="7" fill="{DARK}"/>')
    if center:
        out.append(f'<circle cx="100" cy="100" r="6" fill="{DARK}"/>')
    if deg:
        out.append(f'<text x="100" y="112" font-family="{SANS}" font-size="34" font-weight="700" text-anchor="middle" fill="{RED}">{deg}</text>')
    return _icon(220 if radian else 200, 200, ''.join(out), size)


def angle(size=200, deg=50, color=ORANGE, right=False, label=None, vertex_dot=False, rays=True):
    a = math.radians(deg)
    out = [f'<line x1="20" y1="150" x2="190" y2="150" stroke="{DARK}" stroke-width="6" stroke-linecap="round"/><line x1="20" y1="150" x2="{20 + 170 * math.cos(a):.1f}" y2="{150 - 170 * math.sin(a):.1f}" stroke="{DARK}" stroke-width="6" stroke-linecap="round"/>']
    if rays:
        out.append(f'<path d="M198 150 l-16 -9 v18 z" fill="{DARK}"/><path d="M{20 + 178 * math.cos(a):.1f} {150 - 178 * math.sin(a):.1f} l{-16 * math.cos(a) + 9 * math.sin(a):.1f} {16 * math.sin(a) + 9 * math.cos(a):.1f} l{-18 * math.sin(a):.1f} {-18 * math.cos(a):.1f} z" fill="{DARK}"/>')
    if right:
        out.append(f'<path d="M20 124 H46 V150" fill="none" stroke="{color}" stroke-width="5"/>')
    else:
        out.append(f'<path d="M70 150 A50 50 0 0 0 {20 + 50 * math.cos(a):.1f} {150 - 50 * math.sin(a):.1f}" fill="none" stroke="{color}" stroke-width="6"/>')
    if vertex_dot:
        out.append(f'<circle cx="20" cy="150" r="11" fill="{RED}" stroke="{DARK}" stroke-width="3"/>')
    if label:
        out.append(f'<text x="{20 + 80 * math.cos(a / 2):.1f}" y="{150 - 80 * math.sin(a / 2) + 10:.1f}" font-family="{SANS}" font-size="28" font-weight="700" fill="{color}">{escape(label)}</text>')
    return _icon(210, 170, ''.join(out), size)


def lines_pair(kind='parallel', size=220, marks=False, transversal=False):
    out = []
    if kind == 'parallel':
        out.append(f'<line x1="10" y1="50" x2="190" y2="50" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/><line x1="10" y1="130" x2="190" y2="130" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/>')
        if transversal:
            out.append(f'<line x1="50" y1="170" x2="150" y2="10" stroke="{ORANGE}" stroke-width="7" stroke-linecap="round"/>')
            out.append(f'<path d="M{106 - 22} 50 A22 22 0 0 0 {106 - 12} {50 + 18}" fill="none" stroke="{RED}" stroke-width="5"/><path d="M{94 + 22} 130 A22 22 0 0 0 {94 + 12} {130 - 18}" fill="none" stroke="{RED}" stroke-width="5"/>')
    elif kind == 'perpendicular':
        out.append(f'<line x1="10" y1="90" x2="190" y2="90" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/><line x1="100" y1="5" x2="100" y2="175" stroke="{ORANGE}" stroke-width="7" stroke-linecap="round"/><path d="M100 66 H124 V90" fill="none" stroke="{RED}" stroke-width="4"/>')
    elif kind == 'cross':
        out.append(f'<line x1="10" y1="30" x2="190" y2="150" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/><line x1="10" y1="150" x2="190" y2="30" stroke="{ORANGE}" stroke-width="7" stroke-linecap="round"/>')
        if marks:
            out.append(f'<path d="M70 70 A36 36 0 0 0 70 110" fill="none" stroke="{RED}" stroke-width="5"/><path d="M130 70 A36 36 0 0 1 130 110" fill="none" stroke="{RED}" stroke-width="5"/>')
    elif kind == 'straight':
        out.append(f'<line x1="10" y1="140" x2="190" y2="140" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/><line x1="100" y1="140" x2="160" y2="30" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/>'
                   f'<path d="M130 140 A30 30 0 0 0 {100 + 30 * math.cos(math.radians(-61)):.1f} {140 + 30 * math.sin(math.radians(-61)):.1f}" fill="none" stroke="{ORANGE}" stroke-width="6"/><path d="M60 140 A40 40 0 0 1 {100 + 40 * math.cos(math.radians(-61)):.1f} {140 + 40 * math.sin(math.radians(-61)):.1f}" fill="none" stroke="{BLUE}" stroke-width="6"/>')
    return _icon(200, 180, ''.join(out), size)


def solid(kind='cube', size=180, color=BLUE, labels=None, hl_face=False, units=None, layers=None, slice_=False):
    """cube, box, prism (triangular), pyramid, cylinder, cone, sphere; units=(l, w, h) draws unit cubes on a box."""
    st = f'stroke="{DARK}" stroke-width="5" stroke-linejoin="round"'
    c1, c2, c3 = soft(color), color, '#ffffff'
    if kind in ('cube', 'box'):
        w_, h_, d_ = (100, 100, 40) if kind == 'cube' else (140, 80, 50)
        if units:
            l, wd, ht = units
            u = 120 / max(l + wd * 0.5, ht + wd * 0.5)
            out = []
            for z in range(ht):
                for yy in range(wd - 1, -1, -1):
                    for x in range(l):
                        X0, Y0 = 10 + x * u + yy * u * 0.5, 10 + (ht - 1 - z) * u + (wd - 1 - yy) * u * 0.5 + 0
                        top = layers and z == ht - 1
                        out.append(f'<path d="M{X0:.1f} {Y0 + u * 0.5:.1f} h{u:.1f} l{u * 0.5:.1f} -{u * 0.5:.1f} h-{u:.1f} z" fill="{c1 if not top else soft(ORANGE)}" stroke="{DARK}" stroke-width="2"/>'
                                   f'<rect x="{X0:.1f}" y="{Y0 + u * 0.5:.1f}" width="{u:.1f}" height="{u:.1f}" fill="{c2 if not top else ORANGE}" stroke="{DARK}" stroke-width="2"/>'
                                   f'<path d="M{X0 + u:.1f} {Y0 + u * 0.5:.1f} l{u * 0.5:.1f} -{u * 0.5:.1f} v{u:.1f} l-{u * 0.5:.1f} {u * 0.5:.1f} z" fill="{soft(DARK)}" stroke="{DARK}" stroke-width="2"/>')
            return _icon(10 + (l + wd * 0.5) * u + 10, 10 + (ht + wd * 0.5) * u + 10, ''.join(out), size)
        svg = (f'<rect x="10" y="{10 + d_}" width="{w_}" height="{h_}" fill="{ORANGE if hl_face else c2}" {st}/>'
               f'<path d="M10 {10 + d_} L{10 + d_} 10 H{10 + d_ + w_} L{10 + w_} {10 + d_} Z" fill="{c1}" {st}/>'
               f'<path d="M{10 + w_} {10 + d_} L{10 + w_ + d_} 10 V{10 + h_} L{10 + w_} {10 + d_ + h_} Z" fill="{soft(DARK)}" {st}/>')
        if hl_face == 'bottom':
            svg = svg.replace(f'fill="{ORANGE}"', f'fill="{c2}"') + f'<path d="M10 {10 + d_ + h_} L{10 + d_} {10 + h_} H{10 + d_ + w_} L{10 + w_} {10 + d_ + h_} Z" fill="{ORANGE}" opacity="0.8" {st}/>'
        if labels:
            svg += (f'<text x="{10 + w_ / 2}" y="{10 + d_ + h_ + 32}" font-family="{MATHF}" font-size="28" font-weight="700" text-anchor="middle" fill="{RED}">{labels[0]}</text>'
                    f'<text x="{10 + w_ + d_ / 2 + 16}" y="{10 + d_ + h_ - 6}" font-family="{MATHF}" font-size="28" font-weight="700" fill="{RED}">{labels[1]}</text>'
                    f'<text x="-6" y="{10 + d_ + h_ / 2 + 10}" font-family="{MATHF}" font-size="28" font-weight="700" text-anchor="end" fill="{RED}">{labels[2]}</text>')
        return _icon(20 + w_ + d_ + (90 if labels else 0), 20 + h_ + d_ + (40 if labels else 0), f'<g transform="translate({50 if labels else 0} 0)">{svg}</g>', size)
    if kind == 'prism':
        svg = (f'<path d="M10 120 L60 30 L110 120 Z" fill="{c2}" {st}/><path d="M60 30 L150 10 L200 100 L110 120 Z" fill="{c1}" {st}/>'
               f'<path d="M110 120 L200 100" fill="none" {st}/><path d="M10 120 L100 100 L150 10" fill="none" stroke="{DARK}" stroke-width="3" stroke-dasharray="7 6"/><path d="M100 100 L200 100" fill="none" stroke="{DARK}" stroke-width="3" stroke-dasharray="7 6"/>')
        if hl_face:
            svg += f'<path d="M10 120 L60 30 L110 120 Z" fill="{ORANGE}" opacity="0.6"/>'
        return _icon(210, 130, svg, size)
    if kind == 'pyramid':
        return _icon(180, 160, f'<path d="M20 120 L110 140 L160 110 L90 10 Z" fill="{c1}" {st}/><path d="M20 120 L110 140 L90 10 Z" fill="{c2}" {st}/><path d="M20 120 L70 92 L160 110 M70 92 L90 10" fill="none" stroke="{DARK}" stroke-width="3" stroke-dasharray="7 6"/>', size)
    if kind == 'cylinder':
        svg = f'<path d="M10 30 V130 A60 18 0 0 0 130 130 V30" fill="{c2}" {st}/><ellipse cx="70" cy="30" rx="60" ry="18" fill="{c1}" {st}/>'
        if slice_:
            svg += f'<ellipse cx="70" cy="80" rx="60" ry="18" fill="{ORANGE}" stroke="{DARK}" stroke-width="4" opacity="0.9"/>'
        if labels:
            svg += (f'<line x1="70" y1="30" x2="130" y2="30" stroke="{RED}" stroke-width="4"/><circle cx="70" cy="30" r="4" fill="{RED}"/>'
                    f'<path d="M100 26 V2" stroke="{RED}" stroke-width="2.5"/><text x="100" y="-4" font-family="{MATHF}" font-size="26" font-weight="700" text-anchor="middle" fill="{RED}">{labels[0]}</text>')
            svg += f'<text x="146" y="90" font-family="{MATHF}" font-size="26" font-weight="700" fill="{RED}">{labels[1]}</text>'
            return _icon(170, 190, f'<g transform="translate(0 30)">{svg}</g>', size)
        return _icon(140, 160, svg, size)
    if kind == 'cone':
        svg = f'<path d="M10 130 L70 10 L130 130" fill="{c2}" {st}/><ellipse cx="70" cy="130" rx="60" ry="18" fill="{c1}" {st}/>'
        if slice_:
            svg += f'<ellipse cx="70" cy="80" rx="35" ry="10" fill="{ORANGE}" stroke="{DARK}" stroke-width="4"/>'
        return _icon(140, 154, svg, size)
    if kind == 'sphere':
        return _icon(120, 120, f'<circle cx="60" cy="60" r="54" fill="{c2}" {st}/><ellipse cx="60" cy="60" rx="54" ry="16" fill="none" stroke="{DARK}" stroke-width="3" stroke-dasharray="7 6"/><circle cx="40" cy="38" r="12" fill="#fff" opacity="0.5"/>', size)
    raise ValueError(kind)


# ---------- waves, maps and the rest ----------

def wave(size=360, cycles=2, amp=1.0, square=False, marks=None, color=BLUE, midline=False, second=None, packed=1.0, decay=False, arrows_=None):
    """A sine (or square) wave. marks: 'amplitude', 'wavelength', 'period'; second: (amp, shift, color) another wave."""
    W, Hh = 400, 200
    cy = 100
    out = []
    if midline:
        out.append(f'<line x1="0" y1="{cy}" x2="{W}" y2="{cy}" stroke="{GRAY}" stroke-width="4" stroke-dasharray="12 8"/>')

    def wpath(a, shift, c, cyc):
        pts = []
        for i in range(201):
            x = W * i / 200
            t = 2 * math.pi * cyc * packed * i / 200 + shift
            y = math.copysign(1, math.sin(t)) if square else math.sin(t)
            if decay:
                y *= math.exp(-2.2 * i / 200)
            pts.append((x, cy - a * 70 * y))
        return '<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + f'" fill="none" stroke="{c}" stroke-width="7" stroke-linejoin="round"/>'
    out.append(wpath(amp, 0, color, cycles))
    if second:
        out.append(wpath(second[0], second[1], second[2], cycles))
    if marks == 'amplitude':
        x = W / (4 * cycles * packed)
        out.append(f'<line x1="{x:.1f}" y1="{cy}" x2="{x:.1f}" y2="{cy - amp * 70:.1f}" stroke="{RED}" stroke-width="5"/><line x1="0" y1="{cy}" x2="{W}" y2="{cy}" stroke="{GRAY}" stroke-width="3" stroke-dasharray="10 7"/>'
                   f'<path d="M{x:.1f} {cy - amp * 70:.1f} l-8 14 h16 z" fill="{RED}"/>')
    if marks in ('wavelength', 'period'):
        x0, x1 = W / (4 * cycles * packed), W / (4 * cycles * packed) + W / (cycles * packed)
        y = cy - amp * 70 - 18
        out.append(f'<path d="M{x0:.1f} {y + 10:.1f} V{y:.1f} H{x1:.1f} V{y + 10:.1f}" fill="none" stroke="{RED}" stroke-width="5"/>')
    if arrows_:
        for i in range(4):
            x = 40 + i * 100
            out.append(f'<path d="M{x} {cy - 30} V{cy + 30} M{x} {cy - 40} l-8 12 h16 z M{x} {cy + 40} l-8 -12 h16 z" stroke="{RED}" stroke-width="4" fill="{RED}"/>')
    return sized(Item(W, Hh, f'<g transform="translate(0 0)">' + ''.join(out) + '</g>'), size)


def spring(size=380, bands=True):
    out = []
    for i in range(30):
        x = 10 + i * 12.5 + (8 * math.sin(i * 0.6) if bands else 0)
        out.append(f'<ellipse cx="{x:.1f}" cy="60" rx="5" ry="40" fill="none" stroke="{BLUE if (i // 5) % 2 == 0 else ORANGE}" stroke-width="4"/>')
    return _icon(400, 120, ''.join(out), size)


def us_map(size=420, shade=(), color=BLUE, line=None, split=False, arrows_=(), labels=False):
    """US states (from tools/me-on-the-map). shade: postal codes to fill; split: shade north and south apart."""
    states = json.loads((ROOT / 'tools' / 'me-on-the-map' / 'states.json').read_text(encoding='utf-8'))
    SOUTH = set('TX OK AR LA MS AL GA FL SC NC TN KY VA WV MD DE'.split())
    out = []
    for st in states:
        f = soft(color)
        if st['a'] in shade:
            f = color
        if split:
            f = ORANGE if st['a'] in SOUTH else BLUE
        out.append(f'<path d="{st["d"]}" fill="{f}" stroke="#fff" stroke-width="1.5"/>')
    if line:
        out.append(f'<path d="{line}" fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="12 8"/>')
    for (x1, y1, x2, y2) in arrows_:
        dx, dy = x2 - x1, y2 - y1
        n = math.hypot(dx, dy)
        ux, uy = dx / n, dy / n
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2 - ux * 18:.1f}" y2="{y2 - uy * 18:.1f}" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>'
                   f'<path d="M{x2} {y2} L{x2 - ux * 26 - uy * 15:.1f} {y2 - uy * 26 + ux * 15:.1f} L{x2 - ux * 26 + uy * 15:.1f} {y2 - uy * 26 - ux * 15:.1f} Z" fill="{RED}"/>')
    return sized(Item(900, 560, f'<g transform="translate(-10 -20)">' + ''.join(out) + '</g>'), size)


_WORLD = None


def world_map(size=440, color=GREEN, shade=None, arrows_=(), pins=(), sea='#e3eff6', continents=False, lines=False, view=None, polys=(),
              flows=(), borders=(), land=None, labels=()):
    """The world in Equal Earth (land from tools/art-passport). shade: [(lon0, lat0, lon1, lat1)] boxes colored over the land;
    arrows_: [(lon1, lat1, lon2, lat2)]; pins: [(lon, lat)]. view: (lon0, lat0, lon1, lat1) zooms to that part of the world;
    polys: [([(lon, lat), ...], color)] areas colored over the land; flows: [([(lon, lat), ...], color, width)] thick arrows
    along a path (winds, currents, trade routes); borders: [[(lon, lat), ...]] lines drawn over the land; land: land color."""
    global _WORLD
    if _WORLD is None:
        _WORLD = json.loads((ROOT / 'tools' / 'art-passport' / 'world.json').read_text(encoding='utf-8'))
    w = _WORLD
    import charts as ch
    P = lambda lon, lat: ch.equal_earth(w, lon, lat)
    mh = 2 * w['ymax'] * w['s']
    edge = [P(-180, lat) for lat in range(-90, 91, 5)] + [P(180, lat) for lat in range(90, -91, -5)]
    out = [f'<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in edge) + f' Z" fill="{sea}" stroke="{DARK}" stroke-width="3"/>']
    out.append(f'<defs><clipPath id="land"><path d="{w["d"]}"/></clipPath></defs>')
    out.append(f'<path d="{w["d"]}" fill="{land or (soft(color) if (shade or continents or polys) else color)}" stroke="{DARK}" stroke-width="1.2"/>')
    zk = 1.0
    if view:
        vx = [P(view[0] + (view[2] - view[0]) * t / 8, view[1] + (view[3] - view[1]) * u / 8) for t in range(9) for u in range(9)]
        bx0, bx1 = min(x for x, _ in vx), max(x for x, _ in vx)
        by0, by1 = min(y for _, y in vx), max(y for _, y in vx)
        zk = (bx1 - bx0) / w['w']
    for pts_, col_ in polys:
        out.append(f'<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in (P(lo, la) for lo, la in pts_)) + f' Z" fill="{col_}" clip-path="url(#land)"/>')
    for pts_ in borders:
        out.append(f'<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in (P(lo, la) for lo, la in pts_)) + f'" fill="none" stroke="{DARK}" stroke-width="{2.2 * zk:.2f}" stroke-linejoin="round" clip-path="url(#land)"/>')
    if continents:
        boxes = [((-170, 10, -50, 80), ORANGE), ((-90, -60, -30, 12), YELLOW), ((-20, -40, 55, 37), BROWN), ((-12, 36, 40, 72), BLUE), ((40, 0, 180, 80), RED), ((110, -45, 160, -10), PURPLE), ((26, 36, 45, 75), BLUE)]
        for (a, b, c, d), col_ in boxes:
            pts = [P(a, b), P(a, d), P(c, d), P(c, b)]
            out.append(f'<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + f' Z" fill="{col_}" clip-path="url(#land)"/>')
    for i, box_ in enumerate(shade or ()):
        a, b, c, d = box_[:4]
        col_ = box_[4] if len(box_) > 4 else color
        pts = [P(a + (c - a) * t / 10, b) for t in range(11)] + [P(c, b + (d - b) * t / 10) for t in range(11)] + [P(c - (c - a) * t / 10, d) for t in range(11)] + [P(a, d - (d - b) * t / 10) for t in range(11)]
        out.append(f'<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + f' Z" fill="{col_}" clip-path="url(#land)"/>')
    if lines:
        for lat in range(-60, 61, 30):
            x1, y1 = P(-180, lat)
            x2, _ = P(180, lat)
            out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y1:.1f}" stroke="{DARK}" stroke-width="1.5" opacity="0.6"/>')
    for (lo1, la1, lo2, la2) in arrows_:
        (x1, y1), (x2, y2) = P(lo1, la1), P(lo2, la2)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - abs(x2 - x1) * 0.15
        ux, uy = x2 - mx, y2 - my
        n = math.hypot(ux, uy) or 1
        ux, uy = ux / n, uy / n
        out.append(f'<path d="M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2 - ux * 14:.1f} {y2 - uy * 14:.1f}" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>'
                   f'<path d="M{x2:.1f} {y2:.1f} L{x2 - ux * 26 - uy * 15:.1f} {y2 - uy * 26 + ux * 15:.1f} L{x2 - ux * 26 + uy * 15:.1f} {y2 - uy * 26 - ux * 15:.1f} Z" fill="{RED}"/>')
    for pts_, col_, sw_ in flows:
        xy = [P(lo, la) for lo, la in pts_]
        sw_ = sw_ * zk
        (xa, ya), (xb, yb) = xy[-2], xy[-1]
        n = math.hypot(xb - xa, yb - ya) or 1
        ux, uy = (xb - xa) / n, (yb - ya) / n
        hl_, hw = sw_ * 2.6, sw_ * 1.7
        body = xy[:-1] + [(xb - ux * hl_ * 0.8, yb - uy * hl_ * 0.8)]
        out.append(f'<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in body) + f'" fill="none" stroke="{col_}" stroke-width="{sw_:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'
                   f'<path d="M{xb:.1f} {yb:.1f} L{xb - ux * hl_ - uy * hw:.1f} {yb - uy * hl_ + ux * hw:.1f} L{xb - ux * hl_ + uy * hw:.1f} {yb - uy * hl_ - ux * hw:.1f} Z" fill="{col_}"/>')
    for (lo, la) in pins:
        x, y = P(lo, la)
        out.append(g(pin(50 * zk), x - 15 * zk, y - 46 * zk))
    for (lo, la, txt, col_, fs) in labels:  # fs: the text size in pixels of the finished picture
        x, y = P(lo, la)
        fs = fs * zk * w['w'] / size
        out.append(f'<text x="{x:.1f}" y="{y + fs * 0.35:.1f}" font-family="{SANS}" font-size="{fs:.1f}" font-weight="700" text-anchor="middle" fill="{col_}" '
                   f'stroke="#fff" stroke-width="{fs * 0.22:.1f}" paint-order="stroke" stroke-linejoin="round">{escape(txt)}</text>')
    if view:
        vw, vh = bx1 - bx0, by1 - by0
        return sized(Item(vw, vh, f'<svg x="0" y="0" width="{vw:.1f}" height="{vh:.1f}" viewBox="{bx0:.1f} {by0:.1f} {vw:.1f} {vh:.1f}" overflow="hidden">' + ''.join(out) + '</svg>'), size)
    return sized(Item(w['w'], mh, ''.join(out)), size)


def map_tile(size=300, roads=True, river=False, lakes=False, pins=(), grid_=False, legend=False, scale_bar=False, color=GREEN, houses=()):
    """A simple made-up map: green land, roads, a river, lakes, map pins, a lettered grid."""
    out = [f'<rect x="4" y="4" width="292" height="232" rx="10" fill="#e9f3dc" stroke="{DARK}" stroke-width="5"/>']
    if river:
        out.append(f'<path d="M150 6 C130 60 180 90 150 140 C120 190 160 210 150 234" fill="none" stroke="{BLUE}" stroke-width="14"/>')
    if lakes:
        out.append(f'<ellipse cx="80" cy="70" rx="44" ry="26" fill="{soft(BLUE)}" stroke="{BLUE}" stroke-width="4"/><ellipse cx="220" cy="170" rx="38" ry="22" fill="{soft(BLUE)}" stroke="{BLUE}" stroke-width="4"/>')
    if roads:
        out.append(f'<path d="M4 120 H296 M200 4 V236" stroke="#b9b2a6" stroke-width="14"/><path d="M4 120 H296 M200 4 V236" stroke="#fff" stroke-width="2" stroke-dasharray="10 8"/>')
    for (x, y) in houses:
        out.append(g(house(46), x, y))
    if grid_:
        for i in range(1, 4):
            out.append(f'<line x1="{4 + i * 73}" y1="4" x2="{4 + i * 73}" y2="236" stroke="{DARK}" stroke-width="2"/><line x1="4" y1="{4 + i * 58}" x2="296" y2="{4 + i * 58}" stroke="{DARK}" stroke-width="2"/>')
        out.append(''.join(f'<text x="{40 + i * 73}" y="-6" font-family="{SANS}" font-size="22" font-weight="700" text-anchor="middle" fill="{DARK}">{"ABCD"[i]}</text>' for i in range(4)))
        out.append(''.join(f'<text x="-8" y="{40 + i * 58}" font-family="{SANS}" font-size="22" font-weight="700" text-anchor="end" fill="{DARK}">{i + 1}</text>' for i in range(4)))
    for (x, y) in pins:
        out.append(g(pin(46), x - 16, y - 46))
    if scale_bar:
        out.append(f'<rect x="20" y="200" width="100" height="12" fill="#fff" stroke="{DARK}" stroke-width="3"/><rect x="20" y="200" width="50" height="12" fill="{DARK}"/><text x="70" y="194" font-family="{SANS}" font-size="16" font-weight="700" text-anchor="middle" fill="{DARK}">0   1   2 km</text>')
    return sized(Item(300, 240, f'<g transform="translate({24 if grid_ else 0} {24 if grid_ else 0})">' + ''.join(out) + '</g>'), size)


def legend_box(size=260, items=('tree', 'house', 'road')):
    rows_ = []
    for k in items:
        sym = {'tree': tree(40), 'house': house(40), 'road': Item(60, 20, f'<line x1="0" y1="10" x2="60" y2="10" stroke="#b9b2a6" stroke-width="12"/><line x1="0" y1="10" x2="60" y2="10" stroke="#fff" stroke-width="2" stroke-dasharray="8 6"/>'),
               'water': Item(60, 30, f'<rect x="2" y="2" width="56" height="26" rx="6" fill="{soft(BLUE)}" stroke="{BLUE}" stroke-width="3"/>')}[k]
        rows_.append(row(sized(sym, 60, 44), Item(110, 16, f'<rect x="0" y="4" width="100" height="10" rx="5" fill="{GRAY}"/>'), gap=16))
    return box(col(*rows_, gap=12, align='l'), color=DARK, fill='#fff', p=18)


def scale_bar(size=320, labels=('0', '1', '2', '3 km')):
    out = []
    for i in range(3):
        out.append(f'<rect x="{10 + i * 100}" y="40" width="100" height="22" fill="{DARK if i % 2 == 0 else "#fff"}" stroke="{DARK}" stroke-width="4"/>')
    for i, l in enumerate(labels):
        out.append(f'<text x="{10 + i * 100}" y="30" font-family="{SANS}" font-size="24" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(l)}</text>')
    return _icon(330, 70, f'<g transform="translate(10 0)">' + ''.join(out) + '</g>', size)


def timeline(n=4, size=420, labels=None, hl=None, dots_=True, arrow_end=True, now=None, segment=None, wavy=None, repeated=False, back=False, pics=None, closed=None, keep_going=None, check_at=None):
    """A timeline: n dots; labels under them; hl: index circled; now: index marked NOW; segment: (i, j) a bar;
    wavy: (i, j) a wavy stretch; back: an arrow pointing back from now."""
    W = 460
    xs = [40 + i * (W - 100) / max(1, n - 1) for i in range(n)]
    y = 80
    out = [f'<line x1="20" y1="{y}" x2="{W - 30}" y2="{y}" stroke="{DARK}" stroke-width="9" stroke-linecap="round"/>']
    if arrow_end:
        out.append(f'<path d="M{W - 10} {y} l-30 -17 v34 z" fill="{DARK}"/>')
    if segment:
        out.append(f'<line x1="{xs[segment[0]]:.1f}" y1="{y}" x2="{xs[segment[1]]:.1f}" y2="{y}" stroke="{ORANGE}" stroke-width="14" stroke-linecap="round"/>'
                   + ''.join(f'<line x1="{xs[k]:.1f}" y1="{y - 20}" x2="{xs[k]:.1f}" y2="{y + 20}" stroke="{ORANGE}" stroke-width="6"/>' for k in segment))
    if wavy:
        x0, x1 = xs[wavy[0]], xs[wavy[1]]
        out.append('<path d="M' + ' L'.join(f'{x0 + (x1 - x0) * t / 60:.1f} {y - 14 * math.sin(t / 60 * 6 * math.pi) - 28:.1f}' for t in range(61)) + f'" fill="none" stroke="{ORANGE}" stroke-width="6"/>')
    if keep_going is not None:
        out.append(f'<line x1="{xs[keep_going]:.1f}" y1="{y - 26}" x2="{W - 30}" y2="{y - 26}" stroke="{ORANGE}" stroke-width="8"/><path d="M{W - 16} {y - 26} l-18 -11 v22 z" fill="{ORANGE}"/>')
    if back:
        out.append(f'<line x1="{xs[now if now is not None else -1]:.1f}" y1="{y - 30}" x2="{xs[0] + 10:.1f}" y2="{y - 30}" stroke="{ORANGE}" stroke-width="8"/><path d="M{xs[0] - 6:.1f} {y - 30} l18 -11 v22 z" fill="{ORANGE}"/>')
    for i, x in enumerate(xs):
        if dots_:
            c = RED if (hl == i or now == i or closed == i) else (BLUE if not repeated else ORANGE)
            out.append(f'<circle cx="{x:.1f}" cy="{y}" r="{20 if (hl == i or now == i) else 15}" fill="{c}" stroke="{DARK}" stroke-width="3"/>')
        if hl == i:
            out.append(f'<circle cx="{x:.1f}" cy="{y}" r="32" fill="none" stroke="{RED}" stroke-width="5"/>')
        if labels and i < len(labels) and labels[i]:
            fs = min(38, (W - 60) / n / max(0.5, measure(labels[i], 1, True)) * 0.95)
            out.append(f'<text x="{x:.1f}" y="{y + 58}" font-family="{SANS}" font-size="{fs:.1f}" font-weight="700" text-anchor="middle" fill="{RED if now == i else DARK}">{escape(labels[i])}</text>')
        if pics and i < len(pics) and pics[i] is not None:
            p = sized(pics[i], 56, 56)
            out.append(g(p, x - p.w / 2, y - 76))
    if check_at is not None:
        out.append(g(check(40), xs[check_at] - 20, y - 70))
    return sized(Item(W, 150, f'<g transform="translate(0 {20 if pics else 0})">' + ''.join(out) + '</g>'), size)


def flowchart(size=300, labels=('Start', '?', 'Yes', 'No')):
    out = []
    out.append(g(box(T(labels[0], 26), w=130, h=54, color=BLUE, rx=27), 85, 0))
    out.append(f'<line x1="150" y1="54" x2="150" y2="80" stroke="{DARK}" stroke-width="5"/><path d="M150 88 l-9 -12 h18 z" fill="{DARK}"/>')
    out.append(f'<path d="M150 90 L210 140 L150 190 L90 140 Z" fill="{soft(ORANGE)}" stroke="{ORANGE}" stroke-width="5"/>')
    out.append(f'<text x="150" y="152" font-family="{SANS}" font-size="34" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(labels[1])}</text>')
    out.append(f'<path d="M90 140 H40 V210 M210 140 H260 V210" fill="none" stroke="{DARK}" stroke-width="5"/><path d="M40 218 l-9 -12 h18 z M260 218 l-9 -12 h18 z" fill="{DARK}"/>')
    out.append(g(box(T(labels[2], 24), w=100, h=50, color=GREEN), -10, 220) + g(box(T(labels[3], 24), w=100, h=50, color=RED), 210, 220))
    return sized(Item(320, 274, f'<g transform="translate(10 2)">' + ''.join(out) + '</g>'), size)


def diamond(size=200, text=None, color=ORANGE, yes_no=False):
    out = [f'<path d="M100 10 L190 80 L100 150 L10 80 Z" fill="{soft(color)}" stroke="{color}" stroke-width="6" stroke-linejoin="round"/>']
    if text:
        out.append(f'<text x="100" y="94" font-family="{SANS}" font-size="38" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(text)}</text>')
    if yes_no:
        out.append(f'<path d="M10 80 H-40 V150 M190 80 H240 V150" fill="none" stroke="{DARK}" stroke-width="5"/><path d="M-40 160 l-9 -14 h18 z M240 160 l-9 -14 h18 z" fill="{DARK}"/>'
                   f'<text x="-40" y="196" font-family="{SANS}" font-size="30" font-weight="700" text-anchor="middle" fill="{GREEN}">yes</text><text x="240" y="196" font-family="{SANS}" font-size="30" font-weight="700" text-anchor="middle" fill="{RED}">no</text>')
        return _icon(320, 210, f'<g transform="translate(60 0)">' + ''.join(out) + '</g>', size)
    return _icon(200, 160, ''.join(out), size)


def machine(size=320, inp=None, outp=None, label='f', color=PURPLE):
    m = box(T(label, 54, '#fff', font=MATHF, italic=True), w=150, h=120, color=color, fill=color)
    gear_ = sized(gear(40, '#fff'), 34)
    m = Item(m.w, m.h, m.svg + g(gear_, m.w - 40, 8))
    parts = []
    if inp is not None:
        parts += [it(inp) if isinstance(inp, Item) else T(inp, 54), arrow(60)]
    else:
        parts += [arrow(70, text='in')]
    parts.append(m)
    if outp is not None:
        parts += [arrow(60), it(outp) if isinstance(outp, Item) else T(outp, 54)]
    else:
        parts += [arrow(70, text='out')]
    return row(*parts, gap=6)


def tree_diagram(size=320, levels=(2, 2), labels=None):
    out = []
    W, Hh = 300, 220
    nodes = [[(20, Hh / 2)]]
    for li, k in enumerate(levels):
        prev = nodes[-1]
        cnt = len(prev) * k
        xs = 20 + (li + 1) * (W - 40) / len(levels)
        new = [(xs, 20 + (Hh - 40) * (i + 0.5) / cnt) for i in range(cnt)]
        for i, (x, y) in enumerate(new):
            px, py = prev[i // k]
            out.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{DARK}" stroke-width="4"/>')
        nodes.append(new)
    for li, lv in enumerate(nodes):
        for i, (x, y) in enumerate(lv):
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="{[DARK, BLUE, ORANGE, GREEN][li % 4]}" stroke="{DARK}" stroke-width="2"/>')
            if labels and li > 0:
                lab = labels[li - 1][i % len(labels[li - 1])]
                out.append(f'<text x="{x + 18:.1f}" y="{y + 7:.1f}" font-family="{SANS}" font-size="20" font-weight="700" fill="{DARK}">{escape(lab)}</text>')
    return sized(Item(W + 40, Hh, ''.join(out)), size)


def branch_tree(size=320, leaves=4, labels=None, cladogram=False):
    out = []
    W, Hh = 300, 220
    xs = [30 + i * (W - 60) / (leaves - 1) for i in range(leaves)]
    if cladogram:
        out.append(f'<line x1="30" y1="200" x2="{W - 30}" y2="20" stroke="{DARK}" stroke-width="5"/>')
        for i, x in enumerate(xs):
            yb = 200 - (x - 30) / (W - 60) * 180
            if i:
                out.append(f'<line x1="{(x + xs[i - 1]) / 2 if i < leaves - 1 else x:.1f}" y1="{200 - ((x + xs[i - 1]) / 2 - 30) / (W - 60) * 180 if i < leaves - 1 else yb:.1f}" x2="{x - 40 if i < leaves - 1 else x:.1f}" y2="20" stroke="{DARK}" stroke-width="5"/>')
        for i, x in enumerate(xs):
            out.append(f'<circle cx="{x - (40 if 0 < i < leaves - 1 else (0 if i else -0)):.1f}" cy="20" r="11" fill="{[BLUE, ORANGE, GREEN, PURPLE, RED][i % 5]}" stroke="{DARK}" stroke-width="3"/>')
        return sized(Item(W, Hh, ''.join(out)), size)
    out.append(f'<line x1="{W / 2}" y1="210" x2="{W / 2}" y2="150" stroke="{BROWN}" stroke-width="8"/>')
    mid = [(W / 4 + 10, 90), (3 * W / 4 - 10, 90)]
    for mx, my in mid:
        out.append(f'<line x1="{W / 2}" y1="150" x2="{mx}" y2="{my}" stroke="{BROWN}" stroke-width="7"/>')
    for i, x in enumerate(xs):
        mx, my = mid[0] if x < W / 2 else mid[1]
        out.append(f'<line x1="{mx}" y1="{my}" x2="{x:.1f}" y2="26" stroke="{BROWN}" stroke-width="5"/><circle cx="{x:.1f}" cy="22" r="14" fill="{[BLUE, ORANGE, GREEN, PURPLE, RED][i % 5]}" stroke="{DARK}" stroke-width="3"/>')
    return sized(Item(W, Hh, ''.join(out)), size)


def pyramid_levels(n=4, size=300, labels=None, colors=(GREEN, YELLOW, ORANGE, RED, PURPLE), blocks=False):
    out = []
    W, Hh = 300, 240
    for i in range(n):
        y0, y1 = Hh - (i + 1) * Hh / n, Hh - i * Hh / n
        hw0, hw1 = (W / 2) * (1 - (i + 1) / n) if not blocks else (W / 2) * (1 - i / n) * 0.95, (W / 2) * (1 - i / n)
        if blocks:
            out.append(f'<rect x="{W / 2 - hw1 * 0.95:.1f}" y="{y0 + 2:.1f}" width="{2 * hw1 * 0.95:.1f}" height="{y1 - y0 - 4:.1f}" rx="4" fill="{colors[i % len(colors)]}" stroke="{DARK}" stroke-width="4"/>')
        else:
            out.append(f'<path d="M{W / 2 - hw1:.1f} {y1:.1f} L{W / 2 - hw0:.1f} {y0:.1f} L{W / 2 + hw0:.1f} {y0:.1f} L{W / 2 + hw1:.1f} {y1:.1f} Z" fill="{colors[i % len(colors)]}" stroke="{DARK}" stroke-width="4" stroke-linejoin="round"/>')
        if labels:
            out.append(f'<text x="{W / 2}" y="{(y0 + y1) / 2 + 8:.1f}" font-family="{SANS}" font-size="20" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(labels[i])}</text>')
    return sized(Item(W, Hh, ''.join(out)), size)


def pop_pyramid(size=300):
    out = []
    widths = [120, 112, 100, 88, 72, 56, 38, 20]
    for i, w_ in enumerate(widths):
        y = 200 - i * 24
        out.append(f'<rect x="{150 - w_:.1f}" y="{y}" width="{w_}" height="20" fill="{BLUE}" stroke="{DARK}" stroke-width="2"/><rect x="150" y="{y}" width="{w_ * 0.96:.1f}" height="20" fill="{PINK}" stroke="{DARK}" stroke-width="2"/>')
    return _icon(300, 230, ''.join(out), size)


def orbit(size=320, center=None, body=None, ellipse_=False, rings=1, foci=False, sun_size=60, angle=-30, arrow_=True):
    W, Hh = 340, 260
    rx, ry = (140, 90) if ellipse_ else (120, 100)
    out = []
    for k in range(rings):
        f = 1 - k * (0.85 / max(1, rings))
        out.append(f'<ellipse cx="{W / 2}" cy="{Hh / 2}" rx="{rx * f:.1f}" ry="{ry * f:.1f}" fill="none" stroke="{GRAY}" stroke-width="3" stroke-dasharray="{"" if rings > 1 else "10 8"}"/>')
    c = math.sqrt(max(0, rx ** 2 - ry ** 2)) if ellipse_ else 0
    cx = W / 2 - c * 0.9
    if center is not None:
        cc = sized(center, sun_size, sun_size)
        out.append(g(cc, cx - cc.w / 2, Hh / 2 - cc.h / 2))
    if foci:
        out.append(f'<circle cx="{W / 2 - c:.1f}" cy="{Hh / 2}" r="7" fill="{DARK}"/><circle cx="{W / 2 + c:.1f}" cy="{Hh / 2}" r="7" fill="{DARK}"/>')
    if body is not None:
        a = math.radians(angle)
        bx, by = W / 2 + rx * math.cos(a), Hh / 2 + ry * math.sin(a)
        bb = sized(body, 46, 46)
        out.append(g(bb, bx - bb.w / 2, by - bb.h / 2))
        if arrow_:
            a2 = a + 0.5
            ex, ey = W / 2 + rx * math.cos(a2), Hh / 2 + ry * math.sin(a2)
            out.append(f'<path d="M{ex:.1f} {ey:.1f} l{-14 * math.sin(a2) - 8:.1f} {14 * math.cos(a2) - 10:.1f}" stroke="{DARK}" stroke-width="0"/>')
    return sized(Item(W, Hh, ''.join(out)), size)


def earth(size=80):
    return globe(size)


def solar_system(size=420):
    W, Hh = 440, 300
    out = [f'<circle cx="{W / 2}" cy="{Hh / 2}" r="26" fill="{YELLOW}" stroke="{DARK}" stroke-width="4"/>']
    cols = ['#b8b1a8', '#e7c27a', BLUE, RED, '#d9a066', '#e8d29a', '#9fd6e0', '#4f7fd8']
    for i in range(8):
        rx, ry = 44 + i * 23, 30 + i * 15.5
        out.append(f'<ellipse cx="{W / 2}" cy="{Hh / 2}" rx="{rx}" ry="{ry}" fill="none" stroke="{GRAY}" stroke-width="2"/>')
        a = i * 0.8 + 0.3
        out.append(f'<circle cx="{W / 2 + rx * math.cos(a):.1f}" cy="{Hh / 2 + ry * math.sin(a):.1f}" r="{[5, 7, 7, 6, 13, 12, 9, 9][i]}" fill="{cols[i]}" stroke="{DARK}" stroke-width="2"/>')
    return sized(Item(W, Hh, ''.join(out)), size)


def layers(n=5, size=300, colors=('#d9a066', '#c98b4f', '#e7c27a', '#a7744b', '#8f6a4f', '#c2a37c'), fossils=(), labels=None, water_=False, arrow_bottom=False):
    out = []
    W, Hh = 300, 220
    lh = Hh / n
    for i in range(n):
        y = i * lh
        out.append(f'<path d="M0 {y + 6 * math.sin(i):.1f} Q75 {y - 6:.1f} 150 {y + 4:.1f} T300 {y:.1f} V{y + lh + 6:.1f} H0 Z" fill="{colors[i % len(colors)]}" stroke="{DARK}" stroke-width="3"/>')
    if water_:
        out.append(f'<rect x="0" y="{Hh - lh * 1.4:.1f}" width="300" height="{lh * 1.4:.1f}" fill="{BLUE}" opacity="0.55"/>')
    for (i, x) in fossils:
        y = i * lh + lh / 2
        out.append(f'<path d="M{x} {y + 8} a12 12 0 1 1 12 -12 a8 8 0 1 1 -8 8 a4 4 0 1 1 4 -4" fill="none" stroke="{DARK}" stroke-width="3"/>')
    if arrow_bottom:
        out.append(f'<line x1="270" y1="20" x2="270" y2="{Hh - 30}" stroke="{RED}" stroke-width="7"/><path d="M270 {Hh - 10} l-12 -22 h24 z" fill="{RED}"/>')
    return sized(Item(W, Hh + 10, f'<g transform="translate(0 4)">' + ''.join(out) + '</g>'), size)


def circuit(size=320, bulbs=1, series=True, battery_=True):
    out = [f'<rect x="20" y="20" width="260" height="160" rx="12" fill="none" stroke="{DARK}" stroke-width="6"/>']
    if battery_:
        out.append(f'<rect x="110" y="166" width="80" height="28" rx="5" fill="{GREEN}" stroke="{DARK}" stroke-width="4"/><text x="176" y="188" font-family="{SANS}" font-size="20" font-weight="700" fill="#fff">+</text>')
    for k in range(bulbs):
        x = 150 if bulbs == 1 else 90 + k * 120 / max(1, bulbs - 1)
        b = sized(lightbulb_on(70), 56)
        out.append(f'<rect x="{x - 30:.1f}" y="10" width="60" height="22" fill="#fff"/>' + g(b, x - b.w / 2, -24))
    return sized(Item(300, 200, f'<g transform="translate(0 40)">' + ''.join(out) + '</g>'), size)


def resistor(size=300):
    return _icon(300, 80, f'<path d="M10 40 H80 L95 15 L120 65 L145 15 L170 65 L195 15 L210 40 H290" fill="none" stroke="{DARK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>', size)


def field_lines(size=300, kind='sphere'):
    out = []
    if kind == 'magnet':
        for k in range(1, 5):
            out.append(f'<path d="M80 100 C80 {100 - k * 30} 220 {100 - k * 30} 220 100" fill="none" stroke="{BLUE}" stroke-width="3"/><path d="M80 100 C80 {100 + k * 30} 220 {100 + k * 30} 220 100" fill="none" stroke="{BLUE}" stroke-width="3"/>')
        m = magnet(150)
        out.append(g(m, 75, 100 - m.h / 2))
        return _icon(300, 220, f'<g transform="translate(0 10)">' + ''.join(out) + '</g>', size)
    for k in range(12):
        a = 2 * math.pi * k / 12
        out.append(f'<line x1="{150 + 40 * math.cos(a):.1f}" y1="{110 + 40 * math.sin(a):.1f}" x2="{150 + 100 * math.cos(a):.1f}" y2="{110 + 100 * math.sin(a):.1f}" stroke="{BLUE}" stroke-width="4"/>'
                   f'<path d="M{150 + 108 * math.cos(a):.1f} {110 + 108 * math.sin(a):.1f} l{-14 * math.cos(a) - 7 * math.sin(a):.1f} {-14 * math.sin(a) + 7 * math.cos(a):.1f} l{14 * math.sin(a):.1f} {-14 * math.cos(a):.1f} z" fill="{BLUE}"/>')
    out.append(f'<circle cx="150" cy="110" r="36" fill="{RED if kind == "plus" else soft(ORANGE)}" stroke="{DARK}" stroke-width="5"/>')
    if kind == 'plus':
        out.append(f'<text x="150" y="128" font-family="{SANS}" font-size="52" font-weight="700" text-anchor="middle" fill="#fff">+</text>')
    return _icon(300, 220, ''.join(out), size)


def charge(sign='+', size=90):
    c = RED if sign == '+' else BLUE
    return _icon(100, 100, f'<circle cx="50" cy="50" r="44" fill="{c}" stroke="{DARK}" stroke-width="5"/><text x="50" y="70" font-family="{SANS}" font-size="62" font-weight="700" text-anchor="middle" fill="#fff">{"+" if sign == "+" else "−"}</text>', size)


def ball(size=70, color=RED):
    return _icon(60, 60, f'<circle cx="30" cy="30" r="26" fill="{color}" stroke="{DARK}" stroke-width="4"/><circle cx="21" cy="21" r="6" fill="#fff" opacity="0.6"/>', size)


def crate(size=100, color=BROWN):
    return _icon(100, 100, f'<rect x="5" y="5" width="90" height="90" fill="#d9a066" stroke="{DARK}" stroke-width="5"/><path d="M5 5 L95 95 M95 5 L5 95" stroke="{BROWN}" stroke-width="4"/>', size)


def push(item=None, arrows_=(('left', 90, RED),), size=320, labels=None):
    """An object with force arrows pointing at it (from the side named)."""
    c = item or crate(110)
    parts = []
    left = [a for a in arrows_ if a[0] == 'left']
    right = [a for a in arrows_ if a[0] == 'right']
    up = [a for a in arrows_ if a[0] in ('up', 'down')]
    body = c
    for d, ln, col_ in up:
        body = col(arrow(ln, col_, 'up'), body, gap=4) if d == 'up' else col(body, arrow(ln, col_, 'down'), gap=4)
    return row(*[arrow(ln, col_, 'right') for _, ln, col_ in left], body, *[arrow(ln, col_, 'left') for _, ln, col_ in right], gap=4)


def spectrum(size=420, labels=('radio', 'micro', 'IR', 'visible', 'UV', 'X-ray', 'gamma'), rainbow=False, lines_at=None):
    W = 460
    out = []
    if rainbow:
        cols = ['#8f2bd8', '#3a4be0', '#2fa0e0', '#2fb84a', '#f2d02a', '#f28b1e', '#e0302a']
        for i, c in enumerate(cols):
            out.append(f'<rect x="{10 + i * 62}" y="20" width="63" height="80" fill="{c}"/>')
        for x in (lines_at or ()):
            out.append(f'<line x1="{x}" y1="20" x2="{x}" y2="100" stroke="{DARK}" stroke-width="5"/>')
        return sized(Item(460, 110, ''.join(out)), size)
    n = len(labels)
    for i, l in enumerate(labels):
        hue = ['#9c6b4f', '#b78a5d', '#d26a5a', 'url(#rb)', '#9a6bd8', '#6b7fd8', '#4f5f9a'][i % 7]
        out.append(f'<rect x="{10 + i * (W - 20) / n:.1f}" y="40" width="{(W - 20) / n + 1:.1f}" height="50" fill="{hue}"/>')
        out.append(f'<text x="{10 + (i + 0.5) * (W - 20) / n:.1f}" y="124" font-family="{SANS}" font-size="17" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(l)}</text>')
    out.insert(0, '<defs><linearGradient id="rb"><stop offset="0" stop-color="#e0302a"/><stop offset=".25" stop-color="#f2d02a"/><stop offset=".5" stop-color="#2fb84a"/><stop offset=".75" stop-color="#3a4be0"/><stop offset="1" stop-color="#8f2bd8"/></linearGradient></defs>')
    wv = '<path d="M10 20 ' + ' '.join(f'L{10 + t * 4.4:.1f} {20 + 12 * math.sin(t * t / 260):.1f}' for t in range(101)) + f'" fill="none" stroke="{DARK}" stroke-width="3"/>'
    out.append(wv)
    out.append(f'<rect x="10" y="40" width="{W - 20}" height="50" fill="none" stroke="{DARK}" stroke-width="4"/>')
    return sized(Item(W, 134, ''.join(out)), size)


def handshake(size=180, left=BLUE, right=ORANGE):
    """Two hands clasped in a handshake, each coming in from its own sleeve."""
    st = f'stroke="{DARK}" stroke-width="5" stroke-linejoin="round"'
    svg = (f'<rect x="4" y="58" width="56" height="58" rx="6" fill="{left}" {st}/>'
           f'<rect x="216" y="44" width="56" height="58" rx="6" fill="{right}" {st}/>'
           # the right hand, underneath: palm coming in from the right, fingers curling under on the left
           f'<path d="M218 50 L152 46 C128 44 104 54 98 70 C94 84 104 96 122 98 L218 96 Z" fill="{SKIN}" {st}/>'
           # the left hand, on top: fingers wrap down over the back of the right hand
           f'<path d="M58 64 L118 60 C136 58 158 62 172 70 C186 78 188 96 176 106 C164 114 142 112 120 110 L58 110 Z" fill="{SKIN}" {st}/>'
           + ''.join(f'<path d="M{x} {y0} C{x + 8} {y0 + 10} {x + 10} {y0 + 24} {x + 6} {y0 + 38}" fill="none" stroke="{DARK}" stroke-width="3.5" stroke-linecap="round"/>' for x, y0 in ((134, 66), (150, 68), (164, 74)))
           # the right thumb lies over the top of the left hand
           + f'<path d="M150 47 C132 40 112 42 104 54 C100 62 110 66 118 62 C126 58 138 56 150 58 Z" fill="{SKIN}" {st}/>')
    return _icon(276, 124, svg, size)


def web(nodes, edges, size=400, w=420, h=340, fs=26):
    """A food web: nodes {name: (x, y, color)} as labeled boxes; edges [(food, eater)] arrows that point from the food
    to the eater (the way the energy goes)."""
    bw = {n: measure(n, fs, True) + 28 for n in nodes}
    out = []
    for a, b in edges:
        (x1, y1, _), (x2, y2, _) = nodes[a], nodes[b]
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L

        def cut(n):
            hw, hh = bw[n] / 2 + 6, 26
            return min(hw / abs(ux) if ux else 1e9, hh / abs(uy) if uy else 1e9)
        sx, sy = x1 + ux * cut(a), y1 + uy * cut(a)
        ex, ey = x2 - ux * cut(b), y2 - uy * cut(b)
        out.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex - ux * 14:.1f}" y2="{ey - uy * 14:.1f}" stroke="{DARK}" stroke-width="5"/>'
                   f'<path d="M{ex:.1f} {ey:.1f} L{ex - ux * 20 - uy * 11:.1f} {ey - uy * 20 + ux * 11:.1f} L{ex - ux * 20 + uy * 11:.1f} {ey - uy * 20 - ux * 11:.1f} Z" fill="{DARK}"/>')
    for n, (x, y, c) in nodes.items():
        out.append(f'<rect x="{x - bw[n] / 2:.1f}" y="{y - 21}" width="{bw[n]:.1f}" height="42" rx="10" fill="{soft(c)}" stroke="{c}" stroke-width="4"/>'
                   f'<text x="{x}" y="{y + fs * 0.36:.1f}" font-family="{SANS}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(n)}</text>')
    return sized(Item(w, h, ''.join(out)), size)


def bug(size=80, color=RED):
    """A small beetle (a bug in code)."""
    legs = ''.join(f'<path d="M{50 + sx * 14} {y} l{sx * 20} {dy}" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>' for sx in (-1, 1) for y, dy in ((44, -10), (58, 0), (72, 10)))
    return _icon(100, 100, legs + f'<ellipse cx="50" cy="60" rx="24" ry="30" fill="{color}" stroke="{DARK}" stroke-width="5"/><circle cx="50" cy="26" r="13" fill="{DARK}"/>'
                 f'<line x1="50" y1="34" x2="50" y2="88" stroke="{DARK}" stroke-width="4"/><path d="M44 16 l-8 -12 M56 16 l8 -12" stroke="{DARK}" stroke-width="4" stroke-linecap="round"/>', size)


def person(size=120, color=BLUE):
    """A simple standing figure (head and body), no face."""
    return _icon(80, 120, f'<circle cx="40" cy="24" r="20" fill="{SKIN}" stroke="{DARK}" stroke-width="5"/><path d="M8 116 V78 C8 56 22 48 40 48 C58 48 72 56 72 78 V116 Z" fill="{color}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>', size)


def server(size=150, light=GREEN):
    return _icon(90, 120, f'<rect x="5" y="5" width="80" height="110" rx="8" fill="{DARK}" stroke="{DARK}" stroke-width="4"/>' + ''.join(f'<rect x="14" y="{16 + i * 32}" width="62" height="22" rx="4" fill="#4a5060"/><circle cx="64" cy="{27 + i * 32}" r="5" fill="{light}"/>' for i in range(3)), size)


def chip(size=140, inner=None):
    pins_ = ''.join(f'<rect x="{24 + i * 16}" y="2" width="6" height="16" fill="{GRAY}"/><rect x="{24 + i * 16}" y="102" width="6" height="16" fill="{GRAY}"/><rect x="2" y="{24 + i * 16}" width="16" height="6" fill="{GRAY}"/><rect x="102" y="{24 + i * 16}" width="16" height="6" fill="{GRAY}"/>' for i in range(5))
    c = _icon(120, 120, pins_ + f'<rect x="16" y="16" width="88" height="88" rx="8" fill="{DARK}"/>', size)
    if inner is not None:
        c = over(c, sized(inner, size * 0.45, size * 0.45))
    return c


def network(size=300, n=5, broken=None, redundancy=False):
    W = 300
    pts = [(150 + 110 * math.cos(2 * math.pi * k / n - math.pi / 2), 120 + 95 * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    edges = [(k, (k + 1) % n) for k in range(n)] + ([(0, 2), (1, 3)] if n > 4 else [])
    out = []
    for i, (a, b) in enumerate(edges):
        (x1, y1), (x2, y2) = pts[a], pts[b]
        bad = broken == i
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{RED if bad else BLUE}" stroke-width="5"{" stroke-dasharray=\"8 8\"" if bad else ""}/>')
    for x, y in pts:
        s = screen(56)
        out.append(g(s, x - s.w / 2, y - s.h / 2))
    return sized(Item(W, 250, ''.join(out)), size)


def blocks_stack(heights=(3, 5, 2), size=280, star_=None, color=BLUE, colors=None, labels=None):
    cols_ = []
    for i, h in enumerate(heights):
        c = colors[i] if colors else color
        s = col(*[cube_icon(46, c) for _ in range(h)], gap=0)
        if star_ == i:
            s = col(star(40), s, gap=4)
        if labels:
            s = col(s, T(labels[i], 26), gap=4)
        cols_.append(s)
    return row(*cols_, gap=26, align='b')


def boxplot(size=360, outlier=False, bracket=False):
    W = 400
    out = [f'<line x1="20" y1="140" x2="380" y2="140" stroke="{DARK}" stroke-width="3"/>']
    out.append(f'<line x1="40" y1="80" x2="120" y2="80" stroke="{DARK}" stroke-width="5"/><line x1="40" y1="60" x2="40" y2="100" stroke="{DARK}" stroke-width="5"/>'
               f'<rect x="120" y="50" width="130" height="60" fill="{soft(BLUE)}" stroke="{DARK}" stroke-width="5"/><line x1="170" y1="50" x2="170" y2="110" stroke="{DARK}" stroke-width="6"/>'
               f'<line x1="250" y1="80" x2="{300 if outlier else 340}" y2="80" stroke="{DARK}" stroke-width="5"/><line x1="{300 if outlier else 340}" y1="60" x2="{300 if outlier else 340}" y2="100" stroke="{DARK}" stroke-width="5"/>')
    if outlier:
        out.append(f'<circle cx="370" cy="80" r="9" fill="{RED}" stroke="{DARK}" stroke-width="3"/>')
    if bracket:
        out.append(f'<path d="M120 36 v-10 H250 v10" fill="none" stroke="{RED}" stroke-width="5"/><text x="185" y="18" font-family="{SANS}" font-size="22" font-weight="700" text-anchor="middle" fill="{RED}">IQR</text>')
    return sized(Item(W, 150, ''.join(out)), size)


def histogram(values=(2, 5, 8, 6, 3, 1), size=320, color=BLUE):
    return bars(values, size=size, color=color, touch=True)


def dotplot(values, size=360, color=BLUE, a=None, b=None, center=None, bracket=False, dev=False):
    a = min(values) - 1 if a is None else a
    b = max(values) + 1 if b is None else b
    cnt = {}
    for v in values:
        cnt[v] = cnt.get(v, 0) + 1
    nl = numberline(a, b, size=size, dots_=cnt, color=color, arrow_ends=False, bracket=(min(values), max(values), 'range') if bracket else None)
    if center is not None:
        W = 500
        X = 30 + (center - a) / (b - a) * 440
        k = size / W
        extra = f'<line x1="{X:.1f}" y1="10" x2="{X:.1f}" y2="130" stroke="{RED}" stroke-width="5" stroke-dasharray="10 6"/>'
        if dev:
            for v, c in cnt.items():
                xv = 30 + (v - a) / (b - a) * 440
                extra += f'<line x1="{X:.1f}" y1="{96 - 0:.1f}" x2="{xv:.1f}" y2="96" stroke="{ORANGE}" stroke-width="4"/>'
        nl = Item(nl.w, nl.h, nl.svg + f'<g transform="scale({k:.4f})">{extra}</g>')
    return nl


def scatter(n=14, trend=1.0, noise=0.8, size=300, line=False, outlier=None, seed=3, resid=None, band=False, zero=False, tight=False):
    import random
    rnd = random.Random(seed)
    pts = []
    for i in range(n):
        x = 0.5 + 8.5 * i / (n - 1)
        y = 1 + trend * 0.8 * x + rnd.gauss(0, noise * (0.35 if tight else 1)) if not zero else rnd.gauss(0, 1.2) + 4.5
        pts.append((x, max(0.3, min(9.5, y))))
    if outlier:
        pts.append(outlier)
    fns = [(lambda x: 1 + trend * 0.8 * x)] if line or resid is not None or band else []
    segs = []
    if resid is not None:
        x, y = pts[resid]
        segs.append(((x, y), (x, 1 + trend * 0.8 * x), RED))
    p = plot(*fns, size=size, xr=(0, 10), yr=(0, 10), scatter=pts, segs=segs, colors=(ORANGE,), hlines=((4.5,) if zero else ()),
             fill_between=((lambda x: 1.8 + trend * 0.8 * x + 0.1 * (x - 5) ** 2 * 0.1), (lambda x: 0.2 + trend * 0.8 * x - 0.1 * (x - 5) ** 2 * 0.1), 0, 10) if band else None)
    return p


def dice(n=6, size=90):
    pos = {1: [(50, 50)], 2: [(30, 30), (70, 70)], 3: [(28, 28), (50, 50), (72, 72)], 4: [(30, 30), (70, 30), (30, 70), (70, 70)],
           5: [(28, 28), (72, 28), (50, 50), (28, 72), (72, 72)], 6: [(30, 26), (70, 26), (30, 50), (70, 50), (30, 74), (70, 74)]}[n]
    return _icon(100, 100, f'<rect x="5" y="5" width="90" height="90" rx="16" fill="#fff" stroke="{DARK}" stroke-width="5"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="8" fill="{DARK}"/>' for x, y in pos), size)


def domino(a=6, b=6, size=120):
    d1, d2 = dice(a, 60), dice(b, 60)
    return box(col(d1, d2, gap=0), color=DARK, fill='#fff', p=6)


def coin(size=90, label=None, color='#c9ccd1'):
    c = _icon(100, 100, f'<circle cx="50" cy="50" r="45" fill="{color}" stroke="{DARK}" stroke-width="5"/><circle cx="50" cy="50" r="35" fill="none" stroke="{DARK}" stroke-width="2" opacity="0.4"/>', size)
    return over(c, T(label, size * 0.32)) if label else c


def ruler(size=420, units=10, label='cm', every=1, inches=False, first=None):
    """A ruler; the unit name sits past the last tick; first: a label for the first unit, which is shaded and bracketed."""
    W = 460
    out = [f'<rect x="5" y="20" width="450" height="70" rx="6" fill="{YELLOW}" stroke="{DARK}" stroke-width="5"/>']
    sub = (4 if inches else 2) if units <= 20 else 1
    n = units * sub
    x0, x1 = 25, 400
    if first:
        out.append(f'<rect x="{x0}" y="23" width="{(x1 - x0) / units:.1f}" height="64" fill="{soft(BLUE)}"/>')
    for i in range(n + 1):
        x = x0 + i * (x1 - x0) / n
        full = i % sub == 0
        out.append(f'<line x1="{x:.1f}" y1="20" x2="{x:.1f}" y2="{20 + (32 if full else 16)}" stroke="{DARK}" stroke-width="{3 if full else 2}"/>')
        if full and (i // sub) % every == 0:
            out.append(f'<text x="{x:.1f}" y="76" font-family="{SANS}" font-size="20" font-weight="700" text-anchor="middle" fill="{DARK}">{i // sub}</text>')
    out.append(f'<text x="448" y="62" font-family="{SANS}" font-size="20" font-weight="700" text-anchor="end" fill="{GRAY}">{label}</text>')
    if first:
        xa, xb = x0, x0 + (x1 - x0) / units
        out.append(f'<path d="M{xa} 12 v-10 H{xb:.1f} v10" fill="none" stroke="{RED}" stroke-width="4"/>'
                   f'<text x="{(xa + xb) / 2 + 8:.1f}" y="-12" font-family="{SANS}" font-size="28" font-weight="700" text-anchor="middle" fill="{RED}">{escape(first)}</text>')
        return sized(Item(W, 150, '<g transform="translate(0 50)">' + ''.join(out) + '</g>'), size)
    return sized(Item(W, 100, ''.join(out)), size)


def meter(size=220, value=0.9, label=None, zone=None):
    a = math.pi * (1 - value)
    out = [f'<path d="M20 120 A100 100 0 0 1 220 120" fill="none" stroke="{LIGHT}" stroke-width="26"/>']
    if zone:
        a0, a1 = math.pi * (1 - zone[0]), math.pi * (1 - zone[1])
        out.append(f'<path d="M{120 + 100 * math.cos(a0):.1f} {120 - 100 * math.sin(a0):.1f} A100 100 0 0 1 {120 + 100 * math.cos(a1):.1f} {120 - 100 * math.sin(a1):.1f}" fill="none" stroke="{GREEN}" stroke-width="26"/>')
    else:
        out.append(f'<path d="M20 120 A100 100 0 0 1 {120 + 100 * math.cos(a):.1f} {120 - 100 * math.sin(a):.1f}" fill="none" stroke="{GREEN}" stroke-width="26"/>')
    out.append(f'<line x1="120" y1="120" x2="{120 + 80 * math.cos(a):.1f}" y2="{120 - 80 * math.sin(a):.1f}" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/><circle cx="120" cy="120" r="10" fill="{DARK}"/>')
    if label:
        out.append(f'<text x="120" y="170" font-family="{SANS}" font-size="38" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(label)}</text>')
    return _icon(240, 180 if label else 135, ''.join(out), size)


def toggle(on=True, size=150, label=None):
    t = _icon(120, 64, f'<rect x="4" y="4" width="112" height="56" rx="28" fill="{GREEN if on else LIGHT}" stroke="{DARK}" stroke-width="5"/><circle cx="{88 if on else 32}" cy="32" r="22" fill="#fff" stroke="{DARK}" stroke-width="4"/>', size)
    return row(t, T(label, 40)) if label else t


def slider(size=260, pos=0.7):
    return _icon(260, 60, f'<line x1="20" y1="30" x2="240" y2="30" stroke="{LIGHT}" stroke-width="12" stroke-linecap="round"/><line x1="20" y1="30" x2="{20 + 220 * pos:.1f}" y2="30" stroke="{BLUE}" stroke-width="12" stroke-linecap="round"/>'
                 f'<circle cx="{20 + 220 * pos:.1f}" cy="30" r="20" fill="#fff" stroke="{DARK}" stroke-width="5"/>', size)


def browser(size=260, inner=None, tabs=1, search=False, check_=False, warn=False, query=None):
    W, Hh = 220, 160
    out = [f'<rect x="3" y="3" width="{W - 6}" height="{Hh - 6}" rx="10" fill="#fff" stroke="{DARK}" stroke-width="5"/><rect x="3" y="3" width="{W - 6}" height="34" rx="10" fill="{LIGHT}" stroke="{DARK}" stroke-width="5"/>']
    for i in range(tabs):
        out.append(f'<rect x="{12 + i * 60}" y="10" width="54" height="20" rx="5" fill="{"#fff" if i == 0 else "#f4f5f8"}" stroke="{DARK}" stroke-width="2.5"/>')
    if search:
        out.append(f'<rect x="30" y="66" width="160" height="34" rx="17" fill="#fff" stroke="{DARK}" stroke-width="4"/>')
        out.append(g(magnifier(30), 154, 68))
        if query:
            qt = T(query, 24, DARK)
            out.append(f'<rect x="42" y="70" width="{qt.w + 10:.1f}" height="26" rx="5" fill="#fde97a"/>' + g(qt, 47, 68))
    b = Item(W, Hh, ''.join(out))
    if inner is not None:
        c = sized(inner, 120, 90)
        b = Item(W, Hh, b.svg + g(c, (W - c.w) / 2, 37 + (Hh - 37 - c.h) / 2))
    if check_:
        b = Item(W, Hh, b.svg + g(check(70), W / 2 - 35, 62))
    if warn:
        b = Item(W, Hh, b.svg + g(warning(70), W / 2 - 35, 60))
    return sized(b, size)


def code_blocks(n=3, size=220, colors=(BLUE, ORANGE, GREEN, PURPLE), widths=None, labels=None):
    bs = []
    for i in range(n):
        w = (widths or [180, 140, 200, 160])[i % 4]
        c = colors[i % len(colors)]
        lab = labels[i] if labels else None
        bs.append(Item(w, 44, f'<path d="M3 3 H30 l6 7 h18 l6 -7 H{w - 3} V41 H60 l-6 7 h-18 l-6 -7 H3 Z" fill="{c}" stroke="{DARK}" stroke-width="3.5" stroke-linejoin="round"/>'
                       + (g(T(lab, 22, '#fff'), 12, 6) if lab else f'<rect x="14" y="16" width="{w * 0.45:.1f}" height="10" rx="5" fill="#fff" opacity="0.8"/>')))
    return sized(col(*bs, gap=0, align='l'), size)


def code_lines(n=5, size=240, indent=(), hl=None, comment=None, arrow_at=None, hl_color='#5a5020', skip=False):
    """Lines of code on a dark editor. hl: a line index with a highlight band (hl_color); comment: a line index drawn as a
    gray "#" comment; skip: a curved arrow jumping past the comment line; arrow_at: a step arrow at the left of a line."""
    out = [f'<rect x="3" y="3" width="234" height="{30 + n * 26}" rx="10" fill="#22262f" stroke="{DARK}" stroke-width="4"/>']
    cols_ = ['#7fb4ff', '#ffb86b', '#9be29b', '#f2a2d6', '#e6e6e6']
    for i in range(n):
        y = 22 + i * 26
        x0 = 20 + (22 if i in indent else 0)
        if hl == i:
            out.append(f'<rect x="8" y="{y - 10}" width="224" height="22" rx="4" fill="{hl_color}"/>')
        if comment == i:
            out.append(f'<text x="{x0}" y="{y + 7}" font-family="Consolas, monospace" font-size="21" font-weight="700" fill="#8d94a5">#</text>'
                       f'<rect x="{x0 + 18}" y="{y - 4}" width="130" height="9" rx="4" fill="#6b7180"/>')
            continue
        out.append(f'<rect x="{x0}" y="{y - 4}" width="{40 + (i * 37) % 60}" height="9" rx="4" fill="{cols_[i % 5]}"/><rect x="{x0 + 50 + (i * 37) % 60}" y="{y - 4}" width="{30 + (i * 23) % 50}" height="9" rx="4" fill="#cfd3dc"/>')
    right = 0
    if skip and comment is not None:
        y1, y2 = 22 + (comment - 1) * 26, 22 + (comment + 1) * 26
        out.append(f'<path d="M240 {y1} C278 {y1} 278 {y2} 248 {y2}" fill="none" stroke="{ORANGE}" stroke-width="6" stroke-linecap="round"/>'
                   f'<path d="M240 {y2} l14 -10 l0 20 z" fill="{ORANGE}"/>')
        right = 40
    if arrow_at is not None:
        out.append(f'<path d="M-30 {22 + arrow_at * 26} h22 m0 0 l-10 -8 m10 8 l-10 8" fill="none" stroke="{ORANGE}" stroke-width="6" stroke-linecap="round"/>')
    left = 34 if arrow_at is not None else 0
    return sized(Item(240 + left + right, 40 + n * 26, f'<g transform="translate({left} 0)">' + ''.join(out) + '</g>'), size)


# ---------- reading and writing structures ----------

def plot_arc(hl=None, size=440):
    """The plot mountain (exposition, rising action, climax, falling action, resolution); hl: the part picked out (0 to 4)."""
    pts = [(20, 230), (120, 230), (270, 60), (380, 200), (470, 200)]
    out = []
    for k, ((xa, ya), (xb, yb)) in enumerate(zip(pts, pts[1:])):
        part = {0: 0, 1: 1, 2: 3, 3: 4}[k]
        on = hl == part
        out.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="{ORANGE if on else "#b4b8c2"}" stroke-width="{16 if on else 9}" stroke-linecap="round"/>')
    on = hl == 2
    out.append(f'<circle cx="270" cy="60" r="{20 if on else 13}" fill="{ORANGE if on else "#b4b8c2"}" stroke="{DARK}" stroke-width="4"/>')
    labs = [(('exposition',), 70, 272, 'middle'), (('rising', 'action'), 182, 120, 'end'), (('climax',), 270, 30, 'middle'),
            (('falling', 'action'), 340, 108, 'start'), (('resolution',), 425, 242, 'middle')]
    for k, (lines, x, y, anc) in enumerate(labs):
        on = hl == k
        for j, s in enumerate(lines):
            out.append(f'<text x="{x}" y="{y + j * 30}" font-family="{SANS}" font-size="{32 if on else 26}" font-weight="700" text-anchor="{anc}" fill="{ORANGE if on else GRAY}">{s}</text>')
    return sized(Item(490, 290, ''.join(out)), size)


def parts3(pics, labels=('beginning', 'middle', 'end'), hl=None, size=440, numbers=False):
    """Three picture panels in order, top to bottom, joined by arrows, a label beside each; hl: the panel picked out."""
    rows_ = []
    for k, (p, l) in enumerate(zip(pics, labels)):
        on = hl is None or hl == k
        c = (ORANGE if hl == k else BLUE) if on else GRAY
        pan = card(p, 170, 150, c, '#fff' if on else '#f3f4f7')
        if not on:
            pan = Item(pan.w, pan.h, f'<g opacity="0.45">{pan.svg}</g>')
        if hl == k:
            pan = Item(pan.w, pan.h, f'<rect x="-7" y="-7" width="{pan.w + 14}" height="{pan.h + 14}" rx="22" fill="{soft(ORANGE)}"/>' + pan.svg)
        lab = T(f'{k + 1}. {l}' if numbers else l, 44 if hl == k else 36, ORANGE if hl == k else (DARK if on else '#9aa0ad'))
        rows_.append(row(pan, lab, gap=22))
    out = []
    for k, r in enumerate(rows_):
        if k:
            out.append(row(Item(70, 10, ''), arrow(26, DARK, 'down', sw=7), gap=0))
        out.append(r)
    stack = col(*out, gap=4, align='l')
    return sized(Item(stack.w, stack.h, stack.svg), size)


def argue(top='claim', mid='reason', bottom='evidence', n=2, hl=None, size=440, texts=None, pick=None):
    """An argument built like a house: the claim on top, held up by reasons, each resting on evidence.
    hl: 'top', 'mid' or 'bottom' (that row in orange, the rest gray); texts: {'top': ..., 'mid': [...], 'bottom': [...]} words in the boxes."""
    texts = texts or {}
    W = 460

    def lvl(name):
        return ORANGE if hl == name else (BLUE if hl is None else '#9aa0ad')
    bw = (W - 20 * (n - 1)) / n
    out = []
    y = 0
    th = 90
    tc = lvl('top')
    tt = T(texts.get('top', top), 34 if 'top' in texts else 40, DARK if hl in (None, 'top') else GRAY)
    tt = sized(tt, W - 40) if tt.w > W - 40 else tt
    out.append(g(box(tt, w=W, h=th, color=tc, fill=soft(tc) if hl in (None, 'top') else '#f1f2f5', sw=6 if hl == 'top' else 5), 0, y))
    y += th
    mh = 74
    rows_ = [('mid', mid)] + ([('bottom', bottom)] if bottom else [])
    for name, word in rows_:
        c = lvl(name)
        on = hl in (None, name)
        for i in range(n):
            x = i * (bw + 20)
            out.append(f'<line x1="{x + bw / 2:.1f}" y1="{y + 4}" x2="{x + bw / 2:.1f}" y2="{y + 40}" stroke="{DARK}" stroke-width="6"/><path d="M{x + bw / 2:.1f} {y + 2} l-11 16 h22 z" fill="{DARK}"/>')
            s = texts.get(name, [word] * n)[i]
            if pick is not None and name == hl and i != pick:
                c, on = '#9aa0ad', False
            else:
                c, on = lvl(name), hl in (None, name)
            t = T(s, 30 if name in texts else 34, DARK if on else GRAY)
            if t.w > bw - 20:
                t = sized(t, bw - 20)
            out.append(g(box(t, w=bw, h=mh, color=c, fill=soft(c) if on else '#f1f2f5', sw=6 if hl == name else 5), x, y + 44))
        y += 44 + mh
    return sized(Item(W, y, ''.join(out)), size)


def tagged(*parts, size=44, top=None, gap=None, links=(), ts=0.56):
    """A sentence as words. A tuple (text, color, tag) gets a color band and its tag under it; top: (text, color), a bracket
    over the whole sentence with that label; links: [(from part, to part, color)] curved arrows over the words."""
    items = []
    for p in parts:
        if isinstance(p, tuple):
            txt, c, tag = (tuple(p) + (None, None))[:3]
            w = T(txt, size, DARK)
            bw = w.w * 1.07 + 22
            band = Item(bw, w.h, f'<rect x="0" y="{w.h * 0.06:.1f}" width="{bw:.1f}" height="{w.h * 0.86:.1f}" rx="9" fill="{soft(c)}" stroke="{c}" stroke-width="4"/>' + g(w, 11, 0))
            items.append(col(band, T(tag, size * ts, c), gap=4) if tag else band)
        else:
            items.append(T(p, size, DARK, bold=False))
    gp = gap if gap is not None else size * 0.28
    r = row(*items, gap=gp, align='t')
    if links:
        xs, x = [], 0
        for i_ in items:
            xs.append(x + i_.w / 2)
            x += i_.w + gp
        lift = size * 1.3
        arcs = ''
        for a, b, c in links:
            xa, xb = xs[a], xs[b]
            arcs += (f'<path d="M{xa:.1f} {lift - 4:.1f} C{xa:.1f} {lift * 0.15:.1f} {xb:.1f} {lift * 0.15:.1f} {xb:.1f} {lift - 14:.1f}" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
                     f'<path d="M{xb:.1f} {lift:.1f} l-10 -18 h20 z" fill="{c}"/>')
        r = Item(r.w, r.h + lift, arcs + g(r, 0, lift))
    if top:
        txt, c = top
        br = Item(r.w, 24, f'<path d="M4 22 V6 H{r.w - 4:.1f} V22" fill="none" stroke="{c}" stroke-width="5" stroke-linejoin="round"/>')
        r = col(T(txt, size * 0.62, c), br, r, gap=4)
    return r


def family_tree(hl=None, size=420):
    """Grandmother and grandfather, then mother and father, then me; hl: the person picked out by name."""
    people = {'grandmother': (50, 10, PURPLE, 96), 'grandfather': (250, 10, TEAL, 96), 'mother': (150, 170, RED, 96),
              'father': (310, 170, BLUE, 96), 'me': (230, 330, ORANGE, 78)}
    out = ['<path d="M114 60 H250 M182 60 V170 M214 220 H310 M262 220 V330" fill="none" stroke="#8a8f9c" stroke-width="6"/>']
    for name, (x, y, c, s) in people.items():
        on = hl == name
        if on:
            bw = max(s * 0.67 + 52, len(name) * 17 + 16)
            out.append(f'<rect x="{x + s * 0.67 / 2 - bw / 2:.0f}" y="{y - 8}" width="{bw:.0f}" height="{s + 52}" rx="16" fill="#fde97a" stroke="{ORANGE}" stroke-width="6"/>')
        out.append(g(person(s, c), x, y))
    for name, (x, y, c, s) in people.items():
        on = hl == name
        cx = x + s * 0.67 / 2
        out.append(f'<text x="{cx:.0f}" y="{y + s + 34}" font-family="{SANS}" font-size="{28 if on else 23}" font-weight="700" text-anchor="middle" fill="{RED if on else GRAY}">{name}</text>')
    return sized(Item(400, 470, ''.join(out)), size)


def nutrition_label(hl=None, size=320):
    """A cereal's Nutrition Facts label; hl: 'serving', 'calories' or 'sugars' gets a highlighter band."""
    rows_ = [('serving', 'Serving size', '1 cup', 30, 4), ('calories', 'Calories', '150', 40, 8), ('fat', 'Total Fat', '2g', 26, 2),
             ('sodium', 'Sodium', '190mg', 26, 2), ('sugars', 'Total Sugars', '9g', 26, 2), ('protein', 'Protein', '4g', 26, 2)]
    out = [f'<rect x="4" y="4" width="312" height="{80 + sum(r[3] + 22 for r in rows_)}" fill="#fff" stroke="{DARK}" stroke-width="6"/>',
           f'<text x="18" y="56" font-family="{SANS}" font-size="40" font-weight="900" fill="{DARK}">Nutrition Facts</text>']
    y = 76
    for key_, name, val, fs, bar in rows_:
        out.append(f'<rect x="16" y="{y - 4}" width="288" height="{bar}" fill="{DARK}"/>')
        y += bar
        if hl == key_:
            out.append(f'<rect x="12" y="{y + 2}" width="296" height="{fs + 14}" rx="6" fill="#fde97a" stroke="{ORANGE}" stroke-width="4"/>')
        out.append(f'<text x="18" y="{y + fs + 4}" font-family="{SANS}" font-size="{fs}" font-weight="700" fill="{DARK}">{name}</text>'
                   f'<text x="302" y="{y + fs + 4}" font-family="{SANS}" font-size="{fs}" font-weight="700" text-anchor="end" fill="{DARK}">{val}</text>')
        y += fs + 18
    return sized(Item(320, y + 14, ''.join(out)), size)


def dnl(top, bottom, names=('', ''), hl=None, size=440, colors=(BLUE, ORANGE)):
    """A double number line: top and bottom values lined up tick by tick; names label each line; hl: a tick index boxed."""
    n = len(top)
    x0, x1 = 120, 470
    X = lambda i: x0 + i * (x1 - x0) / (n - 1)
    out = []
    for y, vals, nm, c in ((60, top, names[0], colors[0]), (170, bottom, names[1], colors[1])):
        out.append(f'<line x1="{x0 - 14}" y1="{y}" x2="{x1 + 22}" y2="{y}" stroke="{DARK}" stroke-width="5"/><path d="M{x1 + 32} {y} l-16 -9 v18 z" fill="{DARK}"/>'
                   f'<text x="{x0 - 26}" y="{y + 10}" font-family="{SANS}" font-size="28" font-weight="700" text-anchor="end" fill="{c}">{escape(nm)}</text>')
        for i, v in enumerate(vals):
            out.append(f'<line x1="{X(i):.1f}" y1="{y - 12}" x2="{X(i):.1f}" y2="{y + 12}" stroke="{DARK}" stroke-width="4"/>'
                       f'<text x="{X(i):.1f}" y="{y + (-22 if y == 60 else 46)}" font-family="{SANS}" font-size="30" font-weight="700" text-anchor="middle" fill="{c}">{escape(str(v))}</text>')
    if hl is not None:
        out.insert(0, f'<rect x="{X(hl) - 46:.1f}" y="2" width="92" height="230" rx="14" fill="#fde97a" stroke="{ORANGE}" stroke-width="5"/>')
    return sized(Item(510, 236, ''.join(out)), size)


def us_coins(hl='penny', size=440):
    """A penny, nickel, dime and quarter at their true sizes; hl: the coin picked out, named with its value under it."""
    info = [('penny', 19.05, '#c97a42', '1¢', '1 cent'), ('nickel', 21.21, '#c9ccd1', '5¢', '5 cents'),
            ('dime', 17.91, '#c9ccd1', '10¢', '10 cents'), ('quarter', 24.26, '#c9ccd1', '25¢', '25 cents')]
    cells = []
    for name, mm, c, short, value in info:
        on = name == hl
        r = mm * 4.2
        svg = (f'<circle cx="{r / 2 + 6:.1f}" cy="{r / 2 + 6:.1f}" r="{r / 2:.1f}" fill="{c if on else "#eef0f4"}" stroke="{DARK if on else "#b4b8c2"}" stroke-width="{5 if on else 4}"/>'
               f'<circle cx="{r / 2 + 6:.1f}" cy="{r / 2 + 6:.1f}" r="{r / 2 - 9:.1f}" fill="none" stroke="{DARK if on else "#c4c8d0"}" stroke-width="2" opacity="0.45"/>')
        coin_ = Item(r + 12, r + 12, svg)
        if on:
            coin_ = over(coin_, T(short, r * 0.34, DARK))
        lab = T(name, 30 if on else 24, DARK if on else '#9aa0ad')
        parts = [coin_, lab] + ([T(value, 36, RED)] if on else [Item(10, 45, '')])
        cells.append(col(*parts, gap=6))
    return sized(row(*cells, gap=18, align='t'), size)


def grid2x2(cols, rows_, cells, hl=None, size=420, title=('', '')):
    """A 2 by 2 table (a confusion matrix, a decision table): cols/rows_ name the columns and rows; cells: 4 strings
    read across; hl: the cell picked out (0 to 3); title: (column heading, row heading)."""
    cw, ch, lx, ty = 170, 110, 200, 96
    out = [f'<text x="{lx + cw:.0f}" y="28" font-family="{SANS}" font-size="26" font-weight="700" text-anchor="middle" fill="{GRAY}">{escape(title[0])}</text>',
           f'<text x="24" y="{ty + ch:.0f}" font-family="{SANS}" font-size="26" font-weight="700" text-anchor="middle" fill="{GRAY}" transform="rotate(-90 24 {ty + ch:.0f})">{escape(title[1])}</text>']
    for j, s in enumerate(cols):
        out.append(f'<text x="{lx + j * cw + cw / 2:.0f}" y="{ty - 18}" font-family="{SANS}" font-size="28" font-weight="700" text-anchor="middle" fill="{DARK}">{escape(s)}</text>')
    for i, s in enumerate(rows_):
        out.append(f'<text x="{lx - 14}" y="{ty + i * ch + ch / 2 + 10:.0f}" font-family="{SANS}" font-size="28" font-weight="700" text-anchor="end" fill="{DARK}">{escape(s)}</text>')
    for k, s in enumerate(cells):
        i, j = divmod(k, 2)
        on = hl == k
        x, y = lx + j * cw, ty + i * ch
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{"#fde97a" if on else "#fff"}" stroke="{DARK}" stroke-width="4"/>')
        lines = s.split('\n')
        for m, ln in enumerate(lines):
            out.append(f'<text x="{x + cw / 2:.0f}" y="{y + ch / 2 + 9 + (m - (len(lines) - 1) / 2) * 30:.0f}" font-family="{SANS}" font-size="{26 if on else 22}" font-weight="700" text-anchor="middle" fill="{RED if on else GRAY}">{escape(ln)}</text>')
    if hl is not None:
        i, j = divmod(hl, 2)
        out.append(f'<rect x="{lx + j * cw - 3}" y="{ty + i * ch - 3}" width="{cw + 6}" height="{ch + 6}" fill="none" stroke="{RED}" stroke-width="7"/>')
    return sized(Item(lx + 2 * cw + 10, ty + 2 * ch + 10, ''.join(out)), size)


def paint(prompt):
    """Not drawn here: the image model paints this card (scripts/wordart.py reads these)."""
    return ('paint', prompt)


# ---------- the pipeline ----------

def render(item):
    item = it(item)
    k = min((SIZE - 2 * PAD) / item.w, (SIZE - 2 * PAD) / item.h, 2.2)
    x, y = (SIZE - item.w * k) / 2, (SIZE - item.h * k) / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">'
            f'<rect width="{SIZE}" height="{SIZE}" fill="#fff"/>{g(item, x, y, k)}</svg>')


def specs():
    """{key: Item or ('paint', prompt)} from data/closet/words/diagrams.py."""
    src = (ROOT / 'data' / 'closet' / 'words' / 'diagrams.py').read_text(encoding='utf-8')
    env = {k: v for k, v in globals().items() if not k.startswith('_')}
    out = {}
    for n, line in enumerate(src.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        key, sep, expr = line.partition(' = ')
        if not sep:
            sys.exit(f'diagrams.py:{n}: not "<key> = <spec>"')
        out[key.strip()] = (n, expr.strip())
    return out, env


CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'


def rasterize(svgs, dest):
    """Rasterize {key: svg} through headless Chrome, 32 to a sheet, and save each as webp."""
    from PIL import Image
    import tempfile
    keys = list(svgs)
    per, cols = 32, 8
    tmp = Path(tempfile.mkdtemp())
    for s in range(0, len(keys), per):
        batch = keys[s:s + per]
        rows = math.ceil(len(batch) / cols)
        html = ('<html><head><style>body{margin:0;background:#fff}svg{position:absolute}</style></head><body>' +
                ''.join(svgs[k].replace('<svg ', f'<svg style="left:{(i % cols) * SIZE}px;top:{(i // cols) * SIZE}px" ', 1) for i, k in enumerate(batch)) + '</body></html>')
        page = tmp / 'sheet.html'
        page.write_text(html, encoding='utf-8')
        png = tmp / 'sheet.png'
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1', f'--window-size={cols * SIZE},{rows * SIZE}',
                        f'--screenshot={png}', page.as_uri()], check=True, capture_output=True)
        im = Image.open(png).convert('RGB')
        for i, k in enumerate(batch):
            x, y = (i % cols) * SIZE, (i // cols) * SIZE
            out = dest(k)
            out.parent.mkdir(parents=True, exist_ok=True)
            im.crop((x, y, x + SIZE, y + SIZE)).save(out, 'WEBP', quality=88, method=6)
        print(f'{min(s + per, len(keys))}/{len(keys)} drawn', flush=True)


def main():
    import check_words
    a = sys.argv[1:]
    cards = {f"{c['module_id']}/{c['slug']}": c for cs in check_words.load().values() for c in cs if c['picture'].startswith('svg:')}
    sp, env = specs()
    if '--status' in a:
        drawn = sum(c['art'].exists() for c in cards.values())
        print(f'{len(cards)} diagram cards, {len(sp)} specs ({sum(1 for k in sp if "paint(" in sp[k][1])} handed to the painter), {drawn} pictures exist, '
              f'{len([k for k in cards if k not in sp])} without a spec, {len([k for k in sp if k not in cards])} specs with no card')
        return
    if '--sheets' in a:
        from PIL import Image, ImageDraw, ImageFont
        raw = check_words.ART / '_raw'
        raw.mkdir(parents=True, exist_ok=True)
        font = ImageFont.load_default(size=15)
        done = [(k, cards[k]) for k in sp if k in cards and cards[k]['art'].exists() and 'paint(' not in sp[k][1]]
        start = int(a[a.index('--sheets') + 1]) - 1 if len(a) > a.index('--sheets') + 1 else 0
        for n in range(start - start % 30, len(done), 30):
            grp = done[n:n + 30]
            sheet = Image.new('RGB', (256 * 6, 296 * 5), 'white')
            d = ImageDraw.Draw(sheet)
            for i, (k, c) in enumerate(grp):
                x, y = (i % 6) * 256, (i // 6) * 296
                sheet.paste(Image.open(c['art']).convert('RGB').resize((248, 248)), (x + 4, y + 4))
                d.rectangle((x + 3, y + 3, x + 252, y + 252), outline='#bbb')
                d.text((x + 6, y + 254), f"{n + i + 1}. {c['word']}", fill='#b23a17', font=font)
                d.text((x + 6, y + 272), c['picture'][4:40], fill='#333', font=font)
            sheet.save(raw / f'diagrams-{n // 30 + 1:03d}.jpg', quality=85)
            (raw / f'diagrams-{n // 30 + 1:03d}.txt').write_text(''.join(f'{n + i + 1}\t{k}\t{c["picture"]}\n' for i, (k, c) in enumerate(grp)), encoding='utf-8')
        print(f'{len(done)} diagrams on {-(-len(done) // 30)} sheets in {raw}')
        return
    only = set(a[a.index('--only') + 1:]) if '--only' in a else None
    todo = {}
    for k, (n, expr) in sp.items():
        if k not in cards or 'paint(' in expr:
            continue
        if only and k not in only:
            continue
        if not only and '--force' not in a and cards[k]['art'].exists():
            continue
        try:
            todo[k] = render(eval(expr, env))
        except Exception as e:  # noqa: BLE001
            print(f'diagrams.py:{n} {k}: {type(e).__name__}: {e}')
    if todo:
        rasterize(todo, lambda k: cards[k]['art'])
    print(f'{len(todo)} diagrams drawn')


if __name__ == '__main__':
    main()
