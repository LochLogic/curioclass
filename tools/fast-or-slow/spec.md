# Fast or Slow?

## One idea
A long timeline stretches across the screen with picture stops (a blink, a day, a year, a grandparent's life, a very, very long time), and a stack of event cards waits: a landslide that buried a stretch of California highway in a few minutes, Mount St. Helens erupting, lava from Kilauea building new land in Hawaii over months, the Colorado River carving the Grand Canyon over millions of years, a North Carolina beach washing away so slowly that a lighthouse had to be moved; for each card the student opens two or more clues from different sources (a before-and-after photo, a short read-aloud from a park ranger or a scientist, a short clip), places the event on the timeline, sees the real time, and taps which clue helped; then a hillside home and a beach house face wind and water, and the student tries solutions (plant grass, a sand fence, a stone wall, a ditch, a row of trees as a windbreak), runs a storm and a sped-up year, and compares how much land each saved and what it costs or blocks; at the end the full timeline and a comparison card show that some changes happen in minutes and some take longer than people have lived, so a second grader learns to use information from several sources as evidence that Earth events can be quick or slow, and compares solutions that slow wind or water from changing the land.

## Not like
- erosion-table (4, concept): measuring rates of weathering and erosion. Here quick or slow, from clues.
- island-maker (2, spec): the shapes of land. Here land changing over time.
- earth-s-calendar (6, concept): deep time. Here seconds to millions of years in pictures.
- beaver-builders (K, spec): an animal changing a stream. Here wind, water and rock.

## Who and how
- Grade 2, Science, module "Changing Landforms". Standards: 2-ESS1-1 (use information from several sources to provide evidence that Earth events can occur quickly or slowly), 2-ESS2-1 (compare multiple solutions designed to slow or prevent wind or water from changing the shape of the land).
- Format: timeline. Driver: one child alone or with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Six event cards with three clues each, the timeline, two places to protect with five solutions, the comparison card. Extra: Class timeline (the class places each card together on the projector). tool.json `modes: ["Timeline", "Class timeline"]`, `minutes: "20-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2-ESS1-1 | Open two or more clues for each event and place it on the timeline | the clues; the timeline with real times | 2 |
| 2-ESS1-1 (sources) | Tap which clue helped | the clue's source named | 3 |
| 2-ESS2-1 | Try solutions on a hillside and a beach and compare land saved and trade-offs | the storm and year runs; the comparison card | 4 |

## Screens and modes
Header (kit): title "Fast or Slow?"; `Timeline`, `Class timeline`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** The timeline with five picture stops and a stack of event cards. A ranger (made up, labeled "illustration") waves. The welcome is queued (`welcomeAfter: true`): "The Earth is always changing. Some changes are fast and some are very, very slow. Tap a card to find out how long one took." First hint: "Tap the top card."

**Event cards (focus: the clues).** At 1366x768 the card fills the left with the timeline below; at 680x425 the clues are a sheet. Each card has three clues; the student must open at least two before placing it:
1. Mud Creek landslide, Big Sur, California (May 20, 2017): a hillside slid onto the highway in minutes.
2. Mount St. Helens, Washington (May 18, 1980): the side of the mountain fell and it erupted in one morning.
3. Kilauea, Hawaii (2018): lava flowed into the ocean for about three months and made new land.
4. A sand dune moving a few feet a year at Great Sand Dunes, Colorado.
5. The Cape Hatteras shore, North Carolina: the beach washed away over about a hundred years, and in 1999 the lighthouse was moved 2,900 feet inland.
6. The Grand Canyon: the Colorado River carved it over about 5 to 6 million years.
- After placing, the real time shows and the student taps the clue that helped most.

**Protect the land (2-ESS2-1).** A hillside home above a road and a beach house behind dunes. Five solutions: plant grass, a sand fence, a stone wall, a ditch, a row of trees as a windbreak. The student places up to two per place, then runs a storm and a sped-up year. A picture meter counts land saved; trade-off cards say what each costs or blocks (a wall can wash out the beach beside it; trees take years to grow). The student tries a second plan and compares.

**The comparison (the aha).** The full timeline and a card: "This worked best on the hill: ___. This worked best on the beach: ___, because ___." Narrator: "Some changes happen faster than you can blink. Some take longer than all of history. And people can slow some of them down."

**The end.** The timeline and the comparison card. `Print` prints them.

**Class timeline (extra).** The class places each card together.

## Content
- Six real events with three clues each from public sources, the five-stop timeline, two places, five solutions with trade-offs, the comparison card.
- Events are shown as land, not people; no injuries or losses are shown or described.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A card can be moved on the timeline until all six are placed.
- Keyboard: Tab to cards, clues, timeline stops and solutions; Enter places.
- With Motion off clips show as before-and-after stills.

## Look
- Accent `--brand` #9a3f1c canyon rust (header, the timeline, cards); gold #f4c542 (the card in hand, the chosen solution); paper #fcf3ef; ink #2b1007; muted #61554f.
- Contrast (WCAG 2.1, computed): white on brand 6.77:1; brand on paper 6.19:1; ink on paper 16.28:1; muted on paper 6.58:1; ink on gold 10.94:1.
- Never color alone: timeline stops carry pictures and words; the land meter carries numbers.
- Different from this batch (berry, gadget green, dusk blue, lagoon).

## Art
- Public domain photos from the U.S. Geological Survey and National Park Service for the six events, checked one by one (about 12, before and after).
- Local FLUX (`scripts/localart.py`): the hillside home and beach house, each before and after a storm (4, 16:9).
- People (illustrated) for the ranger, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Drawn in code: the timeline, clue cards, the land meter.
About 17 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the park ranger and the clue readings; `clear-teacher` as the guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `clue`: "Tap two clues on the card."
- how `place`: "Drag the card to how long it took."
- event, whole, each real time.
- how `helped`: "Tap the clue that helped most."
- how `protect`: "Drag a solution to the hill or the beach."
- event, whole, each storm and year run.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the timeline, clue cards, the protect runs, the comparison. Event data and photo credits sit in a marked block `/* FAST-OR-SLOW DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Placing | Place without clues | Placing opens after two clues. |
| Clue tap | Tap the first clue | Allowed; the card says what each clue showed. |
| Protect | Use the wall everywhere | The trade-off card shows the beach washing out beside it; the comparison asks why. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `clue`; `place`.
2. Real time (whole), waits; `helped`.
3. `protect`; run (whole).
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 2-ESS1-1, 2-ESS2-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Mud Creek landslide, May 20, 2017 | U.S. Geological Survey, "Mud Creek landslide" | California Department of Transportation, Highway 1 reopening | yes |
| Mount St. Helens, May 18, 1980 | U.S. Geological Survey, "1980 Cataclysmic Eruption" | National Park Service and U.S. Forest Service, Mount St. Helens National Volcanic Monument | yes |
| Kilauea 2018 lava flows made new land | U.S. Geological Survey, Hawaiian Volcano Observatory | National Park Service, Hawaii Volcanoes National Park | yes |
| Cape Hatteras Lighthouse moved 2,900 feet in 1999 | National Park Service, "Moving the Lighthouse" | U.S. Geological Survey, coastal change studies | yes |
| Grand Canyon carved over about 5 to 6 million years | National Park Service, Grand Canyon geology | U.S. Geological Survey, "Grand Canyon" | yes |
| Dunes move; sand fences, grass and windbreaks slow wind and water | National Park Service, Great Sand Dunes | USDA Natural Resources Conservation Service, "Windbreaks" and dune guides | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r26, 2026-11-09): six events and five timeline stops; Mount St. Helens erupted 46 years before 2026; the lighthouse move came 18 years before the Mud Creek slide; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 card and timeline; at 680x425 sheet.
2. Six events are placed after two clues each, with the real time shown. (2-ESS1-1)
3. The helping clue is tapped and its source named. (2-ESS1-1)
4. Two plans on two places are run and compared with trade-offs. (2-ESS2-1)
5. Photos are public domain and checked one by one.
6. No injuries or losses shown or described.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: stills; no network requests.

## Open questions
- The idea card flags a data source (default used: U.S. Geological Survey and National Park Service public domain photos, checked one by one, with credits in the data block).
