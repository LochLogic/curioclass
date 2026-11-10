# Map Maker

## One idea
The child gets a satellite-style picture of an island they have never seen (a deep cove on the west coast, a shallow sandy beach on the east, a river running down from the hills through flat green land, a forest and a swamp) and a blank map sheet beside it, traces the coast and river onto the sheet, places a port, a market, homes and farms where the land suits them (each with a reason check), adds a key, a scale bar and grid letters, then hands the map to Nia the traveler, who follows it on three errands and shows step by step where a missing symbol, a wrong scale bar or a mixed-up grid would get her lost, so a third grader learns to build a map that works for someone else and to read land from a picture from above.

## Not like
- compass-rose-quest (1, spec): directions on a park grid with clues. Here the child builds the whole map with key, scale and grid.
- me-on-the-map (K, built): levels of place from room to planet. Here one made-up island, mapped from above.
- then-and-now-overlay (3, spec, this batch): reading old maps as sources. Here making a new map.
- state-economy-map (4, concept): industries on a real state map. Here a made-up island and why things sit where they do.

## Who and how
- Grade 3, Social Studies (Geography), module "Map Skills and Regions". Standards: D2.Geo.1.3-5 (construct maps and other graphic representations of both familiar and unfamiliar places), D2.Geo.2.3-5 (use maps, satellite images, photographs, and other representations to explain relationships between the locations of places and regions and their environmental characteristics).
- Driver: one child alone (tool.json `driver: "student"`); `Read` reads every label and line. Controls 44 px or more.
- Four parts: Trace, Build, Key and grid, Nia's trip; then the extra My school map. tool.json `modes: ["Island", "My school map"]`, `minutes: "25-35"`, `grades_label: "Grade 3"`.
- Family: me-map (map sheet, place markers, the zoomed view). No engine doc exists yet; this spec names the parts it adds.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.2.3-5 | Read the picture from above to find the deep cove, the flat river land, the hills and the swamp, then place each feature and pass its reason check | the picture and the map side by side; a reason line for each place | 2, 3 |
| D2.Geo.1.3-5 (unfamiliar place) | Add a key with a symbol for each feature, set the scale bar, label the grid, then fix the map until Nia finishes all three errands | the map with key, scale bar and grid; Nia's path and where it goes wrong | 4, 5 |
| D2.Geo.1.3-5 (familiar place) | Make a simple map of their own school area with a key | the school map template with symbols | 6 |

## Screens and modes
Header (kit): title "Map Maker"; `Island`, `My school map`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Left: the satellite-style picture of the island. Right: a blank map sheet with a faint outline of the picture's frame. The welcome is queued (`welcomeAfter: true`): "This island has never been mapped. You'll make the first map! Trace the coastline onto your map." First hint: "Drag your finger around the coast on the map sheet."

**Trace (focus: the two panes).** At 1366x768 picture and map sit side by side; at 680x425 they stack as two tabs, `Picture` and `Map`, and the child switches with one tap.
- The child traces the coast, then the river. Tracing snaps to the true line when the stroke stays within 20 px of it; outside that, the stroke shows a ghost of the true line for two seconds and asks to try again. A `Help me` button appears after two misses and traces the rest of the line for them.
- Then three land patches (hills, forest, swamp) are tapped on the picture and painted onto the map with a tap.

**Build (focus: the map and a tray of five pieces).** Pieces: port, market, homes (two), farm (two). Each drop runs a reason check against the land under it:
- Port: must touch the coast and sit in the deep cove (the dark blue water on the west). On the east beach: "The water's light and shallow here. Big boats would scrape the bottom. Look for dark water."
- Farms: must sit on the flat land by the river. On the hills: "Hills are steep and rocky. Where's flat land with water close by?"
- Homes: on dry land, not in the swamp. In the swamp: "The ground is soggy here. Homes need dry land."
- Market: between the homes and the farms, within two squares of both. Too far: "The farmers have to carry food here and the families have to walk here. Can you put it closer to both?"
- Passed checks leave a short reason under each piece (tap to hear it again).

**Key and grid (focus: the map edges).**
- Key: each piece type needs a symbol picked from a small set (a boat, a house, a stall, a sprout, plus wrong-looking spares) and a word. The key box fills as the child picks.
- Scale bar: a bar the child drags to the length of one grid square and labels "1 km". The picture's frame says "Each square on the picture is 1 km."
- Grid: letters A to F across the top, numbers 1 to 5 down the side. The child drags letter and number tiles into place.

**Nia's trip (focus: the map, read by Nia).** Nia the traveler gets three errands, built from the child's own map:
1. "Walk from the port to the market." Nia reads the key to find the stall symbol and walks there.
2. "Take seeds to the farm that's 1 km from the market." Nia uses the scale bar.
3. "Meet my friend in square E2." Nia uses the grid.
- Nia walks one square per step with a dotted path. If the map is wrong, she goes wrong in a way that shows why:
  - A missing or doubled key symbol: she stops at the wrong building ("Is this the market? The key doesn't say.").
  - A scale bar set to two squares: she walks twice as far and ends up in the forest ("Your map said 1 km. I walked that far, but no farm!").
  - Grid letters or numbers out of order: she arrives at the wrong square ("This is E2 on your map, but it's the swamp!").
