# Expert cold read: scope and sequence of Music, grades 9 to 12 (2026-11-26)

Job: docs/pipeline/briefs/sequence-read.md, course `music-grades-9-to-12`, subject arts (lens docs/agents/lenses/arts.md;
bar: docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts", items 1 to 9 and "Fails if", with docs/courses/arts/STANDARD.md
and docs/courses/arts/APPROACH.md), with the arts additions in build/scope-writes/ARTS-READ.md and the writer's brief
build/scope-writes/ARTS-BRIEF.md. The scope was written by a fresh agent; read cold.

## What I read

- docs/courses/music-grades-9-to-12/scope-and-sequence.md (all) and data/plans/music-grades-9-to-12/days.csv (all 640
  rows: kind, assess, goal, codes, school_day and retrieves for every row; the notes of every day named below; the
  "Short path" clause of every note, parsed and grouped by script).
- docs/courses/music-grades-9-to-12/frame.md (all: the course in brief, Seams, Models carried, Units table, Course-level
  checks, Cross-subject, For the lead).
- The mu-g8 to mu-g12 rows of data/progressions/arts.csv; the 21 Level 1 lines (and the Level 2 and 3 lines named
  below) of data/standards/ncas-performance-standards-words.txt.
- docs/courses/CALENDAR.md (the words, rule 4 and the 9 to 12 rows), data/plans/calendar.csv for this course,
  STANDARD.md 3.2 to 3.4, APPROACH.md (kinds of day, readiness and the baseline look, scoring, critique, what is
  carried, high school levels), UNIT-PLAN.md rule 6, docs/agents/EXPERT.md, the arts lens.
- Earlier reads, for repeat tags: docs/reviews/sequence-music-grades-6-to-8-2026-11-26.md and the other arts sequence
  reads of 2026-11-26 (music K to 2 and 3 to 5, dance, media arts, theater, visual arts); no earlier read of this
  course's scope exists.
- Gates: `scripts/sequence.py check music-grades-9-to-12`: 0 failures (notes only: units 1, 6, 11 and 16 to 19 own
  no standard). `scripts/plan.py check`: this course 0 failures (failures printed belong to other courses).
  `scripts/frame.py calendar`: prints no 9 to 12 rows and no break. `scripts/stale.py check`: 0 failures.
- By script, beyond the gates: every code on every day sits in its own level (no `.II` code in Level 1 and so on);
  every owned code of every thread unit is on an `end` day except Pr5.1.C.Ia, IIa and IIIa (finding 5); every
  retrieval sits on a unit's day 2 or 3 except units 6 and 11 (finding 10); every readiness check sits in the last
  ten minutes of the day before the unit.
- No outside source was fetched. Nothing here rests on memory of the national text except where a finding says so.
- EXPERT.md asks for each finding to be logged with `scripts/plan.py defect`; this job's brief says to edit no file
  but this report, so the caller logs them.

## Verdict

The scope and sequence is sound in its structure: each level carries only its own 21 ids, every owned code is taught
and assessed in its level, every thread unit runs studies, technique on step cards, drafting with one critique, a
revision, a showing and a respond day, the works range across regions, periods and living composers with every
frame-flagged work carrying its sensitivity note, and the course-level checks sit on weeks 16 and 32 and do not repeat
the unit just assessed. The biggest risk is the 80-day short path: the .md says days merge in pairs, but the rows
merge up to eight days into one 45-minute period, with three to five teaching days (four technique step cards on one
day; three sensitive works in one day) compressed together, which cannot be taught as written. The one change that
matters most is finding 1 (a cap on what one short day holds, paid for by dropping the mid-unit check on short-path
units, which are under 25 days); the through-composed technique gap in unit 13 (finding 2) is next.

## Findings, most serious first

### 1. The 80-day short path merges up to eight days into one period, against its own "pairs" rule

- **LAYER** sequence. **REPEAT** yes (same kind as sequence-music-grades-6-to-8-2026-11-26.md finding 5: a merged
  path with no minute budget).
