# Front Line

## One idea
A front is a line nobody can see: the student reads a row of five weather stations every half hour, finds the same
sudden change (wind swings, dew point drops or climbs, pressure turns around) reaching each station in turn, times
it, and forecasts when it reaches home as a window and a chance, then watches ten possible next days score the call.

## Not like
- raindrop-s-journey (gr 6 story, concept): one water molecule's path through the water cycle. No stations, no
  fronts, no forecast.
- ocean-conveyor (gr 6 simulator, concept): global winds, currents and coastal climate. Here one day, one row of
  stations, one boundary between two air masses.
- climate-dashboard (gr 9 data, spec) and warming-evidence-desk (gr 8 data, draft): decades of real records, trend
  against noise. Here hours of readings and a forecast that is checked the next day.
- weather-wardrobe (K) and climate-postcards (gr 3), the weather family (concepts): daily sky stamps and monthly
  climate graphs. This tool shares no engine with them and stays out of the family (idea card flag).
- cooler-challenge (gr 6 builder, draft): heat moving through walls. Nothing here about heat transfer by design.
- moon-phase-model, pocket-universe (gr 6 space): no overlap in idea or mechanic.
- Batch neighbors tap-to-start-puppets, paper-plane-assembly-line, box-packer, leaf-factory: different subjects and
  grades; no shared mechanic (no assembly, packing or factory loop here).

## Who and how
Grade 6 science, module Air Masses and Weather (science-6-air-masses-and-weather). Driver: students (or teacher on a
projector, the class calling out readings). 25 to 40 minutes: one forecast day takes about 15, Side view about 10.
Standard: MS-ESS2-5. Prompts are not personal; no disclosure note needed.

## Standards map
MS-ESS2-5: "Collect data to provide evidence for how the motions and complex interactions of air masses results in
changes in weather conditions." One code, five parts, each with its own step:

| Part of the code | Student action | What they see | Done when check |
|---|---|---|---|
| Collect data | Read stations (or Auto-read) logs a reading at all five stations every 30 min, 12 am to 6 pm | Cards update, five chart lines grow one point per read | After 6 pm the log holds 37 readings per station and the charts plot exactly those |
| Motion of air masses | Track: mark when each station's weather changed; Forecast: lay the ruler line through the marks | Marks as dots on the front tracker (distance against time); the line's speed in km per hour | Marks within 1 h of the true passage at 3 stations give a line that crosses Elm Grove within 1.5 h of the true arrival |
| Interactions change the weather | Side view: pick the arriving and resident air masses, play | Cold air wedging under warm air (storms) or warm air sliding up a gentle ramp (wide steady rain), dry pairs with no rain | Each of the 9 pairs plays its own picture and its own line; the desk verdict names the day's pair |
| High to low pressure | Big picture: tap where the air behind the front came from | Map with H, L, the front and flow arrows; the pressure chart rising behind each front | Tapping H gives "right"; L or the front gives the reason |
| Forecasts are probabilities | Set an arrival window (30 min to 3 h) and a rain chance; Check | Ten possible next days as ticks on the Home row; rain on N of 10 | A window from the marks catches 7 or more of 10; the rain band matches the count |

## Screens and modes
Header: title, mode buttons "Forecast desk" and "Side view" (.seg), Motion, Sound, Read.

**On load**: Forecast desk, Day 1, clock at 12:00 am, no readings logged. The station row shows names and empty
readouts ("--"). Nothing plays. The hint reads "Tap Read stations to take the first reading." The welcome (wDesk) is
queued for after the first tap; the first tap on Read stations logs the 12:00 am reading at once and cuts or skips
it (BASELINE rule 16). First tap on each control: Read stations logs one reading; Auto-read starts reading every
0.4 s; a chart tab switches the chart; Side view switches mode.

