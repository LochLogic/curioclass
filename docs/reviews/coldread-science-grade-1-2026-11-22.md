# Cold read: Science, Grade 1 (science-grade-1), course finish

Read on 2026-11-22 by a cold reader who wrote none of the course, against docs/RUBRIC-SCIENCE.md and the pass rule in docs/ADOPTION-BAR-SUBJECTS.md. Course finish, docs/COURSE-RUN.md stage 7. Read-only: nothing but this report was edited. A dated record; it is not rewritten.

## Verdict

**It would not pass yet.** Four things stop it:

1. **Every sampled unit rates 7 on EQuIP** (units 2, 4 and 7). Pass rule point 3 needs 8 or 9 for every sampled unit.
2. **S5 is a door and does not pass.** Day-level safety is good: every hands-on day lists materials and has Safety and set-up, and every hazard has a control. But there is no course safety page and no safety-agent read on file. These are known gaps (below), and they also hold 3h below full marks, so Gateway 3 cannot meet.
3. **Three part passes, S2, S3 and S6.** The rule allows two.
4. **Gateway 1 is estimated at 27 of 34**, partly meets, below the 29 line. Most of the lost points come from one design pattern. The evidence children reason from is often invented or not yet made: shoot strips, dog frames, the unit 3 parent-young masters, the unit 4 recordings and the unit 7 drawn media. Students rarely meet the phenomenon first hand.

The worst single finding is unit 4's end-of-unit assessment. Half its points are scored from held-back record cards whose spec gives them no observable result.

The course is close in shape:
- The storylines drive.
- Models are revised and then used in the end tasks.
- Scoring guidance, samples at two levels and the error registers are strong.
- Engineering is taught as design.
- Accuracy held up in every fact checked.

The fixes are mostly local. The exception is the evidence-provenance pattern, which runs across units 2, 3, 4 and 7.

## Sample read

- **Read whole:**
  - the scope and sequence and its coverage table (docs/courses/science-grade-1/scope-and-sequence.md);
  - unit 2 (first third): s02.md, u02-1.md, u02-2.md and days 10 to 21;
  - unit 4 (middle third): s04.md, u04-1.md, u04-2.md and days 28 to 34;
  - unit 7 (last third): s07.md, u07-1.md and days 56 to 61.
- **Also read:**
  - the moves of the course checks on days 35 to 37 (they sit in courses/science-grade-1/u04-2/);
  - the held-back card files the sampled days lean on;
  - sources.csv rows for units 2 and 7;
  - items.csv and parts.csv, filtered.
- **Gate run:** the filtered `plan.py check`. It printed 13 FAIL lines for science-grade-1, all of one kind: "section N.N (science-grade-1-uNN-N) is not in data/units.csv", for all 13 sections, 1.1 to 8.1. Sequence and frame checks show 0 failures. The rest are notes: error rows from memory, prose length, the unit 8 early start, and 51 "shows names no end-of-unit item" notes.

## Scores

### Gateway estimates (K-5 criteria, estimated by the reader)

| Gateway | Estimate | Line | Reading |
|---|---|---|---|
| 1 (1a to 1k) | 27 of 34 | meets at 29 | Partly meets. 1a 3/4, 1b 2/2, 1c 1/2 (first-hand evidence weak, see findings 2 to 4), 1d 2/2, 1e 4/6, 1f 2/2, 1g 3/4 (day goals do not state elements), 1h 2/2, 1i 3/4, 1j 3/4 (unit 4 item 2 validity), 1k 2/2 |
| 2 (2a to 2h) | 29 of 34 | meets at 29 | Meets, borderline. 2a physical, life, earth and space, engineering 8/8; 2b 6/8 and 2c 6/8 (elements named in unit plans but not traced to items, finding 6); 2d 2/2 (no science error found in the sample); 2e 2/2; 2f 1/2 (nature of science placed on named days, done only in part); 2g 2/2; 2h 2/2 |
| 3 (3a to 3q) | 12 of 18 | meets at 16 | Partly meets. 3a 2, 3b 2, 3c 2, 3e 0 (no approach page), 3f 0 (no course supplies list), 3g 3 of 4, 3h 0 (no course safety page or safety read; day-level safety is good), 3j 2, 3k 1 (one-line extensions only). 3d (family): unit family notes exist in English and Spanish. 3i (time): fits, with a cut path and a 58-meeting fold table |

**Not judged here.** 1e and 2a to 2c in full across all eight units (only three units were read whole); 3l to 3u beyond a line; the EdReports K-5 evidence guide and the multilingual learner criteria (not on file in the repository); anything about classroom use (nothing is taught yet).

