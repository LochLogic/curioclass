// Spanish and French Practice generator, grades K-12 (novice K-5, then levels 1 to 4 in middle and high school).
// Loads world-language-data.js first (verb principal parts, word banks, and hand-typed check tables).
// Skills by level:
//   Novice K-5: count and write 1 to 10 with the number words to trace, color words matched to crayons, days of the
//     week and months in order, clocks on the hour.
//   Novice (level 1): present tense charts and sentences (regular, the core irregulars, stem changers, reflexives),
//     ir a / aller + infinitive, numbers in words (0 to 100, with the French 70 to 99 math), math with number words,
//     colors and nationalities that agree, articles (and French partitives), possessive adjectives, days, months and
//     dates, telling time (clock faces), the French 24-hour clock, gustar, French en/au/aux/à with places, vocabulary
//     by theme, and a mixed review.
//   Intermediate (level 2): present, preterite / passé composé (with être agreement), imperfect, ir a / futur proche,
//     preterite-or-imperfect signal words, numbers to 9,999, the 24-hour clock, places, dates, mixed review.
//   Advanced (levels 3-4): future, conditional, present subjunctive, imperfect subjunctive (Spanish), plus-que-parfait
//     (French), subjunctive-or-indicative with a reason, si clauses (real and hypothetical), mixed review.
// make() builds every verb form by rule from principal parts; verify() re-derives each one from hand-typed full
// paradigms (irregulars) and model-verb substitution (regulars), and re-works every number word, agreement and article
// by a second, separately written rule.
// Standards: ACTFL World-Readiness Standards 1.1 Interpersonal, 1.2 Interpretive, 1.3 Presentational, 4.1 Language
// comparisons; ACTFL Proficiency Guidelines, Novice Low to Intermediate Mid / Advanced Low for levels 3-4.
(() => {
const { blank, part, example, fill, esc, table } = Gen.h;
const W = (typeof window !== 'undefined' ? window : globalThis).WLDATA;
const ES = W.es, FR = W.fr;

/* ---------- small text helpers ---------- */
const cap = s => s.charAt(0).toUpperCase() + s.slice(1);
const vowel = s => /^[aeiouyàâäéèêëîïôöùûüœh]/i.test(s);
const list = s => { const t = s.split(' '), out = []; for (let i = 0; i < t.length; i++) { if (t[i] === 'se') { out.push('se ' + t[++i]); } else out.push(t[i]); } return out; };
const NB = ' ';   // French puts a no-break space before ? and :

/* ---------- Spanish forms, by rule from principal parts ---------- */
const ESE = {
  pres: { ar: ['o', 'as', 'a', 'amos', 'áis', 'an'], er: ['o', 'es', 'e', 'emos', 'éis', 'en'], ir: ['o', 'es', 'e', 'imos', 'ís', 'en'] },
  pret: { ar: ['é', 'aste', 'ó', 'amos', 'asteis', 'aron'], er: ['í', 'iste', 'ió', 'imos', 'isteis', 'ieron'], ir: ['í', 'iste', 'ió', 'imos', 'isteis', 'ieron'] },
  impf: { ar: ['aba', 'abas', 'aba', 'ábamos', 'abais', 'aban'], er: ['ía', 'ías', 'ía', 'íamos', 'íais', 'ían'], ir: ['ía', 'ías', 'ía', 'íamos', 'íais', 'ían'] },
  fut: ['é', 'ás', 'á', 'emos', 'éis', 'án'], cond: ['ía', 'ías', 'ía', 'íamos', 'íais', 'ían'],
};
const lastSwap = (s, from, to) => { const i = s.lastIndexOf(from); return i < 0 ? s : s.slice(0, i) + to + s.slice(i + from.length); };
const boot = (st, sc) => sc === 'ug' ? lastSwap(st, 'u', 'ue') : sc === 'ue' ? lastSwap(st, 'o', 'ue') : sc === 'ie' ? lastSwap(st, 'e', 'ie') : lastSwap(st, 'e', 'i');
const shortStem = (st, sc) => sc === 'ue' ? lastSwap(st, 'o', 'u') : lastSwap(st, 'e', 'i');
const esSpell = st => st.replace(/c$/, 'qu').replace(/g$/, 'gu').replace(/z$/, 'c');
function esCore(base, v, tense, p) {
  const t = base.slice(-2), st = base.slice(0, -2);
  if (tense === 'pres') {
    if (v.pres) return v.pres[p];
    if (p === 0 && v.yo) return v.yo;
    return (v.sc && [0, 1, 2, 5].includes(p) ? boot(st, v.sc) : st) + ESE.pres[t][p];
  }
  if (tense === 'pret') {
    if (v.pret) return v.pret[p];
    if (v.ps) return v.ps + ['e', 'iste', 'o', 'imos', 'isteis', v.ps.endsWith('j') ? 'eron' : 'ieron'][p];
    if (t === 'ar' && p === 0) return esSpell(st) + 'é';
    if (t === 'ir' && v.sc && (p === 2 || p === 5)) return shortStem(st, v.sc) + ESE.pret.ir[p];
    return st + ESE.pret[t][p];
  }
  if (tense === 'impf') return v.impf ? v.impf[p] : st + ESE.impf[t][p];
  if (tense === 'fut') return (v.fut || base) + ESE.fut[p];
  if (tense === 'cond') return (v.fut || base) + ESE.cond[p];
  if (tense === 'subj') {
    if (v.subj) return v.subj[p];
    const yst = esCore(base, v, 'pres', 0).replace(/o$/, '');
    let s = yst;
    if ((p === 3 || p === 4) && !v.yo && v.sc) s = t === 'ir' ? shortStem(st, v.sc) : st;
    if (t === 'ar') s = esSpell(s);
    return s + (t === 'ar' ? ['e', 'es', 'e', 'emos', 'éis', 'en'] : ['a', 'as', 'a', 'amos', 'áis', 'an'])[p];
  }
  if (tense === 'impsubj') {
    let s = esCore(base, v, 'pret', 5).replace(/ron$/, '');
    if (p === 3) s = s.slice(0, -1) + ({ a: 'á', e: 'é' }[s.slice(-1)] || s.slice(-1));
    return s + ['ra', 'ras', 'ra', 'ramos', 'rais', 'ran'][p];
  }
  if (tense === 'ira') return ES.verbs.ir.pres[p] + ' a ' + base;
  return '';
}
function esForm(inf, tense, p) {
  const v = ES.verbs[inf], refl = inf.endsWith('se'), base = refl ? inf.slice(0, -2) : inf;
  const f = esCore(base, v, tense, p);
  return refl ? ['me', 'te', 'se', 'nos', 'os', 'se'][p] + ' ' + f : f;
}

/* ---------- French forms, by rule ---------- */
const frGroup = base => base.endsWith('er') ? 'er' : base.endsWith('ir') ? 'ir' : 're';
const frFix = (st, end) => /^[ao]/.test(end) ? (st.endsWith('g') ? st + 'e' : st.endsWith('c') ? st.slice(0, -1) + 'ç' : st) : st;
const frUnfix = (st, end) => /^[ie]/.test(end) ? st.replace(/ge$/, 'g').replace(/ç$/, 'c') : st;
function frBase(inf) { return inf.replace(/^se /, '').replace(/^s'/, ''); }
function frPres(base, v, p) {
  if (v && v.pres) return v.pres[p];
  const g = frGroup(base), st = base.slice(0, -2);
  if (g === 'er') { const e = ['e', 'es', 'e', 'ons', 'ez', 'ent'][p]; return frFix(st, e) + e; }
  if (g === 'ir') return st + ['is', 'is', 'it', 'issons', 'issez', 'issent'][p];
  return st + ['s', 's', '', 'ons', 'ez', 'ent'][p];
}
const frImpfStem = (base, v) => (v && v.impf) || frPres(base, v, 3).replace(/ons$/, '');
const FRI = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient'];
function frPP(base, v) { if (v && v.pp) return v.pp; const g = frGroup(base), st = base.slice(0, -2); return st + (g === 'er' ? 'é' : g === 'ir' ? 'i' : 'u'); }
// past participle agreement with être: g is m, f, or '' when the subject's gender is not known
function frAgree(pp, p, g) {
  if (p <= 1) return pp + '(e)';
  if (p === 2) return pp + (g === 'm' ? '' : g === 'f' ? 'e' : '(e)');
  if (p === 4) return pp + '(e)(s)';
  return pp + (g === 'm' ? 's' : g === 'f' ? 'es' : '(e)s');
}
function frCore(base, v, tense, p, g) {
  if (tense === 'pres') return frPres(base, v, p);
  if (tense === 'impf') { const st = frImpfStem(base, v), e = FRI[p]; return frUnfix(st, e) + e; }
  const fst = (v && v.fut) || (base.endsWith('re') ? base.slice(0, -1) : base);
  if (tense === 'fut') return fst + ['ai', 'as', 'a', 'ons', 'ez', 'ont'][p];
  if (tense === 'cond') return fst + FRI[p];
  if (tense === 'subj') {
    if (v && v.subj) return v.subj[p];
    if (p === 3 || p === 4) return frCore(base, v, 'impf', p);
    return frPres(base, v, 5).replace(/ent$/, '') + ['e', 'es', 'e', '', '', 'ent'][p];
  }
  if (tense === 'pc' || tense === 'pqp') {
    const aux = v && v.e ? 'être' : 'avoir', av = FR.verbs[aux];
    const a = tense === 'pc' ? frPres(aux, av, p) : frCore(aux, av, 'impf', p);
    const pp = frPP(base, v);
    return a + ' ' + (v && v.e ? frAgree(pp, p, g) : pp);
  }
  if (tense === 'proche') return FR.verbs.aller.pres[p] + ' ' + base;
  return '';
}
function frForm(inf, tense, p, g = '') {
  const v = FR.verbs[inf], refl = inf !== frBase(inf), base = frBase(inf);
  const f = frCore(base, v, tense, p, g);
  if (!refl) return f;
  const pro = ['me', 'te', 'se', 'nous', 'vous', 'se'][p];
  return (p !== 3 && p !== 4 && vowel(f) ? pro[0] + '\'' : pro + ' ') + f;
}
const form = (lang, inf, tense, p, g) => lang === 'es' ? esForm(inf, tense, p) : frForm(inf, tense, p, g);

/* ---------- the second route, used only by verify() ---------- */
const MODEL = {
  es: { pres: { ar: 'hablo hablas habla hablamos habláis hablan', er: 'como comes come comemos coméis comen', ir: 'vivo vives vive vivimos vivís viven' },
    pret: { ar: 'hablé hablaste habló hablamos hablasteis hablaron', er: 'comí comiste comió comimos comisteis comieron', ir: 'viví viviste vivió vivimos vivisteis vivieron' },
    impf: { ar: 'hablaba hablabas hablaba hablábamos hablabais hablaban', er: 'comía comías comía comíamos comíais comían', ir: 'vivía vivías vivía vivíamos vivíais vivían' },
    subj: { ar: 'hable hables hable hablemos habléis hablen', er: 'coma comas coma comamos comáis coman', ir: 'viva vivas viva vivamos viváis vivan' },
    fut: 'hablaré hablarás hablará hablaremos hablaréis hablarán', cond: 'hablaría hablarías hablaría hablaríamos hablaríais hablarían' },
  fr: { pres: { er: 'parle parles parle parlons parlez parlent', ir: 'finis finis finit finissons finissez finissent', re: 'vends vends vend vendons vendez vendent' },
    subj: { er: 'parle parles parle parlions parliez parlent', ir: 'finisse finisses finisse finissions finissiez finissent', re: 'vende vendes vende vendions vendiez vendent' },
    impf: 'parlais parlais parlait parlions parliez parlaient', fut: 'parlerai parleras parlera parlerons parlerez parleront',
    cond: 'parlerais parlerais parlerait parlerions parleriez parleraient' },
};
const MS = { ar: 'habl', er: 'com', ir: 'viv' };
function esCheck(inf, tense, p) {
  const refl = inf.endsWith('se'), base = refl ? inf.slice(0, -2) : inf, t = base.slice(-2), st = base.slice(0, -2), C = ES.chk;
  const from = (tbl, k) => tbl[k] ? tbl[k].split(' ')[p] : null;
  const swap = (m, model) => st + m.split(' ')[p].slice(model.length);
  let f;
  if (tense === 'pres') f = from(C.pres, base) || swap(MODEL.es.pres[t], MS[t]);
  else if (tense === 'pret') f = from(C.pret, base) || swap(MODEL.es.pret[t], MS[t]);
  else if (tense === 'impf') f = from(C.impf, base) || swap(MODEL.es.impf[t], MS[t]);
  else if (tense === 'fut' || tense === 'cond') f = (C.fut[base] || base) + MODEL.es[tense].split(' ')[p].slice('hablar'.length);
  else if (tense === 'subj') f = from(C.subj, base) || swap(MODEL.es.subj[t], MS[t]);
  else if (tense === 'impsubj') {
    const third = C.pret[base] ? C.pret[base].split(' ')[5] : swap(MODEL.es.pret[t], MS[t]).replace(/.*/, () => st + MODEL.es.pret[t].split(' ')[5].slice(MS[t].length));
    const s = third.slice(0, -3);
    f = (p === 3 ? s.replace(/a$/, 'á').replace(/e$/, 'é') : s) + 'ra ras ra ramos rais ran'.split(' ')[p];
  } else if (tense === 'ira') f = C.pres.ir.split(' ')[p] + ' a ' + base;
  if (refl) f = 'me te se nos os se'.split(' ')[p] + ' ' + f;
  return f;
}
function frCheck(inf, tense, p, g = '') {
  const refl = /^se |^s'/.test(inf), base = inf.replace(/^se |^s'/, ''), C = FR.chk;
  const grp = base.endsWith('er') ? 'er' : base.endsWith('ir') ? 'ir' : 're', st = base.slice(0, -2);
  const from = (tbl, k) => tbl[k] ? tbl[k].split(' ')[p] : null;
  const spell = (stem, ending) => (base.endsWith('ger') && /^[ao]/.test(ending)) ? stem + 'e' + ending : (base.endsWith('cer') && /^[ao]/.test(ending)) ? stem.slice(0, -1) + 'ç' + ending : stem + ending;
  const model = (m, mst) => { const e = m.split(' ')[p].slice(mst.length); return spell(st, e); };
  const pres = q => C.pres[base] ? C.pres[base].split(' ')[q] : (() => { const m = MODEL.fr.pres[grp].split(' ')[q], ms = { er: 'parl', ir: 'fin', re: 'vend' }[grp]; return spell(st, m.slice(ms.length)); })();
  const impfStem = C.impf[base] || (C.pres[base] ? C.pres[base].split(' ')[3].replace(/ons$/, '').replace(/ge$/, 'g').replace(/ç$/, 'c') : grp === 'ir' ? st + 'iss' : st);
  const impf = q => { const e = MODEL.fr.impf.split(' ')[q].slice(4); return C.impf[base] ? C.impf[base] + e : spell(impfStem, e); };
  const agree = (pp, q) => {
    const tail = q === 0 || q === 1 ? '(e)' : q === 4 ? '(e)(s)' : q === 3 ? '(e)s' : q === 2 ? { m: '', f: 'e' }[g] ?? '(e)' : { m: 's', f: 'es' }[g] ?? '(e)s';
    return pp + tail;
  };
  let f;
  if (tense === 'pres') f = pres(p);
  else if (tense === 'impf') f = impf(p);
  else if (tense === 'fut' || tense === 'cond') {
    const s = C.fut[base] || (grp === 're' ? base.slice(0, -1) : base);
    f = s + MODEL.fr[tense].split(' ')[p].slice('parler'.length);
  } else if (tense === 'subj') f = from(C.subj, base) || model(MODEL.fr.subj[grp], { er: 'parl', ir: 'fin', re: 'vend' }[grp]);
  else if (tense === 'pc' || tense === 'pqp') {
    const etre = C.etre.split(' ').includes(base);
    const aux = tense === 'pc' ? C.pres[etre ? 'être' : 'avoir'].split(' ')[p] : (etre ? 'ét' : 'av') + MODEL.fr.impf.split(' ')[p].slice(4);
    const pp = C.pp[base] || st + { er: 'é', ir: 'i', re: 'u' }[grp];
    f = aux + ' ' + (etre ? agree(pp, p) : pp);
  } else if (tense === 'proche') f = C.pres.aller.split(' ')[p] + ' ' + base;
  if (refl) { const pro = 'me te se nous vous se'.split(' ')[p]; f = (p < 3 || p === 5) && /^[aeiouhéèê]/.test(f) ? pro.slice(0, 1) + '\'' + f : pro + ' ' + f; }
  return f;
}
const check = (lang, inf, tense, p, g) => lang === 'es' ? esCheck(inf, tense, p) : frCheck(inf, tense, p, g);

/* ---------- numbers in words ---------- */
const ESU = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince',
  'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte', 'veintiuno', 'veintidós', 'veintitrés', 'veinticuatro', 'veinticinco', 'veintiséis',
  'veintisiete', 'veintiocho', 'veintinueve'];
const EST = { 3: 'treinta', 4: 'cuarenta', 5: 'cincuenta', 6: 'sesenta', 7: 'setenta', 8: 'ochenta', 9: 'noventa' };
const ESH = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos'];
function esNum(n) {
  const b100 = x => x < 30 ? ESU[x] : EST[Math.floor(x / 10)] + (x % 10 ? ' y ' + ESU[x % 10] : '');
  const b1000 = x => x === 100 ? 'cien' : x < 100 ? b100(x) : ESH[Math.floor(x / 100)] + (x % 100 ? ' ' + b100(x % 100) : '');
  if (n < 1000) return b1000(n);
  const th = Math.floor(n / 1000), rest = n % 1000;
  return (th === 1 ? 'mil' : ESU[th] + ' mil') + (rest ? ' ' + b1000(rest) : '');
}
const FRU = ['zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize'];
const FRT = { 2: 'vingt', 3: 'trente', 4: 'quarante', 5: 'cinquante', 6: 'soixante' };
function frNum(n) {
  const b100 = x => {
    if (x < 17) return FRU[x];
    if (x < 20) return 'dix-' + FRU[x - 10];
    if (x < 70) { const u = x % 10; return FRT[Math.floor(x / 10)] + (u === 0 ? '' : u === 1 ? ' et un' : '-' + FRU[u]); }
    if (x < 80) return x === 71 ? 'soixante et onze' : 'soixante-' + b100(x - 60);
    return x === 80 ? 'quatre-vingts' : 'quatre-vingt-' + b100(x - 80);
  };
  const b1000 = x => { if (x < 100) return b100(x); const h = Math.floor(x / 100), r = x % 100;
    return (h === 1 ? 'cent' : FRU[h] + (r ? ' cent' : ' cents')) + (r ? ' ' + b100(r) : ''); };
  if (n < 1000) return b1000(n);
  const th = Math.floor(n / 1000), rest = n % 1000;
  return (th === 1 ? 'mille' : FRU[th] + ' mille') + (rest ? ' ' + b1000(rest) : '');
}
const num = (lang, n) => lang === 'es' ? esNum(n) : frNum(n);
// second route for verify: built digit by digit from different tables
function numCheck(lang, n) {
  if (lang === 'es') {
    const u = 'cero uno dos tres cuatro cinco seis siete ocho nueve'.split(' '), teen = 'diez once doce trece catorce quince'.split(' ');
    const accent = { dos: 'dós', tres: 'trés', seis: 'séis' };
    const two = x => x < 10 ? u[x] : x < 16 ? teen[x - 10] : x < 20 ? 'dieci' + (accent[u[x - 10]] || u[x - 10]) : x === 20 ? 'veinte' : x < 30 ? 'veinti' + (accent[u[x - 20]] || u[x - 20])
      : 'x x x treinta cuarenta cincuenta sesenta setenta ochenta noventa'.split(' ')[Math.floor(x / 10)] + (x % 10 ? ' y ' + u[x % 10] : '');
    const three = x => { const h = Math.floor(x / 100), r = x % 100;
      if (!h) return two(r);
      const hw = { 1: r ? 'ciento' : 'cien', 5: 'quinientos', 7: 'setecientos', 9: 'novecientos' }[h] || u[h] + 'cientos';
      return hw + (r ? ' ' + two(r) : ''); };
    const th = Math.floor(n / 1000), r = n % 1000;
    return th ? (th > 1 ? u[th] + ' ' : '') + 'mil' + (r ? ' ' + three(r) : '') : three(n);
  }
  const u = 'zéro un deux trois quatre cinq six sept huit neuf dix onze douze treize quatorze quinze seize'.split(' ');
  const two = x => {
    if (x <= 16) return u[x];
    const score = Math.floor(x / 20);   // 60-79 count in sixty, 80-99 in four twenties
    if (x >= 60) { const head = x >= 80 ? 'quatre-vingt' : 'soixante', rest = x >= 80 ? x - 80 : x - 60;
      if (rest === 0) return x === 80 ? 'quatre-vingts' : 'soixante';
      if (rest === 1 && x < 80) return 'soixante et un';
      if (rest === 11 && x < 80) return 'soixante et onze';
      return head + '-' + (rest <= 16 ? u[rest] : 'dix-' + u[rest - 10]); }
    if (x < 20) return 'dix-' + u[x - 10];
    const tens = { 2: 'vingt', 3: 'trente', 4: 'quarante', 5: 'cinquante' }[Math.floor(x / 10)], one = x % 10;
    void score;
    return one === 0 ? tens : one === 1 ? tens + ' et un' : tens + '-' + u[one];
  };
  const three = x => { const h = Math.floor(x / 100), r = x % 100; if (!h) return two(r);
    return (h > 1 ? u[h] + ' ' : '') + 'cent' + (h > 1 && !r ? 's' : '') + (r ? ' ' + two(r) : ''); };
  const th = Math.floor(n / 1000), r = n % 1000;
  return th ? (th > 1 ? u[th] + ' ' : '') + 'mille' + (r ? ' ' + three(r) : '') : three(n);
}

/* ---------- time ---------- */
function esTime(h, m) {
  let hh = h, mm = m, sign = 'y';
  if (m > 30) { hh = h % 12 + 1; mm = 60 - m; sign = 'menos'; }
  const hw = hh === 1 ? 'Es la una' : 'Son las ' + esNum(hh);
  const mw = mm === 0 ? '' : mm === 15 ? ' ' + sign + ' cuarto' : mm === 30 ? ' y media' : ' ' + sign + ' ' + esNum(mm);
  return hw + mw + '.';
}
function frTime(h, m) {   // 12-hour, hours 1-11 (noon and midnight left out)
  let hh = h, mm = m, sign = '';
  if (m > 30) { hh = h + 1; mm = 60 - m; sign = 'moins'; }
  const hw = hh === 1 ? 'une heure' : frNum(hh) + ' heures';
  const mw = mm === 0 ? '' : sign ? (mm === 15 ? ' moins le quart' : ' moins ' + frNum(mm)) : mm === 15 ? ' et quart' : mm === 30 ? ' et demie' : ' ' + frNum(mm);
  return 'Il est ' + hw + mw + '.';
}
const frHour24 = h => (h === 1 ? 'une' : h === 21 ? 'vingt et une' : frNum(h)) + (h === 1 ? ' heure' : ' heures');
const fr24 = (h, m) => 'Il est ' + frHour24(h) + (m ? ' ' + frNum(m) : '') + '.';
const ampm = (h, m) => `${h % 12 === 0 ? 12 : h % 12}:${String(m).padStart(2, '0')} ${h < 12 ? 'a.m.' : 'p.m.'}`;
const hhmm = (h, m) => `${h}:${String(m).padStart(2, '0')}`;

/* ---------- drawings ---------- */
function clockSvg(h, m, showHands, keyHands, size = 92) {
  const c = 50, R = 44;
  let b = `<circle cx="${c}" cy="${c}" r="${R}" fill="#fff" stroke="#222" stroke-width="2.5"/>`;
  for (let i = 1; i <= 12; i++) {
    const a = i * Math.PI / 6;
    b += `<text x="${(c + 34 * Math.sin(a)).toFixed(1)}" y="${(c - 34 * Math.cos(a) + 4).toFixed(1)}" font-size="10" text-anchor="middle" font-family="sans-serif" fill="#222">${i}</text>`;
  }
  for (let i = 0; i < 60; i++) if (i % 5) { const a = i * Math.PI / 30; b += `<line x1="${(c + 41 * Math.sin(a)).toFixed(1)}" y1="${(c - 41 * Math.cos(a)).toFixed(1)}" x2="${(c + 43 * Math.sin(a)).toFixed(1)}" y2="${(c - 43 * Math.cos(a)).toFixed(1)}" stroke="#666" stroke-width="1"/>`; }
  const ha = ((h % 12) + m / 60) * Math.PI / 6, ma = m * Math.PI / 30;
  const hands = col => `<line x1="${c}" y1="${c}" x2="${(c + 22 * Math.sin(ha)).toFixed(1)}" y2="${(c - 22 * Math.cos(ha)).toFixed(1)}" stroke="${col}" stroke-width="4" stroke-linecap="round"/>` +
    `<line x1="${c}" y1="${c}" x2="${(c + 33 * Math.sin(ma)).toFixed(1)}" y2="${(c - 33 * Math.cos(ma)).toFixed(1)}" stroke="${col}" stroke-width="2.5" stroke-linecap="round"/>`;
  if (showHands) b += hands('#222');
  if (keyHands) b += `<g class="ws-ans">${hands('#b03020')}</g>`;
  b += `<circle cx="${c}" cy="${c}" r="3" fill="#222"/>`;
  return `<svg class="gen-svg wl-clock" viewBox="0 0 100 100" role="img" aria-label="${showHands ? 'Clock showing ' + hhmm(h, m) : 'Blank clock'}" style="width:${size}px;height:${size}px" data-h="${h}" data-m="${m}">${b}</svg>`;
}
const SHAPES = ['circle', 'star', 'square', 'heart'];
function countSvg(n, shape) {
  const cols = 5, w = 130, cell = 24;
  let b = '';
  for (let i = 0; i < n; i++) {
    const x = 16 + (i % cols) * cell, y = 16 + Math.floor(i / cols) * cell;
    if (shape === 'circle') b += `<circle class="k5o" cx="${x}" cy="${y}" r="8" fill="none" stroke="#222" stroke-width="2"/>`;
    else if (shape === 'square') b += `<rect class="k5o" x="${x - 8}" y="${y - 8}" width="16" height="16" fill="none" stroke="#222" stroke-width="2"/>`;
    else if (shape === 'star') { const pts = []; for (let k = 0; k < 10; k++) { const a = k * Math.PI / 5 - Math.PI / 2, rr = k % 2 ? 4 : 9; pts.push(`${(x + rr * Math.cos(a)).toFixed(1)},${(y + rr * Math.sin(a)).toFixed(1)}`); }
      b += `<polygon class="k5o" points="${pts.join(' ')}" fill="none" stroke="#222" stroke-width="1.6"/>`; }
    else b += `<path class="k5o" d="M${x} ${y + 7} C${x - 12} ${y - 2} ${x - 5} ${y - 11} ${x} ${y - 4} C${x + 5} ${y - 11} ${x + 12} ${y - 2} ${x} ${y + 7}Z" fill="none" stroke="#222" stroke-width="1.8"/>`;
  }
  return `<svg class="gen-svg" viewBox="0 0 ${w} 58" role="img" aria-label="${n} things to count" style="width:1.35in">${b}</svg>`;
}
const crayonSvg = col => `<svg class="gen-svg" viewBox="0 0 90 22" role="img" aria-label="crayon" style="width:0.95in"><polygon points="70,3 88,11 70,19" fill="${col}" stroke="#222" stroke-width="1.5"/><rect x="4" y="3" width="66" height="16" rx="3" fill="${col}" stroke="#222" stroke-width="1.5" style="-webkit-print-color-adjust:exact;print-color-adjust:exact"/><line x1="14" y1="3" x2="14" y2="19" stroke="#222"/><line x1="58" y1="3" x2="58" y2="19" stroke="#222"/></svg>`;

/* ---------- settings ---------- */
const LANGS = [['es', 'Spanish'], ['fr', 'French']];
const LEVELS = [['k5', 'Novice, grades K-5'], ['novice', 'Novice (level 1)'], ['intermediate', 'Intermediate (level 2)'], ['advanced', 'Advanced (levels 3-4)']];
const L = (v, es, fr) => v.lang === 'es' ? es : fr;
function skillsFor(v) {
  const es = v.lang === 'es';
  if (v.level === 'k5') return [['count', 'Count and write 1 to 10'], ['colors', 'Color words'], ['days', 'Days of the week'], ['months', 'Months of the year'], ['clock', 'Clocks on the hour']];
  if (v.level === 'novice') return [['conj', 'Verb charts and sentences'], ['numbers', 'Numbers in words'], ['nummath', 'Math with number words'],
    ['colors', 'Colors that agree'], ['nation', es ? 'Ser and nationalities' : 'Être and nationalities'], ['articles', 'Articles'],
    ['possess', 'Possessive adjectives'], ['dates', 'Days, months and dates'], ['time', 'Telling time'], ...(es ? [['gustar', 'Gustar: me gusta, me gustan']] : [['time24', 'The 24-hour clock'], ['places', 'En, au, aux, à with places']]),
    ['vocab', 'Vocabulary by theme'], ['review', 'Mixed review']];
  if (v.level === 'intermediate') return [['conj', 'Verb charts and sentences'], ['pastmix', es ? 'Preterite or imperfect?' : 'Passé composé or imparfait?'],
    ['numbers', 'Numbers in words'], ['nummath', 'Math with number words'], ['dates', 'Days, months and dates'], ...(es ? [['time', 'Telling time']] : [['time24', 'The 24-hour clock'], ['places', 'En, au, aux, à with places']]),
    ['review', 'Mixed review']];
  return [['conj', 'Verb charts and sentences'], ['mood', 'Subjunctive or indicative?'], ['si', 'Si clauses'], ['review', 'Mixed review']];
}
const TENSES = {
  es: { novice: [['pres', 'Present'], ['ira', 'Ir a + infinitive (going to)']],
    intermediate: [['pres', 'Present'], ['pret', 'Preterite'], ['impf', 'Imperfect'], ['ira', 'Ir a + infinitive (going to)']],
    advanced: [['fut', 'Future'], ['cond', 'Conditional'], ['subj', 'Present subjunctive'], ['impsubj', 'Imperfect subjunctive']] },
  fr: { novice: [['pres', 'Present (présent)'], ['proche', 'Futur proche (aller + infinitive)']],
    intermediate: [['pres', 'Present (présent)'], ['pc', 'Passé composé'], ['impf', 'Imparfait'], ['proche', 'Futur proche (aller + infinitive)']],
    advanced: [['fut', 'Futur simple'], ['cond', 'Conditionnel'], ['subj', 'Subjonctif présent'], ['pqp', 'Plus-que-parfait']] },
};
const TNAME = { pres: 'present', pret: 'preterite', impf: 'imperfect', fut: 'future', cond: 'conditional', subj: 'present subjunctive', impsubj: 'imperfect subjunctive',
  ira: 'ir a + infinitive', pc: 'passé composé', pqp: 'plus-que-parfait', proche: 'futur proche' };
const FRTNAME = { pres: 'présent', impf: 'imparfait', fut: 'futur simple', cond: 'conditionnel', subj: 'subjonctif présent' };
const tname = (lang, t) => lang === 'fr' && FRTNAME[t] ? FRTNAME[t] : TNAME[t];
const GLABEL = {
  es: { reg: 'Regular -ar, -er, -ir verbs', core: 'Ser, estar, tener, ir', stem: 'Stem-changing verbs', yogo: 'Irregular yo forms (tengo, hago, pongo...)',
    irr: 'Irregular verbs', refl: 'Reflexive verbs (levantarse...)', spell: 'Spelling changes (-car, -gar, -zar)', other: 'Verbs irregular elsewhere, regular here', mix: 'A mix of all of these' },
  fr: { er: 'Regular -er verbs', irre: 'Regular -ir and -re verbs', big: 'Être, avoir, aller, faire', irr: 'Irregular verbs', refl: 'Reflexive verbs (se lever...)',
    avoir: 'Verbs with avoir', etre: 'Verbs with être (agreement)', mix: 'A mix of all of these' },
};
const GSPECIAL = { es: { pret: { stem: '-ir stem changers (pidió, durmió)', irr: 'Irregular (fui, hice, tuve...)' }, impf: { irr: 'Ser, ir, ver (the only three irregulars)' },
  fut: { reg: 'Regular stems', irr: 'Irregular stems (tendr-, har-, dir-...)' }, subj: { irr: 'Dar, estar, haber, ir, saber, ser', yogo: 'From irregular yo forms (tenga, haga...)' } },
  fr: { fut: { irre: 'Regular -ir and -re, and stems that keep the infinitive', irr: 'Irregular stems (ser-, aur-, ir-, fer-...)' }, impf: { irr: 'Irregular verbs (être is ét-)' } } };
const groupKey = (lang, t) => lang === 'es' ? (t === 'cond' ? 'fut' : t === 'ira' ? null : t) : (t === 'cond' ? 'fut' : t === 'pqp' ? 'pc' : t === 'proche' ? null : t);
function groupsFor(v) {
  const k = groupKey(v.lang, v.tense);
  if (!k) return [['mix', 'Regular and irregular verbs']];
  const gs = (v.lang === 'es' ? ES : FR).groups[k];
  return Object.keys(gs).map(g => [g, (GSPECIAL[v.lang][k] || {})[g] || GLABEL[v.lang][g]]).concat([['mix', GLABEL[v.lang].mix]]);
}
function verbPool(lang, tense, grp) {
  const B = lang === 'es' ? ES : FR, k = groupKey(lang, tense);
  if (!k) {   // ir a / futur proche: present-tense regulars and irregulars, no reflexives
    const g = B.groups.pres;
    return [...new Set(list(lang === 'es' ? g.reg + ' ' + g.irr : g.er + ' ' + g.irre + ' ' + g.irr + ' ' + g.big))];
  }
  const gs = B.groups[k];
  if (grp === 'mix' || !gs[grp]) return [...new Set(Object.keys(gs).filter(x => x !== 'refl').flatMap(x => list(gs[x])))];
  return list(gs[grp]);
}
const THEMES = [['family', 'Family'], ['food', 'Food'], ['school', 'School things'], ['subjects', 'School subjects'], ['body', 'The body'], ['clothes', 'Clothes'],
  ['house', 'The house'], ['animals', 'Animals'], ['weather', 'Weather']];
const RANGES = { novice: { es: [['20', '0 to 20'], ['100', '21 to 100, with counting by tens']], fr: [['20', '0 to 20'], ['69', '21 to 69'], ['99', '70 to 99, with the math (soixante-dix, quatre-vingts)']] },
  intermediate: { es: [['100', '21 to 100, with counting by tens'], ['big', '100 to 9,999']], fr: [['99', '70 to 99, with the math'], ['big', '100 to 9,999']] } };
// item counts: [fewer, standard, more]
const SIZES = { count: [6, 8, 10], colorsk: [6, 8, 10], days: [3, 4, 5], months: [6, 9, 12], clock: [4, 6, 8],
  conjboth: [8, 10, 12], conjsent: [12, 16, 20], conjchart: [3, 4, 6], numbers: [10, 14, 20], nummath: [8, 12, 16], colors: [10, 12, 16], nation: [6, 8, 10],
  articles: [12, 18, 24], part: [8, 12, 16], possess: [10, 12, 16], dates: [6, 8, 10], time: [6, 8, 10], time24: [6, 8, 10], gustar: [8, 10, 14],
  places: [8, 12, 14], vocab: [8, 10, 12], review: [12, 15, 20], pastmix: [10, 12, 16], mood: [8, 12, 15], si: [6, 8, 10] };
const sizeKey = v => v.skill === 'conj' ? 'conj' + v.fmt : v.skill === 'colors' && v.level === 'k5' ? 'colorsk' : v.skill === 'articles' && v.art === 'part' ? 'part' : v.skill;
const CI = { s: 0, m: 1, l: 2 };
const nOf = v => SIZES[sizeKey(v)][CI[v.count] ?? 1];

/* ---------- subjects for sentences ---------- */
function subjects(lang, opt = {}) {
  if (lang === 'es') return ES.subj.filter(s => (opt.vos || s[1] !== 4) && !(opt.no || []).includes(s[1]))
    .map(s => ({ t: s[0], p: s[1], name: !!s[2], g: '' }));
  return FR.subj.filter(s => !(opt.compound && s[4]) && !(opt.no || []).includes(s[1])).map(s => ({ t: s[0], p: s[1], g: s[2], name: !!s[3] }));
}
const FRPRO = { je: 'je', tu: 'tu', il: 'il', elle: 'elle', on: 'on', Marie: 'elle', Paul: 'il', nous: 'nous', 'Marie et moi': 'nous', vous: 'vous',
  ils: 'ils', elles: 'elles', 'mes amis': 'ils', 'Léo et Sophie': 'ils', 'Julie et Léa': 'elles' };
// "que" + subject in French, with elision (qu'il, que j')
function frQue(word, subj, ans) {
  if (subj.t === 'je' && vowel(ans)) return word + ' j\'';
  if (/^(il|elle|ils|elles|on)$/.test(subj.t)) return word.replace(/que$/, 'qu\'').replace(/^Si$/, subj.t.startsWith('i') ? 'S\'' : 'Si ') + (word === 'Si' && !subj.t.startsWith('i') ? '' : '') + subj.t;
  return word + ' ' + subj.t;
}
// the words in front of the blank; joinTight = no space before the blank (after j' or qu')
function lead(lang, cue, subj, ans) {
  if (lang === 'fr' && subj.t === 'je' && vowel(ans)) return cue ? `${cue}, j'` : 'J\'';
  const s = cue ? `${cue}, ${subj.t}` : cap(subj.t);
  return s + ' ';
}
const blankFor = a => blank(a, Math.max(4.5, Math.min(12, 0.6 * a.length + 1.6)));

/* ---------- conjugation sentences ---------- */
const CUES = {
  es: { pret: ['Ayer', 'Anoche', 'El sábado pasado', 'La semana pasada'], impf: ['Cuando éramos niños', 'En la escuela primaria'],
    fut: ['Mañana', 'El año que viene', 'En el futuro'], cond: ['Con más tiempo', 'En un mundo ideal', 'Con un millón de dólares'],
    ira: ['Mañana', 'Este fin de semana', 'Esta noche', 'El sábado'] },
  fr: { pc: ['Hier', 'Samedi dernier', 'La semaine dernière', 'Le week-end dernier'], impf: ['Quand nous étions petits', 'À l\'école primaire'],
    fut: ['Demain', 'L\'année prochaine', 'En 2050'], cond: ['Avec plus de temps', 'Dans un monde idéal', 'Avec un million d\'euros'],
    proche: ['Demain', 'Ce week-end', 'Ce soir', 'Samedi'], pqp: ['Quand le film a commencé', 'Quand la prof est arrivée', 'Avant le dîner hier soir'] },
};
// triggers: text, mood (s or i), reason, persons it cannot take (the speaker)
const TRIG = {
  es: { subj: [['Es importante que', 's', 'impersonal expression'], ['Es necesario que', 's', 'impersonal expression'], ['Ojalá que', 's', 'ojalá (hope)'],
    ['Quiero que', 's', 'wish', [0]], ['Espero que', 's', 'wish', [0]], ['Mis padres quieren que', 's', 'wish', [5]], ['Dudo que', 's', 'doubt', [0]],
    ['No creo que', 's', 'doubt', [0]], ['Me alegra que', 's', 'emotion', [0]], ['Es posible que', 's', 'impersonal expression'], ['Recomiendo que', 's', 'recommendation', [0]]],
    ind: [['Creo que', 'i', 'belief (certain)'], ['Es verdad que', 'i', 'certainty'], ['Sé que', 'i', 'certainty', [0]], ['Es obvio que', 'i', 'certainty'],
      ['Pienso que', 'i', 'belief (certain)'], ['No hay duda de que', 'i', 'certainty']],
    impsubj: [['Era importante que', 's', 'impersonal expression'], ['Mis padres querían que', 's', 'wish', [5]], ['La profesora quería que', 's', 'wish', [2]],
      ['Ojalá que', 's', 'ojalá (hope)'], ['Me alegró que', 's', 'emotion', [0]]] },
  fr: { subj: [['Il faut que', 's', 'necessity'], ['Il est important que', 's', 'necessity'], ['Je veux que', 's', 'wish', [0]], ['Mes parents veulent que', 's', 'wish', [5]],
    ['Je doute que', 's', 'doubt', [0]], ['Je ne pense pas que', 's', 'doubt', [0]], ['Je regrette que', 's', 'emotion', [0]], ['C\'est dommage que', 's', 'emotion'],
    ['Il est possible que', 's', 'possibility']],
    ind: [['Je pense que', 'i', 'belief (certain)'], ['Je sais que', 'i', 'certainty', [0]], ['Il est vrai que', 'i', 'certainty'], ['Il est certain que', 'i', 'certainty'],
      ['Je crois que', 'i', 'belief (certain)'], ['Il est évident que', 'i', 'certainty']] },
};
function comp(lang, inf, p, r) {
  const v = (lang === 'es' ? ES : FR).verbs[inf];
  if (v.cp) return r.pick(v.cp)[p >= 3 ? 1 : 0];
  return r.pick(v.c);
}
// one sentence item: tense, verb, chosen subject; returns {html, q, a, ...}
function sentence(lang, tense, inf, r, opt) {
  const compound = lang === 'fr' && (tense === 'pc' || tense === 'pqp');
  let trig = null;
  if (tense === 'subj' || tense === 'impsubj' || opt.trig) trig = opt.trig || r.pick(TRIG[lang][tense === 'impsubj' ? 'impsubj' : 'subj']);
  const subs = subjects(lang, { vos: opt.vos, compound, no: trig && trig[3] });
  const subj = r.pick(subs);
  const realTense = opt.trig ? (trig[1] === 's' ? 'subj' : 'pres') : tense;
  const a = form(lang, inf, realTense, subj.p, subj.g);
  const c = comp(lang, inf, subj.p, r);
  let pre, mid = '', post = c;
  if (trig) pre = lang === 'fr' ? frQue(trig[0], subj, a) + (subj.t === 'je' && vowel(a) ? '' : ' ') : `${trig[0]} ${subj.t} `;
  else {
    const cues = CUES[lang][tense], cue = opt.cue || (cues ? r.pick(cues) : '');
    pre = lead(lang, cue, subj, a);
    if (tense === 'impf' && !opt.cue) { if (lang === 'es') mid = 'siempre '; else post = 'toujours ' + c; }
  }
  if (opt.cue && opt.cueAdv) { if (lang === 'es') mid = opt.cueAdv + ' '; else post = opt.cueAdv + ' ' + c; }
  const text = `${pre}${mid}___ (${inf}) ${post}.`;
  const html = `${esc(pre)}${esc(mid)}${blankFor(a)} (${esc(inf)}) ${esc(post)}.`;
  return { k: 'conj', lang, t: realTense, inf, p: subj.p, g: subj.g, q: text, a, html, trig };
}

/* ---------- conjugation sheet ---------- */
const PLABEL = { es: ['yo', 'tú', 'él / ella / usted', 'nosotros', 'vosotros', 'ellos / ellas / ustedes'], fr: ['je (j\')', 'tu', 'il / elle / on', 'nous', 'vous', 'ils / elles'] };
function chart(lang, tense, verbs, vos, items) {
  const persons = lang === 'es' && !vos ? [0, 1, 2, 3, 5] : [0, 1, 2, 3, 4, 5];
  const out = [];
  for (let i = 0; i < verbs.length; i += 3) {
    const vs = verbs.slice(i, i + 3);
    const rows = persons.map(p => [esc(PLABEL[lang][p]), ...vs.map(inf => { const a = form(lang, inf, tense, p, ''); items.push({ k: 'conj', lang, t: tense, inf, p, g: '', q: `${inf}, ${PLABEL[lang][p]} (${tname(lang, tense)})`, a }); return blankFor(a); })]);
    out.push(table(['', ...vs.map(x => `<i>${esc(x)}</i>`)], rows));
  }
  return out.join('');
}
const HOW = {
  es: { pres: 'Drop -ar, -er or -ir and add the ending for the subject: hablo, hablas, habla, hablamos, habláis, hablan.',
    ira: 'Use ir in the present (voy, vas, va, vamos, vais, van), then a, then the infinitive: voy a bailar.',
    pret: 'Regular -ar endings: -é, -aste, -ó, -amos, -asteis, -aron. Regular -er and -ir endings: -í, -iste, -ió, -imos, -isteis, -ieron.',
    impf: '-ar verbs take -aba endings (hablaba); -er and -ir verbs take -ía endings (comía). Only ser, ir and ver are irregular.',
    fut: 'Add -é, -ás, -á, -emos, -éis, -án to the whole infinitive (hablaré), or to an irregular stem (tendré).',
    cond: 'Add -ía, -ías, -ía, -íamos, -íais, -ían to the whole infinitive (hablaría), or to the same irregular stems as the future (tendría).',
    subj: 'Start from the yo form of the present, drop the -o and switch the vowel: -ar verbs take e endings (hable), -er and -ir verbs take a endings (coma).',
    impsubj: 'Start from the ellos form of the preterite, drop -ron and add -ra, -ras, -ra, -ramos, -rais, -ran (hablaron: hablara, habláramos).' },
  fr: { pres: 'Drop -er and add -e, -es, -e, -ons, -ez, -ent (je parle). -ir verbs like finir add -is, -is, -it, -issons, -issez, -issent. -re verbs add -s, -s, -, -ons, -ez, -ent.',
    proche: 'Use aller in the present (vais, vas, va, allons, allez, vont), then the infinitive: je vais danser.',
    pc: 'Use avoir or être in the present, then the past participle (parlé, fini, vendu). With être, the participle agrees with the subject: elles sont allées.',
    impf: 'Take the nous form of the present, drop -ons and add -ais, -ais, -ait, -ions, -iez, -aient (nous parlons: je parlais). Only être is irregular (j\'étais).',
    fut: 'Add -ai, -as, -a, -ons, -ez, -ont to the infinitive (drop the final e of -re verbs), or to an irregular stem (je serai, j\'irai).',
    cond: 'Use the future stem with the imparfait endings: -ais, -ais, -ait, -ions, -iez, -aient (je parlerais, je serais).',
    subj: 'Take the ils form of the present, drop -ent and add -e, -es, -e, -ions, -iez, -ent (ils finissent: que je finisse). Nous and vous look like the imparfait.',
    pqp: 'Use avoir or être in the imparfait, then the past participle (j\'avais fini, elle était partie). It shows an action that happened before another past action.' },
};
const MISTAKES = {
  pres: 'Using the infinitive instead of a conjugated form, and missing the written accents on vosotros forms (habláis).',
  ira: 'Leaving out the a (voy bailar) or conjugating the second verb (voy a bailo).',
  proche: 'Conjugating the second verb (je vais danse) instead of keeping it as an infinitive.',
  pret: 'Dropping the accent on -é and -ó (hablo is present, habló is past), and giving the strong preterites (tuve, hice) accents they do not have.',
  impf: 'Forgetting the accent in the nosotros form of -ar verbs (hablábamos) and on every -ía ending.',
  fut: 'Putting the ending on the stem instead of the whole infinitive, and missing the accents.',
  cond: 'Mixing up the conditional and the imperfect: hablaría (would speak) and hablaba (used to speak) look alike.',
  subj: 'Using the present indicative after a trigger, and forgetting the spelling changes (busque, llegue, empiece).',
  impsubj: 'Starting from the infinitive instead of the ellos preterite, and forgetting the accent on the nosotros form (tuviéramos).',
  pc: 'Choosing avoir for a verb of motion (j\'ai allé) and forgetting agreement with être (elles sont allées).',
  pqp: 'Using the present of avoir or être (the passé composé) instead of the imparfait (j\'avais, j\'étais).',
};
const FRMIST = { pres: 'Pronouncing or writing the silent endings wrong, and forgetting the spelling changes (nous mangeons, nous commençons).',
  impf: 'Using the wrong stem: it comes from the nous form of the present (nous faisons: je faisais).', fut: 'Leaving the final e on -re verbs (je prendrai, not je prenderai).',
  cond: 'Mixing up the conditionnel (je parlerais) and the imparfait (je parlais).', subj: 'Using the indicative after il faut que, and missing irregular forms (que je sois, que j\'aille, que je fasse).' };

function makeConj(v, r) {
  const lang = v.lang, tense = v.tense, n = nOf(v), pool = verbPool(lang, tense, v.verbs);
  const items = [], parts = [], vos = v.vosotros;
  const nChart = v.fmt === 'chart' ? n : v.fmt === 'both' ? { s: 2, m: 3, l: 6 }[v.count] : 0;
  const nSent = v.fmt === 'chart' ? 0 : n;
  const chartVerbs = r.sample(pool, Math.min(nChart, pool.length));
  const sentPool = pool.filter(x => !(lang === 'es' ? ES : FR).verbs[x].chartOnly);
  // worked example from a verb and subject the sheet does not use
  const exVerb = r.pick(sentPool.filter(x => !chartVerbs.includes(x))) || sentPool[0];
  const ex = sentence(lang, tense, exVerb, r, { vos });
  if (chartVerbs.length) parts.push(part(v.fmt === 'chart' ? 'Charts' : 'Part 1: Complete the charts', chart(lang, tense, chartVerbs, vos, items)));
  if (nSent) {
    const order = r.shuffle(sentPool);
    const sents = r.distinct(nSent, () => sentence(lang, tense, order[Math.floor(r.next() * order.length)], r, { vos }), s => s.q).filter(s => s.q !== ex.q);
    // keep each sentence verb different from its neighbour where possible
    for (const s of sents) items.push(s);
    parts.push(part(v.fmt === 'chart' ? '' : (chartVerbs.length ? 'Part 2: ' : '') + 'Complete each sentence', fill(sents.map(s => s.html))));
  }
  parts.unshift(part('', example(ex.html.replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a)}</b>`), esc(HOW[lang][tense]))));
  const tn = tname(lang, tense), gl = groupsFor(v).find(g => g[0] === v.verbs);
  return {
    title: `${cap(tn)}: ${gl ? gl[1] : 'verbs'}`, level: `${L(v, 'Spanish', 'French')}, ${LEVELS.find(x => x[0] === v.level)[1]}`,
    ican: `I can write the ${tn} forms of ${gl && v.verbs !== 'mix' ? gl[1].charAt(0).toLowerCase() + gl[1].slice(1) : 'regular and irregular verbs'} and use them in sentences.`,
    directions: (chartVerbs.length ? 'Fill in each chart with the right form for each subject. ' : '') + (nSent ? `Write the ${tn} form of the verb in parentheses on each line.` : '') + ' Include every accent.',
    minutes: 20 + (v.count === 'l' ? 5 : 0), materials: 'pencil', parts, items,
    mistakes: (lang === 'fr' && FRMIST[tense]) || MISTAKES[tense],
    notes: 'Press New sheet for new verbs and subjects at the same setting. ' + (lang === 'es' ? (vos ? 'Vosotros forms are included (Spain); turn them off for Latin American usage. ' : 'Vosotros forms are left out; turn them on for Spain. ') : '') +
      (tense === 'pc' || tense === 'pqp' ? 'When the subject\'s gender is not known (je, tu, nous, vous), the key shows the agreement in parentheses: allé(e)s. ' : '') +
      (tense === 'subj' || tense === 'impsubj' ? 'Every sentence starts with a trigger that needs the subjunctive, and the subject after que is never the speaker of a wish or doubt. ' : '') +
      'A good follow-up: students read their sentences aloud to a partner, who checks the form against the chart.',
  };
}

/* ---------- pastmix: signal words decide the tense ---------- */
const PAST = {
  es: { a: { t: 'pret', name: 'preterite', cues: [['Ayer', 'one finished event'], ['Anoche', 'one finished event'], ['El sábado pasado', 'a specific time'], ['Una vez', 'it happened one time']] },
    b: { t: 'impf', name: 'imperfect', cues: [['Cuando éramos niños', 'siempre', 'a habit in the past'], ['En la escuela primaria', 'todos los días', 'a repeated action'], ['Antes', 'a menudo', 'a habit in the past']] } },
  fr: { a: { t: 'pc', name: 'passé composé', cues: [['Hier', 'one finished event'], ['Samedi dernier', 'a specific time'], ['La semaine dernière', 'a specific time'], ['Une fois', 'it happened one time']] },
    b: { t: 'impf', name: 'imparfait', cues: [['Quand nous étions petits', 'toujours', 'a habit in the past'], ['À l\'école primaire', 'souvent', 'a repeated action'], ['Autrefois', 'toujours', 'a habit in the past']] } },
};
function pastItem(lang, r, vos, pool) {
  const side = r.chance(0.5) ? 'a' : 'b', P = PAST[lang][side], cue = r.pick(P.cues), inf = r.pick(pool);
  const s = sentence(lang, P.t, inf, r, { vos, cue: cue[0], cueAdv: side === 'b' ? (lang === 'es' && cue[1] !== 'siempre' ? null : cue[1]) : null });
  let { html, q } = s;
  if (side === 'b' && lang === 'es' && cue[1] !== 'siempre') { html = html.replace(/\.$/, ` ${esc(cue[1])}.`); q = q.replace(/\.$/, ` ${cue[1]}.`); }
  const why = `${P.name}: ${side === 'a' ? cue[1] : cue[2]} (${side === 'a' ? cue[0].toLowerCase() : cue[1]})`;
  return { ...s, html: html + ` <span class="wl-why">Why? ${blank(why, 13)}</span>`, q, why, side, cue: cue[0] };
}
function makePast(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es';
  const pool = es ? [...new Set(list(ES.groups.pret.reg + ' ' + ES.groups.pret.irr + ' ' + ES.groups.pret.stem))] : list(FR.groups.pc.avoir + ' ' + FR.groups.pc.etre);
  const ex = pastItem(lang, r, v.vosotros, pool);
  const its = r.distinct(n, () => pastItem(lang, r, v.vosotros, pool), s => s.q).filter(s => s.q !== ex.q);
  const items = its.map(s => ({ k: 'past', lang, t: s.t, inf: s.inf, p: s.p, g: s.g, q: s.q, a: s.a, side: s.side, cue: s.cue }));
  const A = PAST[lang].a, B = PAST[lang].b;
  return {
    title: es ? 'Preterite or Imperfect? Signal Words' : 'Passé composé or Imparfait? Signal Words', level: `${L(v, 'Spanish', 'French')}, Intermediate`,
    ican: `I can choose the ${A.name} or the ${B.name} from the signal words in a sentence and explain why.`,
    directions: `Read the signal words in each sentence. Write the verb in the ${A.name} or the ${B.name}, then write which tense you chose and why.`,
    minutes: 25, materials: 'pencil', items,
    parts: [part('', example(ex.html.replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a)}</b>`).replace(/<span class="wl-why">[^]*$/, ''), esc(`${A.name}: one finished event or a specific time (${A.cues.map(c => c[0].toLowerCase()).join(', ')}). ${cap(B.name)}: habits and repeated actions (${B.cues.map(c => c[1]).join(', ')}).`))),
      part('Practice', fill(its.map(s => s.html)))],
    mistakes: 'Choosing by the verb instead of the signal words, and dropping the accents on preterite forms or the imperfect -ía endings.',
    notes: `Signal words used: ${A.cues.map(c => c[0]).join(', ')} for the ${A.name}; ${B.cues.map(c => c[1]).join(', ')} for the ${B.name}. A reason that names the signal word is enough.`,
  };
}

