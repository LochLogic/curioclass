# Biome Atlas

## One idea
Every place on Earth sits at a spot in climate space: read a real weather station's year of temperature and rain,
run it through a five-question biome key, check your prediction against the biome that really grows there (12 of 13
match, and the one miss is the lesson), then knock the land down with a fire or a clearing and watch succession
rebuild the same biome, unless you also nudge the climate, in which case it rebuilds a different one.

## Not like
- carrying-capacity (grade 9, sci-bio): one deer herd and its food in one habitat; here the unit is the whole biome
  and the driver is climate, not a population.
- reserve-designer (grade 9, sci-bio): buys land cells for species in one valley; here there is no planning, you read
  climate and predict what grows.
- tree-of-life (grade 9, sci-bio): evolution and relatedness; nothing here is about lineages.
- climate-dashboard (grade 9, sci-earth-phys): global temperature and CO2 trends over time; here every station is a
  fixed 1991 to 2020 average, and the climate sliders are "what if this place were different", not a forecast.
- water-shapes-earth (grade 9): erosion and landforms; no rainfall chemistry or landform work here.
- rain-gauge (wave 2, calculus): rainfall rate summed into a barrel; here rain totals are given, not accumulated.
- Grid Operator, Population Dashboard, Up the Watershed, Design Challenge Studio (this group): no maps of real places
  besides this one; this is the only tool in the group about living systems.

## Who and how
- Grade 12, Environmental science (Earth and Space Science), Ecosystems and Biomes. Students drive, alone or in pairs.
  25 to 40 minutes.
- Topic line: "biomes, climate and succession".
- Standards (module): HS-LS2-6 (complex interactions keep an ecosystem relatively stable when conditions hold;
  changed conditions can give a new ecosystem). Read and Key build the "conditions decide the ecosystem" half;
  Change is the evidence for both halves (same climate: the same biome comes back; new climate: a new one).
- tool.json: driver "students", minutes "25-40", modes ["Read", "Key", "Change"], grades_label "Grade 12".

## Screens and modes
Layout: map stage on the left (about 60 percent), panel on the right with the mode tabs, the station card and the
mode's buttons on top. At 760 wide and below, the map is a strip on top (station pins only) and the panel below; at
1366x768 the map, the climate chart and the mode buttons all fit without scrolling.

**Read (default).** A world map (equirectangular, drawn in code) with 13 station pins. Tap a pin or pick from the
**Station** list (keyboard users: the list comes first in tab order). The panel shows the station card (name,
country, latitude, elevation) and its climograph: 12 rain bars (mm, --gr-1) and a temperature line (°C, --gr-4 with
dots), months on the x axis Jan to Dec, except southern stations start at Jul so summer sits in the middle as it
does for northern ones (the axis then reads "Jul ... Jun").
Under it, the **Climate space** chart: annual temperature (x, -15 to 30 °C) against annual rain (y, 0 to 2,800 mm),
with every visited station as a dot. Faint guides: vertical lines at 3 °C and 20 °C, a horizontal line at 2,000 mm,
and the station's own dry line (see Content) as a dashed sloped line with the "dry" side shaded. Buttons: **Place on
chart** (animates the dot in from the climograph totals), **Show all stations** (adds all 13 dots, labeled).

**Key.** For the chosen station the five questions appear one at a time, each with the station's numbers already
filled in and the student choosing Yes or No:
1. "Is the warmest month below 10 °C?" (**Yes** / **No**)
2. "Is yearly rain below half the dry line?" then "below the dry line?"
3. "Is the yearly average 20 °C or warmer?" then "How many months get under 60 mm?" (number chips 0 to 12)
4. "Is the driest summer month under 40 mm and under a third of the wettest winter month?" then "2,000 mm or more?"
5. "Is the yearly average 3 °C or warmer?"
Each answer shows the comparison in numbers ("558.9 mm is more than 546.0 mm"). A wrong Yes/No is not blocked: the
key follows the student's answer, and **Check my answers** at the end flags any step where the numbers say otherwise.
The key ends in a predicted biome. **Reveal** shows the real biome (from the ecoregion map) beside the prediction as
two scene cards, with "Match" or "Miss". A miss opens a short "Why the key missed" note. **Next station** moves on;
a tally "Predicted right: n of m" sits under the map. The map gets a **Layer** toggle: **My predictions** /
**Real biomes** (pin fill = biome color plus a letter code, so color is never alone).

