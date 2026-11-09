# Fact Fusion

## One idea
Three sources on the Wright brothers' first flights of December 17, 1903 (an encyclopedia-style page, Orville Wright's own telegram and diary, and a museum page with a map) pour their facts into one table with a column per source, and the student filters for what all agree on, what only one says and where they clash (the telegram says the longest flight lasted 57 seconds; the others say 59), works out why each clash happened, and builds a short report where every sentence carries its source tags, so they learn that combining sources means tracking who said what and noticing why accounts differ.

## Not like
- research-rover (4, spec): investigating a topic from many sides into an outline. Here three sources fused in a table and a report, grade 5.
- eyewitness-vs-reporter (4, spec): two accounts compared. Here three sources combined into one report.
- source-mixer (11, concept): synthesis at grade 11. Here grade 5 fact tracking.
- note-card-shuffle (3, spec): notes into pockets. Here facts in a source-by-source table.
- claim-court (5, spec): an author's support. Here facts from several sources.

## Who and how
- Grade 5, ELA, module "Using Multiple Sources" (Reading Informational Text and Writing). Standards: RI.5.6, RI.5.7, RI.5.9, W.5.7, W.5.8.
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap; the student's report is read back by the browser's speech voice.
- Topic: The First Flights (December 17, 1903). tool.json `modes: []`, `minutes: "30-45"`, `grades_label: "Grade 5"`.
- Saving: the table and report are kept in this browser (research engine Store); footer: "Your work stays on this device." `Clear my work` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.5.8 | Highlight a fact in a source, write it in a few words, and drop it in the table; matching facts from other sources join its row | the fact table with a column per source | 2 |
| RI.5.9 | Filter rows: all agree, only one says, disagree | the filtered table | 3 |
| RI.5.6 | For each clash row, check who was there and when each source was written, and pick why they differ | the clash card with a "why" line | 4 |
| RI.5.7 | Quick-find cards: answer a question fast from the map, the date line or the photo caption | the answer and the feature used | 5 |
| W.5.7, RI.5.9 | Build the report from table rows; each sentence shows its source tags; untagged sentences turn red | the report and the sources list | 6 |

## Screens and modes
Header (kit): title "Fact Fusion"; `Sources`, `Table`, `Report`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A workbench in an old bicycle shop with three source cards pinned up and an empty table on the bench, and Spoke, a cheerful bicycle-bell robot. First hint: "Tap a source card to open it." The first tap reads the source's title; the welcome is queued after it (`welcomeAfter: true`).

**Sources (A, B, C).**
- A: "The First Flights", an encyclopedia-style page written for Curio Class from sourced facts (who, where, four flights, distances and times, the photo, what happened after).
- B: Orville Wright's own words: his telegram to his father (exact text, public domain) and a short adapted passage from his diary for that day, labeled adapted.
- C: a museum-style page written for Curio Class from the Smithsonian's and the Park Service's facts, with a map of the Outer Banks (Kitty Hawk, Kill Devil Hills four miles south, the camp) and the 1903 photo of the fourth landing with its caption.
Each opens in the reader; tap sentences to hear them.

**Table.** The research engine's Matrix (`R.matrix`): rows are facts, columns are A, B and C, each cell states, differs or silent. The student highlights a segment and writes the fact in a few words (`R.closeness` wrinkles 5-word copies). When a fact matches an existing row (same row id in data), it joins that row.

**Filters.** All agree (four flights on December 17; Orville flew first), Only one says (the camera was set up by Orville and the shutter pressed by a lifesaving station man, from C), Disagree.

