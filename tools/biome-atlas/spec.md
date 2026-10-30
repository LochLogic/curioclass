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
Layout: stage on the left (about 62 percent), panel on the right with the mode tabs, the station card and the mode's
buttons on top. At 760 wide and below the stage is on top and the panel below; at 1366x768 the stage, the mode
buttons and the panel's main control fit without scrolling. Every mode has one focus, the biggest thing in the
middle of the stage.

**Read (default).** Focus: the station's climograph. The stage holds a world map strip across the top (about a third
of the stage height; equirectangular, drawn in code, a data map) with 13 station pins, and under it the climograph,
large: 12 rain bars (mm, --gr-1) and a temperature line (°C, --gr-4 with dots), months on the x axis Jan to Dec,
except southern stations start at Jul so summer sits in the middle as it does for northern ones (the axis then reads
"Jul ... Jun"). Tap a pin or pick from the **Station** list in the panel (keyboard users: the list comes first in tab
order). The panel shows the station card (name, country, latitude, elevation, T and P) and the small **Climate space**
chart: annual temperature (x, -15 to 30 °C) against annual rain (y, 0 to 2,800 mm), with every visited station as a
dot. Faint guides: vertical lines at 3 °C and 20 °C, a horizontal line at 2,000 mm, and the station's own dry line
(see Content) as a dashed sloped line with the "dry" side shaded. Buttons: **Place on chart** (animates the dot from
the climograph totals into Climate space, 600 ms), **Show all stations** (adds all 13 dots, labeled).

**Key.** Focus: the current question card, centered on the stage, with the station's climograph shrunk beside it and
the months the question is about outlined. For the chosen station the five questions appear one at a time, each
with the station's numbers already filled in and the student choosing **Yes** or **No** (or a number chip):
1. "Is the warmest month below 10 °C?" (**Yes** / **No**)
2. "Is yearly rain below half the dry line?" then "below the dry line?"
3. "Is the yearly average 20 °C or warmer?" then "How many months get under 60 mm?" (number chips 0 to 12)
4. "Is the yearly average 3 °C or warmer, and is the driest summer month under 40 mm and under a third of the
   wettest winter month?" then "2,000 mm or more?"
5. "Is the yearly average 3 °C or warmer?"
Each answer shows the comparison in numbers ("558.9 mm is more than 546.0 mm"). A wrong answer is not blocked: the
key follows the student's answer, and **Check my answers** at the end flags any step where the numbers say otherwise.
The key ends in a predicted biome. **Reveal** (live once the key ends) puts the predicted and the real biome (from
the ecoregion map) side by side as two painted scene cards filling the stage, with "Match" or "Miss". A miss opens a
short "Why the key missed" note under the cards. **Next station** moves on; a tally "Predicted right: n of m" sits
in the panel. **Key again** re-keys the station. The map strip gets a **Layer** toggle: **My predictions** / **Real
biomes** (pin fill = biome color plus a letter code, so color is never alone).

**Change.** Focus: the painted landscape, filling the stage. Pick a station from the Station list. If its key is not
done yet, the stage shows only the sky and ground band with "Key this station first" and a **Go to Key**
button (no picture, so the answer stays hidden), and Fire, Clearing and Play are disabled. For a keyed station the stage shows a side view of the land built
from painted cutout layers (Art: the succession kit) over a code sky and ground band: the biome's last stage at
first. Controls:
- **Fire** or **Clearing** (one per biome, see Content): knocks the scene to stage 0 at once.
- **Years after** slider, 0 to the biome's span (Content), 200 steps; tick marks at the stage times. **Play** runs it
  to the end in about 8 s whatever the span (from 0 if it is already at the end); **Pause**.
- **Warmer or cooler** slider, -4 to +6 °C (step 0.5) and **Wetter or drier** slider, -50 to +50 percent (step 5).
  Both shift all 12 months. Moving them re-runs the key live; the climate dot moves in the small Climate space inset
  in the panel and a line says "Key now says: Dry grassland or savanna".
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
4. T 3 °C or more, and the driest summer month under 40 mm and under a third of the wettest winter month:
   **Mediterranean shrubland**. Else P 2,000 mm or more: **Temperate rainforest**.
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

