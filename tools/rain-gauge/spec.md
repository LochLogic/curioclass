# Rain Gauge

## One idea
A storm's rainfall rate over one day pours off a roof into a rain barrel: slice the day into rectangles and each
rectangle drops its own block of water into the barrel, so you watch a Riemann sum fill up next to the true amount,
and the barrel's level graph rises with a slope that is exactly the rate at that moment.

## Not like
- speedometer (this group): from an amount (position) to its rate. Here the other direction: from a rate to an amount.
- solid-spinner (this group): integrals as volumes of solids built from slices. Here the integral is water collected over time, and the slices are slices of time.
- savings-plan (gr 11, built): sums of sequences of deposits. Here the rate changes continuously and the sum becomes an integral as the slices thin.
- outbreak-model (gr 11, built simulator): growth over time from a formula; no accumulation from a rate.
- slope-field-garden (this group): a rate that depends on the amount itself; here the rate depends only on the time of day.

## Who and how
Grade 12, AP Calculus (The Integral). Students drive, 25 to 40 minutes. Explore first: Storm opens with a storm ready
to play.
Topic line: "Riemann sums and accumulation".
Standards: AP-CALC.U6 (6.1 to 6.2 accumulation and Riemann sums, 6.3 to 6.4 the definite integral and the accumulation
function, 6.5 to 6.7 the Fundamental Theorem, antiderivatives and evaluating definite integrals).
tool.json: driver "students", minutes "25-40", modes ["Storm", "Slices", "Forecast"].

## Screens and modes
Header (kit, 9-12 theme): "Rain Gauge", small line "Rate in, water out." Modes `Storm`, `Slices`, `Forecast`; kit
`Motion`, `Sound`, `Read`.

Stage: left (about 40 percent of the width), the painted scene: the cottage in the storm (art: storm-cottage) with the
rain barrel (art: rain-barrel) on the stone pad under the downspout; rain streaks in code whose density follows the
current rate, a clock "14:30" in code, and the barrel's water level drawn in code inside its glass window with a liter
scale beside it. Right (about 60 percent), two stacked engine planes sharing the time axis (0 to 24 h): top "rain rate
(mm per hour)" r(t), bottom "rain so far (mm)" A(t) = integral of r from 0 to t, both with a moving time line.

Panel: storm picker (cards S1 to S5 with a mini graph), roof area slider (10 to 100 m², default 50), barrel size
(100, 200 or 400 L, default 200), `Garden tap` toggle (drains 20 L/h while open), and the readouts: "rain so far ... mm",
"water caught ... L" (mm x m² = L), "in the barrel ... L", "overflowed ... L".

### Storm (explore, default)
Focus: the top plane's shaded area growing under r(t), the largest thing on the stage (the top plane takes about 60
percent of the graph column's height), with the barrel filling beside it.
`Play` runs the day (1 real second = 1 hour, so 24 s; `x4` toggle makes it 6 s), `Pause`, time scrubber, `Restart`.
The top graph shades the area under r up to now (the area is the rain so far); the bottom graph draws A(t) as it goes,
with a tangent at the time line labeled "slope = r(t) = ... mm/h" (FTC). The barrel fills; when full, water spills over
the rim (code drips; an overflow counter keeps adding). With the tap open, a code stream runs from the barrel's brass
tap and the barrel's net rate is (roof x r(t) - 20) L/h, shown as its own line.

### Slices
Focus: the top plane with its n rectangles (or trapezoids), which grows to about 70 percent of the graph column's
height; the measuring cylinder (art: measuring-cylinder) stands at the plane's right end and replaces the cottage
scene, which shrinks to a small thumbnail with the barrel's total.
- Slice count n: buttons `4`, `8`, `24`, `96` and a slider 1 to 96. Method buttons `Left`, `Right`, `Midpoint`,
  `Trapezoid`.
- `Pour slices` drops the slices one by one into the cylinder (one code block per slice, its height in mm; 120 ms
  each, instant with Motion off).
- Table: method, n, sum (mm, 3 decimals), exact (mm), error. Line under it: "Thinner slices, closer sum."
- `Exact` card: the antiderivative F(t), "F(24) - F(0) = ...", for storms with a formula antiderivative.

