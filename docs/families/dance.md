# Family: dance

Four tools, grades K to 12 (arts, dance), share one engine: `kit/dance.js`, inlined with
`<script src="kit:dance"></script>` after `kit:curio`. It exposes `Dance`. The full description lives in
`tools/levels-and-pathways/spec.md`, "Family engine"; this file is the working reference. Built 2026-10-28 with
levels-and-pathways, the first tool of the family.

Warning: the bundler inlines the file between script tags, so a literal closing script tag anywhere in
`kit/dance.js` (even inside a comment) ends the script early and `Dance` is undefined. Never write one.

**The figure is dance's own.** The spec's open question (share one dancer figure with the PE movement family in a
`kit/movement.js`) was answered by Cory on 2026-10-27 (decisions/BASELINE.md, w1-21): "do not share one dancer figure
between PE and dance; each gets its own." So the figure lives inside `kit/dance.js`, there is no `kit/movement.js`
from this family, and fitness-circuit's builder makes its own figure. Copying ideas from this file is fine; loading
`kit/dance.js` into a PE tool is not.

## Units and the floor

Floor units: x 0 (left) to 100 (right), z 0 (back wall) to 60 (front edge, nearest the class), y up. A dancer's
height is in floor units too (`floor.dancerHeight`, about 40 percent of the stage height at z 50).

```js
const floor = Dance.floor(svg, 'studio' | 'stage' | 'square' | 'void', {w, h, box, colors, backdrop, dancerFrac})
floor.resize(w, h, {x0, x1, yBack, yFront})   // real pixels; the box is where the floor's front edge (x0 to x1) and
                                              // its back and front edges sit on screen. Call on every relayout.
floor.layers   // svg groups, back to front: bg, floor, marks, mirror, trail, shadow, actors, front (put your own in them)
floor.project(x, y, z) -> [sx, sy, depth]      // pinhole camera; depth sorts actors
floor.map(x, z) -> {x, y, s}; floor.unmap(px, py) -> {x, z}; floor.scale(z) -> pixels per floor unit
floor.inside(x, z, pad); floor.quad(x0, z0, x1, z1) -> polygon points; floor.wallTop(); floor.onResize(fn)
floor.mirror   // {x, y, w, h} of the studio mirror strip (null in other views)
Dance.flat(k, ox, oy)   // a flat front-on projection (k pixels per body height, origin at ox, oy): no floor, for
                        // contact sheets and tests (Dance.icon uses it)
```

- `studio`: wood floor, back wall with a mirror strip, a barre and two window patches (levels-and-pathways).
- `stage`: proscenium audience view, dark floor with depth rows, red curtains in front of the actors.
- `square`: outdoor platform; `backdrop` is an image URL (data URI) or the built-in sky and hills.
- `void`: dark space with a faint grid (good with exposure trails).
- Decoration is redrawn on every resize (a studio's barre sits behind the actors, a stage's curtains in front).

## Poses

```js
Dance.poses             // 27 named poses: stand, reach-up, arms-wide, bend-fwd, bend-side, twist, curl, crouch, kneel,
                        // sit, lie, lunge, plie, releve, passe, arabesque, star-jump, tuck-jump, clap, point, kick,
                        // stamp, step, hop, contraction, release, bow
Dance.pose(p)           // a name or a partial pose -> a full pose (missing joints from Dance.BASE)
Dance.level(p, 'high' | 'middle' | 'low')   // a pose's own .high / .low version wins; else high = tiptoe and arms
                        // up, low = a wide deep squat with a forward lean. stand has its own low: a neat squat that
                        // faces the class (the generic low modifier reads as a fall at rest)
Dance.mirror(p); Dance.mix(a, b, t)
Dance.skeleton(p) -> {joint: [x, y, z]}   // joint positions in body heights, grounded on the lowest support (feet,
                        // knees, pelvis); measure a pose's head-top height with it (head[1] + .074)
Dance.BASE              // the full standing pose every partial pose is filled from
```

