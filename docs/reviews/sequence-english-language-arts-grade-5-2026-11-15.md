# Expert read: scope and sequence of English Language Arts, Grade 5

Course `english-language-arts-grade-5`. Cold read, 2026-11-15, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of any Codex read of this course, which was not opened.
This report closes the grade 3 to 5 band, so it ends with "Across the band".

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md.
- Cold: docs/courses/english-language-arts-grade-5/scope-and-sequence.md; data/plans/english-language-arts-grade-5/days.csv
  (160 rows: goals, skills, codes, assess values, the notes of every assessment, course and respond day, and the
  skills-block focus of every week) and source-map.csv (154 rows).
- Beside them: the frame; the grade 5 rows of data/plans/ela-texts.csv; data/progressions/ela.csv (the e4 and e5
  rows and their assumes cells); data/plans/calendar.csv; the EL Education K-5 base, grade 5 module zips (lesson
  lists, and the first page of every lesson for its mid- and end-of-unit assessments), for ideas only; the grade 4
  days for the hand-off; the 2026-11-14 expert reads of ELA K to grade 2.
- Gates: `sequence.py check` for this course, 0 failures; the frame, 0 failures. `plan.py check` exits 1 only on
  english-language-arts-grade-6, another course's work in progress. `frame.py calendar`: ELA checks in weeks 17 and
  32 (math 11, 22, 31; science 10, 21, 30; social studies 16 and 29), no stagger break. `stale.py check`: 0 failures.

## Verdict

The strongest of the three on foundations: a named weekly long-word and word-part sequence, fluency on 72 days,
cumulative checks every fifteen days, and a grade 6 hand-off. The source map is exact (154 lessons on 153 days, every
base assessment on its day, the one merge the frame allowed), the whole novel and biography are read in ordered
packets, and the course checks use cold texts on earlier content. The faults are the band's: the spring one-to-one
is scheduled on day 156 and again on days 157 and 158; end days stack (days 38, 39 and 158); check 2 repeats unit
4's on-demand opinion a week later; and the root list reteaches grade 4's. Fix findings 1 to 3 and it is ready.

## Findings, most serious first

### 1. Cumulative decoding and fluency evidence is collected twice, one-to-one, within days (serious; firm)

LAYER sequence. REPEAT yes (finding 1 of the K to 2 reads; grade 3 finding 1).
- **What is wrong.** Day 156's skills block reads "Spring individual long-word and oral-reading checks"; days 157
  and 158 then run the spring individual oral reading and word checks in a 45-minute rotation. The day 150
  cumulative word check sits seven days before them. In winter, the day 75 cumulative check and the day 79 and 80
  "cumulative check and regroup" sit two to six days before the winter screens on days 81 and 82.
- **Why it matters.** Each one-to-one round costs about two blocks for a class; a second round in the same week
  gives no new information and leaves no time to act on the first.
- **Fix (days.csv days 79, 80, 150 and 156; scope and sequence weekly sequence, weeks 16 and 32).** Day 156's skills
  block becomes regrouping and the grade 6 word-part record; days 157 and 158 carry the spring checks. Day 150's
  cumulative check becomes practice. Days 79 and 80 regroup from the day 75 check without a second check. The
  fifteenth-day checks otherwise stay.
- **Confidence.** Firm.

### 2. End days stack performances (moderate; firm)

LAYER sequence. REPEAT yes (finding 2 of the K to 2 reads; grade 3 finding 2).
- **What is wrong.** Day 39 carries 29 codes: the full monologue rewrite (W.5.3a to e, W.5.4, W.5.5), every L.5.1a
  to e, L.5.3a and L.5.2a to e part in 20 minutes of sentence tasks, and an individual RF.5.4 rereading sample. Day
  38 carries 25: a program note plus a three-form reading suite with a heard summary and chart, every L.5.4 and
  L.5.5 part. Course day 158 carries 26: a full on-demand opinion essay, every L.5.1, L.5.2 and L.5.3 part, and the
  end of the spring rotation.
- **Why it matters.** The end-day rule: no one end day asks for full performances on two or more expectations. A
  50-minute window cannot sample thirteen language parts and a full narrative revision fairly for each child.
- **Fix (days.csv days 38 to 41 and 157 to 158; scope and sequence unit 1 and check 2).** Unit 1: the L.5.1, L.5.2
  and L.5.3a short tasks move to day 41's small groups (the fluency evidence there comes from the day 40 recordings, so the
  groups have the time), so
  day 39 keeps the rewrite and its edited product; day 38's heard summary and chart (SL.5.2, RI.5.2) move to day 40,
  which records monologues and needs only short tasks. Check 2: the language item set moves to day 157, beside the
  reading parts; day 158 keeps the opinion and the end of the rotation.
