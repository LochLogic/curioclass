# Population Dashboard

## One idea
Every resource total is people times use per person, so the dashboard draws a country's energy use as a rectangle
(width = people, height = use per person) and splits the change since 1990 into three colored strips, "more people",
"more use per person" and "both together", which shows at a glance that India's and Nigeria's growth comes from
different strips than China's, and that the US and Germany shrank use per person while their populations grew; then
the future is a UN fan of possible populations, not a line, and a calculator shows what sets how many people the
world's grain could feed.

## Not like
- carrying-capacity (grade 9, sci-bio): deer and the regrowth of their food in one habitat, simulated; here it is
  real human data, and the Feed calculator is a formula with stated assumptions, not a simulation.
- island-economy (grade 9, sci-earth-phys): you manage resources over generations; here nothing is managed, you read
  and decompose real data.
- climate-dashboard (grade 9): temperature and CO2 series; this tool never shows temperature or CO2.
- which-model-wins (wave 2): fits models to the US census 1790 to 1950; here the future comes from the UN's own
  projections, and no curve fitting happens.
- data-desk-distributions (wave 2): describes distributions of World Bank life expectancy and income; here eight
  countries' energy and population over time, and the move is decomposition, not describing a distribution.
- compound-interest-head-start (wave 2): growth math with money; no rates are computed here.
- cloud-through-time (wave 2): data centers' electricity and water; here whole countries' primary energy.
- Grid Operator (this group): runs one made-up grid hour by hour; this tool uses only real, dated data.

## Who and how
- Grade 12, Environmental science (Earth and Space Science), Population and Resources. Students drive, pairs work
  well; a teacher can project Split for a class discussion. 25 to 40 minutes.
- Topic line: "human population growth and resource use".
- Standards (module): HS-ESS3-1 (resource availability and human activity: Feed's "people, yields and land" panel
  shows population growth matched by yield growth, with land per person falling), HS-LS2-1 (mathematical
  representations of factors that affect carrying capacity: the Feed calculator at world scale).
- tool.json: driver "students", minutes "25-40", modes ["Split", "Future", "Feed"], grades_label "Grade 12".

## Screens and modes
Layout: chart stage left, panel right (country chips, mode tabs, readouts). Country chips (8, one selected, plus
**Compare** to pin a second) stay at the top of the panel at every size; at 760 wide and below they become a
scrollable row above the stage. "Data as of" line under every chart.

**Split (default).** Focus: the two rectangles and their strips, filling most of the stage. Stage: the rectangle view. Two rectangles share a bottom-left corner: 1990 (outlined, `--muted`)
and 2024 (filled). Width = population (millions), height = primary energy per person (kWh). The change becomes strips:
- right strip, "More people": (P2024 - P1990) x e1990, `--gr-1` with dots pattern
- top strip, "More use per person": P1990 x (e2024 - e1990), `--gr-2` with diagonal hatching
- corner, "Both together": (P2024 - P1990) x (e2024 - e1990), `--gr-3` solid
A strip whose value is negative is drawn inside the 1990 rectangle as an outlined, cross-hatched "removed" band with
its label in words ("less use per person"). Both axes rescale per country so the shapes fill the stage; a **Same
scale** toggle puts all countries on World's scale (small countries become tiny; that is the point).
Panel readouts: the three strips in TWh and as percent of 1990 total, the total change, and a one-line reading
built from the numbers ("Most of the growth came from more use per person."). **Compare** shows two countries'
rectangles side by side at the same scale. A small **Over time** line chart below the rectangles (about a fifth of the stage height) shows energy per
person from 1965 to 2024 for the selected countries (data-desk chart, `--gr-1`, `--gr-2`).