### Forecast desk
Stage (left, 920 px wide at 1366x768):
- **Station row** (top, 230 px): five cards west to east, Ash Creek, Bell Plains, Cedar Bluff, Dover Flats, Elm Grove
  (Home, gold outline and a house icon), with "120 km" between cards and "West" and "East" at the ends. Each card: sky
  tile (painted, 16:9) with the station cutout in front and a code-drawn wind arrow over it; temperature (28 px,
  "28 °C (82 °F)"); "Wind from S, 25 km/h"; "Dew point 19 °C"; "Pressure 1008.8 mb"; rain drops icon with "5 mm" in
  the last 30 min, or "dry". Night hours (before 6:30 am, after 7:30 pm) dim the tile with a navy overlay.
- **Charts** (below, 440 px): tabs Temperature, Dew point, Pressure, Wind, Rain. One chart at a time, five lines
  (station color plus marker shape plus end label letter A to E, never color alone), x axis 12 am today to 6 pm
  (extends to 6 pm tomorrow after Check), y axis named with unit. Wind is a step chart on compass rows N, NE ... NW.
  Rain is bars per reading. Tapping a station card highlights its line (others dim to 30 percent); tap again clears.
  A one-line note under the Dew point tab: "Dew point: the temperature air must cool to for dew to form. Higher dew
  point, more water vapor."

Panel (right, 446 px): hint (always on top), then step tabs **1 Read**, **2 Track**, **3 Forecast** (all open at
any time; the hint suggests the order), then the step's controls, then a day line ("Day 1. Forecasts verified: 0 of
0") with **New day**.
- **1 Read**: clock ("Today 9:30 am"), **Read stations**, **Auto-read** (becomes **Pause**), a review slider over
  logged readings (moving it shows that reading on the cards; the chart gets a cursor). At 6:00 pm Read stations and
  Auto-read disable and the clock says "6:00 pm. Now. Everything after this is the forecast."
- **2 Track**: station chips A to E. Pick a chip, then tap a reading on the chart: a vertical mark in that station's
  color and letter sits on that reading (any tab). Keyboard: arrows move the mark 30 min, Enter sets. A list shows
  "Ash Creek: 9:30 am / Bell Plains: 1:00 pm / Cedar Bluff: -- ...", each with **Clear**. Marks are never judged here.
- **3 Forecast**: the stage chart area swaps to the **front tracker** (focus): x is time 12 am today to 6 pm tomorrow,
  y is distance east of Ash Creek, 0 to 480 km, with a row line per station; "Now" line at 6 pm, the future shaded.
  The student's marks are dots. A **ruler line** with two round handles (start drawn flat across Ash, so it says
  nothing) is dragged through the dots; it shows "Your line: 34 km per hour" and, where it crosses the Elm Grove row,
  a dot labeled with the time. The **arrival window** is a band on the Elm Grove row with two handles (30 min snaps,
  width 30 min to 3 h, inside 6 pm today to 6 pm tomorrow), labeled "10:30 pm to 1:00 am". The panel holds three picks:
  **Wind after the front** (8 arrow pictures, "from N" to "from NW", 56 px), **Tomorrow afternoon compared with this
  afternoon** (Much colder: 10 °C or more / A little colder: 3 to 9 °C / Warmer), **Chance of rain at Elm Grove**
  (Low: under 30% / Medium: 30 to 60% / High: over 60%), each card with a code-drawn icon and words. **Check forecast**
  enables when the window is placed and all three picks are made; until then the hint names the first missing part.
- **After Check** (one per day; picks lock): the tracker shows ten possible-next-day ticks on the Elm Grove row (a
  drop on the ones with rain), the true passage times at every station as hollow dots and the true front as a dashed
  line beside the student's. The panel lists four result rows (check or cross icon plus words, see Content), the
  verdict "Forecast verified" (all four right) or "Not verified: see the rows", and **Play the next day**.
- **Play the next day**: the clock runs 6:30 pm to 6 pm tomorrow, one reading per 0.5 s (24 s). Cards and charts
  extend live; Elm Grove's sky changes when the front arrives. **Pause** and **Skip to end** stay live; chart tabs,
  card highlight and the review slider work during the run and change the view at once.
- **Big picture** (stage tab beside Charts and Tracker, unlocked after the run): a code-drawn map of the row with the
  front (cold: blue line with triangles, warm: red line with half circles, always labeled in words), H and L, and
  flow arrows from H toward L. Question card: "The wind behind the front blew from the [direction]. Tap where that air
  came from." Targets: H, L, the front line (60 px hit areas). One try.
