// Reading Graphs generator, grades 1-8.
// Makes a small realistic dataset and draws it as a picture graph (grades 1-3; at grade 3 one picture stands for 2),
// a bar graph (grades 1-5), a line graph (grades 4-8) or a data table with a dot plot (grades 6-8). Questions climb
// from reading one value to comparing, totals and differences, and at grades 6-8 the mean, median, range and a
// reasoning question. Every answer is worked from the data, and verify re-works it and checks the drawn scale.
(() => {
const { part, example, fill, blank, lines, keyline, esc } = Gen.h;
const { fmt, gcd } = Gen.m;

const GRADES = [['1', 'Grade 1'], ['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'], ['6', 'Grade 6'], ['7', 'Grade 7'], ['8', 'Grade 8']];
const TYPES = { picture: 'Picture graph', bar: 'Bar graph', line: 'Line graph', dot: 'Table and dot plot' };
const typesFor = g => +g <= 2 ? ['picture', 'bar'] : +g === 3 ? ['picture', 'bar'] : +g <= 5 ? ['bar', 'line'] : ['line', 'dot'];
const lc = s => s.toLowerCase();

/* ---------- datasets ---------- */
// category data (picture and bar graphs): the question wording lives with each set
const CATS = [
  { id: 'fruit', two: (a, b, c) => `How many more students chose ${lc(a)} or ${lc(b)} than chose ${lc(c)}?`, frac: c => `What fraction of the students chose ${lc(c)}?`, title: 'Favorite Fruit', cats: ['Apple', 'Banana', 'Grapes', 'Orange', 'Strawberry', 'Peach'], axis: 'Number of students', catAxis: 'Fruit', pic: 'student',
    read: c => `How many students chose ${lc(c)}?`, most: 'Which fruit did the most students choose?', least: 'Which fruit did the fewest students choose?',
    more: (a, b) => `How many more students chose ${lc(a)} than ${lc(b)}?`, both: (a, b) => `How many students chose ${lc(a)} or ${lc(b)}?`, total: 'How many students voted in all?', who: 'students', claim: (a, b) => `${a} got twice as many votes as ${b}` },
  { id: 'pet', two: (a, b, c) => `How many more students chose ${lc(a)} or ${lc(b)} than chose ${lc(c)}?`, frac: c => `What fraction of the students chose ${lc(c)}?`, title: 'Favorite Pet', cats: ['Dog', 'Cat', 'Fish', 'Bird', 'Rabbit', 'Hamster'], axis: 'Number of students', catAxis: 'Pet', pic: 'student',
    read: c => `How many students chose ${lc(c)}?`, most: 'Which pet did the most students choose?', least: 'Which pet did the fewest students choose?',
    more: (a, b) => `How many more students chose ${lc(a)} than ${lc(b)}?`, both: (a, b) => `How many students chose ${lc(a)} or ${lc(b)}?`, total: 'How many students voted in all?', who: 'students', claim: (a, b) => `${a} got twice as many votes as ${b}` },
  { id: 'season', two: (a, b, c) => `How many more students chose ${lc(a)} or ${lc(b)} than chose ${lc(c)}?`, frac: c => `What fraction of the students chose ${lc(c)}?`, title: 'Favorite Season', cats: ['Spring', 'Summer', 'Fall', 'Winter'], axis: 'Number of students', catAxis: 'Season', pic: 'student',
    read: c => `How many students chose ${lc(c)}?`, most: 'Which season did the most students choose?', least: 'Which season did the fewest students choose?',
    more: (a, b) => `How many more students chose ${lc(a)} than ${lc(b)}?`, both: (a, b) => `How many students chose ${lc(a)} or ${lc(b)}?`, total: 'How many students voted in all?', who: 'students', claim: (a, b) => `${a} got twice as many votes as ${b}` },
  { id: 'weather', cap: 20, two: (a, b, c) => `How many more days were ${lc(a)} or ${lc(b)} than were ${lc(c)}?`, frac: c => `What fraction of the days were ${lc(c)}?`, title: 'Weather Log', cats: ['Sunny', 'Cloudy', 'Rainy', 'Windy'], axis: 'Number of days', catAxis: 'Weather', pic: 'day',
    read: c => `How many days were ${lc(c)}?`, most: 'Which kind of weather happened on the most days?', least: 'Which kind of weather happened on the fewest days?',
    more: (a, b) => `How many more days were ${lc(a)} than ${lc(b)}?`, both: (a, b) => `How many days were ${lc(a)} or ${lc(b)}?`, total: 'How many days are shown in all?', who: 'days', claim: (a, b) => `there were twice as many ${lc(a)} days as ${lc(b)} days` },
  { id: 'books', cap: 20, two: (a, b, c) => `How many more books did ${a} and ${b} read together than ${c}?`, frac: c => `What fraction of all the books did ${c} read?`, title: 'Books Read This Month', cats: ['Maya', 'Leo', 'Ava', 'Sam', 'Kai', 'Zoe'], axis: 'Number of books', catAxis: 'Student', pic: 'book',
    read: c => `How many books did ${c} read?`, most: 'Who read the most books?', least: 'Who read the fewest books?',
    more: (a, b) => `How many more books did ${a} read than ${b}?`, both: (a, b) => `How many books did ${a} and ${b} read together?`, total: 'How many books did they read in all?', who: 'books', claim: (a, b) => `${a} read twice as many books as ${b}` },
  { id: 'goals', cap: 20, two: (a, b, c) => `How many more goals did the ${a} and the ${b} score together than the ${c}?`, frac: c => `What fraction of all the goals did the ${c} score?`, title: 'Goals Scored This Season', cats: ['Lions', 'Tigers', 'Bears', 'Hawks', 'Sharks', 'Wolves'], axis: 'Number of goals', catAxis: 'Team', pic: 'goal',
    read: c => `How many goals did the ${c} score?`, most: 'Which team scored the most goals?', least: 'Which team scored the fewest goals?',
    more: (a, b) => `How many more goals did the ${a} score than the ${b}?`, both: (a, b) => `How many goals did the ${a} and the ${b} score together?`, total: 'How many goals did all the teams score?', who: 'goals', claim: (a, b) => `the ${a} scored twice as many goals as the ${b}` },
  { id: 'lemon', two: (a, b, c) => `How many more cups were sold on ${a} and ${b} together than on ${c}?`, frac: c => `What fraction of all the cups were sold on ${c}?`, title: 'Lemonade Cups Sold', cats: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], axis: 'Cups sold', catAxis: 'Day', pic: 'cup', ordered: true, minGrade: 3,
    read: c => `How many cups were sold on ${c}?`, most: 'On which day were the most cups sold?', least: 'On which day were the fewest cups sold?',
    more: (a, b) => `How many more cups were sold on ${a} than on ${b}?`, both: (a, b) => `How many cups were sold on ${a} and ${b} together?`, total: 'How many cups were sold in all?', who: 'cups', claim: (a, b) => `twice as many cups were sold on ${a} as on ${b}` },
  { id: 'cans', two: (a, b, c) => `How many more cans did ${a} and ${b} collect together than ${c}?`, frac: c => `What fraction of all the cans did ${c} collect?`, title: 'Cans Collected for Recycling', cats: ['Room 101', 'Room 102', 'Room 103', 'Room 104', 'Room 105', 'Room 106'], axis: 'Number of cans', catAxis: 'Class', pic: 'can', minGrade: 4,
    read: c => `How many cans did ${c} collect?`, most: 'Which class collected the most cans?', least: 'Which class collected the fewest cans?',
    more: (a, b) => `How many more cans did ${a} collect than ${b}?`, both: (a, b) => `How many cans did ${a} and ${b} collect together?`, total: 'How many cans were collected in all?', who: 'cans', claim: (a, b) => `${a} collected twice as many cans as ${b}` },
];
// data over time (line graphs). make(r, n, unit) returns values as multiples of unit; mono = always going up;
// whole = counted things (points, cups), so no halfway values
const LINES = [
  { id: 'plant', title: 'Height of a Bean Plant', xs: ['1', '2', '3', '4', '5', '6', '7'], xAxis: 'Week', axis: 'Height (cm)', u: 'cm', mono: true, lo: 0, hi: 40,
    read: x => `How tall was the plant in week ${x}?`, change: (a, b) => `How much did the plant grow from week ${a} to week ${b}?`,
    biggest: 'Between which two weeks in a row did the plant grow the most?', xname: x => `week ${x}`, noun: 'the plant\'s height' },
  { id: 'temp', title: 'Temperature at Noon', xs: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], xAxis: 'Day', axis: 'Temperature (°F)', u: '°F', lo: 40, hi: 85, axis0: 0,
    read: x => `What was the temperature on ${DAY[x]}?`, change: (a, b) => `How many degrees warmer was it on ${DAY[b]} than on ${DAY[a]}?`, most: 'Which day was the warmest?', least: 'Which day was the coolest?',
    biggest: 'Between which two days in a row did the temperature change the most?', xname: x => DAY[x], noun: 'the temperature', warm: true },
  { id: 'points', title: 'Points Scored by the Team', xs: ['1', '2', '3', '4', '5', '6', '7', '8'], xAxis: 'Game', axis: 'Points', u: 'points', lo: 20, hi: 75, add: true, whole: true,
    read: x => `How many points did the team score in game ${x}?`, change: (a, b) => `How many more points did the team score in game ${b} than in game ${a}?`, most: 'In which game did the team score the most points?', least: 'In which game did the team score the fewest points?',
    biggest: 'Between which two games in a row did the score change the most?', xname: x => `game ${x}`, noun: 'the score', total: 'How many points did the team score in all the games?' },
  { id: 'savings', title: 'Money in a Savings Jar', xs: ['1', '2', '3', '4', '5', '6', '7', '8'], xAxis: 'Week', axis: 'Dollars', u: 'dollars', mono: true, lo: 5, hi: 100,
    read: x => `How many dollars were in the jar in week ${x}?`, change: (a, b) => `How many dollars were added from week ${a} to week ${b}?`,
    biggest: 'Between which two weeks in a row was the most money added?', xname: x => `week ${x}`, noun: 'the money in the jar' },
  { id: 'puppy', title: "A Puppy's Weight", xs: ['2', '3', '4', '5', '6', '7'], xAxis: 'Age (months)', axis: 'Weight (kg)', u: 'kg', mono: true, lo: 3, hi: 26,
    read: x => `How much did the puppy weigh at ${x} months?`, change: (a, b) => `How much weight did the puppy gain from ${a} months to ${b} months?`,
    biggest: 'Between which two months in a row did the puppy gain the most weight?', xname: x => `${x} months`, noun: 'the puppy\'s weight' },
  { id: 'cups', title: 'Lemonade Cups Sold', xs: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], xAxis: 'Day', axis: 'Cups sold', u: 'cups', lo: 10, hi: 70, add: true, whole: true,
    read: x => `How many cups were sold on ${DAY[x]}?`, change: (a, b) => `How many more cups were sold on ${DAY[b]} than on ${DAY[a]}?`, most: 'On which day were the most cups sold?', least: 'On which day were the fewest cups sold?',
    biggest: 'Between which two days in a row did sales change the most?', xname: x => DAY[x], noun: 'the cups sold', total: 'How many cups were sold in all?' },
];
const DAY = { Mon: 'Monday', Tue: 'Tuesday', Wed: 'Wednesday', Thu: 'Thursday', Fri: 'Friday', Sat: 'Saturday', Sun: 'Sunday' };
// survey data (dot plots): values from lo to hi in steps
const DOTS = [
  { id: 'pets', title: 'Number of Pets', axis: 'Number of pets', lo: 0, hi: 5, step: 1, who: 'students', u: 'pets', weights: [4, 6, 4, 2, 1, 1],
    at: v => `How many students have ${v} ${v === 1 ? 'pet' : 'pets'}?`, over: v => `How many students have more than ${v} ${v === 1 ? 'pet' : 'pets'}?`, unitWord: 'pets', unitOne: 'pet', newWho: 'A new student with', survey: 'Each dot is one student in a class survey.' },
  { id: 'sleep', title: 'Hours of Sleep Last Night', axis: 'Hours of sleep', lo: 6, hi: 11, step: 1, who: 'students', u: 'hours', weights: [1, 2, 4, 6, 4, 2],
    at: v => `How many students slept ${v} hours?`, over: v => `How many students slept more than ${v} hours?`, unitWord: 'hours', unitOne: 'hour', newWho: 'A new student who slept', survey: 'Each dot is one student in a class survey.' },
  { id: 'goals', title: 'Goals Scored per Game', axis: 'Goals', lo: 0, hi: 6, step: 1, who: 'games', u: 'goals', weights: [3, 5, 5, 3, 2, 1, 1],
    at: v => `In how many games did the team score ${v} ${v === 1 ? 'goal' : 'goals'}?`, over: v => `In how many games did the team score more than ${v} ${v === 1 ? 'goal' : 'goals'}?`, unitWord: 'goals', unitOne: 'goal', newWho: 'One more game with', survey: 'Each dot is one game in a soccer season.' },
  { id: 'books', title: 'Books Read Over the Summer', axis: 'Number of books', lo: 0, hi: 10, step: 1, who: 'students', u: 'books', weights: [1, 2, 3, 4, 4, 4, 3, 2, 2, 1, 1],
    at: v => `How many students read ${v} ${v === 1 ? 'book' : 'books'}?`, over: v => `How many students read more than ${v} ${v === 1 ? 'book' : 'books'}?`, unitWord: 'books', unitOne: 'book', newWho: 'A new student who read', survey: 'Each dot is one student in a class survey.' },
  { id: 'commute', title: 'Minutes to Get to School', axis: 'Minutes', lo: 5, hi: 35, step: 5, who: 'students', u: 'minutes', weights: [3, 5, 6, 4, 3, 1, 1],
    at: v => `How many students take ${v} minutes to get to school?`, over: v => `How many students take more than ${v} minutes?`, unitWord: 'minutes', newWho: 'A new student who takes', survey: 'Each dot is one student in a class survey.' },
];