**Future.** Focus: the fan chart, filling the stage. Stage: population 1950 to 2100. Solid line to 2023 (estimates), then the UN fan: 95 percent band (light),
80 percent band (darker), median line, and the Low and High variants as dashed lines labeled "Low (half a child
fewer)" and "High (half a child more)". A legend says the bands are the UN's probabilities, while Low and High are
"what if" lines with no probability. Year slider (2024 to 2100) with a readout of median, both bands and both
variants for that year. Buttons: **2050**, **2100** (jump), **Show peak** (marks the median's highest year; China,
Japan and Germany peak before 2050; a country whose median is highest in 2100 reads "still rising in 2100").

**Feed.** Focus: the bar against the population line, centered on the stage. Stage: a stacked bar (people the world's cereal could feed, in billions) against a horizontal line for the
2023 world population (8.09 billion). Sliders: **Cereal land** (400 to 1,000 million hectares, default 739.4),
**Yield** (1.0 to 9.0 tonnes per hectare, chips **1961**, **1990**, **2023**, **US 2023**), **Share eaten by people**
(0 to 100 percent, chips **Today 45.6 percent** and **All of it**), **Calories per person per day** (1,800 to 3,000, default
2,100). The formula is written out live with the numbers in it. Under it, the **People, yields and land** panel: three
small bars, 1990 to 2023: population +51.9 percent, cereal yield +53.3 percent, arable land per person -24.2 percent,
with the sentence "Yields kept pace with people while land per person shrank." Model note: "If every calorie came from
cereal. People also eat vegetables, fruit, oils, sugar, meat, milk and fish; feed grain becomes meat, milk and eggs,
at a loss. The real limit also depends on water, soil, energy and how food is shared."

## Content
**Countries:** World, United States, China, India, Nigeria, Japan, Brazil, Germany.

**Population, millions** (UN WPP 2024; 1990 and 2023 are estimates, 2024 on are the medium projection):
| | 1965 | 1990 | 2023 | 2024 | 2050 | 2100 |
|---|---|---|---|---|---|---|
| World | 3,334.5 | 5,327.8 | 8,091.7 | 8,162.0 | 9,664.4 | 10,180.2 |
| United States | 195.7 | 253.4 | 343.5 | 345.4 | 380.8 | 421.3 |
| China | 723.4 | 1,153.6 | 1,422.6 | 1,419.3 | 1,260.3 | 633.4 |
| India | 490.1 | 865.0 | 1,438.1 | 1,450.9 | 1,679.6 | 1,505.3 |
| Nigeria | 50.1 | 97.1 | 227.9 | 232.7 | 359.2 | 476.7 |
| Japan | 100.9 | 123.4 | 124.4 | 123.8 | 105.1 | 76.8 |
| Brazil | 83.8 | 149.1 | 211.1 | 212.0 | 217.5 | 163.4 |
| Germany | 76.0 | 79.7 | 84.5 | 84.6 | 78.3 | 70.9 |

**Fan values** (Low / High variants; 80 percent interval; 95 percent interval), 2050 then 2100:
- World 2050: 8,942.3 / 10,395.1; 9,495.0 to 9,820.1; 9,415.7 to 9,899.9. 2100: 6,986.8 / 14,395.2; 9,405.1 to
  11,034.8; 9,046.8 to 11,437.4.
- United States 2050: 353.9 / 407.9; 355.3 to 404.3; 342.1 to 420.0. 2100: 307.5 / 566.5; 315.7 to 537.1; 255.7 to
  625.2.
- China 2050: 1,173.2 / 1,347.9; 1,194.0 to 1,323.3; 1,158.6 to 1,353.6. 2100: 405.6 / 954.2; 473.9 to 799.6; 403.8
  to 890.4.
- India 2050: 1,548.0 / 1,812.4; 1,571.6 to 1,785.6; 1,510.8 to 1,847.9. 2100: 991.3 / 2,196.9; 1,114.7 to 1,943.0;
  924.3 to 2,299.0.
- Nigeria 2050: 332.5 / 386.3; 313.1 to 418.6; 293.7 to 451.6. 2100: 335.4 / 659.9; 310.4 to 845.3; 255.5 to 1,142.5.
- Japan 2050: 98.3 / 111.9; 99.5 to 111.1; 96.4 to 115.0. 2100: 53.4 / 106.4; 57.6 to 97.1; 47.8 to 112.8.
- Brazil 2050: 201.0 / 234.2; 204.3 to 229.2; 196.5 to 235.5. 2100: 106.4 / 240.3; 121.6 to 208.0; 100.7 to 236.4.
- Germany 2050: 73.2 / 83.4; 71.4 to 85.6; 68.1 to 90.1. 2100: 50.5 / 96.4; 52.7 to 94.8; 43.3 to 110.7.
Every year 2024 to 2100 for all five series is pulled at build from the same file (see Sources).

**Primary energy per person, kWh** (1965 / 1990 / 2024) and total, TWh (1990 / 2024): World 12,470 / 17,270 /
20,154 (92,013 / 164,494); United States 71,812 / 87,859 / 74,018 (22,261 / 25,568); China 2,064 / 6,667 / 31,076
(7,691 / 44,107); India 1,187 / 2,511 / 7,432 (2,172 / 10,783); Nigeria (no 1965 value) / 2,012 / 2,213 (195 / 515);
Japan 16,677 / 41,523 / 37,278 (5,124 / 4,613); Brazil 2,672 / 7,766 / 14,378 (1,158 / 3,048); Germany 38,669 /
52,539 / 33,062 (4,188 / 2,795). Primary energy counts fuels before conversion and leaves out traditional biomass
(wood, dung), which matters most for Nigeria and India; a note on those two countries says so.

**Split results 1990 to 2024** (TWh: more people / more use per person / both = total; percent of 1990 total):
- World: 48,947 / 15,362 / 8,172 = 72,481 (+53.2 / +16.7 / +8.9 = +78.8 percent)
- United States: 8,088 / -3,507 / -1,274 = 3,307 (+36.3 / -15.8 / -5.7 = +14.9)
- China: 1,772 / 28,158 / 6,486 = 36,416 (+23.0 / +366.1 / +84.3 = +473.5)
- India: 1,471 / 4,256 / 2,883 = 8,611 (+67.7 / +196.0 / +132.7 = +396.5)
- Nigeria: 273 / 20 / 27 = 319 (+139.6 / +10.0 / +13.8 = +163.5)
- Japan: 15 / -524 / -1 = -511 (+0.3 / -10.2 / -0.0 = -10.0)
- Brazil: 488 / 986 / 416 = 1,890 (+42.1 / +85.1 / +35.9 = +163.2)
- Germany: 255 / -1,552 / -94 = -1,392 (+6.1 / -37.1 / -2.2 = -33.2)
Reading lines (rule: total negative gives the "fell" line; else a negative per person strip gives the "kept rising" line;
else the largest strip names the cause): "Most of the growth came from
more people." (World, Nigeria), "Most of the growth came from more use per person." (China, India, Brazil), "Use per
person fell, but more people kept the total rising." (United States), "Use per person fell faster than people grew,
so the total fell." (Japan, Germany).

**Feed:** cereal production 2023: 3,126.27 million tonnes; uses 2023: food 1,426.9, animal feed 1,122.2, other 276.9
million tonnes (food is 45.6 percent of production). World cereal yield t/ha 1961 / 1990 / 2023: 1.353 / 2.758 /
4.228; US 2023: 8.330. Cereal land = production / yield = 739.4 million ha. Arable land per person, ha, 1990 / 2023:
0.227 / 0.172. Energy in cereal grain: 3,500 kcal per kg (rounded). Daily need: 2,100 kcal (humanitarian planning
figure). Formula: people fed = land x yield x share x 3,500 / (calories x 365).
Worked values (land 739.4): yield 4.228, all of it: 14.28 billion; food share: 6.52 billion; yield 1.353 all: 4.57
billion, food share: 2.09 billion; yield 8.330 all: 28.12 billion; 4.228 with food and feed both eaten as grain
(81.5 percent): 11.64 billion; 4.228, food share, 2,500 kcal: 5.47 billion.

## Interactions in detail
- Changing country animates the rectangles (400 ms; a tap on another chip or toggle during it jumps to the new
  state at once); the strips grow out from the 1990 rectangle in order: people,
  per person, both, so the eye follows the split. Hover or focus on a strip shows its formula with numbers
  ("(1,450.9 - 865.0) million x 2,511 kWh = 1,471 TWh").
- Values are computed live from the data table, not typed in; the build check compares each strip to Content within
  0.5 percent of that country's 1990 total (strips near zero, like Japan's people strip, differ by a few TWh with
  rounded inputs).
