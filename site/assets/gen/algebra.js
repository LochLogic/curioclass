// Algebra and Functions generator, grade 8 through precalculus: the high school layer above the Expressions and
// Equations generator (equations.js keeps grades 6-9 one-step to multi-step equations, inequalities and expressions).
// Grade 8: slope from graphs and points (8.EE.6, 8.F.4), equations of lines (8.F.4), square and cube root equations
// (8.EE.2), square roots squeezed on a number line (8.NS.2), exponent rules (8.EE.1), systems by graphing and in
// stories (8.EE.8), function or not (8.F.1).
// Algebra 1: forms of a line (A-CED.2, F-LE.2, G-GPE.5), compound and literal inequalities (A-REI.3, A-CED.4), systems
// by graphing, substitution and elimination, in stories, and systems of inequalities (A-REI.5-6, A-REI.12, A-CED.3),
// function notation (F-IF.1-2), average rate of change (F-IF.6), linear or exponential tables (F-LE.1-2), multiplying
// polynomials with area models (A-APR.1), factoring task cards (A-SSE.2), quadratics by factoring, square roots,
// completing the square and the formula with the discriminant (A-REI.4), factored and vertex form (A-SSE.3, F-IF.8a),
// projectile motion (A-CED.1, F-IF.4).
// Geometry: circle equations by completing the square (G-GPE.1).
// Algebra 2: complex numbers (N-CN.1-2, N-CN.7), remainder theorem (A-APR.2), rational expressions and equations with
// extraneous solutions (A-APR.6-7, A-REI.2), logarithms and exponential equations (F-LE.4, F-BF.5), growth and decay
// (F-LE.5, A-SSE.3c), combining and inverting functions (F-BF.1b-c, F-BF.4a), sequences and series (F-IF.3, F-BF.2,
// F-LE.2, A-SSE.4).
// Precalculus: composition and decomposition (F-BF.1c), inverses with restricted domains (F-BF.4d), rational functions
// (F-IF.7d), 2 by 2 matrices and systems (N-VM.10, N-VM.12, A-REI.9), conics in standard form (G-GPE.1, G-GPE.3).
// Every answer is exact and simplified (fractions in lowest terms, radicals simplified). verify() reads each printed
// answer back with its own small parser and substitutes it into the problem, so the key is checked as it prints.
(() => {
const { part, example, esc } = Gen.h;
const { gcd } = Gen.m;

/* ---------- writing math as text: one string serves the key, the checker and the page ---------- */
const MIN = '−', SUPD = '⁰¹²³⁴⁵⁶⁷⁸⁹', SUBD = '₀₁₂₃₄₅₆₇₈₉';
const sup = n => String(n).replace(/-/g, '⁻').replace(/\d/g, c => SUPD[c]);
const sub = n => String(n).replace(/\d/g, c => SUBD[c]);
const num = n => (n < 0 ? MIN : '') + Math.abs(n);
const nz = (r, lo, hi) => { for (;;) { const x = r.int(lo, hi); if (x) return x; } };
const Q = (n, d = 1) => { if (d < 0) { n = -n; d = -d; } const g = gcd(n, d) || 1; return { n: n / g, d: d / g }; };
const toQ = c => typeof c === 'number' ? Q(c) : c;
const qT = q => { q = toQ(q); return q.d === 1 ? num(q.n) : `${q.n < 0 ? MIN : ''}${Math.abs(q.n)}/${q.d}`; };
const qv = q => q.n / q.d;
// a term's size with its monomial: 3x, x, (2/3)x, 5
const termT = (c, m) => { const a = Q(Math.abs(c.n), c.d); if (!m) return qT(a); if (a.n === 1 && a.d === 1) return m; return a.d === 1 ? a.n + m : `(${qT(a)})${m}`; };
// a signed sum of [coefficient, monomial] terms, zeros dropped: 3x² − x + 5
const sum = ts => { const t = ts.map(([c, m]) => [toQ(c), m]).filter(([c]) => c.n); if (!t.length) return '0';
  return t.map(([c, m], i) => (i ? (c.n < 0 ? ` ${MIN} ` : ' + ') : (c.n < 0 ? MIN : '')) + termT(c, m)).join(''); };
const mono = (v, p) => p === 0 ? '' : p === 1 ? v : v + sup(p);
const poly = (cs, v = 'x') => sum(cs.map((c, p) => [c, mono(v, p)]).reverse());   // cs[p] = coefficient of v^p
const pmul = (a, b) => { const o = Array(a.length + b.length - 1).fill(0); a.forEach((x, i) => b.forEach((y, j) => { o[i + j] += x * y; })); return o; };
const padd = (a, b) => Array.from({ length: Math.max(a.length, b.length) }, (_, i) => (a[i] || 0) + (b[i] || 0));
const pscale = (a, k) => a.map(x => x * k);
const pval = (cs, x) => cs.reduce((s, c, p) => s + c * x ** p, 0);
const deg = cs => { let d = cs.length - 1; while (d > 0 && !cs[d]) d--; return d; };
const lin = (a, b, v = 'x') => sum([[a, v], [b, '']]);
// x − 3, x + 2, x: the factor (x − p)
const fac = (p, v = 'x') => p === 0 ? v : `${v} ${p < 0 ? '+' : MIN} ${Math.abs(p)}`;
const pt = (x, y) => `(${qT(x)}, ${qT(y)})`;
// √n simplified: [outside, inside]
const rootSplit = n => { let o = 1, i = n; for (let f = 2; f * f <= i; f++) while (i % (f * f) === 0) { i /= f * f; o *= f; } return [o, i]; };
const isSq = n => n >= 0 && Math.round(Math.sqrt(n)) ** 2 === n;
const radT = n => { const [o, i] = rootSplit(n); return i === 1 ? String(o) : (o === 1 ? '' : o) + '√' + i; };
const money = x => '$' + comma(Math.round(x));
const cents = x => '$' + x.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
const comma = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
// math text to html: escaped, single-letter variables in italics
const ital = s => s.replace(/(^|[^a-zA-Z&#;])([a-z])(?![a-zA-Z;])/g, '$1<i>$2</i>');
const F = s => ital(esc(s));
const ab = (t, em) => `<span class="ws-blank" style="min-width:${(em || Math.max(3, Math.min(16, 0.55 * String(t).length + 1.5))).toFixed(1)}em"><span class="ws-ans">${F(t)}</span></span>`;
const keyp = t => `<p class="ws-keyonly">${t}</p>`;

/* ---------- roots of ax² + bx + c = 0 as simplified exact text ---------- */
function quadText(a, b, c, complex) {
  const D = b * b - 4 * a * c;
  if (D < 0 && !complex) return 'no real solutions';
  if (D >= 0 && isSq(D)) {
    const s = Math.sqrt(D), r1 = Q(-b - s, 2 * a), r2 = Q(-b + s, 2 * a);
    if (D === 0) return `x = ${qT(r1)}`;
    const [p, q] = qv(r1) < qv(r2) ? [r1, r2] : [r2, r1];
    return `x = ${qT(p)}, x = ${qT(q)}`;
  }
  const [k, m] = rootSplit(Math.abs(D));
  const g = gcd(gcd(b, k), 2 * a);
  let bb = -b / g, dd = 2 * a / g; const kk = k / g;
  if (dd < 0) { bb = -bb; dd = -dd; }
  const rad = D < 0 ? (kk === 1 ? '' : kk) + 'i' + (m === 1 ? '' : '√' + m) : (kk === 1 ? '' : kk) + '√' + m;
  if (!bb) return dd === 1 ? `x = ±${rad}` : `x = ±${rad}/${dd}`;
  return dd === 1 ? `x = ${num(bb)} ± ${rad}` : `x = (${num(bb)} ± ${rad})/${dd}`;
}

/* ---------- a small reader for the printed math, used by verify(): complex values, ± gives two ---------- */
const SUPMAP = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁺': '+', '⁻': '-', '⁽': '(', '⁾': ')', 'ˣ': 'x', 'ⁿ': 'n', 'ᵗ': 't', 'ᵏ': 'k' };
const SUBMAP = { '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9', 'ₙ': 'n', '₋': '-' };
const C = {
  add: (a, b) => [a[0] + b[0], a[1] + b[1]], sub: (a, b) => [a[0] - b[0], a[1] - b[1]],
  mul: (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]],
  div: (a, b) => { const d = b[0] * b[0] + b[1] * b[1]; if (d < 1e-20) throw new Error('divide by zero'); return [(a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d]; },
  pow: (a, e) => { const p = e[0];
    if (Number.isInteger(p)) { let o = [1, 0], b = a, k = Math.abs(p); while (k) { if (k & 1) o = C.mul(o, b); b = C.mul(b, b); k = Math.floor(k / 2); } return p < 0 ? C.div([1, 0], o) : o; }
    if (Math.abs(a[1]) < 1e-12 && a[0] >= 0) return [a[0] ** p, 0];
    const rr = Math.hypot(a[0], a[1]) ** p, t = Math.atan2(a[1], a[0]) * p; return [rr * Math.cos(t), rr * Math.sin(t)]; },
  sqrt: a => { if (Math.abs(a[1]) < 1e-12) return a[0] >= 0 ? [Math.sqrt(a[0]), 0] : [0, Math.sqrt(-a[0])]; return C.pow(a, [0.5, 0]); },
};
function ev(src, env = {}) {
  const s = String(src).replace(/−/g, '-').replace(/[·×]/g, '*').replace(/÷/g, '/');
  const toks = [];
  for (let i = 0; i < s.length;) {
    const c = s[i];
    if (/\s/.test(c)) { i++; continue; }
    if (SUPMAP[c] != null) { let t = ''; while (i < s.length && SUPMAP[s[i]] != null) t += SUPMAP[s[i++]]; toks.push({ k: 'sup', v: t }); continue; }
    if (/[\d.]/.test(c)) { let t = ''; while (i < s.length && /[\d.]/.test(s[i])) t += s[i++]; toks.push({ k: 'num', v: +t }); continue; }
    if (s.startsWith('ln', i)) { toks.push({ k: 'fn', v: 'ln' }); i += 2; continue; }
    if (s.startsWith('log', i)) { i += 3; let b = ''; while (i < s.length && SUBD.includes(s[i])) b += SUBD.indexOf(s[i++]); toks.push({ k: 'fn', v: 'log', b: b ? +b : 10 }); continue; }
    if (c === '√' || c === '∛') { toks.push({ k: 'fn', v: c }); i++; continue; }
    if (/[a-zA-Zπ]/.test(c)) { let t = c; i++; while (i < s.length && SUBMAP[s[i]] != null) t += SUBMAP[s[i++]]; toks.push({ k: 'id', v: t }); continue; }
    if ('+-*/^()±'.includes(c)) { toks.push({ k: c }); i++; continue; }
    throw new Error(`cannot read "${c}" in ${src}`);
  }
  let p = 0;
  const peek = () => toks[p], neg = a => [-a[0], -a[1]];
  const lift = (A, B, f) => { const o = []; for (const a of A) for (const b of B) o.push(f(a, b)); return o; };
  const starts = t => t && (t.k === 'num' || t.k === 'id' || t.k === 'fn' || t.k === '(');
  function expr() {
    let sg = null; if (peek() && '+-±'.includes(peek().k)) sg = toks[p++].k;
    let a = term(); if (sg === '-') a = a.map(neg); if (sg === '±') a = [...a, ...a.map(neg)];
    while (peek() && '+-±'.includes(peek().k)) { const op = toks[p++].k, b = term();
      a = op === '+' ? lift(a, b, C.add) : op === '-' ? lift(a, b, C.sub) : [...lift(a, b, C.add), ...lift(a, b, C.sub)]; }
    return a;
  }
  function term() {
    let a = factor();
    for (;;) { const t = peek();
      if (t && (t.k === '*' || t.k === '/')) { p++; const b = factor(); a = lift(a, b, t.k === '*' ? C.mul : C.div); }
      else if (starts(t)) a = lift(a, factor(), C.mul); else return a; }
  }
  function factor() {
    let a = atom();
    for (;;) { const t = peek();
      if (t && t.k === 'sup') { p++; a = lift(a, ev(t.v, env), C.pow); }
      else if (t && t.k === '^') { p++; let sg = 1; if (peek() && peek().k === '-') { p++; sg = -1; } const e = atom(); a = lift(a, sg < 0 ? e.map(neg) : e, C.pow); }
      else return a; }
  }
  function atom() {
    const t = toks[p++]; if (!t) throw new Error('ends early: ' + src);
    if (t.k === 'num') return [[t.v, 0]];
    if (t.k === '(') { const a = expr(); if (!toks[p] || toks[p].k !== ')') throw new Error('no ) in ' + src); p++; return a; }
    if (t.k === 'id') { if (t.v in env) { const x = env[t.v]; return [Array.isArray(x) ? x : [x, 0]]; } if (t.v === 'i') return [[0, 1]]; if (t.v === 'e') return [[Math.E, 0]]; if (t.v === 'π') return [[Math.PI, 0]]; throw new Error(`unknown ${t.v} in ${src}`); }
    if (t.k === 'fn') {
      if (t.v === '√') return atom().map(C.sqrt);
      if (t.v === '∛') return atom().map(a => [Math.cbrt(a[0]), 0]);
      const a = factor();
      return a.map(x => { if (Math.abs(x[1]) > 1e-9 || x[0] <= 0) throw new Error('log of a non-positive number'); return [t.v === 'ln' ? Math.log(x[0]) : Math.log(x[0]) / Math.log(t.b), 0]; });
    }
    throw new Error(`unexpected ${t.k} in ${src}`);
  }
  const out = expr();
  if (p !== toks.length) throw new Error('left over in ' + src);
  return out;
}
const ev1 = (s, env) => { const v = ev(s, env); if (v.length !== 1) throw new Error('two values in ' + s); return v[0]; };
const evR = (s, env) => { const v = ev1(s, env); if (Math.abs(v[1]) > 1e-7 * Math.max(1, Math.abs(v[0]))) throw new Error('not real'); return v[0]; };
const close = (a, b, tol = 1e-7) => Math.abs(a - b) <= tol * Math.max(1, Math.abs(a), Math.abs(b));
const closeC = (a, b) => close(a[0], b[0]) && close(a[1], b[1]);
// does "left = right" (or a chain with < > ≤ ≥) hold at env?
function holds(eq, env) {
  const parts = eq.split(/\s*([=<>≤≥])\s*/);
  for (let i = 0; i + 2 < parts.length; i += 2) {
    const a = ev1(parts[i], env), b = ev1(parts[i + 2], env), rel = parts[i + 1];
    if (rel === '=') { if (!closeC(a, b)) return false; continue; }
    if (Math.abs(a[1]) > 1e-9 || Math.abs(b[1]) > 1e-9) return false;
    const ok = { '<': a[0] < b[0] - 1e-9, '>': a[0] > b[0] + 1e-9, '≤': a[0] <= b[0] + 1e-9, '≥': a[0] >= b[0] - 1e-9 }[rel];
    if (!ok) return false;
  }
  return true;
}
const safe = f => { try { return f(); } catch (e) { return undefined; } };
// the values in an answer like "x = 3 ± √5" or "x = −2, x = 7"
const rootsOf = a => a.replace(/^x = /, '').split(/, x = /).flatMap(t => ev(t));
// check a printed quadratic answer against the equation: every value solves it and the count is right
function quadCheck(eq, ans, complex) {
  const out = [];
  const [L, R] = eq.split(' = '), f = x => C.sub(ev1(L, { x }), ev1(R, { x }));
  const c0 = f([0, 0]), c1 = f([1, 0]), cm = f([-1, 0]);   // a x² + b x + c from three values
  const a = (c1[0] + cm[0]) / 2 - c0[0], b = (c1[0] - cm[0]) / 2, c = c0[0], D = b * b - 4 * a * c;
  if (ans === 'no real solutions') { if (!(D < -1e-9)) out.push(`${eq}: says no real solutions, discriminant is ${D}`); return out; }
  const vals = rootsOf(ans);
  for (const v of vals) { const y = f(v); if (Math.hypot(y[0], y[1]) > 1e-6 * Math.max(1, Math.abs(a) * (v[0] * v[0] + v[1] * v[1]))) out.push(`${eq}: ${ans} does not solve it`); }
  const want = Math.abs(D) < 1e-9 ? 1 : 2, distinct = vals.filter((v, i) => vals.findIndex(w => closeC(v, w)) === i).length;
  if (distinct !== want) out.push(`${eq}: ${ans} gives ${distinct} values, should be ${want}`);
  if (!complex && vals.some(v => Math.abs(v[1]) > 1e-9)) out.push(`${eq}: ${ans} is not real`);
  return out;
}
// tidy-text checks shared by every answer
function tidy(t) {
  const s = String(t), bad = [];
  if (/\+ −|− −|\+ \+|− \+/.test(s)) bad.push('untidy signs');
  if (/(^|[\s(−+±])1(?=[a-z(√])/.test(s)) bad.push('a coefficient of 1 is written');
  if (/(^|[\s(−+±])0(?=[a-z(√])/.test(s)) bad.push('a zero term is written');
  for (const m of s.matchAll(/(?<![\d).√])(\d+)\/(\d+)(?![\d(.])/g)) if (gcd(+m[1], +m[2]) !== 1 || +m[2] === 1) bad.push(`fraction ${m[0]} not in lowest terms`);
  for (const m of s.matchAll(/√(\d+)/g)) { const n = +m[1]; if (rootSplit(n)[0] !== 1) bad.push(`√${n} not simplified`); }
  return bad;
}

/* ---------- drawing ---------- */
const RED = '#b03020', FONT = 'font-family="Helvetica, Arial, sans-serif"';
let UID = 0;
// a coordinate grid; draw({X, Y, ...}) returns the marks; key marks go in <g class="ws-ans">
function plane(o, draw, label) {
  const { xlo = -8, xhi = 8, ylo = xlo, yhi = xhi, S = 13, every = 2, ystep = 1, xstep = 1 } = o, m = 16;
  const W = (xhi - xlo) / xstep * S + 2 * m, Ht = (yhi - ylo) / ystep * S + 2 * m;
  const X = x => +(m + (x - xlo) / xstep * S).toFixed(1), Y = y => +(m + (yhi - y) / ystep * S).toFixed(1);
  const id = 'alclip' + (++UID);
  let b = `<defs><clipPath id="${id}"><rect x="${X(xlo)}" y="${Y(yhi)}" width="${X(xhi) - X(xlo)}" height="${Y(ylo) - Y(yhi)}"/></clipPath></defs>`;
  for (let x = xlo; x <= xhi + 1e-9; x += xstep) b += `<line x1="${X(x)}" y1="${Y(yhi)}" x2="${X(x)}" y2="${Y(ylo)}" stroke="#c8c8c8" stroke-width="0.7"/>`;
  for (let y = ylo; y <= yhi + 1e-9; y += ystep) b += `<line x1="${X(xlo)}" y1="${Y(y)}" x2="${X(xhi)}" y2="${Y(y)}" stroke="#c8c8c8" stroke-width="0.7"/>`;
  const ax = ylo <= 0 && yhi >= 0 ? 0 : ylo, ay = xlo <= 0 && xhi >= 0 ? 0 : xlo;
  b += `<line x1="${X(xlo)}" y1="${Y(ax)}" x2="${X(xhi)}" y2="${Y(ax)}" stroke="#222" stroke-width="1.6"/><line x1="${X(ay)}" y1="${Y(ylo)}" x2="${X(ay)}" y2="${Y(yhi)}" stroke="#222" stroke-width="1.6"/>`;
  const fs = 9;
  for (let x = xlo; x <= xhi + 1e-9; x += xstep * every) if (Math.abs(x - ay) > 1e-9) b += `<text x="${X(x)}" y="${Y(ax) + 10}" ${FONT} font-size="${fs}" text-anchor="middle" fill="#222">${num(+x.toFixed(4))}</text>`;
  for (let y = ylo; y <= yhi + 1e-9; y += ystep * every) if (Math.abs(y - ax) > 1e-9) b += `<text x="${X(ay) - 3}" y="${Y(y) + 3}" ${FONT} font-size="${fs}" text-anchor="end" fill="#222">${num(+y.toFixed(4))}</text>`;
  b += `<text x="${X(xhi) + 3}" y="${Y(ax) + 4}" ${FONT} font-size="11" font-style="italic">x</text><text x="${X(ay) + 4}" y="${Y(yhi) - 5}" ${FONT} font-size="11" font-style="italic">y</text>`;
  b += `<g clip-path="url(#${id})">${draw({ X, Y, xlo, xhi, ylo, yhi })}</g>`;
  return `<svg class="gen-svg" viewBox="0 0 ${W} ${Ht}" role="img" aria-label="${esc(label)}" style="max-width:${(W / 96).toFixed(2)}in">${b}</svg>`;
}
// a straight line y = m x + b across the whole grid (or x = c when vert)
const lineMark = (g, mm, bb, color, dash, vert) => {
  const [x1, y1, x2, y2] = vert != null ? [vert, g.ylo - 1, vert, g.yhi + 1] : [g.xlo - 1, mm * (g.xlo - 1) + bb, g.xhi + 1, mm * (g.xhi + 1) + bb];
  return `<line x1="${g.X(x1)}" y1="${g.Y(y1)}" x2="${g.X(x2)}" y2="${g.Y(y2)}" stroke="${color}" stroke-width="2.2"${dash ? ' stroke-dasharray="7 5"' : ''}/>`;
};
const dot = (g, x, y, color = '#222', rr = 3.6) => `<circle cx="${g.X(x)}" cy="${g.Y(y)}" r="${rr}" fill="${color}"/>`;
// a curve y = f(x), broken where f is undefined or jumps (asymptotes)
function curveMark(g, f, color, lo = g.xlo, hi = g.xhi) {
  const N = 240, span = g.yhi - g.ylo; let d = '', prev = null;
  for (let k = 0; k <= N; k++) {
    const x = lo + (hi - lo) * k / N, y = safe(() => f(x));
    if (y == null || !isFinite(y) || Math.abs(y) > 60 * span) { prev = null; continue; }
    const yc = Math.max(g.ylo - span, Math.min(g.yhi + span, y));
    if (prev == null || Math.abs(yc - prev) > span) d += `M${g.X(x)} ${g.Y(yc).toFixed(1)}`; else d += `L${g.X(x)} ${g.Y(yc).toFixed(1)}`;
    prev = yc;
  }
  return `<path d="${d}" fill="none" stroke="${color}" stroke-width="2.2"/>`;
}
// keep the part of a polygon where a x + b y ≤ c
function clipPoly(pts, a, b, c) {
  const out = [], f = p => a * p[0] + b * p[1] - c;
  for (let i = 0; i < pts.length; i++) {
    const P = pts[i], R = pts[(i + 1) % pts.length], fp = f(P), fr = f(R);
    if (fp <= 0) out.push(P);
    if ((fp < 0 && fr > 0) || (fp > 0 && fr < 0)) { const t = fp / (fp - fr); out.push([P[0] + t * (R[0] - P[0]), P[1] + t * (R[1] - P[1])]); }
  }
  return out;
}

/* ---------- layout ---------- */
const cell = (n, head, work, foot, cls = '') => `<div class="al-cell${cls}"><p><span class="ws-num">${n}.</span> ${head}</p>${work ? `<div class="al-work" style="min-height:${work}in"></div>` : ''}${foot ? `<div class="al-ans">${foot}</div>` : ''}</div>`;
const grid = (cells, cols = 2) => `<div class="al-grid al-c${cols}">${cells.join('')}</div>`;
const sys = (a, b) => `<span class="al-sys"><span>${F(a)}</span><span>${F(b)}</span></span>`;
const htable = (rows) => `<table class="al-ht">${rows.map(([h, ...cs]) => `<tr><th>${F(h)}</th>${cs.map(c => `<td>${c}</td>`).join('')}</tr>`).join('')}</table>`;
const frac = (n, d) => `<span class="gen-frac"><span>${n}</span><span>${d}</span></span>`;
const lines = n => `<div class="ws-lines">${'<span></span>'.repeat(n)}</div>`;
const NAMES = ['Ana', 'Ben', 'Carla', 'Dev', 'Eli', 'Fatima', 'Grace', 'Hugo', 'Ivy', 'Jamal', 'Kai', 'Lena', 'Marco', 'Nina', 'Omar', 'Priya', 'Rosa', 'Sam', 'Tara', 'Victor', 'Wen', 'Zoe'];

/* ---------- lines ---------- */
const siT = (m, b) => `y = ${sum([[m, 'x'], [b, '']])}`;
function psT(m, x1, y1) {
  m = toQ(m);
  const left = y1 === 0 ? 'y' : `y ${y1 < 0 ? '+' : MIN} ${Math.abs(y1)}`;
  let right;
  if (m.n === 0) right = '0';
  else if (x1 === 0) right = sum([[m, 'x']]);
  else { const inner = `(${fac(x1)})`, a = Q(Math.abs(m.n), m.d);
    right = (m.n < 0 ? MIN : '') + (a.n === 1 && a.d === 1 ? (m.n < 0 ? inner : fac(x1)) : (a.d === 1 ? a.n : `(${qT(a)})`) + inner); }
  return `${left} = ${right}`;
}
function stdT(m, b) {   // y = (p/q) x + b  ->  A x + B y = C, A > 0 (or A = 0, B > 0), whole numbers with no common factor
  m = toQ(m); b = toQ(b);
  let A = -m.n * b.d, B = m.d * b.d, Cc = b.n * m.d;
  if (A < 0 || (A === 0 && B < 0)) { A = -A; B = -B; Cc = -Cc; }
  const g = gcd(gcd(A, B), Cc) || 1; A /= g; B /= g; Cc /= g;
  return `${sum([[A, 'x'], [B, 'y']])} = ${num(Cc)}`;
}
// coefficients of a line written any way: A x + B y + C0 = 0
const lineCoef = eq => { const [L, R] = eq.split(' = '), f = (x, y) => evR(L, { x, y }) - evR(R, { x, y }); const c = f(0, 0); return [f(1, 0) - c, f(0, 1) - c, c]; };
// a line y = (p/q) x + b through lattice points: x = k q
function latticeLine(r, o = {}) {
  const { lo = -6, hi = 6, prop = false, qs = [1, 1, 2, 3], pmax = 5, bmax = 4, zero = false } = o;
  for (let t = 0; t < 300; t++) {
    const q = r.pick(qs), p = zero && r.chance(.12) ? 0 : nz(r, -pmax, pmax);
    if (p === 0 && q !== 1) continue;
    if (gcd(Math.abs(p), q) !== 1 || Math.abs(p / q) > 4) continue;
    const b = prop ? 0 : nz(r, -bmax, bmax), ks = [];
    for (let k = -12; k <= 12; k++) { const x = k * q, y = p * k + b; if (x >= lo && x <= hi && y >= lo && y <= hi) ks.push(k); }
    if (ks.length < 2) continue;
    const [k1, k2] = r.sample(ks, 2).sort((a, c) => a - c);
    return { p, q, m: Q(p, q), b, P1: [k1 * q, p * k1 + b], P2: [k2 * q, p * k2 + b], ks };
  }
  return null;
}

function skSlope(r, n) {
  const ng = Math.ceil(n / 2), cells = [], items = [];
  const made = r.distinct(n, () => { const prop = r.chance(.4), L = latticeLine(r, items.length < ng ? { prop } : { prop, lo: -12, hi: 12, pmax: 9, bmax: 9, qs: [1, 2, 3, 4, 5] }); return L; }, L => `${L.P1}|${L.P2}`);
  made.forEach((L, i) => {
    const graph = i < ng, slope = qT(L.m), prop = L.b === 0 ? siT(L.m, 0) : 'not proportional';
    let [A, B] = [L.P1, L.P2]; if (!graph && r.chance(.5)) [A, B] = [B, A];
    items.push({ k: 'slope', q: `${graph ? 'Graph' : 'Points'}: ${pt(...A)} and ${pt(...B)}`, a: `${slope}; ${prop}`, P1: A, P2: B });
    const foot = `<p>slope = ${ab(slope, 3.5)}</p><p>y = mx, or not proportional: ${ab(prop, 7)}</p>`;
    if (graph) {
      const svg = plane({ xlo: -6, xhi: 6, S: 11 }, g => lineMark(g, qv(L.m), L.b, '#222') + dot(g, ...A) + dot(g, ...B), `A line through ${pt(...A)} and ${pt(...B)}`);
      cells.push(cell(i + 1, 'Find the slope of the line through the two marked points.', 0, svg + foot, ' al-graph'));
    } else cells.push(cell(i + 1, `Find the slope of the line through ${F(pt(...A))} and ${F(pt(...B))}.`, 0.55, foot));
  });
  return {
    ican: 'I can find the slope of a line from a graph or from two points, and write y = mx when the line goes through the origin.',
    directions: 'Find each slope as rise over run, in simplest form. If the line goes through the origin, the relationship is proportional: write its equation y = mx. Otherwise write "not proportional".',
    ex: example(`Through (−2, 1) and (4, −3): slope = (−3 − 1) / (4 − (−2)) = −4/6 = −2/3.`, 'The line does not pass through (0, 0), so it is not proportional. A line through (0, 0) with slope 3 is y = 3x.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Subtracting the coordinates in a different order on top and bottom (the sign flips), and putting run over rise. A line through the origin is the test for proportional, not a positive slope.',
  };
}

function skLine(r, n, course) {
  const items = [], cells = [], hs = course !== 'g8';
  const forms = r.shuffle(Array.from({ length: n }, (_, i) => ['si', 'ps', 'std'][i % 3]));
  const ins = hs ? ['pts', 'table', 'slopept', 'par', 'perp'] : ['pts', 'pts', 'table'];
  const made = r.distinct(n, () => {
    const L = latticeLine(r, { lo: -9, hi: 9, pmax: 6, bmax: 8, zero: true }); if (!L) return null;
    return { L, src: r.pick(ins) };
  }, x => `${x.L.p}/${x.L.q}/${x.L.b}`);
  made.forEach(({ L, src }, i) => {
    const form = hs ? forms[i] : 'si', P = L.P1, P2 = L.P2;
    let head, given;
    if (src === 'pts') head = `Through ${F(pt(...P))} and ${F(pt(...P2))}.`;
    else if (src === 'table') { const ks = L.ks.slice(0, 4).length >= 3 ? L.ks.slice(0, 4) : L.ks;
      head = `The table shows points on a line.${htable([['x', ...ks.map(k => num(k * L.q))], ['y', ...ks.map(k => num(L.p * k + L.b))]])}`; }
    else if (src === 'slopept') head = `Slope ${F(qT(L.m))}, through ${F(pt(...P))}.`;
    else if (src === 'par') { let b2 = L.b; while (b2 === L.b) b2 = nz(r, -9, 9); given = siT(L.m, b2); head = `Parallel to ${F(given)}, through ${F(pt(...P))}.`; }
    else { if (!L.p) { head = `Through ${F(pt(...P))} and ${F(pt(...P2))}.`; src = 'pts'; }
      else { const pm = Q(-L.q, L.p), b2 = nz(r, -6, 6); given = siT(pm, b2); head = `Perpendicular to ${F(given)}, through ${F(pt(...P))}.`; } }
    const ans = form === 'si' ? siT(L.m, L.b) : form === 'ps' ? psT(L.m, P[0], P[1]) : stdT(L.m, L.b);
    const fname = { si: 'slope-intercept form', ps: `point-slope form, using ${pt(...P)}`, std: 'standard form' }[form];
    items.push({ k: 'line', q: `${src} ${fname}: ${pt(...P)} m ${qT(L.m)}`, a: ans, P, P2: [P[0] + L.q, P[1] + L.p], form });
    cells.push(cell(i + 1, `${head}${hs ? ` Write it in <b>${esc(fname)}</b>.` : ''}`, hs ? 0.7 : 0.75, ab(ans, 10)));
  });
  const exL = siT(Q(2), -1);
  return {
    ican: hs ? 'I can write the equation of a line in slope-intercept, point-slope and standard form.' : 'I can write the equation of a line from two points or a table.',
    directions: hs ? 'Write an equation for each line in the form asked. Use fractions in simplest form; in standard form, use whole numbers with A positive.'
      : 'Write the equation of each line in the form y = mx + b. Find the slope first, then the y-intercept. Use fractions in simplest form.',
    ex: example(`Through (1, 1) and (3, 5): m = (5 − 1)/(3 − 1) = 2. Then 1 = 2(1) + b, so b = −1, and ${exL}.`,
      hs ? 'Point-slope form: y − 1 = 2(x − 1). Standard form: 2x − y = 1. Parallel lines have the same slope; perpendicular slopes multiply to −1.' : 'Check: the other point works too, since 2(3) − 1 = 5.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Finding b with the wrong sign, mixing up x and y when substituting, and using the opposite slope instead of the opposite reciprocal for a perpendicular line.',
    notes: hs ? 'Point-slope answers use the point named in the problem; another point on the same line is also correct.' : '',
  };
}

/* ---------- grade 8 roots, squeezing, exponent rules ---------- */
function skRoots(r, n) {
  const SQF = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 33, 35, 37, 38, 39, 41, 42, 43, 46, 47];
  const maker = () => {
    const T = r.pick(['sq', 'sq', 'sqstep', 'sqfrac', 'sqirr', 'cube', 'cube', 'cubefrac', 'cubestep']);
    if (T === 'sq') { const k = r.int(2, 15); return { eq: `x² = ${k * k}`, a: `x = ±${k}`, p: 2 }; }
    if (T === 'sqstep') { const k = r.int(2, 12), c = r.int(2, 30);
      return r.chance(.5) ? { eq: `x² ${MIN} ${c} = ${num(k * k - c)}`, a: `x = ±${k}`, p: 2 } : { eq: `${c % 4 + 2}x² = ${(c % 4 + 2) * k * k}`, a: `x = ±${k}`, p: 2 }; }
    if (T === 'sqfrac') { const b = r.int(2, 9), a = r.int(1, b + 3); if (gcd(a, b) !== 1) return null; return { eq: `x² = ${a * a}/${b * b}`, a: `x = ±${a}/${b}`, p: 2 }; }
    if (T === 'sqirr') { const m = r.pick(SQF); return { eq: `x² = ${m}`, a: `x = ±√${m}`, p: 2 }; }
    if (T === 'cube') { const k = nz(r, -6, 10); if (Math.abs(k) < 2) return null; return { eq: `x³ = ${num(k ** 3)}`, a: `x = ${num(k)}`, p: 3 }; }
    if (T === 'cubefrac') { const b = r.int(2, 5), a = r.int(1, 4); if (gcd(a, b) !== 1) return null; return { eq: `x³ = ${a ** 3}/${b ** 3}`, a: `x = ${a}/${b}`, p: 3 }; }
    const k = r.int(2, 6), c = r.int(1, 40); return { eq: `x³ + ${c} = ${k ** 3 + c}`, a: `x = ${k}`, p: 3 };
  };
  const eqs = r.distinct(n, maker, x => x.eq), items = [], cells = [];
  eqs.forEach((e, i) => { items.push({ k: 'root', q: e.eq, a: e.a, p: e.p }); cells.push(cell(i + 1, `Solve ${F(e.eq)}.`, 0.5, ab(e.a, 6))); });
  const OBJ = [['gift box', 'inches'], ['storage crate', 'feet'], ['ice cube tray mold', 'centimeters'], ['water tank', 'meters'], ['toy block', 'centimeters'], ['planter', 'inches']];
  const cubes = r.sample(OBJ, 2).map(([o, u]) => { const k = r.int(2, 12); return { o, u, k, V: k ** 3 }; });
  const ccells = cubes.map((c, j) => { const a = `${c.k} ${c.u}`;
    items.push({ k: 'cube', q: `cube ${c.o} ${c.V}`, a, V: c.V });
    return cell(n + j + 1, `A cube-shaped ${c.o} has a volume of ${comma(c.V)} cubic ${c.u}. How long is each edge?`, 0.55, ab(a, 6)); });
  return {
    ican: 'I can solve equations like x² = p and x³ = p with square roots and cube roots.',
    directions: 'Solve each equation. A square has two square roots, so x² = p has two solutions (write ±). A cube root has one value, and it can be negative. Leave a root that is not whole as √.',
    ex: example('x² = 81, so x = ±9, because 9 × 9 = 81 and (−9)(−9) = 81.', 'x³ = −8, so x = −2, because (−2)(−2)(−2) = −8. x² = 7, so x = ±√7.'),
    parts: [part('Practice', grid(cells)), part('Cubes', grid(ccells))], items,
    mistakes: 'Giving only the positive answer to x² = p, giving ± for a cube root, and dividing by 2 or 3 instead of taking a root.',
  };
}

function numLine(lo, mark, label) {   // lo to lo + 1 in tenths; the key marks the value
  const x0 = 20, x1 = 320, y = 24, X = t => x0 + (t - lo) * (x1 - x0);
  let s = `<line x1="${x0 - 10}" y1="${y}" x2="${x1 + 10}" y2="${y}" stroke="#222" stroke-width="1.5"/>`;
  for (let k = 0; k <= 10; k++) { const t = lo + k / 10, big = k % 5 === 0;
    s += `<line x1="${X(t)}" y1="${y - (big ? 8 : 5)}" x2="${X(t)}" y2="${y + (big ? 8 : 5)}" stroke="#222" stroke-width="1.2"/>`;
    if (big) s += `<text x="${X(t)}" y="${y + 22}" ${FONT} font-size="12" text-anchor="middle">${+(t.toFixed(1))}</text>`; }
  s += `<g class="ws-ans"><circle cx="${X(mark).toFixed(1)}" cy="${y}" r="5.5" fill="${RED}"/></g>`;
  return `<svg class="gen-svg" viewBox="0 0 340 52" role="img" aria-label="${esc(label)}" style="max-width:3.4in">${s}</svg>`;
}
function skSqueeze(r, n) {
  const ns = r.distinct(n, () => { const v = r.int(2, 150); if (isSq(v)) return null; const s = Math.sqrt(v), f = s * 10 - Math.floor(s * 10); if (Math.abs(f - 0.5) < 0.08) return null; return v; }, x => x);
  const items = [], cells = [];
  ns.forEach((v, i) => {
    const a = Math.floor(Math.sqrt(v)), t = (Math.round(Math.sqrt(v) * 10) / 10).toFixed(1);
    items.push({ k: 'squeeze', q: `√${v}`, a: `${a} and ${a + 1}; ${t}`, v });
    cells.push(cell(i + 1, `√${v} is between ${ab(a, 2.2)} and ${ab(a + 1, 2.2)}, because ${ab(a * a, 2.5)} &lt; ${v} &lt; ${ab((a + 1) ** 2, 2.5)}.`, 0,
      `<p>To the nearest tenth, √${v} ≈ ${ab(t, 3)}. Mark it on the number line.</p>${numLine(a, Math.sqrt(v), `Number line from ${a} to ${a + 1} in tenths`)}`));
  });
  return {
    ican: 'I can estimate a square root by squeezing it between perfect squares and place it on a number line.',
    directions: 'Find the two whole numbers each square root is between, using perfect squares. Then square tenths to get closer, and mark the square root on the number line.',
    ex: example('√50: 7² = 49 and 8² = 64, so √50 is between 7 and 8, close to 7.', 'Try tenths: 7.1² = 50.41, which is just over 50, and 7.0² = 49. 50 is closer to 50.41 than to 49, so √50 ≈ 7.1.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Dividing by 2 instead of finding a square root, and picking the tenth by halfway between the whole numbers instead of squaring tenths.',
    notes: 'Each root is at least 0.03 away from a halfway point, so the nearest tenth is clear. A calculator check is fine after the squeeze.',
  };
}

function skExpRules(r, n) {
  const [nA, nB] = n, items = [], ca = [], cb = [];
  const rep = (b, k) => Array(k).fill(b).join('·');
  const A = r.distinct(nA, () => {
    const b = r.pick(['x', 'a', 'y', 'm', '2', '3']), T = r.pick(['prod', 'quot', 'pow']);
    if (T === 'prod') { const m = r.int(2, 4), k = r.int(2, 4); return { q: `${b}${sup(m)} · ${b}${sup(k)}`, ex: `(${rep(b, m)})(${rep(b, k)})`, res: `${b}${sup(m + k)}`, b }; }
    if (T === 'quot') { const m = r.int(4, 7), k = r.int(2, m - 1); return { q: `${b}${sup(m)}/${b}${sup(k)}`, ex: `(${rep(b, m)})/(${rep(b, k)})`, res: m - k === 1 ? b : `${b}${sup(m - k)}`, b }; }
    const m = r.int(2, 3), k = r.int(2, 3); return { q: `(${b}${sup(m)})${sup(k)}`, ex: Array(k).fill(`(${rep(b, m)})`).join(''), res: `${b}${sup(m * k)}`, b };
  }, x => x.q);
  A.forEach((e, i) => { items.push({ k: 'expo', q: e.q, a: `${e.ex} = ${e.res}`, part: 'A' });
    ca.push(cell(i + 1, `${F(e.q)}`, 0, `<p>Written out: ${ab(e.ex, 10)}</p><p>As one power: ${ab(e.res, 3)}</p>`)); });
  const monoT = (c, ex) => { const v = ex.filter(([, e]) => e > 0).map(([s, e]) => mono(s, e)).join(''), d = ex.filter(([, e]) => e < 0).map(([s, e]) => mono(s, -e)).join('');
    const top = c === 1 && v ? v : `${c}${v}`; return d ? `${top}/${d}` : top; };
  const aQ = new Set(A.map(e => e.q));
  const B = r.distinct(nB, () => { const e = (() => {
    const T = r.pick(['prod', 'quot', 'pow', 'neg', 'zero', 'num', 'two']);
    const c1 = r.int(1, 6), c2 = r.int(2, 6), m = r.int(2, 6), k = r.int(2, 5);
    if (T === 'prod') return { q: `(${c1 === 1 ? '' : c1}x${sup(m)})(${c2}x${sup(k)})`, a: monoT(c1 * c2, [['x', m + k]]) };
    if (T === 'quot') { const top = c1 * c2; if (m === k) return null; return { q: `${top}x${sup(m)}/(${c2}x${sup(k)})`, a: monoT(c1, [['x', m - k]]) }; }
    if (T === 'pow') { const c = r.int(1, 3), mm = r.int(2, 4), kk = r.int(2, 4); if (c ** kk > 81) return null; return { q: `(${c === 1 ? '' : c}x${sup(mm)})${sup(kk)}`, a: monoT(c ** kk, [['x', mm * kk]]) }; }
    if (T === 'neg') { const a1 = -r.int(1, 5), b1 = r.int(1, 8); if (a1 + b1 === 0 || a1 + b1 === 1) return null; return { q: `x${sup(a1)} · x${sup(b1)}`, a: monoT(1, [['x', a1 + b1]]) }; }
    if (T === 'zero') { const c = r.int(2, 9); return r.chance(.5) ? { q: `${c}x⁰`, a: String(c) } : { q: `(${c}x${sup(m)})⁰`, a: '1' }; }
    if (T === 'num') { const b = r.pick([2, 3, 5, 10]), e1 = r.int(-4, 4), e2 = r.int(-4, 4), e = e1 + e2; if (!e1 || !e2 || Math.abs(e) > 3 || b ** Math.abs(e) > 1000) return null;
      return { q: `${b}${sup(e1)} · ${b}${sup(e2)}`, a: e >= 0 ? String(b ** e) : `1/${b ** -e}` }; }
    const p1 = r.int(1, 4), q1 = r.int(1, 4), kk = r.int(2, 3); return { q: `(x${sup(p1).replace('¹', '')}y${sup(q1).replace('¹', '')})${sup(kk)}`, a: mono('x', p1 * kk) + mono('y', q1 * kk) };
  })(); return e && !aQ.has(e.q) ? e : null; }, x => x.q);
  B.forEach((e, i) => { items.push({ k: 'expo', q: e.q, a: e.a, part: 'B' }); cb.push(cell(nA + i + 1, `Simplify ${F(e.q)}`, 0.45, ab(e.a, 4))); });
  return {
    ican: 'I can use the product, quotient and power rules for exponents, including zero and negative exponents.',
    directions: 'Part A: write each expression out as repeated multiplication, then as one power. Look for the pattern. Part B: simplify using the rules. Answers have only positive exponents.',
    ex: example('x³ · x² = (x·x·x)(x·x) = x⁵: add the exponents when multiplying the same base.', 'x⁶/x² = x⁴ (subtract). (x²)³ = x⁶ (multiply). x⁰ = 1, and x⁻³ = 1/x³.'),
    parts: [part('Part A: Expand to see the rule', grid(ca)), part('Part B: Use the rules', grid(cb))], items,
    mistakes: 'Multiplying exponents when multiplying powers (x³ · x² as x⁶), multiplying the base by the exponent, and forgetting to raise the number in front to the power: (2x³)² is 4x⁶.',
  };
}

/* ---------- systems ---------- */
function sysLines(r, std) {
  for (let t = 0; t < 400; t++) {
    const x0 = r.int(-5, 5), y0 = r.int(-5, 5);
    const mk = () => { const q = r.pick([1, 1, 2]), p = nz(r, -3, 3); if (q === 2 && p % 2 === 0) return null; const b = y0 - p * x0 / q; if (!Number.isInteger(b) || Math.abs(b) > 7) return null; return { m: Q(p, q), b }; };
    const L1 = mk(), L2 = mk();
    if (!L1 || !L2 || L1.m.n * L2.m.d === L2.m.n * L1.m.d) continue;
    const e = [L1, L2].map((L, i) => std && i === 1 ? stdT(L.m, L.b) : siT(L.m, L.b));
    return { x0, y0, L1, L2, e };
  }
}
function skSysGraph(r, n, course) {
  const sys2 = r.distinct(n, () => sysLines(r, course !== 'g8' && r.chance(.5)), s => s.e.join('|'));
  const items = [], cells = [];
  sys2.forEach((s, i) => {
    const a = pt(s.x0, s.y0);
    items.push({ k: 'sys', q: s.e.join(' and '), a, eqs: s.e });
    const svg = plane({ xlo: -8, xhi: 8, S: 12 }, g => `<g class="ws-ans">${lineMark(g, qv(s.L1.m), s.L1.b, RED)}${lineMark(g, qv(s.L2.m), s.L2.b, RED)}${dot(g, s.x0, s.y0, RED, 5)}</g>`, 'Empty coordinate grid from −8 to 8 for graphing the system');
    cells.push(cell(i + 1, `Graph the system ${sys(s.e[0], s.e[1])}`, 0, `${svg}<p>Solution: ${ab(a, 5)}</p><p>Check it in both equations:</p><div class="al-work" style="min-height:.55in"></div>`, ' al-graph'));
  });
  return {
    ican: 'I can solve a system of two linear equations by graphing and check the intersection point.',
    directions: 'Graph both lines on the grid. The point where they cross is the solution. Write it as an ordered pair, then substitute it into both equations to check.',
    ex: example('y = x + 1 and y = −x + 3 cross at (1, 2).', 'Check: 2 = 1 + 1 is true, and 2 = −1 + 3 is true, so (1, 2) solves both equations.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Graphing the slope as run over rise, starting at the x-intercept instead of the y-intercept, and checking in only one equation. For standard form, find the two intercepts or solve for y first.',
  };
}
function sysAlgOne(r) {
  const x0 = nz(r, -9, 9), y0 = nz(r, -9, 9), T = r.pick(['sub', 'sub', 'elim', 'elim', 'elim2']);
  const std = (A, B) => `${sum([[A, 'x'], [B, 'y']])} = ${num(A * x0 + B * y0)}`;
  const okC = (A, B) => gcd(gcd(A, B), A * x0 + B * y0) === 1;
  let e1, e2, A1, B1, A2, B2;
  if (T === 'sub') {
    if (r.chance(.6)) { const m = nz(r, -5, 5), b = y0 - m * x0; if (Math.abs(b) > 15) return null; e1 = siT(Q(m), b); [A1, B1] = [-m, 1]; }
    else { const k = nz(r, -4, 4), c = x0 - k * y0; if (Math.abs(c) > 15) return null; e1 = `x = ${lin(k, c, 'y')}`; [A1, B1] = [1, -k]; }
    A2 = nz(r, -6, 6); B2 = nz(r, -6, 6); if (!okC(A2, B2)) return null; e2 = std(A2, B2);
  } else {
    A1 = nz(r, -6, 6); B1 = nz(r, -6, 6);
    if (T === 'elim') { if (r.chance(.5)) { B2 = r.chance(.5) ? -B1 : B1; A2 = nz(r, -6, 6); } else { A2 = r.chance(.5) ? -A1 : A1; B2 = nz(r, -6, 6); } }
    else { A2 = nz(r, -7, 7); B2 = nz(r, -7, 7); if (Math.abs(A1) === Math.abs(A2) || Math.abs(B1) === Math.abs(B2)) return null; }
    if (!okC(A1, B1) || !okC(A2, B2)) return null;
    e1 = std(A1, B1); e2 = std(A2, B2);
  }
  if (A1 * B2 - A2 * B1 === 0) return null;
  return { e: [e1, e2], a: pt(x0, y0), T };
}
function skSysAlg(r, n) {
  const ss = r.distinct(n, () => sysAlgOne(r), s => s.e.join('|')), items = [], cells = [];
  ss.forEach((s, i) => { items.push({ k: 'sys', q: s.e.join(' and '), a: s.a, eqs: s.e });
    cells.push(cell(i + 1, `${sys(s.e[0], s.e[1])}`, 1.05, `(<i>x</i>, <i>y</i>) = ${ab(s.a, 5)}`)); });
  const why = 'If (x, y) makes both equations true, the left sides equal the right sides, and adding equal amounts to equal amounts keeps them equal, so the new equation is true for the same (x, y). The step can be undone by subtracting, so no solution is gained or lost: the new system has exactly the same solutions.';
  return {
    ican: 'I can solve a system of linear equations by substitution or elimination and explain why elimination works.',
    directions: 'Solve each system by substitution or elimination. Pick the method that fits: substitution when a variable is already alone, elimination when the coefficients line up. Check your answer in both equations.',
    ex: example('2x + y = 7 and x − y = 2: add the equations to get 3x = 9, so x = 3. Then 3 − y = 2, so y = 1.', 'Solution (3, 1). Check: 2(3) + 1 = 7 and 3 − 1 = 2.'),
    parts: [part('Practice', grid(cells)), part('Explain', `<p>Why does adding two equations (or a multiple of one to the other) give a new system with the same solution as the old one?</p>${lines(3)}${keyp(why)}`)], items,
    mistakes: 'Multiplying only one side of an equation by a number, dropping a negative sign when subtracting equations, and stopping after finding one variable.',
  };
}
function sysStory(r, kind) {
  const nm = r.pick(NAMES);
  if (kind === 'tickets') {
    const [place, A, B] = r.pick([['school play', 'adult', 'student'], ['concert', 'adult', 'child'], ['basketball game', 'adult', 'student'], ['science museum', 'adult', 'child'], ['county fair', 'adult', 'child']]);
    const pa = r.pick([6, 7, 8, 9, 10, 12, 15]), pc = r.int(3, pa - 2), na = r.int(20, 220), nc = r.int(20, 260), tot = na + nc, M = pa * na + pc * nc;
    const va = A[0], vc = B[0];
    return { kind, text: `The ${place} sold ${tot} tickets and took in ${money(M)}. ${A[0].toUpperCase() + A.slice(1)} tickets cost $${pa} and ${B} tickets cost $${pc}. How many of each kind were sold?`,
      vars: `${va} = number of ${A} tickets, ${vc} = number of ${B} tickets`, sys: [`${va} + ${vc} = ${tot}`, `${pa}${va} + ${pc}${vc} = ${M}`], env: { [va]: na, [vc]: nc },
      a: `${na} ${A} and ${nc} ${B} tickets`, d: { tot, M, pa, pc } };
  }
  if (kind === 'mixture') {
    if (r.chance(.5)) {
      for (let t = 0; t < 200; t++) {
        const p1 = r.pick([5, 10, 15, 20]), p2 = r.pick([25, 30, 40, 45, 50, 60]), x = r.int(2, 30), y = r.int(2, 30), V = x + y;
        if ((p1 * x + p2 * y) % V) continue; const p = (p1 * x + p2 * y) / V;
        const dec = v => String(v / 100).replace(/^0/, '0');
        return { kind, text: `A chemist has a ${p1}% salt solution and a ${p2}% salt solution. How many liters of each should she mix to make ${V} liters of a ${p}% salt solution?`,
          vars: `x = liters of the ${p1}% solution, y = liters of the ${p2}% solution`, sys: [`x + y = ${V}`, `${dec(p1)}x + ${dec(p2)}y = ${dec(p * V)}`], env: { x, y },
          a: `${x} liters of the ${p1}% solution and ${y} liters of the ${p2}% solution`, d: { V, p1, p2, p } };
      }
    }
    for (let t = 0; t < 200; t++) {
      const [n1, n2] = r.pick([['peanuts', 'cashews'], ['raisins', 'almonds'], ['oats', 'walnuts']]), c1 = r.int(2, 4), c2 = r.int(7, 12), x = r.int(2, 20), y = r.int(2, 20), W = x + y;
      if ((c1 * x + c2 * y) % W) continue; const c = (c1 * x + c2 * y) / W;
      return { kind, text: `A store mixes ${n1} that cost $${c1} per pound with ${n2} that cost $${c2} per pound. How many pounds of each make ${W} pounds of a mix that costs $${c} per pound?`,
        vars: `x = pounds of ${n1}, y = pounds of ${n2}`, sys: [`x + y = ${W}`, `${c1}x + ${c2}y = ${c * W}`], env: { x, y },
        a: `${x} pounds of ${n1} and ${y} pounds of ${n2}`, d: { V: W, p1: c1, p2: c2, p: c } };
    }
  }
  if (kind === 'plans') {
    for (let t = 0; t < 300; t++) {
      const [what, A, B, unit, fee, per] = r.pick([['gyms', 'Gym A', 'Gym B', 'months', 'to join', 'per month'], ['phone plans', 'Plan A', 'Plan B', 'gigabytes of data', 'each month', 'per gigabyte'],
        ['bike rental shops', 'Shop A', 'Shop B', 'hours', 'to rent a bike', 'per hour'], ['music schools', 'School A', 'School B', 'lessons', 'to sign up', 'per lesson']]);
      const r1 = r.int(4, 30), r2 = r.int(2, r1 - 2), nn = r.int(2, 15), F1 = r.int(0, 60), F2 = F1 + nn * (r1 - r2);
      if (F2 > 400) continue; const cost = F1 + r1 * nn;
      const u1 = unit.split(' ')[0];
      return { kind, text: `Two ${what} have different prices. ${A} charges $${F1} ${fee} plus $${r1} ${per}. ${B} charges $${F2} ${fee} plus $${r2} ${per}. For how many ${unit} do they cost the same, and what is that cost? Which one costs less for more ${unit} than that?`,
        vars: `n = number of ${u1}, c = total cost in dollars`, sys: [`c = ${lin(r1, F1, 'n')}`, `c = ${lin(r2, F2, 'n')}`], env: { n: nn, c: cost },
        a: `${nn} ${u1} at $${cost}; ${B} costs less after that`, d: { F1, r1, F2, r2, B } };
    }
  }
  for (let t = 0; t < 300; t++) {   // travel with and against a current or wind
    const boat = r.chance(.5), b = boat ? r.int(8, 25) : r.int(20, 60) * 10, c = boat ? r.int(1, 6) : r.int(2, 9) * 10, t1 = r.int(2, 5);
    const D = (b + c) * t1; if (D % (b - c)) continue; const t2 = D / (b - c); if (t2 > 9 || t2 === t1) continue;
    const s = boat ? ['boat', 'downstream', 'upstream', 'current', 'in still water'] : ['plane', 'with the wind', 'against the wind', 'wind', 'in still air'];
    return { kind: 'travel', text: `A ${s[0]} travels ${comma(D)} miles ${s[1]} in ${t1} hours. The trip back ${s[2]} takes ${t2} hours. Find the speed of the ${s[0]} ${s[4]} and the speed of the ${s[3]}.`,
      vars: `s = speed of the ${s[0]} ${s[4]}, w = speed of the ${s[3]}, in miles per hour`, sys: [`${t1}(s + w) = ${D}`, `${t2}(s − w) = ${D}`], env: { s: b, w: c },
      a: `${s[0]} ${b} mph, ${s[3]} ${c} mph`, d: { D, t1, t2 } };
  }
}
function skSysWord(r, n, story) {
  const kinds = story === 'mix' ? ['tickets', 'mixture', 'plans', 'travel'] : [story];
  const order = Array.from({ length: n }, (_, i) => kinds[i % kinds.length]);
  const ps = []; const seen = new Set();
  for (const kd of r.shuffle(order)) { const p = r.distinct(1, () => { const x = sysStory(r, kd); return x && !seen.has(x.text) ? x : null; }, x => x.text)[0]; if (p) { seen.add(p.text); ps.push(p); } }
  const items = [], blocks = [];
  ps.forEach((p, i) => {
    items.push({ k: 'story', q: p.text, a: p.a, sys: p.sys, env: p.env, kind: p.kind, d: p.d });
    blocks.push(`<div class="al-story"><p><span class="ws-num">${i + 1}.</span> ${esc(p.text)}</p>
<p class="al-row">Let ${H2('______ = ______', p.vars)}</p><p class="al-row">System: ${keyspan(sys(p.sys[0], p.sys[1]))}</p><div class="al-work" style="min-height:.9in"></div><p class="al-row">Answer: ${ab(p.a, 18)}</p></div>`);
  });
  return {
    ican: 'I can write a system of equations for a real situation, solve it and say what the solution means.',
    directions: 'For each problem, say what each variable stands for, write a system of two equations, solve it, and answer in a sentence with units.',
    ex: example('Tickets: a + s = 100 and 8a + 5s = 650. Multiply the first by 5 and subtract: 3a = 150, so a = 50 and s = 50.', 'Answer: 50 adult and 50 student tickets. Check: 50 + 50 = 100 and 8(50) + 5(50) = 650.'),
    parts: [part('Problems', blocks.join(''))], items,
    mistakes: 'Using one variable for two different amounts, mixing up the two prices, and writing percents as whole numbers in a mixture equation (25% is 0.25).',
    notes: 'The key gives one way to name the variables. Any clear names work if the system matches them.',
  };
}
const keyspan = html => `<span class="ws-blank al-sysblank"><span class="ws-ans">${html}</span></span>`;
const H2 = (blankText, ans) => `<span class="ws-blank" style="min-width:18em"><span class="ws-ans">${F(ans)}</span></span>`;

function ineqText(L) { return `y ${L.rel} ${sum([[L.m, 'x'], [L.b, '']])}`; }
function skSysIneq(r, n) {
  const blocks = [], items = [];
  const one = () => {
    const mk = () => { const q = r.pick([1, 1, 2]), p = r.int(-3, 3); if (q === 2 && p % 2 === 0) return null; return { m: Q(p, q), b: r.int(-5, 5), rel: r.pick(['<', '≤', '>', '≥']) }; };
    const L1 = mk(), L2 = mk(); if (!L1 || !L2 || L1.m.n * L2.m.d === L2.m.n * L1.m.d) return null;
    let poly = [[-8, -8], [8, -8], [8, 8], [-8, 8]];
    for (const L of [L1, L2]) { const m = qv(L.m), below = L.rel === '<' || L.rel === '≤'; poly = below ? clipPoly(poly, -m, 1, L.b) : clipPoly(poly, m, -1, -L.b); }
    let area = 0; for (let i = 0; i < poly.length; i++) { const [a, b] = poly[i], [c, d] = poly[(i + 1) % poly.length]; area += a * d - b * c; }
    if (Math.abs(area) / 2 < 20 || Math.abs(area) / 2 > 200) return null;
    const ok = (x, y, L) => { const v = y - qv(L.m) * x - L.b; return { '<': v < 0, '≤': v <= 0, '>': v > 0, '≥': v >= 0 }[L.rel]; };
    const on = (x, y) => [L1, L2].some(L => Math.abs(y - qv(L.m) * x - L.b) < 0.3);
    const tests = r.distinct(4, () => { const x = r.int(-7, 7), y = r.int(-7, 7); return on(x, y) ? null : [x, y]; }, p => p.join());
    if (tests.length < 4) return null;
    const ins = tests.map(([x, y]) => ok(x, y, L1) && ok(x, y, L2));
    if (ins.every(Boolean) || !ins.some(Boolean)) return null;
    return { L1, L2, poly, tests, ins, e: [ineqText(L1), ineqText(L2)] };
  };
  const ss = r.distinct(n, one, s => s.e.join('|'));
  ss.forEach((s, i) => {
    const svg = plane({ xlo: -8, xhi: 8, S: 12 }, g => `<g class="ws-ans"><polygon points="${s.poly.map(([x, y]) => `${g.X(x)},${g.Y(y)}`).join(' ')}" fill="${RED}" fill-opacity="0.16" stroke="none"/>` +
      [s.L1, s.L2].map(L => lineMark(g, qv(L.m), L.b, RED, L.rel === '<' || L.rel === '>')).join('') + '</g>', 'Empty coordinate grid from −8 to 8 for graphing the system of inequalities');
    const rows = s.tests.map(([x, y], j) => { const a = s.ins[j] ? 'yes' : 'no'; items.push({ k: 'ineqpt', q: `System ${i + 1}: ${s.e.join(', ')} at ${pt(x, y)}`, a, ineqs: s.e, x, y });
      return `<p>${F(pt(x, y))}: ${ab(a, 3)}</p>`; }).join('');
    blocks.push(`<div class="al-side"><div>${svg}</div><div><p><span class="ws-num">${i + 1}.</span> Graph ${sys(s.e[0], s.e[1])}</p><p>Shade where both are true. Is each point a solution?</p>${rows}</div></div>`);
  });
  return {
    ican: 'I can graph a system of linear inequalities, shade its solution region and test points.',
    directions: 'Graph each boundary line: dashed for &lt; or &gt;, solid for ≤ or ≥. Shade the side that makes each inequality true, and find where the shading overlaps. Then test each point in both inequalities: write yes if it is a solution, no if it is not.',
    ex: example('y &lt; x + 1 and y ≥ −2: draw y = x + 1 dashed and shade below it; draw y = −2 solid and shade above it.', 'Test (2, 0): 0 &lt; 3 is true and 0 ≥ −2 is true, so yes. Test (−4, 0): 0 &lt; −3 is false, so no.'),
    parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Shading the wrong side when the inequality says y &gt; (shade above), using a solid line for a strict inequality, and testing a point in only one inequality.',
    notes: 'No test point sits on a boundary line, so every answer is a clear yes or no. The key shades the overlap.',
  };
}

/* ---------- functions ---------- */
function skFnNotation(r, n) {
  const nf = Math.ceil(n / 2), letters = r.shuffle(['f', 'g', 'h', 'p', 'k', 'q']), items = [], cells = [];
  const kinds = r.shuffle(['lin', 'quad', 'expo', 'rat', 'sqrt', 'lin2']).slice(0, nf);
  kinds.forEach((kd, i) => {
    const f = letters[i]; let rule, ins, extra = null;
    if (kd === 'lin' || kd === 'lin2') { const a = nz(r, -6, 6), b = nz(r, -10, 10); rule = lin(a, b); ins = r.sample([-4, -3, -2, -1, 0, 2, 3, 5, 6, 10], 2);
      extra = kd === 'lin2' ? { solve: a * r.int(-6, 8) + b } : { expr: r.int(1, 4) }; }
    else if (kd === 'quad') { rule = poly([nz(r, -9, 9), r.int(-6, 6), r.pick([1, 1, -1, 2])]); ins = r.sample([-3, -2, -1, 1, 2, 3, 4], 2); }
    else if (kd === 'expo') { const c = r.int(1, 5), b = r.pick([2, 3]); rule = `${c === 1 ? '' : c + ' · '}${b}ˣ`; ins = r.sample([0, 1, 2, 3, -1], 2); }
    else if (kd === 'rat') { const c = r.int(-3, 4), k = r.pick([12, 24, 36]); rule = `${k}/(${fac(-c)})`; ins = r.sample([1, 2, 4, 6, 10].map(t => t - c), 2); }
    else { const c = r.int(-4, 6); rule = `√(${fac(-c)})`; ins = r.sample([1, 4, 9, 16, 25, 36].map(t => t - c), 2); }
    const asks = ins.map(x => ({ q: `${f}(${num(x)})`, a: qT(evQ(rule, x)) }));
    if (extra && extra.solve != null) asks[1] = { q: `${f}(x) = ${num(extra.solve)}`, a: `x = ${qT(Q(extra.solve - pval([0], 0) - evB(rule), evA(rule)))}`, solve: extra.solve };
    if (extra && extra.expr) { const k = extra.expr, A = evA(rule), B = evB(rule); asks[1] = { q: `${f}(a + ${k})`, a: lin(A, A * k + B, 'a'), expr: k }; }
    const heads = asks.map(s => s.solve != null ? `Find x when ${F(s.q)}.` : `Find ${F(s.q)}.`);
    asks.forEach(s => items.push({ k: 'fn', q: `${f}(x) = ${rule}; ${s.q}`, a: s.a, rule, ask: s.q, solve: s.solve, expr: s.expr }));
    cells.push(cell(i + 1, `${F(`${f}(x) = ${rule}`)}`, 0, asks.map((s, j) => `<p>${'ab'[j]}. ${heads[j]}</p><div class="al-work" style="min-height:.4in"></div><p class="al-ans">${ab(s.a, 5)}</p>`).join('')));
  });
  // a context: cell growth
  const N0 = r.pick([25, 40, 50, 60, 75, 100, 120, 150, 200]), b = r.pick([2, 2, 3]), t1 = r.int(2, 4), t2 = r.int(t1 + 1, 6), word = b === 2 ? 'doubles' : 'triples';
  const C = t => N0 * b ** t, model = `C(t) = ${N0} · ${b}ᵗ`;
  const ctx = [
    { q: `Find C(${t1}). What does it mean?`, a: `C(${t1}) = ${comma(C(t1))}: after ${t1} hours there are ${comma(C(t1))} cells.`, t: t1, v: C(t1) },
    { q: `What does C(0) = ${N0} tell you?`, a: `At the start (0 hours) there are ${N0} cells.`, t: 0, v: N0 },
    { q: `Solve C(t) = ${comma(C(t2))}. What does it mean?`, a: `t = ${t2}: the sample reaches ${comma(C(t2))} cells after ${t2} hours.`, t: t2, v: C(t2) },
  ];
  ctx.forEach(c => items.push({ k: 'ctx', q: `${model}; ${c.q}`, a: c.a, N0, b, t: c.t, v: c.v }));
  const ctxHtml = `<p>A lab grows cells in a dish. The number of cells ${word} every hour, and ${F(model)} gives the number of cells after <i>t</i> hours.</p>` +
    ctx.map((c, j) => `<p><span class="ws-num">${nf + j + 1}.</span> ${F(c.q)}</p>${lines(1)}${keyp(F(c.a))}`).join('');
  return {
    ican: 'I can evaluate functions written in function notation and explain what a statement like f(3) = 12 means in context.',
    directions: 'Evaluate each function at the input given, or find the input that gives the output. Then use the cell growth model to answer in sentences.',
    ex: example('f(x) = 2x² − 3. f(−2) = 2(−2)² − 3 = 2(4) − 3 = 5.', 'f(−2) = 5 means: when the input is −2, the output is 5. It is a point (−2, 5) on the graph.'),
    parts: [part('Evaluate', grid(cells)), part('In context', ctxHtml)], items,
    mistakes: 'Reading f(3) as f times 3, squaring a negative input without parentheses (−2² instead of (−2)²), and swapping input and output when interpreting.',
  };
}
// value of a rule at a whole number x, exactly
function evQ(rule, x) { const v = evR(rule, { x }); for (let d = 1; d <= 64; d++) if (Math.abs(v * d - Math.round(v * d)) < 1e-9) return Q(Math.round(v * d), d); throw new Error('not rational'); }
const evB = rule => Math.round(evR(rule, { x: 0 })), evA = rule => Math.round(evR(rule, { x: 1 }) - evR(rule, { x: 0 }));

function skRate(r, n) {
  const items = [], cells = [], names = ['f', 'g', 'h', 'k', 'p', 'q'];
  const kinds = Array.from({ length: n }, (_, i) => i % 2 ? 'graph' : 'table');
  kinds.forEach((kd, i) => {
    const f = names[i]; let rule, xs, html;
    if (kd === 'table') {
      if (r.chance(.5)) { const c = r.int(1, 5), b = r.pick([2, 3]); rule = `${c === 1 ? '' : c + ' · '}${b}ˣ`; xs = b === 2 ? [0, 1, 2, 3, 4, 5] : [0, 1, 2, 3, 4]; }
      else { const a = r.pick([1, -1, 2, -2]), h = r.int(-1, 3), k = r.int(-6, 6); rule = `${a === 1 ? '' : a === -1 ? MIN : num(a)}(${fac(h)})² ${k < 0 ? MIN : '+'} ${Math.abs(k)}`.replace(/ \+ 0$/, ''); xs = [-1, 0, 1, 2, 3, 4, 5]; }
      html = htable([['x', ...xs.map(num)], [`${f}(x)`, ...xs.map(x => qT(evQ(rule, x)))]]);
    } else {
      const a = r.pick([1, -1]), h = r.int(-1, 4), k = a > 0 ? r.int(-6, 0) : r.int(1, 7);
      rule = `${a === 1 ? '' : MIN}(${fac(h)})² ${k < 0 ? MIN : '+'} ${Math.abs(k)}`.replace(/ \+ 0$/, '');
      xs = [h - 3, h - 2, h - 1, h, h + 1, h + 2, h + 3];
      const ys = xs.map(x => evR(rule, { x })), ylo = Math.min(...ys, 0) - 1, yhi = Math.max(...ys, 0) + 1;
      html = plane({ xlo: Math.min(h - 3, 0) - 1, xhi: Math.max(h + 3, 0) + 1, ylo, yhi, S: 12 }, g => curveMark(g, x => evR(rule, { x }), '#222', h - 3.2, h + 3.2) + xs.map((x, j) => dot(g, x, ys[j])).join(''), `Graph of a parabola through ${xs.map((x, j) => pt(x, ys[j])).join(', ')}`);
    }
    const ivs = r.distinct(2, () => { const [a, b] = r.sample(xs, 2).sort((p, q) => p - q); return [a, b]; }, p => p.join());
    const rows = ivs.map(([a, b]) => { const v = qT(Q(evQ(rule, b).n * evQ(rule, a).d - evQ(rule, a).n * evQ(rule, b).d, (b - a) * evQ(rule, a).d * evQ(rule, b).d));
      items.push({ k: 'rate', q: `${f}: ${rule} from ${a} to ${b}`, a: v, rule, x1: a, x2: b });
      return `<p>From x = ${num(a)} to x = ${num(b)}: ${ab(v, 4)}</p>`; }).join('');
    cells.push(cell(i + 1, `The ${kd === 'table' ? 'table' : 'graph'} shows <i>y</i> = ${F(`${f}(x)`)}.`, 0, `${html}${rows}`, kd === 'graph' ? ' al-graph' : ''));
  });
  return {
    ican: 'I can find the average rate of change of a function over an interval from a table or a graph.',
    directions: 'For each interval, find the average rate of change: the change in the output divided by the change in the input. Give fractions in simplest form.',
    ex: example('f(1) = 3 and f(4) = 18. Average rate of change from x = 1 to x = 4: (18 − 3)/(4 − 1) = 15/3 = 5.', 'On average, the output goes up 5 for each 1 the input goes up on that interval.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Dividing the change in x by the change in y, subtracting the outputs in a different order than the inputs, and using a single point instead of the two ends of the interval.',
  };
}

function skLinExp(r, n) {
  const types = r.shuffle(Array.from({ length: n }, (_, i) => i % 2 ? 'exp' : 'lin'));
  const items = [], cells = [], seen = new Set();
  types.forEach((t, i) => {
    const one = () => {
      if (t === 'lin') { const m = nz(r, -8, 8), b = r.int(-10, 25); return { rule: siT(Q(m), b).slice(4), type: 'linear' }; }
      const B = r.pick([2, 3, 4, '1/2', '1/3', '3/2']);
      const c = { 2: r.int(1, 6), 3: r.int(1, 4), 4: r.int(1, 3), '1/2': r.pick([16, 32, 48, 64, 80]), '1/3': r.pick([81, 162]), '3/2': r.pick([16, 32, 48]) }[B];
      return { rule: typeof B === 'number' ? `${c === 1 ? '' : c + ' · '}${B}ˣ` : `${c}(${B})ˣ`, type: 'exponential' };
    };
    const f = r.distinct(1, () => { const x = one(); return seen.has(x.rule) ? null : x; }, x => x.rule)[0]; seen.add(f.rule);
    const xs = [0, 1, 2, 3, 4], ys = xs.map(x => qT(evQ(f.rule, x)));
    const a = `${f.type}; y = ${f.rule}`;
    items.push({ k: 'linexp', q: `Table ${xs.map((x, j) => `(${x}, ${ys[j]})`).join(' ')}`, a, xs, ys });
    cells.push(cell(i + 1, 'Linear or exponential?', 0, `${htable([['x', ...xs.map(String)], ['y', ...ys]])}<p>Type: ${ab(f.type, 6)}</p><p>Function: ${ab('y = ' + f.rule, 8)}</p>`));
  });
  return {
    ican: 'I can tell a linear table from an exponential one by its differences or ratios, and write its function.',
    directions: 'Find the difference between each y-value and the next, and the ratio of each y-value to the one before. Constant differences mean linear (y = mx + b); constant ratios mean exponential (y = a · bˣ). Write the function.',
    ex: example('y: 3, 6, 12, 24, 48. Differences 3, 6, 12, 24 change; ratios are all 2. Exponential: y = 3 · 2ˣ (3 is the value at x = 0).', 'y: 7, 4, 1, −2, −5. Differences are all −3: linear, y = −3x + 7.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Calling a table linear because it goes up by the same amount at first, using the y-value at x = 1 as the starting value, and writing a decay factor of 2 instead of 1/2.',
  };
}

function skFnOrNot(r, n) {
  const items = [], cards = [], expl = [];
  const kinds = r.shuffle(Array.from({ length: n }, (_, i) => ['table', 'map', 'graph'][i % 3]));
  const yes = r.shuffle(Array.from({ length: n }, (_, i) => i % 2 === 0));
  kinds.forEach((kd, i) => {
    let xs = r.sample([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6], kd === 'graph' ? 5 : 4), ys = xs.map(() => r.int(-4, 7));
    if (!yes[i]) { const j = r.int(1, xs.length - 1); xs[j] = xs[r.int(0, j - 1)]; while (ys[j] === ys[xs.indexOf(xs[j])]) ys[j] = r.int(-4, 7); }
    const pairs = xs.map((x, j) => [x, ys[j]]);
    if (kd === 'graph') { const seen = new Set(); for (const p of pairs) { const k = p.join(); if (seen.has(k)) p[1] = p[1] + 1; seen.add(p.join()); } }
    const isF = pairs.every(([x, y]) => pairs.every(([x2, y2]) => x !== x2 || y === y2));
    const ans = isF ? 'function' : 'not a function';
    let html;
    if (kd === 'table') html = htable([['x', ...pairs.map(p => num(p[0]))], ['y', ...pairs.map(p => num(p[1]))]]);
    else if (kd === 'graph') html = plane({ xlo: -4, xhi: 7, ylo: -5, yhi: 8, S: 10, every: 4 }, g => pairs.map(([x, y]) => dot(g, x, y)).join(''), `Points ${pairs.map(p => pt(...p)).join(', ')}`);
    else {
      const ins = [...new Set(pairs.map(p => p[0]))], outs = [...new Set(pairs.map(p => p[1]))], h = 26, top = 22, Yi = j => top + j * h, Yo = j => top + j * h;
      let s = `<ellipse cx="40" cy="${top + (ins.length - 1) * h / 2}" rx="26" ry="${ins.length * h / 2 + 8}" fill="none" stroke="#222"/><ellipse cx="160" cy="${top + (outs.length - 1) * h / 2}" rx="26" ry="${outs.length * h / 2 + 8}" fill="none" stroke="#222"/>`;
      s += `<defs><marker id="alarr${++UID}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#222"/></marker></defs>`;
      ins.forEach((x, j) => { s += `<text x="40" y="${Yi(j) + 4}" ${FONT} font-size="12" text-anchor="middle">${num(x)}</text>`; });
      outs.forEach((y, j) => { s += `<text x="160" y="${Yo(j) + 4}" ${FONT} font-size="12" text-anchor="middle">${num(y)}</text>`; });
      const done = new Set();
      pairs.forEach(([x, y]) => { const k = x + ',' + y; if (done.has(k)) return; done.add(k); s += `<line x1="52" y1="${Yi(ins.indexOf(x))}" x2="146" y2="${Yo(outs.indexOf(y))}" stroke="#222" stroke-width="1.3" marker-end="url(#alarr${UID})"/>`; });
      const Ht = top + Math.max(ins.length, outs.length) * h + 6;
      html = `<svg class="gen-svg" viewBox="0 0 200 ${Ht}" role="img" aria-label="Mapping diagram ${pairs.map(p => `${p[0]} to ${p[1]}`).join(', ')}" style="max-width:2.1in">${s}</svg>`;
    }
    items.push({ k: 'fnornot', q: `Card ${i + 1} ${kd}: ${pairs.map(p => pt(...p)).join(' ')}`, a: ans, pairs });
    cards.push(`<div class="al-card"><p><span class="ws-num">${i + 1}.</span> ${kd === 'table' ? 'Table' : kd === 'map' ? 'Mapping' : 'Graph'}</p>${html}<p>${ab(ans, 6.5)}</p></div>`);
  });
  const pickF = items.findIndex(it => it.a === 'function'), pickN = items.findIndex(it => it.a !== 'function');
  for (const j of [pickN, pickF].filter(j => j >= 0)) {
    const it = items[j], dup = it.pairs.find(([x, y]) => it.pairs.some(([x2, y2]) => x === x2 && y !== y2));
    const why = dup ? `Card ${j + 1} is not a function: the input ${num(dup[0])} has two outputs, ${it.pairs.filter(p => p[0] === dup[0]).map(p => num(p[1])).filter((v, k, a) => a.indexOf(v) === k).join(' and ')}.`
      : `Card ${j + 1} is a function: each input has exactly one output.`;
    items.push({ k: 'why', q: `Explain card ${j + 1}`, a: why, pairs: it.pairs, card: j + 1 });
    expl.push(`<p>Card ${j + 1}: Each input ${'_'.repeat(28)}</p>${lines(1)}${keyp(F(why))}`);
  }
  return {
    ican: 'I can decide whether a table, mapping or graph shows a function, and explain why.',
    directions: 'Cut out the cards and sort them into two piles: function and not a function. A relation is a function when each input (x) has exactly one output (y). Write your choice on each card, then explain two cards.',
    ex: example('Inputs 1, 2, 3 with outputs 5, 5, 7: a function (two inputs can share an output).', 'Inputs 1, 1, 2 with outputs 4, 6, 8: not a function, because the input 1 has two outputs.'),
    parts: [part('Cards', `<div class="al-cards">${cards.join('')}</div>`), part('Explain two cards', expl.join(''))], items,
    mistakes: 'Calling a relation "not a function" because two inputs share an output, and checking the outputs for repeats instead of the inputs. On a graph, two points straight above each other mean not a function.',
  };
}

/* ---------- polynomials ---------- */
const termsOf = cs => cs.map((c, p) => [c, p]).filter(([c]) => c).reverse();
const termText = (c, p) => sum([[c, mono('x', p)]]);
function skPolyMul(r, n) {
  const items = [], cells = [];
  const ps = r.distinct(n, () => {
    const T = r.pick(['bb', 'bb', 'bb', 'sq', 'bt']);
    const a1 = r.pick([1, 1, 2, 3]), b1 = nz(r, -7, 7);
    if (T === 'sq') { const f = [b1, a1]; return { q: `(${poly(f)})²`, A: f, B: f }; }
    if (T === 'bb') { const a2 = r.pick([1, 1, 2, 3, 4]), b2 = nz(r, -8, 8); const A = [b1, a1], B = [b2, a2]; return { q: `(${poly(A)})(${poly(B)})`, A, B }; }
    const A = [b1, r.pick([1, 1, 2])], B = [nz(r, -6, 6), nz(r, -5, 5), 1]; return { q: `(${poly(A)})(${poly(B)})`, A, B };
  }, x => x.q);
  ps.forEach((p, i) => {
    const prod = pmul(p.A, p.B), ans = poly(prod), tA = termsOf(p.A), tB = termsOf(p.B);
    const box = `<table class="al-box"><tr><th></th>${tA.map(([c, e]) => `<th>${F(termText(c, e))}</th>`).join('')}</tr>${tB.map(([c2, e2]) => `<tr><th>${F(termText(c2, e2))}</th>${tA.map(([c, e]) => `<td><span class="ws-ans">${F(termText(c * c2, e + e2))}</span></td>`).join('')}</tr>`).join('')}</table>`;
    items.push({ k: 'poly', q: p.q, a: ans, cells: tB.flatMap(([c2, e2]) => tA.map(([c, e]) => [termText(c, e), termText(c2, e2), termText(c * c2, e + e2)])) });
    cells.push(cell(i + 1, `${F(p.q)}`, 0, `${box}<p>= ${ab(ans, 9)}</p>`));
  });
  const xv = r.pick([2, 3, -1]), chk = ps.slice(0, 2).map((p, j) => { const v = num(pval(pmul(p.A, p.B), xv));
    items.push({ k: 'polycheck', q: `Check ${j + 1} at x = ${xv}`, a: v, expr: p.q, x: xv });
    return `<p><span class="ws-num">${j + 1}.</span> Problem ${j + 1} at x = ${num(xv)}: the product is ${ab(v, 3)}, and your answer is ${ab(v, 3)}.</p>`; }).join('');
  return {
    ican: 'I can multiply polynomials with an area model and check the product by substituting a number.',
    directions: 'Put the terms of one factor across the top of the box and the other down the side. Multiply to fill each cell, then add like terms to write the product. Then check two problems by substituting the same number for x into the question and your answer.',
    ex: example('(2x + 3)(x − 4): the cells are 2x², −8x, 3x and −12.', 'Add like terms: 2x² − 8x + 3x − 12 = 2x² − 5x − 12.'),
    parts: [part('Practice', grid(cells)), part('Check by substitution', `${chk}<p>If the two numbers match, the product is very likely right.</p>`)], items,
    mistakes: 'Losing the sign of a negative term in the box, adding exponents wrong (x · x is x², not 2x), and squaring a binomial as only the two squares: (x + 3)² is x² + 6x + 9.',
  };
}

function skFactor(r, n) {
  const items = [], cards = [];
  const types = r.shuffle(Array.from({ length: n }, (_, i) => ['gcf', 'tri', 'dos'][i % 3]));
  const gcdAll = cs => cs.filter(Boolean).reduce((g, c) => gcd(g, c), 0);
  const make1 = t => {
    if (t === 'gcf') {
      const g = r.int(2, 8), e = r.int(0, 2);
      let inner;
      if (r.chance(.5)) { const k = r.int(1, 2), a = r.int(1, 6), b = nz(r, -9, 9); inner = Array(k + 1).fill(0); inner[0] = b; inner[k] = a;
        if (k === 2 && b < 0 && isSq(a) && isSq(-b)) return null; }
      else { const a = r.int(1, 4), b = nz(r, -9, 9), c = nz(r, -9, 9); if (isSq(b * b - 4 * a * c)) return null; inner = [c, b, a]; }
      if (gcdAll(inner) !== 1) return null;
      const cs = Array(e).fill(0).concat(inner.map(c => c * g));
      return { cs, f: `${g}${mono('x', e)}(${poly(inner)})`, m: 'GCF', g: `${g}${mono('x', e)}` };
    }
    if (t === 'tri') { const a = r.pick([1, 1, 1, 2, 3, 5]), p = nz(r, -9, 9), q = nz(r, -9, 9); if (gcd(a, Math.abs(p)) !== 1 || p + a * q === 0) return null;
      const cs = pmul([p, a], [q, 1]); const f1 = `(${poly([p, a])})`, f2 = `(${poly([q, 1])})`;
      return { cs, f: a === 1 && p === q ? `${f1}²` : a === 1 && p > q ? f2 + f1 : f1 + f2, m: 'trinomial' }; }
    const a = r.int(1, 5), b = r.int(1, 12); if (gcd(a, b) !== 1) return null;
    return { cs: [-b * b, 0, a * a], f: `(${poly([-b, a])})(${poly([b, a])})`, m: 'difference of squares' };
  };
  const seen = new Set(), list = [];
  for (const t of types) { const c = r.distinct(1, () => { const x = make1(t); return x && !seen.has(poly(x.cs)) ? x : null; }, x => poly(x.cs))[0]; if (c) { seen.add(poly(c.cs)); list.push(c); } }
  list.forEach((c, i) => {
    const q = poly(c.cs);
    items.push({ k: 'factor', q, a: `${c.m}: ${c.f}`, cs: c.cs });
    cards.push(`<div class="al-card"><p><span class="ws-num">${i + 1}.</span> <b>${F(q)}</b></p><p>Method: ${ab(c.m, 7)}</p><p>${ab(c.f, 8)}</p></div>`);
  });
  return {
    ican: 'I can choose a factoring method (greatest common factor, trinomial or difference of squares) and factor an expression.',
    directions: 'Cut out the cards. First sort them by method: GCF, trinomial, or difference of squares. Write the method on each card, then factor the expression completely.',
    ex: example('GCF: 6x² + 9x = 3x(2x + 3). Trinomial: x² + 5x + 6 = (x + 2)(x + 3).', 'Difference of squares: 4x² − 25 = (2x − 5)(2x + 5). Check any answer by multiplying it back out.'),
    parts: [part('Task cards', `<div class="al-cards">${cards.join('')}</div>`)], items,
    mistakes: 'Taking out a common factor that is not the greatest one, factoring a sum of squares (x² + 9 does not factor), and sign mix-ups in a trinomial with a negative constant.',
    notes: 'Each card needs exactly one method: the trinomials and differences of squares have no common factor, and what is left inside a GCF card does not factor further.',
  };
}

/* ---------- quadratics ---------- */
const eqZero = cs => `${poly(cs)} = 0`;
function skQFactor(r, n) {
  const items = [], cells = [], steps = [];
  const ps = r.distinct(n, () => {
    const T = r.pick(['monic', 'monic', 'nonmonic', 'move', 'gcf', 'double', 'dos']);
    const p = nz(r, -9, 9), q = nz(r, -9, 9);
    if (T === 'monic') { if (p === q) return null; const cs = pmul([-p, 1], [-q, 1]); return { eq: eqZero(cs), cs, fz: `(${fac(p)})(${fac(q)}) = 0` }; }
    if (T === 'nonmonic') { const a = r.int(2, 5), pp = nz(r, -7, 7); if (gcd(a, Math.abs(pp)) !== 1) return null; const cs = pmul([-pp, a], [-q, 1]); return { eq: eqZero(cs), cs, fz: `(${poly([-pp, a])})(${fac(q)}) = 0` }; }
    if (T === 'move') { if (p === q) return null; const cs = pmul([-p, 1], [-q, 1]); if (!cs[1]) return null;
      return r.chance(.5) ? { eq: `x² = ${poly([-cs[0], -cs[1]])}`, cs, fz: `(${fac(p)})(${fac(q)}) = 0` } : { eq: `${poly([0, cs[1], 1])} = ${num(-cs[0])}`, cs, fz: `(${fac(p)})(${fac(q)}) = 0` }; }
    if (T === 'gcf') { const a = r.int(1, 4); const cs = [0, -a * p, a]; return { eq: eqZero(cs), cs, fz: `${a === 1 ? '' : a}x(${fac(p)}) = 0` }; }
    if (T === 'double') { const cs = pmul([-p, 1], [-p, 1]); return { eq: eqZero(cs), cs, fz: `(${fac(p)})² = 0` }; }
    const k = r.int(2, 12); return { eq: `x² ${MIN} ${k * k} = 0`, cs: [-k * k, 0, 1], fz: `(${fac(k)})(${fac(-k)}) = 0` };
  }, x => x.eq);
  ps.forEach((p, i) => { const a = quadText(p.cs[2], p.cs[1], p.cs[0]);
    items.push({ k: 'quad', q: p.eq, a }); steps.push(`${F(p.fz)}, so ${F(a)}`);
    cells.push(cell(i + 1, `Solve ${F(p.eq)}.`, 0.75, ab(a, 7))); });
  return {
    ican: 'I can solve a quadratic equation by factoring and using the zero product property.',
    directions: 'Get 0 on one side, factor, and set each factor equal to 0. Write every solution, then check each one in the original equation. If both factors are the same, there is one solution.',
    ex: example('x² − 2x = 15 → x² − 2x − 15 = 0 → (x − 5)(x + 3) = 0.', 'So x − 5 = 0 or x + 3 = 0: x = −3, x = 5. Check: 25 − 10 = 15 and 9 + 6 = 15.'),
    parts: [part('Practice', grid(cells))], items,
    teacher: `<h3>Factored forms</h3><ol class="al-steps">${steps.map(s => `<li>${s}</li>`).join('')}</ol>`,
    mistakes: 'Factoring before moving every term to one side, dividing both sides by x (which loses the solution x = 0), and giving the numbers in the factors instead of their opposites.',
  };
}
function skQSquare(r, n) {
  const items = [], cells = [], steps = [];
  const ps = r.distinct(n, () => {
    const T = r.pick(['sq', 'sq', 'sqm', 'plain', 'cs', 'cs', 'cs']), h = nz(r, -8, 8);
    if (T === 'sq' || T === 'sqm') { const K = r.chance(.5) ? r.int(1, 9) ** 2 : r.int(2, 60), m = T === 'sqm' ? r.int(2, 4) : 1;
      const cs = pscale(padd(pmul([-h, 1], [-h, 1]), [-K]), m);
      return { eq: `${m === 1 ? '' : m}(${fac(h)})² = ${m * K}`, cs, st: `(${fac(h)})² = ${K}` }; }
    if (T === 'plain') { const k = r.int(2, 6), m = r.pick([2, 3, 5, 6, 7]); return { eq: `x² = ${k * k * m}`, cs: [-k * k * m, 0, 1], st: `x = ±√${k * k * m}` }; }
    const c = r.int(-12, 12), D4 = h * h - c; if (D4 <= 0) return null;
    const cs = [c, -2 * h, 1];
    return r.chance(.5) ? { eq: eqZero(cs), cs, st: `(${fac(h)})² = ${D4}` } : { eq: `${poly([0, -2 * h, 1])} = ${num(-c)}`, cs, st: `(${fac(h)})² = ${D4}` };
  }, x => x.eq);
  ps.forEach((p, i) => { const a = quadText(p.cs[2], p.cs[1], p.cs[0]);
    items.push({ k: 'quad', q: p.eq, a }); steps.push(`${F(p.st)}, so ${F(a)}`);
    cells.push(cell(i + 1, `Solve ${F(p.eq)}.`, 0.8, ab(a, 7))); });
  return {
    ican: 'I can solve quadratic equations by taking square roots and by completing the square.',
    directions: 'If the equation is a square equal to a number, take the square root of both sides (remember ±). Otherwise complete the square: move the constant, add (b/2)² to both sides, write the square, then take square roots. Simplify radicals.',
    ex: example('x² − 6x − 4 = 0 → x² − 6x = 4 → x² − 6x + 9 = 13 → (x − 3)² = 13.', 'x − 3 = ±√13, so x = 3 ± √13.'),
    parts: [part('Practice', grid(cells))], items,
    teacher: `<h3>Square form of each</h3><ol class="al-steps">${steps.map(s => `<li>${s}</li>`).join('')}</ol>`,
    mistakes: 'Forgetting ±, adding (b/2)² to only one side, and leaving a radical like √12 unsimplified (it is 2√3).',
  };
}
function skQFormula(r, n) {
  const items = [], cells = [];
  const kinds = r.shuffle(Array.from({ length: n }, (_, i) => i < Math.max(1, Math.round(n / 4)) ? 'neg' : i === Math.round(n / 4) + 0 ? 'zero' : 'pos'));
  const seen = new Set();
  for (const kd of kinds) {
    const p = r.distinct(1, () => {
      let a, b, c;
      if (kd === 'zero') { const s = r.int(1, 3), t = nz(r, -6, 6); if (gcd(s, Math.abs(t)) !== 1) return null; [a, b, c] = [s * s, 2 * s * t, t * t]; }
      else { a = r.pick([1, 1, 2, 2, 3, 4, 5, -1, -2]); b = r.int(-9, 9); c = nz(r, -9, 9); }
      const D = b * b - 4 * a * c;
      if (kd === 'neg' && D >= 0) return null; if (kd === 'pos' && (D <= 0 || (isSq(D) && r.chance(.7)))) return null;
      const eq = eqZero([c, b, a]); return seen.has(eq) ? null : { a, b, c, D, eq };
    }, x => x.eq)[0];
    if (!p) continue; seen.add(p.eq);
    const cnt = p.D > 0 ? '2' : p.D === 0 ? '1' : '0', sols = quadText(p.a, p.b, p.c);
    items.push({ k: 'qform', q: p.eq, a: `D = ${num(p.D)}; ${cnt}; ${sols}` });
    cells.push(cell(items.length, `${F(p.eq)}`, 0.85, `<p>Discriminant: ${ab(num(p.D), 3)} Real solutions: ${ab(cnt, 2)}</p><p>${ab(sols, 9)}</p>`));
  }
  return {
    ican: 'I can use the discriminant to predict the number of real solutions and solve with the quadratic formula.',
    directions: 'Find the discriminant b² − 4ac and say how many real solutions there are (positive: 2, zero: 1, negative: 0). Then solve with x = (−b ± √(b² − 4ac))/(2a), giving exact answers with radicals simplified. If there are no real solutions, say so.',
    ex: example('2x² + 3x − 1 = 0: a = 2, b = 3, c = −1. b² − 4ac = 9 + 8 = 17, so 2 real solutions.', 'x = (−3 ± √17)/4.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Using b instead of −b, writing −b² for (−b)² when b is negative, dividing only the radical by 2a, and simplifying (4 ± 2√3)/2 to 2 ± 2√3.',
  };
}
function skForms(r, n) {
  const items = [], blocks = [];
  const ps = r.distinct(n, () => {
    const a = r.pick([1, -1, 2, -2, 1, -1]), p = r.int(-6, 7), q = r.int(-6, 7); if (p >= q || (p + q) % 2) return null;
    const h = (p + q) / 2, k = -a * ((q - p) / 2) ** 2, cs = pscale(pmul([-p, 1], [-q, 1]), a);
    const lead = a === 1 ? '' : a === -1 ? MIN : num(a);
    return { std: `f(x) = ${poly(cs)}`, fz: `f(x) = ${lead}${(q === 0 ? [q, p] : [p, q]).map(z => z === 0 ? 'x' : `(${fac(z)})`).join('')}`, vx: `f(x) = ${lead}${h ? `(${fac(h)})²` : 'x²'}${k ? ` ${k < 0 ? MIN : '+'} ${Math.abs(k)}` : ''}`,
      zeros: p === q ? `x = ${num(p)}` : `x = ${num(p)}, x = ${num(q)}`, vert: `${pt(h, k)}, ${a < 0 ? 'maximum' : 'minimum'}` };
  }, x => x.std);
  ps.forEach((p, i) => {
    items.push({ k: 'forms', q: p.std, a: `${p.fz}; ${p.vx}; ${p.zeros}; ${p.vert}` });
    blocks.push(`<div class="al-story"><p><span class="ws-num">${i + 1}.</span> ${F(p.std)}</p><div class="al-two"><div><p>Factored form: ${ab(p.fz, 10)}</p><div class="al-work" style="min-height:.6in"></div><p>Zeros: ${ab(p.zeros, 7)}</p></div>` +
      `<div><p>Vertex form: ${ab(p.vx, 10)}</p><div class="al-work" style="min-height:.6in"></div><p>Vertex: ${ab(p.vert, 9)}</p></div></div></div>`);
  });
  const why = 'Factored form a(x − p)(x − q) shows the zeros, p and q, right away. Vertex form a(x − h)² + k shows the vertex (h, k), which is the maximum when a is negative and the minimum when a is positive.';
  return {
    ican: 'I can rewrite a quadratic in factored form and vertex form and explain what each form shows.',
    directions: 'Rewrite each quadratic in factored form and in vertex form. Give the zeros, the vertex, and whether the vertex is a maximum or a minimum. Then answer the question at the end.',
    ex: example('f(x) = x² − 6x + 5 = (x − 1)(x − 5), so the zeros are 1 and 5.', 'Complete the square: x² − 6x + 9 − 4 = (x − 3)² − 4. Vertex (3, −4), a minimum because a = 1 is positive.'),
    parts: [part('Practice', blocks.join('')), part('Explain', `<p>Which form shows the zeros? Which shows the maximum or minimum? Explain how you can tell.</p>${lines(3)}${keyp(why)}`)], items,
    mistakes: 'Factoring out the leading coefficient from only some terms, giving the vertex as (−h, k), and calling the vertex a maximum when the parabola opens up.',
  };
}
function skProjectile(r, n) {
  const items = [], blocks = [];
  const CTX = [s => s ? `A ball is thrown straight up from a height of ${s} feet` : 'A ball is kicked straight up from the ground',
    s => s ? `A model rocket is launched from a platform ${s} feet high` : 'A model rocket is launched from the ground',
    s => s ? `A water balloon is tossed upward from a balcony ${s} feet above the ground` : 'A water balloon is tossed straight up from the ground',
    s => s ? `A pebble is flicked upward from the edge of a cliff ${s} feet high` : 'A beanbag is tossed straight up from the ground'];
  const ps = r.distinct(n, () => {
    const v = r.pick([32, 48, 64, 80, 96, 112, 128]), s = r.pick([0, 0, 4, 5, 6, 10, 20, 50, 80, 100, 160]);
    const land = (v + Math.sqrt(v * v + 64 * s)) / 32, f = land * 100 - Math.floor(land * 100);
    if (s && Math.abs(f - 0.5) < 0.02) return null;
    return { v, s, ci: r.int(0, 3), land };
  }, x => `${x.v}/${x.s}`);
  ps.forEach((p, i) => {
    const tm = p.v / 32, hm = p.s + p.v * p.v / 64, land = p.s ? p.land.toFixed(2) : String(p.v / 16);
    const hT = `h = −16t² + ${p.v}t${p.s ? ' + ' + p.s : ''}`;
    const a = `${tm} s; ${hm} ft; ${land} s`;
    items.push({ k: 'proj', q: `${hT} (${i})`, a, v: p.v, s: p.s });
    blocks.push(`<div class="al-story"><p><span class="ws-num">${i + 1}.</span> ${CTX[p.ci](p.s)} with an upward speed of ${p.v} feet per second. Its height in feet after <i>t</i> seconds is ${F(hT)}.</p>` +
      `<div class="al-two"><div><p>a. When does it reach its highest point? ${ab(tm + ' s', 4)}</p><p>b. How high does it go? ${ab(hm + ' ft', 4)}</p></div><div><p>c. When does it hit the ground?${p.s ? ' (Round to the nearest hundredth.)' : ''} ${ab(land + ' s', 4)}</p></div></div><div class="al-work" style="min-height:.9in"></div></div>`);
  });
  return {
    ican: 'I can use a quadratic model to find the maximum height and landing time of a launched object.',
    directions: 'The highest point is at the vertex: t = −b/(2a). Put that time back in to find the height. The object lands when h = 0: solve with the quadratic formula and keep the positive answer.',
    ex: example('h = −16t² + 64t: t = −64/(2 · −16) = 2 s, and h = −16(4) + 64(2) = 64 ft.', 'Landing: −16t² + 64t = 0 → −16t(t − 4) = 0 → t = 4 s (t = 0 is the launch).'),
    parts: [part('Problems', blocks.join(''))], items,
    mistakes: 'Giving the time of the highest point as the height, keeping the negative root of the landing equation, and dropping the starting height s when it is not 0.',
    notes: 'Uses h = −16t² + vt + s, with feet and seconds and no air resistance.',
  };
}

/* ---------- inequalities ---------- */
const FLIP = { '<': '>', '>': '<', '≤': '≥', '≥': '≤' };
function compoundLine(k1, k2, inc1, inc2, or, lo) {
  const x0 = 16, x1 = 316, y = 22, nT = 12, X = t => x0 + (t - lo) * (x1 - x0) / nT;
  let s = `<line x1="${x0 - 10}" y1="${y}" x2="${x1 + 10}" y2="${y}" stroke="#222" stroke-width="1.5"/><path d="M${x0 - 10} ${y} l7 -5 v10 z M${x1 + 10} ${y} l-7 -5 v10 z" fill="#222"/>`;
  for (let t = lo; t <= lo + nT; t++) s += `<line x1="${X(t)}" y1="${y - 6}" x2="${X(t)}" y2="${y + 6}" stroke="#222"/><text x="${X(t)}" y="${y + 20}" ${FONT} font-size="11" text-anchor="middle">${num(t)}</text>`;
  const circ = (t, inc) => `<circle cx="${X(t)}" cy="${y}" r="5.5" fill="${inc ? RED : '#fff'}" stroke="${RED}" stroke-width="2.4"/>`;
  const seg = (a, b) => `<line x1="${a}" y1="${y}" x2="${b}" y2="${y}" stroke="${RED}" stroke-width="5"/>`;
  s += `<g class="ws-ans">${or ? seg(x0 - 8, X(k1)) + seg(X(k2), x1 + 8) : seg(X(k1), X(k2))}${circ(k1, inc1)}${circ(k2, inc2)}</g>`;
  return `<svg class="gen-svg" viewBox="0 0 332 46" role="img" aria-label="Number line from ${lo} to ${lo + nT}" style="max-width:3.3in">${s}</svg>`;
}
function skCompound(r, n) {
  const nl = n >= 8 ? 2 : 1, items = [], cells = [];
  const ps = r.distinct(n - nl, () => {
    const k1 = r.int(-7, 5), k2 = r.int(k1 + 2, Math.min(k1 + 9, 8)), inc1 = r.chance(.5), inc2 = r.chance(.5), or = r.chance(.45);
    const p = nz(r, -4, 5), q = r.int(-9, 9), L = p * k1 + q, U = p * k2 + q, e = lin(p, q), R = i => i ? '≤' : '<';
    let txt;
    if (!or) txt = p > 0 ? `${num(L)} ${R(inc1)} ${e} ${R(inc2)} ${num(U)}` : `${num(U)} ${R(inc2)} ${e} ${R(inc1)} ${num(L)}`;
    else { const p2 = nz(r, -4, 5), q2 = r.int(-9, 9), e2 = lin(p2, q2), r1 = inc1 ? '≤' : '<', r2 = inc2 ? '≥' : '>';
      txt = `${e} ${p > 0 ? r1 : FLIP[r1]} ${num(L)} or ${e2} ${p2 > 0 ? r2 : FLIP[r2]} ${num(p2 * k2 + q2)}`; }
    const iv = or ? `(−∞, ${num(k1)}${inc1 ? ']' : ')'} ∪ ${inc2 ? '[' : '('}${num(k2)}, ∞)` : `${inc1 ? '[' : '('}${num(k1)}, ${num(k2)}${inc2 ? ']' : ')'}`;
    return { txt, iv, k1, k2, inc1, inc2, or };
  }, x => x.txt);
  ps.forEach((p, i) => { items.push({ k: 'compound', q: p.txt, a: p.iv });
    cells.push(cell(i + 1, `${F(p.txt)}`, 0.6, `<p>${ab(p.iv, 8)}</p>${compoundLine(p.k1, p.k2, p.inc1, p.inc2, p.or, Math.round((p.k1 + p.k2) / 2) - 6)}`)); });
  const LIT = [['ax + b < c', 'x < (c − b)/a', '<'], ['ax − b ≥ c', 'x ≥ (c + b)/a', '≥'], ['−ax + b ≤ c', 'x ≥ (b − c)/a', '≥'], ['a(x − b) > c', 'x > c/a + b', '>'], ['b − ax > c', 'x < (b − c)/a', '<']];
  r.sample(LIT, nl).forEach(([q, a], j) => { items.push({ k: 'literal', q: `${q} (a > 0)`, a });
    cells.push(cell(ps.length + j + 1, `Solve for <i>x</i>: ${F(q)}. Assume <i>a</i> &gt; 0.`, 0.6, ab(a, 8))); });
  return {
    ican: 'I can solve compound and literal inequalities, graph them and write them in interval notation.',
    directions: 'Solve each compound inequality, graph it on the number line and write it in interval notation: ( ) for an endpoint that is not included, [ ] for one that is. "And" is the overlap; "or" is both pieces. Solve the literal inequalities for x.',
    ex: example('−3 &lt; 2x + 1 ≤ 7 → −4 &lt; 2x ≤ 6 → −2 &lt; x ≤ 3, which is (−2, 3].', 'x + 2 &lt; 0 or 3x ≥ 12 → x &lt; −2 or x ≥ 4, which is (−∞, −2) ∪ [4, ∞).'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Forgetting to flip both signs when dividing a three-part inequality by a negative, using a bracket next to ∞, and drawing an "or" answer as the piece between the endpoints.',
  };
}

/* ---------- complex numbers ---------- */
const imT = b => b === 1 ? 'i' : b === -1 ? MIN + 'i' : num(b) + 'i';
const cT = (a, b) => !b ? num(a) : !a ? imT(b) : `${num(a)} ${b < 0 ? MIN : '+'} ${Math.abs(b) === 1 ? '' : Math.abs(b)}i`;
function skComplex(r, n) {
  const items = [], cells = [];
  const ps = r.distinct(n, () => {
    const T = r.pick(['add', 'add', 'sub', 'sub', 'mul', 'mul', 'mul', 'mono', 'sq', 'conj']);
    const a = nz(r, -9, 9), b = nz(r, -9, 9), c = nz(r, -9, 9), d = nz(r, -9, 9);
    if (T === 'add') return { q: `(${cT(a, b)}) + (${cT(c, d)})`, re: a + c, im: b + d };
    if (T === 'sub') return { q: `(${cT(a, b)}) ${MIN} (${cT(c, d)})`, re: a - c, im: b - d };
    if (T === 'mono') { const k = nz(r, -6, 6); return r.chance(.5) ? { q: `${imT(k)}(${cT(c, d)})`, re: -k * d, im: k * c } : { q: `${num(k)}(${cT(c, d)})`, re: k * c, im: k * d }; }
    const A = r.int(-6, 6) || 1, B = nz(r, -6, 6), Cc = r.int(-6, 6) || 2, D = nz(r, -6, 6);
    if (T === 'sq') return { q: `(${cT(A, B)})²`, re: A * A - B * B, im: 2 * A * B };
    if (T === 'conj') return { q: `(${cT(A, B)})(${cT(A, -B)})`, re: A * A + B * B, im: 0 };
    return { q: `(${cT(A, B)})(${cT(Cc, D)})`, re: A * Cc - B * D, im: A * D + B * Cc };
  }, x => x.q);
  ps.forEach((p, i) => { const a = cT(p.re, p.im); items.push({ k: 'same', q: p.q, a }); cells.push(cell(i + 1, F(p.q), 0.5, `= ${ab(a, 6)}`)); });
  return {
    ican: 'I can add, subtract and multiply complex numbers and write the answer in a + bi form.',
    directions: 'Simplify. Combine real parts with real parts and imaginary parts with imaginary parts. When you multiply, use i² = −1. Write each answer as a + bi.',
    ex: example('(3 + 2i)(1 − 4i) = 3 − 12i + 2i − 8i² = 3 − 10i + 8 = 11 − 10i.', '(5 − i) − (2 + 3i) = 5 − i − 2 − 3i = 3 − 4i.'),
    parts: [part('Practice', grid(cells, 3))], items,
    mistakes: 'Leaving i² in the answer instead of −1, subtracting only the real part of the second number, and writing (2 + 3i)² as 4 + 9i².',
  };
}
function skQComplex(r, n) {
  const items = [], cells = [];
  // problem 1 has whole-number roots re ± im·i, so its check can be done by hand
  const re = nz(r, -5, 5), im = r.int(1, 6), b0 = -2 * re, c0 = re * re + im * im;
  const first = { a: 1, b: b0, c: c0, eq: eqZero([c0, b0, 1]) };
  const rest = r.distinct(n - 1, () => {
    const a = r.pick([1, 1, 1, 2, 3]), b = r.int(-8, 8), c = r.int(1, 40);
    if (b * b - 4 * a * c >= 0) return null;
    const eq = eqZero([c, b, a]); return eq === first.eq ? null : { a, b, c, eq };
  }, x => x.eq);
  const ps = [first, ...rest];
  ps.forEach((p, i) => { const a = quadText(p.a, p.b, p.c, true); items.push({ k: 'quadc', q: p.eq, a }); cells.push(cell(i + 1, `Solve ${F(p.eq)}.`, 0.85, ab(a, 8))); });
  const z = cT(re, im), z2 = cT(re * re - im * im, 2 * re * im), bz = cT(b0 * re, b0 * im);
  const bTerm = `${b0 < 0 ? MIN : '+'} ${Math.abs(b0)}(${z})`;
  const work = `(${z})² ${bTerm} + ${c0} = (${z2}) + (${bz}) + ${c0} = 0`;
  items.push({ k: 'qccheck', q: `check ${z} in ${first.eq}`, a: work });
  const check = `<p>Substitute <i>x</i> = ${F(z)} from problem 1 into ${F(poly([c0, b0, 1]))} and show that you get 0.</p><div class="al-work" style="min-height:1in"></div>` + keyp(F(work));
  return {
    ican: 'I can solve quadratic equations that have complex solutions and check a complex root.',
    directions: 'Solve each equation with the quadratic formula or by completing the square. Write √(−n) as i√n and simplify. Write both solutions with ±.',
    ex: example('x² − 4x + 13 = 0: x = (4 ± √(16 − 52))/2 = (4 ± √−36)/2 = (4 ± 6i)/2.', 'So x = 2 ± 3i.'),
    parts: [part('Practice', grid(cells)), part('Check a root', check)], items,
    mistakes: 'Writing √−36 as −6, dividing only part of the numerator by 2a, and losing the i when simplifying.',
  };
}

/* ---------- polynomials: the remainder theorem ---------- */
function skRemainder(r, n) {
  const items = [], blocks = [], np = n >= 9 ? 3 : 2, per = Math.ceil(n / np), seen = new Set();
  for (let k = 0; k < np && items.length < n; k++) {
    let cs, roots;
    for (;;) { roots = r.sample([-4, -3, -2, -1, 1, 2, 3, 4], r.chance(.6) ? 3 : 2);
      cs = roots.reduce((acc, z) => pmul(acc, [-z, 1]), [1]); if (roots.length === 2) cs = pmul(cs, [r.int(1, 6), nz(r, -3, 3), 1]);
      if (!seen.has(poly(cs)) && cs.every(c => Math.abs(c) < 80)) break; }
    seen.add(poly(cs));
    const nm = 'PQR'[k], want = Math.min(per, n - items.length);
    const cands = r.shuffle([...r.sample(roots, Math.min(roots.length, Math.ceil(want / 2))), ...r.sample([-4, -3, -2, -1, 1, 2, 3, 4, 5].filter(z => !roots.includes(z)), want)]).slice(0, want);
    const rows = cands.map(c => { const rem = pval(cs, c), a = `${nm}(${num(c)}) = ${num(rem)}; ${rem === 0 ? 'yes' : 'no'}`;
      items.push({ k: 'rem', q: `${nm}(x) = ${poly(cs)}; x ${c < 0 ? '+' : MIN} ${Math.abs(c)}`, a, cs, c, P: poly(cs) });
      return `<div class="al-cell"><p>Is (${F(fac(c))}) a factor?</p><div class="al-work" style="min-height:.55in"></div><div class="al-ans">${ab(`${nm}(${num(c)}) = ${num(rem)}`, 6)} Factor? ${ab(rem === 0 ? 'yes' : 'no', 2.5)}</div></div>`; });
    blocks.push(`<p><b>${F(`${nm}(x) = ${poly(cs)}`)}</b></p><div class="al-grid al-c3">${rows.join('')}</div>`);
  }
  return {
    ican: 'I can use the remainder theorem to test whether x − c is a factor of a polynomial.',
    directions: 'For each possible factor x − c, find P(c). By the remainder theorem, P(c) is the remainder when P(x) is divided by x − c, so x − c is a factor exactly when P(c) = 0. Watch the sign: x + 2 means c = −2.',
    ex: example('P(x) = x³ − 2x² − 5x + 6. Test x − 3: P(3) = 27 − 18 − 15 + 6 = 0, so x − 3 is a factor.', 'Test x + 1: P(−1) = −1 − 2 + 5 + 6 = 8, so the remainder is 8 and x + 1 is not a factor.'),
    parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Using c = 2 for x + 2, and sign slips when cubing or squaring a negative number.',
  };
}

/* ---------- rational expressions and equations ---------- */
const factT = (k, roots) => { const fs = roots.map(z => `(${fac(z)})`).join(''); return k === 1 ? fs || '1' : k === -1 ? MIN + fs : num(k) + fs; };
// parenthesize anything that is not a lone number or a lone letter, so a/b reads the same to a person and the parser
const wrap = s => /^(−?\d+|[a-z])$/.test(s) ? s : `(${s})`;
// a numerator needs parentheses only when it is a sum at the top level
const wrapN = s => { let d = 0; for (let i = 0; i < s.length; i++) { const c = s[i]; if (c === '(') d++; else if (c === ')') d--; else if (!d && i > 0 && (c === '+' || c === '−') && s[i - 1] === ' ') return `(${s})`; } return s; };
function skRatSimp(r, n) {
  const items = [], cells = [];
  const ps = r.distinct(n, () => {
    const T = r.pick(['qq', 'qq', 'lq', 'ql', 'mono', 'gq']);
    if (T === 'mono') { const c1 = r.int(2, 12), c2 = r.int(2, 12), m = r.int(1, 6), k = r.int(1, 6); if (m === k || gcd(c1, c2) === 1) return null;
      const g = gcd(c1, c2), A = c1 / g, B = c2 / g, e = m - k;
      const top = e > 0 ? `${A === 1 ? '' : A}${mono('x', e)}` : String(A), bot = e < 0 ? `${B === 1 ? '' : B}${mono('x', -e)}` : (B === 1 ? '' : String(B));
      return { N: `${c1}${mono('x', m)}`, D: `${c2}${mono('x', k)}`, s: bot ? `${top}/${wrap(bot)}` : top, ex: [0] };
    }
    const [a, b, c] = r.sample([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6], 3);
    let k1 = r.pick([1, 1, 1, 2, 3]), k2 = r.pick([1, 1, 1, 2, -1]); const g = gcd(k1, k2); k1 /= g; k2 /= g; if (k2 < 0) { k1 = -k1; k2 = -k2; }
    let nr, dr;
    if (T === 'qq') { nr = [a, b]; dr = [a, c]; } else if (T === 'lq') { nr = [a]; dr = [a, c]; } else if (T === 'ql') { nr = [a, b]; dr = [a]; } else { nr = [a]; dr = [a, -a]; if (!a) return null; }
    const Ncs = pscale(nr.reduce((p, z) => pmul(p, [-z, 1]), [1]), k1), Dcs = pscale(dr.reduce((p, z) => pmul(p, [-z, 1]), [1]), k2);
    const nl = nr.slice(1), dl = dr.slice(1);
    let top = nl.length ? factT(k1, nl) : num(k1), bot = dl.length ? factT(k2, dl) : (k2 === 1 ? '' : String(k2));
    if (nl.length && k1 !== 1 && k1 !== -1) top = `${num(k1)}(${fac(nl[0])})`;
    if (nl.length === 1 && k1 === 1) top = fac(nl[0]);
    if (dl.length === 1 && k2 === 1) bot = fac(dl[0]);
    const s = bot ? `${wrapN(top)}/${wrap(bot)}` : top;
    return { N: poly(Ncs), D: poly(Dcs), s: s.replace(/^\(−\((.*)\)\)\//, '−($1)/'), ex: [...new Set(dr)] };
  }, x => x.N + '|' + x.D);
  ps.forEach((p, i) => { const ex = p.ex.slice().sort((x, y) => x - y).map(num).join(', '), a = `${p.s}; x ≠ ${ex}`;
    items.push({ k: 'ratsimp', q: `(${p.N})/(${p.D})`, a, N: p.N, D: p.D, s: p.s, ex: p.ex });
    cells.push(cell(i + 1, `Simplify ${frac(F(p.N), F(p.D))}`, 0.75, `<p>= ${ab(p.s, 7)}</p><p>Excluded: ${ab('x ≠ ' + ex, 6)}</p>`)); });
  return {
    ican: 'I can simplify a rational expression by factoring and state the values excluded from its domain.',
    directions: 'Factor the top and the bottom, then cancel common factors. List every value of x that makes the original denominator 0: those values stay excluded even after a factor cancels.',
    ex: example(`${frac('<i>x</i>² − 9', '<i>x</i>² + 5<i>x</i> + 6')} = ${frac('(<i>x</i> − 3)(<i>x</i> + 3)', '(<i>x</i> + 2)(<i>x</i> + 3)')} = ${frac('<i>x</i> − 3', '<i>x</i> + 2')}`, 'Excluded: x ≠ −3, −2, because both make the original denominator 0.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Canceling terms instead of factors (x + 3 over x + 5 is not 3/5), and leaving out the excluded value of a factor that canceled.',
  };
}
function skRatAdd(r, n) {
  const items = [], cells = [];
  const ps = r.distinct(n, () => {
    const [p, q] = r.sample([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6], 2), T = r.pick(['ab', 'ab', 'shared', 'x']), a = r.int(1, 7), b = r.int(1, 7), plus = r.chance(.5);
    let t1, t2, N; const op = plus ? '+' : MIN;
    if (T === 'ab') { t1 = [String(a), fac(p)]; t2 = [String(b), fac(q)]; N = padd(pscale([-q, 1], a), pscale([-p, 1], plus ? b : -b)); }
    else if (T === 'shared') { t1 = [String(a), fac(p)]; t2 = [String(b), poly(pmul([-p, 1], [-q, 1]))]; N = padd(pscale([-q, 1], a), [plus ? b : -b]); }
    else { t1 = ['x', fac(p)]; t2 = [String(b), fac(q)]; N = padd(pmul([0, 1], [-q, 1]), pscale([-p, 1], plus ? b : -b)); }
    while (N.length > 1 && !N[N.length - 1]) N.pop();
    if (N.every(c => !c) || pval(N, p) === 0 || pval(N, q) === 0) return null;
    const [s, t] = p < q ? [p, q] : [q, p];
    return { q: `${t1[0]}/(${t1[1]}) ${op} ${t2[0]}/(${t2[1]})`, a: `${wrapN(poly(N))}/((${fac(s)})(${fac(t)}))`, html: `${frac(F(t1[0]), F(t1[1]))} ${op} ${frac(F(t2[0]), F(t2[1]))}` };
  }, x => x.q);
  ps.forEach((p, i) => { items.push({ k: 'same', q: p.q, a: p.a, rat: true });
    const html = p.html;
    cells.push(cell(i + 1, html, 0.85, `= ${ab(p.a, 9)}`)); });
  return {
    ican: 'I can add and subtract rational expressions with unlike denominators using the least common denominator.',
    directions: 'Factor each denominator and find the least common denominator. Rewrite each fraction over it, combine the numerators (watch the subtraction sign), and simplify. Leave the denominator factored.',
    ex: example(`${frac('3', '<i>x</i> − 1')} + ${frac('2', '<i>x</i> + 2')} = ${frac('3(<i>x</i> + 2) + 2(<i>x</i> − 1)', '(<i>x</i> − 1)(<i>x</i> + 2)')} = ${frac('5<i>x</i> + 4', '(<i>x</i> − 1)(<i>x</i> + 2)')}`, 'Check that the numerator has no factor in common with the denominator.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Adding the denominators, subtracting only the first term of the second numerator, and multiplying out a denominator that has to be factored to find the LCD.',
  };
}
function skExtraneous(r, n) {
  const items = [], cells = [];
  const ps = r.distinct(n, () => {
    const T = r.pick(['rad', 'rad', 'rad', 'radk', 'ratA', 'ratB', 'ratC']);
    if (T === 'rad' || T === 'radk') {
      const [r1, r2] = r.sample([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2); if ((r1 + r2) % 2 === 0) return null;
      const b = (1 - r1 - r2) / 2, a = b * b - r1 * r2;
      const eq = T === 'rad' ? `√(${fac(-a)}) = ${lin(1, b)}` : (b ? `√(${fac(-a)}) ${b < 0 ? '+' : MIN} ${Math.abs(b)} = x` : null);
      if (!eq || !a) return null;
      const good = [r1, r2].filter(z => z + b >= 0), bad = [r1, r2].filter(z => z + b < 0);
      return { eq, good, bad, T, a, b, html: F(eq) };
    }
    if (T === 'ratA') { const a = nz(r, -6, 6), s = nz(r, -7, 7); if (s === a) return null; const q = a + s, rr = -a * s;
      const N = poly([rr, q]), eq = `x²/(${fac(a)}) = ${wrapN(N)}/(${fac(a)})`;
      return { eq, good: [s], bad: [a], T, a, q, rr, html: `${frac(F('x²'), F(fac(a)))} = ${frac(F(N), F(fac(a)))}` }; }
    if (T === 'ratB') { const a = nz(r, -6, 6), c = r.pick([2, 3, 4, -1, -2]);
      const cs = c < 0 ? `${MIN} ${-c}` : `+ ${c}`;
      return { eq: `x/(${fac(a)}) = ${num(a)}/(${fac(a)}) ${cs}`, good: [], bad: [a], T, a, c, html: `${frac(F('x'), F(fac(a)))} = ${frac(num(a), F(fac(a)))} ${cs}` }; }
    const [r1, r2] = r.sample([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6], 2), m = r1 + r2, k = r1 * r2;
    const op = k < 0 ? MIN : '+';
    return { eq: `x ${op} ${Math.abs(k)}/x = ${num(m)}`, good: [r1, r2], bad: [], T: 'ratC', html: `${F('x')} ${op} ${frac(Math.abs(k), F('x'))} = ${num(m)}` };
  }, x => x.eq);
  const list = z => z.slice().sort((a, b) => a - b).map(v => `x = ${num(v)}`).join(', ');
  ps.forEach((p, i) => {
    const sol = p.good.length ? list(p.good) : 'no solution', ext = p.bad.length ? list(p.bad) : 'none';
    items.push({ k: 'extr', q: p.eq, a: `${sol}; extraneous: ${ext}`, d: p });
    cells.push(cell(i + 1, `Solve ${p.html}`, 0.95, `<p>Solution: ${ab(sol, 7)}</p><p>Extraneous: ${ab(ext, 5)}</p>`));
  });
  const why = 'Squaring both sides, or multiplying both sides by an expression with x, can make a new equation that has more solutions than the original. A value can solve the squared equation while the original square root would be negative, or it can make a denominator 0. Checking each answer in the original equation finds these extraneous solutions.';
  return {
    ican: 'I can solve rational and radical equations, check every answer and explain where an extraneous solution comes from.',
    directions: 'Solve each equation. Check every answer in the original equation. Write the solutions that work, and list any extraneous solutions (answers that came out of the algebra but do not work). Write "none" or "no solution" when that is the case.',
    ex: example('√(x + 7) = x + 1 → x + 7 = x² + 2x + 1 → x² + x − 6 = 0 → x = −3 or x = 2.', 'Check: x = 2 gives 3 = 3 (works). x = −3 gives 2 = −2 (fails), so x = −3 is extraneous.'),
    parts: [part('Practice', grid(cells)), part('Explain', `<p>Where do extraneous solutions come from? Use one of your problems as an example.</p>${lines(3)}${keyp(why)}`)], items,
    mistakes: 'Skipping the check, squaring only one term of x + 1, and keeping an answer that makes a denominator 0.',
  };
}

/* ---------- logarithms ---------- */
const logN = b => b === 10 ? 'log' : b === 'e' ? 'ln' : 'log' + sub(b);
const argT = q => q.d === 1 ? String(q.n) : `(${qT(q)})`;
function skLogForm(r, n) {
  const [nr, ne] = n, items = [], ca = [], cb = [];
  const rw = r.distinct(nr, () => {
    const b = r.pick([2, 3, 4, 5, 10, 2, 3]), e = r.int(-3, 5), v = b ** Math.abs(e); if (v > 100000 || (b === 10 && e > 4)) return null;
    const val = e >= 0 ? Q(v) : Q(1, v), expT = `${b}${sup(e)} = ${qT(val)}`, logT = `${logN(b)} ${argT(val)} = ${num(e)}`;
    return r.chance(.5) ? { q: expT, a: logT, to: 'log' } : { q: logT, a: expT, to: 'exp' };
  }, x => x.q);
  rw.forEach((p, i) => { items.push({ k: 'logrw', q: p.q, a: p.a, to: p.to }); ca.push(cell(i + 1, `${F(p.q)}`, 0, `→ ${ab(p.a, 7)}`)); });
  const evs = r.distinct(ne, () => {
    if (r.chance(.12)) { const k = r.int(2, 6); return { q: `ln e${sup(k)}`, a: String(k) }; }
    const c = r.pick([2, 3, 5, 10]), m = r.pick([1, 1, 1, 2, 3]), k = r.int(-3, 6); const b = c ** m; if (b > 125 || c ** Math.abs(k) > 10000 || (c === 10 && m > 1)) return null;
    const val = k >= 0 ? Q(c ** k) : Q(1, c ** -k); return { q: `${logN(b)} ${argT(val)}`, a: qT(Q(k, m)) };
  }, x => x.q);
  evs.forEach((p, i) => { items.push({ k: 'same', q: p.q, a: p.a }); cb.push(cell(nr + i + 1, `${F(p.q)}`, 0.3, `= ${ab(p.a, 3)}`)); });
  return {
    ican: 'I can rewrite equations between exponential and logarithmic form and evaluate logarithms without a calculator.',
    directions: 'Part A: rewrite each exponential equation in logarithmic form, or each logarithmic equation in exponential form. Part B: evaluate each logarithm by asking "the base to what power gives this number?"',
    ex: example('2⁵ = 32 means log₂ 32 = 5. log₃ (1/9) = −2 means 3⁻² = 1/9.', 'log₄ 2 = 1/2, because 4^(1/2) = √4 = 2. log means base 10; ln means base e.'),
    parts: [part('Part A: Rewrite', grid(ca, 3)), part('Part B: Evaluate', grid(cb, 3))], items,
    mistakes: 'Swapping the exponent and the result (log₂ 32 = 5 is 2⁵ = 32, not 2³² = 5), and thinking a negative log value is impossible.',
  };
}
function logExpr(r) {
  const b = r.pick([10, 'e', 2, 3, 5]), L = logN(b), vs = r.sample(['x', 'y', 'z'], r.pick([2, 2, 3])).sort();
  const P = vs.map(v => [v, r.pick([1, 1, 2, 3, 4, 'h']), r.chance(.35) ? -1 : 1]);
  if (!P.some(p => p[2] > 0)) P[0][2] = 1;
  P.sort((u, w) => w[2] - u[2]);
  const pw = (v, e) => e === 'h' ? '√' + v : e === 1 ? v : v + sup(e);
  const top = P.filter(p => p[2] > 0).sort((a, c) => (a[1] === 'h') - (c[1] === 'h')).map(p => pw(p[0], p[1])).join(''), bots = P.filter(p => p[2] < 0).map(p => pw(p[0], p[1]));
  const cond = `${L}(${top}${bots.length ? '/' + (bots.length > 1 ? `(${bots.join('')})` : bots[0]) : ''})`;
  const ex = P.map(([v, e, s], i) => { const c = e === 'h' ? '(1/2) ' : e === 1 ? '' : e + ' '; return `${i ? (s < 0 ? ` ${MIN} ` : ' + ') : (s < 0 ? MIN : '')}${c}${L} ${v}`; }).join('');
  return { cond, ex };
}
function skLogProp(r, n) {
  const [nm, nmore] = n, items = [];
  const pairs = r.distinct(nm + nmore, () => logExpr(r), x => x.cond), M = pairs.slice(0, nm), more = pairs.slice(nm);
  const letters = 'ABCDEFGHIJKLMNOP', order = r.shuffle(M.map((_, i) => i)), list = order.map(i => M[i].ex);
  const left = M.map((p, i) => { const L = letters[order.indexOf(i)]; items.push({ k: 'logmatch', q: p.cond, a: L, list });
    return `<li>${F(p.cond)} ${ab(L, 2.2)}</li>`; });
  const right = list.map((e, j) => `<li><b>${letters[j]}.</b> ${F(e)}</li>`);
  const mc = more.map((p, j) => { const expand = j % 2 === 0, q = expand ? p.cond : p.ex, a = expand ? p.ex : p.cond;
    items.push({ k: 'logsame', q, a, expand }); return cell(nm + j + 1, `${expand ? 'Expand' : 'Condense'} ${F(q)}`, 0.45, ab(a, 10)); });
  return {
    ican: 'I can use the product, quotient and power properties to expand and condense logarithms.',
    directions: 'Match each condensed logarithm on the left to its expanded form on the right: write the letter on the line. Then expand or condense the last expressions on your own. All variables are positive.',
    ex: example('log₂(x³y/z) = log₂ x³ + log₂ y − log₂ z = 3 log₂ x + log₂ y − log₂ z.', 'A square root is a power of 1/2: ln √x = (1/2) ln x.'),
    parts: [part('Match', `<div class="al-match"><ol class="ws-fill">${left.join('')}</ol><ul class="al-opts">${right.join('')}</ul></div>`), part('On your own', grid(mc))], items,
    mistakes: 'Writing log(x + y) as log x + log y, putting the power on the whole log instead of the variable, and giving the denominator a plus sign.',
  };
}
function skExpEq(r, n) {
  const items = [], cells = [];
  const notPow = (v, b) => { if (v <= 0) return false; const L = Math.log(v) / Math.log(b) * 6; return Math.abs(L - Math.round(L)) > 1e-6; };
  const ps = r.distinct(n, () => {
    const T = r.pick(['F1', 'F2', 'F3', 'F4', 'F5', 'F6']), b = r.pick([2, 3, 4, 5, 6, 7]), c = r.int(5, 90);
    let eq, ex;
    if (T === 'F1') { if (!notPow(c, b)) return null; eq = `${b}ˣ = ${c}`; ex = `x = log${sub(b)} ${c}`; }
    else if (T === 'F2') { const a = r.int(2, 6), cc = a * r.int(2, 30) + r.int(0, 1) * r.int(1, a - 1); const q = Q(cc, a); if (!notPow(qv(q), b)) return null; eq = `${a} · ${b}ˣ = ${cc}`; ex = `x = log${sub(b)} ${argT(q)}`; }
    else if (T === 'F3') { const h = nz(r, -4, 4); if (!notPow(c, b)) return null; eq = `${b}ˣ${h > 0 ? '⁻' : '⁺'}${sup(Math.abs(h))} = ${c}`; ex = `x = log${sub(b)} ${c} ${h > 0 ? '+' : MIN} ${Math.abs(h)}`; }
    else if (T === 'F4') { const k = r.int(1, 5), cc = r.int(2, 40); eq = `e${k === 1 ? '' : sup(k)}ˣ = ${cc}`; ex = k === 1 ? `x = ln ${cc}` : `x = (ln ${cc})/${k}`; }
    else if (T === 'F5') { const d = r.int(2, 20); if (!notPow(c, b)) return null; eq = `${b}ˣ + ${d} = ${c + d}`; ex = `x = log${sub(b)} ${c}`; }
    else { const a = r.int(2, 6), cc = r.int(3, 60); const q = Q(cc, a); if (q.d === 1 && q.n === 1) return null; eq = `${a}eˣ = ${cc}`; ex = q.d === 1 ? `x = ln ${q.n}` : `x = ln(${qT(q)})`; }
    const x = evR(ex.slice(4)), f = x * 1000 - Math.floor(x * 1000); if (Math.abs(f - 0.5) < 0.02) return null;
    return { eq, ex, dec: x.toFixed(3) };
  }, x => x.eq);
  ps.forEach((p, i) => { items.push({ k: 'expeq', q: p.eq, a: `${p.ex} ≈ ${p.dec}` });
    cells.push(cell(i + 1, `Solve ${F(p.eq)}.`, 0.8, `<p>Exact: ${ab(p.ex, 8)}</p><p>Decimal: ${ab('x ≈ ' + p.dec, 6)}</p>`)); });
  return {
    ican: 'I can solve exponential equations with logarithms and give exact and decimal answers.',
    directions: 'Get the power by itself, then take a logarithm of both sides (or rewrite in log form). Give the exact answer with a logarithm, then a decimal to the nearest thousandth. Use log_b a = (log a)/(log b) on a calculator.',
    ex: example('4 · 3ˣ = 40 → 3ˣ = 10 → x = log₃ 10.', 'x = (log 10)/(log 3) ≈ 2.096. For e³ˣ = 7: 3x = ln 7, so x = (ln 7)/3 ≈ 0.649.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Taking the log before dividing out the number in front, writing log₃ 10 as log 10/3, and rounding too early.',
  };
}
function skGrowth(r, n) {
  const items = [], blocks = [];
  const types = r.shuffle(Array.from({ length: n }, (_, i) => ['comp', 'cont', 'half', 'carbon', 'goal', 'dep'][i % 6]));
  const fine = (x, step) => { const f = x / step - Math.floor(x / step); return Math.abs(f - 0.5) > 0.03; };
  const ISO = [['iodine-131', 8, 'days'], ['radon-222', 3.8, 'days'], ['phosphorus-32', 14.3, 'days'], ['cobalt-60', 5.27, 'years'], ['strontium-90', 28.8, 'years'], ['cesium-137', 30.2, 'years']];
  const seen = new Set();
  for (const t of types) {
    const p = r.distinct(1, () => {
      const nm = r.pick(NAMES), P = r.pick([500, 1000, 1500, 2000, 2500, 4000, 5000]), rate = r.pick([2, 2.5, 3, 3.5, 4, 4.5, 5, 6]), yrs = r.int(3, 20);
      if (t === 'comp') { const [fw, k] = r.pick([['annually', 1], ['quarterly', 4], ['monthly', 12]]), A = P * (1 + rate / 100 / k) ** (k * yrs); if (!fine(A, 0.01)) return null;
        return { text: `${nm} puts ${money(P)} in a savings account that pays ${rate}% interest per year, compounded ${fw}. How much is in the account after ${yrs} years? Round to the nearest cent.`, a: cents(A), d: { t, P, rate, k, yrs } }; }
      if (t === 'cont') { const A = P * Math.exp(rate / 100 * yrs); if (!fine(A, 0.01)) return null;
        return { text: `${nm} invests ${money(P)} at ${rate}% per year, compounded continuously. How much is there after ${yrs} years? Round to the nearest cent.`, a: cents(A), d: { t, P, rate, yrs } }; }
      if (t === 'half') { const [iso, h, u] = r.pick(ISO), A0 = r.pick([50, 80, 100, 200, 400, 500]), tt = Math.round(h * r.int(10, 45) / 10), A = A0 * 0.5 ** (tt / h); if (!fine(A, 0.1)) return null;
        return { text: `A lab has ${A0} milligrams of ${iso}, which has a half-life of about ${h} ${u}. How much is left after ${tt} ${u}? Round to the nearest tenth of a milligram.`, a: `${A.toFixed(1)} mg`, d: { t, A0, h, tt } }; }
      if (t === 'carbon') { const pc = r.int(2, 18) * 5, age = 5730 * Math.log(pc / 100) / Math.log(0.5); if (!fine(age, 100)) return null;
        return { text: `A ${r.pick(['bone', 'piece of charcoal', 'wooden tool', 'seed'])} has ${pc}% of the carbon-14 it had when it was alive. Carbon-14 has a half-life of about 5,730 years. About how old is it? Round to the nearest hundred years.`, a: `${comma(Math.round(age / 100) * 100)} years`, d: { t, pc } }; }
      if (t === 'goal') { const G = P * r.pick([1.5, 2, 2.5, 3, 4]), tt = Math.log(G / P) / (rate / 100); if (!fine(tt, 0.1)) return null;
        return { text: `${nm} invests ${money(P)} at ${rate}% per year, compounded continuously. How many years until it grows to ${money(G)}? Round to the nearest tenth of a year.`, a: `${tt.toFixed(1)} years`, d: { t, P, G, rate } }; }
      const V = r.pick([18000, 22000, 25000, 30000, 34000]), dr = r.pick([10, 12, 15, 18, 20]), A = V * (1 - dr / 100) ** yrs; if (!fine(A, 0.01) || yrs > 12) return null;
      return { text: `A car bought for ${money(V)} loses ${dr}% of its value each year. What is it worth after ${yrs} years? Round to the nearest cent.`, a: cents(A), d: { t, V, dr, yrs } };
    }, x => x.text)[0];
    if (!p || seen.has(p.text)) continue; seen.add(p.text);
    items.push({ k: 'growth', q: p.text, a: p.a, d: p.d });
    blocks.push(`<div class="al-story"><p><span class="ws-num">${items.length}.</span> ${esc(p.text)}</p><div class="al-work" style="min-height:.8in"></div><p class="al-ans">${ab(p.a, 8)}</p></div>`);
  }
  return {
    ican: 'I can solve growth and decay problems with compound interest, continuous compounding and half-life.',
    directions: 'Choose the model that fits each problem. Compound interest: A = P(1 + r/n)ⁿᵗ. Continuous: A = Peʳᵗ. Half-life h: A = A₀(1/2)^(t/h). Loss of r% a year: A = P(1 − r)ᵗ. Use logarithms when the time is unknown.',
    ex: example('$1,000 at 4% compounded quarterly for 5 years: A = 1000(1 + 0.04/4)²⁰ ≈ $1,220.19.', 'Carbon-14 with 50% left is one half-life old: about 5,730 years. With 25% left, two half-lives: about 11,460 years.'),
    parts: [part('Problems', blocks.join(''))], items,
    mistakes: 'Using the percent as a whole number (4 instead of 0.04), forgetting to multiply n by t in the exponent, and rounding in the middle of the work.',
  };
}

/* ---------- combining, composing and inverting functions ---------- */
function domText(dm) { if (!dm) return 'all real numbers'; return `x ${dm.rel} ${qT(dm.v)}`; }
function skCombine(r, n) {
  const items = [], cells = [];
  const ps = r.distinct(n, () => {
    const T = r.pick(['ll', 'ql', 'ql', 'sl', 'slc', 'rl', 'rlc', 'qs']), a = nz(r, -5, 5), b = r.int(-9, 9), h = nz(r, -6, 6);
    const L = [b, a], Lt = poly(L);
    if (T === 'll') { const L2 = [r.int(-9, 9), nz(r, -5, 5)], op = r.pick(['+', '−', '·', '∘']);
      const res = op === '+' ? padd(L, L2) : op === '−' ? padd(L, pscale(L2, -1)) : op === '·' ? pmul(L, L2) : padd(pscale([L2[0], L2[1]], a), [b]);
      if (deg(res) < 1) return null; return { f: Lt, g: poly(L2), op, ans: poly(res), dm: null }; }
    if (T === 'ql') { const Qc = [nz(r, -9, 9), r.int(-5, 5), 1], op = r.pick(['+', '−', '·', '∘', '∘']);
      const res = op === '+' ? padd(Qc, L) : op === '−' ? padd(Qc, pscale(L, -1)) : op === '·' ? pmul(Qc, L) : padd(padd(pmul(L, L), pscale(L, Qc[1])), [Qc[0]]);
      return { f: poly(Qc), g: Lt, op, ans: poly(res), dm: null }; }
    if (T === 'sl') return { f: `√(${fac(h)})`, g: Lt, op: '+', ans: `√(${fac(h)}) ${Lt.startsWith(MIN) ? MIN + ' ' + Lt.slice(1) : '+ ' + Lt}`, dm: { rel: '≥', v: Q(h) } };
    if (T === 'slc') { const inner = [b - h, a]; if (!inner[0] && Math.abs(a) === 1) return null; return { f: `√(${fac(h)})`, g: Lt, op: '∘', ans: `√(${poly(inner)})`, dm: { rel: a > 0 ? '≥' : '≤', v: Q(h - b, a) } }; }
    if (T === 'rl') { if (a * h + b === 0) return null; return { f: `1/(${fac(h)})`, g: Lt, op: '·', ans: `${wrapN(Lt)}/(${fac(h)})`, dm: { rel: '≠', v: Q(h) } }; }
    if (T === 'rlc') { const inner = [b - h, a]; return { f: `1/(${fac(h)})`, g: Lt, op: '∘', ans: `1/(${poly(inner)})`, dm: { rel: '≠', v: Q(h - b, a) } }; }
    const c = nz(r, -9, 9); return { f: `x² ${c < 0 ? MIN : '+'} ${Math.abs(c)}`, g: `√(${fac(h)})`, op: '∘', ans: poly([c - h, 1]), dm: { rel: '≥', v: Q(h) } };
  }, x => x.f + x.g + x.op);
  ps.forEach((p, i) => {
    const name = p.op === '∘' ? 'f(g(x))' : p.op === '·' ? '(fg)(x)' : `(f ${p.op} g)(x)`, a = `${p.ans}; ${domText(p.dm)}`;
    items.push({ k: 'combine', q: `f(x) = ${p.f}, g(x) = ${p.g}; ${name}`, a, f: p.f, g: p.g, op: p.op, ans: p.ans, dm: p.dm });
    cells.push(cell(i + 1, `${F(`f(x) = ${p.f}`)} and ${F(`g(x) = ${p.g}`)}. Find ${F(name)} and its domain.`, 0.7, `<p>${F(name)} = ${ab(p.ans, 8)}</p><p>Domain: ${ab(domText(p.dm), 6)}</p>`));
  });
  return {
    ican: 'I can find sums, differences, products and compositions of functions and state their domains.',
    directions: 'Combine the functions as asked and simplify. The domain is every x where the result makes sense: no negative under a square root and no zero in a denominator. For f(g(x)), x must also be in the domain of g.',
    ex: example('f(x) = √(x − 2), g(x) = 3x + 5: f(g(x)) = √(3x + 5 − 2) = √(3x + 3).', 'Domain: 3x + 3 ≥ 0, so x ≥ −1.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Multiplying instead of composing, distributing a minus sign to only one term of g, and judging the domain of f(g(x)) from the simplified answer alone: with g(x) = √(x − 3), f(g(x)) = x − 3 + 1 still needs x ≥ 3.',
  };
}
function invOne(r, T) {
  const h = nz(r, -6, 6), k = nz(r, -6, 6), b = r.pick([2, 3]);
  const shift = (s, c) => c ? `${s} ${c < 0 ? MIN : '+'} ${Math.abs(c)}` : s;
  if (T === 'lin') { const a = r.pick([2, 3, 4, 5, -2, -3, -4]), c = nz(r, -9, 9);
    const inv = a > 0 ? `(${fac(c)})/${a}` : `${MIN}(${fac(c)})/${-a}`; return { f: lin(a, c), inv, dom: null }; }
  if (T === 'cube') return { f: shift(`(${fac(h)})³`, k), inv: shift(`∛(${fac(k)})`, h), dom: null };
  if (T === 'sqrt') return { f: shift(`√(${fac(h)})`, k), inv: `${shift(`(${fac(k)})²`, h)}, x ≥ ${num(k)}`, dom: { lo: h } };
  if (T === 'exp') return { f: shift(`${b}ˣ`, k), inv: `log${sub(b)}(${fac(k)})`, dom: null };
  if (T === 'log') return { f: shift(`log${sub(b)} x`, k), inv: `${b}ˣ${k > 0 ? '⁻' : '⁺'}${sup(Math.abs(k))}`, dom: { lo: 0, open: true } };
  if (T === 'rec') return { f: shift(`1/(${fac(h)})`, k), inv: shift(`1/(${fac(k)})`, h), dom: null };
  if (T === 'quadR') { const neg = r.chance(.3); return { f: shift(`(${fac(h)})²`, k), inv: neg ? `${num(h)} ${MIN} √(${fac(k)})` : shift(`√(${fac(k)})`, h), restr: `x ${neg ? '≤' : '≥'} ${num(h)}`, dom: neg ? { hi: h } : { lo: h } }; }
  return { f: shift('x²', k), inv: `√(${fac(k)})`, restr: 'x ≥ 0', dom: { lo: 0 } };
}
function skInverse(r, n, course) {
  const pre = course === 'pre', items = [], cells = [];
  const kinds = pre ? ['quadR', 'quadR', 'sq0', 'lin', 'cube', 'exp', 'rec', 'sqrt'] : ['lin', 'lin', 'cube', 'sqrt', 'exp', 'log', 'rec'];
  const ps = r.distinct(n, () => invOne(r, r.pick(kinds)), x => x.f);
  ps.forEach((p, i) => {
    const restr = p.restr || 'none needed';
    const a = pre ? `${restr}; f⁻¹(x) = ${p.inv}` : `f⁻¹(x) = ${p.inv}`;
    const shown = p.f;
    items.push({ k: 'inverse', q: `f(x) = ${pre ? p.f : shown}`, a, f: p.f, inv: p.inv, dom: p.dom, restr: pre ? restr : null });
    cells.push(cell(i + 1, `${F(`f(x) = ${pre ? p.f : shown}`)}`, pre ? 0.8 : 0.85, (pre ? `<p>Restrict to: ${ab(restr, 5)}</p>` : '') + `<p>${ab(`f⁻¹(x) = ${p.inv}`, 10)}</p>`));
  });
  return {
    ican: pre ? 'I can restrict the domain of a function so it is one-to-one and find its inverse.' : 'I can find the inverse of a function and verify it by composing.',
    directions: pre ? 'If the function is not one-to-one, restrict its domain to the part where x ≥ the vertex (or write "none needed"). Then swap x and y and solve for y to find the inverse. State any limit on the inverse.'
      : 'Find each inverse: write y = f(x), swap x and y, and solve for y. Then check that f(f⁻¹(x)) = x and f⁻¹(f(x)) = x in the space.',
    ex: example('f(x) = 2x − 6: x = 2y − 6 → y = (x + 6)/2, so f⁻¹(x) = (x + 6)/2.', pre ? 'f(x) = (x − 1)² + 3 is not one-to-one. Restrict to x ≥ 1: then f⁻¹(x) = √(x − 3) + 1.' : 'Check: f((x + 6)/2) = 2 · (x + 6)/2 − 6 = x.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Writing 1/f(x) for the inverse, undoing the steps in the wrong order, and forgetting that the inverse of a square root function has a restricted domain.',
    notes: pre ? 'For a parabola, x ≥ the vertex is the usual choice; x ≤ the vertex also works and gives the other branch with a minus sign before the root.' : '',
  };
}

/* ---------- sequences and series ---------- */
const AN = 'aₙ', AP = 'aₙ₋₁';
const qmul = (a, b) => Q(a.n * b.n, a.d * b.d), qadd = (a, b) => Q(a.n * b.d + b.n * a.d, a.d * b.d), qpow = (a, k) => Q(a.n ** k, a.d ** k);
function arithSeq(r) { const a1 = r.int(-15, 30), d = nz(r, -9, 12); return { kind: 'arith', a1: Q(a1), d: Q(d) }; }
function geoSeq(r) {
  const rt = r.pick([Q(2), Q(3), Q(-2), Q(-3), Q(1, 2), Q(1, 3), Q(-1, 2), Q(4)]);
  const a1 = rt.d === 2 ? r.pick([16, 32, 48, 64, 80, 96, 160, -32, -64]) : rt.d === 3 ? r.pick([81, 162, -81]) : r.pick([1, 2, 3, 4, 5, 6, -1, -2, -3, -5]);
  if (Math.abs(a1 * qv(rt) ** 4) > 2000) return null;
  return { kind: 'geo', a1: Q(a1), r: rt };
}
function neitherSeq(r) {
  const T = r.pick(['sq', 'sqc', 'cube', 'tri', 'fib', 'alt']), c = nz(r, -5, 6), a = r.int(1, 5), b = r.int(2, 7);
  const ts = T === 'sq' ? [1, 4, 9, 16, 25] : T === 'sqc' ? [1, 2, 3, 4, 5].map(k => k * k + c) : T === 'cube' ? [1, 8, 27, 64, 125]
    : T === 'tri' ? [1, 3, 6, 10, 15] : T === 'fib' ? [a, b, a + b, a + 2 * b, 2 * a + 3 * b] : [a, a + 2, a + 5, a + 7, a + 10];
  return { kind: 'neither', ts: ts.map(x => Q(x)) };
}
const termsOfSeq = (s, k = 5) => s.ts || Array.from({ length: k }, (_, i) => s.kind === 'arith' ? qadd(s.a1, qmul(s.d, Q(i))) : qmul(s.a1, qpow(s.r, i)));
const seqText = s => termsOfSeq(s).map(qT).join(', ') + ', ...';
function explicitT(s) {
  if (s.kind === 'arith') return `${AN} = ${sum([[s.d, 'n'], [qadd(s.a1, Q(-s.d.n, s.d.d)), '']])}`;
  const rr = s.r, base = rr.d === 1 && rr.n > 0 ? String(rr.n) : `(${qT(rr)})`, a = s.a1.n;
  const coef = a === 1 ? '' : a === -1 ? MIN : num(a) + (rr.d === 1 && rr.n > 0 ? ' · ' : '');
  return `${AN} = ${coef}${base}ⁿ⁻¹`;
}
function recursiveT(s) {
  if (s.kind === 'arith') return `a₁ = ${qT(s.a1)}, ${AN} = ${AP} ${s.d.n < 0 ? MIN : '+'} ${Math.abs(s.d.n)}`;
  const rr = s.r, c = rr.d === 1 ? (rr.n === -1 ? MIN : num(rr.n)) : `(${qT(rr)})`;
  return `a₁ = ${qT(s.a1)}, ${AN} = ${c}${AP}`;
}
const seqClassT = s => s.kind === 'arith' ? `arithmetic, d = ${qT(s.d)}` : s.kind === 'geo' ? `geometric, r = ${qT(s.r)}` : 'neither';
function skSeqSort(r, n) {
  const [nc, nf] = n, items = [];
  const kinds = r.shuffle(Array.from({ length: nc }, (_, i) => ['arith', 'geo', 'neither'][i % 3]));
  const seen = new Set(), cards = [];
  for (const k of kinds) {
    for (let t = 0; t < 60; t++) { const s = k === 'arith' ? arithSeq(r) : k === 'geo' ? geoSeq(r) : neitherSeq(r); if (!s) continue; const key = seqText(s); if (seen.has(key)) continue; seen.add(key); cards.push(s); break; }
  }
  const L = 'ABCDEFGHIJKLMNOP';
  const cardHtml = cards.map((s, i) => { const a = seqClassT(s); items.push({ k: 'seqclass', q: `Card ${L[i]}: ${seqText(s)}`, a, ts: termsOfSeq(s).map(qT) });
    return `<div class="al-card"><b>${L[i]}</b><p>${F(seqText(s))}</p><p class="al-ans">${ab(a, 8)}</p></div>`; });
  const by = k => cards.map((s, i) => s.kind === k ? L[i] : '').filter(Boolean).join(', ');
  const mat = `<table class="al-ht al-mat"><tr><th>Arithmetic</th><th>Geometric</th><th>Neither</th></tr><tr><td>${ab(by('arith'), 7)}</td><td>${ab(by('geo'), 7)}</td><td>${ab(by('neither'), 7)}</td></tr></table>`;
  const pickF = r.shuffle(cards.map((s, i) => [s, i]).filter(([s]) => s.kind !== 'neither')).slice(0, nf).sort((x, y) => x[1] - y[1]);
  const fcells = pickF.map(([s, i], j) => { const ex = explicitT(s), rc = recursiveT(s);
    items.push({ k: 'seqform', q: `Formulas for card ${L[i]}: ${seqText(s)}`, a: `${ex}; ${rc}`, ts: termsOfSeq(s, 6).map(qT) });
    return cell(j + 1, `Card ${L[i]}: ${F(seqText(s))}`, 0.25, `<p>Explicit: ${ab(ex, 8)}</p><p>Recursive: ${ab(rc, 10)}</p>`); });
  return {
    ican: 'I can tell arithmetic, geometric and other sequences apart and write explicit and recursive formulas.',
    directions: 'Cut out the cards and sort them. Arithmetic: the same number is added each time (common difference d). Geometric: each term is multiplied by the same number (common ratio r). Write each card\'s type on it, record the sort, then write both formulas for the cards listed.',
    ex: example('5, 8, 11, 14, ... adds 3: arithmetic, d = 3. aₙ = 3n + 2; a₁ = 5, aₙ = aₙ₋₁ + 3.', '2, 6, 18, 54, ... times 3: geometric, r = 3. aₙ = 2 · 3ⁿ⁻¹; a₁ = 2, aₙ = 3aₙ₋₁.'),
    parts: [part('Cards', `<div class="al-cards">${cardHtml.join('')}</div>`), part('Sort', mat), part('Write formulas', grid(fcells))], items,
    mistakes: 'Calling a sequence arithmetic after checking only the first two terms, using n instead of n − 1 in the geometric formula, and forgetting the starting term in a recursive formula.',
  };
}
function skArithWord(r, n) {
  const items = [], blocks = [], seen = new Set();
  const ctx = [
    () => { const s = r.int(12, 24), d = r.int(2, 4), k = r.int(10, 25), N = r.int(15, 30), X = s + d * r.int(8, 30);
      return { text: `A theater has ${s} seats in the first row, and each row has ${d} more seats than the row in front of it.`, s, d, k, N, X,
        asks: [`How many seats are in row ${k}?`, `How many seats are in the first ${N} rows in all?`, `Which row has ${X} seats?`], unit: ['seats', 'seats', 'row'] }; },
    () => { const s = r.pick([5, 10, 15, 20]), d = r.pick([2, 3, 5]), k = r.int(8, 20), N = r.int(10, 26), X = s + d * r.int(6, 30);
      return { text: `${r.pick(NAMES)} saves $${s} the first week and $${d} more each week than the week before.`, s, d, k, N, X,
        asks: [`How much is saved in week ${k}?`, `How much is saved in all after ${N} weeks?`, `In which week is $${X} saved?`], unit: ['$', '$', 'week'] }; },
    () => { const s = r.int(10, 20), d = r.pick([2, 3, 5]), k = r.int(6, 15), N = r.int(10, 20), X = s + d * r.int(5, 18);
      return { text: `${r.pick(NAMES)} trains for a race by running ${s} minutes on day 1 and ${d} minutes longer each day after that.`, s, d, k, N, X,
        asks: [`How long is the run on day ${k}?`, `How many minutes are run in all over the first ${N} days?`, `On which day is the run ${X} minutes long?`], unit: ['minutes', 'minutes', 'day'] }; },
    () => { const s = r.int(20, 40), d = r.int(1, 3), k = r.int(8, 16), N = r.int(10, 18), X = s + d * r.int(5, 16);
      return { text: `An outdoor stage is built with ${s} chairs in the front row and ${d} more chairs in each row going back.`, s, d, k, N, X,
        asks: [`How many chairs are in row ${k}?`, `How many chairs are in the first ${N} rows?`, `Which row has ${X} chairs?`], unit: ['chairs', 'chairs', 'row'] }; },
    () => { const s = r.int(3, 8), d = r.int(2, 4), k = r.int(10, 20), N = r.int(10, 20), X = s + d * r.int(8, 25);
      return { text: `A tile pattern uses ${s} tiles in step 1 and ${d} more tiles in each step after that.`, s, d, k, N, X,
        asks: [`How many tiles are in step ${k}?`, `How many tiles are used for steps 1 through ${N} together?`, `Which step uses ${X} tiles?`], unit: ['tiles', 'tiles', 'step'] }; },
  ];
  const order = r.shuffle(ctx.map((_, i) => i));
  for (let i = 0; items.length < n && i < order.length * 3; i++) {
    const p = ctx[order[i % order.length]](); if (seen.has(p.text)) continue; seen.add(p.text);
    const ak = p.s + (p.k - 1) * p.d, SN = p.N * (2 * p.s + (p.N - 1) * p.d) / 2, row = (p.X - p.s) / p.d + 1;
    const fmt = (v, u) => u === '$' ? '$' + comma(v) : ['row', 'week', 'day', 'step'].includes(u) ? `${u} ${v}` : `${comma(v)} ${u}`;
    const ans = [fmt(ak, p.unit[0]), fmt(SN, p.unit[1]), fmt(row, p.unit[2])];
    items.push({ k: 'arithword', q: p.text, a: `a) ${ans[0]}; b) ${ans[1]}; c) ${ans[2]}`, d: { s: p.s, d: p.d, k: p.k, N: p.N, X: p.X } });
    blocks.push(`<div class="al-story"><p><span class="ws-num">${items.length}.</span> ${esc(p.text)}</p><ol class="al-sub" type="a">${p.asks.map((q, j) => `<li>${esc(q)} ${ab(ans[j], 6)}</li>`).join('')}</ol><div class="al-work" style="min-height:${n > 4 ? 0.5 : 0.9}in"></div></div>`);
  }
  return {
    ican: 'I can use arithmetic sequences and series to answer questions about rows, savings and patterns.',
    directions: 'Write aₙ = a₁ + (n − 1)d for each situation. Use it to find a term, use Sₙ = n(a₁ + aₙ)/2 for a total, and solve aₙ = the given value to find which term it is.',
    ex: example('First row 20 seats, 3 more each row. Row 10: a₁₀ = 20 + 9 · 3 = 47 seats.', 'First 10 rows: S₁₀ = 10(20 + 47)/2 = 335 seats. Row with 65 seats: 20 + (n − 1)3 = 65, so n = 16.'),
    parts: [part('Problems', blocks.join(''))], items,
    mistakes: 'Using n · d instead of (n − 1)d, adding only the first and last rows for a total, and forgetting to add 1 when finding which row.',
  };
}
function geoSum(a, rt, N) { let s = Q(0), t = Q(a); for (let i = 0; i < N; i++) { s = qadd(s, t); t = qmul(t, rt); } return s; }
function skSeries(r, n) {
  const items = [], cells = [];
  // the guided example
  const ga = r.pick([2, 3, 4, 5]), gr = r.pick([2, 3]), gn = r.pick([4, 5]);
  const gts = Array.from({ length: gn }, (_, i) => ga * gr ** i), S = gts.reduce((x, y) => x + y, 0);
  const rts = gts.map(t => t * gr);
  const guide = `<ol class="al-steps">
<li>Write the sum of the first ${gn} terms of ${F(`${ga}, ${ga * gr}, ${ga * gr * gr}, ...`)}: <i>S</i> = ${ab(gts.join(' + '), 12)} = ${ab(String(S), 3)}</li>
<li>Multiply every term by <i>r</i> = ${gr}: ${gr}<i>S</i> = ${ab(rts.join(' + '), 12)}</li>
<li>Subtract the first line from the second. Every term cancels except two: ${gr}<i>S</i> − <i>S</i> = ${ab(`${rts[gn - 1]} − ${ga}`, 6)}, so ${gr - 1 === 1 ? '' : gr - 1}<i>S</i> = ${ab(String(rts[gn - 1] - ga), 3)}.</li>
<li>Do the same with letters: <i>S</i> = <i>a</i> + <i>ar</i> + ... + <i>ar</i>ⁿ⁻¹ and <i>rS</i> = <i>ar</i> + <i>ar</i>² + ... + <i>ar</i>ⁿ. Subtract and solve for <i>S</i>: <i>S</i>ₙ = ${ab('a(1 − rⁿ)/(1 − r)', 9)}</li></ol>`;
  items.push({ k: 'seriesguide', q: `guided: ${ga}, r = ${gr}, n = ${gn}`, a: `S = ${S}; ${gr}S − S = ${rts[gn - 1] - ga}`, d: { ga, gr, gn, S } });
  const ps = r.distinct(n, () => {
    const T = r.pick(['list', 'list', 'sigma', 'sigma', 'word']), a = r.pick([1, 2, 3, 4, 5, 6, -2, -3]), rt = r.pick([Q(2), Q(3), Q(-2), Q(1, 2), Q(1, 3), Q(-3), Q(-1, 2)]), N = r.int(5, 10);
    if (Math.abs(a * qv(rt) ** (N - 1)) > 50000) return null;
    const ts = Array.from({ length: 3 }, (_, i) => qmul(Q(a), qpow(rt, i)));
    if (T === 'list') return { html: `Find the sum of the first ${N} terms: ${F(ts.map(qT).join(' + ').replace(/\+ −/g, '− ') + ' + ...')}`, q: `sum ${N} of ${ts.map(qT).join(', ')}`, a, rt, N };
    if (T === 'sigma') { const base = rt.d === 1 && rt.n > 0 ? String(rt.n) : `(${qT(rt)})`, coef = a === 1 ? '' : a === -1 ? MIN : num(a) + (rt.d === 1 && rt.n > 0 ? ' · ' : '');
      return { html: `Evaluate <span class="al-sig"><small>${N}</small>Σ<small><i>k</i> = 1</small></span> ${F(`${coef}${base}ᵏ⁻¹`)}`, q: `sigma ${N} ${coef}${base}`, a, rt, N }; }
    const w = r.pick([
      () => { const s = r.pick([1, 2, 3, 5]), d = r.int(6, 12); return { a: s, rt: Q(2), N: d, text: `${r.pick(NAMES)} puts ${s} ${s === 1 ? 'penny' : 'pennies'} in a jar on day 1 and doubles the amount each day. How many pennies are in the jar after ${d} days?` }; },
      () => { const s = r.pick([2, 3, 4]), d = r.int(5, 8); return { a: s, rt: Q(3), N: d, text: `The first round of a message reaches ${s} people. In each round after that, every person reached in the round before sends it to 3 new people. How many people in all have the message after ${d} rounds?` }; },
    ])();
    return { html: esc(w.text), q: w.text, a: w.a, rt: w.rt, N: w.N };
  }, x => x.q);
  ps.forEach((p, i) => { const s = qT(geoSum(p.a, p.rt, p.N)); items.push({ k: 'series', q: p.q, a: s, d: { a: p.a, r: [p.rt.n, p.rt.d], N: p.N } });
    cells.push(cell(i + 1, p.html, 0.75, `<i>S</i> = ${ab(s, 6)}`)); });
  return {
    ican: 'I can derive the formula for a finite geometric series and use it to find sums.',
    directions: 'Work through the guided example to see where the formula comes from. Then use Sₙ = a(1 − rⁿ)/(1 − r), where a is the first term, r the common ratio and n the number of terms. Give exact answers; fractions in lowest terms.',
    ex: example('3 + 6 + 12 + ... for 6 terms: a = 3, r = 2, n = 6.', 'S₆ = 3(1 − 2⁶)/(1 − 2) = 3(−63)/(−1) = 189.'),
    parts: [part('Guided derivation', guide), part('Use the formula', grid(cells))], items,
    mistakes: 'Using the last term\'s exponent as n, dropping the parentheses around a negative ratio (−2)ⁿ, and mixing up 1 − r with r − 1 on only one part of the fraction.',
  };
}
function skSeqMissing(r, n) {
  const items = [], cells = [];
  const ord = k => k + (k % 10 === 1 && k !== 11 ? 'st' : k % 10 === 2 && k !== 12 ? 'nd' : k % 10 === 3 && k !== 13 ? 'rd' : 'th');
  const ps = r.distinct(n, () => {
    const T = r.pick(['ca', 'cg', 'ba', 'bg']);
    if (T === 'ca' || T === 'ba') {
      const s = arithSeq(r), a1 = s.a1.n, d = s.d.n;
      if (T === 'ca') { const i = r.int(2, 5), j = i + r.int(2, 6), t = j + r.int(2, 6), at = k => a1 + (k - 1) * d;
        return { q: `The ${ord(i)} term is ${num(at(i))} and the ${ord(j)} term is ${num(at(j))}.`, ask: `Find a₁, d and the ${ord(t)} term.`, a: `a₁ = ${num(a1)}, d = ${num(d)}; a${sub(t)} = ${num(at(t))}`, d: { T: 'a', i, j, t, vi: at(i), vj: at(j) } }; }
      const len = r.int(5, 6), ts = Array.from({ length: len }, (_, k) => a1 + k * d), hide = r.sample([1, 2, 3, 4].filter(k => k < len - 1), 2).sort((x, y) => x - y);
      return { q: ts.map((x, k) => hide.includes(k) ? '___' : num(x)).join(', '), ask: 'Fill in the missing terms of this arithmetic sequence.', a: hide.map(k => num(ts[k])).join(', '), d: { T: 'ba', shown: ts.map((x, k) => hide.includes(k) ? null : x) } };
    }
    const rt = r.pick([2, 3, -2, -3, 4]), a1 = r.pick([1, 2, 3, 4, 5, -1, -2, -3]), at = k => a1 * rt ** (k - 1);
    if (T === 'cg') { const i = r.int(1, 4), j = i + r.pick([1, 3]), t = j + r.int(1, 3); if (Math.abs(at(t)) > 50000) return null;
      return { q: `The ${ord(i)} term is ${num(at(i))} and the ${ord(j)} term is ${num(at(j))}.`, ask: `This sequence is geometric. Find a₁, r and the ${ord(t)} term.`, a: `a₁ = ${num(a1)}, r = ${num(rt)}; a${sub(t)} = ${num(at(t))}`, d: { T: 'g', i, j, t, vi: at(i), vj: at(j) } }; }
    const ts = Array.from({ length: 5 }, (_, k) => at(k + 1)), hide = r.pick([[1, 2], [2, 3]]);
    return { q: ts.map((x, k) => hide.includes(k) ? '___' : num(x)).join(', '), ask: 'Fill in the missing terms of this geometric sequence.', a: hide.map(k => num(ts[k])).join(', '), d: { T: 'bg', shown: ts.map((x, k) => hide.includes(k) ? null : x) } };
  }, x => x.q);
  ps.forEach((p, i) => { items.push({ k: 'seqmiss', q: p.q, a: p.a, d: p.d });
    cells.push(cell(i + 1, `${esc(p.ask)}<br>${F(p.q)}`, 0.75, ab(p.a, 10))); });
  return {
    ican: 'I can find missing terms of arithmetic and geometric sequences from clues.',
    directions: 'Use the clues to find the common difference or ratio. Between the ith and jth terms there are j − i steps: an arithmetic sequence adds d at each step, a geometric one multiplies by r. Then work back to a₁ or forward to the term asked for.',
    ex: example('Geometric: the 3rd term is 12 and the 6th is 96. Three steps: r³ = 96/12 = 8, so r = 2.', 'a₁ = 12/2² = 3, and the 8th term is 3 · 2⁷ = 384.'),
    parts: [part('Puzzles', grid(cells))], items,
    mistakes: 'Dividing by j − i for a geometric sequence instead of taking a root, counting the terms instead of the steps, and losing a negative ratio.',
  };
}

/* ---------- precalculus: composition and decomposition ---------- */
// a function as text in x plus how to substitute an inner expression into it (simplified where it is a polynomial)
function fnPick(r, T) {
  const a = r.pick([2, 3, 4, 5, -2, -3]), b = nz(r, -9, 9), c = nz(r, -9, 9);
  if (T === 'lin') return { T, t: lin(a, b), cs: [b, a] };
  if (T === 'quad') return { T, t: poly([c, 0, 1]), cs: [c, 0, 1] };
  if (T === 'sqrt') return { T, t: `√(${fac(-c)})`, c };
  return { T: 'rec', t: '1/x' };
}
// outer(inner) as simplified text
function composeT(o, i) {
  if (o.cs && i.cs) { let out = [0]; o.cs.forEach((k, p) => { let pw = [1]; for (let j = 0; j < p; j++) pw = pmul(pw, i.cs); out = padd(out, pscale(pw, k)); }); return poly(out); }
  if (o.T === 'sqrt') return `√(${poly(padd(i.cs, [o.c]))})`;
  if (o.T === 'rec') return i.T === 'sqrt' ? `1/${i.t}` : `1/(${i.t})`;
  // polynomial outer, non-polynomial inner
  if (o.T === 'lin') { const [b, a] = o.cs; const head = i.T === 'rec' ? `${num(a)}/x` : `${a === 1 ? '' : a === -1 ? MIN : num(a)}${i.t}`; return `${head} ${b < 0 ? MIN : '+'} ${Math.abs(b)}`; }
  // quadratic x² + c outer
  const k = o.cs[0];
  if (i.T === 'sqrt') return poly([i.c + k, 1]);
  return `1/x² ${k < 0 ? MIN : '+'} ${Math.abs(k)}`;
}
function skCompose(r, n) {
  const [np, nd] = n, items = [], cells = [], dcells = [];
  const pairs = r.distinct(np, () => {
    const [A, B] = r.pick([['lin', 'lin'], ['lin', 'quad'], ['quad', 'lin'], ['quad', 'sqrt'], ['lin', 'sqrt'], ['lin', 'rec'], ['quad', 'rec']]);
    const f = fnPick(r, A), g = fnPick(r, B); if (f.t === g.t) return null; return { f, g };
  }, x => x.f.t + '|' + x.g.t);
  pairs.forEach((p, i) => { const fg = composeT(p.f, p.g), gf = composeT(p.g, p.f);
    items.push({ k: 'compose', q: `f(x) = ${p.f.t}, g(x) = ${p.g.t}`, a: `f(g(x)) = ${fg}; g(f(x)) = ${gf}`, f: p.f.t, g: p.g.t });
    cells.push(cell(i + 1, `${F(`f(x) = ${p.f.t}`)} and ${F(`g(x) = ${p.g.t}`)}`, 0.55, `<p>${F('f(g(x))')} = ${ab(fg, 8)}</p><p>${F('g(f(x))')} = ${ab(gf, 8)}</p>`)); });
  const D = [
    () => { const a = r.pick([2, 3, 4, 5]), b = nz(r, -9, 9), e = r.int(3, 8), inner = lin(a, b); return { h: `(${inner})${sup(e)}`, f: `x${sup(e)}`, g: inner }; },
    () => { const c = r.int(1, 25), inner = poly([c, 0, 1]); return { h: `√(${inner})`, f: '√x', g: inner }; },
    () => { const a = r.pick([2, 3, 5]), b = nz(r, -9, 9), inner = lin(a, b); return { h: `1/(${inner})`, f: '1/x', g: inner }; },
    () => { const k = r.int(2, 9), b = nz(r, -6, 6), inner = fac(-b); return { h: `${k}/(${inner})²`, f: `${k}/x²`, g: inner }; },
    () => { const a = r.pick([2, 3]), b = nz(r, -9, 9), c = nz(r, -9, 9), inner = lin(a, b); return { h: `√(${inner}) ${c < 0 ? MIN : '+'} ${Math.abs(c)}`, f: `√x ${c < 0 ? MIN : '+'} ${Math.abs(c)}`, g: inner }; },
    () => { const c = nz(r, -9, 9), e = r.pick([2, 3]), inner = poly([c, 0, 1]), k = r.int(2, 5); return { h: `${k}(${inner})${sup(e)}`, f: `${k}x${sup(e)}`, g: inner }; },
  ];
  const ds = r.distinct(nd, () => r.pick(D)(), x => x.h);
  ds.forEach((p, i) => { items.push({ k: 'decomp', q: `h(x) = ${p.h}`, a: `f(x) = ${p.f}, g(x) = ${p.g}`, h: p.h });
    dcells.push(cell(np + i + 1, `${F(`h(x) = ${p.h}`)}`, 0.3, `<p>${F('f(x)')} = ${ab(p.f, 5)} ${F('g(x)')} = ${ab(p.g, 6)}</p>`)); });
  return {
    ican: 'I can compose two functions in both orders and break a function into an inner and an outer part.',
    directions: 'Part A: find f(g(x)) and g(f(x)) and simplify. Order matters: in f(g(x)), g goes inside f. Part B: write each h(x) as f(g(x)), where g is the inner part and f is the outer part. Do not use g(x) = x.',
    ex: example('f(x) = x² + 1, g(x) = 2x − 3: f(g(x)) = (2x − 3)² + 1 = 4x² − 12x + 10, and g(f(x)) = 2(x² + 1) − 3 = 2x² − 1.', 'h(x) = (5x + 2)⁴ is f(g(x)) with f(x) = x⁴ and g(x) = 5x + 2.'),
    parts: [part('Part A: Compose', grid(cells)), part('Part B: Decompose', grid(dcells))], items,
    mistakes: 'Multiplying f and g instead of substituting, assuming f(g(x)) = g(f(x)), and squaring a binomial term by term.',
    notes: 'Part B has more than one right answer: the key gives the most common inner and outer parts. Accept any pair that composes back to h(x) without using the identity function.',
  };
}

/* ---------- rational functions ---------- */
function ratFn(r, T) {
  const k = r.pick([1, 1, 2, 3, -1, -2]);
  const [a, p, q, h] = r.sample([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 4);
  let N, D, hole = null, asym, dr;
  const L = z => [-z, 1];
  if (T === 'A') { N = pscale(L(a), k); D = L(p); asym = { m: 0, b: Q(k) }; dr = [p]; }
  else if (T === 'B') { N = pscale(L(a), k); D = pmul(L(p), L(q)); asym = { m: 0, b: Q(0) }; dr = [p, q]; }
  else if (T === 'C') { N = [k * r.pick([1, 2, 3, 4])]; dr = r.chance(.5) ? [p] : [p, q]; D = dr.reduce((acc, z) => pmul(acc, L(z)), [1]); asym = { m: 0, b: Q(0) }; }
  else if (T === 'D') { N = pscale(pmul(L(a), L(h)), k); D = pmul(L(p), L(h)); hole = [h, Q(k * (h - a), h - p)]; asym = { m: 0, b: Q(k) }; dr = [p, h]; }
  else if (T === 'E') { N = pscale(L(h), k); D = pmul(L(p), L(h)); hole = [h, Q(k, h - p)]; asym = { m: 0, b: Q(0) }; dr = [p, h]; }
  else { const b = r.int(-6, 6), c = r.int(-9, 9); N = [c, b, k]; D = L(p); if (pval(N, p) === 0) return null; asym = { m: k, b: Q(b + k * p), slant: true }; dr = [p]; }
  const va = dr.filter(z => !hole || z !== hole[0]).sort((x, y) => x - y);
  return { T, N, D, va, hole, asym, k };
}
function asymT(s) { return s.slant ? `y = ${sum([[s.m, 'x'], [s.b, '']])}` : `y = ${qT(s.b)}`; }
function endT(s) {
  if (!s.slant) return `f(x) → ${qT(s.b)} as x → ±∞`;
  return s.m > 0 ? 'f(x) → ∞ as x → ∞; f(x) → −∞ as x → −∞' : 'f(x) → −∞ as x → ∞; f(x) → ∞ as x → −∞';
}
function skRational(r, n) {
  const [nf, ns] = n, items = [], cells = [];
  const fs = r.distinct(nf, () => ratFn(r, r.pick(['A', 'B', 'C', 'D', 'E', 'F', 'D', 'F'])), x => poly(x.N) + '|' + poly(x.D));
  fs.forEach((f, i) => {
    const va = f.va.length ? f.va.map(z => `x = ${num(z)}`).join(', ') : 'none', hole = f.hole ? pt(f.hole[0], f.hole[1]) : 'none', as = asymT(f.asym), eb = endT(f.asym);
    items.push({ k: 'rational', q: `f(x) = ${wrap(poly(f.N))}/${wrap(poly(f.D))}`, a: `VA: ${va}; hole: ${hole}; ${f.asym.slant ? 'slant' : 'HA'}: ${as}; end: ${eb}`, N: poly(f.N), D: poly(f.D), va: f.va, hole: f.hole && [f.hole[0], qv(f.hole[1])], asym: [f.asym.m, qv(f.asym.b)] });
    cells.push(cell(i + 1, `${F('f(x)')} = ${frac(F(poly(f.N)), F(poly(f.D)))}`, 0.45,
      `<p>Vertical asymptotes: ${ab(va, 6)}</p><p>Holes: ${ab(hole, 5)}</p><p>Horizontal or slant asymptote: ${ab(as, 5)}</p><p>End behavior: ${ab(eb, 11)}</p>`));
  });
  const sk = fs.slice(0, ns).map((f, i) => {
    const fx = x => pval(f.N, x) / pval(f.D, x);
    const svg = plane({ xlo: -8, xhi: 8, S: 12 }, g => `<g class="ws-ans">${f.va.map(z => lineMark(g, 0, 0, RED, true, z)).join('')}${lineMark(g, f.asym.m, qv(f.asym.b), RED, true)}${curveMark(g, fx, RED)}${f.hole ? `<circle cx="${g.X(f.hole[0])}" cy="${g.Y(qv(f.hole[1]))}" r="3.6" fill="#fff" stroke="${RED}" stroke-width="1.6"/>` : ''}</g>`, `Blank grid to sketch problem ${i + 1}`);
    return `<div class="al-graph"><p><span class="ws-num">${i + 1}.</span> Sketch ${F('f(x)')} = ${frac(F(poly(f.N)), F(poly(f.D)))}</p>${svg}</div>`;
  });
  return {
    ican: 'I can find the vertical asymptotes, holes, horizontal or slant asymptote and end behavior of a rational function.',
    directions: 'Factor the top and bottom. A factor that cancels makes a hole; give its point. A zero of the bottom that is left makes a vertical asymptote. Compare degrees for the horizontal asymptote, and divide when the top is one degree higher to find a slant asymptote. Then sketch the first two.',
    ex: example(`${frac('<i>x</i>² − 1', '<i>x</i>² − 3<i>x</i> + 2')} = ${frac('(<i>x</i> − 1)(<i>x</i> + 1)', '(<i>x</i> − 1)(<i>x</i> − 2)')}: hole at (1, −2), vertical asymptote x = 2.`, 'Same degree on top and bottom, so the horizontal asymptote is y = 1/1 = 1, and f(x) → 1 as x → ±∞.'),
    parts: [part('Practice', grid(cells)), part('Sketch', `<div class="al-grid al-c2">${sk.join('')}</div>`)], items,
    mistakes: 'Calling a canceled factor an asymptote, forgetting the y-value of a hole, and using the ratio of leading coefficients when the degrees differ.',
  };
}

/* ---------- 2 by 2 matrices ---------- */
const matT = m => `[${m[0].map(qT).join(', ')}; ${m[1].map(qT).join(', ')}]`;
const matH = (m, cls = '') => `<span class="al-mx${cls}"><span>${m[0].map(x => `<span>${F(typeof x === 'string' ? x : qT(x))}</span>`).join('')}</span><span>${m[1].map(x => `<span>${F(typeof x === 'string' ? x : qT(x))}</span>`).join('')}</span></span>`;
function skMatrix(r, n) {
  const [nm, ns] = n, items = [], cells = [], scells = [];
  const ms = r.distinct(nm, () => {
    const sing = r.chance(.15), a = nz(r, -6, 6), b = r.int(-6, 6), c = r.int(-6, 6);
    let d;
    if (sing) { if (!b || !c || (b * c) % a) return null; d = b * c / a; }
    else { d = r.int(-6, 6); const det = a * d - b * c; if (!det || Math.abs(det) > 6) return null; }
    return [[a, b], [c, d]];
  }, x => JSON.stringify(x));
  ms.forEach((m, i) => {
    const det = m[0][0] * m[1][1] - m[0][1] * m[1][0];
    const inv = det ? [[Q(m[1][1], det), Q(-m[0][1], det)], [Q(-m[1][0], det), Q(m[0][0], det)]] : null;
    items.push({ k: 'matrix', q: `A = ${matT(m)}`, a: `det = ${num(det)}; ${inv ? 'A⁻¹ = ' + matT(inv) : 'no inverse'}`, m, det, inv: inv && inv.map(row => row.map(x => [x.n, x.d])) });
    cells.push(cell(i + 1, `${F('A')} = ${matH(m)}`, 0.5, `<p>det ${F('A')} = ${ab(num(det), 3)}</p><p>${F('A⁻¹')} = <span class="ws-blank al-sysblank"><span class="ws-ans">${inv ? matH(inv, ' al-mxk') : 'no inverse'}</span></span></p>`));
  });
  const ss = r.distinct(ns, () => {
    const a = nz(r, -5, 5), b = nz(r, -5, 5), c = nz(r, -5, 5), d = nz(r, -5, 5), det = a * d - b * c; if (!det || Math.abs(det) > 12) return null;
    const x = r.int(-6, 6), y = r.int(-6, 6); return { a, b, c, d, x, y, e: a * x + b * y, f: c * x + d * y };
  }, s => [s.a, s.b, s.c, s.d].join());
  ss.forEach((s, i) => {
    const e1 = `${sum([[s.a, 'x'], [s.b, 'y']])} = ${num(s.e)}`, e2 = `${sum([[s.c, 'x'], [s.d, 'y']])} = ${num(s.f)}`, ans = `x = ${num(s.x)}, y = ${num(s.y)}`;
    items.push({ k: 'msys', q: `${e1}; ${e2}`, a: ans, eqs: [e1, e2] });
    scells.push(cell(nm + i + 1, `${sys(e1, e2)}`, 0.8, `<p>Matrix form: ${matH([[s.a, s.b], [s.c, s.d]])} ${matH([['x'], ['y']])} = ${matH([[s.e], [s.f]])}</p><p>${ab(ans, 7)}</p>`));
  });
  return {
    ican: 'I can find the determinant and inverse of a 2 by 2 matrix and use the inverse to solve a system.',
    directions: 'For A = [a b; c d], det A = ad − bc. If det A ≠ 0, A⁻¹ = (1/det A)[d −b; −c a]: swap a and d, change the signs of b and c, and divide every entry by the determinant. If det A = 0, write "no inverse". For each system, write AX = B and solve with X = A⁻¹B.',
    ex: example('A = [4 3; 1 1]: det A = 4 − 3 = 1, so A⁻¹ = [1 −3; −1 4].', '4x + 3y = 10 and x + y = 3: X = A⁻¹B = [1 −3; −1 4][10; 3] = [1; 2], so x = 1, y = 2.'),
    parts: [part('Part A: Determinants and inverses', grid(cells, 3)), part('Part B: Solve with inverse matrices', grid(scells))], items,
    mistakes: 'Computing bc − ad, swapping b and c instead of a and d, and multiplying B times A⁻¹ in the wrong order.',
  };
}

/* ---------- conic sections ---------- */
const sqT = (h, v) => h === 0 ? `${v}²` : `(${fac(h, v)})²`;
const ptR = (x, y) => `(${x}, ${y})`;
// h + s·√c2 as simplified text
const radSum = (h, s, c2) => { if (isSq(c2)) return num(h + s * Math.sqrt(c2)); const R = radT(c2); return h ? `${num(h)} ${s < 0 ? MIN : '+'} ${R}` : (s < 0 ? MIN : '') + R; };
function paramMark(g, fx, fy, t0, t1, color, N = 200) {
  let d = ''; for (let i = 0; i <= N; i++) { const t = t0 + (t1 - t0) * i / N; d += `${i ? 'L' : 'M'}${g.X(fx(t))} ${g.Y(fy(t)).toFixed(1)}`; }
  return `<path d="${d}" fill="none" stroke="${color}" stroke-width="2.2"/>`;
}
function skCircles(r, n) {
  const [ng, nd] = n, items = [], cells = [];
  const ps = r.distinct(ng, () => {
    const h = r.int(-8, 8), k = r.int(-8, 8), r2 = r.pick([4, 9, 16, 25, 36, 49, 64, 81, 100, 8, 12, 18, 20, 27, 32]), L = r.pick([1, 1, 1, 2, 3]);
    if (!h && !k) return null;
    const D = -2 * h * L, E = -2 * k * L, Fc = (h * h + k * k - r2) * L;
    const eq = `${sum([[L, 'x²'], [L, 'y²'], [D, 'x'], [E, 'y'], [Fc, '']])} = 0`;
    return { eq, h, k, r2 };
  }, x => x.eq);
  ps.forEach((p, i) => { const a = `center ${pt(p.h, p.k)}; r = ${radT(p.r2)}`; items.push({ k: 'circle', q: p.eq, a, h: p.h, ck: p.k, r2: p.r2 });
    cells.push(cell(i + 1, F(p.eq), 0.75, `<p>Center: ${ab(pt(p.h, p.k), 4)} Radius: ${ab(radT(p.r2), 3)}</p>`)); });
  const gs = r.distinct(nd, () => ({ h: r.int(-4, 4), k: r.int(-4, 4), rr: r.int(2, 4) }), x => JSON.stringify(x)).map((c, i) => {
    const eq = `${sqT(c.h, 'x')} + ${sqT(c.k, 'y')} = ${c.rr * c.rr}`;
    items.push({ k: 'circleq', q: `graph: center ${pt(c.h, c.k)}, radius ${c.rr}`, a: eq, h: c.h, ck: c.k, rr: c.rr });
    const svg = plane({ xlo: -8, xhi: 8, S: 12 }, g => paramMark(g, t => c.h + c.rr * Math.cos(t), t => c.k + c.rr * Math.sin(t), 0, 2 * Math.PI, '#222') + dot(g, c.h, c.k), `A circle with center ${pt(c.h, c.k)} and radius ${c.rr}`);
    return `<div class="al-graph"><p><span class="ws-num">${ng + i + 1}.</span> Write the equation of the circle.</p>${svg}<p class="al-ans">${ab(eq, 12)}</p></div>`;
  });
  return {
    ican: 'I can complete the square to find the center and radius of a circle and write a circle\'s equation from its graph.',
    directions: 'Divide by the number in front of x² if it is not 1. Group the x terms and the y terms, move the constant, and complete the square for each. Write (x − h)² + (y − k)² = r², then read the center (h, k) and radius r. Simplify radicals.',
    ex: example('x² + y² − 6x + 4y − 3 = 0 → (x² − 6x + 9) + (y² + 4y + 4) = 3 + 9 + 4.', '(x − 3)² + (y + 2)² = 16: center (3, −2), radius 4.'),
    parts: [part('Find the center and radius', grid(cells)), part('From a graph', `<div class="al-grid al-c2">${gs.join('')}</div>`)], items,
    mistakes: 'Adding the completing-the-square numbers to only one side, reading the center as (−3, 2) from (x − 3)² + (y + 2)², and giving r² as the radius.',
  };
}
// a conic in standard form with its expanded general form
function conicOne(r, T) {
  const h = r.int(-5, 5), k = r.int(-5, 5);
  let std, G, type;   // G: [A, C, D, E, F] for A x² + C y² + D x + E y + F = 0
  if (T === 'circle') { const r2 = r.pick([4, 9, 16, 25, 36]); std = `${sqT(h, 'x')} + ${sqT(k, 'y')} = ${r2}`; G = [1, 1, -2 * h, -2 * k, h * h + k * k - r2]; type = 'circle'; }
  else if (T === 'ellipse' || T === 'hyperbola') {
    const [a2, b2] = r.sample([1, 4, 9, 16, 25, 36], 2), s = T === 'ellipse' ? 1 : -1, yfirst = T === 'hyperbola' && r.chance(.5);
    const xt = a2 === 1 ? sqT(h, 'x') : `${sqT(h, 'x')}/${a2}`, yt = b2 === 1 ? sqT(k, 'y') : `${sqT(k, 'y')}/${b2}`;
    if (T === 'ellipse') { std = `${xt} + ${yt} = 1`; G = [b2, a2, -2 * h * b2, -2 * k * a2, b2 * h * h + a2 * k * k - a2 * b2]; }
    else if (!yfirst) { std = `${xt} ${MIN} ${yt} = 1`; G = [b2, -a2, -2 * h * b2, 2 * k * a2, b2 * h * h - a2 * k * k - a2 * b2]; }
    else { std = `${yt} ${MIN} ${xt} = 1`; G = [-b2, a2, 2 * h * b2, -2 * k * a2, -b2 * h * h + a2 * k * k - a2 * b2]; }
    type = T; if (G[0] < 0) G = G.map(x => -x);
  } else {
    const p4 = r.pick([4, 8, 12, -4, -8, 2, -2, 6]), xside = r.chance(.5);
    if (xside) { std = `${sqT(k, 'y')} = ${num(p4)}(${fac(h)})`.replace(/= 1\(/, '= (').replace(/= −1\(/, '= −('); G = [0, 1, -p4, -2 * k, k * k + p4 * h]; }
    else { std = `${sqT(h, 'x')} = ${num(p4)}(${fac(k, 'y')})`; G = [1, 0, -2 * h, -p4, h * h + p4 * k]; }
    if (h === 0 && xside) std = std.replace(/\(x\)$/, 'x'); if (k === 0 && !xside) std = std.replace(/\(y\)$/, 'y');
    type = 'parabola';
  }
  const g = Math.abs(G.reduce((x, y) => gcd(x, y))); if (g > 1) G = G.map(x => x / g);
  const gen = `${sum([[G[0], 'x²'], [G[1], 'y²'], [G[2], 'x'], [G[3], 'y'], [G[4], '']])} = 0`;
  return { std, gen, type, h, k };
}
function skConicClass(r, n) {
  const items = [], cells = [];
  const types = r.shuffle(Array.from({ length: n }, (_, i) => ['circle', 'ellipse', 'hyperbola', 'parabola'][i % 4]));
  const seen = new Set();
  types.forEach(T => { for (let t = 0; t < 40; t++) { const c = conicOne(r, T); if (seen.has(c.gen)) continue; seen.add(c.gen);
    items.push({ k: 'conic', q: c.gen, a: `${c.std}; ${c.type}`, std: c.std, type: c.type });
    cells.push(cell(items.length, F(c.gen), 0.95, `<p>Standard form: ${ab(c.std, 11)}</p><p>Type: ${ab(c.type, 5)}</p>`)); break; } });
  return {
    ican: 'I can complete the square to put a second-degree equation in standard form and name the conic.',
    directions: 'Group the x terms and the y terms, factor out the number in front of each squared term, and complete the square. Divide so the right side is 1 (or, for a parabola, solve for the squared part). Then classify: same signs and same numbers in front of x² and y² is a circle, same signs different numbers an ellipse, opposite signs a hyperbola, only one squared term a parabola.',
    ex: example('4x² + 9y² − 16x + 18y − 11 = 0 → 4(x² − 4x + 4) + 9(y² + 2y + 1) = 11 + 16 + 9 = 36.', 'Divide by 36: (x − 2)²/9 + (y + 1)²/4 = 1, an ellipse.'),
    parts: [part('Practice', grid(cells))], items,
    mistakes: 'Adding 4 instead of 4 · 4 = 16 to the right side after factoring out a 4, and calling an ellipse a circle when only the signs match.',
  };
}
function ellHypOne(r, T) {
  const h = r.int(-3, 3), k = r.int(-3, 3), vert = r.chance(.4);
  let A, B, c2;
  if (T === 'ellipse') { [A, B] = r.pick([[5, 3], [5, 4], [4, 2], [5, 2], [3, 2], [4, 3], [5, 1], [3, 1]]); c2 = A * A - B * B; }
  else { A = r.int(1, 4); B = r.int(1, 4); c2 = A * A + B * B; }
  const big = sqT(vert ? k : h, vert ? 'y' : 'x'), small = sqT(vert ? h : k, vert ? 'x' : 'y');
  const fr = (s, d) => d === 1 ? s : `${s}/${d}`;
  const eq = T === 'ellipse' ? (vert ? `${fr(small, B * B)} + ${fr(big, A * A)} = 1` : `${fr(big, A * A)} + ${fr(small, B * B)} = 1`) : `${fr(big, A * A)} ${MIN} ${fr(small, B * B)} = 1`;
  const P = (s, along) => vert ? ptR(num(h), along) : ptR(along, num(k));
  const c0 = vert ? k : h;
  const vs = [P(-1, num(c0 - A)), P(1, num(c0 + A))], fs = [P(-1, radSum(c0, -1, c2)), P(1, radSum(c0, 1, c2))];
  return { T, h, k, A, B, c2, vert, eq, a: `center ${pt(h, k)}; vertices ${vs.join(', ')}; foci ${fs.join(', ')}`, vs, fs };
}
function skEllHyp(r, n) {
  const [nf, ns] = n, items = [], cells = [];
  const ps = r.distinct(nf, () => ellHypOne(r, r.chance(.5) ? 'ellipse' : 'hyperbola'), x => x.eq);
  ps.forEach((p, i) => { items.push({ k: 'ellhyp', q: p.eq, a: p.a, T: p.T });
    cells.push(cell(i + 1, F(p.eq), 0.5, `<p>Center: ${ab(pt(p.h, p.k), 4)}</p><p>Vertices: ${ab(p.vs.join(', '), 8)}</p><p>Foci: ${ab(p.fs.join(', '), 10)}</p>`)); });
  const sk = ps.slice(0, ns).map((p, i) => {
    const svg = plane({ xlo: -8, xhi: 8, S: 12 }, g => {
      const ax = p.vert ? [t => p.h, t => p.k] : null;
      let s;
      if (p.T === 'ellipse') s = p.vert ? paramMark(g, t => p.h + p.B * Math.cos(t), t => p.k + p.A * Math.sin(t), 0, 2 * Math.PI, RED) : paramMark(g, t => p.h + p.A * Math.cos(t), t => p.k + p.B * Math.sin(t), 0, 2 * Math.PI, RED);
      else {
        const m = p.vert ? p.A / p.B : p.B / p.A;
        s = [1, -1].map(sg => p.vert ? paramMark(g, t => p.h + p.B * Math.sinh(t), t => p.k + sg * p.A * Math.cosh(t), -3, 3, RED) : paramMark(g, t => p.h + sg * p.A * Math.cosh(t), t => p.k + p.B * Math.sinh(t), -3, 3, RED)).join('')
          + lineMark(g, m, p.k - m * p.h, RED, true) + lineMark(g, -m, p.k + m * p.h, RED, true);
      }
      return `<g class="ws-ans">${s}${dot(g, p.h, p.k, RED)}</g>`;
    }, `Blank grid to sketch problem ${i + 1}`);
    return `<div class="al-graph"><p><span class="ws-num">${i + 1}.</span> Sketch ${F(p.eq)}</p>${svg}</div>`;
  });
  return {
    ican: 'I can find the center, vertices and foci of an ellipse or hyperbola from its equation and sketch it.',
    directions: 'Read the center (h, k). The larger denominator of an ellipse (the first one of a hyperbola) is a², and its variable tells the direction of the vertices, a units from the center. Ellipse: c² = a² − b². Hyperbola: c² = a² + b². The foci are c units from the center in the same direction. Then sketch the first two.',
    ex: example('(x − 1)²/25 + (y + 2)²/9 = 1: center (1, −2), a = 5, b = 3, c = √(25 − 9) = 4.', 'Vertices (−4, −2), (6, −2); foci (−3, −2), (5, −2).'),
    parts: [part('Practice', grid(cells)), part('Sketch', `<div class="al-grid al-c2">${sk.join('')}</div>`)], items,
    mistakes: 'Using c² = a² + b² for an ellipse, putting the vertices along the wrong axis, and forgetting the center shift on the foci.',
  };
}

/* ---------- the skill list ---------- */
const COURSES = [['g8', 'Grade 8 math'], ['alg1', 'Algebra 1'], ['geo', 'Geometry'], ['alg2', 'Algebra 2'], ['pre', 'Precalculus']];
// id: [title, courses, maker, counts for s/m/l, minutes, materials]
const SK = {
  slope: ['Slope From Graphs and Points', 'g8', skSlope, [6, 8, 10], 30],
  line: ['Equations of Lines', 'g8 alg1', skLine, [6, 8, 10], 30],
  roots: ['Square and Cube Root Equations', 'g8', skRoots, [6, 10, 12], 25],
  squeeze: ['Squeeze the Square Root', 'g8', skSqueeze, [6, 8, 10], 30],
  expo: ['Exponent Rules', 'g8', skExpRules, [[6, 6], [8, 8], [9, 12]], 30],
  sysgraph: ['Solve Systems by Graphing', 'g8 alg1', skSysGraph, [2, 4, 6], 30, 'pencil, ruler'],
  sysalg: ['Substitution and Elimination', 'alg1', skSysAlg, [6, 8, 10], 35],
  sysword: ['Systems in Real Problems', 'g8 alg1', skSysWord, [3, 4, 5], 35],
  sysineq: ['Systems of Inequalities', 'alg1', skSysIneq, [2, 3, 4], 30, 'pencil, ruler, colored pencil'],
  fnnot: ['Evaluate and Interpret Functions', 'alg1', skFnNotation, [6, 10, 12], 30],
  fnornot: ['Function or Not', 'g8 alg1', skFnOrNot, [9, 12, 12], 30, 'pencil, scissors'],
  rate: ['Average Rate of Change', 'alg1', skRate, [2, 4, 6], 30],
  linexp: ['Linear or Exponential', 'alg1', skLinExp, [4, 6, 8], 30],
  polymul: ['Multiply Polynomials With Area Models', 'alg1', skPolyMul, [6, 8, 10], 30],
  factor: ['Factoring Task Cards', 'alg1', skFactor, [9, 15, 18], 35, 'pencil, scissors'],
  qfactor: ['Solve Quadratics by Factoring', 'alg1', skQFactor, [8, 10, 12], 30],
  qsquare: ['Square Roots and Completing the Square', 'alg1', skQSquare, [6, 8, 10], 35],
  qformula: ['The Quadratic Formula and the Discriminant', 'alg1 alg2', skQFormula, [6, 8, 10], 35],
  forms: ['Factored and Vertex Form', 'alg1', skForms, [3, 4, 5], 35],
  proj: ['Launch and Landing', 'alg1', skProjectile, [3, 4, 5], 35, 'pencil, calculator'],
  compound: ['Compound and Literal Inequalities', 'alg1', skCompound, [6, 8, 10], 30],
  complex: ['Complex Number Arithmetic', 'alg2', skComplex, [9, 12, 15], 25],
  qcomplex: ['Quadratics With Complex Solutions', 'alg2', skQComplex, [6, 8, 10], 35],
  remainder: ['The Remainder Theorem', 'alg2', skRemainder, [6, 10, 12], 30],
  ratsimp: ['Simplify Rational Expressions', 'alg2', skRatSimp, [8, 10, 12], 30],
  ratadd: ['Add and Subtract Rational Expressions', 'alg2', skRatAdd, [6, 8, 10], 35],
  extraneous: ['Extraneous Solution Hunt', 'alg2', skExtraneous, [6, 8, 10], 40],
  logform: ['Logs Are Exponents', 'alg2', skLogForm, [[8, 6], [12, 6], [12, 9]], 25],
  logprop: ['Log Properties Match-Up', 'alg2', skLogProp, [[8, 2], [12, 4], [12, 6]], 30],
  expeq: ['Solve Exponential Equations', 'alg2', skExpEq, [6, 8, 10], 35, 'pencil, calculator'],
  growth: ['Growth and Decay', 'alg2', skGrowth, [4, 6, 8], 40, 'pencil, calculator'],
  combine: ['Combine Functions', 'alg2', skCombine, [6, 8, 10], 35],
  inverse: ['Inverse Functions', 'alg2 pre', skInverse, [6, 8, 10], 35],
  seqsort: ['Sequence Card Sort', 'alg2', skSeqSort, [[9, 4], [12, 6], [12, 8]], 35, 'pencil, scissors'],
  arithword: ['Arithmetic Sequences in Real Problems', 'alg2', skArithWord, [3, 4, 6], 35],
  series: ['Finite Geometric Series', 'alg2', skSeries, [4, 6, 8], 35],
  seqmissing: ['Missing Terms Puzzle', 'alg2', skSeqMissing, [6, 8, 10], 30],
  compose: ['Composition and Decomposition', 'pre', skCompose, [[4, 2], [6, 4], [8, 4]], 35],
  rational: ['Rational Functions', 'pre', skRational, [[6, 2], [8, 2], [10, 2]], 40, 'pencil, ruler'],
  matrix: ['Inverse Matrices and Systems', 'pre', skMatrix, [[3, 2], [6, 4], [9, 4]], 35],
  circles: ['Circle Equations', 'geo alg2 pre', skCircles, [[6, 2], [8, 2], [10, 2]], 35],
  conicclass: ['Complete the Square to Classify', 'pre', skConicClass, [4, 6, 8], 35],
  ellhyp: ['Ellipses and Hyperbolas', 'pre', skEllHyp, [[6, 2], [8, 2], [10, 2]], 40, 'pencil, ruler'],
};
const SKDEF = { g8: 'slope', alg1: 'line', geo: 'circles', alg2: 'complex', pre: 'compose' };
const nOf = (v) => { const s = SK[v.skill] || SK.line; return s[3][{ s: 0, m: 1, l: 2 }[v.count] ?? 1]; };
const nText = c => Array.isArray(c) ? `${c[0]} + ${c[1]}` : String(c);

/* ---------- verify: each kind re-worked a different way ---------- */
const XS = [0.37, 1.71, -2.43, 3.19, -0.83];
const sameAt = (a, b, env = {}, xs = XS) => xs.every(x => { const p = safe(() => ev(a, { ...env, x })), q = safe(() => ev(b, { ...env, x })); if (p === undefined && q === undefined) return true;
  if (!p || !q || p.length !== q.length) return false; return p.every((u, i) => closeC(u, q[i])); });
const numsIn = s => (String(s).replace(/−/g, '-').match(/-?\d+(\.\d+)?/g) || []).map(Number);
const parsePt = s => { const m = String(s).match(/^\((.+), (.+)\)$/); return m ? [evR(m[1]), evR(m[2])] : null; };
const ptsIn = s => [...String(s).matchAll(/\(([^()]*(?:\([^()]*\))?[^()]*), ([^()]*(?:\([^()]*\))?[^()]*)\)/g)].map(m => [evR(m[1]), evR(m[2])]);
function parseMat(s) { const m = s.match(/\[(.*); (.*)\]/); return m ? [m[1], m[2]].map(row => row.split(', ').map(t => evR(t))) : null; }
function horner(cs, c) { let rr = 0; for (let p = cs.length - 1; p >= 0; p--) rr = rr * c + cs[p]; return rr; }
function inIv(iv, x) {   // membership in an interval-notation answer
  return iv.split(' ∪ ').some(part => { const m = part.match(/^([[(])(.+), (.+)([\])])$/); if (!m) throw new Error('bad interval ' + iv);
    const lo = m[2].includes('∞') ? -Infinity : evR(m[2]), hi = m[3].includes('∞') ? Infinity : evR(m[3]);
    return (m[1] === '[' ? x >= lo - 1e-9 : x > lo + 1e-9) && (m[4] === ']' ? x <= hi + 1e-9 : x < hi - 1e-9); });
}
const holdsS = (eq, env) => safe(() => holds(eq, env)) === true;
// both sides of "left = right" as a value
const sideDiff = (eq, env) => { const [L, R] = eq.split(' = '); return C.sub(ev1(L, env), ev1(R, env)); };

const VER = {
  same: it => sameAt(it.q, it.a) ? [] : [`${it.q} is not ${it.a}`],
  slope: it => { const [x1, y1] = it.P1, [x2, y2] = it.P2, [s, prop] = it.a.split('; '), m = (y2 - y1) / (x2 - x1), o = [];
    if (!close(evR(s), m)) o.push(`slope of ${it.q} is ${m}, key ${s}`);
    const thru0 = Math.abs(y1 - m * x1) < 1e-9;
    if (thru0 !== (prop !== 'not proportional')) o.push(`${it.q}: proportional is ${thru0}`);
    if (thru0 && !(holdsS(prop, { x: x1, y: y1 }) && holdsS(prop, { x: x2, y: y2 }))) o.push(`${prop} misses the points`);
    return o; },
  line: it => { const o = []; if (!holdsS(it.a, { x: it.P[0], y: it.P[1] }) || !holdsS(it.a, { x: it.P2[0], y: it.P2[1] })) o.push(`${it.a} misses the line of ${it.q}`);
    if (it.form === 'si' && !/^y = [^y]*$/.test(it.a)) o.push(`${it.a} not slope-intercept`);
    if (it.form === 'std') { const [A, B, Cc] = lineCoef(it.a); if (!/^[^=]*y? = −?\d+$/.test(it.a) || A < 0 || !Number.isInteger(A) || !Number.isInteger(B) || !Number.isInteger(Cc) || gcd(gcd(Math.abs(A), Math.abs(B)), Math.abs(Cc)) !== 1) o.push(`${it.a} not standard form`); }
    return o; },
  root: it => { const vals = rootsOf(it.a), o = []; if (vals.length !== (it.p === 2 ? 2 : 1)) o.push(`${it.q}: ${it.a} wrong count`);
    vals.forEach(v => { if (!holdsS(it.q, { x: v })) o.push(`${it.q}: ${it.a} fails`); }); return o; },
  cube: it => { const k = numsIn(it.a)[0]; return k ** 3 === it.V ? [] : [`edge ${k} for ${it.V}`]; },
  squeeze: it => { const [a, b, t] = numsIn(it.a); return a * a < it.v && it.v < b * b && b === a + 1 && Math.abs(t - Math.sqrt(it.v)) <= 0.05 + 1e-9 ? [] : [`squeeze ${it.v}: ${it.a}`]; },
  expo: it => { const env = { a: 1.7, y: 0.9, m: 2.1 }; const o = [];
    if (it.part === 'A') { const [ex, res] = it.a.split(' = '); if (!sameAt(it.q, ex, env) || !sameAt(it.q, res, env)) o.push(`${it.q}: ${it.a}`); }
    else { if (!sameAt(it.q, it.a, env)) o.push(`${it.q} is not ${it.a}`); if (/⁻|(?<![¹²³⁴⁵⁶⁷⁸⁹])⁰/.test(it.a)) o.push(`${it.a} keeps a zero or negative exponent`); }
    return o; },
  sys: it => { const p = parsePt(it.a); return p && it.eqs.every(e => holdsS(e, { x: p[0], y: p[1] })) ? [] : [`${it.q}: ${it.a}`]; },
  story: it => { const o = []; if (!it.sys.every(e => holdsS(e, it.env))) o.push(`story system fails: ${it.q}`);
    Object.values(it.env).forEach(x => { if (!numsIn(it.a.replace(/,(?=\d{3})/g, '')).includes(x)) o.push(`story answer ${it.a} lacks ${x}`); });
    if (it.kind === 'plans' && !(it.d.r2 < it.d.r1 && it.a.includes(it.d.B))) o.push('plans: cheaper plan wrong'); return o; },
  ineqpt: it => { const inside = it.ineqs.every(e => holdsS(e, { x: it.x, y: it.y })); return (inside ? 'yes' : 'no') === it.a ? [] : [`${it.q}: ${it.a}`]; },
  fn: it => { const f = x => evR(it.rule, { x });
    if (it.solve != null) { const x = evR(it.a.replace('x = ', '')); return close(f(x), it.solve) ? [] : [`${it.q}: ${it.a}`]; }
    if (it.expr) return [1.3, -2.2].every(t => close(evR(it.a, { a: t }), f(t + it.expr))) ? [] : [`${it.q}: ${it.a}`];
    const x = evR(it.ask.replace(/^[a-z]\((.*)\)$/, '$1')); return close(f(x), evR(it.a)) ? [] : [`${it.q}: ${it.a}`]; },
  ctx: it => { const v = it.N0 * Math.pow(it.b, it.t); return v === it.v && it.a.includes(`${comma(v)} cells`) && it.a.includes(`${it.t} hours`) ? [] : [`ctx ${it.q}`]; },
  rate: it => { const f = x => evR(it.rule, { x }); return close((f(it.x2) - f(it.x1)) / (it.x2 - it.x1), evR(it.a)) ? [] : [`${it.q}: ${it.a}`]; },
  linexp: it => { const ys = it.ys.map(y => evR(y)), [type, rule] = it.a.split('; '), o = [];
    const d = ys.slice(1).map((y, i) => y - ys[i]), lin1 = d.every(x => close(x, d[0])), rt = ys.slice(1).map((y, i) => y / ys[i]), geo = rt.every(x => close(x, rt[0]));
    if ((type === 'linear') !== lin1 || (type === 'exponential') !== (geo && !lin1)) o.push(`linexp type ${it.q}`);
    it.xs.forEach((x, i) => { if (!close(evR(rule.replace('y = ', ''), { x }), ys[i])) o.push(`${rule} misses ${x}`); }); return o; },
  fnornot: it => { const f = it.pairs.every(([x, y]) => it.pairs.every(([x2, y2]) => x !== x2 || y === y2)); return (f ? 'function' : 'not a function') === it.a ? [] : [`${it.q}: ${it.a}`]; },
  why: it => { const f = it.pairs.every(([x, y]) => it.pairs.every(([x2, y2]) => x !== x2 || y === y2)); return f === !it.a.includes('not a function') ? [] : [`why ${it.q}`]; },
  poly: it => { const o = sameAt(it.q, it.a) ? [] : [`${it.q} is not ${it.a}`]; it.cells.forEach(([a, b, c]) => { if (!sameAt(`(${a})(${b})`, c)) o.push(`box ${a} by ${b} is not ${c}`); }); return o; },
  polycheck: it => close(evR(it.expr, { x: it.x }), evR(it.a)) ? [] : [`check ${it.q}`],
  factor: it => { const [m, f] = it.a.split(': '), o = []; if (!sameAt(poly(it.cs), f)) o.push(`${it.q} is not ${f}`);
    const g = it.cs.filter(Boolean).reduce((x, y) => gcd(x, y), 0), want = Math.abs(g) > 1 || it.cs[0] === 0 ? 'GCF' : it.cs.length === 3 && it.cs[1] === 0 && it.cs[0] < 0 && isSq(it.cs[2]) && isSq(-it.cs[0]) ? 'difference of squares' : 'trinomial';
    if (m !== want) o.push(`${it.q}: method ${m}, should be ${want}`); return o; },
  quad: it => quadCheck(it.q, it.a),
  qform: it => { const [Dt, cnt, sols] = it.a.split('; '), D = evR(Dt.replace('D = ', '')), f = x => sideDiff(it.q, { x: [x, 0] })[0];
    const c0 = f(0), a = (f(1) + f(-1)) / 2 - c0, b = (f(1) - f(-1)) / 2, o = [];
    if (!close(D, b * b - 4 * a * c0)) o.push(`${it.q}: D ${D}`); if (cnt !== (D > 0 ? '2' : D === 0 ? '1' : '0')) o.push(`${it.q}: count ${cnt}`);
    return o.concat(quadCheck(it.q, sols)); },
  forms: it => { const [fz, vx, zeros, vert] = it.a.split('; '), rhs = s => s.replace(/^f\(x\) = /, ''), std = rhs(it.q), o = [];
    if (!sameAt(std, rhs(fz)) || !sameAt(std, rhs(vx))) o.push(`${it.q}: forms differ`);
    rootsOf(zeros).forEach(z => { if (!close(evR(std, { x: z[0] }), 0)) o.push(`${it.q}: zero ${z[0]}`); });
    const [hk, mm] = [vert.slice(0, vert.lastIndexOf(',')), vert.slice(vert.lastIndexOf(',') + 2)], [h, k] = parsePt(hk), f = x => evR(std, { x });
    if (!close(f(h), k) || !close(f(h - 1), f(h + 1))) o.push(`${it.q}: vertex ${vert}`);
    if ((f(h + 1) > k) !== (mm === 'minimum')) o.push(`${it.q}: max or min`); return o; },
  proj: it => { const h = t => -16 * t * t + it.v * t + it.s, [tm, hm, land] = numsIn(it.a), o = [];
    if (!(h(tm) >= h(tm - 0.01) && h(tm) >= h(tm + 0.01)) || !close(h(tm), hm)) o.push(`proj ${it.q}: top`);
    let lo = tm, hi = 100; for (let i = 0; i < 200; i++) { const mid = (lo + hi) / 2; if (h(mid) > 0) lo = mid; else hi = mid; }
    if (Math.abs(lo - land) > 0.005 + 1e-9) o.push(`proj ${it.q}: lands ${lo}, key ${land}`); return o; },
  compound: it => { const parts = it.q.split(' or '), o = [];
    for (let x = -30; x <= 30; x += 0.25) { const ins = parts.some(p => holdsS(p, { x })); if (ins !== inIv(it.a, x)) { o.push(`${it.q} vs ${it.a} at ${x}`); break; } } return o; },
  literal: it => { const q = it.q.replace(' (a > 0)', ''), o = [];
    for (const [a, b, c] of [[2, 3, 11], [0.5, -4, 1.5], [3, 7, -2]]) for (let x = -20; x <= 20; x += 0.25) if (holdsS(q, { a, b, c, x }) !== holdsS(it.a, { a, b, c, x })) { o.push(`${it.q} vs ${it.a}`); return o; }
    return o; },
  quadc: it => { const o = quadCheck(it.q, it.a, true); if (!rootsOf(it.a).every(v => Math.abs(v[1]) > 1e-9)) o.push(`${it.q}: roots should be complex`); return o; },
  qccheck: it => { const z = ev1(it.q.match(/^check (.*) in /)[1]), eq = it.q.replace(/^check .* in /, ''), o = [];
    if (!holdsS(eq, { x: z })) o.push(`${it.q}: not a root`); if (!holdsS(it.a, {})) o.push(`${it.q}: work line ${it.a} is false`); return o; },
  rem: it => { const rr = horner(it.cs, it.c), [val, yn] = it.a.split('; ');
    return val.startsWith(`${it.q[0]}(${num(it.c)}) = `) && close(evR(val.split(' = ')[1]), rr) && yn === (rr === 0 ? 'yes' : 'no') ? [] : [`${it.q}: ${it.a}, remainder ${rr}`]; },
  ratsimp: it => { const o = [], sv = it.a.split('; x ≠ ')[0]; if (!sameAt(it.q, sv)) o.push(`${it.q} is not ${sv}`);
    const zs = []; for (let x = -12; x <= 12; x++) if (Math.abs(evR(it.D, { x })) < 1e-9) zs.push(x);
    const ex = numsIn(it.a.split('x ≠ ')[1]); if (zs.join() !== ex.join()) o.push(`${it.q}: excluded ${ex}, should be ${zs}`); return o; },
  extr: it => { const p = it.d, o = [], [sol, ext] = it.a.split('; extraneous: ');
    const good = sol === 'no solution' ? [] : numsIn(sol), bad = ext === 'none' ? [] : numsIn(ext);
    const works = []; for (let x = -60; x <= 60; x++) if (holdsS(it.q, { x })) works.push(x);
    if (works.join() !== good.slice().sort((a, b) => a - b).join()) o.push(`${it.q}: works for ${works}, key ${sol}`);
    bad.forEach(x => { const ok = p.T === 'rad' || p.T === 'radk' ? (x + p.a === (x + p.b) ** 2 && x + p.b < 0) : p.T === 'ratA' ? x === p.a && x * x === p.q * x + p.rr : p.T === 'ratB' ? x === p.a : false;
      if (!ok || holdsS(it.q, { x })) o.push(`${it.q}: ${x} is not extraneous`); });
    if (['rad', 'radk', 'ratA', 'ratC'].includes(p.T) && new Set([...good, ...bad]).size !== 2) o.push(`${it.q}: the cleared quadratic needs 2 roots`);
    return o; },
  logrw: it => { const parts = s => { let m = s.match(/^(\d+)(\S+) = (.+)$/); if (m && !s.startsWith('log')) return { b: +m[1], e: evR(m[2].replace(/./g, c => SUPMAP[c] || c)), v: evR(m[3]) };
      m = s.match(/^(log\S*|ln) (.+) = (.+)$/); const b = m[1] === 'log' ? 10 : m[1] === 'ln' ? Math.E : +m[1].slice(3).replace(/./g, c => SUBD.indexOf(c)); return { b, e: evR(m[3]), v: evR(m[2]), log: true }; };
    const P = parts(it.q), A = parts(it.a);
    return P.b === A.b && close(P.e, A.e) && close(P.v, A.v) && close(P.b ** P.e, P.v) && !!A.log === (it.to === 'log') ? [] : [`${it.q} -> ${it.a}`]; },
  logmatch: it => { const env = { x: 1.9, y: 3.7, z: 0.6 }, L = 'ABCDEFGHIJKLMNOP', want = evR(it.q, env), hits = it.list.map((e, j) => close(evR(e, env), want) ? L[j] : null).filter(Boolean);
    return hits.length === 1 && hits[0] === it.a ? [] : [`${it.q}: matches ${hits}, key ${it.a}`]; },
  logsame: it => { const env = { x: 1.9, y: 3.7, z: 0.6 }, o = close(evR(it.q, env), evR(it.a, env)) ? [] : [`${it.q} is not ${it.a}`];
    if (it.expand && /(log\S*|ln)\(/.test(it.a)) o.push(`${it.a} not expanded`); if (!it.expand && (it.a.match(/log|ln/g) || []).length !== 1) o.push(`${it.a} not condensed`); return o; },
  expeq: it => { const [ex, dec] = it.a.split(' ≈ '), x = evR(ex.replace('x = ', ''));
    return holdsS(it.q, { x }) && dec === x.toFixed(3) ? [] : [`${it.q}: ${it.a}`]; },
  growth: it => { const d = it.d, v = numsIn(it.a.replace(/,/g, ''))[0]; let want, tol;
    if (d.t === 'comp') { want = d.P * Math.exp(d.k * d.yrs * Math.log1p(d.rate / 100 / d.k)); tol = 0.005; }
    else if (d.t === 'cont') { want = d.P * Math.exp(d.rate * d.yrs / 100); tol = 0.005; }
    else if (d.t === 'half') { want = d.A0 / Math.pow(2, d.tt / d.h); tol = 0.05; }
    else if (d.t === 'carbon') { want = Math.log2(100 / d.pc) * 5730; tol = 50; }
    else if (d.t === 'goal') { want = 100 * Math.log(d.G / d.P) / d.rate; tol = 0.05; }
    else { want = d.V * Math.exp(d.yrs * Math.log(1 - d.dr / 100)); tol = 0.005; }
    return Math.abs(v - want) <= tol + 1e-9 ? [] : [`${it.q}: ${it.a}, want ${want}`]; },
  combine: it => { const [ans, dom] = it.a.split('; '), o = [];
    const val = x => { const f = t => ev1(it.f, { x: t }), g = ev1(it.g, { x });
      if (it.op === '∘') return f(g); const F1 = ev1(it.f, { x }); return it.op === '+' ? C.add(F1, g) : it.op === '−' ? C.sub(F1, g) : C.mul(F1, g); };
    const isR = z => z && Math.abs(z[1]) < 1e-9;
    const real = x => { const g = safe(() => ev1(it.g, { x: [x, 0] })), f0 = safe(() => ev1(it.f, { x: [x, 0] })); if (!isR(g) || (it.op !== '∘' && !isR(f0))) return null; const v = safe(() => val([x, 0])); return isR(v) ? v : null; };
    for (let x = -12.3; x <= 12.3; x += 0.7) { const v = real(x); if (!v) continue; const w = safe(() => ev1(ans, { x })); if (!w || !closeC(v, w)) { o.push(`${it.q}: ${ans} at ${x}`); break; } }
    for (let x = -12.25; x <= 12.25; x += 0.5) { const inD = !!real(x), says = dom === 'all real numbers' ? true : dom.includes('≠') ? !close(x, evR(dom.split('≠ ')[1])) : holdsS(dom, { x });
      if (inD !== says) { o.push(`${it.q}: domain ${dom} wrong at ${x}`); break; } }
    return o; },
  inverse: it => { const inv = it.a.split('f⁻¹(x) = ')[1].replace(/, x ≥ .*$/, ''), o = [], dm = it.dom || {};
    for (let x = -9.5; x <= 9.5; x += 0.75) {
      if (dm.lo != null && (dm.open ? x <= dm.lo : x < dm.lo)) continue; if (dm.hi != null && x > dm.hi) continue;
      const y = safe(() => evR(it.f, { x })); if (y == null || !isFinite(y) || Math.abs(y) > 1e6) continue;
      const back = safe(() => evR(inv, { x: y })); if (back == null || !close(back, x, 1e-6)) { o.push(`${it.q}: f⁻¹(f(${x})) = ${back}`); break; } }
    if (it.restr && it.restr !== 'none needed') { const m = it.restr.match(/x ([≥≤]) (.+)/), c = evR(m[2]), s = m[1] === '≥' ? 1 : -1;
      if (!close(evR(it.f, { x: c + s }), evR(it.f, { x: c - s })) || !close(evR(it.f, { x: c + 2 * s }), evR(it.f, { x: c - 2 * s }))) o.push(`${it.q}: ${it.restr} is not at the turning point`); }
    if (it.restr === 'none needed') { const ys = []; for (let x = -9.5; x <= 9.5; x += 0.75) { const y = safe(() => evR(it.f, { x })); if (y != null && isFinite(y)) ys.push(y); } if (new Set(ys.map(y => y.toFixed(6))).size !== ys.length) o.push(`${it.q}: not one-to-one`); }
    return o; },
  seqclass: it => { const t = it.ts.map(x => evR(x)), d = t.slice(1).map((y, i) => y - t[i]), r0 = t.slice(1).map((y, i) => y / t[i]);
    const want = d.every(x => close(x, d[0])) ? `arithmetic, d = ${qT(Q(Math.round(d[0])))}` : r0.every(x => close(x, r0[0])) ? 'geometric' : 'neither';
    return it.a === want || (want === 'geometric' && it.a.startsWith('geometric, r = ') && close(evR(it.a.split('r = ')[1]), r0[0])) ? [] : [`${it.q}: ${it.a}, want ${want}`]; },
  seqform: it => { const [ex, rc] = it.a.split('; '), t = it.ts.map(x => evR(x)), o = [];
    t.forEach((v, i) => { if (!close(evR(ex.split(' = ')[1], { n: i + 1 }), v)) o.push(`${ex} misses term ${i + 1}`); });
    const m = rc.match(/^a₁ = (.+), aₙ = (.+)$/); let cur = evR(m[1]);
    t.forEach((v, i) => { if (i) cur = evR(m[2], { 'an-1': cur }); if (!close(cur, v)) o.push(`${rc} misses term ${i + 1}`); });
    return o; },
  arithword: it => { const d = it.d, o = []; let row = 0, tot = 0, seat = d.s, rowX = null; for (let i = 1; i <= 200; i++) { if (i <= d.N) tot += seat; if (i === d.k) row = seat; if (seat === d.X && rowX == null) rowX = i; seat += d.d; }
    const [a1, a2, a3] = it.a.split('; ').map(s => numsIn(s.replace(/,(?=\d{3})/g, '')).pop());
    if (a1 !== row || a2 !== tot || a3 !== rowX) o.push(`${it.q}: ${it.a}, want ${row}, ${tot}, ${rowX}`); return o; },
  seriesguide: it => { const d = it.d; let S = 0; for (let i = 0; i < d.gn; i++) S += d.ga * d.gr ** i; return S === d.S && it.a.includes(`S = ${S}`) && it.a.includes(`S − S = ${d.ga * d.gr ** d.gn - d.ga}`) ? [] : [`guided ${it.q}`]; },
  series: it => { const d = it.d, rr = d.r[0] / d.r[1], want = d.a * (1 - rr ** d.N) / (1 - rr); return close(evR(it.a), want) ? [] : [`${it.q}: ${it.a}, want ${want}`]; },
  seqmiss: it => { const d = it.d, o = [];
    if (d.T === 'a' || d.T === 'g') { const m = it.a.match(/^a₁ = (.+), [dr] = (.+); a\S+ = (.+)$/), a1 = evR(m[1]), k = evR(m[2]), at = j => d.T === 'a' ? a1 + (j - 1) * k : a1 * k ** (j - 1);
      if (!close(at(d.i), d.vi) || !close(at(d.j), d.vj) || !close(at(d.t), evR(m[3]))) o.push(`${it.q}: ${it.a}`);
      if (d.T === 'g' && (d.j - d.i) % 2 === 0) o.push(`${it.q}: even gap, ratio not unique`); }
    else { const fill = numsIn(it.a), t = d.shown.map(x => x == null ? fill.shift() : x), df = t.slice(1).map((y, i) => y - t[i]), rt = t.slice(1).map((y, i) => y / t[i]);
      if (d.T === 'ba' ? !df.every(x => x === df[0]) : !rt.every(x => close(x, rt[0]))) o.push(`${it.q}: ${it.a}`);
      if (d.T === 'bg') { const known = d.shown.map((x, i) => x == null ? null : i).filter(i => i != null); if (!known.some((i, j) => j && (i - known[j - 1]) % 2 === 1)) o.push(`${it.q}: ratio not unique`); } }
    return o; },
  compose: it => { const [fg, gf] = it.a.split('; ').map(s => s.split(' = ').slice(1).join(' = ')), o = [];
    for (const x of [0.37, 1.71, 3.19, 5.3]) { const g = safe(() => ev1(it.g, { x })), f = safe(() => ev1(it.f, { x }));
      const A = g && safe(() => ev1(it.f, { x: g })), B = f && safe(() => ev1(it.g, { x: f }));
      if (A && !closeC(A, ev1(fg, { x }))) o.push(`f(g(x)) for ${it.q}`); if (B && !closeC(B, ev1(gf, { x }))) o.push(`g(f(x)) for ${it.q}`); }
    return [...new Set(o)]; },
  decomp: it => { const m = it.a.match(/^f\(x\) = (.+), g\(x\) = (.+)$/), h = it.q.replace('h(x) = ', ''), o = [];
    if (m[2] === 'x') o.push('identity inner'); if (!XS.every(x => { const g = safe(() => ev1(m[2], { x })), hv = safe(() => ev1(h, { x })); return !g || !hv || closeC(ev1(m[1], { x: g }), hv); })) o.push(`${it.q}: ${it.a}`); return o; },
  rational: it => { const o = [], f = x => evR(it.N, { x }) / evR(it.D, { x });
    const zs = []; for (let x = -12; x <= 12; x++) if (Math.abs(evR(it.D, { x })) < 1e-9) zs.push(x);
    const holes = zs.filter(z => Math.abs(evR(it.N, { z, x: z })) < 1e-9), vas = zs.filter(z => !holes.includes(z));
    if (vas.join() !== it.va.join()) o.push(`${it.q}: VA ${it.va}, want ${vas}`);
    if (holes.length !== (it.hole ? 1 : 0) || (it.hole && (holes[0] !== it.hole[0] || !close((f(holes[0] + 1e-6) + f(holes[0] - 1e-6)) / 2, it.hole[1], 1e-4)))) o.push(`${it.q}: hole`);
    const big = 1e6; if (Math.abs(f(big) - (it.asym[0] * big + it.asym[1])) > 1e-3 || Math.abs(f(-big) - (-it.asym[0] * big + it.asym[1])) > 1e-3) o.push(`${it.q}: asymptote`);
    const sm = it.a.match(/VA: (.*); hole: (.*); (HA|slant): y = (.*); end/); if (!sm) o.push(`${it.q}: answer shape`);
    else { if ((sm[1] === 'none' ? [] : numsIn(sm[1])).join() !== it.va.join()) o.push(`${it.q}: VA text`);
      if (!close(evR(sm[4], { x: 2 }), 2 * it.asym[0] + it.asym[1])) o.push(`${it.q}: asymptote text`);
      if (sm[2] !== 'none') { const p = parsePt(sm[2]); if (!p || p[0] !== it.hole[0] || !close(p[1], it.hole[1])) o.push(`${it.q}: hole text`); } }
    return o; },
  matrix: it => { const [a, b] = it.m[0], [c, d] = it.m[1], det = a * d - b * c, o = [];
    if (evR(it.a.match(/det = ([^;]+)/)[1]) !== det) o.push(`${it.q}: det`);
    if (!det) { if (!it.a.includes('no inverse')) o.push(`${it.q}: singular`); return o; }
    const M = parseMat(it.a.split('A⁻¹ = ')[1]); const P = [[a * M[0][0] + b * M[1][0], a * M[0][1] + b * M[1][1]], [c * M[0][0] + d * M[1][0], c * M[0][1] + d * M[1][1]]];
    if (!(close(P[0][0], 1) && close(P[1][1], 1) && close(P[0][1], 0) && close(P[1][0], 0))) o.push(`${it.q}: inverse times A is not I`); return o; },
  msys: it => { const m = it.a.match(/x = (.+), y = (.+)/), env = { x: evR(m[1]), y: evR(m[2]) }; return it.eqs.every(e => holdsS(e, env)) ? [] : [`${it.q}: ${it.a}`]; },
  circle: it => { const m = it.a.match(/^center (\(.+\)); r = (.+)$/), [h, k] = parsePt(m[1]), R = evR(m[2]), G = (x, y) => sideDiff(it.q, { x, y })[0], o = [];
    if (![[h + R, k], [h - R, k], [h, k + R], [h, k - R]].every(([x, y]) => Math.abs(G(x, y)) < 1e-6)) o.push(`${it.q}: ${it.a} not on the circle`);
    if (Math.abs(G(h, k)) < 1e-6) o.push(`${it.q}: center on the curve`); if (!close(R * R, it.r2)) o.push(`${it.q}: radius`); return o; },
  circleq: it => { const { h, ck: k, rr } = it; return [[h + rr, k], [h, k - rr], [h - rr, k]].every(([x, y]) => holdsS(it.a, { x, y })) && !holdsS(it.a, { x: h, y: k }) ? [] : [`${it.q}: ${it.a}`]; },
  conic: it => { const [std, type] = it.a.split('; '), G = (x, y) => sideDiff(it.q, { x, y })[0], S = (x, y) => sideDiff(std, { x, y })[0], o = [];
    const pts = [[0.3, 1.7], [-2.2, 0.9], [3.1, -1.4], [1.1, 4.2], [-3.3, -2.6]], lam = pts.map(([x, y]) => G(x, y) / S(x, y));
    if (!lam.every(l => close(l, lam[0], 1e-6)) || !isFinite(lam[0])) o.push(`${it.q}: ${std} is a different curve`);
    const c0 = G(0, 0), A = (G(1, 0) + G(-1, 0)) / 2 - c0, Cc = (G(0, 1) + G(0, -1)) / 2 - c0;
    const want = !A || !Cc ? 'parabola' : A * Cc < 0 ? 'hyperbola' : close(A, Cc) ? 'circle' : 'ellipse';
    if (want !== type) o.push(`${it.q}: ${type}, want ${want}`); return o; },
  ellhyp: it => { const [cT0, vT, fT] = it.a.split('; '), cen = ptsIn(cT0)[0], vs = ptsIn(vT), fs = ptsIn(fT), o = [];
    const L = (x, y) => evR(it.q.split(' = ')[0], { x, y });
    if (vs.length !== 2 || fs.length !== 2) return [`${it.q}: answer shape`];
    vs.forEach(([x, y]) => { if (!close(L(x, y), 1)) o.push(`${it.q}: vertex (${x}, ${y}) not on the curve`); });
    const mid = P => [(P[0][0] + P[1][0]) / 2, (P[0][1] + P[1][1]) / 2];
    if (!closeC(mid(vs), cen) || !closeC(mid(fs), cen)) o.push(`${it.q}: center`);
    const a = Math.hypot(vs[0][0] - cen[0], vs[0][1] - cen[1]), u = [(vs[1][0] - cen[0]) / a, (vs[1][1] - cen[1]) / a], w = [-u[1], u[0]];
    const base = it.T === 'ellipse' ? cen : [cen[0] + 2 * a * u[0], cen[1] + 2 * a * u[1]], g = t => L(base[0] + t * w[0], base[1] + t * w[1]) - 1;
    let lo = 0, hi = 60; if (g(lo) * g(hi) > 0) return o.concat(`${it.q}: no curve point found`);
    for (let i = 0; i < 200; i++) { const m = (lo + hi) / 2; if (g(lo) * g(m) <= 0) hi = m; else lo = m; }
    const P = [base[0] + lo * w[0], base[1] + lo * w[1]], d1 = Math.hypot(P[0] - fs[0][0], P[1] - fs[0][1]), d2 = Math.hypot(P[0] - fs[1][0], P[1] - fs[1][1]);
    if (!close(it.T === 'ellipse' ? d1 + d2 : Math.abs(d1 - d2), 2 * a, 1e-6)) o.push(`${it.q}: foci ${fT}`); return o; },
};
const TIDY = new Set(['same', 'quad', 'quadc', 'ratsimp', 'combine', 'inverse', 'compose', 'decomp', 'line', 'fn', 'expeq', 'logsame', 'seqform', 'conic', 'ellhyp', 'circle', 'circleq', 'rational', 'matrix', 'series', 'forms', 'qform']);

Gen.add('algebra', {
  title: 'Algebra and Functions',
  fields: [
    { id: 'course', label: 'Course', type: 'select', options: COURSES, def: 'alg1' },
    { id: 'skill', label: 'Skill', type: 'select', def: 'line',
      options: v => Object.entries(SK).filter(([, s]) => s[1].split(' ').includes(v.course)).map(([id, s]) => [id, s[0]]) },
    { id: 'count', label: 'Problems', type: 'select', def: 'm',
      options: v => { const c = (SK[v.skill] || SK.line)[3]; return [['s', `Fewer (${nText(c[0])})`], ['m', `Standard (${nText(c[1])})`], ['l', `More (${nText(c[2])})`]]; } },
    { id: 'story', label: 'Story problems', type: 'select', def: 'mix', show: v => v.skill === 'sysword',
      options: [['mix', 'A mix'], ['tickets', 'Ticket sales'], ['mixture', 'Mixtures'], ['plans', 'Price plans (gyms, phones)'], ['travel', 'Travel with a current or wind']] },
  ],
  make(v, r) {
    UID = 0;
    const s = SK[v.skill] || SK.line, n = nOf(v);
    const out = s[2](r, n, v.skill === 'sysword' ? v.story : v.course);
    const parts = [part('', out.ex), ...out.parts];
    return {
      title: s[0], level: COURSES.find(c => c[0] === v.course)[1], minutes: s[4], materials: s[5] || 'pencil',
      ican: out.ican, directions: out.directions, parts, items: out.items, mistakes: out.mistakes, notes: out.notes || '', teacher: out.teacher || '',
    };
  },
  verify(sheet) {
    const out = [];
    for (const it of sheet.items) {
      const f = VER[it.k];
      if (!f) { out.push(`no check for kind ${it.k}`); continue; }
      let bad;
      try { bad = f(it); } catch (e) { bad = [`${it.k} ${it.q}: ${e.message}`]; }
      out.push(...bad);
      if (TIDY.has(it.k)) tidy(it.a).forEach(t => out.push(`${it.a}: ${t}`));
    }
    return out;
  },
  css: `.al-grid{display:grid;gap:4px 26px;margin:6px 0 10px}
.al-c2{grid-template-columns:1fr 1fr}.al-c3{grid-template-columns:1fr 1fr 1fr}
.al-cell{break-inside:avoid;display:flex;flex-direction:column;border-top:1px solid #ddd;padding-top:6px}
.al-cell > p{margin:0 0 2px;font-size:16px}
.al-work{flex:1}
.al-ans{margin:2px 0 4px;font-size:15px}
.al-ans p{margin:2px 0}
.al-cell .gen-svg,.al-graph .gen-svg{display:block;max-width:100%;height:auto;margin:4px 0}
.al-graph p{margin:2px 0}
.al-sys{display:inline-flex;flex-direction:column;border-left:2px solid #222;padding:1px 0 1px 8px;margin:2px 4px;vertical-align:middle;line-height:1.35;border-radius:8px 0 0 8px}
.al-sysblank{display:inline-block;min-width:12em;min-height:2.6em;vertical-align:middle}
.al-ht{border-collapse:collapse;margin:4px 0 6px;font-size:15px}
.al-ht th,.al-ht td{border:1px solid #888;padding:2px 9px;text-align:center;min-width:2.2em}
.al-ht th{background:#f1f1f1}
.al-mat{width:100%}.al-mat td{height:.45in}
.al-box{border-collapse:collapse;margin:4px 0;font-size:15px}
.al-box th{padding:2px 8px;font-weight:600}
.al-box td{border:1.5px solid #444;width:.95in;height:.42in;text-align:center}
.al-cards{display:grid;grid-template-columns:1fr 1fr 1fr;margin:6px 0 10px}
.al-card{border:1.5px dashed #555;padding:6px 10px;margin:0 -1.5px -1.5px 0;break-inside:avoid}
.al-card p{margin:2px 0}
.al-side{display:grid;grid-template-columns:auto 1fr;gap:16px;align-items:start;break-inside:avoid;border-top:1px solid #ddd;padding-top:6px;margin-bottom:6px}
.al-side .gen-svg{max-width:2.6in}
.al-story{break-inside:avoid;border-top:1px solid #ddd;padding-top:6px;margin-bottom:6px}
.al-story p{margin:3px 0}
.al-two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.al-row{margin:4px 0}
.al-steps{margin:4px 0;padding-left:1.8em;font-size:15px}
.al-steps li{margin-bottom:8px}
.al-match{display:grid;grid-template-columns:1fr 1.3fr;gap:24px}
.al-opts{list-style:none;margin:6px 0;padding:0}.al-opts li{margin:0 0 10px}
.al-sub{margin:4px 0;padding-left:1.8em}.al-sub li{margin-bottom:4px}
.al-mx{display:inline-flex;flex-direction:column;border-left:1.6px solid #222;border-right:1.6px solid #222;border-radius:3px;padding:0 4px;vertical-align:middle;line-height:1.3}
.al-mx > span{display:flex;gap:10px;justify-content:space-around}.al-mx > span > span{min-width:1.3em;text-align:center}
.al-mxk{color:inherit}
.al-sig{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;font-size:1.25em}.al-sig small{font-size:.5em}`,
});
})();