- **New day**: new data (see Content); the step tabs return to Read with an empty log.

Layout at 680x425: stage left 450 px, panel right 230 px. Cards drop the sky tile to a 24 px strip and show only
temperature and wind; pressure, dew point and rain fold into the charts (tap a card for a small popover). Chart tabs
become a select. The panel shows hint plus the current step's main buttons first; the day line folds under a
"More" button. Nothing the current step needs is below the fold.

### Side view
Stage: a code-drawn cross-section (focus, 920x470 at 1366x768): the same row along the ground, height 0 to 10 km up
the side, with a caption "Heights are stretched about [N] times so the air layers show" (N computed from the drawn
scale). Air masses are tinted bodies (cold blue, warm humid green, hot dry tan) with flow arrows; clouds are painted
cutouts placed and scaled in code where the lifted air is humid; rain streaks are code. Below it, a compact copy of the
station row (temperature, wind) at 150 px.
Panel: "Arriving from the west" and "Sitting over the row" (three painted air-mass cards each), **Play** / **Pause**,
a time slider 0 to 24 h, and a result box naming the pair (front type in words, the weather it brings). Picking a
card stops play and redraws at time 0. Play runs 24 model hours in 16 s. Nothing is scored.
At 680x425 the station strip folds away and the cards shrink to 64 px thumbnails with names.

## Content
**Stations**: x = 0, 120, 240, 360, 480 km (Ash Creek, Bell Plains, Cedar Bluff, Dover Flats, Elm Grove). Fictional
towns on a plain; the notes say the readings are a model built from how real fronts behave.
**Clock**: readings every 30 min, t = 0 (12:00 am) to t = 18 (6:00 pm), 37 per station. Forecast period to t = 42.
**Day draw** (seeded; Day 1 fixed, then a shuffled cycle of the three types, reshuffled each cycle):
speed v uniform: Storm and Dry 20 to 45 km/h, Warm 12 to 25 km/h. Lead L uniform 1.5 to 18 h; front position at 6 pm
x_now = 480 - L v; redraw unless 120 + v <= x_now <= 17 v (so 2 to 4 stations have passed and Ash passed after 1 am).
Passage time at station k: T_k = 18 - (x_now - x_k) / v. Pressure at the front pf: whole number 1000 to 1008 mb.
Storm and Dry contrast c: 6 or 12 °C. Warm rise r: 7 or 11 °C. Storm moisture ahead dpa: 13, 16 or 19 °C.
Behind wind: Storm and Dry from NW (315) or N (360); Warm from SW (225).
**Day 1** (fixed): Storm, v 35, L 5, pf 1004, c 12, dpa 19, behind NW. Passages: Ash 9:17 am, Bell 12:43 pm, Cedar
4:09 pm, Dover 7:34 pm, Elm Grove 11:00 pm.
**Readings** (d = t - T_k in hours; D(t, A) = A cos(2 pi (t - 15) / 24), warmest at 3 pm; noise per reading, seeded:
temperature and dew point +-0.3, pressure +-0.2, direction +-8 degrees, speed +-3):
| | Storm (cold front, humid air ahead) | Dry (cold front, hot dry air ahead) | Warm (warm front) |
|---|---|---|---|
| Temp ahead | 24 + D(t,4) | 27 + D(t,4) | 7 + D(t,1.5) |
| Temp behind | 24 - c + D(t,3), blended over d 0 to 1 | 27 - c + D(t,3), blended over 0 to 1.5 | 7 + r + D(t,3), blended over 0 to 2 |
| Dew point | dpa, then dpa - 14 (blend as temp) | 2, then -8 | 3; from d = -6 rises to 6 at d = 0; then 3 + r (blend 0 to 2) |
| Wind | from S 25; at front 50; behind 35, 25 after d = 6 | from SW 30; at front 55; behind 35, 25 after 6 | from SE 15; behind 20 |
| Pressure | pf + 0.6 min(-d,10); behind pf + 2 min(d,3) + 0.5 clamp(d-3, 0, 8) | as Storm | pf + 0.4 min(-d,16); behind pf + 0.05 min(d,10) |
| Sky tile | d<-3 fair; -3 to -0.5 building; -0.5 to 1 storm (if raining) else building; 1 to 3 clearing; then clear cold | d<0 hot clear; 0 to 1.5 dust; then clear cold | d<-14 clear cold; -14 to -9 cirrus; -9 to -6 thickening; -6 to 0 steady rain; 0 to 1.5 low gray; then warm hazy |
| Rain | 5 mm per reading for d in [-0.5, 1) at raining stations | none | 1 mm per reading for d in [-6, 0) everywhere |

