# Graph Studio (Curiosity No. 08)

## The real thing
A graphing plotter: type any equation and a pen draws it on graph paper. Engineers, scientists, economists and maths
teachers use plotters like this every day to see what a formula does, fit a curve to measurements and find where two
curves meet; students know its ancestor, the handheld graphing calculator. Here it is drawn as a pen plotter over an
engineering pad, with an equation tape and slide-rule sliders, and the pen draws the real function, point by point.

## Map
- Anchor: math-9-function-notation-and-graphs (F-IF.A, F-IF.B). Also reaches: math-8-defining-functions,
  math-8-modeling-with-functions, math-9-linear-quadratic-and-exponential-models, math-11-polynomial-functions,
  math-11-exponential-and-logarithmic-functions, math-11-trigonometric-functions, math-12-functions-and-their-graphs.
  Grade band 8 to 12, tuned for grade 9.
- The dozen graphing lesson tools planned in those modules stay; each can open this one.
- Teacher plan: yes, a plan could teach F-IF.A and F-IF.B well here (f(x) notation that evaluates, domain and range,
  key features marked on the curve, average rate of change between two pins). No plan.md in this build, so it is a
  second card beside graph-story-lab.

## The first two minutes
- On open: cream graph paper fills the screen. The pen carriage sits on its rail at the top. On the equation tape at
  the left, line 1 reads `y = x^2`, and the pen draws the parabola in about 1.2 s with a soft scratch (Sound on).
- First action, nothing read: the 2 in the exponent glows. Drag it up (or scroll on it) and it ticks 2, 3, 4; the
  curve redraws live, snapping from a bowl to an S to a steeper bowl. Drag it to 0.5 and half the curve vanishes.
- First reaction: type `a` in front of x on the tape. A slide-rule slider for a appears under that line on its own.
  Drag it through zero and the bowl flattens, turns over, and opens downward.

## Things to do
1. Drag any number in an equation and watch the curve move with it.
2. Type a letter such as a, b or k and drag the slider the plotter makes for it.
3. Plot y = 2^x and y = x^10 together and find both places they cross.
4. Define f(x) = x^2 - 3x and type f(4) on the next line to see the value printed.
5. Tap a curve and slide the trace pen along it, reading x and f(x) as it goes.
6. Drop two pins on a curve and read the slope of the line between them; slide one pin onto the other.
7. Turn on key points and see each zero, peak, valley and intercept marked with its coordinates.
8. Open the table for any line and scroll through x and y values in steps you choose.
9. Load the Mauna Loa carbon dioxide data and try a line, then a quadratic, and compare R squared.
10. Load the planets and look for the law Kepler found, then switch both axes to log scale.
11. Graph r = sin(4t) in polar and count the petals, then change 4 to 5.
12. Plot x = cos(3t), y = sin(2t) as a parametric curve and change the two numbers.
13. Paste your own two columns of numbers from a spreadsheet and fit a curve to them.
14. Save a page of graphs on this device and come back to it.

## Controls
- Equation tape (left): up to 8 lines, each with its own pen colour. Type with the keyboard; Enter makes a new line;
  Delete on an empty line removes it. Grammar: + - * / ^, implicit multiplication (2x, 3(x+1)), pi, e, sqrt, abs, sin,
  cos, tan, asin, acos, atan, ln, log, exp, floor, round. Forms: y = ..., x = ..., f(x) = ... and g(x) = ...,
  f(number) to evaluate, r = ... in t (polar), (x(t), y(t)) (parametric), (a, b) for a point.
- Number scrubbing: drag or scroll any number on the tape; with it focused, up and down arrows change its last digit,
  Shift multiplies the step by 10.
- Sliders, one per free letter, made automatically: drag the cursor; set minimum, maximum and step in the slider's end
  caps (defaults -10, 10, 0.1); arrows step, Page keys step 10 times; a play toggle sweeps the slider back and forth.
- Paper: drag to pan, wheel or pinch to zoom, +, - and 0 keys (0 resets to -10 to 10); square-grid toggle; log scale
  toggles for each axis; degrees or radians switch (radians by default).
- Trace pen: tap a curve or press T; left and right arrows move along it, up and down switch curves.
- Pins: P drops a pin at the trace point; drag pins along their curve; Escape clears them. Tangent toggle (G).
- Key points toggle (K): zeros, extremes, intercepts and intersections of the selected lines.
- Data drawer: a two-column table; paste, type or load a bundled set; fit selector (line, quadratic, exponential,
  power, none). Table drawer: x start and step per line.
