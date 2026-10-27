# Energy Accountant

## One idea
Keep the books for living things: every reaction is a ledger entry that must balance in carbon, hydrogen, oxygen
and nitrogen atoms and in kilojoules, so you can post a leaf's sugar, a deer's sprint and a loaf's rise and see where
every atom and every kilojoule went (a tree's wood is mostly air; a sprinting muscle with no oxygen pays 2 ATP where
it could have had about 32), and then read the same books for the whole planet in the real seasonal breathing of
CO2 at three NOAA stations.

## Not like
- equation-balancer (chem 10): students balance equations by adding molecules. Here equations arrive balanced; the
  work is posting where atoms and energy go between organisms, air, water and rock, and reading the totals.
- hand-warmer-lab (chem 10): reaction heat in a pack. Here energy is tracked as stored, captured as ATP and lost as
  heat inside living things.
- climate-dashboard (sci 9) and feedback-loop-builder (sci 9): long-term CO2, temperature and climate loops. Here only
  the one-year seasonal swing, read as photosynthesis against respiration; no trend, warming or policy.
- game-day-fuel (health): food energy for an athlete. No meals here; cells and molecules.
- body-thermostat (same group): heat leaving a body. Here the chemistry before the heat.
- which-model-wins and the data-desk tools: fitting and comparing data. Here the chart is evidence for one biology
  claim, with no fitting.

## Who and how
Grade 9, science (Life Science module Photosynthesis and Cellular Respiration: "Energy conversions and
macromolecules"). Driver: students on laptops. 20 to 40 minutes. Standards: HS-LS1-5 (photosynthesis turns light
into stored chemical energy), HS-LS1-6 (carbon, hydrogen and oxygen from sugar build amino acids and other large
molecules), HS-LS1-7 (respiration breaks and forms bonds for a net energy transfer), HS-LS2-5 (carbon cycling among
biosphere, atmosphere, hydrosphere and geosphere), HS-LS2-3 (energy and matter in aerobic and anaerobic conditions:
the Oxygen switch mode, added in the gap fill).
Topic line: photosynthesis, respiration and the carbon cycle.
9-12 dark theme. Header: title, `.seg` modes **Ledger**, **Oxygen switch**, **Planet's books**, kit buttons.

## Screens and modes
Shared: stage left (a scene drawn in code above a ledger), panel right (controls, `hint`, `tip`). The **ledger**
is a real `table.inst` with columns Entry, C, H, O, N (atoms in and out), Energy in (kJ), Stored (kJ), ATP
captured (kJ), Heat (kJ), and a totals row whose cells show a check mark and "balances" or the difference.

**Ledger** (opens first). **Scene** `.seg`: **Leaf by day**, **Leaf by night**, **Deer**, **Bread dough**,
**Soil**. Each scene offers its own entry buttons (see Content). Pressing an entry plays a 1.5 s animation (atoms as
small lettered balls moving from their source account to their destination, Motion off: instant) and posts one row.
Accounts are boxes around the scene: **Air**, **Water**, **Sugar store**, **Body (proteins, starch)**, **ATP spent on
work**, **Heat**, and in Soil also **Soil**. Each box shows its running atom counts; the C count in every box is
also a bar.
- **Where did the wood come from?** card (Leaf by day): three sliders Soil, Water, Air that must sum to 100
  (moving one rescales the others). **Check** posts one photosynthesis entry and reveals the mass ledger for one
  glucose: carbon 72 g and oxygen 96 g came from the air (CO2), hydrogen 12 g from water: 93.3 percent from air,
  6.7 percent from water, 0 from soil. The O2 given off came from the water (stated, sourced).
- **Follow one carbon** button: tags one carbon atom (accent ring) and steps through stamps with **Next stamp**:
  Air, Leaf (photosynthesis), Sugar, Deer (eats the leaf), Deer muscle (respiration), Air, Ocean (dissolves,
  becomes bicarbonate), Clam shell (calcium carbonate), Limestone (rock, millions of years), back to Air
  (volcano or weathering). Each stamp names the sphere (atmosphere, biosphere, hydrosphere, geosphere) and shows its
  balanced equation where one applies. A passport strip records the stamps.
- **Clear ledger** empties the rows and accounts.