- Compare uses the larger of the two countries for the shared scale.
- Future: the year slider snaps to whole years; keyboard arrows step 1, Page keys step 10. Bands draw under lines;
  both bands and both variants are labeled at the right edge (no legend-only reading).
- Feed: sliders update the bar and the formula on input. The bar's axis runs 0 to 50 billion (the largest setting,
  1,000 million ha, 9.0 t/ha, all of it, 1,800 kcal, feeds 47.95 billion). When the bar passes the population line the line label
  reads "enough grain calories for everyone, if shared evenly"; below it, "not enough from grain alone". At share 0
  the bar is 0 and the line says why.
- Reset returns to World, Split, and all Feed defaults. Nothing is saved; no localStorage.
- `window.__tool`: `{mode, country, compare, split: {people, perPerson, both, total}, year, feed: {land, yield, share,
  kcal, fed}}`.

## Look
Accent `--brand #f261ce` (orchid), `--brand-ink #10161f`. Charts on `--gr-bg`; strips use `--gr-1`, `--gr-2`,
`--gr-3` each with its own pattern (dots, hatching, solid) so they read in grayscale; removed bands are `--gr-4`
outlines with cross-hatching. Fan bands `#5aa9ff` at 18 and 32 percent alpha, median `--gr-1`, variants dashed
`--muted`. Contrast (computed): brand on --panel 6.08:1, on --sec-bg 5.76:1; brand-ink on brand 6.38:1. Nearest
accent on any spec is #ff7ac8 (dE 15.9); group siblings are 37 or more apart.

