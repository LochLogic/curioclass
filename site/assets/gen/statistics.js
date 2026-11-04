// Statistics and Probability generator, grades K-12. Graph-reading.js reads finished graphs; this one builds the data
// skills around them. Every skill draws its own data, and verify() re-works every answer by a second route.
// K-5: plan and run a class survey (a question, answer choices, a tally chart, who to ask, a bar graph grid to fill,
//   summary sentence frames in English, Spanish or French; ACTFL Interpersonal and Presentational modes), organize raw
//   survey answers into a tally and frequency table and a bar graph (1.MD.4, 2.MD.10, 3.MD.3), find the odd one out
//   (outliers), mean and median with and without an outlier, line plots in eighths with an equal share (5.MD.2), a
//   two-way table from survey answers, and a right-and-wrong box for a junk mail sorter (CSTA 1B-DA-06, 1B-DA-07).
// 6-8: mean, median, mode and range; mean absolute deviation with a deviation table; five-number summaries and box
//   plots on one shared scale; dot plots and histograms; mean or median? (6.SP.2-5); comparing two groups with means
//   and MAD (7.SP.3-4); probability with marble bags, compound events and a spinner lab (7.SP.5-8); scatter plots,
//   lines of fit, what slope and intercept mean, two-way tables (8.SP.1-4); classifier accuracy, confusion matrices
//   and accuracy by group (CSTA 2-DA-08, 2-DA-09, 2-IC-20).
// 9-12: comparing distributions with box plots and outliers, joint, marginal and conditional relative frequency,
//   residuals (S-ID.1-3, 5, 6); Venn diagrams and the addition rule, conditional probability and independence, hidden
//   two-way tables (S-CP.1-7); z-scores and the 68-95-99.7 rule (S-ID.4); the Statistics course: 1.5 x IQR fences,
//   least squares by hand, segmented bar graphs, expected value, combining random variables, tree diagrams for
//   screening tests, sampling distributions of a proportion, confidence intervals, chi-square tests (S-IC.1-6,
//   S-MD.1-7); precision, recall and false positive rates by group (CSTA 3A-DA-12, 3A-IC-24).
// Key drawings (bars, dots, box plots, plotted points, lines of fit) are red and class ws-ans, hidden on the student copy.
(() => {
const { part, example, fill, blank, keyline, lines, table, esc, work } = Gen.h;
const { fmt, gcd } = Gen.m;

/* ---------- settings ---------- */
const GRADES = [['k', 'Kindergarten'], ['1', 'Grade 1'], ['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'],
  ['6', 'Grade 6'], ['7', 'Grade 7'], ['8', 'Grade 8'], ['9', 'Grade 9 (Algebra 1)'], ['10', 'Grade 10 (Geometry)'],
  ['11', 'Grade 11 (Algebra 2)'], ['12', 'Grade 12 (Statistics course)']];
const SURVEY = ['survey', 'Plan and run a class survey'];
const SKILLS = {
  k: [SURVEY],
  1: [['tally', 'Organize survey answers: tally chart and bar graph'], SURVEY],
  2: [['tally', 'Organize survey answers: tally chart and bar graph'], SURVEY],
  3: [['tally', 'Organize survey answers: frequency table and bar graph'], ['odd', 'Find the odd one out (outliers)'], SURVEY],
  4: [['tally', 'Organize survey answers: frequency table and bar graph'], SURVEY],
  5: [['center', 'Mean and median, with and without the outlier'], ['lineplot', 'Line plots of eighths and fair shares'],
    ['twoway', 'Two-way table from survey answers'], ['tally', 'Organize survey answers: frequency table and bar graph'],
    ['confusion', 'Right and wrong box for a sorting program'], SURVEY],
  6: [['center', 'Mean, median, mode and range'], ['mad', 'Mean absolute deviation (MAD)'], ['box', 'Five-number summary and box plots'],
    ['dothist', 'Dot plot and histogram'], ['choose', 'Mean or median?'], ['confusion', 'Accuracy of a computer model'], SURVEY],
  7: [['bags', 'Probability: pick the better bag'], ['compound', 'Compound events and sample spaces'], ['spinner', 'Spinner experiment'],
    ['compare', 'Compare two groups: means and MAD'], ['confusion', 'Confusion matrix'], SURVEY],
  8: [['scatter', 'Scatter plots and association'], ['fit', 'Line of fit and predictions'], ['slope', 'What the slope and intercept mean'],
    ['twoway', 'Two-way tables and relative frequency'], ['confusion', 'Accuracy by group'], SURVEY],
  9: [['compare', 'Compare two distributions with box plots'], ['twoway', 'Joint, marginal and conditional relative frequency'],
    ['residuals', 'Residuals and residual plots'], SURVEY],
  10: [['venn', 'Venn diagrams and the addition rule'], ['twoway', 'Conditional probability and independence'],
    ['hidden', 'Hidden two-way table puzzle'], ['confusion', 'Precision and recall'], SURVEY],
  11: [['normal', 'Normal curve: the 68-95-99.7 rule'], ['zscore', 'Z-scores across scales'], SURVEY],
  12: [['zscore', 'Z-scores across scales'], ['fences', 'Five-number summary and 1.5 × IQR outliers'], ['normal', 'Normal curve: the 68-95-99.7 rule'],
    ['lsr', 'Least squares regression by hand'], ['residuals', 'Residuals and residual plots'], ['segbar', 'Segmented bar graphs'],
    ['ev', 'Expected value: is the game fair?'], ['combine', 'Combining random variables'], ['tree', 'Tree diagrams: screening tests'],
    ['sampprop', 'Sampling distribution of a proportion'], ['ci', 'Confidence intervals'], ['chisq', 'Chi-square test of independence'],
    ['gof', 'Chi-square goodness of fit (candy colors)'], ['confusion', 'False positive rates across groups'], SURVEY],
};
// how many sets or items each length makes: [short, standard, long] and the noun; two entries = only short and standard
function CN(skill, g) {
  const G = g === 'k' ? 0 : +g;
  const t = {
    tally: [[3, 4, 5], 'questions'], odd: [[4, 5, 6], 'data sets'], center: G === 5 ? [[2, 3, 4], 'data sets'] : [[4, 6, 8], 'data sets'],
    lineplot: [[1, 2], 'line plots'], twoway: G === 5 ? [[30, 40], 'answers'] : G === 8 ? [[1, 2, 3], 'tables'] : [[1, 2], 'tables'],
    confusion: G === 5 ? [[12, 16, 20], 'messages'] : G === 6 ? [[16, 20, 24], 'predictions'] : G === 7 ? [[20, 30, 40], 'predictions'] : G === 8 ? [[1, 2, 3], 'tables'] : [[1, 2], 'rounds'],
    mad: [[3, 4, 5], 'data sets'], box: [[2, 3, 4], 'data sets'], dothist: [[16, 20, 24], 'values'], choose: [[4, 5, 6], 'data sets'],
    bags: [[4, 6, 8], 'pairs'], compound: [[4, 5, 6], 'events'], spinner: [[20, 40, 50], 'spins'], compare: G === 7 ? [[1, 2, 3], 'pairs'] : [[1, 2], 'pairs'],
    scatter: [[1, 2], 'data sets'], fit: [[2, 3], 'scatter plots'], slope: [[4, 5, 6], 'models'], residuals: [[1, 2], 'data sets'],
    venn: [[3, 4, 6], 'diagrams'], hidden: [[1, 2], 'puzzles'], normal: [[1, 2, 3], 'curves'], zscore: [[4, 6, 8], 'comparisons'],
    fences: [[3, 4, 5], 'data sets'], lsr: [[1, 2], 'data sets'], segbar: [[1, 2], 'tables'], ev: [[3, 4, 5], 'games'],
    combine: [[4, 6, 8], 'problems'], tree: [[2, 3], 'problems'], sampprop: [[4, 6, 8], 'problems'], ci: [[4, 6], 'intervals'],
    chisq: [[1, 2], 'tables'], gof: [[1, 1], 'bags'],
  }[skill];
  return t || [[1, 1], 'sets'];
}
const skillOf = v => (SKILLS[v.grade] || SKILLS[6]).some(s => s[0] === v.skill) ? v.skill : (SKILLS[v.grade] || SKILLS[6])[0][0];
const countOpts = v => {
  const sk = skillOf(v), [n, noun] = CN(sk, v.grade);
  if (sk === 'gof') return [['s', 'One worked bag'], ['m', 'One worked bag and a table for your own bag']];
  const o = [['s', `Fewer (${n[0]} ${noun})`], ['m', `Standard (${n[1]} ${noun})`]];
  if (n[2]) o.push(['l', `More (${n[2]} ${noun})`]);
  return o;
};
const LANGS = [['en', 'English'], ['es', 'Spanish (español)'], ['fr', 'French (français)']];

/* ---------- small math ---------- */
const sum = a => a.reduce((s, x) => s + x, 0);
const mean = a => sum(a) / a.length;
const srt = a => a.slice().sort((x, y) => x - y);
const median = a => { const s = srt(a), n = s.length; return n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2; };
// quartiles: the median of each half, leaving the middle value out of both halves when the count is odd
const five = a => { const s = srt(a), n = s.length, h = Math.floor(n / 2); return [s[0], median(s.slice(0, h)), median(s), median(s.slice(n - h)), s[n - 1]]; };
const fencesOf = a => { const f = five(a), q = f[3] - f[1]; return [f[1] - 1.5 * q, f[3] + 1.5 * q]; };
const outsOf = a => { const [lo, hi] = fencesOf(a); return srt(a.filter(x => x < lo || x > hi)); };
const madOf = a => { const m = mean(a); return mean(a.map(x => Math.abs(x - m))); };
const modesOf = a => { const c = new Map(); a.forEach(x => c.set(x, (c.get(x) || 0) + 1)); const top = Math.max(...c.values()); return [...c].filter(e => e[1] === top).map(e => e[0]); };
const fr = (n, d) => { const g = gcd(n, d) || 1; n /= g; d /= g; if (d < 0) { n = -n; d = -d; } return d === 1 ? String(n) : `${n}/${d}`; };
const mixedTxt = (n, d) => { const w = Math.floor(n / d), rem = n - w * d; return rem ? (w ? `${w} ${fr(rem, d)}` : fr(rem, d)) : String(w); };
const pc = (x, dp = 0) => fmt(100 * x, dp) + '%';
const money = x => (x < -0.004 ? '−' : '') + '$' + Math.abs(x).toFixed(2);
const N = (x, dp = 2) => fmt(x, dp);
const list = a => a.map(x => fmt(x, 2)).join(', ');
const LET = 'ABCDEFGH';
const NAMES = ['Maya', 'Leo', 'Ava', 'Sam', 'Kai', 'Zoe', 'Nora', 'Eli', 'Ruby', 'Omar', 'Lily', 'Ben', 'Rosa', 'Jin'];
const sd = (vals, ps) => { const m = sum(vals.map((x, i) => x * ps[i])); return Math.sqrt(sum(vals.map((x, i) => ps[i] * (x - m) ** 2))); };
const lsrOf = pts => { const mx = mean(pts.map(p => p[0])), my = mean(pts.map(p => p[1]));
  const sxy = sum(pts.map(p => (p[0] - mx) * (p[1] - my))), sxx = sum(pts.map(p => (p[0] - mx) ** 2)), syy = sum(pts.map(p => (p[1] - my) ** 2));
  const b = sxy / sxx; return { b, a: my - b * mx, r: sxy / Math.sqrt(sxx * syy), mx, my, sxy, sxx, syy }; };

// n values from lo to hi with a whole-number mean
function withMean(r, n, lo, hi) {
  for (let t = 0; t < 400; t++) {
    const a = Array.from({ length: n - 1 }, () => r.int(lo, hi));
    const m = Math.round(sum(a) / (n - 1)) + r.int(-1, 1), last = m * n - sum(a);
    if (last >= lo && last <= hi) return r.shuffle(a.concat(last));
  }
  return null;
}
// k positive counts that add to total, all different
function split(r, total, k) {
  for (let t = 0; t < 3000; t++) {
    const a = []; let left = total;
    for (let i = 0; i < k - 1; i++) { const x = r.int(1, Math.max(1, Math.floor(2 * left / (k - i)) - 1)); a.push(x); left -= x; }
    if (left < 1 || new Set(a.concat(left)).size < k) continue;
    return r.shuffle(a.concat(left));
  }
  const a = Array.from({ length: k }, (_, i) => i + 1); a[k - 1] += total - sum(a); return a;
}

/* ---------- drawing ---------- */
const FONT = 'font-family="Helvetica, Arial, sans-serif"';
const RED = '#b03020';
const r1 = x => Math.round(x * 10) / 10;
const T = (x, y, s, o = {}) => `<text x="${r1(x)}" y="${r1(y)}" ${FONT} font-size="${o.fs || 11}" text-anchor="${o.a || 'middle'}" fill="${o.c || '#222'}"${o.b ? ' font-weight="700"' : ''}${o.rot ? ` transform="rotate(${o.rot} ${r1(x)} ${r1(y)})"` : ''}>${s}</text>`;
const Ln = (x1, y1, x2, y2, c = '#222', w = 1, ex = '') => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}" stroke="${c}" stroke-width="${w}"${ex}/>`;
const KG = s => `<g class="ws-ans">${s}</g>`;
const SVG = (w, h, body, label) => Gen.h.svg(w, h, body, label);
const short = (s, n = 16) => { s = String(s); return s.length > n ? s.slice(0, n - 1) + '.' : s; };

// a scale for lo..hi with at most max ticks
function scaleFor(lo, hi, max = 20) {
  for (const st of [1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000, 5000]) {
    const a = Math.floor(lo / st) * st, b = Math.ceil(hi / st) * st;
    if ((b - a) / st <= max && b > a) return { lo: a, hi: b, tick: st, lab: (b - a) / st > 12 ? 2 * st : st };
  }
  return { lo, hi, tick: (hi - lo) / 10, lab: (hi - lo) / 5 };
}
// a horizontal number line from x0 to x1; ticks every tick, numbers every lab; fl = label text for a value
function nline(x0, x1, y, lo, hi, tick, lab, fl = v => fmt(v, 3)) {
  const X = v => x0 + (v - lo) * (x1 - x0) / (hi - lo);
  let b = Ln(x0 - 8, y, x1 + 8, y, '#222', 1.5);
  const n = Math.round((hi - lo) / tick);
  for (let i = 0; i <= n; i++) {
    const v = +(lo + i * tick).toFixed(6), q = (v - lo) / lab, major = Math.abs(q - Math.round(q)) < 1e-6;
    b += Ln(X(v), y - (major ? 5 : 3), X(v), y + (major ? 5 : 3));
    if (major) b += T(X(v), y + 17, fl(v));
  }
  return { X, b };
}
// a dot plot: one dot per value, stacked; keyed = red and only on the key
function dotPlot(vals, sc, keyed, label, room) {
  const W = 640, x0 = 30, x1 = 610, cnt = new Map();
  vals.forEach(x => cnt.set(x, (cnt.get(x) || 0) + 1));
  const top = Math.max(room || 0, ...cnt.values()), H = 44 + top * 11, y = H - 26;
  const { X, b } = nline(x0, x1, y, sc.lo, sc.hi, sc.tick, sc.lab);
  let d = '';
  for (const [x, c] of cnt) for (let i = 0; i < c; i++) d += `<circle cx="${r1(X(x))}" cy="${r1(y - 10 - i * 11)}" r="4.5" fill="${keyed ? RED : '#222'}"/>`;
  return SVG(W, H, b + (keyed ? KG(d) : d), label);
}
// box plots on one shared scale: rows = [{name, data, keyed, mod}] (mod = whiskers stop at the fences, outliers as rings)
function boxPlots(rows, sc, label) {
  const W = 640, x0 = 96, x1 = 610, rh = 50, H = rows.length * rh + 42, y = H - 26;
  const { X, b } = nline(x0, x1, y, sc.lo, sc.hi, sc.tick, sc.lab);
  let body = b;
  rows.forEach((rw, i) => {
    const cy = 10 + i * rh + rh / 2, c = rw.keyed ? RED : '#222';
    body += T(4, cy + 4, esc(short(rw.name, 17)), { a: 'start', b: true, fs: 11 });
    body += Ln(x0, cy, x1, cy, '#ccc', 0.6, ' stroke-dasharray="2 5"');
    const [mn, q1, md, q3, mx] = five(rw.data), os = rw.mod ? outsOf(rw.data) : [];
    const inside = rw.data.filter(x => !os.includes(x)), lo = rw.mod ? Math.min(...inside) : mn, hi = rw.mod ? Math.max(...inside) : mx;
    let s = Ln(X(lo), cy, X(q1), cy, c, 2) + Ln(X(q3), cy, X(hi), cy, c, 2) + Ln(X(lo), cy - 8, X(lo), cy + 8, c, 2) + Ln(X(hi), cy - 8, X(hi), cy + 8, c, 2)
      + `<rect x="${r1(X(q1))}" y="${r1(cy - 14)}" width="${r1(Math.max(1, X(q3) - X(q1)))}" height="28" fill="none" stroke="${c}" stroke-width="2"/>` + Ln(X(md), cy - 14, X(md), cy + 14, c, 2.5);
    for (const o of os) s += `<circle cx="${r1(X(o))}" cy="${r1(cy)}" r="4" fill="none" stroke="${c}" stroke-width="1.6"/>`;
    body += rw.keyed ? KG(s) : s;
  });
  return SVG(W, H, body, label);
}
// a bar graph grid: cats along the bottom, 0..maxY up the side; vals (optional) drawn as red key bars
function barGrid(o) {
  const n = o.cats.length, x0 = 54, cw = Math.min(110, Math.max(54, Math.floor(560 / n))), W = x0 + cw * n + 16;
  const top = 16, ph = o.tall || (o.maxY > 20 ? 260 : 210), y0 = top + ph, H = y0 + (o.blankCats ? 40 : 34);
  const per = ph / o.maxY, lab = o.lab || (o.maxY > 20 ? 5 : o.maxY > 10 ? 2 : 1), gs = o.grid || 1;
  let b = '';
  for (let v = 0; v <= o.maxY + 1e-9; v += gs) {
    const yy = y0 - v * per, major = Math.abs(v / lab - Math.round(v / lab)) < 1e-9;
    b += Ln(x0, yy, x0 + cw * n, yy, major ? '#999' : '#ccc', major ? 0.9 : 0.6);
    if (major) b += T(x0 - 6, yy + 4, o.pct ? v + '%' : fmt(v), { a: 'end', fs: 10.5 });
  }
  if (o.cells) for (let i = 0; i <= n; i++) b += Ln(x0 + i * cw, top, x0 + i * cw, y0, '#bbb', 0.7);
  b += Ln(x0, top - 4, x0, y0, '#222', 1.5) + Ln(x0, y0, x0 + cw * n, y0, '#222', 1.5);
  o.cats.forEach((c, i) => {
    const xm = x0 + i * cw + cw / 2;
    if (o.blankCats && !c) b += Ln(xm - cw * 0.38, y0 + 24, xm + cw * 0.38, y0 + 24, '#555', 0.8);
    else b += T(xm, y0 + 16, esc(short(c, Math.floor(cw / 6.2))), { fs: 10.5 });
  });
  if (o.yl) b += T(14, top + ph / 2, esc(o.yl), { rot: -90, fs: 11 });
  if (o.vals) {
    const g = o.gap == null ? cw * 0.18 : o.gap;
    b += KG(o.vals.map((v, i) => `<rect x="${r1(x0 + i * cw + g)}" y="${r1(y0 - v * per)}" width="${r1(cw - 2 * g)}" height="${r1(v * per)}" fill="${RED}" fill-opacity="0.22" stroke="${RED}" stroke-width="1.6"/>`
      + (o.showVals ? T(x0 + i * cw + cw / 2, y0 - v * per - 4, fmt(v), { c: RED, fs: 10, b: true }) : '')).join(''));
  }
  return SVG(W, H, b, o.label || 'Bar graph grid');
}
// a scatter grid: xs/ys = {lo, hi, st}; pts drawn black, keyPts red (key only), keyLine [x1, y1, x2, y2] red
function scatter(o) {
  const W = 480, H = 340, x0 = 62, x1 = 462, y0 = 296, y1 = 12;
  const X = x => x0 + (x - o.xs.lo) * (x1 - x0) / (o.xs.hi - o.xs.lo), Y = y => y0 - (y - o.ys.lo) * (y0 - y1) / (o.ys.hi - o.ys.lo);
  let b = '';
  const nx = Math.round((o.xs.hi - o.xs.lo) / o.xs.st), ny = Math.round((o.ys.hi - o.ys.lo) / o.ys.st);
  for (let i = 0; i <= nx; i++) { const v = o.xs.lo + i * o.xs.st; b += Ln(X(v), y0, X(v), y1, '#ccc', 0.7) + T(X(v), y0 + 15, fmt(v, 2), { fs: 10 }); }
  for (let i = 0; i <= ny; i++) { const v = o.ys.lo + i * o.ys.st; b += Ln(x0, Y(v), x1, Y(v), Math.abs(v) < 1e-9 && o.zero ? '#222' : '#ccc', Math.abs(v) < 1e-9 && o.zero ? 1.5 : 0.7) + T(x0 - 6, Y(v) + 3.5, fmt(v, 2), { a: 'end', fs: 10 }); }
  b += Ln(x0, y0, x1, y0, '#222', 1.5) + Ln(x0, y0, x0, y1, '#222', 1.5);
  b += T((x0 + x1) / 2, H - 8, esc(o.xl), { fs: 11.5, b: true }) + T(14, (y0 + y1) / 2, esc(o.yl), { rot: -90, fs: 11.5, b: true });
  for (const p of o.pts || []) b += `<circle cx="${r1(X(p[0]))}" cy="${r1(Y(p[1]))}" r="4" fill="#222"/>`;
  let k = '';
  for (const p of o.keyPts || []) k += `<circle cx="${r1(X(p[0]))}" cy="${r1(Y(p[1]))}" r="4.2" fill="${RED}"/>`;
  if (o.keyLine) { const [a, c, d, e] = o.keyLine; k += Ln(X(a), Y(c), X(d), Y(e), RED, 2.2); }
  if (k) b += KG(k);
  return SVG(W, H, b, o.label || 'Scatter plot grid');
}
// tally marks for n, drawn small: groups of five with a slash
function tallySvg(n) {
  let b = '', x = 4;
  for (let g = 0; g < Math.ceil(n / 5); g++) {
    const k = Math.min(5, n - g * 5);
    for (let i = 0; i < Math.min(4, k); i++) b += Ln(x + i * 6, 3, x + i * 6, 21, '#222', 1.8);
    if (k === 5) b += Ln(x - 3, 18, x + 21, 6, '#222', 1.8);
    x += 34;
  }
  const w = Math.max(30, x);
  return `<svg class="st-tal" viewBox="0 0 ${w} 24" width="${w}" height="24" role="img" aria-label="${n} tally marks">${b}</svg>`;
}
// a spinner with equal sections, each labeled
function spinnerSvg(labels) {
  const n = labels.length, R = 100, cx = 112, cy = 112;
  let b = `<circle cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="#222" stroke-width="2"/>`;
  labels.forEach((l, i) => {
    const a = -Math.PI / 2 + i * 2 * Math.PI / n, m = a + Math.PI / n;
    b += Ln(cx, cy, cx + R * Math.cos(a), cy + R * Math.sin(a), '#222', 1.5);
    b += T(cx + 64 * Math.cos(m), cy + 64 * Math.sin(m) + 4, esc(l), { fs: n > 8 ? 10 : 11.5, b: true });
  });
  b += `<circle cx="${cx}" cy="${cy}" r="4" fill="#222"/>`;
  return SVG(224, 224, b, `Spinner with ${n} equal sections: ${labels.join(', ')}`);
}
// a Venn diagram with counts in each region
function vennSvg(o) {
  let b = `<rect x="3" y="3" width="294" height="174" rx="6" fill="none" stroke="#222" stroke-width="1.5"/>`
    + `<circle cx="118" cy="98" r="64" fill="none" stroke="#222" stroke-width="2"/><circle cx="182" cy="98" r="64" fill="none" stroke="#222" stroke-width="2"/>`
    + T(84, 26, esc(o.la), { b: true, fs: 11.5 }) + T(216, 26, esc(o.lb), { b: true, fs: 11.5 })
    + T(90, 103, o.a, { fs: 15, b: true }) + T(150, 103, o.ab, { fs: 15, b: true }) + T(210, 103, o.b, { fs: 15, b: true }) + T(268, 166, o.n, { fs: 15, b: true });
  return SVG(300, 180, b, `Venn diagram: ${o.a} only ${o.la}, ${o.ab} both, ${o.b} only ${o.lb}, ${o.n} neither`);
}

/* ---------- data banks ---------- */
const TSETS = [
  { t: 'Favorite Fruit', q: 'What is your favorite fruit?', cats: ['Apple', 'Banana', 'Grapes', 'Orange', 'Pear'] },
  { t: 'Favorite Pet', q: 'Which pet do you like best?', cats: ['Dog', 'Cat', 'Fish', 'Bird', 'Rabbit'] },
  { t: 'Favorite Color', q: 'What is your favorite color?', cats: ['Red', 'Blue', 'Green', 'Yellow', 'Purple'] },
  { t: 'Recess Games', q: 'What do you like to play at recess?', cats: ['Tag', 'Swings', 'Slide', 'Soccer', 'Jump rope'] },
  { t: 'Favorite Lunch', q: 'What is your favorite lunch?', cats: ['Pizza', 'Tacos', 'Pasta', 'Soup', 'Salad'] },
  { t: 'Favorite Season', q: 'Which season do you like best?', cats: ['Spring', 'Summer', 'Fall', 'Winter'] },
];
// dir = which way the odd value usually falls, why = a likely reason
const NUM = [
  { what: 'Minutes to get to school', unit: 'minutes', lo: 5, hi: 35, dir: 1, why: 'a missed bus or a long detour' },
  { what: 'Standing long jumps', unit: 'inches', lo: 40, hi: 64, dir: -1, why: 'a slip at takeoff, or a jump measured from the wrong line' },
  { what: 'Bean plant heights', unit: 'cm', lo: 10, hi: 26, dir: -1, why: 'a plant that sat in the shade or did not get water' },
  { what: 'Push-ups in one minute', unit: 'push-ups', lo: 8, hi: 30, dir: -1, why: 'a sore arm, or a count that was written down wrong' },
  { what: 'Quiz scores', unit: 'points', lo: 62, hi: 96, dir: -1, why: 'a student who was sick or missed the lesson' },
  { what: 'Pages read in one night', unit: 'pages', lo: 8, hi: 30, dir: 1, why: 'a reader who finished a whole short book' },
  { what: 'Daily high temperatures', unit: '°F', lo: 58, hi: 80, dir: 1, why: 'a heat wave, or a thermometer left in the sun' },
  { what: 'Books read this summer', unit: 'books', lo: 2, hi: 14, dir: 1, why: 'a reader who read a whole series' },
];
const PEOPLE = c => c.unit === '°F' ? 'days' : c.unit === 'cm' ? 'plants' : 'students';

/* ---------- shared bits ---------- */
const line = (w = 11) => `<span class="st-line" style="width:${w}em"></span>`;
const frame = s => esc(s).replace(/____/g, line(8));
const vals = a => `<div class="st-vals">${a.map(x => `<span class="st-v">${esc(fmt(x, 2))}</span>`).join('')}</div>`;
const ctab = (head, rows, cls = '') => table(head, rows).replace('class="ws-table"', `class="ws-table st-tbl${cls ? ' ' + cls : ''}"`);

// counting questions about a set of category counts
function countQs(r, cats, counts, kinds, who, tag) {
  const items = [], total = sum(counts), byDesc = cats.map((c, i) => i).sort((a, b) => counts[b] - counts[a]);
  const used = new Set();
  for (const kind of kinds) {
    let it = null;
    for (let t = 0; t < 30 && !it; t++) {
      const i = r.int(0, cats.length - 1), j = r.int(0, cats.length - 1);
      if (kind === 'read') it = { q: `How many ${who} chose ${cats[i].toLowerCase()}?`, a: String(counts[i]), i };
      else if (kind === 'most') it = { q: 'Which answer got the most votes?', a: cats[byDesc[0]] };
      else if (kind === 'least') it = { q: 'Which answer got the fewest votes?', a: cats[byDesc[byDesc.length - 1]] };
      else if (kind === 'total') it = { q: `How many ${who} answered in all?`, a: String(total) };
      else if (i !== j && kind === 'more' && counts[i] > counts[j]) it = { q: `How many more ${who} chose ${cats[i].toLowerCase()} than ${cats[j].toLowerCase()}?`, a: String(counts[i] - counts[j]), i, j };
      else if (i < j && kind === 'or') it = { q: `How many ${who} chose ${cats[i].toLowerCase()} or ${cats[j].toLowerCase()}?`, a: String(counts[i] + counts[j]), i, j };
      else if (kind === 'not') it = { q: `How many ${who} did not choose ${cats[i].toLowerCase()}?`, a: String(total - counts[i]), i };
      else if (kind === 'pct') it = { q: `What percent of the ${who} chose ${cats[i].toLowerCase()}?`, a: pc(counts[i] / total, 1), i };
      if (it && used.has(it.q)) it = null;
    }
    if (it) { used.add(it.q); items.push(Object.assign(it, { k: 'cq', kind, cats, counts, q: tag + it.q })); }
  }
  return items;
}
const qRows = items => items.map(it => `${esc(it.q.replace(/^[^:]*: /, ''))} ${blank(it.a)}`);

/* ---------- skills ---------- */
const S = {};

// K-12: plan and run a survey, with a practice tally chart first
const LANG = {
  en: { q: 'Our question', ch: 'Answer', item: 'Item', tally: 'Tally', tot: 'Total', pic: 'Picture', ask: 'Who I will ask',
    one: ['Most people chose ____.', '____ people chose ____.', 'More people chose ____ than ____.', 'The fewest people chose ____.'],
    grid: ['____ classmates said "____" for ____.', 'The most common answer for ____ was "____".', 'Few classmates said "____" for ____.', 'Overall, my classmates ____.'],
    scale: ['Often', 'Sometimes', 'Never'], yl: 'Number of people' },
  es: { q: 'Nuestra pregunta', ch: 'Respuesta', item: 'Opción', tally: 'Conteo', tot: 'Total', pic: 'Dibujo', ask: '¿A quién voy a preguntar?',
    one: ['La respuesta más popular es ____.', '____ compañeros eligieron ____.', 'Más compañeros eligieron ____ que ____.', 'La respuesta menos popular es ____.'],
    grid: ['____ compañeros dijeron «____» para ____.', 'La respuesta más común para ____ es «____».', 'Pocos compañeros dijeron «____» para ____.', 'En general, mis compañeros ____.'],
    scale: ['Siempre', 'A veces', 'Nunca'], yl: 'Número de compañeros' },
  fr: { q: 'Notre question', ch: 'Réponse', item: 'Choix', tally: 'Bâtons', tot: 'Total', pic: 'Dessin', ask: 'Qui je vais interroger',
    one: ['La réponse la plus populaire est ____.', '____ élèves ont choisi ____.', "Plus d'élèves ont choisi ____ que ____.", 'La réponse la moins populaire est ____.'],
    grid: ['____ élèves ont dit « ____ » pour ____.', 'La réponse la plus fréquente pour ____ est « ____ ».', "Peu d'élèves ont dit « ____ » pour ____.", 'En général, mes camarades ____.'],
    scale: ['Souvent', 'Parfois', 'Jamais'], yl: "Nombre d'élèves" },
};
const parseList = s => String(s || '').split(',').map(x => x.trim()).filter(x => x && x.length <= 40).slice(0, 6);
S.survey = c => {
  const { r, v, G } = c, L = LANG[v.lang] || LANG.en, K0 = G === 0;
  // practice: read a finished tally chart (or frequency table from grade 6)
  const set = r.pick(TSETS), k = K0 ? 3 : G <= 2 ? r.pick([3, 4]) : G <= 5 ? 4 : Math.min(5, set.cats.length);
  const cats = r.sample(set.cats, k), total = K0 ? r.int(8, 12) : G <= 2 ? r.int(12, 18) : G <= 5 ? r.pick([20, 24]) : r.pick([20, 25, 40]);
  const counts = split(r, total, k);
  const kinds = K0 ? ['read', 'read', 'most'] : G <= 2 ? ['read', 'most', 'more', 'least'] : G <= 5 ? ['read', 'most', 'more', 'total'] : ['total', 'pct', 'pct', 'more'];
  const items = countQs(r, cats, counts, kinds, 'students', 'Practice: ');
  const pt = ctab(G >= 6 ? ['Answer', 'Number of students'] : ['Answer', 'Tally'], cats.map((x, i) => [esc(x), G >= 6 ? String(counts[i]) : tallySvg(counts[i])]), 'st-narrow');
  const practice = `<p class="st-cap"><b>${esc(set.t)}.</b> ${esc(set.q)}</p>${pt}${fill(qRows(items), 1)}`;

  // the student's own survey
  const typed = parseList(v.choices), ch = typed.length >= 2 ? typed : null;
  const grid = v.form === 'grid' && !K0, topic = String(v.topic || '').trim();
  const scaleTyped = parseList(v.scale), scale = scaleTyped.length >= 2 ? scaleTyped.slice(0, 4) : L.scale;
  const nRows = ch ? ch.length : K0 ? 3 : grid ? 5 : 4, people = K0 ? 10 : +v.people || 10;
  const rowsLab = Array.from({ length: nRows }, (_, i) => ch ? esc(ch[i]) : line(7));
  let own = '';
  if (K0) {
    const qs = topic ? [esc(topic)] : r.sample(TSETS, 3).map(s => esc(s.q));
    own += topic ? `<p class="st-q"><b>${L.q}:</b> ${qs[0]}</p>` : `<p class="st-q"><b>Pick one question.</b></p><ul class="st-pick">${qs.map(q => `<li><span class="st-box"></span> ${q}</li>`).join('')}</ul>`;
    own += `<table class="ws-table st-k"><tbody><tr>${rowsLab.map(x => `<td class="st-kdraw">${ch ? x : ''}</td>`).join('')}</tr><tr>${rowsLab.map(() => '<td class="st-ktally"></td>').join('')}</tr></tbody></table>`;
  } else {
    own += `<p class="st-q"><b>${L.q}:</b> ${topic ? esc(topic) : line(26)}</p>`;
    if (grid) own += ctab([L.item, ...scale.map(esc)], rowsLab.map(x => [x, ...scale.map(() => '')]), 'st-grid');
    else own += ctab(G <= 2 ? [L.ch, L.pic, L.tally, L.tot] : [L.ch, L.tally, L.tot], rowsLab.map(x => G <= 2 ? [x, '', '', ''] : [x, '', '']), 'st-own');
    own += `<p class="st-cap"><b>${esc(L.ask)}</b></p><ol class="st-names" style="columns:${people > 10 ? 3 : 2}">${Array.from({ length: people }, () => `<li>${line(9)}</li>`).join('')}</ol>`;
  }
  const parts = [part('Practice: read the chart', practice), part('Your survey', own)];
  if (!K0) {
    const gcats = Array.from({ length: nRows }, (_, i) => ch ? ch[i] : '');
    const cap = grid ? `Make a bar for each ${L.item.toLowerCase()}: how many said "${esc(scale[0])}".` : 'Make a bar for each answer.';
    parts.push(part('Graph your results', `<p class="st-cap">${cap} ${G <= 2 ? 'Color one box for each vote.' : 'Give the graph a title.'}</p>${G >= 3 ? `<p>Title: ${line(24)}</p>` : ''}`
      + barGrid({ cats: gcats, blankCats: !ch, maxY: people, cells: G <= 2, yl: L.yl, label: 'Empty bar graph for the survey results' })));
    const fr2 = (grid ? L.grid : L.one).slice(0, G === 1 ? 1 : 4);
    parts.push(part('Write about the results', `<ol class="st-sent">${fr2.map(s => `<li>${frame(s)}</li>`).join('')}</ol>`));
  }
  return {
    title: topic ? `Class Survey: ${short(topic, 60)}` : 'Class Survey',
    ican: K0 ? 'I can ask a question and make a tally mark for each answer.' : 'I can plan a survey, collect answers with tally marks and show the results in a graph.',
    directions: K0 ? 'Read the tally chart and answer. Then pick a question, draw a picture of each answer in the top boxes, ask your classmates, and make a tally mark under the answer each one picks.'
      : `First read the practice chart and answer the questions. Then plan your survey: ${ch ? 'the answer choices are ready' : 'write your question and the answer choices'}, write the names of the ${people} classmates you will ask, and make one tally mark for each answer. Count the tallies, fill in the graph${G >= 2 ? ' and finish the sentences' : ''}.`,
    minutes: K0 ? 20 : 35, materials: 'pencil' + (G <= 2 ? ', crayons' : ''),
    parts, items,
    mistakes: 'Asking the same person twice or skipping someone: checking off each name keeps the count honest. In the graph, bars that do not start at zero or a scale that skips numbers.',
    notes: 'Only the practice chart has a key; the survey results are the class\'s own. Type a question and answer choices in the settings to print them on every copy' + (v.lang !== 'en' ? '; the headings and sentence frames are in the chosen language.' : '.'),
  };
};

// grades 1-5: raw answers (or a tally chart) to a frequency table, a bar graph and questions
S.tally = c => {
  const { r, v, G, n } = c;
  const set = r.pick(TSETS), k = G <= 1 ? 3 : G <= 3 ? 4 : Math.min(5, set.cats.length);
  const total = G <= 1 ? r.int(10, 14) : G === 2 ? 20 : G === 3 ? 24 : 30;
  const cats = r.sample(set.cats, k), counts = split(r, total, k);
  const fromTally = v.from === 'tally';
  const items = cats.map((x, i) => ({ k: 'cnt', q: `Number for ${x}`, a: String(counts[i]), cats, counts, i, raw: null }));
  let given;
  if (fromTally) given = ctab(['Answer', 'Tally', 'Number'], cats.map((x, i) => [esc(x), tallySvg(counts[i]), blank(counts[i], 3)]), 'st-narrow');
  else {
    const raw = r.shuffle(cats.flatMap((x, i) => Array(counts[i]).fill(x)));
    items.forEach(it => { it.raw = raw; });
    const per = 6, rows = [];
    for (let i = 0; i < raw.length; i += per) rows.push(raw.slice(i, i + per).map(esc));
    given = `<p class="st-cap">The answers, one for each student. Cross out each answer as you tally it.</p>` + table([], rows).replace('class="ws-table"', 'class="ws-table st-raw"').replace('<thead><tr></tr></thead>', '')
      + `<p class="st-cap"><b>Make the table.</b></p>` + ctab(['Answer', 'Tally', 'Number'], cats.map((x, i) => [esc(x), `<span class="ws-keyonly">${tallySvg(counts[i])}</span>`, blank(counts[i], 3)]), 'st-narrow');
  }
  const kinds = r.shuffle(G <= 2 ? ['most', 'least', 'more', 'or', 'total'] : ['most', 'more', 'or', 'not', 'least', 'total']).slice(0, n);
  const qs = countQs(r, cats, counts, kinds, 'students', 'Question: ');
  const maxY = Math.max(...counts) + 1;
  const graph = `<p>Title: ${blank(set.t, 14)}</p>` + barGrid({ cats, maxY, cells: G <= 2, vals: counts, yl: 'Number of students', label: `Bar graph grid for ${set.t}` });
  return {
    title: `${set.t}: Tally, Table and Bar Graph`,
    ican: 'I can sort survey answers with tally marks, count them and show them in a bar graph.',
    directions: `${esc(set.q)} ${total} students answered. ${fromTally ? 'Count each tally and write the number.' : 'Make a tally mark for each answer, then write the number.'} Draw a bar for each answer, give the graph a title, then answer the questions.`,
    minutes: 30, materials: 'pencil, crayons or a ruler',
    parts: [part(fromTally ? 'Count the tallies' : 'Sort the answers', given), part('Draw the bar graph', graph), part('Answer the questions', fill(qRows(qs), 1))],
    items: items.concat(qs),
    mistakes: 'Losing count in the list (crossing out each answer fixes it), and a bar graph scale that skips numbers or does not start at 0.',
    notes: `Check: the numbers in the table should add to ${total}. Any clear title works, like "${set.t}".`,
  };
};

// grade 3: circle the odd one out and give a reason
S.odd = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(NUM, n).forEach((x, si) => {
    const span = x.hi - x.lo, w = Math.max(4, Math.round(span / 3)), cnt = r.int(6, 8);
    const base = r.int(x.lo + (x.dir < 0 ? Math.round(span * 0.6) : 0), x.hi - w - (x.dir > 0 ? Math.round(span * 0.6) : 0));
    const rest = Array.from({ length: cnt - 1 }, () => r.int(base, base + w));
    const gap = Math.max(w + 3, Math.round(span * 0.55)) + r.int(0, 3);
    let o = x.dir > 0 ? Math.max(...rest) + gap : Math.min(...rest) - gap;
    if (o < 1) o = Math.max(...rest) + gap;
    const data = r.shuffle(rest.concat(o)), L = LET[si];
    items.push({ k: 'odd', q: `Set ${L}: odd one out`, a: String(o), data });
    items.push({ k: 'typlo', q: `Set ${L}: most are from`, a: String(Math.min(...rest)), data, o });
    items.push({ k: 'typhi', q: `Set ${L}: most are up to`, a: String(Math.max(...rest)), data, o });
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.what)}</b> (${esc(x.unit)})</p><div class="st-vals">${data.map(d => `<span class="st-v${d === o ? ' st-odd' : ''}">${d}</span>`).join('')}</div>`
      + `<p>Most of the numbers are from ${blank(Math.min(...rest), 3)} to ${blank(Math.max(...rest), 3)}. Why might the odd one have happened? ${line(16)}</p>${keyline('A possible reason: ' + esc(x.why) + '.')}</div>`);
  });
  return {
    title: 'The Odd One Out', ican: 'I can find a number that does not fit with the others and think of a reason.',
    directions: 'In each set, circle the number that is far away from the others. Write where most of the numbers are, then give a reason the odd one might have happened.',
    minutes: 20, parts: [part('', example('Jump distances: 52, 55, 21, 54, 50, 53', 'Most jumps are from 50 to 55 inches. 21 is far away from the rest, so circle it. Maybe the jumper slipped.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Circling the biggest number every time. The odd one can be very small too: look for the number far from the rest.',
    notes: 'Statisticians call the odd one out an outlier. Any reason that could really happen is fine.',
  };
};

// grade 5: mean and median with and without the outlier; grade 6: mean, median, mode and range
S.center = c => {
  const { r, n, G } = c, items = [], blocks = [];
  const ctxs = r.sample(NUM, Math.min(n, NUM.length)).concat(r.sample(NUM, Math.max(0, n - NUM.length)));
  if (G === 5) {
    ctxs.forEach((x, si) => {
      let rest, o, cnt;
      for (let t = 0; t < 200; t++) {
        cnt = r.int(6, 7);
        const span = x.hi - x.lo, w = Math.max(5, Math.round(span / 2.5)), base = r.int(x.lo + (x.dir < 0 ? Math.round(span / 2) : 0), x.hi - w - (x.dir > 0 ? Math.round(span / 2) : 0));
        rest = withMean(r, cnt - 1, base, base + w); if (!rest) continue;
        o = x.dir > 0 ? Math.max(...rest) + Math.round(span * 0.7) : Math.min(...rest) - Math.round(span * 0.7);
        while ((sum(rest) + o) % cnt) o += x.dir > 0 ? 1 : -1;
        if (o >= 1) break;
      }
      const data = r.shuffle(rest.concat(o)), L = LET[si];
      const m1 = mean(data), d1 = median(data), m2 = mean(rest), d2 = median(rest);
      items.push({ k: 'odd', q: `Set ${L}: outlier`, a: String(o), data },
        { k: 'mean', q: `Set ${L}: mean with`, a: N(m1), data, dp: 2 }, { k: 'median', q: `Set ${L}: median with`, a: N(d1), data },
        { k: 'mean', q: `Set ${L}: mean without`, a: N(m2), data: rest, dp: 2 }, { k: 'median', q: `Set ${L}: median without`, a: N(d2), data: rest });
      blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.what)}</b> (${esc(x.unit)}): ${list(data)}</p><p>The outlier is ${blank(o, 3)}.</p>`
        + ctab(['', 'Mean', 'Median'], [['With the outlier', blank(N(m1), 4), blank(N(d1), 4)], ['Without the outlier', blank(N(m2), 4), blank(N(d2), 4)]], 'st-narrow')
        + `<p>What changed? ${line(26)}</p>${keyline(`Taking out ${o} moved the mean ${o > m2 ? 'down' : 'up'} by ${N(Math.abs(m1 - m2))} but the median by only ${N(Math.abs(d1 - d2))}. The mean feels the outlier much more.`)}</div>`);
    });
    return {
      title: 'Mean, Median and the Outlier', ican: 'I can find the mean and median and explain how an outlier changes them.',
      directions: 'Find the outlier in each set. Then find the mean and the median with the outlier and again without it. Say what changed.',
      minutes: 30, parts: [part('', example('4, 6, 5, 25, 5: the outlier is 25.', 'With it: mean = 45 ÷ 5 = 9, median = 5 (the middle of 4, 5, 5, 6, 25). Without it: mean = 20 ÷ 4 = 5, median = 5. The mean dropped a lot; the median stayed.')), part('Practice', blocks.join(''))], items,
      mistakes: 'Finding the median without putting the numbers in order first, and dividing by the old count after taking the outlier out.',
      notes: 'Every mean on this sheet is a whole number or ends in .5 or less often a longer decimal; medians of an even count are the average of the two middle numbers.',
    };
  }
  ctxs.forEach((x, si) => {
    let data;
    for (let t = 0; t < 300; t++) { data = withMean(r, r.int(7, 10), x.lo, x.hi); if (data && modesOf(data).length === 1 && data.filter(d => d === modesOf(data)[0]).length >= 2) break; }
    const L = LET[si], m = mean(data), md = median(data), mo = modesOf(data)[0], rg = Math.max(...data) - Math.min(...data);
    items.push({ k: 'mean', q: `Set ${L}: mean`, a: N(m), data, dp: 2 }, { k: 'median', q: `Set ${L}: median`, a: N(md), data },
      { k: 'mode', q: `Set ${L}: mode`, a: String(mo), data }, { k: 'range', q: `Set ${L}: range`, a: String(rg), data });
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.what)}</b> (${esc(x.unit)}): ${list(data)}</p><p class="st-ans4">Mean ${blank(N(m), 3)} Median ${blank(N(md), 3)} Mode ${blank(mo, 3)} Range ${blank(rg, 3)}</p></div>`);
  });
  return {
    title: 'Mean, Median, Mode and Range', ican: 'I can find the mean, median, mode and range of a data set.',
    directions: 'For each data set, find the mean, median, mode and range. Put the numbers in order first.',
    minutes: 30, parts: [part('', example('Data: 9, 4, 7, 13, 7', 'In order: 4, 7, 7, 9, 13. Mean = 40 ÷ 5 = 8. Median = 7 (the middle). Mode = 7 (most often). Range = 13 − 4 = 9.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Taking the middle number before ordering the data, and giving the largest value as the range instead of largest minus smallest.',
    notes: 'Every mean is a whole number, and each set has exactly one mode.',
  };
};

S.mad = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(NUM, n).forEach((x, si) => {
    const data = withMean(r, r.int(5, 8), x.lo, x.hi) || [x.lo, x.hi], m = mean(data), L = LET[si];
    const dev = data.map(d => Math.abs(d - m)), tot = sum(dev), mad = tot / data.length;
    items.push({ k: 'mean', q: `Set ${L}: mean`, a: N(m), data, dp: 2 });
    dev.forEach((d, i) => items.push({ k: 'dev', q: `Set ${L}: distance ${i + 1}`, a: N(d), x: data[i], data }));
    items.push({ k: 'devsum', q: `Set ${L}: sum`, a: N(tot), data }, { k: 'mad', q: `Set ${L}: MAD`, a: N(mad, 1), data, dp: 1 });
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.what)}</b> (${esc(x.unit)}). Mean = ${blank(N(m), 3)}</p>`
      + ctab(['Value', ...data.map(d => String(d))], [['Distance from the mean', ...dev.map(d => blank(N(d), 2))]])
      + `<p>Sum of the distances ${blank(N(tot), 3)} ÷ ${data.length} = MAD ${blank(N(mad, 1), 3)}</p></div>`);
  });
  return {
    title: 'Mean and Mean Absolute Deviation', ican: 'I can find the mean absolute deviation to describe how spread out data are.',
    directions: 'Find the mean. Write how far each value is from the mean (always a positive distance). Add the distances and divide by how many values there are. Round the MAD to the nearest tenth.',
    minutes: 30, parts: [part('', example('Data: 3, 5, 6, 10. Mean = 24 ÷ 4 = 6.', 'Distances: 3, 1, 0, 4. Sum = 8. MAD = 8 ÷ 4 = 2. On average, a value is 2 away from the mean.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Keeping negative signs on the distances (they would add to zero), and dividing by the wrong count.',
    notes: 'Each mean is a whole number, so every distance is a whole number too.',
  };
};

const GROUPS = [['Group A', 'Group B', 'Group C', 'Group D'], ['Sample 1', 'Sample 2', 'Sample 3', 'Sample 4']];
S.box = c => {
  const { r, n } = c, x = r.pick(NUM), names = r.pick(GROUPS), items = [], rows = [], sets = [];
  for (let i = 0; i < n; i++) {
    const span = x.hi - x.lo, cnt = r.int(9, 13), w = Math.round(span * r.pick([0.45, 0.6, 0.8])), base = r.int(x.lo, x.hi - w);
    const data = Array.from({ length: cnt }, () => r.int(base, base + w)), f = five(data), L = names[i];
    sets.push({ L, data, f });
    ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum'].forEach((nm, j) => items.push({ k: 'q5', j, q: `${L}: ${nm}`, a: N(f[j]), data }));
    items.push({ k: 'iqr', q: `${L}: IQR`, a: N(f[3] - f[1]), data });
    rows.push([`<b>${esc(L)}</b>`, ...f.map(v => blank(N(v), 2.6)), blank(N(f[3] - f[1]), 2.6)]);
  }
  const all = sets.flatMap(s => s.data), sc = scaleFor(Math.min(...all) - 1, Math.max(...all) + 1, 26);
  const data = sets.map(s => `<p><b>${esc(s.L)}:</b> ${list(s.data)}</p>`).join('');
  const qs = [];
  const iqrs = sets.map(s => s.f[3] - s.f[1]), meds = sets.map(s => s.f[2]);
  if (iqrs.filter(q => q === Math.max(...iqrs)).length === 1) qs.push({ k: 'pickmax', q: 'Which set has the greatest IQR (the most spread in the middle half)?', a: sets[iqrs.indexOf(Math.max(...iqrs))].L, vals: iqrs, names: sets.map(s => s.L) });
  if (meds.filter(q => q === Math.max(...meds)).length === 1) qs.push({ k: 'pickmax', q: 'Which set has the highest median?', a: sets[meds.indexOf(Math.max(...meds))].L, vals: meds, names: sets.map(s => s.L) });
  return {
    title: 'Box Plot Builder', ican: 'I can find a five-number summary and draw box plots to compare data sets.',
    directions: `Each set lists ${esc(x.what.toLowerCase())} (${esc(x.unit)}). Order each set, find its five-number summary and IQR, then draw all the box plots on the shared scale.`,
    minutes: 35, materials: 'pencil, ruler',
    parts: [part('The data', data + `<p class="st-cap">Q1 is the median of the lower half and Q3 the median of the upper half. When the count is odd, leave the middle value out of both halves.</p>`),
      part('Five-number summaries', ctab(['Set', 'Min', 'Q1', 'Median', 'Q3', 'Max', 'IQR'], rows)),
      part('Draw the box plots', boxPlots(sets.map(s => ({ name: s.L, data: s.data, keyed: true })), { lo: sc.lo, hi: sc.hi, tick: sc.tick, lab: sc.lab }, 'Box plots on one shared scale')
        + (qs.length ? fill(qs.map(q => `${esc(q.q)} ${blank(q.a)}`), 1) : ''))],
    items: items.concat(qs),
    mistakes: 'Finding quartiles from the unordered list, and drawing each box plot on its own scale so they cannot be compared.',
    notes: 'Quartiles use the method taught in most grade 6 books (the median is left out of both halves when the count is odd). Calculators and spreadsheets may use another method and give slightly different quartiles.',
  };
};

S.fences = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(NUM, n).forEach((x, si) => {
    const span = x.hi - x.lo, cnt = r.int(10, 15), L = LET[si];
    const data = Array.from({ length: cnt }, () => r.int(x.lo + Math.round(span * 0.2), x.hi - Math.round(span * 0.2)));
    const extra = r.pick([0, 1, 1, 2]);
    for (let i = 0; i < extra; i++) { const up = x.dir > 0 ? r.chance(0.8) : r.chance(0.2); data[r.int(0, cnt - 1)] = up ? x.hi + r.int(Math.round(span * 0.4), Math.round(span * 1.1)) : Math.max(0, x.lo - r.int(Math.round(span * 0.4), Math.round(span * 0.9))); }
    const f = five(data), q = f[3] - f[1], fe = [f[1] - 1.5 * q, f[3] + 1.5 * q], os = outsOf(data);
    ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum'].forEach((nm, j) => items.push({ k: 'q5', j, q: `${L}: ${nm}`, a: N(f[j]), data }));
    items.push({ k: 'iqr', q: `${L}: IQR`, a: N(q), data }, { k: 'fence', side: 0, q: `${L}: lower fence`, a: N(fe[0]), data }, { k: 'fence', side: 1, q: `${L}: upper fence`, a: N(fe[1]), data },
      { k: 'outs', q: `${L}: outliers`, a: os.length ? os.join(', ') : 'none', data });
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.what)}</b> (${esc(x.unit)}): ${list(data)}</p><p class="st-ans4">Min ${blank(N(f[0]), 2.6)} Q1 ${blank(N(f[1]), 2.6)} Median ${blank(N(f[2]), 2.6)} Q3 ${blank(N(f[3]), 2.6)} Max ${blank(N(f[4]), 2.6)}</p>`
      + `<p class="st-ans4">IQR ${blank(N(q), 2.6)} Lower fence ${blank(N(fe[0]), 3)} Upper fence ${blank(N(fe[1]), 3)} Outliers ${blank(os.length ? os.join(', ') : 'none', 5)}</p></div>`);
  });
  return {
    title: 'Five-Number Summary and Outliers', ican: 'I can compute a five-number summary and use the 1.5 × IQR rule to flag outliers.',
    directions: 'Order each data set and find the five-number summary and the IQR. The fences are Q1 − 1.5 × IQR and Q3 + 1.5 × IQR; any value outside the fences is an outlier. Write "none" if there are none.',
    minutes: 30, parts: [part('', example('Data: 2, 4, 5, 6, 7, 8, 9, 30', 'Q1 = 4.5, median = 6.5, Q3 = 8.5, IQR = 4. Fences: 4.5 − 6 = −1.5 and 8.5 + 6 = 14.5. Only 30 is outside, so 30 is an outlier.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Using the range instead of the IQR, and calling the minimum or maximum an outlier without checking the fences.',
    notes: 'Quartiles are the medians of the lower and upper halves, leaving out the overall median when n is odd. Software may use another quartile rule; the outliers rarely change.',
  };
};

const DH = [
  { what: 'travel times to school', unit: 'minutes', lo: 3, hi: 44, b0: 0, bw: 10, lab: 5 },
  { what: 'quiz scores', unit: 'points', lo: 52, hi: 99, b0: 50, bw: 10, lab: 5 },
  { what: 'heights of students', unit: 'inches', lo: 50, hi: 69, b0: 50, bw: 5, lab: 2 },
];
S.dothist = c => {
  const { r, n } = c, x = r.pick(DH);
  let data;
  for (let t = 0; t < 400; t++) {
    data = Array.from({ length: n }, () => Math.round(x.lo + (x.hi - x.lo) * (r.next() + r.next()) / 2));
    const bins = []; for (let a = x.b0; a <= x.hi; a += x.bw) bins.push(data.filter(d => d >= a && d < a + x.bw).length);
    if (modesOf(data).length === 1 && bins.filter(b => b === Math.max(...bins)).length === 1) break;
  }
  const bins = []; for (let a = x.b0; a <= x.hi; a += x.bw) bins.push([a, a + x.bw - 1]);
  const counts = bins.map(([a, b]) => data.filter(d => d >= a && d <= b).length), hiB = bins.length - 1;
  const cut = bins[Math.max(1, Math.floor(bins.length / 2))][0];
  const sc = { lo: x.b0, hi: x.b0 + bins.length * x.bw, tick: 1, lab: x.lab };
  const items = bins.map(([a, b], i) => ({ k: 'bin', q: `Bin ${a}-${b}`, a: String(counts[i]), lo: a, hi: b, data }));
  const big = counts.indexOf(Math.max(...counts));
  const qs = [
    { k: 'atleast', q: `How many values are ${cut} or more?`, a: String(data.filter(d => d >= cut).length), cut, data },
    { k: 'mode', q: 'Which exact value happens most often (the mode)?', a: String(modesOf(data)[0]), data },
    { k: 'bigbin', q: 'Which interval has the most values?', a: `${bins[big][0]}-${bins[big][1]}`, bins, data },
    { k: 'median', q: 'What is the median?', a: N(median(data)), data },
  ];
  const labs = bins.map(([a, b]) => `${a}-${b}`);
  return {
    title: 'Dot Plot or Histogram?', ican: 'I can make a dot plot and a histogram from the same data and say what each one shows.',
    directions: `Here are ${n} ${esc(x.what)} (${esc(x.unit)}). Make a dot plot, then count the values in each interval and draw a histogram. Answer the questions.`,
    minutes: 35, materials: 'pencil, ruler',
    parts: [part('The data', vals(data)), part('Dot plot', dotPlot(data, sc, true, `Number line for a dot plot of ${x.what}`, Math.max(5, ...[...new Set(data)].map(d => data.filter(e => e === d).length))) ),
      part('Histogram', ctab(['Interval', ...labs.map(esc)], [['Frequency', ...counts.map(k => blank(k, 2))]]) + barGrid({ cats: labs, maxY: Math.max(...counts) + 1, gap: 0, vals: counts, yl: 'Frequency', label: 'Empty histogram grid' })),
      part('Questions', fill(qs.map(q => `${esc(q.q)} ${blank(q.a)}`), 1) + `<p>What can you see in the dot plot that the histogram hides? What does the histogram show quickly?</p>${lines(2)}`
        + keyline('The dot plot shows every exact value (so the mode and median can be read off it). The histogram groups the values, so the overall shape, where most values fall, is easier to see at a glance.'))],
    items: items.concat(qs),
    mistakes: 'Gaps between histogram bars (the intervals touch), and putting a value on the edge of two intervals into the wrong one: 20 belongs to 20-29, not 10-19.',
    notes: `The intervals are ${x.bw} wide. The key draws the dot plot and histogram in red.`,
  };
};

const CH = [
  { what: 'Prices of homes on one street', unit: 'thousand dollars', lo: 180, hi: 320, out: [760, 1200], up: true },
  { what: 'Yearly pay at a small shop', unit: 'thousand dollars', lo: 28, hi: 52, out: [180, 260], up: true },
  { what: 'Ages of people at a birthday party', unit: 'years', lo: 9, hi: 13, out: [66, 82], up: true },
  { what: 'Minutes on hold for a help line', unit: 'minutes', lo: 2, hi: 9, out: [44, 60], up: true },
  { what: 'Weekly allowance', unit: 'dollars', lo: 5, hi: 15, out: [60, 80], up: true },
  { what: 'Points scored by a basketball team', unit: 'points', lo: 40, hi: 62 },
  { what: 'Heights of sunflowers', unit: 'cm', lo: 140, hi: 180 },
  { what: 'Daily low temperatures', unit: '°F', lo: 28, hi: 44 },
];
S.choose = c => {
  const { r, n } = c, items = [], blocks = [];
  const outl = r.sample(CH.filter(x => x.out), n - 1), even = r.pick(CH.filter(x => !x.out));
  const sets = r.shuffle(outl.concat(even));
  sets.forEach((x, si) => {
    let data;
    for (let t = 0; t < 400; t++) {
      data = Array.from({ length: r.int(6, 9) }, () => r.int(x.lo, x.hi));
      if (x.out) data[0] = r.int(x.out[0], x.out[1]);
      const os = outsOf(data);
      if (x.out ? os.length === 1 && os[0] === data[0] : !os.length && Math.abs(mean(data) - median(data)) <= 1.5) break;
    }
    data = r.shuffle(data);
    const m = mean(data), md = median(data), os = outsOf(data), L = LET[si], pick = os.length ? 'median' : 'mean';
    items.push({ k: 'mean', q: `${L}: mean`, a: N(m, 1), data, dp: 1 }, { k: 'median', q: `${L}: median`, a: N(md), data }, { k: 'choose', q: `${L}: better center`, a: pick, data });
    const why = os.length ? `Median: the outlier ${os[0]} pulls the mean ${os[0] > md ? 'up' : 'down'} to ${N(m, 1)}, but most values are near the median, ${N(md)}.`
      : `Mean: there are no outliers and the mean (${N(m, 1)}) and median (${N(md)}) are close, so the mean uses every value well. The median works too.`;
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.what)}</b> (${esc(x.unit)}): ${list(data)}</p><p class="st-ans4">Mean ${blank(N(m, 1), 3)} Median ${blank(N(md), 3)} Better choice ${blank(pick, 4)}</p><p>Why? ${line(30)}</p>${keyline(why)}</div>`);
  });
  return {
    title: 'Mean or Median?', ican: 'I can choose the mean or the median to describe the center of a data set and explain why.',
    directions: 'Find the mean (to the nearest tenth) and the median of each set. Decide which one better describes a typical value and explain your choice.',
    minutes: 30, parts: [part('', example('Allowances: $5, $6, $6, $7, $50', 'Mean = $14.80, median = $6. Four of the five kids get $5 to $7, so the median describes a typical kid better. The $50 pulls the mean up.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Always choosing the mean because it uses every number, even when one huge value pulls it far from where most of the data sit.',
    notes: 'The key uses the 1.5 × IQR rule to decide whether a set has an outlier: with an outlier, the median; without one, the mean (the median is also accepted).',
  };
};

// grade 5: line plot in eighths, then the equal share
const LP = [
  { what: 'liquid in 10 beakers', unit: 'liter', thing: 'beaker', ask: 'If all the liquid were poured together and shared equally among the 10 beakers, how much would each beaker hold?' },
  { what: 'trail mix in 10 bags', unit: 'pound', thing: 'bag', ask: 'If all the trail mix were mixed together and shared equally among the 10 bags, how much would each bag hold?' },
];
S.lineplot = c => {
  const { r, n } = c, items = [], blocks = [];
  LP.slice(0, n).forEach((x, si) => {
    let e;
    for (let t = 0; t < 500; t++) {
      e = Array.from({ length: 9 }, () => r.int(1, 7));
      const last = (10 - sum(e) % 10) % 10;
      if (last >= 1 && last <= 7) { e.push(last); if (modesOf(e)[0] !== undefined && Math.max(...e) > Math.min(...e)) break; }
    }
    e = r.shuffle(e);
    const tot = sum(e), common = modesOf(e)[0], L = LET[si];
    const W = 640, x0 = 40, x1 = 600, y = 150, X = k => x0 + k * (x1 - x0) / 8;
    let b = Ln(x0 - 10, y, x1 + 10, y, '#222', 1.5), k2 = '';
    for (let k = 0; k <= 8; k++) b += Ln(X(k), y - 6, X(k), y + 6) + T(X(k), y + 20, k === 0 ? '0' : k === 8 ? '1' : fr(k, 8), { fs: 12 });
    const cnt = {}; e.forEach(k => { cnt[k] = (cnt[k] || 0) + 1; k2 += T(X(k), y - 12 - (cnt[k] - 1) * 15, '×', { fs: 17, c: RED, b: true }); });
    b += KG(k2) + T((x0 + x1) / 2, y + 40, `${x.unit === 'liter' ? 'Liters' : 'Pounds'}`, { fs: 12, b: true });
    items.push({ k: 'lpcount', q: `${L}: how many hold ${fr(common, 8)}`, a: String(e.filter(k => k === common).length), e, v8: common },
      { k: 'lpdiff', q: `${L}: difference`, a: fr(Math.max(...e) - Math.min(...e), 8), e },
      { k: 'lptot', q: `${L}: total`, a: mixedTxt(tot, 8), e }, { k: 'lpshare', q: `${L}: equal share`, a: fr(tot / 10, 8), e });
    blocks.push(`<div class="st-set"><p><b>${L}. The ${esc(x.what)}</b> (${x.unit}s): ${e.map(k => fr(k, 8)).join(', ')}</p>${SVG(W, 196, b, 'Number line from 0 to 1 in eighths')}`
      + fill([`How many ${x.thing}s hold ${fr(common, 8)} ${x.unit}? ${blank(e.filter(k => k === common).length, 3)}`,
        `What is the difference between the most and the least? ${blank(fr(Math.max(...e) - Math.min(...e), 8), 4)} ${x.unit}`,
        `How much is there in all? ${blank(mixedTxt(tot, 8), 5)} ${x.unit}s`, `${esc(x.ask)} ${blank(fr(tot / 10, 8), 4)} ${x.unit}`], 1, si * 4 + 1) + '</div>');
  });
  return {
    title: 'Line Plots and Fair Shares', ican: 'I can make a line plot of measurements in fractions of a unit and use it to share equally.',
    directions: 'Put an × above the number line for each measurement (1/4 is the same as 2/8, and 1/2 is the same as 4/8). Use the line plot to answer the questions. Write fractions in simplest form.',
    minutes: 30, materials: 'pencil', parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Putting 1/4 on the 1/8 mark instead of the 2/8 mark, and dividing by the number of different amounts instead of by 10.',
    notes: 'The total always shares out evenly into eighths, so each fair share is a whole number of eighths (in simplest form).',
  };
};

// two-way tables: grade 5 build from answers; 8 complete and compare; 9 relative frequencies; 10 probability and independence
const TW = [
  { rows: ['Has a curfew', 'No curfew'], cols: ['Does chores', 'No chores'], a: 'has a curfew', b: 'does chores', na: 'has no curfew', nb: 'does not do chores' },
  { rows: ['Plays a sport', 'No sport'], cols: ['Eats breakfast', 'Skips breakfast'], a: 'plays a sport', b: 'eats breakfast', na: 'does not play a sport', nb: 'skips breakfast' },
  { rows: ['Owns a pet', 'No pet'], cols: ['Likes hiking', 'Does not like hiking'], a: 'owns a pet', b: 'likes hiking', na: 'does not own a pet', nb: 'does not like hiking' },
  { rows: ['Takes music', 'No music'], cols: ['Reads for fun', 'Does not read for fun'], a: 'takes music', b: 'reads for fun', na: 'does not take music', nb: 'does not read for fun' },
  { rows: ['Rides the bus', 'Does not ride'], cols: ['Has a phone', 'No phone'], a: 'rides the bus', b: 'has a phone', na: 'does not ride the bus', nb: 'has no phone' },
  { rows: ['Grade 9', 'Grade 10'], cols: ['Plays an instrument', 'No instrument'], a: 'is in grade 9', b: 'plays an instrument', na: 'is in grade 10', nb: 'does not play an instrument' },
];
// a 2 x 2 table [[a, b], [c, d]]: assoc = the two rows split very differently; exact = the rows split exactly the same
function twoByTwo(r, assoc, exact) {
  for (let t = 0; t < 2000; t++) {
    const T0 = r.pick([40, 50, 60, 80, 100, 120, 150, 200]), R1 = Math.round(T0 * r.pick([0.3, 0.4, 0.5, 0.6])), R2 = T0 - R1;
    const q1 = r.pick([0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8]), q2 = assoc ? q1 + r.pick([-0.35, -0.3, -0.25, 0.25, 0.3, 0.35]) : exact ? q1 : q1 + r.pick([-0.02, 0, 0.02]);
    const a = R1 * q1, c = R2 * q2;
    if (q2 <= 0.05 || q2 >= 0.95) continue;
    if (exact && (!Number.isInteger(a) || !Number.isInteger(c))) continue;
    const A = Math.round(a), C = Math.round(c), m = [[A, R1 - A], [C, R2 - C]];
    if (m.flat().some(v => v < 3)) continue;
    const d = Math.abs(A / R1 - C / R2);
    if (assoc ? d < 0.15 : exact ? A * R2 !== C * R1 : d > 0.04) continue;
    return m;
  }
  return [[12, 18], [20, 30]];
}
const tw = m => ({ R: [m[0][0] + m[0][1], m[1][0] + m[1][1]], C: [m[0][0] + m[1][0], m[0][1] + m[1][1]], T: sum(m.flat()) });
S.twoway = c => {
  const { r, n, G } = c;
  if (G === 5) {
    const choices = r.pick([['Soccer', 'Basketball', 'Swimming'], ['Pizza', 'Tacos', 'Pasta'], ['Art', 'Music', 'Drama'], ['Dogs', 'Cats', 'Fish']]);
    let m;
    for (let t = 0; t < 500; t++) {
      const r1c = split(r, Math.round(n / 2) + r.int(-2, 2), 3), r2c = split(r, 0, 3);
      const rest = n - sum(r1c); const r2 = split(r, rest, 3); m = [r1c, r2];
      const col = [0, 1, 2].map(j => m[0][j] + m[1][j]);
      if (new Set(col).size === 3 && m.flat().every(v => v >= 2) && m[0].some((v, j) => v !== m[1][j]) && r2c) break;
    }
    const answers = r.shuffle(m.flatMap((row, i) => row.flatMap((v, j) => Array(v).fill(`Grade ${4 + i}, ${choices[j]}`))));
    const rows = []; for (let i = 0; i < answers.length; i += 5) rows.push(answers.slice(i, i + 5).map(esc));
    const R = m.map(row => sum(row)), C = [0, 1, 2].map(j => m[0][j] + m[1][j]);
    const items = [];
    m.forEach((row, i) => row.forEach((v, j) => items.push({ k: 'cell5', q: `Grade ${4 + i} ${choices[j]}`, a: String(v), answers, i, j, choices })));
    R.forEach((v, i) => items.push({ k: 'row5', q: `Grade ${4 + i} total`, a: String(v), answers, i }));
    C.forEach((v, j) => items.push({ k: 'col5', q: `${choices[j]} total`, a: String(v), answers, choice: choices[j] }));
    items.push({ k: 'tot5', q: 'Total', a: String(n), answers });
    const top = choices[C.indexOf(Math.max(...C))], j0 = r.int(0, 2), more = m[0][j0] > m[1][j0] ? 4 : m[0][j0] < m[1][j0] ? 5 : 0;
    const finds = [`${top} was the most popular choice overall (${Math.max(...C)} of ${n}).`, more ? `More grade ${more} students chose ${choices[j0].toLowerCase()} (${m[more - 4][j0]} compared to ${m[5 - more][j0]}).` : `The same number of grade 4 and grade 5 students chose ${choices[j0].toLowerCase()}.`, `${R[0]} grade 4 students and ${R[1]} grade 5 students answered.`];
    return {
      title: 'Two-Way Table Results', ican: 'I can organize survey answers into a two-way table and write what I notice.',
      directions: `${n} students answered a survey. Each answer shows the student's grade and choice. Tally them into the two-way table, find the totals, then write 3 things you notice.`,
      minutes: 30, parts: [part('The answers', table([], rows).replace('class="ws-table"', 'class="ws-table st-raw"').replace('<thead><tr></tr></thead>', '')),
        part('The two-way table', ctab(['', ...choices, 'Total'], [0, 1].map(i => [`<b>Grade ${4 + i}</b>`, ...m[i].map(v => blank(v, 2.5)), blank(R[i], 2.5)]).concat([['<b>Total</b>', ...C.map(v => blank(v, 2.5)), blank(n, 2.5)]]))),
        part('What I notice', `${fill([line(30), line(30), line(30)], 1)}${keyline('Possible findings: ' + finds.map(esc).join(' '))}`)],
      items, mistakes: 'Counting an answer in the right column but the wrong row. Cross out each answer as you count it, and check that the totals add to ' + n + '.',
      notes: 'Findings can compare the grades, the choices, or both. The key shows three examples.',
    };
  }
  const items = [], blocks = [];
  const ctxs = r.sample(TW, n);
  ctxs.forEach((x, si) => {
    const L = LET[si], assoc = G === 10 ? r.chance(0.5) : (si === 0 ? r.chance(0.5) : !items.find(it => it.k === 'assoc' && it.tag === LET[0])?.yes);
    const m = twoByTwo(r, assoc, G === 10 && !assoc), { R, C, T: T0 } = tw(m);
    const head = ['', ...x.cols.map(esc), 'Total'];
    const full = (cell) => [[`<b>${esc(x.rows[0])}</b>`, cell(m[0][0], 'a'), cell(m[0][1], 'b'), cell(R[0], 'R1')], [`<b>${esc(x.rows[1])}</b>`, cell(m[1][0], 'c'), cell(m[1][1], 'd'), cell(R[1], 'R2')], ['<b>Total</b>', cell(C[0], 'C1'), cell(C[1], 'C2'), cell(T0, 'T')]];
    const tag = `Table ${L}: `;
    if (G === 8) {
      const shown = r.chance(0.5) ? ['a', 'b', 'c', 'T'] : ['a', 'R1', 'C1', 'T'];
      const t = ctab(head, full((v, id) => { if (shown.includes(id)) return String(v); items.push({ k: 'cell', id, q: tag + id, a: String(v), m }); return blank(v, 2.6); }));
      const p1 = m[0][0] / R[0], p2 = m[1][0] / R[1], yes = Math.abs(p1 - p2) >= 0.1;
      items.push({ k: 'rowpct', q: `${tag}${x.rows[0]} who ${x.b}`, a: pc(p1), num: m[0][0], den: R[0] }, { k: 'rowpct', q: `${tag}${x.rows[1]} who ${x.b}`, a: pc(p2), num: m[1][0], den: R[1] },
        { k: 'assoc', tag: L, yes, q: `${tag}association`, a: yes ? 'yes' : 'no', m });
      blocks.push(`<div class="st-set"><p><b>${L}.</b> A survey of students.</p>${t}${fill([`Of the students who ${esc(x.a)}, what percent ${esc(x.b)}? ${blank(pc(p1), 3)}`,
        `Of the students who ${esc(x.na)}, what percent ${esc(x.b)}? ${blank(pc(p2), 3)}`, `Is there an association between the two? ${blank(yes ? 'yes' : 'no', 3)} Why? ${line(16)}`], 1, si * 3 + 1)}`
        + keyline(yes ? `The percents (${pc(p1)} and ${pc(p2)}) are far apart, so there is an association.` : `The percents (${pc(p1)} and ${pc(p2)}) are about the same, so there is no clear association.`) + '</div>');
    } else if (G === 9) {
      const t = ctab(head, full(v => String(v)));
      const rel = ctab(head, full((v, id) => { items.push({ k: 'rel', id, q: tag + 'relative ' + id, a: N(v / T0, 2), num: v, den: T0, m }); return blank(N(v / T0, 2), 2.6); }));
      const p1 = m[0][0] / R[0], p2 = m[1][0] / R[1], yes = Math.abs(p1 - p2) >= 0.1;
      items.push({ k: 'rowpct', q: `${tag}P1`, a: pc(p1), num: m[0][0], den: R[0] }, { k: 'rowpct', q: `${tag}P2`, a: pc(p2), num: m[1][0], den: R[1] }, { k: 'assoc', tag: L, yes, q: `${tag}association`, a: yes ? 'yes' : 'no', m });
      blocks.push(`<div class="st-set"><p><b>${L}.</b> Survey counts</p>${t}<p class="st-cap">Joint and marginal relative frequencies (divide each count by ${T0}, round to hundredths):</p>${rel}`
        + fill([`Conditional: of the students who ${esc(x.a)}, what percent ${esc(x.b)}? ${blank(pc(p1), 3)}`, `Conditional: of the students who ${esc(x.na)}, what percent ${esc(x.b)}? ${blank(pc(p2), 3)}`,
          `Is there an association? ${blank(yes ? 'yes' : 'no', 3)} Explain: ${line(16)}`], 1, si * 3 + 1)
        + keyline(yes ? `Yes: ${pc(p1)} compared to ${pc(p2)} is a big difference.` : `No: ${pc(p1)} and ${pc(p2)} are close.`) + '</div>');
    } else {
      const t = ctab(head, full(v => String(v)));
      const pA = fr(R[0], T0), pB = fr(C[0], T0), pAB = fr(m[0][0], T0), pBgA = fr(m[0][0], R[0]), pAgB = fr(m[0][0], C[0]);
      const ind = m[0][0] * T0 === R[0] * C[0];
      const qs = [['pa', `P(${x.a})`, pA, R[0], T0], ['pb', `P(${x.b})`, pB, C[0], T0], ['pab', `P(${x.a} and ${x.b})`, pAB, m[0][0], T0], ['pbga', `P(${x.b} | ${x.a})`, pBgA, m[0][0], R[0]], ['pagb', `P(${x.a} | ${x.b})`, pAgB, m[0][0], C[0]]];
      qs.forEach(([id, q, a, num, den]) => items.push({ k: 'frac', q: tag + q, a, num, den }));
      items.push({ k: 'indep', q: `${tag}independent`, a: ind ? 'yes' : 'no', m });
      blocks.push(`<div class="st-set"><p><b>${L}.</b> One student is chosen at random from this table.</p>${t}${fill(qs.map(([, q, a]) => `${esc(q)} = ${blank(a, 4)}`), 2, si * 6 + 1)}`
        + `<p>Are "${esc(x.a)}" and "${esc(x.b)}" independent? ${blank(ind ? 'yes' : 'no', 3)} Show the check: ${line(16)}</p>`
        + keyline(ind ? `Yes: P(${esc(x.b)} | ${esc(x.a)}) = ${pBgA} equals P(${esc(x.b)}) = ${pB}.` : `No: P(${esc(x.b)} | ${esc(x.a)}) = ${pBgA} is not equal to P(${esc(x.b)}) = ${pB}.`) + '</div>');
    }
  });
  const title = G === 8 ? 'Two-Way Tables' : G === 9 ? 'Two-Way Frequencies' : 'Two-Way Tables and Conditional Probability';
  return {
    title, ican: G === 8 ? 'I can complete a two-way table, find relative frequencies and decide whether there is an association.'
      : G === 9 ? 'I can find joint, marginal and conditional relative frequencies and describe an association.' : 'I can find conditional probabilities from a two-way table and test whether two events are independent.',
    directions: G === 8 ? 'Fill in the missing numbers so every row and column adds up. Then compare the row percents (round to the nearest whole percent) to decide whether there is an association.'
      : G === 9 ? 'Find the relative frequencies (to the nearest hundredth) and the conditional percents (to the nearest whole percent). Decide whether there is an association.'
        : 'Write each probability as a fraction in simplest form. Two events are independent when P(B | A) = P(B).',
    minutes: 30, parts: [part('Practice', blocks.join(''))], items,
    mistakes: G === 10 ? 'Dividing by the grand total for a conditional probability: P(B | A) divides by the number in A only.' : 'Dividing by the grand total when the question asks about one row ("of the students who...").',
    notes: G === 10 ? 'Some tables are exactly independent and some are not. A vertical bar | is read "given".' : 'The key calls it an association when the two row percents differ by 10 points or more. The tables are made up for practice.',
  };
};

S.hidden = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(TW, n).forEach((x, si) => {
    const m = twoByTwo(r, r.chance(0.5), false), { R, C, T: T0 } = tw(m), L = LET[si], tag = `Puzzle ${L}: `;
    const clues = [`There are ${T0} students in all.`, `P(${x.a}) = ${fr(R[0], T0)}`, `P(${x.b}) = ${fr(C[0], T0)}`,
      `P(${x.a} and ${x.b}) = ${fr(m[0][0], T0)}`, `P(${x.b} | ${x.a}) = ${fr(m[0][0], R[0])}`, `P(${x.na} and ${x.nb}) = ${fr(m[1][1], T0)}`];
    const ids = { a: m[0][0], b: m[0][1], R1: R[0], c: m[1][0], d: m[1][1], R2: R[1], C1: C[0], C2: C[1], T: T0 };
    Object.entries(ids).forEach(([id, v]) => items.push({ k: 'cell', id, q: tag + id, a: String(v), m }));
    const cell = id => blank(ids[id], 2.6);
    const qs = [[`P(${x.b} | ${x.na})`, m[1][0], R[1]], [`P(${x.nb} | ${x.a})`, m[0][1], R[0]], [`P(${x.a} | ${x.b})`, m[0][0], C[0]]];
    qs.forEach(([q, num, den]) => items.push({ k: 'frac', q: tag + q, a: fr(num, den), num, den }));
    blocks.push(`<div class="st-set"><p><b>${L}. Clues</b></p>${fill(r.shuffle(clues).map(esc), 2)}`
      + ctab(['', ...x.cols.map(esc), 'Total'], [[`<b>${esc(x.rows[0])}</b>`, cell('a'), cell('b'), cell('R1')], [`<b>${esc(x.rows[1])}</b>`, cell('c'), cell('d'), cell('R2')], ['<b>Total</b>', cell('C1'), cell('C2'), cell('T')]])
      + fill(qs.map(([q, num, den]) => `${esc(q)} = ${blank(fr(num, den), 4)}`), 1, si * 3 + 1) + '</div>');
  });
  return {
    title: 'Hidden Two-Way Table', ican: 'I can rebuild a two-way table from probability clues and use it to find conditional probabilities.',
    directions: 'Use the clues to fill in every cell of the table. Some clues are extra: use them to check your table. Then answer the questions as fractions in simplest form.',
    minutes: 30, parts: [part('', example('There are 50 students. P(A) = 2/5, so 2/5 × 50 = 20 students are in A.', 'Turn each probability into a count by multiplying by the total, then fill the rest so rows and columns add up.')), part('Puzzles', blocks.join(''))], items,
    mistakes: 'Using a conditional clue like P(B | A) as if it were out of the whole table: it is out of the A row only.',
    notes: 'Clues 1 to 4 are enough to fill the table. The others are checks.',
  };
};

const VN = [
  { la: 'Soccer', lb: 'Basketball', a: 'plays soccer', b: 'plays basketball' }, { la: 'Dog', lb: 'Cat', a: 'has a dog', b: 'has a cat' },
  { la: 'Art', lb: 'Band', a: 'takes art', b: 'takes band' }, { la: 'Pizza', lb: 'Tacos', a: 'likes pizza', b: 'likes tacos' },
  { la: 'Walks', lb: 'Breakfast', a: 'walks to school', b: 'eats breakfast at school' }, { la: 'Mysteries', lb: 'Comics', a: 'reads mysteries', b: 'reads comics' },
  { la: 'Swims', lb: 'Bikes', a: 'can swim', b: 'rides a bike' },
];
S.venn = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(VN, n).forEach((x, si) => {
    const a = r.int(3, 18), ab = r.int(2, 12), b = r.int(3, 18), nn = r.int(1, 12), T0 = a + ab + b + nn, L = LET[si], tag = `Diagram ${L}: `;
    const qs = [['pA', `P(${x.la})`, a + ab], ['pB', `P(${x.lb})`, b + ab], ['pAB', `P(${x.la} and ${x.lb})`, ab], ['pAoB', `P(${x.la} or ${x.lb})`, a + ab + b]];
    qs.forEach(([id, q, num]) => items.push({ k: 'venn', id, q: tag + q, a: fr(num, T0), reg: [a, ab, b, nn] }));
    blocks.push(`<div class="st-row">${vennSvg({ a, ab, b, n: nn, la: x.la, lb: x.lb })}<div><p><b>${L}.</b> ${T0} students. One is picked at random.</p>${fill(qs.map(([, q, num]) => `${esc(q)} = ${blank(fr(num, T0), 4)}`), 1, si * 4 + 1)}</div></div>`);
  });
  return {
    title: 'Venn Diagrams and the Addition Rule', ican: 'I can use a Venn diagram to find P(A or B) and explain the addition rule.',
    directions: 'Each region shows how many students are in it; the number in the corner is students in neither circle. Write each probability as a fraction in simplest form.',
    minutes: 30, parts: [part('', example('A only 8, both 4, B only 6, neither 2 (20 students).', 'P(A) = 12/20, P(B) = 10/20, P(A and B) = 4/20, so P(A or B) = 12/20 + 10/20 − 4/20 = 18/20 = 9/10.')), part('Practice', blocks.join('')),
      part('Explain', `<p>Why do we subtract P(A and B) in P(A or B) = P(A) + P(B) − P(A and B)?</p>${lines(2)}${keyline('The students in both circles are counted once in P(A) and again in P(B). Subtracting P(A and B) once makes them count only one time.')}`)],
    items, mistakes: 'Adding P(A) and P(B) without subtracting the overlap, and forgetting the students outside both circles when finding the total.',
    notes: 'Check each P(A or B) with the addition rule: it should match the count of A only + both + B only over the total.',
  };
};

