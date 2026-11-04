// Coordinate Plane generator, grades 5-8. Draws a coordinate plane (first quadrant 0 to 10 at grade 5, all four
// quadrants -10 to 10 from grade 6) with lettered points. Skills: plot and name points (5.G.1, 6.NS.6), distance
// between points on the same horizontal or vertical line (6.NS.8), reflections across an axis (6.NS.6b), vertices of
// rectangles and right triangles with their side lengths, perimeter and area (6.G.3, 7.G.6), and transformations:
// translate, reflect, rotate about the origin and dilate (8.G.1-3). Every answer is a coordinate pair or a number;
// the key draws every plotted answer on the plane in red (class ws-ans, hidden on the student copy).
(() => {
const { part, example, fill, blank, key, esc } = Gen.h;
const { fmt } = Gen.m;

const GRADES = [['5', 'Grade 5'], ['6', 'Grade 6'], ['7', 'Grade 7'], ['8', 'Grade 8']];
const SKILLS = {
  5: [['plot1', 'Plot and name points (first quadrant)']],
  6: [['plot4', 'Plot and name points (four quadrants)'], ['dist', 'Distance between points'], ['reflect', 'Reflect a point across an axis']],
  7: [['shape', 'Shapes on the plane: sides, perimeter and area']],
  8: [['trans', 'Transformations']],
};
const COUNTS = [['s', 'Short (one plane)'], ['m', 'Medium (one plane)'], ['l', 'Long (two pages)']];
// questions per plane, by skill and length
const PLAN = {
  plot1: { s: [6], m: [10], l: [8, 8] }, plot4: { s: [6], m: [10], l: [8, 8] },
  dist: { s: [4], m: [6], l: [5, 5] }, reflect: { s: [5], m: [8], l: [6, 6] },
  shape: { s: [1, 1], m: [1, 1, 1], l: [1, 1, 1, 1] }, trans: { s: [1, 1, 1, 1], m: [1, 1, 1, 1, 1], l: [1, 1, 1, 1, 1, 1] },
};
const pair = (x, y) => `(${fmt(x)}, ${fmt(y)})`;
const P = p => pair(p[0], p[1]);
const PRIME = '′';

/* ---------- drawing ---------- */
const F = 'font-family="Helvetica, Arial, sans-serif"';
const RED = '#b03020';
// marks: [{x, y, l (letter), key}], polys: [{pts: [[x, y]...], key}]; key = true draws it in red, only on the answer key
function plane(lo, hi, S, marks, polys, label) {
  const n = hi - lo, m = 26, W = n * S + 2 * m;
  const X = x => (m + (x - lo) * S).toFixed(1), Y = y => (m + (hi - y) * S).toFixed(1);
  let b = '';
  for (let i = lo; i <= hi; i++) b += `<line x1="${X(i)}" y1="${m}" x2="${X(i)}" y2="${m + n * S}" stroke="#bbb" stroke-width="0.8"/><line x1="${m}" y1="${Y(i)}" x2="${m + n * S}" y2="${Y(i)}" stroke="#bbb" stroke-width="0.8"/>`;
  b += `<line x1="${m}" y1="${Y(0)}" x2="${m + n * S}" y2="${Y(0)}" stroke="#222" stroke-width="2"/><line x1="${X(0)}" y1="${m}" x2="${X(0)}" y2="${m + n * S}" stroke="#222" stroke-width="2"/>`;
  const step = n > 12 ? 2 : 1, fs = n > 12 ? 9.5 : 11;
  for (let i = lo; i <= hi; i += step) {
    if (i === 0) continue;
    b += `<text x="${X(i)}" y="${+Y(0) + 12}" ${F} fill="#222" font-size="${fs}" text-anchor="middle">${fmt(i)}</text>` +
      `<text x="${+X(0) - 4}" y="${+Y(i) + 3.5}" ${F} fill="#222" font-size="${fs}" text-anchor="end">${fmt(i)}</text>`;
  }
  b += `<text x="${+X(0) - 4}" y="${+Y(0) + 12}" ${F} fill="#222" font-size="${fs}" text-anchor="end">0</text>`;
  b += `<text x="${m + n * S + 4}" y="${+Y(0) + 4}" ${F} fill="#222" font-size="13" font-style="italic">x</text><text x="${+X(0) + 5}" y="${m - 7}" ${F} fill="#222" font-size="13" font-style="italic">y</text>`;
  for (const p of polys || []) {
    const c = p.key ? RED : '#222';
    b += `<polygon class="${p.key ? 'ws-ans' : ''}" points="${p.pts.map(q => `${X(q[0])},${Y(q[1])}`).join(' ')}" fill="none" stroke="${c}" stroke-width="2" stroke-linejoin="round"/>`;
  }
  for (const k of marks || []) {
    const c = k.key ? RED : '#222';
    // the letter sits up and to the right, unless that would leave the plane
    const dx = k.x + 1 > hi ? -6 : 6, dy = k.y + 1 > hi ? 13 : -6, anchor = dx < 0 ? 'end' : 'start';
    b += `<g class="${k.key ? 'ws-ans' : ''}"><circle cx="${X(k.x)}" cy="${Y(k.y)}" r="4" fill="${c}"/><text x="${+X(k.x) + dx}" y="${+Y(k.y) + dy}" ${F} fill="${c}" font-size="13" font-weight="700" text-anchor="${anchor}">${esc(k.l)}</text></g>`;
  }
  return `<svg class="gen-svg" viewBox="0 0 ${W} ${W}" role="img" aria-label="${esc(label)}" style="max-width:${(W / 96).toFixed(2)}in">${b}</svg>`;
}

/* ---------- points ---------- */
const far = (a, b) => Math.max(Math.abs(a[0] - b[0]), Math.abs(a[1] - b[1])) >= 2;   // room for both letters
// n points in [lo, hi], at least two squares from each other and from the points in taken
function points(r, lo, hi, n, taken = [], ok = () => true) {
  const all = taken.slice(), out = [];
  for (let t = 0; t < n * 80 && out.length < n; t++) {
    const p = [r.int(lo, hi), r.int(lo, hi)];
    if (all.every(q => far(p, q)) && ok(p)) { all.push(p); out.push(p); }
  }
  return out;
}
const NAMES = 'ABCDEFGH';

/* ---------- transformations (grade 8) ---------- */
const TR = {
  tr: (p, t) => [p[0] + t.dx, p[1] + t.dy], rx: p => [p[0], -p[1]], ry: p => [-p[0], p[1]],
  r90: p => [-p[1], p[0]], r90cw: p => [p[1], -p[0]], r180: p => [-p[0], -p[1]], d2: p => [2 * p[0], 2 * p[1]], dh: p => [p[0] / 2, p[1] / 2],
};
const dirWord = (k, pos, neg) => `${Math.abs(k)} ${Math.abs(k) === 1 ? 'unit' : 'units'} ${k > 0 ? pos : neg}`;
function describe(t) {
  switch (t.kind) {
    case 'tr': return `Translate ${[t.dx ? dirWord(t.dx, 'right', 'left') : '', t.dy ? dirWord(t.dy, 'up', 'down') : ''].filter(Boolean).join(' and ')}`;
    case 'rx': return 'Reflect across the x-axis'; case 'ry': return 'Reflect across the y-axis';
    case 'r90': return 'Rotate 90° counterclockwise about the origin'; case 'r90cw': return 'Rotate 90° clockwise about the origin';
    case 'r180': return 'Rotate 180° about the origin';
    case 'd2': return 'Dilate by a scale factor of 2, centered at the origin'; case 'dh': return 'Dilate by a scale factor of 1/2, centered at the origin';
  }
}

/* ---------- the blocks of each skill: {html, items} ---------- */
function plotBlock(r, g, k, start, bi) {
  const names = bi ? 'FGHJK' : 'ABCDE', plots = bi ? 'UVWZ' : 'PQRST';
  const lo = g === '5' ? 0 : -10, hi = 10, S = g === '5' ? 30 : 17;
  const nName = Math.ceil(k / 2), nPlot = k - nName;
  const pts = points(r, lo, hi, k);
  if (pts.length < k) return null;
  const named = pts.slice(0, nName).map((p, i) => ({ x: p[0], y: p[1], l: names[i] }));
  const plot = pts.slice(nName).map((p, i) => ({ x: p[0], y: p[1], l: plots[i], key: true }));
  const items = [], rows = [];
  // name and plot questions take turns so the sheet reads as one task
  const order = r.shuffle([...named.map(p => ['name', p]), ...plot.map(p => ['plot', p])]);
  for (const [kind, p] of order) {
    const a = pair(p.x, p.y);
    if (kind === 'name') { items.push({ q: `Point ${p.l}`, a, k: 'name', l: p.l, x: p.x, y: p.y }); rows.push(`Point ${p.l} = ${blank(a, 5)}`); }
    else { items.push({ q: `Plot ${p.l} at ${a}`, a, k: 'plot', l: p.l, x: p.x, y: p.y }); rows.push(`Plot point ${p.l} at ${a}. ${key('(drawn on the plane)')}`); }
  }
  const svg = plane(lo, hi, S, named.concat(plot), [], `Coordinate plane from ${lo} to ${hi} with points ${named.map(p => `${p.l} at ${pair(p.x, p.y)}`).join(', ')}`);
  return { html: `<div class="cp-block">${svg}${fill(rows, 1, start)}</div>`, items, pts: named.concat(plot), lo, hi };
}
function distBlock(r, k, start, bi) {
  const letters = bi ? 'NPQRSTUVWZ' : 'ABCDEFGHJKLM', lo = -10, hi = 10, taken = [], pairs = [];
  for (let t = 0; t < k * 60 && pairs.length < k; t++) {
    const a = [r.int(lo, hi), r.int(lo, hi)], horiz = r.chance(.5), d = r.int(2, 12);
    const b = horiz ? [a[0] + (r.chance(.5) ? d : -d), a[1]] : [a[0], a[1] + (r.chance(.5) ? d : -d)];
    if (b[0] < lo || b[0] > hi || b[1] < lo || b[1] > hi) continue;
    if (!taken.every(q => far(a, q) && far(b, q))) continue;
    taken.push(a, b); pairs.push([a, b, d]);
  }
  if (pairs.length < k) return null;
  const marks = [], items = [], rows = [];
  pairs.forEach(([a, b, d], i) => {
    const la = letters[2 * i], lb = letters[2 * i + 1];
    marks.push({ x: a[0], y: a[1], l: la }, { x: b[0], y: b[1], l: lb });
    items.push({ q: `${la}${P(a)} to ${lb}${P(b)}`, a: String(d), k: 'dist', x1: a[0], y1: a[1], x2: b[0], y2: b[1] });
    rows.push(`From ${la} ${P(a)} to ${lb} ${P(b)}: ${blank(d, 3)} units`);
  });
  const svg = plane(lo, hi, 17, marks, [], `Coordinate plane from -10 to 10 with points ${marks.map(p => `${p.l} at ${pair(p.x, p.y)}`).join(', ')}`);
  return { html: `<div class="cp-block">${svg}${fill(rows, 1, start)}</div>`, items };
}
function reflectBlock(r, k, start, bi) {
  const letters = bi ? 'GHJKLMNP' : NAMES, lo = -10, hi = 10, marks = [], items = [], rows = [], taken = [];
  for (let t = 0; t < k * 80 && items.length < k; t++) {
    const p = [r.int(lo, hi), r.int(lo, hi)], axis = r.pick(['x', 'y']);
    const q = axis === 'x' ? [p[0], -p[1]] : [-p[0], p[1]];
    if (!p[0] || !p[1] || !taken.every(z => far(p, z) && far(q, z))) continue;   // off both axes, so the image moves
    taken.push(p, q);
    const l = letters[items.length], a = P(q);
    marks.push({ x: p[0], y: p[1], l }, { x: q[0], y: q[1], l: l + PRIME, key: true });
    items.push({ q: `Reflect ${l}${P(p)} across the ${axis}-axis`, a, k: 'reflect', x: p[0], y: p[1], axis });
    rows.push(`Reflect ${l} ${P(p)} across the <i>${axis}</i>-axis. ${l}${PRIME} = ${blank(a, 5)}`);
  }
  if (items.length < k) return null;
  const svg = plane(lo, hi, 17, marks, [], `Coordinate plane from -10 to 10 with points ${marks.filter(m => !m.key).map(p => `${p.l} at ${pair(p.x, p.y)}`).join(', ')}`);
  return { html: `<div class="cp-block">${svg}${fill(rows, 1, start)}</div>`, items };
}
function shapeCell(r, i) {
  const lo = -10, hi = 10, rect = r.chance(.55);
  const w = r.int(2, 10), h = r.int(2, 10), x = r.int(lo, hi - w), y = r.int(lo, hi - h);
  const items = [], tag = `Shape ${i + 1}`;
  let pts, text, lines;
  if (rect) {
    pts = [[x, y], [x + w, y], [x + w, y + h], [x, y + h]];
    items.push({ q: `${tag} AB ${P(pts[0])} ${P(pts[1])}`, a: String(w), k: 'len', p: pts[0], q2: pts[1] },
      { q: `${tag} BC ${P(pts[1])} ${P(pts[2])}`, a: String(h), k: 'len', p: pts[1], q2: pts[2] },
      { q: `${tag} perimeter ${pts.map(P).join(' ')}`, a: String(2 * (w + h)), k: 'perim', pts },
      { q: `${tag} area ${pts.map(P).join(' ')}`, a: String(w * h), k: 'area', pts });
    text = `Plot A ${P(pts[0])}, B ${P(pts[1])}, C ${P(pts[2])} and D ${P(pts[3])}. Join them in order to make a rectangle.`;
    lines = `<p>AB = ${blank(w, 3)} units &nbsp; BC = ${blank(h, 3)} units</p><p>Perimeter = ${blank(2 * (w + h), 3)} units &nbsp; Area = ${blank(w * h, 3)} square units</p>`;
  } else {
    // a right angle at A; the legs run along grid lines
    const sx = r.pick([1, -1]), sy = r.pick([1, -1]), ax = sx > 0 ? x : x + w, ay = sy > 0 ? y : y + h;
    pts = [[ax, ay], [ax + sx * w, ay], [ax, ay + sy * h]];
    items.push({ q: `${tag} AB ${P(pts[0])} ${P(pts[1])}`, a: String(w), k: 'len', p: pts[0], q2: pts[1] },
      { q: `${tag} AC ${P(pts[0])} ${P(pts[2])}`, a: String(h), k: 'len', p: pts[0], q2: pts[2] },
      { q: `${tag} area ${pts.map(P).join(' ')}`, a: fmt(w * h / 2), k: 'area', pts });
    text = `Plot A ${P(pts[0])}, B ${P(pts[1])} and C ${P(pts[2])}. Join them to make a right triangle.`;
    lines = `<p>AB = ${blank(w, 3)} units &nbsp; AC = ${blank(h, 3)} units</p><p>Area = ${blank(fmt(w * h / 2), 3)} square units</p>`;
  }
  const marks = pts.map((p, j) => ({ x: p[0], y: p[1], l: 'ABCD'[j], key: true }));
  const svg = plane(lo, hi, 13, marks, [{ pts, key: true }], `Empty coordinate plane from -10 to 10 for shape ${i + 1}`);
  return { html: `<div class="cp-cell"><p><span class="ws-num">${i + 1}.</span> ${text}</p>${svg}${lines}</div>`, items };
}
function transCell(r, i) {
  const lo = -10, hi = 10, tri = r.chance(.5);
  const kind = r.pick(['tr', 'rx', 'ry', 'r90', 'r90cw', 'r180', 'd2', 'dh']);
  const t = { kind, dx: 0, dy: 0 };
  if (kind === 'tr') { t.dx = r.int(-6, 6); t.dy = r.int(-6, 6); if (!t.dx && !t.dy) t.dx = r.pick([-3, 3]); }
  // the preimage stays where its image fits on the plane
  const lim = kind === 'd2' ? 5 : kind === 'tr' ? 4 : 9;
  const ok = p => p[0] && p[1] && (kind !== 'dh' || (p[0] % 2 === 0 && p[1] % 2 === 0));
  const n = tri ? 3 : 1;
  let pre = [];
  for (let z = 0; z < 20 && pre.length < n; z++) {
    pre = points(r, -lim, lim, n, [], ok);
    if (tri && pre.length === 3 && (pre[1][0] - pre[0][0]) * (pre[2][1] - pre[0][1]) === (pre[2][0] - pre[0][0]) * (pre[1][1] - pre[0][1])) pre = [];   // not in a line
  }
  if (pre.length < n) return null;
  const img = pre.map(p => TR[kind](p, t));
  if (img.some(p => p[0] < lo || p[0] > hi || p[1] < lo || p[1] > hi)) return null;
  const letters = tri ? ['A', 'B', 'C'] : ['A'];
  const items = pre.map((p, j) => ({ q: `${i + 1}. ${describe(t)}: ${letters[j]}${P(p)}`, a: P(img[j]), k: 'trans', t, p }));
  const marks = pre.map((p, j) => ({ x: p[0], y: p[1], l: letters[j] })).concat(img.map((p, j) => ({ x: p[0], y: p[1], l: letters[j] + PRIME, key: true })));
  const polys = tri ? [{ pts: pre }, { pts: img, key: true }] : [];
  const what = tri ? `triangle ABC with A ${P(pre[0])}, B ${P(pre[1])}, C ${P(pre[2])}` : `point A ${P(pre[0])}`;
  const svg = plane(lo, hi, 12, marks, polys, `Coordinate plane from -10 to 10 showing ${what}`);
  const lines = `<p>${letters.map((l, j) => `${l}${PRIME} = ${blank(P(img[j]), 5)}`).join(' &nbsp; ')}</p>`;
  return { html: `<div class="cp-cell"><p><span class="ws-num">${i + 1}.</span> ${describe(t)}. Draw the image and write its ${tri ? 'vertices' : 'coordinates'}.</p>${svg}${lines}</div>`, items };
}

/* ---------- examples and teacher text ---------- */
const EX = {
  plot1: example('To plot (3, 5): start at 0, go 3 to the right along the x-axis, then 5 up. The x number always comes first.', 'A point at (3, 5) is 3 across and 5 up.'),
  plot4: example('To plot (−3, 5): start at 0, go 3 to the left (x is negative), then 5 up. Negative x goes left; negative y goes down.', 'A point at (−3, 5) is 3 left and 5 up.'),
  dist: example('Points on the same horizontal or vertical line: count the squares between them, or subtract the numbers that differ.', '(−3, 4) to (5, 4): the y values match, so the distance is 5 − (−3) = <b>8</b> units.'),
  reflect: example('Reflecting across the x-axis flips the sign of y. Reflecting across the y-axis flips the sign of x.', '(−3, 4) across the x-axis is (−3, −4). Across the y-axis it is (3, 4).'),
  shape: example('Plot the vertices and join them in order. A side along a grid line is as long as the difference in the coordinates that change.', 'A(1, 2) to B(6, 2): 6 − 1 = 5 units. A rectangle 5 by 3 has perimeter 2 × (5 + 3) = 16 and area 5 × 3 = 15 square units.'),
  trans: example('Translate: add to x and y. Reflect across the x-axis: (x, y) to (x, −y). Across the y-axis: (−x, y). Rotate 90° counterclockwise: (−y, x). 90° clockwise: (y, −x). 180°: (−x, −y). Dilate by k: (kx, ky).', '(2, 5) rotated 90° counterclockwise about the origin is (−5, 2).'),
};
const ICAN = {
  plot1: 'I can plot a point from its coordinates and name a point on the plane.', plot4: 'I can plot and name points in all four quadrants.',
  dist: 'I can find the distance between two points on the same horizontal or vertical line.', reflect: 'I can reflect a point across the x-axis or the y-axis.',
  shape: 'I can draw a shape from its vertices and find its side lengths, perimeter and area.', trans: 'I can translate, reflect, rotate and dilate figures on the coordinate plane.',
};
const DIRS = {
  plot1: 'Use the plane. Write the coordinates of each lettered point as (x, y). Plot the points you are given and label them with their letter.',
  plot4: 'Use the plane. Write the coordinates of each lettered point as (x, y), with a minus sign where it belongs. Plot the points you are given and label them with their letter.',
  dist: 'Use the plane. Each pair of points is on the same horizontal or vertical line. Write how many units apart they are.',
  reflect: 'Use the plane. Reflect each point across the axis named, draw the image, and write its coordinates.',
  shape: 'Plot each set of points, join them in order, and find the lengths asked for. Lengths are in units; area is in square units.',
  trans: 'Plot the image of each figure after the transformation, then write the coordinates of the image. Use a prime mark for the image, like A′.',
};
const MISTAKES = {
  plot1: 'Swapping x and y: going up first, then across. Reading a point from the grid line nearest instead of counting from 0.',
  plot4: 'Dropping the minus sign, and going the wrong way for a negative coordinate (negative x is left, negative y is down).',
  dist: 'Subtracting without the sign: the distance from −3 to 5 is 8, not 2. Counting grid lines instead of the spaces between them.',
  reflect: 'Flipping the wrong coordinate. Across the x-axis the point moves up or down, so only y changes.',
  shape: 'Counting grid lines instead of units for a side length, and mixing up perimeter and area.',
  trans: 'Rotating the wrong way (counterclockwise is the usual positive direction), forgetting that dilation multiplies both coordinates, and reflecting across the wrong axis.',
};

Gen.add('coordinate-plane', {
  title: 'Coordinate Plane', type: 'Practice',
  css: `.cp-block{display:grid;grid-template-columns:auto minmax(0,1fr);gap:4px 18px;align-items:start;margin:6px 0 14px;break-inside:avoid}
.cp-block .gen-svg{margin:0}
.cp-block .ws-fill{margin:4px 0 0}
.cp-block .ws-fill li{margin-bottom:11px;break-inside:avoid;font-size:15px}
.cp-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 18px;margin:6px 0 10px}
.cp-cell{border:1px solid #bbb;border-radius:8px;padding:6px 8px;break-inside:avoid}
.cp-cell p{margin:3px 0;font-size:14px}
.cp-cell .gen-svg{margin:2px auto}
@media print{.cp-block .ws-fill li{margin-bottom:9px}}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '6' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => SKILLS[v.grade], def: 'plot4' },
    { id: 'count', label: 'Length', type: 'select', options: COUNTS, def: 'm' },
  ],
  make(v, r) {
    const g = v.grade, skill = v.skill, plan = PLAN[skill][v.count];
    const label = SKILLS[g].find(s => s[0] === skill)[1], gname = GRADES.find(x => x[0] === g)[1];
    const items = [], blocks = [];
    let start = 1;
    const build = (k, i) => {
      for (let t = 0; t < 30; t++) {
        const b = skill === 'plot1' || skill === 'plot4' ? plotBlock(r, g, k, start, i) : skill === 'dist' ? distBlock(r, k, start, i)
          : skill === 'reflect' ? reflectBlock(r, k, start, i) : skill === 'shape' ? shapeCell(r, i) : transCell(r, i);
        if (b) return b;
      }
      return null;
    };
    plan.forEach((k, i) => { const b = build(k, i); if (b) { blocks.push(b); items.push(...b.items); start += b.items.length; } });
    const cells = skill === 'shape' || skill === 'trans';
    const body = cells ? `<div class="cp-grid">${blocks.map(b => b.html).join('')}</div>` : blocks.map(b => b.html).join('');
    const parts = [part('', EX[skill]), part(cells ? 'Practice' : '', body)];
    const notes = { plot1: 'Named points and points to plot share one plane, so the sheet reads as one task. The key draws each plotted point in red.',
      plot4: 'Named points and points to plot share one plane; the key draws each plotted point in red. Points can sit on an axis, which is worth a word: a point on the x-axis has y = 0.',
      dist: 'Every pair sits on one grid line, so counting squares and subtracting give the same answer. Pairs that cross an axis are the ones to watch: the subtraction needs the sign.',
      reflect: 'Points are kept off both axes so every reflection moves. The key draws each image in red with a prime mark.',
      shape: 'Every side asked for runs along a grid line. Triangle areas can end in .5. The key draws each shape in red.',
      trans: 'Preimages are chosen so every image fits on the plane. Rotations are about the origin and dilations are centered there. The key draws each image in red.' }[skill];
    return {
      title: `${label.replace(/ \(.*\)$/, '')}: ${gname}`, level: `${gname}, ${g === '5' ? 'first quadrant, 0 to 10' : 'four quadrants, −10 to 10'}`,
      ican: ICAN[skill], directions: DIRS[skill],
      minutes: plan.length > 1 && !cells ? 30 : 25, materials: 'pencil, ruler or straightedge',
      parts, items, blocks: blocks.map(b => ({ pts: b.pts, lo: b.lo, hi: b.hi })),
      mistakes: MISTAKES[skill], notes: notes + ' Press New sheet for new points at the same level.',
    };
  },
  verify(s, v) {
    const out = [];
    const num = t => parseFloat(String(t).replace(/−/g, '-').replace(/,/g, ''));
    const parse = t => { const m = String(t).match(/^\(\s*([−-]?[\d.]+)\s*,\s*([−-]?[\d.]+)\s*\)$/); return m ? [num(m[1]), num(m[2])] : null; };
    const lo = v.grade === '5' ? 0 : -10, hi = 10;
    const inRange = p => p[0] >= lo && p[0] <= hi && p[1] >= lo && p[1] <= hi;
    const same = (a, b) => Math.abs(a[0] - b[0]) < 1e-9 && Math.abs(a[1] - b[1]) < 1e-9;
    // every plotted point on a plane matches its letter in the plane's list
    const where = new Map();
    for (const b of s.blocks || []) for (const p of b.pts || []) where.set(p.l, [p.x, p.y]);
    for (const it of s.items) {
      if (it.k === 'name' || it.k === 'plot') {
        const a = parse(it.a), w = where.get(it.l);
        if (!a || !w || !same(a, w)) out.push(`${it.q}: key ${it.a} but the plane has ${it.l} at ${w}`);
        else if (!inRange(a)) out.push(`${it.q}: off the plane`);
      } else if (it.k === 'dist') {
        const d = Math.hypot(it.x2 - it.x1, it.y2 - it.y1);
        if (it.x1 !== it.x2 && it.y1 !== it.y2) out.push(`${it.q}: not on one line`);
        if (num(it.a) !== d) out.push(`${it.q}: key ${it.a}, want ${d}`);
        if (!inRange([it.x1, it.y1]) || !inRange([it.x2, it.y2])) out.push(`${it.q}: off the plane`);
      } else if (it.k === 'reflect') {
        const a = parse(it.a), want = it.axis === 'x' ? [it.x, it.y * -1] : [it.x * -1, it.y];
        if (!a || !same(a, want)) out.push(`${it.q}: key ${it.a}, want ${want}`);
        if (same([it.x, it.y], want)) out.push(`${it.q}: point on the axis`);
      } else if (it.k === 'len') {
        const d = Math.hypot(it.q2[0] - it.p[0], it.q2[1] - it.p[1]);
        if (num(it.a) !== d || !Number.isInteger(d) || d < 1) out.push(`${it.q}: key ${it.a}, want ${d}`);
      } else if (it.k === 'perim' || it.k === 'area') {
        const pts = it.pts, n = pts.length;
        let per = 0, area2 = 0;
        for (let i = 0; i < n; i++) { const p = pts[i], q = pts[(i + 1) % n]; per += Math.hypot(q[0] - p[0], q[1] - p[1]); area2 += p[0] * q[1] - q[0] * p[1]; }
        const want = it.k === 'perim' ? per : Math.abs(area2) / 2;
        if (Math.abs(num(it.a) - want) > 1e-9) out.push(`${it.q}: key ${it.a}, want ${want}`);
        if (pts.some(p => !inRange(p))) out.push(`${it.q}: off the plane`);
      } else if (it.k === 'trans') {
        const t = it.t, p = it.p, a = parse(it.a);
        const ang = { r90: 90, r90cw: -90, r180: 180 }[t.kind];
        let want;
        if (t.kind === 'tr') want = [p[0] + t.dx, p[1] + t.dy];
        else if (ang != null) { const c = Math.round(Math.cos(ang * Math.PI / 180)), sn = Math.round(Math.sin(ang * Math.PI / 180)); want = [c * p[0] - sn * p[1], sn * p[0] + c * p[1]]; }
        else if (t.kind === 'rx') want = [p[0], -p[1]]; else if (t.kind === 'ry') want = [-p[0], p[1]];
        else want = [p[0] * (t.kind === 'd2' ? 2 : .5), p[1] * (t.kind === 'd2' ? 2 : .5)];
        if (!a || !same(a, want)) out.push(`${it.q}: key ${it.a}, want ${want}`);
        else if (!inRange(a)) out.push(`${it.q}: image off the plane`);
        if (same(p, want)) out.push(`${it.q}: the figure does not move`);
      } else out.push(`unknown kind ${it.k}`);
    }
    return out;
  },
});
})();
