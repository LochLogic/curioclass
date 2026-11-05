// Music Notation and Rhythm generator, grades K-12. Every symbol is drawn as inline SVG paths: staff lines, simplified
// treble and bass clefs, noteheads, stems, flags, beams, rests, dots, ledger lines, sharps, flats, bar lines, time and
// key signatures, and a piano keyboard. Answers draw in red on the key (class ws-ans, hidden on the student copy).
// Skills by grade:
//   Rhythm: count the sounds (K); read stick notation with ta, ti-ti, ta-a and rest (1-2); write the counts
//     (1 & 2 &, 1 e & a, 6/8 counts) under rhythms from grade 3, with a focus on sixteenths, dotted notes or
//     syncopation; which rhythm did I clap (K-3, the teacher claps from the key); rhythm dictation (3-8); complete
//     the measure with one note or rest; add the bar lines; find and fix measures with the wrong number of beats;
//     rests and their beats.
//   Pitch: so-mi, so-mi-la and do-re-mi-so-la on 2-, 3- and 5-line staves (1-3); steps, skips and repeats (2-4);
//     name the notes on the treble, bass or grand staff with or without ledger lines; note-name words; draw the note
//     for a letter; whole and half steps on the keyboard (4-6).
//   Theory: build major, natural minor, harmonic and melodic minor and major pentatonic scales on the staff and the
//     keyboard; key signatures (name and write, major and minor); intervals (number from grade 5, quality from 7);
//     triads (build and name), inversions, chords of the key with Roman numerals (triads, and seventh chords from
//     grade 9); chord symbols to notes (8-12).
//   Composition staff paper (1-12): rhythm line, 2- and 3-line so-mi staves, treble, bass or grand staff, a measure
//     grid with numbers, time signature and form labels; the key draws a model in red.
// Standards (National Core Arts Standards, music): MU:Pr4.2 (read and perform rhythmic and melodic patterns from
// iconic and standard notation, K-8; interpret notation and theory, HS), MU:Cr2.1 (document musical ideas with iconic
// or standard notation), MU:Cr3.2 (present a final version, the staff paper). Grades 9-12 theory follows the topics of
// the AP Music Theory course.
(() => {
const { part, example, fill, blank, key, esc } = Gen.h;

/* ---------- drawing primitives ---------- */
const RED = '#b03020', INK = '#222', GREY = '#9a9a9a';
const SP = 10;                       // one staff space in px
const OFF = 7;                       // a note sits this far into its time slot
const f1 = x => Math.round(x * 10) / 10;
const FONT = 'font-family="Helvetica, Arial, sans-serif"';
const SERIF = 'font-family="Georgia, \'Times New Roman\', serif"';
const ln = (x1, y1, x2, y2, c = INK, w = 1) => `<line x1="${f1(x1)}" y1="${f1(y1)}" x2="${f1(x2)}" y2="${f1(y2)}" stroke="${c}" stroke-width="${w}"/>`;
const rect = (x, y, w, h, fillc, stroke, sw = 1, rx = 0) => `<rect x="${f1(x)}" y="${f1(y)}" width="${f1(w)}" height="${f1(h)}"${rx ? ` rx="${rx}"` : ''} fill="${fillc}"${stroke ? ` stroke="${stroke}" stroke-width="${sw}"` : ''}/>`;
const circ = (x, y, rr, c, stroke) => `<circle cx="${f1(x)}" cy="${f1(y)}" r="${rr}" fill="${c}"${stroke ? ` stroke="${stroke}" stroke-width="1.2"` : ''}/>`;
const tx = (x, y, s, c = INK, size = 12, anchor = 'middle', bold = false) => `<text x="${f1(x)}" y="${f1(y)}" ${FONT} font-size="${size}" fill="${c}" text-anchor="${anchor}"${bold ? ' font-weight="700"' : ''}>${esc(s)}</text>`;
const ans = (on, body) => (on && body ? `<g class="ws-ans">${body}</g>` : body);
const pathD = (pts, c, w, extra = '') => `<path d="${pts}" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"${extra}/>`;
const svg = (w, h, body, label, scale = 1) => `<svg class="gen-svg" viewBox="0 0 ${Math.ceil(w)} ${Math.ceil(h)}" role="img" aria-label="${esc(label)}" style="max-width:${(w * scale / 96).toFixed(2)}in">${body}</svg>`;
const wline = (x, y, w) => ln(x - w / 2, y, x + w / 2, y, GREY, 0.9);   // a short writing line

// a staff: kind 'treble' | 'bass' | 'five' (5 lines, no clef) | 'one' (rhythm line) | 'none' (stick notation on a
// baseline) | 'two' | 'three' (so-mi staves). y(p) gives the height of staff position p (0 = bottom line, 1 = the
// space above it, and so on); mid is where rests sit; hi and lo bound the bar lines.
function staff(kind, top) {
  const s = { kind, top, five: kind === 'treble' || kind === 'bass' || kind === 'five' };
  if (s.five) { s.y = p => top + 4 * SP - p * SP / 2; s.lines = [0, 2, 4, 6, 8]; s.mid = s.y(4); s.hi = s.y(8); s.lo = s.y(0); }
  else if (kind === 'two' || kind === 'three') {
    const n = kind === 'two' ? 2 : 3;
    s.y = p => top + (n - 1) * SP * 1.2 - p * SP * 0.6; s.lines = kind === 'two' ? [0, 2] : [0, 2, 4];
    s.hi = top; s.lo = s.y(0); s.mid = (s.hi + s.lo) / 2;
  } else if (kind === 'one') { s.y = () => top; s.lines = []; s.mid = top; s.hi = top - 13; s.lo = top + 13; }
  else { s.y = () => top; s.lines = []; s.mid = top - 14; s.hi = top - 36; s.lo = top + 5; }
  return s;
}
function staffLines(s, x1, x2) {
  if (s.kind === 'one') return ln(x1, s.top, x2, s.top, INK, 1.1);
  return s.lines.map(p => ln(x1, s.y(p), x2, s.y(p), INK, 1)).join('');
}
const stemUp = (s, p) => (s.five ? p < 4 : true);
function ledgers(s, x, p, c) {
  if (!s.five) return '';
  let o = '';
  for (let q = -2; q >= p; q -= 2) o += ln(x - 9.5, s.y(q), x + 9.5, s.y(q), c, 1.2);
  for (let q = 10; q <= p; q += 2) o += ln(x - 9.5, s.y(q), x + 9.5, s.y(q), c, 1.2);
  return o;
}
function head(x, y, open, c, whole) {
  if (whole) return `<ellipse cx="${f1(x)}" cy="${f1(y)}" rx="7.2" ry="4.8" fill="${c}"/><ellipse cx="${f1(x)}" cy="${f1(y)}" rx="3.4" ry="2.5" transform="rotate(-55 ${f1(x)} ${f1(y)})" fill="#fff"/>`;
  return `<ellipse cx="${f1(x)}" cy="${f1(y)}" rx="${open ? 5.9 : 6}" ry="${open ? 4 : 4.2}" transform="rotate(-22 ${f1(x)} ${f1(y)})" fill="${open ? '#fff' : c}" stroke="${c}" stroke-width="${open ? 1.8 : 0.6}"/>`;
}
// sharp (1), flat (-1) or natural (0), centered at x
function accG(x, y, a, c) {
  if (a === 1) return ln(x - 2.3, y - 9, x - 2.3, y + 10, c, 1.2) + ln(x + 2.3, y - 10, x + 2.3, y + 9, c, 1.2) + ln(x - 5, y - 2, x + 5, y - 5, c, 2.8) + ln(x - 5, y + 5, x + 5, y + 2, c, 2.8);
  if (a === -1) return ln(x - 3, y - 15, x - 3, y + 4.5, c, 1.4) + pathD(`M${f1(x - 3)} ${f1(y + 4.5)} C${f1(x + 7)} ${f1(y - 0.5)} ${f1(x + 5)} ${f1(y - 8)} ${f1(x - 3)} ${f1(y - 2)}`, c, 1.9);
  return ln(x - 3, y - 11, x - 3, y + 4.5, c, 1.2) + ln(x + 3, y - 4.5, x + 3, y + 11, c, 1.2) + ln(x - 3, y - 2, x + 3, y - 4, c, 2.6) + ln(x - 3, y + 4, x + 3, y + 2, c, 2.6);
}
// a simplified treble clef: one stroke that curls round the G line, loops above the staff and ends in a hook and a dot
function trebleClef(s, x, c = INK) {
  const g = s.y(2), P = (dx, dy) => `${f1(x + dx)} ${f1(g + dy)}`;
  const d = `M${P(1.5, 2.5)} C${P(6.5, 2)} ${P(6.5, -6.5)} ${P(0.5, -6.5)} C${P(-6, -6.5)} ${P(-8, 1)} ${P(-5.5, 5)} C${P(-3, 10)} ${P(8, 10.5)} ${P(9.5, 2.5)} C${P(11, -5)} ${P(5, -10)} ${P(0, -14)} C${P(-6, -19)} ${P(-6.5, -27)} ${P(-2, -35)} C${P(1, -41)} ${P(6.5, -38)} ${P(5, -30.5)} C${P(4, -24)} ${P(-2, -21)} ${P(-1, -13)} L${P(2.5, 22)} C${P(3, 28.5)} ${P(-3.5, 30)} ${P(-5.5, 26)}`;
  return pathD(d, c, 2.2) + circ(x - 3.8, g + 25.5, 2.8, c);
}
// a bass clef: the dot on the F line, the curve, and the two dots either side of the F line
function bassClef(s, x, c = INK) {
  const fy = s.y(6);
  return circ(x + 3, fy, 3.4, c) + pathD(`M${f1(x + 1)} ${f1(fy - 1)} C${f1(x + 2)} ${f1(fy - 10.5)} ${f1(x + 17.5)} ${f1(fy - 11)} ${f1(x + 17.5)} ${f1(fy - 0.5)} C${f1(x + 17.5)} ${f1(fy + 9)} ${f1(x + 9)} ${f1(fy + 17)} ${f1(x - 1)} ${f1(fy + 23)}`, c, 2.5) +
    circ(x + 23, fy - 5, 1.8, c) + circ(x + 23, fy + 5, 1.8, c);
}
function timeSig(s, x, top, bot, c = INK) {
  const t = (y, n, size) => `<text x="${f1(x)}" y="${f1(y)}" ${SERIF} font-size="${size}" font-weight="700" fill="${c}" text-anchor="middle">${n}</text>`;
  if (s.five) return t(s.y(4) - 1.5, top, 23) + t(s.y(0) - 1.5, bot, 23);
  if (s.kind === 'one') return t(s.top - 2.5, top, 18) + t(s.top + 15.5, bot, 18);
  return t(s.top - 17, top, 17) + t(s.top + 1, bot, 17);
}
const SH_POS = [8, 5, 9, 6, 3, 7, 4], FL_POS = [4, 7, 3, 6, 2, 5, 1];   // treble positions; bass is two lower
function keySig(s, x, n, c = INK) {
  let o = '';
  const k = Math.abs(n), off = s.kind === 'bass' ? -2 : 0;
  for (let i = 0; i < k; i++) o += accG(x + 7 + i * 11, s.y((n > 0 ? SH_POS : FL_POS)[i] + off), n > 0 ? 1 : -1, c);
  return { svg: o, w: k ? k * 11 + 10 : 0 };
}
function bar(s, x, kind, c = INK) {
  const a = s.hi, b = s.lo;
  if (kind === 'final') return ln(x - 6, a, x - 6, b, c, 1.3) + ln(x - 1.8, a, x - 1.8, b, c, 4);
  if (kind === 'double') return ln(x - 4, a, x - 4, b, c, 1.3) + ln(x, a, x, b, c, 1.3);
  return ln(x, a, x, b, c, 1.3);
}
function rest(s, x, d, c) {
  const m = s.mid;
  let o = '';
  if (d === 4 || d === 6) o = `<path d="M${f1(x - 2)} ${f1(m - 14)} L${f1(x + 3.5)} ${f1(m - 7.5)} L${f1(x - 1.5)} ${f1(m - 2)} L${f1(x + 3.5)} ${f1(m + 4)} C${f1(x - 3)} ${f1(m + 1)} ${f1(x - 4.5)} ${f1(m + 8)} ${f1(x + 0.5)} ${f1(m + 12)}" fill="none" stroke="${c}" stroke-width="2.6" stroke-linejoin="miter" stroke-linecap="round"/>`;
  else if (d === 2 || d === 1) {
    o = circ(x - 2.5, m - 5, 2.5, c) + pathD(`M${f1(x - 2.5)} ${f1(m - 3)} C${f1(x)} ${f1(m - 1.5)} ${f1(x + 2.5)} ${f1(m - 3)} ${f1(x + 4)} ${f1(m - 6.5)} L${f1(x - 1)} ${f1(m + (d === 1 ? 14 : 9))}`, c, 1.6);
    if (d === 1) o += circ(x - 4, m + 1.5, 2.5, c) + pathD(`M${f1(x - 4)} ${f1(m + 3.5)} C${f1(x - 1.5)} ${f1(m + 5)} ${f1(x + 0.5)} ${f1(m + 3.5)} ${f1(x + 2)} ${f1(m + 0.5)}`, c, 1.6);
  } else if (d === 8 || d === 12) {
    const y = s.five ? s.y(4) - 5 : s.kind === 'one' ? s.top - 5 : s.top - 9;
    o = rect(x - 6.5, y, 13, 5, c);
  } else if (d === 16) {
    const y = s.five ? s.y(6) : s.kind === 'one' ? s.top : s.top - 18;
    o = rect(x - 6.5, y, 13, 5, c);
  }
  if (d === 6 || d === 12) o += circ(x + 9, m - 4, 1.9, c);
  return o;
}
function flags(sx, y2, up, n, c) {
  let o = '';
  for (let k = 0; k < n; k++) {
    const yy = up ? y2 + k * 7 : y2 - k * 7, sg = up ? 1 : -1;
    o += pathD(`M${f1(sx)} ${f1(yy)} C${f1(sx + 1)} ${f1(yy + sg * 7)} ${f1(sx + 10)} ${f1(yy + sg * 10)} ${f1(sx + 8)} ${f1(yy + sg * 20)}`, c, 1.9);
  }
  return o;
}
function dotFor(s, e, y, c) {
  const dy = s.five ? ((((e.p ?? 4) % 2) + 2) % 2 === 0 ? -5 : 0) : -4;
  return circ(e.x + 10, y + dy, 1.9, c);
}
function noteSvg(s, e, o, c) {
  const y = s.y(e.p ?? 4);
  const open = e.d >= 8, whole = e.d === 16, stick = o.stick && !open;
  let out = ledgers(s, e.x, e.p, c);
  if (e.a != null) out += accG(e.x - 15, y, e.a, c);
  if (!stick) out += head(e.x, y, open, c, whole);
  if (!whole) {
    const up = stemUp(s, e.p);
    const sx = stick ? e.x : up ? e.x + 5.4 : e.x - 5.4, y2 = up ? y - 32 : y + 32;
    out += ln(sx, stick ? y + 2 : y, sx, y2, c, 1.5);
    if (e.d < 4) out += flags(sx, y2, up, e.d === 1 ? 2 : 1, c);
  }
  if (e.d === 3 || e.d === 6 || e.d === 12) out += dotFor(s, e, y, c);
  return out;
}
function beamSvg(s, g, o, c) {
  const ys = g.map(e => s.y(e.p ?? 4));
  const up = s.five ? g.reduce((a, e) => a + e.p, 0) / g.length < 4 : true;
  const yb = up ? Math.min(...ys) - 31 : Math.max(...ys) + 31, t = 4.6;
  let out = '';
  const sxs = g.map((e, i) => {
    const y = ys[i], sx = o.stick ? e.x : up ? e.x + 5.4 : e.x - 5.4;
    out += ledgers(s, e.x, e.p, c);
    if (e.a != null) out += accG(e.x - 15, y, e.a, c);
    if (!o.stick) out += head(e.x, y, false, c);
    out += ln(sx, o.stick ? y + 2 : y, sx, yb, c, 1.5);
    return sx;
  });
  out += rect(sxs[0] - 0.75, up ? yb : yb - t, sxs[sxs.length - 1] - sxs[0] + 1.5, t, c);
  for (let i = 0; i + 1 < g.length; i++) if (g[i].d === 1 && g[i + 1].d === 1) out += rect(sxs[i] - 0.75, up ? yb + 7.5 : yb - 7.5 - t, sxs[i + 1] - sxs[i] + 1.5, t, c);
  return out;
}
// draw the events of one measure (x and pos already set): beams join eighths and sixteenths inside one beat
function drawEvents(s, ev, o) {
  const groups = [];
  let cur = [];
  const flush = () => { if (cur.length) groups.push(cur); cur = []; };
  for (const e of ev) {
    const beamable = !e.r && !e.gap && !e.key && e.d < 4 && e.d !== 3;
    if (!beamable) { flush(); groups.push([e]); continue; }
    if (cur.length && Math.floor(cur[0].pos / o.beat) !== Math.floor(e.pos / o.beat)) flush();
    cur.push(e);
  }
  flush();
  let out = '';
  for (const g of groups) {
    const e = g[0], red = !!(o.key || e.key || e.gap), c = red ? RED : INK;
    let body;
    if (g.length > 1) body = beamSvg(s, g, o, c);
    else if (e.r) body = rest(s, e.x, e.d, c);
    else body = noteSvg(s, e, o, c);
    if (e.gap) out += rect(e.x - OFF + 1, s.hi - 8, e.d * o.u - 2, s.lo - s.hi + 16, 'none', INK, 1.1, 4).replace('/>', ' stroke-dasharray="4 3"/>');
    out += ans(red, body);
  }
  return out;
}
// lay out and draw measures from x0; o: {u (px per sixteenth), beat, stick, pad, padR, bar, final, key, barKey}
function engrave(s, x0, meas, o) {
  let x = x0, out = '';
  const info = [];
  meas.forEach((m, mi) => {
    const mx = x + o.pad;
    let pos = 0;
    const ev = m.map(e => { const z = { ...e, pos, x: mx + pos * o.u + OFF }; pos += e.d; return z; });
    out += drawEvents(s, ev, o);
    x = mx + pos * o.u + o.padR;
    info.push({ mx, x2: x, ev, len: pos });
    const kind = mi === meas.length - 1 ? (o.final || 'single') : (o.bar || 'single');
    if (kind !== 'none') out += bar(s, x, kind);
  });
  return { svg: out, end: x, info };
}
// a whole-note chord (or single note) at x; notes: [{p, a}] where a is the accidental to show (undefined = none)
function chordSvg(s, x, notes, c) {
  const ns = notes.slice().sort((a, b) => a.p - b.p);
  let out = '', col = 0, lastP = null;
  for (const n of ns) out += ledgers(s, x, n.p, c);
  for (let i = ns.length - 1; i >= 0; i--) {
    const n = ns[i];
    if (n.a == null) continue;
    col = lastP != null && lastP - n.p < 6 ? col + 1 : 0;
    out += accG(x - 17 - col * 10, s.y(n.p), n.a, c);
    lastP = n.p;
  }
  for (const n of ns) out += head(x, s.y(n.p), true, c, true);
  return out;
}
// a staff with its clef, key signature and time signature from x1 to x2; returns the staff, the svg and the next free x
function frame(kind, top, x1, x2, o = {}) {
  const s = staff(kind, top);
  let out = staffLines(s, x1, x2), x = x1 + 4;
  if (kind === 'treble') { out += trebleClef(s, x + 11); x += 32; }
  else if (kind === 'bass') { out += bassClef(s, x + 3); x += 34; }
  if (o.key) { const k = keySig(s, x, o.key, o.keyRed ? RED : INK); out += ans(!!o.keyRed, k.svg); x += o.keyW != null ? o.keyW : k.w; }
  if (o.time) { out += timeSig(s, x + 10, o.time[0], o.time[1]); x += 24; }
  if (s.five || kind === 'two' || kind === 'three') out += ln(x1, s.hi, x1, s.lo, INK, 1.2);
  return { s, svg: out, x };
}
// a two-octave keyboard (or nW white keys) from C; marks: [{k: half steps above the first C, key: red on the key}]
const WHITE_OF = [0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6], IS_BLACK = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0];
function keyboard(x, y, nW, marks, w = 15, h = 56) {
  const bw = w * 0.62, bh = h * 0.6;
  let out = '';
  for (let i = 0; i < nW; i++) out += rect(x + i * w, y, w, h, '#fff', INK, 1.1);
  for (let i = 0; i < nW - 1; i++) if ([0, 1, 3, 4, 5].includes(i % 7)) out += rect(x + (i + 1) * w - bw / 2, y, bw, bh, INK);
  for (const m of marks || []) {
    const sm = ((m.k % 12) + 12) % 12, wi = Math.floor(m.k / 12) * 7 + WHITE_OF[sm];
    if (IS_BLACK[sm]) out += ans(m.key, circ(x + (wi + 1) * w, y + bh - 8, 3.6, m.key ? RED : '#fff', '#fff'));
    else out += ans(m.key, circ(x + wi * w + w / 2, y + h - 9, 4.3, m.key ? RED : INK));
  }
  return out;
}

/* ---------- pitch ---------- */
const LET = 'CDEFGAB', NAT = [0, 2, 4, 5, 7, 9, 11];
const accTxt = a => (a === 1 ? '♯' : a === -1 ? '♭' : '');
const nm = n => LET[n.l] + accTxt(n.a);
const midi = n => 12 * (n.o + 1) + NAT[n.l] + n.a;
const dia = n => n.o * 7 + n.l;
const BOT = { treble: 30, bass: 18 };           // the bottom line: E4 and G2
const posOf = (n, clef) => dia(n) - BOT[clef];
const atPos = (p, clef) => { const d = p + BOT[clef]; return { l: ((d % 7) + 7) % 7, o: Math.floor(d / 7), a: 0 }; };
// the note `steps` letters and `semis` half steps above n, or null when it would need a double sharp or flat
function above(n, steps, semis) {
  const d = dia(n) + steps, l = ((d % 7) + 7) % 7, o = Math.floor(d / 7);
  const a = midi(n) + semis - (12 * (o + 1) + NAT[l]);
  return Math.abs(a) > 1 ? null : { l, o, a };
}
const noteOf = (name, o) => ({ l: LET.indexOf(name[0]), a: name.includes('♯') ? 1 : name.includes('♭') ? -1 : 0, o });
const tid = name => name[0].toLowerCase() + (name.includes('♯') ? 's' : name.includes('♭') ? 'b' : '');
// the octave that keeps the notes (letter steps above the root) closest to the middle of the staff
function fitOct(root, steps, clef) {
  let best = null;
  for (let o = 1; o <= 6; o++) {
    const ps = steps.map(st => posOf({ l: root.l, o, a: 0 }, clef) + st);
    const cost = ps.reduce((a, p) => a + (p < 0 ? -p : p > 8 ? p - 8 : 0), 0) * 10 + Math.abs(ps[0] + ps[ps.length - 1] - 8);
    if (!best || cost < best.cost) best = { o, cost };
  }
  return best.o;
}
const PAT = { maj: [2, 2, 1, 2, 2, 2, 1], nmin: [2, 1, 2, 2, 1, 2, 2], hmin: [2, 1, 2, 2, 1, 3, 1], mmin: [2, 1, 2, 2, 2, 2, 1] };
function scaleOf(t, type) {
  if (type === 'penta') { const m = scaleOf(t, 'maj'); return m && [0, 1, 2, 4, 5, 7].map(i => m[i]); }
  const out = [t];
  let cur = t;
  for (const st of PAT[type]) { cur = above(cur, 1, st); if (!cur) return null; out.push(cur); }
  return out;
}
const MAJ = { 0: 'C', 1: 'G', 2: 'D', 3: 'A', 4: 'E', 5: 'B', 6: 'F♯', 7: 'C♯', '-1': 'F', '-2': 'B♭', '-3': 'E♭', '-4': 'A♭', '-5': 'D♭', '-6': 'G♭', '-7': 'C♭' };
const MIN = { 0: 'A', 1: 'E', 2: 'B', 3: 'F♯', 4: 'C♯', 5: 'G♯', 6: 'D♯', 7: 'A♯', '-1': 'D', '-2': 'G', '-3': 'C', '-4': 'F', '-5': 'B♭', '-6': 'E♭', '-7': 'A♭' };
const sigOfMajor = name => +Object.keys(MAJ).find(k => MAJ[k] === name);

/* ---------- rhythm ---------- */
// durations in sixteenths: 16 whole, 12 dotted half, 8 half, 6 dotted quarter, 4 quarter, 2 eighth, 1 sixteenth
const METER = { 4: [4, 4, 16], 3: [3, 4, 12], 2: [2, 4, 8], 6: [6, 8, 12] };
const CELL = {
  q: [[4]], ee: [[2], [2]], qr: [[4, 1]], h: [[8]], hr: [[8, 1]], w: [[16]], dh: [[12]],
  ssss: [[1], [1], [1], [1]], ess: [[2], [1], [1]], sse: [[1], [1], [2]], dqe: [[6], [2]], syn: [[2], [4], [2]], ere: [[2, 1], [2]],
  dq: [[6]], eee: [[2], [2], [2]], qe: [[4], [2]], eq: [[2], [4]], dqr: [[6, 1]], dh6: [[12]],
};
const clen = k => CELL[k].reduce((a, e) => a + e[0], 0);
const FEAT = { six: ['ssss', 'ess', 'sse'], dot: ['dh', 'w'], dotq: ['dqe'], sync: ['syn'] };
function pool(lvl, m, focus) {
  if (m === '6') return { cells: [['dq', 3], ['eee', 3], ['qe', 3], ['dqr', 1], ['dh6', 1]].concat(lvl >= 6 ? [['eq', 2]] : []), feat: [] };
  const base = [['q', 4], ['ee', 3], ['qr', 1]];
  if (lvl >= 2) base.push(['h', 2]);
  if (focus && focus !== 'all' && FEAT[focus]) return { cells: base.concat(FEAT[focus].map(k => [k, 3])), feat: FEAT[focus] };
  if (lvl >= 3) base.push(['hr', 1], ['w', 1]);
  if (lvl >= 4) base.push(['dh', 1], ['ssss', 2], ['ess', 1], ['sse', 1]);
  if (lvl >= 5) base.push(['dqe', 2]);
  if (lvl >= 6) base.push(['syn', 2], ['ere', 1]);
  return { cells: base, feat: [] };
}
function fits(k, pos, T) {
  const n = clen(k);
  if (pos + n > T) return false;
  if (n === 16) return pos === 0;
  if (n === 12 && T !== 12) return pos === 0 || pos === 4;
  if (n === 12) return pos === 0;
  if (n === 8 && T === 16) return pos % 8 === 0;
  return true;
}
function wpick(r, arr) {
  let t = r.next() * arr.reduce((a, x) => a + x[1], 0);
  for (const [k, w] of arr) { t -= w; if (t < 0) return k; }
  return arr[arr.length - 1][0];
}
const toEv = cells => cells.flatMap(k => CELL[k].map(([d, rr]) => ({ d, r: !!rr })));
function measure(r, P, T, lvl, needRest) {
  let cells = [];
  for (let t = 0; t < 80; t++) {
    let pos = 0;
    cells = [];
    while (pos < T) { const c = P.cells.filter(([k]) => fits(k, pos, T)); if (!c.length) break; const k = wpick(r, c); cells.push(k); pos += clen(k); }
    if (pos !== T) continue;
    const rests = cells.filter(k => CELL[k].some(e => e[1])).length;
    if (rests === cells.length || rests > (lvl <= 3 ? 1 : 2) || (needRest && !rests)) continue;
    return { cells, ev: toEv(cells) };
  }
  cells = T === 12 && P.cells.some(c => c[0] === 'dq') ? ['dq', 'dq'] : Array(T / 4).fill('q');
  if (needRest) cells[cells.length - 1] = cells[0] === 'dq' ? 'dqr' : 'qr';
  return { cells, ev: toEv(cells) };
}
const enc = ev => ev.map(e => (e.r ? 'r' : '') + e.d).join(' ');
function rline(r, P, T, n, lvl) {
  let ms = [];
  for (let t = 0; t < 40; t++) {
    ms = Array.from({ length: n }, () => measure(r, P, T, lvl));
    if (P.feat.length && !ms.some(m => m.cells.some(k => P.feat.includes(k)))) continue;
    if (n > 1 && ms.every(m => enc(m.ev) === enc(ms[0].ev))) continue;
    break;
  }
  return ms;
}
// counts under each note: 1 e & a in simple meters, 1 to 6 in 6/8; held beats and rests in parentheses
function countLabels(ev, m) {
  const out = [], comp = m === '6';
  let pos = 0;
  for (const e of ev) {
    const lab = comp ? String(pos / 2 + 1) : pos % 4 === 0 ? String(pos / 4 + 1) : ['', 'e', '&', 'a'][pos % 4];
    out.push({ pos, t: e.r ? `(${lab})` : lab });
    for (let t = pos + 1; t < pos + e.d; t++) if (t % (comp ? 2 : 4) === 0) out.push({ pos: t, t: `(${comp ? t / 2 + 1 : t / 4 + 1})` });
    pos += e.d;
  }
  return out;
}
const SYL = { 4: 'ta', 2: 'ti', 8: 'ta-a' };
const sylLabels = ev => { let pos = 0; return ev.map(e => { const z = { pos, t: e.r ? 'rest' : SYL[e.d] }; pos += e.d; return z; }); };
const VAL = { 16: 'whole', 12: 'dotted half', 8: 'half', 6: 'dotted quarter', 4: 'quarter', 2: 'eighth', 1: 'sixteenth' };
function beatsTxt(sixteenths, m) {
  if (m === '6') { const n = sixteenths / 2; return `${n} eighth${n === 1 ? '' : 's'}`; }
  const b = sixteenths / 4, w = Math.floor(b), fr = { 0: '', 0.25: '1/4', 0.5: '1/2', 0.75: '3/4' }[b - w];
  const t = w && fr ? `${w} ${fr}` : w ? String(w) : fr;
  return `${t} beat${b === 1 ? '' : 's'}`;
}
// a rhythm on one line (or stick notation): returns the svg body, its width and height
function rhythmBody(ms, m, o) {
  const s = staff(o.stick ? 'none' : 'one', o.stick ? 52 : 46);
  const x0 = o.x0 ?? 26;
  let body = '';
  if (o.num != null) body += tx(x0 - 22, s.top + 5, o.num + '.', INK, 14, 'start', true);
  const ts = timeSig(s, x0 + 10, METER[m][0], METER[m][1]);
  const e = engrave(s, x0 + 20, ms.map(x => x.ev || x), { u: o.u, beat: m === '6' ? 6 : 4, stick: o.stick, pad: o.stick ? 14 : 6, padR: 6, final: o.final || 'final', key: o.red });
  if (!o.stick) body += ln(x0, s.top, e.end, s.top, INK, 1.1);
  body += ts + e.svg;
  const ly = s.top + (o.stick ? 24 : 32);
  if (o.labels) {
    body += ln(x0 + 22, ly + 5, e.end, ly + 5, '#bbb', 0.8);
    let t = '';
    e.info.forEach(mi => { for (const L of (o.labels === 'syl' ? sylLabels : x => countLabels(x, m))(mi.ev)) t += tx(mi.mx + L.pos * o.u + OFF, ly, L.t, RED, o.u >= 14 ? 12 : 11); });
    body += ans(true, t);
  }
  return { body, end: e.end, info: e.info, s, h: o.labels ? ly + 12 : s.lo + 10 };
}
const rhythmText = (ms, m, mode) => ms.map(x => (mode === 'syl' ? sylLabels(x.ev || x) : countLabels(x.ev || x, m)).map(L => L.t).join(' ')).join(' | ');

/* ---------- grades, skills, settings ---------- */
const GRADES = [['k', 'Kindergarten'], ['1', 'Grade 1'], ['2', 'Grade 2'], ['3', 'Grade 3'], ['4', 'Grade 4'], ['5', 'Grade 5'], ['6', 'Grade 6'],
  ['7', 'Grade 7'], ['8', 'Grade 8'], ['9', 'Grade 9'], ['10', 'Grade 10'], ['11', 'Grade 11'], ['12', 'Grade 12']];
const gn = g => (g === 'k' ? 0 : +g);
const SK = [['rhythm', 0, 12], ['listen', 0, 3], ['dictate', 3, 8], ['complete', 2, 8], ['barlines', 2, 5], ['fix', 2, 6], ['rests', 1, 5],
  ['solfa', 1, 3], ['motion', 2, 4], ['names', 3, 12], ['words', 3, 5], ['draw', 3, 12], ['steps', 4, 6], ['scales', 3, 12], ['keysig', 5, 12],
  ['intervals', 5, 12], ['triads', 6, 12], ['inversions', 7, 12], ['diatonic', 7, 12], ['symbols', 8, 12], ['staff', 1, 12]];
function skillName(id, g) {
  switch (id) {
    case 'rhythm': return g === 0 ? 'Read a rhythm and count the sounds' : g <= 2 ? 'Read a rhythm and write ta and ti-ti' : 'Read a rhythm and write the counts';
    case 'listen': return 'Which rhythm did I clap? (teacher claps)';
    case 'dictate': return 'Rhythm dictation (teacher claps, students write)';
    case 'complete': return 'Complete the measure (add one note or rest)';
    case 'barlines': return 'Add the bar lines';
    case 'fix': return 'Find and fix measures with the wrong number of beats';
    case 'rests': return g === 1 ? 'Find the quarter rests' : 'Rests and how long they last';
    case 'solfa': return g === 1 ? 'So and mi on a 2-line staff' : g === 2 ? 'So, mi and la on a 3-line staff' : 'Do, re, mi, so and la on the staff';
    case 'motion': return 'Steps, skips and repeats';
    case 'names': return 'Name the notes';
    case 'words': return 'Note-name words (decode words written in notes)';
    case 'draw': return 'Draw the note for each letter';
    case 'steps': return 'Whole steps and half steps on the keyboard';
    case 'scales': return 'Build scales on the staff';
    case 'keysig': return 'Key signatures';
    case 'intervals': return g <= 6 ? 'Intervals (number)' : 'Intervals (quality and number)';
    case 'triads': return 'Triads: build and name';
    case 'inversions': return 'Triad inversions';
    case 'diatonic': return 'Chords of the key with Roman numerals';
    case 'symbols': return 'Chord symbols to notes';
    default: return 'Composition staff paper';
  }
}
const skillOpts = v => { const g = gn(v.grade); return SK.filter(x => g >= x[1] && g <= x[2]).map(x => [x[0], skillName(x[0], g)]); };
const RHY = ['rhythm', 'listen', 'dictate', 'complete', 'barlines', 'fix', 'staff'];
function meterOpts(v) {
  const g = gn(v.grade), sk = v.skill;
  if (g === 0) return [['4', '4/4 (four beats)']];
  const all = [['4', '4/4 (four beats)'], ['3', '3/4 (three beats)'], ['2', '2/4 (two beats)']];
  const list = g <= 2 ? [all[0], all[2]] : all.slice();
  const six = g >= 5 && ['rhythm', 'dictate', 'complete', 'staff'].includes(sk);
  if (six) list.push(['6', '6/8 (two beats of three eighths)']);
  if (sk !== 'staff') list.push(['mix', g <= 2 ? 'Mix of 2/4 and 4/4' : six ? 'Mix of meters, with 6/8' : 'Mix of 2/4, 3/4 and 4/4']);
  return list;
}
const meterList = (v, g) => { const o = meterOpts(v).map(x => x[0]).filter(x => x !== 'mix'); return v.meter === 'mix' ? o : [v.meter]; };
function focusOpts(v) {
  const g = gn(v.grade), o = [['all', 'All note values for the grade'], ['six', 'Sixteenth notes (1 e & a)']];
  if (v.meter !== '2') o.push(['dot', 'Half, dotted half and whole notes']);
  if (g >= 5) o.push(['dotq', 'Dotted quarter and eighth']);
  if (g >= 6) o.push(['sync', 'Syncopation (eighth, quarter, eighth)']);
  return o;
}
const hasFocus = v => ['rhythm', 'dictate'].includes(v.skill) && gn(v.grade) >= 4 && v.meter !== '6';
const CLEFS = { treble: 'Treble clef', bass: 'Bass clef', both: 'Treble and bass, mixed', grand: 'Grand staff (both, joined at middle C)' };
function clefOpts(v) {
  const g = gn(v.grade);
  if (g < 5) return [['treble', CLEFS.treble]];
  const o = [['treble', CLEFS.treble], ['bass', CLEFS.bass], ['both', CLEFS.both]];
  if (v.skill === 'names') o.push(['grand', CLEFS.grand]);
  return o;
}
const hasClef = v => ['names', 'draw', 'keysig', 'intervals', 'triads', 'inversions', 'symbols', 'scales'].includes(v.skill);
function scaleOpts(v) {
  const g = gn(v.grade), o = [['maj', 'Major']];
  if (g >= 5) o.push(['nmin', 'Natural minor']);
  if (g >= 9) o.push(['hmin', 'Harmonic minor'], ['mmin', 'Melodic minor (ascending)'], ['forms', 'Three forms of minor (natural, harmonic, melodic)']);
  if (g >= 6) o.push(['penta', 'Major pentatonic']);
  return o;
}
function tonics(g, type) {
  if (type === 'maj') return g <= 3 ? ['C', 'G', 'F'] : g === 4 ? ['C', 'G', 'F', 'D', 'B♭'] : g === 5 ? ['C', 'G', 'F', 'D', 'B♭', 'A', 'E♭'] : g <= 8 ? ['C', 'G', 'F', 'D', 'B♭', 'A', 'E♭', 'E', 'A♭'] : ['C', 'G', 'F', 'D', 'B♭', 'A', 'E♭', 'E', 'A♭', 'B', 'D♭', 'F♯', 'G♭'];
  if (type === 'nmin') return g === 5 ? ['A', 'D', 'E'] : g <= 8 ? ['A', 'D', 'E', 'B', 'G', 'C'] : ['A', 'D', 'E', 'B', 'G', 'C', 'F♯', 'C♯', 'F', 'B♭'];
  if (type === 'penta') return ['C', 'G', 'F', 'D', 'A'];
  return ['A', 'D', 'E', 'B', 'G', 'C', 'F♯', 'F'];
}
const TYPE_NAME = { maj: 'major', nmin: 'natural minor', hmin: 'harmonic minor', mmin: 'melodic minor', forms: 'minor', penta: 'major pentatonic' };
const DIA_KEYS = g => (g === 7 ? ['C', 'G', 'F', 'D', 'B♭'] : g === 8 ? ['C', 'G', 'F', 'D', 'B♭', 'A', 'E♭'] : ['C', 'G', 'F', 'D', 'B♭', 'A', 'E♭', 'E', 'A♭']);
function tonicOpts(v) {
  const g = gn(v.grade);
  if (v.skill === 'diatonic') { const l = DIA_KEYS(g); return [['any', 'Any (changes with each sheet)'], ['first', `The easiest keys first (${l.slice(0, 3).join(', ')})`]].concat(l.map(t => [tid(t), `${t} major`])); }
  const l = tonics(g, v.scale === 'forms' ? 'hmin' : v.scale);
  return [['any', 'Any (changes with each sheet)'], ['first', `The easiest first (${l.slice(0, 3).join(', ')})`]].concat(l.map(t => [tid(t), `${t} ${TYPE_NAME[v.scale]}`]));
}
function keysOpts(v) {
  const g = gn(v.grade);
  if (g === 5) return [['maj', 'Major keys'], ['rel', 'Major and relative minor']];
  return [['maj', 'Major keys'], ['min', 'Minor keys'], ['rel', 'Major and relative minor'], ['mix', 'Mixed: each one asks major or minor']];
}
function linesOpts(v) {
  const g = gn(v.grade);
  if (g === 1) return [['two', '2-line staff (so and mi)'], ['rhythm', 'Rhythm line (no pitches)']];
  if (g === 2) return [['three', '3-line staff (so, mi and la)'], ['rhythm', 'Rhythm line (no pitches)']];
  return [['treble', 'Treble staff'], ['bass', 'Bass staff'], ['grand', 'Grand staff'], ['rhythm', 'Rhythm line (no pitches)']];
}
const barsOpts = v => (gn(v.grade) <= 2 ? [['1', '1 measure'], ['2', '2 measures'], ['4', '4 measures'], ['8', '8 measures']] : [['4', '4 measures'], ['8', '8 measures'], ['16', '16 measures']]);
function countOpts(v) {
  const g = gn(v.grade), sk = v.skill;
  const L = (a, b, c, unit) => [['s', `Fewer (${a}${unit ? ' ' + unit : ''})`], ['m', `Standard (${b}${unit ? ' ' + unit : ''})`], ['l', `More (${c}${unit ? ' ' + unit : ''})`]];
  const c = COUNT[sk](g);
  return L(c.s, c.m, c.l, c.unit);
}
const COUNT = {
  rhythm: g => (g === 0 ? { s: 4, m: 5, l: 6, unit: 'rows' } : { s: 4, m: 6, l: 8, unit: 'lines' }),
  listen: g => (g === 0 ? { s: 3, m: 4, l: 5, unit: 'rows' } : { s: 4, m: 5, l: 6, unit: 'rows' }),
  dictate: () => ({ s: 3, m: 4, l: 6, unit: 'rhythms' }),
  complete: () => ({ s: 6, m: 8, l: 12, unit: 'measures' }),
  barlines: () => ({ s: 3, m: 4, l: 6, unit: 'lines' }),
  fix: () => ({ s: 6, m: 10, l: 12, unit: 'measures' }),
  rests: g => (g === 1 ? { s: 4, m: 5, l: 6, unit: 'rows' } : { s: 3, m: 4, l: 6, unit: 'measures' }),
  solfa: () => ({ s: 4, m: 6, l: 8, unit: 'patterns' }),
  motion: () => ({ s: 2, m: 3, l: 4, unit: 'melodies' }),
  names: g => (g >= 9 ? { s: 12, m: 16, l: 24, unit: 'notes' } : { s: 8, m: 12, l: 16, unit: 'notes' }),
  words: () => ({ s: 6, m: 8, l: 10, unit: 'words' }),
  draw: () => ({ s: 8, m: 12, l: 16, unit: 'notes' }),
  steps: () => ({ s: 6, m: 10, l: 12, unit: 'pairs' }),
  scales: () => ({ s: 1, m: 2, l: 3, unit: 'scales' }),
  keysig: g => (g === 5 ? { s: 6, m: 8, l: 10, unit: '' } : { s: 12, m: 18, l: 28, unit: '' }),
  intervals: () => ({ s: 10, m: 14, l: 18, unit: '' }),
  triads: () => ({ s: 8, m: 12, l: 16, unit: '' }),
  inversions: () => ({ s: 8, m: 12, l: 18, unit: '' }),
  diatonic: () => ({ s: 1, m: 2, l: 3, unit: 'keys' }),
  symbols: () => ({ s: 6, m: 10, l: 12, unit: 'chords' }),
  staff: () => ({ s: 1, m: 1, l: 1, unit: '' }),
};

/* ---------- the skills: each returns {title, parts, items, ...} ---------- */
const grid = (cells, n, cls = '') => `<div class="mu-grid${cls ? ' ' + cls : ''}" style="--n:${n}">${cells.join('')}</div>`;
const cell = (n, html, cap) => `<div class="mu-cell"><p class="mu-cap"><span class="ws-num">${n}.</span>${cap ? ' ' + cap : ''}</p>${html}</div>`;
const pickMeter = (r, v, g) => { const l = meterList(v, g), nd = l.filter(m => m !== '2'); return r.pick(hasFocus(v) && v.focus === 'dot' && nd.length ? nd : l); };   // the dotted-half focus skips 2/4
const meterTxt = m => `${METER[m][0]}/${METER[m][1]}`;

function mkRhythm(v, r, g) {
  const lvl = Math.min(g, 6), stick = g <= 2, n = COUNT.rhythm(g)[v.count];
  const mode = g === 0 ? 'sounds' : g <= 2 ? 'syl' : 'count';
  const lines = r.distinct(n, () => {
    const m = g === 0 ? '4' : pickMeter(r, v, g), T = METER[m][2];
    const P = pool(lvl, m, hasFocus(v) ? (v.focus === 'dot' && m === '2' ? 'all' : v.focus) : 'all');
    const six = P.cells.some(c => c[1] && FEAT.six.includes(c[0]));
    const u = g === 0 ? 15 : stick ? 12 : six ? 15 : 10;
    const per = g === 0 ? 1 : g === 1 ? T / 8 : g === 2 ? Math.min(4, 32 / T) : Math.max(1, Math.min(4, Math.floor(560 / (T * u + 12))));
    return { m, u, ms: rline(r, P, T, per, lvl) };
  }, L => L.m + ':' + L.ms.map(x => enc(x.ev)).join('|'));
  const items = [], rows = [];
  lines.forEach((L, i) => {
    const sounds = L.ms.reduce((a, x) => a + x.ev.filter(e => !e.r).length, 0);
    const R = rhythmBody(L.ms, L.m, { u: L.u, stick, num: i + 1, labels: mode === 'sounds' ? null : mode });
    let body = R.body, w = R.end + 10;
    if (mode === 'sounds') { body += tx(w + 14, R.s.top - 8, 'Sounds:', INK, 14, 'start') + wline(w + 100, R.s.top - 8, 40) + ans(true, tx(w + 100, R.s.top - 11, String(sounds), RED, 17, 'middle', true)); w += 130; }
    rows.push(`<div class="mu-line">${svg(w, R.h, body, `Rhythm line ${i + 1} in ${meterTxt(L.m)}`, g === 0 ? 1.15 : 1)}</div>`);
    items.push({ q: `${i + 1}. ${meterTxt(L.m)}: ${L.ms.map(x => enc(x.ev)).join(' | ')}`, a: mode === 'sounds' ? String(sounds) : rhythmText(L.ms, L.m, mode), k: 'cnt', mode, m: L.m, ms: L.ms.map(x => x.ev) });
  });
  const parts = [part('', rows.join(''))];
  if (v.fixpart && g >= 3) { const f = fixBlock(r, v, g, 4, items.length + 1); parts.push(part('Fix the measures', f.html)); items.push(...f.items); }
  return { parts, items };
}

function mkListen(v, r, g) {
  const n = COUNT.listen(g)[v.count], stick = g <= 2, lvl = Math.min(g, 3);
  const items = [], rows = [], clap = [];
  for (let i = 0; i < n; i++) {
    const m = g <= 1 ? '4' : pickMeter(r, v, g), T = METER[m][2], P = pool(lvl, m, 'all');
    const ch = r.distinct(3, () => measure(r, P, T, lvl), x => enc(x.ev));
    if (ch.length < 3) continue;
    if (items.some(it => it.ch.join('/') === ch.map(x => enc(x.ev)).join('/'))) { i--; continue; }
    const idx = r.int(0, 2), u = stick ? 11 : 9, cw = T * u + 96;
    let body = '';
    ch.forEach((x, j) => {
      const R = rhythmBody([x], m, { u, stick, x0: j * cw + 26 });
      body += tx(j * cw + 6, R.s.top - 20, 'ABC'[j], INK, 15, 'start', true) + R.body;
      if (j === idx) body += ans(true, rect(j * cw + 2, 6, cw - 8, R.h - 2, 'none', RED, 2.4, 10));
    });
    rows.push(`<div class="mu-line mu-listen"><span class="ws-num">${i + 1}.</span>${svg(3 * cw, 76, body, `Row ${i + 1}: three rhythms in ${meterTxt(m)}, A, B and C`, g === 0 ? 1.1 : 1)}</div>`);
    const said = rhythmText([ch[idx]], m, g <= 2 ? 'syl' : 'count');
    clap.push(`<li>Row ${i + 1}: clap ${'ABC'[idx]}, <i>${esc(said)}</i></li>`);
    items.push({ q: `Row ${i + 1}: ${ch.map(x => enc(x.ev)).join(' / ')}`, a: 'ABC'[idx], k: 'listen', m, idx, ch: ch.map(x => enc(x.ev)), chev: ch.map(x => x.ev) });
  }
  return { parts: [part('', rows.join(''))], items, teacher: `<h3>What to clap</h3><p>Clap each row twice at a steady tempo, saying nothing. Students circle the letter of the rhythm you clapped.</p><ol class="mu-tlist">${clap.join('')}</ol>` };
}

function mkDictate(v, r, g) {
  const n = COUNT.dictate(g)[v.count], lvl = Math.min(g, 6);
  const its = r.distinct(n, () => {
    const m = pickMeter(r, v, g), T = METER[m][2], P = pool(lvl, m, hasFocus(v) ? (v.focus === 'dot' && m === '2' ? 'all' : v.focus) : 'all');
    return { m, ms: rline(r, P, T, T <= 8 ? 4 : 2, lvl) };
  }, L => L.m + L.ms.map(x => enc(x.ev)).join('|'));
  const items = [], rows = [], clap = [];
  its.forEach((L, i) => {
    const six = L.ms.some(x => x.ev.some(e => e.d === 1));
    const R = rhythmBody(L.ms, L.m, { u: six ? 15 : 12, num: i + 1, red: true });
    rows.push(`<div class="mu-line">${svg(R.end + 10, R.h + 4, R.body, `Empty measures in ${meterTxt(L.m)} for rhythm ${i + 1}`)}</div>`);
    const said = rhythmText(L.ms, L.m, 'count');
    clap.push(`<li>${meterTxt(L.m)}: <i>${esc(said)}</i></li>`);
    items.push({ q: `${i + 1}. ${meterTxt(L.m)} ${L.ms.map(x => enc(x.ev)).join(' | ')}`, a: said, k: 'cnt', mode: 'count', m: L.m, ms: L.ms.map(x => x.ev) });
  });
  return { parts: [part('', rows.join(''))], items, teacher: `<h3>What to clap</h3><p>Say the time signature, count one measure aloud, then clap each rhythm three times. The counts are written under the notes on the key.</p><ol class="mu-tlist">${clap.join('')}</ol>` };
}

const GAPS = g => (g <= 2 ? [4, 8] : g === 3 ? [2, 4, 8] : g === 4 ? [2, 4, 8, 12] : [2, 4, 6, 8, 12]);
const valueTxt = d => (d === 6 || d === 12 ? `${VAL[d]} note` : `${VAL[d]} note or ${VAL[d]} rest`);
function mkComplete(v, r, g) {
  const n = COUNT.complete(g)[v.count], lvl = Math.min(g, 6), stick = g <= 2;
  const ms = r.distinct(n, () => {
    const m = pickMeter(r, v, g), T = METER[m][2], P = pool(lvl, m, 'all');
    const x = measure(r, P, T, lvl);
    const can = x.ev.map((e, i) => i).filter(i => GAPS(g).includes(x.ev[i].d) && !(x.ev[i].r && x.ev[i].d === 16));
    if (x.ev.length < 3 || !can.length) return null;
    return { m, ev: x.ev, gi: r.pick(can) };
  }, x => x.m + enc(x.ev) + x.gi);
  const items = [], cells = [];
  ms.forEach((x, i) => {
    const ev = x.ev.map((e, j) => (j === x.gi ? { ...e, gap: true } : e));
    const R = rhythmBody([ev], x.m, { u: stick ? 12 : 11, stick });
    const d = x.ev[x.gi].d, a = `${valueTxt(d)} (${beatsTxt(d, x.m)})`;
    cells.push(cell(i + 1, svg(R.end + 8, R.h + 2, R.body, `A measure of ${meterTxt(x.m)} with one empty box`) + `<p class="mu-ans">Missing: ${blank(a, 11)}</p>`));
    items.push({ q: `${i + 1}. ${meterTxt(x.m)} ${enc(x.ev)} gap ${x.gi}`, a, k: 'comp', m: x.m, ev: x.ev, gi: x.gi });
  });
  return { parts: [part('', grid(cells, 2))], items };
}

function mkBarlines(v, r, g) {
  const n = COUNT.barlines(g)[v.count], lvl = Math.min(g, 6), stick = g <= 2, u = stick ? 12 : 11;
  const its = r.distinct(n, () => {
    const m = pickMeter(r, v, g), T = METER[m][2], P = pool(lvl, m, 'all');
    const k = { 16: 3, 12: 4, 8: 5 }[T] - (stick && T === 16 ? 1 : 0);
    const ms = rline(r, P, T, k, lvl);
    let ev = ms.flatMap(x => x.ev), short = 0;
    if (g >= 3 && r.chance(0.5) && ms[k - 1].ev.length >= 2) { const last = ev[ev.length - 1]; if (GAPS(g).includes(last.d) && !last.r) { short = last.d; ev = ev.slice(0, -1); } }
    return { m, ev, short };
  }, x => x.m + enc(x.ev));
  const items = [], rows = [];
  its.forEach((x, i) => {
    const T = METER[x.m][2], s = staff(stick ? 'none' : 'one', stick ? 52 : 46);
    const e = engrave(s, 46, [x.ev], { u, beat: 4, stick, pad: 6, padR: 14, final: 'none' });
    let body = tx(4, s.top + 5, (i + 1) + '.', INK, 14, 'start', true) + timeSig(s, 36, METER[x.m][0], METER[x.m][1]) + e.svg;
    if (!stick) body = ln(26, s.top, e.end + 4, s.top, INK, 1.1) + body;
    let pos = 0, red = '';
    const after = [];
    x.ev.forEach((ev, j) => { pos += ev.d; if (pos % T === 0 && j < x.ev.length - 1) { after.push(j + 1); red += bar(s, e.info[0].mx + pos * u + 1, 'single', RED); } });
    red += bar(s, e.end + 2, 'final', RED);
    body += ans(true, red);
    let a = `bar lines after notes ${after.join(', ')}; double bar at the end`;
    if (x.short) a += `; the last measure needs ${beatsTxt(x.short, x.m)}: add a ${valueTxt(x.short)}`;
    const h = s.lo + 14;
    rows.push(`<div class="mu-line">${svg(e.end + 12, h, body, `Rhythm line ${i + 1} in ${meterTxt(x.m)} with no bar lines`)}${x.short ? key(`<p class="mu-ans" style="color:${RED}">The last measure is short: add a ${esc(valueTxt(x.short))} (${esc(beatsTxt(x.short, x.m))}).</p>`) : ''}</div>`);
    items.push({ q: `${i + 1}. ${meterTxt(x.m)} ${enc(x.ev)}`, a, k: 'bars', m: x.m, ev: x.ev, short: x.short, after });
  });
  return { parts: [part('', rows.join(''))], items };
}

// measures to check: some have one note or rest too many or too few
function fixBlock(r, v, g, n, start) {
  const lvl = Math.min(g, 6), stick = g <= 2, wrongN = Math.round(n * (n >= 12 ? 0.67 : 0.6));
  const ms = meterList(v, g).filter(m => m !== '6');
  const meters = ms.length ? ms : ['4'];
  const wrong = new Set(r.sample(Array.from({ length: n }, (_, i) => i), wrongN));
  const list = r.distinct(n, () => {
    const m = r.pick(meters), T = METER[m][2], P = pool(Math.min(lvl, 3), m, 'all'), x = measure(r, P, T, Math.min(lvl, 3));
    return { m, ev: x.ev, T };
  }, x => x.m + enc(x.ev));
  const items = [], cells = [];
  list.forEach((x, i) => {
    let ev = x.ev, fixTxt = '';
    if (wrong.has(i)) {
      const can = ev.map((e, j) => j).filter(j => ev[j].d === 4 || ev[j].d === 8);
      if (can.length && ev.length > 2 && r.chance(0.5)) { const j = r.pick(can); fixTxt = `add a ${VAL[ev[j].d]} note or rest`; ev = ev.filter((e, k) => k !== j); }
      else { const add = r.pick(x.T - 4 >= 4 ? [4, 4, 8] : [4]), at = r.int(0, ev.length); ev = ev.slice(0, at).concat([{ d: add, r: false }], ev.slice(at)); fixTxt = `take away a ${VAL[add]} note, or change a note to make ${METER[x.m][0]} beats`; }
    }
    const tot = ev.reduce((a, e) => a + e.d, 0), bad = tot !== x.T;
    const R = rhythmBody([ev], x.m, { u: stick ? 11 : 10, stick });
    let body = R.body;
    if (bad) body += ans(true, rect(R.info[0].mx - 4, 4, R.end - R.info[0].mx + 8, R.h - 6, 'none', RED, 2.2, 14));
    const a = beatsTxt(tot, x.m);
    cells.push(cell(start + i, svg(R.end + 8, R.h + 2, body, `Measure ${start + i} in ${meterTxt(x.m)}`) + `<p class="mu-ans">Beats: ${blank(a, 6)} ${bad ? key(`<b style="color:${RED}">Wrong: ${esc(fixTxt)}</b>`) : key(`<b style="color:${RED}">Right</b>`)}</p>`));
    items.push({ q: `${start + i}. ${meterTxt(x.m)} ${enc(ev)}`, a, k: 'fix', m: x.m, ev, bad });
  });
  return { html: grid(cells, 2), items };
}
const mkFix = (v, r, g) => { const f = fixBlock(r, v, g, COUNT.fix(g)[v.count], 1); return { parts: [part('', f.html)], items: f.items }; };

function mkRests(v, r, g) {
  const items = [];
  if (g === 1) {
    const n = COUNT.rests(g)[v.count], P = pool(1, '4', 'all'), rows = [];
    const ms = r.distinct(n, () => measure(r, P, 16, 4, true), x => enc(x.ev));
    ms.forEach((x, i) => {
      const R = rhythmBody([x], '4', { u: 14, stick: true, num: i + 1 });
      let pos = 0, red = '';
      const beats = [];
      for (const e of x.ev) { if (e.r) { beats.push(pos / 4 + 1); red += `<ellipse cx="${f1(R.info[0].mx + pos * 14 + OFF)}" cy="${f1(R.s.mid)}" rx="13" ry="20" fill="none" stroke="${RED}" stroke-width="2.2"/>`; } pos += e.d; }
      const a = `beat${beats.length > 1 ? 's' : ''} ${beats.join(' and ')}`;
      rows.push(`<div class="mu-line mu-row">${svg(R.end + 8, R.h + 4, R.body + ans(true, red), `Rhythm ${i + 1}, four beats`, 1.1)}<p class="mu-ans">Rest on ${blank(a, 7)}</p></div>`);
      items.push({ q: `${i + 1}. ${enc(x.ev)}`, a, k: 'restbeat', ev: x.ev });
    });
    const s = staff('none', 14);
    let tr = '';
    for (let i = 0; i < 4; i++) tr += `<g transform="translate(${40 + i * 70} 44) scale(1.8)">${rest(s, 0, 4, GREY).replace('stroke-width="2.6"', 'stroke-width="1.6" stroke-dasharray="2.5 2"')}</g>`;
    for (let i = 0; i < 4; i++) tr += rect(300 + i * 72, 12, 56, 60, 'none', GREY, 1, 6).replace('/>', ' stroke-dasharray="4 3"/>');
    return { parts: [part('', rows.join('')), part('Trace, then draw your own', svg(600, 80, tr, 'Four dotted quarter rests to trace and four spaces to draw your own', 1.1))], items };
  }
  // note values and their rests, then beats of silence in measures
  const vals = g === 3 ? [16, 8, 4, 2] : g === 4 ? [16, 12, 8, 4, 2, 1] : [16, 12, 8, 6, 4, 2, 1];
  const order = r.shuffle(vals), cellsA = [];
  order.forEach((d, i) => {
    const s = staff('one', 46);
    let body = ln(6, s.top, 150, s.top, INK, 1.1) + noteSvg(s, { d, x: 34, p: 4 }, {}, INK);
    body += tx(66, s.top + 5, '→', INK, 16) + rect(86, s.top - 26, 48, 46, 'none', GREY, 1, 4) + ans(true, rest(s, 110, d, RED));
    const a = `${VAL[d]} rest, ${beatsTxt(d, '4')}`;
    cellsA.push(cell(i + 1, svg(156, 76, body, `A ${VAL[d]} note and an empty box`) + `<p class="mu-ans">Beats: ${blank(beatsTxt(d, '4'), 5)}</p>`));
    items.push({ q: `${i + 1}. ${VAL[d]} note`, a, k: 'restval', d });
  });
  const n = COUNT.rests(g)[v.count], lvl = Math.min(g, 6), cellsB = [];
  const ms = r.distinct(n, () => { const m = r.pick(meterList({ ...v, meter: 'mix' }, g).filter(x => x !== '6')); return { m, ...measure(r, pool(lvl, m, 'all'), METER[m][2], lvl, true) }; }, x => x.m + enc(x.ev));
  ms.forEach((x, i) => {
    const R = rhythmBody([x], x.m, { u: g >= 4 ? 13 : 11 });
    const sil = x.ev.filter(e => e.r).reduce((a, e) => a + e.d, 0), a = beatsTxt(sil, x.m);
    cellsB.push(cell(order.length + i + 1, svg(R.end + 8, R.h + 2, R.body, `Measure in ${meterTxt(x.m)}`) + `<p class="mu-ans">Silence: ${blank(a, 6)}</p>`));
    items.push({ q: `${order.length + i + 1}. ${meterTxt(x.m)} ${enc(x.ev)}`, a, k: 'silence', m: x.m, ev: x.ev });
  });
  return { parts: [part('Draw the matching rest', grid(cellsA, 4)), part('Beats of silence', grid(cellsB, 2))], items };
}

// so-mi (2-line), so-mi-la (3-line) and do-re-mi-so-la (5-line, do on the G line)
const SOLFA = { two: { 0: 'mi', 2: 'so' }, three: { 0: 'mi', 2: 'so', 3: 'la' }, treble: { 2: 'do', 3: 're', 4: 'mi', 6: 'so', 7: 'la' } };
function mkSolfa(v, r, g) {
  const kind = g === 1 ? 'two' : g === 2 ? 'three' : 'treble', map = SOLFA[kind], ps = Object.keys(map).map(Number);
  const n = COUNT.solfa(g)[v.count], len = g === 1 ? 4 : g === 2 ? 5 : 6;
  const pats = r.distinct(n, () => {
    const x = Array.from({ length: len }, () => r.pick(ps));
    return new Set(x).size >= Math.min(ps.length, g === 1 ? 2 : 3) ? x : null;
  }, x => x.join(','));
  const items = [], cells = [];
  pats.forEach((pat, i) => {
    const top = kind === 'treble' ? 30 : 34, F = frame(kind, top, 4, 300);
    let body = F.svg;
    if (kind === 'treble') body += tx(F.x + 4, F.s.y(2) + 4, 'do', INK, 10, 'start', true) + ln(F.x + 18, F.s.y(2), F.x + 26, F.s.y(2), INK, 1.4);
    const x0 = F.x + (kind === 'treble' ? 44 : 24), dx = (290 - x0) / len, ly = F.s.lo + 30;
    pat.forEach((p, j) => {
      const x = x0 + j * dx + 6;
      body += noteSvg(F.s, { d: 4, x, p }, {}, INK) + wline(x, ly + 3, dx - 8) + ans(true, tx(x, ly, map[p], RED, 12));
    });
    body += bar(F.s, 300, 'final');
    const a = pat.map(p => map[p]).join(' ');
    cells.push(cell(i + 1, svg(306, ly + 10, body, `Pattern ${i + 1} on a ${kind === 'treble' ? '5' : kind === 'two' ? '2' : '3'}-line staff`, g <= 2 ? 1.05 : 1)));
    items.push({ q: `${i + 1}. ${kind} ${pat.join(',')}`, a, k: 'solfa', kind, ps: pat });
  });
  return { parts: [part('', grid(cells, 2))], items };
}

const MOVE = d => (d === 0 ? 'repeat' : Math.abs(d) === 1 ? 'step' : 'skip');
function mkMotion(v, r, g) {
  const n = COUNT.motion(g)[v.count], len = 6;
  const mels = r.distinct(n, () => {
    const ps = [r.int(1, 7)];
    while (ps.length < len) { const d = r.pick([-2, -1, 0, 1, 2]), p = ps[ps.length - 1] + d; if (p >= 0 && p <= 8) ps.push(p); }
    const kinds = new Set(ps.slice(1).map((p, i) => MOVE(p - ps[i])));
    return kinds.size === 3 ? ps : null;
  }, x => x.join(','));
  const items = [], rows = [];
  mels.forEach((ps, i) => {
    const F = frame('treble', 30, 4, 600);
    let body = F.svg;
    const dx = (590 - F.x - 20) / len, ly = F.s.lo + 36;
    ps.forEach((p, j) => {
      const x = F.x + 30 + j * dx;
      body += noteSvg(F.s, { d: 4, x, p }, {}, INK);
      if (j) {
        const xm = x - dx / 2, mv = MOVE(p - ps[j - 1]);
        body += wline(xm, ly + 3, dx - 18) + ans(true, tx(xm, ly, mv, RED, 12));
        items.push({ q: `Melody ${i + 1}, move ${j}`, a: mv, k: 'motion', p1: ps[j - 1], p2: p });
      }
    });
    body += bar(F.s, 600, 'final');
    rows.push(`<div class="mu-line"><p class="mu-cap"><span class="ws-num">${i + 1}.</span> Melody ${i + 1}</p>${svg(606, ly + 10, body, `Melody ${i + 1}: six notes on the treble staff`)}</div>`);
  });
  // a sample melody of their own on the key
  const F = frame('treble', 30, 4, 600);
  let sb = F.svg;
  const sample = [4, 5, 5, 3, 2, 2];
  sample.forEach((p, j) => { sb += ans(true, noteSvg(F.s, { d: 4, x: F.x + 30 + j * 86, p }, {}, RED)); });
  sb += bar(F.s, 600, 'final');
  return { parts: [part('', rows.join('')), part('Your turn', `<p class="mu-cap">Write a 6-note melody that uses at least one step, one skip and one repeat. Label each move.</p>${svg(606, 96, sb, 'An empty treble staff for your own melody')}${H_KEYNOTE('Sample on the key: B, C, C, A, G, G (step, repeat, skip, step, repeat).')}`)], items };
}
const H_KEYNOTE = t => key(`<p class="mu-ans" style="color:${RED}">${esc(t)}</p>`);

const RANGE = (g, range) => (range === 'ledger' ? (g <= 4 ? [-2, 10] : [-4, 12]) : [0, 8]);
function namePos(r, lo, hi, prev) {
  for (let t = 0; t < 30; t++) { const p = r.int(lo, hi); if (p !== prev && (lo === 0 || t > 6 || p < 0 || p > 8 || r.chance(0.55))) return p; }
  return lo === prev ? hi : lo;
}
// a staff row of whole notes with an answer line under each; notes: [{p, a?, red?, label (red answer), top (label above)}]
function noteRow(kind, notes, o = {}) {
  const hiP = Math.max(8, ...notes.map(n => n.p)), loP = Math.min(0, ...notes.map(n => n.p));
  const top = 20 + (hiP - 8) * 5 + (o.above ? 18 : 0), W = o.w || 640;
  const F = frame(kind, top, 4, W, { key: o.key });
  const dx = (W - F.x - 20) / notes.length, ly = F.s.y(Math.min(loP, -1)) + 24;
  let body = F.svg;
  notes.forEach((n, j) => {
    const x = F.x + 24 + j * dx;
    body += ans(!!n.red, chordSvg(F.s, x, [n], n.red ? RED : INK));
    if (o.above) body += tx(x, 14, n.top, INK, 12, 'middle', true);
    if (n.label != null) body += wline(x, ly + 3, Math.min(48, dx - 10)) + ans(true, tx(x, ly, n.label, RED, 13, 'middle', true));
    if (o.nums) body += tx(x - dx / 2 + 6, F.s.hi - 6, String(o.nums + j), GREY, 9, 'start');
  });
  body += bar(F.s, W, 'final');
  return { svg: body, h: ly + 10, w: W + 4 };
}
function grandRow(notes, o = {}) {
  const T = 30, B = T + 40 + 54, W = 640;
  const Ft = frame('treble', T, 14, W), Fb = frame('bass', B, 14, W);
  let body = Ft.svg + Fb.svg + ln(14, Ft.s.hi, 14, Fb.s.lo, INK, 1.4) + pathD(`M10 ${T} C2 ${T + 20} 12 ${T + 40} 2 ${(T + Fb.s.lo) / 2} C12 ${Fb.s.lo - 40} 2 ${Fb.s.lo - 20} 10 ${Fb.s.lo}`, INK, 2.6);
  const dx = (W - Ft.x - 20) / notes.length, ly = Fb.s.y(-2) + 26;
  notes.forEach((n, j) => {
    const x = Ft.x + 24 + j * dx, s = n.clef === 'treble' ? Ft.s : Fb.s;
    body += chordSvg(s, x, [n], INK) + wline(x, ly + 3, Math.min(48, dx - 10)) + ans(true, tx(x, ly, n.label, RED, 13, 'middle', true));
  });
  body += bar(Ft.s, W, 'final') + bar(Fb.s, W, 'final') + ln(W - 1.8, Ft.s.lo, W - 1.8, Fb.s.hi, INK, 4) + ln(W - 6, Ft.s.lo, W - 6, Fb.s.hi, INK, 1.3);
  return { svg: body, h: ly + 10, w: W + 4 };
}
const WORDS = ['BAG', 'CAB', 'BED', 'BEE', 'FED', 'FADE', 'FACE', 'CAFE', 'EGG', 'BADGE', 'CAGE', 'BEAD', 'DAD', 'ADD', 'AGE', 'ACE', 'BAD', 'FEED', 'BEEF', 'CABBAGE', 'BAGGAGE', 'EDGE', 'DEED', 'DAB', 'BEG', 'DEAF', 'FACED', 'FADED', 'ACED', 'AGED', 'CAGED', 'GAB', 'DECADE', 'BEADED'];
function wordsBlock(r, g, clef, range, n, start) {
  const [lo, hi] = RANGE(g, range), maxLen = g <= 3 ? 5 : 7;
  const ws = r.sample(WORDS.filter(w => w.length <= maxLen), n);
  const items = [], rows = [];
  for (let i = 0; i < ws.length; i += 2) {
    const pair = ws.slice(i, i + 2), F = frame(clef, range === 'ledger' ? 38 : 22, 4, 640);
    let body = F.svg, x = F.x + 30;
    const ly = F.s.y(Math.min(lo, -1)) + 26;
    pair.forEach((w, k) => {
      const x0 = x, ps = [...w].map(ch => { const c = []; for (let p = lo; p <= hi; p++) if (LET[atPos(p, clef).l] === ch) c.push(p); return r.pick(c); });
      ps.forEach(p => { body += chordSvg(F.s, x, [{ p }], INK); x += 36; });
      const mid = (x0 + x - 36) / 2;
      body += tx(x0 - 18, F.s.hi - 6, String(start + i + k) + '.', INK, 12, 'start', true);
      body += wline(mid, ly + 3, Math.max(70, w.length * 22)) + ans(true, tx(mid, ly, w, RED, 14, 'middle', true));
      x += 14;
      body += k === 0 && pair.length > 1 ? bar(F.s, x - 6, 'double') : '';
      x += 36;
      items.push({ q: `${start + i + k}. ${clef} ${ps.join(',')}`, a: w, k: 'word', clef, ps });
    });
    body += bar(F.s, 640, 'final');
    rows.push(`<div class="mu-line">${svg(644, ly + 10, body, `Two words written in ${clef} clef notes`)}</div>`);
  }
  return { html: rows.join(''), items };
}
const clefFor = (v, i) => (v.clef === 'both' ? (i % 2 ? 'bass' : 'treble') : v.clef === 'grand' ? 'treble' : v.clef);
function mkNames(v, r, g) {
  const n = COUNT.names(g)[v.count], [lo, hi] = RANGE(g, v.range), items = [], rows = [];
  const per = 8;
  if (v.clef === 'grand') {
    const rng = v.range === 'ledger' ? [-2, 10] : [0, 8];
    for (let i = 0; i < n; i += per) {
      const notes = [];
      for (let j = i; j < Math.min(n, i + per); j++) {
        const clef = r.chance(0.5) ? 'treble' : 'bass', p = namePos(r, rng[0], rng[1], notes.length ? notes[notes.length - 1].p : null), nt = atPos(p, clef);
        notes.push({ clef, p, label: LET[nt.l] });
        items.push({ q: `Note ${j + 1}: ${clef} position ${p}`, a: LET[nt.l], k: 'name', clef, p });
      }
      const R = grandRow(notes);
      rows.push(`<div class="mu-line">${svg(R.w, R.h, R.svg, `Grand staff with ${notes.length} notes`)}</div>`);
    }
  } else {
    for (let i = 0, row = 0; i < n; i += per, row++) {
      const clef = clefFor(v, row), notes = [];
      for (let j = i; j < Math.min(n, i + per); j++) {
        const p = namePos(r, lo, hi, notes.length ? notes[notes.length - 1].p : null), nt = atPos(p, clef);
        notes.push({ p, label: LET[nt.l] });
        items.push({ q: `Note ${j + 1}: ${clef} position ${p}`, a: LET[nt.l], k: 'name', clef, p });
      }
      const R = noteRow(clef, notes, { nums: i + 1 });
      rows.push(`<div class="mu-line">${svg(R.w, R.h, R.svg, `${clef === 'treble' ? 'Treble' : 'Bass'} staff with ${notes.length} notes`)}</div>`);
    }
  }
  const parts = [part('', rows.join(''))];
  if (v.spell && g <= 5) { const w = wordsBlock(r, g, v.clef === 'bass' ? 'bass' : 'treble', v.range, 4, n + 1); parts.push(part('Spell the hidden words', w.html)); items.push(...w.items); }
  return { parts, items };
}
function mkWords(v, r, g) {
  const n = COUNT.words(g)[v.count], w = wordsBlock(r, g, 'treble', v.range, n, 1);
  const F = frame('treble', 22, 4, 640);
  const own = `<p class="mu-cap">Write 2 words of your own in notes for a partner to solve. Use only the letters A to G.</p>${svg(644, 80, F.svg + bar(F.s, 320, 'double') + bar(F.s, 640, 'final'), 'An empty treble staff for two words')}`;
  return { parts: [part('', w.html), part('Your turn', own)], items: w.items };
}
// where a letter sits: on a line, in a space, below or above the staff
const where = p => (p < 0 ? 'below the staff' : p > 8 ? 'above the staff' : p % 2 === 0 ? 'on a line' : 'in a space');
function mkDraw(v, r, g) {
  const n = COUNT.draw(g)[v.count], [lo, hi] = RANGE(g, v.range), items = [], rows = [];
  for (let i = 0, row = 0; i < n; i += 8, row++) {
    const clef = clefFor(v, row), notes = [];
    for (let j = i; j < Math.min(n, i + 8); j++) {
      const p = namePos(r, lo, hi, notes.length ? notes[notes.length - 1].p : null), L = LET[atPos(p, clef).l];
      notes.push({ p, red: true, top: `${L}` });
      items.push({ q: `Note ${j + 1}: ${clef} ${L} ${where(p)} (${p})`, a: `${L} ${where(p)}`, k: 'draw', clef, p, L, wh: where(p), lo, hi });
    }
    const R = noteRow(clef, notes, { above: true, nums: i + 1 });
    const hints = notes.map((x, k) => `<li>${esc(x.top)} ${esc(where(x.p))}</li>`).join('');
    rows.push(`<div class="mu-line">${svg(R.w, R.h, R.svg, `${clef === 'treble' ? 'Treble' : 'Bass'} staff with letters to draw`)}<ol class="mu-hints" start="${i + 1}">${hints}</ol></div>`);
  }
  return { parts: [part('', rows.join(''))], items };
}

function mkSteps(v, r, g) {
  const n = COUNT.steps(g)[v.count], items = [], cells = [];
  const pairs = r.distinct(n, () => { const a = r.int(0, 14), st = r.chance(0.5) ? 1 : 2; return a + st <= 16 ? [a, a + st] : null; }, x => x.join('-'));
  pairs.forEach(([a, b], i) => {
    const body = keyboard(4, 4, 10, [{ k: a }, { k: b }], 15, 58);
    const ansT = b - a === 1 ? 'H' : 'W';
    cells.push(cell(i + 1, svg(158, 66, body, `Keyboard ${i + 1} with two keys marked`) + `<p class="mu-ans">W or H: ${blank(ansT, 2.4)}</p>`, ''));
    items.push({ q: `${i + 1}. keys ${a} and ${b}`, a: ansT, k: 'step', a1: a, a2: b });
  });
  const nat = 'E and F, B and C';
  items.push({ q: 'The two white-key half steps', a: nat, k: 'nat' });
  return { parts: [part('', grid(cells, 4)),
    part('Natural half steps', `<p class="mu-cap">Two pairs of white keys have no black key between them, so they are half steps. Name both pairs: ${blank(nat, 10)}</p>`)], items };
}

const roman = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'];
function scaleBlock(t, type, clef, kb, compact) {
  const sc = scaleOf(t, type), steps = !compact && (type === 'maj' || type === 'nmin');
  const ps = sc.map(nt => posOf(nt, clef)), F = frame(clef, 26 + Math.max(0, Math.max(...ps) - 8) * 5, 4, 640);
  const slots = sc.length, dx = (620 - F.x - 30) / slots, ly = F.s.y(Math.min(-2, ...ps)) + 20;
  let body = F.svg;
  const deg = type === 'penta' ? [1, 2, 3, 5, 6, 8] : [1, 2, 3, 4, 5, 6, 7, 8];
  sc.forEach((nt, j) => {
    const x = F.x + 30 + j * dx, p = posOf(nt, clef);
    body += tx(x, 13, String(deg[j]), GREY, 11, 'middle', true);
    body += ans(j > 0, chordSvg(F.s, x, [{ p, a: nt.a ? nt.a : undefined }], j ? RED : INK));
    body += wline(x, ly + 3, 34) + ans(true, tx(x, ly, nm(nt), RED, 13, 'middle', true));
    if (steps && j) { const xm = x - dx / 2, st = midi(nt) - midi(sc[j - 1]) === 1 ? 'H' : 'W'; body += wline(xm, ly + 21, 18) + ans(true, tx(xm, ly + 18, st, RED, 12, 'middle', true)); }
  });
  body += bar(F.s, 640, 'final');
  let h = ly + (steps ? 30 : 12);
  if (kb) {
    const c0 = midi({ l: 0, o: t.o, a: 0 });
    body += keyboard(150, h + 2, 14, sc.map(nt => ({ k: midi(nt) - c0, key: true })), 22, 62);
    h += 70;
  }
  return { svg: body, h, sc };
}
function mkScales(v, r, g) {
  const type = v.scale, kb = !!v.kb && g <= 8;
  const list = tonics(g, type === 'forms' ? 'hmin' : type);
  const fixed = v.tonic !== 'any' && v.tonic !== 'first' ? list.find(t => tid(t) === v.tonic) : null;
  const n = fixed ? 1 : COUNT.scales(g)[v.count] + (kb || type === 'forms' ? 0 : 1);
  const picks = fixed ? [fixed] : v.tonic === 'first' ? list.slice(0, n) : r.sample(list, Math.min(n, list.length));
  const items = [], blocks = [], quiz = [];
  picks.forEach((name, i) => {
    const clef = v.clef === 'both' ? (i % 2 ? 'bass' : 'treble') : g >= 5 ? v.clef : 'treble';
    const L = LET.indexOf(name[0]);
    const t = noteOf(name, clef === 'treble' ? 4 : L <= 1 ? 3 : 2);
    const forms = type === 'forms' ? ['nmin', 'hmin', 'mmin'] : [type];
    forms.forEach(ty => {
      const B = scaleBlock(t, ty, clef, kb && type !== 'forms', type === 'forms');
      const title = `${name} ${TYPE_NAME[ty]}${ty === 'mmin' ? ' (going up)' : ''} scale${clef === 'bass' ? ', bass clef' : ''}`;
      blocks.push(`<div class="mu-line"><p class="mu-cap"><span class="ws-num">${blocks.length + 1}.</span> <b>${esc(title)}</b>. The first note is given.</p>${svg(644, B.h, B.svg, `Staff for the ${name} ${TYPE_NAME[ty]} scale`, type === 'forms' ? 0.82 : 1)}</div>`);
      items.push({ q: `${blocks.length}. ${name} ${ty} ${clef}`, a: B.sc.map(nm).join(' '), k: 'scale', ty, name, notes: B.sc });
      if (type !== 'forms' && (ty === 'maj' || ty === 'nmin')) items.push({ q: `${blocks.length}. steps of ${name} ${ty}`, a: B.sc.slice(1).map((x, j) => (midi(x) - midi(B.sc[j]) === 1 ? 'H' : 'W')).join(' '), k: 'wh', ty, notes: B.sc });
      if (ty !== 'penta') for (let d = 2; d <= 7; d++) quiz.push({ q: `In ${name} ${TYPE_NAME[ty]}, scale degree ${d} is`, a: nm(B.sc[d - 1]), k: 'deg', ty, name, d });
      else { for (let d = 2; d <= 5; d++) quiz.push({ q: `In ${name} major pentatonic, note ${d} going up is`, a: nm(B.sc[d - 1]), k: 'deg', ty, name, d }); quiz.push({ q: `${name} major pentatonic leaves out two notes of the ${name} major scale. Which?`, a: (() => { const m = scaleOf(t, 'maj'); return `${nm(m[3])} and ${nm(m[6])} (degrees 4 and 7)`; })(), k: 'pleft', name, t }); }
    });
  });
  const qn = type === 'forms' ? { s: 2, m: 4, l: 4 }[v.count] : { s: 4, m: 6, l: 8 }[v.count];
  const qs = r.sample(quiz, Math.min(qn, quiz.length));
  const parts = [part('', blocks.join(''))];
  if (qs.length) parts.push(part('Check your scales', fill(qs.map(q => `${esc(q.q)} ${blank(q.a, q.k === 'pleft' ? 10 : 3)}`), qs.length > 3 && type !== 'penta' ? 2 : 1, blocks.length + 1)));
  if (type === 'forms') {
    const why = 'Harmonic minor raises degree 7 so it becomes a leading tone, a half step below the tonic; that makes the V chord major and pulls home. Melodic minor also raises 6 going up, to smooth the wide step (an augmented 2nd) between 6 and raised 7; going down it is usually natural minor.';
    parts.push(part('Why the changes?', `<p class="mu-cap">Explain why harmonic minor raises one note and melodic minor raises two.</p><div class="ws-lines">${'<span></span>'.repeat(3)}</div>${H_KEYNOTE(why)}`));
    items.push({ q: 'Why the alterations', a: why, k: 'text' });
  }
  items.push(...qs);
  return { parts, items };
}

function mkKeysig(v, r, g) {
  const max = g === 5 ? 3 : g === 6 ? 4 : g === 7 ? 5 : g === 8 ? 6 : 7, c = COUNT.keysig(g)[v.count];
  const nName = g === 5 ? c : Math.round(c * 0.7), nWrite = g === 5 ? Math.round(c / 3) : c - nName;
  const clefs = v.clef === 'both' ? ['treble', 'bass'] : [v.clef], items = [];
  const modeFor = () => (v.keys === 'mix' ? r.pick(['maj', 'min']) : v.keys);
  const all = [];
  for (let n = -max; n <= max; n++) for (const clef of clefs) all.push({ n, clef });
  const ns15 = Array.from({ length: 2 * max + 1 }, (_, i) => i - max);
  const nPick = r.shuffle(ns15).concat(r.shuffle(ns15)).slice(0, Math.min(nName, all.length));
  const names = nPick.map((n, i) => ({ n, clef: clefs[i % clefs.length], mode: modeFor() }));
  const writes = r.sample(all.filter(x => x.n !== 0), Math.min(nWrite, all.length - clefs.length)).map(x => ({ ...x, mode: v.keys === 'min' ? 'min' : v.keys === 'mix' ? r.pick(['maj', 'min']) : 'maj' }));
  const label = (n, mode) => (mode === 'maj' ? `${MAJ[n]} major` : mode === 'min' ? `${MIN[n]} minor` : `${MAJ[n]} major, ${MIN[n]} minor`);
  const cellsA = names.map((x, i) => {
    const F = frame(x.clef, 26, 4, 150, { key: x.n });
    const a = label(x.n, x.mode);
    const prompt = x.mode === 'rel' ? `${blank(MAJ[x.n], 2.6)} major, ${blank(MIN[x.n], 2.6)} minor` : `${blank(x.mode === 'maj' ? MAJ[x.n] : MIN[x.n], 3)} ${x.mode === 'maj' ? 'major' : 'minor'}`;
    items.push({ q: `${i + 1}. name ${x.clef} ${x.n} ${x.mode}`, a, k: 'ksname', n: x.n, mode: x.mode });
    return cell(i + 1, svg(154, 76, F.svg, `${x.clef} clef with a key signature of ${Math.abs(x.n)} ${x.n < 0 ? 'flats' : 'sharps'}`) + `<p class="mu-ans">${prompt}</p>`);
  });
  const cellsB = writes.map((x, i) => {
    const F = frame(x.clef, 26, 4, 150, { key: x.n, keyRed: true });
    const what = x.mode === 'min' ? `${MIN[x.n]} minor` : `${MAJ[x.n]} major`;
    const a = `${Math.abs(x.n)} ${x.n > 0 ? 'sharp' : 'flat'}${Math.abs(x.n) > 1 ? 's' : ''}: ${(x.n > 0 ? 'FCGDAEB' : 'BEADGCF').slice(0, Math.abs(x.n)).split('').map(l => l + (x.n > 0 ? '♯' : '♭')).join(' ')}`;
    items.push({ q: `${names.length + i + 1}. write ${x.clef} ${what}`, a, k: 'kswrite', n: x.n, what });
    return cell(names.length + i + 1, svg(154, 76, F.svg, `Empty ${x.clef} staff to write the key signature of ${what}`), `<b>${esc(what)}</b>`);
  });
  const parts = [part('Name the key', grid(cellsA, 4))];
  if (cellsB.length) parts.push(part('Write the key signature', grid(cellsB, 4)));
  return { parts, items };
}

// interval names: number from the letters, quality from the half steps
const ORD = { 1: 'unison', 2: '2nd', 3: '3rd', 4: '4th', 5: '5th', 6: '6th', 7: '7th', 8: 'octave' };
const IV = [['m2', 2, 1], ['M2', 2, 2], ['m3', 3, 3], ['M3', 3, 4], ['P4', 4, 5], ['A4', 4, 6], ['d5', 5, 6], ['P5', 5, 7], ['m6', 6, 8], ['M6', 6, 9], ['m7', 7, 10], ['M7', 7, 11], ['P8', 8, 12]];
function ivPick(r, g, clef) {
  const list = g <= 6 ? IV.filter(x => !['A4', 'd5'].includes(x[0])) : g <= 8 ? IV.filter(x => !['A4', 'd5'].includes(x[0])) : IV;
  for (let t = 0; t < 60; t++) {
    const iv = r.pick(list), p = r.int(-1, 6), b = atPos(p, clef);
    if (g >= 9 && r.chance(0.3)) b.a = r.pick([1, -1]);
    const top = above(b, iv[1] - 1, iv[2]);
    if (!top || posOf(top, clef) > 11) continue;
    if (g <= 6 && top.a !== 0) continue;   // number only: both notes natural
    return { b, top, iv };
  }
  return null;
}
const ivName = (iv, g) => (g <= 6 ? ORD[iv[1]] : iv[0]);
function mkIntervals(v, r, g) {
  const c = COUNT.intervals(g)[v.count], nName = Math.round(c * 0.7), nBuild = c - nName, items = [];
  const list = r.distinct(c, () => ivPick(r, g, v.clef === 'both' ? r.pick(['treble', 'bass']) : v.clef), x => nm(x.b) + x.b.o + x.iv[0]);
  const cells = [], cellsB = [];
  list.forEach((x, i) => {
    const clef = v.clef === 'both' ? (i % 2 ? 'bass' : 'treble') : v.clef;
    const b = { ...x.b }, top = above(b, x.iv[1] - 1, x.iv[2]);
    if (!top) return;
    const pb = posOf(b, clef), pt = posOf(top, clef), F = frame(clef, 30, 4, 150), ly = F.s.y(-3) + 22;
    const sb = { p: pb, a: b.a ? b.a : undefined }, st = { p: pt, a: top.a ? top.a : undefined };
    const a = ivName(x.iv, g);
    if (i < nName) {
      const harm = x.iv[1] > 2 && r.chance(0.5);
      const body = F.svg + (harm ? chordSvg(F.s, 100, [sb, st], INK) : chordSvg(F.s, 78, [sb], INK) + chordSvg(F.s, 122, [st], INK));
      cells.push(cell(i + 1, svg(154, ly - 8, body, `Two notes on the ${clef} staff`) + `<p class="mu-ans">${blank(a, 4)}</p>`));
      items.push({ q: `${i + 1}. name ${clef} ${nm(b)}${b.o} ${nm(top)}${top.o}`, a, k: 'int', b, top, g });
    } else {
      const body = F.svg + chordSvg(F.s, 80, [sb], INK) + ans(true, chordSvg(F.s, 122, [st], RED));
      const what = g <= 6 ? `a ${ORD[x.iv[1]]} above` : `a ${x.iv[0]} above`;
      cellsB.push(cell(i + 1, svg(154, ly - 8, body, `One note on the ${clef} staff`) + `<p class="mu-ans">Note: ${blank(nm(top), 3)}</p>`, `Draw ${esc(what)}`));
      items.push({ q: `${i + 1}. build ${clef} ${nm(b)}${b.o} ${x.iv[0]}`, a: nm(top), k: 'ibuild', b, top, iv: x.iv, g });
    }
  });
  const parts = [part('Name the interval', grid(cells, 4))];
  if (cellsB.length) parts.push(part('Draw the interval', grid(cellsB, 4)));
  return { parts, items };
}

// chord qualities as half steps above the root, letters as thirds
const QUAL = { maj: [4, 7], min: [3, 7], dim: [3, 6], aug: [4, 8], maj7: [4, 7, 11], dom7: [4, 7, 10], min7: [3, 7, 10], hdim7: [3, 6, 10], dim7: [3, 6, 9] };
const QNAME = { maj: 'major', min: 'minor', dim: 'diminished', aug: 'augmented', maj7: 'major 7th', dom7: 'dominant 7th', min7: 'minor 7th', hdim7: 'half-diminished 7th', dim7: 'diminished 7th' };
const SYM = { maj: '', min: 'm', dim: 'dim', aug: 'aug', maj7: 'maj7', dom7: '7', min7: 'm7', hdim7: 'm7♭5', dim7: 'dim7' };
function chordOf(root, q) {
  const out = [root];
  for (let i = 0; i < QUAL[q].length; i++) { const n = above(root, 2 * (i + 1), QUAL[q][i]); if (!n) return null; out.push(n); }
  return out;
}
const ROOTS = g => (g <= 6 ? ['C', 'D', 'E', 'F', 'G', 'A', 'B'] : g <= 8 ? ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'B♭', 'E♭', 'F♯'] : ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'B♭', 'E♭', 'A♭', 'D♭', 'F♯', 'C♯', 'G♭']);
// the chord placed on a staff: inversion moves the lowest notes up an octave
function voiced(chord, inv, clef) {
  const ns = chord.map((n, i) => (i < inv ? { ...n, o: n.o + 1 } : { ...n }));
  const order = ns.slice(inv).concat(ns.slice(0, inv));
  const o = fitOct(order[0], order.map(n => dia(n) - dia(order[0])), clef), shift = o - order[0].o;
  return order.map(n => ({ ...n, o: n.o + shift }));
}
const asStaff = (ns, clef) => ns.map(n => ({ p: posOf(n, clef), a: n.a ? n.a : undefined }));
function chordPick(r, g, quals, roots) {
  for (let t = 0; t < 40; t++) { const q = r.pick(quals), root = noteOf(r.pick(roots), 4), ch = chordOf(root, q); if (ch) return { q, root, ch }; }
  return { q: 'maj', root: noteOf('C', 4), ch: chordOf(noteOf('C', 4), 'maj') };
}
function chordCell(clef, ns, red, w = 150) {
  const ps = asStaff(ns, clef), hi = Math.max(8, ...ps.map(p => p.p)), F = frame(clef, 22 + (hi - 8) * 5, 4, w), lo = Math.min(-1, ...ps.map(p => p.p));
  return { body: F.svg + ans(red, chordSvg(F.s, w * 0.62, ps, red ? RED : INK)), h: F.s.y(lo) + 14 };
}
function mkTriads(v, r, g) {
  const c = COUNT.triads(g)[v.count], nName = Math.round(c * 0.65), nBuild = c - nName;
  const quals = g <= 6 ? ['maj', 'min'] : ['maj', 'min', 'dim', 'aug'], kb = !!v.kb && g <= 8, items = [];
  const list = r.distinct(c, () => chordPick(r, g, quals, ROOTS(g)), x => nm(x.root) + x.q);
  const cellsA = [], cellsB = [];
  list.forEach((x, i) => {
    const clef = v.clef === 'both' ? (i % 2 ? 'bass' : 'treble') : v.clef, ns = voiced(x.ch, 0, clef);
    const name = `${nm(x.root)} ${QNAME[x.q]}`;
    if (i < nName) {
      const C = chordCell(clef, ns, false);
      cellsA.push(cell(i + 1, svg(154, C.h, C.body, `A triad on the ${clef} staff`) + `<p class="mu-ans">${blank(name, 7)}</p>`));
      items.push({ q: `${i + 1}. name ${clef} ${ns.map(nm).join(' ')}`, a: name, k: 'triad', ns });
    } else {
      const C = chordCell(clef, ns, true, 170);
      let body = C.body, h = C.h;
      if (kb) { const c0 = midi({ l: 0, o: ns[0].o, a: 0 }); body += keyboard(4, h + 10, 14, ns.map(n => ({ k: midi(n) - c0, key: true })), 11.6, 44); h += 58; }
      const a = ns.map(nm).join(' ');
      cellsB.push(cell(i + 1, svg(174, h, body, `Empty ${clef} staff to build ${name}`) + `<p class="mu-ans">Notes: ${blank(a, 6)}</p>`, `Build <b>${esc(name)}</b>`));
      items.push({ q: `${i + 1}. build ${name} ${clef}`, a, k: 'tbuild', root: x.root, qual: x.q, ns });
    }
  });
  const parts = [part('Name the triad', grid(cellsA, 4))];
  if (cellsB.length) parts.push(part('Build the triad', grid(cellsB, kb ? 3 : 4)));
  return { parts, items };
}
const INV = ['root position', '1st inversion', '2nd inversion'], FIG = ['5/3', '6', '6/4'];
function mkInversions(v, r, g) {
  const c = COUNT.inversions(g)[v.count], nBuild = { s: 3, m: 6, l: 9 }[v.count], nName = c - nBuild, items = [];
  const quals = g <= 8 ? ['maj', 'min'] : ['maj', 'min', 'dim', 'aug'];
  const list = r.distinct(nName, () => ({ ...chordPick(r, g, quals, ROOTS(g)), inv: r.int(0, 2) }), x => nm(x.root) + x.q + x.inv);
  const cellsA = list.map((x, i) => {
    const clef = v.clef === 'both' ? (i % 2 ? 'bass' : 'treble') : v.clef, ns = voiced(x.ch, x.inv, clef), C = chordCell(clef, ns, false);
    const a = `${nm(x.root)} ${QNAME[x.q]}, ${INV[x.inv]}${g >= 9 ? ` (${FIG[x.inv]})` : ''}, bass ${nm(ns[0])}`;
    items.push({ q: `${i + 1}. name ${clef} ${ns.map(n => nm(n) + n.o).join(' ')}`, a, k: 'inv', ns, g });
    return cell(i + 1, svg(154, C.h, C.body, `A triad on the ${clef} staff`) + `<p class="mu-ans">${blank(a, 12)}</p>`);
  });
  // build: three chords in all three positions
  const roots = g === 7 ? ['C', 'F', 'G'].slice(0, Math.ceil(nBuild / 3)) : r.sample(g <= 8 ? ['C', 'F', 'G', 'D', 'A', 'B♭'] : ROOTS(g), Math.ceil(nBuild / 3));   // grade 7 writes C, F and G major
  const cellsB = [];
  roots.forEach((rn, k) => {
    const q = g === 7 ? 'maj' : g <= 8 ? (k ? r.pick(['maj', 'min']) : 'maj') : r.pick(['maj', 'min']), root = noteOf(rn, 4), ch = chordOf(root, q);
    if (!ch) return;
    [0, 1, 2].forEach(inv => {
      if (cellsB.length >= nBuild) return;
      const clef = v.clef === 'both' ? (k % 2 ? 'bass' : 'treble') : v.clef, ns = voiced(ch, inv, clef), C = chordCell(clef, ns, true);
      const what = `${rn} ${QNAME[q]}, ${INV[inv]}`, a = `${ns.map(nm).join(' ')} (bass ${nm(ns[0])})`, n = nName + cellsB.length + 1;
      cellsB.push(cell(n, svg(154, C.h, C.body, `Empty ${clef} staff to build ${what}`) + `<p class="mu-ans">Bass note: ${blank(nm(ns[0]), 3)}</p>`, `<b>${esc(what)}</b>`));
      items.push({ q: `${n}. build ${what}`, a, k: 'ibuildch', root, qual: q, inv, ns });
    });
  });
  return { parts: [part('Name the chord and its position', grid(cellsA, 3)), part('Write each chord in three positions', grid(cellsB, 3))], items };
}