// grade 7 probability
const COLORS = ['blue', 'green', 'yellow'];
function bagSvg(red, other, col, x0) {
  let b = `<path d="M${x0 + 10} 30 Q${x0 + 10} 20 ${x0 + 30} 18 L${x0 + 170} 18 Q${x0 + 190} 20 ${x0 + 190} 30 L${x0 + 195} 120 Q${x0 + 195} 132 ${x0 + 180} 132 L${x0 + 20} 132 Q${x0 + 5} 132 ${x0 + 5} 120 Z" fill="none" stroke="#222" stroke-width="1.5"/>`;
  const balls = Array(red).fill('R').concat(Array(other).fill(col[0].toUpperCase()));
  balls.forEach((t, i) => { const cx = x0 + 24 + (i % 8) * 21, cy = 40 + Math.floor(i / 8) * 22;
    b += t === 'R' ? `<circle cx="${cx}" cy="${cy}" r="9" fill="#444"/>${T(cx, cy + 4, 'R', { c: '#fff', fs: 10, b: true })}` : `<circle cx="${cx}" cy="${cy}" r="9" fill="none" stroke="#222" stroke-width="1.3"/>${T(cx, cy + 4, t, { fs: 10, b: true })}`; });
  return b;
}
S.bags = c => {
  const { r, n } = c, items = [], blocks = [];
  const same = r.int(0, n - 1), seen = new Set();
  for (let i = 0; i < n; i++) {
    let A, B;
    for (let t = 0; t < 300; t++) {
      A = [r.int(1, 8), r.int(1, 10)];
      if (i === same) { const k = r.pick([2, 3]); const g = gcd(A[0], A[1]); const a0 = A[0] / g, a1 = A[1] / g; if ((a0 + a1) * k > 24 || (a0 + a1) * k === A[0] + A[1]) continue; B = [a0 * k, a1 * k]; }
      else B = [r.int(1, 8), r.int(1, 10)];
      const pa = A[0] / (A[0] + A[1]), pb = B[0] / (B[0] + B[1]);
      if (A[0] + A[1] > 24 || B[0] + B[1] > 24) continue;
      if (i !== same && Math.abs(pa - pb) < 0.02) continue;
      const kk = A.join() + '|' + B.join(); if (seen.has(kk)) continue; seen.add(kk); break;
    }
    const col = r.pick(COLORS), L = `Pair ${i + 1}`;
    const pa = fr(A[0], A[0] + A[1]), pb = fr(B[0], B[0] + B[1]), cmp = A[0] * (B[0] + B[1]) - B[0] * (A[0] + A[1]);
    const better = cmp > 0 ? 'Bag A' : cmp < 0 ? 'Bag B' : 'same chance';
    items.push({ k: 'bag', q: `${L} A`, a: pa, red: A[0], other: A[1] }, { k: 'bag', q: `${L} B`, a: pb, red: B[0], other: B[1] }, { k: 'better', q: `${L} better`, a: better, A, B });
    const svgB = SVG(420, 140, bagSvg(A[0], A[1], col, 4) + bagSvg(B[0], B[1], col, 220) + T(100, 12, 'Bag A', { b: true }) + T(316, 12, 'Bag B', { b: true }), `Bag A: ${A[0]} red, ${A[1]} ${col}. Bag B: ${B[0]} red, ${B[1]} ${col}.`);
    blocks.push(`<div class="st-row">${svgB}<div><p><b>${i + 1}.</b> Bag A has ${A[0]} red and ${A[1]} ${col} marbles. Bag B has ${B[0]} red and ${B[1]} ${col} marbles.</p>`
      + `<p>P(red from A) = ${blank(pa, 3.5)}</p><p>P(red from B) = ${blank(pb, 3.5)}</p><p>I would rather pick from ${blank(better, 6)}</p></div></div>`);
  }
  return {
    title: 'Would You Rather: Pick a Bag', ican: 'I can write a probability as a fraction and compare chances.',
    directions: 'You win if you pull out a red marble (R) without looking. For each pair, write the probability of red from each bag as a fraction in simplest form. Then choose the better bag, or write "same chance".',
    minutes: 25, parts: [part('', example('Bag A: 2 red, 3 blue. Bag B: 3 red, 5 blue.', 'P(red from A) = 2/5 = 16/40. P(red from B) = 3/8 = 15/40. Bag A is a little better.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Picking the bag with more red marbles. What matters is red compared to all the marbles: 3 red out of 4 beats 5 red out of 12.',
    notes: 'One pair on each sheet has the same chance in both bags, written two different ways.',
  };
};

const EXP = [
  { text: 'Flip a coin and roll a number cube (1 to 6).', st: [['H', 'T'], [1, 2, 3, 4, 5, 6]], ev: [
    ['heads and an even number', o => o[0] === 'H' && o[1] % 2 === 0], ['tails and a number greater than 4', o => o[0] === 'T' && o[1] > 4], ['heads and a 3', o => o[0] === 'H' && o[1] === 3], ['tails and a number less than 3', o => o[0] === 'T' && o[1] < 3]] },
  { text: 'Roll two number cubes (1 to 6) and add the numbers.', st: [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]], ev: [
    ['a sum of 7', o => o[0] + o[1] === 7], ['a sum of 10', o => o[0] + o[1] === 10], ['doubles', o => o[0] === o[1]], ['a sum less than 5', o => o[0] + o[1] < 5], ['a sum of 11 or more', o => o[0] + o[1] >= 11]] },
  { text: 'Spin a spinner with 3 equal parts (red, blue, green) and flip a coin.', st: [['red', 'blue', 'green'], ['H', 'T']], ev: [
    ['blue and heads', o => o[0] === 'blue' && o[1] === 'H'], ['not red, and tails', o => o[0] !== 'red' && o[1] === 'T'], ['green, with either side of the coin', o => o[0] === 'green']] },
  { text: 'Choose a shirt (red, blue, white or green) and pants (jeans or shorts) without looking.', st: [['red', 'blue', 'white', 'green'], ['jeans', 'shorts']], ev: [
    ['a blue shirt with jeans', o => o[0] === 'blue' && o[1] === 'jeans'], ['shorts with a shirt that is not white', o => o[1] === 'shorts' && o[0] !== 'white'], ['a red or green shirt', o => o[0] === 'red' || o[0] === 'green']] },
  { text: 'Flip three coins.', st: [['H', 'T'], ['H', 'T'], ['H', 'T']], ev: [
    ['exactly two heads', o => o.filter(x => x === 'H').length === 2], ['at least one tail', o => o.includes('T')], ['all three the same', o => o[0] === o[1] && o[1] === o[2]]] },
  { text: 'Spin a spinner numbered 1 to 4 two times.', st: [[1, 2, 3, 4], [1, 2, 3, 4]], ev: [
    ['a sum of 5', o => o[0] + o[1] === 5], ['the same number twice', o => o[0] === o[1]], ['a product greater than 6', o => o[0] * o[1] > 6]] },
  { text: 'Pick a letter tile (A, B or C) and roll a number cube (1 to 6).', st: [['A', 'B', 'C'], [1, 2, 3, 4, 5, 6]], ev: [
    ['A and an odd number', o => o[0] === 'A' && o[1] % 2 === 1], ['not C, and a number less than 3', o => o[0] !== 'C' && o[1] < 3], ['B and a 6', o => o[0] === 'B' && o[1] === 6]] },
];
const outcomes = st => st.reduce((acc, s) => acc.flatMap(a => s.map(x => a.concat([x]))), [[]]);
const oName = o => o.map(x => typeof x === 'string' && x.length > 1 ? x[0].toUpperCase() + x.slice(1) : x).join(o.some(x => typeof x === 'string' && x.length > 1) ? '-' : '');
S.compound = c => {
  const { r, n } = c, items = [], blocks = [];
  const methods = ['tree diagram', 'table', 'organized list'];
  r.sample(EXP, n).forEach((x, si) => {
    const ei = r.int(0, x.ev.length - 1), [evName, pred] = x.ev[ei], all = outcomes(x.st), good = all.filter(pred);
    const size = x.st.reduce((p, s) => p * s.length, 1), how = x.st.length === 3 ? r.pick(['tree diagram', 'organized list']) : methods[si % 3];
    items.push({ k: 'ss', q: `${si + 1}: outcomes`, a: String(size), ex: EXP.indexOf(x) }, { k: 'pev', q: `${si + 1}: P(${evName})`, a: fr(good.length, size), ex: EXP.indexOf(x), ei });
    blocks.push(`<div class="st-set">${Gen.h.q(si + 1, `${esc(x.text)} Use a <b>${how}</b> to show the sample space.`, work(1.25, 'Your ' + how)
      + `<p class="st-ans4">Number of outcomes ${blank(size, 3)} P(${esc(evName)}) = ${blank(fr(good.length, size), 4)}</p>`
      + keyline(`Favorable: ${good.length <= 12 ? good.map(oName).join(', ') : good.length + ' outcomes'}.`))}</div>`);
  });
  return {
    title: 'Tree Diagrams and Outcome Tables', ican: 'I can find the sample space of a compound event and use it to find a probability.',
    directions: 'For each experiment, show every possible outcome with the method named. Count the outcomes, then write the probability of the event as a fraction in simplest form.',
    minutes: 35, parts: [part('', example('Flip a coin and spin a 1-2 spinner: HT tree with 2 × 2 = 4 outcomes: H1, H2, T1, T2.', 'P(heads and 2) = 1/4 because one outcome out of four matches.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Adding the choices instead of multiplying them (2 coin sides and 6 numbers make 12 outcomes, not 8), and counting 3 + 4 and 4 + 3 as one outcome.',
    notes: 'The key lists the favorable outcomes so students can check their diagrams.',
  };
};

const SPCOL = ['Red', 'Blue', 'Green', 'Yellow', 'Purple'];
S.spinner = c => {
  const { r, n } = c;
  const secs = r.pick(n === 50 ? [5, 10] : n === 20 ? [4, 5, 10] : [4, 5, 8, 10]), k = Math.min(secs, r.pick([3, 4]));
  let counts = split(r, secs, k);
  if (secs < 6) counts = Array(k).fill(1).map((x, i) => i < secs - k ? 2 : 1);
  const cols = SPCOL.slice(0, counts.length);
  const labels = r.shuffle(cols.flatMap((cl, i) => Array(counts[i]).fill(cl)));
  const items = [];
  cols.forEach((cl, i) => {
    items.push({ k: 'spin', q: `P(${cl})`, a: fr(counts[i], secs), num: labels.filter(x => x === cl).length, den: labels.length },
      { k: 'spinexp', q: `Expected ${cl} in ${n}`, a: String(n * counts[i] / secs), num: labels.filter(x => x === cl).length, den: labels.length, spins: n });
  });
  const theo = ctab(['Color', 'Sections', 'Theoretical probability', `Expected in ${n} spins`], cols.map((cl, i) => [cl, String(counts[i]), blank(fr(counts[i], secs), 3.5), blank(n * counts[i] / secs, 3)]), 'st-narrow');
  const exp = ctab(['Color', 'Tally', 'Count', 'Experimental probability'], cols.map(cl => [cl, '', '', '']), 'st-own');
  return {
    title: 'Spinner Experiment', ican: 'I can find theoretical probabilities, run an experiment and compare the two.',
    directions: `Before you spin, find the theoretical probability of each color and how many times you expect it in ${n} spins. Then spin ${n} times: hold a paper clip at the center with a pencil point and flick it. Tally each result.`,
    minutes: 40, materials: 'pencil, paper clip',
    parts: [part('The spinner', `<div class="st-row">${spinnerSvg(labels)}<div>${theo}</div></div>`), part(`Spin ${n} times`, exp),
      part('Compare', fill([`Which color came closest to what you expected? ${line(14)}`, `Which color was furthest from what you expected? ${line(14)}`, `If you spun ${n * 10} times, what would you expect to happen to your experimental probabilities? ${line(18)}`], 1)
        + keyline('Answers depend on the spins. With more spins, experimental probabilities usually get closer to the theoretical ones.'))],
    items, mistakes: 'Counting colors instead of sections: a color with 3 sections out of 8 has probability 3/8, not 1/4.',
    notes: 'The theoretical answers are keyed; the experiment results are the students\' own. Pooling the class results is a good way to show the law of large numbers.',
  };
};

// comparing two groups: grade 7 with means and MAD, grade 9 with box plots
const CMP = [
  { what: 'Heights of players', unit: 'inches', g: ['Basketball team', 'Soccer team'], lo: 60, hi: 78 },
  { what: 'Minutes of homework per night', unit: 'minutes', g: ['Grade 6', 'Grade 8'], lo: 10, hi: 60 },
  { what: 'Long jump distances', unit: 'inches', g: ['Class A', 'Class B'], lo: 40, hi: 72 },
  { what: 'Points scored per game', unit: 'points', g: ['Hawks', 'Owls'], lo: 30, hi: 70 },
  { what: 'Hours of sleep on a school night', unit: 'hours', g: ['Grade 7', 'Grade 11'], lo: 5, hi: 11 },
];
S.compare = c => {
  const { r, n, G } = c, items = [], blocks = [];
  r.sample(CMP, n).forEach((x, si) => {
    const L = LET[si], span = x.hi - x.lo, tag = `Pair ${L}: `;
    if (G === 7) {
      let A, B;
      for (let t = 0; t < 300; t++) {
        const w = Math.max(4, Math.round(span * 0.45)), base = r.int(x.lo, x.hi - w - Math.round(span * 0.3));
        const shift = r.int(Math.round(span * 0.08) + 1, Math.round(span * 0.35) + 1);
        A = withMean(r, 10, base, base + w); B = withMean(r, 10, base + shift, Math.min(x.hi, base + w + shift));
        if (A && B && mean(B) !== mean(A) && madOf(A) > 0 && madOf(B) > 0) break;
      }
      const mA = mean(A), mB = mean(B), dA = madOf(A), dB = madOf(B), diff = Math.abs(mA - mB), big = Math.max(dA, dB), ratio = diff / big;
      items.push({ k: 'mean', q: tag + 'mean 1', a: N(mA), data: A, dp: 2 }, { k: 'mean', q: tag + 'mean 2', a: N(mB), data: B, dp: 2 },
        { k: 'mad', q: tag + 'MAD 1', a: N(dA, 1), data: A, dp: 1 }, { k: 'mad', q: tag + 'MAD 2', a: N(dB, 1), data: B, dp: 1 },
        { k: 'mdiff', q: tag + 'difference', a: N(diff), A, B }, { k: 'ratio', q: tag + 'ratio', a: N(ratio, 1), A, B });
      const sc = scaleFor(Math.min(...A, ...B) - 1, Math.max(...A, ...B) + 1, 40);
      const room = Math.max(...[...A, ...B].map(v => Math.max(A.filter(a => a === v).length, B.filter(b => b === v).length)));
      blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.what)}</b> (${esc(x.unit)})</p><p class="st-cap"><b>${esc(x.g[0])}:</b> ${list(A)}</p>${dotPlot(A, { lo: sc.lo, hi: sc.hi, tick: sc.tick, lab: sc.lab * (sc.hi - sc.lo > 20 ? 5 / sc.tick : 1) }, false, x.g[0], room)}`
        + `<p class="st-cap"><b>${esc(x.g[1])}:</b> ${list(B)}</p>${dotPlot(B, { lo: sc.lo, hi: sc.hi, tick: sc.tick, lab: sc.lab * (sc.hi - sc.lo > 20 ? 5 / sc.tick : 1) }, false, x.g[1], room)}`
        + `<p class="st-ans4">Mean: ${esc(x.g[0])} ${blank(N(mA), 3)} ${esc(x.g[1])} ${blank(N(mB), 3)}. MAD: ${esc(x.g[0])} ${blank(N(dA, 1), 3)} ${esc(x.g[1])} ${blank(N(dB, 1), 3)}</p>`
        + `<p>The means differ by ${blank(N(diff), 3)}, which is ${blank(N(ratio, 1), 3)} times the larger MAD. What does that tell you? ${line(14)}</p>`
        + keyline(ratio >= 2 ? 'The difference is at least 2 MADs, so the groups are clearly different with little overlap.' : 'The difference is less than 2 MADs, so the groups overlap a lot.') + '</div>');
    } else {
      let A, B;
      for (let t = 0; t < 300; t++) {
        const w = Math.round(span * 0.5), base = r.int(x.lo, x.hi - w - Math.round(span * 0.25)), shift = r.int(1, Math.round(span * 0.3));
        A = Array.from({ length: r.int(11, 14) }, () => r.int(base, base + w)); B = Array.from({ length: r.int(11, 14) }, () => r.int(base + shift, base + shift + Math.round(w * r.pick([0.5, 0.8, 1.2]))));
        if (r.chance(0.6)) (r.chance(0.5) ? A : B)[0] = r.chance(0.5) ? base + shift + 2 * w : Math.max(0, base - w);
        if (five(A)[2] !== five(B)[2]) break;
      }
      const fa = five(A), fb = five(B);
      [[A, fa, 0], [B, fb, 1]].forEach(([d, f, gi]) => {
        ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum'].forEach((nm, j) => items.push({ k: 'q5', j, q: `${tag}${x.g[gi]} ${nm}`, a: N(f[j]), data: d }));
        items.push({ k: 'iqr', q: `${tag}${x.g[gi]} IQR`, a: N(f[3] - f[1]), data: d }, { k: 'outs', q: `${tag}${x.g[gi]} outliers`, a: outsOf(d).length ? outsOf(d).join(', ') : 'none', data: d });
      });
      const all = A.concat(B), sc = scaleFor(Math.min(...all) - 1, Math.max(...all) + 1, 26);
      const row = (gi, d, f) => [`<b>${esc(x.g[gi])}</b>`, ...f.map(v => blank(N(v), 2.4)), blank(N(f[3] - f[1]), 2.4), blank(outsOf(d).length ? outsOf(d).join(', ') : 'none', 3.5)];
      const hi = fa[2] > fb[2] ? 0 : 1, spread = (fa[3] - fa[1]) > (fb[3] - fb[1]) ? 0 : (fa[3] - fa[1]) < (fb[3] - fb[1]) ? 1 : -1;
      blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.what)}</b> (${esc(x.unit)})</p><p class="st-cap"><b>${esc(x.g[0])}:</b> ${list(A)}</p><p class="st-cap"><b>${esc(x.g[1])}:</b> ${list(B)}</p>`
        + ctab(['', 'Min', 'Q1', 'Median', 'Q3', 'Max', 'IQR', 'Outliers'], [row(0, A, fa), row(1, B, fb)])
        + boxPlots([{ name: x.g[0], data: A, keyed: true, mod: true }, { name: x.g[1], data: B, keyed: true, mod: true }], sc, 'Two box plots on a shared scale')
        + `<p>Compare the two groups using the medians and IQRs.</p>${lines(1)}`
        + keyline(`${esc(x.g[hi])} has the higher median (${N(hi ? fb[2] : fa[2])} compared to ${N(hi ? fa[2] : fb[2])}). ${spread < 0 ? 'The IQRs are equal.' : `${esc(x.g[spread])} is more spread out in the middle half (IQR ${N(spread ? fb[3] - fb[1] : fa[3] - fa[1])}).`}`) + '</div>');
    }
  });
  return G === 7 ? {
    title: 'Compare Two Groups', ican: 'I can compare two groups using their means and mean absolute deviations.',
    directions: 'Find the mean and MAD of each group (round the MAD to the nearest tenth). Then compare the difference in means to the larger MAD (round to the nearest tenth).',
    minutes: 35, parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Comparing only the means. A difference of 5 means a lot when the MAD is 1 and very little when the MAD is 10.',
    notes: 'A difference of 2 MADs or more is the usual sign that two groups are clearly different (7.SP.3).',
  } : {
    title: 'Compare Two Distributions', ican: 'I can compare two data sets with box plots, using the median, IQR and outliers.',
    directions: 'Find each five-number summary, IQR and any outliers (outside Q1 − 1.5 × IQR or Q3 + 1.5 × IQR). Draw both box plots on the shared scale, with outliers as separate dots. Then compare.',
    minutes: 35, materials: 'pencil, ruler', parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Comparing the maximums instead of the medians, and stretching a whisker out to an outlier.',
    notes: 'The whiskers go to the most extreme values that are not outliers; outliers are drawn as separate rings. Quartiles leave the median out of both halves when n is odd.',
  };
};

// grade 8 bivariate data
const SC = [
  { xl: 'Hours studied', yl: 'Test score', xr: [0, 10], m: 4, b: 55, noise: 5, ys: [40, 100, 10], kind: 'positive', xs: 1 },
  { xl: 'Age of the car (years)', yl: 'Value (thousands of dollars)', xr: [1, 12], m: -2, b: 28, noise: 2, ys: [0, 32, 4], kind: 'negative', xs: 1 },
  { xl: 'Temperature (°F)', yl: 'Hot cocoa sold (cups)', xr: [30, 80], m: -1, b: 95, noise: 5, ys: [0, 80, 10], kind: 'negative', xs: 5 },
  { xl: 'Temperature (°F)', yl: 'Ice cream cones sold', xr: [60, 100], m: 2, b: -90, noise: 7, ys: [0, 120, 10], kind: 'positive', xs: 5 },
  { xl: 'Arm span (inches)', yl: 'Height (inches)', xr: [50, 70], m: 1, b: 1, noise: 1.5, ys: [48, 72, 4], kind: 'positive', xs: 2 },
  { xl: 'Hours of screen time a day', yl: 'Hours of sleep', xr: [0, 8], m: -0.5, b: 10, noise: 0.6, ys: [4, 11, 1], kind: 'negative', xs: 1 },
  { xl: 'Day of the month born', yl: 'Height (inches)', xr: [1, 30], m: 0, b: 0, noise: 0, ys: [50, 70, 2], kind: 'none', xs: 2, flat: [52, 68] },
  { xl: 'Shoe size', yl: 'Number of books read', xr: [4, 12], m: 0, b: 0, noise: 0, ys: [0, 20, 2], kind: 'none', xs: 1, flat: [1, 19] },
];
const rnd = (x, st) => Math.round(x / st) * st;
const lw = l => l.replace(/ \([^)]*\)$/, '').toLowerCase();   // 'Temperature (°F)' -> 'temperature'
const unitOf = l => { const m = l.match(/\(([^)]*)\)$/); return m ? (m[1] === '°F' ? ' °F' : ' ' + m[1]) : ''; };
function bivar(r, x, cnt, withOut) {
  for (let t = 0; t < 400; t++) {
    const pool = Array.from({ length: Math.round((x.xr[1] - x.xr[0]) / x.xs) + 1 }, (_, i) => x.xr[0] + i * x.xs);
    cnt = Math.min(cnt, pool.length);
    const xs = r.sample(pool, cnt).sort((a, b) => a - b);
    const yst = x.ys[2] >= 4 ? 1 : x.ys[2] >= 1 ? 0.5 : 0.1;
    let pts = xs.map(v => [v, x.kind === 'none' ? r.int(x.flat[0], x.flat[1]) : +rnd(x.m * v + x.b + (r.next() * 2 - 1) * x.noise, yst).toFixed(1)]);
    if (pts.some(p => p[1] < x.ys[0] || p[1] > x.ys[1])) continue;
    let out = null;
    if (withOut && x.kind !== 'none') {
      const i = r.int(1, cnt - 2), yy = +rnd(pts[i][1] + (r.chance(0.5) ? 1 : -1) * (x.ys[1] - x.ys[0]) * 0.35, yst).toFixed(1);
      if (yy < x.ys[0] || yy > x.ys[1]) continue;
      pts[i] = [pts[i][0], yy]; out = pts[i];
    }
    const f = lsrOf(pts);
    if (x.kind === 'positive' && f.r < 0.55) continue;
    if (x.kind === 'negative' && f.r > -0.55) continue;
    if (x.kind === 'none' && Math.abs(f.r) > 0.3) continue;
    if (out) { const res = pts.map(p => Math.abs(p[1] - f.a - f.b * p[0])), mi = res.indexOf(Math.max(...res)); const s2 = srt(res); if (pts[mi] !== out || s2[s2.length - 1] < 2 * s2[s2.length - 2]) continue; }
    return { pts, out };
  }
  return null;
}
const ptxt = p => `(${fmt(p[0], 2)}, ${fmt(p[1], 2)})`;
S.scatter = c => {
  const { r, n } = c, items = [], blocks = [];
  const pool = r.shuffle(SC);
  let made = 0;
  for (const x of pool) {
    if (made >= n) break;
    const d = bivar(r, x, r.int(10, 12), x.kind !== 'none' && r.chance(0.5)); if (!d) continue;
    const L = LET[made++], tag = `Set ${L}: `;
    items.push({ k: 'assocdir', q: tag + 'association', a: x.kind, pts: d.pts }, { k: 'outpt', q: tag + 'outlier', a: d.out ? ptxt(d.out) : 'none', pts: d.pts, out: d.out });
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.xl)} and ${esc(lw(x.yl))}</b></p>` + ctab([esc(x.xl), ...d.pts.map(p => fmt(p[0], 2))], [[esc(x.yl), ...d.pts.map(p => fmt(p[1], 2))]])
      + scatter({ xs: { lo: x.xr[0] - (x.xr[0] % x.xs), hi: x.xr[1], st: x.xs * ((x.xr[1] - x.xr[0]) / x.xs > 12 ? 2 : 1) }, ys: { lo: x.ys[0], hi: x.ys[1], st: x.ys[2] }, xl: x.xl, yl: x.yl, keyPts: d.pts, label: `Empty grid for ${x.xl} and ${x.yl}` })
      + `<p class="st-ans4">Association (positive, negative or none): ${blank(x.kind, 5)} Outlier point, if any: ${blank(d.out ? ptxt(d.out) : 'none', 5)}</p><p>Describe the pattern: ${line(26)}</p>`
      + keyline(x.kind === 'none' ? 'No association: the points are scattered with no upward or downward trend.' : `A ${x.kind} association: as ${esc(lw(x.xl))} goes up, ${esc(lw(x.yl))} tends to go ${x.kind === 'positive' ? 'up' : 'down'}. The pattern is close to a line.${d.out ? ' The point ' + ptxt(d.out) + ' is far from the others.' : ''}`) + '</div>');
  }
  return {
    title: 'Scatter Plot Patterns', ican: 'I can make a scatter plot and describe its association, form and outliers.',
    directions: 'Plot each point from the table on the grid. Decide whether the association is positive, negative or none, and name any point that is far from the pattern (or write "none").',
    minutes: 35, materials: 'pencil, ruler', parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Swapping x and y when plotting, and calling a single odd point a pattern.',
    notes: 'The data are made up for practice, in realistic ranges. The key plots every point in red.',
  };
};

const eqTxt = (m, b) => { const mm = m === 1 ? '' : m === -1 ? '−' : fmt(m, 2); return `y = ${mm}x${b ? (b > 0 ? ' + ' : ' − ') + fmt(Math.abs(b), 2) : ''}`; };
S.fit = c => {
  const { r, n } = c, items = [], blocks = [];
  const pool = r.shuffle(SC.filter(x => x.kind !== 'none'));
  let made = 0;
  for (const x of pool) {
    if (made >= n) break;
    const d = bivar(r, Object.assign({}, x, { noise: x.noise * 0.7 }), r.int(9, 11), false); if (!d) continue;
    const used = d.pts.map(p => p[0]), cand = []; for (let v = x.xr[0]; v <= x.xr[1]; v += x.xs) if (!used.includes(v)) cand.push(v);
    const xp = cand.length ? r.pick(cand) : x.xr[1], yp = x.m * xp + x.b, L = LET[made++], tag = `Plot ${L}: `;
    items.push({ k: 'fiteq', q: tag + 'equation', a: eqTxt(x.m, x.b), m: x.m, b: x.b, pts: d.pts }, { k: 'fitpred', q: tag + 'prediction', a: N(yp), m: x.m, b: x.b, xp });
    const lx0 = x.xr[0], lx1 = x.xr[1];
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.xl)} and ${esc(lw(x.yl))}</b></p>`
      + scatter({ xs: { lo: x.xr[0] - (x.xr[0] % x.xs), hi: x.xr[1], st: x.xs * ((x.xr[1] - x.xr[0]) / x.xs > 12 ? 2 : 1) }, ys: { lo: x.ys[0], hi: x.ys[1], st: x.ys[2] }, xl: x.xl, yl: x.yl, pts: d.pts, keyLine: [lx0, x.m * lx0 + x.b, lx1, x.m * lx1 + x.b], label: `Scatter plot of ${x.xl} and ${x.yl}` })
      + `<p class="st-ans4">Equation of my line: ${blank(eqTxt(x.m, x.b), 7)} Predict the ${esc(lw(x.yl))} when the ${esc(lw(x.xl))} is ${fmt(xp, 2)}${esc(unitOf(x.xl))}: about ${blank(N(yp), 4)}${esc(unitOf(x.yl))}</p></div>`);
  }
  return {
    title: 'Line of Fit', ican: 'I can draw a line of fit, write its equation and use it to make a prediction.',
    directions: 'Draw a straight line that follows the trend, with about as many points above it as below. Pick two points on your line to find the slope, write the equation, then make the prediction.',
    minutes: 35, materials: 'pencil, ruler', parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Drawing the line through the first and last points only, or connecting the dots. A line of fit passes through the middle of the cloud.',
    notes: 'Lines of fit vary. The key shows one good line in red; accept equations with a close slope and intercept, and predictions near the key.',
  };
};

