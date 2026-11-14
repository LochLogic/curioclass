# Frame read: English Language Arts Grade 6, 2026-11-14

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Brief: docs/pipeline/briefs/frame-read.md, with the
caller's added checks (text picks, the original-text load, the writing split, the 50-minute day, repeated picks
across frames and subjects, every lettered part, the 15 lessons in docs/pipeline/briefs/frame-write.md).

## What I read

- docs/courses/english-language-arts-grade-6/frame.md in full; its row in data/plans/frames.csv (6 units, 160 days).
  No base text, so no source map.
- The 29 grade 6 rows of data/progressions/ela.csv, every column, and the grade 5 and grade 7 rows they take from
  and hand to.
- The neighbour frames: docs/courses/english-language-arts-grade-5/frame.md (seams, its unit 1 and unit 4) and
  docs/courses/english-language-arts-grade-7/frame.md.
- The same-year frames: docs/courses/world-geography-and-ancient-civilizations-i/frame.md (social studies 6),
  docs/courses/science-grade-6/frame.md, docs/courses/math-grade-6/frame.md (units table and checks). Every frame
  searched for the grade 6 picks (Hammurabi, the Rosetta Stone, Hangul, Galveston, the 2011 tsunami, Rossetti,
  Stevenson, floods and storms).
- The bar and lens: docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md, the grade 6 lines of
  data/standards/ccss-ela-standards-full.txt; docs/agents/decisions/DESK-ANSWERS.md, entries of 2026-11-12 and
  2026-11-13 for ELA; the "For the course frames" sections of docs/reviews/progression-cross-2026-11-13.md and
  docs/reviews/progression-cross-codex-2026-11-13.md; docs/reviews/frame-world-geography-and-ancient-civilizations-i-2026-11-13.md
  and docs/reviews/frame-6-8-fixes-2026-11-13.md (for REPEAT tags).
- Gates: `python -X utf8 scripts/plan.py check` (this frame: 0 failures; 6 units, 148 days in units, 12 for checks);
  `python -X utf8 scripts/frame.py check english-language-arts-grade-6` (0 failures); `python -X utf8 scripts/stale.py
  check` (56 files, 0 failures). By hand: unit days run 1 to 32, 33 to 58, check 59 to 62, 63 to 86, 87 to 108, check
  109 to 112, 113 to 136, 137 to 156, check 157 to 160, as the frame's day ranges say.
- Not opened, as told: the earlier grade 6 ELA planning (docs/courses/ela-6/, docs/ela-6-spine.md and its reviews).

## Verdict