**Which storm stations rain**: n = stations passed by 6 pm. dpa 19: all of them, and Dover and Elm Grove. dpa 16:
floor(n / 2) of them, chosen by seed; Elm Grove rains in the played day on half the seeds. dpa 13: none.
**Ten possible next days**: speed factors f = 0.92, 0.938 ... 1.08 (ten even steps); arrival = 18 + (480 - x_now) /
(v f). Rain at Elm Grove on: Storm dpa 19: 9, dpa 16: 5, dpa 13: 2; Warm: 10; Dry: 1 (a stray shower). The played
next day uses f = 1.
**Results** (rows after Check):
- Arrival: "Your window caught [k] of 10 possible next days." Right at 7 or more.
- Wind: right when the pick is the behind direction. Reason: "Behind the front, every station turned to from the [NW]."
- Temperature: Elm Grove 3 pm tomorrow minus 3 pm today is -13 (c 12), -7 (c 6) or +8 to +12 (Warm). Reason: "Behind
  the front the stations ran about [c] °C colder" or "warmer".
- Rain: band from the ten (Low 0 to 2, Medium 3 to 6, High 7 to 10). Reason: "Rain fell at [m] of [n] stations as the
  front passed, and on [N] of 10 possible next days at Elm Grove."
- Day name, shown after Check: "Cold front: cold, dry air from Canada pushed under warm, humid Gulf air" (Storm), "Dry
  cold front: cold Canadian air pushed under hot, dry desert air" (Dry), "Warm front: warm, humid Gulf air slid up
  over cold air" (Warm).
**Big picture map**: Storm and Dry: H west-northwest of Ash, L north of Elm Grove. Warm: H southeast of Elm Grove
(air came around it from the Gulf), L northwest of Ash. Right: H, "Right. Air flows out of high pressure toward low
pressure." L: "That's where the air is heading. Air flows out of the high toward the low." Front: "The front is
where the two air masses meet. The air behind it came out of the high."
**Air masses (Side view)**: Cold, dry: from Canada (continental polar), 5 °C, dew point -8. Warm, humid: from the Gulf
of Mexico (maritime tropical), 26 °C, dew point 20. Hot, dry: from the desert Southwest and northern Mexico
(continental tropical), 32 °C, dew point 2.
**Pairs** (arriving, then over the row): cold dry into warm humid: cold front, tall storms at the steep nose; cold dry
into hot dry: dry cold front, wind and blowing dust; warm humid into cold dry: warm front, clouds far ahead (cirrus,
then lower gray), steady rain; hot dry into cold dry: warm front, thin high clouds, little rain; warm humid and hot
dry either way: dry line, a sharp dew point drop and, between 2 pm and 8 pm model time, storm clouds bubbling up on
the humid side; same into same: no front. Slopes drawn true before the stretch: cold front 1:100 near the ground,
warm front 1:200.

## Interactions in detail
- Read stations always logs the next reading; Auto-read logs one per 0.4 s and any tap on Read stations, a tab or a
  card acts at once (Auto-read keeps going until Pause or 6 pm). Mode switch pauses it.
- A mark can sit on any reading of any station, including Dover and Elm Grove before the front reaches them (the
  student may be wrong; the verdict shows it). Fewer than two marks: the ruler line still works; Check still allowed.
- Ruler handles clamp to the tracker; a vertical or flat line shows "Your line: no speed" and no crossing.
- Window: dragging one handle past 3 h pulls the other; it never crosses 6 pm today or 6 pm tomorrow.
- After Check the day is locked: picks, marks, line and window cannot change. New day starts fresh data; Reset is
  not offered (New day is the reset). Mode switches keep the day's state.
