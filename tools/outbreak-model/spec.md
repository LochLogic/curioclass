# Outbreak Model

## One idea
Drag a target line to any number ("1 million people") and logarithms tell you exactly when the outbreak gets
there, worked three ways (base 2, base 10, base e) that always land on the same answer.

## Not like
- germ-spread-sim (grades 3-5, health): dots in one classroom and handwashing habits. This tool has no germs, people
  or habits; it is a function model on a graph, solved with logarithms.
- which-model-wins (grade 9): picks the best fit for real data sets. Here the model is given and the question is
  "when", answered by inverting it.
- savings-plan (grade 11, same batch): sequences and series of money, who wins and when, by adding up terms. This
  tool is a continuous growth function solved for time with logs; no money, no sums.
- compound-interest-garden (CTE 9-12): money growth over decades. No money here.
- half-life-dice (science 10): random dice show decay. This tool is deterministic; decay appears only as a
  "shrinking" setting.
- size-of-everything (grade 8): a log slider through sizes. This tool uses a log axis to show that equal factors
  take equal time, not to compare sizes.
- slope-field-garden (grade 12): differential equations. Logistic appears here only as a dashed "reality" curve.
- rollercoaster-polynomials (grade 11): shares the graphing engine only; polynomial zeros, nothing exponential.
- health-claim-checker (health 9-12): judges viral claims. The "rumor" here is just a story label for a count.

## Who and how
Grade 11, math (Algebra 2, Exponential and Logarithmic Functions). Driver: students, on their own laptops (a
teacher can project it). 15 to 30 minutes. Standards: F-LE.A.4 (solve a times b to the ct equals d with base 2,
10 or e, and evaluate the log with technology), F-IF.C.8b (read percent growth from an exponential), F-IF.C.9
(compare the same function as equation, graph and table).

Look: 9-12 dark instrument theme. Link `kit:curio`, then `kit:theme-912`, then the tool's own style. The tool sets
`--brand` to a warm amber-orange accent that passes WCAG AA on the theme panel. No confetti, no mascot, no score.

Header: title "Outbreak Model" with small line "When will it reach a million?", a `.seg` mode group with three
buttons **Grow**, **Ask when**, **Hit the ceiling**, then the kit buttons `motion`, `sound`, `read`.

## Screens and modes
Every mode shares one layout: the graph on the stage (left, about 640 x 560 of the 1000 x 620 scene), a readout
column on the right of the scene, and the kit panel with `hint` and `tip`.

Shared controls (in the scene, under the graph, all modes):
- **Story** select: Rumor at school, Virus X in a city, Viral post, Fading rumor, Steady spread (the five presets
  in Content). Picking one loads its numbers and its words (what is counted, the time unit).
- **Describe growth by** three-way `.seg`: **Doubling time**, **Tenfold time**, **Continuous rate**. Changes
  which slider shows and which equation is the "main" one. The curve never changes when you switch; only the
  description does.
- Slider **Start (a)**: logarithmic slider, 1 to 10,000, snapping to 1, 2, 3, 5 times powers of ten.
- Slider for the chosen description: **Doubling time D** 0.5 to 30 units (step 0.5), or **Tenfold time W** 1 to
  100 units (step 1), or **Continuous rate k** -0.50 to 1.50 per unit (step 0.01).
- Switch **Growing / Shrinking** (beside Doubling time and Tenfold time only; with Continuous rate the sign of k
  does this). Shrinking turns D into a halving time and W into a "tenth time".
- Buttons **Play**, **Pause**, **Reset clock**, and a **Scale: Linear / Log** toggle.
- The graph's trace dot (engine `g.trace`) reads out (t, N) as you move along the curve.

Readout column (all modes): the clock "Day 12.4" (or hour), a big rolling counter of N(t) in words, and the
**Same curve, three ways** card showing, live:
- N = a times 2 to the (t over D)
- N = a times 10 to the (t over W)
- N = a times e to the (k t)
- growth per unit: factor and percent (for example "times 1.260 each day, up 26.0 percent")
On screen these use real math formatting (superscripts); in voice and `aria-label` they are words.

