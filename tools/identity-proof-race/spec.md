# Identity Proof Race

## One idea
A proof is a lap: the two sides of an identity sit on a workbench, and you drag identity cards onto either side to
rewrite it until both sides read the same, racing a ghost of your own best time; every lap has more than one route,
the route map shows which ones you have found, and fake identity cards hide in the deck to cost you time when you
trust one.

## Not like
- undo-machine (gr 11, built): building inverse chains of function machines. Here inverse trig appears only as the
  calculator's one answer, and the dial shows the others.
- ferris-wheel (gr 11, built): sine as the height of a moving car. Here the trig functions are fixed and the work is
  rewriting expressions exactly.
- polar-rose-studio (this group): trig as a drawing pen. Here trig is algebra on the page, with no graph.
- function-family-reunion (this group): transformations seen on graphs. Here nothing is graphed; the proof is a chain
  of exact rewrites.
- hole-hunter (this group): factoring to find holes in a graph. Here factoring is one card among the identity cards.

## Who and how
Grade 12, precalculus and trigonometry. Students drive, 15 to 30 minutes, alone or as a class race (each student
against their own ghost). Explore first: Workbench opens on lap L1 with no clock.
Topic line: "Trig identities and equations".
Standards: F-TF.B (B.6 restricting a trig function's domain to invert it, B.7 solving trig equations with inverses),
F-TF.C (C.8 the Pythagorean identity, C.9 sum and difference formulas), AP-PRECALC.U3 (3.9 inverse trig functions,
3.10 trig equations and inequalities, 3.11 reciprocal functions, 3.12 equivalent representations: Pythagorean, sum and
difference, double angle).
tool.json: driver "students", minutes "15-30", modes ["Workbench", "Race", "Solve"].

## Screens and modes
Header (kit, 9-12 theme): "Identity Proof Race", small line "Make both sides match." Modes `Workbench`, `Race`,
`Solve`; kit `Motion`, `Sound`, `Read`.

Stage: a thin race lane across the top (your marker and, in Race, a ghost marker, both moving lap by lap); below it the
workbench: two plates, `Left side` and `Right side`, each showing its current expression in large math type with a
history of past lines under it (each line labeled with the card used); between them a status sign: "≠" while they
differ, "=" when they match.

Card tray (bottom or right): identity cards grouped by kind, each with its rule written out:
- Reciprocal: sec θ = 1/cos θ, csc θ = 1/sin θ, cot θ = 1/tan θ.
- Quotient: tan θ = sin θ/cos θ, cot θ = cos θ/sin θ.
- Pythagorean: sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, 1 + cot²θ = csc²θ (read either way).
- Sum and difference: sin(a ± b), cos(a ± b).
- Double angle: sin 2θ = 2 sin θ cos θ, cos 2θ = cos²θ - sin²θ.
- Cofunction: cos(π/2 - θ) = sin θ.
- Exact values: the unit circle values at multiples of π/6 and π/4.
- Algebra: Expand, Factor, Common denominator, Cancel, Simplify, Split the angle.
- Fakes (in Race, mixed into the tray, look like the others): sin(a + b) = sin a + sin b, sin 2θ = 2 sin θ,
  (a + b)² = a² + b², √(x²) = x.

### Workbench (explore, default)
- Lap picker L1 to L8. No clock, no fake cards. Drag a card (or select it and press Enter) onto a plate. If the card
  has several forms, a chooser lists all its forms; choosing one that has nothing to rewrite on that plate says
  "Nothing to rewrite here with that card" and changes nothing.
- `Undo` steps back one line on either plate. `Route map` (side panel) shows the lap's routes as a small graph of
  expressions; routes you have walked light up, others stay as dotted shapes with their length ("a 3 move route").
- When both plates match: the sign turns "=", the chain is printed as a two-column proof (statement, reason) with
  `Copy proof` (plain text to the clipboard).

### Race
- Track picker: `Sprint` (L1, L2, L5, T1, L3) or `Long track` (L4, L6, L7, T3, L8, T4). `Go` starts the clock.
- Identity laps work as on the Workbench, with the fake cards in the tray. Dropping a fake: the card greys out with
  its counterexample ("fails at a = 30°, b = 60°: 1 ≠ 1.366") and 5 s are added. The plate does not change.
- Trap laps (T1 to T4): a finished-looking proof is shown, one line of it wrong; click the bad line. Right: next lap.
  Wrong: 5 s added and the line you picked shows its value at the test angle matching the line above.
- Ghost: your best time on that track (per device) runs as the ghost marker, lap by lap. Finish card: time, penalties,
  routes found, and "New best" when it is. No other celebration.

### Solve
- Equation laps S1 to S8 on 0 ≤ x < 2π. Step 1, rewrite (same cards, one plate) until the equation is in a form like
  sin x = c, a product equal to 0, or tan x = c. Step 2, the unit-circle dial: tap points on the circle to mark every
  solution (snaps to multiples of π/12; for S6 and S7 free placement, read to 0.01 rad), or drag an arc for the
  inequality S8. `Lock in` checks the set.
- `Calculator` button for S6 and S7: arcsin or arccos gives one value and shades its restricted range on the dial
  ([-π/2, π/2] for arcsin, [0, π] for arccos), so the student finds the second solution by symmetry.

## Content
Identity laps (each line checked equal at θ = 0.7 when written; routes listed by cards):
- L1: sin θ cot θ = cos θ. Route: Quotient → sin θ cos θ / sin θ → Cancel → cos θ.
- L2: (1 - cos²θ)/sin θ = sin θ. Route: Pythagorean → sin²θ/sin θ → Cancel → sin θ.
- L3: sec²θ - tan²θ = 1. Route A: Pythagorean → 1 + tan²θ - tan²θ → Simplify → 1. Route B: Reciprocal → 1/cos²θ - tan²θ
  → Quotient → 1/cos²θ - sin²θ/cos²θ → Common denominator → (1 - sin²θ)/cos²θ → Pythagorean → cos²θ/cos²θ → Cancel → 1.
- L4: (sin θ + cos θ)² = 1 + sin 2θ. Route A: Expand → sin²θ + 2 sin θ cos θ + cos²θ → Pythagorean → 1 + 2 sin θ
  cos θ → Double angle → 1 + sin 2θ. Route B: Expand → Double angle → sin²θ + sin 2θ + cos²θ → Pythagorean → 1 + sin 2θ.
  Route C: work the right side, Double angle → 1 + 2 sin θ cos θ, and meet the left in the middle.
- L5: cos(π/2 - θ) = sin θ. Route A: Difference → cos(π/2)cos θ + sin(π/2)sin θ → Exact values → 0·cos θ + 1·sin θ →
  Simplify → sin θ. Route B: Cofunction, one move.
- L6: cos 2θ = 1 - 2 sin²θ. Route A (left): Double angle → cos²θ - sin²θ → Pythagorean → (1 - sin²θ) - sin²θ →
  Simplify → 1 - 2 sin²θ. Route B (right): Pythagorean on 1 → sin²θ + cos²θ - 2 sin²θ → Simplify → cos²θ - sin²θ →
  Double angle → cos 2θ.
- L7: sin 75° = (√6 + √2)/4. Route A: Split the angle 45° + 30° → Sum → sin 45° cos 30° + cos 45° sin 30° → Exact
  values → (√2/2)(√3/2) + (√2/2)(1/2) → Simplify → (√6 + √2)/4. Route B: split 120° - 45° → Difference → (√3/2)(√2/2) -
  (-1/2)(√2/2) → Simplify → (√6 + √2)/4. (Both ≈ 0.96593.)
- L8: tan θ + cot θ = sec θ csc θ. Route A: Quotient → sin θ/cos θ + cos θ/sin θ → Common denominator → (sin²θ +
  cos²θ)/(sin θ cos θ) → Pythagorean → 1/(sin θ cos θ) → Reciprocal → sec θ csc θ. Route B: Reciprocal on the right,
  → 1/(sin θ cos θ), and meet in the middle.
Values at θ = 0.7 (every line of a lap must equal these): L1 0.764842, L2 0.644218, L3 1, L4 1.98545, L5 0.644218,
L6 0.169967, L8 2.02953.

Trap laps (the claim is false; the bad line and its counterexample):
- T1: (sin θ + cos θ)² = 1. Lines: (sin θ + cos θ)² → sin²θ + cos²θ [bad: (a + b)² = a² + b²] → 1. At θ = π/4 the
  first line is 2, the second 1.
- T2: sin(θ + π/6) = sin θ + 1/2. Lines: sin(θ + π/6) → sin θ + sin(π/6) [bad: sin(a + b) = sin a + sin b] →
  sin θ + 1/2. At θ = π/3: 1 versus 1.366.
- T3: √(1 - cos²θ) = sin θ for every θ. Lines: √(1 - cos²θ) → √(sin²θ) [fine] → sin θ [bad: √(x²) = |x|]. At θ = 240°:
  0.866 versus -0.866.
- T4: tan θ + 1 = sec θ. Lines: 1 + tan²θ = sec²θ [fine, Pythagorean] → 1 + tan θ = sec θ [bad: square root of each
  term]. At θ = π/4: 2 versus 1.414.

Solve laps (solutions on 0 ≤ x < 2π):
- S1: 2 sin x - 1 = 0 → sin x = 1/2: π/6, 5π/6.
- S2: 2 cos²x - 1 = 0 → cos x = ±√2/2: π/4, 3π/4, 5π/4, 7π/4.
- S3: tan x = √3: π/3, 4π/3.
- S4: sin 2x = sin x → sin x (2 cos x - 1) = 0: 0, π/3, π, 5π/3.
- S5: 2 sin²x + sin x - 1 = 0 → (2 sin x - 1)(sin x + 1) = 0: π/6, 5π/6, 3π/2.
- S6: sin x = 0.3: arcsin 0.3 ≈ 0.3047, and π - 0.3047 ≈ 2.8369.
- S7: cos x = -0.6: arccos(-0.6) ≈ 2.2143, and 2π - 2.2143 ≈ 4.0689.
- S8: sin x ≥ 1/2: the arc from π/6 to 5π/6, both ends included.

## Interactions in detail
- No algebra engine: each lap is a hand-written state graph in the tool's data (states as display strings, edges as
  card, form and plate). A card applies only along an edge from the current state; this keeps every step exact and
  the routes known. A build test evaluates every state of every identity lap at θ = 0.4, 0.7 and 1.3 and fails if any
  differs from the lap's value by more than 1e-9.
