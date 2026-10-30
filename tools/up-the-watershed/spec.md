# Up the Watershed
Renamed from: Watershed Detective

## One idea
Pollution has an address: with only eight sample kits per case you walk a made-up creek upstream from the problem
(a closed beach, a green lake, a muddy trout stream), bracketing each suspect with a sample above and below it, on a
dry day and the day after a storm, until the jumps in the numbers point to the sources; then with a $3 million budget
you pick fixes and find that no plan cleans everything, so you choose what matters most and say why.

## Not like
- ph-mystery-liquids (grade 10, sci-chem): identifies unknown liquids at a lab bench; here the evidence is where along
  a creek a number jumps, and weather is a clue.
- water-shapes-earth (grade 9): erosion and deposition as landforms; here sediment is a pollutant with sources and
  fixes.
- island-economy (grade 9, possibly reshaped to a lake town): harvesting a shared resource over generations; here
  nothing is harvested, you trace pollution and pay for fixes.
- reserve-designer (grade 9): buying habitat cells; here land use matters only as a source of runoff.
- resource-detective (grade 2): the earlier "detective" tool; this title drops the word and the case is about
  sampling strategy.
- Grid Operator and Design Challenge Studio (this group): their trade-offs are energy and a design brief; here the
  trade-off is which water goal to meet first under one budget.

## Who and how
- Grade 12, Environmental science (Earth and Space Science), Pollution and Solutions. Students drive, pairs work best
  (one samples, one argues). 30 to 45 minutes for one case and Fix-it; three cases take two class periods.
- Topic line: "watershed pollution and solutions".
- Standards (module): HS-ESS3-4 (evaluate or refine a technological solution that reduces impacts of human
  activities on natural systems: Fix-it), HS-ETS1-3 (evaluate a solution to a complex real-world problem on
  prioritized criteria and trade-offs, including cost and social impacts: the goals, budget and who-pays notes).
  Cases supply the evidence the fixes are judged on.
- tool.json: driver "students", minutes "30-45", modes ["Cases", "Sample", "Claim", "Fix-it"], grades_label
  "Grade 12".

## Screens and modes
Layout: stage left (about 62 percent), panel right with the case card, kit counter and the mode's controls. The
watershed map is code shapes (creek, forks, lake, land parcels, roads) filled with painted textures, with the
suspects as painted cutout icons on it and sample spots, flags and labels in code (Art). At 1366x768 the map and the panel's buttons fit without scrolling; below 760 wide the map is on top with
pinch and drag disabled (it fits the width), and the panel below.

**Cases (default).** Focus: the three painted case cards, side by side on the stage. Three case cards: **Beach closed** (Heron Lake beach, E. coli), **Green lake** (Heron Lake,
phosphorus), **Muddy creek** (trout below Main Street, sediment). Each card: what people noticed, the measured
problem, the limit it breaks, and **Open case**. Cards show a check when solved.

**Sample.** Focus: the map, filling the stage; the newest result card opens beside the spot it came from. The map: two forks join into Alder Creek, which runs past the town of Linden into Heron Lake. Eleven
sample spots (circles with labels S1 to S9, Pipe, Outfall) and seven suspects (icons with names). Choose a spot, then
**Dry day** or **Day after storm**, then **Take sample** (uses one kit; 8 per case, counter "Kits left: 5"). The
result card lists all four tests (E. coli, nitrate, phosphorus, suspended sediment) with units, the limit for the
case's pollutant as a line on a small bar, and stays pinned on the map as a flag (blue = dry, gray-blue = storm, with
"D" or "S" in it). The **Logbook** tab lists every sample. **Compare two** picks two flags and shows the difference
("Up 1,333 CFU per 100 mL from S6 to S7, dry day"). A spot sampled twice in the same weather gives the same numbers
(the model has no noise; a note says real samples vary and real teams repeat them).

