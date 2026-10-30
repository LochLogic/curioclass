# Algebra Tile Studio

## One idea
A factor frame that only accepts a finished rectangle: drop algebra tiles in, and the moment they close into a
rectangle its two edges are the factors, and when they can't close (x² + x − 6 needs zero pairs, x² + 6x + 5 is
missing a corner of a square) the gap you see is exactly the algebra you were missing.

## Not like
- expression-garden (gr 6, algebra-tiles): grows and combines like terms with positive tiles only, no frame. Here the frame, negative tiles, zero pairs, factoring and completing the square.
- expression-match (gr 7, algebra-tiles): a card game matching equivalent expressions. Here you build the rectangle yourself.
- polynomials-as-numbers (gr 9, same group): multiplies polynomials as long multiplication with x = 10, no area model. This tool owns the area model (Cory's overlap call).
- launch-pad (gr 9, same group): solves quadratics for times in a flight. Here a quadratic is never solved for x; it is rewritten (factored, completed square) and read.
- rollercoaster-polynomials (gr 11): zeros of higher-degree polynomials on a graph. Here degree 2 only, as area.
- equation-golf (gr 9, same group): rewrites equations by moves on a balance. Here expressions only, no equals sign.

## Who and how
- Grade 9, Algebra 1, Structure of Expressions. Students drive, own laptops or pairs. 15 to 40 minutes.
- Topic line: "factoring and completing the square with algebra tiles".
- Standards (module): A-SSE.A (interpret structure: terms, factors, coefficients; see x² − 9 as a difference of squares), A-SSE.B (A-SSE.B.3a factor to reveal zeros, B.3b complete the square to reveal the minimum). See Open questions for B.3c and B.4.
- CCSS clusters: Mat serves A-SSE.A.1; Frame serves A-SSE.A.2 and B.3a; Square serves B.3b.
- tool.json: driver "students", minutes "15-40", modes ["Mat", "Frame", "Square"], grades_label "Grade 9".

## Screens and modes
Header (kit, 9-12 theme): title, subtitle "Close the rectangle. Read the factors." Modes `Mat` (opens first),
`Frame`, `Square`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: stage left (the mat, on the painted studio mat, art: studio-mat), panel right. Under 1000 px wide the panel
goes under the stage with the tray first. Under 900 px tall the tray sits in a single row across the top of the stage
so tiles and the frame stay in view.

Tile tray (every mode): `x²`, `x`, `1` buttons, each draggable onto the mat or pressed to drop one at the mat's
free spot. `Flip` (selected tile changes sign), `Turn` (selected x strip rotates 90 degrees), `Remove`,
`Zero pair` (drops an x and a −x side by side, or a 1 and a −1, by the last kind used). `Flip`, `Turn` and `Remove`
are disabled until a tile is selected.
Tiles: x² is an x by x square, x is an x by 1 strip, 1 is a unit square. Positive tiles are solid; negative tiles
are the red side with diagonal hatching and a minus glyph in the corner, so sign is never color alone.
Slider `x length` (from 1.3 to 4.7 units, default 2.6): every x edge changes length together; unit tiles never
do. Its readout: "x = 2.6". It shows x is not a fixed number of units.

### Mat (explore)
Focus: the tiles on the mat, center stage and taking most of it; the live expression is the first line of the panel.
A free mat (a grid in unit lengths). Panel: the expression read from the mat, live ("x² + 3x − 2"), the parts
named on hover or focus of each term ("coefficient 3", "term 3x", "constant −2"), and "Value at x = 2.6:" (the
signed total area). Dragging a tile onto an opposite tile of the same kind removes both with a short fade (250 ms,
"zero pair"); the expression does not change. `Clear mat`.

### Frame (factor)
Focus: the frame and the tiles inside it, center stage; the card's loose pile sits beside it, smaller, and the
answer lines sit in the panel.
A frame: a top edge and a left edge with an empty corner. Pick a card from the card list (Content). The card's tiles
appear in a loose pile beside the frame. Drag tiles into the frame; they snap to the frame grid (x² in the corner
zone, x strips along the edges, units in the far corner). While the tiles are not a rectangle, the frame shows the
empty cells as dashed outlines and the tip names what is wrong ("A hole at row 2: a unit tile fits here").
When every frame cell is filled and the rectangle is consistent, the edges light, each edge reads its length
("x + 2", "x + 3"), and the panel writes: "x² + 5x + 6 = (x + 2)(x + 3)", then "Zeros: x = −2 and x = −3 (each
factor is 0 there)". Card buttons: `Check`, `Start over`, `No rectangle` (claim this one cannot close).

