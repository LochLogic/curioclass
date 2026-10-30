# Data Desk: Distributions

## One idea
Describing a distribution is a claim, and every clause of it needs evidence on the chart. You build a description
from chips (shape, center, spread, anything unusual) about real data, and each chip lights up its proof as you add it:
the bins that make the tail, the median line, the IQR bracket, the fence the outlier crosses. Check marks every
clause backed or not backed.

## Not like
- box-plot-builder (gr 6, data-desk): drag one point and watch mean and median react. Here whole real distributions, described in words with evidence, plus z-scores and the normal model.
- correlation-guessing-game (gr 9): judging r and residuals. Here the scatter desk only describes form, direction, strength and a log rescale; r and residual plots stay there.
- sample-machine (gr 12, same group): distributions of a statistic over many samples. Here distributions of data.
- region-compare (gr 6, data-desk): regions side by side on population, income, language and climate. Here life expectancy by country, and the comparison is shape, center and spread, not rankings.
- economy-dashboard (gr 12, data-desk): time series of the economy. Here one moment in time, one or two variables.

## Who and how
- Grade 12, Statistics, Math: statistics. Students drive, alone or in pairs. 20 to 40 minutes.
- Topic line: "describing distributions: shape, center, spread and outliers".
- Standards (module): AP-STAT.U1; AP-STAT.U2; S-ID.A.
- CCSS clusters: Explore serves S-ID.A.1 (dot plots, histograms, box plots), S-ID.A.2 (center and spread, compare
  groups), S-ID.A.3 (shape and outliers, effect of outliers) and S-ID.A.4 (normal model and percentages). Describe
  serves S-ID.A.2 and A.3.
- AP-STAT.U1 (Exploring One-Variable Data): desks 1 to 3. AP-STAT.U2 (Exploring Two-Variable Data): desk 4 only
  (form, direction, strength, unusual points, a log transform); see Open questions.
- tool.json: driver "students", minutes "20-40", modes ["Explore", "Describe"], grades_label "Grade 12".

## Screens and modes
Header: title, subtitle "Every claim needs a mark on the chart." Modes `Explore` (opens first), `Describe`. Desk
picker (4 desks): a row of four small cards, each a painted picture (art: desk-ages, desk-statehood, desk-lifespan,
desk-wealth) with the desk's name typed in code under it. Kit buttons.
Stage: the chart on graph paper, centered and as large as the stage allows (the focus in both modes); under it the
stats readout. Panel: controls (Explore) or the description builder
(Describe). A "data as of" line sits under every real-data chart.

### Explore
Focus: the chart. A tapped dot's label card opens beside the dot, on the chart, not in the panel.
- Chart type: `Dot`, `Histogram`, `Box` (desk 4: `Scatter`). Bin width slider for histograms (settable start too).
- Stats readout: n, min, Q1, median, Q3, max, IQR, mean, SD, fences and outliers.
- Tap or arrow to a dot: its label, value, z-score and percentile (percent of values below it).
- `Normal model`: overlays the normal curve with the data's mean and SD and a table: within 1, 2, 3 SD, data versus
  68, 95, 99.7.
- `Units lens` (desk 1 and 2): re-express the variable (add a constant, multiply by a constant) and watch which stats
  move. Readouts show old and new side by side.
- Desk 3: `Split by region` draws side-by-side box plots on one axis.
- Desk 4: `Log x` toggle redraws the x axis on a log scale and refits the line; readouts r and the line.

### Describe
Focus: the chart with the evidence marks; the growing sentence sits right under the chart so the eye goes from a mark
to its clause. The chip rows are in the panel.
Four chip rows, one claim each, plus a context row filled in by the desk (variable, units, who):
- Shape: `Roughly symmetric`, `Skewed left`, `Skewed right`, `Two peaks`, `Uniform`.
- Center: `Median = ...`, `Mean = ...` (values filled from the data; the student picks which measure).
- Spread: `IQR = ...`, `SD = ...`, `Range = ...`.
- Unusual: chips built from the data (`Outlier at 78`, `Gap from 1912 to 1959`, `Cluster from 1787 to 1790`,
  `None`), plus decoys that are not true.
