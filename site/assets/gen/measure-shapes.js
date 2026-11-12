// Area, Perimeter and Volume generator, grades 2-8. Drawn shapes with labeled measurements, roughly to scale:
// perimeter, perimeter with a missing side and area by counting grid squares (2-3, 3.MD.6-8), rectangle and composite
// rectilinear area (3.MD.7, 4.MD.3), volume of rectangular prisms (5.MD.5), area of triangles, parallelograms and
// trapezoids and surface area of rectangular prisms (6.G.1, 6.G.4), circles and surface area of triangular prisms
// (7.G.4, 7.G.6), cylinders, and cylinders, cones and spheres rounded to the nearest tenth (8.G.9).
// Every answer carries its unit: units, square units or cubic units.
(() => {
const H = Gen.h, { part, example, svg, esc } = H;
const { fmt } = Gen.m;

const GRADES = [['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'], ['6', 'Grade 6'], ['7', 'Grade 7'], ['8', 'Grade 8']];
const SKILLS = {
  2: [['perim', 'Perimeter of shapes']],
  3: [['perim', 'Perimeter of polygons'], ['area', 'Area of rectangles'], ['compo', 'Area of L-shapes'], ['mix3', 'Area and perimeter'], ['unknown', 'Perimeter with a missing side'], ['grid', 'Area by counting squares']],
  4: [['ap', 'Area and perimeter of rectangles'], ['compo', 'Composite shapes'], ['missing', 'Find the missing side'], ['mix4', 'Mixed review'], ['formulas', 'Both formulas, no pictures (12 and 5 to fix)']],
  5: [['vol', 'Volume of rectangular prisms'], ['volc', 'Volume of two joined boxes']],
  6: [['tri', 'Area of triangles'], ['para', 'Area of parallelograms'], ['trap', 'Area of trapezoids'], ['poly', 'Triangles, parallelograms and trapezoids'], ['sa', 'Surface area of rectangular prisms']],
  7: [['circ', 'Circumference of circles'], ['carea', 'Area of circles'], ['circles', 'Circumference and area'], ['prismsa', 'Surface area of triangular prisms']],
  8: [['cyl', 'Volume of cylinders'], ['vol8', 'Prisms and cylinders'], ['round', 'Volume of cylinders, cones and spheres']],
};
const UNITS = [['metric', 'Metric (cm, m)'], ['customary', 'Customary (in, ft)'], ['both', 'Some of each']];
const usesPi = v => (v.grade === '7' || v.grade === '8') && v.skill !== 'prismsa';
const piChoice = v => usesPi(v) && v.skill !== 'round';   // the round mode always uses 3.14
const COUNTS = [6, 9, 12];

/* ---------- units and answer text ---------- */
const UNAME = { cm: 'cm', m: 'm', in: 'in', ft: 'ft' };
const pickUnit = (r, mode, big) => { const pool = mode === 'metric' ? ['cm', 'm'] : mode === 'customary' ? ['in', 'ft'] : ['cm', 'm', 'in', 'ft'];
  return big ? r.pick(pool) : r.pick(pool.filter(u => u === 'cm' || u === 'in')); };
// words for grades 2-5, exponents from grade 6
// (spelled out below grade 6: "square in" reads oddly, "square inches" does not)
const ULONG = { cm: 'centimeters', m: 'meters', in: 'inches', ft: 'feet' };
const sq = (u, g) => +g >= 6 ? `${u}²` : `square ${ULONG[u] || u}`;
const cu = (u, g) => +g >= 6 ? `${u}³` : `cubic ${ULONG[u] || u}`;
const piText = (k, mode, u, power) => mode === 'pi' ? `${k === 1 ? '' : fmt(k, 0)}π ${u}${power}` : `${fmtc(k * 314)} ${u}${power}`;
const fmtc = hundredths => { const s = fmt(hundredths / 100, 2); return s; };   // 3.14 × k, written from whole hundredths

/* ---------- drawing ---------- */
const ST = 'stroke="#222" stroke-width="2" fill="#fff"', THIN = 'stroke="#222" stroke-width="1.2"', DASH = 'stroke="#222" stroke-width="1.3" stroke-dasharray="5 4"';
const lab = (x, y, t, anchor = 'middle', size = 18) => `<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" text-anchor="${anchor}" font-size="${size}" font-weight="600">${esc(t)}</text>`;
const rightMark = (x, y, dx, dy) => `<path d="M${x + dx} ${y} v${dy} h${-dx}" fill="none" ${THIN}/>`;
const W = 230, HH = 160;   // drawing box
// like Gen.h.svg with room at the sides, so labels never get clipped
const pic = (w, h, body, label) => `<svg class="gen-svg" viewBox="-34 0 ${w + 68} ${h}" role="img" aria-label="${esc(label)}" style="max-width:${((w + 68) / 96).toFixed(2)}in">${body}</svg>`;
function fit(w, h, maxW = 160, maxH = 105) { return Math.min(maxW / w, maxH / h, 26); }

function drawRect(w, h, u) {
  const s = fit(w, h), pw = w * s, ph = h * s, x = (W - pw) / 2, y = 22;
  return pic(W, ph + 52, `<rect x="${x}" y="${y}" width="${pw}" height="${ph}" ${ST}/>` + lab(W / 2, y - 7, `${w} ${u}`) + lab(x + pw + 6, y + ph / 2 + 5, `${h} ${u}`, 'start'),
    `Rectangle, ${w} ${u} long and ${h} ${u} wide`);
}
// polygon with every side labeled; pts in units, labels in order
function drawPoly(pts, labels, u, desc, inner) {
  const xs = pts.map(p => p[0]), ys = pts.map(p => p[1]), minx = Math.min(...xs), miny = Math.min(...ys);
  const w = Math.max(...xs) - minx, h = Math.max(...ys) - miny, s = fit(w, h, 185, 115), ox = (W - w * s) / 2, oy = 24;
  const P = pts.map(([a, b]) => [ox + (a - minx) * s, oy + (b - miny) * s]);
  let out = `<polygon points="${P.map(p => p.map(c => c.toFixed(1)).join(',')).join(' ')}" ${ST}/>`;
  // outward normal of each edge from the winding direction (works for the notch of an L-shape too)
  let area2 = 0; P.forEach((p, i) => { const q = P[(i + 1) % P.length]; area2 += p[0] * q[1] - q[0] * p[1]; });
  const sgn = area2 > 0 ? 1 : -1;
  P.forEach((p, i) => { const q = P[(i + 1) % P.length], mx = (p[0] + q[0]) / 2, my = (p[1] + q[1]) / 2;
    let nx = sgn * (q[1] - p[1]), ny = -sgn * (q[0] - p[0]); const L = Math.hypot(nx, ny) || 1; nx /= L; ny /= L;
    // an edge inside the bounding box (the notch of an L) gets its label on the inner side, away from the other notch label
    const bx = [Math.min(...P.map(t => t[0])), Math.max(...P.map(t => t[0]))], by = [Math.min(...P.map(t => t[1])), Math.max(...P.map(t => t[1]))];
    const onBox = (Math.abs(p[0] - q[0]) < .5 && (Math.abs(p[0] - bx[0]) < .5 || Math.abs(p[0] - bx[1]) < .5)) || (Math.abs(p[1] - q[1]) < .5 && (Math.abs(p[1] - by[0]) < .5 || Math.abs(p[1] - by[1]) < .5));
    if (inner && !onBox) { nx = -nx; ny = -ny; }
    const side = Math.abs(nx) > .6;
    out += lab(mx + nx * (side ? 6 : 12), my + ny * (side ? 6 : 12) + (side ? 5 : ny > 0 ? 9 : 1), labels[i] === '?' ? '?' : `${labels[i]} ${u}`, side ? (nx > 0 ? 'start' : 'end') : 'middle'); });
  return pic(W, h * s + 56, out, desc);
}
function drawL(Wd, Ht, cw, ch, u, corner, hide = -1) {
  // a W by H rectangle with a cw by ch notch cut from one corner; all six sides labeled (side hide gets a ? instead)
  const pts = corner === 'tr' ? [[0, 0], [Wd - cw, 0], [Wd - cw, ch], [Wd, ch], [Wd, Ht], [0, Ht]]
    : [[0, 0], [Wd, 0], [Wd, Ht - ch], [Wd - cw, Ht - ch], [Wd - cw, Ht], [0, Ht]];
  const len = pts.map((p, i) => { const q = pts[(i + 1) % 6]; return Math.abs(q[0] - p[0]) + Math.abs(q[1] - p[1]); });
  const labels = len.map((x, i) => i === hide ? '?' : x);
  return drawPoly(pts, labels, u, `L-shaped figure made of rectangles. Sides: ${labels.map(x => x === '?' ? 'unknown' : x + ' ' + u).join(', ')}`, true);
}
// a rectangle or L-shape on a grid of unit squares, one square of grid showing around it
function drawGrid(w, h, cw, ch) {
  const s = Math.min(185 / (w + 2), 115 / (h + 2), 20), ox = (W - (w + 2) * s) / 2, oy = 8;
  const pts = cw ? [[0, 0], [w - cw, 0], [w - cw, ch], [w, ch], [w, h], [0, h]] : [[0, 0], [w, 0], [w, h], [0, h]];
  const P = pts.map(([a, b]) => `${(ox + (a + 1) * s).toFixed(1)},${(oy + (b + 1) * s).toFixed(1)}`).join(' ');
  let o = `<polygon points="${P}" fill="#dcdcdc" stroke="none"/>`;
  for (let i = 0; i <= w + 2; i++) o += `<line x1="${(ox + i * s).toFixed(1)}" y1="${oy}" x2="${(ox + i * s).toFixed(1)}" y2="${(oy + (h + 2) * s).toFixed(1)}" stroke="#aaa" stroke-width="1"/>`;
  for (let j = 0; j <= h + 2; j++) o += `<line x1="${ox.toFixed(1)}" y1="${(oy + j * s).toFixed(1)}" x2="${(ox + (w + 2) * s).toFixed(1)}" y2="${(oy + j * s).toFixed(1)}" stroke="#aaa" stroke-width="1"/>`;
  o += `<polygon points="${P}" fill="none" stroke="#222" stroke-width="2.4"/>`;
  const cells = w * h - (cw || 0) * (ch || 0);
  return pic(W, (h + 2) * s + 16, o, `${cw ? 'L-shaped figure' : 'Rectangle'} drawn on a grid of unit squares, covering ${cells} squares`);
}
function drawBox(l, w, h, u) {
  const s = Math.min(120 / (l + w * .5), 90 / (h + w * .4), 22), L = l * s, D = w * s * .5, Hh = h * s, x = 30, y = 14 + D * .8;
  const dx = D, dy = -D * .8;
  let o = `<rect x="${x}" y="${y}" width="${L}" height="${Hh}" ${ST}/>` +
    `<path d="M${x} ${y} l${dx} ${dy} h${L} l${-dx} ${-dy} Z M${x + L} ${y} l${dx} ${dy} v${Hh} l${-dx} ${-dy} Z" ${ST}/>` +
    `<path d="M${x} ${y + Hh} l${dx} ${dy} v${-Hh} M${x + dx} ${y + dy} h${L}" fill="none" ${DASH}/>`;
  o += lab(x + L / 2, y + Hh + 18, `${fmt(l)} ${u}`) + lab(x + L + dx / 2 + 7, y + Hh + dy / 2 + 12, `${fmt(w)} ${u}`, 'start') + lab(x - 6, y + Hh / 2 + 5, `${fmt(h)} ${u}`, 'end');
  return `<svg class="gen-svg" viewBox="-20 0 ${W + 20} ${y + Hh + 26}" role="img" aria-label="${esc(`Rectangular prism, ${fmt(l)} ${u} long, ${fmt(w)} ${u} wide and ${fmt(h)} ${u} high`)}" style="max-width:${((W + 20) / 96).toFixed(2)}in">${o}</svg>`;
}
function drawTri(b, h, t, u) {
  // base b along the bottom, apex t units from the left (t may be outside 0..b for an obtuse triangle)
  const minx = Math.min(0, t), maxx = Math.max(b, t), s = fit(maxx - minx, h, 160, 100), ox = (W - (maxx - minx) * s) / 2 - minx * s, oy = 14;
  const A = [ox, oy + h * s], B = [ox + b * s, oy + h * s], C = [ox + t * s, oy];
  let o = `<polygon points="${A.join(',')} ${B.join(',')} ${C.join(',')}" ${ST}/>`;
  const fx = C[0];
  if (t < 0 || t > b) o += `<line x1="${t < 0 ? fx : B[0]}" y1="${A[1]}" x2="${t < 0 ? A[0] : fx}" y2="${A[1]}" ${DASH}/>`;
  o += `<line x1="${fx}" y1="${C[1]}" x2="${fx}" y2="${A[1]}" ${DASH}/>` + rightMark(fx, A[1] - 9, t > b ? -9 : 9, 9);
  o += lab((A[0] + B[0]) / 2, A[1] + 18, `${b} ${u}`) + lab(fx + (t > b ? -5 : 5), oy + h * s / 2 + 5, `${h} ${u}`, t > b ? 'end' : 'start');
  return pic(W, h * s + 40, o, `Triangle with base ${b} ${u} and height ${h} ${u}`);
}
function drawPara(b, h, t, side, u) {
  const s = fit(b + t, h, 160, 100), ox = (W - (b + t) * s) / 2, oy = 14, y1 = oy + h * s;
  const P = [[ox, y1], [ox + b * s, y1], [ox + (b + t) * s, oy], [ox + t * s, oy]];
  let o = `<polygon points="${P.map(p => p.join(',')).join(' ')}" ${ST}/>`;
  o += `<line x1="${P[3][0]}" y1="${oy}" x2="${P[3][0]}" y2="${y1}" ${DASH}/>` + rightMark(P[3][0], y1 - 9, 9, 9);
  o += lab((P[0][0] + P[1][0]) / 2, y1 + 18, `${b} ${u}`) + lab(P[3][0] + 5, oy + h * s / 2 + 5, `${h} ${u}`, 'start');
  if (side) o += lab((P[1][0] + P[2][0]) / 2 + 8, (P[1][1] + P[2][1]) / 2 + 5, `${side} ${u}`, 'start');
  return pic(W, h * s + 40, o, `Parallelogram with base ${b} ${u}, height ${h} ${u}${side ? `, slanted side ${side} ${u}` : ''}`);
}
function drawTrap(b1, b2, h, t, u) {
  // b1 bottom, b2 top starting t units in from the left
  const wide = Math.max(b1, t + b2), s = fit(wide, h, 160, 95), ox = (W - wide * s) / 2, oy = 24, y1 = oy + h * s;
  const P = [[ox, y1], [ox + b1 * s, y1], [ox + (t + b2) * s, oy], [ox + t * s, oy]];
  let o = `<polygon points="${P.map(p => p.join(',')).join(' ')}" ${ST}/>`;
  o += `<line x1="${P[3][0]}" y1="${oy}" x2="${P[3][0]}" y2="${y1}" ${DASH}/>` + rightMark(P[3][0], y1 - 9, 9, 9);
  o += lab((P[0][0] + P[1][0]) / 2, y1 + 18, `${b1} ${u}`) + lab((P[2][0] + P[3][0]) / 2, oy - 7, `${b2} ${u}`) + lab(P[3][0] + 5, oy + h * s / 2 + 5, `${h} ${u}`, 'start');
  return pic(W, h * s + 50, o, `Trapezoid with bases ${b1} ${u} and ${b2} ${u}, height ${h} ${u}`);
}
function drawCircle(rad, useD, u) {
  const R = 58, cx = W / 2, cy = 72;
  let o = `<circle cx="${cx}" cy="${cy}" r="${R}" ${ST}/><circle cx="${cx}" cy="${cy}" r="3" fill="#222"/>`;
  if (useD) o += `<line x1="${cx - R}" y1="${cy}" x2="${cx + R}" y2="${cy}" ${THIN}/>` + lab(cx, cy - 8, `${rad * 2} ${u}`);
  else o += `<line x1="${cx}" y1="${cy}" x2="${cx + R}" y2="${cy}" ${THIN}/>` + lab(cx + R / 2, cy - 8, `${rad} ${u}`);
  return pic(W, 150, o, `Circle with ${useD ? `diameter ${rad * 2}` : `radius ${rad}`} ${u}`);
}
function drawCyl(rad, h, useD, u) {
  const R = 64, ry = 26, Hh = Math.max(50, Math.min(120, 100 * h / (rad * 2 + h) * 1.4)), cx = W / 2, top = 30;
  let o = `<path d="M${cx - R} ${top} v${Hh} a${R} ${ry} 0 0 0 ${2 * R} 0 v${-Hh}" ${ST}/>` +
    `<ellipse cx="${cx}" cy="${top}" rx="${R}" ry="${ry}" ${ST}/>` +
    `<path d="M${cx - R} ${top + Hh} a${R} ${ry} 0 0 1 ${2 * R} 0" fill="none" ${DASH}/><circle cx="${cx}" cy="${top}" r="2.5" fill="#222"/>`;
  if (useD) o += `<line x1="${cx - R}" y1="${top}" x2="${cx + R}" y2="${top}" ${THIN}/>` + lab(cx, top - 5, `${rad * 2} ${u}`, 'middle', 15);
  else o += `<line x1="${cx}" y1="${top}" x2="${cx + R}" y2="${top}" ${THIN}/>` + lab(cx + R / 2, top - 5, `${rad} ${u}`, 'middle', 15);
  o += lab(cx + R + 6, top + Hh / 2 + 5, `${h} ${u}`, 'start');
  return pic(W, top + Hh + ry + 10, o, `Cylinder with ${useD ? `diameter ${rad * 2}` : `radius ${rad}`} ${u} and height ${h} ${u}`);
}
function drawCone(rad, h, useD, u) {
  const R = 64, ry = 24, Hh = Math.max(60, Math.min(125, 110 * h / (rad * 2 + h) * 1.6)), cx = W / 2, top = 14, base = top + Hh;
  let o = `<path d="M${cx} ${top} L${cx - R} ${base} a${R} ${ry} 0 0 0 ${2 * R} 0 Z" ${ST}/>` +
    `<path d="M${cx - R} ${base} a${R} ${ry} 0 0 1 ${2 * R} 0" fill="none" ${DASH}/>` +
    `<line x1="${cx}" y1="${top}" x2="${cx}" y2="${base}" ${DASH}/><circle cx="${cx}" cy="${base}" r="2.5" fill="#222"/>`;
  if (useD) o += `<line x1="${cx - R}" y1="${base}" x2="${cx + R}" y2="${base}" ${THIN}/>` + lab(cx, base + ry + 17, `${rad * 2} ${u}`, 'middle', 15);
  else o += `<line x1="${cx}" y1="${base}" x2="${cx + R}" y2="${base}" ${THIN}/>` + lab(cx + R / 2, base + ry + 17, `${rad} ${u}`, 'middle', 15);
  o += lab(cx + 6, top + Hh / 2 + 5, `${h} ${u}`, 'start', 15);
  return pic(W, base + ry + 30, o, `Cone with ${useD ? `diameter ${rad * 2}` : `radius ${rad}`} ${u} and height ${h} ${u}`);
}
function drawSphere(rad, useD, u) {
  const R = 58, ry = 18, cx = W / 2, cy = 72;
  let o = `<circle cx="${cx}" cy="${cy}" r="${R}" ${ST}/><path d="M${cx - R} ${cy} a${R} ${ry} 0 0 0 ${2 * R} 0" fill="none" ${THIN}/>` +
    `<path d="M${cx - R} ${cy} a${R} ${ry} 0 0 1 ${2 * R} 0" fill="none" ${DASH}/><circle cx="${cx}" cy="${cy}" r="3" fill="#222"/>`;
  if (useD) o += `<line x1="${cx - R}" y1="${cy}" x2="${cx + R}" y2="${cy}" ${THIN}/>` + lab(cx, cy - ry - 7, `${rad * 2} ${u}`, 'middle', 16);
  else o += `<line x1="${cx}" y1="${cy}" x2="${cx + R}" y2="${cy}" ${THIN}/>` + lab(cx + R / 2, cy - ry - 7, `${rad} ${u}`, 'middle', 16);
  return pic(W, 150, o, `Sphere with ${useD ? `diameter ${rad * 2}` : `radius ${rad}`} ${u}`);
}
function drawTriPrism(a, b, c, L, u) {
  // right-triangle end at the front (leg a along the bottom, leg b up the right side, hypotenuse c on the left),
  // stretched L back and to the right; the hypotenuse face and the right face show, the bottom is dashed
  const s = Math.min(135 / (a + L * .5), 95 / (b + L * .4), 18), A = a * s, B = b * s, D = L * s * .5, dy = -D * .8, x = 30, base = 16 + D * .8 + B;
  const F = [[x, base], [x + A, base], [x + A, base - B]], Bk = F.map(([px, py]) => [px + D, py + dy]);
  const pt = p => p.map(q => q.toFixed(1)).join(',');
  let o = `<polygon points="${pt(F[0])} ${pt(F[2])} ${pt(Bk[2])} ${pt(Bk[0])}" ${ST}/><polygon points="${pt(F[1])} ${pt(F[2])} ${pt(Bk[2])} ${pt(Bk[1])}" ${ST}/><polygon points="${F.map(pt).join(' ')}" ${ST}/>` +
    `<path d="M${pt(F[0])} L${pt(Bk[0])} L${pt(Bk[1])}" fill="none" ${DASH}/>` + rightMark(x + A, base - 9, -9, 9);
  o += lab(x + A / 2, base + 18, `${a} ${u}`) + lab(x + A + D + 6, base - B / 2 + dy + 5, `${b} ${u}`, 'start') +
    lab((F[0][0] + F[2][0]) / 2 - 12 * B / Math.hypot(A, B), (F[0][1] + F[2][1]) / 2 - 12 * A / Math.hypot(A, B) + 5, `${c} ${u}`, 'end') + lab(x + A + D / 2 + 8, base + dy / 2 + 16, `${L} ${u}`, 'start');
  return `<svg class="gen-svg" viewBox="-34 0 ${W + 50} ${base + 26}" role="img" aria-label="${esc(`Triangular prism, ${L} ${u} long, with right-triangle ends: legs ${a} and ${b} ${u}, hypotenuse ${c} ${u}`)}" style="max-width:${((W + 50) / 96).toFixed(2)}in">${o}</svg>`;
}
function drawTwoBoxes(a, b, u) {
  // two boxes side by side, front view as an L: box A (l1 w h1) and box B (l2 w h2) share the depth w
  const l = a.l + b.l, hmax = Math.max(a.h, b.h), s = Math.min(130 / (l + a.w * .5), 90 / (hmax + a.w * .4), 20);
  const D = a.w * s * .5, dy = -D * .8, x = 26, base = 16 + D * .8 + hmax * s;
  const box = (x0, L, Hh) => `<rect x="${x0}" y="${base - Hh}" width="${L}" height="${Hh}" ${ST}/><path d="M${x0} ${base - Hh} l${D} ${dy} h${L} l${-D} ${-dy} Z M${x0 + L} ${base - Hh} l${D} ${dy} v${Hh} l${-D} ${-dy} Z" ${ST}/>`;
  const A = a.l * s, B = b.l * s;
  // draw the taller one last so its faces sit in front
  let o = a.h >= b.h ? box(x + A, B, b.h * s) + box(x, A, a.h * s) : box(x, A, a.h * s) + box(x + A, B, b.h * s);
  o += lab(x + A / 2, base + 18, `${a.l} ${u}`) + lab(x + A + B / 2, base + 18, `${b.l} ${u}`) + lab(x - 6, base - a.h * s / 2 + 5, `${a.h} ${u}`, 'end') +
    lab(x + A + B + D + 6, base - b.h * s / 2 + dy + 8, `${b.h} ${u}`, 'start') + lab(x + A + B + D / 2 + 6, base + dy / 2 + 14, `${a.w} ${u}`, 'start');
  return `<svg class="gen-svg" viewBox="-22 0 ${W + 40} ${base + 26}" role="img" aria-label="${esc(`Two rectangular prisms joined side by side, both ${a.w} ${u} deep: one ${a.l} by ${a.w} by ${a.h} ${u}, one ${b.l} by ${b.w} by ${b.h} ${u}`)}" style="max-width:${((W + 40) / 96).toFixed(2)}in">${o}</svg>`;
}

/* ---------- problems: {kind, ask, draw, ans (number or text), unit text, check data} ---------- */
const TRIPLES = [[3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 12, 15], [8, 6, 10], [4, 3, 5], [12, 5, 13], [12, 9, 15]];
function makeShape(r, g, kind, umode, pimode) {
  const big = +g >= 4, u = pickUnit(r, umode, big);
  if (kind === 'perim') {
    const T = r.int(1, g === '2' ? 3 : 5), hi = g === '2' ? 12 : 20;
    if (T === 1) { const w = r.int(3, hi), h = r.int(2, Math.min(w, hi)); if (w === h) return null;
      return { kind, ask: 'perimeter', u, sides: [w, h, w, h], ans: 2 * w + 2 * h, draw: drawPoly([[0, 0], [w, 0], [w, h], [0, h]], [w, h, w, h], u, `Rectangle with sides ${w}, ${h}, ${w} and ${h} ${u}`), key: `rect ${w}x${h}` }; }
    if (T === 2) { const [a, b, c] = r.pick(TRIPLES), k = g === '2' ? 1 : r.int(1, 2);
      const sides = [a * k, b * k, c * k], pts = [[0, b * k], [a * k, b * k], [0, 0]];
      return { kind, ask: 'perimeter', u, sides, ans: sides[0] + sides[1] + sides[2], draw: drawPoly(pts, [a * k, c * k, b * k], u, `Right triangle with sides ${sides.join(', ')} ${u}`), key: `tri ${sides}` }; }
    if (T === 3) { const s = r.int(2, g === '2' ? 9 : 15); const n = r.pick([3, 4]);
      const pts = n === 4 ? [[0, 0], [s, 0], [s, s], [0, s]] : [[0, s * .866], [s, s * .866], [s / 2, 0]];
      return { kind, ask: 'perimeter', u, sides: Array(n).fill(s), ans: n * s, draw: drawPoly(pts, Array(n).fill(s), u, `${n === 4 ? 'Square' : 'Triangle'} with all sides ${s} ${u}`), key: `reg${n} ${s}` }; }
    if (T === 4) {   // pentagon shaped like a house; the roof is a 3-4-5 style triangle so every side is whole
      const [hx, c, roof] = r.pick([[3, 4, 5], [4, 3, 5], [6, 8, 10], [8, 6, 10], [5, 12, 13]]), a = 2 * hx, b = r.int(3, 12);
      const order = [[0, c], [a / 2, 0], [a, c], [a, c + b], [0, c + b]], sides = [roof, roof, b, a, b];
      return { kind, ask: 'perimeter', u, sides, ans: sides.reduce((x, y) => x + y, 0), draw: drawPoly(order, sides, u, `Pentagon shaped like a house, sides ${sides.join(', ')} ${u}`), key: `pent ${sides}` }; }
    const w = r.int(6, 14), h = r.int(5, 10), cw = r.int(Math.ceil(w / 3), w - 3), ch = r.int(Math.ceil(h / 3), h - 2);
    return { kind, ask: 'perimeter', u, sides: [w - cw, ch, cw, h - ch, w, h], ans: 2 * (w + h), draw: drawL(w, h, cw, ch, u, 'tr'), key: `L ${w} ${h} ${cw} ${ch}` };
  }
  if (kind === 'area' || kind === 'ap') {
    const w = r.int(2, g === '3' ? 10 : 25), h = r.int(2, g === '3' ? 9 : 15); if (w === h && r.chance(.6)) return null;
    const ask = kind === 'ap' ? r.pick(['area', 'perimeter', 'both']) : 'area';
    return { kind: 'rect', ask, u, w, h, ans: ask === 'perimeter' ? 2 * (w + h) : w * h, ans2: 2 * (w + h), draw: drawRect(w, h, u), key: `R ${w} ${h} ${ask}` };
  }
  if (kind === 'compo') {
    const w = r.int(6, g === '3' ? 10 : 16), h = r.int(5, g === '3' ? 9 : 12), cw = r.int(Math.max(2, Math.ceil(w / 3)), w - 3), ch = r.int(Math.max(2, Math.ceil(h / 3)), h - 3);
    if (cw > w - 3 || ch > h - 3) return null;
    const ask = g === '3' ? 'area' : r.pick(['area', 'area', 'perimeter']);
    return { kind: 'L', ask, u, w, h, cw, ch, ans: ask === 'area' ? w * h - cw * ch : 2 * (w + h), draw: drawL(w, h, cw, ch, u, r.pick(['tr', 'br'])), key: `L ${w} ${h} ${cw} ${ch} ${ask}` };
  }
  if (kind === 'missing') {
    const w = r.int(3, 15), h = r.int(2, 12), byArea = r.chance(.5);
    return { kind: 'miss', ask: 'side', u, w, h, byArea, ans: h, given: byArea ? w * h : 2 * (w + h), key: `M ${w} ${h} ${byArea}`,
      text: byArea ? `A rectangle has an area of ${w * h} ${sq(u, g)}. One side is ${w} ${u}. How long is the other side?` : `A rectangle has a perimeter of ${2 * (w + h)} ${u}. One side is ${w} ${u}. How long is the other side?` };
  }
  if (kind === 'unknown') {
    // perimeter given, one side marked ?: a rectangle or an L-shape
    if (r.chance(.5)) { const w = r.int(3, 20), h = r.int(2, 20); if (w === h) return null;
      const sides = [w, h, w, h], hide = r.int(0, 3), labels = sides.map((x, i) => i === hide ? '?' : x);
      return { kind: 'unk', ask: 'unknown', u, sides, hide, given: 2 * (w + h), ans: sides[hide], key: `U rect ${w} ${h} ${hide}`,
        draw: `<p>Perimeter = ${2 * (w + h)} ${u}</p>` + drawPoly([[0, 0], [w, 0], [w, h], [0, h]], labels, u, `Rectangle with perimeter ${2 * (w + h)} ${u}; sides ${labels.map(x => x === '?' ? 'unknown' : x + ' ' + u).join(', ')}`) }; }
    const w = r.int(6, 14), h = r.int(5, 10), cw = r.int(Math.ceil(w / 3), w - 3), ch = r.int(Math.ceil(h / 3), h - 2), hide = r.int(0, 5);
    const sides = [w - cw, ch, cw, h - ch, w, h];
    return { kind: 'unk', ask: 'unknown', u, sides, hide, given: 2 * (w + h), ans: sides[hide], key: `U L ${w} ${h} ${cw} ${ch} ${hide}`,
      draw: `<p>Perimeter = ${2 * (w + h)} ${u}</p>` + drawL(w, h, cw, ch, u, 'tr', hide) };
  }
  if (kind === 'grid') {
    const w = r.int(2, 8), h = r.int(2, 6);
    if (r.chance(.4) && w >= 4 && h >= 3) { const cw = r.int(1, w - 2), ch = r.int(1, h - 1);
      return { kind: 'grid', ask: 'area', u, w, h, cw, ch, ans: w * h - cw * ch, draw: drawGrid(w, h, cw, ch), key: `G ${w} ${h} ${cw} ${ch}` }; }
    if (w === h && r.chance(.5)) return null;
    return { kind: 'grid', ask: 'area', u, w, h, cw: 0, ch: 0, ans: w * h, draw: drawGrid(w, h, 0, 0), key: `G ${w} ${h}` };
  }
  if (kind === 'prismsa') {
    const [a, b, c] = r.pick(TRIPLES), L = r.int(2, 12);
    return { kind: 'tprism', ask: 'surface', u, a, b, c, L, ans: a * b + (a + b + c) * L, draw: drawTriPrism(a, b, c, L, u), key: `TP ${a} ${b} ${c} ${L}` };
  }
  if (kind === 'round') {
    const shape = r.pick(['cyl', 'cone', 'sphere']), rad = r.int(2, 10), h = shape === 'sphere' ? 0 : r.int(2, 15), useD = r.chance(.4);
    const exact = shape === 'cyl' ? 3.14 * rad * rad * h : shape === 'cone' ? 3.14 * rad * rad * h / 3 : 4 / 3 * 3.14 * rad * rad * rad;
    return { kind: 'solid', shape, ask: 'volume', u, rad, h, useD, pimode: '3.14', exact, ans: Gen.m.round(exact, 1), key: `V ${shape} ${rad} ${h} ${useD}`,
      draw: shape === 'cyl' ? drawCyl(rad, h, useD, u) : shape === 'cone' ? drawCone(rad, h, useD, u) : drawSphere(rad, useD, u) };
  }
  if (kind === 'vol') {
    const l = r.int(2, 12), w = r.int(2, 8), h = r.int(2, 10);
    return { kind: 'box', ask: 'volume', u, l, w, h, ans: l * w * h, draw: drawBox(l, w, h, u), key: `B ${l} ${w} ${h}` };
  }
  if (kind === 'volc') {
    const w = r.int(2, 6), a = { l: r.int(2, 6), w, h: r.int(2, 9) }, b = { l: r.int(2, 7), w, h: r.int(2, 9) }; if (a.h === b.h) return null;
    return { kind: 'box2', ask: 'volume', u, a, b, ans: a.l * a.w * a.h + b.l * b.w * b.h, draw: drawTwoBoxes(a, b, u), key: `B2 ${JSON.stringify([a, b])}` };
  }
  if (kind === 'sa') {
    const l = r.int(2, 12), w = r.int(2, 8), h = r.int(2, 10);
    return { kind: 'box', ask: 'surface', u, l, w, h, ans: 2 * (l * w + l * h + w * h), draw: drawBox(l, w, h, u), key: `S ${l} ${w} ${h}` };
  }
  if (kind === 'tri') {
    const h = r.int(3, 14), b = r.int(3, 16); if ((b * h) % 2 && r.chance(.5)) return null;   // half-unit answers allowed, fewer of them
    const t = r.chance(.2) ? -r.int(1, 4) : r.int(0, b);
    return { kind: 'tri', ask: 'area', u, b, h, t, ans: b * h / 2, draw: drawTri(b, h, t, u), key: `T ${b} ${h}` };
  }
  if (kind === 'para') {
    const [t, h, side] = r.chance(.6) ? r.pick(TRIPLES) : [r.int(1, 5), r.int(3, 12), 0], b = r.int(Math.max(4, t), 18);
    return { kind: 'para', ask: 'area', u, b, h, side, ans: b * h, draw: drawPara(b, h, t, side, u), key: `P ${b} ${h}` };
  }
  if (kind === 'trap') {
    const b1 = r.int(6, 20), b2 = r.int(3, b1 - 2), h = r.int(3, 12), t = r.int(0, b1 - b2);
    return { kind: 'trap', ask: 'area', u, b1, b2, h, ans: (b1 + b2) * h / 2, draw: drawTrap(b1, b2, h, t, u), key: `Z ${b1} ${b2} ${h}` };
  }
  if (kind === 'poly') return makeShape(r, g, r.pick(['tri', 'para', 'trap']), umode, pimode);
  if (kind === 'circ' || kind === 'carea') {
    const rad = r.int(2, 15), useD = r.chance(.45), ask = kind === 'circ' ? 'circumference' : 'area';
    return { kind: 'circle', ask, u, rad, useD, pimode, ans: ask === 'area' ? rad * rad : 2 * rad, draw: drawCircle(rad, useD, u), key: `C ${rad} ${useD} ${ask}` };
  }
  if (kind === 'circles') return makeShape(r, g, r.pick(['circ', 'carea']), umode, pimode);
  if (kind === 'cyl') {
    const rad = r.int(2, 10), h = r.int(2, 15), useD = r.chance(.4);
    return { kind: 'cyl', ask: 'volume', u, rad, h, useD, pimode, ans: rad * rad * h, draw: drawCyl(rad, h, useD, u), key: `Y ${rad} ${h} ${useD}` };
  }
  if (kind === 'vol8') return makeShape(r, g, r.chance(.6) ? 'cyl' : 'vol', umode, pimode);
}

// the answer text with its unit; circle answers are k (as in kπ) turned into 3.14k or kπ
function answerText(p, g) {
  const u = p.u;
  if (p.kind === 'circle' || p.kind === 'cyl') {
    const pow = p.ask === 'area' ? '²' : p.ask === 'volume' ? '³' : '';
    return piText(p.ans, p.pimode, u, pow);
  }
  if (p.kind === 'solid') return `${fmt(p.ans, 1)} ${cu(u, g)}`;
  const unit = p.kind === 'grid' ? 'square units' : p.ask === 'area' || p.ask === 'both' ? sq(u, g) : p.ask === 'volume' ? cu(u, g) : p.ask === 'surface' ? sq(u, g) : u;
  return `${fmt(p.ans)} ${unit}`;
}
const ASK = { perimeter: 'Perimeter', area: 'Area', volume: 'Volume', surface: 'Surface area', circumference: 'Circumference', side: 'Other side', unknown: 'Missing side' };
function formula(p, g) {   // the worked line for the teacher page
  const u = p.u, A = answerText(p, g), pi = p.pimode === 'pi' ? 'π' : '3.14';
  switch (p.kind) {
    case 'perim': return `${p.sides.join(' + ')} = ${A}`;
    case 'rect': return p.ask === 'perimeter' ? `2 × (${p.w} + ${p.h}) = ${A}` : `${p.w} × ${p.h} = ${A}`;
    case 'L': return p.ask === 'perimeter' ? `${p.w} + ${p.h} + ${p.w - p.cw} + ${p.ch} + ${p.cw} + ${p.h - p.ch} = ${A}` : `${p.w} × ${p.h} − ${p.cw} × ${p.ch} = ${p.w * p.h} − ${p.cw * p.ch} = ${A}`;
    case 'miss': return p.byArea ? `${p.given} ÷ ${p.w} = ${A}` : `${p.given} ÷ 2 = ${p.given / 2}, and ${p.given / 2} − ${p.w} = ${A}`;
    case 'box': return p.ask === 'volume' ? `${p.l} × ${p.w} × ${p.h} = ${A}` : `2 × (${p.l}×${p.w} + ${p.l}×${p.h} + ${p.w}×${p.h}) = 2 × ${p.l * p.w + p.l * p.h + p.w * p.h} = ${A}`;
    case 'box2': return `${p.a.l}×${p.a.w}×${p.a.h} + ${p.b.l}×${p.b.w}×${p.b.h} = ${p.a.l * p.a.w * p.a.h} + ${p.b.l * p.b.w * p.b.h} = ${A}`;
    case 'tri': return `½ × ${p.b} × ${p.h} = ${A}`;
    case 'para': return `${p.b} × ${p.h} = ${A}`;
    case 'trap': return `½ × (${p.b1} + ${p.b2}) × ${p.h} = ${A}`;
    case 'circle': return (p.ask === 'area' ? `${pi} × ${p.rad}² = ${A}` : `2 × ${pi} × ${p.rad} = ${A}`);
    case 'cyl': return `${pi} × ${p.rad}² × ${p.h} = ${A}`;
    case 'unk': { const known = p.sides.filter((x, i) => i !== p.hide); return `${p.given} − (${known.join(' + ')}) = ${p.given} − ${known.reduce((x, y) => x + y, 0)} = ${A}`; }
    case 'grid': return p.cw ? `${p.w} × ${p.h} − ${p.cw} × ${p.ch} = ${p.w * p.h} − ${p.cw * p.ch} = ${A}` : `${p.h} rows of ${p.w} squares: ${p.w} × ${p.h} = ${A}`;
    case 'tprism': return `2 × (½ × ${p.a} × ${p.b}) + (${p.a} + ${p.b} + ${p.c}) × ${p.L} = ${p.a * p.b} + ${(p.a + p.b + p.c) * p.L} = ${A}`;
    case 'solid': { const ex = `${fmt(p.exact, 3)}`;
      return (p.shape === 'cyl' ? `3.14 × ${p.rad}² × ${p.h} = ${ex}` : p.shape === 'cone' ? `3.14 × ${p.rad}² × ${p.h} ÷ 3 = ${ex}` : `4 × 3.14 × ${p.rad}³ ÷ 3 = ${ex}`) + `, rounded to the nearest tenth: ${A}`; }
  }
  return A;
}
void UNAME;
const rNote = p => (p.kind === 'circle' || p.kind === 'cyl' || p.kind === 'solid') && p.useD ? `r = ${p.rad * 2} ÷ 2 = ${p.rad} ${p.u}. ` : '';

/* ---------- grade 4 "formulas": the unit sheet for 4.MD.A.3 (grade 4 math, unit 11.1, day 91) ----------
   Twelve problems with no pictures, in mixed order: 2 area with both sides (one within 100, one a one-digit number
   times a multiple of 10), 2 area with a side unknown, 2 perimeter with a side unknown (even, 100 or less), 3
   perimeter with multi-digit sides, 2 perimeter with like-denominator fraction sides, 1 "times as long" area. Then 5
   wrong answers to fix, one for each error A to E of the unit's error register. Half bare rectangles, half one-line
   stories. No problem uses a pair of numbers that the unit teaches or checks (RESERVED_S11, kept in step with
   data/plans/math-4/items.csv by `python -X utf8 scripts/plan.py reserve math-4 11`). */
// RESERVED_S11 begin (generated; do not edit by hand)
const RESERVED_S11 = [['1', '6', '9'], ['1 1/8', '2 3/8'], ['1 4/5', '2 3/5'], ['1 7/8', '3 5/8'], ['10', '17', '7'], ['10', '2'], ['10', '3'], ['11', '8'], ['12', '38'], ['12', '40'], ['129', '264'], ['13', '42'], ['138', '60', '9'], ['14', '30', '44'], ['14', '9'], ['147', '318'], ['148', '235'], ['150', '3', '50'], ['158', '264'], ['16', '50'], ['17', '24', '58'], ['17', '46'], ['18', '3'], ['189', '274', '463'], ['2', '6'], ['2', '7'], ['2', '9'], ['2 3/4', '6 3/4'], ['2 4/10', '3 1/10'], ['21', '3'], ['22', '5', '6'], ['22', '7'], ['24', '7'], ['24', '8'], ['26', '40'], ['27', '3'], ['275', '419'], ['28', '4'], ['3', '4'], ['3', '5'], ['3', '8'], ['30', '35', '5'], ['30', '5'], ['32', '60'], ['36', '4'], ['4', '5'], ['4', '9'], ['40', '6'], ['42', '6'], ['48', '6'], ['48', '8'], ['5', '60'], ['5', '9'], ['56', '7'], ['6', '7'], ['63', '7'], ['64', '72', '8'], ['70', '8'], ['72', '8']];
// RESERVED_S11 end
const reservedHit = nums => { const s = nums.map(String); return RESERVED_S11.some(set => s.every(x => set.includes(x))); };
const FXU = [['ft', 'feet', 'square feet'], ['m', 'meters', 'square meters'], ['in', 'inches', 'square inches'], ['yd', 'yards', 'square yards'], ['cm', 'centimeters', 'square centimeters']];
const FXU_C = FXU.filter(u => ['ft', 'in', 'yd'].includes(u[0])), FXU_M = FXU.filter(u => ['m', 'cm'].includes(u[0]));
const AREA_THINGS = ['rug', 'garden bed', 'poster', 'patio', 'tablecloth', 'classroom floor', 'mural', 'tile'];
const EDGE_THINGS = [['fence', 'a pen'], ['ribbon', 'a gift box lid'], ['trim', 'a window'], ['rope', 'a play area'], ['tape', 'a table top']];
const NAMES = ['Ava', 'Ben', 'Cruz', 'Dina', 'Eli', 'Fay', 'Gus', 'Hana', 'Ivan', 'June', 'Kai', 'Lena', 'Milo', 'Nia', 'Omar', 'Pia', 'Raj', 'Sol', 'Tess', 'Uma'];
const fracText = (w, n, d) => n === 0 ? `${w}` : w ? `${w} ${n}/${d}` : `${n}/${d}`;
const fracHtml = (w, n, d) => n === 0 ? `${w}` : H.mixed(w, n, d);
// a total in eighths (or any d) as a mixed number with the fraction part under 1, not simplified (grade 4: 4.NF.B.3)
const asMixed = (num, d) => [Math.floor(num / d), num % d];

function fxProblem(r, type, units) {
  const pool = units === 'metric' ? FXU_M : units === 'customary' ? FXU_C : FXU;
  const [u, ulong, usq] = r.pick(pool), story = r.chance(.5);
  const thing = r.pick(AREA_THINGS), [edge, around] = r.pick(EDGE_THINGS);
  if (type === 'areaSmall' || type === 'areaTens') {
    const w = r.int(3, 9), l = type === 'areaSmall' ? r.int(w + 1, Math.min(12, Math.floor(100 / w))) : 10 * r.int(2, 9);
    if (type === 'areaSmall' && w * l > 100) return null;
    const ans = l * w, nums = [l, w];
    const text = story ? `A ${thing} is ${l} ${ulong} long and ${w} ${ulong} wide. How much space does it cover?`
      : `A rectangle is ${l} ${ulong} long and ${w} ${ulong} wide. Find its area.`;
    return { type, nums, text, html: esc(text), eq: `${l} × ${w} = ${ans}`, a: `${ans} ${usq}`, ans, unitKind: 'sq', p: { type, l, w } };
  }
  if (type === 'areaMissing') {
    const w = r.int(3, 9), l = r.int(w + 1, 12), A = l * w;
    if (A > 100) return null;
    const nums = [A, w];
    const text = story ? `A ${thing} covers ${A} ${usq}. It is ${w} ${ulong} wide. How long is it?`
      : `A rectangle has an area of ${A} ${usq}. One side is ${w} ${ulong}. Find the other side.`;
    return { type, nums, text, html: esc(text), eq: `${w} × ? = ${A}, so ? = ${l}`, a: `${l} ${ulong}`, ans: l, unitKind: 'len', p: { type, A, w } };
  }
  if (type === 'perimMissing') {
    const l = r.int(6, 30), w = r.int(2, l - 1), P = 2 * (l + w);
    if (P > 100) return null;
    const nums = [P, l];
    const text = story ? `${edge[0].toUpperCase() + edge.slice(1)} goes all the way around ${around}: ${P} ${ulong}. It is ${l} ${ulong} long. How wide is it?`
      : `A rectangle has a perimeter of ${P} ${ulong}. It is ${l} ${ulong} long. How wide is it?`;
    return { type, nums, text, html: esc(text), eq: `${l} + ? + ${l} + ? = ${P}, so ? = ${w}`, a: `${w} ${ulong}`, ans: w, unitKind: 'len', p: { type, P, l } };
  }
  if (type === 'perimBig') {
    const l = r.int(100, 420), w = r.int(25, Math.min(l - 1, 480 - l)), P = 2 * (l + w);
    if (P >= 1000 || w < 10) return null;
    const nums = [l, w];
    const text = story ? `A field is ${l} ${ulong} long and ${w} ${ulong} wide. How far is it all the way around?`
      : `A rectangle is ${l} ${ulong} long and ${w} ${ulong} wide. Find its perimeter.`;
    return { type, nums, text, html: esc(text), eq: `${l} + ${w} = ${l + w}; ${l + w} + ${l + w} = ${P}`, a: `${P.toLocaleString('en-US')} ${ulong}`, ans: P, unitKind: 'len', p: { type, l, w } };
  }
  if (type === 'perimFrac') {
    const d = r.pick([2, 3, 4, 5, 6, 8, 10, 12]), lw = r.int(2, 8), ln = r.int(1, d - 1), ww = r.int(1, lw), wn = r.int(1, d - 1);
    if (ww === lw && wn >= ln) return null;
    const total = 2 * ((lw * d + ln) + (ww * d + wn)), [tw, tn] = asMixed(total, d);
    const L = fracText(lw, ln, d), Wt = fracText(ww, wn, d), A = fracText(tw, tn, d);
    const nums = [L, Wt];
    const lead = story ? `A card is` : `A rectangle is`;
    const tail = story ? `How long is the edge all the way around?` : `Find its perimeter.`;
    const text = `${lead} ${L} ${ulong} long and ${Wt} ${ulong} wide. ${tail}`;
    return { type, nums, text, html: `${lead} ${fracHtml(lw, ln, d)} ${esc(ulong)} long and ${fracHtml(ww, wn, d)} ${esc(ulong)} wide. ${tail}`,
      eq: `${L} + ${Wt} + ${L} + ${Wt} = ${A}`, a: `${A} ${ulong}`, ans: total / d, unitKind: 'len', p: { type, d, lnum: lw * d + ln, wnum: ww * d + wn } };
  }
  if (type === 'times') {
    const w = r.int(2, 5), k = r.int(2, 4), l = k * w, A = l * w;
    if (A > 100) return null;
    const nums = [w, k];
    const text = story ? `A ${thing} is ${w} ${ulong} wide. It is ${k} times as long as it is wide. Find its area.`
      : `A rectangle is ${w} ${ulong} wide and ${k} times as long. Find its area.`;
    return { type, nums, text, html: esc(text), eq: `length ${k} × ${w} = ${l}; area ${l} × ${w} = ${A}`, a: `${A} ${usq}`, ans: A, unitKind: 'sq', p: { type, w, k } };
  }
  return null;
}

// one wrong answer to fix for each error A to E
function fxFix(r, err, units) {
  const pool = units === 'metric' ? FXU_M : units === 'customary' ? FXU_C : FXU;
  const [u, ulong, usq] = r.pick(pool), who = r.pick(NAMES);
  if (err === 'A') {   // area asked, perimeter given
    const l = r.int(5, 12), w = r.int(2, l - 2), right = l * w, wrong = 2 * (l + w);
    if (right === wrong) return null;
    return { err, nums: [l, w], text: `${who} says: "A rectangle ${l} ${ulong} by ${w} ${ulong} has an area of ${wrong} ${usq}."`,
      a: `${right} ${usq}: ${l} × ${w} = ${right}. ${who} found the perimeter`, ans: right, p: { err, l, w } };
  }
  if (err === 'B') {   // perimeter as one length plus one width
    const l = r.int(8, 25), w = r.int(3, l - 1), right = 2 * (l + w);
    return { err, nums: [l, w], text: `${who} says: "A rectangle ${l} ${ulong} by ${w} ${ulong} has a perimeter of ${l + w} ${ulong}."`,
      a: `${right} ${ulong}: ${l} + ${w} + ${l} + ${w} = ${right}. ${who} added only two sides`, ans: right, p: { err, l, w } };
  }
  if (err === 'C') {   // side from an area by subtracting
    const w = r.int(3, 9), l = r.int(w + 1, 11), A = l * w;
    if (A > 100) return null;
    return { err, nums: [A, w], text: `${who} says: "The area is ${A} ${usq} and one side is ${w} ${ulong}, so the other side is ${A - w} ${ulong}."`,
      a: `${l} ${ulong}: ${w} × ? = ${A}, so ? = ${l}. ${who} subtracted`, ans: l, p: { err, A, w } };
  }
  if (err === 'D') {   // side from a perimeter: one side taken off, not halved
    const l = r.int(8, 24), w = r.int(2, l - 1), P = 2 * (l + w);
    if (P > 100) return null;
    return { err, nums: [P, l], text: `${who} says: "The perimeter is ${P} ${ulong} and it is ${l} ${ulong} long, so it is ${P - l} ${ulong} wide."`,
      a: `${w} ${ulong}: ${l} + ? + ${l} + ? = ${P}, so ? = ${w}. ${who} took off one side and did not halve`, ans: w, p: { err, P, l } };
  }
  if (err === 'E') {   // area written in a length unit
    const l = r.int(4, 12), w = r.int(2, 9), A = l * w;
    return { err, nums: [l, w], text: `${who} says: "A rug ${l} ${ulong} by ${w} ${ulong} has an area of ${A} ${ulong}."`,
      a: `${A} ${usq}. The number is right, but area is in square units`, ans: A, p: { err, l, w } };
  }
  return null;
}

function makeFormulas(v, r) {
  const plan = r.shuffle(['areaSmall', 'areaTens', 'areaMissing', 'areaMissing', 'perimMissing', 'perimMissing', 'perimBig', 'perimBig', 'perimBig', 'perimFrac', 'perimFrac', 'times']);
  const used = new Set(), probs = [];
  const fresh = (maker) => { for (let t = 0; t < 400; t++) { const p = maker(); if (!p) continue; const k = p.nums.join('|'); if (used.has(k) || reservedHit(p.nums)) continue; used.add(k); return p; } return null; };
  for (const t of plan) { const p = fresh(() => fxProblem(r, t, v.units)); if (p) probs.push(p); }
  const fixes = ['A', 'B', 'C', 'D', 'E'].map(e => fresh(() => fxFix(r, e, v.units))).filter(Boolean);
  const items = probs.map(p => ({ q: p.text, a: p.a, p: { ...p.p, unitKind: p.unitKind } }))
    .concat(fixes.map(f => ({ q: f.text, a: f.a, p: f.p })));
  const cells = probs.map((p, i) => H.q(i + 1, p.html, `<p class="ms-ans">Equation: ${H.blank(p.eq, 12)}</p><p class="ms-ans">Answer: ${H.blank(p.a)}</p>`));
  const fixCells = fixes.map((f, i) => H.q(probs.length + i + 1, esc(f.text), `<p class="ms-ans">What went wrong, and the right answer: ${H.blank(f.a, 16)}</p>`));
  const teacher = `<h3>Equations</h3><ol class="ms-steps">${probs.map(p => `<li>${esc(p.eq)}; ${esc(p.a)}</li>`).join('')}${fixes.map(f => `<li>Error ${f.err}: ${esc(f.a)}</li>`).join('')}</ol>`;
  return {
    title: 'Area and perimeter formulas: Grade 4', level: 'Grade 4',
    ican: 'I can use both formulas with no picture, with big sides and fraction sides.',
    directions: 'Write an equation for each rectangle, then answer with the unit. Sketch a rectangle if it helps.',
    minutes: 30, materials: 'pencil, scrap paper for sketches',
    parts: [part('Practice', cells.join('')), part('Fix it', fixCells.join(''))], items, teacher,
    mistakes: 'A: one formula for the other measure. B: one length plus one width. C: a side from an area by subtracting. D: from a perimeter, one side taken off or not halved. E: a length unit on an area.',
    notes: 'Made for grade 4 math, unit 11.1, day 91 (Curio Class course). No problem reuses a pair of numbers the unit teaches or checks. A fraction answer is written with its fraction part under 1 and not simplified; equivalent forms are right.',
  };
}

function verifyFormulas(s) {
  const out = [];
  const num = a => { const m = String(a).match(/^([\d,]+)(?: (\d+)\/(\d+))?/); return m ? +m[1].replace(/,/g, '') + (m[2] ? m[2] / m[3] : 0) : NaN; };
  for (const it of s.items) {
    const p = it.p; let want;
    if (p.err) want = { A: p.l * p.w, B: 2 * (p.l + p.w), C: p.A / p.w, D: p.P / 2 - p.l, E: p.l * p.w }[p.err];
    else want = { areaSmall: p.l * p.w, areaTens: p.l * p.w, areaMissing: p.A / p.w, perimMissing: p.P / 2 - p.l, perimBig: 2 * (p.l + p.w),
      perimFrac: p.d ? 2 * (p.lnum + p.wnum) / p.d : NaN, times: p.k * p.w * p.w }[p.type];
    const got = num(it.a);
    if (!(Math.abs(got - want) < 1e-9)) out.push(`${it.q}: key says ${it.a}, want ${want}`);
    if (!Number.isInteger(want) && !p.d) out.push(`${it.q}: not a whole number`);
    if (p.unitKind && /square/.test(it.a) !== (p.unitKind === 'sq')) out.push(`${it.q}: unit ${it.a}`);
  }
  if (s.items.length !== 17) out.push(`${s.items.length} items, want 17`);
  return out;
}

Gen.add('measure-shapes', {
  title: 'Area, Perimeter and Volume', type: 'Diagram',
  css: `.ms-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px 16px;margin:6px 0 10px}
.ms-cell{border:1px solid #bbb;border-radius:8px;padding:6px 8px;display:flex;flex-direction:column;break-inside:avoid}
.ms-cell > p{margin:0;font-size:14px}
.ms-cell svg{margin:2px auto;max-height:1.75in}
.ms-cell .ms-ans{margin-top:auto;font-size:14.5px}
.ms-cell .ws-blank{min-width:5.6em !important}
.ms-ans{line-height:1.6}
.ms-text{min-height:1.1in}
.ms-steps{margin:4px 0;padding-left:1.8em;font-size:14px;columns:2;column-gap:24px}
.ms-steps li{margin-bottom:5px;break-inside:avoid}
.ms-formulas{font-size:13.5px;margin:2px 0 0}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '4' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => SKILLS[v.grade], def: 'ap' },
    { id: 'units', label: 'Units', type: 'select', options: UNITS, def: 'both' },
    { id: 'pi', label: 'Pi', type: 'select', options: [['3.14', 'Use 3.14'], ['pi', 'Answer in terms of π']], def: '3.14', show: piChoice },
    { id: 'count', label: 'Problems', type: 'select', options: COUNTS.map(c => [String(c), String(c)]), def: '9' },
  ],
  make(v, r) {
    if (v.skill === 'formulas') return makeFormulas(v, r);
    const g = v.grade, skill = v.skill, n = +v.count, pimode = piChoice(v) ? v.pi : '3.14';
    const label = SKILLS[g].find(s => s[0] === skill)[1], gname = GRADES.find(x => x[0] === g)[1];
    let kinds = skill;
    const pick = () => {
      const k = skill === 'mix3' ? r.pick(['perim', 'area', 'compo']) : skill === 'mix4' ? r.pick(['ap', 'compo', 'missing']) : kinds;
      return makeShape(r, g, k, v.units, pimode);
    };
    const ps = r.distinct(n + 1, pick, p => p.key), ex = ps.pop();
    const items = [], cells = [];
    ps.forEach((p, i) => {
      const A = answerText(p, g);
      const it = { q: p.key + ' ' + p.u, a: A, p: { ...p, draw: undefined } };
      delete it.p.draw;
      items.push(it);
      let ask = p.ask === 'both' ? null : ASK[p.ask];
      let body;
      if (p.kind === 'miss') body = `<p class="ms-text">${esc(p.text)}</p>`;
      else body = p.draw;
      let ansLine;
      if (p.ask === 'both') {
        const A2 = `${fmt(p.ans2)} ${p.u}`; it.a2 = A2;
        ansLine = `<p class="ms-ans">Area = ${H.blank(A)}</p><p class="ms-ans">Perimeter = ${H.blank(A2)}</p>`;
      } else ansLine = `<p class="ms-ans">${ask} = ${H.blank(A)}</p>`;
      cells.push(`<div class="ms-cell"><p><span class="ws-num">${i + 1}.</span> ${p.kind === 'miss' ? '' : `Find the ${p.ask === 'both' ? 'area and perimeter' : ask.toLowerCase()}.`}</p>${body}${ansLine}</div>`);
    });
    const exText = (() => {
      const A = answerText(ex, g), what = ex.ask === 'both' ? 'area' : ASK[ex.ask].toLowerCase();
      const desc = { perim: 'add the lengths of all the sides', rect: ex.ask === 'perimeter' ? 'add all four sides, or 2 × (length + width)' : 'multiply length × width',
        L: ex.ask === 'perimeter' ? 'add all six sides' : 'split it into rectangles, or take the small rectangle away from the big one', miss: 'work backward from the area or perimeter',
        box: ex.ask === 'volume' ? 'multiply length × width × height' : 'add the areas of all six faces', box2: 'find the volume of each box and add them',
        tri: 'area = ½ × base × height', para: 'area = base × height', trap: 'area = ½ × (base 1 + base 2) × height',
        circle: ex.ask === 'area' ? `area = π × r × r${ex.useD ? ' (halve the diameter to get r)' : ''}` : `circumference = 2 × π × r, or π × d`,
        cyl: `volume = π × r × r × height${ex.useD ? ' (halve the diameter to get r)' : ''}`,
        unk: 'add the sides you know, then subtract that total from the perimeter', grid: 'count the squares inside, or count the rows and multiply by the squares in each row',
        tprism: 'add the two triangle ends (½ × base × height each) and the three rectangle faces (each side of the triangle × the length)',
        solid: { cyl: 'volume = 3.14 × r × r × height', cone: 'volume = 3.14 × r × r × height ÷ 3', sphere: 'volume = 4 × 3.14 × r × r × r ÷ 3' }[ex.shape] + `${ex.useD ? ' (halve the diameter to get r)' : ''}, then round to the nearest tenth` }[ex.kind];
      const head = ex.kind === 'miss' ? `${esc(ex.text)} To find it,` : ex.kind === 'unk' ? `The perimeter is ${ex.given} ${ex.u} and one side is marked ?. To find it,`
        : `How to find the ${what} of ${{ perim: 'a shape', rect: 'a rectangle', L: 'an L-shape', box: 'a box', box2: 'two joined boxes', tri: 'a triangle', para: 'a parallelogram', trap: 'a trapezoid', circle: 'a circle', cyl: 'a cylinder',
          grid: 'a shape on a grid', tprism: 'a triangular prism', solid: { cyl: 'a cylinder', cone: 'a cone', sphere: 'a sphere' }[ex.shape] }[ex.kind]}:`;
      return example(`${head} ${desc}.`, `${rNote(ex)}${ASK[ex.ask === 'both' ? 'area' : ex.ask]} = ${formula(ex.ask === 'both' ? { ...ex, ask: 'area' } : ex, g)}`);
    })();
    const parts = [part('', exText), part('Practice', `<div class="ms-grid">${cells.join('')}</div>`)];
    const usesSq = ps.some(p => ['area', 'surface', 'both'].includes(p.ask)), usesCu = ps.some(p => p.ask === 'volume');
    const unitWord = +g >= 6 ? `square units (cm²)${usesCu ? ' and cubic units (cm³)' : ''}` : `square units${usesCu ? ' and cubic units' : ''}`;
    const piWord = usesPi(v) ? (pimode === 'pi' ? ' Leave π in your answer, like 16π cm².' : ' Use 3.14 for π.') + (skill === 'round' ? ' Round each answer to the nearest tenth.' : '') : '';
    const directions = `Find each measurement. Write the number and the unit on the line${usesSq || usesCu ? `, using ${unitWord} where they belong` : ''}.${piWord}`;
    const teacher = `<h3>Worked answers</h3><ol class="ms-steps">${ps.map(p => `<li>${p.ask === 'both' ? `Area: ${esc(formula({ ...p, ask: 'area' }, g))}. Perimeter: ${esc(formula({ ...p, ask: 'perimeter', ans: p.ans2 }, g))}` : esc(rNote(p) + formula(p, g))}</li>`).join('')}</ol>`;
    const mistakes = {
      2: 'Missing a side, especially the sides with no label on a square. Count sides as you add them.',
      3: 'Mixing up area and perimeter, and writing area in plain units. On L-shapes, counting the corner piece twice or not at all.',
      4: 'Mixing up area and perimeter. For a missing side from the perimeter, forgetting to halve first.',
      5: 'Adding the three edges instead of multiplying, and writing square units for volume.',
      6: 'Forgetting the ½ for triangles and trapezoids, and using the slanted side as the height. Surface area: counting only three faces.',
      7: 'Using the diameter as the radius, and mixing up the two formulas. Area is in square units; circumference is not.',
      8: 'Using the diameter as the radius, and forgetting to square the radius.' }[g];
    return {
      title: `${label}: ${gname}`, level: gname + (usesPi(v) ? (pimode === 'pi' ? ', answers in terms of π' : ', π ≈ 3.14') : ''),
      ican: { perim: 'I can find the perimeter of a shape by adding its sides.', area: 'I can find the area of a rectangle.', compo: 'I can find the area of a shape made of rectangles.',
        mix3: 'I can tell area from perimeter and find both.', ap: 'I can find the area and perimeter of rectangles.', missing: 'I can find a missing side from the area or perimeter.',
        mix4: 'I can solve area and perimeter problems.', vol: 'I can find the volume of a rectangular prism.', volc: 'I can find the volume of a solid made of two boxes.',
        tri: 'I can find the area of a triangle.', para: 'I can find the area of a parallelogram.', trap: 'I can find the area of a trapezoid.', poly: 'I can find the area of triangles, parallelograms and trapezoids.',
        sa: 'I can find the surface area of a rectangular prism.', circ: 'I can find the circumference of a circle.', carea: 'I can find the area of a circle.', circles: 'I can find the circumference and area of a circle.',
        cyl: 'I can find the volume of a cylinder.', vol8: 'I can find the volume of prisms and cylinders.',
        unknown: 'I can find a missing side when I know the perimeter.', grid: 'I can find area by counting unit squares.',
        prismsa: 'I can find the surface area of a triangular prism.', round: 'I can find the volume of cylinders, cones and spheres.' }[skill],
      directions, minutes: n > 9 ? 30 : 25, materials: 'pencil' + (+g >= 6 ? ', calculator optional' : ''),
      parts, items, teacher, mistakes,
      notes: `Shapes are drawn roughly to scale, so students can sense when an answer is far off, but they should use the labels, not a ruler.${['tri', 'para', 'trap', 'poly'].includes(skill) ? ' Some parallelograms show the slanted side as well: it is there on purpose, to check that students use the height.' : ''}${skill === 'round' ? ' Answers use 3.14 for π and are rounded to the nearest tenth; the teacher page shows the unrounded value.' : usesPi(v) && pimode !== 'pi' ? ' Answers with 3.14 are exact to the hundredth, so a calculator answer should match.' : ''}${skill === 'grid' ? ' Grid answers are in square units with no length unit, since the squares have no size given.' : ''}`,
    };
  },
  verify(s, v) {
    if (v.skill === 'formulas') return verifyFormulas(s);
    const out = [];
    const g = +v.grade;
    for (const it of s.items) {
      const p = it.p;
      let want;   // recomputed here from the measurements, in hundredths for the π answers
      switch (p.kind) {
        case 'perim': want = p.sides.reduce((a, b) => a + b, 0); break;
        case 'rect': want = p.ask === 'perimeter' ? p.w + p.h + p.w + p.h : p.w * p.h; break;
        case 'L': want = p.ask === 'perimeter' ? (p.w - p.cw) + p.ch + p.cw + (p.h - p.ch) + p.w + p.h : (p.w - p.cw) * p.h + p.cw * (p.h - p.ch); break;
        case 'miss': want = p.byArea ? p.given / p.w : p.given / 2 - p.w; break;
        case 'box': want = p.ask === 'volume' ? p.l * p.w * p.h : 2 * p.l * p.w + 2 * p.l * p.h + 2 * p.w * p.h; break;
        case 'box2': want = p.a.l * p.a.w * p.a.h + p.b.l * p.b.w * p.b.h; break;
        case 'tri': want = p.b * p.h / 2; break;
        case 'para': want = p.b * p.h; break;
        case 'trap': want = (p.b1 + p.b2) / 2 * p.h; break;
        case 'circle': want = p.ask === 'area' ? p.rad * p.rad : p.rad * 2; break;
        case 'cyl': want = p.rad * p.rad * p.h; break;
        case 'unk': { let known = 0; p.sides.forEach((x, i) => { if (i !== p.hide) known += x; }); want = p.given - known; break; }
        case 'grid': want = p.cw ? (p.w - p.cw) * p.h + p.cw * (p.h - p.ch) : p.w * p.h; break;
        case 'tprism': want = p.a * p.b / 2 + p.a * p.b / 2 + p.a * p.L + p.b * p.L + p.c * p.L; break;
        case 'solid': {   // in whole hundredths of a cubic unit, then to the nearest tenth
          const hund = p.shape === 'cyl' ? 314 * p.rad * p.rad * p.h : p.shape === 'cone' ? 314 * p.rad * p.rad * p.h / 3 : 4 * 314 * p.rad * p.rad * p.rad / 3;
          want = Math.round(hund / 10) / 10; break; }
      }
      const m = String(it.a).match(/^([\d,.]*)(π?) (.+)$/);
      if (!m) { out.push(`${it.q}: cannot read ${it.a}`); continue; }
      let got = m[1] === '' ? 1 : parseFloat(m[1].replace(/,/g, ''));
      if (p.kind === 'circle' || p.kind === 'cyl') {
        if (p.pimode === 'pi') { if (!m[2] || Math.abs(got - want) > 1e-9) out.push(`${it.q}: key says ${it.a}, want ${want}π`); }
        else if (Math.abs(got - want * 3.14) > 0.004) out.push(`${it.q}: key says ${it.a}, want ${(want * 3.14).toFixed(2)}`);
      } else if (Math.abs(got - want) > 1e-9) out.push(`${it.q}: key says ${it.a}, want ${want}`);
      if (!(want > 0) || ((p.kind === 'miss' || p.kind === 'unk') && !Number.isInteger(want))) out.push(`${it.q}: bad measurement ${want}`);
      if (p.kind === 'unk' && p.sides.reduce((x, y) => x + y, 0) !== p.given) out.push(`${it.q}: sides do not add to the given perimeter`);
      if (p.kind === 'tprism' && p.a * p.a + p.b * p.b !== p.c * p.c) out.push(`${it.q}: not a right triangle`);
      // the unit must match the question: plain, square or cubic
      const unit = m[3], sqU = /square|²/.test(unit), cuU = /cubic|³/.test(unit);
      const needSq = ['area', 'surface'].includes(p.ask) || p.ask === 'both', needCu = p.ask === 'volume';
      if (sqU !== needSq || cuU !== needCu) out.push(`${it.q}: unit ${unit} does not fit ${p.ask}`);
      if (g < 6 && /[²³]/.test(unit)) out.push(`${it.q}: exponent units below grade 6`);
      if (p.kind === 'para' && p.side && p.side <= p.h) out.push(`${it.q}: slanted side not longer than the height`);
      if (it.a2 && parseFloat(it.a2) !== 2 * (p.w + p.h)) out.push(`${it.q}: perimeter ${it.a2}`);
    }
    return out;
  },
});
})();
