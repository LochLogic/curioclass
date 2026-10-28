# Stage family

Tools where actors, set pieces and lights are placed on a stage seen from above, then read from seats in the house:
who is hidden behind whom, who is upstaged, what each seat sees, and where the eye goes. Director's notes are checked
from every seat at once.

Engine: `kit/stage.js` (one global `Stage`). Include it after the kit with `<script src="kit:stage"></script>`.
First built for stage-blocker (6-8, 2026-10-28); director-s-chair (9-12) adds five more stage shapes and reuses
everything here. Sizes, thresholds and focus weights are stage-blocker's own choices (a rough guide, said on screen),
not facts.

## World frame

- Meters. x runs from house left to house right (x = 0 on the center line). Stage right, the actor's right facing
  the house, is negative x. y runs upstage from the apron edge (y = 0); the house is at negative y. z is up from the
  stage floor; the house floor is at z = -stageH.
- Facing is absolute, in degrees: 0 faces straight out to the house (-y), 90 faces house right (+x, the actor's
  left), 180 faces upstage, 270 house left. Turning left adds 45. (The spec's "0 = toward seat B3" is the same
  direction for a centered seat; body positions are always measured to the actual seat.)
- A seat's eye is at `seat.eye - stageH` in this frame (eye heights are given from the house floor).

## Houses: `Stage.house(def)`

Fills in defaults and derived values, and returns the house. Every field:

| Field | Default | Meaning |
|---|---|---|
| `id`, `name` | | names for the tool |
| `outline` | required | the stage floor polygon `[[x, y], ...]` |
| `stageH` | 0 | stage floor height above the house floor (m) |
| `areas` | `[]` | `[{id, label, row: 'down'\|'center'\|'up', poly}]`: lights, the `at` note and the focus row bonus |
| `spots` | `{}` | `{name: [x, y]}`: spike marks drawn on the plan |
| `entrances` | `[]` | `[{id, label, at, quiet}]`: `at` is one point `[x, y]` or a list; `quiet: true` draws arrows without words (when wings are labeled) |
| `levels` | `[]` | `[{id, poly, h}]`: raised floors that are part of the house (bridges, platforms built in) |
| `blockers` | `[]` | `[{id, poly, h, z0, hideInPlan, color}]`: solid prisms from z0 (default 0) to h: proscenium walls, pillars, a header (`z0` above the opening, `hideInPlan` so the plan does not show it) |
| `wings` | `[]` | `[{id, label, poly, labelAt}]`: off-stage floor drawn on the plan and the house view; the label sits at the wing's upstage end, or at `labelAt: [x, y]` |
| `seats` | `[]` | `[{id, label, x, y, eye, planAt, tag, tagSide}]`: `planAt: [[x, y]]` draws a seat closer on the plan than it is (a balcony, or every row so the stage gets more of the plan; rays then run along the true line from where it crosses the drawn row, with a faint dotted link to the dot); `tag` a label beside the dot; `tagSide: 'left'` |
| `frame` | `'open'` | `'proscenium'` \| `'thrust'` \| `'arc'` \| `'open'`: today only `'proscenium'` changes anything (the plan draws the curtain line); the house view does not read it (see Not yet) |
| `light` | `'areas'` | `'areas'` (the lights panel works), `'daylight'` or `'even'` (fixed full light; the tool says why) |
| `spotR` | 1 | the spot's radius (m) |
| `focusSeats` | the middle seat | seats a `focus` note is checked from (stage-blocker: A3, B3, C3) |
| `upSeat` | middle of focusSeats | the seat upstaging is judged from (B3) |
| `look` | center of outline, z 1.2 | the point every seat's camera aims at |
| `curtainY` | null | the curtain line, dashed on the plan (proscenium) |
| `opening` | none | `{x0, x1, y, h}`: the proscenium opening (house view framing and the curtain line) |
| `backWall` | from the outline | `{y, x0, x1, h}`: the back wall in the house view (always drawn) |
| `frontFace` | true | false leaves out the apron's front face in the house view (drawn when `stageH > 0`) |
| `fitPts` | outline and opening | `[[x, y, z], ...]`: what the seat camera must frame (stage-blocker frames the playing area to 3.4 m, so figures read larger) |
| `planBox` | everything drawn plus a margin | `{x0, x1, y0, y1}`: the plan's extents (m) |