**Change.** Pick a station whose key is done. The stage swaps the map for a side-view landscape drawn in code
(ground line, layers of grass, shrubs, young trees, tall trees, drawn per biome stage). Controls:
- **Fire** or **Clearing** (one per biome, see Content): knocks the scene to stage 0.
- **Years after** slider, 0 to 200 (step 1; tick marks at the stage times), with **Play** (about 8 s to 200 years) and
  **Pause**.
- **Warmer or cooler** slider, -4 to +6 °C (step 0.5) and **Wetter or drier** slider, -50 to +50 percent (step 5).
  Both shift all 12 months. Moving them re-runs the key live; the climate dot moves in the small Climate space inset
  and a line says "Key now says: Dry grassland or savanna".
- **Reset climate**.
If the sliders are at 0, the stages lead back to the station's real biome. If the key now gives a different biome,
the late stages blend into the new biome's stages, and the last stage reads "would take decades to centuries, and
might stall: seeds, soils and fire decide the path". The model note under the stage says what it leaves out.

## Content
**Stations** (WMO 1991 to 2020 normals; lat, lon, elevation m; monthly mean temperature °C Jan to Dec; monthly rain mm
Jan to Dec). T = mean of the 12 months, P = sum of the 12 months (both shown to one decimal).
- Manaus, Brazil (-3.103, -60.016, 61): T 26.6 26.6 26.6 26.7 27.0 27.3 27.5 28.2 28.6 28.5 28.0 27.2; P 305.6 296.8
  320.9 331.0 233.3 117.2 67.1 56.1 79.0 113.9 188.0 253.5. T 27.4, P 2,362.4.
- Kumasi, Ghana (6.717, -1.600, 286): T 27.4 28.8 28.5 28.0 27.5 26.3 25.3 24.9 25.8 26.6 27.4 27.3; P 24.8 49.0 109.9
  163.6 174.0 227.3 125.6 68.8 175.1 175.6 50.1 27.6. T 27.0, P 1,371.4.
- Kasama, Zambia (-10.217, 31.133, 1,384): T 21.8 21.8 22.0 21.3 19.9 18.1 17.6 19.8 22.5 24.0 23.6 22.3; P 254.4 248.1
  238.9 67.0 2.6 0.0 0.0 0.2 2.3 35.5 101.5 261.4. T 21.2, P 1,211.9.
- Niamey, Niger (13.483, 2.167, 222): T 24.6 27.8 31.9 34.7 34.5 32.2 29.5 28.1 29.6 31.5 29.0 25.5; P 0.0 0.3 0.2 9.8
  25.3 78.6 145.6 192.6 85.1 16.7 0.0 0.0. T 29.9, P 554.2.
- Phoenix, United States (33.428, -112.004, 337): T 13.8 15.5 19.0 22.9 27.8 33.0 35.3 34.6 31.8 25.2 18.4 13.2; P 22.1
  22.1 21.0 5.7 3.2 0.6 23.0 23.6 14.6 14.3 14.6 18.7. T 24.2, P 183.5.
- Ulaanbaatar, Mongolia (47.918, 106.848, 1,303): T -21.3 -16.2 -6.7 3.0 10.3 16.6 19.0 16.6 10.0 0.9 -10.6 -19.0;
  P 2.1 2.8 4.6 8.4 21.7 47.2 74.5 65.4 27.9 8.6 6.3 3.5. T 0.2, P 273.0.
- Dodge City, United States (37.761, -99.968, 789): T 0.5 2.3 7.5 12.4 18.2 23.9 26.7 25.6 21.1 13.8 6.5 1.1; P 15.2
  15.6 34.4 50.4 76.0 83.6 78.2 75.8 33.4 51.4 20.4 24.5. T 13.3, P 558.9.
- Berlin-Tempelhof, Germany (52.467, 13.402, 48): T 1.2 2.1 5.2 10.3 14.7 18.0 20.2 19.7 15.2 10.2 5.4 2.2; P 47.7
  36.0 40.5 29.3 52.3 58.2 71.7 58.1 46.6 43.9 41.7 44.2. T 10.4, P 570.2.
