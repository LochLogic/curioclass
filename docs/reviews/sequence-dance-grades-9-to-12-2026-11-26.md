# Expert read: scope and sequence of Dance, grades 9 to 12 (2026-11-26)

Course `dance-grades-9-to-12`. A cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md. I did not write
the scope; this file is the only file I changed.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9
  and "Fails if"), docs/courses/arts/STANDARD.md and docs/courses/arts/APPROACH.md in full, build/scope-writes/ARTS-BRIEF.md.
- docs/courses/dance-grades-9-to-12/scope-and-sequence.md and data/plans/dance-grades-9-to-12/days.csv (all 640 rows,
  goals, codes, `retrieves` and the notes of every flagged, check and safety day), read cold.
- Beside them: the frame (docs/courses/dance-grades-9-to-12/frame.md: the brief, Seams, Models carried, Units rows for
  units 1, 2 and 8 in full, Course-level checks, Cross-subject, For the lead), the 36 da-g9 to da-g12 rows of
  data/progressions/arts.csv, the 63 high school dance lines of data/standards/ncas-performance-standards-words.txt,
  docs/courses/CALENDAR.md (the four 9 to 12 dance rows), the course's rows in data/plans/calendar.csv and the
  leaned-on rows of physical education grade 9 (unit 5, weeks 22 to 26) and health grade 9 (unit 5, week 4).
- Earlier reads for REPEAT tags: docs/reviews/sequence-dance-grades-6-to-8-2026-11-26.md,
  sequence-theater-grades-6-to-8-2026-11-26.md, sequence-visual-arts-grades-6-to-8-2026-11-26.md.
- Gates: `scripts/sequence.py check dance-grades-9-to-12` (0 failures; the "standard None is on no day" notes are For
  the lead 5), `scripts/plan.py check` (no failure for this course), `scripts/frame.py calendar` (0 failures; check
  weeks 17 and 32 for Levels 1 to 3, 15 and 28 for Level 4), `scripts/stale.py check` (0 failures). Short scripts over
  days.csv: every one of the 63 ids sits only on days of its own level (Level 4 carries only `.III` codes); every id
  is on a mid-unit or end-of-unit day of its unit; all fifteen 80-day unit counts compute to the stated totals with no
  day used twice and no protected day merged.
- No outside source was opened for this read. The standards' wording rests on our own-words file; room and minute
  judgments rest on the frame's minute budgets and on memory of high school dance programs, marked so.

## Verdict

