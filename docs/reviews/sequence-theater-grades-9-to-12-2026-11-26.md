# Expert read: scope and sequence of Theater, grades 9 to 12 (2026-11-26)

Course `theater-grades-9-to-12`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), as
docs/pipeline/briefs/sequence-read.md and build/scope-writes/ARTS-READ.md ask. A fresh agent wrote the scope. I did
not write it.

## What I read

- The scope and sequence (docs/courses/theater-grades-9-to-12/scope-and-sequence.md, whole) and all 640 rows of
  data/plans/theater-grades-9-to-12/days.csv, read cold, with my own scripts over the CSV (codes by level, codes
  taught before use, codes on assessed days, short-path merge map, fold-in and senior-fold days, baseline looks,
  retrieval column).
- Beside them: the frame (docs/courses/theater-grades-9-to-12/frame.md, whole), the theater rows th-g8 to th-g12 of
  data/progressions/arts.csv, the theater lines of data/standards/ncas-performance-standards-words.txt for every id
  sampled on a check, docs/courses/CALENDAR.md (rule 4 and the 9-12 table) and the course's rows of
  data/plans/calendar.csv.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md section 2 (items 1 to 9 and "Fails if"), docs/courses/arts/STANDARD.md (3.2,
  3.4), docs/courses/arts/APPROACH.md (kinds of day, growth, scoring), the lens docs/agents/lenses/arts.md,
  docs/agents/EXPERT.md, the writer's brief build/scope-writes/ARTS-BRIEF.md and docs/pipeline/briefs/sequence-write.md
  (rule 2 and the check-form line).
- Earlier reads: the other arts sequence reads of 2026-11-26 in docs/reviews/ (headings only, to tag REPEAT). No
  earlier read of this course exists.
- Gates, run first: `plan.py check` has no failure for this course; `frame.py calendar` reports none;
  `sequence.py check theater-grades-9-to-12` 0 failures (its "standard None" notes are the three opening units and
  Level 4, which own no id, as the frame sets); `stale.py check` 121 files, 0 failures. My scripts confirmed: each of
  Levels 1 to 3 carries exactly its 24 ids, no id sits in the wrong level, every id is on a teaching day before its
  first assessed day and on a mid or end day of its own unit, and every Application, Fluency and Check day uses only
  codes an earlier Understanding day of the same unit taught.
- No outside source was opened for this read; what rests on judgment says so.

## Verdict