const SLM = [
  { xs: 'mile', xw: 'the number of miles', y: 'cost of the taxi ride', zero: 'the ride starts, before any miles', m: [1.5, 2, 2.25, 2.5, 3], b: [2.5, 3, 3.5, 4], f: v => money(v), xr: [3, 12] },
  { xs: 'week', xw: 'the number of weeks', y: 'height of the plant', zero: 'it was first measured', m: [1.5, 2, 2.5, 3], b: [3, 4, 5, 6], f: v => fmt(v, 2) + ' cm', xr: [4, 10] },
  { xs: 'minute', xw: 'the number of minutes', y: 'water left in the tank', zero: 'the tank starts draining', m: [-5, -8, -10, -12], b: [200, 240, 300], f: v => fmt(v, 2) + ' liters', xr: [5, 15] },
  { xs: 'hour of use', xw: 'the hours of use', y: 'battery charge', zero: 'the phone is fully charged', m: [-5, -8, -10, -12.5], b: [100], f: v => fmt(v, 2) + '%', xr: [2, 7] },
  { xs: 'week', xw: 'the number of weeks', y: 'money in savings', zero: 'saving starts', m: [10, 15, 20, 25], b: [40, 50, 75], f: v => money(v), xr: [6, 20] },
  { xs: 'hour', xw: 'the hours it burns', y: 'height of the candle', zero: 'the candle is lit', m: [-0.5, -1, -1.5], b: [12, 15, 18], f: v => fmt(v, 2) + ' cm', xr: [2, 8] },
  { xs: 'month', xw: 'the number of months', y: 'total cost of a gym plan', zero: 'you join (the sign-up fee)', m: [25, 30, 35], b: [20, 40, 50], f: v => money(v), xr: [3, 12] },
  { xs: 'thousand feet climbed', xw: 'thousands of feet climbed', y: 'air temperature', zero: 'the hike starts', m: [-3, -3.5, -4], b: [60, 65, 70], f: v => fmt(v, 2) + '°F', xr: [2, 6] },
];
S.slope = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(SLM, n).forEach((x, si) => {
    const m = r.pick(x.m), b = r.pick(x.b), xp = r.int(x.xr[0], x.xr[1]), yp = m * xp + b, tag = `Model ${si + 1}: `;
    const dir = m > 0 ? 'increases' : 'decreases';
    items.push({ k: 'slm', q: tag + 'slope', a: N(m), m }, { k: 'sldir', q: tag + 'direction', a: dir, m }, { k: 'slamt', q: tag + 'amount', a: x.f(Math.abs(m)), m, unitf: SLM.indexOf(x) },
      { k: 'slb', q: tag + 'intercept', a: x.f(b), b, unitf: SLM.indexOf(x) }, { k: 'slp', q: tag + 'prediction', a: x.f(yp), m, b, xp, unitf: SLM.indexOf(x) });
    blocks.push(Gen.h.q(si + 1, `The model <b>${eqTxt(m, b)}</b> gives the ${esc(x.y)}, where x is ${esc(x.xw)}.`,
      fill([`The slope is ${blank(N(m), 3)}. For each additional ${esc(x.xs)}, the ${esc(x.y)} ${blank(dir, 5)} by ${blank(x.f(Math.abs(m)), 4)}.`,
        `The y-intercept means: when ${esc(x.zero)}, the ${esc(x.y)} is ${blank(x.f(b), 4)}.`,
        `Predict the ${esc(x.y)} when x = ${xp}: ${blank(x.f(yp), 4)}`], 1)));
  });
  return {
    title: 'What the Slope Means', ican: 'I can explain what the slope and the y-intercept of a linear model mean in context.',
    directions: 'Each linear model describes a real situation. Say what the slope and the y-intercept mean, with units, then use the model to make a prediction.',
    minutes: 25, parts: [part('', example('y = 4x + 10 gives the cost of a bowling game in dollars, where x is the number of games.', 'Slope: each additional game costs $4 more. Intercept: $10 before any games (shoe rental). For 3 games: 4(3) + 10 = $22.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Reading the slope as the starting amount, and leaving off the units.',
    notes: 'A negative slope means the quantity goes down by that amount for each unit of x.',
  };
};

const RS = [
  { xl: 'Hours of practice', yl: 'Free throws made', lin: true, xs: [1, 8], m: [2, 2.5, 3], b: [8, 10, 12] },
  { xl: 'Minutes reading', yl: 'Pages read', lin: true, xs: [5, 40], step: 5, m: [0.5, 1], b: [0, 2, 3] },
  { xl: 'Speed (mph)', yl: 'Stopping distance (ft)', lin: false, xs: [10, 70], step: 10, q: x => 0.05 * x * x + 1.1 * x },
  { xl: 'Seconds after the drop', yl: 'Distance fallen (ft)', lin: false, xs: [0, 4], step: 0.5, q: x => 16 * x * x },
];
S.residuals = c => {
  const { r, n } = c, items = [], blocks = [];
  const pool = r.sample(RS.filter(x => x.lin), 1).concat(r.sample(RS.filter(x => !x.lin), 1));
  r.shuffle(pool).slice(0, n).forEach((x, si) => {
    const st = x.step || 1, xs = []; for (let v = x.xs[0]; v <= x.xs[1] + 1e-9; v += st) xs.push(+v.toFixed(2));
    let pts, m, b;
    for (let t = 0; t < 200; t++) {
      if (x.lin) { m = r.pick(x.m); b = r.pick(x.b); pts = xs.map(v => [v, Math.max(0, Math.round(m * v + b + r.int(-3, 3)))]); }
      else { pts = xs.map(v => [v, Math.round(x.q(v) * (1 + (r.next() - 0.5) * 0.04))]); const f = lsrOf(pts); m = Math.round(f.b * 2) / 2; b = Math.round(f.a); }
      const res = pts.map(p => p[1] - (m * p[0] + b));
      if (res.every(v => v === 0)) continue;
      const curved = Math.abs(lsrOf(pts.map((p, i) => [(p[0] - mean(xs)) ** 2, res[i]])).r) > 0.75;
      if (curved === !x.lin) break;
    }
    const L = LET[si], tag = `Set ${L}: `, pred = pts.map(p => m * p[0] + b), res = pts.map((p, i) => p[1] - pred[i]);
    pts.forEach((p, i) => items.push({ k: 'yhat', q: `${tag}predicted ${i + 1}`, a: N(pred[i], 1), x: p[0], m, b }, { k: 'resid', q: `${tag}residual ${i + 1}`, a: N(res[i], 1), x: p[0], y: p[1], m, b }));
    items.push({ k: 'linfit', q: tag + 'good fit', a: x.lin ? 'yes' : 'no', pts, m, b });
    const mx = Math.max(...res.map(Math.abs)), ysc = scaleFor(-mx - Math.max(1, mx * 0.1), mx + Math.max(1, mx * 0.1), 12);
    const xstep = st * (xs.length > 10 ? 2 : 1);
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.xl)} and ${esc(lw(x.yl))}.</b> The line of fit is ŷ = ${eqTxt(m, b).slice(4)}.</p>`
      + ctab(['x', ...pts.map(p => fmt(p[0], 2))], [['y', ...pts.map(p => fmt(p[1], 2))], ['Predicted ŷ', ...pred.map(v => blank(N(v, 1), 2.4))], ['Residual y − ŷ', ...res.map(v => blank(N(v, 1), 2.4))]])
      + scatter({ xs: { lo: x.xs[0], hi: x.xs[1], st: xstep }, ys: { lo: Math.min(ysc.lo, -ysc.hi), hi: Math.max(ysc.hi, -ysc.lo), st: ysc.tick * (Math.max(ysc.hi, -ysc.lo) * 2 / ysc.tick > 12 ? 2 : 1) }, zero: true, xl: x.xl, yl: 'Residual', keyPts: pts.map((p, i) => [p[0], res[i]]), label: 'Empty residual plot' })
      + `<p>Is a line a good model for these data? ${blank(x.lin ? 'yes' : 'no', 3)} How does the residual plot show it? ${line(16)}</p>`
      + keyline(x.lin ? 'Yes: the residuals scatter above and below 0 with no pattern.' : 'No: the residuals make a curved (U-shaped) pattern, so the data curve and a line misses the shape.') + '</div>');
  });
  return {
    title: 'Residuals and Fit', ican: 'I can compute residuals, make a residual plot and judge whether a linear model fits.',
    directions: 'Use the line of fit to find each predicted value ŷ, then each residual (actual y minus predicted ŷ). Plot the residuals against x and decide whether the line is a good model.',
    minutes: 35, materials: 'pencil, ruler', parts: [part('', example('Line ŷ = 2x + 5, point (4, 15).', 'Predicted ŷ = 2(4) + 5 = 13. Residual = 15 − 13 = 2: the point is 2 above the line.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Subtracting in the wrong order (ŷ − y), which flips every residual. A residual is actual minus predicted.',
    notes: 'One data set fits a line and the other curves (stopping distance and falling distance really do grow with the square of speed and time).',
  };
};

// HS probability and statistics
const ZP = [
  { ea: 'a history test', eb: 'a science test', ua: 'points', ub: 'points', ma: [70, 80], sa: [5, 8], mb: [60, 75], sb: [8, 12], dpa: 0, dpb: 0 },
  { ea: 'the long jump', eb: 'the high jump', ua: 'cm', ub: 'cm', ma: [380, 420], sa: [25, 35], mb: [130, 150], sb: [8, 12], dpa: 0, dpb: 0 },
  { ea: 'the 100 m dash', eb: 'the 400 m run', ua: 'seconds', ub: 'seconds', ma: [13, 15], sa: [0.6, 0.9], mb: [62, 70], sb: [3, 5], dpa: 1, dpb: 1, low: true },
  { ea: 'a bowling league', eb: 'a golf round', ua: 'pins', ub: 'strokes', ma: [140, 160], sa: [15, 20], mb: [88, 96], sb: [5, 8], dpa: 0, dpb: 0, lowB: true },
  { ea: 'an exam scored out of 1600', eb: 'an exam scored out of 36', ua: 'points', ub: 'points', ma: [1000, 1100], sa: [180, 220], mb: [20, 22], sb: [4, 6], dpa: 0, dpb: 0 },
  { ea: 'a math contest', eb: 'a spelling bee score', ua: 'points', ub: 'points', ma: [40, 50], sa: [6, 9], mb: [70, 80], sb: [10, 14], dpa: 0, dpb: 0 },
];
S.zscore = c => {
  const { r, n } = c, items = [], rows = [];
  for (let i = 0; i < n; i++) {
    const x = ZP[i % ZP.length], [pa, pb] = r.sample(NAMES, 2);
    let A, B;
    for (let t = 0; t < 200; t++) {
      const ma = r.int(x.ma[0], x.ma[1]), sa = x.dpa ? +(x.sa[0] + r.next() * (x.sa[1] - x.sa[0])).toFixed(1) : r.int(x.sa[0], x.sa[1]);
      const mb = r.int(x.mb[0], x.mb[1]), sb = x.dpb ? +(x.sb[0] + r.next() * (x.sb[1] - x.sb[0])).toFixed(1) : r.int(x.sb[0], x.sb[1]);
      const va = +(ma + (r.next() * 4 - 2) * sa).toFixed(x.dpa), vb = +(mb + (r.next() * 4 - 2) * sb).toFixed(x.dpb);
      A = { m: ma, s: sa, v: va, z: (va - ma) / sa }; B = { m: mb, s: sb, v: vb, z: (vb - mb) / sb };
      const ga = x.low ? -A.z : A.z, gb = (x.low || x.lowB) ? -B.z : B.z;
      if (Math.abs(ga - gb) >= 0.15 && Math.abs(A.z) >= 0.05 && Math.abs(B.z) >= 0.05) break;
    }
    const ga = x.low ? -A.z : A.z, gb = (x.low || x.lowB) ? -B.z : B.z, who = ga > gb ? pa : pb, tag = `${i + 1}: `;
    items.push({ k: 'z', q: tag + pa, a: N(A.z), ...A }, { k: 'z', q: tag + pb, a: N(B.z), ...B }, { k: 'zwho', q: tag + 'better', a: who, A, B, low: !!x.low, lowB: !!(x.low || x.lowB), pa, pb });
    const lowNote = x.low ? ' (lower times are better)' : x.lowB ? ' (in golf, fewer strokes is better)' : '';
    rows.push(`${pa} scored ${fmt(A.v, 2)} ${x.ua} in ${x.ea} (mean ${fmt(A.m, 2)}, SD ${fmt(A.s, 2)}). ${pb} scored ${fmt(B.v, 2)} ${x.ub} in ${x.eb} (mean ${fmt(B.m, 2)}, SD ${fmt(B.s, 2)})${lowNote}.`
      + `<br>z for ${pa} = ${blank(N(A.z), 3.5)} z for ${pb} = ${blank(N(B.z), 3.5)} Better relative performance: ${blank(who, 4)}`);
  }
  return {
    title: 'Z-Scores Across Scales', ican: 'I can use z-scores to compare performances measured on different scales.',
    directions: 'Find each z-score, z = (value − mean) ÷ SD, rounded to the nearest hundredth. The higher z is the better relative performance, unless lower is better for that event.',
    minutes: 25, parts: [part('', example('Ana ran 13.2 s (mean 14.0, SD 0.5): z = (13.2 − 14.0) ÷ 0.5 = −1.60.', 'For a race, a negative z is good: Ana was 1.6 SDs faster than average.')), part('Practice', fill(rows, 1))], items,
    mistakes: 'Comparing raw scores across different scales, and forgetting that for times and golf a lower (more negative) z is better.',
    notes: 'The means and SDs are invented for practice.',
  };
};

const NC = [
  { what: 'IQ scores', mu: 100, sd: 15, unit: '', who: 'people', m: 'an IQ score', iq: true },
  { what: 'weights of apples from one orchard', mu: 150, sd: 12, unit: ' g', who: 'the apples', m: 'a weight' },
  { what: 'battery lives of one phone model', mu: 20, sd: 2, unit: ' hours', who: 'the phones', m: 'a battery life' },
  { what: 'scores on a state exam', mu: 500, sd: 100, unit: ' points', who: 'the students', m: 'a score' },
  { what: 'lengths of one kind of trout', mu: 30, sd: 4, unit: ' cm', who: 'the trout', m: 'a length' },
  { what: 'times people take to finish a puzzle', mu: 18, sd: 3, unit: ' minutes', who: 'the people', m: 'a time' },
];
const REG = [0.15, 2.35, 13.5, 34, 34, 13.5, 2.35, 0.15];   // percent below −3, then each SD band, then above +3
const cut = z => [0, 0.15, 2.5, 16, 50, 84, 97.5, 99.85, 100][z + 4];   // percent below mu + z sd (z = −4 means none)
function normalSvg(mu, sdv, keyed) {
  const W = 600, H = 176, x0 = 30, x1 = 570, yb = 140, X = z => x0 + (z + 3.6) * (x1 - x0) / 7.2, Y = z => yb - 115 * Math.exp(-z * z / 2);
  let p = ''; for (let i = 0; i <= 144; i++) { const z = -3.6 + i * 0.05; p += `${i ? 'L' : 'M'}${r1(X(z))} ${r1(Y(z))}`; }
  let b = `<path d="${p}" fill="none" stroke="#222" stroke-width="2"/>` + Ln(x0, yb, x1, yb, '#222', 1.5), k = '';
  for (let z = -3; z <= 3; z++) { b += Ln(X(z), yb, X(z), Y(z), '#888', 0.8, ' stroke-dasharray="3 3"') + Ln(X(z), yb - 4, X(z), yb + 4) + (keyed ? Ln(X(z) - 18, yb + 22, X(z) + 18, yb + 22, '#555', 0.8) : T(X(z), yb + 18, fmt(mu + z * sdv, 2), { fs: 11 })); if (keyed) k += T(X(z), yb + 18, fmt(mu + z * sdv, 2), { c: RED, b: true, fs: 11 }); }
  [-2.75, -1.5, -0.5, 0.5, 1.5, 2.75].forEach((z, i) => { k += T(X(z), yb - (Math.abs(z) < 1 ? 40 : Math.abs(z) < 2 ? 14 : 8), [2.35, 13.5, 34, 34, 13.5, 2.35][i] + '%', { c: RED, fs: Math.abs(z) > 2 ? 8.5 : 10.5, b: true }); });
  return SVG(W, H, b + KG(k), `Normal curve with mean ${mu} and standard deviation ${sdv}`);
}
S.normal = c => {
  const { r, n, v } = c, items = [], blocks = [];
  const ctxs = v.ctx === 'iq' ? [NC[0]].concat(r.sample(NC.slice(1), n - 1)) : r.sample(NC, n);
  ctxs.forEach((x, si) => {
    const L = LET[si], tag = `Curve ${L}: `, val = z => fmt(x.mu + z * x.sd, 2) + x.unit, used = new Set(), qs = [];
    items.push({ k: 'nticks', q: tag + 'axis', a: [-3, -2, -1, 0, 1, 2, 3].map(z => fmt(x.mu + z * x.sd, 2)).join(', '), mu: x.mu, sd: x.sd });
    while (qs.length < 4) {
      const t = r.int(0, 2); let a, b;
      if (t === 0) { a = r.int(-3, 2); b = r.int(a + 1, 3); } else if (t === 1) { a = r.int(-3, 3); b = 4; } else { a = -4; b = r.int(-3, 3); }
      const key = a + ':' + b; if (used.has(key) || (a === -4 && b === 4)) continue; used.add(key);
      const pct = cut(b === 4 ? 4 : b) - cut(a);
      const q = a === -4 ? `What percent of ${x.who} have ${x.m} below ${val(b)}?` : b === 4 ? `What percent of ${x.who} have ${x.m} above ${val(a)}?` : `What percent of ${x.who} have ${x.m} between ${val(a)} and ${val(b)}?`;
      qs.push(q); items.push({ k: 'npct', q: tag + q, a: fmt(pct, 2) + '%', lo: a, hi: b, mu: x.mu, sd: x.sd });
    }
    const zc = r.pick([-1, 1, 2, -2]), count = 1000, nAbove = Math.round((zc > 0 ? 100 - cut(zc) : cut(zc)) * count / 100);
    const qc = `Out of ${count} ${x.who.replace(/^the /, '')}, about how many have ${x.m} ${zc > 0 ? 'above' : 'below'} ${val(zc)}?`;
    items.push({ k: 'ncount', q: tag + qc, a: String(nAbove), z: zc, count });
    const extra = x.iq ? `<p>IQ tests are scored so the mean is 100 and the SD is 15. Name one thing an IQ score does not measure, or one limit of the test.</p>${lines(1)}${keyline('Possible answers: creativity, motivation or practical skills; scores can be affected by language, schooling, test anxiety or culture; one test day is a single measurement with error.')}` : '';
    blocks.push(`<div class="st-set"><p><b>${L}.</b> The ${esc(x.what)} are approximately normal with mean ${fmt(x.mu, 2)}${x.unit} and standard deviation ${fmt(x.sd, 2)}${x.unit}. Label the axis.</p>${normalSvg(x.mu, x.sd, true)}`
      + fill(qs.map((q, i) => `${esc(q)} ${blank(items.find(it => it.q === tag + q).a, 4)}`).concat([`${esc(qc)} ${blank(nAbove, 4)}`]), 1, si * 5 + 1) + extra + '</div>');
  });
  return {
    title: ctxs[0].iq ? 'The Normal Curve and IQ' : 'The 68-95-99.7 Rule', ican: 'I can use the 68-95-99.7 rule to find percents in a normal distribution.',
    directions: 'Write the value at each standard deviation mark under the curve. About 68% of values are within 1 SD of the mean, 95% within 2 SD and 99.7% within 3 SD. Use the bands (34%, 13.5%, 2.35%, 0.15%) to answer.',
    minutes: 30, parts: [part('', example('Mean 50, SD 10: from 40 to 70 is −1 SD to +2 SD.', '34% + 34% + 13.5% = 81.5% of values are between 40 and 70.')), part('Practice', blocks.join(''))], items,
    mistakes: 'Using 68% for one side of the mean (each side is 34%), and adding the band percents in the wrong places.',
    notes: 'The rule gives approximate percents. A z-table gives slightly different values (68.27% instead of 68%).',
  };
};

S.lsr = c => {
  const { r, n } = c, items = [], blocks = [];
  const LS = [{ xl: 'Hours studied', yl: 'Quiz score' }, { xl: 'Hours of sunlight', yl: 'Plant growth (cm)' }, { xl: 'Price ($)', yl: 'Cups sold' }, { xl: 'Practice sessions', yl: 'Goals scored' }];
  r.sample(LS, n).forEach((x, si) => {
    let pts, f;
    for (let t = 0; t < 500; t++) {
      const cnt = r.int(5, 6), xs = r.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], cnt).sort((a, b) => a - b);
      if (sum(xs) % cnt) continue;
      const slope = x.yl === 'Cups sold' ? -r.int(2, 4) : r.int(1, 4), b0 = x.yl === 'Cups sold' ? r.int(35, 45) : r.int(2, 10);
      const ys = xs.map(v => slope * v + b0 + r.int(-3, 3));
      if (sum(ys) % cnt || ys.some(y => y < 0)) continue;
      pts = xs.map((v, i) => [v, ys[i]]); f = lsrOf(pts);
      if (Math.abs(f.r) > 0.6 && Math.abs(f.r) < 0.999) break;
    }
    const L = LET[si], tag = `Set ${L}: `, mx = f.mx, my = f.my;
    const cols = [p => p[0] - mx, p => p[1] - my, p => (p[0] - mx) * (p[1] - my), p => (p[0] - mx) ** 2, p => (p[1] - my) ** 2], heads = ['x − x̄', 'y − ȳ', '(x − x̄)(y − ȳ)', '(x − x̄)²', '(y − ȳ)²'];
    const rows = pts.map((p, i) => [String(p[0]), String(p[1]), ...cols.map((fn, j) => { items.push({ k: 'lcell', q: `${tag}row ${i + 1} ${heads[j]}`, a: N(fn(p)), p, j, pts }); return blank(N(fn(p)), 2.6); })]);
    const sums = [null, null, f.sxy, f.sxx, f.syy];
    rows.push(['', '<b>Sum</b>', '', '', ...[2, 3, 4].map(j => { items.push({ k: 'lsum', q: `${tag}sum ${heads[j]}`, a: N(sums[j]), j, pts }); return blank(N(sums[j]), 2.6); })]);
    items.push({ k: 'lmean', q: tag + 'x mean', a: N(mx), pts, j: 0 }, { k: 'lmean', q: tag + 'y mean', a: N(my), pts, j: 1 },
      { k: 'lb', q: tag + 'slope', a: N(f.b, 3), pts }, { k: 'la', q: tag + 'intercept', a: N(f.a, 3), pts }, { k: 'lr', q: tag + 'r', a: N(f.r, 3), pts }, { k: 'lr2', q: tag + 'r squared', a: N(f.r * f.r, 3), pts });
    blocks.push(`<div class="st-set"><p><b>${L}. x = ${esc(lw(x.xl))}, y = ${esc(lw(x.yl))}.</b> x̄ = ${blank(N(mx), 2.6)} ȳ = ${blank(N(my), 2.6)}</p>` + ctab(['x', 'y', ...heads], rows)
      + `<p class="st-ans4">Slope b = ${blank(N(f.b, 3), 4)} Intercept a = ${blank(N(f.a, 3), 4)} ŷ = a + bx. r = ${blank(N(f.r, 3), 4)} r² = ${blank(N(f.r * f.r, 3), 4)}</p>`
      + `<p>Interpret the slope and r² in context: ${line(20)}</p>${keyline(`For each additional unit of ${esc(lw(x.xl))}, the predicted ${esc(lw(x.yl))} ${f.b > 0 ? 'rises' : 'falls'} by about ${N(Math.abs(f.b), 3)}. About ${pc(f.r * f.r, 1)} of the variation in ${esc(lw(x.yl))} is explained by the line.`)}</div>`);
  });
  return {
    title: 'Least Squares by Hand', ican: 'I can compute the least squares regression line, r and r² by hand and interpret them.',
    directions: 'Find the means, fill in the table, and add the last three columns. Then b = Σ(x − x̄)(y − ȳ) ÷ Σ(x − x̄)², a = ȳ − b·x̄, and r = Σ(x − x̄)(y − ȳ) ÷ √(Σ(x − x̄)² · Σ(y − ȳ)²). Round b, a, r and r² to three decimal places.',
    minutes: 40, materials: 'pencil, calculator', parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Rounding b before finding a (use the unrounded slope), and squaring r before checking its sign.',
    notes: 'The means are whole numbers so the deviations stay simple. A calculator\'s LinReg gives the same b, a and r.',
  };
};

const SEG = [
  { q: 'How do you get to school?', groups: ['Grade 9', 'Grade 10', 'Grade 11'], cats: ['Bus', 'Car', 'Walk or bike'] },
  { q: 'Which lunch do you buy most often?', groups: ['Freshmen', 'Seniors'], cats: ['Hot lunch', 'Salad bar', 'Sandwich'] },
  { q: 'How much sleep do you get on school nights?', groups: ['Athletes', 'Non-athletes'], cats: ['Under 7 hours', '7 to 8 hours', 'Over 8 hours'] },
  { q: 'Where do you study most?', groups: ['Morning class', 'Afternoon class', 'Evening class'], cats: ['Home', 'Library', 'Other'] },
];
S.segbar = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(SEG, n).forEach((x, si) => {
    const assoc = r.chance(0.6), g = x.groups.length;
    let m;
    for (let t = 0; t < 500; t++) {
      const base = split(r, 20, 3).map(v => v / 20);
      m = x.groups.map(() => { const tot = r.pick([40, 50, 60, 80]), sh = assoc ? r.shuffle(base) : base; const a = Math.round(tot * sh[0] + r.int(-2, 2)), b = Math.round(tot * sh[1] + r.int(-2, 2)); return [a, b, tot - a - b]; });
      if (m.flat().some(v => v < 3)) continue;
      const pcts = m.map(col => col.map(v => v / sum(col))), spread = Math.max(...[0, 1, 2].map(k => Math.max(...pcts.map(p => p[k])) - Math.min(...pcts.map(p => p[k]))));
      if (assoc ? spread >= 0.15 : spread <= 0.06) break;
    }
    const L = LET[si], tag = `Table ${L}: `, pcts = m.map(col => col.map(v => v / sum(col)));
    const spread = Math.max(...[0, 1, 2].map(k => Math.max(...pcts.map(p => p[k])) - Math.min(...pcts.map(p => p[k])))), yes = spread >= 0.1;
    m.forEach((col, gi) => col.forEach((v, k) => items.push({ k: 'segp', q: `${tag}${x.groups[gi]} ${x.cats[k]}`, a: pc(v / sum(col)), num: v, col })));
    items.push({ k: 'segassoc', q: tag + 'association', a: yes ? 'yes' : 'no', m });
    const counts = ctab(['', ...x.groups.map(esc)], x.cats.map((ct, k) => [`<b>${esc(ct)}</b>`, ...m.map(col => String(col[k]))]).concat([['<b>Total</b>', ...m.map(col => String(sum(col)))]]));
    const pt = ctab(['Percent of the group', ...x.groups.map(esc)], x.cats.map((ct, k) => [`<b>${esc(ct)}</b>`, ...m.map(col => blank(pc(col[k] / sum(col)), 3))]));
    // the segmented bars: blank 0-100% grid; the key stacks the segments in red with their labels
    const W = 120 + g * 130, H = 250, y0 = 220, top = 20, per = (y0 - top) / 100;
    let b = '';
    for (let p = 0; p <= 100; p += 10) b += Ln(60, y0 - p * per, 80 + g * 130, y0 - p * per, p % 50 ? '#ddd' : '#999', 0.7) + T(54, y0 - p * per + 4, p + '%', { a: 'end', fs: 10 });
    b += Ln(60, top, 60, y0, '#222', 1.5) + Ln(60, y0, 80 + g * 130, y0, '#222', 1.5);
    let k = '';
    m.forEach((col, gi) => {
      const xl = 90 + gi * 130; b += T(xl + 45, y0 + 16, esc(x.groups[gi]), { fs: 11 });
      let acc = 0; col.forEach((v, ci) => { const h = 100 * v / sum(col); k += `<rect x="${xl}" y="${r1(y0 - (acc + h) * per)}" width="90" height="${r1(h * per)}" fill="none" stroke="${RED}" stroke-width="1.6"/>` + T(xl + 45, y0 - (acc + h / 2) * per + 4, esc(short(x.cats[ci], 14)), { c: RED, fs: 9.5, b: true }); acc += h; });
    });
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.q)}</b></p>${counts}${pt}${SVG(W, H, b + KG(k), 'Empty grid for segmented bar graphs')}`
      + `<p>Is there an association between the group and the answer? ${blank(yes ? 'yes' : 'no', 3)} Explain: ${line(18)}</p>`
      + keyline(yes ? 'Yes: the segments are very different sizes from one group to another.' : 'No: the bars are split into nearly the same percents for every group.') + '</div>');
  });
  return {
    title: 'Segmented Bar Graphs', ican: 'I can build segmented bar graphs from a two-way table and describe an association.',
    directions: 'Turn each column into percents of that group (nearest whole percent). Draw one bar for each group, 100% tall, split into segments for each answer, and label them. Then decide whether there is an association.',
    minutes: 35, materials: 'pencil, ruler', parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Using counts instead of percents (bigger groups look bigger), and dividing by the grand total instead of the group total.',
    notes: 'Rounded percents in a group may add to 99% or 101%. The key calls it an association when an answer\'s percent differs by 10 points or more between groups.',
  };
};