**Biome colors and codes** (pin fill, letter and scene card): Tundra T `#c9d6e3`; Boreal forest B `#3b9a83`;
Temperate deciduous forest D `#8bbf5a`; Temperate rainforest R `#46b574`; Mediterranean shrubland M `#c9a65a`; Dry
grassland or savanna G `#d9c27a`; Desert X `#e3a46f`; Tropical savanna S `#b8b04a`; Tropical seasonal forest F
`#5fae3c`; Tropical rainforest W `#2a9d3a`. Letters in `#10161f` on the fill.

**Succession stages** (years after the event: what is shown [kit pieces from Art with their height multiplier]; a
ground strip fades as the next stage arrives). Times are rounded and approximate. Span = the end of the Years slider.
- Tropical rainforest (Clearing, span 200): 0 bare soil and stumps [bare-soil]; 1 grasses, vines and ferns
  [tropical-understory x0.6]; 3 fast pioneer trees, umbrella-crowned, like Cecropia [understory x1, cecropia x0.6];
  20 young mixed forest, closed canopy [cecropia x1, tropical-canopy x0.6]; 60 tall mixed forest [tropical-canopy
  x0.85, understory x1]; 120 old-growth structure, though the full species mix can take centuries [tropical-canopy
  x1, understory x1].
- Tropical seasonal forest (Clearing, span 200): same stages and layers as rainforest, with a note "dry seasons bring
  fire risk to young regrowth".
- Tropical savanna (Fire, span 5): 0 black ground with tree trunks standing [burned]; 0.2 green grass shoots
  [green-grass x0.4]; 1 full grass [golden-grass x1]; 3 trees resprouted from roots [golden-grass x1, savanna-trees
  x0.8]; label "fire every few years is part of how this biome stays itself".
- Dry grassland or savanna (Fire, span 8): 0 burned ground [burned]; 0.3 grass shoots from living roots [green-grass
  x0.4]; 1 grass cover [golden-grass x0.7]; 5 full grassland [golden-grass x1].
- Desert (Clearing, as by off-road tracks, span 150): 0 scraped soil [scarred]; 5 a few short-lived annuals after
  rain [scarred at half, desert-annuals x0.6]; 30 scattered shrubs [desert-shrubs x0.5]; 100 shrubs nearly back
  [desert-shrubs x0.9, desert-annuals x0.6]; note "desert soil crusts and shrubs can take a century or more".
- Mediterranean shrubland (Fire, span 25): 0 ash [burned]; 1 resprouting shrubs and seedlings [evergreen-shrubs
  x0.3]; 5 knee-high shrubs [x0.6]; 15 dense shrubland [x1].
- Temperate deciduous forest (Clearing, an abandoned field, span 150): 0 bare field [bare-soil]; 1 annual weeds
  [green-grass x0.5]; 3 grasses and perennials [green-grass x1]; 15 shrubs and pine seedlings [green-grass x1,
  leafy-shrubs x0.7, pines x0.3]; 40 pine and young hardwoods [pines x0.7, oak-hickory x0.5]; 100 oak and hickory
  forest [oak-hickory x1, leafy-shrubs x0.5].
- Temperate rainforest (Clearing, span 200): 0 stumps [bare-soil]; 3 shrubs and alder [leafy-shrubs x0.8]; 30 young
  Douglas-fir [leafy-shrubs x0.8, douglas-fir x0.5]; 100 tall conifers [douglas-fir x1]; 200 old-growth with hemlock
  and cedar [douglas-fir x1, cedar-hemlock x1].
- Boreal forest (Fire, span 150): 0 burned trunks [burned]; 1 fireweed and grasses [green-grass x0.6]; 10 birch,
  aspen and larch saplings [birch-aspen x0.5]; 50 young conifer stand [birch-aspen x0.8, spruce-larch x0.6]; 120
  mature taiga [spruce-larch x1].
- Tundra (Clearing, as by vehicle tracks, span 80): 0 scarred ground [scarred]; 10 sedges and grasses colonize the
  tracks [scarred at half, sedge-moss x0.5]; 50 most cover back [scarred at a fifth, sedge-moss x1]; note "tracks in
  tundra can stay visible for decades".