- Side view: changing a card mid-play stops, redraws at 0 and keeps the new pair; the slider scrubs while paused.
- Extremes: v 45 with L 1.5 puts the front 68 km from home at 6 pm (arrival 7:30 pm, the earliest); L 18 (possible
  for v 13.7 to 18.9 km/h) puts arrival at noon tomorrow (the latest). Every day has 2 to 4 passed stations.

## Look
Weather office, light: paper #eef2f5, panel #ffffff, ink #15202b (14.65:1 on paper), muted #4f5b67 (6.17:1), line
#c9d2db, focus #1f5fd1 3 px ring. Accent `--brand #5b3fa6` (storm violet; white on it 7.76:1, it on paper 6.89:1),
used for step tabs, Check and the ruler line. Station lines on white: A #0b6e99 circle (5.67:1), B #b35c00 square
(4.72:1), C #2e7d32 triangle (5.13:1), D #a1286a diamond (6.94:1), E Home #15202b thick with star (16.49:1). Front
symbols: cold #1f5fd1 (5.81:1), warm #c62828 (5.62:1). Night overlay #1b2a44 at 55 percent; white text on it 14.37:1.
Side view air tints at 35 percent: cold #7fb2e5, humid #6fbf8f, dry #d9b77a. Different from neighbors' accents
(cooler-challenge red #b32630, warming-evidence-desk amber, climate-dashboard sea glass, pocket-universe pink).

## Art
Painted, none with people. Sky tiles share one low horizon of prairie grass so they swap cleanly.
- sky-fair: summer prairie with puffy white cumulus in a blue sky; 16:9; no cutout; station tile.
- sky-building: tall gray-based cumulus towers building over the prairie, hazy humid light; 16:9; tile.
- sky-storm: dark thunderstorm with heavy rain shafts and a lightning flash over the prairie; 16:9; tile.
- sky-clearing: broken clouds moving off, crisp light, wet grass; 16:9; tile.
- sky-clear-cold: deep clear blue sky, crisp air, long shadows on the grass; 16:9; tile.
- sky-cirrus: thin high cirrus streaks and a halo round a pale sun; 16:9; tile.
- sky-thickening: smooth gray sheet of cloud lowering, sun a dim disk; 16:9; tile.
- sky-steady-rain: low dark gray overcast with steady light rain; 16:9; tile.
- sky-low-gray: low gray cloud and mist after rain, damp grass; 16:9; tile.
- sky-warm-hazy: warm humid haze, scattered small clouds, soft sun; 16:9; tile.
- sky-hot-clear: pale hot sky with heat shimmer over dry grass; 16:9; tile.
- sky-dust: brown blowing dust wall rolling across dry prairie; 16:9; tile.
- station: a white louvered instrument shelter on legs, a rain gauge and a mast with cup anemometer, on a grass tuft;
  3:4; cutout; sits bottom-center of every tile (the wind arrow is code, so it can turn).
- mass-cold: snowy spruce forest under a pale clear winter sky, northern Canada; 4:3; Side view card.
- mass-humid: Gulf of Mexico shoreline with warm humid haze over the water; 4:3; Side view card.
- mass-dry: red desert mesas under a hot pale sky; 4:3; Side view card.
- cloud-cb: a towering cumulonimbus with a flat anvil top; 3:4; cutout; Side view at a cold front nose.
- cloud-ns: a long dark rain cloud layer with rain beneath; 4:1; cutout; Side view warm front.
- cloud-ci: thin wispy high cirrus; 4:1; cutout; Side view far ahead of a warm front.
- cloud-cu: small puffy cumulus; 4:3; cutout; fair weather in Side view.
- cloud-dust: a low rolling dust cloud; 16:9; cutout; dry cold front in Side view.
Night is a code overlay, never a second painting. Text never sits on the paintings.

## Voice
Bank `news-reader` ("Say clearly and steadily, like a trusted radio news reader"), styled: "Say clearly and steadily,
like a radio weather forecaster reading the evening report." Not used by a science neighbor (climate-dashboard
hs-narrator, cooler-challenge and warming-evidence-desk friendly-dad, molecule-forge knowing-guide, pocket-universe
casual-peer, living-pond gravel-ranger, which-way-is-down upbeat-guide). Uses the kit voice queue, scope = mode.