## Art
none: drawn in code. Every mode is a chart of real data (area rectangles, a projection fan, a bar against a line),
and painting any of it would blur the numbers; no scene, place or object is shown.

## Voice
Bank voice `news-reader` (Rasalgethi, "Say clearly and steadily, like a trusted radio news reader"); it suits
reading numbers out. No neighbor and no other spec in this batch uses it. `Curio.voice`, `scope: () => state.mode`.
- wSplit (how; Split welcome; stale once a country chip is tapped): "Tap a country chip. The colored strips show
  where its energy growth came from."
- reading (event; country change in Split; stale on the next change): the reading line for that country (the four
  fixed lines in Content).
- wFuture (how; Future welcome; stale once the year slider or a jump button is used): "Drag the year slider, or press
  2050 or 2100. The shaded bands show how sure the UN is."
- variants (how; first time Low or High is hovered or focused; stale on mode change): "Low and High are what-ifs,
  half a child fewer or more per woman. They are not the edges of the bands."
- wFeed (how; Feed welcome; stale once a slider or chip moves): "Move the Yield and Share sliders, or tap a chip.
  Watch the bar against the line for today's people."
- crossed (event; bar crosses the line upward; stale when it drops back): "Enough grain calories for everyone, if
  shared evenly."

## Family engine
none. The Over time chart may reuse data-desk's Chart for a line chart, adding nothing to the engine.

