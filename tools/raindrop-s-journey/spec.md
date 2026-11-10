# Raindrop's Journey

## One idea
The student is one water molecule in a puddle at noon, with a sun meter (energy in) and a gravity arrow beside it, and chooses where to go next, but each choice opens only when the sun's energy or gravity allows it: evaporate (needs the sun), rise and cool, condense on a speck of dust, fall as rain or snow (gravity), soak into the ground, run downhill to a river, freeze into a glacier, sink deep into an aquifer, or get pulled up by a tree and breathed out of a leaf (the sun again); a log keeps the time spent in each place, from about 9 days in the air to 10,000 years deep underground, and every path loops back, so there are no dead ends; at the end a journey map shows every loop the student took with each arrow labeled by its driver (the sun lifts water up, gravity brings it down), so a sixth grader learns to develop a model of how water cycles through Earth's systems, driven by energy from the sun and the force of gravity.

## Not like
- sphere-connections (5, spec): cards linking Earth's spheres. Here one molecule's path and what drives it.
- ocean-conveyor (6, spec): currents and climate. Here water changing state and place.
- erosion-table (4, spec): water shaping land. Here water itself moving.
- front-line (6, spec): weather when air masses meet. Here the whole water cycle.

## Who and how
- Grade 6, Science, module "Water Cycle and Weather". Standard: MS-ESS2-4 (develop a model to describe the cycling of water through Earth's systems driven by energy from the sun and the force of gravity).
- Format: story. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Nine places (puddle, air, cloud, snowpack, glacier, soil, aquifer, river, ocean, plus a tree as a path), about 14 moves, the sun meter, the gravity arrow, the time log, the journey map. Extra: Class maps (compare maps: whose molecule spent longest underground?). tool.json `modes: ["Journey", "Class maps"]`, `minutes: "15-25"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ESS2-4 (sun) | Charge the sun meter to evaporate or transpire | the meter filling; the molecule rising | 2 |
| MS-ESS2-4 (gravity) | Follow gravity to fall, run off and sink | the gravity arrow; the molecule moving down | 3 |
| MS-ESS2-4 (model) | Build the journey map with each arrow's driver | the map; the time log | 4 |

## Screens and modes
Header (kit): title "Raindrop's Journey"; `Journey`, `Class maps`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A puddle on a sidewalk at noon. The student's molecule glows among others, with a face only on the meter (the molecule itself is drawn plainly). The sun meter sits empty. The welcome is queued (`welcomeAfter: true`): "You're one tiny bit of water in a puddle. Where will you go? To leave, you need energy. Tap the sun meter to soak up sunlight." First hint: "Tap the sun meter."

**The journey (focus: the molecule).** At 1366x768 a side-view landscape (mountains, a forest, a town, a river, the sea, layers underground) fills the screen with the log as a strip on the right; at 680x425 the view pans to the molecule and the log is a sheet. Each place shows two to four move cards, each with its driver: Evaporate (sun), Rise and cool, Condense on dust, Fall as rain or snow (gravity), Soak in (gravity), Run downhill (gravity), Freeze (losing energy), Melt (sun), Taken up by roots and breathed out of a leaf (sun). A move whose driver isn't ready is shown with "needs sunlight" and opens when the meter fills; the hint never points to it.

**The log.** Each stop adds a line with a typical time: air about 9 days, river a few months, soil a month or two, glacier 20 to 100 years, lake 50 to 100 years, ocean about 3,200 years, shallow groundwater 100 to 200 years, deep groundwater up to 10,000 years. The log adds them up.

**The journey map (the aha).** After at least six moves, the student taps `Map`. Every move is an arrow labeled sun or gravity. Narrator: "The sun lifts water up. Gravity brings it down. Every drop you drink has made this trip again and again."

**The end.** The map and the log. `Print` prints them.

**Class maps (extra).** Maps from the class side by side on the projector, sorted by time underground.

## Content
- Nine places with typical times, 14 moves each labeled with its driver, the meter rule, the map, a note that times are typical, not exact.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Every place has at least one open move; every path loops back.
- Keyboard: Tab to the meter and move cards; Enter chooses.
- With Motion off the molecule jumps between places.

## Look
- Accent `--brand` #1f5f99 raindrop blue (header, arrows, the log); gold #f4c542 (the sun meter, the student's molecule); paper #f0f5fa; ink #0a1a2b; muted #4c5866.
- Contrast (WCAG 2.1, computed): white on brand 6.66:1; brand on paper 6.07:1; ink on paper 16.01:1; muted on paper 6.61:1; ink on gold 10.80:1.
- Never color alone: arrows carry a sun or down-arrow icon and a word.
- Different from this batch (granite brown, tomato red, olive, lake teal).

## Art
- Local FLUX (`scripts/localart.py`): the side-view landscape in one long panorama (1, 32:9), a puddle close-up (1, 16:9), a cloud close-up (1, 16:9).
- Drawn in code: the molecule, meter, arrows, the log, the map.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as the molecule's inner voice; `gentle-storyteller` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.place + ':' + state.move + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `meter`: "Tap the sun meter to soak up sunlight."
- how `move`: "Tap a move card to go."
- event, whole, each arrival with its time.
- how `map`: "Tap Map to see your whole trip."
- event, whole, the map.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the place graph, the meter rule, the map. Places, moves and times sit in a marked block `/* RAINDROP DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Moves | Tap the first card each time | Any path is allowed; the map still labels each driver and the student checks two. |
| Map | Open it at once | Map opens after six moves. |
| Drivers | Guess sun or gravity | The map asks for two arrows' drivers and shows why on a miss. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `meter`; `move`.
2. Arrival (whole), waits.
3. `map`.
4. Map (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-ESS2-4 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| The sun drives evaporation and transpiration; gravity drives precipitation, runoff and infiltration | U.S. Geological Survey, "The Water Cycle" | NASA Earth Observatory, "The Water Cycle" | yes |
| Typical residence times (air about 9 days, ocean about 3,200 years, deep groundwater up to 10,000 years) | UCAR Center for Science Education, "The Water Cycle" | Pidwirny, "Fundamentals of Physical Geography", residence times table | yes |
| Water vapor condenses on tiny particles to form clouds | NOAA National Weather Service JetStream, "Clouds" | NASA, "Clouds and aerosols" | yes |
| Plants take up water through roots and release it from leaves | U.S. Geological Survey, "Evapotranspiration" | NOAA Ocean Service, "Transpiration" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-10): 10,000 years deep underground is about 406,000 times 9 days in the air; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 landscape and log; at 680x425 pan and sheet.
2. Sun-driven moves open only when the meter fills. (MS-ESS2-4)
3. Gravity-driven moves carry the molecule down. (MS-ESS2-4)
4. The journey map labels every arrow's driver and the log adds times. (MS-ESS2-4)
5. Times match the cited tables and say "typical".
6. Every place has an open move; no dead ends.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps between places; no network requests.

## Open questions
- Code move: the idea card moves MS-ESS2-5 to front-line (default used: this tool teaches MS-ESS2-4 only).