- Notebook: 4 save slots on this device and 6 setups (rose curves, the 2^x race, parabola family, Lissajous,
  Mauna Loa, planets).
- Power panel on the plotter's base, top right: Motion, Sound, Read toggles.

## Readouts
- Cursor (x, y) at the paper's bottom right, and the trace's x, f(x) and line name on a brass tag riding with the
  pen; all monospace, 4 significant figures.
- Pins: both coordinates, the change in y over the change in x, and "average rate of change = 2.000" on a tag between
  them; tangent slope to 4 significant figures when the tangent is on (numeric derivative).
- Key points: coordinates beside each mark (an open circle where a function is undefined). Evaluations: f(4) = 4
  at the right end of its tape line.
- Fit: the fitted equation with coefficients to 4 significant figures, R squared to 4 decimals, n points, on the data
  drawer's foot.

## The Manual
Lower-left drawer. Contents: the equation grammar with examples; what each readout means; how fits are computed (least
squares, exponential and power by fitting logs); honesty notes; sources. "Things people have found":
- 2^x and x^10 cross twice, near x = 1.078 and x = 58.77; after the second crossing 2^x stays ahead forever (computed
  2026-11-05; any exponential with base above 1 outgrows any polynomial, OpenStax College Algebra 2e, chapter 6).
- The planets fall on one straight line when the square of the year is plotted against the cube of the distance; on
  log axes the line's slope is 1.5 (fit of NASA data gives 1.4997; Kepler's third law, 1619).
- Mauna Loa's yearly carbon dioxide fits a straight line with R squared 0.981, but a quadratic fits with 0.9995: the
  rise is speeding up (NOAA GML annual means 1959 to 2025, fitted 2026-11-05).
- From 1790 to 1860 the US population grew about 3.0 percent a year, close to an exponential; after that it bends below
  it (US Census Bureau decennial counts).
- A rose r = sin(n t) has n petals when n is odd and 2n when n is even (Wolfram MathWorld, "Rose").
- y = sin(x)/x looks smooth through x = 0 but has no value there: zoom in and the hole is still there, at height 1.
- y = (1 + 1/n)^n creeps up toward e = 2.71828... as the slider n grows (OpenStax College Algebra 2e, 6.1).
- x = cos(3t), y = sin(2t) draws a Lissajous figure, the same shape an oscilloscope draws from two tones whose
  frequencies are in the ratio 3 to 2 (Wolfram MathWorld, "Lissajous Curve").

## Look
- Grammar: a pen plotter over an engineering pad. Cream paper with a fine green grid (minor every unit, major every 5),
  axes in darker ink with tick numbers in a small drafting hand (monospace); a metal rail across the top with a pen
  carriage that runs to where the pen is drawing; curves drawn in technical-pen inks with a slight ink-spread edge.
  The equation tape is a strip of adding-machine paper down the left with the typed lines; sliders are slide-rule
  bars with an engraved scale and a clear cursor with a hairline. No calculator body, no LCD, no app-style list with
  coloured dots: it must not look like any branded graphing calculator or graphing website in name, look or layout.
- Palette: paper #f4f1e4, minor grid #d5e2cf, major grid #a9c3a0, axes #4a4a44, tape #fbf8ee, brass #b08d57; inks
  black #1b1b1b, red #b8322a, blue #1f4e9a, green #2d6a3e, violet #5b3a8c, brown #7a4a1e, teal #116466, orange #a4480a.
  Every ink at least 4.5:1 on the paper; notes.md states the ratios.
- 1366x768: tape at the left (about 300 px wide), paper filling the rest, rail along the top, sliders under their own
  tape lines, the data and table drawers sliding out over the tape; power panel on the plotter base top right; the
  plate "Curio Class Curiosities · No. 08 · Graph Studio" and the Manual handle lower-left, under the tape, as on
  Span and Spire and Pocket Universe.
- 375x812: paper on top (about 60 percent of the height), tape below it as a scrolling strip with the active line and
  its sliders always showing, drawers as bottom sheets; plate and Manual handle lower-left.