- Plates match when they reach the same state id. Both plates can be worked in any order ("meet in the middle").
- Fakes: counterexamples are fixed per card (sin(a + b) at 30° and 60°; sin 2θ at 30°: 0.866 versus 1; (a + b)² at
  a = b = 1; √(x²) at x = -2). Penalties are 5 s each, shown on the clock as "+5".
- Solve check: the marked set must equal the solution set, each mark within 0.01 rad (snapped marks are exact);
  missing or extra marks are named ("one solution missing", "π/2 is not a solution: sin 2(π/2) = 0, sin(π/2) = 1"). The
  inequality arc must match its ends within 0.01 rad and include them.
- Times to 0.1 s. Best times per track per device (localStorage `curio-identity-proof-race`, try/catch) with
  `Clear times`; routes found per lap kept the same way.
- Sound: a short tick per accepted card, a low thud for a fake, a soft bell at lap end; off with Sound.
- Keyboard: cards are buttons (Enter picks one up, then Left or Right puts it on a plate); the dial is a radiogroup of
  24 points (arrows move, Space marks) plus a number box for free marks; trap lines are buttons.
- Motion off: no marker glide, cards apply instantly. Mode change: `Curio.stop()`, `V.hush()`, clock stops.

## Look
Accent (`--brand`) #ff5cf0, finish-line magenta: 6.6:1 on --panel #141b25, 6.3:1 on --sec-bg #18202b; --brand-ink #10161f
on it 7.0:1. Far more saturated than Image Transformer's violet #a58cff, Polar Rose Studio's #ff8ab6 and the algebra
group's #e59cff (Correlation Guessing Game); no 9-12 math neighbor uses it.
Scene: a dark track lane #111821 with lane lines #2b3442, your marker the accent, the ghost marker #9aa6b4 at 60 percent
with a dashed outline; plates #18202b with a 1 px #2b3442 border, expressions #e8edf3 (over 13:1). Card kinds get a
left stripe: Pythagorean `--gr-1`, sum and difference `--gr-2`, double angle `--gr-3`, reciprocal and quotient
#c9b48a, algebra #8a96a3. Fakes wear the stripe of the kind they imitate. The "=" sign glows in the accent; "+5" in
`--gr-4`.

