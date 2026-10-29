// Curio Class family engine: stage (stage-blocker, director-s-chair). Docs: docs/families/stage.md
// Inlined by scripts/bundle_tool.py from a kit:stage script tag, after kit:curio. Exposes one global, Stage.
// Never write a literal closing script tag in this file (the bundler inlines it between script tags).
//
// World frame: meters. x runs from house left to house right (x = 0 on the center line; stage right, the actor's
// right facing the house, is negative x). y runs upstage from the apron edge (the house is at negative y). z is up
// from the stage floor. Actor facing is in degrees: 0 faces straight out to the house (-y), 90 faces house right
// (+x, the actor's left), 180 faces upstage. Turning left adds 45.
// Sizes, thresholds and focus weights are stage-blocker's own choices (a rough guide), not facts.
const Stage = (() => {
  const D2R = Math.PI / 180;
  const clone = o => JSON.parse(JSON.stringify(o));
  const hyp = Math.hypot;
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const num = v => Math.round(v * 10) / 10;
  const list = a => a.length < 2 ? a.join('') : a.slice(0, -1).join(', ') + ' and ' + a[a.length - 1];

  // ---------- the set catalog: a tool registers its pieces (Stage.addPieces) ----------
  // {type: {label, w, d, h, color, sit, standable, opening, entrance, round, parts}}
  //   w along x and d along y before rotation; sit: actors dropped on it sit; standable: a level actors stand on;
  //   opening: a gap (m) in the middle, full height up to h - lintel (a door flat), entrance: its entrance id;
  //   round: drawn and tested as a cylinder of diameter w; parts: [{w, d, z0, z1, round}] to override one solid.
  const catalog = {};
  function addPieces(c) { Object.assign(catalog, c); return catalog; }

  // ---------- focus weights (stage-blocker's spec, "Focus"): a rough model of common directing rules ----------
  const WEIGHTS = {
    speak: 3, light: [-3, 1, 2], spot: 2,
    pos: {'full front': 2, 'one-quarter': 1.5, 'profile': 1, 'three-quarter': 0, 'full back': -1},
    level: 1, standAlone: 1, row: {down: 1, center: .5, up: 0}, crossed: 1.5, crossM: .5,
    gaze: 1, gazeDeg: 30, alone: 1, aloneM: 1.5, partly: -2,
    terms: [],   // extra terms: [{id, fn(actor, ctx) -> {score, reason} or null}] (director-s-chair: chorusGaze, address)
  };
  const POSES = {stand: 1.6, sit: 1.2, kneel: .9};
  const HEAD_R = .12, BODY_R = .25;

  // ---------- houses ----------
  function inPoly(poly, x, y) {
    let c = false;
    for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
      const [xi, yi] = poly[i], [xj, yj] = poly[j];
      if ((yi > y) !== (yj > y) && x < (xj - xi) * (y - yi) / (yj - yi) + xi) c = !c;
    }
    return c;
  }
  function bounds(polys) {
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const p of polys) for (const [x, y] of p) { x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
    return {x0, y0, x1, y1};
  }
  // Stage.house(def): fills in defaults and derived values. See the family doc for every field.
  function house(def) {
    const h = Object.assign({stageH: 0, areas: [], spots: {}, entrances: [], levels: [], blockers: [], wings: [], seats: [],
      frame: 'open', light: 'areas', spotR: 1, focusSeats: null, upSeat: null, look: null, curtainY: null}, clone(def));
    h.entrances = h.entrances.map(e => ({...e, at: typeof e.at[0] === 'number' ? [e.at] : e.at}));
    const b = bounds([h.outline]);
    h.box = b;
    if (!h.look) h.look = [(b.x0 + b.x1) / 2, (b.y0 + b.y1) / 2, 1.2];
    if (!h.focusSeats) h.focusSeats = h.seats.length ? [h.seats[Math.floor(h.seats.length / 2)].id] : [];
    if (!h.upSeat) h.upSeat = h.focusSeats[Math.floor(h.focusSeats.length / 2)] || (h.seats[0] || {}).id;
    // the plan's extents: everything drawn, plus a margin
    const all = [h.outline, ...h.wings.map(w => w.poly), ...h.levels.map(l => l.poly), ...h.blockers.filter(x => !x.hideInPlan).map(x => x.poly),
      h.seats.filter(s => !s.planAt).map(s => [[s.x, s.y]]), h.seats.filter(s => s.planAt).map(s => s.planAt)];
    const pb = bounds(all.filter(p => p.length));
    h.planBox = h.planBox || {x0: pb.x0 - .5, y0: pb.y0 - .6, x1: pb.x1 + .5, y1: pb.y1 + .6};
    h.seatById = Object.fromEntries(h.seats.map(s => [s.id, s]));
    return h;
  }
  const seatOf = (h, s) => typeof s === 'string' ? h.seatById[s] : s;
  function areaOf(h, x, y) { const a = h.areas.find(a => inPoly(a.poly, x, y)); return a || null; }
  function onStage(h, x, y) { return inPoly(h.outline, x, y) || h.levels.some(l => inPoly(l.poly, x, y)); }

  // ---------- pieces as solids ----------
  function rotPts(p, pts) {
    const c = Math.cos((p.rot || 0) * D2R), s = Math.sin((p.rot || 0) * D2R);
    return pts.map(([u, v]) => [p.x + u * c - v * s, p.y + u * s + v * c]);
  }
  function rect(w, d, ox = 0, oy = 0) { return [[ox - w / 2, oy - d / 2], [ox + w / 2, oy - d / 2], [ox + w / 2, oy + d / 2], [ox - w / 2, oy + d / 2]]; }
  function circ(r, n = 12, ox = 0, oy = 0) { return Array.from({length: n}, (_, i) => [ox + r * Math.cos(i / n * 2 * Math.PI), oy + r * Math.sin(i / n * 2 * Math.PI)]); }
  // solids of one piece: [{poly (world xy), z0, z1, round: {x, y, r} or null, id, part}]
  function solids(p) {
    const c = catalog[p.type]; if (!c) return [];
    let parts = c.parts;
    if (!parts) {
      if (c.opening) {
        const side = (c.w - c.opening) / 2, lintel = c.lintel || .3;
        parts = [{w: side, d: c.d, ox: -(c.opening + side) / 2, z0: 0, z1: c.h}, {w: side, d: c.d, ox: (c.opening + side) / 2, z0: 0, z1: c.h},
          {w: c.opening, d: c.d, ox: 0, z0: c.h - lintel, z1: c.h}];
      } else parts = [{w: c.w, d: c.d, z0: 0, z1: c.h, round: c.round}];
    }
    return parts.map((q, i) => {
      const ox = q.ox || 0, oy = q.oy || 0;
      if (q.round) {
        const [cx, cy] = rotPts(p, [[ox, oy]])[0];
        return {poly: circ(q.w / 2, 12, cx, cy), z0: q.z0, z1: q.z1, round: {x: cx, y: cy, r: q.w / 2}, id: p.id, part: i, color: q.color};
      }
      return {poly: rotPts(p, rect(q.w, q.d, ox, oy)), z0: q.z0, z1: q.z1, round: null, id: p.id, part: i, color: q.color};
    });
  }
  function footprint(p) { const c = catalog[p.type] || {w: .5, d: .5}; return c.round ? rotPts(p, circ(c.w / 2, 12)) : rotPts(p, rect(c.w, c.d)); }
  // levels: the house's own plus standable pieces (platforms)
  function levels(snap, h) {
    return [...h.levels, ...(snap.pieces || []).filter(p => (catalog[p.type] || {}).standable).map(p => ({id: p.id, poly: footprint(p), h: catalog[p.type].h, piece: true}))];
  }
  function levelH(snap, h, id) { if (!id) return 0; const l = levels(snap, h).find(l => l.id === id); return l ? l.h : 0; }

  // ---------- actors ----------
  const on = a => a && !a.off;
  const byId = (snap, id) => (snap.cast || []).find(a => a.id === id);
  function headZ(a, snap, h) { return (POSES[a.pose] || POSES.stand) + levelH(snap, h, a.on); }
  function facingVec(f) { return [Math.sin(f * D2R), -Math.cos(f * D2R)]; }
  function angleTo(a, x, y) {   // degrees between a's facing and the direction from a to (x, y)
    const [fx, fy] = facingVec(a.facing || 0), dx = x - a.x, dy = y - a.y, d = hyp(dx, dy) || 1e-9;
    return Math.acos(clamp((fx * dx + fy * dy) / d, -1, 1)) / D2R;
  }
  const POS = ['full front', 'one-quarter', 'profile', 'three-quarter', 'full back'];
  function bodyPos(a, seat) {
    const g = angleTo(a, seat.x, seat.y);
    return g < 22.5 ? POS[0] : g < 67.5 ? POS[1] : g < 112.5 ? POS[2] : g < 157.5 ? POS[3] : POS[4];
  }
  // letters and digits only: "O'Neil" gives On, not O'
  function initials(name) { const w = String(name || '').trim().split(/\s+/).map(x => x.replace(/[^\p{L}\p{N}]/gu, '')).filter(Boolean); if (!w.length) w.push('?'); return w.length > 1 ? (w[0][0] + w[1][0]).toUpperCase() : w[0].slice(0, 1).toUpperCase() + w[0].slice(1, 2).toLowerCase(); }

  // ---------- sightlines ----------
  // a segment E -> P (t in 0..tmax) against a convex prism (poly, z0..z1): Cyrus-Beck
  function hitPrism(E, P, s, tmax) {
    let t0 = 1e-6, t1 = tmax;
    const d = [P[0] - E[0], P[1] - E[1], P[2] - E[2]];
    if (s.round) {
      const fx = E[0] - s.round.x, fy = E[1] - s.round.y, a = d[0] * d[0] + d[1] * d[1];
      if (a < 1e-12) { if (fx * fx + fy * fy > s.round.r ** 2) return false; }
      else {
        const b = 2 * (fx * d[0] + fy * d[1]), c = fx * fx + fy * fy - s.round.r ** 2, disc = b * b - 4 * a * c;
        if (disc <= 0) return false;
        const q = Math.sqrt(disc); t0 = Math.max(t0, (-b - q) / (2 * a)); t1 = Math.min(t1, (-b + q) / (2 * a));
      }
    } else {
      const n = s.poly.length;
      let cx = 0, cy = 0; for (const [x, y] of s.poly) { cx += x / n; cy += y / n; }
      for (let i = 0; i < n; i++) {
        const [ax, ay] = s.poly[i], [bx, by] = s.poly[(i + 1) % n];
        let nx = by - ay, ny = -(bx - ax);   // an edge normal, turned inward below
        if (nx * (cx - ax) + ny * (cy - ay) < 0) { nx = -nx; ny = -ny; }
        const den = nx * d[0] + ny * d[1], numr = nx * (E[0] - ax) + ny * (E[1] - ay);
        if (Math.abs(den) < 1e-12) { if (numr < 0) return false; continue; }
        const t = -numr / den;
        if (den > 0) t0 = Math.max(t0, t); else t1 = Math.min(t1, t);
        if (t0 > t1) return false;
      }
    }
    // the height band
    if (Math.abs(d[2]) < 1e-12) { if (E[2] < s.z0 || E[2] > s.z1) return false; }
    else {
      let a = (s.z0 - E[2]) / d[2], b = (s.z1 - E[2]) / d[2]; if (a > b) [a, b] = [b, a];
      t0 = Math.max(t0, a); t1 = Math.min(t1, b);
    }
    return t0 < t1;
  }
  // every solid in the scene: other actors (cylinders up to head top), pieces, house blockers
  function blockersOf(snap, h) {
    const out = [];
    for (const a of snap.cast || []) if (on(a)) {
      const base = levelH(snap, h, a.on);
      out.push({poly: null, round: {x: a.x, y: a.y, r: BODY_R}, z0: base, z1: headZ(a, snap, h) + HEAD_R, id: a.id, actor: true});
    }
    for (const p of snap.pieces || []) for (const s of solids(p)) out.push({...s, piece: true});
    for (const b of h.blockers) out.push({poly: b.poly, round: null, z0: b.z0 || 0, z1: b.h, id: b.id || 'wall', wall: true});
    return out;
  }
  function eyeOf(h, seat) { return [seat.x, seat.y, seat.eye - h.stageH]; }
  // Stage.sight(snap, house, seat) -> {cast: {id: {blocked 0..5, status 'clear'|'partly'|'hidden', by: [ids]}}, pieces: {id: {seen, by}}}
  // five face points (head center, 0.1 m left and right across the sight line, 0.1 m up and down); 3+ blocked: hidden
  function sight(snap, h, seat, pre) {
    seat = seatOf(h, seat);
    const E = eyeOf(h, seat), all = pre || blockersOf(snap, h), res = {cast: {}, pieces: {}};
    for (const a of snap.cast || []) {
      if (!on(a)) continue;
      const hz = headZ(a, snap, h), dx = a.x - E[0], dy = a.y - E[1], dl = hyp(dx, dy) || 1, nx = -dy / dl * .1, ny = dx / dl * .1;
      const pts = [[a.x, a.y, hz], [a.x + nx, a.y + ny, hz], [a.x - nx, a.y - ny, hz], [a.x, a.y, hz + .1], [a.x, a.y, hz - .1]];
      const sitOn = a.sitOn || null;
      let blocked = 0; const by = new Set();
      for (const P of pts) {
        let hit = false;
        for (const s of all) {
          if (s.id === a.id || (sitOn && s.id === sitOn) || (a.on && s.id === a.on)) continue;
          if (hitPrism(E, P, s, .999)) { hit = true; by.add(s.id); }
        }
        if (hit) blocked++;
      }
      res.cast[a.id] = {blocked, status: blocked >= 3 ? 'hidden' : blocked ? 'partly' : 'clear', by: [...by]};
    }
    for (const p of snap.pieces || []) {
      const c = catalog[p.type]; if (!c) continue;
      const P = [p.x, p.y, c.h], by = new Set();
      for (const s of all) { if (s.id === p.id) continue; if (hitPrism(E, P, s, .999)) by.add(s.id); }
      res.pieces[p.id] = {seen: !by.size, by: [...by]};
    }
    return res;
  }

  // ---------- light ----------
  function lightAt(snap, h, x, y) {
    if (h.light !== 'areas') return 2;
    const a = areaOf(h, x, y); return a ? +((snap.lights || {})[a.id] || 0) : 0;
  }
  function inSpot(snap, h, x, y) { return !!snap.spot && hyp(x - snap.spot.x, y - snap.spot.y) <= (h.spotR || 1); }
  function lit(snap, h, a) { return lightAt(snap, h, a.x, a.y) >= 1 || (h.light === 'areas' && inSpot(snap, h, a.x, a.y)); }

  // ---------- focus ----------
  const LNAME = ['in the dark', 'half light', 'full light'];
  // Stage.focus(snap, beat, house, seat, weights, prev) -> {id: {score (null when hidden), reasons: [text], hidden,
  //   parts: {term: value}, why: {term: text}}}: parts and why let a caller name the biggest gap between two actors
  function focus(snap, beat, h, seat, weights, prev, pre) {
    seat = seatOf(h, seat); const W = Object.assign({}, WEIGHTS, weights || {});
    const sg = sight(snap, h, seat, pre), cast = (snap.cast || []).filter(on), out = {};
    for (const a of cast) {
      const st = sg.cast[a.id], r = [];
      if (st.status === 'hidden') { out[a.id] = {score: null, reasons: ['hidden'], hidden: true, parts: {}, why: {}}; continue; }
      let s = 0; const parts = {}, whyOf = {};
      const add = (v, why, key) => { if (v) { s += v; r.push((v > 0 ? '+' : '') + num(v) + ' ' + why); key = key || why; parts[key] = (parts[key] || 0) + v; whyOf[key] = why; } };
      if (beat && beat.speaker === a.id) add(W.speak, 'speaking');
      if (h.light === 'areas') {
        const L = lightAt(snap, h, a.x, a.y), li = Math.round(clamp(L, 0, 2));
        add(W.light[li], LNAME[li], 'light');
        if (inSpot(snap, h, a.x, a.y)) add(W.spot, 'spot');
      }
      const bp = bodyPos(a, seat); add(W.pos[bp], bp, 'pos');
      if (a.on) add(W.level, 'on a level');
      const others = cast.filter(b => b.id !== a.id);
      if ((a.pose || 'stand') === 'stand' && others.length && others.every(b => b.pose === 'sit' || b.pose === 'kneel')) add(W.standAlone, 'only one standing');
      const ar = areaOf(h, a.x, a.y); if (ar && W.row[ar.row]) add(W.row[ar.row], {down: 'downstage', center: 'center row', up: 'upstage'}[ar.row] || ar.row, 'row');
      const pa = prev && byId(prev, a.id);
      if (prev && (!on(pa) || hyp(pa.x - a.x, pa.y - a.y) >= W.crossM)) add(W.crossed, on(pa) ? 'crossed' : 'entered', 'move');
      const gz = others.filter(b => angleTo(b, a.x, a.y) <= W.gazeDeg).length; add(gz * W.gaze, 'looked at by ' + gz, 'gaze');
      if (!others.some(b => hyp(b.x - a.x, b.y - a.y) < W.aloneM)) add(W.alone, 'space around them');
      if (st.status === 'partly') add(W.partly, 'partly hidden');
      for (const t of W.terms || []) { const v = t.fn(a, {snap, beat, house: h, seat, prev, sight: sg}); if (v) add(v.score, v.reason, t.id); }
      // dark: in an areas house and not lit (no area light, no spot); leader() never gives the eye to a dark actor
      out[a.id] = {score: Math.round(s * 10) / 10, reasons: r, hidden: false, dark: h.light === 'areas' && !lit(snap, h, a), parts, why: whyOf};
    }
    return out;
  }
  function leader(f) {
    let best = null, top = -Infinity, tie = false;
    // the eye goes to someone it can see: hidden actors (score null) and actors in the dark are never the leader
    const can = v => v.score !== null && !v.dark;
    for (const [id, v] of Object.entries(f)) { if (!can(v)) continue; if (v.score > top + 1e-9) { top = v.score; best = id; tie = false; } else if (Math.abs(v.score - top) < 1e-9) tie = true; }
    return {id: tie ? null : best, top, tie, tied: tie ? Object.keys(f).filter(k => can(f[k]) && Math.abs(f[k].score - top) < 1e-9) : []};
  }

  // ---------- upstaging ----------
  // Stage.upstaged(snap, beat, seat, house) -> {speaker, partner, gap, pos} or null: the "to" partner stands 1 m or
  // more farther upstage and the speaker, playing toward them, shows three-quarter or full back to the seat
  function upstaged(snap, beat, seat, h) {
    if (!beat || !beat.speaker || !beat.to || beat.to === 'all') return null;
    const s = byId(snap, beat.speaker), p = byId(snap, beat.to); if (!on(s) || !on(p)) return null;
    seat = h ? seatOf(h, seat || h.upSeat) : seat;
    const gap = p.y - s.y; if (gap < 1) return null;
    const pos = bodyPos(s, seat); if (pos !== 'three-quarter' && pos !== 'full back') return null;
    if (angleTo(s, p.x, p.y) >= 90) return null;   // turned away from the partner too: not playing to them
    return {speaker: s.id, partner: p.id, gap: num(gap), pos};
  }

  // ---------- entrances ----------
  function entrancePts(snap, h) {
    const out = [];
    for (const e of h.entrances) for (const at of e.at) out.push({id: e.id, label: e.label, x: at[0], y: at[1], quiet: !!e.quiet});
    for (const p of snap.pieces || []) {
      const c = catalog[p.type]; if (!c || !c.entrance) continue;
      const [x, y] = rotPts(p, [[0, -(c.d / 2 + .05)]])[0];
      out.push({id: c.entrance, label: c.entranceLabel || c.label, x, y, piece: p.id});
    }
    return out;
  }
  function nearestEntrance(snap, h, x, y) {
    let best = null, bd = Infinity;
    for (const e of entrancePts(snap, h)) { const d = hyp(e.x - x, e.y - y); if (d < bd) { bd = d; best = e; } }
    return best;
  }
  const entLabel = (snap, h, id) => { const e = entrancePts(snap, h).find(e => e.id === id) || h.entrances.find(e => e.id === id); return e ? e.label : id; };

  // ---------- beats and carry forward ----------
  // a beat: {speaker, to, line, dir, notes, snap: {cast, pieces, lights, spot}, changed}
  // carry(beats, i): every later beat that was never changed becomes a copy of the beat before it
  function carry(beats, from = 0) {
    for (let j = from + 1; j < beats.length; j++) if (!beats[j].changed) beats[j].snap = clone(beats[j - 1].snap);
    return beats;
  }
  // edit(beats, i, fn): change beat i's snapshot, mark it changed, then carry forward
  function edit(beats, i, fn) { fn(beats[i].snap); beats[i].changed = true; carry(beats, i); return beats[i].snap; }

  // ---------- notes ----------
  const NOTE_TYPES = ['see', 'lit', 'focus', 'at', 'enters', 'exits', 'crosses', 'near', 'apart', 'notUpstaged', 'notHiding', 'notFullBack', 'onLevel', 'seeProp', 'group'];
  // Stage.check(notes, beats, house, opts) -> per note {met, why, seats}. Each note names its beat: {t, beat, ...}.
  // opts: {weights, names: {id: name}}
  function check(notes, beats, h, opts = {}) {
    const cache = {};
    const ctx = i => {
      if (cache[i]) return cache[i];
      const snap = beats[i].snap, prev = i > 0 ? beats[i - 1].snap : null, pre = blockersOf(snap, h);
      const c = {snap, prev, pre, beat: beats[i], sight: {}, focus: {}};
      c.sightAt = s => c.sight[s] || (c.sight[s] = sight(snap, h, s, pre));
      c.focusAt = s => c.focus[s] || (c.focus[s] = focus(snap, beats[i], h, s, opts.weights, prev, pre));
      return cache[i] = c;
    };
    const nm = (snap, id) => { const a = byId(snap, id); return (opts.names && opts.names[id]) || (a && a.name) || id; };
    // a note may name several actors: {t: 'see', ids: [...]} (also lit, focus, notFullBack, notUpstaged, at, crosses) or
    // {t: 'notHiding' | 'near' | 'apart', a, b: [...]}: met when every part is met; the first part that fails explains
    const parts = n => n.ids && n.t !== 'group' ? n.ids.map(a => ({...n, a, ids: null})) : Array.isArray(n.b) ? n.b.map(b => ({...n, b})) : [n];
    return notes.map(n => {
      try {
        const rs = parts(n).map(p => checkOne(p, ctx(n.beat), h, x => nm(ctx(n.beat).snap, x))), bad = rs.filter(r => !r.met);
        if (rs.length === 1) return rs[0];
        return bad.length ? {met: false, why: [...new Set(bad.map(r => r.why))].join(' '), seats: [...new Set(bad.flatMap(r => r.seats))]} : {met: true, why: '', seats: []};
      } catch (e) { return {met: false, why: 'Could not check this note.', seats: []}; }
    });
  }
  // three-quarter and full back are closed to the house: a focus or not-upstaged note needs profile or better
  const closedPos = p => p === 'three-quarter' || p === 'full back';
  const shutWhy = (name, p, seat) => p === 'full back' ? 'From ' + seat + ', ' + name + '\'s back is to the house (full back).' : 'From ' + seat + ', ' + name + ' is turned mostly away from the house (three-quarter).';
  // the focus term with the biggest gap between the leader and the actor ("Biggest gap: Ben +2 for full light, Gran +1 for half light.")
  function gapWhy(top, mine, tn, mn) {
    let best = null;
    for (const k of new Set([...Object.keys(top.parts || {}), ...Object.keys(mine.parts || {})])) { const d = ((top.parts || {})[k] || 0) - ((mine.parts || {})[k] || 0); if (d > 1e-9 && (!best || d > best.d)) best = {k, d}; }
    if (!best) return '';
    const say = (f, who) => who + ' ' + (f.parts[best.k] ? (f.parts[best.k] > 0 ? '+' : '') + num(f.parts[best.k]) + ' for ' + f.why[best.k] : '0');
    return ' Biggest gap: ' + say(top, tn) + ', ' + say(mine, mn) + '.';
  }
  function pieceFor(snap, ref) { return (snap.pieces || []).find(p => p.id === ref) || (snap.pieces || []).find(p => p.type === ref); }
  function checkOne(n, c, h, nm) {
    const {snap, prev} = c, A = byId(snap, n.a), B = n.b ? byId(snap, n.b) : null, seatsAll = h.seats.map(s => s.id);
    const offWhy = id => ({met: false, why: nm(id) + ' is off stage.', seats: []});
    const dist = (p, q) => hyp(p.x - q.x, p.y - q.y);
    const ok = (why = '') => ({met: true, why, seats: []});
    const area = a => { const r = areaOf(h, a.x, a.y); return r ? r.label || r.id : 'no area'; };
    switch (n.t) {
      case 'see': {
        if (!on(A)) return offWhy(n.a);
        const bad = seatsAll.filter(s => c.sightAt(s).cast[A.id].status === 'hidden');
        return bad.length ? {met: false, why: nm(n.a) + ' is hidden from seat' + (bad.length > 1 ? 's ' : ' ') + list(bad) + '.', seats: bad} : ok('Seen from all ' + seatsAll.length + ' seats.');
      }
      case 'lit': {
        if (!on(A)) return offWhy(n.a);
        if (lit(snap, h, A)) return ok();
        const ar = areaOf(h, A.x, A.y);
        return {met: false, why: ar ? nm(n.a) + ' is in ' + (ar.label || ar.id) + ', and its light is off. Raise the ' + (ar.label || ar.id) + ' light, or move ' + nm(n.a) + ' into light.' : nm(n.a) + ' is outside the lit areas.', seats: []};
      }
      case 'focus': {
        if (!on(A)) return offWhy(n.a);
        const seats = n.seats || h.focusSeats;
        // the eye goes to a lit face: an actor in the dark (no area light, no spot) never has the focus
        if (!lit(snap, h, A)) { const ar = areaOf(h, A.x, A.y), an = ar ? ar.label || ar.id : null; return {met: false, why: nm(n.a) + ' is in the dark' + (an ? ' (' + an + ' is off). Light ' + an + ' or use the spot.' : '. Move ' + nm(n.a) + ' into light or use the spot.'), seats: seats.slice()}; }
        // the eye goes to an open face: from every judging seat the actor must be profile or better
        const shut = seats.filter(s => closedPos(bodyPos(A, seatOf(h, s))));
        if (shut.length) return {met: false, why: shutWhy(nm(n.a), bodyPos(A, seatOf(h, shut[0])), shut[0]) + (shut.length > 1 ? ' Also from ' + list(shut.slice(1)) + '.' : '') + ' Turn ' + nm(n.a) + ' out to the house, at least to profile.', seats: shut};
        const bad = [], whys = [];
        for (const s of seats) {
          const f = c.focusAt(s), L = leader(f), mine = f[A.id];
          if (L.id === A.id) continue;
          bad.push(s);
          if (!whys.length) {
            if (mine.score === null) whys.push('From ' + s + ', ' + nm(n.a) + ' is hidden.');
            else if (L.tie && L.tied.includes(A.id)) whys.push('From ' + s + ', ' + nm(n.a) + ' ties with ' + list(L.tied.filter(x => x !== A.id).map(nm)) + ' (' + num(mine.score) + ').');
            else { const top = L.id || L.tied[0]; whys.push('From ' + s + ', the eye goes to ' + nm(top) + ' (' + num(f[top].score) + '), not ' + nm(n.a) + ' (' + num(mine.score) + ').' + gapWhy(f[top], mine, nm(top), nm(n.a))); }
          }
        }
        return bad.length ? {met: false, why: whys[0] + (bad.length > 1 ? ' Also from ' + list(bad.slice(1)) + '.' : ''), seats: bad} : ok();
      }
      case 'at': {
        if (!on(A)) return offWhy(n.a);
        const ar = areaOf(h, A.x, A.y);
        return ar && n.areas.includes(ar.id) ? ok() : {met: false, why: nm(n.a) + ' is in ' + area(A) + '. This note needs ' + list(n.areas.map(x => (h.areas.find(a => a.id === x) || {}).label || x)).replace(/ and ([^ ]+)$/, ' or $1') + '.', seats: []};
      }
      case 'enters': {
        const P = prev && byId(prev, n.a);
        if (!on(A)) return {met: false, why: nm(n.a) + ' is still off stage.', seats: []};
        if (prev && on(P)) return {met: false, why: nm(n.a) + ' was already on stage before this beat.', seats: []};
        // the way in is the wing or Door the actor waited in during the beat before (as exits use the way out); the
        // entrance nearest where the actor first stands only when that is not known
        const w = P && P.wing && entrancePts(prev, h).concat(entrancePts(snap, h)).find(x => x.id === P.wing);
        if (w) return w.id === n.entrance ? ok() : {met: false, why: nm(n.a) + ' waited in the ' + w.label + ' in the beat before, so ' + nm(n.a) + ' comes on from there, not the ' + entLabel(snap, h, n.entrance) + '. In the beat before, drag ' + nm(n.a) + ' off stage by the ' + entLabel(snap, h, n.entrance) + '.', seats: []};
        const e = nearestEntrance(snap, h, A.x, A.y);
        return e && e.id === n.entrance ? ok() : {met: false, why: nm(n.a) + ' first stands nearest the ' + (e ? e.label : 'wings') + '. Bring ' + nm(n.a) + ' on near the ' + entLabel(snap, h, n.entrance) + ', then cross on the next beat.', seats: []};
      }
      case 'exits': {
        const P = prev && byId(prev, n.a);
        if (on(A)) return {met: false, why: nm(n.a) + ' is still on stage. Select ' + nm(n.a) + ' and tap Off stage.', seats: []};
        if (!prev || !on(P)) return {met: false, why: nm(n.a) + ' was not on stage before this beat.', seats: []};
        // the way out is the wing the actor went to (A.wing, set when dropped in a wing or sent off), else the nearest one
        const e = (A.wing && entrancePts(snap, h).concat(entrancePts(prev, h)).find(x => x.id === A.wing)) || nearestEntrance(prev, h, P.x, P.y);
        return e && e.id === n.entrance ? ok() : {met: false, why: nm(n.a) + ' left by the ' + (e ? e.label : 'wings') + ', not the ' + entLabel(snap, h, n.entrance) + '.', seats: []};
      }
      case 'crosses': {
        const P = prev && byId(prev, n.a);
        if (!on(A)) return offWhy(n.a);
        if (!on(P)) return {met: false, why: nm(n.a) + ' was not on stage in the beat before.', seats: []};
        const d = dist(A, P);
        return d >= n.m - 1e-9 ? ok('Crosses ' + num(d) + ' m.') : {met: false, why: nm(n.a) + ' moves ' + num(d) + ' m. This note needs at least ' + n.m + ' m.', seats: []};
      }
      case 'near': case 'apart': {
        if (!on(A)) return offWhy(n.a); if (!on(B)) return offWhy(n.b);
        const d = dist(A, B), good = n.t === 'near' ? d <= n.m + 1e-9 : d >= n.m - 1e-9;
        return good ? ok(num(d) + ' m.') : {met: false, why: nm(n.a) + ' and ' + nm(n.b) + ' are ' + num(d) + ' m apart. This note needs ' + (n.t === 'near' ? 'at most ' : 'at least ') + n.m + ' m.', seats: []};
      }
      case 'notUpstaged': {
        if (!on(A)) return offWhy(n.a);
        const seat = n.seat || h.upSeat, u = upstaged(snap, c.beat, seat, h);
        if (u && u.speaker === A.id) return {met: false, why: nm(u.partner) + ' stands ' + u.gap + ' m upstage, so ' + nm(A.id) + ' shows ' + u.pos + ' from ' + seat + '. Bring ' + nm(u.partner) + ' down level with ' + nm(A.id) + ', or have ' + nm(A.id) + ' cheat out: turn partly out to the house while still talking to ' + nm(u.partner) + '.', seats: [seat]};
        // not upstaged also means open to the house: profile or better from the judging seat
        const p = bodyPos(A, seatOf(h, seat));
        if (closedPos(p)) return {met: false, why: shutWhy(nm(A.id), p, seat) + ' Turn ' + nm(A.id) + ' out to the house, at least to profile.', seats: [seat]};
        return ok();
      }
      case 'notHiding': {   // a does not hide b from any seat
        if (!on(B)) return offWhy(n.b); if (!on(A)) return ok();
        const bad = seatsAll.filter(s => { const st = c.sightAt(s).cast[B.id]; return st.status === 'hidden' && st.by.includes(A.id); });
        return bad.length ? {met: false, why: nm(n.a) + ' covers ' + nm(n.b) + ' from seat' + (bad.length > 1 ? 's ' : ' ') + list(bad) + '.', seats: bad} : ok();
      }
      case 'notFullBack': {
        if (!on(A)) return offWhy(n.a);
        const s = seatOf(h, n.seat), p = bodyPos(A, s);
        return p !== 'full back' ? ok(p + ' from ' + n.seat + '.') : {met: false, why: nm(n.a) + ' is full back from ' + n.seat + '. Turn ' + nm(n.a) + ' toward the house.', seats: [n.seat]};
      }
      case 'onLevel': {
        if (!on(A)) return offWhy(n.a);
        const lv = levels(snap, h), want = lv.filter(l => l.id === n.level || (l.piece && (pieceFor(snap, l.id) || {}).type === n.level));
        if (!want.length) return {met: false, why: 'There is no ' + ((catalog[n.level] || {}).label || n.level).toLowerCase() + ' on stage.', seats: []};
        return want.some(l => l.id === A.on) ? ok() : {met: false, why: nm(n.a) + ' is not on the ' + ((catalog[n.level] || {}).label || n.level).toLowerCase() + '. Drag ' + nm(n.a) + ' onto it.', seats: []};
      }
      case 'seeProp': {
        const p = pieceFor(snap, n.piece), label = ((catalog[(p || {}).type || n.piece] || {}).label || n.piece).toLowerCase();
        if (!p) return {met: false, why: 'There is no ' + label + ' on stage.', seats: []};
        const bad = seatsAll.filter(s => !c.sightAt(s).pieces[p.id].seen);
        return bad.length ? {met: false, why: 'The ' + label + ' is hidden from seat' + (bad.length > 1 ? 's ' : ' ') + list(bad) + '.', seats: bad} : ok();
      }
      case 'group': {
        const G = n.ids.map(id => byId(snap, id));
        for (let i = 0; i < G.length; i++) if (!on(G[i])) return offWhy(n.ids[i]);
        let worst = null;
        for (let i = 0; i < G.length; i++) for (let j = i + 1; j < G.length; j++) { const d = dist(G[i], G[j]); if (d > n.m + 1e-9 && (!worst || d > worst.d)) worst = {i, j, d}; }
        if (worst) return {met: false, why: nm(n.ids[worst.i]) + ' and ' + nm(n.ids[worst.j]) + ' are ' + num(worst.d) + ' m apart. Keep the group within ' + n.m + ' m of each other.', seats: []};
        if (n.areas) { const out = G.find(a => { const r = areaOf(h, a.x, a.y); return !r || !n.areas.includes(r.id); }); if (out) return {met: false, why: nm(out.id) + ' is in ' + area(out) + '. The group needs ' + list(n.areas.map(x => (h.areas.find(a => a.id === x) || {}).label || x)).replace(/ and ([^ ]+)$/, ' or $1') + '.', seats: []}; }
        return ok();
      }
    }
    return {met: false, why: 'Unknown note type ' + n.t + '.', seats: []};
  }

  // ---------- placement help ----------
  // free(snap, house, id, x, y): where actor id may stand near (x, y): not inside a piece (sit pieces and levels are
  // fine), at least 0.5 m from other actors, on the stage. Returns {x, y, on, sitOn} (slides to the nearest free spot)
  function free(snap, h, id, x, y, opt = {}) {
    const R = opt.r || BODY_R, gap = opt.gap || .5;
    const solid = (snap.pieces || []).filter(p => { const c = catalog[p.type] || {}; return !c.sit && !c.standable; });
    const sits = (snap.pieces || []).filter(p => (catalog[p.type] || {}).sit);
    const blockedAt = (px, py) => {
      if (!onStage(h, px, py)) return true;
      for (const p of solid) for (const s of solids(p)) {
        if (s.z0 > 1.9) continue;   // a lintel or a canopy: walk under it
        if (s.round ? hyp(px - s.round.x, py - s.round.y) < s.round.r + R * .6 : distPoly(s.poly, px, py) < R * .6) return true;
      }
      for (const a of snap.cast || []) if (on(a) && a.id !== id && hyp(a.x - px, a.y - py) < gap) return true;
      return false;
    };
    const finish = (px, py) => {
      const sp = sits.find(p => inPoly(footprint(p), px, py));
      const lv = levels(snap, h).find(l => inPoly(l.poly, px, py));
      return {x: Math.round(px * 100) / 100, y: Math.round(py * 100) / 100, on: lv ? lv.id : null, sitOn: sp ? sp.id : null};
    };
    if (!blockedAt(x, y)) return finish(x, y);
    for (let r = .1; r <= 4; r += .1) for (let k = 0; k < 24; k++) {
      const px = x + r * Math.cos(k / 24 * 2 * Math.PI), py = y + r * Math.sin(k / 24 * 2 * Math.PI);
      if (!blockedAt(px, py)) return finish(px, py);
    }
    return finish(x, y);
  }
  // signed-ish distance from a point to a polygon: 0 inside, else the distance to the nearest edge
  function distPoly(poly, x, y) {
    if (inPoly(poly, x, y)) return 0;
    let best = Infinity;
    for (let i = 0; i < poly.length; i++) {
      const [ax, ay] = poly[i], [bx, by] = poly[(i + 1) % poly.length], dx = bx - ax, dy = by - ay;
      const t = clamp(((x - ax) * dx + (y - ay) * dy) / (dx * dx + dy * dy || 1), 0, 1);
      best = Math.min(best, hyp(x - ax - t * dx, y - ay - t * dy));
    }
    return best;
  }

  // ---------- tweening and play ----------
  const lerp = (a, b, t) => a + (b - a) * t;
  function lerpAng(a, b, t) { let d = ((b - a) % 360 + 540) % 360 - 180; return a + d * t; }
  // tween(a, b, t, tl): the snapshot between beats a and b (positions at t, lights at tl, both 0..1)
  function tween(a, b, t, tl = t) {
    if (!a) return clone(b);
    const out = clone(b);
    out.cast = b.cast.map(x => {
      const p = a.cast.find(y => y.id === x.id);
      if (!p) return {...x};
      if (on(p) && on(x)) return {...x, x: lerp(p.x, x.x, t), y: lerp(p.y, x.y, t), facing: lerpAng(p.facing, x.facing, t), pose: t < .5 ? p.pose : x.pose, on: t < .5 ? p.on : x.on};
      if (on(p) && !on(x)) return t < 1 ? {...p} : {...x};
      return t > 0 ? {...x} : {...p};
    });
    const L = {}; for (const k of new Set([...Object.keys(a.lights || {}), ...Object.keys(b.lights || {})])) L[k] = lerp(+(a.lights || {})[k] || 0, +(b.lights || {})[k] || 0, tl);
    out.lights = L;
    return out;
  }
  // Stage.play(beats, view, {cross: 1200, fade: 400, reduce}) -> {beat(i): Promise, stop(), playing}
  //   view: a function (snap, info) or an object with update(snap, info), called every frame with the tweened
  //   snapshot. beat(i) tweens from beat i - 1 to beat i and resolves when done: 'done' or 'stopped'. With reduce
  //   (default Curio.reduce) it shows beat i at once but still waits the same time (calm removes movement, not time).
  function play(beats, view, opts = {}) {
    const cross = opts.cross == null ? 1200 : opts.cross, fade = opts.fade == null ? 400 : opts.fade;
    const show = typeof view === 'function' ? view : (s, i) => view.update(s, i);
    let stopped = false, raf = 0, pending = null;
    const reduce = () => opts.reduce != null ? opts.reduce : (typeof Curio !== 'undefined' && Curio.reduce);
    function beat(i) {
      const b = beats[i].snap, a = i > 0 ? beats[i - 1].snap : null;
      const moves = a && b.cast.some(x => { const p = a.cast.find(y => y.id === x.id); return p && on(p) && on(x) && (hyp(p.x - x.x, p.y - x.y) > .01 || Math.abs(p.facing - x.facing) > .5); });
      const fades = a && Object.keys({...(a.lights || {}), ...(b.lights || {})}).some(k => (+(a.lights || {})[k] || 0) !== (+(b.lights || {})[k] || 0));
      const T = Math.max(moves ? cross : 0, fades ? fade : 0);
      return new Promise(res => {
        pending = res;
        if (stopped) return res('stopped');
        if (!a || !T) { show(clone(b), {beat: i, t: 1}); return res('done'); }
        const t0 = performance.now(), calm = reduce();
        if (calm) show(clone(b), {beat: i, t: 1}); else show(tween(a, b, 0, 0), {beat: i, t: 0});
        const tick = () => {
          if (stopped) return res('stopped');
          const e = performance.now() - t0, t = moves ? clamp(e / cross, 0, 1) : 1, tl = fades ? clamp(e / fade, 0, 1) : 1;
          if (!calm) { const k = t < .5 ? 2 * t * t : 1 - (-2 * t + 2) ** 2 / 2; show(tween(a, b, k, tl), {beat: i, t}); }
          if (e >= T) { show(clone(b), {beat: i, t: 1}); res('done'); } else raf = requestAnimationFrame(tick);
        };
        raf = requestAnimationFrame(tick);
      });
    }
    return {beat, stop() { stopped = true; cancelAnimationFrame(raf); if (pending) pending('stopped'); }, get stopped() { return stopped; }};
  }

  // ======================================================================================================
  // views
  // ======================================================================================================
  const NS = 'http://www.w3.org/2000/svg';
  const esc = s => String(s).replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
  const cssv = (el, name, d) => (getComputedStyle(el).getPropertyValue(name) || '').trim() || d;
  function colors(el) {
    return {
      floor: cssv(el, '--st-floor', '#1b1b1f'), lines: cssv(el, '--st-lines', '#3a3a42'), spike: cssv(el, '--st-spike', '#e07a2e'),
      house: cssv(el, '--st-house', '#2a2a30'), seat: cssv(el, '--st-seat', '#8a8a94'), pool: cssv(el, '--st-pool', '#ffe7b0'),
      wing: cssv(el, '--st-wing', '#232328'), label: cssv(el, '--st-label', '#c9c9d2'), ink: cssv(el, '--st-ink', '#111114'),
      piece: cssv(el, '--st-piece', '#57505a'), pieceLine: cssv(el, '--st-piece-line', '#b9b0bc'), wall: cssv(el, '--st-wall', '#4a4650'),
      sel: cssv(el, '--st-sel', '#ffffff'), bad: cssv(el, '--st-bad', '#ff6b6b'), ok: cssv(el, '--st-ok', '#cfd3dc'), part: cssv(el, '--st-part', '#ffb347'),
      frame: cssv(el, '--st-frame', '#3b2a33'), back: cssv(el, '--st-back', '#141418'), dark: cssv(el, '--st-dark', '#0c0c0f'),
    };
  }

  // ---------- the plan (top-down SVG) ----------
  // Stage.view.plan(el, state, opts) -> {update(state), layout(), toWorld(px, py), toScreen(x, y), k, svg}
  //   opts: {house, mini, pad: {top, right, bottom, left}, minR (px), hitR (px), onPick(sel), onDrag(sel, x, y),
  //          onDrop(sel, x, y), onSeat(id), onTurn(id, facing), label, slots(actor) -> [x, y] (where an off-stage
  //          actor waits)}
  //   state: {snap, prev, beat, seat, sel: {kind: 'actor'|'piece'|'spot', id}, areas, rays, focus, flags}
  function plan(el, state, opts = {}) {
    const h = opts.house, mini = !!opts.mini;
    const svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('class', 'st-plan' + (mini ? ' st-mini' : ''));
    svg.style.cssText = 'position:absolute;left:0;top:0;width:100%;height:100%;display:block;touch-action:none;user-select:none';
    if (opts.label) svg.setAttribute('aria-label', opts.label);
    el.append(svg);
    let S = state, k = 20, ox = 0, oy = 0, W = 0, H = 0, C = null, drag = null, last = {};
    const V = {svg, update, layout, toWorld, toScreen, get k() { return k; }, get box() { return {ox, oy, k, W, H}; }, last: () => last, pad: opts.pad || {}};
    function layout() {
      const r = el.getBoundingClientRect(); W = Math.max(10, r.width); H = Math.max(10, r.height);
      const p = Object.assign({top: 0, right: 0, bottom: 0, left: 0}, V.pad), b = h.planBox;
      const aw = W - p.left - p.right, ah = H - p.top - p.bottom;
      k = Math.max(2, Math.min(aw / (b.x1 - b.x0), ah / (b.y1 - b.y0)));
      ox = p.left + (aw - (b.x1 - b.x0) * k) / 2 - b.x0 * k;
      oy = p.top + (ah - (b.y1 - b.y0) * k) / 2 + b.y1 * k;
      svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
      C = colors(el);
      update(S);
    }
    function toScreen(x, y) { return [ox + x * k, oy - y * k]; }
    function toWorld(px, py) { return [(px - ox) / k, (oy - py) / k]; }
    const pt = (x, y) => toScreen(x, y).map(v => v.toFixed(1)).join(',');
    const poly = (ps) => ps.map(([x, y]) => pt(x, y)).join(' ');
    const minR = () => opts.minR || (mini ? 6 : 11);
    const actorR = () => Math.max(BODY_R * 1.25 * k, minR());
    function slotOf(a) {
      if (opts.slots) return opts.slots(a, S.snap);
      return [a.x, a.y];
    }
    function update(st) {
      S = st || S; if (!S || !S.snap || !C) return;
      const sn = S.snap, out = [], fs = mini ? 10 : Math.round(Math.max(11, Math.min(15, k * .36))), seat = S.seat ? seatOf(h, S.seat) : null;
      last = {actors: {}, seats: {}, pieces: {}, k};
      // house and wings
      out.push(`<rect x="0" y="0" width="${W}" height="${H}" fill="${C.house}"/>`);
      for (const w of h.wings) {
        out.push(`<polygon points="${poly(w.poly)}" fill="${C.wing}"/>`);
        if (!mini && w.label) { const b = bounds([w.poly]), [lx, ly] = toScreen(...(w.labelAt || [(b.x0 + b.x1) / 2, b.y1 - .25])); out.push(`<text x="${lx}" y="${ly + 4}" text-anchor="middle" font-size="${fs}" fill="${C.label}">${esc(w.label)}</text>`); }
      }
      out.push(`<polygon points="${poly(h.outline)}" fill="${C.floor}"/>`);
      for (const l of h.levels) out.push(`<polygon points="${poly(l.poly)}" fill="${C.piece}" stroke="${C.pieceLine}" stroke-width="1"/>`);
      // light pools (areas) and the spot
      if (h.light === 'areas') for (const a of h.areas) {
        const L = +((sn.lights || {})[a.id] || 0); if (L <= 0) continue;
        out.push(`<polygon points="${poly(a.poly)}" fill="${C.pool}" fill-opacity="${(.2 + .075 * (L - 1)).toFixed(3)}"/>`);
      }
      if (sn.spot && h.light === 'areas') {
        const [sx, sy] = toScreen(sn.spot.x, sn.spot.y);
        out.push(`<circle cx="${sx}" cy="${sy}" r="${(h.spotR || 1) * k}" fill="${C.pool}" fill-opacity=".35" stroke="${C.pool}" stroke-dasharray="4 3" stroke-width="${S.sel && S.sel.kind === 'spot' ? 3 : 1.5}"/>`);
        if (!mini) out.push(`<text x="${sx}" y="${sy - (h.spotR || 1) * k - 4}" text-anchor="middle" font-size="${fs}" fill="${C.label}">Spot</text>`);
        last.spot = [sx, sy];
      }
      // areas
      // an area label gives way to an actor standing on it (the token, its tags and its focus bar), so they never overlap
      const busy = mini ? [] : sn.cast.filter(on).map(a => { const [px, py] = toScreen(a.x, a.y), R = actorR(); return [px - R - 16, py - R - 18, px + R + 26, py + R + 44]; });
      const tok = busy.map(r => [r[0] + 14, r[1] + 16, r[2] - 24, r[3] - 14]);   // the token and its first tag only
      if (S.areas !== false && !mini) for (const a of h.areas) {
        out.push(`<polygon points="${poly(a.poly)}" fill="none" stroke="${C.lines}" stroke-width="1"/>`);
        const b = bounds([a.poly]), [lx, ly] = toScreen(b.x0 + .12, b.y1 - .12), lb = [lx, ly, lx + 4 + String(a.label || a.id).length * fs * .62, ly + fs + 4];
        if (busy.some(r => r[0] < lb[2] && r[2] > lb[0] && r[1] < lb[3] && r[3] > lb[1])) continue;
        out.push(`<text x="${lx + 2}" y="${ly + fs}" font-size="${fs}" fill="${C.label}" fill-opacity=".85">${esc(a.label || a.id)}</text>`);
      }
      // blockers (walls), the curtain line
      for (const b of h.blockers) if (!b.hideInPlan) out.push(`<polygon points="${poly(b.poly)}" fill="${C.wall}"/>`);
      if (h.curtainY != null && h.frame === 'proscenium' && h.opening) {
        const [ax, ay] = toScreen(h.opening.x0, h.curtainY), [bx] = toScreen(h.opening.x1, h.curtainY);
        out.push(`<line x1="${ax}" y1="${ay}" x2="${bx}" y2="${ay}" stroke="${C.lines}" stroke-width="1.5" stroke-dasharray="6 4"/>`);
      }
      // spike marks
      if (!mini) for (const [nm, [x, y]] of Object.entries(h.spots || {})) {
        const [sx, sy] = toScreen(x, y), r = 5;
        out.push(`<path d="M${sx - r},${sy}H${sx + r}M${sx},${sy - r}V${sy + r}" stroke="${C.spike}" stroke-width="2"/>`);
      }
      // entrances
      if (!mini) for (const e of entrancePts(sn, h)) {
        const [sx, sy] = toScreen(e.x, e.y), L = 14;
        const lab = e.piece ? e.label : e.id;
        if (e.piece) {   // a door in a set piece: the arrow runs from the opening down into the stage
          out.push(`<path d="M${sx},${sy}L${sx},${sy + L}" stroke="${C.spike}" stroke-width="2" marker-end="url(#st-ah)"/>`);
          out.push(`<text x="${sx + 7}" y="${sy + L + 2}" font-size="${fs}" fill="${C.spike}">${esc(lab)}</text>`);
          continue;
        }
        const inward = [e.x < 0 ? 1 : -1, 0], tx = sx - inward[0] * L, ty = sy;
        out.push(`<path d="M${tx},${ty}L${sx},${sy}" stroke="${C.spike}" stroke-width="2" marker-end="url(#st-ah)"/>`);
        if (!e.quiet) out.push(`<text x="${tx + (e.x < 0 ? -3 : 3)}" y="${sy - 5}" text-anchor="${e.x < 0 ? 'end' : 'start'}" font-size="${fs}" fill="${C.spike}">${esc(lab)}</text>`);
      }
      // pieces
      for (const p of sn.pieces || []) {
        const c = catalog[p.type] || {}, sel = S.sel && S.sel.kind === 'piece' && S.sel.id === p.id;
        for (const s of solids(p)) {
          if (s.z0 > 1.9 && c.opening) continue;   // the lintel is over the opening: drawn as the gap
          out.push(`<polygon points="${poly(s.poly)}" fill="${c.plan || C.piece}" stroke="${sel ? C.sel : C.pieceLine}" stroke-width="${sel ? 2.5 : 1}"/>`);
        }
        const fp = footprint(p), b = bounds([fp]), [cx, cy] = toScreen(p.x, p.y);
        last.pieces[p.id] = {x: cx, y: cy, poly: fp.map(([x, y]) => toScreen(x, y))};
        const pl = String(c.short || c.label || p.type), plb = [cx - pl.length * 3.4, cy - 8, cx + pl.length * 3.4, cy + 6];
        if (!mini && !c.entrance && (b.x1 - b.x0) * k > 38 && !tok.some(r => r[0] < plb[2] && r[2] > plb[0] && r[1] < plb[3] && r[3] > plb[1])) out.push(`<text x="${cx}" y="${cy + 4}" text-anchor="middle" font-size="${fs - 1 < 10 ? 10 : fs - 1}" fill="${C.label}" pointer-events="none">${esc((c.short || c.label || p.type).toLowerCase())}</text>`);
        if (sel) out.push(`<polygon points="${poly(fp)}" fill="none" stroke="${C.sel}" stroke-dasharray="5 4" stroke-width="1.5" transform="translate(0,0)"/>`);
      }
      // cross arrows
      if (S.prev && !mini) for (const a of sn.cast) {
        const p = byId(S.prev, a.id); if (!on(a) || !on(p) || hyp(p.x - a.x, p.y - a.y) < .3) continue;
        const [x0, y0] = toScreen(p.x, p.y), [x1, y1] = toScreen(a.x, a.y), d = hyp(x1 - x0, y1 - y0), r = actorR() + 3;
        if (d < r * 2) continue;
        const ex = x1 - (x1 - x0) / d * r, ey = y1 - (y1 - y0) / d * r;
        out.push(`<circle cx="${x0}" cy="${y0}" r="${Math.max(4, actorR() * .45)}" fill="none" stroke="${a.color}" stroke-dasharray="3 3" stroke-width="1.5"/>`);
        out.push(`<path d="M${x0},${y0}L${ex},${ey}" stroke="${a.color}" stroke-width="2" stroke-dasharray="7 4" marker-end="url(#st-ah-${a.id})"/>`);
      }
      // sightline rays from the chosen seat
      const sg = seat && (S.rays || S.flags) ? sight(sn, h, seat) : null;
      if (seat && S.rays && sg) {
        const sp = seat.planAt ? seat.planAt[0] : [seat.x, seat.y], [sx, sy] = toScreen(sp[0], sp[1]);
        for (const a of sn.cast) {
          if (!on(a)) continue;
          const st = sg.cast[a.id], [ax, ay] = toScreen(a.x, a.y);
          let x0 = sx, y0 = sy;
          if (seat.planAt) {
            const t = (seat.planAt[0][1] - a.y) / (seat.y - a.y); [x0, y0] = toScreen(a.x + (seat.x - a.x) * t, seat.planAt[0][1]);
            if (hyp(x0 - sx, y0 - sy) > 3) out.push(`<line x1="${sx}" y1="${sy}" x2="${x0}" y2="${y0}" stroke="${C.ok}" stroke-opacity=".35" stroke-width="1" stroke-dasharray="2 3"/>`);
          }
          const bad = st.status !== 'clear';
          out.push(`<line x1="${x0}" y1="${y0}" x2="${ax}" y2="${ay}" stroke="${bad ? (st.status === 'hidden' ? C.bad : C.part) : C.ok}" stroke-opacity="${bad ? .95 : .55}" stroke-width="${bad ? 2 : 1.5}"${bad ? ' stroke-dasharray="7 5"' : ''}/>`);
        }
      }
      // seats
      for (const s of h.seats) {
        const at = s.planAt ? s.planAt[0] : [s.x, s.y], [sx, sy] = toScreen(at[0], at[1]), chosen = seat && seat.id === s.id;
        const r = Math.max(mini ? 4 : 5, (opts.seatR || .3) * k);
        out.push(`<circle cx="${sx}" cy="${sy}" r="${r}" fill="${chosen ? C.spike : C.seat}" stroke="${chosen ? C.sel : 'none'}" stroke-width="2"/>`);
        if (chosen) out.push(`<circle cx="${sx}" cy="${sy}" r="${r + 4}" fill="none" stroke="${C.spike}" stroke-width="2"/>`);
        last.seats[s.id] = [sx, sy];
        if (!mini && (s.tag || chosen)) {
          const lab = chosen ? (s.label || s.id) : s.tag;
          out.push(`<text x="${sx + (s.tagSide === 'left' ? -r - 4 : r + 4)}" y="${sy + 4}" text-anchor="${s.tagSide === 'left' ? 'end' : 'start'}" font-size="${fs}" font-weight="${chosen ? 700 : 400}" fill="${chosen ? C.spike : C.label}">${esc(lab)}</text>`);
        }
      }
      // focus scores (bars) and the leader's eye
      let fo = null, lead = null;
      if (S.focus && seat) { fo = focus(sn, S.beat, h, seat, S.weights, S.prev); lead = leader(fo); }
      // actors
      const up = S.beat ? upstaged(sn, S.beat, h.upSeat, h) : null;
      const R = actorR(), tagRects = [], tagQ = [];
      // a tag tries below its token, then lower, then above; it must not cover another tag or another actor's token
      const tag = (q) => {
        const {x, y, top, text, color, owner} = q, w = text.length * 6.2 + 8, hh = 15;
        const clash = ty => tagRects.some(r => Math.abs(r[0] - x) < (r[2] + w) / 2 && Math.abs(r[1] - ty) < hh) ||
          Object.entries(last.actors).some(([id, t]) => id !== owner && Math.abs(t.x - x) < w / 2 + t.r && ty - 11 < t.y + t.r && ty + 3 > t.y - t.r);
        const tries = [y, y + hh, y + 2 * hh, y + 3 * hh, top, top - hh, top - 2 * hh];
        const ty = tries.find(t => !clash(t)) ?? y;
        tagRects.push([x, ty, w]);
        out.push(`<rect x="${x - w / 2}" y="${ty - 11}" width="${w}" height="${hh - 1}" rx="4" fill="${C.ink}" fill-opacity=".85"/><text x="${x}" y="${ty}" text-anchor="middle" font-size="10.5" fill="${color}">${esc(text)}</text>`);
      };
      // every token's place first, so tags and scores can keep clear of tokens drawn later
      for (const a of sn.cast) { const off = !on(a), [px, py] = off && !a.dragging ? toScreen(...slotOf(a)) : toScreen(a.x, a.y); last.actors[a.id] = {x: px, y: py, r: R, off}; }
      for (const a of sn.cast) {
        const off = !on(a), [px, py] = off && !a.dragging ? toScreen(...slotOf(a)) : toScreen(a.x, a.y);
        const sel = S.sel && S.sel.kind === 'actor' && S.sel.id === a.id;
        last.actors[a.id] = {x: px, y: py, r: R, off};
        const f = (a.facing || 0) * D2R, fx = Math.sin(f), fy = Math.cos(f);   // screen: +x right, +y down; facing 0 points down
        if (!off) {
          const tip = [px + fx * (R + 8), py + fy * (R + 8)], b1 = [px + fx * R * .7 - fy * R * .55, py + fy * R * .7 + fx * R * .55], b2 = [px + fx * R * .7 + fy * R * .55, py + fy * R * .7 - fx * R * .55];
          out.push(`<polygon points="${tip.join(',')} ${b1.join(',')} ${b2.join(',')}" fill="${a.color}" stroke="${C.ink}" stroke-width="1"/>`);
        }
        out.push(`<circle cx="${px}" cy="${py}" r="${R}" fill="${a.color}" fill-opacity="${off ? .55 : 1}" stroke="${sel ? C.sel : C.ink}" stroke-width="${sel ? 3 : 1.5}"${off ? ' stroke-dasharray="4 3"' : ''}/>`);
        if (a.pose === 'sit' || a.pose === 'kneel') out.push(`<circle cx="${px}" cy="${py}" r="${R - 3.5}" fill="none" stroke="${C.ink}" stroke-width="1.2"${a.pose === 'kneel' ? ' stroke-dasharray="2 2"' : ''}/>`);
        out.push(`<text x="${px}" y="${py + Math.max(10, R * .8) * .36}" text-anchor="middle" font-size="${Math.max(10, Math.min(16, R * .85))}" font-weight="700" fill="${C.ink}" pointer-events="none">${esc(a.initials || initials(a.name))}</text>`);
        if (sel && !off && !mini) {
          const hx = px + fx * (R + 20), hy = py + fy * (R + 20);
          out.push(`<line x1="${px + fx * (R + 8)}" y1="${py + fy * (R + 8)}" x2="${hx}" y2="${hy}" stroke="${C.sel}" stroke-width="1.5"/><circle cx="${hx}" cy="${hy}" r="7" fill="${C.ink}" stroke="${C.sel}" stroke-width="2"/>`);
          last.handle = [hx, hy, a.id];
        }
        if (mini) continue;
        const below = py + R + 13;
        if (!off) {
          const tags = [], ini = a.initials || initials(a.name);
          if (a.pose === 'sit' || a.pose === 'kneel') tags.push([a.pose === 'sit' ? 'sitting' : 'kneeling', C.label]);
          if (up && up.speaker === a.id) tags.push(['upstaged (from ' + h.upSeat + ')', C.bad]);
          if (sg && S.flags && sg.cast[a.id].status !== 'clear') tags.push([(sg.cast[a.id].status === 'hidden' ? 'hidden' : 'partly hidden') + ' from ' + seat.id, sg.cast[a.id].status === 'hidden' ? C.bad : C.part]);
          tags.forEach(([t, col], i) => tagQ.push({x: px, y: below + i * 15, top: py - R - 8 - (tags.length - 1 - i) * 15, text: ini + ' ' + t, color: col, owner: a.id}));
          if (fo) {
            const v = fo[a.id], bx = px - R - 12, top = py - R;
            if (v.score !== null) {
              const hgt = clamp((v.score + 3) / 15, .04, 1) * R * 2;
              out.push(`<rect x="${bx}" y="${top}" width="7" height="${R * 2}" fill="${C.ink}" fill-opacity=".7"/><rect x="${bx}" y="${top + R * 2 - hgt}" width="7" height="${hgt}" fill="${C.spike}"/>`);
              // the score sits over its bar, or under it when another actor's token is there
              const hitTok = ly => Object.entries(last.actors).some(([id, t]) => id !== a.id && Math.abs(t.x - (bx + 3.5)) < t.r + 9 && ly - 9 < t.y + t.r && ly + 1 > t.y - t.r);
              const ly = hitTok(top - 3) ? top + R * 2 + 11 : top - 3;
              out.push(`<text x="${bx + 3.5}" y="${ly}" text-anchor="middle" font-size="10.5" font-weight="700" fill="${C.label}">${num(v.score)}</text>`);
            }
            if (lead && lead.id === a.id) { out.push(eyeIcon(px + R + 12, py - R - 4, C)); last.eye = a.id; }
          }
        }
      }
      for (const q of tagQ) tag(q);
      // markers
      const defs = [`<marker id="st-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="${C.spike}"/></marker>`,
        ...sn.cast.map(a => `<marker id="st-ah-${a.id}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="${a.color}"/></marker>`)];
      svg.innerHTML = `<defs>${defs.join('')}</defs>` + out.join('');
      last.focus = fo; last.leader = lead; last.sight = sg; last.upstaged = up;
    }
    // ---------- pointer: drag actors, pieces and the spot; turn with the facing handle; tap seats ----------
    const hitR = () => opts.hitR || (mini ? 16 : 22);
    function pick(px, py) {
      if (!mini && last.handle && hyp(px - last.handle[0], py - last.handle[1]) <= 14) return {kind: 'turn', id: last.handle[2]};
      if (!mini) {
        let best = null, bd = hitR();
        for (const [id, a] of Object.entries(last.actors)) { const d = hyp(px - a.x, py - a.y); if (d <= Math.max(bd, a.r) && (!best || d < best.d)) best = {kind: 'actor', id, d}; }
        if (best) return best;
        if (last.spot && hyp(px - last.spot[0], py - last.spot[1]) <= Math.max((h.spotR || 1) * k, 16)) {
          // a piece inside the spot wins when the point is on it
          const pc = pieceAt(px, py); return pc || {kind: 'spot', id: 'spot'};
        }
        const pc = pieceAt(px, py); if (pc) return pc;
      }
      let best = null, bd = hitR();
      for (const [id, [sx, sy]] of Object.entries(last.seats)) { const d = hyp(px - sx, py - sy); if (d <= bd) { bd = d; best = {kind: 'seat', id}; } }
      return best;
    }
    function pieceAt(px, py) {
      let best = null;
      for (const [id, p] of Object.entries(last.pieces)) {
        if (inPoly(p.poly, px, py)) return {kind: 'piece', id};
        // a small piece (a chair is 10 to 18 px wide) still gets a 44 px target around its center
        const d = Math.min(distPoly(p.poly, px, py) + 14, hyp(px - p.x, py - p.y)); if (d <= 22 && (!best || d < best.d)) best = {kind: 'piece', id, d};
      }
      return best;
    }
    const local = e => { const r = svg.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };
    svg.addEventListener('pointerdown', e => {
      if (e.button > 0) return;
      const [px, py] = local(e), hit = pick(px, py);
      // capture first, on every pointerdown: the plan redraws under the pointer, and the click must still land
      try { svg.setPointerCapture(e.pointerId); } catch {}
      downEl = e.target;
      if (!hit) { opts.onPick && opts.onPick(null); return; }
      if (hit.kind === 'seat') { opts.onSeat && opts.onSeat(hit.id); return; }
      e.preventDefault();
      let grab = [0, 0];
      if (hit.kind === 'actor') { const a = last.actors[hit.id]; grab = [px - a.x, py - a.y]; }
      else if (hit.kind === 'piece') { const p = last.pieces[hit.id]; grab = [px - p.x, py - p.y]; }
      else if (hit.kind === 'spot') grab = [px - last.spot[0], py - last.spot[1]];
      drag = {hit, x0: px, y0: py, grab, moved: false, id: e.pointerId};
    });
    svg.addEventListener('pointermove', e => {
      if (!drag || e.pointerId !== drag.id) return;
      const [px, py] = local(e);
      if (!drag.moved && hyp(px - drag.x0, py - drag.y0) < 4) return;
      if (!drag.moved) { drag.moved = true; if (drag.hit.kind !== 'turn') opts.onPick && opts.onPick({kind: drag.hit.kind, id: drag.hit.id}, true); }
      if (drag.hit.kind === 'turn') {
        const a = byId(S.snap, drag.hit.id), [ax, ay] = toScreen(a.x, a.y);
        const ang = Math.atan2(px - ax, py - ay) / D2R, f = ((Math.round(ang / 45) * 45) % 360 + 360) % 360;
        opts.onTurn && opts.onTurn(drag.hit.id, f);
        return;
      }
      const [x, y] = toWorld(px - drag.grab[0], py - drag.grab[1]);
      opts.onDrag && opts.onDrag({kind: drag.hit.kind, id: drag.hit.id}, x, y);
    });
    const end = e => {
      if (!drag || e.pointerId !== drag.id) return;
      const d = drag; drag = null;
      try { svg.releasePointerCapture(e.pointerId); } catch {}
      if (d.hit.kind === 'turn') return;
      if (!d.moved) { opts.onPick && opts.onPick({kind: d.hit.kind, id: d.hit.id}); return; }
      const [px, py] = local(e), [x, y] = toWorld(px - d.grab[0], py - d.grab[1]);
      opts.onDrop && opts.onDrop({kind: d.hit.kind, id: d.hit.id}, x, y);
    };
    svg.addEventListener('pointerup', end);
    // a tap whose element was redrawn away before the pointer came up gets no click from the browser (no common
    // ancestor); send one from the plan so page-level click listeners (the kit's first-tap welcome) still hear it
    let downEl = null;
    svg.addEventListener('pointerup', e => { const d = downEl; downEl = null; if (d && !d.isConnected) svg.dispatchEvent(new MouseEvent('click', {bubbles: true, clientX: e.clientX, clientY: e.clientY})); });
    svg.addEventListener('pointercancel', end);
    new ResizeObserver(() => layout()).observe(el);
    layout();
    return V;
  }
  function eyeIcon(x, y, C) {
    return `<g transform="translate(${x},${y})" aria-hidden="true"><path d="M-10,0Q0,-8 10,0Q0,8 -10,0z" fill="${C.sel}" stroke="${C.ink}" stroke-width="1.2"/><circle r="3.4" fill="${C.ink}"/></g>`;
  }

  // ---------- the house view (canvas perspective from one seat) ----------
  // Stage.view.house(el, state, seat, opts) -> {update(state, seat), layout(), canvas, last()}
  //   opts: {house, mini, tags (default !mini), margin}
  //   state: {snap, prev, beat, focus (show the eye), weights, fit (optional [x, y, z] points to frame; default h.fitPts)}
  function camera(h, seat, W, H, margin = .06, pts) {
    const E = eyeOf(h, seat), T = h.look;
    const F = norm([T[0] - E[0], T[1] - E[1], T[2] - E[2]]), R = norm(cross(F, [0, 0, 1])), U = cross(R, F);
    const raw = p => { const d = [p[0] - E[0], p[1] - E[1], p[2] - E[2]], zc = dot(d, F); return [dot(d, R) / zc, dot(d, U) / zc, zc]; };
    const fit = pts && pts.length ? pts : h.fitPts || [...h.outline.map(([x, y]) => [x, y, 0]), ...(h.opening ? [[h.opening.x0, h.opening.y, h.opening.h], [h.opening.x1, h.opening.y, h.opening.h]] : h.outline.map(([x, y]) => [x, y, 3]))];
    let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
    for (const p of fit) { const q = raw(p); if (q[2] <= .05) continue; x0 = Math.min(x0, q[0]); x1 = Math.max(x1, q[0]); y0 = Math.min(y0, q[1]); y1 = Math.max(y1, q[1]); }
    const s = Math.min(W * (1 - 2 * margin) / (x1 - x0), H * (1 - 2 * margin) / (y1 - y0));
    const ox = W / 2 - s * (x0 + x1) / 2, oy = H / 2 + s * (y0 + y1) / 2;
    return {E, F, R, U, s, W, H, raw, proj: p => { const q = raw(p); return q[2] <= .05 ? null : [ox + s * q[0], oy - s * q[1], q[2]]; },
      clipPoly(pts) {   // clip a 3D polygon at the near plane, then project
        const cam = this, d = p => dot([p[0] - E[0], p[1] - E[1], p[2] - E[2]], F) - .06, out = [];
        for (let i = 0; i < pts.length; i++) {
          const a = pts[i], b = pts[(i + 1) % pts.length], da = d(a), db = d(b);
          if (da >= 0) out.push(a);
          if ((da >= 0) !== (db >= 0)) { const t = da / (da - db); out.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t]); }
        }
        return out.map(p => cam.proj(p)).filter(Boolean);
      }};
  }
  function norm(v) { const l = Math.hypot(...v) || 1; return v.map(x => x / l); }
  function cross(a, b) { return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]; }
  function dot(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
  function shadeHex(hex, f) {
    const m = /^#?([0-9a-f]{6})$/i.exec(hex); if (!m) return hex;
    const n = parseInt(m[1], 16), c = [n >> 16, (n >> 8) & 255, n & 255].map(v => clamp(Math.round(v * f), 0, 255));
    return '#' + c.map(v => v.toString(16).padStart(2, '0')).join('');
  }
  function houseView(el, state, seat, opts = {}) {
    const h = opts.house, mini = !!opts.mini, cv = document.createElement('canvas');
    cv.className = 'st-house' + (mini ? ' st-mini' : '');
    cv.style.cssText = 'position:absolute;left:0;top:0;width:100%;height:100%;display:block';
    cv.setAttribute('role', 'img');
    el.append(cv);
    let S = state, seatId = seat, W = 0, H = 0, dpr = 1, C = null, last = {};
    function layout() {
      const r = el.getBoundingClientRect(); W = Math.max(10, Math.floor(r.width)); H = Math.max(10, Math.floor(r.height));
      dpr = Math.min(2, devicePixelRatio || 1); cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      C = colors(el); update(S, seatId);
    }
    function update(st, seat) {
      if (st) S = st; if (seat) seatId = seat; if (!S || !S.snap || !C || !seatId) return;
      const ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const sn = S.snap, s0 = seatOf(h, seatId), cam = camera(h, s0, W, H, opts.margin, S.fit), E = cam.E;
      const fill = (pts, col, stroke) => { if (pts.length < 3) return; ctx.beginPath(); pts.forEach(([x, y], i) => i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)); ctx.closePath(); ctx.fillStyle = col; ctx.fill(); if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = 1; ctx.stroke(); } };
      ctx.fillStyle = C.dark; ctx.fillRect(0, 0, W, H);
      const b = h.box, sg = sight(sn, h, s0), fo = S.focus ? focus(sn, S.beat, h, s0, S.weights, S.prev) : null, lead = fo ? leader(fo) : null;
      last = {sight: sg, focus: fo, leader: lead, tags: {}, seat: s0.id};
      // back wall and floor
      const back = h.backWall || {y: b.y1, x0: b.x0 - 4, x1: b.x1 + 4, h: h.opening ? h.opening.h + 1 : 4};
      fill(cam.clipPoly([[back.x0, back.y, 0], [back.x1, back.y, 0], [back.x1, back.y, back.h], [back.x0, back.y, back.h]]), C.back);
      for (const w of h.wings) fill(cam.clipPoly(w.poly.map(([x, y]) => [x, y, 0])), C.wing);
      fill(cam.clipPoly(h.outline.map(([x, y]) => [x, y, 0])), C.floor);
      // light pools
      if (h.light === 'areas') {
        for (const a of h.areas) { const L = +((sn.lights || {})[a.id] || 0); if (L > 0) { ctx.globalAlpha = .2 + .075 * (L - 1); fill(cam.clipPoly(a.poly.map(([x, y]) => [x, y, .001])), C.pool); ctx.globalAlpha = 1; } }
        if (sn.spot) { ctx.globalAlpha = .35; fill(cam.clipPoly(circ(h.spotR || 1, 28, sn.spot.x, sn.spot.y).map(([x, y]) => [x, y, .002])), C.pool); ctx.globalAlpha = 1; }
      } else if (h.light === 'daylight') { ctx.globalAlpha = .12; fill(cam.clipPoly(h.outline.map(([x, y]) => [x, y, .001])), C.pool); ctx.globalAlpha = 1; }
      // house levels (raised floors)
      const items = [];
      for (const l of h.levels) items.push({d: distTo(E, l.poly), draw: () => prism(ctx, cam, l.poly, 0, l.h, C.piece, E, fill, 1)});
      // pieces
      for (const p of sn.pieces || []) {
        const c = catalog[p.type] || {};
        const L = lightAt(sn, h, p.x, p.y) + (inSpot(sn, h, p.x, p.y) ? 1 : 0), br = h.light === 'areas' ? .55 + .45 * clamp(L / 2, 0, 1) : 1;
        for (const s of solids(p)) items.push({d: distTo(E, s.poly), y: p.y, draw: () => prism(ctx, cam, s.poly, s.z0, s.z1, shadeHex(s.color || c.color || '#77707a', br), E, fill, 1)});
      }
      // actors
      const figs = [];
      for (const a of sn.cast || []) {
        if (!on(a)) continue;
        const st = sg.cast[a.id];
        const f = {a, st, d: Math.hypot(a.x - E[0], a.y - E[1])};
        figs.push(f);
        if (st.status !== 'hidden') items.push({d: f.d, y: a.y, draw: () => figure(ctx, cam, a, sn, h, s0, C, false, f)});
      }
      // walls: the proscenium is drawn between upstage things and the apron
      const cy = h.curtainY;
      const ups = items.filter(i => cy == null || i.y == null || i.y > cy), downs = items.filter(i => !(cy == null || i.y == null || i.y > cy));
      ups.sort((p, q) => q.d - p.d).forEach(i => i.draw());
      for (const bl of h.blockers) prism(ctx, cam, bl.poly, bl.z0 || 0, bl.h, bl.color || C.frame, E, fill, .9);
      if (h.frontFace !== false && h.stageH > 0) fill(cam.clipPoly([[b.x0, b.y0, -h.stageH], [b.x1, b.y0, -h.stageH], [b.x1, b.y0, 0], [b.x0, b.y0, 0]]), C.dark, C.lines);
      downs.sort((p, q) => q.d - p.d).forEach(i => i.draw());
      // ghosts for hidden actors, then every tag on top
      for (const f of figs) if (f.st.status === 'hidden') figure(ctx, cam, f.a, sn, h, s0, C, true, f);
      const placed = [];
      for (const f of figs.sort((p, q) => q.d - p.d)) {
        if (!f.box) continue;
        const pos = bodyPos(f.a, s0), lines = [], ini = f.a.initials || initials(f.a.name);
        if (f.st.status === 'hidden') lines.push('hidden');
        else {
          lines.push(pos);
          if (f.st.status === 'partly') lines.push('partly hidden');
          if (h.light === 'areas' && !lit(sn, h, f.a)) lines.push('in the dark');
        }
        last.tags[f.a.id] = lines.slice();
        if (opts.tags === false || mini) continue;
        lines[0] = ini + ' ' + lines[0];   // whose tag it is
        const fsz = 12, lh = 15, w = Math.max(...lines.map(t => t.length)) * 6.6 + 12, hh = lines.length * lh + 4;
        let x = f.box.cx, y = f.box.bottom + 4;
        for (let n = 0; n < 6 && placed.some(r => Math.abs(r.x - x) < (r.w + w) / 2 + 2 && Math.abs(r.y - y) < (r.h + hh) / 2 + 1); n++) y += hh * .6 + 2;
        y = Math.min(y, H - hh - 2);
        placed.push({x, y: y + 0, w, h: hh});
        ctx.fillStyle = 'rgba(12,12,15,.86)'; roundRect(ctx, x - w / 2, y, w, hh, 5); ctx.fill();
        ctx.font = `600 ${fsz}px "Segoe UI",system-ui,sans-serif`; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
        lines.forEach((t, i) => { const k = i ? t : t.slice(ini.length + 1); ctx.fillStyle = k === 'hidden' ? C.bad : k === 'partly hidden' || k === 'in the dark' ? C.part : '#f2f2f5'; ctx.fillText(t, x, y + 3 + i * lh); });
      }
      if (lead && lead.id) {
        const f = figs.find(f => f.a.id === lead.id);
        if (f && f.box) { const sz = mini ? 9 : 14; drawEye(ctx, f.box.cx, f.box.top - sz - 4, sz, C); last.eye = lead.id; }
      }
      ctx.textAlign = 'start'; ctx.textBaseline = 'alphabetic';
      cv.setAttribute('aria-label', 'Seat ' + s0.id + ' view: ' + figs.map(f => (f.a.name || f.a.id) + ' ' + last.tags[f.a.id].join(', ')).join('; '));
      last.figs = Object.fromEntries(figs.map(f => [f.a.id, f.box]));
    }
    new ResizeObserver(() => layout()).observe(el);
    layout();
    return {canvas: cv, update, layout, last: () => last};
  }
  function distTo(E, poly) { let cx = 0, cy = 0; for (const [x, y] of poly) { cx += x / poly.length; cy += y / poly.length; } return Math.hypot(cx - E[0], cy - E[1]); }
  function prism(ctx, cam, poly, z0, z1, col, E, fill, alpha) {
    const n = poly.length; let cx = 0, cy = 0; for (const [x, y] of poly) { cx += x / n; cy += y / n; }
    const faces = [];
    for (let i = 0; i < n; i++) {
      const [ax, ay] = poly[i], [bx, by] = poly[(i + 1) % n];
      let nx = by - ay, ny = -(bx - ax); if (nx * (ax - cx) + ny * (ay - cy) < 0) { nx = -nx; ny = -ny; }
      if (nx * (E[0] - (ax + bx) / 2) + ny * (E[1] - (ay + by) / 2) <= 0) continue;
      const l = Math.hypot(nx, ny), toward = -ny / l;   // faces toward the house are lit most
      faces.push({pts: [[ax, ay, z0], [bx, by, z0], [bx, by, z1], [ax, ay, z1]], f: .62 + .3 * clamp(toward, 0, 1) + .08 * Math.abs(nx / l), d: Math.hypot((ax + bx) / 2 - E[0], (ay + by) / 2 - E[1])});
    }
    faces.sort((p, q) => q.d - p.d);
    ctx.globalAlpha = alpha;
    for (const f of faces) fill(cam.clipPoly(f.pts), shadeHex(col, f.f), 'rgba(0,0,0,.35)');
    if (E[2] > z1) fill(cam.clipPoly(poly.map(([x, y]) => [x, y, z1])), shadeHex(col, 1.12), 'rgba(0,0,0,.3)');
    ctx.globalAlpha = 1;
  }
  function roundRect(ctx, x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }
  function drawEye(ctx, x, y, s, C) {
    ctx.beginPath(); ctx.moveTo(x - s, y); ctx.quadraticCurveTo(x, y - s * .8, x + s, y); ctx.quadraticCurveTo(x, y + s * .8, x - s, y); ctx.closePath();
    ctx.fillStyle = C.sel; ctx.fill(); ctx.lineWidth = 1.5; ctx.strokeStyle = C.ink; ctx.stroke();
    ctx.beginPath(); ctx.arc(x, y, s * .33, 0, 2 * Math.PI); ctx.fillStyle = C.ink; ctx.fill();
  }
  // a simple figure: rounded body and head, the actor's color, initials on the chest, a face mark toward the facing
  function figure(ctx, cam, a, snap, h, seat, C, ghost, f) {
    const base = levelH(snap, h, a.on), hz = headZ(a, snap, h), top = hz - .22;
    const B = cam.proj([a.x, a.y, base]), Hc = cam.proj([a.x, a.y, hz]); if (!B || !Hc) return;
    const ppm = cam.s / Hc[2], bw = .46 * ppm, hr = .13 * ppm, sh = cam.proj([a.x, a.y, top]);
    const x = Hc[0], yTop = sh[1], yBot = B[1];
    f.box = {cx: x, top: Hc[1] - hr, bottom: yBot, w: bw};
    const L = h.light === 'areas' ? clamp(lightAt(snap, h, a.x, a.y) / 2 + (inSpot(snap, h, a.x, a.y) ? .5 : 0), 0, 1) : 1;
    // in the dark the figure drops to 30% (a gray rim keeps its shape on the dark floor, light initials stay AA);
    // half light 75%, full 100%; a fade in Run passes smoothly between them
    const br = L < .5 ? .3 + .9 * L : .5 + .5 * L, col = shadeHex(a.color, br), dim = br < .7, rim = dim ? '#8a8a94' : C.ink;
    ctx.save();
    if (ghost) { ctx.setLineDash([5, 4]); ctx.lineWidth = 2; ctx.strokeStyle = C.bad; }
    // body
    ctx.beginPath(); const r = Math.min(bw / 2, (yBot - yTop) / 2);
    roundRect(ctx, x - bw / 2, yTop, bw, Math.max(4, yBot - yTop), Math.max(2, r * .9));
    if (ghost) ctx.stroke(); else { ctx.fillStyle = col; ctx.fill(); ctx.lineWidth = 1.2; ctx.strokeStyle = rim; ctx.stroke(); }
    // head
    ctx.beginPath(); ctx.arc(x, Hc[1], hr, 0, 2 * Math.PI);
    if (ghost) ctx.stroke(); else {
      ctx.fillStyle = shadeHex(a.color, br * 1.08); ctx.fill(); ctx.lineWidth = 1.2; ctx.strokeStyle = rim; ctx.stroke();
      // the face: which way it turns, seen from this seat (signed angle between facing and the seat direction)
      const [fx, fy] = facingVec(a.facing || 0), dx = seat.x - a.x, dy = seat.y - a.y;
      const ang = Math.atan2(fx * dy - fy * dx, fx * dx + fy * dy);   // + when the actor faces to the seat's left
      if (Math.abs(ang) < 1.96) {
        const off = -Math.sin(ang) * hr * .55;
        ctx.fillStyle = dim ? '#f2f2f5' : C.ink;
        const er = Math.max(1, hr * .12);
        if (Math.abs(ang) < 1.2) { ctx.beginPath(); ctx.arc(x + off - hr * .3 * Math.cos(ang), Hc[1] - hr * .15, er, 0, 7); ctx.fill(); }
        ctx.beginPath(); ctx.arc(x + off + hr * .3 * Math.cos(ang), Hc[1] - hr * .15, er, 0, 7); ctx.fill();
      } else {
        ctx.beginPath(); ctx.arc(x, Hc[1], hr * .78, 0, 2 * Math.PI); ctx.fillStyle = shadeHex(a.color, br * .55); ctx.fill();
      }
      if (a.mask) {
        ctx.beginPath();
        if (a.mask === 'full') ctx.ellipse(x, Hc[1], hr * .85, hr * 1.05, 0, 0, 2 * Math.PI);
        else ctx.ellipse(x, Hc[1] - hr * .3, hr * .85, hr * .55, 0, 0, 2 * Math.PI);
        ctx.fillStyle = shadeHex('#efe6d2', dim ? .45 : 1); ctx.fill(); ctx.strokeStyle = C.ink; ctx.lineWidth = 1; ctx.stroke();
      }
      // initials on the chest
      const fs = Math.max(10, Math.min(28, bw * .42));
      ctx.font = `800 ${fs}px "Segoe UI",system-ui,sans-serif`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillStyle = dim ? '#f2f2f5' : C.ink; ctx.fillText(a.initials || initials(a.name), x, yTop + Math.min((yBot - yTop) * .35, fs * 1.1));
    }
    ctx.restore();
  }

  return {
    house, catalog, addPieces, WEIGHTS, POSES, POS, NOTE_TYPES,
    sight, bodyPos, focus, leader, upstaged, check, carry, edit, tween, play, free,
    areaOf, onStage, levels, lightAt, inSpot, lit, entrancePts, nearestEntrance, footprint, solids, initials,
    headZ, angleTo, inPoly, clone,
    view: {plan, house: houseView, camera},
  };
})();
