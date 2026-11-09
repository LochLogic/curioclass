# Research Rover

## One idea
The student drives a little rover through a mini library of kid articles, a map, a chart and an interview to investigate one topic from several sides (monarch butterflies: where they go and why there are fewer), beaming notes in their own words into the cargo bay, each stamped with its source, while a mission board lights the sides that have notes; at one stop two articles give different numbers and the student writes one sentence that is true to both, and the cargo unloads into an outline and a sources list, so they learn that research looks at a topic from different angles and keeps track of where every fact came from.

## Not like
- note-card-shuffle (3, spec): notes from three pages into pockets. Here several kinds of source, sides of a topic, a sources list and combining two texts.
- fact-fusion (5, concept): a report from three sources. Here an outline is the end, at grade 4.
- question-sharpener (12, spec): pricing a research question. Here a set question.
- eyewitness-vs-reporter (4, spec): firsthand and secondhand accounts. Here many sources on one topic.
- structure-spotter (3, spec): finding answers on a fact site. Here gathering across sources.

## Who and how
- Grade 4, ELA, module "Short Research Projects" (Writing). Standards: W.4.7, W.4.8, RI.4.9.
- Driver: one student (tool.json `driver: "student"`). Every source is read on tap; typed notes are read back by the browser's speech voice.
- Two missions: "Monarch Butterflies: Where Do They Go, and Why Are There Fewer?" and "Honeybees: How Does a Hive Work, and What Helps Them?". tool.json `modes: []`, `minutes: "30-45"`, `grades_label: "Grade 4"`.
- Saving: the cargo is kept in this browser (research engine Store); footer: "Your notes stay on this device." `Clear my cargo` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.4.8 (recall) | Load a "what I know" note and an optional "my own observation" note before driving | notes with a house icon and an eye icon | 2 |
| W.4.8 (gather, print and digital) | Drive to shelves: two articles, a web page, a map, a chart and an interview transcript | the source cards on the floor plan | 3 |
| W.4.8 (notes, categories) | Beam notes in a few words; each is stamped with its source and dropped on a side of the mission board | the mission board's four sides lighting | 3, 4 |
| W.4.7 | The mission needs notes on every side and from at least three kinds of source | the board and a source-kind count | 4 |
| RI.4.9 | At the disagreement stop, write one sentence that uses both articles' numbers accurately | the combined sentence with both stamps | 5 |
| W.4.8 (list of sources) | Unload: the outline and the sources list are built from the stamps | the outline and the list | 6 |

## Screens and modes
Header (kit): title "Research Rover"; `Missions`, `Cargo`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A library floor plan seen from above with aisles (Science, History, Maps, Interviews, Web) and Rova, a small six-wheeled rover with a camera eye and a cargo bay. First hint: "Tap a mission card to load it." The first tap reads the mission; the welcome is queued after it (`welcomeAfter: true`).

**Launch pad.** Two optional notes: "What I know" and "My own observation" (things the student has seen, like a monarch in the yard).

**Drive.** Tap a shelf (or use arrow keys) and the rover drives there. Each stop opens a source in the reader: tap sentences to hear them, pick a segment, then type a note (up to 15 words). The research engine's `R.closeness` wrinkles a note with a run of 5 or more words copied from the segment ("Try it in your own words."). The note is stamped with the source's icon and title and the student picks its side.

**Mission board.** Four sides for the monarch mission: The Journey, The Life Cycle, Threats, Helpers. Each side lights by its note count; an empty side shows "Nothing yet" and a `Where to look` button that highlights a shelf with a fact for it (data); a side with 6 or more notes says "Crowded! Any repeats?" A counter shows source kinds used (article, web page, map, chart, interview).

**Disagreement stop.** Two articles give different estimates of how many monarchs fit in one hectare of winter forest (one says about 21 million, the other says estimates vary widely, from under 10 million to over 50 million). Rova flashes both stamps: "These two don't match. Write one sentence that's true to both." The sentence frame suggests "Scientists estimate ___, and one common estimate is ___." The sentence must mention both stamps (the student taps them in) and include a number from each.

**Unload.** When every side has a note and three source kinds are used, `Unload` builds an outline (sides as headings, notes as bullets, stamps as small superscript numbers) and a sources list (title, kind, author or group; `R.cite` 'simple'). A side with no notes sends the rover back out instead. The outline prints.

At 1366x768 the floor plan and reader fit side by side; at 680x425 the reader slides over the plan.

## Content
Sources written for Curio Class from sourced facts (each source names a made-up kid publication or the real agency whose facts it uses, labeled as written for Curio Class):
- Monarchs: eastern monarchs migrate up to about 3,000 miles to winter in fir forests in central Mexico; western monarchs winter along the California coast; a migration takes several generations, and the last fall generation lives much longer (up to about 8 or 9 months); caterpillars eat only milkweed; threats are loss of milkweed and winter forest, pesticides and extreme weather; helpers plant native milkweed and nectar flowers. The map shows the eastern flyway; the chart shows the area of winter forest the eastern monarchs covered in Mexico in some winters (from about 18 hectares in 1996-97 to under 1 hectare in 2013-14, with ups and downs since); the interview is with a made-up schoolyard garden volunteer.
- Honeybees: a hive has one queen, thousands of workers and some drones; workers do jobs by age; bees make honey from nectar; helpers plant flowers and limit pesticides. Map: none; chart: what a worker bee does at each age.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Driving is a short animation; with Motion off the rover jumps to the shelf.
- Notes can be edited, moved between sides or recycled.
- The closeness check lets names and numbers repeat (milkweed, 3,000 miles); only 5-word runs of other words wrinkle.