**Oxygen switch**. A muscle cell (or a yeast cell, **Cell** `.seg` **Muscle**, **Yeast**) with an ATP demand
slider **Work** (8 to 64 ATP per tick, step 8, default 32) and the **Oxygen** switch (on). Each **Tick** button
press (or **Run** for 10 ticks) burns as much glucose as the work needs: with oxygen, 1 glucose per 32 ATP; without,
1 glucose per 2 ATP, piling up lactic acid (muscle) or ethanol and CO2 bubbles (yeast). Two side-by-side counters:
glucose used, ATP made, waste made, energy still locked in waste (kJ). The ledger rows post as in Ledger.
Readout line: "Same work, oxygen off: 16 times the glucose."

**Planet's books** (the data). A line chart (data-desk engine) of monthly CO2 in 2023 at **Utqiagvik, Alaska**,
**Mauna Loa, Hawaii** and **South Pole**, each toggled by a checkbox button. `.seg` **Raw ppm** / **Swing**
(each station minus its own trend line, see Content). A data table under the chart (`renderTable`, read-only).
Prompts (cards, no scoring): "Which months does the air lose CO2 at Utqiagvik?" / "Why is the South Pole's swing
small and flipped?" / "Which ledger entry wins in northern summer?" **Show what scientists conclude** reveals the
explanation: northern land plants photosynthesize faster than everything respires in summer, and respiration wins in
winter; the south has much less land, and its seasons are opposite. "Data as of" line: NOAA GML, downloaded
2026-10-27.

## Content
Entries (atoms per one glucose; energy per mole of glucose, from free energy):
| Entry | Equation | Energy |
|---|---|---|
| Photosynthesize | 6 CO2 + 6 H2O -> C6H12O6 + 6 O2 | 2,870 kJ of light stored in sugar |
| Respire (oxygen) | C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O | 2,870 released: about 32 ATP x 30.5 = 976 kJ captured (34 percent), 1,894 heat |
| Ferment to lactic acid | C6H12O6 -> 2 C3H6O3 | 196 released: 2 ATP = 61 kJ captured (31 percent of 196), 135 heat; 2,674 still in lactic acid |
| Ferment to ethanol (yeast) | C6H12O6 -> 2 C2H5OH + 2 CO2 | 235 released: 61 captured, 174 heat; 2,635 still in ethanol |
| Build sucrose (two sugars join) | 2 C6H12O6 -> C12H22O11 + H2O | a little energy stored in the new bond; real cells pay for it with ATP |
| Build an amino acid (alanine) | C6H12O6 + 2 NH3 -> 2 C3H7NO2 + 2 H2O | atom summary only, labeled "not one real reaction: cells use many steps" |
Scenes and their buttons: Leaf by day: Photosynthesize, Respire, Build sucrose, Build an amino acid (N from soil
nitrate shown as NH3 for the atom count, said in a note). Leaf by night: Respire, Build sucrose (Photosynthesize is
disabled with "No light"). Deer: Respire, Ferment to lactic acid (sprint), Build an amino acid. Bread dough: Ferment
to ethanol, Respire (yeast with air). Soil: decomposers Respire on dead leaves (atoms leave Body, go to Air and Soil).
Mass for one glucose: C 6 x 12 = 72 g, H 12 x 1 = 12 g, O 6 x 16 = 96 g; total 180 g; from air 168/180 = 93.3
percent. In: 6 CO2 = 264 g, 6 H2O = 108 g; out: glucose 180 g, 6 O2 = 192 g (372 g each side).
Oxygen switch numbers: Work 32 ATP per tick: oxygen on 1 glucose; off 16 glucose and 32 lactic acid. Work 8: on
0.25 glucose (shown as a quarter), off 4. Yeast off: per 32 ATP, 16 glucose, 32 ethanol, 32 CO2.
Carbon passport sphere lines (text): bicarbonate step CO2 + H2O -> HCO3- + H+; shell step Ca2+ + 2 HCO3- -> CaCO3 +
CO2 + H2O; limestone "carbon can stay locked in rock for millions of years".

