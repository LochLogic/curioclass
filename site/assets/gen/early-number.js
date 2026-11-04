// Early Number generator, grades K-2: the pictures of early number sense, all drawn in SVG, with the answers in red on
// the key (class ws-ans, hidden on the student copy).
// Kindergarten: count objects in a row, a circle or scattered (K.CC.4-5), ten frames and how many more make 10 (K.OA.4),
// teen numbers as ten and some more (K.NBT.1), more, fewer or the same and the greater number (K.CC.6-7), trace and
// write numbers 0 to 20 with optional number words (K.CC.3), count on from any number (K.CC.2), number lines with just
// before and just after (K.CC.4), number bonds (K.OA.3) and longer or shorter (K.MD.2).
// Grade 1: make a ten to add with double ten frames (1.OA.6), count on to 120 and number lines (1.NBT.1), tens and ones
// blocks to read, draw or show two ways (1.NBT.2), tens and ones in expanded form (1.NBT.2), compare with >, < and =
// (1.NBT.3), 10 more and 10 less in a table or on 120 chart pieces (1.NBT.5), time to the hour and half hour (1.MD.3),
// measure with cubes or paper clips and order three by length (1.MD.1-2).
// Grade 2: hundreds, tens and ones blocks (2.NBT.1), standard, word and expanded form (2.NBT.3), compare and order
// three-digit numbers (2.NBT.4), 10 or 100 more or less (2.NBT.8), skip count by 5s, 10s and 100s (2.NBT.2), number
// lines to 1,000 (2.MD.6), time to five minutes (2.MD.7), coins (2.MD.8), inches and centimeters with a drawn ruler and
// how much longer (2.MD.1-2, 2.MD.4), odd and even (2.OA.3) and arrays (2.OA.4).
// Coins are labeled circles at their true relative sizes, never photos. Every ruler is drawn under its line, so a
// printer that scales the page cannot change an answer. Kindergarten sheets fit one page and use very few words.
(() => {
const H = Gen.h, { part, example, fill, blank, esc } = H;
const { fmt } = Gen.m;
const RED = '#b03020', INK = '#222';
const F = 'font-family="Helvetica, Arial, sans-serif"';
const nf = x => String(Math.round(x * 10) / 10);
const show = n => fmt(n, 0);
const svgw = (w, h, body, label, inches) => `<svg class="gen-svg" viewBox="0 0 ${nf(w)} ${nf(h)}" role="img" aria-label="${esc(label)}" style="max-width:${(inches || w / 96).toFixed(2)}in">${body}</svg>`;
const keyg = body => `<g class="ws-ans">${body}</g>`;
const txt = (x, y, s, size = 12, more = '') => `<text x="${nf(x)}" y="${nf(y)}" ${F} font-size="${size}" text-anchor="middle"${more ? ' ' + more : ''}>${esc(s)}</text>`;
const pad2 = m => String(m).padStart(2, '0');
const cells = (arr, cols, start = 1) => `<div class="en-cells" style="--c:${cols}">${arr.map((h, i) => `<div class="en-cell"><span class="ws-num">${i + start}.</span><div>${h}</div></div>`).join('')}</div>`;
const lineRows = arr => arr.map((h, i) => `<div class="en-line"><span class="ws-num">${i + 1}.</span><div>${h}</div></div>`).join('');

/* ---------- settings ---------- */
const GRADES = [['k', 'Kindergarten'], ['1', 'Grade 1'], ['2', 'Grade 2']];
const SKILLS = {
  k: [['count', 'Count and write how many'], ['tenframe', 'Ten frames: how many, and how many more make 10'], ['teen', 'Teen numbers: ten and some more'],
    ['compare', 'More, fewer or the same'], ['trace', 'Trace and write numbers'], ['seq', 'Count on: what comes next'], ['numline', 'Number lines'],
    ['bonds', 'Number bonds: two parts of a number'], ['length', 'Longer or shorter']],
  1: [['blocks', 'Tens and ones blocks'], ['maketen', 'Make a ten to add (double ten frames)'], ['seq', 'Count on to 120'], ['numline', 'Number lines to 120'],
    ['expanded', 'Tens and ones: expanded form'], ['compare', 'Compare numbers with >, < and ='], ['tenmore', '10 more and 10 less'],
    ['clock', 'Tell time to the hour and half hour'], ['length', 'Measure and order lengths']],
  2: [['blocks', 'Hundreds, tens and ones blocks'], ['expanded', 'Standard, word and expanded form'], ['compare', 'Compare and order three-digit numbers'],
    ['tenmore', '10 and 100 more or less'], ['seq', 'Skip count by 5s, 10s and 100s'], ['numline', 'Number lines to 1,000'], ['clock', 'Tell time to five minutes'],
    ['coins', 'Coins'], ['length', 'Measure in inches and centimeters'], ['evenodd', 'Odd and even'], ['arrays', 'Arrays and repeated addition']],
};
function tasks(v) {
  const g = v.grade;
  switch (v.skill) {
    case 'count': return [['write', 'Write how many'], ['circle', 'Circle the number (three choices)']];
    case 'compare': return g === 'k' ? [['more', 'Circle the group with more'], ['fewer', 'Circle the group with fewer'], ['num', 'Circle the greater number']]
      : g === '1' ? [['num', 'Two-digit numbers'], ['pics', 'Numbers to 20 with ten frame pictures']] : [['pairs', 'Compare pairs'], ['order', 'Compare pairs, then order sets of four']];
    case 'seq': return [['next', 'Write the next numbers'], ['missing', 'Fill in the missing numbers']];
    case 'blocks': return g === '1' ? [['mix', 'Read and draw'], ['read', 'Read the blocks'], ['draw', 'Draw the blocks'], ['two', 'Show a number two ways']]
      : [['mix', 'Read and draw'], ['read', 'Read the blocks'], ['draw', 'Draw the blocks']];
    case 'tenmore': return g === '1' ? [['table', '10 less and 10 more table'], ['chart', '120 chart pieces']] : [['table', '10 and 100 more or less table']];
    case 'clock': return g === '1' ? [['mix', 'Read and draw'], ['read', 'Read the clock'], ['draw', 'Draw both hands'], ['hour', 'Draw the hour hand']]
      : [['mix', 'Read and draw'], ['read', 'Read the clock'], ['draw', 'Draw both hands']];
    case 'coins': return [['count', 'Count the coins'], ['buy', 'Count, then decide: buy now or save?'], ['make', 'Show an amount three ways']];
    case 'length': return g === 'k' ? [['longer', 'Circle the longer one'], ['shorter', 'Circle the shorter one']]
      : g === '1' ? [['cubes', 'Measure with cubes'], ['clips', 'Measure with paper clips'], ['order', 'Order three by length']]
      : [['in', 'Inches'], ['cm', 'Centimeters'], ['both', 'Inches and centimeters'], ['diff', 'How much longer? (centimeters)']];
    case 'evenodd': return [['pairs', 'Pair up pictures: odd or even?'], ['doubles', 'Even numbers as doubles']];
    case 'arrays': return [['read', 'Write equations for arrays'], ['draw', 'Draw arrays, then write equations']];
  }
  return [['all', 'All']];
}
function ranges(v) {
  if (v.grade === 'k') return {
    count: [['5', '1 to 5'], ['10', '1 to 10'], ['20', '1 to 20']], trace: [['5', '1 to 5'], ['10', '0 to 10'], ['20', '0 to 20']],
    compare: [['5', 'Up to 5'], ['10', 'Up to 10']], numline: [['10', '0 to 10'], ['20', '0 to 20']], seq: [['20', 'Within 20'], ['100', 'Within 100']],
  }[v.skill] || [['10', '1 to 10']];
  if (v.grade === '1') return [['100', 'Within 100'], ['120', 'Past 100, up to 120']];
  return [['10', '1 to 10']];
}
const hasRange = v => (v.grade === 'k' && ['count', 'trace', 'compare', 'numline', 'seq'].includes(v.skill)) || (v.grade === '1' && ['seq', 'numline'].includes(v.skill));
const hasTask = v => tasks(v).length > 1;
const taskOf = v => tasks(v).some(t => t[0] === v.task) ? v.task : tasks(v)[0][0];
const hasFrames = v => (v.skill === 'compare' && v.grade !== 'k') || (v.skill === 'length' && v.grade === '1' && taskOf(v) !== 'order');
function plan(v) {
  const g = v.grade, s = v.skill, t = taskOf(v), i = { s: 0, m: 1, l: 2 }[v.count] ?? 1;
  const P = (a, b, c) => [a, b, c][i];
  switch (s) {
    case 'count': case 'tenframe': return P(6, 8, 10);
    case 'teen': return P(4, 6, 8);
    case 'compare': return g === 'k' ? (t === 'num' ? P(6, 9, 12) : P(4, 6, 8)) : g === '1' ? (t === 'pics' ? P(4, 6, 8) : P(9, 12, 15)) : P(8, 10, 12);
    case 'trace': return P(5, 8, 10);
    case 'seq': return g === 'k' ? P(6, 8, 10) : P(8, 10, 12);
    case 'numline': return g === 'k' ? P(2, 3, 4) : P(3, 4, 5);
    case 'bonds': return P(4, 6, 8);
    case 'length': return g === 'k' ? P(4, 6, 8) : g === '1' ? (t === 'order' ? P(3, 4, 6) : P(4, 6, 8)) : t === 'diff' ? P(3, 5, 6) : t === 'both' ? P(4, 5, 6) : P(4, 6, 8);
    case 'maketen': return P(6, 8, 10);
    case 'blocks': return g === '1' ? P(6, 8, 10) : P(4, 6, 8);
    case 'expanded': return g === '1' ? P(9, 12, 15) : P(6, 8, 10);
    case 'tenmore': return t === 'chart' ? P(4, 8, 12) : P(6, 8, 10);
    case 'clock': return g === '1' ? P(6, 8, 12) : P(8, 12, 16);
    case 'coins': return t === 'make' ? P(3, 4, 5) : t === 'buy' ? P(4, 6, 8) : P(6, 8, 10);
    case 'evenodd': return P(6, 8, 10);
    case 'arrays': return P(4, 6, 8);
  }
  return P(6, 8, 10);
}

/* ---------- number words ---------- */
const ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
  'sixteen', 'seventeen', 'eighteen', 'nineteen'];
const TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
const words = n => n < 20 ? ONES[n] : n < 100 ? TENS[Math.floor(n / 10)] + (n % 10 ? '-' + ONES[n % 10] : '')
  : ONES[Math.floor(n / 100)] + ' hundred' + (n % 100 ? ' ' + words(n % 100) : '');

/* ---------- drawing: shapes, ten frames, objects, blocks, clocks, coins, rulers ---------- */
const KINDS = ['dot', 'star', 'square', 'tri', 'heart', 'ring'];
function shape(k, x, y, s, color = INK) {
  const h = s / 2, st = `stroke="${color}" stroke-width="1.6"`, fl = color === INK ? '#e4e4e4' : '#fbe9e6';
  if (k === 'dot') return `<circle cx="${nf(x)}" cy="${nf(y)}" r="${nf(h * .82)}" fill="${color}"/>`;
  if (k === 'ring') return `<circle cx="${nf(x)}" cy="${nf(y)}" r="${nf(h * .8)}" fill="#fff" ${st}/>`;
  if (k === 'square') return `<rect x="${nf(x - h * .78)}" y="${nf(y - h * .78)}" width="${nf(h * 1.56)}" height="${nf(h * 1.56)}" fill="${fl}" ${st}/>`;
  if (k === 'tri') return `<polygon points="${nf(x)},${nf(y - h * .9)} ${nf(x + h * .92)},${nf(y + h * .75)} ${nf(x - h * .92)},${nf(y + h * .75)}" fill="${fl}" ${st} stroke-linejoin="round"/>`;
  if (k === 'star') {
    const p = [];
    for (let i = 0; i < 10; i++) { const a = Math.PI * i / 5 - Math.PI / 2, rr = i % 2 ? h * .42 : h * .98; p.push(`${nf(x + rr * Math.cos(a))},${nf(y + rr * Math.sin(a))}`); }
    return `<polygon points="${p.join(' ')}" fill="${fl}" ${st} stroke-linejoin="round"/>`;
  }
  return `<path d="M${nf(x)} ${nf(y + h * .8)} C${nf(x - h * 1.3)} ${nf(y - h * .1)} ${nf(x - h * .5)} ${nf(y - h)} ${nf(x)} ${nf(y - h * .35)} C${nf(x + h * .5)} ${nf(y - h)} ${nf(x + h * 1.3)} ${nf(y - h * .1)} ${nf(x)} ${nf(y + h * .8)}Z" fill="${fl}" ${st}/>`;
}
// n spots for shapes of size s in a w by h box: in a row (two rows past 10), in a circle, or scattered
function arrange(r, n, w, h, s, how) {
  const gap = s * 1.3;
  const rows = () => {
    const per = n <= 7 ? n : n <= 10 ? 5 : n <= 14 ? 7 : 10, nr = Math.ceil(n / per);
    const dx = Math.min(gap, (w - s) / Math.max(1, per - 1)), dy = Math.min(gap, (h - s) / Math.max(1, nr - 1));
    const x0 = (w - dx * (per - 1)) / 2, y0 = (h - dy * (nr - 1)) / 2;
    return Array.from({ length: n }, (_, i) => [x0 + (i % per) * dx, y0 + Math.floor(i / per) * dy]);
  };
  if (how === 'row' || n < 3) return rows();
  if (how === 'ring' && n <= 12) {
    const R = Math.min(h / 2 - s * .6, Math.max(s * .9, n * gap / (2 * Math.PI)));
    return Array.from({ length: n }, (_, i) => { const t = 2 * Math.PI * i / n - Math.PI / 2; return [w / 2 + R * Math.cos(t), h / 2 + R * Math.sin(t)]; });
  }
  for (let t = 0; t < 30; t++) {   // scattered: random spots at least a shape apart
    const pts = [];
    for (let k = 0; k < 300 && pts.length < n; k++) {
      const p = [s * .85 + r.next() * (w - 1.7 * s), s * .85 + r.next() * (h - 1.7 * s)];
      if (pts.every(q => Math.hypot(p[0] - q[0], p[1] - q[1]) >= s * 1.2)) pts.push(p);
    }
    if (pts.length === n) return pts;
  }
  return rows();
}
const sizeFor = n => n <= 6 ? 24 : n <= 10 ? 20 : 15;
// a ten frame at (x, y) with cells c: filled dots first, then hollow ones
function frame(x, y, c, filled, hollow = 0, color = INK) {
  let b = `<rect x="${nf(x)}" y="${nf(y)}" width="${nf(5 * c)}" height="${nf(2 * c)}" fill="#fff" stroke="${color}" stroke-width="2"/>`;
  for (let i = 1; i < 5; i++) b += `<line x1="${nf(x + i * c)}" y1="${nf(y)}" x2="${nf(x + i * c)}" y2="${nf(y + 2 * c)}" stroke="${color}" stroke-width="1.2"/>`;
  b += `<line x1="${nf(x)}" y1="${nf(y + c)}" x2="${nf(x + 5 * c)}" y2="${nf(y + c)}" stroke="${color}" stroke-width="1.2"/>`;
  for (let i = 0; i < filled + hollow; i++) {
    const cx = x + (i % 5 + .5) * c, cy = y + (Math.floor(i / 5) + .5) * c;
    b += i < filled ? `<circle cx="${nf(cx)}" cy="${nf(cy)}" r="${nf(c * .34)}" fill="${color}"/>`
      : `<circle cx="${nf(cx)}" cy="${nf(cy)}" r="${nf(c * .32)}" fill="#fff" stroke="${color}" stroke-width="1.6"/>`;
  }
  return b;
}
// long thin things, drawn from x to exactly x + len, centered on y
const OBJECTS = ['pencil', 'crayon', 'straw', 'marker', 'stick', 'ribbon'];
function obj(kind, x, y, len) {
  const st = `stroke="${INK}" stroke-width="1.5"`, e = x + len;
  if (kind === 'pencil') return `<rect x="${nf(x)}" y="${nf(y - 6)}" width="9" height="12" fill="#cfcfcf" ${st}/><rect x="${nf(x + 9)}" y="${nf(y - 6)}" width="${nf(len - 24)}" height="12" fill="#fff" ${st}/>` +
    `<line x1="${nf(x + 9)}" y1="${nf(y)}" x2="${nf(e - 15)}" y2="${nf(y)}" stroke="#999" stroke-width=".8"/><polygon points="${nf(e - 15)},${nf(y - 6)} ${nf(e)},${nf(y)} ${nf(e - 15)},${nf(y + 6)}" fill="#f1e2c9" ${st} stroke-linejoin="round"/>` +
    `<polygon points="${nf(e - 5)},${nf(y - 2)} ${nf(e)},${nf(y)} ${nf(e - 5)},${nf(y + 2)}" fill="${INK}"/>`;
  if (kind === 'crayon') return `<rect x="${nf(x)}" y="${nf(y - 7)}" width="${nf(len - 11)}" height="14" rx="3" fill="#ddd" ${st}/><line x1="${nf(x + 8)}" y1="${nf(y - 7)}" x2="${nf(x + 8)}" y2="${nf(y + 7)}" ${st}/>` +
    `<line x1="${nf(e - 22)}" y1="${nf(y - 7)}" x2="${nf(e - 22)}" y2="${nf(y + 7)}" ${st}/><polygon points="${nf(e - 11)},${nf(y - 5)} ${nf(e)},${nf(y - 2)} ${nf(e)},${nf(y + 2)} ${nf(e - 11)},${nf(y + 5)}" fill="#bbb" ${st} stroke-linejoin="round"/>`;
  if (kind === 'straw') { let b = `<rect x="${nf(x)}" y="${nf(y - 4)}" width="${nf(len)}" height="8" fill="#fff" ${st}/>`; for (let s = x + 8; s < e - 6; s += 10) b += `<line x1="${nf(s)}" y1="${nf(y + 4)}" x2="${nf(s + 5)}" y2="${nf(y - 4)}" stroke="${INK}" stroke-width="1"/>`; return b; }
  if (kind === 'marker') return `<rect x="${nf(x)}" y="${nf(y - 8)}" width="${nf(len * .62)}" height="16" rx="4" fill="#fff" ${st}/><rect x="${nf(x + len * .62)}" y="${nf(y - 9)}" width="${nf(len * .38 - 6)}" height="18" rx="4" fill="#bbb" ${st}/>` +
    `<rect x="${nf(e - 6)}" y="${nf(y - 3)}" width="6" height="6" fill="${INK}"/>`;
  if (kind === 'stick') return `<line x1="${nf(x + 3)}" y1="${nf(y)}" x2="${nf(e - 3)}" y2="${nf(y)}" stroke="#6b6b6b" stroke-width="6" stroke-linecap="round"/>` +
    `<line x1="${nf(x + len * .55)}" y1="${nf(y - 1)}" x2="${nf(x + len * .55 + 9)}" y2="${nf(y - 9)}" stroke="#6b6b6b" stroke-width="3" stroke-linecap="round"/>`;
  return `<polygon points="${nf(x)},${nf(y - 6)} ${nf(e)},${nf(y - 6)} ${nf(e - 6)},${nf(y)} ${nf(e)},${nf(y + 6)} ${nf(x)},${nf(y + 6)} ${nf(x + 6)},${nf(y)}" fill="#e2e2e2" ${st} stroke-linejoin="round"/>`;
}
// base-ten blocks: hundreds flats (perRow to a row), tens rods, ones cubes in columns of five; counts drawn come back too
function blocks(hn, tn, on, u, x0, y0, color = INK, perRow = 3) {
  const fl = color === INK ? '#f2f2f2' : '#fbe9e6', gap = u * .7, st = `stroke="${color}" stroke-width="1.3"`, thin = `stroke="${color === INK ? '#888' : color}" stroke-width=".6"`;
  let b = '', x = x0;
  const drawn = [0, 0, 0];
  for (let i = 0; i < hn; i++) {
    const fx = x + (i % perRow) * (10 * u + gap), fy = y0 + Math.floor(i / perRow) * (10 * u + gap);
    b += `<rect x="${nf(fx)}" y="${nf(fy)}" width="${nf(10 * u)}" height="${nf(10 * u)}" fill="${fl}" ${st}/>`;
    for (let k = 1; k < 10; k++) b += `<line x1="${nf(fx + k * u)}" y1="${nf(fy)}" x2="${nf(fx + k * u)}" y2="${nf(fy + 10 * u)}" ${thin}/><line x1="${nf(fx)}" y1="${nf(fy + k * u)}" x2="${nf(fx + 10 * u)}" y2="${nf(fy + k * u)}" ${thin}/>`;
    drawn[0]++;
  }
  if (hn) x += Math.min(hn, perRow) * (10 * u + gap) + gap;
  for (let i = 0; i < tn; i++) {
    const rx = x + i * (u + gap * .8);
    b += `<rect x="${nf(rx)}" y="${nf(y0)}" width="${nf(u)}" height="${nf(10 * u)}" fill="${fl}" ${st}/>`;
    for (let k = 1; k < 10; k++) b += `<line x1="${nf(rx)}" y1="${nf(y0 + k * u)}" x2="${nf(rx + u)}" y2="${nf(y0 + k * u)}" ${thin}/>`;
    drawn[1]++;
  }
  if (tn) x += tn * (u + gap * .8) + gap;
  for (let i = 0; i < on; i++) {
    b += `<rect x="${nf(x + Math.floor(i / 5) * (u + gap * .6))}" y="${nf(y0 + 10 * u - (i % 5 + 1) * (u + gap * .5) + gap * .5)}" width="${nf(u)}" height="${nf(u)}" fill="${fl}" ${st}/>`;
    drawn[2]++;
  }
  return { b, drawn };
}
// a clock face 100 by 100; black: the hands drawn for everyone ('h', 'm'), red: the hands drawn only on the key
const handAngles = (h, m) => [((h % 12) + m / 60) * 30, m * 6];
function hand(deg, len, width, color) {
  const a = deg * Math.PI / 180;
  return `<line x1="50" y1="50" x2="${nf(50 + len * Math.sin(a))}" y2="${nf(50 - len * Math.cos(a))}" stroke="${color}" stroke-width="${width}" stroke-linecap="round"/>`;
}
function clockSvg(h, m, black, red, fine) {
  let b = `<circle cx="50" cy="50" r="46" fill="#fff" stroke="${INK}" stroke-width="2.5"/>`;
  for (let i = 0; i < 60; i++) {
    const big = i % 5 === 0;
    if (!big && !fine) continue;
    const a = i * 6 * Math.PI / 180, r1 = big ? 40 : 43;
    b += `<line x1="${nf(50 + r1 * Math.sin(a))}" y1="${nf(50 - r1 * Math.cos(a))}" x2="${nf(50 + 45 * Math.sin(a))}" y2="${nf(50 - 45 * Math.cos(a))}" stroke="${INK}" stroke-width="${big ? 1.6 : .7}"/>`;
  }
  for (let k = 1; k <= 12; k++) { const a = k * 30 * Math.PI / 180; b += txt(50 + 33 * Math.sin(a), 50 - 33 * Math.cos(a) + 3.6, String(k), 10, 'font-weight="700"'); }
  const [ha, ma] = handAngles(h, m);
  const draw = (which, color) => (which.includes('m') ? hand(ma, 38, 2.2, color) : '') + (which.includes('h') ? hand(ha, 22, 4, color) : '');
  b += draw(black, INK);
  if (red) b += keyg(draw(red, RED));
  b += `<circle cx="50" cy="50" r="2.6" fill="${INK}"/>`;
  return { b, ha, ma };
}
const COIN = { q: { name: 'quarter', many: 'quarters', c: 25, mm: 24.26 }, d: { name: 'dime', many: 'dimes', c: 10, mm: 17.91 },
  n: { name: 'nickel', many: 'nickels', c: 5, mm: 21.21 }, p: { name: 'penny', many: 'pennies', c: 1, mm: 19.05 } };
function coin(x, y, k, both) {   // diameter in millimeters times 2.5, so the four coins keep their real relative sizes
  const c = COIN[k], R = c.mm * 1.25;
  return `<circle cx="${nf(x)}" cy="${nf(y)}" r="${nf(R)}" fill="${k === 'p' ? '#ead6c2' : '#e9e9e9'}" stroke="#444" stroke-width="1.5"/>` +
    `<circle cx="${nf(x)}" cy="${nf(y)}" r="${nf(R - 3)}" fill="none" stroke="#999" stroke-width=".7"/>` +
    (both ? txt(x, y - 1, c.name, 11, 'font-weight="700"') + txt(x, y + 12, `${c.c}¢`, 12) : txt(x, y + 4, c.name, 11, 'font-weight="700"'));
}
function coinRow(list, both, perRow = 4) {
  const D = 64;
  let b = '';
  list.forEach((k, i) => { b += coin(D / 2 + (i % perRow) * D, D / 2 + Math.floor(i / perRow) * D, k, both); });
  return { b, w: Math.min(list.length, perRow) * D, h: Math.ceil(list.length / perRow) * D };
}
const INCH = 96, CM = 96 / 2.54;
// a ruler whose 0 sits at x; units whole units long; ticks hang from the top edge at y
function ruler(x, y, units, unit) {
  const px = unit === 'in' ? INCH : CM, W = units * px, sub = unit === 'in' ? 4 : 10;
  let b = `<rect x="${nf(x - 10)}" y="${nf(y)}" width="${nf(W + 20)}" height="32" fill="#fff" stroke="${INK}" stroke-width="1.5" rx="2"/>`;
  for (let i = 0; i <= units * sub; i++) {
    const whole = i % sub === 0, half = unit === 'in' ? i % 2 === 0 : i % 5 === 0, len = whole ? 14 : half ? 9 : 5;
    b += `<line x1="${nf(x + i * px / sub)}" y1="${nf(y)}" x2="${nf(x + i * px / sub)}" y2="${nf(y + len)}" stroke="${INK}" stroke-width="${whole ? 1.4 : .8}"/>`;
    if (whole) b += txt(x + i * px / sub, y + 26, String(i / sub), 10.5);
  }
  b += `<text x="${nf(x - 14)}" y="${nf(y + 20)}" ${F} font-size="11" text-anchor="end" font-weight="700">${unit === 'in' ? 'inches' : 'cm'}</text>`;
  return b;
}
const bar = (x, y, len) => `<rect x="${nf(x)}" y="${nf(y - 4)}" width="${nf(len)}" height="8" fill="${INK}"/>`;

/* ---------- pieces used by several skills ---------- */
const symbol = (a, b) => a > b ? '>' : a < b ? '<' : '=';
const phrase = (a, b) => a > b ? 'greater than' : a < b ? 'less than' : 'equal to';
const symBox = s => `<span class="en-sym"><span class="ws-ans">${esc(s)}</span></span>`;
const chain = (vals, step) => `<div>${step ? `<p class="en-step">Count by ${step}s</p>` : ''}<div class="en-chain">${vals.map(x => `<span class="en-seg">${x}</span>`).join('')}</div></div>`;
function nline(ticks, W = 640) {
  const pad = 34, n = ticks.length, dx = (W - 2 * pad) / (n - 1), y = 22;
  let b = `<line x1="${pad - 20}" y1="${y}" x2="${W - pad + 20}" y2="${y}" stroke="${INK}" stroke-width="2"/>` +
    `<polygon points="${pad - 26},${y} ${pad - 16},${y - 5} ${pad - 16},${y + 5}" fill="${INK}"/><polygon points="${W - pad + 26},${y} ${W - pad + 16},${y - 5} ${W - pad + 16},${y + 5}" fill="${INK}"/>`;
  ticks.forEach((t, i) => {
    const x = pad + i * dx;
    b += `<line x1="${nf(x)}" y1="${y - 8}" x2="${nf(x)}" y2="${y + 8}" stroke="${INK}" stroke-width="1.6"/>`;
    if (t.mode === 'label') b += txt(x, y + 27, show(t.v), 13, 'font-weight="700"');
    if (t.mode === 'box') b += `<rect x="${nf(x - 21)}" y="${y + 12}" width="42" height="22" fill="#fff" stroke="${INK}" stroke-width="1.3" rx="3"/>` + keyg(txt(x, y + 28, show(t.v), 13, `font-weight="700" fill="${RED}"`));
    if (t.mode === 'mark') b += keyg(`<circle cx="${nf(x)}" cy="${y}" r="5.5" fill="${RED}"/>`);
  });
  return b;
}

/* ---------- Kindergarten ---------- */
function skCount(v, r, n) {
  const hi = +v.range, task = v.task;
  const list = r.distinct(n, () => ({ k: r.int(1, hi), kind: r.pick(KINDS), how: v.layout === 'mix' ? r.pick(['row', 'ring', 'scatter']) : v.layout }), x => `${x.k} ${x.kind} ${x.how}`);
  const items = [], html = [];
  for (const x of list) {
    const s = sizeFor(x.k), pts = arrange(r, x.k, 230, 100, s, x.how);
    const pic = svgw(230, 100, `<rect x="1" y="1" width="228" height="98" rx="8" fill="none" stroke="#bbb"/>` + pts.map(p => shape(x.kind, p[0], p[1], s)).join(''), 'A group of shapes to count', 2.2);
    const q = `${x.k} ${x.kind} in a ${x.how}`;
    if (task === 'circle') {
      const near = [1, -1, 2, -2, 3, -3, 4, -4].map(d => x.k + d).filter(z => z >= 1 && z <= Math.max(hi, 5));
      const opts = r.shuffle([x.k, ...r.sample(near.slice(0, 4), 2)]);
      html.push(`<div class="en-row">${pic}<div class="en-opts">${opts.map(o => `<span class="en-opt${o === x.k ? ' en-ok' : ''}">${o}</span>`).join('')}</div></div>`);
      items.push({ k: 'count', q, a: String(x.k), drawn: pts.length, opts });
    } else {
      html.push(`<div class="en-row">${pic}<div class="en-big">${blank(x.k, 2.6)}</div></div>`);
      items.push({ k: 'count', q, a: String(x.k), drawn: pts.length });
    }
  }
  return { body: cells(html, 2), items, dirs: task === 'circle' ? 'Count. Circle the number.' : 'Count. Write how many.',
    ican: 'I can count to tell how many.', mistakes: 'Counting a shape twice or skipping one. Touching or crossing out each shape while counting helps, most of all in the scattered groups.',
    notes: 'Groups come in a row, in a circle and scattered. The arrangement never changes how many, which is worth saying out loud after a circle group.' };
}
function skTenframe(v, r, n) {
  const list = r.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n), items = [], html = [];
  for (const k of list) {
    const pic = svgw(124, 52, frame(2, 2, 24, k), 'A ten frame with dots', 1.45);
    html.push(`<div class="en-row">${pic}<div class="en-k"><p>${blank(k, 1.8)}</p><p class="en-lab">To make 10: ${blank(10 - k, 1.8)}</p></div></div>`);
    items.push({ k: 'tf', q: `ten frame with ${k}`, a: `${k}; ${10 - k}`, drawn: k });
  }
  return { body: cells(html, 2), items, dirs: 'Count the dots. Write how many. How many more make 10?',
    ican: 'I can tell how many are in a ten frame and how many more make 10.',
    mistakes: 'Counting the empty boxes for "how many" instead of the dots. The dots and the empty boxes always make 10 together.',
    notes: 'Dots fill the top row first, left to right, the way most classrooms fill a ten frame, so a full top row is 5 at a glance.' };
}
function skTeen(v, r, n) {
  const list = r.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], n), items = [], html = [];
  for (const k of list) {
    const pic = svgw(216, 44, frame(2, 2, 20, 10) + frame(114, 2, 20, k), 'Two ten frames with dots', 2.2);
    html.push(`${pic}<p class="en-k">10 + ${blank(k, 1.6)} = ${blank(10 + k, 2)}</p>`);
    items.push({ k: 'teen', q: `teen ${10 + k}`, a: `10 + ${k} = ${10 + k}`, f1: 10, f2: k });
  }
  return { body: cells(html, 2), items, dirs: 'Count the dots. Fill in 10 + ___.',
    ican: 'I can see a teen number as ten and some more.', mistakes: 'Counting every dot from 1 instead of starting at 10 for the full frame, or writing the number backward (61 for 16).',
    notes: 'The first frame is always full. Ask: how many in the full frame? How many more? Then read the number: ten and six more is sixteen.' };
}
function skCompareK(v, r, n) {
  const hi = +v.range, task = v.task, items = [], html = [];
  if (task === 'num') {
    const list = r.distinct(n, () => { const a = r.int(0, hi), b = r.int(0, hi); return a === b ? null : [a, b]; }, x => x.join(' '));
    for (const [a, b] of list) {
      html.push(`<div class="en-pair">${[a, b].map(x => `<span class="en-opt${x === Math.max(a, b) ? ' en-ok' : ''}">${x}</span>`).join('')}</div>`);
      items.push({ k: 'num2', q: `${a} or ${b}`, a: String(Math.max(a, b)), x: a, y: b });
    }
    return { body: cells(html, 3), items, dirs: 'Circle the bigger number.', ican: 'I can tell which number is greater.',
      mistakes: 'Picking the number that looks bigger on the page. Counting up from 0, or a number line, shows which one comes later.',
      notes: 'A number that comes later when we count is greater. A number line or counting cubes helps with any pair that causes trouble.' };
  }
  const list = r.distinct(n, () => { const a = r.int(1, hi), b = r.chance(.2) ? a : r.int(1, hi); return [a, b]; }, x => x.join(' '));
  if (list.length > 2 && !list.some(x => x[0] === x[1])) { const a = r.int(1, hi); list[r.int(0, list.length - 1)] = [a, a]; }
  for (const [a, b] of list) {
    const kind = r.pick(KINDS), s = hi <= 5 ? 20 : 16;
    const pa = arrange(r, a, 110, 80, s, r.pick(['row', 'scatter'])), pb = arrange(r, b, 110, 80, s, r.pick(['row', 'scatter']));
    const want = a === b ? 'same' : (task === 'fewer') === (a < b) ? 'first' : 'second';
    let body = `<rect x="2" y="2" width="110" height="80" rx="8" fill="none" stroke="#999"/><rect x="128" y="2" width="110" height="80" rx="8" fill="none" stroke="#999"/>`;
    body += pa.map(p => shape(kind, p[0] + 2, p[1] + 2, s)).join('') + pb.map(p => shape(kind, p[0] + 128, p[1] + 2, s)).join('');
    if (want !== 'same') body += keyg(`<rect x="${want === 'first' ? 0 : 126}" y="0" width="114" height="84" rx="10" fill="none" stroke="${RED}" stroke-width="3"/>`);
    html.push(svgw(240, 84, body, 'Two groups of shapes', 2.5) + `<p class="en-center"><span class="en-same${want === 'same' ? ' en-ok' : ''}">Same</span></p>`);
    items.push({ k: 'cmpk', q: `${a} and ${b}`, a: want, na: pa.length, nb: pb.length, ask: task });
  }
  return { body: cells(html, 2), items, dirs: task === 'fewer' ? 'Circle the group with fewer. If they are the same, circle Same.' : 'Circle the group with more. If they are the same, circle Same.',
    ican: 'I can tell which group has more, which has fewer, or if they are the same.',
    mistakes: 'Choosing the group that takes up more space. Matching one shape in each group with a line, or counting both groups, settles it.',
    notes: 'Some pairs are the same on purpose. Students can match shapes one to one with lines or count both groups.' };
}
function skTrace(v, r, n) {
  const hi = +v.range, lo = hi === 5 ? 1 : 0, pool = Array.from({ length: hi - lo + 1 }, (_, i) => lo + i);
  const list = r.sample(pool, Math.min(n, pool.length)).sort((a, b) => a - b), items = [], html = [], kind = r.pick(KINDS), wd = !!v.words;
  for (const k of list) {
    const s = k <= 10 ? 14 : 11, pts = arrange(r, k, 120, 70, s, r.pick(['row', 'scatter']));
    const dots = svgw(120, 70, `<rect x="1" y="1" width="118" height="68" rx="8" fill="none" stroke="#bbb"/>` + pts.map(p => shape(kind, p[0], p[1], s)).join(''), 'Shapes to count', 1.2);
    const W = wd ? 130 : 90, Ht = wd ? 98 : 70;
    let t = `<text x="${W / 2}" y="58" ${F} font-size="60" text-anchor="middle" fill="none" stroke="#888" stroke-width="1.3" stroke-dasharray="3 2.4">${k}</text>`;
    if (wd) t += `<text x="${W / 2}" y="92" ${F} font-size="${words(k).length > 7 ? 19 : 23}" text-anchor="middle" fill="#c4c4c4">${words(k)}</text>`;
    html.push(`<div class="en-row">${dots}${svgw(W, Ht, t, `The number ${k} to trace`, W / 96 * 1.05)}<div class="en-big">${blank(k, 2.6)}</div></div>`);
    items.push({ k: 'trace', q: `trace ${k}`, a: String(k), drawn: pts.length, word: wd ? words(k) : '' });
  }
  return { body: cells(html, 2), items, dirs: `Count. Trace the number${wd ? ' and the word' : ''}. Write it.`,
    ican: 'I can count and write the number.', mistakes: 'Writing a number backward (common with 2, 3, 5, 7 and 9), or starting the stroke at the bottom.',
    notes: `Numbers run in order so the sheet doubles as a counting line.${lo === 0 ? ' Zero shows an empty box: nothing to count.' : ''} Trace the gray outline, then write the number on the line.` };
}