const NUMERAL = (deg, q) => { const R = roman[deg]; return q === 'maj' ? R : q === 'min' ? R.toLowerCase() : q === 'dim' ? R.toLowerCase() + '°' : q === 'aug' ? R + '+' : q === 'maj7' ? R + 'maj7' : q === 'dom7' ? R + '7' : q === 'min7' ? R.toLowerCase() + '7' : q === 'hdim7' ? R.toLowerCase() + 'ø7' : R.toLowerCase() + '°7'; };
const qualOf = ns => { const s = ns.slice(1).map(n => midi(n) - midi(ns[0])).join(','); return Object.keys(QUAL).find(k => QUAL[k].join(',') === s); };
function mkDiatonic(v, r, g) {
  const sev = v.chords === 'sev' && g >= 9, n = COUNT.diatonic(g)[v.count];
  const pool = DIA_KEYS(g), fixed = pool.find(t => tid(t) === v.tonic);
  const keys = fixed ? [fixed] : v.tonic === 'first' ? pool.slice(0, n) : r.sample(pool, n), items = [], blocks = [];
  keys.forEach((kname, i) => {
    const sig = sigOfMajor(kname), t0 = noteOf(kname, 4), given = r.int(0, 6);
    const sc = scaleOf(t0, 'maj'), size = sev ? 4 : 3;
    const chords = sc.slice(0, 7).map((root, d) => Array.from({ length: size }, (_, k) => sc[(d + 2 * k) % 7] && { ...sc[(d + 2 * k) % 7], o: sc[(d + 2 * k) % 7].o + Math.floor((d + 2 * k) / 7) }));
    // octave: keep every chord on or near the staff
    const lowP = Math.min(...chords.map(c => posOf(c[0], 'treble'))), highP = Math.max(...chords.map(c => posOf(c[size - 1], 'treble')));
    const shift = highP > 13 ? -1 : lowP < -3 ? 1 : 0;
    const F = frame('treble', 34 + Math.max(0, (highP + shift * 7) - 9) * 5, 4, 640, { key: sig });
    const dx = (620 - F.x - 10) / 7, ly = F.s.y(Math.min(-3, lowP + shift * 7)) + 22;
    let body = F.svg;
    const quals = [];
    chords.forEach((ch, d) => {
      const ns = ch.map(nn => ({ ...nn, o: nn.o + shift })), x = F.x + 34 + d * dx, q = qualOf(ns), num = NUMERAL(d, q);
      quals.push(q);
      if (d === given) body += chordSvg(F.s, x, ns.map(nn => ({ p: posOf(nn, 'treble') })), INK);
      else body += ans(true, chordSvg(F.s, x, ns.map(nn => ({ p: posOf(nn, 'treble') })), RED));
      body += wline(x, ly + 3, 46) + ans(true, tx(x, ly, num, RED, 13, 'middle', true));
      body += wline(x, ly + 23, 56) + ans(true, tx(x, ly + 20, QNAME[q].replace('-diminished', '-dim.').replace('dominant', 'dom.'), RED, 9.5));
      items.push({ q: `${kname} major, degree ${d + 1}`, a: `${num} ${QNAME[q]}`, k: 'dia', ns, d, kname, num });
    });
    body += bar(F.s, 640, 'final');
    blocks.push(`<div class="mu-line"><p class="mu-cap"><span class="ws-num">${i + 1}.</span> <b>${esc(kname)} major</b>. The ${sev ? 'seventh chord' : 'triad'} on degree ${given + 1} is given. Write the rest, then the Roman numeral and quality under each.</p>${svg(644, ly + 30, body, `Treble staff in ${kname} major with seven chord spaces`)}</div>`);
    if (!sev) {
      const grp = q => quals.map((x, d) => (x === q ? NUMERAL(d, x) : null)).filter(Boolean).join(', ');
      const a = `major: ${grp('maj')}; minor: ${grp('min')}; diminished: ${grp('dim')}`;
      blocks.push(`<p class="mu-sort">Sort the ${esc(kname)} chords. Major: ${blank(grp('maj'), 6)} Minor: ${blank(grp('min'), 6)} Diminished: ${blank(grp('dim'), 3)}</p>`);
      items.push({ q: `${kname} sort`, a, k: 'sort', quals });
    }
  });
  return { parts: [part('', blocks.join(''))], items };
}

