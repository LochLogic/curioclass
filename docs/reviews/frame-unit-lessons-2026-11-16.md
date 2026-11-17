# Lessons from below the frame, for the six grade 12 elective frames

Read-only research, 2026-11-16, in S:\CurioClass. Sources: AGENTS.md, HANDOFF.md, PRODUCTION-PATH.md, the briefs
(frame-write, sequence-write, sequence-read, plan, plan-codex-math and -science, plan-read, plan-codex-read, unit-lens,
unit-ruling-fix, unit-correct, unit-calendar-fix), UNIT-PLAN.md, data/plans/unit-rejections.csv (155 rows: 76 lead,
69 upheld, 5 overruled, 5 noise), DESK-ANSWERS from 2026-11-13, the high school sequence reads (expert and Codex) for
Algebra I, Geometry, Algebra II, Biology, Chemistry, Physics, the plan reads for the high school social studies
courses, the probe measures, sample-read-loop-2026-11-16.md, the 2026-11-15 structure passes, and the 806
codex-write-lens files of 2026-11-16 (1,683 findings, counted by grep; counts below are grep counts, so approximate).

Context worth knowing first: both social studies probes traced 0 findings to a frame (probe-social-studies-2026-11-15.md
and -2-). The frame-rooted faults show up one layer down, in the scope and sequence (days.csv), and from there in the
unit loop as "lead" rulings the unit fixer could not make (days.csv is outside its brief). So the cheapest fix is a
frame that says the thing before the scope writer guesses.

## Lessons

1. **Say what each day kind means in this course.**
   (a) Scope writers labelled first-teaching days Fluency or Application; units then taught new content on "practice"
   days or scored work from them, and every fix needed a days.csv change by the lead.
   (b) unit-rejections.csv: 24 lead rulings to relabel days (biology 10, chemistry 01 and 04, physics 03,
   science-grade-8 02, math-grade-8 07 and 08, ELA grades 2, 7 to 12); 14 rows on fluency-day scoring. Lens files: 32
   findings of a Fluency day introducing new content (chemistry s01, s02, s04; physics s03, s06; geometry s01, s02;
   biology s02, s10). GLOSSARY and sequence-write name the five kinds but define them only as "in every subject".
   (c) A "Day kinds" bullet: first explicit teaching of anything (a formula, model, method, term set) is
   Understanding; Fluency practises only what an earlier day taught; drafting, investigating, editing or using taught
   ideas on a new task is Application. Say what Fluency looks like in this course, or that the course has few or none.
   (d) All; most science and psychology, which have no fluency standards to anchor the word.