/* ---------- mood: subjunctive or indicative ---------- */
function makeMood(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es';
  const g = (es ? ES : FR).groups.subj;
  const pool = [...new Set(Object.keys(g).flatMap(k => list(g[k])))].filter(x => !(es ? ES : FR).verbs[x].chartOnly);
  const all = TRIG[lang].subj.concat(TRIG[lang].ind);
  const mk = () => { const trig = r.chance(0.55) ? r.pick(TRIG[lang].subj) : r.pick(TRIG[lang].ind);
    const s = sentence(lang, 'pres', r.pick(pool), r, { vos: v.vosotros, trig });
    const why = (trig[1] === 's' ? 'subjunctive: ' : 'indicative: ') + trig[2];
    return { ...s, k: 'mood', why, html: s.html + ` <span class="wl-why">Mood and reason: ${blank(why, 13)}</span>` }; };
  const ex = mk();
  const its = r.distinct(n, mk, s => s.q).filter(s => s.q !== ex.q);
  return {
    title: es ? 'Indicative or Subjunctive?' : 'Subjonctif ou indicatif?', level: `${L(v, 'Spanish', 'French')}, Advanced`,
    ican: 'I can choose the subjunctive or the indicative after a trigger and explain my choice.',
    directions: 'Write the verb in the present subjunctive or the present indicative. Then name the mood and the reason (wish, emotion, doubt, an impersonal expression, or certainty).',
    minutes: 25, materials: 'pencil', items: its.map(s => ({ k: 'mood', lang, t: s.t, inf: s.inf, p: s.p, g: s.g, q: s.q, a: s.a, trig: s.trig[0], why: s.why })),
    parts: [part('', example(ex.html.replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a)}</b>`).replace(/<span class="wl-why">[^]*$/, ''),
      esc(`${ex.trig[0]} takes the ${ex.trig[1] === 's' ? 'subjunctive' : 'indicative'} (${ex.trig[2]}). ` + (es ? 'Certainty (creo que, es verdad que) takes the indicative; doubt and denial (no creo que, dudo que) take the subjunctive.' : 'Certainty (je pense que, il est vrai que) takes the indicative; doubt (je ne pense pas que, je doute que) takes the subjonctif.')))),
      part('Practice', fill(its.map(s => s.html)))],
    mistakes: es ? 'Treating creo que like no creo que, and using the subjunctive after es verdad que.' : 'Treating je pense que like je ne pense pas que, and using the indicative after il faut que.',
    notes: 'Triggers on this sheet: ' + all.map(t => t[0]).join(', ') + '. The subject after a wish, doubt or emotion that starts with I is never I.',
  };
}

/* ---------- si clauses ---------- */
const SIB = {
  es: { cond: [['tener', 'más tiempo'], ['tener', 'mucho dinero'], ['ganar', 'la lotería', 'reg'], ['vivir', 'en la playa'], ['saber', 'hablar japonés'], ['estar', 'de vacaciones'], ['poder', 'volar', 0, 1]],
    res: [['viajar', 'por el mundo'], ['comprar', 'una casa grande'], ['aprender', 'a bailar salsa'], ['escribir', 'un libro'], ['ayudar', 'a los demás'],
      ['comer', 'en restaurantes elegantes'], ['visitar', 'a la familia'], ['dormir', 'hasta tarde'], ['hacer', 'un viaje a Perú'], ['tener', 'un perro']] },
  fr: { cond: [['avoir', 'plus de temps'], ['avoir', 'beaucoup d\'argent'], ['gagner', 'au loto'], ['habiter', 'près de la mer'], ['savoir', 'parler japonais'], ['être', 'en vacances'], ['pouvoir', 'voler', 0, 1]],
    res: [['voyager', 'partout dans le monde'], ['acheter', 'une grande maison'], ['apprendre', 'à danser'], ['écrire', 'un livre'], ['aider', 'les autres'],
      ['manger', 'au restaurant'], ['rendre', 'visite à la famille'], ['dormir', 'jusqu\'à midi'], ['faire', 'le tour du monde'], ['avoir', 'un chien']] },
};
// verbs used only here, regular: register them so the rule engines can find them
ES.verbs.ganar = ES.verbs.ganar || { c: ['la lotería'] };
ES.verbs.viajar = ES.verbs.viajar || { c: ['por el mundo'] };
function siItem(lang, type, r, vos) {
  const es = lang === 'es', B = SIB[lang];
  const c = r.pick(B.cond.filter(x => type === 'unreal' || !x[3])), res = r.pick(B.res.filter(x => x[0] !== c[0]));
  const subj = r.pick(subjects(lang, { vos, compound: false }).filter(s => s.t !== 'on'));
  const t1 = type === 'unreal' ? (es ? 'impsubj' : 'impf') : 'pres', t2 = type === 'unreal' ? 'cond' : 'fut';
  const a1 = form(lang, c[0], t1, subj.p), a2 = form(lang, res[0], t2, subj.p);
  let pre1, pre2;
  if (es) { pre1 = `Si ${subj.t} `; pre2 = ''; }
  else {
    const pro = FRPRO[subj.t];
    pre1 = subj.t === 'je' && vowel(a1) ? 'Si j\'' : /^ils?$/.test(subj.t) ? `S'${subj.t} ` : `Si ${subj.t} `;
    pre2 = pro === 'je' && vowel(a2) ? 'j\'' : pro + ' ';
  }
  const q = `${pre1}___ (${c[0]}) ${c[1]}, ${pre2}___ (${res[0]}) ${res[1]}.`;
  const html = `${esc(pre1)}${blankFor(a1)} (${esc(c[0])}) ${esc(c[1])}, ${esc(pre2)}${blankFor(a2)} (${esc(res[0])}) ${esc(res[1])}.`;
  return { k: 'si', lang, type, p: subj.p, c1: c[0], c2: res[0], t1, t2, q, a: `${a1} ... ${a2}`, a1, a2, html };
}
function makeSi(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es';
  const typ = () => v.sitype === 'mix' ? (r.chance(0.5) ? 'real' : 'unreal') : v.sitype;
  const ex = siItem(lang, typ(), r, v.vosotros);
  const its = r.distinct(n, () => siItem(lang, typ(), r, v.vosotros), s => s.q).filter(s => s.q !== ex.q);
  const rule = es ? 'Real: si + present, then the future (Si tengo tiempo, viajaré). Hypothetical: si + imperfect subjunctive, then the conditional (Si tuviera tiempo, viajaría).'
    : 'Real: si + présent, then the futur (Si j\'ai le temps, je voyagerai). Hypothetical: si + imparfait, then the conditionnel (Si j\'avais le temps, je voyagerais).';
  const exHtml = ex.html.replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a1)}</b>`).replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a2)}</b>`);
  return {
    title: v.sitype === 'real' ? 'Si Clauses: Real Conditions' : v.sitype === 'unreal' ? (es ? 'Si yo fuera: Hypothetical Si Clauses' : 'Si j\'avais: Hypothetical Si Clauses') : 'Si Clauses: Real and Hypothetical',
    level: `${L(v, 'Spanish', 'French')}, Advanced`,
    ican: 'I can complete si clauses with the right pair of tenses.',
    directions: 'Write both verbs in the right tenses. ' + (v.sitype === 'mix' ? 'Decide first: is the condition real and likely, or hypothetical? ' : '') + 'Include every accent.',
    minutes: 20, materials: 'pencil', items: its.map(s => ({ k: 'si', lang, type: s.type, p: s.p, c1: s.c1, c2: s.c2, t1: s.t1, t2: s.t2, q: s.q, a: s.a })),
    parts: [part('', example(exHtml, esc(rule))), part('Practice', fill(its.map(s => s.html)))],
    mistakes: es ? 'Putting the conditional after si (si tendría). Si never takes the conditional or the present subjunctive.' : 'Putting the conditionnel or the futur after si (si j\'aurais). After si, use the présent or the imparfait.',
    notes: 'Both clauses share one subject, so the second verb matches the first. ' + (v.sitype === 'mix' ? 'Real and hypothetical items are mixed; some conditions could be read either way, so accept the real pair for a likely condition and the hypothetical pair for an unlikely one if a student explains it. The key shows the type this sheet chose.' : ''),
  };
}