- Quillayute, United States (47.938, -124.555, 56): T 5.4 5.6 6.6 8.3 10.9 13.0 15.2 15.6 13.9 10.3 7.0 5.0; P 396.1
  247.0 299.1 205.9 107.9 83.8 40.2 67.2 115.8 271.3 387.5 351.6. T 9.7, P 2,573.4.
- Perth Airport, Australia (-31.927, 115.976, 15): T 24.9 25.0 23.1 19.8 16.4 14.2 13.3 13.7 14.8 17.2 20.2 22.9;
  P 15.8 16.6 17.9 30.7 81.4 123.9 139.6 122.1 78.9 33.6 28.7 9.6. T 18.8, P 698.8.
- Yakutsk, Russia (62.017, 129.717, 98): T -36.9 -32.9 -19.1 -3.7 8.0 17.0 19.9 15.6 6.4 -6.9 -25.9 -37.0; P 9.7 8.5
  6.3 7.9 20.1 29.5 40.1 37.1 29.6 18.6 16.9 8.5. T -8.0, P 232.8.
- Utqiagvik (Barrow), United States (71.283, -156.781, 9): T -24.2 -24.4 -23.6 -15.5 -5.2 2.2 5.4 4.3 0.9 -6.0 -14.6
  -21.3; P 3.7 5.4 4.5 4.5 7.2 10.9 24.8 27.6 19.7 13.8 9.3 5.7. T -10.2, P 137.1.
- Kredarica, Slovenia (46.379, 13.854, 2,513, a mountain station in the Julian Alps): T -7.0 -7.9 -5.9 -3.1 1.1 5.0
  7.2 7.5 3.5 0.9 -3.0 -6.2; P 89.1 96.1 120.8 141.1 162.5 206.2 217.8 205.8 235.6 236.4 215.8 131.3. T -0.7, P 2,058.5.

**The key** (thresholds from the Koppen-Geiger system as given by Peel et al. 2007; biome names after Whittaker).
Summer half = Apr to Sep north of the equator, Oct to Mar south. Dry line D (mm) = 20T + 280 if 70 percent or more of
the rain falls in the summer half, 20T if 70 percent or more falls in the winter half, else 20T + 140.
1. Warmest month under 10 °C: **Tundra**.
2. P under D/2: **Desert**. P under D: **Dry grassland or savanna**.
3. T 20 °C or more: months under 60 mm 0 to 2: **Tropical rainforest**; 3 to 4: **Tropical seasonal forest**; 5 or
   more: **Tropical savanna**.
4. Driest summer month under 40 mm and under a third of the wettest winter month: **Mediterranean shrubland**. Else P
   2,000 mm or more: **Temperate rainforest**.
5. T 3 °C or more: **Temperate deciduous forest**. Else: **Boreal forest**.

**Worked key per station** (summer share, D, result; real biome from WWF ecoregions):
- Manaus: 63 percent, D 688.0, 1 dry month: Tropical rainforest. Real: tropical moist broadleaf forest. Match.
- Kumasi: 68, D 679.7, 4 dry months: Tropical seasonal forest. Real: Eastern Guinean forests (moist, partly
  leaf-shedding). Match.
- Kasama: 94 (Oct to Mar), D 704.5, 6 dry months: Tropical savanna. Real: Central Zambezian miombo woodland. Match.
- Niamey: 97, D 878.2, P 554.2 is between 439.1 and 878.2: Dry grassland or savanna. Real: Sahelian acacia savanna.
  Match.
- Phoenix: 39, D 624.2, P under 312.1: Desert. Real: Sonoran desert. Match.
- Ulaanbaatar: 90, D 284.3, P 273.0 between 142.2 and 284.3: Dry grassland or savanna. Real: forest steppe
  (temperate grassland). Match.
- Dodge City: 71, D 546.0, P 558.9 is just over D; driest summer month Sep 33.4 is not under 51.4/3 = 17.1; T 13.3:
  Temperate deciduous forest. Real: shortgrass and mixed prairie. **Miss.**
- Berlin: 55, D 347.3, driest summer Apr 29.3 not under 47.7/3 = 15.9: Temperate deciduous forest. Real: Central
  European mixed forests. Match.