function mkSymbols(v, r, g) {
  const n = COUNT.symbols(g)[v.count], kb = !!v.kb && g <= 8, items = [], cells = [];
  const quals = g <= 8 ? ['maj', 'min', 'dom7', 'maj7', 'min7', 'dim'] : ['maj', 'min', 'dim', 'aug', 'dom7', 'maj7', 'min7', 'hdim7', 'dim7'];
  const list = r.distinct(n, () => chordPick(r, g, quals, ROOTS(Math.max(g, 7))), x => nm(x.root) + x.q);
  list.forEach((x, i) => {
    const clef = v.clef === 'both' ? (i % 2 ? 'bass' : 'treble') : v.clef, ns = voiced(x.ch, 0, clef), C = chordCell(clef, ns, true, 170);
    let body = C.body, h = C.h;
    if (kb) { const c0 = midi({ l: 0, o: ns[0].o, a: 0 }); body += keyboard(4, h + 10, 14, ns.map(nn => ({ k: midi(nn) - c0, key: true })), 11.6, 44); h += 58; }
    const sym = nm(x.root) + SYM[x.q], a = ns.map(nm).join(' ');
    cells.push(cell(i + 1, svg(174, h, body, `Empty ${clef} staff for the chord ${sym}`) + `<p class="mu-ans">Notes: ${blank(a, 7)}</p>`, `<b class="mu-sym">${esc(sym)}</b>`));
    items.push({ q: `${i + 1}. ${sym} ${clef}`, a, k: 'sym', sym, qual: x.q, root: x.root, ns });
  });
  return { parts: [part('', grid(cells, 3))], items };
}

