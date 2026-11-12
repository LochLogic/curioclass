"""The Map (docs/SUPPLY-CLOSET-PLAN.md, Phase F): the teaching order from data/sequence.csv, drawn as inline SVG.

Regions are subject and grade pairs from data/modules.csv; stops are their modules in the order data/sequence.csv
gives. Everything else (ready or planned, pins) is derived at build time, so the only upkeep is one sequence.csv row
per new module. A module with no row is still drawn, at the end of its region, and the build prints a warning.
"""
import csv
from html import escape
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / 'data'
BASIS = {  # basis column -> what it means, shown on the region page
    'im-order': 'Unit order of Illustrative Mathematics K-12, first edition (CC BY 4.0)',
    'progressions': 'The Progressions for the Common Core math standards (CC BY 4.0)',
    'ngss-k': 'Grade placement in NGSS Appendix K, Conceptual Progressions model',
    'chronology': 'Chronological order',
    'horizons': 'Expanding horizons: self, family, school, community, state',
    'pair': 'Paired with the reading module just before it',
    'framework': 'The framework\'s own order',
    'judgment': 'Our judgment: what each topic needs first',
}
PIN = {'tool': 'T', 'words': 'W', 'chart': 'C', 'game': 'G', 'sub': 'S'}
TEAL = '#1d5c63'


