# Emerging Tech Pitch

## One idea
A new technology only helps the people it can reach: build a concept for a made-up valley town by picking an emerging technology and a few add-ons, and a grid of the town's 100 households lights up house by house with who it reaches and who it leaves out (the canyon ranches with no cell signal, the deaf family a siren can't wake, the grandparents with flip phones), right beside the old fix it would replace, its cost and its energy, until you can pitch it honestly.

## Not like
- data-policy-council (9-12 CS): redraws one student's day as a data trail under a policy. Here nothing is about one person's data; the question is reach and cost across a whole town, house by house.
- ai-evaluator (9-12 CS): measures a trained model's accuracy by district on a map. Here no model is tested; you design a concept and see which households its needs (signal, smartphone, hearing, English) shut out.
- network-architect (9-12 CS): wires a building and runs network tests. Here the infrastructure is a choice between whole technologies, compared on what they need from people.
- api-playground (9-12 CS): builds an app from APIs. Here nothing is coded; the made thing is a concept and a pitch sheet.
- sprint-board (this group): a team builds a bus-alert app over sprints. This tool stays at the concept stage, compares technologies, and has no bus brief on purpose (the concept's "late buses" example moved to sprint-board's client).
- cloud-through-time (this group): energy and labor over 80 years of one technology. Here energy is one column in a present-day cost check.
- game-remix (grade 5, studio): changes a working game. Here the studio makes a concept sheet, not a program.

## Who and how
- Grades 9 to 12, computer science. Module: Emerging Technology Review (Computing and Society), "How an emerging technology differs, who it helps or harms, and a concept design". Topic line: "comparing emerging and established technology".
- Driver: students on laptops, alone or in pairs; the Pitch view can go on the projector for the class to question. 25 to 45 minutes (one brief about 15 minutes).
- Standards (module codes, CSTA 2026): HS-SOC-ET-40, HS-SOC-ET-41, HS-SOC-ET-42. ET-40 is the Compare view (how the emerging technology differs from the established one), ET-41 the reach grid and the benefit and harm cards (who it helps or harms), ET-42 the Build and Pitch views (a concept design). CSTA 2017 crosswalk: 3B-IC-25 (evaluate artifacts to maximize benefits and minimize harms), 3B-IC-26 (equity and access in the distribution of computing resources), 3B-IC-27 (predict how computational innovations might evolve).
- tool.json: driver "students", minutes "25-45", modes ["Brief", "Compare", "Build", "Pitch"], grades_label "Grades 9-12". Kit starter, `kit:theme-912`.

## Screens and modes
Header (kit): "Emerging Tech Pitch", small line "Cedar Gap, a made-up valley town". Mode buttons: **Brief** (opens first), **Compare**, **Build**, **Pitch**. Motion, Sound, Read. All four are open from the start; Compare, Build and Pitch use the brief picked in Brief (default Smoke alerts).

Focus: in Brief and Build, the **household grid**, centered and the largest thing on the stage; in Compare, the three option columns; in Pitch, the pitch sheet. A painted banner of Cedar Gap (Art) runs as a thin strip above the grid in Brief and heads the pitch sheet.
Stage, every mode except Pitch: the **household grid**, 10 by 10 squares, one per household, grouped in seven labeled blocks (group name and count beside each block, Content). Each square shows the state for the current concept: **reached** (filled, brand coral, a ✓), **left out** (outline only, a small ✕). Under the grid one line: "Reached 72 of 100 households" and the left-out groups as chips ("Canyon, older, no car 8"). Tap a group label: a card with its row of needs (signal, smartphone, any cell phone, home internet, hears a siren, reads English, car, lives in town) as ✓ and ✕.