Each chip, when added, marks its evidence on the chart (the long tail's bins tinted, the median line, the IQR bracket,
the fence line and the outlier ringed, the gap shaded). The sentence builds as text: "The distribution of ages at first
inauguration is roughly symmetric, centered at a median of 55 years, with an IQR of 9.5 years and one high outlier at
78." `Check` marks every clause "backed" or "not backed" with the reason (for example: the mean is a fine center
for a symmetric shape, but for a skewed one the median and IQR are the backed pair).
Desk 4 Describe uses form (linear, curved), direction, strength (weak, moderate, strong) and unusual points.

## Content
Desk 1, Presidents' ages at first inauguration (45 people, Washington through Biden; Cleveland and Trump counted once,
at their first inauguration): 57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47,
55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70, 78.
- Min 42, Q1 51, median 55, Q3 60.5, max 78; IQR 9.5; mean 55.511; SD 7.4334. Fences 36.75 and 74.75: outlier 78.
- Within 1, 2, 3 SD: 31 (68.9%), 44 (97.8%), 44 (97.8%).
- Kennedy 43: z = -1.683, percentile 2.2. Biden 78: z = 3.025, percentile 97.8.
- Lens "years over 35" (minimum age): median 20, mean 20.511, IQR and SD unchanged. Lens "months": median 660, mean
  666.13, SD 89.20, IQR 114.
- Histogram, 5-year bins from 40: 2, 7, 13, 11, 7, 3, 1, 1. Shape: roughly symmetric with a slight right tail.
Desk 2, Year each state joined the Union (50; the 13 original states by year of ratifying the Constitution):
Delaware, Pennsylvania, New Jersey 1787; Georgia, Connecticut, Massachusetts, Maryland, South Carolina, New Hampshire,
Virginia, New York 1788; North Carolina 1789; Rhode Island 1790; Vermont 1791; Kentucky 1792; Tennessee 1796; Ohio
1803; Louisiana 1812; Indiana 1816; Mississippi 1817; Illinois 1818; Alabama 1819; Maine 1820; Missouri 1821; Arkansas
1836; Michigan 1837; Florida, Texas 1845; Iowa 1846; Wisconsin 1848; California 1850; Minnesota 1858; Oregon 1859;
Kansas 1861; West Virginia 1863; Nevada 1864; Nebraska 1867; Colorado 1876; North Dakota, South Dakota, Montana,
Washington 1889; Idaho, Wyoming 1890; Utah 1896; Oklahoma 1907; New Mexico, Arizona 1912; Alaska, Hawaii 1959.
- Q1 1790, median 1836.5, Q3 1876, IQR 86, mean 1839.7, SD 47.85. Fences 1661 and 2005: no outliers.
- Unusual: a gap from 1912 to 1959; a cluster of 13 states from 1787 to 1790. Shape skewed right.
- 20-year bins from 1780: 16, 6, 4, 7, 5, 7, 3, 0, 2.
- Lens "years as a state in 2026" (2026 minus year): skewed left, median 189.5, mean 186.3. A flip, not a new shape.
Desk 3, Life expectancy at birth, 2024 (World Bank, indicator SP.DYN.LE00.IN): countries and economies (no regional or
income aggregates) with 2024 population (SP.POP.TOTL) at least 1,000,000 and a 2024 value; n = 160; values to 0.1 year.
- Min 54.6 (Nigeria), Q1 67.6, median 74.2, Q3 78.9, max 85.4 (Hong Kong SAR, China); IQR 11.3; mean 73.28; SD 7.385.
  Fences 50.65 and 95.85: no outliers. Skewed left.