def load(modules, grades):
    """(regions, warnings). regions: {(subject, grade): [dict(module, n, builds_on, basis)]} in teaching order."""
    rows, warn = {}, []
    with open(DATA / 'sequence.csv', newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if r['module_id'] not in modules:
                warn.append(f"sequence.csv names an unknown module {r['module_id']}")
                continue
            rows[r['module_id']] = r
    missing = [mid for mid in modules if mid not in rows]
    if missing:
        warn.append(f'{len(missing)} topics have no row in data/sequence.csv (like {missing[0]}); '
                    'they go at the end of their region until they get one')
    regions = {}
    for i, (mid, m) in enumerate(modules.items()):
        r = rows.get(mid, {})
        links = [b for b in r.get('builds_on', '').split(';') if b]
        bad = [b for b in links if b not in modules]
        if bad:
            warn.append(f'sequence.csv: {mid} builds on unknown {bad[0]}')
        regions.setdefault((m['subject'], m['grade']), []).append(dict(
            m=m, key=(int(r['order']) if r.get('order', '').isdigit() else 10_000 + i),
            builds_on=[modules[b] for b in links if b in modules], basis=r.get('basis') or 'unplaced'))
    out = {}
    for k in sorted(regions, key=lambda k: (k[0], grades.index(k[1].split('-')[0]), k[1])):
        stops = sorted(regions[k], key=lambda s: s['key'])
        for n, s in enumerate(stops, 1):
            s['n'] = n
        out[k] = stops
    return out, warn


def _wrap(text, width, lines=2):
    words, out, cur = text.split(), [], ''
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= width:
            cur = f'{cur} {w}' if cur else w
        else:
            out.append(cur)
            cur = w
    out.append(cur)
    if len(out) > lines:
        out = out[:lines]
        out[-1] = out[-1][:width - 3].rstrip(' ,') + '...'
    return out


def _stop(s, x, y, color, tx, ty, anchor, width):
    """One stop: a filled circle when a tool is ready, a dashed outline when only planned; pins; the title."""
    ready = s['ready']
    tip = f"{s['n']}. {s['m']['title']}" + ('' if ready else ' (planned)')
    if s['builds_on']:
        tip += '. Builds on ' + ', '.join(b['title'] for b in s['builds_on'])
    g = [f'<a href="{s["m"]["url"]}" class="stop"><title>{escape(tip)}</title>']
    if s['builds_on']:
        g.append(f'<circle cx="{x}" cy="{y}" r="27" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="1 4" stroke-linecap="round"/>')
    if ready:
        g.append(f'<circle cx="{x}" cy="{y}" r="20" fill="{color}" stroke="#fff" stroke-width="3"/>')
    else:
        g.append(f'<circle cx="{x}" cy="{y}" r="19" fill="#fff" stroke="{color}" stroke-width="2.5" stroke-dasharray="5 4"/>')
    g.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" class="num" fill="{"#fff" if ready else color}">{s["n"]}</text>')
    for i, line in enumerate(_wrap(s['m']['title'], width)):
        g.append(f'<text x="{tx}" y="{ty + i * 16}" text-anchor="{anchor}" class="lbl">{escape(line)}</text>')
    pins = s['pins']
    px = tx - (len(pins) - 1) * 9 if anchor == 'middle' else tx + 8
    py = ty + 30 if anchor == 'middle' else ty + 34
    for i, p in enumerate(pins):
        fill = color if p == 'tool' else TEAL
        g.append(f'<circle cx="{px + i * 18}" cy="{py}" r="8" fill="{fill}"/><text x="{px + i * 18}" y="{py + 3.5}" '
                 f'text-anchor="middle" class="pin">{PIN[p]}</text>')
    g.append('</a>')
    return ''.join(g)


def trail(stops, color, label, phone=False):
    """The region map. Desktop: a winding trail, five stops a row. Phone: a straight trail down the page."""
    if phone:
        w, x, top, step = 360, 34, 40, 84
        pts = [(x, top + i * step) for i in range(len(stops))]
        h = top + (len(stops) - 1) * step + 50
        path = f'M{x},{top - 26} V{pts[-1][1] + 26}'
        body = [_stop(s, px, py, color, px + 36, py - 4, 'start', 32) for s, (px, py) in zip(stops, pts)]
    else:
        cols, w, mx, top, rowh = 5, 1000, 112, 64, 156
        cw = (w - 2 * mx) / (cols - 1)
        pts = []
        for i in range(len(stops)):
            r, c = divmod(i, cols)
            pts.append((round(mx + (c if r % 2 == 0 else cols - 1 - c) * cw), top + r * rowh))
        h = top + (len(pts) - 1) // cols * rowh + 110
        d = [f'M{pts[0][0] - 50},{pts[0][1]} L{pts[0][0]},{pts[0][1]}']
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            if ay == by:
                d.append(f'L{bx},{by}')
            else:
                side = 1 if ax > w / 2 else -1
                d.append(f'C{ax + side * 130},{ay} {bx + side * 130},{by} {bx},{by}')
        path = ' '.join(d)
        body = [_stop(s, px, py, color, px, py + 42, 'middle', 26) for s, (px, py) in zip(stops, pts)]
    return (f'<svg class="trail-map{" phone" if phone else " wide"}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="group" aria-label="{escape(label)}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{path}" fill="none" stroke="{color}" stroke-opacity=".28" stroke-width="10" stroke-linecap="round"/>'
            f'<path d="{path}" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="2 9" stroke-linecap="round"/>'
            + ''.join(body) + '</svg>')


def overview(rows, cols, color_of, label_of):
    """/map/: subjects down the side, grades across the top, a box per region shaded by how much is ready.
    rows: [(subject_id, label, [region dicts with x0, x1, lane, url, ready, total, title])]"""
    lw, cw, lh, gap, top = 178, 62, 34, 10, 34
    y, body = top, []
    for i, c in enumerate(cols):
        body.append(f'<text x="{lw + i * cw + cw / 2}" y="22" text-anchor="middle" class="col">{c}</text>')
    for sid, label, regs in rows:
        lanes = max(r['lane'] for r in regs) + 1
        hh = lanes * lh
        col = color_of(sid)
        body.append(f'<rect x="0" y="{y - 3}" width="{lw + len(cols) * cw}" height="{hh + 6}" rx="8" class="band"/>')
        body.append(f'<text x="10" y="{y + hh / 2 + 5}" class="subj" fill="{col}">{escape(label)}</text>')
        for r in regs:
            x, rw, ry = lw + r['x0'] * cw + 3, (r['x1'] - r['x0'] + 1) * cw - 6, y + r['lane'] * lh + 2
            frac = r['ready'] / r['total']
            dark = frac >= .45
            if r['ready']:
                box = f'<rect x="{x}" y="{ry}" width="{rw}" height="{lh - 4}" rx="7" fill="{col}" fill-opacity="{.12 + .88 * frac:.2f}" stroke="{col}"/>'
            else:
                box = f'<rect x="{x}" y="{ry}" width="{rw}" height="{lh - 4}" rx="7" fill="#fff" stroke="{col}" stroke-dasharray="4 3"/>'
            txt = f"{r['ready']}/{r['total']}" if rw < 100 else f"{r['short']} · {r['ready']}/{r['total']} ready"
            body.append(f'<a href="{r["url"]}"><title>{escape(r["title"])}: {r["ready"]} of {r["total"]} stops have a tool ready</title>{box}'
                        f'<text x="{x + rw / 2}" y="{ry + lh / 2 + 2}" text-anchor="middle" class="cell" fill="{"#fff" if dark else "#1f2430"}">{escape(txt)}</text></a>')
        y += hh + gap
    w = lw + len(cols) * cw
    return (f'<svg class="map-grid" viewBox="0 0 {w} {y}" width="{w}" height="{y}" role="group" aria-label="{escape(label_of)}" '
            f'xmlns="http://www.w3.org/2000/svg">' + ''.join(body) + '</svg>')


def strip(stops, hits, color, label):
    """A small row of a region's stops for a standard's page; the stops that teach the code are filled."""
    gap, w = 16, max(len(stops) * 16 + 8, 40)
    dots = []
    for i, s in enumerate(stops):
        on = s['m']['module_id'] in hits
        dots.append(f'<circle cx="{12 + i * gap}" cy="12" r="{6 if on else 4}" fill="{color if on else "#fff"}" stroke="{color}" stroke-width="1.5"/>')
    return (f'<svg viewBox="0 0 {w} 24" width="{w}" height="24" role="img" aria-label="{escape(label)}" xmlns="http://www.w3.org/2000/svg">'
            f'<line x1="12" y1="12" x2="{12 + (len(stops) - 1) * gap}" y2="12" stroke="{color}" stroke-opacity=".35" stroke-width="3"/>'
            + ''.join(dots) + '</svg>')
