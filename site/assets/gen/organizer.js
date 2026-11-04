// Graphic Organizer Maker, grades K-12. A layout generator: no computed answers (noKey), but the guiding prompts, the
// sentence starters and the idea lines are drawn from banks, so New sheet gives a fresh wording of the same organizer.
// The topic goes in the heading (and, for Venn and compare layouts, "A and B" fills the circle and column names).
// Grade band sets the box count, the writing space and the wording; the teacher page holds a filled-in model.
// Optional settings: row labels (fill the rows of the compare chart, the steps, the chain links and the cause and effect
// boxes; extra labels add rows, up to 8), 2 to 4 subjects with typed column headers for the compare chart, and a T-chart
// (two-column sort) with its own headers and a cut-out strip of cards to sort.
(() => {
const { esc } = Gen.h;

const BANDS = [['k2', 'Grades K-2'], ['35', 'Grades 3-5'], ['68', 'Grades 6-8'], ['912', 'Grades 9-12']];
const LAYOUTS = [
  ['venn2', 'Venn diagram, 2 circles'], ['venn3', 'Venn diagram, 3 circles'], ['compare', 'Compare and contrast chart'],
  ['cause', 'Cause and effect'], ['chain', 'Cause chain'], ['main', 'Main idea and details'], ['sequence', 'Sequence / flow chart'],
  ['cer', 'Claim, evidence, reasoning'], ['kwl', 'KWL chart'], ['problem', 'Problem and solution'], ['web', 'Concept web'],
  ['story', 'Story map'], ['frayer', 'Frayer model'], ['tchart', 'T-chart (two-column sort)'],
];
const NAME = Object.fromEntries(LAYOUTS);
const GROW = /*GROW*/{"venn2-k2":2.17,"venn2-35":2.07,"venn2-68":1.82,"venn2-912":2.4,"venn3-k2":1.07,"venn3-68":0.86,"venn3-912":0.82,"compare-k2":1.23,"compare-35":1.35,"compare-68":1.31,"compare-912":1.22,"cause-k2":1.31,"cause-35":2.16,"cause-68":1.89,"cause-912":1.72,"chain-k2":1.3,"chain-68":1.24,"chain-912":1.24,"main-k2":1.32,"main-35":1.72,"main-68":1.96,"main-912":1.09,"sequence-k2":1.24,"sequence-35":1.23,"sequence-912":1.15,"cer-k2":1.14,"cer-35":1.35,"cer-68":1.37,"cer-912":1.15,"kwl-k2":1.54,"kwl-35":1.2,"kwl-68":1.25,"kwl-912":1.22,"problem-k2":0.96,"problem-35":1.13,"problem-68":0.93,"problem-912":1.14,"web-k2":0.98,"web-35":0.88,"web-68":0.78,"web-912":0.81,"story-k2":1.48,"story-35":1.24,"story-68":1.49,"story-912":1.15,"frayer-k2":1.03,"frayer-35":0.9,"frayer-68":0.98,"frayer-912":1.08,"venn3-35":0.98,"sequence-68":0.87}/*GROW*/;   // per layout and band: how much to stretch the writing space to fill the page (tuned by print tests)
const LH = { k2: 0.44, 35: 0.34, 68: 0.3, 912: 0.28 };   // ruled line spacing in inches
const young = b => b === 'k2' || b === '35';

// pieces every layout uses; r makes the prompt and starter choices, st turns sentence starters on
function kit(b, r, st, g = 1) {
  const lh = LH[b];
  const pk = x => Array.isArray(x) ? r.pick(x) : x;
  const lines = (h, starter) => {
    const n = Math.max(1, Math.round(h * g / lh));
    return `<div class="org-lines" style="--lh:${lh}in">${Array.from({ length: n }, (_, i) => `<span>${i === 0 && starter ? `<i>${esc(starter)}</i>` : ''}</span>`).join('')}</div>`;
  };
  // a labeled box: q = guiding prompt (string or bank), h = writing height in inches, draw = drawing space height, st = starter bank
  const box = (lab, o = {}) => `<div class="org-box${o.cls ? ' ' + o.cls : ''}"${o.style ? ` style="${o.style}"` : ''}>` +
    `<p class="org-head"><span class="org-lab">${lab}</span>${o.q ? ` <span class="org-q">${pk(o.q)}</span>` : ''}</p>` +
    (o.draw ? `<div class="org-draw" style="height:${(o.draw * g).toFixed(2)}in"><span>Draw</span></div>` : '') +
    (o.h ? lines(o.h, st && o.st ? pk(o.st) : '') : '') + (o.extra || '') + '</div>';
  const grid = (cols, items, cls = '') => `<div class="org-grid${cls ? ' ' + cls : ''}" style="grid-template-columns:${cols}">${items.join('')}</div>`;
  const down = (word = '') => `<div class="org-down" aria-hidden="true">&#8595;${word ? ` <span>${word}</span>` : ''}</div>`;
  const right = `<div class="org-right" aria-hidden="true">&#8594;</div>`;
  return { pk, lines, box, grid, down, right, lh, g };
}

// split "frogs and toads" or "A, B and C" into names for the Venn and compare layouts
function names(topic, n) {
  const t = String(topic || '').trim();
  if (!t) return [];
  const parts = t.split(/\s*,\s*(?:and\s+)?|\s+(?:and|vs\.?|versus|&)\s+/i).map(s => s.trim()).filter(Boolean);
  return parts.length === n && parts.every(p => p.length <= 28) ? parts : [];
}
const cap = s => s.charAt(0).toUpperCase() + s.slice(1);
// "size, color, where it lives" -> up to max short labels; text with no commas is one label (none when blank)
function list(text, max = 8, maxLen = 40) {
  return String(text || '').split(',').map(x => x.trim()).filter(Boolean).map(x => x.length > maxLen ? x.slice(0, maxLen - 1).trim() + '.' : x).slice(0, max);
}

/* ---------- the layouts: each returns the organizer html ---------- */
const BUILD = {
  venn(b, K, nm, n) {
    const W = 720, k2 = b === 'k2';
    const lab = (s, x, y) => {
      if (!s) return `<line x1="${x - 95}" y1="${y + 4}" x2="${x + 95}" y2="${y + 4}" stroke="#222" stroke-width="1.5"/>`;
      const size = Math.min(22, 190 / (s.length * 0.56));
      return `<text x="${x}" y="${y}" text-anchor="middle" font-size="${size.toFixed(1)}" font-weight="700" fill="#222">${esc(cap(s))}</text>`;
    };
    let svg, H;
    if (n === 2) {
      const R = 214, cy = 262; H = cy + R + 8;
      svg = `<circle cx="263" cy="${cy}" r="${R}" fill="none" stroke="#222" stroke-width="2.4"/><circle cx="457" cy="${cy}" r="${R}" fill="none" stroke="#222" stroke-width="2.4"/>` +
        lab(nm[0], 150, 26) + lab(nm[1], 570, 26) + `<text x="360" y="26" text-anchor="middle" font-size="18" font-weight="700" fill="#555">Both</text>`;
    } else {
      const R = 178; H = 590;
      svg = [[280, 226], [440, 226], [360, 364]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="${R}" fill="none" stroke="#222" stroke-width="2.4"/>`).join('') +
        lab(nm[0], 165, 26) + lab(nm[1], 555, 26) + lab(nm[2], 360, 580) +
        `<text x="360" y="276" text-anchor="middle" font-size="12" fill="#777">all three</text>`;
    }
    const label = n === 2 ? `Venn diagram with two overlapping circles${nm.length ? ': ' + nm.join(' and ') : ''}` : `Venn diagram with three overlapping circles${nm.length ? ': ' + nm.join(', ') : ''}`;
    const pic = Gen.h.svg(W, H, svg, label);
    const A = nm[0] || 'the first one', B = nm[1] || 'the second one';
    const after = k2
      ? K.grid('1fr 1fr', [
        K.box('Alike', { q: n === 2 ? ['How are they the same?', 'What do they both have or do?'] : ['What do all three have?', 'How are all three the same?'], h: 0.9, st: n === 2 ? ['They both', 'They are alike because'] : ['All three', 'They are alike because'] }),
        K.box('Different', { q: n === 2 ? ['How are they not the same?', 'What is one big difference?'] : ['Which one is most different? How?', 'What is one big difference?'], h: 0.9, st: ['One is different because', 'Only one of them'] })])
      : K.box('Sum it up', {
        q: n === 2 ? ['Are they more alike or more different? Explain.', 'What is the most important difference? Why does it matter?', 'Write two sentences: one way they are alike and one way they differ.']
          : ['What do all three share, and which one is most different from the others?', 'Which two are the most alike? Explain with details from the diagram.', 'Write a sentence that sums up all three.'],
        h: n === 2 ? (b === '912' ? 0.84 : 1.0) : 0.84,
        st: n === 2 ? [`Both ${A} and ${B}`, `Although ${A} and ${B} both`, `The biggest difference is that`, `${cap(A)} and ${B} are more alike than different because`]
          : ['All three', 'The two that are most alike are', 'Of the three, the one that stands out is'] });
    return pic + after;
  },
  venn2: (b, K, c) => BUILD.venn(b, K, names(c.topic, 2), 2),
  venn3: (b, K, c) => BUILD.venn(b, K, names(c.topic, 3), 3),

  compare(b, K, c) {
    const n = Math.min(4, Math.max(2, +c.subjects || 2));
    const typed = list(c.cols, n, 28), nm = typed.length ? typed : names(c.topic, n);
    const subj = Array.from({ length: n }, (_, i) => nm[i] ? esc(cap(nm[i])) : '');
    const head = s => s || '<span class="org-hblank"></span>';
    const set = { k2: { rows: 3, h: 1.35, first: 'Look at', last: '', w: [24, 0] },
      35: { rows: 4, h: 1.0, first: 'What we compare', last: 'Same or different?', w: [22, 18] },
      68: { rows: 5, h: 0.86, first: 'Point of comparison', last: 'Alike or different? How?', w: [20, 24] },
      912: { rows: 6, h: 0.78, first: 'Criterion', last: 'Why the difference matters', w: [18, 28] } }[b];
    const cols = [set.first, ...subj.map(head), ...(set.last ? [set.last] : [])];
    const share = (100 - set.w[0] - set.w[1]) / n;
    const widths = [set.w[0], ...subj.map(() => share), ...(set.last ? [set.w[1]] : [])];
    const ideas = { k2: [['size', 'color', 'where it lives', 'what it eats'], ['how it looks', 'how it moves', 'where it is', 'what it does'], ['shape', 'sound', 'where you find it', 'how we use it']],
      35: [['looks', 'where or when', 'how it works', 'what it needs'], ['size', 'parts', 'uses', 'good and bad points'], ['characters', 'setting', 'problem', 'lesson']],
      68: [['purpose', 'structure', 'causes', 'effects', 'who it affects'], ['features', 'time and place', 'strengths', 'weaknesses', 'impact'], ['process', 'inputs', 'outputs', 'uses', 'limits']],
      912: [['purpose', 'structure', 'causes', 'consequences', 'scale', 'perspective'], ['origins', 'key features', 'strengths', 'limitations', 'evidence', 'long-term impact'], ['assumptions', 'methods', 'outcomes', 'costs', 'who benefits', 'significance']] }[b];
    const labels = c.rows || [], nRows = Math.max(set.rows, labels.length);
    const h = set.h * set.rows / nRows;   // extra rows share the same space, so the sheet stays one page
    const lastCell = b === '35' ? '<p class="org-circle">same &nbsp; / &nbsp; different</p>' : '';
    const last = cols.length - 1;
    const rows = Array.from({ length: nRows }, (_, ri) => `<tr>${cols.map((_, i) => `<td style="height:${(h * K.g).toFixed(2)}in">` +
      (i === 0 && labels[ri] ? `<b class="org-rowlab">${esc(cap(labels[ri]))}</b>` : i === last && lastCell ? lastCell : K.lines(h - 0.12)) + '</td>').join('')}</tr>`).join('');
    const table = `<table class="org-table"><colgroup>${widths.map(w => `<col style="width:${w.toFixed(1)}%">`).join('')}</colgroup><thead><tr>${cols.map(x => `<th>${x}</th>`).join('')}</tr></thead><tbody>${rows}</tbody></table>`;
    const idea = labels.length ? '' : `<p class="org-ideas"><b>${b === 'k2' ? 'Things to look at' : 'Ideas for rows'}:</b> ${K.pk(ideas).join(', ')}${b === 'k2' ? '' : ', or your own'}.</p>`;
    const sum = K.box(b === 'k2' ? 'My sentence' : 'Sum it up', { q: b === 'k2' ? ['Tell one way they are the same and one way they are different.', 'What is the biggest difference?']
      : ['Overall, are they more alike or more different? Use one row of your chart as proof.', 'Which difference matters most? Explain why.', 'Write a sentence that compares them on your most important row.'],
      h: b === 'k2' ? 0.9 : 0.68, st: b === 'k2' ? ['They are the same because', 'They are different because'] : ['Overall,', 'The most important difference is', 'While both', 'Unlike'] });
    return idea + table + sum;
  },

  tchart(b, K, c) {
    const typed = list(c.cols, 2, 28), nm = typed.length ? typed : names(c.topic, 2);
    const head = s => s ? esc(cap(s)) : '<span class="org-hblank"></span>';
    const cards = c.cards || [];
    const per = b === 'k2' ? 3 : 4, strip = cards.length ? Math.ceil(cards.length / per) * (b === 'k2' ? 0.5 : 0.42) + 0.3 : 0;
    const h = Math.max(1.6, { k2: 5.0, 35: 5.9, 68: 6.2, 912: 6.3 }[b] - strip);
    const table = `<table class="org-table org-t"><thead><tr><th>${head(nm[0])}</th><th>${head(nm[1])}</th></tr></thead><tbody><tr>` +
      [0, 1].map(() => `<td style="height:${(h * K.g).toFixed(2)}in">${cards.length ? '' : K.lines(h - 0.12)}</td>`).join('') + '</tr></tbody></table>';
    const sum = K.box(b === 'k2' ? 'My sentence' : 'Sum it up', { q: b === 'k2' ? ['How did you know where each one goes?', 'Tell about one thing in each side.']
      : ['What rule did you use to sort? Was anything hard to place?', 'Which item was hardest to place? Why?', 'Write one sentence about each column.'],
      h: b === 'k2' ? 0.88 : 0.6, st: b === 'k2' ? ['I put', 'I know because'] : ['I sorted by', 'The hardest one was', 'Everything on the left'] });
    const cut = cards.length ? `<p class="org-cut">cut out the cards and sort them</p><div class="org-cards" style="--n:${per}">${cards.map(x => `<span>${esc(x)}</span>`).join('')}</div>` : '';
    return table + sum + cut;
  },

  cause(b, K, c) {
    const lab = (i, dflt) => c.rows && c.rows[i] ? esc(cap(c.rows[i])) : dflt;   // typed labels fill the boxes in order
    if (b === 'k2') {
      const pair = i => K.grid('1fr auto 1fr', [
        K.box(lab(i - 1, `${i}. Why did it happen?`), { q: ['This is the cause.', 'This is the cause. Ask: why?'], draw: 1.25, h: 0.44, st: ['Because', 'First,'] }),
        K.right,
        K.box(`${i}. What happened?`, { q: ['This is the effect.', 'This is the effect. Ask: what happened?'], draw: 1.25, h: 0.44, st: ['So', 'Then'] })]);
      return pair(1) + `<div class="org-gap"></div>` + pair(2) + K.box('My sentence', { q: ['Put one pair together in a sentence.', 'Use the word <b>because</b> in a sentence.'], h: 0.88, st: ['This happened because', 'Because of this,'] });
    }
    if (b === '35') {
      const eff = i => K.box(lab(i, `Effect ${i}`), { q: ['What happened because of the cause?', 'What was one result?', 'What changed?'], h: 0.68, st: ['As a result,', 'So', 'Because of this,'] });
      const cause = K.box(lab(0, 'Cause'), { q: ['Why did it happen? What made it happen?', 'What happened first that led to the effects?'], h: 2.4, st: ['It started when', 'The cause was'], cls: 'org-main' });
      return `<div class="org-ce">${cause}<div class="org-ce-arrows" aria-hidden="true">&#8594;<br>&#8594;<br>&#8594;</div><div class="org-stack">${eff(1)}${eff(2)}${eff(3)}</div></div>` +
        K.box('Sum it up', { q: ['Which effect is the most important? Why?', 'Write one sentence that links the cause to an effect.'], h: 0.68, st: ['The most important effect was', 'Because', 'This led to'] });
    }
    const older = b === '912';
    const cz = older ? [['Long-term cause', 'Something that built up over time'], ['Long-term cause', 'Another condition that set the stage'], ['Immediate cause', 'The spark: what happened right before']]
      : [['Cause 1', ['What led to the event?', 'Why did it happen?']], ['Cause 2', ['What else led to the event?', 'Name another reason.']]];
    const ez = older ? [['Short-term effect', 'What happened right away?'], ['Short-term effect', 'Another immediate result'], ['Long-term effect', 'What changed for years after?']]
      : [['Effect 1', ['What happened as a result?', 'What changed?']], ['Effect 2', ['What else happened as a result?', 'Name another result.']]];
    const h = older ? 0.72 : 1.05;
    const side = (boxes, sts, at) => `<div class="org-stack">${boxes.map(([l, q], i) => K.box(lab(at + i, l), { q, h, st: sts })).join('')}</div>`;
    const ev = K.box(older ? 'Event' : 'The event', { q: ['What happened? Write it in a few words.', 'Name the event or change.'], h: older ? 1.4 : 1.2, cls: 'org-main', st: ['The event was'] });
    return `<div class="org-ce3">${side(cz, ['One cause was', 'This happened because', 'Before the event,'], 0)}<div class="org-right" aria-hidden="true">&#8594;</div>${ev}<div class="org-right" aria-hidden="true">&#8594;</div>${side(ez, ['As a result,', 'Consequently,', 'This led to'], cz.length)}</div>` +
      K.box(older ? 'Weigh the causes' : 'Explain', { q: older ? ['Which cause mattered most? Defend your answer with evidence.', 'Could the event have happened without the immediate cause? Explain.', 'Which effect lasted longest, and why?']
        : ['Which cause do you think mattered most? Why?', 'How do you know? Name a source or a detail.', 'Which effect was biggest, and why?'],
      h: older ? 0.84 : 0.9, st: ['The most important cause was', 'The evidence shows', 'Without'] });
  },

  chain(b, K, c) {
    const n0 = { k2: 3, 35: 4, 68: 5, 912: 5 }[b], typed = c.rows || [], n = Math.max(n0, typed.length);
    const labs0 = { k2: ['First this happened', 'So this happened', 'Then this happened'], 35: ['It starts here', 'That caused', 'That caused', 'In the end'],
      68: ['Starting event', 'Which led to', 'Which led to', 'Which led to', 'Final effect'], 912: ['Initial cause', 'Which led to', 'Which led to', 'Which led to', 'Outcome'] }[b];
    const labs = Array.from({ length: n }, (_, i) => typed[i] ? esc(cap(typed[i])) : i === 0 ? labs0[0] : i === n - 1 ? labs0[n0 - 1] : labs0[1]);
    // more links than the default go in a grid (the numbers give the order); k2 shrinks its boxes by the number of grid rows
    const gridCols = n > n0 ? (b === 'k2' && n > 4 ? 3 : 2) : 0, gridRows = gridCols ? Math.ceil(n / gridCols) : 0;
    const sc = b === 'k2' ? [1, 1, 1, 0.75][gridRows] || 0.75 : (gridCols ? Math.min(1, 2 * n0 / n) : 1);
    const h = { k2: 0.44, 35: 0.95, 68: 0.6, 912: 0.56 }[b] * sc;
    const qs = [['What happened first?', 'Where does the chain begin?'], ['What happened next because of that?', 'What did that cause?', 'What was the result?'], ['How did that lead to the end?', 'What did that change?']];
    const sts = b === 'k2' ? [['First,'], ['So', 'Then'], ['So', 'At last,']] : [['It began when', 'First,'], ['Because of this,', 'As a result,', 'This caused', 'This led to'], ['In the end,', 'Finally,', 'Ultimately,']];
    const out = [];
    for (let i = 0; i < n; i++) {
      const pos = i === 0 ? 0 : i === n - 1 ? 2 : 1;
      out.push(K.box(`${i + 1}. ${labs[i]}`, { q: qs[pos], h, st: sts[pos], draw: b === 'k2' ? 1.05 * sc : 0, cls: i === 0 || i === n - 1 ? 'org-main' : '' }));
      if (i < n - 1 && !gridCols) out.push(K.down(b === 'k2' ? '' : 'led to'));
    }
    if (gridCols) out.splice(0, out.length, K.grid(`repeat(${gridCols}, 1fr)`, out));
    if (b !== 'k2') out.push(K.box(b === '912' ? 'Analyze the chain' : 'Think about it', { q: b === '912' ? ['Where could the chain have been broken? What would have changed?', 'Which link was the turning point? Explain.']
      : ['What would happen if one link were missing?', 'Which link surprised you? Why?', 'Why does this chain matter?'], h: b === '35' ? 0.6 : 0.6, st: ['If', 'The turning point was', 'This matters because'] }));
    return out.join('');
  },

  main(b, K) {
    const n = { k2: 2, 35: 3, 68: 3, 912: 4 }[b];
    const top = K.box(b === '912' ? 'Central idea' : b === 'k2' ? 'What is it mostly about?' : 'Main idea', {
      q: b === 'k2' ? ['Tell the big idea in a few words.', 'What is it all about?', 'What is the most important idea?'] : ['What is the whole text or topic mostly about? Write it as one complete sentence.', 'What big point does the author want you to know?', 'Write one sentence that the details below all prove.'],
      h: b === 'k2' ? 0.88 : 0.68, cls: 'org-main', st: b === 'k2' ? ['It is about', 'This is mostly about'] : ['The main idea is that', 'This text is mostly about', 'The author shows that'] });
    const det = i => K.box(b === '912' ? `Evidence ${i}` : b === 'k2' ? `Detail ${i}` : `Detail ${i}`, {
      q: b === '912' ? ['Quote or paraphrase. Note the page or paragraph.', 'A fact, example or quotation that supports the idea.'] : b === 'k2' ? ['Draw and write one thing you learned.', 'Draw and write one fact about the big idea.', 'What is one thing the text tells you?'] : ['A fact or example that supports the main idea.', 'What does the text say that proves it?'],
      draw: b === 'k2' ? 1.6 : 0, h: { k2: 0.88, 35: 2.04, 68: 1.5, 912: 1.12 }[b], st: b === 'k2' ? ['I learned', 'It can'] : ['For example,', 'The text states', 'One detail is', 'According to the text,'],
      extra: b === '68' ? `<p class="org-src">Where I found it: ______________</p>` : b === '912' ? `<p class="org-sub">How it supports the idea:</p>${K.lines(0.56)}` : '' });
    const cols = n === 4 ? '1fr 1fr' : `repeat(${n}, 1fr)`;
    const end = K.box(b === 'k2' ? 'My sentence' : b === '912' ? 'Synthesis' : 'Summary', {
      q: b === 'k2' ? ['Tell the big idea again in your own words.', 'What did you learn? Tell it in one sentence.'] : b === '912' ? ['How do the pieces of evidence work together? What do they show beyond the central idea?', 'Write two sentences that connect the evidence to the central idea.']
        : ['Put the main idea and your details together in two sentences.', 'Write a short summary in your own words.'],
      h: b === 'k2' ? 0.88 : 0.68, st: b === 'k2' ? ['Now I know'] : ['In summary,', 'Together, these details show', 'Overall,'] });
    return top + `<div class="org-ties" aria-hidden="true">${'<span></span>'.repeat(n === 4 ? 2 : n)}</div>` + K.grid(cols, Array.from({ length: n }, (_, i) => det(i + 1))) + end;
  },

  sequence(b, K, c) {
    const typed = c.rows || [];
    if (b === 'k2') {
      const n = Math.max(4, typed.length), cols = n > 4 ? 3 : 2, sc = [1, 1, 0.75, 0.5][Math.ceil(n / cols)] || 0.5;
      const w = i => typed[i] ? cap(typed[i]) : i === 0 ? 'First' : i === n - 1 ? 'Last' : i % 2 ? 'Next' : 'Then';
      return K.grid(`repeat(${cols}, 1fr)`, Array.from({ length: n }, (_, i) => K.box(`${i + 1}. ${esc(w(i))}`, { q: ['What happens?', 'Draw and write this step.'], draw: 1.85 * sc, h: 0.88 * sc, st: [w(i) + ','] })), n === 4 ? 'org-steps4' : '');
    }
    const n0 = { 35: 5, 68: 6, 912: 6 }[b], n = Math.max(n0, typed.length), two = n > n0, sc = two ? Math.min(1, 2 * n0 / n) : 1;
    const trans = { 35: [['First,', 'To begin,'], ['Next,', 'Then,'], ['After that,', 'Next,'], ['Then,', 'Soon,'], ['Finally,', 'Last,']],
      68: [['First,', 'To begin,'], ['Next,', 'Second,'], ['Then,', 'After that,'], ['Meanwhile,', 'Following this,'], ['Later,', 'Subsequently,'], ['Finally,', 'In the end,']],
      912: [['Initially,', 'To begin,'], ['Next,', 'Following this,'], ['Subsequently,', 'Then,'], ['At the same time,', 'After this,'], ['Later,', 'Eventually,'], ['Ultimately,', 'Finally,']] }[b];
    const h = { 35: 0.68, 68: 0.6, 912: 0.56 }[b] * sc;
    const rows = [];
    for (let i = 0; i < n; i++) {
      rows.push(`<div class="org-step"><span class="org-num">${i + 1}</span>${K.box(typed[i] ? esc(cap(typed[i])) : i === 0 ? 'Step 1' : i === n - 1 ? `Step ${n}` : `Step ${i + 1}`, {
        q: i === 0 ? ['What happens first?', 'Where does it start?'] : i === n - 1 ? ['How does it end?', 'What is the last step or result?'] : ['What happens next?', 'What comes after the step above?', 'What is the next step?'],
        h, st: trans[Math.min(i, trans.length - 1)] })}</div>`);
      if (i < n - 1 && !two) rows.push(K.down());
    }
    if (two) rows.splice(0, rows.length, K.grid('1fr 1fr', rows));   // more steps than the default: two columns, numbered
    if (b === '912') rows.push(K.box('Turning point', { q: ['Star the step that changed things most. Why does the order matter here?', 'Which step could not be moved? Explain.'], h: 0.56, st: ['The key step is', 'The order matters because'] }));
    else rows.push(K.box('Check it', { q: ['Read your steps in order. Could someone follow them? What would go wrong if two steps switched?', 'Which step is the most important? Why?'], h: b === '35' ? 0.68 : 0.6, st: ['The most important step is', 'If two steps switched,'] }));
    return rows.join('');
  },

  cer(b, K) {
    const k2 = b === 'k2';
    const q = K.box(k2 ? 'My question' : 'Question', { q: k2 ? ['What do we want to find out?', 'Write the question we are testing.', 'What are we trying to learn?'] : ['What question are you answering?', 'Write the question the investigation or text asks.'], h: k2 ? 0.44 : 0.34 * (b === '35' ? 1 : 1.2), st: k2 ? ['I wonder'] : ['The question is'] });
    const claim = K.box(k2 ? 'I think' : 'Claim', { q: k2 ? ['Answer the question.', 'What do you think the answer is?'] : ['One sentence that answers the question.', 'Your answer to the question, in a complete sentence.'], h: k2 ? 0.88 : b === '35' ? 0.68 : 0.6, cls: 'org-main', st: k2 ? ['I think'] : ['I claim that', 'The answer is', 'Our data show that'] });
    const nEv = { k2: 1, 35: 2, 68: 3, 912: 3 }[b];
    const ev = Array.from({ length: nEv }, (_, i) => K.box(k2 ? 'I saw' : `Evidence ${i + 1}`, {
      q: k2 ? ['What did you see or find out?', 'Draw what happened. Then write about it.', 'What did you notice when you looked closely?'] : b === '912' ? ['Data, an observation or a quotation. Name the source.', 'A measurement or fact. Note where it came from.'] : ['A fact, a measurement or something you observed.', 'What data or observation supports your claim?'],
      draw: k2 ? 1.5 : 0, h: { k2: 0.88, 35: 1.36, 68: 1.2, 912: 0.84 }[b], st: k2 ? ['I saw', 'I noticed'] : ['The data show', 'We observed', 'In the test,', 'According to'] }));
    const reason = K.box(k2 ? 'Because' : 'Reasoning', {
      q: k2 ? ['Why does what you saw prove your idea?', 'How does what you saw help answer the question?'] : b === '35' ? ['Why does the evidence prove the claim? Use a science idea.', 'Explain how the evidence supports your claim.'] : ['Connect the evidence to the claim with a scientific principle or rule.', 'Explain WHY the evidence supports the claim. Name the science idea.'],
      h: { k2: 0.88, 35: 1.36, 68: 1.2, 912: 0.84 }[b], st: k2 ? ['This shows', 'I know because'] : ['This evidence supports my claim because', 'This happens because', 'The science idea that explains this is'] });
    const parts = [q, K.down(), claim, K.down(), K.grid(nEv === 1 ? '1fr' : `repeat(${nEv}, 1fr)`, ev), K.down(), reason];
    if (b === '912') parts.push(K.box('Rebuttal', { q: ['What is another explanation someone might give? Why is your claim stronger?', 'Name one limit of your evidence and how a new test could check it.'], h: 0.84, st: ['Someone might argue that', 'One limit of this evidence is'] }));
    return parts.join('');
  },

  kwl(b, K) {
    const cols = b === '68' || b === '912'
      ? [['K', 'What I Know', ['What do you already know or think you know?', 'Facts you are fairly sure of.']], ['W', 'What I Want to know', ['Write questions. Start with how, why or what if.', 'What do you want to find out?']],
        ['H', 'How I will find out', ['Books, sites, experts, experiments.', 'Where will you look? Name real sources.']], ['L', 'What I Learned', ['Answer your W questions. Cross out wrong K ideas.', 'New facts, with where you found them.']]]
      : [['K', b === 'k2' ? 'What I know' : 'What I Know', ['What do you already know?', 'Write facts you know now.']], ['W', b === 'k2' ? 'What I wonder' : 'What I Want to know', ['What do you want to find out?', 'Write questions.']],
        ['L', b === 'k2' ? 'What I learned' : 'What I Learned', ['What did you find out?', 'Answer your questions here.']]];
    const h = { k2: 4.4, 35: 5.8, 68: 5.0, 912: 4.6 }[b];
    const sts = { K: ['I know', 'I think'], W: ['I wonder', 'How do', 'Why does'], H: ['I will read', 'I will ask'], L: ['I learned', 'Now I know'] };
    const out = K.grid(`repeat(${cols.length}, 1fr)`, cols.map(([L, lab, q]) => K.box(`<span class="org-letter">${L}</span>${lab}`, { q, h: b === 'k2' && L === 'L' ? h - 1.6 : h, draw: b === 'k2' && L === 'L' ? 1.5 : 0, st: sts[L] })));
    return out + (b === '912' ? K.box('Still wondering', { q: ['What new questions came up? Which source was most reliable, and why?', 'What would you research next?'], h: 0.56, st: ['I still wonder', 'The most reliable source was'] }) : '');
  },

  problem(b, K) {
    if (b === 'k2') return K.box('The problem', { q: ['What is wrong? Who has the problem?', 'What needs to be fixed?'], draw: 1.5, h: 0.88, st: ['The problem is'], cls: 'org-main' }) + K.down() +
      K.box('A way to fix it', { q: ['How could we fix it?', 'What could someone do?'], draw: 1.5, h: 0.88, st: ['We could', 'One way is'] }) + K.down() +
      K.box('What happened', { q: ['Did it work? What happened next?', 'How did it turn out?'], h: 0.88, st: ['In the end,', 'It worked because'] });
    const prob = K.box('Problem', { q: ['What is the problem? Who does it affect?', 'Describe the problem in one or two sentences.'], h: b === '35' ? 0.68 : 0.6, cls: 'org-main', st: ['The problem is that', 'A problem for'] });
    const why = K.box(b === '912' ? 'Causes and stakes' : 'Why it matters', { q: b === '912' ? ['What causes the problem? What happens if nothing changes?', 'Root cause, and who is affected most.'] : ['Why is this a problem? What happens if nobody fixes it?', 'Who is affected, and how?'],
      h: b === '35' ? 0.68 : 0.6, st: ['This matters because', 'If nothing changes,'] });
    let sols;
    if (b === '35') sols = K.grid('1fr 1fr', [1, 2].map(i => K.box(`Solution ${i}`, { q: ['One way to solve it.', 'An idea that could fix it.'], h: 1.02, st: ['One way is to', 'We could'],
      extra: `<p class="org-sub">Good point / bad point:</p>${K.lines(0.68)}` })));
    else {
      const head = b === '912' ? ['Possible solution', 'Pros', 'Cons', 'Evidence it could work'] : ['Possible solution', 'Pros (good points)', 'Cons (problems)'];
      const rh = b === '912' ? 0.84 : 0.9;
      sols = `<table class="org-table"><thead><tr>${head.map(x => `<th>${x}</th>`).join('')}</tr></thead><tbody>${[1, 2, 3].map(i => `<tr>${head.map((_, j) => `<td style="height:${(rh * K.g).toFixed(2)}in">${j === 0 ? `<b class="org-cell-n">${i}</b>` : ''}${K.lines(rh - 0.1)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
    }
    const best = K.box('Best solution', { q: b === '912' ? ['Which solution is strongest? Defend it, and admit its biggest cost.', 'Choose one and justify it against the others.'] : ['Which solution is best? Why?', 'Pick one and give two reasons.'], h: b === '35' ? 1.02 : 0.84, cls: 'org-main', st: ['The best solution is', 'I choose', 'Although it has a cost,'] });
    const check = K.box(b === '35' ? 'What happened' : 'How we will know it worked', { q: b === '35' ? ['How did it turn out? (For a story, what happened at the end?)', 'Did the solution work? What happened?'] : ['What would you measure or watch to know the solution worked?', 'Name one sign of success you could check.'], h: b === '35' ? 0.68 : 0.6, st: ['We will know it worked when', 'In the end,'] });
    return prob + K.grid('1fr', [why]) + sols + best + check;
  },

  web(b, K, c) {
    const n = { k2: 4, 35: 6, 68: 6, 912: 8 }[b];
    const W = 720, H = { k2: 590, 35: 610, 68: 610, 912: 610 }[b], cx = W / 2, cy = H / 2;
    const bw = n === 8 ? 222 : n === 6 ? 226 : 300, bh = n === 8 ? 190 : n === 6 ? 196 : 250;
    const xs = n === 4 ? [[10, 10], [W - 10 - bw, 10], [10, H - 10 - bh], [W - 10 - bw, H - 10 - bh]]
      : n === 6 ? [[0, 0], [(W - bw) / 2, 0], [W - bw, 0], [0, H - bh], [(W - bw) / 2, H - bh], [W - bw, H - bh]]
        : [[0, 0], [(W - bw) / 2, 0], [W - bw, 0], [0, (H - bh) / 2], [W - bw, (H - bh) / 2], [0, H - bh], [(W - bw) / 2, H - bh], [W - bw, H - bh]];
    const lh = K.lh * 96;
    let body = '';
    const ew = n === 8 ? 128 : 140, eh = n === 8 ? 62 : 70;
    for (const [x, y] of xs) body += `<line x1="${cx}" y1="${cy}" x2="${x + bw / 2}" y2="${y + bh / 2}" stroke="#222" stroke-width="2"/>`;
    xs.forEach(([x, y]) => {
      body += `<rect x="${x + 1}" y="${y + 1}" width="${bw - 2}" height="${bh - 2}" rx="14" fill="#fff" stroke="#222" stroke-width="2"/>`;
      body += `<line x1="${x + 14}" y1="${y + 38}" x2="${x + bw - 14}" y2="${y + 38}" stroke="#222" stroke-width="1.6"/>`;
      body += `<text x="${x + 14}" y="${y + 52}" font-size="11" fill="#666">${b === 'k2' ? 'idea' : 'subtopic'}</text>`;
      for (let ly = y + 58 + lh; ly < y + bh - 8; ly += lh) body += `<line x1="${x + 14}" y1="${ly}" x2="${x + bw - 14}" y2="${ly}" stroke="#999" stroke-width="1"/>`;
    });
    const t = String(c.topic || '').trim();
    body += `<ellipse cx="${cx}" cy="${cy}" rx="${ew}" ry="${eh}" fill="#fff" stroke="#222" stroke-width="3"/>`;
    if (t) {
      const words = t.split(/\s+/); let l1 = t, l2 = '';
      if (t.length > 16 && words.length > 1) { const mid = Math.ceil(words.length / 2); l1 = words.slice(0, mid).join(' '); l2 = words.slice(mid).join(' '); }
      const size = Math.min(22, (ew * 1.7) / (Math.max(l1.length, l2.length) * 0.56));
      body += l2 ? `<text x="${cx}" y="${cy - 4}" text-anchor="middle" font-size="${size.toFixed(1)}" font-weight="700">${esc(l1)}</text><text x="${cx}" y="${cy + size}" text-anchor="middle" font-size="${size.toFixed(1)}" font-weight="700">${esc(l2)}</text>`
        : `<text x="${cx}" y="${cy + size / 3}" text-anchor="middle" font-size="${size.toFixed(1)}" font-weight="700">${esc(t)}</text>`;
    } else body += `<line x1="${cx - ew + 26}" y1="${cy + 10}" x2="${cx + ew - 26}" y2="${cy + 10}" stroke="#222" stroke-width="1.5"/><text x="${cx}" y="${cy + 28}" text-anchor="middle" font-size="11" fill="#666">topic</text>`;
    const pic = Gen.h.svg(W, H, body, `Concept web: a center topic${t ? ' (' + t + ')' : ''} joined to ${n} boxes for subtopics and details`);
    return pic + K.box(b === 'k2' ? 'My sentence' : 'Connect two ideas', { q: b === 'k2' ? ['Tell about your topic using two ideas.', 'Write one thing you know about your topic.', 'Which idea is your favorite? Tell why.']
      : ['Pick two subtopics and explain how they are connected.', 'Which subtopic is most important to understanding the topic? Why?', 'Draw a line between two boxes that are linked, then explain the link here.'],
      h: b === 'k2' ? 0.88 : 0.6, st: b === 'k2' ? ['My topic', 'I know that'] : ['These two ideas connect because', 'The most important part is', 'Both'] });
  },

  story(b, K) {
    if (b === 'k2') return K.box('Title', { h: 0.44 }) + K.grid('1fr 1fr', [
      K.box('Who is in the story?', { q: ['The characters', 'The characters: people or animals in the story'], draw: 1.35, h: 0.44, st: ['The story is about'] }),
      K.box('Where does it happen?', { q: ['The setting', 'The setting: the place and time'], draw: 1.35, h: 0.44, st: ['It happens'] }),
      K.box('What is the problem?', { q: ['What goes wrong?', 'What do the characters need?'], draw: 1.35, h: 0.44, st: ['The problem is'] }),
      K.box('How does it end?', { q: ['How is the problem solved?', 'What happens at the end?'], draw: 1.35, h: 0.44, st: ['At the end,'] })]);
    if (b === '35') return K.grid('3fr 2fr', [K.box('Title', { h: 0.34 }), K.box('Author', { h: 0.34 })]) +
      K.grid('1fr 1fr', [K.box('Characters', { q: ['Who is in the story? Tell one trait for each.', 'Main character and others. What are they like?'], h: 1.02, st: ['The main character is'] }),
        K.box('Setting', { q: ['Where and when does it happen?', 'Time and place. How does it look or feel?'], h: 1.02, st: ['The story takes place'] })]) +
      K.box('Problem', { q: ['What problem does the main character face?', 'What does the main character want, and what is in the way?'], h: 0.68, cls: 'org-main', st: ['The problem is that', 'The main character wants'] }) +
      K.grid('1fr 1fr 1fr', ['Beginning', 'Middle', 'End'].map((w, i) => K.box(w, { q: [['What happens first?', 'How does it start?'], ['What are the big events?', 'What happens as they try to solve the problem?'], ['How does it wrap up?', 'What happens last?']][i], h: 1.36, st: [['At first,', 'In the beginning,'], ['Then', 'Next,'], ['Finally,', 'At the end,']][i] }))) +
      K.box('Solution and lesson', { q: ['How is the problem solved? What lesson can we learn?', 'How does it end, and what does the character learn?'], h: 0.68, st: ['The problem is solved when', 'The lesson is'] });
    const older = b === '912';
    return K.grid('3fr 2fr', [K.box('Title', { h: 0.3 }), K.box('Author', { h: 0.3 })]) +
      K.grid('1fr 1fr', [K.box(older ? 'Characters and motivation' : 'Characters', { q: older ? ['Protagonist, antagonist and what each one wants.', 'Who drives the story, and why do they act as they do?'] : ['Main and supporting characters, with a trait and evidence for each.', 'Who is the protagonist? Who or what opposes them?'], h: 0.9, st: ['The protagonist,'] }),
        K.box(older ? 'Setting and mood' : 'Setting', { q: older ? ['Time, place and the mood the setting creates.', 'How does the setting shape what happens?'] : ['Time and place. How does it affect the characters?', 'Where and when? Why does it matter?'], h: 0.9, st: ['The story is set in'] })]) +
      K.box(older ? 'Central conflict' : 'Conflict', { q: ['What is the main conflict? Is it character vs. character, self, society or nature?', 'Name the conflict and its type.'], h: 0.6, cls: 'org-main', st: ['The main conflict is', 'struggles against'] }) +
      K.grid('1fr 1fr 1fr', [K.box('Rising action', { q: ['Key events that build tension.', 'What complications pile up?'], h: older ? 1.12 : 1.2, st: ['First,', 'The tension builds when'] }),
        K.box('Climax', { q: ['The turning point. What is decided or revealed?', 'The moment of highest tension.'], h: older ? 1.12 : 1.2, st: ['The turning point comes when'] }),
        K.box('Resolution', { q: ['How is the conflict resolved, or left open?', 'What happens after the climax?'], h: older ? 1.12 : 1.2, st: ['In the end,'] })]) +
      K.box(older ? 'Theme and evidence' : 'Theme', { q: older ? ['State the theme as a complete sentence (not one word), then cite a line that shows it.', 'What does the story say about people or life? Support it with a detail.'] : ['What message does the author share? Write it as a sentence.', 'What lesson about life does the story teach?'], h: 0.6, st: ['The author suggests that', 'One theme is that'] }) +
      (older ? K.box('Point of view and craft', { q: ['Who narrates, and how does that shape what we know?', 'Name one choice the author made (structure, symbol, word choice) and its effect.'], h: 0.56, st: ['Because the narrator', 'The author uses'] }) : '');
  },

  frayer(b, K, c) {
    const t = String(c.topic || '').trim();
    const q = b === 'k2'
      ? [['What it means', ['Tell what the word means in your own words.', 'What does it mean?'], ['It means']], ['Draw it', 'Draw a picture of the word.', null],
        ['Example', ['Write or draw something that IS this.', 'Name one example.'], ['One example is']], ['Not an example', ['Write or draw something that is NOT this.', 'Name something that does not fit.'], ['This is not']]]
      : [['Definition', ['In your own words, not copied.', 'What does the word mean?'], ['It means', 'is a']], ['Characteristics', ['Traits that are always true of it.', 'What makes it what it is?'], ['It always', 'It has']],
        ['Examples', ['Two or three that fit.', 'Things that are this.'], ['Examples are']], ['Non-examples', ['Close, but they do not fit. Why?', 'Things that are NOT this.'], ['This is not']]];
    const h = { k2: 2.2, 35: 2.4, 68: 2.04, 912: 1.68 }[b];
    const cells = q.map(([lab, qq, st]) => st ? K.box(lab, { q: qq, h, st }) : K.box(lab, { q: qq, draw: h + 0.3 }));
    const word = `<div class="org-word">${t ? `<b>${esc(t)}</b>` : '<span>word</span>'}</div>`;
    const extra = b === '68' ? K.box('Use it in a sentence', { q: ['Write a sentence that shows you know what it means.', 'Use the word in a sentence about your own life or this unit.'], h: 0.6, st: ['I'] })
      : b === '912' ? K.grid('1fr 1fr', [K.box('Word parts or origin', { q: ['Roots, prefixes or suffixes, and what they mean.', 'Where does the word come from?'], h: 0.56 }),
        K.box('Related words', { q: ['Other forms of the word, and words that go with it.', 'Synonyms, antonyms or other forms.'], h: 0.56 })]) + K.box('Use it in a sentence', { q: 'Write a sentence that shows the meaning, not just the word.', h: 0.56 })
        : b === '35' ? K.box('Use it in a sentence', { q: 'Write a sentence that shows you know what it means.', h: 0.68, st: ['I'] }) : '';
    return `<div class="org-frayer">${K.grid("1fr 1fr", cells.slice(0, 2))}${word}${K.grid("1fr 1fr", cells.slice(2))}</div>` + extra;
  },
};


const TIPS = {
  venn: { y: ['Start with the middle: what do both have?', 'Write short words, not long sentences, in the circles.', 'Read each fact and ask: is this true for one, or for both?', 'Try to put at least three things in each part.'],
    o: ['Fill the overlap first; it is often the hardest part.', 'Use short phrases in the circles; save full sentences for the bottom.', 'Test each fact: is it true of one, or of both? Only facts true of both go in the middle.', 'Aim for balance: about the same number of facts in each part.'] },
  venn3: { y: ['Start in the very middle: what do all three have?', 'Write short words, not long sentences.', 'Read each fact and ask: which ones is this true for?', 'It is OK if a part stays empty.'],
    o: ['Work from the center out: all three, then pairs, then each alone.', 'Test each fact against all three before you place it.', 'Use short phrases; an empty region is a real answer.', 'Check the pair overlaps: they are the easiest to miss.'] },
  compare: { y: ['Ask the same question about both things in each row.', 'Fill one whole row before you start the next.', 'Use short words in the boxes.', 'Look back at your book or notes for each row.'],
    o: ['Each row asks one question of both items; answer it for each.', 'Use phrases, not sentences, in the cells.', 'Choose rows that show real differences, not trivia.', 'Note a source in a cell if a fact came from your reading.'] },
  cause: { y: ['Ask "Why did it happen?" to find the cause.', 'Ask "What happened because of it?" to find an effect.', 'Clue words: because, so, since, as a result.', 'Check each arrow: does the first box really make the next one happen?'],
    o: ['Signal words: because, due to, led to, as a result, consequently.', 'Test each arrow: would the effect still happen without the cause?', 'Happening first does not prove a cause. Look for how one led to the other.', 'Note where each fact came from so you can cite it.'] },
  chain: { y: ['Each box should make the next box happen.', 'Read your chain aloud with "so" between the boxes.', 'Start with what happened first.', 'Use short sentences.'],
    o: ['Read the chain aloud with "which led to" between boxes; every link should make sense.', 'If a link feels like a jump, you may be missing a step.', 'Use dates or times if you have them.', 'Each box holds one event, not two.'] },
  main: { y: ['Details answer "How do I know?" about the main idea.', 'Look at the title and headings for clues to the main idea.', 'The main idea is a whole sentence, not one word.', 'Put each detail in its own box.'],
    o: ['A main idea makes a point; a topic is just a subject.', 'Every detail should answer "How do I know?" for the main idea.', 'Paraphrase details; quote only what is worth quoting exactly.', 'If your details do not fit, revise the main idea.'] },
  sequence: { y: ['Picture it happening, then write each step.', 'Put one step in each box.', 'Use order words: first, next, then, last.', 'Read your steps aloud to check the order.'],
    o: ['One action or event per box.', 'Vary your transitions so the order is clear.', 'Include steps that seem obvious; a reader may need them.', 'Use dates, times or amounts where they help.'] },
  cer: { y: ['Your claim answers the question.', 'Evidence is what you saw, counted or measured.', 'Reasoning tells why the evidence proves the claim.', 'Use numbers if you have them.'],
    o: ['A claim answers the question in one sentence that someone could disagree with.', 'Strong evidence is specific: numbers, units, sources.', 'Reasoning names the science idea, not just "the data prove it."', 'Ask yourself: would a skeptic accept this evidence?'] },
  kwl: { y: ['It is OK if something in K turns out to be wrong.', 'Good W questions start with how, why or what.', 'Come back to this sheet when you learn something new.', 'Draw if a word is hard to write.'],
    o: ['Write W questions that need more than a yes or no.', 'Revisit K at the end and fix any ideas that turned out wrong.', 'In L, note where each fact came from.', 'A good H column names specific sources.'] },
  problem: { y: ['A problem is something that needs fixing.', 'Think of more than one way to fix it.', 'Ask: what would make it better for everyone?', 'Draw if it helps you think.'],
    o: ['Describe the problem without blaming; stick to facts.', 'Brainstorm first, judge later: list solutions, then weigh them.', 'Every solution has a cost; name it honestly.', 'Choose a sign of success you could actually measure.'] },
  web: { y: ['Put one idea in each box.', 'Ask: what are the parts of my topic?', 'Add details that tell more about each idea.', 'Draw small pictures if it helps.'],
    o: ['Subtopics should be broad enough to hold several details.', 'Use phrases, not full sentences, inside the boxes.', 'Each box could become one paragraph.', 'Leave a box empty until you find a subtopic that fits.'] },
  story: { y: ['Think: who, where, what went wrong and how it ended.', 'Look back at the pictures and pages for help.', 'Use names from the story.', 'Tell only the big events.'],
    o: ['Choose only the events that move the plot forward.', 'Use character names and page numbers.', 'The climax is a turning point, not just the most exciting part.', 'A theme is a full sentence about life, not one word.'] },
  frayer: { y: ['Use your own words, like you are explaining to a friend.', 'A good non-example is something close, but different.', 'Draw if it helps.', 'Check a glossary if you are stuck.'],
    o: ['Write the definition in your own words; do not copy.', 'Characteristics are always true; examples are specific cases.', 'The strongest non-examples are close calls.', 'Check the word in more than one source.'] },
  tchart: { y: ['Read each card and ask: which side does it fit?', 'Put one thing on each line.', 'If you are not sure, set the card aside and come back to it.', 'Check: does everything on one side have the same thing in common?'],
    o: ['Decide the rule for each column before you sort.', 'Use short phrases, one per line.', 'An item that fits neither side is worth a note at the bottom.', 'Count your items: both columns should be full.'] },
};
TIPS.venn2 = TIPS.venn;

/* ---------- directions, aims and teacher notes per layout ---------- */
const DIR = {
  venn2: { k2: 'Write or draw in the circles. Put things that are the same in the middle.', d: 'Write each name on its line. Put what is true of only one in its own circle and what is true of both in the middle. Then answer below.' },
  venn3: { k2: 'Write or draw in the circles. Things that fit all three go in the very middle.', d: 'Write each name on its line. Put each fact in the part of the diagram where it fits: one circle, an overlap of two, or the middle for all three. Some parts may stay empty.' },
  compare: { k2: 'Write the two things at the top. In each row, tell how each one is.', d: 'Write what you are comparing at the top of each column. Fill one row for each point of comparison, then sum it up below.' },
  cause: { k2: 'For each pair, draw and write why it happened and what happened.', d: 'Fill in the causes on the left and the effects on the right. Follow the arrows. Then answer the question at the bottom.' },
  chain: { k2: 'Draw and write what happened, in order. Each box makes the next one happen.', d: 'Start at the top. Each box should cause the box below it. Then answer the question at the bottom.' },
  main: { k2: 'Write the big idea at the top. Draw and write two details that tell about it.', d: 'Write the main idea in the top box. Write one supporting detail in each box below, then sum it up at the bottom.' },
  sequence: { k2: 'Draw and write the steps in order: first, next, then, last.', d: 'Write the steps in order, one step in each box. Start each one with a time-order word. Then check your order at the bottom.' },
  cer: { k2: 'Answer the question. Tell what you saw, then tell why it proves your idea.', d: 'Write the question, then your claim. Add evidence in each box. In the reasoning box, explain why the evidence proves the claim.' },
  kwl: { k2: 'Before you learn, fill in K and W. After you learn, fill in L.', d: 'Fill in K and W before you start. Fill in the rest as you learn and after.' },
  problem: { k2: 'Draw and write the problem, a way to fix it, and what happened.', d: 'Describe the problem and why it matters. List possible solutions, then choose the best one and explain how you will know it worked.' },
  web: { k2: 'Write your topic in the middle. Write or draw one idea in each box.', d: 'Write the topic in the center. Name a subtopic on the top line of each box, then add details on the lines below it.' },
  story: { k2: 'Draw and write about the story in each box.', d: 'Fill in each box as you read or after you finish. Use details from the story.' },
  frayer: { k2: 'Write the word in the middle. Fill in each box.', d: 'Write the word in the oval. Fill in all four boxes, then use the word in a sentence.' },
  tchart: { k2: 'Write or draw each thing on the side where it belongs.', d: 'Write the two headings. Sort each item into the column where it belongs, then answer below.' },
};
const ICAN = {
  venn2: { k2: 'I can tell how two things are the same and different.', d: 'I can compare and contrast two things using details.' },
  venn3: { k2: 'I can sort what three things share and what makes each one different.', d: 'I can compare and contrast three things and find what they all share.' },
  compare: { k2: 'I can tell how two things are the same and different.', d: 'I can compare two things point by point and explain which differences matter.' },
  cause: { k2: 'I can tell why something happened.', d: 'I can explain causes and effects and how they connect.' },
  chain: { k2: 'I can tell how one thing makes the next thing happen.', d: 'I can trace a chain of causes and effects from start to finish.' },
  main: { k2: 'I can tell what a text is mostly about and give details.', d: 'I can find the main idea and the details that support it.' },
  sequence: { k2: 'I can tell the steps in order.', d: 'I can put events or steps in order and explain why the order matters.' },
  cer: { k2: 'I can answer a question and tell what I saw that proves it.', d: 'I can back a claim with evidence and explain my reasoning.' },
  kwl: { k2: 'I can tell what I know, what I wonder and what I learned.', d: 'I can track what I know, what I want to learn and what I found out.' },
  problem: { k2: 'I can tell a problem and a way to fix it.', d: 'I can describe a problem, weigh solutions and choose the best one.' },
  web: { k2: 'I can tell ideas that go with my topic.', d: 'I can organize a topic into subtopics and details.' },
  story: { k2: 'I can tell who, where, the problem and the ending of a story.', d: 'I can map the parts of a story and explain how they connect.' },
  frayer: { k2: 'I can show what a word means.', d: 'I can define a word and show what it is and is not.' },
  tchart: { k2: 'I can sort things into two groups.', d: 'I can sort ideas into two groups and explain my rule.' },
};
const pickB = (o, b) => o[b] || o.d;
const ROWED = ['compare', 'cause', 'sequence', 'chain'];   // layouts whose rows or boxes take typed labels
const MISTAKES = {
  venn2: 'Putting a shared trait in one circle only, and writing opposites in the middle ("one is big, one is small" belongs in the two outer parts, not the overlap).',
  venn3: 'Leaving the pairwise overlaps empty when a trait fits two, or forcing something into every region. Some regions can honestly stay blank.',
  compare: 'Rows that compare different things (size for one, color for the other). Each row should ask the same question of both.',
  cause: 'Mixing up cause and effect, and listing things that only happened at the same time ("after" is not always "because").',
  chain: 'Boxes that are just a list of events. Each link should answer "why did the next thing happen?"',
  main: 'A main idea that is only a topic ("frogs") instead of a full sentence that makes a point, and details that are interesting but do not support it.',
  sequence: 'Skipping a step the reader needs, and using the same time-order word every time.',
  cer: 'Evidence that just repeats the claim, and reasoning that says "this proves it" without naming the science idea that connects them.',
  kwl: 'W questions that can be answered yes or no. Push for how and why. In L, students often forget to check their K column for ideas that turned out wrong.',
  problem: 'Jumping to one solution without weighing others, and a "best" choice with no reason tied to the problem.',
  web: 'Details that belong under a different subtopic, and subtopics that are really details (too narrow to hold more).',
  story: 'Retelling every event instead of choosing the key ones, and a theme written as one word ("friendship") instead of a sentence.',
  frayer: 'A definition copied word for word, and non-examples that are random. The best non-examples are close calls.',
  tchart: 'Sorting by a guess instead of a rule, and columns that are really the same group in different words. Ask students to say the rule out loud.',
};
const USE = {
  venn2: 'Model one fact in each part with the class first. Students can work in pairs, then write the sum-up on their own. A Venn suits two things that share a lot; for point-by-point comparison use the compare chart.',
  venn3: 'Fill the middle first (what all three share), then the pairs, then each one alone. Tell students an empty region is an answer, not a mistake.',
  compare: 'Choose the rows together the first time; later, let students choose their own. The last column is where the thinking shows.',
  cause: 'Read or watch the source first, then fill in the event or cause before the effects. Ask "how do you know?" for each arrow.',
  chain: 'Good for history, science processes and stories. Students can cut the boxes apart and reorder them as a check.',
  main: 'Works for a paragraph, a chapter, a video or a unit. Have students find the details first if the main idea is hard, then ask what they all have in common.',
  sequence: 'Use it for a process, a story, a procedure or a historical sequence. The bottom question makes students reread their steps.',
  cer: 'Use after a lab, a demo or a data set. The question can come from you or from the student. Reasoning is the hardest part: model it aloud.',
  kwl: 'Fill K and W at the start of a unit or text; return to the rest during and after. Keep it in a folder so students can add to it.',
  problem: 'Fits a story (how a character solves a problem) or a real-world problem at school or in the community. For older students the table pushes them to weigh trade-offs.',
  web: 'Use it to brainstorm before writing, or to review a unit. Each box can become one paragraph of a report.',
  story: 'Use during or after reading a story, novel, film or play. Partners can compare maps and argue about the climax or theme.',
  frayer: 'One word per sheet. Put finished Frayer models on the wall as a word bank, or have partners trade and quiz each other.',
  tchart: 'Type the two headings and, if you like, a comma-separated list of items to sort: they print as a cut-out strip at the bottom. Without a list, students write their own items on the lines.',
};

/* ---------- filled-in models for the teacher page (sample topics; facts checked) ---------- */
const MODELS = {
  venn2: { y: { topic: 'Frogs and toads', rows: [['Only frogs', 'Most have smooth, moist skin. Long back legs for leaping. Usually live in or near water.'],
    ['Both', 'Amphibians. Most lay eggs in water and start life as tadpoles. Eat insects.'], ['Only toads', 'Most have dry, bumpy skin. Shorter legs for hopping and walking. Can live farther from water.'],
    ['Sum it up', 'Frogs and toads are both amphibians that start as tadpoles, but most frogs have smooth skin and long legs, while toads have bumpy skin and short legs.']] },
  o: { topic: 'Plant cells and animal cells', rows: [['Only plant cells', 'Cell wall made of cellulose. Chloroplasts for photosynthesis. One large central vacuole.'],
    ['Both', 'Nucleus, cell membrane, cytoplasm, mitochondria, ribosomes.'], ['Only animal cells', 'No cell wall. No chloroplasts. Small vacuoles, if any. Centrioles.'],
    ['Sum it up', 'Plant and animal cells share the same basic machinery, but only plant cells have a cell wall and chloroplasts, which let a plant keep its shape and make its own food.']] } },
  venn3: { y: { topic: 'Fish, birds and mammals', rows: [['All three', 'Have a backbone. Need oxygen to live.'], ['Fish and birds', 'Most lay eggs.'], ['Birds and mammals', 'Warm-blooded: keep a steady body temperature.'],
    ['Fish and mammals', 'Left empty: nothing we found fits only these two. That is OK.'], ['Only fish', 'Gills for breathing in water. Most have scales.'], ['Only birds', 'Feathers and a beak.'], ['Only mammals', 'Hair or fur. Babies drink milk.']] },
  o: { topic: 'The three branches of the U.S. government', rows: [['All three', 'Set up by the Constitution. Each can check the power of the others.'],
    ['Legislative and executive', 'Members are elected (the President through the Electoral College).'], ['Executive and judicial', 'Left empty: this sample found nothing that fits only these two.'],
    ['Legislative and judicial', 'Left empty.'], ['Only legislative (Congress)', 'Makes laws. Two houses. Can override a veto with a two-thirds vote of both houses.'],
    ['Only executive (President)', 'Carries out laws. Can veto bills. Commander in chief.'], ['Only judicial (courts)', 'Decides what laws mean. Can rule a law unconstitutional. Federal judges serve during good behavior, usually for life.']] } },
  compare: { y: { topic: 'Summer and winter (in most of the United States)', rows: [['Weather', 'Summer: hot. Winter: cold. Different.'], ['Daylight', 'Summer: long days. Winter: short days. Different.'],
    ['Clothes', 'Summer: shorts and sandals. Winter: coats and boots. Different.'], ['Length', 'Both seasons last about three months. Same.'],
    ['Sum it up', 'Summer and winter both last about three months, but they are different in almost every other way, especially temperature and daylight.']] },
  o: { topic: 'Mitosis and meiosis', rows: [['Purpose', 'Mitosis: growth and repair. Meiosis: makes sex cells (gametes).'], ['Number of divisions', 'Mitosis: one. Meiosis: two.'],
    ['Cells made', 'Mitosis: two. Meiosis: four.'], ['Chromosome number', 'Mitosis: same as the parent cell. Meiosis: half.'], ['Genetic match', 'Mitosis: identical to the parent. Meiosis: each cell is different.'],
    ['Sum it up', 'Both divide a cell, but meiosis halves the chromosome number and shuffles genes, which, along with fertilization, is why offspring are not copies of either parent.']] } },
  cause: { y: { topic: 'A night of heavy rain', rows: [['Cause', 'It rained hard all night.'], ['Effect 1', 'Big puddles covered the playground.'], ['Effect 2', 'Recess was held inside.'],
    ['Effect 3', 'The school garden got a good soaking.'], ['Sum it up', 'The most important effect was indoor recess, because it changed everyone\'s day.']] },
  o: { topic: 'The Dust Bowl (1930s, southern Great Plains)', rows: [['Long-term cause', 'Farmers plowed up native prairie grasses whose roots had held the soil in place.'],
    ['Long-term cause', 'Severe drought through much of the 1930s dried out the soil.'], ['Immediate cause', 'Strong winds lifted the loose, dry topsoil into huge dust storms.'],
    ['Short-term effects', 'Crops failed and many families lost their farms. Dust caused breathing illness.'], ['Long-term effect', 'Many families moved west, often to California. The federal government created the Soil Conservation Service (1935) to teach soil-saving farming, such as contour plowing and crop rotation.'],
    ['Weigh the causes', 'Plowing the grass mattered most: drought had struck the Plains before, but without grass roots the soil had nothing to hold it.']] } },
  chain: { y: { topic: 'How a puddle becomes rain', rows: [['1', 'The sun warms a puddle.'], ['2', 'The water evaporates and becomes water vapor, a gas.'], ['3', 'High in the sky the vapor cools and condenses into tiny drops that make a cloud.'],
    ['4', 'The drops join and get heavy, then fall as rain.']] },
  o: { topic: 'How World War I spread in 1914', rows: [['1', 'June 1914: Archduke Franz Ferdinand of Austria-Hungary is assassinated in Sarajevo.'], ['2', 'July 1914: Austria-Hungary declares war on Serbia.'],
    ['3', 'Russia mobilizes its army to support Serbia.'], ['4', 'Germany, Austria-Hungary\'s ally, declares war on Russia and then on France.'], ['5', 'Germany invades Belgium; Britain declares war on Germany (August 4, 1914).'],
    ['Analyze', 'Alliances were the turning point: they turned a regional conflict into a war among the great powers.']] } },
  main: { y: { topic: 'Bees', rows: [['Main idea', 'Bees are important helpers for plants and people.'], ['Detail 1', 'Bees carry pollen from flower to flower, which helps plants make seeds and fruit.'],
    ['Detail 2', 'Honeybees make honey from the nectar they collect.'], ['Detail 3', 'Many fruits and vegetables we eat come from plants that bees pollinate.'],
    ['Summary', 'Bees help plants grow fruit and seeds, and they give us honey, so they matter to the food we eat.']] },
  o: { topic: 'Threats to coral reefs', rows: [['Central idea', 'Coral reefs are under pressure from several human-caused threats at once.'], ['Evidence 1', 'When ocean water stays too warm, corals expel the algae that live in them and turn white (bleaching); long bleaching can kill them.'],
    ['Evidence 2', 'Runoff from farms and cities carries mud and nutrients that cloud the water and feed algae that compete with coral.'], ['Evidence 3', 'Ocean acidification, caused by the sea absorbing carbon dioxide, makes it harder for corals to build their skeletons.'],
    ['Evidence 4', 'Overfishing removes fish that keep algae in check.'], ['Synthesis', 'Because the threats stack, a reef weakened by one is less able to recover from the next.']] } },
  sequence: { y: { topic: 'Planting a seed', rows: [['First', 'Fill a cup with soil and poke a hole with your finger.'], ['Next', 'Drop the seed in the hole and cover it with soil.'], ['Then', 'Water the soil until it is damp, not soaked.'],
    ['Last', 'Set the cup in a sunny spot and check it every day.']] },
  o: { topic: 'How a bill becomes a federal law', rows: [['1', 'A member of Congress introduces the bill.'], ['2', 'A committee studies it, holds hearings and may change it.'], ['3', 'The full House or Senate debates and votes.'],
    ['4', 'The other chamber passes the same version (differences are worked out first).'], ['5', 'The bill goes to the President.'], ['6', 'The President signs it into law or vetoes it; Congress can override a veto with a two-thirds vote in both houses. (If the President does neither within 10 days, Sundays excepted, the bill becomes law anyway, unless Congress has adjourned.)'],
    ['Turning point', 'Committee review: most bills never leave committee.']] } },
  cer: { y: { topic: 'Do plants need light? (sample data)', rows: [['Question', 'Do plants need light to stay healthy?'], ['Claim', 'Plants need light to stay healthy and green.'],
    ['Evidence', 'After two weeks, the bean plant by the window had green leaves and a strong stem. The one in the closet was pale yellow and thin, and it drooped.'],
    ['Reasoning', 'Plants use light to make their own food. In the dark, the plant could not make food, so it grew weak.']] },
  o: { topic: 'Does mass change a pendulum\'s period? (sample data)', rows: [['Question', 'Does the mass of a pendulum bob change how long one swing takes?'], ['Claim', 'Mass does not noticeably change the period; length does.'],
    ['Evidence', 'With a 50 cm string, bobs of 50 g, 100 g and 200 g each took about 1.4 s per back-and-forth swing (average of 10 swings). Shortening the string to 25 cm cut the period to about 1.0 s.'],
    ['Reasoning', 'A heavier bob feels a bigger pull of gravity but also has more inertia, so its acceleration is the same, just as all objects fall at the same rate without air resistance. The period depends on length and gravity, not mass.'],
    ['Rebuttal', 'Someone might say heavier bobs swing faster, but our three masses differed by less than 0.05 s, which is within our stopwatch error.']] } },
  kwl: { y: { topic: 'Butterflies', rows: [['K', 'Butterflies have wings. They come from caterpillars.'], ['W', 'What do butterflies eat? How does a caterpillar change?'],
    ['L', 'Adult butterflies sip nectar from flowers through a long tube-like mouthpart. A caterpillar forms a chrysalis and changes into a butterfly inside it.']] },
  o: { topic: 'Volcanoes', rows: [['K', 'Volcanoes erupt lava. There are volcanoes in Hawaii.'], ['W', 'Why do volcanoes form where they do?'], ['H', 'Textbook chapter on plate tectonics; the U.S. Geological Survey volcano pages.'],
    ['L', 'Most volcanoes form near plate boundaries, where plates pull apart or one plate sinks under another. Hawaii is different: its volcanoes sit over a hot spot in the middle of the Pacific Plate.']] } },
  problem: { y: { topic: 'Our class keeps losing pencils', rows: [['Problem', 'Pencils go missing, so we waste time looking for one.'], ['Solution 1', 'A pencil cup on every table. Good: easy. Bad: cups can tip over.'],
    ['Solution 2', 'A sign-out chart. Good: we know who has one. Bad: takes time.'], ['Best solution', 'The pencil cup, because it is quick and everyone can reach it.'], ['What happened', 'After two weeks, we lost far fewer pencils.']] },
  o: { topic: 'Litter in the school courtyard after lunch', rows: [['Problem', 'Wrappers and cups are left in the courtyard every day.'], ['Why it matters', 'It attracts pests, blows into the street and takes custodians time.'],
    ['Solution 1', 'More trash and recycling bins. Pro: easy to use. Con: costs money.'], ['Solution 2', 'A rotating student clean-up crew. Pro: free, builds ownership. Con: some may not show up.'],
    ['Solution 3', 'Lose courtyard lunch for a day after a messy day. Pro: fast results. Con: punishes everyone.'],
    ['Best solution', 'Bins plus the crew: bins make the right thing easy, and the crew keeps it going.'], ['How we will know', 'Count pieces of litter at 1:00 p.m. for a week before and two weeks after.']] } },
  web: { y: { topic: 'What animals need', rows: [['Food', 'Plants, seeds or other animals.'], ['Water', 'From ponds, rain or the food they eat.'], ['Shelter', 'Nests, burrows, dens.'], ['Air', 'Many land animals breathe with lungs; fish use gills to get oxygen from water.']] },
  o: { topic: 'Ecosystems', rows: [['Producers', 'Plants and algae make their own food from sunlight.'], ['Consumers', 'Herbivores, carnivores and omnivores eat other living things.'],
    ['Decomposers', 'Fungi and bacteria break down dead matter and return nutrients to the soil.'], ['Nonliving factors', 'Sunlight, water, temperature, soil.'],
    ['Energy flow', 'Food chains and webs; only a small part of the energy (often about 10 percent) passes to the next level.'], ['Human impact', 'Habitat loss, pollution, invasive species.']] } },
  story: { y: { topic: 'The Tortoise and the Hare (Aesop)', rows: [['Characters', 'A slow Tortoise and a fast, proud Hare.'], ['Setting', 'A race course in the countryside.'], ['Problem', 'The Hare makes fun of the Tortoise for being slow, so they agree to race.'],
    ['Events', 'The Hare runs far ahead, then stops to nap. The Tortoise keeps going, slow and steady.'], ['Ending and lesson', 'The Tortoise crosses the finish line first. Lesson: slow and steady wins the race.']] },
  o: { topic: 'The Gift of the Magi (O. Henry, 1905)', rows: [['Characters', 'Della and Jim Young, a young married couple with little money.'], ['Setting', 'A cheap furnished flat in New York City on Christmas Eve.'],
    ['Conflict', 'Della has only one dollar and eighty-seven cents to buy Jim a present (a struggle against poverty: character vs. society).'], ['Rising action', 'Della sells her long hair for twenty dollars and buys a platinum chain for Jim\'s prized gold watch.'],
    ['Climax', 'Jim reveals that he sold his watch to buy Della a set of combs for her hair.'], ['Resolution', 'They put the gifts away; neither can use them, but each now knows the other\'s love.'],
    ['Theme', 'Real generosity is sacrifice for someone you love; the narrator calls the pair the wisest of givers.']] } },
  frayer: { y: { topic: 'habitat', rows: [['Definition', 'The natural home where a plant or animal lives and gets what it needs.'], ['Characteristics', 'Has food, water, shelter and space.'],
    ['Examples', 'A pond for a frog. A desert for a camel. An ocean for a whale.'], ['Non-examples', 'A toy box. A parking lot for a whale.']] },
  o: { topic: 'democracy', rows: [['Definition', 'A system of government in which power comes from the people, who rule directly or through elected representatives.'],
    ['Characteristics', 'Free and fair elections. Rule of law. Protected rights such as free speech and a free press. Majority rule with minority rights.'],
    ['Examples', 'Ancient Athens (direct democracy, for male citizens only). The United States (a representative democracy and constitutional republic).'],
    ['Non-examples', 'An absolute monarchy. A dictatorship. A one-party state with no real elections.'], ['Word origin', 'Greek <i>demos</i> (people) + <i>kratos</i> (power, rule).']] } },
};
MODELS.tchart = { y: { topic: 'Living and nonliving', rows: [['Living', 'dog, tree, mushroom, ant, grass'], ['Nonliving', 'rock, water, chair, cloud, bike'],
    ['My sentence', 'I put the tree with living things because it grows and needs water.']] },
  o: { topic: 'Physical and chemical changes', rows: [['Physical change', 'ice melting, paper torn, sugar dissolving in water, glass breaking'], ['Chemical change', 'wood burning, iron rusting, bread baking, a nail turning green in vinegar'],
    ['Sum it up', 'I sorted by whether a new substance forms. Sugar dissolving was the hardest: it looks like it disappears, but it is still sugar, so it is physical.']] } };
MODELS.venn = MODELS.venn2;

function modelHtml(m) {
  return `<h3>Model: ${esc(m.topic)}</h3><p>A filled-in example for a sample topic. Show it after students try, or fill part of it with the class.</p>` +
    `<table class="ws-table org-model"><tbody>${m.rows.map(([k, v]) => `<tr><th>${esc(k)}</th><td>${v}</td></tr>`).join('')}</tbody></table>`;
}

const CSS = `
.org { margin-top: 2px; }
.org-grid { display: grid; gap: .12in; margin: .08in 0; }
.org-box { border: 1.5px solid #222; border-radius: 8px; padding: .05in .1in .07in; break-inside: avoid; display: flex; flex-direction: column; margin: .08in 0; background: #fff; }
.org-grid > .org-box, .org-stack > .org-box, .org-step > .org-box { margin: 0; }
.org-box.org-main { border-width: 2.6px; }
.org-head { margin: 0; line-height: 1.3; }
.org-lab { font: 700 12.5px/1.3 var(--sans); text-transform: uppercase; letter-spacing: .06em; margin-right: 4px; }
.org-q { font-size: 12.5px; color: #444; font-style: italic; }
.org-sub { margin: 4px 0 0; font-size: 12px; color: #444; font-weight: 600; }
.org-src { margin: 4px 0 0; font-size: 12px; color: #444; }
.org-lines { margin-top: auto; }
.org-lines span { display: block; height: var(--lh); border-bottom: 1px solid #888; position: relative; }
.org-lines span i { position: absolute; left: 0; bottom: 2px; font-size: 12.5px; color: #555; white-space: nowrap; }
.org-k2 .org-lines span::after { content: ''; position: absolute; left: 0; right: 0; top: 50%; border-top: 1px dashed #bbb; }
.org-k2 .org-lines span i { font-size: 15px; }
.org-k2 .org-lab { font-size: 16px; text-transform: none; letter-spacing: 0; }
.org-k2 .org-q { font-size: 14px; }
.org-draw { border: 1px dashed #888; border-radius: 6px; margin: 4px 0 2px; position: relative; }
.org-draw span { position: absolute; left: 6px; top: 3px; font-size: 10.5px; color: #888; }
.org-down { text-align: center; font: 700 18px/1 var(--sans); margin: 1px 0; }
.org-down span { font: 600 10.5px var(--sans); letter-spacing: .08em; text-transform: uppercase; color: #555; vertical-align: 3px; }
.org-right { align-self: center; font: 700 22px/1 var(--sans); }
.org-gap { height: .08in; }
.org-stack { display: flex; flex-direction: column; gap: .1in; }
.org-ce { display: grid; grid-template-columns: 1fr auto 1.35fr; gap: .1in; align-items: stretch; margin: .08in 0; }
.org-ce > .org-box { margin: 0; justify-content: center; }
.org-ce-arrows { align-self: center; font: 700 24px/2.6 var(--sans); }
.org-ce3 { display: grid; grid-template-columns: 1fr auto .8fr auto 1fr; gap: .08in; align-items: center; margin: .08in 0; }
.org-ce3 > .org-box { margin: 0; }
.org-step { display: grid; grid-template-columns: .34in 1fr; gap: .06in; align-items: center; }
.org-num { display: inline-grid; place-items: center; width: .3in; height: .3in; border: 2px solid #222; border-radius: 50%; font: 700 14px var(--sans); }
.org-ties { display: flex; justify-content: space-around; height: .14in; margin: -.08in 0 -.08in; }
.org-ties span { border-left: 2px solid #222; }
.org-table { width: 100%; border-collapse: collapse; margin: .06in 0 .08in; table-layout: fixed; }
.org-table th { border: 1.5px solid #222; padding: 4px 6px; font: 700 12.5px/1.2 var(--sans); background: #eee; -webkit-print-color-adjust: exact; print-color-adjust: exact; text-align: center; }
.org-table td { border: 1.5px solid #222; padding: 2px 6px 4px; vertical-align: bottom; position: relative; }
.org-cell-n { position: absolute; left: 5px; top: 3px; font-size: 12px; }
.org-k2 .org-table th { font-size: 15px; }
.org-hblank { display: inline-block; width: 75%; border-bottom: 1.5px solid #222; height: 1em; }
.org-circle { text-align: center; font-size: 13px; margin: 0 0 .3in; }
.org-tip { margin: 0 0 2px; font-size: 13px; }
.org-k2 .org-tip { font-size: 14.5px; }
.org-ideas { margin: 4px 0; font-size: 13px; }
.org-letter { display: inline-grid; place-items: center; width: 1.5em; height: 1.5em; border: 2px solid #222; border-radius: 50%; margin-right: 6px; font-size: 15px; letter-spacing: 0; }
.org-frayer { position: relative; }
.org-frayer > .org-grid { gap: .14in; }
.org-word { width: 2.8in; min-height: .62in; margin: 0 auto; border: 2.6px solid #222; border-radius: 50%; background: #fff; display: grid; place-items: center; text-align: center; padding: 6px 14px; box-sizing: border-box; }
.org-word b { font-size: 20px; overflow-wrap: anywhere; }
.org-word span { color: #888; font-size: 12px; border-top: 1.5px solid #222; width: 70%; margin-top: .22in; padding-top: 2px; }
.org-steps4 .org-box { min-height: 3.3in; }
.org-rowlab { display: block; font: 700 13px/1.25 var(--sans); position: absolute; left: 6px; top: 5px; right: 6px; }
.org-k2 .org-rowlab { font-size: 15px; }
.org-t td { vertical-align: top; }
.org-cut { display: flex; align-items: center; gap: 8px; margin: .1in 0 .04in; font-size: 10.5px; color: #555; }
.org-cut::before, .org-cut::after { content: ''; flex: 1; border-top: 1.5px dashed #555; }
.org-cards { display: grid; grid-template-columns: repeat(var(--n), 1fr); }
.org-cards span { border: 1.5px dashed #555; padding: 6px 8px; min-height: .3in; display: grid; place-items: center; text-align: center; font-size: 13px; }
.org-k2 .org-cards span { font-size: 15px; min-height: .38in; }
.org-model th { text-align: left; white-space: nowrap; width: 1%; vertical-align: top; }
.org-model td { text-align: left; height: auto; }
`;

Gen.add('organizer', {
  title: 'Graphic Organizer Maker', type: 'Organizer', noKey: true, css: CSS,
  fields: [
    { id: 'layout', label: 'Layout', type: 'select', options: LAYOUTS, def: 'venn2' },
    { id: 'band', label: 'Grade band', type: 'select', options: BANDS, def: '35' },
    { id: 'topic', label: 'Topic or title (optional)', type: 'text', def: '' },
    { id: 'starters', label: 'Add sentence starters', type: 'check', def: false },
    { id: 'rows', label: 'Row labels, comma separated (compare, cause and effect, sequence, chain)', type: 'text', def: '', show: v => ROWED.includes(v.layout) },
    { id: 'subjects', label: 'Things to compare (columns)', type: 'select', options: [['2', '2'], ['3', '3'], ['4', '4']], def: '2', show: v => v.layout === 'compare' },
    { id: 'cols', label: 'Column headers, comma separated (compare, T-chart)', type: 'text', def: '', show: v => v.layout === 'compare' || v.layout === 'tchart' },
    { id: 'cards', label: 'Cards to sort, comma separated (T-chart; prints a cut-out strip)', type: 'text', def: '', show: v => v.layout === 'tchart' },
  ],
  make(v, r) {
    const b = v.band, L = v.layout, topic = String(v.topic || '').trim();
    const K = kit(b, r, v.starters, GROW[L + "-" + b] || 1);
    const longTopic = topic.length > 55;
    const rows = ROWED.includes(L) ? list(v.rows, 8, 40) : [], cards = L === 'tchart' ? list(v.cards, 16, 36) : [];
    const tip = (longTopic ? `<p class="org-tip"><b>Topic:</b> ${esc(topic)}</p>` : '') + `<p class="org-tip"><b>Tip:</b> ${esc(r.pick(TIPS[L][young(b) ? 'y' : 'o']))}</p>`;
    const html = `<div class="org org-${b}">${tip}${BUILD[L](b, K, { topic, rows, subjects: v.subjects, cols: v.cols, cards })}</div>`;
    const yo = young(b) ? 'y' : 'o', m = MODELS[L][yo];
    const band = BANDS.find(x => x[0] === b)[1];
    const many = L === 'compare' && +v.subjects > 2 ? s => s.replace('two things', ['three', 'four'][v.subjects - 3] + ' things') : s => s;
    const tips = { k2: 'Read each box aloud with the class before students start. Students may draw first and then write a word or a sentence.',
      35: 'Model the first box aloud. Students who finish early can add a detail to every box.',
      68: 'Ask students to cite where each detail came from (page, paragraph, source).', 912: 'Expect academic vocabulary and cited evidence in every box.' }[b];
    return {
      title: (!longTopic && topic) || NAME[L].replace(/,.*$/, '').replace(' / flow chart', '').replace(' (two-column sort)', ''), eyebrow: 'Graphic organizer · ' + NAME[L], level: band,
      ican: many(pickB(ICAN[L], b)), directions: many(pickB(DIR[L], b)) + (cards.length ? ' Cut out the cards at the bottom and sort them into the two columns.' : '') + (v.starters ? ' Sentence starters are on the first line of each box; you can use them or start your own way.' : ''),
      minutes: b === 'k2' ? 20 : 25, materials: 'pencil' + (b === 'k2' ? ', crayons' : '') + (L === 'cer' ? ', your data or notes' : '') + (cards.length ? ', scissors, glue' : ''),
      parts: [['', html]], items: [],
      mistakes: MISTAKES[L],
      notes: `${USE[L]} ${tips} The guiding questions${v.starters ? ' and sentence starters' : ''} change with each New sheet, so neighbors can get different wording of the same organizer.`,
      teacher: modelHtml(m),
    };
  },
});
})();
