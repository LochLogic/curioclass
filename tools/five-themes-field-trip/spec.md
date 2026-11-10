# Five Themes Field Trip

## One idea
On a field trip through New Orleans, a river city built on the high ground beside the Mississippi, the child visits five stops (the French Quarter on the natural levee, a neighborhood below sea level, the riverfront port, a floodwall and pump station, the wetlands at the city's edge), tags each stop's photo with one of the five themes of geography, and builds their own map of the city layer by layer (a location grid, place symbols, a region they draw, movement arrows, human-environment marks); then they compare real satellite images decades apart, turn one layer into a chart (ground height along a line from the river to the lake), and write one sentence linking where people built to what the land is like, so a sixth grader learns to make and read maps that explain a place.

## Not like
- region-compare (6, spec): data across world regions. Here one city up close.
- the-shrinking-lake (6, spec): one change over sixty years on a timeline. Here building a layered map.
- layers-and-scales (9, concept): class breaks and map scale. Here making a first layered map.
- map-maker (3, spec): a made-up island with key and scale. Here a real city and real images.

## Who and how
- Grade 6, Social Studies (Geography), module "Five Themes of Geography". Standards: D2.Geo.1.6-8 (construct maps to represent and explain the spatial patterns of cultural and environmental characteristics), D2.Geo.2.6-8 (use maps, satellite images, photographs, and other representations to explain relationships between the locations of places and regions and changes in their environmental characteristics), D2.Geo.3.6-8 (use paper based and electronic mapping and graphing techniques to represent and analyze spatial patterns of different environmental and cultural characteristics).
- Format: the idea card changes it from explorer to map, because all three codes ask the child to make and read maps.
- Driver: one child alone (tool.json `driver: "student"`). `Read` reads every note. Controls 44 px or more.
- Five stops, the then-and-now images, the chart layer and the sentence. Extra: a second river city, St. Louis, with the same toolkit. tool.json `modes: ["New Orleans", "St. Louis"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.1.6-8 | Place a symbol for each stop on the blank base map and add one layer per theme (grid, place symbols, a drawn region, movement arrows, interaction marks) | the child's own layered map with a key they build | 2 |
| D2.Geo.2.6-8 | Compare a then-and-now satellite pair and photos, and pick what changed and why | the image pair with a slider; the change chips | 3 |
| D2.Geo.3.6-8 | Turn the elevation layer into a line chart from river to lake, and choose symbols for each layer | the chart; the key | 4 |
| D2.Geo.1.6-8 (explain) | Write one sentence linking where people built to the land | the sentence card with the map beside it | 5 |

## Screens and modes
Header (kit): title "Five Themes Field Trip"; `New Orleans`, `St. Louis`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A nearly blank outline: the Mississippi's curve, Lake Pontchartrain to the north, the city edge, and a trip ticket listing five stops, each with a theme stamp still blank. The welcome is queued (`welcomeAfter: true`): "Today's field trip is New Orleans. At each stop you'll take a photo and add it to a map you build yourself. Tap the first stop on your ticket." First hint: "Tap Stop 1 on the ticket."

**The stops (focus: the photo and the map).** At 1366x768 the map fills the right two-thirds with the photo and guide note on the left; at 680x425 the map and photo swap with tabs.
1. The French Quarter on the natural levee (Location). Guide note: the city was founded here in 1718 on the highest ground near the river, a few feet above sea level. The child adds a latitude and longitude grid and places a star at about 29.96 N, 90.06 W.
2. A neighborhood below sea level (Place). Guide note: much of the city sits below sea level, some neighborhoods several feet below, kept dry by levees and pumps. The child places a place symbol and picks two place details (low ground, houses raised on piers).
3. The riverfront port (Movement). Guide note: ships carry grain, oil and goods up and down the river and out to the Gulf. The child draws movement arrows for ships, roads and rail.
4. A floodwall and pump station (Human-environment interaction). Guide note: people built levees, floodwalls and pumps to live on low land; in 2005, after Hurricane Katrina, floodwalls and levees failed and about 80 percent of the city flooded. Teacher note offered. The child places interaction marks (levee, pump, floodwall).
5. The wetlands at the city's edge (Region). Guide note: coastal Louisiana has lost about 2,000 square miles of land since the 1930s. The child draws a region boundary around the wetlands and names it.
- At each stop the child tags the photo with one theme from five stamps; a wrong stamp plays "Which question does this photo answer: where, what is it like, how do things move, how do people change the land, or what makes this area one region?"

**Then and now (focus: the satellite pair).** A slider moves between a Landsat image of the delta in the 1980s and a recent one: open water where marsh was, and the city's growth toward the lake. The child picks what changed (land lost, city grew, river path same) and why (from chips: levees keep river mud from building marsh, canals let salt water in, sea level rising, the land sinking).

**The chart layer (focus: the elevation line).** The child draws a line across the map from the river to the lake; a chart plots ground height along it (high by the river, dipping below sea level in the middle, low near the lake). The child picks which places sit high and low and what was built there first.

**The end.** The child's finished map, its key, the chart, and the sentence card: "People built first on ___ because ___." (tiles plus a free line). Narrator: "Your map shows why the old city sits by the river. The land decided first." `Print` prints the map, key, chart and sentence.

**St. Louis (extra).** Five new stops (the riverfront and Gateway Arch, the floodwall, the confluence with the Missouri, an old brick neighborhood, the bluffs) with the same toolkit.

## Content
- Five stops with photos and notes, five layer tools, a then-and-now satellite pair, an elevation profile from public data, chips and tiles, the St. Louis set.
- All places, images and facts are real; heights are rounded and labeled "about".
- Katrina is named with what happened and a teacher note; no images of people in danger.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Layers can be shown or hidden from the key; each layer's symbol can be swapped from three choices.
- The region is drawn by tapping points around it (or Enter on grid squares with the keyboard).
- Keyboard: Tab to the ticket, tools and map; arrows move a symbol; Enter to place.
- With Motion off the slider jumps between images without fading.

## Look
- Accent `--brand` #1d5c63 bayou teal (header, ticket, the child's symbols); gold #f4c542 (the current stop, the chart line); paper #eef5f6; ink #062023; muted #4a5859.
- Contrast (WCAG 2.1, computed): white on brand 7.60:1; brand on paper 6.89:1; ink on paper 15.36:1; muted on paper 6.72:1; ink on gold 10.42:1.
- Never color alone: each layer has its own symbol shapes and a key; below-sea-level ground is hatched as well as tinted.
- Different from this batch (river green, museum terracotta, smoke slate, lake blue).

## Art
- Public domain: USGS and NASA Landsat images of the Mississippi delta and New Orleans, two dates (picked at build from USGS EarthExplorer or NASA Earth Observatory); Library of Congress photos for the French Quarter and the riverfront; the USGS land-loss map of coastal Louisiana. Each with credit.
- Local FLUX (`scripts/localart.py`): only if a stop lacks a public-domain photo (the pump station, 1, 3:2).
- People art goes to Gemini with `people: true`: the trip guide (1, cutout yes).
- Drawn in code: the base map, grid, symbols, region, arrows, the chart.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the trip guide and note reader; `casual-peer` as a classmate, Andre (made for this game), who asks the theme questions. `Curio.voice` with `scope: () => state.mode + ':' + state.stop + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each guide note.
- how `tag`: "Stamp the photo with one theme."
- how `layer`: "Add this stop to your map with the tool shown."
- how `slider`: "Slide between the two images, then pick what changed."
- how `chart`: "Draw a line from the river to the lake."
- how `sentence`: "Finish the sentence about where people built first."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the base map with five layer tools and a built key, the image slider, the elevation profile chart, the sentence card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Theme stamps | Try stamps until one sticks | The guiding question plays after each miss; the map key records only first-try themes for the teacher view. |
| Layers | Drop symbols anywhere | Each symbol must land in its stop's area; the star must land near the right grid square. |
| Chart | Draw any line | The line must touch the river and the lake; the chart then shows the real profile. |
| Sentence | Leave it blank | Print waits for the blanks. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Guide note (whole), waits.
2. `tag`; `layer`, for each stop.
3. `slider`; `chart`.
4. `sentence`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.1.6-8, D2.Geo.2.6-8 and D2.Geo.3.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The five themes of geography: location, place, human-environment interaction, movement, region | NCGE and AAG, "Guidelines for Geographic Education" (1984) | National Geographic Education, "Five themes of geography" | yes |
| New Orleans founded 1718 on high ground by the river | Encyclopaedia Britannica, "New Orleans" | The Historic New Orleans Collection, "New Orleans founding" | yes |
| Much of the city lies below sea level | USGS, "New Orleans elevation" (LiDAR study) | NASA Earth Observatory, "New Orleans sinking" | yes |
| After Katrina (2005) levees and floodwalls failed and about 80 percent of the city flooded | NOAA National Hurricane Center, Katrina report | U.S. Army Corps of Engineers, IPET report summary | yes |
| Coastal Louisiana lost about 2,000 square miles of land since 1932 | USGS, "Land area change in coastal Louisiana, 1932 to 2016" (2017) | NOAA, "Louisiana coastal land loss" | yes |
| Causes of land loss: levees stop river sediment, canals, sinking, sea-level rise | USGS (2017) | Coastal Protection and Restoration Authority of Louisiana, Master Plan | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: Hurricane Katrina is named with what happened (the levee failures and flooding) and a teacher note; there are no images of people in danger, and the tour stays on land and building choices. A fresh-agent read of the stop notes is needed before build.

Checks run (Python, scratchpad r11, 2026-11-09): five stops map one-to-one to five themes; the star at 29.96 N, 90.06 W falls in the French Quarter grid square; 1718 to 2005 is 287 years; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and photo side by side; at 680x425 tabs.
2. Each stop adds one layer and the key builds itself. (D2.Geo.1.6-8)
3. The satellite slider and change chips work. (D2.Geo.2.6-8)
4. The elevation chart plots along the child's line. (D2.Geo.3.6-8)
5. The sentence card prints with the map. (D2.Geo.1.6-8)
6. St. Louis loads its own five stops.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fading; no network requests (images and the profile are bundled).

## Open questions
- Sensitivity flag: New Orleans means Hurricane Katrina, which some students' families lived through (default used: named plainly with a teacher note, no images of people in danger, fresh-agent read before build).
