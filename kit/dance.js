// Curio Class family engine: dance (docs/families/dance.md). Exposes Dance.
// Inlined by scripts/bundle_tool.py from a kit:dance script tag, after kit:curio.
// Never write a closing script tag anywhere in this file (not even in a comment): the bundler inlines it between
// script tags and the page would end the script early.
// What it holds: the jointed dancer drawn from simple shapes (no face), the named pose library, the level modifier,
// stepping gaits, energy qualities, phrases, one count clock, a sequencer, floors (studio, square, stage, void),
// trails (ribbon, exposure), synthesized music locked to the clock, and the count strip. Dance keeps its own figure
// (Cory, decision w1-21: dance and PE do not share one figure; kit/movement.js is the PE family's own).
const Dance = (() => {
  const NS = 'http://www.w3.org/2000/svg';
  const RAD = Math.PI / 180;
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const lerp = (a, b, t) => a + (b - a) * t;
  const sin = d => Math.sin(d * RAD), cos = d => Math.cos(d * RAD);
  function mk(tag, at, parent) {
    const e = document.createElementNS(NS, tag);
    if (at) for (const k in at) e.setAttribute(k, at[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  const calm = () => typeof Curio !== 'undefined' && Curio.reduce;
  const soundOn = () => typeof Curio === 'undefined' || Curio.sound;
  let heard = false;   // nothing sounds before the first tap or key (browsers block it)
  for (const ev of ['pointerdown', 'keydown']) addEventListener(ev, () => { heard = true; }, {once: true, capture: true});

  // ---------------------------------------------------------------- poses
  // A pose is a set of joint angles in degrees. Body frame: X to the dancer's left, Y up, Z forward.
  //   head: head tilt forward (+) or back; tilt: head tilt to the dancer's left
  //   lean: trunk lean forward (+) or arch back; side: side bend to the dancer's left; twist: chest turns to the left
  //   lArm, rArm: [up, fwd, foreUp, foreFwd]: the upper arm's direction (up 0 hangs down, 90 level, 180 overhead;
  //     fwd 0 out to the side, 90 forward, -90 back, 180 across the body) and the forearm's, both in the trunk frame
  //   lLeg, rLeg: [hip, out, knee]: hip flexion forward (+) or back, hip out to the side, knee bend (0 straight)
  //   lToe, rToe (or toe for both): 0 flat foot, 1 up on the toes (relevé) or pointed
  //   pitch: the whole body tips forward (+90 lies face down, -90 on the back); roll: the whole body rolls to the left
  //   yaw: the whole body turns to its left (degrees), inside the pose: a floor shape can turn so its legs read lying
  //     along the floor while the dancer still faces the class
  //   lift: off the floor, in body heights (jumps)
  const NUM = ['head', 'tilt', 'lean', 'side', 'twist', 'lToe', 'rToe', 'pitch', 'roll', 'yaw', 'lift'];
  const ARR = ['lArm', 'rArm', 'lLeg', 'rLeg'];
  const BASE = {head: 0, tilt: 0, lean: 0, side: 0, twist: 0, lToe: 0, rToe: 0, pitch: 0, roll: 0, yaw: 0, lift: 0,
    lArm: [8, 0, 10, 30], rArm: [8, 0, 10, 30], lLeg: [0, 3, 0], rLeg: [0, 3, 0]};
  const hug = [70, 70, 85, 165], hips = [40, -25, 55, 165];
  // the shared named pose library. Each entry is a partial pose (filled from stand); it may carry its own high and
  // low versions, which win over the level modifier. Tools add their own: Dance.poses.myShape = {...}
  const poses = {
    // stand's own low version is a neat squat facing the class (the generic low modifier reads as a fall at rest)
    stand: {low: {lLeg: [108, 16, 140], rLeg: [108, 16, 140], lean: 30, head: -8, arms: [46, 70, 56, 96], lToe: .3, rToe: .3}},
    'reach-up': {arms: [176, 0, 178, 0], high: {toe: 1, arms: [179, 0, 180, 0], lean: -4}, low: {lLeg: [95, 6, 120], rLeg: [95, 6, 120], lean: 30, arms: [150, 30, 160, 30]}},
    'arms-wide': {arms: [90, 0, 92, 0], lLeg: [0, 12, 0], rLeg: [0, 12, 0]},
    'bend-fwd': {lean: 72, arms: [72, 90, 72, 90], head: 10},
    'bend-side': {side: 28, lArm: [20, 0, 15, 20], rArm: [165, 0, 175, -30]},
    twist: {twist: 40, arms: [90, 0, 92, 0]},
    curl: {lean: 38, head: 32, arms: hug, lLeg: [25, 4, 45], rLeg: [25, 4, 45]},
    crouch: {lLeg: [100, 8, 128], rLeg: [100, 8, 128], lean: 34, arms: [55, 85, 60, 90], head: -10},
    kneel: {lLeg: [0, 6, 92], rLeg: [0, 6, 92], lToe: 1, rToe: 1},
    sit: {lLeg: [90, 5, 0], rLeg: [90, 5, 0], lean: 4, arms: [28, -50, 30, -50], lToe: .6, rToe: .6},
    lie: {pitch: -90, arms: [168, 0, 170, 0], lToe: 1, rToe: 1},
    lunge: {lLeg: [72, 4, 82], rLeg: [-32, 4, 8], arms: [88, 90, 90, 90], lean: 8},
    plie: {lLeg: [30, 30, 62], rLeg: [30, 30, 62], arms: [62, 55, 70, 130]},
    releve: {toe: 1, arms: [165, 22, 172, 75]},
    passe: {rLeg: [80, 38, 135], lToe: 1, rToe: 1, arms: [165, 22, 172, 75]},
    arabesque: {lean: 22, rLeg: [-72, 2, 0], rToe: 1, lArm: [95, 85, 98, 85], rArm: [95, 10, 98, 10]},
    'star-jump': {arms: [140, 0, 142, 0], lLeg: [0, 26, 0], rLeg: [0, 26, 0], toe: 1, lift: .1},
    'tuck-jump': {lLeg: [100, 4, 130], rLeg: [100, 4, 130], arms: [80, 80, 90, 110], toe: 1, lift: .16},
    clap: {arms: [78, 72, 84, 158]},
    point: {rArm: [92, 55, 92, 55]},
    kick: {rLeg: [78, 0, 0], rToe: 1, arms: [90, 0, 92, 0]},
    stamp: {rLeg: [45, 2, 55], arms: [30, 0, 35, 20]},
    step: {lLeg: [24, 3, 6], rLeg: [-16, 3, 22], lArm: [22, -90, 26, -90], rArm: [22, 90, 40, 90]},
    hop: {rLeg: [-10, 3, 85], lift: .07, arms: [40, 30, 60, 60]},
    contraction: {lean: 30, head: 28, arms: [72, 60, 64, 138], lLeg: [18, 4, 26], rLeg: [18, 4, 26]},
    release: {lean: -18, head: -20, arms: [150, 18, 162, 18]},
    bow: {lean: 55, head: 18, lArm: [52, 90, 58, 90], rArm: [30, -60, 32, -60]},
  };
  // a full pose from a name, a partial or a full pose. arms / legs set both sides; lArm etc. win over them
  function pose(p) {
    if (typeof p === 'string') { if (!poses[p]) throw new Error('Dance: no pose "' + p + '"'); p = poses[p]; }
    p = p || {};
    const o = {};
    for (const k of NUM) o[k] = p[k] != null ? p[k] : BASE[k];
    if (p.toe != null) { if (p.lToe == null) o.lToe = p.toe; if (p.rToe == null) o.rToe = p.toe; }
    o.lArm = (p.lArm || p.arms || BASE.lArm).slice(); o.rArm = (p.rArm || p.arms || BASE.rArm).slice();
    o.lLeg = (p.lLeg || p.legs || BASE.lLeg).slice(); o.rLeg = (p.rLeg || p.legs || BASE.rLeg).slice();
    return o;
  }
  // left for right: the same shape on the other side
  function mirror(p) {
    p = pose(p);
    return {...p, tilt: -p.tilt, side: -p.side, twist: -p.twist, roll: -p.roll, yaw: -p.yaw, lToe: p.rToe, rToe: p.lToe,
      lArm: p.rArm.slice(), rArm: p.lArm.slice(), lLeg: p.rLeg.slice(), rLeg: p.lLeg.slice()};
  }
  // in-between of two full poses (t 0 to 1)
  function mix(a, b, t) {
    const o = {};
    for (const k of NUM) o[k] = lerp(a[k], b[k], t);
    for (const k of ARR) o[k] = a[k].map((v, i) => lerp(v, b[k][i], t));
    return o;
  }
  // the level modifier. High rises to the toes and lifts the arms; low bends the knees deep and leans the trunk
  // forward. A library pose (or a partial passed in) with its own high or low version uses that version instead.
  function level(p, lvl) {
    const src = typeof p === 'string' ? poses[p] : p;
    if (!lvl || lvl === 'middle') return pose(src);
    if (src && src[lvl]) return pose(src[lvl]);
    const o = pose(src);
    if (lvl === 'high') {
      o.lToe = Math.max(o.lToe, o.lLeg[0] > 40 ? o.lToe : 1); o.rToe = Math.max(o.rToe, o.rLeg[0] > 40 ? o.rToe : 1);
      for (const k of ['lArm', 'rArm']) { const a = o[k]; a[0] = Math.max(a[0], 150); a[2] = Math.max(a[2], 158); a[1] = clamp(a[1], -30, 60); a[3] = clamp(a[3], -30, 70); }
      o.lean = Math.min(o.lean, 8); o.lift *= 1.5;
    } else if (lvl === 'low') {
      for (const k of ['lLeg', 'rLeg']) { const l = o[k]; l[0] += 48; l[1] += 18; l[2] += 80; }   // a wide, deep squat (reads from the front too)
      o.lean += 24;
      for (const k of ['lArm', 'rArm']) { const a = o[k]; if (a[0] > 60) { a[0] = 60; a[2] = Math.min(a[2], 70); } }
      o.lift *= .45; o.lToe = Math.min(o.lToe, .3); o.rToe = Math.min(o.rToe, .3);
    }
    return o;
  }

  // ---------------------------------------------------------------- energy qualities (Dance.dyn)
  // ease(t): how far between two keyframes the dancer is at t (0 to 1) of a count; jitter: a small fast shake
  const dyn = {
    smooth: {ease: t => (1 - Math.cos(Math.PI * t)) / 2},
    sharp: {ease: t => t >= .2 ? 1 : 1 - Math.pow(1 - t / .2, 3)},
    swing: {ease: t => t - Math.sin(2 * Math.PI * t) / (2 * Math.PI), dip: .025},
    suspend: {ease: t => 1 - Math.pow(1 - t, 3)},
    collapse: {ease: t => t < .55 ? t * .08 : .044 + .956 * Math.pow((t - .55) / .45, 2)},
    shake: {ease: t => (1 - Math.cos(Math.PI * t)) / 2, jitter: 7},
  };

  // ---------------------------------------------------------------- gaits (Dance.gaits)
  // a stepping cycle: counts per cycle, which way the dancer faces ('travel' or 'front'), and pose(q, dir) for the
  // phase q (0 to 1 of the cycle) returning {pose (partial), lift}. dir: +1 travels to the dancer's left, -1 right
  // (used by slide). swing: true for gaits danced to swung eighths (skip, gallop).
  const sag = a => a >= 0 ? [a, 90] : [-a, -90];
  function arm(a, bend = 18, out = 8) {
    const [u, f] = sag(a), [u2, f2] = sag(a + bend);
    return [u, f > 0 ? f - out : f + out, u2, f2 > 0 ? f2 - out : f2 + out];
  }
  const sm = t => t <= 0 ? 0 : t >= 1 ? 1 : (1 - Math.cos(Math.PI * t)) / 2;
  const seg = (q, a, b) => sm((q - a) / (b - a));
  const gaits = {
    walk: {counts: 2, facing: 'travel', pose(q) {
      const s = Math.sin(2 * Math.PI * q), c = Math.cos(2 * Math.PI * q);
      return {pose: {lLeg: [24 * s, 3, 8 + 30 * Math.max(0, c)], rLeg: [-24 * s, 3, 8 + 30 * Math.max(0, -c)],
        lArm: arm(-22 * s), rArm: arm(22 * s), lean: 3}, lift: 0};
    }},
    run: {counts: 1, facing: 'travel', pose(q) {
      const s = Math.sin(2 * Math.PI * q), c = Math.cos(2 * Math.PI * q);
      return {pose: {lLeg: [36 * s, 3, 14 + 70 * Math.max(0, c)], rLeg: [-36 * s, 3, 14 + 70 * Math.max(0, -c)],
        lArm: arm(-40 * s, 80), rArm: arm(40 * s, 80), lean: 12}, lift: .035 * Math.abs(Math.sin(2 * Math.PI * q))};
    }},
    skip: {counts: 2, facing: 'travel', swing: true, pose(q) {
      // each count is a step-hop: leg A steps down from the knee-up shape, leg B swings up into it; they swap each count
      const half = q < .5, u = (q * 2) % 1;
      const down = seg(u, 0, .3), up = seg(u, .25, .8);
      const A = [lerp(62, 8, down) - 14 * seg(u, .3, 1), 3, lerp(85, 8, down)], B = [lerp(-6, 62, up), 3, lerp(10, 85, up)];
      const aArm = arm(lerp(-30, 70, up), 30), bArm = arm(lerp(70, -30, down), 30);
      const lift = u > .45 ? .065 * Math.sin(Math.PI * clamp((u - .45) / .5, 0, 1)) : 0;
      return half ? {pose: {lLeg: A, rLeg: B, lArm: aArm, rArm: bArm, lean: 4}, lift}
        : {pose: {rLeg: A, lLeg: B, rArm: aArm, lArm: bArm, lean: 4}, lift};
    }},
    gallop: {counts: 1, facing: 'travel', swing: true, pose(q) {
      // the same foot leads every time; the back foot catches up, then a short flight
      const close = seg(q, 0, .5), open = seg(q, .55, 1);
      const r = lerp(lerp(-26, 2, close), -26, open);
      const lift = q > .35 && q < .9 ? .055 * Math.sin(Math.PI * (q - .35) / .55) : 0;
      const fl = lift / .055;   // in the air: the lead knee lifts like a pony's front leg
      return {pose: {lLeg: [lerp(30, 22, close) + 8 * open + 26 * fl, 3, 12 + 10 * close + 55 * fl], rLeg: [r - 6 * fl, 3, 14 + 10 * close + 20 * fl],
        lArm: arm(45 + 15 * fl, 40), rArm: arm(30 - 10 * fl, 40), lean: 5}, lift};
    }},
    slide: {counts: 1, facing: 'front', swing: false, pose(q, dir = 1) {
      // step out sideways, then the other foot closes (step-together) with a tiny lift
      const out = seg(q, 0, .42), shut = seg(q, .45, .85);
      const lead = lerp(3, 26, out), trail = 3 + 0 * shut;
      const a = lerp(lead, 3, shut);
      const lift = q > .5 && q < .95 ? .03 * Math.sin(Math.PI * (q - .5) / .45) : 0;
      const legs = dir > 0 ? {lLeg: [0, a, 6], rLeg: [0, trail + 2 * shut, 6]} : {rLeg: [0, a, 6], lLeg: [0, trail + 2 * shut, 6]};
      return {pose: {...legs, arms: [82, 0, 86, 0], roll: 3 * dir * (out - shut)}, lift};
    }},
    hop: {counts: 1, facing: 'travel', pose(q) {
      const lift = .075 * Math.sin(Math.PI * q);
      return {pose: {lLeg: [6 * Math.sin(2 * Math.PI * q), 3, 10 + 25 * (1 - Math.sin(Math.PI * q))], rLeg: [-12, 3, 85],
        arms: arm(30 + 25 * Math.sin(Math.PI * q), 40), lToe: Math.sin(Math.PI * q)}, lift};
    }},
    march: {counts: 2, facing: 'travel', pose(q) {
      const s = Math.sin(2 * Math.PI * q);
      return {pose: {lLeg: [70 * Math.max(0, s), 3, 88 * Math.max(0, s)], rLeg: [70 * Math.max(0, -s), 3, 88 * Math.max(0, -s)],
        lArm: arm(-32 * s, 75), rArm: arm(32 * s, 75)}, lift: 0};
    }},
    leap: {counts: 2, facing: 'travel', pose(q) {
      if (q < .5) { const r = gaits.run.pose(q * 2 % 1); return r; }
      const u = (q - .5) * 2, f = Math.sin(Math.PI * u);
      return {pose: {lLeg: [lerp(20, 68, f), 3, lerp(40, 4, f)], rLeg: [lerp(-20, -58, f), 3, lerp(40, 14, f)],
        lArm: [lerp(60, 150, f), 80, lerp(70, 155, f), 80], rArm: [lerp(40, 95, f), 0, lerp(45, 95, f), 0], rToe: f, lToe: f, lean: 8}, lift: .15 * f};
    }},
  };

  // ---------------------------------------------------------------- paths on the floor (floor units)
  // Dance.path(points, {smooth}): a polyline with arc length. at(u) gives {x, z, dx, dz} for u 0 to 1 (dx, dz: the
  // direction of travel, averaged over a short window so corners turn quickly but not in one frame).
  function path(pts, o = {}) {
    if (o.smooth) pts = spline(pts, o.smooth === true ? 8 : o.smooth);
    pts = pts.map(p => Array.isArray(p) ? {x: p[0], z: p[1]} : {x: p.x, z: p.z});
    const cum = [0];
    for (let i = 1; i < pts.length; i++) cum.push(cum[i - 1] + Math.hypot(pts[i].x - pts[i - 1].x, pts[i].z - pts[i - 1].z));
    const length = cum[cum.length - 1];
    function pointAt(s) {
      s = clamp(s, 0, length);
      let i = 1; while (i < cum.length - 1 && cum[i] < s) i++;
      const a = pts[i - 1], b = pts[i] || a, l = (cum[i] - cum[i - 1]) || 1, t = (s - cum[i - 1]) / l;
      return {x: lerp(a.x, b.x, t), z: lerp(a.z, b.z, t)};
    }
    function at(u) {
      const s = u * length, p = pointAt(s), w = Math.min(2.5, length / 6 || 1);
      const a = pointAt(s - w), b = pointAt(s + w); let dx = b.x - a.x, dz = b.z - a.z;
      const n = Math.hypot(dx, dz) || 1;
      return {x: p.x, z: p.z, dx: dx / n, dz: dz / n};
    }
    return {points: pts, length, at, pointAt};
  }
  // a smooth curve through points (Catmull-Rom), n samples per span
  function spline(pts, n = 8) {
    pts = pts.map(p => Array.isArray(p) ? {x: p[0], z: p[1]} : p);
    if (pts.length < 3) return pts;
    const out = [];
    for (let i = 0; i < pts.length - 1; i++) {
      const p0 = pts[i - 1] || pts[i], p1 = pts[i], p2 = pts[i + 1], p3 = pts[i + 2] || p2;
      for (let k = 0; k < n; k++) {
        const t = k / n, t2 = t * t, t3 = t2 * t;
        const f = (a, b, c, d) => .5 * (2 * b + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t2 + (-a + 3 * b - 3 * c + d) * t3);
        out.push({x: f(p0.x, p1.x, p2.x, p3.x), z: f(p0.z, p1.z, p2.z, p3.z)});
      }
    }
    out.push(pts[pts.length - 1]);
    return out;
  }
  const paths = {
    line: (a, b) => path([a, b]),
    arc: (cx, cz, r, a0, a1, n = 48) => path(Array.from({length: n + 1}, (_, i) => { const a = lerp(a0, a1, i / n); return [cx + r * cos(a), cz + r * sin(a)]; })),
    poly: pts => path(pts),
    smooth: (pts, n) => path(pts, {smooth: n || 8}),
    join: (...ps) => path(ps.flatMap((p, i) => i ? p.points.slice(1) : p.points)),
  };

  // ---------------------------------------------------------------- reading a drawn pathway (Dance.readPath)
  // readPath(raw points in floor units, {start, bounds, floor, ...RP}) -> {tooShort} or {parts, geo, length, lead}.
  // parts: [{kind: 'straight' | 'curved' | 'zigzag', pts, geo}] in drawing order, at most maxParts.
  // With `floor` (a Dance.floor) the drawing is read as it looks on screen, in units of the floor's scale at mid
  // depth, so a shape reads the same drawn side to side, front to back or on a slant; parts come back in floor units.
  // The rule, in order:
  //  1. Smooth the drag, resample it 1 unit apart and simplify it (tol). Under minLen units in all: tooShort.
  //  2. A corner turns sharp or more on the simplified line (points under 7 units apart count as one), all within 8
  //     units, at least local and half of that turn within 4 units of the point, and a real tip: on a barely
  //     smoothed copy of the line, tipK of the turn or more happens within 1.5 units (8 pixels on a small stage) of
  //     its sharpest point. The tip of a wave or an S, however tight, spreads its turn out and is not a corner.
  //  3. Two or more corners in a row that each turn zigMin or more, turn left and right in turn (or both turn hair
  //     degrees or more, as a scribble's hairpins do), and are joined by straight legs of zigMax units or less make one
  //     zigzag. Corners that turn the same way and less than hair (an L, a box) stay part boundaries.
  //  4. The leg before and after a zigzag joins it when it is straight, no longer than sideK zigzag legs and zigMax,
  //     and its corner turns at least sideT of the run's middle turn (a straight line that bends gently into a zigzag
  //     stays its own part); a curved leg gives the zigzag only its straight start, when that is 0.4 legs or more.
  //  5. Any other stretch is curved when its heading swings curve degrees (curveScreen with a floor) or more, else
  //     straight. A straight end is
  //     split off a curve only when it is long (25 units and a quarter of the stretch), the rest turns 90 degrees or
  //     more, and the bend starts at once (a rainbow or an S stays one curved part).
  //  6. A start more than 8 units from `start` adds a straight lead from it. Parts past maxParts join the last one.
  const RP = {tol: 2, sharp: 45, local: 32, tipK: .47, zigTurn: 75, zigMin: 60, zigMax: 90, hair: 100, sideK: 3, sideT: .6, curve: 30, curveScreen: 24, minLen: 15, maxParts: 4};
  const pd = (a, b) => Math.hypot(a.x - b.x, a.z - b.z);
  const plen = pts => { let s = 0; for (let i = 1; i < pts.length; i++) s += pd(pts[i], pts[i - 1]); return s; };
  function rpSmooth(pts, k) {
    return pts.map((p, i) => { if (i === 0 || i === pts.length - 1) return p; let x = 0, z = 0, n = 0; for (let j = Math.max(0, i - k); j <= Math.min(pts.length - 1, i + k); j++) { x += pts[j].x; z += pts[j].z; n++; } return {x: x / n, z: z / n}; });
  }
  function rpResample(pts, step) {
    const out = [pts[0]]; let acc = 0;
    for (let i = 1; i < pts.length; i++) {
      let a = pts[i - 1]; const b = pts[i]; let d = pd(a, b);
      while (acc + d >= step) { const t = (step - acc) / d; a = {x: a.x + (b.x - a.x) * t, z: a.z + (b.z - a.z) * t}; out.push(a); d = pd(a, b); acc = 0; }
      acc += d;
    }
    if (pd(out[out.length - 1], pts[pts.length - 1]) > .3) out.push(pts[pts.length - 1]);
    return out;
  }
  const lineOff = (A, B, P) => Math.abs((B.x - A.x) * (A.z - P.z) - (A.x - P.x) * (B.z - A.z)) / (pd(A, B) || 1e-9);
  function rpSimplify(pts, tol) {
    const keep = new Array(pts.length).fill(false); keep[0] = keep[pts.length - 1] = true;
    const st = pts.length > 2 ? [[0, pts.length - 1]] : [];
    while (st.length) {
      const [a, b] = st.pop(); let md = 0, mi = -1;
      for (let i = a + 1; i < b; i++) { const d = lineOff(pts[a], pts[b], pts[i]); if (d > md) { md = d; mi = i; } }
      if (md > tol) { keep[mi] = true; st.push([a, mi], [mi, b]); }
    }
    const out = pts.filter((_, i) => keep[i]);
    out.idx = keep.map((k, i) => k ? i : -1).filter(i => i >= 0);   // where each kept point sits in pts
    return out;
  }
  // signed turn at b, degrees (one way positive, the other negative)
  const sturn = (a, b, c) => { let d = (Math.atan2(c.z - b.z, c.x - b.x) - Math.atan2(b.z - a.z, b.x - a.x)) / RAD; while (d > 180) d -= 360; while (d < -180) d += 360; return d; };
  // how far the heading swings along dense points (chords 6 units long): a steady hand wobble stays small, an arc or an
  // S swings by its full turn
  const headingRange = (d, step = 6) => {
    const hs = [];
    for (let i = 0; i + step < d.length; i += 2) hs.push(Math.atan2(d[i + step].z - d[i].z, d[i + step].x - d[i].x) / RAD);
    if (d.length > step) hs.push(Math.atan2(d[d.length - 1].z - d[d.length - 1 - step].z, d[d.length - 1].x - d[d.length - 1 - step].x) / RAD);
    let lo = 0, hi = 0, h = 0;
    for (let i = 1; i < hs.length; i++) { let dd = hs[i] - hs[i - 1]; while (dd > 180) dd -= 360; while (dd < -180) dd += 360; h += dd; lo = Math.min(lo, h); hi = Math.max(hi, h); }
    return hi - lo;
  };
  // how many points from the start stay within w of one line
  const straightRun = (arr, w = .6) => { let e = 1; for (let m = 2; m < arr.length; m++) { let ok = true; for (let q = 1; q < m; q++) if (lineOff(arr[0], arr[m], arr[q]) > w) { ok = false; break; } if (!ok) break; e = m; } return Math.min(e, arr.length - 1); };
  const isStraight = d => { const L = plen(d); return d.length < 3 || d.every(p => lineOff(d[0], d[d.length - 1], p) <= Math.max(2, L * .08)); };
  // a stretch with no corner (dense points 1 unit apart): straight, curved, or a long straight end and a curve
  function rpBend(dense, C, trim = [false, false]) {
    if (dense.length < 2) return [];
    const simp = rpSimplify(dense, C.tol);
    // the curve test leaves out 4 units at an end that is a corner, where the hand-drawn corner's rounding spills in
    const core = dense.length > 24 ? dense.slice(trim[0] ? 4 : 0, dense.length - (trim[1] ? 4 : 0)) : dense;
    if (headingRange(core) < C.curve) return [{kind: 'straight', pts: [dense[0], dense[dense.length - 1]]}];
    const total = plen(dense);
    // a straight end of arr (from its start) that may stand alone: long, the rest turns 90 or more as a clear,
    // tight bend (2.2 degrees a unit on average, about a half circle 25 units wide or smaller) that starts at once
    // (12 degrees or more over the 8 units past the straight). A rainbow's long, nearly straight sides bend in
    // slowly, so a rainbow stays one curve
    const endRun = arr => {
      const e = straightRun(arr, 1.6), L = plen(arr.slice(0, e + 1)), rest = arr.slice(e);
      if (L < Math.max(25, total * .25) || rest.length < 16) return 0;
      const rt = headingRange(rest);
      if (rt < 90) return 0;
      const near = Math.abs(sturn(rest[0], rest[8], rest[16])), k = rt / plen(rest);
      return near >= 12 && k >= 2.2 ? e : 0;
    };
    const a = endRun(dense), rb = endRun(dense.slice().reverse()), b = rb ? dense.length - 1 - rb : dense.length - 1;
    if (!a && !rb || b - a < 8) return [{kind: 'curved', pts: simp}];
    const out = [];
    if (a) out.push({kind: 'straight', pts: [dense[0], dense[a]]});
    out.push({kind: 'curved', pts: rpSimplify(dense.slice(a, b + 1), C.tol)});
    if (rb) out.push({kind: 'straight', pts: [dense[b], dense[dense.length - 1]]});
    return out;
  }
  function readPath(raw, o = {}) {
    // with a floor, read the drawing as it looks on screen (screen pixels over the floor's scale at mid depth), so a
    // shape reads the same whichever way it is drawn; the parts come back in floor units
    if (o.floor) {
      const F = o.floor, k = F.scale(30), B = o.bounds || {x0: 0, x1: 100, z0: 0, z1: 60};
      const to = p => { const q = F.project(clamp(p.x, B.x0, B.x1), 0, clamp(p.z, B.z0, B.z1)); return {x: q[0] / k, z: q[1] / k}; };
      const back = p => { const q = F.unmap(p.x * k, p.z * k); return {x: clamp(q.x, B.x0, B.x1), z: clamp(q.z, B.z0, B.z1)}; };
      const r = readPath((raw || []).map(to), {curve: RP.curveScreen, ...o, floor: null, px: 1 / k, bounds: {x0: -1e9, x1: 1e9, z0: -1e9, z1: 1e9}, start: o.start ? to(o.start) : null});
      if (r.tooShort) return r;
      for (const p of r.parts) { p.pts = p.pts.map(back); p.geo = p.geo.map(back); }
      r.geo = r.parts.flatMap((p, i) => i ? p.geo.slice(1) : p.geo); r.length = plen(r.geo);
      return r;
    }
    const C = {...RP, ...o}, B = o.bounds || {x0: 0, x1: 100, z0: 0, z1: 60};
    let pts = (raw || []).map(p => ({x: clamp(p.x, B.x0, B.x1), z: clamp(p.z, B.z0, B.z1)}));
    if (pts.length < 2 || plen(pts) < C.minLen) return {tooShort: true};
    // fine: barely smoothed, half a unit apart, for how sharp a corner's tip is
    // (on a small stage a pixel is a large share of a unit, so the fine scale never goes under a few pixels)
    const px = C.px || 0, fs = Math.max(.5, 1.5 * px), fw = u => Math.max(1, Math.round(u / fs));
    const fine = rpResample(rpSmooth(rpResample(pts, fs), 1), fs);
    const W3 = fw(Math.max(1.5, 8 * px));
    pts = rpResample(rpSmooth(rpResample(pts, .8), 3), 1);
    const lead = !!o.start && pd(pts[0], o.start) > 8;
    const simp = rpSimplify(pts, C.tol), n = simp.length;
    // 2. corners with their signed turn. Simplified points closer than 7 units count as one corner (a hand-drawn
    // corner often simplifies to two points of half the turn each); d: its point in pts
    const corners = [], groups = [];
    for (let i = 1; i < n - 1; i++) {
      const t = sturn(simp[i - 1], simp[i], simp[i + 1]), g = groups[groups.length - 1];
      if (Math.abs(t) < 12) continue;
      if (g && g.last === i - 1 && pd(simp[i - 1], simp[i]) < 7 && Math.sign(t) === Math.sign(g.t)) { g.t += t; g.last = i; g.big = Math.abs(t) > Math.abs(g.bt) ? (g.bt = t, i) : g.big; }
      else groups.push({first: i, last: i, t, bt: t, big: i});
    }
    for (const g of groups) {
      const a = simp.idx[g.first], b = simp.idx[g.last], d = Math.round((a + b) / 2), at = Math.abs(g.t);
      // sharp at the point: the turn happens within 8 units, and half of it or more within 4 units of either end of
      // that (a tight arc spreads its turn out, so it is not a corner)
      const loc = Math.abs(sturn(pts[Math.max(0, a - 4)], pts[d], pts[Math.min(pts.length - 1, b + 4)]));
      // a gentle corner (under zigTurn) must be sharper right at the point, and not a hook in the last 10 units
      const gentle = at < C.zigTurn, hook = gentle && (d < 10 || d > pts.length - 11);
      // and a real tip: on the barely smoothed line, half the turn or more is made within 1.5 units (or 8 pixels) of
      // the sharpest point. A hand-drawn corner turns there; the tip of a wave or an S, however tight, spreads its turn
      // out, so it stays one curve whichever way it is drawn
      const T = (i, w) => i - w < 0 || i + w >= fine.length ? 0 : Math.abs(sturn(fine[i - w], fine[i], fine[i + w]));
      const fd = Math.round(d / fs), S3 = fw(Math.max(3, 12 * px));
      let ni = 0, nd = 1e9; for (let i = Math.max(0, fd - fw(40)); i <= Math.min(fine.length - 1, fd + fw(40)); i++) { const q = pd(fine[i], pts[d]); if (q < nd) { nd = q; ni = i; } }
      let tv = 0; for (let i = Math.max(W3, ni - S3); i <= Math.min(fine.length - 1 - W3, ni + S3); i++) tv = Math.max(tv, T(i, W3));
      if (at >= C.sharp && b - a <= 8 && !hook && loc >= Math.max(C.local, at * (gentle ? .6 : .5)) && tv >= C.tipK * at) corners.push({d, t: g.t});
    }
    // legs: dense ranges between cuts (the ends and the corners); leg j lies between corner j-1 and corner j
    const cuts = [0, ...corners.map(c => c.d), pts.length - 1];
    const legs = cuts.slice(0, -1).map((a, j) => { const d = pts.slice(a, cuts[j + 1] + 1); return {a, b: cuts[j + 1], len: plen(d), straight: isStraight(d)}; });
    // 3. zigzag runs of corners k..e
    const own = legs.map(() => null);   // per leg: {run, from, to}, the dense range a zigzag takes from it
    const zc = c => Math.abs(c.t) >= C.zigMin;
    let k = 0, runId = 0;
    while (k < corners.length) {
      let e = k;
      // the next corner alternates, or both are hairpins (a scribble), and the leg between is a short straight one
      const turnOn = (c0, c1) => Math.sign(c1.t) !== Math.sign(c0.t) || (Math.abs(c0.t) >= C.hair && Math.abs(c1.t) >= C.hair);
      if (zc(corners[k])) while (e + 1 < corners.length && zc(corners[e + 1]) && turnOn(corners[e], corners[e + 1]) && legs[e + 1].straight && legs[e + 1].len <= C.zigMax) e++;
      if (e > k) {
        const r = ++runId, inner = [];
        for (let j = k + 1; j <= e; j++) { own[j] = {run: r, from: legs[j].a, to: legs[j].b}; inner.push(legs[j].len); }
        inner.sort((x, y) => x - y);
        const m = inner[inner.length >> 1], ts = corners.slice(k, e + 1).map(c => Math.abs(c.t)).sort((x, y) => x - y), mt = ts[ts.length >> 1];
        // 4. the legs on either side
        const side = (j, after) => {
          const L = legs[j];
          if (!L || own[j]) return;
          // a straight side leg is one more zigzag leg when its corner turns about as much as the run's (a straight
          // line that bends gently into a zigzag stays its own part)
          const jc = corners[after ? e : k];
          if (L.straight && L.len <= Math.min(C.zigMax, m * C.sideK) && Math.abs(jc.t) >= Math.max(C.zigMin, C.sideT * mt)) { own[j] = {run: r, from: L.a, to: L.b}; return; }
          if (L.straight) return;
          const d = pts.slice(L.a, L.b + 1), arr = after ? d : d.slice().reverse(), q = straightRun(arr, 1);
          if (plen(arr.slice(0, q + 1)) < m * .4) return;
          own[j] = after ? {run: r, from: L.a, to: L.a + q} : {run: r, from: L.b - q, to: L.b};
        };
        side(k, false); side(e + 1, true);
      }
      k = e + 1;
    }
    // pieces in order: zigzag pieces of the same run join; free stretches go through rpBend
    const parts = [];
    let zig = null;
    const isCut = i => i > 0 && i < pts.length - 1 && cuts.includes(i);
    const free = (a, b) => { if (b - a < 1) return; zig = null; parts.push(...rpBend(pts.slice(a, b + 1), C, [isCut(a), isCut(b)])); };
    legs.forEach((L, j) => {
      const w = own[j];
      if (!w) return free(L.a, L.b);
      if (w.from > L.a) free(L.a, w.from);
      if (zig && zig.run === w.run) zig.d.push(...pts.slice(w.from + 1, w.to + 1));
      else { zig = {run: w.run, d: pts.slice(w.from, w.to + 1)}; parts.push({kind: 'zigzag', z: zig}); }
      if (w.to < L.b) free(w.to, L.b);
    });
    // a straight leg next to a straight leg with no corner between them cannot happen; two straights at a gentle
    // corner (under sharp) were one leg already
    for (const p of parts) if (p.z) { p.pts = rpSimplify(p.z.d, C.tol); delete p.z; }
    if (lead) parts.unshift({kind: 'straight', pts: [{x: o.start.x, z: o.start.z}, pts[0]], lead: true});
    while (parts.length > C.maxParts) { const p = parts.pop(); parts[C.maxParts - 1].pts.push(...p.pts.slice(1)); }
    // each part redrawn clean: straight as one line, curved through its points, zigzag through its corners
    for (const p of parts) p.geo = p.kind === 'straight' ? [p.pts[0], p.pts[p.pts.length - 1]] : p.kind === 'curved' ? spline(p.pts, 8) : p.pts.map(q => ({x: q.x, z: q.z}));
    const geo = parts.flatMap((p, i) => i ? p.geo.slice(1) : p.geo);
    return {parts, geo, length: plen(geo), lead};
  }

  // ---------------------------------------------------------------- floors (Dance.floor)
  // Floor units: x 0 (left) to 100 (right), z 0 (back) to 60 (front). A pinhole camera looks at the floor from the
  // front: project(x, y, z) gives [screenX, screenY, distance] for a point y floor units above the floor.
  function floor(svg, view = 'studio', o = {}) {
    const layers = {};
    for (const k of ['bg', 'floor', 'marks', 'mirror', 'trail', 'shadow', 'actors', 'front']) layers[k] = mk('g', {class: 'dz-' + k}, svg);
    const fns = [];
    const f = {view, svg, layers, w: 0, h: 0, d0: 100, F: 1, cx: 0, hz: 0, FH: 1, opts: o, uid: 'dz' + Math.random().toString(36).slice(2, 7),
      project(x, y, z) { const D = (60 - z) + f.d0; return [f.cx + f.F * (x - 50) / D, f.hz + (f.FH - f.F * y) / D, D]; },
      map(x, z) { const [px, py, D] = f.project(x, 0, z); return {x: px, y: py, s: f.F / D}; },
      unmap(px, py) { const D = f.FH / Math.max(1e-6, py - f.hz); return {x: 50 + (px - f.cx) * D / f.F, z: 60 + f.d0 - D}; },
      scale(z) { return f.F / ((60 - z) + f.d0); },
      inside: (x, z, pad = 0) => x >= pad && x <= 100 - pad && z >= pad && z <= 60 - pad,
      onResize(fn) { fns.push(fn); },
      // box: {x0, x1, yBack, yFront}: where the floor's front edge (x0 to x1) and its back and front edges sit on screen
      resize(w, h, box) {
        f.w = w; f.h = h;
        const b = box || {x0: w * .06, x1: w * .94, yBack: h * .38, yFront: h * .9};
        f.box = b; f.d0 = view === 'stage' ? 140 : view === 'void' ? 120 : 100;
        f.F = b.x1 - b.x0; f.cx = (b.x0 + b.x1) / 2;
        f.FH = (b.yFront - b.yBack) / (1 / f.d0 - 1 / (60 + f.d0));
        f.hz = b.yFront - f.FH / f.d0;
        // a dancer's height in floor units: about 40 percent of the stage height at the front of the floor
        f.dancerHeight = clamp((o.dancerFrac || .4) * h / f.scale(50), 18, 44);
        draw(); fns.forEach(fn => fn(f));
      },
      quad(x0, z0, x1, z1) { return [[x0, z0], [x1, z0], [x1, z1], [x0, z1]].map(([x, z]) => f.project(x, 0, z).slice(0, 2).join(',')).join(' '); },
    };
    function draw() {
      layers.bg.textContent = ''; layers.floor.textContent = '';
      // decoration redrawn on every resize: deco sits over the actors (curtains), back over the mirror and under them (barre)
      if (f.deco) { f.deco.remove(); f.back.remove(); }
      f.deco = mk('g', {class: 'dz-deco'}, null); layers.front.insertBefore(f.deco, layers.front.firstChild);
      f.back = mk('g', {class: 'dz-back'}, null); layers.mirror.after(f.back);
      const {w, h} = f, P = (x, y, z) => f.project(x, y, z).slice(0, 2).map(v => v.toFixed(1)).join(',');
      const id = f.uid, defs = mk('defs', {}, layers.bg);
      if (view === 'studio') {
        const c = {wall: '#eef6f5', wall2: '#e2efed', mirror: '#dbe9ee', wood: '#e9d3b0', wood2: '#d9b98a', plank: '#cfae80', barre: '#a8794a', ...(o.colors || {})};
        const g1 = mk('linearGradient', {id: id + 'w', x1: 0, y1: 0, x2: 0, y2: 1}, defs);
        mk('stop', {offset: 0, 'stop-color': c.wall2}, g1); mk('stop', {offset: 1, 'stop-color': c.wall}, g1);
        const g2 = mk('linearGradient', {id: id + 'f', x1: 0, y1: 0, x2: 0, y2: 1}, defs);
        mk('stop', {offset: 0, 'stop-color': c.wood2}, g2); mk('stop', {offset: 1, 'stop-color': c.wood}, g2);
        mk('rect', {x: 0, y: 0, width: w, height: h, fill: `url(#${id}w)`}, layers.bg);
        // side walls: the floor's edges carried up to the top of the stage
        const [blx, bly] = f.project(0, 0, 0), [brx] = f.project(100, 0, 0), [flx, fly] = f.project(0, 0, 60), [frx] = f.project(100, 0, 60);
        mk('polygon', {points: `${flx},${fly} ${blx},${bly} ${blx},0 ${Math.min(flx, 0)},0 ${Math.min(flx, 0)},${fly}`, fill: '#e3efed'}, layers.bg);
        mk('polygon', {points: `${frx},${fly} ${brx},${bly} ${brx},0 ${Math.max(frx, w)},0 ${Math.max(frx, w)},${fly}`, fill: '#e3efed'}, layers.bg);
        mk('line', {x1: blx, y1: 0, x2: blx, y2: bly, stroke: '#c9dcd9', 'stroke-width': 2}, layers.bg);
        mk('line', {x1: brx, y1: 0, x2: brx, y2: bly, stroke: '#c9dcd9', 'stroke-width': 2}, layers.bg);
        // the mirror strip on the back wall, with a soft sheen, and the barre in front of it
        const m0 = f.project(4, 8, 0), m1 = f.project(96, f.wallTop() * .94, 0);
        f.mirror = {x: m0[0], y: m1[1], w: m1[0] - m0[0], h: m0[1] - m1[1]};
        mk('rect', {x: f.mirror.x, y: f.mirror.y, width: f.mirror.w, height: f.mirror.h, fill: c.mirror, stroke: '#b8ccd3', 'stroke-width': 3, rx: 3}, layers.bg);
        const cp = mk('clipPath', {id: id + 'm'}, defs);
        mk('rect', {x: f.mirror.x + 2, y: f.mirror.y + 2, width: f.mirror.w - 4, height: f.mirror.h - 4}, cp);
        layers.mirror.setAttribute('clip-path', `url(#${id}m)`);
        f.sheen = mk('g', {'clip-path': `url(#${id}m)`, opacity: .55}, f.back);
        for (const k of [.18, .52, .78]) {
          const x = f.mirror.x + f.mirror.w * k, s = f.mirror.h;
          mk('polygon', {points: `${x},${f.mirror.y} ${x + s * .35},${f.mirror.y} ${x + s * .05},${f.mirror.y + s} ${x - s * .3},${f.mirror.y + s}`, fill: '#ffffff', opacity: .35}, f.sheen);
        }
        // the barre: a wooden rail on brackets, in front of the mirror at about hip height of a grown-up
        const bh = f.wallTop() * .52, b0 = f.project(4, bh, 1.5), b1 = f.project(96, bh, 1.5);
        for (const x of [10, 50, 90]) { const p = f.project(x, bh, 1.5), q = f.project(x, bh, 0); mk('line', {x1: p[0], y1: p[1], x2: q[0], y2: q[1] + 6, stroke: '#8b6a45', 'stroke-width': 3}, f.back); }
        mk('line', {x1: b0[0], y1: b0[1], x2: b1[0], y2: b1[1], stroke: c.barre, 'stroke-width': Math.max(4, f.scale(1.5) * 1.1), 'stroke-linecap': 'round'}, f.back);
        f.barre = {y: b0[1]};
        // floor, planks running front to back, a skirting line, two window light patches
        mk('polygon', {points: f.quad(0, 0, 100, 60), fill: `url(#${id}f)`}, layers.floor);
        for (let x = 0; x <= 100; x += 6.25) mk('line', {x1: P(x, 0, 0).split(',')[0], y1: bly, x2: P(x, 0, 60).split(',')[0], y2: fly, stroke: c.plank, 'stroke-width': 1, opacity: .7}, layers.floor);
        for (const z of [9, 21, 34, 48]) mk('line', {x1: P(0, 0, z).split(',')[0], y1: P(0, 0, z).split(',')[1], x2: P(100, 0, z).split(',')[0], y2: P(100, 0, z).split(',')[1], stroke: c.plank, 'stroke-width': .8, opacity: .35}, layers.floor);
        mk('line', {x1: blx, y1: bly, x2: brx, y2: bly, stroke: '#b9a17a', 'stroke-width': 3}, layers.floor);
        for (const [x0, x1] of [[18, 34], [62, 78]]) mk('polygon', {points: [[x0, 6], [x1, 6], [x1 + 8, 40], [x0 + 8, 40]].map(([x, z]) => P(x, 0, z)).join(' '), fill: '#fff8e6', opacity: .32}, layers.floor);
      } else if (view === 'stage') {
        mk('rect', {x: 0, y: 0, width: w, height: h, fill: '#1d1a24'}, layers.bg);
        mk('polygon', {points: f.quad(0, 0, 100, 60), fill: '#3a3340'}, layers.floor);
        for (const z of [20, 40]) { const a = f.project(0, 0, z), b = f.project(100, 0, z); mk('line', {x1: a[0], y1: a[1], x2: b[0], y2: b[1], stroke: '#ffffff', 'stroke-opacity': .12, 'stroke-dasharray': '6 6'}, layers.floor); }
        const [flx, fly] = f.project(0, 0, 60), [frx] = f.project(100, 0, 60);
        mk('rect', {x: flx, y: fly, width: frx - flx, height: Math.max(6, h * .02), fill: '#2a2430'}, layers.floor);
        const cl = '#7a1f2b';
        mk('rect', {x: 0, y: 0, width: w, height: h * .08, fill: cl}, f.deco);
        mk('rect', {x: 0, y: 0, width: Math.max(10, f.project(0, 0, 60)[0] + 8), height: fly, fill: cl}, f.deco);
        mk('rect', {x: Math.min(w - 10, frx - 8), y: 0, width: w, height: fly, fill: cl}, f.deco);
        f.mirror = null;
      } else if (view === 'square') {
        if (o.backdrop) mk('image', {href: o.backdrop, x: 0, y: 0, width: w, height: f.project(0, 0, 0)[1] + 4, preserveAspectRatio: 'xMidYMid slice'}, layers.bg);
        else {
          const g = mk('linearGradient', {id: id + 's', x1: 0, y1: 0, x2: 0, y2: 1}, defs);
          mk('stop', {offset: 0, 'stop-color': '#9fd3f0'}, g); mk('stop', {offset: 1, 'stop-color': '#e8f4ea'}, g);
          mk('rect', {x: 0, y: 0, width: w, height: h, fill: `url(#${id}s)`}, layers.bg);
          const by = f.project(0, 0, 0)[1];
          mk('path', {d: `M0 ${by} Q ${w * .25} ${by - h * .16} ${w * .5} ${by - h * .05} T ${w} ${by - h * .08} V ${by} Z`, fill: '#8fbf7a'}, layers.bg);
        }
        mk('polygon', {points: f.quad(0, 0, 100, 60), fill: '#c99a62'}, layers.floor);
        for (let x = 0; x <= 100; x += 10) { const a = f.project(x, 0, 0), b = f.project(x, 0, 60); mk('line', {x1: a[0], y1: a[1], x2: b[0], y2: b[1], stroke: '#a77a45', 'stroke-width': 1}, layers.floor); }
        const [flx, fly] = f.project(0, 0, 60), [frx] = f.project(100, 0, 60);
        mk('rect', {x: flx, y: fly, width: frx - flx, height: Math.max(8, h * .03), fill: '#8a5f33'}, layers.floor);
        f.mirror = null;
      } else {
        const g = mk('radialGradient', {id: id + 'v', cx: .5, cy: .55, r: .75}, defs);
        mk('stop', {offset: 0, 'stop-color': '#2b2f45'}, g); mk('stop', {offset: 1, 'stop-color': '#0d0f1a'}, g);
        mk('rect', {x: 0, y: 0, width: w, height: h, fill: `url(#${id}v)`}, layers.bg);
        for (let x = 0; x <= 100; x += 10) { const a = f.project(x, 0, 0), b = f.project(x, 0, 60); mk('line', {x1: a[0], y1: a[1], x2: b[0], y2: b[1], stroke: '#ffffff', 'stroke-opacity': .08}, layers.floor); }
        for (let z = 0; z <= 60; z += 10) { const a = f.project(0, 0, z), b = f.project(100, 0, z); mk('line', {x1: a[0], y1: a[1], x2: b[0], y2: b[1], stroke: '#ffffff', 'stroke-opacity': .08}, layers.floor); }
        f.mirror = null;
      }
    }
    // how high the back wall reaches, in floor units, at the top of the stage
    f.wallTop = () => (f.FH + f.hz * (60 + f.d0)) / f.F;
    f.resize(o.w || +svg.getAttribute('width') || 800, o.h || +svg.getAttribute('height') || 500, o.box);
    return f;
  }
  // a flat projector for icons: no perspective, a slight view from above
  function flat(k = 100, ox = 0, oy = 0) {
    return {project: (x, y, z) => [ox + x * k, oy - y * k + z * k * .12, 1000 - z], scale: () => k, map: (x, z) => ({x: ox + x * k, y: oy + z * k * .12, s: k})};
  }

  // ---------------------------------------------------------------- the dancer (Dance.dancer)
  const L = {ankle: .035, shin: .245, thigh: .245, foot: .085, trunk: .3, neck: .045, headRy: .074, headRx: .06,
    uarm: .165, farm: .175, hand: .028, sh: .09, hip: .058, waist: .07};
  const WID = {thigh: .085, shin: .066, uarm: .056, farm: .045, foot: .045};
  function shade(hex, k) {
    const n = parseInt(hex.slice(1), 16), c = [n >> 16, (n >> 8) & 255, n & 255].map(v => Math.round(v * (1 - k)));
    return '#' + c.map(v => v.toString(16).padStart(2, '0')).join('');
  }
  // rotations of a point [x, y, z] (degrees)
  const rx = (p, a) => [p[0], p[1] * cos(a) - p[2] * sin(a), p[1] * sin(a) + p[2] * cos(a)];   // about X: + tips forward
  const rz = (p, a) => [p[0] * cos(a) + p[1] * sin(a), -p[0] * sin(a) + p[1] * cos(a), p[2]];   // about Z: + leans to the left
  const ry = (p, a) => [p[0] * cos(a) + p[2] * sin(a), p[1], -p[0] * sin(a) + p[2] * cos(a)];   // about Y: + turns to the left
  const add = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]], mul = (a, k) => [a[0] * k, a[1] * k, a[2] * k];
  const armDir = (up, fwd, s) => [s * sin(up) * cos(fwd), -cos(up), sin(up) * sin(fwd)];
  const legDir = (fl, ab, s) => [s * sin(ab), -cos(fl) * cos(ab), sin(fl) * cos(ab)];
  function norm(v) { const n = Math.hypot(...v) || 1; return mul(v, 1 / n); }
  // the joints of a full pose, in body heights, grounded (the lowest support point on the floor)
  function skeleton(P) {
    const body = p => ry(rx(rz(p, P.roll), P.pitch), P.yaw || 0);
    const trunk = p => body(rx(rz(ry(p, P.twist), P.side), P.lean));
    const J = {pelvis: body([0, 0, 0])};
    J.chest = trunk([0, L.trunk, 0]);
    J.neck = trunk([0, L.trunk + L.neck, 0]);
    J.head = add(J.neck, trunk(rz(rx([0, L.headRy, .006], P.head), P.tilt)));
    J.fwd = trunk([0, 0, 1]); J.up = trunk([0, 1, 0]); J.hfwd = trunk(rz(rx([0, 0, 1], P.head), P.tilt)); J.hup = trunk(rz(rx([0, 1, 0], P.head), P.tilt));
    for (const [s, k] of [[1, 'l'], [-1, 'r']]) {
      const a = P[k + 'Arm'], g = P[k + 'Leg'], toe = P[k + 'Toe'];
      J[k + 'Sh'] = trunk([s * L.sh, L.trunk - .022, 0]);
      J[k + 'Wa'] = trunk([s * L.waist, .07, 0]);
      J[k + 'El'] = add(J[k + 'Sh'], trunk(mul(armDir(a[0], a[1], s), L.uarm)));
      J[k + 'Ha'] = add(J[k + 'El'], trunk(mul(armDir(a[2], a[3], s), L.farm)));
      J[k + 'Hi'] = body([s * L.hip, 0, 0]);
      J[k + 'Kn'] = add(J[k + 'Hi'], body(mul(legDir(g[0], g[1], s), L.thigh)));
      const shin = legDir(g[0] - g[2], g[1], s);
      J[k + 'An'] = add(J[k + 'Kn'], body(mul(shin, L.shin)));
      const flatFoot = norm([s * sin(g[1]) * .5, 0, 1]);
      const fd = norm(add(mul(flatFoot, 1 - toe * .78), mul(shin, toe * .78)));
      J[k + 'To'] = add(J[k + 'An'], body(mul(fd, L.foot)));
    }
    const sup = [['lAn', L.ankle], ['rAn', L.ankle], ['lTo', .016], ['rTo', .016], ['lKn', .036], ['rKn', .036], ['pelvis', .07],
      ['lHi', .06], ['rHi', .06], ['chest', .06], ['lSh', .05], ['rSh', .05], ['head', .075]];
    let low = Infinity; for (const [k, r] of sup) low = Math.min(low, J[k][1] - r);
    const dy = -low + (P.lift || 0);
    for (const k in J) if (!['fwd', 'up', 'hfwd', 'hup'].includes(k)) J[k] = [J[k][0], J[k][1] + dy, J[k][2]];
    return J;
  }
  const BADGES = {
    circle: r => `M ${-r} 0 a ${r} ${r} 0 1 0 ${2 * r} 0 a ${r} ${r} 0 1 0 ${-2 * r} 0 Z`,
    square: r => `M ${-r * .85} ${-r * .85} h ${r * 1.7} v ${r * 1.7} h ${-r * 1.7} Z`,
    triangle: r => `M 0 ${-r} L ${r * .95} ${r * .75} L ${-r * .95} ${r * .75} Z`,
    diamond: r => `M 0 ${-r * 1.1} L ${r} 0 L 0 ${r * 1.1} L ${-r} 0 Z`,
  };
  // a dancer from simple shapes, no face. o: {floor (or a projector from Dance.flat), top, bottom, skin, hair, shoe,
  // badge, scale, height (floor units), reflect (draw the image in the studio mirror), ghost (a faint copy)}
  function dancer(parent, o = {}) {
    const c = {top: '#00798c', bottom: '#33393d', skin: '#a8714f', hair: '#2b1d16', shoe: '#f2e6da', ...o};
    const ol = k => o[k + 'Line'] || shade(c[k], .38);
    const g = mk('g', {class: 'dz-dancer', 'aria-hidden': 'true'}, parent);
    if (o.ghost) g.setAttribute('opacity', o.ghost);
    const shadow = o.reflect || o.noShadow ? null : mk('ellipse', {fill: '#000', opacity: .13}, o.shadowLayer || (o.floor && o.floor.layers && o.floor.layers.shadow) || g);
    const parts = {};
    const limb = (name, color) => { const e = mk('g', {}, g); const a = mk('line', {stroke: ol(color), 'stroke-linecap': 'round'}, e), b = mk('line', {stroke: c[color], 'stroke-linecap': 'round'}, e); parts[name] = {e, a, b}; };
    for (const s of ['l', 'r']) { limb(s + 'Th', 'bottom'); limb(s + 'Sn', 'bottom'); limb(s + 'Ft', 'shoe'); limb(s + 'Ua', 'top'); limb(s + 'Fa', 'skin'); }
    const torso = mk('g', {}, g);
    parts.torso = {e: torso, top: mk('path', {fill: c.top, stroke: ol('top'), 'stroke-linejoin': 'round'}, torso),
      low: mk('path', {fill: c.bottom, stroke: ol('bottom'), 'stroke-linejoin': 'round'}, torso),
      badge: o.badge ? mk('path', {fill: '#fff', stroke: ol('top')}, torso) : null};
    const hd = mk('g', {}, g);
    parts.hair = {e: mk('g', {}, g)};
    parts.hairBack = mk('ellipse', {fill: c.hair, stroke: shade(c.hair, .3)}, parts.hair.e);
    parts.bun = mk('circle', {fill: c.hair, stroke: shade(c.hair, .3)}, parts.hair.e);
    parts.head = {e: hd, el: mk('ellipse', {fill: c.skin, stroke: ol('skin')}, hd)};
    parts.neck = mk('line', {stroke: c.skin, 'stroke-linecap': 'round'}, torso);
    const d = {g, parts, x: 50, z: 40, facing: 0, pose: pose('stand'), lift: 0, floor: o.floor, opts: o, joints: null, order: '',
      height: o.height || (o.floor && o.floor.dancerHeight) || 1, scale: o.scale || 1, listeners: [],
      set(s) {
        if (s.pose) d.pose = s.pose.lArm ? s.pose : pose(s.pose);
        if (s.x != null) d.x = s.x; if (s.z != null) d.z = s.z; if (s.facing != null) d.facing = s.facing;
        if (s.lift != null) d.lift = s.lift;
        d.render(); d.listeners.forEach(fn => fn(d));
        return d;
      },
      onMove(fn) { d.listeners.push(fn); },
      // the screen point of a joint and the floor-unit world point (for trails)
      world(k) { return d.wj && d.wj[k]; },
      render() {
        const f = d.floor, P = d.pose, U = (o.height || (f && f.dancerHeight) || 1) * d.scale;
        d.height = U;
        const J = skeleton(d.lift ? {...P, lift: (P.lift || 0) + d.lift} : P); d.joints = J;
        const th = d.facing, W = {}, S = {};
        // reflect: true, or a number that pulls the image toward the mirror (1 is true depth; less keeps a big dancer's
        // image inside a short mirror strip)
        const refl = !!o.reflect, rk = typeof o.reflect === 'number' ? o.reflect : 1;
        for (const k in J) {
          if (['fwd', 'up', 'hfwd', 'hup'].includes(k)) continue;
          const [X, Y, Z] = J[k];
          const wx = d.x + (X * cos(th) + Z * sin(th)) * U, wz = d.z + (Z * cos(th) - X * sin(th)) * U, wy = Y * U;
          W[k] = [wx, wy, wz];
          S[k] = f.project(wx, wy, refl ? -d.z * rk - (wz - d.z) : wz);
        }
        d.wj = W; d.sj = S;
        const k = f.scale(refl ? -d.z * rk : d.z) * U;   // pixels per body height
        const lw = Math.max(1.2, Math.min(2.4, k * .012)) * (o.lineScale || 1);
        const dir = v => { const [X, , Z] = v; const wz = Z * cos(th) - X * sin(th); return refl ? -wz : wz; };
        const items = [];
        const put = (name, a, b, w) => {
          const p = parts[name], A = S[a], B = S[b];
          for (const [ln, ww] of [[p.a, w * k + lw * 2], [p.b, w * k]]) { ln.setAttribute('x1', A[0].toFixed(1)); ln.setAttribute('y1', A[1].toFixed(1)); ln.setAttribute('x2', B[0].toFixed(1)); ln.setAttribute('y2', B[1].toFixed(1)); ln.setAttribute('stroke-width', ww.toFixed(1)); }
          items.push([p.e, (A[2] + B[2]) / 2, name]);
        };
        for (const s of ['l', 'r']) {
          put(s + 'Th', s + 'Hi', s + 'Kn', WID.thigh); put(s + 'Sn', s + 'Kn', s + 'An', WID.shin); put(s + 'Ft', s + 'An', s + 'To', WID.foot);
          put(s + 'Ua', s + 'Sh', s + 'El', WID.uarm); put(s + 'Fa', s + 'El', s + 'Ha', WID.farm);
        }
        // the hand and foot ends sit a little in front of their own limb so they never vanish behind it
        const pt = a => S[a][0].toFixed(1) + ' ' + S[a][1].toFixed(1);
        const tp = parts.torso;
        tp.top.setAttribute('d', `M ${pt('lSh')} L ${pt('rSh')} L ${pt('rWa')} L ${pt('lWa')} Z`);
        tp.low.setAttribute('d', `M ${pt('lWa')} L ${pt('rWa')} L ${pt('rHi')} L ${pt('lHi')} Z`);
        tp.top.setAttribute('stroke-width', (lw * 2 + .05 * k).toFixed(1)); tp.low.setAttribute('stroke-width', (lw * 2 + .05 * k).toFixed(1));
        // the outline of the torso is drawn as a fat stroke in the darker color under the fill: emulate by paint order
        tp.top.style.paintOrder = 'stroke'; tp.low.style.paintOrder = 'stroke';
        parts.neck.setAttribute('x1', S.chest[0]); parts.neck.setAttribute('y1', S.chest[1]); parts.neck.setAttribute('x2', S.neck[0]); parts.neck.setAttribute('y2', S.neck[1]);
        parts.neck.setAttribute('stroke-width', (.05 * k).toFixed(1));
        const fwdDepth = dir(J.fwd);
        if (tp.badge) {
          const cx = (S.lSh[0] + S.rSh[0] + S.lWa[0] + S.rWa[0]) / 4, cy = (S.lSh[1] + S.rSh[1] + S.lWa[1] * 1.6 + S.rWa[1] * 1.6) / 5.2;
          tp.badge.setAttribute('d', BADGES[o.badge](.032 * k)); tp.badge.setAttribute('transform', `translate(${cx.toFixed(1)} ${cy.toFixed(1)})`);
          tp.badge.setAttribute('stroke-width', lw); tp.badge.style.display = fwdDepth > -.2 ? '' : 'none';
        }
        const torsoDepth = (S.chest[2] + S.pelvis[2]) / 2 - fwdDepth * .001;
        items.push([tp.e, torsoDepth, 'torso']);
        // head: the face side is plain skin; hair is an oval set toward the back of the head, plus a bun
        const H = S.head, hr = L.headRx * k, hry = L.headRy * k;
        const he = parts.head.el;
        he.setAttribute('cx', H[0].toFixed(1)); he.setAttribute('cy', H[1].toFixed(1)); he.setAttribute('rx', hr.toFixed(1)); he.setAttribute('ry', hry.toFixed(1)); he.setAttribute('stroke-width', lw);
        const hupS = [(J.hup[0] * cos(th) + J.hup[2] * sin(th)), -J.hup[1]];
        he.setAttribute('transform', `rotate(${(Math.atan2(hupS[0], -hupS[1]) / RAD).toFixed(1)} ${H[0].toFixed(1)} ${H[1].toFixed(1)})`);
        const hf = J.hfwd, hfS = [(hf[0] * cos(th) + hf[2] * sin(th)), -hf[1]], hfD = dir(hf);
        const back = [H[0] - hfS[0] * hr * .32 + hupS[0] * hry * .1, H[1] - hfS[1] * hry * .32 - hry * .12 * (1 - Math.abs(hupS[0]))];
        const hb = parts.hairBack;
        hb.setAttribute('cx', back[0].toFixed(1)); hb.setAttribute('cy', back[1].toFixed(1)); hb.setAttribute('rx', (hr * 1.04).toFixed(1)); hb.setAttribute('ry', (hry * .98).toFixed(1)); hb.setAttribute('stroke-width', lw);
        hb.setAttribute('transform', he.getAttribute('transform'));
        const bun = [H[0] - hfS[0] * hr * 1.0 + hupS[0] * hry * .55, H[1] - hfS[1] * hry * .9 - hry * .55 * (-hupS[1])];
        parts.bun.setAttribute('cx', bun[0].toFixed(1)); parts.bun.setAttribute('cy', bun[1].toFixed(1)); parts.bun.setAttribute('r', (hr * .5).toFixed(1)); parts.bun.setAttribute('stroke-width', lw);
        // face toward the viewer: hair behind the head; face away: hair over it
        items.push([parts.hair.e, H[2] + (hfD >= 0 ? .02 : -.02) * U, 'hair']);
        items.push([parts.head.e, H[2], 'head']);
        // far things first (larger distance from the camera)
        items.sort((a, b) => b[1] - a[1]);
        const order = items.map(i => i[2]).join();
        if (order !== d.order) { d.order = order; for (const [e] of items) g.appendChild(e); }
        if (shadow) {
          const m = f.map(d.x, d.z), r = .2 * U * m.s;
          shadow.setAttribute('cx', m.x.toFixed(1)); shadow.setAttribute('cy', m.y.toFixed(1)); shadow.setAttribute('rx', r.toFixed(1));
          shadow.setAttribute('ry', (r * Math.max(.18, (f.map(d.x, d.z + 1).y - m.y) / m.s)).toFixed(1));
          shadow.setAttribute('opacity', (.14 / (1 + (d.lift + (P.lift || 0)) * 6)).toFixed(3));
        }
      },
      remove() { g.remove(); if (shadow) shadow.remove(); },
    };
    if (d.floor) d.render();
    return d;
  }
  // a still figure drawn into its own small svg (for buttons and cards), fitted to the box
  function icon(svg, p, o = {}) {
    svg.textContent = '';
    const pr = flat(100, 0, 0), dn = dancer(svg, {...o, floor: pr, height: 1, noShadow: true, lineScale: o.lineScale || 1.4});
    dn.set({pose: p, x: 0, z: 0, facing: o.facing != null ? o.facing : 18});
    let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
    for (const k in dn.sj) { const [x, y] = dn.sj[k]; x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
    const pad = 12, w = x1 - x0 + 2 * pad, h = y1 - y0 + 2 * pad, s = Math.max(w, h * (o.aspect || 1));
    svg.setAttribute('viewBox', `${((x0 + x1) / 2 - s / 2).toFixed(1)} ${((y0 + y1) / 2 - s / (o.aspect || 1) / 2).toFixed(1)} ${s.toFixed(1)} ${(s / (o.aspect || 1)).toFixed(1)}`);
    return dn;
  }

  // ---------------------------------------------------------------- phrases (Dance.phrase)
  // steps: [{poses, counts, level, dyn, side, facing, travel, gait, at}]
  //   poses: keyframes (names or poses), one per count, looping (two poses: A to B on count 1, B to A on count 2)
  //   level: 'high' | 'middle' | 'low', or a function (absolute count index from 0) => level, read per count
  //   dyn: a key of Dance.dyn; side: 'L' mirrors; facing: degrees (0 faces the front), 'travel' or 'front'
  //   travel: a path (Dance.path) covered during the step; gait: a key of Dance.gaits (its cycle replaces poses)
  //   at: {x, z} where a step without travel stands (default: where the last step ended)
  function phrase(steps) {
    let t = 0;
    const S = steps.map(s => { const o = {counts: 8, dyn: 'smooth', ...s, from: t}; t += o.counts; return o; });
    const lvAt = (s, j) => typeof s.level === 'function' ? s.level(j) : s.level || 'middle';
    function at(c) {
      c = clamp(c, 0, t - 1e-6);
      let i = 0; while (i < S.length - 1 && c >= S[i].from + S[i].counts) i++;
      const s = S[i], lc = c - s.from, j = Math.floor(lc), u = lc - j, abs = s.from + j;
      let P, lift = 0, x = null, z = null, facing = typeof s.facing === 'number' ? s.facing : null;
      const dy = dyn[s.dyn] || dyn.smooth;
      if (s.gait) {
        const G = gaits[s.gait], q = (lc / G.counts) % 1;
        let dir = 1;
        if (s.travel) {
          const p = s.travel.at(lc / s.counts); x = p.x; z = p.z;
          const face = s.facing === 'front' || (s.facing == null && G.facing === 'front');
          if (face) { facing = 0; dir = p.dx >= 0 ? 1 : -1; } else if (facing == null) facing = Math.atan2(p.dx, p.dz) / RAD;
        }
        const r = G.pose(q, dir), lvl = lvAt(s, abs);
        P = level(r.pose, lvl); lift = r.lift * (lvl === 'high' ? 1.6 : lvl === 'low' ? .5 : 1);
      } else {
        const kf = (s.poses || ['stand']).map(p => typeof p === 'string' || !p.lArm ? p : p);
        const m = kf.length, l0 = j > 0 ? lvAt(s, abs - 1) : lvAt(s, abs), l1 = lvAt(s, abs);
        const A = level(kf[j % m], l0), B = level(kf[m > 1 ? (j + 1) % m : 0], l1);
        P = mix(A, B, m > 1 || l0 !== l1 ? dy.ease(u) : 0);
        if (dy.jitter) { const a = dy.jitter * Math.sin(c * Math.PI * 2 * 5); for (const k of ['lArm', 'rArm']) { P[k][0] += a; P[k][2] += a * 1.4; } P.side += a * .4; }
        if (dy.dip) P.lLeg[2] += 18 * Math.sin(Math.PI * u), P.rLeg[2] += 18 * Math.sin(Math.PI * u);
        if (s.travel) { const p = s.travel.at(lc / s.counts); x = p.x; z = p.z; if (facing == null && s.facing === 'travel') facing = Math.atan2(p.dx, p.dz) / RAD; }
        else if (s.at) { x = s.at.x; z = s.at.z; }
        if (s.facing === 'front') facing = 0;
      }
      if (s.side === 'L') P = mirror(P);
      return {pose: P, lift, x, z, facing, step: i, count: lc};
    }
    return {steps: S, total: t, at};
  }

  // ---------------------------------------------------------------- the count clock (Dance.clock)
  // pos: the count position. The count-in runs from -countIn to 0; count n (1, 2, ...) runs from n - 1 to n.
  // onCount(n): n 1, 2, ... for counts, and n <= 0 for the count-in (its beat is n + countIn, 1 to countIn).
  // A tempo change (setBpm) takes effect on the next count. stop() ends it for good (its token goes stale).
  const clocks = new Set();
  let ticking = false, tokenN = 0;
  function tickAll() { const t = performance.now(); for (const c of [...clocks]) c._tick(t); }
  function loop() { tickAll(); if (clocks.size) requestAnimationFrame(loop); else ticking = false; }
  setInterval(() => { if (clocks.size) tickAll(); }, 50);   // when frames stall (a hidden tab), counts still come
  function clock(bpm, o = {}) {
    const countIn = o.countIn == null ? 4 : o.countIn;
    let pos0 = -countIn, t0 = 0, last = null, pending = null, running = false, paused = false;
    const countFns = [], frameFns = [];
    const c = {bpm, meter: o.meter || 4, countIn, token: ++tokenN, stopped: false,
      get pos() { return running && !paused ? pos0 + (performance.now() - t0) * c.bpm / 60000 : pos0; },
      get running() { return running && !paused; }, get paused() { return paused; },
      get countMs() { return 60000 / c.bpm; },
      onCount(fn) { countFns.push(fn); return () => countFns.splice(countFns.indexOf(fn), 1); },
      onFrame(fn) { frameFns.push(fn); return () => { const i = frameFns.indexOf(fn); if (i >= 0) frameFns.splice(i, 1); }; },
      start(from = -countIn) {
        if (c.stopped) return c;
        pos0 = from; t0 = performance.now(); running = true; paused = false; last = Math.ceil(from) - 1;
        clocks.add(c); if (!ticking) { ticking = true; requestAnimationFrame(loop); }
        c._tick(t0); return c;
      },
      pause() { if (!running || paused) return; pos0 = c.pos; paused = true; },
      resume() { if (!running || !paused || c.stopped) return; t0 = performance.now(); paused = false; },
      seek(p) { pos0 = p; t0 = performance.now(); last = Math.ceil(p) - 1; if (running) c._tick(t0); },
      setBpm(b) { if (running && !paused) pending = b; else c.bpm = b; },
      stop() { running = false; c.stopped = true; c.token = -1; clocks.delete(c); countFns.length = 0; frameFns.length = 0; },
      _tick(t) {
        if (!running || paused || c.stopped) return;
        let p = c.pos;
        while (last < Math.floor(p)) {
          last++;
          if (pending) {   // the new tempo starts exactly on this count
            const tl = t0 + (last - pos0) * 60000 / c.bpm;
            c.bpm = pending; pending = null; pos0 = last; t0 = tl; p = c.pos;
          }
          const n = last + 1, tok = c.token;
          for (const fn of [...countFns]) { if (c.token !== tok) return; fn(n, {beat: n <= 0 ? n + countIn : ((n - 1) % c.meter) + 1, countIn: n <= 0}); }
        }
        const tok = c.token;
        for (const fn of [...frameFns]) { if (c.token !== tok) return; fn(c.pos); }
      },
    };
    return c;
  }

  // ---------------------------------------------------------------- the sequencer (Dance.play)
  // dancers and phrases (one phrase for all, or one each); offsets delay each dancer by counts (canon); trails get a
  // point every frame. Motion off: the pose and the position jump once per count, with no in-between.
  // Returns {done: Promise ('end' or 'stop'), stop()}.
  function play(dancers, phrases, o = {}) {
    dancers = [].concat(dancers); phrases = [].concat(phrases);
    const clk = o.clock, offs = o.offsets || [], trails = [].concat(o.trails || []);
    const ph = i => phrases[i] || phrases[0];
    const total = Math.max(...dancers.map((_, i) => ph(i).total + (offs[i] || 0)));
    let fin, ended = false;
    const done = new Promise(r => { fin = r; });
    function frame(pos) {
      if (ended) return;
      dancers.forEach((d, i) => {
        let c = pos - (offs[i] || 0);
        const P = ph(i);
        if (o.loop) c = ((c % P.total) + P.total) % P.total;
        if (calm() && c > 0) c = Math.min(Math.floor(c) + .999, P.total - 1e-6);
        const st = P.at(Math.max(0, c));
        if (c < 0) st.lift = 0;
        d.set(st);
        if (trails[i] && c >= 0) {
          // Motion off jumps a count at a time: start the record where the step starts, not one count along it
          if (!trails[i].points.length && c > 0) { const s0 = P.at(0); if (s0.x != null) trails[i].points.push({x: s0.x, z: s0.z, c: 0, s: trails[i].styleOf(0)}); }
          trails[i].capture(c);
        }
      });
      if (o.onFrame) o.onFrame(pos);
      if (!o.loop && pos >= total) end('end');
    }
    function end(why) { if (ended) return; ended = true; off(); fin(why); if (why === 'end' && o.onEnd) o.onEnd(); }
    const off = clk.onFrame(frame);
    frame(clk.pos);
    return {done, stop: () => end('stop'), get total() { return total; }};
  }
  // ease a dancer into a pose (and facing) over ms; resolves false if the token went stale. Motion off: a jump.
  function tween(d, to, ms = 400, isLive = () => true) {
    const from = d.pose, P = to.pose ? (to.pose.lArm ? to.pose : pose(to.pose)) : from, f0 = d.facing;
    let f1 = to.facing != null ? to.facing : f0; while (f1 - f0 > 180) f1 -= 360; while (f1 - f0 < -180) f1 += 360;
    if (calm() || ms <= 0) { d.set({pose: P, facing: f1, x: to.x, z: to.z, lift: 0}); return Promise.resolve(true); }
    const t0 = performance.now(), x0 = d.x, z0 = d.z;
    return new Promise(res => {
      const step = () => {
        if (!isLive()) return res(false);
        const u = Math.min(1, (performance.now() - t0) / ms), e = (1 - Math.cos(Math.PI * u)) / 2;
        d.set({pose: mix(from, P, e), facing: lerp(f0, f1, e), x: to.x != null ? lerp(x0, to.x, e) : null, z: to.z != null ? lerp(z0, to.z, e) : null, lift: 0});
        if (u < 1) requestAnimationFrame(step); else res(true);
      };
      requestAnimationFrame(step);
    });
  }

  // ---------------------------------------------------------------- trails (Dance.trail)
  // 'ribbon': a floor ribbon under the feet, styled by level; 'exposure': ghost copies every half count plus the
  // traced paths of the hands and feet; 'off'. trail.points keeps the record (floor units) either way.
  const ribbonStyles = {
    high: {color: '#1565c0', kind: 'prints', width: 3.2},
    middle: {color: '#2e7d32', kind: 'band', width: 4.2},
    low: {color: '#b45309', kind: 'stripes', width: 7, stripe: '#f6cf8f'},
    plain: {color: '#c08a00', kind: 'magic', width: 4.6},
  };
  function trail(d, o = {}) {
    const f = d.floor;
    const g = mk('g', {class: 'dz-trail'}, o.layer || f.layers.trail);
    const t = {mode: o.mode || 'ribbon', style: o.style || 'middle', points: [], ghosts: [], hidden: !!o.hidden, g, opacity: 1, xf: null, badge: null,
      endDraw: null, lastHalf: -1,
      // o.styleAt(count): a style per point (a pathway that changes level part by part); else t.style for all
      styleOf: c => o.styleAt ? o.styleAt(c) : undefined,
      capture(c) {
        const x = d.x, z = d.z, P = t.points[t.points.length - 1], s = t.styleOf(c);
        if (!P || Math.hypot(x - P.x, z - P.z) > .5 || s !== P.s) { t.points.push({x, z, c, s}); if (!t.hidden) t.render(); }
        if (t.mode === 'exposure') {
          const h = Math.floor(c * 2);
          if (h !== t.lastHalf && t.ghosts.length < 64) { t.lastHalf = h; t.ghosts.push({pose: d.pose, x: d.x, z: d.z, facing: d.facing, lift: d.lift, hands: ['lHa', 'rHa', 'lTo', 'rTo'].map(k => d.world(k).slice())}); if (!t.hidden) t.render(); }
        }
      },
      add(x, z) { t.points.push({x, z}); if (!t.hidden) t.render(); },
      setPoints(pts) { t.points = pts.map(p => ({x: p.x, z: p.z, s: p.s})); t.render(); },
      // one style for the whole record (it replaces any per-point styles)
      setStyle(s) { t.style = s; t.points.forEach(p => { p.s = undefined; }); t.render(); },
      show(v = true) { t.hidden = !v; t.render(); },
      // xf: draw the record moved and scaled on the floor (a gallery): {ox, oz, s} maps (x, z) to (ox + x*s, oz + z*s)
      transform(xf) { t.xf = xf; t.render(); },
      end(fn) { t.endDraw = fn; t.render(); },
      fade(to, ms = 500) {
        t.opacity = to;
        g.style.transition = calm() ? 'none' : `opacity ${ms}ms`; g.setAttribute('opacity', to);
        return new Promise(r => setTimeout(r, calm() ? 0 : ms));
      },
      // paint the whole record in along its length over ms (Motion off: it appears at once, after the same time)
      paintIn(ms = 1500, isLive = () => true) {
        const all = t.points.slice(); t.hidden = false;
        if (calm()) { t.points = all; t.render(); return new Promise(r => setTimeout(() => r(isLive()), ms)); }
        const t0 = performance.now();
        return new Promise(res => {
          const step = () => {
            if (!isLive()) { t.points = all; t.render(); return res(false); }
            const u = Math.min(1, (performance.now() - t0) / ms);
            t.points = all.slice(0, Math.max(2, Math.ceil(all.length * u))); t.render();
            if (u < 1) requestAnimationFrame(step); else res(true);
          };
          step();
        });
      },
      clear() { t.points = []; t.ghosts = []; t.lastHalf = -1; t.render(); },
      remove() { g.remove(); },
      render() {
        g.textContent = '';
        if (t.hidden || t.mode === 'off') return;
        const xf = t.xf, F = p => xf ? {x: xf.ox + p.x * xf.s, z: xf.oz + p.z * xf.s} : p, ws = xf ? xf.s : 1;
        const pts = t.points.map(F);
        if (t.mode === 'exposure') return renderExposure(pts);
        if (pts.length < 2) return;
        // runs of points that share a style, each drawn in its own style (they overlap by one point)
        const runs = [];
        t.points.forEach((p, i) => { const k = p.s || t.style, r = runs[runs.length - 1]; if (r && r.k === k) r.pts.push(pts[i]); else { if (r) r.pts.push(pts[i]); runs.push({k, pts: r ? [pts[i - 1], pts[i]] : [pts[i]]}); } });
        for (const r of runs) if (r.pts.length > 1) drawRun(r.pts, typeof r.k === 'string' ? ribbonStyles[r.k] : r.k);
        if (t.endDraw && pts.length > 1) { const e = pts[pts.length - 1], p = f.project(e.x, 0, e.z); const eg = mk('g', {class: 'dz-end'}, g); t.endDraw(eg, p[0], p[1], f.scale(e.z) * ws); }
      },
    };
    function drawRun(pts, st) {
        const ws = t.xf ? t.xf.s : 1;
        const W = st.width * ws;
        const side = (k) => pts.map((p, i) => {
          const a = pts[Math.max(0, i - 1)], b = pts[Math.min(pts.length - 1, i + 1)];
          let dx = b.x - a.x, dz = b.z - a.z; const n = Math.hypot(dx, dz) || 1; dx /= n; dz /= n;
          return f.project(p.x - dz * k, 0, p.z + dx * k);
        });
        const band = (w, attrs) => {
          const A = side(w / 2), B = side(-w / 2).reverse();
          return mk('path', {d: 'M' + A.concat(B).map(p => p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' L') + ' Z', 'stroke-linejoin': 'round', ...attrs}, g);
        };
        const line = (attrs) => mk('polyline', {points: pts.map(p => f.project(p.x, 0, p.z).slice(0, 2).map(v => v.toFixed(1)).join(',')).join(' '), fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round', ...attrs}, g);
        const sc = f.scale(30);
        if (st.kind === 'band') band(W, {fill: st.color, stroke: shade(st.color, .3), 'stroke-width': 1.5, opacity: .92});
        else if (st.kind === 'stripes') {
          const pid = f.uid + 'st' + (st.color + st.stripe).replace(/#/g, '');
          if (!document.getElementById(pid)) {
            const defs = f.svg.querySelector('defs') || mk('defs', {}, f.svg);
            const pat = mk('pattern', {id: pid, width: 14, height: 14, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(40)'}, defs);
            mk('rect', {width: 14, height: 14, fill: st.color}, pat); mk('rect', {width: 5, height: 14, fill: st.stripe}, pat);
          }
          band(W, {fill: `url(#${pid})`, stroke: shade(st.color, .3), 'stroke-width': 2, opacity: .95});
        } else if (st.kind === 'prints') {
          line({stroke: st.color, 'stroke-width': Math.max(ws < 1 ? 2.6 : 1.5, .35 * sc * ws), opacity: .9});
          // tiptoe prints: small rounded prints, left and right of the line in turn, every 3.2 floor units. Scaled
          // down (a gallery), the prints keep a readable size and spread out instead of shrinking to dots
          const pk = ws < 1 ? Math.min(1 / ws, 2.4) : 1, gap = 3.2 * ws * pk;
          let acc = 0, n = 0;
          for (let i = 1; i < pts.length; i++) {
            const a = pts[i - 1], b = pts[i], l = Math.hypot(b.x - a.x, b.z - a.z); acc += l;
            while (acc >= gap) {
              acc -= gap; n++;
              const u = 1 - acc / (l || 1), x = lerp(a.x, b.x, u), z = lerp(a.z, b.z, u), dx = (b.x - a.x) / (l || 1), dz = (b.z - a.z) / (l || 1), off = (n % 2 ? 1.1 : -1.1) * ws * pk;
              const c0 = f.project(x - dz * off, 0, z + dx * off), c1 = f.project(x - dz * off + dx, 0, z + dx * off + dz);
              const ang = Math.atan2(c1[1] - c0[1], c1[0] - c0[0]) / RAD, s = f.scale(z) * ws * pk;
              mk('ellipse', {cx: c0[0].toFixed(1), cy: c0[1].toFixed(1), rx: (1.05 * s).toFixed(1), ry: (.62 * s * Math.max(.45, Math.abs(Math.sin(ang * RAD)) * .4 + .6)).toFixed(1), fill: st.color, stroke: '#fff', 'stroke-width': 1, transform: `rotate(${ang.toFixed(0)} ${c0[0].toFixed(1)} ${c0[1].toFixed(1)})`}, g);
            }
          }
        } else if (st.kind === 'magic') {
          band(W, {fill: '#fff6d6', stroke: st.color, 'stroke-width': 2.5, 'stroke-dasharray': '7 5', opacity: .95});
          line({stroke: st.color, 'stroke-width': 2, 'stroke-dasharray': '1 9', opacity: .9});
        }
    }
    function renderExposure(pts) {
      const fs = f.scale(30);
      if (pts.length > 1) mk('polyline', {points: pts.map(p => f.project(p.x, 0, p.z).slice(0, 2).join(',')).join(' '), fill: 'none', stroke: o.color || '#00798c', 'stroke-width': Math.max(1.5, .25 * fs), opacity: .5, 'stroke-dasharray': '4 4'}, g);
      t.ghosts.forEach((s, i) => {
        if (i % 1) return;
        const gd = dancer(g, {...(o.ghostColors || {}), floor: f, ghost: .22, noShadow: true});
        gd.set(s);
      });
      for (let k = 0; k < 4; k++) {
        const pts3 = t.ghosts.map(s => s.hands[k]);
        if (pts3.length > 1) mk('polyline', {points: pts3.map(p => f.project(p[0], p[1], p[2]).slice(0, 2).map(v => v.toFixed(1)).join(',')).join(' '), fill: 'none', stroke: k < 2 ? (o.handColor || '#c2185b') : (o.footColor || '#1565c0'), 'stroke-width': 2, opacity: .7}, g);
      }
    }
    f.onResize(() => t.render());
    return t;
  }

  // ---------------------------------------------------------------- music (Dance.music)
  // A track: {len: counts per loop, sub: steps per count (2 or 4), swing: 0 to .34 (delays the off-beat eighth),
  // vol, parts: {inst: pattern}}. A pattern is a string of 'x' (hit), 'X' (accent) and '.' per step, or a list per
  // step of null, a MIDI note, or a list of notes (a chord). Instruments: kick, snare, hat, clap, shaker, wood, bass,
  // piano, pluck, pad, tap, stamp, click. The count-in plays clicks (accent on beat 1) unless track.countIn is false.
  // Silent with Sound off and before the first tap. stop() silences at once.
  let noiseBuf = null;
  const ctxOf = () => (typeof Curio !== 'undefined' && Curio.audio) ? Curio.audio() : null;
  const musics = new Set();
  if (typeof Curio !== 'undefined' && Curio.onSound) Curio.onSound(s => { for (const m of musics) m.mute(!s); });
  const mtof = m => 440 * Math.pow(2, (m - 69) / 12);
  function voiceAt(a, out, inst, t, note, vel, dur) {
    const g = a.createGain(); g.connect(out);
    const env = (peak, att, dec) => { g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(peak * vel, t + att); g.gain.exponentialRampToValueAtTime(.0001, t + att + dec); };
    const osc = (type, f, t1 = t + dur + .4) => { const o = a.createOscillator(); o.type = type; o.frequency.setValueAtTime(f, t); o.connect(g); o.start(t); o.stop(t1); return o; };
    const noise = (len, filt, fq, q = 1) => {
      if (!noiseBuf) { noiseBuf = a.createBuffer(1, a.sampleRate, a.sampleRate); const d = noiseBuf.getChannelData(0); for (let i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1; }
      const s = a.createBufferSource(); s.buffer = noiseBuf; const bq = a.createBiquadFilter(); bq.type = filt; bq.frequency.value = fq; bq.Q.value = q;
      s.connect(bq).connect(g); s.start(t, Math.random() * .5); s.stop(t + len);
    };
    switch (inst) {
      case 'kick': { env(.9, .004, .28); const o = osc('sine', 140, t + .35); o.frequency.exponentialRampToValueAtTime(45, t + .18); break; }
      case 'snare': env(.4, .002, .16); noise(.2, 'bandpass', 1800, .8); osc('triangle', 190, t + .1); break;
      case 'hat': env(.18, .001, .04); noise(.06, 'highpass', 7500); break;
      case 'clap': for (const k of [0, .012, .026]) { const h = a.createGain(); h.connect(out); h.gain.setValueAtTime(.0001, t + k); h.gain.exponentialRampToValueAtTime(.35 * vel, t + k + .002); h.gain.exponentialRampToValueAtTime(.0001, t + k + .08); const s = a.createBufferSource(); if (!noiseBuf) noise(.01, 'bandpass', 1200); s.buffer = noiseBuf; const bq = a.createBiquadFilter(); bq.type = 'bandpass'; bq.frequency.value = 1300; s.connect(bq).connect(h); s.start(t + k, Math.random() * .5); s.stop(t + k + .1); } break;
      case 'shaker': env(.12, .012, .06); noise(.09, 'bandpass', 6200, 1.2); break;
      case 'wood': env(.5, .001, .07); osc('sine', note ? mtof(note) : 1250, t + .1); break;
      case 'click': env(.55, .001, .05); osc('square', note ? mtof(note) : 1500, t + .07); break;
      case 'tap': env(.3, .001, .05); noise(.06, 'lowpass', 2400); break;
      case 'stamp': env(.8, .002, .18); osc('sine', 90, t + .2).frequency.exponentialRampToValueAtTime(40, t + .15); noise(.08, 'lowpass', 600); break;
      case 'bass': { env(.45, .01, Math.max(.2, dur)); const o = osc('triangle', mtof(note)); const lp = a.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 600; o.disconnect(); o.connect(lp).connect(g); break; }
      case 'piano': env(.16, .005, Math.max(.5, dur * 1.6)); osc('triangle', mtof(note)); osc('sine', mtof(note) * 2).detune.value = 3; break;
      case 'pluck': { env(.18, .003, .25); const o = osc('sawtooth', mtof(note)); const lp = a.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.setValueAtTime(2400, t); lp.frequency.exponentialRampToValueAtTime(300, t + .25); o.disconnect(); o.connect(lp).connect(g); break; }
      case 'pad': { g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(.07 * vel, t + .25); g.gain.setValueAtTime(.07 * vel, t + dur); g.gain.exponentialRampToValueAtTime(.0001, t + dur + .4); osc('triangle', mtof(note)); osc('sine', mtof(note) * 1.003); break; }
    }
  }
  function music(track, clk) {
    let out = null, muted = false, offCount = null;
    const vol = track.vol || .7;
    const m = {track, clock: null,
      attach(c) { if (offCount) offCount(); m.clock = c; offCount = c ? c.onCount(n => m.count(n)) : null; return m; },
      mute(v) { muted = v; if (out) { const a = out.context; out.gain.cancelScheduledValues(a.currentTime); out.gain.setValueAtTime(v ? 0 : vol, a.currentTime); } },
      count(n) {
        if (!heard || !soundOn() || muted || !m.clock) return;
        const a = ctxOf(); if (!a) return;
        if (a.state === 'suspended') a.resume();
        if (!out) { out = a.createGain(); out.gain.value = vol; out.connect(a.destination); musics.add(m); }
        const dur = 60 / m.clock.bpm, t = a.currentTime + .02;
        if (n <= 0) { if (track.countIn !== false) voiceAt(a, out, 'click', t, n + m.clock.countIn === 1 ? 96 : 88, 1, .05); return; }
        const sub = track.sub || 2, idx = (n - 1) % (track.len || 8);
        for (let s = 0; s < sub; s++) {
          let off = s / sub; if (sub === 2 && s === 1 && track.swing) off += track.swing / 2; if (sub === 4 && s % 2 && track.swing) off += track.swing / 4;
          const at = t + off * dur;
          for (const inst in track.parts) {
            const p = track.parts[inst], ev = p[idx * sub + s];
            if (ev == null || ev === '.' || ev === ' ') continue;
            if (typeof ev === 'string') voiceAt(a, out, inst, at, null, ev === 'X' ? 1 : .7, dur / sub);
            else for (const nt of [].concat(ev)) voiceAt(a, out, inst, at, nt, 1, inst === 'pad' ? dur * 2 : dur / sub * 1.6);
          }
        }
      },
      stop() {
        if (offCount) { offCount(); offCount = null; }
        if (out) { const a = out.context; try { out.gain.cancelScheduledValues(a.currentTime); out.gain.setValueAtTime(0, a.currentTime); } catch {} const o2 = out; setTimeout(() => o2.disconnect(), 80); out = null; }
        musics.delete(m); m.clock = null;
      },
    };
    if (clk) m.attach(clk);
    return m;
  }

  // ---------------------------------------------------------------- the count strip (Dance.counts)
  // dots (or numbers) in an svg group: the current count lit, count-in beats in their own style, and the phrase
  // number as small pips at the end. o: {n: 8, mode: 'dots' | 'numbers', phrases: how many 8-count phrases}
  function counts(parent, clk, o = {}) {
    const n = o.n || 8, g = mk('g', {class: 'dz-counts', 'aria-hidden': 'true'}, parent);
    const st = {n, mode: o.mode || 'dots', cur: 0, kind: 'off', phrases: o.phrases || 1, phrase: 0, box: {x: 0, y: 0, w: 300, h: 30}};
    let off = null;
    const C = {g, st,
      bind(c, phrases) { if (off) off(); if (c) clk = c; st.phrases = phrases || st.phrases; off = c ? c.onCount(k => C.set(k)) : null; return C; },
      layout(box) { st.box = box; C.draw(); },
      // set(k): k 1.. lights count ((k-1) mod n)+1; k <= 0 a count-in beat; 0 / null: all dark
      set(k, kind) {
        if (k == null || k === false) { st.kind = 'off'; st.cur = 0; }
        else if (k <= 0 && kind !== 'count') { st.kind = 'in'; st.cur = k + (clk ? clk.countIn : 4); st.phrase = 0; }
        else { st.kind = kind || 'count'; st.cur = ((k - 1) % n) + 1; st.phrase = Math.floor((k - 1) / n); }
        C.draw();
      },
      draw() {
        g.textContent = '';
        const {x, y, w, h} = st.box, pip = st.phrases > 1 && st.kind !== 'off' ? 1 : 0;   // phrase pips only while counting
        const r = Math.min(h * .42, w / (n + pip * 1.6) / 2.6), gap = (w - (pip ? r * 3.4 : 0)) / n;
        for (let i = 1; i <= n; i++) {
          const cx = x + gap * (i - .5), cy = y + h / 2, on = st.cur === i;
          const inBeat = st.kind === 'in' && i <= st.cur;
          const live = st.kind === 'count' && on, past = st.kind === 'count' && i < st.cur;
          mk('circle', {cx, cy, r: live ? r * 1.18 : r, fill: live ? (o.on || '#ffd34d') : inBeat ? (o.inFill || '#ffffff') : past ? (o.past || '#f3e3a8') : (o.off || '#ffffff'),
            stroke: live ? (o.onLine || '#7a5a00') : inBeat ? (o.inLine || '#00798c') : (o.offLine || '#9fb5b3'), 'stroke-width': live ? 3 : inBeat ? 4 : 2, opacity: st.kind === 'off' ? .75 : 1}, g);
          if (inBeat && st.cur === i) mk('circle', {cx, cy, r: r * .45, fill: o.inLine || '#00798c'}, g);
          if (st.mode === 'numbers') mk('text', {x: cx, y: cy + r * .38, 'text-anchor': 'middle', 'font-size': r * 1.05, 'font-weight': 700, fill: live ? '#3a2c00' : '#4e6266'}, g).textContent = i;
        }
        if (pip) for (let k = 0; k < Math.min(st.phrases, 4); k++) mk('rect', {x: x + w - r * 3 + (k % 2) * r * 1.5, y: y + h / 2 - r + Math.floor(k / 2) * r * 1.1, width: r * 1.1, height: r * .8, rx: r * .2, fill: k <= st.phrase && st.kind === 'count' ? (o.on || '#ffd34d') : '#fff', stroke: o.offLine || '#9fb5b3', 'stroke-width': 1.5}, g);
      },
    };
    if (clk) C.bind(clk);
    return C;
  }

  return {poses, pose, mirror, mix, level, dyn, gaits, path, paths, spline, readPath, readRules: RP, floor, flat, dancer, icon, phrase, clock, play, tween,
    trail, ribbonStyles, music, counts, skeleton, BASE, shade,
    get heard() { return heard; }};
})();
