# Three Towns

## One idea
Three postcards show three kinds of places (a city by a harbor, a suburb of houses with yards, a farm town in a river valley), and the child sorts homes, work and ways to travel onto the right postcard, then follows one kid's breakfast in each place and taps each food to draw a line to where it came from (eggs from the hens out back in the farm town, milk trucked into the city, bananas shipped from far away to all three), and finally lifts a land layer that shows why each place has the work it does (deep water for ships, flat rich soil for farms, roads and trains to the city's jobs), so a second grader learns how different communities meet their needs from near and far and how the land shapes the work.

## Not like
- me-on-the-map (K, built): levels of place from room to planet. Here three kinds of community compared.
- state-economy-map (4, concept): industries on a real state map. Here three made-up places at grade 2.
- day-in-the-life (3, concept, next batch): daily life in other countries. Here three kinds of places in one country.
- pen-pal-parcels (2, spec, this batch): goods traded between countries. Here where a breakfast comes from, near or far.
- storm-helpers (2, spec, this batch): one street after a storm. Here three whole places.

## Who and how
- Grade 2, Social Studies (Geography), module "Urban, Suburban and Rural". Standards: D2.Geo.8.K-2 (compare how people in different types of communities use local and distant environments to meet their daily needs), D2.Geo.9.K-2 (describe the connections between the physical environment of a place and the economic activities found there).
- Driver: teacher on the projector with the class, or one child alone; every card, food and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Three parts: Sort, Breakfast, Land and work. Extra: "Which is our town most like?" tool.json `modes: ["Sort", "Breakfast", "Land and work"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.8.K-2 (types of community) | Sort twelve cards (homes, work, travel) onto City, Suburb or Farm town | each postcard filling with its four cards | 2 |
| D2.Geo.8.K-2 (near and far) | Tap each breakfast food to draw its line, then sort it Near or Far | lines from the table to a farm, a town, a port or a faraway place; a Near and Far tally per town | 3, 4 |
| D2.Geo.9.K-2 | Lift the land layer and match each place's land to its work | harbor depth, valley soil and roads and rails, each joined to a work card | 5 |

## Screens and modes
Header (kit): title "Three Towns"; `Sort`, `Breakfast`, `Land and work`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** Three big postcards on a table: Harbor City (tall buildings by a harbor with ships), Maple Grove (rows of houses with yards and a school), Riverbend (a small farm town with fields in a river valley). One card sits in a deck: an apartment building. The welcome is queued (`welcomeAfter: true`): "Three postcards from three kinds of places! A city, a suburb and a farm town. Where does this apartment building belong? Drag it to a postcard." First hint: "Drag the card to a postcard." Tapping a postcard reads its name and kind and cuts the welcome.

**Sort (focus: the deck and the postcards).** At 1366x768 the three postcards sit across the top, the deck below at center. At 680x425 the postcards stack as three tabs.
- Twelve cards, each with a picture and spoken name:
  - City: apartment building; subway; ferry; cargo ship crane.
  - Suburb: house with a yard; car in a driveway; shopping center; commuter train to the city.
  - Farm town: tractor; grain elevator; barn; pickup on a dirt road.
- A right drop settles with a clue line ("Lots of people live close together in a city, so homes stack up high."). A wrong drop: "Look at the postcard. Is there a harbor there? Lots of fields?" and the card returns.

**Breakfast (focus: one kid's table).** Three tabs, one per place, each with a kid at a breakfast table:
- Lina, Harbor City: a bagel, milk, an orange.
- Owen, Maple Grove: cereal, a banana, milk.
- Cal, Riverbend: eggs, toast, milk, a banana.
- Tapping a food draws a line on a small map to where it came from and plays its line:
  - Lina's bagel: "Baked fresh at the bakery on my block." (Near)
  - Lina's milk: "Trucked into the city from dairy farms outside it." (Far)
  - Lina's orange: "Grown in a warm state far away and trucked here." (Far)
  - Owen's cereal: "Made in a factory in another state." (Far)
  - Owen's banana: "Grown in Central America and shipped here." (Far)
  - Owen's milk: "From dairy farms in our state." (Near-ish: the line is short; it counts as Near)
  - Cal's eggs: "From our own hens, out back!" (Near)
  - Cal's toast: "The wheat grows right here in our valley. The bread is baked in town." (Near)
  - Cal's milk: "From the dairy farm next door." (Near)
  - Cal's banana: "Shipped from Central America, just like everyone's." (Far)
- After each line, the child taps `Near` (a house icon) or `Far` (a globe icon). Wrong: the line replays with the map zoomed.
- When all three tables are done, a tally compares: Lina 1 near, 2 far. Owen 1 near, 2 far. Cal 3 near, 1 far. The narrator: "Farm towns grow lots of food close by. Cities bring most food in from far away. And bananas travel to everyone!"

**Land and work (focus: the three postcards with a lift tab).** Each postcard has a `Lift the land` tab that peels the buildings away to show the land underneath:
- Harbor City: deep water at the shore, deep enough for big ships.
- Riverbend: flat land beside the river, with dark rich soil the river left when it flooded long ago.
- Maple Grove: roads and a train line running toward the city.
- Three work cards to match: "Loading ships at the port" (Harbor City), "Growing wheat and raising cows" (Riverbend), "Riding the train to jobs in the city" (Maple Grove). A wrong match: "What does the land there have?" and the land line replays.
- Then the child taps `Which is ours?` and picks the postcard most like their own town (any answer). `Print` prints the three postcards with their cards, tallies and work.

## Content
- Three places (made up), twelve sort cards, three kids with ten breakfast foods, three land layers and three work cards.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Near` and `Far` show only after a food's line plays. `Lift the land` shows only in the third part. `Which is ours?` shows after the three matches.
- Keyboard: Tab to a card, Enter to pick up, arrow keys between postcards, Enter to drop.
- With Motion off lines appear without drawing and the land layer swaps without peeling.

