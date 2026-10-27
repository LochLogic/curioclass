r"""Draw anchor charts and posters (docs/SUPPLY-CLOSET-PLAN.md, Phase D) as SVG.

    python scripts/charts.py <chart-id> [fill] [es]     print one chart's SVG (fill: the fill-in version)

check_charts.py reads the files; build_site.py calls symbol() for each version and language, and the page shows
the same symbol through different viewBoxes for one page, 2x2 and 3x3 tiles. Every chart is drawn on an 850 x 1100
grid (US Letter in hundredths of an inch). Text is wrapped here with estimated letter widths, and a layout that does
not fit is drawn again a little smaller until it does (it starts big: a wall chart is read from across the room).
"""
import math, sys
from html import escape

import check_charts

W, H, M = 850, 1100, 50  # page, margin
FOOT = 40  # room kept at the bottom for the footer line
SANS = "'Instrument Sans', 'Segoe UI', Arial, sans-serif"
SERIF = "Fraunces, Georgia, serif"
NARROW, WIDE = set("ijlt.,;:'!|()[]/ fr\"-"), set('mwMW@%')


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

    def svg(self, x, y, fill_in, color='#1f2430'):
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


def tint(hexcolor, k=0.16):
    r, g, b = (int(hexcolor[i:i + 2], 16) for i in (1, 3, 5))
    return '#%02x%02x%02x' % tuple(round(255 - (255 - v) * k) for v in (r, g, b))


def pick(pair, lang):
    return pair[0] if lang == 'en' else pair[1]


def body_items(c, lang):
    return [it[lang] for it in c['items']]


