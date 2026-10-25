// Curio Class family engine: graphing. A coordinate plane in SVG that plots functions and points and lets people
// drag things that change them. Inlined by scripts/bundle_tool.py from a kit:graphing script tag, after
// kit:curio. Spec and API: docs/families/graphing.md. New features go here and into that doc in the same change.
const Plane = (() => {
  const NS = 'http://www.w3.org/2000/svg';
  const mk = (tag, attrs = {}, parent) => {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) if (attrs[k] != null) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  };
  // series colors 1 to 4 always come with their own dash pattern, so color is never the only signal
  const DASH = {1: null, 2: '10 6', 3: '2 5', 4: '12 4 2 4'};
  const colorOf = c => typeof c === 'number' ? `var(--gr-${c})` : (c || 'var(--gr-1)');
  const dashOf = (o, fallback) => o.dashed === true ? '8 6' : (typeof o.dashed === 'string' ? o.dashed :
    (o.dashed === false ? null : (typeof o.color === 'number' ? DASH[o.color] : fallback)));
  let uid = 0, styled = false;
  function style() {
    if (styled) return; styled = true;
    const s = document.createElement('style');
    s.textContent = `
.gr-grid line{stroke:var(--gr-grid,rgba(128,128,128,.18));stroke-width:1}
.gr-grid line.major{stroke:var(--gr-grid-major,rgba(128,128,128,.35))}
.gr-axis{stroke:var(--gr-axis,#444);stroke-width:2}
.gr-tick{fill:var(--gr-text,#555);font:13px 'Segoe UI',system-ui,sans-serif}
.gr-axlabel{fill:var(--gr-text,#555);font:600 14px 'Segoe UI',system-ui,sans-serif}
.gr-fn{fill:none;stroke-linecap:round;stroke-linejoin:round}
.gr-grid,.gr-fn,.gr-seg,.gr-label,.gr-tick,.gr-axlabel{pointer-events:none}
.gr-pt{cursor:grab;outline:none}
.gr-pt.drag{cursor:grabbing}
.gr-pt .gr-hit{fill:transparent}
.gr-pt .gr-ring{fill:none;stroke:transparent;stroke-width:4}
.gr-pt:focus-visible .gr-ring{stroke:var(--focus,#e0662a)}
.gr-ptlabel,.gr-label{fill:var(--ink,#222);font:600 14px 'Segoe UI',system-ui,sans-serif}
.gr-slider{display:grid;grid-template-columns:1fr auto;gap:4px 10px;align-items:center}
.gr-slider label{grid-column:1/-1;font-weight:600}
`;
    document.head.appendChild(s);
  }

  // numbers as people read them: up to dp decimals, trailing zeros dropped, a true minus sign
  function fmt(n, dp = 2) {
    if (!isFinite(n)) return n > 0 ? '∞' : n < 0 ? '−∞' : '?';
    let s = (+(+n).toFixed(dp)).toString();
    if (/e/.test(s)) s = (+n).toPrecision(3);
    if (s === '-0') s = '0';
    return s.replace('-', '−');
  }
  // significant figures (for coefficients): fmtSig(0.0333333, 3) = "0.0333"
  function fmtSig(n, sig = 3) {
    if (!isFinite(n)) return fmt(n);
    if (n === 0) return '0';
    return fmt(+(+n).toPrecision(sig), 12);
  }

  // ---------- numeric helpers (pure; also on every plane) ----------
  function roots(f, [a, b], {n = 2000} = {}) {
    const xs = [], ys = [];
    for (let i = 0; i <= n; i++) { const x = a + (b - a) * i / n; xs.push(x); ys.push(f(x)); }
    const big = Math.max(1, ...ys.filter(isFinite).map(Math.abs)), eps = big * 1e-10, out = [];
    for (let i = 0; i <= n; i++) {
      if (ys[i] === 0) { out.push(xs[i]); continue; }
      if (i < n && isFinite(ys[i]) && isFinite(ys[i + 1]) && ys[i] * ys[i + 1] < 0) {
        let lo = xs[i], hi = xs[i + 1], flo = ys[i];
        for (let k = 0; k < 80; k++) { const m = (lo + hi) / 2, fm = f(m); if (fm === 0) { lo = hi = m; break; } if (fm * flo < 0) hi = m; else { lo = m; flo = fm; } }
        // a big jump with a sign change is an asymptote, not a root
        const m = (lo + hi) / 2; if (Math.abs(f(m)) <= Math.max(eps, Math.abs(ys[i]), Math.abs(ys[i + 1]))) out.push(m);
      } else if (i > 0 && i < n && Math.abs(ys[i]) <= Math.abs(ys[i - 1]) && Math.abs(ys[i]) <= Math.abs(ys[i + 1]) && ys[i - 1] * ys[i + 1] > 0) {
        // touching roots (even multiplicity) never change sign: look for |f| dipping to zero
        const m = golden(x => Math.abs(f(x)), xs[i - 1], xs[i + 1]);
        if (Math.abs(f(m)) < eps) out.push(m);
      }
    }
    out.sort((p, q) => p - q);
    const tol = (b - a) * 1e-5;
    return out.filter((x, i) => i === 0 || x - out[i - 1] > tol);
  }
  function golden(f, a, b, maxi = 100) { // minimum of f on [a, b]
    const r = (Math.sqrt(5) - 1) / 2;
    let c = b - r * (b - a), d = a + r * (b - a), fc = f(c), fd = f(d);
    for (let i = 0; i < maxi && Math.abs(b - a) > 1e-12; i++) {
      if (fc < fd) { b = d; d = c; fd = fc; c = b - r * (b - a); fc = f(c); } else { a = c; c = d; fc = fd; d = a + r * (b - a); fd = f(d); }
    }
    return (a + b) / 2;
  }
  // interior turning points: [{x, y, kind: 'max' | 'min'}], left to right (a flat crossing is not one)
  function extrema(f, [a, b], {n = 2000} = {}) {
    const xs = [], ys = [], out = [];
    for (let i = 0; i <= n; i++) { const x = a + (b - a) * i / n; xs.push(x); ys.push(f(x)); }
    for (let i = 1; i < n; i++) {
      const d0 = ys[i] - ys[i - 1], d1 = ys[i + 1] - ys[i];
      if (!isFinite(d0) || !isFinite(d1)) continue;
      const kind = d0 > 0 && d1 <= 0 ? 'max' : d0 < 0 && d1 >= 0 ? 'min' : null;
      if (!kind) continue;
      const x = golden(kind === 'max' ? t => -f(t) : f, xs[i - 1], xs[i + 1]);
      if (!out.length || x - out[out.length - 1].x > (b - a) * 1e-5) out.push({x, y: f(x), kind});
    }
    return out;
  }

  function Plane(parent, opts = {}) {
    style();
    const o = Object.assign({x: [-10, 10], y: [-10, 10], width: 600, height: 600, grid: 1, labels: 5, xLabel: '', yLabel: '',
      left: 0, top: 0, ticks: 'axis', axes: true}, opts);
    const W = o.width, H = o.height, id = 'gr' + (++uid);
    let X = [...o.x], Y = [...o.y];
    const pair = v => Array.isArray(v) ? v : [v, v];
    const root = mk('g', {class: 'gr', transform: `translate(${o.left},${o.top})`}, parent);
    const defs = mk('defs', {}, root);
    mk('rect', {x: 0, y: 0, width: W, height: H}, mk('clipPath', {id: id + '-clip'}, defs));
    const clip = `url(#${id}-clip)`;
    const layers = {};
    layers.back = mk('g', {'clip-path': clip}, root);
    layers.grid = mk('g', {class: 'gr-grid', 'clip-path': clip}, root);
    layers.plot = mk('g', {'clip-path': clip}, root);
    layers.front = mk('g', {'clip-path': clip}, root);
    layers.points = mk('g', {}, root);
    layers.labels = mk('g', {}, root);
    const tickG = mk('g', {}, layers.labels);   // tick and axis text, redrawn on every view (a tool's own labels are kept)
    const hit = mk('rect', {x: 0, y: 0, width: W, height: H, fill: 'transparent'}, layers.back);
    layers.back.insertBefore(hit, layers.back.firstChild);

    const px = (x, y) => [(x - X[0]) * W / (X[1] - X[0]), (Y[1] - y) * H / (Y[1] - Y[0])];
    const coord = (u, v) => [X[0] + u / W * (X[1] - X[0]), Y[1] - v / H * (Y[1] - Y[0])];
    function eventCoord(e) {
      const p = (root.ownerSVGElement || root).createSVGPoint(); p.x = e.clientX; p.y = e.clientY;
      const q = p.matrixTransform(root.getScreenCTM().inverse());
      return coord(q.x, q.y);
    }

    // ---------- grid, axes, ticks ----------
    function drawGrid() {
      layers.grid.textContent = ''; tickG.textContent = '';
      // a step may be a number or fn(lo, hi) -> step, worked out again for every view (for ranges that change size)
      const stepOf = (s, lo, hi) => typeof s === 'function' ? s(lo, hi) : s;
      const [gx0, gy0] = pair(o.grid), [lx0, ly0] = pair(o.labels);
      const gx = stepOf(gx0, ...X), gy = stepOf(gy0, ...Y), lx = stepOf(lx0, ...X), ly = stepOf(ly0, ...Y);
      // tickFormat(v, 'x' | 'y') -> label text; null or '' leaves that tick unlabeled
      const tick = (v, axis) => o.tickFormat ? o.tickFormat(v, axis) : fmt(v);
      const steps = (lo, hi, s) => { const out = []; for (let v = Math.ceil(lo / s - 1e-9) * s; v <= hi + 1e-9; v += s) out.push(+v.toFixed(10)); return out; };
      const isMul = (v, s) => Math.abs(v / s - Math.round(v / s)) < 1e-6;
      for (const x of steps(X[0], X[1], gx)) { const [u] = px(x, 0); mk('line', {x1: u, x2: u, y1: 0, y2: H, class: isMul(x, lx) ? 'major' : null}, layers.grid); }
      for (const y of steps(Y[0], Y[1], gy)) { const [, v] = px(0, y); mk('line', {x1: 0, x2: W, y1: v, y2: v, class: isMul(y, ly) ? 'major' : null}, layers.grid); }
      const [ox, oy] = px(0, 0);
      const edge = o.ticks === 'edge';
      if (o.axes) {
        if (oy >= 0 && oy <= H) mk('line', {x1: 0, x2: W, y1: oy, y2: oy, class: 'gr-axis'}, layers.grid);
        if (ox >= 0 && ox <= W) mk('line', {x1: ox, x2: ox, y1: 0, y2: H, class: 'gr-axis'}, layers.grid);
      }
      const tyX = edge ? H + 18 : Math.min(Math.max(oy + 18, 14), H - 4);   // where x tick labels sit
      const txY = edge ? -16 : Math.min(Math.max(ox - 6, 30), W - 4);       // where y tick labels sit
      for (const x of steps(X[0], X[1], lx)) {
        if (!edge && Math.abs(x) < 1e-9) continue;
        const t = tick(x, 'x'); if (t == null || t === '') continue;
        const [u] = px(x, 0); mk('text', {x: u, y: tyX, 'text-anchor': 'middle', class: 'gr-tick'}, tickG).textContent = t;
      }
      for (const y of steps(Y[0], Y[1], ly)) {
        if (!edge && Math.abs(y) < 1e-9) continue;
        const t = tick(y, 'y'); if (t == null || t === '') continue;
        const [, v] = px(0, y); mk('text', {x: txY, y: v + 4.5, 'text-anchor': 'end', class: 'gr-tick'}, tickG).textContent = t;
      }
      if (o.xLabel) mk('text', edge ? {x: W / 2, y: H + 40, 'text-anchor': 'middle', class: 'gr-axlabel'} :
        {x: W - 4, y: Math.max(oy - 8, 16), 'text-anchor': 'end', class: 'gr-axlabel'}, tickG).textContent = o.xLabel;
      if (o.yLabel) mk('text', edge ? {transform: `translate(${-48},${H / 2}) rotate(-90)`, 'text-anchor': 'middle', class: 'gr-axlabel'} :
        {x: Math.min(ox + 8, W - 4), y: 16, class: 'gr-axlabel'}, tickG).textContent = o.yLabel;
    }

    // ---------- items: everything plotted re-renders itself when the view changes ----------
    let items = [];
    const viewFns = [];
    function add(item) { items.push(item); item.render(); return item; }
    function removeItem(item) { item.el.remove(); items = items.filter(i => i !== item); }

    // sample y = f(x) between a and b in data units, subdividing where the curve moves fast; null marks a break
    function sampleFn(f, a, b) {
      const out = [], n = Math.max(60, Math.ceil(W / 3)), ky = H / (Y[1] - Y[0]);
      const outside = (y0, y1) => (y0 > Y[1] && y1 > Y[1]) || (y0 < Y[0] && y1 < Y[0]);
      const refine = (x0, y0, x1, y1, d) => {
        if (!isFinite(y0) || !isFinite(y1)) return;
        if (Math.abs(y1 - y0) * ky <= 3 || outside(y0, y1)) return;
        if (d >= 8) { if (Math.abs(y1 - y0) * ky > 2 * H && y0 * y1 < 0) out.push(null); return; } // asymptote
        const xm = (x0 + x1) / 2, ym = f(xm);
        refine(x0, y0, xm, ym, d + 1); out.push(isFinite(ym) ? [xm, ym] : null); refine(xm, ym, x1, y1, d + 1);
      };
      let x0 = a, y0 = f(a); out.push(isFinite(y0) ? [x0, y0] : null);
      for (let i = 1; i <= n; i++) {
        const x1 = a + (b - a) * i / n, y1 = f(x1);
        refine(x0, y0, x1, y1, 0); out.push(isFinite(y1) ? [x1, y1] : null); x0 = x1; y0 = y1;
      }
      return out;
    }
    // data points to pixel runs, clipped to the plane's height (plus a margin for the stroke)
    function runsOf(pts, m = 12) {
      const runs = []; let run = null;
      const lo = -m, hi = H + m;
      for (let i = 0; i < pts.length; i++) {
        const p = pts[i] && px(...pts[i]), q = pts[i + 1] && px(...pts[i + 1]);
        if (!p) { run = null; continue; }
        const inside = p[1] >= lo && p[1] <= hi;
        if (inside && !run) { run = [p]; runs.push(run); }
        else if (inside) run.push(p);
        if (!q) continue;
        // where the segment p to q crosses the top or bottom edge
        const qin = q[1] >= lo && q[1] <= hi;
        if (inside && !qin) { const e = q[1] < lo ? lo : hi, t = (e - p[1]) / (q[1] - p[1]); run.push([p[0] + t * (q[0] - p[0]), e]); run = null; }
        else if (!inside && qin) { const e = p[1] < lo ? lo : hi, t = (e - p[1]) / (q[1] - p[1]); run = [[p[0] + t * (q[0] - p[0]), e]]; runs.push(run); }
        else if (!inside && !qin && (p[1] < lo) !== (q[1] < lo)) { // straight through the view
          const t1 = (lo - p[1]) / (q[1] - p[1]), t2 = (hi - p[1]) / (q[1] - p[1]);
          const a = [p[0] + t1 * (q[0] - p[0]), lo], b = [p[0] + t2 * (q[0] - p[0]), hi];
          runs.push(t1 < t2 ? [a, b] : [b, a]);
        }
      }
      return runs.filter(r => r.length > 1);
    }
    const dOf = runs => runs.map(r => 'M' + r.map(p => p[0].toFixed(1) + ',' + p[1].toFixed(1)).join('L')).join('');
    function arrowD(tip, from, size) {
      const ang = Math.atan2(tip[1] - from[1], tip[0] - from[0]), s = size;
      const pt = (r, t) => [tip[0] + r * Math.cos(ang + t), tip[1] + r * Math.sin(ang + t)];
      const [l, rr] = [pt(s, Math.PI - .45), pt(s, Math.PI + .45)];
      return `M${tip[0].toFixed(1)},${tip[1].toFixed(1)}L${l[0].toFixed(1)},${l[1].toFixed(1)}L${rr[0].toFixed(1)},${rr[1].toFixed(1)}Z`;
    }
    function curveItem(sample, opt) {
      const layer = layers[opt.layer || 'plot'];
      const el = mk('g', {class: 'gr-fn' + (opt.class ? ' ' + opt.class : ''), opacity: opt.opacity}, layer);
      const path = mk('path', {class: 'gr-fn', stroke: colorOf(opt.color), 'stroke-width': opt.width || 3, 'stroke-dasharray': dashOf(opt, null)}, el);
      if (opt.label) { mk('title', {}, path).textContent = opt.label; path.setAttribute('aria-label', opt.label); }
      const heads = mk('path', {fill: colorOf(opt.color)}, el);
      const item = {id: opt.id, el, path, opt, runs: [], render() {
        const runs = item.runs = runsOf(sample(), (opt.width || 3) + 2);
        path.setAttribute('d', dOf(runs));
        let d = '';
        if (runs.length && opt.arrows) {
          const size = 8 + (opt.width || 3) * 1.4;
          const back = (r, i, dir) => { let j = i; while (j + dir >= 0 && j + dir < r.length && Math.hypot(r[j][0] - r[i][0], r[j][1] - r[i][1]) < size) j += dir; return r[j]; };
          const f0 = runs[0], l0 = runs[runs.length - 1];
          if (opt.arrows === 'start' || opt.arrows === 'both' || opt.arrows === true) d += arrowD(f0[0], back(f0, 0, 1), size);
          if (opt.arrows === 'end' || opt.arrows === 'both' || opt.arrows === true) d += arrowD(l0[l0.length - 1], back(l0, l0.length - 1, -1), size);
        }
        heads.setAttribute('d', d);
      }};
      return add(item);
    }
    // y = f(x): {color, width, domain: [a, b], id, dashed, arrows: 'start' | 'end' | 'both', label, class, layer, opacity}
    function fn(f, opt = {}) {
      return curveItem(() => {
        const a = Math.max(opt.domain ? opt.domain[0] : -Infinity, X[0]), b = Math.min(opt.domain ? opt.domain[1] : Infinity, X[1]);
        return b > a ? sampleFn(f, a, b) : [];
      }, opt);
    }
    // parametric (x(t), y(t)) for t in [t0, t1]: f returns [x, y]
    function param(f, [t0, t1], opt = {}) {
      return curveItem(() => {
        const n = opt.samples || 400, out = [];
        for (let i = 0; i <= n; i++) { const p = f(t0 + (t1 - t0) * i / n); out.push(p && isFinite(p[0]) && isFinite(p[1]) ? p : null); }
        return out;
      }, opt);
    }
    // a straight segment from a = [x, y] to b = [x, y]: {color, width, dashed, id, class, layer, arrow: 'end'}
    function segment(a, b, opt = {}) {
      const el = mk('g', {class: 'gr-seg' + (opt.class ? ' ' + opt.class : '')}, layers[opt.layer || 'plot']);
      const line = mk('line', {stroke: colorOf(opt.color), 'stroke-width': opt.width || 2, 'stroke-dasharray': dashOf(opt, null), 'stroke-linecap': 'round'}, el);
      const head = opt.arrow ? mk('path', {fill: colorOf(opt.color)}, el) : null;
      const item = {id: opt.id, el, a, b, set(na, nb) { item.a = na; item.b = nb; item.render(); }, render() {
        const p = px(...item.a), q = px(...item.b);
        line.setAttribute('x1', p[0]); line.setAttribute('y1', p[1]); line.setAttribute('x2', q[0]); line.setAttribute('y2', q[1]);
        if (head) head.setAttribute('d', arrowD(q, p, 9 + (opt.width || 2)));
      }};
      return add(item);
    }
    // text at (x, y): {anchor, dx, dy, class, id, layer}
    function label(x, y, text, opt = {}) {
      const el = mk('text', {class: 'gr-label' + (opt.class ? ' ' + opt.class : ''), 'text-anchor': opt.anchor || 'start'}, layers[opt.layer || 'front']);
      el.textContent = text;
      const item = {id: opt.id, el, x, y, set(t) { el.textContent = t; }, move(nx, ny) { item.x = nx; item.y = ny; item.render(); }, render() {
        const [u, v] = px(item.x, item.y); el.setAttribute('x', u + (opt.dx || 0)); el.setAttribute('y', v + (opt.dy || 0));
      }};
      return add(item);
    }

    // ---------- points: pointer and keyboard, 44 px hit area ----------
    // opts: label, color, draggable, onMove(x, y, h), onDrop(x, y, h, from), onKey(e, h) (return true when handled),
    // snap (a step, or fn(x, y) -> [x, y]), lock: {y: 0} (slides left and right only) or {x: c}, range: {x: [a, b], y: [a, b]},
    // step (arrow-key nudge, default the snap step or a tenth of the grid), shape: 'circle' | 'diamond' | 'none', r,
    // hit (radius of the pointer target in plane pixels, default 22: a 44 px target at scale 1),
    // ariaLabel (text or fn(x, y)), valueText fn(x, y), id, class
    function point(x, y, opt = {}) {
      const r = opt.r || 8;
      const el = mk('g', {class: 'gr-pt' + (opt.class ? ' ' + opt.class : ''), tabindex: opt.draggable ? 0 : null,
        role: opt.draggable ? 'slider' : 'img'}, layers.points);
      const hitC = mk('circle', {class: 'gr-hit', r: opt.hit || Math.max(22, r + 6)}, el);
      const ring = mk('circle', {class: 'gr-ring', r: r + 7}, el);
      if (opt.shape === 'diamond') { const s = r * 1.35; mk('path', {d: `M0,${-s}L${s},0L0,${s}L${-s},0Z`, fill: colorOf(opt.color), stroke: 'var(--paper,#fff)', 'stroke-width': 2}, el); ring.setAttribute('r', s + 7); }
      else if (opt.shape !== 'none') mk('circle', {r, fill: colorOf(opt.color), stroke: 'var(--paper,#fff)', 'stroke-width': 2}, el);
      const body = mk('g', {}, el);   // the tool may draw its own marks here, in pixels around the point
      const text = opt.label ? mk('text', {class: 'gr-ptlabel', x: r + 8, y: -r - 4}, el) : null;
      if (text) text.textContent = opt.label;
      const lock = opt.lock || {};
      const fix = (nx, ny) => {
        if (lock.x != null) nx = lock.x;
        if (lock.y != null) ny = lock.y;
        if (typeof h.snap === 'function') [nx, ny] = h.snap(nx, ny);
        else if (h.snap) { const s = h.snap; if (lock.x == null) nx = Math.round(nx / s) * s; if (lock.y == null) ny = Math.round(ny / s) * s; }
        const rx = opt.range && opt.range.x, ry = opt.range && opt.range.y;
        if (rx) nx = Math.min(rx[1], Math.max(rx[0], nx));
        if (ry) ny = Math.min(ry[1], Math.max(ry[0], ny));
        return [+nx.toFixed(9), +ny.toFixed(9)];
      };
      const h = {id: opt.id, el, body, x, y, snap: opt.snap, step: opt.step, render() {
        const [u, v] = px(h.x, h.y); el.setAttribute('transform', `translate(${u.toFixed(1)},${v.toFixed(1)})`);
        const al = typeof opt.ariaLabel === 'function' ? opt.ariaLabel(h.x, h.y) : opt.ariaLabel || opt.label || 'point';
        el.setAttribute('aria-label', al);
        const vt = opt.valueText ? opt.valueText(h.x, h.y) : lock.y != null ? `x = ${fmt(h.x)}` : lock.x != null ? `y = ${fmt(h.y)}` : `(${fmt(h.x)}, ${fmt(h.y)})`;
        if (opt.draggable) {
          el.setAttribute('aria-valuetext', vt);
          const main = lock.y != null || lock.x == null ? h.x : h.y, rg = opt.range && (lock.y != null || lock.x == null ? opt.range.x : opt.range.y);
          el.setAttribute('aria-valuenow', main); if (rg) { el.setAttribute('aria-valuemin', rg[0]); el.setAttribute('aria-valuemax', rg[1]); }
        }
      }, set(nx, ny) { h.x = nx; h.y = ny; h.render(); }, setHit(nr) { hitC.setAttribute('r', nr); }, setLabel(t) { if (text) text.textContent = t; }, focus() { el.focus(); },
      remove() { removeItem(h); }};
      if (opt.draggable) {
        let from = null;
        el.addEventListener('pointerdown', e => {
          if (e.button) return;
          e.preventDefault(); el.focus(); el.setPointerCapture(e.pointerId); el.classList.add('drag'); from = [h.x, h.y]; h.dragging = true;
        });
        el.addEventListener('pointermove', e => {
          if (!from) return;
          const [nx, ny] = fix(...eventCoord(e));
          if (nx !== h.x || ny !== h.y) { h.set(nx, ny); opt.onMove && opt.onMove(h.x, h.y, h); }
        });
        const end = () => { if (!from) return; const f = from; from = null; h.dragging = false; el.classList.remove('drag'); opt.onDrop && opt.onDrop(h.x, h.y, h, f); };
        el.addEventListener('pointerup', end); el.addEventListener('pointercancel', end);
        el.addEventListener('keydown', e => {
          if (opt.onKey && opt.onKey(e, h)) { e.preventDefault(); return; }
          const s = h.step || (typeof h.snap === 'number' ? h.snap : pair(o.grid)[0] / 10);
          const d = {ArrowLeft: [-s, 0], ArrowRight: [s, 0], ArrowUp: [0, s], ArrowDown: [0, -s]}[e.key];
          if (!d) return;
          e.preventDefault();
          const f = [h.x, h.y];
          const [nx, ny] = fix(h.x + d[0], h.y + d[1]);
          if (nx === h.x && ny === h.y) return;
          h.set(nx, ny); opt.onMove && opt.onMove(h.x, h.y, h); opt.onDrop && opt.onDrop(h.x, h.y, h, f);
        });
      }
      return add(h);
    }

    // a dot that rides y = f(x) and reads out (x, f(x)): {x, color, r, onMove(x, y), draggable, readout, domain, id,
    // valueText fn(x, y) (its screen-reader value), hit}. domain is read live, so a tool may change its array in place.
    function trace(f, opt = {}) {
      const dom = opt.domain || X;
      const p = point(opt.x != null ? opt.x : dom[0], 0, {color: opt.color, r: opt.r || 6, draggable: opt.draggable, id: opt.id,
        ariaLabel: opt.ariaLabel || 'trace point', range: {x: dom}, lock: {}, step: opt.step, hit: opt.hit,
        valueText: opt.valueText || ((x, y) => `(${fmt(x)}, ${fmt(y)})`),
        snap: (nx) => [Math.min(dom[1], Math.max(dom[0], nx)), f(Math.min(dom[1], Math.max(dom[0], nx)))],
        onMove: (x, y) => { show(); opt.onMove && opt.onMove(x, y); }});
      const text = opt.readout ? mk('text', {class: 'gr-ptlabel', x: 12, y: -12}, p.el) : null;
      const show = () => { if (text) text.textContent = `(${fmt(p.x)}, ${fmt(p.y)})`; };
      const t = {id: opt.id, el: p.el, get x() { return p.x; }, get y() { return p.y; },
        set(x) { p.set(x, f(x)); show(); opt.onMove && opt.onMove(p.x, p.y); }, remove() { p.remove(); }, setHit: r => p.setHit(r), point: p};
      t.set(p.x);
      return t;
    }

    // animated zoom and pan; resolves when done (instant when Curio's Motion is off or ms is 0)
    function view(xr, yr, {ms = 600} = {}) {
      const x0 = [...X], y0 = [...Y];
      const apply = t => { const e = t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
        X = [x0[0] + (xr[0] - x0[0]) * e, x0[1] + (xr[1] - x0[1]) * e]; Y = [y0[0] + (yr[0] - y0[0]) * e, y0[1] + (yr[1] - y0[1]) * e]; redraw(); };
      if (!ms || (window.Curio && Curio.reduce)) { apply(1); return Promise.resolve(); }
      return new Promise(done => { const s = performance.now(); const step = now => { const t = Math.min(1, (now - s) / ms); apply(t); t < 1 ? requestAnimationFrame(step) : done(); }; requestAnimationFrame(step); });
    }
    function redraw() { drawGrid(); items.forEach(i => i.render()); viewFns.forEach(f => f()); }

    // remove everything with this id (no id: everything plotted)
    function clear(cid) { for (const i of [...items]) if (cid == null || i.id === cid) removeItem(i); }

    drawGrid();
    return {
      px, coord, eventCoord, fn, param, point, segment, label, trace, view, clear, slider,
      roots, extrema, intersect: (f1, f2, ab, o2) => roots(x => f1(x) - f2(x), ab, o2),
      layer: name => layers[name], onView: f => viewFns.push(f), onClick: f => hit.addEventListener('click', e => f(...eventCoord(e), e)),
      get range() { return {x: [...X], y: [...Y]}; }, width: W, height: H, root, clipId: id + '-clip', fmt,
    };
  }

  // a labeled, keyboard-friendly parameter slider in an HTML container:
  // {label, min, max, step, value, onInput(v, source), scale: 'linear' | 'log', box (a number box beside it),
  //  format(v) -> box and readout text, parse(text) -> a value, or null to refuse (the box then restores), id}
  // source is 'slider', 'box' or 'set'. Returns {value, set(v, quiet), el, range, box}.
  function slider(container, opt = {}) {
    style();
    const o = Object.assign({min: 0, max: 1, step: .01, value: 0, scale: 'linear', box: true, format: v => fmt(v, 3)}, opt);
    const sid = o.id || 'grs' + (++uid);
    const el = document.createElement('div'); el.className = 'gr-slider';
    const lab = document.createElement('label'); lab.htmlFor = sid; lab.textContent = o.label || ''; el.appendChild(lab);
    const range = document.createElement('input'); range.type = 'range'; range.id = sid; el.appendChild(range);
    const log = o.scale === 'log', N = 1000;
    if (log) { range.min = 0; range.max = N; range.step = 1; } else { range.min = o.min; range.max = o.max; range.step = o.step; }
    const toPos = v => log ? Math.round((Math.log10(v) - Math.log10(o.min)) / (Math.log10(o.max) - Math.log10(o.min)) * N) : v;
    const fromPos = p => log ? +Math.pow(10, Math.log10(o.min) + p / N * (Math.log10(o.max) - Math.log10(o.min))).toPrecision(4) : +p;
    let box = null;
    if (o.box) {
      box = document.createElement('input'); box.type = 'text'; box.inputMode = 'decimal'; box.className = 'num';
      box.setAttribute('aria-label', (o.label || 'value') + ', type a number'); el.appendChild(box);
    }
    const h = {el, range, box, value: o.value,
      set(v, quiet) { h.value = Math.min(o.max, Math.max(o.min, v)); show(); if (!quiet) o.onInput && o.onInput(h.value, 'set'); },
      refresh: () => show()};
    function show() {
      range.value = toPos(h.value);
      const t = o.format(h.value);
      range.setAttribute('aria-valuetext', t);
      if (box && document.activeElement !== box) box.value = t;
    }
    range.addEventListener('input', () => { h.value = fromPos(range.value); show(); o.onInput && o.onInput(h.value, 'slider'); });
    if (box) {
      const commit = () => {
        const v = o.parse ? o.parse(box.value) : (isFinite(parseFloat(box.value.replace('−', '-'))) ? parseFloat(box.value.replace('−', '-')) : null);
        if (v == null) { box.value = o.format(h.value); return; }
        h.value = Math.min(o.max, Math.max(o.min, v)); range.value = toPos(h.value);
        o.onInput && o.onInput(h.value, 'box'); box.value = o.format(h.value);
      };
      box.addEventListener('change', commit);
      box.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); commit(); } });
      box.addEventListener('blur', () => { box.value = o.format(h.value); });
    }
    show();
    container.appendChild(el);
    return h;
  }

  Plane.fmt = fmt; Plane.fmtSig = fmtSig; Plane.roots = roots; Plane.extrema = extrema; Plane.slider = slider;
  return Plane;
})();
