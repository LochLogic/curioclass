// Curio Class family engine: ml-lab (machine learning labs). Docs: docs/families/ml-lab.md
// Inlined by scripts/bundle_tool.py from a kit:ml-lab script tag, after kit:curio. Exposes MLLab.
// (Never write a closing script tag in this file, even in a comment: the inlined copy would end there.)
// Five tools share it: teach-the-robot (2), biased-bot (4), leaf-sorter-ai (5), model-mechanic (6-8), ai-evaluator (9-12).
// The full description is in tools/teach-the-robot/spec.md, "Family engine". The engine draws nothing on its own except
// the three views; their colors come from CSS variables the tool sets (see "Colors" below).
const MLLab = (() => {
  const EPS = 1e-9;   // distances and impurities closer than this count as equal (ties then go by position)

  // ---------- numbers: a seeded random stream, so every dataset in a spec can be rebuilt exactly ----------
  // mulberry32, exactly as written in the family spec
  function rng(seed) {
    let a = seed;
    return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  }
  const uni = (R, lo, hi) => lo + (hi - lo) * R();
  // generated feature values are rounded to 2 decimals at creation (half away from zero, guarded against 0.285 -> 0.28)
  const r2 = x => Math.sign(x) * Math.round(Math.abs(x) * 100 + EPS) / 100;
  // an item: {id, label, v: {feature: 0..1}, tags: {...}}
  const item = (id, label, v, tags = {}) => ({id, label, v, tags});
  const featuresOf = it => Object.keys(it.v);

  // ---------- k nearest neighbors ----------
  // Euclidean distance over the listed features. Neighbors sorted by distance, then by position in train. Vote by
  // count; a tie goes to the tied label whose nearest member comes first. score(label) = share of the k with that label.
  function dist(a, b, features) {
    let s = 0;
    for (const f of features) { const d = (a.v[f] || 0) - (b.v[f] || 0); s += d * d; }
    return Math.sqrt(s);
  }
  function knn(train, it, o = {}) {
    const features = o.features || featuresOf(it), k = Math.max(1, Math.min(o.k || 1, train.length));
    const all = train.map((t, i) => ({item: t, d: dist(t, it, features), i}));
    all.sort((a, b) => Math.abs(a.d - b.d) > EPS ? a.d - b.d : a.i - b.i);
    const neighbors = all.slice(0, k).map(({item, d}) => ({item, d}));
    const votes = {}, first = {};
    neighbors.forEach((n, j) => { const l = n.item.label; votes[l] = (votes[l] || 0) + 1; if (!(l in first)) first[l] = j; });
    let label = null;
    for (const l in votes) if (label === null || votes[l] > votes[label] || (votes[l] === votes[label] && first[l] < first[label])) label = l;
    const score = l => neighbors.length ? (votes[l] || 0) / neighbors.length : 0;
    return {label, votes, neighbors, score};
  }

  // ---------- models: train(type, train, opts) -> {type, predict(item) -> {label, score, ...}} ----------
  // score: with opts.positive (a binary model) it is the positive label's score; otherwise the predicted label's.
  // scores: every label's score. knn adds neighbors and votes; tree adds path (the rules taken); linear adds parts.
  function labelsOf(train) { const s = []; for (const t of train) if (!s.includes(t.label)) s.push(t.label); return s; }
  function negOf(train, o) { return o.negative != null ? o.negative : labelsOf(train).find(l => l !== o.positive); }

  function trainKnn(train, o) {
    const labels = labelsOf(train);
    return {type: 'knn', k: o.k || 1, features: o.features, positive: o.positive, predict(it) {
      const r = knn(train, it, o), scores = {};
      for (const l of labels) scores[l] = r.score(l);
      return {label: r.label, score: o.positive != null ? scores[o.positive] || 0 : r.score(r.label), scores, neighbors: r.neighbors, votes: r.votes};
    }};
  }

  // Decision tree (binary): greedy, Gini impurity, depth o.depth (default 3). Candidate thresholds are midpoints between
  // sorted distinct values of each feature; features tried in the listed order, the first best kept on ties. A split
  // needs at least o.minLeaf (default 5) items on each side and must lower impurity. Left is "at most the threshold".
  // Leaf score = positive share. Rule text: "If Rim is at most 0.31" (o.names maps feature keys to words).
  function trainTree(train, o) {
    const features = o.features || featuresOf(train[0]), pos = o.positive, neg = negOf(train, o);
    const maxDepth = o.depth == null ? 3 : o.depth, minLeaf = o.minLeaf == null ? 5 : o.minLeaf;
    const gini = (p, n) => n ? 1 - (p / n) ** 2 - (1 - p / n) ** 2 : 0;
    function grow(items, depth) {
      const n = items.length, p = items.filter(t => t.label === pos).length, g = gini(p, n);
      const node = {n, pos: p, score: n ? p / n : 0};
      if (depth >= maxDepth || g < EPS) return node;
      let best = null;
      for (const f of features) {
        const vals = [...new Set(items.map(t => t.v[f]))].sort((a, b) => a - b);
        for (let i = 0; i + 1 < vals.length; i++) {
          const th = (vals[i] + vals[i + 1]) / 2;
          let nl = 0, pl = 0;
          for (const t of items) if (t.v[f] <= th) { nl++; if (t.label === pos) pl++; }
          const nr = n - nl, pr = p - pl;
          if (nl < minLeaf || nr < minLeaf) continue;
          const w = (nl * gini(pl, nl) + nr * gini(pr, nr)) / n;
          if (!best || w < best.w - EPS) best = {f, th, w};
        }
      }
      if (!best || best.w >= g - EPS) return node;
      node.feature = best.f; node.threshold = best.th;
      node.left = grow(items.filter(t => t.v[best.f] <= best.th), depth + 1);
      node.right = grow(items.filter(t => t.v[best.f] > best.th), depth + 1);
      return node;
    }
    const root = grow(train, 0), name = f => (o.names && o.names[f]) || f;
    const ruleText = (f, th, le) => `If ${name(f)} is ${le ? 'at most' : 'more than'} ${r2(th).toFixed(2)}`;
    // every rule as nested lines, for showing the trained tree: [{depth, text, leaf, score, n}]
    function rules(node = root, depth = 0, out = []) {
      if (node.feature == null) { out.push({depth, leaf: true, score: node.score, n: node.n, text: `score ${r2(node.score).toFixed(2)} (${node.pos} of ${node.n})`}); return out; }
      out.push({depth, text: ruleText(node.feature, node.threshold, true)}); rules(node.left, depth + 1, out);
      out.push({depth, text: ruleText(node.feature, node.threshold, false)}); rules(node.right, depth + 1, out);
      return out;
    }
    return {type: 'tree', root, rules, positive: pos, negative: neg, predict(it) {
      let node = root; const path = [];
      while (node.feature != null) {
        const le = it.v[node.feature] <= node.threshold;
        path.push({feature: node.feature, threshold: node.threshold, le, text: ruleText(node.feature, node.threshold, le)});
        node = le ? node.left : node.right;
      }
      const s = node.score;
      return {label: s >= .5 ? pos : neg, score: s, scores: {[pos]: s, [neg]: 1 - s}, path, leaf: node};
    }};
  }

  // Linear (logistic regression, binary): weights and bias start at 0; o.rounds (2000) rounds of full-batch gradient
  // descent, learning rate o.rate (1), gradients averaged over the training set. score = 1 / (1 + e^-(bias + sum w x)).
  function trainLinear(train, o) {
    const features = o.features || featuresOf(train[0]), pos = o.positive, neg = negOf(train, o);
    const rounds = o.rounds == null ? 2000 : o.rounds, rate = o.rate == null ? 1 : o.rate, n = train.length;
    const w = features.map(() => 0); let b = 0;
    const X = train.map(t => features.map(f => t.v[f])), Y = train.map(t => t.label === pos ? 1 : 0);
    const sig = z => 1 / (1 + Math.exp(-z));
    for (let r = 0; r < rounds; r++) {
      const gw = features.map(() => 0); let gb = 0;
      for (let i = 0; i < n; i++) {
        let z = b; for (let j = 0; j < w.length; j++) z += w[j] * X[i][j];
        const e = sig(z) - Y[i]; gb += e; for (let j = 0; j < w.length; j++) gw[j] += e * X[i][j];
      }
      b -= rate * gb / n; for (let j = 0; j < w.length; j++) w[j] -= rate * gw[j] / n;
    }
    const weights = Object.fromEntries(features.map((f, j) => [f, w[j]]));
    return {type: 'linear', weights, bias: b, positive: pos, negative: neg, predict(it) {
      const parts = features.map((f, j) => ({feature: f, w: w[j], x: it.v[f], wx: w[j] * it.v[f]}));
      const s = sig(b + parts.reduce((a, p) => a + p.wx, 0));
      return {label: s >= .5 ? pos : neg, score: s, scores: {[pos]: s, [neg]: 1 - s}, parts, bias: b};
    }};
  }

  function train(type, items, o = {}) {
    if (type === 'knn') return trainKnn(items, o);
    if (type === 'tree') return trainTree(items, o);
    if (type === 'linear') return trainLinear(items, o);
    throw new Error('MLLab.train: unknown type ' + type);
  }

  // ---------- evaluate ----------
  // evaluate(model, items, {classes, groupBy, positive, threshold}) ->
  //   {n, ok, acc, cm, cells, classes, byGroup, results, mistakes, tp, fp, fn, tn, recall, precision}
  // cm[true][predicted] counts; cells[true][predicted] lists the items. With positive and threshold the positive label
  // is predicted when its score is at least the threshold. Metrics with a zero denominator are null.
  function posScore(p, pos) {
    if (p.scores && pos in p.scores) return p.scores[pos];
    return p.label === pos ? p.score : 1 - p.score;
  }
  function tally(results, classes, pos) {
    const cm = {}, cells = {};
    for (const a of classes) { cm[a] = {}; cells[a] = {}; for (const b of classes) { cm[a][b] = 0; cells[a][b] = []; } }
    let ok = 0, tp = 0, fp = 0, fn = 0, tn = 0;
    for (const r of results) {
      const t = r.item.label, p = r.pred;
      if (!cm[t]) { cm[t] = {}; cells[t] = {}; }
      cm[t][p] = (cm[t][p] || 0) + 1; (cells[t][p] = cells[t][p] || []).push(r.item);
      if (r.ok) ok++;
      if (pos != null) { if (p === pos) t === pos ? tp++ : fp++; else t === pos ? fn++ : tn++; }
    }
    const n = results.length, out = {n, ok, acc: n ? ok / n : null, cm, cells};
    if (pos != null) Object.assign(out, {tp, fp, fn, tn, recall: tp + fn ? tp / (tp + fn) : null, precision: tp + fp ? tp / (tp + fp) : null});
    return out;
  }
  function evaluate(model, items, o = {}) {
    const pos = o.positive, th = o.threshold;
    const results = items.map(item => {
      const out = model.predict(item);
      const pred = pos != null && th != null ? (posScore(out, pos) >= th - EPS ? pos : (model.negative != null ? model.negative : otherLabel(items, pos, out))) : out.label;
      return {item, pred, ok: pred === item.label, out};
    });
    const classes = o.classes || (() => { const s = []; for (const r of results) for (const l of [r.item.label, r.pred]) if (l != null && !s.includes(l)) s.push(l); return s; })();
    const ev = tally(results, classes, pos);
    ev.classes = classes; ev.results = results; ev.mistakes = results.filter(r => !r.ok);
    ev.byGroup = {};
    if (o.groupBy) {
      const groups = new Map();
      for (const r of results) { const g = o.groupBy(r.item); if (!groups.has(g)) groups.set(g, []); groups.get(g).push(r); }
      for (const [g, rs] of groups) ev.byGroup[g] = tally(rs, classes, pos);
    }
    return ev;
  }
  function otherLabel(items, pos, out) {
    if (out.scores) { const l = Object.keys(out.scores).find(k => k !== pos); if (l != null) return l; }
    const l = items.map(i => i.label).find(x => x !== pos); return l != null ? l : 'not ' + pos;
  }

  // ---------- views (SVG) ----------
  // Colors: the views read CSS variables, with fallbacks, so a tool themes them on :root:
  //   --ml-ink, --ml-muted, --ml-line, --ml-bg (panel behind a view), --ml-cell (an empty cell), --ml-ok (right),
  //   --ml-bad (wrong), --ml-focus, and per class the color given in glyphs[label].color (any CSS color or var()).
  // glyphs[label] = {shape, color, letter}: shape one of circle, square, triangle, diamond, star, hex, plus, x, down;
  // letter is drawn in or beside it. Every class shows a glyph or letter as well as a color (never color alone).
  // names[label or feature] = the word shown. Each view: re-laid out on resize, keyboard focusable where it can be
  // tapped, and an aria-label listing its numbers. Returns {svg, update(data, opts), redraw(), destroy()}.
  const NS = 'http://www.w3.org/2000/svg';
  const C = {ink: 'var(--ml-ink, var(--ink, #222))', muted: 'var(--ml-muted, var(--muted, #555))', line: 'var(--ml-line, var(--line, #ccc))',
    bg: 'var(--ml-bg, var(--panel, #fff))', cell: 'var(--ml-cell, #fff)', ok: 'var(--ml-ok, #1f7a3f)', bad: 'var(--ml-bad, #b42318)',
    focus: 'var(--ml-focus, var(--focus, #c2410c))', brand: 'var(--brand, #333)'};
  function mk(tag, attrs = {}, parent, style) {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (style) Object.assign(e.style, style);
    if (parent) parent.appendChild(e);
    return e;
  }
  function txt(parent, x, y, s, o = {}) {
    const t = mk('text', {x, y, 'text-anchor': o.anchor || 'middle', 'dominant-baseline': o.base || 'central'}, parent,
      {fill: o.fill || C.ink, font: `${o.weight || 600} ${o.size || 13}px ${o.font || "'Segoe UI', system-ui, sans-serif"}`});
    t.textContent = s; return t;
  }
  // a glyph shape centred on (x, y) with radius r, as one path or circle
  function glyph(shape, x, y, r, parent, style = {}) {
    let e;
    const P = pts => mk('path', {d: 'M' + pts.map(p => p.map(v => v.toFixed(2)).join(' ')).join('L') + 'Z'}, parent, style);
    const poly = (n, rot, rr = r) => Array.from({length: n}, (_, i) => { const a = rot + i * 2 * Math.PI / n; return [x + rr * Math.cos(a), y + rr * Math.sin(a)]; });
    switch (shape) {
      case 'square': e = mk('rect', {x: x - r * .85, y: y - r * .85, width: r * 1.7, height: r * 1.7, rx: r * .15}, parent, style); break;
      case 'triangle': e = P(poly(3, -Math.PI / 2, r * 1.12).map(([px, py]) => [px, py + r * .15])); break;
      case 'down': e = P(poly(3, Math.PI / 2, r * 1.12).map(([px, py]) => [px, py - r * .15])); break;
      case 'diamond': e = P(poly(4, -Math.PI / 2, r * 1.15)); break;
      case 'hex': e = P(poly(6, 0)); break;
      case 'star': e = P(Array.from({length: 10}, (_, i) => { const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r * .5 : r * 1.15; return [x + rr * Math.cos(a), y + rr * Math.sin(a)]; })); break;
      case 'plus': { const a = r * .38; e = P([[x - a, y - r], [x + a, y - r], [x + a, y - a], [x + r, y - a], [x + r, y + a], [x + a, y + a], [x + a, y + r], [x - a, y + r], [x - a, y + a], [x - r, y + a], [x - r, y - a], [x - a, y - a]]); break; }
      case 'x': { const g = mk('g', {transform: `rotate(45 ${x} ${y})`}, parent); const a = r * .36;
        mk('path', {d: `M${x - a} ${y - r}H${x + a}V${y - a}H${x + r}V${y + a}H${x + a}V${y + r}H${x - a}V${y + a}H${x - r}V${y - a}H${x - a}Z`}, g, style); e = g; break; }
      default: e = mk('circle', {cx: x, cy: y, r}, parent, style);
    }
    return e;
  }
  const gOf = (glyphs, l, i) => {
    const g = (glyphs && glyphs[l]) || {}, s = typeof g === 'string' ? {shape: g} : g;
    const shapes = ['circle', 'square', 'triangle', 'diamond', 'star', 'hex'];
    return {shape: s.shape || shapes[i % shapes.length], color: s.color || `var(--ml-${i % 6 + 1}, ${['#1f77b4', '#d95f02', '#1b9e77', '#7570b3', '#e7298a', '#66a61e'][i % 6]})`, letter: s.letter || ''};
  };
  function drawGlyph(parent, glyphs, l, i, x, y, r, extra = {}) {
    const g = gOf(glyphs, l, i);
    glyph(g.shape, x, y, r, parent, {fill: g.color, stroke: C.ink, strokeWidth: Math.max(1, r * .14), ...extra});
    if (g.letter && r >= 7) txt(parent, x, y + .5, g.letter, {size: Math.round(r * 1.05), weight: 800, fill: '#fff'}).style.paintOrder = 'stroke';
    return g;
  }
  // the box a view draws in: its element's size, watched for changes
  function host(el, draw) {
    el.textContent = '';
    const svg = mk('svg', {role: 'group'}, el, {display: 'block', width: '100%', height: '100%', overflow: 'visible'});
    let W = 0, H = 0, dead = false;
    const go = () => {
      if (dead) return;
      const r = el.getBoundingClientRect(), w = Math.max(60, Math.round(r.width)), h = Math.max(60, Math.round(r.height));
      W = w; H = h; svg.setAttribute('viewBox', `0 0 ${w} ${h}`); svg.setAttribute('width', w); svg.setAttribute('height', h);
      svg.textContent = ''; draw(svg, w, h);
    };
    const ro = new ResizeObserver(() => { const r = el.getBoundingClientRect(); if (Math.round(r.width) !== W || Math.round(r.height) !== H) go(); });
    ro.observe(el);
    return {svg, redraw: go, destroy() { dead = true; ro.disconnect(); el.textContent = ''; }};
  }
  // make an SVG group act like a button: focusable, Enter or Space, and a visible focus ring
  function tappable(g, label, fn, ring) {
    g.setAttribute('tabindex', '0'); g.setAttribute('role', 'button'); g.setAttribute('aria-label', label);
    g.style.cursor = 'pointer'; g.style.outline = 'none';
    g.addEventListener('click', fn);
    g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fn(e); } });
    if (ring) { g.addEventListener('focus', () => ring.style.display = ''); g.addEventListener('blur', () => ring.style.display = 'none'); ring.style.display = 'none'; }
  }

  // confusion(el, ev, {classes, names, glyphs, onCell, rowTitle, colTitle}): rows = what it really was, columns = what
  // the model said; counts in every cell; diagonal cells outlined; other cells shaded by count. Tap or Enter on a cell:
  // onCell({truth, pred, count, items}). Arrow keys move between cells.
  function confusion(el, ev, o = {}) {
    let E = ev, O = o, focus = null;
    const h = host(el, draw);
    function draw(svg, W, H) {
      const cls = O.classes || E.classes, n = cls.length, nm = l => (O.names && O.names[l]) || l;
      // the row labels column fits the longest name (estimated text width), within 40% of the width
      const tw = (s, size) => String(s).length * size * .56;
      const gr0 = 10, head = Math.min(W * .4, Math.max(64, 18 + gr0 * 2 + Math.max(...cls.map(l => tw(nm(l), 13))))), x0 = head;
      const ct = O.colTitle || 'What the model said', rt = O.rowTitle || 'What it really was';
      // the two titles share one line when they fit side by side, else the column title takes a second line
      let cell = Math.max(28, Math.min((W - head - 8) / n, (H - 46 - 8) / n));
      const oneLine = 6 + tw(rt, 13) + 10 <= x0 + cell * n / 2 - tw(ct, 13) / 2;
      const top = oneLine ? 46 : 64;
      cell = Math.max(28, Math.min((W - head - 8) / n, (H - top - 8) / n));
      const y0 = top, max = Math.max(1, ...cls.flatMap(t => cls.filter(p => p !== t).map(p => (E.cm[t] || {})[p] || 0)));
      if (oneLine) txt(svg, x0 + cell * n / 2, 12, ct, {size: 13, fill: C.muted});
      else txt(svg, Math.max(6, Math.min(x0 + cell * n / 2 - tw(ct, 13) / 2, W - 6 - tw(ct, 13))), 30, ct, {size: 13, fill: C.muted, anchor: 'start'});
      txt(svg, 6, 12, rt, {size: 13, fill: C.muted, anchor: 'start'});
      const gr = Math.min(gr0, cell * .2), fs = Math.max(12, Math.min(26, cell * .32));
      cls.forEach((l, i) => {
        const cx = x0 + cell * (i + .5);
        const cs = Math.max(11, Math.min(13, cell * .2)), x1 = cx - (gr * 2 + 4 + tw(nm(l), cs)) / 2;   // glyph and name centred as one
        drawGlyph(svg, O.glyphs, l, i, x1 + gr, top - 14, gr);
        txt(svg, x1 + gr * 2 + 4, top - 14, nm(l), {size: cs, anchor: 'start'});
        drawGlyph(svg, O.glyphs, l, i, 6 + gr, y0 + cell * (i + .5), gr);
        txt(svg, 10 + gr * 2, y0 + cell * (i + .5), nm(l), {size: 13, anchor: 'start'});
      });
      const cells = [];
      cls.forEach((t, i) => cls.forEach((p, j) => {
        const c = (E.cm[t] || {})[p] || 0, x = x0 + j * cell, y = y0 + i * cell, diag = i === j;
        const g = mk('g', {}, svg);
        mk('rect', {x: x + 2, y: y + 2, width: cell - 4, height: cell - 4, rx: 6}, g, {fill: C.cell, stroke: C.line, strokeWidth: 1});
        if (!diag && c) mk('rect', {x: x + 2, y: y + 2, width: cell - 4, height: cell - 4, rx: 6}, g, {fill: C.bad, opacity: .08 + .37 * c / max});
        if (diag) mk('rect', {x: x + 3.5, y: y + 3.5, width: cell - 7, height: cell - 7, rx: 5}, g, {fill: 'none', stroke: C.ok, strokeWidth: 3});
        txt(g, x + cell / 2, y + cell / 2 + 1, String(c), {size: fs, weight: 800, font: 'var(--readout-font, ui-monospace, Consolas, monospace)'});
        const ring = mk('rect', {x: x - 1, y: y - 1, width: cell + 2, height: cell + 2, rx: 8}, g, {fill: 'none', stroke: C.focus, strokeWidth: 3});
        const items = ((E.cells || {})[t] || {})[p] || [];
        tappable(g, `${nm(t)} that the model called ${nm(p)}: ${c}`, () => { focus = [i, j]; O.onCell && O.onCell({truth: t, pred: p, count: c, items}); }, ring);
        g.addEventListener('keydown', e => {
          const d = {ArrowLeft: [0, -1], ArrowRight: [0, 1], ArrowUp: [-1, 0], ArrowDown: [1, 0]}[e.key];
          if (!d) return; e.preventDefault();
          const ni = Math.max(0, Math.min(n - 1, i + d[0])), nj = Math.max(0, Math.min(n - 1, j + d[1]));
          cells[ni * n + nj].focus({preventScroll: true}); focus = [ni, nj];
        });
        if (!O.onCell) { g.removeAttribute('role'); g.removeAttribute('tabindex'); }   // nothing to do on a tap: not a stop for the keyboard
        cells.push(g);
      }));
      svg.setAttribute('aria-label', 'Confusion matrix. ' + cls.map(t => `Really ${nm(t)}: ` + cls.map(p => `${(E.cm[t] || {})[p] || 0} called ${nm(p)}`).join(', ')).join('. '));
      if (focus && document.activeElement && el.contains(document.activeElement) === false) focus = null;
    }
    return {svg: h.svg, redraw: h.redraw, destroy: h.destroy, update(ev2, o2) { if (ev2) E = ev2; if (o2) O = {...O, ...o2}; h.redraw(); }};
  }

  // scatter(el, items, {fx, fy, glyphs, names, labels: {x, y}, query: {item, neighbors}, onPick, classes}): two features
  // as axes 0 to 1 (fy null draws a strip on one axis); each item a glyph by its label; a query item drawn as a ring
  // with dashed lines to its neighbors. Tap or Enter on a point: onPick(item).
  function scatter(el, items, o = {}) {
    let I = items, O = o;
    const h = host(el, draw);
    function draw(svg, W, H) {
      const cls = O.classes || labelsOf(I), nm = k => (O.names && O.names[k]) || k;
      const L = 44, B = O.fy ? 40 : 30, T = 10, Rr = 12, pw = W - L - Rr, ph = O.fy ? H - T - B : Math.min(60, H - T - B);
      const r = Math.max(6, Math.min(11, Math.min(pw, ph || pw) / 30)), m = r + 4;   // points at 0 and 1 stay inside the frame
      const X = v => L + m + v * (pw - 2 * m), Y = v => O.fy ? T + m + (1 - v) * (ph - 2 * m) : T + ph / 2;
      mk('rect', {x: L, y: T, width: pw, height: ph, rx: 4}, svg, {fill: C.cell, stroke: C.line});
      for (const t of [0, .5, 1]) {
        txt(svg, X(t), T + ph + 12, t.toFixed(1), {size: 11, fill: C.muted});
        mk('line', {x1: X(t), y1: T, x2: X(t), y2: T + ph}, svg, {stroke: C.line, strokeWidth: 1});
        if (O.fy) { txt(svg, L - 6, Y(t), t.toFixed(1), {size: 11, fill: C.muted, anchor: 'end'}); mk('line', {x1: L, y1: Y(t), x2: L + pw, y2: Y(t)}, svg, {stroke: C.line, strokeWidth: 1}); }
      }
      txt(svg, L + pw / 2, T + ph + 28, (O.labels && O.labels.x) || nm(O.fx), {size: 13, weight: 700});
      if (O.fy) { const t = txt(svg, 12, T + ph / 2, (O.labels && O.labels.y) || nm(O.fy), {size: 13, weight: 700}); t.setAttribute('transform', `rotate(-90 12 ${T + ph / 2})`); }
      const at = it => [X(it.v[O.fx]), Y(O.fy ? it.v[O.fy] : 0)];
      const q = O.query;
      if (q && q.item) {
        const [qx, qy] = at(q.item);
        for (const nb of q.neighbors || []) { const [nx, ny] = at(nb.item); mk('line', {x1: qx, y1: qy, x2: nx, y2: ny}, svg, {stroke: C.ink, strokeWidth: 2, strokeDasharray: '5 4'}); }
      }
      const near = new Set(q && q.neighbors ? q.neighbors.map(n => n.item) : []);
      I.forEach(it => {
        const [x, y] = at(it), i = Math.max(0, cls.indexOf(it.label)), g = mk('g', {}, svg);
        if (near.has(it)) mk('circle', {cx: x, cy: y, r: r + 5}, g, {fill: 'none', stroke: C.ink, strokeWidth: 2});
        drawGlyph(g, O.glyphs, it.label, i, x, y, r);
        const ring = mk('circle', {cx: x, cy: y, r: r + 8}, g, {fill: 'none', stroke: C.focus, strokeWidth: 3});
        if (O.onPick) tappable(g, `${it.name || it.id}, ${nm(it.label)}: ${nm(O.fx)} ${it.v[O.fx]}` + (O.fy ? `, ${nm(O.fy)} ${it.v[O.fy]}` : ''), () => O.onPick(it), ring);
        else ring.remove();
      });
      if (q && q.item) {
        const [qx, qy] = at(q.item);
        mk('circle', {cx: qx, cy: qy, r: r + 3}, svg, {fill: C.bg, stroke: C.ink, strokeWidth: 3});
        txt(svg, qx, qy + .5, '?', {size: r * 1.5, weight: 800});
      }
      svg.setAttribute('aria-label', `Map of ${nm(O.fx)}` + (O.fy ? ` across and ${nm(O.fy)} up` : '') + `, ${I.length} items: ` +
        cls.map(l => `${I.filter(i => i.label === l).length} ${nm(l)}`).join(', ') + (q && q.item ? `. The new item's nearest: ${(q.neighbors || []).map(n => nm(n.item.label)).join(', ')}` : ''));
    }
    return {svg: h.svg, redraw: h.redraw, destroy: h.destroy, update(it2, o2) { if (it2) I = it2; if (o2) O = {...O, ...o2}; h.redraw(); }};
  }

  // groupBars(el, byGroup, {names, glyphs, order, unit}): one bar per group, length = share right, with "n of m right"
  function groupBars(el, byGroup, o = {}) {
    let G = byGroup, O = o;
    const h = host(el, draw);
    function draw(svg, W, H) {
      const keys = O.order || Object.keys(G), nm = k => (O.names && O.names[k]) || k, unit = O.unit || 'right';
      const rowH = Math.max(30, Math.min(52, H / Math.max(1, keys.length))), lab = Math.min(150, Math.max(80, W * .3)), bw = W - lab - 12;
      keys.forEach((k, i) => {
        const g = G[k] || {n: 0, ok: 0}, y = i * rowH, r = Math.min(9, rowH * .22), share = g.n ? g.ok / g.n : 0;
        drawGlyph(svg, O.glyphs, k, i, r + 2, y + rowH * .38, r);
        txt(svg, r * 2 + 8, y + rowH * .38, nm(k), {size: 13, weight: 700, anchor: 'start'});
        mk('rect', {x: lab, y: y + 4, width: bw, height: rowH * .5, rx: 5}, svg, {fill: C.cell, stroke: C.line});
        if (share) mk('rect', {x: lab, y: y + 4, width: bw * share, height: rowH * .5, rx: 5}, svg, {fill: gOf(O.glyphs, k, i).color, stroke: C.ink, strokeWidth: 1});
        txt(svg, lab, y + rowH * .5 + 14, `${g.ok} of ${g.n} ${unit}`, {size: 12, anchor: 'start', fill: C.ink});
      });
      svg.setAttribute('aria-label', keys.map(k => `${nm(k)}: ${(G[k] || {}).ok || 0} of ${(G[k] || {}).n || 0} ${unit}`).join('. '));
    }
    return {svg: h.svg, redraw: h.redraw, destroy: h.destroy, update(g2, o2) { if (g2) G = g2; if (o2) O = {...O, ...o2}; h.redraw(); }};
  }

  return {rng, uni, r2, item, dist, knn, train, evaluate, glyph, view: {confusion, scatter, groupBars}, version: 1};
})();
if (typeof module !== 'undefined') module.exports = MLLab;