- 5-year bins from 50: 1, 5, 20, 29, 32, 38, 34, 1.
- By World Bank region (n, median, IQR): Sub-Saharan Africa 44, 63.95, 5.65; Europe & Central Asia 46, 78.4, 6.5;
  Latin America & Caribbean 23, 75.3, 5.6; Middle East, North Africa, Afghanistan & Pakistan 22, 76.6, 9.1; East Asia &
  Pacific 19, 74.7, 13.2. South Asia (4) and North America (2) show as points with a "too few for a box plot" note.
- Data as of: World Bank data last updated 2026-10-08, pulled 2026-10-27.
Desk 4, Life expectancy against GDP per capita, 2024 (NY.GDP.PCAP.CD, current US$): the desk 3 countries with both
values, n = 154 (no 2024 GDP for Cuba, Eritrea, Korea Dem. People's Rep., South Sudan, Syria, Yemen).
- Raw x: r = 0.7015, line LE = 69.52 + 0.000222 × GDP; clearly curved.
- Log10 x: r = 0.8862, r² = 0.785, line LE = 33.79 + 10.31 × log10(GDP): each tenfold rise in income goes with about
  10.3 more years.
- Farthest from the log line: Nigeria -10.4, Equatorial Guinea -9.5, Chad -9.4; Lebanon +6.5, Sri Lanka +6.2.
- The build agent pulls desks 3 and 4 from the World Bank API with exactly these rules, stores them as JSON in the
  tool, and checks n and the summary values above before shipping.

## Interactions in detail
- Quartiles by the median of halves (exclude the median when n is odd), the AP and OpenStax textbook method; the engine
  must use this (see Family engine). SD with n - 1. Fences Q1 - 1.5 IQR and Q3 + 1.5 IQR.
- Percentile = percent of values strictly below; z = (x - mean) / SD, 3 places.
- Describe checks: Shape against the desk's stored answer (desk 1 accepts symmetric or slightly skewed right);
  Center and Spread must be a matched pair (median with IQR for skewed or outlier data, mean with SD allowed only for
  roughly symmetric data without outliers); Unusual chips must match the fence rule or a stored gap or cluster;
  decoys are marked not backed.
- Chart changes (chart type, bins, lens, Log x, an evidence mark) redraw with a short ease of at most 300 ms (none
  with Motion off); a tap during it acts at once on the newest state, and nothing else plays on its own.
- Every chart has a text alternative listing its numbers; the evidence marks have text labels.
- Last desk and chart type remembered on device (localStorage `curio-ddd-last`, try/catch) with `Clear`.
- `window.__tool = {state, setMode, desk(i), stats(), chart(type), bins(w, start), lens(k), describe(chips), check()}`.

## Look
Light graph-paper theme overriding kit/theme-912.css tokens (see Open questions): paper `#eef2f6` with a faint
`#dfe6ee` grid, panel `#ffffff`, sections `#f7f9fb`, ink `#1b2430`, muted `#56606e`, button line `#7b8794`, header
`#e6ecf2`, ok `#1f7a3f`, warn `#a3261b`, focus `#0b6bcb`. Accent `--brand #7a2e8e` (plum: chips, evidence marks,
the Check button). Region series on white: `#1f6fb2`, `#b45309`, `#2f7d4f`, `#b0306a`, `#5b5bd6`, `#4b5563`, each with
its own marker shape.
Contrast (computed): ink on panel 15.65:1; muted 6.04:1; brand on panel 8.05:1, on sections 7.63:1; white on brand
8.05:1; header text 13.15:1; focus 5.28:1; button line 3.47:1 (non-text); ok 5.08:1; warn 6.98:1; series 5.28, 5.02,
5.04, 6.04, 5.37, 7.56:1. No celebration: Check shows a count of backed clauses.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: soft painted still life, light and airy, on pale gray-blue,
to sit on the light graph-paper theme. The charts themselves are drawn in code; these four pictures only mark the
desks so a student can tell them apart at a glance.
- desk-ages: "An empty wooden lectern on a small stage in front of a deep blue curtain, a glass of water on a side
  table, soft light, painted still life"; 4:3; cutout no; people no; desk 1 card (presidents' ages).
- desk-statehood: "A stack of old parchment documents tied with ribbon beside a red wax seal, a quill and an inkwell
  on a wooden desk, the papers blank, soft light, painted still life"; 4:3; cutout no; people no; desk 2 card
  (statehood years).
- desk-lifespan: "A small desk globe beside a potted plant and a pair of reading glasses on a light wooden table, soft
  morning light, painted still life"; 4:3; cutout no; people no; desk 3 card (life expectancy).
- desk-wealth: "A brass balance scale on a wooden table, a short stack of plain blank coins on one pan and a sprouting
  seedling in a small pot on the other, soft light, painted still life"; 4:3; cutout no; people no; desk 4 card (life expectancy and income).
Dot plots, histograms, box plots, scatter plots, evidence marks, chips, the graph paper and preview.svg are drawn in
code (the tool is otherwise all charts).

## Voice
Bank voice `upbeat-guide` (Zephyr; bright, encouraging data-desk host). Not used by grade 12 math neighbors or group
siblings. `Curio.voice`, `scope: () => state.mode + ':' + state.desk`. Readouts and reasons are read on screen; Read
speaks the hint.
- wExplore (how, Explore welcome; stale after the first chart-type tap): "Tap Dot, Histogram or Box to switch the chart. Then tap any dot to see where it stands."
- normal (how, first Normal model; stale when Normal model is turned off): "The curve uses the data's mean and SD. Compare the table with sixty-eight, ninety-five, ninety-nine point seven."
- wDescribe (how, Describe welcome; stale once a chip is added): "Tap one chip from each row. Each one shows its evidence on the chart. Then press Check."
- notBacked (event, Check with any clause not backed; stale on chip change): "Some claims aren't backed yet. Read the reason under each one, then swap that chip."
- allBacked (event, Check all backed; stale on desk change): "Every claim is backed by the chart."
- logx (how, first Log x on desk 4; stale when Log x is turned off): "Same data, new scale. Watch the curve straighten."

## Family engine
data-desk (`kit/data-desk.js`, docs/families/data-desk.md). Uses DataTable, t.stats, Chart types dot, histogram,
box (with groupBy) and scatter, chart.fit('linear'), highlight and onPoint. Asks the engine for (into the engine and
the family doc in the same change, existing calls kept working):
1. Quartiles by median of halves as the documented rule of t.stats (and its unit test with desk 1: Q1 51, Q3 60.5).
2. Settable histogram bin width and start (`bins: {width, start}`).
3. Evidence marks: `chart.mark({kind: 'line' | 'bracket' | 'fence' | 'ring' | 'shade', at, to, label})`.
4. A log x axis option (`xScale: 'log10'`), with fit run on log10(x).
5. A normal curve overlay on histograms (`chart.curve` from which-model-wins' ask, with a density helper).

## Sources
- S-ID.A: Common Core State Standards for Mathematics, Interpreting Categorical and Quantitative Data, https://www.thecorestandards.org/Math/Content/HSS/ID/
- AP-STAT.U1 and U2: College Board, AP Statistics Course and Exam Description, https://apcentral.collegeboard.org/courses/ap-statistics
- Describing distributions, quartiles, outliers, z-scores and the normal model: OpenStax, Introductory Statistics 2e, chapter 2 "Descriptive Statistics" and 6.1 "The Standard Normal Distribution", https://openstax.org/books/introductory-statistics-2e/pages/2-introduction
- Presidents' ages: computed from birth and first inauguration dates, The White House, "Presidents", https://www.whitehouse.gov/presidents/, cross-checked with the Miller Center (University of Virginia) president pages, https://millercenter.org/president; data as of 2026-10-27.
- Statehood years: U.S. Senate, "States in the Senate", https://www.senate.gov/states/statesmap.htm; the original 13 by ratification year, National Archives, "The Constitution: How Did it Happen?", https://www.archives.gov/founding-docs/constitution/how-did-it-happen
- Life expectancy and GDP per capita: World Bank, World Development Indicators, SP.DYN.LE00.IN, NY.GDP.PCAP.CD, SP.POP.TOTL, https://data.worldbank.org/indicator/SP.DYN.LE00.IN (CC BY 4.0); last updated 2026-10-08, pulled 2026-10-27.
- Every summary value above was recomputed in Python on 2026-10-27.
- Checks run again (Python, numpy and scipy, 2026-10-29), all match the Content list: desk 1 n 45, quartiles by the
  median of halves 51, 55, 60.5, mean 55.511, SD 7.4334, fences 36.75 and 74.75 (only 78 outside), within 1, 2, 3 SD
  31, 44, 44, Kennedy z -1.683 at 2.2, Biden z 3.025 at 97.8, lenses (years over 35: median 20, mean 20.511; months:
  median 660, mean 666.13, SD 89.20, IQR 114), bins 2, 7, 13, 11, 7, 3, 1, 1, sample skewness 0.71 (so "slight right
  tail" is fair). Desk 2 n 50, Q1 1790, median 1836.5, Q3 1876, mean 1839.7, SD 47.85, fences 1661 and 2005, bins,
  flip median 189.5 and mean 186.3. Desks 3 and 4 re-pulled from the World Bank API (last updated 2026-10-08): n 160,
  quartiles 67.6, 74.2, 78.9, min 54.6, max 85.4, mean 73.28, SD 7.385, bins, every region n, median and IQR; n 154,
  raw r 0.7015, log r 0.8862, line 33.79 + 10.31 log10(GDP), the five largest residuals.

## Done when
1. Desk 1 readout: Q1 51, median 55, Q3 60.5, IQR 9.5, mean 55.511, SD 7.433, outlier 78; Kennedy z -1.683, percentile 2.2.
2. Units lens months gives SD 89.20 and IQR 114; years over 35 leaves SD and IQR unchanged.
3. Desk 2 shows no outliers, the gap 1912 to 1959 and the 1787 to 1790 cluster as true chips.
4. Desk 3 has n 160, median 74.2, IQR 11.3, and the "data as of" line; region boxes show 5 regions, 2 flagged too few.
5. Desk 4 Log x reads r 0.886 and the line 33.79 + 10.31 log10(GDP).
6. Describe with "mean and SD" on desk 3 marks the pair not backed with the skew reason; the desk 1 example sentence checks fully backed.
7. Focus: at 1366x768 and 1000x625 the chart is the largest thing on the stage in both modes, the dot label opens on
   the chart, and in Describe the sentence sits under the chart.
8. Tap while it plays: switching chart type, bins or a chip during a redraw ease acts at once, and the readout and
   marks match the final state.
9. The four desk cards show their pictures; no image has people or lettering.
10. Every size in STANDARDS.md keeps the chart, the stats readout and the chip rows visible without page scrolling; keyboard only works; console clean, no network.

## Open questions
- [data-desk-distributions] AP-STAT.U2 is covered only by desk 4 (form, direction, strength, a log transform); r, residuals and two-way tables live in correlation-guessing-game and data-detective. Enough, or add a two-way table desk?
- [data-desk-distributions] Desk 1 includes recent presidents (Trump 70, Biden 78). Fine for classrooms, or stop at an earlier president?
- [data-desk-distributions] The light graph-paper theme overrides the dark 9-12 theme. OK?

Data note (integrator, BR1, 2026-10-28): the Old Faithful geyser data is used by simulation-studio; don't add it here.