- Quillayute: 24 (so 76 percent in winter), D 194.7, driest summer Jul 40.2 is not under 40, P 2,573.4: Temperate
  rainforest. Real: Pacific coastal conifer rainforest. Match.
- Perth: 17, D 375.8, driest summer Dec 9.6 under 139.6/3 = 46.5: Mediterranean shrubland. Real: Mediterranean forest,
  woodland and scrub. Match.
- Yakutsk: 71, D 120.8, P 232.8 over D, T -8.0: Boreal forest. Real: East Siberian taiga. Match.
- Utqiagvik (warmest 5.4) and Kredarica (warmest 7.5): Tundra. Real: Arctic coastal tundra; above the tree line in
  the Alps (alpine tundra). Match.
"Why the key missed" (Dodge City): "Dodge City gets just enough rain on average for trees, but the key uses averages.
Dry years, big summer storms that run off, hot winds, fire and grazing all favor grass. Before farms, prairie fires
kept trees to the creek banks. A key built on two numbers draws a sharp line where nature has a wide edge."

**Biome colors and codes** (pin fill, letter and scene card): Tundra T `#c9d6e3`; Boreal forest B `#2f7d6b`;
Temperate deciduous forest D `#8bbf5a`; Temperate rainforest R `#1f8a4c`; Mediterranean shrubland M `#c9a65a`; Dry
grassland or savanna G `#d9c27a`; Desert X `#e3a46f`; Tropical savanna S `#b8b04a`; Tropical seasonal forest F
`#5fae3c`; Tropical rainforest W `#2a9d3a`. Letters in `#10161f` on the fill.

**Succession stages** (years after the event, stage name, what is drawn). Times are rounded and approximate.
- Tropical rainforest (Clearing): 0 bare soil and stumps; 1 grasses, vines and ferns; 3 fast pioneer trees
  (umbrella-crowned, like Cecropia); 20 young mixed forest, closed canopy; 60 tall mixed forest; 120 old-growth
  structure, though the full species mix can take centuries.
- Tropical seasonal forest (Clearing): same stages as rainforest, with a note "dry seasons bring fire risk to young
  regrowth".
- Tropical savanna (Fire): 0 black ground with tree trunks standing; 0.2 green grass shoots; 1 full grass; 3 trees
  resprouted from roots; label "fire every few years is part of how this biome stays itself".
- Dry grassland or savanna (Fire): 0 burned ground; 0.3 grass shoots from living roots; 1 grass cover; 5 full
  grassland.
- Desert (Clearing, as by off-road tracks): 0 scraped soil; 5 a few short-lived annuals after rain; 30 scattered
  shrubs; 100 shrubs nearly back; note "desert soil crusts and shrubs can take a century or more".
- Mediterranean shrubland (Fire): 0 ash; 1 resprouting shrubs and seedlings; 5 knee-high shrubs; 15 dense shrubland.
- Temperate deciduous forest (Clearing, an abandoned field): 0 bare field; 1 annual weeds; 3 grasses and perennials;
  15 shrubs and pine seedlings; 40 pine and young hardwoods; 100 oak and hickory forest.
- Temperate rainforest (Clearing): 0 stumps; 3 shrubs and alder; 30 young Douglas-fir; 100 tall conifers; 200
  old-growth with hemlock and cedar.
- Boreal forest (Fire): 0 burned trunks; 1 fireweed and grasses; 10 birch, aspen and larch saplings; 50 young conifer
  stand; 120 mature taiga.
- Tundra (Clearing, as by vehicle tracks): 0 scarred ground; 10 sedges and grasses colonize the tracks; 50 most cover
  back; note "tracks in tundra can stay visible for decades".
Change-mode notes: "Fire" is offered for savanna, grassland, Mediterranean and boreal; "Clearing" for the rest.
Model note (always visible, small): "This model uses only yearly temperature, yearly rain and its timing. It leaves out
soil, slope, fire habits, grazing, seasons of frost and how fast seeds arrive. Real biome edges are wide."