/* ---------- scales ---------- */
// pick a gridline spacing so the axis has at most `most` gridlines; labels every `lab`
// unit: values are multiples of it, so a gridline spacing must divide it (grade 5 may also use twice it: halfway reads)
function scale(max, g, kind, unit) {
  const cands = [1, 2, 5, 10, 20, 25, 50].filter(m => !unit || unit % m === 0 || (+g === 5 && m === 2 * unit));
  const most = +g <= 2 ? 20 : 16;
  const minor = cands.find(m => Math.ceil(max / m) <= most) || cands[cands.length - 1];
  const top = Math.ceil(max / minor) * minor + (max % minor === 0 && kind !== 'pic' ? minor : 0);
  const lab = top / minor > 10 ? minor * 2 : minor;
  return { minor, top, lab };
}

/* ---------- drawing ---------- */
const T = (x, y, s, o = '') => `<text x="${x}" y="${y}" ${o}>${esc(s)}</text>`;
const FONT = 'font-family="Helvetica, Arial, sans-serif" fill="#222"';
function icon(kind, cx, cy) {
  const base = `stroke="#222" stroke-width="1.5" fill="#fff"`;
  if (kind === 'book') return `<rect x="${cx - 9}" y="${cy - 11}" width="18" height="22" rx="2" ${base}/><line x1="${cx - 5}" y1="${cy - 11}" x2="${cx - 5}" y2="${cy + 11}" stroke="#222" stroke-width="1.5"/>`;
  if (kind === 'goal') return `<circle cx="${cx}" cy="${cy}" r="11" ${base}/><path d="M${cx} ${cy - 5} l4.8 3.5 -1.8 5.6 h-6 l-1.8 -5.6z" fill="#222"/>`;
  if (kind === 'cup') return `<path d="M${cx - 8} ${cy - 10} h16 l-2.5 21 h-11z" ${base}/><line x1="${cx - 7}" y1="${cy - 4}" x2="${cx + 7}" y2="${cy - 4}" stroke="#222" stroke-width="1.2"/>`;
  if (kind === 'can') return `<rect x="${cx - 7}" y="${cy - 11}" width="14" height="22" rx="3" ${base}/><line x1="${cx - 7}" y1="${cy - 6}" x2="${cx + 7}" y2="${cy - 6}" stroke="#222"/>`;
  if (kind === 'day') return `<rect x="${cx - 10}" y="${cy - 10}" width="20" height="21" rx="2" ${base}/><rect x="${cx - 10}" y="${cy - 10}" width="20" height="6" fill="#222"/>`;
  return `<circle cx="${cx}" cy="${cy}" r="11" ${base}/><circle cx="${cx - 4}" cy="${cy - 3}" r="1.6" fill="#222"/><circle cx="${cx + 4}" cy="${cy - 3}" r="1.6" fill="#222"/><path d="M${cx - 5} ${cy + 3} q5 5 10 0" stroke="#222" stroke-width="1.5" fill="none"/>`;
}
const PICNAME = { student: ['student', 'students'], book: ['book', 'books'], goal: ['goal', 'goals'], cup: ['cup', 'cups'], can: ['can', 'cans'], day: ['day', 'days'] };