### Square (complete the square)
Focus: the square being built from the x² tile and the split strips, center stage; the three rewrite lines in the
panel; the number line and its small inset sit under the square, smaller.
Pick a card (Content). The x² tile is placed in the corner; the card's x strips are split evenly along the top and
left edges by `Split strips` (or by dragging). The square's missing corner is outlined and labeled with its size
("3 by 3: 9 units"). `Fill the corner` (enabled after the strips are split) drops 9 unit tiles there and the same
number of negative unit tiles beside the square (a zero pair set), so the expression is unchanged. The panel shows the
three lines: "x² + 6x + 5", "= (x² + 6x + 9) − 9 + 5", "= (x + 3)² − 4", then "Smallest value: −4, when x = −3".
A dot on a small number line of x (from −8 to 8, step 0.5) lets you slide x. Beside it a small inset square of side
|x + 3| units (drawn at the unit scale, separate from the tiles, since a tile edge can't be negative) shrinks to
nothing at x = −3, and the readout prints "(x + 3)² − 4 = −4 at x = −3" for the current x.

## Content
Frame cards (expression, its pile, the answer):
1. x² + 5x + 6 = (x + 2)(x + 3). Pile: 1 x², 5 x, 6 ones.
2. x² + 7x + 12 = (x + 3)(x + 4). Pile: 1 x², 7 x, 12 ones.
3. x² + 6x + 9 = (x + 3)². Pile: 1 x², 6 x, 9 ones. The rectangle is a square: the panel says "a perfect square".
4. x² − 5x + 6 = (x − 2)(x − 3). Pile: 1 x², 5 −x, 6 ones.
5. x² + x − 6 = (x + 3)(x − 2). Pile: 1 x², 1 x, 6 −1. Needs 2 zero pairs of x (3 x and 2 −x in the frame).
6. x² − 9 = (x + 3)(x − 3). Pile: 1 x², 9 −1. Needs 3 zero pairs of x. Panel adds "a difference of squares".
7. 2x² + 7x + 3 = (2x + 1)(x + 3). Pile: 2 x², 7 x, 3 ones.
8. 2x² + 5x + 2 = (2x + 1)(x + 2). Pile: 2 x², 5 x, 2 ones.
9. x² + x + 1: no rectangle (whole-number edges). Pile: 1 x², 1 x, 1 one. `No rectangle` is the right claim.
10. x² + 4: no rectangle. Pile: 1 x², 4 ones.
Square cards: x² + 6x + 5 = (x + 3)² − 4, min −4 at x = −3. x² + 4x + 7 = (x + 2)² + 3, min 3 at x = −2.
x² + 8x + 16 = (x + 4)², min 0 at x = −4 (no tiles left over). x² − 6x + 10 = (x − 3)² + 1, min 1 at x = 3
(negative strips). x² + 2x − 3 = (x + 1)² − 4, min −4 at x = −1. x² − 4x = (x − 2)² − 4, min −4 at x = 2.
Only even x counts appear here, so strips always split evenly.

## Interactions in detail
- A frame cell's tile must equal (its row edge piece) times (its column edge piece): x by x is x², x by 1 is x,
  1 by 1 is 1, and signs multiply. Edge pieces are read from the first row and first column. A tile placed where
  its kind or sign breaks this gets a red outline plus "doesn't fit" text and the tip says why.
- Zero pairs may be added anywhere in Frame; they never change the expression, and the panel says "added 0".
- `Check` with a consistent full rectangle: correct. `Check` with gaps names the first gap. `No rectangle` is
  right only for cards 9 and 10 (the tool tests every whole-number factor pair of the constant; none makes the
  middle coefficient). On cards 1 to 8 it answers "This one does close. Try a zero pair." for 5 and 6, and "Try
  moving the strips" for the others.
- Answers are checked exactly: the factors' product is expanded with integer coefficients and compared term by
  term with the card. Any order of factors, and either sign arrangement that multiplies out, is accepted.
- Square: the corner size is (b/2)²; the constant left over is c − (b/2)²; the minimum is that number at
  x = −b/2. Zero leftover (card 3 and x² + 8x + 16) shows "nothing left over: a perfect square".
- `x length` changes only the drawing; it never changes which tiles fit.
- Animations are short (zero-pair fade 250 ms, corner fill 400 ms, Motion off: instant). A tap or key during one
  finishes it at once and then acts; nothing waits for an animation to end.
- Keyboard: Tab to a tile, arrow keys move it one grid cell, F flips, T turns, Delete removes, Enter on a tray
  button drops a tile. The frame announces "row 2, column 3: unit tile, fits".
- Reset: `Start over` per card; mode switches keep each mode's state for the page session; nothing is saved.
- `window.__tool = {state, setMode, load(card), check(), expression()}`.

## Look
Accent `--brand #6cc4ff` (sky blue), `--brand-ink #04192a`. The painted studio mat (art: studio-mat) fills the stage,
dimmed under a unit grid `#1c2c3d` at 70% so tile edges stay crisp. Tiles: x² `#6cc4ff` fill, x `#7ee08a` fill,
1 `#ffd166` fill, all with a `#0b1017` 2 px outline and ink labels; negative tiles `#ff8a8a` with dark diagonal hatch
and a minus glyph. Frame edges `#e8edf3`; missing corner dashed `#ffd166`.
Contrast (computed): brand on panel 9.05:1, on --sec-bg 8.57:1, brand-ink on brand 9.32:1. Tile label ink `#0b1017`
on x² 9.97:1, on x 11.73:1, on 1 13.23:1, on negative 8.41:1. Different from math 9-12 neighbors (amber, orange,
teal, gold, green) and group siblings.

## Art
Local FLUX (`scripts/localart.py`); no people.
- studio-mat: "A dark slate-blue rubber craft mat seen straight from above, faint fabric grain, soft even studio
  light, painted illustration"; 16:10; cutout no; people no; full-frame texture under the unit grid on every mode,
  dimmed; the grid, tiles and frame are drawn in code over it.
Tiles, the frame, the number line, the inset square and preview.svg stay in code: tiles must stretch with the
`x length` slider and snap to a grid, so they are shapes the tool must bend.

## Voice
Bank voice `wise-mentor` (thoughtful, warm). No 9-12 math neighbor or batch spec uses it. `Curio.voice`,
`scope: () => state.mode`. Tip and hint text are read on screen; Read speaks the hint.
- wMat (how; Mat entered; stale once a tile is on the mat): "Press x squared, x or 1 to drop a tile, or drag one onto the mat. A red tile on a matching solid tile makes zero."
- wFrame (how; Frame entered; stale once a card is picked): "Pick a card from the list. Then drag its tiles into the frame until they close into a rectangle."
- wSquare (how; Square entered; stale once a card is picked): "Pick a card. Press Split strips, then press Fill the corner."
- zeroHint (how; first Check on card 5 or 6 with the pile used up and the frame not closed; stale when a zero pair is added or the card changes): "Stuck? Press Zero pair. It changes the picture, not the value."
- gap (event; Check with gaps; stale on the next tile move): "Not closed yet. Fill the dashed cell the tip names, then press Check."
- closed (event; rectangle checks; stale when the card changes): "It closes. The edges are the factors."
- noRect (event; correct No rectangle claim; stale on card change): "Right. No whole-number rectangle exists for this one."
- noRectWrong (event; No rectangle on cards 1 to 8; stale on the next tile move): "This one does close. Read the tip and keep building."
- square (event; corner filled; stale on card change): "The square is done. What is left over is the smallest value."

## Family engine
algebra-tiles (`kit/algebra-tiles.js`, inlined after `kit:curio`). This spec holds the full description for the
family; expression-garden (gr 6) and expression-match (gr 7) reuse it.
- `Poly`: exact polynomials in x (and y) with integer or fraction coefficients. `Poly.parse('2x^2+7x+3')`,
  `.add .sub .mul`, `.equal`, `.eval(x)`, `.fmt()` (true minus sign, superscript ², terms in descending degree).
- `TileMat(svgGroup, {width, height, unit, xLen, yLen, kinds: ['x2','x','1','y','y2','xy'], negatives, grid})`:
  tiles `{id, kind, sign, col, row, turned}`; `add(kind, sign, at)`, `remove(id)`, `flip(id)`, `turn(id)`,
  `move(id, col, row)`, `poly()`, `onChange(fn)`, `setXLen(v)`; zero pairs vanish when dropped on each other
  (`zeroPairs: true`); pointer and keyboard dragging with 44 px targets; each tile has an aria label.
- `Frame(mat, {at})`: a factor frame; `read()` returns `{full, consistent, gaps: [...], bad: [...], rows, cols,
  factors: [Poly, Poly]}` using the rule "cell = row edge times column edge".
- Fixed by the engine: tile shapes and proportions (x never a whole number of units), colors x² blue, x green,
  1 yellow, negative red with hatch and minus glyph, the zero-pair fade (instant with Motion off).
- What each sibling feeds it: expression-garden: positive x and 1 tiles in a garden skin, no Frame. expression-match:
  `Poly.equal` and small static tile pictures on cards. This tool: x² tiles, negatives, Frame, and the Square
  helper (split strips, corner outline), which stays in this tool.

## Sources
- A-SSE.A and A-SSE.B text: Common Core State Standards for Mathematics, High School Algebra, Seeing Structure in Expressions, https://www.thecorestandards.org/Math/Content/HSA/SSE/
- Factoring trinomials and completing the square: OpenStax, Elementary Algebra 2e, 7.3 "Factor Trinomials of the Form ax² + bx + c" and Intermediate Algebra 2e, 9.2 "Solve Quadratic Equations by Completing the Square", https://openstax.org/books/intermediate-algebra-2e/pages/9-2-solve-quadratic-equations-by-completing-the-square
- Algebra tiles as an area model with zero pairs: NCTM Illuminations, "Algebra Tiles" interactive, https://www.nctm.org/Classroom-Resources/Illuminations/Interactives/Algebra-Tiles/
- Checks run (Python with sympy, 2026-10-29): all 8 closing cards expand back to their expressions and match
  sympy's factor(); cards 9 and 10 do not factor over the integers. Frame strip counts from the edges: card 5 needs
  3 x and 2 −x (pile has 1 x, so 2 zero pairs), card 6 needs 3 x and 3 −x (3 zero pairs), card 4 needs 5 −x and
  6 ones, card 7 needs 7 x. Every square card: (x − h)² + k expands back; corners 9, 4, 16, 9, 1, 4; minimums −4,
  3, 0, 1, −4, −4 at x = −3, −2, −4, 3, −1, 2. x² + 3x − 2 at x = 2.6 is 12.56. The first draft's number line slid
  x to −3 while the tile square's edge (x + 3) can't be drawn below zero length; the inset square of side |x + 3|
  fixes that.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Mat: dropping 1 x², 3 x and 2 −1 reads "x² + 3x − 2"; a +x dropped on a −x removes both and the expression is unchanged.
2. Frame card 1 closes only as (x + 2)(x + 3) and the panel shows zeros −2 and −3.
3. Card 5 cannot close until 2 zero pairs of x are added; then it reads (x + 3)(x − 2). Card 6 needs 3 and says "difference of squares".
4. Card 7 closes as (2x + 1)(x + 3); a misplaced unit tile is outlined "doesn't fit" with a reason.
5. `No rectangle` is accepted on cards 9 and 10 and refused, with the tip, on cards 1 to 8.
6. Square: x² + 6x + 5 gives (x + 3)² − 4 and "Smallest value: −4, when x = −3"; x² + 8x + 16 says nothing is left over; x² − 6x + 10 gives (x − 3)² + 1; the inset square vanishes at x = −3.
7. `x length` changes every x edge and no unit tile; the fit results don't change.
8. Focus: at 1366x768 and 1000x625 the mat (Mat), the frame (Frame) and the square (Square) are each the largest thing on the stage.
9. Tap while it plays: during a zero-pair fade or a corner fill, a drag, `Flip` or `Start over` acts at once and the expression stays exact.
10. Keyboard alone can finish card 1; sign is readable without color; no voice line names a disabled control; every size in STANDARDS.md keeps the tray and frame visible without page scrolling.
11. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- A-SSE.B.3c (rewrite exponential expressions, like 1.15^t as (1.15^(1/12))^(12t)) and A-SSE.B.4 (finite geometric series) are on this module but are not tile work. This tool does not teach them. exponent-rule-builder touches exponent rewriting and savings-plan (gr 11) owns series. Leave them uncovered here, or add a small fourth mode?
