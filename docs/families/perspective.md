# Perspective family

Tools where a real pinhole camera looks at a world of boxes on a ground plane: the horizon is the eye height, edges
meet at vanishing points, and the student either moves the camera or draws over guides that obey it.

Engine: `kit/perspective.js` (one global `Persp`, pure math, no DOM). Include it after the kit with
`<script src="kit:perspective"></script>`. First built for city-skyline-studio (2026-10-28).

## What the engine does (shared)

World frame ("level frame"): meters, x right, y up from the ground, z forward; the eye stands at (0, eye, 0). Pitch
(Tilt) is positive looking up. Screen: u right, v down, in CSS px.

Camera model: a 36 mm wide sensor, so f = lensMm / 36 x W px and the field of view is 2 atan(18 / lensMm)
(24 mm 73.7 degrees, 35 mm 54.4, 50 mm 39.6, 85 mm 23.9). `horizonY` places the image center row on the page (a lens
shift: it moves the drawing, never changes its geometry); `horizonRow` instead places the true horizon on that row, so
a tilted camera keeps its horizon where the student put it (the image center moves by f tan pitch). Level camera:
u = cx + f x / z, v = cy - f (y - eye) / z.

```js
const cam = Persp.camera({W, H, lensMm, eye, horizonY, horizonRow, pitch = 0, cx = W/2, near = 1})
// -> {W, H, lensMm, eye, pitch, f, cx, cy, sp, cp, near, fov, horizon, focalLengths(px)}
//    horizon = cy + f tan(pitch) (screen y); cam.focalLengths(px) = px / f (a screen distance in focal lengths)
Persp.project(cam, [x, y, z])          // -> {u, v, z} or null when the point is behind the near plane (z < near)
Persp.ground(cam, u, v, y = 0)         // screen -> world point on the level plane at height y, or null (sky side)
Persp.ray(cam, u, v)                   // the level-frame direction of the sight line through (u, v), from the eye
Persp.vp(cam, dir)                     // vanishing point of a world direction: {u, v, inf: false} or {inf: true, angle}
Persp.dirs(turn)                       // the grid's two directions at turn t (degrees): R (cos t, 0, sin t), L (-sin t, 0, cos t), V
Persp.vps(cam, turn)                   // {L, R, V3 (null when level), apart (px, null if one is infinite), off: {L, R, V3}}
Persp.poly(cam, worldPts)              // a world polygon clipped at the near plane and projected: [{u, v}]
Persp.line(cam, A, B)                  // a world segment clipped and projected: [p, q] or null
Persp.clipRect(seg, x0, y0, x1, y1)    // a screen segment clipped to a rectangle, or null
Persp.box(cam, {x, z, w, d, h, y0 = 0, turn, id})
  // the visible faces of a box (back faces culled, near plane clipped), far to near. Each face:
  // {pts, world (4 corners: s along the bottom, t up), normal, depth, center, kind 'wall'|'top'|'bottom',
  //  side '-L'|'+R'|'+L'|'-R'|'top'|'bottom', vp 'L'|'R' (the VP its receding edges run to), vps, widthM, heightM,
  //  clipped, id, cam}
Persp.order(faces)                     // painter's order (far to near by face-center depth)
Persp.corners(faces)                   // visible corners [{u, v, world, id}] (for guides)
Persp.homography(quad)                 // (s, t) in 0..1 -> {u, v} for a projected quad
Persp.divide(face, rows, cols)         // projective division: {rows: [segments], cols: [segments], at(s, t), cell(i, j, inset, insetV)}
Persp.targets(cam, turn, {vertical, horizontal = true})
  // snap targets: VP L, VP R, VP 3 (with pitch), vertical, horizontal: {id, label, u, v} or {id, label, angle}.
  // With pitch the screen vertical is left out (uprights run to VP 3) unless {vertical: true} asks for it
Persp.snap(cam, start, end, targets, maxDeg = 6)
  // -> {end, target (id or null), label, deg}: the end moved onto the nearest target's line through start when
  //    within maxDeg (either direction along the line; off-page and infinite VPs work). cam is unused (the targets
  //    carry the camera); it stays first so calls read like the rest of the API
Persp.shade(normal, sunAngleDeg)       // 'light' | 'mid' | 'dark' (walls by n . sun: > .25 light, < -.25 dark; tops mid; bottoms dark)
Persp.hatch(pts, vp, spacing)          // segments filling a convex screen polygon, aimed at vp (parallel for an infinite vp)
Persp.inside(pts, u, v), Persp.chord(convexPts, p, dx, dy)
Persp.fov(lensMm), Persp.focal(lensMm, W), Persp.baseY(cam, z), Persp.size(cam, z, h), Persp.toCam(cam, p), Persp.SENSOR (36)
  // baseY and size assume a level camera (pitch 0): the ground-plane shortcut for fixed-camera tools
```

