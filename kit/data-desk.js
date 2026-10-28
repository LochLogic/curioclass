// Curio Class family engine: data desk. A small data table and the SVG charts that read from it, all updating live
// when the data changes. Inlined by scripts/bundle_tool.py from a kit:data-desk script tag, after kit:curio.
// Spec and API: docs/families/data-desk.md. New features go here and into that doc in the same change, keeping
// existing calls working. Globals: DataTable, Chart, DataDesk. No network requests, no dependencies.
const DataDesk = (() => {
  const NS = 'http://www.w3.org/2000/svg';
  const version = '1.1';
  const mk = (tag, attrs = {}, parent) => {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) if (attrs[k] != null) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  };
  const isNum = v => typeof v === 'number' && isFinite(v);
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const coarse = () => typeof matchMedia === 'function' && matchMedia('(pointer: coarse)').matches;
  const calm = () => typeof Curio !== 'undefined' && !!Curio.reduce;
  let uid = 0, styled = false;

  // ---------- look: colors come from CSS variables, so a tool sets its own on :root ----------
  // --dd-1 to --dd-6 (series), --dd-text, --dd-axis, --dd-grid, --dd-ring (highlight), --dd-font, --dd-bgline (the
  // edge of solid points), --dd-bg-solid (the inside of hollow marks).
  // Defaults sit in :where(:root) (no specificity), dark ones when the 9-12 theme is loaded, so any tool's :root wins.
  const LIGHT = {1: '#1f6fbf', 2: '#b35900', 3: '#2b8a3e', 4: '#b4236b', 5: '#6b4fbb', 6: '#56606b',
    text: '#3b4654', axis: '#4a5563', grid: 'rgba(0,0,0,.09)', ring: '#d0461b', bg: 'transparent'};
  const DARK = {1: '#5aa9ff', 2: '#ffd166', 3: '#5fd39a', 4: '#ff8a8a', 5: '#c9a0ff', 6: '#a6b3c4',
    text: '#a6b3c4', axis: '#c9d3df', grid: 'rgba(255,255,255,.08)', ring: '#ff7f32', bg: 'transparent'};
  // series shapes: color is never the only signal
  const SHAPES = {1: 'circle', 2: 'triangle', 3: 'square', 4: 'diamond', 5: 'cross', 6: 'star'};
  const DASH = {1: null, 2: '8 5', 3: '2 4', 4: '10 4 2 4', 5: '14 6', 6: '4 4'};
  function style() {
    if (styled) return; styled = true;
    const dark = !!getComputedStyle(document.documentElement).getPropertyValue('--gr-bg').trim();
    const P = dark ? DARK : LIGHT, v = [];
    for (let i = 1; i <= 6; i++) v.push(`--dd-${i}:${P[i]}`);
    v.push(`--dd-text:${P.text}`, `--dd-axis:${P.axis}`, `--dd-grid:${P.grid}`, `--dd-ring:${P.ring}`);
    const s = document.createElement('style');
    s.id = 'dd-style';
    s.textContent = `
:where(:root){${v.join(';')}}
.dd-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.dd-chart text{font-family:var(--dd-font,'Segoe UI',system-ui,sans-serif);fill:var(--dd-text)}
.dd-chart .dd-axis{stroke:var(--dd-axis);stroke-width:1.5}
.dd-chart .dd-grid{stroke:var(--dd-grid);stroke-width:1}
.dd-chart .dd-marks,.dd-chart .dd-deco{pointer-events:none}
.dd-chart .dd-axlabel{font-weight:600}
.dd-pick{outline:none;cursor:pointer}
.dd-pick .dd-focus{fill:none;stroke:transparent;stroke-width:3}
.dd-pick:focus-visible .dd-focus{stroke:var(--focus,#e0662a)}
.dd-drag{cursor:grab}
.dd-tablewrap{display:flex;flex-direction:column;gap:6px;min-width:0}
:where(.dd-table){border-collapse:collapse;font-variant-numeric:tabular-nums}
:where(.dd-table) :where(th,td){padding:2px 8px;text-align:right;border:1px solid var(--dd-grid)}
:where(.dd-table) td.dd-text{text-align:left}
:where(.dd-table) td.dd-missing::after{content:'(blank)';opacity:.6;font-style:italic}
.dd-table input.dd-cell{width:6em;min-height:44px;box-sizing:border-box;font:inherit;color:inherit;background:transparent;border:1px solid transparent;text-align:inherit;border-radius:4px}
.dd-table input.dd-cell:focus{border-color:var(--focus,#e0662a)}
.dd-pager{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
:where(.dd-pager button,.dd-rowbtn){min-height:44px;min-width:44px}
.dd-tablewrap .dd-remove,.dd-tablewrap .dd-add{min-height:44px;min-width:44px;box-sizing:border-box}
.dd-tablewrap>.dd-add{align-self:flex-start;padding:0 14px}
.dd-table td:has(>.dd-remove){padding:0}
.dd-pager [aria-disabled="true"]{opacity:.4;cursor:not-allowed}
.dd-pageno{font-variant-numeric:tabular-nums;min-width:7.5em;text-align:center}
`;
    document.head.prepend(s);
  }

  // ---------- numbers ----------
  // numbers as people read them: thousands separators, a true minus sign; d decimals (fixed), or up to 2 with
  // trailing zeros dropped when d is left out
  // opts.group: false leaves out the thousands separator (years: 2000, not 2,000)
  function fmt(n, d, opts = {}) {
    if (n == null || n === '') return '';
    if (!isFinite(n)) return n > 0 ? '∞' : n < 0 ? '−∞' : '?';
    let s;
    const useGrouping = opts.group !== false;
    if (d == null) s = (+(+n).toFixed(2)).toLocaleString('en-US', {maximumFractionDigits: 2, useGrouping});
    else s = (+n).toLocaleString('en-US', {minimumFractionDigits: d, maximumFractionDigits: d, useGrouping});
    if (/^-0(\.0+)?$/.test(s)) s = s.slice(1);
    return s.replace('-', '−');
  }
  // "nice" axis steps (1, 2, 2.5 or 5 times a power of ten) covering lo..hi with about count ticks
  function nice(lo, hi, count = 5) {
    if (!isNum(lo) || !isNum(hi)) { lo = 0; hi = 1; }
    if (lo === hi) { const p = Math.abs(lo) || 1; lo -= p / 2; hi += p / 2; }
    if (lo > hi) [lo, hi] = [hi, lo];
    const raw = (hi - lo) / Math.max(1, count), p = Math.pow(10, Math.floor(Math.log10(raw))), f = raw / p;
    const step = (f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10) * p;
    const a = Math.floor(lo / step + 1e-9) * step, b = Math.ceil(hi / step - 1e-9) * step, ticks = [];
    for (let v = a; v <= b + step * 1e-6; v += step) ticks.push(+v.toFixed(10));
    return {lo: a, hi: b, step, ticks};
  }
  const mean = a => a.reduce((s, v) => s + v, 0) / a.length;
  const medianSorted = s => { const n = s.length; return n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2; };
  // summary statistics of a list (non-numbers skipped). Quartiles: the median of each half, leaving the median
  // out when n is odd (the method taught in US grades 6 to 8 and used by TI calculators). mad is the mean absolute
  // deviation (grade 6); sd the sample standard deviation (n - 1), sdp the population one. Outliers: the 1.5 IQR rule.
  function stats(values) {
    const s = values.filter(isNum).sort((a, b) => a - b), n = s.length;
    if (!n) return {n: 0, min: NaN, max: NaN, mean: NaN, median: NaN, q1: NaN, q3: NaN, iqr: NaN, mad: NaN, sd: NaN, sdp: NaN,
      sum: 0, lo: NaN, hi: NaN, whiskerLo: NaN, whiskerHi: NaN, outliers: []};
    const m = mean(s), half = Math.floor(n / 2);
    const q1 = n === 1 ? s[0] : medianSorted(s.slice(0, half)), q3 = n === 1 ? s[0] : medianSorted(s.slice(n - half));
    const iqr = q3 - q1, lo = q1 - 1.5 * iqr, hi = q3 + 1.5 * iqr;
    const ss = s.reduce((a, v) => a + (v - m) * (v - m), 0);
    const inside = s.filter(v => v >= lo && v <= hi);
    return {n, min: s[0], max: s[n - 1], mean: m, median: medianSorted(s), q1, q3, iqr,
      mad: s.reduce((a, v) => a + Math.abs(v - m), 0) / n, sd: n > 1 ? Math.sqrt(ss / (n - 1)) : 0, sdp: Math.sqrt(ss / n),
      sum: m * n, lo, hi, whiskerLo: inside.length ? inside[0] : s[0], whiskerHi: inside.length ? inside[inside.length - 1] : s[n - 1],
      outliers: s.filter(v => v < lo || v > hi)};
  }
  // least squares line y = a + b x with Pearson's r (signed)
  function linreg(xs, ys) {
    const n = xs.length;
    if (n < 2) return {a: NaN, b: NaN, r: NaN, r2: NaN, n};
    const mx = mean(xs), my = mean(ys);
    let sxy = 0, sxx = 0, syy = 0;
    for (let i = 0; i < n; i++) { const dx = xs[i] - mx, dy = ys[i] - my; sxy += dx * dy; sxx += dx * dx; syy += dy * dy; }
    const b = sxx ? sxy / sxx : NaN, r = sxx && syy ? sxy / Math.sqrt(sxx * syy) : NaN;
    return {a: my - b * mx, b, r, r2: r * r, n};
  }
  // fit a model by least squares. linear: y = a + b x; quadratic: y = a + b x + c x^2 (normal equations);
  // exponential: y = a e^(b x), fitted as a line through ln y (points with y <= 0 are left out).
  // Returns {kind, f, params, r2, r, residuals, n, eq}: r2 on the original y scale for all three, so models compare;
  // r is Pearson's r (signed) for linear, and the square root of r2 for the others.
  function fit(kind, xs, ys) {
    let pts = xs.map((x, i) => [x, ys[i]]).filter(p => isNum(p[0]) && isNum(p[1]));
    if (kind === 'exponential') pts = pts.filter(p => p[1] > 0);
    const X = pts.map(p => p[0]), Y = pts.map(p => p[1]), n = pts.length;
    let f, params, eq, r;
    if (kind === 'quadratic') {
      let S = [0, 0, 0, 0, 0], T = [0, 0, 0];
      for (let i = 0; i < n; i++) { let p = 1; for (let k = 0; k < 5; k++) { S[k] += p; if (k < 3) T[k] += p * Y[i]; p *= X[i]; } }
      const M = [[S[0], S[1], S[2], T[0]], [S[1], S[2], S[3], T[1]], [S[2], S[3], S[4], T[2]]];
      for (let c = 0; c < 3; c++) {                              // Gaussian elimination with partial pivoting
        let p = c; for (let r2 = c + 1; r2 < 3; r2++) if (Math.abs(M[r2][c]) > Math.abs(M[p][c])) p = r2;
        [M[c], M[p]] = [M[p], M[c]];
        for (let r2 = 0; r2 < 3; r2++) if (r2 !== c && M[c][c]) { const k = M[r2][c] / M[c][c]; for (let j = c; j < 4; j++) M[r2][j] -= k * M[c][j]; }
      }
      const a = M[0][3] / M[0][0], b = M[1][3] / M[1][1], c = M[2][3] / M[2][2];
      params = {a, b, c}; f = x => a + b * x + c * x * x;
      eq = `y = ${fmt(a)} ${b < 0 ? '−' : '+'} ${fmt(Math.abs(b))}x ${c < 0 ? '−' : '+'} ${fmt(Math.abs(c))}x²`;
    } else if (kind === 'exponential') {
      const L = linreg(X, Y.map(Math.log)), a = Math.exp(L.a), b = L.b;
      params = {a, b}; f = x => a * Math.exp(b * x);
      eq = `y = ${fmt(a)} × e^(${fmt(b, 3)}x)`;
    } else {
      kind = 'linear';
      const L = linreg(X, Y);
      params = {a: L.a, b: L.b}; f = x => L.a + L.b * x; r = L.r;
      eq = `y = ${fmt(L.a)} ${L.b < 0 ? '−' : '+'} ${fmt(Math.abs(L.b))}x`;
    }
    const my = n ? mean(Y) : NaN;
    let res = 0, tot = 0;
    const residuals = X.map((x, i) => Y[i] - f(x));
    residuals.forEach((e, i) => { res += e * e; tot += (Y[i] - my) * (Y[i] - my); });
    const r2 = tot ? 1 - res / tot : NaN;
    if (r == null) r = Math.sqrt(Math.max(0, r2));
    return {kind, f, params, r2, r, residuals, n, eq};
  }

  // ---------- DataTable ----------
  // rows: plain objects. opts.columns: {key: {label, unit, digits, type: 'number' | 'year' | 'text' | 'bool', values}}
  function DataTable(rows = [], opts = {}) {
    const fns = {};
    let hold = 0, held = null;
    const t = {
      rows: rows.map(r => ({...r})),
      columns: {},
      on(ev, f) { (fns[ev] = fns[ev] || []).push(f); return () => { fns[ev] = (fns[ev] || []).filter(g => g !== f); }; },
      emit(ev, info = {}) {
        if (ev === 'change' && hold) { held = held ? {type: 'batch'} : info; return; }
        (fns[ev] || []).slice().forEach(f => f(info, t));
      },
      // run fn with change events held, then send one
      batch(fn) { hold++; try { fn(t); } finally { hold--; if (!hold && held) { const h = held; held = null; t.emit('change', h); } } },
      add(row) { t.rows.push({...row}); const i = t.rows.length - 1; t.emit('change', {type: 'add', i}); return i; },
      set(i, key, v) {
        const c = t.columns[key];
        if (c && (c.type === 'number' || c.type === 'year') && v !== null && v !== '' && typeof v !== 'number') { const x = parseFloat(v); v = isFinite(x) ? x : null; }
        if (v === '') v = null;
        t.rows[i][key] = v; t.emit('change', {type: 'set', i, key});
      },
      remove(i) { t.rows.splice(i, 1); t.emit('change', {type: 'remove', i}); },
      replace(rows2) { t.rows = rows2.map(r => ({...r})); t.emit('change', {type: 'replace'}); },
      values: (key, keep) => t.rows.filter((r, i) => !keep || keep(r, i)).map(r => r[key]),
      column: (key, keep) => t.values(key, keep).filter(isNum),
      stats: (key, keep) => stats(t.column(key, keep)),
      // how many rows have each value of a column, in the column's own order (columns[key].values) or first appearance
      count(key, keep) {
        const m = new Map(), order = (t.columns[key] || {}).values;
        if (order) order.forEach(v => m.set(v, 0));
        t.values(key, keep).forEach(v => { if (v != null && v !== '') m.set(v, (m.get(v) || 0) + 1); });
        return [...m].map(([value, n]) => ({value, n}));
      },
      // a two-way table: {rows: values of a, cols: values of b, n(ra, cb), total}
      crosstab(a, b, keep) {
        const ra = t.count(a, keep).map(x => x.value), cb = t.count(b, keep).map(x => x.value), cells = new Map();
        t.rows.forEach((r, i) => { if (keep && !keep(r, i)) return; const k = r[a] + '\u0000' + r[b]; cells.set(k, (cells.get(k) || 0) + 1); });
        const n = (x, y) => cells.get(x + '\u0000' + y) || 0;
        return {rows: ra, cols: cb, n, total: ra.reduce((s, x) => s + cb.reduce((s2, y) => s2 + n(x, y), 0), 0)};
      },
      label(key, unit = true) {
        const c = t.columns[key] || {};
        return (c.label || key) + (unit && c.unit ? ` (${c.unit})` : '');
      },
      where: keep => DataTable(t.rows.filter((r, i) => keep(r, i)), {columns: t.columns}),
      renderTable: (el, o) => renderTable(t, el, o),
    };
    // columns: given ones first, then any other key seen in the rows; the type is inferred when not given
    const keys = [...Object.keys(opts.columns || {})];
    t.rows.forEach(r => Object.keys(r).forEach(k => { if (!keys.includes(k)) keys.push(k); }));
    for (const k of keys) {
      const c = {...(opts.columns || {})[k]};
      if (!c.type) {
        const vs = t.rows.map(r => r[k]).filter(v => v != null && v !== '');
        c.type = vs.length && vs.every(v => typeof v === 'number') ? 'number' : vs.length && vs.every(v => typeof v === 'boolean') ? 'bool' : 'text';
      }
      t.columns[k] = c;
    }
    return t;
  }

  // a real <table> (screen reader friendly: caption, th scope), paged when opts.page is a number of rows per page.
  // opts: {page, columns: [keys], index: '#' (a row-number column) | false, caption, editable, removable, addRow (a
  // button label), rowClass(row, i), onRow(i, row, event), cellClass(row, i, key)}. Returns a controller:
  // {el, update(), go(p), show(i), page, pages, onPage(fn), destroy()}. Pager buttons stay put and use aria-disabled
  // at the ends, so keyboard focus is never lost when a page changes.
  function renderTable(t, host, o = {}) {
    style();
    const id = 'dd' + (++uid), per = o.page > 0 ? o.page : 0;
    const wrap = document.createElement('div'); wrap.className = 'dd-tablewrap';
    const table = document.createElement('table'); table.className = 'inst dd-table'; table.id = id;
    const cap = document.createElement('caption'); cap.className = 'dd-sr'; table.appendChild(cap);
    const thead = table.createTHead(), tbody = table.createTBody();
    wrap.appendChild(table);
    let pager = null, prev, next, label, addBtn, p = 0;
    const pageFns = [];
    if (per) {
      pager = document.createElement('div'); pager.className = 'dd-pager';
      prev = document.createElement('button'); prev.className = 'btn dd-prev'; prev.textContent = 'Previous'; prev.setAttribute('aria-controls', id);
      label = document.createElement('span'); label.className = 'dd-pageno'; label.setAttribute('aria-live', 'polite');
      next = document.createElement('button'); next.className = 'btn dd-next'; next.textContent = 'Next'; next.setAttribute('aria-controls', id);
      pager.append(prev, label, next); wrap.appendChild(pager);
      prev.onclick = () => { if (p > 0) go(p - 1, true); };
      next.onclick = () => { if (p < pages() - 1) go(p + 1, true); };
    }
    if (o.addRow) {
      addBtn = document.createElement('button'); addBtn.className = 'btn dd-add'; addBtn.textContent = o.addRow;
      addBtn.onclick = () => { const blank = {}; keys().forEach(k => { blank[k] = null; }); const i = t.add(blank); show(i); focusCell(i, keys()[0]); };
      (pager || wrap).appendChild(addBtn);
    }
    const keys = () => o.columns || Object.keys(t.columns);
    const pages = () => per ? Math.max(1, Math.ceil(t.rows.length / per)) : 1;
    function head() {
      thead.textContent = '';
      const tr = thead.insertRow();
      const th = txt => { const h = document.createElement('th'); h.scope = 'col'; h.textContent = txt; tr.appendChild(h); };
      if (o.index !== false) th(o.index || '#');
      keys().forEach(k => th(t.label(k)));
      if (o.removable) th('');
    }
    function focusCell(i, k) {
      const inp = tbody.querySelector(`input[data-i="${i}"][data-k="${k}"]`);
      if (inp) inp.focus({preventScroll: true});
    }
    function body() {
      tbody.textContent = '';
      const a = per ? p * per : 0, b = per ? Math.min(t.rows.length, a + per) : t.rows.length;
      for (let i = a; i < b; i++) {
        const r = t.rows[i], tr = tbody.insertRow();
        tr.dataset.i = i;
        const rc = o.rowClass ? o.rowClass(r, i) : '';
        if (rc) tr.className = rc;
        if (o.index !== false) {
          const h = document.createElement('th'); h.scope = 'row';
          if (o.onRow) {
            const btn = document.createElement('button'); btn.className = 'dd-rowbtn'; btn.textContent = i + 1;
            btn.setAttribute('aria-label', `Row ${i + 1}`); btn.onclick = e => o.onRow(i, r, e); h.appendChild(btn);
          } else h.textContent = i + 1;
          tr.appendChild(h);
        }
        for (const k of keys()) {
          const c = t.columns[k] || {}, td = tr.insertCell(), v = r[k];
          const numeric = c.type === 'number' || c.type === 'year';
          if (!numeric) td.classList.add('dd-text');
          if (o.cellClass) { const cc = o.cellClass(r, i, k); if (cc) td.className += ' ' + cc; }
          if (o.editable) {
            const inp = document.createElement('input'); inp.className = 'dd-cell';
            inp.value = v == null ? '' : numeric ? String(v) : v;
            if (numeric) inp.inputMode = 'decimal';
            inp.dataset.i = i; inp.dataset.k = k;
            inp.setAttribute('aria-label', `Row ${i + 1}, ${t.label(k)}`);
            inp.onchange = () => t.set(i, k, numeric ? inp.value : inp.value.trim());
            inp.onkeydown = e => {
              if (e.key !== 'Enter') return;
              e.preventDefault(); inp.onchange();
              const j = i + 1;
              if (j < t.rows.length) { show(j); focusCell(j, k); }
            };
            td.appendChild(inp);
          } else if (v == null || v === '') td.classList.add('dd-missing');
          else td.textContent = c.type === 'year' ? fmt(v, 0, {group: false}) : c.type === 'number' ? fmt(v, c.digits) : String(v);
        }
        if (o.removable) {
          const td = tr.insertCell(), x = document.createElement('button');
          x.className = 'btn dd-remove'; x.textContent = '×'; x.setAttribute('aria-label', `Remove row ${i + 1}`);
          x.onclick = () => { t.remove(i); const j = Math.min(i, t.rows.length - 1); if (j >= 0) { show(j); const n2 = tbody.querySelector(`tr[data-i="${j}"] .dd-remove`); if (n2) n2.focus({preventScroll: true}); } };
          td.appendChild(x);
        }
      }
      if (per) {
        label.textContent = `Page ${p + 1} of ${pages()}`;
        prev.setAttribute('aria-disabled', p === 0); next.setAttribute('aria-disabled', p >= pages() - 1);
      }
      cap.textContent = (o.caption || 'Data table') + `, ${t.rows.length} rows` + (per ? `, rows ${a + 1} to ${b} shown` : '');
    }
    // onPage functions get (page, {user}): user is true for a Previous or Next press, false for go() or show() from code
    function go(q, user = false) {
      const q2 = clamp(q | 0, 0, pages() - 1), changed = q2 !== p;
      p = q2; body();
      if (changed) pageFns.forEach(f => f(p, {user}));
    }
    function show(i) { if (per) go(Math.floor(i / per)); else body(); }
    const goCode = q => go(q);
    function update() { head(); if (p > pages() - 1) p = pages() - 1; body(); }
    const off = t.on('change', info => { if (o.editable && info.type === 'set') return; update(); });
    update();
    host.appendChild(wrap);
    return {el: wrap, table, update, go: goCode, show, get page() { return p; }, get pages() { return pages(); },
      onPage: f => pageFns.push(f), destroy() { off(); wrap.remove(); }};
  }

  // ---------- marks ----------
  // a marker of a series shape centered at x, y with radius r
  function shape(g, kind, x, y, r, attrs = {}) {
    let e;
    if (kind === 'triangle') e = mk('path', {d: `M${x} ${y - r * 1.25}L${x + r * 1.15} ${y + r * .8}L${x - r * 1.15} ${y + r * .8}Z`});
    else if (kind === 'square') e = mk('rect', {x: x - r * .9, y: y - r * .9, width: r * 1.8, height: r * 1.8});
    else if (kind === 'diamond') e = mk('path', {d: `M${x} ${y - r * 1.25}L${x + r * 1.25} ${y}L${x} ${y + r * 1.25}L${x - r * 1.25} ${y}Z`});
    else if (kind === 'cross') e = mk('path', {d: `M${x - r} ${y - r}L${x + r} ${y + r}M${x + r} ${y - r}L${x - r} ${y + r}`, 'stroke-width': 2.2, fill: 'none'});
    else if (kind === 'star') {
      let d = ''; for (let k = 0; k < 10; k++) { const a = -Math.PI / 2 + k * Math.PI / 5, rr = k % 2 ? r * .55 : r * 1.35; d += (k ? 'L' : 'M') + (x + rr * Math.cos(a)).toFixed(1) + ' ' + (y + rr * Math.sin(a)).toFixed(1); }
      e = mk('path', {d: d + 'Z'});
    } else e = mk('circle', {cx: x, cy: y, r});
    for (const k in attrs) if (attrs[k] != null) e.setAttribute(k, attrs[k]);
    g.appendChild(e);
    return e;
  }
  const col = s => typeof s === 'number' ? `var(--dd-${s})` : (s || 'var(--dd-1)');

  // ---------- Chart ----------
  // Chart(svgOrGroup, table, opts). opts: {type: 'dot' | 'bar' | 'histogram' | 'box' | 'scatter' | 'line', x, y (a key,
  // or a list of keys for line), width, height, bins (a width, or {width, start}), groupBy, filter(row, i), xLabel,
  // yLabel, xDomain, yDomain, share (histogram: shares in percent instead of counts), style ('fill' | 'outline'),
  // series (1 to 6), label (the series name), overlay ({table, x, filter, style, series, label}: a second histogram
  // series; faded: true dims it), tops (histogram: each series' shape on its bars), groups (box: the order of the groups),
  // groupLabels ({value: label}: box rows and grouped-bar legend), domainFaint (false: faint points do not stretch the axes), marks (['mean', 'median']), bands ([{from, to, label}]),
  // point(row, i) -> {shape, series, ring, faint, hidden}, font, margin, pointSize, animate (ms, default 300; 0 when
  // Motion is off), title, xFormat, yFormat (v -> text), dragStep ({x, y}), live (default true: redraw on every table change)}.
  // Returns {update(opts), resize(w, h), highlight(sel), onPoint(fn), fit(kind), curve(f, style), drag(on), text(),
  // lastFit, bins, scales, el, destroy()}.
  function Chart(target, t, opts = {}) {
    style();
    const svg = target.ownerSVGElement || target;
    const root = target.tagName.toLowerCase() === 'svg' ? mk('g', {}, target) : target;
    root.classList.add('dd-chart');
    const o = {type: 'scatter', width: 400, height: 260, font: 12, animate: 300, live: true, ...opts};
    const ch = {el: root, bins: null, lastFit: null, scales: null};
    let marked = new Set(), pickFns = [], fitKind = null, fitStyle = {}, curves = [], dragOn = false, sel = -1, pickAt = -1;
    const prevH = new Map(), shown = new Map();
    let tween = 0, built = null, pickEl = null;
    const id = 'ddc' + (++uid);
    const T = (x, y, s, a = {}, g) => { const {size, ...rest} = a; const e = mk('text', {x, y, 'font-size': size || o.font, ...rest}, g); e.textContent = s; return e; };
    const keep = (r, i) => !o.filter || o.filter(r, i);
    const lab = (key, given) => given != null ? given : key ? t.label(key) : '';
    const pr = (r, i) => (o.point ? o.point(r, i) : null) || {};
    // tick and text formats: xFormat / yFormat win; a 'year' column prints as 1985 (no comma) on whole-number ticks only
    const isYear = key => typeof key === 'string' && (t.columns[key] || {}).type === 'year';
    const fx = v => o.xFormat ? o.xFormat(v) : isYear(o.x) ? fmt(v, 0, {group: false}) : fmt(v);
    const fy = v => o.yFormat ? o.yFormat(v) : isYear(Array.isArray(o.y) ? o.y[0] : o.y) ? fmt(v, 0, {group: false}) : fmt(v);
    const wholeTicks = (key, n) => isYear(key) ? {...n, ticks: n.ticks.filter(v => Math.abs(v - Math.round(v)) < 1e-9)} : n;

    // the plotted points for scatter and line: [{i, x, y, shape, series, ring, faint}]
    function points(yKey = o.y, series = o.series || 1) {
      const out = [];
      t.rows.forEach((r, i) => {
        if (!keep(r, i)) return;
        const x = r[o.x], y = r[yKey];
        if (!isNum(x) || !isNum(y)) return;
        const p = pr(r, i);
        if (p.hidden) return;
        out.push({i, x, y, series: p.series || series, shape: p.shape || SHAPES[p.series || series], ring: p.ring, faint: !!p.faint});
      });
      return out;
    }
    function histBins() {
      const bw = typeof o.bins === 'object' && o.bins ? o.bins.width : (o.bins || null);
      const sets = [{t, x: o.x, filter: o.filter, style: o.style || (o.overlay ? 'outline' : 'fill'), series: o.series || 1, label: o.label || ''}];
      if (o.overlay) sets.push({style: 'fill', series: 2, label: '', x: o.x, ...o.overlay, t: o.overlay.table || t});
      const vals = sets.map(s => s.t.rows.map((r, i) => (!s.filter || s.filter(r, i)) && isNum(r[s.x]) ? [r[s.x], i] : null).filter(Boolean));
      const all = vals.flat().map(v => v[0]);
      let lo, hi, w = bw;
      if (!w) { const nn = nice(Math.min(...all), Math.max(...all), 8); w = nn.step; }
      const start = typeof o.bins === 'object' && o.bins && isNum(o.bins.start) ? o.bins.start : null;
      if (o.xDomain) [lo, hi] = o.xDomain;
      else {
        lo = start != null ? start : Math.floor((all.length ? Math.min(...all) : 0) / w) * w;
        hi = Math.max(lo + w, Math.floor((all.length ? Math.max(...all) : lo) / w) * w + w);
        if (start != null) while (lo > Math.min(...all)) lo -= w;
      }
      const nb = Math.max(1, Math.round((hi - lo) / w));
      const series = sets.map((s, k) => {
        const counts = new Array(nb).fill(0), rows = Array.from({length: nb}, () => []);
        for (const [v, i] of vals[k]) {
          const b = Math.floor((v - lo) / w + 1e-9);
          if (b >= 0 && b < nb) { counts[b]++; rows[b].push(i); }
        }
        const n = vals[k].length;
        return {...s, counts, rows, n, shares: counts.map(c => n ? c / n : 0)};
      });
      return {lo, hi, w, nb, series, edges: Array.from({length: nb + 1}, (_, k) => lo + k * w)};
    }

    function axisX(g, X, ticks, y0, x0, x1, labels) {
      mk('line', {x1: x0, x2: x1, y1: y0, y2: y0, class: 'dd-axis'}, g);
      for (const v of ticks) {
        const x = X(v);
        if (x < x0 - .5 || x > x1 + .5) continue;
        mk('line', {x1: x, x2: x, y1: y0, y2: y0 + 4, class: 'dd-axis'}, g);
        T(x, y0 + 4 + o.font, labels ? labels(v) : fx(v), {'text-anchor': 'middle'}, g);
      }
    }
    function axisY(g, Y, ticks, x0, x1, y0, y1, f = fy) {
      for (const v of ticks) {
        const y = Y(v);
        if (y < y1 - .5 || y > y0 + .5) continue;
        mk('line', {x1: x0, x2: x1, y1: y, y2: y, class: 'dd-grid'}, g);
        T(x0 - 5, y + o.font * .35, f(v), {'text-anchor': 'end'}, g);
      }
      mk('line', {x1: x0, x2: x0, y1: y0, y2: y1, class: 'dd-axis'}, g);
    }
    // extraTop: room for a legend row above the plot
    function frame(yTicksText, extraTop = 0) {
      const m = {l: 10, r: 10, t: 8, b: 10, ...(o.margin || {})};
      const tw = Math.max(2, ...yTicksText.map(s => s.length)) * o.font * .58 + 10;
      if (!(o.margin && o.margin.l != null)) m.l = Math.round(tw + 4);
      if (!(o.margin && o.margin.r != null)) m.r = Math.round(o.font * 1.3 + 2);   // room for half the last x tick label
      if (!(o.margin && o.margin.b != null)) m.b = Math.round(o.font * 2.9 + 6);
      if (!(o.margin && o.margin.t != null)) m.t = Math.round(o.font * 2.1 + 4 + extraTop);
      return {x0: m.l, x1: o.width - m.r, y0: o.height - m.b, y1: m.t};
    }
    function titles(g, F, xl, yl) {
      if (xl) T((F.x0 + F.x1) / 2, o.height - 4, xl, {'text-anchor': 'middle', class: 'dd-axlabel'}, g);
      if (yl) T(Math.max(2, F.x0 - 30), F.y1 - o.font * 1.05, yl, {'text-anchor': 'start', class: 'dd-axlabel'}, g);
    }
    const lin = (d0, d1, p0, p1) => v => p0 + (v - d0) / (d1 - d0 || 1) * (p1 - p0);

    function render() {
      cancelAnimationFrame(tween);
      // the pick layer is kept across redraws (never rebuilt under the pointer or the keyboard focus); the rest is redrawn
      const keepL = pickEl && pickEl.parentNode === root && (pickFns.length || dragOn) ? pickEl : null;
      for (const n of [...root.childNodes]) if (n !== keepL) n.remove();
      if (!keepL && pickEl) pickEl = null;
      if (root.parentNode === target && target === svg) {   // a chart that owns its <svg> sizes it in real pixels
        svg.setAttribute('width', o.width); svg.setAttribute('height', o.height); svg.setAttribute('viewBox', `0 0 ${o.width} ${o.height}`);
      }
      const g = mk('g', {class: 'dd-deco'}, root), mg = mk('g', {class: 'dd-marks', role: 'img'}, root);
      if (keepL) { root.insertBefore(g, keepL); root.insertBefore(mg, keepL); }
      const desc = mk('desc', {}, mg);
      let text = '';
      const type = o.type;
      if (type === 'histogram') text = drawHist(g, mg);
      else if (type === 'box') text = drawBox(g, mg);
      else if (type === 'bar') text = drawBar(g, mg);
      else if (type === 'dot') text = drawDot(g, mg);
      else text = drawXY(g, mg, type);
      desc.textContent = text;
      mg.setAttribute('aria-label', (o.title ? o.title + '. ' : '') + text.split('. ')[0]);
      ch.textAlt = (o.title ? o.title + '. ' : '') + text;
      if (pickFns.length || dragOn) pickLayer();
    }

    // ----- scatter and line -----
    function drawXY(g, mg, type) {
      const ys = Array.isArray(o.y) ? o.y : [o.y];
      const sets = ys.map((k, j) => ({key: k, pts: points(k, (o.series || 1) + j)}));
      if (type === 'line') sets.forEach(s => s.pts.sort((a, b) => a.x - b.x));
      const all = sets.flatMap(s => s.pts), shownPts = all.filter(p => !p.faint || o.domainFaint !== false);
      const nx = wholeTicks(o.x, o.xDomain ? {lo: o.xDomain[0], hi: o.xDomain[1], ticks: nice(o.xDomain[0], o.xDomain[1], 6).ticks} : nice(Math.min(...shownPts.map(p => p.x)), Math.max(...shownPts.map(p => p.x)), 6));
      const ny = wholeTicks(ys[0], o.yDomain ? {lo: o.yDomain[0], hi: o.yDomain[1], ticks: nice(o.yDomain[0], o.yDomain[1], 5).ticks} : nice(Math.min(...shownPts.map(p => p.y)), Math.max(...shownPts.map(p => p.y)), 5));
      const F = frame(ny.ticks.map(fy));
      const X = lin(nx.lo, nx.hi, F.x0, F.x1), Y = lin(ny.lo, ny.hi, F.y0, F.y1);
      ch.scales = {x: X, y: Y, frame: F, xDomain: [nx.lo, nx.hi], yDomain: [ny.lo, ny.hi]};
      for (const b of o.bands || []) {
        const a = clamp(X(b.from), F.x0, F.x1), c = clamp(X(b.to), F.x0, F.x1);
        mk('rect', {x: a, y: F.y1, width: Math.max(0, c - a), height: F.y0 - F.y1, fill: b.color || 'var(--dd-grid)'}, g);
        if (b.label) T(a + 3, F.y1 + o.font, b.label, {size: o.font - 1}, g);
      }
      axisY(g, Y, ny.ticks, F.x0, F.x1, F.y0, F.y1);
      axisX(g, X, nx.ticks, F.y0, F.x0, F.x1);
      titles(g, F, lab(o.x, o.xLabel), lab(ys.length === 1 ? ys[0] : null, o.yLabel));
      const clip = mk('clipPath', {id: id + 'c'}, g); mk('rect', {x: F.x0, y: F.y1 - 6, width: F.x1 - F.x0 + 6, height: F.y0 - F.y1 + 6}, clip);
      const r = o.pointSize || (coarse() ? 5 : 3.5);
      // fit and curves under the points
      ch.lastFit = null;
      if (fitKind && sets[0]) {
        const P = sets[0].pts.filter(p => !p.faint);
        const res = fit(fitKind, P.map(p => p.x), P.map(p => p.y));
        ch.lastFit = res;
        if (res.n >= 2) curve1(mg, res.f, X, Y, nx, F, {color: 'var(--dd-text)', dash: '6 4', width: 2, ...fitStyle});
      }
      for (const c of curves) curve1(mg, c.f, X, Y, nx, F, c.style || {});
      const lines = [];
      sets.forEach((s, j) => {
        const sr = (o.series || 1) + j;
        if (type === 'line' && s.pts.length > 1)
          mk('path', {d: s.pts.map((p, k) => (k ? 'L' : 'M') + X(p.x).toFixed(1) + ' ' + Y(p.y).toFixed(1)).join(''), fill: 'none',
            stroke: col(sr), 'stroke-width': 2.2, 'stroke-dasharray': DASH[sr] || null, 'stroke-linejoin': 'round', 'clip-path': `url(#${id}c)`}, mg);
        const faint = [], solid = [];
        s.pts.forEach(p => (p.faint ? faint : solid).push(p));
        for (const p of faint) shape(mg, p.shape, X(p.x), Y(p.y), r, {fill: 'none', stroke: p.ring || col(p.series), 'stroke-width': 1.2, opacity: .55});
        for (const p of solid) {
          const e = shape(mg, p.shape, X(p.x), Y(p.y), r, {fill: col(p.series), stroke: p.shape === 'cross' ? col(p.series) : 'var(--dd-bgline, rgba(0,0,0,.35))', 'stroke-width': p.shape === 'cross' ? 2.2 : .8});
          e.dataset.i = p.i;
          if (p.ring) mk('circle', {cx: X(p.x), cy: Y(p.y), r: r + 3, fill: 'none', stroke: p.ring, 'stroke-width': 1.8}, mg);
        }
        for (const p of s.pts) if (marked.has(p.i)) mk('circle', {cx: X(p.x), cy: Y(p.y), r: r + 4.5, fill: 'none', stroke: 'var(--dd-ring)', 'stroke-width': 2.4}, mg);
        lines.push(`${lab(s.key)}: ` + s.pts.filter(p => !p.faint).map(p => `(${fx(p.x)}, ${fy(p.y)})`).join(', '));
      });
      if (sel >= 0) { const p = all.find(q => q.i === sel); if (p) mk('circle', {cx: X(p.x), cy: Y(p.y), r: r + 7, class: 'dd-focus', fill: 'none', stroke: 'var(--focus,#e0662a)', 'stroke-width': 2.5}, mg); }
      const n = all.filter(p => !p.faint).length;
      let head = `${type === 'line' ? 'Line chart' : 'Scatter plot'} of ${ys.map(k => lab(k)).join(' and ')} against ${lab(o.x, o.xLabel)}, ${n} points`;
      if (ch.lastFit && ch.lastFit.n >= 2) head += `, ${ch.lastFit.kind} fit ${ch.lastFit.eq}` + (ch.lastFit.kind === 'linear' ? `, r = ${fmt(ch.lastFit.r)}` : `, r squared ${fmt(ch.lastFit.r2)}`);
      return head + '. ' + lines.join('. ');
    }
    function curve1(g, f, X, Y, nx, F, s) {
      let d = '', pen = false;
      const N = 120;
      for (let k = 0; k <= N; k++) {
        const v = nx.lo + (nx.hi - nx.lo) * k / N, y = f(v);
        if (!isNum(y)) { pen = false; continue; }
        const py = Y(y);
        if (py < F.y1 - 2000 || py > F.y0 + 2000) { pen = false; continue; }
        d += (pen ? 'L' : 'M') + X(v).toFixed(1) + ' ' + py.toFixed(1); pen = true;
      }
      if (d) mk('path', {d, fill: 'none', stroke: s.color || 'var(--dd-text)', 'stroke-width': s.width || 2, 'stroke-dasharray': s.dash || null, 'clip-path': `url(#${id}c)`}, g);
    }

    // ----- histogram (one series, or two with overlay) -----
    function drawHist(g, mg) {
      const H = histBins(); ch.bins = H;
      const val = s => o.share ? s.shares : s.counts;
      const top = Math.max(...H.series.flatMap(s => val(s)), o.share ? .05 : 1);
      const ny = o.yDomain ? {lo: o.yDomain[0], hi: o.yDomain[1], ticks: nice(o.yDomain[0], o.yDomain[1], 4).ticks} : nice(0, top, 4);
      const yf = v => o.share ? fmt(v * 100, 0) + '%' : fmt(v);
      const F = frame(ny.ticks.map(yf));
      const X = lin(H.lo, H.hi, F.x0, F.x1), Y = lin(ny.lo, ny.hi, F.y0, F.y1);
      ch.scales = {x: X, y: Y, frame: F, xDomain: [H.lo, H.hi], yDomain: [ny.lo, ny.hi]};
      axisY(g, Y, ny.ticks, F.x0, F.x1, F.y0, F.y1, yf);
      const step = Math.max(1, Math.ceil(H.nb / Math.max(2, Math.floor((F.x1 - F.x0) / (o.font * 3)))));
      axisX(g, X, H.edges.filter((_, k) => k % step === 0), F.y0, F.x0, F.x1);
      titles(g, F, lab(o.x, o.xLabel), o.yLabel != null ? o.yLabel : o.share ? 'Share' : 'Count');
      // fill series first, outlines on top, so an outline is never hidden
      const order = H.series.map((s, k) => k).sort((a, b) => (H.series[a].style === 'fill' ? 0 : 1) - (H.series[b].style === 'fill' ? 0 : 1));
      const bars = [];
      const gap = H.series.length > 1 ? 0 : 1;
      for (const k of order) {
        const s = H.series[k];
        val(s).forEach((v, b) => {
          const x = X(H.edges[b]) + gap / 2, w = Math.max(1, X(H.edges[b + 1]) - X(H.edges[b]) - gap), key = k + ':' + b;
          const isOut = s.style === 'outline';
          const e = mk('rect', {x, width: w, fill: isOut ? 'none' : col(s.series), 'fill-opacity': isOut ? null : (s.faded ? .3 : .85), opacity: s.faded ? .6 : null,
            stroke: isOut ? col(s.series) : null, 'stroke-width': isOut ? 2.2 : null}, mg);
          const markedBin = marked.size && s === H.series[0] && s.rows[b].some(i => marked.has(i));
          // tops: the series shape on top of each bar, so the series differ by shape as well as by fill and color
          const top = o.tops && v > 0 ? shape(mg, SHAPES[s.series], 0, 0, Math.min(4.5, w / 3), {fill: isOut ? 'var(--dd-bg-solid, var(--paper, #fff))' : col(s.series), stroke: col(s.series), 'stroke-width': 1.6}) : null;
          bars.push({e, key, to: Y(0) - Y(v), y0: Y(0), isOut, v, markedBin, x, w, top});
        });
      }
      if (pickAt >= 0 && pickAt < H.nb) mk('rect', {x: X(H.edges[pickAt]) - 1, y: F.y1, width: X(H.edges[pickAt + 1]) - X(H.edges[pickAt]) + 2, height: F.y0 - F.y1, fill: 'none', stroke: 'var(--dd-ring)', 'stroke-width': 2, 'stroke-dasharray': '4 3'}, mg);
      for (const b of bars) if (b.markedBin && b.v > 0) b.ring = mk('rect', {x: b.x - 1, width: b.w + 2, fill: 'none', stroke: 'var(--dd-ring)', 'stroke-width': 2.5}, mg);
      const set = (b, h) => { b.e.setAttribute('y', (b.y0 - h).toFixed(1)); b.e.setAttribute('height', Math.max(0, h).toFixed(1)); shown.set(b.key, h); if (b.top) b.top.setAttribute('transform', `translate(${(b.x + b.w / 2).toFixed(1)} ${(b.y0 - h - (b.isOut ? 0 : 0)).toFixed(1)})`); if (b.ring) { b.ring.setAttribute('y', (b.y0 - h - 1).toFixed(1)); b.ring.setAttribute('height', Math.max(0, h + 2).toFixed(1)); } };
      const ms = calm() ? 0 : (o.animate || 0);
      if (!ms) bars.forEach(b => set(b, b.to));
      else {
        const from = bars.map(b => shown.has(b.key) ? shown.get(b.key) : 0), t0 = performance.now();
        const stepF = now => {
          const u = Math.min(1, (now - t0) / ms), e = 1 - Math.pow(1 - u, 3);
          bars.forEach((b, k) => set(b, from[k] + (b.to - from[k]) * e));
          if (u < 1) tween = requestAnimationFrame(stepF);
        };
        bars.forEach((b, k) => set(b, from[k]));
        tween = requestAnimationFrame(stepF);
      }
      for (const m of o.marks || []) markLine(mg, m, H.series[0], X, F);
      const unit = o.share ? 'percent' : 'count';
      return `Histogram of ${lab(o.x, o.xLabel)} in bins of ${fmt(H.w)}` + H.series.map(s => `. ${s.label || 'Series ' + s.series} (${s.n} ${s.n === 1 ? 'value' : 'values'}, ${unit}): ` +
        H.edges.slice(0, -1).map((e, b) => `${fx(e)} to ${fx(e + H.w)}: ${o.share ? fmt(s.shares[b] * 100, 0) : s.counts[b]}`).join(', ')).join('');
    }
    function markLine(g, m, s, X, F) {
      const st = stats(s.t.rows.filter((r, i) => !s.filter || s.filter(r, i)).map(r => r[s.x]));
      const v = m === 'median' ? st.median : st.mean;
      if (!isNum(v)) return;
      const x = X(v);
      mk('line', {x1: x, x2: x, y1: F.y1, y2: F.y0, stroke: 'var(--dd-text)', 'stroke-width': 2, 'stroke-dasharray': m === 'median' ? null : '5 4'}, g);
      T(x + 3, F.y1 + o.font, `${m} ${fx(v)}`, {size: o.font - 1}, g);
    }

    // ----- box plots, one per group -----
    function drawBox(g, mg) {
      const groups = o.groupBy ? (o.groups || t.count(o.groupBy, keep).map(c => c.value)) : [null];
      const S = groups.map(gv => ({gv, st: stats(t.rows.filter((r, i) => keep(r, i) && (gv == null || r[o.groupBy] === gv)).map(r => r[o.x])),
        rows: t.rows.map((r, i) => keep(r, i) && (gv == null || r[o.groupBy] === gv) && isNum(r[o.x]) ? i : -1).filter(i => i >= 0)}));
      const allv = S.filter(s => s.st.n).flatMap(s => [s.st.min, s.st.max]);
      const nx = o.xDomain ? {lo: o.xDomain[0], hi: o.xDomain[1], ticks: nice(o.xDomain[0], o.xDomain[1], 6).ticks} : nice(Math.min(...allv), Math.max(...allv), 6);
      const names = groups.map(gv => gv == null ? '' : String((o.groupLabels && o.groupLabels[gv]) || gv));
      const m = {...(o.margin || {})};
      if (m.l == null) m.l = Math.round(Math.max(1, ...names.map(s => s.length)) * o.font * .56 + 14);
      const F = {x0: m.l, x1: o.width - (m.r != null ? m.r : 10), y0: o.height - (m.b != null ? m.b : Math.round(o.font * 2.9 + 6)), y1: m.t != null ? m.t : 6};
      const X = lin(nx.lo, nx.hi, F.x0, F.x1);
      ch.scales = {x: X, frame: F, xDomain: [nx.lo, nx.hi]};
      for (const v of nx.ticks) { const x = X(v); if (x >= F.x0 - .5 && x <= F.x1 + .5) mk('line', {x1: x, x2: x, y1: F.y1, y2: F.y0, class: 'dd-grid'}, g); }
      axisX(g, X, nx.ticks, F.y0, F.x0, F.x1);
      if (o.xLabel !== '') T((F.x0 + F.x1) / 2, o.height - 4, lab(o.x, o.xLabel), {'text-anchor': 'middle', class: 'dd-axlabel'}, g);
      const rowH = (F.y0 - F.y1) / S.length;
      ch.boxes = [];
      S.forEach((s, k) => {
        const sr = (o.series || 1) + (o.groupBy && o.colorGroups ? k : 0), cy = F.y1 + rowH * (k + .5), h = Math.min(rowH * .56, 34);
        ch.boxes.push({group: s.gv, y0: F.y1 + rowH * k, y1: F.y1 + rowH * (k + 1), stats: s.st, rows: s.rows});
        if (names[k]) T(F.x0 - 8, cy + o.font * .35, names[k], {'text-anchor': 'end'}, g);
        if (!s.st.n) return;
        const st = s.st, c = col(sr);
        mk('line', {x1: X(st.whiskerLo), x2: X(st.q1), y1: cy, y2: cy, stroke: c, 'stroke-width': 2}, mg);
        mk('line', {x1: X(st.q3), x2: X(st.whiskerHi), y1: cy, y2: cy, stroke: c, 'stroke-width': 2}, mg);
        for (const w of [st.whiskerLo, st.whiskerHi]) mk('line', {x1: X(w), x2: X(w), y1: cy - h / 4, y2: cy + h / 4, stroke: c, 'stroke-width': 2}, mg);
        mk('rect', {x: X(st.q1), y: cy - h / 2, width: Math.max(1, X(st.q3) - X(st.q1)), height: h, fill: c, 'fill-opacity': .22, stroke: c, 'stroke-width': 2}, mg);
        mk('line', {x1: X(st.median), x2: X(st.median), y1: cy - h / 2, y2: cy + h / 2, stroke: c, 'stroke-width': 3}, mg);
        if ((o.marks || []).includes('mean')) shape(mg, 'diamond', X(st.mean), cy, 4, {fill: 'var(--dd-text)'});
        for (const v of st.outliers) shape(mg, SHAPES[sr], X(v), cy, 3.2, {fill: 'none', stroke: c, 'stroke-width': 1.5});
        if (marked.size && s.rows.some(i => marked.has(i))) mk('rect', {x: X(st.min) - 6, y: cy - h / 2 - 5, width: X(st.max) - X(st.min) + 12, height: h + 10, rx: 6, fill: 'none', stroke: 'var(--dd-ring)', 'stroke-width': 2}, mg);
      });
      if (pickAt >= 0 && ch.boxes[pickAt]) { const b = ch.boxes[pickAt]; mk('rect', {x: 2, y: b.y0 + 1, width: o.width - 4, height: b.y1 - b.y0 - 2, rx: 6, fill: 'none', stroke: 'var(--dd-ring)', 'stroke-width': 2, 'stroke-dasharray': '4 3'}, mg); }
      return (lab(o.x, o.xLabel) ? `Box plot of ${lab(o.x, o.xLabel)}` : 'Box plot') +  // no empty "of" when xLabel is ''
        S.map((s, k) => `. ${names[k] || 'All'} (${s.st.n} ${s.st.n === 1 ? 'value' : 'values'}): minimum ${fx(s.st.min)}, first quartile ${fx(s.st.q1)}, median ${fx(s.st.median)}, third quartile ${fx(s.st.q3)}, maximum ${fx(s.st.max)}` + (s.st.outliers.length ? `, outliers ${s.st.outliers.map(v => fx(v)).join(', ')}` : '')).join('');
    }

    // ----- bar chart: a value per row (y given), or counts of each value of x (grouped by groupBy) -----
    function drawBar(g, mg) {
      let cats, groups = [null], val;
      if (o.y) {
        const rows = t.rows.map((r, i) => [r, i]).filter(([r, i]) => keep(r, i));
        cats = rows.map(([r]) => r[o.x]);
        val = (c, gv, k) => rows[k][0][o.y];
      } else {
        cats = t.count(o.x, keep).map(c => c.value);
        if (o.groupBy) groups = o.groups || t.count(o.groupBy, keep).map(c => c.value);
        const tab = o.groupBy ? t.crosstab(o.x, o.groupBy, keep) : null, cnt = new Map(t.count(o.x, keep).map(c => [c.value, c.n]));
        val = (c, gv) => o.groupBy ? tab.n(c, gv) : cnt.get(c) || 0;
      }
      const vals = cats.flatMap((c, k) => groups.map(gv => val(c, gv, k))).filter(isNum);
      const ny = o.yDomain ? {lo: o.yDomain[0], hi: o.yDomain[1], ticks: nice(o.yDomain[0], o.yDomain[1], 4).ticks} : nice(Math.min(0, ...vals), Math.max(1, ...vals), 4);
      // grouped bars differ by color, dash, a shape on each bar top and a legend row, never by color alone
      const gname = gv => gv == null ? '' : String((o.groupLabels && o.groupLabels[gv]) || gv);
      const legend = groups.length > 1;
      const F = frame(ny.ticks.map(fy), legend ? Math.round(o.font * 1.5 + 4) : 0);
      const Y = lin(ny.lo, ny.hi, F.y0, F.y1), slot = (F.x1 - F.x0) / Math.max(1, cats.length);
      if (legend) {
        let lx = F.x0; const ly = Math.round(o.font * .9 + 4);
        groups.forEach((gv, j) => {
          const sr = (o.series || 1) + j;
          mk('rect', {x: lx, y: ly - o.font * .45, width: 14, height: o.font * .9, fill: col(sr), 'fill-opacity': .85, stroke: col(sr), 'stroke-dasharray': DASH[sr] || null}, g);
          shape(g, SHAPES[sr], lx + 7, ly - o.font * .45 - 1, 4, {fill: col(sr), stroke: 'var(--dd-bgline, rgba(0,0,0,.35))', 'stroke-width': .8});
          T(lx + 20, ly + o.font * .35, gname(gv), {}, g);
          lx += 20 + gname(gv).length * o.font * .58 + 16;
        });
      }
      ch.scales = {y: Y, frame: F, slot, cats};
      axisY(g, Y, ny.ticks, F.x0, F.x1, F.y0, F.y1);
      mk('line', {x1: F.x0, x2: F.x1, y1: Y(0), y2: Y(0), class: 'dd-axis'}, g);
      const bw = slot * .7 / groups.length;
      ch.barRects = [];
      cats.forEach((c, k) => {
        T(F.x0 + slot * (k + .5), F.y0 + 4 + o.font, String(c), {'text-anchor': 'middle'}, g);
        groups.forEach((gv, j) => {
          const v = val(c, gv, k); if (!isNum(v)) return;
          const sr = (o.series || 1) + j, x = F.x0 + slot * k + slot * .15 + bw * j;
          mk('rect', {x, y: Math.min(Y(v), Y(0)), width: bw, height: Math.abs(Y(0) - Y(v)), fill: col(sr), 'fill-opacity': .85,
            stroke: col(sr), 'stroke-width': 1, 'stroke-dasharray': DASH[sr] || null}, mg);
          if (legend && v !== 0) shape(mg, SHAPES[sr], x + bw / 2, Math.min(Y(v), Y(0)), Math.min(4.5, bw / 3), {fill: col(sr), stroke: 'var(--dd-bgline, rgba(0,0,0,.35))', 'stroke-width': .8});
          ch.barRects.push({cat: c, group: gv, k, j, x, w: bw, v});
        });
      });
      if (pickAt >= 0 && ch.barRects[pickAt]) { const b = ch.barRects[pickAt]; mk('rect', {x: b.x - 3, y: F.y1, width: b.w + 6, height: F.y0 - F.y1, fill: 'none', stroke: 'var(--dd-ring)', 'stroke-width': 2, 'stroke-dasharray': '4 3'}, mg); }
      titles(g, F, lab(o.x, o.xLabel), o.yLabel != null ? o.yLabel : o.y ? lab(o.y) : 'Count');
      return `Bar chart of ${o.y ? lab(o.y) : 'counts'} by ${lab(o.x, o.xLabel)}. ` + cats.map((c, k) => `${c}: ` + groups.map(gv => (gv == null ? '' : gname(gv) + ' ') + fy(val(c, gv, k))).join(', ')).join('. ');
    }

    // ----- dot plot: one dot per value, stacked (values rounded to bins when given) -----
    function drawDot(g, mg) {
      const w = typeof o.bins === 'object' && o.bins ? o.bins.width : o.bins;
      const pts = [];
      t.rows.forEach((r, i) => { if (keep(r, i) && isNum(r[o.x])) pts.push({i, v: w ? Math.round(r[o.x] / w) * w : r[o.x], p: pr(r, i)}); });
      pts.sort((a, b) => a.v - b.v || a.i - b.i);
      const nx = o.xDomain ? {lo: o.xDomain[0], hi: o.xDomain[1], ticks: nice(o.xDomain[0], o.xDomain[1], 6).ticks} : nice(Math.min(...pts.map(p => p.v)), Math.max(...pts.map(p => p.v)), 6);
      const F = frame([]); F.x0 = (o.margin && o.margin.l != null) ? o.margin.l : 14;
      const X = lin(nx.lo, nx.hi, F.x0, F.x1);
      const stack = new Map(); pts.forEach(p => { p.k = stack.get(p.v) || 0; stack.set(p.v, p.k + 1); });
      const most = Math.max(1, ...stack.values()), r = Math.max(2.5, Math.min(o.pointSize || (coarse() ? 7 : 6), (F.y0 - F.y1) / most / 2 - 1));
      ch.scales = {x: X, frame: F, xDomain: [nx.lo, nx.hi], r};
      axisX(g, X, nx.ticks, F.y0, F.x0, F.x1);
      titles(g, F, lab(o.x, o.xLabel), '');
      for (const p of pts) {
        const sr = p.p.series || o.series || 1, x = X(p.v), y = F.y0 - r - 2 - p.k * (2 * r + 1.5);
        p.x = x; p.y = y;
        const e = shape(mg, p.p.shape || SHAPES[sr], x, y, r, p.p.faint ? {fill: 'none', stroke: col(sr), opacity: .55} : {fill: col(sr)});
        e.dataset.i = p.i;
        if (marked.has(p.i)) mk('circle', {cx: x, cy: y, r: r + 3, fill: 'none', stroke: 'var(--dd-ring)', 'stroke-width': 2}, mg);
        if (p.i === sel) mk('circle', {cx: x, cy: y, r: r + 5, fill: 'none', stroke: 'var(--focus,#e0662a)', 'stroke-width': 2.5}, mg);
      }
      ch.dots = pts;
      for (const m of o.marks || []) markLine(mg, m, {t, x: o.x, filter: o.filter}, X, F);
      return `Dot plot of ${lab(o.x, o.xLabel)}, ${pts.length} values: ` + pts.map(p => fx(p.v)).join(', ');  // fx: years plain, xFormat honored (exit check round 2, item 15)
    }

    // ----- picking and dragging: one focusable target over the whole plot, so even narrow bins meet the 44 px
    // target rule. Pointer: tap a bin, bar, box or point. Keys: arrows step, Enter or Space picks, Escape clears.
    function units() {
      const tp = o.type;
      if (tp === 'histogram') return (ch.bins || {nb: 0}).nb;
      if (tp === 'box') return (ch.boxes || []).length;
      if (tp === 'bar') return (ch.barRects || []).length;
      return 0;
    }
    function infoAt(k) {
      const tp = o.type;
      if (tp === 'histogram') { const H = ch.bins, s = H.series[0]; return {type: 'bin', bin: k, lo: H.edges[k], hi: H.edges[k + 1], n: s.counts[k], rows: s.rows[k].slice(), series: H.series.map(x => ({n: x.counts[k], share: x.shares[k]}))}; }
      if (tp === 'box') { const b = ch.boxes[k]; return {type: 'box', group: b.group, stats: b.stats, rows: b.rows.slice()}; }
      if (tp === 'bar') { const b = ch.barRects[k]; return {type: 'bar', cat: b.cat, group: b.group, value: b.v, rows: t.rows.map((r, i) => keep(r, i) && r[o.x] === b.cat && (b.group == null || r[o.groupBy] === b.group) ? i : -1).filter(i => i >= 0)}; }
      return null;
    }
    function nearestPoint(px, py) {
      const P = o.type === 'dot' ? (ch.dots || []).map(p => ({i: p.i, x: p.x, y: p.y})) : points().filter(p => !p.faint).map(p => ({i: p.i, x: ch.scales.x(p.x), y: ch.scales.y(p.y)}));
      let best = null, bd = (coarse() ? 24 : 14) ** 2;
      for (const p of P) { const d = (p.x - px) ** 2 + (p.y - py) ** 2; if (d < bd) { bd = d; best = p; } }
      return best;
    }
    function local(e) {
      const pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY;
      const m = root.getScreenCTM(); return m ? pt.matrixTransform(m.inverse()) : {x: 0, y: 0};
    }
    function pickLayer() {
      const F0 = ch.scales && ch.scales.frame; if (!F0) return;
      const tp0 = o.type, xy0 = tp0 === 'scatter' || tp0 === 'line' || tp0 === 'dot';
      const label = (o.title || 'Chart') + (xy0 ? (dragOn ? ': arrow keys move the chosen point, Page Up and Page Down choose another' : ': Enter picks the point nearest the middle')
        : tp0 === 'box' ? ': up and down arrows choose, Enter picks, Escape clears' : ': left and right arrows choose, Enter picks, Escape clears');
      const x0 = tp0 === 'box' ? 0 : F0.x0, y0 = F0.y1, w = (tp0 === 'box' ? o.width : F0.x1 - F0.x0), h = F0.y0 - F0.y1;
      if (pickEl) {                                  // already there: only its size, label and drag class change
        pickEl.setAttribute('class', 'dd-pick' + (dragOn ? ' dd-drag' : '')); pickEl.setAttribute('aria-label', label);
        const [r1, r2] = pickEl.children;
        for (const [k, v] of Object.entries({x: x0, y: y0, width: w, height: h})) r1.setAttribute(k, v);
        for (const [k, v] of Object.entries({x: x0 + 1.5, y: y0 + 1.5, width: Math.max(0, w - 3), height: Math.max(0, h - 3)})) r2.setAttribute(k, v);
        return;
      }
      const L = pickEl = mk('g', {class: 'dd-pick' + (dragOn ? ' dd-drag' : ''), tabindex: 0, role: 'group', 'aria-roledescription': 'chart', 'aria-label': label}, root);
      mk('rect', {x: x0, y: y0, width: w, height: h, fill: 'transparent'}, L);
      mk('rect', {x: x0 + 1.5, y: y0 + 1.5, width: Math.max(0, w - 3), height: Math.max(0, h - 3), rx: 4, class: 'dd-focus'}, L);
      L.addEventListener('pointerdown', e => {
        const F = ch.scales.frame, tp = o.type, xy = tp === 'scatter' || tp === 'line' || tp === 'dot';
        const p = local(e);
        if (xy) {
          const q = nearestPoint(p.x, p.y);
          if (!q) return;
          sel = q.i;
          if (dragOn) startDrag(e, q.i);
          fire({type: 'point', i: q.i, row: t.rows[q.i]});
          return;
        }
        let k = -1;
        if (tp === 'histogram') k = Math.floor((p.x - F.x0) / (F.x1 - F.x0) * ch.bins.nb);
        else if (tp === 'box') k = ch.boxes.findIndex(b => p.y >= b.y0 && p.y < b.y1);
        else if (tp === 'bar') k = ch.barRects.findIndex(b => p.x >= b.x - 4 && p.x <= b.x + b.w + 4);
        if (k < 0 || k >= units()) return;
        pickAt = k; fire(infoAt(k));
      });
      L.addEventListener('keydown', e => {
        const xy = o.type === 'scatter' || o.type === 'line' || o.type === 'dot';
        if (xy) return keyPoint(e);
        const n = units(); if (!n) return;
        const back = o.type === 'box' ? 'ArrowUp' : 'ArrowLeft', fwd = o.type === 'box' ? 'ArrowDown' : 'ArrowRight';
        if (e.key === back || e.key === fwd) { e.preventDefault(); pickAt = clamp((pickAt < 0 ? (e.key === fwd ? -1 : n) : pickAt) + (e.key === fwd ? 1 : -1), 0, n - 1); render(); }
        else if ((e.key === 'Enter' || e.key === ' ') && pickAt >= 0) { e.preventDefault(); fire(infoAt(pickAt)); }
        else if (e.key === 'Escape') { pickAt = -1; render(); fire(null); }
      });
    }
    function fire(info) { pickFns.forEach(f => f(info)); if (o.type === 'histogram' || o.type === 'box' || o.type === 'bar') render(); }
    function keyPoint(e) {
      const P = (o.type === 'dot' ? (ch.dots || []).map(p => p.i) : points().filter(p => !p.faint).map(p => p.i));
      if (!P.length) return;
      if (e.key === 'PageDown' || e.key === 'PageUp') {
        e.preventDefault(); const k = P.indexOf(sel); sel = P[(k + (e.key === 'PageDown' ? 1 : P.length - 1) + (k < 0 ? 1 : 0)) % P.length];
        render(); return;
      }
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); if (sel < 0) sel = P[0]; fire({type: 'point', i: sel, row: t.rows[sel]}); render(); return; }
      if (!dragOn || sel < 0) return;
      const st = o.dragStep || {};
      const dx = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0, dy = e.key === 'ArrowUp' ? 1 : e.key === 'ArrowDown' ? -1 : 0;
      if (!dx && !dy) return;
      e.preventDefault();
      const r = t.rows[sel];
      t.batch(() => {
        if (dx) t.set(sel, o.x, +(r[o.x] + dx * (st.x || niceStep('x'))).toFixed(10));
        if (dy && o.type !== 'dot') t.set(sel, o.y, +(r[o.y] + dy * (st.y || niceStep('y'))).toFixed(10));
      });
    }
    const niceStep = ax => { const d = ax === 'x' ? ch.scales.xDomain : ch.scales.yDomain; return d ? nice(d[0], d[1], 5).step / 10 : 1; };
    // the drag listens on the window, so a move outside the plot still counts; the pick layer itself is kept across redraws
    function startDrag(e, i) {
      e.preventDefault();
      const st = o.dragStep || {}, sx = ch.scales, F = sx.frame;
      const inv = (p, d0, d1, a, b) => d0 + (p - a) / (b - a) * (d1 - d0);
      const snap = (v, s) => s ? +(Math.round(v / s) * s).toFixed(10) : +v.toFixed(2);
      const move = ev => {
        const p = local(ev);
        t.batch(() => {
          t.set(i, o.x, snap(inv(p.x, sx.xDomain[0], sx.xDomain[1], F.x0, F.x1), st.x));
          if (o.type !== 'dot' && sx.yDomain) t.set(i, o.y, snap(inv(p.y, sx.yDomain[0], sx.yDomain[1], F.y0, F.y1), st.y));
        });
      };
      const up = () => { removeEventListener('pointermove', move); removeEventListener('pointerup', up); removeEventListener('pointercancel', up); };
      addEventListener('pointermove', move); addEventListener('pointerup', up); addEventListener('pointercancel', up);
    }

    // ----- public -----
    ch.update = o2 => { if (o2) Object.assign(o, o2); render(); return ch; };
    ch.resize = (w, h) => { o.width = w; o.height = h; render(); return ch; };
    ch.highlight = s => { marked = s == null ? new Set() : new Set(typeof s === 'number' ? [s] : [...s]); render(); return ch; };
    ch.onPoint = fn => { pickFns.push(fn); render(); return ch; };
    ch.pick = k => { pickAt = k == null ? -1 : k; render(); return ch; };
    ch.fit = (kind, st = {}) => { fitKind = kind || null; fitStyle = st; render(); return ch.lastFit; };
    ch.curve = (f, st = {}) => { if (f == null) curves = []; else curves.push({f, style: st}); render(); return ch; };
    ch.drag = (on = true) => { dragOn = !!on; render(); return ch; };
    ch.text = () => ch.textAlt;
    ch.options = o;
    let off = o.live ? t.on('change', () => render()) : null;
    let off2 = o.live && o.overlay && o.overlay.table && o.overlay.table !== t ? o.overlay.table.on('change', () => render()) : null;
    ch.destroy = () => { if (off) off(); if (off2) off2(); cancelAnimationFrame(tween); root.textContent = ''; };
    render();
    return ch;
  }

  return {version, DataTable, Chart, stats, linreg, fit, nice, fmt, shape, SHAPES, DASH, mk};
})();
const DataTable = DataDesk.DataTable, Chart = DataDesk.Chart;
