# Equation Golf

## One idea
Every legal move on an equation is a golf stroke on a balance beam (add, subtract, multiply, divide, distribute),
so the shortest route to "x = number" is par: dividing by 4 before distributing saves a stroke, multiplying by a
reciprocal can finish in one, and on the inequality holes dividing by a negative tips the beam the other way, so
the sign has to flip.

## Not like
- balance-puzzle (gr 6, balance): mystery bags and weights, positive only, remove the same from both sides. Here negatives (balloons), groups, fractions, inequalities, and strokes against par.
- balance-the-beam (gr 1) and snack-scale (K), balance: equality and comparison with counts. Same engine, no variables.
- undo-machine (gr 11): builds the inverse of a chain of function machines. Here no machines; the moves act on both sides of one equation and the score is how few you need.
- model-my-world (gr 9, same group): writes equations from situations and rearranges formulas with letters. Here equations are given and only solved.
- algebra-tile-studio (gr 9, same group): rewrites expressions as rectangles; no equals sign there.
- intersection-quest (gr 9, same group): two-variable systems. Here one variable.

## Who and how
- Grade 9, Algebra 1, Solving Linear Equations and Inequalities. Students drive. 15 to 35 minutes (a nine takes about 12).
- Topic line: "solving linear equations and inequalities".
- Standards (module): A-REI.A (A-REI.A.1: each step follows from equality and is named), A-REI.B (A-REI.B.3: linear equations and inequalities in one variable). A-REI.B.4 (quadratics) is on the module's cluster but belongs to launch-pad; see Open questions.
- CCSS clusters: Front nine serves A-REI.A.1 and B.3 (equations); Back nine serves B.3 (inequalities).
- tool.json: driver "students", minutes "15-35", modes ["Range", "Front nine", "Back nine"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "Fewest legal moves wins." Modes `Range` (opens first), `Front nine`, `Back nine`.
Kit buttons `Motion`, `Sound`, `Read`.
Stage: the balance beam stands on a painted fairway (art: fairway), center stage and the largest thing on it, with the
equation in large type above it. The beam, pivot and pans are painted cutouts (art: beam kit) that the code tilts.
Each side's items sit in its pan as painted cutouts: weight blocks for positive constants (the number in code on the
blank face), balloons (tied on, pulling up) for negative constants, mystery bags for +x, balloon bags for −x, a bag
cut in parts for fractions of x (dashed cut lines and "1/3" in code over the bag), and code-drawn brackets around a
group with its multiplier on a tag ("4 ×"). Pans hold up to 12 glyphs; more become a crate with the count in code
("38").
Panel, top to bottom: stroke counter "Strokes 2 / Par 3", the move bar, the scorecard, the hint.
Move bar: `Add`, `Subtract` (each opens a term box: a number, or a number times x, like "2x" or "-3"),
`Multiply`, `Divide` (each opens a number box: integers, fractions "6/5", decimals), `Distribute` (then tap a
group; disabled when no group is on the beam), `Tidy` (free), `Swap sides` (free), `Undo` (disabled before the first
move), `Declare` (opens: `x = ...` is automatic; `No solution`, `Every x works`).
Under 900 px tall the move bar sits beside the beam; at 760 wide it sits right under the equation.

### Range (explore)
Focus: the beam and the number line under it; the shading is the thing to watch while moves change the beam.
Type any linear equation or inequality in one variable into the box `Your equation` (or pick from the Content
sample list) and play moves freely. No par, no score. A `Try x` slider (from −10 to 10, step 0.5) tips the beam by
the two sides' values at that x, and a number line under the beam shades every x for which the statement is true.
The shading never changes as you make legal moves: that is the point the Range shows.

### Front nine and Back nine
Focus: the beam and the equation above it; the move bar sits next to it in the panel.
Holes 1 to 9 (equations) and 10 to 18 (two special equations, then inequalities). Each hole shows its par. Make
moves until the hole is finished: one side is exactly x and the other a number (either order), or you Declare.
Then a card with the painted green (art: green-flag) across its top: strokes, par, the golf name (eagle 2 under,
birdie 1 under, par, bogey 1 over, double bogey 2 over, "+3" and so on), the move log with each step's reason, and
`Replay` (the moves animate in order, 0.8 s each, at most 6 s), `Retry`, `Next hole`. Best strokes per hole saved on
this device (localStorage `curio-equation-golf`, try/catch) with `Clear scores` in the scorecard.

