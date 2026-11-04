// Punnett Squares generator, grades 7-12.
// Grades 7-8: one trait with complete dominance. Grades 9-12 add incomplete dominance, codominance (roan cattle and ABO
// blood type), sex-linked traits and two-trait (dihybrid) crosses on a 4 x 4 square. Every trait is a real, correctly
// described one: Mendel's pea traits, fruit fly body color, snapdragon flower color, roan shorthorn cattle, ABO blood
// type, red-green color blindness and white eyes in fruit flies. The student fills each square and gives the ratios
// and a probability; the key fills everything in. One-trait sheets can hold 3 to 8 crosses (6 and 8 use a smaller
// square); dihybrid sheets hold 1 or 2.
(() => {
const { part, example, esc } = Gen.h;

const GRADES = [['7', 'Grade 7'], ['8', 'Grade 8'], ['9', 'Grade 9'], ['10', 'Grade 10'], ['11', 'Grade 11'], ['12', 'Grade 12']];
const hs = g => +g >= 9;
const CROSSES = { mono: 'One trait (complete dominance)', incomplete: 'Incomplete dominance', codom: 'Codominance', sex: 'Sex-linked (X-linked) traits', di: 'Two traits (dihybrid, 4 × 4)', mix: 'Mixed review' };
const crossesFor = g => hs(g) ? Object.keys(CROSSES) : ['mono'];

// ---------- traits ----------
// complete dominance: L is the letter, dom/rec the short phenotype labels, dd/rd the organism described
const MONO = [
  { id: 'height', L: 'T', trait: 'plant height', dom: 'tall', rec: 'short', dd: 'tall pea plant', rd: 'short pea plant', di: ['tall', 'short'], al: ['tall plants', 'short plants'] },
  { id: 'shape', L: 'R', trait: 'seed shape', dom: 'round seeds', rec: 'wrinkled seeds', dd: 'pea plant with round seeds', rd: 'pea plant with wrinkled seeds', di: ['round', 'wrinkled'] },
  { id: 'scolor', L: 'Y', trait: 'seed color', dom: 'yellow seeds', rec: 'green seeds', dd: 'pea plant with yellow seeds', rd: 'pea plant with green seeds', di: ['yellow', 'green'] },
  { id: 'flower', L: 'P', trait: 'flower color', dom: 'purple flowers', rec: 'white flowers', dd: 'pea plant with purple flowers', rd: 'pea plant with white flowers', di: ['purple-flowered', 'white-flowered'] },
  { id: 'pod', L: 'G', trait: 'pod color', dom: 'green pods', rec: 'yellow pods', dd: 'pea plant with green pods', rd: 'pea plant with yellow pods' },
  { id: 'position', L: 'A', trait: 'flower position', dom: 'axial flowers', rec: 'terminal flowers', dd: 'pea plant with axial flowers', rd: 'pea plant with terminal flowers', al: ['axial flowers', 'terminal flowers'], note: 'Axial flowers grow along the stem, and terminal flowers grow at the tip of the stem.' },
  { id: 'body', L: 'E', trait: 'body color', dom: 'gray body', rec: 'ebony body', dd: 'fruit fly with a gray body', rd: 'fruit fly with an ebony body', org: 'fruit fly', orgs: 'fruit flies', al: ['a gray body', 'an ebony body'], q: ['has a gray body', 'has an ebony body'] },
];
// two alleles, the heterozygote shows its own phenotype
const BLEND = [
  { id: 'snap', kind: 'incomplete', name: 'snapdragon flower color', org: 'snapdragon', A: ['R', 'W'], ph: { RR: 'red', RW: 'pink', WW: 'white' },
    who: { RR: 'a red snapdragon', RW: 'a pink snapdragon', WW: 'a white snapdragon' }, letter: 'C' },
  { id: 'four', kind: 'incomplete', name: "four o'clock flower color", org: "four o'clock plant", A: ['R', 'W'], ph: { RR: 'red', RW: 'pink', WW: 'white' },
    who: { RR: "a red four o'clock plant", RW: "a pink four o'clock plant", WW: "a white four o'clock plant" }, letter: 'C' },
  { id: 'roan', kind: 'codom', name: 'coat color in shorthorn cattle', org: 'cow', A: ['R', 'W'], ph: { RR: 'red', RW: 'roan', WW: 'white' },
    who: { RR: 'a red shorthorn', RW: 'a roan shorthorn (red and white hairs mixed)', WW: 'a white shorthorn' }, letter: 'C' },
];
const SEX = [
  { id: 'cb', name: 'red-green color blindness', D: 'B', d: 'b', ok: 'normal-vision', bad: 'colorblind', okQ: 'has normal vision', badQ: 'is colorblind',
    fem: { DD: 'a woman with normal vision who is not a carrier', Dd: 'a woman with normal vision who is a carrier', dd: 'a woman who is colorblind' },
    mal: { D: 'a man with normal vision', d: 'a man who is colorblind' }, girl: 'daughter', boy: 'son', girls: 'daughters', boys: 'sons', mom: 'Mother', dad: 'Father' },
  { id: 'eye', name: 'eye color in fruit flies', D: 'W', d: 'w', ok: 'red-eyed', bad: 'white-eyed', okQ: 'is red-eyed', badQ: 'is white-eyed',
    fem: { DD: 'a red-eyed female that is homozygous', Dd: 'a red-eyed female that is heterozygous', dd: 'a white-eyed female' },
    mal: { D: 'a red-eyed male', d: 'a white-eyed male' }, girl: 'female', boy: 'male', girls: 'females', boys: 'males', mom: 'Female', dad: 'Male' },
];

// ---------- allele display ----------
const sup = (b, s) => `${b}<sup>${s}</sup>`;
const plain = h => String(h).replace(/<sup>(.*?)<\/sup>/g, '^$1').replace(/<[^>]+>/g, '');

// A cross: loci = list of {alleles order (rank), html(allele)} ; parents are arrays of allele codes per locus
// genotype canonical text: alleles sorted by rank within each locus
function genoHtml(spec, g) {   // g: array (per locus) of [a, b]
  return g.map((pair, i) => pair.slice().sort((x, y) => spec.loci[i].rank.indexOf(x) - spec.loci[i].rank.indexOf(y)).map(a => spec.loci[i].html(a)).join('')).join('');
}
// gametes: one allele from each locus, in FOIL order
function gametes(spec, g) {
  let out = [[]];
  g.forEach(pair => { out = out.flatMap(pre => pair.map(a => pre.concat([a]))); });
  return out;
}

// ---------- making each kind of cross ----------
function monoCross(r, words) {
  const t = r.pick(MONO), L = t.L, l = L.toLowerCase();
  const [g1, g2] = r.pick([[[L, l], [L, l]], [[L, l], [L, l]], [[L, l], [l, l]], [[L, L], [l, l]], [[L, L], [L, l]], [[L, l], [l, l]]]);
  const spec = { kind: 'mono', t, loci: [{ rank: [L, l], html: a => a }] };
  const org = t.org || 'pea plant';
  const desc = gg => { const k = gg.join(''); const het = k === L + l || k === l + L;
    return k === l + l ? `a ${t.rd}` : `a ${het ? 'heterozygous' : 'homozygous'} ${t.dd}`; };
  const P = [[g1], [g2]];
  const al = t.al || [t.dom, t.rec];
  const rule = `In ${t.orgs || org + 's'}, the allele for ${al[0]} (${L}) is dominant over the allele for ${al[1]} (${l}).${t.note ? ' ' + t.note : ''}`;
  const text = words ? `${rule} Cross ${desc(g1)} with ${desc(g2)}.` : `${rule} Cross ${desc(g1)} (${g1.join('')}) with ${desc(g2)} (${g2.join('')}).`;
  return { words, spec, P, text, phen: gg => gg[0].includes(L) ? t.dom : t.rec, labels: [t.dom, t.rec], trait: t.id };
}
function blendCross(r, kind, words) {
  const t = r.pick(BLEND.filter(b => b.kind === kind));
  const pairs = [['RW', 'RW'], ['RW', 'RW'], ['RR', 'WW'], ['RW', 'WW'], ['RW', 'RR']];
  const [a, b] = r.pick(pairs).map(k => k.split(''));
  const spec = { kind, t, loci: [{ rank: ['R', 'W'], html: x => sup(t.letter, x) }] };
  const gh = g => genoHtml(spec, [g]);
  const rule = kind === 'incomplete' ? `Flower color in ${t.org}s shows incomplete dominance: ${gh(['R', 'R'])} is red, ${gh(['R', 'W'])} is pink and ${gh(['W', 'W'])} is white.`
    : `Coat color in shorthorn cattle shows codominance: ${gh(['R', 'R'])} is red, ${gh(['R', 'W'])} is roan (both red and white hairs) and ${gh(['W', 'W'])} is white.`;
  const text = words ? `${rule} Cross ${t.who[a.join('')].replace(/ \(.*\)/, '')} with ${t.who[b.join('')].replace(/ \(.*\)/, '')}.`
    : `${rule} Cross ${t.who[a.join('')].replace(/ \(.*\)/, '')} (${gh(a)}) with ${t.who[b.join('')].replace(/ \(.*\)/, '')} (${gh(b)}).`;
  return { words, spec, P: [[a], [b]], text, phen: gg => t.ph[gg[0].slice().sort().join('').replace('WR', 'RW')], labels: ['red', t.ph.RW, 'white'], trait: t.id };
}
function aboCross(r) {
  const opts = [['AO', 'BO'], ['AA', 'BB'], ['AB', 'OO'], ['AB', 'AB'], ['AO', 'AO'], ['AB', 'AO'], ['BO', 'OO'], ['AB', 'BO']];
  const [a, b] = r.pick(opts).map(k => k.split(''));
  const html = x => x === 'O' ? 'i' : sup('I', x);
  const spec = { kind: 'abo', loci: [{ rank: ['A', 'B', 'O'], html }] };
  const ph = gg => { const s = new Set(gg[0]); return s.has('A') && s.has('B') ? 'type AB' : s.has('A') ? 'type A' : s.has('B') ? 'type B' : 'type O'; };
  const gh = g => genoHtml(spec, [g]);
  const text = `ABO blood type: ${sup('I', 'A')} and ${sup('I', 'B')} are codominant, and both are dominant over i. A parent with genotype ${gh(a)} (${ph([a]).replace('type ', 'type ')}) has children with a parent with genotype ${gh(b)} (${ph([b])}).`;
  return { spec, P: [[a], [b]], text, phen: ph, labels: ['type A', 'type B', 'type AB', 'type O'], trait: 'abo', given: true };
}
function sexCross(r, words) {
  const t = r.pick(SEX);
  const [mom, dad] = r.pick([['Dd', 'D'], ['Dd', 'D'], ['Dd', 'd'], ['DD', 'd'], ['dd', 'D']]);
  const code = c => c === 'D' ? 'XD' : c === 'd' ? 'Xd' : 'Y';
  const m = mom.split('').map(code), f = [code(dad), 'Y'];
  const html = x => x === 'Y' ? 'Y' : sup('X', x === 'XD' ? t.D : t.d);
  const spec = { kind: 'sex', t, loci: [{ rank: ['XD', 'Xd', 'Y'], html }] };
  const gh = g => genoHtml(spec, [g]);
  const ph = gg => { const g = gg[0]; const male = g.includes('Y'); const good = g.includes('XD');
    return `${good ? t.ok : t.bad} ${male ? t.boy : t.girl}`; };
  const rule = t.id === 'cb' ? `Red-green color blindness is a recessive trait carried on the X chromosome: ${sup('X', 'B')} is the allele for normal color vision and ${sup('X', 'b')} is the allele for red-green color blindness.`
    : `In fruit flies, white eye color is a recessive trait carried on the X chromosome: ${sup('X', 'W')} is the allele for red eyes and ${sup('X', 'w')} is the allele for white eyes.`;
  const text = words ? `${rule} ${cap(t.fem[mom])} and ${t.mal[dad]} have ${t.id === 'cb' ? 'children' : 'offspring'}.`
    : `${rule} ${cap(t.fem[mom])} (${gh(m)}) and ${t.mal[dad]} (${gh(f)}) have ${t.id === 'cb' ? 'children' : 'offspring'}.`;
  const labels = [`${t.ok} ${t.girl}`, `${t.bad} ${t.girl}`, `${t.ok} ${t.boy}`, `${t.bad} ${t.boy}`];
  return { words, spec, P: [[m], [f]], text, phen: ph, labels, trait: t.id, sex: t };
}
function diCross(r, words) {
  const pairs = [['shape', 'scolor'], ['shape', 'scolor'], ['height', 'flower'], ['shape', 'height'], ['scolor', 'height'], ['shape', 'flower']];
  const [t1, t2] = r.pick(pairs).map(id => MONO.find(t => t.id === id));
  const A = t1.L, a = A.toLowerCase(), B = t2.L, b = B.toLowerCase();
  const [g1, g2] = r.pick([[[[A, a], [B, b]], [[A, a], [B, b]]], [[[A, a], [B, b]], [[A, a], [B, b]]], [[[A, a], [B, b]], [[a, a], [b, b]]], [[[A, A], [B, B]], [[a, a], [b, b]]],
    [[[A, a], [B, B]], [[A, a], [b, b]]], [[[A, a], [b, b]], [[a, a], [B, b]]], [[[A, a], [B, b]], [[A, A], [b, b]]]]);
  const spec = { kind: 'di', loci: [{ rank: [A, a], html: x => x }, { rank: [B, b], html: x => x }], t: [t1, t2] };
  const gh = g => genoHtml(spec, g);
  const ph = gg => `${gg[0].includes(A) ? t1.di[0] : t1.di[1]}, ${gg[1].includes(B) ? t2.di[0] : t2.di[1]}`;
  const desc = g => { const parts = [[t1, g[0]], [t2, g[1]]].map(([t, p]) => {
      const het = p[0] !== p[1], dom = p.includes(t.L);
      return `${het ? 'heterozygous' : 'homozygous'} ${dom ? t.di[0] : t.di[1]}`; });
    return `a pea plant that is ${parts.join(' and ')}`; };
  const al = t => t.al || [t.dom, t.rec];
  const rule = `In pea plants, the allele for ${al(t1)[0]} (${A}) is dominant over the allele for ${al(t1)[1]} (${a}), and the allele for ${al(t2)[0]} (${B}) is dominant over the allele for ${al(t2)[1]} (${b}).`;
  const text = words ? `${rule} Cross ${desc(g1)} with ${desc(g2)}.` : `${rule} Cross ${gh(g1)} × ${gh(g2)}.`;
  const labels = [`${t1.di[0]}, ${t2.di[0]}`, `${t1.di[0]}, ${t2.di[1]}`, `${t1.di[1]}, ${t2.di[0]}`, `${t1.di[1]}, ${t2.di[1]}`];
  return { words, spec, P: [g1, g2], text, phen: ph, labels, trait: t1.id + '+' + t2.id, dlab: [t1.di, t2.di] };
}
const cap = s => s[0].toUpperCase() + s.slice(1);

// ---------- solving a cross (the make side) ----------
function solveCross(c) {
  const top = gametes(c.spec, c.P[0]), side = gametes(c.spec, c.P[1]);
  const cells = side.map(sg => top.map(tg => tg.map((x, i) => [x, sg[i]])));
  const flat = cells.flat();
  const gk = g => genoHtml(c.spec, g);
  const gcount = new Map(), pcount = new Map();
  for (const g of flat) { gcount.set(gk(g), (gcount.get(gk(g)) || 0) + 1); pcount.set(c.phen(g), (pcount.get(c.phen(g)) || 0) + 1); }
  // genotype order: by rank of each allele
  const rankKey = g => (c.spec.kind === 'sex' && g[0].includes('Y') ? 'm' : 'f') + g.map((pair, i) => pair.map(a => c.spec.loci[i].rank.indexOf(a)).sort().join('')).join('|');
  const gorder = [...new Map(flat.map(g => [gk(g), rankKey(g)])).entries()].sort((x, y) => x[1] < y[1] ? -1 : 1).map(x => x[0]);
  const porder = c.labels.filter(l => pcount.has(l));
  const gcd = (a, b) => b ? gcd(b, a % b) : a;
  const ratio = (order, m) => { if (order.length === 1) return `all ${order[0]}`; const k = order.map(x => m.get(x)).reduce(gcd); return order.map(x => `${m.get(x) / k} ${x}`).join(' : '); };
  return { top, side, cells, n: flat.length, gcount, pcount, gratio: ratio(gorder, gcount), pratio: ratio(porder, pcount), gorder, porder };
}
function frac(k, n) {
  const gcd = (a, b) => b ? gcd(b, a % b) : a;
  if (k === 0) return '0 (0%)';
  if (k === n) return '1 (100%)';
  const d = gcd(k, n);
  return `${k / d}/${n / d} (${Gen.m.fmt(100 * k / n, 2)}%)`;
}

// ---------- drawing ----------
function square(c, sol, edges, sz) {
  const gam = g => g.map((a, i) => c.spec.loci[i].html(a)).join('');
  const edge = x => edges ? x : `<span class="ws-ans">${x}</span>`;
  const lab = c.spec.kind === 'sex' ? [c.sex.mom, c.sex.dad] : ['Parent 1', 'Parent 2'];
  return `<div class="pn-wrap"><p class="pn-top">${lab[0]}</p><div class="pn-mid"><p class="pn-side">${lab[1]}</p>` +
    `<table class="pn-sq pn-${sz}"><tr><th class="pn-c"></th>${sol.top.map(g => `<th>${edge(gam(g))}</th>`).join('')}</tr>` +
    sol.cells.map((row, i) => `<tr><th>${edge(gam(sol.side[i]))}</th>${row.map(g => `<td><span class="ws-ans">${genoHtml(c.spec, g)}</span></td>`).join('')}</tr>`).join('') +
    `</table></div></div>`;
}
const line = (label, ans) => `<div class="pn-l"><span>${label}</span><b><span class="ws-ans">${ans}</span></b></div>`;

// the probability question for one cross: pick an outcome and ask its chance
function probQ(r, c, sol) {
  if (c.spec.kind === 'sex') {
    const boy = r.chance(.5), t = c.sex;
    const who = boy ? t.boy : t.girl;
    const bad = r.chance(.5);
    const k = sol.pcount.get(`${bad ? t.bad : t.ok} ${who}`) || 0;
    return { text: `Chance a ${who} ${bad ? t.badQ : t.okQ}`, ans: frac(k, sol.n / 2), target: { sex: boy ? 'm' : 'f', bad }, k, n: sol.n / 2 };
  }
  const ph = r.pick(c.labels.filter(l => sol.pcount.has(l)).concat(r.chance(.15) ? c.labels : []));
  const k = sol.pcount.get(ph) || 0;
  const t = c.spec.t, mq = c.spec.kind === 'mono' && t.q ? t.q[ph === t.dom ? 0 : 1] : null;
  const what = mq || (/(seeds|flowers|pods)$/.test(ph) ? 'has ' + ph : 'is ' + ph);
  return { text: `Chance ${c.spec.kind === 'abo' ? 'a child' : 'an offspring'} ${what}`, ans: frac(k, sol.n), target: { ph }, k, n: sol.n };
}

Gen.add('punnett', {
  title: 'Punnett Squares', type: 'Practice',
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '7' },
    { id: 'cross', label: 'Kind of cross', type: 'select', def: 'mono', options: v => crossesFor(v.grade).map(k => [k, CROSSES[k]]) },
    { id: 'count', label: 'Crosses', type: 'select', def: '3',
      options: v => v.cross === 'di' ? [['2', '2'], ['1', '1']] : v.cross === 'mono' ? [['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8']] : [['3', '3'], ['4', '4']] },
    { id: 'edges', label: 'Print the parent alleles on each square (easier)', type: 'check', def: false },
  ],
  css: `
.pn-card { display: grid; grid-template-columns: auto 1fr; gap: 6px 18px; align-items: start; border: 1px solid #888; border-radius: 6px; padding: 6px 10px 8px; margin: 0 0 10px; break-inside: avoid; }
.pn-card > p { grid-column: 1 / -1; margin: 0; font-size: 14px; line-height: 1.35; }
.pn-wrap { display: inline-block; }
.pn-top { margin: 0 0 1px 1.6em; text-align: center; font: 600 11px var(--sans); text-transform: uppercase; letter-spacing: .06em; color: #444; }
.pn-mid { display: flex; align-items: center; }
.pn-side { writing-mode: vertical-rl; transform: rotate(180deg); margin: 0 3px 0 0; font: 600 11px var(--sans); text-transform: uppercase; letter-spacing: .06em; color: #444; }
.pn-sq { border-collapse: collapse; }
.pn-sq td, .pn-sq th { border: 1.5px solid #222; text-align: center; padding: 0; font: 600 15px var(--sans); }
.pn-sq th { background: #eee; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.pn-sq th.pn-c { background: transparent; border-top: 0; border-left: 0; }
.pn-2 td, .pn-2 th { width: 0.7in; height: 0.42in; }
.pn-4 td, .pn-4 th { width: 0.66in; height: 0.36in; font-size: 13px; }
.pn-2s td, .pn-2s th { width: 0.56in; height: 0.33in; font-size: 14px; }
.pn-qs { min-width: 0; }
.pn-l { display: flex; align-items: flex-end; gap: 6px; min-height: 0.34in; }
.pn-l > span { font: 600 12px var(--sans); color: #333; white-space: nowrap; padding-bottom: 2px; width: 7.4em; flex: none; }
.pn-l > b { flex: 1; border-bottom: 1px solid #555; font-weight: 400; font-size: 13.5px; line-height: 1.3; padding-bottom: 1px; }
.pn-ex { display: grid; grid-template-columns: auto 1fr; gap: 4px 16px; align-items: center; }
.pn-ex .pn-sq td .ws-ans, .pn-ex .pn-sq th .ws-ans { visibility: visible; color: inherit; font-weight: 600; }
@media (max-width: 700px) { .pn-card, .pn-ex { grid-template-columns: 1fr; } }
@media print { .pn-card > p { font-size: 9.5pt; } .pn-l { min-height: 0.29in; } .pn-l > span { font-size: 8.5pt; } .pn-card { margin-bottom: 6px; padding: 4px 8px 6px; } .pn-2 td, .pn-2 th { height: 0.34in; width: 0.6in; } .pn-4 td, .pn-4 th { height: 0.3in; } .pn-2s td, .pn-2s th { height: 0.26in; width: 0.5in; } .pn-many .pn-card { margin-bottom: 4px; padding: 3px 8px 4px; } .pn-many .pn-l { min-height: 0.25in; } .pn-ex .pn-2 td, .pn-ex .pn-2 th { height: 0.27in; width: 0.5in; } }
`,
  make(v, r) {
    const g = v.grade, H = hs(g), kind = v.cross;
    const n = +v.count;
    const words = () => +g >= 8 && r.chance(.5);
    const one = k => k === 'mono' ? monoCross(r, words()) : k === 'incomplete' ? blendCross(r, 'incomplete', words())
      : k === 'codom' ? (r.chance(.5) ? blendCross(r, 'codom', words()) : aboCross(r)) : k === 'sex' ? sexCross(r, words()) : diCross(r, words());
    let kinds;
    if (kind === 'mix') { const pool = r.shuffle(['mono', 'incomplete', 'codom', 'sex']); kinds = Array.from({ length: n }, (_, i) => pool[i % 4]); if (n >= 4 && r.chance(.6)) kinds[n - 1] = 'di'; }
    else kinds = Array.from({ length: n }, () => kind);
    let i = 0;
    const usedT = new Set(); let tries = 0;
    const crosses = r.distinct(n, () => { const c = one(kinds[i % n]); if (usedT.has(c.trait) && tries++ < 40) return null; i++; usedT.add(c.trait); return c; }, c => c.trait + JSON.stringify(c.P));
    // order the crosses as the kinds came out so a dihybrid sits last
    crosses.sort((a, b) => (a.spec.kind === 'di') - (b.spec.kind === 'di'));
    const items = [], cards = [];
    crosses.forEach((c, k) => {
      const sol = solveCross(c), pq = probQ(r, c, sol);
      const showP = !!c.words;
      const pg = `${genoHtml(c.spec, c.P[0])} × ${genoHtml(c.spec, c.P[1])}`;
      const qs = [];
      if (showP) qs.push(line('Parents:', pg));
      if (c.spec.kind === 'di') {
        const het = genoHtml(c.spec, c.spec.loci.map(l => l.rank.slice(0, 2)));
        const cnt = sol.gcount.get(het) || 0;
        qs.push(line(`Boxes with ${het}:`, `${cnt} of 16`));
        c.countG = { geno: het, cnt };
      } else qs.push(line('Genotype ratio:', sol.gratio));
      qs.push(line('Phenotype ratio:', sol.pratio));
      qs.push(line('Chance:', pq.ans));
      const sz = c.spec.kind === 'di' ? 4 : n >= 6 ? '2s' : 2;   // 6 or 8 one-trait crosses use a smaller square to stay on two pages
      cards.push(`<div class="pn-card"><p><span class="ws-num">${k + 1}.</span> ${c.text} Find the ${pq.text.replace(/^Chance /, 'chance that ')}.</p>${square(c, sol, v.edges, sz)}<div class="pn-qs">${qs.join('')}</div></div>`);
      items.push({ q: plain(c.text), a: plain(`${pg}; ${c.countG ? c.countG.cnt + ' ' + c.countG.geno : sol.gratio}; ${sol.pratio}; ${pq.ans}`),
        kind: c.spec.kind, P: c.P, trait: c.trait, top: sol.top, side: sol.side, cells: sol.cells.map(row => row.map(x => plain(genoHtml(c.spec, x)))),
        gratio: plain(sol.gratio), pratio: sol.pratio, prob: pq, countG: c.countG ? { geno: plain(c.countG.geno), cnt: c.countG.cnt } : null, sexT: c.sex ? c.sex.id : null, dlab: c.dlab || null });
    });
    // worked example: a one-trait cross (or, on a dihybrid sheet, how to list the four gametes)
    let ex;
    if (kind === 'di') {
      ex = example('<b>Finding the gametes of RrYy.</b> Each gamete gets one allele for each trait. Pair them like FOIL: first R with Y and y, then r with Y and y.',
        'Gametes: <b>RY, Ry, rY, ry</b>. Write the four gametes of one parent across the top and the other parent\'s down the side, then fill all 16 boxes. A plant like RRyy gives the same gamete four times: Ry, Ry, Ry, Ry.');
    } else {
      let e = null;
      for (let t = 0; t < 60 && !e; t++) { const c = monoCross(r, false); const k = c.P.map(p => p[0].join('')).join(' '); if (!crosses.some(x => plain(x.text) === plain(c.text)) && /[A-Z][a-z] [a-z]{2}|[A-Z][a-z] [A-Z][a-z]/.test(k)) e = c; }
      e = e || monoCross(r, false);
      const s = solveCross(e), L = e.spec.t.L;
      const short = e.spec.t.rec;
      const kk = s.pcount.get(short) || 0;
      ex = `<div class="ws-example"><p class="ws-tag">Example</p><div class="pn-ex">${square(e, s, true, 2)}<div><p style="margin:0 0 4px">${e.text}</p>` +
        `<p style="margin:0">Each box gets one allele from its column and one from its row. ` +
        `Genotype ratio: <b>${s.gratio}</b>. Phenotype ratio: <b>${s.pratio}</b>. Chance of ${e.spec.t.al ? e.spec.t.al[1] : short}: <b>${kk} of ${s.n} boxes = ${frac(kk, s.n)}</b>.</p></div></div></div>`;
      void L;
    }
    const gl = GRADES.find(x => x[0] === g)[1];
    const title = kind === 'mix' ? 'Punnett Squares: mixed review' : `Punnett Squares: ${CROSSES[kind].replace(/ \(.*\)/, '').toLowerCase()}`;
    return {
      title, level: `${gl}${kind === 'di' ? ', 4 × 4 squares' : ''}`,
      ican: kind === 'di' ? 'I can use a 4 × 4 Punnett square to predict the offspring of a two-trait cross.'
        : 'I can use a Punnett square to predict the genotypes and phenotypes of offspring and the chance of each.',
      directions: `${v.edges ? 'Fill' : 'Write each parent\'s alleles on the edges of the square and fill'} every box with an offspring genotype. Answer beside the square. Write ratios like 1 TT : 2 Tt : 1 tt and chances as a fraction and a percent.`,
      minutes: kind === 'di' ? 30 : 25, materials: 'pencil',
      parts: [part('', ex), part('Crosses', n >= 6 ? `<div class="pn-many">${cards.join('')}</div>` : cards.join(''))], items,
      mistakes: 'Writing both alleles from one parent in a box, or forgetting that a homozygous parent still gives two (identical) gametes. Mixing up genotype (letters) and phenotype (what the organism looks like). For incomplete and codominance, calling the heterozygote the dominant color.' +
        (H ? ' For sex-linked crosses, giving a son an X from his father; sons get their X from their mother and a Y from their father. For two-trait crosses, putting two alleles of the same gene in one gamete.' : ''),
      notes: 'Every trait is a real one: Mendel\'s pea traits (seed shape, seed color, plant height, flower color, pod color, flower position), fruit fly body color (gray over ebony), snapdragon and four o\'clock flower color (incomplete dominance), roan shorthorn cattle and ABO blood type (codominance), and red-green color blindness and white eyes in fruit flies (sex-linked recessive). ' +
        'Equal ratios in a different form (2 Tt : 2 tt for 1 Tt : 1 tt) are fine. Sex-linked chances are asked among sons or among daughters, so the denominator is the 2 boxes of that sex. ' +
        (kind === 'di' || kind === 'mix' ? 'Two-trait crosses ask how many of the 16 boxes have the double heterozygote in place of a full genotype ratio, which has up to nine parts. ' : '') +
        'The order of the gametes on the edges can differ from the key; the counts will match.',
    };
  },
  verify(s) {
    const out = [];
    // independent re-work: enumerate every way to take one allele from each parent at each locus, count outcomes
    const RANK = { abo: ['A', 'B', 'O'], sex: ['XD', 'Xd', 'Y'] };
    for (const it of s.items) {
      const loci = it.P[0].length;
      // all offspring: product over loci of (parent1 allele i) x (parent2 allele j)
      let kids = [[]];
      for (let L = 0; L < loci; L++) {
        const next = [];
        for (const k of kids) for (const a of it.P[0][L]) for (const b of it.P[1][L]) next.push(k.concat([[a, b]]));
        kids = next;
      }
      if (kids.length * (loci === 2 ? 1 : 1) !== it.cells.flat().length) out.push(`${it.q}: ${it.cells.flat().length} boxes for ${kids.length} outcomes`);
      const toText = (L, a) => it.kind === 'abo' ? (a === 'O' ? 'i' : 'I^' + a) : it.kind === 'sex' ? (a === 'Y' ? 'Y' : null) : (it.kind === 'incomplete' || it.kind === 'codom') ? 'C^' + a : a;
      // phenotype rules, written from the biology
      const phen = k => {
        const g = k.map(p => p.join(''));
        if (it.kind === 'abo') { const s2 = g[0]; return /A/.test(s2) && /B/.test(s2) ? 'type AB' : /A/.test(s2) ? 'type A' : /B/.test(s2) ? 'type B' : 'type O'; }
        if (it.kind === 'incomplete' || it.kind === 'codom') return { RR: 'red', WW: 'white' }[g[0]] || (it.kind === 'incomplete' ? 'pink' : 'roan');
        if (it.kind === 'sex') return null;
        return g.map(x => x !== x.toLowerCase() ? 'D' : 'r').join('');
      };
      // check each box against its row and column gamete
      it.cells.forEach((row, i) => row.forEach((cell, j) => {
        const want = it.top[j].map((a, L) => [a, it.side[i][L]]);
        if (it.kind === 'sex' || it.kind === 'abo' || it.kind === 'incomplete' || it.kind === 'codom') {
          const rank = RANK[it.kind] || ['R', 'W'];
          const sorted = want[0].slice().sort((x, y) => rank.indexOf(x) - rank.indexOf(y));
          const txt = it.kind === 'sex' ? sorted.map(a => a === 'Y' ? 'Y' : 'X^' + (a === 'XD' ? (it.sexT === 'cb' ? 'B' : 'W') : (it.sexT === 'cb' ? 'b' : 'w'))).join('') : sorted.map(a => toText(0, a)).join('');
          if (cell !== txt) out.push(`${it.q}: box ${i},${j} says ${cell}, should be ${txt}`);
        } else {
          const txt = want.map(p => p.slice().sort((x, y) => (x === x.toLowerCase()) - (y === y.toLowerCase())).join('')).join('');
          if (cell !== txt) out.push(`${it.q}: box ${i},${j} says ${cell}, should be ${txt}`);
        }
      }));
      // the edges must be the parents' own alleles, each allele appearing as often as in the parent
      for (const [edge, P] of [[it.top, it.P[0]], [it.side, it.P[1]]]) for (let L = 0; L < loci; L++) {
        const seen = edge.map(gm => gm[L]).sort().join(''), want = loci === 1 ? P[L].slice().sort().join('') : P[L].concat(P[L]).sort().join('');
        if (seen !== want) out.push(`${it.q}: edge alleles ${seen}, parent has ${P[L].join('')}`);
      }
      // ratios: parse the key text and compare to fresh counts
      const parse = t => { const m = new Map(); if (/^all /.test(t)) { m.set(t.slice(4), 1); return m; } for (const p of t.split(' : ')) { const x = p.match(/^(\d+) (.+)$/); m.set(x[2], +x[1]); } return m; };
      const same = (m1, m2) => { const k1 = [...m1.keys()].sort().join('|'), k2 = [...m2.keys()].sort().join('|'); if (k1 !== k2) return false;
        const keys = [...m1.keys()], f = m2.get(keys[0]) / m1.get(keys[0]); return keys.every(k => Math.abs(m2.get(k) / m1.get(k) - f) < 1e-9); };
      if (it.kind !== 'sex') {
        const pc = new Map();
        for (const k of kids) { const p = phen(k); pc.set(p, (pc.get(p) || 0) + 1); }
        const parsed = parse(it.pratio);
        if (parsed.size !== pc.size) out.push(`${it.q}: phenotype ratio ${it.pratio} has ${parsed.size} classes, expected ${pc.size}`);
        // match class sizes regardless of label wording: sorted counts must be proportional
        const a1 = [...parsed.values()].sort((x, y) => x - y), a2 = [...pc.values()].sort((x, y) => x - y);
        const f = a2[0] / a1[0]; if (a1.length !== a2.length || a1.some((x, i) => Math.abs(a2[i] / x - f) > 1e-9)) out.push(`${it.q}: phenotype ratio ${it.pratio} vs counts ${a2.join(':')}`);
        if (it.kind === 'abo' || it.kind === 'incomplete' || it.kind === 'codom') if (!same(parsed, pc)) out.push(`${it.q}: phenotype labels ${it.pratio}`);
        if (it.kind === 'di') {
          const lc = new Map();
          for (const k of kids) { const lab = k.map((p, L) => it.dlab[L][p.some(x => x !== x.toLowerCase()) ? 0 : 1]).join(', '); lc.set(lab, (lc.get(lab) || 0) + 1); }
          if (!same(parsed, lc)) out.push(`${it.q}: phenotype labels ${it.pratio}`);
        }
        if (it.kind === 'mono' || it.kind === 'di') {   // label check: dominant phenotype count = kids with an uppercase allele
          const domCount = kids.filter(k => k[0].some(a => a !== a.toLowerCase())).length;
          const t = parsed; const first = [...t.keys()][0];
          if (domCount && domCount !== kids.length && it.kind === 'mono' && Math.abs(t.get(first) / [...t.values()].reduce((x, y) => x + y) - domCount / kids.length) > 1e-9) out.push(`${it.q}: dominant share wrong in ${it.pratio}`);
        }
      } else {
        const sons = kids.filter(k => k[0].includes('Y')), daus = kids.filter(k => !k[0].includes('Y'));
        if (sons.length !== daus.length) out.push(`${it.q}: sons and daughters not equal`);
        const pool = it.prob.target.sex === 'm' ? sons : daus;
        // a son shows the trait with one recessive X; a daughter needs two
        const affected = k => k[0].every(a => a !== 'XD');
        const want = pool.filter(k => it.prob.target.bad ? affected(k) : !affected(k)).length;
        if (want !== it.prob.k || pool.length !== it.prob.n) out.push(`${it.q}: chance ${it.prob.ans}, recount ${want}/${pool.length}`);
        const words = it.sexT === 'cb' ? ['normal-vision', 'colorblind', 'daughter', 'son'] : ['red-eyed', 'white-eyed', 'female', 'male'];
        const pc = new Map();
        for (const k of kids) { const lab = `${affected(k) ? words[1] : words[0]} ${k[0].includes('Y') ? words[3] : words[2]}`; pc.set(lab, (pc.get(lab) || 0) + 1); }
        if (!same(parse(it.pratio), pc)) out.push(`${it.q}: phenotype ratio ${it.pratio}`);
        const gc = new Map(); for (const x of it.cells.flat()) gc.set(x, (gc.get(x) || 0) + 1);
        if (!same(parse(it.gratio), gc)) out.push(`${it.q}: genotype ratio ${it.gratio}`);
        continue;
      }
      if (it.countG) {
        const c = it.cells.flat().filter(x => x === it.countG.geno).length;
        if (c !== it.countG.cnt) out.push(`${it.q}: ${it.countG.geno} count ${it.countG.cnt}, boxes show ${c}`);
      } else {
        const gc = new Map(); for (const x of it.cells.flat()) gc.set(x, (gc.get(x) || 0) + 1);
        if (!same(parse(it.gratio), gc)) out.push(`${it.q}: genotype ratio ${it.gratio}`);
      }
      // probability: k of n must match the parsed phenotype class
      const pm = parse(it.pratio), tot = [...pm.values()].reduce((x, y) => x + y);
      const share = /^all /.test(it.pratio) ? (pm.has(it.prob.target.ph) ? 1 : 0) : (pm.get(it.prob.target.ph) || 0) / tot;
      if (Math.abs(share - it.prob.k / it.prob.n) > 1e-9) out.push(`${it.q}: chance ${it.prob.ans} for ${it.prob.target.ph}, ratio says ${share}`);
    }
    return out;
  },
});
})();
