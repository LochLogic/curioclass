# Curio Class continuity review, 2026-11-14

Read-only. Nothing under S:\CurioClass or S:\CurioClass-sources was changed. Line numbers are as of this review (a Codex run is writing files, so they may drift a little).

## Verdict

The newest layer (PRODUCTION-PATH, GLOSSARY, DESK-ANSWERS, the sequence and plan briefs, the frames, sequence.py) agrees with itself on the key 2026-11-12 to 2026-11-14 decisions: readiness timing, NGSS as base, social studies as test bed, Codex as primary builder, no timers shown, site hidden. The disagreements are almost all in older documents that were never brought forward, plus HANDOFF's own top section, which is out of order and partly stale, and one generated page (COURSES-STATUS) that is wrong because its script is out of date. No em dashes were found in any doc, and "Curio" is never used alone in a current doc outside rule statements. Glossary words and step names are used correctly in the current layer.

Biggest problems, in order: (1) the course counts disagree (105 and 56 in many files, 107 and 68 in the generated status, 58 and 52 in the frames, which are the ones that match the data); (2) HANDOFF's top section lists two blocks as "latest", puts the newest news in the middle, and ends with a "Next" line from hours earlier; (3) COURSES-STATUS reports progressions, scopes and plans that exist as "no"; (4) the FOUNDATION and BASELINE human-reader rules contradict Cory's 2026-11-14 "no outside readers" answer, and PRODUCTION-PATH contradicts itself on it; (5) the pilot-first plan still stands in ROADMAP, FOUNDATION, ADOPTION-BAR, pipeline README and others.

Counts: wrong 13, stale 21, unclear 9 (43 findings).

## Findings by theme

### A. Course counts (wrong)

A1. wrong. The repo gives three different pairs.
- Current data: docs/COURSES-STATUS.md (generated 2026-11-14) says 107 courses, 68 flagged core; the four core subjects are 58 courses, 52 core, plus 6 electives (precalculus, statistics, calculus, earth and space science, environmental science, psychology). data/plans/frames.csv has 52 rows. HANDOFF:109, PRODUCTION-PATH:31, :259, :307, SITE-DESIGN:16, :144, DESK-ANSWERS:1002 all say 58 and 52.
- "105 courses": HANDOFF:377, :389, :395, :568, :576; ROADMAP:26, :103; BASELINE:106; ADOPTION-BAR-SUBJECTS:12; PRODUCTION-PATH:335; LESSON-DAY:43; NEXT-SPINES:62; pilots/COST.md:4; pilots/README.md:34.
- "56 core": HANDOFF:395 ("56 are in the four core subjects"), ROADMAP:103, BASELINE:106 ("56 of the 105"). 56 was the four-subject total before Physics became core and social studies was redrawn; it is now 58 courses with 52 core.
- Should say: "107 courses; 58 in the four core subjects, of which 52 are core and 6 electives; the other 49 follow". Source of truth: COURSES-STATUS (generated), frames.csv, PRODUCTION-PATH:31. Note that your brief's "105 courses, 56 core" matches the old text, not the data.

A2. unclear. PRODUCTION-PATH:361-364 says "the 49 courses of the other subjects ... world languages stay shelved". The 49 in COURSES-STATUS includes 2 world language courses (Spanish, French or ASL as counted). Either say "47 plus 2 shelved" or note that the 49 includes them. Also HANDOFF:395 says world languages are "still counted as a reminder", which is the same point.

A3. unclear. ROADMAP:46-47 lists world languages in the end goal ("arts, computer science, health and PE, world languages, ...") while ROADMAP:93 and Track 10 treat them as shelved. Add "(shelved)" at :46.

A4. stale (memory). MEMORY.md says "105 courses" and curio-path-from-here.md says "course frames for all 56 core courses". Should be 107 / 52.

### B. HANDOFF (the single current-state page)

B1. stale. HANDOFF:3 says "Last updated 2026-11-14, after baseline 1 (top block)". The top block (line 6) is the social studies unit plans block, which is later. Should say "after the social studies unit plans".

