// Fractions generator, grades 3-7. Grade 3 works from pictures and number lines (3.NF.1-3); grade 4 equivalence,
// comparing, like-denominator sums and mixed numbers (4.NF.1-4); grade 5 unlike denominators, multiplying and unit
// fraction division (5.NF.1-7); grade 6 dividing fractions by fractions (6.NS.1); grade 7 negative fractions (7.NS.1-3).
(() => {
const H = Gen.h, { part, example, svg } = H;
const { gcd, lcm } = Gen.m;

const GRADES = [['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'], ['6', 'Grade 6'], ['7', 'Grade 7']];
const SKILLS = {
  3: [['line', 'Fractions on a number line'], ['pic', 'Name the shaded fraction'], ['equiv', 'Equivalent fractions with pictures'], ['compare', 'Compare fractions with pictures']],
  4: [['equiv', 'Equivalent fractions'], ['compare', 'Compare fractions'], ['addlike', 'Add and subtract, like denominators'], ['mixed', 'Add and subtract mixed numbers'], ['mulwhole', 'Multiply a fraction by a whole number']],
  5: [['addunlike', 'Add and subtract, unlike denominators'], ['mul', 'Multiply fractions'], ['divunit', 'Divide unit fractions and whole numbers'], ['mix5', 'Mixed review']],
  6: [['div', 'Divide fractions by fractions'], ['all6', 'All four operations']],
  7: [['negas', 'Add and subtract with negatives'], ['negmd', 'Multiply and divide with negatives'], ['negall', 'All four operations with negatives']],
};
// how many problems: fewer / standard / more, by the kind of problem
const COUNTS = { line: [6, 8, 10], pic: [8, 12, 16], equiv3: [4, 6, 8], compare3: [6, 8, 10], equiv: [12, 16, 20], compare: [12, 16, 20], ops: [8, 12, 16] };
const countKey = (g, s) => g === '3' ? (s === 'equiv' ? 'equiv3' : s === 'compare' ? 'compare3' : s) : (s === 'equiv' || s === 'compare' ? s : 'ops');

/* ---------- fraction values: {n, d} with d > 0; n is the signed improper numerator ---------- */
const red = (n, d) => { if (d < 0) { n = -n; d = -d; } const g = gcd(n, d) || 1; return { n: n / g, d: d / g }; };
const calc = (op, x, y) => op === '+' ? red(x.n * y.d + y.n * x.d, x.d * y.d) : op === '−' ? red(x.n * y.d - y.n * x.d, x.d * y.d)
  : op === '×' ? red(x.n * y.n, x.d * y.d) : red(x.n * y.d, x.d * y.n);
const MINUS = '−';
// simplest form, mixed number when bigger than 1: "1 1/2", "−3/4", "2"
const atext = f => { const neg = f.n < 0, n = Math.abs(f.n), w = Math.floor(n / f.d), r = n % f.d;
  return (neg ? MINUS : '') + (r === 0 ? String(w) : w ? `${w} ${r}/${f.d}` : `${r}/${f.d}`); };
const fr = (a, b) => `<span class="gen-frac"><span>${a}</span><span>${b}</span></span>`;   // like Gen.h.frac, no escaping
const vhtml = (f, asMixed = true) => { const neg = f.n < 0, n = Math.abs(f.n), w = Math.floor(n / f.d), r = n % f.d;
  const core = f.d === 1 ? String(n) : r === 0 && asMixed ? String(w) : asMixed && w ? `${w}&#8202;${fr(r, f.d)}` : fr(n, f.d);
  return (neg ? MINUS : '') + core; };
// an operand keeps the form it was written in: o = {n, d, mx} (mx: show as a mixed number)
const otext = o => o.d === 1 ? (o.n < 0 ? MINUS : '') + Math.abs(o.n) : o.mx ? atext(o) : (o.n < 0 ? MINUS : '') + `${Math.abs(o.n)}/${o.d}`;
const ohtml = o => o.d === 1 ? (o.n < 0 ? MINUS : '') + Math.abs(o.n) : vhtml(o, !!o.mx);
const paren = (o, s) => o.n < 0 ? `(${s})` : s;
const qtext = (op, x, y) => `${otext(x)} ${op} ${paren(y, otext(y))}`;
const qhtml = (op, x, y) => `${ohtml(x)} ${op} ${paren(y, ohtml(y))}`;
const ansBox = f => `<span class="fr-box"><span class="ws-ans">${vhtml(f)}</span></span>`;
const numBlank = n => `<span class="fr-nb"><span class="ws-ans">${n}</span></span>`;

/* ---------- drawings ---------- */
const STROKE = '#222', SHADE = '#c4c4c4', KEY = '#b03020';
function bar(x, y, w, h, parts, shaded, keyShade = 0) {
  let s = '';
  for (let i = 0; i < parts; i++) {
    const px = x + i * w / parts;
    s += `<rect x="${px.toFixed(1)}" y="${y}" width="${(w / parts).toFixed(1)}" height="${h}" fill="${i < shaded ? SHADE : '#fff'}" stroke="${STROKE}" stroke-width="1.5"/>`;
    if (i < keyShade) s += `<rect class="ws-keyonly" x="${(px + 2).toFixed(1)}" y="${y + 2}" width="${(w / parts - 4).toFixed(1)}" height="${h - 4}" fill="${KEY}" fill-opacity=".35"/>`;
  }
  return s;
}
function pie(cx, cy, rad, parts, shaded) {
  let s = '';
  for (let i = 0; i < parts; i++) {
    const a0 = -Math.PI / 2 + i * 2 * Math.PI / parts, a1 = a0 + 2 * Math.PI / parts;
    const p = a => `${(cx + rad * Math.cos(a)).toFixed(1)} ${(cy + rad * Math.sin(a)).toFixed(1)}`;
    s += `<path d="M${cx} ${cy} L${p(a0)} A${rad} ${rad} 0 0 1 ${p(a1)} Z" fill="${i < shaded ? SHADE : '#fff'}" stroke="${STROKE}" stroke-width="1.5"/>`;
  }
  return s;
}
// number line from 0 to W wholes, each cut into d parts; mark = numerator k of the point (shown, or key-only to place)
function numberLine(W, d, k, mode) {
  const x0 = 22, x1 = 298, y = 34, step = (x1 - x0) / (W * d);
  let s = `<line x1="${x0 - 8}" y1="${y}" x2="${x1 + 8}" y2="${y}" stroke="${STROKE}" stroke-width="1.6"/>`;
  for (let i = 0; i <= W * d; i++) {
    const x = (x0 + i * step).toFixed(1), whole = i % d === 0;
    s += `<line x1="${x}" y1="${y - (whole ? 10 : 6)}" x2="${x}" y2="${y + (whole ? 10 : 6)}" stroke="${STROKE}" stroke-width="${whole ? 1.8 : 1.3}"/>`;
    if (whole) s += `<text x="${x}" y="${y + 26}" text-anchor="middle" font-size="15" font-weight="600">${i / d}</text>`;
  }
  const px = (x0 + k * step).toFixed(1);
  if (mode === 'name') s += `<circle cx="${px}" cy="${y}" r="5.5" fill="${STROKE}"/>`;
  else s += `<g class="ws-keyonly"><circle cx="${px}" cy="${y}" r="5.5" fill="${KEY}"/><text x="${px}" y="${y - 14}" text-anchor="middle" font-size="13" fill="${KEY}" font-weight="700">${k}/${d}</text></g>`;
  return svg(320, 66, s, mode === 'name' ? `Number line from 0 to ${W}, cut into ${d} equal parts between whole numbers, with a dot ${k} parts from 0` : `Number line from 0 to ${W}, cut into ${d} equal parts between whole numbers`);
}

/* ---------- problem makers ---------- */
const D4 = [2, 3, 4, 5, 6, 8, 10, 12], D5 = [2, 3, 4, 5, 6, 8, 9, 10, 12];
// operands are written in simplest form (2/8 + 3/8 style like-denominator problems are built separately)
const lowNum = (r, d) => { for (;;) { const n = r.int(1, d - 1); if (gcd(n, d) === 1) return n; } };
const proper = (r, ds) => { const d = r.pick(ds); return { n: lowNum(r, d), d }; };
const mixedOf = (r, ds, wlo, whi) => { const d = r.pick(ds), w = r.int(wlo, whi); return { n: w * d + lowNum(r, d), d, mx: true }; };
const bigger = (x, y) => x.n * y.d > y.n * x.d;
function makeOp(r, kind) {
  let op, x, y;
  if (kind === 'addlike') {
    const d = r.pick(D4); op = r.pick(['+', '−']); x = { n: r.int(1, d - 1), d }; y = { n: r.int(1, d - 1), d };
  } else if (kind === 'mixed') {
    const d = r.pick([2, 3, 4, 5, 6, 8, 10, 12]); op = r.pick(['+', '−']);
    x = { n: r.int(1, 6) * d + r.int(1, d - 1), d, mx: true };
    y = r.chance(.2) ? { n: r.int(1, d - 1), d } : { n: r.int(1, 4) * d + r.int(1, d - 1), d, mx: true };
  } else if (kind === 'mulwhole') {
    op = '×'; const f = proper(r, D4), w = { n: r.int(2, 10), d: 1 };
    [x, y] = r.chance(.5) ? [w, f] : [f, w];
  } else if (kind === 'addunlike') {
    op = r.pick(['+', '−']);
    const mx = r.chance(.3);
    x = mx ? mixedOf(r, D5, 1, 4) : proper(r, D5); y = mx && r.chance(.5) ? mixedOf(r, D5, 1, 3) : proper(r, D5);
    if (x.d === y.d || lcm(x.d, y.d) > 60) return null;
  } else if (kind === 'mul') {
    op = '×'; const t = r.int(1, 4);
    if (t === 1) { x = { n: r.int(2, 12), d: 1 }; y = proper(r, D5); if (r.chance(.5)) [x, y] = [y, x]; }
    else if (t === 2) { x = mixedOf(r, [2, 3, 4, 5, 6], 1, 3); y = proper(r, [2, 3, 4, 5, 6, 8]); }
    else { x = proper(r, D5.slice(0, 7)); y = proper(r, D5.slice(0, 7)); }
  } else if (kind === 'divunit') {
    op = '÷'; const u = { n: 1, d: r.int(2, 10) }, w = { n: r.int(2, 9), d: 1 };
    [x, y] = r.chance(.5) ? [u, w] : [w, u];
  } else if (kind === 'div') {
    op = '÷'; const t = r.int(1, 5);
    x = t === 1 ? mixedOf(r, [2, 3, 4, 5, 6], 1, 4) : t === 2 ? { n: r.int(2, 9), d: 1 } : proper(r, D5);
    y = t === 3 && r.chance(.5) ? mixedOf(r, [2, 3, 4], 1, 2) : proper(r, D5);
  } else if (kind === 'all6') {
    return makeOp(r, r.pick(['addunlike', 'mul', 'div', 'div']));
  } else if (kind === 'mix5') {
    return makeOp(r, r.pick(['addunlike', 'mul', 'divunit']));
  } else if (kind === 'negas' || kind === 'negmd' || kind === 'negall') {
    const ops = kind === 'negas' ? ['+', '−'] : kind === 'negmd' ? ['×', '÷'] : ['+', '−', '×', '÷'];
    op = r.pick(ops);
    const mk = () => r.chance(.25) ? mixedOf(r, [2, 3, 4, 5, 6, 8], 1, 3) : r.chance(.15) ? { n: r.int(2, 9), d: 1 } : proper(r, D5);
    x = mk(); y = mk();
    if (x.d === 1 && y.d === 1) return null;
    const sx = r.pick([1, -1, -1]), sy = sx === 1 ? -1 : r.pick([1, -1]);   // at least one negative
    x = { ...x, n: sx * x.n }; y = { ...y, n: sy * y.n };
    if ((op === '+' || op === '−') && x.d !== 1 && y.d !== 1 && lcm(x.d, y.d) > 48) return null;
  }
  if (op === '−' && !kind.startsWith('neg') && !bigger(x, y)) { if (bigger(y, x)) [x, y] = [y, x]; else return null; }
  const a = calc(op, x, y);
  if (a.n === 0 || a.d > 144) return null;
  return { op, x, y, a };
}

// the steps of one operation, as html (used in the worked example and the teacher page)
function steps(p) {
  const { op, x, y } = p, out = [qhtml(op, x, y)];
  const imp = o => ({ n: o.n, d: o.d }), anyMx = x.mx || y.mx;
  if (anyMx) out.push(qhtml(op, imp(x), imp(y)));
  let raw;
  if (op === '+' || op === '−') {
    const L = lcm(x.d, y.d), X = { n: x.n * L / x.d, d: L }, Y = { n: y.n * L / y.d, d: L };
    if (x.d !== y.d) out.push(qhtml(op, X, Y));
    raw = { n: op === '+' ? X.n + Y.n : X.n - Y.n, d: L };
  } else if (op === '×') raw = { n: x.n * y.n, d: x.d * y.d };
  else { const flip = { n: y.d * Math.sign(y.n), d: Math.abs(y.n) }; out.push(qhtml('×', imp(x), flip)); raw = { n: x.n * flip.n, d: x.d * flip.d }; }
  const rawH = fr((raw.n < 0 ? MINUS : '') + Math.abs(raw.n), raw.d), fin = vhtml(red(raw.n, raw.d));
  out.push(raw.d === 1 ? String(raw.n).replace('-', MINUS) : rawH);
  if (out[out.length - 1] !== fin) out.push(fin);
  return out.join(' = ');
}

/* ---------- stretch: one short story per grade ---------- */
const NAMES = ['Ana', 'Kai', 'Lena', 'Omar', 'Mei', 'Diego', 'Amara', 'Ravi', 'Sofia', 'Jamal', 'Yuki', 'Nia', 'Mateo', 'Priya', 'Owen', 'Zara'];
function stretch(r, g) {
  const nm = r.pick(NAMES);
  if (g === '3') {
    const d = r.pick([3, 4, 6, 8]), k = r.int(1, d - 1);
    return { q: `A ribbon is cut into ${d} equal pieces. ${nm} uses ${k} of the pieces. What fraction of the ribbon does ${nm} use?`, a: `${k}/${d}`, unit: 'of the ribbon', kind: 'name', k, d };
  }
  if (g === '4') {
    const d = r.pick([4, 5, 8, 10]), a = r.int(1, d - 1), b = r.int(1, d - 1), x = { n: a, d }, y = { n: b, d };
    return { q: `${nm} ran ${a}/${d} mile on Monday and ${b}/${d} mile on Tuesday. How far did ${nm} run in all?`, op: '+', x, y, unit: 'mile', html: `${nm} ran ${fr(a, d)} mile on Monday and ${fr(b, d)} mile on Tuesday. How far did ${nm} run in all?` };
  }
  if (g === '5') {
    const x = proper(r, [2, 3, 4]), y = proper(r, [2, 3, 4, 5]);
    return { q: `There is ${otext(x)} of a pizza left. ${nm} eats ${otext(y)} of the leftover pizza. What fraction of the whole pizza does ${nm} eat?`, op: '×', x: y, y: x, unit: 'of the pizza',
      html: `There is ${ohtml(x)} of a pizza left. ${nm} eats ${ohtml(y)} of the leftover pizza. What fraction of the whole pizza does ${nm} eat?` };
  }
  if (g === '6') {
    const y = proper(r, [2, 3, 4, 5, 8]), k = r.int(3, 12), x = red(y.n * k, y.d), xo = { ...x, mx: x.d > 1 && x.n > x.d };
    return { q: `${nm} has ${otext(xo)} pounds of trail mix and fills bags that each hold ${otext(y)} pound. How many bags can ${nm} fill?`, op: '÷', x: xo, y, unit: 'bags',
      html: `${nm} has ${ohtml(xo)} pounds of trail mix and fills bags that each hold ${ohtml(y)} pound. How many bags can ${nm} fill?` };
  }
  const y = proper(r, [2, 3, 4, 5]), k = r.int(3, 9), x = { n: -y.n, d: y.d };
  return { q: `A diver goes down ${otext(y)} meter each minute for ${k} minutes. Write the diver's change in depth as a fraction or mixed number (down is negative).`, op: '×', x, y: { n: k, d: 1 }, unit: 'meters',
    html: `A diver goes down ${ohtml(y)} meter each minute for ${k} minutes. Write the change in depth as a number (down is negative).` };
}

/* ---------- the generator ---------- */
Gen.add('fractions', {
  title: 'Fractions', type: 'Practice',
  css: `.fr-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px 28px;margin:6px 0 10px}
.fr-cell{display:flex;gap:8px;align-items:center;min-height:.78in;font-size:19px;break-inside:avoid}
.fr-tight .fr-cell{min-height:.56in}
.fr-cell .ws-num{font-size:15px;min-width:1.6em}
.fr-box{display:inline-grid;place-items:center;min-width:3.4em;min-height:2.3em;border:1.5px solid #444;border-radius:5px;vertical-align:middle;margin-left:4px}
.fr-nb{display:inline-block;min-width:1.7em;min-height:1.05em;border-bottom:1.5px solid #222;text-align:center}
.fr-pics{display:grid;grid-template-columns:repeat(4,1fr);gap:10px 14px;margin:6px 0}
.fr-pic{text-align:center;border:1px solid #bbb;border-radius:8px;padding:6px 4px;break-inside:avoid}
.fr-pic svg{max-width:1.3in;margin:0 auto 4px}
.fr-wide{display:grid;grid-template-columns:1fr 1fr;gap:10px 24px;margin:6px 0}
.fr-wide > div{break-inside:avoid}
.fr-wide p{margin:0;font-size:17px}
.fr-circle{display:inline-grid;place-items:center;width:1.7em;height:1.7em;border:1.5px solid #222;border-radius:50%;margin:0 6px;vertical-align:middle}
.fr-story{display:flex;gap:10px;align-items:flex-end;justify-content:space-between}
.fr-story p{margin:0;flex:1}
.fr-steps{margin:4px 0;padding-left:1.8em;font-size:15px}
.fr-steps li{margin-bottom:6px}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '4' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => SKILLS[v.grade], def: 'equiv' },
    { id: 'count', label: 'Problems', type: 'select', def: 'm',
      options: v => { const c = COUNTS[countKey(v.grade, v.skill)]; return [['s', `Fewer (${c[0]})`], ['m', `Standard (${c[1]})`], ['l', `More (${c[2]})`]]; } },
  ],
  make(v, r) {
    const g = v.grade, skill = v.skill, ck = countKey(g, skill), n = COUNTS[ck][{ s: 0, m: 1, l: 2 }[v.count]];
    const label = SKILLS[g].find(s => s[0] === skill)[1], gname = GRADES.find(x => x[0] === g)[1];
    const parts = [], items = [];
    let directions, ican, mistakes, notes, teacher = '', exHtml;

    if (g === '3' && skill === 'line') {
      const mk = () => { const W = r.chance(.3) ? 2 : 1, d = r.pick([2, 3, 4, 6, 8]), k = r.int(1, W * d - 1); if (k % d === 0) return null;
        return { W, d, k, mode: r.chance(.5) ? 'name' : 'place' }; };
      const ps = r.distinct(n + 1, mk, p => `${p.W}:${p.d}:${p.k}`), ex = ps.pop();
      exHtml = example(`${numberLine(ex.W, ex.d, ex.k, 'name')}`, `Each whole is cut into ${ex.d} equal parts, so each part is 1/${ex.d}. The dot is ${ex.k} parts from 0, so it shows <b>${ex.k}/${ex.d}</b>.`);
      parts.push(part('', exHtml));
      const cells = ps.map((p, i) => { const a = `${p.k}/${p.d}`;
        items.push({ q: `${p.mode} ${p.k}/${p.d} on 0-${p.W}`, a, kind: 'line', W: p.W, d: p.d, k: p.k });
        return `<div><p><span class="ws-num">${i + 1}.</span> ${p.mode === 'name' ? `What fraction does the dot show? <span class="fr-box"><span class="ws-ans">${fr(p.k, p.d)}</span></span>` : `Draw a dot at ${fr(p.k, p.d)}. Label it.`}</p>${numberLine(p.W, p.d, p.k, p.mode)}</div>`; });
      parts.push(part('Practice', `<div class="fr-wide">${cells.join('')}</div>`));
      directions = 'Some lines have a dot: write the fraction it shows. Some lines ask you to draw a dot: put it in the right place and label it.';
      ican = 'I can show and name fractions on a number line.';
      mistakes = 'Counting the tick marks instead of the spaces between them, and starting the count at 1 instead of 0. On lines that go to 2, some students restart the count at 1.';
    } else if (g === '3' && skill === 'pic') {
      const mk = () => { const d = r.pick([2, 3, 4, 6, 8]); return { shape: r.pick(['bar', 'circle']), d, k: r.int(1, d) }; };
      const ps = r.distinct(n + 1, mk, p => `${p.shape}${p.d}:${p.k}`), ex = ps.pop();
      const draw = p => p.shape === 'bar' ? svg(130, 90, bar(5, 22, 120, 46, p.d, p.k), `A bar cut into ${p.d} equal parts with ${p.k} shaded`)
        : svg(90, 90, pie(45, 45, 40, p.d, p.k), `A circle cut into ${p.d} equal parts with ${p.k} shaded`);
      exHtml = example(`<span style="display:inline-block;width:1.2in;vertical-align:middle">${draw(ex)}</span> ${ex.d} equal parts, ${ex.k} shaded: <b>${ex.k}/${ex.d}</b>`, 'The bottom number counts all the equal parts. The top number counts the shaded parts.');
      parts.push(part('', exHtml));
      parts.push(part('Practice', `<div class="fr-pics">${ps.map((p, i) => { const a = `${p.k}/${p.d}`;
        items.push({ q: `${p.shape} ${p.k} of ${p.d}`, a, kind: 'pic', d: p.d, k: p.k });
        return `<div class="fr-pic"><p style="text-align:left;margin:0"><span class="ws-num">${i + 1}.</span></p>${draw(p)}<span class="fr-box"><span class="ws-ans">${fr(p.k, p.d)}</span></span></div>`; }).join('')}</div>`));
      directions = 'Write the fraction of each shape that is shaded in the box under it.';
      ican = 'I can name the fraction of a shape that is shaded.';
      mistakes = 'Writing shaded over unshaded (3/5 for 3 shaded and 2 not) instead of shaded over all the parts. A shape with every part shaded is a whole, like 4/4.';
    } else if (g === '3' && skill === 'equiv') {
      const PAIRS = [[2, 4], [2, 6], [2, 8], [3, 6], [4, 8], [4, 2], [6, 3], [8, 4], [8, 2], [6, 2]];
      const mk = () => { const [b, c] = r.pick(PAIRS), a = r.int(1, b - 1), m = a * c / b; return Number.isInteger(m) ? { b, a, c, m } : null; };
      const ps = r.distinct(n + 1, mk, p => `${p.a}/${p.b}=${p.c}`), ex = ps.pop();
      const draw = (p, keyOnly) => svg(300, 70, bar(10, 3, 280, 30, p.b, p.a) + bar(10, 38, 280, 30, p.c, keyOnly ? 0 : p.m, keyOnly ? p.m : 0), `Two bars the same size: the top is cut into ${p.b} parts with ${p.a} shaded; the bottom is cut into ${p.c} parts`);
      exHtml = example(draw(ex, false), `${fr(ex.a, ex.b)} = ${fr(`<b>${ex.m}</b>`, ex.c)}. The same amount is shaded in both bars, so the fractions are equal.`);
      parts.push(part('', exHtml));
      parts.push(part('Practice', `<div class="fr-wide">${ps.map((p, i) => {
        items.push({ q: `${p.a}/${p.b} = ?/${p.c}`, a: String(p.m), kind: 'eq3', L: { n: p.a, d: p.b }, c: p.c, miss: 'top' });
        return `<div><p><span class="ws-num">${i + 1}.</span> ${fr(p.a, p.b)} = ${fr(numBlank(p.m), p.c)}</p>${draw(p, true)}</div>`; }).join('')}</div>`));
      directions = 'Shade the bottom bar to match the top bar. Then write the missing top number.';
      ican = 'I can use pictures to find equivalent fractions.';
      mistakes = 'Shading the same number of parts instead of the same amount of the bar. Check that both shaded parts end at the same place.';
    } else if (g === '3' && skill === 'compare') {
      const mk = () => { if (r.chance(.5)) { const d = r.pick([2, 3, 4, 6, 8]); const a = r.int(1, d - 1), b = r.int(1, d - 1); if (a === b && r.chance(.7)) return null; return { x: { n: a, d }, y: { n: b, d } }; }
        const nn = r.int(1, 3), ds = r.sample([2, 3, 4, 6, 8].filter(d => d > nn), 2); if (ds.length < 2) return null; return { x: { n: nn, d: ds[0] }, y: { n: nn, d: ds[1] } }; };
      const ps = r.distinct(n + 1, mk, p => `${p.x.n}/${p.x.d}?${p.y.n}/${p.y.d}`), ex = ps.pop();
      const sym = p => { const L = p.x.n * p.y.d, R = p.y.n * p.x.d; return L > R ? '>' : L < R ? '<' : '='; };
      const draw = p => svg(300, 58, bar(10, 3, 280, 24, p.x.d, p.x.n) + bar(10, 32, 280, 24, p.y.d, p.y.n), `Two bars the same size: ${p.x.n} of ${p.x.d} parts shaded, and ${p.y.n} of ${p.y.d} parts shaded`);
      exHtml = example(draw(ex), `${fr(ex.x.n, ex.x.d)} <b>${H.esc(sym(ex))}</b> ${fr(ex.y.n, ex.y.d)}. Both bars are the same size, so compare how much of each is shaded.`);
      parts.push(part('', exHtml));
      parts.push(part('Practice', `<div class="fr-wide">${ps.map((p, i) => { const s = sym(p);
        items.push({ q: `${p.x.n}/${p.x.d} ? ${p.y.n}/${p.y.d}`, a: s, kind: 'cmp', x: p.x, y: p.y });
        return `<div><p><span class="ws-num">${i + 1}.</span> ${fr(p.x.n, p.x.d)}<span class="fr-circle"><span class="ws-ans">${H.esc(s)}</span></span>${fr(p.y.n, p.y.d)}</p>${draw(p)}</div>`; }).join('')}</div>`));
      directions = 'Look at the shaded parts. Write &lt;, &gt; or = in each circle.';
      ican = 'I can compare fractions that have the same top number or the same bottom number.';
      mistakes = 'Thinking a bigger bottom number means a bigger fraction. With the same top number, more parts means smaller parts, so 1/8 &lt; 1/4.';
    } else if (skill === 'compare') {
      const mk = () => { if (r.chance(.2)) { const b = r.pick([2, 3, 4, 5, 6]), a = r.int(1, b - 1), k = r.int(2, Math.floor(12 / b)); if (k < 2) return null; return r.chance(.5) ? { x: { n: a, d: b }, y: { n: a * k, d: b * k } } : { x: { n: a * k, d: b * k }, y: { n: a, d: b } }; }
        const x = proper(r, D4), y = proper(r, D4); return x.d === y.d ? null : { x, y }; };
      const ps = r.distinct(n + 1, mk, p => `${p.x.n}/${p.x.d}?${p.y.n}/${p.y.d}`), ex = ps.pop();
      const sym = p => { const L = p.x.n * p.y.d, R = p.y.n * p.x.d; return L > R ? '>' : L < R ? '<' : '='; };
      const L = lcm(ex.x.d, ex.y.d);
      exHtml = example(`${fr(ex.x.n, ex.x.d)} <b>${H.esc(sym(ex))}</b> ${fr(ex.y.n, ex.y.d)}`, `Rename both with the same denominator: ${fr(ex.x.n, ex.x.d)} = ${fr(ex.x.n * L / ex.x.d, L)} and ${fr(ex.y.n, ex.y.d)} = ${fr(ex.y.n * L / ex.y.d, L)}. Now compare the numerators.`);
      parts.push(part('', exHtml));
      parts.push(part('Practice', `<div class="fr-grid fr-tight">${ps.map((p, i) => { const s = sym(p);
        items.push({ q: `${p.x.n}/${p.x.d} ? ${p.y.n}/${p.y.d}`, a: s, kind: 'cmp', x: p.x, y: p.y });
        return `<div class="fr-cell"><span class="ws-num">${i + 1}.</span> ${fr(p.x.n, p.x.d)}<span class="fr-circle"><span class="ws-ans">${H.esc(s)}</span></span>${fr(p.y.n, p.y.d)}</div>`; }).join('')}</div>`));
      directions = 'Write &lt;, &gt; or = in each circle. Use a common denominator, a benchmark like 1/2, or a picture.';
      ican = 'I can compare two fractions with different denominators.';
      mistakes = 'Comparing only the numerators or only the denominators. Benchmarks help: 3/8 is less than 1/2 and 4/6 is more than 1/2.';
    } else if (skill === 'equiv') {
      const mk = () => { const t = r.int(1, 4);
        if (t === 4) { const a = r.int(1, 9); return { t: 'hund', a, b: 10, c: 100, m: a * 10 }; }
        const b = r.pick([2, 3, 4, 5, 6]), a = r.int(1, b - 1), k = r.int(2, 6);
        if (t === 1) return { t: 'num', a, b, c: b * k, m: a * k };
        if (t === 2) return { t: 'den', a, b, c: a * k, m: b * k };
        return gcd(a, b) === 1 ? { t: 'simp', a: a * k, b: b * k, sa: a, sb: b } : null; };
      const ps = r.distinct(n + 1, mk, p => JSON.stringify(p)), ex = { a: 2, b: 3, k: 4 };
      exHtml = example(`${fr(2, 3)} = ${fr(`<b>8</b>`, 12)}: 3 × 4 = 12, so multiply the top by 4 too: 2 × 4 = 8.`, `${fr(6, 8)} in simplest form: divide the top and bottom by 2 to get <b>${fr(3, 4)}</b>.`);
      void ex;
      parts.push(part('', exHtml));
      parts.push(part('Practice', `<div class="fr-grid fr-tight">${ps.map((p, i) => { let body, a, q;
        if (p.t === 'simp') { a = `${p.sa}/${p.sb}`; q = `simplest ${p.a}/${p.b}`; body = `${fr(p.a, p.b)} = ${ansBox({ n: p.sa, d: p.sb })} <small>(simplest form)</small>`; }
        else if (p.t === 'den') { a = String(p.m); q = `${p.a}/${p.b} = ${p.c}/?`; body = `${fr(p.a, p.b)} = ${fr(p.c, numBlank(p.m))}`; }
        else { a = String(p.m); q = `${p.a}/${p.b} = ?/${p.c}`; body = `${fr(p.a, p.b)} = ${fr(numBlank(p.m), p.c)}`; }
        items.push({ q, a, kind: 'eq4', t: p.t, L: { n: p.a, d: p.b }, c: p.c, miss: p.t === 'den' ? 'bottom' : 'top' });
        return `<div class="fr-cell"><span class="ws-num">${i + 1}.</span> ${body}</div>`; }).join('')}</div>`));
      directions = 'Write the missing number to make the fractions equal. When it says simplest form, write the fraction in the box using the smallest numbers you can.';
      ican = 'I can find equivalent fractions and write a fraction in simplest form.';
      mistakes = 'Adding the same number to the top and bottom (2/3 = 4/5) instead of multiplying. In simplest form, dividing by a common factor that is not the greatest one and stopping too soon.';
    } else {
      // operations
      const kind = skill;
      const ps = r.distinct(n + 1, () => makeOp(r, kind), p => qtext(p.op, p.x, p.y)), ex = ps.pop();
      exHtml = example(steps(ex), {
        addlike: 'Same denominators: add or subtract the numerators and keep the denominator. Then simplify.',
        mixed: 'Add or subtract the whole numbers and the fractions, or change both to fractions greater than 1 first. Regroup a whole when the fraction part is too small.',
        mulwhole: 'Multiply the whole number by the numerator. Keep the denominator. Then simplify.',
        addunlike: 'Find a common denominator, rename both fractions, then add or subtract the numerators. Simplify the answer.',
        mul: 'Multiply the numerators, multiply the denominators, then simplify. Write a whole number as a fraction over 1.',
        divunit: 'Dividing by a number is multiplying by its reciprocal: ÷ 3 is × 1/3, and ÷ 1/3 is × 3.',
        mix5: 'Read each sign first. Add and subtract with a common denominator; multiply straight across; divide by multiplying by the reciprocal.',
        div: 'Keep the first fraction, change ÷ to ×, and flip the second fraction. Then multiply and simplify.',
        all6: 'Read each sign first. Change mixed numbers to fractions greater than 1 before you multiply or divide.',
        negas: 'Use a common denominator. Then add or subtract the numerators using integer rules.',
        negmd: 'Work out the fraction, then the sign: same signs give a positive answer, different signs give a negative answer.',
        negall: 'Do the fraction work, then use integer rules for the sign.',
      }[kind]);
      parts.push(part('', exHtml));
      parts.push(part('Practice', `<div class="fr-grid">${ps.map((p, i) => {
        items.push({ q: qtext(p.op, p.x, p.y), a: atext(p.a), kind: 'op', op: p.op, x: p.x, y: p.y });
        return `<div class="fr-cell"><span class="ws-num">${i + 1}.</span> ${qhtml(p.op, p.x, p.y)} = ${ansBox(p.a)}</div>`; }).join('')}</div>`));
      teacher = `<h3>Worked solutions</h3><ol class="fr-steps">${ps.map(p => `<li>${steps(p)}</li>`).join('')}</ol>`;
      directions = 'Solve each problem. Write the answer in the box in simplest form.' + (kind === 'divunit' ? '' : ' Write an answer greater than 1 as a mixed number.') + (g === '7' ? ' Remember the sign.' : '');
      ican = { addlike: 'I can add and subtract fractions with like denominators.', mixed: 'I can add and subtract mixed numbers with like denominators.',
        mulwhole: 'I can multiply a fraction by a whole number.', addunlike: 'I can add and subtract fractions with unlike denominators.', mul: 'I can multiply fractions and mixed numbers.',
        divunit: 'I can divide a unit fraction by a whole number and a whole number by a unit fraction.', mix5: 'I can add, subtract, multiply and divide with fractions.',
        div: 'I can divide fractions by fractions.', all6: 'I can use all four operations with fractions and mixed numbers.',
        negas: 'I can add and subtract positive and negative fractions.', negmd: 'I can multiply and divide positive and negative fractions.', negall: 'I can use all four operations with positive and negative fractions.' }[kind];
      mistakes = { addlike: 'Adding the denominators too (1/4 + 2/4 = 3/8). An answer like 6/4 should become 1 1/2.',
        mixed: 'Subtracting the smaller fraction from the bigger one when the bigger one is on the bottom, instead of regrouping a whole.',
        mulwhole: 'Multiplying the denominator by the whole number as well, which gives the same fraction back.',
        addunlike: 'Adding the numerators and the denominators (1/2 + 1/3 = 2/5). Renaming only one fraction.',
        mul: 'Finding a common denominator first (not needed), and forgetting to change mixed numbers to fractions before multiplying.',
        divunit: 'Expecting division to make the answer smaller: 4 ÷ 1/3 = 12 because there are 12 thirds in 4.',
        mix5: 'Using the rule for one operation on another, like flipping a fraction when multiplying.',
        div: 'Flipping the first fraction instead of the second, or flipping a mixed number before changing it to a fraction.',
        all6: 'Multiplying mixed numbers part by part (1 1/2 × 2 1/3 is not 2 1/6).',
        negas: 'Losing the sign when renaming, and treating subtracting a negative as subtracting.',
        negmd: 'Getting the size right but the sign wrong. Count the negative signs.',
        negall: 'Mixing the sign rules: two negatives make a positive only for multiplying and dividing.' }[kind];
    }

    // stretch
    const st = stretch(r, g);
    if (st.kind === 'name') items.push({ q: st.q, a: st.a, kind: 'story3', k: st.k, d: st.d });
    else { const a = calc(st.op, st.x, st.y); st.a = atext(a); items.push({ q: st.q, a: st.a, kind: 'op', op: st.op, x: st.x, y: st.y }); }
    const sbox = st.kind === 'name' ? ansBox({ n: st.k, d: st.d }).replace(vhtml({ n: st.k, d: st.d }), fr(st.k, st.d)) : ansBox(calc(st.op, st.x, st.y));
    parts.push(part('Stretch', `<div class="fr-story"><p>${st.html || H.esc(st.q)}</p><span>${sbox} ${st.unit}</span></div>`));
    if (teacher && st.op) teacher = teacher.replace('</ol>', `<li>Stretch: ${steps({ op: st.op, x: st.x, y: st.y })}</li></ol>`);

    return {
      title: `${label}: ${gname}`, level: gname, ican, directions,
      minutes: n > 12 ? 25 : 20, materials: 'pencil' + (g === '3' ? ', crayon or colored pencil for shading' : ''),
      parts, items, mistakes, teacher,
      notes: notes || (g === '3' ? 'Pictures and number lines come before symbols at this grade (3.NF). Fold paper strips to check a tricky one. Press New sheet for another set at the same level.'
        : 'Answers are in simplest form' + (skill === 'equiv' || skill === 'compare' ? '' : ', with mixed numbers for answers greater than 1') + '. The teacher page lists the steps for each problem where steps help. Press New sheet for another set at the same level.'),
    };
  },
  verify(s) {
    const out = [];
    const parse = t => { t = String(t).replace(/−/g, '-').trim();
      let m = t.match(/^(-?)(\d+) (\d+)\/(\d+)$/); if (m) { const d = +m[4]; return { n: (m[1] ? -1 : 1) * (+m[2] * d + +m[3]), d, w: +m[2], r: +m[3] }; }
      m = t.match(/^(-?)(\d+)\/(\d+)$/); if (m) return { n: (m[1] ? -1 : 1) * +m[2], d: +m[3], w: 0, r: +m[2] };
      m = t.match(/^(-?)(\d+)$/); if (m) return { n: (m[1] ? -1 : 1) * +m[2], d: 1, w: +m[2], r: 0 };
      return null; };
    for (const it of s.items) {
      if (it.kind === 'op') {
        const { x, y } = it; let N, D;   // the exact answer by cross multiplying, worked out here on its own
        if (it.op === '+') { N = x.n * y.d + y.n * x.d; D = x.d * y.d; }
        else if (it.op === '−') { N = x.n * y.d - y.n * x.d; D = x.d * y.d; }
        else if (it.op === '×') { N = x.n * y.n; D = x.d * y.d; }
        else { N = x.n * y.d; D = x.d * y.n; }
        const p = parse(it.a);
        if (!p) { out.push(`${it.q}: cannot read answer ${it.a}`); continue; }
        if (p.n * D !== N * p.d) out.push(`${it.q}: key says ${it.a}, should be ${N}/${D}`);
        if (p.d > 1 && (p.r >= p.d || gcd(p.r, p.d) !== 1)) out.push(`${it.q}: ${it.a} is not in simplest mixed form`);
        if (x.n >= 0 && y.n >= 0 && N < 0) out.push(`${it.q}: negative answer from positive numbers`);
      } else if (it.kind === 'cmp') {
        const L = it.x.n * it.y.d, R = it.y.n * it.x.d, want = L > R ? '>' : L < R ? '<' : '=';
        if (it.a !== want) out.push(`${it.q}: key says ${it.a}, should be ${want}`);
      } else if (it.kind === 'line' || it.kind === 'pic' || it.kind === 'story3') {
        const p = parse(it.a);
        if (!p || p.n !== it.k || p.d !== it.d) out.push(`${it.q}: key says ${it.a}`);
        if (it.kind === 'line' && (it.k <= 0 || it.k >= it.W * it.d)) out.push(`${it.q}: point off the line`);
        if (it.kind === 'pic' && it.k > it.d) out.push(`${it.q}: more shaded than parts`);
      } else if (it.kind === 'eq3' || (it.kind === 'eq4' && it.t !== 'simp')) {
        // left fraction L.n/L.d equals top/bottom, with the missing number filled in from the key
        const m = +it.a, top = it.miss === 'bottom' ? it.c : m, bottom = it.miss === 'bottom' ? m : it.c;
        if (!(Number.isInteger(m) && m > 0)) out.push(`${it.q}: answer ${it.a} is not a whole number`);
        else if (it.L.n * bottom !== top * it.L.d) out.push(`${it.q}: ${it.L.n}/${it.L.d} is not ${top}/${bottom}`);
      } else if (it.kind === 'eq4' && it.t === 'simp') {
        const p = parse(it.a);
        if (!p || gcd(p.n, p.d) !== 1 || p.n * it.L.d !== it.L.n * p.d) out.push(`${it.q}: key says ${it.a}`);
      }
    }
    return out;
  },
});
})();