## Art
none: drawn in code (lane, plates, cards, dial, route map, preview.svg).

## Voice
`hero-coach` (Puck), style "Say briskly and steadily, like a track coach calling splits, and keep it short." Not used
by a group sibling or 9-12 math neighbor (lively-host is taken by Correlation Guessing Game in the algebra group). `Curio.voice`, `scope: () => state.mode`.
- bench (how, Workbench welcome): "Drag a card onto either side. Make both sides match."
- routes (how, first lap finished): "Open the route map. There is another way to the same proof."
- race (how, Race welcome): "Press Go. Fake cards hide in the tray, and each one costs five seconds."
- trap (how, first trap lap): "One line of this proof is wrong. Click it."
- solve (how, Solve welcome): "Rewrite first, then mark every solution on the circle."
- calc (how, first Calculator use): "The calculator gives one answer. Use the circle to find the other."
- best (event, a new best time; stale on the next Go): "New best time."

## Family engine
none. The state-graph proof format (laps as hand-written graphs of exact states, checked numerically at build) is
this tool's own; it could serve a later algebra proof tool, but no family is defined now.

## Sources
- Pythagorean, reciprocal, quotient, sum and difference, double angle and cofunction identities; inverse trig ranges;
  solving trig equations and inequalities: OpenStax, Precalculus 2e, 7.1 "Solving Trigonometric Equations with
  Identities", 7.2 "Sum and Difference Identities", 7.3 "Double-Angle, Half-Angle, and Reduction Formulas", 7.5
  "Solving Trigonometric Equations" and 6.3 "Inverse Trigonometric Functions",
  https://openstax.org/books/precalculus-2e/pages/7-1-solving-trigonometric-equations-with-identities