// composition staff paper; the key draws a short model in red
function modelMeasures(r, g, lines, m, n) {
  const T = METER[m][2], lvl = Math.min(g, 4), P = pool(lvl, m, 'all');
  const ms = Array.from({ length: n }, () => measure(r, P, T, Math.min(lvl, 3)).ev);
  const pitch = lines === 'two' ? [0, 2] : lines === 'three' ? [0, 2, 3] : lines === 'bass' ? [1, 2, 3, 4, 5, 6] : [-2, -1, 0, 1, 2, 3, 4, 5, 6];
  let prev = r.pick(pitch);
  ms.forEach((ev, mi) => ev.forEach((e, j) => {
    if (e.r) return;
    const near = pitch.filter(p => Math.abs(p - prev) <= 2);
    e.p = r.pick(near.length ? near : pitch); prev = e.p;
    if (mi === n - 1 && j === ev.length - 1 && lines !== 'rhythm' && lines !== 'two' && lines !== 'three') e.p = lines === 'bass' ? 3 : -2;   // end on C
  }));
  return ms;
}
function mkStaff(v, r, g) {
  const lines = v.lines, m = v.meter === 'mix' ? '4' : v.meter, nb = +v.bars, per = nb === 1 ? 1 : nb === 2 ? 2 : 4;
  const T = METER[m][2], sys = Math.ceil(nb / per), grand = lines === 'grand';
  const kind = lines === 'rhythm' ? 'one' : lines === 'grand' ? 'treble' : lines;
  const items = [], rows = [];
  const nModel = Math.min(per, nb);
  const model = modelMeasures(r, g, lines, m, nModel);
  const sections = v.form === 'none' ? [] : v.form === 'ab' ? ['A', 'B'] : ['A', 'B', 'A'];
  const secAt = {};
  // AB: two halves; ABA: A a quarter, B the middle half, A the last quarter (rounded to whole measures)
  const starts = v.form === 'ab' ? [0, Math.floor(nb / 2)] : [0, Math.max(1, Math.round(nb / 4)), nb - Math.max(1, Math.round(nb / 4))];
  if (sections.length && nb >= sections.length) sections.forEach((s, i) => { secAt[starts[i]] = s; });
  for (let k = 0; k < sys; k++) {
    const W = 640, top = kind === 'one' ? 48 : 38;
    const F = frame(kind, top, 4, W, { time: k === 0 && kind !== 'two' && kind !== 'three' ? METER[m] : null });
    let body = F.svg;
    let Fb = null;
    if (grand) { Fb = frame('bass', top + 94, 4, W, { time: k === 0 ? METER[m] : null }); body += Fb.svg + ln(4, F.s.hi, 4, Fb.s.lo, INK, 1.4); }
    const x0 = F.x + 8, mw = (W - x0) / per;
    for (let j = 0; j < per && k * per + j < nb; j++) {
      const bi = k * per + j, mx = x0 + j * mw, last = bi === nb - 1;
      body += bar(F.s, mx + mw, last ? 'final' : 'single');
      if (Fb) body += bar(Fb.s, mx + mw, last ? 'final' : 'single');
      body += tx(mx + 4, F.s.hi - 7, String(bi + 1), GREY, 10, 'start');
      if (secAt[bi]) body += tx(mx + 26, F.s.hi - 7, `Section ${secAt[bi]}`, INK, 12, 'start', true);
      if (g <= 3) for (let b = 0; b < METER[m][0]; b++) body += circ(mx + 14 + (b + 0.5) * (mw - 20) / METER[m][0], (Fb ? Fb.s.lo : F.s.lo) + 16, 1.6, GREY);
      if (g <= 2) body += wline(mx + mw / 2, (Fb ? Fb.s.lo : F.s.lo) + 34, mw - 16);
      if (k === 0 && bi < nModel) {
        const u = (mw - 22) / T, ev = model[bi].map(e => ({ ...e }));
        const E = engrave(F.s, mx + 4, [ev], { u, beat: m === '6' ? 6 : 4, stick: false, pad: 4, padR: 0, final: 'none', key: true });
        body += E.svg;
        if (g <= 2) { let t = ''; for (const L of (lines === 'rhythm' && g >= 3 ? countLabels(ev, m) : sylLabels(ev))) t += tx(E.info[0].mx + L.pos * u + OFF, (Fb ? Fb.s.lo : F.s.lo) + 31, L.t, RED, 11); body += ans(true, t); }
        if (Fb) { const roots = [0, 3, 4, 0], rp = [3 - 2 + roots[bi % 4] * 1 - 0, 0][0]; body += ans(true, chordSvg(Fb.s, mx + mw / 2, [{ p: [1, 4, 5, 1][bi % 4] + 2 - 0 }], RED)); }
        items.push({ q: `Model measure ${bi + 1}`, a: (g <= 2 ? sylLabels(ev) : countLabels(ev, m)).map(L => L.t).join(' '), k: 'model', m, ev, mode: g <= 2 ? 'syl' : 'count' });
      }
    }
    const h = (Fb ? Fb.s.lo : F.s.lo) + (g <= 2 ? 40 : g <= 3 ? 24 : 16);
    rows.push(`<div class="mu-line">${svg(W + 4, h, body, `Staff system ${k + 1} with ${Math.min(per, nb - k * per)} empty measures`, kind === 'two' || kind === 'three' ? 1 : 1)}</div>`);
  }
  const title = v.topic ? esc(v.topic) : '';
  const headBits = [`<span>Title: ${title ? `<b>${title}</b>` : '<span class="mu-wl"></span>'}</span>`, '<span>Composer: <span class="mu-wl"></span></span>'];
  if (g >= 4) headBits.push('<span>Tempo: <span class="mu-wl mu-short"></span></span>', '<span>Dynamics: <span class="mu-wl mu-short"></span></span>');
  const check = g >= 2 ? `<ul class="mu-check"><li>${kind === 'two' || kind === 'three' ? 'Every note sits on a line or space' : 'Time signature at the start'}</li><li>Every measure has ${METER[m][0]} ${m === '6' ? 'eighths' : 'beats'}</li><li>Double bar at the end</li><li>A title</li>${g >= 4 ? '<li>Tempo and dynamics marked</li>' : ''}</ul>` : '';
  return { parts: [part('', `<div class="mu-head">${headBits.join('')}</div>${rows.join('')}${check}`)], items };
}

