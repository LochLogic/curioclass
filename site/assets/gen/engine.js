// Curio Class Worksheet Generators: the shared engine (docs/WORKSHEETS-PLAN.md, Generators).
// A generator is one file, site/assets/gen/<id>.js, that calls Gen.add(id, def). This file gives it a seeded random
// source, HTML helpers that draw in the same ws-* style as the built worksheets, and (in a browser) the page around it:
// the settings form, New sheet, the student/key switch, Print, and a URL that reprints the same sheet.
// It also runs under Node for scripts/check_generators.mjs, which makes thousands of sheets and checks every one.
//
// def = {
//   title, type,                 shown on the sheet (type is the worksheet type, like "Practice")
//   data: 'words',               optional: fetch /closet/worksheets/make/<data>.json first and pass it to make()
//   fields: [{id, label, type: 'select'|'check'|'number'|'text', options: [[value, label]] or (v, d) => [...],
//             def, min, max, show: v => bool}],
//   make(v, r, d) -> {title, ican, directions, minutes, materials, parts: [[name, html]], mistakes, notes,
//                     items: [{q, a, ...}]}   items: one per question, for the checker (q = question text, a = answer)
//   verify(sheet, v, d) -> [problem strings]   optional: re-work every item independently and report any mismatch
//   css: '...'                   optional: styles only this generator needs (added to the page once)
//   fixed: true, noKey: true     optional: for layout generators whose sheet does not change with the code or has no answers
// }
(function (G) {
'use strict';
const Gen = G.Gen = { defs: {} };
Gen.add = (id, def) => { Gen.defs[id] = def; };

/* ---------- seeded random ---------- */
const SEEDCH = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
Gen.newSeed = () => Array.from({ length: 5 }, () => SEEDCH[Math.floor(Math.random() * SEEDCH.length)]).join('');
Gen.rng = seed => {
  let h = 2166136261;
  for (const c of String(seed)) h = Math.imul(h ^ c.charCodeAt(0), 16777619);
  let a = h >>> 0;
  const next = () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  const r = {
    next,
    int: (lo, hi) => lo + Math.floor(next() * (hi - lo + 1)),     // inclusive
    pick: arr => arr[Math.floor(next() * arr.length)],
    chance: p => next() < p,
    shuffle: arr => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(next() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; },
    sample: (arr, n) => r.shuffle(arr).slice(0, n),
    // n distinct items from maker(), compared by key(item); gives up after many tries and returns what it has
    distinct(n, maker, key = x => JSON.stringify(x)) {
      const out = [], seen = new Set();
      for (let tries = 0; out.length < n && tries < n * 60; tries++) {
        const x = maker(); if (x == null) continue;
        const k = key(x); if (!seen.has(k)) { seen.add(k); out.push(x); }
      }
      return out;
    },
  };
  return r;
};

/* ---------- html helpers (same classes as scripts/worksheets.py, styled in curio.css) ---------- */
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const H = Gen.h = {
  esc,
  // a blank line on the student copy that shows the answer on the key; em = minimum width
  blank: (ans, em) => `<span class="ws-blank" style="min-width:${(em || Math.max(2.2, Math.min(10, 0.62 * String(ans).length + 1.4))).toFixed(1)}em"><span class="ws-ans">${esc(ans)}</span></span>`,
  key: html => `<span class="ws-keyonly">${html}</span>`,           // shown only on the key
  keyline: html => `<p class="ws-keyonly">${html}</p>`,
  part: (name, html) => [name, html],
  example: (...rows) => `<div class="ws-example"><p class="ws-tag">Example</p>${rows.map(x => `<p>${x}</p>`).join('')}</div>`,
  // numbered list of fill-in rows; cols = 1, 2 or 3; start = first number
  fill: (rows, cols = 1, start = 1) => `<ol class="ws-fill${cols > 1 ? ' ws-cols' : ''}" start="${start}"${cols > 2 ? ' style="columns:3"' : ''}>${rows.map(x => `<li>${x}</li>`).join('')}</ol>`,
  q: (n, html, after = '') => `<div class="ws-q"><p><span class="ws-num">${n}.</span> ${html}</p>${after}</div>`,
  choice: (n, html, opts, right) => H.q(n, html, `<ul class="ws-choice">${opts.map((o, i) => `<li class="${i === right ? 'ws-right' : ''}"><span class="ws-bubble">${'ABCDEFGH'[i]}</span> ${o}</li>`).join('')}</ul>`),
  lines: n => `<div class="ws-lines">${'<span></span>'.repeat(n)}</div>`,
  work: (h = 1.1, label = 'Show your work') => `<div class="ws-draw" style="height:${h}in"><span>${esc(label)}</span></div>`,
  table: (head, rows) => `<table class="ws-table"><thead><tr>${head.map(x => `<th>${x}</th>`).join('')}</tr></thead><tbody>${rows.map(r => `<tr>${r.map(x => `<td>${x}</td>`).join('')}</tr>`).join('')}</tbody></table>`,
  text: html => `<p class="ws-text">${html}</p>`,
  sub: html => `<p class="ws-sub">${html}</p>`,
  // a simple vertical stacked problem: top over bottom with an operator and a line, answer in the key
  stack: (top, op, bottom, ans) => `<div class="gen-stack"><span>${esc(top)}</span><span><b>${esc(op)}</b> ${esc(bottom)}</span><span class="gen-stack-ans"><span class="ws-ans">${esc(ans)}</span></span></div>`,
  stacks: (cells, perRow = 4) => `<div class="gen-stacks" style="--n:${perRow}">${cells.map((c, i) => `<div class="gen-stack-cell"><span class="ws-num">${i + 1}.</span>${c}</div>`).join('')}</div>`,
  // long division in a bracket: the answer sits above the dividend on the key
  longdiv: (dividend, divisor, ans) => `<div class="gen-ld"><span class="gen-ld-q"><span class="ws-ans">${esc(ans)}</span></span><span class="gen-ld-d">${esc(divisor)}</span><span class="gen-ld-n">${esc(dividend)}</span></div>`,
  // an inline fraction: frac(3, 4) ; mixed(1, 3, 4)
  frac: (n, d) => `<span class="gen-frac"><span>${esc(n)}</span><span>${esc(d)}</span></span>`,
  mixed: (w, n, d) => `${w ? `${esc(w)}&#8202;` : ''}${H.frac(n, d)}`,
  svg: (w, h, body, label) => `<svg class="gen-svg" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(label || 'Drawing')}" style="max-width:${(w / 96).toFixed(2)}in">${body}</svg>`,
};

/* ---------- small math helpers ---------- */
const M = Gen.m = {
  gcd: (a, b) => { a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a; },
  lcm: (a, b) => Math.abs(a * b) / M.gcd(a, b),
  round: (x, dp = 2) => Math.round((x + Number.EPSILON) * 10 ** dp) / 10 ** dp,
  // number to text with commas and no float noise: 1234.5 -> "1,234.5"
  fmt: (x, dp = 2) => { const v = M.round(x, dp); const [i, f] = String(Math.abs(v)).split('.');
    return (v < 0 ? '−' : '') + i.replace(/\B(?=(\d{3})+(?!\d))/g, ',') + (f ? '.' + f : ''); },
  minus: s => String(s).replace(/^-/, '−'),
};

/* ---------- making a sheet ---------- */
Gen.values = (def, given = {}, d) => {   // fill defaults and coerce types; given usually comes from the URL
  const v = {};
  for (const f of def.fields) {
    let x = given[f.id];
    if (f.type === 'check') x = x == null ? !!f.def : (x === true || x === '1' || x === 'true');
    else if (f.type === 'number') { x = x == null || x === '' || isNaN(+x) ? f.def : +x; if (f.min != null) x = Math.max(f.min, x); if (f.max != null) x = Math.min(f.max, x); }
    else if (f.type === 'select') { const opts = Gen.opts(f, v, d); x = opts.some(o => String(o[0]) === String(x)) ? x : (opts.some(o => String(o[0]) === String(f.def)) ? f.def : opts[0]?.[0]); }
    else x = x == null ? (f.def ?? '') : String(x).slice(0, 240);
    v[f.id] = x;
  }
  return v;
};
Gen.opts = (f, v, d) => (typeof f.options === 'function' ? f.options(v, d) : f.options) || [];

// the rng is seeded from the sheet code and the settings that differ from their defaults, in id order, so a generator
// can gain a setting without changing the sheets old links print
Gen.seedKey = (def, v) => JSON.stringify(def.fields.filter(f => String(v[f.id]) !== String(f.def ?? '')).map(f => [f.id, v[f.id]]).sort());
Gen.make = (id, v, seed, d) => {
  const def = Gen.defs[id], s = def.make(v, Gen.rng(id + ':' + seed + ':' + Gen.seedKey(def, v)), d);
  s.seed = seed;
  return s;
};

Gen.render = (id, s, meta = {}) => {   // meta: {title, url} for the footer
  const def = Gen.defs[id], url = meta.url || `curioclass.org/closet/worksheets/make/${id}/`;
  const head = `<header class="ws-head"><div class="ws-name"><span>Name</span><span>Date</span><span>Class</span></div>` +
    `<p class="ws-eyebrow">${esc(s.eyebrow || def.type || 'Practice')}${s.level ? ' · ' + esc(s.level) : ''}</p><h1>${esc(s.title)}</h1>` +
    (s.ican ? `<p class="ws-ican">${s.ican}</p>` : '') + `<p class="ws-directions"><b>Directions:</b> ${s.directions}</p></header>`;
  const body = s.parts.map(([name, html]) => `<section class="ws-section">${name ? `<h2 class="ws-part">${esc(name)}</h2>` : ''}${html}</section>`).join('');
  const foot = `<p class="ws-foot">${esc(s.title)} · sheet ${esc(s.seed)} · made with the ${esc(meta.title || def.title || id)} generator, ${esc(url)} · free under CC BY 4.0</p>`;
  const t = [`<p class="ws-eyebrow">Teacher page · answer key above</p><h2>${esc(s.title)}</h2><dl class="ws-facts">`,
    `<dt>Sheet</dt><dd>${esc(s.seed)} (open the same link to print this exact sheet again)</dd>`,
    s.level ? `<dt>Level</dt><dd>${esc(s.level)}</dd>` : '',
    `<dt>Time</dt><dd>${esc(s.minutes || 20)} minutes</dd><dt>Materials</dt><dd>${esc(s.materials || 'pencil')}</dd></dl>`];
  if (s.mistakes) t.push(`<h3>Watch for</h3><p>${s.mistakes}</p>`);
  if (s.notes) t.push(`<h3>Notes</h3><p>${s.notes}</p>`);
  if (s.teacher) t.push(s.teacher);   // extra teacher-page html, such as a worked solution list
  return `<article class="ws-sheet">${head}${body}${foot}</article><article class="ws-teacher">${t.join('')}${foot}</article>`;
};

/* ---------- the page (browser only) ---------- */
if (typeof document === 'undefined') return;
G.addEventListener('DOMContentLoaded', () => {
  const root = document.getElementById('gen');
  if (!root) return;
  const id = root.dataset.gen, def = Gen.defs[id];
  const form = document.getElementById('gen-form'), view = document.getElementById('gen-view');
  if (def && def.css) { const st = document.createElement('style'); st.textContent = def.css; document.head.appendChild(st); }
  if (!def) { view.innerHTML = '<p class="ws-msg">This generator did not load. Try reloading the page.</p>'; return; }
  const q = new URLSearchParams(location.search);
  let seed = /^[A-Z2-9]{5}$/.test(q.get('s') || '') ? q.get('s') : Gen.newSeed(), d = null, v;

  function drawForm() {
    form.innerHTML = '';
    for (const f of def.fields) {
      if (f.show && !f.show(v, d)) continue;
      const wrap = document.createElement('div');
      wrap.className = 'pr-field' + (f.type === 'check' ? ' check' : '');
      const fid = 'gen-' + f.id;
      if (f.type === 'check') wrap.innerHTML = `<label><input type="checkbox" id="${fid}"${v[f.id] ? ' checked' : ''}> ${esc(f.label)}</label>`;
      else if (f.type === 'select') wrap.innerHTML = `<label for="${fid}">${esc(f.label)}</label><select id="${fid}">${Gen.opts(f, v, d).map(([val, lab]) => `<option value="${esc(val)}"${String(val) === String(v[f.id]) ? ' selected' : ''}>${esc(lab)}</option>`).join('')}</select>`;
      else wrap.innerHTML = `<label for="${fid}">${esc(f.label)}</label><input id="${fid}" type="${f.type === 'number' ? 'number' : 'text'}"${f.min != null ? ` min="${f.min}"` : ''}${f.max != null ? ` max="${f.max}"` : ''} maxlength="240" value="${esc(v[f.id])}">`;
      const input = wrap.querySelector('input,select');
      input.addEventListener(f.type === 'text' || f.type === 'number' ? 'input' : 'change', () => {
        v[f.id] = f.type === 'check' ? input.checked : input.value;
        v = Gen.values(def, v, d);
        if (def.fields.some(g => g.show || typeof g.options === 'function')) { drawForm(); document.getElementById(fid)?.focus(); }
        draw();
      });
      form.appendChild(wrap);
    }
  }
  function draw() {
    const s = Gen.make(id, v, seed, d);
    view.innerHTML = Gen.render(id, s, { title: root.dataset.title });
    const p = new URLSearchParams();
    for (const f of def.fields) if (String(v[f.id]) !== String(f.def ?? '')) p.set(f.id, f.type === 'check' ? (v[f.id] ? '1' : '0') : v[f.id]);
    p.set('s', seed);
    history.replaceState(null, '', '?' + p.toString());
    document.getElementById('gen-code').textContent = 'Sheet ' + seed;
  }
  document.getElementById('gen-new').addEventListener('click', () => { seed = Gen.newSeed(); draw(); });
  document.getElementById('gen-print').addEventListener('click', () => print());
  document.querySelectorAll('input[name="copy"]').forEach(r => r.addEventListener('change', () => view.classList.toggle('show-key', r.value === 'key' && r.checked)));
  if (q.get('copy') === 'key') { document.querySelector('input[name="copy"][value="key"]').checked = true; view.classList.add('show-key'); }
  (async () => {
    if (def.data) {
      const res = await fetch(`/closet/worksheets/make/${def.data}.json`).catch(() => null);
      if (!res || !res.ok) { view.innerHTML = '<p class="ws-msg">The word list did not load. Try reloading the page.</p>'; return; }
      d = await res.json();
    }
    v = Gen.values(def, Object.fromEntries(q), d);
    drawForm(); draw();
  })();
});
})(typeof window !== 'undefined' ? window : globalThis);
