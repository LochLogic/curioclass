/* Curio Class family engine: perspective (kit/perspective.js). One global, Persp. Docs: docs/families/perspective.md.
   Built by city-skyline-studio (grades 9-12) to the full description in tools/city-skyline-studio/spec.md
   ("Family engine"); vanishing-point-studio (6-8) moves onto it when next touched.

   A pinhole camera (Szeliski, Computer Vision, 2nd ed., section 2.1): a 36 mm wide sensor, so f = lens / 36 x W px
   and the horizontal field of view is 2 atan(18 / lens). World frame ("level frame"): meters, x right, y up from the
   ground, z forward from the eye's foot; the eye sits at (0, eye, 0). Screen: px, u right, v down.
   A level camera (pitch 0) projects (x, y, z) to u = cx + f x / z, v = cy - f (y - eye) / z, so the horizon is the
   row v = cy. A pitched camera (pitch p in degrees, up is positive) turns the picture plane: verticals meet at VP 3,
   f / tan p from the image center (above when looking up), and the horizon moves f tan p the other way.
   `horizonY` is a lens shift: the screen row of the image center. It never changes the drawing's shape.

   Everything here is pure (no DOM), so it runs in tests too. */
const Persp = (() => {
  const D = Math.PI / 180, SENSOR = 36, NEAR = 1;

  // ---------- camera ----------
  // camera({W, H, lensMm, eye, horizonY, horizonRow, pitch, cx, near}) -> cam (a plain object; read its fields, never
  // set them). horizonY is the image center row (a lens shift). horizonRow instead places the true horizon on that row
  // whatever the pitch (the image center then sits f tan(pitch) above it): use it when a "Horizon on page" control
  // should keep meaning the horizon once the camera tilts.
  function camera(o = {}) {
    const W = o.W || 1000, H = o.H || 620, lensMm = o.lensMm || 35, eye = o.eye == null ? 1.6 : o.eye;
    const pitch = o.pitch || 0, p = pitch * D, f = lensMm / SENSOR * W;
    const cy = o.horizonRow != null ? o.horizonRow - f * Math.tan(p) : o.horizonY == null ? H / 2 : o.horizonY;
    const cam = {W, H, lensMm, eye, pitch, f, cx: o.cx == null ? W / 2 : o.cx, cy,
      sp: Math.sin(p), cp: Math.cos(p), near: o.near || NEAR};
    cam.fov = 2 * Math.atan(SENSOR / 2 / lensMm) / D;                 // horizontal field of view, degrees
    cam.horizon = cam.cy + f * Math.tan(p);                             // the screen row of the true horizon
    cam.focalLengths = px => px / f;                                    // a screen distance in focal lengths
    return cam;
  }
  // level frame -> camera frame [x, y, z] (z is depth along the line of sight)
  function toCam(cam, P) {
    const Y = P[1] - cam.eye;
    return [P[0], Y * cam.cp - P[2] * cam.sp, Y * cam.sp + P[2] * cam.cp];
  }
  function fromCamDir(cam, d) {   // camera frame direction -> level frame direction
    return [d[0], d[1] * cam.cp + d[2] * cam.sp, -d[1] * cam.sp + d[2] * cam.cp];
  }
  // ray(cam, u, v) -> the level-frame direction of the sight line through screen point (u, v), from the eye (0, eye, 0)
  const ray = (cam, u, v) => fromCamDir(cam, [(u - cam.cx) / cam.f, -(v - cam.cy) / cam.f, 1]);
  const proj = (cam, c) => ({u: cam.cx + cam.f * c[0] / c[2], v: cam.cy - cam.f * c[1] / c[2], z: c[2]});
  // project(cam, [x, y, z]) -> {u, v, z} (z = depth), or null when the point is behind the near plane (z < 1 m)
  function project(cam, P) {
    const c = toCam(cam, P);
    return c[2] < cam.near ? null : proj(cam, c);
  }
  // ground(cam, u, v, y = 0) -> [x, y, z]: where the sight line through screen point (u, v) meets the level plane at
  // height y (the ground by default). null when it never does (above the horizon for the ground) or behind the eye.
  function ground(cam, u, v, y = 0) {
    const d = ray(cam, u, v);
    const dy = y - cam.eye;
    if (Math.abs(d[1]) < 1e-9 || dy / d[1] <= 0) return null;
    const t = dy / d[1];
    if (d[2] * t < 0) return null;
    return [d[0] * t, y, d[2] * t];
  }
  // vanishing point of a direction (level frame): {u, v, inf: false} or, parallel to the picture plane, {inf: true,
  // angle} (the screen direction those lines keep, radians). Off-page values are kept (u may be -5000).
  function vp(cam, dir) {
    const c = toCam(cam, [dir[0], dir[1] + cam.eye, dir[2]]);
    if (Math.abs(c[2]) < 1e-9) return {inf: true, angle: Math.atan2(-c[1], c[0]), u: NaN, v: NaN};
    const q = proj(cam, c);
    return {u: q.u, v: q.v, inf: false};
  }
  // the two edge directions of a grid turned by `turn` degrees: R along (cos t, 0, sin t), L along (-sin t, 0, cos t)
  const dirs = turn => { const t = turn * D; return {R: [Math.cos(t), 0, Math.sin(t)], L: [-Math.sin(t), 0, Math.cos(t)], V: [0, 1, 0]}; };
  // vps(cam, turn) -> {L, R, V3 (null when level), apart (px, null if one is at infinity), off: {L, R, V3}}
  // With pitch 0: VP R at u = W/2 + f cot t, VP L at u = W/2 - f tan t, both on the horizon, 2f / sin 2t apart.
  function vps(cam, turn) {
    const d = dirs(turn), L = vp(cam, d.L), R = vp(cam, d.R), V3 = cam.pitch ? vp(cam, d.V) : null;
    const offOne = p => !p || p.inf || p.u < 0 || p.u > cam.W || p.v < 0 || p.v > cam.H;
    return {L, R, V3, apart: L.inf || R.inf ? null : Math.hypot(R.u - L.u, R.v - L.v),
      off: {L: offOne(L), R: offOne(R), V3: V3 ? offOne(V3) : false}};
  }

  // ---------- clipping ----------
  // clip a polygon (level frame points) to the near plane; returns camera-frame points
  function clipNear(cam, pts) {
    const c = pts.map(p => toCam(cam, p)), out = [], n = cam.near;
    for (let i = 0; i < c.length; i++) {
      const a = c[i], b = c[(i + 1) % c.length], ia = a[2] >= n, ib = b[2] >= n;
      if (ia) out.push(a);
      if (ia !== ib) { const t = (n - a[2]) / (b[2] - a[2]); out.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, n]); }
    }
    return out;
  }
  // poly(cam, worldPts) -> screen points [{u, v}] of the part in front of the eye (may be empty)
  const poly = (cam, pts) => clipNear(cam, pts).map(c => proj(cam, c));
  // line(cam, A, B) -> [{u, v}, {u, v}] for the part of a world segment in front of the eye, or null
  function line(cam, A, B) {
    let a = toCam(cam, A), b = toCam(cam, B); const n = cam.near;
    if (a[2] < n && b[2] < n) return null;
    if (a[2] < n || b[2] < n) {
      const t = (n - a[2]) / (b[2] - a[2]), m = [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, n];
      if (a[2] < n) a = m; else b = m;
    }
    return [proj(cam, a), proj(cam, b)];
  }
  // clip a screen segment to a rectangle (Liang-Barsky): [{u, v}, {u, v}] or null
  function clipRect(seg, x0, y0, x1, y1) {
    let [a, b] = seg, t0 = 0, t1 = 1; const du = b.u - a.u, dv = b.v - a.v;
    for (const [p, q] of [[-du, a.u - x0], [du, x1 - a.u], [-dv, a.v - y0], [dv, y1 - a.v]]) {
      if (p === 0) { if (q < 0) return null; continue; }
      const r = q / p;
      if (p < 0) { if (r > t1) return null; if (r > t0) t0 = r; } else { if (r < t0) return null; if (r < t1) t1 = r; }
    }
    return [{u: a.u + du * t0, v: a.v + dv * t0}, {u: a.u + du * t1, v: a.v + dv * t1}];
  }

  // ---------- boxes ----------
  // box(cam, {x, z, w, d, h, y0, turn, id}) -> the visible faces of a box, far to near. (x, z) is the footprint center in
  // the level frame, w runs along R (cos t, sin t), d along L (-sin t, cos t), the box spans heights y0 to y0 + h.
  // Each face: {pts (screen, clipped at the near plane), world (4 level-frame corners), normal, depth (m, eye to face
  // center), kind 'wall' | 'top' | 'bottom', vp 'L' | 'R' (the VP its horizontal edges run to; a top or bottom has
  // both: vps ['L', 'R']), side ('+R' | '-R' | '+L' | '-L' | 'top' | 'bottom'), widthM, heightM, id, cam}.
  // Back faces are culled; a face wholly behind the eye is dropped.
  function box(cam, b) {
    const t = (b.turn || 0) * D, a = [Math.cos(t), Math.sin(t)], c = [-Math.sin(t), Math.cos(t)];
    const w2 = b.w / 2, d2 = b.d / 2, y0 = b.y0 || 0, y1 = y0 + b.h;
    const at = (i, j, y) => [b.x + a[0] * w2 * i + c[0] * d2 * j, y, b.z + a[1] * w2 * i + c[1] * d2 * j];
    // corners in order around the footprint: (-,-) (+,-) (+,+) (-,+)
    const F = [[-1, -1], [1, -1], [1, 1], [-1, 1]];
    const lo = F.map(([i, j]) => at(i, j, y0)), hi = F.map(([i, j]) => at(i, j, y1));
    const walls = [
      {side: '-L', n: [-c[0], 0, -c[1]], q: [lo[0], lo[1], hi[1], hi[0]], vp: 'R', wm: b.w},   // near-L face: edges along R
      {side: '+R', n: [a[0], 0, a[1]], q: [lo[1], lo[2], hi[2], hi[1]], vp: 'L', wm: b.d},
      {side: '+L', n: [c[0], 0, c[1]], q: [lo[2], lo[3], hi[3], hi[2]], vp: 'R', wm: b.w},
      {side: '-R', n: [-a[0], 0, -a[1]], q: [lo[3], lo[0], hi[0], hi[3]], vp: 'L', wm: b.d},
    ];
    const eye = [0, cam.eye, 0], out = [];
    const add = (fc, kind) => {
      const m = fc.q.reduce((s, p) => [s[0] + p[0] / 4, s[1] + p[1] / 4, s[2] + p[2] / 4], [0, 0, 0]);
      const toEye = [eye[0] - m[0], eye[1] - m[1], eye[2] - m[2]];
      if (fc.n[0] * toEye[0] + fc.n[1] * toEye[1] + fc.n[2] * toEye[2] <= 1e-9) return;   // back face
      const pts = poly(cam, fc.q);
      if (pts.length < 3) return;
      out.push({pts, world: fc.q, normal: fc.n, depth: Math.hypot(...toEye), kind, side: fc.side, vp: fc.vp,
        vps: kind === 'wall' ? [fc.vp] : ['L', 'R'], widthM: fc.wm, heightM: kind === 'wall' ? b.h : b.d,
        clipped: pts.length !== 4 || fc.q.some(p => toCam(cam, p)[2] < cam.near), id: b.id, cam, center: m});
    };
    walls.forEach(fc => add(fc, 'wall'));
    add({side: 'top', n: [0, 1, 0], q: hi, vp: 'L', wm: b.w}, 'top');
    if (y0 > 0) add({side: 'bottom', n: [0, -1, 0], q: [lo[3], lo[2], lo[1], lo[0]], vp: 'L', wm: b.w}, 'bottom');
    return order(out);
  }
  // order(faces) sorts far to near (painter's order by the distance from the eye to each face center), in place
  const order = faces => faces.sort((p, q) => q.depth - p.depth);
  // corners(faces) -> the distinct world corners of these faces that are in front of the eye: [{u, v, world, id}]
  function corners(faces) {
    const seen = new Map();
    for (const fc of faces) for (const P of fc.world) {
      const k = P.map(x => x.toFixed(3)).join(',') + '|' + fc.id;
      if (seen.has(k)) continue;
      const q = project(fc.cam, P);
      if (q) seen.set(k, {u: q.u, v: q.v, world: P, id: fc.id});
    }
    return [...seen.values()];
  }

  // ---------- dividing a face in perspective ----------
  // homography(quad) -> (s, t) => {u, v}: the projective map from the unit square onto a screen quad (corners in order
  // (0,0) (1,0) (1,1) (0,1)). Exact for the picture of any flat rectangle, with no world needed (one-point tools).
  function homography(q) {
    const [p0, p1, p2, p3] = q.map(p => [p.u, p.v]);
    const dx1 = p1[0] - p2[0], dx2 = p3[0] - p2[0], sx = p0[0] - p1[0] + p2[0] - p3[0];
    const dy1 = p1[1] - p2[1], dy2 = p3[1] - p2[1], sy = p0[1] - p1[1] + p2[1] - p3[1];
    const den = dx1 * dy2 - dx2 * dy1;
    const g = den ? (sx * dy2 - dx2 * sy) / den : 0, h = den ? (dx1 * sy - sx * dy1) / den : 0;
    const A = p1[0] - p0[0] + g * p1[0], B = p3[0] - p0[0] + h * p3[0], C = p0[0];
    const Dd = p1[1] - p0[1] + g * p1[1], E = p3[1] - p0[1] + h * p3[1], F = p0[1];
    return (s, t) => { const w = g * s + h * t + 1; return {u: (A * s + B * t + C) / w, v: (Dd * s + E * t + F) / w}; };
  }
  // divide(face, rows, cols) -> {rows: [[a, b], ...], cols: [[a, b], ...], at(s, t), cell(i, j, inset)}
  // rows - 1 lines across and cols - 1 lines up the face, spaced equally on the real face, so they crowd together as
  // the face recedes (projective division). A face from box() divides its world rectangle (clipped at the near plane);
  // a face with only screen pts (4 corners: bottom-left, bottom-right, top-right, top-left) uses the homography.
  function divide(face, rows, cols) {
    const W = face.world, cam = face.cam;
    let at, seg;
    if (W && cam) {
      const P = (s, t) => [0, 1, 2].map(k => W[0][k] + (W[1][k] - W[0][k]) * s + (W[3][k] - W[0][k]) * t);
      at = (s, t) => project(cam, P(s, t));
      seg = (s0, t0, s1, t1) => line(cam, P(s0, t0), P(s1, t1));
    } else {
      const H = homography(face.pts);
      at = H; seg = (s0, t0, s1, t1) => [H(s0, t0), H(s1, t1)];
    }
    const R = [], C = [];
    for (let i = 1; i < rows; i++) { const s = seg(0, i / rows, 1, i / rows); if (s) R.push(s); }
    for (let j = 1; j < cols; j++) { const s = seg(j / cols, 0, j / cols, 1); if (s) C.push(s); }
    // a window in cell (row i from the bottom, column j): inset is the margin on each side as a fraction of the cell
    const cell = (i, j, inset = .2, insetV = inset) => {
      const s0 = (j + inset) / cols, s1 = (j + 1 - inset) / cols, t0 = (i + insetV) / rows, t1 = (i + 1 - insetV) / rows;
      const q = [at(s0, t0), at(s1, t0), at(s1, t1), at(s0, t1)];
      return q.every(Boolean) ? q : null;
    };
    return {rows: R, cols: C, at, cell};
  }

  // ---------- snapping ----------
  // targets(cam, turn, {vertical, horizontal}) -> the standard snap list: VP L, VP R, VP 3 (with pitch), vertical,
  // horizontal. A target is {id, label, u, v} (a point) or {id, label, angle} (a direction, radians, screen frame).
  // With pitch, building uprights run to VP 3, so the screen vertical is left out unless {vertical: true} asks for it.
  function targets(cam, turn, o = {}) {
    const v = vps(cam, turn), out = [];
    const pt = (id, label, p) => out.push(p.inf ? {id, label, angle: p.angle} : {id, label, u: p.u, v: p.v});
    pt('L', 'VP L', v.L); pt('R', 'VP R', v.R);
    if (v.V3) pt('V3', 'VP 3', v.V3);
    if (o.vertical === true || (o.vertical !== false && !cam.pitch)) out.push({id: 'vertical', label: 'vertical', angle: Math.PI / 2});
    if (o.horizontal !== false) out.push({id: 'horizontal', label: 'horizontal', angle: 0});
    return out;
  }
  // snap(cam, start, end, targets, maxDeg = 6) -> {end, target, label, deg}: if the stroke start -> end is within maxDeg
  // of the line from start toward a target (either way along it), end moves onto that line (same length along it).
  // VPs off the page still work (the line just aims off the page). target is null for a free line.
  // cam is not used (the targets already carry the camera); it stays first so calls read like the rest of the API.
  function snap(cam, start, end, tg, maxDeg = 6) {
    const du = end.u - start.u, dv = end.v - start.v, len = Math.hypot(du, dv);
    if (len < 1e-6) return {end, target: null, label: '', deg: 0};
    const ang = Math.atan2(dv, du);
    const diff = (x, y) => { let d = Math.abs(x - y) % Math.PI; return Math.min(d, Math.PI - d); };
    let best = null;
    for (const t of tg || []) {
      let a;
      if (t.angle != null) a = t.angle;
      else { if (Math.hypot(t.u - start.u, t.v - start.v) < 1e-6) continue; a = Math.atan2(t.v - start.v, t.u - start.u); }
      const d = diff(ang, a);
      if (d <= maxDeg * D && (!best || d < best.d)) best = {t, a, d};
    }
    if (!best) return {end, target: null, label: '', deg: 0};
    const ex = Math.cos(best.a), ey = Math.sin(best.a), k = du * ex + dv * ey;
    return {end: {u: start.u + ex * k, v: start.v + ey * k}, target: best.t.id, label: best.t.label, deg: best.d / D};
  }

  // ---------- light ----------
  // shade(normal, sunAngle) -> 'light' | 'mid' | 'dark'. The sun is low (dusk): sunAngle (degrees) is its direction
  // on the ground plane in the same frame as the normal, toward (cos a, 0, sin a). A wall facing it is light, one
  // edge-on is mid, one facing away is dark; a roof catches grazing light (mid); an underside is dark.
  function shade(n, sunAngle) {
    if (n[1] > .5) return 'mid';
    if (n[1] < -.5) return 'dark';
    const a = sunAngle * D, k = n[0] * Math.cos(a) + n[2] * Math.sin(a);
    return k > .25 ? 'light' : k < -.25 ? 'dark' : 'mid';
  }

  // ---------- small helpers for drawings ----------
  const fov = lensMm => 2 * Math.atan(SENSOR / 2 / lensMm) / D;
  const focal = (lensMm, W) => lensMm / SENSOR * W;
  // where the base of a thing z m away sits on the page (ground-plane formula), and how tall h m looks there (px).
  // Level camera only (pitch 0): they ignore pitch.
  const baseY = (cam, z) => cam.cy + cam.f * cam.eye / z;
  const size = (cam, z, h) => cam.f * h / z;
  // point in polygon (screen) and the convex clip of a line through it, for hit tests and hatching
  function inside(pts, u, v) {
    let k = false;
    for (let i = 0, j = pts.length - 1; i < pts.length; j = i++) {
      const a = pts[i], b = pts[j];
      if ((a.v > v) !== (b.v > v) && u < (b.u - a.u) * (v - a.v) / (b.v - a.v) + a.u) k = !k;
    }
    return k;
  }
  // the part of the infinite line through p with direction (dx, dy) inside a convex polygon, or null
  function chord(pts, p, dx, dy) {
    let t0 = -Infinity, t1 = Infinity;
    const n = pts.length;
    let area = 0;
    for (let i = 0; i < n; i++) { const a = pts[i], b = pts[(i + 1) % n]; area += a.u * b.v - b.u * a.v; }
    const s = area > 0 ? 1 : -1;
    for (let i = 0; i < n; i++) {
      const a = pts[i], b = pts[(i + 1) % n];
      const nx = -(b.v - a.v) * s, ny = (b.u - a.u) * s;          // inward normal
      const num = (p.u - a.u) * nx + (p.v - a.v) * ny, den = dx * nx + dy * ny;
      if (Math.abs(den) < 1e-12) { if (num < 0) return null; continue; }
      const t = -num / den;
      if (den > 0) t0 = Math.max(t0, t); else t1 = Math.min(t1, t);
      if (t0 > t1) return null;
    }
    return [{u: p.u + dx * t0, v: p.v + dy * t0}, {u: p.u + dx * t1, v: p.v + dy * t1}];
  }
  // hatch(face pts, vp, spacing) -> segments filling a convex face with lines aimed at vp ({u, v} or {inf, angle});
  // spacing (px) is measured at the face's far side from the VP, so the lines close up toward it like real edges do
  function hatch(pts, v, spacing) {
    const out = [];
    if (!pts || pts.length < 3) return out;
    if (v.inf) {
      const dx = Math.cos(v.angle), dy = Math.sin(v.angle), nx = -dy, ny = dx;
      const ds = pts.map(p => p.u * nx + p.v * ny), lo = Math.min(...ds), hi = Math.max(...ds);
      for (let s = lo + spacing / 2; s < hi; s += spacing) {
        const c = chord(pts, {u: nx * s, v: ny * s}, dx, dy);
        if (c) out.push(c);
      }
      return out;
    }
    if (inside(pts, v.u, v.v)) return out;
    const angs = pts.map(p => Math.atan2(p.v - v.v, p.u - v.u));
    const base = angs[0], rel = angs.map(a => { let d = a - base; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI; return d; });
    const lo = Math.min(...rel), hi = Math.max(...rel), far = Math.max(...pts.map(p => Math.hypot(p.u - v.u, p.v - v.v)));
    const step = spacing / Math.max(far, 1);
    for (let r = lo + step / 2; r < hi; r += step) {
      const a = base + r, c = chord(pts, {u: v.u, v: v.v}, Math.cos(a), Math.sin(a));
      if (c) out.push(c);
      if (out.length > 600) break;
    }
    return out;
  }

  return {camera, project, ground, ray, vp, vps, dirs, box, order, corners, divide, homography, targets, snap, shade,
    poly, line, clipRect, toCam, fov, focal, baseY, size, inside, chord, hatch, SENSOR};
})();
if (typeof module !== 'undefined') module.exports = Persp;