/* ---------- counting on, number lines, before and after ---------- */
const stepFor = (v, r) => v.grade !== '2' ? 1 : v.by === 'mix' ? r.pick([5, 10, 100]) : +v.by;
function skSeq(v, r, n) {
  const g = v.grade, len = g === 'k' ? 5 : 6, items = [], rows = [];
  const runs = r.distinct(n, () => {
    const d = stepFor(v, r);
    let s;
    if (g === 'k') s = v.range === '20' ? r.int(0, 20 - (len - 1)) : r.int(1, 100 - (len - 1));
    else if (g === '1') s = v.range === '120' ? (r.chance(.5) ? r.int(100 - len + 1, 99) : r.int(100, 120 - (len - 1))) : r.int(1, 100 - (len - 1));
    else s = d === 5 ? 5 * r.int(0, (1000 - 5 * (len - 1)) / 5) : d === 10 ? r.int(1, 1000 - 10 * (len - 1)) : 10 * r.int(1, (1000 - 100 * (len - 1)) / 10);
    return { s, d };
  }, x => `${x.s} ${x.d}`);
  for (const { s, d } of runs) {
    const vals = Array.from({ length: len }, (_, i) => s + i * d);
    let hide;
    if (v.task === 'missing') hide = r.sample(Array.from({ length: len - 1 }, (_, i) => i + 1), g === 'k' ? 2 : r.int(2, 3)).sort((a, b) => a - b);
    else hide = Array.from({ length: g === 'k' ? len - 1 : len - 2 }, (_, i) => len - (g === 'k' ? len - 1 : len - 2) + i);
    rows.push(chain(vals.map((x, i) => hide.includes(i) ? blank(show(x), 1.8) : show(x)), g === '2' ? d : 0));
    items.push({ k: 'seq', q: `count by ${d} from ${s}`, a: hide.map(i => show(vals[i])).join(', '), vals, hide, d });
  }
  const body = `<div class="en-chains${g === 'k' ? ' en-k' : ''}">${rows.map((x, i) => `<div class="en-chainrow"><span class="ws-num">${i + 1}.</span>${x}</div>`).join('')}</div>`;
  const dirs = v.task === 'missing' ? 'Write the missing numbers.' : g === 'k' ? 'Count on. Write the next numbers.' : g === '1' ? 'Count on. Write the next four numbers.' : 'Skip count. Write the next four numbers.';
  return { body, items, dirs, ican: g === '2' ? 'I can skip count by 5s, 10s and 100s.' : g === '1' ? 'I can count on to 120, starting at any number.' : 'I can count on from any number.',
    ex: g === '2' ? example('Find the jump, then keep adding it.', 'By 10s: 347, 357, <b>367</b>, <b>377</b>. Only the tens digit changes, until it passes 9.')
      : g === '1' ? example('Say the numbers aloud as you write them.', '97, 98, <b>99</b>, <b>100</b>, <b>101</b>, <b>102</b>') : null,
    mistakes: g === '2' ? 'Changing the wrong digit when skip counting, or losing track when a count crosses a hundred (95, 100, 105).' : 'Going from 99 to 1000, or from 109 to 200. Say the numbers aloud: one hundred nine, one hundred ten.',
    notes: g === '1' && v.range === '120' ? 'About half the rows cross 100, where most mistakes happen.' : 'Saying the numbers aloud while writing them catches most slips.' };
}
function skNumline(v, r, n) {
  const g = v.grade, items = [], parts = [], rows = [];
  const lines = r.distinct(n, () => {
    const d = stepFor(v, r), T = d === 100 ? 9 : 11;
    let s;
    if (g === 'k') s = v.range === '10' ? 0 : r.int(0, 10);
    else if (g === '1') s = v.range === '120' ? r.int(90, 110) : r.int(0, 90);
    else s = d === 100 ? 100 * r.int(0, 2) : d === 10 ? 10 * r.int(0, 90) : 5 * r.int(0, 190);
    return { s, d, T, salt: g === 'k' && v.range === '10' ? r.int(0, 999) : 0 };
  }, x => `${x.s} ${x.d} ${x.salt}`);
  lines.forEach((ln, li) => {
    const { s, d, T } = ln, vals = Array.from({ length: T }, (_, i) => s + i * d);
    const inner = r.shuffle(Array.from({ length: T - 2 }, (_, i) => i + 1));
    const boxes = inner.slice(0, 4).sort((a, b) => a - b), marks = g === 'k' ? [] : inner.slice(4, 6).sort((a, b) => a - b);
    const ticks = vals.map((x, i) => ({ v: x, mode: boxes.includes(i) ? 'box' : marks.includes(i) ? 'mark' : 'label' }));
    const lab = `Number line ${li + 1}`;
    for (const i of boxes) items.push({ k: 'nlbox', q: `${lab}: box at tick ${i + 1}`, a: show(vals[i]), s, d, i });
    for (const i of marks) items.push({ k: 'nlmark', q: `${lab}: mark ${vals[i]}`, a: `dot at ${show(vals[i])}`, s, d, i, v: vals[i] });
    const markText = marks.length ? `<p class="en-mark">Mark ${marks.map(i => `<b>${show(vals[i])}</b>`).join(' and ')} with a dot.</p>` : '';
    rows.push(svgw(640, 62, nline(ticks), `Number line from ${show(vals[0])} to ${show(vals[T - 1])}`, 6.6) + markText);
  });
  parts.push(part('', lineRows(rows)));
  if (g !== '2') {   // just before and just after
    const hi = g === 'k' ? +v.range : v.range === '120' ? 120 : 100, lo = g === '1' && v.range === '120' ? 95 : 1;
    const ns = r.distinct(4, () => r.int(lo, hi - 1));
    const brows = ns.map(x => `<div class="en-chain"><span class="en-seg">${blank(x - 1, 1.6)}</span><span class="en-seg en-given">${x}</span><span class="en-seg">${blank(x + 1, 1.6)}</span></div>`);
    ns.forEach(x => items.push({ k: 'ba', q: `before and after ${x}`, a: `${x - 1}, ${x + 1}`, n: x }));
    parts.push(part(g === 'k' ? 'Before and after' : 'Just before and just after', `<div class="en-chains${g === 'k' ? ' en-k' : ''}">${brows.map((x, i) => `<div class="en-chainrow"><span class="ws-num">${lines.length + i + 1}.</span>${x}</div>`).join('')}</div>`));
  }
  const dirs = g === 'k' ? 'Write the missing numbers.' : `Write the missing number in each box. Then mark the numbers asked for with a dot.${g === '1' ? ' Last, write the numbers just before and just after.' : ''}`;
  return { parts, items, dirs, ican: g === '2' ? 'I can find and place numbers on a number line that counts by 5s, 10s or 100s.' : 'I can find and place numbers on a number line.',
    ex: g === '2' ? example('Find the jump between two labeled ticks first.', 'If the ticks go 300, 400, the jump is 100, so the next tick is <b>500</b>.')
      : g === '1' ? example('Each tick is one more than the tick before it.', '46, 47, <b>48</b>, 49. To mark 51, count two ticks past 49.') : null,
    mistakes: g === '2' ? 'Counting each tick as 1 when the line counts by 5s, 10s or 100s.' : 'Skipping a tick, or counting the first tick as 1 instead of the number printed under it.',
    notes: 'The first and last ticks are always labeled, so the jump between ticks can always be worked out.' + (g === '2' ? ' Lines that count by 100s have 9 ticks to stay within 1,000.' : '') + (g === 'k' ? ' Before and after: the number in the gray circle is given.' : '') };
}
function skBonds(v, r, n) {
  const fixed = v.whole !== 'mix', items = [], html = [];
  let list;
  if (fixed) { const N = +v.whole; list = r.shuffle(Array.from({ length: N + 1 }, (_, k) => [N, k])).slice(0, n); }
  else list = r.distinct(n, () => { const N = r.int(2, 10); return [N, r.int(1, N - 1)]; }, x => x.join(' '));
  for (const [N, k] of list) {
    const sp = 22, x0 = (230 - sp * (N - 1)) / 2;
    let b = '';
    for (let i = 0; i < N; i++) b += i < k ? `<circle cx="${nf(x0 + i * sp)}" cy="16" r="8.5" fill="${INK}"/>` : `<circle cx="${nf(x0 + i * sp)}" cy="16" r="8" fill="#fff" stroke="${INK}" stroke-width="1.8"/>`;
    b += `<line x1="115" y1="58" x2="72" y2="96" stroke="${INK}" stroke-width="1.6"/><line x1="115" y1="58" x2="158" y2="96" stroke="${INK}" stroke-width="1.6"/>`;
    b += `<circle cx="115" cy="54" r="18" fill="#fff" stroke="${INK}" stroke-width="2"/>` + txt(115, 61, String(N), 20, 'font-weight="700"');
    b += `<circle cx="70" cy="100" r="18" fill="#fff" stroke="${INK}" stroke-width="2"/><circle cx="160" cy="100" r="18" fill="#fff" stroke="${INK}" stroke-width="2"/>`;
    b += keyg(txt(70, 107, String(k), 20, `font-weight="700" fill="${RED}"`) + txt(160, 107, String(N - k), 20, `font-weight="700" fill="${RED}"`));
    html.push(svgw(230, 122, b, `${N} dots and a number bond`, 2.3));
    items.push({ k: 'bond', q: `${N} split ${k} and ${N - k}`, a: `${k} and ${N - k}`, N, dark: k, light: N - k });
  }
  return { body: cells(html, 2), items, dirs: 'Count the dark dots and the white dots. Write the two parts.',
    ican: fixed ? `I can find ways to make ${v.whole}.` : 'I can break a number into two parts.',
    mistakes: 'Writing the whole again in a part circle, or counting all the dots for one part.',
    notes: (fixed ? `Every way to make ${v.whole} appears once when the sheet is long enough, including 0 and ${v.whole}. Putting the bonds in order afterward shows the pattern.` : 'Wholes run from 2 to 10.') + ' The left part is the dark dots and the right part the white dots.' };
}
function skLengthK(v, r, n) {
  const shorter = v.task === 'shorter', items = [], html = [];
  const list = r.distinct(n, () => {
    const a = r.int(60, 270), b = r.int(60, 270);
    if (Math.abs(a - b) < Math.max(30, .22 * Math.min(a, b))) return null;
    const [ka, kb] = r.sample(OBJECTS, 2);
    return { a, b, ka, kb };
  }, x => `${x.ka}${x.a} ${x.kb}${x.b}`);
  for (const { a, b, ka, kb } of list) {
    const top = (a < b) === shorter, y = top ? 22 : 64, len = top ? a : b;
    let body = `<line x1="10" y1="4" x2="10" y2="82" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>` + obj(ka, 10, 22, a) + obj(kb, 10, 64, b);
    body += keyg(`<rect x="3" y="${y - 15}" width="${nf(len + 14)}" height="30" rx="14" fill="none" stroke="${RED}" stroke-width="2.8"/>`);
    html.push(svgw(300, 86, body, `A ${ka} and a ${kb}`, 3.1));
    items.push({ k: 'lenk', q: `${ka} ${a} and ${kb} ${b}`, a: top ? 'top' : 'bottom', la: a, lb: b, ask: v.task });
  }
  return { body: cells(html, 2), items, dirs: shorter ? 'Circle the shorter one.' : 'Circle the longer one.',
    ican: 'I can compare two things to see which is longer or shorter.',
    mistakes: 'Judging by thickness, or by which one looks bigger. Both start at the same line, so look at the ends on the right.',
    notes: 'Both objects start at the dotted line, the way students should line things up to compare. Ask how they know.' };
}