### Forecast (optional)
Focus: the chosen card (question, answer box, `Check`) centered over the top of the graph column, with that card's
storm graphed under it; the scene shows the card's roof and barrel.
Cards F1 to F4, each a question with a box and a `Check` button: when does the barrel overflow, how much is caught by a
time, how full is it at the end with the tap open. Answers checked (Content). `Show me` appears after two misses and
opens the integral work.

## Content
Storms (made up; t in hours from midnight, r in mm per hour):
| Storm | r(t) | Total over 24 h (mm) | Antiderivative |
|---|---|---|---|
| S1 Steady drizzle | 2 | 48 | 2t |
| S2 Long soaker | 3 sin(πt/24) | 144/π ≈ 45.837 | -(72/π) cos(πt/24) |
| S3 Afternoon build | 0.01t(24 - t) | 23.04 | 0.01(12t² - t³/3) |
| S4 Cloudburst | 0 before 14:00, up to 30 at 15:00, down to 0 at 17:00 (straight lines) | 45 | piecewise (area of a triangle) |
| S5 Two showers | 4 from 6:00 to 9:00, 8 from 18:00 to 20:00, else 0 | 28 | piecewise |
Rain so far for S3: 11.52 mm by noon, 23.04 mm by midnight. S5's showers switch on at the start hour and off at the end
hour (the rate at exactly 6:00 is 4, at exactly 9:00 it is 0).

Riemann sums (mm), left / right / midpoint / trapezoid:
- S2: n = 4: 43.456 / 43.456 / 47.036 / 43.456; n = 8: 45.246 / 45.246 / 46.132 / 45.246; n = 24: 45.771 / 45.771 /
  45.869 / 45.771; n = 96: 45.833 / 45.833 / 45.839 / 45.833.
- S3: n = 4: 21.6 / 21.6 / 23.76 / 21.6; n = 8: 22.68 / 22.68 / 23.22 / 22.68; n = 24: 23.0 / 23.0 / 23.06 / 23.0; n = 96:
  23.038 / 23.038 / 23.041 / 23.038.
- S4: n = 4: 0 / 0 / 180 / 0 (the coarse slices miss the burst or catch only its peak); n = 8: 90 / 90 / 22.5 / 90;
  n = 24 and 96: 45 exactly for every method (slice edges land on the corners).
- S1: every method gives 48 for every n.
- S5: n = 4: 72 / 72 / 0 / 72; n = 8: 36 for every method (the 20:00 edge falls inside a 3-hour slice); n = 24 and 96:
  28 exactly for every method (slice edges land on 6, 9, 18 and 20).
(Left equals right for S2, S3 and S4 because r is 0 at both ends of the day.)
Water: 1 mm of rain on 1 m² is 1 liter. 50 m² roof: S3 gives 1,152 L in a day (overflows a 200 L barrel).

Forecast cards (roof and barrel as stated on the card):
- F1: roof 40 m², 200 L barrel, empty at midnight, storm S1. Overflow when 5 mm has fallen: at 2.5 h (2:30).
- F2: same barrel and roof, storm S3. Solve 0.01(12T² - T³/3) = 5: T ≈ 7.22 h (about 7:13).
- F3: same, storm S2. Solve (72/π)(1 - cos(πT/24)) = 5: T ≈ 5.14 h (about 5:09).
- F4: roof 20 m², 400 L barrel starting with 100 L, tap open all day (20 L/h out), storm S4. How much is in the barrel
  at midnight? The plain integral (100 + 900 - 480 = 520 L) is wrong because the barrel clamps: it runs empty at 5:00
  (100 L / 20 L/h) and stays empty until the burst; from 14:00 it fills at 20r(t) - 20 L/h, is full at about 15:13
  (15.22 h) and spills; it stays full until the rain rate drops under 1 mm/h at 16:56 (t = 17 - 1/15), loses 0.67 L by
  17:00, then drains 20 L/h for 7 hours: 399.33 - 140 = 259.3 L. Answer 259 L. The card's work shows each stretch.
Checks: times within 0.05 h (3 min, typed as hours or as hh:mm), amounts within 1 L or 0.1 mm.

## Interactions in detail
- Accumulation is computed by exact antiderivatives where listed (S1 to S3) and exactly by geometry for the
  piecewise storms; the barrel level is integrated step by step (0.01 h) because it clamps at 0 and at the barrel
  size; the panel says "clamped" when that happened.