When a climate shift changes the biome, the span is the larger of the two biomes' spans.
Change-mode notes: "Fire" is offered for savanna, grassland, Mediterranean and boreal; "Clearing" for the rest.
Model note (always visible, small): "This model uses only yearly temperature, yearly rain and its timing. It leaves out
soil, slope, fire habits, grazing, seasons of frost and how fast seeds arrive. Real biome edges are wide."

**What-if checks** (key results the sliders must give): Dodge City -15 percent rain: Dry grassland or savanna (P 475.1
under D 546.0). Dodge City +2 °C: Dry grassland or savanna (D 586.0). Berlin -50 percent: Dry grassland or savanna
(P 285.1 under 347.3). Kumasi -30 percent: Tropical savanna (5 dry months). Manaus -40 percent: Tropical seasonal
forest (3 dry months). Niamey -40 percent: Desert (332.5 under 439.1). Kasama -3 °C: Temperate deciduous forest
(T 18.2). Kredarica +3 °C: Temperate rainforest (warmest 10.5, P over 2,000). Utqiagvik +4 °C: still Tundra (warmest
9.4). Utqiagvik +6 °C: Boreal forest (warmest 11.4; T -4.2 is under 3, so not Mediterranean). Quillayute -5
percent: Mediterranean shrubland (driest summer month 38.2 is under 40 and under 125.4).

## Interactions in detail
- Pins are 24 px targets (32 px on touch) with labels on hover and focus; arrow keys move between pins in list order.
- The climograph redraws with a 300 ms ease when the station changes (a tap during the ease jumps straight to the
  new station); the rain axis is fixed at 0 to 400 mm so stations compare by eye, and a note shows when a bar is clipped (none in this set reach 400).
- The Key never hides the numbers. A chip answer for "months under 60 mm" that differs from the real count is
  accepted and flagged at **Check my answers** ("Kumasi has 4 months under 60 mm: Jan, Feb, Nov, Dec").
- Tally counts only stations keyed with every step right; a station can be re-keyed (**Key again**).
- Change sliders re-run the key on every input event (cheap). The stage cross-fades and rescales the layers over
  0.5 s as the Years slider passes each stage time. Dragging Years backward rewinds. At the span the slider stops.
- While Play runs every control stays live: dragging Years pauses at once and shows that year; Fire or Clearing
  restarts at year 0 at once; the climate sliders re-key and redraw in the same frame and Play keeps going.
- A biome change in Change mode shows both scene cards: "Was" and "Key now says".
- Reset (kit button) clears the tally, the keyed set and sliders. Progress (keyed stations, tally) saves in
  localStorage under `biome-atlas`; **Clear my progress** in the panel footer wipes it.
- No network: the map outline, station data and all 30 images ship with the tool.
- `window.__tool`: `{mode, station, keyResult, tally, years, dT, dP}` for tests.

## Look
Accent `--brand #5cbf2a` (leaf green), `--brand-ink #10161f`. Map strip ocean `#0f1a26`, land `#1d2a33` with coast
line `#3a4a5a`; pins in biome colors with a 2 px `#e8edf3` ring when selected. Climograph on `--gr-bg`. Change stage:
code sky `#16202c` to `#223042` (night blue so the painted layers carry the color), code ground band `#2b2a22`, the
painted layers on top. Scene cards sit on `--sec-bg` with a 1 px `--line` border. Contrast (computed): brand on
--panel 7.37:1, on --sec-bg 6.98:1; brand-ink on brand 7.73:1. Pin letters `#10161f` pass AA on every biome fill
(lowest: boreal `#3b9a83` 5.31:1, then tropical rainforest `#2a9d3a` 5.17:1). Nearest accent on any spec is #9be564
(compound-interest, dE 18.6); in this group the closest is Design Challenge Studio's #00f28d (dE 34.2).

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 30 images: 10 scene cards and a 20-piece succession kit.
Prompts say only what is in the picture.