/* ---------- sheet text ---------- */
const MAKERS = { rhythm: mkRhythm, listen: mkListen, dictate: mkDictate, complete: mkComplete, barlines: mkBarlines, fix: mkFix, rests: mkRests, solfa: mkSolfa,
  motion: mkMotion, names: mkNames, words: mkWords, draw: mkDraw, steps: mkSteps, scales: mkScales, keysig: mkKeysig, intervals: mkIntervals, triads: mkTriads,
  inversions: mkInversions, diatonic: mkDiatonic, symbols: mkSymbols, staff: mkStaff };
function texts(sk, g, v) {
  const beats = g <= 2 ? 'ta (one sound on a beat), ti-ti (two sounds on a beat)' : 'counts';
  switch (sk) {
    case 'rhythm': return g === 0 ? { d: 'Clap each row while you say ta and ti-ti. Count the claps. Write how many sounds you made.', i: 'I can clap a rhythm and count its sounds.',
      ex: example('A stick with no partner is ta: one clap. Two sticks joined at the top are ti-ti: two quick claps on one beat. The squiggle is a rest: no clap.', 'ta, ti-ti, rest, ta has 4 sounds.'),
      w: 'Counting the rest as a sound, or counting ti-ti as one sound.' }
      : g <= 2 ? { d: 'Read each rhythm. Write ta, ti or ta-a under each note and rest under each rest. Then clap it.', i: 'I can read and clap rhythms with ta, ti-ti, ta-a and rest.',
        ex: example('ta is one sound on one beat. ti-ti is two sounds on one beat. ta-a is one sound held for two beats. A rest is a silent beat.', 'ta &nbsp; ti ti &nbsp; rest &nbsp; ta'), w: 'Writing one ti under a pair of eighth notes, or forgetting that ta-a lasts two beats.' }
      : { d: 'Write the counts under every note. Put held beats and rests in parentheses. Then clap each line while you count aloud.', i: 'I can count and clap rhythms in different meters.',
        ex: example('Each beat gets a number. Eighths split a beat: 1 &. Sixteenths split it in four: 1 e & a. In 6/8, count each eighth: 1 2 3 4 5 6.', 'A half note on beat 1 then two quarters: 1 (2) 3 4.'),
        w: 'Losing the beat after a long note, writing & on a beat that has no eighth note, and counting 6/8 as six slow beats instead of two groups of three.' };
    case 'listen': return { d: 'Listen to your teacher clap. Circle the letter of the rhythm you hear.', i: 'I can match a rhythm I hear to the rhythm I see.',
      ex: example('Say each rhythm in your head before your teacher claps.', g <= 2 ? 'ta ti-ti ta ta' : '1 2 & 3 4'), w: 'Choosing after one hearing; clap it back softly to check.' };
    case 'dictate': return { d: 'Your teacher will clap each rhythm. Write it in the empty measures. Check that each measure has the right number of beats.', i: 'I can write down a rhythm I hear.',
      ex: example('Tap the beat while you listen. Write the beats first, then split the beats that had more than one sound.', 'Heard: long, short short, short short, long. Wrote: half, two eighths, two eighths... check the beats.'), w: 'Measures with too many beats; writing a quarter where the sound was held.' };
    case 'complete': return { d: 'Each box is missing one note or rest. Count the beats, then draw one note or rest in the box that makes the measure full. Write its name.', i: 'I can complete a measure so it has the right number of beats.',
      ex: example('In 4/4, a measure holds 4 beats. If the notes add up to 3, one beat is missing: a quarter note or quarter rest fits.', 'Quarter + half + ? = 4 beats, so ? = 1 beat.'), w: 'Reading the top number of the time signature as the note value, and forgetting a dot adds half the note.' };
    case 'barlines': return { d: `Read the time signature. Draw a bar line after each full measure and a double bar at the end.${g >= 3 ? ' If the last measure is short, add one note or rest to fill it.' : ''}`, i: 'I can split a rhythm into measures with bar lines.',
      ex: example('The top number tells how many beats are in each measure. Count beats and draw a bar line every time you reach it.', 'In 3/4: 1 2 3 | 1 2 3 | ...'), w: 'Drawing a bar line in the middle of a held note, and forgetting the double bar at the end.' };
    case 'fix': return { d: 'Count the beats in each measure and write the total. Circle each measure that does not match the time signature, then fix it by adding or crossing out one note or rest.', i: 'I can find and fix measures with the wrong number of beats.',
      ex: example('Add the beats: quarter = 1, half = 2, two eighths = 1, quarter rest = 1.', 'In 4/4: half + quarter = 3 beats, so one beat is missing.'), w: 'Counting two eighth notes as two beats, and skipping rests.' };
    case 'rests': return g === 1 ? { d: 'Find the rest in each rhythm and circle it. Write the beat it is on. Clap each line with a silent beat. Then trace the rests and draw four of your own.', i: 'I can find a quarter rest and keep it silent.',
      ex: example('A quarter rest is one beat of silence. Open your hands on the rest; do not clap.', 'ta ta rest ta: the rest is on beat 3.'), w: 'Clapping on the rest, or skipping the rest beat so the line speeds up.' }
      : { d: 'Draw the rest that lasts as long as each note and write its beats (a quarter note gets 1 beat). Then add up the beats of silence in each measure.', i: 'I can match each note to its rest and count beats of silence.',
        ex: example('The whole rest hangs below the line; the half rest sits on top of it. A dot adds half the value.', 'Dotted half rest = 2 + 1 = 3 beats.'), w: 'Mixing up the whole rest (hangs) and the half rest (sits).' };
    case 'solfa': return { d: g === 1 ? 'So is on the top line, mi is on the bottom line. Write so or mi under each note, then sing the pattern.' : g === 2 ? 'Mi is on the bottom line, so on the middle line and la in the space just above so. Write the solfège under each note, then sing it.' : 'Do is on the second line. Write do, re, mi, so or la under each note, then sing the pattern with hand signs.',
      i: 'I can read solfège on the staff and sing it.', ex: example(g <= 2 ? 'So is higher than mi. La is one step higher than so.' : 'From do: re is one step up, mi two steps up, so is a skip above mi, la a step above so.', g === 1 ? 'so mi so so' : g === 2 ? 'so la so mi' : 'do re mi so la'), w: 'Reading a space note as the line below it.' };
    case 'motion': return { d: 'Look at each pair of notes. Write step (next line or space), skip (jumps one line or space) or repeat (same note).', i: 'I can see steps, skips and repeats in a melody.',
      ex: example('Line to the next space is a step. Line to the next line is a skip. Same place is a repeat.', 'G to A: step. G to B: skip. G to G: repeat.'), w: 'Calling line-to-line a step; it skips over a space.' };
    case 'names': return { d: `Write the letter name under each note.${v.clef === 'grand' ? ' Check the clef of each staff first.' : ''}`, i: 'I can name the notes on the staff.',
      ex: example(v.clef === 'bass' ? 'Bass clef lines from the bottom: G B D F A (Good Boys Do Fine Always). Spaces: A C E G (All Cows Eat Grass).' : v.clef === 'treble' || g <= 4 ? 'Treble clef lines from the bottom: E G B D F (Every Good Boy Does Fine). Spaces: F A C E.' : 'Treble lines E G B D F, spaces F A C E. Bass lines G B D F A, spaces A C E G. Middle C sits on one ledger line between the staves.', 'Ledger lines keep the pattern going: line, space, line, space.'),
      w: 'Using treble names on the bass staff, and losing count on ledger lines.' };
    case 'words': return { d: 'Name each note. The letters spell a word. Write the word on the line.', i: 'I can read note names quickly enough to spell words.',
      ex: example('Lines E G B D F; spaces F A C E.', 'Notes on space 2, space 3, line 1 spell A C E: ACE.'), w: 'Mixing up the lines and spaces in the middle of the staff.' };
    case 'draw': return { d: 'Draw a whole note for each letter in the place shown: on a line, in a space, below or above the staff. Use ledger lines when you need them.', i: 'I can draw a note for its letter name.',
      ex: example('Find the letter on the staff, then check: is it on a line or in a space?', 'Treble E on a line is the bottom line. Treble E in a space is the top space.'), w: 'Drawing the note half on a line and half in a space; make it clearly one or the other.' };
    case 'steps': return { d: 'Two keys are marked on each keyboard. Write H if they are a half step apart (next key, black or white) or W if they are a whole step apart (two half steps).', i: 'I can find whole steps and half steps on a keyboard.',
      ex: example('A half step goes to the very next key. A whole step skips exactly one key.', 'C to C♯: half step. C to D: whole step. E to F: half step (no black key between).'), w: 'Calling E to F and B to C whole steps because both are white keys.' };
    case 'scales': return { d: `Write the scale up from the given note, one note on each line or space, adding sharps or flats where the pattern needs them. Write each letter name under its note${v.scale === 'maj' || v.scale === 'nmin' ? ' and W or H between notes' : ''}.${v.kb && g <= 8 ? ' Mark the scale on the keyboard with dots.' : ''}`,
      i: 'I can build a scale from its step pattern.', ex: example({ maj: 'Major: W W H W W W H.', nmin: 'Natural minor: W H W W H W W.', hmin: 'Harmonic minor: natural minor with degree 7 raised a half step.', mmin: 'Melodic minor going up: natural minor with degrees 6 and 7 raised.', forms: 'Natural minor: W H W W H W W. Harmonic: raise 7. Melodic going up: raise 6 and 7.', penta: 'Major pentatonic: degrees 1, 2, 3, 5 and 6 of the major scale.' }[v.scale], { maj: 'G major: G A B C D E F♯ G.', nmin: 'A minor: A B C D E F G A.', hmin: 'A harmonic minor: A B C D E F G♯ A.', mmin: 'A melodic minor: A B C D E F♯ G♯ A.', forms: 'A minor: natural A B C D E F G A; harmonic G♯; melodic F♯ G♯.', penta: 'C pentatonic: C D E G A C.' }[v.scale]),
      w: 'Skipping a letter or using one twice (each letter once), and writing E♭ where the pattern needs D♯.' };
    case 'keysig': return { d: 'Name the key of each key signature. Then write the key signatures asked for, in order, on the staff.', i: 'I can name and write key signatures.',
      ex: example('Sharps: the last sharp is a half step below the major key (F♯ C♯: D major). Flats: the next-to-last flat names the major key (B♭ E♭ A♭: E♭ major). The relative minor is 3 half steps below the major.', 'Sharps go in the order F C G D A E B; flats B E A D G C F.'),
      w: 'Writing sharps in the wrong order or octave, and naming the major key when the minor was asked.' };
    case 'intervals': return { d: g <= 6 ? 'Count the lines and spaces from the lower note to the upper note, counting both notes. Write the interval number. Then draw the intervals asked for.' : 'Name each interval with its quality and number (M = major, m = minor, P = perfect, A = augmented, d = diminished). Then draw the upper note for each interval asked for.',
      i: 'I can name and build intervals.', ex: example(g <= 6 ? 'Count every line and space, including both notes.' : 'Count letters for the number, then half steps for the quality: M3 = 4 half steps, m3 = 3, P5 = 7.', g <= 6 ? 'C up to G: C D E F G = a 5th.' : 'D up to F: 3 letters, 3 half steps = m3.'), w: 'Starting the count at zero, and naming by half steps alone (C to E♭ and C to D♯ are both 3 half steps but are a m3 and an A2).' };
    case 'triads': return { d: 'Name each triad: root letter and quality. Then build each triad asked for, root on the bottom, and write its notes.', i: 'I can build and name triads.',
      ex: example('A triad stacks two thirds: root, third, fifth. Major = 4 + 3 half steps. Minor = 3 + 4.' + (g >= 7 ? ' Diminished = 3 + 3. Augmented = 4 + 4.' : ''), 'D F♯ A is D major; D F A is D minor.'), w: 'Leaving out a sharp or flat the key needs, and reading the top note as the root.' };
    case 'inversions': return { d: 'Name each chord: root, quality, position and bass note. Then write each chord in root position, first inversion and second inversion.', i: 'I can name and write triads in every inversion.',
      ex: example(`Stack the notes in thirds to find the root. Root in the bass: root position${g >= 9 ? ' (5/3)' : ''}. Third in the bass: 1st inversion${g >= 9 ? ' (6)' : ''}. Fifth in the bass: 2nd inversion${g >= 9 ? ' (6/4)' : ''}.`, 'E G C is C major, 1st inversion, bass E.'), w: 'Naming the bass note as the root.' };
    case 'diatonic': return { d: 'Write the chord on each degree of the scale using only notes of the key. Label each with its Roman numeral (upper case for major, lower case for minor, ° for diminished) and quality.', i: 'I can build the chords of a key and label them with Roman numerals.',
      ex: example(v.chords === 'sev' && g >= 9 ? 'In every major key: Imaj7 ii7 iii7 IVmaj7 V7 vi7 viiø7.' : 'In every major key: I ii iii IV V vi vii°.', 'In C major, the chord on G (degree 5) is G B D: V, major.'), w: 'Adding accidentals the key signature already gives, and writing upper case for minor chords.' };
    case 'symbols': return { d: 'Write each chord on the staff in root position and list its notes.' + (v.kb && g <= 8 ? ' Mark it on the keyboard too.' : ''), i: 'I can turn a chord symbol into notes.',
      ex: example('C = major triad. Cm = minor. C7 = major triad + minor 7th. Cmaj7 = major triad + major 7th. Cm7 = minor triad + minor 7th.' + (g >= 9 ? ' Cm7♭5 = diminished triad + minor 7th.' : ''), 'G7: G B D F. Fmaj7: F A C E.'), w: 'Using a major 7th for a plain 7 chord.' };
    default: return { d: g <= 2 ? 'Make up your own music. Write a note or rest for every beat, and write the rhythm words under it.' : 'Compose your piece on the staff. Fill each measure with the right number of beats.', i: 'I can write my own music down so others can play it.',
      ex: '', w: 'Measures that do not add up, and a missing double bar.' };
  }
}