- Riemann sums are computed from r directly: left uses t_i = 24i/n, right t_(i+1), midpoint their average, trapezoid
  the average of left and right. Printed to 3 decimals, trailing zeros dropped.
- n slider: any whole number 1 to 96; `Pour slices` for n over 24 animates in batches so it takes at most 3 s.
- Taps while it plays: during Play, the scrubber, `Pause`, `x4` and `Garden tap` act at once (the tap stream starts or
  stops on that frame); changing storm, roof or barrel resets the day to 0:00 and pauses. During a pour, changing n or
  the method stops the pour and shows the new slices and table at once; `Pour slices` starts again from empty.
- Tangent on A(t): slope from r(t) exactly; at S4's corners (14, 15, 17) the label says "corner: the rate jumps
  direction here" and draws no tangent at exactly those times.
- The tap only affects the barrel, never the mm readouts.
- Sound (on as the kit sets it): soft rain noise (Web Audio filtered noise) whose loudness follows r(t), one drip per
  poured slice; off with Sound.
- Keyboard: scrubber range input (arrows 0.1 h, PageUp/PageDown 1 h); method and n buttons in tab order before the
  table; Enter in a Forecast box presses `Check`.
- Mode change: `Curio.stop()`, `V.hush()`. Forecast check marks per device (localStorage `curio-rain-gauge`, try/catch),
  `Clear marks`.

## Look
Accent (`--brand`) #7e98ff, cornflower rain blue: 6.45:1 on --panel #141b25, 6.11:1 on --sec-bg #18202b; --brand-ink
#10161f on it 6.76:1. Bluer and darker than flight-planner's sky #3aa8ff; no 9-12 math neighbor uses it.
Scene: the painted storm at dusk sets the palette (slate cloud greys, dark shingles, wet green grass, warm barrel wood);
code over it: water #4f7fd9 at 80 percent inside the barrel window, rain streaks #9fb4d9, the clock and liter scale
#e8edf3 on a #10161f chip at 85 percent (15.4:1). Rate curve `--gr-1`, accumulation `--gr-3`, slices filled with the
accent at 35 percent with a full-strength edge.

## Art
Local FLUX (`scripts/localart.py`); no people. One style: soft painted illustration, stormy dusk light.
- storm-cottage: "A small wooden cottage seen from the side under heavy grey storm clouds at dusk, a sloped dark
  shingle roof with a metal gutter along its lower edge and a downspout running down the right corner to a flat stone
  pad, wet grass and a stone path, soft painted illustration"; 4:3; cutout no; people no; the left stage background in
  Storm and Forecast, the small thumbnail in Slices; rain streaks, splashes and the clock drawn over it in code.
- rain-barrel: "A wooden rain barrel with dark iron hoops, an open top, a tall clear glass window strip down its front
  and a brass tap near the bottom, soft painted illustration, plain white background"; 3:4; cutout yes; people no;
  stands on the stone pad at the downspout's foot (the build places it once from measured points); the water level is
  drawn in code inside the window strip, the liter scale beside it, overflow drips over the rim and the tap stream.
- measuring-cylinder: "A tall clear glass laboratory measuring cylinder with a round glass foot and a pouring lip,
  smooth blank glass, soft painted illustration, plain white background"; 9:16; cutout yes; people no; Slices: poured
  slice blocks stack inside it in code, with the mm scale in code beside it.
Rain streaks, water, the two planes, slices, tangents, storm-card mini graphs and preview.svg are drawn in code (they
change every frame or are graphs).

