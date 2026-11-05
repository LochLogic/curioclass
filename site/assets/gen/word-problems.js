// Word Problems generator, grades 1-6. Short everyday stories with clear numbers: joining and taking apart (1.OA.1,
// 2.OA.1), money (2.MD.8, 4.MD.2), elapsed time (3.MD.1, 4.MD.2), measurement and conversion (2.MD.5, 3.MD.2, 4.MD.1-2,
// 5.MD.1), equal groups and sharing (2.OA.4, 3.OA.3, 4.OA.3), interpreting remainders (4.OA.3: round up, drop it or
// report it, with a "What does the remainder mean?" line), multi-step problems, fractions of amounts (5.NF.4, 5.NF.6)
// and rates and percents (6.RP.3). Every story is built from its numbers, and every answer has a unit.
(() => {
const H = Gen.h, { part, example, esc } = H;
const { fmt } = Gen.m;

const GRADES = [['1', 'Grade 1'], ['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'], ['6', 'Grade 6']];
const TOPICS = {
  join: 'Adding and subtracting', money: 'Money', time: 'Time', measure: 'Measurement', groups: 'Equal groups and sharing',
  multi: 'Multi-step', frac: 'Fractions of amounts', rates: 'Rates and percents', remainders: 'Interpreting remainders',
};
const BYGRADE = { 1: ['join', 'time', 'measure'], 2: ['join', 'money', 'time', 'measure', 'groups'], 3: ['money', 'time', 'measure', 'groups', 'multi'],
  4: ['money', 'time', 'measure', 'groups', 'multi', 'remainders'], 5: ['money', 'time', 'measure', 'groups', 'multi', 'frac'], 6: ['money', 'time', 'measure', 'multi', 'frac', 'rates'] };

const NAMES = ['Ava', 'Ben', 'Carlos', 'Chloe', 'Diego', 'Elena', 'Emma', 'Ethan', 'Grace', 'Isaac', 'Jamal', 'Kai', 'Leo', 'Liam', 'Lucia', 'Maya',
  'Mia', 'Noah', 'Olivia', 'Omar', 'Owen', 'Priya', 'Rosa', 'Sam', 'Sofia', 'Theo', 'Zoe', 'Mateo', 'Nina', 'Jack', 'Ruby', 'Eli'];
const THINGS = [['sticker', 'stickers'], ['marble', 'marbles'], ['crayon', 'crayons'], ['seashell', 'seashells'], ['bead', 'beads'], ['baseball card', 'baseball cards'],
  ['stamp', 'stamps'], ['rock', 'rocks'], ['pencil', 'pencils'], ['button', 'buttons'], ['acorn', 'acorns'], ['toy car', 'toy cars'], ['leaf', 'leaves']];
const FOOD = [['cookie', 'cookies'], ['strawberry', 'strawberries'], ['cracker', 'crackers'], ['grape', 'grapes'], ['muffin', 'muffins'], ['orange slice', 'orange slices'], ['carrot stick', 'carrot sticks']];
// things to buy, with a sensible price range in cents
const SHOP = [['notebook', 150, 450], ['pen', 99, 299], ['juice box', 75, 199], ['apple', 50, 125], ['sandwich', 350, 795], ['bag of popcorn', 150, 450], ['eraser', 50, 150],
  ['ruler', 99, 250], ['comic book', 299, 599], ['water bottle', 99, 299], ['yo-yo', 199, 499], ['box of crayons', 199, 499], ['kite', 599, 1299], ['puzzle', 499, 1299],
  ['soccer ball', 899, 1599], ['book', 499, 1299], ['plant', 399, 999], ['T-shirt', 599, 1499], ['banana', 25, 60], ['pencil', 25, 95]];
const price = (r, it, step = 1) => { const lo = Math.ceil(it[1] / step), hi = Math.floor(it[2] / step); return lo > hi ? null : r.int(lo, hi) * step; };
// short activities for grades 1-2, each with the longest it sensibly lasts, in hours
const ACTS12 = [['reading', 1], ['soccer practice', 2], ['piano practice', 1], ['a bike ride', 2], ['art class', 1], ['swim lessons', 1], ['a movie', 2], ['homework', 1], ['a hike', 3], ['a picnic', 2]];
const ACTS = ['reading', 'soccer practice', 'piano practice', 'a bike ride', 'art class', 'swim lessons', 'a movie', 'homework', 'a hike', 'chess club'];

/* ---------- formatting ---------- */
const money = (c, g) => (c < 100 && +g <= 3) ? `${c}¢` : `$${c % 100 === 0 && +g <= 3 ? c / 100 : (c / 100).toFixed(2)}`;
const money2 = c => `$${(c / 100).toFixed(2)}`;
const clock = (m, ampm = true) => { m = ((m % 1440) + 1440) % 1440; const h24 = Math.floor(m / 60), mm = m % 60, h = h24 % 12 || 12;
  return `${h}:${String(mm).padStart(2, '0')}${ampm ? (h24 < 12 ? ' a.m.' : ' p.m.') : ''}`; };
const dur = m => { const h = Math.floor(m / 60), mm = m % 60;
  return [h ? `${h} hour${h > 1 ? 's' : ''}` : '', mm ? `${mm} minute${mm > 1 ? 's' : ''}` : ''].filter(Boolean).join(' ') || '0 minutes'; };
const mixedText = (n, d) => { const w = Math.floor(n / d), rr = n % d, g = Gen.m.gcd(rr, d); return rr ? `${w ? w + ' ' : ''}${rr / g}/${d / g}` : String(w); };
const plural = (n, [one, many]) => n === 1 ? one : many;
const big = n => fmt(n, 2);

/* ---------- the templates: each makes {text, ans, unit, type, f, vals, show, steps} or null ----------
   type: num | money | clock | dur.  f: the answer as a formula over vals (cents for money, minutes for time), worked
   again by verify.  show: number strings that must appear in the story.  */
const T = [];
const add = (topics, lo, hi, make) => T.push({ topics, lo, hi, make });

// joining and taking apart, grades 1-2
add(['join'], 1, 2, (r, g, A, B) => { const it = r.pick(THINGS), max = g === '1' ? 20 : 100, x = r.int(g === '1' ? 2 : 12, max - 10), y = r.int(2, max - x);
  return { text: `${A} has ${x} ${it[1]}. ${B} gives ${A} ${y} more. How many ${it[1]} does ${A} have now?`, ans: x + y, unit: it[1], f: 'x+y', vals: { x, y }, steps: `${x} + ${y} = ${x + y}` }; });
add(['join'], 1, 2, (r, g, A, B) => { const it = r.pick(THINGS), max = g === '1' ? 20 : 100, x = r.int(g === '1' ? 6 : 25, max), y = r.int(2, x - 1);
  return { text: `${A} had ${x} ${it[1]}. ${A} gave ${y} of them to ${B}. How many ${it[1]} does ${A} have left?`, ans: x - y, unit: it[1], f: 'x-y', vals: { x, y }, steps: `${x} − ${y} = ${x - y}` }; });
add(['join'], 1, 2, (r, g, A, B) => { const it = r.pick(THINGS), max = g === '1' ? 20 : 100, x = r.int(g === '1' ? 5 : 20, max), y = r.int(1, x - 2);
  return { text: `${A} has ${x} ${it[1]}. ${B} has ${y} ${plural(y, it)}. How many more ${it[1]} does ${A} have than ${B}?`, ans: x - y, unit: it[1], f: 'x-y', vals: { x, y }, steps: `${x} − ${y} = ${x - y}` }; });
add(['join'], 1, 2, (r, g, A) => { const it = r.pick(THINGS), max = g === '1' ? 20 : 100, z = r.int(g === '1' ? 8 : 30, max), x = r.int(1, z - 2);
  return { text: `${A} has ${x} ${plural(x, it)}. ${A} wants to have ${z}. How many more ${it[1]} does ${A} need?`, ans: z - x, unit: it[1], f: 'z-x', vals: { x, z }, steps: `${x} + ? = ${z}, so ${z} − ${x} = ${z - x}` }; });
add(['join'], 1, 2, (r, g) => { const f = r.pick(FOOD), max = g === '1' ? 20 : 100, x = r.int(2, max / 2), y = r.int(2, max / 2), z = g === '1' ? r.int(1, 5) : r.int(3, 20);
  if (g === '1' && x + y + z > 20) return null;
  return { text: `A plate has ${x} ${f[1]}. Then ${y} more ${f[1]} are added, and later ${z} more. How many ${f[1]} are on the plate now?`, ans: x + y + z, unit: f[1], f: 'x+y+z', vals: { x, y, z }, steps: `${x} + ${y} + ${z} = ${x + y + z}` }; });
add(['join'], 1, 2, (r, g, A) => { const max = g === '1' ? 18 : 90, red = r.int(2, max / 2), blue = r.int(2, max / 2);
  return { text: `${A} has some balloons. ${red} are red and ${blue} are blue. How many balloons does ${A} have?`, ans: red + blue, unit: 'balloons', f: 'red+blue', vals: { red, blue }, steps: `${red} + ${blue} = ${red + blue}` }; });

// money
add(['money'], 2, 2, (r, g, A) => { const q = r.int(0, 3), d = r.int(1, 4), n = r.int(0, 3), p = r.int(0, 4), c = 25 * q + 10 * d + 5 * n + p; if (c > 99 || c < 15) return null;
  const parts = [q && `${q} ${q === 1 ? 'quarter' : 'quarters'}`, `${d} ${d === 1 ? 'dime' : 'dimes'}`, n && `${n} ${n === 1 ? 'nickel' : 'nickels'}`, p && `${p} ${p === 1 ? 'penny' : 'pennies'}`].filter(Boolean);
  return { text: `${A} has ${parts.slice(0, -1).join(', ')} and ${parts[parts.length - 1]}. How many cents does ${A} have?`, ans: c, unit: 'cents', type: 'cents', f: '25*q+10*d+5*n+p', vals: { q, d, n, p },
    steps: `${[q && `${q} × 25`, `${d} × 10`, n && `${n} × 5`, p && `${p} × 1`].filter(Boolean).join(' + ')} = ${c}¢` }; });
add(['money'], 2, 2, (r, g, A) => { const item = r.pick(SHOP.filter(x => x[1] < 100)), cost = Math.min(95, price(r, item, 5)), it = item[0];
  return { text: `A ${it} costs ${cost}¢. ${A} pays with one dollar (100¢). How much change does ${A} get?`, ans: 100 - cost, unit: 'cents', type: 'cents', f: '100-cost', vals: { cost }, steps: `100 − ${cost} = ${100 - cost}¢` }; });
add(['money'], 2, 2, (r, g, A) => { const ones = r.int(1, 9), fives = r.int(1, 4), tens = r.int(1, 3);
  return { text: `${A} has ${tens} ten-dollar ${tens === 1 ? 'bill' : 'bills'}, ${fives} five-dollar ${fives === 1 ? 'bill' : 'bills'} and ${ones} one-dollar ${ones === 1 ? 'bill' : 'bills'}. How many dollars does ${A} have?`,
    ans: 5 * fives + 10 * tens + ones, unit: 'dollars', f: '5*fives+10*tens+ones', vals: { fives, tens, ones }, steps: `${fives} × 5 + ${tens} × 10 + ${ones} = ${5 * fives + 10 * tens + ones}` }; });
add(['money'], 3, 3, (r, g, A) => { const [x1, x2] = r.sample(SHOP.filter(x => x[2] >= 500), 2), i1 = x1[0], i2 = x2[0], a = price(r, x1, 100) / 100, b = price(r, x2, 100) / 100, paid = a + b < 20 ? 20 : 50;
  if (!a || !b || a + b >= paid) return null;
  return { text: `${A} buys a ${i1} for $${a} and a ${i2} for $${b}. ${A} pays with a $${paid} bill. How much change does ${A} get?`, ans: (paid - a - b) * 100, type: 'money', f: '(paid-a-b)*100', vals: { a, b, paid },
    steps: `$${a} + $${b} = $${a + b}; $${paid} − $${a + b} = $${paid - a - b}` }; });
add(['money'], 3, 3, (r, g, A) => { const n = r.int(3, 9), each = r.int(2, 9), it = r.pick(['ticket', 'book', 'plant', 'toy']);
  return { text: `Each ${it} costs $${each}. ${A} buys ${n} of them. How much does ${A} spend?`, ans: n * each * 100, type: 'money', f: 'n*each*100', vals: { n, each }, steps: `${n} × $${each} = $${n * each}` }; });
add(['money'], 4, 6, (r, g, A) => { const [x1, x2, x3] = r.sample(SHOP, 3), [i1, i2, i3] = [x1[0], x2[0], x3[0]], a = price(r, x1), b = price(r, x2), three = r.chance(.5), c = three ? price(r, x3) : 0;
  const paid = r.pick([1000, 2000]), tot = a + b + c; if (tot >= paid) return null;
  return { text: `${A} buys a ${i1} for ${money2(a)}${three ? ',' : ' and'} a ${i2} for ${money2(b)}${three ? ` and a ${i3} for ${money2(c)}` : ''}. ${A} pays with a ${money2(paid).replace('.00', '')} bill. How much change does ${A} get?`,
    ans: paid - tot, type: 'money', f: 'paid-a-b-c', vals: { a, b, c, paid }, steps: `${money2(a)} + ${money2(b)}${three ? ` + ${money2(c)}` : ''} = ${money2(tot)}; ${money2(paid)} − ${money2(tot)} = ${money2(paid - tot)}` }; });
add(['money'], 4, 6, (r, g, A) => { const n = r.int(3, g === '4' ? 6 : 12);
  // each thing with a sensible price range in cents
  const [it, lo, hi] = r.pick([['notebooks', 150, 499], ['packs of seeds', 99, 399], ['bottles of glue', 99, 349], ['granola bars', 50, 199], ['tickets', 300, 899], ['postcards', 50, 199]]), each = r.int(lo, hi);
  if (g === '4' && (each % 5 || each > 450)) return null;
  return { text: `${it[0].toUpperCase() + it.slice(1)} cost ${money2(each)} each. ${A} buys ${n} of them. How much does ${A} spend in all?`, ans: n * each, type: 'money', f: 'n*each', vals: { n, each }, steps: `${n} × ${money2(each)} = ${money2(n * each)}` }; });
add(['money'], 5, 6, (r, g, A) => { const w = r.int(4, 12), save = r.int(3, 15) * 100 + r.pick([0, 25, 50, 75]), spend = r.int(5, 30) * 100; if (spend >= w * save) return null;
  return { text: `${A} saves ${money2(save)} each week for ${w} weeks, then spends ${money2(spend)} on a gift. How much money does ${A} have left?`, ans: w * save - spend, type: 'money', f: 'w*save-spend', vals: { w, save, spend },
    steps: `${w} × ${money2(save)} = ${money2(w * save)}; ${money2(w * save)} − ${money2(spend)} = ${money2(w * save - spend)}` }; });

// time
add(['time'], 1, 2, (r, g, A) => { const start = r.int(7, 17) * 60 + (g === '1' ? r.pick([0, 30]) : r.pick([0, 15, 30, 45])), [act, most] = r.pick(ACTS12), len = g === '1' ? r.int(1, most) * 60 : r.pick([30, 60, 90, 120].filter(m => m <= most * 60));
  return { text: `${A} starts ${act} at ${clock(start, false)}. It lasts ${dur(len)}. What time does it end?`, ans: start + len, type: 'clock12', f: 'start+len', vals: { start, len }, show: [clock(start, false), dur(len)],
    steps: `${clock(start, false)} + ${dur(len)} = ${clock(start + len, false)}` }; });
add(['time'], 3, 3, (r, g, A) => { const start = r.int(8, 16) * 60 + r.int(0, 11) * 5, len = r.int(2, 11) * 5 + (r.chance(.4) ? 0 : 0), act = r.pick(ACTS);
  return { text: `${A} starts ${act} at ${clock(start)} and finishes at ${clock(start + len)}. How many minutes does it take?`, ans: len, type: 'dur', f: 'end-start', vals: { start, end: start + len }, show: [clock(start), clock(start + len)],
    steps: `from ${clock(start)} to ${clock(start + len)} is ${len} minutes` }; });
add(['time'], 3, 4, (r, g, A) => { const start = r.int(8, 16) * 60 + r.int(0, 11) * 5, len = g === '3' ? r.int(3, 12) * 5 : r.int(5, 30) * 5, act = r.pick(ACTS);
  return { text: `${A} starts ${act} at ${clock(start)}. It lasts ${dur(len)}. What time does ${A} finish?`, ans: start + len, type: 'clock', f: 'start+len', vals: { start, len }, show: [clock(start), dur(len)],
    steps: `${clock(start)} + ${dur(len)} = ${clock(start + len)}` }; });
add(['time'], 4, 6, (r, g, A) => { const start = r.int(7, 15) * 60 + r.int(0, 11) * 5, len = r.int(g === '4' ? 13 : 20, g === '4' ? 40 : 90) * 5, act = r.pick(['a road trip', 'a museum visit', 'a hike', 'a volunteer shift', 'a tournament', 'a field trip']);
  return { text: `${A} leaves for ${act} at ${clock(start)} and gets back at ${clock(start + len)}. How long is ${A} gone?`, ans: len, type: 'dur', f: 'end-start', vals: { start, end: start + len }, show: [clock(start), clock(start + len)],
    steps: `from ${clock(start)} to ${clock(start + len)} is ${dur(len)}` }; });
add(['time'], 4, 6, (r, g, A) => { const days = r.int(3, 7), m = r.int(4, 12) * 5, act = r.pick(['practices the violin', 'reads', 'jogs', 'practices typing', 'walks the dog']);
  return { text: `${A} ${act} for ${m} minutes a day for ${days} days. How much time is that in all? Write it in hours and minutes.`, ans: days * m, type: 'dur', f: 'days*m', vals: { days, m },
    steps: `${days} × ${m} = ${days * m} minutes = ${dur(days * m)}` }; });
add(['time'], 5, 6, (r, g, A) => { const end = r.int(13, 21) * 60 + r.int(0, 11) * 5, len = r.int(18, 40) * 5, act = r.pick(['a movie', 'a concert', 'a game', 'a play']);
  return { text: `${act[0].toUpperCase() + act.slice(1)} ends at ${clock(end)}. It lasted ${dur(len)}. What time did it start?`, ans: end - len, type: 'clock', f: 'end-len', vals: { end, len }, show: [clock(end), dur(len)],
    steps: `${clock(end)} − ${dur(len)} = ${clock(end - len)}` }; });

// measurement
// lengths in linking cubes (about 2 cm each), kept near the real size of each thing
const CUBELEN = { crayon: [3, 5], marker: [6, 8], spoon: [6, 9], toothbrush: [8, 10], pencil: [5, 10], paintbrush: [9, 15], shoe: [9, 13] };
add(['measure'], 1, 1, (r, g, A, B) => { const [o1, o2] = r.sample(Object.keys(CUBELEN), 2), a = r.int(...CUBELEN[o1]), b = r.int(...CUBELEN[o2]); if (a <= b || a > 20) return null;
  return { text: `${A}'s ${o1} is ${a} cubes long. ${B}'s ${o2} is ${b} cubes long. How much longer is the ${o1}?`, ans: a - b, unit: 'cubes', f: 'a-b', vals: { a, b }, steps: `${a} − ${b} = ${a - b}` }; });
add(['measure'], 2, 2, (r, g, A) => { const u = r.pick([['centimeters', 'cm'], ['inches', 'in']]), a = r.int(30, 99), b = r.int(10, a - 5), obj = r.pick(['ribbon', 'piece of string', 'strip of paper', 'piece of yarn']);
  return { text: `${A} has a ${obj} that is ${a} ${u[0]} long. ${A} cuts off ${b} ${u[0]}. How long is the ${obj} now?`, ans: a - b, unit: u[0], f: 'a-b', vals: { a, b }, steps: `${a} − ${b} = ${a - b}` }; });
add(['measure'], 2, 2, (r, g, A) => { const a = r.int(12, 50), b = r.int(12, 45), u = r.pick(['feet', 'meters']);
  return { text: `${A} walks ${a} ${u} to the swings and then ${b} ${u} to the slide. How far does ${A} walk?`, ans: a + b, unit: u, f: 'a+b', vals: { a, b }, steps: `${a} + ${b} = ${a + b}` }; });
add(['measure'], 3, 3, (r, g, A) => { const n = r.int(2, 9), each = r.int(2, 9), c = r.pick([['pitcher', 'liters of water'], ['bag', 'kilograms of rice'], ['bucket', 'liters of paint']]);
  return { text: `${A} has ${n} ${c[0]}s. Each ${c[0]} holds ${each} ${c[1]}. How many ${c[1].split(' ')[0]} is that in all?`, ans: n * each, unit: c[1].split(' ')[0], f: 'n*each', vals: { n, each }, steps: `${n} × ${each} = ${n * each}` }; });
add(['measure'], 3, 3, (r, g, A) => { const a = 10 * r.int(20, 90), b = 10 * r.int(10, a / 10 - 5), m = r.pick(['a backpack', 'a box of books', 'a pumpkin']);  // tens, so the subtraction stays friendly
  return { text: `${m[0].toUpperCase() + m.slice(1)} has a mass of ${a} grams. ${A} takes out something with a mass of ${b} grams. What is the mass now?`, ans: a - b, unit: 'grams', f: 'a-b', vals: { a, b }, steps: `${a} − ${b} = ${a - b}` }; });
const CONV = [['feet', 'inches', 12], ['yards', 'feet', 3], ['meters', 'centimeters', 100], ['kilograms', 'grams', 1000], ['liters', 'milliliters', 1000], ['hours', 'minutes', 60], ['pounds', 'ounces', 16], ['gallons', 'quarts', 4]];
const CONVOBJ = { feet: 'board', yards: 'rope', meters: 'garden hose', kilograms: 'bag of flour', liters: 'jug of juice', hours: 'car trip', pounds: 'watermelon', gallons: 'fish tank' };
add(['measure'], 4, 6, (r, g, A) => { const [bigU, small, k] = r.pick(CONV), n = r.int(2, g === '4' ? 9 : 15);
  return { text: `A ${CONVOBJ[bigU]} ${bigU === 'hours' ? 'takes' : bigU === 'kilograms' || bigU === 'pounds' ? 'weighs' : bigU === 'liters' || bigU === 'gallons' ? 'holds' : 'is'} ${n} ${bigU}${bigU === 'hours' ? '' : bigU === 'kilograms' || bigU === 'pounds' || bigU === 'liters' || bigU === 'gallons' ? '' : ' long'}. How many ${small} is that?`,
    ans: n * k, unit: small, f: 'n*k', vals: { n, k }, show: [String(n)], steps: `1 ${bigU.replace(/s$/, '').replace('feet', 'foot')} = ${k} ${small}, so ${n} × ${k} = ${n * k}` }; });
add(['measure'], 4, 6, (r, g, A) => { const [bigU, small, k] = r.pick(CONV.filter(c => c[2] >= 12)), n = r.int(2, 6), cut = r.int(1, n * k - 1);
  const [verb, has] = { inches: ['cuts off', `a board that is ${n} ${bigU} long`], centimeters: ['cuts off', `a ribbon that is ${n} ${bigU} long`], grams: ['uses', `a bag with ${n} ${bigU} of flour`],
    milliliters: ['pours out', `a jug with ${n} ${bigU} of juice`], minutes: ['spends', `${n} ${bigU} of free time and`], ounces: ['uses', `${n} ${bigU} of clay for an art project`] }[small];
  if (cut % (k >= 100 ? 50 : k === 60 ? 5 : 1)) return null;
  return { text: small === 'minutes' ? `${A} has ${n} hours of free time and spends ${fmt(cut, 0)} minutes of it reading. How many minutes are left?` : `${A} has ${has}. ${A} ${verb} ${fmt(cut, 0)} ${small}. How many ${small} are left?`, ans: n * k - cut, unit: small, f: 'n*k-cut', vals: { n, k, cut }, show: [String(n), fmt(cut, 0)],
    steps: `${n} ${bigU} = ${fmt(n * k, 0)} ${small}; ${fmt(n * k, 0)} − ${fmt(cut, 0)} = ${fmt(n * k - cut, 0)}` }; });
add(['measure'], 5, 6, (r, g, A) => { const totalM = r.int(2, 9), piece = r.pick([20, 25, 50]);
  return { text: `${A} has a rope ${totalM} meters long and cuts it into pieces that are each ${piece} centimeters long. How many pieces does ${A} get?`, ans: totalM * 100 / piece, unit: 'pieces', f: 'm*100/piece', vals: { m: totalM, piece },
    steps: `${totalM} m = ${totalM * 100} cm; ${totalM * 100} ÷ ${piece} = ${totalM * 100 / piece}` }; });

// equal groups and sharing
add(['groups'], 2, 2, (r, g, A) => { const rows = r.int(2, 5), cols = r.int(2, 5), it = r.pick([['chairs', 'rows of'], ['muffins', 'rows of'], ['stamps', 'rows of'], ['plants', 'rows of']]);
  return { text: `${A} puts ${it[0]} in ${rows} rows. There are ${cols} ${it[0]} in each row. How many ${it[0]} are there?`, ans: rows * cols, unit: it[0], f: 'rows*cols', vals: { rows, cols }, steps: `${Array(rows).fill(cols).join(' + ')} = ${rows * cols}` }; });
add(['groups'], 3, 3, (r, g, A) => { const n = r.int(2, 9), each = r.int(2, 10), f = r.pick(FOOD);
  return { text: `${A} has ${n * each} ${f[1]} and shares them equally among ${n} friends. How many ${f[1]} does each friend get?`, ans: each, unit: f[1], f: 'total/n', vals: { total: n * each, n }, steps: `${n * each} ÷ ${n} = ${each}` }; });
add(['groups'], 3, 3, (r, g) => { const n = r.int(3, 9), each = r.int(3, 9), box = r.pick([['box', 'crayons'], ['bag', 'apples'], ['pack', 'juice boxes'], ['tray', 'muffins']]);
  return { text: `There are ${n} ${box[0]}s. Each ${box[0]} has ${each} ${box[1]}. How many ${box[1]} are there in all?`, ans: n * each, unit: box[1], f: 'n*each', vals: { n, each }, steps: `${n} × ${each} = ${n * each}` }; });
add(['groups'], 4, 5, (r, g) => { const per = r.int(4, 8), people = r.int(20, g === '4' ? 60 : 150); if (people % per === 0) return null;
  const v = r.pick([['van', 'students', 'go on a field trip'], ['table', 'guests', 'come to a party'], ['cabin', 'campers', 'stay at camp'], ['minivan', 'players', 'ride to a game']]);
  return { text: `${people} ${v[1]} ${v[2]}. Each ${v[0]} holds ${per} ${v[1]}. How many ${v[0]}s are needed so everyone fits?`, ans: Math.ceil(people / per), unit: `${v[0]}s`, f: 'ceil(people/per)', vals: { people, per },
    steps: `${people} ÷ ${per} = ${Math.floor(people / per)} R ${people % per}; the ${people % per} left over need one more ${v[0]}, so ${Math.ceil(people / per)}` }; });
add(['groups'], 4, 5, (r, g) => { const per = r.int(4, 12), items = r.int(30, g === '4' ? 99 : 500); if (items % per === 0) return null;
  const v = r.pick([['box', 'eggs'], ['bag', 'oranges'], ['bundle', 'pencils'], ['carton', 'juice boxes']]);
  const many = v[0] === 'box' ? 'boxes' : v[0] + 's';
  return { text: `A farm stand has ${items} ${v[1]}. Each ${v[0]} holds ${per} ${v[1]}. How many ${many} can be filled all the way?`,
    ans: Math.floor(items / per), unit: `full ${many}`, f: 'floor(items/per)', vals: { items, per }, steps: `${items} ÷ ${per} = ${Math.floor(items / per)} R ${items % per}; only ${Math.floor(items / per)} are full` }; });
add(['groups'], 5, 5, (r, g) => { const n = r.int(12, 36), each = r.int(12, 48);
  const [outer, inner, prep] = r.pick([['rows', 'seats', 'in'], ['chapters', 'pages', 'in'], ['sheets', 'stickers', 'on'], ['crates', 'apples', 'in'], ['shelves', 'books', 'on']]);
  return { text: `There are ${n} ${outer} with ${each} ${inner} ${prep} each. How many ${inner} are there in all?`, ans: n * each, unit: inner, f: 'n*each', vals: { n, each }, steps: `${n} × ${each} = ${fmt(n * each, 0)}` }; });
add(['groups'], 5, 5, (r, g) => { const groups = r.int(12, 32), each = r.int(11, 25), total = groups * each;
  const [who, what] = r.pick([['teams', 'players'], ['buses', 'riders'], ['classrooms', 'students'], ['boxes', 'oranges']]);
  return { text: `${fmt(total, 0)} ${what} are split equally into ${groups} ${who}. How many ${what} are in each of the ${who}?`, ans: each, unit: what, f: 'total/groups', vals: { total, groups }, show: [fmt(total, 0), String(groups)], steps: `${fmt(total, 0)} ÷ ${groups} = ${each}` }; });

// interpreting remainders, grade 4: every story divides with a remainder; the student says what to do with it
// (round up, drop it, or report it). meaning is the line the key shows under "What does the remainder mean?"
const rem = (r, lo, hi, per) => { for (let t = 0; t < 40; t++) { const n = r.int(lo, hi); if (n % per) return n; } return null; };
const remText = (n, per) => `${n} ÷ ${per} = ${Math.floor(n / per)} R ${n % per}`;
add(['remainders'], 4, 4, (r, g) => { const per = r.int(4, 9), v = r.pick([['van', 'students', 'go on a field trip'], ['bus', 'campers', 'ride to the lake'], ['boat', 'hikers', 'cross the river'], ['car', 'players', 'ride to a game']]), n = rem(r, 30, 99, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `${n} ${v[1]} ${v[2]}. Each ${v[0]} holds ${per} ${v[1]}. How many ${v[0]}s are needed so everyone goes?`, ans: q + 1, ansText: `${q + 1} ${v[0]}s`, unit: `${v[0]}s`, f: 'ceil(n/per)', vals: { n, per },
    meaning: `Round up: the ${rr} left over need one more ${v[0]}.`, steps: `${remText(n, per)}; the ${rr} left over need one more ${v[0]}, so ${q + 1}` }; });
add(['remainders'], 4, 4, (r, g, A) => { const per = r.pick([4, 5, 6, 8, 10, 12]), [it, box, many] = r.pick([['photos', 'album page', 'album pages'], ['cupcakes', 'box', 'boxes'], ['books', 'shelf', 'shelves'], ['toy cars', 'bin', 'bins']]), n = rem(r, 40, 150, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `${A} has ${n} ${it} to put away. Each ${box} holds ${per} ${it}. How many ${many} does ${A} need for all of them?`, ans: q + 1, ansText: `${q + 1} ${many}`, unit: many, f: 'ceil(n/per)', vals: { n, per },
    meaning: `Round up: the last ${rr} ${it} need a ${box} too.`, steps: `${remText(n, per)}; the last ${rr} ${it} need one more ${box}, so ${q + 1}` }; });
add(['remainders'], 4, 4, (r, g) => { const per = r.int(3, 9), [ride, what] = r.pick([['ferry', 'cars'], ['elevator', 'people'], ['ski lift', 'skiers'], ['raft', 'riders']]), n = rem(r, 20, 80, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `A ${ride} carries ${per} ${what} at a time. ${n} ${what} are waiting. How many trips does the ${ride} make to carry them all?`, ans: q + 1, ansText: `${q + 1} trips`, unit: 'trips', f: 'ceil(n/per)', vals: { n, per },
    meaning: `Round up: the last ${rr} ${what} still need a trip.`, steps: `${remText(n, per)}; the last ${rr} ${what} need one more trip, so ${q + 1}` }; });
add(['remainders'], 4, 4, (r, g, A) => { const per = r.pick([4, 5, 6, 8, 10, 12]), [it, box, many, verb] = r.pick([['cookies', 'box', 'boxes', 'bakes'], ['eggs', 'carton', 'cartons', 'collects'], ['pencils', 'pack', 'packs', 'has'], ['muffins', 'tray', 'trays', 'bakes']]), n = rem(r, 40, 150, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `${A} ${verb} ${n} ${it} and packs them ${per} to a ${box}. How many ${many} can ${A} fill all the way?`, ans: q, ansText: `${q} full ${many}`, unit: `full ${many}`, f: 'floor(n/per)', vals: { n, per },
    meaning: `Drop it: the ${rr} left over do not fill a ${box}.`, steps: `${remText(n, per)}; only ${q} ${many} are full, the ${rr} left over do not fill one` }; });
add(['remainders'], 4, 4, (r, g) => { const per = r.int(3, 9), [team, who] = r.pick([['team', 'players'], ['relay team', 'runners'], ['reading group', 'students'], ['band', 'musicians']]), n = rem(r, 20, 70, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `${n} ${who} sign up. Each ${team} needs exactly ${per} ${who}. How many full ${team}s can be made?`, ans: q, ansText: `${q} full ${team}s`, unit: `full ${team}s`, f: 'floor(n/per)', vals: { n, per },
    meaning: `Drop it: the ${rr} left over are not enough for another ${team}.`, steps: `${remText(n, per)}; ${q} full ${team}s, and ${rr} ${who} are not enough for another` }; });
add(['remainders'], 4, 4, (r, g, A) => { const per = r.int(3, 9), [thing, u] = r.pick([['ribbon', 'inches'], ['rope', 'feet'], ['string', 'centimeters'], ['board', 'inches']]), n = rem(r, 30, 99, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `${A} has ${n} ${u} of ${thing} and cuts it into pieces that are each ${per} ${u} long. How many whole pieces does ${A} get?`, ans: q, ansText: `${q} whole pieces`, unit: 'whole pieces', f: 'floor(n/per)', vals: { n, per },
    meaning: `Drop it: the ${rr} ${u} left over are too short for a piece.`, steps: `${remText(n, per)}; ${q} whole pieces, with ${rr} ${u} too short for another` }; });
add(['remainders'], 4, 4, (r, g, A) => { const per = r.int(3, 9), [it, one] = r.pick([['tickets', 'ticket'], ['comic books', 'comic book'], ['snacks', 'snack'], ['sticker packs', 'sticker pack']]), n = rem(r, 20, 80, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `${A} has $${n}. Each ${one} costs $${per}. How many ${it} can ${A} buy?`, ans: q, ansText: `${q} ${it}`, unit: it, f: 'floor(n/per)', vals: { n, per },
    meaning: `Drop it: the $${rr} left over is not enough for another ${one}.`, steps: `${remText(n, per)}; ${q} ${it}, and $${rr} is not enough for one more` }; });
add(['remainders'], 4, 4, (r, g, A) => { const per = r.int(3, 9), it = r.pick(THINGS), n = rem(r, 30, 99, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `${A} shares ${n} ${it[1]} equally among ${per} friends. How many ${it[1]} are left over?`, ans: rr, ansText: `${rr} ${plural(rr, it)} left over`, unit: it[1], f: 'n-floor(n/per)*per', vals: { n, per },
    meaning: `Report it: each friend gets ${q}, and the remainder is the answer.`, steps: `${remText(n, per)}; each friend gets ${q} and ${rr} ${rr === 1 ? 'is' : 'are'} left over` }; });
add(['remainders'], 4, 4, (r, g, A) => { const per = r.int(4, 9) * 2, n = rem(r, 40, 150, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `A book has ${n} pages. ${A} reads ${per} pages every day until the book is done. How many pages does ${A} read on the last day?`, ans: rr, ansText: `${rr} pages on the last day`, unit: 'pages', f: 'n-floor(n/per)*per', vals: { n, per },
    meaning: `Report it: after ${q} full days, the ${rr} pages left are the last day.`, steps: `${remText(n, per)}; ${q} full days of ${per} pages, then ${rr} pages on the last day` }; });
add(['remainders'], 4, 4, (r, g) => { const per = r.pick([6, 8, 10, 12]), [it, box, many] = r.pick([['eggs', 'carton', 'cartons'], ['juice boxes', 'pack', 'packs'], ['crayons', 'box', 'boxes'], ['bottles', 'crate', 'crates']]), n = rem(r, 40, 150, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `A store gets ${n} ${it} and puts them in ${many} of ${per}. How many ${it} do not fit in a full ${box}?`, ans: rr, ansText: `${rr} ${it} left out`, unit: it, f: 'n-floor(n/per)*per', vals: { n, per },
    meaning: `Report it: ${q} ${many} are full, and the remainder is what is left out.`, steps: `${remText(n, per)}; ${q} full ${many}, and ${rr} ${it} are left out` }; });
add(['remainders'], 4, 4, (r, g, A) => { const n = rem(r, 15, 90, 7);
  if (!n) return null; const q = Math.floor(n / 7), rr = n % 7;
  return { text: `${A}'s trip is ${n} days long. How many whole weeks is that, and how many extra days?`, ans: q, ansText: `${q} weeks and ${rr} ${rr === 1 ? 'day' : 'days'}`, unit: 'weeks', f: 'floor(n/7)', vals: { n }, show: [String(n)],
    meaning: `Report it: the remainder is the ${rr} extra ${rr === 1 ? 'day' : 'days'}.`, steps: `${remText(n, 7)}; ${q} weeks and ${rr} extra ${rr === 1 ? 'day' : 'days'}` }; });
add(['remainders'], 4, 4, (r, g) => { const per = r.int(3, 9), [who, row] = r.pick([['students', 'row'], ['singers', 'row'], ['plants', 'row'], ['cars', 'row']]), n = rem(r, 25, 90, per);
  if (!n) return null; const q = Math.floor(n / per), rr = n % per;
  return { text: `${n} ${who} line up in ${row}s of ${per}. How many ${row}s are there if the last ${row} can be short?`, ans: q + 1, ansText: `${q + 1} ${row}s`, unit: `${row}s`, f: 'ceil(n/per)', vals: { n, per },
    meaning: `Round up: the ${rr} left over make a short last ${row}.`, steps: `${remText(n, per)}; ${q} full ${row}s plus a short ${row} of ${rr}, so ${q + 1}` }; });

// multi-step
add(['multi'], 3, 6, (r, g, A) => { const packs = r.int(2, 6), per = r.int(4, 10), give = r.int(2, packs * per - 2), it = r.pick(THINGS);
  return { text: `${A} buys ${packs} packs of ${it[1]}. Each pack has ${per} ${it[1]}. ${A} gives ${give} ${it[1]} to friends. How many ${it[1]} does ${A} have left?`, ans: packs * per - give, unit: it[1], f: 'packs*per-give', vals: { packs, per, give },
    steps: `${packs} × ${per} = ${packs * per}; ${packs * per} − ${give} = ${packs * per - give}` }; });
add(['multi'], 3, 6, (r, g, A) => { const days = r.int(3, 6), per = r.int(5, g === '3' ? 12 : 30), extra = r.int(5, 40);
  return { text: `${A} reads ${per} pages a day for ${days} days. On Saturday, ${A} reads ${extra} more pages. How many pages does ${A} read in all?`, ans: days * per + extra, unit: 'pages', f: 'days*per+extra', vals: { days, per, extra },
    steps: `${days} × ${per} = ${days * per}; ${days * per} + ${extra} = ${days * per + extra}` }; });
add(['multi'], 4, 6, (r, g) => { const ad = r.int(1, 4), kid = r.int(1, 5), pa = r.int(6, 15) * 100 + (g === '4' ? 0 : r.pick([0, 50])), pk = r.int(3, 9) * 100 + (g === '4' ? 0 : r.pick([0, 25, 50, 75])), fam = r.pick(['The Garcia family', 'The Nguyen family', 'The Okafor family', 'The Patel family', 'The Begay family', 'The Kim family']);
  return { text: `Zoo tickets cost ${money2(pa)} for an adult and ${money2(pk)} for a child. ${fam} buys ${ad} adult ${ad === 1 ? 'ticket' : 'tickets'} and ${kid} child ${kid === 1 ? 'ticket' : 'tickets'}. What is the total cost?`,
    ans: ad * pa + kid * pk, type: 'money', f: 'ad*pa+kid*pk', vals: { ad, pa, kid, pk }, steps: `${ad} × ${money2(pa)} + ${kid} × ${money2(pk)} = ${money2(ad * pa)} + ${money2(kid * pk)} = ${money2(ad * pa + kid * pk)}` }; });
add(['multi'], 4, 6, (r, g, A, B) => { const a = r.int(20, 90), more = r.int(5, 30), team = r.int(3, 6); if ((2 * a + more) % team) return null;
  return { text: `${A} collected ${a} cans for recycling. ${B} collected ${more} more cans than ${A}. They put all their cans into ${team} bins, with the same number in each bin. How many cans go in each bin?`, ans: (a + a + more) / team, unit: 'cans', f: '(a+a+more)/team', vals: { a, more, team },
    steps: `${B}: ${a} + ${more} = ${a + more}; together ${a} + ${a + more} = ${2 * a + more}; ${2 * a + more} ÷ ${team} = ${(2 * a + more) / team}` }; });
add(['multi'], 5, 6, (r, g, A) => { const laps = r.int(3, 8), lapM = r.pick([200, 250, 400]), days = r.int(2, 5);
  return { text: `${A} runs ${laps} laps around a ${lapM}-meter track each day for ${days} days. How many kilometers does ${A} run in all?`, ans: laps * lapM * days / 1000, unit: 'kilometers', f: 'laps*lapM*days/1000', vals: { laps, lapM, days },
    steps: `${laps} × ${lapM} × ${days} = ${fmt(laps * lapM * days, 0)} meters = ${big(laps * lapM * days / 1000)} km` }; });

// fractions of amounts
add(['frac'], 5, 6, (r, g) => { const d = r.pick([2, 3, 4, 5, 6, 8]), n = r.int(1, d - 1), k = r.int(2, 8), total = d * k, grp = r.pick([['students in a class', 'ride the bus', 'students'], ['books on a shelf', 'are mysteries', 'books'], ['marbles in a jar', 'are blue', 'marbles'], ['players on a team', 'are left-handed', 'players']]);
  if (Gen.m.gcd(n, d) !== 1) return null;
  return { text: `There are ${total} ${grp[0]}. ${n}/${d} of them ${grp[1]}. How many ${grp[2]} is that?`, ans: n * k, unit: grp[2], f: 'n*total/d', vals: { n, d, total }, steps: `${total} ÷ ${d} = ${k}; ${k} × ${n} = ${n * k}` }; });
add(['frac'], 5, 6, (r, g, A) => { const d = r.pick([2, 3, 4]), n = r.int(1, d - 1), batches = r.int(2, 9), it = r.pick(['oats', 'flour', 'milk', 'sugar']); if (Gen.m.gcd(n, d) !== 1) return null;
  return { text: `A recipe uses ${n}/${d} cup of ${it}. ${A} makes ${batches} batches. How many cups of ${it} does ${A} need?`, ans: n * batches / d, ansText: `${mixedText(n * batches, d)} ${n * batches <= d ? 'cup' : 'cups'}`, unit: 'cups', f: 'n*batches/d', vals: { n, d, batches },
    steps: `${batches} × ${n}/${d} = ${n * batches}/${d} = ${mixedText(n * batches, d)}` }; });
add(['frac'], 5, 6, (r, g, A) => { const d = r.pick([2, 3, 4, 5]), n = r.int(1, d - 1), k = r.int(2, 6), len = d * k; if (Gen.m.gcd(n, d) !== 1) return null;
  return { text: `${A} has a ${len}-foot roll of paper and uses ${n}/${d} of it for a banner. How many feet of paper are left?`, ans: len - n * k, unit: 'feet', f: 'len-len*n/d', vals: { len, n, d },
    steps: `${n}/${d} of ${len} = ${n * k}; ${len} − ${n * k} = ${len - n * k}` }; });
add(['frac'], 6, 6, (r, g, A) => { const d = r.pick([2, 3, 4]), n = r.int(1, d - 1), k = r.int(3, 12), total = n * k; if (Gen.m.gcd(n, d) !== 1 || total % d) return null;
  return { text: `${A} has ${total / d} cups of trail mix. Each serving is ${n}/${d} cup. How many servings can ${A} make?`, ans: k, unit: 'servings', f: '(total/d)/(n/d)', vals: { total, n, d }, show: [String(total / d), `${n}/${d}`],
    steps: `${total / d} ÷ ${n}/${d} = ${total / d} × ${d}/${n} = ${k}` }; });

// rates and percents, grade 6
add(['rates'], 6, 6, (r, g, A) => { const n = r.int(3, 12), each = r.int(15, 250); const tot = n * each;
  return { text: `${n} ${r.pick(['granola bars', 'pens', 'bottles of water', 'bus tickets'])} cost ${money2(tot)}. What is the cost of one?`, ans: each, type: 'money', f: 'tot/n', vals: { tot, n }, steps: `${money2(tot)} ÷ ${n} = ${money2(each)}` }; });
add(['rates'], 6, 6, (r, g, A) => { const h = r.int(2, 6), mph = r.int(8, 65), what = mph > 25 ? 'drives' : 'bikes';
  return { text: `${A}'s family ${what} ${h * mph} miles in ${h} hours at a steady speed. How many miles do they go in one hour?`.replace(`${A}'s family bikes`, `${A} bikes`).replace('do they go', what === 'bikes' ? `does ${A} go` : 'do they go'),
    ans: mph, unit: 'miles per hour', f: 'miles/h', vals: { miles: h * mph, h }, steps: `${h * mph} ÷ ${h} = ${mph} miles per hour` }; });
add(['rates'], 6, 6, (r, g, A) => { const per = r.int(2, 4), mins = r.int(2, 5), k = r.int(2, 6);   // 20 to 40 words a minute
  if (per * 10 * k > 1000) return null;
  return { text: `${A} can type ${per * 10 * mins} words in ${mins} minutes. At that rate, how many words can ${A} type in ${mins * k} minutes?`, ans: per * 10 * mins * k, unit: 'words', f: 'w*(t2/t1)', vals: { w: per * 10 * mins, t1: mins, t2: mins * k },
    steps: `${mins * k} is ${k} times ${mins}, so ${per * 10 * mins} × ${k} = ${per * 10 * mins * k}` }; });
add(['rates'], 6, 6, (r, g) => { const pct = r.pick([10, 20, 25, 30, 40, 50, 60, 75]), total = r.int(2, 12) * (pct % 25 === 0 ? 4 : 10), grp = r.pick([['students voted in the class election', 'voted for the field trip', 'students'], ['seeds were planted', 'sprouted', 'seeds'], ['games were played this season', 'were wins', 'games']]);
  return { text: `${total} ${grp[0]}. ${pct}% of them ${grp[1]}. How many ${grp[2]} is that?`, ans: pct * total / 100, unit: grp[2], f: 'pct*total/100', vals: { pct, total }, steps: `${pct}% of ${total} = ${pct / 100} × ${total} = ${pct * total / 100}` }; });
add(['rates'], 6, 6, (r, g, A) => { const price = r.int(4, 20) * 500, pct = r.pick([10, 20, 25, 30, 40, 50]), it = r.pick(['jacket', 'pair of shoes', 'skateboard', 'backpack', 'board game']);
  const off = price * pct / 100;
  return { text: `A ${it} costs ${money2(price)}. It is on sale for ${pct}% off. What is the sale price?`, ans: price - off, type: 'money', f: 'price-price*pct/100', vals: { price, pct },
    steps: `${pct}% of ${money2(price)} = ${money2(off)}; ${money2(price)} − ${money2(off)} = ${money2(price - off)}` }; });

/* ---------- reading answers back (used by verify) ---------- */
function readAnswer(t) {
  t = String(t).trim();
  let m = t.match(/^\$([\d,]+(?:\.\d\d)?)$/); if (m) return Math.round(parseFloat(m[1].replace(/,/g, '')) * 100);
  m = t.match(/^(\d+)¢$/); if (m) return +m[1];
  m = t.match(/^(\d+):(\d\d)(?: ([ap])\.m\.)?$/); if (m) { let h = +m[1] % 12; if (m[3] === 'p') h += 12; return h * 60 + +m[2]; }
  m = t.match(/^(?:(\d+) hours?)? ?(?:(\d+) minutes?)?$/); if (m && (m[1] || m[2])) return (+m[1] || 0) * 60 + (+m[2] || 0);
  m = t.match(/^(\d+) (\d+)\/(\d+) /); if (m) return +m[1] + m[2] / m[3];
  m = t.match(/^(\d+)\/(\d+) /); if (m) return m[1] / m[2];
  m = t.match(/^([\d,]+(?:\.\d+)?) /); if (m) return parseFloat(m[1].replace(/,/g, ''));
  return NaN;
}
// a small arithmetic reader for the formulas: + - * / ( ), ceil( ), floor( ), names from vals
function calc(f, vals) {
  const toks = f.match(/\d+(?:\.\d+)?|[a-zA-Z]\w*|[-+*/()]/g); let i = 0;
  const expr = () => { let a = term(); while (toks[i] === '+' || toks[i] === '-') { const o = toks[i++], b = term(); a = o === '+' ? a + b : a - b; } return a; };
  const term = () => { let a = atom(); while (toks[i] === '*' || toks[i] === '/') { const o = toks[i++], b = atom(); a = o === '*' ? a * b : a / b; } return a; };
  const atom = () => { const t = toks[i++];
    if (t === '(') { const a = expr(); i++; return a; }
    if (t === 'ceil' || t === 'floor') { i++; const a = expr(); i++; return Math[t](a + (t === 'ceil' ? -1e-9 : 1e-9)); }
    if (/^\d/.test(t)) return +t;
    if (t in vals) return vals[t];
    throw new Error('unknown ' + t); };
  return expr();
}

function answerText(p, g) {
  if (p.ansText) return p.ansText;
  if (p.type === 'money') return money(p.ans, g);
  if (p.type === 'cents') return `${p.ans}¢`;
  if (p.type === 'clock') return clock(p.ans);
  if (p.type === 'clock12') return clock(p.ans, false);
  if (p.type === 'dur') return dur(p.ans);
  return `${big(p.ans)} ${p.unit}`;
}

Gen.add('word-problems', {
  title: 'Word Problems', type: 'Apply',
  css: `.wp-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px 20px;margin:6px 0 10px}
.wp-card{border:1.5px solid #333;border-radius:8px;padding:8px 10px;display:flex;flex-direction:column;break-inside:avoid}
.wp-card > p{margin:0 0 6px;line-height:1.45}
.wp-card .ws-draw{margin:0 0 6px;flex:1;min-height:.95in}
.wp-ans{margin:0;text-align:right}
.wp-g1 .wp-card > p, .wp-g2 .wp-card > p{font-size:16.5px;line-height:1.4}
.wp-card .ws-draw{min-height:.8in}
.wp-steps{margin:4px 0;padding-left:1.8em;font-size:14px}
.wp-steps li{margin-bottom:5px}
.wp-why{text-align:left;margin-top:6px}
.wp-why .ws-blank{display:block;width:100%;min-width:0!important;text-align:left;margin:4px 0 0}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '3' },
    { id: 'topic', label: 'Topic', type: 'select', def: 'mix', options: v => [['mix', 'A mix of topics']].concat(BYGRADE[v.grade].map(t => [t, TOPICS[t]])) },
    { id: 'count', label: 'Problems', type: 'select', options: [['4', '4'], ['6', '6'], ['8', '8']], def: '6' },
  ],
  make(v, r) {
    const g = v.grade, n = +v.count, topics = v.topic === 'mix' ? BYGRADE[g] : [v.topic];
    const pool = T.filter(t => t.lo <= +g && +g <= t.hi && t.topics.some(x => topics.includes(x)));
    const used = new Set();
    // spread the topics and templates: take the least-used template of a random topic each time
    const counts = new Map();
    const mk = () => {
      const topic = r.pick(topics), cands = pool.filter(t => t.topics.includes(topic));
      if (!cands.length) return null;
      const least = Math.min(...cands.map(t => counts.get(t) || 0)), tpl = r.pick(cands.filter(t => (counts.get(t) || 0) === least));
      const [A, B] = r.sample(NAMES.filter(x => !used.has(x)), 2);
      const p = tpl.make(r, g, A, B);
      if (!p || (!p.type && p.ans === 1)) return null;
      // tidy the English: one period after a.m./p.m., and "an" before a vowel sound
      p.text = p.text.replace(/m\.\./g, 'm.').replace(/\ba (?=[aeiou]|8\b|8-|11\b|11-|18\b|18-)/gi, m0 => m0[0] === 'A' ? 'An ' : 'an ');
      p.steps = p.steps.replace(/m\.\./g, 'm.');
      p.type = p.type || 'num'; p.topic = topic; p.tpl = T.indexOf(tpl);
      return p;
    };
    const ps = r.distinct(n + 1, () => { const p = mk(); if (p) { counts.set(T[p.tpl], (counts.get(T[p.tpl]) || 0) + 1); for (const nm of NAMES) if (p.text.includes(nm)) used.add(nm); } return p; }, p => p.text);
    const ex = ps.shift();
    const preUnit = +g <= 2;
    const items = [], cards = [];
    ps.forEach((p, i) => {
      const a = answerText(p, g);
      items.push({ q: p.text, a, f: p.f, vals: p.vals, type: p.type, show: p.show, whole: p.type === 'num' && !p.ansText && p.unit !== 'kilometers', unit: p.unit });
      let ansLine;
      if (preUnit && p.type === 'num') ansLine = `Answer: ${H.blank(big(p.ans), 3)} ${esc(p.unit)}`;
      else if (preUnit && p.type === 'cents') ansLine = `Answer: ${H.blank(String(p.ans), 3)} ¢`;
      else ansLine = `Answer: ${H.blank(a, Math.max(7, a.length * .6 + 1.5))}`;
      if (p.meaning) ansLine += `</p><p class="wp-ans wp-why">What does the remainder mean? ${H.blank(p.meaning, 10)}`;
      cards.push(`<div class="wp-card"><p><span class="ws-num">${i + 1}.</span> ${esc(p.text)}</p>${H.work(+g <= 2 ? 0.8 : 0.95, +g <= 2 ? 'Draw or write to show your thinking' : 'Show your work')}<p class="wp-ans">${ansLine}</p></div>`);
    });
    const exAns = answerText(ex, g);
    const parts = [part('', example(esc(ex.text), `${esc(ex.steps)}. <b>Answer: ${esc(exAns)}</b>` + (ex.meaning ? ` ${esc(ex.meaning)}` : ''))), part('Practice', `<div class="wp-grid wp-g${g}">${cards.join('')}</div>`)];
    const teacher = `<h3>Solutions</h3><ol class="wp-steps">${ps.map((p, i) => `<li>${esc(p.steps)}. Answer: <b>${esc(items[i].a)}</b>${p.meaning ? ` ${esc(p.meaning)}` : ''}</li>`).join('')}</ol>`;
    const tl = v.topic === 'mix' ? 'Word Problems' : TOPICS[v.topic];
    return {
      title: `${tl}: ${GRADES.find(x => x[0] === g)[1]}`, level: GRADES.find(x => x[0] === g)[1] + (v.topic === 'mix' ? ', mixed topics' : ''),
      ican: +g <= 2 ? 'I can read a story, find the numbers and solve it.' : 'I can read a story problem, plan my steps and answer with the right unit.',
      directions: preUnit ? 'Read each story. Draw or write to show your thinking. Write the number on the answer line.'
        : 'Read each story. Show your work in the box. Write the answer with its unit, like 12 cm or $3.50.' + (topics.includes('remainders') ? ' Then tell what the remainder means: round up, drop it, or report it.' : ''),
      minutes: n > 6 ? 35 : 25, materials: 'pencil' + (+g <= 2 ? ', counters if you like' : ''),
      parts, items, teacher,
      mistakes: +g <= 2 ? 'Adding every time two numbers show up. Ask: is the amount getting bigger or smaller? In "how many more" stories, students often add.'
        : 'Answering a different question than the one asked (the total instead of the change), and leaving off units. ' + (topics.includes('remainders') ? 'Writing the quotient with R and stopping: the story decides whether to round up, drop the remainder, or report it. ' : '') + (topics.includes('groups') ? 'With remainders, read whether the story needs to round up (vans) or down (full boxes). ' : '') + (topics.includes('time') ? 'With time, counting by 100 instead of 60 across the hour. ' : ''),
      notes: 'Every story is built from its numbers and checked: no fractional people, no change bigger than the money paid, and every answer has a unit. Names and settings change with each sheet. Read the first story aloud together for younger readers.',
    };
  },
  verify(s) {
    const out = [];
    const fmtv = x => fmt(x, 2);
    for (const it of s.items) {
      let want;
      try { want = calc(it.f, it.vals); } catch (e) { out.push(`${it.q.slice(0, 50)}: ${e.message}`); continue; }
      const got = readAnswer(it.a);
      const isClock = it.type === 'clock' || it.type === 'clock12';
      const same = isClock ? ((got - want) % (it.type === 'clock12' ? 720 : 1440) + 1440) % (it.type === 'clock12' ? 720 : 1440) === 0 : Math.abs(got - want) < 1e-6;
      if (!same) out.push(`${it.q.slice(0, 60)}: key says ${it.a}, works out to ${want}`);
      if (!isClock && !(want > 0)) out.push(`${it.q.slice(0, 60)}: answer ${want} is not positive`);
      if (it.whole && !Number.isInteger(want)) out.push(`${it.q.slice(0, 60)}: ${want} ${it.unit} is not a whole number`);
      if (!/[a-z¢$:]/i.test(it.a)) out.push(`${it.q.slice(0, 60)}: answer ${it.a} has no unit`);
      // the story must show the numbers the formula uses
      const shows = it.show || Object.values(it.vals).filter(x => x !== 0).map(x => it.type === 'money' ? null : fmtv(x)).filter(Boolean);
      for (const sh of shows) if (!it.q.includes(sh)) { out.push(`${it.q.slice(0, 60)}: story does not show ${sh}`); break; }
      if (it.type === 'money' && /pays with/.test(it.q)) { const paid = it.vals.paid; if (paid != null && want > paid * (paid < 100 ? 100 : 1)) out.push(`${it.q.slice(0, 60)}: change bigger than paid`); }
    }
    return out;
  },
});
})();
