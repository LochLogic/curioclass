# Undo Machine

## One idea
Number tokens ride out along a chain of machines and must ride home along the undo chain you build, so you feel why
undoing goes in reverse order, and you watch two different tokens crash into the same output when a machine forgets
something (squaring, absolute value, rounding) until a gate on the input fixes it.

## Not like
- rule-machine (grade 4): there the rule is hidden and you guess it from inputs and outputs; here every rule is in plain sight and the job is to reverse a chain of them.
- function-machine-factory (grade 8): there one machine is rejected for giving two outputs for one input; here the machine is fine and it is the undo that breaks, because two inputs gave one output (one-to-one, not "is it a function").
- function-family-reunion (grade 12): there sliders transform parent graphs; here there are no sliders, and the graph is only a mirror check across y = x.
- image-transformer (grade 12): there order matters for matrices on a photo; here order matters because undo runs backward, with numbers, no images.
- transformation-golf (grade 10): there you move shapes with the fewest moves; here nothing is counted, a chain either brings every token home or it does not.
- rollercoaster-polynomials, ferris-wheel (grade 11 batch): they share the graphing engine only; no scenario overlap.

## Who and how
- Grade 11, math (Algebra 2 / Functions), module "Building and Inverting Functions".
- Driver: students, on their own laptops. 15 to 30 minutes.
- Standards: F-BF.A.1c (compose functions), F-BF.B.4a (write an inverse), F-BF.B.4b (verify by composition),
  F-BF.B.4c (read inverse values from a graph or table), F-BF.B.4d (make a function invertible by restricting the
  domain), F-BF.B.5 (exponents and logs are inverses).
- Look: 9-12 dark instrument panel. Link `kit:curio`, then `kit:theme-912`, then `kit:graphing`. Own `--brand`
  accent: a copper orange that passes AA on the theme's `--panel`. No confetti, no mascot.

## Screens and modes
Header: title "Undo Machine", mode tabs `Workshop` and `Puzzles` (`.seg`), icon buttons `Motion`, `Sound`, `Read`.
Opens in Workshop. Stage on the left (the machine floor), panel on the right (`.panel`, hint paragraph id `hint`).

**The machine floor (both modes).** A wide dark stage with two conveyor lines drawn in code (SVG):
- Top line, "Forward", runs left to right from a `HOME` dock on the left to an `OUT` bin on the right. Up to 6 machine
  slots. The optional gate sits just right of HOME.
- Bottom line, "Undo", runs right to left from `OUT` back to `HOME`. Up to 8 undo slots. A curved chute joins OUT to
  the start of the undo line, so a token visibly drops from the top line onto the bottom line and travels home.
- Each machine is a boxy card with a big symbol, its name, and its parameter (for parts that have one) with `-` and
  `+` steppers. A small `x` removes it. `<` and `>` on the focused card move it one slot.
- Parts bin (in the panel, scrollable): every part in Content, each a card to drag or tap.
- Formula strip above the floor: `f(x) = ...` built from the forward line, `g(x) = ...` built from the undo line,
  and after a full success `g(x) = f⁻¹(x)` with the line "g(f(x)) = x for every token that got through".

**Workshop (free explore).** Build any forward chain, build any undo chain, run tokens.
- Buttons: `Run` (sends the 8 test tokens), a number box plus `Send my number` (one token of your own),
  `Gate` (toggle), `Graph` (toggle the graph view in the panel), `Random chain`, `Clear undo`, `Clear all`.
- Gate controls (shown when Gate is on): a `≥` / `≤` switch and a value stepper from -10 to 10. The gate label reads
  live, for example "Only x ≥ -3 may enter".
- Verdict light on the panel, always word plus icon: `Undoes it` (all tokens home), `Some tokens lost` (names them),
  `Can't be undone as built` (collision found, see below), `Nothing got through` (every token rejected).