**Clash cards.** Three clashes in data (`R.conflicts`):
1. Longest flight: 57 seconds (B, telegram) against 59 seconds (A and C). Why: the telegram was relayed through two offices and the number changed in transmission; the same telegram misspelled Orville's name.
2. Place: Kitty Hawk (B, telegram, sent from the Kitty Hawk weather station) against near the Kill Devil Hills, about four miles south (C). Why: Kitty Hawk was the nearest settlement and the telegram office.
3. Wind: "twenty one mile wind" (B) against "more than 20 miles an hour" (A). Why: these agree once you read closely; one gives a reading, one a range. (A clash that isn't one.)
For each, the student picks why from four reasons (one was there, one was written later; a mistake in copying or sending; a different name for the place; they actually agree) and writes one sentence.

**Quick find.** Four timed (gentle, no penalty) cards: "How far is Kill Devil Hills from Kitty Hawk?" (the map), "What time was the famous photo taken?" (the caption), "Who flew last?" (A's date line), "How many people were watching?" (C). The student picks the feature they used; the card says whether that feature was the fastest one.

**Report.** Sentence frames fill from table rows; each sentence shows tags (A, B, C). `R.trace` marks each sentence: own idea, no source (red), one source, synthesis. The report needs at least one synthesis sentence and one sentence about a clash. The sources list writes itself (`R.cite` 'simple').

At 1366x768 the reader and table fit side by side; at 680x425 the table is a tab.

## Content
- A and C written for Curio Class from sourced facts (Sources table). B: the telegram exact; the diary passage adapted for grade 5 from the Library of Congress's Wright Papers, marked adapted.
- Facts: four flights on December 17, 1903; first by Orville, 12 seconds, 120 feet; the fourth by Wilbur, 59 seconds, 852 feet; the plane was wrecked by a gust after the fourth flight; the photo of the first flight was taken by John T. Daniels of the Kill Devil Hill Lifesaving Station on Orville's camera; the brothers walked four miles to the Kitty Hawk weather station to send the telegram.
- Images: Library of Congress photograph of the fourth flight's landing (item 2001696559) and the first flight photograph (Wright Papers, "First Flight" highlight), both public domain.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Facts can be edited, moved to another row or recycled.
- Quick-find timing shows seconds but never scores.
- With Motion off the filters change without sliding.

## Look
- Accent `--brand` #1f5f8b sky blue (header, table rules, tags); gold #f4c542 (agree rows, the Flyer's wings in the logo); paper #f2f7fb; ink #0b1e2c; muted #4e5d69. Scene: a sunny bicycle shop workbench.
- Contrast (WCAG 2.1, computed): white on brand 6.84:1; brand on paper 6.35:1; ink on paper 15.75:1; muted on paper 6.29:1; ink on gold 10.44:1.
- Never color alone: cells say states, differs or silent; red sentences also show "no source".
- Different from this batch (storm violet, pumpkin, granite green, museum burgundy).

## Art
- Public domain: two Library of Congress photographs (above).
- Local FLUX (`scripts/localart.py`): bicycle shop workbench (1); Spoke (4 poses: ring, point, think, cheer), "A friendly small robot made from a brass bicycle bell and spokes <pose>, soft gouache, plain white background"; 1:1; cutout yes.
About 7 images. Drawn in code: map, table, report.

## Voice
Bank voice `curious-librarian` as Spoke (unique in this batch); Orville's telegram and diary are read by `firm-captain` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.row`, `welcomeAfter: true`.
- how `welcome`: "Three sources, one big day. Put every fact in the table, and keep track of who said it."
- event, whole, `segment`: the tapped sentence.
- event `joined`: "Source {C} says this too. It joined the row."
- event `clash`: "{57} seconds or {59}? Find out why they differ."
- event `quick`: "Found it in {5} seconds with {the map}."
- event `noSource`: "This sentence has no source. Which row did it come from?"
- event `report`: the report, read whole.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
research (`kit/research.js`), described in full in tools/question-sharpener/spec.md, exposed as `R`. This tool uses: Source, Shelf and Reader, Note (`R.closeness`, threshold 5), Matrix (`R.matrix`, the fact table), Conflicts (`R.conflicts`, three clash pairs), Trace (`R.trace` for report sentences), Cite (`'simple'`), Store (`ff-work`). Not Board, Weight or Question.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Table | Copy whole sentences | Copies wrinkle; rows join only by meaning in data, so a fact in the wrong row stays alone. |
| Clashes | Pick any reason | Each clash has one best reason in data; the third clash's answer is "they agree", which guessing rarely finds. |
| Report | Write without tags | `R.trace` turns untagged sentences red; the report needs a synthesis sentence and a clash sentence. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a source: title, `welcome` (queued, first time).
2. Sentences: `segment` (whole). Facts: `joined` as it fires.
3. Clashes: `clash`. Quick find: `quick`.
4. Report: `noSource` as it fires; `Play`: `report`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.5.6, RI.5.7, RI.5.9, W.5.7, W.5.8 wording | thecorestandards.org, Grade 5 | CCSS ELA 2010 PDF | yes |
| Four flights on December 17, 1903; Orville first, 12 seconds, 120 feet; Wilbur fourth, 59 seconds, 852 feet | Library of Congress, telegram record mcc.061 notes (checked 2026-11-09) | Library of Congress, photograph item 2001696559 caption | yes |
| The telegram turned 59 seconds into 57 in transmission and misspelled Orville's name; the brothers walked four miles to the Kitty Hawk weather station to send it | Library of Congress, telegram record mcc.061 (checked 2026-11-09) | Library of Congress, telegram item 2003680165 | yes |
| The flights were near the Kill Devil Hills, about four miles south of Kitty Hawk | National Park Service, Wright Brothers National Memorial | Library of Congress, Wright Papers "First Flight" | yes |
| John T. Daniels of the Kill Devil Hill Lifesaving Station took the first flight photo with Orville's camera | Library of Congress, Wright Papers "First Flight" (checked 2026-11-09) | Smithsonian National Air and Space Museum, 1903 Wright Flyer | yes |
Backed twice: 5. Cut: 1 (an early newspaper's wrong account of the flights; the exact newspaper text couldn't be checked twice, so it's left out).

Checks run (Python, scratchpad b16, 2026-11-09): the sample table has at least two all-agree rows, one only-one row and three clash rows, one of which resolves as agreement; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the reader and table fit; at 680x425 the table is a tab.
2. Facts drop into the table and join rows. (W.5.8)
3. Filters show agree, only one and disagree rows. (RI.5.9)
4. Clash cards take a reason and a sentence. (RI.5.6)
5. Quick-find cards record the feature used. (RI.5.7)
6. The report marks untagged sentences and builds the sources list. (W.5.7)
7. Work survives a reload where storage works; `Clear my work` removes it.
8. Print shows the table and report.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: filters don't slide; no network requests.

## Open questions
- None for Cory.
