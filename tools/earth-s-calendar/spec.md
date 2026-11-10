# Earth's Calendar

## One idea
Three short rock columns from real places lie side by side unlabeled (the Grand Canyon in Arizona, the Grand Staircase in southern Utah and the Hell Creek badlands in Montana), with a fossil tray and an empty calendar ribbon below; the student taps layers to see their fossils, notices that the same index fossil in two columns means the same age and slides the columns into one tall stack, then places boundary markers where the fossils change most sharply (many kinds ending at once), and the tool snaps each marker to the named boundary it matches and adds its age from the international chart; finally the student drags the finished column onto a one-year calendar and watches 4.6 billion years squeeze in: animals with shells spread around November 19, the great dying at the end of the Permian falls on December 12, the dinosaurs other than birds vanish on December 26, and our species arrives about 34 minutes before midnight on December 31; the student writes why one boundary sits where it does, using the layers as evidence, so a sixth grader learns how rock strata and fossils are used to build the geologic time scale and organize Earth's 4.6-billion-year history.

## Not like
- canyon-reader (4, spec): one canyon's local story. Here many places stacked into one time scale.
- fossil-clues (3, spec): what fossils say about a past place. Here what they say about time.
- star-life-story (9, spec): a star's life line. Here Earth's.
- fossil-and-bone-bench (8, concept): fossils as evidence for change in life forms. Here fossils as clocks.