**What-if checks** (key results the sliders must give): Dodge City -15 percent rain: Dry grassland or savanna (P 475.1
under D 546.0). Dodge City +2 °C: Dry grassland or savanna (D 586.0). Berlin -50 percent: Dry grassland or savanna
(P 285.1 under 347.3). Kumasi -30 percent: Tropical savanna (5 dry months). Manaus -40 percent: Tropical seasonal
forest (3 dry months). Niamey -40 percent: Desert (332.5 under 439.1). Kasama -3 °C: Temperate deciduous forest
(T 18.2). Kredarica +3 °C: Temperate rainforest (warmest 10.5, P over 2,000). Utqiagvik +4 °C: still Tundra (warmest
9.4).

## Interactions in detail
- Pins are 24 px targets (32 px on touch) with labels on hover and focus; arrow keys move between pins in list order.
- The climograph redraws with a 300 ms ease when the station changes; the rain axis is fixed at 0 to 400 mm so
  stations compare by eye, and a note shows when a bar is clipped (none in this set reach 400).
- The Key never hides the numbers. A chip answer for "months under 60 mm" that differs from the real count is
  accepted and flagged at **Check my answers** ("Kumasi has 4 months under 60 mm: Jan, Feb, Nov, Dec").
- Tally counts only stations keyed with every step right; a station can be re-keyed (**Key again**).
- Change sliders re-run the key on every input event (cheap). The stage blends between stage drawings over 0.5 s as
  the Years slider passes each stage time. Dragging Years backward rewinds. At 200 years the slider stops.
- A biome change in Change mode shows both scene cards: "Was" and "Key now says".
- Reset (kit button) clears the tally, the keyed set and sliders. Progress (keyed stations, tally) saves in
  localStorage under `biome-atlas`; **Clear my progress** in the panel footer wipes it.
- No network: the map outline, station data and stage drawings ship with the tool.
- `window.__tool`: `{mode, station, keyResult, tally, years, dT, dP}` for tests.

## Look
Accent `--brand #5cbf2a` (leaf green), `--brand-ink #10161f`. Map ocean `#0f1a26`, land `#1d2a33` with coast line
`#3a4a5a`; pins in biome colors with a 2 px `#e8edf3` ring when selected. Climograph on `--gr-bg`. Change stage: sky
`#16202c` to `#223042`, ground `#2b2a22`, plant layers in the biome's color family. Contrast (computed): brand on
--panel 7.37:1, on --sec-bg 6.98:1; brand-ink on brand 7.73:1. Nearest accent on any spec is #9be564
(compound-interest, dE 18.6); in this group the closest is Design Challenge Studio's #00f28d (dE 34.2).

## Art
Ten biome scene cards (FLUX via cfart.py), all 16:9, no cutout, people: false, shown as the Match/Miss cards in Key
and the "Was / Key now says" pair in Change, about 480 px wide:
- tundra: "Low arctic tundra plain in summer, mosses, sedges and small flowers, pale sky, wide view, natural light"
- boreal: "Larch and spruce taiga on flat land in late summer, tall straight trees, mossy floor, soft light"
- deciduous: "Temperate oak and hickory forest in summer, tall broadleaf trees, sunlight through leaves"
- temperate-rain: "Pacific coast temperate rainforest, giant conifers, ferns and moss-covered logs, misty light"
- mediterranean: "Mediterranean shrubland on a sunny hillside, dense evergreen shrubs and a few small trees, dry summer"
- dry-grass: "Dry shortgrass steppe under a big sky, low grasses, distant low hills, late afternoon light"
- desert: "Sonoran desert with saguaro cactus, creosote shrubs and rocky ground, clear blue sky"
- trop-savanna: "Miombo woodland savanna, scattered trees above tall golden grass, dry season light"
- trop-seasonal: "West African semi-deciduous tropical forest, tall trees, some bare crowns in the dry season"
- trop-rain: "Amazon rainforest seen from a river bank, layered green canopy, warm humid light"
Map and succession stages: drawn in code.

