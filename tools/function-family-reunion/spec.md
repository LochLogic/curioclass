# Function Family Reunion

## One idea
Ten parent functions hang on a family photo wall, and every relative at the reunion is one parent after the same four
moves, g(x) = a f(b(x - h)) + k: drag the relative's home point and stretch point (or use one slider per parameter)
and watch each parent point (p, q) land at (p/b + h, aq + k), while a key-features card (domain, range, asymptotes,
intervals, symmetry) rewrites itself and a mirror cousin shows the inverse.

## Not like
- rollercoaster-polynomials (gr 11, graphing, built): builds a polynomial from its zeros. Here no zeros are placed; any of ten parents is moved by four parameters.
- graph-story-lab (gr 9, graphing): labels key features of real-world graphs. Here the features are computed live for a whole family as the parameters move, and the graphs are pure functions.
- launch-pad (gr 9, graphing): one quadratic as a projectile. Here the quadratic is one parent of ten.
- intersection-quest, two-trains, ski-slope-designer (graphing): lines and systems. Here lines appear only as the identity parent.
- undo-machine (gr 11, puzzle): inverses as machine chains. Here the inverse is the reflection across y = x, with the domain restriction it sometimes needs.
- polar-rose-studio and zoom-to-the-limit (this group): polar curves; rates at a point. Neither moves a parent function.

## Who and how
Grade 12, precalculus (Functions and Their Graphs). Students drive, 20 to 40 minutes. Explore first: the photo wall
opens; any parent opens a live plane.
Topic line: "parent functions and transformations".
Standards: AP-PRECALC.U1 (polynomial and rational parents, asymptotes, transformations 1.12 to 1.14), AP-PRECALC.U2
(exponential and log parents, inverses 2.7 to 2.9), F-IF.C (key features from different representations, comparing two
functions), F-BF.B (F-BF.B.3 effect of k, kf(x), f(kx), f(x + k), even and odd; F-BF.B.4 inverses).
CCSS per mode: Reunion F-BF.B.3 and F-IF.C.7; Mirror cousin F-BF.B.4; Who's who F-BF.B.3 and F-IF.C.9.
tool.json: driver "students", minutes "20-40", modes ["Reunion", "Mirror cousin", "Who's who"].

## Screens and modes
Header (kit, 9-12 theme): "Function Family Reunion", small line "Ten parents, endless relatives." Modes `Reunion`,
`Mirror cousin`, `Who's who`; kit `Motion`, `Sound`, `Read`.