const GAMES = [
  { text: (c, p) => `Pay ${money(c)} to roll a number cube. Roll a 6 and win ${money(p[0])}${p[1] ? `; roll a 5 and win ${money(p[1])}` : ''}.`, den: 6, nums: [1, 1], labs: ['Roll a 6', 'Roll a 5'] },
  { text: (c, p) => `Pay ${money(c)} to spin a spinner with 10 equal sections: 1 gold section wins ${money(p[0])}${p[1] ? ` and 3 silver sections win ${money(p[1])}` : ''}.`, den: 10, nums: [1, 3], labs: ['Gold', 'Silver'] },
  { text: (c, p) => `Pay ${money(c)} to draw a card from a standard 52-card deck. An ace wins ${money(p[0])}${p[1] ? `; a face card (jack, queen or king) wins ${money(p[1])}` : ''}.`, den: 52, nums: [4, 12], labs: ['Ace', 'Face card'] },
  { text: (c, p) => `Pay ${money(c)} to flip two coins. Two heads win ${money(p[0])}${p[1] ? `; exactly one head wins ${money(p[1])}` : ''}.`, den: 4, nums: [1, 2], labs: ['Two heads', 'One head'] },
  { text: (c, p) => `Pay ${money(c)} to pick a rubber duck from a pool of 20. Two have a star and win ${money(p[0])}${p[1] ? `; five have a dot and win ${money(p[1])}` : ''}.`, den: 20, nums: [2, 5], labs: ['Star', 'Dot'] },
  { text: (c, p) => `Pay ${money(c)} to roll two number cubes. Doubles win ${money(p[0])}${p[1] ? `; a sum of 7 wins ${money(p[1])}` : ''}.`, den: 36, nums: [6, 6], labs: ['Doubles', 'Sum of 7'] },
];
S.ev = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(GAMES, n).forEach((g, si) => {
    const cost = r.pick([1, 2, 3, 5]), two = g.nums[0] + g.nums[1] < g.den && r.chance(0.5), fair = r.chance(0.35);
    let p;
    for (let t = 0; t < 300; t++) {
      const b = two ? r.int(1, Math.max(1, Math.floor(cost * g.den / g.nums[1] / 3))) : 0;
      const need = cost * g.den - (two ? g.nums[1] * b : 0);
      let a = need / g.nums[0];
      if (fair) { if (!Number.isInteger(a) || a <= cost) continue; }
      else { a = Math.max(cost + 1, Math.round(a * r.pick([0.5, 0.6, 0.7, 0.8, 1.25]))); if (a * g.nums[0] + (two ? b * g.nums[1] : 0) === cost * g.den) continue; }
      p = two ? [a, b] : [a]; if (!two || a > b) break;
    }
    const outs = p.map((amt, i) => ({ lab: g.labs[i], net: amt - cost, num: g.nums[i] }));
    outs.push({ lab: 'No prize', net: -cost, num: g.den - sum(outs.map(o => o.num)) });
    const ev = sum(outs.map(o => o.net * o.num)) / g.den, sdev = sd(outs.map(o => o.net), outs.map(o => o.num / g.den));
    const gross = sum(p.map((amt, i) => amt * g.nums[i])), verdict = gross === cost * g.den ? 'fair' : gross < cost * g.den ? 'not fair (favors the booth)' : 'not fair (favors the player)';
    const tag = `Game ${si + 1}: `;
    outs.forEach(o => items.push({ k: 'evnet', q: `${tag}${o.lab} net`, a: money(o.net), o, cost }, { k: 'evp', q: `${tag}${o.lab} probability`, a: fr(o.num, g.den), o, den: g.den }));
    items.push({ k: 'evm', q: tag + 'expected value', a: money(ev), outs, den: g.den }, { k: 'evsd', q: tag + 'SD', a: money(sdev), outs, den: g.den }, { k: 'evfair', q: tag + 'fair', a: verdict, cost, p, nums: g.nums, den: g.den });
    blocks.push(Gen.h.q(si + 1, esc(g.text(cost, p)) + ' (The prize is paid instead of returning what you paid.)',
      ctab(['Outcome', 'Net gain X', 'Probability'], outs.map(o => [esc(o.lab), blank(money(o.net), 3.5), blank(fr(o.num, g.den), 3.5)]), 'st-narrow')
      + `<p class="st-ans4">E(X) = ${blank(money(ev), 4)} SD of X = ${blank(money(sdev), 4)} The game is ${blank(verdict, 12)}</p>`));
  });
  return {
    title: 'Is the Carnival Game Fair?', ican: 'I can compute the expected value and standard deviation of a game and decide whether it is fair.',
    directions: 'For each game, list the net gain for each outcome (prize minus the cost to play) and its probability. Then find E(X) = Σ x·P(x) and SD = √Σ (x − E(X))²·P(x), to the nearest cent. A game is fair when E(X) = $0.',
    minutes: 35, materials: 'pencil, calculator', parts: [part('', example('Pay $1, roll a 6 to win $4.', 'Net gains: $3 with P = 1/6, −$1 with P = 5/6. E(X) = 3/6 − 5/6 = −$0.33: on average you lose 33 cents a game, so it favors the booth.')), part('Games', blocks.join(''))], items,
    mistakes: 'Using the prize instead of the net gain (prize minus the cost), and forgetting the "no prize" outcome.',
    notes: 'Some games are built to be exactly fair. A face card is a jack, queen or king (12 per deck).',
  };
};

