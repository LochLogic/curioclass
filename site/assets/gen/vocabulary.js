// Vocabulary Practice generator, grades K-12. Reads the Word Wall list (words.json): pick a subject, a grade band and a
// module (and an optional second module for small lists). Part 1 matches words to meanings, Part 2 writes the word that
// fits each meaning from a word bank, Part 3 (grades 3-12) uses words in the student's own sentences.
(() => {
const { blank, part, example, esc, lines } = Gen.h;

const BANDS = [['k2', 'Grades K-2'], ['35', 'Grades 3-5'], ['68', 'Grades 6-8'], ['912', 'Grades 9-12']];
const COUNTS = { k2: [['4', '4 words'], ['5', '5 words'], ['6', '6 words']],
  35: [['6', '6 words'], ['8', '8 words'], ['10', '10 words']],
  68: [['6', '6 words'], ['8', '8 words'], ['10', '10 words'], ['12', '12 words']],
  912: [['6', '6 words'], ['8', '8 words'], ['10', '10 words'], ['12', '12 words']] };
const LET = 'ABCDEFGHIJKLMNOP';
const mods = d => (d && d.modules) || [];
const subjects = d => { const seen = new Map(); for (const m of mods(d)) if (!seen.has(m.subject)) seen.set(m.subject, m.s);
  return [...seen].sort((a, b) => a[1].localeCompare(b[1])); };
const inBand = (v, d) => mods(d).filter(m => m.subject === v.subject && m.band === v.band);
const gradeNote = m => /^\d+$/.test(m.grade) ? ` (grade ${m.grade})` : m.grade === 'k' ? ' (kindergarten)' : '';
const byId = (d, id) => mods(d).find(m => m.id === id);

// hide the word (and its close forms) when a meaning is shown as a clue
function mask(word, def) {
  const w = word.trim();
  const reEsc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  let re;
  if (/\s/.test(w)) re = new RegExp(reEsc(w), 'gi');
  else if (w.length < 3) re = new RegExp(`\\b${reEsc(w)}\\b`, 'gi');
  else { const stem = w.length >= 5 ? w.slice(0, Math.max(4, w.length - 2)) : w; re = new RegExp(`\\b${reEsc(stem)}[a-z]*`, 'gi'); }
  return def.replace(re, '_____');
}

// the words for a sheet: the module, plus the second module when chosen; no repeated word or meaning
function pool(v, d) {
  const out = [], seen = new Set();
  for (const id of [v.mod, v.mod2]) {
    const m = id && byId(d, id);
    if (!m) continue;
    for (const [w, df] of m.words) {
      const k1 = 'w:' + w.toLowerCase(), k2 = 'd:' + df.toLowerCase();
      if (seen.has(k1) || seen.has(k2)) continue;
      seen.add(k1); seen.add(k2); out.push([w, df]);
    }
  }
  return out;
}

Gen.add('vocabulary', {
  title: 'Vocabulary Practice', type: 'Vocabulary', data: 'words',
  fields: [
    { id: 'subject', label: 'Subject', type: 'select', options: (v, d) => subjects(d), def: 'science' },
    { id: 'band', label: 'Grades', type: 'select', def: '35',
      options: (v, d) => BANDS.filter(b => mods(d).some(m => m.subject === v.subject && m.band === b[0])) },
    { id: 'mod', label: 'Word Wall module', type: 'select', options: (v, d) => inBand(v, d).map(m => [m.id, m.title + gradeNote(m)]) },
    { id: 'mod2', label: 'Add a second module (optional)', type: 'select', def: '',
      options: (v, d) => [['', 'None']].concat(inBand(v, d).filter(m => m.id !== v.mod).map(m => [m.id, m.title + gradeNote(m)])) },
    { id: 'count', label: 'Words', type: 'select', options: v => COUNTS[v.band] || COUNTS['35'], def: '6' },
  ],
  make(v, r, d) {
    const k2 = v.band === 'k2', band = BANDS.find(b => b[0] === v.band) || BANDS[1];
    const m1 = byId(d, v.mod), m2 = v.mod2 ? byId(d, v.mod2) : null;
    const all = pool(v, d);
    const n = Math.min(+v.count, all.length);
    const words = r.sample(all, n);                       // [word, definition]
    // Part 1: match. Words in a numbered list, meanings lettered in a shuffled order.
    const defs = r.shuffle(words.map(w => w[1]));
    const items = words.map(([w, df], i) => ({ q: `Match: ${w}`, a: LET[defs.indexOf(df)], word: w, opts: defs, part: 1, n: i + 1 }));
    const matchHtml = `<div class="ws-match gen-vmatch"><ol>${words.map(([w]) => `<li><b>${esc(w)}</b> ${blank(LET[defs.indexOf(words.find(x => x[0] === w)[1])], 2.4)}</li>`).join('')}</ol>` +
      `<ul>${defs.map((df, i) => `<li><b>${LET[i]}.</b> ${esc(mask(words.find(x => x[1] === df)[0], df))}</li>`).join('')}</ul></div>`;
    // Part 2: the word that fits each meaning, from a word bank, in a new order
    const order = r.shuffle(words);
    const bank = r.shuffle(words.map(w => w[0]));
    // every blank is the same width, so its length does not give the word away
    const wide = Math.min(11, Math.max(...words.map(([w]) => w.length)) * 0.62 + 1.6);
    const frame = (w, df) => { const md = esc(mask(w, df));
      return /^to /i.test(df) ? `To ${blank(w, wide)} means ${md}.` : `The word ${blank(w, wide)} means ${md}.`; };
    const fillItems = order.map(([w, df]) => ({ q: `Fill: ${df}`, a: w, word: w, def: df, part: 2 }));
    const fillHtml = `<div class="gen-wordbank">${bank.map(w => `<span>${esc(w)}</span>`).join('')}</div>` +
      `<ol class="ws-fill gen-vfill" start="${n + 1}">${order.map(([w, df]) => `<li>${frame(w, df)}</li>`).join('')}</ol>`;
    // a model from a word that is not on this sheet (another module at the same grades)
    const used = new Set(all.map(x => x[0].toLowerCase()));
    // prefer a word from the same subject, so an art sheet does not model with a math word
    const spareIn = same => mods(d).filter(m => m.band === v.band && m.id !== v.mod && m.id !== v.mod2 && (!same || m.subject === v.subject))
      .flatMap(m => m.words).filter(([w, df]) => !used.has(w.toLowerCase()) && df.length < 60 && !/\s/.test(w) && !/\bnull\b/.test(df));
    const spare = spareIn(true).length ? spareIn(true) : spareIn(false);
    const ex = spare.length ? r.pick(spare) : ['tool', 'something you use to help you do a job'];
    const exHtml = example(
      `<b>${esc(ex[0])}</b> <span class="gen-vexl">C</span> &nbsp; &nbsp; ... &nbsp; <b>C.</b> ${esc(mask(ex[0], ex[1]))}`,
      `Part 1: meaning C fits <b>${esc(ex[0])}</b>, so write <b>C</b> next to it. Part 2: write <b>${esc(ex[0])}</b> on the line before its meaning.`);
    const own = [];
    const big = html => k2 ? `<div class="gen-vk2">${html}</div>` : html;
    const parts = [part('', exHtml),
      part('Part 1: Match each word to its meaning', big(matchHtml)),
      part('Part 2: Write the word that fits', big(fillHtml))];
    if (k2) parts.push(part('Part 3: Draw it', `<p class="ws-text">Draw a picture of one word. Write the word under your picture.</p><div class="ws-draw gen-vdraw"><span>My picture</span></div>`));
    else {
      const k = v.band === '35' ? 1 : 2;
      for (let i = 0; i < k; i++) own.push({ q: `Own sentence ${i + 1}`, a: 'Answers vary: the sentence uses a word from the box correctly and shows what it means.', part: 3 });
      parts.push(part('Part 3: Use it in a sentence',
        `<p class="ws-text">${k === 1 ? 'Choose one word from the box. Write a sentence that uses the word and shows what it means.' : 'Choose two different words from the box. Write one sentence for each that uses the word and shows what it means.'}</p>` +
        Array.from({ length: k }, (_, i) => `<p class="ws-text gen-vown">${i + 1 + 2 * n}. Word: ${'<span class="ws-blank" style="min-width:9em"></span>'}</p>${lines(2)}`).join('')));
    }
    void own;
    const title = `${m1 ? m1.title : 'Vocabulary'}${m2 ? ' and ' + m2.title : ''}: Vocabulary`;
    return {
      title, level: `${band[1]}, ${m1 ? m1.s : ''}${n < +v.count ? `, ${n} words (all the module has)` : ''}`,
      ican: `I can match ${k2 ? 'words' : 'vocabulary words'} to their meanings and use them${k2 ? '.' : ' in my own sentences.'}`,
      directions: k2 ? 'Write the letter of the meaning next to each word. Then write the word from the box that fits on each line.'
        : 'Part 1: write the letter of the matching meaning on the line. Part 2: write a word from the box on each line. Use each word once. Part 3: write your own sentence.',
      minutes: k2 ? 15 : n > 8 ? 25 : 20, materials: k2 ? 'pencil, crayons' : 'pencil',
      parts, items: items.concat(fillItems, own),
      mistakes: 'Matching by a single shared word instead of the whole meaning, and in Part 3 sentences that use the word but do not show what it means ("I like photosynthesis").',
      notes: 'Part 2 asks for the same words from the other direction, meaning to word. For a harder check, fold the sheet so Part 1 is hidden. If the word appears inside its own meaning it is shown as a blank. Add a second module when one module has only a few words.',
    };
  },
  verify(s, v, d) {
    const out = [];
    const dict = new Map();
    for (const id of [v.mod, v.mod2]) { const m = id && (d.modules || []).find(x => x.id === id); if (m) for (const [w, df] of m.words) if (!dict.has(w.toLowerCase())) dict.set(w.toLowerCase(), df); }
    const letters = new Set();
    for (const it of s.items) {
      if (it.part === 1) {
        const want = dict.get(it.word.toLowerCase());
        const i = 'ABCDEFGHIJKLMNOP'.indexOf(it.a);
        if (!want) out.push(`${it.word}: not in the chosen modules`);
        else if (it.opts[i] !== want) out.push(`${it.word}: key letter ${it.a} points to "${it.opts[i]}", should be "${want}"`);
        if (letters.has(it.a)) out.push(`letter ${it.a} used twice`); letters.add(it.a);
      } else if (it.part === 2) {
        if (dict.get(it.a.toLowerCase()) !== it.def) out.push(`fill "${it.def}": key ${it.a} does not match the module`);
        if (mask(it.a, it.def).toLowerCase().includes(it.a.toLowerCase()) && it.a.length > 2) out.push(`fill "${it.def}": the clue shows the answer`);
      }
    }
    const p1 = s.items.filter(i => i.part === 1).length, p2 = s.items.filter(i => i.part === 2).length;
    if (p1 !== p2) out.push(`part 1 has ${p1} words, part 2 has ${p2}`);
    if (p1 < 4) out.push(`only ${p1} words`);
    return out;
  },
  css: `.gen-vexl { display: inline-block; min-width: 2.4em; border-bottom: 1.5px solid #222; text-align: center; font-weight: 700; }
.gen-vmatch ol li { margin-bottom: 12px; }
.gen-vmatch ul li { margin-bottom: 8px; }
.gen-vfill li { margin-bottom: 12px; }
.gen-vown { margin-top: 10px; }
.gen-vk2 { font-size: 19px; }
.gen-vk2 .gen-wordbank { font-size: 22px; }
.gen-vdraw { height: 1.7in; }
@media print { .gen-vk2 { font-size: 13pt; } .gen-vk2 .gen-wordbank { font-size: 15pt; } .gen-vdraw { height: 1.15in; }
  .gen-vmatch ol li, .gen-vmatch ul li { margin-bottom: 5px; } .gen-vfill li { margin-bottom: 7px; } .gen-vown { margin: 4px 0 0; }
  .gen-vk2 .gen-vmatch ol li, .gen-vk2 .gen-vfill li { margin-bottom: 9px; } }`,
});
})();