Sound in shape: the level rule is stated once and kept (21 ids a level, each on its own level's days, Level 4 claiming
none), every owning unit retrieves its assumed rows on day 2 as the rows' `assumes` cells say, technique is taught in
named steps and drilled before the making that uses it, every unit has one critique by protocol and a revision before
its end showing, and the works run across five continents from 1836 to today with each flagged tradition named in its
day's note. The biggest risk is the 80-day path: in six places a kept piece's first version and its revision from
written feedback land in the same merged lesson, so the feedback step the frame requires cannot happen before the
piece is scored. The one change that matters most is to re-pair those merges (four settled here at no cost, two
needing For the lead 2's rebalance); close behind, DA:Cr2.1.IIa's "alone" part is never assessed.

## Findings, most serious first

### 1. The 80-day path collapses draft, feedback and revision into one lesson in six places

LAYER sequence. REPEAT yes (the short path not holding in the room: dance 6 to 8 finding 1, theater 6 to 8 finding 1).
Confidence: firm (the frame's own kept-piece rule and the scope's merge lists).

- **What is wrong.** The frame says a kept piece is "drafted, given written feedback and revised on earlier counted
  days, then scored". These short-path merges put the draft day and its "revised from written feedback" day in one
  45-minute lesson:
  - Unit 2 `25+26+28`: the invented dancer's habits plan (DA:Pr5.1.Ib, scored day 48 and sampled at the mid-year check).
  - Unit 8 `213+214+215+216`: the comparison with Tharp and Abraham (DA:Cr1.1.IIb, scored day 218).
  - Unit 9 `259+260+262`: the recording plan (DA:Cr3.1.IIb, scored day 275).
  - Unit 10 `285+286+287+288+289`: the linked dance's insight (DA:Cn10.1.IIa, scored day 290).
  - Unit 10 `304+305+306+307+309+310`: the process evaluation (DA:Pr6.1.IIa, scored day 314), merged as well with
    the technical rehearsal.
  - Unit 15 `445+446+447+448+449`: the growth review (DA:Cn10.1.IIIa, scored day 450).
- **Why it matters.** On the 80-day path the teacher cannot read thirty drafts inside the lesson they are written, so
  the piece is scored unrevised, or the revision is skipped. A busy writer copying the list builds those days wrong.
- **Fix.** Add one rule to the Shorter path paragraph: "A kept piece's first version and its revision from written
  feedback never share a merged lesson; at least one lesson lies between them." Then: the four re-pairs in "Settled by
  the expert" (units 2, 8, 9 and the second unit 10 group) keep every count. Unit 10's first group and unit 15's
  group have no slack left (their only unmerged days are the hook and the full run), so they need For the lead 2's
  rebalance; see "The writer's For the lead items" for the exact merges that rebalance allows.

### 2. DA:Cr2.1.IIa's "alone" part is taught but never assessed

LAYER frame (the frame's evidence line), carried into the sequence. REPEAT yes (items that list a code but ask only
part of it: dance 6 to 8 finding 6, visual arts 6 to 8 finding 9). Confidence: firm.

- **What is wrong.** The words line asks students to design original dances alone and with others. Day 221 teaches
  "alone and with others", but every making day after it (223, 224, 227) and the end showing (234) are the group
  dance, and the frame's evidence line names only "the group dance's structure and composition". The solo or duet
  study (day 213) is made before Cr2.1.IIa is taught and is scored for Cr1.1.IIa and IIb.
- **Why it matters.** One part of an owned id has no item, so the end-of-unit assessment does not cover the id in full.
- **Fix.** Settled below: day 224 becomes "Groups build the middle and finish; each student designs one solo passage
  of at least 8 counts inside the group dance (duet version allowed)", and day 234's look-for names the solo passage
  beside the group structure. The frame's unit 8 evidence line needs the same words; the scope puts that under its
  For the lead.

### 3. The Level 1 mid-unit item for DA:Re7.1.Ib rests on a dance with no cultural setting

LAYER sequence. REPEAT yes (a check item that misses a part of its code). Confidence: likely.

- **What is wrong.** Day 102's sitting is "an unseen Curio Class dance and a written description of a second", asking
  how an element carries intent "in each stated setting". The scope itself says, for the year-end check, that "the
  unseen Curio Class dance has no cultural setting of its own". DA:Re7.1.Ib asks about elements across styles and
  cultural traditions in cultural context, so one of the two dances cannot carry the item, and Re7.1.Ib is scored
  nowhere else in unit 4.
- **Why it matters.** The only unit item for an owned id can be answered without the "across traditions" part.
- **Fix.** Settled below: day 102's Re7.1.Ib item uses two short written descriptions from two traditions, each with
  its stated setting (when, where, by whom, for what), written by Curio Class from the work cards' facts; the unseen
  phrase keeps the Re7.1.Ia item. I also recommend taking For the lead 4 (see below).

### 4. Rows used earlier the same level are leaned on with no retrieval

LAYER sequence. REPEAT yes (dance 6 to 8 finding 5, visual arts 6 to 8 finding 6). Confidence: firm.

- **What is wrong.** Rule 2 asks that a row used earlier the same year opens as a retrieval task. Day 2 of each unit
  retrieves the previous level's rows, but not the same-level rows the unit builds on:
  - Unit 4 reworks the unit 3 dance's structure and devices (da-g9-form) from day 96; day 88 retrieves only da-g8-revise
    and da-g8-respond.
  - Unit 5 leads rehearsals and evaluates rehearsal methods (DA:Pr6.1.Ia) on unit 2's rehearsal plan (da-g9-technique);
    day 126 retrieves only da-g8-stage and da-g8-connect.
  - The same pattern in Levels 2 and 3: unit 9 refines unit 8's dance (da-g10-form), unit 10 leads rehearsals after unit
    7's plans (da-g10-technique), unit 14 refines unit 13's dance (da-g11-form), unit 15 leads rehearsals after unit
    12's led rehearsals (da-g11-technique).
- **Why it matters.** Unit 4 and 9 and 14's revising days and unit 5, 10 and 15's leading days assume work done 6 to 16
  weeks before with no recall.
- **Fix.** Settled below: add the same-level row to `retrieves` and to the day 2 note on days 88, 126, 244, 284, 404
  and 444, inside the same ten minutes (the frame says the retrieval combines the unit's threads).

### 5. Unit 17 has no dance shown, and unit 19's dance is optional

LAYER frame (Level 4's design), carried into the sequence. REPEAT new. Confidence: likely.

- **What is wrong.** The lens lists "No showing in a unit" as a scope and sequence error, and bar item 4 asks students
  to make and show. Unit 17's only making is day 571 ("one section remade from what the self-critique found"), shown
  to no one; its end is a spoken panel and a written set. Unit 19's talk carries "a short dance excerpt from the series
  where the student chooses" (day 634), and the 16-count answer phrase made on day 626 is never shown.
- **Why it matters.** A Level 4 student can go 24 days (unit 17) without dancing for anyone, and the capstone can end
  with no dance at all, in a performing-arts course.
- **Fix.** Settled below: day 571 ends with the remade section shown to the student's panel group (describe only,
  unscored); the unit 19 talk on days 636 and 637 includes the day 626 answer phrase, danced by the student or a cast,
  or a seated or described version, and the scope's unit 19 Processes line says so.

### 6. Units 9, 13 and 14 carry five or six light days after their respond day

LAYER sequence. REPEAT new. Confidence: likely.

- **What is wrong.** Days by load. After the respond day, unit 9 runs days 277 to 282 (six days: a responding talk,
  the portfolio choice, concert pieces chosen, one more recorded section, a teacher-danced social dance "lead-in",
  teams formed), unit 14 runs 437 to 442 (six) and unit 13 runs 396 to 400 (five, including day 400, a studio day
  cleaning a piece already scored). Meanwhile the same units' written ids (Re7.1.IIb, Re9.1.IIa; Re7.1.IIIb,
  Re9.1.IIIa) get one draft day and one revision day before scoring.
- **Why it matters.** About a week of each of three units sits after the work is scored, while the scored writing is
  thin; and day 281's "social dance across eras" asks a teacher without dance training to demonstrate several eras'
  social dances, which the frame's teacher promise does not cover.
- **Fix.** For the fix pass: after a respond day keep at most the portfolio choice, the next unit's setup and the
  check setup day; move the rest before the end-of-unit assessment as a second practice day on the unit's written
  ids (unit 9: Re7.1.IIb or Re9.1.IIa; unit 14: Re7.1.IIIb or Re9.1.IIIa; unit 13: a second rehearsal with the
  statement), renumbering inside the unit only. Day 281 becomes a described work card, not teacher demonstrations.

### 7. The 10-days-short year folds production rehearsals and both landing runs

LAYER sequence. REPEAT yes (dance 6 to 8 finding 4). Confidence: likely.

- **What is wrong.** The ten folds a level are all Fluency, nothing assessed, which is right. But Level 1 folds day 144
  (the concert running order run), Level 2 folds days 297 and 308 (the production unit's projection drill and running
  order run) and both of unit 7's landing practices (171 and 178), and Level 3 folds day 459 (the projection drill in
  each venue). The frame's grade 12 bullet already treats the production unit's rehearsal days as the ones that never
  fold, and the jump and leap look-for depends on practiced landings.
