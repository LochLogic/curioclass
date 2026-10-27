r"""Draw anchor charts and posters (docs/SUPPLY-CLOSET-PLAN.md, Phase D) as SVG.

    python scripts/charts.py <chart-id> [fill] [es] [ink]     print one chart's SVG (fill: the fill-in version)

check_charts.py reads the files; build_site.py calls symbol() for each version, language and ink, and the page shows
the same symbol through different viewBoxes for one page, 2x2 and 3x3 tiles. A chart is drawn on an 850 x 1100 grid
(US Letter in hundredths of an inch), or 1100 x 850 for "orient: landscape". Text is wrapped here with estimated letter
widths, and a layout that does not fit is drawn again a little smaller until it does (it starts big: a wall chart is
read from across the room).

Looks: a theme (classic, bold or soft; "theme:" picks one, otherwise the id does, so a wall of charts varies) in the
chart's color (the subject color, or a poster's "color:"), and an ink-saver version of every chart: white boxes and
dark lines, nothing filled. Drawn posters ("layout: grid") are number grids, number lines, a fraction wall, a
coordinate plane, the unit circle, coins, a US map, a world map and the periodic table; their small labels are here
in both languages, and the maps and the elements come from the tools that already have them.
"""
import hashlib, json, math, re, sys
from html import escape
from pathlib import Path

import check_charts

ROOT = Path(__file__).resolve().parent.parent
W, H, M = 850, 1100, 50  # portrait page, margin (landscape swaps W and H; see dims)
FOOT = 40  # room kept at the bottom for the footer line
SANS = "'Instrument Sans', 'Segoe UI', Arial, sans-serif"
SERIF = "Fraunces, Georgia, serif"
DARK = '#1f2430'
NARROW, WIDE = set("ijlt.,;:'!|()[]/ fr\"-"), set('mwMW@%')
THEMES = ('classic', 'bold', 'soft')


def dims(c):
    return (H, W) if c.get('orient') == 'landscape' else (W, H)


def measure(text, size, bold=False, serif=False):
    w = 0.0
    for ch in text:
        w += 0.3 if ch in NARROW else 0.86 if ch in WIDE else 0.66 if ch.isupper() else 0.56 if ch.isdigit() else 0.53
    return w * size * (1.07 if bold else 1.0) * (1.14 if serif else 1.0)


def tokens(text):
    """Words, with each [[blank]] kept as one token: (text, is_blank)."""
    out, pos = [], 0
    for m in check_charts.BLANK.finditer(text):
        out += [(w, False) for w in text[pos:m.start()].split()]
        out.append((m[1], True))
        pos = m.end()
    out += [(w, False) for w in text[pos:].split()]
    # punctuation right after a blank sticks to it so it does not wrap alone
    merged = []
    for t in out:
        if merged and merged[-1][1] and not t[1] and all(ch in '.,;:!?)"’”' + "'" for ch in t[0]):
            merged[-1] = (merged[-1][0], True, t[0])
        else:
            merged.append(t + ('',))
    return merged


def blank_len(word, size):
    """Underscores for a blank: at least as wide as the bold word, and never shorter than four."""
    return max(4, math.ceil(measure(word, size, True) / (0.5 * size)) + 1)


def wrap(text, size, width, bold=False, serif=False):
    lines, line, used = [], [], 0.0
    space = measure(' ', size, serif=serif)
    for word, is_blank, tail in tokens(text):
        w = (blank_len(word, size) * 0.5 * size if is_blank else measure(word, size, bold, serif)) + measure(tail, size, bold, serif)
        if line and used + space + w > width:
            lines.append(line)
            line, used = [], 0.0
        used += (space if line else 0) + w
        line.append((word, is_blank, tail))
    if line:
        lines.append(line)
    return lines or [[]]


def spans(line, size, fill_in):
    out = []
    for word, is_blank, tail in line:
        if is_blank:
            out.append('<tspan>' + '_' * blank_len(word, size) + '</tspan>' + escape(tail) if fill_in
                       else f'<tspan font-weight="700">{escape(word)}</tspan>{escape(tail)}')
        else:
            out.append(escape(word))
    return ' '.join(out)


class Text:
    """A wrapped block of text: .h is its height; .svg(x, y) draws it with its first baseline below y."""

    def __init__(self, text, size, width, bold=False, serif=False, lead=1.25, label=None, anchor='start'):
        self.size, self.lead, self.bold, self.serif, self.anchor, self.width = size, lead, bold, serif, anchor, width
        self.label = label
        first = (label + ': ') if label else ''
        self.lines = wrap(first + text, size, width, bold, serif)
        self.h = size * lead * len(self.lines)

    def svg(self, x, y, fill_in, color=DARK):
        fam = SERIF if self.serif else SANS
        out = [f'<text x="{x:.0f}" y="{y:.0f}" font-family="{fam}" font-size="{self.size:.1f}" fill="{color}"'
               f'{" font-weight=\"700\"" if self.bold else ""} text-anchor="{self.anchor}">']
        for i, line in enumerate(self.lines):
            body = spans(line, self.size, fill_in)
            if i == 0 and self.label:  # the label is bold, the text after it is not
                lab = escape(self.label) + ':'
                body = body.replace(lab, f'<tspan font-weight="700">{lab}</tspan>', 1)
            out.append(f'<tspan x="{x:.0f}" dy="{self.size * (0.95 if i == 0 else self.lead):.1f}">{body}</tspan>')
        return ''.join(out) + '</text>'


def text(x, y, s, size, fill=DARK, bold=False, anchor='middle', serif=False):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{SERIF if serif else SANS}" font-size="{size:.1f}" fill="{fill}"'
            f'{" font-weight=\"700\"" if bold else ""} text-anchor="{anchor}">{escape(s)}</text>')


def tint(hexcolor, k=0.16):
    r, g, b = (int(hexcolor[i:i + 2], 16) for i in (1, 3, 5))
    return '#%02x%02x%02x' % tuple(round(255 - (255 - v) * k) for v in (r, g, b))