## Who and how
- Grade 6, Science, module "Geologic Time". Standard: MS-ESS1-4 (construct a scientific explanation based on evidence from rock strata for how the geologic time scale is used to organize Earth's 4.6-billion-year-old history).
- Format: timeline. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three columns with 16 layers in all, eight index fossils, five boundary markers, the calendar ribbon, the explanation card. Extra: Your lifetime (a button that shows a lifetime on the calendar). tool.json `modes: ["Columns", "Your lifetime"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ESS1-4 (strata) | Match index fossils and slide three columns into one stack | the columns; matching fossils glowing in pairs | 2 |
| MS-ESS1-4 (time scale) | Place markers where life changes most and see them become named boundaries | the markers; eras and periods; dated ages | 3 |
| MS-ESS1-4 (explanation) | Put the column on the calendar and explain one boundary | the calendar; the explanation card | 4 |

## Screens and modes
Header (kit): title "Earth's Calendar"; `Columns`, `Your lifetime`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** Three rock columns standing like slices of cake on a table, unlabeled, each from a different place on a small map. A fossil tray and an empty ribbon marked January to December. The welcome is queued (`welcomeAfter: true`): "These rocks come from three places. Can you line them up in time? Tap a layer to see what's inside." First hint: "Tap the top layer of the first column."

**The columns (focus: one layer).** At 1366x768 the three columns stand center with the fossil tray right and the ribbon below; at 680x425 one column shows at a time with a swipe and the tray is a sheet. Tapping a layer shows its fossils with a name and a picture. The Grand Canyon top (Kaibab Limestone) and the Grand Staircase bottom share fossils; the Grand Staircase top and Hell Creek share Cretaceous fossils. The student drags a column up or down until the matching layers line up; they lock with a click and a line between them.

**Markers (the time scale).** The stack now reads oldest at the bottom. The student drags five markers to where many fossils stop at once. Each marker snaps and names itself: the start of the Cambrian (538.8 million years ago), the end of the Permian (251.9), the end of the Triassic (201.4), the end of the Cretaceous (66.0), and the start of the record (the oldest rock, much older). Eras label the spans between: Paleozoic, Mesozoic, Cenozoic. A wrong spot says "Not yet. Look for a layer where many kinds of fossils stop."

**The calendar (the aha).** The student drags the stack onto the ribbon. Earth forms on January 1; the stack's ages map to dates: shelled animals around November 19, the great dying on December 12, the dinosaurs other than birds gone on December 26, our species about 34 minutes before midnight on December 31. Narrator: "Almost all of Earth's story happened before anything with a shell. People are the last half hour."

**The explanation card.** "The line between the ___ and the ___ sits here because ___. The rocks show ___." The student picks one boundary and fills it with evidence from the layers.

**The end.** The stack, the calendar and the explanation on one page. `Print` prints it.

**Your lifetime (extra).** A button lights the last 0.08 seconds of December 31 for an 11-year-old.

## Content
- Three simplified teaching columns from published sections (16 layers), eight index fossils (trilobites, brachiopods, crinoids, ammonites, a Triassic plant, Cretaceous shellfish, a dinosaur bone, a Paleocene mammal tooth), five boundaries with ages from the International Commission on Stratigraphy chart, the calendar, the explanation card.
- A note: "Columns are simplified; real ones have many more layers."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Columns slide only up or down; markers snap to the nearest layer line.
- Keyboard: Tab to layers, columns, markers and the ribbon; arrows slide a column; Enter places.
- With Motion off columns jump to place and the calendar fills at once.

## Look
- Accent `--brand` #6b3f7a strata plum (header, markers, the ribbon); gold #f4c542 (matching fossils, the marker in hand); paper #f7f2f8; ink #1e1022; muted #5a4f5d.
- Contrast (WCAG 2.1, computed): white on brand 8.02:1; brand on paper 7.26:1; ink on paper 16.50:1; muted on paper 7.01:1; ink on gold 11.20:1.
- Never color alone: layers carry names and patterns; eras carry labels.
- Different from this batch (schoolyard brick, cell green, current blue, magma red).

## Art
- Local FLUX (`scripts/localart.py`): one landscape strip per era (Paleozoic sea, Mesozoic forest, Cenozoic grassland) (3, 16:9).
- Fossils: public domain or openly licensed photos where found and checked, otherwise generated and labeled (8, 1:1).
- Drawn in code: the columns, layers, markers, the calendar ribbon, the map.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the calendar narrator; `knowing-guide` as the field geologist and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.layer + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `layer`: "Tap a layer to see its fossils."
- how `match`: "Drag a column until the matching fossils line up."
- how `marker`: "Drag a marker to where many fossils stop."
- how `calendar`: "Drag the stack onto the calendar."
- event, whole, the calendar dates.
- how `explain`: "Pick a boundary and fill in the card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the columns, matching, markers, the calendar. Columns, fossils and boundary ages sit in a marked block `/* EARTH-S-CALENDAR DATA: begin */ ... /* end */`, with fossil records shaped like the FOSSILS DATA block in fossil-clues so they can be shared later.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Matching | Slide columns at random | They lock only where shared fossils line up. |
| Markers | Drop markers evenly | Only lines where many fossils stop snap. |
| Explanation | Name a boundary only | The card needs what the layers show above and below it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `layer`; `match`.
2. `marker`; `calendar`.
3. Calendar dates (whole), waits.
4. `explain`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-ESS1-4 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Boundary ages 538.8, 251.9, 201.4 and 66.0 million years | International Commission on Stratigraphy, International Chronostratigraphic Chart (2023) | U.S. Geological Survey, "Divisions of Geologic Time" (Fact Sheet 2010-3059, updated) | yes |
| Earth is about 4.6 billion years old | U.S. Geological Survey, "Age of the Earth" | NASA, "How Old Is Earth?" (Space Place) | yes |
| Kaibab Limestone tops the Grand Canyon and forms the base of the Grand Staircase | National Park Service, Grand Canyon geology | National Park Service, Bryce Canyon, "Grand Staircase" | yes |
| Hell Creek holds the end-Cretaceous boundary with dinosaur fossils below it | Bureau of Land Management, Hell Creek paleontology | U.S. Geological Survey, "K-T boundary" | yes |
| Homo sapiens arose about 300,000 years ago | Smithsonian National Museum of Natural History, Human Origins | Natural History Museum (London), "Homo sapiens" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r1, 2026-11-10): on a 4,600 million year calendar, 538.8 falls on November 19, 251.9 on December 12 and 66 on December 26; 300,000 years is 34 minutes; 11 years is 0.08 seconds; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 three columns with tray and ribbon; at 680x425 swipe and sheet.
2. Three columns are matched into one stack by shared fossils. (MS-ESS1-4)
3. Five markers snap to named boundaries with ages. (MS-ESS1-4)
4. The stack is placed on the calendar and one boundary is explained with layer evidence. (MS-ESS1-4)
5. Boundary ages match the cited chart and calendar dates match them.
6. The simplified-columns note shows.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps and instant fill; no network requests.

## Open questions
- The idea card flags a data source (default used: boundary ages from the 2023 International Chronostratigraphic Chart, simplified columns from NPS and BLM published sections, index fossils checked against each site before build; calendar dates computed from them).