CO2 data 2023, monthly means (ppm), January to December:
- Utqiagvik (BRW): 424.68, 425.55, 427.54, 427.57, 427.39, 423.62, 414.41, 409.60, 412.20, 418.97, 424.71, 427.67
- Mauna Loa (MLO): 419.48, 420.31, 420.99, 423.35, 424.00, 423.68, 421.83, 419.68, 418.50, 418.82, 420.46, 421.86
- South Pole (SPO): 415.22, 415.14, 415.08, 415.43, 415.90, 416.28, 416.67, 417.14, 417.56, 417.76, 417.88, 417.96
Annual means for the trend: BRW 2022 420.24, 2023 421.99, 2024 425.62; MLO 418.53, 421.08, 424.60; SPO 414.42,
416.50, 420.07. Swing = value minus (2023 mean + g x (month - 6.5)/12), g = (2024 mean - 2022 mean)/2 (BRW 2.69,
MLO 3.04, SPO 2.83 ppm per year). Swings (rounded to 0.1): BRW +3.9 +4.6 +6.3 +6.1 +5.7 +1.7 -7.7 -12.7 -10.4 -3.8
+1.7 +4.4 (range 19.1, lowest August); MLO -0.2 +0.4 +0.8 +2.9 +3.3 +2.7 +0.6 -1.8 -3.2 -3.1 -1.8 -0.6 (range 6.5,
highest May, lowest September); SPO +0.0 -0.3 -0.6 -0.5 -0.2 -0.1 +0.1 +0.3 +0.5 +0.4 +0.3 +0.2 (range 1.1,
lowest March, highest September).

Hints: Ledger "<b>Ledger.</b> Pick a scene and press an entry. Every atom in must show up somewhere out." /
Oxygen switch "<b>Oxygen switch.</b> Set the work, press Tick, then switch the oxygen off and tick again." /
Planet's books "<b>Planet's books.</b> Turn on a station and switch to Swing. When does the air lose CO2?"
Tips: "ATP is the cell's spending money; glucose is the savings account." / "Fermenting cells are not wasteful by
choice: without oxygen it is the only way to pay." / "Plants respire too, day and night." / "Carbon atoms are never
used up, only moved."
Model limits line: "Real cells use dozens of steps; this ledger shows only the totals. ATP numbers are about 30 to 32
in real cells; this tool uses 32."

## Interactions in detail
- Totals row recomputes after each posting; every entry is balanced, so totals always show balanced. The teaching
  moment is the accounts: the C bar in Air drops when the leaf photosynthesizes and climbs at night.
- Accounts start with a stock (Air 600 C, Water 0 C, others 0) so nothing goes negative; an entry whose inputs are
  missing (Respire with no sugar in a scene) is disabled with the reason ("No sugar to burn: photosynthesize or eat
  first"). Deer scene starts with 12 glucose of eaten leaves in Sugar store.
- The wood sliders always sum to 100 (integer percents); Check works at any setting and never scores.
- Oxygen switch: fractional glucose shown as fractions of a hexagon icon; waste piles cap their drawing at 64 icons
  with a number.
- Chart: toggling a station never rescales without animation (instant with Motion off); y axis "ppm CO2"; months on x.
- Keyboard: every entry, slider and toggle in tab order; the ledger table is real HTML.
- Mode change: `V.hush()`; ledger kept per mode until Clear ledger.

## Look
Accent `--brand #d3b069` (ledger gilt), `--brand-ink #10161f`. Stage `#121821` with faint green column rules like
ledger paper. Atom balls: C dark gray with white "C", O red, H white, N blue, all with letters (never color only).
Contrast (computed): brand on --panel 8.39:1, on --sec-bg 7.95:1; brand-ink on brand 8.81:1. Station lines use the
data-desk colors plus dash patterns. Nearest 9-12 accents #e8b54a (field-lines), #f3e3a0, #e39b6e (dE 19 to 20).

## Art
none: drawn in code (leaf, deer outline, dough bowl, soil, cells, atoms, chart).

## Voice
Bank `calm-professor` ("Say evenly and clearly, like a calm, friendly college professor"): an even accountant's
voice. Uses `Curio.voice`, scope = mode.
- welcomeLedger (how): "Welcome to Energy Accountant. Pick a scene, then press an entry. Every atom that goes in has
  to come out somewhere."
- welcomeOxygen (how): "Oxygen switch. Set the work, press Tick, then switch the oxygen off and tick again."
- welcomePlanet (how): "Planet's books. Turn on a station, then switch to Swing and look for the months the air loses
  carbon dioxide."
- woodAsk (how, when the wood card opens): "Where did the wood come from? Set the three sliders, then press Check."
- woodReveal (event, each Check; stale on scene change): "Almost all of it came from the air. The carbon and most of
  the oxygen arrived as carbon dioxide."
- oxygenOff (event, each switch off; stale if switched back on): "Oxygen off. Each glucose now pays two ATP instead
  of about thirty two."
- passport (how, first Follow one carbon): "Press Next stamp to follow one carbon atom through air, life, ocean and
  rock."
- night (how, first Leaf by night): "No light, so no photosynthesis. The leaf only respires."

## Family engine
none (not a family member). Uses data-desk parts as a consumer (`kit/data-desk.js`): `DataTable` for the 36 CO2
rows plus a computed swing column, `Chart` type `line` with `groupBy` station, `renderTable` read-only. Dataset claim
for the data-desk table: NOAA monthly CO2 2023 at BRW, MLO and SPO (seasonal use only). climate-dashboard (sci 9)
may also use NOAA CO2 for long-term trends: see Open questions.

## Sources
- NOAA GML monthly CO2: Mauna Loa https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt ; Utqiagvik and
  South Pole in-situ monthly files https://gml.noaa.gov/aftp/data/trace_gases/co2/in-situ/surface/txt/ (files
  co2_brw_surface-insitu_1_ccgg_MonthlyData.txt and co2_spo_...). Downloaded 2026-10-27; values above copied
  exactly; swings computed in Python by the formula above.
