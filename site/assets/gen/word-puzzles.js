// Word Puzzles generator, grades 1-12. Reads the Word Wall list (words.json): pick a subject, a grade band and a module
// (and an optional second module), then a word search or a crossword. The word search hides the words in a grid whose
// size and directions grow with the grade; the crossword is laid out by code so every word crosses another, with the
// meanings as numbered clues. Words with spaces or hyphens go in the grid as letters only, and the clue says so.
// Crosswords (grades 3-12) also offer 12 and 15 words when the chosen modules have that many; the bigger grids use
// smaller boxes so the page still fits.
(() => {
const { part, example, esc, blank } = Gen.h;

const BANDS = [['k2', 'Grades 1-2'], ['35', 'Grades 3-5'], ['68', 'Grades 6-8'], ['912', 'Grades 9-12']];
const COUNTS = { k2: [['5', '5 words'], ['6', '6 words'], ['8', '8 words']],
  35: [['6', '6 words'], ['8', '8 words'], ['10', '10 words']],
  68: [['8', '8 words'], ['10', '10 words'], ['12', '12 words']],
  912: [['8', '8 words'], ['10', '10 words'], ['12', '12 words']] };
const CAP = { k2: 10, 35: 12, 68: 15, 912: 17 };        // largest word search grid, and the longest word that fits
const BASE = { k2: 8, 35: 10, 68: 12, 912: 13 };        // starting word search grid size
// directions as [row step, column step]
const DIRS = { k2: [[0, 1], [1, 0]], 35: [[0, 1], [1, 0], [1, 1], [-1, 1]] };
DIRS['68'] = DIRS['912'] = DIRS['35'].concat([[0, -1], [-1, 0], [-1, -1], [1, -1]]);
const ALL8 = DIRS['68'];
const DIRWORDS = { k2: 'Words go across (left to right) and down.', 35: 'Words go across, down and on a slant (diagonal).',
  68: 'Words go across, down and diagonally, and some are backwards.', 912: 'Words go in all eight directions, including backwards.' };
// filler letters must not spell these (stored in ROT13 so the file does not print them)
const BLOCK = ['shpx', 'fuvg', 'phag', 'qvpx', 'pbpx', 'ovgpu', 'juber', 'fyhg', 'gvgf', 'cvff', 'nff', 'snt', 'frk', 'penc', 'cbea', 'enpvfg', 'xvyy']
  .map(w => w.replace(/[a-z]/g, c => String.fromCharCode((c.charCodeAt(0) - 84) % 26 + 97)).toUpperCase());

const mods = d => (d && d.modules) || [];
const subjects = d => { const seen = new Map(); for (const m of mods(d)) if (!seen.has(m.subject)) seen.set(m.subject, m.s);
  return [...seen].sort((a, b) => a[1].localeCompare(b[1])); };
const inBand = (v, d) => mods(d).filter(m => m.subject === v.subject && m.band === v.band);
const gradeNote = m => /^\d+$/.test(m.grade) ? ` (grade ${m.grade})` : m.grade === 'k' ? ' (kindergarten)' : '';
const byId = (d, id) => mods(d).find(m => m.id === id);
const letters = w => w.replace(/[^A-Za-z]/g, '').toUpperCase();
const usable = w => !/[0-9\/×=+]/.test(w) && letters(w).length >= 3;
// what the clue says about a word that is not one plain word
function note(w) {
  const n = w.trim().split(/\s+/).length, h = /-/.test(w);
  return n > 1 ? `(${n} words${h ? ', with a hyphen' : ''})` : h ? '(hyphenated word)' : '';
}
function mask(word, def) {
  const w = word.trim(), reEsc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  let re;
  if (/\s/.test(w)) re = new RegExp(reEsc(w), 'gi');
  else if (w.length < 3) re = new RegExp(`\\b${reEsc(w)}\\b`, 'gi');
  else { const stem = w.length >= 5 ? w.slice(0, Math.max(4, w.length - 2)) : w; re = new RegExp(`\\b${reEsc(stem)}[a-z]*`, 'gi'); }
  return def.replace(re, '_____');
}
function pool(v, d, maxLen) {
  const out = [], seen = new Set();
  for (const id of [v.mod, v.mod2]) {
    const m = id && byId(d, id);
    if (!m) continue;
    for (const [w, df] of m.words) {
      const L = letters(w);
      if (!usable(w) || L.length > maxLen || seen.has(L)) continue;
      seen.add(L); out.push({ w, df, L });
    }
  }
  return out;
}

/* ---------- word search ---------- */
// count how many times word appears in the grid along the given directions (a palindrome counts once per spot)
function occurrences(grid, word, dirs) {
  const n = grid.length, hits = [];
  for (let r = 0; r < n; r++) for (let c = 0; c < n; c++) for (const [dr, dc] of dirs) {
    let ok = true;
    for (let i = 0; i < word.length && ok; i++) { const rr = r + dr * i, cc = c + dc * i;
      ok = rr >= 0 && cc >= 0 && rr < n && cc < n && grid[rr][cc] === word[i]; }
    if (ok) hits.push([r, c, dr, dc]);
  }
  const keys = new Set(hits.map(([r, c, dr, dc]) => { const e = [r + dr * (word.length - 1), c + dc * (word.length - 1)];
    return [[r, c], e].map(x => x.join(',')).sort().join('|'); }));
  return keys.size;
}
// true if word can be read in any direction using at least one filler square (a word inside a module word is fine)
function spells(g, word, placedGrid) {
  const n = g.length;
  for (let r = 0; r < n; r++) for (let c = 0; c < n; c++) for (const [dr, dc] of ALL8) {
    let ok = true, filler = false;
    for (let i = 0; i < word.length && ok; i++) { const rr = r + dr * i, cc = c + dc * i;
      ok = rr >= 0 && cc >= 0 && rr < n && cc < n && g[rr][cc] === word[i]; if (ok && !placedGrid[rr][cc]) filler = true; }
    if (ok && filler) return true;
  }
  return false;
}
function search(r, words, band) {
  const dirs = DIRS[band];
  let size = Math.max(BASE[band], ...words.map(w => w.L.length));
  for (let attempt = 0; attempt < 60; attempt++) {
    if (attempt && attempt % 15 === 0 && size < CAP[band]) size++;
    const grid = Array.from({ length: size }, () => Array(size).fill(''));
    const placed = [];
    for (const w of words.slice().sort((a, b) => b.L.length - a.L.length)) {
      let spot = null;
      for (let t = 0; t < 400 && !spot; t++) {
        const [dr, dc] = r.pick(dirs), r0 = r.int(0, size - 1), c0 = r.int(0, size - 1);
        const er = r0 + dr * (w.L.length - 1), ec = c0 + dc * (w.L.length - 1);
        if (er < 0 || ec < 0 || er >= size || ec >= size) continue;
        let ok = true;
        for (let i = 0; i < w.L.length && ok; i++) { const x = grid[r0 + dr * i][c0 + dc * i]; ok = !x || x === w.L[i]; }
        if (ok) spot = [r0, c0, dr, dc];
      }
      if (!spot) break;
      const [r0, c0, dr, dc] = spot;
      for (let i = 0; i < w.L.length; i++) grid[r0 + dr * i][c0 + dc * i] = w.L[i];
      placed.push({ ...w, r: r0, c: c0, dr, dc });
    }
    if (placed.length < words.length) continue;
    // fill the empty squares; try again if a word now appears twice or a filler spells something unkind
    for (let f = 0; f < 40; f++) {
      const g = grid.map(row => row.map(x => x || String.fromCharCode(65 + r.int(0, 25))));
      if (placed.some(w => occurrences(g, w.L, dirs) !== 1)) continue;
      if (BLOCK.some(b => spells(g, b, grid))) continue;
      return { grid: g, placed, size };
    }
  }
  return null;
}

/* ---------- crossword ---------- */
// lay out words so each crosses another; returns {placed: [{w, df, L, r, c, dir}], rows, cols} or null
function crossword(r, words, maxDim) {
  let best = null;
  for (let attempt = 0; attempt < 50; attempt++) {
    const order = r.shuffle(words).sort((a, b) => (b.L.length - a.L.length) + (r.next() - 0.5) * 4);
    const cells = new Map();   // "r,c" -> {ch, A: bool, D: bool}
    const placed = [];
    let box = null;
    const at = (y, x) => cells.get(y + ',' + x);
    const put = (w, y, x, dir) => {
      const [dy, dx] = dir === 'A' ? [0, 1] : [1, 0];
      for (let i = 0; i < w.L.length; i++) { const k = (y + dy * i) + ',' + (x + dx * i), cell = cells.get(k) || { ch: w.L[i] }; cell[dir] = true; cells.set(k, cell); }
      placed.push({ ...w, r: y, c: x, dir });
      const ey = y + dy * (w.L.length - 1), ex = x + dx * (w.L.length - 1);
      box = box ? [Math.min(box[0], y), Math.min(box[1], x), Math.max(box[2], ey), Math.max(box[3], ex)] : [y, x, ey, ex];
    };
    const fits = (w, y, x, dir) => {   // number of crossings, or -1 if it cannot go here
      const [dy, dx] = dir === 'A' ? [0, 1] : [1, 0], L = w.L.length;
      if (at(y - dy, x - dx) || at(y + dy * L, x + dx * L)) return -1;
      let cross = 0;
      for (let i = 0; i < L; i++) {
        const yy = y + dy * i, xx = x + dx * i, cell = at(yy, xx);
        if (cell) { if (cell.ch !== w.L[i] || cell[dir]) return -1; cross++; }
        else if (at(yy + dx, xx + dy) || at(yy - dx, xx - dy)) return -1;   // side neighbours must be empty
      }
      const nb = [Math.min(box[0], y), Math.min(box[1], x), Math.max(box[2], y + dy * (L - 1)), Math.max(box[3], x + dx * (L - 1))];
      if (nb[2] - nb[0] + 1 > maxDim || nb[3] - nb[1] + 1 > maxDim) return -1;
      return cross;
    };
    const first = order[0];
    if (first.L.length > maxDim) continue;
    put(first, 0, 0, r.chance(.5) ? 'A' : 'D');
    let rest = order.slice(1);
    for (let pass = 0; pass < 2; pass++) {
      const left = [];
      for (const w of rest) {
        let opts = [];
        for (const [k, cell] of cells) {
          const [cy, cx] = k.split(',').map(Number);
          for (let i = 0; i < w.L.length; i++) {
            if (w.L[i] !== cell.ch) continue;
            for (const dir of ['A', 'D']) {
              if (cell[dir]) continue;
              const y = dir === 'A' ? cy : cy - i, x = dir === 'A' ? cx - i : cx;
              const cr = fits(w, y, x, dir);
              if (cr > 0) opts.push({ y, x, dir, score: cr * 10 + r.next() * 6 });
            }
          }
        }
        if (!opts.length) { left.push(w); continue; }
        opts.sort((a, b) => b.score - a.score);
        const o = opts[0];
        put(w, o.y, o.x, o.dir);
      }
      rest = left;
      if (!rest.length) break;
    }
    const area = (box[2] - box[0] + 1) * (box[3] - box[1] + 1);
    const score = placed.length * 1000 - area;
    if (!best || score > best.score) {
      const crossings = [...cells.values()].filter(c => c.A && c.D).length;
      best = { score, crossings, placed: placed.map(p => ({ ...p, r: p.r - box[0], c: p.c - box[1] })), rows: box[2] - box[0] + 1, cols: box[3] - box[1] + 1 };
    }
    if (best.placed.length === words.length && attempt > 12) break;
  }
  return best;
}
// fill a letter grid from placed words and number the starting squares (rows first, then columns)
function numberGrid(placed, rows, cols) {
  const g = Array.from({ length: rows }, () => Array(cols).fill(''));
  for (const p of placed) for (let i = 0; i < p.L.length; i++) g[p.r + (p.dir === 'D' ? i : 0)][p.c + (p.dir === 'A' ? i : 0)] = p.L[i];
  const num = {};
  let k = 0;
  for (let y = 0; y < rows; y++) for (let x = 0; x < cols; x++) if (placed.some(p => p.r === y && p.c === x)) num[y + ',' + x] = ++k;
  return { g, num };
}

Gen.add('word-puzzles', {
  title: 'Word Puzzles', type: 'Puzzle', data: 'words',
  fields: [
    { id: 'subject', label: 'Subject', type: 'select', options: (v, d) => subjects(d), def: 'science' },
    { id: 'band', label: 'Grades', type: 'select', def: '35',
      options: (v, d) => BANDS.filter(b => mods(d).some(m => m.subject === v.subject && m.band === b[0])) },
    { id: 'mod', label: 'Word Wall topic', type: 'select', options: (v, d) => inBand(v, d).map(m => [m.id, m.title + gradeNote(m)]) },
    { id: 'mod2', label: 'Add a second topic (optional)', type: 'select', def: '',
      options: (v, d) => [['', 'None']].concat(inBand(v, d).filter(m => m.id !== v.mod).map(m => [m.id, m.title + gradeNote(m)])) },
    { id: 'kind', label: 'Puzzle', type: 'select', options: [['search', 'Word search'], ['cross', 'Crossword']], def: 'search' },
    { id: 'list', label: 'Word search list', type: 'select', def: 'words', show: v => v.kind === 'search' && v.band !== 'k2',
      options: [['words', 'Words with their meanings'], ['clues', 'Meanings only (students work out each word)']] },
    { id: 'count', label: 'Words', type: 'select', def: '8', options: (v, d) => {
      const base = COUNTS[v.band] || COUNTS['35'];
      if (v.kind !== 'cross' || v.band === 'k2') return base;
      // bigger crosswords when the modules have the words for them (usable words, both modules together)
      const have = pool(v, d, 17).length;
      return base.concat([['12', '12 words'], ['15', '15 words']].filter(([c]) => +c <= have && !base.some(b => b[0] === c)));
    } },
  ],
  make(v, r, d) {
    const band = BANDS.find(b => b[0] === v.band) ? v.band : '35', bandName = BANDS.find(b => b[0] === band)[1];
    const m1 = byId(d, v.mod), m2 = v.mod2 ? byId(d, v.mod2) : null;
    const search_ = v.kind !== 'cross';
    const maxDim = band === 'k2' ? 11 : +v.count <= 8 ? 13 : +v.count <= 12 ? 15 : 17;   // crossword size limit
    const maxLen = search_ ? CAP[band] : maxDim;
    let all = pool(v, d, maxLen);
    // in a word search a word hidden inside another (ART in ARTIST) would show up twice, so keep only the longer one
    const rev = x => x.split('').reverse().join('');
    const inside = search_ ? all.filter(w => all.some(o => o !== w && (o.L.includes(w.L) || o.L.includes(rev(w.L))))) : [];
    all = all.filter(w => !inside.includes(w));
    const want = Math.min(+v.count, all.length);
    const clues = search_ && band !== 'k2' && v.list === 'clues';
    const parts = [], items = [];
    let teacher = '', skipped = [], extra = {};
    // a model from a word on another module, so it gives nothing away
    const used = new Set(all.map(x => x.L));
    // prefer a word from the same subject, so an art puzzle does not model with a math word
    const spareIn = same => mods(d).filter(m => m.band === band && m.id !== v.mod && m.id !== v.mod2 && (!same || m.subject === v.subject)).flatMap(m => m.words)
      .filter(([w, df]) => /^[a-z]{4,7}$/i.test(w) && !used.has(letters(w)) && df.length < 50 && !/\bnull\b/.test(df));
    const spare = spareIn(true).length ? spareIn(true) : spareIn(false);
    const ex = spare.length ? r.pick(spare) : ['tool', 'something you use to help you do a job'];
    const EX = letters(ex[0]);
    if (search_) {
      let words = r.sample(all, want), res = search(r, words, band);
      while (!res && words.length > 3) { skipped.push(words.pop()); res = search(r, words, band); }
      if (!res) { words = []; res = { grid: [['A']], placed: [], size: 1 }; }
      const { grid, placed } = res;
      const hit = new Set();
      for (const p of placed) for (let i = 0; i < p.L.length; i++) hit.add((p.r + p.dr * i) + ',' + (p.c + p.dc * i));
      const table = `<table class="gen-grid gen-ws${grid.length <= 10 ? ' gen-ws-big' : ''}" aria-label="Word search grid, ${grid.length} by ${grid.length} letters">` +
        grid.map((row, y) => `<tr>${row.map((ch, x) => `<td${hit.has(y + ',' + x) ? ' class="gen-hit"' : ''}>${ch}</td>`).join('')}</tr>`).join('') + '</table>';
      const shown = r.shuffle(placed);
      const dirName = ([dr, dc]) => ({ '0,1': 'across', '1,0': 'down', '1,1': 'diagonal down', '-1,1': 'diagonal up', '0,-1': 'backwards across', '-1,0': 'up', '-1,-1': 'backwards diagonal up', '1,-1': 'backwards diagonal down' }[dr + ',' + dc]);
      for (const p of shown) items.push({ q: `Find ${p.L}`, a: `row ${p.r + 1}, column ${p.c + 1}, ${dirName([p.dr, p.dc])}`, word: p.w, L: p.L, r: p.r, c: p.c, dr: p.dr, dc: p.dc, kind: 'search' });
      const listHtml = clues
        ? `<ol class="ws-fill gen-wsclues">${shown.map(p => `<li>${esc(mask(p.w, p.df))} ${note(p.w) ? `<i>${note(p.w)}</i> ` : ''}<span class="gen-cnt">(${p.L.length} letters)</span><br>${blank(p.w, Math.max(6, p.w.length * 0.62 + 1.4))}</li>`).join('')}</ol>`
        : `<ul class="gen-wslist">${shown.map(p => `<li><span class="gen-box-tick"></span><b>${esc(p.w)}</b>${band === 'k2' ? '' : `: ${esc(mask(p.w, p.df))}`}</li>`).join('')}</ul>`;
      parts.push(part('', example(clues
        ? `Clue: <i>${esc(mask(ex[0], ex[1]))}</i> (${EX.length} letters). The word is <b>${esc(ex[0])}</b>. Write it on the line, then find ${esc(EX)} in the grid and circle it.`
        : `Look for the letters <b>${esc(EX.split('').join(' '))}</b> in a row. When you find <b>${esc(ex[0])}</b>, circle the whole word and check it off the list.`,
        DIRWORDS[band] + (placed.some(p => /[\s-]/.test(p.w)) ? ' Words with two parts have no space or hyphen in the grid.' : ''))));
      parts.push(part('Find the words', `<div class="gen-wswrap">${table}</div>`));
      parts.push(part(clues ? 'Clues: write the word, then find it' : (band === 'k2' ? 'Words to find' : 'Words to find, with their meanings'), listHtml));
      extra = { grid };
      teacher = `<h3>Where the words are</h3><ul>${shown.map(p => `<li><b>${esc(p.w)}</b>: starts at row ${p.r + 1}, column ${p.c + 1}, goes ${dirName([p.dr, p.dc])}</li>`).join('')}</ul>`;
    } else {
      const chosen = r.sample(all, want);
      let cw = crossword(r, chosen, maxDim) || { placed: [], rows: 1, cols: 1 };
      // swap in other words from the module for any that would not cross
      if (cw.placed.length < chosen.length && all.length > chosen.length) {
        const spareW = all.filter(w => !chosen.includes(w));
        const keep = chosen.filter(w => cw.placed.some(p => p.L === w.L));
        const cw2 = crossword(r, keep.concat(r.sample(spareW, chosen.length - keep.length)), maxDim);
        if (cw2 && cw2.placed.length > cw.placed.length) cw = cw2;
      }
      skipped = chosen.filter(w => !cw.placed.some(p => p.L === w.L));
      const { g, num } = numberGrid(cw.placed, cw.rows, cw.cols);
      const placed = cw.placed.map(p => ({ ...p, num: num[p.r + ',' + p.c] }));
      const cell = (y, x) => { const ch = g[y][x]; if (!ch) return '<td class="gen-cw-x"></td>';
        const n = num[y + ',' + x]; return `<td>${n ? `<i>${n}</i>` : ''}<span class="ws-ans">${ch}</span></td>`; };
      const table = `<table class="gen-cw${cw.cols <= 9 && cw.rows <= 9 ? ' gen-cw-big' : cw.cols > 13 || cw.rows > 13 ? ' gen-cw-small' : ''}" aria-label="Crossword grid, ${cw.rows} rows by ${cw.cols} columns">` +
        g.map((row, y) => `<tr>${row.map((_, x) => cell(y, x)).join('')}</tr>`).join('') + '</table>';
      const list = dir => placed.filter(p => p.dir === dir).sort((a, b) => a.num - b.num);
      const clueLi = p => `<li><b>${p.num}.</b> ${esc(mask(p.w, p.df))} ${note(p.w) ? `<i>${note(p.w)}</i>` : ''}<span class="ws-keyonly gen-cwans"> ${esc(p.w)}</span></li>`;
      for (const p of placed) items.push({ q: `${p.num} ${p.dir === 'A' ? 'Across' : 'Down'}`, a: p.L, word: p.w, L: p.L, r: p.r, c: p.c, dir: p.dir, num: p.num, kind: 'cross' });
      parts.push(part('', example(`Clue: <b>1 Down.</b> <i>${esc(mask(ex[0], ex[1]))}</i>`,
        `The word is <b>${esc(ex[0])}</b>. Start in the box with a small 1 and write one letter in each box going down: ${esc(EX.split('').join(' '))}.`,
        'Across words go left to right. Down words go top to bottom. Where two words cross, they share a letter.' +
        (placed.some(p => /[\s-]/.test(p.w)) ? ' Words with two parts go in with no space or hyphen.' : ''))));
      parts.push(part('Crossword', `<div class="gen-wswrap">${table}</div>`));
      parts.push(part('Clues', `<div class="gen-cwclues"><div><h3>Across</h3><ul>${list('A').map(clueLi).join('')}</ul></div><div><h3>Down</h3><ul>${list('D').map(clueLi).join('')}</ul></div></div>`));
      extra = { cw: { rows: cw.rows, cols: cw.cols, placed: placed.map(p => ({ L: p.L, r: p.r, c: p.c, dir: p.dir, num: p.num })) } };
    }
    if (skipped.length) teacher += `<h3>Left out</h3><p>These words would not fit this ${search_ ? 'grid' : 'crossword'}, so they are not on this sheet: ${skipped.map(w => esc(w.w)).join(', ')}. Press New sheet for a different layout.</p>`;
    const why = [];
    for (const [w] of [v.mod, v.mod2].map(id => id && byId(d, id)).filter(Boolean).flatMap(m => m.words)) {
      if (/[0-9\/×=+]/.test(w)) why.push(`${esc(w)} (has numbers or symbols)`);
      else if (letters(w).length < 3) why.push(`${esc(w)} (too short)`);
      else if (letters(w).length > maxLen) why.push(`${esc(w)} (${letters(w).length} letters, too long for this ${search_ ? 'grid' : 'crossword'})`);
    }
    for (const w of inside) why.push(`${esc(w.w)} (hidden inside a longer word on the list, so it would show up twice)`);
    if (why.length) teacher += `<h3>Not used in this puzzle</h3><p>${why.join('; ')}. The Vocabulary Practice generator uses every word.</p>`;
    const n = items.length;
    const name = `${m1 ? m1.title : 'Word Wall'}${m2 ? ' and ' + m2.title : ''}`;
    return {
      title: `${name}: ${search_ ? 'Word Search' : 'Crossword'}`, eyebrow: 'Puzzle',
      level: `${bandName}, ${m1 ? m1.s : ''}, ${n} words`,
      ican: search_ ? `I can find ${band === 'k2' ? 'words' : 'vocabulary words'} and ${clues ? 'work out each word from its meaning' : 'read what each one means'}.` : 'I can use the meaning of a word to fill in a crossword.',
      directions: search_ ? (clues ? 'Read each meaning and write the word on the line. Then find the word in the grid and circle it.' : `Find each word in the grid and circle it. Check off each word on the list when you find it. ${DIRWORDS[band]}`)
        : 'Read each clue. Write the word in the boxes that start at the clue\'s number, one letter in each box.',
      minutes: n > 8 ? 25 : 20, materials: 'pencil' + (search_ ? ', highlighter (optional)' : ''),
      parts, items, teacher, ...extra,
      mistakes: search_ ? 'Circling part of a longer word, or stopping when a word bends: words always run in a straight line.'
        : 'Starting a word in the wrong box, and counting boxes wrong. A word that does not fit the number of boxes is the wrong word; check the crossing letters.',
      notes: (search_ ? 'The key shades every square that belongs to a word. ' : 'The crossword is laid out fresh for each sheet code, and every word crosses at least one other. ') +
        'Clues are the Word Wall meanings; if a word appears inside its own meaning it is shown as a blank. Add a second topic for a longer puzzle.',
    };
  },
  verify(s, v, d) {
    const out = [];
    const dict = new Map();
    for (const id of [v.mod, v.mod2]) { const m = id && (d.modules || []).find(x => x.id === id); if (m) for (const [w] of m.words) dict.set(w.replace(/[^A-Za-z]/g, '').toUpperCase(), w); }
    if (s.grid) {
      const g = s.grid, n = g.length;
      const dirs = DIRS[v.band] || DIRS['35'];
      for (const it of s.items) {
        if (!dict.has(it.L)) out.push(`${it.L} is not a word from the module`);
        if (!dirs.some(([a, b]) => a === it.dr && b === it.dc)) out.push(`${it.L} runs in a direction not allowed at this grade`);
        let got = '';
        for (let i = 0; i < it.L.length; i++) { const y = it.r + it.dr * i, x = it.c + it.dc * i; got += y >= 0 && x >= 0 && y < n && x < n ? g[y][x] : '?'; }
        if (got !== it.L) out.push(`${it.L}: the grid says ${got} at the claimed spot`);
        if (occurrences(g, it.L, dirs) !== 1) out.push(`${it.L} appears ${occurrences(g, it.L, dirs)} times`);
      }
      if (g.some(row => row.length !== n || row.some(ch => !/^[A-Z]$/.test(ch)))) out.push('grid has a gap or a non-letter');
    }
    if (s.cw) {
      const { rows, cols, placed } = s.cw;
      const g = Array.from({ length: rows }, () => Array(cols).fill(''));
      for (const p of placed) {
        if (!dict.has(p.L)) out.push(`${p.L} is not a word from the module`);
        for (let i = 0; i < p.L.length; i++) {
          const y = p.r + (p.dir === 'D' ? i : 0), x = p.c + (p.dir === 'A' ? i : 0);
          if (y >= rows || x >= cols) { out.push(`${p.L} runs off the grid`); break; }
          if (g[y][x] && g[y][x] !== p.L[i]) out.push(`${p.L} and another word disagree at row ${y + 1}, column ${x + 1}`);
          g[y][x] = p.L[i];
        }
      }
      // every run of two or more letters must be exactly one placed word, starting where the word starts
      const runs = [];
      for (let y = 0; y < rows; y++) for (let x = 0; x < cols; x++) {
        if (g[y][x] && !(x > 0 && g[y][x - 1]) && x + 1 < cols && g[y][x + 1]) { let L = ''; for (let k = x; k < cols && g[y][k]; k++) L += g[y][k]; runs.push(['A', y, x, L]); }
        if (g[y][x] && !(y > 0 && g[y - 1][x]) && y + 1 < rows && g[y + 1][x]) { let L = ''; for (let k = y; k < rows && g[k][x]; k++) L += g[k][x]; runs.push(['D', y, x, L]); }
      }
      for (const [dir, y, x, L] of runs) if (!placed.some(p => p.dir === dir && p.r === y && p.c === x && p.L === L)) out.push(`stray ${dir === 'A' ? 'across' : 'down'} letters ${L} at row ${y + 1}, column ${x + 1}`);
      if (runs.length !== placed.length) out.push(`${runs.length} letter runs for ${placed.length} words`);
      // numbering: squares that start a word, counted rows first
      let k = 0; const want = {};
      for (let y = 0; y < rows; y++) for (let x = 0; x < cols; x++) if (runs.some(([, ry, rx]) => ry === y && rx === x)) want[y + ',' + x] = ++k;
      for (const p of placed) if (want[p.r + ',' + p.c] !== p.num) out.push(`${p.L} is numbered ${p.num}, should be ${want[p.r + ',' + p.c]}`);
      // every word is joined to the rest
      if (placed.length > 1) {
        const cellsOf = p => Array.from({ length: p.L.length }, (_, i) => (p.r + (p.dir === 'D' ? i : 0)) + ',' + (p.c + (p.dir === 'A' ? i : 0)));
        const seen = new Set([0]), stack = [0];
        while (stack.length) { const a = cellsOf(placed[stack.pop()]); placed.forEach((q, j) => { if (!seen.has(j) && cellsOf(q).some(c => a.includes(c))) { seen.add(j); stack.push(j); } }); }
        if (seen.size !== placed.length) out.push('some words do not connect to the rest');
      }
      for (const it of s.items) if (it.a !== it.L || !placed.some(p => p.L === it.a && p.num === it.num)) out.push(`clue ${it.q}: key ${it.a} not in the grid`);
    }
    if (s.items.length < 3) out.push(`only ${s.items.length} words`);
    return out;
  },
  css: `.gen-wswrap { display: flex; justify-content: center; }
.gen-ws td { width: 0.3in; height: 0.3in; font: 600 16px var(--sans); }
.gen-ws-big td { width: 0.4in; height: 0.4in; font-size: 21px; }
.gen-wslist { list-style: none; padding: 0; margin: 4px 0; columns: 2; column-gap: 24px; font-size: 14px; }
.gen-wslist li { margin: 0 0 5px; break-inside: avoid; }
.gen-box-tick { display: inline-block; width: .85em; height: .85em; border: 1.5px solid #333; border-radius: 2px; margin-right: 6px; vertical-align: -1px; }
.gen-wsclues { columns: 2; column-gap: 24px; font-size: 14px; }
.gen-wsclues li { break-inside: avoid; }
.gen-cnt { color: #555; font-size: 12.5px; }
.gen-cw { border-collapse: collapse; margin: 4px auto; }
.gen-cw td { width: 0.3in; height: 0.3in; border: 1.5px solid #222; position: relative; text-align: center; vertical-align: middle; padding: 0; font: 700 15px var(--sans); }
.gen-cw-big td { width: 0.38in; height: 0.38in; font-size: 18px; }
.gen-cw-small td { width: 0.25in; height: 0.25in; font-size: 13px; }
.gen-cw-small td i { font-size: 7.5px; }
.gen-cw td.gen-cw-x { border: 0; }
.gen-cw td i { position: absolute; top: 1px; left: 2px; font: 600 8.5px/1 var(--sans); font-style: normal; }
.gen-cwclues { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; font-size: 14px; }
.gen-cwclues h3 { font-size: 14px; margin: 0 0 4px; text-transform: uppercase; letter-spacing: .08em; }
.gen-cwclues ul { list-style: none; padding: 0; margin: 0; }
.gen-cwclues li { margin: 0 0 5px; }
.gen-cwans { color: #b03020; font-weight: 700; }
@media print { .gen-wslist, .gen-wsclues, .gen-cwclues { font-size: 9.5pt; }
  .gen-ws td { width: 0.26in; height: 0.26in; font-size: 11.5pt; } .gen-ws-big td { width: 0.36in; height: 0.36in; font-size: 15pt; }
  .gen-cw td { width: 0.28in; height: 0.28in; } .gen-cw-big td { width: 0.34in; height: 0.34in; } .gen-cw-small td { width: 0.23in; height: 0.23in; font-size: 10pt; } }`,
});
})();