- **Why it matters.** A short year loses concert rehearsal and safe-landing practice while drills of written skills stay.
- **Fix.** Settled below: swap 144 for 106; 178 for 187, 297 for 261, 308 for 267; 459 for 354. All swaps are Fluency
  days with nothing scored on them.

### 8. "The same slot at once" in a mixed room holds only roughly

LAYER frame, carried into the sequence. REPEAT new. Confidence: a judgment call.

- **What is wrong.** The scope says a mixed room "runs the same slot at once". Level 1's body unit starts on level day
  13 and Levels 2 and 3 on day 7; unit lengths then differ (38 against 40, 38 against 40, 34 against 36), and the
  mid-year checks fall on level days 85 and 81. A teacher with Level 1 and Level 2 students on one floor has two
  different check days and units that end on different days.
- **Why it matters.** Mixed rooms are the frame's named common case; a teacher who reads "at once" plans one calendar
  and meets six-day gaps.
- **Fix.** The scope's mixed-room bullet states the offsets plainly and gives one rule (the room follows Level 1's
  calendar; Level 2 and 3 students run their review unit on level days 1 to 6, then work as phrase leaders in the
  bridge's days 7 to 12, each level keeping its own check days in the same weeks). A full mixed-room calendar is a
  course page item for the lead.