def ink(hexcolor):
    """The color, darkened when it is too light to carry white text."""
    r, g, b = (int(hexcolor[i:i + 2], 16) for i in (1, 3, 5))
    k = min(1.0, 0.42 / max(0.01, (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255))
    return '#%02x%02x%02x' % tuple(round(v * k) for v in (r, g, b))


def theme_name(c):
    return c.get('theme') or THEMES[int(hashlib.md5(c['id'].encode()).hexdigest()[:6], 16) % len(THEMES)]


def theme(name, color):
    """Colors and strokes for one look. solid is what numbers and column heads sit on; on_solid is their text."""
    if name == 'ink':  # ink saver: nothing filled, dark lines
        return dict(name=name, color=DARK, bg='#fff', card='#fff', stroke=DARK, sw=2, solid='#fff', solid_stroke=DARK,
                    on_solid=DARK, light='#fff', label='#fff', idea=DARK, title=DARK, band=False, rx=10)
    c = ink(color)
    t = dict(name=name, color=c, solid=c, solid_stroke='none', on_solid='#fff', idea='#3a3f4b', title=DARK)
    if name == 'bold':  # a color band across the top, tinted boxes without outlines
        t.update(bg='#fff', card=tint(c, 0.10), stroke='none', sw=0, light=tint(c, 0.26), label=tint(c, 0.26), band=True, rx=18)
    elif name == 'soft':  # a tinted page, white boxes with light outlines, a colored title
        t.update(bg=tint(c, 0.07), card='#fff', stroke=tint(c, 0.5), sw=2, light=tint(c, 0.15), label=tint(c, 0.15), band=False,
                 rx=24, title=c)
    else:  # classic: a thin color bar, white boxes outlined in the color
        t.update(bg='#fff', card='#fff', stroke=c, sw=2.5, light=tint(c), label=tint(c), band=False, rx=14)
    return t


def box(x, y, w, h, T, fill=None, stroke=None, sw=None, rx=None, dash=None):
    st = stroke or T['stroke']
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx if rx is not None else T["rx"]}" '
            f'fill="{fill or T["card"]}" stroke="{st}" stroke-width="{sw if sw is not None else T["sw"]}"'
            f'{f" stroke-dasharray=\"{dash}\"" if dash else ""}/>')


def pick(pair, lang):
    return pair[0] if lang == 'en' else pair[1]


def body_items(c, lang):
    return [it[lang] for it in c['items']]


def head(c, lang, fill_in, s, T):
    """The title (and idea line): elements and the y below them."""
    W, H = dims(c)
    el = []
    if T['band']:
        title = Text(pick(c['title'], lang), 52 * min(s, 1.1), W - 2 * M, bold=True, serif=True, lead=1.1)
        bh = title.h + 60
        el.append(f'<rect x="0" y="0" width="{W}" height="{bh:.0f}" fill="{T["color"]}"/>')
        el.append(f'<circle cx="{W - 70}" cy="{bh - 6:.0f}" r="44" fill="{tint(T["color"], 0.45)}" opacity="0.5"/>')
        el.append(title.svg(M, 30, fill_in, '#fff'))
        y = bh + 26
    else:
        if T['name'] == 'soft':
            el.append(f'<circle cx="{W - 40}" cy="30" r="120" fill="{T["light"]}"/>')
            el.append(f'<circle cx="{W - 175}" cy="-10" r="60" fill="{tint(T["color"], 0.28)}"/>')
        else:
            el.append(f'<rect x="0" y="0" width="{W}" height="{16 if T["name"] == "classic" else 8}" fill="{T["color"]}"/>')
        title = Text(pick(c['title'], lang), 52 * min(s, 1.1), W - 2 * M - (90 if T['name'] == 'soft' else 0), bold=True, serif=True, lead=1.1)
        el.append(title.svg(M, M, fill_in, T['title']))
        y = M + title.h + 14
    if c.get('idea') and c['layout'] != 'big-idea':
        idea = Text(pick(c['idea'], lang), 28 * min(s, 1.15), W - 2 * M, lead=1.25)
        el.append(idea.svg(M, y, fill_in, T['idea']))
        y += idea.h + 24
    else:
        y += 10 * s
    return el, y


