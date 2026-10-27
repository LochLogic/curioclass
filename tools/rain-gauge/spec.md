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

Stage: left, a house roof with a gutter and downspout feeding a rain barrel (drawn in code), rain streaks whose
density follows the current rate, a clock "14:30", and the barrel's level with a liter scale; right, two stacked
engine planes sharing the time axis (0 to 24 h): top "rain rate (mm per hour)" r(t), bottom "rain so far (mm)"
A(t) = integral of r from 0 to t, both with a moving time line.

Panel: storm picker (cards S1 to S5 with a mini graph), roof area slider (10 to 100 m², default 50), barrel size
(100, 200 or 400 L, default 200), `Garden tap` toggle (drains 20 L/h while open), and the readouts: "rain so far ... mm",
"water caught ... L" (mm x m² = L), "in the barrel ... L", "overflowed ... L".

### Storm (explore, default)
`Play` runs the day (1 real second = 1 hour; `x4` toggle), `Pause`, time scrubber, `Restart`. The top graph shades the
area under r up to now (the area is the rain so far); the bottom graph draws A(t) as it goes, with a tangent at the
time line labeled "slope = r(t) = ... mm/h" (FTC). The barrel fills; when full, water spills over the rim (an
overflow counter keeps adding). With the tap open, the barrel's net rate is (roof x r(t) - 20) L/h, shown as its own
line.

### Slices
- Slice count n: buttons `4`, `8`, `24`, `96` and a slider 1 to 96. Method buttons `Left`, `Right`, `Midpoint`,
  `Trapezoid`.
- The top graph shows the n rectangles (or trapezoids); `Pour slices` drops them one by one into a measuring cylinder
  beside the barrel (one block per slice, its height in mm; 120 ms each, instant with Motion off).
- Table: method, n, sum (mm, 3 decimals), exact (mm), error. Line under it: "Thinner slices, closer sum."
- `Exact` card: the antiderivative F(t), "F(24) - F(0) = ...", for storms with a formula antiderivative.

### Forecast (optional)
Cards F1 to F4, each a question with a box: when does the barrel overflow, how much is caught by a time, how full is
it at the end with the tap open. Answers checked (Content). `Show me` after two misses opens the integral work.

## Content
Storms (made up; t in hours from midnight, r in mm per hour):
| Storm | r(t) | Total over 24 h (mm) | Antiderivative |
|---|---|---|---|
| S1 Steady drizzle | 2 | 48 | 2t |
| S2 Long soaker | 3 sin(πt/24) | 144/π ≈ 45.837 | -(72/π) cos(πt/24) |
| S3 Afternoon build | 0.01t(24 - t) | 23.04 | 0.01(12t² - t³/3) |
| S4 Cloudburst | 0 before 14:00, up to 30 at 15:00, down to 0 at 17:00 (straight lines) | 45 | piecewise (area of a triangle) |
| S5 Two showers | 4 from 6:00 to 9:00, 8 from 18:00 to 20:00, else 0 | 28 | piecewise |
Rain so far for S3: 11.52 mm by noon, 23.04 mm by midnight.

Riemann sums (mm), left / right / midpoint / trapezoid:
- S2: n = 4: 43.456 / 43.456 / 47.036 / 43.456; n = 8: 45.246 / 45.246 / 46.132 / 45.246; n = 24: 45.771 / 45.771 /
  45.869 / 45.771; n = 96: 45.833 / 45.833 / 45.839 / 45.833.
- S3: n = 4: 21.6 / 21.6 / 23.76 / 21.6; n = 8: 22.68 / 22.68 / 23.22 / 22.68; n = 24: 23.0 / 23.0 / 23.06 / 23.0; n = 96:
  23.038 / 23.038 / 23.041 / 23.038.
- S4: n = 4: 0 / 0 / 180 / 0 (the coarse slices miss the burst or catch only its peak); n = 8: 90 / 90 / 22.5 / 90;
  n = 24 and 96: 45 exactly for every method (slice edges land on the corners).
- S1: every method gives 48 for every n. S5: left and right are exact when the slice edges land on the hours 6, 9,
  18 and 20 (n = 8, 24, 96).
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
- Tangent on A(t): slope from r(t) exactly; at S4's corners (14, 15, 17) the label says "corner: the rate jumps
  direction here" and draws no tangent at exactly those times.