**Puzzles (optional challenge).** Level picker `1` to `12` across the top of the panel, each with its title and a
check mark once solved (remembered in localStorage `curio-undo-machine-solved`, wrapped in try/catch). The forward
line is locked (cards dimmed, no `x`, no steppers) except in level 11. The panel shows the goal text.
- Buttons: `Run`, `Hint`, `Can't be undone`, `Reset puzzle`, `Next puzzle` (enabled once solved), `Graph`, plus the
  `Gate` controls on levels 7 to 10 only.

**Graph view (panel, either mode).** Plane from `kit:graphing`, x and y from -10 to 10, grid 1, labels every 5.
- f plotted with `--gr-1`, the undo chain g with `--gr-2` (dashed), the line y = x with `--gr-3` (dotted), each with
  its equation in text. The gate shows as a shaded band on the x axis over the inputs it blocks.
- `Mirror` button: draws the reflection of f across y = x as a parametric curve (x = f(t), y = t over the gated
  domain), morphing from f over 1.2 seconds (instant when Motion is off). If g is right, the mirror lands on g.
- If f is not one-to-one, the mirror curve fails the vertical line test: the tool draws a vertical line at the
  collision output, marks its two hits, and labels it "One output, two ways back: the undo is not a function".

## Content
Parts (the function-machine block defines each: symbol, name, parameter range, rule, domain, formula template,
partner undo, kind):

| Part | Rule | Parameter a | Domain | Undone by | Kind |
|---|---|---|---|---|---|
| Add a | x + a | 1 to 20 | all | Subtract a | one-to-one |
| Subtract a | x - a | 1 to 20 | all | Add a | one-to-one |
| Multiply by a | a·x | -10 to 10, not 0 | all | Divide by a | one-to-one |
| Divide by a | x / a | -10 to 10, not 0 | all | Multiply by a | one-to-one |
| Flip sign | -x | none | all | Flip sign | one-to-one, self-undoing |
| Reciprocal | 1 / x | none | x ≠ 0 | Reciprocal | one-to-one, self-undoing |
| Square | x² | none | all | Square root, only when inputs were 0 or more | folds at 0 |
| Square root | √x (principal) | none | x ≥ 0 | Square | one-to-one |
| Cube | x³ | none | all | Cube root | one-to-one |
| Cube root | ∛x | none | all | Cube | one-to-one |
| Power of 2 | 2^x | none | all | Log base 2 | one-to-one |
| Log base 2 | log₂ x | none | x > 0 | Power of 2 | one-to-one |
| Absolute value | abs(x) | none | all | nothing, unless inputs were all 0 or more (or all 0 or less) | folds at 0 |
| Round | nearest whole number, halves up: floor(x + 0.5) | none | all | nothing | many-to-one |
| Always 5 | 5 | none | all | nothing | many-to-one |

Default parameter when a part is dropped: Add 3, Subtract 3, Multiply by 2, Divide by 2.

Formula templates (□ is the inner expression): `□ + a`, `□ - a`, `a□`, `□ / a`, `-□`, `1 / (□)`, `□²`, `√(□)`,
`□³`, `∛(□)`, `2^(□)` (drawn as a superscript), `log₂(□)`, `|□|`, `round(□)`, `5`. Wrap □ in parentheses when it
is not a bare `x` and the template is multiply, divide, flip, square or cube. A negative a in multiply shows `-3(□)`.
No algebraic simplifying. Example: Multiply by 3 then Add 4 gives `f(x) = 3x + 4`.

Test tokens (fixed, round chips showing their value): -6, -2.5, -1, 0, 0.5, 2, 3, 9.

Puzzles (goal text in quotes; any undo chain that brings every token home counts, not only the listed answer):