### 9. Small text a writer would copy wrong

LAYER sequence. REPEAT yes for the first item (respond days labeled the artistic process: visual arts 6 to 8
finding 7); the rest new. Confidence: firm.

- Unit 2's Processes line lists day 49, a respond day, as responding (the lens's day error). Drop it; day 50 (the
  portfolio choice) is not connecting either: unit 2's connecting days are 13 and 24.
- "How to read this file" says "every showing has the unit's critique ... and a revision before it". Mid-unit showings
  (days 30, 62, 183, 218, 342, 377) have a peer look-for check, not the critique. Say "every end-of-unit showing".
- Unit 4's Order line says "the revision starts once the class has a criteria card"; the rework starts on day 95 and
  the criteria card is taught on day 99. Say "the rework uses the bridge's criteria card, retrieved on day 88; the
  evaluation criteria for analysis follow on day 99".
- The Course-level checks table labels the year-end samples "Units 3 and 4", "Units 8 and 9", "Units 13 and 14", but
  every sampled code is from units 4, 9 and 14. Label them "Unit 4 (unit 3 carried)" and so on.
- The Shorter path paragraph says "never merged: ... any mid-unit or end-of-unit day", then hands in the kept-piece
  end days (48, 81, 155, 203, 235, 275, 314, 363, 394, 435, 473) on the showing day. Add "except a kept-piece end
  day, handed in on the showing day before it".
- The first page reads "`DA:...I a`, `b`, `c`"; write "`.Ia`, `.Ib`, `.Ic`". Each Level heading may add its suffix
  ("claims the 21 Proficient ids, `.I`") so a reader landing mid-file sees which standards the level carries.
- Day 538 is a Check day with no `assess` and nothing scored; call it Application ("studio showing, feedback only"),
  or say in the note why it is a Check.
- Units 17 and 19 have no baseline look in any note (the frame promises two marks a unit); add it to days 554 and 620.
- Day 283 says Loie Fuller's dance is "shown from a public domain film". From memory, several early serpentine films
  show imitators, not Fuller; the unit plan confirms on the archive's record who dances, and calls it "her design" if
  the dancer is another.

## The writer's For the lead items

1. **Level 4's end-of-unit assessment as a checkpoint.** Keep the form (day 550 collects, day 551 scores once). It is
   honest and the note says it; no gate change needed now.
2. **Short-path counts in the production units.** Take the rebalance (Levels 2 and 3: 3, 20, 17, 19 and 17). It is
   what finding 1 needs for units 10 and 15. With it: unit 10 merges `285+286+287` and `288+289` (instead of the five);
   unit 15 merges `445+446+447` and `448+449`; unit 9 drops one day by merging all of `277+278+279+280+281+282` (after
   the re-pair settled below, which already uses day 282); unit 14 drops one day by merging `437+438+439+440+441+442`.
   All four keep their protected days whole. This changes the frame's Days bullet and unit rows, so it is the lead's.
