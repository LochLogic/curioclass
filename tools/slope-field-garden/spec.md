# Slope Field Garden

## One idea
A differential equation is a field of grass blades, each blade tilted to the slope dy/dx the equation gives at that
spot; plant a seed anywhere and a vine grows by always following the blades, so every vine is one solution, the seed
is its starting condition, and changing the equation re-combs the whole garden at once.

## Not like
- rain-gauge (this group): a rate that depends only on time, added up into an amount. Here the rate depends on where
  you are, including the amount itself, and the answer is a whole family of curves.
- outbreak-model (gr 11, built): an exponential formula given up front, solved with logarithms. Here the formula comes
  last: the field comes first, the vine shows the shape, then separation of variables names the curve.
- speedometer (this group): finding a rate from a position formula. Here the rate rule is given and the curve is found.
- function-family-reunion (this group): a curve moved by sliders. Here no curve is chosen; the field decides where it
  goes.

## Who and how
Grade 12, AP Calculus (Differential Equations). Students drive, 20 to 40 minutes, free play first. Sandbox: no wrong
answers; the garden only shows what each equation does. Explore first: Garden opens on dy/dx = x + y with one vine
already growing from (0, 1).
Topic line: "Slope fields and differential equations".
Standards: AP-CALC.U7 (7.1 modeling with differential equations, 7.2 verifying solutions, 7.3 to 7.4 sketching and
reasoning with slope fields, 7.5 Euler's method (BC), 7.6 to 7.7 separation of variables and particular solutions,
7.8 exponential models, 7.9 logistic models (BC)).
tool.json: driver "students", minutes "20-40", modes ["Garden", "Step by step", "Models"].

## Screens and modes
Header (kit, 9-12 theme): "Slope Field Garden", small line "Every blade is a slope." Modes `Garden`, `Step by step`,
`Models`; kit `Motion`, `Sound`, `Read`.

Stage: an engine plane (window -5 to 5 in both directions by default) drawn as a raised garden bed: painted soil (art:
soil-bed) clipped to the plane, framed by four painted cedar planks (art: bed-plank) along its edges, and a grid of
short grass blades in code (one every half unit, 21 by 21), each tilted to f(x, y) there. Vines are smooth code curves
in the accent with a painted leaf (art: vine-leaf) every unit, turned to the vine's direction; each seed point shows a
painted sprouting seed (art: seed-sprout). Tapping or clicking the bed plants a seed; the vine grows both ways from it
(forward and back in x) over about 1.5 s (instant with Motion off).