| # | Title | Forward line | Goal | One answer |
|---|---|---|---|---|
| 1 | Warm-up | Add 5 | "Bring every token home." | Subtract 5 |
| 2 | Socks and shoes | Multiply by 3, Add 4 | "Bring every token home." | Subtract 4, Divide by 3 |
| 3 | Three steps | Subtract 2, Multiply by 5, Add 1 | "Bring every token home." | Subtract 1, Divide by 5, Add 2 |
| 4 | Cubed | Cube, Subtract 8 | "Bring every token home." | Add 8, Cube root |
| 5 | Its own undo | Reciprocal | "Bring every token home with one machine." | Reciprocal |
| 6 | Exponent and log | Power of 2, Multiply by 3 | "Bring every token home." | Divide by 3, Log base 2 |
| 7 | The crash | Add 3, Square | "Make it undoable with a gate, then undo it." | Gate x ≥ -3: Square root, Subtract 3. Or gate x ≤ -3: Square root, Flip sign, Subtract 3 |
| 8 | Forgetful | Absolute value, Add 1 | "Make it undoable with a gate, then undo it." | Gate x ≥ 0: Subtract 1. Or gate x ≤ 0: Subtract 1, Flip sign |
| 9 | Lost for good | Round, Multiply by 2 | "Undo it, or show it can't be done." | Press Can't be undone |
| 10 | Deep fold | Square, Add 1, Reciprocal | "Make it undoable with a gate, then undo it." | Gate x ≥ 0: Reciprocal, Subtract 1, Square root. Or gate x ≤ 0: the same, then Flip sign |
| 11 | Mirror machine | (you build it) | "Build a 2-machine chain that undoes itself. It must change at least one number." | Flip sign, Add 10 (that is 10 - x); or Reciprocal, Flip sign |
| 12 | Long way home | Subtract 1, Cube, Multiply by 2, Add 7 | "Bring every token home." | Subtract 7, Divide by 2, Cube root, Add 1 |

Any gate value that removes the collision solves levels 7, 8 and 10 (level 7: x ≥ c with c ≥ -3, or x ≤ c with
c ≤ -3; levels 8 and 10: x ≥ c with c ≥ 0, or x ≤ c with c ≤ 0), as long as at least one token gets through.

Hints (one per press, in order, then the last repeats):
- Undo levels (1 to 6, 12): 1 "Start at the OUT end. What was the last thing done?" 2 "Each machine is undone by its opposite: add and subtract, multiply and divide, cube and cube root, power of 2 and log base 2." 3 shows the first missing undo part as a ghost card in its slot.
- Levels 7, 8, 10: 1 "Press Run. Which two tokens crashed into the same output?" 2 "The crash happens at the fold. Keep the numbers entering it all on one side of zero." 3 sets the gate switch to ≥ and leaves the value for the student.
- Level 9: 1 "Press Run with any undo line. Do 0 and 0.1 come out the same?" 2 "If two inputs give one output, no machine can know which one to send back."
- Level 11: 1 "Flip sign undoes itself. What could you add after it so the pair still does?" 2 "Try sending x to 10 minus x. What happens if you do it twice?"

## Interactions in detail
- **Placing:** drag a part from the bin onto a slot, or tap a part (it lifts, `aria-pressed`) and then tap a slot.
  Keyboard: Tab to a part, Enter lifts it, arrow keys pick a slot, Enter drops, Escape cancels. Dropping on a filled
  slot inserts and shifts the rest right. A full line refuses with the hint "This line is full (6 machines)" or
  "(8 machines)".
- **Editing:** steppers change a by 1 and skip 0; Delete or the `x` removes; `<` `>` (or `[` `]` on the focused card)
  reorder. Any edit stops a run in progress and clears token results and the verdict.
- **Run:** tokens leave HOME one after another, 0.25 seconds apart, about 0.4 seconds per machine. A readout above
  each card shows the value that just left it. Values show up to 4 decimal places with trailing zeros cut; beyond
  1,000,000 in size, scientific notation (for example 7.29e+8). `Send my number` takes any finite number typed in;
  anything else gives the hint "Type a number, like -2.5".
- **Rejections:** a token stops, dims and gets a tag when blocked by the gate ("gate"), outside a machine's domain
  ("√ needs 0 or more", "log₂ needs more than 0", "1/x can't take 0"), or not finite ("too big"). Rejected on the
  forward line means not counted. Rejected on the undo line means lost.