| id | kind | when | stale when | text |
|---|---|---|---|---|
| wDesk | how (welcome) | Forecast desk entered | a reading is logged | "This is the forecast desk. Five weather stations sit in a row, and Elm Grove is home. Tap Read stations to take the first reading." |
| readMore | how | after the first reading | clock at 6 pm | "Each reading adds a point to every chart. Keep tapping Read stations, or tap Auto-read." |
| change | how | first logged reading where a station's wind has turned over 45 degrees | Track step opened | "Something just changed at [Ash Creek]. Look at its wind and its dew point." (one clip per station name) |
| atNow | how | clock reaches 6 pm | Track opened | "That's 6 pm, the last reading. Open Track, pick a station, and tap the reading where its weather changed." |
| track | how | Track opened first time | a mark is set | "Pick a station chip, then tap the reading where its weather suddenly changed." |
| forecast | how | Forecast opened first time | the line is moved | "Drag the ends of the ruler line through your marks. Where it crosses Elm Grove is your best guess." |
| window | how | the line is moved first time | window moved | "Now drag the window on the Elm Grove row, then pick the wind, the temperature and the chance of rain." |
| ready | how | all parts set; needs Check enabled | Check tapped | "Your forecast is ready. Tap Check forecast." |
| pass | event, whole | Check, all four right | never | "Forecast verified. Here's how the possible next days turned out." |
| fail | event, whole | Check, any wrong | never | "Not verified yet. Each row shows what the data said." |
| play | how | after pass or fail finishes | run started | "Tap Play the next day to watch it arrive at Elm Grove." |
| arrived | event | front reaches Elm Grove in the run | run skipped past by more than 2 h | "The front is here. Watch the wind swing." |
| big | how | run ends | map answered | "Open Big picture and tap where the air behind the front came from." |
| bigRight | event, whole | H tapped | never | "Right. Air flows out of high pressure toward low pressure." |
| bigL | event, whole | L tapped | never | "That's where the air is heading. Air flows out of the high toward the low." |
| bigFront | event, whole | front tapped | never | "The front is where the two air masses meet. The air behind it came out of the high." |
| newDay | how | New day | a reading is logged | "A new day. Tap Read stations to start." |
| wSide | how (welcome) | Side view entered | Play tapped | "Side view. Pick the air arriving from the west and the air over the row, then tap Play." |
| pCold | how, per pair | Play with that pair, first time | pair changed | "Cold, dense air plows under the warm, humid air and shoves it up fast. Tall storm clouds grow right at the front." |
| pDryCold | how | same | same | "Cold air pushes under hot, dry air. The air gets lifted, but it's too dry to rain, so you get wind and dust." |
| pWarm | how | same | same | "Warm air slides up over the cold air on a long, gentle ramp. Clouds spread far ahead, and steady rain falls for hours." |
| pDryWarm | how | same | same | "Hot, dry air rides up over the cold air. Only thin, high clouds form." |
| pDryLine | how | same | same | "Humid Gulf air meets dry desert air at a dry line. On hot afternoons, storms can bubble up along it." |
| pSame | how | same | same | "Same air on both sides, so there's no front. Only day and night change the weather." |

How lines speak once per page load, then only set the hint. Event lines speak every time. pass and fail never repeat
within a day (one Check). No line names a disabled control: atNow needs Track; ready needs #check enabled.

