# Rigid Motion Twins

## One idea
At a fossil trackway every level has a footprint pressed in the rock and a plaster cast of it somewhere else on the
grid: move the cast onto the print with slides, turns and flips, in as few moves as you can, and the moves you used
are written out as functions on points, which is the proof that the two are congruent; later levels ask which moves
map a shape onto itself, catch a cast that only looks like a twin, and show why SSS, SAS and ASA work but SSA does
not.

## Not like
- dance-floor-moves (gr 8 studio, same family): a free routine of moves with dilations, set to music. Here every level has one target, dilations are not allowed, and the move list is a proof.
- coordinate-proof-lab (gr 10, this group): proves shape names by measuring. Here congruence is proved by motion, not by numbers.
- proof-blocks, now Proof Tower (gr 10, this group): written proofs with reasons; its level 6 cites ASA as a reason card. Here ASA itself is shown to follow from rigid motions.
- shadow-measure (gr 10, this group): similar triangles, sizes change. Here sizes never change.
- image-transformer (gr 12 studio): transformations as matrices on images. Here plain moves on a grid, no matrices.

## Who and how
- Grade 10, Geometry, module Rigid Motions and Congruence. Students drive, own laptops or pairs. 15 to 40 minutes.
- Topic line: "rigid motions and congruence".
- Standards (module): G-CO.A (transformations as functions; symmetries of polygons; definitions of rotation,
  reflection and translation; drawing images and sequences), G-CO.B (congruence by rigid motions; corresponding
  parts; ASA, SAS and SSS from rigid motions).
- CCSS clusters: Tracks levels 1 to 8 serve G-CO.A.2, A.4, A.5 and B.6; level 9 serves A.3; level 10 serves B.6;
  Criteria serves B.7 and B.8.
- tool.json: driver "students", minutes "15-40", modes ["Tracks", "Criteria"], grades_label "Grade 10".

## Screens and modes
Header (kit, 9-12 theme): title "Rigid Motion Twins", subtitle "Move the cast onto the print." Modes `Tracks`
(opens first), `Criteria`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: square plane left (x and y from −10 to 10 on the painted sandstone, art: rmt-sandstone), panel right (level
list under a banner of the trackway, art: rmt-trackway; move bar; move list). Under 1000 px wide the panel goes under the plane, move bar first. Under 900 px tall the level list becomes a
dropdown so the plane and the move bar stay in view.

### Tracks (puzzle)
- Focus: the plane with the cast and the print, the largest thing on screen, centered in the stage; the move being
  set up (slide arrow, turn center and arc, flip line) is drawn on it in the scene ink.
- The print (target) is a code polygon filled with the dark mud texture (art: rmt-mud) and a dashed outline, sunk
  in the rock; the cast (source) is a code polygon filled with the plaster texture (art: rmt-plaster) with its
  vertices labeled A to I. The texture moves, turns and mirrors with the polygon, so a flip shows on the plaster. Move bar: `Slide` (drag the arrow from any vertex; its tip snaps to lattice points), `Turn` (place
  the center on a lattice or half point, pick 90°, 180° or 270° counterclockwise, or 15° steps on level 9), `Flip`
  (tap two lattice points to set the line). `Undo`, `Start over`.
- Each move animates (slide straight, turn along an arc, flip as a fold over the line; instant with Motion off)
  and is added to the move list as a name and a function: "turn 90° about (0, 0): (x, y) → (−y, x)".