/* ---------- numbers ---------- */
function numRange(v, r) {
  const k = v.range;
  if (k === '20') return r.int(0, 20);
  if (k === '69') return r.int(21, 69);
  if (k === '99') return r.int(70, 99);
  if (k === '100') return r.int(21, 100);
  return r.chance(0.5) ? r.int(100, 999) : r.int(1000, 9999);
}
function logic(n) { return n < 80 ? `60 + ${n - 60}` : n === 80 ? '4 × 20' : `4 × 20 + ${n - 80}`; }
function makeNumbers(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', items = [], parts = [];
  const fmtN = x => x >= 1000 ? Gen.m.fmt(x, 0) : String(x);
  const nums = r.distinct(n + 1, () => numRange(v, r));
  const ex = nums.pop();
  if (v.range === '100' || (!es && v.range === '69')) {   // counting by tens
    const tens = es ? [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] : [0, 10, 20, 30, 40, 50, 60];
    const hide = new Set(r.sample(tens.slice(1), es ? 5 : 3));
    const cells = tens.map(t => hide.has(t) ? (items.push({ k: 'num', lang, n: t, q: `tens ${t}`, a: num(lang, t) }), `${t}: ${blankFor(num(lang, t))}`) : `${t}: <i>${num(lang, t)}</i>`);
    parts.push(part('Part 1: Count by tens', `<p class="wl-line">${cells.join(' · ')}</p>`));
  }
  const words = nums.slice(0, Math.ceil(n * 0.7)), back = nums.slice(words.length);
  const logicOn = !es && v.range === '99';
  parts.push(part(`${parts.length ? 'Part 2: ' : ''}Write each number in words`, fill(words.map(x => {
    const a = num(lang, x);
    items.push({ k: 'num', lang, n: x, q: `words ${x}`, a });
    if (logicOn) { items.push({ k: 'logic', n: x, q: `math ${x}`, a: logic(x) }); return `<b>${x}</b> = ${blank(logic(x), 6)} : ${blankFor(a)}`; }
    return `<b>${fmtN(x)}</b> ${blankFor(a)}`;
  }), logicOn ? 1 : 2)));
  parts.push(part('Now write the numeral', fill(back.map(x => { items.push({ k: 'numr', lang, n: x, q: `numeral ${x}`, a: fmtN(x) }); return `<i>${esc(num(lang, x))}</i> = ${blank(fmtN(x), 3)}`; }), 2, words.length + 1)));
  const exLine = logicOn ? `<b>${ex}</b> = ${logic(ex)} : <b>${num(lang, ex)}</b>` : `<b>${fmtN(ex)}</b> = <b>${esc(num(lang, ex))}</b>`;
  const how = es ? (v.range === 'big' ? 'Hundreds: ciento (but cien for exactly 100), doscientos, quinientos, setecientos, novecientos. Thousands: mil, dos mil (mil never takes un or an s).' : '16 to 29 are one word (dieciséis, veintiuno, veintidós). From 31 on, join tens and ones with y: treinta y uno.')
    : v.range === '99' ? '70 is 60 + 10 (soixante-dix), 80 is 4 × 20 (quatre-vingts), 90 is 4 × 20 + 10 (quatre-vingt-dix). 71 is soixante et onze; 81 and 91 have no et.'
      : v.range === 'big' ? 'Cent takes an s only when it ends the number and is multiplied (deux cents, deux cent trois). Mille never takes an s. Quatre-vingts keeps its s only at the end.'
        : 'Join tens and ones with a hyphen (vingt-deux), but use et for 21, 31, 41, 51 and 61 (vingt et un).';
  parts.unshift(part('', example(exLine, esc(how))));
  const rng = (RANGES[v.level][lang] || []).find(x => x[0] === v.range);
  return {
    title: `${es ? 'Números' : 'Les nombres'}: ${rng ? rng[1] : ''}`, level: `${L(v, 'Spanish', 'French')}, ${LEVELS.find(x => x[0] === v.level)[1]}`,
    ican: 'I can write numbers in words and read number words as numerals.',
    directions: 'Write each number in words, with the right accents and hyphens. Then write the numeral for each number word.',
    minutes: 20, materials: 'pencil', parts, items,
    mistakes: es ? 'Writing veinte y uno for veintiuno, missing the accents on dieciséis, veintidós, veintitrés and veintiséis, and writing cinco cientos for quinientos.'
      : 'Writing soixante-onze for soixante et onze, adding et to 81 and 91, and putting an s on quatre-vingt when another number follows.',
    notes: es ? 'Veintiuno and the other -uno numbers shorten before a masculine noun (veintiún libros); this sheet uses the counting form.' : 'This sheet uses the traditional spelling, with hyphens only under 100. The 1990 spelling reform allows hyphens everywhere (deux-cent-trois); accept either.',
  };
}
function makeNumMath(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', big = v.level !== 'novice';
  const W1 = es ? { '+': 'más', '-': 'menos', x: 'por' } : { '+': 'plus', '-': 'moins', x: 'fois' };
  const mk = () => {
    const op = r.pick(big ? ['+', '-', 'x'] : ['+', '-']);
    let x, y, a;
    if (op === 'x') { x = r.int(2, 12); y = r.int(2, big ? 20 : 9); a = x * y; }
    else if (op === '+') { x = r.int(2, big ? 500 : 60); y = r.int(2, (big ? 999 : 100) - x); a = x + y; }
    else { x = r.int(10, big ? 999 : 100); y = r.int(1, x - 1); a = x - y; }
    return { k: 'nmath', lang, x, op, y, q: `${num(lang, x)} ${W1[op]} ${num(lang, y)}`, a: num(lang, a) };
  };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  return {
    title: es ? 'Matemáticas con palabras' : 'Les maths en mots', level: `${L(v, 'Spanish', 'French')}, ${LEVELS.find(x => x[0] === v.level)[1]}`,
    ican: 'I can read math problems written in words and write the answer in words.',
    directions: 'Read each problem, work it out, and write the answer in words.',
    minutes: 20, materials: 'pencil, scrap paper', items: its,
    parts: [part('', example(`${esc(ex.q)} = <b>${esc(ex.a)}</b>`, esc(es ? `más = plus, menos = minus${big ? ', por = times' : ''}, es = equals.` : `plus = plus, moins = minus${big ? ', fois = times' : ''}, font or égale = equals.`))),
      part('Practice', fill(its.map(s => `${esc(s.q)} = ${blankFor(s.a)}`)))],
    mistakes: 'Writing the answer as a numeral, and dropping accents and hyphens in the answer words.',
    notes: 'Students can say each problem aloud with a partner before solving it. Answers stay under 1,000.',
  };
}

