# World Layers Map

## One idea
A plain world map sits under a stack of switches, and the student turns on one layer at a time (mountains, volcanoes, earthquakes from the past year, ocean depth, ocean trenches), each built from real public data, and is asked "What do you notice?" after each one; volcanoes and earthquakes crowd into a ring around the Pacific, deep trenches run beside many of those same coasts, a long underwater mountain range runs down the middle of the Atlantic, and the tallest mountains sit in long chains rather than scattered dots; the student draws loops around each pattern they find, names it on a pattern card, and checks it with a "Does it line up?" overlay that counts how many points fall inside their loop; at the end a pattern notebook holds five patterns, each with a map snip and a sentence, and a closing card says scientists explain why these line up in grade 6, so a fourth grader learns to analyze and interpret map data to describe patterns in Earth's features.

## Not like
- erosion-table (4, concept): how land wears away. Here where features are.
- plate-puzzle (6, concept): why features line up. Here only that they do.
- map-maker (3, spec): making a map. Here reading real data on one.
- me-on-the-map (K, live): where I am. Here what the whole planet shows.

## Who and how
- Grade 4, Science, module "Earth's Features on Maps". Standards: 4-ESS2-2 (analyze and interpret data from maps to describe patterns of Earth's features).
- Format: map. Driver: one student alone, or the class on the projector (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- Five data layers, the loop tool, the "Does it line up?" check, five pattern cards, the pattern notebook. Extra: Class notice (the class calls out what they notice as each layer turns on). tool.json `modes: ["Layers", "Class notice"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4-ESS2-2 (analyze) | Turn layers on and off and compare them | real points and shading lining up | 2 |
| 4-ESS2-2 (interpret) | Loop a pattern and check how many points fall inside | the loop count | 3 |
| 4-ESS2-2 (describe) | Name each pattern with a sentence | the pattern notebook | 4 |

## Screens and modes
Header (kit): title "World Layers Map"; `Layers`, `Class notice`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A plain world map in soft colors with five switches on the side. The welcome is queued (`welcomeAfter: true`): "This map holds secrets. Turn on volcanoes. What do you notice?" First hint: "Tap the Volcanoes switch."

**Layers (focus: the map).** At 1366x768 the map fills the screen with switches on the right; at 680x425 switches are a bottom bar. Five layers:
1. Volcanoes: active volcanoes as triangles.
2. Earthquakes: one year of larger earthquakes as dots sized by strength.
3. Mountains: high land shaded.
4. Ocean depth: shallow to deep blues with a depth key.
5. Trenches: the deepest places as lines, with the Mariana Trench labeled.
Zoom and pan let the student look closer. Tapping a point shows its name, depth or height.

**Loops and checks.** The student draws a loop around a pattern. `Check` counts how many volcanoes or earthquakes fall inside the loop and what share of all of them that is. Patterns to find: the ring around the Pacific; trenches beside the Pacific ring; the mid-Atlantic underwater mountain range; long mountain chains (the Andes, the Himalayas, the Rockies); few volcanoes and earthquakes in the middle of most continents.

**Pattern cards.** For each pattern: "I noticed ___ line up along ___." The card holds a snip of the loop.

**The notebook (the aha).** Five patterns on one page. Narrator: "Volcanoes, earthquakes, mountains and trenches aren't scattered at random. They line up. Why they line up is a mystery you'll solve in grade 6."

**The end.** The pattern notebook. `Print` prints it with the map snips.

**Class notice (extra).** The class calls out what they notice as each layer turns on.

## Content
- Five layers from public data, bundled and simplified for speed, with the date range and source on each layer's key.
- No plate boundaries are drawn; the closing card points ahead to grade 6.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Loops close when the finger lifts; a loop can be redrawn.
- Keyboard: Tab to switches, the map, the loop tool, `Check` and cards; arrow keys pan; plus and minus zoom; a keyboard loop uses four corner points.
- With Motion off layers appear without fading and zoom jumps.

## Look
- Accent `--brand` #1b3a5c ocean navy (header, switches, the notebook); gold #f4c542 (the loop, the switch just turned on); paper #eef3f8; ink #08182a; muted #4d5866.
- Contrast (WCAG 2.1, computed): white on brand 11.63:1; brand on paper 10.41:1; ink on paper 16.02:1; muted on paper 6.48:1; ink on gold 10.99:1.
- Never color alone: layers use shapes (triangles, dots, lines) and keys in words; depth has a number key.
- Different from this batch (magnet red, collar green, postcard orange, lane indigo).

## Art
- Real data drawn in code: the base map and all five layers.
- Local FLUX (`scripts/localart.py`): a volcano, a deep-sea trench view, a mountain range (3, 4:3) for the pattern cards.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the map scientist; `upbeat-guide` as the guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.layer + ':' + state.pattern + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `layer`: "Tap a switch to turn on a layer."
- event, whole, a "what do you notice" line for each layer.
- how `loop`: "Draw a loop around the pattern."
- how `check`: "Tap Check to count what's inside."
- how `card`: "Finish the sentence on the card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the map, layers, loop tool, the inside-loop count. Layer data sits in a marked block `/* WORLD LAYERS DATA: begin */ ... /* end */` so plate-puzzle can reuse it.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Loops | Loop the whole map | `Check` reports the loop covers too much; a pattern needs a narrow band. |
| Cards | Write the same sentence | Each card needs a different place named. |
| Layers | Turn on all at once | Allowed, but each card asks which layer showed it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `layer`; notice (whole), waits.
2. `loop`; `check`.
3. `card`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 4-ESS2-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Earthquake locations and sizes | U.S. Geological Survey, Earthquake Catalog (ComCat) | International Seismological Centre, ISC Bulletin | yes |
| Volcano locations | Smithsonian Institution, Global Volcanism Program | U.S. Geological Survey, Volcano Hazards Program | yes |
| Ocean depth and land height | NOAA National Centers for Environmental Information, ETOPO 2022 | GEBCO, global bathymetric grid | yes |
| Most earthquakes and many volcanoes sit around the Pacific (the Ring of Fire) | U.S. Geological Survey, "Ring of Fire" | NOAA Ocean Exploration, "What is the Ring of Fire" | yes |
| Challenger Deep is about 10,935 meters deep; Mount Everest is 8,849 meters tall | NOAA Ocean Exploration, "How deep is the ocean" | Nepal and China survey (2020) reported by National Geographic | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r28, 2026-11-09): five layers and five patterns; Challenger Deep (10,935 meters) is about 2,086 meters deeper than Everest (8,849 meters) is tall; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and switches; at 680x425 bottom bar.
2. Five real data layers turn on and off with keys and sources. (4-ESS2-2)
3. Loops around patterns are counted by `Check`. (4-ESS2-2)
4. Five patterns are named in the notebook. (4-ESS2-2)
5. No plate boundaries are drawn; grade 6 is pointed to.
6. Layer data is bundled with dates and sources shown.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fades; no network requests.

## Open questions
- The idea card flags a data source (default used: USGS ComCat earthquakes of magnitude 5 and up for one stated year, Smithsonian Global Volcanism Program volcanoes, NOAA ETOPO 2022 depth and height, all simplified and bundled; no network).