/* ---------- Grade 1 ---------- */
function skMaketen(v, r, n) {
  const items = [], html = [];
  const list = r.distinct(n, () => { const a = r.int(6, 9), b = r.int(2, 9); return a + b > 10 ? [a, b] : null; }, x => x.join(' '));
  for (const [a, b] of list) {
    const need = 10 - a, rest = b - need;
    const pic = svgw(236, 50, frame(2, 2, 22, a) + frame(122, 2, 22, 0, b), 'Two ten frames: dark dots and white dots', 2.4);
    html.push(`${pic}<p class="en-eq">${a} + ${b} = ${a} + ${blank(need, 1.6)} + ${blank(rest, 1.6)} = ${blank(a + b, 2)}</p>`);
    items.push({ k: 'maketen', q: `${a} + ${b}`, a: `${a} + ${need} + ${rest} = ${a + b}`, x: a, y: b, need, rest, sum: a + b });
  }
  return { body: cells(html, 2), items, ex: example('8 + 5: move 2 white dots to fill the first frame. 8 + 2 = 10, and 3 white dots are left.', '8 + 5 = 8 + <b>2</b> + <b>3</b> = <b>13</b>'),
    dirs: 'Fill the first ten frame with white dots from the second. Write how many you moved, how many are left, and the sum.',
    ican: 'I can make a ten to add.', mistakes: 'Splitting the second number into the wrong parts. The first part is always what fills the frame to 10.',
    notes: 'Dark dots are the first number and white dots the second. Students can cross out the white dots they move and draw them in the first frame.' };
}
function skBlocks(v, r, n) {
  const g = v.grade, two = g === '2', items = [], html = [], task = v.task;
  const list = r.distinct(n, () => {
    if (!two) { const t = task === 'two' ? r.int(2, 9) : r.int(1, 9); return t * 10 + r.int(0, 9); }
    return 100 * r.int(1, 9) + 10 * (r.chance(.3) ? 0 : r.int(0, 9)) + r.int(0, 9);
  });
  if (two && list.length && !list.some(x => Math.floor(x / 10) % 10 === 0)) { const i = r.int(0, list.length - 1), x = list[i] - (Math.floor(list[i] / 10) % 10) * 10; if (!list.includes(x)) list[i] = x; }
  const u = two ? 5 : 8, W = two ? 290 : 170, Ht = two ? 3 * 50 + 2 * 3.5 + 6 : 86;
  const box = () => `<rect x="1" y="1" width="${W - 2}" height="${Ht + 4}" rx="6" fill="none" stroke="#555" stroke-width="1.2" stroke-dasharray="5 4"/>`;
  list.forEach((num, i) => {
    const hh = Math.floor(num / 100), t = Math.floor(num / 10) % 10, o = num % 10;
    const mode = task === 'mix' ? (i % 2 ? 'draw' : 'read') : task;
    const chart = two ? `${blank(hh, 1.4)} hundreds ${blank(t, 1.4)} tens ${blank(o, 1.4)} ones` : `${blank(t, 1.4)} tens ${blank(o, 1.4)} ones`;
    const ans = `${two ? hh + ' hundreds ' : ''}${t} tens ${o} ones`;
    if (mode === 'read') {
      const bl = blocks(hh, t, o, u, 3, 3, INK);
      html.push(svgw(W, Ht, bl.b, 'Base-ten blocks', W / 96) + `<p>${chart}</p><p>The number is ${blank(show(num), 2.6)}</p>`);
      items.push({ k: 'blocks', q: `read ${num}`, a: `${ans} = ${num}`, num, drawn: bl.drawn });
    } else if (mode === 'draw') {
      const bl = blocks(hh, t, o, u, 6, 6, RED);
      html.push(`<p>Draw <b>${show(num)}</b>.</p>` + svgw(W, Ht + 6, box() + keyg(bl.b), 'A box to draw base-ten blocks', W / 96) + `<p>${chart}</p>`);
      items.push({ k: 'blocks', q: `draw ${num}`, a: ans, num, drawn: bl.drawn });
    } else {   // two ways: t tens o ones, and t - 1 tens o + 10 ones
      const bl = blocks(0, t - 1, o + 10, u, 6, 6, RED);
      html.push(`<p><b>${num}</b> = ${blank(t, 1.4)} tens ${blank(o, 1.4)} ones</p><p><b>${num}</b> = ${t - 1} tens ${blank(o + 10, 1.6)} ones</p>` +
        svgw(W, Ht + 6, box() + keyg(bl.b), 'A box to draw base-ten blocks', W / 96));
      items.push({ k: 'two', q: `two ways ${num}`, a: `${t} tens ${o} ones; ${t - 1} tens ${o + 10} ones`, num, t, o, t2: t - 1, o2: o + 10, drawn: bl.drawn });
    }
  });
  const dirs = task === 'two' ? 'Write each number as tens and ones. Then show it another way, with one ten traded for 10 ones, and draw that way in the box.'
    : task === 'draw' ? `Draw each number with ${two ? 'hundreds flats, ' : ''}tens rods and ones cubes. Fill in the ${two ? 'hundreds, ' : ''}tens and ones.`
    : task === 'read' ? `Count the ${two ? 'hundreds, ' : ''}tens and ones. Write the number.` : 'Read the blocks and write the number. Draw blocks for the numbers given.';
  const ex = two ? example('A flat is 100, a rod is 10 and a cube is 1.', '2 flats, 0 rods and 6 cubes: 2 hundreds 0 tens 6 ones = <b>206</b>. The 0 holds the tens place.')
    : task === 'two' ? example('A rod is 10 ones. Trade one rod for 10 cubes and the number stays the same.', '34 = 3 tens 4 ones = 2 tens <b>14</b> ones')
    : example('A rod is 10 and a cube is 1. Draw a rod as a tall stick and a cube as a small square.', '4 rods and 7 cubes: 4 tens 7 ones = <b>47</b>');
  return { body: cells(html, 2), items, ex, dirs, materials: 'pencil' + (two ? '' : ', base-ten blocks (optional)'),
    ican: two ? 'I can show a three-digit number with hundreds, tens and ones.' : task === 'two' ? 'I can show a two-digit number in more than one way.' : 'I can show a two-digit number with tens and ones.',
    mistakes: two ? 'Leaving out the 0 when there are no tens (writing 26 for 206), and counting a flat as 10.' : 'Counting each rod as 1, or writing the ones before the tens.',
    notes: (two ? 'At least one number has zero tens, which is the one to talk through. ' : '') + 'Students may draw a rod as a line and a cube as a dot or small square: any clear drawing counts.' };
}
function skExpanded(v, r, n) {
  const g = v.grade, items = [];
  if (g === '1') {
    const list = r.distinct(n, () => { const x = r.int(11, 99); return x % 10 ? x : null; });
    const rows = list.map((x, i) => {
      const t = Math.floor(x / 10), o = x % 10, kind = ['te', 'ex', 'st'][i % 3];
      if (kind === 'te') { items.push({ k: 'exp1', q: `${x} = tens ones`, a: `${t} tens ${o} ones`, x, kind }); return `${x} = ${blank(t, 1.4)} tens ${blank(o, 1.4)} ones`; }
      if (kind === 'ex') { items.push({ k: 'exp1', q: `${x} = + `, a: `${10 * t} + ${o}`, x, kind }); return `${x} = ${blank(10 * t, 1.8)} + ${blank(o, 1.4)}`; }
      items.push({ k: 'exp1', q: `${10 * t} + ${o} =`, a: String(x), x, kind }); return `${10 * t} + ${o} = ${blank(x, 1.8)}`;
    });
    return { body: fill(rows, 2), items, ex: example('47 is 4 tens and 7 ones. 4 tens is 40, so 47 = 40 + 7.', '47 = <b>4</b> tens <b>7</b> ones = <b>40</b> + <b>7</b>'),
      dirs: 'Fill in the blanks. Think of each number as tens and ones.', ican: 'I can write a two-digit number as tens and ones.',
      mistakes: 'Writing 4 + 7 for 47: the 4 is 4 tens, which is 40.', notes: 'Three kinds of rows take turns: tens and ones, expanded form, and back to the number.' };
  }
  const list = r.distinct(n, () => 100 * r.int(1, 9) + 10 * (r.chance(.25) ? 0 : r.int(0, 9)) + (r.chance(.15) ? 0 : r.int(0, 9)));
  const rows = list.map((x, i) => {
    const hh = Math.floor(x / 100), t = Math.floor(x / 10) % 10, o = x % 10;
    const ex = [hh * 100, t * 10, o].filter(Boolean).join(' + '), wd = words(x), give = ['std', 'word', 'exp'][i % 3];
    items.push({ k: 'exp2', q: `${give}: ${give === 'std' ? x : give === 'word' ? wd : ex}`, a: `${x}; ${wd}; ${ex}`, x, wd, ex });
    return [`<span class="ws-num">${i + 1}.</span> ` + (give === 'std' ? `<b>${x}</b>` : blank(x, 3)), give === 'word' ? `<b>${wd}</b>` : blank(wd, Math.max(8, .52 * wd.length)), give === 'exp' ? `<b>${ex}</b>` : blank(ex, Math.max(6, .52 * ex.length))];
  });
  return { body: `<div class="en-table">${H.table(['Standard form', 'Word form', 'Expanded form'], rows)}</div>`, items,
    ex: example('Standard form: 406. Word form: four hundred six. Expanded form: 400 + 6.', 'A zero place is left out of the word form and the expanded form, but in 406 the 0 holds the tens place.'),
    dirs: 'Each row gives one form of a number. Write the other two forms.', ican: 'I can write a three-digit number in standard, word and expanded form.',
    mistakes: 'Writing 4006 for four hundred six, and putting "and" in the word form (four hundred and six). Numbers like forty-two take a hyphen.',
    notes: 'Rows take turns giving the standard, word and expanded form. Some numbers have a zero in the tens or ones place on purpose.' };
}
function skCompare12(v, r, n) {
  const g = v.grade, frames = !!v.frames, items = [], parts = [];
  let list;
  if (g === '1' && v.task === 'pics') {
    list = r.distinct(n, () => { const a = r.int(1, 20), b = r.chance(.15) ? a : r.int(1, 20); return [a, b]; }, x => x.join(' '));
    const html = list.map(([a, b]) => {
      const fr = (x0, k) => frame(x0, 2, 11, Math.min(k, 10)) + frame(x0, 28, 11, Math.max(0, k - 10));
      let body = fr(2, a) + fr(118, b) + `<circle cx="88" cy="26" r="15" fill="#fff" stroke="${INK}" stroke-width="1.6"/>` + keyg(txt(88, 32, symbol(a, b), 18, `font-weight="700" fill="${RED}"`));
      body += txt(29.5, 68, String(a), 15, 'font-weight="700"') + txt(145.5, 68, String(b), 15, 'font-weight="700"');
      items.push({ k: 'cmp', q: `${a} ? ${b}`, a: symbol(a, b), x: a, y: b, ph: frames ? phrase(a, b) : '' });
      return svgw(176, 74, body, `Ten frames showing ${a} and ${b}`, 1.95) + (frames ? `<p>${a} is ${blank(phrase(a, b), 6.5)} ${b}.</p>` : '');
    });
    parts.push(part('', cells(html, 2)));
  } else {
    const lo = g === '1' ? 10 : 100, hi = g === '1' ? 99 : 999;
    list = r.distinct(n, () => {
      const a = r.int(lo, hi), roll = r.next();
      let b;
      if (roll < .1) b = a;
      else if (roll < .45) b = g === '1' ? Math.floor(a / 10) * 10 + r.int(0, 9) : Math.floor(a / 100) * 100 + r.int(0, 99);
      else if (roll < .65 && g === '2') b = Math.floor(a / 10) * 10 + r.int(0, 9);
      else if (roll < .8) b = Number(String(a).split('').reverse().join(''));
      else b = r.int(lo, hi);
      if (b < lo || b > hi || (b === a && roll >= .1)) return null;
      return [a, b];
    }, x => x.join(' '));
    const rows = list.map(([a, b]) => {
      items.push({ k: 'cmp', q: `${a} ? ${b}`, a: symbol(a, b), x: a, y: b, ph: frames ? phrase(a, b) : '' });
      return `<span class="en-cmp">${show(a)} ${symBox(symbol(a, b))} ${show(b)}</span>` + (frames ? ` &nbsp; ${show(a)} is ${blank(phrase(a, b), 6.5)} ${show(b)}.` : '');
    });
    parts.push(part('', fill(rows, frames ? 1 : 3)));
    if (g === '2' && v.task === 'order') {
      const sets = v.count === 's' ? 1 : v.count === 'm' ? 2 : 3, orows = [];
      for (let k = 0; k < sets; k++) {
        const hd = r.int(1, 8), nums = r.distinct(4, () => r.chance(.6) ? 100 * hd + r.int(0, 99) : 100 * (hd + 1) + r.int(0, 99));
        const sorted = nums.slice().sort((a, b) => a - b);
        items.push({ k: 'order', q: `order ${nums.join(' ')}`, a: sorted.join(', '), nums });
        orows.push(`${nums.map(show).join(', ')}<br>${sorted.map(x => blank(show(x), 2.6)).join(' , ')}`);
      }
      parts.push(part('Order from least to greatest', fill(orows, 1, list.length + 1)));
    }
  }
  if (g === '1') {
    const [a, b] = list.find(x => x[0] !== x[1]) || list[0];
    const ta = Math.floor(a / 10), tb = Math.floor(b / 10), oa = a % 10, ob = b % 10;
    const why = a === b ? `Both have ${ta} tens and ${oa} ones, so they are equal.`
      : ta !== tb ? `${a} has ${ta} ${ta === 1 ? 'ten' : 'tens'} and ${b} has ${tb} ${tb === 1 ? 'ten' : 'tens'}, so ${a} is ${phrase(a, b)} ${b}.`
      : `Both have ${ta} ${ta === 1 ? 'ten' : 'tens'}. ${oa} ones is ${oa > ob ? 'more' : 'fewer'} than ${ob} ones, so ${a} is ${phrase(a, b)} ${b}.`;
    const num = list.findIndex(x => x[0] === a && x[1] === b) + 1;
    parts.push(part('Tell how you know', `<p>Look at problem ${num}: ${a} ${esc(symbol(a, b))} ${b}. How do you know?</p>${H.lines(2)}<p class="ws-keyonly">Sample: ${esc(why)}</p>`));
  }
  const ex = g === '1' ? example('Compare the tens first. If the tens are the same, compare the ones. The open side of the sign faces the greater number.', '47 <b>&lt;</b> 52 (4 tens is less than 5 tens) &nbsp; 63 <b>&gt;</b> 61 (same tens; 3 ones is more than 1)')
    : example('Compare the hundreds first, then the tens, then the ones. The open side of the sign faces the greater number.', '452 <b>&lt;</b> 524 (4 hundreds is less than 5 hundreds) &nbsp; 381 <b>&gt;</b> 318 (same hundreds; 8 tens is more than 1 ten)');
  return { parts, items, ex, dirs: `Write &gt;, &lt; or = in each circle.${frames ? ' Then finish the sentence with greater than, less than or equal to.' : ''}${v.task === 'order' ? ' Then write each set in order from least to greatest.' : ''}`,
    ican: g === '1' ? 'I can compare two-digit numbers using tens and ones.' : 'I can compare and order three-digit numbers using place value.',
    mistakes: 'Reading the sign backward (read left to right, > says greater than), and comparing the ones before the tens. Pairs like 47 and 74 use the same digits on purpose.',
    notes: 'Some pairs are equal and some share their first digit, so students have to look past the first place.' };
}
function skTenmore(v, r, n) {
  const g = v.grade, items = [];
  if (v.task === 'chart') {
    const list = r.distinct(n, () => r.int(12, 109));
    const c = 38, pos = { up: [1, 0], down: [1, 2], left: [0, 1], right: [2, 1] };
    const html = list.map(x => {
      const nb = { up: x > 10 ? x - 10 : null, left: x % 10 !== 1 ? x - 1 : null, right: x % 10 !== 0 ? x + 1 : null, down: x + 10 <= 120 ? x + 10 : null };
      let b = `<rect x="${c + 2}" y="${c + 2}" width="${c}" height="${c}" fill="#e8e8e8" stroke="${INK}" stroke-width="1.6"/>` + txt(1.5 * c + 2, 1.5 * c + 8, String(x), 15, 'font-weight="700"');
      for (const d of ['up', 'left', 'right', 'down']) {
        if (nb[d] == null) continue;
        const [cx, cy] = pos[d];
        b += `<rect x="${cx * c + 2}" y="${cy * c + 2}" width="${c}" height="${c}" fill="#fff" stroke="${INK}" stroke-width="1.6"/>` + keyg(txt((cx + .5) * c + 2, (cy + .5) * c + 8, String(nb[d]), 15, `font-weight="700" fill="${RED}"`));
        items.push({ k: 'piece', q: `piece ${x} ${d}`, a: String(nb[d]), x, d });
      }
      return svgw(3 * c + 4, 3 * c + 4, b, `A piece of the 120 chart around ${x}`, 1.25);
    });
    return { body: cells(html, 4), items, ex: example('On a 120 chart, the square below is 10 more and the square above is 10 less. Left is 1 less and right is 1 more.', 'Around 45: above <b>35</b>, below <b>55</b>, left <b>44</b>, right <b>46</b>.'),
      dirs: 'Each piece comes from a 120 chart. Fill in the empty squares around the gray one.', ican: 'I can find 10 more, 10 less, 1 more and 1 less on a 120 chart.',
      mistakes: 'Adding 1 for the square below instead of 10. On a chart with rows of ten, going down one row is 10 more.',
      notes: 'Pieces at the edge of the chart leave out squares that would sit in another row: a number ending in 1 has nothing to its left, and a number ending in 0 has nothing to its right.', materials: 'pencil, a 120 chart (optional)' };
  }
  const list = r.distinct(n, () => g === '1' ? r.int(10, 89) : r.int(100, 899));
  const head = g === '1' ? ['10 less', 'Number', '10 more'] : ['100 less', '10 less', 'Number', '10 more', '100 more'];
  const ds = g === '1' ? [-10, null, 10] : [-100, -10, null, 10, 100];
  const rows = list.map((x, i) => {
    items.push({ k: 'tm', q: `around ${x}`, a: ds.filter(d => d != null).map(d => x + d).join(', '), x, ds: ds.filter(d => d != null) });
    return ds.map(d => d == null ? `<span class="ws-num">${i + 1}.</span> <b>${x}</b>` : blank(x + d, 2.6));
  });
  return { body: `<div class="en-table">${H.table(head, rows)}</div>`, items,
    ex: g === '1' ? example('10 more makes the tens digit go up by 1. 10 less makes it go down by 1. The ones digit stays the same.', '10 less than 46 is <b>36</b>. 10 more than 46 is <b>56</b>.')
      : example('10 more or less changes the tens digit by 1. 100 more or less changes the hundreds digit by 1.', '100 less than 347 is <b>247</b>, 10 less is <b>337</b>, 10 more is <b>357</b> and 100 more is <b>447</b>.'),
    dirs: g === '1' ? 'Write 10 less and 10 more than each number. Try it in your head, without counting by ones.' : 'Write 100 less, 10 less, 10 more and 100 more than each number.',
    ican: g === '1' ? 'I can find 10 more and 10 less than a number in my head.' : 'I can find 10 or 100 more or less than a number in my head.',
    mistakes: g === '1' ? 'Changing the ones digit instead of the tens digit.' : 'Changing the ones digit instead of the tens. Watch numbers like 195, where 10 more is 205, and 103, where 10 less is 93.',
    notes: 'A hundred chart helps students who are not ready to do it in their heads. Look for the pattern: only one digit changes, except when the count crosses a hundred.' };
}
function skClock(v, r, n) {
  const g = v.grade, task = v.task, items = [], html = [];
  const list = r.distinct(n, () => [r.int(1, 12), g === '1' ? r.pick([0, 30]) : 5 * r.int(0, 11)], x => x.join(':'));
  const nRead = task === 'mix' ? Math.ceil(list.length * 2 / 3) : 0;
  list.forEach(([h, m], i) => {
    const mode = task === 'mix' ? (i < nRead ? 'read' : 'draw') : task, time = `${h}:${pad2(m)}`;
    if (mode === 'read') {
      const c = clockSvg(h, m, 'hm', '', g === '2');
      html.push(svgw(100, 100, c.b, 'A clock', 1.3) + `<p class="en-center">${blank(time, 3)}</p>`);
      items.push({ k: 'clock', q: `read ${time}`, a: time, ha: c.ha, ma: c.ma });
    } else if (mode === 'draw') {
      const c = clockSvg(h, m, '', 'hm', g === '2');
      html.push(svgw(100, 100, c.b, 'A clock with no hands', 1.3) + `<p class="en-time">${time}</p>`);
      items.push({ k: 'clock', q: `draw ${time}`, a: time, ha: c.ha, ma: c.ma });
    } else {
      const c = clockSvg(h, m, 'm', 'h', false);
      html.push(svgw(100, 100, c.b, 'A clock with only the minute hand', 1.3) + `<p class="en-time">${m ? `half past ${h}` : `${h} o'clock`}</p><p class="en-center">${blank(time, 3)}</p>`);
      items.push({ k: 'clock', q: `hour hand ${time}`, a: time, ha: c.ha, ma: c.ma });
    }
  });
  const dirs = task === 'read' ? 'Write the time shown on each clock.' : task === 'draw' ? 'Draw the hour hand and the minute hand to show each time. Make the hour hand shorter.'
    : task === 'hour' ? 'The long minute hand is drawn. Draw the short hour hand, then write the time.' : `Write the time on clocks 1 to ${nRead}. Draw the hands on the rest. Make the hour hand shorter.`;
  return { body: cells(html, 4), items,
    ex: g === '1' ? example('The short hand is the hour hand. The long hand is the minute hand.', 'At 3:00 the long hand points to 12 and the short hand points to 3. At 3:30 the long hand points to 6 and the short hand is halfway between 3 and 4.')
      : example('The short hand is the hour hand. The long hand counts minutes by 5s: at the 1 it is 5 minutes, at the 2 it is 10, at the 3 it is 15, and so on.', 'The long hand on the 4 and the short hand just past the 7 is <b>7:20</b>.'),
    dirs, ican: g === '1' ? 'I can tell and show time to the hour and half hour.' : 'I can tell and show time to the nearest five minutes.',
    mistakes: g === '1' ? 'Pointing the hour hand right at the hour at half past. At 3:30 it sits halfway between 3 and 4.' : 'Reading the number the minute hand points to as the minutes (4 instead of 20), and naming the next hour when the hour hand is only partway there.',
    notes: 'The key draws the hour hand where it really sits, partway to the next number, so students can check that detail.' + (g === '2' ? ' Minute marks are drawn on every clock.' : '') };
}
function skLength1(v, r, n) {
  const task = v.task, items = [], html = [], parts = [];
  if (task === 'order') {
    const list = r.distinct(n, () => {
      const ls = [r.int(60, 250), r.int(60, 250), r.int(60, 250)], s = ls.slice().sort((a, b) => a - b);
      return s[1] - s[0] < 25 || s[2] - s[1] < 25 ? null : { ls, ks: r.sample(OBJECTS, 3) };
    }, x => x.ls.join(' '));
    for (const { ls, ks } of list) {
      const sorted = ls.slice().sort((a, b) => b - a), rank = ls.map(l => sorted.indexOf(l) + 1);
      let b = `<line x1="10" y1="4" x2="10" y2="110" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>`;
      ls.forEach((l, j) => {
        const y = 20 + j * 36;
        b += obj(ks[j], 10, y, l) + `<rect x="276" y="${y - 14}" width="26" height="28" fill="#fff" stroke="${INK}" stroke-width="1.4" rx="3"/>` + keyg(txt(289, y + 6, String(rank[j]), 17, `font-weight="700" fill="${RED}"`));
      });
      html.push(svgw(306, 114, b, `A ${ks.join(', a ')}`, 3.15));
      items.push({ k: 'order3', q: `order ${ls.join(' ')}`, a: rank.join(', '), ls });
    }
    parts.push(part('', cells(html, 2)));
    const [a, b, c] = r.sample(OBJECTS, 3), ask = r.chance(.5) ? [a, c] : [c, a];
    items.push({ k: 'trans', q: `${a} > ${b} > ${c}`, a, chain: [a, b, c], ask });
    parts.push(part('Think about it', `<p>${list.length + 1}. The ${a} is longer than the ${b}. The ${b} is longer than the ${c}. Which is longer, the ${ask[0]} or the ${ask[1]}?</p><p>The ${blank(a, 5)} is longer.</p>`));
    return { parts, items, ex: example('Line things up at one end, then look at the other end.', 'The longest gets <b>1</b>, the next gets <b>2</b> and the shortest gets <b>3</b>.'),
      dirs: 'In each set, write 1 in the box by the longest, 2 by the next and 3 by the shortest. Then answer the last question.', ican: 'I can put three objects in order by length.',
      mistakes: 'Writing 1 by the shortest. Say it aloud: 1 is the longest.',
      notes: 'All three objects start at the dotted line. The last question compares two things through a third (1.MD.1): students can act it out with real objects or draw it.' };
  }
  const cubes = task === 'cubes', u = cubes ? 24 : 40, lo = cubes ? 3 : 2, hi = cubes ? 10 : 6, unit = cubes ? 'cubes' : 'paper clips';
  let names = r.shuffle(OBJECTS);
  while (names.length < n) names = names.concat(r.sample(OBJECTS, Math.min(OBJECTS.length, n - names.length)));
  names = names.slice(0, n);
  const lens = r.distinct(n, () => r.int(lo, hi)), all = lens.concat(Array.from({ length: n - lens.length }, () => r.int(lo, hi)));
  const objs = names.map((nm, i) => ({ nm, k: all[i] }));
  objs.forEach(({ nm, k }, i) => {
    let b = obj(nm, 8, 16, k * u), drawn = 0;
    for (let j = 0; j < k; j++) {
      const x = 8 + j * u;
      b += cubes ? `<rect x="${x}" y="34" width="${u}" height="${u}" fill="#eee" stroke="${INK}" stroke-width="1.4"/>`
        : `<rect x="${x + 1}" y="36" width="${u - 2}" height="14" rx="7" fill="none" stroke="${INK}" stroke-width="1.6"/><rect x="${x + 6}" y="39.5" width="${u - 16}" height="7" rx="3.5" fill="none" stroke="${INK}" stroke-width="1.3"/>`;
      drawn++;
    }
    html.push(`<p class="en-name">the ${nm}</p>` + svgw(264, cubes ? 62 : 54, b, `A ${nm} with ${unit} under it`, 2.75) + `<p>${blank(k, 1.8)} ${unit} long</p>`);
    items.push({ k: 'units', q: `${i + 1}. the ${nm}`, a: String(k), len: k * u, u, drawn });
  });
  parts.push(part('', cells(html, 2)));
  if (v.frames) {
    const once = objs.filter(o => objs.filter(p => p.nm === o.nm).length === 1), pairs = [];
    for (let i = 0; i < once.length; i++) for (let j = i + 1; j < once.length; j++) if (once[i].k !== once[j].k) pairs.push(r.chance(.5) ? [once[i], once[j]] : [once[j], once[i]]);
    const rows = r.sample(pairs, 2).map(([a, b]) => {
      const w = a.k > b.k ? 'longer' : 'shorter';
      items.push({ k: 'lensay', q: `The ${a.nm} is ___ than the ${b.nm}`, a: w, x: a.k, y: b.k });
      return `The ${a.nm} is ${blank(w, 4.5)} than the ${b.nm}.`;
    });
    if (rows.length) parts.push(part('Say it', fill(rows, 1, objs.length + 1)));
  }
  return { parts, items, ex: example(`Count the ${unit} from one end of the object to the other.`, `An object as long as 5 ${unit} is <b>5</b> ${unit} long.`),
    dirs: `Count the ${unit} under each object. Write how many ${unit} long it is.${v.frames ? ' Then finish each sentence with longer or shorter.' : ''}`, materials: `pencil, ${cubes ? 'connecting cubes' : 'paper clips'} (optional, to measure real objects after)`,
    ican: `I can measure length with ${unit}.`, mistakes: `Counting ${unit} that stick past the end, or leaving gaps between ${unit} when measuring real objects.`,
    notes: `The ${unit} are drawn end to end with no gaps or overlaps, the way students should lay them out. Follow up by measuring real classroom objects.` };
}

/* ---------- Grade 2 ---------- */
function skLength2(v, r, n) {
  const task = v.task, items = [], html = [], parts = [];
  if (task === 'diff') {
    const list = r.distinct(n, () => { const a = r.int(3, 15), b = r.int(3, 15); return Math.abs(a - b) >= 2 ? [a, b] : null; }, x => x.join(' '));
    for (const [a, b] of list) {
      const L = Math.max(a, b), S = Math.min(a, b), longer = a > b ? 'A' : 'B';
      let body = obj('pencil', 40, 14, a * CM) + txt(20, 19, 'A', 14, 'font-weight="700"') + obj('pencil', 40, 44, b * CM) + txt(20, 49, 'B', 14, 'font-weight="700"');
      body += `<line x1="40" y1="2" x2="40" y2="62" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>` + ruler(40, 62, 16, 'cm');
      html.push(svgw(670, 98, body, 'Pencils A and B above a centimeter ruler', 6.7) +
        `<p>A: ${blank(a, 2)} cm &nbsp; B: ${blank(b, 2)} cm &nbsp; ${blank(L, 2)} − ${blank(S, 2)} = ${blank(L - S, 2)} &nbsp; Pencil ${blank(longer, 1.6)} is ${blank(L - S, 2)} cm longer.</p>`);
      items.push({ k: 'diff', q: `pencils ${a} and ${b}`, a: `${a}, ${b}; ${L} − ${S} = ${L - S}; ${longer}`, la: a, lb: b, longer, d: L - S });
    }
    parts.push(part('', lineRows(html)));
    return { parts, items, ex: example('Measure both pencils. Subtract the shorter length from the longer one.', 'A is 12 cm and B is 7 cm. 12 − 7 = <b>5</b>, so A is 5 cm longer.'),
      dirs: 'Measure each pencil with the centimeter ruler. Write a subtraction equation to find how much longer one is.', ican: 'I can measure two objects and find how much longer one is.',
      mistakes: 'Subtracting the longer length from the shorter one, or counting tick marks from 1 instead of reading the number at the end.',
      notes: 'Both pencils start at 0, marked by the dotted line. The ruler is drawn on the page, so a printer that scales the sheet does not change the answers.' };
  }
  const both = task === 'both', unit = task === 'cm' ? 'cm' : 'in', max = unit === 'in' ? 6 : 16;
  const list = r.distinct(n, () => {
    const L = unit === 'in' ? r.int(1, 6) : r.int(2, 15), s = both || r.chance(.6) ? 0 : r.int(1, unit === 'in' ? 2 : 3);
    return s + L <= max ? { L, s } : null;
  }, x => `${x.L} ${x.s}`);
  list.forEach(({ L, s }, i) => {
    const px = unit === 'in' ? INCH : CM, x0 = 70, letter = 'ABCDEFGHJK'[i];
    let body = bar(x0 + s * px, 12, L * px) + txt(24, 17, `Line ${letter}`, 12, 'font-weight="700"') + ruler(x0, 22, max, unit);
    let h = 58, cm = 0;
    if (both) { cm = Math.round(L * 2.54); body += ruler(x0, 62, 16, 'cm'); h = 98; }
    const W = both ? x0 + 16 * CM + 20 : x0 + max * px + 20;
    const line = both ? `<p>Line ${letter}: about ${blank(L, 2)} inches and about ${blank(cm, 2)} centimeters</p>` : `<p>Line ${letter} is ${blank(L, 2)} ${unit === 'in' ? 'inches' : 'centimeters'} long.</p>`;
    html.push(svgw(W, h, body, `Line ${letter} above a ${both ? 'inch ruler and a centimeter ruler' : unit === 'in' ? 'inch ruler' : 'centimeter ruler'}`, W / 96) + line);
    items.push({ k: 'ruler', q: `line ${letter}: ${s} to ${s + L} ${unit}`, a: both ? `${L} in; ${cm} cm` : String(L), s, e: s + L, unit, both });
  });
  parts.push(part('', lineRows(html)));
  if (both) {
    items.push({ k: 'which', q: 'Which number is bigger?', a: 'centimeters' });
    parts.push(part('Think about it', `<p>For each line, which number is bigger, the inches or the centimeters? Why?</p>${H.lines(2)}<p class="ws-keyonly">The number of centimeters is always bigger. A centimeter is a smaller unit than an inch, so it takes more of them to cover the same line.</p>`));
  }
  const offset = list.some(x => x.s > 0);
  return { parts, items, ex: both ? example('Read where the line ends on each ruler. Round to the nearest whole unit.', 'A line 3 inches long is about <b>8</b> centimeters long.')
      : example('Line up the start of the line with 0. If a line starts at another number, count the units between its ends.', `A line from 1 to 5 is 5 − 1 = <b>4</b> ${unit === 'in' ? 'inches' : 'centimeters'} long.`),
    dirs: both ? 'Use the rulers under each line. Write its length to the nearest inch and to the nearest centimeter.' : `Use the ruler under each line. Write how many ${unit === 'in' ? 'inches' : 'centimeters'} long it is.`,
    ican: both ? 'I can measure the same length in inches and centimeters and tell why the numbers differ.' : `I can measure length in ${unit === 'in' ? 'inches' : 'centimeters'} with a ruler.`,
    mistakes: 'Starting at 1 instead of 0, and reading the number where a line ends when it did not start at 0.',
    notes: (offset ? 'Some lines start past 0 on purpose: the length is the number of units between the two ends. ' : '') + 'The rulers are drawn on the page, so a printer that scales the sheet does not change the answers.' + (both ? ' Inch lengths are whole; centimeter answers are rounded to the nearest centimeter.' : '') };
}
function coinMix(r) {
  for (let t = 0; t < 200; t++) {
    const c = { q: r.int(0, 3), d: r.int(0, 4), n: r.int(0, 3), p: r.int(0, 5) };
    const total = 25 * c.q + 10 * c.d + 5 * c.n + c.p, count = c.q + c.d + c.n + c.p, kinds = ['q', 'd', 'n', 'p'].filter(k => c[k]).length;
    if (total >= 10 && total <= 99 && count >= 2 && count <= 8 && kinds >= 2) return c;
  }
  return null;
}
const comboText = c => ['q', 'd', 'n', 'p'].filter(k => c[k]).map(k => `${c[k]} ${c[k] === 1 ? COIN[k].name : COIN[k].many}`).join(', ');
function skCoins(v, r, n) {
  const task = v.task, both = v.coinlabel !== 'name', items = [], parts = [];
  if (both) parts.push(part('', `<div class="en-legend">${['p', 'n', 'd', 'q'].map(k => `<div>${svgw(66, 66, coin(33, 33, k, true), `A ${COIN[k].name}`, .72)}<span>${COIN[k].name} = ${COIN[k].c}¢</span></div>`).join('')}</div>`));
  if (task === 'make') {
    const amts = r.distinct(n, () => r.chance(.7) ? 5 * r.int(5, 19) : r.int(26, 99));
    const rows = amts.map(A => {
      const all = [];
      for (let q = 0; q * 25 <= A; q++) for (let d = 0; q * 25 + d * 10 <= A; d++) for (let nn = 0; q * 25 + d * 10 + nn * 5 <= A; nn++) {
        const p = A - 25 * q - 10 * d - 5 * nn, cnt = q + d + nn + p;
        if (cnt <= 12) all.push({ q, d, n: nn, p, cnt });
      }
      all.sort((a, b) => a.cnt - b.cnt);
      const ways = [all[0], ...r.sample(all.slice(1), 2)];
      items.push({ k: 'make', q: `make ${A}`, a: ways.map(comboText).join('; '), A, ways });
      return `<p>Show <b>${A}¢</b> three ways.</p><div class="en-ways">${ways.map((w, j) => `<div class="en-way">${H.key(`${j === 0 ? '★ ' : ''}${comboText(w)}`)}</div>`).join('')}</div>`;
    });
    parts.push(part('', lineRows(rows)));
    return { parts, items, ex: example('Draw circles and write Q, D, N or P in each. Add them up to check.', '30¢ = Q N (2 coins) = D D D (3 coins) = D D N N (4 coins). Q N uses the fewest coins.'),
      dirs: 'Draw coins to show each amount three different ways. Write Q, D, N or P in each coin. Put a star on the way that uses the fewest coins.',
      ican: 'I can show the same amount of money with different coins.', mistakes: 'Using more quarters than fit (4 quarters is already a dollar), and drawing a way that adds up to the wrong total.',
      notes: 'Any three correct ways count. The key shows the way with the fewest coins first, starred, and two other ways as samples.' };
  }
  const NAMES = ['Maya', 'Leo', 'Sam', 'Ana', 'Ben', 'Mia', 'Omar', 'Lily', 'Jack', 'Zoe', 'Eli', 'Rosa'];
  const TOYS = ['ball', 'kite', 'yo-yo', 'sticker book', 'toy car', 'jump rope', 'bubble wand', 'box of crayons', 'puzzle', 'bouncy ball'];
  const mixes = r.distinct(n, () => coinMix(r), c => `${c.q}${c.d}${c.n}${c.p}`), who = r.sample(NAMES, NAMES.length), toys = r.sample(TOYS, TOYS.length);
  const html = mixes.map((c, i) => {
    const list = r.shuffle(['q', 'd', 'n', 'p'].flatMap(k => Array(c[k]).fill(k))), total = 25 * c.q + 10 * c.d + 5 * c.n + c.p, cr = coinRow(list, both);
    const pic = svgw(cr.w, cr.h, cr.b, 'Coins to count', cr.w / 96 * .95);
    if (task === 'buy') {
      const nm = who[i % who.length], toy = toys[i % toys.length];
      const price = Math.min(99, Math.max(5, total + (r.chance(.5) ? -r.int(0, 15) : r.int(1, 20))));
      const yes = total >= price, need = yes ? 0 : price - total;
      items.push({ k: 'buy', q: `${nm}: ${toy} for ${price}`, a: `${total}¢; ${yes ? 'yes' : 'no'}; ${need}¢`, coins: list, price });
      return `<p class="en-name">${nm}'s piggy bank</p>${pic}<p>Total: ${blank(total, 2.2)}¢</p><p>The ${toy} costs <b>${price}¢</b>. Can ${nm} buy it now? ${blank(yes ? 'yes' : 'no', 2.4)}</p><p>${nm} needs ${blank(need, 2)}¢ more. (Write 0 if there is enough.)</p>`;
    }
    items.push({ k: 'coins', q: `coins ${comboText(c)}`, a: `${total}¢`, coins: list });
    return `${pic}<p>Total: ${blank(total, 2.2)}¢</p>`;
  });
  parts.push(part('', cells(html, 2)));
  return { parts, items, ex: example('Sort the coins from greatest to least value. Count on: quarters by 25s, dimes by 10s, nickels by 5s, pennies by 1s.', 'quarter, dime, dime, nickel, penny: 25, 35, 45, 50, 51. The total is <b>51¢</b>.'),
    dirs: task === 'buy' ? 'Count the coins in each piggy bank. Decide if there is enough to buy the toy. If not, find how much more is needed.' : 'Count the coins. Write the total with the cent sign (¢).',
    ican: task === 'buy' ? 'I can count coins and decide if I have enough money.' : 'I can count a mix of coins and write the total with the ¢ sign.',
    mistakes: 'Counting the coins instead of their values (5 coins is not 5¢), and thinking a nickel is worth more than a dime because it is bigger.',
    notes: `Coins are drawn as labeled circles at their real relative sizes (the dime is the smallest), and they are mixed up on purpose: sorting them first is the strategy to teach.${both ? '' : ' The coins show their names only; students supply the values.'}` };
}
function skEvenodd(v, r, n) {
  const items = [], parts = [];
  if (v.task === 'doubles') {
    const list = r.sample([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], n), odd = 2 * r.int(2, 9) + 1;
    const rows = list.map(x => { items.push({ k: 'dbl', q: `${x} as doubles`, a: `${x / 2} + ${x / 2}`, x }); return `${x} = ${blank(x / 2, 1.6)} + ${blank(x / 2, 1.6)}`; });
    parts.push(part('', fill(rows, 3)));
    parts.push(part('Think about it', `<p>Can ${odd} be split into two equal parts? Why or why not?</p>${H.lines(2)}<p class="ws-keyonly">No. ${odd} = ${(odd - 1) / 2} + ${(odd + 1) / 2}: when ${odd} things are put in pairs, one is left over, so the two parts can never be equal. That is what makes ${odd} odd.</p>`));
    return { parts, items, ex: example('An even number splits into two equal parts, called doubles.', '14 = <b>7</b> + <b>7</b>'),
      dirs: 'Write each even number as a double: two equal numbers added together.', ican: 'I can write an even number as the sum of two equal addends.',
      mistakes: 'Writing two different numbers (14 = 6 + 8). Both parts must be the same.', notes: 'Counters help: split the counters into two equal rows and count one row.' };
  }
  const list = r.sample(Array.from({ length: 19 }, (_, i) => i + 2), n), kind = r.pick(KINDS);
  const html = list.map(x => {
    const s = x <= 10 ? 18 : 15, pts = arrange(r, x, 230, 90, s, 'scatter'), even = x % 2 === 0;
    items.push({ k: 'eo', q: `${x} ${kind}`, a: even ? `even; ${x / 2} + ${x / 2}` : 'odd', x, drawn: pts.length });
    return svgw(230, 90, `<rect x="1" y="1" width="228" height="88" rx="8" fill="none" stroke="#bbb"/>` + pts.map(p => shape(kind, p[0], p[1], s)).join(''), 'Shapes to pair up', 2.3) +
      `<p>Odd or even? ${blank(even ? 'even' : 'odd', 3)}</p><p>If even, as doubles: ${blank(even ? `${x / 2} + ${x / 2}` : 'odd, no doubles', 5.5)}</p>`;
  });
  parts.push(part('', cells(html, 2)));
  return { parts, items, ex: example('Circle the shapes in pairs. If every shape has a partner, the number is even. If one is left over, it is odd.', '9 shapes make 4 pairs and 1 left over, so 9 is <b>odd</b>. 8 shapes make 4 pairs, so 8 is <b>even</b> and 8 = 4 + 4.'),
    dirs: 'Circle the shapes in pairs. Write odd or even. If the group is even, write it as doubles.', ican: 'I can tell if a group is odd or even by pairing.',
    mistakes: 'Circling a shape twice. Crossing off each pair helps. An even group splits into two equal groups: one from each pair.',
    notes: 'Groups run from 2 to 20 shapes, scattered so students have to make the pairs themselves.' };
}
function skArrays(v, r, n) {
  const draw = v.task === 'draw', items = [];
  const CTX = [['A muffin tin', 'ring'], ['A tray of eggs', 'ring'], ['A garden bed', 'star'], ['A sheet of stickers', 'star'], ['A box of crackers', 'square'], ['A window', 'square'], ['A pan of rolls', 'dot']];
  const list = r.distinct(n, () => [r.int(2, 5), r.int(2, 5)], x => x.join('x'));
  const html = list.map(([R, C]) => {
    const [label, kind] = draw ? ['', 'dot'] : r.pick(CTX), sp = 22, W = 130, Ht = 120;
    const x0 = (W - sp * (C - 1)) / 2, y0 = (Ht - sp * (R - 1)) / 2;
    let dots = '';
    for (let i = 0; i < R; i++) for (let j = 0; j < C; j++) dots += shape(kind, x0 + j * sp, y0 + i * sp, 17, draw ? RED : INK);
    const pic = draw ? `<rect x="1" y="1" width="${W - 2}" height="${Ht - 2}" rx="6" fill="none" stroke="#555" stroke-width="1.2" stroke-dasharray="5 4"/>` + keyg(dots)
      : `<rect x="${nf(x0 - 16)}" y="${nf(y0 - 16)}" width="${nf(sp * (C - 1) + 32)}" height="${nf(sp * (R - 1) + 32)}" rx="10" fill="#fafafa" stroke="${INK}" stroke-width="1.6"/>` + dots;
    const rowsEq = Array(R).fill(C).join(' + '), colsEq = Array(C).fill(R).join(' + ');
    items.push({ k: 'arr', q: `${R} rows of ${C}`, a: `${rowsEq} = ${R * C}; ${colsEq} = ${R * C}`, R, C, rowsEq, colsEq, dots: (dots.match(/<(circle|rect|polygon|path) /g) || []).length });
    return `<div class="en-arr">${svgw(W, Ht, pic, draw ? 'A box to draw an array' : `${label}: an array`, 1.3)}<div>` + (draw ? `<p>Draw <b>${R} rows of ${C}</b>.</p>` : `<p><b>${label}</b></p><p>${blank(R, 1.4)} rows of ${blank(C, 1.4)}</p>`) +
      `<p>By rows: ${blank(rowsEq, Math.max(4, .55 * rowsEq.length))} = ${blank(R * C, 1.8)}</p><p>By columns: ${blank(colsEq, Math.max(4, .55 * colsEq.length))} = ${blank(R * C, 1.8)}</p></div></div>`;
  });
  return { body: cells(html, 2), items, ex: example('Rows go across. Columns go up and down. Add the rows, then add the columns: both give the same total.', '3 rows of 4: 4 + 4 + 4 = <b>12</b>. By columns: 3 + 3 + 3 + 3 = <b>12</b>.'),
    dirs: draw ? 'Draw each array in the box. Then write an addition equation by rows and another by columns.' : 'Write how many rows there are and how many are in each row. Then write an addition equation by rows and another by columns.',
    ican: 'I can use repeated addition to find the total in an array.', mistakes: 'Mixing up rows and columns. Rows go across, like rows of seats.',
    notes: 'Arrays have 2 to 5 rows and 2 to 5 columns. Both equations give the same total, which is worth pointing out.' };
}

/* ---------- the generator ---------- */
const BUILD = { count: skCount, tenframe: skTenframe, teen: skTeen, trace: skTrace, seq: skSeq, numline: skNumline, bonds: skBonds, maketen: skMaketen,
  blocks: skBlocks, expanded: skExpanded, tenmore: skTenmore, clock: skClock, coins: skCoins, evenodd: skEvenodd, arrays: skArrays,
  compare: (v, r, n) => v.grade === 'k' ? skCompareK(v, r, n) : skCompare12(v, r, n), length: (v, r, n) => v.grade === 'k' ? skLengthK(v, r, n) : v.grade === '1' ? skLength1(v, r, n) : skLength2(v, r, n) };

Gen.add('early-number', {
  title: 'Early Number', type: 'Practice',
  css: `.en-cells{display:grid;grid-template-columns:repeat(var(--c),minmax(0,1fr));gap:10px 14px;margin:6px 0 10px}
.en-cell{border:1px solid #bbb;border-radius:8px;padding:6px 8px;break-inside:avoid;display:flex;gap:6px;align-items:flex-start}
.en-cell>.ws-num{flex:none}
.en-cell>div{flex:1;min-width:0}
.en-cell p{margin:3px 0}
.en-cell .gen-svg,.en-line .gen-svg{margin:2px 0}
.en-row{display:flex;align-items:center;gap:10px}
.en-row>.gen-svg{flex:0 1 auto;min-width:0}
.en-big .ws-blank,.en-k .ws-blank{font-size:22px}
.en-k{font-size:18px}
.en-lab{font-size:13px}
.en-opts{display:flex;flex-direction:column;gap:1px;flex:none}
.en-pair{display:flex;gap:26px;justify-content:center}
.en-opt{display:inline-grid;place-items:center;width:1.55em;height:1.55em;font:600 24px/1 var(--sans);border:2.5px solid transparent;border-radius:50%}
.show-key .en-opt.en-ok{border-color:#b03020;color:#b03020}
.en-center{text-align:center}
.en-same{display:inline-block;border:1.5px solid #333;border-radius:6px;padding:0 12px;font-weight:600}
.show-key .en-same.en-ok{border:2.5px solid #b03020;color:#b03020;border-radius:50%}
.en-chains{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 16px;margin:6px 0 10px}
.en-chainrow{display:flex;align-items:center;gap:6px;break-inside:avoid}
p.en-step{font:600 12px var(--sans);color:#444;margin:0 0 2px}
.en-chain{display:flex;align-items:center;gap:4px}
.en-seg{display:inline-grid;place-items:center;width:.52in;height:.52in;border:2px solid #222;border-radius:50%;font:600 15px var(--sans);flex:none}
.en-k .en-seg{width:.6in;height:.6in;font-size:20px}
.en-seg.en-given{background:#e8e8e8;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.en-seg .ws-blank{border:0;min-width:0!important;margin:0}
.en-line{display:flex;gap:6px;align-items:flex-start;margin:4px 0 10px;break-inside:avoid}
.en-line>div{flex:1;min-width:0}
.en-line p{margin:2px 0}
p.en-mark{margin:0 0 4px;font-size:14px}
.en-sym{display:inline-grid;place-items:center;width:1.7em;height:1.7em;border:1.5px solid #333;border-radius:50%;vertical-align:middle;margin:0 4px}
.en-cmp{white-space:nowrap;font-size:17px}
.en-eq{font-size:16px}
.en-time{font-weight:700;font-size:17px;text-align:center}
.en-name{font-weight:700}
.en-table td,.en-table th{text-align:center}
.en-legend{display:flex;flex-wrap:wrap;gap:6px 22px;align-items:center;border:1.5px solid #333;border-radius:6px;padding:4px 10px}
.en-legend>div{display:flex;align-items:center;gap:6px;font-weight:600}
.en-legend .gen-svg{margin:0;width:.62in}
.en-ways{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.en-way{border:1.5px solid #333;border-radius:6px;height:.85in;padding:4px 6px;font-size:13px}
.en-arr{display:flex;gap:8px;align-items:center}
.en-arr>.gen-svg{flex:none;width:1.3in}
.en-arr p{margin:3px 0;font-size:14px}
@media print{.en-cells{gap:8px 12px}.en-line{margin-bottom:6px}}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '1' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => SKILLS[v.grade], def: 'blocks' },
    { id: 'task', label: 'Task', type: 'select', options: v => tasks(v), def: 'mix', show: hasTask },
    { id: 'range', label: 'Numbers', type: 'select', options: v => ranges(v), def: '10', show: hasRange },
    { id: 'by', label: 'Count by', type: 'select', options: [['mix', '5s, 10s and 100s'], ['5', '5s'], ['10', '10s'], ['100', '100s']], def: 'mix',
      show: v => v.grade === '2' && (v.skill === 'seq' || v.skill === 'numline') },
    { id: 'layout', label: 'Groups', type: 'select', options: [['mix', 'Mixed: rows, circles and scattered'], ['row', 'In a row'], ['ring', 'In a circle'], ['scatter', 'Scattered']], def: 'mix',
      show: v => v.grade === 'k' && v.skill === 'count' },
    { id: 'whole', label: 'Whole', type: 'select', options: [['mix', 'Any number 2 to 10'], ...[3, 4, 5, 6, 7, 8, 9, 10].map(k => [String(k), `Every way to make ${k}`])], def: 'mix',
      show: v => v.grade === 'k' && v.skill === 'bonds' },
    { id: 'coinlabel', label: 'Coin labels', type: 'select', options: [['both', 'Name and value'], ['name', 'Name only']], def: 'both', show: v => v.grade === '2' && v.skill === 'coins' },
    { id: 'words', label: 'Add the number word to trace', type: 'check', def: false, show: v => v.grade === 'k' && v.skill === 'trace' },
    { id: 'frames', label: 'Add a sentence frame to say each answer', type: 'check', def: false, show: hasFrames },
    { id: 'count', label: 'Length', type: 'select', options: v => [['s', `Fewer (${plan({ ...v, count: 's' })})`], ['m', `Standard (${plan({ ...v, count: 'm' })})`], ['l', `More (${plan({ ...v, count: 'l' })})`]], def: 'm' },
  ],
  make(v, r) {
    const g = v.grade, skill = v.skill, n = plan(v);
    const w = { ...v, task: taskOf(v), frames: hasFrames(v) && !!v.frames, words: g === 'k' && skill === 'trace' && !!v.words };
    const res = BUILD[skill](w, r, n);
    const label = SKILLS[g].find(s => s[0] === skill)[1], gname = GRADES.find(x => x[0] === g)[1];
    const parts = [];
    if (res.ex && g !== 'k') parts.push(part('', res.ex));
    if (res.body) parts.push(part('', res.body));
    if (res.parts) parts.push(...res.parts);
    const tl = hasTask(v) ? tasks(v).find(t => t[0] === w.task)[1] : '';
    return {
      title: `${label.replace(/ \(.*\)$/, '').replace(/: .*$/, '')}: ${gname}`,
      level: gname + (tl ? `, ${tl.charAt(0).toLowerCase() + tl.slice(1)}` : '') + (hasRange(v) ? `, numbers ${ranges(v).find(x => x[0] === v.range)[1].toLowerCase()}` : ''),
      ican: res.ican, directions: res.dirs, minutes: g === 'k' ? 15 : 20, materials: res.materials || (g === 'k' ? 'pencil, crayons' : 'pencil'),
      parts, items: res.items, mistakes: res.mistakes, notes: res.notes + ' Press New sheet for a fresh set at the same level.',
    };
  },
  verify(s, v) {
    const out = [], g = v.grade;
    const bad = (it, msg) => out.push(`${it.q}: ${msg}`);
    const val = { q: 25, d: 10, n: 5, p: 1 };
    const unword = t => { let cur = 0; for (const w of String(t).split(/[\s-]+/)) { if (w === 'hundred') { cur *= 100; continue; } const i = ONES.indexOf(w), j = TENS.indexOf(w); if (i >= 0) cur += i; else if (j >= 2) cur += 10 * j; else return NaN; } return cur; };
    for (const it of s.items) {
      switch (it.k) {
        case 'count': if (it.drawn !== +it.a) bad(it, `drew ${it.drawn}, key ${it.a}`); if (it.opts && (it.opts.filter(o => o === it.drawn).length !== 1 || new Set(it.opts).size !== 3)) bad(it, 'choices'); break;
        case 'tf': if (it.a !== `${it.drawn}; ${10 - it.drawn}`) bad(it, 'ten frame'); break;
        case 'teen': if (it.a !== `10 + ${it.f2} = ${it.f1 + it.f2}` || it.f1 + it.f2 < 11 || it.f1 + it.f2 > 19) bad(it, 'teen'); break;
        case 'num2': if (+it.a !== (it.x > it.y ? it.x : it.y) || it.x === it.y) bad(it, 'greater'); break;
        case 'cmpk': { const want = it.na === it.nb ? 'same' : (it.na > it.nb) === (it.ask !== 'fewer') ? 'first' : 'second'; if (it.a !== want) bad(it, `want ${want}`); break; }
        case 'trace': if (it.drawn !== +it.a) bad(it, 'trace count'); if (it.word && unword(it.word) !== +it.a) bad(it, `word ${it.word}`); break;
        case 'seq': {
          for (let i = 1; i < it.vals.length; i++) if (it.vals[i] - it.vals[i - 1] !== it.d) bad(it, 'step');
          if (it.vals.some(x => x < 0 || x > (g === 'k' ? 100 : g === '1' ? 120 : 1000))) bad(it, 'out of range');
          if (it.a !== it.hide.map(i => show(it.vals[0] + i * it.d)).join(', ')) bad(it, 'answers');
          if (it.hide.includes(0) || !it.hide.length) bad(it, 'hidden');
          break;
        }
        case 'nlbox': if (it.a !== show(it.s + it.i * it.d)) bad(it, 'box'); break;
        case 'nlmark': if (it.v !== it.s + it.i * it.d) bad(it, 'mark'); break;
        case 'ba': if (it.a !== `${it.n - 1}, ${it.n + 1}` || it.n - 1 < 0) bad(it, 'before/after'); break;
        case 'bond': if (it.dark + it.light !== it.N || it.a !== `${it.dark} and ${it.light}`) bad(it, 'bond'); break;
        case 'lenk': { const top = it.ask === 'shorter' ? it.la < it.lb : it.la > it.lb; if (it.a !== (top ? 'top' : 'bottom') || it.la === it.lb) bad(it, 'length'); break; }
        case 'maketen': if (it.x + it.need !== 10 || it.need + it.rest !== it.y || it.rest < 1 || it.sum !== it.x + it.y) bad(it, 'make ten'); break;
        case 'blocks': {
          const [f, rd, o] = it.drawn;
          if (100 * f + 10 * rd + o !== it.num || o > 9 || rd > 9) bad(it, `blocks ${it.drawn} for ${it.num}`);
          if (!String(it.a).includes(`${rd} tens ${o} ones`) || (g === '2' && !String(it.a).startsWith(`${f} hundreds`))) bad(it, 'chart');
          break;
        }
        case 'two': if (10 * it.drawn[1] + it.drawn[2] !== it.num || it.t2 * 10 + it.o2 !== it.num || it.t * 10 + it.o !== it.num || it.o2 < 10) bad(it, 'two ways'); break;
        case 'exp1': { const p = String(it.a).match(/\d+/g).map(Number); const got = it.kind === 'te' ? 10 * p[0] + p[1] : it.kind === 'ex' ? p[0] + p[1] : p[0]; if (got !== it.x) bad(it, 'expanded'); break; }
        case 'exp2': { const ps = it.ex.split(' + '); if (ps.reduce((a, b) => a + +b, 0) !== it.x || unword(it.wd) !== it.x || ps.some(p => !/^[1-9]0*$/.test(p))) bad(it, 'forms'); break; }
        case 'cmp': { const d = it.x - it.y, want = d > 0 ? '>' : d < 0 ? '<' : '='; if (it.a !== want) bad(it, 'symbol'); if (it.ph && it.ph !== { '>': 'greater than', '<': 'less than', '=': 'equal to' }[want]) bad(it, 'phrase'); break; }
        case 'order': { const s2 = [...it.nums].sort((a, b) => a - b); if (it.a !== s2.join(', ') || new Set(it.nums).size !== 4) bad(it, 'order'); break; }
        case 'tm': if (it.a !== it.ds.map(d => it.x + d).join(', ') || it.ds.some(d => it.x + d < 0 || it.x + d > (g === '1' ? 100 : 999))) bad(it, 'ten more'); break;
        case 'piece': {   // rebuild the 120 chart and look up the neighbor
          const row = Math.floor((it.x - 1) / 10), col = (it.x - 1) % 10;
          const [rr, cc] = { up: [row - 1, col], down: [row + 1, col], left: [row, col - 1], right: [row, col + 1] }[it.d];
          if (cc < 0 || cc > 9 || rr < 0 || rr > 11) bad(it, 'off the chart');
          else if (+it.a !== rr * 10 + cc + 1) bad(it, `want ${rr * 10 + cc + 1}`);
          break;
        }
        case 'clock': {
          const mm = Math.round(it.ma / 6) % 60, base = Math.floor(it.ha / 30 + 1e-9), hh = base % 12 || 12;
          if (Math.abs(it.ha - 30 * base - mm / 2) > 1e-6) bad(it, 'hour hand not where the minutes put it');
          if (it.a !== `${hh}:${String(mm).padStart(2, '0')}`) bad(it, `hands show ${hh}:${mm}`);
          if (mm % (g === '1' ? 30 : 5)) bad(it, 'minutes');
          break;
        }
        case 'units': if (it.drawn !== +it.a || it.len !== it.drawn * it.u) bad(it, 'units'); break;
        case 'lensay': if (it.a !== (it.x > it.y ? 'longer' : 'shorter') || it.x === it.y) bad(it, 'say'); break;
        case 'order3': { const s2 = it.ls.slice().sort((a, b) => b - a); if (it.a !== it.ls.map(l => s2.indexOf(l) + 1).join(', ') || new Set(it.ls).size !== 3) bad(it, 'rank'); break; }
        case 'ruler': { const L = it.e - it.s; if (it.both ? it.a !== `${L} in; ${Math.round(L * 2.54)} cm` || Math.abs(L * 2.54 - Math.round(L * 2.54)) > .4 : it.a !== String(L)) bad(it, 'ruler'); if (it.e > (it.unit === 'in' ? 6 : 16) || L < 1) bad(it, 'off the ruler'); break; }
        case 'which': break;
        case 'trans': { const len = { [it.chain[0]]: 3, [it.chain[1]]: 2, [it.chain[2]]: 1 }; const w = len[it.ask[0]] > len[it.ask[1]] ? it.ask[0] : it.ask[1]; if (it.a !== w || new Set(it.chain).size !== 3) bad(it, 'third object'); break; }
        case 'diff': { const d = Math.abs(it.la - it.lb); if (d !== it.d || it.longer !== (it.la > it.lb ? 'A' : 'B') || !it.a.endsWith(`= ${d}; ${it.longer}`)) bad(it, 'diff'); break; }
        case 'coins': { const t = it.coins.reduce((a, k) => a + val[k], 0); if (`${t}¢` !== it.a) bad(it, `coins make ${t}`); break; }
        case 'buy': { const t = it.coins.reduce((a, k) => a + val[k], 0), yes = t >= it.price; if (it.a !== `${t}¢; ${yes ? 'yes' : 'no'}; ${yes ? 0 : it.price - t}¢`) bad(it, 'buy'); break; }
        case 'make': {
          let best = 99;
          for (let q = 0; q <= 3; q++) for (let d = 0; d <= 9; d++) for (let nn = 0; nn <= 19; nn++) { const p = it.A - 25 * q - 10 * d - 5 * nn; if (p >= 0) best = Math.min(best, q + d + nn + p); }
          if (it.ways.some(w => 25 * w.q + 10 * w.d + 5 * w.n + w.p !== it.A)) bad(it, 'a way adds up wrong');
          if (it.ways[0].q + it.ways[0].d + it.ways[0].n + it.ways[0].p !== best) bad(it, `fewest is ${best}`);
          if (new Set(it.ways.map(w => `${w.q} ${w.d} ${w.n} ${w.p}`)).size !== 3) bad(it, 'ways repeat');
          break;
        }
        case 'dbl': if (it.a !== `${it.x / 2} + ${it.x / 2}` || it.x % 2) bad(it, 'doubles'); break;
        case 'eo': if (it.drawn !== it.x || (it.x % 2 ? it.a !== 'odd' : it.a !== `even; ${it.x / 2} + ${it.x / 2}`)) bad(it, 'odd or even'); break;
        case 'arr': {
          const rs = it.rowsEq.split(' + ').map(Number), cs = it.colsEq.split(' + ').map(Number);
          if (rs.length !== it.R || rs.some(x => x !== it.C) || cs.length !== it.C || cs.some(x => x !== it.R)) bad(it, 'equations');
          if (it.dots !== rs.reduce((a, b) => a + b, 0) || it.dots !== cs.reduce((a, b) => a + b, 0)) bad(it, `drew ${it.dots}`);
          break;
        }
        default: bad(it, `unknown kind ${it.k}`);
      }
    }
    return out;
  },
});
})();