def layout(c, lang, fill_in, s, T, pad=0.0):
    """SVG elements, the bottom y of everything and how many boxes can stretch, at text scale s; pad is extra
    height for each stretchy box, to spread a short chart down the page."""
    W, H = dims(c)
    el, y = head(c, lang, fill_in, s, T)
    color, light = T['color'], T['light']
    lay = c['layout']
    gap = 18 * s
    if lay == 'steps':
        r = 28 * s
        tx = M + 2 * r + 24 * s
        items = body_items(c, lang)
        for i, (label, text_) in enumerate(items, 1):
            t = Text(text_, 25 * s, W - M - tx - 16 * s, label=label)
            h = max(t.h + 28 * s, 2 * r + 20 * s) + pad
            el.append(box(M, y, W - 2 * M, h, T))
            cy = y + h / 2
            el.append(f'<circle cx="{M + r + 12 * s:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{T["solid"]}" stroke="{T["solid_stroke"]}" stroke-width="2.5"/>')
            el.append(text(M + r + 12 * s, cy + 10 * s, str(i), 28 * s, T['on_solid'], True))
            el.append(t.svg(tx, y + (h - t.h) / 2, fill_in))
            y += h
            if i < len(items):
                ax = M + r + 12 * s
                el.append(f'<path d="M{ax:.0f} {y + 3:.0f} l-9 0 l9 {gap - 6:.0f} l9 -{gap - 6:.0f} z" fill="{color}"/>')
                y += gap
    elif lay == 'parts':
        items = body_items(c, lang)
        longest = max(measure(w, 1, bold=True) for label, _ in items for w in label.split())
        lw = min(max(230, longest * 27 * s / 0.92 + 30), 300)  # one long word (Multiplicidad) widens the label cell,
        ls = min(27 * s, (lw - 30) * 0.92 / longest)  # then shrinks the labels if it still does not fit
        for label, text_ in items:
            lt = Text(label, ls, lw - 30, bold=True, lead=1.1)
            t = Text(text_, 24 * s, W - 2 * M - lw - 34)
            h = max(lt.h, t.h) + 30 * s + pad
            r = min(T['rx'], h / 2)
            el.append(box(M, y, W - 2 * M, h, T))
            el.append(f'<path d="M{M + r:.1f} {y:.1f} h{lw - r:.1f} v{h:.1f} h-{lw - r:.1f} a{r:.1f} {r:.1f} 0 0 1 -{r:.1f} -{r:.1f} '
                      f'v-{h - 2 * r:.1f} a{r:.1f} {r:.1f} 0 0 1 {r:.1f} -{r:.1f} z" fill="{T["label"]}" stroke="{T["stroke"]}" stroke-width="{T["sw"]}"/>')
            el.append(lt.svg(M + 16, y + (h - lt.h) / 2, False))
            el.append(t.svg(M + lw + 18, y + (h - t.h) / 2, fill_in))
            y += h + gap
        y -= gap
    elif lay == 'list':  # numbered, in two columns: down the left, then down the right
        items = body_items(c, lang)
        n, cols = len(items), 2
        rows = math.ceil(n / cols)
        cw = (W - 2 * M - 20) / cols
        r = 20 * s
        cells = [Text(text_, 22 * s, cw - 2 * r - 44 * s, label=label) for label, text_ in items]
        for row in range(rows):
            group = [(k, cells[k]) for k in (row, row + rows) if k < n]
            rh = max(t.h for _, t in group) + 28 * s + pad
            for j, (k, t) in enumerate(group):
                x0 = M + j * (cw + 20)
                el.append(box(x0, y, cw, rh, T))
                el.append(f'<circle cx="{x0 + r + 12 * s:.1f}" cy="{y + rh / 2:.1f}" r="{r:.1f}" fill="{T["solid"]}" stroke="{T["solid_stroke"]}" stroke-width="2"/>')
                el.append(text(x0 + r + 12 * s, y + rh / 2 + 7.5 * s, str(k + 1), 21 * s, T['on_solid'], True))
                el.append(t.svg(x0 + 2 * r + 28 * s, y + (rh - t.h) / 2, fill_in))
            y += rh + 14 * s
        y -= 14 * s
    elif lay == 'cycle':
        items = body_items(c, lang)
        n = len(items)
        bw = 350 if n <= 4 else 250  # five boxes: the two low ones must clear each other
        boxes = []
        for label, text_ in items:
            lt = Text(label, 25 * s, bw - 28, bold=True, lead=1.1, anchor='middle')
            t = Text(text_, 21 * s, bw - 28, lead=1.22, anchor='middle')
            boxes.append((lt, t, lt.h + t.h + 34 * s))
        bh = max(b[2] for b in boxes)
        avail = H - FOOT - M - y - (90 * s if c.get('example') else 0)
        cx, cy = W / 2, y + avail / 2
        rx, ry = (W - 2 * M - bw) / 2, (avail - bh) / 2
        el.append(f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="none" stroke="{color}" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>')
        pts = [(cx + rx * math.sin(2 * math.pi * k / n), cy - ry * math.cos(2 * math.pi * k / n)) for k in range(n)]
        for k in range(n):  # an arrowhead halfway to the next box, pointing clockwise
            a = 2 * math.pi * (k + 0.5) / n
            px, py = cx + rx * math.sin(a), cy - ry * math.cos(a)
            dx, dy = rx * math.cos(a), ry * math.sin(a)
            d = math.hypot(dx, dy) or 1
            ux, uy = dx / d, dy / d
            el.append(f'<path d="M{px + ux * 16:.1f} {py + uy * 16:.1f} L{px - ux * 10 - uy * 13:.1f} {py - uy * 10 + ux * 13:.1f} '
                      f'L{px - ux * 10 + uy * 13:.1f} {py - uy * 10 - ux * 13:.1f} z" fill="{color}"/>')
        for (lt, t, h), (px, py) in zip(boxes, pts):
            x0, y0 = px - bw / 2, py - bh / 2
            el.append(box(x0, y0, bw, bh, T, sw=T['sw'] and 3, rx=16))
            el.append(box(x0, y0, bw, lt.h + 16 * s, T, fill=light, stroke='none', sw=0, rx=16))
            el.append(lt.svg(px, y0 + 10 * s, False))
            el.append(t.svg(px, y0 + lt.h + 24 * s, fill_in))
        clear = all(abs(a[0] - b[0]) >= bw + 30 or abs(a[1] - b[1]) >= bh + 44  # room between boxes for the arrows
                    for i, a in enumerate(pts) for b in pts[i + 1:])
        y = cy + ry + bh / 2 if clear else H * 2  # boxes too big: draw it again smaller
    elif lay == 'compare':
        cols = c['cols']
        n = len(cols)
        cg = 18
        cw = (W - 2 * M - cg * (n - 1)) / n
        cs = min(s, 1.8 if n == 2 else 1.55)  # narrow columns read badly in huge type
        heads = [Text(pick(col['name'], lang), (30 if n == 2 else 26) * min(s, 1.6 if n == 2 else 1.2), cw - 24, bold=True, lead=1.1, anchor='middle') for col in cols]
        hh = max(t.h for t in heads) + 26 * s
        cells = [[Text(text_, (23 if n == 2 else 20) * cs, cw - 40, label=label) for label, text_ in (it[lang] for it in col['items'])] for col in cols]
        ch = max(sum(t.h + 24 * s + pad for t in col) for col in cells) + 10 * s
        r = min(T['rx'], 20)
        for i, (hd, col) in enumerate(zip(heads, cells)):
            x0 = M + i * (cw + cg)
            el.append(box(x0, y, cw, hh + ch, T, sw=T['sw'] and 3, rx=r))
            el.append(f'<path d="M{x0 + r:.0f} {y:.0f} h{cw - 2 * r:.0f} a{r} {r} 0 0 1 {r} {r} v{hh - r:.0f} h-{cw:.0f} v-{hh - r:.0f} a{r} {r} 0 0 1 {r} -{r} z" '
                      f'fill="{T["solid"]}" stroke="{T["solid_stroke"]}" stroke-width="2"/>')
            el.append(hd.svg(x0 + cw / 2, y + (hh - hd.h) / 2, False, T['on_solid']))
            yy = y + hh + 14 * s
            for t in col:
                el.append(f'<circle cx="{x0 + 18:.0f}" cy="{yy + pad / 2 + t.size * 0.6:.0f}" r="{5 * s:.1f}" fill="{color}"/>')
                el.append(t.svg(x0 + 32, yy + pad / 2, fill_in))
                yy += t.h + 24 * s + pad
        y += hh + ch
    elif lay == 'big-idea':
        idea = Text(pick(c['idea'], lang), 40 * min(s, 1.25), W - 2 * M - 60, serif=True, lead=1.18, anchor='middle')
        bh = idea.h + 56 * s
        el.append(box(M, y, W - 2 * M, bh, T, fill=light, stroke=color, sw=0 if T['name'] == 'bold' else 4, rx=22))
        el.append(idea.svg(W / 2, y + 28 * s, fill_in))
        y += bh + 26 * s
        items = body_items(c, lang)
        cols = 2 if len(items) in (2, 4) else 1
        cw = (W - 2 * M - 20 * (cols - 1)) / cols
        cards = [Text(text_, 24 * s, cw - 40, label=label) for label, text_ in items]
        for row in range(0, len(cards), cols):
            group = cards[row:row + cols]
            rh = max(t.h for t in group) + 34 * s + pad
            for j, t in enumerate(group):
                x0 = M + j * (cw + 20)
                el.append(box(x0, y, cw, rh, T))
                el.append(t.svg(x0 + 20, y + (rh - t.h) / 2, fill_in))
            y += rh + 16 * s
        y -= 16 * s
    elif lay == 'grid':
        y = DRAWN[c['grid']](c, el, y, T, lang)
    if c.get('example'):
        y += 26 * s
        lab = 'Example' if lang == 'en' else 'Ejemplo'
        t = Text(pick(c['example'], lang), 23 * s, W - 2 * M - 40, label=lab)
        el.append(box(M, y, W - 2 * M, t.h + 30 * s, T, stroke=color, sw=2, dash='8 6'))
        el.append(t.svg(M + 20, y + 15 * s, fill_in))
        y += t.h + 30 * s
    stretch = {'steps': len(c['items']), 'parts': len(c['items']), 'list': math.ceil(len(c['items']) / 2),
               'big-idea': math.ceil(len(c['items']) / (2 if len(c['items']) in (2, 4) else 1)),
               'compare': max((len(col['items']) for col in c['cols']), default=0)}.get(lay, 0)
    return el, y, stretch


# ---------- drawn posters (layout: grid) ----------
# each takes (chart, elements, top y, theme, lang), appends its drawing and returns the bottom y

def L(lang, en, es):
    return en if lang == 'en' else es


def g_hundred(c, el, y, T, lang):
    W, H = dims(c)
    n, cell = 10, min((W - 2 * M) / 10, (H - FOOT - M - y) / 10)
    x0 = (W - cell * n) / 2
    for k in range(100):
        r, col = divmod(k, 10)
        ten = (k + 1) % 10 == 0
        el.append(box(x0 + col * cell, y + r * cell, cell, cell, T, fill=T['light'] if ten else '#fff', stroke=T['color'], sw=1.5, rx=0))
        el.append(text(x0 + col * cell + cell / 2, y + r * cell + cell * 0.64, str(k + 1), cell * 0.4, bold=ten))
    return y + cell * n


def g_times(c, el, y, T, lang):
    W, H = dims(c)
    n = 13
    cell = min((W - 2 * M) / n, (H - FOOT - M - y) / n)
    x0 = (W - cell * n) / 2
    for r in range(n):
        for col in range(n):
            hd = r == 0 or col == 0
            sq = r == col and r > 0
            label = '×' if r == col == 0 else str(max(r, col) if hd else r * col)
            fill = T['solid'] if hd else T['light'] if sq else '#fff'
            el.append(box(x0 + col * cell, y + r * cell, cell, cell, T, fill=fill, stroke=T['color'], sw=1.2, rx=0))
            el.append(text(x0 + col * cell + cell / 2, y + r * cell + cell * 0.64, label, cell * 0.38, T['on_solid'] if hd else DARK, hd))
    return y + cell * n


def g_numberline(c, el, y, T, lang):
    """A vertical number line (it reads like a thermometer): 0 to 20, or -10 to 10 with the two sides named."""
    W, H = dims(c)
    a, b = (int(v) for v in c.get('range', '0 20').split())
    top, bottom = y + 30, H - FOOT - M - 20
    step = (bottom - top) / (b - a)
    x = W / 2 + (60 if a >= 0 else -60)
    el.append(f'<line x1="{x}" y1="{top - 24:.0f}" x2="{x}" y2="{bottom + 24:.0f}" stroke="{T["color"]}" stroke-width="6" stroke-linecap="round"/>')
    for yy, d in ((top - 30, -1), (bottom + 30, 1)):  # arrowheads: the line goes on forever
        el.append(f'<path d="M{x - 14} {yy - d * 16:.0f} L{x} {yy:.0f} L{x + 14} {yy - d * 16:.0f}" fill="none" stroke="{T["color"]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
    for v in range(b, a - 1, -1):
        yy = top + (b - v) * step
        big = v % 5 == 0
        el.append(f'<line x1="{x - (26 if big else 16)}" y1="{yy:.1f}" x2="{x + (26 if big else 16)}" y2="{yy:.1f}" stroke="{T["color"]}" stroke-width="{4 if big else 2.5}"/>')
        if v == 0:
            el.append(f'<circle cx="{x}" cy="{yy:.1f}" r="13" fill="{T["solid"]}" stroke="{T["solid_stroke"]}" stroke-width="2"/>')
        el.append(text(x + 44, yy + min(step * 0.8, 40) * 0.36, str(v).replace('-', '−'), min(step * 0.8, 40), bold=big or v == 0, anchor='start'))
        if a >= 0:  # the number word on the other side, for readers still learning them
            el.append(text(x - 44, yy + min(step * 0.6, 30) * 0.36, (NUM_EN if lang == 'en' else NUM_ES)[v], min(step * 0.6, 30), '#3a3f4b', anchor='end'))
    if a < 0:  # name the two sides with a bracket
        for lo, hi, label in ((1, b, L(lang, 'Positive numbers', 'Números positivos')), (a, -1, L(lang, 'Negative numbers', 'Números negativos'))):
            y1, y2 = top + (b - hi) * step, top + (b - lo) * step
            bx = x - 70
            el.append(f'<path d="M{bx + 16} {y1:.0f} h-16 v{y2 - y1:.0f} h16" fill="none" stroke="{T["color"]}" stroke-width="3"/>')
            t = Text(label, 24, 200, bold=True, anchor='end')
            el.append(t.svg(bx - 14, (y1 + y2) / 2 - t.h / 2, False))
        el.append(text(x + 90, top + b * step + step * 0.22, L(lang, '← zero', '← cero'), 20, T['color'], anchor='start'))
    return bottom + 6


NUM_EN = ('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen '
          'eighteen nineteen twenty').split()
NUM_ES = ('cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince dieciséis diecisiete '
          'dieciocho diecinueve veinte').split()


def frac(x, y, n, d, size, fill=DARK):
    """A stacked fraction centered on x, with its bar at y."""
    w = max(measure(str(n), size), measure(str(d), size)) + 6
    return (text(x, y - size * 0.18, str(n), size, fill, True) + text(x, y + size * 0.86, str(d), size, fill, True)
            + f'<line x1="{x - w / 2:.1f}" y1="{y:.1f}" x2="{x + w / 2:.1f}" y2="{y:.1f}" stroke="{fill}" stroke-width="2"/>')


def g_fractions(c, el, y, T, lang):
    """A fraction wall: one whole, then halves through twelfths, each row the same length."""
    W, H = dims(c)
    dens = [1, 2, 3, 4, 5, 6, 8, 10, 12]
    rh = (H - FOOT - M - y) / len(dens)
    bw = W - 2 * M
    for i, d in enumerate(dens):
        yy = y + i * rh
        fill = '#fff' if T['name'] == 'ink' else tint(T['color'], 0.12 + 0.30 * (i % 3) / 2)
        for k in range(d):
            el.append(box(M + k * bw / d, yy + 4, bw / d, rh - 8, T, fill=fill, stroke=T['color'], sw=2, rx=6))
            cx = M + (k + 0.5) * bw / d
            if d == 1:
                el.append(text(cx, yy + rh / 2 + 12, L(lang, '1 whole', '1 entero'), 32, bold=True))
            else:
                el.append(frac(cx, yy + rh / 2 - 4, 1, d, min(38, rh * 0.36, bw / d * 0.5)))
    return y + rh * len(dens)


def g_coordinate(c, el, y, T, lang):
    """The coordinate plane from -10 to 10, with the four quadrants and their signs."""
    W, H = dims(c)
    size = min(W - 2 * M - 20, H - FOOT - M - y - 70)
    u = size / 20
    x0, y0 = (W - size) / 2, y + 10
    ox, oy = x0 + size / 2, y0 + size / 2
    for k in range(21):
        st = 'stroke="#c9ccd3" stroke-width="1"'
        el.append(f'<line x1="{x0 + k * u:.1f}" y1="{y0:.1f}" x2="{x0 + k * u:.1f}" y2="{y0 + size:.1f}" {st}/>')
        el.append(f'<line x1="{x0:.1f}" y1="{y0 + k * u:.1f}" x2="{x0 + size:.1f}" y2="{y0 + k * u:.1f}" {st}/>')
    quads = [('II', '(−, +)', -1, -1), ('I', '(+, +)', 1, -1), ('III', '(−, −)', -1, 1), ('IV', '(+, −)', 1, 1)]
    for name, signs, sx, sy in quads:
        qx, qy = ox + sx * size / 4, oy + sy * size / 4
        el.append(box(qx - 92, qy - 56, 184, 112, T, fill=T['light'] if T['name'] != 'ink' else '#fff', stroke=T['color'], sw=2, rx=14))
        el.append(text(qx, qy - 8, L(lang, 'Quadrant ', 'Cuadrante ') + name, 22, T['color'] if T['name'] != 'ink' else DARK, True))
        el.append(text(qx, qy + 30, signs, 28, bold=True))
    for k in range(-10, 11):
        if k and k % 2 == 0:
            el.append(text(ox + k * u, oy + 22, str(k).replace('-', '−'), 15))
            el.append(text(ox - 8, oy - k * u + 5, str(k).replace('-', '−'), 15, anchor='end'))
    for x1, y1, x2, y2 in ((x0 - 6, oy, x0 + size + 6, oy), (ox, y0 + size + 6, ox, y0 - 6)):
        el.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{DARK}" stroke-width="3.5"/>')
    el.append(f'<path d="M{x0 + size + 16:.1f} {oy:.1f} l-16 -9 v18 z M{ox:.1f} {y0 - 16:.1f} l-9 16 h18 z" fill="{DARK}"/>')
    el.append(text(x0 + size + 4, oy - 14, 'x', 26, bold=True, anchor='end', serif=True))
    el.append(text(ox + 14, y0 + 6, 'y', 26, bold=True, anchor='start', serif=True))
    el.append(f'<circle cx="{ox:.1f}" cy="{oy:.1f}" r="7" fill="{T["color"]}"/>')
    yy = y0 + size + 44
    el.append(text(W / 2, yy, L(lang, 'The origin is (0, 0). A point is (x, y): across first, then up or down.',
                                'El origen es (0, 0). Un punto es (x, y): primero a lo ancho, luego arriba o abajo.'), 21))
    return yy + 10


def g_unitcircle(c, el, y, T, lang):
    """The unit circle: every 30 and 45 degree angle, in degrees and radians, with (cos, sin)."""
    W, H = dims(c)
    r = 250
    cx, cy = W / 2, y + 30 + (H - FOOT - M - y - 60) / 2
    el.append(f'<line x1="{cx - r - 50}" y1="{cy}" x2="{cx + r + 50}" y2="{cy}" stroke="{DARK}" stroke-width="2.5"/>')
    el.append(f'<line x1="{cx}" y1="{cy - r - 50}" x2="{cx}" y2="{cy + r + 50}" stroke="{DARK}" stroke-width="2.5"/>')
    el.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{T["light"] if T["name"] != "ink" else "#fff"}" stroke="{T["color"]}" stroke-width="5"/>')
    rt2, rt3 = '√2/2', '√3/2'
    vals = {0: ('1', '0'), 30: (rt3, '1/2'), 45: (rt2, rt2), 60: ('1/2', rt3), 90: ('0', '1')}
    rad = {0: '0', 30: 'π/6', 45: 'π/4', 60: 'π/3', 90: 'π/2', 120: '2π/3', 135: '3π/4', 150: '5π/6', 180: 'π',
           210: '7π/6', 225: '5π/4', 240: '4π/3', 270: '3π/2', 300: '5π/3', 315: '7π/4', 330: '11π/6'}
    for deg, rd in rad.items():
        ref = deg % 180 if deg % 180 <= 90 else 180 - deg % 180
        cs, sn = vals[ref]
        cs = ('−' if 90 < deg < 270 else '') + cs if cs != '0' else cs
        sn = ('−' if deg > 180 else '') + sn if sn != '0' else sn
        a = math.radians(deg)
        px, py = cx + r * math.cos(a), cy - r * math.sin(a)
        el.append(f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="{T["color"]}" stroke-width="1.2" opacity="0.5"/>')
        el.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7" fill="{T["solid"]}" stroke="{DARK if T["name"] == "ink" else "none"}" stroke-width="2"/>')
        lx, ly = cx + (r + 78) * math.cos(a), cy - (r + 56) * math.sin(a)
        el.append(text(lx, ly - 12, f'{deg}° · {rd}', 19, T['color'] if T['name'] != 'ink' else DARK, True))
        el.append(text(lx, ly + 11, f'({cs}, {sn})', 18))
    el.append(text(cx + 70, cy + 90, '(cos θ, sin θ)', 24, bold=True, serif=True))
    el.append(text(cx + 70, cy + 120, L(lang, 'radius 1', 'radio 1'), 19))
    return cy + r + 80


COINS = [('penny', 'un centavo', 1, 19.05, '#c27a4a'), ('nickel', 'cinco centavos', 5, 21.21, '#b9bcc2'),
         ('dime', 'diez centavos', 10, 17.91, '#c9ccd1'), ('quarter', 'veinticinco centavos', 25, 24.26, '#b4b7bd')]


def g_coins(c, el, y, T, lang):
    """The four coins, drawn to scale with each other, with their values."""
    W, H = dims(c)
    ch = (H - FOOT - M - y - 80) / 2
    cw = (W - 2 * M - 30) / 2
    k = min(cw, ch - 110) / 24.26 * 0.86
    for i, (name, es, cents, mm, metal) in enumerate(COINS):
        x0, y0 = M + (i % 2) * (cw + 30), y + (i // 2) * (ch + 20)
        el.append(box(x0, y0, cw, ch, T))
        r = mm * k / 2
        cx, cy = x0 + cw / 2, y0 + 20 + (ch - 120) / 2
        fill = '#fff' if T['name'] == 'ink' else metal
        el.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{DARK}" stroke-width="3"/>')
        el.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r - 9:.1f}" fill="none" stroke="{DARK}" stroke-width="1.5" opacity="0.35"/>')
        el.append(text(cx, cy + r * 0.2, f'{cents}¢', r * 0.6, bold=True))
        label = name if lang == 'en' else es
        el.append(text(cx, y0 + ch - 58, label, min(34, (cw - 30) / measure(label, 1, True, True)), bold=True, serif=True))
        el.append(text(cx, y0 + ch - 22, (f'{cents} cent' + ('s' if cents > 1 else '')) if lang == 'en' else f'({name})', 24, '#3a3f4b'))
    yy = y + 2 * ch + 20 + 52
    el.append(text(W / 2, yy, L(lang, '100¢ = $1.00', '100¢ = $1.00 (un dólar)'), 40, T['color'] if T['name'] != 'ink' else DARK, True, serif=True))
    return yy + 10


def rings(d):
    """Polygons [(x, y), ...] from an SVG path of M, L and Z commands."""
    out = []
    for part in re.split(r'(?=M)', d):
        pts = [(float(a), float(b)) for a, b in re.findall(r'(-?[\d.]+)[ ,](-?[\d.]+)', part)]
        if len(pts) > 2:
            out.append(pts)
    return out


def centroid(pts):
    a = cx = cy = 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        f = x1 * y2 - x2 * y1
        a += f
        cx += (x1 + x2) * f
        cy += (y1 + y2) * f
    if abs(a) < 1e-9:
        return pts[0]
    return cx / (3 * a), cy / (3 * a)


ES_STATES = {'Hawaii': 'Hawái', 'Louisiana': 'Luisiana', 'Mississippi': 'Misisipi', 'Missouri': 'Misuri',
             'New Hampshire': 'Nuevo Hampshire', 'New Jersey': 'Nueva Jersey', 'New Mexico': 'Nuevo México',
             'New York': 'Nueva York', 'North Carolina': 'Carolina del Norte', 'North Dakota': 'Dakota del Norte',
             'Pennsylvania': 'Pensilvania', 'South Carolina': 'Carolina del Sur', 'South Dakota': 'Dakota del Sur',
             'West Virginia': 'Virginia Occidental'}
CALLOUT = ['VT', 'NH', 'MA', 'RI', 'CT', 'NJ', 'DE', 'MD']  # too small to hold their own labels


def g_usmap(c, el, y, T, lang):
    """The 50 states (shapes from the Me on the Map tool) with their postal abbreviations, and a list below."""
    W, H = dims(c)
    states = json.loads((ROOT / 'tools' / 'me-on-the-map' / 'states.json').read_text(encoding='utf-8'))
    names = sorted((st['n'], st['a']) for st in states)
    rows = 5
    list_h = rows * 19 + 10
    mx0, mx1, my0, my1 = 18, 882, 25, 531  # the shapes' bounding box
    k = min((W - 2 * M - 70) / (mx1 - mx0), (H - FOOT - M - y - list_h - 16) / (my1 - my0))
    ox, oy = M + 10 - mx0 * k, y - my0 * k
    shades = [tint(T['color'], v) for v in (0.22, 0.36, 0.5, 0.3)] if T['name'] != 'ink' else ['#fff'] * 4
    for i, st in enumerate(states):
        el.append(f'<path d="{st["d"]}" transform="translate({ox:.1f} {oy:.1f}) scale({k:.4f})" fill="{shades[(i * 7) % 4]}" '
                  f'stroke="{"#fff" if T["name"] != "ink" else DARK}" stroke-width="{1.3 / k:.2f}"/>')
    for st in states:
        big = max(rings(st['d']), key=lambda p: abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(p, p[1:] + p[:1]))))
        px, py = centroid(big)
        px, py = ox + px * k, oy + py * k
        if st['a'] in CALLOUT:
            i = CALLOUT.index(st['a'])
            lx, ly = W - M - 22, y + 70 + i * 34
            el.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{lx - 22:.1f}" y2="{ly - 6:.1f}" stroke="{DARK}" stroke-width="1"/>')
            el.append(text(lx, ly, st['a'], 16, bold=True))
        else:
            if st['a'] == 'FL':
                px += 18 * k
            elif st['a'] == 'MI':
                px, py = px + 14 * k, py + 20 * k
            elif st['a'] == 'LA':
                px -= 10 * k
            el.append(text(px, py + 5, st['a'], 14 if st['a'] not in ('AK', 'TX', 'CA', 'MT') else 18, bold=True))
    yy = H - FOOT - M - list_h + 22
    colw = (W - 2 * M) / 10
    for i, (n, a) in enumerate(names):
        col, row = divmod(i, rows)
        name = n if lang == 'en' else ES_STATES.get(n, n)
        el.append(f'<text x="{M + col * colw:.1f}" y="{yy + row * 19:.1f}" font-family="{SANS}" font-size="{min(12.5, (colw - 30) / measure(name, 1)):.1f}" fill="{DARK}">'
                  f'<tspan font-weight="700">{a}</tspan> {escape(name)}</text>')
    return H - FOOT - M


def equal_earth(world, lon, lat):
    A1, A2, A3, A4, Mq = 1.340264, -.081106, .000893, .003796, math.sqrt(3) / 2
    t = math.asin(Mq * math.sin(math.radians(lat)))
    x = 2 * math.sqrt(3) * math.radians(lon) * math.cos(t) / (3 * (9 * A4 * t ** 8 + 7 * A3 * t ** 6 + 3 * A2 * t * t + A1))
    yv = A4 * t ** 9 + A3 * t ** 7 + A2 * t ** 3 + A1 * t
    return (x + world['xmax']) * world['s'], (world['ymax'] - yv) * world['s']


CONTINENTS = [('North America', 'América del Norte', -102, 44), ('South America', 'América del Sur', -60, -14),
              ('Europe', 'Europa', 18, 53), ('Africa', 'África', 19, 6), ('Asia', 'Asia', 90, 45),
              ('Australia', 'Australia', 134, -25), ('Antarctica', 'Antártida', 20, -79)]
OCEANS = [('Pacific Ocean', 'Océano Pacífico', -140, 16), ('Atlantic Ocean', 'Océano Atlántico', -38, 22),
          ('Indian Ocean', 'Océano Índico', 76, -24), ('Arctic Ocean', 'Océano Ártico', -5, 83),
          ('Southern Ocean', 'Océano Austral', -100, -62), ('Pacific Ocean', 'Océano Pacífico', 152, 20)]


def g_worldmap(c, el, y, T, lang):
    """The seven continents and five oceans on an Equal Earth map (land from the Art Passport tool)."""
    W, H = dims(c)
    world = json.loads((ROOT / 'tools' / 'art-passport' / 'world.json').read_text(encoding='utf-8'))
    mh = 2 * world['ymax'] * world['s']  # the whole globe; world['h'] stops where the land does
    k = min((W - 2 * M) / world['w'], (H - FOOT - M - y - 110) / mh)
    ox, oy = (W - world['w'] * k) / 2, y
    tr = f'translate({ox:.1f} {oy:.1f}) scale({k:.4f})'
    sea, land = ('#fff', '#fff') if T['name'] == 'ink' else ('#e3eff6', tint(T['color'], 0.42))
    edge = [equal_earth(world, -180, lat) for lat in range(-90, 91, 5)] + [equal_earth(world, 180, lat) for lat in range(90, -91, -5)]
    el.append(f'<path d="M' + ' L'.join(f'{x:.1f} {yy:.1f}' for x, yy in edge) + f' Z" transform="{tr}" fill="{sea}" stroke="{DARK}" stroke-width="{1.5 / k:.2f}"/>')
    # the land drawing stops short of Antarctica: draw it as a simple band under a wavy coast
    coast = [equal_earth(world, lon, -69 + 3.5 * math.sin(math.radians(lon * 2 + 40))) for lon in range(-180, 181, 6)]
    pole = [equal_earth(world, lon, -90) for lon in (180, -180)]
    el.append(f'<path d="M' + ' L'.join(f'{x:.1f} {yy:.1f}' for x, yy in coast + pole) + f' Z" transform="{tr}" fill="{land}" '
              f'stroke="{DARK if T["name"] == "ink" else ink(T["color"])}" stroke-width="{0.8 / k:.2f}"/>')
    el.append(f'<path d="{world["d"]}" transform="{tr}" fill="{land}" stroke="{DARK if T["name"] == "ink" else ink(T["color"])}" stroke-width="{0.8 / k:.2f}"/>')
    for lat, en, es in ((0, 'Equator', 'Ecuador'),):
        x1, y1 = equal_earth(world, -180, lat)
        x2, _ = equal_earth(world, 180, lat)
        el.append(f'<line x1="{ox + x1 * k:.1f}" y1="{oy + y1 * k:.1f}" x2="{ox + x2 * k:.1f}" y2="{oy + y1 * k:.1f}" stroke="{DARK}" stroke-width="1.5" stroke-dasharray="7 6"/>')
        el.append(text(ox + x1 * k + 60, oy + y1 * k - 7, L(lang, en, es), 14, '#3a3f4b', anchor='start'))
    for en, es, lon, lat in CONTINENTS:
        x, yy = equal_earth(world, lon, lat)
        el.append(text(ox + x * k, oy + yy * k + 8, L(lang, en, es), 26, DARK, True, serif=True))
    for en, es, lon, lat in OCEANS:
        x, yy = equal_earth(world, lon, lat)
        el.append(text(ox + x * k, oy + yy * k + 7, L(lang, en, es), 20, '#2d5d7c' if T['name'] != 'ink' else DARK))
    yy = oy + mh * k + 24
    cx, cy = W - M - 50, yy + 32  # a compass rose
    for ang, lab in zip((0, 90, 180, 270), ('N', 'E', 'S', L(lang, 'W', 'O'))):
        a = math.radians(ang)
        dx, dy = math.sin(a), -math.cos(a)
        el.append(f'<path d="M{cx:.1f} {cy:.1f} L{cx + dx * 30 - dy * 8:.1f} {cy + dy * 30 + dx * 8:.1f} L{cx + dx * 42:.1f} {cy + dy * 42:.1f} '
                  f'L{cx + dx * 30 + dy * 8:.1f} {cy + dy * 30 - dx * 8:.1f} z" fill="{T["solid"] if ang == 0 else "#fff"}" stroke="{DARK}" stroke-width="1.5"/>')
        el.append(text(cx + dx * 58, cy + dy * 58 + 6, lab, 17, bold=True))
    note = Text(L(lang, 'Seven continents and five oceans. The equator splits the Earth into the Northern and Southern Hemispheres.',
                  'Siete continentes y cinco océanos. El ecuador divide la Tierra en el hemisferio norte y el hemisferio sur.'), 21, W - 2 * M - 160)
    el.append(note.svg(M, yy + 8, False))
    return max(yy + 8 + note.h, cy + 60)


CATS = {'alkali': ('Alkali metals', 'Metales alcalinos', '#f6b0a8'), 'alk-earth': ('Alkaline earth metals', 'Metales alcalinotérreos', '#f8cf9a'),
        'transition': ('Transition metals', 'Metales de transición', '#f3e39b'), 'post-trans': ('Post-transition metals', 'Otros metales', '#c9e2a4'),
        'metalloid': ('Metalloids', 'Metaloides', '#a8dcc7'), 'nonmetal': ('Nonmetals', 'No metales', '#a9d3ef'),
        'halogen': ('Halogens', 'Halógenos', '#b9c0f2'), 'noble': ('Noble gases', 'Gases nobles', '#d9b9ef'),
        'lanthanide': ('Lanthanides', 'Lantánidos', '#efb9d8'), 'actinide': ('Actinides', 'Actínidos', '#e3c2b3')}
ES_ELEMENTS = ('Hidrógeno Helio Litio Berilio Boro Carbono Nitrógeno Oxígeno Flúor Neón Sodio Magnesio Aluminio Silicio Fósforo Azufre Cloro '
               'Argón Potasio Calcio Escandio Titanio Vanadio Cromo Manganeso Hierro Cobalto Níquel Cobre Zinc Galio Germanio Arsénico Selenio '
               'Bromo Kriptón Rubidio Estroncio Itrio Circonio Niobio Molibdeno Tecnecio Rutenio Rodio Paladio Plata Cadmio Indio Estaño '
               'Antimonio Telurio Yodo Xenón Cesio Bario Lantano Cerio Praseodimio Neodimio Prometio Samario Europio Gadolinio Terbio '
               'Disprosio Holmio Erbio Tulio Iterbio Lutecio Hafnio Tántalo Wolframio Renio Osmio Iridio Platino Oro Mercurio Talio Plomo '
               'Bismuto Polonio Astato Radón Francio Radio Actinio Torio Protactinio Uranio Neptunio Plutonio Americio Curio Berkelio '
               'Californio Einstenio Fermio Mendelevio Nobelio Laurencio Rutherfordio Dubnio Seaborgio Bohrio Hasio Meitnerio '
               'Darmstatio Roentgenio Copernicio Nihonio Flerovio Moscovio Livermorio Teneso Oganesón').split()


def elements():
    h = (ROOT / 'tools' / 'elements-inspector' / 'elements-inspector.html').read_text(encoding='utf-8')
    i = h.index('const ELEMENTS = ') + len('const ELEMENTS = ')
    return json.JSONDecoder().raw_decode(h[i:])[0]


def g_periodic(c, el, y, T, lang):
    """The periodic table: number, symbol, name and mass in every cell, colored by family (data from Elements
    Inspector), with the lanthanides and actinides in two rows below."""
    W, H = dims(c)
    legend_h = 58
    cw = (W - 2 * M) / 18
    ch = min(cw * 1.12, (H - FOOT - M - y - legend_h) / 9.4)
    ink_ = T['name'] == 'ink'
    for e in elements():
        if e['isSeries']:
            row, col = (7.4 if e['period'] == 6 else 8.4), 3 + (e['z'] - (57 if e['period'] == 6 else 89))
        else:
            row, col = e['period'] - 1, e['group'] - 1
        x0, y0 = M + col * cw, y + row * ch
        el.append(box(x0 + 1, y0 + 1, cw - 2, ch - 2, T, fill=tint(CATS[e['catKey']][2], 0.45) if ink_ else CATS[e['catKey']][2], stroke=DARK if ink_ else '#fff', sw=1.2 if ink_ else 1, rx=3))
        name = e['name'] if lang == 'en' else ES_ELEMENTS[e['z'] - 1]
        el.append(text(x0 + 5, y0 + ch * 0.2, str(e['z']), ch * 0.16, anchor='start'))
        el.append(text(x0 + cw / 2, y0 + ch * 0.56, e['symbol'], ch * 0.34, bold=True))
        el.append(text(x0 + cw / 2, y0 + ch * 0.75, name, min(ch * 0.135, (cw - 5) / measure(name, 1))))
        el.append(text(x0 + cw / 2, y0 + ch * 0.92, e['mass'].strip('[]'), ch * 0.12, '#3a3f4b'))
    for row, label in ((5, '57-71'), (6, '89-103')):  # the series' place in the main table
        x0, y0 = M + 2 * cw, y + row * ch
        el.append(box(x0 + 1, y0 + 1, cw - 2, ch - 2, T, fill='#fff', stroke=DARK, sw=1, rx=3, dash='3 3'))
        el.append(text(x0 + cw / 2, y0 + ch * 0.58, label, ch * 0.17, bold=True))
    el.append(text(M + 3 * cw, y + 0.42 * ch, L(lang, 'atomic number · symbol · name · atomic mass', 'número atómico · símbolo · nombre · masa atómica'), 15, '#3a3f4b', anchor='start'))
    yy = y + 9.4 * ch + 14
    cats = list(CATS.items())
    colw = (W - 2 * M) / 5
    for i, (key, (en, es, fill)) in enumerate(cats):
        x0, y0 = M + (i % 5) * colw, yy + (i // 5) * 24
        el.append(box(x0, y0, 18, 18, T, fill=tint(fill, 0.45) if ink_ else fill, stroke=DARK, sw=1, rx=3))
        el.append(text(x0 + 26, y0 + 14, L(lang, en, es), 15, anchor='start'))
    return yy + 48


DRAWN = {'hundred': g_hundred, 'times': g_times, 'numberline': g_numberline, 'fractions': g_fractions,
         'coordinate': g_coordinate, 'unitcircle': g_unitcircle, 'coins': g_coins, 'usmap': g_usmap,
         'worldmap': g_worldmap, 'periodic': g_periodic}


def draw(c, lang='en', fill_in=False, color='#e4572e', ink_saver=False):
    """The chart's SVG elements at the biggest text that fits above the footer (a wall chart is read from across the
    room), capped so short charts do not shout."""
    W, H = dims(c)
    T = theme('ink' if ink_saver else theme_name(c), color)
    s, end = 2.0, H - FOOT - M + 8
    while True:
        el, bottom, stretch = layout(c, lang, fill_in, s, T)
        if bottom <= end or s <= 0.55:
            break
        s -= 0.04
    if bottom <= end and stretch and end - bottom > 30:  # spread a short chart down the page
        el, bottom, _ = layout(c, lang, fill_in, s, T, min((end - bottom - 20) / stretch, 110 * s))
    return [f'<rect width="{W}" height="{H}" fill="{T["bg"]}"/>'] + el, bottom <= end


def footer(c, lang):
    W, H = dims(c)
    left = 'Curio Class · curioclass.org' + c['url'] + (' · free under CC BY 4.0' if lang == 'en' else ' · libre bajo CC BY 4.0')
    return f'<text x="{M}" y="{H - M + 10}" font-family="{SANS}" font-size="14" fill="#5e6472">{escape(left)}</text>'


def symbol(c, sid, lang='en', fill_in=False, color='#e4572e', ink_saver=False):
    """A <symbol> of the whole chart for <use>; returns (svg, fits)."""
    W, H = dims(c)
    el, fits = draw(c, lang, fill_in, color, ink_saver)
    return f'<symbol id="{sid}" viewBox="0 0 {W} {H}">' + ''.join(el) + footer(c, lang) + '</symbol>', fits


def svg(c, lang='en', fill_in=False, color='#e4572e', ink_saver=False):
    W, H = dims(c)
    el, _ = draw(c, lang, fill_in, color, ink_saver)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">' + ''.join(el) + footer(c, lang) + '</svg>'


def tiles(n, c=None, overlap=0.06):
    """viewBoxes for an n x n print: each tile is one nth of the chart plus a strip of overlap on every side to
    trim or glue, and the rectangle of the true tile (drawn dashed so the pages line up)."""
    W, H = dims(c or {})
    tw, th = W / n, H / n
    ox, oy = tw * overlap, th * overlap
    return [dict(row=r + 1, col=k + 1, box=f'{k * tw - ox:.1f} {r * th - oy:.1f} {tw + 2 * ox:.1f} {th + 2 * oy:.1f}',
                 cut=(round(k * tw, 1), round(r * th, 1), round(tw, 1), round(th, 1))) for r in range(n) for k in range(n)]


if __name__ == '__main__':
    cid = sys.argv[1]
    found = check_charts.load('chart', [cid]) or check_charts.load('poster', [cid])
    print(svg(found[cid], 'es' if 'es' in sys.argv else 'en', 'fill' in sys.argv, ink_saver='ink' in sys.argv))