Derived: `box` (outline bounds), `planBox`, `seatById`.

## Set pieces: `Stage.addPieces({type: def})`

Registers catalog entries (shared across the page). A piece in a snapshot is `{id, type, x, y, rot}` (rot in degrees,
90 steps in stage-blocker). Catalog fields: `label`, `short` (plan label), `w` (along x before rotation), `d` (along
y), `h`, `color` (house view), `plan` (plan fill), `sit` (actors dropped on it sit, and it does not push them away),
`standable` (a level: actors stand on it, head height plus `h`), `opening` (a gap in the middle up to `h - lintel`, a
door flat), `lintel` (default 0.3), `entrance` (its entrance id, at the front of the opening), `entranceLabel`,
`round` (a cylinder of diameter `w`), `parts: [{w, d, ox, oy, z0, z1, round, color}]` (several solids, for example a
tree's trunk and canopy). `Stage.solids(piece)` and `Stage.footprint(piece)` give the geometry.

## Snapshots, cast and beats

- Actor: `{id, name, initials, color, mask: null | 'full' | 'half', x, y, facing, pose: 'stand' | 'sit' | 'kneel',
  on: level id or null, off: bool, wing: entrance id while off stage, sitOn: piece id or null}`. `dragging: true`
  while a drag is live (the plan draws it at x, y even when off stage).
- Snapshot: `{cast, pieces, lights: {areaId: 0 | 1 | 2}, spot: null | {x, y}}`.
- Beat: `{speaker, to: id | 'all' | null, line, dir, notes, snap, changed}`.
- `Stage.carry(beats, from)`: every later beat that was never changed becomes a copy of the beat before it.
  `Stage.edit(beats, i, fn)`: runs `fn(beats[i].snap)`, marks beat i changed, then carries. So a change in beat 2
  reaches beats 3 on until a changed beat, and never reaches beat 1.
- `Stage.POSES = {stand: 1.6, sit: 1.2, kneel: 0.9}`: head heights (plus the level's height). Bodies are 0.25 m
  radius cylinders up to the head top (head radius 0.12).

## Analysis

```js
Stage.bodyPos(actor, seat)          // 'full front' (< 22.5 deg) | 'one-quarter' (< 67.5) | 'profile' (< 112.5) | 'three-quarter' (< 157.5) | 'full back'
Stage.sight(snap, house, seat)      // {cast: {id: {blocked: 0..5, status: 'clear' | 'partly' | 'hidden', by: [ids]}}, pieces: {id: {seen, by}}}
Stage.focus(snap, beat, house, seat, weights, prevSnap)   // {id: {score (null when hidden), reasons: ['+3 speaking', ...], hidden, parts: {term: value}, why: {term: text}}}
Stage.leader(focusResult)           // {id (null on a tie), top, tie, tied: [ids]}
Stage.upstaged(snap, beat, seat, house)   // {speaker, partner, gap, pos} or null
Stage.check(notes, beats, house, {weights, names})        // per note {met, why, seats}
Stage.free(snap, house, id, x, y, {r, gap})               // {x, y, on, sitOn}: the nearest free spot
Stage.areaOf(house, x, y), Stage.onStage(house, x, y), Stage.levels(snap, house), Stage.lightAt(snap, house, x, y),
Stage.inSpot(snap, house, x, y), Stage.lit(snap, house, actor), Stage.entrancePts(snap, house),
Stage.nearestEntrance(snap, house, x, y), Stage.headZ(actor, snap, house), Stage.angleTo(actor, x, y),
Stage.initials(name) (first letters of the first two words, or the first two of one word; letters and digits only, so
"O'Neil" gives On), Stage.inPoly(poly, x, y), Stage.clone(o)
```

- **Sightlines.** Five face points: head center, 0.1 m left and right across the sight line, 0.1 m up and down.
  Each ray from the seat's eye is tested (Cyrus-Beck) against other actors' cylinders, every piece solid and the
  house blockers; the actor's own body, the piece it sits on and the level it stands on are left out. 3 or more
  blocked: hidden; 1 or 2: partly hidden. `by` lists who or what is in the way. A piece is seen when its top center
  is unblocked.
- **Focus** (`Stage.WEIGHTS`, merged with `weights`): `speak` 3; `light` [off -3, half 1, full 2] (areas houses only);
  `spot` 2; `pos` full front 2, one-quarter 1.5, profile 1, three-quarter 0, full back -1; `level` 1 (on a level);
  `standAlone` 1 (standing while every other actor sits or kneels); `row` down 1, center 0.5, up 0; `crossed` 1.5
  (moved `crossM` 0.5 m or more since the beat before, or entered); `gaze` 1 per other actor facing within `gazeDeg`
  30 deg of them; `alone` 1 (nobody within `aloneM` 1.5 m); `partly` -2; hidden: no score. `terms: [{id, fn(actor,
  ctx) -> {score, reason} | null}]` adds terms (`ctx`: snap, beat, house, seat, prev, sight); director-s-chair adds
  `chorusGaze` and `address`. A tie has no leader. `parts` and `why` are keyed by term (`speak`, `light`, `spot`,
  `pos`, `level`, `standAlone`, `row`, `move`, `gaze`, `alone`, `partly`, or a term's `id`), so a tool can name the
  biggest gap between two actors; the `focus` note's why does ("Biggest gap: Ben +2 for full light, Gran +1 for half
  light."). The light reasons read "full light", "half light", "in the dark".
- **Upstaged.** The beat's `to` partner stands 1 m or more farther upstage than the speaker, the speaker shows
  three-quarter or full back from the seat (`house.upSeat`), and the speaker is turned toward the partner (under 90
  deg). The note's why gives the fix: "Bring Ben down level with Ava, or have Ava cheat out: turn partly out to the
  house while still talking to Ben."
- **Open to the house.** Three-quarter and full back are closed. A `focus` or `notUpstaged` note fails when the actor
  is closed to a judging seat, whatever the scores say, so a check never passes an actor with their back to the
  house. Why: "From B3, Ava's back is to the house (full back). Turn Ava out to the house, at least to profile."

## Notes: `Stage.check`

Each note is `{t, beat (index), text, ...}`; `Stage.NOTE_TYPES` lists the 15 types:

| `t` | Fields | Met when |
|---|---|---|
| `see` | `a` | not hidden from any seat (partly hidden is fine) |
| `lit` | `a` | standing in a half or full area, or in the spot |
| `focus` | `a, seats?` | open (profile or better) to, and the leader from, every one of `seats` (default `house.focusSeats`) |
| `at` | `a, areas` | in one of the listed areas |
| `enters` | `a, entrance` | off stage in the beat before, on stage now, by `entrance`: the wing or Door they waited in during the beat before (`actor.wing` there), else the entrance nearest where they first stand |
| `exits` | `a, entrance` | on stage before, off now, by `entrance`: the wing they were sent to (`actor.wing`), else the entrance nearest their last place |
| `crosses` | `a, m` | moved at least m since the beat before |
| `near` / `apart` | `a, b, m` | at most / at least m apart |
| `notUpstaged` | `a, seat?` | not the upstaged speaker, and open (profile or better), from `seat` or `house.upSeat` |
| `notHiding` | `a, b` | a is not in `by` of any seat where b is hidden |
| `notFullBack` | `a, seat` | not full back from that seat |
| `onLevel` | `a, level` | standing on that level (a level id, or a piece id or type) |
| `seeProp` | `piece` | the piece (id or type) is seen from every seat |
| `group` | `ids, m, areas?` | every pair within m, and (with `areas`) every member in one of them |

Several actors in one note: `ids: [...]` on `see`, `lit`, `focus`, `at`, `crosses`, `notUpstaged`, `notFullBack`, or an
array `b` on `notHiding`, `near`, `apart`. Met when every part is met; the why joins the failed parts (each different
sentence once). A result's
`seats` lists the seats that failed (for example `["A1"]` for "Ben covers Ava from seat A1."). `opts.names` maps ids
to the names used in the whys.

## Playing a scene

```js
Stage.tween(snapA, snapB, t, tl)    // positions and facings at t, lights at tl (0..1); entrances and exits switch at the ends
const p = Stage.play(beats, view, {cross: 1200, fade: 400, reduce})
await p.beat(i)                     // 'done' | 'stopped': tweens beat i - 1 to beat i (eased); view(snap, {beat, t}) or view.update(snap, info) each frame
p.stop()
p.stopped                           // true once stopped
```

With `reduce` (default `Curio.reduce`) a beat jumps to its end but still takes the same time.

## Views

Colors come from CSS variables on the element (defaults in brackets): `--st-floor` (#1b1b1f), `--st-lines`
(#3a3a42), `--st-spike` (#e07a2e), `--st-house` (#2a2a30), `--st-seat` (#8a8a94), `--st-pool` (#ffe7b0),
`--st-wing`, `--st-label` (#c9c9d2), `--st-ink` (#111114), `--st-piece`, `--st-piece-line`, `--st-wall`,
`--st-sel` (#fff), `--st-bad`, `--st-ok`, `--st-part`, `--st-frame`, `--st-back`, `--st-dark`.

### `Stage.view.plan(el, state, opts)`: the ground plan

A top-down SVG at real pixel size, re-laid out when `el` resizes. Returns `{svg, update(state), layout(),
toWorld(px, py), toScreen(x, y), k (px per m), box, pad, last()}`. Set `view.pad = {top, right, bottom, left}` (px)
and call `layout()` to keep a corner free (stage-blocker's seat-view inset).

- `opts`: `house`, `mini` (no labels, no drag: a seat map), `pad`, `minR` (smallest token radius, px), `hitR`
  (seat hit radius, px), `seatR` (seat dot radius, m, default 0.3), `label` (aria-label), `slots(actor, snap) -> [x, y]` (where an off-stage actor waits),
  `onPick(sel, dragging)`, `onDrag(sel, x, y)`, `onDrop(sel, x, y)`, `onSeat(id)`, `onTurn(id, facing)`.
  `sel` is `{kind: 'actor' | 'piece' | 'spot', id}`.
- `state`: `snap`, `prev` (cross arrows), `beat` (upstaged tag, focus), `seat` (chosen seat), `sel`, `areas`
  (outlines and labels), `rays` (sightline rays from the seat: solid where clear, dashed amber partly, dashed red
  hidden), `focus` (a bar and score per actor, the eye on the leader), `flags` (tags: sitting, kneeling, upstaged,
  hidden or partly hidden from the seat), `weights`.
- Draws: wings and their labels, the floor, light pools (20 to 35%), the spot, areas and labels (a label gives way to
  an actor on it), walls, the curtain line, spike marks, entrance arrows (a door's arrow runs from its opening into
  the stage), pieces (labels give way to tokens), cross arrows, rays, seats (the chosen one ringed and named), actor
  tokens with initials and a facing wedge, a turn handle on the selected actor.
- Tags (`flags`) start with the actor's initials so they say whose they are ("Av sitting", "Av upstaged (from B3)",
  "Be hidden from A1"). They are placed after every token: below the token, lower, then above it, clear of other
  tags and other actors' tokens.
- Input: pointer drag (picks in order: turn handle, actor within 22 px, spot, piece (inside it, or within 22 px of a
  small piece's center), seat). Every pointerdown captures the pointer first, so a tap still lands while the plan
  redraws under it; when the tapped element was redrawn away before pointerup, the plan sends a click itself so
  page-level click listeners (the kit's first-tap welcome) still hear the tap. Snapping is the
  tool's job (`Stage.free`). Keyboard is the tool's job too (stage-blocker: arrows 0.25 m, Q and E turn, [ and ]).
- `last()`: `{actors: {id: {x, y, r, off}}, seats: {id: [x, y]}, pieces: {id: {x, y, poly}}, spot, handle, eye, k}`
  in px, for tests.

### `Stage.view.house(el, state, seat, opts)`: the seat view

A canvas perspective from one seat. Returns `{canvas, update(state, seat), layout(), last()}`.

- `opts`: `house`, `mini` (smaller tags and eye), `tags` (default `!mini`), `margin` (framing margin, default 0.06).
- `state`: `snap`, `prev`, `beat`, `focus` (draw the eye on the leader), `weights`, `fit` (optional `[[x, y, z]]`
  points to frame instead of `house.fitPts`; stage-blocker frames the actors and pieces of the whole scene, so the
  figures fill the view and the frame holds still from beat to beat).
- Camera: from the seat's eye toward `house.look`, scaled so the fit points (`fit`, else `house.fitPts`) fill the
  canvas. `Stage.view.camera(house, seat, W, H, margin, pts)` takes a seat object (from `house.seatById`, not an id)
  and returns `{E, F, R, U, s, proj([x, y, z]), clipPoly(pts)}`.
- Paint order: back wall, wings, floor, pools, then everything upstage of the blockers far to near, the blockers
  (the frame), the apron's front face, then everything downstage far to near. Actors are a rounded body and head in
  their color with initials on the chest and a face mark toward their facing; a hidden actor is a dashed ghost.
  Tags under each actor, the first line starting with the initials ("Av full back"): body position, "partly
  hidden", "in the dark", "hidden" (moved down to avoid overlaps). `last().tags` keeps the words without initials.
  Masks (`mask: 'full' | 'half'`) draw a face shape over the head.
- `last()`: `{sight, focus, leader, tags: {id: [text]}, seat, eye, figs: {id: {cx, top, bottom, w}}}`. The canvas
  carries an aria-label summarizing what the seat sees.

## Not yet

What the engine draws today is above; these are documented wishes, not built. director-s-chair's spec decides which
it needs.

- `frame: 'thrust' | 'arc' | 'open'`: the house view draws every house as a proscenium-style picture (back wall,
  wings, floor, blockers, apron face); the frame value is read only for the curtain line on the plan.
- The audience is assumed at negative y: the house view's apron face, the plan's seat tags and the "faces toward the
  house are lit most" shading all take the house to be in front (-y). Seats around a thrust or in the round would
  need these to follow each seat.
- `frontFace` is the only switch for the apron face; there is no `backWall: false` (the back wall always draws).
- Entrance arrows: a door piece's arrow runs from its opening down into the stage; a house entrance's arrow always
  points across x toward the center line (from the side it is on), so an entrance on the back wall or downstage
  edge would point the wrong way.
- No path within a beat: `Stage.play` tweens straight from one snapshot to the next, through pieces and other
  actors. A cross around a table needs an extra beat.

## Fixed by the engine, chosen by the tool

The engine fixes the frame, the geometry, the five body positions, the sightline test and the note types. The tool
chooses its house(s), catalog, scenes, notes, weights (stage-blocker uses the defaults), colors, layout, voice, and
everything about placement rules (snapping, wing slots, what a drop on a chair does).