/* ---------- agreement: colors and nationalities ---------- */
const nounPh = (lang, nn, pl, art) => {
  const g = nn[2], vw = !!nn[4];
  if (lang === 'es') return (art === 'indef' ? (pl ? (g === 'm' ? 'unos' : 'unas') : (g === 'm' ? 'un' : 'una')) : (pl ? (g === 'm' ? 'los' : 'las') : (g === 'm' ? 'el' : 'la'))) + ' ' + (pl ? nn[1] : nn[0]);
  return (pl ? 'les ' : vw ? 'l\'' : g === 'm' ? 'le ' : 'la ') + (pl ? nn[1] : nn[0]);
};
function makeColors(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', B = es ? ES : FR;
  const mk = () => { const nn = r.pick(B.nouns), c = r.pick(B.colors), pl = r.chance(0.45), idx = (nn[2] === 'f' ? 1 : 0) + (pl ? 2 : 0);
    return { k: 'agree', lang, adj: c[0], g: nn[2], pl, noun: nounPh(lang, nn, pl), q: `${nounPh(lang, nn, pl)} (${c[0]})`, a: c[idx] }; };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  return {
    title: es ? 'Colors That Agree: los colores' : 'Colors That Agree: les couleurs', level: `${L(v, 'Spanish', 'French')}, Novice`,
    ican: 'I can make a color word agree with the noun it describes.',
    directions: 'Write the color in parentheses so it agrees with the noun: masculine or feminine, singular or plural. The color goes after the noun.',
    minutes: 15, materials: 'pencil', items: its,
    parts: [part('', example(`${esc(ex.noun)} <b>${esc(ex.a)}</b> (${esc(ex.adj)})`, esc(es ? 'Colors ending in -o change to -a, -os, -as. Colors ending in -e or a consonant change only for plural: verde, verdes; azul, azules.' : 'Add -e for feminine and -s for plural: vert, verte, verts, vertes. Colors that already end in -e (rouge) do not add another; blanc becomes blanche, violet becomes violette.'))),
      part('Practice', fill(its.map(s => `${esc(s.noun)} ${blankFor(s.a)} (${esc(s.adj)})`), 2))],
    mistakes: es ? 'Changing verde or azul for gender (verda), and keeping the accent in marrones.' : 'Adding -e to rouge or jaune again, and writing blance or violete.',
    notes: es ? 'Rosa and naranja are left out because usage varies (they are often invariable).' : 'Orange and marron are left out because they never change; a good extension is to teach them as the exception.',
  };
}
function makeNation(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', B = es ? ES : FR, items = [];
  const be = es ? 'ser' : 'être';
  const ch = chart(lang, 'pres', [be], v.vosotros, items);
  const mk = () => {
    const per = r.pick(B.people), c = r.pick(B.nations), idx = { m: 1, f: 2, mp: 3, fp: 4 }[per[1]], pl = per[1].length > 1;
    const lead1 = es ? `${per[0]} ${pl ? 'son' : 'es'} de ${c[0]}. ${pl ? 'Son' : 'Es'}` : `${per[0]} ${pl ? 'viennent' : 'vient'} ${c[0]}. ${{ m: 'Il est', f: 'Elle est', mp: 'Ils sont', fp: 'Elles sont' }[per[1]]}`;
    return { k: 'nat', lang, m: c[1], gg: per[1], q: lead1, a: c[idx], html: `${esc(lead1)} ${blankFor(c[idx])}.` };
  };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  items.push(...its);
  return {
    title: es ? 'Ser and Nationalities' : 'Être and Nationalities', level: `${L(v, 'Spanish', 'French')}, Novice`,
    ican: `I can conjugate ${be} and make nationalities agree with the person.`,
    directions: `Fill in the chart for ${be}. Then complete each sentence with the nationality, matching the person: masculine or feminine, one or more.`,
    minutes: 20, materials: 'pencil, a world map if you have one', items,
    parts: [part('', example(`${ex.html.replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a)}</b>`)}`, esc(es ? 'Nationalities do not take a capital letter in Spanish. -o becomes -a for a woman; a consonant adds -a (español, española) and loses its accent (francés, francesa). A mixed group uses the masculine plural.'
      : 'Nationalities used as adjectives do not take a capital letter in French. Add -e for a woman (français, française); -ien becomes -ienne. A mixed group uses the masculine plural.'))),
    part(`Part 1: ${be}`, ch), part('Part 2: Nationalities', fill(its.map(s => s.html)))],
    mistakes: es ? 'Capitalizing nationalities, and keeping the accent in the feminine (francésa).' : 'Capitalizing nationalities, and writing canadiene with one n.',
    notes: 'A follow-up: students write one sentence about where their family or a favorite athlete is from.',
  };
}

/* ---------- articles, partitives, possessives ---------- */
function makeArticles(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', B = es ? ES : FR;
  if (!es && v.art === 'part') return makePartitive(v, r);
  const kinds = v.art === 'mix' ? ['def', 'indef'] : [v.art];
  const mk = () => { const nn = r.pick(B.nouns), pl = r.chance(0.4), kind = r.pick(kinds);
    const ph = nounPh(lang, nn, pl, kind), a = es ? ph.split(' ')[0] : kind === 'def' ? (pl ? 'les' : nn[4] ? 'l\'' : nn[2] === 'm' ? 'le' : 'la') : (pl ? 'des' : nn[2] === 'm' ? 'un' : 'une');
    const word = pl ? nn[1] : nn[0];
    return { k: 'art', lang, kind, g: nn[2], pl, vw: !!nn[4], word, q: `${kind} ${word}`, a, en: (kind === 'def' ? 'the ' : pl ? 'some ' : 'a ') + nn[3] + (pl ? 's' : '') };
  };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  const label = { def: es ? 'el, la, los, las' : 'le, la, l\', les', indef: es ? 'un, una, unos, unas' : 'un, une, des', mix: es ? 'el, la, los, las, un, una, unos, unas' : 'le, la, l\', les, un, une, des' }[v.art];
  return {
    title: `${es ? 'Articles' : 'Articles'}: ${label}`, level: `${L(v, 'Spanish', 'French')}, Novice`,
    ican: 'I can choose the article that matches a noun\'s gender and number.',
    directions: `Write the right article (${label}) on each line. The English below each noun tells you whether to use "the" or "a / some".`,
    minutes: 15, materials: 'pencil', items: its,
    parts: [part('', example(`<b>${esc(ex.a)}</b>${ex.a.endsWith('\'') ? '' : ' '}${esc(ex.word)} (${esc(ex.en)})`, esc(es ? 'Masculine nouns take el / un; feminine take la / una; plurals take los, las, unos, unas. Most nouns in -o are masculine and most in -a, -ción, -dad are feminine, but watch el mapa and la mano.'
      : 'Masculine nouns take le / un; feminine take la / une. Before a vowel or a silent h, le and la become l\'. All plurals take les or des.'))),
      part('Practice', fill(its.map(s => `${blank(s.a, 2.6)} ${esc(s.word)} <span class="wl-en">(${esc(s.en)})</span>`), 3))],
    mistakes: es ? 'Using el with feminine nouns that end in a consonant (la flor, la ciudad), and missing the exceptions el mapa and la mano.' : 'Writing le or la before a vowel (l\'école, l\'arbre), and guessing gender from English.',
    notes: 'Every noun on the sheet is a common, concrete word. Have students say each pair aloud: the article and noun are learned together.',
  };
}
function makePartitive(v, r) {
  const n = nOf(v), F = FR.foods;
  const mk = () => {
    const f = r.pick(F), neg = r.chance(0.3), drink = !!f[3];
    const verb = drink ? r.pick([['Je bois', 'Je ne bois pas'], ['Nous buvons', 'Nous ne buvons pas'], ['Elle prend', 'Elle ne prend pas']]) : r.pick([['Je mange', 'Je ne mange pas'], ['Tu achètes', 'Tu n\'achètes pas'], ['Nous prenons', 'Nous ne prenons pas'], ['Ils veulent', 'Ils ne veulent pas']]);
    const a = neg ? (f[2] ? 'd\'' : 'de') : f[1] === 'p' ? 'des' : f[2] ? 'de l\'' : f[1] === 'm' ? 'du' : 'de la';
    const lead1 = neg ? verb[1] : verb[0];
    return { k: 'part', food: f[0], g: f[1], vw: !!f[2], neg, q: `${lead1} ___ ${f[0]}`, a, html: `${esc(lead1)} ${blank(a, 3)}${a.endsWith('\'') ? '' : ' '}${esc(f[0])}.` };
  };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  return {
    title: 'Du, de la, de l\', des: Partitive Articles', level: 'French, Novice', ican: 'I can use du, de la, de l\' and des for some of something, and de after a negative.',
    directions: 'Write du, de la, de l\' or des on each line. After ne... pas, write de (or d\' before a vowel).',
    minutes: 15, materials: 'pencil', items: its,
    parts: [part('', example(ex.html.replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a)}</b>`), esc('Du for masculine, de la for feminine, de l\' before a vowel, des for plural. Negative: Je ne mange pas de pain; Je ne bois pas d\'eau.'))),
      part('Practice', fill(its.map(s => s.html), 2))],
    mistakes: 'Keeping du or de la after ne... pas, and writing de le or de les instead of du and des.',
    notes: 'Food words: everyday items from a French café or kitchen. A follow-up: students write what they eat for breakfast with the partitive.',
  };
}
const POWN = { es: [['my', 0], ['your (tú)', 1], ['his', 2], ['her', 2], ['your (usted)', 2], ['our', 3], ['your (vosotros)', 4], ['their', 5], ['your (ustedes)', 5]],
  fr: [['my', 0], ['your (tu)', 1], ['his', 2], ['her', 2], ['our', 3], ['your (vous)', 4], ['their', 5]] };
