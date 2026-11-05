// Number Operations generator, grades K-6 (the reference generator: other generators follow this shape).
// Grade sets the size of the numbers; skill picks the operation; regrouping is a choice for addition and subtraction.
// Grade 2 can be kept to two-digit numbers within 100. Grades 1-4 offer a Missing number skill (7 + ? = 15, and at
// grades 3-4 unknown factors). Grade 6 does long division with decimal quotients and multiplies decimals. "Estimate
// first" (grades 2-5 add, subtract, multiply) adds an Estimate blank to each problem; the key rounds each number to its
// leading place.
(() => {
const { blank, part, example, fill, stacks, stack, longdiv } = Gen.h;
const { fmt } = Gen.m;

const GRADES = [['k', 'Kindergarten'], ['1', 'Grade 1'], ['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'], ['6', 'Grade 6']];
const SKILLS = {  // which skills each grade offers
  k: [['add', 'Addition'], ['sub', 'Subtraction'], ['addsub', 'Addition and subtraction']],
  1: [['add', 'Addition'], ['sub', 'Subtraction'], ['addsub', 'Addition and subtraction'], ['missing', 'Missing number']],
  2: [['add', 'Addition'], ['sub', 'Subtraction'], ['addsub', 'Addition and subtraction'], ['missing', 'Missing number']],
  3: [['add', 'Addition'], ['sub', 'Subtraction'], ['mul', 'Multiplication facts'], ['div', 'Division facts'], ['muldiv', 'Multiplication and division'], ['mix', 'All four'], ['missing', 'Missing number']],
  4: [['add', 'Addition'], ['sub', 'Subtraction'], ['mul', 'Multiplication'], ['div', 'Division with remainders'], ['mix', 'All four'], ['missing', 'Missing number']],
  5: [['mul', 'Multiplication'], ['div', 'Long division'], ['dec', 'Adding and subtracting decimals'], ['mix', 'All four']],
  6: [['div', 'Long division with decimal quotients'], ['decmul', 'Multiply decimals'], ['mix', 'Both']],
};
const SIGN = { '+': '+', '-': '−', 'x': '×', '/': '÷', 'dd': '÷', 'dx': '×' };

// the numbers for one problem: returns {x, op, y, a} where a is the answer text
// size = '100' keeps grade 2 to two-digit numbers with sums up to 100
function problem(r, g, op, regroup, size) {
  const digits = n => String(n).split('').reverse().map(Number);
  const carries = (x, y) => { const a = digits(x), b = digits(y); return a.some((d, i) => d + (b[i] || 0) >= 10); };
  const borrows = (x, y) => { const a = digits(x), b = digits(y); return b.some((d, i) => d > a[i]); };
  const ok = (x, y, plus) => regroup === 'any' || (plus ? carries(x, y) : borrows(x, y)) === (regroup === 'with');
  if (op === '+' || op === '-') {
    const [lo, hi] = { k: [0, 10], 1: [0, 20], 2: [10, 999], 3: [100, 999], 4: [1000, 99999] }[g];
    for (let t = 0; t < 200; t++) {
      let x, y;
      if (g === 'k') { x = r.int(op === '+' ? 0 : 1, 10); y = r.int(0, op === '+' ? 10 - x : x); }
      else if (g === '1') { x = r.int(1, op === '+' ? 18 : 20); y = r.int(0, op === '+' ? 20 - x : x); }
      else if (g === '2' && size === '100') { x = op === '+' ? r.int(10, 90) : r.int(10, 99); y = r.int(10, op === '+' ? 100 - x : x); }
      else if (g === '2') { const big = r.chance(.5); x = big ? r.int(100, 899) : r.int(10, 99); y = big ? r.int(10, op === '+' ? 999 - x : x) : r.int(10, op === '+' ? 99 : x); }
      else { x = r.int(lo, hi); y = r.int(Math.floor(lo / 2), op === '+' ? hi : x); }
      if (op === '-' && y > x) [x, y] = [y, x];
      if (op === '+' && g !== 'k' && g !== '1' && x + y > (g === '2' ? 1000 : g === '3' ? 1000 : 1000000)) continue;
      if ((g === 'k' || g === '1') || ok(x, y, op === '+')) return { x, op, y, a: op === '+' ? x + y : x - y };
    }
    return null;
  }
  if (op === 'x') {
    if (g === '3') { const x = r.int(0, 10), y = r.int(0, 10); return { x, op, y, a: x * y }; }
    if (g === '4') { const two = r.chance(.4); const x = two ? r.int(11, 99) : r.int(100, 9999), y = two ? r.int(11, 99) : r.int(2, 9); return { x, op, y, a: x * y }; }
    const x = r.int(100, 999), y = r.int(11, 99); return { x, op, y, a: x * y };
  }
  if (op === '/') {
    if (g === '3') { const y = r.int(1, 10), q = r.int(0, 10); return { x: y * q, op, y, a: q }; }
    const y = g === '4' ? r.int(2, 9) : r.int(11, 49), x = g === '4' ? r.int(100, 9999) : r.int(1000, 9999);
    const q = Math.floor(x / y), rem = x % y;
    return { x, op, y, a: rem ? `${fmt(q, 0)} R ${rem}` : q, q, rem };
  }
  if (op === 'd+' || op === 'd-') {  // decimals to hundredths, kept as whole hundredths to avoid float error
    const x = r.int(105, 9999), y = r.int(105, op === 'd+' ? 9999 : x);
    const h = n => fmt(n / 100, 2).replace(/(\.\d)$/, '$10').replace(/^(\d+)$/, '$1.00');
    return { x: h(x), op: op[1], y: h(y), a: h(op === 'd+' ? x + y : x - y), dec: true, xh: x, yh: y };
  }
  if (op === 'dd') {  // grade 6: a two-digit divisor, a 3-4 digit dividend, a quotient that ends at tenths or hundredths
    for (let t = 0; t < 400; t++) {
      const y = r.int(11, 99), fr = [];   // the decimal parts (in hundredths) that this divisor can make exactly
      for (let f = 1; f < 100; f++) if ((y * f) % 100 === 0) fr.push(f);
      if (!fr.length) continue;
      const qh = r.int(2, 400) * 100 + r.pick(fr), x = y * qh / 100;   // quotient in hundredths
      if (x < 100 || x > 9999) continue;
      return { x, op, y, a: fmt(qh / 100, 2), dec: true, qh };
    }
    return { x: 282, op, y: 12, a: '23.5', dec: true, qh: 2350 };
  }
  if (op === 'dx') {  // grade 6: a tenths or hundredths number times a whole number or a tenths number
    const dx = r.chance(.5) ? 1 : 2, xi = r.int(11, dx === 1 ? 999 : 9999), whole = r.chance(.5), dy = whole ? 0 : 1, yi = whole ? r.int(2, 99) : r.int(11, 99);
    if (xi % 10 === 0 || (!whole && yi % 10 === 0)) return null;   // keep the decimals real (3.0 is a whole number)
    const show = (n, d) => { if (!d) return String(n); const s = String(n).padStart(d + 1, '0'); return s.slice(0, -d) + '.' + s.slice(-d); };
    return { x: show(xi, dx), op, y: show(yi, dy), a: fmt(xi * yi / 10 ** (dx + dy), dx + dy), dec: true, xi, yi, dx, dy };
  }
}

// a missing-number problem for the Missing number skill: one of the two numbers is hidden
function missing(r, g, size) {
  const op = r.pick(g === '3' || g === '4' ? ['+', '-', 'x', '/'] : ['+', '-']);
  let p;
  if (op === '+' || op === '-') p = problem(r, g, op, 'any', size);
  else if (g === '3') p = problem(r, g, op, 'any');
  else if (op === 'x') { const x = r.int(2, 9), y = r.int(11, 99); p = { x, op, y, a: x * y }; }
  else { const y = r.int(2, 9), q = r.int(11, 99); p = { x: y * q, op, y, a: q }; }
  if (!p || p.x === 0 || p.y === 0 || p.a === 0) return null;
  if ((op === 'x' || op === '/') && (p.x === 1 || p.y === 1 || p.a === 1)) return null;
  p.hide = r.pick(['x', 'y']);
  p.m = p[p.hide];
  return p;
}
// round n to its leading place: 523 -> 500, 87 -> 90, 7 -> 7
const lead = n => { if (n < 10) return n; const k = 10 ** (String(n).length - 1); return Math.round(n / k) * k; };
const estimate = p => p.op === '+' ? lead(p.x) + lead(p.y) : p.op === '-' ? lead(p.x) - lead(p.y) : lead(p.x) * lead(p.y);

function opsFor(skill) {
  return { add: ['+'], sub: ['-'], addsub: ['+', '-'], mul: ['x'], div: ['/'], muldiv: ['x', '/'], mix: ['+', '-', 'x', '/'], dec: ['d+', 'd-'], decmul: ['dx'] }[skill];
}
const show = n => typeof n === 'number' ? fmt(n, 0) : String(n);
const canEst = v => ['2', '3', '4', '5'].includes(v.grade) && ({ 2: ['add', 'sub', 'addsub'], 3: ['add', 'sub', 'addsub'], 4: ['add', 'sub', 'mul', 'mix'], 5: ['mul', 'mix'] }[v.grade]).includes(v.skill);

Gen.add('number-ops', {
  title: 'Number Operations', type: 'Practice',
  css: `.gen-estwrap{display:inline-flex;flex-direction:column;gap:4px}
.gen-est{font-size:13px;white-space:nowrap}
.gen-est .ws-blank{min-width:3.4em}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '2' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => SKILLS[v.grade], def: 'add' },
    { id: 'regroup', label: 'Regrouping', type: 'select', def: 'any',
      options: [['any', 'Some with, some without'], ['with', 'Every problem regroups'], ['without', 'No regrouping']],
      show: v => ['2', '3', '4'].includes(v.grade) && ['add', 'sub', 'addsub'].includes(v.skill) },
    { id: 'count', label: 'Problems', type: 'select', options: [['12', '12'], ['20', '20'], ['24', '24']], def: '20' },
    { id: 'est', label: 'Estimate first (an Estimate blank before each answer; the key rounds each number to its leading place)', type: 'check', def: false, show: canEst },
    { id: 'size', label: 'Number size', type: 'select', def: 'mixed', options: [['mixed', 'Two- and three-digit numbers'], ['100', 'Two-digit numbers, within 100']],
      show: v => v.grade === '2' && ['add', 'sub', 'addsub', 'missing'].includes(v.skill) },
  ],
  make(v, r) {
    const g = v.grade, skill = v.skill;
    const regroup = ['2', '3', '4'].includes(g) && ['add', 'sub', 'addsub'].includes(skill) ? v.regroup : 'any';
    const size = g === '2' ? v.size : 'mixed';
    const n = +v.count, est = !!v.est && canEst(v);
    const label = SKILLS[g].find(s => s[0] === skill)[1];
    const gradeName = GRADES.find(x => x[0] === g)[1];

    if (skill === 'missing') {   // a full sheet of 7 + ? = 15 problems, sized by the grade
      const key = p => `${p.x}${p.op}${p.y}${p.hide}`;
      const probs = r.distinct(n, () => missing(r, g, size), key);
      const line = p => `${p.hide === 'x' ? '?' : show(p.x)} ${SIGN[p.op]} ${p.hide === 'y' ? '?' : show(p.y)} = ${show(p.a)}`;
      const items = probs.map(p => ({ q: line(p), a: show(p.m), p, missing: true }));
      const ex = r.distinct(1, () => { const e = missing(r, g, size); return e && items.some(i => i.q === line(e)) ? null : e; })[0] || probs[0];
      const undo = { '+': 'subtract', '-': ex.hide === 'x' ? 'add' : 'subtract', x: 'divide', '/': ex.hide === 'x' ? 'multiply' : 'divide' }[ex.op];
      const think = ex.op === '+' ? `${show(ex.a)} − ${show(ex.hide === 'x' ? ex.y : ex.x)}` : ex.op === '-' ? (ex.hide === 'x' ? `${show(ex.a)} + ${show(ex.y)}` : `${show(ex.x)} − ${show(ex.a)}`)
        : ex.op === 'x' ? `${show(ex.a)} ÷ ${show(ex.hide === 'x' ? ex.y : ex.x)}` : (ex.hide === 'x' ? `${show(ex.a)} × ${show(ex.y)}` : `${show(ex.x)} ÷ ${show(ex.a)}`);
      const exLine = line(ex).replace('?', `<b>${show(ex.m)}</b>`);
      const how = `To find the missing number, ${undo}: ${think} = ${show(ex.m)}. Then check by putting it back in.`;
      const rows = items.map(i => `${i.p.hide === 'x' ? blank(i.a, 3) : show(i.p.x)} ${SIGN[i.p.op]} ${i.p.hide === 'y' ? blank(i.a, 3) : show(i.p.y)} = ${show(i.p.a)}`);
      return {
        title: `${label}: ${gradeName}`, level: gradeName,
        ican: 'I can find the missing number in an equation and check it.',
        directions: 'Find the number that makes each equation true. Write it on the line. Check by putting it back in.',
        minutes: n > 20 ? 25 : 20, materials: 'pencil' + (g === '1' ? ', counters or a number line' : ''),
        parts: [part('', example(exLine, how)), part('Practice', fill(rows, g === '4' ? 2 : 3))], items,
        mistakes: 'Doing the operation shown instead of undoing it: for 7 + ? = 15, adding 7 and 15. Ask what number goes in the box, then check by putting it back.',
        notes: 'Press New sheet for another set at the same level. Problems hide the first number as often as the second, so students have to think about which operation undoes the one shown.',
      };
    }

    const ops = g === '6' ? { div: ['dd'], decmul: ['dx'], mix: ['dd', 'dx'] }[skill] : opsFor(skill);
    const mix = ops;
    const big = !(g === 'k' || g === '1' || (g === '3' && (skill === 'mul' || skill === 'div' || skill === 'muldiv')));
    const pick = () => {
      let op = r.pick(mix);
      if (g === '5' && skill === 'mix' && (op === '+' || op === '-')) op = 'd' + op;
      const p = problem(r, g === '5' && skill === 'mix' && op[0] !== 'd' ? '5' : g, op, regroup, size);
      if (est && p && p.op === '-' && estimate(p) <= 0) return null;   // an estimate of 0 teaches nothing
      return p;
    };
    const probs = r.distinct(n, pick, p => `${p.x}${p.op}${p.y}`);
    const estOf = p => est && !p.dec && (p.op === '+' || p.op === '-' || p.op === 'x') ? estimate(p) : null;
    const items = probs.map(p => { const e = estOf(p); return { q: `${show(p.x)} ${SIGN[p.op]} ${show(p.y)}`, a: show(p.a), p, ...(e != null ? { est: e } : {}) }; });
    // worked example, made from a fresh problem so it is not one of the practice problems
    const ex = r.distinct(1, () => { const e = pick(); return !e || items.some(i => i.q === `${show(e.x)} ${SIGN[e.op]} ${show(e.y)}`) ? null : e; })[0] || probs[0];
    const exEst = estOf(ex);
    const exLine = `${show(ex.x)} ${SIGN[ex.op]} ${show(ex.y)} = <b>${show(ex.a)}</b>` + (exEst != null ? ` (estimate: ${show(lead(ex.x))} ${SIGN[ex.op]} ${show(lead(ex.y))} = ${show(exEst)})` : '');
    const how = { '+': 'Line up the place values and add from the ones. Carry a ten when a column makes 10 or more.',
      '-': 'Line up the place values and subtract from the ones. When the top digit is smaller, regroup from the next place.',
      x: big ? 'Multiply each place, then add the partial products.' : 'Think of equal groups: 4 × 3 is 4 groups of 3.',
      '/': big ? 'Divide, multiply, subtract, bring down. Anything left over is the remainder, written R.' : 'Think: what times the divisor makes the number?',
      dd: 'Divide as with whole numbers. When a remainder is left, write a decimal point and a zero, bring the zero down and keep dividing until nothing is left.',
      dx: 'Multiply as if there were no decimal points. Then count the decimal places in both numbers and put that many in the answer.' }[ex.op] || 'Line up the decimal points, then add or subtract as with whole numbers.';
    const cell = i => {
      const body = i.p.op === '/' || i.p.op === 'dd' ? longdiv(show(i.p.x), show(i.p.y), show(i.p.a)) : stack(show(i.p.x), SIGN[i.p.op], show(i.p.y), show(i.p.a));
      return i.est != null ? `<div class="gen-estwrap">${body}<div class="gen-est">Estimate ${blank(show(i.est), 3.4)}</div></div>` : body;
    };
    const practice = big
      ? stacks(items.map(cell), g === '6' || g === '5' || g === '4' ? 4 : 5)
      : fill(items.map(i => `${i.q} = ${blank(i.a, 2.6)}`), 3);
    // stretch: three missing-number problems built from practice problems (a + ? = c)
    const stretch = r.sample(items.filter(i => typeof i.p.a === 'number' && !i.p.dec && (i.p.op === '+' || i.p.op === '-' || (i.p.x && i.p.y))), 3);
    const sitems = stretch.map(i => ({ q: `${show(i.p.x)} ${SIGN[i.p.op]} ? = ${show(i.p.a)}`, a: show(i.p.y), p: i.p, stretch: true }));
    const parts = [part('', example(exLine, how)), part('Practice', practice)];
    if (sitems.length) parts.push(part('Stretch: find the missing number', fill(sitems.map(s => `${show(s.p.x)} ${SIGN[s.p.op]} ${blank(s.a, 3)} = ${show(s.p.a)}`), 3, n + 1)));
    const verbs = { '+': 'add', '-': 'subtract', x: 'multiply', '/': 'divide', dd: 'divide', dx: 'multiply' };
    const what = [...new Set(ops.map(o => verbs[o] || verbs[o[o.length - 1]] || 'add and subtract'))].join(' and ');
    const lastOp = ops[0] === 'dd' || ops[0] === 'dx' ? ops[0] : ops[0][ops[0].length - 1];
    return {
      title: `${label}: ${gradeName}`, level: gradeName + (regroup !== 'any' ? (regroup === 'with' ? ', with regrouping' : ', no regrouping') : '') + (size === '100' ? ', within 100' : '') + (est ? ', estimate first' : ''),
      ican: `I can ${what}${g === '6' || (g === '5' && skill === 'dec') ? ' decimals' : ''}${est ? ', estimate first,' : ''} and check my answer.`,
      directions: (big ? 'Solve each problem. Write the answer under the line.' + (ops.includes('/') ? ' Write any remainder with R, like 23 R 4.' : '') + (ops.includes('dd') ? ' Keep dividing past the decimal point until nothing is left.' : '') : 'Solve each problem. Write the answer on the line.')
        + (est ? ' First round each number to its leading place and write your estimate. Then solve, and check that the answer is close to the estimate.' : ''),
      minutes: n > 20 ? 25 : 20, materials: 'pencil' + (g === 'k' || g === '1' ? ', counters or a number line' : ''),
      parts, items: items.concat(sitems),
      mistakes: { '+': 'Forgetting to add the carried ten, and lining up numbers by the left edge instead of the ones place.',
        '-': 'Subtracting the smaller digit from the bigger one in every column, even when the bigger digit is on the bottom.',
        x: 'Leaving out the zero placeholder in the second partial product.', '/': 'A remainder as big as the divisor, which means the quotient can go up by one.',
        dd: 'Stopping at a remainder instead of writing a decimal point and bringing down a zero, and forgetting the decimal point in the quotient.',
        dx: 'Lining up the decimal points as in addition, and counting the decimal places in only one of the numbers.' }[lastOp] || '',
      notes: 'Press New sheet for another set at the same level. The stretch problems reuse three practice problems with one number hidden, so a student who checks back can see the link.'
        + (est ? ' An estimate within a few hundred of the answer is a good one; the key shows the estimate from rounding each number to its leading place.' : ''),
    };
  },
  verify(s) {
    const out = [];
    // a second rounding, done on the number itself rather than its text
    const lead2 = n => { if (n < 10) return n; let k = 1; while (n >= k * 10) k *= 10; return Math.round(n / k) * k; };
    const places = t => (String(t).split('.')[1] || '').length;
    for (const it of s.items) {
      const p = it.p;
      let want;
      if (it.missing) {
        const shown = p.hide === 'x' ? p.y : p.x, a = p.a;
        if (p.op === '+') want = a - shown;
        else if (p.op === '-') want = p.hide === 'x' ? a + p.y : p.x - a;
        else if (p.op === 'x') want = a / shown;
        else want = p.hide === 'x' ? a * p.y : p.x / a;
        if (String(it.a).replace(/,/g, '') !== String(want)) out.push(`${it.q}: key says ${it.a}, should be ${want}`);
        if (!Number.isInteger(want) || want <= 0) out.push(`${it.q}: missing number ${want} is not a counting number`);
        continue;
      }
      if (p.op === 'dd') {   // x / y must end exactly at tenths or hundredths
        const hund = p.x * 100;
        if (hund % p.y) { out.push(`${it.q}: does not end at hundredths`); continue; }
        want = (hund / p.y) / 100;
        const got = parseFloat(String(it.a).replace(/,/g, ''));
        if (Math.abs(got - want) > 1e-9) out.push(`${it.q}: key says ${it.a}, should be ${want}`);
        if (Number.isInteger(want)) out.push(`${it.q}: quotient ${want} is a whole number`);
        if (String(p.y).length !== 2 || p.x < 100 || p.x > 9999) out.push(`${it.q}: sizes off`);
        continue;
      }
      if (p.op === 'dx') {   // multiply the digits as whole numbers, then place the decimal point
        const dx = places(p.x), dy = places(p.y), xi = +String(p.x).replace('.', ''), yi = +String(p.y).replace('.', '');
        const prod = String(xi * yi).padStart(dx + dy + 1, '0');
        const wantText = dx + dy ? prod.slice(0, -(dx + dy)) + '.' + prod.slice(-(dx + dy)) : prod;
        const gotN = parseFloat(String(it.a).replace(/,/g, '')), wantN = parseFloat(wantText);
        if (Math.abs(gotN - wantN) > 1e-9) out.push(`${it.q}: key says ${it.a}, should be ${wantText}`);
        if (!dx) out.push(`${it.q}: first number is not a decimal`);
        continue;
      }
      if (p.dec) want = (p.op === '+' ? p.xh + p.yh : p.xh - p.yh) / 100;
      else if (p.op === '+') want = p.x + p.y;
      else if (p.op === '-') want = p.x - p.y;
      else if (p.op === 'x') want = p.x * p.y;
      else if (p.op === '/') want = p.y ? `${fmt(Math.floor(p.x / p.y), 0).replace(/,/g, '')}${p.x % p.y ? ' R ' + (p.x % p.y) : ''}` : 'x';
      if (it.stretch) { if (String(it.a) !== show(p.y)) out.push(`${it.q}: stretch answer ${it.a}`); continue; }
      const got = p.dec ? parseFloat(String(it.a).replace(/,/g, '')) : String(it.a).replace(/,/g, '');
      if (String(got) !== String(want)) out.push(`${it.q}: key says ${it.a}, should be ${want}`);
      if (!p.dec && (p.op === '-' && p.a < 0)) out.push(`${it.q}: negative answer`);
      if (p.op === '/' && p.y === 0) out.push(`${it.q}: divides by zero`);
      if (it.est != null) {
        const e = p.op === '+' ? lead2(p.x) + lead2(p.y) : p.op === '-' ? lead2(p.x) - lead2(p.y) : lead2(p.x) * lead2(p.y);
        if (e !== it.est) out.push(`${it.q}: estimate ${it.est}, should be ${e}`);
        if (p.op === '-' && e < 0) out.push(`${it.q}: negative estimate`);
      }
    }
    return out;
  },
});
})();