The scope is sound where it matters most: all 72 owned ids sit on days of the right level, every paired unit teaches
technique before the making, runs a critique and a revision before a two-day end-of-unit assessment that covers every
owned id, the works range across five continents with living makers each level, and the readiness and retrieval plan
follows the progression's one-level-back chain. The biggest risks are the 80-day short path, whose merge map piles up
to six days (including a second technique's first teaching) onto one 45-minute kept day while merging revision and
feedback sessions the frame protects, and Level 4, which never says whose production unit 20 stages: thirty
student-designed productions or one show. The one change that matters most is a merge rule (no kept day takes more
than two merged days, a first-taught technique pairs only with a kept teaching day that takes nothing else, no
revision or feedback session merges) and one line under Level 4 that sets the company model.

Finding count: 12 (2 serious, 5 moderate, 5 minor).

## Findings, most serious first

### 1. The 80-day merge map overloads kept days and merges days the frame protects (serious)

LAYER sequence. REPEAT yes (the same kind as the music and visual arts reads of 2026-11-26: once-a-week or short-path
merges piled onto one session).

**What is wrong.** The day counts (17 of 34 or 35 days in a paired unit) are the frame's and stand. The map that
says which day takes which is the writer's, and it is uneven:
- Kept days taking five or six other days: 52 (49, 54, 55, 56, 58, 59), 187 (186, 188, 189, 191, 193, 194), 207 (204,
  209, 210, 211, 213), 259 (258, 260, 261, 263, 265, 266), 347 (346, 348, 349, 351, 353, 354), 367 (364, 369, 370, 371,
  373), 419 (418, 420, 421, 423, 425, 426), 482, 520, 585 (586, 587, 588, 589, 591); about forty more kept days take
  three or four.
- Ten owned ids lose their own first-teaching day and are taught inside another technique's kept day, usually one
  that also takes several rehearsal or work sessions: day 50 (TH:Cr1.1.Ic) into 48, 54 (TH:Cr3.1.Ib) into 52, 86
  (TH:Re9.1.Ib) into 84, 205 (TH:Cr1.1.IIc) and 209 (TH:Cr3.1.IIb) into 203 and 207, 242 (TH:Cr1.1.IIb) into 240, 365
  (TH:Pr5.1.IIIa) and 369 (TH:Cr3.1.IIIb) into 363 and 367, 402 (TH:Pr5.1.IIIb) into 400, 588 (TH:Re8.1.IIIc) into 585.
- The .md says "A fold-in never takes a critique, a feedback, a revision or a respond day", but day 598 ("Revision
  session: the student's own role or concept revised from the critique", the work TH:Re8.1.IIIa is scored on) merges
  into 597, and the Level 4 work sessions that hold the unit's peer feedback round (for example 485, 492, 497, 505,
  523, 530, 563, 568, 572, 610, 616, 620, 627) all merge. Days 165 and 325 (revision and source note) merge too; the
  frame's three-day review path allows that one, so it may stand.
- Two respond days take a work session: 500 into 499 and 538 into 537, so the second try shares its 45 minutes with
  new writing.
- Unit 16 keeps all five reading sessions (507 to 511) but merges every research and writing session (483 to 487,
  489 to 497), so on the short path a student writes a researched play in two kept mini-lesson days (488 and 494).

**Why it matters.** Nothing is cut on paper, but a writer building the 80-day teacher pages from this map would write
days that cannot run: a technique demonstration, a second technique and four rehearsal sessions in 45 minutes.
STANDARD.md 3.2 and the frame promise every id kept on this path; an id taught in ten minutes inside someone else's
day is cut in the room.

**Fix (settled, a day map inside each unit).** Re-map every merge by three rules and write them in the .md's Shorter
path section: (a) a merged Understanding day that first teaches an owned id merges into a kept Understanding day of
the same thread that takes no other day; (b) Application and work-session days merge into the critique day, the
revision day, the final rehearsal day or the next kept Application day, at most two into any one kept day; Fluency
days fold into warm-ups as now; (c) no revision session, no work session that holds the unit's peer feedback round and
no day into a respond day. Check in unit 3 that this fits: first-half Applications 51, 55, 56, 58, 59 go two, two and
one into 60, 61 and 63; 50 into 48 and 54 into 52 with nothing else; second-half 69, 72, 73 into 74, 75 and 77. In
unit 16 keep 489 and 495 and merge 509 and 510 into 508 and 511 (still 19 kept). Merge 500 into 506 and 538 into 544.
In units 16 to 20 merge the "continued" teacher-conference sessions and keep the session with the peer feedback round
(swap 598 to kept and merge 596's partner day, 601, already a fold-in, by the same rule). Confidence: firm on the
counts (my script), likely on what a room can hold.

### 2. Level 4 never says whose production is staged (serious)

LAYER frame and sequence. REPEAT new.

**What is wrong.** Units 16 to 19 are each student's own work: their play (unit 16), their concept (unit 17), a role
"from a public domain play, their own play or a classmate's" (unit 18), their critique (unit 19). Unit 20 asks "How do
I bring my production to the audience I choose", day 606 has "each student name the audience their production is
for", days 607 to 611 build "the full design folio for the student's production", and day 628 brings "the production
to the audience the student chooses". Then day 636's note says "the production runs as one show, each student scored
once on the role they lead". Unit 17's rehearsal showing and unit 18's performed role imply classmates acting in each
other's plays, and days 516, 554 and 581 mention "groups of five", but no line says how the class is organized.

**Why it matters.** Thirty productions cannot run in one 45-minute day (the frame: "an end day holds at most one full
performance"), and one show cannot carry thirty students' own audiences and designs. TH:Pr6.1.IIIa (research from each
creative role, for a chosen audience) and TH:Cr1.1.IIIb (every element designed) are scored per student; a unit-plan
writer cannot build days 606 to 638 until the model is set.

**Fix (for the lead: one line in the frame's Level 4 bullet, then the scope).** Under the Level 4 heading write the
company model once: the class works as companies of about five (six in a class of 30); units 16 to 19 stay each
student's own work, with the company as cast and readers; in unit 20 each company stages one piece built from its
members' plays (about 5 minutes, six pieces on day 636, the frame's showing budget), each student leading one creative
role and its research (TH:Pr6.1.IIIa) and running the element they design in the cued run (TH:Cr3.1.IIIc); each
student's full design folio and its defense (TH:Cr1.1.IIIb, TH:Pr5.1.IIIb, TH:Re9.1.IIIb) are for their own play, on
paper; the company chooses the audience. Then reword days 606, 607, 628 and 636 to match. A small Level 4 class (common
in schools) runs as one company. Confidence: firm that the text contradicts itself; the company model is a judgment
call.

### 3. Baseline looks sit on days that both short paths remove, and Level 4 has none (moderate)

LAYER sequence. REPEAT yes (the dance, music and visual arts reads of 2026-11-26 found baseline looks on fold-ins).

**What is wrong.** APPROACH "Growth" and the frame give every unit a baseline look at the main look-for, so "every
student has two marks a unit". The 21 baseline looks are all on Fluency days. Sixteen of them are also short-year
fold-in days (15, 49, 85, 119, 169, 186, 204, 221, 241, 276, 329, 346, 364, 381, 401, 436), whose note says only that
"its practice moves into the next day's warm-up"; all 21 merge on the 80-day path with no word on where the look
goes. Units 16 to 20 carry no baseline look at all. The logic model in the .md says the two marks are "mid-unit and
end-of-unit", which is not what the frame or APPROACH says.

**Why it matters.** On a short year most units lose the first of the two marks the growth claim rests on; on the
80-day path all do.

**Fix (settled).** Swap each of the 16 fold-ins for a free Fluency day of the same unit half: 15 for 19, 49 for 53,
85 for 89, 119 for 123, 169 for 173, 186 for 190, 204 for 208, 221 for 225, 241 for 245, 276 for 280, 329 for 333, 346
for 350, 364 for 368, 381 for 385, 401 for 405, 436 for 440 (each still a Fluency day with nothing assessed; the
table under "A year about 10 days short" changes to match). On the 80-day path, each baseline day's merge note adds
"the baseline look moves to day n" (the kept day it merges into). Put a baseline look in the first work session of
each Level 4 unit (483, 521, 561, 586, 608), recorded in that day's conferences. Rewrite the logic model's outputs to
"two marks a unit per student on the main look-for (the baseline look and the end-of-unit)". Confidence: firm.

### 4. Course-level check goals ask only part of some ids they sample (moderate)

LAYER sequence. REPEAT yes (the same kind in the dance, music and media arts reads of 2026-11-26).

**What is wrong.** Each check note says "each part of each listed id has its own short prompt", but the goal a writer
builds from drops parts, read against the words file:
- Day 159, TH:Re9.1.Ia (evidence and criteria, linking to other arts, history and culture): "a short critique with
  criteria and purpose" asks no evidence and no link.
- Day 479, TH:Re8.1.IIIa (revise your own work and interpret others'): only "a revision of a given scene"; TH:Re9.1.IIIc
  (compare and debate a tie to current issues): "a researched judgment ... with a current issue" asks no comparison
  and no two sides; TH:Cr2.1.IIIa (analysis, background, research, western and non-western traditions): "two credited
  traditions" does not ask for one of each or for the research.
- Day 397, TH:Cn11.2.IIIa (defend creative choices by critically reading research): "a source judged sound or not"
  asks no choice defended.
- Day 237, TH:Cn11.2.IIb (your own biases): "a bias check on a given research note" can be answered about the note's
  writer, not the student.
- Day 557, TH:Cn10.1.IIIa (personal, local and cultural viewpoints) and TH:Cn11.2.IIIb (using critical research):
  "its viewpoints on the issue" and "social and historical meaning" name neither the three viewpoints nor the research.

**Why it matters.** A check that drops a part marks the id met on half of it.

**Fix (settled, wording inside the standards).** Rewrite the goals: 159 "a short critique of an unseen described scene
with one criterion, one piece of evidence and one link each to another art, history and culture, and its purpose and
intended audience"; 479 "a revision of a given scene from proof and a standard, and an interpretation of a given
classmate's choice with its evidence; an original concept from a given research page drawing one western and one
non-western tradition, each credited; an unseen production's tie to a current issue argued from two sides and
compared"; 397 "one production choice defended by judging a given source sound or not"; 237 "one belief of your own
that could skew how you read the given research note, and how you would test it"; 557 "the play's personal, local and
cultural viewpoints on the issue, and its social and historical meaning defended from one critically read source".
The frame's checks table should match (for the lead). Confidence: firm.

### 5. The senior fold for unit 20 cuts all four folio sessions and two feedback rounds (moderate)

LAYER sequence. REPEAT yes (the music 9 to 12 read of 2026-11-26 found senior folds on protected days).

**What is wrong.** The rule is Fluency days first, then plain work days, never critique, revision or observation.
Unit 20 has only three Fluency days (614, 625, 634), so seven work sessions fold: 608, 609, 610 and 611 (every
session after the folio mini-lesson, so the folio checkpoint on day 621 follows no work time), 613, 615 and 616. Days
610 and 616 hold the peer feedback rounds. Units 5, 10 and 15 fold Fluency days only and are fine.

**Fix (settled).** Unit 20 senior fold days: 609, 611, 614, 615, 618, 619, 625, 626, 630, 634 (the three Fluency days,
then one "continued" session from each run, keeping each run's first session and its peer feedback round). The
unit's work then reads folio 608 and 610, defense 613 and 616, reading 620, tech 624 and 627, run 629 and 631.
Confidence: firm on the conflict, judgment on the pick.

### 6. Rows used earlier the same level are leaned on with no retrieval (moderate)

LAYER sequence. REPEAT yes (the dance, media arts and visual arts reads of 2026-11-26).

**What is wrong.** Rule 2: a row used earlier the same year opens as a retrieval task. Each paired unit's day 2
retrieves only the level-before rows, while the frame's "Why this unit, here" names same-level rows the unit uses:
unit 3 builds the character on unit 2's researched reading (th-g9-story); unit 4's critique uses unit 3's criteria
(th-g9-notice) and its design serves unit 2's or 3's play; unit 8's file uses unit 7's checked research and concept
(th-g10-story, th-g10-imagine); unit 9's critique uses unit 8's standards (th-g10-notice); unit 13's role serves unit
12's concept (th-g11-imagine); unit 14's design serves unit 13's role and unit 12's concept. The production units say
"the unit 4 design skills return" (day 146) and "the unit 9 design skills return" (day 303) with no retrieval.

**Fix (settled).** Add to the `retrieves` column and the note's ten-minute task: 48 th-g9-story; 84 th-g9-notice; 203
th-g10-story; 240 th-g10-notice; 363 th-g11-imagine; 400 th-g11-actor; and a five-minute retrieval of the design
folio at the start of 146 (th-g9-design), 303 (th-g10-design) and the matching tech day of unit 15. Where day 2's ten
minutes now hold two rows, the note splits them five and five. Confidence: firm.

### 7. A student new to the school has no day to sit the placement's written part (moderate)

LAYER sequence. REPEAT new.

**What is wrong.** Units 6 and 11 say "a student new to this level sat the previous level's year-end check as the
written component". A student arriving from another school, or after a gap, was not in the room on day 159 or 319.
No day of the six-day review holds a 33-minute sitting for them.

**Fix (settled).** Day 162's note (and 322's): a student new to the level sits a parallel form of the previous
level's year-end check in the first 35 minutes while the class stages the scene, then joins the staging; the
practical components follow on days 162 to 165 as written. On the three-day short path the sitting moves to day 161
after the hook. Confidence: firm.

### 8. Fluency days far over the frame's count, many thin (minor)

LAYER sequence. REPEAT new.

**What is wrong.** The frame says Fluency in 9 to 12 is "the five-minute warm-up and one or two fluency days a unit";
the CSV has 130 Fluency days (37, 39, 39 and 15 by level), seven to fifteen a paired unit. Many are full run-throughs
of a production (150 to 152, 307 to 312, 467 to 472), which are rehearsal of the students' own work. Others are
template fills a writer cannot teach for 45 minutes: 132 "run-through of the dramaturgy page shared in a discussion",
123 "discussion rounds", and the Level 4 days that state 15 of the working minutes ("warm-up led by a student, then a
ten-minute skill run").

**Fix (settled).** Relabel the production run-throughs as Application ("rehearsal with choice"); rewrite 123 and 132
as Application work on the dramaturgy page and discussion note; give each Level 4 Fluency day its second half (for
example "then a work session on the same skill with a partner's look-for"). If the lead keeps the counts, the .md
gives the reason (rehearsal weeks are run-throughs) under For the lead. Confidence: likely.

### 9. Template text a writer would copy wrong (minor)

LAYER sequence. REPEAT yes (every arts read of 2026-11-26 had a "small text" finding).

- Day 133: "Final rehearsal ... final live observation round" before a mid-unit that scores a written dramaturgy page
  and discussion; rewrite as the final work session on the page and the discussion note.
- Day 490: "three viewpoints on the issue in the devised scenes" (unit 15's words); read "in the student's play". Day
  503: "(the director's note)"; read "(the defense of the play's meaning)".
- Day 281: "builds the written reflection ... using the reflection on the chosen play" repeats itself; read "builds the
  reflection and the cross-cultural piece from the day 278 notes".
- Days 75 and other revision days of written threads: "say what changed in the rehearsal log" for an audience journal
  or critique; read "in the journal" or "on the critique's revision line".
- Day 601: "a timed run of the part to be shown" in the critique unit; read "a timed read of the critique".
- Day 134's goal scores "the class discussion"; name the kept discussion note as the scored product, as the frame's
  evidence line does, and the format (a fishbowl in two rounds of fifteen).

### 10. The four-process table claims hook days and misses real ones (minor)

LAYER sequence. REPEAT yes (the music and media arts reads: process lists drift from the days).

**What is wrong.** Every unit is listed with all four processes, but Connecting for units 17, 19 and 20 is only the
hook day (519, 584, 606), where students pick a play or look at a staging; unit 18 lists 559 (picking a role) and
misses 560 to 563, where TH:Cr1.1.IIIc weaves history and culture into the role, which is the unit's real connecting
work. Unit 19's "Performing" is the critique read aloud (602, 603).

**Fix (settled).** List the days that do the work: unit 18 Connecting 560 to 563; unit 17 Connecting 526 to 531 and
536 (traditions credited for TH:Cr2.1.IIIa); unit 20 Connecting 628 to 631 (the chosen audience and each role's
research); unit 19 Connecting 592 to 595 (a play's history and its current issue). Keep 602 to 603 as "presenting"
in unit 19's Performing cell. The bar asks all four in each course, and every level has them; the brief's "every
unit" then holds on real days. Confidence: firm.

### 11. Unit 3 re-scores kept work that other units let stand (minor)

LAYER sequence. REPEAT new.

**What is wrong.** Units 2, 4, 7, 8, 9, 12, 13 and 14 say the first half's kept products keep their mid-unit mark
"unless reworked". Unit 3's day 79 has the rehearsal log (TH:Pr5.1.Ia) and the script notes (TH:Cr1.1.Ic), both
scored on day 64, "collected and scored after the session" again with no such line. A writer cannot tell which rule
holds.

**Fix (settled).** Add "mid-unit marks standing unless reworked" to day 79 and the unit 3 Assessment line.

### 12. The 80-day path has no weeks and no finals week (minor)

LAYER sequence. REPEAT new.

**What is wrong.** CALENDAR.md rule 4 makes week 16 a finals week for a half-year course. The .md places the full
path's checks but never says where the 80-day path's checks fall. Its line "the 9 to 12 rule is only that week 32 is
a finals week" leaves out the half-year clause.

**Fix (settled).** Add to the Shorter path section: on the 80-day path a level's kept day k sits in week ceil(k / 5);
the mid-year check falls on kept day 41 (Level 1, week 9) or 38 (Levels 2 and 3, week 8), and the year-end check and
its respond day on kept days 79 and 80, week 16, the half-year finals week. Amend the line in "Course-level checks" to
name both finals weeks.

## The writer's For the lead items

1. **End slot without an id (units 1, 6, 11).** Agree: keep, and add the frame line the writer offers.
2. **Check form within two weeks of a unit-end sitting.** sequence-write.md says a course-level check "never repeats a
   task form given in the last two weeks", and every check here does. The aim of that rule (no evidence collected
   twice) is met: each check samples an earlier unit on a new unseen scene. Agree to accept it, but the lead logs it
   as an arts 9 to 12 exception in DESK-ANSWERS so later reads do not raise it again.
3. **Level 4 mid-year talk for 30.** Agree with the written plan (defense note for all, trios at once, the rest on
   the respond day).
4. **50 of 72 ids not on a check.** Agree: keep; the reason is stated.
5. **Sources and browser checks.** Agree: left to the unit plans.
6. **From the frame.** Unchanged; the supplies ceiling is Cory's (below).

## The data, line by line

- **Order inside each unit:** met. No code is used before an Understanding day of its unit teaches it; each paired
  unit's arc reaches its showing and its compelling question.
- **Assessments:** every owned id is on a mid or end day of its unit; mid-units sit at unit day 17 or 18 in every unit
  over 25 days; units 18 and 19 (25 and 22 days) have none, as the frame sets; response time is one respond day per
  assessment. Check-item parts: finding 4.
- **Readiness and retrieval:** the day 1 readiness check is right (last ten minutes after the hook, grade 8 rows, not
  core); every later unit opens retrieval on day 2, never day 1. Same-level gaps: finding 6.
- **Checks that do not repeat:** each check draws on earlier units and the .md says so. Form rule: lead item 2.
- **Standards in full:** all 72 ids carried by days of their own level; Level 4 reassesses Level 3 ids and claims none.
- **Days by load:** unit lengths are the frame's; inside units, findings 1 and 8.
- **The calendar:** checks on weeks 17 or 16 and 32, matching CALENDAR.md's table; no cross-subject lean exists, so no
  day waits on another course. Short path weeks: finding 12.
- **Candidate cells:** all settled with a day or a reason; the three drops (units 7, 10, 12) give reasons that the
  other units' kept candidates bear out.
- **Shorter path:** present, with the 80-day path (the frame's semester path, which stands in for the K to 8
  once-a-week path in 9 to 12) and the ten-days-short year; counts add to 80 and 150 a level. Holding it: findings 1,
  3 and 5.
- **Source map:** not applicable (no base text).
- **Lens checklist, scope and sequence:** ids in the right level, met; every level all four processes, met (finding
  10 for the table); works from many traditions and centuries, met (Ireland, Norway, Nigeria, India, Japan, Ghana,
  the Philippines, Spain, Rome, Cree, Mohegan, Cherokee and Kiowa and Delaware makers, living makers each level);
  technique harder across levels, met (the frame's ladder is carried day by day); daily period in K to 8, not
  applicable; a showing in every unit, met (table reading, rehearsal showing and read critique in Level 4).
- **Bar items 1 to 9 and "Fails if":** met, with item 9 (pacing for real schedules) at risk on the 80-day path
  (finding 1). Equipment and safe use are in every working day's note; sensitivity flags from the frame appear on
  their days (Rover, Macbeth, Sovereignty, Noh, Kathakali and Kabuki, Sweat, The Rez Sisters).
- **Stale notes:** stale.py clean; text slips in finding 9 and the finals-week line in finding 12.

## What is right and should not be touched

- The level placement of every id, and Level 4 owning none.
- The two-thread paired unit, with the first thread assessed at mid-unit and the second at the end, so the teacher
  never marks a performance and a sitting on the same day.
- The observation roster, the final observation rounds before each showing, and the seated or small-group take in
  place of a forced solo.
- The time budgets for 30 on every one-by-one end day.
- The sensitivity lines: studied, never performed, for the Native, sacred and hard-history works.

## What I could not judge

- Whether six companies can tech six pieces in unit 20's days (needs the unit plan's tech schedule).
- The safety rules, which stay "from memory" until the safety agent's read opens the three named guides.
- Outside evidence on semester-length theater pacing: no source was opened for this read.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Short-path merge rules (a) to (c) and the unit 3, unit 16 and respond-day re-maps | No kept day over two merged days; protected days kept (finding 1) | scope-and-sequence.md Shorter path; days.csv notes |
| Swap 16 fold-in days off baseline looks (15 for 19, 49 for 53, 85 for 89, 119 for 123, 169 for 173, 186 for 190, 204 for 208, 221 for 225, 241 for 245, 276 for 280, 329 for 333, 346 for 350, 364 for 368, 381 for 385, 401 for 405, 436 for 440) | Keeps the growth mark on a short year (finding 3) | days.csv notes; fold-in table |
| Baseline carries to the merged-into day on the 80-day path; Level 4 baseline on 483, 521, 561, 586, 608; logic model outputs reworded | APPROACH "Growth" (finding 3) | days.csv; scope-and-sequence.md |
| Check goal rewrites for days 159, 237, 397, 479, 557 | Every part of each sampled id asked (finding 4) | days.csv goals; .md check lines |
| Unit 20 senior folds: 609, 611, 614, 615, 618, 619, 625, 626, 630, 634 | No feedback round or whole folio run folded (finding 5) | scope-and-sequence.md senior table; days.csv notes |
| Same-level retrievals on 48, 84, 203, 240, 363, 400 and design retrieval on 146, 303 and unit 15's tech day | Rule 2 (finding 6) | days.csv retrieves and notes |
| Placement sitting for a new student on day 162 and 322 (161 and 321 on the short path) | The written component needs a day (finding 7) | days.csv notes; units 6 and 11 lines |
| Production run-throughs relabeled Application; 123 and 132 rewritten; Level 4 Fluency days given a second half | Frame's Fluency line (finding 8) | days.csv kind and goal |
| Text fixes on 75, 133, 134, 281, 490, 503, 601 | Writer would copy them wrong (finding 9) | days.csv |
| Process table rows for units 17 to 20 | Real days named (finding 10) | scope-and-sequence.md |
| "Mid-unit marks standing unless reworked" on day 79 | One rule across units (finding 11) | days.csv; .md unit 3 |
| 80-day path weeks and both finals weeks named | CALENDAR.md rule 4 (finding 12) | scope-and-sequence.md |

## For Cory

- The supplies ceiling (frame For the lead item 5): $150 a class a level for high school theater, every free path
  kept. Still open from the frame; nothing in this read changes it.
- Nothing else here changes scope, money, people or audience. The Level 4 company model (finding 2) is a frame
  clarification for the lead.

## Sources

No outside source was opened. Every finding rests on the repository files listed under "What I read" and the
standards' own words file (data/standards/ncas-performance-standards-words.txt); the company model in finding 2 and
the room limits in finding 1 are judgment, marked so. Findings were not logged with `plan.py defect`, since the brief
allows this report as the only edited file; the caller may log them.