A pose is joint angles in degrees: `head` (nod, + down), `tilt`, `lean` (trunk, + forward), `side` (+ to the dancer's
left), `twist`; `lArm` / `rArm` `[up, fwd, foreUp, foreFwd]` (upper arm and forearm: up from hanging, then swung
forward from the side); `lLeg` / `rLeg` `[hip, out, knee]` (hip + forward, out to the side, knee bend); `lToe` /
`rToe` 0 to 1 (tiptoe; `toe` sets both); `pitch`, `roll` (whole body, for floor shapes); `yaw` (the whole body turns
to its own left, inside the pose: a lying shape turns so it reads along the floor while the dancer still faces the
class; `Dance.mirror` negates it); `lift` (floor units, a jump). `arms` and `legs` set both sides. A partial pose may
carry `high` and `low` partial poses for `Dance.level`.

Facing angles (`d.set`, `Dance.icon`, phrase steps): degrees, 0 faces the class (the front), 90 turns to the dancer's
own left (seen from the class, the dancer faces right), 180 faces the back wall, -90 or 270 the dancer's right.

Low level reads low only when the body is on the floor. Measured head heights (body heights, from `Dance.skeleton`):
standing middle shapes 0.8 to 1.0, sitting 0.5 to 0.6, kneeling back on the heels about 0.5, lying 0.15. Upright
kneeling (0.77) and a crouch (0.6 to 0.7) sit too close to middle for K-2 copying; levels-and-pathways keeps every low
keyframe at 0.62 or under and every middle one at 0.8 or over (its handoff.md has the contact sheet).

## Figures

```js
const d = Dance.dancer(floor.layers.actors, {floor, top, bottom, skin, hair, shoe, badge, scale, height, reflect,
                                             ghost, noShadow, lineScale})
d.set({pose, x, z, facing, lift})   // facing: degrees, 0 faces the class, 90 the dancer's left
d.onMove(fn); d.world(joint) -> [x, y, z]; d.sj (screen joints), d.render(), d.remove(); d.scale (live)
Dance.icon(svg, pose, {facing, badge, ...colors})   // a still figure fitted into its own small svg (buttons, cards)
```

- `Dance.shade(color, k)`: a "#rrggbb" color darkened by k (0 to 1), as the figure darkens its outlines and hair line.
- No face. Colors per tool; `badge` ('circle', 'square', 'triangle', 'diamond') puts a shape on the chest so dancers
  never differ by color alone.
- `reflect: true` draws the studio mirror image (put it in `floor.layers.mirror`); a number under 1 pulls the image
  toward the glass so a big dancer's head stays in a short mirror. `ghost: 0.4` makes a faint copy.
- Limbs are capsules with outlines, sorted by depth every frame; hair sits behind or over the head by facing.

## Movement in time

```js
Dance.gaits             // walk, run, skip, gallop, slide, hop, march, leap: {counts per cycle, facing, swing, pose(q, dir)}
Dance.dyn               // smooth, sharp, swing, suspend, collapse, shake: timing curves between keyframes
Dance.path(points, {smooth}) -> {points, length, at(u) -> {x, z, dx, dz}, pointAt(s)}
Dance.paths.line(a, b), .arc(cx, cz, r, deg0, deg1, n), .poly(pts), .smooth(pts, n), .join(...paths); Dance.spline(pts, n)
Dance.readPath(raw, {start, bounds, floor, ...Dance.readRules}) -> {tooShort} | {parts: [{kind, pts, geo}], geo, length, lead}
  // reads a drawn line (floor units; with floor, as it looks on screen) as straight, curved and zigzag parts in drawing order (see "Reading a drawn
  // pathway" below); geo is the clean line (straight as one segment, curved as a spline, zigzag through its corners)
Dance.phrase([{poses, counts, level, dyn, side: 'L', facing, travel, gait, at}]) -> {steps, total, at(count)}
  // poses: keyframes, one per count, looping (A to B on count 1, B to A on count 2); level: a level or
  // fn(count index from 0) read every count; gait replaces poses; travel: a path covered during the step;
  // facing: degrees, 'travel' or 'front'; at: {x, z} for a step in place
const clk = Dance.clock(bpm, {meter: 3 | 4 | 6, countIn: 4})
  // clk.start(), pause(), resume(), seek(pos), setBpm(b) (next count), stop() (for good; its token goes stale)
  // clk.onCount((n, {beat, countIn}) => ...): n <= 0 during the count-in, 1, 2, ... after; it ticks once past the
  // last count of a phrase, so guard n <= phrase.total. clk.onFrame(fn) -> unsubscribe. clk.pos, clk.running.
const run = Dance.play(dancers, phrases, {clock: clk, offsets, loop, trails, onEnd, onFrame})
  // run.done: a promise, 'end' or 'stop'; run.stop(). offsets delay dancers by counts (canon). Motion off: the
  // pose and position jump once per count.
Dance.tween(d, {pose, facing, x, z}, ms, isLive) -> promise true, or false if isLive() went false
```