- The child taps `Fix my map`, which jumps to the part that needs it, then `Send Nia again`.
- When all three errands work: "Your map got me everywhere! You're a real mapmaker." `Print` prints the map with its key, scale bar and grid.

**My school map (extra).** A blank sheet with a road, a building block and a playground piece the child places and labels (school, playground, a road, the way home), plus a key and arrows for North. Nothing leaves the page. Hint: "Put your school in the middle, then add what's around it."

## Content
- One island picture with a matching true layer: coast, river, deep cove, shallow beach, hills, forest, swamp, flat river land.
- Five piece types with reason checks; eight symbols (four right, four spares); a 6 by 5 grid of 1 km squares.
- Three errands, each tied to one map part (key, scale, grid), and three failure kinds with their lines.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Help me` shows only after two misses on one line. `Fix my map` shows only after Nia gets lost; `Send Nia again` only after a fix.
- Keyboard: arrow keys move a selected piece one square; Enter drops; Tab moves through the tray and the key.
- With Motion off Nia jumps square to square instead of walking.

## Look
- Accent `--brand` #2d6a3e forest green (header, map frame, the key box); gold #f4c542 (the selected piece, Nia's path); paper #f1f7f2; ink #0c2213; muted #4e5d51.
- Contrast (WCAG 2.1, computed): white on brand 6.48:1; brand on paper 5.96:1; ink on paper 15.41:1; muted on paper 6.42:1; ink on gold 10.30:1.
- Never color alone: deep and shallow water carry labels on the picture ("deep", "shallow") on tap; each symbol has its word in the key.
- Different from this batch (promise navy, day-in-the-life clay, overlay sepia, pool aqua).

## Art
- Local FLUX (`scripts/localart.py`): the island seen from above (1, 4:3, satellite style, no labels); Nia (2 poses: walking, waving; cutout yes, illustrated, not photographic).
- Drawn in code: the map sheet and every traced line, patches, pieces, symbols, the key, the scale bar, the grid, Nia's path, the school map pieces.
About 3 images. Nia is a cartoon figure, so no Gemini people art.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the narrator; `upbeat-guide` as Nia. `Curio.voice` with `scope: () => state.mode + ':' + state.part + ':' + state.errand`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `trace-river` (once): "Now trace the river."
- how `land`: "Tap the hills, the forest and the swamp on the picture."
- how `build`: "Drag each piece onto your map where the land suits it."
- event, whole, each reason line (pass or try again).
- how `key`: "Pick a symbol for each piece and drag it to the key."
- how `scale`: "Drag the scale bar to the size of one square."
- how `grid`: "Put the letters across the top and the numbers down the side."
- how `send`: "Tap Send Nia when your map is ready."
- event, whole, each of Nia's errand and lost lines (Nia's voice).
- how `fix`: "Tap Fix my map to see what to change."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
me-map (no engine doc): uses its map sheet, place markers and zoomed view. Tool-only code: the trace snapping, land patches, reason checks, key builder, scale bar and grid tiles, and Nia's path that reads the child's own key, scale and grid.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reason checks | Drop pieces anywhere until one sticks | Each try-again line names what the land needs; the port has only one good cove. |
| Key | Pick any symbols | Nia reads the key; two pieces with the same symbol send her to the wrong one. |
| Scale bar | Leave it as it starts | It starts at two squares, so Nia walks too far until it's fixed. |
| Grid | Drop tiles in any order | Nia goes to the square the labels say; wrong order sends her to the swamp. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Coast traced: `trace-river` (once); then `land`.
2. Build: `build`; each drop: a reason line (whole).
3. Key and grid: `key`, `scale`, `grid`; then `send`.
4. Nia: each errand line (whole), waits; lost line (whole); `fix`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.1.3-5 and D2.Geo.2.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| A map key explains symbols; a scale bar shows real distance; a grid of letters and numbers locates places | National Geographic Education, "Map" and "Scale" | USGS, "Map scales" fact sheet | yes |
| Deep water near shore shows darker on satellite pictures; ports need deep water for big ships | NOAA Ocean Service, "What is a port?" and bathymetry | National Geographic Education, "Port" | yes |
| Flat floodplain land by rivers has rich soil and water for farming | National Geographic Education, "Floodplain" | Wikipedia, Floodplain (checked 2026-11-09) | yes |
| Swamps and wetlands have soggy ground that is poor for building | National Geographic Education, "Wetland" | U.S. EPA, "What is a wetland?" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r5, 2026-11-09): on the true layer the port has exactly one passing coast square group (the west cove); the grid is 6 by 5 with 1 km squares; errand 2's "1 km from the market" has at least one farm square in reach on every passing layout; a scale bar of two squares doubles Nia's walk; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 picture and map sit side by side; at 680x425 they become tabs.
2. Each piece passes its reason check only on suitable land. (D2.Geo.2.3-5)
3. Each reason line names the land feature seen in the picture. (D2.Geo.2.3-5)
4. Key, scale bar and grid are built by the child and read by Nia. (D2.Geo.1.3-5)
5. Each of the three failure kinds sends Nia wrong in its own way, and fixing it lets her finish. (D2.Geo.1.3-5)
6. My school map prints with a key. (D2.Geo.1.3-5)
7. `Help me`, `Fix my map` and `Send Nia again` are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: Nia jumps squares; no network requests.

## Open questions
- None for Cory.
