# Canyon Reader

## One idea
A case file opens at the Grand Canyon's rim at sunrise with the words "The rocks here tell a story. Read it from the bottom up.", and the student hikes down a trail past eight rock stops, using a hand lens, a field guide of places today (a beach, a muddy sea floor, a shallow warm sea, a swampy river plain, a sand dune desert) and the clues in each rock (ripple marks, trilobite tracks, sea lily stems and shells, fern prints and mud cracks, slanted dune lines with small animal tracks) to decide what this place was like when each layer formed; each answer goes on a stacked case board with its clue; three pattern clues help: lower layers are older, a tilted set of layers cut flat under level ones marks a big gap in time, and the Colorado River cut down through all of them much later; at the end the student closes the case by telling the landscape's story from oldest to youngest (beach, then sea, then swampy plain, then desert, then sea again, then a river carving a canyon), citing a clue for each change, and compares it to the park geologist's account; the case file opens by naming the Grand Canyon as the homeland of Native nations who have their own knowledge of this place, so a fourth grader learns to use patterns in rock layers and fossils as evidence of how a landscape changed over time.

## Not like
- fossil-clues (3, spec): one change, same engine. Here a whole stack of changes in order.
- erosion-table (4, spec): how the river carves. Here what the layers record.
- earth-s-calendar (6, concept): the deep time scale. Here reading one place's story.
- world-layers-map (4, spec): patterns across the globe. Here patterns down one wall.

## Who and how
- Grade 4, Science, module "Rock Layers and Earth History". Standards: 4-ESS1-1 (identify evidence from patterns in rock formations and fossils in rock layers to support an explanation for changes in a landscape over time).
- Format: mystery. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight rock stops, the field guide with five places, three pattern clues, the case board, the closing story and the geologist's account. Extra: Second wall (a short wall from another real place to solve alone). tool.json `modes: ["Case", "Second wall"]`, `minutes: "25-35"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4-ESS1-1 (fossils) | Match each layer's clues to a place in the field guide | the hand lens view; the case board | 2 |
| 4-ESS1-1 (patterns) | Apply the three pattern clues to order and explain the layers | the stacked board; the gap in time | 3 |
| 4-ESS1-1 (explanation) | Tell the story oldest to youngest with a clue for each change | the closing story; the geologist's account | 4 |

## Screens and modes
Header (kit): title "Canyon Reader"; `Case`, `Second wall`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The canyon rim at sunrise and a case file. The first card of the case file: "The Grand Canyon is the homeland of many Native nations, including the Havasupai, Hualapai, Hopi, Navajo, Zuni and Southern Paiute, who have known this place for thousands of years and have their own stories of it. This case reads what the rocks record." The welcome is queued (`welcomeAfter: true`): "Let's hike down. Each layer is a clue. Tap the trail to go to the first stop." First hint: "Tap the trail."

**Rock stops (focus: the hand lens).** At 1366x768 the rock fills the left with the field guide and case board right; at 680x425 the guide is a sheet. The student taps the hand lens on the rock and matches clues to a place in the field guide. Stops, from the rim down:
1. Kaibab Limestone: shells, sponges and sea lily bits; a shallow warm sea.
2. Coconino Sandstone: slanted lines from old sand dunes and small animal tracks; a desert.
3. Hermit Formation: fern prints and mud cracks; a swampy river plain.
4. Redwall Limestone: sea lily stems and shells; a shallow warm sea.
5. Bright Angel Shale: trilobite tracks in mud; a muddy sea floor.
6. Tapeats Sandstone: ripple marks; a beach.
7. Tilted layers cut flat (the Great Unconformity): a gap in time.
8. Vishnu Schist at the bottom: very old twisted rock with no fossils.

**Pattern clues.** Three cards unlock along the way: lower layers are older (the board stacks oldest at the bottom); a tilted set cut flat under level layers means the old layers were tilted and worn away before new ones formed on top; the river cut through all the layers long after the youngest formed. The student applies each.

**Closing the case (the aha).** The student drags story cards into order from oldest to youngest and attaches a clue to each change. Then the park geologist's account appears beside it. Narrator: "This wall was a beach, a sea, a swamp, a desert and a sea again before a river cut through it. The rocks kept the record."

**The end.** The case board and story. `Print` prints them.

**Second wall (extra).** A short wall from another real place to solve alone.