## Content
Holes (start as written; par route; answer):
1. x − 4 = 9. Par 1: add 4. x = 13.
2. 5x + 3 = 38. Par 2: subtract 3, divide by 5. x = 7.
3. 4(x + 1) = 28. Par 2: divide by 4, subtract 1. x = 6. (Distributing first costs 3.)
4. 7x − 5 = 3x + 11. Par 3: subtract 3x, add 5, divide by 4. x = 4.
5. x/3 + 2 = 6. Par 2: subtract 2, multiply by 3. x = 12.
6. 2(x − 3) + 4 = 3x − 9. Par 3: distribute (2x − 2 = 3x − 9), subtract 2x, add 9. x = 7.
7. x/2 + x/3 = 10. Par 1: Tidy (free: 5x/6 = 10), multiply by 6/5. x = 12.
8. 0.4x + 1.2 = 2 (shown in decimals). Par 2: subtract 1.2, divide by 0.4. x = 2.
9. 5 − 2x = 11. Par 2: subtract 5, divide by −2. x = −3.
10. 3(2x − 1) = 2(3x + 4). Par 3: distribute, distribute, subtract 6x (−3 = 8), Declare No solution.
11. 2(x + 3) = 2x + 6. Par 1: distribute (both sides identical), Declare Every x works.
12. (x + 5)/4 = (x − 1)/2. Par 4: multiply by 4 (x + 5 = 2(x − 1)), distribute, subtract x, add 2. x = 7.
13. x + 6 > 10. Par 1: subtract 6. x > 4.
14. 3x − 2 ≤ 13. Par 2: add 2, divide by 3. x ≤ 5.
15. −4x + 1 < 9. Par 2: subtract 1, divide by −4 (flip). x > −2.
16. 2(x − 1) ≥ 5x + 7. Par 4: distribute, subtract 2x, subtract 7, divide by 3. −3 ≥ x, read as x ≤ −3.
17. 3 − x/2 > 1. Par 2: subtract 3, multiply by −2 (flip). x < 4.
18. 2x + 5 ≤ 2(x + 1). Par 2: distribute, subtract 2x (5 ≤ 2, false), Declare No solution.
Range samples: the 18 holes plus 6(x − 1) = 3(2x − 2) (every x) and 1.5x − 2 ≥ 0.5x + 3 (x ≥ 5).
Every par was confirmed by a breadth-first search (Sources). The build keeps that search as a test over the
candidate moves (add or subtract any term that appears, inside groups too, with either sign; multiply or divide by
any coefficient, denominator, group multiplier, their negatives and reciprocals; distribute any group; Tidy;
Declare), up to depth par. If a shorter route ever appears, par drops to it and this table is updated in the same
change.

## Interactions in detail
- Exact arithmetic: every coefficient is a fraction (integers with gcd reduction). Decimal holes display decimals
  (to as many places as exact, up to 4), others display fractions.
- Model: a side is a list of items; an item is a term (a·x or a constant) or a group k·(terms). Multiply or divide
  a side: terms scale; a group's k scales, and a group whose k becomes 1 dissolves into its terms. Distribute
  turns k·(terms) into terms. After every stroke, like terms at the top level combine and zero pairs vanish (the
  balloons and blocks pop together, 250 ms, instant with Motion off); the log notes "combined like terms".
- Strokes: Add, Subtract, Multiply, Divide, Distribute count 1. Tidy, Swap sides, Declare and Undo count 0 (Undo
  also removes the stroke).
- Refused moves (no stroke, tip says why): multiply by 0 ("That makes 0 = 0 and loses the answer"), divide by 0
  ("Dividing by zero is undefined"), a term box that isn't a number or a number times x.
- Declare is accepted only when true: when both sides are numbers, a false statement (−3 = 8, 5 ≤ 2) is No solution
  and a true one (6 = 6, 2 ≤ 5) is Every x works; when the two sides are identical after tidying (2x + 6 = 2x + 6),
  Every x works. A wrong Declare costs a stroke and shows the shading of the true solution set.
- Inequalities: after multiplying or dividing by a negative, the sign shows "?" and the beam swings to show that
  every x now makes the other side heavier; two buttons `<` `>` (or `≤` `≥`) ask which way. A wrong pick shades
  the number line differently from the original's shading, side by side, and asks again. No stroke for the pick.
- Finish check: the final statement's solution set (one value, a ray with open or closed end, none, all) must equal
  the original's, computed exactly. It always does if only legal moves were used; the check guards the code.
- Try x slider in Range: tilt angle = sign(left − right) × min(14°, 3° + 2° × |left − right|); level only when
  equal (an open circle on the number line shows a boundary that is not included).
- Nothing waits for an animation: a move during a beam swing, a pop or a Replay ends that animation at once (Replay
  stops) and the move acts on the current equation.