## Real material and sources
- The maths itself: an expression parser and plotter written for this tool (no eval of typed text). Adaptive
  sampling: at least one sample per screen pixel, refined where the curve bends, breaks drawn at undefined points and
  jumps (tan, 1/x).
- Mauna Loa CO2 annual means, ppm, 1959 to 2025, NOAA Global Monitoring Laboratory (co2_annmean_mlo.txt; "freely
  available to the public", US government work; cite GML). Values in year order, checked 2026-11-05:
  315.98 316.91 317.64 318.45 318.99 319.62 320.04 321.37 322.18 323.05 324.62 325.68 326.32 327.46 329.68 330.19
  331.13 332.03 333.84 335.41 336.84 338.76 340.12 341.48 343.15 344.87 346.35 347.61 349.31 351.69 353.20 354.45
  355.70 356.54 357.21 358.96 360.97 362.74 363.88 366.84 368.54 369.71 371.32 373.45 375.98 377.70 379.98 382.09
  384.02 385.83 387.64 390.10 391.85 394.06 396.74 398.81 401.01 404.41 406.76 408.72 411.65 414.21 416.41 418.53
  421.08 424.61 427.35
- US population, millions, 1790 to 2020 every 10 years, US Census Bureau decennial counts (public domain): 3.93 5.31
  7.24 9.64 12.87 17.07 23.19 31.44 38.56 50.19 62.98 76.21 92.23 106.02 123.20 132.16 151.33 179.32 203.30 226.54
  248.71 281.42 308.75 331.45.
- Planets, distance in AU and year in Earth years, NASA Planetary Fact Sheet (public domain): Mercury 0.387 0.241,
  Venus 0.723 0.615, Earth 1 1, Mars 1.524 1.881, Jupiter 5.203 11.86, Saturn 9.537 29.46, Uranus 19.19 84.01,
  Neptune 30.07 164.8.
- Budget: data under 3 KB; code about 250 KB; no images. Goal under 400 KB.

## Honesty notes
In the Manual: the plotter samples the curve, so very fast wiggles (sin(1000x)) can alias, and it says so when the
sample count is too low for the zoom; key points and intersections are found numerically to about 6 significant
figures; the tangent is a numeric slope; R squared for exponential and power fits is computed on the logs; the
bundled data are yearly averages or official counts, rounded as shown.

## Voice
Bank voice wise-mentor (a thoughtful maths teacher leaning over the plotter), unlike Span and Spire (firm-captain) and
Pocket Universe (casual-peer). First-run hint, spoken once: "Drag the 2 up or down." Read speaks the hint, then the
active line and the trace, written for the ear: "y equals x squared. At x equals 3, y equals 9." The numbers are
spoken only if the kit's read fallback speaks text that has no recording; otherwise Read gives the hint alone and the
readouts reach screen readers through a polite live region.

## Done when
1. Opening draws y = x^2 with nothing typed; dragging the exponent redraws live with no lag at 60 fps.
2. Typing a new letter makes its slider at once; the slider's play toggle sweeps it smoothly.
3. f(x) = x^2 - 3x with f(4) on the next line prints f(4) = 4.
4. 2^x and x^10: key points show crossings near 1.078 and 58.77 (zoomed out far enough).
5. Mauna Loa: a line gives R squared 0.981 and a quadratic 0.9995 (to the stated decimals).
6. Planets on log-log axes: a power fit gives exponent 1.500 within 0.01.
7. Pins on y = x^2 at x = 1 and x = 3 read an average rate of change of 4.000.
8. tan(x) and 1/x draw with breaks, not vertical joining lines; sin(x)/x shows an open circle at (0, 1).
9. Every control works by keyboard and announces its value; Motion off draws curves at once, no pen travel.
10. 680x425, 1366x768, 1920x1080 and 375x812 keep the paper and the active tape line visible without page scroll.
11. One offline file, no network, passes scripts/check_tools.py, no em dashes; the short test answered in the report.
12. No score, goal, level, sticker or finish screen anywhere.

## Open questions
- Inequalities (y < x^2 shaded)? Lean: leave out of this build, add in a fix round if wanted.
- Implicit equations (x^2 + y^2 = 25)? Lean: later, with marching squares, unless time is left in this build.
- Should lesson tools open Graph Studio with a preloaded equation (a URL hash such as #y=2x+1)? Lean: yes, read-only
  hash parsing, nothing sent anywhere.