### EQuIP, per sampled unit

| Unit | I. 3D design | II. Supports | III. Monitoring | Sum | Rating |
|---|---|---|---|---|---|
| 2, Parts that help | 2 | 2 | 3 | 7 | A model if improved |
| 4, Sound | 3 | 2 | 2 | 7 | A model if improved |
| 7, Parents and young | 2 | 2 | 3 | 7 | A model if improved |

- **Unit 2.**
  - Category I: the tower problem drives a real design cycle (define, sketch, partner reading, build, fan test, one change, retest, transfer). But days 10 and 13 teach part jobs by read-aloud before any evidence.
  - Category II: plant and animal response evidence is invented (strip A and strip B, the dog frames). No real shoot is ever grown in the unit.
  - Category III: strong, with ten scored components, samples at two levels, letter repairs and revision before scoring. It depends on photographs that are not on file (finding 2).
- **Unit 4.**
  - Category I: a genuine investigation storyline in both causal directions. Cause and effect is used, and the stopping test does real work.
  - Category II: the exits ask for competing-cause comparisons that rest on eight adult recordings, none on file.
  - Category III: item 2 for half of each class is scored from static cards with no observable result (finding 1).
- **Unit 7.**
  - Category I: the patterns crosscutting concept is used with the obtaining-information practice. But "comparing sources" mostly compares Curio Class words with Curio Class drawings made from the same account.
  - Category II: careful sensitivity limits.
  - Category III: strong. Ten components, samples, error letters D and E for the plant case, and a fresh case on day 61.

### Rows S1 to S13

| Row | Mark | Evidence |
|---|---|---|
| S1 storyline | Pass | Anchors drive each unit (s02.md:13-14, s04.md:13-14, s07.md compelling question). Question boards hand each day's question on (s02.md:49, s04.md:44, s07.md field 2). Unit 3's schoolyard question is honestly left unresolved (s03.md:12) |
| S2 3D in lessons | Part pass | Unit 4 days are investigation-first (d031 stopping test). In unit 2, part jobs are told before evidence: d010.md:39-41 and d013.md:33-35 |
| S3 3D in assessment | Part pass | End-of-unit points all need a practice with an idea on a new case (s02.md:112, s04.md:96, s07.md field 5). But exits E11a, E11b and E12a (u02-1.md:51-54) ask only to touch a named part. items.csv names no practice element for any of 240 items |
| S4 models revised | Pass | Unit 2 chart and class model revised days 11, 14, 17, 18 and 19, used on days 20 to 21. Unit 4 two-arrow model revised days 31 and 32, used on day 33. Unit 7 model revised days 57 to 59, used on day 60 |
| S5 safety (door) | Fail, known gap | Day level passes: materials in every day's front matter, plus Safety and set-up (for example d018 glasses, seated cutting and counted scissors; d032 sealed rice and adult-only speaker). The course safety page and the safety read are missing (Known gaps) |
| S6 low cost | Part pass | Costs stated per unit ($10, $8, $1; s02.md:216, s04.md:178), and stand-ins named. Unit 4's no-kit path rests on recordings that are not made, and its spec (static line drawings) cannot carry the observation (finding 1) |
| S7 right source | Pass | K-5 is Curio Class's own; OpenSciEd elementary is read for reference only (s02.md:234, s04.md:197); no copied text found in the sample |
| S8 credits | Pass | Days say "Ours"; day 10 and day 56 credit the federal photographs only (d010 Credit, d056 Credit) |
| S9 checks to act on | Pass | An exit closes each section (E15, E21, E31, E34, E61). End-of-unit assessments have scoring, two-level samples, error meanings and response groups (s02.md:112-116, s04.md:96-100, s07.md fields 5 to 7) |
| S10 accurate, in band (door) | Pass | Sampled facts hold, for example the alligator snout and bat call-and-smell facts (sources.csv 12E, 12X), and no wave model, organs or mechanisms. One provenance mislabel on day 36 (finding 10) is a labelling fix, not a science error |
| S11 every standard | Pass | All ten owned codes have lesson sets and check items (trace below). The trace is by code and part; elements are not traced at item level (finding 6) |
| S12 math and ELA | Pass | Direct ordering instead of units (scope:62), the no-gaps strip bridge before math unit 6 (scope:90), and W.1.8, RI.1.2 and SL.1.5 bridges by drawing and dictation (s02.md:63, s04.md:59) |
| S13 engineering as design | Pass | Unit 2 days 16 to 21 (define, sketch, build, fan test, one change, retest, transfer); unit 6 per the scope (scope:88-92) |