- **Home check:** a token is home if |result - start| ≤ 1e-9 × max(1, |start|). Home tokens settle into HOME; one soft
  Curio.yes per run when all are home, not per token. Lost tokens stop in a "Lost" tray under HOME with a line such as
  "-1 came back as 1".
- **Verdict:** `Undoes it` needs at least one token through the forward line and every such token home, and no
  collision. An empty undo line means g is "do nothing", which only works when the forward line is empty too.
- **Collision check (after every edit, no animation):** track the set of values that can enter each machine as a
  union of intervals, starting from all real numbers or the gate's ray, pushed through each part (monotone parts map
  interval ends, decreasing ones swap them; reciprocal splits at 0; domain limits trim). A fold part (Square, Absolute
  value) is safe only if its entering set lies inside [0, ∞) or inside (-∞, 0]. Round and Always 5 are never safe.
  If any part is unsafe, find a collision pair: try inputs 0, 1, -1, 2, -2 and so on to ±10, then the tenths from
  -10 to 10 in the same near-zero-first order, keep only inputs the gate and domains allow, and stop at the first
  input whose output equals an earlier one's. Show the pair as two chips on the OUT bin, for example "-2 and -4 both
  come out as 1". Verdict `Can't be undone as built`, even if some tokens happened to get home.
- **Can't be undone (puzzles):** on level 9 it solves the level and shows the collision pair with "Two inputs, one
  output. Nothing can send it back." On levels 7, 8, 10 before a working gate: "As built, no. But a gate can fix
  this one." On every other level: "This one can be undone. Run your undo line to test it."
- **Level 11:** the forward line is unlocked and limited to 2 slots; the undo line is hidden and Run sends each token
  through the forward line twice (the second lap drawn on the bottom line). Solved when both slots are filled, every
  token that gets through is home, and at least one token was changed by one lap.
- **Gate:** only at the start of the forward line. Switching it on sets `≥ 0`. Blocked tokens never leave HOME.
- **Random chain (Workshop):** 3 parts with random parameters; 3 times in 4 they are all one-to-one parts, otherwise
  one is Square or Absolute value. Clears the undo line and the gate.
- **Mode switch:** Workshop and Puzzles each keep their own lines while the page is open; Curio.stop() on switch.
- **Reset puzzle** restores the level's forward line, empties the undo line, turns the gate off, resets hints.
- **Clear all** empties both lines and turns the gate off. **Clear undo** empties only the bottom line.
- **Motion off:** tokens jump machine to machine with the same step timing; the mirror morph is instant.
- **Read:** reads the goal (Puzzles) and the current verdict through readFallback, else the hint.
- **Small screens:** under about 900 px wide the panel goes below the stage; Curio.fit scales the floor (design size
  1200 x 560).

## Art
none: drawn in code. Machines, conveyors, tokens, gate and chute are SVG shapes on the theme colors.
(Optional, only if the builder wants texture: "dark brushed steel plate with faint rivets, even lighting, no text";
16:9; cutout no; people no.)

## Voice
`"bank": "hs-narrator"`, `"voice": "Kore"`, `"style": "Read clearly and naturally, at a moderate pace"`.
Lines (11):
1. workshop-welcome: "Welcome to the Undo Machine. Build a chain on the top line, then build the chain that brings every number home on the bottom line."
2. workshop-run: "Press Run to send the test numbers through. Each one rides out on top and has to ride home on the bottom."
3. puzzles-welcome: "Twelve puzzles. Each one gives you a chain of machines. Your job is to bring every number home."
4. order-hint: "Start at the out end. The last thing done is the first thing to undo."
5. collision-found: "Two different numbers just came out the same. Once that happens, no machine can know which one to send back."
6. gate-intro: "A gate decides which numbers may enter. Keep everything entering the fold on one side of zero, and the crash goes away."
7. all-home: "Every number made it home. Your bottom line is the inverse."
8. some-lost: "Some numbers came home as something else. Check the lost tray to see where they ended up."
9. graph-intro: "The graph shows your chain, your undo chain, and the line y equals x. Press Mirror to flip your chain across that line."
10. mirror-fails: "The mirror image has two points above one input. That flipped graph is not a function, so the chain can't be undone as built."
11. self-undo: "Puzzle eleven. Build a two machine chain that undoes itself, so doing it twice brings every number home."