function possForm(lang, p, g, pl, vw) {
  if (lang === 'es') {
    if (p === 3 || p === 4) return (p === 3 ? 'nuestr' : 'vuestr') + (g === 'f' ? 'a' : 'o') + (pl ? 's' : '');
    return ['mi', 'tu', 'su', '', '', 'su'][p] + (pl ? 's' : '');
  }
  if (p === 3) return pl ? 'nos' : 'notre';
  if (p === 4) return pl ? 'vos' : 'votre';
  if (p === 5) return pl ? 'leurs' : 'leur';
  const s = ['m', 't', 's'][p];
  return pl ? s + 'es' : (g === 'm' || vw) ? s + 'on' : s + 'a';
}
function makePossess(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', B = es ? ES : FR;
  const owners = POWN[lang].filter(o => es ? (v.vosotros || o[1] !== 4) : true);
  const mk = () => { const nn = r.pick(B.nouns), o = r.pick(owners), pl = r.chance(0.4), word = pl ? nn[1] : nn[0];
    const a = possForm(lang, o[1], nn[2], pl, !!nn[4]);
    return { k: 'poss', lang, p: o[1], g: nn[2], pl, vw: !!nn[4], word, owner: o[0], q: `(${o[0]}) ${word}`, a }; };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  return {
    title: es ? 'Whose Is It? mi, tu, su, nuestro' : 'Whose Is It? mon, ma, mes', level: `${L(v, 'Spanish', 'French')}, Novice`,
    ican: 'I can choose a possessive adjective that matches the thing owned.',
    directions: 'The word in parentheses says who owns it. Write the possessive adjective that matches the thing owned: masculine or feminine, one or more.',
    minutes: 15, materials: 'pencil', items: its,
    parts: [part('', example(`(${esc(ex.owner)}) <b>${esc(ex.a)}</b> ${esc(ex.word)}`, esc(es ? 'Mi, tu and su add -s for plural things. Nuestro (and vuestro) also match gender: nuestra casa, nuestros libros. Su can mean his, her, its, your (usted) or their.'
      : 'The possessive matches the thing owned, not the owner: sa maison can be his house or her house. Before a feminine word that starts with a vowel, use mon, ton, son: mon amie, son école.'))),
      part('Practice', fill(its.map(s => `<span class="wl-en">(${esc(s.owner)})</span> ${blank(s.a, 3.4)} ${esc(s.word)}`), 2))],
    mistakes: es ? 'Matching su to the owner (sus for "their" with one thing), and forgetting that nuestro changes for gender.' : 'Choosing son or sa by the owner\'s gender, and writing ma before a vowel (ma amie).',
    notes: 'For a picture version, have students draw the owner next to a few items and label them.',
  };
}