def layout(c, lang, fill_in, s, color, pad=0.0):
    """SVG elements, the bottom y of everything and how many boxes can stretch, at text scale s; pad is extra
    height for each stretchy box, to spread a short chart down the page."""
    el, light = [], tint(color)
    title = Text(pick(c['title'], lang), 52 * min(s, 1.1), W - 2 * M, bold=True, serif=True, lead=1.1)  # titles stay put
    y = M
    el.append(f'<rect x="0" y="0" width="{W}" height="16" fill="{color}"/>')
    el.append(title.svg(M, y, fill_in))
    y += title.h + 14
    lay = c['layout']
    if c.get('idea') and lay != 'big-idea':
        idea = Text(pick(c['idea'], lang), 28 * min(s, 1.15), W - 2 * M, lead=1.25)
        el.append(idea.svg(M, y, fill_in, '#3a3f4b'))
        y += idea.h + 24
    else:
        y += 10 * s
    gap = 18 * s
    if lay == 'steps':
        r = 28 * s
        tx = M + 2 * r + 24 * s
        items = body_items(c, lang)
        for i, (label, text) in enumerate(items, 1):
            t = Text(text, 25 * s, W - M - tx - 16 * s, label=label)
            h = max(t.h + 28 * s, 2 * r + 20 * s) + pad
            el.append(f'<rect x="{M}" y="{y:.0f}" width="{W - 2 * M}" height="{h:.0f}" rx="14" fill="#fff" stroke="{color}" stroke-width="2.5"/>')
            cy = y + h / 2
            el.append(f'<circle cx="{M + r + 12 * s:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{color}"/>')
            el.append(f'<text x="{M + r + 12 * s:.0f}" y="{cy + 10 * s:.0f}" font-family="{SANS}" font-size="{28 * s:.0f}" font-weight="700" fill="#fff" text-anchor="middle">{i}</text>')
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
        for label, text in items:
            lt = Text(label, ls, lw - 30, bold=True, lead=1.1)
            t = Text(text, 24 * s, W - 2 * M - lw - 34)
            h = max(lt.h, t.h) + 30 * s + pad
            el.append(f'<rect x="{M}" y="{y:.0f}" width="{W - 2 * M}" height="{h:.0f}" rx="14" fill="#fff" stroke="{color}" stroke-width="2.5"/>')
            el.append(f'<path d="M{M + 14} {y:.0f} h{lw - 14} v{h:.0f} h-{lw - 14} a14 14 0 0 1 -14 -14 v-{h - 28:.0f} a14 14 0 0 1 14 -14 z" fill="{light}" stroke="{color}" stroke-width="2.5"/>')
            el.append(lt.svg(M + 16, y + (h - lt.h) / 2, False))
            el.append(t.svg(M + lw + 18, y + (h - t.h) / 2, fill_in))
            y += h + gap
        y -= gap
    elif lay == 'cycle':
        items = body_items(c, lang)
        n = len(items)
        bw = 350 if n <= 4 else 250  # five boxes: the two low ones must clear each other
        boxes = []
        for label, text in items:
            lt = Text(label, 25 * s, bw - 28, bold=True, lead=1.1, anchor='middle')
            t = Text(text, 21 * s, bw - 28, lead=1.22, anchor='middle')
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
            el.append(f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{bw}" height="{bh:.0f}" rx="16" fill="#fff" stroke="{color}" stroke-width="3"/>')
            el.append(f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{bw}" height="{lt.h + 16 * s:.0f}" rx="16" fill="{light}"/>')
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
        cells = [[Text(text, (23 if n == 2 else 20) * cs, cw - 40, label=label) for label, text in (it[lang] for it in col['items'])] for col in cols]
        ch = max(sum(t.h + 24 * s + pad for t in col) for col in cells) + 10 * s
        for i, (head, col) in enumerate(zip(heads, cells)):
            x0 = M + i * (cw + cg)
            el.append(f'<rect x="{x0:.0f}" y="{y:.0f}" width="{cw:.0f}" height="{hh + ch:.0f}" rx="16" fill="#fff" stroke="{color}" stroke-width="3"/>')
            el.append(f'<path d="M{x0 + 16:.0f} {y:.0f} h{cw - 32:.0f} a16 16 0 0 1 16 16 v{hh - 16:.0f} h-{cw:.0f} v-{hh - 16:.0f} a16 16 0 0 1 16 -16 z" fill="{color}"/>')
            el.append(head.svg(x0 + cw / 2, y + (hh - head.h) / 2, False, '#fff'))
            yy = y + hh + 14 * s
            for t in col:
                el.append(f'<circle cx="{x0 + 18:.0f}" cy="{yy + pad / 2 + t.size * 0.6:.0f}" r="{5 * s:.1f}" fill="{color}"/>')
                el.append(t.svg(x0 + 32, yy + pad / 2, fill_in))
                yy += t.h + 24 * s + pad
        y += hh + ch
    elif lay == 'big-idea':
        idea = Text(pick(c['idea'], lang), 40 * min(s, 1.25), W - 2 * M - 60, serif=True, lead=1.18, anchor='middle')
        bh = idea.h + 56 * s
        el.append(f'<rect x="{M}" y="{y:.0f}" width="{W - 2 * M}" height="{bh:.0f}" rx="22" fill="{light}" stroke="{color}" stroke-width="4"/>')
        el.append(idea.svg(W / 2, y + 28 * s, fill_in))
        y += bh + 26 * s
        items = body_items(c, lang)
        cols = 2 if len(items) in (2, 4) else 1
        cw = (W - 2 * M - 20 * (cols - 1)) / cols
        cards = [Text(text, 24 * s, cw - 40, label=label) for label, text in items]
        for row in range(0, len(cards), cols):
            group = cards[row:row + cols]
            rh = max(t.h for t in group) + 34 * s + pad
            for j, t in enumerate(group):
                x0 = M + j * (cw + 20)
                el.append(f'<rect x="{x0:.0f}" y="{y:.0f}" width="{cw:.0f}" height="{rh:.0f}" rx="14" fill="#fff" stroke="{color}" stroke-width="2.5"/>')
                el.append(t.svg(x0 + 20, y + (rh - t.h) / 2, fill_in))
            y += rh + 16 * s
        y -= 16 * s
    elif lay == 'grid':
        y = grid(c, el, y, color, light)
    if c.get('example'):
        y += 26 * s
        lab = 'Example' if lang == 'en' else 'Ejemplo'
        t = Text(pick(c['example'], lang), 23 * s, W - 2 * M - 40, label=lab)
        el.append(f'<rect x="{M}" y="{y:.0f}" width="{W - 2 * M}" height="{t.h + 30 * s:.0f}" rx="14" fill="#fff" stroke="{color}" stroke-width="2" stroke-dasharray="8 6"/>')
        el.append(t.svg(M + 20, y + 15 * s, fill_in))
        y += t.h + 30 * s
    stretch = {'steps': len(c['items']), 'parts': len(c['items']), 'big-idea': math.ceil(len(c['items']) / (2 if len(c['items']) in (2, 4) else 1)),
               'compare': max((len(col['items']) for col in c['cols']), default=0)}.get(lay, 0)
    return el, y, stretch


def grid(c, el, y, color, light):
    """Number grids for posters: a hundred chart or a 12 x 12 times table."""
    avail = H - FOOT - M - y
    if c['grid'] == 'hundred':
        n, cell = 10, min((W - 2 * M) / 10, avail / 10)
        x0 = (W - cell * n) / 2
        for k in range(100):
            r, col = divmod(k, 10)
            fill = light if (k + 1) % 10 == 0 else '#fff'
            el.append(f'<rect x="{x0 + col * cell:.1f}" y="{y + r * cell:.1f}" width="{cell:.1f}" height="{cell:.1f}" fill="{fill}" stroke="{color}" stroke-width="1.5"/>')
            el.append(f'<text x="{x0 + col * cell + cell / 2:.1f}" y="{y + r * cell + cell * 0.64:.1f}" font-family="{SANS}" font-size="{cell * 0.4:.1f}" font-weight="{700 if (k + 1) % 10 == 0 else 500}" text-anchor="middle" fill="#1f2430">{k + 1}</text>')
        return y + cell * n
    n = 13
    cell = min((W - 2 * M) / n, avail / n)
    x0 = (W - cell * n) / 2
    for r in range(n):
        for col in range(n):
            head = r == 0 or col == 0
            sq = r == col and r > 0
            label = '×' if r == col == 0 else str(max(r, col) if head else r * col)
            fill = color if head else light if sq else '#fff'
            el.append(f'<rect x="{x0 + col * cell:.1f}" y="{y + r * cell:.1f}" width="{cell:.1f}" height="{cell:.1f}" fill="{fill}" stroke="{color}" stroke-width="1.2"/>')
            el.append(f'<text x="{x0 + col * cell + cell / 2:.1f}" y="{y + r * cell + cell * 0.64:.1f}" font-family="{SANS}" font-size="{cell * 0.38:.1f}" font-weight="{700 if head else 500}" text-anchor="middle" fill="{"#fff" if head else "#1f2430"}">{label}</text>')
    return y + cell * n


def ink(hexcolor):
    """The subject color, darkened when it is too light to carry white text."""
    r, g, b = (int(hexcolor[i:i + 2], 16) for i in (1, 3, 5))
    k = min(1.0, 0.42 / max(0.01, (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255))
    return '#%02x%02x%02x' % tuple(round(v * k) for v in (r, g, b))


def draw(c, lang='en', fill_in=False, color='#e4572e'):
    """The chart's SVG elements at the biggest text that fits above the footer (a wall chart is read from across the
    room), capped so short charts do not shout."""
    color, s, end = ink(color), 2.0, H - FOOT - M + 8
    while True:
        el, bottom, stretch = layout(c, lang, fill_in, s, color)
        if bottom <= end or s <= 0.55:
            break
        s -= 0.04
    if bottom <= end and stretch and end - bottom > 30:  # spread a short chart down the page
        el, bottom, _ = layout(c, lang, fill_in, s, color, min((end - bottom - 20) / stretch, 110 * s))
    return el, bottom <= end


def footer(c, lang):
    left = 'Curio Class · curioclass.org' + c['url'] + (' · free under CC BY 4.0' if lang == 'en' else ' · libre bajo CC BY 4.0')
    return (f'<text x="{M}" y="{H - M + 10}" font-family="{SANS}" font-size="14" fill="#5e6472">{escape(left)}</text>')


def symbol(c, sid, lang='en', fill_in=False, color='#e4572e'):
    """A <symbol> of the whole chart for <use>; returns (svg, fits)."""
    el, fits = draw(c, lang, fill_in, color)
    return (f'<symbol id="{sid}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>'
            + ''.join(el) + footer(c, lang) + '</symbol>'), fits


def svg(c, lang='en', fill_in=False, color='#e4572e'):
    el, _ = draw(c, lang, fill_in, color)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>'
            + ''.join(el) + footer(c, lang) + '</svg>')


def tiles(n, overlap=0.06):
    """viewBoxes for an n x n print: each tile is one nth of the chart plus a strip of overlap on every side to
    trim or glue, and the rectangle of the true tile (drawn dashed so the pages line up)."""
    tw, th = W / n, H / n
    ox, oy = tw * overlap, th * overlap
    return [dict(row=r + 1, col=k + 1, box=f'{k * tw - ox:.1f} {r * th - oy:.1f} {tw + 2 * ox:.1f} {th + 2 * oy:.1f}',
                 cut=(round(k * tw, 1), round(r * th, 1), round(tw, 1), round(th, 1))) for r in range(n) for k in range(n)]


if __name__ == '__main__':
    cid = sys.argv[1]
    found = check_charts.load('chart', [cid]) or check_charts.load('poster', [cid])
    print(svg(found[cid], 'es' if 'es' in sys.argv else 'en', 'fill' in sys.argv))