**Claim.** Focus: the map, with each checked suspect's icon ringed and its evidence pair drawn as a bracket. The
panel holds a suspect list with checkboxes; for each checked suspect, **Add evidence** opens the logbook to pick a
bracketing pair (one sample above, one below, same weather) or a direct sample (Pipe, Outfall). **Submit claim**.
Feedback per suspect: right with good evidence; right but the evidence doesn't bracket it (with what to sample);
wrong (with its real share at the target); missed (a hint naming the weather). After a submit, **Show the whole
creek** fills every spot in both weathers and draws each suspect's share at the target as a bar. Claims can be
revised; the case is solved when the culprit set is right with evidence for each.

**Fix-it.** Focus: the three goal gauges, before and after, in a row across the top of the stage, with the budget
bar under them; the solution cards fill the rest of the stage, each with its source's painted icon. Fix-it opens
when any case is solved (all three goals show; unsolved ones are marked "case not solved yet").
Solution cards with cost, what it changes, and who pays. Toggle any with **Add** / **Remove** on the card; the budget bar ($3,000,000) fills; over budget
turns the bar red and disables **Test plan**. **Test plan** shows the three goals as gauges, before and after, in both
weathers. **Save plan** keeps up to three for side by side; a **Why** box per plan offers sentence starters ("We put
the beach first because ..."), not saved beyond the session.

## Content
**Sites** (flow m³/s dry / storm): S1 North Fork at Ridge Road (0.30 / 1.80); suspect A pasture where cattle wade in
the creek; S2 North Fork below the pasture; S3 East Branch at County Line (0.40 / 2.40); suspect B fields with tile
drains (adds 0.05 / 0.10); S4 East Branch below the fields; S5 Alder Creek at Old Mill Bridge; suspect C construction
site, 12 acres of bare soil; S6 Alder Creek above Linden; suspect D1 town storm drains (adds 0 / 0.80; flows only in
storms); suspect D2 old sewer line leaking under the creek bank; S7 Main Street bridge; suspect E Linden treatment
plant outfall (adds 0.05); S8 Heron Lake inlet; S9 the beach; suspect F Canada geese on the beach. Direct samples:
**Pipe** (storm drain outfall at Main Street; dry: "no flow") and **Outfall** (plant effluent).

**Sample values** (E. coli CFU/100 mL; nitrate-N mg/L; total phosphorus mg/L; suspended sediment mg/L), dry then storm:
| Spot | Dry | Storm |
|---|---|---|
| S1 | 30; 0.30; 0.020; 5.0 | 200; 0.50; 0.080; 60 |
| S2 | 230; 0.60; 0.030; 15.0 | 3,200; 1.00; 0.180; 210 |
| S3 | 30; 0.30; 0.020; 5.0 | 200; 0.50; 0.080; 60 |
| S4 | 27; 1.60; 0.022; 5.6 | 492; 1.48; 0.277; 198 |
| S5 | 108; 1.20; 0.025; 9.3 | 1,626; 1.28; 0.236; 203 |
| S6 | 108; 1.20; 0.025; 11.3 | 1,626; 1.28; 0.336; 552 |
| Pipe | no flow | 5,000; 1.00; 0.300; 100 |
| S7 | 1,441; 1.23; 0.031; 11.5 | 2,351; 1.24; 0.331; 481 |
| Outfall | 100; 15.0; 3.00; 10 | 100; 15.0; 3.00; 10 |
| S8 | 1,358; 2.09; 0.216; 11.4 | 2,329; 1.37; 0.357; 476 |
| S9 beach | 447 (E. coli only) | 739 |
Model (for the builder): loads add and flows add; concentration = load / flow. Background per fork, dry / storm:
E. coli 30 / 200, nitrate 0.3 / 0.5, phosphorus 0.02 / 0.08, sediment 5 / 60. Loads added (E. coli CFU/s; others g/s),
dry / storm: A 6e5 / 5.4e7, 0.09 / 0.9, 0.003 / 0.18, 3.0 / 270; B 0 / 7.5e6, 0.60 / 2.5, 0.002 / 0.50, 0.5 / 350;
C 0 / 0, 0 / 0, 0 / 0.43, 1.5 / 1,500; D1 0 / 4.0e7, 0 / 0.8, 0 / 0.24, 0 / 80; D2 1.0e7, 0.02, 0.004, 0.1 (both); E
5e4, 0.75, 0.15, 0.5 (both). E. coli concentration = load / (flow x 10,000). Beach = 0.30 x inlet E. coli + 40 from
geese.

**Cases and answers** (a culprit adds 20 percent or more of the pollutant at the target in a weather where the target
breaks its limit):
- Beach closed: E. coli single-sample limit 410 (geometric mean 126). Beach 447 dry, 739 storm. Shares dry: sewer D2
  83.8, geese 8.9, pasture A 5.0 percent; storm: pasture 42.6, storm drains D1 31.5, sewer 7.9, background 6.6, fields
  5.9, geese 5.4. Culprits: D2, A, D1. Geese are the red herring.
- Green lake: phosphorus at the inlet over 0.05 in both weathers (0.216 dry, 0.357 storm). Shares dry: plant E 86.7,
  background 8.1; storm: fields B 27.2, construction C 23.4, background 18.3, storm drains 13.0, pasture 9.8, plant
  8.2. Culprits: E, B, C.
- Muddy creek: sediment at S7 481 in storms (over 80, "unlikely to support good fisheries"; dry 11.5 is under 25, "no
  harm"). Shares storm: construction C 61.2, fields 14.3, pasture 11.0, background 10.3, storm drains 3.3. Culprit: C.
Nitrate never passes 10 mg/L (the drinking water limit) anywhere but the Outfall pipe itself, which no one drinks.

**Fixes** (model effects; cost; who pays):
- A fence the creek, add water troughs: E. coli -70, sediment -60, phosphorus -50, nitrate -20 percent; $60,000;
  farmer with a conservation cost-share.
- B1 30 m grass buffers along the fields (storm only; tiles bypass them): E. coli -40, sediment -60, phosphorus -50,
  nitrate -30; $150,000; 12 hectares taken out of crops.
- B2 tile drain bioreactors: nitrate -40 dry, -25 storm; $80,000; farmers.
- C silt fence, sediment basin, quick seeding: storm sediment -75, phosphorus -60; $40,000; the developer (required by
  permit).
- D1 rain gardens and a stormwater pond: storm sediment -80, phosphorus -50, E. coli -60, nitrate -30; $900,000; town.
- D2 reline the old sewer: everything from it -98 percent; $350,000; sewer customers.
- E add phosphorus removal at the plant: effluent phosphorus 3.0 to 0.3 mg/L (-90 percent); $2,500,000; sewer
  customers.
- F goose management (no feeding, shoreline plants): geese term -50 percent; $15,000; parks.
- G rain advisory: beach posted closed for 48 hours after a big storm; $5,000; county health. Cleans nothing; on storm
  days the beach goal reads "swimmers protected, water still over 410".
All fixes: $4,100,000.

**Goals:** Beach: under 410 on dry days and storm days. Lake: inlet phosphorus under 0.05 on dry days and storm
phosphorus load cut by at least 25 percent. Creek: storm sediment at S7 cut by at least half.
**Worked plans** (beach dry / storm; inlet P dry, storm load change; S7 storm sediment, change):
- E alone ($2,500,000): 447 / 739; 0.047, -7.3; 481, 0.
- C alone ($40,000): 447 / 739; 0.216, -14.0; 260.2, -45.9. C + A ($100,000): 432 / 519; 0.214, -18.9; 228.5, -52.5.
- D2 + A ($410,000): 64.0 / 461.5. Add D1 ($1,310,000): 64.0 / 321.7.
- E + D2 + A + C + G ($2,955,000): 64.0 / posted (461.5); 0.041, -26.5; 228.4, -52.5. Meets every goal, the beach by
  advisory.
- D2 + A + D1 + C + B1 + B2 + F ($1,595,000): 44.0 / 284.2; 0.209, -39.2; 174.7, -63.7. Beach and creek met for real;
  lake fails on dry days.
- Everything ($4,100,000): 44.0 / 284.2; 0.041, -46.6; 174.7, -63.7.
No plan under $3,000,000 meets every goal without the advisory: E and D1 together cost $3,400,000.
**Model note:** "Leaves out: lake sediments that release old phosphorus for years, how long fixes take to work,
bacteria dying in sunlight, groundwater, and the fact that real samples vary from hour to hour."

## Interactions in detail
- Kits run out at 0: **Take sample** greys with "Out of kits. Make your claim, or press Restart case." Restart case
  refills kits and clears that case's flags and claim.
- Flags never overlap: two samples at one spot stack side by side (dry left, storm right).
- Claim feedback names the weather that would show a missed source ("The storm drains only flow in storms.").
- A bracketing pair must be adjacent across the suspect: A needs S1 and S2; B needs S3 and S4; C needs S5 and S6; D1
  needs the Pipe in a storm, or S6 and S7 in a storm with a dry S6 and S7 pair for contrast; D2 needs S6 and S7 dry;
  E needs the Outfall, or S7 and S8; geese are cleared by S8 and S9 in the same weather.
- Fix-it updates the budget bar on each toggle; gauges animate 400 ms after Test plan. A toggle during the
  animation clears the gauges to "plan changed, press Test plan" at once; nothing else plays on its own.
- Progress (solved cases, logbooks, saved plans) persists in localStorage under `up-the-watershed`; **Clear my
  progress** wipes it. Reset (kit) returns to Cases without clearing saved progress.
- `window.__tool`: `{mode, caseId, kitsLeft, samples, claim, solved, plan, goals}`.

## Look
Accent `--brand #5aa6c8` (creek blue), `--brand-ink #10161f`. Map: the painted textures are multiplied down to the
map palette so code labels stay readable: land `#1a2420`, fields `#2a3322`, town blocks `#2a2f38`, creek `#3b7fa8`
widening downstream, lake `#2c6a8f`. Painted suspect icons get a `#ffb8a8` ring when accused. Dry flags `#5aa9ff`
with "D" (7.40:1 for the `#10161f` letter), storm flags `#9fb4c8` with "S" (8.50:1). Contrast (computed): brand
on --panel 6.37:1, on --sec-bg 6.03:1; brand-ink on brand 6.68:1. Nearest accent on any spec is #9ec9e8 (gas-law-lab,
dE 16.6); group siblings are 81 or more apart.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 22 images. Prompts say only what is in the picture; signs
stay blank (the beach notice text is code).
Case and suspect cards: 4:3; cutout no; people no; the three case cards in Cases (about 300 px) and a suspect's card
when its icon is tapped (about 280 px).
- uw-beach: small lake beach with an empty lifeguard stand and a blank white notice board on a post, calm water,
  empty sand, summer afternoon (Beach closed case card; the notice text "Beach closed" is code over the board)
- uw-green-lake: a lake shore with thick bright green algae scum on the water, reeds, overcast light (Green lake)
- uw-muddy-creek: a small brown muddy creek under a stone bridge in a small town, cloudy day (Muddy creek)
- uw-pasture: brown cattle standing in a shallow creek in a green pasture, muddy banks, summer
- uw-fields: flat cornfields with a drainage tile pipe outlet flowing into a ditch, early summer
- uw-construction: graded bare-soil construction site next to a small creek, a muddy runoff channel, cloudy day
- uw-storm-drain: concrete storm drain outfall pipe under a town bridge, water flowing into a creek after rain
- uw-sewer: old brick manhole on a grassy creek bank, damp ground around it, small town houses behind
- uw-plant: small town wastewater treatment plant with round clarifier tanks beside a river, aerial view
- uw-geese: Canada geese on a sandy lake beach, calm water, morning light
Map icons (the suspects on the map, also the picture on each Fix-it card): one shared prompt, "a tiny <piece>,
three-quarter view from above, like a model railway miniature, crisp painted illustration, on a plain flat light
grey background"; 1:1; cutout yes; people no; drawn 48 px on the map (40 px at 760 wide and below), 64 px on fix
cards. Pieces (7): uw-i-cattle (two brown cows standing in a strip of creek water); uw-i-tile (a short black drain
pipe pouring water into a ditch beside green crop rows); uw-i-construction (a small yellow excavator on a patch of
bare brown soil); uw-i-storm-drain (a round concrete pipe mouth spilling grey water); uw-i-sewer (an old brick
manhole with a cracked iron lid on grass); uw-i-plant (two round treatment tanks and a small building); uw-i-geese
(three Canada geese standing together). Fix G (rain advisory) uses a code notice-board shape.
Map textures: one shared prompt, "seamless top-down aerial texture of <piece>, even soft light, filling the whole
frame"; 1:1; cutout no; people no; tiled and clipped to the code shapes of the map, darkened to the map palette.
Pieces (5): uw-t-pasture (green grazed grass with a few cattle paths); uw-t-cropland (rows of young corn in brown
soil); uw-t-town (small town rooftops, yards and trees); uw-t-bare-soil (graded brown soil with tire tracks);
uw-t-water (calm blue-green lake water with small ripples).
Sizing rule: icons sit on their suspect's map point, bottom-centered; textures tile at 256 px.
Drawn in code: the map shapes and roads, sample spots, flags, labels, the logbook, result cards, gauges, budget bar,
brackets, preview.svg.

## Voice
Bank voice `casual-peer` (Zubenelgenubi, "Say casually and naturally, like a friendly teenager explaining
something"), framed as a volunteer on Linden's stream team. No neighbor and no other spec in this batch uses it.
`Curio.voice`, `scope: () => state.mode`.
- wCases (how; Cases welcome; stale once a case is opened): "Pick a case card and press Open case. We have eight
  kits, so plan your stops."
- wSample (how; Sample welcome; stale once a sample is taken): "Tap a spot, choose Dry day or Day after storm, then
  press Take sample."
- bracket (how; first time two samples in the same weather sit on both sides of a suspect; stale on case change):
  "Nice, that pair brackets a suspect. A jump between them is evidence."
- lastKit (event; one kit left; stale on Restart case): "Last kit. Make it count."
- outOfKits (event; kits reach 0; stale on Restart case or Claim): "Out of kits. Go to Claim and make your case, or
  press Restart case."
- wClaim (how; Claim welcome; stale once a suspect is checked): "Check each suspect you blame, then press Add
  evidence for each one."
- solved (event; claim right; stale on case change): "That's the case. Every source has evidence behind it."
- wFix (how; Fix-it welcome; stale once a fix is added): "Press Add on the fixes you want, keep the bar under three
  million, then press Test plan."
- noPlan (event; first Test plan that misses a goal; stale on plan change): "No plan here fixes everything for three
  million. Pick what matters most, and write why."

## Family engine
none.

## Sources
- E. coli limits 126 (geometric mean) and 410 (statistical threshold) CFU/100 mL: EPA, 2012 Recreational Water Quality
  Criteria, https://www.epa.gov/wqc/2012-recreational-water-quality-criteria
- Nitrate-N 10 mg/L: EPA National Primary Drinking Water Regulations,
  https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations
- Phosphorus 0.05 mg/L for streams entering lakes: EPA (1986), Quality Criteria for Water ("Gold Book"),
  https://www.epa.gov/sites/default/files/2018-10/documents/quality-criteria-water-1986.pdf
- Sediment bands (under 25 no harm; 25 to 80 good to moderate fisheries; 80 to 400 unlikely good): European Inland
  Fisheries Advisory Commission (1965), Water quality criteria for European freshwater fish: finely divided solids,
  EIFAC Technical Paper 1, FAO.
- Farm fixes (fencing, buffers, bioreactors): EPA (2003), National Management Measures to Control Nonpoint Source
  Pollution from Agriculture, EPA 841-B-03-004; USDA NRCS conservation practice standards 382, 390, 605.
- Town fixes (rain gardens, ponds, sewer repair): EPA (2005), National Management Measures to Control Nonpoint Source
  Pollution from Urban Areas, EPA 841-B-05-004.
- Construction fixes and permit: EPA Construction General Permit,
  https://www.epa.gov/npdes/stormwater-discharges-construction-activities
- Plant phosphorus removal to 0.3 mg/L and below: EPA (2008), Municipal Nutrient Removal Technologies Reference
  Document, EPA 832-R-08-006.
- Rain advisories at beaches: EPA BEACH Act program, https://www.epa.gov/beaches
- Creek, town, flows, loads and costs: made up for this tool, scaled to the sources above.
- Number checks (Python, 2026-10-29, scratch ws.py, ws2.py): the load model as written (loads and flows add,
  E. coli = load / (flow x 10,000), beach = 0.30 x inlet + 40 x geese) reproduces every Sample value, every case
  share listed (beach dry 83.8 / 8.9 / 5.0; storm 42.6 / 31.5 / 7.9 / 6.6 / 5.9 / 5.4; lake dry 86.7 / 8.1, storm
  27.2 / 23.4 / 18.3 / 13.0 / 9.8 / 8.2; creek 61.2 / 14.3 / 11.0 / 10.3 / 3.3) and every worked plan. Nitrate peaks
  at 2.09 mg/L (S8 dry), under 10 everywhere but the Outfall. All 512 fix sets checked: none at $3,000,000 or less
  meets every goal without the advisory; two meet them with it (E + D2 + A + C + G at $2,955,000, and the same + F at
  $2,970,000). Kits: each case solves in 5, 5 and 2 samples, inside 8. No line, table or rule changed.

## Done when
1. The Sample table values appear for every spot and weather (rounded as listed).
2. Beach closed solved with D2 (S6 and S7 dry), A (S1 and S2 storm) and D1 (Pipe storm) in 8 kits or fewer.
3. Accusing geese shows "about 9 percent dry, 5 percent storm" and marks it wrong.
4. Green lake: the plant is caught by the Outfall alone; fields and construction need storm samples.
5. Muddy creek: claiming C alone with S5 and S6 storm solves it; adding B gives "adds sediment, but only 14 percent".
6. Fix-it E + D2 + A + C + G shows $2,955,000 and all three goals met (beach "protected" on storm days).
7. D2 + A + D1 + C + B1 + B2 + F shows the lake goal failing on dry days at 0.209.
8. Turning on every fix goes over budget at $4,100,000 and disables Test plan.
9. Focus: at 1366x768 and 680x425 the case cards fill the stage in Cases, the map in Sample and Claim, and the
   gauges lead Fix-it; spot labels are at least 10 px in the preview.
10. A tap while the gauges animate: adding or removing a fix clears them at once; no other motion waits on a tap.
11. At 1366x768 and 375 wide the map, Take sample and the kit counter are visible without scrolling; all 22 images
    load, the map textures line up with their shapes, and none shows a person.
12. Each how-to line speaks once in five actions; lastKit, outOfKits and solved speak every time; no line names a
    disabled control.

## Open questions
- [up-the-watershed] Title: "Up the Watershed" (keeps the topic word; the overlap note's "Upstream" drops it). Take
  it, or another?
- [up-the-watershed] The rain advisory lets a plan meet the beach goal without cleaning the water. Keep it as an
  honest real-world option, or count it as a miss?
- [up-the-watershed] Costs, flows and loads are made up (scaled to EPA guidance). OK, or should Sources name real
  cost studies?