2. **Readiness and retrieval: give the evidence, not a verdict that goes stale.**
   (a) Frames wrote per-row "readiness" or "retrieval" in prose and Seams cells; the scope's counted rule then
   differed, the frame was not updated, and unit writers met two contracts. Loose words ("idle two or more grades",
   "kept in use", "maintained by") hid rows that were never taught on a day.
   (b) About 50 review files flag stale frame readiness wording (sequence-geometry-codex finding 5, -algebra-i-codex 5,
   -algebra-ii-codex 5, -chemistry-codex 4, ELA grades 3 to 5 "Fix (frame)"); sequence-physics "Across the band" 1 and
   2 (Biology's gloss cost readiness in seven units; "kept in use" claims hid idle rows); lead ruling geometry 08;
   unit writers: "The frame still describes both as readiness" (codex-write-geometry-s07, s08; algebra-ii-s01).
   (c) For each assumed row: the grade and the core course day (from that course's days.csv) of its last use, then the
   treatment that follows from the count, with a line that the scope gate's rule 2 count governs and the scope fix
   pass updates the frame. No "kept in use" without a day number. A course open to grades 11 and 12 says which grade
   the count starts from and what changes for the other (psychology: Chemistry grade 10 rows flip between retrieval and
   readiness); a course with routes says which route the rows assume (calculus after precalculus, or both in one year).
   (d) All; psychology and calculus most.

3. **Plan where scored evidence comes from, inside the unit's days.**
   (a) Scopes reserved first-teaching or Fluency-day products as end-of-unit evidence; units then could not score them
   (no feedback, no revision) and the calendar fix fell to the lead. End days asked for two or three full performances
   in one period.
   (b) Lead rulings algebra-i 02 and 05, math-grade-8 06, math-grade-3 01, math-grade-7 05 and 08; 17 rejection rows on
   first-teaching scoring, 23 on same-period scoring (4 overruled, rule clarified dcb2f4a6); sample-read repeated kind 3
   (4 units); probe K2 (26 cases); sequence-biology finding 2 and sequence-physics finding 2 (end days overloaded).
   (c) Per unit, name the end-of-unit evidence form: a sitting with unseen items, or a product with a draft day,
   written feedback and a revision before the score, all counted in the unit's days (Days by load). A unit owning three
   or more performance expectations or a long product budgets its end days. Scored work never comes from the day a
   topic is first taught.
   (d) All; psychology (research proposal), statistics (the investigation), environmental science (field project).

4. **Course-level checks claim only what they sample.**
   (a) Check rows that said "every code" or relisted recent end-of-unit codes led to overclaiming check days and
   re-collected records.
   (b) sequence-algebra-i 3, -geometry 1, -algebra-ii 1, -biology 3, -chemistry 2, -physics 3 (all REPEAT yes from the
   K to 8 reads); later.csv L28.
   (c) "What it checks" names the units sampled, the task forms, the direct fluency station (math) and which recent
   unit records are reused unscored; a check right after a unit's end draws that unit's items from earlier units.
   (d) All.

5. **Every minute fits the period, set-up, clean-up and collection included.**
   (a) Plans and days.csv put 52 to 55 minutes in a 50-minute period, forgot clean-up and paper collection, used a
   15-minute readiness block, or folded a day that held revision time.
   (b) Lead rulings math-grade-8 04 (55 in 50), science-grade-8 05 and 06 (15 against the settled 10 readiness minutes),
   math-grade-2 06 and 07, math-grade-7 05, science-grade-6 03; lens: 19 over-time findings (biology s08 collection,
   chemistry s11 clean-up, biology s02 and s07 fold-in days).
   (c) The Days bullet says the 50 minutes hold set-up, clean-up and collection; lab and field days name their
   clean-up minutes; readiness is ten minutes; Shorter path fold-ins never take a feedback or revision day.
   (d) Science most; all.

6. **Name the safety guidance and put each unit's hazards in the frame.**
   (a) Frames said "published school science safety guidance"; unit writers then cited student sign-off forms, and
   days.csv safety cells said `none` or lacked supplies. sequence-write tells scope writers to use "the words of the
   frame's safety column", but the Units table has no such column.
   (b) 30 lens findings citing a student acknowledgment or conduct form as guidance (biology, chemistry, physics, grade 6
   to 8 science); sample-read kind 7 (findings 21, 25); lead rulings science-grade-8 06 (hazard `none` despite controls),
   science-grade-2 05 (no supplies or precautions); sample-read 26 (a frame demonstration silently dropped);
   sequence-biology 4 (frame option with no safety cell). The earth and space and environmental drafts repeat the
   generic wording.
   (c) The Safety read bullet names the guides by title with free links (a state or professional laboratory, field
   work and field trip guide), never a student form. The last Units column gives each hands-on or field unit's hazards
   and controls in the words days.csv will copy; any teacher demonstration is one the safety read would pass.
   (d) Earth and space, environmental science.

7. **Give high school units a cost line and quantities.**
   (a) Cory's cost figures cover K to 5 only (DESK 2026-11-14 card q-frames-ela-sci-math-1, item 4); high school scopes
   deferred costs and units got quantities wrong.
   (b) sequence-biology-codex 3, -physics-codex 3, -chemistry-codex 3 ("all ten unit costs deferred"); 21 lens cost
   findings; chemistry s03 and s04 tray and bag counts; sample-read 23.
   (c) A provisional cost per unit for a class of 30 (consumables, reusable items counted once, printing), with the
   ceiling under "For the lead" (a money question for Cory).
   (d) Earth and space, environmental science; statistics (printing, dice and cards).

8. **State the device assumption and the technology parts of standards.**
   (a) Paper paths were written, but not how many devices a class has; a one-device route left a standard's
   "using technology" part unfinished for most students.
   (b) codex-write-lens-sequence-algebra-ii-s05 finding 1 (F-BF.B.3); ELA 2, 10, 11 device schedules; 35 lens findings
   on devices or technology. The three elective math drafts give paper paths, not a device count.
   (c) One line: devices per student (class set, pairs, one shared), which owned codes require technology and how a
   paper-path student meets them in full; tools by generic name only.
   (d) Math (statistics, precalculus, calculus); environmental science.

9. **Real data named with its source, or labelled invented.**
   (a) Units supplied data tables with no provenance, or constructed values presented as measured.
   (b) 71 lens findings on unsourced or unlabelled data (physics s01, s03, s08, s10; chemistry s01, s02, s09; algebra-ii
   s01, s04, s07; algebra-i s06; math grade 8).
   (c) Per unit, the data sets by name with a free source (agency page, archive), or "invented for practice"; no
   constructed value passed as a measurement. Psychology: a study's results come from the study itself, verified.
   (d) Statistics, earth and space, environmental science, psychology.

10. **Fact-check anchors and picks in the frame, with a date where they can change.**
    (a) Frame anchors carried wrong mechanisms or dated figures into the skeleton, and unit writers had to correct them.
    (b) sequence-biology 4 (LAYER frame: root growth is not feedback), sequence-physics 4 (heavy elements overstated),
    codex-write-biology-s10 (cod anchor corrected), -chemistry-s09 (dated ice comparison), -science-grade-3-s05
    (Svalbard anchor corrected).
    (c) Each anchor, case and named figure carries its source; anything that can change gets "as of" wording.
    (d) Science; psychology (classic studies with later replication problems).

11. **State depth limits per unit.**
    (a) Where frames stated limits ("without band theory", "qualitative carbon transfers"), unit writers cited them
    and stayed in bounds; plan-codex-science and plan-codex-math say there is no other rule for high school depth.
    (b) Over 30 "followed the frame's depth" lines in codex-write-biology, -chemistry, -physics s01 to s11; plan-codex-math
    "Open for the lead" (no unit-level high school rigor rule).
    (c) "What students learn" names what is out (a proof method, (+) parts left out, a mechanism kept qualitative).
    (d) All; precalculus and calculus most (the precalculus draft names no boundary).

12. **One focus method for high school math, with its counting rule.**
    (a) With no stated unit rule, writers computed "prerequisite shares" from 33.7 to 97.5 percent, each counting
    differently (repairs excluded or not, applications counted or not).
    (b) sequence-geometry-codex 4, -algebra-ii-codex 4 (focus calculation missing); codex-write-algebra-ii and
    -geometry s01 to s08 "For the lead" lines; later.csv L49 open.
    (c) Which RUBRIC-MATH-HS rows apply (L49), what stands in for focus in a (+)-only course, whether a unit reports a
    share, and exactly what counts.
    (d) Math.

13. **Owned, begun and revisited codes, labelled one way.**
    (a) Mixed labels led writers to rewrite ownership and contribution lines, and begun codes went unchecked.
    (b) sequence-algebra-i 2 (begun codes never on a check) and 7, -geometry 4, -algebra-ii 5 (tilde codes); unit
    writers corrected ownership labels in codex-write-algebra-i-s02, algebra-ii-s03, s04, s06, s07.
    (c) Owned codes in Owned standards; a begun code named in What students learn with its later owner; a revisit
    named as review in the text; the course that finishes a code checks it.
    (d) Math; psychology where one APA target recurs across units.

14. **Literacy standards claimed in full need days and checks.**
    (a) Courses claimed WHST and RST "also met", then taught a lettered part once and never scored it.
    (b) codex-write-lens-sequence-physics-s05 finding 2 (WHST.11-12.2a to e on one day), sequence-physics-codex 2 (the
    mathematical communication part), sample-read 20 (biology s03 RST.9-10.3 unchecked, writing scored before its model).
    (c) Either name the units that teach and check each lettered part, or say "practised, not owned".
    (d) Psychology, earth and space, environmental science; statistics.

15. **Name each unit's tools so the tool asks exist before units.**
    (a) Units named simulations with no day, job or TOOL-ASKS entry; one days.csv carried a product name.
    (b) Lead rulings chemistry 10 (no TOOL-ASKS entry) and physics 06 (product name); lens physics s01, s02; writers
    reporting TOOL-ASKS.md and DEFAULTS.md "unavailable" (biology, physics).
    (c) Per unit, each key tool by generic name, its job and its paper path; the scope writes TOOL-ASKS.md from it.
    (d) Science, statistics, calculus.

16. **Textbook base texts: say how sections become days.**
    (a) All six bases are textbooks placed by section, not lesson. Below the frame, "keep" lessons were turned into
    tests, goals were close paraphrases, layouts differed, and a dense text was given too few reading minutes.
    (b) 11 lens findings of a kept base lesson turned into a test or changed (algebra-ii s05, algebra-i s01 and s06,
    geometry s06, ELA 2 s04); sequence-algebra-ii 3 (paraphrased goal); sequence-algebra-i 6 and -geometry 3
    (source-map layout); lead ruling algebra-i 03 (source map wrong about the base); sample-read 35 (reading rate).
    (c) The Source map says a section is not a lesson (days are ours, adapted, credited once a day); check days are
    `ours`, never a kept section; goals are in our words; students read our adapted text, with a words-a-day load at
    the course's reading level, unless the frame says otherwise.
    (d) All six.

17. **List what Curio Class must write before units can run.**
    (a) Units planned around unwritten texts and evidence packs and could not finish.
    (b) later.csv L58; sample-read kind 6 (3 units); writer reports "evidence packs, count tables, simulation remain to
    be made" (codex-write-biology, -physics).
    (c) Per unit, what we write ourselves (case studies, readings, data cards, maps), so one writing step is planned.
    (d) Psychology, earth and space, environmental science, statistics.

18. **Sensitivity lists match each unit's days.**
    (a) Reads left out a community the days needed, or cited sources unrelated to the unit.
    (b) Probe K10 (4 units), sample-read 19 (biology s03).
    (c) Each flagged unit names its communities and their own sources; for psychology, by unit (mental illness and
    getting help, disability, the history of intelligence testing).
    (d) Psychology most; environmental science (communities near pollution and dams).

19. **Grade 12 may end early.**
    (a) US History II's frame planned around seniors leaving early; electives in grade 12 have the same calendar.
    (b) docs/courses/us-history-ii/frame.md "Senior calendar"; sequence-us-history-ii-2026-11-14.md (short senior year).
    (c) Say whether the last weeks hold teaching, where the year-end check sits, and which days fold if seniors leave.
    (d) All six.

20. **Lean only on core courses.**
    (a) Same-year leans need an "if later" line; an elective cannot assume another elective is taken.
    (b) sequence-physics "Across the band" 5 (math leans needed one rule, now sequence-write rule 2); psychology draft
    leans on "Algebra I and II statistics" (core, fine).
    (c) Cross-subject leans name core courses only; a lean on another elective is a bridge the unit teaches.
    (d) All.

## Already covered by frame-write.md

- Respond day after each check (lesson 1); minutes and lessons a week (3); standards in full (4); readiness timing,
  unit 1 on day 1 after the hook (16); sensitivity reads line (12); no math ahead of math (13); paper path bullet (14);
  stale status lines (15); "Candidate:" cells (2); days by load (9). Each held below the frame; item 2 above adds only
  the evidence and counting-grade part.
- Mid-unit assessment in units over 25 days: in the Days bullet wording.
- Year-end direct fluency station: sequence-write rule 2; the three elective math drafts already carry "Fluency without
  a timer" bullets.
- Collect once, class size 30, "Our words" for days.csv: sequence-write rule 2 (lesson 16 above extends "Our words" to
  the frame's Source map).
- A pilot course per new subject, gated layouts, rule 2 count at scope stage: PRODUCTION-PATH "Before a new subject's
  scopes"; not frame text.
- Same-period scoring and error-letter rules: UNIT-PLAN fields 5 and 6 and the lens brief; not frame matters.

## Brief gaps (proposed lessons 17 to 27 for frame-write.md)

17. **Day kinds defined.** A "Day kinds" bullet: first explicit teaching is Understanding; Fluency practises only what
    an earlier day taught; investigating, drafting, editing or a new task is Application. Say what Fluency means in
    this course.
18. **Readiness evidence, not verdicts.** Each assumed row gives its last-use grade and core day; the treatment follows
    the count, which the scope gate governs. No "kept in use" without a day. A course open to two grades names the
    grade the count starts from.
19. **Scored evidence placed.** Each unit names its end-of-unit evidence form; a product's draft, feedback and revision
    days are counted in the unit's days; no score from a first-teaching day; end days hold one full performance each.
20. **Checks claim samples.** "What it checks" names the units sampled, the task forms and any record reused unscored,
    never "every code".
21. **Inside the period.** Set-up, clean-up and collection fit the lesson's minutes; readiness is ten minutes.
22. **Safety named.** The Safety read bullet names guides by title and free link (never a student form); the last
    Units column gives each hands-on or field unit's hazards and controls, in the words days.csv will use.
23. **Facts sourced.** Anchors, cases, figures and data sets carry a free source, an "as of" date where they can change,
    or "invented for practice".
24. **Depth and devices.** "What students learn" names what is out; a Devices line gives devices per student and how a
    paper-path student meets each "using technology" part.
25. **Tools and what we write.** Per unit: key tools by generic name with their job; texts, data cards and cases
    Curio Class writes itself.
26. **Literacy standards.** Claimed in full only with the units that teach and check each lettered part; otherwise
    "practised, not owned".
27. **Textbook source maps.** A section is not a lesson; check days are `ours`; goals in our words; a reading load a day.

Also small: the Days bullet must say "lessons a week" (frame.py's per_week parse misses "meetings",
structure-pass-science-2026-11-15.md "For the lead"); sequence-write's "frame's safety column" should point to the
last Units column (or the frame gains the column).
