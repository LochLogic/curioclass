# Memoir and Biography

## One idea
The student reads three tellings of one morning in April 1887, when Helen Keller understood that the word spelled into her hand meant water: Helen's own memoir (1903), Anne Sullivan's letter written that same day, and a short biography written for Curio Class; they tag how each introduces Helen, which anecdotes it picks and what it wants readers to think, line up where the three differ (Helen remembers a fight over "mug" and "water" and a broken doll before they went out; Sullivan writes that the trouble was "mug" and "milk", and she was the one pumping), and then decide how the biography should handle the difference, so they learn that how a person is presented depends on who is telling and why.

## Not like
- portrait-in-four-media (10, concept): four media on one scientist. Here memoir, letter and biography on one morning, grades 6-8.
- two-authors-one-event (7, concept): two articles' spin on one event. Here a person presented by herself, her teacher and a biographer.
- fact-check-desk (8, concept): conflicting facts in arguments. Here conflicting memories in life writing.
- eyewitness-vs-reporter (4, spec): firsthand and secondhand. Here grades 6-8 point of view and how a person is introduced.
- fact-fusion (5, spec): facts in a table. Here people, anecdotes and point of view.

## Who and how
- Grades 6-8, ELA, module "How Authors Present People and Ideas" (Reading Informational Text). Standards: RI.6.3, RI.6.6, RI.6.9, RI.7.3, RI.8.3, RI.8.6.
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap.
- One morning, three texts; grade picker sets the tags (grade 6: introduce, anecdote, point of view; grade 7 adds links between people, events and ideas; grade 8 adds comparisons the authors draw and the conflict round). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "30-40"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the comparison table and the student's biography sentences.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.6.3 | Tag how Helen is introduced and the anecdotes each text uses | highlights by type | 2 |
| RI.6.6 | Tag where each author's point of view shows, and name it in a line | point-of-view tags and lines | 2 |
| RI.6.9 | The comparison table fills: only the memoir tells, only the letter tells, the biography adds | the three-column table | 3 |
| RI.7.3 | Link people, events and ideas (Sullivan's method, the pump, the word) with labeled threads | threads between highlights | 4 |
| RI.8.3 | Tag comparisons and analogies an author draws ("as one transfixed", "awakened my soul") and say what each connects | comparison tags | 4 |
| RI.8.6 | Conflict round: choose how the biography handles the different accounts and write the two sentences | the student's sentences and a real example | 5 |

## Screens and modes
Header (kit): title "Memoir and Biography"; `Desk`, `Table`, `Conflict`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A reading desk with three documents (a book open to chapter 4, a folded letter, a printed biography page), a photograph of Helen Keller and Anne Sullivan, and a reading lamp. The host is Mr. Abernathy, a librarian in the reading room (seen only as a voice and a hand on the lamp). First hint: "Tap the memoir to start reading." The first tap reads its title; the welcome is queued after it (`welcomeAfter: true`).

**The texts.**
- Memoir: Helen Keller, "The Story of My Life" (1903), chapter 4, from "One day, while I was playing with my new doll" through leaving the well-house (exact text, about 450 words).
- Letter: Anne Sullivan's letter of April 5, 1887, printed in the same 1903 book (exact text, about 400 words).
- Biography: written for Curio Class (about 400 words) on Helen's whole life with this morning as one paragraph, naming its sources.
A note at the start says Helen was six, deaf and blind from an illness at 19 months, and that the three texts were written by Helen at 22, by Sullivan that day, and by a writer today.

**Tag.** Highlight types: Introduces Helen, Anecdote, Point of view shows, Link (grade 7), Comparison (grade 8). The student selects a span and picks a type; the key rates spans so a mismatched tag gets "One reading tags this as {anecdote}."

**Table.** Three columns fill from tags: what only the memoir tells (what it felt like; the doll; the honeysuckle), what only the letter tells (what Sullivan tried first; that she pumped; the nurse and baby sister after), what the biography adds (later life, the wider view). The student moves rows that land in the wrong column.

**Timeline row.** One row shows that morning step by step from each telling. Three differences light: the trouble before (mug and water, memoir; mug and milk with "drink", letter), the doll (memoir only), and who drew the water (someone, memoir; Sullivan herself, letter).

**Conflict (grade 8 focus, open to all).** The biographer's question: "Two eyewitnesses tell this differently. How should I write it?" Four choices: pick one and say nothing; pick the earlier source and say why; tell both and name each source; leave the detail out. The student picks one and writes the two sentences. Then a panel shows how biographers often handle it (naming both accounts, and noting the letter was written that day), and the student says in a line whether they'd change their choice.

At 1366x768 two texts fit side by side; at 680x425 texts are tabs.

## Content
- Memoir and letter: exact text from Project Gutenberg eBook #2397 ("The Story of My Life", 1903, which prints Sullivan's letters in its supplement).
- Biography: written for Curio Class from sourced facts (born 1880 in Tuscumbia, Alabama; illness at 19 months; Sullivan arrived March 1887; graduated from Radcliffe College in 1904; a writer and activist for disability rights and other causes; died 1968).
- Key: spans rated per tag type; the timeline row's steps from each text.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tags can be changed or removed; the table updates.
- The tool presents Helen as a full person: her temper, humor, work and opinions, not as an inspiration story.
- With Motion off threads appear without drawing.

## Look
- Accent `--brand` #5c4a7d lilac (header, tags frame, the table rule); gold #f4c542 (the lamp, highlights); paper #f6f4f9; ink #1c1528; muted #58546a. Scene: a quiet reading room.
- Contrast (WCAG 2.1, computed): white on brand 7.69:1; brand on paper 7.04:1; ink on paper 16.19:1; muted on paper 6.65:1; ink on gold 10.88:1.
- Never color alone: tags show their type in words; table columns have headings.
- Different from this batch (editor's red, blueprint blue, web green, lamp amber).

## Art
- Public domain: Library of Congress photographs "Helen Keller and Anne Sullivan" (1897, item 2004672077) and the 1893 seated portrait (item 97513763); the Art step checks each item's rights statement before use.
- Local FLUX (`scripts/localart.py`): reading desk with three documents (1); a water pump under a honeysuckle-covered well-house roof (1); no people.
About 4 images. Drawn in code: tags, threads, table, timeline.

## Voice
Bank voice `knowing-guide` as Mr. Abernathy (unique in this batch); the memoir is read by `gentle-storyteller`, the letter by `big-sister`, and the biography by `clear-teacher` (each unique in this batch). `Curio.voice` with `scope: () => state.grade + ':' + state.text + ':' + state.tag`, `welcomeAfter: true`.
- how `welcome`: "Three people tell one morning. Tag how each one shows Helen, then we'll see where they differ."
- event, whole, `sentence`: the tapped sentence in its text's voice.
- how `tagHow`: "Select a passage, then pick a tag."
- event `keyTag`: "One reading tags this as {an anecdote}."
- event `differ`: "Here they tell it differently: {who drew the water}."
- how `conflictHow`: "How should the biography handle it? Pick a way, then write the two sentences."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: span tagging, three-column table, threads, timeline row, conflict choice. (The evidence family's claims and links are for arguments; here tags describe presentation.)

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag everything "anecdote" | Mismatches with the key are named. |
| Table | Leave rows where they land | Rows in the wrong column show why ("The letter says this too."). |
| Conflict | Pick any way | Each choice is accepted with two sentences; the panel shows what each choice gains or loses. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the memoir: title, `welcome` (queued, first time).
2. Sentences: `sentence` (whole). Tags: `tagHow` (first time), `keyTag` as it fires.
3. Timeline: `differ` per difference.
4. Conflict: `conflictHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.6.3, RI.6.6, RI.6.9, RI.7.3, RI.8.3, RI.8.6 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| The memoir's account (mug and water, the broken doll, the well-house) and Sullivan's letter of April 5, 1887 (mug and milk, she pumped) | Project Gutenberg eBook #2397, chapter 4 and the April 5, 1887 letter (checked 2026-11-09) | Perkins School for the Blind, Helen Keller archive | yes |
| Born 1880 in Tuscumbia, Alabama; illness at 19 months; Sullivan arrived in March 1887; Radcliffe 1904; died 1968 | American Foundation for the Blind, Helen Keller biography | Library of Congress, Helen Keller | yes |
| Photographs of Keller and Sullivan, 1893 and 1897 | Library of Congress, items 97513763 and 2004672077 (checked 2026-11-09) | Perkins School for the Blind, photograph collection | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: disability is presented plainly; Helen is a full person with opinions and a working life; the memoir's other chapters (not used) contain a dated description of a Black child, so only chapter 4 and the letter are used; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b17, 2026-11-09): the memoir passage contains "m-u-g" and "w-a-t-e-r" and the broken doll; the April 5 letter contains "mug" and "milk", "pump-house" and "while I pumped"; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 two texts fit; at 680x425 texts are tabs.
2. Tags work by grade and are compared with the key. (RI.6.3, RI.6.6)
3. The table fills from tags and rows can move. (RI.6.9)
4. Threads link people, events and ideas; comparisons are tagged at grade 8. (RI.7.3, RI.8.3)
5. The timeline row lights three differences. (RI.6.9)
6. The conflict round takes a choice and two sentences and shows the panel. (RI.8.6)
7. Print shows the table and sentences.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: threads appear without drawing; no network requests.

## Open questions
- None for Cory.