## Content
- Eight stops with layer names, clues and places from park and survey sources; five field-guide places; three pattern clues; story cards; the geologist's account.
- Layer ages are given as "about" numbers on the board for older students and hidden by default.
- The case file names the Native nations with care, says they have their own knowledge of the canyon, and links to each nation's own website. It does not retell their stories or show sacred places.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A match can be changed until the case closes.
- Keyboard: Tab to the trail, the lens, guide places, the board and story cards; Enter picks and places.
- With Motion off the hike jumps between stops.

## Look
- Accent `--brand` #9a3b1b canyon rust (header, the case board, the trail); gold #f4c542 (the clue under the lens, the matched place); paper #fcf2ed; ink #2b0e05; muted #615049.
- Contrast (WCAG 2.1, computed): white on brand 6.96:1; brand on paper 6.32:1; ink on paper 16.32:1; muted on paper 6.93:1; ink on gold 11.06:1.
- Never color alone: layers carry names; places carry words and icons; the board marks the gap in time with a jagged line and a label.
- Different from this batch (workshop teal, civic blue, dusk purple, moss green).

## Art
- Local FLUX (`scripts/localart.py`): the rim at sunrise (1, 16:9), eight rock close-ups (8, 1:1), five field-guide places (5, 4:3).
- Public domain National Park Service photos of the canyon walls where found and checked, with credits; otherwise generated and labeled.
- Drawn in code: the trail, the lens, the case board, story cards.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the case file and hints; `wise-mentor` as the park geologist. `Curio.voice` with `scope: () => state.mode + ':' + state.stop + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `hike`: "Tap the trail to go to the next stop."
- how `lens`: "Tap the hand lens on the rock."
- how `match`: "Tap the place in the field guide that matches."
- event, whole, each pattern clue.
- how `story`: "Drag the story cards from oldest to youngest."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fossils (family "fossils"). Reuses fossil-clues's `/* FOSSILS DATA: begin */ ... /* end */` block (fossil records with living relatives and needs, the then-and-now slider) and adds layer records, the stacked board and the gap-in-time marker inside it.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Matches | Tap every place until one sticks | Each wrong match shows the clue again; the board needs a clue for each layer. |
| Order | Copy the layers top to bottom | The story asks oldest first, which is bottom up. |
| Story | Skip the clues | Each story card needs a clue attached. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: case file card; `welcome` (queued). `hike`; `lens`; `match`.
2. Pattern clue (whole), waits.
3. `story`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 4-ESS1-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Grand Canyon layers, their fossils and the places they formed in | National Park Service, Grand Canyon National Park, "Geology" and "Rock layers" | U.S. Geological Survey, "Geology of Grand Canyon" | yes |
| The Great Unconformity is a large gap in the rock record | National Park Service, Grand Canyon, "Great Unconformity" | U.S. Geological Survey, "The Great Unconformity" | yes |
| The Colorado River cut the canyon within the last several million years | National Park Service, Grand Canyon, "Geologic formations" | Karlstrom and colleagues, Science (2008) | yes |
| Grand Canyon is the homeland of traditionally associated Native nations | National Park Service, Grand Canyon, "Traditionally associated tribes" | Inter Tribal Council of Arizona, member nations | yes |
Backed twice: 5. Cut: 0.
Sensitivity note: the Grand Canyon is the homeland of Native nations, and the park works with eleven traditionally associated tribes; the case file names this first, says these nations hold their own knowledge of the canyon, links to their own sites, and does not retell their stories or show sacred places; a fresh review agent reads the case file before build.

Checks run (Python, scratchpad r29, 2026-11-09): eight stops; stop ages from the rim down (about 270, 275, 280, 340, 505 and 525 million years, then much older) rise at every step, so lower layers are older; six nations named; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 rock and guide; at 680x425 sheet.
2. Each of eight stops is matched to a place with a clue. (4-ESS1-1)
3. Three pattern clues order the layers and mark the gap in time. (4-ESS1-1)
4. The story is told oldest to youngest with a clue for each change and compared with the geologist. (4-ESS1-1)
5. The case file opens by naming the Native nations with care, with links to their own sites.
6. Layer facts match the park and survey sources.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: stops jump; no network requests.

## Open questions
- Sensitivity flag: the Grand Canyon as the homeland of Native nations (default used: opening card naming six nations and noting eleven associated tribes, links to the nations' own sites, no retelling of their stories or sacred places, fresh-agent read before build).
- The idea card flags a data source (default used: layer names, fossils and places from National Park Service Grand Canyon geology pages, checked against USGS).