**Grow** (the explore mode, opens first). Press Play: the clock runs from 0 to the right edge of the window, the
curve draws itself, the counter rolls. The **Milestones** list under the counter lights each row as the curve
passes it, with its time: 10, 100, 1 thousand, 10 thousand, 100 thousand, 1 million, 10 million, 100 million,
1 billion. Toggle **Compare steady growth** draws a dashed straight line that adds the first unit's gain every
unit forever, with its own milestone times in a second column, so the gap between "steady" and "exponential" is
visible. Toggle **Log** and the curve becomes a straight line; a note appears: "Every 10 times bigger takes the
same W units."

**Ask when** (the one idea). A horizontal **target line** appears across the graph, draggable (pointer and arrow
keys; PageUp/PageDown jump a power of ten), plus a **Target** number box and quick buttons **1 thousand**,
**1 million**, **1 billion**. Optional **Guess first** toggle: when on, the answer panel stays covered until the
student drags a guess pin along the time axis and presses **Show the answer**; then the guess and answer show
together, with no score. The **Solve it** panel shows the steps for all three bases side by side, each ending at
the same t:
1. a times 2 to the (t over D) equals d
2. 2 to the (t over D) equals d over a
3. t over D equals log base 2 of (d over a)
4. t equals D times log(d over a) over log 2, then the calculator value
(base 10: t equals W times log base 10 of (d over a); base e: t equals ln(d over a) over k.)
A vertical line drops from the crossing to the time axis with the label "t = 49.8 days". **Check it** plays the
clock to that exact t and stops; the counter shows N reaching the target. Under the steps, a whole-unit table shows
the unit before and the unit after (for example "Day 49: 794,000. Day 50: 1,000,000 passed").

**Hit the ceiling** (where the model breaks). A **Place** select sets a ceiling K: Denver, Colorado, United States,
World. A solid horizontal line marks K. The pure exponential is drawn as before and keeps climbing past K, shaded
red-orange above it with the label "more people than exist". A dashed logistic curve with the same start a and the
same k bends and levels off at K. The readout shows "Exponential says everyone by day 74.9" and "Logistic: half of
everyone by day 74.9, and it never quite reaches all". Toggle **Show the logistic equation** shows N = K over
(1 plus ((K minus a) over a) times e to the minus k t). The hint text explains in two sentences why: people who
already heard cannot hear it again, so spread slows.

## Content
Model (single source of truth): N(t) = a times e to the (k t). Conversions: D = ln 2 over k, W = ln 10 over k,
growth factor per unit = e to the k, percent = (e to the k minus 1) times 100. Shrinking means k is negative.