- Keyboard: every move is a button; the term and number boxes accept Enter; Ctrl+Z is Undo.
- `window.__tool = {state, setMode, load(hole), move(name, arg), solution()}`.

## Look
Accent `--brand #7ddc72` (fairway green), `--brand-ink #062008`. The painted fairway (art: fairway) fills the stage,
dimmed to 60% under the beam so the cutouts and the equation stand out; the equation sits on a `#0f1c2a` band at 85%.
Balloons are painted red with a code minus glyph; bags are painted burlap with a code "x"; weights are painted iron
with dark numerals in code on a light `#e8edf3` label; true-shading on the number line `#7ddc72` with open or closed
circles. Contrast (computed): brand on panel 10.18:1, on --sec-bg 9.65:1, brand-ink on brand 10.14:1. Sign is shown
by glyph (weight vs balloon, minus mark) as well as color.

## Art
Local FLUX (`scripts/localart.py`); no people. One style: sunny painted illustration.
- fairway: "A sunny golf fairway seen from the side, mown stripes of green grass, a sand bunker and a few round trees,
  pale blue sky, painted illustration"; 16:9; cutout no; people no; stage background on every mode, dimmed.
- green-flag: "A putting green on a golf course with a flagstick standing in the cup, the flag a plain red cloth,
  late afternoon light, painted illustration"; 4:1; cutout no; people no; the band across the top of the hole card.
- Beam kit (8 cutouts, one shared prompt): "<piece>, seen from the front, soft daylight, painted illustration, plain
  white background"; 1:1 (beam 4:1); cutout yes; people no. Pieces: beam "a long polished wooden plank with brass end
  caps"; pivot "a sturdy iron stand shaped like a triangle with a round pin at the top"; pan "a shallow brass weighing
  pan hanging from three short chains"; weight "a gray iron block weight with a smooth blank front face and a small
  handle on top"; balloon "a round red balloon with a curled white string"; bag "a small tied burlap sack with a
  smooth blank front"; balloon-bag "a small tied burlap sack lifted by a red balloon on a string"; crate "a small
  wooden crate with a blank plank front". Sizing rule: the beam spans 70% of the stage width and pivots at the pivot's
  pin; the pivot is 30% of the stage height; each pan is 22% of the beam length and hangs from the beam end; weights,
  bags and crates fit a cell 44 to 64 px square, two rows of six per pan; balloons float one cell above their pan on
  their strings.
The equation, numerals, x and fraction marks on the pieces, group brackets and tags, the number line, the scorecard
and preview.svg are drawn in code.

## Voice
Bank voice `easy-coach` (relaxed sports coach). Not used by math 9-12 neighbors, group siblings or batch specs.
`Curio.voice`, scope = mode. The move log and cards are read on screen; Read speaks the hint.
- wRange (how; Range entered; stale after the first move): "Type an equation in Your equation, then tap a move. Slide Try x to see which values keep it true."
- wHoles (how; Front or Back nine entered; stale after the first move): "Tap a move in the bar, like Subtract or Divide. Each move on both sides is one stroke."
- groupTip (how; first hole with a group; stale after the first move on it): "Dividing the whole side can be cheaper than distributing. Your call."
- flip (how; first negative multiply or divide on an inequality; stale once a sign is picked): "Negative number, so the heavy side just swapped. Tap the new sign."
- declareHow (how; first time both sides are numbers or identical; stale once Declare is pressed): "Nothing left to solve for. Press Declare and pick what it means."
- holed (event; hole finished at or under par; stale on Next hole): "In the hole. That's par or better."
- over (event; finished over par; stale on Next hole): "Holed out. Press Replay and look for a shorter route."
- declareWrong (event; wrong Declare; stale after the next move): "That declare doesn't hold. Check the shading, then tap a move."

## Family engine
balance (`kit/balance.js`, inlined after `kit:curio`). This spec holds the full description for the family;
snack-scale (K), balance-the-beam (gr 1) and balance-puzzle (gr 6) reuse it.
- `Frac`: exact fractions (`Frac(3, 4)`, `.add .sub .mul .div .neg .cmp .toString({decimal})`).
- Model: an equation is `{left: Side, right: Side, rel: '=' | '<' | '>' | '<=' | '>=' | '?'}`; a side is a list of
  `{kind: 'num', a: Frac}`, `{kind: 'x', a: Frac}`, `{kind: 'group', k: Frac, items: [...]}`, or
  `{kind: 'icon', icon, n}` (K counts).