Scene cards: 16:9; cutout no; people no; shown as the Match/Miss pair in Key (each about half the stage), the
"Was / Key now says" pair in Change.
- ba-tundra: low arctic tundra plain in summer, mosses, sedges and small flowers, pale sky, wide view, natural light
- ba-boreal: larch and spruce taiga on flat land in late summer, tall straight trees, mossy floor, soft light
- ba-deciduous: temperate oak and hickory forest in summer, tall broadleaf trees, sunlight through leaves
- ba-temperate-rain: Pacific coast temperate rainforest, giant conifers, ferns and moss-covered logs, misty light
- ba-mediterranean: Mediterranean shrubland on a sunny hillside, dense evergreen shrubs and a few small trees, dry
  summer
- ba-dry-grass: dry shortgrass steppe under a big sky, low grasses, distant low hills, late afternoon light
- ba-desert: Sonoran desert with saguaro cactus, creosote shrubs and rocky ground, clear blue sky
- ba-trop-savanna: miombo woodland savanna, scattered trees above tall golden grass, dry season light
- ba-trop-seasonal: West African semi-deciduous tropical forest, tall trees, some bare crowns in the dry season
- ba-trop-rain: Amazon rainforest seen from a river bank, layered green canopy, warm humid light

Succession kit (the Change stage): one shared prompt, "a single row of <piece> spread evenly across the whole width,
side view, painted natural history illustration, soft daylight, on a plain flat light grey background"; 4:1; cutout
yes (background removed); people no. Pieces, with their full height as a share of the stage height:
- grounds (0.25, sitting on the ground band): ba-k-bare-soil (bare brown plowed soil with a few cut tree stumps);
  ba-k-burned (black burned ground with ash and a few charred standing trunks); ba-k-scarred (pale scraped soil with
  deep tire ruts)
- low (0.15): ba-k-green-grass (low green grasses and weeds with pink fireweed spikes and small white flowers);
  ba-k-golden-grass (tall golden savanna grass); ba-k-sedge-moss (tundra sedges, mosses and tiny flowers in a low
  mat); ba-k-desert-annuals (small yellow and purple desert wildflowers on sand)
- middle (0.3): ba-k-tropical-understory (tropical ferns, vines and broad-leaved seedlings); ba-k-evergreen-shrubs
  (dense rounded Mediterranean evergreen shrubs); ba-k-leafy-shrubs (green leafy shrubs and young alder);
  ba-k-desert-shrubs (creosote bushes with one saguaro cactus)
- small trees (0.5): ba-k-cecropia (umbrella-crowned Cecropia pioneer trees); ba-k-savanna-trees (scattered
  flat-topped miombo trees); ba-k-birch-aspen (young white birch, aspen and larch); ba-k-pines (young pine trees)
- tall trees (0.85): ba-k-tropical-canopy (tall layered tropical forest trees with buttress roots); ba-k-oak-hickory
  (tall oak and hickory trees in summer leaf); ba-k-douglas-fir (tall straight Douglas-fir trees);
  ba-k-cedar-hemlock (giant old-growth cedar and hemlock with mossy trunks); ba-k-spruce-larch (narrow spruce and
  larch taiga trees)
Sizing rule: every piece is bottom-aligned on the ground line, stretched to the stage width, and drawn at its full
height times the stage multiplier in Content (x0.3 to x1); later layers in a stage's list draw in front.
Drawn in code: the map strip, pins, climograph, Climate space chart, sky gradient and ground band, the question
cards, preview.svg.

## Voice
Bank voice `curious-librarian` (Aoede, "Say curiously and warmly, like a friendly school librarian"). No neighbor
and no other spec in this batch uses it. `Curio.voice`, `scope: () => state.mode`.
- wRead (how; Read welcome; stale once a station is picked): "Tap a pin on the map, or pick from the Station list,
  to open its climate chart."
- placeIt (how; first station picked in Read; stale once Place on chart is pressed): "Now press Place on chart to see
  where this place sits in climate space."
- wKey (how; Key welcome; stale once the first answer is given): "Answer each question with the Yes, No or number
  buttons. The numbers are on the card."
- reveal (how; the key ends for the first time; stale once Reveal is pressed): "That's your prediction. Press Reveal
  to see what really grows there."
