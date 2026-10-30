# Image Transformer

## One idea
A 2x2 matrix is four numbers that move every pixel of a picture at once: its two columns are where the picture's
two edge arrows land, its determinant is how much the area grows (and whether the picture flips), and two matrices
stacked in the other order give a different picture, which you see side by side.

## Not like
- flight-planner (this group): vectors as velocities that add. Here vectors are the columns of a matrix and the matrix moves a whole picture.
- rigid-motion-twins (gr 10, transformations): rigid motions named as moves (turn, slide, flip). Here every move is a grid of numbers, most moves are not rigid (shear, stretch, flatten), and you multiply them.
- polar-rose-studio (this group): multiplying a complex number turns and stretches a drawing; that is one kind of matrix. Here any 2x2 matrix, including shears and flattening ones a complex number cannot make.
- imaginary-island (gr 11): quarter turns by multiplying by i; no matrices, no determinant.
- undo-machine (gr 11, puzzle): undoing a chain of function machines. Here undoing is a matrix inverse, and a determinant of 0 is the reason a picture cannot be undone.

## Who and how
Grade 12, precalculus (Matrices). Students drive, 25 to 40 minutes. Explore first: Studio opens with a picture and
the identity matrix, every number live.
Topic line: "matrices as transformations".
Standards: N-VM.C (N-VM.6 to 12: multiply, scalar multiples, not commutative, identity and zero, determinant and
inverses, matrix times vector, 2x2 matrices as transformations, |det| as area), A-REI.C.9 (inverse of a matrix to solve
a system: here "where did this pixel come from" and a 3x3 color filter undone by its inverse), AP-PRECALC.U4 (4.10 to
4.14, matrices as linear transformations).
CCSS per mode: Studio N-VM.C.12 and C.7; Order matters N-VM.C.8 and C.9; Undo it N-VM.C.10 and A-REI.C.9.
tool.json: driver "students", minutes "25-40", modes ["Studio", "Order matters", "Undo it"].

## Screens and modes
Header (kit, 9-12 theme): "Image Transformer", small line "Four numbers move every pixel." Modes `Studio`,
`Order matters`, `Undo it`; kit `Motion`, `Sound`, `Read`.

Stage: a canvas with a coordinate grid (x and y from -6 to 6, equal scale, origin at the center, y up). The picture
sits with its lower left corner at the origin, filling the rectangle from (0, 0) to (4, 3) (pictures are 4:3).
Two arrows from the origin: i-hat (to (1, 0), `--gr-1` solid) and j-hat (to (0, 1), `--gr-2` dashed); a faint unit
square between them. Under a matrix the grid, the picture, the arrows and the unit square all move together (canvas
transform, with y flipped so math y is up). A ghost of the original picture stays at 20 percent opacity.

Panel:
- "Picture": thumbnails `Lighthouse`, `Balloon`, `Fox` (painted, Art) and `Letter F` (drawn in code, an F on a 4x3
  checkerboard, not symmetric so flips show).
- "Matrix": four number boxes [a b; c d], each with a small slider (-3 to 3, step 0.1), written as a bracket matrix in
  large readout type. Columns are tinted: the first column's boxes have a `--gr-1` edge, the second `--gr-2`, to match
  the arrows. Under it: "Column 1 is where i-hat lands: (a, c). Column 2 is where j-hat lands: (b, d)."
- Presets: `Identity`, `Turn 90°`, `Turn 30°`, `Shear`, `Stretch x2`, `Reflect`, `Flatten`. Button `Scale by k`
  with a k box (multiplies every entry by k).
- Readouts: "det = ad - bc = ...", "Area x |det|: 12 square units becomes ...", "Flipped: yes/no" (det < 0),
  "Flattened onto a line" (det = 0) or "Flattened to a point" (zero matrix).
- `Animate` (eases from the identity to the matrix over 1 s; instant with Motion off), `Reset`.

### Studio (explore, default)
Focus: the picture moving on the grid with its two arrows, center stage and largest; the matrix and readouts are in
the panel.
Drag the tip of i-hat or j-hat on the grid (they snap to 0.1) and the matrix boxes follow, or type the boxes and the
arrows follow. A probe: tap any point of the picture to drop a pin; the panel shows "M times (x, y) = (ax + by,
cx + dy)" with numbers, and the pin moves with the picture.