Gen.add('music-notation', {
  title: 'Music Notation and Rhythm', type: 'Practice',
  css: `.mu-grid{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:6px 14px;margin:4px 0 8px}
.mu-cell{break-inside:avoid;min-width:0}
.mu-cell .gen-svg,.mu-line .gen-svg{margin:2px 0}
.mu-line{break-inside:avoid;margin:2px 0 6px}
.mu-row{display:flex;align-items:center;gap:14px}
.mu-row .gen-svg{flex:0 1 auto}
.mu-listen{display:flex;align-items:flex-start;gap:6px}
.mu-cap{margin:2px 0;font-size:14px}
.mu-ans{margin:0 0 4px;font-size:14px}
.mu-sym{font-size:16px}
.mu-sort{margin:0 0 12px;font-size:14px}
.mu-hints{display:flex;flex-wrap:wrap;gap:2px 14px;margin:0 0 6px;padding-left:1.4em;font-size:12.5px;color:#444}
.mu-hints li{margin-right:10px}
.mu-head{display:flex;flex-wrap:wrap;gap:6px 22px;margin:2px 0 8px;font-size:14px}
.mu-wl{display:inline-block;min-width:2.2in;border-bottom:1px solid #444;height:1em;vertical-align:baseline}
.mu-wl.mu-short{min-width:1.1in}
.mu-check{display:flex;flex-wrap:wrap;gap:4px 18px;list-style:none;padding:0;margin:6px 0 0;font-size:13px}
.mu-check li::before{content:'';display:inline-block;width:.8em;height:.8em;border:1.5px solid #333;margin-right:6px;vertical-align:-1px}
.mu-tlist{margin:4px 0 0 1.2em;padding:0}`,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '3' },
    { id: 'skill', label: 'Skill', type: 'select', options: skillOpts, def: 'rhythm' },
    { id: 'meter', label: 'Time signature', type: 'select', options: meterOpts, def: '4', show: v => RHY.includes(v.skill) && v.grade !== 'k' },
    { id: 'focus', label: 'Rhythm focus', type: 'select', options: focusOpts, def: 'all', show: hasFocus },
    { id: 'clef', label: 'Clef', type: 'select', options: clefOpts, def: 'treble', show: v => hasClef(v) && gn(v.grade) >= 5 },
    { id: 'range', label: 'Note range', type: 'select', options: v => [['staff', 'On the staff only'], ['ledger', gn(v.grade) <= 4 ? 'With ledger lines (middle C to high A)' : 'With ledger lines (up to two above and below)']], def: 'staff', show: v => ['names', 'draw', 'words'].includes(v.skill) },
    { id: 'spell', label: 'Add 4 note-name words to decode', type: 'check', def: false, show: v => v.skill === 'names' && gn(v.grade) <= 5 },
    { id: 'scale', label: 'Scale', type: 'select', options: scaleOpts, def: 'maj', show: v => v.skill === 'scales' },
    { id: 'tonic', label: 'Starting note', type: 'select', options: tonicOpts, def: 'any', show: v => v.skill === 'scales' || v.skill === 'diatonic' },
    { id: 'keys', label: 'Keys', type: 'select', options: keysOpts, def: 'maj', show: v => v.skill === 'keysig' },
    { id: 'chords', label: 'Chords', type: 'select', options: v => (gn(v.grade) >= 9 ? [['tri', 'Triads'], ['sev', 'Seventh chords']] : [['tri', 'Triads']]), def: 'tri', show: v => v.skill === 'diatonic' },
    { id: 'kb', label: 'Add a keyboard to mark the notes on', type: 'check', def: true, show: v => ['scales', 'triads', 'symbols'].includes(v.skill) && gn(v.grade) <= 8 },
    { id: 'fixpart', label: 'Add 4 measures to check and fix', type: 'check', def: false, show: v => v.skill === 'rhythm' && gn(v.grade) >= 3 },
    { id: 'lines', label: 'Staff', type: 'select', options: linesOpts, def: 'treble', show: v => v.skill === 'staff' },
    { id: 'bars', label: 'Measures', type: 'select', options: barsOpts, def: '8', show: v => v.skill === 'staff' },
    { id: 'form', label: 'Form labels', type: 'select', options: [['none', 'None'], ['ab', 'AB (two sections)'], ['aba', 'ABA (three sections)']], def: 'none', show: v => v.skill === 'staff' && gn(v.grade) >= 3 },
    { id: 'topic', label: 'Title of the piece (optional)', type: 'text', def: '', show: v => v.skill === 'staff' },
    { id: 'count', label: 'Length', type: 'select', options: countOpts, def: 'm', show: v => v.skill !== 'staff' },
  ],
  make(v, r) {
    const g = gn(v.grade), sk = v.skill;
    const out = MAKERS[sk](v, r, g);
    const t = texts(sk, g, v), gname = GRADES.find(x => x[0] === v.grade)[1];
    const parts = (t.ex ? [part('', t.ex)] : []).concat(out.parts);
    const rhy = RHY.includes(sk) && g > 0 && sk !== 'staff';
    const level = [gname, rhy ? (v.meter === 'mix' ? 'mixed meters' : meterTxt(v.meter)) : '', hasClef(v) && g >= 5 ? { treble: 'treble clef', bass: 'bass clef', both: 'treble and bass clefs', grand: 'grand staff' }[v.clef] : '',
      sk === 'scales' ? TYPE_NAME[v.scale] : '', hasFocus(v) && v.focus !== 'all' ? focusOpts(v).find(x => x[0] === v.focus)?.[1].toLowerCase() : ''].filter(Boolean).join(', ');
    const notes = {
      listen: 'The key circles the rhythm to clap in each row; the list on this page says it aloud as you would count it.',
      dictate: 'The key draws each rhythm in red. Clap from the list on this page.',
      staff: 'The key shows a short model in red in the first measures; any music that keeps the meter is right.',
      keysig: 'Key signatures follow the standard order and octave placement for each clef.',
      names: 'Notes never repeat back to back. With ledger lines on, about half the notes sit off the staff.',
    }[sk] || 'Every answer on the key was worked twice by the generator. Press New sheet for a fresh set at the same level.';
    return {
      title: `${skillName(sk, g).replace(/ \(.*\)$/, '')}: ${gname}`, level,
      ican: t.i, directions: t.d, minutes: g <= 2 ? 15 : 20,
      materials: ['scales', 'triads', 'symbols'].includes(sk) && v.kb && g <= 8 ? 'pencil, colored pencil for the keyboard' : sk === 'listen' || sk === 'dictate' ? 'pencil; the teacher claps' : 'pencil',
      parts, items: out.items, mistakes: t.w, notes, teacher: out.teacher,
    };
  },
  verify(s, v) {
    const out = [];
    const g = gn(v.grade);
    const beatsIn = (ev, m) => ev.reduce((a, e) => a + e.d, 0) * METER[m][1] === 16 * METER[m][0];   // sum in whole notes = top/bottom
    const vCounts = (ev, m) => {   // walk the ticks independently
      const res = [];
      let at = 0;
      const starts = new Map(ev.map(e => { const z = [at, e]; at += e.d; return z; }));
      let cur = null, end = 0;
      for (let t = 0; t < at; t++) {
        if (starts.has(t)) {
          cur = starts.get(t); end = t + cur.d;
          const qb = m === '6' ? t / 2 : t / 4, b = Math.floor(qb) + 1, fr = qb - Math.floor(qb);
          const lab = m === '6' ? String(b) : fr === 0 ? String(b) : fr === 0.25 ? 'e' : fr === 0.5 ? '&' : 'a';
          res.push(cur.r ? `(${lab})` : lab);
        } else if (t < end && t % (m === '6' ? 2 : 4) === 0) res.push(`(${m === '6' ? t / 2 + 1 : t / 4 + 1})`);
      }
      return res.join(' ');
    };
    const vSyl = ev => ev.map(e => (e.r ? 'rest' : { 1: 'ta', 0.5: 'ti', 2: 'ta-a' }[e.d / 4])).join(' ');
    const letterAt = (clef, p) => {
      const lines = clef === 'treble' ? 'EGBDF' : 'GBDFA', spaces = clef === 'treble' ? 'FACE' : 'ACEG', cyc = clef === 'treble' ? 'EFGABCD' : 'GABCDEF';
      if (p >= 0 && p <= 8) return p % 2 === 0 ? lines[p / 2] : spaces[(p - 1) / 2];
      return cyc[((p % 7) + 7) % 7];
    };
    const semis = (a, b) => midi(b) - midi(a);
    const nmV = n => 'CDEFGAB'[n.l] + (n.a === 1 ? '♯' : n.a === -1 ? '♭' : '');
    const rel = ns => ns.slice(1).map(n => semis(ns[0], n));
    const QV = { '4,7': 'major', '3,7': 'minor', '3,6': 'diminished', '4,8': 'augmented', '4,7,11': 'major 7th', '4,7,10': 'dominant 7th', '3,7,10': 'minor 7th', '3,6,10': 'half-diminished 7th', '3,6,9': 'diminished 7th' };
    const thirds = ns => ns.slice(1).every((n, i) => dia(n) - dia(ns[i]) === 2);
    const scaleCount = (tonicName, minor) => {   // count the sharps or flats in a scale built by step pattern
      const pat = minor ? 'WHWWHWW' : 'WWHWWWH';
      let n = noteOf(tonicName, 4), sh = 0, fl = 0;
      for (let i = 0; i < 7; i++) { if (n.a === 1) sh++; if (n.a === -1) fl++; const nx = above(n, 1, pat[i] === 'W' ? 2 : 1); if (!nx) return null; n = nx; }
      return sh && fl ? null : sh - fl;
    };
    for (const it of s.items) {
      switch (it.k) {
        case 'cnt': {
          it.ms.forEach((ev, i) => { if (!beatsIn(ev, it.m)) out.push(`${it.q}: measure ${i + 1} does not fill ${it.m}`); });
          const want = it.mode === 'sounds' ? String(it.ms.flat().filter(e => !e.r).length) : it.ms.map(ev => (it.mode === 'syl' ? vSyl(ev) : vCounts(ev, it.m))).join(' | ');
          if (it.a !== want) out.push(`${it.q}: key ${it.a}, want ${want}`);
          break;
        }
        case 'model': if (!beatsIn(it.ev, it.m)) out.push(`${it.q}: model measure does not fill`); break;
        case 'listen': {
          if (new Set(it.ch).size !== 3) out.push(`${it.q}: choices repeat`);
          it.chev.forEach(ev => { if (!beatsIn(ev, it.m)) out.push(`${it.q}: a choice does not fill`); });
          if (it.a !== 'ABC'[it.idx]) out.push(`${it.q}: key ${it.a}`);
          break;
        }
        case 'comp': {
          const rest2 = it.ev.filter((e, i) => i !== it.gi).reduce((a, e) => a + e.d, 0), miss = METER[it.m][2] - rest2;
          if (!beatsIn(it.ev, it.m) || miss !== it.ev[it.gi].d || !it.a.startsWith(VAL[miss])) out.push(`${it.q}: missing ${miss}, key ${it.a}`);
          break;
        }
        case 'bars': {
          const T = 16 * METER[it.m][0] / METER[it.m][1];
          let sum = 0;
          const after = [];
          it.ev.forEach((e, i) => { sum += e.d; if (sum % T === 0 && i < it.ev.length - 1) after.push(i + 1); });
          const short = sum % T ? T - (sum % T) : 0;
          if (after.join(',') !== it.after.join(',') || short !== it.short) out.push(`${it.q}: bars ${after} short ${short}`);
          break;
        }
        case 'fix': {
          const tot = it.ev.reduce((a, e) => a + e.d, 0);
          if (it.a !== beatsTxt(tot, it.m) || it.bad !== !beatsIn(it.ev, it.m)) out.push(`${it.q}: key ${it.a}`);
          break;
        }
        case 'restval': if (!it.a.startsWith(VAL[it.d] + ' rest') || !it.a.includes(beatsTxt(it.d, '4'))) out.push(`${it.q}: key ${it.a}`); break;
        case 'silence': if (!beatsIn(it.ev, it.m) || it.a !== beatsTxt(it.ev.filter(e => e.r).reduce((a, e) => a + e.d, 0), it.m)) out.push(`${it.q}: key ${it.a}`); break;
        case 'restbeat': {
          let t = 0;
          const b = [];
          it.ev.forEach(e => { if (e.r) b.push(t / 4 + 1); t += e.d; });
          if (!b.length || !it.a.endsWith(b.join(' and '))) out.push(`${it.q}: key ${it.a}`);
          break;
        }
        case 'solfa': {
          const syl = it.kind === 'treble' ? { 2: 'do', 3: 're', 4: 'mi', 6: 'so', 7: 'la' } : { 0: 'mi', 2: 'so', 3: 'la' };
          const pitches = it.ps.map(p => (it.kind === 'treble' ? letterAt('treble', p) : p));
          if (it.kind === 'treble' && pitches.some(L => !'GABDE'.includes(L))) out.push(`${it.q}: off the do pentatonic`);
          const want = it.ps.map(p => syl[p]).join(' ');
          if (it.a !== want || /undefined/.test(want)) out.push(`${it.q}: key ${it.a}, want ${want}`);
          if (it.kind === 'two' && it.ps.some(p => p === 3)) out.push(`${it.q}: la on a 2-line staff`);
          break;
        }
        case 'motion': { const d = Math.abs(it.p2 - it.p1), want = d === 0 ? 'repeat' : d === 1 ? 'step' : d === 2 ? 'skip' : 'leap'; if (it.a !== want) out.push(`${it.q}: key ${it.a}, want ${want}`); break; }
        case 'name': if (it.a !== letterAt(it.clef, it.p)) out.push(`${it.q}: key ${it.a}, want ${letterAt(it.clef, it.p)}`); break;
        case 'word': { const w = it.ps.map(p => letterAt(it.clef, p)).join(''); if (w !== it.a) out.push(`${it.q}: spells ${w}, key ${it.a}`); break; }
        case 'draw': {
          const cands = [];
          for (let p = it.lo; p <= it.hi; p++) if (letterAt(it.clef, p) === it.L && where(p) === it.wh) cands.push(p);
          if (cands.length !== 1 || cands[0] !== it.p) out.push(`${it.q}: places ${cands}`);
          break;
        }
        case 'step': {
          // count keys along the keyboard: white keys C D E F G A B with black keys after C D F G A
          const keys = [];
          for (let o = 0; o < 2; o++) for (const L of 'CDEFGAB') { keys.push(L); if ('CDFGA'.includes(L)) keys.push(L + '#'); }
          const d = it.a2 - it.a1;
          if (it.a !== (d === 1 ? 'H' : d === 2 ? 'W' : '?') || it.a2 >= keys.length) out.push(`${it.q}: key ${it.a}`);
          break;
        }
        case 'nat': { const pairs = []; for (let i = 0; i < 7; i++) if (NAT[(i + 1) % 7] - NAT[i] === 1 || NAT[(i + 1) % 7] + 12 - NAT[i] === 1) pairs.push(LET[i] + ' and ' + LET[(i + 1) % 7]); if (it.a !== pairs.join(', ')) out.push(`${it.q}: ${pairs}`); break; }
        case 'scale': {
          const ns = it.notes, want = { maj: 'WWHWWWH', nmin: 'WHWWHWW', hmin: 'WHWWHAH', mmin: 'WHWWWWH', penta: 'WWAWA' }[it.ty];
          const got = ns.slice(1).map((n, i) => ({ 1: 'H', 2: 'W', 3: 'A' }[semis(ns[i], n)] || '?')).join('');
          const letters = ns.every((n, i) => !i || dia(n) - dia(ns[i - 1]) === (it.ty === 'penta' && (i === 3 || i === 5) ? 2 : 1));
          if (got !== want || !letters || it.a !== ns.map(nmV).join(' ') || nmV(ns[0]) !== it.name) out.push(`${it.q}: steps ${got}`);
          break;
        }
        case 'wh': { const got = it.notes.slice(1).map((n, i) => (semis(it.notes[i], n) === 1 ? 'H' : 'W')).join(' '); if (got !== it.a) out.push(`${it.q}: ${got}`); break; }
        case 'deg': { const sc = scaleOf(noteOf(it.name, 4), it.ty); if (!sc || nmV(sc[it.d - 1]) !== it.a) out.push(`${it.q}: key ${it.a}`); break; }
        case 'pleft': { const m = scaleOf(it.t, 'maj'), p = scaleOf(it.t, 'penta').map(nmV); const left = m.slice(0, 7).map(nmV).filter(x => !p.includes(x)); if (!it.a.startsWith(left.join(' and '))) out.push(`${it.q}: ${left}`); break; }
        case 'text': break;
        case 'ksname': {
          const parts = it.a.split(', ');
          for (const p of parts) { const [ton, mode] = p.split(' '); const c = scaleCount(ton, mode === 'minor'); if (c !== it.n) out.push(`${it.q}: ${p} has ${c}`); }
          if ((it.mode === 'rel') !== (parts.length === 2)) out.push(`${it.q}: mode`);
          break;
        }
        case 'kswrite': {
          const [ton, mode] = it.what.split(' '), c = scaleCount(ton, mode === 'minor');
          const listed = (it.a.split(': ')[1] || '').split(' ');
          const order = c > 0 ? 'FCGDAEB' : 'BEADGCF';
          if (c !== it.n || listed.length !== Math.abs(c) || listed.some((x, i) => x[0] !== order[i])) out.push(`${it.q}: ${it.a}, scale count ${c}`);
          break;
        }
        case 'int': case 'ibuild': {
          const num = dia(it.top) - dia(it.b) + 1, st = semis(it.b, it.top);
          const perfect = { 1: 0, 4: 5, 5: 7, 8: 12 }, major = { 2: 2, 3: 4, 6: 9, 7: 11 };
          let q;
          if (num in perfect) q = { 0: 'P', 1: 'A', '-1': 'd' }[st - perfect[num]];
          else q = { 0: 'M', '-1': 'm', 1: 'A', '-2': 'd' }[st - major[num]];
          const want = it.k === 'int' ? (g <= 6 ? ORD[num] : q + num) : nmV(it.top);
          if (!q || it.a !== want) out.push(`${it.q}: key ${it.a}, want ${want}`);
          if (it.k === 'ibuild' && (q + num !== it.iv[0])) out.push(`${it.q}: built ${q}${num}`);
          break;
        }
        case 'triad': case 'tbuild': case 'sym': {
          const ns = it.ns, qv = QV[rel(ns).join(',')];
          if (!thirds(ns) || !qv) { out.push(`${it.q}: not a stack of thirds`); break; }
          if (it.k === 'triad' && it.a !== `${nmV(ns[0])} ${qv}`) out.push(`${it.q}: key ${it.a}, want ${nmV(ns[0])} ${qv}`);
          if (it.k !== 'triad' && (it.a !== ns.map(nmV).join(' ') || qv !== QNAME[it.qual] || nmV(ns[0]) !== nmV(it.root))) out.push(`${it.q}: key ${it.a}`);
          if (it.k === 'sym' && !it.sym.startsWith(nmV(ns[0]))) out.push(`${it.q}: symbol root`);
          break;
        }
        case 'inv': case 'ibuildch': {
          // find the root: the note whose stack of thirds holds the others
          const ns = it.ns;
          let root = null, inv = -1;
          for (let k = 0; k < 3; k++) {
            const st = ns.slice(k).concat(ns.slice(0, k).map(n => ({ ...n, o: n.o + 1 })));
            if (thirds(st)) { root = st; inv = (3 - k) % 3; }
          }
          if (!root) { out.push(`${it.q}: no root`); break; }
          const qv = QV[rel(root).join(',')], INVV = ['root position', '1st inversion', '2nd inversion'];
          if (it.k === 'inv') { if (!it.a.startsWith(`${nmV(root[0])} ${qv}, ${INVV[inv]}`) || !it.a.endsWith(`bass ${nmV(ns[0])}`)) out.push(`${it.q}: key ${it.a}, root ${nmV(root[0])} ${qv} ${INVV[inv]}`); }
          else if (inv !== it.inv || qv !== QNAME[it.qual] || nmV(root[0]) !== nmV(it.root) || !it.a.endsWith(`(bass ${nmV(ns[0])})`)) out.push(`${it.q}: built ${nmV(root[0])} ${qv} ${INVV[inv]}`);
          break;
        }
        case 'dia': {
          const sc = scaleOf(noteOf(it.kname, 4), 'maj').map(nmV), ns = it.ns, qv = QV[rel(ns).join(',')];
          if (!thirds(ns) || ns.some(n => !sc.includes(nmV(n)))) out.push(`${it.q}: notes outside the key`);
          if (nmV(ns[0]) !== sc[it.d]) out.push(`${it.q}: wrong root`);
          const R = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'][it.d], lower = /minor|diminished/.test(qv) || qv === 'minor 7th';
          const numWant = (lower ? R.toLowerCase() : R) + { major: '', minor: '', diminished: '°', augmented: '+', 'major 7th': 'maj7', 'dominant 7th': '7', 'minor 7th': '7', 'half-diminished 7th': 'ø7', 'diminished 7th': '°7' }[qv];
          if (it.a !== `${numWant} ${qv}`) out.push(`${it.q}: key ${it.a}, want ${numWant} ${qv}`);
          break;
        }
        case 'sort': { if (it.quals.join(',') !== 'maj,min,min,maj,maj,min,dim') out.push(`${it.q}: major key pattern ${it.quals}`); break; }
        default: out.push(`unknown kind ${it.k}`);
      }
    }
    return out;
  },
});
})();
