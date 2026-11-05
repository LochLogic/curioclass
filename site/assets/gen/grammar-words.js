// Grammar and Word Study generator, grades 1-12. Practice sheets with an answer key, drawn from the hand-written,
// tagged sentence and word banks in grammar-words-data.js (loaded first). Grade sets which skills show.
// Grammar: parts of speech, collective nouns, verb tense (past, present, future; irregular past; change to past;
//   perfect tenses), subject-verb agreement, pronoun agreement and case, relative pronouns, comparatives, joining
//   sentences with and/but/or, linking words, the four kinds of sentences, fragments and run-ons, simple, compound and
//   complex sentences, phrases and clauses, verbals, active and passive voice, verb mood, parallel structure, concise
//   writing, formal and casual register, point of view.
// Mechanics: capitals and end marks, end marks, contractions, possessives, commas (series, compound, introductory,
//   direct address and tag questions, dates and places, dialogue), quotation marks in dialogue, titles, coordinate
//   adjectives, semicolon or colon, hyphens in compound modifiers.
// Word study and spelling: pattern sorts (word families, short vowels, silent e, digraphs, vowel teams, r-controlled),
//   root words and endings, compound words, prefixes and suffixes, suffix spelling rules, Greek and Latin roots (sets
//   by grade, including medical terms), synonyms and antonyms, shades of meaning, connotation, homophones, idioms,
//   literal and figurative language, fact and opinion.
// English learners (ELD): sentence frames by function and proficiency level (emerging, expanding, bridging) for a
//   typed topic, signal word sorts, collocations (make, take, do, have), phrasal verbs, verbs to nouns
//   (nominalization).
// Standards: CCSS ELA L.1-12.1 (grammar and usage), L.1-12.2 (capitalization, punctuation, spelling), L.1-12.3
// (knowledge of language: register, concision, voice and mood), L.1-12.4b (affixes and roots), L.1-12.5 (figurative
// language, word relationships, shades of meaning, connotation), RL.4.6 (point of view), RI/W linking words (W.2-8.1c,
// W.2-8.2c); ELD frames follow the emerging / expanding / bridging levels of the California and WIDA-style ELD standards.
// verify() re-works every answer with spelling and grammar rules where one exists (verb forms, comparatives, suffix
// spelling, contractions read backward, possessives, comma and quotation removal, word parts that must spell the
// word, hyphen and comma rules for modifiers, end marks from the first word) and checks the bank tags otherwise.
(() => {
const { blank, part, example, esc, lines, fill, table, keyline, key } = Gen.h;
const D = Gen.gw;
const sp = s => s.split('|');
const ws = s => s.trim().split(/\s+/);
const cap1 = s => s.charAt(0).toUpperCase() + s.slice(1);
const low1 = s => s.charAt(0).toLowerCase() + s.slice(1);

/* ---------- spelling rules (used by verify, and by make only where noted) ---------- */
const V = {};
for (const line of D.verbs.split(/[|\n]/)) { const w = ws(line); if (w.length >= 5) V[w[0]] = { base: w[0], s: w[1], past: w[2], pp: w[3], ing: w[4], S: w[5] === 'S' }; }
const syl = w => { w = w.toLowerCase(); let n = (w.replace(/^y/, '').match(/[aeiouy]+/g) || []).length;
  if (/[^aeiouy]e$/.test(w) && !/[^aeiouy]le$/.test(w) && n > 1) n--; return Math.max(1, n); };
const cvc = w => /(^|[^aeiou])[aeiou][^aeiouwxy]$/.test(w) && !/qu[aeiou][^aeiou]$/.test(w);
const dbl = (w, S) => cvc(w) && (syl(w) === 1 || !!S);
function addSuf(b, suf, S) {
  const vow = /^[aeiouy]/.test(suf);
  if (/[^aeiou]y$/.test(b)) return suf[0] === 'i' ? b + suf : b.slice(0, -1) + 'i' + suf;
  if (/[^aeiou]e$/.test(b) && vow) return b.slice(0, -1) + suf;
  if (vow && dbl(b, S)) return b + b.slice(-1) + suf;
  return b + suf;
}
const sOf = b => b === 'have' ? 'has' : /(s|x|z|ch|sh|o)$/.test(b) ? b + 'es' : /[^aeiou]y$/.test(b) ? b.slice(0, -1) + 'ies' : b + 's';
const IRR = {}; for (const x of D.irrComp.split('|')) { const [a, b, c] = ws(x); IRR[a] = [b, c]; }
function compOf(a) {
  if (IRR[a]) return IRR[a];
  const n = syl(a);
  if (n === 1 || (n === 2 && /[^aeiou]y$/.test(a))) return [addSuf(a, 'er'), addSuf(a, 'est')];
  return ['more ' + a, 'most ' + a];
}
// contractions: make builds forward; verify reads the contraction backward
function contractOf(p) {
  if (p === 'will not') return 'won\'t'; if (p === 'cannot') return 'can\'t'; if (p === 'let us') return 'let\'s';
  const [a, b] = p.split(' ');
  if (b === 'not') return a + 'n\'t';
  return a + { am: '\'m', is: '\'s', are: '\'re', will: '\'ll', have: '\'ve', would: '\'d' }[b];
}
function expandOf(c) {
  if (c === 'won\'t') return 'will not'; if (c === 'can\'t') return 'cannot'; if (c === 'let\'s') return 'let us';
  const m = c.match(/^(.+?)(n't|'m|'s|'re|'ll|'ve|'d)$/);
  if (!m) return '';
  return m[1] + ' ' + { 'n\'t': 'not', '\'m': 'am', '\'s': 'is', '\'re': 'are', '\'ll': 'will', '\'ve': 'have', '\'d': 'would' }[m[2]];
}

/* ---------- bank parsing ---------- */
const VERB_PAST = b => V[b] && V[b].past;
const POSRE = /\[([^:\]]+):(\w+)\]/g;
const posPlain = s => s.replace(POSRE, '$1');
const PARTS = {};
for (const x of D.parts.replace(/\n/g, '').split(',')) { const [p, m, k] = sp(x.trim()); if (p) PARTS[p] = { m, k }; }
const bare = p => p.replace(/~.*/, '');
const NAMES = new Set(ws(D.names));
const SUBS = new Set(ws(D.subordinators));
const CADV = new Set(ws(D.conjAdverbs));
const LONGW = new Set(D.longWorks.split(' ').concat(['TV show']));
const ADJK = Object.fromEntries(D.adjKind.split('|').map(x => ws(x)));
const COMPOUNDS = new Set(ws(D.compoundExtra).concat(D.compound.split('|').map(x => ws(x).join(''))));

const LAB = { n: 'noun', v: 'verb', adj: 'adjective', adv: 'adverb', pron: 'pronoun', prep: 'preposition', conj: 'conjunction', interj: 'interjection' };
const posTags = g => g <= 2 ? ['n', 'v', 'adj'] : g <= 4 ? ['n', 'v', 'adj', 'adv', 'pron'] : ['n', 'v', 'adj', 'adv', 'pron', 'prep', 'conj', 'interj'];
const QW = /^(who|what|where|when|why|how|is|are|can|do|does|did|will|may)\b/i;
const EXW = /^(wow|oh no|hooray|ouch|yay|help)\b/i;
const endOf = s => QW.test(s) ? '?' : EXW.test(s) ? '!' : '.';
const kindOf = s => s.endsWith('?') ? 'q' : s.endsWith('!') ? 'e' : s.startsWith('^') ? 'c' : 's';
const KINDLAB = g => g <= 3 ? { s: 'statement', q: 'question', c: 'command', e: 'exclamation' } : { s: 'declarative', q: 'interrogative', c: 'imperative', e: 'exclamatory' };
const capsShown = a => a.toLowerCase().replace(/[.?!]$/, '');
const stripQ = a => a.replace(/"([a-z])/gi, (m, c, i) => i === 0 ? c : c).replace(/[",]/g, '');
// the dialogue as printed: no quotation marks or commas, and the first word of a quotation inside the line in lower case
function quoteShown(a) {
  let out = '', inq = false;
  for (let i = 0; i < a.length; i++) {
    const c = a[i];
    if (c === '"') { inq = !inq; if (inq && i > 0) { const w = a.slice(i + 1).match(/^[A-Za-z']+/)[0]; if (w !== 'I' && !NAMES.has(w)) { out += a[i + 1].toLowerCase(); i++; } } continue; }
    if (c === ',') continue;
    out += c;
  }
  return out.replace(/\s+/g, ' ');
}
const joinS = (s1, s2, c) => { const w = s2.split(' ')[0]; return s1.replace(/[.?!]$/, '') + ', ' + c + ' ' + (NAMES.has(w) ? s2 : low1(s2)); };
const article = w => /^[aeiou]/i.test(w) ? 'an' : 'a';
const coordOf = (a, b) => ADJK[a] === 'q' && ADJK[b] === 'q';
const hyphOf = (m, pos) => pos === 'b' && !/ly$/.test(m.split(' ')[0]) ? m.replace(/ /g, '-') : 'no hyphen';
const SEMI = { ic: [';', 'A'], ca: [';', 'B'], ser: [';', 'C'], list: [':', 'D'], exp: [':', 'E'] };
const REASONS = [['A', 'joins two complete sentences that are closely related'], ['B', 'joins two sentences when the second starts with a transition such as however or therefore'],
  ['C', 'separates items in a list when the items already have commas'], ['D', 'introduces a list after a complete sentence'], ['E', 'introduces an explanation or example after a complete sentence']];
const linkWords = {};
for (const x of D.linkWords.split('|')) { const [rel, ...rest] = x.split(/:(.*)/s)[0] ? [x.slice(0, x.indexOf(':')), x.slice(x.indexOf(':') + 1)] : []; linkWords[rel] = rest[0].split(',').map(y => { const [w, g] = y.split(':'); return [w, +g]; }); }
const PAT_GRADE = { fam: 1, short: 1, magic: 1, digraph: 1, teams: 2, rctl: 2 };
const PAT_LAB = { fam: 'Word families (-at, -ig, -op ...)', short: 'Short vowels', magic: 'Short vowel or silent e', digraph: 'Digraphs: sh, ch, th', teams: 'Vowel teams', rctl: 'R-controlled vowels' };
const ROOT_SETS = [['tpg', 'tele, photo, graph', 4], ['prs', 'port, rupt, struct', 4], ['bgt', 'bio, geo, therm', 5], ['misc', 'spect, ject, tract, mit, vert, scribe', 5],
  ['avd', 'aud, vis, dict', 6], ['afs', 'act, form, sign', 6], ['bcd', 'bell, cred, dict', 7], ['ced', 'cede, ceed, cess', 8], ['greek', 'Greek: chron, psych, phon, micro', 8],
  ['med', 'Medical word parts', 9]];
const COMMA_KINDS = [['series', 'Items in a series', 3], ['dateplace', 'Dates and places', 3], ['quote', 'Dialogue and quotations', 3], ['compound', 'Compound sentences', 4],
  ['intro', 'Introductory words and phrases', 5], ['address', 'Yes and no, names, tag questions', 5]];
const commaKind = k => k === 'date' || k === 'place' ? 'dateplace' : k === 'yesno' || k === 'tag' ? 'address' : k;
const SIG_SETS = { ce: [['cause', 'Cause words'], ['effect', 'Effect words']], cc: [['compare', 'Alike (compare)'], ['contrast', 'Different (contrast)']],
  seq: [['begin', 'Beginning'], ['middle', 'Middle'], ['end', 'End']], mix: [['cause', 'Cause'], ['effect', 'Effect'], ['contrast', 'Contrast'], ['example', 'Example']] };
const FRAME_FN = [['describe', 'Describe'], ['compare', 'Compare and contrast'], ['cause', 'Cause and effect'], ['opinion', 'Give an opinion'], ['sequence', 'Tell the order (sequence)'],
  ['ask', 'Ask questions'], ['request', 'Make a polite request'], ['discuss', 'Discussion: agree, disagree, add on']];
const LEVELS = [['e', 'Emerging'], ['x', 'Expanding'], ['b', 'Bridging']];

/* ---------- html pieces ---------- */
const opts = list => ` <span class="gw-opts">(${list.map(esc).join(' / ')})</span>`;
const bankBox = list => `<div class="gen-wordbank">${list.map(w => `<span>${esc(w)}</span>`).join('')}</div>`;
const editRow = (shown, ans, n = 1, hint = '') => `<span class="gw-edit">${esc(shown)}</span>${hint}${lines(n)}${keyline(esc(ans))}`;
const turn = (name, prompt, n) => part(name, `<p class="ws-text">${prompt}</p>${lines(n)}`);
const W = list => Math.min(10, Math.max(2.4, Math.max(...list.map(x => String(x).length)) * 0.6 + 1.2));
const pickN = (r, arr, n) => r.sample(arr, Math.min(n, arr.length));

/* ---------- the skills ---------- */
// lo, hi: grades; n(g): counts for s, m, l; make(c) gets {g, r, N, v} and returns the sheet pieces
const nStd = g => g <= 2 ? [6, 8, 10] : g <= 5 ? [8, 10, 12] : [10, 12, 15];
const nRw = g => g <= 2 ? [4, 6, 8] : [6, 8, 10];
const SK = {};
const add = (id, label, lo, hi, n, def) => { SK[id] = Object.assign({ id, label, lo, hi, n }, def); };

add('pos', 'Grammar: parts of speech', 2, 8, nStd, {
  title: 'Parts of Speech',
  make({ g, r, N }) {
    const tags = posTags(g), used = new Set(), items = [];
    const order = [];
    while (order.length < N) order.push(...r.shuffle(tags));
    for (const t of order.slice(0, N + 6)) {
      if (items.length >= N) break;
      const cands = D.pos.filter(s => !used.has(s) && [...s.matchAll(POSRE)].some(m => m[2] === t));
      if (!cands.length) continue;
      const s = r.pick(cands); used.add(s);
      const words = [...s.matchAll(POSRE)].filter(m => m[2] === t);
      const w = r.pick(words)[1];
      let done = false;
      const html = esc(s).replace(/\[([^:\]]+):(\w+)\]/g, (m, x, tg) => { if (!done && x === esc(w) && tg === t) { done = true; return `<u class="gw-u">${x}</u>`; } return x; });
      items.push({ q: `${posPlain(s)} [${w}]`, a: LAB[t], src: s, word: w, html });
    }
    const labs = tags.map(t => LAB[t]);
    const wide = W(labs);
    return { ican: 'I can name the part of speech of a word by what it does in the sentence.',
      directions: 'Read each sentence. Write the part of speech of the underlined word on the line. Use the words in the box.',
      parts: [part('', example(`The <u class="gw-u">little</u> cat slept. &nbsp; <b>adjective</b>`, 'Little tells what kind of cat, so it is an adjective.')),
        part('Name the part of speech', bankBox(labs) + fill(items.map(it => `${it.html} ${blank(it.a, wide)}`)))],
      items, mistakes: 'Labeling a word by what it usually is instead of how it works here (a word like <i>hard</i> can be an adjective or an adverb).',
      notes: `Labels at this grade: ${labs.join(', ')}.` };
  },
  verify(it) { const m = it.src.match(new RegExp(`\\[${it.word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}:(\\w+)\\]`)); return D.pos.includes(it.src) && m && LAB[m[1]] === it.a ? '' : `${it.q}: tag mismatch`; },
});

add('collective', 'Grammar: collective nouns', 2, 3, () => [6, 8, 10], {
  title: 'Collective Nouns',
  make({ r, N }) {
    const all = r.shuffle(D.collective.map(x => { const [c, n, alt] = sp(x); return { c, n, alt: alt ? alt.split(',') : [] }; }).filter(e => e.c !== 'team'));
    const pick = [];
    for (const e of all) { if (pick.length >= N) break;
      if (pick.some(p => p.alt.includes(e.c) || e.alt.includes(p.c) || p.c === e.c)) continue; pick.push(e); }
    const items = pick.map(e => ({ q: `a ___ of ${e.n}`, a: e.c, noun: e.n, others: pick.map(p => p.c) }));
    return { ican: 'I can use collective nouns, the words for a group of people, animals or things.',
      directions: 'Write the word from the box that names each group. Use each word once.',
      parts: [part('', example('a <b>team</b> of players', 'Team is the word for a group of players.')),
        part('Name the group', bankBox(r.shuffle(pick.map(p => p.c))) + fill(items.map(it => `a ${blank(it.a, 5)} of ${esc(it.noun)}`), 2)),
        turn('Your turn', 'Choose two groups from the box. Write a sentence about each one.', 4)],
      items, mistakes: 'Picking a group word that sounds right but belongs to another animal (a pack of cows).',
      notes: 'Pictures are not printed; read the nouns aloud for early readers. A herd of sheep and a pack of cards are also fine, so those pairs never share a sheet.' };
  },
  verify(it) {
    const e = D.collective.map(sp).find(x => x[1] === it.noun);
    if (!e || e[0] !== it.a) return `${it.q}: wrong group word`;
    const alts = e[2] ? e[2].split(',') : [];
    return it.others.some(o => o !== it.a && alts.includes(o)) ? `${it.q}: two box words fit` : '';
  },
});

add('tense', 'Grammar: past, present and future verbs', 1, 4, g => g <= 2 ? [5, 6, 8] : [6, 8, 10], {
  title: 'Past, Present and Future',
  make({ g, r, N }) {
    let pool = ws(D.tense1).filter(b => b !== 'jump');
    if (g >= 2) pool = pool.concat(ws(D.tense2));
    let verbs;
    if (g >= 3) { const irr = ws(D.tense3), k = Math.ceil(N / 2); verbs = pickN(r, irr, k).concat(pickN(r, pool, N - k)); verbs = r.shuffle(verbs); }
    else verbs = pickN(r, pool, N);
    const items = verbs.map(b => ({ q: `tense: ${b}`, a: `${V[b].past}, ${V[b].s}, will ${b}`, base: b, past: V[b].past, pres: V[b].s, fut: `will ${b}` }));
    const rows = items.map(it => [`<b>${esc(it.base)}</b>`, blank(it.past, 6), blank(it.pres, 6), blank(it.fut, 7)]);
    return { ican: 'I can write a verb to tell about yesterday, today and tomorrow.',
      directions: 'Write each verb three ways: what happened yesterday (past), what happens today (present, for he or she) and what will happen tomorrow (future).',
      parts: [part('', example('<b>jump</b>: yesterday she <b>jumped</b>, today she <b>jumps</b>, tomorrow she <b>will jump</b>.')),
        part('Fill the time line', `<div class="gw-tl"><span>Yesterday</span><span>Today</span><span>Tomorrow</span></div>` +
          table(['Verb', 'Yesterday (past)', 'Today (present)', 'Tomorrow (future)'], rows)),
        turn('Your turn', g <= 2 ? 'Write one sentence about something you did yesterday.' : 'Write one sentence in the past and one in the future. Use verbs from the chart.', g <= 2 ? 2 : 3)],
      items, mistakes: g >= 3 ? 'Adding -ed to irregular verbs (runned, buyed) and forgetting the -s on the present form.' : 'Forgetting the -s on the present form (she jump) or doubling where no doubling is needed.',
      notes: g >= 3 ? 'About half the verbs are irregular. The present column uses the he or she form.' : 'The present column uses the he or she form, so the answer ends in -s or -es.' };
  },
  verify(it) {
    const v = V[it.base]; if (!v) return `${it.base}: not a bank verb`;
    if (it.pres !== sOf(it.base)) return `${it.base}: present ${it.pres} breaks the -s rule`;
    if (ws(D.tense3).includes(it.base)) return v.past === it.past ? '' : `${it.base}: past`;
    return it.past === addSuf(it.base, 'ed', v.S) ? '' : `${it.base}: past ${it.past} breaks the -ed rule`;
  },
});

add('tensechange', 'Grammar: change to past tense', 2, 5, nRw, {
  title: 'Change It to the Past',
  make({ r, N }) {
    const items = pickN(r, D.tensechange, N).map(x => { const [s, b] = sp(x); const v = V[b];
      const toks = s.split(' '), i = toks.findIndex(t => t === v.s || t === v.base); toks[i] = v.past;
      return { q: s, a: toks.join(' '), base: b }; });
    return { ican: 'I can change a sentence so it tells about the past, including irregular verbs.',
      directions: 'Each sentence tells about now. Rewrite it so it tells about the past. Change only the verb.',
      parts: [part('', example('The dog <b>jumps</b> over the log. &rarr; The dog <b>jumped</b> over the log.')),
        part('Rewrite in the past tense', fill(items.map(it => editRow(it.q, it.a))))],
      items, mistakes: 'Adding -ed to irregular verbs (builded, goed) and changing words that are not verbs.',
      notes: 'About half the verbs are irregular. Students who finish can underline the verb in each new sentence.' };
  },
  verify(it) {
    const a = it.q.split(' '), b = it.a.split(' ');
    if (a.length !== b.length) return `${it.q}: word count changed`;
    const diff = a.map((w, i) => i).filter(i => a[i] !== b[i]);
    if (diff.length !== 1) return `${it.q}: ${diff.length} words changed`;
    const v = V[it.base], i = diff[0];
    if (!v || (a[i] !== v.s && a[i] !== v.base)) return `${it.q}: changed word is not the verb`;
    return b[i] === v.past ? '' : `${it.q}: past form`;
  },
});

add('perfect', 'Grammar: perfect tenses', 5, 8, () => [6, 8, 10], {
  title: 'Perfect Tenses',
  make({ r, N }) {
    const NAME = { prp: 'present perfect', pp: 'past perfect', fp: 'future perfect' };
    const items = pickN(r, D.perfect, N).map(x => { const [s, b, t, n] = sp(x); const pp = V[b].pp;
      const a = t === 'pp' ? `had ${pp}` : t === 'fp' ? `will have ${pp}` : `${n === 's' ? 'has' : 'have'} ${pp}`;
      return { q: s, a, base: b, tense: t, num: n, tname: NAME[t] }; });
    return { ican: 'I can form and use the present, past and future perfect tenses.',
      directions: 'Write the verb in the tense shown. Use has or have, had, or will have with the past participle.',
      parts: [part('', example('By noon, we <b>will have eaten</b> lunch. (eat, future perfect)', 'Present perfect: has or have + participle. Past perfect: had + participle. Future perfect: will have + participle.')),
        part('Write the perfect tense', fill(items.map(it => esc(it.q).replace('___', blank(it.a, 8)) + ` <span class="gw-opts">(${esc(it.base)}, ${it.tname})</span>`)))],
      items, mistakes: 'Using the simple past instead of the participle (had wrote, has went) and has with plural subjects.',
      notes: 'Each sentence has a time clue (by, before, since, for) that fits its tense. Ask students to circle it.' };
  },
  verify(it) {
    const v = V[it.base]; if (!v) return `${it.base}: not a bank verb`;
    const ppOk = ws(D.tense3).concat(['rise', 'set', 'read', 'leave']).includes(it.base) ? v.pp : addSuf(it.base, 'ed', v.S);
    const aux = it.tense === 'pp' ? 'had' : it.tense === 'fp' ? 'will have' : (it.num === 's' ? 'has' : 'have');
    return it.a === `${aux} ${ppOk}` ? '' : `${it.q}: ${it.a}`;
  },
});

add('sva', 'Grammar: subject-verb agreement', 2, 6, nStd, {
  title: 'Subject-Verb Agreement',
  make({ g, r, N }) {
    const items = pickN(r, D.sva.filter(x => +sp(x)[4] <= g), N).map(x => { const [s, si, pl, n] = sp(x);
      return { q: s, a: n === 's' ? si : pl, si, pl, num: n, o: r.shuffle([si, pl]) }; });
    return { ican: 'I can choose the verb that agrees with the subject.',
      directions: 'Write the verb that agrees with the subject of each sentence.',
      parts: [part('', example('The frogs <b>jump</b> into the pond. (jump / jumps)', 'Frogs is plural, so the verb has no -s.')),
        part('Make them agree', fill(items.map(it => esc(it.q).replace('___', blank(it.a, 4.5)) + opts(it.o))))],
      items, mistakes: g >= 4 ? 'Matching the verb to the nearest noun instead of the subject (the box of crayons are).' : 'Adding -s to the verb when the subject is plural.',
      notes: 'A singular subject takes the verb with -s (or is, has, does); a plural subject takes the verb without it.' };
  },
  verify(it) {
    const ex = { is: 'are', has: 'have', does: 'do' };
    if (!(ex[it.si] === it.pl || it.si === sOf(it.pl))) return `${it.q}: forms ${it.si}/${it.pl}`;
    return it.a === (it.num === 's' ? it.si : it.pl) ? '' : `${it.q}: answer`;
  },
});

const pickSkill = (bankKey, opt) => ({
  make({ g, r, N }) {
    const src = D[bankKey].filter(x => !opt.grade || +sp(x)[3] <= g);
    const items = pickN(r, src, N).map(x => { const [s, o, a] = sp(x); return { q: s, a, o: o.split('/') }; });
    const wide = W(items.flatMap(it => it.o));
    return { ican: opt.ican, directions: opt.dir, parts: [part('', example(opt.ex)),
      part(opt.part, fill(items.map(it => esc(it.q).replace('___', blank(it.a, wide)) + opts(it.o))))].concat(opt.turn ? [turn('Your turn', opt.turn, 3)] : []),
    items, mistakes: opt.mis, notes: opt.notes };
  },
  verify(it) { const x = D[bankKey].map(sp).find(e => e[0] === it.q);
    return x && x[2] === it.a && it.o.filter(o => o === it.a).length === 1 ? '' : `${it.q}: answer not in the bank or options`; },
});

add('pronoun', 'Grammar: pronouns (agreement and case)', 3, 8, nStd, Object.assign({ title: 'Pronouns' }, pickSkill('pronoun', {
  ican: 'I can choose the pronoun that matches the word it stands for and its place in the sentence.',
  dir: 'Write the pronoun that fits each sentence.', ex: 'The girls lost <b>their</b> ball. (her / their)', part: 'Choose the pronoun',
  mis: 'Me and him as subjects (Me and Ana went), and it\'s for its.', notes: 'A trick for pairs: cover the other person. "Mom drove ___ to school" shows me, not I.' })));

add('homophone', 'Word study: homophones and often-confused words', 2, 8, nStd, Object.assign({ title: 'Homophones and Confused Words' }, pickSkill('homophone', {
  grade: true, ican: 'I can choose the right spelling for words that sound alike.', dir: 'Write the word that fits each sentence.',
  ex: 'We ate <b>eight</b> grapes. (ate / eight)', part: 'Choose the word', turn: 'Pick one pair from the sheet. Write a sentence for each word in the pair.',
  mis: 'Their, there and they\'re; its and it\'s. Read the sentence with the long form (they are, it is) to test it.', notes: 'Harder pairs (its and it\'s, than and then) start at grade 4; affect and effect at grade 6.' })));

add('relpron', 'Grammar: relative pronouns', 4, 6, () => [6, 8, 10], Object.assign({ title: 'Relative Pronouns' }, pickSkill('relpron', {
  ican: 'I can use who, whose, which and that to join ideas.', dir: 'Write the relative pronoun that fits. Who is for people, whose shows ownership, which and that are for things.',
  ex: 'The man <b>who</b> fixed our sink was friendly. (who / which / whose)', part: 'Choose the relative pronoun',
  turn: 'Write two sentences about an inventor: one with who and one with which.',
  mis: 'Which for people, and that after a comma. Which follows a comma; that does not.', notes: 'Each sentence lists three choices with exactly one right answer.' })));

add('colloc', 'English learners: make, take, do, have', 3, 8, nStd, {
  title: 'Make, Take, Do or Have',
  make({ r, N }) {
    const items = pickN(r, D.colloc, N).map(x => { const [s, a] = sp(x); const start = s.startsWith('___'); return { q: s, a: start ? cap1(a) : a, base: a, start }; });
    return { ican: 'I can use the right verb with common word partners, like make a decision and take a photo.',
      directions: 'Write make, take, do or have in each sentence. Some words go together in English, so learn them as a pair.',
      parts: [part('', example('Please <b>take</b> a seat. (make / take / do / have)')),
        part('Choose the verb', bankBox(['make', 'take', 'do', 'have']) + fill(items.map(it => esc(it.q).replace('___', blank(it.a, 4)))))],
      items, mistakes: 'Do a mistake, make homework, and other word-for-word translations from a first language.',
      notes: 'American English pairs. Students who finish can write their own sentence with one pair from each verb.' };
  },
  verify(it) { const x = D.colloc.map(sp).find(e => e[0] === it.q); return x && x[1] === it.base && ['make', 'take', 'do', 'have'].includes(it.base) ? '' : `${it.q}: answer`; },
});

add('comp', 'Grammar: comparing with -er, -est, more and most', 2, 5, g => g <= 2 ? [6, 8, 10] : [8, 10, 12], {
  title: 'Comparing Words',
  make({ g, r, N }) {
    const pool = D.comp.map(sp).filter(([a]) => a !== 'tall' && a !== 'careful').filter(([a]) => g >= 3 || (syl(a) === 1 && !IRR[a]));
    const items = pickN(r, pool, N).map(([a, c, s]) => ({ q: `compare: ${a}`, a: `${c}, ${s}`, adj: a, c, s }));
    const rows = items.map(it => [`<b>${esc(it.adj)}</b>`, blank(it.c, 7), blank(it.s, 7)]);
    return { ican: 'I can use -er and -est, or more and most, to compare.',
      directions: 'Write the form that compares two things, then the form that compares three or more.',
      parts: [part('', example('<b>tall</b>: taller, tallest', '<b>careful</b>: more careful, most careful', 'Short words take -er and -est. Long words take more and most.')),
        part('Compare', table(['Word', 'Compares two', 'Compares three or more'], rows)),
        turn('Your turn', 'Write one sentence that compares two things and one that compares three or more.', 3)],
      items, mistakes: 'Double comparing (more taller), and missing spelling changes (biger, happyer).',
      notes: g >= 3 ? 'Includes irregular forms (good, better, best).' : 'One-syllable words only at grade 2.' };
  },
  verify(it) { const [c, s] = compOf(it.adj); return c === it.c && s === it.s ? '' : `${it.adj}: ${it.c}, ${it.s} should be ${c}, ${s}`; },
});

add('conj', 'Grammar: join sentences with and, but, or', 1, 3, g => g <= 2 ? [4, 6, 8] : [6, 8, 10], {
  title: 'And, But, Or',
  make({ g, r, N }) {
    const items = pickN(r, D.conj, N).map(x => { const [s1, s2, c] = sp(x); return { q: `${s1} ${s2}`, a: joinS(s1, s2, c), s1, s2, c }; });
    return { ican: 'I can join two sentences with and, but or or.',
      directions: 'Read the two sentences. Choose and, but or or. Write them as one sentence with a comma before the joining word.',
      parts: [part('', example('I like dogs. My brother likes cats. &rarr; I like dogs, <b>and</b> my brother likes cats.', 'And adds an idea. But shows a difference. Or gives a choice.')),
        part('Join the sentences', fill(items.map(it => editRow(`${it.s1} ${it.s2}`, it.a, g <= 2 ? 2 : 1, opts(['and', 'but', 'or'])))))],
      items, mistakes: 'Using and when the ideas do not match (I wanted to play, and it was raining) and forgetting the comma.',
      notes: 'Pictures are not printed; read each pair aloud for early readers. The key keeps the second sentence\'s capital only for names and I.' };
  },
  verify(it) {
    const x = D.conj.map(sp).find(e => e[0] === it.s1 && e[1] === it.s2);
    if (!x || x[2] !== it.c) return `${it.q}: joining word`;
    const head = it.s1.slice(0, -1) + ', ' + it.c + ' ', tail = it.s2.split(' ').slice(1).join(' ');
    return it.a.startsWith(head) && it.a.endsWith(tail) && it.a.toLowerCase() === (head + it.s2).toLowerCase() ? '' : `${it.q}: joined sentence`;
  },
});

add('link', 'Grammar: linking words and transitions', 3, 9, g => g <= 4 ? [6, 8, 10] : [8, 10, 12], {
  title: 'Linking Words',
  make({ g, r, N }) {
    const sub = D.linkSub.map(x => { const [s, a] = sp(x); const st = s.startsWith('___'); return { kind: 'sub', q: s, a: st ? cap1(a) : a, base: a, o: ['because', 'although', 'so'].map(w => st ? cap1(w) : w) }; });
    const adv = g < 5 ? [] : D.linkAdv.map(x => { const [s1, s2, rel] = sp(x);
      const word = w => r.pick(linkWords[w].filter(y => y[1] <= g))[0];
      const others = ['contrast', 'add', 'result', 'example', 'similar'].filter(x2 => x2 !== rel && !(rel === 'similar' && x2 === 'add') && !(rel === 'add' && x2 === 'similar'));
      const o = r.shuffle([word(rel)].concat(r.sample(others, 3).map(word)));
      return { kind: 'adv', q: `${s1} ${s2}`, a: o.find(w => linkWords[rel].some(y => y[0] === w)), rel, s1, s2, o }; });
    const k = g < 5 ? N : Math.round(N / 3);
    const items = r.shuffle(pickN(r, sub, k).concat(pickN(r, adv, N - k)));
    const wide = W(items.flatMap(it => it.o));
    const row = it => it.kind === 'sub' ? esc(it.q).replace('___', blank(it.a, wide)) + opts(it.o) : `${esc(it.s1)} ${blank(it.a, wide)}, ${esc(it.s2)}` + opts(it.o);
    return { ican: 'I can choose a linking word that shows how two ideas connect.',
      directions: 'Write the linking word that shows how the ideas connect. Read the whole sentence with your choice before you write it.',
      parts: [part('', example(g < 5 ? 'I wore a coat <b>because</b> it was cold. (because / although / so)' : 'Plants need water. <b>As a result</b>, we water the garden every day.',
          g < 5 ? 'Because gives a reason. Although shows a surprise. So tells what happened next.' : 'Contrast: however. Adding: in addition, moreover. Result: as a result, therefore. Example: for example. Alike: similarly.')),
        part('Choose the linking word', fill(items.map(row))), turn('Your turn', 'Write two sentences of your own about a topic you are studying. Use a different linking word in each.', 3)],
      items, mistakes: 'However where the ideas agree, and for example where the second idea is not an example of the first.',
      notes: g < 5 ? 'Because, although and so.' : 'Mixes because, although and so with transition words between sentences.' };
  },
  verify(it) {
    if (it.kind === 'sub') { const x = D.linkSub.map(sp).find(e => e[0] === it.q); return x && x[1] === it.base && it.a.toLowerCase() === it.base ? '' : `${it.q}: answer`; }
    const x = D.linkAdv.map(sp).find(e => e[0] === it.s1 && e[1] === it.s2);
    if (!x || x[2] !== it.rel) return `${it.q}: relation`;
    const fit = it.o.filter(w => linkWords[it.rel].some(y => y[0] === w));
    return fit.length === 1 && fit[0] === it.a ? '' : `${it.q}: ${fit.length} options fit`;
  },
});

const labelSkill = (o) => ({
  make({ g, r, N }) {
    const pool = o.pool(g);
    const items = pickN(r, pool, N).map(x => o.item(x, g, r));
    const labs = o.labels(g);
    const wide = W(labs.concat(items.map(it => it.a)));
    return { ican: o.ican, directions: o.dir(g), parts: [part('', example(...o.ex(g))),
      part(o.part, bankBox(labs) + fill(items.map(it => `${it.html || esc(it.q)} ${blank(it.a, wide)}${it.extra || ''}`)))].concat(o.turn ? [turn(o.turnName || 'Your turn', o.turn(g), o.turnLines || 3)] : []),
    items, mistakes: o.mis, notes: typeof o.notes === 'function' ? o.notes(g) : o.notes };
  },
});

add('kinds', 'Sentences: the four kinds', 2, 5, nStd, Object.assign({ title: 'Four Kinds of Sentences',
  verify(it) { return KINDLAB(it.g)[kindOf(it.src)] === it.a ? '' : `${it.q}: kind`; } }, labelSkill({
  pool: () => D.kinds, labels: g => Object.values(KINDLAB(g)),
  item: (x, g) => ({ q: x.replace(/^\^/, ''), a: KINDLAB(g)[kindOf(x)], src: x, g }),
  ican: 'I can tell what kind of sentence I am reading by what it does and how it ends.',
  dir: g => g <= 3 ? 'Write statement, question, command or exclamation for each sentence.' : 'Write declarative, interrogative, imperative or exclamatory for each sentence.',
  ex: g => [g <= 3 ? 'Open the door. &nbsp; <b>command</b>' : 'Open the door. &nbsp; <b>imperative</b>', 'A command tells someone to do something. It often starts with a verb.'],
  part: 'Name the kind', turn: () => 'Write one question and one command of your own.',
  mis: 'Calling every sentence that ends in an exclamation point a command, and missing commands that end in a period.',
  notes: g => g <= 3 ? 'Plain names at grades 2-3: statement, question, command, exclamation.' : 'Formal names at grades 4-5; you can write the plain names on the board beside them.' })));

add('frag', 'Sentences: fragments and run-ons', 3, 8, nStd, Object.assign({ title: 'Fragments and Run-Ons',
  verify(it) { const x = D.frag.map(sp).find(e => e[0] === it.q);
    if (!x || x[1] !== it.a) return `${it.q}: label`;
    if (it.a === 'run-on' && !(it.q.split(/[.!?]/).length === 2)) return `${it.q}: a run-on should be one punctuated sentence`;
    return ''; } }, labelSkill({
  pool: () => D.frag.filter(x => !x.startsWith('The dog barked')), labels: () => ['complete', 'fragment', 'run-on'],
  item: x => { const [s, l, fix] = sp(x); return { q: s, a: l, extra: fix ? key(` <span class="gw-fix">Fix: ${esc(fix)}</span>`) : '' }; },
  ican: 'I can tell a complete sentence from a fragment or a run-on, and fix them.',
  dir: () => 'Write complete, fragment or run-on for each. Then fix three of the ones that are not complete.',
  ex: () => ['Under the bed. &nbsp; <b>fragment</b> (no subject and verb)', 'The dog barked the cat ran. &nbsp; <b>run-on</b> (two sentences with nothing between them)'],
  part: 'Complete, fragment or run-on?', turnName: 'Fix three', turn: () => 'Choose three that are not complete. Rewrite each one as a complete sentence.', turnLines: 5,
  mis: 'Calling a long sentence a run-on (length is not the problem), and fixing a run-on with only a comma.',
  notes: 'The key shows one fix for each fragment and run-on; other fixes are fine. A comma splice counts as a run-on here.' })));

add('stype', 'Sentences: simple, compound, complex', 3, 9, nStd, Object.assign({ title: 'Sentence Types',
  verify(it) { const [, i, d] = D.stype.map(sp).find(e => e[0] === it.q) || [];
    const want = +i >= 2 && +d >= 1 ? 'compound-complex' : +i >= 2 ? 'compound' : +d >= 1 ? 'complex' : 'simple';
    return want === it.a ? '' : `${it.q}: ${it.a} should be ${want}`; } }, labelSkill({
  pool: g => D.stype.filter(x => g >= 7 || !(+sp(x)[1] >= 2 && +sp(x)[2] >= 1)),
  labels: g => ['simple', 'compound', 'complex'].concat(g >= 7 ? ['compound-complex'] : []),
  item: x => { const [s, i, d] = sp(x); return { q: s, a: +i >= 2 && +d >= 1 ? 'compound-complex' : +i >= 2 ? 'compound' : +d >= 1 ? 'complex' : 'simple' }; },
  ican: 'I can tell simple, compound and complex sentences apart by their clauses.',
  dir: g => `Write ${g >= 7 ? 'simple, compound, complex or compound-complex' : 'simple, compound or complex'} for each sentence.`,
  ex: () => ['When it rained, we went inside. &nbsp; <b>complex</b>', 'One independent clause (we went inside) plus one dependent clause (when it rained).'],
  part: 'Name the type', turn: () => 'Write one compound sentence and one complex sentence about your weekend.',
  mis: 'Calling a sentence with a compound subject or verb (We swam and played) compound; it has one clause, so it is simple.',
  notes: g => g >= 7 ? 'Includes compound-complex sentences.' : 'Compound-complex sentences start at grade 7.' })));

add('clause', 'Sentences: phrases and clauses', 6, 9, nStd, Object.assign({ title: 'Phrase or Clause?',
  verify(it) { const x = D.clause.map(sp).find(e => e[0] === it.q); const tag = { p: 'phrase', i: 'independent clause', d: 'dependent clause' }[x && x[1]];
    if (tag !== it.a) return `${it.q}: label`;
    const first = it.q.split(' ')[0].toLowerCase();
    if (x[1] === 'd' && !SUBS.has(first)) return `${it.q}: dependent clause without a subordinator`;
    if (x[1] === 'i' && SUBS.has(first)) return `${it.q}: independent clause starts with a subordinator`;
    return ''; } }, labelSkill({
  pool: () => D.clause, labels: () => ['phrase', 'independent clause', 'dependent clause'],
  item: x => { const [s, t] = sp(x); return { q: s, a: { p: 'phrase', i: 'independent clause', d: 'dependent clause' }[t] }; },
  ican: 'I can tell phrases from clauses, and independent clauses from dependent ones.',
  dir: () => 'Write phrase, independent clause or dependent clause for each word group.',
  ex: () => ['before the game &nbsp; <b>phrase</b> (no subject and verb)', 'before we played the game &nbsp; <b>dependent clause</b> (subject and verb, but it cannot stand alone)'],
  part: 'Phrase or clause?', turn: () => 'Write one sentence that has an independent clause and a dependent clause. Underline the dependent clause.',
  mis: 'Calling a group with a verb form but no subject (running down the hall) a clause, and mixing up after the game (phrase) with after they won (clause).',
  notes: 'Some word groups start with the same word (after, before) as a phrase and as a clause, on purpose.' })));

add('verbal', 'Grammar: gerunds, participles, infinitives', 8, 12, () => [8, 10, 12], Object.assign({ title: 'Verbals',
  verify(it) { const x = D.verbal.map(sp).find(e => e[0] === it.src); if (!x || `${x[1]}, ${x[2]}` !== it.a) return `${it.q}: tag`;
    const ph = it.src.match(/\[([^\]]+)\]/)[1];
    if ((x[1] === 'infinitive') !== /^to /i.test(ph)) return `${it.q}: infinitive rule`;
    if (x[1] === 'gerund' && (x[2] !== 'noun' || !/ing$/.test(ph.split(' ')[0]))) return `${it.q}: gerund rule`;
    if (x[1] === 'participle' && x[2] !== 'adjective') return `${it.q}: participle rule`;
    return ''; } }, labelSkill({
  pool: () => D.verbal, labels: () => ['gerund', 'participle', 'infinitive', 'noun', 'adjective', 'adverb'],
  item: x => { const [s, t, f] = sp(x); return { q: s.replace(/[[\]]/g, ''), a: `${t}, ${f}`, src: s, html: esc(s).replace(/\[([^\]]+)\]/, '<u class="gw-u">$1</u>') }; },
  ican: 'I can identify gerunds, participles and infinitives and explain how each works in a sentence.',
  dir: () => 'Name the underlined verbal (gerund, participle or infinitive), then how it works (noun, adjective or adverb).',
  ex: () => ['<u class="gw-u">Hiking</u> is fun. &nbsp; <b>gerund, noun</b> (it is the subject)'],
  part: 'Name the verbal and its job', turn: () => 'Write one sentence with a gerund and one with an infinitive. Underline each verbal.',
  mis: 'Calling every -ing word a gerund; an -ing word that describes a noun is a participle.',
  notes: 'A gerund always works as a noun and a participle as an adjective; an infinitive can be a noun, adjective or adverb.' })));

add('mood', 'Grammar: verb mood', 8, 10, () => [8, 10, 12], Object.assign({ title: 'Verb Mood',
  verify(it) { const x = D.mood.map(sp).find(e => e[0] === it.q); if (!x || x[1] !== it.a) return `${it.q}: mood`;
    return (it.q.endsWith('?')) === (it.a === 'interrogative') ? '' : `${it.q}: question mark and mood disagree`; } }, labelSkill({
  pool: () => D.mood, labels: () => ['indicative', 'imperative', 'interrogative', 'conditional', 'subjunctive'],
  item: x => { const [s, m] = sp(x); return { q: s, a: m }; },
  ican: 'I can identify the mood of a verb and what it shows about the speaker.',
  dir: () => 'Write the mood of each sentence: indicative, imperative, interrogative, conditional or subjunctive.',
  ex: () => ['If I were you, I would rest. &nbsp; <b>subjunctive</b> (were for something not true)', 'Indicative states facts. Imperative gives commands. Interrogative asks. Conditional says what would or could happen. Subjunctive wishes, demands or imagines.'],
  part: 'Name the mood', turnName: 'Fix the shift', turn: () => 'This sentence shifts mood: "Take your seat, and you should open your book." Rewrite it so both parts are imperative. Then write one subjunctive sentence of your own.', turnLines: 3,
  mis: 'Calling were in I wish it were summer a past-tense mistake, and calling every sentence with if conditional.',
  notes: 'The fix-the-shift answer: Take your seat, and open your book.' })));

add('register', 'Style: formal or casual', 4, 10, () => [8, 10, 12], Object.assign({ title: 'Formal or Casual?',
  verify(it) { const x = D.register.map(sp).find(e => e[0] === it.q); return x && (x[1] ? 'casual' : 'formal') === it.a ? '' : `${it.q}: register`; } }, labelSkill({
  pool: () => D.register, labels: () => ['formal', 'casual'],
  item: x => { const [s, f] = sp(x); return { q: s, a: f ? 'casual' : 'formal', extra: f ? key(` <span class="gw-fix">Formal: ${esc(f)}</span>`) : '' }; },
  ican: 'I can tell formal language from casual language and change casual words for a formal audience.',
  dir: () => 'Write formal or casual for each sentence. Then rewrite three casual ones so they fit a school report or a letter.',
  ex: () => ['Wanna help? &nbsp; <b>casual</b> &rarr; Would you like to help?'],
  part: 'Formal or casual?', turnName: 'Make it formal', turn: () => 'Choose three casual sentences. Rewrite each one in formal language.', turnLines: 5,
  mis: 'Keeping slang (super, kinda) or short forms (gonna) in the formal versions.',
  notes: 'The key shows one formal version of each casual sentence. Casual is not wrong: it fits a text to a friend.' })));

add('factop', 'Reading: fact or opinion', 2, 5, nStd, Object.assign({ title: 'Fact or Opinion?',
  verify(it) { const x = D.factop.map(sp).find(e => e[0] === it.q); if (!x) return `${it.q}: bank`;
    if ((x[1] ? 'opinion' : 'fact') !== it.a) return `${it.q}: label`;
    return !x[1] || it.q.includes(x[1]) ? '' : `${it.q}: signal word missing`; } }, labelSkill({
  pool: () => D.factop, labels: () => ['fact', 'opinion'],
  item: x => { const [s, sig] = sp(x); return { q: s, a: sig ? 'opinion' : 'fact', extra: sig ? key(` <span class="gw-fix">Signal: ${esc(sig)}</span>`) : '' }; },
  ican: 'I can tell a fact, which can be checked, from an opinion, which tells what someone thinks or feels.',
  dir: () => 'Write fact or opinion. For each opinion, underline the word or words that show it is an opinion.',
  ex: () => ['Apples are the best fruit. &nbsp; <b>opinion</b> (best shows a feeling)'],
  part: 'Fact or opinion?', turn: () => 'Write one fact and one opinion about your school.',
  mis: 'Calling a sentence a fact because the student agrees with it.', notes: 'The key names the signal word in each opinion.' })));

add('figlit', 'Word study: literal or figurative', 3, 6, nStd, Object.assign({ title: 'Literal or Figurative?',
  verify(it) { const x = D.figlit.map(sp).find(e => e[0] === it.q); return x && (x[1] ? 'figurative' : 'literal') === it.a ? '' : `${it.q}: label`; } }, labelSkill({
  pool: () => D.figlit, labels: () => ['literal', 'figurative'],
  item: x => { const [s, m] = sp(x); return { q: s, a: m ? 'figurative' : 'literal', extra: m ? key(` <span class="gw-fix">Plain words: ${esc(m)}</span>`) : '' }; },
  ican: 'I can tell when words mean exactly what they say and when they do not.',
  dir: () => 'Write literal or figurative for each sentence. Then rewrite three figurative ones in plain words.',
  ex: () => ['My feet are killing me. &nbsp; <b>figurative</b> &rarr; My feet hurt a lot.'],
  part: 'Literal or figurative?', turnName: 'Say it plainly', turn: () => 'Choose three figurative sentences. Rewrite each one in plain words.', turnLines: 5,
  mis: 'Calling a sentence figurative because it is descriptive; ask "could this really happen exactly as written?"',
  notes: 'The key gives plain-word versions of each figurative sentence.' })));

add('pov', 'Style: first or third person', 3, 6, () => [4, 6, 8], {
  title: 'First or Third Person?',
  make({ r, N }) {
    const items = pickN(r, D.pov, N).map(x => { const [f, t] = sp(x); const first = r.chance(0.5);
      return { q: first ? f : t, a: first ? 'first person' : 'third person', other: first ? t : f }; });
    return { ican: 'I can tell whether a narrator is a character (first person) or someone outside the story (third person).',
      directions: 'Read each passage. Write first person or third person. Then rewrite two passages from the other point of view.',
      parts: [part('', example('I opened the gate. &nbsp; <b>first person</b> (I, me, my, we)', 'She opened the gate. &nbsp; <b>third person</b> (he, she, they, a name)')),
        part('Name the point of view', fill(items.map(it => `<span class="gw-pass">${esc(it.q)}</span> ${blank(it.a, 7)}${keyline('Other point of view: ' + esc(it.other))}`))),
        turn('Switch it', 'Choose two passages. Rewrite each one from the other point of view.', 6)],
      items, mistakes: 'Calling a passage first person because a character speaks in it; look at who tells the story.',
      notes: 'The key shows each passage rewritten from the other point of view.' };
  },
  verify(it) { const firstWords = /\b(I|me|my|we|us|our)\b/;
    if (firstWords.test(it.q) !== (it.a === 'first person')) return `${it.q}: pronoun rule`;
    return firstWords.test(it.other) === (it.a === 'first person') ? `${it.q}: other version` : ''; },
});

const rewriteSkill = (o) => ({
  make({ g, r, N }) {
    const items = pickN(r, o.pool(g), N).map(x => o.item(x, g, r));
    return { ican: o.ican, directions: o.dir, parts: [part('', example(...o.ex)),
      part(o.part, fill(items.map(it => editRow(it.q, it.a, o.lines || 1, it.hint || ''))))], items, mistakes: o.mis, notes: o.notes };
  },
});

add('voice', 'Grammar: active and passive voice', 5, 12, () => [6, 8, 10], Object.assign({ title: 'Active and Passive Voice',
  verify(it) { const x = D.voice.map(sp).find(e => e[0] === it.q || e[1] === it.q);
    if (!x || (it.dir === 'p' ? x[0] !== it.q || x[1] !== it.a : x[1] !== it.q || x[0] !== it.a)) return `${it.q}: pair`;
    const pas = it.dir === 'p' ? it.a : it.q;
    return /\b(is|are|was|were|be|been)\b \w+ .*\bby\b|\bby\b/.test(pas) && / by /.test(pas) ? '' : `${it.q}: passive needs a form of be and by`; } }, rewriteSkill({
  pool: () => D.voice,
  item: (x, g, r) => { const [a, p] = sp(x); const toP = g < 7 || r.chance(0.6);
    return { q: toP ? a : p, a: toP ? p : a, dir: toP ? 'p' : 'a', hint: ` <span class="gw-opts">(${toP ? 'make it passive' : 'make it active'})</span>` }; },
  ican: 'I can change sentences between active and passive voice and tell when each works better.',
  dir: 'Rewrite each sentence in the voice shown. Keep the meaning and the tense.',
  ex: ['The cat chased the mouse. &rarr; The mouse was chased by the cat.', 'Active: the doer comes first. Passive: the receiver comes first, with a form of be and often by.'],
  part: 'Switch the voice', mis: 'Changing the tense (chased becomes is chased) and dropping the doer by accident.',
  notes: 'Passive voice works when the doer is unknown or less important than what happened (The colony was founded in 1607). Ask students to say which version they like better and why.' })));

add('parallel', 'Style: parallel structure', 8, 12, () => [6, 9, 12], Object.assign({ title: 'Parallel Structure',
  verify(it) { const x = D.parallel.map(sp).find(e => e[0] === it.q); return x && x[1] === it.a && x[0] !== x[1] ? '' : `${it.q}: pair`; } }, rewriteSkill({
  pool: () => D.parallel, item: x => { const [f, k] = sp(x); return { q: f, a: k }; },
  ican: 'I can revise sentences so items in a list or comparison have the same grammatical form.',
  dir: 'Each sentence mixes forms in a list or comparison. Rewrite it so the parts match.',
  ex: ['She likes reading, drawing, and to swim. &rarr; She likes reading, drawing, and swimming.'],
  part: 'Fix the parallelism', mis: 'Fixing one item but leaving another unmatched, and changing the meaning.',
  notes: 'The key shows one parallel version; any version with matching forms and the same meaning is correct.' })));

add('concise', 'Style: cut the wordiness', 6, 12, () => [6, 8, 10], Object.assign({ title: 'Cut the Wordiness',
  verify(it) { const x = D.concise.map(sp).find(e => e[0] === it.q); return x && x[1] === it.a && x[1].split(' ').length < x[0].split(' ').length ? '' : `${it.q}: model is not shorter`; } }, rewriteSkill({
  pool: () => D.concise, item: x => { const [w, c] = sp(x); return { q: w, a: c }; },
  ican: 'I can cut extra and repeated words without losing the meaning.',
  dir: 'Rewrite each sentence with fewer words. Keep the meaning.',
  ex: ['He nodded his head in agreement. &rarr; He nodded.'],
  part: 'Make it concise', mis: 'Cutting words that carry meaning (dates, names, the cause).',
  notes: 'The key shows one concise version; others that keep the meaning in fewer words are fine.' })));

add('caps', 'Mechanics: capitals and end marks', 1, 3, () => [6, 8, 10], Object.assign({ title: 'Capitals and End Marks',
  verify(it) { return capsShown(it.a) === it.q && /^[A-Z]/.test(it.a) && /[.?!]$/.test(it.a) && !/\bi\b/.test(it.a) ? '' : `${it.q}: shown form`; } }, rewriteSkill({
  pool: () => D.caps, item: x => ({ q: capsShown(x), a: x }), lines: 1,
  ican: 'I can start a sentence with a capital, capitalize names and I, and end with the right mark.',
  dir: 'Write each sentence correctly. Use capital letters and an end mark (. ? or !).',
  ex: ['my cat is named tom &rarr; My cat is named Tom.'],
  part: 'Fix the sentences', mis: 'Forgetting capitals on names, days, months and the word I.',
  notes: 'Every sentence is printed in lower case with no end mark.' })));

add('quotes', 'Mechanics: quotation marks in dialogue', 3, 5, () => [6, 8, 10], Object.assign({ title: 'Quotation Marks in Dialogue',
  verify(it) { return quoteShown(it.a) === it.q && (it.a.match(/"/g) || []).length === 2 ? '' : `${it.q}: shown form`; } }, rewriteSkill({
  pool: () => D.quotes, item: x => ({ q: quoteShown(x), a: x }),
  ican: 'I can punctuate dialogue with quotation marks, commas and capitals.',
  dir: 'Rewrite each line of dialogue. Add quotation marks around the spoken words, a comma where it belongs, and a capital at the start of the quotation.',
  ex: ['Sam said let\'s go &rarr; Sam said, "Let\'s go."', '"I am hungry," said Ana.'],
  part: 'Punctuate the dialogue', mis: 'Putting the comma or end mark outside the quotation marks, and no capital at the start of the quotation.',
  notes: 'End marks are left in place; students add quotation marks, commas and capitals. Follow up with two new lines of dialogue on the back.' })));

add('commas', 'Mechanics: commas', 3, 8, g => g <= 5 ? [8, 10, 12] : [10, 12, 15], {
  title: 'Commas',
  make({ g, r, N, v }) {
    const kinds = COMMA_KINDS.filter(k => k[2] <= g).map(k => k[0]);
    const want = v.focus !== 'all' && kinds.includes(v.focus) ? [v.focus] : kinds;
    const pool = D.commas.map(sp).filter(([, k]) => want.includes(commaKind(k)));
    const items = pickN(r, pool, N).map(([a, k]) => ({ q: a.replace(/,/g, ''), a, kind: k }));
    return { ican: 'I can add commas where they belong.',
      directions: 'Add the missing commas. Write them right in each sentence.',
      parts: [part('', example('We need eggs milk and bread. &rarr; We need eggs, milk, and bread.')),
        part('Add the commas', fill(items.map(it => `<span class="gw-edit gw-wide">${esc(it.q)}</span>${keyline(esc(it.a))}`)))],
      items, mistakes: 'A comma between a subject and its verb, and missing the comma before and in a compound sentence.',
      notes: 'The key uses the serial (Oxford) comma before and in a series; some styles leave it out. ' + (want.length === 1 ? `This sheet practices one kind: ${COMMA_KINDS.find(k => k[0] === want[0])[1].toLowerCase()}.` : 'Kinds at this grade: ' + COMMA_KINDS.filter(k => kinds.includes(k[0])).map(k => k[1].toLowerCase()).join('; ') + '.') };
  },
  verify(it) { const x = D.commas.map(sp).find(e => e[0] === it.a); return x && it.a.replace(/,/g, '') === it.q && it.a.includes(',') ? '' : `${it.q}: shown form`; },
});

add('titles', 'Mechanics: titles', 4, 6, nStd, {
  title: 'Titles: Underline or Quotation Marks?',
  make({ r, N }) {
    const items = pickN(r, D.titles, N).map(x => { const [s, k] = sp(x); const t = s.match(/\{(.+?)\}/)[1]; const long = LONGW.has(k);
      return { q: s.replace(/[{}]/g, ''), a: long ? 'U' : 'Q', kind: k, title: t,
        fixed: esc(s).replace(/\{(.+?)\}/, long ? '<u>$1</u>' : '"$1"') }; });
    return { ican: 'I can mark titles: underline (or italics) for long works and quotation marks for short ones.',
      directions: 'Underline the title or put quotation marks around it. Then write U (underlined) or Q (quotation marks) on the line.',
      parts: [part('', example('We read the poem "Snow Day." &nbsp; <b>Q</b>', 'Underline (italics when typing): books, movies, magazines, newspapers, plays, albums, TV shows. Quotation marks: poems, songs, short stories, articles, chapters, episodes.')),
        part('Mark the titles', fill(items.map(it => `${esc(it.q)} ${blank(it.a, 2.4)}${keyline(it.fixed)}`)))],
      items, mistakes: 'Quotation marks around book titles, and underlining a chapter or poem.',
      notes: 'All titles are made up for practice. Sentences name the kind of work so the rule can be applied.' };
  },
  verify(it) { const x = D.titles.map(sp).find(e => e[0].replace(/[{}]/g, '') === it.q); return x && x[1] === it.kind && (LONGW.has(it.kind) ? 'U' : 'Q') === it.a ? '' : `${it.q}: rule`; },
});

add('coord', 'Mechanics: commas with coordinate adjectives', 7, 9, () => [8, 10, 12], {
  title: 'Coordinate Adjectives: Comma or No Comma?',
  make({ r, N }) {
    const items = pickN(r, D.coord.filter(x => x !== 'big|brown|dog'), N).map(x => { const [a, b, n] = sp(x); const c = coordOf(a, b);
      return { q: `${ADJK[a] === 'number' ? '' : article(a) + ' '}${a} ${b} ${n}`, a: c ? `${a}, ${b}` : 'no comma', a1: a, a2: b }; });
    return { ican: 'I can use a comma between coordinate adjectives and leave it out between cumulative ones.',
      directions: 'Read each phrase. If the adjectives are coordinate, write them with a comma. If not, write no comma. Use the and test: if "cold and dark" and "dark cold" both sound right, use a comma.',
      parts: [part('', example('a long hot summer &rarr; <b>long, hot</b> (long and hot works)', 'a big brown dog &rarr; <b>no comma</b> (big and brown dog sounds wrong)')),
        part('Comma or no comma?', fill(items.map(it => `${esc(it.q)} &nbsp; ${blank(it.a, 8)}`), 2)),
        turn('Your turn', 'Write two sentences with coordinate adjectives and one with cumulative adjectives.', 4)],
      items, mistakes: 'A comma between a number, size, age or color word and the next adjective.',
      notes: 'Coordinate adjectives each describe the noun on their own; cumulative adjectives build on each other (old wooden bridge).' };
  },
  verify(it) { if (!(it.a1 in ADJK) || !(it.a2 in ADJK)) return `${it.q}: adjective kind missing`;
    return (coordOf(it.a1, it.a2) ? `${it.a1}, ${it.a2}` : 'no comma') === it.a ? '' : `${it.q}: rule`; },
});

add('semi', 'Mechanics: semicolon or colon', 8, 12, () => [8, 10, 12], {
  title: 'Semicolon or Colon?',
  make({ r, N }) {
    const items = pickN(r, D.semi, N).map(x => { const [L, R, w] = sp(x); return { q: `${L} [ ] ${R}`, a: `${SEMI[w][0]} ${SEMI[w][1]}`, L, R, why: w }; });
    return { ican: 'I can choose a semicolon or a colon and explain why.',
      directions: 'Write a semicolon (;) or a colon (:) in each box. Then write the letter of the reason from the box.',
      parts: [part('', example('I have two pets<span class="gw-box">:</span> a dog and a cat. &nbsp; <b>: D</b>')),
        part('Reasons', `<ol class="gw-reasons">${REASONS.map(([l, t]) => `<li><b>${l}.</b> ${t}</li>`).join('')}</ol>`),
        part('Add the mark and the reason', fill(items.map(it => `${esc(it.L)}<span class="gw-box"><span class="ws-ans">${SEMI[it.why][0]}</span></span> ${esc(it.R)} &nbsp; Reason: ${blank(SEMI[it.why][1], 2.4)}`)))],
      items, mistakes: 'A colon after a verb or preposition (The recipe needs: flour), and a comma alone between two sentences.',
      notes: 'What comes before a colon is always a complete sentence.' };
  },
  verify(it) { const x = D.semi.map(sp).find(e => e[0] === it.L && e[1] === it.R); if (!x) return `${it.q}: bank`;
    const [m, l] = SEMI[x[2]];
    if (it.a !== `${m} ${l}`) return `${it.q}: mark`;
    if (x[2] === 'ca' && !CADV.has(it.R.split(/[ ,]/)[0].toLowerCase())) return `${it.q}: no transition word`;
    return ''; },
});

add('hyphen', 'Mechanics: hyphens in compound modifiers', 9, 12, () => [10, 12, 15], {
  title: 'Hyphens in Compound Modifiers',
  make({ r, N }) {
    const items = pickN(r, D.hyphen, N).map(x => { const [s, p] = sp(x); const m = s.match(/\[(.+?)\]/)[1];
      return { q: s.replace(/[[\]]/g, ''), a: hyphOf(m, p), m, pos: p, html: esc(s).replace(/\[(.+?)\]/, '<u class="gw-u">$1</u>') }; });
    return { ican: 'I can hyphenate compound modifiers before a noun and leave them open after it.',
      directions: 'Look at the underlined words. Write them with hyphens if they need them, or write no hyphen.',
      parts: [part('', example('a <u class="gw-u">well known</u> song &rarr; <b>well-known</b>', 'The song is <u class="gw-u">well known</u>. &rarr; <b>no hyphen</b>', 'Words ending in -ly (a brightly lit room) never take a hyphen.')),
        part('Hyphen or not?', fill(items.map(it => `${it.html} ${blank(it.a, 7)}`))),
        turn('Fix the paragraph', 'Rewrite with correct hyphens: "Our two week trip had a last minute change, but the well planned tour was up to date and our guide was well known."', 3)],
      items, mistakes: 'Hyphenating after the noun (the author is well-known) and after -ly words.',
      notes: 'Paragraph key: Our two-week trip had a last-minute change, but the well-planned tour was up to date and our guide was well known.' };
  },
  verify(it) { const x = D.hyphen.map(sp).find(e => e[0].replace(/[[\]]/g, '') === it.q); if (!x) return `${it.q}: bank`;
    const want = x[1] === 'b' && !/ly$/.test(it.m.split(' ')[0]) ? it.m.split(' ').join('-') : 'no hyphen';
    return want === it.a ? '' : `${it.q}: ${it.a} should be ${want}`; },
});

add('endmark', 'Mechanics: end marks', 1, 2, () => [8, 10, 12], {
  title: 'End Marks',
  make({ r, N }) {
    const items = pickN(r, D.endmark, N).map(s => ({ q: s, a: endOf(s) }));
    return { ican: 'I can end a sentence with a period, a question mark or an exclamation point.',
      directions: 'Read each sentence. Write the end mark: a period (.) for telling, a question mark (?) for asking, or an exclamation point (!) for a strong feeling.',
      parts: [part('', example('Where is the cat<b>?</b> &nbsp; It is asking.')),
        part('Add the end mark', `<div class="gw-big">${fill(items.map(it => `${esc(it.q)}${blank(it.a, 1.8)}`))}</div>`),
        turn('Your turn', 'Write one asking sentence about the zoo. End it with a question mark.', 2)],
      items, mistakes: 'A period after a question that starts with is, can or do.', notes: 'Questions start with a question word or a helping verb; exclamations start with a feeling word like wow or ouch.' };
  },
  verify(it) { return D.endmark.includes(it.q) && it.a === (QW.test(it.q) ? '?' : EXW.test(it.q) ? '!' : '.') ? '' : `${it.q}: end mark`; },
});

add('contract', 'Mechanics: contractions', 1, 4, () => [8, 10, 12], {
  title: 'Contractions',
  make({ g, r, N }) {
    const pool = D.contract1.concat(g >= 3 ? D.contract2 : []).filter(p => p !== 'do not');
    const items = pickN(r, pool, N).map(p => ({ q: p, a: contractOf(p) }));
    return { ican: 'I can make a contraction by joining two words and using an apostrophe for the missing letters.',
      directions: 'Write the contraction for each pair of words. The apostrophe goes where letters are left out.',
      parts: [part('', example('do not &rarr; <b>don\'t</b> (the o in not is left out)')),
        part('Make the contractions', `<div class="${g <= 2 ? 'gw-big' : ''}">${fill(items.map(it => `${esc(it.q)} &rarr; ${blank(it.a, 5)}`), 2)}</div>`),
        turn('Your turn', 'Write a sentence that uses one of your contractions.', 2)],
      items, mistakes: 'Putting the apostrophe where the words join (do\'nt) instead of where letters are missing.',
      notes: 'Will not becomes won\'t, a special case. Cannot becomes can\'t.' };
  },
  verify(it) { return expandOf(it.a) === it.q ? '' : `${it.q}: ${it.a} reads back as ${expandOf(it.a)}`; },
});

add('poss', 'Mechanics: possessives', 2, 6, nStd, {
  title: 'Possessive Nouns',
  make({ g, r, N }) {
    const pool = D.poss.map(sp).filter(x => g >= 3 || x[1] === '0');
    const items = pickN(r, pool, N).map(([o, pl, t]) => ({ q: `the ${t} of the ${o}`, a: `the ${o}${pl === '1' && /s$/.test(o) ? '\'' : '\'s'} ${t}`, o, pl }));
    return { ican: 'I can write possessive nouns for one owner and for more than one owner.',
      directions: 'Rewrite each phrase with a possessive noun.',
      parts: [part('', example('the tail of the dog &rarr; <b>the dog\'s tail</b>', 'the tails of the dogs &rarr; <b>the dogs\' tails</b>', 'One owner: add \'s. More than one owner ending in s: add only \'. Plurals like children: add \'s.')),
        part('Show who owns it', fill(items.map(it => `${esc(it.q)} &rarr; ${blank(it.a, 10)}`)))],
      items, mistakes: 'Adding an apostrophe to a plain plural (the dog\'s ran), and childrens\'.', notes: g >= 3 ? 'Mixes singular, plural and irregular plural owners.' : 'Singular owners only at grade 2.' };
  },
  verify(it) { const x = D.poss.map(sp).find(e => it.q === `the ${e[2]} of the ${e[0]}`); if (!x) return `${it.q}: bank`;
    const own = it.a.split(' ')[1];
    if (own.replace(/'s?$/, '') !== x[0]) return `${it.q}: owner`;
    return (x[1] === '1' && /s$/.test(x[0])) === own.endsWith('s\'') && !(x[1] === '1' && /s$/.test(x[0]) && own.endsWith('\'s')) ? '' : `${it.q}: apostrophe`; },
});

/* word study */
add('pattern', 'Spelling: pattern sort', 1, 3, () => [9, 12, 15], {
  title: 'Spelling Pattern Sort',
  make({ g, r, N, v }) {
    const groups = Object.keys(D.patterns).filter(k => PAT_GRADE[k] <= g);
    const gk = groups.includes(v.focus) ? v.focus : r.pick(groups);
    const cats = r.sample(D.patterns[gk], Math.min(3, D.patterns[gk].length));
    const per = Math.floor(N / cats.length);
    const picks = cats.map(c => r.sample(ws(c[2]), per));
    const items = r.shuffle(cats.flatMap((c, i) => picks[i].map(w => ({ q: `sort: ${w}`, a: c[0], word: w, re: c[1], others: cats.filter(o => o !== c).map(o => o[1]) }))));
    const spare = cats.map((c, i) => ws(c[2]).filter(w => !picks[i].includes(w)));
    const rows = Array.from({ length: per }, (_, i) => cats.map((c, j) => blank(picks[j][i], 5)));
    return { ican: 'I can sort words by their spelling pattern and spell new words that follow it.',
      directions: 'Read each word in the box. Write it under the pattern it follows.',
      parts: [part('', example(`Word: <b>${esc(spare[0][0] || picks[0][0])}</b> goes under <b>${esc(cats[0][0])}</b>.`)),
        part('Sort the words', `<div class="gw-big">${bankBox(items.map(it => it.word))}</div>` + table(cats.map(c => esc(c[0])), rows)),
        part('Spell new words', `<p class="ws-text">Write one more word for each pattern.</p>` + fill(cats.map((c, i) => `${esc(c[0])}: ${blank(spare[i].length ? spare[i][0] : '', 6)}`)))],
      items, mistakes: 'Sorting by the first letter instead of the pattern.', notes: `Pattern set: ${PAT_LAB[gk]}. The new-word answers on the key are examples; any real word with the pattern is right.` };
  },
  verify(it) { if (!new RegExp(it.re).test(it.word)) return `${it.word}: does not match ${it.a}`; return it.others.some(o => new RegExp(o).test(it.word)) ? `${it.word}: matches two patterns` : ''; },
});

add('rootword', 'Word study: root words and endings', 1, 2, () => [4, 6, 8], {
  title: 'Root Words and Endings',
  make({ g, r, N }) {
    const pool = ws(D.rootword1).concat(g >= 2 ? ws(D.rootword2) : []).filter(b => b !== 'look');
    const items = pickN(r, pool, N).map(b => ({ q: `${V[b].ing}, ${V[b].past}`, a: `${b}, ${V[b].s}`, base: b, s: V[b].s, ing: V[b].ing, past: V[b].past }));
    return { ican: 'I can find the root word in words with endings and add endings to a root word.',
      directions: 'Read the two words. Write the root word in the trunk. Then add -s to the root word.',
      parts: [part('', example('looking, looked &rarr; root: <b>look</b> &rarr; add -s: <b>looks</b>')),
        part('Find the root', table(['Words', 'Root word (trunk)', 'Add -s (branch)'], items.map(it => [esc(it.q), blank(it.base, 5), blank(it.s, 5)])))],
      items, mistakes: g >= 2 ? 'Keeping a doubled letter or adding back an e that is not in the root (hopp, smil).' : 'Writing the word with its ending as the root.',
      notes: g >= 2 ? 'Grade 2 includes roots that change spelling (hopping, baked, cried).' : 'Grade 1 roots keep their spelling.' };
  },
  verify(it) { const v = V[it.base]; if (!v) return `${it.base}: bank`;
    return it.ing === addSuf(it.base, 'ing', v.S) && it.past === addSuf(it.base, 'ed', v.S) && it.s === sOf(it.base) ? '' : `${it.base}: an ending breaks the rule`; },
});

add('compound', 'Word study: compound words', 1, 3, g => g <= 2 ? [6, 8, 10] : [8, 10, 12], {
  title: 'Compound Words',
  make({ g, r, N }) {
    const all = r.shuffle(D.compound.split('|').map(x => ws(x)));
    const pick = [];
    for (const p of all) { if (pick.length >= N) break;
      if (pick.some(q => q[0] === p[0] || q[1] === p[1] || COMPOUNDS.has(q[0] + p[1]) || COMPOUNDS.has(p[0] + q[1]))) continue; pick.push(p); }
    const items = pick.map(([a, b]) => ({ q: `${a} + ?`, a: a + b, first: a, second: b, all: pick }));
    return { ican: 'I can put two small words together to make a compound word.',
      directions: 'Find the word in the box that goes with each word. Write the compound word. Use each box word once.',
      parts: [part('', example('rain + drop = <b>raindrop</b>')),
        part('Make compound words', `<div class="${g <= 2 ? 'gw-big' : ''}">${bankBox(r.shuffle(pick.map(p => p[1])))}${fill(items.map(it => `${esc(it.first)} + ____ = ${blank(it.a, 7)}`), 2)}</div>`),
        part('Draw it', `<p class="ws-text">Choose two compound words. Draw what each one means and write the word.</p><div class="gw-draws"><div class="ws-draw"><span>Word:</span></div><div class="ws-draw"><span>Word:</span></div></div>`)],
      items, mistakes: 'Joining words that make a real word but not one from the box pairs; each box word is used once.',
      notes: 'The sheet never offers two pairs that could swap halves (sun with set and rain with bow, but not sun with shine and moon with light at once).' };
  },
  verify(it) {
    if (it.a !== it.first + it.second || !COMPOUNDS.has(it.a)) return `${it.q}: not a bank compound`;
    return it.all.some(p => p[1] !== it.second && COMPOUNDS.has(it.first + p[1])) ? `${it.q}: two answers fit` : '';
  },
});

add('affix', 'Word study: prefixes and suffixes', 2, 6, g => g <= 2 ? [6, 8, 10] : [8, 10, 12], {
  title: 'Prefixes and Suffixes',
  make({ g, r, N }) {
    const okA = new Set(D.prefixes.split(',').concat(D.suffixes.split(',')).map(sp).filter(x => +x[2] <= g).map(x => x[0]));
    const items = pickN(r, D.affix.map(sp).filter(x => okA.has(x[1]) && x[2] !== 'unkind' && x[2] !== 'happiness'), N).map(([b, a, w, m]) => ({ q: `${b} + ${a}`, a: `${w}: ${m}`, base: b, affix: a, word: w, mean: m,
      pre: D.prefixes.split(',').some(x => sp(x)[0] === a) }));
    const affs = [...new Set(items.map(it => it.affix))].map(a => { const x = D.prefixes.split(',').concat(D.suffixes.split(',')).map(sp).find(y => y[0] === a);
      return `${D.prefixes.includes(a + '|') && D.prefixes.split(',').some(y => sp(y)[0] === a) ? a + '-' : '-' + a} = ${x[1]}`; });
    return { ican: 'I can add a prefix or suffix to a base word and tell what the new word means.',
      directions: 'Add the prefix or suffix to the base word. Write the new word and what it means. Watch for spelling changes.',
      parts: [part('', example('un- + kind = <b>unkind</b>: not kind', 'happy + -ness = <b>happiness</b>: the state of being happy (y changes to i)')),
        part('Word parts', bankBox(affs)),
        part('Build new words', table(['Base word', 'Add', 'New word', 'Meaning'], items.map(it => [esc(it.base), it.pre ? esc(it.affix) + '-' : '-' + esc(it.affix), blank(it.word, 6), blank(it.mean, 10)]))),
        turn('Your turn', `Use ${g <= 2 ? 'two' : 'three'} of your new words in sentences.`, g <= 2 ? 3 : 4)],
      items, mistakes: 'Missing the spelling changes: y to i (happiness), dropping e (usable), doubling (runner).', notes: 'Meanings on the key are short definitions; a student\'s own clear wording is fine.' };
  },
  verify(it) { const want = it.pre ? it.affix + it.base : addSuf(it.base, it.affix);
    return want === it.word ? '' : `${it.q}: ${it.word} should be ${want}`; },
});

add('sufspell', 'Spelling: suffix rules', 5, 8, () => [10, 12, 15], {
  title: 'Suffix Spelling Rules',
  make({ r, N }) {
    const rule = (b, suf, w) => w === b + suf ? 'just add' : /[^aeiou]y$/.test(b) ? 'change y to i' : w.length === b.length + suf.length + 1 ? 'double the consonant' : 'drop the e';
    const items = pickN(r, D.sufspell.map(sp), N).map(([b, s, w, S]) => ({ q: `${b} + ${s}`, a: `${w} (${rule(b, s, w)})`, base: b, suf: s, word: w, S, rule: rule(b, s, w) }));
    return { ican: 'I can spell words with suffixes by applying the drop e, double, change y and just-add rules.',
      directions: 'Add the suffix. Write the new word and the rule you used: drop the e, double the consonant, change y to i, or just add.',
      parts: [part('', example('make + ing = <b>making</b> (drop the e)', 'Drop a silent e before a vowel suffix. Double a final consonant after one short vowel in a stressed syllable. Change y to i after a consonant, unless the suffix starts with i.')),
        part('Add the suffix', table(['Word + suffix', 'New word', 'Rule'], items.map(it => [esc(it.q), blank(it.word, 7), blank(it.rule, 9)])))],
      items, mistakes: 'Doubling after two vowels (greetting) or in an unstressed syllable (visitted), and changing y before -ing (studiing).',
      notes: 'Includes stressed two-syllable words that double (beginning, occurred) next to ones that do not (visited, opening).' };
  },
  verify(it) { const want = addSuf(it.base, it.suf, it.S); return want === it.word ? '' : `${it.q}: ${it.word} should be ${want}`; },
});

add('roots', 'Word study: Greek and Latin roots', 4, 12, g => g <= 5 ? [6, 8, 10] : g <= 8 ? [8, 10, 12] : [10, 12, 15], {
  title: 'Greek and Latin Roots',
  make({ g, r, N, v }) {
    const sets = ROOT_SETS.filter(s => s[2] <= g).map(s => s[0]);
    const use = sets.includes(v.focus) ? [v.focus] : sets.filter(s => s !== 'med');
    const seen = new Set();
    const pool = use.flatMap(s => D.roots[s]).map(sp).filter(x => x[0] !== 'telephone' && !seen.has(x[0]) && seen.add(x[0]));
    const items = pickN(r, pool, N).map(([w, p, m]) => ({ q: w, a: `${p.split('+').map(x => `${bare(x)} (${PARTS[x].m})`).join(' + ')}: ${m}`, parts: p.split('+'), mean: m }));
    const box = [...new Set(items.flatMap(it => it.parts).filter(x => PARTS[x].k !== 'o'))].sort((a, b) => bare(a).localeCompare(bare(b)))
      .map(x => `${PARTS[x].k === 'p' ? bare(x) + '-' : PARTS[x].k === 's' ? '-' + bare(x) : bare(x)} = ${PARTS[x].m}`);
    const show = v.hint !== false;
    return { ican: 'I can use Greek and Latin roots and affixes to figure out what a word means.',
      directions: `Split each word into its parts and write what each part means${show ? ' (use the box)' : ''}. Then write what the whole word means.`,
      parts: [part('', example('<b>telephone</b> &rarr; tele (far) + phone (sound): a device that carries sound far away')),
        ...(show ? [part('Word parts', `<div class="gen-wordbank gw-parts">${box.map(b => `<span>${esc(b)}</span>`).join('')}</div>`)] : []),
        part('Break the words apart', table(['Word', 'Parts and their meanings', 'Meaning of the word'], items.map(it => [`<b>${esc(it.q)}</b>`,
          blank(it.parts.map(x => `${bare(x)} (${PARTS[x].m})`).join(' + '), 10), blank(it.mean, 10)]))),
        turn('Make a word', 'Invent a new word from two parts in the box. Write it and what it would mean.', 2)],
      items, mistakes: 'Guessing from the whole word instead of the parts, and mixing up look-alike roots (dict and diet).',
      notes: `Sets: ${(use.length === 1 ? ROOT_SETS.filter(s => s[0] === use[0]) : ROOT_SETS.filter(s => use.includes(s[0]))).map(s => s[1]).join('; ')}. A connecting letter (the o in thermometer) has no meaning of its own. Check meanings against a dictionary as a follow-up.` };
  },
  verify(it) { if (it.parts.map(bare).join('') !== it.q) return `${it.q}: parts spell ${it.parts.map(bare).join('')}`;
    const bad = it.parts.find(x => !PARTS[x]); return bad ? `${it.q}: part ${bad} not in the table` : ''; },
});

add('synant', 'Word study: synonyms and antonyms', 1, 6, nStd, {
  title: 'Synonyms and Antonyms',
  make({ g, r, N }) {
    const pool = D.synant.map(sp).filter(x => +x[3] <= g);
    const items = pickN(r, pool, N).map(([w, s, a, , grp], i) => {
      const syn = r.chance(0.5), right = syn ? s : a, wrong = syn ? a : s;
      const other = r.pick(pool.filter(x => x[4] !== grp && x[0] !== w));
      const third = r.pick([other[1], other[2]]);
      return { q: `${syn ? 'synonym' : 'antonym'} of ${w}`, a: right, word: w, syn, o: r.shuffle([right, wrong, third]) };
    });
    return { ican: 'I can find a word that means the same (synonym) or the opposite (antonym).',
      directions: 'Read the word. Write the synonym or antonym from the choices.',
      parts: [part('', example('An antonym of <b>up</b> is <b>down</b>. (high / down / blue)', 'Synonym: same meaning. Antonym: opposite meaning.')),
        part('Same or opposite', `<div class="${g <= 2 ? 'gw-big' : ''}">${fill(items.map(it => `A${it.syn ? ' synonym' : 'n antonym'} of <b>${esc(it.word)}</b> is ${blank(it.a, 6)}${opts(it.o)}`))}</div>`),
        turn('Your turn', 'Pick one word. Write a sentence with its synonym and a sentence with its antonym.', 3)],
      items, mistakes: 'Choosing the antonym when the line asks for a synonym; circle the word synonym or antonym first.', notes: 'Each line has one synonym or antonym and one unrelated word, so exactly one choice fits.' };
  },
  verify(it) { const x = D.synant.map(sp).find(e => e[0] === it.word); if (!x) return `${it.word}: bank`;
    if ((it.syn ? x[1] : x[2]) !== it.a) return `${it.q}: answer`;
    const wrongFit = it.o.filter(o => o !== it.a && o === (it.syn ? x[1] : x[2]));
    return wrongFit.length || it.o.filter(o => o === it.a).length !== 1 ? `${it.q}: options` : ''; },
});

const orderSkill = (o) => ({
  make({ g, r, N }) {
    const sets = pickN(r, o.pool(g), N);
    const items = sets.map(x => { const s = o.parse(x); let sh = r.shuffle(s.words); if (sh.join() === s.words.join()) sh = sh.slice(1).concat(sh[0]); return Object.assign(s, { q: s.words.join(' '), a: s.words.join(', '), sh }); });
    const ladder = it => `<div class="gw-ladder">${bankBox(it.sh)}<p><span class="gw-end">${esc(it.lo)}</span> ${it.words.map(w => blank(w, W(it.words))).join(' &rarr; ')} <span class="gw-end">${esc(it.hi)}</span></p></div>`;
    return { ican: o.ican, directions: o.dir, parts: [part('', example(o.ex)), part(o.part, fill(items.map(ladder))), turn('Your turn', o.turn, 3)], items, mistakes: o.mis, notes: o.notes };
  },
});
add('shades', 'Word study: shades of meaning', 2, 8, g => g <= 2 ? [4, 5, 6] : [5, 6, 8], Object.assign({ title: 'Shades of Meaning',
  verify(it) { const x = D.shades.map(sp).find(e => e[3] === it.q); return x && it.sh.slice().sort().join() === it.words.slice().sort().join() && it.sh.join() !== it.words.join() ? '' : `${it.q}: set`; } }, orderSkill({
  pool: g => D.shades.filter(x => +sp(x)[0] <= g), parse: x => { const [, lo, hi, w] = sp(x); return { lo, hi, words: ws(w) }; },
  ican: 'I can order words with close meanings from weakest to strongest.', dir: 'Write the words from the box in order on each paint strip, from the label on the left to the label on the right.',
  ex: 'warm &rarr; hot &rarr; <b>scorching</b> (least hot to hottest)', part: 'Paint strips', turn: 'Choose one strip. Write a sentence that uses its strongest word.',
  mis: 'Ordering by word length or alphabet instead of meaning; say each word in the same sentence to compare.', notes: 'Some strips are close calls. Accept a different order if the student can explain it.' })));
add('connot', 'Word study: connotation', 5, 9, () => [5, 6, 8], Object.assign({ title: 'Connotation',
  verify(it) { const x = D.connot.map(sp).find(e => e.slice(1).join(' ') === it.q); return x && it.sh.join() !== it.words.join() ? '' : `${it.q}: set`; } }, orderSkill({
  pool: g => D.connot.filter(x => +sp(x)[0] <= g), parse: x => { const [, p, n, m] = sp(x); return { lo: 'positive', hi: 'negative', words: [p, n, m] }; },
  ican: 'I can rank words with similar meanings by their feeling, from positive to negative.', dir: 'Each set of words means about the same thing. Write them in order from most positive to most negative.',
  ex: 'slim &rarr; thin &rarr; <b>scrawny</b> (positive to negative)', part: 'Connotation thermometers', turn: 'Choose one set. Write one sentence with the positive word and one with the negative word about the same person or thing.',
  mis: 'Ranking by strength instead of feeling.', notes: 'The middle word is the most neutral of the three.' })));

add('idiom', 'Word study: idioms', 3, 8, g => g <= 5 ? [6, 8, 10] : [8, 10, 12], {
  title: 'Idioms',
  make({ g, r, N }) {
    const pick = [];
    for (const x of r.shuffle(D.idiom.map(sp).filter(x => x[0] !== 'a piece of cake'))) { if (pick.length >= N) break; if (pick.some(p => p[2] === x[2] || p[1] === x[1])) continue; pick.push(x); }
    const LET = 'ABCDEFGHIJKL', mean = r.shuffle(pick.map(p => p[1]));
    const items = pick.map(([i, m]) => ({ q: i, a: LET[mean.indexOf(m)], mean: m, opts: mean }));
    return { ican: 'I can explain what common idioms really mean.',
      directions: 'Write the letter of the real meaning next to each idiom.',
      parts: [part('', example('<b>a piece of cake</b> means very easy, not a real cake.')),
        part('Match each idiom', `<div class="ws-match"><ol>${items.map(it => `<li>${esc(it.q)} ${blank(it.a, 2.4)}</li>`).join('')}</ol><ul>${mean.map((m, i) => `<li><b>${LET[i]}.</b> ${esc(m)}</li>`).join('')}</ul></div>`),
        g <= 6 ? part('Draw it', `<p class="ws-text">Choose two idioms. Draw the funny literal meaning, then write the real meaning under it.</p><div class="gw-draws"><div class="ws-draw"><span>Idiom:</span></div><div class="ws-draw"><span>Idiom:</span></div></div>`)
          : turn('Your turn', 'Write a sentence that uses one idiom so its meaning is clear.', 3)],
      items, mistakes: 'Taking the words literally. English learners may know a different idiom with the same meaning; invite them to share it.', notes: 'No two idioms on a sheet share a meaning.' };
  },
  verify(it) { const x = D.idiom.map(sp).find(e => e[0] === it.q); return x && it.opts['ABCDEFGHIJKL'.indexOf(it.a)] === x[1] ? '' : `${it.q}: letter`; },
});

/* English learners */
add('signal', 'English learners: signal word sort', 2, 8, () => [6, 8, 10], {
  title: 'Signal Word Sort',
  make({ g, r, N, v }) {
    const set = SIG_SETS[v.focus] ? v.focus : (g <= 3 ? 'seq' : 'ce');
    const cats = SIG_SETS[set], per = Math.floor(N / cats.length) || 1;
    const exW = { seq: 'first', cc: 'however', ce: 'because', mix: 'because' }[set];
    const picks = cats.map(([c]) => r.sample(D.signal.map(sp).filter(x => x[1] === c && x[0] !== exW).map(x => x[0]), per));
    const items = r.shuffle(cats.flatMap(([c, lab], i) => picks[i].map(w => ({ q: `signal: ${w}`, a: lab, word: w, cat: c }))));
    const rows = Array.from({ length: Math.max(...picks.map(p => p.length)) }, (_, i) => cats.map((c, j) => picks[j][i] ? blank(picks[j][i], 7) : ''));
    const topic = v.topic.trim();
    return { ican: 'I can sort signal words by what they tell the reader and use them in my own sentences.',
      directions: 'Read each signal word in the box. Write it in the column where it belongs.',
      parts: [part('', example(set === 'seq' ? '<b>first</b> goes under Beginning.' : set === 'cc' ? '<b>however</b> goes under Different (contrast).' : '<b>because</b> tells a cause.')),
        part('Sort the words', bankBox(items.map(it => it.word)) + table(cats.map(c => esc(c[1])), rows)),
        turn('Use them', `Write three sentences${topic ? ` about ${esc(topic)}` : ''}. Use a different signal word in each.`, 5)],
      items, mistakes: set === 'ce' ? 'Mixing up because (comes before the cause) and so (comes before the effect).' : 'Sorting by the first letter instead of the meaning.',
      notes: 'Set: ' + cats.map(c => c[1]).join(', ') + '.' };
  },
  verify(it) { const x = D.signal.map(sp).find(e => e[0] === it.word); return x && x[1] === it.cat ? '' : `${it.word}: category`; },
});

add('phrasal', 'English learners: phrasal verbs', 5, 10, () => [6, 8, 10], {
  title: 'Phrasal Verbs',
  make({ r, N }) {
    const pick = [];
    for (const x of r.shuffle(D.phrasal.map(sp))) { if (pick.length >= N) break; if (pick.some(p => p[3] === x[3])) continue; pick.push(x); }
    const items = pick.map(([b, s, a]) => ({ q: s, a, base: b }));
    return { ican: 'I can use phrasal verbs, a verb plus a small word that together have a new meaning.',
      directions: 'Write the phrasal verb from the box that fits each sentence. Change the verb form if the sentence needs it (give up, gave up).',
      parts: [part('', example('I will <b>look for</b> my keys. (look for = try to find)')),
        part('Fill in the phrasal verb', bankBox(r.shuffle(pick.map(p => p[0]))) + fill(items.map(it => esc(it.q).replace('___', blank(it.a, 7))))),
        turn('Your turn', 'Choose two phrasal verbs from the box. Write a sentence for each.', 3)],
      items, mistakes: 'Leaving off the small word (We ran milk) or using the wrong one (give in for give up).', notes: 'No two phrasal verbs on a sheet fit the same sentence.' };
  },
  verify(it) { const x = D.phrasal.map(sp).find(e => e[1] === it.q); if (!x || x[2] !== it.a) return `${it.q}: answer`;
    const tail = x[0].split(' ').slice(1).join(' '); return it.a.toLowerCase().endsWith(' ' + tail) ? '' : `${it.q}: particle`; },
});

add('nominal', 'English learners: verbs to nouns', 5, 12, g => g <= 8 ? [6, 8, 10] : [4, 6, 8], {
  title: 'Verbs to Nouns',
  make({ g, r, N }) {
    const pairs = D.nominal.split('|').map(ws).filter(p => p[0] !== 'pollute');
    const tN = g <= 8 ? N : 6;
    const items = pickN(r, pairs, tN).map(([vb, n]) => ({ q: vb, a: n, nk: 'w' }));
    const parts = [part('', example('pollute &rarr; <b>pollution</b>: The pollution of the river harmed the fish.')),
      part('Turn the verb into a noun', fill(items.map(it => `${esc(it.q)} &rarr; ${blank(it.a, 7)}`), 2))];
    if (g >= 9) {
      const rw = pickN(r, D.nominalRw, N).map(x => { const [e, a] = sp(x); return { q: e, a, nk: 'r' }; });
      items.push(...rw);
      parts.push(part('Rewrite in academic style', `<p class="ws-text">Rewrite each sentence using a noun made from its verb.</p>` + fill(rw.map(it => editRow(it.q, it.a, 2)), 1, tN + 1)));
    } else parts.push(turn('Your turn', 'Use two of the nouns in formal sentences that tell a cause or an effect.', 3));
    return { ican: 'I can turn verbs into nouns to write in a formal, academic way.',
      directions: g >= 9 ? 'Part 1: write the noun form of each verb. Part 2: rewrite each sentence in academic style with a noun.' : 'Write the noun form of each verb. Then use two in your own sentences.',
      parts, items, mistakes: 'Adding -tion to every verb (analyzation, failtion). Some nouns change more (analysis, choice, loss).',
      notes: g >= 9 ? 'The rewrites on the key are models; other academic versions that use a noun and keep the meaning are fine.' : 'Nominalization lets writers name a process (erosion) and say what it caused.' };
  },
  verify(it) { if (it.nk === 'w') return D.nominal.split('|').includes(`${it.q} ${it.a}`) ? '' : `${it.q}: noun`;
    const x = D.nominalRw.map(sp).find(e => e[0] === it.q); return x && x[1] === it.a ? '' : `${it.q}: model`; },
});

add('frames', 'English learners: sentence frames', 1, 12, () => [4, 5, 6], {
  title: 'Sentence Frames',
  make({ g, r, N, v }) {
    const fn = D.frames[v.focus] ? v.focus : 'describe', lvl = D.frames[fn][v.level] ? v.level : 'e';
    const topic = v.topic.trim();
    const allF = r.shuffle(D.frames[fn][lvl]), frames = allF.slice(0, N), exF = allF[N] || allF[0];
    const em = g <= 2 ? 6 : 8;
    const fr = f => esc(f).split('___').join(`<span class="ws-blank" style="min-width:${em}em"></span>`);
    const items = frames.map(f => ({ q: f, a: 'Answers vary: a complete sentence that keeps the frame and fits the topic.' }));
    const fnLab = FRAME_FN.find(x => x[0] === fn)[1], lvLab = LEVELS.find(x => x[0] === lvl)[1];
    return { title: `Sentence Frames: ${fnLab}`, level2: `${lvLab} level`,
      ican: `I can use sentence frames to ${fnLab.toLowerCase()} in English.`,
      directions: `Topic: ${topic ? '<b>' + esc(topic) + '</b>' : '<span class="ws-blank" style="min-width:14em"></span>'}. Say each sentence to a partner, then write it.`,
      parts: [part('', example(fr(exF), 'Fill every blank with your own words. Read the whole sentence aloud before you write.')),
        part(`${fnLab} (${lvLab.toLowerCase()})`, `<div class="${g <= 2 ? 'gw-big' : ''}">${fill(frames.map(f => fr(f) + (lvl === 'b' || g >= 6 ? lines(1) : '')))}</div>`),
        turn('On my own', 'Write one more sentence about the topic without a frame.', g <= 2 ? 2 : 3)],
      items, mistakes: 'Filling a blank with one word where a phrase is needed, and leaving off the end mark.',
      notes: `Levels follow the emerging, expanding and bridging ELD levels: emerging frames are short and concrete, bridging frames add academic connectors. Pair talk before writing helps every level. Answers vary, so the key shows no answers.` };
  },
  verify(it) { return /___/.test(it.q) ? '' : `${it.q}: frame has no blank`; },
});

/* ---------- the generator ---------- */
const GRADES = Array.from({ length: 12 }, (_, i) => [String(i + 1), `Grade ${i + 1}`]);
const skillsFor = g => Object.values(SK).filter(s => s.lo <= g && g <= s.hi);
const focusOpts = v => {
  const g = +v.grade;
  if (v.skill === 'commas') return [['all', 'All kinds for the grade']].concat(COMMA_KINDS.filter(k => k[2] <= g).map(k => [k[0], k[1]]));
  if (v.skill === 'roots') return [['all', 'Mixed roots for the grade']].concat(ROOT_SETS.filter(s => s[2] <= g).map(s => [s[0], s[1]]));
  if (v.skill === 'pattern') return [['all', 'A different pattern each sheet']].concat(Object.keys(PAT_GRADE).filter(k => PAT_GRADE[k] <= g).map(k => [k, PAT_LAB[k]]));
  if (v.skill === 'signal') return [['all', 'Best for the grade'], ['seq', 'Beginning, middle, end'], ['ce', 'Cause or effect'], ['cc', 'Compare or contrast'], ['mix', 'Cause, effect, contrast, example']];
  if (v.skill === 'frames') return FRAME_FN;
  return [['all', 'All']];
};
const HAS_FOCUS = ['commas', 'roots', 'pattern', 'signal', 'frames'];

Gen.add('grammar-words', {
  title: 'Grammar and Word Study', type: 'Practice',
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '3' },
    { id: 'skill', label: 'Skill', type: 'select', def: 'pos', options: v => skillsFor(+v.grade).map(s => [s.id, s.label]) },
    { id: 'focus', label: 'Focus', type: 'select', def: 'all', options: v => focusOpts(v), show: v => HAS_FOCUS.includes(v.skill) },
    { id: 'level', label: 'English level', type: 'select', def: 'e', options: LEVELS, show: v => v.skill === 'frames' },
    { id: 'count', label: 'Length', type: 'select', def: 'm',
      options: v => { const s = SK[v.skill] || SK.pos, n = s.n(+v.grade); return [['s', `Shorter (${n[0]})`], ['m', `Standard (${n[1]})`], ['l', `Longer (${n[2]})`]]; } },
    { id: 'hint', label: 'Print a word-part box with meanings', type: 'check', def: true, show: v => v.skill === 'roots' },
    { id: 'topic', label: 'Topic (optional, for frames and signal-word sentences)', type: 'text', def: '', show: v => v.skill === 'frames' || v.skill === 'signal' },
  ],
  make(v, r) {
    const g = +v.grade, s = SK[v.skill] && SK[v.skill].lo <= g && g <= SK[v.skill].hi ? SK[v.skill] : skillsFor(g)[0];
    const N = s.n(g)[{ s: 0, m: 1, l: 2 }[v.count] ?? 1];
    const out = s.make({ g, r, N, v });
    out.items.forEach(it => { it.k = s.id; });
    return {
      title: out.title || s.title, level: `Grade ${g}${out.level2 ? ', ' + out.level2 : ''}${out.items.length && !['frames', 'nominal', 'pattern', 'signal'].includes(s.id) && out.items.length < N ? `, ${out.items.length} items (all that fit)` : ''}`,
      ican: out.ican, directions: out.directions, minutes: N > 10 ? 25 : 20, materials: /Draw|draw/.test(JSON.stringify(out.parts.map(p => p[0]))) ? 'pencil, crayons' : 'pencil',
      parts: out.parts, items: out.items, mistakes: out.mistakes, notes: out.notes,
    };
  },
  verify(sheet, v) {
    const out = [], g = +v.grade, s = SK[sheet.items[0] && sheet.items[0].k];
    if (!s) return ['no skill on the items'];
    if (s.lo > g || s.hi < g) out.push(`${s.id} printed at grade ${g}`);
    for (const it of sheet.items) { const p = s.verify(it); if (p) out.push(p); }
    const N = s.n(g)[{ s: 0, m: 1, l: 2 }[v.count] ?? 1];
    if (sheet.items.length > N + (s.id === 'nominal' ? 8 : 0)) out.push(`${sheet.items.length} items, more than ${N}`);
    if (sheet.items.length < Math.min(4, N)) out.push(`only ${sheet.items.length} items`);
    return out;
  },
  css: `.gw-opts { color: #444; font-size: .92em; white-space: nowrap; }
.gw-u { text-decoration: underline; text-decoration-thickness: 2px; font-weight: 700; }
.gw-edit { display: inline; }
.gw-wide { letter-spacing: .04em; word-spacing: .35em; line-height: 2.2; }
.gw-big { font-size: 19px; }
.gw-big .gen-wordbank { font-size: 20px; }
.gw-fix { color: #b03020; font-size: .92em; }
.gw-pass { display: inline; }
.gw-box { display: inline-block; min-width: 1.5em; height: 1.3em; border: 1.5px solid #222; margin: 0 4px; text-align: center; vertical-align: -3px; }
.gw-reasons { list-style: none; padding: 0; margin: 0; font-size: 14px; columns: 1; }
.gw-ladder p { margin: 4px 0 10px; line-height: 2; }
.gw-ladder .gen-wordbank { margin: 2px 0; display: inline-flex; }
.gw-end { font-size: 12.5px; color: #444; font-style: italic; }
.gw-tl { display: flex; justify-content: space-around; border-bottom: 2px solid #222; margin: 0 0 6px 18%; font-weight: 700; font-size: 13px; }
.gw-draws { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.gw-draws .ws-draw { height: 1.4in; }
.gw-parts { font-weight: 500; font-size: 13.5px; }
@media print { .gw-big { font-size: 14pt; } .gw-wide { line-height: 2; } .gw-draws .ws-draw { height: 1.2in; } }`,
});
})();