- **Confidence.** Firm.

### 3. Check 2 repeats unit 4's on-demand opinion a week later (moderate; judgment call)

LAYER frame and sequence. REPEAT yes (grade 4 finding 4, the same shape).
- **What is wrong.** Days 150 and 151 assess an on-demand opinion essay with every W.5.1 part; day 158 asks a full
  on-demand opinion with every W.5.1 part again. L.5.3b is assessed on days 144, 153 and 158.
- **Why it matters.** Two full essays in the same form in eight days, with the unit's response (day 156) between
  them, so the check measures the same thing before teaching can change it. The frame's check 2 names W.5.1, so the
  sequence followed it.
- **Fix (frame, check 2; days.csv days 153 and 158).** Either check 2's writing becomes a short cold opinion
  paragraph group (two reasons, one link, a conclusion) that samples transfer rather than a second essay, or it
  moves to an on-demand narrative scene (W.5.3, last assessed day 80) so the year's check covers a form not just
  assessed. Day 153 drops L.5.3b (assessed on day 144); day 158 carries it with the language set (finding 2).
- **Confidence.** Firm on the doubling; which form check 2 uses is a judgment call for the lead.

### 4. The root list reteaches grade 4 (moderate; firm)

LAYER sequence. REPEAT yes (grade 4 finding 2).
- **What is wrong.** Week 12 (day 56) teaches graph and photo, week 18 (day 86) port and week 21 (day 101) -tion and
  -sion, all taught in grade 4 (weeks 9, 11 and 17, and 14). Week 20 returns to dict, taught in week 7.
- **Why it matters.** L.5.4b asks for Greek and Latin affixes and roots as clues; rubric 1o to 1r look for a growing
  inventory. Three weeks of a 32-week list go to parts the children met the year before.
- **Fix (days.csv first rows of weeks 12, 18, 20 and 21; scope and sequence weekly sequence).** Week 12: retrieve
  graph and photo inside new Greek meter and therm; week 18: retrieve port inside new mit and miss; week 20: cred
  alone, dict retrieved; week 21: -tion and -sion retrieved inside -ity and -ial words, with new -ive or -ance. If
  grade 4 takes the roots in its finding 2 (scrib, tract, ject, aud, vis), grade 5's day 160 hand-off and the
  grade 6 list should name them as known.
- **Confidence.** Firm on the repetition; the root choice is a judgment call.

### 5. The grade 4 hand-off is marked unverified, and it is now verifiable (low; firm)

LAYER sequence. REPEAT new (grade 4 finding 5, the same note).
- **What is wrong.** The prerequisite table marks all thirty e4 rows "day map pending" because no grade 4 days.csv
  existed. It exists now and every e4 row is used on its days, so the retrieval treatment is confirmed. One caution:
  e4-fluency is on only 10 grade 4 days (grade 4 finding 1), so the day 2 fall fluency screen matters more than the
  table suggests.
- **Fix (scope and sequence, prerequisites).** Mark each e4 row "grade 4, confirmed"; drop the verification limit
  paragraph; keep the day 2 screen and say that children below it join the twice-weekly rereading group from week 1.
- **Confidence.** Firm.

### 6. Frame readiness wording is stale, and one cell is broken (low; firm)

LAYER frame. REPEAT yes (finding 7 of the grade 2 read; grade 3 finding 5; grade 4 finding 6).
- **What is wrong.** The unit 1 cell says "Readiness checks: the fall oral reading check, grade 4 fragments and
  run-ons, grade 4 discussion roles"; under the grade-number rule these are retrieval, which the scope and sequence
  rightly says. The same cell ends "The unit's word list Lettered parts of these standards taught in another unit:
  L.5.3b (unit 2, unit 4)", two sentences run together.
- **Fix (frame).** "Retrieval: grade 4 fragments and run-ons and discussion roles; the fall oral reading check is a
  diagnostic." Add the missing full stop after "word list".
- **Confidence.** Firm.

### 7. Small slips (low; firm)

LAYER sequence. REPEAT new.
- Source decisions says module 3 unit 2 has no separate lesson 14 file; the base zip G5M3U2 does hold a lesson 14.
  The mapping (day 109) is right; correct the sentence.
- The shorter path gives a two-session split but no minutes for a single shorter period, and sends that case to the
  lead. That is the right answer; grades 3 and 4 should copy the split (their finding 6 and 7).