3. **Rule 2 count for a band course.** Agree: the skeleton should read the level from the Year column. Tooling.
4. **DA:Re7.1.Ib and DA:Re7.1.IIb unsampled at year-end.** Take it: one short item on a described dance with a stated
   setting, no day added. It also mends the gap finding 3 names.
5. **"None" read as a code.** Agree; tooling.

## The lens checklist (scope and sequence layer)

| Line | Result |
|---|---|
| A grade's ids in the wrong year, or a level tied to a grade | Met: ids by level only, no level names a grade |
| A year with one artistic process missing | Met for every level; per unit, met except finding 5 (unit 17 performing rests on one unseen day) |
| Works all from one tradition or one century | Met: Africa, the Americas, Asia, Europe and the Pacific, 1836 to today, living makers each level |
| Technique that does not get harder | Met: balances and syncopation, then ground and aerial and unpredictable time, then full range and layered rhythm |
| A plan that needs a daily period in K to 8 | Not applicable (high school, five a week by STANDARD.md 3.4; the 80-day path covers a rotation) |
| No showing in a unit | Missed in unit 17 (finding 5) |
| Bar "Fails if" | None fires: technique before making, a showing in every Levels 1 to 3 unit, discipline words in every response, no single canon, no daily K to 8 period |

## Checks the gates cannot see, in brief

- **Order inside units:** sound except finding 9's unit 4 wording. Every technique has its own Understanding day
  before the Application that uses it (for example syncopation day 15 before the section on day 22; landings day 169
  before jumps in the passage day 175; Labanotation days 104 and 105 before the two-method record day 107).
- **Assessments:** every owned id is on a mid-unit or end-of-unit day of its unit; findings 2 and 3 are the parts
  missed. Mid-unit assessments sit in every owning unit (all are over 25 days). Response time is one day a unit.
- **Readiness and retrieval:** day 2 retrieval matches each row's `assumes`; gap returners are placed by the review
  units' day 5 showings (165, 325), before the first owning unit, as the frame designs. Finding 4 is the same-level gap.