/* ---------- gustar, places ---------- */
function makeGustar(v, r) {
  const n = nOf(v);
  const likers = ES.likers.filter(l => v.vosotros || l[2] !== 4);
  const mk = () => { const l = r.pick(likers), t = r.pick(ES.likes), neg = r.chance(0.2);
    const a = (neg ? 'no ' : '') + l[1] + ' ' + (t[1] ? 'gustan' : 'gusta');
    return { k: 'gust', who: l[0], pro: l[1], pl: !!t[1], thing: t[0], neg, q: `${l[0]} ${neg ? '(no) ' : ''}___ ${t[0]}`, a,
      html: `${esc(l[0])} ${neg ? '<i>(no)</i> ' : ''}${blankFor(a)} ${esc(t[0])}.` }; };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  return {
    title: 'Gusta or Gustan? Me gusta, te gusta...', level: 'Spanish, Novice', ican: 'I can say what people like with gustar and the right pronoun.',
    directions: 'Write the pronoun (me, te, le, nos, os, les) and gusta or gustan. Use gusta for one thing or an activity, gustan for more than one thing. When you see (no), start with no.',
    minutes: 15, materials: 'pencil', items: its,
    parts: [part('', example(ex.html.replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a)}</b>`), esc('A mí me gusta la pizza. A mí me gustan los tacos. The verb matches the thing liked, not the person.'))),
      part('Practice', fill(its.map(s => s.html)))],
    mistakes: 'Matching gustar to the person (yo gusto), and using gustan with an infinitive (me gustan nadar).',
    notes: 'A follow-up: students write three things they like and two they do not, then compare with a partner.',
  };
}
function makePlaces(v, r) {
  const n = nOf(v), C = FR.countries, items = [];
  const nA = Math.min(8, Math.max(6, Math.round(n / 2)));
  const artCs = r.sample(C, nA);
  const partA = fill(artCs.map(c => { items.push({ k: 'cart', name: c[0], g: c[2], q: `article ${c[0]}`, a: c[1] }); return `${blank(c[1], 2.6)}${c[1].endsWith('\'') ? '' : ' '}${esc(c[0])}`; }), 2);
  const frames = [['Je vais', 0], ['Nous habitons', 0], ['Elle travaille', 0], ['Ils voyagent', 0], ['Tu es', 0], ['Mon oncle habite', 0]];
  const mk = () => { const city = r.chance(0.3), f = r.pick(frames);
    if (city) { const c = r.pick(FR.cities); return { k: 'prep', city: c, q: `${f[0]} ___ ${c}`, a: 'à', html: `${esc(f[0])} ${blank('à', 2.4)} ${esc(c)}.` }; }
    const c = r.pick(C); return { k: 'prep', name: c[0], g: c[2], q: `${f[0]} ___ ${c[0]}`, a: c[3], html: `${esc(f[0])} ${blank(c[3], 2.4)} ${esc(c[0])}.` }; };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  items.push(...its);
  return {
    title: 'En France, au Canada, aux États-Unis', level: 'French, Novice', ican: 'I can say where someone goes or lives with en, au, aux and à.',
    directions: 'Part 1: write le, la, l\' or les before each country. Part 2: write en, au, aux or à to say "to" or "in".',
    minutes: 20, materials: 'pencil, a world map if you have one', items,
    parts: [part('', example(ex.html.replace(/<span class="ws-blank"[^]*?<\/span><\/span>/, `<b>${esc(ex.a)}</b>`), esc('Feminine countries (most end in -e) and countries that start with a vowel: en. Masculine countries: au. Plural countries: aux. Cities: à.'))),
      part('Part 1: The article for each country', partA), part('Part 2: To or in', fill(its.map(s => s.html), 2))],
    mistakes: 'Writing à for a country (à France), and missing the masculine countries that end in -e (le Mexique: au Mexique).',
    notes: 'Exceptions worth a mention: le Mexique and le Cambodge end in -e but are masculine. Haïti, Israël and islands like Cuba take no article.',
  };
}

/* ---------- dates and time ---------- */
const EN_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
const EN_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const dateText = (lang, dw, d, m) => lang === 'es' ? `el ${ES.days[dw]} ${d} de ${ES.months[m]}` : `le ${FR.days[dw]} ${d} ${FR.months[m]}`;
function orderItem(lang, r) {
  const B = lang === 'es' ? ES : FR, months = r.chance(0.5), arr = months ? B.months : B.days, i = r.int(0, arr.length - 1), after = r.chance(0.5);
  const j = (i + (after ? 1 : -1) + arr.length) % arr.length;
  const q = lang === 'es' ? (months ? `¿Qué mes viene ${after ? 'después de' : 'antes de'} ${arr[i]}?` : `¿Qué día viene ${after ? 'después del' : 'antes del'} ${arr[i]}?`)
    : (months ? `Quel mois vient ${after ? 'après' : 'avant'} ${arr[i]}${NB}?` : `Quel jour vient ${after ? 'après' : 'avant'} ${arr[i]}${NB}?`);
  return { k: 'order', lang, list: months ? 'months' : 'days', i, after, q, a: arr[j] };
}
function makeDates(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es';
  const mk = () => { const dw = r.int(0, 6), d = r.int(2, 28), m = r.int(0, 11);
    return { k: 'date', lang, dw, d, m, q: `${EN_DAYS[dw]}, ${EN_MONTHS[m]} ${d}`, a: dateText(lang, dw, d, m) }; };
  const ds = r.distinct(n + 1, mk, s => s.q), ex = ds.pop();
  const os = r.distinct({ s: 4, m: 6, l: 8 }[v.count], () => orderItem(lang, r), s => s.q);
  return {
    title: es ? 'Los días, los meses y la fecha' : 'Les jours, les mois et la date', level: `${L(v, 'Spanish', 'French')}, ${LEVELS.find(x => x[0] === v.level)[1]}`,
    ican: 'I can write the date and name the days and months in order.',
    directions: es ? 'Part 1: write each date in Spanish, like the example. Part 2: answer each question with a day or a month.' : 'Part 1: write each date in French, like the example. Part 2: answer each question with a day or a month.',
    minutes: 15, materials: 'pencil, a calendar', items: ds.concat(os),
    parts: [part('', example(`${esc(ex.q)}: <b>${esc(ex.a)}</b>`, esc(es ? 'Day, then number, then de and the month: el lunes 3 de mayo. Days and months take no capital letter. The first of the month is el primero (or el uno) de mayo.'
      : 'Le, then the day, the number and the month: le lundi 3 mars. Days and months take no capital letter. The first of the month is le premier: le lundi 1er mars.'))),
      part('Part 1: Write the date', fill(ds.map(s => `${esc(s.q)}: ${blankFor(s.a)}`))),
      part('Part 2: Before and after', fill(os.map(s => `${esc(s.q)} ${blankFor(s.a)}`), 2, ds.length + 1))],
    mistakes: es ? 'Capitalizing days and months, putting the month first as in English, and leaving out de.' : 'Capitalizing days and months, putting the month first as in English, and adding de (le 3 de mars).',
    notes: 'Days on this sheet do not follow a real calendar year, so students practice the words, not looking up the weekday.',
  };
}
function makeTime(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es';
  const mk = () => { const h = r.int(1, es ? 12 : 10), m = r.int(0, 11) * 5; return { k: 'time', lang, h, m, q: hhmm(h, m), a: es ? esTime(h, m) : frTime(h, m) }; };
  const its = r.distinct(n + 1 + { s: 3, m: 4, l: 4 }[v.count], mk, s => s.q), ex = its.pop();
  const draw = its.splice(n);
  const items = its.concat(draw.map(d => ({ ...d, k: 'draw', q: 'draw ' + d.a, a: hhmm(d.h, d.m) })));
  const rows = its.map((s, i) => `<div class="wl-trow"><span class="ws-num">${i + 1}.</span>${clockSvg(s.h, s.m, true, false, 78)}<span class="wl-tline">${blankFor(s.a)}</span></div>`).join('');
  const drawRow = `<div class="wl-draw">${draw.map((d, i) => `<div><span class="ws-num">${its.length + i + 1}.</span>${clockSvg(d.h, d.m, false, true, 96)}<p>${esc(d.a)}</p></div>`).join('')}</div>`;
  return {
    title: es ? '¿Qué hora es? Y cuarto, y media, menos' : 'Quelle heure est-il? Et quart, et demie, moins', level: `${L(v, 'Spanish', 'French')}, Novice`,
    ican: 'I can read a clock and say the time in a full sentence.',
    directions: `Part 1: write the time on each clock as a full sentence. Part 2: draw the hands to show each time.`,
    minutes: 20, materials: 'pencil', items,
    parts: [part('', example(`${hhmm(ex.h, ex.m)}: <b>${esc(ex.a)}</b>`, esc(es ? 'Es la una for one o\'clock, Son las for the other hours. Past the hour: y cuarto, y media, y diez. After half past, count back from the next hour with menos: 2:40 is Son las tres menos veinte.'
      : 'Il est une heure, Il est deux heures. Past the hour: et quart, et demie, or the minutes (dix). After half past, count back from the next hour with moins: 2:40 is Il est trois heures moins vingt.'))),
      part('Part 1: Write the time', `<div class="wl-tgrid">${rows}</div>`), part('Part 2: Draw the hands', drawRow)],
    mistakes: es ? 'Using Son las with una, and saying y cuarenta instead of counting back with menos.' : 'Forgetting heures, writing demi instead of demie after heures, and saying et quarante instead of counting back with moins.',
    notes: es ? 'Times are on the five-minute marks. Many speakers also say y cuarenta; the key uses the menos form taught in most programs.' : 'Times are on the five-minute marks between 1:00 and 11:00 (midi and minuit are left out). The key uses the everyday 12-hour style; the 24-hour clock has its own skill.',
  };
}
function makeTime24(v, r) {
  const n = nOf(v);
  const mk = () => { const h = r.int(13, 23), m = r.int(0, 11) * 5; return { h, m, q: hhmm(h, m) }; };
  const its = r.distinct(n + 1, mk, s => s.q), ex = its.pop();
  const items = [];
  const rows = its.map(s => { items.push({ k: 't24e', h: s.h, m: s.m, q: s.q + ' everyday', a: ampm(s.h, s.m) }, { k: 't24f', h: s.h, m: s.m, q: s.q + ' French', a: fr24(s.h, s.m) });
    return [`<b>${s.q}</b>`, blank(ampm(s.h, s.m), 5.5), blankFor(fr24(s.h, s.m))]; });
  return {
    title: 'L\'heure: The 24-Hour Clock', level: `French, ${LEVELS.find(x => x[0] === v.level)[1]}`,
    ican: 'I can read the 24-hour clock and say the time in French.',
    directions: 'For each 24-hour time, write the everyday time (with a.m. or p.m.), then write the time in French the way a train station or a timetable says it.',
    minutes: 15, materials: 'pencil', items,
    parts: [part('', example(`<b>${ex.q}</b> = ${ampm(ex.h, ex.m)} = <b>${esc(fr24(ex.h, ex.m))}</b>`, esc('Subtract 12 from hours after 12 for the everyday time. In French, say the hour, then heures, then the minutes as a number: dix-sept heures quarante-cinq. 21:00 is vingt et une heures.'))),
      part('Practice', table(['24-hour', 'Everyday', 'En français'], rows))],
    mistakes: 'Using et quart or et demie with the 24-hour clock (official times say quinze, trente), and writing vingt et un heures instead of vingt et une.',
    notes: 'Times are afternoon and evening, from 13:00 to 23:55. French timetables, TV listings and school schedules all use this clock.',
  };
}

/* ---------- vocabulary ---------- */
const LET = 'ABCDEFGHIJKLMNOP';
function makeVocab(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', B = es ? ES : FR;
  const bank = v.theme === 'weather' ? B.weather : B.themes[v.theme];
  const words = r.sample(bank, Math.min(n, bank.length));
  const right = r.shuffle(words);
  const items = words.map(w => ({ k: 'vm', lang, theme: v.theme, w: w[0], q: `match ${w[0]}`, a: LET[right.indexOf(w)], en: right.map(x => x[1]) }));
  const nB = { s: 4, m: 6, l: 6 }[v.count];
  const rest = bank.filter(w => !words.includes(w));
  const wb = r.sample(rest.length >= nB ? rest : bank, nB);
  for (const w of wb) items.push({ k: 'vw', lang, theme: v.theme, en: w[1], q: `write ${w[1]}`, a: w[0] });
  const th = THEMES.find(t => t[0] === v.theme)[1];
  const match = `<div class="wl-match"><ol class="ws-fill">${words.map((w, i) => `<li>${esc(w[0])} ${blank(items[i].a, 2)}</li>`).join('')}</ol><ul class="wl-letters">${right.map((w, i) => `<li><b>${LET[i]}.</b> ${esc(w[1])}</li>`).join('')}</ul></div>`;
  return {
    title: `${th}: ${es ? 'Spanish' : 'French'} Vocabulary`, level: `${L(v, 'Spanish', 'French')}, Novice`,
    ican: `I can understand and write ${th.toLowerCase()} words${v.theme === 'weather' ? ' and phrases' : ' with their articles'}.`,
    directions: `Part 1: write the letter of the English meaning next to each ${es ? 'Spanish' : 'French'} word. Part 2: write each word in ${es ? 'Spanish' : 'French'}${v.theme === 'weather' ? '' : ', with its article'}.`,
    minutes: 15, materials: 'pencil', items,
    parts: [part('Part 1: Match', match), part(`Part 2: Write it in ${es ? 'Spanish' : 'French'}`, fill(wb.map(w => `${esc(w[1])}: ${blankFor(w[0])}`), 2, words.length + 1))],
    mistakes: v.theme === 'weather' ? (es ? 'Using es or está for weather that takes hace (hace frío).' : 'Using est for weather that takes il fait (il fait froid).') : 'Leaving off the article, which carries the gender, and dropping accents.',
    notes: 'Learn each noun with its article. A quick game: call out an English word and students hold up the card or point to the word.',
  };
}

/* ---------- mixed review ---------- */
function makeReview(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', B = es ? ES : FR, its = [];
  const kinds = v.level === 'novice' ? ['conj', 'num', 'agree', 'date', 'time', 'weather', 'art']
    : v.level === 'intermediate' ? ['conj', 'conj2', 'past', 'num', 'date'] : ['fut', 'cond', 'subj', 'mood', 'si'].concat(es ? [] : ['pqp']);
  const mk = () => {
    const k = r.pick(kinds);
    if (k === 'conj' || k === 'conj2' || k === 'fut' || k === 'cond' || k === 'subj' || k === 'pqp') {
      const t = k === 'conj' ? 'pres' : k === 'conj2' ? (es ? 'pret' : 'pc') : k;
      const pool = verbPool(lang, t, v.level === 'novice' ? (es ? 'core' : 'big') : 'mix').filter(x => !B.verbs[x].chartOnly);
      const s = sentence(lang, t, r.pick(pool), r, { vos: v.vosotros });
      return { ...s, html: s.html + ` <span class="wl-en">(${tname(lang, t)})</span>` };
    }
    if (k === 'past') { const pool = es ? list(ES.groups.pret.reg + ' ' + ES.groups.pret.irr) : list(FR.groups.pc.avoir + ' ' + FR.groups.pc.etre); const s = pastItem(lang, r, v.vosotros, pool); return { ...s, k: 'past' }; }
    if (k === 'mood') { const trig = r.chance(0.5) ? r.pick(TRIG[lang].subj) : r.pick(TRIG[lang].ind); const g = B.groups.subj; const pool = list(g.reg || g.er);
      const s = sentence(lang, 'pres', r.pick(pool), r, { vos: v.vosotros, trig }); return { ...s, k: 'mood', why: '' }; }
    if (k === 'si') { const s = siItem(lang, r.chance(0.5) ? 'real' : 'unreal', r, v.vosotros); return s; }
    if (k === 'num') { const x = v.level === 'novice' ? r.int(11, 100) : r.int(100, 9999); const a = num(lang, x); return { k: 'num', lang, n: x, q: `Write ${x} in words`, a, html: `Write <b>${x >= 1000 ? Gen.m.fmt(x, 0) : x}</b> in words: ${blankFor(a)}` }; }
    if (k === 'agree') { const nn = r.pick(B.nouns), c = r.pick(B.colors), pl = r.chance(0.5), a = c[(nn[2] === 'f' ? 1 : 0) + (pl ? 2 : 0)];
      const ph = nounPh(lang, nn, pl); return { k: 'agree', lang, adj: c[0], g: nn[2], pl, q: `${ph} (${c[0]})`, a, html: `${esc(ph)} ${blankFor(a)} (${esc(c[0])})` }; }
    if (k === 'date') { const dw = r.int(0, 6), d = r.int(2, 28), m = r.int(0, 11), a = dateText(lang, dw, d, m); return { k: 'date', lang, dw, d, m, q: `${EN_DAYS[dw]}, ${EN_MONTHS[m]} ${d}`, a, html: `Write the date: ${EN_DAYS[dw]}, ${EN_MONTHS[m]} ${d}. ${blankFor(a)}` }; }
    if (k === 'time') { const h = r.int(1, es ? 12 : 10), m = r.int(0, 11) * 5, a = es ? esTime(h, m) : frTime(h, m); return { k: 'time', lang, h, m, q: hhmm(h, m), a, html: `Write the time ${hhmm(h, m)}: ${blankFor(a)}` }; }
    if (k === 'weather') { const w = r.pick(B.weather); return { k: 'vw', lang, theme: 'weather', en: w[1], q: `write ${w[1]}`, a: w[0], html: `Say it: ${esc(w[1])} ${blankFor(w[0])}` }; }
    const nn = r.pick(B.nouns), pl = r.chance(0.4), word = pl ? nn[1] : nn[0];
    const a = es ? (pl ? (nn[2] === 'm' ? 'los' : 'las') : (nn[2] === 'm' ? 'el' : 'la')) : (pl ? 'les' : nn[4] ? 'l\'' : nn[2] === 'm' ? 'le' : 'la');
    return { k: 'art', lang, kind: 'def', g: nn[2], pl, vw: !!nn[4], word, q: `the ${word}`, a, html: `The word for "the": ${blank(a, 2.6)}${a.endsWith('\'') ? '' : ' '}${esc(word)}` };
  };
  const all = r.distinct(n, mk, s => s.q);
  for (const s of all) its.push(s);
  return {
    title: `${LEVELS.find(x => x[0] === v.level)[1].replace(/ \(.*/, '')} Review`, level: `${L(v, 'Spanish', 'French')}, ${LEVELS.find(x => x[0] === v.level)[1]}`,
    ican: 'I can show what I know across this level\'s grammar and vocabulary.',
    directions: 'Answer each item. For verbs, the tense is in parentheses; include every accent.',
    minutes: 25, materials: 'pencil',
    items: its.map(s => { const o = { ...s }; delete o.html; return o; }),
    parts: [part('Review', fill(its.map(s => s.html)))],
    mistakes: 'Rushing past accents and agreement; check each answer against its subject or noun.',
    notes: 'Items mix this level\'s skills: ' + ({ novice: 'present-tense verbs, numbers, color agreement, dates, time, weather and articles', intermediate: 'present and past verbs, past-tense signal words, numbers and dates', advanced: 'future, conditional, subjunctive, mood choice and si clauses' + (es ? '' : ', and the plus-que-parfait') }[v.level]) + '. Press New sheet for a different mix.',
  };
}

/* ---------- K-5 ---------- */
function makeK5(v, r) {
  const lang = v.lang, n = nOf(v), es = lang === 'es', B = es ? ES : FR, LN = es ? 'Spanish' : 'French';
  const base = { level: `${LN}, grades K-5`, materials: 'pencil, crayons', minutes: 15 };
  if (v.skill === 'count') {
    const nums = r.shuffle(r.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n));
    const items = nums.map((x, i) => ({ k: 'count', lang, n: x, q: `box ${i + 1}`, a: String(x) }));
    const cells = nums.map((x, i) => { const svg = countSvg(x, r.pick(SHAPES)); items[i].svg = svg;
      return `<div class="wl-cbox"><span class="ws-num">${i + 1}.</span>${svg}<div>${blank(String(x), 2.4)}</div><p class="wl-trace">${esc(num(lang, x))}</p></div>`; });
    return { ...base, title: es ? 'Cuenta conmigo: Count 1 to 10' : 'Compte avec moi: Count 1 to 10', ican: 'I can count and say the numbers 1 to 10 in ' + LN + '.',
      directions: 'Count the shapes in each box. Write the number. Then trace the word.', items,
      parts: [part('', `<div class="wl-cgrid">${cells.join('')}</div>`)],
      mistakes: 'Counting a shape twice. Touch each shape as you count.', notes: 'Say each word aloud together before students trace it. The words are printed light for tracing.' };
  }
  if (v.skill === 'colors') {
    const cs = r.sample(B.crayons, n), right = r.shuffle(cs);
    const items = cs.map(c => ({ k: 'kcolor', lang, w: c[0], q: c[0], a: LET[right.indexOf(c)], hex: right.map(x => x[1]) }));
    const draws = r.sample(cs, { s: 3, m: 4, l: 4 }[v.count]);
    const match = `<div class="wl-match"><ol class="ws-fill">${cs.map((c, i) => `<li class="wl-big">${esc(c[0])} ${blank(items[i].a, 2)}</li>`).join('')}</ol><ul class="wl-letters">${right.map((c, i) => `<li><b>${LET[i]}.</b> ${crayonSvg(c[1])}</li>`).join('')}</ul></div>`;
    return { ...base, title: es ? 'Crayon Box: Los colores' : 'Crayon Box: Les couleurs', ican: 'I can match color words to colors.',
      directions: 'Draw a line from each color word to its crayon, or write the crayon\'s letter. Then draw something that color in each box.', items,
      parts: [part('Match', match), part('Draw', `<div class="wl-draw">${draws.map(c => `<div><div class="ws-draw" style="height:1in"><span></span></div><p>${esc(c[0])}</p></div>`).join('')}</div>`)],
      mistakes: 'Mixing up colors with similar words. Say each word aloud while pointing.', notes: 'Print in color for the crayon pictures, or have students color the crayons first as the teacher says each word.' };
  }
  if (v.skill === 'days' || v.skill === 'months') {
    const arr = v.skill === 'days' ? B.days : B.months;
    const hide = new Set(r.sample(arr.map((_, i) => i), n));
    const items = [...hide].sort((a, b) => a - b).map(i => ({ k: 'kord', lang, list: v.skill, i, q: `${v.skill} ${i + 1}`, a: arr[i] }));
    const bank = r.shuffle([...hide].map(i => arr[i]));
    const cars = arr.map((d, i) => `<div class="wl-car"><span class="wl-cn">${i + 1}</span>${hide.has(i) ? blankFor(d) : `<b>${esc(d)}</b>`}</div>`).join('');
    const extra = v.skill === 'months' ? part('Draw', `<div class="wl-draw">${r.sample(arr, 4).map(m => `<div><div class="ws-draw" style="height:1in"><span></span></div><p>${esc(m)}</p></div>`).join('')}</div>`) : null;
    return { ...base, title: v.skill === 'days' ? (es ? 'Los días de la semana' : 'Les jours de la semaine') : (es ? 'Los meses del año' : 'Les mois de l\'année'),
      ican: `I can say the ${v.skill === 'days' ? 'days of the week' : 'months of the year'} in order.`,
      directions: `Write the missing ${v.skill === 'days' ? 'days' : 'months'} in order. Use the word box.${v.skill === 'months' ? ' Then draw a picture for each month at the bottom.' : ''}`, items,
      parts: [part('Word box', `<p class="wl-bank">${bank.map(esc).join(' · ')}</p>`), part('', `<div class="wl-train${v.skill === 'months' ? ' wl-months' : ''}">${cars}</div>`)].concat(extra ? [extra] : []),
      mistakes: 'Starting the week on Sunday. In Spanish- and French-speaking countries the week starts on Monday.', notes: 'Sing or chant the list together first. Days and months take no capital letter in ' + LN + '.' };
  }
  // clock
  const its = r.distinct(n, () => { const h = r.int(1, es ? 12 : 11); return { k: 'kclock', lang, h, q: es ? (h === 1 ? 'Es la una.' : `Son las ${esNum(h)}.`) : (h === 1 ? 'Il est une heure.' : `Il est ${frNum(h)} heures.`), a: `${h}:00` }; }, s => s.q);
  return { ...base, title: es ? '¿Qué hora es? Clock Faces' : 'Quelle heure est-il? Clock Faces', ican: 'I can show a time on the hour that I hear in ' + LN + '.',
    directions: 'Listen to the time, or read it. Draw the hands on each clock: the short hand points to the hour, the long hand points to 12.', items: its,
    parts: [part('', `<div class="wl-draw wl-k5clock">${its.map((s, i) => `<div><span class="ws-num">${i + 1}.</span>${clockSvg(s.h, 0, false, true, 120)}<p>${esc(s.q)}</p></div>`).join('')}</div>`)],
    mistakes: 'Drawing both hands the same length. The hour hand is short.', notes: 'Read each time aloud before students draw. Times are on the hour only' + (es ? '.' : ', 1 to 11 (midi and minuit are left out).') };
}

/* ---------- the generator ---------- */
const fmtShow = v => v.level !== 'k5' && v.skill === 'conj';
Gen.add('world-language', {
  title: 'Spanish and French Practice', type: 'Practice',
  css: `.wl-why{display:block;margin:2px 0 0 0;font-size:13px;color:#444}
.wl-en{font-size:12px;color:#555}
.wl-line{line-height:2.2}
.wl-match{display:grid;grid-template-columns:1.2fr 1fr;gap:16px;align-items:start}
.wl-letters{list-style:none;padding:0;margin:6px 0}.wl-letters li{margin:0 0 10px;min-height:22px}
.wl-big{font-size:18px}
.wl-tgrid{display:grid;grid-template-columns:1fr 1fr;gap:6px 18px}
.wl-trow{display:flex;align-items:center;gap:8px;break-inside:avoid}.wl-tline{flex:1}
.wl-draw{display:flex;flex-wrap:wrap;gap:14px 22px}.wl-draw>div{text-align:center;break-inside:avoid;min-width:1.4in}.wl-draw p{margin:4px 0;font-size:14px}
.wl-k5clock p{font-size:16px}
.wl-cgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}
.wl-cbox{border:1.5px solid #444;border-radius:8px;padding:4px;text-align:center;break-inside:avoid}.wl-cbox .ws-num{float:left}
.wl-trace{font-size:20px;color:#bbb;letter-spacing:2px;margin:4px 0;font-family:sans-serif}
.wl-bank{border:1.5px solid #444;border-radius:6px;padding:6px 10px;font-size:16px}
.wl-train{display:flex;flex-wrap:wrap;gap:8px}
.wl-car{border:2px solid #333;border-radius:6px;padding:16px 8px 8px;min-width:1.25in;text-align:center;position:relative;font-size:16px}
.wl-months .wl-car{min-width:1.6in}
.wl-cn{position:absolute;top:2px;left:6px;font-size:11px;color:#666}`,
  fields: [
    { id: 'lang', label: 'Language', type: 'select', options: LANGS, def: 'es' },
    { id: 'level', label: 'Level', type: 'select', options: LEVELS, def: 'novice' },
    { id: 'skill', label: 'Skill', type: 'select', options: skillsFor, def: 'conj' },
    { id: 'tense', label: 'Tense', type: 'select', options: v => TENSES[v.lang][v.level] || [['pres', 'Present']], def: 'pres', show: fmtShow },
    { id: 'verbs', label: 'Verbs', type: 'select', options: groupsFor, def: 'reg', show: fmtShow },
    { id: 'fmt', label: 'Format', type: 'select', options: [['both', 'Charts, then sentences'], ['sent', 'Sentences only'], ['chart', 'Charts only']], def: 'both', show: fmtShow },
    { id: 'range', label: 'Numbers', type: 'select', options: v => (RANGES[v.level] || RANGES.novice)[v.lang], def: '20', show: v => v.skill === 'numbers' && v.level !== 'k5' },
    { id: 'art', label: 'Articles', type: 'select', options: v => [['def', 'Definite (the)'], ['indef', 'Indefinite (a, some)'], ['mix', 'Both']].concat(v.lang === 'fr' ? [['part', 'Partitive (du, de la, des)']] : []), def: 'def', show: v => v.skill === 'articles' },
    { id: 'theme', label: 'Theme', type: 'select', options: THEMES, def: 'family', show: v => v.skill === 'vocab' },
    { id: 'sitype', label: 'Kind of si clause', type: 'select', options: [['unreal', 'Hypothetical (if I had... I would)'], ['real', 'Real (if I have... I will)'], ['mix', 'Both, mixed']], def: 'unreal', show: v => v.skill === 'si' },
    { id: 'vosotros', label: 'Include vosotros (Spain)', type: 'check', def: false, show: v => v.lang === 'es' && v.level !== 'k5' },
    { id: 'count', label: 'Length', type: 'select', def: 'm', options: v => { const k = SIZES[sizeKey(v)] || SIZES.conjboth; return [['s', `Fewer (${k[0]})`], ['m', `Standard (${k[1]})`], ['l', `More (${k[2]})`]]; } },
  ],
  make(v, r) {
    const s = v.level === 'k5' ? makeK5(v, r) : ({ conj: makeConj, pastmix: makePast, mood: makeMood, si: makeSi, numbers: makeNumbers, nummath: makeNumMath, colors: makeColors,
      nation: makeNation, articles: makeArticles, possess: makePossess, gustar: makeGustar, places: makePlaces, dates: makeDates, time: makeTime, time24: makeTime24,
      vocab: makeVocab, review: makeReview }[v.skill] || makeConj)(v, r);
    s.eyebrow = s.eyebrow || (v.lang === 'es' ? 'Spanish practice' : 'French practice');
    return s;
  },
  verify(s, v) {
    const out = [], es = v.lang === 'es', B = es ? ES : FR;
    const strip = w => w.replace(/[áéíóú]([^áéíóú]*)$/, (m, rest) => ({ á: 'a', é: 'e', í: 'i', ó: 'o', ú: 'u' }[m[0]]) + rest);
    const agreeRule = (lang, m, g, pl, nat) => {
      if (lang === 'es') {
        if (m.endsWith('o')) return m.slice(0, -1) + (g === 'f' ? 'a' : 'o') + (pl ? 's' : '');
        if (m.endsWith('e')) return pl ? m + 's' : m;
        if (nat && /(és|án)$/.test(m)) return g === 'f' ? strip(m) + 'a' + (pl ? 's' : '') : pl ? strip(m) + 'es' : m;
        if (nat && m === 'español') return g === 'f' ? strip(m) + 'a' + (pl ? 's' : '') : pl ? strip(m) + 'es' : m;
        return pl ? (m.endsWith('ón') ? m.slice(0, -2) + 'ones' : m + 'es') : m;
      }
      let f = g === 'f' ? (m === 'blanc' ? 'blanche' : m === 'violet' ? 'violette' : m.endsWith('ien') ? m + 'ne' : m.endsWith('e') ? m : m + 'e') : m;
      if (pl && !f.endsWith('s')) f += 's';
      return f;
    };
    for (const it of s.items) {
      let want = null;
      const k = it.k;
      if (k === 'conj' || k === 'past' || k === 'mood') {
        want = check(it.lang, it.inf, it.t, it.p, it.g);
        if (k === 'past') { const side = PAST[it.lang].a.t === it.t ? 'a' : 'b'; if (side !== it.side) out.push(`${it.q}: tense ${it.t} does not match its signal words`); }
        if (k === 'mood') { const tr = TRIG[it.lang].subj.concat(TRIG[it.lang].ind).find(x => x[0] === (it.trig || '')) || TRIG[it.lang].subj.concat(TRIG[it.lang].ind).find(x => it.q.startsWith(x[0]));
          if (tr && (tr[1] === 's') !== (it.t === 'subj')) out.push(`${it.q}: mood does not match the trigger`); }
      } else if (k === 'si') {
        const a1 = check(it.lang, it.c1, it.t1, it.p), a2 = check(it.lang, it.c2, it.t2, it.p);
        want = `${a1} ... ${a2}`;
        if ((it.type === 'unreal') !== (it.t2 === 'cond')) out.push(`${it.q}: wrong tense pair`);
      } else if (k === 'num' || k === 'nmath') {
        const n = k === 'num' ? it.n : it.op === '+' ? it.x + it.y : it.op === '-' ? it.x - it.y : it.x * it.y;
        want = numCheck(it.lang, n);
        if (k === 'nmath' && n < 0) out.push(`${it.q}: negative`);
      } else if (k === 'numr') want = it.n >= 1000 ? String(it.n).replace(/(\d)(\d{3})$/, '$1,$2') : String(it.n);
      else if (k === 'logic') want = it.n >= 80 ? '4 × 20' + (it.n > 80 ? ' + ' + (it.n - 80) : '') : '60 + ' + (it.n - 60);
      else if (k === 'agree') want = agreeRule(it.lang, it.adj, it.g, it.pl);
      else if (k === 'nat') want = agreeRule(it.lang, it.m, it.gg[0], it.gg.length > 1, true);
      else if (k === 'art') want = it.lang === 'es' ? (it.kind === 'def' ? (it.pl ? 'l' + (it.g === 'm' ? 'os' : 'as') : it.g === 'm' ? 'el' : 'la') : 'un' + (it.g === 'm' ? (it.pl ? 'os' : '') : (it.pl ? 'as' : 'a')))
        : it.kind === 'def' ? (it.pl ? 'les' : it.vw ? 'l\'' : it.g === 'f' ? 'la' : 'le') : (it.pl ? 'des' : it.g === 'f' ? 'une' : 'un');
      else if (k === 'part') want = it.neg ? (it.vw ? 'd\'' : 'de') : { p: 'des', m: it.vw ? 'de l\'' : 'du', f: it.vw ? 'de l\'' : 'de la' }[it.g];
      else if (k === 'poss') {
        if (it.lang === 'es') want = it.p === 3 || it.p === 4 ? ['nuestr', 'vuestr'][it.p - 3] + (it.g === 'm' ? 'o' : 'a') + (it.pl ? 's' : '') : { 0: 'mi', 1: 'tu', 2: 'su', 5: 'su' }[it.p] + (it.pl ? 's' : '');
        else want = it.pl ? ['mes', 'tes', 'ses', 'nos', 'vos', 'leurs'][it.p] : it.p >= 3 ? ['notre', 'votre', 'leur'][it.p - 3] : (it.g === 'f' && !it.vw ? ['ma', 'ta', 'sa'] : ['mon', 'ton', 'son'])[it.p];
      } else if (k === 'gust') { const pro = { 'A mí': 'me', 'A ti': 'te', 'A nosotros': 'nos', 'A vosotros': 'os' }[it.who] || (/^A (ellos|ellas|ustedes|mis padres)$/.test(it.who) ? 'les' : 'le');
        want = (it.neg ? 'no ' : '') + pro + (it.pl ? ' gustan' : ' gusta');
        if (/^(bailar|nadar|leer|cantar)$/.test(it.thing) && it.pl) out.push(`${it.q}: infinitive marked plural`);
      } else if (k === 'cart') want = /^(États-Unis|Pays-Bas|Philippines)$/.test(it.name) ? 'les' : /^[AEIOUÉ]/.test(it.name) ? 'l\'' : it.g === 'f' ? 'la' : 'le';
      else if (k === 'prep') want = it.city ? 'à' : it.g.length > 1 ? 'aux' : it.g === 'f' || /^[AEIOUÉ]/.test(it.name) ? 'en' : 'au';
      else if (k === 'date') want = it.lang === 'es' ? `el ${'lunes martes miércoles jueves viernes sábado domingo'.split(' ')[it.dw]} ${it.d} de ${'enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre'.split(' ')[it.m]}`
        : `le ${'lundi mardi mercredi jeudi vendredi samedi dimanche'.split(' ')[it.dw]} ${it.d} ${'janvier février mars avril mai juin juillet août septembre octobre novembre décembre'.split(' ')[it.m]}`;
      else if (k === 'order' || k === 'kord') {
        const arr = it.list === 'days' ? (it.lang === 'es' ? 'lunes martes miércoles jueves viernes sábado domingo' : 'lundi mardi mercredi jeudi vendredi samedi dimanche').split(' ')
          : (it.lang === 'es' ? 'enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre' : 'janvier février mars avril mai juin juillet août septembre octobre novembre décembre').split(' ');
        want = k === 'kord' ? arr[it.i] : arr[(it.i + (it.after ? 1 : arr.length - 1)) % arr.length];
      } else if (k === 'time') {   // rebuild from total minutes
        const tot = it.h * 60 + it.m, back = it.m > 30, hh = back ? Math.floor(tot / 60) % 12 + 1 : it.h, mm = back ? 60 - it.m : it.m;
        if (it.lang === 'es') want = (hh === 1 ? 'Es la una' : 'Son las ' + numCheck('es', hh)) + (mm === 0 ? '' : back ? ' menos ' + (mm === 15 ? 'cuarto' : numCheck('es', mm)) : ' y ' + (mm === 15 ? 'cuarto' : mm === 30 ? 'media' : numCheck('es', mm))) + '.';
        else want = 'Il est ' + (hh === 1 ? 'une heure' : numCheck('fr', hh) + ' heures') + (mm === 0 ? '' : back ? (mm === 15 ? ' moins le quart' : ' moins ' + numCheck('fr', mm)) : mm === 15 ? ' et quart' : mm === 30 ? ' et demie' : ' ' + numCheck('fr', mm)) + '.';
        if (it.lang === 'fr' && (hh > 11 || it.h > 11)) out.push(`${it.q}: noon or midnight`);
      } else if (k === 'draw') want = `${it.h}:${it.m < 10 ? '0' : ''}${it.m}`;
      else if (k === 't24e') want = `${it.h - 12}:${it.m < 10 ? '0' : ''}${it.m} p.m.`;
      else if (k === 't24f') want = 'Il est ' + (it.h === 21 ? 'vingt et une' : numCheck('fr', it.h)) + ' heures' + (it.m ? ' ' + numCheck('fr', it.m) : '') + '.';
      else if (k === 'vm') { const bank = it.theme === 'weather' ? B.weather : B.themes[it.theme]; const en = bank.find(w => w[0] === it.w)[1]; want = LET[it.en.indexOf(en)]; }
      else if (k === 'vw') { const bank = it.theme === 'weather' ? B.weather : B.themes[it.theme]; want = bank.find(w => w[1] === it.en)[0]; }
      else if (k === 'count') { want = String((it.svg.match(/class="k5o"/g) || []).length); }
      else if (k === 'kcolor') { const c = B.crayons.find(x => x[0] === it.w); want = LET[it.hex.indexOf(c[1])]; }
      else if (k === 'kclock') { const w = it.q.replace(/^(Es la |Son las |Il est )/, '').replace(/ heures?\.$|\.$/, ''); const hours = (es ? 'x una dos tres cuatro cinco seis siete ocho nueve diez once doce' : 'x une deux trois quatre cinq six sept huit neuf dix onze douze').split(' ');
        want = `${hours.indexOf(w)}:00`; }
      else { out.push(`${it.q}: no check for kind ${k}`); continue; }
      if (want == null || String(want) !== String(it.a)) out.push(`${it.q}: key says ${it.a}, check says ${want}`);
    }
    return out;
  },
});
})();