### Order matters
Focus: the two stages side by side (stacked below 1000 px), equal in size and together filling the stage, each with
its product matrix over it.
Two matrix cards A and B (presets plus boxes, as above) and two stages labeled "A then B: BA" and "B then A: AB". Each
shows the product matrix and its picture. A line under them: "Same picture" or "Different pictures" (products
compared entry by entry within 0.0005). `Swap` exchanges A and B. A small toggle `A + B` shows a third stage with the
sum matrix, for comparison only. Note on screen: "Matrix products read right to left: in BA, A acts first."

### Undo it
Focus: the moved picture over its faint home ghost, center stage and largest (for the color filter: the filtered
picture with the probed pixel ringed); the card's boxes in the panel.
Three cards:
1. "Undo the move": a picture already moved by a matrix M (`Move 1` to `Move 4`). The student types the four entries
   of the undo matrix; `Apply` multiplies and the picture snaps home if their matrix times M is the identity (each
   entry within 0.005). `Show the formula` shows M inverse = (1/det)[d -b; -c a]. For `Move 4` (det 0) the right
   answer is the button `It can't be undone`, and the card explains: "Every point on a line lands on the same spot,
   so no matrix can send them back apart."
2. "Where did this pixel come from?": a pin on the moved picture at b; the student types (x, y) with Mx = b and
   presses `Check`. Checked exactly (fractions or decimals to 0.01). Work card shows x = M inverse times b.
3. "Color filter": the picture shown through a 3x3 color filter F acting on each pixel's (R, G, B). A pixel readout
   gives a filtered color; the student types the original R, G, B (whole numbers 0 to 255) and presses `Check`. The
   tool shows F, has `Find F inverse` (technology does the 3x3 inverse, as A-REI.C.9 expects for 3x3), and
   `Gray filter`, a filter that cannot be undone (det 0).

## Content
Presets: Identity [1 0; 0 1]; Turn 90° [0 -1; 1 0]; Turn 30° [0.866 -0.5; 0.5 0.866] (cos 30° and sin 30° to 3 places,
det 0.999956, shown to 3 decimals as 1); Shear [1 1; 0 1]; Stretch x2 [2 0; 0 1]; Reflect [-1 0; 0 1] (across the
y-axis, det -1); Flatten [1 2; 0.5 1] (det 0: everything lands on the line y = x/2).
Order example loaded first: A = Turn 90°, B = Shear. BA = [1 -1; 1 0]; AB = [0 -1; 1 1]. Different pictures, both det 1.
Second pair to try (named in a tip): A = Stretch x2, B = Turn 90°: BA = [0 -1; 2 0], AB = [0 -2; 1 0]: different.
A pair that does commute: two turns (Turn 90° and Turn 30°), and any matrix with Identity.

Undo moves:
- Move 1: M = [2 1; 1 1], det 1, inverse [1 -1; -1 2]. Pixel b = (5, 3) came from (2, 1).
- Move 2: M = [3 1; 2 1], det 1, inverse [1 -1; -2 3]. b = (7, 5) came from (2, 1).
- Move 3: M = [1 2; 3 4], det -2, inverse [-2 1; 1.5 -0.5]. b = (5, 11) came from (1, 2).
- Move 4: M = [1 2; 2 4], det 0: no inverse.

Color filter "Blend": F = [0.5 0.5 0; 0 0.5 0.5; 0.5 0 0.5] (each new channel averages two old ones), det 0.25,
F inverse = [1 -1 1; 1 1 -1; -1 1 1].
| Filtered pixel | Original |
|---|---|
| (150, 70, 120) | (200, 100, 40) |
| (120, 150, 90) | (60, 180, 120) |
| (140, 60, 170) | (250, 30, 90) |
Gray filter: every row (1/3, 1/3, 1/3), det 0: "(90, 90, 90) could have come from (90, 90, 90), (270, 0, 0) or
(0, 135, 135), and many more, so no inverse exists." (Each sums to 270.)