- **Checks that do not repeat:** each course-level check draws from the units before the one just ended, and the
  scope says so (with finding 9's label fix).
- **Standards in full:** 63 of 63 ids on days of their own level; Level 4's 11 reassessed ids each on a scored day.
- **Calendar:** check weeks match CALENDAR.md (Levels 1 to 3 weeks 17 and 32, Level 4 weeks 15 and 28); concerts fall
  in week 31. Physical education's "Dance by design" (weeks 22 to 26) comes after units 2 and 3, and days 13 and 67
  name the boundary. data/plans/calendar.csv places health's habits unit in grade 9 week 4, one week before day 24,
  so for a grade 9 student the lean meets; day 24 teaches the dance habits itself either way.
- **Candidate cells:** all 19 settled, each kept with its day cost or dropped with a reason.
- **Shorter path:** present for the 80-day path and the 10-days-short year; counts compute; findings 1 and 7.
- **Source map:** not applicable (no base text).
- **Stale notes:** stale.py passes. Beyond it: docs/courses/CALENDAR.md's four 9 to 12 dance rows print cut labels
  ("Level 1 mid-year (week 1 week 17, Level 1 year-end (week 3 week 32"); the label column is truncated before the
  week text. For the lead, not this scope.

## What is right and should not be touched

- The level rule stated once on the first page, with Level 4 owning no id and reassessing 11 named ones.
- Day 2 retrieval blocks with their minute budget, and day 1 of every unit kept clean for the hook.
- The draft, written feedback, revision cycle on every kept piece in the full year.
- Every flagged work's note: Kykunkor, The Rite of Spring, Birds with Skymirrors and Grace watched and never danced;
  tap watched, not done in hard shoes; beauty ideals studied in the works, never on students' bodies; invented-dancer
  food plans.
- The floor rule on every jump and leap day (169, 171), groups of five on showing days, no student dancing alone.
- The candidate decisions, each with a reason tied to the level's range.

## What I could not judge

- Whether two lessons of Labanotation (days 104 and 105) are enough for a teacher without dance training to teach
  it; the unit plan's step card decides. From memory, introductory high school courses often stop at motif notation.
- Whether a Level 4 class of thirty can each lead a cast (unit 18's 14 led rehearsals, two showing evenings); likely
  Level 4 classes are small, but nothing in the frame says so.
- The Level 3 year-end "description from a tradition not studied": the sensitivity read must see the description.
- Rights lines for every linked work: the unit plans' job.

## Settled by the expert

| Choice | Reason in one line | File |
|---|---|---|
| Unit 2 short path: `22+23+24+25` and `26+28` replace `22+23+24` and `25+26+28` | the habits plan's draft and revision fall in different lessons; count stays 18 | scope-and-sequence.md Shorter path |
| Unit 8 short path: `209+210+211+215` and `213+214+216` replace `209+210+211` and `213+214+215+216` | the comparison's draft and revision fall in different lessons; count stays 17 | scope-and-sequence.md Shorter path |
| Unit 9 short path: `259+260` and `280+281+282` replace `259+260+262` and `280+281` (262 kept whole) | the recording plan's draft and revision fall in different lessons; count stays 20 | scope-and-sequence.md Shorter path |
| Unit 10 short path: `300+301+305` and `304+306+307+309+310` replace `300+301` and `304+305+306+307+309+310` | the process evaluation's draft and revision fall in different lessons; count stays 16 | scope-and-sequence.md Shorter path |
| The no-shared-lesson rule for draft and revision | finding 1, stated once | scope-and-sequence.md Shorter path |
| Day 224: each student designs one solo passage of at least 8 counts inside the group dance (duet allowed); day 234's look-for names it | DA:Cr2.1.IIa "alone" part assessed | days.csv days 224, 234; scope-and-sequence.md unit 8 Assessments; frame line under the scope's For the lead |
| Day 102's DA:Re7.1.Ib item on two written descriptions from two traditions with stated settings | the item needs a cultural context to answer | days.csv day 102; scope-and-sequence.md unit 4 Assessments |
| Same-level rows added to day 2 retrieval: 88 da-g9-form, 126 da-g9-technique, 244 da-g10-form, 284 da-g10-technique, 404 da-g11-form, 444 da-g11-technique | rule 2 for rows used earlier the same level, inside the ten minutes | days.csv `retrieves` and notes; scope-and-sequence.md Retrieval lines |
| Day 571 ends with the remade section shown to the panel group; the unit 19 talk includes the day 626 answer phrase (or its seated or described version) | a showing in every unit | days.csv days 571, 626, 636, 637; scope-and-sequence.md units 17 and 19 |
| 10-days-short swaps: 144 to 106; 178 to 187, 297 to 261, 308 to 267; 459 to 354 | keeps concert rehearsals and a landing run | scope-and-sequence.md Shorter path |
| The text fixes in finding 9 | copy errors a writer would build from | scope-and-sequence.md; days.csv days 283, 538, 554, 620 |

## For Cory

Nothing new from this read on scope, money or people. The frame's two Cory items stay open as the frame states them:
the supplies ceiling (frame For the lead 8) and how far Level 4 promises to recover unmet Advanced ids (frame For the
lead 10).

## Defect log (for the caller to file with `scripts/plan.py defect`, found_by expert)

1. Short-path draft and revision in one lesson, units 2, 8, 9, 10 (two), 15; sequence; moderate.
2. DA:Cr2.1.IIa "alone" part unassessed, unit 8; frame and sequence; moderate.
3. DA:Re7.1.Ib mid-unit item without a cultural setting, day 102; sequence; moderate.
4. Same-level rows without retrieval, units 4, 5, 9, 10, 14, 15; sequence; minor.
5. No showing in unit 17, optional dance in unit 19; frame; minor.
6. Five or six post-respond days in units 9, 13, 14; sequence; minor.
7. 10-days-short folds production rehearsals and landing runs; sequence; minor.
8. Mixed-room "same slot at once" overstated; frame; minor.
9. Text: respond day as responding, critique claim, unit 4 Order line, check labels, never-merged wording, id text,
   day 538 kind, baseline look in units 17 and 19, Fuller film attribution; sequence; minor.