Stage, top to bottom: the photo wall strip (art: reunion-wall behind ten portrait-frame cutouts; each frame holds a
mini graph of its parent drawn in code on the frame's blank mat, with the name on a plate under it in code), then the
graphing plane (x and y from -10 to 10, equal scale, grid 1, labels 2), which takes at least 70 percent of the stage
height and the full stage width. The wall strip is short (about 90 px at 1366x768, 64 px in the 680x425 preview) and
scrolls sideways when it does not fit. The chosen parent is drawn faint (`--gr-1` at 35 percent, solid) and the
relative bold (`--brand`, dashed pattern of series 2 so color is not the only cue). Two handles on the relative: the
home point (a small cross at (h, k)) and the stretch point (a ring at the image of the parent's key point, Content).
The chosen portrait lifts slightly and gets an accent outline.

### Reunion (explore, default)
Focus: the plane with the parent, the bold relative and its two handles, center stage and largest. The features card
sits in the panel, never over the plane.
- Tap a portrait to bring that parent and a relative (starting equal to the parent: a = 1, b = 1, h = 0, k = 0).
- Panel "Moves": four engine sliders with number boxes: a (vertical stretch and flip, -4 to 4, step 0.25, never 0),
  b (horizontal squash and flip, -4 to 4, step 0.25, never 0), h (shift right, -6 to 6, step 0.5), k (shift up, -6 to 6,
  step 0.5). Each slider's label says what it does in words ("a = -2: stretched x2 tall and flipped upside down").
- Equation: "g(x) = a f(b(x - h)) + k" with the numbers and with the parent written out, e.g. "g(x) = -2(0.5(x - 3))² + 1",
  and a simplified line when it is cleaner ("= -0.5(x - 3)² + 1").
- "Where points land" table: three parent key points (p, q) and their images (p/b + h, aq + k).
- "Key features" card: domain, range, x-intercepts, y-intercept, asymptotes, increasing and decreasing intervals,
  end behavior, symmetry (even, odd or neither). All update live.
- `Add to the photo`: freezes the current relative as a labeled faint curve (up to 4) so several relatives can be
  compared on one plane (F-IF.C.9); `Clear photo`.
- Dragging the home point sets h and k (snaps 0.5). Dragging the stretch point sets b from its x and a from its y
  (each rounded to the 0.25 step; values that would make a or b 0 are skipped).

### Mirror cousin
Focus: the plane with the relative, the dotted line y = x and the cousin (the reflection), center stage.
- If the relative is one-to-one, the cousin is labeled "inverse function" with its formula (Content).
- If not (square, absolute value, reciprocal square), the reflection is drawn but labeled "not a function: it fails
  the vertical line test", and a button `Keep the right half` restricts the relative to x ≥ h (x > h for the reciprocal
  square); the cousin then becomes a function with its formula.
- A point probe: tap the relative to drop a pin at (x, y); its mirror pin appears at (y, x) with both coordinates.

### Who's who (optional)
Focus: the plane with the mystery guest's curve and the student's relative over it, center stage; the guest's
name-badge card sits at the top of the panel.
Picker `Guest 1` to `Guest 10`. A mystery relative is drawn (no equation) and its card shows a blank name badge (art:
name-badge) with "Guest 3" written on it in code. The student picks its parent from the wall and sets the four moves
until their relative lies on it. Live check: "Same curve" when the curves agree (see checks). Then the badge shows the
guest's name and one equation (others may also be right: "Your moves give the same curve.").

## Content
Parents (key points for the table; the stretch point is the image of the second one):
| Parent | f(x) | Key points | Domain | Range | Asymptotes |
|---|---|---|---|---|---|
| Line | x | (0, 0), (1, 1), (-1, -1) | all | all | none |
| Square | x² | (0, 0), (1, 1), (-1, 1) | all | y ≥ 0 | none |
| Cube | x³ | (0, 0), (1, 1), (-1, -1) | all | all | none |
| Absolute value | abs(x) | (0, 0), (1, 1), (-1, 1) | all | y ≥ 0 | none |
| Square root | √x | (0, 0), (1, 1), (4, 2) | x ≥ 0 | y ≥ 0 | none |
| Cube root | ∛x | (0, 0), (1, 1), (-1, -1) | all | all | none |
| Reciprocal | 1/x | (1, 1), (-1, -1), (2, 0.5) | x ≠ 0 | y ≠ 0 | x = 0, y = 0 |
| Reciprocal square | 1/x² | (1, 1), (-1, 1), (2, 0.25) | x ≠ 0 | y > 0 | x = 0, y = 0 |
| Exponential | 2ˣ | (0, 1), (1, 2), (-1, 0.5) | all | y > 0 | y = 0 |
| Logarithm | log₂ x | (1, 0), (2, 1), (0.5, -1) | x > 0 | all | x = 0 |
Home point (h, k) is the image of the origin for every parent (for the reciprocals, the meeting of the asymptotes; for
the exponential, where the asymptote y = k meets x = h; for the logarithm, where x = h meets y = k).

Feature rules for g(x) = a f(b(x - h)) + k (exact, used instead of sampling):
- Domain: square root b(x - h) ≥ 0 (x ≥ h if b > 0, x ≤ h if b < 0); logarithm b(x - h) > 0; reciprocals x ≠ h;
  otherwise all real numbers.
- Range: parents with range y ≥ 0 or y > 0 map to y ≥ k (or y > k) when a > 0 and y ≤ k (or y < k) when a < 0;
  reciprocal y ≠ k; otherwise all.
- Asymptotes: vertical x = h (reciprocals, logarithm); horizontal y = k (reciprocals, exponential).
- Increasing or decreasing: monotone parents (line, cube, cube root, square root, exponential, logarithm) are
  increasing on their domain when a x b > 0, decreasing when a x b < 0 (square root and logarithm: same rule).
  Square and absolute value: decreasing then increasing around x = h when a > 0, the reverse when a < 0. Reciprocal:
  decreasing on each piece when a x b > 0, increasing when a x b < 0. Reciprocal square: for a > 0 increasing for x < h,
  decreasing for x > h; reversed for a < 0 (the sign of b does not matter: 1/(b(x - h))² is the same for b and -b).
- Intercepts: y-intercept g(0) when 0 is in the domain; x-intercepts from the engine's `roots` on the domain, printed
  to 3 decimals (exact when they are whole or halves).
- End behavior: from the parent and the signs of a and b, as sentences ("as x goes to infinity, g(x) goes to -infinity").
- Symmetry: even if g(-x) = g(x), odd if g(-x) = -g(x), each within 1e-9 x (1 + |g(x)|), at 81 points of [-10, 10]
  where both sides are defined, with matching domains; else neither. (Example: x² with h = 0 stays even, also with
  k = 2; with h = 2 it is neither.)
Inverse formulas (shown in Mirror cousin, with f⁻¹ of the parent): g⁻¹(x) = h + (1/b) f⁻¹((x - k)/a), where f⁻¹ is x,
∛x, x³, 1/x, log₂ x, 2ˣ, and x² with x ≥ 0 for the square root. After `Keep the right half`: square
g⁻¹(x) = h + √((x - k)/a)/|b|; absolute value g⁻¹(x) = h + (x - k)/(a|b|); reciprocal square
g⁻¹(x) = h + 1/(|b|√((x - k)/a)).

Guests (one correct setting each; any setting giving the same curve also matches):
1. Aunt Vertex: -(x - 2)² + 3 (square; a = -1, h = 2, k = 3).
2. Cousin Root: 2√(x + 4) - 1 (square root; a = 2, h = -4, k = -1; also b = 4, h = -4, k = -1).
3. Uncle Split: 1/(x - 1) + 2 (reciprocal; h = 1, k = 2).
4. Grandpa Growth: 2^(x + 1) - 3 (exponential; h = -1, k = -3; also a = 2, h = 0, k = -3).
5. Cousin Mirror: log₂(-x) + 1 (logarithm; b = -1, k = 1).
6. Aunt Peak: -abs(2x) + 4 (absolute value; b = 2, a = -1, k = 4; also a = -2, b = 1).
7. Baby Cube: (x/2)³ (cube; b = 0.5).
8. Uncle Valley: -1/(x + 3)² (reciprocal square; a = -1, h = -3).
9. Great-aunt Curl: ∛(x - 5) + 1 (cube root; h = 5, k = 1).
10. Cousin Straight: 3x - 2 (line; a = 3, k = -2; also b = 3, k = -2; also a = 3, h = 1, k = 1).

## Interactions in detail
- Same-curve check (Who's who): both functions sampled at 161 points of [-10, 10]; the defined or undefined status must
  agree at every point, and values must agree within 1e-6 x (1 + |value|) wherever defined. Parent choice must give
  the same curve, so Line with a = 3 for guest 10 matches, and Cube cannot match a square root guest.
- Sliders and boxes refuse 0 for a and b (box text restored, tip "a can't be 0: the relative would be flat."). Boxes
  accept fractions ("1/2") and decimals; values snap to the step.
- Asymptotes are drawn dashed `--muted` with labels; curves break at them (engine).
- Exponential with large a and b may leave the view: the curve clips; features are still exact.
- `Keep the right half` resets when the parent changes. Mirror pins clear on any parameter change.
- Nothing plays on its own. Every drag, slider step or typed value redraws the relative, the table and the features in
  the same frame; a portrait tap swaps the parent at once (with Motion on the portrait lifts over 150 ms, but the
  plane never waits for it).
- Keyboard: handles are engine points (arrows move one step of h and k, or of the stretch point); portraits are buttons
  in a row (arrow keys move along the wall). Tab order: wall, moves, equation, table, features.
- Mode change: `Curio.stop()`, `V.hush()`; the current relative is kept across modes. Who's who check marks per device
  (localStorage `curio-ffr-guests`, try/catch), `Clear marks`.

## Look
Accent (`--brand`) #f7c59f, warm peach (an old photo): 11.1:1 on --panel #141b25, 10.5:1 on --sec-bg #18202b;
--brand-ink #10161f on it 11.6:1. Lighter and pinker than the amber of rollercoaster-polynomials and ferris-wheel
(#f2a93b) and the gold of poll-workshop; distinct from every group sibling.
Scene: the painted walnut wall (reunion-wall) behind the portrait strip, dimmed to about #1e1813 so the frames read;
each portrait-frame's mat is cream about #e9dcc8 with the mini graph on a #10161f inset, and the name plates are
#e9dcc8 with #10161f text (13.4:1). The plane uses the theme plane colors.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: warm, softly lit painted illustration, like an old family
album.
- reunion-wall: "A long wall of dark walnut wood paneling in a cozy old farmhouse living room, a wooden picture rail
  near the top, a string of paper bunting in faded peach and cream, soft afternoon window light from the left, painted
  illustration"; 4:1; cutout no; people no; the backdrop of the portrait strip, cropped to the strip's height and
  dimmed.
- portrait-frame: "An antique carved wooden picture frame with worn gold leaf around a plain smooth cream mat, front
  view, soft warm light, painted illustration, plain white background"; 3:4; cutout yes; people no; used ten times on
  the wall; the mini graph is drawn in code on the blank mat.
- name-badge: "A blank white sticky name badge with a plain peach band across the top and a slightly curled corner,
  smooth empty surfaces, painted illustration, plain white background"; 4:3; cutout yes; people no; the guest card in
  Who's who, with "Guest 3" and later the guest's name written in code on the white area.
The plane, curves, handles, mini graphs, asymptotes, tables and preview.svg (the wall strip over a plane with one
relative) are drawn in code: they are graphs and labels.

## Voice
`gentle-storyteller` (Vindemiatrix), style "Say gently and expressively, like a grandmother showing the family photo
album." Not used by a group sibling, a 9-12 math neighbor or another spec in batch R05. `Curio.voice`,
`scope: () => state.mode`. Cards and tables are read on screen; Read speaks the hint.
- reunion (how, Reunion welcome; stale once a handle or slider has moved): "Tap a parent on the photo wall. Then drag the cross or the ring on the graph, and the relative moves."
- moves (how, first slider or box change; stale on a mode change): "a stretches and flips up and down. b squashes and flips side to side. h slides right, and k slides up."
- points (how, first time the Where points land table changes; stale on a mode change): "Every parent point p, q lands at p over b plus h, and a times q plus k."
- mirror (how, Mirror cousin welcome; stale when the relative changes): "The cousin is the relative reflected across the line y equals x. Tap the relative to drop a pin and see its mirror."
- notFn (event, a non one-to-one relative shown in Mirror cousin; stale once Keep the right half is pressed or the relative changes): "This reflection is not a function. Press Keep the right half to fix that."
- guests (how, Who's who welcome; stale on the first parameter change): "Tap the parent you think this guest has on the photo wall. Then set the four moves until your curve lies on theirs."
- same (event, a guest matched; stale on a new guest): "Same curve. You found who they are."

## Family engine
Graphing (`kit/graphing.js`, docs/families/graphing.md; this tool is the grade 12 sibling). Uses `Plane` (main plane,
plus ten tiny planes or plain sampled paths for the portraits), `g.fn` with `domain` for the parent and relatives,
`g.param` for the mirror cousin, `g.point` for the home and stretch handles (`snap`, `onMove`, keyboard) and probe
pins, `g.slider` with `box` for a, b, h, k (`parse` refuses 0), `g.roots` for x-intercepts, `g.segment` for asymptotes
and y = x, `g.label`, `g.clear`. No new engine features needed.

## Sources
- Parent functions, transformations a f(b(x - h)) + k, domain, range, asymptotes: OpenStax, Precalculus 2e, 1.5
  "Transformation of Functions" and 3.7 "Rational Functions", 4.2 "Graphs of Exponential Functions", 4.4 "Graphs of
  Logarithmic Functions", https://openstax.org/books/precalculus-2e/pages/1-5-transformation-of-functions
- Inverse functions and domain restriction: OpenStax, Precalculus 2e, 1.7 "Inverse Functions",
  https://openstax.org/books/precalculus-2e/pages/1-7-inverse-functions
- Standards: CCSS Math F-IF.C and F-BF.B, https://www.thecorestandards.org/Math/Content/HSF/BF/ ; College Board, AP
  Precalculus CED (2023), Units 1 and 2.
- Guests are made up.
- Checks run (Python, NumPy, 2026-10-29): every guest's listed and "also" settings pass the same-curve check exactly as
  specified (161 points, defined status, 1e-6 tolerance), and Cube with no moves matches no guest; every listed setting
  sits on the slider steps and ranges. Added "also b = 4" to guest 2 (it passes, and a student may find it). Done when
  1: (1, 1) lands at (5, -1) and -2(0.5)² = -0.5. Symmetry rule on x², x² + 2, x³, ∛x, 1/x, 1/x² gives even, even,
  odd, odd, odd, even, and on x² and x³ with h = 2 and on x + 1 gives neither; the first draft compared exactly, so a
  1e-9 tolerance was added for floating point. The increasing and decreasing rule agreed with numeric slopes for all
  six monotone parents at every sign of a and b (0 failures), and the reciprocal square rule holds for both signs of b.
  The general inverse formula and the three right-half formulas returned the original x for several settings each.

## Done when
1. Square with a = -2, b = 0.5, h = 3, k = 1 shows "-2(0.5(x - 3))² + 1 = -0.5(x - 3)² + 1", range y ≤ 1, increasing
   for x < 3 and decreasing for x > 3, and (1, 1) landing at (5, -1).
2. Reciprocal with h = 2, k = -1 shows asymptotes x = 2 and y = -1, domain x ≠ 2, range y ≠ -1.
3. Square root with b = -1 has domain x ≤ 0; logarithm with b = -1 has domain x < 0.
4. Square at h = 0 reads "even", cube at h = 0, k = 0 reads "odd", either with h = 2 reads "neither".
5. Mirror cousin of the exponential with k = 0 is labeled inverse with formula log₂ x; the square shows "not a
   function" until `Keep the right half`, then g⁻¹(x) = h + √((x - k)/a)/|b|.
6. Guest 6 matches with a = -1, b = 2, k = 4 and with a = -2, b = 1, k = 4; guest 10 matches with a = 3, k = -2 and with
   b = 3, k = -2.
7. a or b typed as 0 is refused with the tip; dragging the stretch point never makes a or b 0.
8. Handles and sliders work by keyboard; the relative's dash pattern differs from the parent's.
9. Focus: at 1366x768 and 1000x625 the plane is the largest thing on the stage in every mode, and neither the wall
   strip nor the features card covers it.
10. Nothing waits: tapping a new portrait while the last one's lift plays swaps the parent at once, and a slider moved
    while a voice line plays redraws in the same frame.
11. How-to lines spoken once each in five actions; "Same curve." each time a guest is matched; no line names a control
    that is not on screen.
12. Controls visible without scrolling at 1366x768; the wall scrolls sideways at 375 wide; three painted images, no
    people; no network; no em dashes.

## Open questions
none