function drawPicture(ds, cats, vals, per) {
  const rowH = 36, labW = 130, W = 600, top = 40, H = top + cats.length * rowH + 52;
  let b = T(W / 2, 24, ds.title, `${FONT} font-size="18" font-weight="700" text-anchor="middle"`);
  cats.forEach((c, i) => {
    const y = top + i * rowH;
    b += `<rect x="10" y="${y}" width="${W - 20}" height="${rowH}" fill="none" stroke="#222" stroke-width="1"/>` + `<line x1="${labW}" y1="${y}" x2="${labW}" y2="${y + rowH}" stroke="#222"/>`;
    b += T(labW - 10, y + rowH / 2 + 5, c, `${FONT} font-size="15" text-anchor="end"`);
    for (let k = 0; k < vals[i] / per; k++) b += icon(ds.pic, labW + 22 + k * 30, y + rowH / 2);
  });
  const ky = top + cats.length * rowH + 30, nm = PICNAME[ds.pic];
  b += `<rect x="${W / 2 - 110}" y="${ky - 18}" width="220" height="36" rx="4" fill="none" stroke="#222" stroke-width="1.5"/>` + T(W / 2 - 96, ky + 5, 'Key:', `${FONT} font-size="14" font-weight="700"`) + icon(ds.pic, W / 2 - 46, ky) +
    T(W / 2 - 28, ky + 5, `= ${per} ${per === 1 ? nm[0] : nm[1]}`, `${FONT} font-size="14"`);
  return Gen.h.svg(W, H, b, `Picture graph: ${ds.title}. ` + cats.map((c, i) => `${c}, ${vals[i] / per} pictures`).join('; ') + `. Each picture stands for ${per}.`);
}
function axes(W, H, L, R, Tp, B, sc, title, yLab, xLab) {
  const ph = H - Tp - B, y = v => Tp + ph - (v / sc.top) * ph;
  let b = T(W / 2, 22, title, `${FONT} font-size="18" font-weight="700" text-anchor="middle"`);
  for (let v = 0; v <= sc.top + 1e-9; v += sc.minor) {
    const major = Math.abs(v / sc.lab - Math.round(v / sc.lab)) < 1e-9;
    b += `<line x1="${L}" y1="${y(v)}" x2="${W - R}" y2="${y(v)}" stroke="${major ? '#999' : '#ccc'}" stroke-width="1"/>`;
    if (major) b += T(L - 8, y(v) + 5, fmt(v, 2), `${FONT} font-size="13" text-anchor="end"`);
  }
  b += `<line x1="${L}" y1="${Tp}" x2="${L}" y2="${Tp + ph}" stroke="#222" stroke-width="2"/><line x1="${L}" y1="${Tp + ph}" x2="${W - R}" y2="${Tp + ph}" stroke="#222" stroke-width="2"/>`;
  b += T(16, Tp + ph / 2, yLab, `${FONT} font-size="14" font-weight="600" text-anchor="middle" transform="rotate(-90 16 ${Tp + ph / 2})"`);
  b += T((L + W - R) / 2, H - 8, xLab, `${FONT} font-size="14" font-weight="600" text-anchor="middle"`);
  return { b, y, ph };
}
function drawBar(ds, cats, vals, sc) {
  const W = 600, H = 330, L = 64, R = 16, Tp = 38, B = 56;
  const ax = axes(W, H, L, R, Tp, B, sc, ds.title, ds.axis, ds.catAxis);
  const slot = (W - L - R) / cats.length, bw = Math.min(64, slot * 0.6);
  let b = ax.b;
  cats.forEach((c, i) => {
    const x = L + slot * i + (slot - bw) / 2;
    b += `<rect x="${x}" y="${ax.y(vals[i])}" width="${bw}" height="${ax.y(0) - ax.y(vals[i])}" fill="#d4d4d4" stroke="#222" stroke-width="1.5"/>`;
    b += T(x + bw / 2, H - B + 20, c, `${FONT} font-size="${c.length > 8 ? 12 : 14}" text-anchor="middle"`);
  });
  return Gen.h.svg(W, H, b, `Bar graph: ${ds.title}. The scale goes up by ${sc.minor}. ` + cats.map((c, i) => `${c}: ${vals[i]}`).join('; ') + '.');
}
function drawLine(ds, xs, vals, sc) {
  const W = 600, H = 330, L = 64, R = 20, Tp = 38, B = 56;
  const ax = axes(W, H, L, R, Tp, B, sc, ds.title, ds.axis, ds.xAxis);
  const slot = (W - L - R) / xs.length, X = i => L + slot * (i + 0.5);
  let b = ax.b;
  xs.forEach((x, i) => { b += `<line x1="${X(i)}" y1="${ax.y(0)}" x2="${X(i)}" y2="${ax.y(0) + 5}" stroke="#222" stroke-width="1.5"/>` + T(X(i), H - B + 20, x, `${FONT} font-size="14" text-anchor="middle"`); });
  b += `<polyline points="${vals.map((v, i) => `${X(i)},${ax.y(v)}`).join(' ')}" fill="none" stroke="#222" stroke-width="2.2"/>`;
  b += vals.map((v, i) => `<circle cx="${X(i)}" cy="${ax.y(v)}" r="4.5" fill="#222"/>`).join('');
  return Gen.h.svg(W, H, b, `Line graph: ${ds.title}. The scale goes up by ${sc.minor}. ` + xs.map((x, i) => `${ds.xAxis} ${x}: ${vals[i]}`).join('; ') + '.');
}
function drawDots(ds, data) {
  const vals = []; for (let v = ds.lo; v <= ds.hi; v += ds.step) vals.push(v);
  const counts = vals.map(v => data.filter(x => x === v).length), tall = Math.max(...counts);
  const W = 600, L = 40, R = 40, gap = 20, base = 46 + tall * gap + 10, H = base + 56;
  const X = i => L + (W - L - R) * (i / (vals.length - 1));
  let b = T(W / 2, 22, ds.title, `${FONT} font-size="18" font-weight="700" text-anchor="middle"`);
  b += `<line x1="${L - 20}" y1="${base}" x2="${W - R + 20}" y2="${base}" stroke="#222" stroke-width="2"/>`;
  vals.forEach((v, i) => {
    b += `<line x1="${X(i)}" y1="${base - 6}" x2="${X(i)}" y2="${base + 6}" stroke="#222" stroke-width="1.5"/>` + T(X(i), base + 24, String(v), `${FONT} font-size="14" text-anchor="middle"`);
    for (let k = 0; k < counts[i]; k++) b += `<circle cx="${X(i)}" cy="${base - 16 - k * gap}" r="7" fill="#222"/>`;
  });
  b += T(W / 2, H - 8, ds.axis, `${FONT} font-size="14" font-weight="600" text-anchor="middle"`);
  return Gen.h.svg(W, H, b, `Dot plot: ${ds.title}. ` + vals.map((v, i) => `${v}: ${counts[i]} dots`).join('; ') + '.');
}