The frame is sound in its bones: every grade 6 row sits in one unit, every lettered part of the grade 6 standards is
named where it is taught, the days add up, the units are each a specific topic with named texts, and the science and
math calendars line up better than the frame could know when it was written. The biggest risk is in the texts: the
frame names older public-domain texts (the 1910 Hammurabi translation, Cline's 1900 report) as anchors while saying
no older text is ever an anchor, and almost all of the year's literature would be written by one author, Curio
Class. The one change that matters most is to give unit 2 a question of its own: as drawn, students read the same
code in the same weeks as social studies unit 4 and argue the same question ("was it just, for whom?") twice.

## Findings

### 1. Older texts are named as anchors while the frame says they never are

- **What is wrong.** The Base text bullet says an older public-domain text "appears only as a paired or optional
  read, never the anchor" (BASELINE rule 29, DESK-ANSWERS 2026-11-12, card q-course-texts). The Reading level bullet
  then names "the Hammurabi translation, Cline's 1900 report" among "a few [anchors] at the top with support". The
  units agree with the second sentence, not the first: unit 2's RI.6.6 work is on the code's prologue and epilogue,
  and unit 6's RI.6.9 compare is "Cline's own account and the profile", so Cline's report is one of the two texts the
  standard is taught on.
- **Why it matters.** The scope and sequence writer cannot tell which texts get a text record and count toward the
  55 percent (RUBRIC-ELA 2a counts anchors only), and the rule Cory set is broken without his say. The likely
  reading of the rule (his complaint was about old and far-away stories) leaves room for primary sources, but that
  is his call.
- **Fix.** Under "For the lead" add: "Primary sources as anchors (scope). Rule 29 keeps older texts paired. Units 2
  and 6 teach RI.6.6 and RI.6.9 on two primary sources (the Code of Hammurabi, King's translation, 1910; Cline's
  Galveston report, 1900). Pick: primary historical and scientific documents may anchor in grades 6 to 8 where the
  standard's work is on them, each excerpted short and framed by an original or federal text; literature keeps the
  rule. Cory decides." Until he does, change the Reading level bullet's parenthesis to "(the paired Hammurabi
  translation and Cline's 1900 report, read with full support; the forecasting articles)". The same item is in the
  grade 7 and grade 8 reads; one question to Cory covers the band.
- LAYER frame. REPEAT new. Confidence: firm (the frame's two sentences contradict each other in words).

### 2. Unit 2 asks social studies unit 4's question about the same text in the same weeks

- **What is wrong.** Social studies 6 unit 4 (days 40 to 55) reads the Code of Hammurabi with "eye for an eye"
  applied by class and ends in "a short written claim: was the code just, and for whom?" ELA unit 2 (days 33 to 58)
  reads the same code and asks "Did Hammurabi's laws protect the weak, as his prologue claims?", with a process
  argument on that question. ELA also starts the code a week before social studies opens Mesopotamia, while the
  social studies frame asks that ELA's law-codes work "follow unit 4" and the cross-subject read asked that ELA 6 to
  8 thread texts "follow the order of the social studies and science units they sit beside"
  (progression-cross-2026-11-13) and that shared topics get "distinct disciplinary questions"
  (progression-cross-codex-2026-11-13, item 4).
- **Why it matters.** Students argue the same claim on the same source twice in a fortnight; one of the two
  courses loses its point, and a teacher who teaches both (common in grade 6) sees the overlap at once.
- **Fix.** Give ELA the reading-and-writing lens: compelling question "How did Hammurabi want his people to see
  him, and how did the words on the stone make them believe it?" (RI.6.6 on the prologue and epilogue, RI.6.4 on
  word choice, all answerable from the unit's texts). Process argument prompt: "Should every rule in our town be
  posted where anyone can read it, as Hammurabi's stone was?", argued from the code, the two feature articles and the
  recorded council talk on the park rule (W.6.1b's credible sources are then the unit's own). Keep the short
  on-demand argument on the scribe story. In "Why this unit, here" replace the first sentence with "Thread 1, beside
  social studies grade 6 unit 4 (days 40 to 55): ELA's first articles (Babylon and its scribes) give the background
  in days 33 to 39, the prologue is read for purpose by about day 45, and the question of justice stays with
  social studies' written claim." Change the first Cross-subject row's "Need" text to match.
- LAYER frame. REPEAT yes (the progression cross reads raised distinct questions for shared topics).
  Confidence: firm (both frames say it in words).

### 3. Unit 1 repeats grade 5 unit 1's question and premise

- **What is wrong.** Grade 5 unit 1 is "Starting over: stories of human rights. 'What does a person need to start
  over...?'", on a novel about a girl whose family moves after her father's death. Grade 6 unit 1 asks "What does a
  family, and a town, need to start again after a flood?" on a novella about a twelve-year-old whose family moves
  into a new town, and its process narrative is "a story about a character starting over". Lesson 11 of the frame
  brief: picks chosen so they do not repeat another grade's.
- **Why it matters.** Two years running, the year opens on the same question with the same plot shape (a family
  moves after a loss), in the anchor unit that sets the tone of the year.
- **Fix.** Keep the flood town (it is the right seam with grade 5's water unit). Change the novella's premise: the
  narrator's family has lived in the river town for generations and must decide whether to rebuild on the low
  ground or move uphill; no move to a new town. Question: "What does a river town keep, and what does it change,
  after a flood?" Narrative prompt: "a story in which a character makes a choice the river forces on them". The
  sensitivity note stands.
- LAYER frame. REPEAT yes (lesson 11, picks that repeat another grade's). Confidence: firm.

### 4. One author for nearly all the literature, and the original-text count is off

- **What is wrong.** Every literary anchor of the year is an original Curio Class text: the novella, four stories,
  nine poems and a monologue poem, the one-act play. The only published literature is two paired older poems.
  RUBRIC-ELA 2a scores whether anchors are well made and engaging, and 2e asks who wrote the texts and who is in
  them. A year whose stories, poems and play share one writer reads as one voice, whatever the spec says. The count
  under "For the lead" 3 also does not match the units: about 6 stories (the units name 4: the scribe school, the
  weather log, the Hangul story, the ice storm), 3 editorials and letters (the units name 5: two editorials, two
  letters, a town notice).
- **Why it matters.** This is the course's largest cost and its largest adoption risk at once. Across grades 6 to 8
  the three frames ask for about 75 to 80 original texts, three novellas (about 60,000 to 65,000 words), three plays
  and about 20 poems, each to be read by a qualified ELA teacher. The informational originals (features, editorials,
  advertisements) are cheap and sound; the literary ones carry the risk.
- **Fix.** (a) Correct For the lead 3 to the units' own count: "one novella, 4 stories, 10 poems (8 storm poems, the
  monologue, plus the booklet's none), one one-act play, about 8 articles, booklet chapters and profiles, 2
  editorials, 2 letters and a town notice, an advertisement, a recorded talk and two course recordings: about 31".
  (b) Add to the Base text bullet: "The grade 6 text spec gives each original literary text its own named narrator
  or speaker, voice and setting, and no two anchors in a unit share a voice." (c) Add to "For the lead": "Before the
  poems and the play are written, run the open-licence search the 2026-11-12 decision allows (recent CC BY poems and
  plays fit for grade 6); any fit replaces an original." (d) The question of human writers for the literary
  originals goes to Cory (below).
- LAYER frame. REPEAT new. Confidence: likely (2a and 2e from RUBRIC-ELA as summarised; the one-voice judgment is
  mine).

### 5. The weekly conference does not fit the 50-minute day, and the independent books have no free source

- **What is wrong.** The frame assumes one 50-minute lesson a day and puts independent reading at home ("about 20
  minutes ... on four nights a week"), yet asks "a short conference in class each week" with every student. With no
  independent reading time in class, there is no slot in which a teacher can confer while the class reads; 25
  students at 3 minutes each is about 15 minutes of every lesson. Separately, the independent book is "a long book of
  the student's choice", while the same bullet says "No text is sent home from a library or a paid copy"; the frame
  never says where a free choice book comes from. The seam with grade 5 is also unnamed: grade 5 runs a 90-minute
  block with a 30-minute skills and independent-reading slot; grade 6 drops to 50 minutes.
- **Why it matters.** The scope and sequence will either steal the minutes from reading and writing or drop the
  conferences, and a family with no library nearby has no book.
- **Fix.** Replace the Days bullet's sentence with: "It assumes one ELA lesson of about 50 minutes every school day,
  five a week, for 32 weeks (grade 5's 90-minute block ends here; its skills block's word study moves into the unit
  lessons), about 20 minutes of independent reading on four nights a week, logged, and 15 minutes of in-class
  independent reading twice a week, when the teacher confers with each student about once every two weeks.
  Choice books come from the Curio Class Reading Room shelf, printable, or any book the student already has."
  The 50-minute day itself is sound: it matches a common middle school period, grade 9 uses the same, and the unit
  days hold what the rows ask once the week has a rhythm (the scope and sequence names it).
- LAYER frame. REPEAT new. Confidence: likely (the arithmetic is mine; the 90-minute block is in the grade 5 frame).

### 6. No readiness checks are placed

- **What is wrong.** Lesson 5 of the frame brief: "A readiness check on an earlier grade's skill sits in the first
  unit that needs it." The Seams table says where each grade 5 row is picked up, some of them months into the year
  (e5-narrator-influence and e5-visual-multimedia in unit 5, about day 113; e5-research in unit 3, day 63), but no
  unit names a readiness check. Grade 5's frame and grade 9's frame both state the rule.
- **Why it matters.** The unit writer will not plan the ten minutes, and a skill last used eight months earlier is
  assumed.
- **Fix.** Add under the Seams table: "Each pick-up opens with a short readiness task on the grade 5 skill in the
  unit named in the last column, not all in week 1. Units 2 to 6 name theirs in 'Why this unit, here'." Then add
  "Opens with a readiness task on e5-..." to each unit's "Why this unit, here" for the rows in that seam line.
- LAYER frame. REPEAT yes (lesson 5, social studies frames). Confidence: firm.

### 7. Two standards are not said in full where they finish, and one "first" claim is wrong

- **What is wrong.** (a) W.6.6 is placed in unit 1 ("W.6.6 begins", one typed page); its keyboarding bar, "type a
  minimum of three pages in a single sitting", is first asked in unit 6's one-sitting argument, and unit 6 does not
  say so. (b) Unit 2's reason says "The first informational unit, so the year's word-list row starts where the
  informational anchors start", but unit 1 reads two federal flood explainers with a map and captions (RI.6.1), and
  the Knowledge threads bullet says "Each unit's word list is drawn from its texts".
- **Why it matters.** A standard that finishes in an unnamed unit is the "quietly narrowed" case of lesson 4; and
  RUBRIC-ELA 2k and 2l ask for a word list in every unit, so a unit writer reading "starts in unit 2" may give unit 1
  none.
- **Fix.** (a) In unit 6's "What students learn" after "typed, three pages" add "(W.6.6's three pages in one sitting,
  the year's keyboarding bar, met here)". (b) Replace that sentence of unit 2's reason with "L.6.6 is owned here,
  where the domain words thicken (stele, cuneiform, decree); unit 1 keeps a word list from the novella and the
  explainers as grade 5's e5-academic-words in use."
- LAYER frame. REPEAT yes (lessons 4 and 6). Confidence: firm.

### 8. Narrative writing sits at 25 percent, counted by pieces

- **What is wrong.** The calendar gives argument 3, informative 3 and narrative 2, "about 37, 38 and 25 percent
  against the 35, 35 and 30 the rubric reports" (RUBRIC-ELA 2o, reported in words, not scored). The count weighs a
  one-sitting scene the same as a typed two-page process piece, so by time narrative is lower still.
- **Why it matters.** Small on its own (the figure is not scored), but grades 7 and 8 make the same split, so the
  band ends at 25 percent narrative three years running.
- **Fix.** Add a one-sitting narrative in unit 4: "a scene in which a character learns to write a word in a new
  script, modelled on the Hangul story (W.6.3, used again)". The calendar becomes 3, 3 and 3. State that the shares
  are counted by pieces and that the scope and sequence also reports them by days.
- LAYER frame. REPEAT new. Confidence: likely.

### 9. The same-year calendar can now be checked, and three lines change

- **What is wrong.** The cross-subject table names science and math by base unit only ("Base unit 6.3", "math's
  data unit, late in the year"), as the brief asked when no frame existed. Those frames now exist: science 6 unit 3
  (weather, days 52 to 90) runs beside ELA unit 3 (days 63 to 86); science 6 unit 4 (plate tectonics, days 93 to
  116) and unit 5 (natural hazards, days 117 to 136) both come before ELA unit 6 (days 137 to 156), and science
  unit 5's anchor is the 2011 earthquake and tsunami in Japan, the event ELA unit 6 reads. Math 6 unit 3 (unit rates
  and percentages, days 39 to 58) teaches percent before ELA unit 3, and math unit 8 (data displays) runs about days
  142 to 158.
- **Why it matters.** Unit 6's bridge ("the plate model is not assumed") and unit 3's ban on percent work are not
  needed, and the shared tsunami is a knowledge link worth naming (and content notes should match, Codex cross read
  item 10).
- **Fix.** Science rows: "The other course should teach it by" becomes "Science 6 unit 3, days 52 to 90 (beside)"
  and "Science 6 units 4 and 5, days 93 to 136 (before)"; unit 6's teacher note adds "the 2011 tsunami is science 6
  unit 5's anchor: ELA reads how the warning was made, science the plate model; the content note matches science's".
  Unit 3: replace the percent sentence with "A 'percent chance of rain' is read as a percent (math 6 teaches it by
  about day 58); no task uses a temperature below zero (math 6 unit 7)". Math row: "Math 6 unit 8, about days 142
  to 158; bar graphs, line graphs and tables before then".
- LAYER frame. REPEAT yes (cross-subject calendar lines in the social studies reads). Confidence: firm.

### 10. Stale notes the frame leans on

- **What is wrong.** (a) e6-punctuation-spelling's note says the dash in model sentences "is an open question with
  the lead"; Cory settled it on 2026-11-13 (card q-ela-progression-1: a dash appears only in exercise sentences and
  the texts), and this frame already follows the decision. (b) docs/RUBRIC-ELA.md, the bar this frame cites, still
  answers every part from "docs/courses/ela-6-spine.md, a draft" (its "Where we answer it today" column: 13 pieces,
  150 days, three research projects, units 3, 5 and 6 with no anchor) and calls the first pilot "five days of grade
  6, unit 2"; the frame's own unit 2 is a different topic. (c) The ELA lens names docs/courses/ela-6/RIGHTS.md as the
  rights record; this frame keeps its rights lines in the Units table. Lesson 15: stale wording in shared docs goes
  under "For the lead" with replacement text.
- **Why it matters.** A reader of the rubric page will check this course against a plan it no longer follows.
- **Fix.** Add under "For the lead": "(1) Row e6-punctuation-spelling: replace 'how model sentences show it beside
  the Curio Class house rule against the em dash in its own prose is an open question with the lead' with 'a dash
  appears only in the exercise sentences students punctuate and in the texts they read (Cory, 2026-11-13)'. (2)
  RUBRIC-ELA.md: replace the first sentence under 'What each part asks' with 'The grade 6 answers below are from the
  earlier grade 6 plan (docs/ela-6-spine.md) and are being redone against the course frames
  (docs/courses/english-language-arts-grade-6/frame.md and the grades 7 and 8 frames); the frame reconcile settles
  which holds.' (3) The ELA lens, 'What this lens does not cover': replace 'docs/courses/ela-6/RIGHTS.md' with 'each
  course frame's rights lines (the Units table) and the text records'."
- LAYER process. REPEAT yes (lesson 15). Confidence: firm for (a), likely for (b) and (c) (the reconcile may keep
  parts of the earlier plan).

### 11. Cory's 2026-11-12 grade 6 decision is not mentioned

- **What is wrong.** DESK-ANSWERS 2026-11-12 (card q-course-texts, item 3), inside the dates the brief told the
  writer to read: for the grade 6 pilot, "Keep heroes and their trials; the anchor becomes a new Curio Class hero
  story set today, with one myth retold in our own words as the paired text." This frame has no hero unit and says
  nothing about it.
- **Why it matters.** The frames were written blind on purpose and a reconcile step follows, but a frame that drops
  a Cory decision should say so, so the reconcile and Cory see it at once.
- **Fix.** Add under "For the lead": "Heroes (Cory, 2026-11-12, for the grade 6 pilot): this frame has no hero unit;
  the frame reconcile decides whether the hero set returns (it would fit beside unit 5's literary work or replace
  unit 4) or the pilot moves to a unit of this frame. Cory's call if it changes a unit."
- LAYER process. REPEAT new. Confidence: firm.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 2's compelling question and process prompt as in finding 2 | Keeps the code shared with social studies but gives ELA its own lens (purpose and word choice) | docs/courses/english-language-arts-grade-6/frame.md, unit 2 |
| Unit 1's novella premise, question and narrative prompt as in finding 3 | Ends the repeat of grade 5 unit 1 while keeping the flood-town seam | grade 6 frame, unit 1 |
| A one-sitting narrative scene in unit 4 | Brings narrative to 3 of 9 pieces | grade 6 frame, unit 4 and Writing calendar |
| Percent may be used in unit 3 | Math 6 unit 3 teaches it by about day 58 | grade 6 frame, unit 3 teacher notes |
| Rossetti's "Who Has Seen the Wind?" stays in grade 6; grade 4's Rossetti picks (unnamed in its frame) exclude it | Avoids a repeat the grade 4 scope and sequence could make | grade 6 frame (no change); docs/courses/english-language-arts-grade-4/frame.md, unit naming the Rossetti poems |
| Choice books from the Curio Class Reading Room shelf | The free source the frame lacks; Cory made it the independent-reading shelf on 2026-11-12 | grade 6 frame, Days bullet |

## For Cory

- **Primary sources as anchors** in grades 6 to 8 (finding 1): may the Code of Hammurabi and Cline's report (and
  grade 7 and 8's founding-era and 1906 documents) anchor where a standard's work is on them? Pick: yes for
  historical and scientific documents, no change for literature.
- **Who writes the literary originals** (finding 4): about 75 to 80 original texts across grades 6 to 8, including
  three novellas, three plays and about 20 poems, each read by a qualified ELA teacher; and whether some literary
  pieces should come from paid human writers. Money and people.
- **The assumed time** (For the lead 1): 50 minutes a day plus home reading on four nights. Audience.
- **Readers:** the Korean language and culture reader for unit 4's Hangul story (already listed). People.

## For the lead items, judged

- **1 (minutes):** sound; add in-class reading time (finding 5).
- **2 (the "Texts" column):** sound.
- **3 (about 30 originals):** count corrected (finding 4); the load is sound for informational texts, a risk for the
  literary ones.
- **Picks:** sound, with the unit 1 and unit 2 changes (findings 2 and 3).

## Lens checklist

- Every lettered part in full: met, with W.6.6 named where it finishes (finding 7).
- Text picks public domain or licensable: met.
- Reading level and range: met.
- Informational share near 55 percent: met if the primary sources count (finding 1).
- Writing split: narrative low (finding 8).
- Picks not repeated: missed (findings 2 and 3).
- Same-year alignment: unit 2 ahead of social studies (finding 2); science and math lines to update (finding 9).
- Readiness checks: missed (finding 6).
- Sensitivity reads: met.
- Paper path: met.

## What is right and should not be touched

- Every unit is a specific topic with named texts; the threads (law codes and writing systems; floods, weather and
  warnings) are real topic sets that reach history and science, and they sit beside the social studies and science
  units by day.
- The writing ladder: tracing arguments before writing one, research before social studies unit 8, the process
  pieces kept out of social studies' research weeks.
- The fluency line (a one-minute check, a cut named as untested, no rate shown to students) and the paper path that
  says plainly where W.6.6 is not met.
- The sensitivity notes (no student asked to tell a disaster; the code's punishments without role play; L.6.1e
  taught as choosing a form for the setting).
- Days by load: unit 1 (32 days, ten rows, the long text and the first process piece) down to unit 6 (20 days, two
  rows and two one-sitting pieces) weigh about right.

## What I could not judge

- The quality of texts that do not exist yet; only the text spec and the teacher read can settle 2a and 2b.
- Each federal page's images (the frame already says they are checked one by one).
- Whether the Reading Room shelf has enough grade 6 choice books in the 925 to 1185 band.

## Sources

- data/standards/ccss-ela-standards-full.txt: every grade 6 code and lettered part checked against the units.
- docs/RUBRIC-ELA.md: 2a, 2e, 2k, 2l, 2o as summarised there (the EdReports files themselves not re-read).
- Science 6, social studies 6, math 6 and grade 5 ELA frames: the day calendar and the repeats.
- From memory, not re-fetched: Hasbrouck and Tindal (2017) grade 6 fall 25th percentile near 112 words correct a
  minute (the frame's figure agrees with my recollection); Cline's report in Monthly Weather Review, September 1900.
