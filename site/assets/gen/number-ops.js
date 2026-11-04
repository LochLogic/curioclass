// Number Operations generator, grades K-5 (the reference generator: other generators follow this shape).
// Grade sets the size of the numbers; skill picks the operation; regrouping is a choice for addition and subtraction.
(() => {
const { blank, part, example, fill, stacks, stack, longdiv } = Gen.h;
const { fmt } = Gen.m;

const GRADES = [['k', 'Kindergarten'], ['1', 'Grade 1'], ['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5']];
const SKILLS = {  // which skills each grade offers
  k: [['add', 'Addition'], ['sub', 'Subtraction'], ['addsub', 'Addition and subtraction']],
  1: [['add', 'Addition'], ['sub', 'Subtraction'], ['addsub', 'Addition and subtraction']],
  2: [['add', 'Addition'], ['sub', 'Subtraction'], ['addsub', 'Addition and subtraction']],
  3: [['add', 'Addition'], ['sub', 'Subtraction'], ['mul', 'Multiplication facts'], ['div', 'Division facts'], ['muldiv', 'Multiplication and division'], ['mix', 'All four']],
  4: [['add', 'Addition'], ['sub', 'Subtraction'], ['mul', 'Multiplication'], ['div', 'Division with remainders'], ['mix', 'All four']],
  5: [['mul', 'Multiplication'], ['div', 'Long division'], ['dec', 'Adding and subtracting decimals'], ['mix', 'All four']],
};
const SIGN = { '+': '+', '-': '−', 'x': '×', '/': '÷' };

// the numbers for one problem: returns {x, op, y, a} where a is the answer text
function problem(r, g, op, regroup) {
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
}

function opsFor(skill) {
  return { add: ['+'], sub: ['-'], addsub: ['+', '-'], mul: ['x'], div: ['/'], muldiv: ['x', '/'], mix: ['+', '-', 'x', '/'], dec: ['d+', 'd-'] }[skill];
}
const show = n => typeof n === 'number' ? fmt(n, 0) : String(n);

Gen.add('number-ops', {
  title: 'Number Operations', type: 'Practice',
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '2' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => SKILLS[v.grade], def: 'add' },
    { id: 'regroup', label: 'Regrouping', type: 'select', def: 'any',
      options: [['any', 'Some with, some without'], ['with', 'Every problem regroups'], ['without', 'No regrouping']],
      show: v => ['2', '3', '4'].includes(v.grade) && ['add', 'sub', 'addsub'].includes(v.skill) },
    { id: 'count', label: 'Problems', type: 'select', options: [['12', '12'], ['20', '20'], ['24', '24']], def: '20' },
  ],
  make(v, r) {
    const g = v.grade, skill = v.skill, ops = opsFor(skill);
    let mix = skill === 'mix' && g === '5' ? ['+', '-', 'x', '/'] : ops;
    const regroup = ['2', '3', '4'].includes(g) && ['add', 'sub', 'addsub'].includes(skill) ? v.regroup : 'any';
    const n = +v.count;
    const big = !(g === 'k' || g === '1' || (g === '3' && (skill === 'mul' || skill === 'div' || skill === 'muldiv')));
    const pick = () => {
      let op = r.pick(mix);
      if (g === '5' && skill === 'mix' && (op === '+' || op === '-')) op = 'd' + op;
      return problem(r, g === '5' && skill === 'mix' && op[0] !== 'd' ? '5' : g, op, regroup);
    };
    const probs = r.distinct(n, pick, p => `${p.x}${p.op}${p.y}`);
    const items = probs.map(p => ({ q: `${show(p.x)} ${SIGN[p.op]} ${show(p.y)}`, a: show(p.a), p }));
    const label = SKILLS[g].find(s => s[0] === skill)[1];
    // worked example, made from a fresh problem so it is not one of the practice problems
    const ex = r.distinct(1, () => { const e = pick(); return items.some(i => i.q === `${show(e.x)} ${SIGN[e.op]} ${show(e.y)}`) ? null : e; })[0] || probs[0];
    const exLine = `${show(ex.x)} ${SIGN[ex.op]} ${show(ex.y)} = <b>${show(ex.a)}</b>`;
    const how = { '+': 'Line up the place values and add from the ones. Carry a ten when a column makes 10 or more.',
      '-': 'Line up the place values and subtract from the ones. When the top digit is smaller, regroup from the next place.',
      x: big ? 'Multiply each place, then add the partial products.' : 'Think of equal groups: 4 × 3 is 4 groups of 3.',
      '/': big ? 'Divide, multiply, subtract, bring down. Anything left over is the remainder, written R.' : 'Think: what times the divisor makes the number?' }[ex.op] || 'Line up the decimal points, then add or subtract as with whole numbers.';
    const practice = big
      ? stacks(items.map(i => i.p.op === '/' ? longdiv(show(i.p.x), show(i.p.y), show(i.p.a)) : stack(show(i.p.x), SIGN[i.p.op], show(i.p.y), show(i.p.a))), g === '5' || g === '4' ? 4 : 5)
      : fill(items.map(i => `${i.q} = ${blank(i.a, 2.6)}`), 3);
    // stretch: three missing-number problems built from practice problems (a + ? = c)
    const stretch = r.sample(items.filter(i => typeof i.p.a === 'number' && !i.p.dec && (i.p.op === '+' || i.p.op === '-' || (i.p.x && i.p.y))), 3);
    const sitems = stretch.map(i => ({ q: `${show(i.p.x)} ${SIGN[i.p.op]} ? = ${show(i.p.a)}`, a: show(i.p.y), p: i.p, stretch: true }));
    const parts = [part('', example(exLine, how)), part('Practice', practice)];
    if (sitems.length) parts.push(part('Stretch: find the missing number', fill(sitems.map(s => `${show(s.p.x)} ${SIGN[s.p.op]} ${blank(s.a, 3)} = ${show(s.p.a)}`), 3, n + 1)));
    const verbs = { '+': 'add', '-': 'subtract', x: 'multiply', '/': 'divide' };
    const what = [...new Set(ops.map(o => verbs[o[o.length - 1]] || 'add and subtract'))].join(' and ');
    return {
      title: `${label}: ${GRADES.find(x => x[0] === g)[1]}`, level: GRADES.find(x => x[0] === g)[1] + (regroup !== 'any' ? (regroup === 'with' ? ', with regrouping' : ', no regrouping') : ''),
      ican: `I can ${what}${g === '5' && skill === 'dec' ? ' decimals' : ''} and check my answer.`,
      directions: big ? 'Solve each problem. Write the answer under the line.' + (ops.includes('/') ? ' Write any remainder with R, like 23 R 4.' : '') : 'Solve each problem. Write the answer on the line.',
      minutes: n > 20 ? 25 : 20, materials: 'pencil' + (g === 'k' || g === '1' ? ', counters or a number line' : ''),
      parts, items: items.concat(sitems),
      mistakes: { '+': 'Forgetting to add the carried ten, and lining up numbers by the left edge instead of the ones place.',
        '-': 'Subtracting the smaller digit from the bigger one in every column, even when the bigger digit is on the bottom.',
        x: 'Leaving out the zero placeholder in the second partial product.', '/': 'A remainder as big as the divisor, which means the quotient can go up by one.' }[ops[0][ops[0].length - 1]] || '',
      notes: 'Press New sheet for another set at the same level. The stretch problems reuse three practice problems with one number hidden, so a student who checks back can see the link.',
    };
  },
  verify(s) {
    const out = [];
    const num = x => typeof x === 'number' ? x : x;
    for (const it of s.items) {
      const p = it.p;
      let want;
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
      void num;
    }
    return out;
  },
});
})();
