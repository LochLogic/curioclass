# Climbing Reads

## One idea
On a climbing wall of real public-domain texts in six kinds (fiction, poetry, drama, history, science, technical writing), the student climbs from grade-level holds to top-of-band holds, starting each route with supports (read-aloud, a glossary, chunked sections, guiding questions) and clipping them off one by one, with a short check after each section and a range map that shows which kinds they have read and how many supports they still used, so they learn to read harder texts on their own across the whole range.

## Not like
- stretch-shelf (3-5, concept): the elementary band. Here grades 6-8.
- tough-text-club (9-12, concept): high school. Here middle school.
- research-rover (4, spec): gathering facts. Here reading for understanding.
- book-group-table (6, spec): discussing a story. Here reading alone.
- echo-reader (concept): fluency. Here comprehension of complex texts.

## Who and how
- Grades 6-8, ELA, module "Reading Range and Text Complexity" (Reading Literature and Informational Text). Standards: RL.6.10, RL.7.10, RL.8.10, RI.6.10, RI.7.10, RI.8.10.
- Driver: one student (tool.json `driver: "student"`). Read-aloud is a support the student can turn off.
- Grade picker sets the wall: 6, 7 or 8 (each grade's top holds are harder passages of the same works). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "20-40 per route"`, `grades_label: "Grades 6-8"`.
- Saving: the range map is kept in this browser; footer: "Your range map stays on this device." `Clear my map` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.6.10 to RL.8.10 | Climb fiction, poetry and drama routes, answering a check after each section | the route with holds and checks | 2 |
| RI.6.10 to RI.8.10 | Climb history, science and technical routes the same way | the route with holds and checks | 2 |
| RL.x.10, RI.x.10 (independently) | Clip off supports one at a time; the top hold counts only with no supports | the support clips and a "free climb" badge | 3 |
| RL.x.10, RI.x.10 (range) | The range map shows each kind read and the supports used | the range map | 4 |

## Screens and modes
Header (kit): title "Climbing Reads"; `Wall`, `Range map`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** An indoor climbing wall with six colored routes, each labeled with its kind, and Belay, a calm mountain marmot holding the rope at the bottom. First hint: "Tap a route to start climbing." The first tap reads the route's name; the welcome is queued after it (`welcomeAfter: true`).

**A route.** Four holds from bottom to top: grade level, a bit harder, harder, top of the band. Each hold is a passage of 250 to 450 words from the route's work. Supports sit as clips on the climber's harness: Read-aloud (sentences read on tap), Glossary (tap a marked word), Chunks (the passage in short sections with a break line between), Guide questions (one question before each chunk). All four are on at the first hold.

**Check.** After each hold, three questions: one on what the text says, one on a word or line's meaning in context, one on how a part fits the whole. Two of three right moves the climber up. A miss shows the line that answers it and lets the student try a new question from a pool of six.

**Clip off.** Before each hold the student may clip off supports. The top hold's badge is "free climb" only with all four off; with any on, the hold still counts and the map shows the clips used. Clipping one back on mid-passage is allowed and noted.

**Range map.** Six kinds around a circle; each fills by holds reached and shows a support count. A note per kind: "Fiction: top hold, free climb", "Science: hold 3, glossary on".

At 1366x768 the wall and passage fit side by side; at 680x425 the passage slides over the wall.

## Content
Public-domain works (excerpts, each hold a passage; spellings kept; a few long sentences split for grade 6 holds, marked):
- Fiction: Jack London, "White Fang" (1906), part 1, Project Gutenberg #910.
- Poetry: Robert Frost, "The Road Not Taken" and other poems from "Mountain Interval" (1916), Project Gutenberg #29345.
- Drama: William Shakespeare, "A Midsummer Night's Dream", the mechanicals' scenes, Project Gutenberg #1514.
- History: Frederick Douglass, "Narrative of the Life of Frederick Douglass, an American Slave" (1845), chapter 7 (learning to read), Project Gutenberg #23.
- Science: Michael Faraday, "The Chemical History of a Candle" (1861), lecture 1, Project Gutenberg #14474.
- Technical: "Boy Scouts Handbook" (1911), knot-tying and fire-building instructions, Project Gutenberg #29558, with the diagrams redrawn in code.
- Checks: 6 questions per hold (a pool), keyed to lines.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- With Motion off the climber jumps from hold to hold.
- No timer; routes can be left and resumed.
- The Douglass route opens with a short note on what the reader will meet (slavery, cruelty, and Douglass's hunger to read).

## Look
- Accent `--brand` #3d6b2f granite green (header, route ropes, clips); gold #f4c542 (the holds reached, the free climb badge); paper #f4f8f2; ink #13220e; muted #4f5c4a. Scene: an indoor climbing gym with tall windows.
- Contrast (WCAG 2.1, computed): white on brand 6.28:1; brand on paper 5.85:1; ink on paper 15.49:1; muted on paper 6.60:1; ink on gold 10.22:1.
- Never color alone: routes carry their kind in words; clips have icons and words.
- Different from this batch (sky blue, storm violet, pumpkin, museum burgundy).

## Art
Local FLUX (`scripts/localart.py`), no people.
- climbing wall (1); Belay (4 poses: hold rope, cheer, point, think), "A calm friendly marmot climbing coach holding a rope, harness and chalk bag <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- route pictures (6): "<a wolf in a snowy forest / a fork in a woodland path / a stage in a forest at night / an old book and a candle / a lit candle close up / a coil of rope with knots>, realistic illustration, no text, no people"; 4:3.
About 11 images. Drawn in code: holds, clips, map, knot diagrams.

## Voice
Bank voice `knowing-guide` as Belay (unique in this batch); passages are read by `calm-professor` when Read-aloud is on (unique in this batch). `Curio.voice` with `scope: () => state.route + ':' + state.hold`, `welcomeAfter: true`.
- how `welcome`: "Start with every support on. Clip one off when you're ready, and see how high you can climb."
- event, whole, `sentence`: the tapped sentence (Read-aloud on).
- event `check`: the check question.
- event `miss`: "Here's the line that answers it. Try a new one."
- event `up`: "Up you go. Hold {3}."
- how `clipHow`: "Ready to clip one off? Tap a clip."
- event `free`: "Free climb! Top of the {science} route with no supports."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: route and hold state, support clips, check pools, range map. (The read-aloud family is for fluency practice; here read-aloud is one simple support.)

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Checks | Guess | Two of three per hold, drawn from a pool of six; misses show the answering line and a new question. |
| Free climb | Leave supports on | The hold counts, but the badge and map show the clips used. |
| Range | Climb one route | The range map shows the empty kinds. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a route: the name, `welcome` (queued, first time).
2. Passage: `sentence` (whole). Checks: `check`, then `up` or `miss`.
3. Before holds 2 to 4: `clipHow` (first time). Top: `free`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.10 to RL.8.10 and RI.6.10 to RI.8.10 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| Six public-domain works and their Gutenberg numbers (#910, #29345, #1514, #23, #14474, #29558) | Project Gutenberg title headers (checked 2026-11-09) | Library of Congress catalog records for the first editions | yes |
| Text complexity in the standards has three parts: quantitative measures, qualitative features, and the reader and task | CCSS ELA Appendix A | CCSS supplement to Appendix A, new research on text complexity | yes |
Backed twice: 3. Cut: 1 (a Lexile range for each hold; the published ranges are for whole bands and excerpts vary, so holds are ordered by the guide's judgment and checked with a readability score instead of a stated Lexile).

Sensitivity note: the Douglass chapter describes slavery and cruelty; it opens with a note, keeps Douglass's own words, and goes to the fresh-agent review.

Checks run (Python, scratchpad b16, 2026-11-09): six Gutenberg title headers match the named works; "The Road Not Taken" is in #29345; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the wall and passage fit; at 680x425 the passage slides over.
2. All six routes run with checks after each hold. (RL.x.10, RI.x.10)
3. Supports clip off and on; free climb needs none. (RL.x.10, RI.x.10)
4. The range map shows kinds and supports. (RL.x.10, RI.x.10)
5. Misses show the answering line and a new question.
6. The map survives a reload where storage works; `Clear my map` removes it.
7. Print shows the range map.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the climber jumps; no network requests.

## Open questions
- None for Cory.
