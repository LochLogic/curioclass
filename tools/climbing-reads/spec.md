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
- Driver: one student (tool.json `driver: "student"`). Role: practice (a station the student returns to over the year), with hold 1 of each route as the model.
- Three grade paths. Each grade has its own wall: six routes of four holds, 24 passages that no other grade uses, and that grade's wording on the goal card. No path needs another.
  - Grades 6 and 7 (RL.6.10, RI.6.10, RL.7.10, RI.7.10): read and comprehend literature and literary nonfiction in the grades 6 to 8 band proficiently, with scaffolding as needed at the high end of the range. So holds 2 and 3 must be read with no supports, and supports may stay on at the top hold.
  - Grade 8 (RL.8.10, RI.8.10): read and comprehend at the high end of the band independently and proficiently. So holds 3 and 4 count only with no supports.
- Change note (spec fix, 2026-11-11): the wall, Belay, the four supports and the range map stay. Before, every hold counted with all four supports on, so a student could finish a wall and never read alone; the map and the screens also disagreed about the top hold. Now each grade has holds that count only when read free, as its standard words it. A check answer is the answer and the line that proves it together. The technical route is replaced by a memoir route, because the standard names literary nonfiction. Each wall ends with free reads on your own. Added the three hooks.
- English learners: every instruction and every question is spoken and on screen in short sentences. The words route, hold, support, clip off and free each show with a picture on the wall the first time they are used. Instructions use no idioms. For a student who needs passages read aloud as an access need, the teacher can set `Read-aloud always`; the map then says "read aloud by setting" and the hold still counts as free.
- tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "20-40 per route"`, `grades_label: "Grades 6-8"`. Nothing is timed.
- Saving: the range map is kept in this browser; footer: "Your range map stays on this device." `Clear my map` removes it.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RL.6.10, RL.7.10 | read and comprehend stories, dramas and poems in the 6 to 8 band proficiently, with scaffolding as needed at the high end | the student | Climb the fiction, poetry and drama routes: read each hold's passage and answer three checks, each with its proving line; holds 2 and 3 free, supports as needed at hold 4 | 12 holds, plus 2 free reads | the route, the support clips, the checks | 2, 3 |
| RI.6.10, RI.7.10 | read and comprehend literary nonfiction in the 6 to 8 band proficiently, with scaffolding as needed at the high end | the student | The same on the history, science and memoir routes | 12 holds, plus 2 free reads | the route, the support clips, the checks | 2, 3 |
| RL.8.10 | read and comprehend stories, dramas and poems at the high end of the band independently and proficiently | the student | Climb the three literature routes; holds 3 and 4 count only free | 12 holds, plus 2 free reads | the route and the "free" mark on each hold | 2, 3 |
| RI.8.10 | read and comprehend literary nonfiction at the high end of the band independently and proficiently | the student | Climb the three nonfiction routes; holds 3 and 4 count only free | 12 holds, plus 2 free reads | the route and the "free" mark on each hold | 2, 3 |
| all (range) | read across kinds of text | the student | Climb more than one kind; the range map shows each kind read and how | 6 kinds a wall | the range map | 4 |

## Screens and modes
Header (kit): title "Climbing Reads"; `Wall`, `Range map`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card gives the grade's two standards in their own words.

**On load and first tap.** An indoor climbing wall with six routes, each with its own color, pattern and name label, and Belay, a calm mountain marmot holding the rope at the bottom. First hint: "Tap a route to start climbing." The first tap reads the route's name; the welcome is queued after it (`welcomeAfter: true`).

**A route.** Four holds from bottom to top: grade level, a bit harder, harder, top of the band. Each hold is a passage of 250 to 450 words, or a whole short work where the route allows it (every poetry hold is a whole poem; the top fiction hold is a whole short tale). Supports sit as clips on the climber's harness: Read-aloud (sentences read on tap), Glossary (tap a marked word), Chunks (the passage in short sections with a break line between), Guide questions (one question before each chunk).

**Hold 1 (the model).** All four supports are on and Belay shows each one working on the first lines: taps a word for the glossary, reads a guide question and says what she will look for, and answers the first check aloud with her finger on the proving line. The student finishes the hold. Hold 1 never counts as free.

**Free holds.** In grades 6 and 7, holds 2 and 3 open with every clip off and the clips locked; at hold 4 the student may clip supports on as needed, and the map records which. In grade 8, hold 2 lets the student choose, and holds 3 and 4 open with every clip off. A student who is stuck on a free hold may tap `I need a support`: the clips unlock, the hold is finished as "practice, with support", it does not count, and a twin passage at the same level is added to the route to be read free. A route is done only when its free holds are done free.

**Check.** After each hold, three questions, one at a time, with the passage still in view: one on what the text says, one on a word or line's meaning in context, one on how a part fits the whole. Each is a choice of four with the wrong three written from likely misreadings, and the student must also tap the sentence or line that proves the answer; choice and line are judged as one answer. All three right moves the climber up. A miss says only "Not yet. Read that part again." and draws a new question of the same kind from the hold's pool of six; a second miss on the same kind shows the proving line, logs the hold as "shown", and adds the twin passage.

**Free reads (on your own).** When the three literature routes are climbed, two free reads open: new passages at the grade's free level, one from two different kinds, with no clips, no Belay, three questions each with a proving line, one answer a question, and nothing marked until both reads are in. The same happens for the three nonfiction routes.

**Range map and results.** Six kinds around a circle; each fills by holds reached and says in words how each was read: "Fiction: hold 4, free", "Science: hold 3, practice with glossary". Under it, a results strip for the teacher by code (the grade's RL code and RI code): free reads right out of six questions, with each wrong choice shown beside the question; free holds done out of the grade's count; holds logged "shown" or "practice, with support" and which clips were used.

At 1366x768 the wall and passage fit side by side; at 680x425 the passage slides over the wall.

## Content
Public-domain works (spellings kept; a few long sentences split for grade 6 holds, marked). Each grade draws its own 24 passages from these, a different chapter, scene or poem for each grade, plus a twin for every free hold and four free reads:
- Fiction: Jack London, "White Fang" (1906), Project Gutenberg #910. Top hold in each grade: one whole Aesop or Grimm tale chosen at Build for length and level.
- Poetry: Robert Frost, poems from "Mountain Interval" (1916), Project Gutenberg #29345, each hold a whole poem.
- Drama: William Shakespeare, "A Midsummer Night's Dream", the mechanicals' scenes, Project Gutenberg #1514.
- History: Frederick Douglass, "Narrative of the Life of Frederick Douglass, an American Slave" (1845), chapters 6 and 7 (learning to read), Project Gutenberg #23.
- Science: Michael Faraday, "The Chemical History of a Candle" (1861), lectures 1 and 2, Project Gutenberg #14474.
- Memoir: Helen Keller, "The Story of My Life" (1903), chapters 4 to 7, Project Gutenberg #2397. This replaces the Boy Scouts Handbook route: knot and fire instructions are not literary nonfiction, which is what the standard names.
- Checks: 6 questions a hold (two of each kind), each keyed to an answer, three wrong choices with the misreading each one stands for, and the proving line.
- What a wrong answer on a free read means. "What the text says" wrong with a line from the right paragraph: the student found the place and misread it. Wrong with a line from elsewhere: the student is answering from memory of the topic and not from the page. "Meaning in context" wrong with the word's everyday meaning chosen: the student is not using the sentences around the word. "How a part fits" wrong while the other two are right: the student reads sentence by sentence and is not yet holding the whole passage.
- Sensitivity read, left for the final review: the Douglass chapters (slavery, cruelty, the words of the time), "White Fang" (hunger, animals killed), the Keller chapters (how blindness and deafness are spoken of in 1903). The Douglass route keeps its opening note. The reviewer picks the exact passages with this in mind.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- With Motion off the climber jumps from hold to hold.
- No timer; routes can be left and resumed.
- The Douglass route opens with a short note on what the reader will meet (slavery, cruelty, and Douglass's hunger to read).
- Access: every action works by tap and by keyboard; a route, a hold, a clip, a choice and a proving line are each reached with Tab or arrow keys and chosen with Enter. Routes are told apart by name and pattern, never color alone; "free", "practice" and "shown" are words. Motion can be paused. Read-aloud of instructions and questions is always there; only the reading of the passage is a support.
- Free reads: one answer a question, no feedback until both reads are in.

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
- how `freeHold`: "This hold is a free read. No clips. Read it, then answer."
- how `proveIt`: "Choose your answer. Then tap the line that proves it."
- how `need`: "Stuck? Tap I need a support. You'll get a new passage to read free after."
- how `own`: "Two free reads, on your own. Answer each question once."
- event, whole, Belay's model on hold 1.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None. Tool-only code: route and hold state, support clips, check pools, range map. (The read-aloud family is for fluency practice; here read-aloud is one simple support.)

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Checks | Guess from four | The choice and its proving line are one answer, all three kinds must be right, a miss draws a new question, and a second miss logs the hold as shown and adds a twin. |
| Free holds | Leave supports on | The clips are locked off on the grade's free holds; asking for a support makes the hold practice and adds a twin to read free. |
| Top of the band (grade 8) | Finish with supports | Holds 3 and 4 count only free, and the route is not done until they are. |
| Range | Climb one route | The range map shows the empty kinds, and the free reads open only after three routes. |
| Free reads | Lean on turn-backs | One answer a question and nothing marked until both are in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a route: the name, `welcome` (queued, first time), then Belay's model on hold 1 (whole), waits.
2. Passage: `sentence` (whole, Read-aloud on). Free hold: `freeHold` (first time), `need` after a first miss.
3. Checks: `check`, `proveIt` (first time), then `up` or `miss`.
4. Grades 6 and 7 before hold 4, grade 8 before hold 2: `clipHow`. Top: `free`.
5. Free reads: `own`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.10 to RL.8.10 and RI.6.10 to RI.8.10 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| Six public-domain works and their Gutenberg numbers (#910, #29345, #1514, #23, #14474, #29558) | Project Gutenberg title headers (checked 2026-11-09) | Library of Congress catalog records for the first editions | yes |
| Text complexity in the standards has three parts: quantitative measures, qualitative features, and the reader and task | CCSS ELA Appendix A | CCSS supplement to Appendix A, new research on text complexity | yes |
Backed twice: 3. Cut: 1 (a Lexile range for each hold; the published ranges are for whole bands and excerpts vary, so holds are ordered by the guide's judgment and checked with a readability score instead of a stated Lexile).

Sensitivity note: the Douglass chapter describes slavery and cruelty; it opens with a note, keeps Douglass's own words, and goes to the fresh-agent review.

Checks run (Python, scratchpad b16, 2026-11-09): six Gutenberg title headers match the named works; "The Road Not Taken" is in #29345; contrast as in Look.
Spec fix notes (2026-11-11): the Keller eBook number and chapter range were written from memory and not opened in this pass; Build must confirm them. The split of free holds by grade follows the wording of the two standards (scaffolding as needed at the high end in grades 6 and 7; independently at the high end in grade 8).

## Done when
1. Focus and fold: at 1366x768 the wall and passage fit; at 680x425 the passage slides over.
2. Each grade has its own wall of six routes and 24 passages with its own goal card. Each check takes a choice and its proving line as one answer, and all three kinds must be right to move up. (RL.6.10 to RL.8.10, RI.6.10 to RI.8.10)
3. Free holds: in grades 6 and 7, holds 2 and 3 run with clips locked off; in grade 8, holds 3 and 4 do. Asking for a support makes the hold practice and adds a twin passage; a route is done only when its free holds are done free.
4. The range map shows each kind and, in words, how each hold was read.
5. Hold 1 of each route opens with Belay's model. A second miss on one kind shows the line, logs the hold as shown and adds a twin.
6. Two literature and two nonfiction free reads run with no clips, one answer a question and no marks until both are in; the results strip shows them under the grade's two codes.
7. The map survives a reload where storage works; `Clear my map` removes it. Print shows the range map and results.
8. Every spoken instruction and question is also on screen; each key word shows with a picture at first use.
9. Every action works by keyboard as well as tap, routes and marks are named in words and never by color alone, nothing is timed, and motion can be paused.
10. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
11. Motion off: the climber jumps; no network requests.

## Open questions
- For Cory: the technical route (Boy Scouts Handbook) is swapped for a memoir route (Helen Keller), because RI.6.10 to RI.8.10 name literary nonfiction. Default used: swap. Say if the handbook should stay as a seventh route that does not count toward the standard.
- For Cory: each grade now has its own 24 passages (72 in all, with twins and free reads on top). Default used: specified in full. If that is too much to source, the cut is to share hold 1 passages across grades.
