// Curio Class printables: one engine for the Supply Closet Printables shelf (/closet/printables/).
// Each page has <div id="pr" data-kind="..."> ; this file builds the settings form, draws the sheet as SVG (units:
// 1/100 inch inside 0.5 in margins, so a letter page is 750 x 1000 portrait or 1000 x 750 landscape) and prints it.
(() => {
'use strict';
const root = document.getElementById('pr');
if (!root) return;
const KIND = root.dataset.kind;
const $ = (s, el = document) => el.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const FONT = "'Instrument Sans', 'Segoe UI', Arial, sans-serif";
const INK = '#1f2430', SOFT = '#8a8f99', FAINT = '#c9ccd2', GUIDE = '#9aa7c7';

/* ---------- svg helpers ---------- */
const line = (x1, y1, x2, y2, o = {}) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${o.c || INK}" stroke-width="${o.w || 1.2}"${o.dash ? ` stroke-dasharray="${o.dash}"` : ''}${o.cap ? ' stroke-linecap="round"' : ''}/>`;
const rect = (x, y, w, h, o = {}) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${o.r ?? 10}" fill="${o.fill || 'none'}" stroke="${o.c || INK}" stroke-width="${o.w || 2}"/>`;
const circle = (cx, cy, r, o = {}) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${o.fill || 'none'}" stroke="${o.c || INK}" stroke-width="${o.w || 2}"${o.op ? ` fill-opacity="${o.op}"` : ''}/>`;
const text = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-family="${o.f || FONT}" font-size="${o.size || 16}" font-weight="${o.wt || 400}" fill="${o.c || INK}" text-anchor="${o.a || 'start'}"${o.ls ? ` letter-spacing="${o.ls}"` : ''}>${esc(s)}</text>`;
const arrow = (x1, y1, x2, y2) => { const a = Math.atan2(y2 - y1, x2 - x1), h = 12; return line(x1, y1, x2, y2, { w: 2.2 }) +
  `<path d="M${x2} ${y2} L${x2 - h * Math.cos(a - .45)} ${y2 - h * Math.sin(a - .45)} L${x2 - h * Math.cos(a + .45)} ${y2 - h * Math.sin(a + .45)}Z" fill="${INK}"/>`; };
const fit = (s, w, max, k = .58) => Math.max(10, Math.min(max, w / (Math.max(1, s.length) * k)));
function writeLines(x, y, w, h, gap) {  // ruled writing lines inside a box
  if (!gap) return '';
  let out = '';
  for (let yy = y + gap; yy <= y + h - 6; yy += gap) out += line(x, yy, x + w, yy, { c: FAINT, w: 1 });
  return out;
}

/* ---------- words (English, Spanish, or both) ---------- */
const W = {
  name: ['Name', 'Nombre'], date: ['Date', 'Fecha'],
  both: ['Both', 'Ambos'],
  k: ['What I Know', 'Lo que sé'], wnt: ['What I Want to Know', 'Lo que quiero saber'], h: ['How I Will Find Out', 'Cómo lo voy a averiguar'], l: ['What I Learned', 'Lo que aprendí'],
  title: ['Title', 'Título'], characters: ['Characters', 'Personajes'], setting: ['Setting', 'Ambiente'], problem: ['Problem', 'Problema'],
  beginning: ['Beginning', 'Principio'], middle: ['Middle', 'Desarrollo'], end: ['End', 'Final'], solution: ['Solution', 'Solución'],
  cause: ['Cause', 'Causa'], effect: ['Effect', 'Efecto'],
  main: ['Main Idea', 'Idea principal'], detail: ['Detail', 'Detalle'],
  first: ['First', 'Primero'], next: ['Next', 'Después'], then: ['Then', 'Luego'], last: ['Last', 'Al final'],
  word: ['Word', 'Palabra'], definition: ['Definition', 'Definición'], traits: ['Characteristics', 'Características'],
  examples: ['Examples', 'Ejemplos'], non: ['Non-examples', 'No son ejemplos'],
  picture: ['Picture', 'Dibujo'],
};
let LANG = 'en';
const t = k => LANG === 'es' ? W[k][1] : LANG === 'both' ? `${W[k][0]} / ${W[k][1]}` : W[k][0];

/* ---------- settings form ---------- */
const LANGSEL = { id: 'lang', label: 'Language', type: 'select', options: [['en', 'English'], ['es', 'Español'], ['both', 'Both']], def: 'en' };
const NAMEDATE = { id: 'nd', label: 'Name and date line', type: 'check', def: true };
const TITLE = { id: 'title', label: 'Title (optional)', type: 'text', def: '' };
const LINES = { id: 'lines', label: 'Writing lines in boxes', type: 'select', options: [['0', 'None'], ['50', 'Wide'], ['36', 'Narrow']], def: '50' };

const KINDS = {
  /* ----- paper ----- */
  handwriting: {
    fields: [{ id: 'size', label: 'Line size', type: 'select', options: [['100', 'Large (K)'], ['75', 'Medium (grade 1)'], ['55', 'Small (grade 2)']], def: '100' },
      { id: 'pic', label: 'Picture box at the top', type: 'check', def: false }, NAMEDATE, { id: 'orient', label: 'Page', type: 'select', options: [['p', 'Portrait'], ['l', 'Landscape']], def: 'p' }],
    land: v => v.orient === 'l',
    draw(v, W_, H) {
      let out = '', y = 0, h = +v.size;
      if (v.nd) { out += nameDate(W_); y = 55; }
      if (v.pic) { out += rect(0, y, W_, H * .4, { r: 8, w: 1.6 }); y += H * .4 + 25; }
      for (; y + h <= H; y += h * 1.45) {
        out += line(0, y, W_, y, { w: 1.6 }) + line(0, y + h / 2, W_, y + h / 2, { c: GUIDE, w: 1.2, dash: '10 8' }) + line(0, y + h, W_, y + h, { w: 1.6 });
      }
      return out;
    },
  },
  lined: {
    fields: [{ id: 'rule', label: 'Ruling', type: 'select', options: [['50', 'Extra wide (1/2 in)'], ['34.4', 'Wide (11/32 in)'], ['28.1', 'College (9/32 in)']], def: '34.4' },
      { id: 'margin', label: 'Margin line', type: 'check', def: true }, NAMEDATE],
    draw(v, W_, H) {
      let out = '', y0 = v.nd ? 70 : 20, g = +v.rule;
      if (v.nd) out += nameDate(W_);
      for (let y = y0; y <= H; y += g) out += line(0, y, W_, y, { c: '#9fb3d1', w: 1.1 });
      if (v.margin) out += line(90, y0 - g, 90, H, { c: '#e3a0a0', w: 1.4 });
      return out;
    },
  },
  graph: {
    fields: [{ id: 'cell', label: 'Square size', type: 'select', options: [['25', '1/4 inch'], ['50', '1/2 inch'], ['39.37', '1 centimeter'], ['19.685', '5 millimeters']], def: '25' },
      { id: 'bold', label: 'Darker line every 5 squares', type: 'check', def: false }, NAMEDATE],
    draw(v, W_, H) {
      let out = '', c = +v.cell, y0 = v.nd ? 60 : 0;
      if (v.nd) out += nameDate(W_);
      const cols = Math.floor(W_ / c), rows = Math.floor((H - y0) / c), x0 = (W_ - cols * c) / 2;
      for (let i = 0; i <= cols; i++) { const b = v.bold && i % 5 === 0; out += line(x0 + i * c, y0, x0 + i * c, y0 + rows * c, { c: b ? '#7b8fb4' : '#b9c6dd', w: b ? 1.5 : .9 }); }
      for (let j = 0; j <= rows; j++) { const b = v.bold && j % 5 === 0; out += line(x0, y0 + j * c, x0 + cols * c, y0 + j * c, { c: b ? '#7b8fb4' : '#b9c6dd', w: b ? 1.5 : .9 }); }
      return out;
    },
  },
  dots: {
    fields: [{ id: 'grid', label: 'Dot pattern', type: 'select', options: [['sq', 'Square'], ['iso', 'Isometric (triangles)']], def: 'sq' },
      { id: 'gap', label: 'Spacing', type: 'select', options: [['50', '1/2 inch'], ['39.37', '1 centimeter'], ['25', '1/4 inch']], def: '50' }, NAMEDATE],
    draw(v, W_, H) {
      let out = '', g = +v.gap, y0 = v.nd ? 70 : 10;
      if (v.nd) out += nameDate(W_);
      const dy = v.grid === 'iso' ? g * Math.sqrt(3) / 2 : g, r = g < 30 ? 2.2 : 3;
      for (let j = 0, y = y0; y <= H; j++, y += dy) {
        const off = v.grid === 'iso' && j % 2 ? g / 2 : 0;
        for (let x = off + 5; x <= W_; x += g) out += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r}" fill="#5e6472"/>`;
      }
      return out;
    },
  },

  /* ----- math and letters ----- */
  numberline: {
    fields: [{ id: 'from', label: 'From', type: 'number', def: 0 }, { id: 'to', label: 'To', type: 'number', def: 20 },
      { id: 'step', label: 'Count by', type: 'number', def: 1 },
      { id: 'show', label: 'Numbers', type: 'select', options: [['all', 'All shown'], ['ends', 'Only the ends (fill in the rest)'], ['none', 'None (blank ticks)']], def: 'all' },
      { id: 'rows', label: 'Lines on the page', type: 'select', options: [['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['6', '6']], def: '3' }, NAMEDATE],
    land: () => true,
    draw(v, W_, H) {
      let out = '', y0 = v.nd ? 70 : 0;
      if (v.nd) out += nameDate(W_);
      const step = Math.abs(+v.step) || 1, from = +v.from, to = Math.max(+v.to, from + step);
      const n = Math.min(60, Math.round((to - from) / step)), rows = +v.rows, band = (H - y0) / rows;
      const x0 = 30, x1 = W_ - 30, dx = (x1 - x0) / n, size = Math.min(26, dx * .55);
      for (let r = 0; r < rows; r++) {
        const y = y0 + band * (r + .5);
        out += line(x0 - 20, y, x1 + 20, y, { w: 2.4 }) + arrowHead(x1 + 22, y, 0) + arrowHead(x0 - 22, y, Math.PI);
        for (let i = 0; i <= n; i++) {
          const x = x0 + i * dx, val = +(from + i * step).toFixed(4);
          out += line(x, y - 14, x, y + 14, { w: 2 });
          if (v.show === 'all' || (v.show === 'ends' && (i === 0 || i === n))) out += text(x, y + 14 + size + 4, val, { size, a: 'middle' });
        }
      }
      return out;
    },
  },
  hundreds: {
    fields: [{ id: 'range', label: 'Numbers', type: 'select', options: [['1-100', '1 to 100'], ['0-99', '0 to 99'], ['1-120', '1 to 120']], def: '1-100' },
      { id: 'fill', label: 'Show', type: 'select', options: [['all', 'Every number'], ['some', 'Some numbers (fill in the rest)'], ['none', 'Blank chart']], def: 'all' }, NAMEDATE],
    draw(v, W_, H) {
      let out = '', y0 = v.nd ? 70 : 0;
      if (v.nd) out += nameDate(W_);
      const [a, b] = v.range.split('-').map(Number), rows = (b - a + 1) / 10, c = Math.min(W_ / 10, (H - y0) / rows), x0 = (W_ - c * 10) / 2;
      let seed = a * 7 + b;  // steady "random" gaps, so a reprint matches
      const rnd = () => (seed = (seed * 9301 + 49297) % 233280) / 233280;
      for (let i = 0; i < b - a + 1; i++) {
        const x = x0 + (i % 10) * c, y = y0 + Math.floor(i / 10) * c;
        out += `<rect x="${x}" y="${y}" width="${c}" height="${c}" fill="none" stroke="${INK}" stroke-width="1.4"/>`;
        const showIt = v.fill === 'all' || (v.fill === 'some' && rnd() > .5);
        if (showIt) out += text(x + c / 2, y + c * .64, a + i, { size: c * .4, a: 'middle', wt: 600 });
      }
      return out;
    },
  },
  alphabet: {
    fields: [{ id: 'case', label: 'Letters', type: 'select', options: [['both', 'Aa (both)'], ['upper', 'Uppercase'], ['lower', 'Lowercase']], def: 'both' },
      { id: 'style', label: 'Layout', type: 'select', options: [['strip', 'Desk strips (3 per page)'], ['cards', 'Letter cards (one page)']], def: 'strip' }],
    land: v => v.style === 'strip',
    draw(v, W_, H) {
      const L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''), lab = c => v.case === 'upper' ? c : v.case === 'lower' ? c.toLowerCase() : c + c.toLowerCase();
      let out = '';
      if (v.style === 'strip') {
        const sh = H / 3;
        for (let s = 0; s < 3; s++) {
          const y = s * sh + 12, h = sh - 24, cw = W_ / 13;
          out += rect(0, y, W_, h, { r: 12, w: 1.6 });
          L.forEach((c, i) => { const col = i % 13, row = Math.floor(i / 13), x = col * cw;
            if (col) out += line(x, y + row * h / 2 + 8, x, y + (row + 1) * h / 2 - 8, { c: FAINT, w: 1 });
            out += text(x + cw / 2, y + row * h / 2 + h * .36, lab(c), { size: Math.min(h * .3, cw * (v.case === 'both' ? .42 : .7)), a: 'middle', wt: 600 }); });
          out += line(10, y + h / 2, W_ - 10, y + h / 2, { c: FAINT, w: 1 });
        }
      } else {
        const cols = 4, rows = 7, cw = W_ / cols, ch = H / rows;
        L.forEach((c, i) => { const x = (i % cols) * cw, y = Math.floor(i / cols) * ch;
          out += rect(x + 6, y + 6, cw - 12, ch - 12, { r: 14, w: 1.6 }) + text(x + cw / 2, y + ch * .66, lab(c), { size: ch * .5, a: 'middle', wt: 600 }); });
      }
      return out;
    },
  },

  /* ----- organizers ----- */
  venn: {
    fields: [LANGSEL, TITLE, { id: 'n', label: 'Circles', type: 'select', options: [['2', 'Two'], ['3', 'Three']], def: '2' },
      { id: 'a', label: 'Label A', type: 'text', def: '' }, { id: 'b', label: 'Label B', type: 'text', def: '' }, { id: 'c', label: 'Label C (three circles)', type: 'text', def: '' }, NAMEDATE],
    land: v => v.n === '2',
    draw(v, W_, H) {
      let { out, y } = head(v, W_);
      const blank = s => s || '____________';
      if (v.n === '2') {
        const r = Math.min((H - y - 40) / 2, W_ * .3), cy = y + 40 + r, cx1 = W_ / 2 - r * .58, cx2 = W_ / 2 + r * .58;
        out += circle(cx1, cy, r, { w: 2.4 }) + circle(cx2, cy, r, { w: 2.4 });
        out += text(cx1 - r * .45, y + 28, blank(v.a), { size: 20, a: 'middle', wt: 700 }) + text(cx2 + r * .45, y + 28, blank(v.b), { size: 20, a: 'middle', wt: 700 });
        out += text(W_ / 2, y + 28, t('both'), { size: 18, a: 'middle', wt: 700, c: SOFT });
      } else {
        const r = Math.min((H - y - 40) / 3.1, W_ * .3), cx = W_ / 2, cy = y + 40 + r * 1.55;
        const pts = [[cx - r * .58, cy - r * .45], [cx + r * .58, cy - r * .45], [cx, cy + r * .55]];
        pts.forEach(([x, yy]) => out += circle(x, yy, r, { w: 2.4 }));
        out += text(pts[0][0] - r * .4, y + 26, blank(v.a), { size: 18, a: 'middle', wt: 700 }) + text(pts[1][0] + r * .4, y + 26, blank(v.b), { size: 18, a: 'middle', wt: 700 })
          + text(cx, Math.min(H - 6, cy + r * 1.55 + 24), blank(v.c), { size: 18, a: 'middle', wt: 700 });
      }
      return out;
    },
  },
  kwl: {
    fields: [LANGSEL, TITLE, { id: 'hcol', label: 'Add "How I will find out"', type: 'check', def: false }, LINES, NAMEDATE],
    land: () => true,
    draw(v, W_, H) {
      let { out, y } = head(v, W_);
      const cols = v.hcol ? ['k', 'wnt', 'h', 'l'] : ['k', 'wnt', 'l'], letters = v.hcol ? 'KWHL' : 'KWL', cw = W_ / cols.length;
      cols.forEach((k, i) => {
        const x = i * cw + 6, w = cw - 12;
        out += rect(x, y, w, H - y, { r: 12 }) + text(x + w / 2, y + 48, letters[i], { size: 40, a: 'middle', wt: 700, c: '#1d5c63' })
          + text(x + w / 2, y + 78, t(k), { size: fit(t(k), w - 16, 17, .52), a: 'middle', wt: 600 }) + writeLines(x + 14, y + 92, w - 28, H - y - 100, +v.lines);
      });
      return out;
    },
  },
  storymap: {
    fields: [LANGSEL, TITLE, LINES, NAMEDATE],
    draw(v, W_, H) {
      let { out, y } = head(v, W_);
      const g = 14, row = (H - y - 3 * g) / 4;
      const box = (x, yy, w, h, k) => rect(x, yy, w, h, { r: 12 }) + text(x + 14, yy + 28, t(k), { size: 18, wt: 700, c: '#1d5c63' }) + writeLines(x + 14, yy + 36, w - 28, h - 42, +v.lines);
      out += box(0, y, W_, row * .55, 'title');
      const y2 = y + row * .55 + g, h2 = row * 1.15;
      out += box(0, y2, (W_ - g) / 2, h2, 'characters') + box((W_ + g) / 2, y2, (W_ - g) / 2, h2, 'setting');
      const y3 = y2 + h2 + g; out += box(0, y3, W_, row * .8, 'problem');
      const y4 = y3 + row * .8 + g, h4 = row * 1, cw = (W_ - 2 * g) / 3;
      ['beginning', 'middle', 'end'].forEach((k, i) => out += box(i * (cw + g), y4, cw, h4, k));
      const y5 = y4 + h4 + g; out += box(0, y5, W_, H - y5, 'solution');
      return out;
    },
  },
  causeeffect: {
    fields: [LANGSEL, TITLE, { id: 'shape', label: 'Shape', type: 'select', options: [['one', 'One cause, three effects'], ['chain', 'Chain of four']], def: 'one' }, LINES, NAMEDATE],
    draw(v, W_, H) {
      let { out, y } = head(v, W_);
      const lab = (x, yy, w, h, k) => rect(x, yy, w, h, { r: 12 }) + text(x + 14, yy + 28, t(k), { size: 18, wt: 700, c: '#1d5c63' }) + writeLines(x + 14, yy + 36, w - 28, h - 42, +v.lines);
      if (v.shape === 'one') {
        const ch = H - y, cw = W_ * .36, ew = W_ * .5, eh = (ch - 40) / 3;
        out += lab(0, y + ch / 2 - ch * .2, cw, ch * .4, 'cause');
        for (let i = 0; i < 3; i++) { const yy = y + i * (eh + 20); out += lab(W_ - ew, yy, ew, eh, 'effect') + arrow(cw + 6, y + ch / 2, W_ - ew - 8, yy + eh / 2); }
      } else {
        const g = 44, bh = (H - y - 3 * g) / 4;
        ['cause', 'effect', 'effect', 'effect'].forEach((k, i) => { const yy = y + i * (bh + g); out += lab(W_ * .1, yy, W_ * .8, bh, k);
          if (i < 3) out += arrow(W_ / 2, yy + bh + 4, W_ / 2, yy + bh + g - 6); });
      }
      return out;
    },
  },
  mainidea: {
    fields: [LANGSEL, TITLE, { id: 'n', label: 'Details', type: 'select', options: [['3', 'Three'], ['4', 'Four']], def: '3' }, LINES, NAMEDATE],
    draw(v, W_, H) {
      let { out, y } = head(v, W_);
      const top = (H - y) * .3, n = +v.n, g = 14, dw = (W_ - (n - 1) * g) / n, dy = y + top + 30;
      out += rect(0, y, W_, top, { r: 12, fill: '#f3eee2' }) + text(14, y + 30, t('main'), { size: 20, wt: 700, c: '#1d5c63' }) + writeLines(14, y + 38, W_ - 28, top - 44, +v.lines);
      for (let i = 0; i < n; i++) { const x = i * (dw + g);
        out += line(x + dw / 2, y + top, x + dw / 2, dy, { w: 2.4 }) + rect(x, dy, dw, H - dy, { r: 12 }) + text(x + 14, dy + 28, `${t('detail')} ${i + 1}`, { size: 17, wt: 700, c: '#1d5c63' })
          + writeLines(x + 12, dy + 36, dw - 24, H - dy - 42, +v.lines); }
      return out;
    },
  },
  tchart: {
    fields: [TITLE, { id: 'left', label: 'Left heading', type: 'text', def: '' }, { id: 'right', label: 'Right heading', type: 'text', def: '' }, LINES, NAMEDATE],
    draw(v, W_, H) {
      let { out, y } = head(v, W_);
      const hy = y + 50;
      out += line(0, hy, W_, hy, { w: 3, cap: 1 }) + line(W_ / 2, y, W_ / 2, H, { w: 3, cap: 1 });
      [[v.left, W_ / 4], [v.right, W_ * .75]].forEach(([s, x]) => out += s ? text(x, y + 34, s, { size: fit(s, W_ / 2 - 30, 26), a: 'middle', wt: 700 }) : line(x - 110, y + 36, x + 110, y + 36, { c: FAINT }));
      out += writeLines(10, hy + 6, W_ / 2 - 24, H - hy - 6, +v.lines) + writeLines(W_ / 2 + 14, hy + 6, W_ / 2 - 24, H - hy - 6, +v.lines);
      return out;
    },
  },
  sequence: {
    fields: [LANGSEL, TITLE, { id: 'n', label: 'Steps', type: 'select', options: [['4', 'Four: First, Next, Then, Last'], ['6', 'Six (numbered)']], def: '4' },
      { id: 'pic', label: 'Space to draw in each box', type: 'check', def: true }, LINES, NAMEDATE],
    draw(v, W_, H) {
      let { out, y } = head(v, W_);
      const n = +v.n, cols = 2, rows = n / 2, g = 34, bw = (W_ - g) / cols, bh = (H - y - (rows - 1) * g) / rows;
      const names = n === 4 ? ['first', 'next', 'then', 'last'].map(t) : [1, 2, 3, 4, 5, 6].map(String);
      for (let i = 0; i < n; i++) {
        const c = i % 2, r = Math.floor(i / 2), x = c * (bw + g), yy = y + r * (bh + g);
        out += rect(x, yy, bw, bh, { r: 12 }) + text(x + 14, yy + 30, names[i], { size: 20, wt: 700, c: '#1d5c63' });
        let ly = yy + 40;
        if (v.pic) { out += rect(x + 12, ly, bw - 24, bh * .5, { r: 8, w: 1.2, c: FAINT }); ly += bh * .5 + 4; }
        out += writeLines(x + 14, ly, bw - 28, yy + bh - ly - 4, +v.lines);
        if (c === 0) out += arrow(x + bw + 4, yy + bh / 2, x + bw + g - 4, yy + bh / 2);
        else if (i < n - 1) out += arrow(x + bw / 2 - 10, yy + bh + 4, bw / 2 + 10, yy + bh + g - 4);
      }
      return out;
    },
  },
  frayer: {
    fields: [LANGSEL, { id: 'word', label: 'Word (optional)', type: 'text', def: '' }, LINES, NAMEDATE],
    draw(v, W_, H) {
      let { out, y } = head(v, W_);
      const h = H - y, cx = W_ / 2, cy = y + h / 2, qs = [['definition', 0, 0], ['traits', 1, 0], ['examples', 0, 1], ['non', 1, 1]];
      qs.forEach(([k, c, r]) => { const x = c * W_ / 2 + 5, yy = y + r * h / 2 + 5, w = W_ / 2 - 10, hh = h / 2 - 10;
        out += rect(x, yy, w, hh, { r: 12 }) + text(c ? x + w - 14 : x + 14, r ? yy + hh - 14 : yy + 30, t(k), { size: 18, wt: 700, c: '#1d5c63', a: c ? 'end' : 'start' })
          + writeLines(x + 14, r ? yy + 6 : yy + 40, w - 28, hh - 50, +v.lines); });
      out += `<ellipse cx="${cx}" cy="${cy}" rx="${W_ * .2}" ry="${h * .1}" fill="#fff" stroke="${INK}" stroke-width="2.4"/>`;
      out += v.word ? text(cx, cy + 10, v.word, { size: fit(v.word, W_ * .34, 32), a: 'middle', wt: 700 }) : text(cx, cy - h * .1 + 26, t('word'), { size: 15, a: 'middle', c: SOFT });
      return out;
    },
  },

  /* ----- classroom ----- */
  nameplate: {
    fields: [{ id: 'names', label: 'Names, one per line', type: 'area', def: '' },
      { id: 'style', label: 'Kind', type: 'select', options: [['desk', 'Desk plate: name, alphabet, numbers 0 to 20'], ['tent', 'Folded tent card (name on both sides)']], def: 'desk' }],
    land: v => v.style === 'desk',
    pages(v) { const n = v.names.split(/\n+/).map(s => s.trim()).filter(Boolean); const per = v.style === 'desk' ? 2 : 2, list = n.length ? n : [''];
      const out = []; for (let i = 0; i < list.length; i += per) out.push(list.slice(i, i + per)); return out; },
    draw(v, W_, H, names) {
      let out = '';
      names.forEach((nm, i) => {
        if (v.style === 'desk') {
          const y = i * H / 2 + 10, h = H / 2 - 20;
          out += rect(0, y, W_, h, { r: 16, w: 2 });
          out += nm ? text(W_ / 2, y + h * .38, nm, { size: fit(nm, W_ - 60, 110, .62), a: 'middle', wt: 700 }) : line(80, y + h * .38, W_ - 80, y + h * .38, { c: FAINT });
          const ay = y + h * .58, cw = (W_ - 40) / 26;
          'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach((c, j) => out += text(20 + cw * (j + .5), ay, c + c.toLowerCase(), { size: Math.min(20, cw * .5), a: 'middle', wt: 600 }));
          const ny = y + h * .82, dx = (W_ - 60) / 20;
          out += line(20, ny, W_ - 20, ny, { w: 2 });
          for (let k = 0; k <= 20; k++) out += line(30 + k * dx, ny - 9, 30 + k * dx, ny + 9, { w: 1.6 }) + text(30 + k * dx, ny + 30, k, { size: 16, a: 'middle' });
        } else {
          const y = i * H / 2 + 6, h = H / 2 - 12, mid = y + h / 2, fs = nm ? fit(nm, W_ - 80, 100, .62) : 0;
          out += rect(0, y, W_, h, { r: 4, w: 1.2, c: FAINT }) + line(0, mid, W_, mid, { c: SOFT, w: 1, dash: '8 8' });
          out += text(W_ - 8, mid - 6, 'fold', { size: 11, a: 'end', c: SOFT });
          if (nm) out += text(W_ / 2, mid + h * .25 + fs * .35, nm, { size: fs, a: 'middle', wt: 700 })
            + `<g transform="rotate(180 ${W_ / 2} ${mid - h * .25})">${text(W_ / 2, mid - h * .25 + fs * .35, nm, { size: fs, a: 'middle', wt: 700 })}</g>`;
        }
      });
      return out;
    },
  },
  certificate: {
    fields: [{ id: 'head', label: 'Heading', type: 'text', def: 'Certificate of Achievement' }, { id: 'name', label: 'Student name (blank to write in)', type: 'text', def: '' },
      { id: 'for', label: 'For', type: 'text', def: 'for working hard and never giving up' }, { id: 'by', label: 'Signed by (blank to sign)', type: 'text', def: '' },
      { id: 'date', label: 'Date (blank to write in)', type: 'text', def: '' }, { id: 'color', label: 'Border color', type: 'select', options: [['#1d5c63', 'Teal'], ['#b8761f', 'Gold'], ['#3a6ea5', 'Blue'], ['#8e4a8a', 'Purple'], ['#1f2430', 'Black (saves ink)']], def: '#1d5c63' }],
    land: () => true,
    draw(v, W_, H) {
      const c = v.color, cx = W_ / 2;
      let out = rect(0, 0, W_, H, { r: 6, w: 10, c }) + rect(22, 22, W_ - 44, H - 44, { r: 4, w: 2, c });
      [[40, 40], [W_ - 40, 40], [40, H - 40], [W_ - 40, H - 40]].forEach(([x, y]) => out += star(x, y, 16, c));
      out += text(cx, 170, v.head, { size: fit(v.head, W_ - 200, 54, .55), a: 'middle', wt: 700, c, ls: 1 });
      out += text(cx, 250, 'This certificate is presented to', { size: 22, a: 'middle', c: SOFT });
      out += v.name ? text(cx, 350, v.name, { size: fit(v.name, W_ - 260, 72, .6), a: 'middle', wt: 700 }) : '';
      out += line(170, 370, W_ - 170, 370, { c: SOFT, w: 1.4 });
      out += text(cx, 440, v.for, { size: fit(v.for, W_ - 220, 28, .5), a: 'middle' });
      out += line(110, 600, 420, 600, { c: SOFT, w: 1.4 }) + line(W_ - 420, 600, W_ - 110, 600, { c: SOFT, w: 1.4 });
      out += (v.by ? text(265, 590, v.by, { size: 24, a: 'middle' }) : '') + (v.date ? text(W_ - 265, 590, v.date, { size: 24, a: 'middle' }) : '');
      out += text(265, 628, 'Signed', { size: 17, a: 'middle', c: SOFT }) + text(W_ - 265, 628, 'Date', { size: 17, a: 'middle', c: SOFT });
      out += star(cx, 560, 46, c);
      return out;
    },
  },
};

function star(x, y, r, c) {
  let d = '';
  for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r * .45 : r; d += `${i ? 'L' : 'M'}${(x + rr * Math.cos(a)).toFixed(1)} ${(y + rr * Math.sin(a)).toFixed(1)}`; }
  return `<path d="${d}Z" fill="${c}" fill-opacity=".9"/>`;
}
function arrowHead(x, y, a) { const h = 16; return `<path d="M${x} ${y} L${x - h * Math.cos(a - .5)} ${y - h * Math.sin(a - .5)} L${x - h * Math.cos(a + .5)} ${y - h * Math.sin(a + .5)}Z" fill="${INK}"/>`; }
function nameDate(W_) {
  return text(0, 30, t('name'), { size: 17, wt: 600 }) + line(LANG === 'both' ? 150 : 70, 32, W_ * .62, 32, { c: SOFT })
    + text(W_ * .66, 30, t('date'), { size: 17, wt: 600 }) + line(W_ * .66 + (LANG === 'both' ? 120 : 52), 32, W_, 32, { c: SOFT });
}
function head(v, W_) {  // name/date line and title; returns where the body starts
  let out = '', y = 0;
  if (v.nd) { out += nameDate(W_); y = 55; }
  if (v.title) { out += text(W_ / 2, y + 36, v.title, { size: fit(v.title, W_, 30), a: 'middle', wt: 700 }); y += 58; }
  return { out, y: y + (y ? 6 : 0) };
}

/* ---------- page plumbing ---------- */
const K = KINDS[KIND];
const KEY = 'curio.print.' + KIND;
let saved = {};
try { saved = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch {}
const form = $('#pr-form'), sheet = $('#pr-sheet');
K.fields.forEach(f => {
  const id = 'f-' + f.id, val = f.id in saved ? saved[f.id] : f.def;
  const wrap = document.createElement('div'); wrap.className = 'pr-field' + (f.type === 'check' ? ' check' : '');
  if (f.type === 'select') wrap.innerHTML = `<label for="${id}">${f.label}</label><select id="${id}">${f.options.map(([v, l]) => `<option value="${v}"${String(v) === String(val) ? ' selected' : ''}>${l}</option>`).join('')}</select>`;
  else if (f.type === 'check') wrap.innerHTML = `<label><input type="checkbox" id="${id}"${val ? ' checked' : ''}> ${f.label}</label>`;
  else if (f.type === 'area') wrap.innerHTML = `<label for="${id}">${f.label}</label><textarea id="${id}" rows="8">${esc(val)}</textarea>`;
  else wrap.innerHTML = `<label for="${id}">${f.label}</label><input id="${id}" type="${f.type === 'number' ? 'number' : 'text'}" value="${esc(val)}"${f.type === 'number' ? ' step="any"' : ''}>`;
  form.appendChild(wrap);
});
function values() {
  const v = {};
  K.fields.forEach(f => { const el = $('#f-' + f.id); v[f.id] = f.type === 'check' ? el.checked : el.value; });
  return v;
}
let pageStyle = document.createElement('style'); document.head.appendChild(pageStyle);
function render() {
  const v = values(); LANG = v.lang || 'en';
  try { localStorage.setItem(KEY, JSON.stringify(v)); } catch {}
  const land = K.land ? K.land(v) : false, W_ = land ? 1000 : 750, H = land ? 750 : 1000;
  pageStyle.textContent = `@page { size: letter ${land ? 'landscape' : 'portrait'}; margin: 0.5in; }`;
  const pages = K.pages ? K.pages(v) : [null];
  sheet.innerHTML = pages.map(p => `<div class="pr-page${land ? ' land' : ''}"><svg viewBox="0 0 ${W_} ${H}" width="${W_ / 100}in" height="${H / 100}in" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc(document.title)}">${K.draw(v, W_, H, p)}</svg></div>`).join('');
  $('#pr-count').textContent = pages.length > 1 ? `${pages.length} pages` : '';
}
form.addEventListener('input', render);
form.addEventListener('change', render);
$('#pr-print').addEventListener('click', () => window.print());
$('#pr-reset').addEventListener('click', () => { try { localStorage.removeItem(KEY); } catch {} location.reload(); });
render();
})();