- Glucose oxidation free energy -2,870 kJ per mole (-686 kcal), about 30 or 32 ATP per glucose, ATP hydrolysis
  -30.5 kJ (-7.3 kcal) per mole, efficiency about 34 percent: Urry et al., Campbell Biology, 12th ed. (2020), ch. 9.
- Glucose to 2 lactate -196 kJ per mole; glucose to 2 ethanol + 2 CO2 -235 kJ per mole: Nelson and Cox, Lehninger
  Principles of Biochemistry, 8th ed. (2021), ch. 14 (verify checks both).
- O2 from photosynthesis comes from water: Ruben, Randall, Kamen and Hyde (1941), J. Am. Chem. Soc. 63:877;
  summarized in OpenStax Biology 2e, ch. 8 (CC BY 4.0), https://openstax.org/books/biology-2e/pages/8-introduction
- Fermentation, respiration, carbon cycle and its reservoirs, carbonate in shells and limestone: OpenStax Biology 2e,
  sections 7.5 and 46.3, https://openstax.org/books/biology-2e/pages/46-3-biogeochemical-cycles
- Seasonal CO2 cycle explained by Northern Hemisphere vegetation: NOAA Climate.gov, "Climate Change: Atmospheric
  Carbon Dioxide" https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide
- Atomic masses C 12, H 1, O 16, N 14 (rounded): NIST, https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses
- All equations atom-checked in Python (Curio Class, 2026-10-27).

## Done when
1. Every entry posts a row whose C, H, O, N totals balance; Photosynthesize moves 6 C from Air to Sugar store.
2. The wood card reveals 93.3 percent from air and 6.7 percent from water whatever the sliders say, with no score.
3. Oxygen switch at Work 32: on uses 1 glucose per tick, off uses 16 and makes 32 lactic acid; the energy-in-waste
   counter reads 2,674 kJ per glucose fermented (muscle) and 2,635 (yeast).
4. Planet's books, Swing: Utqiagvik lowest in August at -12.7, range 19.1; Mauna Loa range 6.5; South Pole range 1.1,
   lowest in March; the data-as-of line is visible.
5. Follow one carbon visits all four spheres and the passport strip lists ten stamps.
6. Leaf by night disables Photosynthesize with a reason; Respire with no sugar is disabled with a reason.
7. Main controls visible without scrolling at 1366x768 and 680x425; tables readable at 375 wide (scroll inside).
8. Each how-to line speaks once in five repeated actions; woodReveal speaks every Check.
9. No images, no network, no em dashes.

## Open questions
- [energy-accountant] climate-dashboard may also use NOAA CO2 (long-term). This tool uses only 2023 monthly at three
  stations for the seasonal swing. Fine for the two to share the source, or should one move to another station?
- [energy-accountant] The amino acid entry is an atom summary, not a real reaction (labeled on screen). OK for
  HS-LS1-6, or show a real two-step path (glucose to pyruvate, pyruvate plus ammonia to alanine)?