### Ten standards traced (all ten owned codes)

| Code | Lesson set (days) | Check items |
|---|---|---|
| 1-ESS1-1 | 1 to 6 | s01-E1 to E3 (day 7); c1-S35a to c (day 35) |
| 1-LS1-1 | 10 to 19 | s02-E20a, E21a (days 20 to 21); c1-P35a, P35b, A35a, A35b, C35a (day 35) |
| K-2-ETS1-2 | 16 to 19 | s02-E20b, E21b; c1-C35b to d |
| 1-LS3-1 | 22 to 25 | s03-E26a to l (day 26); c1-L36a, L36b (day 36) |
| 1-PS4-1 | 28 to 32 | s04-E33a, E33b (day 33); c1-V36a to c (day 36) |
| 1-PS4-2 | 38 to 42 | s05-E46a (day 46); c2-V66a, V66b (day 66) |
| 1-PS4-3 | 43 to 45 | s05-E46b; c2-P66a, P66b, T66a to c |
| 1-PS4-4 | 48 to 53 | s06-E54a, E54b (day 54); c2-M67a to d (day 67) |
| 1-LS1-2 | 56 to 59 | s07-E60a to c (day 60); c2-A67a to c (day 67) |
| 1-ESS1-2 | 9, 62 to 63 | s08-E64a (day 64); c2-S67a, S67b (day 67) |

Every code reaches a lesson set and at least two check items, matching scope-and-sequence.md:118-129.

### Coherence across units

The teaching order is 1, 8 (day 9), 2, 3, 4, 5, 6, 7, 8.

**What holds:**
- Models carry forward on purpose. Unit 1's pattern chart opens unit 2 (d010 Warm-up). Unit 2's evidence arrow "I saw ___, so ___" returns in unit 4 (u04-1.md field 5, d031 Rug). Unit 2's ear cone returns on day 36. Unit 6's signal word returns in unit 7 (d059 Robin cards).
- The seams name what is handed on: d028 Before class, and d056 retrieval of units 2 and 3.

**The weak seam is plants, units 2, 3 and 7:**
- Day 12 still has the teacher press parent-tree and seedling leaves with provenance labels for unit 3.
- Unit 3 instead uses invented M22 masters (s03.md:88).
- Unit 7 retrieves that invented diagram and records that "the required documented plant record remains missing" (s07.md:157).

So the scope's promise of a verified parent-and-young plant record (scope-and-sequence.md:52, 66) is not kept, and the day 12 task now prepares something no later day uses as evidence.

## Findings, most serious first