- **What is wrong.** The .md says "Days merge in pairs, Fluency days first". The notes do otherwise. Grouping every
  row by its "Short path: day N of 80" clause: each level keeps 50 to 53 days single (checks, respond days, critique
  and revision days, showings) and so packs the other 107 to 110 days into 27 to 30 short days, 3.7 a day on
  average. 35 short days hold four course days, 25 hold five, 4 hold six, one holds seven (Level 3 days 453 to 459)
  and one eight (Level 4 days 537 to 544: the hook, three Understanding days and four review-writing days). 28 short
  days hold three or more Understanding days, for example:
  - Level 2 short day 44: days 252 to 256, and Level 2 short day 22 (203 to 207); Level 3 days 372 to 376 sit in
    two short days but day 373 to 375 are three technique step cards (modulation, theme and variations,
    counterpoint) on one;
  - Level 2 days 213 to 216: four technique step cards (the four cadences, two-voice writing, a varied return, the
    Roman numeral drill) on one 45-minute short day;
  - Level 1 short day 41: days 81 to 85, the hook plus the Bonds, Ballard and Shaw studies, the two flagged works
    (civil rights history; Quapaw and Cherokee heritage) each left with minutes.
  The frame's short path promises each unit keeps "the technique taught with its step card", and APPROACH "What is
  carried" asks a technique be shown, carried with the card, then withdrawn; four of them in one period is none of
  those. Sensitivity notes ask for setting taught plainly; that needs time.
- **Why it matters.** A school on a semester schedule is exactly the user the short path exists for (STANDARD.md
  3.2). A unit plan writer will either build impossible days or quietly drop teaching, and the fault reads as a
  thin course to an adoption reviewer (bar item 2, technique taught in steps; item 9, pacing fits real schedules).