/* ---------- making data ---------- */
// categorical values: distinct is not needed, but the biggest and smallest must be unique
function catData(r, g, n, cap) {
  const cfg = { 1: [1, 10, 1], 2: [2, 18, 1], 4: [10, 80, 5], 5: [15, 150, 5] }[g] || (cap || r.chance(.5) ? [2, 20, 2] : [5, 50, 5]);
  const [lo, hi, unit] = cfg;
  for (let t = 0; t < 200; t++) {
    const vals = Array.from({ length: n }, () => r.int(lo / unit, hi / unit) * unit);
    const mx = Math.max(...vals), mn = Math.min(...vals);
    if (vals.filter(v => v === mx).length > 1 || vals.filter(v => v === mn).length > 1 || new Set(vals).size < n - 1) continue;
    return { vals, unit };
  }
  return null;
}
function lineData(r, ds, g) {
  const n = Math.min(ds.xs.length, +g <= 5 ? 6 : 7);
  const sc0 = scale(ds.hi, g, 'line');
  const unit = +g === 4 ? sc0.minor : sc0.minor / 2;
  const q = v => Math.round(v / unit) * unit;
  for (let t = 0; t < 1500; t++) {
    let vals;
    if (ds.mono) { let v = q(r.int(ds.lo, ds.lo + (ds.hi - ds.lo) / 4)); vals = [v]; for (let i = 1; i < n; i++) { v += unit * r.int(1, Math.max(1, Math.floor((ds.hi - ds.lo) / n / unit * 1.6))); vals.push(v); } }
    else { let v = q(r.int(ds.lo + 5, ds.hi - 10)); vals = [v]; for (let i = 1; i < n; i++) { v = q(Math.min(ds.hi, Math.max(ds.lo, v + r.int(-15, 15)))); vals.push(v); } }
    if (Math.max(...vals) > ds.hi || Math.min(...vals) < 0) continue;
    if (vals.some(v => Math.abs(v / unit - Math.round(v / unit)) > 1e-9)) continue;
    if (ds.whole && vals.some(v => !Number.isInteger(v))) continue;
    const mx = Math.max(...vals), mn = Math.min(...vals);
    if (vals.filter(v => v === mx).length > 1 || vals.filter(v => v === mn).length > 1) continue;
    const steps = vals.slice(1).map((v, i) => Math.abs(v - vals[i])), big = Math.max(...steps);
    if (steps.filter(s => s === big).length > 1 || steps.some(s => s === 0)) continue;
    return { xs: ds.xs.slice(0, n), vals, unit };
  }
  return null;
}
function dotData(r, ds, g) {
  const n = r.int(14, 20), vals = []; for (let v = ds.lo; v <= ds.hi; v += ds.step) vals.push(v);
  const tot = ds.weights.reduce((a, b) => a + b);
  for (let t = 0; t < 300; t++) {
    const data = Array.from({ length: n }, () => { let x = r.next() * tot; for (let i = 0; i < vals.length; i++) { x -= ds.weights[i]; if (x < 0) return vals[i]; } return vals[vals.length - 1]; });
    const counts = vals.map(v => data.filter(x => x === v).length), mx = Math.max(...counts);
    if (counts.filter(c => c === mx).length > 1) continue;                   // one mode
    if (+g === 6 && (data.reduce((a, b) => a + b) * 10) % n !== 0) continue;   // grade 6: the mean ends in tenths at most
    return data;
  }
  return null;
}