- Standards: Common Core F-TF.B and F-TF.C, https://www.thecorestandards.org/Math/Content/HSF/TF/ ; College Board, AP
  Precalculus CED (2023), Unit 3, https://apcentral.collegeboard.org/courses/ap-precalculus
- Laps, traps and equations are made up; every state value and solution computed in Python (2026-10-27).

## Done when
1. L3 can be finished by Route A in two moves and by Route B in five; the route map lights each when walked.
2. L4 Route C (right side Double angle, left side Expand and Pythagorean) matches in the middle at 1 + 2 sin θ cos θ.
3. L5 by Cofunction in one move; by Difference, Exact values and Simplify in three.
4. The build test passes: every state of L1 to L8 equals the lap value at θ = 0.4, 0.7 and 1.3 (L4 at 0.7: 1.98545).
5. In Race, dropping "sin 2θ = 2 sin θ" greys it with "fails at 30°: 0.866 ≠ 1" and adds 5 s; the plate is unchanged.
6. T3: clicking the line "sin θ" is right; clicking "√(sin²θ)" adds 5 s.
7. S4 accepts {0, π/3, π, 5π/3} and names π/2 as not a solution if marked; S6 accepts 0.30 and 2.84; S8 accepts the
   arc π/6 to 5π/6.
8. A second Sprint run shows the ghost moving at the first run's lap times; "New best time." spoken only on a better
   time.
9. Plates, tray and lane visible at 1366x768; at 760 wide the tray sits under the plates; math type at least 10 px in
   the 680x425 preview; no network, no images, no em dashes.

## Open questions
- identity-proof-race: F-TF.B.5 (choosing trig functions to model periodic situations) is in the module's F-TF.B cluster but is not taught
  here; ferris-wheel (gr 11) already does it. Also AP-PRECALC.U3 includes 3.1 to 3.8 (sine and cosine graphs and
  their transformations) and 3.13 to 3.15 (polar), which this tool does not teach (polar-rose-studio and
  function-family-reunion carry parts). Keep the Standards line as the module's codes, or narrow it?
- identity-proof-race: Fake cards in the tray could feel like trickery to some students; they appear only in Race. Agree?