- match (event; Reveal shows a match; stale on station change): "Your key matches the real biome."
- miss (event; Reveal shows a miss; stale on station change): "A miss. Read the note under the cards to see what
  averages hide."
- needKey (how; Change entered on a station not yet keyed; stale once Go to Key is pressed or a keyed station is
  picked): "Key this station first. Press Go to Key."
- wChange (how; Change entered on a keyed station; stale once Fire, Clearing or Play is pressed): "Press Fire or
  Clearing, then press Play and watch the land grow back."
- shifted (event; the key result changes while a slider moves; stale when it changes back): "The key now predicts a
  different biome. Press Play to watch the new path."
- sameBack (event; Years reaches the end with sliders at zero after a Fire or Clearing; stale on Reset or a new Fire
  or Clearing): "Same climate, same biome. It came back."

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
- Number checks (Python, 2026-10-29, scratch biome.py): the key run on all 13 stations from the monthly values
  reproduces every T, P, summer share, dry line and result in "Worked key per station" (12 matches, Dodge City the
  miss) and all nine original What-if checks. A sweep of every station over the full slider ranges (-4 to +6 °C,
  -50 to +50 percent) found Utqiagvik at +6 °C keyed as Mediterranean shrubland (driest summer month 4.5 under a
  third of 13.8): the old step 4 had no temperature gate. Fixed by asking T 3 °C or more first (Koppen keeps cold
  dry-summer climates out of Cs); every listed result is unchanged and Utqiagvik +6 °C is now Boreal forest.
  Quillayute at -5 percent tips to Mediterranean shrubland (a real Csb edge), added as a What-if.
- Play: the old fixed 0 to 200 year slider at 8 s ran the whole savanna story (0 to 3 years) in 0.12 s and could not
  land on 0.2 or 0.3 years (step 1). Fixed with a span per biome (5 to 200 years, 200 steps, Play always about 8 s).
- Contrast: pin letters `#10161f` on the old boreal `#2f7d6b` (3.69:1) and temperate rainforest `#1f8a4c` (4.15:1)
  failed AA; the fills moved to `#3b9a83` (5.31:1) and `#46b574` (7.02:1). All other fills 5.17:1 or more.

## Done when
1. Every station's climograph and T, P match the Content values; Kasama's axis starts at Jul.
2. Keying all 13 stations with correct answers gives exactly 12 matches and 1 miss (Dodge City), tally "12 of 13".
3. Dodge City's dry line reads 546.0 mm and the step says "558.9 mm is more than 546.0 mm".
4. Kumasi's dry-month count is 4 and its result Tropical seasonal forest; Quillayute's driest summer month 40.2 is
   not under 40 and the result is Temperate rainforest.
5. In Change, every What-if check in Content gives the stated key result, including Utqiagvik +6 °C: Boreal forest.
6. With sliders at 0, Clearing at Berlin and Years at the end shows the oak and hickory layer; with -50 percent rain
   the last stage is Dry grassland or savanna with the "might stall" line.
7. Play takes about 8 s for every biome: Fire at Kasama shows the green shoots and the full grass as separate steps.
8. Focus: at 1366x768 and 680x425 the climograph is the biggest thing in Read, the question card in Key, the two
   scene cards after Reveal, and the painted landscape in Change.
9. A tap while Play runs: dragging Years pauses in the same frame; Fire or Clearing restarts at year 0 at once; a
   climate slider re-keys and redraws without stopping Play.
10. The Layer toggle shows biome letters as well as colors on every pin.
11. At 1366x768 and 375 wide the mode buttons, station list and the mode's focus are visible without scrolling; all
    30 images load and none shows a person.
12. Each how-to line is spoken once in a run of five actions; match, miss and shifted speak every time; no line
    names a disabled control (needKey plays instead of wChange on an unkeyed station).

## Open questions
- [biome-atlas] Dodge City is the only miss, kept on purpose as the lesson about averages. OK, or add a second miss?
- [biome-atlas] The tool teaches only HS-LS2-6; the climate key is the way in. Enough, or should the module add a
  climate standard (HS-ESS2-4 sits with climate-dashboard)?
- [biome-atlas] Succession stage times are rounded from several papers and labeled approximate. Is that precise enough?