Panel: equation picker (cards E1 to E6 and `Your own`), a `Your own` box "dy/dx = ..." taking x and y, the seed list
(each seed's point, with a remove button), `Clear garden`, and the readouts for the last seed: "seed (a, b)", "slope
there = ...".

### Garden (explore, default)
Focus: the bed, square and central, the largest thing on the stage, with the blades and vines; the panel stays beside
it (under it below 1000 px wide).
- Pick an equation; the blades turn to it (a short sweep, instant with Motion off) and every planted vine regrows.
- Plant up to 8 seeds. Hovering the bed shows "slope at (x, y) = ..." and highlights the blade.
- `Isoclines` toggle: draws the curves where the slope is 0 (and 1 and -1) as thin dashed lines, so students see
  where vines turn flat.
- `Name the vine` (for E1 to E6): shows the separated work for the last seed and its particular solution, written
  out (for example "dy/y = dx, ln|y| = x + C, y = 3e^x for the seed (0, 3)"). For E4 (not separable) it says so and
  gives the known solution with a line naming it as a linear equation, not taught here.
- `Check a guess`: type a function "y = ..." in its box and press `Check`; the garden draws it in `--gr-2`; the panel
  says "fits the field" when it follows the blades everywhere in view, or "leaves the blades near (x, y)" naming the
  first spot it does not (a ring marks the spot). Nothing is graded; this is the AP "verify a solution" move made
  visible.

### Step by step (Euler, BC)
Focus: the ladybug's straight steps and the true vine beside them on the bed, which keeps its full size; the table
sits in the panel.
- A ladybug (art: ladybug, rotated to each step's direction) walks from the seed in straight steps of size h (buttons
  `1`, `0.5`, `0.25`, `0.1`): at each stop she reads the blade under her and walks that slope for one step. Each step
  is drawn as a straight segment with a dot; the true vine stays drawn beside it.
- `Step` adds one step, `Walk to x = ...` (a box and a `Walk` button) runs to that x (each step about 150 ms, instant
  with Motion off). Table: step, x, y, slope, next y.
- Readout: "Euler y = ..., true y = ..., gap = ...", and the line "Smaller steps, smaller gap."

### Models
Focus: the bed relabeled as the model's axes with its vine and the time line, the largest thing on the stage; the
card's painted picture is a small header in the panel.
Three cards, each a garden with labeled axes (t across, the amount up) and one seed already planted:
- M1 Cooling cocoa (art: model-cocoa): dT/dt = -0.08(T - 20), T(0) = 90 (degrees C, minutes). Room line at T = 20
  dashed.
- M2 Bacteria (art: model-petri): dP/dt = 0.3P, P(0) = 100 (hours).
- M3 Fish pond (art: model-pond): dP/dt = 0.4P(1 - P/500), P(0) = 50 (years). Carrying capacity line at 500 dashed.
Each card has a time slider and readouts (value at time, rate at time), plus `Plant another start` to see other
starting values. `Name the vine` shows the solution formula and one question answered in the open (cocoa: when it
reaches 60 degrees; bacteria: doubling time; fish: when the pond is half full and how fast it grows then).

## Content
Equations (particular solutions for named seeds; exact):
| Card | dy/dx | General solution | Seed and particular solution |
|---|---|---|---|
| E1 Ramp | x | y = x²/2 + C | (2, 0): y = x²/2 - 2; at x = 3, y = 2.5 |
| E2 Grow | y | y = Ce^x | (0, 3): y = 3e^x; at x = 1, y ≈ 8.1548 |
| E3 Ring | -x/y | x² + y² = C (y not 0) | (0, 2): the upper half of x² + y² = 4 |
| E4 Drift | x + y | y = Ce^x - x - 1 | (0, 1): y = 2e^x - x - 1; at x = 1, y = 2e - 2 ≈ 3.4366 |
| E5 Bell | -xy | y = Ce^(-x²/2) | (0, 2): y = 2e^(-x²/2) |
| E6 Wave | cos x | y = sin x + C | (0, 0): y = sin x |
E3 vines stop where they meet the x-axis (the slope is undefined there); the panel says "the slope is undefined on
y = 0, so the vine ends here." E4 is the one card that does not separate.

Euler (E4 from (0, 1) to x = 1; true 3.4366): h = 1: 2; h = 0.5: 1 → 1.5 → 2.5; h = 0.25: 2.8828; h = 0.1: 3.1875.
Euler (E2 from (0, 1) to x = 1; true e ≈ 2.7183): h = 0.5: 2.25; h = 0.25: 2.4414; h = 0.1: 2.5937.
(Euler is always under the true vine on E2 and E4 because those vines curve up.)

Models (made up, values like a classroom textbook):
- M1: T = 20 + 70e^(-0.08t). At t = 10, T ≈ 51.5. Reaches 60 when t = ln(70/40)/0.08 ≈ 7.0 minutes.
- M2: P = 100e^(0.3t). Doubling time ln 2 / 0.3 ≈ 2.31 hours; at t = 5, P ≈ 448.
- M3: P = 500 / (1 + 9e^(-0.4t)). Half full (250) at t = ln 9 / 0.4 ≈ 5.49 years, where it grows fastest: 0.4 x 250 x
  0.5 = 50 fish per year. At t = 5, P ≈ 225; at t = 10, P ≈ 429. Euler with h = 1 from 50: 68, then 91.5.

## Interactions in detail
- Vines are grown with fourth order Runge-Kutta, step 0.01, both directions from the seed, stopping at the window edge,
  at a point where f is undefined or not finite, where y would change sign on a field undefined at y = 0, or after
  2,000 steps; the Euler walk uses exactly Euler's rule with the chosen h. The table prints 4 decimals, trailing zeros
  dropped.
- `Your own` parser (the tool's own, same grammar as speedometer's: numbers, x, y, + - * / ^, parentheses, sin, cos,
  tan, exp, ln, sqrt, abs, pi, e). A bad entry keeps the old field and says "I can't read that yet." Evaluation that
  gives a non-finite number draws no blade at that spot.
- Check a guess: the guess g(x) is sampled at 41 points across the view where it is on screen; at each, g'(x) by a
  central difference (step 1e-4) is compared with f(x, g(x)); it "fits" when every gap is under 1e-3 times (1 + |f|).
- Blade length is fixed (0.35 units on screen); steep blades are drawn vertical-leaning, never clipped into other
  cells. Isoclines are drawn by marching squares on f - m over a 101 by 101 grid.
- Models: axes relabel (t, T or P) and window to fit (M1 t 0 to 40, T 0 to 100; M2 t 0 to 12, P 0 to 4000; M3 t 0 to
  20, P 0 to 600). Blades are scaled to the axes so their tilt matches the true slope on screen.
- Taps while it plays: while a vine grows or the blades sweep, planting another seed, removing one or picking a new
  equation acts at once (the growing vine finishes on that frame and the new action starts); during a `Walk`, `Step`,
  a new h or a new seed stops the walk and shows the result at once.
- Sound (on as the kit sets it): a soft rustle when the blades turn and a small chime when a vine finishes growing;
  off with Sound.
- Keyboard: a focus cursor on the bed (arrow keys move it by half a unit, Enter plants a seed); seed list items have
  remove buttons; the h buttons, `Step` and `Walk` are in tab order; Enter in the guess box presses `Check`.
- Mode change: `Curio.stop()`, `V.hush()`. The garden for each equation is kept per device (localStorage
  `curio-slope-field-garden`, try/catch), `Clear garden` empties it.

## Look
Accent (`--brand`) #52f05a, new-leaf green: 11.52:1 on --panel #141b25, 10.91:1 on --sec-bg #18202b; --brand-ink #10161f
on it 12.08:1. Brighter than the grade 11 green #2fa37a and the algebra group's #7ddc72 (Equation Golf), and far from
Zoom to the Limit's lime #c6f25a.
Scene: a moonlit garden bed; the painted soil (dark brown, about #1b1712) and weathered cedar planks set the palette.
Code over it: blades #8fae7a (light enough to read, quieter than the vines), vines in the accent, Euler steps `--gr-4`
with dots, guessed curves `--gr-2`, isoclines `--gr-1` dashed, model reference lines (room temperature, carrying
capacity) #c9b48a dashed with labels; axis labels on a #10161f chip at 85 percent so they read over the soil.

## Art
Local FLUX (`scripts/localart.py`); no people. One style: soft painted illustration, cool moonlight with warm wood.
- soil-bed: "Top-down view of dark rich garden soil with faint raked furrows and a few small pebbles, even soft
  moonlight, soft painted illustration, full frame texture"; 1:1; cutout no; people no; clipped to the plane under the
  blades (dimmed 20 percent so blades and vines read).
- bed-plank: "A straight weathered cedar plank seen from above, wood grain running along its length, soft painted
  illustration, full frame texture"; 5:1; cutout no; people no; the four edges of the bed, cut to length by the layout.
- vine-leaf: "A single small fresh green ivy leaf seen from above, pointed tip to the right, soft painted illustration,
  plain white background"; 1:1; cutout yes; people no; placed every unit along each vine, rotated to the vine's
  direction (about 14 px on a 1366x768 bed).
- seed-sprout: "A single plump seed split open with a tiny pale green sprout and two seed leaves, soft painted
  illustration, plain white background"; 1:1; cutout yes; people no; marks each planted seed.
- ladybug: "A single red ladybug with black spots seen from directly above, head pointing right, soft painted
  illustration, plain white background"; 1:1; cutout yes; people no; the Euler walker, rotated to each step's
  direction; Motion off places her at the last stop.
- model-cocoa: "A big mug of hot cocoa with steam rising, on a snowy windowsill at night, soft painted illustration";
  4:3; cutout no; people no; M1's card and panel header.
- model-petri: "A glass petri dish on a lab bench with round cream colored bacteria colonies spreading across pale
  agar, soft painted illustration"; 4:3; cutout no; people no; M2's card and panel header.
- model-pond: "A small reedy fish pond at dusk with orange fish under the water's surface and lily pads, soft painted
  illustration"; 4:3; cutout no; people no; M3's card and panel header.
Blades, vines, isoclines, Euler segments, guesses, axes and preview.svg are drawn in code (they bend with the equation).

## Voice
`soft-breath` (Enceladus), style "Say quietly and gently, like a gardener talking in a greenhouse." Not used by a group
sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`. Readouts and the Name the vine work are read on
screen; Read speaks the hint.
- garden (how, Garden welcome; stale on the first seed planted): "Click the garden to plant a seed. The vine follows the blades."
- comb (how, first equation change; stale on the next equation change): "A new equation turns every blade. The vines regrow to match."
- guess (how, first time the Check a guess box gets focus; stale on Check): "Type a curve in the box and press Check. A solution lies along the blades everywhere."
- fits (event, a guess fits the field; stale on a new equation or guess): "That one fits the field."
- leaves (event, a guess leaves the blades; stale on a new equation or guess): "That one leaves the blades. Look at the ring, then try another curve."
- steps (how, Step by step welcome; stale on the first Step or Walk): "Pick a step size, then press Step. The ladybug follows the blade where she stands."
- smaller (how, first h of 0.1; stale on the next h change): "Smaller steps stay closer to the vine."
- models (how, Models welcome; stale on the first slider move): "Each model is a garden too. Drag the time slider to read the vine."

## Family engine
none. Uses `kit/graphing.js` `Plane` as a plotting tool (`g.fn` for guesses and closed-form vines, `g.point` for seeds,
`g.segment` for Euler steps, blades and RK4 vines drawn in the `plot` layer with `g.px`); the painted soil sits under
the plane's plot layer.

## Sources
- Slope fields, verifying solutions, Euler's method, separation of variables, exponential and logistic models:
  College Board, AP Calculus AB and BC CED (2020), Unit 7, https://apcentral.collegeboard.org/courses/ap-calculus-bc ;
  OpenStax, Calculus Volume 2, 4.2 "Direction Fields and Numerical Methods", 4.3 "Separable Equations" and 4.4 "The
  Logistic Equation", https://openstax.org/books/calculus-volume-2/pages/4-2-direction-fields-and-numerical-methods
- Newton's law of cooling (rate proportional to the gap from room temperature): OpenStax, Calculus Volume 2, 4.3 (same
  book).
- Runge-Kutta fourth order (for drawing vines only): OpenStax, Calculus Volume 2, 4.2 mentions higher-order methods;
  the method itself is standard (Burden and Faires, Numerical Analysis, 5.4).
- Equations and models are made up.
- Checks run (Python, 2026-10-29): RK4 at step 0.01 gives E4 3.4365637 at x = 1 (exact 3.4365637) and E2 8.1548455
  (exact 8.1548455). Euler E4: h = 1: 2; 0.5: 1.5, 2.5; 0.25: 1.625, 2.1562, 2.8828; 0.1: 3.1875, gap 0.2491. Euler E2:
  2.25, 2.4414, 2.5937. M1 T(10) = 51.453, 60 degrees at t = 6.995; M2 doubling 2.3105 h, P(5) = 448.17; M3 half full
  at 5.4931 years, P(5) = 225.43, P(10) = 429.24; Euler h = 1 68, 91.5008. E3 with x steps of 0.01 from (0, 2): the next
  step past x = 2.00 would cross y = 0, so the vine ends at (2.00, 0.022), within 0.03 of (2, 0). Check a guess on E4:
  2e^x - x - 1 and Ce^x - x - 1 for C = -3, 0.5 and 3 fit; e^x leaves at (-5, 0.0067), the first on-screen sample.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. E4 with a seed at (0, 1): the vine passes (1, 3.4366) within 0.001; `Name the vine` gives y = 2e^x - x - 1.
2. E2 seed (0, 3) reaches about 8.1548 at x = 1; E1 seed (2, 0) passes (3, 2.5).
3. E3 seed (0, 2) draws the upper half circle of radius 2 and stops within 0.03 of (±2, 0) with the undefined-slope line.
4. Step by step on E4 from (0, 1): h = 0.5 gives 1.5 then 2.5; h = 0.1 gives 3.1875 at x = 1, gap 0.2491.
5. Check a guess on E4: "2e^x - x - 1" fits; "e^x" leaves the blades and names a spot with a ring.
6. M1 reads T ≈ 51.5 at t = 10 and 60 near t = 7.0; M2 doubles at 2.31 h; M3 is 250 at 5.49 years with rate 50.
7. `Your own` "x - y" draws a field; "x -" says "I can't read that yet." and keeps the old field.
8. Focus: at 1366x768 and 1000x625 the bed is the largest thing on the stage in all three modes; leaves sit on the
   vines and the planks frame the bed at every size.
9. Tap while it plays: while a vine grows, a second tap plants a second seed at once; during a Walk, pressing `0.5`
   stops the walk and shows the new step size.
10. How-to lines spoken once each in five actions; "That one fits the field." once per equation; no line names a
    control that is not on screen.
11. Bed and panel visible at 1366x768; at 760 wide the panel sits under the bed; blades still readable in the 680x425
    preview; Motion off grows vines instantly; no network, no em dashes.

## Open questions
- slope-field-garden: Euler's method (7.5) and logistic models (7.9) are BC only. They are kept in, marked BC on screen. Agree?