const CB = [
  { make: (r) => { const a = [r.int(20, 30), r.int(3, 5)], b = [r.int(12, 20), r.int(2, 4)]; return { text: `X = the time Jo takes to get ready (mean ${a[0]} minutes, SD ${a[1]} minutes) and Y = Jo's drive to school (mean ${b[0]} minutes, SD ${b[1]} minutes) are independent. Find the mean and SD of the total time T = X + Y.`, mean: a[0] + b[0], sd: Math.sqrt(a[1] ** 2 + b[1] ** 2), kind: 'sum', a, b }; } },
  { make: (r) => { const a = [r.int(70, 80), r.int(6, 10)], b = [r.int(60, 72), r.int(6, 10)]; return { text: `The Hawks score X points per game (mean ${a[0]}, SD ${a[1]}) and the Owls score Y points (mean ${b[0]}, SD ${b[1]}), independently. Find the mean and SD of the margin D = X − Y.`, mean: a[0] - b[0], sd: Math.sqrt(a[1] ** 2 + b[1] ** 2), kind: 'diff', a, b }; } },
  { make: (r) => { const a = [r.int(8, 15), r.int(2, 4)], k = r.pick([12, 15, 18]), f = r.pick([10, 20, 25]); return { text: `A tutor works X hours a week (mean ${a[0]}, SD ${a[1]}). Weekly pay is P = ${k}X + ${f} dollars. Find the mean and SD of P.`, mean: k * a[0] + f, sd: k * a[1], kind: 'lin', a, k, f }; } },
  { make: (r) => { const a = [r.int(15, 25), r.int(3, 6)]; return { text: `Daily highs in a city in May have mean ${a[0]} °C and SD ${a[1]} °C. In Fahrenheit, F = 1.8C + 32. Find the mean and SD in °F.`, mean: 1.8 * a[0] + 32, sd: 1.8 * a[1], kind: 'lin', a, k: 1.8, f: 32 }; } },
  { make: (r) => { const a = [r.pick([140, 150, 160]), r.int(8, 15)], k = r.pick([4, 6, 9]); return { text: `Apples from one orchard weigh X grams (mean ${a[0]}, SD ${a[1]}). A bag holds ${k} apples chosen at random (independent). Find the mean and SD of the total weight W.`, mean: k * a[0], sd: a[1] * Math.sqrt(k), kind: 'nsum', a, k }; } },
  { make: (r) => { const a = [r.int(14, 18), r.int(2, 3)], b = [r.int(20, 26), r.int(3, 5)]; return { text: `A quiz score X (mean ${a[0]}, SD ${a[1]}) and a project score Y (mean ${b[0]}, SD ${b[1]}) are independent. The grade is G = X + 2Y. Find the mean and SD of G.`, mean: a[0] + 2 * b[0], sd: Math.sqrt(a[1] ** 2 + 4 * b[1] ** 2), kind: 'combo', a, b }; } },
  { make: (r) => { const a = [r.int(500, 560), r.int(20, 40)], k = r.pick([5, 8, 10]), f = r.pick([200, 500, 1000]); return { text: `A shop sells X jackets a season (mean ${a[0]}, SD ${a[1]}). Profit is ${k}X − ${f} dollars. Find the mean and SD of the profit.`, mean: k * a[0] - f, sd: k * a[1], kind: 'lin', a, k, f: -f }; } },
  { make: (r) => { const a = [r.int(40, 50), r.int(3, 5)], b = [r.int(30, 38), r.int(2, 4)]; return { text: `Box A holds X ounces of cereal (mean ${a[0]}, SD ${a[1]}) and box B holds Y ounces (mean ${b[0]}, SD ${b[1]}), independently. Find the mean and SD of the difference X − Y.`, mean: a[0] - b[0], sd: Math.sqrt(a[1] ** 2 + b[1] ** 2), kind: 'diff', a, b }; } },
];
S.combine = c => {
  const { r, n } = c, items = [], rows = [];
  r.sample(CB, n).forEach((t, si) => {
    const p = t.make(r), tag = `${si + 1}: `;
    items.push({ k: 'cbm', q: tag + 'mean', a: N(p.mean), p }, { k: 'cbs', q: tag + 'SD', a: N(p.sd), p });
    rows.push(`${esc(p.text)}<br>Mean ${blank(N(p.mean), 4)} SD ${blank(N(p.sd), 4)}`);
  });
  return {
    title: 'Combining Random Variables', ican: 'I can find the mean and standard deviation of sums, differences and linear changes of random variables.',
    directions: 'Means add and subtract directly. For independent variables, variances (SD²) add, for sums and for differences. A linear change a + bX multiplies the SD by |b|. Round SDs to the nearest hundredth.',
    minutes: 30, materials: 'pencil, calculator', parts: [part('', example('X: mean 10, SD 3. Y: mean 4, SD 4. Independent.', 'X − Y has mean 10 − 4 = 6 and SD √(3² + 4²) = 5. Note the SDs do not subtract.')), part('Practice', fill(rows, 1))], items,
    mistakes: 'Subtracting variances for X − Y, adding SDs instead of variances, and adding the constant to the SD in a linear change.',
    notes: 'A sum of n independent copies of X has SD σ√n, not nσ (that would be one value times n).',
  };
};