## Trails, music, counts

```js
const t = Dance.trail(d, {mode: 'ribbon' | 'exposure' | 'off', style: 'high' | 'middle' | 'low' | 'plain' | {...},
                          layer, hidden, color, handColor, footColor, ghostColors})
  // play() feeds it (t.capture(count)); t.points keeps the record in floor units
t.setStyle(s); t.show(bool); t.fade(to, ms); t.paintIn(ms, isLive); t.end(drawFn(g, x, y, s)) (an end badge);
t.transform({ox, oz, s}) (a gallery); t.setPoints(pts); t.add(x, z); t.clear(); t.remove()
  // styleAt: fn(count) -> a style per point, so one ribbon changes level part by part (Draw a path); setStyle clears
  // the per-point styles. Under transform s < 1 the high prints scale up (to 2.4x) so a small gallery copy still shows
  // them. In Motion-off (calm) play the record starts at the step's first point, not one count along it.
Dance.ribbonStyles      // high: blue prints, middle: green band, low: amber band with stripes, plain: gold dashed
                        // (Mystery: shape without the level)
Dance.music(track, clk) // {len, sub, swing, vol, countIn, parts: {inst: 'x.X.' or [midi | [chord] | null]}}
  // instruments: kick, snare, hat, clap, shaker, wood, click, tap, stamp, bass, piano, pluck, pad. Count-in clicks.
  // Silent with Sound off and before the first tap; m.mute(bool), m.stop()
const c = Dance.counts(group, clk, {n: 8, mode: 'dots' | 'numbers', phrases})
c.bind(clk, phrases); c.layout({x, y, w, h}); c.set(k | null)
  // phrase pips (one small box per 8 counts) show only for a run of more than one phrase, never when idle
```

`Dance.heard` is true once the page has had a tap or key: music and count clicks stay silent before it (browsers block
audio until then), so a tool's first sound always follows a tap.

## Reading a drawn pathway (Dance.readPath)

The rule a tool uses when a class draws a pathway (levels-and-pathways Draw a path; any sibling that reads a drawn
line). `Dance.readRules` holds the numbers ({tol 2, sharp 45, local 32, tipK 0.47, zigTurn 75, zigMin 60, zigMax 90,
hair 100, sideK 3, sideT 0.6, curve 30, curveScreen 24, minLen 15, maxParts 4}).

Pass the tool's `floor` (`{start, floor}`) whenever the line was drawn on a perspective floor. The line is then read
as it looks on screen, in units of the floor's scale at mid depth, so a shape reads the same drawn side to side, front
to back or on a slant (on the floor itself a front-to-back S is squashed and its far half is tiny, which made it read
straight or zigzag). The parts come back in floor units. Without `floor` the line is read in floor units as before.

1. Smooth the drag, resample it 1 unit apart and simplify it (tol). Under minLen units in all: tooShort.
2. Corners: simplified points that turn the same way within 7 units count as one corner. A corner turns sharp degrees
   or more within 8 units, at least local degrees (and half its turn) within 4 units of the point, and has a real tip:
   on a barely smoothed copy of the line, tipK of the turn happens within 1.5 units (8 pixels on a small stage) of its
   sharpest point. The top of a wave or an S, however tight, spreads its turn out, so it is never a corner, whichever
   way it is drawn. A gentle corner (under zigTurn) must also turn 0.6 of its turn right at the point and is not a
   hook in the first or last 10 units.