- **Fix.** Three changes, applied by the writer:
  1. On the short path every thread unit is 10 to 22 days (unit 16 is 28), so sequence-write's mid-unit rule (units
     over 25 days) does not ask for a mid-unit check there, and the frame's short-path keep list does not name one.
     On the short path drop the mid-unit check day and its mid-unit respond day in every unit but unit 16 (keep one
     there): the product is handed in at the end of the making day it finishes on and scored after the session as
     the unit's baseline mark. This frees 10 short days in Levels 1 to 3 and 10 in Level 4 (units 17 to 19's mid and
     respond days, keeping unit 16's first).
  2. With those days, a short day holds at most three Understanding or Application days, at most two of them
     Understanding, never two technique step cards, and never two works that carry a sensitivity note; Fluency drills
     merge without limit because they fold into the opener (the frame's rule). The counts allow it: Levels 1 to 4
     carry 73, 74, 75 and 75 Understanding or Application days in merged groups, about 1.9 a short day once the
     freed days are added.
  3. Rewrite the .md sentence to the real rule ("Fluency days fold into openers; a short day holds at most three
     teaching or making days, at most two of them Understanding, never two step cards or two flagged works; checks,
     respond days, critique and revision days and readiness days stand alone; the mid-unit check is dropped on
     short-path units under 25 days"), and re-run the notes' merge clauses by script.
  Confidence: firm (the counts are from days.csv; the frame and APPROACH state the promises being broken).

### 2. Unit 13 drafts a through-composed study with no technique day for it

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** Day 378: "Draft 2, dated: a through-composed study of the same ideas." The technique days before
  it are 372 (seventh chords and secondary dominants), 373 (modulation), 374 (theme and variations) and 375
  (counterpoint). Through-composed form is in the frame's Level 3 technique list and in MU:Cr2.1.C.IIIb's row, and it
  is scored on day 397 ("growth analyzed draft by draft in both forms"), but no day shows it in steps.
- **Why it matters.** APPROACH "What is carried": a technique is never first met in independent work. The bar's
  "Fails if" names making with no technique taught. Half of the unit's creating evidence rests on a form never taught.
- **Fix.** Day 376 becomes Understanding: "Technique in named steps with the step card: through-composed form (an idea
  carried forward without a return), shown on a passage of the Pathétique development or Ba Ban." The seventh-chord
  drill of day 376 moves into day 377's opener. Settled below. Confidence: firm.

### 3. Unit 17 has no performing day, and the .md says so

- **LAYER** sequence (and frame, the unit's process line). **REPEAT** new.
- **What is wrong.** The unit's process line reads "perform none". ARTS-READ asks for all four processes in every
  unit, and ARTS-BRIEF told the writer the same ("The four processes ... appear in every unit's days"). The frame's
  Units row says "Responding applied again", which allowed it; the brief is stricter.
- **Why it matters.** A review that cites a passage is stronger when the reviewer can sing or play it, and the
  check-set line will fail it as written.
- **Fix (no day added).** Day 547: the reviewer sings or plays one line from the peer's score before writing.
  Day 552: each reviewer performs (sings, plays, or plays back from the score card) the two passages the review cites
  as evidence while the reader follows. Mark both "performing practiced, not claimed" and change the .md process line
  to "perform 547, 552". Settled below. Confidence: likely.

### 4. Ten-days-short fold-ins drop five baseline marks and squeeze four into check days

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** The fold-in list promises "nothing assessed". Five fold-in days carry the unit's baseline look
  (APPROACH "Growth": the first of each student's two marks a unit): 84 and 120 (Level 1), 244 and 280 (Level 2), 404
  (Level 3). Four fold-in days move their drill "into the next day's opener" when the next day is a check day whose
  45 minutes are already spent (set-up 3, self-check 5, sitting 35, collecting 2) or a showing day that "holds only
  the showing": 151 (next 152), 307 (next 308), 311 (next 312), 467 (next 468).
- **Why it matters.** A school ten days short loses the growth mark in five units, and four drills land nowhere.
- **Fix.** Swap, keeping ten a level and every swap after the mid-year check: Level 1: 84 to 91, 120 to 125, 151 to
  113. Level 2: 244 to 251, 280 to 285, 307 to 267, 311 to 295. Level 3: 404 to 410, 467 to 451. Level 4 unchanged.
  Each replacement is a Fluency day with no baseline, whose next day is a teaching or making day and is not itself
  folded. Settled below. Confidence: firm.

### 5. Pr5.1.C.Ia, IIa and IIIa are missing from the end-of-unit lists of units 5, 10 and 15

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** The frame's end-of-unit evidence for these three units scores the rehearsal plan id ("a look-for
  on the kept rehearsal plan"). In days.csv the code sits only on the mid-unit check (128, 288, 448) and on teaching
  days; the end days' codes omit it, and the .md "End of unit" lines for units 5, 10 and 15 omit it. Only the notes
  of days 149, 309 and 470 say "the rehearsal plan look-for (MU:Pr5.1.C.Ia) is scored from the kept plan".
- **Why it matters.** sequence-read: the end-of-unit assessment covers every part of every standard the unit
  teaches. A unit plan writer working from the .md list builds an end-of-unit guide without the plan.
- **Fix.** Add MU:Pr5.1.C.Ia to day 149's codes, MU:Pr5.1.C.IIa to day 309's, MU:Pr5.1.C.IIIa to day 470's, and the
  same code to the matching day in each .md "End of unit" line. Settled below. Confidence: firm.

### 6. The senior fold rule names one level and folds days the frame protects

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** The frame: a level taken in grade 12 (any level; mixed grades are expected) folds "the concert
  unit's last fluency days (up to five)". The .md names only "Level 4 days 632 to 638", seven days, one of them an
  Application day (634, the final composer's statement, a portfolio entry).
- **Why it matters.** A senior in Level 1, 2 or 3 has no rule, and a Level 4 senior loses a making day.
- **Fix.** "For a senior whose school ends early, these fold first: Level 1 days 154 to 158; Level 2 days 314 to 318;
  Level 3 days 475 to 478 (then 472); Level 4 days 632, 633, 635, 636 and 637. The year-end check and its respond day
  move to the senior's last two days." Settled below. Confidence: firm.

### 7. Retrieval and reteach minutes are not written anywhere

- **LAYER** sequence. **REPEAT** yes (sequence-music-grades-6-to-8-2026-11-26.md finding 3).
- **What is wrong.** The `retrieves` column names rows on each unit's day 2 (and some day 3s), but no note says what
  the retrieval task is, how long it takes, or where the reteach goes. The frame says a student placed into Level 2
  or 3 "meets the same retrieval tasks, each carrying its ten-minute reteach"; day 2 of units 7, 12 and 16 carries two
  or three rows on a day that also teaches a study (Sensemayá, Lichtbogen, the proposal). In Level 1, each readiness
  note says "with the ten-minute reteach" inside the ten readiness minutes; UNIT-PLAN rule 6 puts a reteach in the
  next day's warm-up, which here is the next unit's hook day.
- **Why it matters.** A writer builds a 45-minute day 2 with 20 to 30 minutes of opener, or drops the reteach that a
  placed student needs most.
- **Fix.** Every unit's retrieval day note: "Opener (10 minutes): retrieval of <row> and <row>, five minutes each;
  any reteach (ten minutes per row missed) takes the next day's warm-up and first five minutes, whole class if more
  than a third missed, otherwise a small group (UNIT-PLAN rule 6)." Level 1 readiness notes (days 12, 48, 80, 116):
  "the reteach takes the warm-up of the unit's day 2, before its study, the hook day staying clean". Confidence: firm.

### 8. Unit 14's mid-unit assessment is not the frame's

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** The frame's unit 14 row: "Mid-unit assessment: the defended reading, near day 418." Day 417 scores
  the expression map instead (the unit 4 and 9 pattern), and the .md does not say why. MU:Re8.1.C.IIIa, defending a
  reading against another, is the new Level 3 skill; as written its first scored try is the end sitting (435).
- **Fix.** Day 417: "Mid-unit assessment: the defended reading (day 406's interpretation, defended against another
  reading), handed in and scored on the guide", codes MU:Re8.1.C.IIIa; day 418 acts on it. The expression map stays
  scored at the end (434). Settled below. Confidence: likely.

### 9. Four candidate cells are settled under the wrong name

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** The frame's candidates: unit 5 "a Native American or Asian performance for the critique
  sitting"; unit 7 "an African or Asian text setting"; unit 10 "a Native American or African performance for the
  critique sitting"; unit 15 "a Native American or Asian performer's recording for the critique sitting". The .md
  settles "a further concert work" (5, 10, 15) and "a further model work" (7).
- **Why it matters.** The cells are settled in name only; a later reader cannot tell the frame's ask was weighed.
- **Fix.** Name each frame candidate. The drop reason the .md gives for 5, 10 and 15 holds once named: the sitting's
  unseen performance must be public domain, openly licensed or a Curio Class original, and a Native American
  recording with that status and no ceremonial use is not in hand; keep it as a unit plan option, no day. Unit 7:
  dropped, Level 2 already has Egypt and China and Hindustani rhythm (units 9 and 10). Confidence: firm.

### 10. Units 6 and 11 put retrieval on their hook day

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** Days 161 and 321 (unit day 1, the hook) carry `retrieves` (mu-g9-invent and mu-g9-choose;
  mu-g10-invent and mu-g10-choose). The .md says day 1 of every unit stays clean.
- **Fix.** Clear the two cells and add those rows to days 162 and 322, whose retrieval drills already cover the level.
  Settled below. Confidence: firm.

### 11. "For the lead" 3 is stale

- **LAYER** process. **REPEAT** yes (the frame's For the lead 6 repeated the pilot's item).
- **What is wrong.** It says ADOPTION-BAR-SUBJECTS.md's arts row "still lists the standards gate and the 63 strand ids
  as owed". The row now reads "NCAS id-membership checking (later.csv L83) and the 63 high school music composition
  and theory strand ids were completed 2026-11-21."
- **Fix.** Delete item 3 from the scope's For the lead; the lead closes frame For the lead 6. Confidence: firm.

### 12. Small text and layout faults

- **LAYER** sequence (CALENDAR item: process). **REPEAT** new.
- Day 459 goal: "how its expressive aim carry the aim" reads "how the music's expressive aim comes across"
  (MU:Pr6.1.C.IIIa's line).
- Day 242: "beside the composer's own words" for Umm Kulthum, the singer (the frame names Mohammed Abdel Wahab as
  composer): "beside the singer's and composer's published words or a scholar's page".
- Day 452 asks for a "three-level feedback trail"; a student placed into Level 3 has none from Levels 1 and 2: add
  "a placed student uses the Level 3 trail and the placement record".
- ARTS-READ asks each year's part to name its standards: add one line under each "## Level n" heading ("Carries the
  NCAS composition and theory .Ia to .Ic ids, 21"), and make the unit headings "###" so levels and units are not one
  level.
- CALENDAR.md's generated table cuts the check labels at 24 characters ("Level 1 mid-year (week 1 week 16"), which
  reads as week 1; the weeks themselves (16 and 32) are right. The lead fixes the render in `frame.py sync`.

## What is right and should not be touched

- Each level claims its own 21 ids and Level 4 claims none, scored again on the .III ids against Level 3's bar; the
  .md states it once (bar "Scope and sequence states").
- The thread-unit shape repeats one level harder in the same slot, so every thread returns at a new depth; techniques
  get harder level to level as the frame lists.
- Every thread unit studies three or four works with setting before making, has one critique day and a revision day
  before its end-of-unit evidence, and a showing; the concert units' showings fall in week 30.
- Works across the band: Africa, Asia, Europe and the Americas, Native American composers in Levels 1 and 3, living
  composers every level; every frame-flagged work carries its sensitivity note on its study day (51, 82, 83, 168, 195,
  204, 242, 331, 365, 402, 403), with listening only where the frame asks.
- Course-level checks on school days 79 and 80 and 159 and 160 every level, each sampling earlier units, never the
  unit just assessed, and saying so in the goal (days 79, 159).
- Readiness checks sit in the last ten minutes of the day before each Level 1 unit (12, 48, 80, 116), and Level 2 to 4
  retrieval sits on day 2 or 3.
- Recording consent, no forced solo, hearing and voice safety, and the device-free path are in every relevant note.

## What I could not judge

- Whether the listed works' rights lines hold; that is the unit plan's check on each item's page (the .md's For the
  lead 6 says so).
- Instrument and voice pedagogy at depth (the lens's own limit): whether two-voice counterpoint and secondary
  dominants fit a 45-minute class with no instrument is a music teacher's call.

## Sources

- No outside source was opened for this read. The findings rest on the repository's own files: the frame, STANDARD.md
  3.2 to 3.4, APPROACH.md, UNIT-PLAN.md rule 6, the words file and days.csv, as cited in each finding.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 376 becomes Understanding: through-composed form in steps with the step card; its seventh-chord drill moves into day 377's opener | the form is drafted on day 378 and scored on day 397 with no technique day | data/plans/music-grades-9-to-12/days.csv |
| Days 547 and 552 add performing (a line of the peer's score; the two cited passages), practiced, not claimed; .md process line "perform 547, 552" | unit 17 needs all four processes | days.csv, scope-and-sequence.md |
| Ten-days-short swaps: 84 to 91, 120 to 125, 151 to 113, 244 to 251, 280 to 285, 307 to 267, 311 to 295, 404 to 410, 467 to 451 | keep baseline marks; no drill folded into a check or showing day | scope-and-sequence.md (Shorter path), days.csv notes |
| Add MU:Pr5.1.C.Ia to day 149, MU:Pr5.1.C.IIa to day 309, MU:Pr5.1.C.IIIa to day 470, and to the .md End-of-unit lines | the plan id is scored at the end but not listed | days.csv, scope-and-sequence.md |
| Senior fold days per level: 154 to 158; 314 to 318; 475 to 478 (then 472); 632, 633, 635, 636, 637 | frame rule applies to any level; fluency only, up to five | scope-and-sequence.md |
| Day 417 scores the defended reading (MU:Re8.1.C.IIIa); day 418 acts on it | follows the frame; the new Level 3 skill gets a mid-unit try | days.csv, scope-and-sequence.md |
| Move the retrieves of days 161 and 321 to days 162 and 322 | hook days stay clean | days.csv |
| Day 459 and day 242 goal wording; day 452 placed-student option | text faults | days.csv |

## For Cory

- Nothing new. The supplies ceiling (frame For the lead 7: a pick of $40 a class a level against provisional costs of
  $20 to $35) still waits on the Desk.