Checked (node and Python, 2026-10-28): the spec's worked values at W = 1200 (35 mm: f = 1166.7; turn 45 VPs at -566.7
and 1766.7; turn 30 at -73.6 and 2620.7; 85 mm turn 45 apart 5666.7); every box edge meets its VP within 1e-11 px at
pitch 0, 15 and -10; a point at eye height projects to the horizon; ground() round-trips project().

## Fixed by the engine

- Camera: 36 mm sensor, f from the lens, the horizon at eye height, `horizonY` as a lens shift.
- VPs from the grid turn: VP R at cx + f cot t, VP L at cx - f tan t (level), apart 2f / sin 2t; seen from the eye they
  are 90 degrees apart. Tilt gives VP 3 at f / tan p from center and moves the horizon by f tan p.
- Near-plane clipping (z under 1 m), back-face culling, painter's order by face depth.
- Projective division (windows, floors) and hatching aimed at a face's VP.
- Snapping: by angle from the stroke start, 6 degrees by default.

## Rules for siblings

- Draw at real pixels and build the camera from the stage's CSS size every frame (`Persp.camera({W, H, ...})`); never
  scale one fixed drawing.
- Show the guides the way vanishing-point-studio does: thin dashed lines (5 5) to the VPs, VPs as red dots with a
  dark-chipped label, an arrow at the page edge when a VP is off the page.
- Keep the camera honest: if a tool changes the geometry for framing, say so in a readout and in handoff.md.
- **High eyes must look down (stand-back and Auto horizon).** A camera that rises has to show the city from above: roofs
  and a real street grid, with the city filling at least half the stage at the widest lens. city-skyline-studio's rule
  (settled in refine round 1, 2026-10-28): the eye stands back 120 m + 0.6 m per meter above 1.6 m (Drone 150 m is 209
  m back, about 36 degrees down; Helicopter 400 m is 359 m back, about 48 degrees down), and `Horizon on page` has an
  Auto mode that puts the block's nearest ground corner at 90% of the stage height (the horizon may go up to 600% above
  the page; it never changes a VP, only where the drawing sits). The old rule (6 m back per meter) made Drone and
  Helicopter a shrunken Rooftop and is retired. Show the distance back and the angle down in a readout.
- **Fit a fixed outline whole, with one uniform scale.** A drawing made from a hidden camera must show whole at every
  stage size. Shrink the picture by one scale s (at most 1) so the outline fits the room under any chips, which is the
  same as giving both cameras the focal length f x s: every angle, VP direction and match stays the same, and the lens
  is still compared in mm. Then center the outline with the lens shift (horizonRow; the horizon may sit off the page).
  The student's camera uses the same s, so a match overlays exactly. Say so in the focal-length readout.
  city-skyline-studio's Find the Camera does this per target (findScale, fitHor); round 1's "lowest point at 95%" rule
  cut the tops of 5 of 6 targets and is retired.
- **A camera-finding meter rises setting by setting, and answers only when asked.** Score each setting on its own
  (eye height on a log ratio, turn, lens by stops apart, tilt) and show the mean; call it matched only when every
  setting is at 95% or more. Silhouette overlap had false peaks at street level. The meter is not live: a student who
  watches a live meter can sweep one slider at a time to the answer without reading the picture. The student presses
  Check camera; the meter and per-setting scores show for the camera as checked (marked stale after any change), and
  the first setting that misses names what to read in the picture next (where the horizon crosses the buildings, where
  the edges meet, how far apart the VPs are, how the uprights lean). Targets must not sit on the eye height stops, and
  stops must not snap there.
- **Off-page VPs point where they really are.** An off-page VP is drawn at the page edge where the line from the page's
  middle toward it leaves the page (for a VP infinitely far along the horizon, from the horizon's row), with an arrow
  in that direction: a VP above the page shows at the top edge near its own u, not at a side. A VP under a band that
  covers the stage (a compact hint) counts as off. VP chips keep clear of each other and of the horizon chip. Spoken
  lines must not count dots that may be arrows.
- Store drawings in screen space relative to the image center in units of W (they fit any stage size) with the
  camera they were drawn under.

## What each tool brings

| Tool | Band | Uses | Brings |
|---|---|---|---|
| vanishing-point-studio | 6-8 | (not yet moved; its own code) | one VP: turn 0, fronts on the picture plane, boxes drawn by dragging. Moves onto the engine when next touched: at turn 0, VP L is the one VP (at the image center) and VP R is infinite, so `vps`, `box`, `targets` and `snap` work unchanged. |
| city-skyline-studio | 9-12 | all of it | a city of boxes on a lot grid, a camera with eye height, turn, lens, horizon (Auto) and tilt, Find the Camera (per-setting match on Check camera, outlines fitted whole by a uniform scale), Ink over guides with Check my drawing |
| near-and-far | 3-5 | possible (its spec's open question) | the same ground-plane formula (`baseY`, `size`) with a fixed camera |