- When the cast lands exactly on the print: "Twins!", the moves become a proof card ("The cast maps onto the print
  by T then R. Slides, turns and flips keep every length and angle, so the two footprints are congruent: A ↔ A′,
  B ↔ B′, ...") and the level shows one star, or two if you matched the fewest moves. If several moves were used,
  the card also says what single motion they make, when there is one ("Your three moves are one turn of 90° about
  (0, 0)").
- `Measure`: tap any two vertices of either shape to see their distance (exact).
- Level 9 (Self-twins): no print; a shape sits on the grid and you hunt every move that lands it on itself (not
  counting doing nothing). Found moves fill a tray: "Found 3 of 3". On this level `Flip` and `Turn` handles also
  snap to the shape's vertices, edge midpoints and center, so the hexagon's slanted mirror lines (30°, 60°, 120°,
  150°), which pass through no second lattice point, can be set.
- Level 10 (Not twins?): `Not twins` button beside the move bar. The right call is Not twins, proved with Measure.
### Criteria
- Focus: the two triangles on a ranger's field notebook page (art: rmt-notebook), center stage, with the step's
  sentence directly under them.
- Three cards, `SSS`, `SAS`, `ASA`. Each shows △ABC and △DEF with the given equal parts marked. `Next step` runs
  the standard three moves one at a time: slide A onto D, turn about D until AB lies on DE, flip over DE if C is on
  the wrong side. After each step one sentence says why the next part must land (SSS: "C is the one point that is
  √10 from D and √18 from E on this side"; SAS: "the angle fixes the ray, the length fixes the point"; ASA: "two rays
  from D and E cross at one point").
- A fourth card, `SSA?`, tries the same with a 40° angle, AB = 5 and BC = 4: two different triangles appear, both
  fitting, so SSA is not a rule. A fifth, `AAA?`, shows two triangles with the same angles and different sizes.

## Content
The cast and the print are the same three-toed footprint: F = (1,0) (2,0) (2,2) (4,3) (2,3) (2,5) (1,3) (0,3)
(1,2), a simple polygon of area 5.5 with no symmetry, so every landing has exactly one vertex match.
Levels (cast = F slid by the offset; print = the cast after the listed motion; all coordinates exact):
1. Cast offset (−8, −4). Slide ⟨9, 5⟩: (x, y) → (x + 9, y + 5). Print (2,1) (3,1) (3,3) (5,4) (3,4) (3,6) (2,4)
   (1,4) (2,3). Fewest 1.
2. Cast offset (1, 1). Turn 90° about (0, 0): (x, y) → (−y, x). Print (−1,2) (−1,3) (−3,3) (−4,5) (−4,3) (−6,3)
   (−4,2) (−4,1) (−3,2). Fewest 1.
3. Cast offset (−6, −2). Flip over x = 0: (x, y) → (−x, y). Print (5,−2) (4,−2) (4,0) (2,1) (4,1) (4,3) (5,1)
   (6,1) (5,0). Fewest 1.
4. Cast offset (−6, 1). Turn 180° about (−1/2, 1/2): (x, y) → (−1 − x, 1 − y). Print (4,0) (3,0) (3,−2) (1,−3)
   (3,−3) (3,−5) (4,−3) (5,−3) (4,−2). Fewest 1 (needs a half-point center).
5. Cast offset (−8, 1). Flip over y = 0 then slide ⟨5, 0⟩: (x, y) → (x + 5, −y), a glide reflection. Print (−2,−1)
   (−1,−1) (−1,−3) (1,−4) (−1,−4) (−1,−6) (−2,−4) (−3,−4) (−2,−3). Fewest 2 (no single slide, turn or flip).
6. Cast offset (3, −7). Flip over y = x: (x, y) → (y, x). Print (−7,4) (−7,5) (−5,5) (−4,7) (−4,5) (−2,5) (−4,4)
   (−4,3) (−5,4). Fewest 1.
7. Cast offset (−7, −6). Turn 270° about (1, −1): (x, y) → (y + 2, −x). Print (−4,6) (−4,5) (−2,5) (−1,3) (−1,5)
   (1,5) (−1,6) (−1,7) (−2,6). Fewest 1.
8. Cast offset (−6, −7). Flip over y = −x + 2: (x, y) → (2 − y, 2 − x). Print (9,7) (9,6) (7,6) (6,4) (6,6) (4,6)
   (6,7) (6,8) (7,7). Fewest 1.
9. Self-twins (find all, not counting doing nothing): rectangle (−3,−2) (3,−2) (3,2) (−3,2): 3 (flip x = 0, flip
   y = 0, turn 180°); square with corners (±2, ±2): 7; parallelogram (−3,−1) (1,−1) (3,1) (−1,1): 1 (turn 180°
   about the origin, no flip); isosceles trapezoid (−3,−1) (3,−1) (1,2) (−1,2): 1 (flip x = 0); regular hexagon
   centered at the origin, radius 3, a vertex at (3, 0): 11 (5 turns, 6 flips), with 15° turn steps.
10. Not twins?: the print is F with the right toe at (5,3) instead of (4,3), shown after an offset. The cast's
   (2,2)-to-toe distance is √5 ≈ 2.24, the print's √10 ≈ 3.16; no rigid motion changes a length.
Criteria: △ABC A(0,0) B(4,0) C(1,3) and △DEF D(6,1) E(6,5) F(9,2); AB = DE = 4, AC = DF = √10, BC = EF = √18 = 3√2.
Step 1 slide ⟨6, 1⟩: B → (10,1), C → (7,4). Step 2 turn 90° about D: B → (6,5) = E, C → (3,2). Step 3 flip over
x = 6: C → (9,2) = F. SSA card: angle A = 40°, AB = 5, BC = 4: C = 53.46° with AC = 6.21, or C = 126.54° with
AC = 1.45.

## Interactions in detail
- Coordinates are exact (integers and halves; the hexagon uses floats compared within 1e-9). A landing needs every
  cast vertex on its matching print vertex; landing on the print with the wrong match cannot happen with F.
- Fewest counts slides, turns and flips as one move each. Any landing sequence passes; extra moves cost only the
  second star.
- A move that would push any vertex off the plane is refused with "That would leave the rock." Turn angles other
  than the listed ones are not offered (except 15° steps on level 9's hexagon).
- Not twins pressed on a true twin: "Measure first. Every length here has a match." Trying moves on level 10 is
  allowed; after five moves a hint suggests Measure.
- Criteria steps can go back and forth; the turn and flip use the same animation as Tracks.
- Live while anything moves: a move animation (about 0.6 s) or a Criteria step finishes at once when the student
  taps Undo, starts the next move, changes level or card, or switches mode; nothing waits for an animation.
- Keyboard: Tab to the move bar; arrows move a slide tip or a center one lattice step (Shift for a half step);
  Enter applies. The move list is a live region read aloud with Read.
- Progress (stars per level) is saved in localStorage with a `Clear progress` button; nothing else is saved.
- `window.__tool = {state, setMode, level(n), slide(dx, dy), turn(deg, cx, cy), flip(x1, y1, x2, y2), undo(),
  landed(), notTwins(), measure(a, b), symmetriesFound(), criteria(card, step)}`.

## Look
Accent `--brand #efe6d2` (plaster of a fossil cast), `--brand-ink #10161f`. Plane on the sandstone image
(lightened or darkened in the build to average `#c9a57a`), grid lines `#2a1d12` at 25%; the print the mud image
darkened to average `#5b4636` with a dashed `#2a1d12` outline; the cast the plaster image (average near the accent)
with a `#2a1d12` outline and labels; Criteria on the notebook image (average near `#efe9da`) with the same ink; motion lines (slide arrow, turn arc, flip line) in
`#2a1d12`, 2 px.
Contrast (computed): brand on --panel 13.95:1, on --sec-bg 13.21:1; brand-ink on brand 14.63:1; scene ink `#2a1d12`
on sandstone 7.13:1; plaster on the print fill 7.13:1; print fill on sandstone 3.85:1 (a graphic, needs 3:1). Paler
and greyer than polynomials-as-numbers' #f3e3a0 and function-family-reunion's #f7c59f; warmer than the silver
#c7d2de.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 5 images. One style: sunlit field geology, painted.
- rmt-sandstone: a flat slab of pale rippled sandstone seen straight down, soft even light, fine sandy grain, smooth
  blank surface; 16:9; cutout no; people no; behind the plane, cropped square.
- rmt-plaster: a flat smooth surface of white casting plaster seen straight down, faint brush strokes and tiny air
  bubbles, soft even light, full frame; 1:1; cutout no; people no; texture clipped to the cast polygon and the
  level 9 shapes, moved with them.
- rmt-mud: a flat surface of dark damp brown mudstone seen straight down, fine cracks and grit, soft even light, full
  frame; 1:1; cutout no; people no; texture clipped to the sunken print.
- rmt-trackway: a wide riverside shelf of pale sandstone with a long line of three-toed dinosaur footprints pressed
  into it, ferns and a slow brown river beyond, low warm evening sun, painted illustration; 16:9; cutout no; people
  no; the banner over the level list (cropped 4:1) and the first-load card.
- rmt-notebook: an open field notebook page of pale cream graph paper seen straight down, faint blue grid, a soft
  shadow at the spine, blank page, soft even light; 4:3; cutout no; people no; Criteria background.
Drawn in code: the plane grid and axes, every polygon outline, labels, slide arrows, turn arcs, flip lines, ghosts,
the orientation marker, Criteria's triangles and marks, preview.svg.

## Voice
Bank voice `gravel-ranger` (Algenib), style "Say warmly with a gravelly voice, like an old ranger at a dinosaur
trackway". Not used by its math neighbors or the other specs in this batch (fire-lookout-triangles, grade 12, uses
it and is not a neighbor). `Curio.voice`, `scope: () => state.mode + ':' + state.level`. The move list and proof
cards are read on screen; Read speaks the hint.
- wTracks (how, Tracks welcome; stale on the first move): "Tap Slide, Turn or Flip, then set the move on the rock. Move the cast until it fits the print."
- wSelf (how, level 9 opens; stale on the first found move): "No print this time. Tap Turn or Flip and find every move that lands the shape on itself."
- wNot (how, level 10 opens; stale on the first Measure or Not twins): "Is this cast a true twin? Tap Measure, then tap two corners of each footprint."
- wCriteria (how, Criteria welcome; stale on the first step): "Pick a card, then tap Next step and watch the triangle land, one move at a time."
- twins (event, a cast lands; stale on the next level): "Twins. That move list is your proof."
- fewest (event, a landing in the fewest moves; stale on the next level): "And in the fewest moves. Clean work."
- notTwins (event, Not twins correctly called; stale on the next level): "Good eye. One length doesn't match, so no move can fix it."
- ssa (event, the SSA card shows both triangles; stale on card change): "Two triangles fit the same clues. SSA can't decide."

## Family engine
transformations (`kit/transformations.js`, inlined after `kit:curio` and `kit:graphing`; built on the graphing
`Plane`). This spec holds the full description for the family; dance-floor-moves (gr 8 studio, 8.G.A.1 to A.4)
reuses it. Image-transformer (gr 12) uses matrices and is not in the family.
- `Motion`: `Motion.translate(dx, dy)`, `.rotate(deg, [cx, cy])`, `.reflect([x1, y1], [x2, y2])`, `.dilate(k,
  [cx, cy])`, `.glide(line, d)`. Each is an affine map with `apply(p)`, `applyPoly(poly)`, `invert()`,
  `then(m)` (compose), `fnText()` ("(x, y) → (y + 2, −x)", true minus sign), `name()` ("turn 270° about (1, −1)"),
  `isRigid`, `keepsOrientation`. Exact for lattice and half-lattice data and multiples of 90°; floats otherwise.
- `classify(m)` → `{kind: 'identity' | 'slide' | 'turn' | 'flip' | 'glide' | 'dilation' | 'similarity', params}`,
  naming the single motion a sequence makes.
- `matches(polyA, polyB, {tol})` → the vertex correspondence (list of index pairs) or null; `sameShape(a, b)` by
  side and diagonal lengths.
- `symmetries(poly, {angleStep, centers})` → every motion that maps the polygon onto itself.
- `animate(handle, motion, {ms, style: 'straight' | 'arc' | 'fold'})` → a promise; instant with Motion off; leaves a
  faint ghost of the pre-image.
- `MoveBar(container, plane, {moves: ['slide', 'turn', 'flip', 'dilate'], angles, angleStep, centerSnap, onMove})`:
  the move picker with on-plane arrow, center and line handles (44 px targets, keyboard steps).
- Fixed by the engine: animation styles, ghost look, prime labels for images (A′), the function-notation format,
  the orientation marker (a small curved arrow inside the shape that turns over after a flip).
- What each sibling feeds it: dance-floor-moves: all four moves including dilate, free sequences with no target,
  `fnText` for the routine's "rules" replay; music timing stays in that tool. This tool: rigid moves only, targets
  with `matches`, `classify` for the "your moves are one turn" line, `symmetries` for level 9, fewest-move counts.

## Sources
- G-CO text: Common Core State Standards for Mathematics, High School Geometry, Congruence, https://www.thecorestandards.org/Math/Content/HSG/CO/
- Grade 8 sibling codes: CCSS 8.G.A, https://www.thecorestandards.org/Math/Content/8/G/
- Every isometry of the plane is a translation, rotation, reflection or glide reflection: H. S. M. Coxeter, Introduction to Geometry, 2nd ed., Wiley, 1969, chapter 3 "Isometry in the Euclidean plane".
- Glide reflection: Weisstein, Eric W., "Glide Reflection", MathWorld, https://mathworld.wolfram.com/GlideReflection.html
- SSS, SAS and ASA: Euclid's Elements I.4, I.8 and I.26, D. E. Joyce edition, Clark University, https://mathcs.clarku.edu/~djoyce/java/elements/bookI/bookI.html
- Footprint, levels and the SSA case are made up for this tool; every coordinate and value above was recomputed exactly in Python (2026-10-27).
- Checks run (Python, exact integers, 2026-10-29): F has area 5.5 and no symmetry (its distance table matches itself
  only under the identity, so every landing has one vertex match). All eight prints equal the listed motion applied
  to the offset cast; every cast and print lies inside −10 to 10 and they never overlap; levels 3, 5, 6, 8 reverse
  orientation, the others keep it. Level 5's flip y = 0 step stays on the rock, and the only flip that could send A
  to A′ does not land the cast, so it needs two moves. A 180° turn about (0, 0) does not land level 4. Level 9 by
  brute force (turns in 1° steps, mirror lines in 0.5° steps): rectangle 3, square 7, parallelogram 1 (a turn),
  trapezoid 1 (a flip), hexagon 11; four hexagon mirror lines pass through no second lattice point, so the handles
  now also snap to the shape's vertices, edge midpoints and center on level 9. Level 10: √5 = 2.24 and √10 = 3.16.
  Criteria: squared sides 16, 10, 18 on both triangles; the three steps send B to (10, 1), (6, 5), (6, 5) and C to
  (7, 4), (3, 2), (9, 2). SSA: C 53.46° with AC 6.21, or 126.54° with AC 1.45.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Level 1: one slide ⟨9, 5⟩ lands the cast, shows "Twins!", two stars, and the move list reads (x, y) → (x + 9, y + 5).
2. Level 4 lands with a turn of 180° about (−1/2, 1/2); a 180° turn about (0, 0) does not land.
3. Level 5 can't land in one move; flip y = 0 then slide ⟨5, 0⟩ lands and the card names a glide reflection.
4. Level 2 landed by three moves (any that work) gives one star and names the single motion "turn 90° about (0, 0)".
5. Level 9: the square shows "Found 7 of 7" only after all four flips and three turns; the parallelogram has no flip.
6. Level 10: Measure shows √5 and √10 for the matching toe segments; Not twins wins the level.
7. Criteria SSS: after three steps C lands on (9, 2); SSA shows two triangles with AC 6.21 and 1.45.
8. Focus: at 1366x768 and 1000x625 the plane with the cast and print is the largest thing in Tracks, and the two
   triangles in Criteria.
9. Tap while it plays: during a turn or flip animation, Undo, the next move, a level change and a mode switch act at
   once and the cast ends exactly where the move list says.
10. Level 9 hexagon: all six mirror lines can be set with the snapped handles, and "Found 11 of 11" appears.
11. Keyboard alone can finish levels 1 to 3; every size in STANDARDS.md keeps the plane and the move bar visible without page scrolling.
12. Stars survive a reload; Clear progress empties them. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- none.