## Look
- Accent `--brand` #3a4f8f rover indigo (header, rover, board frame); gold #f4c542 (lit sides, stamps); paper #f3f5fb; ink #121a30; muted #4f5670. Scene: a library floor plan like a map.
- Contrast (WCAG 2.1, computed): white on brand 7.79:1; brand on paper 7.15:1; ink on paper 15.84:1; muted on paper 6.65:1; ink on gold 10.62:1.
- Never color alone: sides show counts and words; stamps show icons and titles.
- Different from this batch (root plum, card red, chameleon green, glacier teal).

## Art
Local FLUX (`scripts/localart.py`), no people in focus.
- source pictures (8): "<monarchs clustered on fir trees in Mexico / a monarch caterpillar on milkweed / a schoolyard pollinator garden / honeybees on a comb>, realistic illustration, no text"; 4:3.
- Rova (3 views), "A cute small six-wheeled library rover robot with a camera eye and a cargo bay <view>, soft gouache, plain white background"; 1:1; cutout yes.
About 11 images. Drawn in code: floor plan, map, chart, board, outline.

## Voice
Bank voice `lively-host` as Rova (unique in this batch); sources are read by Rova too. `Curio.voice` with `scope: () => state.mission + ':' + state.stop + ':' + state.step`, `welcomeAfter: true`.
- event `mission`: "Mission: {Monarch butterflies. Where do they go, and why are there fewer?}"
- how `welcome`: "Researchers look at a topic from every side, and they keep track of where each fact came from. Drive to a shelf to start."
- event, whole, `segment`: the tapped sentence.
- how `noteHow`: "Write the fact in a few words, then pick its side on the board."
- event `wrinkle`: "Try it in your own words."
- event `clash`: "These two don't match. Write one sentence that's true to both."
- event `empty`: "Nothing yet on {Helpers}. Tap Where to look."
- event `unload`: "Cargo unloaded! Here's your outline and your sources."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
research (`kit/research.js`), described in full in tools/question-sharpener/spec.md, exposed as `R`. This tool uses: Source (title, kind, author and segments), Shelf and Reader, Note (`R.note` paraphrase with `R.closeness`, run threshold 5), Board (four sides, empty and crowded readouts, crowded at 6), Trace (stamps on notes and the combined sentence's two sources), Conflicts (`R.conflicts` holds the hectare estimates as a known disagreement), Cite (`'simple'`), Store (`rr-cargo`). Not Weight, Matrix or Question.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sides | Put every note on one side | Unload needs every side lit. |
| Source kinds | Use one article | Unload needs three source kinds. |
| Combined sentence | Use one number | It needs both stamps and a number from each source. |
| Own words | Copy | 5-word runs wrinkle the note. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a mission: `mission`, `welcome` (queued, first time).
2. Stops: `segment` (whole); first note: `noteHow`; copies: `wrinkle`.
3. Disagreement stop: `clash`.
4. Readouts: `empty`. Unload: `unload`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.4.7, W.4.8, RI.4.9 wording | thecorestandards.org, Writing and Reading Informational Grade 4 | CCSS ELA 2010 PDF | yes |
| Eastern monarchs migrate up to about 3,000 miles to fir forests in central Mexico; western monarchs winter on the California coast; several generations a year, the fall generation living much longer | US Fish and Wildlife Service, monarch butterfly | National Park Service, monarch butterfly migration | yes |
| Monarch caterpillars eat only milkweed; threats are habitat loss, pesticides and weather; planting native milkweed helps | US Forest Service, monarch butterfly biology and conservation | Xerces Society, monarch conservation | yes |
| Eastern monarch winter forest area: about 18 hectares in 1996-97 and under 1 hectare in 2013-14 | WWF Mexico, monarch overwintering surveys | Monarch Watch, population status | yes |
| Monarch density per hectare: about 21.1 million is a common estimate; published estimates vary widely, from under 10 million to over 50 million | Thogmartin and others (2017), "Density estimates of monarch butterflies overwintering in central Mexico", PeerJ | Monarch Watch, monarch population status and density notes | yes |
| A hive has one queen, workers and drones; workers change jobs with age | USDA Agricultural Research Service, honey bee biology | Penn State Extension, honey bee colony | yes |
Backed twice: 6. Cut: 1 (a "one billion monarchs in the 1990s" figure; sources give different numbers, so the chart uses forest area instead).

Checks run (Python, scratchpad b14, 2026-11-09): every side of both missions has at least one fact across the sources; the two estimates differ, and a sample combined sentence holds a number from each; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the plan and reader fit; at 680x425 the reader slides over.
2. What-I-know and observation notes load with their icons. (W.4.8)
3. Notes are stamped and placed on sides. (W.4.8)
4. Unload needs every side and three source kinds. (W.4.7)
5. The disagreement stop needs both stamps and a number from each. (RI.4.9)
6. The outline and sources list build from the stamps and print. (W.4.8)
7. The cargo survives a reload where storage works; `Clear my cargo` removes it.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the rover jumps to shelves; no network requests.

## Open questions
- None for Cory.