## Interactions in detail
- Rendering: canvas `setTransform` with the matrix, origin at the grid center, y flipped. The grid lines are drawn
  through the same transform (so they shear and turn too) and the fixed axes are redrawn untransformed and faint.
- Boxes accept decimals and simple fractions ("1/2", "-3/4"); results print to 3 decimals with trailing zeros dropped.
  Entries clamp to -10 to 10 (sliders -3 to 3); values far out simply leave the canvas (clipped).
- det within 0.0005 of 0 counts as 0 for the readouts (avoids "det = 0.000000001" after Turn 30° products).
- The zero matrix draws the picture as a single dot at the origin with "Flattened to a point".
- Checks in Undo: inverse entries within 0.005; pixel origins exact to 0.01; color answers exact whole numbers. Two
  misses show `Show me`. Wrong answers say which equation fails: "Row 1: 2(3) + 1(1) = 7, not 5."
- `Animate` interpolates entries from the identity (linear), so a turn sweeps through shears on the way; a note says
  "The in-between frames are just the in-between matrices." It never blocks: a box edit, slider, arrow drag, preset or
  `Reset` during the 1 s ease stops it and shows the new matrix at once. The Undo snap home also eases over 0.6 s and a
  new `Move` button cuts it short the same way.
- Keyboard: arrow tips are focusable (arrows move 0.1, Shift 1); boxes in tab order before the presets.
- Mode change: `Curio.stop()`, `V.hush()`. Nothing is saved.

## Look
Accent (`--brand`) #a58cff, violet: 6.4:1 on --panel #141b25, 6.1:1 on --sec-bg #18202b; --brand-ink #10161f on it
6.7:1. Different from every 9-12 math neighbor (amber, orange, teal, cyan, green, gold) and the group's fuchsia and
rose by hue. Stage: a darkroom look, canvas background #0e1118 with grid #2a3140 (decorative), the picture full color.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: crisp, clear, photo-like painted illustration with strong
shapes, so every stretch and flip is easy to see. Each is a full-frame 4:3 picture that the matrix moves.
- imt-lighthouse: "A white and red striped lighthouse on a rocky point under a clear blue afternoon sky, small waves
  breaking below, crisp photo-like painted illustration"; 4:3; cutout no; people no; a picture to transform (tall and
  upright, so turns and shears read at once).
- imt-balloon: "One bright red and yellow striped hot air balloon floating over green rolling fields under a clear sky,
  crisp photo-like painted illustration"; 4:3; cutout no; people no; a picture to transform, and the default for the
  color filter card (strong reds, yellows and greens).
- imt-fox: "A red fox sitting in a snowy clearing in side view, facing left, its tail curled to the right, crisp
  photo-like painted illustration"; 4:3; cutout no; people no; a picture to transform (facing one way makes flips
  obvious).
The Letter F grid, arrows, grids, matrices, pins and preview.svg are drawn in code: they are diagrams and labels.

