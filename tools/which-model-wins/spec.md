# Which Model Wins?

## One idea
Three models (a line, a parabola, an exponential) compete on the same real data with its last rows hidden; you
shape each one by hand with transformation handles, pick your winner, then reveal the hidden rows, and the winner
is the model that predicts them, not the one that hugged the past: the parabola wins the stopping distances, and
the exponential that fits the young United States best is beaten when the 1870 and 1880 counts come in.

## Not like
- data-detective (gr 8, data-desk): one line of fit and a two-way table. Here three families compete and the test is prediction on hidden rows.
- model-my-world (gr 9, same group): exact rules from bills, every row must hit. Here real, imperfect data, and no model hits every row.
- correlation-guessing-game (gr 9, same group): judges r for a line. Here r² is one readout of several and the line often loses.
- outbreak-model and savings-plan (gr 11): exponential growth and logs, series. Here exponential is one contestant beside linear and quadratic, chosen from equal differences or equal ratios.
- function-family-reunion (gr 12, graphing): transformation sliders on parent functions with no data. Here the transformations exist to fit data.

## Who and how
- Grade 9, Algebra 1, Linear, Quadratic and Exponential Models. Students drive. 25 to 45 minutes.
- Topic line: "comparing linear, quadratic and exponential models".
- Standards (module): F-LE.A (A.1 equal differences vs equal factors, A.2 build from data, A.3 exponential eventually exceeds), F-BF.A (A.1b combine functions by adding: thinking + braking), F-BF.B (B.3 transformations by k: shift and stretch handles), F-LE.B (B.5 interpret parameters in context).
- CCSS clusters: Differences table serves F-LE.A.1; Build serves F-BF.B.3 and F-LE.A.2; Combine serves F-BF.A.1b; parameter cards serve F-LE.B.5; Long run serves F-LE.A.3.
- tool.json: driver "students", minutes "25-45", modes ["Look", "Build", "Reveal"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "The future decides." Dataset picker `Stopping distances`, `US population`,
`Two savers`. Modes `Look` (opens first), `Build`, `Reveal`. Kit buttons. Each dataset card shows "Data as of" and
its source line.
Stage: a data-desk scatter chart of the visible rows; hidden rows appear as dashed "?" columns at their x values.
Panel: the data table (visible rows), then the model cards.

### Look (explore)
The table with two extra toggle columns: `Differences` (y minus the row before) and `Ratios` (y divided by the row
before), and `Second differences`. A sentence under the table names what to notice without the answer ("Are the
differences steady? Are the ratios?"). Tapping a point highlights its row.

### Build
Three model cards, each with its own engine color and dash pattern, its equation in parameter form, handles on the
chart and sliders with number boxes:
- Line: y = m(x − x0) + y0; handles: a point (x0, y0) and a slope handle.
- Parabola: y = a(x − h)² + k; handles: the vertex (h, k) and a stretch handle.
- Exponential: y = c · b^(x − x0); handles: the anchor point (x0, c) and a growth handle (b).
Each card shows its mean absolute error on the visible rows ("misses the visible rows by 1.9 m on average") and
`Computer's best fit` (least squares; for exponential, least squares on log y), which moves the handles to the
best fit with Motion and prints r². A row of pick buttons `My winner: Line / Parabola / Exponential` and a reason
chip row (`Steady differences`, `Steady second differences`, `Steady ratios`, `It fits the visible rows best`).
Stopping distances adds a `Combine` card: Total = Thinking model + Braking model (F-BF.A.1b), where the student
builds a line for the thinking column and a parabola for the braking column, and the sum is drawn over the totals.

### Reveal
`Reveal the hidden rows`: the hidden points fall into place, each model's prediction for each hidden x is listed
with its error, and the model with the smallest mean absolute error on the hidden rows gets "wins". Your pick and
reason are shown beside it ("You picked Exponential for steady ratios; the hidden rows went to the Parabola").
`Long run` (Two savers and US population): the x range widens step by step (to 1950, or to 60 years) so the student
sees where each model goes. Parameter cards (F-LE.B.5) read the winning model in words (Content).

## Content
1. Stopping distances. UK Highway Code, rule 126, typical stopping distances (data as of the current Highway Code
   page). Speed v (mph): 20, 30, 40, 50, 60, 70. Thinking (m): 6, 9, 12, 15, 18, 21. Braking (m): 6, 14, 24, 38,
   55, 75. Total (m): 12, 23, 36, 53, 73, 96. Visible: 20 to 50; hidden: 60 and 70. Default column: Total.
   Best fits on the visible rows (computed): line 1.36v − 16.6 predicts 65.0 and 78.6 (mean error 12.7 m);
   parabola 0.015v² + 0.31v − 0.1 predicts 72.5 and 95.1 (0.7 m); exponential 4.841 · 1.0503^v predicts 91.8 and
   149.9 (36.4 m). Winner: parabola. Look: differences 11, 13, 17, 20, 23; second differences 2, 4, 3, 3 (steady
   only roughly: the table rounds to whole meters). Thinking differences are exactly 3 per 10 mph.
   Parameter card: thinking slope 0.3 m per mph means a reaction time of about 0.67 s (0.3 m ÷ 0.44704 m/s).
2. US population, census counts in millions (data as of the Census Bureau's historical table): 1790 3.929,
   1800 5.308, 1810 7.240, 1820 9.638, 1830 12.866, 1840 17.069, 1850 23.192, 1860 31.443, then hidden 1870 38.558
   and 1880 50.189; Long run adds 1890 62.980, 1900 76.212, 1910 92.228, 1920 106.022, 1930 123.203, 1940 132.165,
   1950 151.326. x = years since 1790. Ratios 1790 to 1860: 1.351, 1.364, 1.331, 1.335, 1.327, 1.359, 1.356 (steady:
   about 1.34 per decade); 1860 to 1870: 1.226.
   Best fits on 1790 to 1860: exponential 3.956 · 1.02996^x (fits the visible rows best; predicts 41.95 and 56.36,
   mean error 4.78 million); parabola predicts 38.79 and 47.93 (1.24 million); line predicts 30.70 and 34.44
   (11.8 million). Winner on the hidden rows: parabola. Long run to 1950: exponential 444.9 million, parabola 142.2,
   actual 151.3. The reveal card: "Steady ratios really did describe 1790 to 1860. Growth slowed after 1860 (the
   Civil War years, and later changes); a model only promises the pattern it was built on."
   Parameter card: exponential base 1.02996 per year means about 3.0 percent growth a year, about 34 percent a decade.
3. Two savers (model values, labeled "made-up savers, no real bank"). Ana puts $1,000 in a jar and adds $100 every
   year (y = 1000 + 100t); Ben puts $1,000 in an account that grows 6 percent a year and adds nothing
   (y = 1000 · 1.06^t). Visible: years 0 to 5 of Ben's account; hidden: years 10 and 20. Ben's values: 1000, 1060,
   1123.60, 1191.02, 1262.48, 1338.23; hidden 1790.85 (t = 10), 3207.14 (t = 20). Ana's jar is shown as a second
   series. Ben's account starts behind (year 5: Ana $1,500, Ben $1,338.23) and first passes Ana in year 18
   (Ana $2,800, Ben $2,854.34). Long run to 60 years: Ana $7,000, Ben $32,987.69. Winner on the hidden rows:
   exponential (it is the rule that made the data). Parameter card: base 1.06 means 6 percent growth each year.

## Interactions in detail
- Data comes in through `DataTable` with `columns` and units; the scatter, fits and r² come from the engine.
- Handles: dragging changes the parameters live; sliders and number boxes stay in sync; b is limited to 0.5 to 2,
  a to −1 to 1 (stopping) or −0.1 to 0.1 (population), never 0 (a zero stretch is refused with a tip).
- Errors: mean absolute error on the rows named, in the data's units, to 1 decimal (2 for millions).
- Winner on hidden rows: the smallest mean absolute error; ties within 0.05 units are called a tie.
- Two savers crossing: the tool finds the first whole year t where 1000 · 1.06^t > 1000 + 100t by stepping t
  (year 18) and prints it with both values.
- Combine: the Total curve is the pointwise sum of the student's two models; its error on hidden totals is listed.
- Switching datasets keeps each dataset's models this session; `Reset models` clears the current one.
- `window.__tool = {state, setMode, dataset(id), model(kind, params), errors(), reveal()}`.

## Look
Accent `--brand #ff8fd0` (pink), `--brand-ink #2b0a1e`. Chart on `#0e1520`; the three models use data-desk series
colors 1, 2, 3 with their dash patterns and shapes; hidden-row "?" columns dashed `#a6b3c4`; the winner gets a
"wins" tag in words. Contrast (computed): brand on panel 8.32:1, on --sec-bg 7.88:1, brand-ink on brand 8.66:1.

## Art
none: drawn in code.

## Voice
Bank voice `science-narrator` (clear documentary). Not used by math 9-12 neighbors or group siblings.
- wLook (how, Look welcome): "Turn on Differences and Ratios. One of them stays almost steady. Which one?"
- wBuild (how, Build welcome): "Drag each model's handles to fit the dots. Then pick your winner and a reason."
- wReveal (how, Reveal welcome): "Press Reveal to bring in the hidden rows. The best prediction wins."
- winner (event, reveal done; stale on dataset change): "The hidden rows have spoken. Compare your pick with the winner."
- combine (how, Combine opens): "Build the thinking part and the braking part. Their sum is the total."
- longRun (event, Long run finished; stale on dataset change): "Far enough out, the exponential always pulls away."

## Family engine
data-desk (`kit/data-desk.js`, docs/families/data-desk.md). Uses `DataTable` (one per dataset, hidden rows flagged
by a `hidden` column), `renderTable` (read-only, with the tool's Differences and Ratios columns added through two
computed columns), `Chart` type `scatter` with three overlaid model curves, `chart.fit('linear' | 'quadratic' |
'exponential')` for Computer's best fit, and `highlight(i)`. Engine additions needed (into the engine and the family
doc in the same change): computed columns (`columns: {d1: {label, compute: (row, prev) => ...}}`); a way to draw a
caller's function as a curve on a scatter chart (`chart.curve(id, f, {series})`); `fit` accepting a row filter so
hidden rows are left out. The handles, Combine, Reveal and Long run stay in this tool.
Dataset claims for the family table: UK Highway Code stopping distances; US census population 1790 to 1950; the
made-up Two savers. No other sibling may use them.

## Sources
- F-LE, F-BF: Common Core State Standards for Mathematics, High School Functions, https://www.thecorestandards.org/Math/Content/HSF/LE/ and https://www.thecorestandards.org/Math/Content/HSF/BF/
- Typical stopping distances: The Highway Code (UK Department for Transport), rule 126, "Stopping distances", https://www.gov.uk/guidance/the-highway-code/general-rules-techniques-and-advice-for-all-drivers-and-riders-103-to-158 (check the six rows against the page's figure when building; date pulled goes on screen).
- 1 mph = 0.44704 m/s (exact): NIST SP 811, Appendix B.
- US resident population by census, 1790 to 1950: U.S. Census Bureau, "Population and Housing Unit Counts" (2010 Census, CPH-2-1), Table 1, and the Census history page, https://www.census.gov/library/publications/2012/dec/cph-2.html (copy every figure from the table; 1870 to 1890 use the revised counts 38,558,371, 50,189,209 and 62,979,766).
- Linear vs exponential growth, equal differences and equal ratios: OpenStax, College Algebra 2e, 6.1 "Exponential Functions", https://openstax.org/books/college-algebra-2e/pages/6-1-exponential-functions
- Fits and predictions recomputed with numpy least squares (2026-10-27), values as in Content.

## Done when
1. Look on Stopping distances: Differences show 11, 13, 17, 20, 23 for Total and 3, 3, 3, 3, 3 for Thinking.
2. Computer's best fit on Total (20 to 50) gives the three equations in Content within rounding; Reveal lists 72.5 and 95.1 for the parabola and names it the winner.
3. US population: Ratios show about 1.33 to 1.36 up to 1860; exponential has the smallest visible error, and Reveal names the parabola the winner (1.24 vs 4.78 million mean error).
4. Long run on US population shows the exponential at about 445 million in 1950 against 151.3 actual.
5. Combine: a thinking line 0.3v and a braking parabola 0.015v² sum to predictions within 2 m of 73 and 96.
6. Two savers: the crossing is year 18 (Ana $2,800, Ben $2,854.34); Reveal names the exponential the winner at t = 10 and 20 (1,790.85 and 3,207.14).
7. Every dataset shows "Data as of" and its source; handles work by keyboard with value text; a stretch of 0 is refused.
8. Every size in STANDARDS.md keeps the chart and the active model card visible; console clean, no network.
