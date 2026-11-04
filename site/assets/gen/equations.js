// Expressions and Equations generator, grades 6-9. Evaluate expressions (6.EE.2c, 7.NS.3), one-step equations and
// inequalities (6.EE.7-8), two-step and distributive equations and inequalities (7.EE.4), variables on both sides with
// integer or simple fraction answers (8.EE.7), multi-step equations and inequalities (A-REI.3).
// Every equation is built from its answer, and the teacher page lists the steps of each solution.
(() => {
const H = Gen.h, { part, example, svg, esc } = H;
const { gcd } = Gen.m;

const GRADES = [['6', 'Grade 6'], ['7', 'Grade 7'], ['8', 'Grade 8'], ['9', 'Grade 9 (Algebra 1)']];
const SKILLS = {
  6: [['eval', 'Evaluate expressions'], ['one', 'One-step equations'], ['ineq1', 'One-step inequalities'], ['mix', 'Mixed review']],
  7: [['eval', 'Evaluate expressions with integers'], ['two', 'Two-step equations'], ['dist', 'Distributive property equations'], ['ineq2', 'Two-step inequalities'], ['mix', 'Mixed review']],
  8: [['two', 'Two-step equations'], ['both', 'Variables on both sides'], ['dist', 'Distributive property equations'], ['ineq2', 'Two-step inequalities'], ['mix', 'Mixed review']],
  9: [['both', 'Variables on both sides'], ['multi', 'Multi-step equations'], ['ineq', 'Multi-step inequalities'], ['mix', 'Mixed review']],
};
const MIXOF = { 6: ['eval', 'one', 'one', 'ineq1'], 7: ['eval', 'two', 'dist', 'ineq2'], 8: ['two', 'both', 'dist', 'ineq2'], 9: ['both', 'multi', 'ineq'] };
const COUNTS = { eval: [8, 12, 16], ineq: [4, 6, 8], eq: [6, 8, 12], mix: [4, 6, 10] };
const countKey = s => s === 'eval' ? 'eval' : s.startsWith('ineq') ? 'ineq' : 'eq';

/* ---------- writing numbers and terms ---------- */
const MINUS = '−';
const num = n => (n < 0 ? MINUS : '') + Math.abs(n);
const coef = (a, v) => a === 1 ? v : a === -1 ? MINUS + v : num(a) + v;
const lin = (a, b, v) => { if (a === 0) return num(b); const t = coef(a, v); return b === 0 ? t : `${t} ${b < 0 ? MINUS : '+'} ${Math.abs(b)}`; };
const ital = s => s.replace(/(^|[^a-zA-Z&])([a-z])(?![a-zA-Z;])/g, '$1<i>$2</i>');   // variables in italics on the sheet
const fracH = (n, d) => `<span class="gen-frac"><span>${n}</span><span>${d}</span></span>`;
// a value that may be a fraction {n, d}: text "5/2", html stacked
const vtext = q => q.d === 1 ? num(q.n) : `${q.n < 0 ? MINUS : ''}${Math.abs(q.n)}/${q.d}`;
const vhtml = q => q.d === 1 ? num(q.n) : `${q.n < 0 ? MINUS : ''}${fracH(Math.abs(q.n), q.d)}`;
const FLIP = { '<': '>', '>': '<', '≤': '≥', '≥': '≤' };

/* ---------- exact arithmetic parser for verify: + − * / ^ ( ), unary minus, variables ---------- */
function evaluate(src, vars) {
  const R = (n, d = 1) => { if (d < 0) { n = -n; d = -d; } const g = gcd(n, d) || 1; return { n: n / g, d: d / g }; };
  const toks = src.replace(/−/g, '-').match(/\d+|[a-z]|[-+*/^()]/g) || [];
  let i = 0;
  const peek = () => toks[i], take = () => toks[i++];
  function expr() { let a = term(); while (peek() === '+' || peek() === '-') { const op = take(), b = term(); a = op === '+' ? R(a.n * b.d + b.n * a.d, a.d * b.d) : R(a.n * b.d - b.n * a.d, a.d * b.d); } return a; }
  function term() { let a = power(); while (peek() === '*' || peek() === '/') { const op = take(), b = power(); if (op === '/' && b.n === 0) throw new Error('divide by zero'); a = op === '*' ? R(a.n * b.n, a.d * b.d) : R(a.n * b.d, a.d * b.n); } return a; }
  function power() { const a = unary(); if (peek() === '^') { take(); const e = unary(); let p = R(1); for (let k = 0; k < e.n; k++) p = R(p.n * a.n, p.d * a.d); return p; } return a; }
  function unary() { if (peek() === '-') { take(); const a = unary(); return R(-a.n, a.d); } return atom(); }
  function atom() { const t = take(); if (t === '(') { const a = expr(); take(); return a; } if (/\d/.test(t)) return R(+t); if (t in vars) return R(vars[t].n ?? vars[t], vars[t].d ?? 1); throw new Error('bad token ' + t); }
  const out = expr();
  if (i !== toks.length) throw new Error('left over ' + toks.slice(i).join(''));
  return out;
}

/* ---------- problem makers: each returns {kind, disp, mach, ans, steps, ...} ---------- */
const VARS = ['x', 'n', 'y', 'm', 'k', 'p', 'w', 'b'];
const nz = (r, lo, hi) => { for (;;) { const x = r.int(lo, hi); if (x) return x; } };

function makeEval(r, g) {
  const neg = g === '7';
  const val = () => neg ? nz(r, -9, 9) : r.int(1, 10);
  const x = val(), y = val(), a = r.int(2, 9), b = r.int(1, 12), c = r.int(2, 5);
  const T = r.int(1, 9);
  let disp, mach, vars = { x, y }, uses = 'xy';
  if (T === 1) { disp = `${a}x + ${b}`; mach = `${a}*x+${b}`; uses = 'x'; }
  else if (T === 2) { disp = `${a}(x + ${b})`; mach = `${a}*(x+${b})`; uses = 'x'; }
  else if (T === 3) { disp = `x^2 + ${b}`; mach = `x^2+${b}`; uses = 'x'; }
  else if (T === 4) { disp = `${a}x − ${c}y`; mach = `${a}*x-${c}*y`; }
  else if (T === 5) { if ((x + y) % c) return null; disp = `(x + y) ÷ ${c}`; mach = `(x+y)/${c}`; }
  else if (T === 6) { disp = `xy − ${b}`; mach = `x*y-${b}`; }
  else if (T === 7) { disp = `${c}x^2 − y`; mach = `${c}*x^2-y`; }
  else if (T === 8) { const p = r.int(2, 9), q = r.int(2, 9), s = r.int(2, 6), t = r.int(1, 20);
    const forms = [[`${t} + ${p} × ${q}`, `${t}+${p}*${q}`], [`(${t} + ${p}) × ${s}`, `(${t}+${p})*${s}`], [`${p}^2 − ${s} × ${q}`, `${p}^2-${s}*${q}`], [`${p * s} ÷ ${s} + ${q} × ${t % 6 + 2}`, `${p * s}/${s}+${q}*${t % 6 + 2}`]];
    [disp, mach] = r.pick(forms); vars = {}; uses = ''; }
  else { disp = `${b} − ${a}x + y`; mach = `${b}-${a}*x+y`; if (!neg && b - a * x + y < 0) return null; }
  const ans = evaluate(mach, vars);   // exact; a quotient that is not whole is thrown out below
  if (ans.d !== 1 || (!neg && ans.n < 0) || Math.abs(ans.n) > 400) return null;
  const given = uses.split('').filter(Boolean).map(k => `${k} = ${num(vars[k])}`).join(' and ');
  const subd = disp.replace(/(\d)([xy])/g, '$1·$2').replace(/xy/g, 'x·y').replace(/[xy]/g, k => vars[k] < 0 ? `(${num(vars[k])})` : String(vars[k]));
  return { kind: 'eval', disp, mach, vars: uses ? vars : {}, given, ans: { n: ans.n, d: 1 }, q: `${disp} | ${given}`,
    steps: [uses ? `${shown(subd)}` : shown(disp), num(ans.n)] };
}
const shown = s => s.replace(/\^2/g, '²').replace(/-/g, MINUS);

function makeEq(r, g, kind) {
  const v = r.pick(VARS);
  const V = s => s.replace(/x/g, v);
  let disp, mach, sol, steps;
  if (kind === 'one') {
    const T = r.int(1, 4), s = r.int(0, 20), a = r.int(2, 12);
    if (T === 1) { const b = s + a; disp = `${v} + ${a} = ${b}`; mach = `x+${a}=${b}`; steps = [disp, `${v} = ${b} − ${a}  (subtract ${a} from both sides)`]; }
    else if (T === 2) { const b = s - a; if (b < 0) return null; disp = `${v} − ${a} = ${b}`; mach = `x-${a}=${b}`; steps = [disp, `${v} = ${b} + ${a}  (add ${a} to both sides)`]; }
    else if (T === 3) { if (!s) return null; disp = `${a}${v} = ${a * s}`; mach = `${a}*x=${a * s}`; steps = [disp, `${v} = ${a * s} ÷ ${a}  (divide both sides by ${a})`]; }
    else { const q = r.int(1, 12); disp = `${v}/${a} = ${q}`; mach = `x/${a}=${q}`; steps = [disp, `${v} = ${q} × ${a}  (multiply both sides by ${a})`]; sol = { n: q * a, d: 1 }; }
    sol = sol || { n: s, d: 1 };
  } else if (kind === 'two') {
    const s = nz(r, -10, 12);
    if (r.chance(.25)) {   // x/p + q = r
      const p = r.int(2, 5), m = s * p, q = nz(r, -12, 12), rr = s + q;
      disp = `${v}/${p} ${q < 0 ? MINUS : '+'} ${Math.abs(q)} = ${num(rr)}`; mach = `x/${p}+(${q})=${rr}`; sol = { n: m, d: 1 };
      steps = [disp, `${v}/${p} = ${num(rr - q)}  (${q < 0 ? 'add ' + Math.abs(q) + ' to' : 'subtract ' + q + ' from'} both sides)`, `${v} = ${num(m)}  (multiply both sides by ${p})`];
    } else {
      const p = nz(r, g === '7' ? -6 : -9, 9), q = nz(r, -15, 15); if (Math.abs(p) === 1) return null;
      const rr = p * s + q;
      disp = `${V(lin(p, q, 'x'))} = ${num(rr)}`; mach = `(${p})*x+(${q})=${rr}`; sol = { n: s, d: 1 };
      steps = [disp, `${coef(p, v)} = ${num(rr - q)}  (${q < 0 ? 'add ' + Math.abs(q) + ' to' : 'subtract ' + q + ' from'} both sides)`, `${v} = ${num(s)}  (divide both sides by ${num(p)})`];
    }
  } else if (kind === 'dist') {
    const s = nz(r, -10, 10), p = nz(r, -8, 8), q = nz(r, -9, 9); if (Math.abs(p) === 1) return null;
    const rr = p * (s + q);
    disp = `${num(p)}(${V(lin(1, q, 'x'))}) = ${num(rr)}`; mach = `(${p})*(x+(${q}))=${rr}`; sol = { n: s, d: 1 };
    steps = [disp, `${V(lin(p, p * q, 'x'))} = ${num(rr)}  (distribute ${num(p)})`, `${coef(p, v)} = ${num(rr - p * q)}  (${p * q < 0 ? 'add ' + Math.abs(p * q) + ' to' : 'subtract ' + p * q + ' from'} both sides)`, `${v} = ${num(s)}  (divide both sides by ${num(p)})`];
  } else if (kind === 'both' || kind === 'multi') {
    // a x + b = c x + d  (multi: p(x + q) on the left, expanded to a = p, b = p q)
    const fracOk = g === '8' || g === '9';
    const diff = nz(r, -6, 6), c = nz(r, -9, 9), a = c + diff; if (!a) return null;
    let s, top;
    if (fracOk && r.chance(.2) && Math.abs(diff) > 1) { top = nz(r, -20, 20); if (top % diff === 0) return null; s = { n: top, d: diff }; }
    else { const k = nz(r, -10, 10); top = k * diff; s = { n: k, d: 1 }; }
    let b, p = 0, q = 0;
    if (kind === 'multi') { if (Math.abs(a) < 2) return null; p = a; q = nz(r, -8, 8); b = p * q; } else b = nz(r, -15, 15);
    const d = b + top;   // a x + b = c x + d  ->  (a - c) x = d - b = top
    const g2 = gcd(Math.abs(top), Math.abs(diff)); sol = { n: (diff < 0 ? -top : top) / g2, d: Math.abs(diff) / g2 };
    const left = kind === 'multi' ? `${num(p)}(${V(lin(1, q, 'x'))})` : V(lin(a, b, 'x'));
    disp = `${left} = ${V(lin(c, d, 'x'))}`;
    mach = kind === 'multi' ? `(${p})*(x+(${q}))=(${c})*x+(${d})` : `(${a})*x+(${b})=(${c})*x+(${d})`;
    steps = [disp];
    if (kind === 'multi') steps.push(`${V(lin(a, b, 'x'))} = ${V(lin(c, d, 'x'))}  (distribute ${num(p)})`);
    steps.push(`${V(lin(diff, b, 'x'))} = ${num(d)}  (${c < 0 ? 'add ' + coef(-c, v) + ' to' : 'subtract ' + coef(c, v) + ' from'} both sides)`);
    steps.push(`${coef(diff, v)} = ${num(top)}  (${b < 0 ? 'add ' + Math.abs(b) + ' to' : 'subtract ' + b + ' from'} both sides)`);
    steps.push(`${v} = ${vtext(sol)}  (divide both sides by ${num(diff)})`);
    if (sol.d === 1 && diff === 1) steps.pop();
  }
  if (!disp) return null;
  if (sol.d === 1) steps.push(`${v} = ${num(sol.n)}`);
  // tidy: drop a last step that repeats the one before it
  if (steps.length > 2 && steps[steps.length - 1] === steps[steps.length - 2].split('  (')[0]) steps.pop();
  return { kind: 'eq', v, disp, mach, ans: sol, q: disp, steps };
}

function makeIneq(r, g, kind) {
  const v = r.pick(VARS), V = s => s.replace(/x/g, v);
  const rel = r.pick(['<', '>', '≤', '≥']);
  let disp, mach, k, op = rel, steps;
  if (kind === 'ineq1') {
    k = r.int(0, 15); const a = r.int(2, 9), T = r.int(1, 3);
    if (T === 1) { disp = `${v} + ${a} ${rel} ${k + a}`; mach = `x+${a}|${k + a}`; steps = [disp, `${v} ${rel} ${k}  (subtract ${a} from both sides)`]; }
    else if (T === 2) { disp = `${v} − ${a} ${rel} ${k}`; mach = `x-${a}|${k}`; k += a; steps = [disp, `${v} ${rel} ${k}  (add ${a} to both sides)`]; }
    else { if (!k) return null; disp = `${a}${v} ${rel} ${a * k}`; mach = `${a}*x|${a * k}`; steps = [disp, `${v} ${rel} ${k}  (divide both sides by ${a})`]; }
  } else if (kind === 'ineq2') {
    k = nz(r, -8, 8); const p = nz(r, -6, 6), q = nz(r, -12, 12); if (Math.abs(p) === 1) return null;
    const rr = p * k + q;
    disp = `${V(lin(p, q, 'x'))} ${rel} ${num(rr)}`; mach = `(${p})*x+(${q})|${rr}`;
    if (p < 0) op = FLIP[rel];
    steps = [disp, `${coef(p, v)} ${rel} ${num(rr - q)}  (${q < 0 ? 'add ' + Math.abs(q) + ' to' : 'subtract ' + q + ' from'} both sides)`,
      `${v} ${op} ${num(k)}  (divide both sides by ${num(p)}${p < 0 ? '; dividing by a negative flips the sign' : ''})`];
  } else {
    // a(x + q) rel c x + d  or  a x + b rel c x + d
    k = nz(r, -8, 8); const diff = nz(r, -5, 5), c = nz(r, -6, 6), a = c + diff; if (!a) return null;
    const useP = Math.abs(a) > 1 && r.chance(.5), q = nz(r, -6, 6), b = useP ? a * q : nz(r, -12, 12), d = b + diff * k;
    const left = useP ? `${num(a)}(${V(lin(1, q, 'x'))})` : V(lin(a, b, 'x'));
    disp = `${left} ${rel} ${V(lin(c, d, 'x'))}`;
    mach = useP ? `(${a})*(x+(${q}))|(${c})*x+(${d})` : `(${a})*x+(${b})|(${c})*x+(${d})`;
    if (diff < 0) op = FLIP[rel];
    steps = [disp];
    if (useP) steps.push(`${V(lin(a, b, 'x'))} ${rel} ${V(lin(c, d, 'x'))}  (distribute ${num(a)})`);
    steps.push(`${V(lin(diff, b, 'x'))} ${rel} ${num(d)}  (${c < 0 ? 'add ' + coef(-c, v) + ' to' : 'subtract ' + coef(c, v) + ' from'} both sides)`);
    steps.push(`${coef(diff, v)} ${rel} ${num(diff * k)}  (${b < 0 ? 'add ' + Math.abs(b) + ' to' : 'subtract ' + b + ' from'} both sides)`);
    steps.push(`${v} ${op} ${num(k)}  (divide both sides by ${num(diff)}${diff < 0 ? '; dividing by a negative flips the sign' : ''})`);
    if (diff === 1) steps.pop();
  }
  return { kind: 'ineq', v, disp, mach, rel, op, k, q: disp, steps, ansText: `${v} ${op} ${num(k)}` };
}

function make1(r, g, skill) {
  if (skill === 'eval') return makeEval(r, g);
  if (skill === 'ineq1' || skill === 'ineq2' || skill === 'ineq') return makeIneq(r, g, skill);
  return makeEq(r, g, skill);
}

// number line for an inequality: blank on the student copy, the graph on the key
function ineqLine(k, op, lo) {
  const x0 = 18, x1 = 302, y = 22, n = 10, step = (x1 - x0) / n, X = t => x0 + (t - lo) * step;
  let s = `<line x1="${x0 - 12}" y1="${y}" x2="${x1 + 12}" y2="${y}" stroke="#222" stroke-width="1.5"/>` +
    `<path d="M${x0 - 12} ${y} l8 -5 v10 z M${x1 + 12} ${y} l-8 -5 v10 z" fill="#222"/>`;
  for (let t = lo; t <= lo + n; t++) s += `<line x1="${X(t)}" y1="${y - 6}" x2="${X(t)}" y2="${y + 6}" stroke="#222" stroke-width="1.2"/><text x="${X(t)}" y="${y + 21}" text-anchor="middle" font-size="12">${num(t)}</text>`;
  const right = op === '>' || op === '≥', closed = op === '≤' || op === '≥', end = right ? x1 + 10 : x0 - 10;
  s += `<g class="ws-keyonly"><line x1="${X(k)}" y1="${y}" x2="${end}" y2="${y}" stroke="#b03020" stroke-width="5"/>` +
    `<circle cx="${X(k)}" cy="${y}" r="6" fill="${closed ? '#b03020' : '#fff'}" stroke="#b03020" stroke-width="2.5"/></g>`;
  return svg(320, 48, s, `Number line from ${lo} to ${lo + n} for graphing the answer`);
}

Gen.add('equations', {
  title: 'Expressions and Equations', type: 'Practice',
  css: `.eq-grid{display:grid;grid-template-columns:1fr 1fr;gap:4px 30px;margin:6px 0 10px}
.eq-cell{break-inside:avoid;display:flex;flex-direction:column;border-top:1px solid #ddd;padding-top:6px}
.eq-cell > p{margin:0;font-size:17px}
.eq-cell .eq-work{flex:1;min-height:.85in}
.eq-cell.eq-eval .eq-work{min-height:.55in}
.eq-cell.eq-ineq .eq-work{min-height:.5in}
.eq-ans{margin:0 0 4px;text-align:right;font-size:16px}
.eq-cell svg{max-width:3.1in;margin:2px 0 4px}
.eq-steps{margin:4px 0;padding-left:1.8em;font-size:14px;columns:2;column-gap:24px}
.eq-steps li{margin-bottom:6px;break-inside:avoid}
.eq-steps span{display:block}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '7' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => SKILLS[v.grade], def: 'two' },
    { id: 'count', label: 'Problems', type: 'select', def: 'm',
      options: v => { const c = COUNTS[v.skill === 'mix' ? 'mix' : countKey(v.skill)]; return [['s', `Fewer (${c[0]})`], ['m', `Standard (${c[1]})`], ['l', `More (${c[2]})`]]; } },
  ],
  make(v, r) {
    const g = v.grade, skill = v.skill, n = COUNTS[skill === 'mix' ? 'mix' : countKey(skill)][{ s: 0, m: 1, l: 2 }[v.count]];
    const label = SKILLS[g].find(s => s[0] === skill)[1], gname = GRADES.find(x => x[0] === g)[1];
    const pickSkill = () => skill === 'mix' ? r.pick(MIXOF[g]) : skill;
    let ps = r.distinct(n + 1, () => make1(r, g, pickSkill()), p => p.q.replace(/\b[a-z]\b/g, 'x'));
    if (skill === 'mix') ps = [ps[0]].concat(ps.slice(1).sort((a, b) => ['eval', 'eq', 'ineq'].indexOf(a.kind) - ['eval', 'eq', 'ineq'].indexOf(b.kind)));
    const ex = ps.shift();
    const items = [], cells = [];
    const answerOf = p => p.kind === 'ineq' ? p.ansText : p.kind === 'eval' ? num(p.ans.n) : vtext(p.ans);
    ps.forEach((p, i) => {
      const a = answerOf(p);
      items.push({ q: p.q, a, kind: p.kind, mach: p.mach, vars: p.vars, v: p.v, rel: p.rel });
      let head, foot = '';
      if (p.kind === 'eval') { head = p.given ? `Evaluate ${ital(shown(p.disp))} when ${ital(p.given)}.` : `Evaluate ${shown(p.disp)}.`; foot = `<p class="eq-ans">= ${H.blank(a, 4)}</p>`; }
      else if (p.kind === 'eq') foot = `<p class="eq-ans"><i>${p.v}</i> = <span class="ws-blank" style="min-width:4em"><span class="ws-ans">${vhtml(p.ans)}</span></span></p>`;
      else { const lo = p.k - 5 + r.int(-3, 3); foot = `<p class="eq-ans">${H.blank(p.ansText, 5)}</p>${ineqLine(p.k, p.op, lo)}`; }
      if (!head) head = `${p.kind === 'ineq' ? 'Solve and graph:' : 'Solve:'} ${ital(shown(p.disp))}`;
      cells.push(`<div class="eq-cell eq-${p.kind}"><p><span class="ws-num">${i + 1}.</span> ${head}</p><div class="eq-work"></div>${foot}</div>`);
    });
    const exSteps = ex.steps.map(s => { const [m, why] = s.split('  ('); return `${ital(shown(m))}${why ? ` <span style="color:#555">(${esc(why.slice(0, -1))})</span>` : ''}`; });
    const exHtml = example(ex.kind === 'eval' ? `Evaluate ${ital(shown(ex.disp))}${ex.given ? ` when ${ital(ex.given)}` : ''}: ${exSteps.map(s => s).join(' = ')}` : exSteps.join('<br>'),
      ex.kind === 'eval' ? 'Put each value in place of its letter, then use the order of operations: parentheses, exponents, multiply and divide, add and subtract.'
        : ex.kind === 'ineq' ? (g === '6' ? 'Solve it like an equation: do the same thing to both sides and keep the inequality sign. Then graph every number that works.' : 'Solve it like an equation. If you multiply or divide both sides by a negative number, flip the inequality sign.')
          : 'Do the same thing to both sides to undo each step, in reverse order. Check by putting your answer back in.');
    const parts = [part('', exHtml), part('Practice', `<div class="eq-grid">${cells.join('')}</div>`)];
    const hasIneq = ps.some(p => p.kind === 'ineq'), hasEq = ps.some(p => p.kind === 'eq'), hasEval = ps.some(p => p.kind === 'eval');
    const fracs = (g === '8' || g === '9') && ps.some(p => p.kind === 'eq' && p.ans.d > 1);
    const dirs = [];
    if (hasEval) dirs.push('For each expression, put in the values and write the result on the line.');
    if (hasEq) dirs.push('Solve each equation in the space. Write the value of the variable on the line.' + ((g === '8' || g === '9') ? ' If it is not a whole number, write it as a fraction in simplest form.' : ''));
    if (hasIneq) dirs.push('Solve each inequality and write it on the line, like x > 3. Then graph it on the number line: open circle for &lt; or &gt;, closed circle for ≤ or ≥.');
    const teacher = `<h3>Solutions, step by step</h3><ol class="eq-steps">${ps.map(p => `<li>${p.steps.map(s => `<span>${ital(shown(esc(s)))}</span>`).join('')}${p.kind === 'eval' ? '' : ''}</li>`).join('')}</ol>`;
    const mistakes = [hasEval && 'Writing 3x with x = 4 as 34 instead of 3 × 4, and adding before multiplying.' + (g === '7' ? ' Squaring a negative: (−3)² is 9.' : ''),
      hasEq && 'Undoing steps in the wrong order (dividing before subtracting), and changing only one side.' + (skill === 'dist' || skill === 'multi' ? ' Multiplying only the first term inside the parentheses.' : ''),
      hasIneq && 'Forgetting to flip the sign when dividing by a negative, and using a closed circle for &lt; or &gt;.'].filter(Boolean).join(' ');
    return {
      title: `${label}: ${gname}`, level: gname,
      ican: { eval: 'I can evaluate an expression by putting in values and using the order of operations.', one: 'I can solve one-step equations.', ineq1: 'I can solve and graph one-step inequalities.',
        two: 'I can solve two-step equations.', dist: 'I can use the distributive property to solve equations.', ineq2: 'I can solve and graph two-step inequalities.',
        both: 'I can solve equations with the variable on both sides.', multi: 'I can solve multi-step equations.', ineq: 'I can solve and graph multi-step inequalities.',
        mix: 'I can choose the steps to solve expressions, equations and inequalities.' }[skill],
      directions: dirs.join(' '), minutes: n > 10 ? 30 : 25, materials: 'pencil',
      parts, items, teacher, mistakes,
      notes: `Every problem is built from its answer, so answers are whole numbers${fracs ? ' or simple fractions' : ''}. The step list below shows one clear way to solve each; other correct orders are fine. Students can check an equation by putting the answer back in.${hasIneq ? ' The key shows each inequality graphed.' : ''}`,
    };
  },
  verify(s) {
    const out = [];
    const read = t => { t = String(t).replace(/−/g, '-').trim(); let m = t.match(/^(-?\d+)\/(\d+)$/); if (m) return { n: +m[1], d: +m[2] }; m = t.match(/^-?\d+$/); return m ? { n: +t, d: 1 } : null; };
    for (const it of s.items) {
      try {
        if (it.kind === 'eval') {
          const want = evaluate(it.mach, it.vars), got = read(it.a);
          if (!got || got.n * want.d !== want.n * got.d) out.push(`${it.q}: key says ${it.a}, works out to ${want.n}/${want.d}`);
          continue;
        }
        const [L, Rt] = it.mach.split(it.kind === 'eq' ? '=' : '|');
        // each side is linear: find slope and intercept of left minus right from x = 0 and x = 1
        const D = x => { const a = evaluate(L, { x }), b = evaluate(Rt, { x }); return { n: a.n * b.d - b.n * a.d, d: a.d * b.d }; };
        const d0 = D(0), d1 = D(1);
        const c = d0.n / d0.d, m = d1.n / d1.d - c;
        if (Math.abs(m) < 1e-12) { out.push(`${it.q}: no single solution`); continue; }
        if (it.kind === 'eq') {
          const got = read(it.a);
          if (!got) { out.push(`${it.q}: cannot read ${it.a}`); continue; }
          const at = D({ n: got.n, d: got.d });
          if (at.n !== 0) out.push(`${it.q}: ${it.a} does not make both sides equal`);
          if (got.d > 1 && gcd(got.n, got.d) !== 1) out.push(`${it.q}: ${it.a} not in simplest form`);
        } else {
          const mm = String(it.a).replace(/−/g, '-').match(/^([a-z]) ([<>≤≥]) (-?\d+)$/);
          if (!mm) { out.push(`${it.q}: cannot read ${it.a}`); continue; }
          const k = +mm[3], holds = x => { const dd = D({ n: Math.round(x * 2), d: 2 }), val = dd.n / dd.d; return { '<': val < 0, '>': val > 0, '≤': val <= 0, '≥': val >= 0 }[it.rel]; };
          const claims = x => ({ '<': x < k, '>': x > k, '≤': x <= k, '≥': x >= k }[mm[2]]);
          for (const x of [k - 3, k - 1, k - 0.5, k, k + 0.5, k + 1, k + 3]) if (holds(x) !== claims(x)) { out.push(`${it.q}: key ${it.a} is wrong at ${it.v} = ${x}`); break; }
        }
      } catch (e) { out.push(`${it.q}: ${e.message}`); }
    }
    return out;
  },
});
})();
