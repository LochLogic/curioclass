# Graph Story Lab

## One idea
A graph is a story you can scrub: drag the cursor along the x axis and a small scene plays that moment (the sun
crossing the sky, the tea steaming, the phone battery bar), and you mark the story's features on the graph with
brackets, flags and secant lines, which the tool reads back to you in function notation ("f(172) = 15.02: the
longest day") and checks.

## Not like
- motion-graph-match (gr 11, graphing): you make the graph by moving. Here the graph is given and you read and mark it.
- rollercoaster-polynomials (gr 11, graphing): designs a polynomial by its zeros. Here no designing; features of given functions, and only one story is a polynomial (a hike, not a coaster).
- launch-pad (gr 9, same group): one quadratic flight, solved for times. Here many function types, read for features, domain and rate.
- which-model-wins (gr 9, same group): chooses a model for data. Here the function is fixed and the work is interpretation.
- intersection-quest (gr 9, same group): two equations at once. Here one function at a time.

## Who and how
- Grade 9, Algebra 1, Functions and Their Graphs. Students drive. 15 to 35 minutes.
- Topic line: "reading key features of a function's graph in context".
- Standards (module): F-IF.A (A.1 a function gives each input one output, A.2 function notation, A.3 sequences as functions on whole numbers), F-IF.B (B.4 key features in context, B.5 domain in context, B.6 average rate of change over an interval).
- CCSS clusters: Read mode serves F-IF.A.2 and F-IF.B.4; Mark mode F-IF.B.4 to B.6; the Cups and Oval track stories F-IF.A.3 and A.1.
- tool.json: driver "students", minutes "15-35", modes ["Read", "Mark"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "Scrub the graph. Watch the story." Modes `Read` (opens first), `Mark`. Story picker (eight
stories, Content). Kit buttons.
Layout: the graph across the top two thirds of the stage, the scene strip under it (a wide short panel drawn in
code), the panel on the right with readouts and the marking tools. Under 900 px tall the scene strip shrinks to
120 px and stays visible; at 760 wide the panel goes under.

### Read
A vertical cursor on the graph (drag, or arrow keys, Shift for bigger steps; snap to the story's step). The
readout says the input and output in words and in notation: "Day 80 (March 21): f(80) = 12.10 hours of daylight."
The scene plays that moment. A `Compare` toggle adds a second cursor and prints f(b) − f(a), b − a and the average
rate of change with units ("+2.68 minutes of daylight per day").

### Mark
A task list for the story (4 to 6 tasks). Tools:
- `Bracket x`: drag a span on the x axis (interval of increase, decrease, positive, domain).
- `Bracket y`: drag a span on the y axis (range).
- `Flag`: drop a flag on a point (maximum, minimum, intercept, a point where something happens).
- `Secant`: pick two points; the tool draws the line and prints its slope with units.
- `Answer`: a short box for a typed value where a task asks for one.
Each mark is checked when placed: right, or a short reason ("That span includes day 172, where it stops
increasing"). Tasks done per story saved on this device (localStorage `curio-graph-story-lab`, try/catch) with
`Clear progress`.

## Content
Data as of 2026-10-27 for the day length story (computed from the formulas in Sources, not measured). All other
stories are made-up situations, labeled "made-up story" on screen.
1. Daylight at 40° N (Denver, Philadelphia latitude). f(d) = hours from sunrise to sunset on day d of 2027 (a
   non-leap year), computed with the sunrise equation (Cooper declination δ = 23.45° sin(2π(284 + d)/365), sunrise when the sun's center is at −0.833°). Domain 1 to 365
   (whole days). Max 15.02 h on day 172 (June 21), min 9.32 h on day 355 (December 21). Average rate from day 60 to
   day 90 about +2.68 minutes per day. Tasks: flag the maximum and minimum; bracket where it increases (day 1 to 172
   and day 355 to 365); secant from day 60 to day 90; answer f(1) (9.38). Extra lines on `Other latitudes`: 25° N (max 13.69, min
   10.58) and 60° N (max 18.87, min 5.87).
2. Tea cooling. T(t) = 22 + 68e^(−0.045t) °C, t from 0 to 60 minutes. T(0) = 90, T(60) = 26.57; it approaches 22
   (room temperature) and never reaches it. Tasks: bracket the domain; flag the y-intercept; secant over the first 10
   minutes and over minutes 50 to 60 (the first is much steeper); answer "What value does T get close to?" (22).
3. Phone battery (piecewise). From 7:00 at 100 percent: down 6 percent an hour to 15:00 (52), on the charger up
   40 percent an hour to 16:00 (92), down 8 percent an hour to 22:00 (44). Tasks: bracket where it increases
   (15 to 16); flag the minimum on the day (52 at 15:00); secant 7 to 15 (−6 per hour); answer the battery at 20:00
   (60).
4. Stacking cups (sequence). h(n) = n + 11 cm for n = 1 to 20 cups (each cup adds 1 cm on a 12 cm first cup). Drawn
   as dots, not a line. Tasks: answer h(1) (12) and h(20) (31); bracket the domain, which must be whole numbers
   1 to 20 (a continuous bracket is refused with "can you stack 2.5 cups?"); answer the rate (1 cm per cup).
5. Parking garage (step function). $3 for the first hour or part of it, $2 for each extra hour or part, at most $15.
   Domain 0 < t ≤ 24 hours. Range {3, 5, 7, 9, 11, 13, 15}. Tasks: answer the cost for 2.5 hours (7); flag where
   it first reaches the cap (t just above 6); bracket the range (the tool asks for the list since the range is a set
   of values, not a span).
6. Pine Ridge hike. e(x) = 5000 + 540x − 180x² + 15x³ feet of elevation, x from 0 to 7.5 miles along the trail.
   Max 5480 ft at x = 2 (a local maximum), min 5000 ft at x = 6 (and at the start, x = 0), e(7.5) = 5253.1.
   Tasks: flag the local maximum and the local minimum; bracket where it decreases (2 to 6); secant from mile 6 to
   7.5 (+168.75 ft per mile).
7. A July day. T(h) = 77 + 10 sin(π(h − 9)/12) °F, h from 0 to 24 (midnight to midnight). Max 87 at 15:00, min 67 at
   3:00. Tasks: flag both; bracket where it is above 80 (about 10:10 to 19:50, h = 10.16 to 19.84); answer f(9) (77).
8. Oval track (not a function). The runner's position on an oval track graphed as y against x (an oval). In Read,
   the cursor finds two y values for one x and the readout says "Two outputs for one input: not a function of x."
   Task: tap `Function` or `Not a function`; then switch to `Time on x` and see distance along the track against
   time, which is a function.

## Interactions in detail
- Every story is a pure function in code; feature answers are computed from it (max and min by the formula or a
  fine search, checked against the values listed above) and the readouts round to the story's precision (hours to
  0.01, minutes to whole, money to the dollar, feet to whole).
- Bracket checks: endpoints within one step of the true value (day 1, minute 0.5, hour 0.25, mile 0.05); open or
  closed endpoints are not graded.
- Flag checks: within one step in x and on the curve. Secant: the slope is computed from the two picked points (no
  grading unless a task names an interval, then the endpoints must be within one step).
- The scene strip is decorative; everything it shows is also in the readout text.
- Motion off: the scene shows a still frame per cursor position.
- `window.__tool = {state, setMode, story(id), cursor(x), mark(kind, a, b), tasks()}`.

## Look
Accent `--brand #7af0c8` (mint), `--brand-ink #04201a`. Graph on `--gr-bg`, the story's curve in `--gr-1`;
brackets in the accent with end ticks; flags in `--gr-2` with a pennant shape and a text label; secant `--gr-4`
dashed. Scene strip drawn in code with flat shapes per story (sun arc, mug with steam lines, battery bar, cup stack,
parking ticket, trail profile with a hiker dot, thermometer, oval track with a runner dot). Contrast (computed):
brand on panel 12.47:1, on --sec-bg 11.81:1, brand-ink on brand 12.33:1.

## Art
none: drawn in code (scene strips, preview.svg). No people drawn beyond dots.

## Voice
Bank voice `smooth-narrator` (warm storyteller). Not used by math 9-12 neighbors or group siblings.
- wRead (how, Read welcome): "Drag the cursor along the graph. The scene below plays that moment."
- wMark (how, Mark welcome): "Pick a task, then use Bracket, Flag or Secant to mark it on the graph."
- compare (how, first Compare): "Two cursors now. The rate is the change in output over the change in input."
- right (event, a mark checks; stale on the next mark): "That's it."
- story (event, all tasks of a story done; stale on story change): "Story complete. Try another one."
- notFn (how, oval track opens): "Watch the readout as the cursor crosses the oval."

## Family engine
graphing (`kit/graphing.js`, docs/families/graphing.md), unchanged API. Uses `Plane` with per-story ranges, `g.fn`
for the curves (with `g.points` style dots for the cups story), `g.param` for the oval, `g.trace` for the cursor,
`g.extrema` as a cross-check of flagged features, `g.segment` for secants, `g.label`. Brackets and flags are the
tool's own SVG in the `front` layer.

## Sources
- F-IF.A and F-IF.B: Common Core State Standards for Mathematics, High School Functions, Interpreting Functions, https://www.thecorestandards.org/Math/Content/HSF/IF/
- Day length from the sunrise equation with the −0.833° correction for refraction and the sun's radius: NOAA Global Monitoring Laboratory, "General Solar Position Calculations", https://gml.noaa.gov/grad/solcalc/solareqns.PDF; checked against the U.S. Naval Observatory "Duration of Daylight/Darkness Table", https://aa.usno.navy.mil/data/Dur_OneYear (2026-10-27).
- Newton's law of cooling as an exponential approach to room temperature: OpenStax, Calculus Volume 2, 4.3, https://openstax.org/books/calculus-volume-2/pages/4-3-separable-equations (rate 0.045 per minute is made up for a mug).
- Key features, domain and range, average rate of change: OpenStax, College Algebra 2e, 3.2 and 3.3, https://openstax.org/books/college-algebra-2e/pages/3-3-rates-of-change-and-behavior-of-graphs
- Feature values recomputed in Python (2026-10-27): hike e(2) = 5480, e(6) = 5000, e(7.5) = 5253.125; tea T(60) = 26.57; battery 52, 92, 44.

## Done when
1. Daylight: cursor on day 172 reads f(172) = 15.02 h; day 355 reads 9.32; the computed values agree with the USNO table for 40° N to within 5 minutes on the 1st of every month (the Cooper formula is an approximation; the screen says so).
2. Compare from day 60 to day 90 prints about +2.68 minutes per day (to 0.05).
3. Hike: flags at x = 2 and x = 6 check as local max and local min; a bracket 2 to 6 checks as decreasing; secant 6 to 7.5 prints +168.75 ft per mile.
4. Cups: a continuous domain bracket is refused with the whole-number reason; h(20) = 31.
5. Parking: the cost for 2.5 hours is $7; the range task accepts the list 3, 5, ..., 15 and refuses a span.
6. Battery: the value at 20:00 is 60; the increase bracket is 15:00 to 16:00.
7. Oval track: the readout reports two outputs for one input; `Not a function` checks right.
8. Progress survives a reload; `Clear progress` works; every size in STANDARDS.md keeps the graph, scene strip and tools visible; keyboard only works; console clean, no network.