## Voice
Bank voice `curious-librarian` (Aoede, "curiously and warmly, like a friendly school librarian"). Not used by any
wave 3 sibling; this group's other tools use news-reader, firm-captain, casual-peer and easy-coach.
- wRead (how, Read welcome): "Tap a pin on the map to open its climate chart. Then press Place on chart."
- wKey (how, Key welcome): "Answer each question with Yes or No. The numbers are right there. Then press Reveal."
- match (event, Reveal shows a match; stale on station change): "Your key matches the real biome."
- miss (event, Reveal shows a miss; stale on station change): "A miss. Open Why the key missed to see what averages hide."
- wChange (how, Change welcome): "Press Fire or Clearing, then press Play and watch the land grow back."
- shifted (event, the key result changes while a slider moves; stale when it changes back): "The key now predicts a
  different biome. Press Play to watch the new path."
- sameBack (event, Years reaches the last stage with sliders at zero; stale on Reset): "Same climate, same biome. It
  came back."

## Family engine
none.

## Sources
- Station normals: WMO climate normals 1991 to 2020, NOAA NCEI archive accession 0253808, files
  wmo_normals_9120_TAVG.csv and wmo_normals_9120_PRCP.csv
  (https://www.ncei.noaa.gov/data/oceans/archive/arc0216/0253808/6.6/data/0-data/data-composite-primary-parameters/),
  pulled 2026-10-27. On screen: "Climate normals 1991 to 2020 (WMO, via NOAA NCEI)".
- Key thresholds: Peel, Finlayson and McMahon (2007), "Updated world map of the Koppen-Geiger climate
  classification", Hydrology and Earth System Sciences 11: 1633 to 1644.
- Biome names: Whittaker, R. H. (1975), Communities and Ecosystems, 2nd ed., Macmillan.
- Real biomes: Olson et al. (2001), "Terrestrial ecoregions of the world", BioScience 51(11): 933 to 938 (WWF
  ecoregions). Each station's ecoregion is confirmed at build by a point lookup.
- Map outline: Natural Earth 110m land via world-atlas 2.0.2 (https://github.com/topojson/world-atlas), public domain.
- Old-field succession to oak and hickory: OpenStax Biology 2e (2018), section 45.6 "Community Ecology".
- Tropical forest recovery times: Poorter et al. (2021), "Multidimensional tropical forest recovery", Science 374:
  1370 to 1376.
- Savanna and fire: Bond and Keeley (2005), "Fire as a global herbivore", Trends in Ecology and Evolution 20: 387 to
  394.
- Desert recovery: Lovich and Bainbridge (1999), "Anthropogenic degradation of the southern California desert
  ecosystem and prospects for natural recovery and restoration", Environmental Management 24: 309 to 326.
- Mediterranean shrubland fire recovery: Keeley et al. (2012), Fire in Mediterranean Ecosystems, Cambridge University
  Press.
- Pacific Northwest forest development: Franklin et al. (2002), Forest Ecology and Management 155: 399 to 423.
- Boreal fire and regrowth: Johnstone et al. (2010), Canadian Journal of Forest Research 40: 1302 to 1312.
- Tundra disturbance: Forbes, Ebersole and Strandberg (2001), Conservation Biology 15: 954 to 969.

## Done when
1. Every station's climograph and T, P match the Content values; Kasama's axis starts at Jul.
2. Keying all 13 stations with correct answers gives exactly 12 matches and 1 miss (Dodge City), tally "12 of 13".
3. Dodge City's dry line reads 546.0 mm and the step says "558.9 mm is more than 546.0 mm".
4. Kumasi's dry-month count is 4 and its result Tropical seasonal forest; Quillayute's driest summer month 40.2 is
   not under 40 and the result is Temperate rainforest.
5. In Change, every What-if check in Content gives the stated key result.
6. With sliders at 0, Clearing at Berlin and Years at 200 ends on the oak and hickory stage; with -50 percent rain the
   last stage is Dry grassland or savanna with the "might stall" line.
7. Layer toggle shows biome letters as well as colors on every pin.
8. At 1366x768 and 375 wide the mode buttons, station list and climograph are visible without scrolling the panel.
9. Each how-to line is spoken once in a run of five actions; match/miss lines speak every time.

## Open questions
- [biome-atlas] Dodge City is the only miss, kept on purpose as the lesson about averages. OK, or add a second miss?
- [biome-atlas] The tool teaches only HS-LS2-6; the climate key is the way in. Enough, or should the module add a
  climate standard (HS-ESS2-4 sits with climate-dashboard)?
- [biome-atlas] Succession stage times are rounded from several papers and labeled approximate. Is that precise enough?