const TR = [
  { test: 'A screening test checks people for a rare disease.', d: 'have the disease', yes: 'When a person has the disease', no: 'When a person does not', pos: 'comes back positive', D: 'Disease', ND: 'No disease' },
  { test: 'A rapid test checks students for strep throat.', d: 'have strep throat', yes: 'When a student has strep throat', no: 'When a student does not', pos: 'comes back positive', D: 'Strep', ND: 'No strep' },
  { test: 'A scanner checks factory parts for cracks.', d: 'are cracked', yes: 'When a part is cracked', no: 'When a part is not cracked', pos: 'flags it', D: 'Cracked', ND: 'Not cracked' },
  { test: 'A filter checks emails for scams.', d: 'are scams', yes: 'When an email is a scam', no: 'When an email is not a scam', pos: 'flags it', D: 'Scam', ND: 'Not a scam' },
];
function treeSvg(p, se, sp, x) {
  const W = 600, H = 230, root = [20, 115], l1 = [[170, 58], [170, 172]], l2 = [[400, 28], [400, 88], [400, 142], [400, 202]];
  let b = '', k = '';
  const edge = (a, c, lab, keyed) => { b += Ln(a[0], a[1], c[0] - 6, c[1], '#222', 1.4); const mx = (a[0] + c[0]) / 2, my = (a[1] + c[1]) / 2 - 6; if (keyed) { b += Ln(mx - 22, my + 3, mx + 22, my + 3, '#555', 0.8); k += T(mx, my, lab, { c: RED, b: true }); } else b += T(mx, my, lab, { b: true }); };
  edge(root, l1[0], fmt(p, 4), false); edge(root, l1[1], fmt(1 - p, 4), true);
  const n0 = [l1[0][0] + 78, l1[0][1]], n1 = [l1[1][0] + 78, l1[1][1]];
  edge(n0, l2[0], fmt(se, 4), false); edge(n0, l2[1], fmt(1 - se, 4), true); edge(n1, l2[2], fmt(1 - sp, 4), true); edge(n1, l2[3], fmt(sp, 4), false);
  b += T(l1[0][0] + 4, l1[0][1] + 4, esc(x.D), { a: 'start', b: true, fs: 10.5 }) + T(l1[1][0] + 4, l1[1][1] + 4, esc(x.ND), { a: 'start', b: true, fs: 10.5 });
  const ends = [p * se, p * (1 - se), (1 - p) * (1 - sp), (1 - p) * sp], labs = ['+', '−', '+', '−'];
  l2.forEach((pt, i) => { b += T(pt[0] + 2, pt[1] + 4, labs[i], { a: 'start', b: true, fs: 13 }) + T(pt[0] + 20, pt[1] + 4, 'P =', { a: 'start', fs: 11 }) + Ln(pt[0] + 44, pt[1] + 6, pt[0] + 120, pt[1] + 6, '#555', 0.8); k += T(pt[0] + 82, pt[1] + 3, fmt(ends[i], 4), { c: RED, b: true }); });
  return SVG(W, H, b + KG(k), 'Tree diagram with branches for the condition and the test result');
}
S.tree = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(TR, n).forEach((x, si) => {
    const p = r.pick([0.01, 0.02, 0.04, 0.05, 0.1]), se = r.pick([0.9, 0.95, 0.98, 0.99]), sp = r.pick([0.9, 0.92, 0.95, 0.97]);
    const tp = p * se, fp = (1 - p) * (1 - sp), pos = tp + fp, tag = `Problem ${si + 1}: `;
    items.push({ k: 'trc', q: tag + 'P(not D)', a: N(1 - p, 4), p, se, sp, which: 'nd' }, { k: 'trc', q: tag + 'P(- | D)', a: N(1 - se, 4), p, se, sp, which: 'fn' }, { k: 'trc', q: tag + 'P(+ | not D)', a: N(1 - sp, 4), p, se, sp, which: 'fpr' },
      { k: 'trj', q: tag + 'P(D and +)', a: N(tp, 4), p, se, sp, which: 'tp' }, { k: 'trj', q: tag + 'P(not D and +)', a: N(fp, 4), p, se, sp, which: 'fp' },
      { k: 'trj', q: tag + 'P(+)', a: N(pos, 4), p, se, sp, which: 'pos' }, { k: 'trp', q: tag + 'P(D | +)', a: N(tp / pos, 3), p, se, sp, which: 'ppv' }, { k: 'trp', q: tag + 'P(not D | +)', a: N(fp / pos, 3), p, se, sp, which: 'fdr' });
    blocks.push(Gen.h.q(si + 1, `${esc(x.test)} ${pc(p, 2)} of them ${esc(x.d)}. ${esc(x.yes)}, the test ${esc(x.pos)} ${pc(se, 2)} of the time. ${esc(x.no)}, the test still ${esc(x.pos)} ${pc(1 - sp, 2)} of the time. Fill in the missing branch probabilities and the end probabilities.`,
      treeSvg(p, se, sp, x) + fill([`P(${esc(x.D.toLowerCase())} and +) = ${blank(N(tp, 4), 4)}`, `P(${esc(x.ND.toLowerCase())} and +) = ${blank(N(fp, 4), 4)}`, `P(+) = ${blank(N(pos, 4), 4)}`,
        `P(${esc(x.D.toLowerCase())} | +) = ${blank(N(tp / pos, 3), 4)}`, `The chance a positive result is a false positive, P(${esc(x.ND.toLowerCase())} | +) = ${blank(N(fp / pos, 3), 4)}`], 2, si * 5 + 1)));
  });
  return {
    title: 'Tree Diagrams: Screening Tests', ican: 'I can use a tree diagram to find the chance that a positive test result is a false positive.',
    directions: 'Each pair of branches adds to 1. Multiply along a path for an end probability. Then P(+) adds both + paths, and P(condition | +) = P(condition and +) ÷ P(+). Round end probabilities to 4 decimal places and the conditionals to 3.',
    minutes: 35, materials: 'pencil, calculator', parts: [part('Problems', blocks.join(''))], items,
    mistakes: 'Reading the test\'s accuracy as the chance a positive person is sick. When the condition is rare, most positives can be false positives.',
    notes: 'The surprise is the point: with a rare condition, even a good test gives many false positives. Compute P(not condition | +) from the unrounded end probabilities.',
  };
};

const SP = [
  { pop: 'students at a large high school of 2,400', N: 2400, trait: 'have a part-time job', p: [0.2, 0.25, 0.3, 0.35, 0.4] },
  { pop: 'adults in a city of 80,000', N: 80000, trait: 'ride a bike to work', p: [0.05, 0.08, 0.1, 0.12] },
  { pop: 'seeds in a shipment of 5,000', N: 5000, trait: 'sprout', p: [0.8, 0.85, 0.9] },
  { pop: 'voters in a town of 12,000', N: 12000, trait: 'support a new park', p: [0.45, 0.55, 0.6] },
  { pop: 'phones in a factory run of 2,000', N: 2000, trait: 'have a defect', p: [0.02, 0.03, 0.05] },
  { pop: 'households in a county of 30,000', N: 30000, trait: 'have a dog', p: [0.35, 0.4, 0.45] },
  { pop: 'students at a school of 900', N: 900, trait: 'walk to school', p: [0.15, 0.2, 0.25] },
  { pop: 'trees in a forest plot of 1,500', N: 1500, trait: 'show signs of disease', p: [0.06, 0.1, 0.15] },
];
S.sampprop = c => {
  const { r, n } = c, items = [], rows = [];
  r.sample(SP, n).forEach((x, si) => {
    const p = r.pick(x.p), nn = r.pick([20, 40, 50, 80, 100, 150, 200, 300]), sdv = Math.sqrt(p * (1 - p) / nn), tag = `${si + 1}: `;
    const ten = nn <= 0.1 * x.N, lc = nn * p >= 10 && nn * (1 - p) >= 10;
    items.push({ k: 'spm', q: tag + 'mean', a: N(p, 3), p }, { k: 'sps', q: tag + 'SD', a: N(sdv, 4), p, nn }, { k: 'sp10', q: tag + '10%', a: ten ? 'met' : 'not met', nn, N: x.N }, { k: 'splc', q: tag + 'large counts', a: lc ? 'met' : 'not met', nn, p });
    rows.push(`About ${pc(p)} of ${esc(x.pop)} ${esc(x.trait)}. Take a random sample of ${nn}.<br>Mean of p̂ ${blank(N(p, 3), 3)} SD of p̂ ${blank(N(sdv, 4), 4)} 10% condition ${blank(ten ? 'met' : 'not met', 4)} Large Counts ${blank(lc ? 'met' : 'not met', 4)}`);
  });
  return {
    title: 'Sampling Distribution of a Proportion', ican: 'I can find the mean and standard deviation of the sampling distribution of p̂ and check the conditions.',
    directions: 'The mean of p̂ is p and its SD is √(p(1 − p) ÷ n), rounded to 4 decimal places. The SD formula needs n to be at most 10% of the population. A normal model needs np ≥ 10 and n(1 − p) ≥ 10 (Large Counts). Write "met" or "not met".',
    minutes: 30, materials: 'pencil, calculator', parts: [part('Practice', fill(rows, 1))], items,
    mistakes: 'Using n instead of p in the mean, forgetting the square root, and checking Large Counts with the population size.',
    notes: 'When a condition is not met, the honest answer is that the formula or the normal model should not be used.',
  };
};

const TSTAR = { 9: [1.833, 2.262, 3.250], 11: [1.796, 2.201, 3.106], 14: [1.761, 2.145, 2.977], 15: [1.753, 2.131, 2.947], 19: [1.729, 2.093, 2.861], 24: [1.711, 2.064, 2.797], 29: [1.699, 2.045, 2.756] };
const ZSTAR = [1.645, 1.960, 2.576], CONF = [90, 95, 99];
const CIP = [
  { who: 'students at a large school', did: 'get at least 8 hours of sleep on school nights' }, { who: 'adults in a large city', did: 'own a bike' },
  { who: 'customers of a store chain', did: 'used a coupon last month' }, { who: 'seeds in a large shipment', did: 'sprouted' },
];
const CIM = [
  { what: 'the weight of bags of chips', unit: 'grams', mu: 28.5, s: [0.5, 0.9], dp: 2 }, { what: 'the hours of sleep students get on school nights', unit: 'hours', mu: 7.1, s: [0.8, 1.4], dp: 2 },
  { what: 'the time to run a mile', unit: 'minutes', mu: 9.2, s: [1.1, 1.8], dp: 2 }, { what: 'the length of trout in a lake', unit: 'cm', mu: 34, s: [3, 5], dp: 2 },
];
S.ci = c => {
  const { r, n } = c, items = [], rows = [];
  const kinds = r.shuffle(Array.from({ length: n }, (_, i) => i % 2 ? 'm' : 'p'));
  const ps = r.sample(CIP, Math.ceil(n / 2)), ms = r.sample(CIM, Math.ceil(n / 2));
  let pi = 0, mi = 0;
  kinds.forEach((kd, si) => {
    const ci = r.int(0, 2), tag = `${si + 1}: `;
    if (kd === 'p') {
      const x = ps[pi++ % ps.length], nn = r.pick([100, 125, 200, 250, 500, 1000]), cnt = r.int(Math.round(nn * 0.2), Math.round(nn * 0.8)), ph = cnt / nn;
      const se = Math.sqrt(ph * (1 - ph) / nn), me = ZSTAR[ci] * se, lo = ph - me, hi = ph + me;
      items.push({ k: 'cip', q: tag + 'p-hat', a: N(ph, 3), cnt, nn }, { k: 'cistar', q: tag + 'critical value', a: N(ZSTAR[ci], 3), conf: CONF[ci], df: null },
        { k: 'cise', q: tag + 'SE', a: N(se, 4), cnt, nn }, { k: 'ciint', q: tag + 'interval', a: `(${N(lo, 3)}, ${N(hi, 3)})`, cnt, nn, conf: CONF[ci] });
      rows.push(`In a random sample of ${nn} ${esc(x.who)}, ${cnt} ${esc(x.did)}. Build a ${CONF[ci]}% confidence interval for the proportion of all ${esc(x.who)} who ${esc(x.did)}.<br>`
        + `Conditions: ${line(20)}<br>p̂ = ${blank(N(ph, 3), 3)} z* = ${blank(N(ZSTAR[ci], 3), 3)} SE = ${blank(N(se, 4), 4)} Interval ${blank(`(${N(lo, 3)}, ${N(hi, 3)})`, 7)}<br>Interpret: ${line(26)}`
        + keyline(`Random sample stated; ${nn} is less than 10% of all ${esc(x.who)}; ${cnt} and ${nn - cnt} are both at least 10. We are ${CONF[ci]}% confident that the interval from ${N(lo, 3)} to ${N(hi, 3)} captures the true proportion of all ${esc(x.who)} who ${esc(x.did)}.`));
    } else {
      const x = ms[mi++ % ms.length], df = r.pick(Object.keys(TSTAR).map(Number)), nn = df + 1, ts = TSTAR[df][ci];
      const xb = +(x.mu + (r.next() - 0.5) * x.mu * 0.06).toFixed(x.dp), s = +(x.s[0] + r.next() * (x.s[1] - x.s[0])).toFixed(2);
      const se = s / Math.sqrt(nn), me = ts * se, lo = xb - me, hi = xb + me;
      items.push({ k: 'cistar', q: tag + 'critical value', a: N(ts, 3), conf: CONF[ci], df }, { k: 'cisem', q: tag + 'SE', a: N(se, 4), s, nn }, { k: 'cimint', q: tag + 'interval', a: `(${N(lo, 2)}, ${N(hi, 2)})`, xb, s, nn, conf: CONF[ci] });
      rows.push(`A random sample of ${nn} gives a mean of ${fmt(xb, 2)} ${esc(x.unit)} for ${esc(x.what)}, with s = ${fmt(s, 2)} ${esc(x.unit)}. The sample shows no strong skew or outliers. Build a ${CONF[ci]}% confidence interval for the population mean.<br>`
        + `Conditions: ${line(20)}<br>df = ${nn - 1}, t* = ${blank(N(ts, 3), 3)} SE = ${blank(N(se, 4), 4)} Interval ${blank(`(${N(lo, 2)}, ${N(hi, 2)})`, 7)}<br>Interpret: ${line(26)}`
        + keyline(`Random sample stated; the population is much larger than ${nn * 10}; n is under 30 but the data show no strong skew or outliers, so t methods are reasonable. We are ${CONF[ci]}% confident that the interval from ${N(lo, 2)} to ${N(hi, 2)} ${esc(x.unit)} captures the true mean ${esc(x.what)}.`));
    }
  });
  const dfs = Object.keys(TSTAR);
  const tt = ctab(['df', '90%', '95%', '99%'], dfs.map(d => [d, ...TSTAR[d].map(v => v.toFixed(3))]).concat([['z*', ...ZSTAR.map(v => v.toFixed(3))]]), 'st-narrow st-tt');
  return {
    title: 'Build a Confidence Interval', ican: 'I can construct and interpret one-proportion and one-mean confidence intervals after checking conditions.',
    directions: 'Check the conditions first (Random, 10%, Large Counts or Normal). For a proportion, SE = √(p̂(1 − p̂) ÷ n) and the interval is p̂ ± z*·SE (3 decimal places). For a mean, SE = s ÷ √n and the interval is x̄ ± t*·SE (2 decimal places). Use the table for z* and t*.',
    minutes: 40, materials: 'pencil, calculator', parts: [part('Critical values', tt), part('Intervals', fill(rows, 1))], items,
    mistakes: 'Using z* for a mean when σ is unknown, and saying "95% of the data are in the interval" or "there is a 95% chance the true value is in this interval".',
    notes: 'Round the SE only for writing it down; use the unrounded SE for the margin of error.',
  };
};

