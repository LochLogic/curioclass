# Glossary Makers

## One idea
The student builds the glossary page for a short science or history passage: for each bold word they gather clues from three trays (the sentence around it, its word parts, a picture), write a kid definition with a synonym and an opposite, and test the entry by hearing the passage read with their definition swapped in, which must still make sense, so they learn that subject words can be worked out, not just looked up; a later passage brings the same words back to show they stuck.

## Not like
- word-lab (2, spec): word parts in beakers. Here subject words in a passage at grades 3-5.
- root-detective-cards (4, concept): a root card game. Here roots as one clue tray beside context and pictures.
- context-roots-dictionary (6-8, concept): older readers and a dictionary. Here a kid glossary page.
- idiom-illustrator (3-5, spec): figurative language. Here exact subject words.
- note-card-shuffle (3, spec): notes on facts. Here definitions of words.

## Who and how
- Grades 3-5, ELA, module "Academic and Subject Words" (Language). Standards: RI.3.4, L.3.6, RI.4.4, L.4.5c, L.4.6, RI.5.4, L.5.4, L.5.6. L.4.5a and b moved to idiom-illustrator's grade 4 deck, as the idea card says.
- Driver: one student (tool.json `driver: "student"`). Every passage sentence and clue is read on tap; typed definitions are read back by the browser's speech voice.
- Three passages by grade: grade 3 "Beavers Build a Dam", grade 4 "Inside the Rain Forest Layers", grade 5 "Digging the Erie Canal"; each with 5 bold words and a second "new passage" using them. tool.json `modes: []`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.
- Saving: the glossary page is kept in this browser; footer: "Your glossary stays on this device." `Clear my glossary` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.3.4, RI.4.4, RI.5.4 | Work out each bold word from its clue trays and test the definition by swapping it into the passage | the swap test reading with the definition in place | 2, 3 |
| L.5.4 (a, b, c) | Use context, the Greek or Latin part tray, then check on the reference shelf (a print-style dictionary page) | the parts tray and the shelf entry | 2, 4 |
| L.4.5c | Pick a synonym and an opposite for each entry | two chips on the entry | 3 |
| L.4.6 | Precise word round: pick the exact word (gnawed, not ate; drenched, not wet) for the passage | a plain word and three precise choices | 5 |
| L.3.6 | Use time and place phrases (after dusk, upstream of the lodge) in the link round | phrase chips in the student's sentence | 6 |
| L.5.6 | Join two glossary facts with however, similarly, in addition or although | the joined sentence | 6 |

## Screens and modes
Header (kit): title "Glossary Makers"; `Passages`, `My glossary`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A book editor's desk with a book open to a passage and an empty glossary page, and Professor Hedge, a hedgehog with reading glasses and a red pencil. First hint: "Tap a passage to open the book." The first tap opens it; the welcome is queued after it (`welcomeAfter: true`).

**Passage.** The passage on the left with 5 bold words; the glossary page on the right with 5 empty entries in alphabetical order.

**Clue trays.** Tapping a bold word opens three trays:
1. Sentence: the sentence and the one before it, with clue words underlined (data).
2. Word parts: the word split into parts with meanings (lodge has none, and the tray says "No parts to help here. Lean on the other trays."; grade 5 words carry Latin or Greek parts: aqueduct = aqua + duct).
3. Picture: a labeled picture.
The student writes a definition (up to 20 words).

**Swap test.** `Test it` reads the passage sentence with the definition swapped in for the word ("The beavers swam back to their [home of sticks and mud] at dusk."). The student judges: makes sense or doesn't. The tool also checks the definition against the entry's key-idea word groups (data, generous forms); if none match, Professor Hedge says "Hmm, does the sentence still make sense? Check the picture tray."

**Synonym and opposite.** Two chip rows: pick a synonym and an opposite (or "no opposite" where none fits: canal). Wrong picks show why ("Flood is not the opposite of dam").

**Reference shelf.** A print-style dictionary page drawn in code with guide words and the entry's dictionary meaning; the student compares and may edit.

**Precise word round.** Five passage sentences with a plain word (ate, wet, went); pick the precise one that fits (gnawed, drenched, paddled); the reason is read.

**Link round.** Two glossary facts and four joiners; the student builds one sentence, adding a time or place phrase chip.

**New passage check.** A second passage uses the same words without bold; tapping a word shows the student's own glossary entry; three questions check meaning.

At 1366x768 the passage and glossary fit side by side; at 680x425 the glossary is a tab.