| Where | Rubric row | What is wrong | The exact fix | Stage that made it |
|---|---|---|---|---|
| courses/science-grade-1/u04-2/cards-day33.md:10 and the Item 1 and Item 2 records sections; d033.md "18 min. Six group turns" (waiting-children paragraph); s04.md:92 | EQuIP III, S3, 1j, S6 | Half of each class (three groups per item) earns item 2's six points, or item 1's, from "records" specified as plain black line drawings with "no result written on any card". A static drawing cannot show a ribbon moving with sound on, or a ruler sounding when free. The scored panel therefore rests on nothing observable. The same dependency runs through every exit on days 28 to 32 and 34: spoon, comb, tray, bell, foil, fringe, fan and cup "recordings to be made", none on file (s04.md:104, 199) | Make each held-back record a dated frame strip from an adult video: at least four frames per trial, the strip's or ruler's position drawn from the video in each frame, and a sound-on or sound-off icon per frame. Record these before day 28, and keep the videos. Until they exist, run both items live for every group: item 2 as one class demonstration on day 33 (the teacher runs shared-table, separate-support, sound-off and sound-on trials on children's requests; every child marks their own panel), and item 1 in the group turns. Score only live-observed panels | Unit plan (assessment design), then day and data (cards) |
| courses/science-grade-1/u02-2/sheets-day20.md:19; s02.md:108; sources.csv 4E ("not yet on file"); d010.md:15-17 (Before class) | 1c, S1, EQuIP II, S9 | Day 20's plant evidence must be "real dated photographs of a different class shoot, collected before day 10, never altered", with no fallback. No day page tells the teacher to start that shoot, so a teacher following the days reaches day 20 without it. Days 11 and 12 use invented strips A and B, so the class never sees a real plant respond | Add to d008.md (unit 1's last day) or d010.md Before class: "Plant two bean seeds in clear cups now. Keep cup 1 by the window for days 11 and 12. Keep cup 2 out of sight beside a lamp on one side; photograph it daily at the same time, move the lamp to the other side on day 4, and keep photographing. Seal cup 2's photographs for day 20." Use cup 1's real photographs on days 11 and 12, with strips A and B as the stated fallback. Give day 20 a named fallback: a credited public-domain shoot sequence, said aloud to be another class's record | Day (unit 1 and unit 2 days); section plan field 5 |
| scope-and-sequence.md:52, 60, 66; d012.md Safety and set-up (pressing task); s03.md:12, 88; s07.md:57, 157 | Coherence, 1c, S1 | The plant parent-young seam is broken. The scope promises verified parent-tree or seed-grown-young photographs. Day 12 presses provenance-labelled leaves for unit 3. Unit 3 uses invented masters instead, and unit 7 retrieves the invented diagram, so no unit uses the pressed leaves as evidence | Pick one route and make all three layers agree. (a) Keep real evidence: unit 2 day 11 plants a dated seed from a class parent bean, unit 3 day 22 compares that seedling with its parent, and unit 7 day 56 retrieves that record. (b) Keep the masters: cut day 12's pressing task, and change scope:52, 60 and 66 to say unit 3 uses labelled invented models with parentage given by caption | Scope, then unit plans 2, 3 and 7 |
| s02.md:118-133 (exit table) against u02-1.md:49-61 and the days; s04.md:104-115 against u04-1.md field 3 and d028 to d034 exits; u04-2.md field 3 (E34a, E34b) against d034.md "7 min. Exit: fresh evidence" (X34a to c: fringe, fan and cup records) | EQuIP III (aligned guidance), S9 | Each unit plan's exit table describes different cases from the ones the days use. Unit 2: sunflower, beetle wing cover and lighthouse roots in the plan; bean and tube, winged seed and others in the days. Unit 4: spoon and comb trials, fringe with a hand near, in the plan; spring doorstop, fan record and cup record in the days. The goal-map rows drift too. A teacher or reviewer reading the unit plan gets the wrong key | Replace each unit plan's exit table with the day and item id actually used (from items.csv, for example s02-X10a), or a pointer to the section plan's exit list. Make u04-2.md's E34 list match d034's three asks | Unit plan |
| data/plans/science-grade-1/items.csv (practice column, all 240 rows empty) | S3, S11, 1i, 2b, 2c | No item names the practice or crosscutting element it draws on, so element coverage cannot be traced from data to check items. The element lines live only in unit-plan prose | Fill `practice` on every end and exit row from data/standards/ngss-pe-dimensions.csv (for example s04-E33b: planning and carrying out investigations; cause and effect). Use a short script that reads the whole file and writes a temp file | Data |
| courses/science-grade-1/u02-1/d010.md:39-41; d013.md:33-35 | S2, EQuIP I | Part jobs (roots hold and take in water; ears sense, legs move) are told in a read-aloud before children gather any evidence; trays and sorting follow. This is the "teach by telling, practice after" condition | Day 10: after the hook, children look at the photograph and a lifted potted plant, guess each part's job, and the chart records guesses. Move the read-aloud to day 11 after the trays, as a check of their evidence. Day 13: open on the hare picture sequence, sort observed actions first, then read the pages to confirm | Section plan 2.1, then day |
| docs/courses/science-grade-1/u02-1.md:51-54 (E11a, E11b, E12a); d011.md and d012.md exits | S3 | These exits ask only "touch the part that takes in water" or "faces the light" on a new picture: a term, not a practice | Re-pose each as evidence. E11a: two dated pictures of the same plant with soil dry, then watered, and "Which part's job do these pictures show? Say what you saw." E12a: a leaf turned away from a window, then later facing it, and "What did the leaf do, and what does that show?" | Section plan 2.1 |
| docs/courses/science-grade-1/u07-1.md field 5 (key moment 1); s07.md field 10 (Media); d058.md "8 min. Groups compare the deer" | 1-LS1-2 practice, EQuIP I and II, 1c | Only the robin photograph is a real medium. Deer, duck and robin sequences are Curio Class drawings made from the same accounts as the words, so "compare the words with the picture" is not a comparison of two sources | Confirm the fawn photograph's rights now (sources.csv 12C; the park's rights notice) and use it on day 58. Add one credited public-domain photograph of a hen with ducklings beside day 60's words. Keep drawings only where no photograph has clear rights, and say so aloud | Unit plan, data (sources) |
| courses/science-grade-1/u04-2/d036.md "3 min. Launch"; cards-check-35-37.md:10 against :25 | S10 | The teacher is told to say "the pairs and records are new and invented for practice", but the sound records are specified as real adult-taken records ("Nothing is invented as a result") | Launch line: "The goat and hen pictures are invented for practice. The sound records are recordings of real tests made by an adult." Change cards-check-35-37.md:10 the same way | Day, data (cards) |
| plan.py check, filtered: 13 FAIL lines, "section 1.1 to 8.1 (science-grade-1-uNN-N) is not in data/units.csv" | (gate) | No section of the course is registered in data/units.csv | Add the 13 section rows to data/units.csv in the registry's format. This is a lead or pipeline job; no content changes | Data |
| scope-and-sequence.md:98, 120, 128, 147, 157; s02.md:96 and others ("labelled"); goal maps ("recognise") | AGENTS.md US spelling | UK spellings: behaviours, Analyse, specialised, neighbours, labelled, recognise | Change to behaviors, analyze, specialized, neighbors, labeled, recognize when each page is next edited | Scope, unit plan |
| courses/science-grade-1/u02-1/d012.md student page ("I can say what I saw, so.") and At home ("Never taste it" twice); d013.md read-aloud ("six pages, one animal in each scene" while the hare fills four) | S9 (clarity) | Garbled learning target; duplicated safety line; page count contradicts the scene list | "I can say what I saw and what it shows." Keep one "never taste it". "Six pages: four about the hare, one about a fish, one review" (or the actual layout of the read-aloud file) | Day |