3. Zigzag: two or more corners in a row that each turn zigMin or more, turn left and right in turn (or both turn hair
   degrees or more, like a scribble's hairpins), joined by straight legs of zigMax units or less. Corners that turn the
   same way and less than hair (an L, a box) stay boundaries between straight parts.
4. The leg before and after a zigzag joins it when it is straight, no longer than sideK zigzag legs and zigMax, and
   its corner turns at least sideT of the run's middle turn (a straight line that bends gently into a zigzag stays its
   own part); a curved leg gives the zigzag only its straight start, when that is 0.4 legs or more.
5. Any other stretch is curved when its heading changes by curve degrees or more (curveScreen with a floor), else
   straight. A straight end splits off a curve only when it is long (25 units and a quarter of the stretch), the rest
   turns 90 degrees or more and bends at once (a rainbow, an arch and an S stay one curved part).
6. A start more than 8 units from `start` adds a straight lead from it. Parts past maxParts join the last one.

Tested (levels-and-pathways handoff.md, Refine round 2) with 77 shapes (the round 1 table, the exit check's shapes,
wobbly lines) each drawn side to side, front to back both ways and on both slants: real mouse drags at 1280x720,
1366x768 and 760x900, and a node run of three jittered hands on four stage sizes. Known edges: a very gentle wave
(amplitude 15 over 80 units) can read straight when drawn shakily, and on the smallest stages (375 wide, 680x425)
a shape squeezed to fit reads less reliably (handoff.md has the numbers).

## Colors

The engine takes colors as options (it has no stylesheet). Ribbon colors are fixed for meaning, and every level also
has its own pattern and icon so color is never the only cue:

| Level | Color | Pattern | Icon (tools draw it) |
|---|---|---|---|
| High | #1565c0 | tiptoe prints along a thin line | cloud |
| Middle | #2e7d32 | solid band | table |
| Low | #b45309 | wide band with diagonal stripes (#f6cf8f) | grass tuft |
| Plain (hidden level) | #c08a00 | gold dashed band, dotted center | none |

Studio colors (`colors` option): wall #eef6f5, mirror #dbe9ee, wood #e9d3b0 to #d9b98a, barre #a8794a.

## What each tool brings (its own)

| Tool | Grade | Engine parts | Its one idea (not shared) |
|---|---|---|---|
| levels-and-pathways | K-2 | studio floor, one dancer plus a mirror image, `level`, 4 gaits, ribbon trails with `paintIn`, `transform` and `styleAt`, `readPath`, `music`, `counts` | the floor keeps a record of the pathway; levels by color, pattern and icon. Its own six moves (with high and low keyframes on the floor), the Mystery rounds and the per-part levels of a drawn path are in the tool |
| dance-pattern-puzzle | 3-5 | poses, `phrase`, `clock`, `music` | patterns hidden in a sequence of move cards |
| choreography-board | 6-8 | phrases, `dyn`, `side`, offsets (canon), `stage` view | phrases on a timeline, revised with choreographic devices |
| dance-styles-explorer | 9-12 | `square` and `void` views, exposure trails | styles, traces and critique |

## Rules for siblings

- The figure, the floor, phrases, the clock and trails come from the engine. A sibling adds its own moves (as pose
  keyframes with `high` and `low` versions), its own music tracks and its own questions.
- New engine features go into the engine and this file in the same change, keeping existing calls working.
- One run at a time: stop the old clock, play, music and voice before a new action (levels-and-pathways keeps a run
  token; every await checks it).
- Call `floor.resize` from the tool's relayout at real pixel size, then redraw anything placed in floor units.

## Verification (2026-10-28, Chrome, levels-and-pathways frames)

- All 27 poses, the 8 gaits at four phases and all four views (with a leap phrase, a ribbon and an exposure trail)
  rendered with no console errors.
- Refine round 1: a front-view contact sheet of the six moves at three levels (A and the count-8 freeze B): every low
  keyframe sits, kneels on the heels or lies (head 0.15 to 0.62), every middle one stands (0.8 to 1.02).
- The six moves at three levels (36 keyframes) each read as their own shape; Up and down ran 40 counts in the order
  high, middle, low, middle, high; a level tap during a move took effect on the next count.