## Family engine
none (family none). Charts and the tracker are the tool's own SVG. The tool does not join the weather family.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Arrival window (7 of 10) | guess a spot; mash the window; the widest window; "right after now"; one usual window learned over many days; the answer on screen; one station gap after Dover (common wrong); skip marking | Python, 10,000 days per type: random 3 h window passes 12 to 13 percent; "6 pm to 9 pm" 0 to 13 percent; width caps at 3 h; the best single fixed window in hindsight passes 22 to 30 percent (a climatology guess, shown beside the true track after Check); "one gap after the last mark" 6 to 22 percent; nothing on screen gives the arrival before Check (no auto-fit line, the ten ticks and true dots appear only after it, the charts stop at 6 pm); careful marks plus a centered 3 h window pass 93 to 97 percent |
| Wind after the front | guess; the wind blowing now at Elm Grove (common wrong); same answer every day | guess 1 in 8; the current wind (S, SW, SE) is never the behind wind (NW, N, SW); behind wind varies NW, N, SW across days; noise of 8 degrees never crosses a 22.5 degree bucket edge |
| Tomorrow afternoon | guess; "fronts always bring cold" (common wrong); "rain means colder"; always "Much colder" | guess 1 in 3; Warm days are warmer (+8 to +12); weak cold days are -7, so "Much colder" fails them; the answer is in the passed stations' before and after readings, which is the skill |
| Rain chance | guess; "a front always rains" (common wrong); never pick Medium | guess 1 in 3; Dry and moist-poor Storm days are Low; Medium is right on a third of Storm days; checked in Python: the share of passed stations that rained falls in the same band as the ten days on every draw (n = 2, 3, 4) |
| Forecast verified (all four) | any of the above combined | the four are independent picks; the best fixed window times the type rules tops out near 30 percent, a careful student about 95 |
| Retry for the answer | Check, read the answer, redo | one Check per day; the day locks; New day draws new speed, lead and strength |
| Big picture tap | guess; tap L because "air goes to low" (common wrong) | one try; guess 1 in 3; L gets its reason; the rule (air leaves the high) is the content, so learning it is learning the standard |
| Marks and ruler line | not scored | shown against the true passages after Check, so a wrong mark is visible, never graded |
| Side view | no check | nothing scored |

## Heard in order
Grade 6: not every line is voiced, but these must land in order.
- First tap Read stations: the reading logs at once; wDesk is cut or skipped (rule 16); readMore after that tap.
- change plays after the reading that shows the shift, never before the cards show it; a newer reading drops a
  queued change for an older station.
- Check: pass or fail, whole; the result rows are already on screen; play waits for it. Tapping Play the next day
  before play starts drops play.