## Content
Passages written for Curio Class from sourced facts.
- Grade 3 "Beavers Build a Dam": dam, lodge, gnaw, current, pond. Beavers gnaw trees with strong front teeth, build dams of sticks and mud, and live in a lodge with an underwater entrance.
- Grade 4 "Inside the Rain Forest Layers": canopy, understory, emergent, humid, decompose. Layers: emergent, canopy, understory, forest floor.
- Grade 5 "Digging the Erie Canal": canal, aqueduct (aqua water, duct lead), excavate (ex out, cavus hollow), navigate (navis ship), transport (trans across, port carry). The canal opened in 1825 from the Hudson River to Lake Erie.
- New passages: "A Beaver Comes Home", "A Toucan's Day", "Packet Boats on the Canal".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Definitions are plain text; the browser voice reads them; no definition is refused.
- The glossary prints as a book page.

## Look
- Accent `--brand` #5a3e8c word violet (header, bold words, entry rules); gold #f4c542 (tested entries, trays); paper #f6f3fb; ink #1a1229; muted #594f68. Scene: a book editor's desk.
- Contrast (WCAG 2.1, computed): white on brand 8.39:1; brand on paper 7.65:1; ink on paper 16.46:1; muted on paper 6.97:1; ink on gold 11.11:1.
- Never color alone: bold words are bold; tested entries carry a check and "tested".
- Different from this batch (lagoon teal, brick orange, storm slate, kite magenta).

## Art
Local FLUX (`scripts/localart.py`); history scenes show workers small and from a distance.
- desk (1); Professor Hedge (4 poses: read, point, think, cheer), "A friendly hedgehog professor with reading glasses and a red pencil <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- clue pictures (15): "<a beaver gnawing a tree / rain forest layers cutaway / an aqueduct carrying a canal over a river>, labeled-diagram style, no text"; 4:3; cutout no.
- passage scenes (6); 16:9.
About 22 images. Drawn in code: book, trays, dictionary page, chips.

## Voice
Bank voice `calm-professor` as Professor Hedge and the passage reader (unique in this batch). `Curio.voice` with `scope: () => state.passage + ':' + state.word + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "This book needs a glossary. For each bold word, look at the clues, write a meaning in your own words, then test it."
- event `word`: "{Lodge}. Let's find clues."
- event, whole, `sentence`: the tapped sentence.
- event `swap`: the swapped-in sentence.
- event `hmm`: "Hmm, does the sentence still make sense? Check the picture tray."
- event `tested`: "Tested and ready for the book."
- how `preciseHow`: "Pick the word that says exactly what happened."
- how `linkHow`: "Join these two facts with one of the joining words."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (word-lab is a single tool, not a family engine). Tool-only code: clue trays, swap test, chips, dictionary page, glossary page.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Swap test | Copy the dictionary entry | The shelf opens only after a first definition is tested; copying is checking, and the swap test still applies. |
| Key idea | Type one key word | Passes the check, but the swap test reads the sentence aloud, which makes a one-word meaning sound wrong. |
| Synonym and opposite | Guess | 4 chips each; wrong picks explain; the entry keeps only the right ones. |
| New passage | Guess | Three questions per passage, 4 choices each; wrong answers point to the glossary entry. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a passage: `welcome` (queued, first time).
2. Tap a bold word: `word`; tray sentences: `sentence` (whole).
3. Test it: `swap`, then `tested` or `hmm`.
4. Rounds: `preciseHow`, `linkHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| The eight standards' wording | thecorestandards.org, Reading and Language Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Beavers gnaw trees, build dams of sticks and mud, and live in lodges with underwater entrances | US Fish and Wildlife Service, beaver | National Park Service, beavers | yes |
| Rain forest layers: emergent, canopy, understory, forest floor; humid; decomposers break down leaf litter | Smithsonian Tropical Research Institute, rain forest | Rainforest Alliance, rain forest layers | yes |
| The Erie Canal opened in 1825, linking the Hudson River to Lake Erie, with aqueducts over rivers | New York State Canal Corporation, history | National Park Service, Erie Canalway | yes |
| Word origins: aqua (water), duct (lead), ex (out), cavus (hollow), navis (ship), trans (across), portare (carry) | Merriam-Webster, etymologies | Online Etymology Dictionary | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b12, 2026-11-09): every grade has 5 bold words, each appearing again in its new passage; grade 5 part splits rebuild each word's spelling; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the passage and glossary fit; at 680x425 the glossary is a tab.
2. Each bold word opens three clue trays. (RI.x.4, L.5.4)
3. The swap test reads the definition in place; synonym and opposite chips work. (RI.x.4, L.4.5c)
4. The reference shelf opens after a first test. (L.5.4c)
5. The precise word round works. (L.4.6)
6. The link round joins facts with joiners and time or place phrases. (L.5.6, L.3.6)
7. The new passage check shows the student's own entries.
8. The glossary survives a reload where storage works and prints.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: trays open without sliding; no network requests.

## Open questions
- None for Cory.