### 8. Source-map layout differs across the band (low; firm)

LAYER process. REPEAT yes (the grade 2 read, Across the band).
- **What is wrong.** This map's header is source, base_module, base_unit, base_lesson (as G5M1U1L1), stretch, day,
  decision, reason, source_archive; grades 3 and 4 differ. See Across the band.
- **Confidence.** Firm.

## What the two new rules change

- **Readiness counts by grade number.** Nothing in the sequence: every assumed row is an e4 row, used in grade 4
  (finding 5), so retrieval is right; no grade 3 row is assumed, so no readiness check is owed. Only the frame
  wording (finding 6).
- **End days.** Days 38, 39 and 158 change (finding 2); day 153 with finding 3. Days 76 to 80, 118 to 123 and 150 to
  156 otherwise spread their parts well.

## Judged items the brief named

- **Texts against the catalogue.** 25 rows (g5-u1-01 to 05, u2-01 to 06, u3-01 to 06, u4-01 to 08), all placed;
  titles, authors, uses and statuses match. g5-u2-04 is "to confirm" and the sequence uses it only conditionally on
  day 44, with an original replacement; the 1947 reports and teammate memory are conditional on a renewal search.
  Anchors: three literary, two informational (60 and 40), named honestly and left to the frame. Met.
- **Source map against the base.** 154 base lessons; keep 152, merge 2 (module 4 unit 1 lessons 12 and 13, the
  frame's one allowed merge, on day 135). Every base assessment lands on its course day: M1U1 L9 day 9, M1U2 L10 day
  22, M1U3 L5 day 33, M2U1 L8 and L12 days 49 and 53, M2U2 L4 day 58, M2U3 L5 day 72, M3U1 L5 and L12 days 88 and
  95, M3U2 L6 day 101, M3U3 L6 and 7 and L11 days 116, 117 and 121, M4U1 L6 and L12 to 13 days 129 and 135, M4U2
  L5 and 6 and L9 days 140, 141 and 144, M4U3 L2 day 146. Unit 4's 33 days hold its 34 lessons with that merge.
  Met.
- **Reading foundations.** Weeks 1 and 2 retrieve syllable types, schwa and stress, then four- and five-syllable
  decoding; suffixes -ity, -ian, -ial; then roots. RF.5.3 on 159 days, RF.5.4 on 72, fluency on the monologue and
  poems with recorded performances. Met, with findings 1 and 4.
- **Writing across the year.** A twenty-entry cycle at 30/35/35; literary essay and monologue, sensory essay and
  canopy narrative, opinion and informative comparison, water opinion, announcement and leaflet; two-page typing
  and a shared-document exchange in unit 2. Met.
- **Readiness, timers, no outside readers, day totals.** As settled.
- **Calendar and leans.** Science ecosystems (school days 21 to 48), water distribution (105 to 123) and protection
  (125 to 147); social studies sourcing (27 to 43) and civil rights (127 to 142): the scope and sequence reads the
  real dates and bridges on days 42, 84 and 124. Met.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Word-reading scope and sequence explicit, with checks | Met (finding 4 on the root list) |
| Fluency practice and checks | Met (finding 1 on the doubling) |
| Grade 6 assumes foundations grade 5 does not finish | Met: day 160 hands on the word-part record |
| Unit named by a topic and its texts | Met |
| Anchor texts on file, measured, with a reason for their place | Part: all to write; provisional records given |
| Long text read whole | Met (the novel, the biography, both drought stories) |
| Research and full-process writing more than once | Met |
| Formal discussion often | Met (fourteen formal discussions) |
| End task joins reading with writing or speaking on the topic | Met |
| Sensitive content has a teacher note and a sensitivity read | Met |

## What is right and should not be touched

- The weekly word and word-part sequence, written week by week.
- The ordered reading packets for the novel and the biography.
- Every base assessment on its day; the one merge.
- The W.5.6 evidence kept open until the device day exists.
- The real-date bridges on days 42, 84 and 124, and the hundredths grid that never becomes percentages.
- The ten fold-in days, none an assessment.

## What I could not judge

- Text demand: the anchors are unwritten and unmeasured.
- The Puerto Rican and basin-nation sources: left to the sensitivity agent's study, rightly.
- Whether a 45-minute concurrent rotation reaches every child on the check days: the frame's timed probe.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 156, 150 and 79 to 80 drop their one-to-one checks | Course checks carry them | days.csv; scope-and-sequence.md |
| Unit 1 language tasks move to day 41, the heard summary to day 40 | End-days rule | days.csv; scope-and-sequence.md |
| Check 2 language set moves to day 157 | End-days rule | days.csv; scope-and-sequence.md |
| Day 153 drops L.5.3b | Assessed day 144, again day 158 | days.csv |
| Weeks 12, 18, 20 and 21 retrieve grade 4 parts inside new ones | No reteaching | days.csv; scope-and-sequence.md |
| Grade 4 hand-off marked confirmed | The grade 4 days exist | scope-and-sequence.md |

Check 2's writing form (finding 3) and the frame wording (finding 6) are calls for the lead.

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- Common Core State Standards for ELA, grade 5 (data/standards/ccss-ela-standards-full.txt).
- EL Education K-5 Language Arts (2017), grade 5 modules, read for ideas only.
- National Reading Panel (2000) and the WWC foundational skills guide (2016), from memory.

## For the source list

None.

## Across the band

- **The double one-to-one runs through all three, as in K to 2.** Grade 3 days 75 and 76 then 78 and 79, day 150
  then 158; grade 4 day 74 then 79, plus a transfer sample on most assessment rows; grade 5 day 156 then 157 and
  158, day 150, days 79 and 80 then 81 and 82. One rule, written once in the frames' shared assessment wording: the
  course checks carry the cumulative one-to-one; unit windows and fifteenth-day checks regroup.
- **End days stack** in all three (grade 3 days 38, 75, 158; grade 4 days 153 and 158; grade 5 days 38, 39, 158).
  The check 2 language set is the common culprit: in every grade it shares day 158 with an opinion and the spring
  rotation. Moving it to day 157 fixes all three the same way.
- **Unit 4 and check 2 ask the same opinion within a week** in grades 4 and 5. The frames' check 2 wording names
  W.5.1 and W.4.1; the lead should choose once for the band whether check 2 writes a short paragraph group or a
  different form.
- **The word-part inventory is not coordinated.** Grade 3 teaches the common prefixes and suffixes; grade 4 reteaches
  them for five weeks and teaches five roots, two of them twice; grade 5 reteaches graph, photo, port and -tion and
  -sion. A single band list in data/progressions/ela.csv (grade 3 affixes; grade 4 a set of Latin roots such as
  scrib, tract, ject, aud, vis, port, rupt; grade 5 Greek roots and derivational suffixes such as graph, photo,
  meter, therm, bio, geo, -ity, -ial, -ive) would let each grade retrieve rather than reteach. A call for the lead.
- **Fluency coding is uneven.** Grades 3 and 5 put partner rereading on every Tuesday and Thursday row; grade 4 on 10
  days. Grade 4 finding 1 is the band's one serious foundations gap.
- **Hand-off, grade 2 to grade 3.** Grade 3 retrieves every e2 row by id with its day; sound.
- **Hand-off, grade 3 to grade 4.** Grade 4 retrieves every e3 row; the grade 3 days now confirm all 28 were used.
  Grade 4's affix weeks reteach rather than retrieve (grade 4 finding 2).
- **Hand-off, grade 4 to grade 5.** Every e4 row is used in grade 4, so grade 5's retrieval is right; the weak link is
  e4-fluency's 10 days. Grade 5's day 2 screen is the safeguard.
- **Readiness wording** is stale in all three frames; all three sequences apply the grade-number rule correctly.
- **Shorter period.** Only grade 5 gives a two-session split; grades 3 and 4 should copy it.
- **Writing shares** are ledgered in grade 3 (30/35/35) and cycled in grade 5; grade 4 states them without a
  ledger. A small consistency point for the unit plans.
- **Water in grades 3 and 5** stays distinct (access and saving in grade 3; how much is usable and how a river is
  shared in grade 5), as the frames settled.
- **Source-map layouts differ in all six ELA courses K to 5.** Grade 3: base_module, base_unit, base_lesson,
  stretch, day, decision, reason, source. Grade 4: source_id, base_module, base_unit, base_lesson, stretch, day,
  decision, source_file, reason. Grade 5: source, base_module, base_unit, base_lesson (G5M1U1L1), stretch, day,
  decision, reason, source_archive. One layout from sequence-write rule 8 for every course: source, base_module,
  base_unit, base_lesson (a plain number), stretch, day, decision (keep, split, merge, cut, ours), reason, with the
  archive path as an optional last column. A call for the lead (low).
- **The course text record** the frames ask for is outside the writers' permitted files in grades 3 and 5; the lead
  should either open it to the writer or file it in the fix pass.