When they play: 1 on the first tap in Workshop, 2 the first time a forward line has a machine and nothing has run,
3 on the first open of Puzzles, 4 with the first Hint on an undo level, 5 the first time a collision appears,
6 the first time the gate is shown, 7 and 8 at most once each per mode per session, 9 on the first Graph open,
10 the first time Mirror shows a two-hit line, 11 on opening level 11. Each at most once per session unless Read is
pressed.

## Family engine
function-machine has no doc or kit file yet. Keep the logic in one block marked
`/* ==== FUNCTION-MACHINE ENGINE (lift to kit/function-machine.js later) ==== */`: the part table (rule, domain,
template, partner, kind), chain run with per-step values and rejections, formula builder, interval tracker and
collision finder. Nothing in that block touches the DOM.
Also uses `kit:graphing` (built by rollercoaster-polynomials): `Plane`, `g.fn`, `g.param` (mirror), `g.segment`
(vertical line), `g.point` (collision hits), `g.clear`. And `kit:theme-912` for colors.

## Sources
- Common Core State Standards, High School Functions, Building Functions (F-BF.A.1c, F-BF.B.4a to 4d, F-BF.B.5): https://www.thecorestandards.org/Math/Content/HSF/BF/
- OpenStax, Precalculus 2e, 1.4 Composition of Functions: https://openstax.org/books/precalculus-2e/pages/1-4-composition-of-functions
- OpenStax, Precalculus 2e, 1.7 Inverse Functions (one-to-one functions, undoing in reverse order, restricting the domain of x squared, the graph of an inverse reflects across y = x): https://openstax.org/books/precalculus-2e/pages/1-7-inverse-functions
- OpenStax, Precalculus 2e, 6.3 Logarithmic Functions (log base b undoes b to the x): https://openstax.org/books/precalculus-2e/pages/6-3-logarithmic-functions
- Puzzle answers are checked by direct arithmetic, for example level 7 with gate x ≤ -3 and x = -5: -5 + 3 = -2, squared 4, root 2, flipped -2, minus 3 gives -5.

## Done when
1. In Workshop, Multiply by 3 then Add 4 with undo Divide by 3 then Subtract 4 loses tokens (2 comes back as -0.6667); swapping the undo order to Subtract 4, Divide by 3 brings all 8 home and shows `g(x) = f⁻¹(x)`.
2. Add 3 then Square with no gate shows "-2 and -4 both come out as 1" and `Can't be undone as built`; setting the gate to x ≥ -3 removes the collision, blocks -6 at the gate, and Square root, Subtract 3 brings the other 7 home.
3. A lone Log base 2 rejects -6, -2.5, -1 and 0 with the tag "log₂ needs more than 0", and they do not count against the verdict.
4. All 12 puzzles solve with the answers in the table, the alternate answers (the x ≤ gate routes) also solve, and the check marks survive a reload.
5. Level 9's `Can't be undone` solves it and shows the pair 0 and 0.1; the same button on level 2 says the chain can be undone.
6. Level 11 accepts Flip sign then Add 10, rejects Add 3 then Subtract 3 (changes nothing), and rejects a single machine.
7. Graph view shows f, g and y = x with text equations; Mirror of Cube lands on Cube root; Mirror of Square with no gate shows the two-hit vertical line and its label.
8. Every control works from the keyboard with visible focus, targets are 44 px or more, verdicts use words and icons not only color, and Motion off makes tokens jump with the same step timing.
9. The chain Cube, Cube, Power of 2 tags 9 as "too big" instead of breaking, and no console errors appear in any mode.
10. It uses the 9-12 dark theme, text passes AA, there is no confetti, and the file makes no network requests.