## Look
- Accent `--brand` #4d6b1f valley olive (header, postcard frames, lines); gold #f4c542 (the active card, the food line's dot, the matched work); paper #f4f7ec; ink #172207; muted #555c49.
- Contrast (WCAG 2.1, computed): white on brand 6.11:1; brand on paper 5.63:1; ink on paper 15.27:1; muted on paper 6.43:1; ink on gold 10.18:1.
- Never color alone: Near and Far carry icons and words; each postcard has its name.
- Different from this batch (piggy rose, pen pal indigo, storm teal, carousel red-brown).

## Art
- People art goes to Gemini with `people: true`: Lina, Owen and Cal at their tables (2 poses each: eating, pointing; cutout yes).
- Local FLUX (`scripts/localart.py`): three postcards in one style (3, 3:2) and their land layers (3, 3:2, same framing so the peel lines up); twelve sort cards (12, 1:1); ten breakfast foods (10, 1:1, cutout yes); three work cards (3, 1:1).
- Drawn in code: the small maps and lines, tallies, the lift tab, buttons.
About 37 images.

## Voice
Four bank voices, each unique in this batch: `curious-librarian` as the narrator; `playful-friend` as Lina; `soft-breath` as Owen; `smooth-narrator` as Cal. `Curio.voice` with `scope: () => state.mode + ':' + state.place + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: "Three postcards from three kinds of places! A city, a suburb and a farm town. Where does this apartment building belong? Drag it to a postcard."
- event `place`: the postcard's name and kind.
- event, whole, each sort clue line.
- event `sort-no`: "Look at the postcard. Is there a harbor there? Lots of fields?"
- how `breakfast`: "Tap a food to see where it came from."
- event, whole, each food line (by that kid's voice).
- how `near-far` (once): "Did it come from near or far? Tap Near or Far."
- event, whole, `tally`: "Farm towns grow lots of food close by. Cities bring most food in from far away. And bananas travel to everyone!"
- how `lift`: "Tap Lift the land to see what's under each place."
- event, whole, each land line; `match-no`: "What does the land there have?"
- how `ours`: "Which place is most like our town? Tap Which is ours?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the three-way sort, breakfast lines on small maps with Near or Far, the tally, the land layer peel, and the work match.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Drag all to one postcard | Each postcard takes four; wrong drops return with a look-again hint. |
| Near or Far | Tap Far for everything | Cal's table is mostly near; wrong taps replay the line with the map zoomed. |
| Land and work | Match in screen order | The work cards are shuffled each time. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Drops: a clue line (whole) or `sort-no`.
2. Breakfast: `breakfast`; each food: its line (whole), waits; `near-far` (once); tap.
3. All three: `tally` (whole).
4. Land and work: `lift`; each lift: the land line (whole); matches; `ours`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.8.K-2 and D2.Geo.9.K-2 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Urban, suburban and rural communities differ in how close together people live, their homes and their transport | National Geographic Education, "Urban area" and "Rural area" | U.S. Census Bureau, "Urban and rural" | yes |
| Ports need deep water near the shore for big ships | NOAA Ocean Service, "What is a port?" and harbor depth | National Geographic Education, "Port" | yes |
| River floodplains have flat land and rich soil good for farming | National Geographic Education, "Floodplain" | Wikipedia, Floodplain (checked 2026-11-09) | yes |
| Most U.S. bananas are imported from Central and South America; U.S. oranges are grown mainly in Florida and California | USDA Economic Research Service, fruit import and production data | Wikipedia, Banana (production and export) and Orange (fruit) (checked 2026-11-09) | yes |
| Cities get milk from dairy farms outside the city by truck | USDA Agricultural Marketing Service, "Dairy marketing" | National Geographic Education, "Food supply chain" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r4, 2026-11-09): twelve sort cards split 4, 4, 4; Near and Far tallies are Lina 1 and 2, Owen 1 and 2, Cal 3 and 1; each land layer joins exactly one work card; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 three postcards and the deck fit; at 680x425 the postcards become tabs.
2. Twelve cards sort four to each postcard. (D2.Geo.8.K-2)
3. Each breakfast food draws its line and takes its Near or Far. (D2.Geo.8.K-2)
4. The tally compares the three places. (D2.Geo.8.K-2)
5. Each land layer matches only its work card. (D2.Geo.9.K-2)
6. `Near`, `Far`, `Lift the land` and `Which is ours?` are never named before they show.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no drawn lines or peels; no network requests.

## Open questions
- None for Cory.