- Run: arrived when Elm Grove's card turns; at the end, big. bigRight, bigL or bigFront whole, then nothing.
- Side view: Play, then that pair's line; a card tap drops it if not started.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| A cold front is colder, denser air advancing under and replacing warmer air | NWS glossary "cold front" | NWS Louisville "Basic fronts" | yes |
| At a cold front the temperature and dew point drop | Penn State METEO 3 "Cold fronts" | Wikipedia "Cold front" (table) | yes |
| Cold front wind shifts from S or SW to W or NW (Northern Hemisphere) | Penn State METEO 3 | Wikipedia "Cold front" | yes |
| Pressure is lowest at the front, then rises behind it | Penn State METEO 3 (trough minimum) | Wikipedia "Cold front"; UCAR "Weather fronts" (falling to rising) | yes |
| With moist air a cold front brings a narrow band of showers or storms | Wikipedia "Cold front" | UCAR "Weather fronts"; NWS Louisville (moist air rains, unstable air storms) | yes |
| A cold front can pass with little or no rain when the air is dry | Wikipedia "Cold front" | NWS Louisville (rain only if the air is moist) | yes |
| Cold fronts move faster than warm fronts | UCAR "Weather fronts" | Wikipedia "Warm front" | yes |
| Warm air rises slantwise over cold air; clouds and rain ahead of a warm front | NWS Louisville | Wikipedia "Warm front"; UCAR | yes |
| Warm front clouds: cirrus first, then lower and thicker | UCAR "Weather fronts" | Wikipedia "Warm front" | yes |
| Warm front wind from SE ahead, SW behind; gradual warming; pressure falls ahead, steady after | Wikipedia "Warm front" | Navy aerographer manual (NWS-derived), "Frontal systems" | yes |
| Cold front steep (about 1:100 near the ground); warm front gentle (about 1:200) | Penn State METEO 3 | Wikipedia "Warm front" | yes (each gives one slope; screen says steep and gentle, the drawing uses the numbers) |
| cP cold dry from Canada; mT warm humid from the Gulf; cT hot dry from the desert Southwest and northern Mexico | UCAR "Air masses" | Oklahoma Climatological Survey "Air masses"; UW-Madison AOS "Air masses" | yes |
| Air flows from high pressure toward low pressure | NOAA SciJinks "Why does the wind blow?" | UCAR "Why the wind blows" | yes |
| Wind direction is where the wind comes from | NWS glossary "wind direction" | NOAA SciJinks | yes |
| Dew point is the temperature air must cool to for saturation; higher means more moisture | NWS glossary "dew point" | NWS La Crosse "Dew point vs humidity" | yes |
| A dry line separates moist and dry air on the Plains; storms can form along it | NWS glossary "dry line" | Wikipedia "Dry line" | yes |
| Chance of rain means the chance of measurable rain (0.01 in) at a point | NWS Peachtree City "PoP" | Wikipedia "Probability of precipitation" | yes |
| Forecasters run many slightly different forecasts; the spread shows how sure they are | NOAA PSL "Ensemble forecasts" | Penn State "A World of Weather" s12 | yes |
Backed twice: 18. Cut: real front speeds in km/h (no two sources gave matching numbers; the tool's speeds are labeled
model ranges in notes), the dry line's 13 °C dew point marker (one source), air-mass names on screen beyond the plain
words plus the code in small type.
Number checks (Python 3, 2026-11-07, model coded as in Content): 30,000 days (10,000 per type): 2 to 4 passed stations
on every day; careful marking (first reading with the wind turned over 45 degrees) plus a least-squares line and a 3 h
window centered on its Elm Grove crossing: Storm 0.966, Dry 0.967, Warm 0.926 pass; random 3 h window 0.116 to 0.128;
"6 to 9 pm" 0.003 to 0.132; best fixed window in hindsight 0.30 (Storm, now+3.5 h), 0.30 (Dry), 0.22 (Warm);
"one gap after last mark" 0.06 to 0.22; last two marks only 0.93 to 0.97. Ten-day spread at most 2.9 h, so 3 h can
catch all ten. Temperature answers on every draw: c 12 = -13, c 6 = -7, Warm +8 or +12. Rain bands: station share
and ten-day count agree on every draw. Pressure 1000 to 1018 mb, temperature 5.5 to 31 °C over all readings. Day 1:
marks 9:30 am, 1:00 pm, 4:30 pm; line 34.3 km/h crossing at 11:30 pm; ten days 10:38 pm to 11:26 pm, all inside
10 pm to 1 am. Half-hour readings were chosen because hourly ones dropped careful Warm days to 0.72.

## Done when
1. Focus: in Read the station row and growing chart are the biggest things; in Forecast the tracker replaces the
   chart; at 1366x768 cards, chart and every step control sit above the fold with no scroll.
2. Collect: after Auto-read to 6 pm each station has 37 readings and the charts plot only logged ones.
3. Motion: on Day 1, marks at 9:30 am, 1:00 pm, 4:30 pm and a line through them cross Elm Grove at 11:30 pm and a
   10:30 pm to 1:00 am window shows "caught 10 of 10".
4. Probability: a 3 h window placed 6 to 9 pm on Day 1 shows 0 of 10 and "Not verified"; rain row shows N of 10.
5. Interactions: all nine Side view pairs draw a different picture and say their own line; desk verdict names the pair.
6. High to low: Big picture tap on H says bigRight; L and the front give their reasons; one try.
7. A tap while anything plays (Auto-read, the next-day run, Side view) changes the view at once; Pause stops it.
8. Nothing before Check shows arrival: no ten-day ticks, no true dots, no auto line, charts end at 6 pm.
9. Day locks after Check; New day gives different passage times.
10. 680x425: each step's main buttons are visible; folded items reachable by tap.
11. Voice: a five-action run speaks each how line at most once; no line names a disabled control.

## Open questions
- A fifth "real day" built from archived hourly station data (for example a spring cold front across Kansas from the
  Iowa Environmental Mesonet ASOS archive) would add real material (BASELINE rule 9) but means picking an event and
  five real stations. Worth a later round?