const CHI = [
  { h: 'grade level and favorite kind of music', rows: ['Grade 9', 'Grade 12'], cols: ['Pop', 'Hip-hop', 'Country'] },
  { h: 'type of school and how students get there', rows: ['City school', 'Rural school'], cols: ['Bus', 'Car', 'Walk or bike'] },
  { h: 'sport participation and favorite snack', rows: ['Athletes', 'Non-athletes'], cols: ['Fruit', 'Chips', 'Granola bar'] },
  { h: 'time of day and the drink people order', rows: ['Morning', 'Afternoon'], cols: ['Coffee', 'Tea', 'Juice'] },
];
const CRIT = { 1: 3.841, 2: 5.991, 3: 7.815, 4: 9.488, 5: 11.070 };
S.chisq = c => {
  const { r, n } = c, items = [], blocks = [];
  r.sample(CHI, n).forEach((x, si) => {
    const assoc = r.chance(0.5);
    let m, chi, E;
    for (let t = 0; t < 500; t++) {
      const base = split(r, 30, 3).map(v => v / 30), R = [r.int(40, 90), r.int(40, 90)];
      m = R.map((tot, i) => { const sh = assoc && i ? r.shuffle(base) : base; const a = Math.round(tot * sh[0] + r.int(-3, 3)), b = Math.round(tot * sh[1] + r.int(-3, 3)); return [a, b, tot - a - b]; });
      if (m.flat().some(v => v < 4)) continue;
      const { E: e, chi: ch } = chiOf(m); E = e; chi = ch;
      if (E.flat().some(v => v < 5) || Math.abs(chi - CRIT[2]) < 0.8) continue;
      break;
    }
    const L = LET[si], tag = `Table ${L}: `, rej = chi > CRIT[2];
    E.forEach((row, i) => row.forEach((v, j) => items.push({ k: 'chie', q: `${tag}expected ${x.rows[i]} ${x.cols[j]}`, a: N(v, 2), m, i, j })));
    items.push({ k: 'chi', q: tag + 'chi-square', a: N(chi, 2), m }, { k: 'chidf', q: tag + 'df', a: '2', m }, { k: 'chicrit', q: tag + 'critical', a: N(CRIT[2], 3), df: 2 }, { k: 'chidec', q: tag + 'decision', a: rej ? 'reject H0' : 'fail to reject H0', m });
    const tot = m.map(row => sum(row)), ctot = [0, 1, 2].map(j => m[0][j] + m[1][j]);
    blocks.push(`<div class="st-set"><p><b>${L}.</b> A random sample of students was asked about ${esc(x.h)}.</p>`
      + ctab(['Observed', ...x.cols.map(esc), 'Total'], m.map((row, i) => [`<b>${esc(x.rows[i])}</b>`, ...row.map(String), String(tot[i])]).concat([['<b>Total</b>', ...ctot.map(String), String(sum(tot))]]))
      + ctab(['Expected', ...x.cols.map(esc)], E.map((row, i) => [`<b>${esc(x.rows[i])}</b>`, ...row.map(v => blank(N(v, 2), 3))]))
      + `<p class="st-ans4">H0: there is no association between ${esc(x.h)}. χ² = ${blank(N(chi, 2), 3.5)} df = ${blank('2', 2)} Critical value (α = 0.05) = ${blank(N(CRIT[2], 3), 3)} Decision: ${blank(rej ? 'reject H0' : 'fail to reject H0', 8)}</p>`
      + `<p>Conclusion in context: ${line(26)}</p>${keyline(rej ? `Because χ² = ${N(chi, 2)} is greater than ${CRIT[2]}, we reject H0: there is convincing evidence of an association between ${esc(x.h)} among students like these.` : `Because χ² = ${N(chi, 2)} is less than ${CRIT[2]}, we fail to reject H0: there is not convincing evidence of an association between ${esc(x.h)}.`)}</div>`);
  });
  return {
    title: 'Chi-Square Test of Independence', ican: 'I can run a chi-square test of independence on a two-way table and state the conclusion in context.',
    directions: 'Expected count = (row total × column total) ÷ grand total, to 2 decimal places. Check that every expected count is at least 5. Then χ² = Σ (observed − expected)² ÷ expected, df = (rows − 1)(columns − 1). Compare χ² to the critical value at α = 0.05.',
    minutes: 40, materials: 'pencil, calculator', parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Using rows × columns for df, dividing by the observed count instead of the expected count, and concluding "H0 is true" when we fail to reject.',
    notes: 'Critical values for α = 0.05: df 1: 3.841, df 2: 5.991, df 3: 7.815. With software, the P-value leads to the same decision.',
  };
};
function chiOf(m) {
  const R = m.map(row => sum(row)), C = m[0].map((_, j) => sum(m.map(row => row[j]))), T0 = sum(R);
  const E = m.map((row, i) => row.map((_, j) => R[i] * C[j] / T0));
  return { E, chi: sum(m.flatMap((row, i) => row.map((o, j) => (o - E[i][j]) ** 2 / E[i][j]))) };
}

const GOF = [[20, 20, 20, 20, 10, 10], [13, 20, 14, 16, 24, 13], [25, 15, 15, 15, 15, 15], [30, 20, 15, 15, 10, 10]];
const GCOL = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Brown'];
S.gof = c => {
  const { r, v } = c, claim = r.pick(GOF), nn = r.pick([60, 80, 100, 120, 150]), off = r.chance(0.5);
  let obs, chi, E;
  for (let t = 0; t < 500; t++) {
    const w = claim.map(p => Math.max(1, p + (off ? r.int(-9, 9) : r.int(-2, 2))));
    const raw = w.map(x => x * nn / sum(w)); obs = raw.map(Math.floor); let left = nn - sum(obs);
    while (left > 0) { obs[r.int(0, 5)]++; left--; }
    E = claim.map(p => p * nn / 100); chi = sum(obs.map((o, i) => (o - E[i]) ** 2 / E[i]));
    if (E.every(e => e >= 5) && Math.abs(chi - CRIT[5]) > 1) break;
  }
  const rej = chi > CRIT[5], items = [];
  GCOL.forEach((cl, i) => items.push({ k: 'gofe', q: `Expected ${cl}`, a: N(E[i], 2), nn, p: claim[i] }, { k: 'gofc', q: `Contribution ${cl}`, a: N((obs[i] - E[i]) ** 2 / E[i], 3), o: obs[i], nn, p: claim[i] }));
  items.push({ k: 'gofchi', q: 'chi-square', a: N(chi, 2), obs, claim }, { k: 'chidf', q: 'df', a: '5', m: null }, { k: 'chicrit', q: 'critical', a: N(CRIT[5], 3), df: 5 }, { k: 'gofdec', q: 'decision', a: rej ? 'reject H0' : 'fail to reject H0', obs, claim });
  const worked = ctab(['Color', 'Claimed %', 'Observed', 'Expected', '(O − E)² ÷ E'], GCOL.map((cl, i) => [cl, claim[i] + '%', String(obs[i]), blank(N(E[i], 2), 3), blank(N((obs[i] - E[i]) ** 2 / E[i], 3), 3)]).concat([['<b>Total</b>', '100%', String(nn), String(nn), blank(N(chi, 2), 3)]]));
  const parts = [part('A class bag', `<p>The company claims its candies come in these percents. A class opened a bag of ${nn} and counted the colors.</p>${worked}`
    + `<p class="st-ans4">χ² = ${blank(N(chi, 2), 3.5)} df = ${blank('5', 2)} Critical value (α = 0.05) = ${blank(N(CRIT[5], 3), 3)} Decision: ${blank(rej ? 'reject H0' : 'fail to reject H0', 8)}</p><p>Conclusion: ${line(26)}</p>`
    + keyline(rej ? `χ² = ${N(chi, 2)} > 11.070, so we reject H0: convincing evidence the colors do not match the claimed percents.` : `χ² = ${N(chi, 2)} < 11.070, so we fail to reject H0: not convincing evidence that the colors differ from the claim.`))];
  if (v.count !== 's') parts.push(part('Your own bag', `<p>Count the colors in your bag, then run the same test. n = ${line(4)}</p>` + ctab(['Color', 'Claimed %', 'Observed', 'Expected', '(O − E)² ÷ E'], GCOL.map((cl, i) => [cl, claim[i] + '%', '', '', '']).concat([['<b>Total</b>', '100%', '', '', '']])) + `<p>χ² = ${line(5)} Decision and conclusion: ${line(22)}</p>`));
  return {
    title: 'Candy Color Goodness of Fit', ican: 'I can use a chi-square goodness-of-fit test to check a claimed distribution.',
    directions: 'H0: the colors follow the claimed percents. Expected = n × claimed percent (2 decimal places); each must be at least 5. Add the contributions (O − E)² ÷ E to get χ², with df = number of colors − 1. Compare to the critical value.',
    minutes: 40, materials: 'pencil, calculator, a bag of mixed candies (optional)', parts, items,
    mistakes: 'Using percents instead of counts for O and E, and using the number of candies for df.',
    notes: 'The claimed percents are invented for practice. Critical value for df = 5 at α = 0.05 is 11.070. Bags smaller than 50 can have expected counts under 5; combine colors if so.',
  };
};