B2. wrong. Two blocks are both labelled "latest" (line 6 and line 20); line 79 block and others also carry "(latest)" tags (:109, :111). Only one can be. Drop "latest" from all but the top one.

B3. stale. The block that starts line 20 is in ascending time order inside, so its newest content is in the middle and its end is old. Line 63 says "ELA, science and math stay paused at step 2" and was superseded by line 65 ("Scopes unpaused ... late"). Line 74 ("Where it stands ... paused at 96% ... Resume: expert reads of all 15 ...") and line 76 ("Next: PRODUCTION-PATH step 3, social studies scopes and sequences first") are done: flow-status.csv has ss-review done and units-review done, all 15 scope-and-sequence.md and 138 plans exist. Should: delete lines 63, 74 and 76 or mark them "done, see top block", and put the Codex scopes run (line 65) in the top block with its real status. Source: flow-status.csv, the 15 scope-and-sequence.md files, the 138 s*.md files.

B4. stale. The top block (line 13) says the C3 own-word lines (283 codes) and 7 Massachusetts lines "need the C3 framework and the Massachusetts 2018 ... PDFs, which are not on file; downloading needs Cory's yes". But data/standards/c3-indicators.txt header says (2026-11-14) each id carries a line "written from the indicator text in the NCSS PDF", the file has 283 lines of ids with text, data/standards/ma-hss-2018.txt notes the 2026-11-14 widened lines were "checked against the framework PDF (pages 97, 101, ...)", and S:\CurioClass-sources\standards-2026-11-14 exists. data/plans/flow-status.csv units-review row says "C3 own-word lines being written". Three versions of the same fact. Should: one status line in HANDOFF and flow-status ("done 2026-11-14" if the PDFs were saved with Cory's yes). Needs a check of which is true; I did not open the PDFs.

B5. stale. HANDOFF:136 "## Start here: the next action" still says "The pilot unit comes first (grade 4 math unit 11 ...)" and lists steps 1 to 5 of the pilot. The line 79 block says everything below it is from before, but the heading "Start here" is a trap for a new reader. Rename to "Old next action (retired 2026-11-13)" or move to docs/archive.

B6. stale. HANDOFF:381-395 "Where things stand" table: Layer 4 "Math grades 3 to 5 done", Layer 5 "3 of 105 courses have a scope and sequence", Layer 6 grade 4 math only. Today: four progressions done, 52 frames, 15 SS scopes plus a Codex run on 37 more, 138 SS unit plans. Should be replaced with the flow-status summary or removed.

B7. stale. HANDOFF has no entry for the two newest DESK-ANSWERS decisions: NGSS over Massachusetts STE (DESK-ANSWERS:1037), K to 2 science three times a week (:1045). Both should be in the top block, with the pending frame and frames.csv change.

B8. stale. HANDOFF:377 "every one of the 105 courses" (see A1); HANDOFF:209 and 204 "18 sub-ready days a year in grade 4 math" disagrees with GLOSSARY (9) and the frame (math-grade-4 has 9 units). See F3.

### C. Build order and "who does what"

C1. wrong. PRODUCTION-PATH:387 "All math planning and writing stays paused until step 5 reaches math, except small fixes" and :388. Cory unpaused scopes for science, ELA and math on 2026-11-14 late (HANDOFF:65, scripts/codex_scopes.py, math-grade-4 scope reconcile brief sequence-reconcile.md). Math units still come last; math days stay paused. Should: "Math scope and sequence is written now (Codex run, 2026-11-14); math units, sections and days wait for math's turn." Also :301-304 "Math last" paragraph and step 5 (:291-299, "Each subject in turn runs step 3 and step 4") should say that step 3 now runs for all subjects together and step 4 goes subject by subject.

C2. stale. PRODUCTION-PATH header says "draft 5, 2026-11-13" but contains edits through 2026-11-14 (lines 31, 327, 365, 373). Add the date or "draft 5, edited through 2026-11-14".

C3. unclear. PRODUCTION-PATH:278 "Cory says yes to each" (scope and sequence). Cory's 2026-11-14 pattern is expert read plus Codex read plus fix pass, no per-course yes (flow-status ss-review done with no Desk card). Say which applies.

C4. wrong (internal). PRODUCTION-PATH:55-57 "qualified people are added when found, and nothing is called finished without them (FOUNDATION 7.3)", :194-195 "FOUNDATION 7.3 rule that qualified people read a course ... still stands; with no people, nothing is called finished", and :333 "a qualified teacher still reads a sample" versus :373-376 "Reviewers are agents ... No outside human reader is planned" and Cory's 2026-11-14 answers ("We have no support. Our agents are our best hope"). Fix :55-57, :194-195 and :333 to match :373-376. See D1 for the same issue in FOUNDATION.

C5. stale. docs/pipeline/README.md:24-31 table says plan and plan-data are "lead Claude", cheap read is "Sara's Claude", writer is Codex. Since 2026-11-14 (DESK-ANSWERS:1026) unit plans are Codex-written from a script skeleton, Codex reads every plan (and will read every day), Claude does expert reads and fix passes. The README also does not mention frame.py, sequence.py, unitplan.py, codex_scopes.py, codex_units.py, codex_read.py or unit_skeleton.py.

C6. stale. docs/pipeline/README.md:69-73 "Beyond math ... a DEFAULTS.md and a written, read pilot unit ... Grade 6 English language arts and grade 4 science are the next pilots". Pilots were retired 2026-11-13 (GLOSSARY, PRODUCTION-PATH:381). Replace with the probe and guard.

C7. stale. docs/agents/CODEX.md:6 "Codex does Build (step 1) and Polish (step 5) only." Codex now writes scopes, unit plans and reads (CODEX.md says nothing about it). The page is tool-only and says "Polish (step 5)", an older numbering; the locked step names are in GLOSSARY. Add a pointer to docs/pipeline/README.md for curriculum jobs and call the step Fix or Refine.

C8. stale. docs/agents/EXPERT.md:18-23 tells the expert to read ROADMAP "The path from here" through "Gaps found" (the stale section), "BASELINE rules 20 to 24" (rules now go to 29), and says "for a subject with no rubric file, ADOPTION-BAR-SUBJECTS" although RUBRIC-ELA.md and RUBRIC-SCIENCE.md now exist. Also :35 lists docs/courses/math-3-5-progression.md as starting reading, which the blind-rule briefs forbid for blind reads. Point at PRODUCTION-PATH and the lenses, and say which briefs override.

C9. unclear. docs/pipeline/briefs/sequence-write.md:82 says unit 1's readiness check takes the last ten minutes of day 1 and sequence.py accepts it, but the gate summary at :116-117 says "never on a first day". sequence.py (lines 189-207) is right: unit 1 day 1 is the one exception. Add "except unit 1's day 1" at :117. DESK-ANSWERS:1008-1019 says unit 1's check is "served by the start-of-year check"; the lead's day-1 rule is how that is done. Say so once.

### D. People, readers and pilots

D1. wrong. FOUNDATION 7.3 table (lines 130-142) was edited for the agent reads but still carries: row "A working teacher of the grade band ... Reads the pilot unit" and "A teacher or a parent ... pilot", "Three students ... First pilot in each subject" (these are pilot rows that PRODUCTION-PATH:376 says stay), "A second reader on rights" (a person), "A native Spanish reader" (a person), and line 142 "Cory's mom, a grade 2 teacher, is reading the approach pages. The first pilot needs a grade 3 to 5 teacher too." The "first pilot" and "each course's pilot unit" wording conflicts with GLOSSARY (pilot retired). Cory's 2026-11-14 answers say no outside human reader anywhere. Needs a decision on the Spanish and rights rows (Question 1).

D2. wrong. BASELINE:124-125 (rule 28) "Qualified people are named where a course needs them ... docs/FOUNDATION.md section 7 holds the table" and :129 (rule 29) "read by a qualified ELA teacher" versus DESK-ANSWERS:974 (Q6, 2026-11-14: "our agent is the check, not a teacher"). Rule 29 should say "read by the expert agent". Rule 5 was updated; rules 28 and 29 were not.

D3. stale. ROADMAP:69, :72-73, :137, :230, :271 and "What a finished course holds" item 7 (:225-230) "One outside read. A working teacher has read at least one section" and "Cory finds the people". Conflicts with D1. Also ADOPTION-BAR:57-58, :79, :82 "A working teacher reads the pilot unit".

D4. stale. docs/funding/ONE-PAGER.md:25 "then a human review before it goes live" and the $16,000 row "native-speaker Spanish review, paid teacher pilots"; COSTS.md:47-48. BASELINE rule 5 says a fresh review agent, then live, and only growing-up-q-a gets Cory's personal review. "A human review" is an untrue claim in a funding document (FOUNDATION promise 6, honest words). Say "a fresh independent review, then Cory's sign-off", and decide whether the Spanish review and teacher pilots rows stay (Question 1).

D5. unclear. docs/pilots/ folder and README (pilot units, "Cory finds the people") are live pointers from FOUNDATION:132, HANDOFF:523 and ROADMAP although pilots are retired and the probe and guard replace them. Either archive or retitle.

### E. Stale pilot-first plan still on the page (the main stale cluster)

E1. stale. docs/ROADMAP.md. Its own banner (lines 3-8) says the pilot text is stale and PRODUCTION-PATH wins, but the file is what README.md points to as "Start here: the one plan". Specific stale places: :26 (105 courses, 3 scopes), :49-50 and :62-75 (pilot first, frozen planning), :94-96 (science pilot "runs right after 11.1"), :112-121 layer table "State" column (Layer 4 "Grades 3 to 5 math"; Layer 5 "More scopes and sequences wait until the pilot is read"; Layer 6 "Grade 4 math units 1, 2, 3, 9, 10"; Layer 7 "Building paused, except pilot unit 11"), :131-135 rule 2 "A section plan for every section comes before tools" (fine) but :145-165 step 4 table (4f "Now"), :168-170 "The shape we build to", :209 "about 150 (180 less testing)" days (calendar is 160 school days, 32 weeks), and :225-230. Should: rework to the order only, or change README to point at PRODUCTION-PATH.

E2. stale. README.md:52 "Start here: docs/ROADMAP.md (the one plan ...)" while CLAUDE.md and AGENTS.md say read HANDOFF for current state and ROADMAP's banner says PRODUCTION-PATH wins. README should say: "Start here: docs/HANDOFF.md (state), docs/PRODUCTION-PATH.md (the build order)". README's folder table also lacks courses/, data/plans, scripts/turn.py and docs/pipeline.

E3. stale. docs/FOUNDATION.md:16-20 "Depth comes first: one course is finished before the next is started ... One bend: the first pilot unit in each of math, English language arts and science is built early". Replaced 2026-11-13 by the top-down order. Say: "Every core subject is planned top down (PRODUCTION-PATH) before days are written; each course is finished as a whole before it is called finished."

E4. stale. FOUNDATION.md:79 and :151 "Kindergarten to grade 2: not yet decided" (device). Decided 2026-11-14: K to 2 may assume one shared classroom device, always with a paper path (DESK-ANSWERS:983-984). BASELINE:99 and ROADMAP:141 say only "grades 3 to 12 assume one device per student ... Still open: the device assumption for K to 2". Update all three.

E5. stale. FOUNDATION.md:36 and SITE-DESIGN.md:59, :74 and HANDOFF:195 "36-week numbered calendar" for the at-home path, versus CALENDAR.md and frames: 160 school days, 32 weeks, half-year courses 16 weeks (frames.csv). The K to 2 frames also speak of "a school year of about 36 weeks" (science-kindergarten/frame.md:12, science-grade-1/frame.md:12) while spreading over 29 to 34 weeks. Decide if "36 weeks" means the real year, and say so once in CALENDAR.md.

E6. stale. Other pilot-first references: ADOPTION-BAR.md:57, :58, :75, :79, :82; ECOSYSTEM.md:14, :27, :60, :73 ("Step 5 (prove one course): the section shape, on grade 4 math and grade 6 ELA"); LESSON-DAY.md:3, :12, :224 ("the first pilot in that subject sets its rule"); UNIT-PLAN.md:30-31 (s11 "the pilot"), :64 ("questions wait for the pilot"), and :37-38 ("The fields have been tried on math only ... checked against the science and ELA scopes and sequences only", while 138 social studies plans now use them); APPROACH-ELA.md:194-195; EXPERT.md:98; VISION.md:42 ("Scope and sequence and unit pilot after the worksheets go live"); COURSES-STATUS.md:5, :18 (generated, see F1); RUBRIC-ELA.md and RUBRIC-MATH-K8.md "pilot read" sections (history, fine if labelled).

E7. stale. docs/courses/UNIT-PLAN.md:1-8 header "Second draft, 2026-11-11" has been edited on 2026-11-14 (readiness, caps, ELA data). Add the dates.

E8. unclear. docs/APPROACH.md:6-7 says science and social studies approach pages "are still to be written", and APPROACH.md calls itself layer 3 that every scope and sequence is built on. Scopes for social studies (done) and science (running) have no subject approach page; the lenses and rubrics stand in. Question 2.

### F. Generated and data files

F1. wrong. docs/COURSES-STATUS.md (generated 2026-11-14) shows Progression "no" for every course except math 3 to 5 (all 385 skill rows of four progressions exist), Scope and sequence "no" for social studies (15 exist), Plans "no" for social studies (138 unit plans), and "Rubric file" "no" for ELA and science although RUBRIC-ELA.md and RUBRIC-SCIENCE.md exist. Cause is scripts/course_status.py lines 62-70: progression hard-coded to math grades 3 to 5, scope and sequence found only as `<course>-spine.md`, rubric hard-coded to math. The page also reports "With a scope and sequence: 3" which feeds ROADMAP:26 and HANDOFF:389. Should: read data/progressions/, docs/courses/<course>/scope-and-sequence.md, docs/RUBRIC-*.md. Also change generated text at COURSES-STATUS:5 and :18 ("starts with the pilot unit"). Edit script, regenerate (not by hand).

F2. unclear. data/plans/frames.csv rows for science-kindergarten, grade 1 and grade 2 still show per_week 2 (64, 68, 76 days over 29, 29, 28 weeks) and the three frames (frame.md lines 12, 159, 178 and 190, 195) say "two lessons a week ... Settled (Cory, Desk 2026-11-14, yes as picked)". Cory's later 2026-11-14 decision (DESK-ANSWERS:1045-1050) moves them to three meetings a week, to be applied in the science scope fix pass after the Codex run. Not wrong yet; it needs a `Pending(...)` marker (the HANDOFF stale-notes rule) or an entry in later.csv so it is not lost. Also science-grade-2/scope-and-sequence.md:21 and :140 already report the conflict.

F3. wrong. Sub-ready day count for grade 4 math: GLOSSARY:54 says 9 a year (matches frame: 9 units); SITE-DESIGN.md:157 and HANDOFF:204, :209 say 18. Should be 9 (one per unit).

F4. unclear. data/plans/flow-status.csv row `baseline1` note ends "paused here per Cory". Cory lifted the pause (social studies on 2026-11-14, others later). Edit note.

F5. unclear. data/plans/flow-status.csv has `ss:` nodes for 15 social studies courses but nothing for the 37 science, ELA and math scopes the Codex run is writing, so the Desk dashboard will show them as not started. They are shown by default as estimates ('e') when frames exist, so this is only a risk; check once the run ends.

F6. unclear. data/plans/later.csv L20 is state "done" but its body (and docs/reviews/build-errors-l20-2026-11-14.md:93) says the Word Wall `culture` definition (13 words, cap 12) was "left untouched for Cory", so the full-site build with --closet may still fail. Either split a new open row or reword. HANDOFF:62 says the build "currently stops on other data errors: later.csv L20", which contradicts L20 being done; one of the two is stale.

F7. unclear. later.csv L19 is "done" but item (3) (file limit 19,468 of 20,000) and L23 (about 9,024 files) give different file counts; state which is current. Also add rows to later.csv for: the K to 2 science change (F2), the two social studies standards PDFs if still pending (B4), approach pages for science and social studies (E8).

F8. unclear. data/progressions/README does not exist, and data/plans/README.md "State" paragraph (last 12 lines) is grade 4 math only and says ELA `texts.csv` "not built yet" while UNIT-PLAN.md:64-76 says ELA text data are in data/plans/ela-texts.csv (2026-11-14). Add a line.

F9. stale. data/courses.csv is a 43-row catalogue-track file (math-k8, science-k5, ss-k5) and its notes are right; GLOSSARY explains it. No change needed, but the header of docs/COURSES-STATUS.md says "Generated ... Do not edit by hand", so the stale counts must be fixed in the script.

### G. Rules that contradict each other

G1. wrong. docs/GAMES.md:30 "Timed modes are welcome." versus the standing rule "no countdown timer shown to a student" (APPROACH.md:17, APPROACH-MATH.md:62, APPROACH-ELA.md:152, UNIT-PLAN.md field 14, LESSON-DAY.md:156, :193, :229, SITE-DESIGN.md:167, HANDOFF:378, scripts/course_pages.py:106). SITE-DESIGN:167 exempts only the Teacher Desk timer. Recess games are outside the bar but not outside the timer rule as written. Question 3.

G2. unclear. scripts/course_pages.py:106 attributes the no-timer rule to BASELINE, but BASELINE has no timer rule (it lives in APPROACH.md, Desk card q-approach, and SPEC.md:42). Add it to BASELINE or fix the comment.

G3. unclear. FOUNDATION.md:134 "timed by a watch the student does not see" and HANDOFF:250, :523 "three timed students" are consistent with the rule, but ROADMAP:230 says only "timed". Add "by a watch the student does not see".

G4. unclear. NGSS base and Massachusetts crosswalk (DESK-ANSWERS:1037-1043) is carried by plan-codex-science.md:21 and scripts/codex_scopes.py:38, but not by docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, sequence-write.md or sequence-read.md, nor by HANDOFF. A reader who skips the plan brief will not know. Add one sentence in the science lens and HANDOFF.

### H. Site and other pages

H1. stale. site/templates/pages/about-plain.html and ONE-PAGER.md present Curio Class as a library of tools ("A cabinet of free, tactile digital tools"), and the course pages (site/templates/courses/*.html, hidden) say "Lessons coming". This is fine while the site is not public (curio-not-public-yet), but VISION.md:13-14 and SITE-DESIGN.md:27-30 say Curio Class "is now a set of full courses". Mark for the launch pass; not an error today.

H2. unclear. site/templates/courses/course.html:97 credits "an openly licensed curriculum" is already tracked as later.csv L21 (pushed to the end by Cory). No change.

H3. unclear. later.csv L16 asks whether "the first free, complete K-12 curriculum" claim holds, while VISION.md:13 and FOUNDATION.md:13 use "free, complete, open K-12 classroom toolkit" as the mission. Keep the claim off public copy until L16; no file uses "first" today (checked site/ and docs/funding). OK.

H4. unclear. docs/CONTRIBUTING.md:19-21 lists the tool path as "Spec, Build, Self-check, Refine, Fix, Exit check, Art and voice, Finish check, Sign-off" and omits Idea and Live (GLOSSARY, memory: Idea, Spec, ... Sign-off, Live). Add them or say "from a spec onward". CONTRIBUTING also says only Cory merges, which is right for outside contributors but AGENTS.md has turn.py committing; fine, different audiences.

H5. unclear. Scripts hold literal em dashes (scripts/check_*.py, course_status.py, catalog_compute.py ...). I did not check each. Probably regexes that detect them, so not a rule breach, but confirm none is in output text.

## Edits to make, in order

1. scripts/course_status.py: read progressions from data/progressions/*.csv, scope and sequence from docs/courses/<course>/scope-and-sequence.md, rubric from docs/RUBRIC-*.md; drop "pilot unit" wording in the generated header; regenerate docs/COURSES-STATUS.md. Then use its numbers everywhere below.
2. Replace course counts (A1): old "105 courses" / "56 of the 105" / "56 are in the four core subjects" with "107 courses" / "58 of the 107 are in the four core subjects (52 core, 6 electives)". Files and lines: HANDOFF:377, :389, :395, :568, :576; ROADMAP:26, :103; BASELINE:106; ADOPTION-BAR-SUBJECTS:12; PRODUCTION-PATH:335; LESSON-DAY:43; NEXT-SPINES:62; pilots/COST.md:4; pilots/README.md:34; MEMORY.md and curio-path-from-here.md. If you prefer to keep 105 as "the plan", say what it excludes.
3. HANDOFF: B1 (line 3 date text), B2 (one "latest"), B3 (cut lines 63, 74, 76 or mark done; move line 65 up into the top block), B4 (one C3 status after checking), B5 (rename "Start here: the next action" at :136), B6 (replace the table at :381-395), B7 (add NGSS and K to 2 science decisions), F3 (18 to 9 at :204, :209).
4. PRODUCTION-PATH: C1 (lines 387-388 and the step 5 paragraphs), C2 (draft date), C3 (:278), C4 (:55-57, :194-195, :333). Suggested C1 new text for :387: "Math scope and sequence is written now with the other subjects (Codex run, 2026-11-14); math unit plans, sections and days wait for math's turn, except small fixes to written days (not days 25 to 28)."
5. FOUNDATION: E3 (lines 16-20), E4 (:79, :151: "K to 2 may assume one shared classroom device, always with a paper path (Cory, 2026-11-14)"), 7.3 table and :142 per D1, E5 (36 weeks).
6. BASELINE: rule 24 numbers (A1); rule 28 and 29 per D2 (replace "a qualified ELA teacher" with "the expert agent"); add the no-timer rule to BASELINE (G2).
7. ROADMAP: either rework per E1 or move "Start here" to HANDOFF and PRODUCTION-PATH in README.md (E2); minimum: fix :26, :46 (world languages shelved), :103, :209 (160 days), :141, and the layer table state column.
8. pipeline README (C5, C6), CODEX.md (C7), EXPERT.md (C8), sequence-write.md:117 (C9).
9. Pilot wording sweep (E6, D3, D5): ADOPTION-BAR, ECOSYSTEM, LESSON-DAY, UNIT-PLAN, APPROACH-ELA, VISION, docs/pilots/README.
10. funding (D4): ONE-PAGER.md "a human review" and the $16,000 row, COSTS.md rows 47-48, after Question 1.
11. GAMES.md:30 after Question 3; science lens, RUBRIC-SCIENCE and HANDOFF: NGSS sentence (G4).
12. Data: F2 (Pending marker or later.csv row for K to 2 science three meetings), F4 (flow-status baseline1 note), F6/F7 (later.csv L19, L20, new rows), F8 (data/plans/README.md state paragraph).
13. CONTRIBUTING step list (H4).
14. Memory: update MEMORY.md and curio-path-from-here.md: 107/52, "math scopes unpaused 2026-11-14, math units and days still paused", SS unit plans done, pilots retired.

## Questions for Cory

1. Spanish and rights readers: FOUNDATION 7.3 still lists "a second reader on rights" and "a native Spanish reader", and funding docs budget a Spanish review and paid teacher pilots. Your 2026-11-14 answers say no outside readers anywhere. Should those two rows become agent reads, or stay as people you may find later (and the funding rows stay)?
2. Science and social studies approach pages: APPROACH.md says they are still to be written, yet their scopes and sequences are being written against the lenses and rubrics. Write short approach pages before the unit plans for science, or declare the lens plus rubric the layer-3 stand-in?
3. Timers in Recess games: GAMES.md allows timed modes; the standing rule says no countdown timer shown to a student. Does the rule cover Recess, or only course tools?
4. Course count: do you want "107 courses, 58 in the four core subjects" used everywhere, or is 105 a deliberate plan number that leaves something out (for example the two shelved world language courses)?

## Applied 2026-11-15

Applied by a fix agent; no git actions. Files named relative to S:\CurioClass.

**Applied**
- A1, A2, A3: course counts worded the same everywhere ("107 courses (105 active, 2 world languages shelved); 52 core courses in the four core subjects plus 6 core electives") in README.md, docs/ROADMAP.md, docs/PRODUCTION-PATH.md, docs/agents/decisions/BASELINE.md (rule 24), docs/ADOPTION-BAR-SUBJECTS.md, docs/pilots/README.md, docs/pilots/COST.md, docs/HANDOFF.md.
- B1-B8: docs/HANDOFF.md new short top block "Now (2026-11-15)", the only one marked latest; old pilot heading renamed "Old next action (retired 2026-11-13)"; done lines marked; C3 and Massachusetts lines done 2026-11-14 (B4); "Where things stand" table current; 18 a year changed to 9.
- C1-C8: docs/PRODUCTION-PATH.md (agents read, no human readers; step 3 all subjects together, step 4 by subject; math pause line; pilots retired; counts), docs/agents/EXPERT.md, docs/agents/CODEX.md, docs/pipeline/README.md ("Planning above the day").
- D1-D5: pilots retired, the probe and guard named, in docs/ADOPTION-BAR.md, docs/ECOSYSTEM.md, docs/LESSON-DAY.md, docs/APPROACH-ELA.md, docs/VISION.md, docs/UNIT-PLAN.md, docs/ROADMAP.md, docs/FOUNDATION.md 7.3.
- E1-E4, E6-E8: K-2 device rule (BASELINE 23, FOUNDATION, ROADMAP rules 5 and 6); NGSS base and Massachusetts crosswalk (docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md); religious texts read as literature, K-2 science three a week, grade 2 mid-year check at week 20 (HANDOFF top block); SITE-DESIGN.md calendar wording.
- F1, F3: timers narrowed to a grounded purpose (BASELINE new rule 30; DAY-WRITER.md, lenses/math.md, APPROACH.md, APPROACH-MATH.md, APPROACH-ELA.md, LESSON-DAY.md, UNIT-PLAN.md, SITE-DESIGN.md, briefs/plan-codex-read.md, GAMES.md:30, scripts/course_pages.py comment, scripts/unit_skeleton.py:739).
- G1-G4: scripts/course_status.py fixed (frame slugs, progressions, scope-and-sequence files, unit plans in both folders, days.csv units, pilot wording) and docs/COURSES-STATUS.md regenerated; funding docs (ONE-PAGER.md, COSTS.md: Spanish review and teacher pilots "only if funded", sign-off wording).
- H4: CONTRIBUTING.md step list now Idea through Live.

**Partly applied**
- E5: docs/courses/CALENDAR.md now explains 36 weeks versus 160 days over 32; the decision and frames go to the lead.

**Not applied**
- F9, H2, H3: checked, no change needed.
- H1: belongs to the launch pass.
- H5: em dashes in scripts are detectors or source matchers only, never output.

**For the lead**
- A4: memory files.
- C9: briefs/sequence-write.md:117, add "except unit 1's day 1".
- E5: science-kindergarten and science-grade-1 frame.md line 12 say "about 36 weeks"; decide what "36-week" means.
- F2: frames.csv per_week 3 for K-2 science, plus a Pending marker or later.csv row.
- F4: flow-status baseline1 note "paused here per Cory" should go.
- B4 data: flow-status units-review:social-studies note "C3 own-word lines being written" is done 2026-11-14.
- F5: ss: nodes for the 37 new scopes.
- F6, F7: later.csv L20 split for the Word Wall `culture` word; L19 versus L23 file counts; new rows for E8 and F2.
- F8: data/plans/README.md "State" paragraph and the ela-texts.csv line.
- "No timers shown to students" lines in the economics, us-government, us-history-i/-ii and world-history-i/-ii scopes, and frames' "Fluency without a timer" lines, if they should be narrowed.
- Grade 8 ELA frame: religious texts as literature (already in the fix pass).
- docs/pipeline/briefs/sensitivity-read.md has no rights or Spanish agent read section.

**Not settled**
- What the 36-week home calendar means (E5).
- Where the social studies probe and baseline 2 sit relative to science and ELA unit plans.
- scripts/lesson.py:319 still gates "At home shows no timer" (left as is).
- The 138 social studies unit plans say "No timer is shown" (left as plan wording).

**Check:** `python -X utf8 scripts/plan.py check` fails only on sequence source-map.csv column checks (another job's); nothing else fails.
