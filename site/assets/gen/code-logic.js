// Code and Logic generator, grades K-12. Unplugged computer science practice with an answer key for every item.
// K-3 grid programs drawn in SVG: follow arrow programs to an animal or a carrot, hop along a numbered track, write the
// arrow program through a maze, collect stars with a pick-up card, find the one wrong arrow, shorten paths with repeat
// loops, predict where a looping program stops, and run an if-then robot over colored squares (CSTA 1A-AP-08, 1A-AP-10,
// 1A-AP-14, 1B-AP-10, 1B-AP-15). Values in named boxes through a story, a score program and work-backwards puzzles
// (1A-AP-09, 1B-AP-09). Codes: secret shape codes, pixel pictures from row codes or 1s and 0s, a two-color bead code
// (5-bit binary), Caesar and keyword ciphers, a digit-sum checksum and small-number public key math (1A-AP-09,
// 1B-NI-05, 2-DA-07, 2-NI-06). Python programs from grade 4: trace tables, loop traces, memory boxes, predict the
// output, lists, local and global scope, counting loop steps and recursion with the call stack (1B-AP-09, 2-AP-11,
// 2-AP-12, 2-AP-14, 3A-AP-15, 3B-AP-10, 3B-AP-11). Data types, password combinations and entropy, hashing, a hash table
// with linear probing, stacks and queues, sorting passes, Dijkstra's shortest paths and making change with dynamic
// programming (2-AP-11, 2-NI-05, 3B-AP-10, 3B-AP-11, 3B-AP-12).
// Every program is generated from a template and run by the template's own JavaScript; verify() re-runs the printed
// code with a small, separate Python interpreter (or re-solves the puzzle another way) and compares every answer.
(() => {
const { part, example, fill, blank, key, keyline, esc, lines } = Gen.h;
const { fmt } = Gen.m;

/* ---------- small shared helpers ---------- */
const range = n => Array.from({ length: n }, (_, i) => i);
const AR = { U: '↑', D: '↓', L: '←', R: '→' };
const DX = { U: 0, D: 0, L: -1, R: 1 }, DY = { U: -1, D: 1, L: 0, R: 0 };
const OPP = { U: 'D', D: 'U', L: 'R', R: 'L' };
const DIRS4 = ['U', 'D', 'L', 'R'];
const arrows = prog => prog.map(d => d === 'P' ? '★' : AR[d]).join(' ');
const cards = (prog, cls = '') => `<span class="cl-cards ${cls}">${prog.map(d => `<span class="cl-card">${d === 'P' ? '★' : AR[d]}</span>`).join('')}</span>`;
const emptyCards = n => `<span class="cl-cards">${range(n).map(() => '<span class="cl-card cl-empty"></span>').join('')}</span>`;
const keyCards = prog => `<span class="cl-cards">${prog.map(d => `<span class="cl-card cl-empty"><span class="ws-ans">${d === 'P' ? '★' : AR[d]}</span></span>`).join('')}</span>`;
const COLS = 'ABCDEFGH';
const cellName = (x, y) => COLS[x] + (y + 1);
const big = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
const A26 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const codeBlock = (src, mark) => `<pre class="cl-code">${src.split('\n').map((l, i) => `<span class="cl-ln${mark && mark.includes(i + 1) ? ' cl-mark' : ''}"><i>${i + 1}</i>${esc(l) || ' '}</span>`).join('')}</pre>`;

/* ---------- a small Python interpreter, used only by verify() ----------
   Supports: ints, strings, True/False, lists; = += -= *=; print; if/elif/else; for x in range(...) or a list or string;
   while; def with parameters, return and global; list append/insert/remove/pop, len, str, int, abs, max, min; the
   operators + - * // % ** == != < > <= >= and or not in. Names assigned inside a function are local unless declared
   global, as in Python. Reports what was printed, the variables after every simple line, line counts and calls. */
function pyRun(src, hook) {
  const L = src.split('\n');
  const TOK = /\s*(?:(\d+)|("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')|([A-Za-z_]\w*)|(==|!=|<=|>=|\/\/|\*\*|[-+*/%<>()[\],.:=]))/y;
  function lex(s) {
    const out = []; TOK.lastIndex = 0;
    while (TOK.lastIndex < s.length) {
      if (/^\s*$/.test(s.slice(TOK.lastIndex))) break;
      const m = TOK.exec(s); if (!m) throw new Error('cannot read: ' + s);
      if (m[1]) out.push({ t: 'num', v: +m[1] }); else if (m[2]) out.push({ t: 'str', v: m[2].slice(1, -1) });
      else if (m[3]) out.push({ t: ['and', 'or', 'not', 'in', 'True', 'False'].includes(m[3]) ? m[3] : 'name', v: m[3] }); else out.push({ t: m[4] });
    }
    return out;
  }
  function parseExpr(toks) {
    let i = 0;
    const peek = () => toks[i] && toks[i].t, eat = t => { if (peek() !== t) throw new Error('expected ' + t + ' in ' + JSON.stringify(toks)); return toks[i++]; };
    const BIN = [['or'], ['and'], null, ['==', '!=', '<', '>', '<=', '>=', 'in'], ['+', '-'], ['*', '//', '%', '/']];
    function level(k) {
      if (k === 2) { if (peek() === 'not') { i++; return { k: 'not', a: level(2) }; } return level(3); }
      if (k === 6) return unary();
      let a = level(k + 1);
      while (BIN[k].includes(peek()) || (k === 3 && peek() === 'not' && toks[i + 1] && toks[i + 1].t === 'in')) {
        let op = toks[i++].t; if (op === 'not') { i++; op = 'not in'; }
        a = { k: 'bin', op, a, b: level(k + 1) };
      }
      return a;
    }
    function unary() { if (peek() === '-') { i++; return { k: 'neg', a: unary() }; } const b = postfix(); if (peek() === '**') { i++; return { k: 'bin', op: '**', a: b, b: unary() }; } return b; }
    function args(close) { const out = []; while (peek() !== close) { out.push(level(0)); if (peek() === ',') i++; } eat(close); return out; }
    function postfix() {
      let e = atom();
      for (;;) {
        if (peek() === '(') { i++; e = { k: 'call', f: e, args: args(')') }; }
        else if (peek() === '[') { i++; e = { k: 'idx', a: e, b: level(0) }; eat(']'); }
        else if (peek() === '.') { i++; e = { k: 'attr', a: e, name: eat('name').v }; }
        else return e;
      }
    }
    function atom() {
      const t = toks[i++]; if (!t) throw new Error('unexpected end');
      if (t.t === 'num') return { k: 'lit', v: t.v }; if (t.t === 'str') return { k: 'lit', v: t.v };
      if (t.t === 'True' || t.t === 'False') return { k: 'lit', v: t.t === 'True' };
      if (t.t === 'name') return { k: 'name', v: t.v };
      if (t.t === '(') { const e = level(0); eat(')'); return e; }
      if (t.t === '[') return { k: 'list', items: args(']') };
      throw new Error('bad token ' + t.t);
    }
    const e = level(0); if (i !== toks.length) throw new Error('extra tokens'); return e;
  }
  // statements by indentation
  const rows = L.map((s, n) => ({ n: n + 1, ind: s.match(/^ */)[0].length, s: s.trim() })).filter(x => x.s && !x.s.startsWith('#'));
  let p = 0;
  function block(ind) {
    const out = [];
    while (p < rows.length && rows[p].ind === ind) {
      const row = rows[p++], s = row.s; let m;
      const body = () => { if (p >= rows.length || rows[p].ind <= ind) throw new Error('empty block at line ' + row.n); return block(rows[p].ind); };
      if ((m = s.match(/^def (\w+)\((.*)\):$/))) { const st = { k: 'def', n: row.n, name: m[1], params: m[2].split(',').map(x => x.trim()).filter(Boolean) }; st.body = body(); out.push(st); }
      else if ((m = s.match(/^if (.*):$/))) {
        const st = { k: 'if', n: row.n, arms: [[parseExpr(lex(m[1])), body()]], els: null };
        while (p < rows.length && rows[p].ind === ind && /^(elif .*|else):$/.test(rows[p].s)) {
          const r2 = rows[p++], m2 = r2.s.match(/^elif (.*):$/);
          if (m2) st.arms.push([parseExpr(lex(m2[1])), body()]); else st.els = body();
        }
        out.push(st);
      }
      else if ((m = s.match(/^for (\w+) in (.*):$/))) out.push({ k: 'for', n: row.n, v: m[1], e: parseExpr(lex(m[2])), body: body() });
      else if ((m = s.match(/^while (.*):$/))) out.push({ k: 'while', n: row.n, e: parseExpr(lex(m[1])), body: body() });
      else if ((m = s.match(/^return\s*(.*)$/))) out.push({ k: 'ret', n: row.n, e: m[1] ? parseExpr(lex(m[1])) : null });
      else if ((m = s.match(/^global (.*)$/))) out.push({ k: 'global', n: row.n, names: m[1].split(',').map(x => x.trim()) });
      else if ((m = s.match(/^([A-Za-z_]\w*(?:\[.*\])?)\s*([-+*]?)=(?!=)\s*(.*)$/))) {
        const tm = m[1].match(/^(\w+)(?:\[(.*)\])?$/);
        out.push({ k: 'set', n: row.n, name: tm[1], idx: tm[2] != null ? parseExpr(lex(tm[2])) : null, op: m[2], e: parseExpr(lex(m[3])) });
      }
      else out.push({ k: 'expr', n: row.n, e: parseExpr(lex(s)) });
    }
    return out;
  }
  const prog = block(0);
  if (p !== rows.length) throw new Error('bad indentation near line ' + rows[p].n);
  // which names each function assigns (its locals)
  function assigned(stmts, set, glob) {
    for (const st of stmts) {
      if (st.k === 'set' && !st.idx) set.add(st.name);
      if (st.k === 'for') set.add(st.v);
      if (st.k === 'global') st.names.forEach(x => glob.add(x));
      for (const b of [st.body, st.els, ...(st.arms || []).map(a => a[1])]) if (b) assigned(b, set, glob);
    }
  }
  const G = new Map(), out = [], counts = {}, calls = [];
  let steps = 0;
  const show = (v, inner) => typeof v === 'boolean' ? (v ? 'True' : 'False') : Array.isArray(v) ? '[' + v.map(x => show(x, true)).join(', ') + ']'
    : typeof v === 'string' ? (inner ? `'${v}'` : v) : String(v);
  const truthy = v => Array.isArray(v) ? v.length > 0 : !!v;
  function frameOf(name, F) { return F && F.locals.has(name) ? F.vars : G; }
  function get(name, F) {
    const M = frameOf(name, F);
    if (M.has(name)) return M.get(name);
    if (['len', 'str', 'int', 'abs', 'max', 'min', 'print', 'range'].includes(name)) return { builtin: name };
    throw new Error('unknown name ' + name);
  }
  function ev(e, F) {
    switch (e.k) {
      case 'lit': return e.v;
      case 'name': return get(e.v, F);
      case 'list': return e.items.map(x => ev(x, F));
      case 'neg': return -ev(e.a, F);
      case 'not': return !truthy(ev(e.a, F));
      case 'idx': { const a = ev(e.a, F); let b = ev(e.b, F); if (b < 0) b += a.length; if (b < 0 || b >= a.length) throw new Error('index out of range'); return a[b]; }
      case 'attr': return { obj: ev(e.a, F), method: e.name };
      case 'bin': {
        if (e.op === 'and') { const a = ev(e.a, F); return truthy(a) ? ev(e.b, F) : a; }
        if (e.op === 'or') { const a = ev(e.a, F); return truthy(a) ? a : ev(e.b, F); }
        const a = ev(e.a, F), b = ev(e.b, F);
        switch (e.op) {
          case '+': if (typeof a !== typeof b && !(Array.isArray(a) && Array.isArray(b))) throw new Error('TypeError: + mixes types'); return Array.isArray(a) ? a.concat(b) : a + b;
          case '-': return a - b; case '*': return typeof a === 'string' ? a.repeat(b) : a * b;
          case '//': return Math.floor(a / b); case '%': return ((a % b) + b) % b; case '/': return a / b; case '**': return a ** b;
          case '==': return JSON.stringify(a) === JSON.stringify(b); case '!=': return JSON.stringify(a) !== JSON.stringify(b);
          case '<': return a < b; case '>': return a > b; case '<=': return a <= b; case '>=': return a >= b;
          case 'in': return Array.isArray(b) ? b.some(x => JSON.stringify(x) === JSON.stringify(a)) : String(b).includes(a);
          case 'not in': return Array.isArray(b) ? !b.some(x => JSON.stringify(x) === JSON.stringify(a)) : !String(b).includes(a);
        }
        throw new Error('bad op ' + e.op);
      }
      case 'call': {
        const f = ev(e.f, F), a = e.args.map(x => ev(x, F));
        if (f.builtin) {
          switch (f.builtin) {
            case 'print': out.push(a.map(x => show(x)).join(' ')); return null;
            case 'len': return a[0].length; case 'str': return show(a[0]); case 'int': return parseInt(a[0], 10);
            case 'abs': return Math.abs(a[0]); case 'max': return Math.max(...(a.length > 1 ? a : a[0])); case 'min': return Math.min(...(a.length > 1 ? a : a[0]));
            case 'range': { const [lo, hi, st] = a.length === 1 ? [0, a[0], 1] : [a[0], a[1], a[2] || 1]; const r = []; for (let k = lo; st > 0 ? k < hi : k > hi; k += st) r.push(k); return r; }
          }
        }
        if (f.method) {
          const o = f.obj;
          switch (f.method) {
            case 'append': o.push(a[0]); return null;
            case 'insert': o.splice(a[0], 0, a[1]); return null;
            case 'remove': { const k = o.findIndex(x => JSON.stringify(x) === JSON.stringify(a[0])); if (k < 0) throw new Error('remove: not in list'); o.splice(k, 1); return null; }
            case 'pop': { if (!o.length) throw new Error('pop from empty list'); const k = a.length ? a[0] : o.length - 1; return o.splice(k, 1)[0]; }
            case 'index': return o.indexOf(a[0]);
            case 'upper': return o.toUpperCase();
          }
          throw new Error('unknown method ' + f.method);
        }
        if (f.def) {
          const d = f.def, vars = new Map();
          d.params.forEach((pn, k) => vars.set(pn, a[k]));
          const depth = (F ? F.depth : 0) + 1;
          const call = { name: d.name, args: a.slice(), depth };
          calls.push(call);
          const r = run(d.body, { vars, locals: d.locals, depth });
          call.ret = r && r.ret !== undefined ? r.ret : null;
          return call.ret;
        }
        throw new Error('not callable');
      }
    }
    throw new Error('bad expression');
  }
  function run(stmts, F) {
    for (const st of stmts) {
      if (++steps > 20000) throw new Error('too many steps');
      counts[st.n] = (counts[st.n] || 0) + 1;
      switch (st.k) {
        case 'def': { const locals = new Set(); assigned(st.body, locals, new Set()); st.params.forEach(x => locals.add(x));
          const g2 = new Set(); assigned(st.body, new Set(), g2); g2.forEach(x => locals.delete(x)); st.locals = locals; G.set(st.name, { def: st }); break; }
        case 'global': break;
        case 'set': {
          const M = frameOf(st.name, F);
          let val = ev(st.e, F);
          if (st.idx) { const arr = M.get(st.name), k = ev(st.idx, F); if (st.op) throw new Error('no op= on index'); arr[k] = val; }
          else {
            if (st.op) { const old = get(st.name, F); val = st.op === '+' ? (typeof old !== typeof val ? (() => { throw new Error('TypeError'); })() : old + val) : st.op === '-' ? old - val : old * val; }
            M.set(st.name, val);
          }
          if (hook) hook(st.n, G, F, out); break;
        }
        case 'expr': ev(st.e, F); if (hook) hook(st.n, G, F, out); break;
        case 'ret': return { ret: st.e ? ev(st.e, F) : null };
        case 'if': {
          let done = false;
          for (const [c, b] of st.arms) if (truthy(ev(c, F))) { const r = run(b, F); if (r) return r; done = true; break; }
          if (!done && st.els) { const r = run(st.els, F); if (r) return r; }
          break;
        }
        case 'for': {
          const seq = ev(st.e, F), items = typeof seq === 'string' ? seq.split('') : seq.slice();
          for (const x of items) { frameOf(st.v, F).set(st.v, x); if (hook) hook(st.n, G, F, out); const r = run(st.body, F); if (r) return r; counts[st.n]++; }
          break;
        }
        case 'while': {
          while (truthy(ev(st.e, F))) { const r = run(st.body, F); if (r) return r; counts[st.n]++; if (++steps > 20000) throw new Error('too many steps'); }
          break;
        }
      }
    }
    return null;
  }
  run(prog, null);
  return { out, G, counts, calls, show };
}
// "what a value prints as", for comparing make()'s answers with the interpreter's
const pyShow = (v, inner) => typeof v === 'boolean' ? (v ? 'True' : 'False') : Array.isArray(v) ? '[' + v.map(x => pyShow(x, true)).join(', ') + ']'
  : typeof v === 'string' ? (inner ? `'${v}'` : v) : String(v);

/* ---------- grid drawings (K-3) ---------- */
const FONT = 'font-family="Helvetica, Arial, sans-serif"';
const RED = '#b03020';
const FILLS = { B: '#a9cdf2', Y: '#f6e07a' };
const ck = (x, y) => x + ',' + y;
// o: {labels, walls: Set, puddles: Set, colors: {key: 'B'|'Y'}, pics: [{x, y, t}], route: [[x, y]] (gray, shown),
//     keyRoute: [[x, y]] (red, key only), keyX: [x, y] (red X, key only), face: {x, y, d} (a robot arrow)}
function grid(W, H, S, o = {}) {
  const m = o.labels ? 20 : 3, X = x => m + x * S, Y = y => m + y * S, C = v => v * S + S / 2;
  let b = '';
  for (const [k, c] of Object.entries(o.colors || {})) {
    const [x, y] = k.split(',').map(Number);
    b += `<rect x="${X(x)}" y="${Y(y)}" width="${S}" height="${S}" fill="${FILLS[c]}"/><text x="${X(x) + 3}" y="${Y(y) + 11}" ${FONT} font-size="10" font-weight="700" fill="#333">${c}</text>`;
  }
  for (const k of o.walls || []) { const [x, y] = k.split(',').map(Number); b += `<rect x="${X(x)}" y="${Y(y)}" width="${S}" height="${S}" fill="#555"/>`; }
  for (const k of o.puddles || []) {
    const [x, y] = k.split(',').map(Number);
    b += `<rect x="${X(x)}" y="${Y(y)}" width="${S}" height="${S}" fill="#cfe2f5"/><path d="M${X(x) + S * .18} ${Y(y) + S * .45} q${S * .16} ${-S * .12} ${S * .32} 0 t${S * .32} 0 M${X(x) + S * .18} ${Y(y) + S * .65} q${S * .16} ${-S * .12} ${S * .32} 0 t${S * .32} 0" fill="none" stroke="#3a6ea5" stroke-width="2"/>`;
  }
  for (let i = 0; i <= W; i++) b += `<line x1="${X(i)}" y1="${m}" x2="${X(i)}" y2="${Y(H)}" stroke="#333" stroke-width="${i === 0 || i === W ? 2 : 1}"/>`;
  for (let j = 0; j <= H; j++) b += `<line x1="${m}" y1="${Y(j)}" x2="${X(W)}" y2="${Y(j)}" stroke="#333" stroke-width="${j === 0 || j === H ? 2 : 1}"/>`;
  if (o.labels) {
    for (let i = 0; i < W; i++) b += `<text x="${m + C(i)}" y="${m - 6}" ${FONT} font-size="12" font-weight="700" text-anchor="middle">${COLS[i]}</text>`;
    for (let j = 0; j < H; j++) b += `<text x="${m - 6}" y="${m + C(j) + 4}" ${FONT} font-size="12" font-weight="700" text-anchor="end">${j + 1}</text>`;
  }
  const line = (pts, attrs) => `<polyline points="${pts.map(p => `${m + C(p[0])},${m + C(p[1])}`).join(' ')}" fill="none" stroke-linecap="round" stroke-linejoin="round" ${attrs}/>`;
  if (o.route) b += line(o.route, `stroke="#9a9a9a" stroke-width="${Math.max(4, S * .2)}" stroke-dasharray="1 ${Math.max(7, S * .32)}"`) + line(o.route, 'stroke="#9a9a9a" stroke-width="2"');
  for (const p of o.pics || []) b += `<text x="${m + C(p.x)}" y="${m + C(p.y) + S * .22}" font-size="${(S * (p.small ? .44 : .62)).toFixed(1)}" text-anchor="middle"${p.ink ? ` fill="${p.ink}" ${FONT} font-weight="700"` : ''}>${p.t}</text>`;
  if (o.face) {
    const { x, y, d } = o.face, cx = m + C(x), cy = m + C(y), a = { R: 0, D: 90, L: 180, U: 270 }[d], s = S * .32;
    b += `<polygon points="${cx + s},${cy} ${cx - s * .7},${cy - s * .75} ${cx - s * .35},${cy} ${cx - s * .7},${cy + s * .75}" fill="#222" transform="rotate(${a} ${cx} ${cy})"/>`;
  }
  if (o.keyRoute) b += `<g class="ws-ans">${line(o.keyRoute, `stroke="${RED}" stroke-width="3" opacity=".85"`)}</g>`;
  if (o.keyX) {
    const cx = m + C(o.keyX[0]), cy = m + C(o.keyX[1]), s = S * .3;
    b += `<g class="ws-ans"><path d="M${cx - s} ${cy - s}L${cx + s} ${cy + s}M${cx + s} ${cy - s}L${cx - s} ${cy + s}" stroke="${RED}" stroke-width="4" stroke-linecap="round"/></g>`;
  }
  const w = X(W) + 3, h = Y(H) + 3;
  return `<svg class="gen-svg cl-grid" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(o.label || 'A grid')}" style="max-width:${(w / 96).toFixed(2)}in">${b}</svg>`;
}
// walk a program from (x, y); returns the cells visited (start included)
function walk(x, y, prog) {
  const cells = [[x, y]];
  for (const d of prog) { if (d === 'P') continue; x += DX[d]; y += DY[d]; cells.push([x, y]); }
  return cells;
}
const inside = (W, H) => c => c[0] >= 0 && c[1] >= 0 && c[0] < W && c[1] < H;
// a route from a to b: the x moves and the y moves, in one of three orders
function route(r, a, b) {
  const dx = b[0] - a[0], dy = b[1] - a[1];
  const xs = Array(Math.abs(dx)).fill(dx > 0 ? 'R' : 'L'), ys = Array(Math.abs(dy)).fill(dy > 0 ? 'D' : 'U');
  const how = r.int(0, 2);
  if (how === 0) return xs.concat(ys);
  if (how === 1) return ys.concat(xs);
  const out = [], X2 = xs.slice(), Y2 = ys.slice();
  while (X2.length || Y2.length) out.push((X2.length && (!Y2.length || r.chance(.5)) ? X2 : Y2).shift());
  return out;
}
// shortest paths by breadth-first search: dist and the number of shortest paths to every cell
function bfs(W, H, blocked, s) {
  const dist = new Map([[ck(...s), 0]]), ways = new Map([[ck(...s), 1]]), q = [s];
  while (q.length) {
    const c = q.shift(), dc = dist.get(ck(...c));
    for (const d of DIRS4) {
      const n = [c[0] + DX[d], c[1] + DY[d]], k = ck(...n);
      if (!inside(W, H)(n) || blocked.has(k)) continue;
      if (!dist.has(k)) { dist.set(k, dc + 1); ways.set(k, 0); q.push(n); }
      if (dist.get(k) === dc + 1) ways.set(k, ways.get(k) + ways.get(ck(...c)));
    }
  }
  return { dist, ways };
}
function cellsOf(r, W, H, n, avoid = new Set()) {
  const all = []; for (let x = 0; x < W; x++) for (let y = 0; y < H; y++) if (!avoid.has(ck(x, y))) all.push([x, y]);
  return r.sample(all, n);
}
const ANIMALS = [['🐱', 'cat'], ['🐶', 'dog'], ['🐰', 'rabbit'], ['🐸', 'frog'], ['🐻', 'bear'], ['🐷', 'pig'], ['🐮', 'cow'], ['🐔', 'hen'], ['🐟', 'fish'], ['🐢', 'turtle'], ['🦆', 'duck'], ['🐭', 'mouse']];
const ring = (t, on) => `<span class="cl-pick">${t}${on ? '<span class="ws-ans cl-ring"></span>' : ''}</span>`;

/* K: follow the arrows to an animal */
function skFollow(r, n) {
  for (let t = 0; t < 40; t++) {
    const W = 4, H = 4, cells = cellsOf(r, W, H, 6), start = cells[0], zoo = r.sample(ANIMALS, 5);
    const spots = cells.slice(1).map((c, i) => ({ c, a: zoo[i] }));
    const at = new Map(spots.map(s => [ck(...s.c), s]));
    const progs = r.distinct(n, () => {
      const s = r.pick(spots), p = route(r, start, s.c);
      if (p.length < 2 || p.length > 5) return null;
      const path = walk(start[0], start[1], p);
      if (path.slice(1, -1).some(c => at.has(ck(...c)))) return null;
      return { p, s };
    }, x => x.p.join(''));
    if (progs.length < n || new Set(progs.map(x => x.s.a[1])).size < Math.min(n, 4)) continue;
    const pics = [{ x: start[0], y: start[1], t: '🤖' }].concat(spots.map(s => ({ x: s.c[0], y: s.c[1], t: s.a[0] })));
    const svg = grid(W, H, 50, { pics, label: `A 4 by 4 grid with a robot and ${zoo.map(z => z[1]).join(', ')}` });
    const items = progs.map((x, i) => ({ q: `Program ${i + 1}: ${arrows(x.p)}`, a: x.s.a[1], k: 'follow', start, prog: x.p, spots: spots.map(s => [s.c[0], s.c[1], s.a[1]]), W, H }));
    const rows = progs.map(x => `<div class="cl-row">${cards(x.p)}<span class="cl-picks">${zoo.map(z => ring(z[0], z === x.s.a)).join('')}</span></div>`);
    return {
      ican: 'I can follow arrow steps to see where the robot goes.',
      directions: 'Put your finger on the robot. Move one square for each arrow. Circle the animal the robot reaches.',
      parts: [part('', `<div class="cl-center">${svg}</div>`), part('Follow the arrows', fill(rows))], items,
      materials: 'pencil or crayon', minutes: 15,
      mistakes: 'Moving two squares for one arrow, or turning the paper so up and down swap. Keep the paper still and say each step out loud.',
      notes: 'Read each program aloud for children who are still learning arrows: "right, right, down." The robot always starts from its own square.',
    };
  }
}

/* K and grade 1: hop along a numbered track */
function skHop(r, n, g) {
  const K = g === 'k', top = K ? 6 : 10;
  const progs = r.distinct(n, () => {
    const len = K ? r.int(2, 4) : r.int(3, 6), start = K ? 0 : r.int(1, top);
    const p = range(len).map(() => r.chance(K ? .72 : .6) ? 'R' : 'L');
    let at = start;
    for (const d of p) { at += d === 'R' ? 1 : -1; if (at < (K ? 0 : 1) || at > top) return null; }
    if (K && at < 1) return null;
    if (!K && at === start) return null;
    return { p, start, end: at };
  }, x => x.start + x.p.join(''));
  const pad = (i, w) => K ? `<span class="cl-pad"><span>🥕</span><b>${i}</b></span>` : `<span class="cl-pad cl-lily"><b>${i}</b></span>`;
  const track = `<div class="cl-track">${K ? '<span class="cl-pad"><span>🐰</span><b>start</b></span>' : ''}${range(top).map(i => pad(i + 1)).join('')}</div>`;
  const items = progs.map((x, i) => ({ q: `${K ? '' : `Start ${x.start}: `}${arrows(x.p)}`, a: String(x.end), k: 'hop', start: x.start, prog: x.p, top }));
  const rows = progs.map(x => K
    ? `<div class="cl-row">${cards(x.p)}<span class="cl-picks">${range(top).map(i => ring(`🥕<small>${i + 1}</small>`, i + 1 === x.end)).join('')}</span></div>`
    : `<div class="cl-row"><span class="cl-start">Start on pad ${x.start}.</span>${cards(x.p)}<span>The frog stops on pad ${blank(x.end, 2.6)}</span></div>`);
  return {
    ican: K ? 'I can follow arrows to see where the bunny hops.' : 'I can read a program and say where it ends.',
    directions: K ? 'The bunny starts on the start mat. Hop one carrot for each arrow: → hops right, ← hops back. Circle the carrot where the bunny lands.'
      : 'Put the frog on the start pad. Each → hops one pad up the numbers, each ← hops one pad back. Write the pad where the frog stops.',
    parts: [part('', track), part(K ? 'Where does the bunny land?' : 'Where does the frog stop?', fill(rows))], items,
    materials: K ? 'pencil or crayon, a small counter for the bunny' : 'pencil, a small counter for the frog', minutes: 15,
    mistakes: 'Counting the pad you start on as the first hop. The first hop lands on the next pad.',
    notes: K ? 'Read each program aloud the first time. A counter on the track lets children act out every hop.' : 'Students can check by counting: the number of → minus the number of ← is how far the frog moves.',
  };
}

/* K: write the arrows through a maze */
function skMaze(r, n) {
  const W = 4, H = 4, out = [];
  for (let t = 0; t < n * 80 && out.length < n; t++) {
    const [s, goal] = cellsOf(r, W, H, 2), walls = new Set(cellsOf(r, W, H, r.int(3, 5), new Set([ck(...s), ck(...goal)])).map(c => ck(...c)));
    const { dist, ways } = bfs(W, H, walls, s), d = dist.get(ck(...goal));
    if (d == null || d < 3 || d > 6 || ways.get(ck(...goal)) !== 1) continue;
    // the one shortest path, read back from the goal
    const path = [goal];
    while (dist.get(ck(...path[0])) > 0) {
      const c = path[0];
      path.unshift(DIRS4.map(dd => [c[0] - DX[dd], c[1] - DY[dd]]).find(p => dist.get(ck(...p)) === dist.get(ck(...c)) - 1 && !walls.has(ck(...p))));
    }
    const prog = path.slice(1).map((c, i) => DIRS4.find(dd => DX[dd] === c[0] - path[i][0] && DY[dd] === c[1] - path[i][1]));
    if (out.some(o => o.prog.join('') === prog.join('') && o.s + '' === s + '')) continue;
    out.push({ s, goal, walls, prog, path });
  }
  const items = out.map((m, i) => ({ q: `Maze ${i + 1}: ${m.s} to ${m.goal} walls ${[...m.walls].join(' ')}`, a: arrows(m.prog), k: 'maze', W, H, s: m.s, goal: m.goal, walls: [...m.walls], prog: m.prog }));
  const cellsH = out.map((m, i) => `<div class="cl-cell"><p><span class="ws-num">${i + 1}.</span></p>${grid(W, H, 40, { walls: m.walls, pics: [{ x: m.s[0], y: m.s[1], t: '🐛' }, { x: m.goal[0], y: m.goal[1], t: '🍎' }], keyRoute: m.path, label: 'A maze with a bug, an apple and dark walls' })}${keyCards(m.prog)}</div>`);
  return {
    ican: 'I can find a way through a maze and write it as arrows.',
    directions: 'Help the bug get to the apple. Dark squares are walls. Trace the way with your finger, then draw one arrow in each box.',
    parts: [part('', example(`${cards(['R', 'R', 'D'])} means: one square right, one more right, then one down.`)), part('Mazes', `<div class="cl-cells cl-c3">${cellsH.join('')}</div>`)], items,
    materials: 'pencil or crayon', minutes: 15,
    mistakes: 'Drawing the arrow for the way the bug faces instead of the way it moves on the page. Up on the page is ↑, every time.',
    notes: 'Each maze has exactly one shortest way, and there is one box for each step of it. The key draws the way in red.',
  };
}

/* grade 1: collect three stars, with walls and puddles */
function skCollect(r, n) {
  const W = 5, H = 5, out = [];
  const solve = (block, s, stars) => {   // breadth-first search over (cell, stars picked up); returns a shortest program
    const k0 = ck(...s) + '|0', prev = new Map([[k0, null]]), q = [[s[0], s[1], 0]];
    const full = (1 << stars.length) - 1;
    while (q.length) {
      const [x, y, mk] = q.shift(), kk = ck(x, y) + '|' + mk;
      if (mk === full) { const prog = []; let c = kk; while (prev.get(c)) { prog.unshift(prev.get(c)[1]); c = prev.get(c)[0]; } return prog; }
      const si = stars.findIndex(st => st[0] === x && st[1] === y);
      const next = DIRS4.map(d => [x + DX[d], y + DY[d], mk, d]);
      if (si >= 0 && !(mk & (1 << si))) next.push([x, y, mk | (1 << si), 'P']);
      for (const [nx, ny, nm, d] of next) {
        const nk = ck(nx, ny) + '|' + nm;
        if (!inside(W, H)([nx, ny]) || block.has(ck(nx, ny)) || prev.has(nk)) continue;
        prev.set(nk, [kk, d]); q.push([nx, ny, nm]);
      }
    }
    return null;
  };
  for (let t = 0; t < n * 60 && out.length < n; t++) {
    const cs = cellsOf(r, W, H, 4 + 4 + 2), s = cs[0], stars = cs.slice(1, 4);
    const walls = new Set(cs.slice(4, 4 + r.int(2, 4)).map(c => ck(...c))), puddles = new Set(cs.slice(8, 10).map(c => ck(...c)));
    const block = new Set([...walls, ...puddles]);
    const prog = solve(block, s, stars);
    if (!prog || prog.length < 9 || prog.length > 14) continue;
    out.push({ s, stars, walls, puddles, prog });
  }
  const items = out.map((m, i) => ({ q: `Course ${i + 1}: ${m.s} stars ${m.stars.join(' ')}`, a: arrows(m.prog), k: 'collect', W, H, s: m.s, stars: m.stars, walls: [...m.walls], puddles: [...m.puddles], prog: m.prog }));
  const cellsH = out.map((m, i) => {
    const pics = [{ x: m.s[0], y: m.s[1], t: '🤖' }].concat(m.stars.map(c => ({ x: c[0], y: c[1], t: '★', ink: '#222' })));
    return `<div class="cl-cell"><p><span class="ws-num">${i + 1}.</span> Collect all 3 stars. Use ${m.prog.length} cards or fewer.</p>${grid(W, H, 36, { walls: m.walls, puddles: m.puddles, pics, keyRoute: walk(m.s[0], m.s[1], m.prog), label: 'A grid with a robot, three stars, walls and puddles' })}${keyCards(m.prog)}<p class="cl-boxes-note">${emptyCards(Math.max(0, 14 - m.prog.length))}</p></div>`;
  });
  return {
    ican: 'I can write a program that gets a robot around walls to collect things.',
    directions: 'Write a program for the robot. Use arrows to move one square. Use the ★ card to pick up a star when the robot is on it. The robot cannot go on a wall (dark) or a puddle (wavy blue).',
    parts: [part('', example(`${cards(['R', 'P', 'D', 'D', 'P'])} means: move right and pick up a star, then move down two and pick up another.`)), part('Obstacle courses', `<div class="cl-cells cl-c2">${cellsH.join('')}</div>`)], items,
    materials: 'pencil', minutes: 25,
    mistakes: 'Walking over a star without the ★ card, so it is not picked up, and cutting through a puddle. Test the program with a finger before calling it done.',
    notes: 'The card count is the length of the shortest program, so it is a target, not a rule: any program that collects all 3 stars without touching a wall or a puddle works. The key shows one shortest program, drawn in red.',
  };
}

/* grades 1-2: the one wrong arrow */
function skDebug(r, n) {
  const W = 5, H = 4, out = [];
  const ends = (s, p) => walk(s[0], s[1], p);
  for (let t = 0; t < n * 80 && out.length < n; t++) {
    const [s, goal] = cellsOf(r, W, H, 2), good = route(r, s, goal);
    if (good.length < 3 || good.length > 6) continue;
    const i = r.int(0, good.length - 1), bad = r.pick(DIRS4.filter(d => d !== good[i]));
    const buggy = good.slice(); buggy[i] = bad;
    const bp = ends(s, buggy);
    if (!bp.every(inside(W, H))) continue;
    let fixes = 0;
    for (let j = 0; j < buggy.length; j++) for (const d of DIRS4) {
      if (d === buggy[j]) continue;
      const f = buggy.slice(); f[j] = d; const fp = ends(s, f), e = fp[fp.length - 1];
      if (fp.every(inside(W, H)) && e[0] === goal[0] && e[1] === goal[1]) fixes++;
    }
    if (fixes !== 1 || out.some(o => o.buggy.join('') === buggy.join(''))) continue;
    out.push({ s, goal, good, buggy, i });
  }
  const items = out.map((m, k) => ({ q: `Program ${k + 1}: ${arrows(m.buggy)} from ${m.s} to ${m.goal}`, a: `Step ${m.i + 1}: ${AR[m.good[m.i]]}`, k: 'debug', W, H, s: m.s, goal: m.goal, buggy: m.buggy, i: m.i, fix: m.good[m.i] }));
  const cellsH = out.map((m, k) => {
    const cardsH = `<span class="cl-cards">${m.buggy.map((d, j) => `<span class="cl-card">${AR[d]}${j === m.i ? `<span class="ws-ans cl-cross">✗</span><span class="ws-ans cl-fix">${AR[m.good[m.i]]}</span>` : ''}</span>`).join('')}</span>`;
    return `<div class="cl-cell"><p><span class="ws-num">${k + 1}.</span></p>${grid(W, H, 34, { pics: [{ x: m.s[0], y: m.s[1], t: '🤖' }, { x: m.goal[0], y: m.goal[1], t: '💎' }], keyRoute: ends(m.s, m.good), label: 'A grid with a robot and a treasure' })}<p>${cardsH}</p><p class="cl-fixline">Fix: step ${blank(m.i + 1, 2)} should be ${blank(AR[m.good[m.i]], 2)}</p></div>`;
  });
  return {
    ican: 'I can find the bug in a program and fix it.',
    directions: 'Each program should take the robot to the treasure, but one arrow is wrong. Trace it with your finger. Cross out the wrong arrow, draw the right one above it, and fill in the fix.',
    parts: [part('', example(`The robot needs ${cards(['R', 'R', 'D'])} but the program says ${cards(['R', 'U', 'D'])}. Step 2 is the bug: it should be →.`)), part('Bug hunt', `<div class="cl-cells cl-c2">${cellsH.join('')}</div>`)], items,
    materials: 'pencil', minutes: 20,
    mistakes: 'Fixing the last arrow because that is where the robot ends up wrong. The bug is the first step that goes the wrong way.',
    notes: 'Every program has exactly one arrow that can be changed to reach the treasure, so the key is the only fix. The key draws the fixed path in red.',
  };
}

/* grade 2: shorten a path with repeat loops */
function skLoops(r, n) {
  const W = 6, H = 6, out = [];
  const perp = { U: ['L', 'R'], D: ['L', 'R'], L: ['U', 'D'], R: ['U', 'D'] };
  for (let t = 0; t < n * 120 && out.length < n; t++) {
    const segs = [], ns = r.int(2, 3);
    let last = null;
    for (let k = 0; k < ns; k++) {
      if (r.chance(.3) && !segs.some(s => s.body.length === 2)) {
        const d1 = last ? r.pick(perp[last]) : r.pick(DIRS4), d2 = r.pick(perp[d1]);
        segs.push({ times: r.int(2, 3), body: [d1, d2] }); last = d2;
      } else {
        const d = last ? r.pick(perp[last]) : r.pick(DIRS4);
        segs.push({ times: r.int(2, 5), body: [d] }); last = d;
      }
    }
    const prog = segs.flatMap(s => range(s.times).flatMap(() => s.body));
    if (prog.length < 6 || prog.length > 13) continue;
    const s = [r.int(0, W - 1), r.int(0, H - 1)], path = walk(s[0], s[1], prog);
    if (!path.every(inside(W, H)) || new Set(path.map(c => ck(...c))).size !== path.length) continue;
    if (out.some(o => o.prog.join('') === prog.join(''))) continue;
    out.push({ s, segs, prog, path });
  }
  const segText = s => s.times === 1 ? s.body.map(d => AR[d]).join(' ') : `repeat ${s.times}: ${s.body.map(d => AR[d]).join(' ')}`;
  const items = [];
  const cellsH = out.map((m, k) => {
    const wrote = m.segs.reduce((a, s) => a + s.body.length, 0), saved = m.prog.length - wrote;
    items.push({ q: `Path ${k + 1}: ${m.s} ${arrows(m.prog)} loop program`, a: m.segs.map(segText).join(', then '), k: 'loopprog', s: m.s, segs: m.segs, path: m.path },
      { q: `Path ${k + 1}: ${arrows(m.prog)} arrows without loops`, a: String(m.prog.length), k: 'loopcount', prog: m.prog },
      { q: `Path ${k + 1}: ${arrows(m.prog)} arrows saved`, a: String(saved), k: 'loopsaved', prog: m.prog, segs: m.segs });
    const e = m.path[m.path.length - 1];
    return `<div class="cl-cell"><p><span class="ws-num">${k + 1}.</span></p>${grid(W, H, 25, { route: m.path, pics: [{ x: m.s[0], y: m.s[1], t: '🤖' }, { x: e[0], y: e[1], t: '🏁' }], label: 'A grid with a path drawn from a robot to a flag' })}
<p class="cl-prog">${m.segs.map(s => `<span class="cl-seg">${blank(segText(s), 6.5)}</span>`).join('')}</p>
<p>Arrows with no loops: ${blank(m.prog.length, 2.4)} Arrows I wrote: ${blank(wrote, 2.4)} Saved: ${blank(saved, 2.4)}</p></div>`;
  });
  return {
    ican: 'I can use a repeat loop to make a program shorter.',
    directions: 'Write a program for each path, one line for each part of the path. Use repeat when the same move happens again and again. Then count: how many arrows would you need with no loops, how many arrows did you write, and how many did the loops save?',
    parts: [part('', example(`The path goes right 4 times, then up 2 times. With no loops: → → → → ↑ ↑, that is 6 arrows.`, `With loops: <b>repeat 4: →</b>, then <b>repeat 2: ↑</b>. That is 2 arrows written, so the loops saved 6 − 2 = 4 arrows.`,
      `A zigzag can loop two arrows: → ↑ → ↑ → ↑ is <b>repeat 3: → ↑</b> (2 arrows written).`)), part('Loop the paths', `<div class="cl-cells cl-c2">${cellsH.join('')}</div>`)], items,
    materials: 'pencil', minutes: 25,
    mistakes: 'Counting the squares in the path instead of the moves between them (one less), and writing repeat 1. A part that happens once is just the arrow.',
    notes: 'Some paths can be looped more than one way, for example a zigzag after a straight part. Accept any loop program that follows the gray path, and check the saved count against the student\'s own program: saved = arrows with no loops − arrows written.',
  };
}

/* grade 2: predict where a looping program stops */
function skPredict(r, n) {
  const W = 5, H = 5, out = [];
  const EV = ['When the green flag is clicked', 'When the space key is pressed', 'When the car is tapped'];
  const SAYS = ['Beep', 'Honk', 'Zoom', 'Hi'];
  for (let t = 0; t < n * 100 && out.length < n; t++) {
    const nb = r.int(2, 3), blocks = [];
    let says = 0;
    for (let k = 0; k < nb; k++) {
      const kind = r.pick(['one', 'rep', 'rep', 'rep2', 'say']);
      if (kind === 'one') blocks.push({ times: 1, body: [r.pick(DIRS4)] });
      else if (kind === 'rep') blocks.push({ times: r.int(2, 4), body: [r.pick(DIRS4)] });
      else if (kind === 'rep2') { const a = r.pick(DIRS4); blocks.push({ times: r.int(2, 3), body: [a, r.pick(DIRS4.filter(d => d !== OPP[a] && d !== a))] }); }
      else if (!says) { says = 1; blocks.push({ times: r.int(2, 3), body: [r.pick(DIRS4), 'say:' + r.pick(SAYS)] }); }
    }
    if (blocks.length < 2) continue;
    const moves = blocks.flatMap(b => range(b.times).flatMap(() => b.body)).filter(x => !x.startsWith('say'));
    const said = blocks.flatMap(b => range(b.times).flatMap(() => b.body)).filter(x => x.startsWith('say')).map(x => x.slice(4));
    const s = [r.int(0, W - 1), r.int(0, H - 1)], path = walk(s[0], s[1], moves);
    if (moves.length < 4 || !path.every(inside(W, H))) continue;
    const e = path[path.length - 1];
    if (e[0] === s[0] && e[1] === s[1]) continue;
    out.push({ ev: r.pick(EV), blocks, s, e, path, said });
  }
  const lineOf = b => {
    const body = b.body.map(x => x.startsWith('say') ? `say "${x.slice(4)}"` : AR[x]).join(', ');
    return b.times === 1 ? `move ${body}` : `repeat ${b.times}: ${b.body.map(x => x.startsWith('say') ? `say "${x.slice(4)}"` : 'move ' + AR[x]).join(', ')}`;
  };
  const items = [];
  const cellsH = out.map((m, k) => {
    const text = m.blocks.map(lineOf);
    items.push({ q: `Program ${k + 1}: from ${cellName(...m.s)} ${text.join('; ')}`, a: cellName(...m.e), k: 'predict', s: m.s, blocks: m.blocks, W, H });
    if (m.said.length) items.push({ q: `Program ${k + 1}: ${text.join('; ')} says`, a: m.said.join(' '), k: 'says', blocks: m.blocks });
    return `<div class="cl-cell"><p><span class="ws-num">${k + 1}.</span></p><div class="cl-side">${grid(W, H, 24, { labels: true, pics: [{ x: m.s[0], y: m.s[1], t: '🚗' }], keyRoute: m.path, keyX: m.e, label: `A 5 by 5 grid with columns A to E, rows 1 to 5, and a car on ${cellName(...m.s)}` })}
<div class="cl-blocks"><p class="cl-hat">${esc(m.ev)}</p>${text.map(x => `<p class="cl-blk">${esc(x)}</p>`).join('')}</div></div>
<p>The car stops on ${blank(cellName(...m.e), 2.6)}${m.said.length ? ` It says: ${blank(m.said.join(' '), 7)}` : ''}</p></div>`;
  });
  return {
    ican: 'I can read a program with loops and predict what it will do.',
    directions: 'Read each program. Start the car on its square and move it one square for each arrow. Do everything inside a repeat that many times. Draw an X where the car stops and write the square. If the car says something, write what it says.',
    parts: [part('', example('repeat 3: move →, say "Hi" means: move right and say Hi, move right and say Hi, move right and say Hi. The car moves 3 squares and says Hi Hi Hi.')), part('Predict the program', `<div class="cl-cells cl-c2">${cellsH.join('')}</div>`)], items,
    materials: 'pencil, a small counter for the car', minutes: 20,
    mistakes: 'Doing the moves inside a repeat only once, and doing only the first move of a two-step loop again. Say each pass aloud: "one, two, three."',
    notes: 'The event at the top tells when the program starts; it does not move the car. Squares are named by column letter, then row number, like C4. The key draws the path and the stopping square in red.',
  };
}

/* grades 3-4: an if-then robot on colored squares */
function skIfGrid(r, n) {
  const W = 6, H = 6;
  for (let t = 0; t < 60; t++) {
    const cs = cellsOf(r, W, H, 9), colors = {};
    cs.slice(0, 5).forEach(c => { colors[ck(...c)] = 'B'; }); cs.slice(5).forEach(c => { colors[ck(...c)] = 'Y'; });
    const blueTurn = r.pick(['right', 'left']), yellowTurn = blueTurn === 'right' ? 'left' : 'right';
    const TURN = { right: { U: 'R', R: 'D', D: 'L', L: 'U' }, left: { U: 'L', L: 'D', D: 'R', R: 'U' } };
    const runs = r.distinct(n, () => {
      const s = [r.int(0, W - 1), r.int(0, H - 1)], d0 = r.pick(DIRS4), times = r.int(5, 8);
      if (colors[ck(...s)]) return null;
      let x = s[0], y = s[1], d = d0, turns = 0;
      const path = [[x, y]];
      for (let i = 0; i < times; i++) {
        x += DX[d]; y += DY[d];
        if (x < 0 || y < 0 || x >= W || y >= H) return null;
        path.push([x, y]);
        const c = colors[ck(x, y)];
        if (c) { d = TURN[c === 'B' ? blueTurn : yellowTurn][d]; turns++; }
      }
      if (turns < 2) return null;
      return { s, d0, times, e: [x, y], path };
    }, x => x.s + x.d0 + x.times);
    if (runs.length < n) continue;
    const prog = times => `repeat ${times} times:\n  move forward 1 square\n  if on a blue square, turn ${blueTurn}\n  if on a yellow square, turn ${yellowTurn}`;
    const WORD = { U: 'up', D: 'down', L: 'left', R: 'right' };
    const items = runs.map((m, k) => ({ q: `Run ${k + 1}: start ${cellName(...m.s)} facing ${WORD[m.d0]}, repeat ${m.times}`, a: cellName(...m.e), k: 'ifgrid', s: m.s, d0: m.d0, times: m.times, colors, blueTurn, W, H }));
    const cellsH = runs.map((m, k) => `<div class="cl-cell"><p><span class="ws-num">${k + 1}.</span> Start on ${cellName(...m.s)}, facing ${WORD[m.d0]}. Repeat <b>${m.times}</b> times.</p>${grid(W, H, 25, { labels: true, colors, face: { x: m.s[0], y: m.s[1], d: m.d0 }, keyRoute: m.path, keyX: m.e, label: `A 6 by 6 grid with blue and yellow squares and a robot on ${cellName(...m.s)}` })}<p>The robot stops on ${blank(cellName(...m.e), 2.6)}</p></div>`);
    return {
      ican: 'I can follow a program with if-then rules and find where it ends.',
      directions: `Run each program. The arrow shows where the robot faces. Each time through the loop it moves forward 1 square, then checks the square it is on: blue (B) means turn ${blueTurn}, yellow (Y) means turn ${yellowTurn}. Turning does not move it. Draw the path, put an X where it stops, and write the square.`,
      parts: [part('', example(`Facing right on a blue square, "turn ${blueTurn}" makes the robot face ${blueTurn === 'right' ? 'down' : 'up'}. The next move goes that way.`)), part('The program', codeBlock(prog('N'))), part('Run the robot', `<div class="cl-cells cl-c2">${cellsH.join('')}</div>`)], items,
      materials: 'pencil, a small counter with an arrow drawn on it', minutes: 25,
      mistakes: 'Turning toward the right side of the page instead of the robot\'s own right, and checking the color before moving instead of after.',
      notes: 'Every run turns at least twice and stays on the grid. A counter with an arrow on it helps students keep track of which way the robot faces. The key draws each path in red.',
    };
  }
}

/* ---------- named boxes and variables ---------- */
const KIDS = ['Sam', 'Ana', 'Max', 'Lily', 'Ben', 'Mia', 'Leo', 'Zoe', 'Ella', 'Jack', 'Rosa', 'Omar'];
const BOX1 = [['Apples', 'apple', 'apples'], ['Eggs', 'egg', 'eggs'], ['Balls', 'ball', 'balls'], ['Crayons', 'crayon', 'crayons'], ['Shells', 'shell', 'shells'], ['Blocks', 'block', 'blocks'], ['Stickers', 'sticker', 'stickers']];
const pl = (n, one, many) => `${n} ${n === 1 ? one : many}`;

/* grade 1: one box through a 5-step story */
function story1(r, theme) {
  const [name, one, many] = theme, kids = r.sample(KIDS, 4);
  let v = r.int(2, 6);
  const start = v, steps = [];
  for (let i = 0; i < 5; i++) {
    const add = v <= 2 || (v < 9 && r.chance(.5)), k = add ? r.int(1, Math.min(4, 10 - v)) : r.int(1, Math.min(4, v));
    v += add ? k : -k;
    steps.push({ text: `${r.pick(kids)} ${add ? 'puts in' : 'takes out'} ${pl(k, one, many)}.`, v });
  }
  return { name, one, many, start, steps };
}
/* grade 2: two boxes through a 6-step story */
const STORY2 = [
  { boxes: ['Cookies', 'Money'], unit: ['cookie', 'cookies'], make: n => `Bake ${n} cookies.`, sell: (n, p) => `Sell ${n} cookies for $${p} each.`, buy: c => `Buy a bag of sugar for $${c}.`, lose: n => `Give ${n} cookies to a friend.` },
  { boxes: ['Cups', 'Money'], unit: ['cup', 'cups'], make: n => `Make ${n} cups of lemonade.`, sell: (n, p) => `Sell ${n} cups for $${p} each.`, buy: c => `Buy lemons for $${c}.`, lose: n => `Spill ${n} cups.` },
  { boxes: ['Muffins', 'Money'], unit: ['muffin', 'muffins'], make: n => `Bake ${n} muffins.`, sell: (n, p) => `Sell ${n} muffins for $${p} each.`, buy: c => `Buy paper cups for $${c}.`, lose: n => `Give ${n} muffins to a friend.` },
];
function story2(r, th) {
  let a = r.int(0, 6), m = r.int(0, 5);
  const start = [a, m], steps = [];
  for (let i = 0; i < 6; i++) {
    const opts = ['make'];
    if (a >= 2) opts.push('sell', 'sell');
    if (a >= 2) opts.push('lose');
    if (m >= 3) opts.push('buy');
    const kind = i === 0 ? 'make' : r.pick(opts);
    if (kind === 'make') { const n = r.int(4, 12); if (a + n > 40) { i--; continue; } a += n; steps.push({ text: th.make(n), v: [a, m] }); }
    else if (kind === 'sell') { const n = r.int(1, Math.min(6, a)), p = r.int(1, 3); a -= n; m += n * p; steps.push({ text: th.sell(n, p), v: [a, m] }); }
    else if (kind === 'lose') { const n = r.int(1, Math.min(3, a)); a -= n; steps.push({ text: th.lose(n), v: [a, m] }); }
    else { const c = r.int(1, Math.min(6, m)); m -= c; steps.push({ text: th.buy(c), v: [a, m] }); }
  }
  return { th, start, steps };
}
function skBoxes(r, n, g) {
  const items = [], blocks = [];
  if (g === '1') {
    r.sample(BOX1, n).forEach((th, k) => {
      const s = story1(r, th);
      const rows = s.steps.map((st, i) => { items.push({ q: `Story ${k + 1} (${s.name}, starts ${s.start}) step ${i + 1}: ${st.text}`, a: String(st.v), k: 'box1', story: s, i }); return [String(i + 1), esc(st.text), blank(st.v, 2.4)]; });
      blocks.push(`<div class="cl-story"><div class="cl-box"><span class="cl-box-name">${esc(s.name)}</span><span class="cl-box-val">${s.start}</span></div>
<div><p><span class="ws-num">${k + 1}.</span> The box named <b>${esc(s.name)}</b> starts with ${pl(s.start, s.one, s.many)}.</p>${tbl(['Step', 'What happens', `${esc(s.name)} now`], rows)}</div></div>`);
    });
    return {
      ican: 'I can keep track of a number in a box as it changes.',
      directions: 'A program keeps a number in a box with a name. Read each step. Write how many are in the box after that step.',
      parts: [part('', example('The box named Apples has 3 apples. Ana puts in 2 apples. Now Apples is <b>5</b>. Ben takes out 1 apple. Now Apples is <b>4</b>.')), part('Follow the box', blocks.join(''))], items,
      materials: 'pencil, counters', minutes: 15 + 5 * n,
      mistakes: 'Starting over from the first number at every step. Each step starts from the number you just wrote.',
      notes: 'The box is what a program calls a variable: a name with a value that can change. Counters in a real box make the idea concrete. Numbers stay between 0 and 10.',
    };
  }
  r.sample(STORY2, Math.min(n, STORY2.length)).forEach((th, k) => {
    const s = story2(r, th), [b1, b2] = th.boxes;
    const rows = [['Start', 'The boxes start like this.', String(s.start[0]), '$' + s.start[1]]].concat(s.steps.map((st, i) => {
      items.push({ q: `Story ${k + 1} step ${i + 1}: ${st.text} ${b1}`, a: String(st.v[0]), k: 'box2', story: s, i, which: 0 },
        { q: `Story ${k + 1} step ${i + 1}: ${st.text} ${b2}`, a: '$' + st.v[1], k: 'box2', story: s, i, which: 1 });
      return [String(i + 1), esc(st.text), blank(st.v[0], 2.4), blank('$' + st.v[1], 2.6)];
    }));
    blocks.push(`<div class="cl-q"><p><span class="ws-num">${k + 1}.</span> Two boxes: <b>${b1}</b> and <b>${b2}</b>.</p>${tbl(['Step', 'What happens', b1, b2], rows)}</div>`);
  });
  return {
    ican: 'I can update the values in named boxes as a program runs.',
    directions: 'Each story changes two boxes. After each step, write the new value in each box. A step can change one box or both.',
    parts: [part('', example('Cookies is 10 and Money is $0. "Sell 3 cookies for $2 each." Cookies goes down by 3 to <b>7</b>. Money goes up by 3 × $2 = $6, to <b>$6</b>.')), part('Update the boxes', blocks.join(''))], items,
    materials: 'pencil', minutes: 20,
    mistakes: 'Forgetting that a sale changes both boxes, and adding the number sold to Money instead of the money they bring in.',
    notes: 'Named boxes are variables. Selling changes two variables at once, which is the idea to talk about. Numbers stay under 100.',
  };
}
const tbl = (head, rows, cls = '') => `<table class="ws-table cl-tbl ${cls}"><thead><tr>${head.map(x => `<th>${x}</th>`).join('')}</tr></thead><tbody>${rows.map(rw => `<tr>${rw.map(x => `<td>${x}</td>`).join('')}</tr>`).join('')}</tbody></table>`;

/* grade 3: block programs (shown as blocks, kept as Python for verify) */
function blockStep(r, name, v, opts) {   // one step that changes name; returns {py, blk, v}
  for (let t = 0; t < 30; t++) {
    const kind = r.pick(opts);
    if (kind === 'add') { const k = r.int(1, 10); return { py: `${name} += ${k}`, blk: `change ${name} by ${k}`, v: v + k }; }
    if (kind === 'sub') { const k = r.int(1, 6); if (v - k < 0) continue; return { py: `${name} -= ${k}`, blk: `change ${name} by -${k}`, v: v - k }; }
    if (kind === 'dbl') { if (v === 0 || v > 30) continue; return { py: `${name} = ${name} * 2`, blk: `set ${name} to ${name} × 2`, v: v * 2 }; }
    if (kind === 'if') {
      const lim = r.int(Math.max(1, v - 6), v + 6), k = r.int(2, 9), up = r.chance(.5), cmp = r.pick(['>', '<']);
      const yes = cmp === '>' ? v > lim : v < lim, nv = yes ? (up ? v + k : v - k) : v;
      if (nv < 0) continue;
      return { py: `if ${name} ${cmp} ${lim}:\n    ${name} ${up ? '+' : '-'}= ${k}`, blk: `if ${name} ${cmp} ${lim} then change ${name} by ${up ? '' : '-'}${k}`, v: nv };
    }
  }
  return { py: `${name} += 1`, blk: `change ${name} by 1`, v: v + 1 };
}
function skScore(r, n) {
  const items = [], blocks = [];
  const NAMES = r.sample(['score', 'points', 'coins', 'stars'], n);
  NAMES.forEach((nm, k) => {
    const s0 = r.int(0, 5), st = [{ py: `${nm} = ${s0}`, blk: `set ${nm} to ${s0}`, v: s0 }];
    let v = s0, ifs = 0;
    while (st.length < 10) {
      const opt = ['add', 'add', 'sub', 'sub', 'if'].concat(st.some(x => x.py.includes('*')) ? [] : ['dbl']);
      const x = blockStep(r, nm, v, ifs >= 2 ? opt.filter(o => o !== 'if') : opt);
      if (x.py.startsWith('if')) ifs++;
      st.push(x); v = x.v;
    }
    const rows = st.map((x, i) => { items.push({ q: `Program ${k + 1} step ${i + 1}: ${x.blk}`, a: String(x.v), k: 'score', py: st.slice(0, i + 1).map(y => y.py).join('\n'), name: nm }); return [String(i + 1), `<code>${esc(x.blk)}</code>`, blank(x.v, 2.6)]; });
    blocks.push(`<div class="cl-q"><p><span class="ws-num">${k + 1}.</span> A game program changes <b>${nm}</b>.</p>${tbl(['Step', 'Block', `${nm} after the step`], rows)}</div>`);
  });
  return {
    ican: 'I can trace a variable through a program and record its value after each step.',
    directions: 'Run each program one step at a time. After each step, write the value of the variable. "Change by" adds (a minus number takes away). An if step only changes the variable when its test is true.',
    parts: [part('', example('set score to 4. change score by 3: score is 7. if score > 5 then change score by 2: 7 > 5 is true, so score is <b>9</b>. if score < 5 then change score by 10: 9 < 5 is false, so score stays <b>9</b>.')), part('Trace the score', blocks.join(''))], items,
    materials: 'pencil', minutes: 15 + 5 * n,
    mistakes: 'Doing the change in an if step even when the test is false, and treating "set" like "change". Set replaces the value; change adds to it.',
    notes: 'The blocks match block-coding tools like Scratch: "change by" adds, "set to" replaces. Every value stays at 0 or above.',
  };
}
function skStart(r, n) {
  const items = [], cells = [];
  const NAMES = ['coins', 'score', 'apples', 'gems', 'points', 'stars'];
  const puzzles = r.distinct(n, () => {
    const nm = r.pick(NAMES), s0 = r.int(1, 20), st = [];
    let v = s0;
    const nOps = r.int(2, 3);
    for (let i = 0; i < nOps; i++) {
      const x = blockStep(r, nm, v, i === 0 ? ['add', 'sub', 'dbl'] : ['add', 'sub', 'dbl', 'sub']);
      if (x.py.includes('*') && st.some(y => y.py.includes('*'))) return null;
      st.push(x); v = x.v;
    }
    return { nm, s0, st, end: v };
  }, p => p.nm + p.st.map(x => x.py).join() + p.end);
  puzzles.forEach((p, k) => {
    items.push({ q: `Puzzle ${k + 1}: ${p.st.map(x => x.blk).join('; ')} says ${p.end}`, a: String(p.s0), k: 'start', py: p.st.map(x => x.py).join('\n') + `\nprint(${p.nm})`, name: p.nm, end: p.end });
    cells.push(`<div class="cl-cell"><p><span class="ws-num">${k + 1}.</span></p><pre class="cl-code cl-blocks3">set ${p.nm} to <span class="cl-q-box">?</span>\n${p.st.map(x => esc(x.blk)).join('\n')}\nsay ${p.nm}</pre><p>It says <b>${p.end}</b>. ${p.nm} started at ${blank(p.s0, 2.6)}</p></div>`);
  });
  return {
    ican: 'I can work backward through a program to find a starting value.',
    directions: 'Each program starts with a value we do not know. You know what it says at the end. Work backward from the end: undo each step, last step first. Then check by running it forward.',
    parts: [part('', example('set coins to ?, change coins by 4, set coins to coins × 2, say coins: it says 14.', 'Undo, last step first: 14 ÷ 2 = 7, then 7 − 4 = <b>3</b>. Check: 3 + 4 = 7, 7 × 2 = 14. Yes.')), part('What was the starting value?', `<div class="cl-cells cl-c2">${cells.join('')}</div>`)], items,
    materials: 'pencil', minutes: 20,
    mistakes: 'Undoing the steps from the top instead of from the bottom, and undoing "× 2" by subtracting 2.',
    notes: 'Undoing each step in reverse order is the same thinking as solving a two-step equation. Every answer is a whole number from 1 to 20.',
  };
}

/* grade 3: translate a small Python program into block words */
function toBlocks(py) {
  return py.split('\n').map(line => {
    const ind = line.match(/^ */)[0].replace(/ {4}/g, '  '), s = line.trim(); let m;
    const ex = e => e.replace(/==/g, '=').replace(/\*/g, '×').replace(/\s%\s2 = 0/, ' is even');
    if ((m = s.match(/^for \w+ in range\((\d+)\):$/))) return `${ind}repeat ${m[1]} times:`;
    if ((m = s.match(/^if (.*):$/))) return `${ind}if ${ex(m[1])} then:`;
    if (s === 'else:') return `${ind}else:`;
    if ((m = s.match(/^(\w+) \+= (\d+)$/))) return `${ind}change ${m[1]} by ${m[2]}`;
    if ((m = s.match(/^(\w+) -= (\d+)$/))) return `${ind}change ${m[1]} by -${m[2]}`;
    if ((m = s.match(/^print\((.*)\)$/))) return `${ind}say ${m[1]}`;
    if ((m = s.match(/^(\w+) = (.*)$/))) return `${ind}set ${m[1]} to ${ex(m[2])}`;
    return ind + s;
  }).join('\n');
}

/* ---------- Python program templates: each returns {src, out} with out = the printed lines, worked in JavaScript ---------- */
const q = s => `"${s}"`;
const OUT3 = [
  r => { const a = r.pick(['clap', 'jump', 'hop']), b = r.pick(['stomp', 'spin', 'snap']), k = r.int(3, 5), out = [];
    let n = 1; for (let i = 0; i < k; i++) { if (n === 1) { out.push(a); n = 2; } else { out.push(b); n = 1; } }
    return { src: `n = 1\nfor i in range(${k}):\n    if n == 1:\n        print(${q(a)})\n        n = 2\n    else:\n        print(${q(b)})\n        n = 1`, out }; },
  r => { const s = r.int(1, 5), d = r.int(2, 4), k = r.int(3, 5), lim = s + d * r.int(1, k - 1), out = [];
    let x = s; for (let i = 0; i < k; i++) { x += d; out.push(x > lim ? 'big' : String(x)); }
    return { src: `x = ${s}\nfor i in range(${k}):\n    x += ${d}\n    if x > ${lim}:\n        print("big")\n    else:\n        print(x)`, out }; },
  r => { const k = r.int(3, 5), d = r.int(2, 5), out = []; let steps = 0;
    for (let i = 0; i < k; i++) { steps += d; out.push(String(steps)); }
    return { src: `steps = 0\nfor i in range(${k}):\n    steps += ${d}\n    print(steps)`, out }; },
  r => { const k = r.int(4, 6), t = r.int(2, k - 1), w = r.pick(['hop', 'skip', 'wave']), out = []; let c = 0;
    for (let i = 0; i < k; i++) { c += 1; out.push(c < t ? w : 'rest'); }
    return { src: `count = 0\nfor i in range(${k}):\n    count += 1\n    if count < ${t}:\n        print(${q(w)})\n    else:\n        print("rest")`, out }; },
  r => { const s = r.int(10, 20), d = r.int(2, 4), k = r.int(3, 4), out = []; let x = s;
    for (let i = 0; i < k; i++) { out.push(String(x)); x -= d; }
    out.push('done');
    return { src: `fuel = ${s}\nfor i in range(${k}):\n    print(fuel)\n    fuel -= ${d}\nprint("done")`, out }; },
];
const OUTPY = [   // [lowest grade, maker]
  [5, r => { const a = r.int(1, 4), b = a + r.int(4, 6), out = [];
    for (let i = a; i < b; i++) out.push(i % 2 === 0 ? 'even' : String(i));
    return { src: `for i in range(${a}, ${b}):\n    if i % 2 == 0:\n        print("even")\n    else:\n        print(i)`, out }; }],
  [5, r => { const n = r.int(8, 15), k = r.int(2, 4); let t = 0; for (let i = 1; i <= n; i++) if (i % k === 0) t += i;
    return { src: `total = 0\nfor i in range(1, ${n + 1}):\n    if i % ${k} == 0:\n        total = total + i\nprint(total)`, out: [String(t)] }; }],
  [5, r => { const s = r.int(1, 5), lim = r.int(20, 90), m = r.pick([2, 3]); let x = s, c = 0; while (x < lim) { x *= m; c++; }
    return { src: `n = ${s}\ncount = 0\nwhile n < ${lim}:\n    n = n * ${m}\n    count = count + 1\nprint(n, count)`, out: [`${x} ${c}`] }; }],
  [5, r => { const a = r.int(8, 15), st = r.int(2, 4), out = []; for (let i = a; i > 0; i -= st) out.push(String(i)); out.push('Go!');
    return { src: `for i in range(${a}, 0, -${st}):\n    print(i)\nprint("Go!")`, out }; }],
  [6, r => { const sc = r.sample([95, 91, 88, 84, 79, 72, 65, 58, 99, 81, 70], 3), out = sc.map(s => s >= 90 ? 'A' : s >= 80 ? 'B' : s >= 70 ? 'C' : 'D');
    return { src: `for score in [${sc.join(', ')}]:\n    if score >= 90:\n        print("A")\n    elif score >= 80:\n        print("B")\n    elif score >= 70:\n        print("C")\n    else:\n        print("D")`, out }; }],
  [6, r => { const nums = r.sample([3, 8, 12, 5, 17, 9, 21, 4, 14, 6], 5); let best = nums[0], c = 0; for (const x of nums) if (x > best) { best = x; c++; }
    return { src: `nums = [${nums.join(', ')}]\nbest = nums[0]\nchanges = 0\nfor n in nums:\n    if n > best:\n        best = n\n        changes = changes + 1\nprint(best, changes)`, out: [`${best} ${c}`] }; }],
  [7, r => { const a = r.int(2, 3), b = r.int(2, 3), out = []; for (let i = 1; i <= a; i++) for (let j = 1; j <= b; j++) out.push(String(i * j));
    return { src: `for i in range(1, ${a + 1}):\n    for j in range(1, ${b + 1}):\n        print(i * j)`, out }; }],
  [7, r => { const w = r.pick(['code', 'loop', 'byte', 'data', 'list', 'bits']); let s = ''; for (const ch of w) s = ch + s;
    return { src: `word = ""\nfor ch in ${q(w)}:\n    word = ch + word\nprint(word)`, out: [s] }; }],
  [6, r => { const s = r.int(10, 25), k = r.int(3, 6), out = []; let x = s; while (x > 0) { out.push(String(x)); x -= k; } out.push(String(x));
    return { src: `x = ${s}\nwhile x > 0:\n    print(x)\n    x = x - ${k}\nprint(x)`, out }; }],
  [8, r => { const m = r.int(7, 13), out = []; for (let i = 1; i < m; i++) { if (i % 2 === 0 && i % 3 === 0) out.push('both'); else if (i % 3 === 0) out.push('three'); else if (i % 2 === 0) out.push('two'); }
    return { src: `for n in range(1, ${m}):\n    if n % 2 == 0 and n % 3 == 0:\n        print("both")\n    elif n % 3 == 0:\n        print("three")\n    elif n % 2 == 0:\n        print("two")`, out }; }],
  [8, r => { const w = r.pick(['banana', 'robot', 'pizza', 'garden', 'planet', 'orange']); let c = 0, s = ''; for (const ch of w) { if ('aeiou'.includes(ch)) c++; else s += ch; }
    return { src: `count = 0\nrest = ""\nfor ch in ${q(w)}:\n    if ch in "aeiou":\n        count = count + 1\n    else:\n        rest = rest + ch\nprint(count, rest)`, out: [`${c} ${s}`] }; }],
];
const SCOPE = [
  r => { const a = r.int(1, 9), b = a + r.int(1, 9); return { src: `x = ${a}\n\ndef change():\n    x = ${b}\n    print(x)\n\nchange()\nprint(x)`, out: [String(b), String(a)] }; },
  r => { const a = r.int(2, 9), b = r.int(2, 9); return { src: `count = 0\n\ndef add(n):\n    global count\n    count = count + n\n\nadd(${a})\nadd(${b})\nprint(count)`, out: [String(a + b)] }; },
  r => { const a = r.int(2, 9); return { src: `def double(x):\n    x = x * 2\n    return x\n\nx = ${a}\ny = double(x)\nprint(x, y)`, out: [`${a} ${2 * a}`] }; },
  r => { const a = r.int(10, 20), b = r.int(1, 9); return { src: `total = ${a}\n\ndef show(total):\n    total = total + 1\n    print(total)\n\nshow(${b})\nprint(total)`, out: [String(b + 1), String(a)] }; },
  r => { const a = r.int(2, 5), b = r.int(2, 6), c = a + r.int(1, 3); return { src: `rate = ${a}\n\ndef pay(hours):\n    return hours * rate\n\nprint(pay(${b}))\nrate = ${c}\nprint(pay(${b}))`, out: [String(a * b), String(c * b)] }; },
  r => { const a = r.int(2, 9), b = r.int(10, 20); return { src: `def setup():\n    level = ${a}\n    return level + 1\n\nlevel = ${b}\nprint(setup())\nprint(level)`, out: [String(a + 1), String(b)] }; },
  r => { const a = r.int(1, 5), b = r.int(2, 5); return { src: `lives = ${a + 3}\n\ndef hit():\n    global lives\n    lives = lives - 1\n\ndef heal(n):\n    lives = n\n    return lives\n\nhit()\nprint(heal(${b}))\nprint(lives)`, out: [String(b), String(a + 2)] }; },
];

function skOutput(r, n, g) {
  const g3 = g === '3', gi = +g;
  const pool = g3 ? OUT3 : OUTPY.filter(([lo]) => lo <= gi).map(x => x[1]);
  const scope = g === 'scope';
  const makers = scope ? r.sample(SCOPE, n) : r.sample(pool, Math.min(n, pool.length));
  const items = [], cells = [];
  makers.forEach((mk, k) => {
    const p = mk(r), shown = g3 ? toBlocks(p.src) : p.src;
    items.push({ q: `Program ${k + 1}: ${p.src}`, a: p.out.join(' / '), k: 'output', src: p.src, out: p.out });
    cells.push(`<div class="cl-cell"><p><span class="ws-num">${k + 1}.</span> ${g3 ? 'What does it say?' : 'What does it print?'}</p>${codeBlock(shown)}<div class="cl-out">${p.out.map(o => `<span>${blank(o, Math.max(4, o.length * .7 + 1.5))}</span>`).join('')}</div></div>`);
  });
  if (scope) return {
    ican: 'I can tell a local variable from a global one and predict what a program prints.',
    directions: 'Trace each program and write every line it prints, in order, one per blank. A variable assigned inside a function is local to that function unless the function says global.',
    parts: [part('', example('<code>x = 5</code>, then a function sets <code>x = 9</code> and prints it. Inside, x is a new local variable: it prints 9. After the call, <code>print(x)</code> prints the global x: <b>5</b>.')), part('Scope detective', `<div class="cl-cells cl-c2">${cells.join('')}</div>`)], items,
    materials: 'pencil', minutes: 25,
    mistakes: 'Thinking a function that assigns x changes the global x, and forgetting that a parameter is a new local name even when it matches a global name.',
    notes: 'Programs are real Python 3; each one can be typed in and run to check. Python decides a name is local when the function assigns to it anywhere, unless it is declared global.',
  };
  return {
    ican: g3 ? 'I can trace a program with loops and if blocks and say what it does.' : 'I can trace a program and predict its exact output.',
    directions: g3 ? 'Run each program in your head. Keep track of each variable on scrap paper. Write each thing it says, in order, one per blank.'
      : 'Trace each program and write every line it prints, in order, one per blank. Keep a small trace table of the variables on scrap paper.',
    parts: [part('', example(g3 ? 'set n to 1, repeat 2 times: say n, change n by 1. It says <b>1</b>, then <b>2</b>.'
      : '<code>for i in range(1, 4): print(i * 2)</code> prints <b>2</b>, <b>4</b>, <b>6</b>. range(1, 4) gives 1, 2, 3: it stops before 4.')), part('Predict the output', `<div class="cl-cells cl-c2">${cells.join('')}</div>`)], items,
    materials: 'pencil, scrap paper', minutes: 25,
    mistakes: g3 ? 'Doing the loop one time too many or too few. Count the passes out loud.' : 'Running range one step too far (range(1, 5) stops at 4), and printing a variable before it has been changed in that pass.',
    notes: g3 ? 'The programs are written in block words like Scratch: "change by" adds, "set to" replaces, "say" shows a word.' : 'Programs are real Python 3; each one can be typed in and run to check. A line with two values, like "8 3", came from print with two values.',
  };
}

/* grade 4: a two-variable trace table */
const PAIRS = [['a', 'b'], ['x', 'y'], ['apples', 'pears'], ['red', 'blue'], ['cats', 'dogs'], ['left', 'right']];
function skTrace(r, n) {
  const items = [], cells = [];
  r.sample(PAIRS, n).forEach(([p, s], k) => {
    for (let t = 0; t < 200; t++) {
      const v = { [p]: r.int(1, 9), [s]: r.int(1, 9) }, lines = [`${p} = ${v[p]}`, `${s} = ${v[s]}`], vals = [[v[p], null], [v[p], v[s]]];
      for (let i = 0; i < 4; i++) {
        const tgt = r.pick([p, s]), oth = tgt === p ? s : p, kind = r.int(0, 4), c = r.int(1, 6);
        let e, nv;
        if (kind === 0) { e = `${tgt} + ${oth}`; nv = v[tgt] + v[oth]; }
        else if (kind === 1) { e = `${tgt} - ${oth}`; nv = v[tgt] - v[oth]; }
        else if (kind === 2) { e = `${tgt} * 2`; nv = v[tgt] * 2; }
        else if (kind === 3) { e = `${oth} + ${c}`; nv = v[oth] + c; }
        else { e = `${tgt} - ${c}`; nv = v[tgt] - c; }
        v[tgt] = nv; lines.push(`${tgt} = ${e}`); vals.push([v[p], v[s]]);
      }
      if (vals.some(x => x.some(y => y != null && (y < 0 || y > 60)))) continue;
      if (new Set(lines.slice(2).map(l => l[0])).size < 2) continue;
      const rows = vals.map((x, i) => {
        if (i > 0) items.push({ q: `Program ${k + 1} line ${i + 1}: ${lines[i]} (${p}, ${s})`, a: `${x[0]}, ${x[1]}`, k: 'trace', src: lines.join('\n'), line: i + 1, names: [p, s] });
        else items.push({ q: `Program ${k + 1} line 1: ${lines[0]}`, a: String(x[0]), k: 'trace', src: lines.join('\n'), line: 1, names: [p] });
        return [String(i + 1), blank(x[0], 2.4), x[1] == null ? '<span class="cl-dash">not made yet</span>' : blank(x[1], 2.4)];
      });
      cells.push(`<div class="cl-pair"><div><p><span class="ws-num">${k + 1}.</span></p>${codeBlock(lines.join('\n'))}</div>${tbl(['Line', p, s], rows)}</div>`);
      break;
    }
  });
  return {
    ican: 'I can use a trace table to follow variables through a program, one line at a time.',
    directions: 'Run each program one line at a time. After each line, write the value of both variables in that row. A line changes only the variable on the left of =; the other one keeps its value.',
    parts: [part('', example('<code>a = 4</code> then <code>b = a + 3</code>: after line 2, a is still 4 and b is <b>7</b>. Then <code>a = a * 2</code>: a becomes <b>8</b>, and b stays 7.')), part('Trace tables', cells.join(''))], items,
    materials: 'pencil', minutes: 20,
    mistakes: 'Leaving the unchanged variable blank instead of copying its value down, and using a variable\'s old value after it has changed.',
    notes: 'Programs are real Python. "=" means "store the value on the right in the name on the left," so <code>a = a * 2</code> doubles a. Values stay between 0 and 60.',
  };
}

/* grades 4-5: a loop that runs 5 times */
const LOOPS = [
  r => { const s = r.int(0, 5), k = r.int(2, 5), th = r.pick([['sheep', 'night'], ['total', 'counter'], ['pages', 'day']]); const t = [], c = []; let v = s;
    for (let i = 1; i <= 5; i++) { v += k; t.push(v); c.push(i); }
    return { src: `${th[0]} = ${s}\nfor ${th[1]} in range(1, 6):\n    ${th[0]} = ${th[0]} + ${k}\nprint(${th[0]})`, tot: th[0], cnt: th[1], t, c }; },
  r => { const th = r.pick([['total', 'counter'], ['sheep', 'night'], ['steps', 'lap']]); const t = [], c = []; let v = 0;
    for (let i = 1; i <= 5; i++) { v += i; t.push(v); c.push(i); }
    return { src: `${th[0]} = 0\nfor ${th[1]} in range(1, 6):\n    ${th[0]} = ${th[0]} + ${th[1]}\nprint(${th[0]})`, tot: th[0], cnt: th[1], t, c }; },
  r => { const s = r.int(0, 10), k = r.int(2, 3), th = r.pick([['total', 'counter'], ['points', 'round']]); const t = [], c = []; let v = s;
    for (let i = 1; i <= 5; i++) { v += i * k; t.push(v); c.push(i); }
    return { src: `${th[0]} = ${s}\nfor ${th[1]} in range(1, 6):\n    ${th[0]} = ${th[0]} + ${th[1]} * ${k}\nprint(${th[0]})`, tot: th[0], cnt: th[1], t, c }; },
  r => { const s = r.pick([1, 2, 3]), th = r.pick([['sheep', 'night'], ['cells', 'hour']]); const t = [], c = []; let v = s;
    for (let i = 1; i <= 5; i++) { v *= 2; t.push(v); c.push(i); }
    return { src: `${th[0]} = ${s}\nfor ${th[1]} in range(1, 6):\n    ${th[0]} = ${th[0]} * 2\nprint(${th[0]})`, tot: th[0], cnt: th[1], t, c }; },
  r => { const a = r.int(5, 10), b = r.int(1, 3), th = r.pick([['total', 'counter'], ['score', 'turn']]); const t = [], c = []; let v = 0;
    for (let i = 1; i <= 5; i++) { v += i % 2 === 0 ? a : b; t.push(v); c.push(i); }
    return { src: `${th[0]} = 0\nfor ${th[1]} in range(1, 6):\n    if ${th[1]} % 2 == 0:\n        ${th[0]} = ${th[0]} + ${a}\n    else:\n        ${th[0]} = ${th[0]} + ${b}\nprint(${th[0]})`, tot: th[0], cnt: th[1], t, c, g5: true }; },
  r => { const s = r.int(30, 50), k = r.int(3, 7), th = r.pick([['fuel', 'trip'], ['cookies', 'day']]); const t = [], c = []; let v = s;
    for (let i = 1; i <= 5; i++) { v -= k; t.push(v); c.push(i); }
    return { src: `${th[0]} = ${s}\nfor ${th[1]} in range(1, 6):\n    ${th[0]} = ${th[0]} - ${k}\nprint(${th[0]})`, tot: th[0], cnt: th[1], t, c }; },
];
function skLoopTrace(r, n, g) {
  const pool = LOOPS.filter((f, i) => g === '5' || i !== 4);
  const items = [], cells = [];
  const made = [];
  for (let t = 0; t < 60 && made.length < n; t++) { const p = r.pick(pool)(r); if (!made.some(m => m.src === p.src || m.tot === p.tot)) made.push(p); }
  made.forEach((p, k) => {
    const rows = p.c.map((c, i) => {
      items.push({ q: `Program ${k + 1} pass ${i + 1}: ${p.src}`, a: `${c}, ${p.t[i]}`, k: 'loop', src: p.src, pass: i, tot: p.tot, cnt: p.cnt });
      return [String(i + 1), blank(c, 2.4), blank(p.t[i], 2.6)];
    });
    items.push({ q: `Program ${k + 1} prints: ${p.src}`, a: String(p.t[4]), k: 'output', src: p.src, out: [String(p.t[4])] });
    cells.push(`<div class="cl-pair"><div><p><span class="ws-num">${k + 1}.</span></p>${codeBlock(p.src)}<p>It prints ${blank(p.t[4], 2.6)}</p></div>${tbl(['Pass', p.cnt, `${p.tot} after the pass`], rows)}</div>`);
  });
  return {
    ican: 'I can trace a loop and record the counter and the running total after each pass.',
    directions: 'Each loop runs 5 times. For each pass, write the value of the counter and the value of the total at the end of that pass. Then write what the program prints.',
    parts: [part('', example('<code>for counter in range(1, 6):</code> runs with counter = 1, 2, 3, 4, 5 (it stops before 6).', '<code>total = 0</code>, then each pass does <code>total = total + 3</code>: after pass 1 total is 3, after pass 2 it is 6, after pass 3 it is <b>9</b>.')), part('Loop traces', cells.join(''))], items,
    materials: 'pencil', minutes: 20 + 5 * n,
    mistakes: 'Starting the counter at 0 (range(1, 6) starts at 1), and adding to the starting value every pass instead of to the running total.',
    notes: 'Programs are real Python; the print line runs once, after the loop ends, so it prints the last total.',
  };
}

/* grade 6: be the computer, with memory boxes */
function memProg(r) {
  const who = r.pick(['Ana', 'Max', 'Zoe', 'Leo', 'Kai', 'Mia', 'Sam', 'Rosa']);
  const v = { score: 0, lives: 3, name: who }, hist = { score: [0], lives: [3], name: [who] };
  const lines = ['score = 0', 'lives = 3', `name = "${who}"`];
  const set = (k, x) => { v[k] = x; hist[k].push(x); };
  let titled = false, ifs = 0;
  while (lines.length < 9) {
    const kind = r.pick(['add', 'add', 'dbl', 'hurt', 'heal', 'bang', 'title', 'if1', 'if2']);
    if (kind === 'add') { const k = r.pick([5, 10, 15, 20, 25]); lines.push(`score = score + ${k}`); set('score', v.score + k); }
    else if (kind === 'dbl') { if (!v.score || v.score > 60) continue; lines.push('score = score * 2'); set('score', v.score * 2); }
    else if (kind === 'hurt') { if (v.lives <= 1) continue; lines.push('lives = lives - 1'); set('lives', v.lives - 1); }
    else if (kind === 'heal') { if (v.lives >= 5) continue; lines.push('lives = lives + 1'); set('lives', v.lives + 1); }
    else if (kind === 'bang') { if (v.name.endsWith('!!')) continue; lines.push('name = name + "!"'); set('name', v.name + '!'); }
    else if (kind === 'title') { if (titled) continue; titled = true; const t = r.pick(['Captain', 'Super', 'Agent']); lines.push(`name = "${t} " + name`); set('name', `${t} ${v.name}`); }
    else if (ifs < 2 && lines.length < 8) {
      ifs++;
      if (kind === 'if1') { const lim = r.pick([10, 20, 30, 40]); lines.push(`if score > ${lim}:`, '    lives = lives + 1'); if (v.score > lim) set('lives', v.lives + 1); }
      else { const lim = r.pick([2, 3, 4]); lines.push(`if lives < ${lim}:`, '    score = score + 50'); if (v.lives < lim) set('score', v.score + 50); }
    }
  }
  return { src: lines.join('\n'), hist };
}
function skMemory(r, n) {
  const items = [], cells = [];
  const progs = r.distinct(n, () => memProg(r), p => p.src);
  progs.forEach((p, k) => {
    const box = nm => {
      const h = p.hist[nm].map(x => pyShow(x));
      items.push({ q: `Program ${k + 1} ${nm}: ${p.src}`, a: h.join(', '), k: 'memory', src: p.src, name: nm });
      return `<div class="cl-mem"><p class="cl-mem-name">${nm}</p><div class="cl-mem-in">${h[0] ? `<span>${esc(h[0])}</span>` : ''}${h.slice(1).map((x, i) => `<span class="ws-ans${i < h.length - 2 ? ' cl-old' : ''}">${esc(x)}</span>`).join(' ')}</div></div>`;
    };
    cells.push(`<div class="cl-pair"><div><p><span class="ws-num">${k + 1}.</span></p>${codeBlock(p.src)}</div><div class="cl-mems">${['score', 'lives', 'name'].map(box).join('')}</div></div>`);
  });
  // the first value of each box is printed for the student; blank-free, so the key shows the rest in red
  return {
    ican: 'I can act as the computer: run a program line by line and update the memory boxes.',
    directions: 'Be the computer. Each memory box already holds its first value. Run the program one line at a time. When a line changes a variable, cross out the old value in its box and write the new one next to it. An if line only runs the indented line when its test is true.',
    parts: [part('', example('Box <b>lives</b> holds 3. The line <code>lives = lives - 1</code> runs: cross out 3, write <b>2</b>. The line <code>if lives < 3:</code> is now true, so its indented line runs too.')), part('Memory boxes', cells.join(''))], items,
    materials: 'pencil', minutes: 25,
    mistakes: 'Writing the new value without crossing out the old one, so the box seems to hold two values, and running an indented line when the if test is false.',
    notes: 'A variable holds one value at a time; crossing out keeps the history visible for checking. The key shows the crossed-out values with a line through them and the final value last. Strings are shown without their quote marks, the way print shows them.',
  };
}

/* grade 7: list operations */
const LISTS = [
  { name: 'pets', bank: ['cat', 'dog', 'fish', 'bird', 'frog', 'snake', 'mouse', 'horse', 'goat'], str: true },
  { name: 'fruits', bank: ['apple', 'pear', 'plum', 'kiwi', 'mango', 'grape', 'lime', 'peach'], str: true },
  { name: 'scores', bank: [10, 12, 15, 18, 20, 25, 30, 7, 9], str: false },
];
function listProg(r, th) {
  const lit = x => th.str ? `"${x}"` : String(x);
  const init = r.sample(th.bank, 3), L = init.slice(), steps = [];
  const fresh = () => r.pick(th.bank.filter(x => !L.includes(x)));
  const need = r.shuffle(['append', 'remove', 'index']);
  for (let i = 0; i < 6; i++) {
    const kind = i < 3 ? need[i] : r.pick(['append', 'insert', 'remove', 'pop', 'pop0', 'set', 'index', 'len']);
    let line, printed = null;
    if (kind === 'append') { const x = fresh(); L.push(x); line = `${th.name}.append(${lit(x)})`; }
    else if (kind === 'insert') { const x = fresh(), at = r.int(0, L.length - 1); L.splice(at, 0, x); line = `${th.name}.insert(${at}, ${lit(x)})`; }
    else if (kind === 'remove') { if (L.length < 2) { i--; continue; } const x = r.pick(L); L.splice(L.indexOf(x), 1); line = `${th.name}.remove(${lit(x)})`; }
    else if (kind === 'pop') { if (L.length < 2) { i--; continue; } printed = L.pop(); line = `print(${th.name}.pop())`; }
    else if (kind === 'pop0') { if (L.length < 2) { i--; continue; } printed = L.shift(); line = `print(${th.name}.pop(0))`; }
    else if (kind === 'set') { const at = r.int(0, L.length - 1), x = fresh(); L[at] = x; line = `${th.name}[${at}] = ${lit(x)}`; }
    else if (kind === 'index') { const at = r.int(0, L.length - 1); printed = L[at]; line = `print(${th.name}[${at}])`; }
    else { printed = L.length; line = `print(len(${th.name}))`; }
    steps.push({ line, list: L.slice(), printed });
  }
  return { src: `${th.name} = [${init.map(lit).join(', ')}]\n${steps.map(s => s.line).join('\n')}`, steps, name: th.name };
}
function skLists(r, n) {
  const items = [], cells = [];
  r.sample(LISTS, n).forEach((th, k) => {
    const p = listProg(r, th);
    const rows = p.steps.map((s, i) => {
      items.push({ q: `Program ${k + 1} line ${i + 2}: ${s.line}`, a: pyShow(s.list), k: 'list', src: p.src, line: i + 2, name: p.name });
      if (s.printed != null) items.push({ q: `Program ${k + 1} line ${i + 2} prints: ${s.line}`, a: pyShow(s.printed), k: 'listprint', src: p.src, line: i + 2 });
      return [String(i + 2), blank(pyShow(s.list), 12), s.printed == null ? '<span class="cl-dash">nothing</span>' : blank(pyShow(s.printed), 3.4)];
    });
    cells.push(`<div class="cl-pair"><div><p><span class="ws-num">${k + 1}.</span></p>${codeBlock(p.src)}</div>${tbl(['Line', `${p.name} after the line`, 'Prints'], rows)}</div>`);
  });
  return {
    ican: 'I can trace list operations and write the list after each one.',
    directions: 'Start with the list on line 1. After each line, write the whole list, in order, with square brackets. If the line prints something, write that too. Positions (indexes) start at 0.',
    parts: [part('', example('<code>pets = ["cat", "dog"]</code>. <code>pets.append("fish")</code> adds to the end: <b>[\'cat\', \'dog\', \'fish\']</b>. <code>pets.insert(0, "owl")</code> puts owl at index 0 and slides the rest right. <code>pets.remove("dog")</code> takes out the first "dog". <code>pets.pop()</code> removes and gives back the last item; <code>pets.pop(0)</code> the first. <code>print(pets[1])</code> prints the item at index 1, the second one.')), part('List traces', cells.join(''))], items,
    materials: 'pencil', minutes: 25,
    mistakes: 'Counting positions from 1 instead of 0, and forgetting that insert slides the later items one place right instead of replacing one.',
    notes: 'Programs are real Python 3. Python shows a list of strings with single quotes, like [\'cat\', \'dog\']; accept either kind of quote.',
  };
}

/* grade 9: how many times does the marked line run? */
const STEPS = [
  r => { const n = r.int(3, 8); return { what: `checks every pair of ${n} sensors`, src: `readings = 0\nfor i in range(${n}):\n    for j in range(${n}):\n        readings = readings + 1`, mark: 4, count: n * n }; },
  r => { const n = r.int(5, 10); return { what: `compares each of ${n} readings with the ones before it`, src: `checks = 0\nfor i in range(${n}):\n    for j in range(i):\n        checks = checks + 1`, mark: 4, count: n * (n - 1) / 2 }; },
  r => { const n = r.int(20, 500); let x = 1, c = 0; while (x < n) { x *= 2; c++; } return { what: `doubles its wait time until it reaches ${n}`, src: `wait = 1\nwhile wait < ${n}:\n    wait = wait * 2`, mark: 3, count: c }; },
  r => { const n = r.int(20, 60), k = r.int(3, 7); return { what: `beeps every ${k} seconds for ${n} seconds`, src: `beeps = 0\nfor t in range(0, ${n}, ${k}):\n    beeps = beeps + 1`, mark: 3, count: Math.ceil(n / k) }; },
  r => { const n = r.int(15, 40), k = r.int(3, 6); return { what: `wakes up ${n} times and saves on every ${k}th wake-up`, src: `saves = 0\nfor i in range(${n}):\n    if i % ${k} == 0:\n        saves = saves + 1`, mark: 4, count: Math.floor((n - 1) / k) + 1 }; },
  r => { const items = r.sample([12, 7, 31, 18, 25, 4, 9, 40, 15, 22], 8), p = r.int(2, 7); return { what: `looks through 8 stored values for ${items[p]}`, src: `items = [${items.join(', ')}]\ni = 0\nwhile items[i] != ${items[p]}:\n    i = i + 1`, mark: 4, count: p }; },
  r => { const n = r.int(10, 40); return { what: `adds up ${n} readings`, src: `total = 0\nfor i in range(${n}):\n    total = total + i`, mark: 3, count: n }; },
];
function skSteps(r, n) {
  for (let t = 0; t < 60; t++) {
    const algs = r.sample(STEPS, n).map(f => f(r)), cs = algs.map(a => a.count), top = Math.max(...cs);
    if (cs.filter(c => c === top).length > 1 || new Set(cs).size < cs.length) continue;
    const L = 'ABCDEFG';
    const items = algs.map((a, i) => ({ q: `Algorithm ${L[i]}: ${a.src}`, a: String(a.count), k: 'steps', src: a.src, mark: a.mark }));
    const win = L[cs.indexOf(top)];
    items.push({ q: 'Most wasteful algorithm', a: win, k: 'waste', counts: cs });
    const cells = algs.map((a, i) => `<div class="cl-cell"><p><b>Algorithm ${L[i]}</b> ${esc(a.what)}.</p>${codeBlock(a.src, [a.mark])}<p>Line ${a.mark} runs ${blank(a.count, 3)} times.</p></div>`);
    return {
      ican: 'I can count how many times a line in a loop runs and compare the cost of algorithms.',
      directions: `Each algorithm runs on a battery-powered device, and every run of the shaded line uses a little battery. Count how many times the shaded line runs. Then decide which algorithm is the most wasteful.`,
      parts: [part('', example('<code>for i in range(3):</code> with <code>for j in range(4):</code> inside runs its inner line 3 × 4 = <b>12</b> times. <code>range(0, 10, 3)</code> gives 0, 3, 6, 9: <b>4</b> passes.')),
        part('Count the steps', `<div class="cl-cells cl-c2">${cells.join('')}</div>`),
        part('Compare', `<p>The most wasteful algorithm is ${blank(win, 2.6)}. Why? ${lines(2)}</p>${keyline(`Algorithm ${win}: its shaded line runs ${top} times, the most of the ${algs.length}.`)}`)], items,
      materials: 'pencil, scrap paper', minutes: 25,
      mistakes: 'Off-by-one counts: range(n) runs n times starting at 0, and a while loop stops the first time its test is false. For loops inside loops, multiply.',
      notes: 'Programs are real Python 3; adding a counter and a print is a quick way to check. The doubling loop is the logarithmic one: it stays small even for big limits, which is worth pointing out.',
    };
  }
}

/* grades 11-12: recursion and the call stack */
const RECUR = [
  r => { const k = r.int(3, 5); const calls = []; for (let i = k; i >= 1; i--) calls.push([`fact(${i})`, String([1, 1, 2, 6, 24, 120][i])]);
    return { src: `def fact(n):\n    if n <= 1:\n        return 1\n    return n * fact(n - 1)\n\nprint(fact(${k}))`, calls, out: [String([1, 1, 2, 6, 24, 120][k])], ret: true }; },
  r => { const k = r.int(3, 4); const calls = []; for (let i = k; i >= 0; i--) calls.push([`countdown(${i})`, i ? String(i) : 'Liftoff!']);
    return { src: `def countdown(n):\n    if n == 0:\n        print("Liftoff!")\n    else:\n        print(n)\n        countdown(n - 1)\n\ncountdown(${k})`, calls, out: calls.map(c => c[1]), ret: false }; },
  r => { const k = r.int(3, 5); const calls = []; for (let i = k; i >= 0; i--) calls.push([`sum_to(${i})`, String(i * (i + 1) / 2)]);
    return { src: `def sum_to(n):\n    if n == 0:\n        return 0\n    return n + sum_to(n - 1)\n\nprint(sum_to(${k}))`, calls, out: [String(k * (k + 1) / 2)], ret: true }; },
  r => { const b = r.int(2, 3), e = r.int(3, 4); const calls = []; for (let i = e; i >= 0; i--) calls.push([`power(${b}, ${i})`, String(b ** i)]);
    return { src: `def power(b, e):\n    if e == 0:\n        return 1\n    return b * power(b, e - 1)\n\nprint(power(${b}, ${e}))`, calls, out: [String(b ** e)], ret: true }; },
  r => { const x = r.int(102, 987); const calls = []; let y = x; while (y >= 10) { calls.push([`digit_sum(${y})`, null]); y = Math.floor(y / 10); } calls.push([`digit_sum(${y})`, null]);
    const ds = s => String(s).split('').reduce((a, c) => a + +c, 0); calls.forEach(c => { c[1] = String(ds(c[0].match(/\d+/)[0])); });
    return { src: `def digit_sum(n):\n    if n < 10:\n        return n\n    return n % 10 + digit_sum(n // 10)\n\nprint(digit_sum(${x}))`, calls, out: [String(ds(x))], ret: true }; },
];
function skRecur(r, n) {
  const items = [], cells = [];
  r.sample(RECUR, n).forEach((f, k) => {
    const p = f(r);
    const rows = p.calls.map((c, i) => {
      items.push({ q: `Procedure ${k + 1} call ${i + 1}: ${p.src}`, a: `${c[0]} ${p.ret ? 'returns' : 'prints'} ${c[1]}`, k: 'recur', src: p.src, i, call: c[0], val: c[1], ret: p.ret });
      return [String(i + 1), blank(c[0], 6), blank(c[1], 4)];
    });
    items.push({ q: `Procedure ${k + 1} output: ${p.src}`, a: p.out.join(' / '), k: 'output', src: p.src, out: p.out });
    cells.push(`<div class="cl-pair"><div><p><span class="ws-num">${k + 1}.</span></p>${codeBlock(p.src)}<p>Output: ${p.out.map(o => blank(o, Math.max(3, o.length * .7 + 1.4))).join(' ')}</p></div>${tbl(['Depth', 'Call on the stack', p.ret ? 'Returns' : 'Prints'], rows)}</div>`);
  });
  return {
    ican: 'I can trace a recursive procedure, drawing the call stack and the value each call returns.',
    directions: 'Trace each procedure. In the table, list every call in the order it is made: each new call sits on top of the stack, one row deeper. Then write what each call returns (or prints). Returns happen in reverse order, from the deepest call back up. Finish with the output.',
    parts: [part('', example('fact(3) calls fact(2), which calls fact(1). Stack, top to bottom: fact(3), fact(2), fact(1). fact(1) is the base case and returns 1; then fact(2) returns 2 × 1 = <b>2</b>; then fact(3) returns 3 × 2 = <b>6</b>.')), part('Recursion traces', cells.join(''))], items,
    materials: 'pencil', minutes: 30,
    mistakes: 'Returning from a call before the call it makes has finished, and stopping one call early: the base case is a call too and goes on the stack.',
    notes: 'Programs are real Python 3. The table lists calls top to bottom in the order they are pushed; the deepest row is the base case and returns first. Students who draw stacked boxes instead of a table are doing the same thing.',
  };
}

/* ---------- codes ---------- */
const SHAPES = {
  circle: '<circle cx="12" cy="12" r="9"/>', square: '<rect x="3" y="3" width="18" height="18"/>', triangle: '<polygon points="12,2 22,21 2,21"/>',
  star: '<polygon points="12,1.5 14.8,8.6 22.5,9 16.5,13.9 18.5,21.5 12,17.3 5.5,21.5 7.5,13.9 1.5,9 9.2,8.6"/>',
  heart: '<path d="M12 21 C3 14 1.5 9.5 3.5 6 C5.5 2.8 10 3.2 12 7 C14 3.2 18.5 2.8 20.5 6 C22.5 9.5 21 14 12 21 Z"/>',
  diamond: '<polygon points="12,1.5 22.5,12 12,22.5 1.5,12"/>', moon: '<path d="M15 2.5 A9.5 9.5 0 1 0 21.5 17 A8 8 0 1 1 15 2.5 Z"/>',
  plus: '<polygon points="9,2 15,2 15,9 22,9 22,15 15,15 15,22 9,22 9,15 2,15 2,9 9,9"/>', hexagon: '<polygon points="7,2.5 17,2.5 22,12 17,21.5 7,21.5 2,12"/>',
};
const shapeSvg = (k, full) => `<svg class="cl-shape" viewBox="0 0 24 24" role="img" aria-label="${k}"><g fill="${full ? '#222' : 'none'}" stroke="#222" stroke-width="2" stroke-linejoin="round">${SHAPES[k]}</g></svg>`;
const WORDS3 = ['CAT', 'DOG', 'SUN', 'HAT', 'PIG', 'BUS', 'CUP', 'BED', 'FOX', 'HEN', 'BEE', 'CAR', 'MAP', 'NET', 'PEN', 'POT', 'EGG', 'ANT', 'BAT', 'BUG', 'COW', 'OWL', 'JAR', 'RAT', 'TOP', 'CAN', 'FAN', 'VAN', 'BAG', 'LOG', 'WEB', 'BOX', 'TEN', 'NUT', 'HUT', 'MUG', 'TUB'];
const letterBoxes = (src, ans, cls = '') => `<span class="cl-msg ${cls}">${src.split(' ').map((w, wi) => `<span class="cl-word">${w.split('').map((c, i) => {
  const a = ans.split(' ')[wi][i];
  return `<span class="cl-lt"><b>${esc(c)}</b><span class="cl-lb"><span class="ws-ans">${esc(a)}</span></span></span>`;
}).join('')}</span>`).join('')}</span>`;

function skShapes(r, n) {
  for (let t = 0; t < 300; t++) {
    const words = [r.pick(WORDS3)];
    for (let k = 0; k < 400 && words.length < n; k++) {
      const w = r.pick(WORDS3), u = new Set((words.join('') + w).split(''));
      if (!words.includes(w) && u.size <= 6) words.push(w);
    }
    if (words.length < n) continue;
    const letters = [...new Set(words.join('').split(''))];
    while (letters.length < 6) { const c = r.pick(A26.split('')); if (!letters.includes(c)) letters.push(c); }
    const keyL = r.shuffle(letters), shapes = r.sample(Object.keys(SHAPES), 6), full = r.chance(.5);
    const S = Object.fromEntries(keyL.map((c, i) => [c, shapes[i]]));
    const legend = `<div class="cl-legend">${keyL.map(c => `<span class="cl-leg">${shapeSvg(S[c], full)}<b>${c}</b></span>`).join('')}</div>`;
    const items = words.map((w, i) => ({ q: `Word ${i + 1}: ${w.split('').map(c => S[c]).join(' ')}`, a: w, k: 'shapes', shapes: w.split('').map(c => S[c]), legend: keyL.map(c => [S[c], c]) }));
    const cells = words.map((w, i) => `<div class="cl-cell"><p><span class="ws-num">${i + 1}.</span></p><p class="cl-code-row">${w.split('').map(c => `<span class="cl-lt">${shapeSvg(S[c], full)}<span class="cl-lb"><span class="ws-ans">${c}</span></span></span>`).join('')}</p><div class="ws-draw" style="height:1in"><span>Draw it</span></div></div>`);
    return {
      ican: 'I can use a code key to turn shapes into letters.',
      directions: 'Each shape stands for a letter. Use the key. Write the letter under each shape. Read the word, then draw it.',
      parts: [part('Code key', legend), part('Secret words', `<div class="cl-cells cl-c2">${cells.join('')}</div>`)], items,
      materials: 'pencil, crayons', minutes: 20,
      mistakes: 'Mixing up shapes that look alike, like the diamond and the square. Point to the shape in the key before writing.',
      notes: 'Symbols standing for letters is how computers store text: every letter is kept as a code. Words are short, sound-out words with a picture to draw.',
    };
  }
}

/* pixel pictures: 8 by 8 */
const PICS = {
  cat: ['#......#', '##....##', '########', '#.####.#', '########', '###..###', '.######.', '..####..'],
  fish: ['........', '...###..', '#.#####.', '####.###', '#.######', '...###..', '........', '........'],
  rabbit: ['.#....#.', '.#....#.', '.##..##.', '.######.', '##.##.##', '########', '###..###', '.######.'],
  owl: ['#......#', '########', '#..##..#', '#..##..#', '###..###', '########', '.######.', '.#....#.'],
  frog: ['.##..##.', '#.#..#.#', '########', '########', '#......#', '.######.', '.#....#.', '........'],
  bird: ['........', '....###.', '...##.##', '#.#####.', '#######.', '.#####..', '..#.#...', '........'],
  turtle: ['........', '.####...', '######.#', '########', '######..', '.#..#...', '........', '........'],
};
const SHAPES8 = {
  heart: ['........', '.##..##.', '########', '########', '.######.', '..####..', '...##...', '........'],
  house: ['...##...', '..####..', '.######.', '########', '.##..##.', '.##..##.', '.######.', '........'],
  arrow: ['...#....', '...##...', '#######.', '########', '#######.', '...##...', '...#....', '........'],
  smile: ['..####..', '.#....#.', '#.#..#.#', '#......#', '#.#..#.#', '#..##..#', '.#....#.', '..####..'],
  tree: ['...##...', '..####..', '.######.', '..####..', '.######.', '########', '...##...', '...##...'],
  boat: ['...#....', '...##...', '...###..', '...#....', '########', '.######.', '..####..', '........'],
};
const flip = rows => rows.map(x => x.split('').reverse().join(''));
const runs = row => { const out = []; let c = '.', k = 0; for (const ch of row) { if (ch === c) k++; else { if (k) out.push([k, c]); c = ch; k = 1; } } out.push([k, c]); return out; };
const runText = row => runs(row).map(([k, c]) => `${k} ${c === '#' ? 'black' : 'white'}`).join(', ');
const runHtml = row => runs(row).map(([k, c]) => `${k}<span class="cl-sq${c === '#' ? ' on' : ''}"></span>`).join(' ');
const bits = row => row.replace(/#/g, '1').replace(/\./g, '0');
function pixGrid(rows, keyed, given) {
  return `<table class="cl-px">${rows.map(row => `<tr>${row.split('').map(c => `<td class="${given && c === '#' ? 'on' : ''}">${keyed && c === '#' ? '<span class="ws-ans cl-on"></span>' : ''}</td>`).join('')}</tr>`).join('')}</table>`;
}
function skPixel(r, n, g) {
  const bin = +g >= 3, items = [], parts = [];
  const nDec = bin ? (n === 3 ? 2 : 1) : n;
  const picks = r.sample(Object.keys(PICS), nDec);
  const dec = picks.map((nm, k) => {
    const rows = r.chance(.5) ? flip(PICS[nm]) : PICS[nm];
    rows.forEach((row, i) => items.push({ q: `Picture ${k + 1} row ${i + 1}: ${bin ? bits(row) : runText(row)}`, a: bits(row), k: bin ? 'pxbin' : 'pxrun', code: bin ? bits(row) : runText(row) }));
    items.push({ q: `Picture ${k + 1}: what animal`, a: nm, k: 'pxname', rows, name: nm });
    const codes = rows.map((row, i) => `<li>${bin ? `<code class="cl-bits">${bits(row)}</code>` : runHtml(row)}</li>`).join('');
    return `<div class="cl-pxwrap"><div><p><span class="ws-num">${k + 1}.</span> Row codes, top to bottom:</p><ol class="cl-rows">${codes}</ol></div><div>${pixGrid(rows, true)}<p>The hidden animal is a ${blank(nm, 5)}</p></div></div>`;
  });
  parts.push(part(bin ? 'Decode: 1 is black, 0 is white' : 'Decode the picture', dec.join('')));
  if (bin && n >= 2) {
    const nm = r.pick(Object.keys(SHAPES8)), rows = SHAPES8[nm];
    rows.forEach((row, i) => items.push({ q: `Encode ${nm} row ${i + 1}`, a: bits(row), k: 'pxenc', row }));
    parts.push(part('Encode: write the 1s and 0s', `<div class="cl-pxwrap"><div>${pixGrid(rows, false, true)}</div><ol class="cl-rows">${rows.map(row => `<li>${blank(bits(row), 7)}</li>`).join('')}</ol></div>`));
    parts.push(part('Your turn: make a picture for a partner', `<div class="cl-pxwrap"><div>${pixGrid(rows.map(() => '........'), false)}</div><ol class="cl-rows">${range(8).map(() => `<li><span class="cl-bitline"></span></li>`).join('')}</ol></div><p>Shade a simple picture, write its 8 rows of 1s and 0s, then fold the picture under and trade codes with a partner.</p>`));
  }
  return {
    ican: bin ? 'I can decode a picture stored as 1s and 0s and encode a picture as bits.' : 'I can follow a code to color a hidden picture.',
    directions: bin ? 'Each row of 8 digits is one row of the picture: 1 means shade the square black, 0 means leave it white. Shade the grid to find the picture. Then turn a picture into code.'
      : 'Each row code tells you how many squares to leave white and how many to color black, from left to right. Do one row at a time. Every row adds up to 8.',
    parts: [part('', example(bin ? '<code>00111100</code>: two white, four black, two white. The computer stores this row as 8 bits.'
      : `${runHtml('..####..')} means 2 white, 4 black, 2 white. Leave 2 squares, color 4, leave 2.`))].concat(parts), items,
    materials: 'pencil' + (bin ? '' : ', black crayon'), minutes: 20 + 5 * nDec,
    mistakes: bin ? 'Reading a row right to left, and losing your place: lay a ruler under the row you are on.' : 'Starting each row with black. Every code starts with the white squares, even when that number is 0.',
    notes: bin ? 'A black and white image is stored this way: one bit per pixel, 8 bits per row here. The partner picture has no key; the partner\'s decoded grid is the check.'
      : 'This is run-length encoding: instead of naming every square, the code says how many in a row are the same color. A row that starts with black begins with 0 white.',
  };
}

/* grade 2: a two-color bead code (5-bit binary, A = 1) */
const W4 = ['FROG', 'DUCK', 'BEAR', 'LION', 'FISH', 'BIRD', 'GOAT', 'DEER', 'WOLF', 'CRAB', 'SEAL', 'MOLE', 'SWAN', 'TOAD', 'LAMB', 'MULE'];
const W3A = ['CAT', 'DOG', 'PIG', 'COW', 'HEN', 'FOX', 'OWL', 'BAT', 'ANT', 'BEE', 'ELK', 'YAK', 'RAT', 'EMU', 'APE'];
const beadBits = c => (A26.indexOf(c) + 1).toString(2).padStart(5, '0');
const beads = (b, keyed) => `<span class="cl-beads">${b.split('').map(x => keyed ? `<span class="cl-bead">${x === '1' ? '<span class="ws-ans cl-dot"></span>' : ''}</span>` : `<span class="cl-bead${x === '1' ? ' on' : ''}"></span>`).join('')}</span>`;
function skBeads(r, n) {
  const nd = n, ne = n === 3 ? 2 : 1, items = [];
  const dw = r.sample(W4, nd), ew = r.sample(W3A, ne);
  const keyT = `<div class="cl-beadkey">${A26.split('').map(c => `<span><b>${c}</b>${beads(beadBits(c))}</span>`).join('')}</div>`;
  const dec = dw.map((w, i) => {
    items.push({ q: `Decode ${i + 1}: ${w.split('').map(beadBits).join(' ')}`, a: w, k: 'beaddec', code: w.split('').map(beadBits) });
    return `<div class="cl-q"><p><span class="ws-num">${i + 1}.</span></p><div class="cl-beadrow">${w.split('').map(c => `<span class="cl-lt">${beads(beadBits(c))}<span class="cl-lb"><span class="ws-ans">${c}</span></span></span>`).join('')}</div></div>`;
  });
  const enc = ew.map((w, i) => {
    w.split('').forEach((c, j) => items.push({ q: `Encode ${w} letter ${j + 1}`, a: beadBits(c).replace(/1/g, '●').replace(/0/g, '○'), k: 'beadenc', c }));
    return `<div class="cl-q"><p><span class="ws-num">${nd + i + 1}.</span> Write <b>${w}</b> in beads. Color the black beads.</p><div class="cl-beadrow">${w.split('').map(c => `<span class="cl-lt"><b>${c}</b>${beads(beadBits(c), true)}</span>`).join('')}</div></div>`;
  });
  return {
    ican: 'I can use a two-color code to read and write letters.',
    directions: 'Each letter is 5 beads, black or white. Find the bead pattern in the key to read each letter. To write a word, find each letter in the key and color its black beads.',
    parts: [part('Bead code key', keyT), part('Read the beads', dec.join('')), part('Write in beads', enc.join(''))], items,
    materials: 'pencil, black crayon', minutes: 20,
    mistakes: 'Reading the beads from right to left. Always read from the left, the way the key shows them.',
    notes: 'This is a binary code: black is 1 and white is 0, and the beads count up A = 1 (○○○○●), B = 2 (○○○●○), C = 3 (○○○●●). Five beads are enough for all 26 letters because 5 bits make 32 patterns.',
  };
}

/* ciphers */
const MSGS = ['MEET AT THE PARK', 'BRING A SNACK', 'THE KEY IS RED', 'LOOK UNDER THE MAT', 'CODE IS FUN', 'SAVE THE LAST COOKIE', 'RECESS AT NOON', 'THE BIRD SINGS',
  'PACK YOUR BOOTS', 'CALL ME LATER', 'THE GATE IS OPEN', 'WAIT BY THE TREE', 'BLUE TEAM WINS', 'READ PAGE TEN', 'LUNCH IS PIZZA', 'HIDE THE MAP', 'THE CAT IS ASLEEP',
  'PLANT THE SEEDS', 'FIND THE GOLD STAR', 'JUMP ON THREE', 'CLUB MEETS AT TWO', 'THE PASSWORD IS MOON', 'BRING YOUR KITE', 'MEET ME AT LUNCH', 'THE BUS LEAVES AT SIX',
  'THE BOX IS EMPTY', 'SWIM AFTER SCHOOL', 'DOGS LOVE BONES', 'TREASURE IS NEAR', 'OPEN THE BLUE DOOR', 'SNOW DAY TOMORROW', 'BAKE A CAKE'];
const shiftC = (s, k) => s.replace(/[A-Z]/g, c => A26[(A26.indexOf(c) + k + 26) % 26]);
const KEYWORDS = ['TIGER', 'PLANET', 'CASTLE', 'MONKEY', 'GARDEN', 'ROCKET', 'JUNGLE', 'WIZARD', 'DRAGON', 'PENCIL', 'FALCON', 'BRIDGE', 'CLOUDY', 'MARBLE', 'VOLCANO'];
const kwAlpha = kw => { const s = [...new Set(kw.split(''))]; return s.concat(A26.split('').filter(c => !s.includes(c))).join(''); };
const subst = (s, from, to) => s.replace(/[A-Z]/g, c => to[from.indexOf(c)]);
function skCipher(r, n, kind) {
  const caesar = kind === 'caesar', nE = Math.ceil(n / 2), nD = n - nE;
  const k = r.int(3, 9), kw = r.pick(KEYWORDS), alpha = caesar ? shiftC(A26, k) : kwAlpha(kw);
  const msgs = r.sample(MSGS, n), items = [];
  const strip = `<div class="cl-strip"><div class="cl-strip-row"><span class="cl-strip-h">Plain</span>${A26.split('').map(c => `<span>${c}</span>`).join('')}</div><div class="cl-strip-row"><span class="cl-strip-h">Cipher</span>${alpha.split('').map(c => `<span class="cl-lb"><span class="ws-ans">${c}</span></span>`).join('')}</div></div>`;
  A26.split('').forEach((c, i) => items.push({ q: `Key: ${c}`, a: alpha[i], k: caesar ? 'ckey' : 'kwkey', c, shift: k, kw }));
  const enc = msgs.slice(0, nE).map((m, i) => { const c = subst(m, A26, alpha); items.push({ q: `Encode: ${m}`, a: c, k: caesar ? 'cenc' : 'kwenc', m, shift: k, kw }); return `<div class="cl-q"><p><span class="ws-num">${i + 1}.</span></p>${letterBoxes(m, c)}</div>`; });
  const dec = msgs.slice(nE).map((m, i) => { const c = subst(m, A26, alpha); items.push({ q: `Decode: ${c}`, a: m, k: caesar ? 'cdec' : 'kwdec', c, shift: k, kw }); return `<div class="cl-q"><p><span class="ws-num">${nE + i + 1}.</span></p>${letterBoxes(c, m)}</div>`; });
  const explain = caesar
    ? ['How does a shift cipher protect <b>confidentiality</b> (keeping a message secret)? What could an attacker do to break it?', `Only someone who knows the key (shift ${k}) can read the message, so a stranger who sees it learns nothing at a glance. But there are only 25 possible shifts, so an attacker can try them all and break it quickly.`]
    : ['Compare the keyword cipher with a shift cipher. Which is harder to break by trying every key, and why? What weakness do both share?', 'A shift cipher has only 25 keys to try. A keyword cipher scrambles the alphabet in a way set by the keyword, so there are far more possible alphabets to try by hand. Both always swap a letter for the same letter, so common letters like E and T still show up most often, and an attacker can use letter counts to break either one.'];
  return {
    ican: caesar ? 'I can encode and decode messages with a shift cipher and explain what it protects.' : 'I can encode and decode messages with a keyword cipher and compare its strength to a shift cipher.',
    directions: caesar ? `This cipher shifts every letter ${k} places forward in the alphabet, wrapping from Z back to A. First fill in the cipher row of the key. Then encode (plain to cipher) and decode (cipher to plain), one letter at a time.`
      : `The keyword is <b>${kw}</b>. To build the cipher alphabet, write the keyword's letters (skip any repeats), then the rest of the alphabet in order, leaving out letters already used. Then encode (find the letter in the Plain row) and decode (find it in the Cipher row).`,
    parts: [part('', example(caesar ? 'Shift 3: A becomes D, B becomes E, and X wraps around to A. CAT becomes <b>FDW</b>. To decode, shift back 3.'
      : 'Keyword ZEBRA: the cipher alphabet starts Z E B R A, then C D F G H I J K L M N O P Q S T U V W X Y. So A becomes Z, B becomes E, and CAB becomes <b>BZE</b>.')),
      part('Build the key', strip), part(caesar ? 'Encode' : 'Encode with the keyword', enc.join('')), part('Decode', dec.join('')),
      part('Explain', `<p>${explain[0]}</p>${lines(3)}${keyline('Sample answer: ' + explain[1])}`)], items,
    materials: 'pencil', minutes: 30,
    mistakes: caesar ? 'Shifting the wrong way when decoding, and forgetting to wrap from Z back to A.' : 'Keeping a repeated keyword letter (each letter appears once in the alphabet), and decoding by looking up the cipher letter in the Plain row.',
    notes: caesar ? 'Spaces stay as they are, which makes short words easy to guess; that is a good thing to point out about weak ciphers.'
      : 'A keyword cipher is a substitution cipher. Letters near the end of the alphabet may map to themselves when the keyword does not use them; that is part of its weakness.',
  };
}

/* grade 5: digit-sum checksum */
function skChecksum(r, n) {
  const nR = n, nM = Math.ceil(n / 2), items = [];
  const msg = () => range(5).map(() => r.int(0, 9));
  const sum = d => d.reduce((a, b) => a + b, 0);
  const changed = new Set(r.sample(range(nR), r.int(2, Math.max(2, Math.floor(nR / 2)))));
  const rows = range(nR).map(i => {
    const d = msg(), c = sum(d) % 10, got = d.slice();
    let cs = c;
    if (changed.has(i)) { if (r.chance(.8)) { const j = r.int(0, 4); got[j] = (got[j] + r.int(1, 9)) % 10; } else cs = (c + r.int(1, 9)) % 10; }
    const s = sum(got), ok = s % 10 === cs;
    items.push({ q: `Message ${i + 1}, received ${got.join('')} check ${cs}: sum`, a: String(s), k: 'cksum', d: got.join('') },
      { q: `Message ${i + 1}, received ${got.join('')} check ${cs}: verdict`, a: ok ? 'OK' : 'changed', k: 'ckok', d: got.join(''), cs });
    return [`<code class="cl-bits">${got.join(' ')}</code>`, `<b>${cs}</b>`, blank(s, 2.6), blank(s % 10, 2), blank(ok ? 'OK' : 'changed', 5)];
  });
  const mk = range(nM).map(i => { const d = msg(); items.push({ q: `Make check digit ${i + 1} for ${d.join('')}`, a: String(sum(d) % 10), k: 'ckmake', d: d.join('') }); return `<li><code class="cl-bits">${d.join(' ')}</code> check digit: ${blank(sum(d) % 10, 2)}</li>`; });
  return {
    ican: 'I can use a checksum to find a message that was changed on the way.',
    directions: 'Each message is 5 digits plus a check digit. The sender adds the 5 digits and sends the last digit of the sum as the check digit. When a message arrives, add the 5 digits again. If the last digit of your sum matches the check digit, write OK. If not, the message was changed.',
    parts: [part('', example('Message 4 7 2 9 3: the sum is 25, so the check digit is <b>5</b>. If 4 7 2 <b>8</b> 3 arrives with check digit 5, the sum is 24, which ends in 4, not 5: the message was changed.')),
      part('Check the messages', tbl(['Message received', 'Check digit', 'Digit sum', 'Last digit', 'OK or changed?'], rows)),
      part('Send your own: add the check digit', fill(mk, 2, nR + 1))], items,
    materials: 'pencil', minutes: 20,
    mistakes: 'Adding the check digit into the sum, and comparing the whole sum (like 25) with the check digit instead of its last digit.',
    notes: 'A one-digit change always changes the last digit of the sum, so this checksum catches every single changed digit. It cannot catch two digits swapped (4 7 and 7 4 add the same), which is a good extension question; real codes like ISBNs use weighted sums for that. Some changed messages have a changed check digit instead of a changed message digit.',
  };
}

/* ---------- data and security ---------- */
const TYPEBANK = {
  Integer: ['42', '-7', '0', '2026', '15', '100', '-3', '8', '365'],
  Decimal: ['3.5', '-0.25', '98.6', '0.5', '2.0', '7.75', '1.99', '-4.1'],
  String: ['"hello"', '"42"', '"true"', '"3.14"', '"A"', '"blue sky"', '"007"', '"Maya"', '"-5"'],
  Boolean: ['true', 'false'],
};
const TYPES = ['Integer', 'Decimal', 'String', 'Boolean'];
function skTypes(r, n) {
  const nB = 2, rest = n - nB, nS = Math.ceil(rest * .36), nI = Math.ceil((rest - nS) / 2), nD = rest - nS - nI;
  const vals = r.shuffle([...r.sample(TYPEBANK.Integer, nI).map(v => [v, 'Integer']), ...r.sample(TYPEBANK.Decimal, nD).map(v => [v, 'Decimal']),
    ...r.sample(TYPEBANK.String, nS).map(v => [v, 'String']), ...TYPEBANK.Boolean.map(v => [v, 'Boolean'])]);
  const items = vals.map(([v, t], i) => ({ q: `Value ${i + 1}: ${v}`, a: t, k: 'type', v }));
  const list = `<ol class="cl-vals">${vals.map(([v]) => `<li><code>${esc(v)}</code></li>`).join('')}</ol>`;
  const sortT = `<div class="ws-sort" style="--cols:4">${TYPES.map(t => `<div class="ws-sort-col"><p class="ws-sort-head cl-sort-head">${t}</p><div class="ws-sort-drop"><span class="ws-ans">${vals.map(([, tt], i) => tt === t ? i + 1 : null).filter(x => x).join(', ')}</span></div></div>`).join('')}</div>`;
  const uses = { Integer: 'a score, the number of players, a year', Decimal: 'a price, a temperature, a height in meters', String: 'a name, a message, a password', Boolean: 'is the game over? is the light on?' };
  return {
    ican: 'I can sort values into data types and say what each type is used for.',
    directions: 'Write the number of each value in the column for its data type. Watch the quote marks: anything in quotes is a string, even if it looks like a number. Then write one use for each type.',
    parts: [part('', example('<code>12</code> is an integer (a whole number). <code>12.0</code> is a decimal, also called a float (it has a decimal point). <code>"12"</code> is a string (text, in quotes). <code>true</code> is a Boolean (only true or false).')),
      part('The values', list), part('Sort them', sortT),
      part('A use for each type', fill(TYPES.map(t => `${t}: <span class="cl-useline"></span>${key(` sample: ${uses[t]}`)}`)))], items,
    materials: 'pencil', minutes: 20,
    mistakes: 'Calling "42" an integer (the quotes make it text) and calling 2.0 an integer (the decimal point makes it a decimal). "true" in quotes is a string, not a Boolean.',
    notes: 'Booleans are written true and false here, as in JavaScript and many block languages; Python writes True and False. Decimals are called floats in most languages.',
  };
}

const RULES = [
  ['4 digits (0 to 9)', 10, 4], ['6 digits (0 to 9)', 10, 6], ['10 digits (0 to 9)', 10, 10], ['4 lowercase letters', 26, 4], ['5 lowercase letters', 26, 5], ['6 lowercase letters', 26, 6],
  ['8 lowercase letters', 26, 8], ['6 letters, uppercase or lowercase', 52, 6], ['6 letters or digits (upper, lower, 0 to 9)', 62, 6], ['8 letters or digits (upper, lower, 0 to 9)', 62, 8],
  ['3 words from a list of 1,000 words', 1000, 3], ['4 words from a list of 2,048 words', 2048, 4], ['8 characters from all 94 keyboard symbols', 94, 8], ['12 characters from all 94 keyboard symbols', 94, 12],
  ['5 words from a list of 7,776 words', 7776, 5],
];
const bitsOf = (N, L) => Math.round(L * Math.log2(N) * 10) / 10;
function skPasswords(r, n, g) {
  const ent = +g >= 9, L = 'ABCDEFGH';
  for (let t = 0; t < 200; t++) {
    const pool = ent ? RULES : RULES.filter(x => (BigInt(x[1]) ** BigInt(x[2])) < 10n ** 15n);
    const rules = r.sample(pool, n);
    const vals = rules.map(([, N, Ln]) => ent ? bitsOf(N, Ln) : BigInt(N) ** BigInt(Ln));
    const sorted = vals.slice().sort((a, b) => a < b ? -1 : a > b ? 1 : 0);
    if (sorted.some((x, i) => i && (ent ? x - sorted[i - 1] < 0.5 : x === sorted[i - 1]))) continue;
    const items = [];
    const rows = rules.map(([d, N, Ln], i) => {
      items.push({ q: `Rule ${L[i]}: ${d} choices`, a: big(N), k: 'pwN', N, d });
      if (ent) { items.push({ q: `Rule ${L[i]}: ${d} bits`, a: vals[i].toFixed(1), k: 'pwbits', N, Ln }); return [`<b>${L[i]}</b>`, esc(d), blank(big(N), 3.4), String(Ln), blank(vals[i].toFixed(1), 3.4)]; }
      items.push({ q: `Rule ${L[i]}: ${d} combinations`, a: big(vals[i]), k: 'pwcount', N, Ln }); return [`<b>${L[i]}</b>`, esc(d), blank(big(N), 3.4), String(Ln), blank(big(vals[i]), 11)];
    });
    const order = vals.map((v, i) => [v, L[i]]).sort((a, b) => a[0] < b[0] ? -1 : 1).map(x => x[1]);
    let last;
    if (ent) { items.push({ q: 'Weakest to strongest', a: order.join(', '), k: 'pwrank', vals: vals.map(Number) }); last = `<p>Weakest to strongest: ${blank(order.join(', '), 9)}</p>`; }
    else { items.push({ q: 'Hardest to guess', a: order[order.length - 1], k: 'pwtop', vals: vals.map(String) }); last = `<p>The rule that makes guessing hardest: ${blank(order[order.length - 1], 2.6)}. Why? ${lines(2)}</p>`; }
    return {
      ican: ent ? 'I can calculate password entropy in bits and rank password policies.' : 'I can count the possible passwords a rule allows and decide which rule is hardest to guess.',
      directions: ent ? 'For each policy, write how many symbols there are to choose from (N) and the length (L), then find the entropy: bits = L × log₂(N). Round to one decimal place. Then rank the policies.'
        : 'For each rule, write how many characters there are to choose from at each spot. Then multiply that number by itself once for each character in the password. Use a calculator for big numbers.',
      parts: [part('', example(ent ? '6 lowercase letters: N = 26, L = 6. bits = 6 × log₂(26) = 6 × 4.70 = <b>28.2</b>. Each extra bit doubles the number of guesses an attacker needs.'
        : 'A 3-digit lock: 10 choices for each digit, so 10 × 10 × 10 = <b>1,000</b> combinations. Two lowercase letters: 26 × 26 = <b>676</b>.')),
        part(ent ? 'Password policies' : 'Password rules', tbl(ent ? ['', 'Policy', 'Symbols N', 'Length L', 'Entropy (bits)'] : ['', 'Rule', 'Choices per spot', 'Length', 'Possible passwords'], rows)),
        part(ent ? 'Rank them' : 'Decide', last)], items,
      materials: 'pencil, calculator', minutes: 25,
      mistakes: ent ? 'Multiplying N by L instead of L by log₂(N), and forgetting that words from a list count as symbols: each word is one pick from the list.'
        : 'Adding instead of multiplying (6 letters is 26 × 26 × 26 × 26 × 26 × 26, not 26 × 6), and thinking a longer rule always wins: length and choices both matter.',
      notes: ent ? 'log₂(N) = log(N) ÷ log(2) on any calculator. Policies that use whole words count each word as one symbol from the list. Entropy here assumes every password is picked at random; people\'s own choices are much weaker.'
        : 'Numbers are exact. A computer can try billions of guesses a second, so the biggest of these can still fall quickly to a fast attacker; length helps most.',
    };
  }
}

/* grades 8-9: a hash rule */
const HWORDS = ['sunny', 'tiger', 'pizza', 'robot', 'apple', 'maple', 'river', 'cloud', 'piano', 'zebra', 'mango', 'otter', 'comet', 'jelly', 'koala', 'llama', 'pearl', 'ruby', 'kite', 'moose'];
const ANAG = [['lemon', 'melon'], ['stone', 'notes'], ['night', 'thing'], ['earth', 'heart'], ['listen', 'silent']];
const lv = c => A26.indexOf(c.toUpperCase()) + 1;
const hsum = w => w.split('').reduce((a, c, i) => a + (i + 1) * lv(c), 0);
function skHash(r, n) {
  const pair = r.pick(ANAG), words = r.shuffle(r.sample(HWORDS.filter(w => !pair.includes(w)), n - 2).concat(pair)), items = [];
  const rows = words.map(w => {
    const s = hsum(w), h = s % 100;
    items.push({ q: `${w}: weighted sum`, a: String(s), k: 'hsum', w }, { q: `${w}: hash`, a: String(h).padStart(2, '0'), k: 'hash', w });
    return [`<code>${w}</code>`, blank(w.split('').map(lv).join(' '), 7), blank(s, 3.4), blank(String(h).padStart(2, '0'), 2.6)];
  });
  const stored = r.pick(words.filter(w => !pair.includes(w))), sh = String(hsum(stored) % 100).padStart(2, '0');
  const tries = [stored, r.pick(HWORDS.filter(w => !words.includes(w) && String(hsum(w) % 100).padStart(2, '0') !== sh))];
  const login = r.shuffle(tries).map((w, i) => { const ok = w === stored; items.push({ q: `Login ${i + 1}: typed ${w}, stored ${sh}`, a: ok ? 'yes' : 'no', k: 'hlogin', w, sh }); return `<li>The server stores hash <b>${sh}</b>. Someone types <code>${w}</code>. Let in? ${blank(ok ? 'yes' : 'no', 3)}</li>`; });
  return {
    ican: 'I can hash passwords with a simple rule and explain why sites store hashes instead of passwords.',
    directions: 'Use the rule: give each letter its place in the alphabet (a = 1, b = 2, ... z = 26). Multiply each letter\'s value by its position in the word (1st × 1, 2nd × 2, ...). Add them up. The hash is the last two digits of the sum.',
    parts: [part('', example('cab: c = 3, a = 1, b = 2. Weighted sum = 3 × 1 + 1 × 2 + 2 × 3 = 11. Hash = <b>11</b>. bed: 2 × 1 + 5 × 2 + 4 × 3 = 24, hash <b>24</b>. A sum of 237 has hash 37.'),
      `<p class="cl-abc">${A26.split('').map((c, i) => `<span><b>${c.toLowerCase()}</b>${i + 1}</span>`).join('')}</p>`),
      part('Hash the passwords', tbl(['Password', 'Letter values', 'Weighted sum', 'Hash'], rows)),
      part('Log in', fill(login, 1, n + 1)),
      part('Explain', `<p>${pair[0]} and ${pair[1]} use the same letters. Why do they get different hashes? Why is it safer for a website to store the hash of your password instead of the password itself?</p>${lines(3)}${keyline('Sample answer: multiplying by position makes the order of the letters count, so rearranged letters give a different sum. If hackers steal the stored list they get only hashes; a hash cannot be turned back into the password, and the site can still check a login by hashing what was typed and comparing.')}`)], items,
    materials: 'pencil, calculator', minutes: 25,
    mistakes: 'Starting positions at 0 instead of 1, and keeping the first two digits of the sum instead of the last two.',
    notes: 'Real password hashes (like bcrypt or Argon2) are designed to be one-way and slow; this toy rule is easy to reverse and has many collisions with only 100 possible hashes, which is a good discussion point.',
  };
}

/* grades 10-12: a hash table with linear probing */
function skHashTable(r, n) {
  const sets = n === 3 ? [[8, 11], [10, 13]] : n === 1 ? [[7, 11]] : [[10, 13]];
  const items = [], blocks = [];
  sets.forEach(([nk, size], b) => {
    for (let t = 0; t < 400; t++) {
      const keys = r.sample(range(90).map(x => x + 10), nk), table = Array(size).fill(null), info = [];
      let coll = 0, far = 0;
      for (const k of keys) { let s = k % size, p = 0; while (table[s] !== null) { s = (s + 1) % size; p++; } table[s] = k; info.push([k, k % size, s]); if (p) coll++; far = Math.max(far, p); }
      if (coll < 3 || far < 2) continue;
      info.forEach(([k, h, s]) => items.push({ q: `Table ${b + 1}: insert ${k}`, a: `home ${h}, slot ${s}`, k: 'htab', key: k, keys, size }));
      blocks.push(`<div class="cl-q"><p><span class="ws-num">${b + 1}.</span> Table size ${size}, hash(key) = key mod ${size}. Insert in this order: <b>${keys.join(', ')}</b>.</p>
${tbl(['Key'].concat(keys.map(String)), [['Home slot'].concat(info.map(x => blank(x[1], 2))), ['Final slot'].concat(info.map(x => blank(x[2], 2)))], 'cl-tight')}
${tbl(['Slot'].concat(range(size).map(String)), [['Key'].concat(table.map(k => k == null ? '' : blank(k, 2)))], 'cl-tight')}</div>`);
      break;
    }
  });
  return {
    ican: 'I can insert keys into a hash table and resolve collisions with linear probing.',
    directions: 'For each key, find its home slot: key mod table size (the remainder after dividing). If that slot is empty, put the key there. If it is taken (a collision), try the next slot, then the next, wrapping from the last slot back to 0, until you find an empty one. Fill the table as you go.',
    parts: [part('', example('Size 7. Insert 15: 15 mod 7 = 1, slot 1 is empty, so 15 goes in slot 1. Insert 22: 22 mod 7 = 1, taken; try slot 2, empty: 22 goes in <b>slot 2</b>.')), part('Build the tables', blocks.join(''))], items,
    materials: 'pencil', minutes: 25,
    mistakes: 'Forgetting to wrap from the last slot to slot 0, and looking only at the home slot when a key moved there earlier was itself a collision.',
    notes: 'Every table has at least 3 collisions and at least one key that probes two or more slots, so clustering shows up. A good follow-up: how many slots does a search for an absent key check?',
  };
}

/* ---------- algorithms ---------- */
function sortPasses(a, alg) {
  const x = a.slice(), out = [];
  if (alg === 'selection') for (let i = 0; i < x.length - 1; i++) { let m = i; for (let j = i + 1; j < x.length; j++) if (x[j] < x[m]) m = j; [x[i], x[m]] = [x[m], x[i]]; out.push(x.slice()); }
  else if (alg === 'bubble') for (let i = 0; i < x.length - 1; i++) { for (let j = 0; j < x.length - 1 - i; j++) if (x[j] > x[j + 1]) [x[j], x[j + 1]] = [x[j + 1], x[j]]; out.push(x.slice()); }
  else for (let i = 1; i < x.length; i++) { const v = x[i]; let j = i - 1; while (j >= 0 && x[j] > v) { x[j + 1] = x[j]; j--; } x[j + 1] = v; out.push(x.slice()); }
  return out;
}
const ALGS = [['selection', 'Selection sort'], ['bubble', 'Bubble sort'], ['insertion', 'Insertion sort']];
function skSort(r, n, alg) {
  const items = [], blocks = [];
  const lists = r.distinct(n, () => { const a = r.sample(range(98).map(x => x + 1), 8), p = sortPasses(a, alg); return p.filter((row, i) => (i ? p[i - 1] : a).join() !== row.join()).length >= 4 ? a : null; }, a => a.join());
  lists.forEach((a, b) => {
    const p = sortPasses(a, alg);
    const rows = [['Start'].concat(a.map(String))].concat(p.map((row, i) => { items.push({ q: `List ${b + 1} (${a.join(' ')}) pass ${i + 1}`, a: row.join(' '), k: 'sort', list: a, pass: i, alg }); return [`Pass ${i + 1}`].concat(row.map(x => blank(x, 1.8))); }));
    blocks.push(`<div class="cl-q"><p><span class="ws-num">${b + 1}.</span> Cards: <b>${a.join(', ')}</b></p>${tbl(['', ...range(8).map(i => String(i + 1))], rows, 'cl-tight')}</div>`);
  });
  const how = { selection: 'Each pass finds the smallest card in the unsorted part and swaps it into the next place from the left. After pass 1 the smallest card is first; after pass 2 the two smallest are in place.',
    bubble: 'Each pass walks from left to right comparing neighbors and swaps any pair that is out of order. After pass 1 the largest card has bubbled to the end; each pass stops one place earlier.',
    insertion: 'Pass 1 takes the 2nd card and slides it left into place among the cards before it; pass 2 takes the 3rd card, and so on. The left part is always sorted.' }[alg];
  const ex = { selection: '<b>5 2 8 1</b>: pass 1 swaps 1 into the first place: 1 2 8 5. Pass 2: 2 is already smallest: 1 2 8 5. Pass 3 swaps 5 and 8: 1 2 5 8.',
    bubble: '<b>5 2 8 1</b>: pass 1 compares 5,2 (swap), 5,8 (keep), 8,1 (swap): 2 5 1 8. Pass 2: 2 1 5 8. Pass 3: 1 2 5 8.',
    insertion: '<b>5 2 8 1</b>: pass 1 slides 2 before 5: 2 5 8 1. Pass 2: 8 stays: 2 5 8 1. Pass 3 slides 1 to the front: 1 2 5 8.' }[alg];
  return {
    ican: `I can trace ${ALGS.find(x => x[0] === alg)[1].toLowerCase()} pass by pass.`,
    directions: `Sort each row of 8 cards from smallest to largest with ${ALGS.find(x => x[0] === alg)[1].toLowerCase()}. ${how} Write the whole list after every pass, even when a pass changes nothing.`,
    parts: [part('', example(ex)), part('Trace tables', blocks.join(''))], items,
    materials: 'pencil; number cards are a help', minutes: 25,
    mistakes: { selection: 'Swapping the first smaller card found instead of the smallest one in the rest of the list.', bubble: 'Doing only one swap per pass; a pass compares every neighboring pair once.', insertion: 'Swapping the new card with only its neighbor instead of sliding it all the way to its place.' }[alg],
    notes: `Every list takes 7 passes here (8 cards), and at least 4 of them change the order. Cutting out 8 numbered cards and sorting them by hand before writing makes the passes concrete.`,
  };
}

/* grade 10: stacks and queues (pseudocode) */
function skStack(r, n) {
  const items = [], blocks = [];
  for (let b = 0; b < n; b++) {
    const S = [], Q = [], rows = [], vals = r.shuffle(range(20).map(x => x + 1));
    let pushes = 0;
    for (let i = 0; i < 8; i++) {
      const opts = ['push', 'enq'].concat(S.length ? ['pop'] : [], Q.length ? ['deq'] : []);
      const kind = i < 2 ? (i ? 'enq' : 'push') : r.pick(opts);
      let op, ret = '';
      if (kind === 'push') { const v = vals[pushes++]; S.push(v); op = `S.push(${v})`; }
      else if (kind === 'enq') { const v = vals[pushes++]; Q.push(v); op = `Q.enqueue(${v})`; }
      else if (kind === 'pop') { ret = String(S.pop()); op = 'S.pop()'; }
      else { ret = String(Q.shift()); op = 'Q.dequeue()'; }
      const sv = '[' + S.join(', ') + ']', qv = '[' + Q.join(', ') + ']';
      items.push({ q: `Set ${b + 1} op ${i + 1}: ${op}`, a: `${ret || 'nothing'}; S ${sv}; Q ${qv}`, k: 'sq', ops: null, i, b });
      rows.push([String(i + 1), `<code>${op}</code>`, ret ? blank(ret, 2.4) : '<span class="cl-dash">nothing</span>', blank(sv, 6), blank(qv, 6)]);
    }
    const ops = rows.map(x => x[1].replace(/<\/?code>/g, ''));
    items.filter(it => it.b === b).forEach(it => { it.ops = ops; });
    blocks.push(`<div class="cl-q"><p><span class="ws-num">${b + 1}.</span> S is a stack and Q is a queue. Both start empty.</p>${tbl(['#', 'Operation', 'Returns', 'Stack S (bottom to top)', 'Queue Q (front to back)'], rows)}</div>`);
  }
  return {
    ican: 'I can trace stack and queue operations and show each structure after every step.',
    directions: 'Run the operations in order. After each one, write what it returns (pop and dequeue give back a value) and the contents of both structures. Write the stack from bottom to top and the queue from front to back.',
    parts: [part('', example('A <b>stack</b> is last in, first out: push puts a value on top, pop takes the top one off. A <b>queue</b> is first in, first out: enqueue joins at the back, dequeue leaves from the front.', 'S.push(4), S.push(9), S.pop() returns <b>9</b>. Q.enqueue(4), Q.enqueue(9), Q.dequeue() returns <b>4</b>.')), part('Trace the operations', blocks.join(''))], items,
    materials: 'pencil', minutes: 25,
    mistakes: 'Popping the bottom of the stack or dequeuing the back of the queue: the two structures take values out from opposite ends.',
    notes: 'The operations are pseudocode; in Python a list works as a stack (append and pop) and collections.deque as a queue (append and popleft). Values are never repeated in a set, so each one can be followed.',
  };
}

/* grade 10: public key encryption with small numbers */
const RSA = [[3, 11, 3, 7], [3, 7, 5, 5], [5, 7, 5, 5], [2, 11, 3, 7], [2, 17, 3, 11], [3, 17, 3, 11]];
const modpow = (b, e, m) => { let x = 1; for (let i = 0; i < e; i++) x = (x * b) % m; return x; };
function skRsa(r, n) {
  const [p, qq, e, d] = r.pick(RSA), N = p * qq, phi = (p - 1) * (qq - 1);
  const ms = r.sample(range(N - 3).map(x => x + 2).filter(m => modpow(m, e, N) !== m), 2 * n), items = [];
  items.push({ q: 'n = p × q', a: String(N), k: 'rsan', p, qq }, { q: 'phi', a: String(phi), k: 'rsaphi', p, qq }, { q: 'e × d mod phi', a: '1', k: 'rsaed', e, d, phi });
  const enc = ms.slice(0, n).map((m, i) => { const c = modpow(m, e, N); items.push({ q: `Encrypt ${m}`, a: String(c), k: 'rsaenc', m, e, N }); return `<li>Encrypt m = <b>${m}</b>: c = ${m}<sup>${e}</sup> mod ${N} = ${blank(c, 2.6)}</li>`; });
  const dec = ms.slice(n).map((m, i) => { const c = modpow(m, e, N); items.push({ q: `Decrypt ${c}`, a: String(m), k: 'rsadec', c, d, N }); return `<li>Decrypt c = <b>${c}</b>: m = ${c}<sup>${d}</sup> mod ${N} = ${blank(m, 2.6)}</li>`; });
  return {
    ican: 'I can encrypt and decrypt with small-number public key math and explain why it works.',
    directions: `Use the keys below. To encrypt a number m, compute m<sup>e</sup> mod n. To decrypt a number c, compute c<sup>d</sup> mod n. "mod n" means the remainder after dividing by n. Keep the numbers small: multiply one step at a time and take the remainder after every step.`,
    parts: [part('', example('Keys n = 15, e = 3, d = 3. Encrypt 7: 7 × 7 = 49, 49 mod 15 = 4; 4 × 7 = 28, 28 mod 15 = <b>13</b>. Decrypt 13: 13 × 13 = 169 mod 15 = 4; 4 × 13 = 52 mod 15 = <b>7</b>. The message comes back.')),
      part('The keys', `<p>Secret primes p = <b>${p}</b>, q = <b>${qq}</b>. Public key: n = p × q = ${blank(N, 2.6)}, e = <b>${e}</b>. Private key: d = <b>${d}</b>.</p><p>Check the keys: φ = (p − 1)(q − 1) = ${blank(phi, 2.6)}, and e × d = ${e * d}, which leaves remainder ${blank(1, 2)} when divided by φ.</p>`),
      part('Encrypt with the public key', fill(enc)), part('Decrypt with the private key', fill(dec, 1, n + 1)),
      part('Explain', `<p>Anyone can know n and e. Why can only the person with d read the messages, and why does choosing e × d to leave remainder 1 when divided by φ make decrypting undo encrypting?</p>${lines(3)}${keyline(`Sample answer: decrypting computes (m<sup>e</sup>)<sup>d</sup> = m<sup>e × d</sup> mod n. Because e × d is 1 more than a multiple of φ, and raising to the power φ gives 1 mod n (Euler's theorem), m<sup>e × d</sup> comes back to m. Finding d needs φ, and finding φ needs the primes p and q. With real keys, n has hundreds of digits and nobody knows a fast way to factor it, so d stays secret.`)}`)], items,
    materials: 'pencil, calculator', minutes: 30,
    mistakes: 'Working out the whole power first (the numbers get huge) instead of taking the remainder after each multiplication, and using e to decrypt.',
    notes: 'This is RSA with tiny primes, so it can be broken by hand; real keys use primes hundreds of digits long. Messages that encrypt to themselves are left out so every answer changes.',
  };
}

/* grade 12: Dijkstra's shortest paths */
const NODES = { A: [60, 150], B: [200, 50], C: [200, 250], D: [360, 50], E: [360, 250], F: [500, 150] };
const EDGES = [['A', 'B'], ['A', 'C'], ['B', 'C'], ['B', 'D'], ['C', 'E'], ['D', 'E'], ['D', 'F'], ['E', 'F'], ['B', 'E'], ['C', 'D']];
function dijkstra(nodes, adj, src) {
  const dist = Object.fromEntries(nodes.map(x => [x, Infinity])), prev = {}, done = [], rows = [];
  dist[src] = 0;
  while (done.length < nodes.length) {
    const u = nodes.filter(x => !done.includes(x)).sort((a, b) => dist[a] - dist[b])[0];
    done.push(u);
    for (const [v, w] of adj[u]) if (!done.includes(v) && dist[u] + w < dist[v]) { dist[v] = dist[u] + w; prev[v] = u; }
    rows.push({ u, d: { ...dist } });
  }
  return { dist, prev, rows };
}
function skDijkstra(r, n) {
  const nodes = Object.keys(NODES), maps = n === 3 ? 2 : 1, steps = n >= 2, items = [], blocks = [];
  for (let b = 0; b < maps; b++) for (let t = 0; t < 500; t++) {
    const diag = r.pick([8, 9]), edges = EDGES.slice(0, 8).filter(() => r.chance(.85)).concat([EDGES[diag]]).map(([a, c]) => [a, c, r.int(1, 9)]);
    const adj = Object.fromEntries(nodes.map(x => [x, []]));
    edges.forEach(([a, c, w]) => { adj[a].push([c, w]); adj[c].push([a, w]); });
    const res = dijkstra(nodes, adj, 'A');
    if (nodes.some(x => res.dist[x] === Infinity)) continue;
    const ds = nodes.map(x => res.dist[x]);
    if (new Set(ds).size < 6) continue;
    // unique shortest paths: no node has two best predecessors
    if (nodes.some(v => v !== 'A' && adj[v].filter(([u, w]) => res.dist[u] + w === res.dist[v]).length !== 1)) continue;
    if (nodes.filter(v => res.prev[v] && res.prev[v] !== 'A').length < 3) continue;   // most routes go through other places
    const pathTo = v => { const p = [v]; while (p[0] !== 'A') p.unshift(res.prev[p[0]]); return p.join(' → '); };
    let svg = '';
    edges.forEach(([a, c, w]) => { const [x1, y1] = NODES[a], [x2, y2] = NODES[c], mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
      svg += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#333" stroke-width="2"/><circle cx="${mx}" cy="${my}" r="11" fill="#fff" stroke="#333"/><text x="${mx}" y="${my + 4.5}" ${FONT} font-size="13" font-weight="700" text-anchor="middle">${w}</text>`; });
    nodes.forEach(x => { const [cx, cy] = NODES[x]; svg += `<circle cx="${cx}" cy="${cy}" r="17" fill="#fff" stroke="#222" stroke-width="2.5"/><text x="${cx}" y="${cy + 5.5}" ${FONT} font-size="16" font-weight="700" text-anchor="middle">${x}</text>`; });
    const graph = `<svg class="gen-svg" viewBox="30 20 500 260" role="img" aria-label="A map of 6 places, A to F, joined by roads with travel times" style="max-width:3.1in">${svg}</svg>`;
    const fin = nodes.slice(1).map(v => { items.push({ q: `Map ${b + 1}: shortest A to ${v}`, a: `${res.dist[v]} via ${pathTo(v)}`, k: 'dij', v, edges }); return [v, blank(res.dist[v], 2.6), blank(pathTo(v), 7)]; });
    let stepT = '';
    if (steps) {
      const show = x => x === Infinity ? '∞' : String(x);
      const rows = res.rows.map((row, i) => { items.push({ q: `Map ${b + 1}: step ${i + 1}`, a: `visit ${row.u}; ${nodes.map(x => show(row.d[x])).join(' ')}`, k: 'dijstep', i, edges }); return [String(i + 1), blank(row.u, 2)].concat(nodes.map(x => blank(show(row.d[x]), 2))); });
      stepT = `<p class="ws-sub">Distance table: after visiting each place, update its neighbors.</p>${tbl(['Step', 'Visit', ...nodes], [['Start', '', '0', '∞', '∞', '∞', '∞', '∞']].concat(rows), 'cl-tight')}`;
    }
    blocks.push(`<div class="cl-q"><p><span class="ws-num">${b + 1}.</span> Travel times in minutes. Start at A.</p><div class="cl-pair cl-dij">${graph}<div><p class="ws-sub">Shortest routes from A</p>${tbl(['To', 'Time', 'Route'], fin)}</div></div>${stepT}</div>`);
    break;
  }
  return {
    ican: 'I can use Dijkstra\'s algorithm to find shortest paths on a weighted map.',
    directions: 'Use Dijkstra\'s algorithm from A. Each step, visit the unvisited place with the smallest known distance. For each of its neighbors, add the road\'s time to the distance of the place you are visiting; if that beats the neighbor\'s current distance, write the smaller number. Distances of visited places never change. ∞ means no route found yet.',
    parts: [part('', example('A is visited first with distance 0. If the road from A to B takes 4 and the road from A to C takes 7, then B = 4 and C = 7. B is visited next (4 is smallest). If the road from B to C takes 2, then 4 + 2 = 6 beats 7, so C becomes <b>6</b>, by way of B.')), part('Shortest paths', blocks.join(''))], items,
    materials: 'pencil', minutes: 35,
    mistakes: 'Visiting places in alphabetical order instead of by smallest distance, and replacing a distance with a larger one.',
    notes: 'Every map has one shortest route to each place and no two places tie in distance, so the visit order and the table are the same for everyone.',
  };
}

/* grade 12: making change with dynamic programming */
const COINS = [[1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 4, 6], [1, 5, 7], [1, 6, 9], [1, 7, 10]];
function changeTable(coins, N) {
  const best = [0], use = [null];
  for (let a = 1; a <= N; a++) { let b = Infinity, u = null; for (const c of coins) if (c <= a && best[a - c] + 1 < b) { b = best[a - c] + 1; u = c; } best.push(b); use.push(u); }
  return { best, use };
}
function skChange(r, n) {
  const N = [12, 20, 25][n - 1], nq = [4, 6, 8][n - 1];
  const coins = r.pick(COINS), { best, use } = changeTable(coins, N), items = [];
  const combo = a => { const out = []; while (a > 0) { out.push(use[a]); a -= use[a]; } return out.sort((x, y) => y - x); };
  const greedy = a => { let k = 0; for (const c of coins.slice().sort((x, y) => y - x)) { k += Math.floor(a / c); a %= c; } return k; };
  const amounts = range(N + 1);
  amounts.slice(1).forEach(a => items.push({ q: `Fewest coins for ${a}`, a: String(best[a]), k: 'chg', amt: a, coins }));
  const half = Math.ceil((N + 1) / 2);
  const tableH = [amounts.slice(0, half), amounts.slice(half)].map(part2 => tbl(['Amount', ...part2.map(String)], [['Fewest coins', ...part2.map(a => a === 0 ? '0' : blank(best[a], 1.6))]], 'cl-tight')).join('');
  const qs = r.sample(amounts.filter(a => a >= coins[1] + 1), nq).sort((x, y) => x - y);
  const qrows = qs.map(a => { const c = combo(a); items.push({ q: `Coins for ${a}`, a: c.join(' + '), k: 'chgcombo', amt: a, coins, n: best[a] }); return `<li>Amount ${a}: ${best[a] === 1 ? 'coin' : 'coins'} used ${blank(c.join(' + '), 6)}</li>`; });
  const fail = amounts.find(a => a > 0 && greedy(a) > best[a]);
  items.push({ q: 'Smallest amount where greedy fails', a: String(fail), k: 'chgfail', coins });
  return {
    ican: 'I can fill a dynamic programming table to find the fewest coins for an amount.',
    directions: `Coins come in values ${coins.join(', ')}. Fill the table from left to right. For each amount, try every coin that fits: take 1 coin, plus the fewest coins already found for what is left. Write the smallest result. Then use the table to list the coins for some amounts.`,
    parts: [part('', example('Coins 1, 3, 4. Amount 6: use a 1 (1 + fewest for 5 = 1 + 2 = 3), a 3 (1 + fewest for 3 = 1 + 1 = 2) or a 4 (1 + fewest for 2 = 1 + 2 = 3). The smallest is <b>2</b> (3 + 3).')),
      part('The table', tableH), part('Which coins?', fill(qrows, 2)),
      part('Greedy check', `<p>The greedy method always takes the biggest coin that fits. What is the smallest amount where greedy uses more coins than the table says? ${blank(fail, 2.6)}</p>`)], items,
    materials: 'pencil', minutes: 30,
    mistakes: 'Taking the biggest coin first, which is the greedy method and is not always best here, and forgetting the + 1 for the coin just used.',
    notes: `Every coin set includes 1, so every amount can be made. Some amounts can be made with the fewest coins in more than one way; the key shows one, and any combination with the right number of coins is correct. Greedy first fails at ${fail} for this coin set.`,
  };
}

/* ---------- the settings ---------- */
const GRADES = [['k', 'Kindergarten'], ['1', 'Grade 1'], ['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'], ['6', 'Grade 6'], ['7', 'Grade 7'],
  ['8', 'Grade 8'], ['9', 'Grade 9'], ['10', 'Grade 10'], ['11', 'Grade 11'], ['12', 'Grade 12']];
const NAMES = {
  follow: 'Follow the arrows to an animal', hop: 'Hop along a number track', maze: 'Mazes: draw the arrow program', collect: 'Obstacle course: collect 3 stars',
  debug: 'Bug hunt: fix the wrong arrow', loops: 'Loop the path: repeat blocks', predict: 'Predict the program: loops and events', ifgrid: 'If-then robot on colored squares',
  boxes: 'Named boxes: follow a story', score: 'Score tracker: trace a variable', start: 'What was the starting value?', output: 'Predict the output',
  trace: 'Trace table: two variables', looptrace: 'Loop trace: counter and running total', memory: 'Be the computer: memory boxes', types: 'Data type sort',
  passwords: 'Password math: count the combinations', caesar: 'Caesar (shift) cipher', keyword: 'Keyword cipher', checksum: 'Digit-sum checksum', shapes: 'Secret shape code',
  pixel: 'Pixel picture from row codes', beads: 'Two-color bead code (binary)', lists: 'Lists: append, remove and index', scope: 'Scope detective: local and global',
  hash: 'Hashing passwords by hand', hashtab: 'Hash table with linear probing', sort: 'Sorting passes', steps: 'Count the steps: loop cost', stack: 'Stacks and queues',
  rsa: 'Public key math with small numbers', recur: 'Recursion and the call stack', dijkstra: 'Shortest paths: Dijkstra\'s algorithm', change: 'Making change: dynamic programming',
};
const BYGRADE = {
  k: ['follow', 'hop', 'maze'], 1: ['hop', 'debug', 'collect', 'boxes', 'shapes', 'pixel'], 2: ['loops', 'predict', 'boxes', 'beads', 'debug', 'pixel', 'shapes'],
  3: ['ifgrid', 'output', 'score', 'start', 'loops', 'beads'], 4: ['trace', 'looptrace', 'ifgrid', 'start'], 5: ['caesar', 'checksum', 'looptrace', 'output'],
  6: ['memory', 'types', 'passwords', 'output', 'caesar', 'checksum', 'pixel'], 7: ['lists', 'keyword', 'types', 'output', 'caesar', 'pixel'],
  8: ['scope', 'hash', 'pixel', 'output', 'lists', 'keyword', 'passwords'], 9: ['sort', 'passwords', 'steps', 'keyword', 'output', 'hash'],
  10: ['stack', 'rsa', 'sort', 'steps', 'passwords', 'hashtab'], 11: ['recur', 'hashtab', 'sort', 'stack', 'rsa'], 12: ['dijkstra', 'change', 'recur', 'hashtab', 'sort'],
};
const label = (s, g) => s === 'hop' ? (g === 'k' ? 'Bunny hops: which carrot?' : 'Frog hops: which lily pad?')
  : s === 'boxes' ? (g === '1' ? 'A named box: follow a story' : 'Two named boxes: a sale story')
  : s === 'output' ? (g === '3' ? 'Loops plus choices: what does it say?' : 'Predict the output (Python)')
  : s === 'passwords' && +g >= 9 ? 'Password entropy in bits'
  : s === 'pixel' && +g >= 3 ? 'Binary pixel pictures (1s and 0s)' : NAMES[s];
// [s, m, l] counts and the noun for the Length labels
const SIZES = {
  follow: [[4, 6, 8], 'programs'], maze: [[2, 3, 4], 'mazes'], collect: [[1, 2, 4], 'courses'], debug: [[3, 5, 6], 'programs'], loops: [[2, 4, 6], 'paths'],
  predict: [[3, 5, 6], 'programs'], ifgrid: [[2, 4, 6], 'runs'], boxes: [[1, 2, 3], 'stories'], score: [[1, 2, 3], 'programs'], start: [[4, 6, 8], 'puzzles'],
  trace: [[1, 2, 3], 'programs'], looptrace: [[1, 2, 3], 'loops'], memory: [[2, 3, 4], 'programs'], types: [[10, 15, 20], 'values'], caesar: [[3, 5, 7], 'messages'],
  keyword: [[2, 4, 6], 'messages'], checksum: [[4, 6, 8], 'messages'], shapes: [[2, 4, 6], 'words'], beads: [[1, 2, 3], 'words to read'], lists: [[1, 2, 3], 'programs'],
  scope: [[3, 4, 6], 'programs'], hash: [[4, 6, 8], 'passwords'], sort: [[1, 2, 3], 'lists'], steps: [[3, 4, 5], 'algorithms'], stack: [[1, 2, 3], 'sets of 8 operations'],
  rsa: [[2, 3, 4], 'numbers each way'], recur: [[2, 4, 5], 'procedures'],
};
function countOpts(v) {
  const s = v.skill, g = v.grade;
  if (s === 'hop') return g === 'k' ? [['s', 'Fewer (3 programs)'], ['m', 'Standard (5)'], ['l', 'More (6)']] : [['s', 'Fewer (4 programs)'], ['m', 'Standard (5)'], ['l', 'More (8)']];
  if (s === 'output') return g === '3' ? [['s', 'Fewer (2 programs)'], ['m', 'Standard (4)'], ['l', 'More (5)']] : [['s', 'Fewer (3 programs)'], ['m', 'Standard (4)'], ['l', 'More (6)']];
  if (s === 'passwords') return +g >= 9 ? [['s', 'Fewer (4 policies)'], ['m', 'Standard (6)'], ['l', 'More (8)']] : [['s', 'Fewer (3 rules)'], ['m', 'Standard (5)'], ['l', 'More (7)']];
  if (s === 'pixel') return +g >= 3 ? [['s', 'Decode one picture'], ['m', 'Decode, encode and make your own'], ['l', 'Two to decode, encode and make your own']]
    : [['s', 'One picture'], ['m', 'Two pictures'], ['l', 'Three pictures']];
  if (s === 'hashtab') return [['s', '7 keys, table of 11'], ['m', '10 keys, table of 13'], ['l', 'Two tables (8 and 10 keys)']];
  if (s === 'dijkstra') return [['s', 'One map, final routes only'], ['m', 'One map with the distance table'], ['l', 'Two maps with distance tables']];
  if (s === 'change') return [['s', 'Amounts to 12, 4 questions'], ['m', 'Amounts to 20, 6 questions'], ['l', 'Amounts to 25, 8 questions']];
  const [c, noun] = SIZES[s];
  return [['s', `Fewer (${c[0]} ${noun})`], ['m', `Standard (${c[1]})`], ['l', `More (${c[2]})`]];
}
const countOf = v => { const s = v.skill, i = 'sml'.indexOf(v.count);
  if (s === 'hop') return (v.grade === 'k' ? [3, 5, 6] : [4, 5, 8])[i];
  if (s === 'output') return (v.grade === '3' ? [2, 4, 5] : [3, 4, 6])[i];
  if (s === 'passwords') return (+v.grade >= 9 ? [4, 6, 8] : [3, 5, 7])[i];
  if (['pixel', 'hashtab', 'dijkstra', 'change'].includes(s)) return i + 1;
  return SIZES[s][0][i]; };

function build(v, r) {
  const g = v.grade, n = countOf(v);
  switch (v.skill) {
    case 'follow': return skFollow(r, n); case 'hop': return skHop(r, n, g); case 'maze': return skMaze(r, n); case 'collect': return skCollect(r, n);
    case 'debug': return skDebug(r, n); case 'loops': return skLoops(r, n); case 'predict': return skPredict(r, n); case 'ifgrid': return skIfGrid(r, n);
    case 'boxes': return skBoxes(r, n, g); case 'score': return skScore(r, n); case 'start': return skStart(r, n); case 'output': return skOutput(r, n, g);
    case 'scope': return skOutput(r, n, 'scope'); case 'trace': return skTrace(r, n); case 'looptrace': return skLoopTrace(r, n, g); case 'memory': return skMemory(r, n);
    case 'lists': return skLists(r, n); case 'steps': return skSteps(r, n); case 'recur': return skRecur(r, n); case 'shapes': return skShapes(r, n);
    case 'pixel': return skPixel(r, n, g); case 'beads': return skBeads(r, n); case 'caesar': return skCipher(r, n, 'caesar'); case 'keyword': return skCipher(r, n, 'keyword');
    case 'checksum': return skChecksum(r, n); case 'types': return skTypes(r, n); case 'passwords': return skPasswords(r, n, g); case 'hash': return skHash(r, n);
    case 'hashtab': return skHashTable(r, n); case 'sort': return skSort(r, n, v.alg); case 'stack': return skStack(r, n); case 'rsa': return skRsa(r, n);
    case 'dijkstra': return skDijkstra(r, n); case 'change': return skChange(r, n);
  }
}

/* ---------- verify: re-work every item another way ---------- */
const VEC = { '↑': [0, -1], '↓': [0, 1], '←': [-1, 0], '→': [1, 0] };
const SYM = { U: '↑', D: '↓', L: '←', R: '→' };
function flood(W, H, blocked, s) {   // distances by repeated relaxation, not a queue
  const d = {}; d[s.join()] = 0;
  for (let changed = true; changed;) {
    changed = false;
    for (let x = 0; x < W; x++) for (let y = 0; y < H; y++) {
      const k = x + ',' + y; if (blocked.includes(k)) continue;
      for (const [dx, dy] of Object.values(VEC)) { const nk = (x + dx) + ',' + (y + dy); if (d[nk] != null && (d[k] == null || d[nk] + 1 < d[k])) { d[k] = d[nk] + 1; changed = true; } }
    }
  }
  return d;
}
const perms = a => a.length <= 1 ? [a] : a.flatMap((x, i) => perms(a.filter((_, j) => j !== i)).map(p => [x, ...p]));
function verifyItem(it, all) {
  const P = [];
  const want = (w, what = '') => { if (String(w) !== String(it.a)) P.push(`${it.q.slice(0, 70)}${what}: key says ${it.a}, should be ${w}`); };
  const run = src => pyRun(src);
  switch (it.k) {
    case 'follow': {
      let [x, y] = it.start; const hits = [];
      for (const d of it.prog) { x += VEC[SYM[d]][0]; y += VEC[SYM[d]][1]; const s = it.spots.find(p => p[0] === x && p[1] === y); hits.push(s ? s[2] : null); if (x < 0 || y < 0 || x >= it.W || y >= it.H) P.push(`${it.q}: leaves the grid`); }
      if (hits.slice(0, -1).some(h => h)) P.push(`${it.q}: passes over an animal`);
      want(hits[hits.length - 1]); break;
    }
    case 'hop': {
      let at = it.start; for (const d of it.prog) { at += d === 'R' ? 1 : -1; if (at < 0 || at > it.top) P.push(`${it.q}: off the track`); }
      want(at); break;
    }
    case 'maze': case 'collect': {
      const blocked = it.k === 'maze' ? it.walls : it.walls.concat(it.puddles), prog = it.a.split(' ');
      let [x, y] = it.s; const got = new Set();
      for (const c of prog) {
        if (c === '★') { const i = (it.stars || []).findIndex(s => s[0] === x && s[1] === y); if (i < 0) P.push(`${it.q}: pick-up off a star`); got.add(i); continue; }
        x += VEC[c][0]; y += VEC[c][1];
        if (x < 0 || y < 0 || x >= it.W || y >= it.H || blocked.includes(x + ',' + y)) P.push(`${it.q}: hits a wall or leaves the grid`);
      }
      if (it.k === 'maze') {
        if (x !== it.goal[0] || y !== it.goal[1]) P.push(`${it.q}: does not reach the apple`);
        const d = flood(it.W, it.H, blocked, it.s); if (d[it.goal.join()] !== prog.length) P.push(`${it.q}: not a shortest way`);
      } else {
        if (got.size !== 3 || got.has(-1)) P.push(`${it.q}: does not collect 3 stars`);
        const pts = [it.s, ...it.stars], dist = pts.map(p => flood(it.W, it.H, blocked, p));
        const best = Math.min(...perms([1, 2, 3]).map(o => [0, ...o].slice(1).reduce((a, j, i) => a + dist[[0, ...o][i]][pts[j].join()], 0))) + 3;
        if (best !== prog.length) P.push(`${it.q}: ${prog.length} cards, shortest is ${best}`);
      }
      break;
    }
    case 'debug': {
      const end = p => { let [x, y] = it.s, ok = true; for (const d of p) { x += VEC[SYM[d]][0]; y += VEC[SYM[d]][1]; if (x < 0 || y < 0 || x >= it.W || y >= it.H) ok = false; } return ok && x === it.goal[0] && y === it.goal[1]; };
      if (end(it.buggy)) P.push(`${it.q}: the buggy program works`);
      let fixes = [];
      it.buggy.forEach((d, j) => ['U', 'D', 'L', 'R'].forEach(e => { if (e !== d) { const f = it.buggy.slice(); f[j] = e; if (end(f)) fixes.push(`Step ${j + 1}: ${SYM[e]}`); } }));
      if (fixes.length !== 1) P.push(`${it.q}: ${fixes.length} fixes`); else want(fixes[0]);
      break;
    }
    case 'loopprog': {   // expand the written loop program and walk it
      const moves = it.a.split(', then ').flatMap(seg => { const m = seg.match(/^repeat (\d+): (.*)$/); const body = (m ? m[2] : seg).split(' '); return Array(m ? +m[1] : 1).fill(body).flat(); });
      let [x, y] = it.s; const path = [[x, y]];
      for (const c of moves) { x += VEC[c][0]; y += VEC[c][1]; path.push([x, y]); }
      if (JSON.stringify(path) !== JSON.stringify(it.path)) P.push(`${it.q}: the loop program does not follow the path`);
      if (it.a.includes('repeat 1:')) P.push(`${it.q}: repeat 1`);
      break;
    }
    case 'loopcount': want(it.prog.length); break;
    case 'loopsaved': want(it.prog.length - it.segs.reduce((a, s) => a + s.body.length, 0)); break;
    case 'predict': case 'says': {
      let [x, y] = it.s || [0, 0]; const said = [];
      for (const b of it.blocks) for (let i = 0; i < b.times; i++) for (const c of b.body) { if (c.startsWith('say:')) said.push(c.slice(4)); else { x += VEC[SYM[c]][0]; y += VEC[SYM[c]][1]; if (it.k === 'predict' && (x < 0 || y < 0 || x >= it.W || y >= it.H)) P.push(`${it.q}: off the grid`); } }
      want(it.k === 'predict' ? 'ABCDE'[x] + (y + 1) : said.join(' ')); break;
    }
    case 'ifgrid': {
      let [x, y] = it.s, [dx, dy] = VEC[SYM[it.d0]];
      for (let i = 0; i < it.times; i++) {
        x += dx; y += dy;
        if (x < 0 || y < 0 || x >= it.W || y >= it.H) P.push(`${it.q}: off the grid`);
        const c = it.colors[x + ',' + y]; if (!c) continue;
        const right = (c === 'B') === (it.blueTurn === 'right');
        [dx, dy] = right ? [-dy, dx] : [dy, -dx];
      }
      want(String.fromCharCode(65 + x) + (y + 1)); break;
    }
    case 'box1': {
      let v = it.story.start;
      it.story.steps.slice(0, it.i + 1).forEach(s => { const m = s.text.match(/(puts in|takes out) (\d+)/); v += (m[1] === 'puts in' ? 1 : -1) * +m[2]; });
      if (v < 0 || v > 10) P.push(`${it.q}: out of 0 to 10`); want(v); break;
    }
    case 'box2': {
      let [a, m] = it.story.start;
      it.story.steps.slice(0, it.i + 1).forEach(s => { let x;
        if ((x = s.text.match(/^Sell (\d+) \w+ for \$(\d+) each/))) { a -= +x[1]; m += x[1] * x[2]; }
        else if ((x = s.text.match(/for \$(\d+)\.$/))) m -= +x[1];
        else if ((x = s.text.match(/^(Bake|Make) (\d+)/))) a += +x[2];
        else if ((x = s.text.match(/^(Give|Spill) (\d+)/))) a -= +x[2]; });
      if (a < 0 || m < 0) P.push(`${it.q}: negative`); want(it.which ? '$' + m : a); break;
    }
    case 'score': want(pyShow(run(it.py).G.get(it.name))); break;
    case 'start': { const o = run(`${it.name} = ${it.a}\n${it.py}`).out; if (o[0] !== String(it.end)) P.push(`${it.q}: starting at ${it.a} says ${o[0]}`); if (+it.a < 1) P.push(`${it.q}: start below 1`); break; }
    case 'output': { const o = run(it.src).out; if (o.join(' / ') !== it.out.join(' / ')) P.push(`${it.q.slice(0, 60)}: prints ${o.join(' / ')}, key ${it.out.join(' / ')}`); want(o.join(' / ')); break; }
    case 'trace': { let snap = null; pyRun(it.src, (n, G) => { if (n === it.line) snap = it.names.map(x => G.get(x)); }); want(snap.join(', ')); break; }
    case 'loop': {
      const marks = []; let fin = null;
      const res = pyRun(it.src, (n, G) => { if (n === 2) marks.push([G.get(it.cnt), G.get(it.tot)]); });
      fin = res.G.get(it.tot);
      const tot = it.pass + 1 < marks.length ? marks[it.pass + 1][1] : fin;
      if (marks.length !== 5) P.push(`${it.q}: loop runs ${marks.length} times`);
      want(`${marks[it.pass][0]}, ${tot}`); break;
    }
    case 'memory': {
      const h = []; let last;
      pyRun(it.src, (n, G) => { const x = G.get(it.name); if (x !== undefined && x !== last) { h.push(pyShow(x)); last = x; } });
      want(h.join(', ')); break;
    }
    case 'list': { let snap; pyRun(it.src, (n, G) => { if (n === it.line) snap = pyShow(G.get(it.name)); }); want(snap); break; }
    case 'listprint': { let before = 0, got = null; pyRun(it.src, (n, G, F, out) => { if (n === it.line) got = out.length > before ? out[out.length - 1] : null; before = out.length; }); want(got); break; }
    case 'steps': want(run(it.src).counts[it.mark] || 0); break;
    case 'waste': { const L = 'ABCDEFG', counts = all.filter(x => x.k === 'steps').map(x => run(x.src).counts[x.mark]); want(L[counts.indexOf(Math.max(...counts))]); break; }
    case 'recur': {
      const res = run(it.src), c = res.calls[it.i];
      if (!c) { P.push(`${it.q}: no call ${it.i + 1}`); break; }
      want(`${c.name}(${c.args.join(', ')}) ${it.ret ? 'returns' : 'prints'} ${it.ret ? pyShow(c.ret) : res.out[it.i]}`); break;
    }
    case 'shapes': { const m = new Map(it.legend); want(it.shapes.map(s => m.get(s)).join('')); if (new Set(it.legend.map(x => x[0])).size !== it.legend.length) P.push('two letters share a shape'); break; }
    case 'pxrun': { let s = ''; for (const part2 of it.code.split(', ')) { const [k, c] = part2.split(' '); s += (c === 'black' ? '1' : '0').repeat(+k); } if (s.length !== 8) P.push(`${it.q}: row is ${s.length} long`); want(s); break; }
    case 'pxbin': want(it.code); break;
    case 'pxname': { const p = PICS[it.a], f = p.map(x => [...x].reverse().join('')); if (JSON.stringify(it.rows) !== JSON.stringify(p) && JSON.stringify(it.rows) !== JSON.stringify(f)) P.push(`${it.q}: picture is not a ${it.a}`); break; }
    case 'pxenc': want(it.row.split('').map(c => c === '#' ? 1 : 0).join('')); break;
    case 'beaddec': want(it.code.map(b => String.fromCharCode(64 + parseInt(b, 2))).join('')); break;
    case 'beadenc': { let k = it.c.charCodeAt(0) - 64, s = ''; for (let i = 0; i < 5; i++) { s = (k % 2 ? '●' : '○') + s; k = Math.floor(k / 2); } want(s); break; }
    case 'ckey': want(String.fromCharCode((it.c.charCodeAt(0) - 65 + it.shift) % 26 + 65)); break;
    case 'cenc': want(it.m.split('').map(c => c === ' ' ? c : String.fromCharCode((c.charCodeAt(0) - 65 + it.shift) % 26 + 65)).join('')); break;
    case 'cdec': want(it.c.split('').map(c => c === ' ' ? c : String.fromCharCode((c.charCodeAt(0) - 65 - it.shift + 26) % 26 + 65)).join('')); break;
    case 'kwkey': case 'kwenc': case 'kwdec': {
      let al = ''; for (const c of it.kw + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') if (!al.includes(c)) al += c;
      if (it.k === 'kwkey') want(al[it.c.charCodeAt(0) - 65]);
      else if (it.k === 'kwenc') want(it.m.split('').map(c => c === ' ' ? c : al[c.charCodeAt(0) - 65]).join(''));
      else want(it.c.split('').map(c => c === ' ' ? c : String.fromCharCode(65 + al.indexOf(c))).join(''));
      break;
    }
    case 'cksum': want(it.d.split('').reduce((a, c) => a + +c, 0)); break;
    case 'ckok': want(it.d.split('').reduce((a, c) => a + +c, 0) % 10 === it.cs ? 'OK' : 'changed'); break;
    case 'ckmake': want(it.d.split('').reduce((a, c) => a + +c, 0) % 10); break;
    case 'type': want(/^".*"$/.test(it.v) ? 'String' : /^(true|false)$/.test(it.v) ? 'Boolean' : /\./.test(it.v) ? 'Decimal' : /^-?\d+$/.test(it.v) ? 'Integer' : '?'); break;
    case 'pwN': want(big(it.N)); break;
    case 'pwcount': { let x = 1n; for (let i = 0; i < it.Ln; i++) x *= BigInt(it.N); want(big(x)); break; }
    case 'pwbits': want((Math.round(it.Ln * Math.log10(it.N) / Math.log10(2) * 10) / 10).toFixed(1)); break;
    case 'pwrank': want(it.vals.map((v2, i) => [v2, 'ABCDEFGH'[i]]).sort((a, b) => a[0] - b[0]).map(x => x[1]).join(', ')); break;
    case 'pwtop': { const b = it.vals.map(BigInt); let top = 0; b.forEach((x, i) => { if (x > b[top]) top = i; }); want('ABCDEFGH'[top]); break; }
    case 'hsum': case 'hash': { let s = 0; for (let i = 0; i < it.w.length; i++) s += (i + 1) * (it.w.charCodeAt(i) - 96); want(it.k === 'hsum' ? s : String(s % 100).padStart(2, '0')); break; }
    case 'hlogin': { let s = 0; for (let i = 0; i < it.w.length; i++) s += (i + 1) * (it.w.charCodeAt(i) - 96); want(String(s % 100).padStart(2, '0') === it.sh ? 'yes' : 'no'); break; }
    case 'htab': {
      const slots = new Map();
      for (const k of it.keys) { let s = k % it.size; for (let tries = 0; slots.has(s); tries++) { s = s + 1 === it.size ? 0 : s + 1; if (tries > it.size) break; } slots.set(s, k); if (k === it.key) { want(`home ${k % it.size}, slot ${s}`); break; } }
      break;
    }
    case 'sort': {
      const x = it.list.slice(), n = x.length;
      for (let p = 0; p <= it.pass; p++) {
        if (it.alg === 'selection') { const rest = x.slice(p), m = Math.min(...rest), j = p + rest.indexOf(m); x[j] = x[p]; x[p] = m; }
        else if (it.alg === 'bubble') { for (let j = 0; j + 1 < n - p; j++) if (x[j] > x[j + 1]) x.splice(j, 2, x[j + 1], x[j]); }
        else { const val = x.splice(p + 1, 1)[0]; let j = 0; while (j <= p && x[j] <= val) j++; x.splice(j, 0, val); }
      }
      want(x.join(' ')); break;
    }
    case 'sq': {
      const S = [], Q = []; let ret = '';
      for (const op of it.ops.slice(0, it.i + 1)) { ret = ''; const m = op.match(/^(S|Q)\.(\w+)\((\d*)\)$/);
        if (m[2] === 'push') S.push(+m[3]); else if (m[2] === 'enqueue') Q.push(+m[3]); else if (m[2] === 'pop') ret = String(S.splice(S.length - 1, 1)[0]); else ret = String(Q.splice(0, 1)[0]); }
      want(`${ret || 'nothing'}; S [${S.join(', ')}]; Q [${Q.join(', ')}]`); break;
    }
    case 'rsan': want(it.p * it.qq); break;
    case 'rsaphi': want((it.p - 1) * (it.qq - 1)); break;
    case 'rsaed': want((it.e * it.d) % it.phi); break;
    case 'rsaenc': { const c = BigInt(it.m) ** BigInt(it.e) % BigInt(it.N); want(String(c)); if (c === BigInt(it.m)) P.push(`${it.q}: encrypts to itself`); break; }
    case 'rsadec': want(String(BigInt(it.c) ** BigInt(it.d) % BigInt(it.N))); break;
    case 'dij': case 'dijstep': {
      const N = 'ABCDEF'.split(''), D = {};
      N.forEach(a => N.forEach(b => { D[a + b] = a === b ? 0 : Infinity; }));
      it.edges.forEach(([a, b, w]) => { D[a + b] = Math.min(D[a + b], w); D[b + a] = Math.min(D[b + a], w); });
      const W0 = { ...D };
      N.forEach(k => N.forEach(a => N.forEach(b => { if (D[a + k] + D[k + b] < D[a + b]) D[a + b] = D[a + k] + D[k + b]; })));
      if (it.k === 'dij') {
        const m = it.a.match(/^(\d+) via (.*)$/), path = m[2].split(' → ');
        const len = path.slice(1).reduce((a, x, i) => a + W0[path[i] + x], 0);
        if (+m[1] !== D['A' + it.v] || len !== D['A' + it.v] || path[0] !== 'A' || path[path.length - 1] !== it.v) P.push(`${it.q}: key ${it.a}, shortest ${D['A' + it.v]}`);
      } else {
        const order = N.slice().sort((a, b) => D['A' + a] - D['A' + b]), seen = order.slice(0, it.i + 1);
        const row = N.map(v => seen.includes(v) ? D['A' + v] : Math.min(...seen.map(u => D['A' + u] + W0[u + v])));
        want(`visit ${order[it.i]}; ${row.map(x => x === Infinity ? '∞' : x).join(' ')}`);
      }
      break;
    }
    case 'chg': case 'chgcombo': case 'chgfail': {
      const [c1, c2, c3] = it.coins;
      const minC = a => { let b = Infinity; for (let z = 0; z * c3 <= a; z++) for (let y = 0; z * c3 + y * c2 <= a; y++) { const rest = a - z * c3 - y * c2; if (rest % c1 === 0) b = Math.min(b, z + y + rest / c1); } return b; };
      if (it.k === 'chg') want(minC(it.amt));
      else if (it.k === 'chgcombo') { const parts2 = it.a.split(' + ').map(Number); if (parts2.reduce((a, b) => a + b, 0) !== it.amt || parts2.length !== minC(it.amt) || parts2.some(x => !it.coins.includes(x))) P.push(`${it.q}: ${it.a} is not a fewest-coin way`); }
      else { const gr = a => { let k = 0; for (const c of [c3, c2, c1]) { k += Math.floor(a / c); a %= c; } return k; }; let a = 1; while (gr(a) === minC(a)) a++; want(a); }
      break;
    }
    default: P.push(`unknown kind ${it.k}`);
  }
  return P;
}

Gen.add('code-logic', {
  title: 'Code and Logic', type: 'Practice',
  css: `.cl-cards{display:inline-flex;flex-wrap:wrap;gap:4px;vertical-align:middle}
.cl-card{position:relative;display:inline-grid;place-items:center;width:.36in;height:.36in;border:1.5px solid #333;border-radius:5px;font:700 20px/1 var(--sans);background:#fff}
.cl-card.cl-empty{border-style:dashed}
.cl-cross{position:absolute;inset:0;display:grid;place-items:center;font-size:30px}
.cl-fix{position:absolute;top:-.3in;left:0;right:0;text-align:center;font-size:18px}
.cl-center{text-align:center}
.cl-row{display:flex;align-items:center;gap:14px;flex-wrap:wrap;min-height:.5in}
.cl-picks{display:inline-flex;gap:6px}
.cl-pick{position:relative;display:inline-grid;place-items:center;min-width:.42in;height:.42in;font-size:24px;line-height:1}
.cl-pick small{font:700 11px var(--sans);margin-left:1px}
.cl-ring{position:absolute;inset:-2px;border:3px solid #b03020;border-radius:50%}
.cl-track{display:flex;gap:4px;justify-content:center;margin:4px 0}
.cl-pad{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;width:.55in;height:.6in;border:1.5px solid #333;border-radius:8px;font-size:22px}
.cl-pad b{font:700 13px var(--sans)}
.cl-lily{border-radius:50%;width:.5in;height:.5in;background:#dcefd6;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cl-lily b{font-size:16px}
.cl-start{font-weight:600;min-width:9em}
.cl-cells{display:grid;gap:10px 16px;margin:6px 0}
.cl-c2{grid-template-columns:repeat(2,minmax(0,1fr))}
.cl-c3{grid-template-columns:repeat(3,minmax(0,1fr))}
.cl-cell{border:1px solid #bbb;border-radius:8px;padding:6px 8px;break-inside:avoid}
.cl-cell p{margin:3px 0;font-size:14px}
.cl-cell .gen-svg{display:block;margin:4px auto}
.cl-fixline{margin-top:8px!important}
.cl-prog{display:flex;flex-direction:column;gap:6px}
.cl-side{display:flex;gap:8px;align-items:flex-start}
.cl-side .gen-svg{margin:0!important;flex:none}
.cl-blocks{font-size:13px}
.cl-hat{background:#eee;border:1.5px solid #333;border-radius:10px 10px 3px 3px;padding:2px 6px;font-weight:700;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cl-blk{border:1.5px solid #333;border-radius:3px;padding:2px 6px}
.cl-story{display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:start;margin:6px 0 12px;break-inside:avoid}
.cl-box{display:flex;flex-direction:column;align-items:center;border:2.5px solid #222;border-radius:4px;width:1in;padding:4px}
.cl-box-name{font-weight:700;border-bottom:1.5px solid #222;width:100%;text-align:center}
.cl-box-val{font:700 30px var(--sans)}
.cl-tbl td,.cl-tbl th{font-size:14px;padding:3px 8px}
.cl-tight td,.cl-tight th{padding:2px 4px;font-size:13px}
.cl-q{margin:6px 0 12px;break-inside:avoid}
.cl-code{font:13.5px/1.45 ui-monospace,Consolas,monospace;border:1.5px solid #333;border-radius:6px;padding:5px 8px;margin:4px 0;white-space:pre;overflow:hidden}
.cl-ln{display:block}
.cl-ln i{display:inline-block;width:1.6em;color:#777;font-style:normal;font-size:11px}
.cl-mark{background:#ddd;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cl-blocks3{white-space:pre}
.cl-q-box{display:inline-block;border:1.5px solid #333;padding:0 6px}
.cl-out{display:flex;flex-wrap:wrap;gap:6px 10px;margin:6px 0 2px}
.cl-pair{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px;align-items:start;margin:6px 0 14px;break-inside:avoid}
.cl-dij{grid-template-columns:3.1in minmax(0,1fr);margin:2px 0 4px}
.cl-dij .gen-svg{margin:0!important}
.cl-dash{color:#777;font-size:12px}
.cl-mems{display:flex;flex-direction:column;gap:6px;min-width:2.6in}
.cl-mem{border:2px solid #222;border-radius:4px;min-height:.55in}
.cl-mem-name{margin:0;padding:1px 6px;font:700 13px ui-monospace,Consolas,monospace;border-bottom:1.5px solid #222}
.cl-mem-in{padding:3px 6px;font:15px ui-monospace,Consolas,monospace}
.cl-old{text-decoration:line-through}
.cl-shape{width:.34in;height:.34in}
.cl-legend{display:flex;flex-wrap:wrap;gap:10px 18px}
.cl-leg{display:inline-flex;align-items:center;gap:6px;font:700 20px var(--sans)}
.cl-msg{display:flex;flex-wrap:wrap;gap:6px 18px}
.cl-word{display:inline-flex;gap:2px}
.cl-lt{display:inline-flex;flex-direction:column;align-items:center;min-width:.28in}
.cl-lt>b{font:700 16px ui-monospace,Consolas,monospace}
.cl-lb{display:inline-block;min-width:.26in;height:.3in;border-bottom:1.5px solid #222;text-align:center;font:700 16px ui-monospace,Consolas,monospace}
.cl-code-row{display:flex;gap:8px}
.cl-sq{display:inline-block;width:.16in;height:.16in;border:1.5px solid #222;vertical-align:-3px;margin-left:2px;background:#fff}
.cl-sq.on{background:#222;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cl-px{border-collapse:collapse}
.cl-px td{width:.3in;height:.3in;border:1px solid #444;padding:0;position:relative}
.cl-px td.on{background:#222;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cl-on{position:absolute;inset:0;background:#b03020;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cl-pxwrap{display:grid;grid-template-columns:auto auto;gap:18px;align-items:start;margin:6px 0 12px;break-inside:avoid}
.cl-rows{margin:4px 0;padding-left:1.8em;font-size:15px}
.cl-rows li{height:.3in}
.cl-bits{font:15px ui-monospace,Consolas,monospace;letter-spacing:.06em}
.cl-bitline{display:inline-block;width:1.4in;border-bottom:1.5px solid #222}
.cl-beads{display:inline-flex;gap:2px;vertical-align:middle}
.cl-bead{position:relative;display:inline-block;width:.15in;height:.15in;border:1.5px solid #222;border-radius:50%;background:#fff}
.cl-bead.on{background:#222;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cl-dot{position:absolute;inset:1px;border-radius:50%;background:#b03020}
.cl-beadkey{display:grid;grid-template-columns:repeat(4,1fr);gap:3px 14px;font-size:14px}
.cl-beadkey span b{display:inline-block;width:1.2em}
.cl-beadrow{display:flex;gap:14px;flex-wrap:wrap}
.cl-beadrow .cl-lt{gap:3px}
.cl-strip{overflow:hidden}
.cl-strip-row{display:flex}
.cl-strip-row>span{flex:1;text-align:center;font:700 13px ui-monospace,Consolas,monospace;border:1px solid #444;margin:-1px 0 0 -1px;min-height:.26in;line-height:.26in}
.cl-strip-row .cl-lb{border-bottom:1px solid #444;height:auto;min-width:0}
.cl-strip-h{flex:0 0 3.4em!important;font-size:11px!important}
.cl-vals{columns:5;margin:4px 0;padding-left:2em;font-size:15px}
.cl-vals li{margin-bottom:6px}
.cl-sort-head{font-size:16px!important}
.cl-useline{display:inline-block;width:4in;border-bottom:1px solid #777}
.cl-abc{display:flex;flex-wrap:wrap;gap:2px 9px;font-size:12px;margin:4px 0}
.cl-abc b{margin-right:2px}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '3' },
    { id: 'skill', label: 'Skill', type: 'select', options: v => BYGRADE[v.grade].map(s => [s, label(s, v.grade)]), def: 'ifgrid' },
    { id: 'alg', label: 'Sorting algorithm', type: 'select', options: ALGS, def: 'selection', show: v => v.skill === 'sort' },
    { id: 'count', label: 'Length', type: 'select', options: countOpts, def: 'm' },
  ],
  make(v, r) {
    const s = build(v, r), gname = GRADES.find(x => x[0] === v.grade)[1], name = label(v.skill, v.grade);
    const alg = v.skill === 'sort' ? ALGS.find(x => x[0] === v.alg)[1] : '';
    return Object.assign({ title: `${alg || name.replace(/ \(Python\)$/, '')}: ${gname}`, level: gname, eyebrow: ['shapes', 'pixel', 'beads', 'caesar', 'keyword', 'start'].includes(v.skill) ? 'Puzzle' : 'Practice' }, s,
      { notes: s.notes + ' Press New sheet for a fresh set at the same level.' });
  },
  verify(s) {
    const out = [];
    for (const it of s.items) { try { out.push(...verifyItem(it, s.items)); } catch (e) { out.push(`${String(it.q).slice(0, 60)}: verify crashed: ${e.message}`); } }
    return out;
  },
});
})();