Presets (fictional, round numbers; every Story card says "A made-up example to explore the math, not a real
forecast"):

| Story | Counts | Unit | a | Given as | Default target |
|---|---|---|---|---|---|
| Rumor at school | students who heard it | hours | 3 | doubles every 2 hours | 1,000 |
| Virus X in a city | cases | days | 10 | doubles every 3 days | 1,000,000 |
| Viral post | shares | hours | 50 | 10 times every 12 hours | 1,000,000 |
| Fading rumor | people still repeating it | days | 2,000 | halves every 5 days | 10 |
| Steady spread | cases | days | 1 | continuous rate 0.25 per day | 1,000,000 |

Worked answers (checked; the verify agent tests these):
- Rumor at school to 1,000: t = 2 times log2(333.33) = 16.76 hours.
- Virus X to 1 million: t = 3 times log2(100,000) = 49.83 days. Day 49 has about 825,700; day 50 about 1,040,300.
- Viral post to 1 million: t = 12 times log10(20,000) = 51.61 hours.
- Fading rumor down to 10: t = 5 times log2(200) = 38.22 days.
- Steady spread to 1 million: t = ln(1,000,000) over 0.25 = 55.26 days.
- Virus X conversions: D = 3, k = 0.2310 per day, W = 9.97 days, times 1.260 per day, up 26.0 percent.
- Virus X, 1 thousand to 1 million takes 29.90 days, and so does 1 million to 1 billion.
- 1 doubling a day from 1 reaches 1 million on day 19.93 (2 to the 20 is 1,048,576).

Ceilings (Hit the ceiling), with Virus X defaults (a = 10, D = 3) and when the pure exponential reaches each:

| Place | K | Exponential reaches K |
|---|---|---|
| Denver | 715,522 | day 48.38 |
| Colorado | 5,773,714 | day 57.42 |
| United States | 331,449,281 | day 74.95 |
| World | 8,000,000,000 | day 88.73 |

Number words: up to 999,999 with commas; then "1.04 million", "3.31 billion", "8.00 trillion"; above 10 to the 15
write "2.1 times 10 to the 18". Below 1 (shrinking) show two decimals, then "less than 0.01".

Hint texts (panel `hint`, one per mode):
- Grow: "<b>Grow.</b> Pick a story and press Play. Watch the milestones: each new power of ten arrives on a
  steady beat. Turn on Log to see why."
- Ask when: "<b>Ask when.</b> Drag the target line to any number. Logarithms undo the exponent and give the exact
  time, three ways that agree."
- Hit the ceiling: "<b>Hit the ceiling.</b> No outbreak can pass the number of people there are. Compare the pure
  exponential with a curve that slows as it runs out of people."

Tip texts (panel `tip`, rotate on each mode open): "Switching between doubling time, tenfold time and continuous
rate never moves the curve." / "On a log scale an exponential is a straight line. Its slope is log of the growth
factor." / "Halving time works the same way as doubling time, just downhill." / "A forecast is only as good as its
assumptions. The ceiling mode shows one that breaks."

## Interactions in detail
- Changing any slider or the Story recomputes everything at once: curve, card, milestones, target answer. The
  clock keeps its t unless Reset clock is pressed. Changing Story resets the clock and sets the default target.
- Switching the description keeps k fixed and recomputes D and W from it (rounded only for display, at 2
  decimals). Slider positions that fall outside a slider's range clamp, and the card says "outside slider range"
  but keeps the exact value.
- k = 0 (or D, W at its limit): "No growth: N stays at a." Ask when answers "Never" unless target equals a.
- Target equals a: t = 0. Growing and target below a: "Already past: it started at a, above the target." Shrinking
  and target above a: "Never: a shrinking count does not climb back." Shrinking and target at or below 0: number
  box refuses it ("Pick a number above 0; the model gets close to 0 but never reaches it").
- Target box accepts plain digits, commas, and "1e6" style; anything else shows a small inline message and keeps
  the old target.
- Answer t longer than 365 days also shows years ("about 2.4 years"). If t is beyond the graph window, the window
  widens with `g.view` (animated unless Motion is off) to fit t times 1.2.
- Linear scale: y window from 0 to the larger of target times 1.2 and N at the window's end, capped at 10 to the
  12; above the cap the curve leaves the top with an arrow "off the chart". Log scale: y axis is log10 of N drawn
  as a plain number axis, with the tool's own tick labels 1, 10, 100, 1 thousand ... placed with `g.label`.
- Play runs about 8 seconds across the window (Motion off: the curve and counter jump to the end in one step, the
  milestones list fills at once). Pause holds. Reset clock returns to t = 0 and clears milestone lights.
- Keyboard: every control in tab order; arrow keys move sliders and the target line; Enter on Play, Check it.
- Mode change: `Curio.stop()`, keep the Story and sliders, reset the clock.
- Sound: a soft tick as each milestone lights, one low tone when the exponential crosses K. Silent when Sound off.
- Read button reads the hint and the current answer sentence.

## Art
none: drawn in code (graph, lines, shading, counter, cards).

## Voice
Bank `hs-narrator`, voice "Kore", style "Read clearly and naturally, at a moderate pace". 9 lines.
1. Welcome to Outbreak Model. Pick a story, press Play, and watch the count grow.
2. Notice the milestones. Each time the count gets ten times bigger, it takes the same amount of time.
3. Try the log scale. An exponential curve turns into a straight line.
4. Ask when. Drag the target line to any number, and logarithms will tell you exactly when the count gets there.
5. Want to test your instinct first? Turn on Guess first, drop a pin on the time axis, then show the answer.
6. Three bases, one answer. Base two, base ten and base e all give the same time, because they describe the same curve.
7. Press Check it to run the clock to that exact moment.
8. Hit the ceiling. A real outbreak runs out of people, so the pure exponential stops telling the truth.
9. This is a made-up example to explore the math. It is not a forecast of any real illness.

Lines 1, 4 and 8 play on first opening each mode (after the first tap); the others play from the Read button or the
first time their control is used.

## Family engine
Graphing (`kit/graphing.js`, written by rollercoaster-polynomials to `docs/families/graphing.md`): `Plane`,
`g.fn` for the exponential, the steady line and the logistic (dashed patterns from the engine), `g.point` with
`draggable` for the guess pin, `g.segment` for the target line, ceiling line and drop line, `g.intersect` for the
target crossing (the Solve panel uses the closed form; `g.intersect` is a cross-check only), `g.trace`, `g.view`,
`g.label` for log-scale ticks, `g.slider` for the three sliders. Log scale is done by plotting log10 of N, not by
an engine feature. Tool-only code: the model and conversions, number words, milestones, the Solve panel, keep in
one marked block.

## Sources
- Exponential and logarithmic models, change of base, logistic model: OpenStax, Algebra and Trigonometry 2e,
  sections 6.5 to 6.7 (CC BY 4.0), https://openstax.org/details/books/algebra-and-trigonometry-2e
- F-LE.A.4 and F-IF.C wording: Common Core State Standards for Mathematics, High School Functions,
  https://www.thecorestandards.org/Math/Content/HSF/
- Denver 715,522 and Colorado 5,773,714 (April 1, 2020): US Census Bureau, 2020 Census, QuickFacts,
  https://www.census.gov/quickfacts/
- United States 331,449,281 (April 1, 2020): US Census Bureau, 2020 Census apportionment results,
  https://www.census.gov/data/tables/2020/dec/2020-apportionment-data.html
- World 8 billion on November 15, 2022: United Nations, Day of Eight Billion,
  https://www.un.org/en/dayof8billion
- All presets are invented round numbers, labeled as such in the tool. All worked answers computed from the
  formulas above (checked in Python).

## Done when
1. Virus X, Ask when, target 1 million shows t = 49.83 days in all three Solve columns, and Check it stops the
   counter at 1,000,000 (within rounding).
2. Switching Doubling time, Tenfold time, Continuous rate on Virus X never moves the curve and shows D 3, W 9.97,
   k 0.2310, "up 26.0 percent".
3. Fading rumor to 10 gives 38.22 days; dragging the target above 2,000 says "Never".
4. Log scale turns the exponential into a straight line; Virus X milestones 1 thousand to 1 million and 1 million
   to 1 billion are each 29.90 days apart.
5. Hit the ceiling with United States shows the exponential passing K at day 74.95, the region above K shaded and
   labeled, and the logistic leveling under K.
6. Guess first hides the answer until a pin is placed and Show the answer is pressed; nothing is scored.
7. k = 0, target equal to a, target below a, and a typed "abc" each give the stated message without errors.
8. Motion off: Play jumps to the end at once and zoom changes are instant; everything still works by keyboard.
9. No images, no network requests, no em dashes, and every Story card says it is a made-up example.