## Known gaps (named by the rubric, not counted again)

- docs/APPROACH-SCIENCE.md is not written (3e).
- There is no course family note. Note: unit family notes do exist in English and Spanish (for example courses/science-grade-1/u04-1/family.md).
- There is no course supplies list. Unit costs are stated as unverified allocations.
- There is no course safety page and no safety-agent read against published guidance (S5, 3h). This is the one known gap that is also a door.

## For the lead

- Item-level choices made here: which units to sample, the EQuIP and Gateway point estimates, and part pass rather than fail for S2, S3 and S6 (each found in one sampled unit, with a local fix).
- Nothing here needs a scope, money, people or audience decision, except finding 3's choice between real plant records and labelled models. That choice changes what the scope promises, so it may be Cory's.
- No sources were added. No browser-check pages arose.

## Fixes applied (2026-11-22)

- Unit 4 records (unit plan, then day and data): applied at day and data stage. cards-day33.md, cards-exits-28-31.md, cards-exits-32-34.md and cards-check-35-37.md state what each finished record must show (dated three-frame card, printed heard mark or motion lines, sound on or off label) with a hand-drawn paper fallback from real trials; d028 and d033 Before class name the early start. Left: running item 2 live for every group is an assessment design change in s04.md (listed for the lead).
- Day 20 shoot photographs (day; section plan): applied at day stage. d010 Before class starts the held-back shoot; d020 checks it; sheets-day20.md states what each photograph must show and gives a drawn fallback. Left: growing a real class shoot for days 11 and 12 (strips-shoots.md already prefers the class's own photographs).
- Plant parent-young seam (scope, unit plans 2, 3, 7): left, for Cory. Every invented master in units 2 and 3 now carries the printed words "invented for practice".
- Unit plan exit tables (unit plan): left, listed for the lead.
- practice column (data): applied. All 183 exit and end rows name the code's science and engineering practice from data/standards/ngss-pe-dimensions.csv.
- Days 10 and 13 teach by telling (section plan, then day): left. Moving the read-alouds after the evidence reorders parts across days 10, 11 and 13; not a local edit.
- E11a, E11b, E12a exits (section plan 2.1): left. Re-posing them as evidence needs new held-back pictures, keys, wrongs and handbacks; listed for the lead.
- Unit 7 media (unit plan, data): left. Fawn photograph rights and a credited duck photograph need a browser and a rights call.
- d036 launch provenance (day, data): applied in d036 and cards-check-35-37.md.
- units.csv FAIL lines: left, known repository-wide gap.
- UK spellings (scope, unit plan): applied in s02, s03, s05, s07 (edited this pass) and in the course files; scope-and-sequence.md and the other unit and section plans left for their next edit.
- d012 target and duplicate line, d013 page count (day): applied.
- Known gaps: the course safety page is now written; APPROACH-SCIENCE.md, a course family note and a supplies list are left (rubric known gaps).