- `Balance.moves`: `add(eq, item)`, `sub`, `mul(eq, Frac)`, `div`, `distribute(eq, side, i)`, `tidy(eq)`,
  `swap(eq)` (also reverses an inequality's direction text), each pure and exact; `Balance.solutions(eq)` returns
  `{kind: 'one', x} | {kind: 'none'} | {kind: 'all'} | {kind: 'ray', at, dir, closed}`; `Balance.parse(text)`.
- `Beam(svgGroup, {width, height, skin: 'snack' | 'weights' | 'bags' | 'fairway', eq, x})`: draws the pivot,
  beam and pans; `set(eq)`, `tryX(x)` tilts by the side values (level only when equal); glyphs: icons (snack),
  weight blocks, balloons for negatives, bags for x, cut bags for fractions, group brackets with a multiplier tag,
  crates past 12 glyphs; pans move with the beam; Motion off sets angles instantly. Each skin may supply image
  cutouts for the beam, pivot, pans and glyphs; this tool's fairway skin uses the beam kit above.
- What each sibling feeds it: snack-scale: icon items, compare tilt, no x. balance-the-beam: number weights and a
  missing-weight box, level check. balance-puzzle: bags and positive weights, add and remove the same on both
  sides. This tool: negatives, groups, fractions, inequalities, the stroke count, par and the sign flip choice.

## Sources
- A-REI.A and A-REI.B: Common Core State Standards for Mathematics, High School Algebra, Reasoning with Equations and Inequalities, https://www.thecorestandards.org/Math/Content/HSA/REI/
- Properties of equality and inequality (multiplying or dividing by a negative reverses the inequality): OpenStax, Elementary Algebra 2e, 2.7 "Solve Linear Inequalities", https://openstax.org/books/elementary-algebra-2e/pages/2-7-solve-linear-inequalities
- Equations with no solution or every real number: OpenStax, Elementary Algebra 2e, 2.3 "Solve Equations with Variables and Constants on Both Sides", https://openstax.org/books/elementary-algebra-2e/pages/2-3-solve-equations-with-variables-and-constants-on-both-sides
- Golf score names (birdie, eagle, bogey): R&A and USGA, Rules of Golf definitions and glossary, https://www.usga.org/
- Checks run (Python, exact fractions, 2026-10-29): a breadth-first search over the move set above, with the
  dissolve and combine rules of this spec, finds the shortest route for all 18 holes; every par in Content matches it
  and every answer matches. Hole 11 reached par 1 only once Declare accepted identical sides (2x + 6 = 2x + 6); the
  first draft's Declare rule allowed only constant sides, so the rule now says both. The first draft's rule said
  "unequal constants" for No solution, which is wrong for inequalities (2 ≤ 5 is true); Declare now tests the truth
  of the constant statement. Range samples: 6(x − 1) = 3(2x − 2) reaches identical sides in 2 moves;
  1.5x − 2 ≥ 0.5x + 3 gives x ≥ 5 in 2. Tilt: difference 0.5 tilts 4°, 1 tilts 5°, 5.5 and more cap at 14°.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Hole 3 finishes in 2 strokes by Divide 4 then Subtract 1; Distribute first takes 3 and the card says bogey.
2. Hole 7: Tidy (no stroke) shows 5x/6 = 10; Multiply 6/5 finishes at 1 stroke, x = 12.
3. Hole 10 ends at −3 = 8; Declare No solution is accepted; Declare Every x works is refused with a stroke added.
4. Hole 11: after one Distribute, Declare Every x works is accepted (par 1).
5. Hole 15: Divide −4 shows "?" and the swing; picking `<` shows mismatched shading; `>` gives x > −2.
6. Hole 16 ends as −3 ≥ x and reads "x ≤ −3"; Range shading for the hole is the same before and after every move.
7. Divide by 0 and Multiply by 0 are refused without a stroke.
8. Focus: at 1366x768 and 1000x625 the beam with its pans is the largest thing on the stage and the equation sits right above it.
9. Tap while it plays: during a beam swing, a pop or a Replay, a move button acts at once on the current equation.
10. Each par in Content is confirmed by the build's search; best scores survive a reload and `Clear scores` clears them.
11. Every size in STANDARDS.md keeps the move bar and equation visible without page scrolling; keyboard-only play works; no voice line names a disabled control; console clean, no network.

## Open questions
- The module lists A-REI.B, which includes A-REI.B.4 (quadratics). launch-pad holds that code as its whole module, so this tool stops at linear. Also A-REI.B.3's "coefficients represented by letters" is left to model-my-world's formula rearranging. Fine?
- The beam kit adds image cutouts to the shared balance engine's Beam (a per-skin option). The other balance tools keep their own skins; is a painted kit wanted for them too when they are next touched?