## Voice
`casual-peer` (Zubenelgenubi), style "Say casually and naturally, like a friendly teen showing a photo-editing trick."
Not used by a group sibling, a 9-12 math neighbor or another spec in batch R05. `Curio.voice`,
`scope: () => state.mode`. Readouts are read on screen; Read speaks the hint.
- studio (how, Studio welcome; stale once a box, slider or arrow changes): "Type in the four number boxes, or drag the tip of either arrow. Every pixel in the picture follows."
- columns (how, first arrow drag; stale on a mode change): "The first column is where the right arrow lands. The second is where the up arrow lands."
- flipped (event, det turns negative; stale when det turns positive): "The determinant went negative, so the picture flipped."
- flat (event, det becomes 0; stale when det is not 0): "Determinant zero. The whole picture got squashed onto a line."
- order (how, Order matters welcome; stale once A or B changes): "Pick a preset for A and for B. The two screens do them in opposite orders. Press Swap to trade them."
- undo (how, Undo it welcome; stale once Apply is pressed): "Type the matrix that puts the picture back, then press Apply."
- pixel (how, first Where did this pixel come from card; stale once Check is pressed): "Type the x and y this pixel started at, then press Check."
- home (event, a correct undo; stale on a new move): "Back home. Your matrix undid it."
- noUndo (event, It can't be undone chosen correctly; stale on a new move): "Right. A flattened picture can't be pulled back apart."
- color (how, first Color filter card; stale once Check is pressed): "Each pixel's color went through the filter. Type the original red, green and blue, then press Check."

## Family engine
none (canvas transforms; no plotting).

## Sources
- Matrix multiplication, determinant, 2x2 inverse formula, solving systems with an inverse: OpenStax, Precalculus 2e,
  9.5 "Matrices and Matrix Operations" and 9.7 "Solving Systems with Inverses",
  https://openstax.org/books/precalculus-2e/pages/9-7-solving-systems-with-inverses
- Columns as images of the basis vectors, |det| as area scale, negative det as orientation flip: College Board, AP
  Precalculus Course and Exam Description (2023), topics 4.11 to 4.14,
  https://apcentral.collegeboard.org/courses/ap-precalculus
- Standards: CCSS Math N-VM.C and A-REI.C.9, https://www.thecorestandards.org/Math/Content/HSN/VM/
- All matrices, moves, pixels and filters are made up.
- Checks run (NumPy, 2026-10-29): Turn 30° det 0.999956 (prints as 1; the first draft said 1.000, now stated
  exactly); Flatten det 0. Turn 90° and Shear: BA [1 -1; 1 0], AB [0 -1; 1 1], both det 1. Stretch x2 and Turn 90°:
  BA [0 -1; 2 0], AB [0 -2; 1 0]. Turn 90° times Turn 30° minus Turn 30° times Turn 90°: largest entry 0, so "Same
  picture" holds even with the rounded 0.866. Moves 1 to 3: det 1, 1, -2, inverses as listed, and the pixels solve to
  (2, 1), (2, 1), (1, 2); Move 4 det 0. Blend det 0.25, inverse [1 -1 1; 1 1 -1; -1 1 1], and each original times F
  gives its filtered pixel. Gray filter sends all three listed colors to (90, 90, 90). Probe [2 1; 1 1] times (1, 1)
  = (3, 2); 3I has det 9; Shear keeps area 12, Stretch x2 makes 24. The wrong-answer example (guess (3, 1) on Move 1)
  gives 7, as the message says.

## Done when
1. Studio: `Shear` shows [1 1; 0 1], det 1, area 12 stays 12; `Stretch x2` gives det 2 and area 24; `Reflect` shows
   "Flipped: yes".
2. Dragging i-hat's tip to (2, 1) sets column 1 to (2, 1); the probe at (1, 1) under [2 1; 1 1] reads (3, 2).
3. `Flatten` gives det 0 and "Flattened onto a line"; `Scale by k` with k = 3 on Identity gives det 9.
4. Order matters with Turn 90° and Shear shows BA = [1 -1; 1 0], AB = [0 -1; 1 1] and "Different pictures"; two turns
   show "Same picture".
5. Undo Move 1 accepts [1 -1; -1 2] and the picture snaps home; Move 3 accepts [-2 1; 1.5 -0.5]; Move 4 accepts only
   `It can't be undone`.
6. Pixel origins: Move 1 (5, 3) to (2, 1); Move 3 (5, 11) to (1, 2). Color: (150, 70, 120) to (200, 100, 40).
7. Order matters with A = Stretch x2, B = Turn 90° shows BA = [0 -1; 2 0] and AB = [0 -2; 1 0]; Identity with anything
   shows "Same picture".
8. Focus: at 1366x768 and 1000x625 the moving picture (Studio, Undo it) and the two stages together (Order matters)
   are the largest thing on the stage.
9. Tap while it plays: changing a box or pressing a preset halfway through `Animate` shows the new matrix at once,
   with no jump back to the old ease.
10. How-to lines spoken once each in five actions; "flipped" and "flat" spoken each time they happen; no line names a
    control that is not on screen.
11. Controls visible without scrolling at 1366x768; at 760 wide the two Order stages stack; the picture stays sharp at
    1920x1080.
12. No network; three painted images, no people; no em dashes.

## Open questions
- image-transformer: the 3x3 color filter is the only 3x3 work (A-REI.C.9 asks for 3x3 or larger with technology).
  Enough, or should Undo it add a plain 3x3 word-problem system?