- Changing storm, roof or barrel resets the day. The tap only affects the barrel, never the mm readouts.
- Sound: soft rain noise (Web Audio filtered noise) whose loudness follows r(t), one drip per poured slice; off with
  Sound.
- Keyboard: scrubber range input (arrows 0.1 h, PageUp/PageDown 1 h); method and n buttons in tab order before the
  table.
- Mode change: `Curio.stop()`, `V.hush()`. Forecast check marks per device (localStorage `curio-rain-gauge`, try/catch),
  `Clear marks`.

## Look
Accent (`--brand`) #7e98ff, cornflower rain blue: 6.4:1 on --panel #141b25, 6.1:1 on --sec-bg #18202b; --brand-ink
#10161f on it 6.8:1. Bluer and darker than flight-planner's sky #3aa8ff; no 9-12 math neighbor uses it.
Scene: overcast night slate #151b24, roof shingles #3a3f47, gutter metal #8a96a3, barrel wood #6e4f33 with iron hoops
#4a525c, water #4f7fd9 at 80 percent, rain streaks #9fb4d9. Liter scale labels #e8edf3 on the barrel side (over 9:1).
Rate curve `--gr-1`, accumulation `--gr-3`, slices filled with the accent at 35 percent with a full-strength edge.

## Art
none: drawn in code (house, gutter, barrel, cylinder, rain, planes, preview.svg).

## Voice
`calm-professor` (Schedar), style "Say evenly and clearly, like a calm TV weather forecaster." Not used by a group
sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`.
- storm (how, Storm welcome): "Press Play. The shaded area under the rate graph is the rain so far, and it pours into the barrel."
- ftc (how, first pause after noon): "The slope of the rain-so-far graph at any time is the rate at that time."
- overflow (event, the barrel first overflows in a run; stale on Restart): "The barrel is full. The rest spills over."
- slices (how, Slices welcome): "Choose a number of slices and a method, then press Pour slices."
- thin (how, first n of 24 or more): "Thinner slices land closer to the exact amount."
- forecast (how, Forecast welcome): "Each card asks about the barrel. Set up the integral, then type your answer."
- right (event, a correct forecast; stale on a new card): "Right on the forecast."

## Family engine
none. Uses `kit/graphing.js` `Plane` as a plotting tool for the two planes (`g.fn`, `g.trace` for the time line,
`g.segment` for the tangent, slices and shading drawn in the `plot` layer with `g.px`); the house and barrel are the
tool's own SVG.

## Sources
- Riemann sums (left, right, midpoint, trapezoid), accumulation functions, the Fundamental Theorem of Calculus: College
  Board, AP Calculus AB and BC CED (2020), Unit 6, https://apcentral.collegeboard.org/courses/ap-calculus-ab ; OpenStax,
  Calculus Volume 1, 5.1 "Approximating Areas" and 5.3 "The Fundamental Theorem of Calculus",
  https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus
- 1 mm of rain on 1 m² = 1 liter (1 mm x 1 m² = 0.001 m³ = 1 L): NIST SP 811 (liter = 0.001 m³),
  https://www.nist.gov/pml/special-publication-811
- Storms, roof, barrels and the tap are made up; every sum, total and time computed in Python (2026-10-27).

## Done when
1. Storm S3 played to 12:00 shows 11.52 mm and, with a 50 m² roof, 576 L caught; at 24:00 23.04 mm and the 200 L barrel
   full with 952 L overflowed.
2. The tangent label on A(t) equals r(t) at three spot times (S3 at t = 6: r = 1.08).
3. Slices S3 left n = 8 gives 22.68; midpoint n = 8 gives 23.22; exact 23.04.
4. Slices S4 midpoint n = 4 gives 180 and n = 24 gives 45.
5. S1 gives 48 for every method and n.
6. Forecast F1 accepts 2.5 (and 2:30); F2 accepts 7.22 h (7:13); F3 accepts 5.14 h; F4 accepts 259 L (and refuses 520).
7. Tap open on S1 with a 10 m² roof: net (20 - 20) = 0 L/h, the level stays flat (a check of the net rate).
8. How-to lines spoken once each in five actions; "The barrel is full." once per run.
9. Scene and graphs visible with controls at 1366x768; at 760 wide the scene sits above the graphs; graph labels at
   least 10 px in the 680x425 preview; no network, no images, no em dashes.

## Open questions
none
