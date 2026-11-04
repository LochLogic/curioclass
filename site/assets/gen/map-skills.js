// Map Skills generator, grades 1-6.
// Draws a made-up town on a lettered and numbered grid with a compass rose, a map key of simple symbols and, from
// grade 3, a scale bar. Questions: what is in a square, which square holds a place, directions (cardinal at grades 1-2,
// intermediate from grade 3), distance with the scale (grade 3 up) and a route. Every answer comes from the layout;
// verify re-works each one from the place positions. North is always at the top of the map.
(() => {
const { part, example, fill, blank, lines, keyline, esc } = Gen.h;
const { fmt } = Gen.m;

const GRADES = [['1', 'Grade 1'], ['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'], ['6', 'Grade 6']];
const COLS = 'ABCDEF';
const STROKE = 'stroke="#222" stroke-width="2" fill="none" stroke-linejoin="round" stroke-linecap="round"';
const FILLW = 'stroke="#222" stroke-width="2" fill="#fff" stroke-linejoin="round"';

// map symbols, drawn around (x, y) inside a box about 2s wide
const PLACES = [
  ['Library', (x, y, s) => `<path d="M${x} ${y - s * .55} q${-s * .5} ${-s * .25} ${-s} 0 v${s * 1.1} q${s * .5} ${-s * .25} ${s} 0 q${s * .5} ${-s * .25} ${s} 0 v${-s * 1.1} q${-s * .5} ${-s * .25} ${-s} 0z M${x} ${y - s * .55} v${s * 1.1}" ${FILLW}/>`],
  ['School', (x, y, s) => `<path d="M${x - s * .8} ${y + s * .7} v${-s * .8} l${s * .8} ${-s * .55} l${s * .8} ${s * .55} v${s * .8}z" ${FILLW}/><path d="M${x} ${y - s * .35} v${-s * .55} l${s * .45} ${s * .14} l${-s * .45} ${s * .14}" ${STROKE}/><rect x="${x - s * .18}" y="${y + s * .25}" width="${s * .36}" height="${s * .45}" fill="#222"/>`],
  ['Fire Station', (x, y, s) => `<rect x="${x - s * .85}" y="${y - s * .55}" width="${s * 1.7}" height="${s * 1.25}" ${FILLW}/><path d="M${x - s * .55} ${y + s * .7} v${-s * .65} h${s * 1.1} v${s * .65} M${x - s * .55} ${y + s * .2} h${s * 1.1} M${x - s * .55} ${y + s * .42} h${s * 1.1}" ${STROKE}/><path d="M${x} ${y - s * .95} q${s * .3} ${s * .2} 0 ${s * .4} q${-s * .3} ${-s * .2} 0 ${-s * .4}" fill="#222"/>`],
  ['Hospital', (x, y, s) => `<rect x="${x - s * .75}" y="${y - s * .75}" width="${s * 1.5}" height="${s * 1.5}" rx="${s * .15}" ${FILLW}/><path d="M${x - s * .18} ${y - s * .5} h${s * .36} v${s * .32} h${s * .32} v${s * .36} h${-s * .32} v${s * .32} h${-s * .36} v${-s * .32} h${-s * .32} v${-s * .36} h${s * .32}z" fill="#222"/>`],
  ['Pond', (x, y, s) => `<ellipse cx="${x}" cy="${y}" rx="${s * .9}" ry="${s * .6}" ${FILLW}/><path d="M${x - s * .5} ${y - s * .1} q${s * .125} ${-s * .15} ${s * .25} 0 t${s * .25} 0 t${s * .25} 0 t${s * .25} 0 M${x - s * .4} ${y + s * .22} q${s * .1} ${-s * .15} ${s * .2} 0 t${s * .2} 0 t${s * .2} 0 t${s * .2} 0" ${STROKE} stroke-width="1.5"/>`],
  ['Park', (x, y, s) => `<circle cx="${x}" cy="${y - s * .25}" r="${s * .55}" ${FILLW}/><path d="M${x} ${y + s * .3} v${s * .5} M${x - s * .3} ${y + s * .8} h${s * .6}" ${STROKE}/><circle cx="${x - s * .15}" cy="${y - s * .35}" r="${s * .1}" fill="#222"/><circle cx="${x + s * .2}" cy="${y - s * .15}" r="${s * .1}" fill="#222"/>`],
  ['Post Office', (x, y, s) => `<rect x="${x - s * .85}" y="${y - s * .55}" width="${s * 1.7}" height="${s * 1.1}" ${FILLW}/><path d="M${x - s * .85} ${y - s * .55} l${s * .85} ${s * .6} l${s * .85} ${-s * .6}" ${STROKE}/>`],
  ['Market', (x, y, s) => `<path d="M${x - s * .85} ${y - s * .2} h${s * 1.7} l${-s * .25} ${s * .9} h${-s * 1.2}z" ${FILLW}/><path d="M${x - s * .5} ${y - s * .2} q${s * .5} ${-s * .9} ${s} 0 M${x - s * .3} ${y + s * .05} v${s * .4} M${x} ${y + s * .05} v${s * .4} M${x + s * .3} ${y + s * .05} v${s * .4}" ${STROKE}/>`],
  ['Bus Stop', (x, y, s) => `<path d="M${x} ${y + s * .85} v${-s * 1.2}" ${STROKE}/><rect x="${x - s * .55}" y="${y - s * .9}" width="${s * 1.1}" height="${s * .6}" rx="${s * .1}" ${FILLW}/><circle cx="${x - s * .25}" cy="${y - s * .6}" r="${s * .1}" fill="#222"/><circle cx="${x + s * .25}" cy="${y - s * .6}" r="${s * .1}" fill="#222"/>`],
  ['Museum', (x, y, s) => `<path d="M${x - s * .9} ${y - s * .35} l${s * .9} ${-s * .5} l${s * .9} ${s * .5}z" ${FILLW}/><path d="M${x - s * .55} ${y - s * .25} v${s * .85} M${x} ${y - s * .25} v${s * .85} M${x + s * .55} ${y - s * .25} v${s * .85} M${x - s * .9} ${y + s * .7} h${s * 1.8}" ${STROKE}/>`],
  ['Police Station', (x, y, s) => `<path d="M${x} ${y - s * .85} l${s * .7} ${s * .25} v${s * .45} q0 ${s * .6} ${-s * .7} ${s * .95} q${-s * .7} ${-s * .35} ${-s * .7} ${-s * .95} v${-s * .45}z" ${FILLW}/><circle cx="${x}" cy="${y - s * .05}" r="${s * .28}" fill="#222"/>`],
  ['Playground', (x, y, s) => `<path d="M${x - s * .85} ${y + s * .8} l${s * .3} ${-s * 1.5} h${s * 1.1} l${s * .3} ${s * 1.5} M${x} ${y - s * .7} v${s * .9} M${x - s * .25} ${y + s * .2} h${s * .5}" ${STROKE}/>`],
  ['Garden', (x, y, s) => { let p = ''; for (let i = 0; i < 6; i++) { const a = i * Math.PI / 3; p += `<circle cx="${(x + s * .45 * Math.cos(a)).toFixed(1)}" cy="${(y - s * .15 + s * .45 * Math.sin(a)).toFixed(1)}" r="${s * .28}" ${FILLW}/>`; } return p + `<circle cx="${x}" cy="${y - s * .15}" r="${s * .22}" fill="#222"/><path d="M${x} ${y + s * .55} v${s * .35}" ${STROKE}/>`; }],
  ['Town Hall', (x, y, s) => `<rect x="${x - s * .9}" y="${y - s * .05}" width="${s * 1.8}" height="${s * .8}" ${FILLW}/><rect x="${x - s * .32}" y="${y - s * .9}" width="${s * .64}" height="${s * 1.65}" ${FILLW}/><circle cx="${x}" cy="${y - s * .5}" r="${s * .2}" ${FILLW} stroke-width="1.5"/><path d="M${x} ${y - s * .5} v${-s * .13} M${x} ${y - s * .5} h${s * .1}" ${STROKE} stroke-width="1.2"/><rect x="${x - s * .13}" y="${y + s * .3}" width="${s * .26}" height="${s * .45}" fill="#222"/>`],
];
const DRAW = Object.fromEntries(PLACES);

const DIRS = { '0,-1': 'north', '0,1': 'south', '1,0': 'east', '-1,0': 'west', '1,-1': 'northeast', '-1,-1': 'northwest', '1,1': 'southeast', '-1,1': 'southwest' };
const sq = p => COLS[p.c] + (p.r + 1);
const sgn = x => x > 0 ? 1 : x < 0 ? -1 : 0;
const dirOf = (a, b) => DIRS[`${sgn(a.c - b.c)},${sgn(a.r - b.r)}`];       // direction of a from b
const moveText = (dc, dr) => [dc ? `${Math.abs(dc)} ${Math.abs(dc) === 1 ? 'square' : 'squares'} ${dc > 0 ? 'east' : 'west'}` : '', dr ? `${Math.abs(dr)} ${Math.abs(dr) === 1 ? 'square' : 'squares'} ${dr > 0 ? 'south' : 'north'}` : ''].filter(Boolean);

function layout(r, G) {
  const size = G <= 2 ? 4 : G <= 4 ? 5 : 6, n = G <= 2 ? 7 : G <= 4 ? 9 : 11;
  for (let t = 0; t < 400; t++) {
    const names = r.sample(PLACES.map(p => p[0]), n);
    const cells = r.sample(Array.from({ length: size * size }, (_, i) => i), n);
    const places = names.map((name, i) => ({ name, c: cells[i] % size, r: Math.floor(cells[i] / size) }));
    const pairs = []; places.forEach(a => places.forEach(b => { if (a !== b) pairs.push([a, b]); }));
    const card = pairs.filter(([a, b]) => (a.c === b.c) !== (a.r === b.r));
    const diag = pairs.filter(([a, b]) => a.c !== b.c && Math.abs(a.c - b.c) === Math.abs(a.r - b.r));
    const far = card.filter(([a, b]) => Math.abs(a.c - b.c) + Math.abs(a.r - b.r) >= 2);
    if (card.length < 6 || (G >= 3 && diag.length < 4) || (G >= 3 && far.length < 2)) continue;
    return { size, places, card, diag, far };
  }
  return null;
}

Gen.add('map-skills', {
  title: 'Map Skills', type: 'Map',
  fields: [{ id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '3' }],
  css: `
.mp-q .ws-fill li { margin-bottom: 12px; break-inside: avoid; }
@media print { .mp-q .ws-fill li { margin-bottom: 8px; } }
`,
  make(v, r) {
    const G = +v.grade;
    let L = null; for (let t = 0; t < 5 && !L; t++) L = layout(r, G);
    const { size, places, card, diag, far } = L;
    const at = (c, rr) => places.find(p => p.c === c && p.r === rr);
    // scale: one grid square stands for this distance
    const sc = G === 3 ? { n: 100, u: 'm' } : G === 4 ? r.pick([{ n: 50, u: 'm' }, { n: 200, u: 'm' }]) : G === 5 ? r.pick([{ n: 250, u: 'm' }, { n: 0.5, u: 'km' }]) : r.pick([{ n: 0.25, u: 'km' }, { n: 0.5, u: 'km' }, { n: 150, u: 'm' }]);
    const dist = k => `${fmt(k * sc.n, 2)} ${sc.u}`;

    const items = [], qs = [];
    const add = (q, a, extra, html) => { const it = { q, a: String(a), ...extra }; items.push(it); qs.push(html || `${esc(q)} ${blank(it.a, Math.max(3.5, String(a).length * 0.55 + 1))}`); return it; };
    const pool = r.shuffle(places);
    // example: read one square
    const ex = pool[0];
    // what is in a square
    add(`What is in square ${sq(pool[1])}?`, `the ${pool[1].name}`, { k: 'at', c: pool[1].c, r: pool[1].r });
    if (G >= 2) add(`What is in square ${sq(pool[2])}?`, `the ${pool[2].name}`, { k: 'at', c: pool[2].c, r: pool[2].r });
    // which square
    add(`In which square is the ${pool[3].name}?`, sq(pool[3]), { k: 'where', name: pool[3].name });
    if (G >= 3) add(`In which square is the ${pool[4].name}?`, sq(pool[4]), { k: 'where', name: pool[4].name });
    // directions
    const cpairs = r.sample(card, G <= 2 ? 2 : 1);
    const used = new Set();
    for (const [a, b] of cpairs) {
      const key = a.name + b.name; if (used.has(key)) continue; used.add(key);
      const d = dirOf(a, b);
      if (G <= 2) add(`The ${a.name} is ___ of the ${b.name}.`, d, { k: 'dir', pa: a.name, pb: b.name }, `The ${esc(a.name)} is ${blank(d, 5)} of the ${esc(b.name)}.`);
      else add(`Which direction is the ${a.name} from the ${b.name}?`, d, { k: 'dir', pa: a.name, pb: b.name });
    }
    if (G <= 2) {   // a place right next to another one
      const adj = r.shuffle(places).map(p => { const nb = r.shuffle([[0, -1], [0, 1], [1, 0], [-1, 0]]).map(([dc, dr]) => [at(p.c + dc, p.r + dr), dc, dr]).find(x => x[0]); return nb ? [p, ...nb] : null; }).find(Boolean);
      if (adj) { const [p, q2, dc, dr] = adj; const d = DIRS[`${dc},${dr}`];
        add(`Which place is in the square just ${d} of the ${p.name}?`, `the ${q2.name}`, { k: 'adj', name: p.name, d }); }
    }
    if (G >= 3) for (const [a, b] of r.sample(diag, G >= 5 ? 2 : 1)) add(`Which direction is the ${a.name} from the ${b.name}?`, dirOf(a, b), { k: 'dir', pa: a.name, pb: b.name });
    // distance with the scale
    if (G >= 3) {
      const [a, b] = r.pick(far), k = Math.abs(a.c - b.c) + Math.abs(a.r - b.r);
      add(`Use the scale. How far is it from the ${a.name} to the ${b.name}, center to center?`, dist(k), { k: 'dist', pa: a.name, pb: b.name, n: sc.n, u: sc.u });
    }
    // route: follow moves to a place
    const rp = r.distinct(1, () => { const [a, b] = r.sample(places, 2); const dc = b.c - a.c, dr = b.r - a.r; if (!dc && !dr) return null; if (G === 1 && dc && dr) return null; return [a, b, dc, dr]; })[0];
    if (rp) { const [a, b, dc, dr] = rp; add(`Start at the ${a.name}. Go ${moveText(dc, dr).join(', then ')}. Where are you?`, `the ${b.name}`, { k: 'route', pa: a.name, dc, dr }); }
    // grades 5-6: walking distance along the grid, and writing a route
    if (G >= 5) {
      const w = r.distinct(1, () => { const [a, b] = r.sample(places, 2); return a.c !== b.c && a.r !== b.r ? [a, b] : null; })[0];
      if (w) { const [a, b] = w, k = Math.abs(a.c - b.c) + Math.abs(a.r - b.r);
        add(`Walk from the ${a.name} to the ${b.name} along the squares, going only north, south, east or west. Use the scale: how far is the shortest walk?`, dist(k), { k: 'walk', pa: a.name, pb: b.name, n: sc.n, u: sc.u });
        const z = r.distinct(1, () => { const [c, d] = r.sample(places, 2); return c.c !== d.c && c.r !== d.r && !(c === a && d === b) ? [c, d] : null; })[0];
        if (z) { const [c, d] = z, wq = `Write directions from the ${c.name} to the ${d.name}. Use squares and north, south, east or west.`, wa = `Go ${moveText(d.c - c.c, d.r - c.r).join(', then ')} (either order).`;
          add(wq, wa, { k: 'write', a1: c.name, b1: d.name }, `${esc(wq)}<br>${blank(wa, 15)}`); }
      }
    }
    // grades 1-3: draw a star in an empty square
    let star = null;
    if (G <= 3) {
      const empty = []; for (let c = 0; c < size; c++) for (let rr = 0; rr < size; rr++) if (!at(c, rr)) empty.push({ c, r: rr });
      star = r.pick(empty);
      add(`Draw a star in square ${sq(star)}.`, `star in ${sq(star)}`, { k: 'draw', c: star.c, r: star.r }, `Draw a star in square ${sq(star)}. ${Gen.h.key('(see the map)')}`);
    }

    /* ---------- the map ---------- */
    const S = G <= 2 ? 76 : G <= 4 ? 64 : 54, ox = 34, oy = 30, gw = size * S, kx = ox + gw + 26;
    const keyRows = places.slice().sort((a, b) => a.name < b.name ? -1 : 1);
    const rowH = places.length > 9 ? 26 : 30, compH = 100, keyTop = oy + compH + 12;
    const scaleH = G >= 3 ? 56 : 0;
    const kc = keyRows.length > 9 ? 2 : 1, kw = kc === 2 ? 300 : 190, kn = Math.ceil(keyRows.length / kc);
    const H = Math.max(oy + gw + scaleH + 10, keyTop + 26 + kn * rowH + 8), W = kx + kw + 20;
    const F = 'font-family="Helvetica, Arial, sans-serif" fill="#222"';
    let b = '';
    // grid and labels
    b += `<rect x="${ox}" y="${oy}" width="${gw}" height="${gw}" fill="#fff" stroke="#222" stroke-width="2.5"/>`;
    for (let i = 1; i < size; i++) b += `<line x1="${ox + i * S}" y1="${oy}" x2="${ox + i * S}" y2="${oy + gw}" stroke="#888" stroke-width="1"/><line x1="${ox}" y1="${oy + i * S}" x2="${ox + gw}" y2="${oy + i * S}" stroke="#888" stroke-width="1"/>`;
    for (let i = 0; i < size; i++) b += `<text x="${ox + i * S + S / 2}" y="${oy - 9}" ${F} font-size="17" font-weight="700" text-anchor="middle">${COLS[i]}</text><text x="${ox - 12}" y="${oy + i * S + S / 2 + 6}" ${F} font-size="17" font-weight="700" text-anchor="middle">${i + 1}</text>`;
    for (const p of places) b += DRAW[p.name](ox + p.c * S + S / 2, oy + p.r * S + S / 2, S * 0.3);
    if (star) { const x = ox + star.c * S + S / 2, y = oy + star.r * S + S / 2; let d = ''; for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? S * .12 : S * .3; d += `${i ? 'L' : 'M'}${(x + rr * Math.cos(a)).toFixed(1)} ${(y + rr * Math.sin(a)).toFixed(1)} `; }
      b += `<g class="ws-keyonly"><path d="${d}z" fill="none" stroke="#b03020" stroke-width="2.5"/></g>`; }
    // compass rose
    const cx = kx + kw / 2, cy = oy + compH / 2 + 2, R = 32;
    b += `<path d="M${cx} ${cy - R} L${cx + 8} ${cy} L${cx} ${cy + R} L${cx - 8} ${cy}z M${cx - R} ${cy} L${cx} ${cy - 8} L${cx + R} ${cy} L${cx} ${cy + 8}z" fill="#fff" stroke="#222" stroke-width="1.5"/>` +
      `<path d="M${cx} ${cy - R} L${cx + 8} ${cy} L${cx - 8} ${cy}z" fill="#222"/>` +
      `<text x="${cx}" y="${cy - R - 6}" ${F} font-size="16" font-weight="700" text-anchor="middle">N</text><text x="${cx}" y="${cy + R + 17}" ${F} font-size="16" font-weight="700" text-anchor="middle">S</text>` +
      `<text x="${cx + R + 7}" y="${cy + 6}" ${F} font-size="16" font-weight="700">E</text><text x="${cx - R - 7}" y="${cy + 6}" ${F} font-size="16" font-weight="700" text-anchor="end">W</text>`;
    if (G >= 3) { const q = R * 0.62; b += [['NE', 1, -1], ['SE', 1, 1], ['SW', -1, 1], ['NW', -1, -1]].map(([t, dx, dy]) => `<line x1="${cx + dx * 9}" y1="${cy + dy * 9}" x2="${cx + dx * q}" y2="${cy + dy * q}" stroke="#222" stroke-width="1.2"/><text x="${cx + dx * (q + 9)}" y="${cy + dy * (q + 9) + 4}" ${F} font-size="11" text-anchor="middle">${t}</text>`).join(''); }
    // map key
    b += `<rect x="${kx}" y="${keyTop}" width="${kw}" height="${26 + kn * rowH}" fill="#fff" stroke="#222" stroke-width="1.5" rx="4"/><text x="${kx + 10}" y="${keyTop + 19}" ${F} font-size="15" font-weight="700">Map key</text>`;
    keyRows.forEach((p, i) => { const y = keyTop + 26 + (i % kn) * rowH + rowH / 2, x0 = kx + Math.floor(i / kn) * 145; b += DRAW[p.name](x0 + 22, y, 11) + `<text x="${x0 + 42}" y="${y + 5}" ${F} font-size="14">${esc(p.name)}</text>`; });
    // scale bar: two squares long
    if (G >= 3) {
      const sy = oy + gw + 26;
      b += `<rect x="${ox}" y="${sy}" width="${S}" height="9" fill="#222" stroke="#222" stroke-width="1.5"/><rect x="${ox + S}" y="${sy}" width="${S}" height="9" fill="#fff" stroke="#222" stroke-width="1.5"/>` +
        [0, 1, 2].map(i => `<text x="${ox + i * S}" y="${sy + 26}" ${F} font-size="13" text-anchor="middle">${i ? fmt(i * sc.n, 2) + ' ' + sc.u : '0'}</text>`).join('') +
        `<text x="${ox + 2 * S + 40}" y="${sy + 10}" ${F} font-size="13">Scale: 1 square = ${fmt(sc.n, 2)} ${sc.u}</text>`;
    }
    const label = `Map of a town on a grid, columns ${COLS[0]} to ${COLS[size - 1]} and rows 1 to ${size}, north at the top. ` + keyRows.map(p => `${p.name} in ${sq(p)}`).join(', ') + '.' + (G >= 3 ? ` Scale: 1 square = ${fmt(sc.n, 2)} ${sc.u}.` : '');
    const map = Gen.h.svg(W, H, b, label);

    const parts = [part('', example(`<b>What is in square ${sq(ex)}?</b>`, `Go to column ${COLS[ex.c]} along the top and row ${ex.r + 1} down the side. The map key shows that symbol is the ${esc(ex.name)}.`)),
      part('', map), part('Questions', `<div class="mp-q">${fill(qs, G <= 2 ? 1 : 2)}</div>`)];
    const gl = GRADES.find(x => x[0] === v.grade)[1];
    return {
      title: 'Map Skills: Around Town', level: `${gl}, ${size} × ${size} grid${G >= 3 ? ', scale 1 square = ' + fmt(sc.n, 2) + ' ' + sc.u : ''}`,
      ican: G <= 2 ? 'I can use a map key, grid squares and north, south, east and west.' : G <= 4 ? 'I can use a map grid, a compass rose with in-between directions, and a scale.' : 'I can use a map grid, directions and a scale to describe and measure routes.',
      directions: G <= 2 ? 'Use the map, the map key and the compass rose. Write each answer on the line.' : 'Use the map, the map key, the compass rose and the scale. Write each answer on the line. A square is named letter first, then number, like B3.',
      minutes: G <= 2 ? 20 : 25, materials: 'pencil',
      parts, items, layout: { size, places, sc },
      mistakes: 'Writing the number before the letter (3B instead of B3), mixing up east and west, and ' + (G >= 3 ? 'naming only one part of an in-between direction (north instead of northeast), or counting squares from the edge of a symbol instead of center to center for distance.' : 'reading the direction backward: "the Pond is north of the School" means you start at the School and go north.'),
      notes: `North is at the top of every map. Directions are only asked between places that are in the same row or column${G >= 3 ? ', or exactly on a diagonal (the same number of squares across and up or down), so every answer is one clear direction' : ''}. ${G >= 3 ? 'Distances count grid squares center to center and multiply by the scale. ' : ''}${G >= 5 ? 'For the written route, any order of the two moves is correct. ' : ''}Accept a place name with or without "the". Press New sheet for a new town.`,
    };
  },
  verify(s) {
    const out = [], L = s.layout, P = new Map(L.places.map(p => [p.name, p]));
    const cells = new Set(L.places.map(p => p.c + ',' + p.r));
    if (cells.size !== L.places.length) out.push('two places share a square');
    if (L.places.some(p => p.c < 0 || p.r < 0 || p.c >= L.size || p.r >= L.size)) out.push('a place is off the grid');
    const name = (c, r) => (L.places.find(p => p.c === c && p.r === r) || {}).name;
    const sqn = p => 'ABCDEF'[p.c] + (p.r + 1);
    // direction worked out by angle, not by the make table
    const compass = (a, b) => { const dx = a.c - b.c, dy = b.r - a.r; if (!dx && !dy) return null;
      if (dx && dy && Math.abs(dx) !== Math.abs(dy)) return 'not one direction';
      const ang = (Math.atan2(dy, dx) * 180 / Math.PI + 360) % 360; return ['east', 'northeast', 'north', 'northwest', 'west', 'southwest', 'south', 'southeast'][Math.round(ang / 45) % 8]; };
    const scaleTxt = (k, n, u) => `${Math.round(k * n * 100) / 100} ${u}`;
    for (const it of s.items) {
      if (it.k === 'at') { if (it.a !== `the ${name(it.c, it.r)}`) out.push(`${it.q}: key ${it.a}`); }
      else if (it.k === 'where') { if (it.a !== sqn(P.get(it.name))) out.push(`${it.q}: key ${it.a}`); }
      else if (it.k === 'dir') { const d = compass(P.get(it.pa), P.get(it.pb)); if (it.a !== d) out.push(`${it.q}: key ${it.a}, map says ${d}`); }
      else if (it.k === 'adj') { const p = P.get(it.name), m = { north: [0, -1], south: [0, 1], east: [1, 0], west: [-1, 0] }[it.d]; if (it.a !== `the ${name(p.c + m[0], p.r + m[1])}`) out.push(`${it.q}: key ${it.a}`); }
      else if (it.k === 'dist' || it.k === 'walk') { const a = P.get(it.pa), b = P.get(it.pb);
        if (it.k === 'dist' && a.c !== b.c && a.r !== b.r) out.push(`${it.q}: not in a straight line`);
        const k = Math.abs(a.c - b.c) + Math.abs(a.r - b.r); if (it.a.replace(/,/g, '') !== scaleTxt(k, it.n, it.u)) out.push(`${it.q}: key ${it.a}, should be ${scaleTxt(k, it.n, it.u)}`); }
      else if (it.k === 'route') { const a = P.get(it.pa); const nm = name(a.c + it.dc, a.r + it.dr);
        if (it.a !== `the ${nm}`) out.push(`${it.q}: key ${it.a}, map says ${nm}`);
        const mv = [...it.q.matchAll(/(\d+) squares? (east|west|north|south)/g)].reduce((acc, m) => { const k = +m[1]; acc[0] += m[2] === 'east' ? k : m[2] === 'west' ? -k : 0; acc[1] += m[2] === 'south' ? k : m[2] === 'north' ? -k : 0; return acc; }, [0, 0]);
        if (mv[0] !== it.dc || mv[1] !== it.dr) out.push(`${it.q}: the moves in the question do not match`); }
      else if (it.k === 'write') { const a = P.get(it.a1), b = P.get(it.b1);
        const mv = [...it.a.matchAll(/(\d+) squares? (east|west|north|south)/g)].reduce((acc, m) => { const k = +m[1]; acc[0] += m[2] === 'east' ? k : m[2] === 'west' ? -k : 0; acc[1] += m[2] === 'south' ? k : m[2] === 'north' ? -k : 0; return acc; }, [0, 0]);
        if (a.c + mv[0] !== b.c || a.r + mv[1] !== b.r) out.push(`${it.q}: written route does not arrive`); }
      else if (it.k === 'draw') { if (name(it.c, it.r)) out.push(`${it.q}: square is not empty`); }
      else out.push(`unknown kind ${it.k}`);
    }
    return out;
  },
});
})();