### Brief
Panel: three brief cards (radio), each with its painted thumbnail (Art): **Smoke alerts** ("Wildfire smoke rolls into the valley at night. Who gets warned within 30 minutes?"), **Library books** ("The only library is in town. Who can get a requested book within a week?"), **Town meetings** ("The council meets Tuesdays at 7 pm. Who can follow it live?"). Under the picked card: the goal line and the town note "Cedar Gap is made up. Its 100 households stand for the kinds of homes many rural towns have." Grid: the established fix's reach.

### Compare
Stage: three columns, one per option of the brief: the established fix and two emerging ones, each headed by its painted option picture (Art). Rows: **How it works** (one line), **Needs** (need chips), **Works in a power outage** (yes / partly / no with a word), **Data it collects**, **Who keeps it running**, **Fact** (one sourced fact card, Content). Under each column a mini grid (100 dots) with its reach number. Panel: **Show differences only** (hides rows where all three match) and the sources drawer for the fact cards.

### Build
Panel, top to bottom:
- **Core** (radio, three options from the brief, each with a small thumbnail of its option picture).
- **Add-ons** (checkboxes, the brief's list, each with its cost line and effect line, for example "Spanish messages too: households that read Spanish best can now use it").
- **Impact check** (`dl.readouts`): Reached, Setup cost, Yearly cost, Energy per year, Works in an outage, Data collected. Each number shows the difference from the established fix in small type ("+12 households", "+$15,000 a year").
- **Benefit and harm**: the core's two benefit cards and two harm cards (Content), each with a **Pin** button; pinned cards go on the pitch sheet (up to 2 of each).
Stage: the grid updates live; a ghost outline shows the established fix's reach so the change is visible. Changed squares pulse once for 400 ms (not with Motion off); a tap during a pulse acts at once, and the grid shows the newest state.

### Pitch
Stage: the pitch sheet, drawn as one page: the Cedar Gap banner, title "Cedar Gap: [brief]", the core's option picture, the concept as a block diagram drawn in code (Sense, Decide, Deliver, Backup boxes filled from the core and add-ons, Content), the reach grid small, the impact table beside the established fix's numbers, the pinned benefits and harms, and an automatic **Who it still leaves out** line. Panel: **Present** (full screen, panel hidden, Escape returns), **Copy pitch text** (plain text to the clipboard), **Save on this device** and **Clear saved** (localStorage, the choices only, no text), **Start over**.

## Content
Households (made up; columns: in town, cell signal at home, smartphone, any cell phone, home internet, hears a siren, reads English, car):
| Group | n | town | signal | smart | phone | internet | hears | English | car |
|---|---|---|---|---|---|---|---|---|---|
| Town, connected | 40 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Spanish-first families | 12 | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | ✕ | ✓ |
| Older, flip phones | 8 | ✓ | ✓ | ✕ | ✓ | ✕ | ✓ | ✓ | ✕ |
| Deaf or hard of hearing | 6 | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | ✓ |
| No car | 10 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| Canyon ranches | 16 | ✕ | ✕ | ✓ | ✓ | ✕ | ✓ | ✓ | ✓ |
| Canyon, older, no car | 8 | ✕ | ✕ | ✕ | ✓ | ✕ | ✓ | ✓ | ✕ |
"Reads English": Spanish-first households read Spanish best. "Hears a siren" is about hearing, not distance; distance is "in town".

Each option reaches a household when the household has every need in at least one of its need sets (sets joined by "or"). Add-ons work in three ways: **waive** a need for every set, **give** a need to households (all, or canyon only), **keep the old fix** (the established fix's sets join with "or"). Costs and energy are Cedar Gap estimates, made up for this town except where a fact card gives a source.

**Smoke alerts** (all 100 households; goal: warned within 30 minutes, day or night)
| Option | Needs | Reach | Setup | Yearly | Energy kWh/yr | Outage | Data |
|---|---|---|---|---|---|---|---|
| Outdoor sirens (established) | town and hears | 70 | $0 (owned) | $2,400 | 300 | yes (battery backup) | none |
| Air sensors with text alerts | signal and phone and English | 64 | $5,000 (20 sensors) | $2,200 | 350 | partly (cell towers may fail) | air readings, phone numbers |
| Satellite internet and an alert app | smartphone and English (dishes give canyon homes internet) | 72 | $20,400 (24 dishes, app) | $15,000 | 12,600 | no (dish needs home power) | phone numbers, app location if allowed |
Add-ons: Spanish messages too (waive English; $0, +$400/yr). Strobe and bed-shaker kits (waive hears; $900 setup). Loan smartphones to 16 homes (give smartphone to all; $3,200 setup, +$2,880/yr). Keep the sirens (keep old fix; +$2,400/yr, +300 kWh).
Block diagram: Sense (sirens: "fire office sees smoke"; sensors: "20 air sensors read fine particles"; satellite: "fire office sees smoke"), Decide ("alert when the air quality index passes 150"), Deliver (siren / text / app), Backup (add-ons).

**Library books** (all 100; goal: a requested book within a week)
| Option | Needs | Reach | Setup | Yearly | Energy kWh/yr | Outage | Data |
|---|---|---|---|---|---|---|---|
| Weekly bookmobile (established), stops in town and at the canyon fire hall | town, or car | 92 | $0 (owned) | $38,000 | 48,300 (1,200 gallons of diesel) | yes | library card holds |
| Drone drop from the library roof | town (the drone must stay in sight) | 76 | $30,000 | $9,000 | 450 | no | holds, home drop spot |
| Satellite hotspots to borrow e-books | smartphone (the hotspot gives internet) | 84 | $6,000 (10 kits) | $10,000 | 880 | no | holds, e-book reading data |
Add-ons: Volunteer drivers (give car to all; $0, +$1,500/yr). Loan e-readers to 16 homes (give smartphone to all, for e-books; $1,920 setup). Keep the bookmobile (keep old fix; +$38,000/yr, +48,300 kWh).

**Town meetings** (all 100; goal: follow the meeting live)
| Option | Needs | Reach | Setup | Yearly | Energy kWh/yr | Outage | Data |
|---|---|---|---|---|---|---|---|
| Meeting at town hall (established) | (town or car) and hears and English | 74 | $0 | $500 | 200 | no lights after dark | none |
| Live video stream | smartphone and (signal or internet) and hears and English | 50 | $3,000 | $1,200 | 15 at the hall | no | viewer counts |
| Stream with on-device captions and translation | smartphone and (signal or internet) | 68 | $5,000 | $1,200 | 15 at the hall | no | viewer counts; captions made on each phone |
Add-ons: ASL interpreter (waive hears; +$2,400/yr). Spanish interpreter (waive English; +$2,400/yr). Satellite dishes for canyon homes (give home internet to canyon households; $14,400 setup, +$14,400/yr, +12,600 kWh). Loan smartphones to 16 homes (as above). Keep the meeting at town hall (keep old fix).

Checked reaches (computed with the rules above; the build reproduces every one):
- Smoke: sensors + Spanish 76; sensors + Spanish + keep sirens 76 (still not the canyon); satellite + Spanish 84; satellite + Spanish + loan smartphones 100; sirens + strobe kits 76.
- Library: drone + keep bookmobile 92; drone + keep bookmobile + volunteer drivers 100; hotspots + loan e-readers 100; bookmobile + volunteer drivers 100 (no setup cost, $39,500 a year; hotspots + e-readers reaches 100 for $7,920 setup and $10,000 a year, so neither is simply "cheapest").
- Meetings: captions + canyon dishes 84; captions + canyon dishes + loan smartphones 100; stream + ASL + Spanish interpreters 68; town hall + both interpreters 92; captions + keep town hall 92.
Energy and costs add up across core and add-ons, with "keep the old fix" adding the established fix's numbers.

Benefit and harm cards (two each per option; examples, all written in the build from these lines):
- Sirens: benefit "Works with no phone and in a power outage." harm "Can't reach the canyon or wake a deaf household."
- Air sensors: benefit "Measures the air where people live, not one spot." harm "Low-cost sensors drift and need checking against a reference monitor."
- Satellite alert app: benefit "Brings internet to homes the cell towers miss." harm "Monthly fees and about 12,600 kWh a year for 24 dishes."
- Bookmobile: benefit "A librarian meets readers in person." harm "Once a week, and it burns diesel."
- Drone drop: benefit "Same-day delivery in town." harm "Noise and a camera over yards; it can't fly to the canyon homes that need it most."
- E-book hotspots: benefit "Any book, any night." harm "Only e-books, and only for readers with a screen."
- Video stream: benefit "Watch from home, no drive at night." harm "Leaves out anyone who can't hear it or read English."
- On-device captions: benefit "Captions and translation made on the phone, so the audio isn't sent away for captions." harm "Captions make mistakes, most often with names."
Fact cards (one per emerging option; sources in Sources):
- Air sensors: "The EPA's Fire and Smoke Map shows readings from low-cost sensors after applying a correction."
- Satellite: "Low Earth orbit is below 2,000 km. Older internet satellites sit in geostationary orbit, 35,786 km up, so signals take longer."
- Satellite (energy): "A home satellite internet dish draws about 50 to 75 watts on average." (used for the 60 W figure: 24 dishes x 60 W x 8,760 h = 12,614 kWh, shown as 12,600)
- Drone: "Under the FAA's small drone rule, the pilot must keep the drone in sight, fly no higher than 400 feet, and the drone must weigh under 55 pounds. Flying beyond sight needs a waiver."
- Bookmobile energy: "A gallon of diesel holds about 137,381 Btu, about 40.3 kWh." (1,200 gallons = 48,300 kWh)
- On-device AI: "An on-device model runs on the phone itself, so it can work without a connection."
- Smoke threshold: "An air quality index above 150 is 'Unhealthy' for everyone."

## Interactions in detail
- Everything recomputes on every change; no Run button. Reach counts are whole households; nothing is random.
- Picking a new core keeps the add-ons that fit the new brief; switching briefs clears the add-ons and the pins (with a one-line "Add-ons cleared for the new brief").
- An add-on that changes nothing for the current core (strobe kits with the satellite app: the app already ignores hearing) stays checkable, adds its cost, and shows "Reaches no one new with this core" in its effect line. This is on purpose: spending that helps no one is part of the lesson.
- "Keep the old fix" is hidden when the core is the established fix.
- Group card: needs the current concept fails for that group are underlined, so "why left out" is one tap away.
- Pins: a third pin of the same kind replaces the oldest, with a note. Pitch shows "Pin a benefit and a harm in Build" when none are pinned.
- Pitch "Who it still leaves out": the left-out groups with counts, or "Every household is reached. Check the cost." when reach is 100.
- Copy pitch text: brief, core, add-ons, reach, costs, energy, pinned cards, left-out line. No typed text exists anywhere.
- Save on this device stores the brief, core, add-ons and pins for each brief; Clear saved removes them. Nothing else is stored.
- Keyboard: modes, then panel controls, then the grid group labels (arrow keys between groups, Enter opens the card). Visible focus.
- Sizes: at 1366x768 and 1280x720 the grid, the core picker and the Impact check fit without scrolling; at 680x425 the grid becomes a compact 20 by 5 strip and the panel shows Core and Reached only, with the rest in a "More" drawer. Grid squares at least 14 px at full screen; group labels at least 12 px.

## Look
- Accent `--brand #ff8a7a` (warm coral: reached squares, Build controls, the header rule) with `--brand-ink #2a0d08`, on `kit:theme-912`.
- Grid: left-out squares outline `#a6b3c4` with ✕; ghost outline of the established fix's reach dashed `#62789a`. Pitch sheet: a light card `#fbfaf7` with ink `#1c1f26` and coral rules, so it reads like a handout.
- Contrast (computed): brand on `--panel #141b25` 7.56:1, on `--sec-bg #18202b` 7.16:1; brand-ink on brand 7.91:1; outline grey on panel 8.13:1; ghost outline 3.85:1 (graphics need 3:1); pitch ink on its card about 16:1. All pass AA. Reached and left out differ by fill and glyph, never color alone.
- Neighbors: ai-evaluator and capture-the-flag pink, sorting-showdown violet, api-playground lemon, network-architect sky blue, simulation-studio orange, data-policy-council navy on paper. Coral is unused in 9-12 computer science.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: warm painted illustration of a small western valley town, late-day light. Objects that usually carry text (signs, vans, screens) are asked for blank; any words go on in code.
- cedar-gap-banner: "A small valley town in the American West seen from a hillside, a main street of low buildings, a water tower, ranch houses scattered up a pine canyon beyond, late afternoon light, painted illustration"; 4:1; cutout no; people no; strip above the grid in Brief and the head of the pitch sheet.
- brief-smoke: "Wildfire smoke rolling into a quiet valley town at night, porch lights glowing through haze, painted illustration"; 4:3; cutout no; people no; Smoke alerts brief card.
- brief-library: "A small brick town library with a blank sign over the door and a book drop box, evening, painted illustration"; 4:3; cutout no; people no; Library books brief card.
- brief-meeting: "A small-town hall with lit windows at dusk and a flagpole, painted illustration"; 4:3; cutout no; people no; Town meetings brief card.
- Option pictures, one shared prompt "[object], painted illustration, warm light, plain soft background" with: opt-sirens "an outdoor warning siren on a tall wooden pole above rooftops"; opt-sensors "a small white air quality sensor box mounted on a fence post"; opt-satellite "a flat satellite internet dish on the roof of a ranch house in a canyon"; opt-bookmobile "a bookmobile van with blank sides parked by a rural fire hall"; opt-drone "a delivery drone carrying a small package over town rooftops"; opt-hotspots "a portable internet hotspot and a tablet with a blank screen on a kitchen table"; opt-hall "rows of empty folding chairs facing a table in a town hall meeting room"; opt-stream "a phone on a small tripod at the back of a town hall meeting room, its screen blank"; opt-captions "a phone with a blank screen propped against a sugar bowl on a kitchen table at night"; 4:3 each; cutout no; people no; Compare column heads, Build's core thumbnails and the pitch sheet. Captions and stream text appear in code over the blank screens.
The household grid, need chips, group cards, the block diagram, the impact table and preview.svg are drawn in code (data, diagrams and labels).
## Voice
Bank voice `upbeat-guide` (Zephyr), style "Say brightly and clearly, like an upbeat tour guide": a friendly guide showing a pitch team around the town. Not used by any 9-12 computer science tool or group sibling. Light narration, `Curio.voice`, `scope: () => state.mode + ':' + state.brief`. Read speaks the hint. Numbers are never spoken.
- w-brief (how, Brief welcome; stale when another mode opens): "Tap a problem card in the panel. Then press Compare to see the old fix and two new ones side by side."
- w-compare (how, Compare welcome; stale when another mode opens): "Three ways to solve one problem. Press Show differences only to see what sets them apart."
- w-build (how, first visit to Build; stale on the first core or add-on change): "Tap a core technology, then tick add-ons. Watch which houses light up."
- all (event, reach rises to 100 for the first time in a brief; stale if reach drops before it plays): "Every household is reached. Now look at what it costs."
- noone (event, an add-on reaches no one new with this core; stale when it is unticked or the core changes): "That add-on costs money but reaches no one new here."
- w-pitch (how, first visit to Pitch; stale on Present): "This is your pitch. Press Present to show the class, and be ready to say who it still leaves out."
## Family engine
none

## Sources
- CSTA 2026 PK-12 Computer Science Standards (statements read for the gap fill): https://csteachers.org/2026-csta-pk-12-computer-science-standards/ ; CSTA K-12 Computer Science Standards (2017): https://csteachers.org/k12standards/
- Low-cost sensors on the Fire and Smoke Map, with correction: EPA AirNow, "Fire and Smoke Map" and EPA, "Sensor data on the Fire and Smoke Map": https://www.airnow.gov/fires/ and https://www.epa.gov/air-sensor-toolbox
- AQI categories (151 to 200 "Unhealthy"): EPA AirNow, "AQI Basics": https://www.airnow.gov/aqi/aqi-basics/
- Low Earth orbit below 2,000 km: ESA, "Types of orbits": https://www.esa.int/Enabling_Support/Space_Transportation/Types_of_orbits ; geostationary 35,786 km: same page.
- Dish power about 50 to 75 W average: a satellite internet maker's published specifications for its standard home dish (brand kept off screen): https://www.starlink.com/specifications
- FAA small drone rule (Part 107: visual line of sight, 400 feet, under 55 pounds, waivers): https://www.faa.gov/uas/commercial_operators
- Diesel heat content 137,381 Btu per gallon: U.S. EIA, "Units and calculators explained: British thermal units": https://www.eia.gov/energyexplained/units-and-calculators/british-thermal-units.php ; 1 kWh = 3,412 Btu (same source).
- On-device AI works without sending data to a server: Chrome for Developers, "Built-in AI": https://developer.chrome.com/docs/ai/built-in
- Cedar Gap, its households, every cost and every other energy figure are made up; reaches were computed with the rules above.
- Checks run (Python, 2026-10-29, the needs rules above on the seven groups): every reach in the option tables and in "Checked reaches", with the left-out groups in Done when; Smoke satellite + Spanish + loan smartphones setup $23,600, yearly $18,280; 16 households lack a smartphone (so "loan to 16 homes" covers them); 24 dishes x 60 W x 8,760 h = 12,614 kWh; 1,200 gallons x 137,381 Btu / 3,412 = 48,317 kWh. The draft called bookmobile + volunteer drivers "the cheapest 100", but hotspots + e-readers costs less a year, so that note now gives both. Contrast recomputed: the outline grey is 8.13:1 (the draft said 8.6), the ghost outline 3.85:1 (graphics need 3:1).

## Done when
1. Brief, Smoke alerts: the grid shows 70 reached; deaf, Canyon ranches and Canyon older are left out.
2. Compare shows three columns with needs chips; mini grids read 70, 64, 72; Show differences only hides no row (all differ) for Smoke.
3. Build, Smoke, satellite core: 72; add Spanish 84; add loan smartphones 100, line 3 plays once; the Impact check reads setup $23,600, yearly $18,280.
4. Build, Library, bookmobile + volunteer drivers: 100, setup $0, yearly $39,500, energy 48,300 kWh.
5. Build, Meetings, captions + canyon dishes: 84; Older flip phones and Canyon older left out. Checking ASL interpreter with the captions core adds $2,400 a year, shows "Reaches no one new with this core", and line 4 plays.
6. Library drone core: 76; tap the Canyon ranches label: "town" is underlined.
7. Pitch shows the block diagram, the pinned cards and the left-out line; Present hides the panel; Copy pitch text contains no typed text.
8. Save, reload: choices return; Clear saved: they are gone.
9. Grid, core picker and Impact check fit without scrolling at 1366x768; every voice how-line plays once in five changes.
10. Focus: at 1366x768 and 1000x625 the household grid is the largest thing on the stage in Brief and Build; Compare's three columns and Pitch's sheet fill theirs.
11. Tap while it plays: ticking two add-ons inside one 400 ms pulse shows the reach for both at once; no change waits for a pulse or a voice line.

## Open questions
- [emerging-tech-pitch] The concept's "late buses" brief became "Town meetings" so it doesn't repeat sprint-board's bus-alert app. OK?
- [emerging-tech-pitch] The pitch has no free-text box (concept name, notes): students pitch out loud. Add an unsaved text box, or keep it out?