/* ---------- sheet ---------- */
const sum = a => a.reduce((x, y) => x + y, 0);
const median = a => { const s = a.slice().sort((x, y) => x - y), m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
const round1 = x => Math.round((x + Number.EPSILON) * 10) / 10;

Gen.add('graph-reading', {
  title: 'Reading Graphs', type: 'Data and graphs',
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '3' },
    { id: 'graph', label: 'Graph', type: 'select', def: 'bar', options: v => typesFor(v.grade).map(t => [t, TYPES[t]]) },
  ],
  css: `
.gr-q .ws-fill li { margin-bottom: 12px; break-inside: avoid; }
.gr-data { width: auto; min-width: 0; margin: 4px 0 6px; }
.gr-data td { height: auto; padding: 2px 9px; }
@media print { .gr-q .ws-fill li { margin-bottom: 8px; } }
`,
  make(v, r) {
    const g = v.grade, G = +g, type = v.graph;
    const items = [], qs = [];   // qs: [html, item] in order
    const add = (q, a, extra = {}, unit = '') => { const it = { q, a: String(a), ...extra }; items.push(it); qs.push(`${esc(q)} ${blank(it.a, Math.max(3, String(a).length * 0.7 + 1.5))}${unit ? ' ' + esc(unit) : ''}`); return it; };
    let graph = '', exHtml = '', data, reason = null;
    if (type === 'picture' || type === 'bar') {
      const pool = CATS.filter(c => (!c.minGrade || G >= c.minGrade) && (!c.cap || G <= 3));   // capped sets (days, one student's books, one team's goals) stay small
      const ds = r.pick(pool);
      const n = Math.min(ds.cats.length, G === 1 ? 3 : G <= 3 ? 4 : (r.chance(.5) ? 5 : 6));
      const cats = ds.ordered ? ds.cats.slice(0, n) : r.sample(ds.cats, n);
      const per = type === 'picture' && G === 3 ? 2 : 1;
      let dd = type === 'picture' ? null : catData(r, g, n, ds.cap);
      if (type === 'picture') {   // at most 10 pictures in a row
        for (let t = 0; t < 200 && !dd; t++) { const vals = Array.from({ length: n }, () => r.int(1, G === 1 ? 7 : 10) * per); const mx = Math.max(...vals), mn = Math.min(...vals);
          if (vals.filter(x => x === mx).length === 1 && vals.filter(x => x === mn).length === 1) dd = { vals, unit: per }; }
      }
      const vals = dd.vals, sc = scale(Math.max(...vals), g, type === 'picture' ? 'pic' : 'bar', dd.unit);
      data = { kind: 'cat', ds: ds.id, cats, vals, per, sc, type };
      graph = type === 'picture' ? drawPicture(ds, cats, vals, per) : drawBar(ds, cats, vals, sc);
      // the example reads one category; the questions then avoid it
      const order = r.shuffle(cats.map((c, i) => i));
      const ei = order[0], rest = order.slice(1);
      exHtml = type === 'picture'
        ? example(`<b>${esc(ds.read(cats[ei]))}</b>`, `Find the ${esc(cats[ei])} row and count the pictures: ${vals[ei] / per}. ${per === 1 ? `Each picture stands for 1, so the answer is <b>${vals[ei]}</b>.` : `Each picture stands for ${per}, so ${vals[ei] / per} × ${per} = <b>${vals[ei]}</b>.`}`)
        : example(`<b>${esc(ds.read(cats[ei]))}</b>`, `Find the ${esc(cats[ei])} bar. Go to the top of the bar, then look straight across to the scale: <b>${vals[ei]}</b>.`);
      const at = i => ({ i, c: cats[i] });
      const mxI = vals.indexOf(Math.max(...vals)), mnI = vals.indexOf(Math.min(...vals));
      add(ds.read(cats[rest[0]]), vals[rest[0]], { k: 'read', i: rest[0] });
      add(ds.read(cats[rest[1]]), vals[rest[1]], { k: 'read', i: rest[1] });
      const askMax = G === 1 || r.chance(.5);
      add(askMax ? ds.most : ds.least, cats[askMax ? mxI : mnI], { k: askMax ? 'max' : 'min' });
      const pair = r.distinct(1, () => { const [a, b] = r.sample(cats.map((c, i) => i), 2); return vals[a] > vals[b] ? [a, b] : null; })[0];
      if (pair) add(ds.more(cats[pair[0]], cats[pair[1]]), vals[pair[0]] - vals[pair[1]], { k: 'more', i: pair[0], j: pair[1] });
      if (G >= 2) { const [a, b] = r.sample(cats.map((c, i) => i), 2).sort((x, y) => x - y); add(ds.both(cats[a], cats[b]), vals[a] + vals[b], { k: 'both', i: a, j: b }); }
      add(ds.total, sum(vals), { k: 'total' });
      if (G >= 3) {   // two-step: two categories together compared with a third
        const tri = r.distinct(1, () => { const [a, b, c] = r.sample(cats.map((x, i) => i), 3); return vals[a] + vals[b] > vals[c] ? [Math.min(a, b), Math.max(a, b), c] : null; })[0];
        if (tri) add(ds.two(cats[tri[0]], cats[tri[1]], cats[tri[2]]),
          vals[tri[0]] + vals[tri[1]] - vals[tri[2]], { k: 'two', i: tri[0], j: tri[1], m: tri[2] });
      }
      if (G === 5) { const i = rest[2] ?? rest[0], d = gcd(vals[i], sum(vals)); add(`${ds.frac(cats[i])} Write it in simplest form.`, `${vals[i] / d}/${sum(vals) / d}`, { k: 'frac', i }); }
      if (G >= 2) {   // reasoning: a "twice as many" claim
        const pairs = []; cats.forEach((a, i) => cats.forEach((b, j) => { if (i !== j && vals[i] > vals[j]) pairs.push([i, j]); }));
        const yes = pairs.filter(([i, j]) => vals[i] === 2 * vals[j]);
        const [i, j] = yes.length && r.chance(.5) ? r.pick(yes) : r.pick(pairs);
        const ok = vals[i] === 2 * vals[j];
        reason = { q: `A student says ${ds.claim(cats[i], cats[j])}. Is the student right? Use numbers from the graph to explain.`,
          a: ok ? `Yes. ${cats[i]} has ${vals[i]} and ${cats[j]} has ${vals[j]}, and ${vals[j]} × 2 = ${vals[i]}.` : `No. ${cats[i]} has ${vals[i]} and ${cats[j]} has ${vals[j]}. Twice ${vals[j]} is ${vals[j] * 2}, not ${vals[i]}.`, k: 'twice', i, j, ok };
      }
      void at;
    } else if (type === 'line') {
      let ds, ld = null;
      for (let t = 0; t < 40 && !ld; t++) { ds = r.pick(LINES); ld = lineData(r, ds, g); }
      const { xs, vals } = ld;
      const sc = scale(ds.hi, g, 'line');
      data = { kind: 'line', ds: ds.id, xs, vals, sc, unit: ld.unit };
      graph = drawLine(ds, xs, vals, sc);
      const order = r.shuffle(xs.map((x, i) => i)), ei = order[0];
      exHtml = example(`<b>${esc(ds.read(xs[ei]))}</b>`, `Find ${esc(ds.xname(xs[ei]))} along the bottom. Go up to the point, then look straight across to the scale: <b>${fmt(vals[ei], 2)} ${esc(ds.u)}</b>.`);
      const u = ds.u;
      add(ds.read(xs[order[1]]), fmt(vals[order[1]], 2), { k: 'read', i: order[1] }, u);
      if (G <= 5) add(ds.read(xs[order[2]]), fmt(vals[order[2]], 2), { k: 'read', i: order[2] }, u);
      if (!ds.mono) { const mx = r.chance(.5); const i = vals.indexOf(mx ? Math.max(...vals) : Math.min(...vals)); add(mx ? ds.most : ds.least, ds.xname(xs[i]).replace(/^\w/, c => c.toUpperCase()), { k: mx ? 'max' : 'min', i }); }
      const ab = r.distinct(1, () => { const [a, b] = r.sample(xs.map((x, i) => i), 2).sort((x, y) => x - y); return vals[b] > vals[a] ? [a, b] : null; })[0];
      if (ab) add(ds.change(xs[ab[0]], xs[ab[1]]), fmt(vals[ab[1]] - vals[ab[0]], 2), { k: 'change', i: ab[0], j: ab[1] }, u);
      const steps = vals.slice(1).map((x, i) => Math.abs(x - vals[i])), bi = steps.indexOf(Math.max(...steps));
      add(ds.biggest, `${ds.xname(xs[bi])} and ${ds.xname(xs[bi + 1])}`, { k: 'biggest', i: bi });
      if (ds.add && G <= 5) add(ds.total, fmt(sum(vals), 2), { k: 'total' }, u);
      if (G >= 6) {
        add(`What is the mean (average) of the ${xs.length} values? Round to the nearest tenth.`, fmt(round1(sum(vals) / vals.length), 1), { k: 'mean' }, u);
        add(`What is the median of the ${xs.length} values?`, fmt(median(vals), 2), { k: 'median' }, u);
        add(`What is the range of the values?`, fmt(Math.max(...vals) - Math.min(...vals), 2), { k: 'range' }, u);
      }
      const d = vals[vals.length - 1] - vals[0];
      reason = { q: `Did ${ds.noun} go up or down from ${ds.xname(xs[0])} to ${ds.xname(xs[xs.length - 1])}? By how much? Explain how the graph shows it.`,
        a: `${d > 0 ? 'Up' : 'Down'} by ${fmt(Math.abs(d), 2)} ${u}: from ${fmt(vals[0], 2)} to ${fmt(vals[vals.length - 1], 2)}. The last point is ${d > 0 ? 'higher' : 'lower'} than the first.`, k: 'trend', d };
      if (d === 0) reason = { q: `Was ${ds.noun} higher at ${ds.xname(xs[0])} or at ${ds.xname(xs[xs.length - 1])}? Explain how the graph shows it.`, a: `Neither: both are ${fmt(vals[0], 2)} ${u}, so the first and last points are at the same height.`, k: 'trend', d };
    } else {
      const ds = r.pick(DOTS);
      const dat = dotData(r, ds, g);
      data = { kind: 'dot', ds: ds.id, data: dat };
      const vs = []; for (let x = ds.lo; x <= ds.hi; x += ds.step) vs.push(x);
      const cnt = x => dat.filter(y => y === x).length;
      graph = `<p class="ws-text">${esc(ds.survey)} The table shows the data in the order it was collected.</p>` +
        `<table class="ws-table gr-data"><tbody>${[dat.slice(0, Math.ceil(dat.length / 2)), dat.slice(Math.ceil(dat.length / 2))].map(row => `<tr>${row.map(x => `<td>${x}</td>`).join('')}</tr>`).join('')}</tbody></table>` + drawDots(ds, dat);
      const order = r.shuffle(vs.filter(x => cnt(x) > 0)), ex = order[0];
      exHtml = example(`<b>${esc(ds.at(ex))}</b>`, `Count the dots above ${ex}: <b>${cnt(ex)}</b>. Each dot is one of the ${ds.who}.`);
      add(ds.at(order[1]), cnt(order[1]), { k: 'at', x: order[1] });
      add(`How many ${ds.who} are in the data set?`, dat.length, { k: 'n' });
      const modeV = vs.reduce((b, x) => cnt(x) > cnt(b) ? x : b, vs[0]);
      add('What is the mode?', modeV, { k: 'mode' }, ds.u);
      add('What is the median?', fmt(median(dat), 2), { k: 'median' }, ds.u);
      add('What is the range?', Math.max(...dat) - Math.min(...dat), { k: 'range' }, ds.u);
      add('What is the mean? Round to the nearest tenth.', fmt(round1(sum(dat) / dat.length), 1), { k: 'mean' }, ds.u);
      const cut = r.pick(vs.slice(1, -2));
      add(ds.over(cut), dat.filter(y => y > cut).length, { k: 'over', x: cut });
      const mn = Math.min(...dat), mx = Math.max(...dat);
      const outside = r.chance(.5);
      const cands = vs.filter(x => outside ? (x < mn || x > mx) : (x >= mn && x <= mx));
      const nv = cands.length ? r.pick(cands) : vs[0];
      const changes = nv < mn || nv > mx;
      reason = { q: `${ds.newWho} ${nv} ${nv === 1 ? ds.unitOne : ds.unitWord} is added to the data. Does the range change? Explain.`,
        a: changes ? `Yes. ${nv} is ${nv < mn ? 'below the smallest' : 'above the largest'} value, so the range becomes ${Math.max(mx, nv) - Math.min(mn, nv)} instead of ${mx - mn}.` : `No. ${nv} is not below the smallest value (${mn}) or above the largest (${mx}), so the range stays ${mx - mn}.`, k: 'range2', nv };
    }
    const parts = [part('', exHtml), part('', graph)];
    const n = items.length;
    parts.push(part('Questions', `<div class="gr-q">${fill(qs, G <= 2 ? 1 : 2)}</div>`));
    if (reason) {
      parts.push(part('', `<div class="ws-q"><p><span class="ws-num">${n + 1}.</span> ${esc(reason.q)}</p>${lines(2)}${keyline(esc(reason.a))}</div>`));
      items.push(reason);
    }
    const gl = GRADES.find(x => x[0] === g)[1];
    const tname = TYPES[type].toLowerCase();
    return {
      title: `Reading a ${tname.replace('table and dot plot', 'dot plot')}`, level: gl,
      ican: G >= 6 ? `I can read a ${type === 'dot' ? 'dot plot' : 'line graph'} and find the mean, median and range.` : `I can read a ${tname} and use it to compare and add.`,
      directions: G <= 2 ? 'Look at the graph. Write each answer on the line.' : 'Use the graph to answer each question. Write the answer on the line. Write a full sentence for the last question.',
      minutes: G <= 2 ? 15 : 20, materials: 'pencil' + (G >= 6 ? ', calculator (optional)' : ''),
      parts, items, gdata: data,
      mistakes: type === 'picture' ? (G === 3 ? 'Counting pictures instead of multiplying by the key: with a key of 2, four pictures stand for 8.' : 'Skipping or double-counting a picture in a long row.')
        : type === 'bar' ? 'Reading the bar against the wrong gridline, especially between labeled lines; adding when the question asks how many more.'
        : type === 'line' ? 'Reading the value at the wrong point along the bottom, and giving the bigger value instead of the change between two points.' + (G >= 6 ? ' Finding the median without putting the values in order first.' : '')
        : 'Finding the median from the table without sorting it (the dot plot is already in order), and giving the most common count instead of the value for the mode.',
      notes: `Each sheet has a fresh dataset and its own graph. The scale fits the grade: ${G <= 2 ? 'ones' : G === 3 ? 'a key of 2 on picture graphs and 2s or 5s on bar graphs' : 'gridlines at friendly steps, with some values halfway between at grades 5 and up'}. The last question asks for a reason, so accept any answer that uses the numbers correctly.`,
    };
  },
  verify(s, v) {
    const out = [], d = s.gdata, G = +v.grade;
    const S = a => a.reduce((x, y) => x + y, 0);
    const near = (a, b) => Math.abs(parseFloat(String(a).replace(/,/g, '')) - b) < 1e-9;
    if (d.kind === 'cat') {
      const { cats, vals, per, sc, type } = d;
      if (type === 'picture') { if (vals.some(x => x % per)) out.push('a picture row needs part of a picture'); if (vals.some(x => x / per > 10)) out.push('a picture row is too long'); if (G > 3) out.push('picture graph above grade 3'); }
      else { if (Math.max(...vals) > sc.top) out.push('a bar is taller than the scale'); if (vals.some(x => x % (G === 5 ? sc.minor / 2 : sc.minor))) out.push('a bar ends between gridlines'); if (G > 5) out.push('bar graph above grade 5'); }
      if (G === 1 && (cats.length > 3 || Math.max(...vals) > 10)) out.push('grade 1 data too big');
      const mx = Math.max(...vals), mn = Math.min(...vals);
      for (const it of s.items) {
        const want = { read: () => vals[it.i], max: () => vals.filter(x => x === mx).length === 1 ? cats[vals.indexOf(mx)] : 'tie', min: () => vals.filter(x => x === mn).length === 1 ? cats[vals.indexOf(mn)] : 'tie',
          more: () => vals[it.i] - vals[it.j], both: () => vals[it.i] + vals[it.j], total: () => S(vals), two: () => vals[it.i] + vals[it.j] - vals[it.m],
          frac: () => { let a = vals[it.i], b = S(vals); for (let k = a; k > 1; k--) if (a % k === 0 && b % k === 0) { a /= k; b /= k; } return `${a}/${b}`; },
          twice: () => null }[it.k];
        if (!want) { out.push(`unknown question kind ${it.k}`); continue; }
        const w = want();
        if (it.k === 'twice') { if ((vals[it.i] === 2 * vals[it.j]) !== it.ok || !it.a.startsWith(it.ok ? 'Yes' : 'No')) out.push(`${it.q}: key ${it.a}`); continue; }
        if (String(w) !== String(it.a)) out.push(`${it.q}: key ${it.a}, should be ${w}`);
        if (typeof w === 'number' && w < 0) out.push(`${it.q}: negative answer`);
      }
    } else if (d.kind === 'line') {
      const { xs, vals, sc, unit } = d;
      if (G < 4) out.push('line graph below grade 4');
      if (Math.max(...vals) > sc.top) out.push('a point is above the scale');
      if (vals.some(x => Math.abs(x / (sc.minor / 2) - Math.round(x / (sc.minor / 2))) > 1e-9)) out.push('a point is not on or halfway between gridlines');
      if (G === 4 && vals.some(x => x % sc.minor)) out.push('grade 4 point between gridlines');
      void unit;
      const steps = vals.slice(1).map((x, i) => Math.abs(x - vals[i]));
      for (const it of s.items) {
        if (it.k === 'read') { if (!near(it.a, vals[it.i])) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'max' || it.k === 'min') { const t = it.k === 'max' ? Math.max(...vals) : Math.min(...vals); if (vals[it.i] !== t || vals.filter(x => x === t).length !== 1) out.push(`${it.q}: not the one ${it.k}`); }
        else if (it.k === 'change') { if (!near(it.a, vals[it.j] - vals[it.i]) || vals[it.j] <= vals[it.i]) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'biggest') { const big = Math.max(...steps); if (steps[it.i] !== big || steps.filter(x => x === big).length !== 1) out.push(`${it.q}: not the one biggest change`); if (!it.a.includes(' and ')) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'total') { if (!near(it.a, S(vals))) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'mean') { if (!near(it.a, Math.round(S(vals) / vals.length * 10) / 10)) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'median') { const so = vals.slice().sort((a, b) => a - b), m = so.length / 2; const md = so.length % 2 ? so[Math.floor(m)] : (so[m - 1] + so[m]) / 2; if (!near(it.a, md)) out.push(`${it.q}: key ${it.a}, median ${md}`); }
        else if (it.k === 'range') { if (!near(it.a, Math.max(...vals) - Math.min(...vals))) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'trend') { if (it.d !== vals[vals.length - 1] - vals[0]) out.push('trend: wrong change'); }
        else out.push(`unknown kind ${it.k}`);
      }
      if (xs.length !== vals.length) out.push('labels and points differ');
    } else {
      const dat = d.data, so = dat.slice().sort((a, b) => a - b), n = so.length;
      if (G < 6) out.push('dot plot below grade 6');
      const counts = new Map(); dat.forEach(x => counts.set(x, (counts.get(x) || 0) + 1));
      const top = Math.max(...counts.values());
      for (const it of s.items) {
        if (it.k === 'at') { if (+it.a !== (counts.get(it.x) || 0)) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'n') { if (+it.a !== n) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'mode') { const modes = [...counts].filter(([, c]) => c === top).map(([x]) => x); if (modes.length !== 1 || +it.a !== modes[0]) out.push(`${it.q}: key ${it.a}, modes ${modes}`); }
        else if (it.k === 'median') { const md = n % 2 ? so[(n - 1) / 2] : (so[n / 2 - 1] + so[n / 2]) / 2; if (!near(it.a, md)) out.push(`${it.q}: key ${it.a}, median ${md}`); }
        else if (it.k === 'range') { if (+it.a !== so[n - 1] - so[0]) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'mean') { if (!near(it.a, Math.round(S(dat) / n * 10) / 10)) out.push(`${it.q}: key ${it.a}`); if (G === 6 && Math.abs(S(dat) * 10 / n - Math.round(S(dat) * 10 / n)) > 1e-9) out.push('grade 6 mean needs rounding'); }
        else if (it.k === 'over') { if (+it.a !== dat.filter(x => x > it.x).length) out.push(`${it.q}: key ${it.a}`); }
        else if (it.k === 'range2') { const ch = it.nv < so[0] || it.nv > so[n - 1]; if (!it.a.startsWith(ch ? 'Yes' : 'No')) out.push(`${it.q}: key ${it.a}`); }
        else out.push(`unknown kind ${it.k}`);
      }
    }
    return out;
  },
});
})();
