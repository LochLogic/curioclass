# Rock Recycler

## One idea
One grain of feldspar sits in a granite mountain and a card asks "Where will it go next?"; the student follows the grain through the rock cycle by choosing each path (frost cracks it loose, rain and gravity carry it downhill, a river drops it in a delta, more sand buries it and presses it into sandstone, deep burial heats and squeezes it into a new rock, it melts into magma, cools slowly underground into new granite, and uplift brings it back to the surface), and every step shows two things: which energy drives it (the sun, through weather, water and gravity at the surface, or Earth's inner heat deep down) and how long it really takes on a clock that stretches from a landslide in seconds to a flood in days, a delta over centuries and uplift over millions of years; a size bar beside the clock shows how big each change is, from one grain to a whole mountain range; at the end the grain is back where it started and the student fills a cycle map naming what powered each step and how fast it ran, so a sixth grader learns to model the cycling of Earth's materials and the energy that drives it, and how geoscience processes change Earth's surface at very different time and size scales.

## Not like
- plate-puzzle (6, spec): evidence that plates moved. Here what happens to the rock they carry.
- erosion-table (4, spec): water and wind wearing land down. Here the whole loop, up and down.
- canyon-reader (4, spec): reading layers already laid down. Here making and remaking them.
- world-layers-map (4, spec): where mountains and volcanoes are. Here how slowly they rise.

## Who and how
- Grade 6, Science, module "Rock Cycle and Earth's Changing Surface". Standards: MS-ESS2-1 (develop a model to describe the cycling of Earth's materials and the flow of energy that drives this process), MS-ESS2-2 (construct an explanation based on evidence for how geoscience processes have changed Earth's surface at varying time and spatial scales).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- One grain, six process steps (weathering, erosion, burial, melting, cooling, uplift) with two or three path choices at each, an energy badge per step, the time clock, the size bar, the cycle map. Extra: Fast and slow (sort ten real events by time and size). tool.json `modes: ["Grain", "Fast and slow"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ESS2-1 (cycling) | Choose the grain's path through each step back to the start | the grain's route; the rock it becomes | 2 |
| MS-ESS2-1 (energy) | Tag each step with the sun or Earth's inner heat | the energy badges; the cycle map | 3 |
| MS-ESS2-2 | Read each step's clock and size bar and sort real events | the time clock; the size bar; the sort | 4 |

## Screens and modes
Header (kit): title "Rock Recycler"; `Grain`, `Fast and slow`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A granite peak under snow, a zoom circle showing one pink feldspar grain locked between quartz and mica. The welcome is queued (`welcomeAfter: true`): "This grain has been in the mountain for a long time. Where will it go next? Tap a path." First hint: "Tap Frost cracks it loose."

**The journey (focus: the grain).** At 1366x768 the scene fills the left with the clock and size bar right; at 680x425 they fold into a strip under the scene. Each step offers two or three paths (from a riverbed: carried to the sea, dropped in a delta, stuck behind a dam). After a choice the step plays; the clock's hand spins to its real time and the size bar shows how big the change is. The student drags an energy badge (sun, inner heat) onto the step. A wrong badge says "Not yet. What makes the water move?"

**The clock.** A long clock with marks for seconds, days, years, a thousand years, a million years. A landslide: seconds, a hillside. A flood: days, a valley. A delta: hundreds of years, a coast. Burial and pressing: millions of years. Uplift: about 1 mm a year, so 1 km takes about a million years, a whole range.

**Deep down.** Burial carries the grain into heat; the student chooses: squeezed into a new rock (metamorphic) or melted into magma. Magma cools slowly underground into granite with big crystals, or erupts and cools fast into rock with tiny crystals.

**The cycle map (the aha).** The grain is back in a mountain. The map shows each step's arrow, its energy badge and its clock time. Narrator: "The sun's heat drives the weather that wears mountains down. Earth's inner heat builds them back up. Your grain is billions of years older than any mountain it has been in."

**The end.** The cycle map with the student's path, badges and times. `Print` prints it.

**Fast and slow (extra).** Ten real events (the 1980 Mount St. Helens landslide, the Grand Canyon's carving, the Himalaya rising, a beach after one storm) sorted on two lines: how long and how big.

## Content
- Six steps with paths, two energy sources, time and size marks per step, the cycle map, ten real events for the extra with dates and sizes from USGS and NPS.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The clock is a log scale with words at each mark.
- Keyboard: Tab to paths, badges, the clock and the map; Enter chooses and places.
- With Motion off steps show before and after stills and the clock jumps.

## Look
- Accent `--brand` #5a4636 granite brown (header, path arrows, the clock); gold #f4c542 (the grain, the badge in hand); paper #f7f4f0; ink #1c140d; muted #5b534b.
- Contrast (WCAG 2.1, computed): white on brand 8.88:1; brand on paper 8.10:1; ink on paper 16.58:1; muted on paper 6.88:1; ink on gold 11.18:1.
- Never color alone: badges carry a sun or flame icon and a word; clock marks carry words.
- Different from this batch (raindrop blue, tomato red, olive, lake teal).

## Art
- Local FLUX (`scripts/localart.py`): granite peak (1, 16:9), riverbed (1, 16:9), delta (1, 16:9), deep crust (1, 16:9), volcano (1, 16:9).
- Drawn in code: the grain, the zoom circle, arrows, the clock, the size bar, the cycle map.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the geologist; `easy-coach` as hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.path + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `path`: "Tap a path for the grain."
- how `badge`: "Drag the sun or the inner heat badge onto this step."
- event, whole, each step's time and size.
- how `deep`: "Tap squeeze or melt."
- event, whole, the cycle map.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the path graph, the log clock, the size bar. Steps and real events sit in a marked block `/* ROCK-RECYCLER DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Badges | Put the sun on everything | Deep steps reject the sun with a reason. |
| Path | Tap the first path every time | Any route works, but the map still needs a badge and a time per step. |
| Sort | Guess times | Each event shows its real time once placed. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `path`; `badge`.
2. Step time and size (whole), waits.
3. `deep`.
4. Cycle map (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-ESS2-1, MS-ESS2-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| The rock cycle and its steps | U.S. Geological Survey, "The Rock Cycle" | National Park Service, "Rock Cycle" (geology education) | yes |
| Surface processes are driven by the sun and gravity; deep ones by Earth's internal heat | National Geographic Education, "The Rock Cycle" | U.S. Geological Survey, "This Dynamic Earth" | yes |
| Uplift runs about millimeters a year | U.S. Geological Survey, "Himalayas" (This Dynamic Earth) | NASA Earth Observatory, "Mountain building" | yes |
| Slow-cooled magma makes large crystals; fast-cooled lava small ones | U.S. Geological Survey, "Igneous rocks" | National Park Service, "Igneous rocks" | yes |
| Mount St. Helens' 1980 landslide was the largest in recorded history and lasted seconds to minutes | U.S. Geological Survey Cascades Volcano Observatory | U.S. Forest Service, Mount St. Helens National Volcanic Monument | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-10): 1 mm a year for a million years is 1 km; ten million years is more than 30 trillion times ten seconds; six process steps; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene with clock and bar; at 680x425 strip.
2. The grain goes all the way around the cycle by student choices. (MS-ESS2-1)
3. Every step is tagged with the right energy source. (MS-ESS2-1)
4. Every step shows its real time and size, and ten events are sorted. (MS-ESS2-2)
5. Times and sizes match the cited sources.
6. The clock labels each mark in words.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: stills and jumps; no network requests.

## Open questions
None.