## Voice
`calm-professor` (Schedar), style "Say evenly and clearly, like a calm TV weather forecaster." Not used by a group
sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`. Cards and readouts are read on screen; Read
speaks the hint.
- storm (how, Storm welcome; stale on the first Play): "Press Play. The shaded area under the rate graph is the rain so far, and it pours into the barrel."
- ftc (how, first Pause or scrub past noon; stale when Play resumes or the storm changes): "The slope of the rain so far graph at any time is the rate at that time."
- overflow (event, the barrel first overflows in a run; stale on Restart or a reset): "The barrel is full. The rest spills over."
- slices (how, Slices welcome; stale on the first Pour slices): "Pick a number of slices and a method, then press Pour slices."
- thin (how, first n of 24 or more; stale when n drops under 24 or the mode changes): "Thinner slices land closer to the exact amount."
- forecast (how, Forecast welcome; stale on the first Check): "Pick a card. Set up the integral, type your answer in the box, then press Check."
- miss (event, a wrong Check; stale on the next Check or a new card): "Not yet. Look at the graph under the card, then press Check again."
- right (event, a correct forecast; stale on a new card): "Right on the forecast."

## Family engine
none. Uses `kit/graphing.js` `Plane` as a plotting tool for the two planes (`g.fn`, `g.trace` for the time line,
`g.segment` for the tangent, slices and shading drawn in the `plot` layer with `g.px`); the scene layers (painted
images plus code rain and water) are the tool's own.

## Sources
- Riemann sums (left, right, midpoint, trapezoid), accumulation functions, the Fundamental Theorem of Calculus: College
  Board, AP Calculus AB and BC CED (2020), Unit 6, https://apcentral.collegeboard.org/courses/ap-calculus-ab ; OpenStax,
  Calculus Volume 1, 5.1 "Approximating Areas" and 5.3 "The Fundamental Theorem of Calculus",
  https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus
- 1 mm of rain on 1 m² = 1 liter (1 mm x 1 m² = 0.001 m³ = 1 L): NIST SP 811 (liter = 0.001 m³),
  https://www.nist.gov/pml/special-publication-811
- Storms, roof, barrels and the tap are made up.
- Checks run (Python, scipy, 2026-10-29): totals by numeric integration 48, 45.8366, 23.04, 45, 28; every Riemann sum in
  Content recomputed. The first draft said S5's left and right sums are exact at n = 8; at n = 8 the 20:00 edge falls
  inside a slice and every method gives 36, so Content now says so and adds S5's n = 4 row (72 / 72 / 0 / 72) and its
  switch-on convention. S3 by noon 11.52 mm, 576 L on 50 m²; day 1,152 L, 952 L overflowed from 200 L; r(6) = 1.08.
  F2 T = 7.2193 h, F3 T = 5.1428 h (both inside the 0.05 h tolerance of the stated answers and of 7:13 and 5:09). F4
  stepped at 0.0001 h: empty at 5.00 h, full at 15.219 h, leaves full at 16.933 h, 259.33 L at midnight. Tap on S1 with
  a 10 m² roof: net 0 L/h. Storm run 24 s (6 s at x4); a 24-slice pour 2.9 s. Contrast ratios by the WCAG 2.1 formula.

## Done when
1. Storm S3 played to 12:00 shows 11.52 mm and, with a 50 m² roof, 576 L caught; at 24:00 23.04 mm and the 200 L barrel
   full with 952 L overflowed.
2. The tangent label on A(t) equals r(t) at three spot times (S3 at t = 6: r = 1.08).
3. Slices S3 left n = 8 gives 22.68; midpoint n = 8 gives 23.22; exact 23.04. S5 at n = 8 gives 36 for every method.
4. Slices S4 midpoint n = 4 gives 180 and n = 24 gives 45.
5. S1 gives 48 for every method and n.
6. Forecast F1 accepts 2.5 (and 2:30); F2 accepts 7.22 h (7:13); F3 accepts 5.14 h; F4 accepts 259 L (and refuses 520).
7. Tap open on S1 with a 10 m² roof: net (20 - 20) = 0 L/h, the level stays flat (a check of the net rate).
8. Focus: at 1366x768 and 1000x625 the shaded rate graph (Storm), the sliced rate graph with its cylinder (Slices) and
   the card with its box (Forecast) are each the largest thing on the stage.
9. Tap while it plays: during Play, dragging the scrubber or toggling the tap changes the barrel and graphs on that
   frame; during a 96-slice pour, pressing `8` shows 8 slices and the new table at once.
10. How-to lines spoken once each in five actions; "The barrel is full." once per run; no line names a control that is
    not on screen.
11. Scene and graphs visible with controls at 1366x768; at 760 wide the scene sits above the graphs; graph labels at
    least 10 px in the 680x425 preview; the barrel stands on the stone pad at every size; no network, no em dashes.

## Open questions
none