// classifier metrics
const CF = {
  5: { pos: 'Junk', neg: 'Not junk', thing: 'message', model: 'A junk mail sorter' },
  6: { pos: 'Cat', neg: 'Dog', thing: 'photo', model: 'A pet photo sorter' },
  7: { pos: 'Sick', neg: 'Healthy', thing: 'leaf', model: 'A leaf disease model' },
};
const GRP = [
  { model: 'A voice assistant', did: 'understood the request', groups: ['Ages 8 to 12', 'Ages 13 to 18', 'Adults'] },
  { model: 'A photo app that finds faces', did: 'found the face', groups: ['Bright light', 'Dim light', 'Night'] },
  { model: 'A handwriting reader', did: 'read the word', groups: ['Printed', 'Cursive', 'Mixed'] },
  { model: 'A plant ID app', did: 'named the plant', groups: ['Leaf photos', 'Flower photos', 'Bark photos'] },
];
S.confusion = c => {
  const { r, n, G } = c;
  if (G <= 7) {
    const x = CF[G], items = [];
    let rows;
    for (let t = 0; t < 200; t++) {
      const errs = G === 6 ? [r.int(3, 5), r.int(0, 1)] : [r.int(1, Math.round(n * 0.15)), r.int(1, Math.round(n * 0.15))];
      const posN = r.int(Math.round(n * 0.35), Math.round(n * 0.6));
      const truth = r.shuffle(Array(posN).fill(x.pos).concat(Array(n - posN).fill(x.neg)));
      const said = truth.slice(); let e0 = errs[0], e1 = errs[1];
      if (G === 6) [e0, e1] = r.chance(0.5) ? [errs[0], errs[1]] : [errs[1], errs[0]];
      truth.forEach((tv, i) => { if (tv === x.pos && e0 > 0) { said[i] = x.neg; e0--; } });
      truth.forEach((tv, i) => { if (tv === x.neg && e1 > 0) { said[i] = x.pos; e1--; } });
      if (e0 || e1) continue;
      const order = r.shuffle(truth.map((tv, i) => i)); rows = order.map(i => [said[i], truth[i]]); break;
    }
    rows.forEach(([s, t], i) => items.push({ k: 'right', q: `${x.thing} ${i + 1}`, a: s === t ? 'yes' : 'no', s, t }));
    const tp = rows.filter(([s, t]) => s === x.pos && t === x.pos).length, fp = rows.filter(([s, t]) => s === x.pos && t === x.neg).length;
    const fn = rows.filter(([s, t]) => s === x.neg && t === x.pos).length, tn = rows.filter(([s, t]) => s === x.neg && t === x.neg).length;
    const right = tp + tn;
    [['tp', tp], ['fp', fp], ['fn', fn], ['tn', tn]].forEach(([id, v]) => items.push({ k: 'cm', id, q: `box ${id}`, a: String(v), rows, pos: x.pos }));
    items.push({ k: 'cmright', q: 'right in all', a: String(right), rows }, { k: 'acc', q: 'accuracy', a: pc(right / n), rows });
    if (G === 5) items.push({ k: 'accfr', q: 'accuracy fraction', a: fr(right, n), rows });
    const half = Math.ceil(n / 2), cell = (i) => i < n ? [String(i + 1), esc(rows[i][0]), esc(rows[i][1]), blank(rows[i][0] === rows[i][1] ? 'yes' : 'no', 2.4)] : ['', '', '', ''];
    const list2 = ctab(['#', 'Said', 'Really', 'Right?', '#', 'Said', 'Really', 'Right?'], Array.from({ length: half }, (_, i) => cell(i).concat(cell(i + half))), 'st-pred');
    const box = ctab(['', `Really ${esc(x.pos.toLowerCase())}`, `Really ${esc(x.neg.toLowerCase())}`], [[`<b>Said ${esc(x.pos.toLowerCase())}</b>`, blank(tp, 2.5), blank(fp, 2.5)], [`<b>Said ${esc(x.neg.toLowerCase())}</b>`, blank(fn, 2.5), blank(tn, 2.5)]], 'st-narrow');
    const moreErr = fn > fp ? `${x.pos.toLowerCase()} ${x.thing}s called ${x.neg.toLowerCase()} (${fn} times, compared to ${fp})` : fp > fn ? `${x.neg.toLowerCase()} ${x.thing}s called ${x.pos.toLowerCase()} (${fp} times, compared to ${fn})` : `both kinds equally (${fp} each)`;
    const after = G === 5 ? `<p class="st-ans4">Right ${blank(right, 2.5)} out of ${n}. Accuracy = ${blank(fr(right, n), 3)} = ${blank(pc(right / n), 3)}</p>`
      : G === 6 ? `<p class="st-ans4">Right ${blank(right, 2.5)} out of ${n}. Accuracy = ${blank(pc(right / n), 3)} (nearest whole percent)</p><p>Which mistake happened more often? ${line(20)}</p>${keyline('The model mixed up ' + esc(moreErr) + '.')}`
        : `<p class="st-ans4">Accuracy = ${blank(pc(right / n), 3)} (nearest whole percent)</p><p>What is a false positive here, and how many were there? ${line(18)}</p>${keyline(`A false positive is a ${esc(x.neg.toLowerCase())} ${x.thing} the model called ${esc(x.pos.toLowerCase())}: ${fp}. A false negative is a ${esc(x.pos.toLowerCase())} ${x.thing} called ${esc(x.neg.toLowerCase())}: ${fn}. A false negative means a sick plant goes untreated.`)}<p>Which mistake would worry a farmer more, and why? ${line(18)}</p>`;
    return {
      title: G === 5 ? 'Right and Wrong Box' : G === 6 ? 'Count the Accuracy' : 'Confusion Matrix: Leaf Disease',
      ican: G === 5 ? 'I can sort a computer\'s guesses into right and wrong and find its accuracy.' : G === 6 ? 'I can compare a model\'s predictions to the true labels and find its accuracy.' : 'I can fill in a confusion matrix and explain false positives and false negatives.',
      directions: `${x.model} made ${n} predictions. For each ${x.thing}, compare what the model said to what it really was, and mark it right (yes) or wrong (no). Then fill in the ${G === 7 ? 'confusion matrix' : 'box'} and find the accuracy.`,
      minutes: 30, parts: [part('The predictions', list2), part(G === 7 ? 'Confusion matrix' : 'Right and wrong box', box + after)], items,
      mistakes: 'Putting a count in the wrong box: the row is what the model said, the column is what it really was.',
      notes: 'Accuracy = right predictions ÷ all predictions. The four boxes must add to ' + n + '.',
    };
  }
  const items = [], blocks = [];
  if (G === 8) {
    r.sample(GRP, n).forEach((x, si) => {
      const L = LET[si], tag = `Table ${L}: `;
      let tots, cor;
      for (let t = 0; t < 400; t++) {
        const acc = x.groups.map(() => r.int(55, 97)); tots = x.groups.map(() => r.pick([20, 25, 50, 100])); cor = acc.map((a, i) => Math.round(a * tots[i] / 100));
        const pr = cor.map((k, i) => Math.round(100 * k / tots[i]));
        if (new Set(pr).size === 3 && Math.max(...pr) - Math.min(...pr) >= 8) break;
      }
      const pcts = cor.map((k, i) => k / tots[i]), best = pcts.indexOf(Math.max(...pcts)), worst = pcts.indexOf(Math.min(...pcts));
      x.groups.forEach((g, i) => items.push({ k: 'gacc', q: `${tag}${g}`, a: pc(pcts[i]), cor: cor[i], tot: tots[i] }));
      const gap = Math.round(100 * pcts[best]) - Math.round(100 * pcts[worst]);
      items.push({ k: 'gbest', q: tag + 'best', a: x.groups[best], cor, tots, groups: x.groups }, { k: 'ggap', q: tag + 'gap', a: String(gap), cor, tots });
      blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.model)}</b> was tested on three groups. "Correct" means it ${esc(x.did)}.</p>`
        + ctab(['Group', 'Correct', 'Wrong', 'Accuracy'], x.groups.map((g, i) => [esc(g), String(cor[i]), String(tots[i] - cor[i]), blank(pc(pcts[i]), 3)]))
        + `<p class="st-ans4">Most accurate group: ${blank(x.groups[best], 6)} Gap between the best and worst: ${blank(gap, 2.5)} percentage points</p><p>Describe the gap and one possible cause: ${line(20)}</p>`
        + keyline(`The model works best for ${esc(x.groups[best].toLowerCase())} and worst for ${esc(x.groups[worst].toLowerCase())}. A likely cause is training data with fewer examples like the weaker group.`) + '</div>');
    });
    return {
      title: 'Bias Audit: Accuracy by Group', ican: 'I can compute a model\'s accuracy for different groups and describe a gap.',
      directions: 'Accuracy = correct ÷ (correct + wrong), as a percent. Find each group\'s accuracy, the most accurate group and the gap in percentage points.',
      minutes: 25, parts: [part('Practice', blocks.join(''))], items,
      mistakes: 'Comparing the number correct instead of the percent: a group tested 100 times will have more correct answers than a group tested 20 times.',
      notes: 'A model can have high overall accuracy and still work much worse for one group. That is what a bias audit looks for.',
    };
  }
  if (G === 10) {
    const goals = r.shuffle([['The school most wants to avoid real emails being sent to the spam folder.', 'precision'], ['The school most wants to catch as much spam as possible.', 'recall']]);
    goals.slice(0, n).forEach(([goal, metric], si) => {
      let f;
      for (let t = 0; t < 500; t++) {
        f = [0, 1, 2].map(() => { const spam = r.int(60, 120), tp = r.int(Math.round(spam * 0.6), spam - 2), fp = r.int(1, 30); return { tp, fp, fn: spam - tp, tn: r.int(200, 400) }; });
        const P = f.map(m => Math.round(100 * m.tp / (m.tp + m.fp))), R = f.map(m => Math.round(100 * m.tp / (m.tp + m.fn)));
        const bp = P.indexOf(Math.max(...P)), br = R.indexOf(Math.max(...R));
        if (bp !== br && srt(P)[2] - srt(P)[1] >= 3 && srt(R)[2] - srt(R)[1] >= 3) break;
      }
      const tag = `Round ${si + 1}: `, P = f.map(m => m.tp / (m.tp + m.fp)), R = f.map(m => m.tp / (m.tp + m.fn));
      f.forEach((m, i) => items.push({ k: 'prec', q: `${tag}Filter ${LET[i]} precision`, a: pc(P[i]), m }, { k: 'rec', q: `${tag}Filter ${LET[i]} recall`, a: pc(R[i]), m }));
      const vals2 = metric === 'precision' ? P : R, best = vals2.indexOf(Math.max(...vals2));
      items.push({ k: 'prbest', q: tag + 'best', a: `Filter ${LET[best]}`, f, metric });
      blocks.push(`<div class="st-set"><p><b>Round ${si + 1}.</b> Three spam filters were tested on the same emails.</p>`
        + ctab(['Filter', 'Spam caught (TP)', 'Real email sent to spam (FP)', 'Spam missed (FN)', 'Real email delivered (TN)', 'Precision', 'Recall'], f.map((m, i) => [`Filter ${LET[i]}`, String(m.tp), String(m.fp), String(m.fn), String(m.tn), blank(pc(P[i]), 3), blank(pc(R[i]), 3)]))
        + `<p>${esc(goal)} Which filter should it pick? ${blank(`Filter ${LET[best]}`, 4)} Why? ${line(16)}</p>${keyline(`Filter ${LET[best]} has the highest ${metric}: ${metric === 'precision' ? 'when it says spam, it is most often right, so the fewest real emails are lost' : 'it catches the largest share of the spam'}.`)}</div>`);
    });
    return {
      title: 'Precision and Recall', ican: 'I can compute precision and recall from test results and choose a model for a goal.',
      directions: 'Precision = TP ÷ (TP + FP): of the emails called spam, the share that really were. Recall = TP ÷ (TP + FN): of the real spam, the share that was caught. Round to the nearest whole percent.',
      minutes: 30, materials: 'pencil, calculator', parts: [part('Practice', blocks.join(''))], items,
      mistakes: 'Swapping FP and FN in the formulas, and judging the filters by accuracy when the spam is a small part of all email.',
      notes: 'The best filter depends on the goal: no filter wins on both measures here.',
    };
  }
  // grade 12: false positive rates across groups
  const FPR = [{ model: 'A model that flags bank transactions as possible fraud', groups: ['North region', 'Central region', 'South region'], pos: 'fraud' },
    { model: 'A model that flags essays for possible copying', groups: ['School A', 'School B', 'School C'], pos: 'copied' },
    { model: 'A model that flags job applications for a second look', groups: ['Group 1', 'Group 2', 'Group 3'], pos: 'a strong match' }];
  r.sample(FPR, n).forEach((x, si) => {
    const fair = r.chance(0.5);
    let f;
    for (let t = 0; t < 500; t++) {
      const base = r.int(4, 12);
      f = x.groups.map(() => { const neg = r.pick([100, 200, 400]), rate = fair ? base + r.int(-1, 1) : base + r.int(-1, 14), fp = Math.round(neg * rate / 100), pos = r.int(20, 60), tp = r.int(Math.round(pos * 0.6), pos - 1); return { tp, fn: pos - tp, fp, tn: neg - fp }; });
      const R = f.map(m => 100 * m.fp / (m.fp + m.tn)), gap = Math.max(...R) - Math.min(...R);
      if (f.every(m => m.fp > 0) && (fair ? gap <= 3 : gap >= 8)) break;
    }
    const L = LET[si], tag = `Table ${L}: `, R = f.map(m => m.fp / (m.fp + m.tn)), gap = 100 * (Math.max(...R) - Math.min(...R)), ok = gap <= 5;
    f.forEach((m, i) => items.push({ k: 'fpr', q: `${tag}${x.groups[i]}`, a: pc(R[i], 1), m }));
    items.push({ k: 'fprfair', q: tag + 'fair', a: ok ? 'yes' : 'no', f });
    blocks.push(`<div class="st-set"><p><b>${L}. ${esc(x.model)}.</b> A positive means the model says "${esc(x.pos)}".</p>`
      + ctab(['Group', 'TP', 'FP', 'FN', 'TN', 'False positive rate'], f.map((m, i) => [esc(x.groups[i]), String(m.tp), String(m.fp), String(m.fn), String(m.tn), blank(pc(R[i], 1), 3.5)]))
      + `<p>Using "equal false positive rates (within 5 points)" as the test, is the model fair across the groups? ${blank(ok ? 'yes' : 'no', 3)} Explain: ${line(16)}</p>`
      + keyline(ok ? `Yes: the rates are within ${N(gap, 1)} points of each other.` : `No: the rates differ by ${N(gap, 1)} points, so innocent members of one group are flagged far more often.`) + '</div>');
  });
  return {
    title: 'Fairness Metrics Across Groups', ican: 'I can compute false positive rates for groups and judge a model against a fairness test.',
    directions: 'False positive rate = FP ÷ (FP + TN): the share of true negatives the model wrongly flags. Round to the nearest tenth of a percent, then compare the groups.',
    minutes: 30, materials: 'pencil, calculator', parts: [part('Practice', blocks.join(''))], items,
    mistakes: 'Dividing FP by all the cases, or by all the positives, instead of by the true negatives (FP + TN).',
    notes: 'Equal false positive rates is one definition of fair; equal accuracy and equal positive rates are others, and they can disagree. The 5-point line is a classroom rule, not a legal standard.',
  };
};

/* ---------- independent checks for verify ---------- */
const pv = s => { s = String(s).replace(/,/g, '').replace(/−/g, '-').replace(/[$%]/g, '').trim(); const m = s.match(/^(-?\d+)\/(\d+)$/); if (m) return +m[1] / +m[2]; const mm = s.match(/^(\d+) (\d+)\/(\d+)$/); return mm ? +mm[1] + mm[2] / mm[3] : parseFloat(s); };
const V = {
  mean: a => a.reduce((m, x, i) => m + (x - m) / (i + 1), 0),   // a running mean
  median: a => { const s = a.slice().sort((x, y) => y - x), n = s.length; return (s[Math.floor((n - 1) / 2)] + s[Math.ceil((n - 1) / 2)]) / 2; },
  quart: a => { const s = a.slice().sort((x, y) => x - y), n = s.length; return [s[0], V.median(s.filter((_, i) => i < Math.floor(n / 2))), V.median(s), V.median(s.filter((_, i) => i >= Math.ceil(n / 2))), s[n - 1]]; },
  count: (a, x) => a.filter(y => y === x).length,
  lowest: s => { const m = String(s).match(/(\d+)\/(\d+)$/); return !m || gcd(+m[1], +m[2]) === 1; },
  outs: a => { const q = V.quart(a), i = q[3] - q[1]; return a.filter(x => x < q[1] - 1.5 * i || x > q[3] + 1.5 * i).sort((x, y) => x - y); },
  // the normal CDF from an erf approximation (Abramowitz and Stegun 7.1.26)
  phi: z => { const t = 1 / (1 + 0.3275911 * Math.abs(z) / Math.SQRT2), y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-z * z / 2); return z >= 0 ? (1 + y) / 2 : (1 - y) / 2; },
  lgam: x => { const g = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5]; let y = x, tmp = x + 5.5; tmp -= (x + 0.5) * Math.log(tmp); let s = 1.000000000190015; for (const c of g) s += c / ++y; return -tmp + Math.log(2.5066282746310005 * s / x); },
  // chi-square CDF from the series for the lower incomplete gamma
  chiCdf: (x, k) => { const a = k / 2, xx = x / 2; let s = 1 / a, t = 1 / a; for (let i = 1; i < 300; i++) { t *= xx / (a + i); s += t; } return s * Math.exp(-xx + a * Math.log(xx) - V.lgam(a)); },
  // the t CDF by Simpson's rule on the density
  tCdf: (t, df) => { const c = Math.exp(V.lgam((df + 1) / 2) - V.lgam(df / 2)) / Math.sqrt(df * Math.PI), f = u => c * (1 + u * u / df) ** (-(df + 1) / 2); const m = 400, h = t / m; let s = f(0) + f(t); for (let i = 1; i < m; i++) s += f(i * h) * (i % 2 ? 4 : 2); return 0.5 + s * h / 3; },
};
const close = (got, want, dp) => Math.abs(pv(got) - want) <= 0.5 * 10 ** -dp + 1e-7;
const dpOf = s => { const m = String(s).replace(/[%$]/g, '').match(/\.(\d+)/); return m ? m[1].length : 0; };

Gen.add('statistics', {
  title: 'Statistics and Probability', type: 'Practice',
  css: `.st-vals{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 8px}
.st-v{display:inline-block;min-width:2.2em;padding:2px 7px;border:1px solid #888;border-radius:4px;text-align:center}
.show-key .st-odd{outline:2.5px solid #b03020;outline-offset:3px;border-radius:50%}
.st-set{break-inside:avoid;margin:0 0 12px}
.st-set p{margin:3px 0}
.st-row{display:flex;gap:16px;align-items:center;break-inside:avoid;margin-bottom:8px}
.st-row>svg{flex:0 0 auto;width:3.1in;margin:0}
.st-line{display:inline-block;border-bottom:1px solid #555;height:1.1em;vertical-align:baseline}
.st-cap{margin:4px 0;font-size:14px}
.st-ans4 .ws-blank{margin-right:10px}
.ws-table.st-tbl td,.ws-table.st-tbl th{padding:2px 6px;height:0.27in}
.ws-table.st-narrow{width:auto;min-width:50%}
.ws-table.st-raw td{padding:1px 6px;height:auto;font-size:13px}
.ws-table.st-own td{height:0.42in}
.ws-table.st-grid td{height:0.5in}
.ws-table.st-pred td,.ws-table.st-pred th{padding:1px 5px;height:0.24in;font-size:13px}
.ws-table.st-tt td{height:auto;padding:1px 8px}
.ws-table.st-k td{width:33%;vertical-align:top;font-weight:700}
.ws-table.st-k td.st-kdraw{height:1.5in}
.ws-table.st-k td.st-ktally{height:1in}
.st-tal{vertical-align:middle}
.st-names{columns:2;column-gap:24px;margin:4px 0 8px;padding-left:2em}
.st-names li{margin:0 0 8px}
.st-sent li{margin:0 0 14px}
.st-pick{list-style:none;padding-left:0}
.st-pick li{margin:4px 0}
.st-box{display:inline-block;width:0.9em;height:0.9em;border:1.5px solid #222;vertical-align:-2px;margin-right:6px}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '6' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => SKILLS[v.grade] || SKILLS[6], def: 'center' },
    { id: 'count', label: 'Length', type: 'select', options: countOpts, def: 'm', show: v => skillOf(v) !== 'survey' },
    { id: 'from', label: 'Start from', type: 'select', options: [['list', 'A list of raw answers to tally'], ['tally', 'A finished tally chart']], def: 'list', show: v => skillOf(v) === 'tally' },
    { id: 'ctx', label: 'Data', type: 'select', options: [['auto', 'Mixed contexts'], ['iq', 'Start with IQ scores (mean 100, SD 15)']], def: 'auto', show: v => skillOf(v) === 'normal' },
    { id: 'topic', label: 'Survey question (leave blank for students to write their own)', type: 'text', def: '', show: v => skillOf(v) === 'survey' },
    { id: 'choices', label: 'Answer choices or items, comma separated: Apple, Banana, Grapes, Other', type: 'text', def: '', show: v => skillOf(v) === 'survey' },
    { id: 'form', label: 'Survey form', type: 'select', options: [['one', 'One question, one answer each'], ['grid', 'Several items rated on a scale (like how often)']], def: 'one', show: v => skillOf(v) === 'survey' && v.grade !== 'k' },
    { id: 'scale', label: 'Scale answers, comma separated: Often, Sometimes, Never (blank uses the language default)', type: 'text', def: '', show: v => skillOf(v) === 'survey' && v.form === 'grid' && v.grade !== 'k' },
    { id: 'people', label: 'Classmates to ask', type: 'select', options: [['10', '10'], ['20', '20'], ['30', '30']], def: '10', show: v => skillOf(v) === 'survey' && v.grade !== 'k' },
    { id: 'lang', label: 'Survey language (headings and sentence frames)', type: 'select', options: LANGS, def: 'en', show: v => skillOf(v) === 'survey' },
  ],
  make(v, r) {
    const g = v.grade, skill = skillOf(v), G = g === 'k' ? 0 : +g, [cn] = CN(skill, g);
    const n = cn[{ s: 0, m: 1, l: 2 }[v.count] ?? 1] ?? cn[1];
    const s = S[skill]({ v, r, g, G, n });
    const gradeName = GRADES.find(x => x[0] === g)[1];
    s.level = gradeName;
    s.title = s.title || 'Statistics';
    return s;
  },
  verify(s, v) {
    const out = [], bad = (it, want) => out.push(`${it.q}: key says ${it.a}, should be ${want}`);
    const num = (it, want, dp) => { if (!close(it.a, want, dp)) bad(it, fmt(want, dp)); };
    for (const it of s.items) {
      const a = String(it.a);
      if (/\d+\/\d+/.test(a) && !V.lowest(a)) out.push(`${it.q}: ${a} is not in simplest form`);
      switch (it.k) {
        case 'cq': {
          const c = it.counts, tot = c.reduce((x, y) => x + y, 0), mx = Math.max(...c), mn = Math.min(...c);
          if (it.kind === 'read') num(it, c[it.i], 0);
          else if (it.kind === 'most') { if (it.cats[c.indexOf(mx)] !== a || c.filter(x => x === mx).length > 1) bad(it, 'a unique most'); }
          else if (it.kind === 'least') { if (it.cats[c.indexOf(mn)] !== a || c.filter(x => x === mn).length > 1) bad(it, 'a unique least'); }
          else if (it.kind === 'total') num(it, tot, 0);
          else if (it.kind === 'more') { num(it, c[it.i] - c[it.j], 0); if (c[it.i] <= c[it.j]) out.push(`${it.q}: not more`); }
          else if (it.kind === 'or') num(it, c[it.i] + c[it.j], 0);
          else if (it.kind === 'not') num(it, tot - c[it.i], 0);
          else if (it.kind === 'pct') num(it, 100 * c[it.i] / tot, 1);
          break;
        }
        case 'cnt': num(it, it.raw ? it.raw.filter(x => x === it.cats[it.i]).length : it.counts[it.i], 0); break;
        case 'odd': { const d = it.data.map(x => Math.abs(x - V.median(it.data))), far = it.data[d.indexOf(Math.max(...d))]; if (+a !== far || d.filter(x => x === Math.max(...d)).length > 1) bad(it, far); break; }
        case 'typlo': case 'typhi': { const rest = it.data.slice(); rest.splice(rest.indexOf(it.o), 1); num(it, it.k === 'typlo' ? Math.min(...rest) : Math.max(...rest), 0); break; }
        case 'mean': { const w = V.mean(it.data); num(it, w, it.dp); break; }
        case 'median': num(it, V.median(it.data), 2); break;
        case 'mode': { const cs = it.data.map(x => V.count(it.data, x)), top = Math.max(...cs); const ms = [...new Set(it.data.filter((x, i) => cs[i] === top))]; if (ms.length !== 1 || +a !== ms[0] || top < 2) bad(it, ms.join(' or ')); break; }
        case 'range': num(it, it.data.reduce((m, x) => Math.max(m, x), -Infinity) - it.data.reduce((m, x) => Math.min(m, x), Infinity), 0); break;
        case 'dev': num(it, Math.abs(it.x - V.mean(it.data)), 2); break;
        case 'devsum': { const m = V.mean(it.data); num(it, it.data.reduce((t, x) => t + Math.abs(x - m), 0), 2); break; }
        case 'mad': { const m = V.mean(it.data); num(it, it.data.reduce((t, x) => t + Math.abs(x - m), 0) / it.data.length, 1); break; }
        case 'q5': num(it, V.quart(it.data)[it.j], 2); break;
        case 'iqr': { const q = V.quart(it.data); num(it, q[3] - q[1], 2); break; }
        case 'fence': { const q = V.quart(it.data), i = q[3] - q[1]; num(it, it.side ? q[3] + 1.5 * i : q[1] - 1.5 * i, 2); break; }
        case 'outs': { const o = V.outs(it.data); if (a !== (o.length ? o.join(', ') : 'none')) bad(it, o.join(', ') || 'none'); break; }
        case 'pickmax': { const mx = Math.max(...it.vals); if (it.vals.filter(x => x === mx).length !== 1 || it.names[it.vals.indexOf(mx)] !== a) bad(it, 'a unique max'); break; }
        case 'bin': num(it, it.data.filter(x => x >= it.lo && x <= it.hi).length, 0); break;
        case 'atleast': num(it, it.data.filter(x => x >= it.cut).length, 0); break;
        case 'bigbin': { const cs = it.bins.map(([lo, hi]) => it.data.filter(x => x >= lo && x <= hi).length), mx = Math.max(...cs); if (cs.filter(x => x === mx).length !== 1 || a !== `${it.bins[cs.indexOf(mx)][0]}-${it.bins[cs.indexOf(mx)][1]}`) bad(it, 'the unique biggest bin'); break; }
        case 'choose': { const o = V.outs(it.data); if (a !== (o.length ? 'median' : 'mean')) bad(it, o.length ? 'median' : 'mean'); break; }
        case 'lpcount': num(it, it.e.filter(x => x === it.v8).length, 0); break;
        case 'lpdiff': num(it, (Math.max(...it.e) - Math.min(...it.e)) / 8, 4); break;
        case 'lptot': num(it, it.e.reduce((t, x) => t + x, 0) / 8, 4); break;
        case 'lpshare': { const t = it.e.reduce((x, y) => x + y, 0); num(it, t / 80, 4); if (t % 10) out.push(`${it.q}: share is not whole eighths`); break; }
        case 'cell5': num(it, it.answers.filter(x => x === `Grade ${4 + it.i}, ${it.choices[it.j]}`).length, 0); break;
        case 'row5': num(it, it.answers.filter(x => x.startsWith(`Grade ${4 + it.i},`)).length, 0); break;
        case 'col5': num(it, it.answers.filter(x => x.endsWith(', ' + it.choice)).length, 0); break;
        case 'tot5': num(it, it.answers.length, 0); break;
        case 'cell': { const [[p, q], [r2, t]] = it.m; num(it, { a: p, b: q, c: r2, d: t, R1: p + q, R2: r2 + t, C1: p + r2, C2: q + t, T: p + q + r2 + t }[it.id], 0); break; }
        case 'rowpct': num(it, 100 * it.num / it.den, 0); break;
        case 'rel': num(it, it.num / it.den, 2); break;
        case 'assoc': { const [[p, q], [r2, t]] = it.m, d = Math.abs(p / (p + q) - r2 / (r2 + t)); if (a !== (d >= 0.1 ? 'yes' : 'no') || (d > 0.05 && d < 0.15)) bad(it, d >= 0.1 ? 'yes' : 'no'); break; }
        case 'frac': num(it, it.num / it.den, 6); break;
        case 'indep': { const [[p, q], [r2, t]] = it.m, T0 = p + q + r2 + t; if (a !== (p * T0 === (p + q) * (p + r2) ? 'yes' : 'no')) bad(it, 'the other'); break; }
        case 'venn': { const [x, y, z, w] = it.reg, T0 = x + y + z + w, pA = (x + y) / T0, pB = (y + z) / T0, pAB = y / T0; num(it, { pA, pB, pAB, pAoB: pA + pB - pAB }[it.id], 6); break; }
        case 'bag': num(it, it.red / (it.red + it.other), 6); break;
        case 'better': { const pa = it.A[0] / (it.A[0] + it.A[1]), pb = it.B[0] / (it.B[0] + it.B[1]); if (a !== (Math.abs(pa - pb) < 1e-12 ? 'same chance' : pa > pb ? 'Bag A' : 'Bag B')) bad(it, 'the other bag'); break; }
        case 'ss': case 'pev': {
          const x = EXP[it.ex]; let total = 0, good = 0;
          const walk = (i, o) => { if (i === x.st.length) { total++; if (it.k === 'pev' && x.ev[it.ei][1](o)) good++; return; } for (const y of x.st[i]) walk(i + 1, o.concat([y])); };
          walk(0, []);
          num(it, it.k === 'ss' ? total : good / total, 6); break;
        }
        case 'spin': num(it, it.num / it.den, 6); break;
        case 'spinexp': { const e = it.spins * it.num / it.den; num(it, e, 0); if (!Number.isInteger(e)) out.push(`${it.q}: expected count is not whole`); break; }
        case 'mdiff': num(it, Math.abs(V.mean(it.A) - V.mean(it.B)), 2); break;
        case 'ratio': { const md = d => { const m = V.mean(d); return d.reduce((t, x) => t + Math.abs(x - m), 0) / d.length; }; num(it, Math.abs(V.mean(it.A) - V.mean(it.B)) / Math.max(md(it.A), md(it.B)), 1); break; }
        case 'assocdir': { const f = lsrOf(it.pts); const w = f.r > 0.5 ? 'positive' : f.r < -0.5 ? 'negative' : Math.abs(f.r) < 0.3 ? 'none' : '?'; if (a !== w) bad(it, w + ' (r = ' + f.r.toFixed(2) + ')'); break; }
        case 'outpt': {
          if (!it.out) { if (a !== 'none') bad(it, 'none'); break; }
          const f = lsrOf(it.pts), res = it.pts.map(p => Math.abs(p[1] - f.a - f.b * p[0])), i = res.indexOf(Math.max(...res));
          if (it.pts[i][0] !== it.out[0] || it.pts[i][1] !== it.out[1]) bad(it, 'the point farthest from the line'); break;
        }
        case 'fiteq': { const f = lsrOf(it.pts), sp = Math.max(...it.pts.map(p => p[0])) - Math.min(...it.pts.map(p => p[0])); if (Math.abs(f.b - it.m) > Math.max(0.35 * Math.abs(it.m), 0.15) || Math.abs((f.a + f.b * f.mx) - (it.b + it.m * f.mx)) > Math.abs(it.m) * sp * 0.25 + 2) bad(it, `near y = ${f.b.toFixed(2)}x + ${f.a.toFixed(2)}`); break; }
        case 'fitpred': num(it, it.b + it.m * it.xp, 2); break;
        case 'slm': num(it, it.m, 2); break;
        case 'sldir': if (a !== (it.m > 0 ? 'increases' : 'decreases')) bad(it, 'the other direction'); break;
        case 'slamt': num(it, Math.abs(it.m), 2); break;
        case 'slb': num(it, it.b, 2); break;
        case 'slp': num(it, it.b + it.m * it.xp, 2); break;
        case 'yhat': num(it, it.b + it.m * it.x, 1); break;
        case 'resid': num(it, it.y - it.b - it.m * it.x, 1); break;
        case 'linfit': { const res = it.pts.map(p => p[1] - it.b - it.m * p[0]), xm = V.mean(it.pts.map(p => p[0])), f = lsrOf(it.pts.map((p, i) => [(p[0] - xm) ** 2, res[i]])); if (a !== (Math.abs(f.r) > 0.75 ? 'no' : 'yes')) bad(it, Math.abs(f.r) > 0.75 ? 'no' : 'yes'); break; }
        case 'z': num(it, (it.v - it.m) / it.s, 2); break;
        case 'zwho': { const za = (it.A.v - it.A.m) / it.A.s, zb = (it.B.v - it.B.m) / it.B.s, ga = it.low ? -za : za, gb = it.lowB ? -zb : zb; if (a !== (ga > gb ? it.pa : it.pb)) bad(it, ga > gb ? it.pa : it.pb); break; }
        case 'nticks': if (a !== [-3, -2, -1, 0, 1, 2, 3].map(z => fmt(it.mu + z * it.sd, 2)).join(', ')) bad(it, 'the SD marks'); break;
        case 'npct': {
          const regs = REG.slice(it.lo === -4 ? 0 : it.lo + 4, it.hi === 4 ? 8 : it.hi + 4), w = regs.reduce((t, x) => t + x, 0);
          num(it, w, 2);
          const real = 100 * ((it.hi === 4 ? 1 : V.phi(it.hi)) - (it.lo === -4 ? 0 : V.phi(it.lo)));
          if (Math.abs(real - w) > 1) out.push(`${it.q}: rule ${w} is far from the normal ${real.toFixed(2)}`); break;
        }
        case 'ncount': num(it, Math.round(1000 * (it.z > 0 ? REG.slice(it.z + 4).reduce((t, x) => t + x, 0) : REG.slice(0, it.z + 4).reduce((t, x) => t + x, 0)) / 100), 0); break;
        case 'lcell': { const xm = V.mean(it.pts.map(p => p[0])), ym = V.mean(it.pts.map(p => p[1])), dx = it.p[0] - xm, dy = it.p[1] - ym; num(it, [dx, dy, dx * dy, dx * dx, dy * dy][it.j], 2); break; }
        case 'lsum': {
          // the computational formulas: n Σxy − Σx Σy, over n
          const n = it.pts.length, sx = it.pts.reduce((t, p) => t + p[0], 0), sy = it.pts.reduce((t, p) => t + p[1], 0);
          const sxy = it.pts.reduce((t, p) => t + p[0] * p[1], 0), sxx = it.pts.reduce((t, p) => t + p[0] * p[0], 0), syy = it.pts.reduce((t, p) => t + p[1] * p[1], 0);
          num(it, [0, 0, (n * sxy - sx * sy) / n, (n * sxx - sx * sx) / n, (n * syy - sy * sy) / n][it.j], 2); break;
        }
        case 'lmean': num(it, V.mean(it.pts.map(p => p[it.j])), 2); break;
        case 'lb': case 'la': case 'lr': case 'lr2': {
          const n = it.pts.length, sx = it.pts.reduce((t, p) => t + p[0], 0), sy = it.pts.reduce((t, p) => t + p[1], 0);
          const sxy = it.pts.reduce((t, p) => t + p[0] * p[1], 0), sxx = it.pts.reduce((t, p) => t + p[0] * p[0], 0), syy = it.pts.reduce((t, p) => t + p[1] * p[1], 0);
          const b = (n * sxy - sx * sy) / (n * sxx - sx * sx), rr = (n * sxy - sx * sy) / Math.sqrt((n * sxx - sx * sx) * (n * syy - sy * sy));
          num(it, { lb: b, la: (sy - b * sx) / n, lr: rr, lr2: rr * rr }[it.k], 3); break;
        }
        case 'segp': num(it, 100 * it.num / it.col.reduce((t, x) => t + x, 0), 0); break;
        case 'segassoc': { const P = it.m.map(col => col.map(x => x / col.reduce((t, y) => t + y, 0))); const sp = Math.max(...[0, 1, 2].map(k => Math.max(...P.map(p => p[k])) - Math.min(...P.map(p => p[k])))); if (a !== (sp >= 0.1 ? 'yes' : 'no')) bad(it, sp >= 0.1 ? 'yes' : 'no'); break; }
        case 'evnet': num(it, it.o.net, 2); break;
        case 'evp': num(it, it.o.num / it.den, 6); break;
        case 'evm': { const e = it.outs.reduce((t, o) => t + o.net * o.num / it.den, 0); num(it, e, 2); break; }
        case 'evsd': { const e = it.outs.reduce((t, o) => t + o.net * o.num / it.den, 0), vv = it.outs.reduce((t, o) => t + o.net * o.net * o.num / it.den, 0) - e * e; num(it, Math.sqrt(vv), 2); break; }
        case 'evfair': { const g = it.p.reduce((t, x, i) => t + x * it.nums[i], 0) - it.cost * it.den; if (a !== (g === 0 ? 'fair' : g < 0 ? 'not fair (favors the booth)' : 'not fair (favors the player)')) bad(it, 'another verdict'); break; }
        case 'cbm': case 'cbs': {
          const p = it.p, va = p.a[1] ** 2, vb = p.b ? p.b[1] ** 2 : 0;
          const m = { sum: p.a[0] + (p.b || [0])[0], diff: p.a[0] - (p.b || [0])[0], lin: p.k * p.a[0] + p.f, nsum: p.k * p.a[0], combo: p.a[0] + 2 * (p.b || [0])[0] }[p.kind];
          const sv = { sum: va + vb, diff: va + vb, lin: p.k * p.k * va, nsum: p.k * va, combo: va + 4 * vb }[p.kind];
          num(it, it.k === 'cbm' ? m : Math.sqrt(sv), 2); break;
        }
        case 'trc': case 'trj': case 'trp': {
          // count a population of 1,000,000 down the tree instead of multiplying probabilities
          const P = 1e6, D = P * it.p, ND = P - D, tp = D * it.se, fp = ND * (1 - it.sp);
          const w = { nd: ND / P, fn: (D - tp) / D, fpr: fp / ND, tp: tp / P, fp: fp / P, pos: (tp + fp) / P, ppv: tp / (tp + fp), fdr: fp / (tp + fp) }[it.which];
          num(it, w, it.k === 'trp' ? 3 : 4); break;
        }
        case 'spm': num(it, it.p, 3); break;
        case 'sps': num(it, Math.sqrt(it.p * (1 - it.p) / it.nn), 4); break;
        case 'sp10': if (a !== (10 * it.nn <= it.N ? 'met' : 'not met')) bad(it, 'the other'); break;
        case 'splc': if (a !== (Math.min(it.nn * it.p, it.nn * (1 - it.p)) >= 10 ? 'met' : 'not met')) bad(it, 'the other'); break;
        case 'cip': num(it, it.cnt / it.nn, 3); break;
        case 'cistar': {
          const tail = (100 + it.conf) / 200;
          if (it.df == null) { if (Math.abs(V.phi(pv(a)) - tail) > 0.0006) bad(it, 'the z* for ' + it.conf + '%'); }
          else if (Math.abs(V.tCdf(pv(a), it.df) - tail) > 0.0006) bad(it, `the t* for df ${it.df}`);
          break;
        }
        case 'cise': { const p = it.cnt / it.nn; num(it, Math.sqrt(p * (1 - p) / it.nn), 4); break; }
        case 'cisem': num(it, it.s / Math.sqrt(it.nn), 4); break;
        case 'ciint': case 'cimint': {
          // the critical value found by bisection on the CDF, not from the table
          const tail = (100 + it.conf) / 200, df = it.k === 'cimint' ? it.nn - 1 : null;
          let lo = 0, hi = 5; for (let i = 0; i < 60; i++) { const mid = (lo + hi) / 2; if ((df ? V.tCdf(mid, df) : V.phi(mid)) < tail) lo = mid; else hi = mid; }
          const ctr = it.k === 'ciint' ? it.cnt / it.nn : it.xb, se = it.k === 'ciint' ? Math.sqrt(ctr * (1 - ctr) / it.nn) : it.s / Math.sqrt(it.nn), dp = it.k === 'ciint' ? 3 : 2;
          const m = a.match(/^\((.+), (.+)\)$/);
          if (!m || Math.abs(pv(m[1]) - (ctr - lo * se)) > 1.5 * 10 ** -dp || Math.abs(pv(m[2]) - (ctr + lo * se)) > 1.5 * 10 ** -dp) bad(it, `(${(ctr - lo * se).toFixed(dp)}, ${(ctr + lo * se).toFixed(dp)})`);
          break;
        }
        case 'chie': { const R = it.m[it.i].reduce((t, x) => t + x, 0), C = it.m.reduce((t, row) => t + row[it.j], 0), T0 = it.m.flat().reduce((t, x) => t + x, 0); num(it, R * C / T0, 2); break; }
        case 'chi': { let t = 0; const T0 = it.m.flat().reduce((x, y) => x + y, 0); it.m.forEach((row, i) => row.forEach((o, j) => { const e = row.reduce((x, y) => x + y, 0) * it.m.reduce((x, rw) => x + rw[j], 0) / T0; t += o * o / e; })); num(it, t - T0, 2); break; }
        case 'chidf': if (it.m && a !== String((it.m.length - 1) * (it.m[0].length - 1))) bad(it, 'another df'); break;
        case 'chicrit': if (Math.abs(V.chiCdf(pv(a), it.df) - 0.95) > 0.0005) bad(it, 'the 0.95 quantile'); break;
        case 'chidec': { const { chi } = chiOf(it.m); if (a !== (chi > CRIT[2] ? 'reject H0' : 'fail to reject H0')) bad(it, 'the other decision'); break; }
        case 'gofe': num(it, it.nn * it.p / 100, 2); break;
        case 'gofc': { const e = it.nn * it.p / 100; num(it, (it.o - e) ** 2 / e, 3); break; }
        case 'gofchi': { const n0 = it.obs.reduce((t, x) => t + x, 0); num(it, it.obs.reduce((t, o, i) => t + o * o / (n0 * it.claim[i] / 100), 0) - n0, 2); break; }
        case 'gofdec': { const n0 = it.obs.reduce((t, x) => t + x, 0), ch = it.obs.reduce((t, o, i) => t + o * o / (n0 * it.claim[i] / 100), 0) - n0; if (a !== (1 - V.chiCdf(ch, 5) < 0.05 ? 'reject H0' : 'fail to reject H0')) bad(it, 'the other decision'); break; }
        case 'right': if (a !== (it.s === it.t ? 'yes' : 'no')) bad(it, 'the other'); break;
        case 'cm': { const pos = it.pos; num(it, it.rows.filter(([s2, t]) => ({ tp: s2 === pos && t === pos, fp: s2 === pos && t !== pos, fn: s2 !== pos && t === pos, tn: s2 !== pos && t !== pos })[it.id]).length, 0); break; }
        case 'cmright': num(it, it.rows.filter(([s2, t]) => s2 === t).length, 0); break;
        case 'acc': num(it, 100 * it.rows.filter(([s2, t]) => s2 === t).length / it.rows.length, 0); break;
        case 'accfr': num(it, it.rows.filter(([s2, t]) => s2 === t).length / it.rows.length, 6); break;
        case 'gacc': num(it, 100 * it.cor / it.tot, 0); break;
        case 'gbest': { const P = it.cor.map((k, i) => k / it.tots[i]), mx = Math.max(...P); if (P.filter(x => x === mx).length !== 1 || it.groups[P.indexOf(mx)] !== a) bad(it, 'a unique best'); break; }
        case 'ggap': { const P = it.cor.map((k, i) => Math.round(100 * k / it.tots[i])); num(it, Math.max(...P) - Math.min(...P), 0); break; }
        case 'prec': num(it, 100 * it.m.tp / (it.m.tp + it.m.fp), 0); break;
        case 'rec': num(it, 100 * it.m.tp / (it.m.tp + it.m.fn), 0); break;
        case 'prbest': { const w = it.f.map(m => it.metric === 'precision' ? m.tp / (m.tp + m.fp) : m.tp / (m.tp + m.fn)), mx = Math.max(...w); if (w.filter(x => x === mx).length !== 1 || a !== `Filter ${LET[w.indexOf(mx)]}`) bad(it, 'a unique best'); break; }
        case 'fpr': num(it, 100 * it.m.fp / (it.m.fp + it.m.tn), 1); break;
        case 'fprfair': { const R = it.f.map(m => 100 * m.fp / (m.fp + m.tn)), gap = Math.max(...R) - Math.min(...R); if (a !== (gap <= 5 ? 'yes' : 'no')) bad(it, 'the other'); break; }
        default: out.push(`${it.q}: no check for kind ${it.k}`);
      }
    }
    return out;
  },
});
})();
