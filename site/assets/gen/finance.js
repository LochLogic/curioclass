// Money and Finance generator, grades 5-12. Personal finance and economics with every number invented and every
// answer worked out on the key. Six areas, each with skills sized by grade:
//   Earning and taxes: hourly, overtime (1.5 times after 40 hours) and salary pay (6.RP.3, 7.RP.3); gross to net pay
//     with made-up deduction rates; reading and labeling a pay stub; a simplified tax return with made-up brackets.
//     Tax rates are always printed as made-up rates for practice, never as current tax law.
//   Spending and budgets: cost totals from a price list (picnic, market booth, e-bike, show, film, recording, concert
//     budgets) with category totals, percents and a bar graph; unit price and the better buy (6.RP.2-3); sales tax;
//     discounts, tips, markups, commission and percent change (7.RP.3); the 50/30/20 budget; a spending log against a
//     budget; a budget circle graph (7.RP.3, 6.SP.4 style display).
//   Saving and interest: simple interest (I = Prt) with a table and graph at two rates; simple against compound year
//     by year; the compound interest formula A = P(1 + r/n)^(nt) (A-SSE.1b, F-LE.2, F-BF.2); annual, monthly and daily
//     compounding; the rule of 72; APR and APY; monthly deposits and starting early (a geometric series, A-SSE.4);
//     savings goals and emergency funds; raises, returns and inflation; real values from a price index.
//   Credit, loans and college costs: a credit card balance month by month (minimum against a fixed payment); the
//     loan payment formula M = P i / (1 - (1 + i)^(-n)) with total interest (A-SSE.4); the first rows of an
//     amortization table; loan costs at several rates and terms; comparing two college award letters.
//   Insurance, investing and big purchases: insurance plans across good and bad years (deductibles, coinsurance and an
//     out-of-pocket maximum); one company or a basket of five; share price percent change; depreciation; total cost
//     of ownership over five years; buying stock on margin (US history, 1929).
//   Economics: demand and supply schedules and curves, equilibrium, shortage and surplus, price ceilings and floors,
//     shift or slide, double shifts, price elasticity (midpoint method) and the total revenue test, marginal benefit
//     and cost, profit where marginal revenue meets marginal cost, the production possibilities frontier, break-even,
//     exchange rates, the money multiplier, GDP by the expenditure approach.
// Standards: Jump$tart National Standards for Personal Financial Education (Earning Income, Spending, Saving,
// Investing, Managing Credit, Managing Risk); CCSS 6.RP.3, 7.RP.3, 7.EE.3, A-SSE.4, F-LE.2; Council for Economic
// Education Voluntary National Content Standards in Economics 1, 2, 7, 8, 9 (scarcity, marginal analysis, markets,
// prices, competition), 11, 12 (money, banking), 15 (growth and GDP) and 5 (trade). Money is kept in whole cents and
// rounded half up; verify() re-works every answer by a second route (balances month by month against the closed
// formula, bisection for loan payments, a bracket table against a running tax sum).
(() => {
const h = Gen.h, { part, example, blank, esc, lines } = h;
const { fmt } = Gen.m;

/* ---------- formatting and exact money math (money is kept in whole cents) ---------- */
const usd = c => { c = Math.round(c); const neg = c < 0; c = Math.abs(c); return `${neg ? '−' : ''}$${fmt(Math.floor(c / 100), 0)}.${String(c % 100).padStart(2, '0')}`; };
const usd0 = d => `${d < 0 ? '−' : ''}$${fmt(Math.abs(d), 0)}`;
const pc = (x, dp = 2) => `${Gen.m.minus(fmt(x, dp))}%`;
const fix = (x, dp) => { const s = (Math.round(x * 10 ** dp) / 10 ** dp).toFixed(dp); return Gen.m.minus(s.replace(/^(-?)(\d+)/, (m, s1, d) => s1 + fmt(+d, 0))); };
const half = (c, bp) => Math.floor((c * bp + 5000) / 10000);   // whole cents times bp/10,000, rounded half up, exact
const edgy = x => Math.abs((Math.abs(x) % 1) - 0.5) < 1e-4;      // x sits too near a rounding edge to round safely
const A = t => `<span class="ws-ans">${esc(t)}</span>`;
const T = (head, rows, cls = '') => `<table class="ws-table fin-t${cls ? ' ' + cls : ''}"><thead><tr>${head.map(x => `<th>${x}</th>`).join('')}</tr></thead><tbody>${rows.map(r => `<tr>${r.map(x => `<td>${x}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
const box = html => `<div class="fin-box">${html}</div>`;
const I = (q, a, k, p = {}) => ({ q, a: String(a), k, p });
const ql = (n, html, ansLines) => `<div class="ws-q"><p><span class="ws-num">${n}.</span> ${html}</p>${ansLines || ''}</div>`;
const aline = (label, a, em = 7) => `<div class="fin-l"><span>${label}</span>${blank(a, em)}</div>`;
const prob = (n, html, rows) => `<div class="fin-p"><p><span class="ws-num">${n}.</span> ${html}</p>${rows.join('')}</div>`;
const probs = cells => `<div class="fin-ps">${cells.join('')}</div>`;
const MADEUP = 'Made-up rates for practice, not real tax law';
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

const NAMES = ['Ava', 'Ben', 'Carlos', 'Chloe', 'Diego', 'Elena', 'Emma', 'Ethan', 'Grace', 'Isaac', 'Jamal', 'Kai', 'Leo', 'Lucia', 'Maya', 'Mia',
  'Noah', 'Omar', 'Owen', 'Priya', 'Rosa', 'Sam', 'Sofia', 'Theo', 'Zoe', 'Mateo', 'Nina', 'Jack', 'Ruby', 'Eli', 'Hana', 'Andre', 'Fatima', 'Lena',
  'Marcus', 'Tess', 'Wei', 'Aisha', 'Jonah', 'Iris', 'Rafael', 'Dana', 'Kofi', 'Mei', 'Luis', 'Sara'];
// hourly jobs with a pay range in dollars an hour
const JOBS = [['cashier', 13, 17], ['line cook', 15, 19], ['lifeguard', 13, 16], ['warehouse worker', 17, 22], ['nursing assistant', 17, 21], ['barista', 13, 16],
  ['electrician apprentice', 18, 24], ['dog groomer', 15, 19], ['delivery driver', 17, 22], ['library aide', 13, 16], ['ski instructor', 16, 22], ['bike mechanic', 16, 21],
  ['camp counselor', 13, 16], ['welder', 22, 29], ['dental assistant', 19, 24], ['farm hand', 14, 18], ['grocery stocker', 14, 18], ['house painter', 18, 25]];
// salaried jobs with a range in thousands of dollars a year
const SALARY = [['teacher', 42, 62], ['graphic designer', 45, 70], ['lab technician', 40, 58], ['office manager', 48, 66], ['web developer', 60, 95], ['park ranger', 38, 52],
  ['accountant', 55, 80], ['social worker', 42, 58], ['civil engineer', 65, 98], ['head chef', 40, 60], ['librarian', 44, 64]];
const PERIODS = [['weekly', 52, 'every week'], ['biweekly', 26, 'every two weeks'], ['semimonthly', 24, 'twice a month'], ['monthly', 12, 'once a month']];
const hourly = (r, j, g) => g < 7 ? r.int(j[1] * 2, j[2] * 2) * 50 : r.int(j[1] * 10, j[2] * 10) * 10;   // cents an hour, even so 1.5x is exact

/* ---------- drawing ---------- */
const F = 'font-family="Helvetica, Arial, sans-serif"', RED = '#b03020';
const tx = (x, y, s, a = '') => `<text x="${x}" y="${y}" ${F} fill="#222" ${a}>${esc(s)}</text>`;
const rtx = (x, y, s, a = '') => `<text x="${x}" y="${y}" ${F} fill="${RED}" font-weight="700" ${a}>${esc(s)}</text>`;
// a nice axis step: about `ticks` steps up to max
const nice = (max, ticks = 6) => { const raw = max / ticks, p = 10 ** Math.floor(Math.log10(raw)); for (const m of [1, 2, 2.5, 5, 10]) if (m * p >= raw - 1e-9) return m * p; return 10 * p; };
const top = (max, step) => Math.ceil(max / step - 1e-9) * step;
// an empty graph grid for students to plot on; key(X, Y) draws the answer in red, shown only on the key.
// x, y: [lo, hi, step, label, format]; brk: draw a break mark on the y axis (the scale does not start at zero)
function grid(o) {
  const [x0, x1, xs, xl, xf] = o.x, [y0, y1, ys, yl, yf] = o.y, fy0 = yf || (y => fmt(y, 2));
  const W = o.W || 560, Ht = o.H || 300, R = 18, Tp = o.title ? 32 : 14, B = 52, L = Math.max(60, Math.max(String(fy0(y0)).length, String(fy0(y1)).length) * 7 + 22);
  const X = x => +(L + (x - x0) / (x1 - x0) * (W - L - R)).toFixed(1), Y = y => +(Ht - B - (y - y0) / (y1 - y0) * (Ht - B - Tp)).toFixed(1);
  const fx = xf || (x => fmt(x, 2)), fy = yf || (y => fmt(y, 2));
  let b = o.title ? tx(W / 2, 21, o.title, 'font-size="15" font-weight="700" text-anchor="middle"') : '';
  const nx = Math.round((x1 - x0) / xs), ny = Math.round((y1 - y0) / ys);
  for (let i = 0; i <= nx; i++) { const x = x0 + i * xs; b += `<line x1="${X(x)}" y1="${Tp}" x2="${X(x)}" y2="${Ht - B}" stroke="#bbb" stroke-width="0.8"/>` + tx(X(x), Ht - B + 17, fx(x), `font-size="${o.small ? 10.5 : 12}" text-anchor="middle"`); }
  for (let i = 0; i <= ny; i++) { const y = y0 + i * ys; b += `<line x1="${L}" y1="${Y(y)}" x2="${W - R}" y2="${Y(y)}" stroke="#bbb" stroke-width="0.8"/>` + tx(L - 6, Y(y) + 4, fy(y), 'font-size="12" text-anchor="end"'); }
  b += `<line x1="${L}" y1="${Ht - B}" x2="${W - R}" y2="${Ht - B}" stroke="#222" stroke-width="2"/><line x1="${L}" y1="${Tp}" x2="${L}" y2="${Ht - B}" stroke="#222" stroke-width="2"/>`;
  if (o.brk) b += `<path d="M${L - 7} ${Ht - B - 10} l14 -5 M${L - 7} ${Ht - B - 16} l14 -5" stroke="#222" stroke-width="1.6"/>`;
  b += tx((L + W - R) / 2, Ht - 10, xl, 'font-size="13" font-weight="600" text-anchor="middle"');
  b += `<text x="16" y="${(Tp + Ht - B) / 2}" ${F} fill="#222" font-size="13" font-weight="600" text-anchor="middle" transform="rotate(-90 16 ${(Tp + Ht - B) / 2})">${esc(yl)}</text>`;
  if (o.show) b += o.show(X, Y);
  if (o.key) b += `<g class="ws-ans">${o.key(X, Y)}</g>`;
  return h.svg(W, Ht, b, o.label || o.title || 'Graph grid');
}
const redLine = (pts, X, Y, dash) => `<polyline points="${pts.map(([x, y]) => `${X(x)},${Y(y)}`).join(' ')}" fill="none" stroke="${RED}" stroke-width="2.4"${dash ? ' stroke-dasharray="6 4"' : ''}/>` + pts.map(([x, y]) => `<circle cx="${X(x)}" cy="${Y(y)}" r="3.4" fill="${RED}"/>`).join('');
// a bar graph frame: category names under empty slots; the key draws the bars
function barFrame(cats, vals, title, ylab, money) {
  const mx = Math.max(...vals), step = nice(mx, 5), hi = top(mx, step);
  const W = 560, Ht = 280, L = 84, R = 18, Tp = 32, B = 52, slot = (W - L - R) / cats.length, bw = Math.min(60, slot * 0.55);
  const Y = y => +(Ht - B - y / hi * (Ht - B - Tp)).toFixed(1);
  let b = tx(W / 2, 21, title, 'font-size="15" font-weight="700" text-anchor="middle"');
  for (let y = 0; y <= hi + 1e-9; y += step) b += `<line x1="${L}" y1="${Y(y)}" x2="${W - R}" y2="${Y(y)}" stroke="#bbb" stroke-width="0.8"/>` + tx(L - 6, Y(y) + 4, money ? usd0(y) : fmt(y, 2), 'font-size="12" text-anchor="end"');
  b += `<line x1="${L}" y1="${Ht - B}" x2="${W - R}" y2="${Ht - B}" stroke="#222" stroke-width="2"/><line x1="${L}" y1="${Tp}" x2="${L}" y2="${Ht - B}" stroke="#222" stroke-width="2"/>`;
  let k = '';
  cats.forEach((c, i) => {
    const x = L + slot * i + (slot - bw) / 2;
    b += tx(x + bw / 2, Ht - B + 17, c, `font-size="${c.length > 12 ? 10.5 : 12}" text-anchor="middle"`);
    k += `<rect x="${x.toFixed(1)}" y="${Y(vals[i])}" width="${bw.toFixed(1)}" height="${(Ht - B - Y(vals[i])).toFixed(1)}" fill="#f3d6d0" stroke="${RED}" stroke-width="1.8"/>`;
  });
  b += `<text x="16" y="${(Tp + Ht - B) / 2}" ${F} fill="#222" font-size="13" font-weight="600" text-anchor="middle" transform="rotate(-90 16 ${(Tp + Ht - B) / 2})">${esc(ylab)}</text>`;
  b += `<g class="ws-ans">${k}</g>`;
  return h.svg(W, Ht, b, `Empty bar graph frame: ${title}`);
}

/* ---------- the skills ---------- */
// each: area, label, lo and hi grade, count: [s, m, l] or null, make(v, r, g, n) -> sheet parts
const SK = {};
const VER = {};   // kind -> p -> the answer text, worked a second way

/* ===== Earning and taxes ===== */
SK.pay = { area: 'earn', label: 'Gross pay: hourly, overtime and salary', lo: 6, hi: 12, count: [3, 5, 8],
  make(v, r, g, n) {
    const who = r.sample(NAMES, n + 6), items = [];
    const ws = Array.from({ length: n }, (_, i) => { const j = r.pick(JOBS); return { name: who[i], job: j[0], rt: hourly(r, j, g), hrs: i % 2 ? r.int(g < 7 ? 20 : 24, 40) : r.int(41, g < 7 ? 46 : 50) }; });
    const rows = r.shuffle(ws).map(w => {
      const reg = w.rt * Math.min(w.hrs, 40), ot = Math.max(0, w.hrs - 40) * w.rt * 3 / 2;
      items.push(I(`${w.name}: regular pay`, usd(reg), 'reg', w), I(`${w.name}: overtime pay`, usd(ot), 'ot', w), I(`${w.name}: gross pay`, usd(reg + ot), 'gross', w));
      return [`${w.name}, ${w.job}`, usd(w.rt), w.hrs, A(usd(reg)), A(usd(ot)), A(usd(reg + ot))];
    });
    const m = Math.max(2, Math.round(n / 2)), srows = [];
    for (let i = 0; i < m; i++) for (let t = 0; t < 60; t++) {
      const j = r.pick(SALARY), s = r.int(j[1] * 2, j[2] * 2) * 500, per = r.pick(PERIODS), c = s * 100 / per[1];
      if (edgy(c) || srows.some(x => x.per === per[0])) continue;
      const p = { name: who[n + i], s, per: per[0], n: per[1] };
      srows.push(p); items.push(I(`${p.name}: pay each check`, usd(Math.round(c)), 'salper', p));
      break;
    }
    const ex = { rt: g < 7 ? 1500 : 1620, hrs: 44 };
    return {
      ican: 'I can find gross pay for hourly workers, including overtime, and for salaried workers.',
      directions: 'Overtime is every hour over 40 in a week, paid at 1.5 times the regular rate. Find each worker\'s pay for the week. Then find each salaried worker\'s pay for one paycheck.',
      parts: [part('', example(`${usd(ex.rt)} an hour, ${ex.hrs} hours: regular pay 40 × ${usd(ex.rt)} = ${usd(ex.rt * 40)}. Overtime rate 1.5 × ${usd(ex.rt)} = ${usd(ex.rt * 1.5)}.`,
        `Overtime pay 4 × ${usd(ex.rt * 1.5)} = ${usd(ex.rt * 6)}. Gross pay ${usd(ex.rt * 40)} + ${usd(ex.rt * 6)} = <b>${usd(ex.rt * 46)}</b>.`)),
        part('Hourly workers: one week', T(['Worker', 'Pay per hour', 'Hours', 'Regular pay', 'Overtime pay', 'Gross pay'], rows)),
        part('Salaried workers: one paycheck', T(['Worker', 'Yearly salary', 'Paid', 'Paychecks a year', 'Gross pay each check'],
          srows.map(p => [p.name, usd0(p.s), PERIODS.find(x => x[0] === p.per)[2], A(String(p.n)), A(usd(Math.round(p.s * 100 / p.n)))])))],
      items: items.concat(srows.map(p => I(`${p.name}: paychecks a year`, String(p.n), 'nper', p))),
      mistakes: 'Paying every hour at 1.5 times instead of only the hours over 40, and dividing a salary by 4 for a monthly check (a year has 12 months but 52 weeks, so weekly pay is salary ÷ 52 and twice a month is salary ÷ 24, not 26).',
      notes: 'Gross pay is pay before anything is taken out. Every pay rate is invented and in a realistic range. Weekly, biweekly (26 checks), semimonthly (24 checks) and monthly (12 checks) are the common pay schedules.',
    };
  } };
VER.reg = p => usd(p.rt * (p.hrs > 40 ? 40 : p.hrs));
VER.ot = p => usd(p.hrs > 40 ? (p.hrs - 40) * p.rt * 1.5 : 0);
VER.gross = p => usd(p.rt * p.hrs + Math.max(0, p.hrs - 40) * p.rt * 0.5);
VER.salper = p => usd(Math.round(p.s / ({ weekly: 52, biweekly: 26, semimonthly: 24, monthly: 12 }[p.per]) * 100));
VER.nper = p => String({ weekly: 52, biweekly: 26, semimonthly: 24, monthly: 12 }[p.per]);

// made-up deduction rates for a sheet, in basis points
function rates(r) {
  return [['Income tax', r.pick([800, 1000, 1200, 1500])], ['State tax', r.pick([300, 400, 500])], ['Payroll tax', r.pick([600, 700, 800])], ['Retirement savings', r.pick([300, 400, 500, 600])]];
}
SK.net = { area: 'earn', label: 'Gross to net pay (made-up deduction rates)', lo: 8, hi: 12, count: [3, 4, 5],
  make(v, r, g, n) {
    const R = rates(r), who = r.sample(NAMES, n), items = [];
    const rows = who.map(name => {
      const j = r.pick(JOBS), rt = hourly(r, j, 9), hrs = r.int(16, 40), gross = rt * hrs;
      const ds = R.map(([, bp]) => half(gross, bp)), net = gross - ds.reduce((a, b) => a + b, 0);
      items.push(I(`${name}: gross pay`, usd(gross), 'grossh', { rt, hrs }));
      R.forEach(([lab, bp], i) => items.push(I(`${name}: ${lab.toLowerCase()}`, usd(ds[i]), 'ded', { gross, bp })));
      items.push(I(`${name}: net pay`, usd(net), 'net', { gross, bps: R.map(x => x[1]) }));
      return [`${name}, ${j[0]}`, `${usd(rt)} × ${hrs} h`, A(usd(gross)), ...ds.map(d => A(usd(d))), A(usd(net))];
    });
    const eg = 120000, eds = R.map(([, bp]) => half(eg, bp));
    return {
      ican: 'I can find gross pay, take out deductions and find net pay.',
      directions: 'Find each worker\'s gross pay for the week. Use the made-up rates in the box to find each deduction (round to the nearest cent). Net pay is gross pay minus all the deductions.',
      parts: [part('', box(`<p class="ws-tag">${MADEUP}</p><p>${R.map(([l, bp]) => `${l}: <b>${pc(bp / 100)}</b> of gross pay`).join(' · ')}</p>`) +
        example(`Gross pay ${usd(eg)}. ${R.map(([l, bp], i) => `${l} ${pc(bp / 100)} × ${usd(eg)} = ${usd(eds[i])}`).join('; ')}.`,
          `Net pay = ${usd(eg)} − ${eds.map(usd).join(' − ')} = <b>${usd(eg - eds.reduce((a, b) => a + b, 0))}</b>`)),
        part('One week of pay', T(['Worker', 'Pay', 'Gross pay', ...R.map(x => x[0]), 'Net pay'], rows, 'fin-small'))],
      items,
      mistakes: 'Taking a deduction from the net pay instead of the gross pay, and adding the percents first and rounding once (that can be a cent off from rounding each deduction).',
      notes: 'The deduction rates are invented for practice and change with each sheet. Real paychecks take out federal income tax by tables, not one flat rate, plus Social Security and Medicare at rates set by law; this sheet does not teach those numbers.',
    };
  } };
VER.grossh = p => usd(p.rt * p.hrs);
VER.ded = p => usd(Math.round(p.gross * p.bp / 10000 + 1e-7));
VER.net = p => usd(p.bps.reduce((a, bp) => a - Math.round(p.gross * bp / 10000 + 1e-7), p.gross));

SK.stub = { area: 'earn', label: 'Read and label a pay stub', lo: 9, hi: 12, count: null,
  make(v, r) {
    const name = r.pick(NAMES), j = r.pick(JOBS), rt = hourly(r, j, 9), k = r.int(4, 22), gross = rt * 80;
    const R = rates(r).concat([['Health insurance', -r.int(30, 90) * 100]]);   // a flat dollar amount, marked negative
    const ds = R.map(([, bp]) => bp < 0 ? -bp : half(gross, bp)), td = ds.reduce((a, b) => a + b, 0), net = gross - td;
    const L = r.shuffle(['A', 'B', 'C', 'D']);   // letters for gross, total deductions, year to date, net
    const tag = i => `<b class="fin-tag">${L[i]}</b> `;
    const big = ds.indexOf(Math.max(...ds));
    if (ds.filter(d => d === ds[big]).length > 1) return null;
    const keep = Math.round(net * 100 / gross), kp = net * 100 / gross;
    if (edgy(kp)) return null;
    const stub = `<div class="fin-stub"><div class="fin-stub-h"><span><b>Employee:</b> ${esc(name)} (${esc(j[0])})</span><span><b>Pay period:</b> ${k} of 26 (every two weeks)</span><span><b>Rate:</b> ${usd(rt)} an hour · 80 hours</span></div>` +
      T(['', 'This period', `${tag(2)}Year to date`], [
        ['<b>Gross pay</b>', tag(0) + usd(gross), usd(gross * k)],
        ...R.map(([l, bp], i) => [`${l}${bp > 0 ? ` (${pc(bp / 100)})` : ''}`, usd(ds[i]), usd(ds[i] * k)]),
        ['<b>Total deductions</b>', tag(1) + A(usd(td)), A(usd(td * k))],
        ['<b>Net pay</b>', tag(3) + A(usd(net)), A(usd(net * k))]]) + `<p class="fin-note">${MADEUP}. Health insurance is a flat amount each check.</p></div>`;
    const terms = ['Gross pay', 'Total deductions', 'Year to date', 'Net pay'];
    const items = terms.map((t, i) => I(`Label: ${t}`, L[i], 'lab', { L, i }));
    items.push(I('Total deductions this period', usd(td), 'sum', { xs: ds }), I('Total deductions year to date', usd(td * k), 'sumk', { xs: ds, k }),
      I('Net pay this period', usd(net), 'diff', { a: gross, xs: ds }), I('Net pay year to date', usd(net * k), 'diffk', { a: gross, xs: ds, k }));
    const Q = [
      [`How much did ${name} earn this period before deductions?`, usd(gross), 'mul', { a: rt, b: 80 }],
      [`How many pay periods have there been so far this year?`, String(k), 'div', { a: gross * k, b: gross }],
      [`What percent of gross pay does ${name} take home this period? Round to the nearest whole percent.`, `${keep}%`, 'pct', { a: net, b: gross }],
      [`Which deduction is the largest this period?`, R[big][0], 'name', { t: R[big][0] }],
      [`How much income tax has been taken out so far this year?`, usd(ds[0] * k), 'mul', { a: ds[0], b: k }],
      [`If every check this year is the same, what is ${name}'s gross pay for all 26 checks?`, usd(gross * 26), 'mul', { a: gross, b: 26 }],
      [`How much bigger would this check be with no retirement savings taken out?`, usd(ds[3]), 'eq', { a: ds[3] }],
      [`After a raise of $1.00 an hour, what would the gross pay be for 80 hours?`, usd((rt + 100) * 80), 'mul', { a: rt + 100, b: 80 }],
    ];
    Q.forEach(([q, a, kk, p]) => items.push(I(q, a, kk, p)));
    return {
      ican: 'I can read a pay stub: gross pay, deductions, year-to-date totals and net pay.',
      directions: 'Fill in the four empty boxes on the pay stub. Then write the letter that labels each part, and answer the questions.',
      parts: [part('The pay stub', stub),
        part('Label the stub: write the letter', `<p class="fin-labels">${terms.map((t, i) => `${t} ${blank(L[i], 2)}`).join(' &nbsp; ')}</p>`),
        part('Questions', Q.map(([q, a], i) => ql(i + 1, esc(q), aline('Answer', a, 8))).join(''))],
      items,
      mistakes: 'Reading the year-to-date column when the question asks about this period, and subtracting only the taxes (not every deduction) to get net pay.',
      notes: 'Year to date is the total so far this year, so it is this period\'s amount times the number of pay periods so far. The rates are invented for practice.',
    };
  } };
VER.lab = p => p.L[p.i];
VER.sum = p => usd(p.xs.reduce((a, b) => a + b, 0));
VER.sumk = p => usd(p.xs.reduce((a, b) => a + b * p.k, 0));
VER.diff = p => usd(p.xs.reduce((a, b) => a - b, p.a));
VER.diffk = p => usd(p.xs.reduce((a, b) => a - b * p.k, p.a * p.k));
VER.mul = p => usd(p.a * p.b);
VER.div = p => String(p.a / p.b);
VER.pct = p => `${Math.round(p.a / p.b * 100)}%`;
VER.name = p => p.t;
VER.eq = p => usd(p.a);

// made-up brackets: [top of the bracket (Infinity for the last), rate in percent]
const BRACKETS = [[[10000, 10], [40000, 15], [Infinity, 20]], [[12000, 8], [36000, 14], [Infinity, 21]], [[8000, 10], [30000, 13], [Infinity, 18]]];
const taxOf = (inc, br) => { let tax = 0, lo = 0; for (const [hi, rt] of br) { if (inc > lo) tax += (Math.min(inc, hi) - lo) * rt; lo = hi; } return tax; };   // dollars × percent = cents
SK.taxret = { area: 'earn', label: 'A simple tax return (made-up brackets)', lo: 10, hi: 12, count: [2, 3, 4],
  make(v, r, g, n) {
    const br = r.pick(BRACKETS), sd = r.pick([8000, 9000, 10000, 11000]), who = r.sample(NAMES, n), items = [];
    const cols = who.map(name => {
      const w = r.int(180, 700) * 100, it = r.int(0, 60) * 10, tot = w + it, ti = Math.max(0, tot - sd), tax = taxOf(ti, br);
      let wh; do { wh = tax + r.int(-90, 90) * 1000 + r.int(0, 99); } while (wh === tax || wh < 0);
      const res = wh > tax ? `Refund ${usd(wh - tax)}` : `Owes ${usd(tax - wh)}`;
      items.push(I(`${name}: total income`, usd0(tot), 'tot', { w, it }), I(`${name}: taxable income`, usd0(ti), 'ti', { w, it, sd }),
        I(`${name}: tax`, usd(tax), 'tax', { ti, br }), I(`${name}: refund or amount owed`, res, 'res', { ti, br, wh }));
      return { name, w, it, tot, ti, tax, wh, res };
    });
    const row = (lab, f) => [lab, ...cols.map(f)];
    const brText = br.map(([hi, rt], i) => { const lo = i ? br[i - 1][0] : 0; return hi === Infinity ? `${rt}% on taxable income over ${usd0(lo)}` : `${rt}% on taxable income ${i ? `from ${usd0(lo)} ` : ''}up to ${usd0(hi)}`; }).join('; ');
    const exI = r.int(40, 60) * 1000, exTax = taxOf(exI, br);
    const exSteps = br.map(([hi, rt], i) => { const lo = i ? br[i - 1][0] : 0; return exI > lo ? `${rt}% × ${usd0(Math.min(exI, hi) - lo)} = ${usd(Math.min(exI, hi) * rt - lo * rt)}` : ''; }).filter(Boolean);
    return {
      ican: 'I can use a standard deduction and tax brackets to find taxable income, the tax, and a refund or amount owed.',
      directions: 'Fill in the empty lines for each person. Taxable income is total income minus the standard deduction. Tax each slice of taxable income at its bracket\'s rate. Compare the tax with the tax already withheld from pay.',
      parts: [part('', box(`<p class="ws-tag">${MADEUP}</p><p><b>Standard deduction:</b> ${usd0(sd)}. <b>Brackets:</b> ${esc(brText)}.</p>`) +
        example(`Taxable income ${usd0(exI)}: ${exSteps.join(' and ')}.`, `Tax = ${exSteps.map(s => s.split('= ')[1]).join(' + ')} = <b>${usd(exTax)}</b>. Only the dollars inside each bracket are taxed at that bracket\'s rate.`)),
        part('The returns', T(['Line', ...cols.map(c => esc(c.name))], [
          row('1. Wages', c => usd0(c.w)), row('2. Interest from savings', c => usd0(c.it)), row('3. Total income (1 + 2)', c => A(usd0(c.tot))),
          row('4. Standard deduction', () => usd0(sd)), row('5. Taxable income (3 − 4)', c => A(usd0(c.ti))), row('6. Tax from the brackets', c => A(usd(c.tax))),
          row('7. Tax withheld from pay', c => usd(c.wh)), row('8. Refund or amount owed', c => A(c.res))]))],
      items,
      mistakes: 'Taxing all of the income at the highest bracket\'s rate. A higher bracket only applies to the dollars inside it, so a raise never lowers take-home pay.',
      notes: 'The standard deduction and the brackets are invented and change with each sheet; real ones are set by law and change most years. A refund means too much was withheld; an amount owed means too little was.',
    };
  } };
VER.tot = p => usd0(p.w + p.it);
VER.ti = p => usd0(Math.max(0, p.w + p.it - p.sd));
// a second route: base tax at the bottom of the bracket plus the rate on the part above it
const tax2 = (ti, br) => { let base = 0, lo = 0; for (const [hi, rt] of br) { if (ti <= hi) return base + (ti - lo) * rt; base += (hi - lo) * rt; lo = hi; } return base; };
VER.tax = p => usd(tax2(p.ti, p.br));
VER.res = p => { const t = tax2(p.ti, p.br); return p.wh > t ? `Refund ${usd(p.wh - t)}` : `Owes ${usd(t - p.wh)}`; };

/* ===== Spending and budgets ===== */
// price lists: [item, unit, low cents, high cents, [qty low, qty high], category, price step in cents]
const CTX = {
  picnic: { label: 'Picnic shopping list', lo: 5, hi: 8, limit: [25, 30, 35], what: 'a class picnic', items: [
    ['bag of rolls', 'bag', 249, 399, [1, 2], 'Food'], ['pack of cheese slices', 'pack', 299, 449, [1, 2], 'Food'], ['pound of grapes', 'pound', 199, 349, [1, 3], 'Food'],
    ['bag of carrots', 'bag', 99, 199, [1, 2], 'Food'], ['bag of chips', 'bag', 199, 349, [1, 2], 'Snacks'], ['box of cookies', 'box', 249, 399, [1, 2], 'Snacks'],
    ['jug of lemonade', 'jug', 229, 349, [1, 2], 'Drinks'], ['pack of water bottles', 'pack', 249, 449, [1, 2], 'Drinks'], ['pack of paper plates', 'pack', 199, 349, [1, 1], 'Supplies'],
    ['pack of napkins', 'pack', 99, 199, [1, 1], 'Supplies']] },
  booth: { label: 'Market booth startup costs', lo: 6, hi: 12, limit: [900, 1200, 1500], what: 'a weekend market booth', items: [
    ['folding table', 'table', 3999, 6999, [1, 2], 'Startup'], ['canopy tent', 'tent', 8999, 14999, [1, 1], 'Startup'], ['banner sign', 'sign', 2499, 4999, [1, 1], 'Startup'],
    ['card reader', 'reader', 2900, 5900, [1, 1], 'Startup'], ['display rack', 'rack', 1999, 3999, [1, 3], 'Startup'], ['booth space', 'weekend', 4000, 7500, [4, 4], 'Monthly'],
    ['craft supplies', 'box', 1500, 3500, [2, 5], 'Monthly'], ['paper bags', 'pack of 100', 899, 1499, [1, 3], 'Monthly'], ['price tags', 'pack', 299, 599, [1, 2], 'Monthly']] },
  bike: { label: 'True first-year cost of an e-bike', lo: 6, hi: 12, limit: [1600, 1800, 2000], what: 'a first year with an e-bike', items: [
    ['e-bike', 'bike', 89900, 129900, [1, 1], 'Bike'], ['spare charger', 'charger', 3999, 7999, [1, 1], 'Gear'], ['lock', 'lock', 2999, 6999, [1, 1], 'Gear'],
    ['helmet', 'helmet', 3999, 8999, [1, 1], 'Gear'], ['set of lights', 'set', 1999, 4999, [1, 1], 'Gear'], ['tune-up', 'visit', 4999, 8999, [2, 3], 'Repairs'],
    ['new tire', 'tire', 2999, 4999, [1, 2], 'Repairs'], ['electricity for charging', 'month', 100, 300, [12, 12], 'Charging']] },
  show: { label: 'Dance site show budget', lo: 6, hi: 12, limit: [900, 1200, 1500], what: 'a dance show in a park', items: [
    ['costume', 'costume', 2500, 6000, [6, 12], 'Costumes'], ['speaker rental', 'day', 4000, 9000, [1, 3], 'Sound'], ['microphone rental', 'day', 1500, 3000, [1, 3], 'Sound'],
    ['printed sign', 'sign', 800, 2000, [3, 8], 'Signs'], ['poster', 'poster', 100, 300, [20, 50], 'Signs'], ['park permit', 'permit', 5000, 15000, [1, 1], 'Permits'],
    ['street closure permit', 'permit', 2500, 7500, [1, 1], 'Permits']] },
  film: { label: 'Short film budget', lo: 6, hi: 12, limit: [1500, 2000, 2500], what: 'a five-minute short film', items: [
    ['camera rental', 'day', 4000, 9000, [2, 4], 'Equipment'], ['light kit rental', 'day', 2500, 5000, [2, 4], 'Equipment'], ['microphone rental', 'day', 1500, 3000, [2, 4], 'Equipment'],
    ['cafe location fee', 'hour', 2500, 6000, [2, 5], 'Locations'], ['park filming permit', 'permit', 2500, 7500, [1, 1], 'Locations'], ['crew lunch', 'lunch', 800, 1400, [12, 30], 'Food'],
    ['snacks and water', 'day', 1500, 3000, [2, 4], 'Food']] },
  doc: { label: 'Documentary budget', lo: 9, hi: 12, limit: [6000, 8000, 10000], what: 'a short documentary', items: [
    ['camera operator', 'day', 20000, 35000, [2, 4], 'Crew'], ['sound recordist', 'day', 15000, 25000, [2, 4], 'Crew'], ['camera kit rental', 'day', 6000, 12000, [2, 4], 'Equipment'],
    ['drone rental', 'day', 5000, 9000, [1, 2], 'Equipment'], ['mileage', 'mile', 50, 70, [150, 400], 'Travel'], ['hotel room', 'night', 9000, 15000, [2, 4], 'Travel'],
    ['archival photo license', 'photo', 2500, 10000, [3, 8], 'Archival'], ['archival film clip license', 'clip', 15000, 40000, [1, 3], 'Archival']] },
  recording: { label: 'Recording production budget', lo: 9, hi: 12, limit: [1200, 1500, 2000], what: 'recording a new piece', items: [
    ['rehearsal room', 'hour', 1500, 3000, [2, 6], 'Rehearsal'], ['studio time', 'hour', 3000, 7500, [3, 8], 'Studio'], ['mixing engineer', 'hour', 4000, 8000, [2, 4], 'Studio'],
    ['player fee', 'player', 5000, 10000, [2, 5], 'Players'], ['printed parts', 'page', 15, 40, [40, 120], 'Printing'], ['printed score', 'copy', 800, 1500, [2, 4], 'Printing']] },
  concert: { label: 'Concert budget with income', lo: 9, hi: 12, income: true, what: 'a spring dance concert', items: [
    ['theater rental', 'night', 25000, 60000, [1, 2], 'Space'], ['lighting technician', 'hour', 3000, 5000, [6, 12], 'Crew'], ['sound technician', 'hour', 3000, 5000, [6, 12], 'Crew'],
    ['costume', 'costume', 2500, 5000, [8, 16], 'Costumes'], ['printed program', 'program', 50, 150, [100, 250], 'Printing'], ['poster', 'poster', 100, 300, [20, 50], 'Printing']],
    inc: [['ticket sales', 'ticket', 800, 1500, [120, 300]], ['program ads', 'ad', 2500, 7500, [4, 10]], ['bake sale', 'table', 5000, 15000, [1, 2]]] },
};
const ctxFor = g => Object.entries(CTX).filter(([, c]) => g >= c.lo && g <= c.hi);
const price = (r, it) => { const step = it[3] > 5000 ? 100 : it[3] > 999 ? 50 : 1; const p = r.int(Math.ceil(it[2] / step), Math.floor(it[3] / step)) * step; return step > 1 && it[2] % 100 === 99 ? p - 1 : p; };
SK.costs = { area: 'spend', label: 'Budget totals from a price list', lo: 5, hi: 12, count: [5, 6, 7],
  make(v, r, g, n) {
    const keys = ctxFor(g).map(c => c[0]), ck = v.ctx !== 'any' && keys.includes(v.ctx) ? v.ctx : r.pick(keys), C = CTX[ck];
    let lns = null, limit = null;
    for (let t = 0; t < 200 && !lns; t++) {
      const pick = r.sample(C.items, Math.min(n, C.items.length));
      if (new Set(pick.map(x => x[5])).size < Math.min(3, new Set(C.items.map(x => x[5])).size)) continue;
      if (ck === 'bike' && !pick.some(x => x[5] === 'Bike')) continue;
      const ls = pick.map(it => { const q = r.int(it[4][0], it[4][1]), p = price(r, it); return { it: it[0], unit: it[1], cat: it[5], q, p, c: q * p }; });
      const tot = ls.reduce((a, b) => a + b.c, 0);
      if (C.limit) { const ok = C.limit.filter(L => L * 100 >= tot && L * 100 - tot < L * 40); if (!ok.length) continue; limit = r.pick(ok); }
      lns = ls;
    }
    if (!lns) return null;
    const order = C.items.map(x => x[0]);
    lns.sort((a, b) => order.indexOf(a.it) - order.indexOf(b.it));
    const cats = [...new Set(lns.map(l => l.cat))], ctot = cats.map(c => lns.filter(l => l.cat === c).reduce((a, b) => a + b.c, 0));
    const total = ctot.reduce((a, b) => a + b, 0), items = [];
    lns.forEach(l => items.push(I(`Cost of ${l.it}`, usd(l.c), 'mul', { a: l.p, b: l.q })));
    const showPct = g >= 7;
    cats.forEach((c, i) => { items.push(I(`Total for ${c}`, usd(ctot[i]), 'sum', { xs: lns.filter(l => l.cat === c).map(l => l.c) }));
      if (showPct) { if (edgy(ctot[i] * 100 / total)) return; items.push(I(`Percent for ${c}`, `${Math.round(ctot[i] * 100 / total)}%`, 'pct', { a: ctot[i], b: total })); } });
    if (showPct && items.filter(x => x.k === 'pct').length < cats.length) return null;
    items.push(I('Total cost', usd(total), 'sum', { xs: lns.map(l => l.c) }));
    const unitTxt = l => l.unit === 'mile' ? `${usd(l.p)} a mile` : `${usd(l.p)} per ${l.unit}`;
    const parts = [part('', example(`3 tickets at ${usd(1250)} each: 3 × ${usd(1250)} = <b>${usd(3750)}</b>. Add the costs in each category, then add the categories.`))];
    parts.push(part(`The plan: ${C.what}`, T(['Item', 'Category', 'Quantity', 'Price', 'Cost'], lns.map(l => [esc(l.it), esc(l.cat), fmt(l.q, 0), unitTxt(l), A(usd(l.c))]))));
    const crow = cats.map((c, i) => [esc(c), A(usd(ctot[i])), ...(showPct ? [A(`${Math.round(ctot[i] * 100 / total)}%`)] : [])]);
    crow.push(['<b>Total</b>', A(usd(total)), ...(showPct ? ['100%'] : [])]);
    let summary = T(['Category', 'Total', ...(showPct ? ['Percent of total (nearest whole percent)'] : [])], crow);
    const qs = [];
    if (C.inc) {
      const inc = r.sample(C.inc, 2).map(it => { const q = r.int(it[4][0], it[4][1]), p = price(r, it); return { it: it[0], unit: it[1], q, p, c: q * p }; });
      const itot = inc.reduce((a, b) => a + b.c, 0), bal = itot - total;
      if (bal === 0) return null;
      inc.forEach(l => items.push(I(`Income from ${l.it}`, usd(l.c), 'mul', { a: l.p, b: l.q })));
      items.push(I('Total income', usd(itot), 'sum', { xs: inc.map(l => l.c) }), I('Profit or loss', bal > 0 ? `Profit of ${usd(bal)}` : `Loss of ${usd(-bal)}`, 'pl', { a: itot, b: total }));
      parts.push(part('Income', T(['Income source', 'Number sold', 'Price', 'Income'], inc.map(l => [esc(l.it), fmt(l.q, 0), unitTxt(l), A(usd(l.c))]).concat([['<b>Total income</b>', '', '', A(usd(itot))]]))));
      qs.push(ql(1, 'Income minus expenses: does the concert make a profit or a loss, and how much?', aline('Answer', items[items.length - 1].a, 12)));
    } else {
      const left = limit * 100 - total;
      items.push(I(`Money left from ${usd0(limit)}`, usd(left), 'left', { L: limit * 100, xs: lns.map(l => l.c) }));
      qs.push(ql(1, `The budget is ${usd0(limit)}. How much money is left after buying everything on the plan?`, aline('Answer', usd(left))));
      const big = cats[ctot.indexOf(Math.max(...ctot))];
      if (ctot.filter(x => x === Math.max(...ctot)).length > 1) return null;
      items.push(I('Biggest category', big, 'name', { t: big }));
      qs.push(ql(2, 'Which category costs the most?', aline('Answer', big)));
      qs.push(ql(3, 'Change one thing on the plan to save money. What would you change, and how much would it save?', lines(2)));
    }
    parts.push(part('Totals by category', summary));
    if (v.graph && g >= 6) parts.push(part('Graph the costs', `<p>Draw a bar for each category's total.</p>` + barFrame(cats, ctot.map(c => c / 100), 'Costs by category', 'Cost (dollars)', true)));
    parts.push(part('Questions', qs.join('')));
    return {
      title: C.label, ican: C.inc ? 'I can multiply and add money to build a budget with income and expenses, total each category and find the profit or loss.' : 'I can multiply and add money to build a budget, total each category and compare with a limit.',
      directions: 'Multiply the quantity by the price for each line. Add the lines in each category, then find the total.' + (showPct ? ' Find what percent of the total each category is.' : ''),
      parts, items,
      mistakes: 'Lining up the cents wrong when adding (write every amount with two decimal places), and forgetting the quantity on a line that is bought more than once.',
      notes: `Every price is invented and in a realistic range. ${showPct ? 'The rounded percents may add to 99% or 101%; that is a rounding effect, not a mistake. ' : ''}Pick a plan under Budget plan to choose the setting, or Any plan for a mix across sheets.`,
    };
  } };
VER.left = p => usd(p.xs.reduce((a, b) => a - b, p.L));
VER.pl = p => p.a > p.b ? `Profit of ${usd(p.a - p.b)}` : `Loss of ${usd(p.b - p.a)}`;

// unit prices: [item, unit, small sizes, large sizes, unit price range in cents]
const GROCERY = [['cereal', 'oz', [10, 12, 14], [18, 20, 24], [15, 30]], ['peanut butter', 'oz', [12, 16], [28, 40], [12, 25]], ['apple juice', 'fl oz', [32, 46], [64, 96], [5, 9]],
  ['rice', 'lb', [2, 5], [10, 20], [90, 200]], ['eggs', 'egg', [12], [18, 24], [25, 45]], ['yogurt', 'oz', [6, 8], [32], [10, 20]], ['shampoo', 'fl oz', [12], [24, 32], [25, 60]],
  ['paper towels', 'roll', [2, 4], [6, 8, 12], [90, 200]], ['oatmeal', 'oz', [18], [42], [8, 15]], ['pasta', 'oz', [16], [32, 48], [8, 16]], ['frozen peas', 'oz', [12, 16], [32], [10, 18]],
  ['granola bars', 'bar', [6], [12, 24], [40, 80]], ['dish soap', 'fl oz', [16, 20], [40, 56], [8, 15]], ['tortillas', 'tortilla', [8, 10], [20, 30], [10, 25]], ['apples', 'lb', [3], [5, 8], [100, 200]],
  ['shredded cheese', 'oz', [8], [16, 32], [25, 45]], ['black beans', 'oz', [15], [29], [7, 14]], ['laundry soap', 'load', [32], [64, 96], [15, 30]]];
SK.unit = { area: 'spend', label: 'Unit price and the better buy', lo: 5, hi: 12, count: [6, 8, 10],
  make(v, r, g, n) {
    const sav = g >= 9, items = [];
    const pairs = r.sample(GROCERY, n).map(G => {
      const s1 = r.pick(G[2]), s2 = r.pick(G[3]);
      let u1, u2; do { u1 = r.int(G[4][0], G[4][1]); u2 = r.int(G[4][0], G[4][1]); } while (u1 === u2 || (u2 > u1 && r.chance(.5)));   // the big size is usually, not always, cheaper per unit
      const L = Gen.m.lcm(s1, s2), use = L * (L < 3 * s2 ? r.int(1, 2) : 1);
      return { G, s1, s2, u1, u2, p1: s1 * u1, p2: s2 * u2, use };
    });
    const rows = pairs.map((p, i) => {
      const better = p.u1 < p.u2 ? `${p.s1} ${p.G[1]}` : `${p.s2} ${p.G[1]}`, save = p.use * Math.abs(p.u1 - p.u2);
      items.push(I(`${p.G[0]}: unit price of the ${p.s1} ${p.G[1]} size`, `${usd(p.u1)} per ${p.G[1]}`, 'unit', { price: p.p1, size: p.s1, u: p.G[1] }),
        I(`${p.G[0]}: unit price of the ${p.s2} ${p.G[1]} size`, `${usd(p.u2)} per ${p.G[1]}`, 'unit', { price: p.p2, size: p.s2, u: p.G[1] }),
        I(`${p.G[0]}: better buy`, better, 'better', p));
      if (sav) items.push(I(`${p.G[0]}: savings a month`, usd(save), 'save', p));
      return [esc(p.G[0]), `${p.s1} ${p.G[1]} for ${usd(p.p1)}`, A(usd(p.u1)), `${p.s2} ${p.G[1]} for ${usd(p.p2)}`, A(usd(p.u2)), A(better), ...(sav ? [`${p.use} ${p.G[1]}`, A(usd(save))] : [])];
    });
    return {
      ican: 'I can find unit prices and choose the better buy' + (sav ? ', then find how much switching saves in a month.' : '.'),
      directions: 'Divide each price by its size to find the price for one unit. Circle or write the size with the lower unit price.' + (sav ? ' Then find how much a shopper who uses the amount shown each month saves by buying only the better size.' : ''),
      parts: [part('', example(`Cereal: 12 oz for ${usd(12 * 21)} or 20 oz for ${usd(20 * 19)}. ${usd(12 * 21)} ÷ 12 = ${usd(21)} per oz; ${usd(20 * 19)} ÷ 20 = ${usd(19)} per oz.`,
        `The 20 oz box is the better buy.${sav ? ` Using 60 oz a month: 60 × (${usd(21)} − ${usd(19)}) = <b>${usd(120)}</b> saved.` : ''}`)),
        part('Compare the sizes', T(['Item', 'Size A', 'Unit price A', 'Size B', 'Unit price B', 'Better buy', ...(sav ? ['Uses a month', 'Saves a month'] : [])], rows, sav ? 'fin-small' : ''))],
      items,
      mistakes: 'Dividing the size by the price (that gives units per dollar, where bigger is better), and assuming the bigger package is always cheaper per unit. Here it usually is, but not always.',
      notes: 'Every unit price comes out to a whole number of cents. Prices are invented but realistic.' + (sav ? ' The monthly amount is a number of units both sizes can make exactly, so the savings are the difference in unit price times the monthly amount.' : ''),
    };
  } };
VER.unit = p => `${usd(p.price / p.size)} per ${p.u}`;
VER.better = p => p.p1 / p.s1 < p.p2 / p.s2 ? `${p.s1} ${p.G[1]}` : `${p.s2} ${p.G[1]}`;
VER.save = p => usd(Math.abs(p.use / p.s1 * p.p1 - p.use / p.s2 * p.p2));

const GEAR = [['helmet', 3999, 8999], ['bike lock', 2499, 6999], ['set of lights', 1999, 4999], ['water bottle', 799, 1999], ['bike pump', 1999, 3999], ['phone mount', 1299, 2999],
  ['rain jacket', 3999, 8999], ['repair kit', 1499, 2999], ['pair of gloves', 1499, 3499], ['backpack', 2999, 6999], ['bell', 599, 1499], ['basket', 2499, 4999], ['reflective vest', 999, 2499], ['tire', 2499, 4999]];
SK.tax = { area: 'spend', label: 'Sales tax at the register', lo: 6, hi: 12, count: [6, 8, 10],
  make(v, r, g, n) {
    const bp = r.pick(g < 7 ? [500, 600, 700, 800] : [550, 650, 700, 725, 775, 825]), items = [];
    const buys = r.sample(GEAR, n).map(x => { const p = r.int(Math.floor(x[1] / 100), Math.floor(x[2] / 100)) * 100 + r.pick([99, 49, 0, 29, 79]); return { it: x[0], p: Math.min(p, x[2] + 1) }; });
    const rows = buys.map(b => { const t = half(b.p, bp); items.push(I(`Tax on the ${b.it}`, usd(t), 'tx', { p: b.p, bp }), I(`Total for the ${b.it}`, usd(b.p + t), 'tt', { p: b.p, bp }));
      return [esc(b.it), usd(b.p), A(usd(t)), A(usd(b.p + t))]; });
    const all = buys.reduce((a, b) => a + b.p + half(b.p, bp), 0);
    items.push(I('All purchases together', usd(all), 'ttall', { ps: buys.map(b => b.p), bp }));
    rows.push(['<b>All purchases</b>', '', '', A(usd(all))]);
    const ep = 4599, et = half(ep, bp);
    return {
      ican: 'I can find the sales tax on a price and the total cost.',
      directions: `The sales tax rate is ${pc(bp / 100)}. Find the tax on each purchase, rounded to the nearest cent, and the total. Then add all the totals.`,
      parts: [part('', example(`${usd(ep)} × ${pc(bp / 100)} = ${usd(ep)} × ${fmt(bp / 10000, 4)} = ${fix(ep * bp / 1000000, 4)}, which rounds to ${usd(et)}.`, `Total = ${usd(ep)} + ${usd(et)} = <b>${usd(ep + et)}</b>`)),
        part('Receipts', `<div class="fin-receipt">${T(['Purchase', 'Price', `Sales tax (${pc(bp / 100)})`, 'Total'], rows)}</div>`)],
      items,
      mistakes: `Moving the decimal point the wrong way when changing ${pc(bp / 100)} to a decimal (it is ${fmt(bp / 10000, 4)}), and rounding down every time instead of to the nearest cent.`,
      notes: 'Each line is a separate purchase, so the tax is rounded on each one. Real stores round the tax on the whole receipt, which can differ by a cent. Rates are typical of U.S. combined state and local rates but invented for practice.',
    };
  } };
VER.tx = p => usd(Math.round(p.p * p.bp / 10000));
VER.tt = p => usd(p.p + Math.round(p.p * p.bp / 10000));
VER.ttall = p => usd(p.ps.reduce((a, x) => a + x + Math.round(x * p.bp / 10000), 0));

// percent word problems: each returns {q, a, k, p} with p enough for verify
const PCT = {
  disc: (r, A1) => { const it = r.pick(['jacket', 'pair of shoes', 'backpack', 'video game', 'guitar', 'tent', 'skateboard', 'lamp']), p = r.int(20, 160) * 100 + r.pick([0, 0, 99, 50]), d = r.pick([10, 15, 20, 25, 30, 40]);
    if ((p * d) % 100 === 50) return null; const s = p - half(p, d * 100);
    return { q: `A ${it} costs ${usd(p)}. It is on sale for ${d}% off. What is the sale price?`, a: usd(s), k: 'pdisc', p: { p, d } }; },
  tip: (r, A1) => { const b = r.int(1800, 9800), t = r.pick([15, 18, 20]);
    return { q: `${A1}'s restaurant bill is ${usd(b)}. ${A1} leaves a ${t}% tip. What is the total with the tip?`, a: usd(b + half(b, t * 100)), k: 'ptip', p: { b, t } }; },
  markup: (r) => { const c = r.int(4, 60) * 100 + r.pick([0, 50]), m = r.pick([25, 40, 50, 60, 75, 100]), shop = r.pick(['A bike shop', 'A bookstore', 'A shoe store', 'A plant nursery', 'A music store']);
    return { q: `${shop} pays ${usd(c)} for an item and marks it up ${m}%. What is the selling price?`, a: usd(c + half(c, m * 100)), k: 'pmark', p: { c, m } }; },
  comm: (r, A1) => { const s = r.int(20, 300) * 100, c = r.pick([3, 4, 5, 6, 8, 10]);
    return { q: `${A1} sells ${usd(s)} worth of furniture and earns a ${c}% commission. How much commission does ${A1} earn?`, a: usd(half(s, c * 100)), k: 'pcomm', p: { s, c } }; },
  change: (r) => { const o = r.int(8, 90) * 5, nn = o + r.pick([-1, 1]) * r.int(1, 12) * 5; if (nn <= 0) return null; const x = (nn - o) / o * 100;
    if (edgy(x * 10)) return null; const it = r.pick(['A concert ticket', 'A monthly bus pass', 'A gym membership', 'A phone plan', 'A bag of dog food']);
    return { q: `${it} went from ${usd0(o)} to ${usd0(nn)}. What is the percent change? Round to the nearest tenth of a percent.`, a: `${fix(Math.abs(x), 1)}% ${x > 0 ? 'increase' : 'decrease'}`, k: 'pchg', p: { o, n: nn } }; },
  disctax: (r) => { const p = r.int(20, 120) * 100 + r.pick([0, 99]), d = r.pick([10, 20, 25, 30]), t = r.pick([5, 6, 7, 8]); if ((p * d) % 100 === 50) return null;
    const s = p - half(p, d * 100), tot = s + half(s, t * 100), it = r.pick(['coat', 'pair of headphones', 'desk chair', 'printer', 'pair of boots']);
    return { q: `A ${it} is ${usd(p)}, now ${d}% off. Sales tax is ${t}%. What is the total at the register?`, a: usd(tot), k: 'pdt', p: { p, d, t } }; },
  orig: (r) => { const o = r.int(10, 120) * 100, d = r.pick([10, 20, 25, 40, 50]), s = o * (100 - d) / 100; if (s % 1) return null;
    return { q: `After a ${d}% discount, a ${r.pick(['bike', 'blender', 'suitcase', 'keyboard', 'camera bag'])} costs ${usd(s)}. What was the price before the discount?`, a: usd(o), k: 'porig', p: { s, d } }; },
};
SK.pct = { area: 'spend', label: 'Discounts, tips, markups and percent change', lo: 7, hi: 12, count: [6, 8, 10],
  make(v, r, g, n) {
    const kinds = ['disc', 'tip', 'markup', 'comm', 'change', ...(g >= 8 ? ['disctax', 'orig'] : [])], who = r.shuffle(NAMES);
    let i = 0;
    const list = r.distinct(n, () => PCT[kinds[(i++) % kinds.length]](r, who[i % who.length]), x => x.q);
    const items = list.map(x => I(x.q, x.a, x.k, x.p));
    return {
      ican: 'I can use percents to find sale prices, tips, markups, commissions and percent change.',
      directions: 'Solve each problem. Round money to the nearest cent. Show your work in the box.',
      parts: [part('', example('A $40.00 game is 25% off. 25% of $40.00 is 0.25 × $40.00 = $10.00.', 'Sale price = $40.00 − $10.00 = <b>$30.00</b>. (Or: 75% × $40.00 = $30.00.)')),
        part('Problems', probs(list.map((x, j) => prob(j + 1, esc(x.q), [`<div class="fin-work"></div>`, aline('Answer', x.a, 9)]))))],
      items,
      mistakes: 'Finding the discount and stopping, instead of subtracting it from the price; and for percent change, dividing by the new amount instead of the original amount.',
      notes: 'Problems rotate through the types so every sheet has a mix.' + (g >= 8 ? ' The "price before the discount" problems work backward: divide the sale price by the percent that is left (for 20% off, 80%).' : ''),
    };
  } };
VER.pdisc = p => usd(Math.round(p.p * (100 - p.d) / 100));
VER.ptip = p => usd(p.b + Math.round(p.b * p.t / 100));
VER.pmark = p => usd(Math.round(p.c * (1 + p.m / 100)));
VER.pcomm = p => usd(Math.round(p.s * p.c / 100));
VER.pchg = p => { const x = (p.n - p.o) / p.o * 100; return `${fix(Math.abs(x), 1)}% ${x > 0 ? 'increase' : 'decrease'}`; };
VER.pdt = p => { const s = Math.round(p.p * (100 - p.d) / 100); return usd(Math.round(s * (100 + p.t) / 100)); };
VER.porig = p => usd(p.s / (1 - p.d / 100));

const NEEDS = [['Rent', 0.26, 0.4], ['Utilities', 0.03, 0.06], ['Groceries', 0.08, 0.12], ['Bus pass or gas', 0.03, 0.06], ['Phone', 0.015, 0.03], ['Insurance', 0.02, 0.05]];
const WANTS = [['Streaming services', 0.005, 0.015], ['Eating out', 0.04, 0.08], ['Concerts and movies', 0.02, 0.05], ['Hobbies', 0.02, 0.05], ['New clothes', 0.02, 0.05], ['Trips', 0.03, 0.06]];
const SAVES = [['Emergency fund', 0.06, 0.12], ['Retirement account', 0.04, 0.08], ['Extra loan payment', 0.02, 0.05]];
SK.b50 = { area: 'spend', label: 'The 50/30/20 budget', lo: 7, hi: 12, count: null,
  make(v, r, g) {
    const name = r.pick(NAMES), inc = r.int(20, 48) * 100;
    for (let t = 0; t < 300; t++) {
      const mk = (L, k) => r.sample(L, k).map(([l, a, b]) => [l, Math.round(inc * (a + r.next() * (b - a)) / 5) * 5]);
      const nd = mk(NEEDS.slice(0, 1), 1).concat(mk(NEEDS.slice(1), 4)), wt = mk(WANTS, 3), sv = mk(SAVES, 2);
      const sum = L => L.reduce((a, b) => a + b[1], 0);
      const gap = inc - sum(nd) - sum(wt) - sum(sv);
      if (Math.abs(gap) > inc * 0.12) continue;
      wt[0][1] += gap; if (wt[0][1] < 20) continue;
      const N = sum(nd), W = sum(wt), S = sum(sv);
      if (S >= inc * 0.2 || N <= inc * 0.4 || N >= inc * 0.6) continue;
      const rise = r.int(3, 12) * 25, newN = N + rise, wmax = inc - newN - inc * 0.2;
      if (wmax <= 0 || edgy(N * 100 / inc) || edgy(W * 100 / inc) || edgy(S * 100 / inc)) continue;
      const all = r.shuffle([...nd.map(x => [...x, 'Need']), ...wt.map(x => [...x, 'Want']), ...sv.map(x => [...x, 'Savings'])]);
      const items = [I('Needs target (50%)', usd0(inc * 0.5), 'pt', { inc, p: 50 }), I('Wants target (30%)', usd0(inc * 0.3), 'pt', { inc, p: 30 }), I('Savings target (20%)', usd0(inc * 0.2), 'pt', { inc, p: 20 })];
      all.forEach(x => items.push(I(`Sort: ${x[0]}`, x[2], 'name', { t: x[2] })));
      const grp = [['Needs', nd, N], ['Wants', wt, W], ['Savings', sv, S]];
      grp.forEach(([l, L, tot]) => items.push(I(`${l} total`, usd0(tot), 'sum0', { xs: L.map(x => x[1]) }), I(`${l} percent`, `${Math.round(tot * 100 / inc)}%`, 'pct', { a: tot, b: inc })));
      items.push(I('New needs total', usd0(newN), 'add0', { a: N, b: rise }), I('Most for wants after the rent rise', usd0(wmax), 'wmax', { inc, nd: nd.map(x => x[1]), rise }));
      return {
        ican: 'I can split take-home pay with the 50/30/20 rule, sort spending into needs, wants and savings, and rebalance a budget.',
        directions: `${name} takes home ${usd0(inc)} a month. Find the 50/30/20 targets. Sort ${name}'s plan into needs, wants and savings, total each group and compare with the targets. Then fix the budget after the rent goes up.`,
        parts: [part('', box(`<p><b>The 50/30/20 rule:</b> about 50% of take-home pay for needs, 30% for wants and 20% for savings and extra debt payments.</p>`) +
          T(['Group', 'Percent', `Target from ${usd0(inc)}`], [['Needs', '50%', A(usd0(inc * 0.5))], ['Wants', '30%', A(usd0(inc * 0.3))], ['Savings', '20%', A(usd0(inc * 0.2))]])),
          part(`${name}'s monthly plan: write Need, Want or Savings`, T(['Spending', 'Amount', 'Need, Want or Savings'], all.map(x => [esc(x[0]), usd0(x[1]), A(x[2])]))),
          part('Compare with the targets', T(['Group', 'Total', 'Percent of take-home pay (nearest whole percent)', 'Target'], grp.map(([l, , tot], i) => [l, A(usd0(tot)), A(`${Math.round(tot * 100 / inc)}%`), `${[50, 30, 20][i]}%`]))),
          part('The rent goes up', ql(1, `${name}'s rent goes up by ${usd0(rise)} a month. What is the new needs total?`, aline('Answer', usd0(newN))) +
            ql(2, `${name} wants to save the full 20% (${usd0(inc * 0.2)}) and spend no more than ${usd0(inc)}. What is the most ${name} can now spend on wants?`, aline('Answer', usd0(wmax))) +
            ql(3, 'Which wants would you cut, and by how much? Explain.', lines(2)))],
        items,
        mistakes: 'Counting savings as whatever is left over instead of planning it first, and putting phone or insurance under wants. A basic phone plan and insurance are needs; streaming and eating out are wants.',
        notes: 'The 50/30/20 rule is a starting guide, not a law; in high-rent places needs often run over 50%. The plan always adds up to the take-home pay exactly, so a rise in one group must come out of another.',
      };
    }
    return null;
  } };
VER.pt = p => usd0(p.inc * p.p / 100);
VER.sum0 = p => usd0(p.xs.reduce((a, b) => a + b, 0));
VER.add0 = p => usd0(p.a + p.b);
VER.wmax = p => usd0(p.inc * 0.8 - p.nd.reduce((a, b) => a + b, 0) - p.rise);

const LOGCAT = { Food: [['lunch at the deli', 650, 1400], ['groceries', 2500, 6500], ['coffee', 300, 650], ['pizza with friends', 900, 1800], ['snacks', 200, 600]],
  Transportation: [['bus fare', 200, 300], ['gas', 2500, 4500], ['bike repair', 1200, 3000], ['ride home', 900, 2200], ['parking', 300, 1200]],
  Fun: [['movie ticket', 1100, 1600], ['video game', 1999, 5999], ['bowling', 1200, 2500], ['concert ticket', 2500, 6000], ['mini golf', 800, 1500]],
  'Personal care': [['haircut', 1800, 3500], ['shampoo', 400, 900], ['toothpaste', 250, 600], ['laundry', 300, 800], ['new socks', 600, 1500]] };
SK.log = { area: 'spend', label: 'Two-week spending log against a budget', lo: 6, hi: 12, count: [10, 12, 16],
  make(v, r, g, n) {
    const name = r.pick(NAMES), cats = Object.keys(LOGCAT), days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    const ent = [];
    for (let i = 0; i < n; i++) { const c = cats[i % cats.length], it = r.pick(LOGCAT[c]); ent.push({ c, it: it[0], amt: r.int(Math.round(it[1] / 5), Math.round(it[2] / 5)) * 5, day: r.int(0, 13) }); }
    ent.sort((a, b) => a.day - b.day);
    const tot = cats.map(c => ent.filter(e => e.c === c).reduce((a, b) => a + b.amt, 0));
    const bud = tot.map(t => { let b; do { b = Math.round((t + r.int(-30, 30) * 100) / 500) * 500; } while (b <= 0 || b === t); return b; });
    const diff = (t, b) => t > b ? `${usd(t - b)} over` : `${usd(b - t)} under`;
    const items = [];
    cats.forEach((c, i) => items.push(I(`${c} spent`, usd(tot[i]), 'sum', { xs: ent.filter(e => e.c === c).map(e => e.amt) }), I(`${c} over or under`, diff(tot[i], bud[i]), 'ou', { xs: ent.filter(e => e.c === c).map(e => e.amt), b: bud[i] })));
    const T1 = tot.reduce((a, b) => a + b, 0), B1 = bud.reduce((a, b) => a + b, 0);
    if (T1 === B1) return null;
    items.push(I('Total spent', usd(T1), 'sum', { xs: ent.map(e => e.amt) }), I('Total over or under', diff(T1, B1), 'ou', { xs: ent.map(e => e.amt), b: B1 }));
    return {
      ican: 'I can total a spending log by category and compare it with a budget.',
      directions: `Here is ${name}'s spending for two weeks. Add up each category, compare it with the budget, and say how much over or under it is.`,
      parts: [part(`${name}'s spending log`, T(['Day', 'What', 'Category', 'Amount'], ent.map(e => [`Week ${e.day < 7 ? 1 : 2}, ${days[e.day % 7]}`, esc(e.it), e.c, usd(e.amt)]), 'fin-small')),
        part('Compare with the budget', T(['Category', 'Budget for two weeks', 'Spent', 'Over or under'], cats.map((c, i) => [c, usd(bud[i]), A(usd(tot[i])), A(diff(tot[i], bud[i]))]).concat([['<b>Total</b>', usd(B1), A(usd(T1)), A(diff(T1, B1))]])) +
          ql(1, `Pick the category where ${name} went most over budget (or came closest to it). Name one way to spend less there next time.`, lines(2)))],
      items,
      mistakes: 'Missing an entry when adding a category (check off each line as you add it), and subtracting the wrong way so over and under swap.',
      notes: 'Over means more was spent than the budget allowed. Every amount is invented. Press New sheet for a new log.',
    };
  } };
VER.ou = p => { const t = p.xs.reduce((a, b) => a + b, 0); return t > p.b ? `${usd(t - p.b)} over` : `${usd(p.b - t)} under`; };

const CIRC = ['Housing', 'Food', 'Transportation', 'Savings', 'Fun', 'Phone and internet', 'Clothing', 'Giving'];
SK.circle = { area: 'spend', label: 'Budget circle graph', lo: 6, hi: 12, count: null,
  make(v, r) {
    const name = r.pick(NAMES), inc = r.int(10, 25) * 200;
    let ps;
    for (let t = 0; t < 400; t++) {
      const k = r.int(5, 6), p = [r.int(5, 8) * 5]; let left = 100 - p[0];
      for (let i = 1; i < k - 1; i++) { const x = r.int(1, Math.min(5, Math.floor(left / 5) - (k - 1 - i))) * 5; p.push(x); left -= x; }
      p.push(left);
      if (left < 5 || left > 30) continue;
      ps = p; break;
    }
    const cats = ['Housing', ...r.shuffle(['Savings', 'Fun', ...r.sample(CIRC.slice(1).filter(c => c !== 'Savings' && c !== 'Fun'), ps.length - 3)])];
    const amt = ps.map(p => inc * p / 100), items = [];
    cats.forEach((c, i) => items.push(I(`${c}: percent`, `${ps[i]}%`, 'pct', { a: amt[i], b: inc }), I(`${c}: degrees`, `${ps[i] * 18 / 5}°`, 'deg', { a: amt[i], b: inc })));
    const fi = cats.indexOf('Fun'), si = cats.indexOf('Savings'), cut = amt[fi] / 2;
    items.push(I('Savings after cutting fun in half', usd0((si >= 0 ? amt[si] : 0) + cut), 'cut', { s: si >= 0 ? amt[si] : 0, f: amt[fi] }));
    // the key's sectors
    const cx = 150, cy = 150, R = 120; let a0 = 0, sec = '';
    cats.forEach((c, i) => {
      const a1 = a0 + ps[i] * 3.6, rad = d => (d - 90) * Math.PI / 180, P = d => `${(cx + R * Math.cos(rad(d))).toFixed(1)} ${(cy + R * Math.sin(rad(d))).toFixed(1)}`;
      sec += `<path d="M${cx} ${cy} L${P(a0)} A${R} ${R} 0 ${a1 - a0 > 180 ? 1 : 0} 1 ${P(a1)} Z" fill="none" stroke="${RED}" stroke-width="2"/>`;
      const m = rad((a0 + a1) / 2);
      sec += rtx((cx + R * 0.62 * Math.cos(m)).toFixed(1), (cy + R * 0.62 * Math.sin(m) + 4).toFixed(1), `${c.split(' ')[0]} ${ps[i]}%`, `font-size="${c.length > 10 ? 9 : 10.5}" text-anchor="middle"`);
      a0 = a1;
    });
    const circ = h.svg(300, 300, `<circle cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="#222" stroke-width="2"/><circle cx="${cx}" cy="${cy}" r="3" fill="#222"/><line x1="${cx}" y1="${cy}" x2="${cx}" y2="${cy - R}" stroke="#222" stroke-width="1.5"/><g class="ws-ans">${sec}</g>`, 'A circle with its center and one radius drawn, for the budget circle graph');
    return {
      ican: 'I can turn a budget into percents and a circle graph.',
      directions: `${name} takes home ${usd0(inc)} a month. Find what percent of the money each category gets, and how many degrees of the circle that is (percent × 3.6). Then draw the circle graph with a protractor, starting at the line.`,
      parts: [part('', example(`${usd0(600)} out of ${usd0(2400)}: ${usd0(600)} ÷ ${usd0(2400)} = 0.25 = 25%.`, '25% of 360° = 0.25 × 360° = <b>90°</b>')),
        part(`${name}'s monthly budget`, T(['Category', 'Amount', 'Percent', 'Degrees'], cats.map((c, i) => [c, usd0(amt[i]), A(`${ps[i]}%`), A(`${ps[i] * 18 / 5}°`)]).concat([['<b>Total</b>', usd0(inc), '100%', '360°']]))),
        part('Draw the circle graph', `<div class="fin-row">${circ}<div>${ql(1, `${name} cuts the Fun money in half and puts it into savings. How much goes to savings each month now?`, aline('Answer', usd0((si >= 0 ? amt[si] : 0) + cut)))}${ql(2, 'Name one other change that would let ' + esc(name) + ' save more. Why?', lines(3))}</div></div>`)],
      items,
      mistakes: 'Dividing the total by the part instead of the part by the total, and using 100 degrees for the whole circle instead of 360.',
      notes: 'Every percent is a multiple of 5, so every angle is a whole number of degrees and the angles add to exactly 360°.',
      materials: 'pencil, calculator, protractor',
    };
  } };
VER.deg = p => `${fmt(p.a / p.b * 360, 2)}°`;
VER.cut = p => usd0(p.s + p.f / 2);

/* ===== Saving and interest ===== */
SK.simple = { area: 'save', label: 'Simple interest', lo: 5, hi: 12, count: [4, 6, 8],
  make(v, r, g, n) {
    const who = r.shuffle(NAMES);
    let k = 0;
    const one = () => {
      const nm = who[k++ % who.length], loan = r.chance(.4);
      let P, rt, yrs, mo = 0;
      if (g <= 5) { P = r.int(1, 10) * 100; rt = r.int(2, 10); yrs = r.int(1, 5); }
      else if (g === 6) { P = r.int(4, 100) * 50; rt = r.int(1, 12); yrs = r.int(1, 6); }
      else { P = r.int(5, 100) * 100; rt = r.int(2, 18) / 2; if (r.chance(.4)) { mo = r.pick([6, 18, 30, 42]); yrs = mo / 12; } else yrs = r.int(1, 8); }
      const Ic = P * rt * yrs;   // cents: dollars × percent
      if (Ic % 1) return null;
      const time = mo ? `${mo} months` : `${yrs} year${yrs > 1 ? 's' : ''}`;
      if (g >= 9 && r.chance(.35)) {   // find the rate or the time
        const findRate = r.chance(.5);
        return findRate ? { q: `${nm} ${loan ? 'borrows' : 'saves'} ${usd0(P)} for ${time} at simple interest and ${loan ? 'pays' : 'earns'} ${usd(Ic)} in interest. What is the yearly interest rate?`, ans: [['Rate', `${fmt(rt, 2)}%`]], k: 'sirate', p: { P, I: Ic, yrs } }
          : { q: `${nm} ${loan ? 'borrows' : 'saves'} ${usd0(P)} at ${fmt(rt, 2)}% simple interest and ${loan ? 'pays' : 'earns'} ${usd(Ic)} in interest. For how many years?`, ans: [['Time', `${fmt(yrs, 2)} years`]], k: 'sitime', p: { P, I: Ic, rt } };
      }
      return { q: loan ? `${nm} borrows ${usd0(P)} at ${fmt(rt, 2)}% simple interest a year for ${time}.` : `${nm} puts ${usd0(P)} in a savings account that pays ${fmt(rt, 2)}% simple interest a year, for ${time}.`,
        ans: [['Interest', usd(Ic)], [loan ? 'Total to pay back' : 'Balance at the end', usd(P * 100 + Ic)]], k: 'si', p: { P, rt, yrs } };
    };
    const list = r.distinct(n, one, x => x.q), items = [];
    list.forEach(x => x.ans.forEach(([l, a]) => items.push(I(`${x.q} ${l}`, a, x.k + (l.startsWith('Interest') || x.k !== 'si' ? '' : 'b'), x.p))));
    const nm = r.pick(NAMES.filter(x => !list.some(l => l.q.startsWith(x)))), P0 = g <= 5 ? 400 : 800, r0 = g <= 5 ? 3 : 4, r1 = r0 + r.int(1, 3), y0 = g <= 5 ? 2 : 3;
    const think = [I(`${nm}: interest at ${r1}%`, usd(P0 * r1 * y0), 'si', { P: P0, rt: r1, yrs: y0 }), I(`${nm}: more interest`, usd(P0 * (r1 - r0) * y0), 'simore', { P: P0, r0, r1, yrs: y0 }),
      I('Who is helped by higher rates', 'The saver earns more interest; the borrower pays more.', 'name', { t: 'The saver earns more interest; the borrower pays more.' })];
    return {
      ican: 'I can use I = P × r × t to find simple interest and the total.',
      directions: 'Use I = P × r × t, where P is the amount, r is the yearly rate as a decimal and t is the time in years. For months, divide by 12 to get years.',
      parts: [part('', box('<p><b>Simple interest:</b> I = P × r × t &nbsp; · &nbsp; Total = P + I</p>') + example(`${usd0(500)} at 4% for 3 years: I = ${usd0(500)} × 0.04 × 3 = <b>${usd(6000)}</b>.`, `Balance = ${usd0(500)} + ${usd(6000)} = <b>${usd(56000)}</b>. Months: 18 months is 18 ÷ 12 = 1.5 years.`)),
        part('Problems', probs(list.map((x, j) => prob(j + 1, esc(x.q), x.ans.map(([l, a]) => aline(l, a)))))),
        part('Think about it', ql(n + 1, `${nm} saves ${usd0(P0)} for ${y0} years. The bank raises its rate from ${r0}% to ${r1}%. How much interest does ${nm} earn at ${r1}%, and how much more is that than at ${r0}%?`, aline(`At ${r1}%`, think[0].a) + aline('How much more', think[1].a)) +
          ql(n + 2, 'When rates go up, who is helped: people who save or people who borrow? Explain.', lines(1) + h.keyline(esc(think[2].a))))],
      items: items.concat(think),
      mistakes: 'Using the percent as a whole number (4 instead of 0.04), and using months as years without dividing by 12.',
      notes: 'Simple interest is paid on the starting amount only, so it grows by the same amount every year. Interest always comes out to whole cents.',
    };
  } };
VER.si = p => usd(Math.round(p.P * 100 * (p.rt / 100) * p.yrs));
VER.sib = p => usd(Math.round(p.P * 100 * (1 + p.rt / 100 * p.yrs)));
VER.sirate = p => `${fmt(p.I / (p.P * p.yrs), 2)}%`;
VER.sitime = p => `${fmt(p.I / (p.P * p.rt), 2)} years`;
VER.simore = p => usd(p.P * p.r1 * p.yrs - p.P * p.r0 * p.yrs);

SK.sgraph = { area: 'save', label: 'Simple interest at two rates: table and graph', lo: 5, hi: 12, count: null,
  make(v, r, g) {
    const P = r.pick(g <= 5 ? [100, 200, 500] : [200, 500, 1000, 2000]), [r1, r2] = r.sample([1, 2, 3, 4, 5, 6, 8, 10], 2).sort((a, b) => a - b), Y = 5, name = r.pick(NAMES);
    const items = [], rows = [];
    for (let y = 0; y <= Y; y++) {
      const b1 = P * 100 + P * r1 * y, b2 = P * 100 + P * r2 * y;
      if (y) items.push(I(`Year ${y} at ${r1}%`, usd(b1), 'sib', { P, rt: r1, yrs: y }), I(`Year ${y} at ${r2}%`, usd(b2), 'sib', { P, rt: r2, yrs: y }));
      rows.push([y, y ? A(usd(b1)) : usd(b1), y ? A(usd(b2)) : usd(b2)]);
    }
    const hi = P * (1 + r2 * Y / 100), span = hi - P, st = nice(span, 6), lo = Math.floor(P / st) * st, top2 = top(hi, st);
    const gr = grid({ x: [0, Y, 1, 'Years'], y: [lo, top2, st, 'Balance (dollars)', y => usd0(y)], brk: lo > 0, title: `${usd0(P)} saved at ${r1}% and ${r2}% simple interest`,
      key: (X, Yf) => redLine(Array.from({ length: Y + 1 }, (_, y) => [y, P * (1 + r1 * y / 100)]), X, Yf) + redLine(Array.from({ length: Y + 1 }, (_, y) => [y, P * (1 + r2 * y / 100)]), X, Yf) +
        rtx(X(Y) - 4, Yf(P * (1 + r1 * Y / 100)) + 16, `${r1}%`, 'font-size="12" text-anchor="end"') + rtx(X(Y) - 4, Yf(hi) - 8, `${r2}%`, 'font-size="12" text-anchor="end"') });
    items.push(I(`Interest each year at ${r1}%`, usd(P * r1), 'si', { P, rt: r1, yrs: 1 }), I(`Interest each year at ${r2}%`, usd(P * r2), 'si', { P, rt: r2, yrs: 1 }),
      I('Difference after 5 years', usd(P * (r2 - r1) * Y), 'simore', { P, r0: r1, r1: r2, yrs: Y }));
    return {
      ican: 'I can make a table and a graph of simple interest and compare two rates.',
      directions: `${name} saves ${usd0(P)} for 5 years. Fill in the balance each year at ${r1}% and at ${r2}% simple interest. Plot both and connect each set of points with a line.`,
      parts: [part('', example(`At ${r1}%, the interest each year is ${usd0(P)} × ${fmt(r1 / 100, 2)} = ${usd(P * r1)}. Add it once for every year.`)),
        part('The table', T(['Year', `Balance at ${r1}%`, `Balance at ${r2}%`], rows)),
        part('The graph', gr),
        part('Questions', ql(1, `How much interest does ${name} earn each year at ${r1}%? At ${r2}%?`, aline(`At ${r1}%`, usd(P * r1)) + aline(`At ${r2}%`, usd(P * r2))) +
          ql(2, 'After 5 years, how much more is in the account at the higher rate?', aline('Answer', usd(P * (r2 - r1) * Y))) +
          ql(3, 'Why are both graphs straight lines? Which line is steeper, and why?', lines(2)))],
      items,
      mistakes: 'Adding interest on the new balance each year (that is compound interest), and starting the vertical scale at zero without room to see the difference.',
      notes: (lo > 0 ? `The vertical scale starts at ${usd0(lo)}, marked with a break, so the lines are easier to tell apart. ` : '') + 'Simple interest adds the same amount every year, so the points fall on a straight line. The key draws both lines.',
      materials: 'pencil, calculator, ruler, two colored pencils',
    };
  } };

// compound balances, rounded to cents once a year (as a bank statement would)
const yearly = (Pc, rt, y) => { let b = Pc; const out = [b]; for (let i = 0; i < y; i++) { b = b + Math.round(b * rt / 100); out.push(b); } return out; };
SK.svc = { area: 'save', label: 'Simple and compound interest, year by year', lo: 7, hi: 12, count: [4, 5, 6],
  make(v, r, g, n) {
    let P, rt, comp;
    for (let t = 0; t < 100; t++) { P = r.int(2, 10) * 500; rt = r.int(2, 8); comp = yearly(P * 100, rt, n); let ok = true; let b = P * 100; for (let y = 0; y < n; y++) { if (edgy(b * rt / 100)) ok = false; b = comp[y + 1]; } if (ok) break; }
    const items = [], rows = [[0, '', usd(P * 100), '', usd(P * 100)]];
    for (let y = 1; y <= n; y++) {
      const si = P * rt, ci = comp[y] - comp[y - 1];
      items.push(I(`Year ${y}: simple interest`, usd(si), 'si', { P, rt, yrs: 1 }), I(`Year ${y}: simple balance`, usd(P * 100 + si * y), 'sib', { P, rt, yrs: y }),
        I(`Year ${y}: compound interest`, usd(ci), 'cyi', { P, rt, y }), I(`Year ${y}: compound balance`, usd(comp[y]), 'cyb', { P, rt, y }));
      rows.push([y, A(usd(si)), A(usd(P * 100 + si * y)), A(usd(ci)), A(usd(comp[y]))]);
    }
    const more = comp[n] - (P * 100 + P * rt * n);
    items.push(I('How much more compound earns', usd(more), 'cmore', { P, rt, n }));
    return {
      ican: 'I can compare simple and compound interest in a year-by-year table.',
      directions: `${usd0(P)} is saved for ${n} years at ${rt}% a year. With simple interest, the interest is ${rt}% of the first ${usd0(P)} every year. With compound interest, it is ${rt}% of the balance at the start of that year. Round each year's interest to the nearest cent.`,
      parts: [part('', example(`Compound, year 1: ${rt}% × ${usd0(P)} = ${usd(P * rt)}, balance ${usd(comp[1])}.`, `Year 2: ${rt}% × ${usd(comp[1])} = ${usd(comp[2] - comp[1])}, balance ${usd(comp[2])}. The interest grows because the balance grows.`)),
        part('Side by side', T(['Year', 'Simple: interest', 'Simple: balance', 'Compound: interest', 'Compound: balance'], rows)),
        part('Questions', ql(1, `After ${n} years, how much more is in the compound account than in the simple one?`, aline('Answer', usd(more))) +
          ql(2, 'Why does the compound interest get bigger each year while the simple interest stays the same?', lines(2)))],
      items,
      mistakes: 'Finding compound interest on the first amount every year (that is simple interest), and rounding only at the end. This sheet rounds each year, as a bank does.',
      notes: 'The key rounds each year\'s compound interest to the nearest cent before adding it; the formula P(1 + r)^t can differ by a cent or two.',
    };
  } };
VER.cyi = p => { const b = yearly(p.P * 100, p.rt, p.y); return usd(b[p.y] - b[p.y - 1]); };
// a second route: the closed formula, which must agree with the rounded-each-year table to within a cent a year
VER.cyb = p => { const b = yearly(p.P * 100, p.rt, p.y)[p.y], c = p.P * 100 * (1 + p.rt / 100) ** p.y; return Math.abs(b - c) <= p.y ? usd(b) : 'formula disagrees'; };
VER.cmore = p => usd(yearly(p.P * 100, p.rt, p.n)[p.n] - p.P * 100 * (1 + p.rt * p.n / 100));

const NFREQ = [[1, 'once a year', 'annually'], [2, 'twice a year', 'semiannually'], [4, 'four times a year', 'quarterly'], [12, 'every month', 'monthly'], [365, 'every day', 'daily']];
const compound = (P, rt, nn, t) => P * (1 + rt / 100 / nn) ** (nn * t);    // dollars
const compoundIter = (P, rt, nn, t) => { let b = P; for (let i = 0; i < nn * t; i++) b *= 1 + rt / 100 / nn; return b; };
SK.compound = { area: 'save', label: 'The compound interest formula', lo: 8, hi: 12, count: [4, 6, 8],
  make(v, r, g, n) {
    const ns = g === 8 ? [1, 2, 4] : g <= 10 ? [1, 4, 12] : [1, 4, 12, 365], who = r.shuffle(NAMES);
    let k = 0;
    const list = r.distinct(n, () => {
      const P = r.int(g === 8 ? 2 : 1, 40) * (g === 8 ? 250 : 500), rt = g === 8 ? r.int(2, 8) : r.int(8, 28) / 4, nn = r.pick(ns), t = r.int(2, g === 8 ? 10 : 30), A1 = compound(P, rt, nn, t);
      if (edgy(A1 * 100)) return null;
      const f = NFREQ.find(x => x[0] === nn);
      return { q: `${who[k++ % who.length]} deposits ${usd0(P)} at ${fmt(rt, 2)}% interest compounded ${f[2]} and leaves it for ${t} years.`, P, rt, nn, t, A: Math.round(A1 * 100) };
    }, x => x.q);
    const items = [];
    list.forEach(x => items.push(I(`${x.q} Balance`, usd(x.A), 'cA', x), I(`${x.q} Interest`, usd(x.A - x.P * 100), 'cI', x)));
    const sub = x => `${usd0(x.P)}(1 + ${fmt(x.rt / 100, 4)}/${x.nn})<sup>${x.nn}×${x.t}</sup>`;
    const e = { P: 1000, rt: 6, nn: 4, t: 5 }, eA = Math.round(compound(1000, 6, 4, 5) * 100);
    return {
      ican: 'I can use A = P(1 + r/n)^(nt) to find a compound interest balance and the interest earned.',
      directions: 'For each account, write the formula with the numbers put in, then find the balance and the interest earned. Round money to the nearest cent at the end only.',
      parts: [part('', box('<p><b>A = P(1 + r/n)<sup>nt</sup></b> &nbsp; P = deposit, r = yearly rate as a decimal, n = times compounded each year, t = years. Interest = A − P.</p>') +
        example(`${usd0(1000)} at 6% compounded quarterly for 5 years: A = ${sub(e)} = ${usd0(1000)}(1.015)<sup>20</sup>`, `A = <b>${usd(eA)}</b>; interest = ${usd(eA)} − ${usd0(1000)} = <b>${usd(eA - 100000)}</b>`)),
        part('Problems', probs(list.map((x, j) => prob(j + 1, esc(x.q), [`<div class="fin-l"><span>Formula</span><span class="ws-ans">${sub(x)}</span></div>`, aline('Balance', usd(x.A)), aline('Interest earned', usd(x.A - x.P * 100))]))))],
      items,
      mistakes: 'Using the rate as a whole number (6 instead of 0.06), forgetting to divide the rate by n, and multiplying the exponent wrong (quarterly for 5 years is 20 periods). Round only at the end.',
      notes: 'Answers use the unrounded calculator value until the last step. A student who rounds 1 + r/n early may be off by a few cents.',
    };
  } };
VER.cA = p => usd(Math.round(compoundIter(p.P, p.rt, p.nn, p.t) * 100));
VER.cI = p => usd(Math.round(compoundIter(p.P, p.rt, p.nn, p.t) * 100) - p.P * 100);

SK.freq = { area: 'save', label: 'Annual, monthly or daily compounding', lo: 9, hi: 12, count: [3, 4, 5],
  make(v, r, g, n) {
    const who = r.sample(NAMES, n), items = [];
    const rows = who.map(nm => {
      let P, rt, t, vals;
      for (let k = 0; k < 100; k++) { P = r.int(2, 40) * 500; rt = r.int(8, 28) / 4; t = r.pick([5, 10, 10, 15, 20]); vals = [1, 12, 365].map(nn => compound(P, rt, nn, t)); if (!vals.some(x => edgy(x * 100))) break; }
      const c = vals.map(x => Math.round(x * 100));
      [1, 12, 365].forEach((nn, i) => items.push(I(`${nm}: compounded ${NFREQ.find(x => x[0] === nn)[2]}`, usd(c[i]), 'cA', { P, rt, nn, t })));
      items.push(I(`${nm}: daily minus annual`, usd(c[2] - c[0]), 'fdiff', { P, rt, t }));
      return [nm, usd0(P), `${fmt(rt, 2)}%`, t, A(usd(c[0])), A(usd(c[1])), A(usd(c[2])), A(usd(c[2] - c[0]))];
    });
    return {
      ican: 'I can compare the same deposit compounded annually, monthly and daily.',
      directions: 'Use A = P(1 + r/n)^(nt) with n = 1, 12 and 365. Round each balance to the nearest cent. Then find how much more daily compounding gives than annual.',
      parts: [part('', box('<p><b>A = P(1 + r/n)<sup>nt</sup></b> &nbsp; annually n = 1, monthly n = 12, daily n = 365</p>') + example(`${usd0(1000)} at 5% for 10 years: annually ${usd0(1000)}(1.05)<sup>10</sup> = ${usd(Math.round(compound(1000, 5, 1, 10) * 100))}; monthly ${usd0(1000)}(1 + 0.05/12)<sup>120</sup> = ${usd(Math.round(compound(1000, 5, 12, 10) * 100))}.`)),
        part('Compare', T(['Saver', 'Deposit', 'Rate', 'Years', 'Annually', 'Monthly', 'Daily', 'Daily − annual'], rows, 'fin-small')),
        part('Questions', ql(1, 'Does compounding more often always give more? Does it give a lot more? Use your table.', lines(2)) + ql(2, 'Which matters more for the final balance: how often interest compounds, or the rate and the number of years? Explain with one row.', lines(2)))],
      items,
      mistakes: 'Using 12 or 365 in the exponent without multiplying by the years, and rounding 1 + r/n before raising it to a power.',
      notes: 'Monthly and daily compounding beat annual, but only a little; the rate and the time matter far more. Daily uses n = 365.',
    };
  } };
VER.fdiff = p => usd(Math.round(compoundIter(p.P, p.rt, 365, p.t) * 100) - Math.round(compoundIter(p.P, p.rt, 1, p.t) * 100));

SK.rule72 = { area: 'save', label: 'The rule of 72', lo: 8, hi: 12, count: null,
  make(v, r, g) {
    const pool = g === 8 ? [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] : [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8, 9, 10, 11, 12];
    const rts = r.sample(pool, 8).sort((a, b) => a - b), items = [];
    rts.forEach(x => items.push(I(`Rule of 72 at ${x}%`, `${fix(72 / x, 1)} years`, 'r72', { x })));
    const chk = r.sample([6, 8, 9, 10, 12].filter(x => true), 2).sort((a, b) => a - b);
    const tabs = chk.map(x => { const b = yearly(100000, x, 14); const yr = b.findIndex(y => y >= 200000);
      b.slice(1, yr + 1).forEach((bb, i) => items.push(I(`At ${x}%, year ${i + 1}`, usd(bb), 'cyb', { P: 1000, rt: x, y: i + 1 })));
      items.push(I(`At ${x}%, doubles in year`, String(yr), 'dbl', { x }));
      return `<div>${T(['Year', `Balance at ${x}%`], [[0, usd(100000)], ...b.slice(1, yr + 1).map((bb, i) => [i + 1, A(usd(bb))])])}<p>It first reaches ${usd0(2000)} in year ${blank(String(yr), 3)}. Rule of 72: ${blank(`${fix(72 / x, 1)}`, 3)} years.</p></div>`; });
    return {
      ican: 'I can estimate doubling time with the rule of 72 and check it with a compound interest table.',
      directions: 'The rule of 72: money growing at r% a year doubles in about 72 ÷ r years. Estimate each doubling time to the nearest tenth of a year. Then check two of them by growing $1,000 year by year, rounding each year to the nearest cent.',
      parts: [part('', example('At 8% a year: 72 ÷ 8 = <b>9 years</b> to double.', '$1,000 at 8%: year 1 is $1,000 × 1.08 = $1,080.00; year 2 is $1,080.00 × 1.08 = $1,166.40; and so on.')),
        part('Estimate', T(['Rate', ...rts.map(x => `${fmt(x, 2)}%`)], [['Years to double', ...rts.map(x => A(fix(72 / x, 1)))]], 'fin-small')),
        part(`Check: ${usd0(1000)} at ${chk[0]}% and at ${chk[1]}%`, `<div class="fin-row">${tabs.join('')}</div>`),
        part('Think about it', ql(1, 'How close was the rule of 72 for your two checks? What happens to doubling time when the rate doubles?', lines(2)))],
      items,
      mistakes: 'Dividing 72 by the rate as a decimal (72 ÷ 0.08 = 900), and stopping the table one year early: the year it doubles is the first year the balance is $2,000 or more.',
      notes: 'The rule of 72 is an estimate. It is closest for rates from about 6% to 10%. A loan or card balance doubles the same way if nothing is paid.',
    };
  } };
VER.r72 = p => `${(Math.round(72 / p.x * 10) / 10).toFixed(1)} years`;
VER.dbl = p => String(Math.ceil(Math.log(2) / Math.log(1 + p.x / 100) - 1e-9) + (yearly(100000, p.x, 20)[Math.ceil(Math.log(2) / Math.log(1 + p.x / 100) - 1e-9)] >= 200000 ? 0 : 1));

const BANKS = ['River Bank', 'Summit Savings', 'Pine Hill Credit Union', 'Harbor Bank', 'Maple Trust', 'Lakeside Credit Union', 'Cedar Savings', 'Prairie Bank', 'Bluebird Bank', 'Granite Savings'];
SK.apy = { area: 'save', label: 'APR and APY: choose the best account', lo: 8, hi: 12, count: [4, 5, 6],
  make(v, r, g, n) {
    for (let t = 0; t < 200; t++) {
      const banks = r.sample(BANKS, n), ns = r.shuffle([1, 4, 12, 365, ...Array.from({ length: n }, () => r.pick([1, 2, 4, 12, 365]))]).slice(0, n);
      const accts = banks.map((b, i) => { const apr = r.int(30, 110) * 5 / 100, nn = ns[i], apy = ((1 + apr / 100 / nn) ** nn - 1) * 100; return { b, apr, nn, apy, show: Math.round(apy * 100) / 100 }; });
      if (accts.some(a => edgy(a.apy * 100))) continue;
      const best = Math.max(...accts.map(a => a.show));
      if (accts.filter(a => a.show === best).length > 1 || new Set(accts.map(a => a.show)).size < n) continue;
      const bestA = accts.find(a => a.show === best), items = accts.map(a => I(`${a.b}: APY`, `${a.show.toFixed(2)}%`, 'apy', a));
      items.push(I('Best account', bestA.b, 'apybest', { accts }));
      return {
        ican: 'I can turn an APR into an APY and use APY to compare savings accounts.',
        directions: 'APR is the yearly rate before compounding. APY is what the account really earns in a year: APY = (1 + APR/n)^n − 1, where n is the number of times it compounds each year. Find each APY as a percent to two decimal places, then choose the best account.',
        parts: [part('', example('4.80% APR compounded monthly: (1 + 0.048/12)<sup>12</sup> − 1 = 0.04907, so the APY is <b>4.91%</b>.')),
          part('The accounts', T(['Account', 'APR', 'Compounds', 'n', 'APY'], accts.map(a => [a.b, `${a.apr.toFixed(2)}%`, NFREQ.find(x => x[0] === a.nn)[2], A(String(a.nn)), A(`${a.show.toFixed(2)}%`)]))),
          part('Choose', ql(1, 'Which account earns the most in a year?', aline('Answer', bestA.b, 10)) + ql(2, 'Why do banks show the APY on savings accounts? Why might a lender prefer to advertise the APR on a loan?', lines(2)))],
        items: items.concat(accts.map(a => I(`${a.b}: n`, String(a.nn), 'nn', a))),
        mistakes: 'Choosing the highest APR without checking how often it compounds, and forgetting to subtract 1 (or the 100%) at the end.',
        notes: 'APY equals APR when interest compounds once a year. The difference grows with the rate and the number of compoundings, but daily is only a little more than monthly.',
      };
    }
    return null;
  } };
VER.apy = p => { let b = 1; for (let i = 0; i < p.nn; i++) b *= 1 + p.apr / 100 / p.nn; return `${(Math.round((b - 1) * 10000) / 100).toFixed(2)}%`; };
VER.apybest = p => p.accts.slice().sort((a, b) => b.apy - a.apy)[0].b;
VER.nn = p => String(p.nn);

const fvm = (pmt, rt, months) => { const i = rt / 1200; return i ? pmt * ((1 + i) ** months - 1) / i : pmt * months; };   // end-of-month deposits
const fvIter = (pmt, rt, months) => { let b = 0; for (let m = 0; m < months; m++) b = b * (1 + rt / 1200) + pmt; return b; };
SK.deposits = { area: 'save', label: 'Monthly deposits and starting early', lo: 9, hi: 12, count: [3, 4, 5],
  make(v, r, g, n) {
    const who = r.sample(NAMES, n + 2), items = [];
    const rows = [];
    for (const nm of who.slice(0, n)) for (let t = 0; t < 60; t++) {
      const pmt = r.int(1, 12) * 25, rt = r.int(6, 16) / 2, y = r.int(1, 8) * 5, fv = fvm(pmt, rt, y * 12);
      if (edgy(fv * 100)) continue;
      const F = Math.round(fv * 100), D = pmt * 12 * y * 100;
      items.push(I(`${nm}: total deposited`, usd(D), 'dep', { pmt, y }), I(`${nm}: balance`, usd(F), 'fv', { pmt, rt, m: y * 12 }), I(`${nm}: interest earned`, usd(F - D), 'fvi', { pmt, rt, m: y * 12 }));
      rows.push([nm, usd0(pmt), `${fmt(rt, 2)}%`, y, A(usd(D)), A(usd(F)), A(usd(F - D))]); break;
    }
    const [a, b] = who.slice(n), M = r.pick([25, 50, 75, 100]), rt = r.pick([4, 5, 6, 7]), age1 = r.pick([15, 16, 17, 18]), age2 = age1 + 10, ages = [];
    for (let x = age2; x < 65; x += 10) ages.push(x);
    ages.push(65);
    const brow = ages.map(x => { const f1 = Math.round(fvm(M, rt, (x - age1) * 12) * 100), f2 = Math.round(fvm(M, rt, (x - age2) * 12) * 100);
      items.push(I(`${a} at age ${x}`, usd(f1), 'fv', { pmt: M, rt, m: (x - age1) * 12 }), I(`${b} at age ${x}`, usd(f2), 'fv', { pmt: M, rt, m: (x - age2) * 12 }));
      return [x, A(usd(f1)), A(usd(f2))]; });
    if (ages.some(x => edgy(fvm(M, rt, (x - age1) * 12) * 100) || edgy(fvm(M, rt, (x - age2) * 12) * 100))) return null;
    const end1 = Math.round(fvm(M, rt, (65 - age1) * 12) * 100), end2 = Math.round(fvm(M, rt, (65 - age2) * 12) * 100);
    const mx = end1 / 100, st = nice(mx, 5);
    const gr = grid({ x: [age1, age1 + 50, 10, 'Age', x => fmt(x, 0)], y: [0, top(mx, st), st, 'Balance (dollars)', y => usd0(y)], W: 560, H: 280, small: true,
      title: `${usd0(M)} a month at ${rt}%`, key: (X, Y) => redLine([age1, ...ages].map(x => [x, fvm(M, rt, (x - age1) * 12)]), X, Y) + redLine([age2, ...ages].map(x => [x, fvm(M, rt, (x - age2) * 12)]), X, Y) +
        rtx(X(65) - 6, Y(mx) + 16, a, 'font-size="12" text-anchor="end"') + rtx(X(65) - 6, Y(end2 / 100) + 16, b, 'font-size="12" text-anchor="end"') });
    items.push(I('Difference at 65', usd(end1 - end2), 'fvd', { M, rt, m1: (65 - age1) * 12, m2: (65 - age2) * 12 }), I(`${a}: deposits by 65`, usd(M * 12 * (65 - age1) * 100), 'dep', { pmt: M, y: 65 - age1 }));
    return {
      ican: 'I can find the balance of monthly deposits with compound interest and see why starting early matters.',
      directions: 'Deposits go in at the end of each month and interest compounds monthly. Use the formula in the box. Round to the nearest cent.',
      parts: [part('', box('<p><b>Balance = D × ((1 + i)<sup>n</sup> − 1) ÷ i</b> &nbsp; D = monthly deposit, i = yearly rate ÷ 12 (as a decimal), n = number of months. This adds a geometric series: D + D(1 + i) + D(1 + i)<sup>2</sup> + … + D(1 + i)<sup>n − 1</sup>.</p>') +
        example(`${usd0(100)} a month at 6% for 10 years: i = 0.06 ÷ 12 = 0.005, n = 120.`, `Balance = ${usd0(100)} × (1.005<sup>120</sup> − 1) ÷ 0.005 = <b>${usd(Math.round(fvm(100, 6, 120) * 100))}</b>. Deposited ${usd0(12000)}, so interest earned ${usd(Math.round(fvm(100, 6, 120) * 100) - 1200000)}.`)),
        part('Savers', T(['Saver', 'Each month', 'Rate', 'Years', 'Total deposited', 'Balance', 'Interest earned'], rows, 'fin-small')),
        part(`Start at ${age1} or ${age2}?`, `<p>${a} and ${b} each put ${usd0(M)} a month into an account earning ${rt}% compounded monthly. ${a} starts at age ${age1}; ${b} starts at age ${age2}. Both keep going until 65.</p>` +
          T(['Age', `${a} (from ${age1})`, `${b} (from ${age2})`], brow) + gr +
          ql(1, `At 65, how much more does ${a} have than ${b}?`, aline('Answer', usd(end1 - end2))) + ql(2, `${a} deposited only ${usd0(M * 120)} more than ${b}. Why is the gap so much bigger?`, lines(2)))],
      items,
      mistakes: 'Using the yearly rate for i instead of the monthly rate, and years instead of months for n.',
      notes: 'The formula assumes each deposit is made at the end of the month. The rates are invented and steady; real investments go up and down.',
      materials: 'pencil, calculator, ruler',
    };
  } };
VER.dep = p => usd(p.pmt * 12 * p.y * 100);
VER.fv = p => usd(Math.round(fvIter(p.pmt, p.rt, p.m) * 100));
VER.fvi = p => usd(Math.round(fvIter(p.pmt, p.rt, p.m) * 100) - p.pmt * p.m * 100);
VER.fvd = p => usd(Math.round(fvIter(p.M, p.rt, p.m1) * 100) - Math.round(fvIter(p.M, p.rt, p.m2) * 100));

const GOALS = [['e-bike', 900, 1500], ['laptop', 500, 1100], ['used guitar', 150, 400], ['concert trip', 200, 600], ['phone', 300, 800], ['skateboard', 80, 200], ['camera', 300, 700], ['class trip', 250, 600]];
SK.goal = { area: 'save', label: 'Savings goals and emergency funds', lo: 6, hi: 12, count: [1, 2, 3],
  make(v, r, g, n) {
    const items = [], who = r.sample(NAMES, n + 5);
    const goals = r.sample(GOALS, n).map((G, i) => {
      const cost = r.int(G[1] / 10, G[2] / 10) * 10, have = r.chance(.5) ? 0 : r.int(1, Math.floor(cost / 40)) * 10;
      const amts = r.sample(g <= 6 ? [10, 15, 20, 25, 30, 40, 50] : [15, 20, 25, 35, 40, 45, 50, 60, 75], 3).sort((a, b) => a - b);
      const wk = amts.map(w => Math.ceil((cost - have) / w));
      amts.forEach((w, j) => items.push(I(`${who[i]}: weeks at ${usd0(w)} a week`, String(wk[j]), 'weeks', { need: cost - have, w })));
      return ql(i + 1, `${who[i]} wants a ${G[0]} that costs ${usd0(cost)}${have ? ` and has already saved ${usd0(have)}` : ''}. How many weeks will it take at each weekly amount?`,
        T(['Saves each week', ...amts.map(usd0)], [['Weeks needed', ...wk.map(x => A(String(x)))]]));
    });
    const wk = r.sample(JOBS, 4).slice(0, Math.min(4, n + 1)).map((j, i) => {
      const e = r.int(g <= 6 ? 16 : 20, g <= 6 ? 30 : 48) * 50, s = r.int(4, 12) * 25;
      const f3 = 3 * e, f6 = 6 * e, m3 = Math.ceil(f3 / s), m6 = Math.ceil(f6 / s), nm = who[n + i];
      items.push(I(`${nm}: 3-month fund`, usd0(f3), 'fund', { e, k: 3 }), I(`${nm}: 6-month fund`, usd0(f6), 'fund', { e, k: 6 }),
        I(`${nm}: months to 3`, String(m3), 'weeks', { need: f3, w: s }), I(`${nm}: months to 6`, String(m6), 'weeks', { need: f6, w: s }));
      return [`${nm}, ${j[0]}`, usd0(e), usd0(s), A(usd0(f3)), A(usd0(f6)), A(String(m3)), A(String(m6))];
    });
    return {
      ican: 'I can plan how long it takes to reach a savings goal and size an emergency fund.',
      directions: 'Divide what is still needed by the amount saved each time. If it does not divide evenly, round up: a partial week still has to be waited out.',
      parts: [part('', example(`Goal ${usd0(450)}, saving ${usd0(40)} a week: ${usd0(450)} ÷ ${usd0(40)} = 11.25, so it takes <b>12 weeks</b>.`, 'After 11 weeks there is only $440, not enough yet.')),
        part('Saving for a goal', goals.join('')),
        part('Emergency funds', `<p>An emergency fund covers 3 to 6 months of needed expenses if pay stops. Find each worker's 3-month and 6-month fund and how many months of saving each takes.</p>` +
          T(['Worker', 'Expenses a month', 'Saves a month', '3-month fund', '6-month fund', 'Months to save 3', 'Months to save 6'], wk, 'fin-small'))],
      items,
      mistakes: 'Rounding 11.25 weeks down to 11, which leaves the goal short, and subtracting what is already saved from the weekly amount instead of from the goal.',
      notes: 'The 3-to-6-month emergency fund is a common guideline; workers with less steady pay often aim for more.',
    };
  } };
VER.weeks = p => { let w = 0, s = 0; while (s < p.need) { s += p.w; w++; } return String(w); };
VER.fund = p => usd0(p.e * p.k);

SK.infl = { area: 'save', label: 'Raises, returns and inflation', lo: 7, hi: 12, count: [3, 4, 5],
  make(v, r, g, n) {
    const who = r.sample(NAMES, n), items = [];
    const rows = who.map(nm => {
      const j = r.pick(JOBS), w = hourly(r, j, 9), raise = r.int(0, 12) / 2, inf = r.int(2, 10) / 2;
      if (raise === inf) return null;
      const nw = w + half(w, raise * 100), need = w + half(w, inf * 100), res = raise > inf ? 'rose' : 'fell';
      items.push(I(`${nm}: new wage`, usd(nw), 'raise', { w, p: raise }), I(`${nm}: wage to keep up`, usd(need), 'raise', { w, p: inf }), I(`${nm}: buying power`, res, 'bp', { a: raise, b: inf }));
      return [`${nm}, ${j[0]}`, usd(w), `${fmt(raise, 1)}%`, `${fmt(inf, 1)}%`, A(usd(nw)), A(usd(need)), A(res)];
    });
    if (rows.some(x => !x)) return null;
    const parts = [part('', example(`A ${usd(2000)} wage with a 3% raise: ${usd(2000)} × 1.03 = ${usd(2060)}. If prices rose 5%, keeping up would take ${usd(2000)} × 1.05 = ${usd(2100)}.`, 'The raise is smaller than inflation, so buying power <b>fell</b>.')),
      part('Did the raise keep up?', T(['Worker', 'Old wage', 'Raise', 'Inflation', 'New wage', 'Wage needed to keep up', 'Buying power rose or fell'], rows, 'fin-small'))];
    if (g >= 9) {
      const inf = r.pick([2, 2.5, 3, 3.5, 4]), acc = r.sample(['basic savings account', 'high-yield savings account', 'certificate of deposit', 'checking account', 'stock index fund (one year)', 'money market account'], 4);
      const rr = acc.map(a => { let x; do { x = r.int(0, 20) / 4; } while (x === inf); return x; });
      acc.forEach((a, i) => items.push(I(`Real return: ${a}`, pc(rr[i] - inf), 'real', { n: rr[i], i: inf }), I(`Buying power: ${a}`, rr[i] > inf ? 'grows' : 'shrinks', 'bp2', { a: rr[i], b: inf })));
      parts.push(part(`Beating inflation (inflation is ${fmt(inf, 1)}%)`, `<p>Real return ≈ interest rate − inflation rate. A negative real return means the money buys less at the end of the year, even though the balance went up.</p>` +
        T(['Account', 'Interest rate', 'Real return', 'Buying power grows or shrinks?'], acc.map((a, i) => [a, `${fmt(rr[i], 2)}%`, A(pc(rr[i] - inf)), A(rr[i] > inf ? 'grows' : 'shrinks')]))));
    }
    parts.push(part('Explain', ql(1, 'A worker gets a raise and still can buy less than last year. How can that be?', lines(2))));
    return {
      ican: 'I can compare a raise or an interest rate with inflation to tell whether buying power rose or fell.',
      directions: 'Find each new wage and the wage needed to keep up with inflation (round to the nearest cent). Buying power rose if the raise is bigger than inflation.',
      parts, items,
      mistakes: 'Comparing the new wage with the old wage instead of with the wage needed to keep up, and treating a bigger balance as more buying power.',
      notes: 'Raises and inflation rates are invented. The real return uses the common estimate rate − inflation; the exact real rate is (1 + rate) ÷ (1 + inflation) − 1, which is a little smaller.',
    };
  } };
VER.raise = p => usd(Math.round(p.w * (1 + p.p / 100) + 1e-7));
VER.bp = p => p.a > p.b ? 'rose' : 'fell';
VER.bp2 = p => p.a > p.b ? 'grows' : 'shrinks';
VER.real = p => pc(p.n - p.i);

SK.index = { area: 'save', label: 'Real and nominal values with a price index', lo: 9, hi: 12, count: [5, 6, 8],
  make(v, r, g, n) {
    const y0 = r.int(1990, 2014), what = r.pick([['hourly wage for a nursing assistant', 900, 1600], ['hourly wage for a line cook', 700, 1300], ['yearly cost of a bus pass', 40000, 70000], ['price of a movie ticket', 500, 900]]);
    const rows = [], items = [];
    let idx = 100, nom = r.int(what[1] / 10, what[2] / 10) * 10;
    for (let i = 0; i < n; i++) {
      if (i) { idx = Math.round((idx * (1 + r.int(5, 40) / 1000)) * 10) / 10; nom = Math.round(nom * (1 + r.int(-5, 60) / 1000)); }
      const real = nom * 100 / idx;
      if (edgy(real)) return null;
      rows.push({ y: y0 + 2 * i, nom, idx, real: Math.round(real) });
    }
    rows.forEach(x => items.push(I(`Real value in ${x.y}`, usd(x.real), 'realv', x)));
    const best = rows.reduce((a, b) => b.real > a.real ? b : a);
    if (rows.filter(x => x.real === best.real).length > 1) return null;
    const up = rows[n - 1].real > rows[0].real ? 'rose' : 'fell';
    items.push(I('Highest real value year', String(best.y), 'name', { t: String(best.y) }), I('Real change first to last', up, 'name', { t: up }));
    return {
      ican: 'I can use a price index to turn nominal values into real values and compare them across years.',
      directions: `The table shows a ${what[0]} in several years, in the dollars of that year (nominal), and a made-up price index with ${y0} = 100. Real value = nominal value × 100 ÷ price index, in ${y0} dollars. Round to the nearest cent.`,
      parts: [part('', example(`Nominal ${usd(1500)} when the index is 120: ${usd(1500)} × 100 ÷ 120 = <b>${usd(1250)}</b> in base-year dollars.`)),
        part('Real values', T(['Year', 'Nominal', 'Price index', `Real (${y0} dollars)`], rows.map(x => [x.y, usd(x.nom), fmt(x.idx, 1), A(usd(x.real))]))),
        part('Questions', ql(1, 'In which year was the real value highest?', aline('Answer', String(best.y))) + ql(2, `From ${rows[0].y} to ${rows[n - 1].y}, did the real value rise or fall?`, aline('Answer', up)) +
          ql(3, 'Why do economists use real values, not nominal ones, to compare wages over time?', lines(2)))],
      items,
      mistakes: 'Multiplying by the index instead of dividing, and comparing nominal values across years as if a dollar always bought the same amount.',
      notes: 'The price index is invented; a real one is the Consumer Price Index. A real value answers: what would this be worth in base-year prices?',
    };
  } };
VER.realv = p => usd(Math.round(p.nom / (p.idx / 100)));

/* ===== Credit, loans and college costs ===== */
// a card balance month by month: interest rounded to cents, then a payment; min: 3% of the balance after interest, at least $25
function cardRun(B0, mr, pay, months) {
  const rows = []; let b = B0;
  for (let m = 1; m <= months; m++) { const it = Math.round(b * mr / 100), nb = b + it, p = pay === 'min' ? Math.min(nb, Math.max(2500, Math.round(nb * 0.03))) : Math.min(nb, pay); rows.push({ m, b, it, p, e: nb - p, edge: edgy(b * mr / 100) || edgy(nb * 0.03) }); b = nb - p; }
  return rows;
}
SK.card = { area: 'credit', label: 'A credit card balance, month by month', lo: 7, hi: 12, count: null,
  make(v, r, g) {
    const hs = g >= 9, name = r.pick(NAMES);
    for (let t = 0; t < 100; t++) {
      const B0 = hs ? r.int(15, 40) * 10000 : r.int(8, 18) * 5000, apr = hs ? r.pick([18, 19.99, 21, 22, 24, 24.99, 26]) : 0, mr = hs ? apr / 12 : r.pick([1.5, 2, 2.5]);
      const fixed = hs ? r.int(10, 20) * 1000 : r.int(5, 10) * 1000;
      const a = cardRun(B0, mr, 'min', 6), b = cardRun(B0, mr, fixed, 6);
      if (a.concat(b).some(x => x.edge) || b[5].e <= 0) continue;
      const items = [];
      const tab = (rows, lab, isMin) => { rows.forEach(x => items.push(I(`${lab}, month ${x.m}: interest`, usd(x.it), 'cint', { b: x.b, mr }), ...(isMin ? [I(`${lab}, month ${x.m}: payment`, usd(x.p), 'cmin', { b: x.b, mr })] : []), I(`${lab}, month ${x.m}: end balance`, usd(x.e), 'cend', { b: x.b, mr, pay: isMin ? 'min' : fixed })));
        return T(['Month', 'Starting balance', 'Interest', 'Payment', 'Ending balance'], rows.map(x => [x.m, x.m === 1 ? usd(x.b) : A(usd(x.b)), A(usd(x.it)), isMin ? A(usd(x.p)) : usd(x.p), A(usd(x.e))])); };
      const ta = tab(a, 'Minimum', true), tb = tab(b, 'Fixed', false);
      const ia = a.reduce((s, x) => s + x.it, 0), ib = b.reduce((s, x) => s + x.it, 0);
      items.push(I('Interest paid, minimum plan', usd(ia), 'csumi', { B0, mr, pay: 'min' }), I('Interest paid, fixed plan', usd(ib), 'csumi', { B0, mr, pay: fixed }),
        I('Balance paid down, minimum plan', usd(B0 - a[5].e), 'cdown', { B0, mr, pay: 'min' }), I('Balance paid down, fixed plan', usd(B0 - b[5].e), 'cdown', { B0, mr, pay: fixed }));
      // payoff, for the teacher page
      const payoff = pay => { let b2 = B0, m = 0, it = 0; while (b2 > 0 && m < 1200) { const i2 = Math.round(b2 * mr / 100), nb = b2 + i2, p = pay === 'min' ? Math.min(nb, Math.max(2500, Math.round(nb * 0.03))) : Math.min(nb, pay); it += i2; b2 = nb - p; m++; } return [m, it]; };
      const [ma, iA] = payoff('min'), [mb, iB] = payoff(fixed);
      const rateTxt = hs ? `${fmt(apr, 2)}% APR, so the monthly rate is ${fmt(apr, 2)}% ÷ 12 = ${fix(mr, 4)}%` : `${fmt(mr, 1)}% interest each month`;
      return {
        ican: 'I can track a credit card balance month by month and see how the payment changes the interest paid.',
        directions: `${name} owes ${usd(B0)} on a card at ${rateTxt}. No new purchases are made. Each month: interest = monthly rate × starting balance (round to the nearest cent); add it, then subtract the payment.`,
        parts: [part('', box(`<p><b>Minimum payment:</b> 3% of the balance after interest is added, but at least ${usd0(25)}. &nbsp; <b>Fixed plan:</b> ${usd(fixed)} every month.</p>`) +
          example(`Starting balance ${usd(50000)} at ${fmt(mr, 4)}%: interest = ${usd(50000)} × ${fix(mr / 100, 6)} = ${usd(Math.round(50000 * mr / 100))}. Balance after interest ${usd(50000 + Math.round(50000 * mr / 100))}.`)),
          part('Plan 1: minimum payments only', ta), part(`Plan 2: ${usd(fixed)} a month`, tb),
          part('Compare', T(['', 'Minimum plan', 'Fixed plan'], [['Interest paid in 6 months', A(usd(ia)), A(usd(ib))], ['How much the balance went down', A(usd(B0 - a[5].e)), A(usd(B0 - b[5].e))]]) +
            ql(1, 'Why is paying only the minimum called a trap?', lines(2)))],
        items,
        mistakes: 'Subtracting the payment before adding interest, and finding the interest on the first balance every month instead of on that month\'s starting balance.',
        notes: `If the plans kept going, the minimum plan would take ${ma} months and ${usd(iA)} of interest to pay off; the fixed plan would take ${mb} months and ${usd(iB)} of interest. Rates and balances are invented.`,
      };
    }
    return null;
  } };
VER.cint = p => usd(Math.round(p.b * p.mr / 100));
VER.cmin = p => { const nb = p.b + Math.round(p.b * p.mr / 100); return usd(Math.min(nb, Math.max(2500, Math.round(nb * 3 / 100)))); };
VER.cend = p => { const nb = p.b + Math.round(p.b * p.mr / 100), pay = p.pay === 'min' ? Math.min(nb, Math.max(2500, Math.round(nb * 3 / 100))) : Math.min(nb, p.pay); return usd(nb - pay); };
VER.csumi = p => usd(cardRun(p.B0, p.mr, p.pay, 6).reduce((a, x) => a + x.it, 0));
// a second route: what the balance fell by = payments minus interest
VER.cdown = p => { const rs = cardRun(p.B0, p.mr, p.pay, 6); return usd(rs.reduce((a, x) => a + x.p - x.it, 0)); };

const payment = (P, apr, months) => { const i = apr / 1200; return P * i / (1 - (1 + i) ** -months); };   // dollars
// a second route: bisect for the payment that leaves a zero balance
const payBisect = (P, apr, months) => { let lo = 0, hi = P; for (let k = 0; k < 200; k++) { const m = (lo + hi) / 2; let b = P; for (let j = 0; j < months; j++) b = b * (1 + apr / 1200) - m; if (b > 0) lo = m; else hi = m; } return (lo + hi) / 2; };
const LOANS = [['car', 8000, 32000], ['used car', 5000, 15000], ['truck', 18000, 40000], ['motorcycle', 4000, 12000], ['home repair', 5000, 20000], ['boat', 10000, 30000]];
SK.loan = { area: 'credit', label: 'The loan payment formula and total interest', lo: 10, hi: 12, count: [3, 4, 6],
  make(v, r, g, n) {
    const who = r.shuffle(NAMES); let k = 0;
    const list = r.distinct(n, () => {
      const L = r.pick(LOANS), P = r.int(L[1] / 500, L[2] / 500) * 500, apr = r.int(12, 48) / 4, yrs = r.int(2, 6), M = payment(P, apr, yrs * 12);
      if (edgy(M * 100)) return null;
      const Mc = Math.round(M * 100);
      return { q: `${who[k++ % who.length]} borrows ${usd0(P)} for a ${L[0]} at ${fmt(apr, 2)}% APR for ${yrs} years, paid monthly.`, P, apr, yrs, Mc };
    }, x => x.q);
    const items = [];
    list.forEach(x => items.push(I(`${x.q} Payment`, usd(x.Mc), 'lpay', x), I(`${x.q} Total paid`, usd(x.Mc * x.yrs * 12), 'ltot', x), I(`${x.q} Total interest`, usd(x.Mc * x.yrs * 12 - x.P * 100), 'lint', x)));
    const eM = Math.round(payment(10000, 6, 36) * 100);
    return {
      ican: 'I can find a monthly loan payment with the payment formula and the total interest on the loan.',
      directions: 'Use the formula in the box with i = APR ÷ 12 as a decimal and n = the number of monthly payments. Round the payment to the nearest cent. Total paid = payment × n; total interest = total paid − amount borrowed.',
      parts: [part('', box('<p><b>M = P × i ÷ (1 − (1 + i)<sup>−n</sup>)</b> &nbsp; Where it comes from: each payment pays back its value today, M ÷ (1 + i)<sup>k</sup>. Those values form a geometric series, and setting their sum equal to P gives the formula.</p>') +
        example(`${usd0(10000)} at 6% APR for 3 years: i = 0.06 ÷ 12 = 0.005, n = 36. M = ${usd0(10000)} × 0.005 ÷ (1 − 1.005<sup>−36</sup>) = <b>${usd(eM)}</b>.`, `Total paid = 36 × ${usd(eM)} = ${usd(eM * 36)}; total interest = <b>${usd(eM * 36 - 1000000)}</b>.`)),
        part('Problems', probs(list.map((x, j) => prob(j + 1, esc(x.q), [`<div class="fin-l"><span>i and n</span><span class="ws-ans">i = ${fix(x.apr / 1200, 6)}, n = ${x.yrs * 12}</span></div>`, aline('Payment', usd(x.Mc)), aline('Total paid', usd(x.Mc * x.yrs * 12)), aline('Total interest', usd(x.Mc * x.yrs * 12 - x.P * 100))]))))],
      items,
      mistakes: 'Using the yearly rate for i, using years for n, and dropping the minus sign in the exponent. The key uses the rounded payment for the totals.',
      notes: 'Real lenders round the payment to the cent and adjust the last payment, so their totals can differ by a few cents. Rates are invented but realistic.',
    };
  } };
VER.lpay = p => usd(Math.round(payBisect(p.P, p.apr, p.yrs * 12) * 100));
VER.ltot = p => usd(Math.round(payBisect(p.P, p.apr, p.yrs * 12) * 100) * p.yrs * 12);
VER.lint = p => usd(Math.round(payBisect(p.P, p.apr, p.yrs * 12) * 100) * p.yrs * 12 - p.P * 100);

SK.amort = { area: 'credit', label: 'Amortization table: the first payments', lo: 10, hi: 12, count: [4, 6, 8],
  make(v, r, g, n) {
    const name = r.pick(NAMES), L = r.pick(LOANS.slice(0, 3));
    for (let t = 0; t < 100; t++) {
      const P = r.int(L[1] / 500, L[2] / 500) * 500, apr = r.int(12, 40) / 4, yrs = r.int(3, 6), M = payment(P, apr, yrs * 12);
      if (edgy(M * 100)) continue;
      const Mc = Math.round(M * 100), rows = []; let b = P * 100, bad = false;
      for (let m = 1; m <= n; m++) { const it = Math.round(b * apr / 1200); if (edgy(b * apr / 1200)) bad = true; rows.push({ m, it, pr: Mc - it, b: b - (Mc - it) }); b -= Mc - it; }
      if (bad) continue;
      const items = [I('Monthly payment', usd(Mc), 'lpay', { P, apr, yrs })];
      rows.forEach(x => items.push(I(`Month ${x.m}: interest`, usd(x.it), 'aint', { P, apr, Mc, m: x.m }), I(`Month ${x.m}: principal`, usd(x.pr), 'apr', { P, apr, Mc, m: x.m }), I(`Month ${x.m}: balance`, usd(x.b), 'abal', { P, apr, Mc, m: x.m })));
      const totI = Mc * yrs * 12 - P * 100;
      items.push(I('Total interest over the loan', usd(totI), 'lint', { P, apr, yrs }));
      return {
        ican: 'I can complete an amortization table and see how each payment splits between interest and principal.',
        directions: `${name} borrows ${usd0(P)} for a ${L[0]} at ${fmt(apr, 2)}% APR for ${yrs} years (${yrs * 12} monthly payments). Find the payment with the formula, then fill in the first ${n} rows. Interest each month = balance × APR ÷ 12, rounded to the nearest cent.`,
        parts: [part('', box('<p><b>M = P × i ÷ (1 − (1 + i)<sup>−n</sup>)</b>, i = APR ÷ 12. Each row: interest = balance × i; principal = payment − interest; new balance = balance − principal.</p>') +
          ql(1, 'What is the monthly payment?', aline('Payment', usd(Mc)))),
          part('Amortization table', T(['Month', 'Payment', 'Interest', 'Principal', 'Balance'], [[0, '', '', '', usd(P * 100)], ...rows.map(x => [x.m, A(usd(Mc)), A(usd(x.it)), A(usd(x.pr)), A(usd(x.b))])])),
          part('Questions', ql(2, 'Estimate the total interest for the whole loan: payment × number of payments − amount borrowed.', aline('Answer', usd(totI))) +
            ql(3, 'Look down the Interest and Principal columns. What happens to each, and why?', lines(2)))],
        items,
        mistakes: 'Finding interest on the original amount every month instead of on the current balance, and subtracting the whole payment from the balance instead of only the principal.',
        notes: 'Interest shrinks and principal grows each month because the balance falls. The total-interest estimate uses the rounded payment; the lender\'s last payment absorbs the leftover cents.',
      };
    }
    return null;
  } };
const amortRow = (P, apr, Mc, m) => { let b = P * 100, it = 0; for (let k = 1; k <= m; k++) { it = Math.round(b * apr / 1200); b -= Mc - it; } return { it, b }; };
VER.aint = p => usd(amortRow(p.P, p.apr, p.Mc, p.m).it);
VER.apr = p => usd(p.Mc - amortRow(p.P, p.apr, p.Mc, p.m).it);
// a second route: the closed form for the balance after m payments, which must agree with the rounded table to within a cent a month
VER.abal = p => { const b = amortRow(p.P, p.apr, p.Mc, p.m).b, i = p.apr / 1200, c = p.P * 100 * (1 + i) ** p.m - p.Mc * ((1 + i) ** p.m - 1) / i; return Math.abs(b - c) <= p.m ? usd(b) : 'closed form disagrees'; };

SK.grid = { area: 'credit', label: 'Loan costs at different rates and terms', lo: 7, hi: 12, count: null,
  make(v, r, g) {
    const L = r.pick(LOANS.slice(0, 3)), P = r.int(L[1] / 1000, L[2] / 1000) * 1000;
    const opts = g === 7 ? r.sample([3, 4, 5, 6, 7, 8, 9], 4).sort((a, b) => a - b).map(x => [x, 5]) : (() => { const [a, b] = r.sample([3, 4, 5, 6, 7, 8], 2).sort((x, y) => x - y), ts = r.pick([[3, 4, 5], [2, 4, 6], [3, 5, 6]]); return [a, b].flatMap(x => ts.map(t => [x, t])); })();
    const rows = opts.map(([apr, y]) => ({ apr, y, Mc: Math.round(payment(P, apr, y * 12) * 100) }));
    if (opts.some(([apr, y]) => edgy(payment(P, apr, y * 12) * 100))) return null;
    const items = [];
    rows.forEach(x => { const tot = x.Mc * x.y * 12; items.push(I(`${x.apr}% for ${x.y} years: total paid`, usd(tot), 'mul', { a: x.Mc, b: x.y * 12 }), I(`${x.apr}% for ${x.y} years: interest`, usd(tot - P * 100), 'gint', { Mc: x.Mc, n: x.y * 12, P })); });
    const lowPay = rows.reduce((a, b) => b.Mc < a.Mc ? b : a), lowTot = rows.reduce((a, b) => b.Mc * b.y < a.Mc * a.y ? b : a);
    const lab = x => `${x.apr}%, ${x.y} yr`;
    items.push(I('Lowest monthly payment', lab(lowPay), 'name', { t: lab(lowPay) }), I('Lowest total cost', lab(lowTot), 'name', { t: lab(lowTot) }));
    const parts = [part('', example(`${usd(31500)} a month for 48 months: 48 × ${usd(31500)} = ${usd(1512000)} total. Interest = ${usd(1512000)} − ${usd0(13000)} = <b>${usd(212000)}</b>.`)),
      part(`A ${usd0(P)} ${L[0]} loan`, T(['Rate (APR)', 'Term', 'Number of payments', 'Monthly payment', 'Total paid', 'Total interest'], rows.map(x => [`${x.apr}%`, `${x.y} years`, x.y * 12, usd(x.Mc), A(usd(x.Mc * x.y * 12)), A(usd(x.Mc * x.y * 12 - P * 100))])))];
    if (v.graph) parts.push(part('Graph the total interest', barFrame(rows.map(lab), rows.map(x => (x.Mc * x.y * 12 - P * 100) / 100), 'Total interest for each loan', 'Interest (dollars)', true)));
    parts.push(part('Questions', ql(1, 'Which loan has the lowest monthly payment?', aline('Answer', lab(lowPay), 8)) + ql(2, 'Which loan costs the least in total?', aline('Answer', lab(lowTot), 8)) +
      ql(3, g === 7 ? 'How does a higher rate change the total cost of the loan?' : 'A longer term lowers the monthly payment. What does it cost you? Which loan would you choose, and why?', lines(2))));
    return {
      ican: 'I can find the total cost and interest of loans and compare rates and terms.',
      directions: 'Each monthly payment is given. Multiply by the number of payments to find the total paid, then subtract the amount borrowed to find the interest.',
      parts, items,
      mistakes: 'Multiplying the payment by the years instead of the months, and choosing the lowest monthly payment as the cheapest loan.',
      notes: 'The monthly payments come from the standard loan payment formula, rounded to the nearest cent. Rates are invented but realistic.',
      materials: 'pencil, calculator' + (v.graph ? ', ruler' : ''),
    };
  } };
VER.gint = p => usd(p.Mc * p.n - p.P * 100);

const SCHOOLS = [['Lakeside State University', 9000, 14000], ['Hillcrest College', 30000, 52000], ['Northfield University', 24000, 42000], ['Riverbend State College', 8000, 12500], ['Mesa Tech Institute', 11000, 18000], ['Pinewood College', 28000, 48000]];
SK.aid = { area: 'credit', label: 'Compare two college award letters', lo: 9, hi: 12, count: null,
  make(v, r) {
    const name = r.pick(NAMES), sch = r.sample(SCHOOLS, 2), items = [];
    const S = sch.map(s => {
      const tu = r.int(s[1] / 100, s[2] / 100) * 100, hf = r.int(100, 150) * 100, bk = r.int(8, 14) * 100, tr = r.int(5, 20) * 100;
      const gr = r.int(10, 70) * 100, sc = r.int(0, Math.floor(tu / 200)) * 100, ws = r.pick([0, 1500, 2000, 2500, 3000]), ln = r.pick([3500, 4500, 5500]);
      const coa = tu + hf + bk + tr, gift = gr + sc, net = coa - gift, left = coa - gift - ws - ln;
      return { n: s[0], tu, hf, bk, tr, gr, sc, ws, ln, coa, gift, net, left };
    });
    if (S[0].net === S[1].net || S.some(s => s.left < 0)) return null;
    S.forEach(s => items.push(I(`${s.n}: cost of attendance`, usd0(s.coa), 'sum0', { xs: [s.tu, s.hf, s.bk, s.tr] }), I(`${s.n}: gift aid`, usd0(s.gift), 'sum0', { xs: [s.gr, s.sc] }),
      I(`${s.n}: net cost`, usd0(s.net), 'net0', { a: s.coa, xs: [s.gr, s.sc] }), I(`${s.n}: loans over 4 years`, usd0(s.ln * 4), 'm4', { a: s.ln }), I(`${s.n}: still to pay`, usd0(s.left), 'net0', { a: s.coa, xs: [s.gr, s.sc, s.ws, s.ln] })));
    const lower = S[0].net < S[1].net ? S[0] : S[1];
    items.push(I('Lower net cost', lower.n, 'name', { t: lower.n }), I('Difference in net cost', usd0(Math.abs(S[0].net - S[1].net)), 'eq0', { a: Math.abs(S[0].net - S[1].net) }));
    const col = f => S.map(f);
    return {
      ican: 'I can read an award letter, find the net cost of college and tell gift aid from loans.',
      directions: `${name} got award letters from two schools for one year. Gift aid (grants and scholarships) does not have to be paid back. Work-study is pay for a campus job, and loans must be paid back with interest.`,
      parts: [part('The award letters', T(['', ...col(s => esc(s.n))], [
        ['Tuition and fees', ...col(s => usd0(s.tu))], ['Housing and food', ...col(s => usd0(s.hf))], ['Books and supplies', ...col(s => usd0(s.bk))], ['Transportation', ...col(s => usd0(s.tr))],
        ['<b>Cost of attendance</b>', ...col(s => A(usd0(s.coa)))], ['Grant', ...col(s => usd0(s.gr))], ['Scholarship', ...col(s => usd0(s.sc))], ['<b>Gift aid</b>', ...col(s => A(usd0(s.gift)))],
        ['<b>Net cost</b> (cost − gift aid)', ...col(s => A(usd0(s.net)))], ['Work-study', ...col(s => usd0(s.ws))], ['Student loan', ...col(s => usd0(s.ln))],
        ['Loans over 4 years (same each year)', ...col(s => A(usd0(s.ln * 4)))], ['<b>Still to pay</b> after all aid', ...col(s => A(usd0(s.left)))]])),
        part('Questions', ql(1, 'Which school has the lower net cost for one year, and by how much?', aline('School', lower.n, 12) + aline('By how much', usd0(Math.abs(S[0].net - S[1].net)))) +
          ql(2, 'One school offers more total aid. Why is total aid not the best way to compare? What else would you ask each school?', lines(3)))],
      items,
      mistakes: 'Counting loans and work-study as if they lower the cost. Loans are paid back with interest, and work-study is earned by working.',
      notes: 'All schools, costs and awards are invented. "Net cost" here is cost of attendance minus gift aid, the same idea as the net price colleges report.',
    };
  } };
VER.net0 = p => usd0(p.xs.reduce((a, b) => a - b, p.a));
VER.m4 = p => usd0(p.a * 4);
VER.eq0 = p => usd0(p.a);

/* ===== Insurance, investing and big purchases ===== */
// plans: {name, prem (yearly cents), ded (cents, per claim), coins (percent you pay after the deductible), oop (cap, cents), covers: [types]}
function youPay(pl, events) {   // events: [{type, cost}] in one year; health uses a yearly deductible, others a deductible per claim
  let pay = pl.prem;
  if (pl.health) { const tot = events.reduce((a, e) => a + e.cost, 0), d = Math.min(tot, pl.ded); return pay + Math.min(pl.oop, d + Math.round((tot - d) * pl.coins / 100)); }
  for (const e of events) pay += pl.covers.includes(e.type) ? Math.min(e.cost, pl.ded) : e.cost;
  return pay;
}
const INS = {
  bike: { lo: 6, label: 'E-bike: warranty, insurance or repair fund', make(r) {
    const price = r.int(9, 15) * 10000, w = r.int(6, 15) * 1000, prem = r.int(8, 18) * 1000, ded = r.pick([5000, 10000, 15000]);
    return { what: `an e-bike that cost ${usd0(price / 100)}`, plans: [{ name: 'Repair fund (no plan)', prem: 0, ded: 0, covers: [] }, { name: `Warranty (${usd(w)} for the year; covers repairs, not theft)`, prem: w, ded: 0, covers: ['repair'] },
      { name: `Insurance (${usd(prem)} a year; ${usd(ded)} deductible; covers repairs and theft)`, prem, ded, covers: ['repair', 'theft'] }],
    scen: [['A quiet year: nothing goes wrong', []], [`A repair year: the motor fails (${usd(r.int(25, 45) * 1000)})`, ['repair']], [`A theft year: the bike is stolen (${usd(price)} to replace)`, ['theft']]].map(([t, ty], i) => ({ t, ev: ty.map(x => ({ type: x, cost: x === 'theft' ? price : +t.match(/\$([\d,]+)\.00/)[1].replace(/,/g, '') * 100 })) })) }; } },
  renters: { lo: 6, label: 'Renters insurance: quiet, theft and fire years', make(r) {
    const p1 = r.int(10, 16) * 1000, p2 = p1 + r.int(5, 12) * 1000, d1 = r.pick([100000, 150000]), d2 = r.pick([25000, 50000]), th = r.int(15, 40) * 10000, fire = r.int(15, 40) * 100000;
    return { what: 'an apartment renter', plans: [{ name: 'No insurance', prem: 0, ded: 0, covers: [] }, { name: `Plan A (${usd(p1)} a year; ${usd(d1)} deductible)`, prem: p1, ded: d1, covers: ['loss'] },
      { name: `Plan B (${usd(p2)} a year; ${usd(d2)} deductible)`, prem: p2, ded: d2, covers: ['loss'] }],
    scen: [{ t: 'A quiet year: no losses', ev: [] }, { t: `A theft year: a laptop and bike are stolen (${usd(th)})`, ev: [{ type: 'loss', cost: th }] }, { t: `A fire year: a kitchen fire ruins belongings (${usd(fire)})`, ev: [{ type: 'loss', cost: fire }] }] }; } },
  health: { lo: 9, label: 'Health plans: yearly cost for three kinds of years', make(r) {
    const m1 = r.int(12, 25) * 1000, m2 = m1 + r.int(8, 20) * 1000, d1 = r.pick([300000, 400000, 500000]), d2 = r.pick([50000, 100000]), c1 = r.pick([20, 30]), c2 = r.pick([10, 20]);
    const o1 = r.pick([700000, 800000]), o2 = r.pick([400000, 500000]);
    const mk = (nm, mp, d, c, o) => ({ name: `${nm} (${usd(mp)} a month; ${usd0(d / 100)} deductible; you pay ${c}% after that; ${usd0(o / 100)} out-of-pocket maximum)`, prem: mp * 12, mp, ded: d, coins: c, oop: o, health: true });
    const small = r.int(3, 8) * 5000, mid = r.int(25, 60) * 10000, big = r.int(30, 80) * 100000;
    return { what: 'a worker choosing a health plan', plans: [mk('Plan A', m1, d1, c1, o1), mk('Plan B', m2, d2, c2, o2)],
      scen: [{ t: `A healthy year: two sick visits (${usd(small)} in all)`, ev: [{ cost: small }] }, { t: `A broken arm (${usd(mid)} in bills)`, ev: [{ cost: mid }] }, { t: `A surgery and hospital stay (${usd(big)} in bills)`, ev: [{ cost: big }] }] }; } },
};
SK.insure = { area: 'risk', label: 'Insurance plans across good and bad years', lo: 6, hi: 12, count: null,
  make(v, r, g) {
    const keys = Object.keys(INS).filter(k => g >= INS[k].lo), kk = v.ins !== 'any' && keys.includes(v.ins) ? v.ins : r.pick(keys), S = INS[kk].make(r), items = [];
    const cost = S.scen.map(s => S.plans.map(p => youPay(p, s.ev)));
    S.scen.forEach((s, i) => S.plans.forEach((p, j) => items.push(I(`${s.t}: ${p.name}`, usd(cost[i][j]), 'ins', { pl: p, ev: s.ev }))));
    const best = cost.map(row => { const m = Math.min(...row); return row.filter(x => x === m).length > 1 ? null : S.plans[row.indexOf(m)].name.split(' (')[0]; });
    if (best.some(b => !b)) return null;
    S.scen.forEach((s, i) => items.push(I(`Cheapest in: ${s.t}`, best[i], 'insbest', { plans: S.plans, ev: s.ev })));
    const rules = kk === 'health' ? 'For the year, you pay the premium (monthly cost × 12), plus the bills up to the deductible, plus your percent of the rest. Your share of the bills never goes above the out-of-pocket maximum.'
      : 'For the year, you pay the plan\'s cost, plus the deductible on each covered loss (or the whole loss if it is smaller). A loss the plan does not cover, you pay in full.';
    const ex = kk === 'health' ? `Plan with ${usd0(2000)} deductible, 20% after, ${usd0(6000)} maximum, ${usd0(150)} a month: bills of ${usd0(10000)} cost you ${usd0(2000)} + 20% × ${usd0(8000)} = ${usd0(3600)}, plus ${usd0(1800)} in premiums = <b>${usd0(5400)}</b>.`
      : `A ${usd0(150)} plan with a ${usd0(500)} deductible and a ${usd0(2000)} covered loss: you pay ${usd0(150)} + ${usd0(500)} = <b>${usd0(650)}</b>; the insurer pays ${usd0(1500)}.`;
    return {
      title: INS[kk].label,
      ican: 'I can compare what insurance plans cost me in good and bad years, and choose a plan with reasons.',
      directions: `Compare the plans for ${S.what}. Find the total you pay for the year under each plan in each kind of year. ${rules}`,
      parts: [part('', example(ex)),
        part('The plans', `<ul class="fin-list">${S.plans.map(p => `<li>${esc(p.name)}</li>`).join('')}</ul>`),
        part('What you pay for the year', T(['Kind of year', ...S.plans.map(p => esc(p.name.split(' (')[0]))], S.scen.map((s, i) => [esc(s.t), ...S.plans.map((p, j) => A(usd(cost[i][j])))])) +
          T(['Kind of year', 'Cheapest plan'], S.scen.map((s, i) => [esc(s.t), A(best[i])]))),
        part('Choose', ql(1, 'No plan is cheapest every year. Which plan would you choose, and why? Think about how likely each year is and what you could afford in the worst year.', lines(3)))],
      items,
      mistakes: kk === 'health' ? 'Forgetting the premiums, which are paid even in a healthy year, and charging the percent on the whole bill instead of only the part after the deductible.' : 'Forgetting the plan\'s cost in a quiet year, and paying the deductible on a loss the plan does not cover.',
      notes: 'Plans, prices and losses are invented. Insurance trades a sure, small cost for protection from a rare, large one, so the cheapest plan in an average year is often not the safest choice.',
    };
  } };
VER.ins = p => { const pl = p.pl; if (pl.health) { const tot = p.ev.reduce((a, e) => a + e.cost, 0), share = tot <= pl.ded ? tot : pl.ded + Math.round((tot - pl.ded) * pl.coins / 100); return usd(pl.mp * 12 + (share > pl.oop ? pl.oop : share)); }
  return usd(p.ev.reduce((a, e) => a + (pl.covers.indexOf(e.type) >= 0 ? (e.cost < pl.ded ? e.cost : pl.ded) : e.cost), pl.prem)); };
VER.insbest = p => { const c = p.plans.map(pl => +VER.ins({ pl, ev: p.ev }).replace(/[$,]/g, '')); return p.plans[c.indexOf(Math.min(...c))].name.split(' (')[0]; };

const FIRMS = ['Sunbeam Snacks', 'Rocket Rides', 'Blue Lake Games', 'Green Leaf Farms', 'Bright Spark Batteries', 'Cloudy Day Umbrellas', 'Pixel Paws Pet Toys', 'Tidewater Boats', 'Golden Crust Bakery', 'Quick Fix Robots'];
SK.basket = { area: 'risk', label: 'One company or the whole basket', lo: 6, hi: 12, count: null,
  make(v, r, g) {
    const names = r.sample(FIRMS, 5), yrs = [0, 2, 4, 6, 8, 10];
    for (let t = 0; t < 100; t++) {
      const fail = r.int(0, 4), star = (fail + r.int(1, 4)) % 5, failAt = r.pick([6, 8, 10]);
      const vals = names.map((nm, i) => {
        const out = [200]; let x = 200;
        for (let k = 1; k < 6; k++) {
          if (i === fail) x = yrs[k] >= failAt ? 0 : Math.max(10, Math.round(x * (0.5 + r.next() * 0.6)));
          else if (i === star) x = Math.round(x * (1.15 + r.next() * 0.45));
          else x = Math.round(x * (0.8 + r.next() * 0.5));
          out.push(x);
        }
        return out;
      });
      const pick = r.int(0, 4), bask = yrs.map((_, k) => vals.reduce((a, row) => a + row[k], 0)), one = yrs.map((_, k) => vals[pick][k] * 5);
      if (bask[5] <= 1000 || pick === fail) { if (t < 99) continue; }
      const drop = arr => { let m = 0; for (let k = 1; k < arr.length; k++) m = Math.max(m, arr[k - 1] - arr[k]); return m; };
      const items = [];
      yrs.slice(1).forEach((y, k) => items.push(I(`Basket, year ${y}`, usd0(bask[k + 1]), 'sum0', { xs: vals.map(row => row[k + 1]) }), I(`All in ${names[pick]}, year ${y}`, usd0(one[k + 1]), 'm5', { a: vals[pick][k + 1] })));
      items.push(I('Biggest two-year drop, basket', usd0(drop(bask)), 'drop', { xs: bask }), I(`Biggest two-year drop, all in ${names[pick]}`, usd0(drop(one)), 'drop', { xs: one }),
        I(`All in ${names[fail]} after 10 years`, usd0(vals[fail][5] * 5), 'm5', { a: vals[fail][5] }), I(`All in ${names[star]} after 10 years`, usd0(vals[star][5] * 5), 'm5', { a: vals[star][5] }));
      const mx = Math.max(...bask, ...one), st = nice(mx, 5);
      const gr = grid({ x: [0, 10, 2, 'Years'], y: [0, top(mx, st), st, 'Value (dollars)', y => usd0(y)], H: 270, title: `${usd0(1000)} in a basket or in one company`,
        key: (X, Y) => redLine(yrs.map((y, k) => [y, bask[k]]), X, Y) + redLine(yrs.map((y, k) => [y, one[k]]), X, Y, true) + rtx(X(10) - 4, Y(bask[5]) - 8, 'Basket', 'font-size="12" text-anchor="end"') + rtx(X(10) - 4, Y(one[5]) + 16, names[pick].split(' ')[0], 'font-size="12" text-anchor="end"') });
      return {
        ican: 'I can compare the risk of owning one company with owning a basket of companies.',
        directions: `Two made-up investors each start with ${usd0(1000)}. One splits it into ${usd0(200)} in each of five made-up companies (a basket). The other puts all ${usd0(1000)} in ${names[pick]}. The table shows what each ${usd0(200)} share of the basket is worth every two years.`,
        parts: [part(`What ${usd0(200)} in each company is worth`, T(['Company', ...yrs.map(y => `Year ${y}`)], vals.map((row, i) => [names[i], ...row.map(usd0)])
          .concat([['<b>Basket total</b>', usd0(1000), ...bask.slice(1).map(x => A(usd0(x)))], [`<b>All ${usd0(1000)} in ${names[pick]}</b> (5 × its row)`, usd0(1000), ...one.slice(1).map(x => A(usd0(x)))]]), 'fin-small')),
          part('Graph both investors', gr),
          part('Questions', ql(1, 'What was the biggest drop from one checkup to the next for each investor?', aline('Basket', usd0(drop(bask))) + aline(`All in ${names[pick]}`, usd0(drop(one)))) +
            ql(2, `What would ${usd0(1000)} all in ${names[fail]} be worth after 10 years? All in ${names[star]}?`, aline(names[fail], usd0(vals[fail][5] * 5)) + aline(names[star], usd0(vals[star][5] * 5))) +
            ql(3, 'Which choice is riskier, and why? What does a basket give up, and what does it protect against?', lines(2)))],
        items,
        mistakes: 'Adding the five company values for the one-company investor (that investor owns five times one row), and judging risk by the final value alone instead of the ups and downs.',
        notes: 'Companies and values are invented: one company always fails and one grows fast, so the basket is never the best or the worst. That is the point of diversifying.',
        materials: 'pencil, calculator, ruler, two colored pencils',
      };
    }
    return null;
  } };
VER.m5 = p => usd0(p.a * 5);
VER.drop = p => { let m = 0; p.xs.forEach((x, k) => { if (k && p.xs[k - 1] - x > m) m = p.xs[k - 1] - x; }); return usd0(m); };

SK.pctchg = { area: 'risk', label: 'Share prices and percent change', lo: 7, hi: 12, count: [5, 6, 8],
  make(v, r, g, n) {
    const names = r.sample(FIRMS, n), mo = r.int(0, 6), months = MONTHS.slice(mo, mo + 6), items = [];
    const rows = names.map(nm => { const out = [r.int(800, 9000)]; for (let k = 1; k < 6; k++) out.push(Math.max(100, Math.round(out[k - 1] * (0.82 + r.next() * 0.36)))); return out; });
    const ch = rows.map(x => (x[5] - x[0]) / x[0] * 100);
    if (ch.some(c => edgy(c * 10) || Math.abs(c) < 0.05)) return null;
    const best = ch.indexOf(Math.max(...ch)), worst = ch.indexOf(Math.min(...ch));
    if (ch[worst] >= 0 || ch[best] <= 0) return null;
    names.forEach((nm, i) => items.push(I(`${nm}: percent change`, `${ch[i] > 0 ? '+' : '−'}${fix(Math.abs(ch[i]), 1)}%`, 'chg', { a: rows[i][0], b: rows[i][5] })));
    const k = r.int(0, n - 1), sh = r.int(1, 10) * 10, gl = (rows[k][5] - rows[k][0]) * sh;
    items.push(I('Biggest gain', names[best], 'name', { t: names[best] }), I('Biggest loss', names[worst], 'name', { t: names[worst] }), I(`${sh} shares of ${names[k]}`, gl > 0 ? `Gain of ${usd(gl)}` : `Loss of ${usd(-gl)}`, 'gl', { a: rows[k][5] * sh, b: rows[k][0] * sh }));
    return {
      ican: 'I can read a table of share prices and find the percent change.',
      directions: `The table shows the made-up share prices of made-up companies at the start of each month. Percent change = (${months[5]} price − ${months[0]} price) ÷ ${months[0]} price × 100. Round to the nearest tenth of a percent and write + for a gain or − for a loss.`,
      parts: [part('', example(`${usd(4000)} to ${usd(4500)}: (${usd(4500)} − ${usd(4000)}) ÷ ${usd(4000)} = 0.125, so <b>+12.5%</b>.`)),
        part('Share prices', T(['Company', ...months, 'Percent change'], names.map((nm, i) => [nm, ...rows[i].map(usd), A(items[i].a)]), 'fin-small')),
        part('Questions', ql(1, 'Which company had the biggest percent gain? The biggest loss?', aline('Gain', names[best], 10) + aline('Loss', names[worst], 10)) +
          ql(2, `${r.pick(NAMES)} bought ${sh} shares of ${names[k]} in ${months[0]} and sold them in ${months[5]}. What was the gain or loss?`, aline('Answer', items[items.length - 1].a, 10)) +
          ql(3, 'Does the company with the biggest price change in dollars also have the biggest percent change? Why not?', lines(2)))],
      items,
      mistakes: 'Dividing by the ending price instead of the starting price, and comparing dollar changes instead of percent changes when the prices are very different.',
      notes: 'Companies and prices are invented. Percent change lets you compare a $10 share with a $90 share fairly.',
    };
  } };
VER.chg = p => { const c = (p.b - p.a) / p.a * 100; return `${c > 0 ? '+' : '−'}${(Math.round(Math.abs(c) * 10) / 10).toFixed(1)}%`; };

const DEP = [['e-bike', 120000, 250000], ['used car', 800000, 1800000], ['laptop', 80000, 180000], ['phone', 50000, 120000], ['riding lawn mower', 150000, 300000]];
SK.deprec = { area: 'risk', label: 'Depreciation: value over five years', lo: 8, hi: 12, count: null,
  make(v, r) {
    const D = r.pick(DEP), name = r.pick(NAMES);
    for (let t = 0; t < 100; t++) {
      const P = r.int(D[1] / 5000, D[2] / 5000) * 5000, rt = r.pick([15, 20, 25, 30]), rows = []; let b = P, bad = false;
      for (let y = 1; y <= 5; y++) { const d = Math.round(b * rt / 100); if (edgy(b * rt / 100)) bad = true; rows.push({ y, s: b, d, e: b - d }); b -= d; }
      if (bad) continue;
      const items = [];
      rows.forEach(x => items.push(I(`Year ${x.y}: depreciation`, usd(x.d), 'dpd', { P, rt, y: x.y }), I(`Year ${x.y}: value at the end`, usd(x.e), 'dpe', { P, rt, y: x.y })));
      items.push(I('Total value lost in 5 years', usd(P - b), 'dplost', { P, rt }));
      const st = nice(P / 100, 5);
      const gr = grid({ x: [0, 5, 1, 'Years'], y: [0, top(P / 100, st), st, 'Value (dollars)', y => usd0(y)], H: 270, title: `Value of the ${D[0]}`, key: (X, Y) => redLine([[0, P / 100], ...rows.map(x => [x.y, x.e / 100])], X, Y) });
      return {
        ican: 'I can find how an item loses value each year and graph its value.',
        directions: `${name} buys a ${D[0]} for ${usd(P)}. It loses ${rt}% of its value each year (${rt}% of what it was worth at the start of that year). Round each year's loss to the nearest cent.`,
        parts: [part('', example(`Worth ${usd(100000)} at the start of a year, losing 20%: 0.20 × ${usd(100000)} = ${usd(20000)}, so it ends the year at <b>${usd(80000)}</b>.`)),
          part('The table', T(['Year', 'Value at the start', `Loss (${rt}%)`, 'Value at the end'], rows.map(x => [x.y, x.y === 1 ? usd(x.s) : A(usd(x.s)), A(usd(x.d)), A(usd(x.e))]))),
          part('The graph', gr),
          part('Questions', ql(1, 'How much value did it lose in all after 5 years?', aline('Answer', usd(P - b))) + ql(2, 'Why does the loss get smaller each year even though the rate stays the same? Why is the graph a curve, not a line?', lines(2)))],
        items,
        mistakes: `Taking ${rt}% of the original price every year (that is straight-line depreciation, a different method), and subtracting the percent itself instead of the dollar loss.`,
        notes: `Each year's value is ${100 - rt}% of the year before, so after 5 years it is worth about ${fmt((1 - rt / 100) ** 5 * 100, 0)}% of the price. Real items lose value at different rates; this one is invented.`,
        materials: 'pencil, calculator, ruler',
      };
    }
    return null;
  } };
const dpRun = (P, rt, y) => { let b = P, d = 0; for (let k = 1; k <= y; k++) { d = Math.round(b * rt / 100); b -= d; } return { d, b }; };
VER.dpd = p => usd(dpRun(p.P, p.rt, p.y).d);
VER.dpe = p => { const b = dpRun(p.P, p.rt, p.y).b, c = p.P * (1 - p.rt / 100) ** p.y; return Math.abs(b - c) <= p.y ? usd(b) : 'closed form disagrees'; };
VER.dplost = p => usd(p.P - dpRun(p.P, p.rt, 5).b);

// total cost of ownership: options with an upfront price and yearly costs (all whole dollars)
const OWN = {
  commute: { label: 'E-bike, bus pass or used car?', what: 'getting to work for five years', opts: r => [
    { n: 'E-bike', up: r.int(10, 18) * 100, yr: [['charging', r.int(3, 6) * 10], ['repairs', r.int(8, 20) * 10]] },
    { n: 'Bus pass', up: 0, yr: [['pass (12 months)', r.int(40, 75) * 12]] },
    { n: 'Used car', up: r.int(50, 90) * 100, yr: [['fuel', r.int(9, 18) * 100], ['insurance', r.int(8, 16) * 100], ['repairs', r.int(3, 8) * 100]] }] },
  lights: { label: 'LED or tungsten stage lights?', what: 'a school theater\'s lighting rig', opts: r => [
    { n: 'LED rig', up: r.int(40, 80) * 100, yr: [['electricity', r.int(15, 40) * 10], ['parts', r.int(0, 5) * 10]] },
    { n: 'Tungsten rig', up: r.int(15, 30) * 100, yr: [['electricity', r.int(90, 160) * 10], ['lamp replacements', r.int(20, 50) * 10]] }] },
  printer: { label: 'Cheap printer or cheap ink?', what: 'a home office printer', opts: r => [
    { n: 'Budget printer', up: r.int(5, 9) * 10, yr: [['ink', r.int(15, 25) * 10]] },
    { n: 'Tank printer', up: r.int(25, 40) * 10, yr: [['ink', r.int(2, 6) * 10]] }] },
};
SK.own = { area: 'risk', label: 'Total cost of ownership over five years', lo: 6, hi: 12, count: null,
  make(v, r) {
    const key = OWN[v.own] ? v.own : r.pick(Object.keys(OWN)), O = OWN[key];
    for (let t = 0; t < 100; t++) {
      const opts = O.opts(r).map(o => ({ ...o, y: o.yr.reduce((a, b) => a + b[1], 0) }));
      const cum = opts.map(o => [1, 2, 3, 4, 5].map(y => o.up + o.y * y));
      const cheap = y => { const c = cum.map(x => x[y - 1]), m = Math.min(...c); return c.filter(x => x === m).length > 1 ? null : opts[c.indexOf(m)].n; };
      if (!cheap(1) || !cheap(5) || cheap(1) === cheap(5) && key !== 'commute') continue;
      const items = [];
      opts.forEach((o, i) => { items.push(I(`${o.n}: cost each year`, usd0(o.y), 'sum0', { xs: o.yr.map(x => x[1]) })); cum[i].forEach((c, y) => items.push(I(`${o.n}: total after year ${y + 1}`, usd0(c), 'own', { up: o.up, ys: o.yr.map(x => x[1]), y: y + 1 }))); });
      items.push(I('Cheapest after 1 year', cheap(1), 'name', { t: cheap(1) }), I('Cheapest after 5 years', cheap(5), 'name', { t: cheap(5) }));
      const mx = Math.max(...cum.flat()), st = nice(mx, 5);
      const gr = grid({ x: [0, 5, 1, 'Years'], y: [0, top(mx, st), st, 'Total spent (dollars)', y => usd0(y)], H: 270, title: 'Total cost over time',
        key: (X, Y) => opts.map((o, i) => redLine([[0, o.up], ...cum[i].map((c, y) => [y + 1, c])], X, Y, i === 1) + rtx(X(5) - 4, Y(cum[i][4]) - 7, o.n, 'font-size="11.5" text-anchor="end"')).join('') });
      return {
        title: O.label,
        ican: 'I can add the price and the yearly costs to find the total cost of owning something over time.',
        directions: `Compare the options for ${O.what}. First add each option's yearly costs. Then find the total spent after each year: price + yearly cost × years.`,
        parts: [part('The options', T(['Option', 'Price up front', 'Yearly costs', 'Cost each year'], opts.map(o => [o.n, usd0(o.up), o.yr.map(([l, c]) => `${l} ${usd0(c)}`).join(', '), A(usd0(o.y))]))),
          part('Total spent', T(['Option', 'After 1 year', '2 years', '3 years', '4 years', '5 years'], opts.map((o, i) => [o.n, ...cum[i].map(c => A(usd0(c)))]))),
          part('The graph', gr),
          part('Questions', ql(1, 'Which option is cheapest after 1 year? After 5 years?', aline('1 year', cheap(1), 9) + aline('5 years', cheap(5), 9)) +
            ql(2, 'Why can the option with the higher price up front end up cheaper? What else, besides cost, would you think about?', lines(2)))],
        items,
        mistakes: 'Comparing only the price up front, and adding the yearly cost once instead of once for every year.',
        notes: 'All prices are invented. The lines start at the price up front and rise by the yearly cost each year, so the steeper line costs more to keep.',
        materials: 'pencil, calculator, ruler',
      };
    }
    return null;
  } };
VER.own = p => usd0(p.up + p.ys.reduce((a, b) => a + b * p.y, 0));

SK.margin = { area: 'risk', label: 'Buying stock on margin (1929)', lo: 9, hi: 12, count: [3, 4, 5],
  make(v, r, g, n) {
    const who = r.sample(NAMES, n), items = [];
    const rows = who.map((nm, i) => {
      const sh = r.int(1, 10) * 100, buy = r.int(40, 200) * 100, up = i % 2 === 0, sell = up ? buy + r.int(5, 40) * buy / 100 : Math.round(buy * r.int(30, 80) / 100);
      const cost = sh * buy, own = cost / 10, loan = cost - own, gl = sh * (sell - buy), pct = gl / own * 100;
      const when = up ? 'sells in summer 1929' : 'sells after the October 1929 crash';
      items.push(I(`${nm}: own money`, usd(own), 'own10', { sh, buy }), I(`${nm}: borrowed`, usd(loan), 'loan90', { sh, buy }), I(`${nm}: gain or loss`, gl > 0 ? `Gain of ${usd(gl)}` : `Loss of ${usd(-gl)}`, 'mgl', { sh, buy, sell }),
        I(`${nm}: percent of own money`, `${gl > 0 ? '+' : '−'}${fmt(Math.abs(Math.round(pct)), 0)}%`, 'mpct', { sh, buy, sell }));
      return [`${nm} (${when})`, fmt(sh, 0), usd(buy), usd(sell), A(usd(own)), A(usd(loan)), A(gl > 0 ? `Gain of ${usd(gl)}` : `Loss of ${usd(-gl)}`), A(items[items.length - 1].a)];
    });
    return {
      ican: 'I can work out how buying on margin multiplied gains and losses before and after the 1929 crash.',
      directions: 'Each investor buys on 10% margin: pays 10% of the cost with their own money and borrows the other 90% from a broker. When they sell, they repay the loan. Find each gain or loss and what it is as a percent of the investor\'s own money (nearest whole percent).',
      parts: [part('', example(`100 shares at ${usd(5000)} cost ${usd(500000)}: own money ${usd(50000)}, borrowed ${usd(450000)}. Sold at ${usd(4000)}: loss 100 × ${usd(1000)} = ${usd(100000)}.`, `That is ${usd(100000)} ÷ ${usd(50000)} = 200% of the investor's own money: they lose it all and still owe ${usd(50000)}.`)),
        part('The investors', T(['Investor', 'Shares', 'Buy price', 'Sell price', 'Own money (10%)', 'Borrowed (90%)', 'Gain or loss', 'Percent of own money'], rows, 'fin-small')),
        part('Questions', ql(1, 'A loss of more than 100% of your own money: what does that mean for the investor? What did brokers do when prices fell (a margin call)?', lines(2)) +
          ql(2, 'How did buying on margin help turn falling prices into a crash?', lines(2)))],
      items,
      mistakes: 'Finding the percent of the whole cost instead of the investor\'s own money, which hides how margin multiplies the result ten times.',
      notes: 'Prices and investors are invented. In the late 1920s many buyers used margin, some putting down as little as 10%. When prices fell, brokers made margin calls, and forced selling pushed prices down further.',
    };
  } };
VER.own10 = p => usd(p.sh * p.buy * 0.1);
VER.loan90 = p => usd(p.sh * p.buy * 0.9);
VER.mgl = p => { const v1 = p.sh * p.sell - p.sh * p.buy; return v1 > 0 ? `Gain of ${usd(v1)}` : `Loss of ${usd(-v1)}`; };
VER.mpct = p => { const x = (p.sell - p.buy) / (p.buy * 0.1) * 100; return `${x > 0 ? '+' : '−'}${fmt(Math.round(Math.abs(x)), 0)}%`; };

/* ===== Economics ===== */
const MARKETS = [
  { good: 'ski rentals', q: 'rentals a day', price: 'Price per day', p0: [15, 20, 25], st: [5], qs: [10, 20] },
  { good: 'cups of coffee', q: 'cups a day', price: 'Price per cup', p0: [1, 2], st: [1], qs: [20, 50] },
  { good: 'concert tickets', q: 'tickets', price: 'Price per ticket', p0: [20, 30], st: [10], qs: [50, 100] },
  { good: 'lift tickets', q: 'tickets a day', price: 'Price per ticket', p0: [40, 50], st: [10], qs: [50, 100] },
  { good: 'slices of pizza', q: 'slices a day', price: 'Price per slice', p0: [1, 2], st: [1], qs: [20, 50] },
  { good: 'bike rentals', q: 'rentals a day', price: 'Price per day', p0: [8, 10], st: [2], qs: [5, 10] },
  { good: 'bags of coffee beans', q: 'bags a week', price: 'Price per bag', p0: [6, 8], st: [2], qs: [10, 20] }];
const LABOR = [
  { good: 'ski instructors', q: 'instructors', price: 'Wage per hour', p0: [12, 14], st: [2], qs: [5, 10], labor: true },
  { good: 'lifeguards', q: 'lifeguards', price: 'Wage per hour', p0: [11, 12], st: [1], qs: [2, 5], labor: true },
  { good: 'farm workers', q: 'workers', price: 'Wage per hour', p0: [12, 14], st: [2], qs: [10, 20], labor: true }];
// a schedule of 6 prices with linear demand and supply crossing at index e (2 or 3)
function schedule(r, M) {
  for (let t = 0; t < 200; t++) {
    const p0 = r.pick(M.p0), st = r.pick(M.st), qs = r.pick(M.qs), e = r.int(2, 3), b = r.int(1, 4), d = r.int(1, 4), Qe = r.int(6, 12);
    const a = Qe + b * e, c = Qe - d * e;
    if (c < 1 || a - 5 * b < 1) continue;
    const P = [0, 1, 2, 3, 4, 5].map(k => p0 + k * st);
    return { M, P, D: P.map((_, k) => (a - b * k) * qs), S: P.map((_, k) => (c + d * k) * qs), e, st };
  }
}
function sdGraph(s, which, extra, W = 520, H = 290) {
  const qmax = Math.max(...s.D, ...s.S), qst = nice(qmax, 6), pst = s.st, pmax = s.P[5] + pst;
  const pts = arr => s.P.map((p, k) => [arr[k], p]);
  return grid({ x: [0, top(qmax, qst), qst, `Quantity (${s.M.q})`, x => fmt(x, 0)], y: [0, pmax, pst, `${s.M.price} ($)`, y => usd0(y)], W, H, small: true, title: s.M.labor ? `The market for ${s.M.good}` : `The market for ${s.M.good}`,
    key: (X, Y) => (which.includes('D') ? redLine(pts(s.D), X, Y) + rtx(X(s.D[5]) + 6, Y(s.P[5]) + 4, s.M.labor ? 'D (employers)' : 'D', 'font-size="12"') : '') +
      (which.includes('S') ? redLine(pts(s.S), X, Y, true) + rtx(X(s.S[5]) + 6, Y(s.P[5]) + 4, s.M.labor ? 'S (workers)' : 'S', 'font-size="12"') : '') +
      (which.includes('E') ? `<circle cx="${X(s.D[s.e])}" cy="${Y(s.P[s.e])}" r="6" fill="none" stroke="${RED}" stroke-width="2.4"/>` + rtx(X(s.D[s.e]) - 10, Y(s.P[s.e]) - 9, 'E', 'font-size="13" text-anchor="end"') : '') + (extra ? extra(X, Y) : '') });
}
const schedTable = (s, which) => T([`${s.M.price}`, ...s.P.map(p => usd0(p))], [...(which.includes('D') ? [[s.M.labor ? 'Workers wanted by employers' : 'Quantity demanded', ...s.D.map(x => fmt(x, 0))]] : []),
  ...(which.includes('S') ? [[s.M.labor ? 'Workers willing to work' : 'Quantity supplied', ...s.S.map(x => fmt(x, 0))]] : [])], 'fin-small');
const mkt = (v, r) => r.pick(v.market === 'labor' ? LABOR : MARKETS);
SK.demand = { area: 'econ', label: 'A demand schedule and curve', lo: 6, hi: 12, count: null,
  make(v, r) {
    const s = schedule(r, mkt(v, r)), [i, j] = r.sample([0, 1, 2, 3, 4, 5], 2).sort((a, b) => a - b), k = r.int(0, 5), L = s.M.labor;
    const items = [I(`Quantity at ${usd0(s.P[k])}`, fmt(s.D[k], 0), 'read', { xs: s.D, k }), I(`Change from ${usd0(s.P[i])} to ${usd0(s.P[j])}`, `falls by ${fmt(s.D[i] - s.D[j], 0)}`, 'fall', { xs: s.D, i, j }),
      I('Law of demand', L ? 'As the wage rises, employers want to hire fewer workers.' : 'As the price rises, the quantity demanded falls.', 'name', { t: L ? 'As the wage rises, employers want to hire fewer workers.' : 'As the price rises, the quantity demanded falls.' })];
    return {
      title: `${L ? 'Labor demand' : 'Demand'}: ${s.M.good}`,
      ican: 'I can graph a demand schedule and describe what happens to quantity demanded as the price rises.',
      directions: `The table is a made-up demand schedule for ${s.M.good}. Plot each pair (quantity, price) and connect the points to draw the demand curve. Label it D.`,
      parts: [part('The demand schedule', schedTable(s, 'D')), part('Graph it', sdGraph(s, 'D')),
        part('Questions', ql(1, `At ${usd0(s.P[k])}, how many ${s.M.q.split(' ')[0]} are ${L ? 'wanted' : 'demanded'}?`, aline('Answer', items[0].a)) +
          ql(2, `When the ${L ? 'wage' : 'price'} rises from ${usd0(s.P[i])} to ${usd0(s.P[j])}, what happens to the quantity ${L ? 'wanted' : 'demanded'}?`, aline('Answer', items[1].a, 9)) +
          ql(3, 'Describe the pattern in one sentence. Why do you think it happens?', lines(2) + h.keyline(esc(items[2].a))))],
      items,
      mistakes: 'Putting price on the horizontal axis (economists put price on the vertical axis), and saying "demand falls" when only the quantity demanded changes along the same curve.',
      notes: 'The numbers are invented and fall evenly, so the demand curve is a straight line. Each point is one row of the schedule.',
      materials: 'pencil, ruler',
    };
  } };
VER.read = p => fmt(p.xs[p.k], 0);
VER.fall = p => `falls by ${fmt(p.xs[p.i] - p.xs[p.j], 0)}`;
VER.rise = p => `rises by ${fmt(p.xs[p.j] - p.xs[p.i], 0)}`;
SK.supply = { area: 'econ', label: 'A supply schedule and curve', lo: 6, hi: 12, count: null,
  make(v, r) {
    const s = schedule(r, mkt(v, r)), [i, j] = r.sample([0, 1, 2, 3, 4, 5], 2).sort((a, b) => a - b), k = r.int(0, 5), L = s.M.labor;
    const why = L ? 'As the wage rises, more people are willing to work.' : 'As the price rises, sellers offer more, because each sale earns more.';
    const items = [I(`Quantity supplied at ${usd0(s.P[k])}`, fmt(s.S[k], 0), 'read', { xs: s.S, k }), I(`Supply change from ${usd0(s.P[i])} to ${usd0(s.P[j])}`, `rises by ${fmt(s.S[j] - s.S[i], 0)}`, 'rise', { xs: s.S, i, j }), I('Law of supply', why, 'name', { t: why })];
    return {
      title: `${L ? 'Labor supply' : 'Supply'}: ${s.M.good}`,
      ican: 'I can graph a supply schedule and explain why sellers offer more at higher prices.',
      directions: `The table is a made-up supply schedule for ${s.M.good}. Plot each pair (quantity, price) and connect the points to draw the supply curve. Label it S.`,
      parts: [part('The supply schedule', schedTable(s, 'S')), part('Graph it', sdGraph(s, 'S')),
        part('Questions', ql(1, `At ${usd0(s.P[k])}, how many are ${L ? 'willing to work' : 'supplied'}?`, aline('Answer', items[0].a)) +
          ql(2, `When the ${L ? 'wage' : 'price'} rises from ${usd0(s.P[i])} to ${usd0(s.P[j])}, what happens to the quantity ${L ? 'of workers' : 'supplied'}?`, aline('Answer', items[1].a, 9)) +
          ql(3, L ? 'Why are more people willing to work at a higher wage?' : 'Why do shops offer more at higher prices?', lines(2) + h.keyline(esc(why))))],
      items,
      mistakes: 'Drawing the supply curve sloping down like demand. Supply slopes up: a higher price brings more to the market.',
      notes: 'The numbers are invented and rise evenly, so the supply curve is a straight line.',
      materials: 'pencil, ruler',
    };
  } };
SK.sd = { area: 'econ', label: 'Equilibrium, shortage and surplus', lo: 6, hi: 12, count: null,
  make(v, r) {
    const s = schedule(r, mkt(v, r)), L = s.M.labor, lo = r.int(0, s.e - 1), hi = r.int(s.e + 1, 5);
    const sh = s.D[lo] - s.S[lo], su = s.S[hi] - s.D[hi], w = L ? 'wage' : 'price';
    const items = [I('Equilibrium ' + w, usd0(s.P[s.e]), 'eqp', s), I('Equilibrium quantity', fmt(s.D[s.e], 0), 'eqq', s),
      I(`At ${usd0(s.P[lo])}`, `shortage of ${fmt(sh, 0)}`, 'gap', { s, k: lo }), I(`At ${usd0(s.P[hi])}`, `surplus of ${fmt(su, 0)}`, 'gap', { s, k: hi }),
      I(`Which way the ${w} moves from ${usd0(s.P[lo])}`, 'up', 'dir', { s, k: lo })];
    const shades = (X, Y) => `<line x1="${X(s.S[lo])}" y1="${Y(s.P[lo])}" x2="${X(s.D[lo])}" y2="${Y(s.P[lo])}" stroke="${RED}" stroke-width="5" opacity="0.5"/>` + rtx((X(s.S[lo]) + X(s.D[lo])) / 2, Y(s.P[lo]) + 16, 'shortage', 'font-size="11" text-anchor="middle"') +
      `<line x1="${X(s.D[hi])}" y1="${Y(s.P[hi])}" x2="${X(s.S[hi])}" y2="${Y(s.P[hi])}" stroke="${RED}" stroke-width="5" opacity="0.5"/>` + rtx((X(s.S[hi]) + X(s.D[hi])) / 2, Y(s.P[hi]) - 8, 'surplus', 'font-size="11" text-anchor="middle"');
    return {
      title: `${L ? 'The labor market' : 'Supply and demand'}: ${s.M.good}`,
      ican: 'I can find the equilibrium on a supply and demand graph and measure a shortage or surplus.',
      directions: 'Plot the demand and the supply schedules on the same graph and label the curves D and S. Mark the equilibrium E, where they cross. Then answer the questions.',
      parts: [part('The schedules', schedTable(s, 'DS')), part('Graph both', sdGraph(s, 'DSE', shades)),
        part('Questions', ql(1, `What are the equilibrium ${w} and quantity?`, aline(L ? 'Wage' : 'Price', usd0(s.P[s.e])) + aline('Quantity', fmt(s.D[s.e], 0))) +
          ql(2, `At a ${w} of ${usd0(s.P[lo])}, is there a shortage or a surplus, and how big is it?`, aline('Answer', items[2].a, 9)) +
          ql(3, `At a ${w} of ${usd0(s.P[hi])}, is there a shortage or a surplus, and how big is it?`, aline('Answer', items[3].a, 9)) +
          ql(4, `If the ${w} starts at ${usd0(s.P[lo])}, will it tend to move up or down? Explain what ${L ? 'employers' : 'buyers and sellers'} do.`, aline('Direction', 'up', 4) + lines(1)))],
      items,
      mistakes: 'Calling a low price a surplus. Below equilibrium, buyers want more than sellers offer, so there is a shortage.',
      notes: `The schedules are invented; the curves cross at a ${w} in the table, so the equilibrium can be read exactly. A shortage pushes the ${w} up and a surplus pushes it down, toward E.`,
      materials: 'pencil, ruler, two colored pencils',
    };
  } };
VER.eqp = p => usd0(p.P[p.D.findIndex((d, k) => d === p.S[k])]);
VER.eqq = p => fmt(p.D.find((d, k) => d === p.S[k]), 0);
VER.gap = p => { const d = p.s.D[p.k] - p.s.S[p.k]; return d > 0 ? `shortage of ${fmt(d, 0)}` : `surplus of ${fmt(-d, 0)}`; };
VER.dir = p => p.s.D[p.k] > p.s.S[p.k] ? 'up' : 'down';
SK.ceiling = { area: 'econ', label: 'Price ceilings and price floors', lo: 8, hi: 12, count: null,
  make(v, r) {
    const A1 = schedule(r, r.pick(MARKETS)), B1 = schedule(r, r.pick(LABOR)), cl = r.int(0, A1.e - 1), fl = r.int(B1.e + 1, 5), items = [];
    const ln = (s, k) => (X, Y) => `<line x1="${X(0)}" y1="${Y(s.P[k])}" x2="${X(Math.max(...s.D, ...s.S))}" y2="${Y(s.P[k])}" stroke="${RED}" stroke-width="2" stroke-dasharray="3 3"/>` +
      rtx(X(Math.max(...s.D, ...s.S)) - 4, Y(s.P[k]) - 6, s === A1 ? 'ceiling' : 'floor', 'font-size="11" text-anchor="end"');
    items.push(I(`${A1.M.good}: equilibrium price`, usd0(A1.P[A1.e]), 'eqp', A1), I(`${A1.M.good}: at the ceiling`, `shortage of ${fmt(A1.D[cl] - A1.S[cl], 0)}`, 'gap', { s: A1, k: cl }),
      I(`${B1.M.good}: equilibrium wage`, usd0(B1.P[B1.e]), 'eqp', B1), I(`${B1.M.good}: at the floor`, `surplus of ${fmt(B1.S[fl] - B1.D[fl], 0)}`, 'gap', { s: B1, k: fl }));
    return {
      ican: 'I can show a price ceiling and a price floor on a graph and find the shortage or surplus each causes.',
      directions: 'For each market, plot both schedules, label D and S, and mark the equilibrium. Then draw the price control as a straight dashed line across the graph and measure the gap between the curves at that price.',
      parts: [part(`A price ceiling on ${A1.M.good}: ${usd0(A1.P[cl])}`, `<p>A town says ${A1.M.good} may not cost more than ${usd0(A1.P[cl])}.</p>` + schedTable(A1, 'DS') + sdGraph(A1, 'DSE', ln(A1, cl), 500, 260) +
        ql(1, 'What is the equilibrium price? At the ceiling, is there a shortage or a surplus, and how big?', aline('Equilibrium', usd0(A1.P[A1.e])) + aline('At the ceiling', items[1].a, 9))),
        part(`A wage floor for ${B1.M.good}: ${usd0(B1.P[fl])} an hour`, `<p>A law says ${B1.M.good} must be paid at least ${usd0(B1.P[fl])} an hour.</p>` + schedTable(B1, 'DS') + sdGraph(B1, 'DSE', ln(B1, fl), 500, 260) +
          ql(2, 'What is the equilibrium wage? At the floor, is there a shortage or a surplus of workers, and how big?', aline('Equilibrium', usd0(B1.P[B1.e])) + aline('At the floor', items[3].a, 9)) +
          ql(3, 'A ceiling set above the equilibrium price, or a floor set below it, changes nothing. Why?', lines(2)))],
      items,
      mistakes: 'Thinking a ceiling must sit above the equilibrium on the graph. A ceiling that matters is below equilibrium (a shortage); a floor that matters is above it (a surplus).',
      notes: 'Both markets are invented. Real price controls, such as rent control and minimum wage laws, are debated: economists weigh the shortage or surplus against who is helped.',
      materials: 'pencil, ruler, two colored pencils',
    };
  } };

// events: [text with {G}, {IN}, {SUB}, {COMP}, curve D or S or slideD or slideS, direction +1/-1, determinant]
const EVENTS = [
  ['Incomes in the town rise, and {G} are a normal good.', 'D', 1, 'income'], ['Incomes in the town fall, and {G} are a normal good.', 'D', -1, 'income'],
  ['A popular video makes {G} the thing everyone wants.', 'D', 1, 'tastes'], ['People get tired of {G} and want them less.', 'D', -1, 'tastes'],
  ['The price of {SUB}, a substitute, goes up.', 'D', 1, 'price of a related good'], ['The price of {SUB}, a substitute, goes down.', 'D', -1, 'price of a related good'],
  ['The price of {COMP}, which people use with {G}, goes up.', 'D', -1, 'price of a related good'], ['The price of {COMP}, which people use with {G}, goes down.', 'D', 1, 'price of a related good'],
  ['Many new families move to town.', 'D', 1, 'number of buyers'], ['Buyers expect the price of {G} to jump next month, so they buy now.', 'D', 1, 'expectations'],
  ['The price of {IN} rises.', 'S', -1, 'input costs'], ['The price of {IN} falls.', 'S', 1, 'input costs'],
  ['A new machine lets sellers make {G} faster and cheaper.', 'S', 1, 'technology'], ['Several new sellers of {G} open in town.', 'S', 1, 'number of sellers'],
  ['Some sellers of {G} close for good.', 'S', -1, 'number of sellers'], ['The government adds a tax on every sale of {G}.', 'S', -1, 'taxes and subsidies'],
  ['The government pays sellers a subsidy for each of {G} they make.', 'S', 1, 'taxes and subsidies'],
  ['The price of {G} rises, so buyers buy fewer of them.', 'slideD', -1, ''], ['The price of {G} falls, so buyers buy more of them.', 'slideD', 1, ''],
  ['The price of {G} rises, so sellers offer more of them.', 'slideS', 1, '']];
const GOODS = [{ G: 'pizzas', IN: 'cheese', SUB: 'tacos', COMP: 'soda' }, { G: 'bikes', IN: 'steel', SUB: 'scooters', COMP: 'bike helmets' }, { G: 'hot dogs', IN: 'meat', SUB: 'hamburgers', COMP: 'hot dog buns' },
  { G: 'ski rentals', IN: 'new skis', SUB: 'snowboard rentals', COMP: 'lift tickets' }, { G: 'cups of coffee', IN: 'coffee beans', SUB: 'cups of tea', COMP: 'muffins' }, { G: 'video game consoles', IN: 'computer chips', SUB: 'gaming computers', COMP: 'video games' }];
const fillEv = (t, G) => t.replace(/\{(\w+)\}/g, (m, k) => G[k]).replace('each of pizzas', 'each pizza').replace(/each of (\w[\w ]*)/, 'each one');
const evAnswer = e => e[1] === 'slideD' ? ['Slide', 'along demand', e[2] > 0 ? 'quantity demanded rises' : 'quantity demanded falls', '(a change in its own price)']
  : e[1] === 'slideS' ? ['Slide', 'along supply', e[2] > 0 ? 'quantity supplied rises' : 'quantity supplied falls', '(a change in its own price)'] : ['Shift', e[1] === 'D' ? 'demand' : 'supply', e[2] > 0 ? 'right (increase)' : 'left (decrease)', e[3]];
SK.shift = { area: 'econ', label: 'Shift or slide? Changes in supply and demand', lo: 8, hi: 12, count: [6, 8, 10],
  make(v, r, g, n) {
    const G = r.pick(GOODS), evs = r.sample(EVENTS, n), items = [];
    if (evs.filter(e => e[1].startsWith('slide')).length < 1 || evs.filter(e => e[1] === 'S').length < 2 || evs.filter(e => e[1] === 'D').length < 2) return null;
    const rows = evs.map((e, i) => { const t = fillEv(e[0], G), a = evAnswer(e);
      items.push(I(`${t} Shift or slide`, a[0], 'ev0', { e }), I(`${t} Curve`, a[1], 'ev1', { e }), I(`${t} Direction`, a[2], 'ev2', { e }), I(`${t} Determinant`, a[3], 'ev3', { e }));
      return [`${i + 1}. ${esc(t)}`, A(a[0]), A(a[1]), A(a[2]), A(a[3])]; });
    return {
      title: `Shift or slide? The market for ${G.G}`,
      ican: 'I can tell a movement along a curve from a shift of the curve, and name what shifted it.',
      directions: `Each event happens in the market for ${G.G}. A change in the price of ${G.G} itself is a slide along a curve. Anything else that changes buying or selling plans shifts a whole curve. For a shift, give the curve, the direction and the determinant from the box.`,
      parts: [part('', box('<p><b>Demand shifters:</b> income, tastes, price of a related good (substitute or complement), number of buyers, expectations. <b>Supply shifters:</b> input costs, technology, number of sellers, taxes and subsidies, expectations.</p>')),
        part('Events', T(['Event', 'Shift or slide?', 'Which curve?', 'Direction', 'Determinant'], rows, 'fin-small'))],
      items,
      mistakes: 'Saying a change in the good\'s own price shifts demand. It only moves buyers along the curve. And mixing up substitutes (used instead of) and complements (used together).',
      notes: 'Every event changes one thing, all else held the same. "Normal good" means people buy more when their income rises.',
    };
  } };
VER.ev0 = p => evAnswer(p.e)[0]; VER.ev1 = p => evAnswer(p.e)[1]; VER.ev2 = p => evAnswer(p.e)[2]; VER.ev3 = p => evAnswer(p.e)[3];
const dbl = (dD, dS) => ({ P: dD === dS ? 'can\'t tell' : dD > 0 ? 'rises' : 'falls', Q: dD === dS ? (dD > 0 ? 'rises' : 'falls') : 'can\'t tell' });
SK.double = { area: 'econ', label: 'Double shifts: when supply and demand both move', lo: 9, hi: 12, count: [4, 6, 8],
  make(v, r, g, n) {
    const G = r.pick(GOODS), Ds = EVENTS.filter(e => e[1] === 'D'), Ss = EVENTS.filter(e => e[1] === 'S'), items = [];
    const combos = [[1, 1], [1, -1], [-1, 1], [-1, -1]];
    const list = r.distinct(n, () => { const [a, b] = combos[items.length % 4] || r.pick(combos); const d = r.pick(Ds.filter(e => e[2] === a)), s = r.pick(Ss.filter(e => e[2] === b));
      return { d, s, q: `${fillEv(d[0], G)} At the same time, ${fillEv(s[0], G).replace(/^\w/, c => c.toLowerCase())}` }; }, x => x.q);
    const rows = list.map((x, i) => { const o = dbl(x.d[2], x.s[2]), dd = x.d[2] > 0 ? 'right' : 'left', ss = x.s[2] > 0 ? 'right' : 'left';
      items.push(I(`${x.q} Demand`, dd, 'dd', x), I(`${x.q} Supply`, ss, 'ds', x), I(`${x.q} Price`, o.P, 'dp', x), I(`${x.q} Quantity`, o.Q, 'dq', x));
      return [`${i + 1}. ${esc(x.q)}`, A(dd), A(ss), A(o.P), A(o.Q)]; });
    return {
      title: `Double shifts: the market for ${G.G}`,
      ican: 'I can predict price and quantity when supply and demand shift together, and tell which result is ambiguous.',
      directions: `Two things happen at once in the market for ${G.G}. Decide which way each curve shifts. Then predict the equilibrium price and quantity: rises, falls, or can't tell (it depends on which shift is bigger). Sketch each case on scrap paper if it helps.`,
      parts: [part('', example('Demand shifts right and supply shifts right: both push quantity up, so quantity <b>rises</b>. Demand pushes price up but supply pushes it down, so price: <b>can\'t tell</b>.')),
        part('Scenarios', T(['Scenario', 'Demand shifts', 'Supply shifts', 'Price', 'Quantity'], rows, 'fin-small'))],
      items,
      mistakes: 'Giving a definite answer for both price and quantity. When two shifts push one of them in opposite directions, it depends on which shift is bigger.',
      notes: 'In every double shift exactly one of price and quantity is ambiguous: price when the curves shift the same way, quantity when they shift opposite ways.',
    };
  } };
VER.dd = p => p.d[2] > 0 ? 'right' : 'left'; VER.ds = p => p.s[2] > 0 ? 'right' : 'left';
VER.dp = p => { const up = p.d[2] > 0 ? 1 : -1, sp = p.s[2] > 0 ? -1 : 1; return up === sp ? (up > 0 ? 'rises' : 'falls') : 'can\'t tell'; };
VER.dq = p => { const a = p.d[2] > 0 ? 1 : -1, b = p.s[2] > 0 ? 1 : -1; return a === b ? (a > 0 ? 'rises' : 'falls') : 'can\'t tell'; };

const ELAS = { elastic: [['movie tickets', 8, 15], ['restaurant meals', 12, 30], ['a brand of sneakers', 50, 90], ['concert T-shirts', 15, 30], ['ski rentals', 20, 40], ['a brand of cereal', 3, 6], ['theme park tickets', 40, 80]],
  inelastic: [['gasoline (per gallon)', 3, 5], ['table salt', 1, 3], ['bus fares for commuters', 2, 4], ['toothpaste', 3, 6], ['milk (per gallon)', 3, 5], ['bread (per loaf)', 2, 5], ['electricity (per 100 kWh)', 12, 20]],
  unit: [['umbrellas', 8, 16], ['notebooks', 2, 6], ['picture frames', 10, 20]] };
const midE = (P1, P2, Q1, Q2) => Math.abs(((Q2 - Q1) / ((Q1 + Q2) / 2)) / ((P2 - P1) / ((P1 + P2) / 2)));
SK.elastic = { area: 'econ', label: 'Price elasticity and total revenue', lo: 8, hi: 12, count: [4, 6, 8],
  make(v, r, g, n) {
    const mid = g >= 9, kinds = r.shuffle(['elastic', 'inelastic', 'unit', ...Array.from({ length: n }, () => r.pick(['elastic', 'inelastic', 'elastic', 'inelastic']))]).slice(0, n);
    const used = new Set(), items = [], rows = [];
    for (const kd of kinds) {
      let ok = false;
      for (let t = 0; t < 200 && !ok; t++) {
        const gd = r.pick(ELAS[kd]); if (used.has(gd[0])) continue;
        const P1 = r.int(gd[1], gd[2]), dP = Math.max(1, Math.round(P1 * r.int(10, 30) / 100)), P2 = P1 + dP;
        let Q1, Q2;
        if (kd === 'unit') { const k = r.int(2, 20) * 5; Q1 = k * P2; Q2 = k * P1; }
        else { Q1 = r.int(20, 100) * 10; const E = kd === 'elastic' ? 1.3 + r.next() * 1.7 : 0.15 + r.next() * 0.55, x = E * dP / ((P1 + P2) / 2); if (x >= 1.9) continue; Q2 = Math.round(Q1 * (2 - x) / (2 + x)); }
        if (Q2 >= Q1 || Q2 <= 0) continue;
        const E = midE(P1, P2, Q1, Q2), cls = kd === 'unit' ? 'unit elastic' : E > 1 ? 'elastic' : 'inelastic';
        if (kd !== 'unit' && Math.abs(E - 1) < 0.08) continue;
        const pq = (Q2 - Q1) / ((Q1 + Q2) / 2) * 100, pp = dP / ((P1 + P2) / 2) * 100;
        if (mid && (edgy(pq * 10) || edgy(pp * 10) || edgy(E * 100))) continue;
        used.add(gd[0]); ok = true;
        const g1 = { P1, P2, Q1, Q2, nm: gd[0] };
        if (mid) {
          items.push(I(`${gd[0]}: percent change in quantity`, `${pq < 0 ? '−' : ''}${fix(Math.abs(pq), 1)}%`, 'eq1', g1), I(`${gd[0]}: percent change in price`, `${fix(pp, 1)}%`, 'ep1', g1),
            I(`${gd[0]}: elasticity`, fix(E, 2), 'ee', g1), I(`${gd[0]}: type`, cls, 'ec', g1));
          rows.push([esc(gd[0]), `${usd0(P1)}&nbsp;→&nbsp;${usd0(P2)}`, `${fmt(Q1, 0)}&nbsp;→&nbsp;${fmt(Q2, 0)}`, A(items[items.length - 4].a), A(items[items.length - 3].a), A(fix(E, 2)), A(cls)]);
        } else {
          const R1 = P1 * Q1, R2 = P2 * Q2, ch = R2 - R1, cls2 = ch < 0 ? 'elastic' : ch > 0 ? 'inelastic' : 'unit elastic';
          items.push(I(`${gd[0]}: revenue before`, usd0(R1), 'rev', { a: P1, b: Q1 }), I(`${gd[0]}: revenue after`, usd0(R2), 'rev', { a: P2, b: Q2 }), I(`${gd[0]}: change`, ch === 0 ? 'no change' : `${ch > 0 ? 'up' : 'down'} ${usd0(Math.abs(ch))}`, 'rch', g1), I(`${gd[0]}: type`, cls2, 'ec', g1));
          rows.push([esc(gd[0]), `${usd0(P1)}&nbsp;→&nbsp;${usd0(P2)}`, `${fmt(Q1, 0)}&nbsp;→&nbsp;${fmt(Q2, 0)}`, A(usd0(R1)), A(usd0(R2)), A(items[items.length - 2].a), A(cls2)]);
        }
      }
      if (!ok) return null;
    }
    const head = mid ? ['Good', 'Price', 'Quantity sold', '% change in quantity', '% change in price', 'Elasticity', 'Elastic, inelastic or unit?'] : ['Good', 'Price', 'Quantity sold', 'Revenue before', 'Revenue after', 'Change', 'Elastic, inelastic or unit?'];
    return {
      ican: mid ? 'I can use the midpoint formula to find price elasticity of demand and classify a good.' : 'I can use total revenue to tell whether demand is elastic or inelastic.',
      directions: mid ? 'Use the midpoint formula. Percent change = change ÷ average of the two values × 100 (nearest tenth). Elasticity = |% change in quantity ÷ % change in price| (two decimals). More than 1 is elastic, less than 1 is inelastic, exactly 1 is unit elastic.'
        : 'Each shop raises its price. Revenue = price × quantity sold. If revenue falls when the price rises, demand is elastic; if it rises, demand is inelastic; if it stays the same, unit elastic.',
      parts: [part('', mid ? example('Price $4 → $6, quantity 120 → 80: % change in quantity = −40 ÷ 100 = −40.0%; % change in price = 2 ÷ 5 = 40.0%.', 'Elasticity = |−40.0 ÷ 40.0| = <b>1.00</b>, unit elastic.')
        : example('Price $4 → $5, quantity 100 → 70: revenue $4 × 100 = $400 before, $5 × 70 = $350 after.', 'Revenue went <b>down</b> when the price rose, so demand is <b>elastic</b>.')),
        part('The goods', T(head, rows, 'fin-small')),
        part('Think about it', ql(1, 'Look at the goods that came out inelastic. What do they have in common? Why would buyers keep buying them when the price rises?', lines(2)))],
      items,
      mistakes: mid ? 'Dividing by the starting value instead of the average (the midpoint method gives the same answer whichever way the price moves), and putting price on top of the fraction.' : 'Deciding by how much the quantity fell instead of what happened to revenue.',
      notes: 'The numbers are invented but follow real patterns: goods with few substitutes or that people need (fuel, salt, bus fares) are inelastic; goods with many substitutes or that people can skip are elastic.',
    };
  } };
VER.eq1 = p => { const x = (p.Q2 - p.Q1) / ((p.Q1 + p.Q2) / 2) * 100; return `${x < 0 ? '−' : ''}${(Math.round(Math.abs(x) * 10) / 10).toFixed(1)}%`; };
VER.ep1 = p => `${(Math.round((p.P2 - p.P1) / ((p.P1 + p.P2) / 2) * 1000) / 10).toFixed(1)}%`;
VER.ee = p => (Math.round(midE(p.P1, p.P2, p.Q1, p.Q2) * 100) / 100).toFixed(2);
VER.ec = p => { const R1 = p.P1 * p.Q1, R2 = p.P2 * p.Q2; return R1 === R2 ? 'unit elastic' : R2 < R1 ? 'elastic' : 'inelastic'; };   // the total revenue test agrees with the midpoint elasticity
VER.rev = p => usd0(p.a * p.b);
VER.rch = p => { const c = p.P2 * p.Q2 - p.P1 * p.Q1; return c === 0 ? 'no change' : `${c > 0 ? 'up' : 'down'} ${usd0(Math.abs(c))}`; };

// marginal benefit and cost: totals for 0..5 units, the best number is the last unit whose MB > MC
const CHOICES = [
  { t: 'Hours of study the night before a test', u: 'hours', b: 'Total benefit (points of value)', c: 'Total cost (points of value: sleep and free time given up)', unit: 'points', mb: [[14, 20], [9, 13], [6, 8], [3, 5], [1, 2]], mc: [[2, 4], [4, 6], [6, 8], [8, 10], [10, 12]] },
  { t: 'Pizzas to order for a club meeting', u: 'pizzas', b: 'Total benefit (dollars the club would pay)', c: 'Total cost (dollars)', unit: 'dollars', mb: [[30, 40], [20, 28], [13, 18], [7, 11], [2, 5]], flat: [10, 16] },
  { t: 'Workers to hire at a car wash for a Saturday', u: 'workers', b: 'Total benefit (extra sales, dollars)', c: 'Total cost (wages, dollars)', unit: 'dollars', mb: [[220, 300], [160, 210], [110, 150], [60, 100], [20, 50]], flat: [100, 140] }];
SK.marginal = { area: 'econ', label: 'Marginal benefit and marginal cost', lo: 9, hi: 12, count: null,
  make(v, r) {
    const items = [], parts = [part('', example('Marginal benefit = the change in total benefit from one more unit. Marginal cost = the change in total cost.', 'Keep adding units while marginal benefit is bigger than marginal cost. Stop before the first unit where it is smaller.'))];
    let n = 0;
    for (const C of CHOICES) {
      let mb, mc, best;
      for (let t = 0; t < 200; t++) {
        mb = C.mb.map(([a, b]) => r.int(a, b)); const f = C.flat ? r.int(C.flat[0], C.flat[1]) : 0; mc = C.flat ? mb.map(() => f) : C.mc.map(([a, b]) => r.int(a, b));
        if (mb.some((x, i) => x === mc[i])) continue;
        best = mb.filter((x, i) => x > mc[i]).length;
        if (best >= 2 && best <= 4 && mb.every((x, i) => (x > mc[i]) === (i < best))) break;
        best = null;
      }
      if (!best) return null;
      const TB = [0], TC = [0]; mb.forEach((x, i) => { TB.push(TB[i] + x); TC.push(TC[i] + mc[i]); });
      mb.forEach((x, i) => items.push(I(`${C.u} ${i + 1}: marginal benefit`, fmt(x, 0), 'mb', { xs: TB, k: i + 1 }), I(`${C.u} ${i + 1}: marginal cost`, fmt(mc[i], 0), 'mb', { xs: TC, k: i + 1 })));
      items.push(I(`Best number of ${C.u}`, String(best), 'mbest', { TB, TC }));
      n++;
      parts.push(part(C.t, T([esc(C.u[0].toUpperCase() + C.u.slice(1)), esc(C.b), esc(C.c), 'Marginal benefit', 'Marginal cost'], TB.map((b, i) => [i, fmt(b, 0), fmt(TC[i], 0), i ? A(fmt(mb[i - 1], 0)) : '', i ? A(fmt(mc[i - 1], 0)) : '']), 'fin-small') +
        `<p>Best number of ${esc(C.u)}: ${blank(String(best), 3)}</p>`));
    }
    parts.push(part('Think about it', ql(1, 'Why is the best choice usually not the one with the biggest total benefit?', lines(2))));
    return {
      ican: 'I can use marginal benefit and marginal cost to find the best amount of something to do or buy.',
      directions: 'Fill in the marginal benefit and marginal cost of each unit from the totals. Then find the best number: the last unit whose marginal benefit is bigger than its marginal cost.',
      parts, items,
      mistakes: 'Choosing where total benefit is biggest, or where total benefit minus total cost is computed wrong. Compare the extra benefit and extra cost of each next unit.',
      notes: 'The tables are invented. Marginal benefit falls as you get more (the fifth pizza matters less than the first), which is why stopping early can be the best choice.',
    };
  } };
VER.mb = p => fmt(p.xs[p.k] - p.xs[p.k - 1], 0);
VER.mbest = p => { let b = 0, k = 0; p.TB.forEach((x, i) => { if (x - p.TC[i] > b) { b = x - p.TC[i]; k = i; } }); return String(k); };   // a second route: most net benefit

SK.profit = { area: 'econ', label: 'Profit where marginal revenue meets marginal cost', lo: 10, hi: 12, count: null,
  make(v, r) {
    const firm = r.pick([['a bakery', 'dozen cookies'], ['a T-shirt printer', 'boxes of shirts'], ['a bike shop', 'repairs a day'], ['a food truck', 'dozen tacos']]), mono = r.chance(.5);
    for (let t = 0; t < 300; t++) {
      const FC = r.int(4, 12) * 5, mc = [r.int(4, 8)]; for (let i = 1; i < 6; i++) mc.push(mc[i - 1] + r.int(2, 6));
      const P = mono ? [0, 1, 2, 3, 4, 5, 6].map(q => 0) : null; let price, TR;
      if (mono) { const a = r.int(30, 50), b = r.int(2, 4); price = [0, 1, 2, 3, 4, 5, 6].map(q => a - b * q); TR = price.map((p, q) => p * q); }
      else { const p = r.int(mc[1] + 1, mc[4] - 1); price = [0, 1, 2, 3, 4, 5, 6].map(() => p); TR = price.map((pp, q) => pp * q); }
      const TC = [FC]; mc.forEach((m, i) => TC.push(TC[i] + m));
      const MR = [1, 2, 3, 4, 5, 6].map(q => TR[q] - TR[q - 1]);
      if (MR.some((m, i) => m === mc[i])) continue;
      const best = MR.filter((m, i) => m > mc[i]).length;
      if (best < 2 || best > 5 || !MR.every((m, i) => (m > mc[i]) === (i < best))) continue;
      const prof = TR.map((x, q) => x - TC[q]), items = [];
      [1, 2, 3, 4, 5, 6].forEach(q => items.push(I(`Q ${q}: total revenue`, usd0(TR[q]), 'rev', { a: price[q], b: q }), I(`Q ${q}: marginal revenue`, usd0(MR[q - 1]), 'mr', { TR, q }),
        I(`Q ${q}: marginal cost`, usd0(mc[q - 1]), 'mr', { TR: TC, q }), I(`Q ${q}: profit`, usd0(prof[q]), 'prof', { TR, TC, q })));
      items.push(I('Best quantity', String(best), 'pbest', { TR, TC }), I('Most profit', usd0(prof[best]), 'maxp', { TR, TC }));
      return {
        ican: 'I can use a cost and revenue table to find the output where marginal revenue meets marginal cost, and the profit there.',
        directions: `Fill in the table for ${firm[0]}. Total revenue = price × quantity. Marginal revenue and marginal cost are the changes from one row to the next. Profit = total revenue − total cost. Then find the quantity where profit is greatest: keep producing while marginal revenue is bigger than marginal cost.`,
        parts: [part('', box(`<p>${mono ? 'This seller must lower its price to sell more, so marginal revenue falls.' : 'This seller sells every unit at the same market price, so marginal revenue equals the price.'} Fixed costs are ${usd0(FC)}.</p>`)),
          part(`${firm[0][0].toUpperCase()}${firm[0].slice(1)}: ${firm[1]}`, T(['Quantity', 'Price', 'Total revenue', 'Total cost', 'Marginal revenue', 'Marginal cost', 'Profit'],
            TR.map((x, q) => [q, usd0(price[q]), q ? A(usd0(x)) : usd0(0), usd0(TC[q]), q ? A(usd0(MR[q - 1])) : '', q ? A(usd0(mc[q - 1])) : '', q ? A(usd0(prof[q])) : usd0(-FC)]))),
          part('Questions', ql(1, 'At what quantity is profit greatest, and what is the profit?', aline('Quantity', String(best), 4) + aline('Profit', usd0(prof[best]))) +
            ql(2, 'Why does producing one more unit past that point lower profit?', lines(2)))],
        items,
        mistakes: 'Picking the quantity with the most revenue instead of the most profit, and reading marginal cost from the total cost column without subtracting.',
        notes: 'The numbers are invented. Marginal cost rises because each extra unit takes more effort (overtime, crowding). The best output is the last unit where marginal revenue is still more than marginal cost.',
      };
    }
    return null;
  } };
VER.mr = p => usd0(p.TR[p.q] - p.TR[p.q - 1]);
VER.prof = p => usd0(p.TR[p.q] - p.TC[p.q]);
VER.maxp = p => usd0(Math.max(...p.TR.slice(1).map((x, q) => x - p.TC[q + 1])));
VER.pbest = p => { let b = -Infinity, k = 0; for (let q = 1; q < p.TR.length; q++) if (p.TR[q] - p.TC[q] > b) { b = p.TR[q] - p.TC[q]; k = q; } return String(k); };
VER.gl = p => p.a > p.b ? `Gain of ${usd(p.a - p.b)}` : `Loss of ${usd(p.b - p.a)}`;

SK.ppf = { area: 'econ', label: 'The production possibilities frontier', lo: 9, hi: 12, count: null,
  make(v, r) {
    const pair = r.pick([['wheat', 'tons of wheat', 'laptops', 'thousand laptops'], ['corn', 'tons of corn', 'bikes', 'hundred bikes'], ['pizzas', 'hundred pizzas', 'robots', 'robots']]);
    for (let t = 0; t < 200; t++) {
      const sx = r.pick([10, 20, 50]), dec = r.shuffle([1, 2, 3, 4, 5].map(() => r.int(2, 30))).sort((a, b) => a - b);
      if (new Set(dec).size < 5) continue;
      const Ymax = dec.reduce((a, b) => a + b, 0), xs = [0, 1, 2, 3, 4, 5].map(k => k * sx), ys = [Ymax]; dec.forEach((d, i) => ys.push(ys[i] - d));
      const L = 'ABCDEF', pts = xs.map((x, k) => ({ l: L[k], x, y: ys[k] }));
      const k1 = r.int(1, 3), k2 = r.int(1, 4), k3 = r.int(1, 3);
      const P1 = { l: 'G', x: xs[k1], y: Math.round(ys[k1] * 0.6) }, P2 = { l: 'H', x: xs[k2], y: ys[k2] }, P3 = { l: 'J', x: xs[k3] + Math.round(sx / 2), y: ys[k3] + 2 };
      if (P1.y >= ys[k1] || P1.y <= 0) continue;
      const items = [];
      [[P1, 'inefficient'], [P2, 'efficient'], [P3, 'impossible']].forEach(([p, a]) => items.push(I(`Point ${p.l} (${p.x}, ${p.y})`, a, 'ppfc', { p, xs, ys })));
      const a = r.int(0, 3);
      items.push(I(`Opportunity cost from ${L[a]} to ${L[a + 1]}`, `${dec[a]} ${pair[3]}`, 'oc', { ys, a, u: pair[3] }), I(`Opportunity cost from ${L[a + 1]} to ${L[a + 2]}`, `${dec[a + 1]} ${pair[3]}`, 'oc', { ys, a: a + 1, u: pair[3] }));
      const marks = r.shuffle([P1, P2, P3]);
      const st = nice(Ymax + 4, 6);
      const gr = grid({ x: [0, xs[5] + sx, sx, `${pair[1][0].toUpperCase()}${pair[1].slice(1)}`, x => fmt(x, 0)], y: [0, top(Ymax + 4, st), st, `${pair[3][0].toUpperCase()}${pair[3].slice(1)}`, y => fmt(y, 0)], H: 290,
        show: (X, Y) => marks.map(p => `<circle cx="${X(p.x)}" cy="${Y(p.y)}" r="4" fill="#222"/>` + tx(X(p.x) + 6, Y(p.y) - 6, p.l, 'font-size="13" font-weight="700"')).join(''),
        key: (X, Y) => redLine(xs.map((x, k) => [x, ys[k]]), X, Y) + pts.filter(p => !(p.x === P2.x && p.y === P2.y)).map(p => rtx(X(p.x) + 5, Y(p.y) - 5, p.l, 'font-size="12"')).join(''), title: `Production possibilities: ${pair[0]} and ${pair[2]}` });
      return {
        ican: 'I can plot a production possibilities frontier, classify points and find opportunity cost.',
        directions: `A made-up country uses all its workers and machines to make ${pair[0]} and ${pair[2]}. Plot points A to F from the table and connect them to draw the frontier. Then decide whether each lettered point on the graph is efficient (on the curve), inefficient (inside) or impossible (outside).`,
        parts: [part('The possibilities', T(['Point', ...pts.map(p => p.l)], [[`${pair[1]}`, ...xs.map(x => fmt(x, 0))], [`${pair[3]}`, ...ys.map(y => fmt(y, 0))]], 'fin-small')),
          part('Graph it', gr),
          part('Questions', ql(1, 'Classify each point.', marks.map(p => aline(`${p.l} (${p.x}, ${p.y})`, items.find(i => i.q.startsWith(`Point ${p.l}`)).a, 8)).join('')) +
            ql(2, `What is the opportunity cost of moving from ${L[a]} to ${L[a + 1]}? From ${L[a + 1]} to ${L[a + 2]}?`, aline(`${L[a]} to ${L[a + 1]}`, items[3].a, 9) + aline(`${L[a + 1]} to ${L[a + 2]}`, items[4].a, 9)) +
            ql(3, `Why does each extra ${sx} ${pair[1]} cost more ${pair[2]} than the last? Why is the curve bowed out?`, lines(2)))],
        items,
        mistakes: 'Calling a point inside the curve impossible (it is possible, just wasteful), and giving opportunity cost as the good gained instead of the good given up.',
        notes: 'The opportunity costs rise along the curve because resources are not equally good at making both goods, which bows the frontier outward. A point outside becomes possible only with growth: more resources or better technology.',
        materials: 'pencil, ruler',
      };
    }
    return null;
  } };
VER.ppfc = p => { const k = p.xs.indexOf(p.p.x); if (k >= 0) return p.p.y === p.ys[k] ? 'efficient' : p.p.y < p.ys[k] ? 'inefficient' : 'impossible';
  const j = p.xs.findIndex(x => x > p.p.x); return p.p.y > p.ys[j - 1] ? 'impossible' : 'check'; };
VER.oc = p => `${p.ys[p.a] - p.ys[p.a + 1]} ${p.u}`;

SK.breakeven = { area: 'econ', label: 'Break-even at three prices', lo: 7, hi: 12, count: null,
  make(v, r) {
    const biz = r.pick([['a market booth selling candles', 'candles'], ['a lemonade stand', 'cups'], ['a sticker shop', 'sticker packs'], ['a bracelet booth', 'bracelets'], ['a bake sale table', 'muffins']]);
    for (let t = 0; t < 200; t++) {
      const F = r.pick([120, 180, 240, 300, 360, 420, 480, 600]), vc = r.int(1, 6), ms = r.sample([2, 3, 4, 5, 6, 8, 10, 12].filter(m => F % m === 0 && F / m <= 150), 3).sort((a, b) => a - b);
      if (ms.length < 3) continue;
      const prices = ms.map(m => m + vc), be = ms.map(m => F / m), items = [];
      prices.forEach((p, i) => items.push(I(`At ${usd0(p)}: profit per item`, usd0(p - vc), 'bpi', { p, vc }), I(`At ${usd0(p)}: break-even`, `${be[i]} ${biz[1]}`, 'be', { F, p, vc, u: biz[1] }), I(`At ${usd0(p)}: revenue at break-even`, usd0(p * be[i]), 'beR', { F, p, vc })));
      const N = r.int(Math.ceil(be[1] / 10), Math.ceil(be[0] / 10)) * 10, pr = (prices[1] - vc) * N - F;
      if (pr === 0) continue;
      items.push(I(`Selling ${N} at ${usd0(prices[1])}`, pr > 0 ? `Profit of ${usd0(pr)}` : `Loss of ${usd0(-pr)}`, 'beP', { F, p: prices[1], vc, N }));
      const xmax = top(be[0] * 1.2, nice(be[0] * 1.2, 6)), ymax = Math.max(F + vc * xmax, prices[2] * xmax * 0.6), st = nice(ymax, 6);
      const gr = grid({ x: [0, xmax, nice(be[0] * 1.2, 6), `Number of ${biz[1]} sold`, x => fmt(x, 0)], y: [0, top(ymax, st), st, 'Dollars', y => usd0(y)], H: 290,
        key: (X, Y) => { const clip = (p) => { const xe = Math.min(xmax, top(ymax, st) / p); return [[0, 0], [xe, p * xe]]; };
          return redLine([[0, F], [xmax, F + vc * xmax]], X, Y) + rtx(X(xmax) - 4, Y(F + vc * xmax) + 15, 'cost', 'font-size="11.5" text-anchor="end"') +
            prices.map((p, i) => redLine(clip(p), X, Y, true) + `<circle cx="${X(be[i])}" cy="${Y(p * be[i])}" r="6" fill="none" stroke="${RED}" stroke-width="2"/>` + rtx(X(clip(p)[1][0]) - 3, Y(clip(p)[1][1]) + 14, usd0(p), 'font-size="11.5" text-anchor="end"')).join(''); }, title: 'Cost and revenue' });
      return {
        ican: 'I can find the break-even point at different prices and show it on a graph.',
        directions: `${biz[0][0].toUpperCase()}${biz[0].slice(1)} has fixed costs of ${usd0(F)} (booth fee and equipment) and spends ${usd0(vc)} on supplies for each of its ${biz[1]}. Break-even is where total revenue equals total cost: fixed costs ÷ (price − cost per item).`,
        parts: [part('', example(`Fixed costs $200, cost per item $3, price $7: each sale covers $7 − $3 = $4 of fixed costs, so $200 ÷ $4 = <b>50 items</b> to break even.`)),
          part('Three prices', T(['Price', 'Profit on each item', 'Break-even (items)', 'Revenue at break-even'], prices.map((p, i) => [usd0(p), A(usd0(p - vc)), A(`${be[i]} ${biz[1]}`), A(usd0(p * be[i]))]))),
          part('Graph it', `<p>Draw the cost line from (0, ${usd0(F)}) rising ${usd0(vc)} per item. Draw a revenue line from (0, $0) for each price. Circle each break-even point.</p>` + gr),
          part('Questions', ql(1, `At ${usd0(prices[1])}, the booth sells ${N} ${biz[1]}. Profit or loss, and how much?`, aline('Answer', items[items.length - 1].a, 10)) +
            ql(2, 'A higher price breaks even sooner. Why might the owner still not choose the highest price?', lines(2)))],
        items,
        mistakes: 'Dividing the fixed costs by the price instead of by the profit on each item, and forgetting that the cost line starts at the fixed costs, not at zero.',
        notes: 'Prices and costs are invented and chosen so each break-even point is a whole number. In real markets, raising the price usually means selling fewer.',
        materials: 'pencil, calculator, ruler',
      };
    }
    return null;
  } };
VER.bpi = p => usd0(p.p - p.vc);
VER.be = p => { let n = 0; while (n * p.p < p.F + n * p.vc) n++; return `${n} ${p.u}`; };
VER.beR = p => { let n = 0; while (n * p.p < p.F + n * p.vc) n++; return usd0(n * p.p); };
VER.beP = p => { const x = p.N * p.p - (p.F + p.N * p.vc); return x > 0 ? `Profit of ${usd0(x)}` : `Loss of ${usd0(-x)}`; };

// exchange rates: [currency, symbol style, rates per US dollar, price step]
const FX = [['Mexican pesos', 'pesos', [16, 17, 17.5, 18, 19, 20], 5], ['euros', 'euros', [0.85, 0.9, 0.92, 0.95], 0.5], ['Canadian dollars', 'Canadian dollars', [1.3, 1.35, 1.4], 0.5],
  ['Japanese yen', 'yen', [125, 140, 150, 160], 100], ['British pounds', 'pounds', [0.75, 0.8, 0.82], 0.5], ['Indian rupees', 'rupees', [80, 83, 85], 10]];
const FXGOODS = [['T-shirt', 8, 25], ['pair of sandals', 15, 45], ['backpack', 20, 60], ['bag of coffee', 6, 15], ['soccer ball', 12, 35], ['hat', 8, 25], ['blanket', 20, 70], ['set of headphones', 20, 80], ['phone case', 8, 25], ['bottle of olive oil', 6, 18]];
SK.exchange = { area: 'econ', label: 'Exchange rates: convert and compare prices', lo: 6, hi: 12, count: [4, 6, 8],
  make(v, r, g, n) {
    const C = r.pick(FX), rt = r.pick(C[2]), items = [];
    const rows = r.sample(FXGOODS, n).map(G => {
      for (let t = 0; t < 60; t++) {
        const us = r.int(G[1] * 2, G[2] * 2) * 50, f = Math.round(us / 100 * rt * (0.75 + r.next() * 0.5) / C[3]) * C[3], conv = f / rt * 100;
        if (f <= 0 || edgy(conv) || Math.round(conv) === us) continue;
        const c = Math.round(conv), where = c < us ? 'abroad' : 'at home';
        items.push(I(`${G[0]}: in dollars`, usd(c), 'fx', { f, rt }), I(`${G[0]}: cheaper`, where, 'fxw', { f, rt, us }));
        return [esc(G[0]), usd(us), `${fmt(f, 2)} ${C[1]}`, A(usd(c)), A(where)];
      }
      return null;
    });
    if (rows.some(x => !x)) return null;
    const parts = [part('', box(`<p><b>Made-up rate for practice:</b> 1 US dollar = ${fmt(rt, 2)} ${C[1]}. (Real rates change every day.) To change ${C[1]} to dollars, divide by ${fmt(rt, 2)}. To change dollars to ${C[1]}, multiply.</p>`) +
      example(`${fmt(rt * 20, 2)} ${C[1]} ÷ ${fmt(rt, 2)} = <b>${usd(2000)}</b>.`)),
      part(`Compare: a store at home and a market abroad (${C[0]})`, T(['Item', 'Price at home', 'Price abroad', 'Price abroad in dollars', 'Cheaper: at home or abroad?'], rows))];
    if (g >= 9) {
      const rt2 = Math.round(rt * 1.2 * 100) / 100, hotel = Math.round(rt * r.int(80, 200) / C[3]) * C[3], h1 = hotel / rt * 100, h2 = hotel / rt2 * 100;
      if (edgy(h1) || edgy(h2)) return null;
      items.push(I('Hotel before', usd(Math.round(h1)), 'fx', { f: hotel, rt }), I('Hotel after', usd(Math.round(h2)), 'fx', { f: hotel, rt: rt2 }), I('Who is helped', 'US tourists and US importers', 'name', { t: 'US tourists and US importers' }), I('Who is hurt', 'US exporters', 'name', { t: 'US exporters' }));
      parts.push(part('The dollar gets stronger', `<p>The rate changes from 1 dollar = ${fmt(rt, 2)} ${C[1]} to 1 dollar = ${fmt(rt2, 2)} ${C[1]}. Each dollar now buys more ${C[1]}.</p>` +
        ql(1, `A hotel night abroad costs ${fmt(hotel, 2)} ${C[1]}. What does it cost in dollars before and after the change?`, aline('Before', usd(Math.round(h1))) + aline('After', usd(Math.round(h2)))) +
        ql(2, 'Who is helped by a stronger dollar: US tourists abroad, US companies that import goods, or US companies that export goods? Who is hurt? Explain.', lines(2) + h.keyline('Helped: US tourists and US importers (foreign goods cost fewer dollars). Hurt: US exporters (US goods cost more in other currencies).'))));
    }
    return {
      ican: 'I can use an exchange rate to convert prices between two currencies and decide where something is cheaper.',
      directions: `Change each price abroad into dollars (round to the nearest cent), then decide where each item is cheaper.`,
      parts, items,
      mistakes: `Multiplying when you should divide. Check: one dollar is worth ${fmt(rt, 2)} ${C[1]}, so a price in ${C[1]} should become ${rt > 1 ? 'a smaller' : 'a bigger'} number of dollars.`,
      notes: 'The exchange rate is invented, near the size of a real one; use the rate printed on the sheet. Real travelers also pay exchange fees.',
    };
  } };
VER.fx = p => usd(Math.round(p.f * 100 / p.rt));
VER.fxw = p => Math.round(p.f * 100 / p.rt) < p.us ? 'abroad' : 'at home';

SK.multiplier = { area: 'econ', label: 'The money multiplier', lo: 9, hi: 12, count: null,
  make(v, r) {
    for (let t = 0; t < 100; t++) {
      const D = r.int(1, 10) * 500, rr = r.pick([5, 10, 20, 25]), rows = []; let d = D * 100, bad = false;
      for (let b = 1; b <= 5; b++) { const res = d * rr / 100, ln = d - Math.round(res); if (edgy(res)) bad = true; rows.push({ b, d, res: Math.round(res), ln }); d = ln; }
      if (bad) continue;
      const items = [];
      rows.forEach(x => items.push(...(x.b > 1 ? [I(`Bank ${x.b}: new deposit`, usd(x.d), 'mmd', { D, rr, b: x.b })] : []), I(`Bank ${x.b}: required reserves`, usd(x.res), 'mmr', { D, rr, b: x.b }), I(`Bank ${x.b}: can lend`, usd(x.ln), 'mml', { D, rr, b: x.b })));
      const loans = rows.reduce((a, x) => a + x.ln, 0), mult = 100 / rr;
      items.push(I('Total loans from 5 banks', usd(loans), 'mmt', { D, rr }), I('Money multiplier', fmt(mult, 2), 'mm', { rr }), I('Most total deposits', usd0(D * mult), 'mmx', { D, rr }), I('Most new money from loans', usd0(D * mult - D), 'mmn', { D, rr }));
      return {
        ican: 'I can trace a deposit through the banking system and use the money multiplier.',
        directions: `${usd0(D)} is deposited in Bank 1. The reserve requirement is ${rr}%: each bank keeps ${rr}% of a deposit and lends out the rest, and each loan is deposited in the next bank. Round to the nearest cent.`,
        parts: [part('', example(`A ${usd0(1000)} deposit with a 10% requirement: keep ${usd0(100)}, lend ${usd0(900)}. The ${usd0(900)} becomes the next bank's deposit.`)),
          part('Five banks', T(['Bank', 'New deposit', `Required reserves (${rr}%)`, 'Amount it can lend'], rows.map(x => [x.b, x.b === 1 ? usd(x.d) : A(usd(x.d)), A(usd(x.res)), A(usd(x.ln))])) +
            `<p>Total lent by the five banks: ${blank(usd(loans), 7)}</p>`),
          part('The money multiplier', ql(1, `The money multiplier is 1 ÷ reserve requirement. What is it for ${rr}%?`, aline('Multiplier', fmt(mult, 2))) +
            ql(2, `If the process kept going forever, what is the most the ${usd0(D)} deposit could become in total deposits? How much of that is new money created by loans?`, aline('Total deposits', usd0(D * mult)) + aline('New money', usd0(D * mult - D))) +
            ql(3, 'Why is the real amount of new money usually smaller than this maximum?', lines(2)))],
        items,
        mistakes: 'Using the reserve requirement itself as the multiplier, and counting the first deposit as new money (it already existed; only the loans create new money).',
        notes: 'This is the simple textbook model. Real banks often hold extra reserves and people keep some cash, so the real multiplier is smaller. In 2020 the U.S. Federal Reserve set reserve requirements to zero, so the requirement here is for practice.',
      };
    }
    return null;
  } };
const mmChain = (D, rr, b) => { let d = D * 100; for (let k = 1; k < b; k++) d = d - Math.round(d * rr / 100); return d; };
VER.mmd = p => usd(mmChain(p.D, p.rr, p.b));
VER.mmr = p => usd(Math.round(mmChain(p.D, p.rr, p.b) * p.rr / 100));
VER.mml = p => usd(mmChain(p.D, p.rr, p.b + 1));
VER.mmt = p => usd([1, 2, 3, 4, 5].reduce((a, b) => a + mmChain(p.D, p.rr, b + 1), 0));
VER.mm = p => fmt(1 / (p.rr / 100), 2);
VER.mmx = p => usd0(p.D / (p.rr / 100));
VER.mmn = p => usd0(p.D / (p.rr / 100) - p.D);

// GDP items: [text, category, low, high] in billions
const GDPI = [['Families buy groceries, clothes and haircuts', 'C', 300, 900], ['Families buy new cars and furniture', 'C', 80, 250], ['People pay rent and doctor bills', 'C', 200, 600],
  ['Businesses buy new machines for factories', 'I', 60, 200], ['Builders put up new houses', 'I', 40, 150], ['A company builds a new warehouse', 'I', 10, 60],
  ['The government pays to build roads and bridges', 'G', 40, 150], ['The government pays teachers and firefighters', 'G', 80, 250],
  ['Farmers sell wheat to buyers in other countries', 'X', 30, 120], ['Factories sell machines to buyers in other countries', 'X', 20, 100],
  ['People and businesses buy goods made in other countries', 'M', 50, 200],
  ['People buy and sell used cars', 'N', 20, 80], ['Investors buy shares of stock', 'N', 50, 300], ['The government sends Social Security checks', 'N', 60, 200], ['A bakery buys flour to make the bread it sells', 'N', 5, 30], ['Parents do unpaid work at home', 'N', 50, 200]];
const GDPN = { C: 'consumer spending (C)', I: 'investment (I)', G: 'government purchases (G)', X: 'exports (X)', M: 'imports (M)', N: 'not counted' };
SK.gdp = { area: 'econ', label: 'GDP by the expenditure approach', lo: 9, hi: 12, count: [9, 11, 13],
  make(v, r, g, n) {
    const by = c => GDPI.filter(x => x[1] === c);
    const nN = n - 7, pick = [...r.sample(by('C'), 2), ...r.sample(by('I'), 1), ...r.sample(by('G'), 1), ...r.sample(by('X'), 1), ...by('M'), ...r.sample(by('I').concat(by('G')).filter(x => true), 1), ...r.sample(by('N'), nN)];
    const uniq = [...new Map(pick.map(x => [x[0], x])).values()];
    if (uniq.length < pick.length) return null;
    const list = r.shuffle(uniq).map(x => ({ t: x[0], c: x[1], v: r.int(x[2] / 5, x[3] / 5) * 5 }));
    const sumc = c => list.filter(x => x.c === c).reduce((a, b) => a + b.v, 0);
    const C = sumc('C'), Iv = sumc('I'), G = sumc('G'), X = sumc('X'), Mv = sumc('M'), gdp = C + Iv + G + X - Mv, items = [];
    list.forEach(x => items.push(I(`${x.t}: category`, GDPN[x.c], 'gcat', { c: x.c })));
    [['C', C], ['I', Iv], ['G', G], ['X', X], ['M', Mv]].forEach(([c, s]) => items.push(I(`Total ${c}`, `$${fmt(s, 0)} billion`, 'gsum', { list, c })));
    items.push(I('GDP', `$${fmt(gdp, 0)} billion`, 'gdp', { list }));
    return {
      ican: 'I can calculate GDP with the expenditure approach and tell which spending does not count.',
      directions: 'A made-up country spent this money in one year (in billions of dollars). Label each item C, I, G, X, M or Not counted. Then total each group and find GDP = C + I + G + (X − M).',
      parts: [part('', box('<p><b>GDP counts new, final goods and services made in the country this year.</b> It leaves out used goods, stocks and other financial deals, transfer payments (money the government gives without buying anything), parts bought to make something else, and unpaid work.</p>')),
        part('The spending', T(['What happened', 'Amount', 'C, I, G, X, M or not counted'], list.map(x => [esc(x.t), `$${fmt(x.v, 0)} billion`, A(GDPN[x.c])]), 'fin-small')),
        part('Add it up', T(['C', 'I', 'G', 'X', 'M', 'GDP = C + I + G + X − M'], [[A(`$${fmt(C, 0)} billion`), A(`$${fmt(Iv, 0)} billion`), A(`$${fmt(G, 0)} billion`), A(`$${fmt(X, 0)} billion`), A(`$${fmt(Mv, 0)} billion`), A(`$${fmt(gdp, 0)} billion`)]]) +
          ql(1, 'Pick one item that is not counted. Explain why counting it would give a wrong picture of what the country made this year.', lines(2)))],
      items,
      mistakes: 'Counting a stock purchase or a used car as investment (investment in GDP means new buildings, machines and inventories), and adding imports instead of subtracting them.',
      notes: 'The country and numbers are invented. Imports are subtracted because they were already counted inside C, I or G but were made somewhere else.',
    };
  } };
VER.gcat = p => GDPN[p.c];
VER.gsum = p => `$${fmt(p.list.filter(x => x.c === p.c).reduce((a, b) => a + b.v, 0), 0)} billion`;
VER.gdp = p => `$${fmt(p.list.reduce((a, x) => a + (x.c === 'M' ? -x.v : x.c === 'N' ? 0 : x.v), 0), 0)} billion`;

/* ---------- fields and the sheet ---------- */
const GRADES = ['5', '6', '7', '8', '9', '10', '11', '12'].map(g => [g, `Grade ${g}`]);
const AREAS = [['earn', 'Earning and taxes'], ['spend', 'Spending and budgets'], ['save', 'Saving and interest'], ['credit', 'Credit, loans and college costs'], ['risk', 'Insurance, investing and big purchases'], ['econ', 'Economics']];
const skillsFor = (area, g) => Object.entries(SK).filter(([, s]) => s.area === area && g >= s.lo && g <= s.hi);
const areasFor = g => AREAS.filter(([a]) => skillsFor(a, g).length);
const curSkill = v => SK[v.skill] && SK[v.skill].area === v.area ? SK[v.skill] : null;

Gen.add('finance', {
  title: 'Money and Finance', type: 'Practice',
  css: `.fin-t td,.fin-t th{text-align:center}
.fin-t td:first-child{text-align:left}
.fin-small{font-size:13px}
.fin-small th,.fin-small td{padding:3px 6px}
.fin-box{border:1.5px solid #222;border-radius:6px;padding:6px 12px;margin:6px 0 10px;break-inside:avoid}
.fin-box p{margin:2px 0}
.fin-ps{display:grid;grid-template-columns:1fr 1fr;gap:10px 20px;margin:6px 0}
.fin-p{border:1px solid #999;border-radius:6px;padding:6px 10px 8px;break-inside:avoid}
.fin-p>p{margin:0 0 4px}
.fin-l{display:flex;gap:8px;align-items:baseline;margin-top:5px;font-size:14px}
.fin-l>span:first-child{min-width:6.5em;color:#333}
.fin-work{height:.55in}
.fin-row{display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start}
.fin-row>div{flex:1;min-width:220px}
.fin-stub{border:2px solid #222;border-radius:6px;padding:8px 12px;break-inside:avoid}
.fin-stub-h{display:flex;flex-wrap:wrap;gap:4px 22px;font-size:14px;margin-bottom:4px}
.fin-tag{display:inline-block;border:1.5px solid #222;border-radius:50%;width:1.35em;height:1.35em;line-height:1.3em;text-align:center;font-size:12px;margin-right:3px}
.fin-note{font-size:12.5px;color:#444;margin:4px 0 0}
.fin-list{margin:4px 0 8px 1.2em;padding:0}
.fin-labels{line-height:2.2}
@media print{.fin-ps{gap:6px 14px}.fin-work{height:.45in}}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '7' },
    { id: 'area', label: 'Area', type: 'select', options: v => areasFor(+v.grade), def: 'save' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => skillsFor(v.area, +v.grade).map(([id, s]) => [id, s.label]), def: 'simple' },
    { id: 'count', label: 'Length', type: 'select', def: 'm', show: v => !!(curSkill(v) && curSkill(v).count),
      options: v => { const s = curSkill(v), c = s && s.count; const word = { costs: 'lines', unit: 'pairs', tax: 'purchases', pct: 'problems', simple: 'problems', compound: 'problems', loan: 'problems', pay: 'workers', net: 'workers',
        taxret: 'people', svc: 'years', freq: 'savers', apy: 'accounts', deposits: 'savers', goal: 'goals', infl: 'workers', index: 'years', amort: 'rows', log: 'entries', pctchg: 'companies', margin: 'investors', shift: 'events', double: 'scenarios', elastic: 'goods', exchange: 'items', gdp: 'items' }[v.skill] || 'items';
        return c ? [['s', `Fewer (${c[0]} ${word})`], ['m', `Standard (${c[1]} ${word})`], ['l', `More (${c[2]} ${word})`]] : [['s', 'Fewer'], ['m', 'Standard'], ['l', 'More']]; } },
    { id: 'ctx', label: 'Budget plan', type: 'select', def: 'any', show: v => v.skill === 'costs' && v.area === 'spend',
      options: v => [['any', 'Any plan (a different one each sheet)'], ...ctxFor(+v.grade).map(([k, c]) => [k, c.label])] },
    { id: 'ins', label: 'Insurance', type: 'select', def: 'any', show: v => v.skill === 'insure' && v.area === 'risk',
      options: v => [['any', 'Any kind'], ['bike', 'E-bike: warranty, insurance or repair fund'], ['renters', 'Renters insurance'], ...(+v.grade >= 9 ? [['health', 'Health plans']] : [])] },
    { id: 'own', label: 'Compare', type: 'select', def: 'any', show: v => v.skill === 'own' && v.area === 'risk',
      options: [['any', 'Any (a different one each sheet)'], ['commute', 'E-bike, bus pass or used car'], ['lights', 'LED or tungsten stage lights'], ['printer', 'Cheap printer or cheap ink']] },
    { id: 'market', label: 'Market', type: 'select', def: 'goods', show: v => ['demand', 'supply', 'sd'].includes(v.skill) && v.area === 'econ',
      options: [['goods', 'Goods (rentals, coffee, tickets, pizza)'], ['labor', 'Labor (workers and wages)']] },
    { id: 'graph', label: 'Add a bar graph to draw', type: 'check', def: true, show: v => (v.skill === 'costs' && +v.grade >= 6) || v.skill === 'grid' },
  ],
  make(v, r) {
    const g = +v.grade, s = curSkill(v) || SK[skillsFor(v.area, g)[0][0]], id = Object.keys(SK).find(k => SK[k] === s);
    const n = s.count ? s.count[{ s: 0, m: 1, l: 2 }[v.count] ?? 1] : 0;
    let sh = null;
    for (let t = 0; t < 60 && !sh; t++) sh = s.make(v, r, g, n);
    if (!sh) throw new Error(`finance: ${id} could not make a sheet`);
    const gl = `Grade ${g}`;
    return {
      title: sh.title || `${s.label}: ${gl}`, level: gl, eyebrow: s.area === 'econ' ? 'Economics' : 'Money and Finance',
      ican: sh.ican, directions: sh.directions, parts: sh.parts, items: sh.items,
      minutes: sh.minutes || (sh.items.length > 30 ? 40 : 30), materials: sh.materials || 'pencil, calculator',
      mistakes: sh.mistakes, notes: (sh.notes || '') + ' Press New sheet for new numbers and names at the same settings.',
    };
  },
  verify(sheet) {
    const out = [];
    for (const it of sheet.items) {
      const f = VER[it.k];
      if (!f) { out.push(`${it.q}: no check for kind ${it.k}`); continue; }
      let want;
      try { want = String(f(it.p)); } catch (e) { out.push(`${it.q}: check crashed: ${e.message}`); continue; }
      if (want !== it.a) out.push(`${it.q.slice(0, 90)}: key says ${it.a}, check says ${want}`);
    }
    return out;
  },
});
})();