## Sources
- Population and projections: United Nations, World Population Prospects 2024, file WPP2024_TotalPopulationBySex.csv.gz
  (https://population.un.org/wpp/downloads), variants Medium, Low, High and the probabilistic 80 and 95 percent
  intervals; pulled 2026-10-27. On screen: "UN World Population Prospects 2024".
- Energy per person and totals: Energy Institute, Statistical Review of World Energy 2026, via Our World in Data
  energy dataset (https://github.com/owid/energy-data, columns energy_per_capita and primary_energy_consumption,
  updated 2026-06-30, pulled 2026-10-27); Nigeria from the EIA extension in the same dataset. On screen: "Energy
  Institute Statistical Review 2026, data to 2024".
- Cereal yield: FAO FAOSTAT via Our World in Data (https://ourworldindata.org/grapher/cereal-yield), pulled
  2026-10-27.
- Cereal production and uses (food, feed, other): FAO Food Balances via Our World in Data
  (https://ourworldindata.org/grapher/cereal-distribution-to-uses), 2023, pulled 2026-10-27.
- Arable land per person: World Bank indicator AG.LND.ARBL.HA.PC via Our World in Data, pulled 2026-10-27.
- Grain energy: USDA FoodData Central (https://fdc.nal.usda.gov/), whole wheat, rice and corn grain about 3,400 to
  3,700 kcal per kg; 3,500 used, rounded.
- 2,100 kcal per person per day: WHO, UNHCR, IFRC and WFP (2004), Food and Nutrition Needs in Emergencies.
- Number checks (Python, 2026-10-29, scratch pop.py): every 2024 total equals population x energy per person within
  3 TWh. The three strips recomputed from the rounded table match Split results within 0.1 percent of each 1990
  total (largest gaps: US people 8,083 against 8,088; Japan people 17 against 15), so the old "within 0.5 percent of
  each value" build check would have failed on the tiny strips; it now uses the 1990 total. The reading-line rule
  gives the listed line for all eight countries. Feed: land 3,126.27 / 4.228 = 739.4 million ha; food share 45.6,
  food and feed 81.5 percent; the seven worked values reproduce (14.28, 6.52, 4.57, 2.09, 28.12, 11.64, 5.47
  billion); the bar crosses the 8.09 billion line at a 56.7 percent share with 2023 yield. 1990 to 2023: population
  +51.9, yield +53.3, arable land per person -24.2 percent.

## Done when
1. Split for India shows strips 1,471 / 4,256 / 2,883 TWh (within 0.5 percent of its 1990 total) and "Most of the
   growth came from more use per person."
2. Split for the United States draws the per person strip as a removed band and reads "Use per person fell, but more
   people kept the total rising."
3. Japan and Germany show a negative total with the "total fell" line.
4. Future for World at 2100 reads median 10,180.2, 80 percent 9,405.1 to 11,034.8, 95 percent 9,046.8 to 11,437.4,
   Low 6,986.8, High 14,395.2 (millions).
5. Show peak marks a year before 2050 for China, Japan and Germany, and for Nigeria says "still rising in 2100".
6. Feed defaults give 6.52 billion; chip All of it gives 14.28; chip 1961 with All of it gives 4.57; every slider at
   its most generous end gives 47.95 and stays on the axis.
7. Focus: at 1366x768 and 680x425 the rectangles are the biggest thing in Split, the fan in Future and the bar in
   Feed; chart text is at least 10 px in the preview.
8. A tap during the 400 ms strip animation (another country chip, or Same scale) shows the new state at once.
9. Every chart shows its "data as of" line; strips read in grayscale by pattern.
10. At 1366x768 and 375 wide, the country chips and the mode's main control are visible without scrolling.
11. Each how-to line speaks once in five actions; reading speaks on every country change.

## Open questions
- [population-dashboard] HS-ESS3-1 is taught only through the "people, yields and land" panel; its natural hazards
  and climate parts are not. Keep the code, or move it to a tool that covers hazards?
- [population-dashboard] Feed is a world-scale formula, not a simulation. Enough for HS-LS2-1 here, given
  carrying-capacity (grade 9) simulates it?
- [population-dashboard] Energy per person stands in for "footprint". Add a second resource (water or land), or keep
  one so the split stays simple?
