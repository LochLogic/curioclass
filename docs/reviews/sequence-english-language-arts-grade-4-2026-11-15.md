# Expert read: scope and sequence of English Language Arts, Grade 4

Course `english-language-arts-grade-4`. Cold read, 2026-11-15, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of any Codex read of this course, which was not opened.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md.
- Cold: docs/courses/english-language-arts-grade-4/scope-and-sequence.md; data/plans/english-language-arts-grade-4/days.csv
  (160 rows: goals, skills, codes, assess values, the notes of every assessment, course and respond day, and the
  word-analysis focus of every week) and source-map.csv.
- Beside them: the frame; the grade 4 rows of data/plans/ela-texts.csv; data/progressions/ela.csv (the e3 and e4
  rows); data/plans/calendar.csv; the EL Education K-5 base, grade 4 module zips (lesson lists and assessment
  lessons), for ideas only; the grade 3 and grade 5 days for the hand-offs; the 2026-11-14 expert reads of ELA K to
  grade 2, for the standard and the REPEAT tags.
- Gates: `sequence.py check` for this course, 0 failures; the frame, 0 failures. `plan.py check` exits 1 only on
  english-language-arts-grade-6, another course's work in progress. `frame.py calendar`: ELA checks in weeks 16 and
  32 (math 12, 23, 31; science 10, 19, 30; social studies 8, 21, 27), no stagger break. `stale.py check`: 0 failures.

## Verdict

The knowledge design is strong: four topics with two literary and two informational anchors, whole long texts read
in installments, discussions about every ten days, bridges for the science and social studies units that the
calendar shows are later, and cold course checks on earlier content. The reading foundations are the weak side.
Fluency, a must-pass Gateway 1 cell, appears in the day rows on only 10 days and not at all in units 2 and 3, though
the prose promises twice-weekly rereading; and the word-part sequence spends five weeks reteaching grade 3's affixes
and only five roots, which grade 5 then reteaches. Fix finding 1 before day writing; findings 2 to 4 are moderate.

## Findings, most serious first

### 1. Fluency is barely in the day rows (serious; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** RF.4.4 and e4-fluency appear on 10 days only (1, 4, 7, 35, 36, 79, 80, 124, 158, 159). Units 2
  and 3, days 39 to 77 and 81 to 119, carry no fluency practice or evidence in days.csv, although the scope and
  sequence promises Tuesday and Thursday partner rereading with teacher feedback all year. Grades 3 and 5 code it
  on 61 and 72 days.
- **Why it matters.** Gateway 1 fluency (1t and 1u) is must-pass: it asks for regular practice and checks across
  the year. The day writer works from the rows; a promise in prose only will not reach the lesson plans. Grade 5
  then assumes e4-fluency as retrieval on day 2.
- **Fix (days.csv, every Tuesday and Thursday row; scope and sequence units 2 and 3).** Add RF.4.4a to c and
  e4-fluency to each Tuesday and Thursday row, with the note grades 3 and 5 use ("15 minutes partner rereading of
  the anchor passage with feedback on accuracy, rate, expression and self-correction; the teacher listens to a
  rotating group"). Keep the winter and spring one-to-one checks where they are.
- **Confidence.** Firm.

### 2. The word-part sequence is thin and repeats grade 3 (moderate; firm)

LAYER sequence. REPEAT new (a band coordination fault; see the grade 5 report).
- **What is wrong.** Weeks 7, 8, 13, 14 and 15 teach un-, re-, dis-, pre-, mis-, -ful, -less, -ness, -ly, -able,
  -tion, -sion, -ment and -ous, all of them grade 3 affixes (RF.3.3a and b, L.3.4b). Only five roots are taught all
  year (graph, photo, tele, port, rupt), and port and rupt come twice (weeks 11 and 12, then 17 and 18). Grade 5
  then teaches graph and photo (day 56), port (day 86) and -tion and -sion (day 101) again as new.
- **Why it matters.** RF.4.3a and L.4.4b ask for Greek and Latin affixes and roots as clues to meaning; rubric 1o
  to 1r look for a growing inventory of word parts. Repeating grade 3's list uses weeks the grade 4 standard needs.
- **Fix (days.csv, weeks 7, 8, 13, 15 and 17 to 18 first rows; scope and sequence weekly sequence).** Weeks 7 and 8
  become new Latin roots (scrib/script, tract) with the grade 3 prefixes retrieved inside the new words; week 13
  becomes ject, week 15 aud and vis; weeks 17 and 18 retrieve port and rupt in the canal words and add struct or
  form. Week 14 (-tion and -sion with unstressed vowels) stays, as spelling. The grade 5 changes follow from this
  (grade 5 finding 4).
- **Confidence.** Firm on the repetition; the root choice is a judgment call.

### 3. The read and spell transfer is sampled on almost every assessment row (moderate; firm)

LAYER sequence. REPEAT yes (the double one-to-one of the K to 2 reads, in a lighter form).
- **What is wrong.** Beside the probes every fifteen days (days 14, 29, 44 and so on to 149), almost every
  assessment row adds "a short read and spell transfer sample" on RF.4.3a and L.4.2d. Day 74's probe falls five
  days before the day 79 winter long-word check.
- **Why it matters.** The same codes are recorded three ways in one week, and the end days look heavier than they
  are (day 74 lists 15 codes, largely from earlier products).
- **Fix (days.csv assessment rows; day 74; scope and sequence assessment conventions).** Drop the transfer sample
  from assessment rows; the fifteen-day probes and the winter and spring checks carry RF.4.3a and L.4.2d. Day 74's
  probe becomes regrouping practice; day 79 carries the long words.
- **Confidence.** Firm.

### 4. Unit 4's end and check 2 ask the same performance five days apart (moderate; firm)

LAYER sequence and frame. REPEAT new.
- **What is wrong.** Day 153 asks an on-demand opinion script (W.4.1a to d) and all of L.4.1a to g; day 158, five
  days later, asks an on-demand opinion and all of L.4.1a to g again. W.4.1 was also assessed on days 116 and 117.
- **Why it matters.** Two full on-demand opinions and two full grammar sets in one week: under the end-day rule,
  day 153 asks two performances, and the check repeats them before the unit's response can act.
- **Fix (days.csv days 153 and 158; scope and sequence unit 4 and check 2).** Day 153 keeps the announcement script
  as a product with L.4.1a and L.4.3 (register), and drops the full W.4.1 and L.4.1 sets; day 158 carries the
  cumulative opinion (on unit 3 content, cold) and the grammar set. If the lead prefers the unit to keep its own
  opinion evidence, day 158's writing moves to a different form and the frame's check 2 wording changes with it.
- **Confidence.** Firm on the doubling; the choice of which day keeps W.4.1 is a judgment call.

### 5. The grade 3 hand-off is marked unverified, and it is now verifiable (low; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** The prerequisite table says no grade 3 ELA days.csv exists, so every e3 row is "day map
  pending". It exists now, and all 28 grade 3 rows are used on its days.
- **Fix (scope and sequence, prerequisites).** Change each row to "grade 3, confirmed" and drop the verification
  limit paragraph. The retrieval treatment is right as written.
- **Confidence.** Firm.

### 6. Frame readiness wording is stale (low; firm)

LAYER frame. REPEAT yes (finding 7 of the grade 2 read).
- **What is wrong.** The frame's unit 1 cell and its row table still name readiness for the fall oral reading check,
  e3-reading-range and the grade 3 sentences. Under the grade-number rule they are retrieval, which the scope and
  sequence rightly schedules.
- **Fix (frame).** Replace "readiness" with "retrieval" in those cells; the fall oral reading check is a diagnostic.
- **Confidence.** Firm.

### 7. The shorter period has no minute budget (low; firm)

LAYER sequence. REPEAT yes (finding 6 of the grade 2 read).
- **What is wrong.** The shorter path splits the 90 minutes into two blocks where possible, but names no minutes for
  the word lesson, rereading and independent reading when the unit lesson itself is shorter.
- **Fix (scope and sequence, shorter path).** Give the grade 5 split: two sessions (60 plus 30, or 45 plus 45), the
  ten-minute word lesson, the twice-weekly rereading and three independent-reading sessions kept whole; a single
  short period goes to the lead.
- **Confidence.** Firm.

### 8. Source-map layout differs across the band (low; firm)

LAYER process. REPEAT yes (the grade 2 read, Across the band).
- **What is wrong.** This map's header is source_id, base_module, base_unit, base_lesson, stretch, day, decision,
  source_file, reason; grades 3 and 5 differ.
- **Fix.** One layout for every course (see the grade 5 report, Across the band).
- **Confidence.** Firm.

## What the two new rules change

- **Readiness counts by grade number.** Nothing in the sequence: every e3 row was used in grade 3 (finding 5
  confirms it) and is retrieved. Only the frame wording (finding 6).
- **End days.** Days 153 and 158 (finding 4); day 74 lightens with finding 3. Days 34 to 38, 74 to 77, 115 to 119
  and 151 to 156 otherwise spread the end components well.

## Judged items the brief named

- **Texts against the catalogue.** The grade 4 rows are all placed; titles, authors, uses and statuses match. Two
  literary anchors (the verse novel, the letters chapter book) and two informational (animal defenses, the Erie
  Canal history): the frame's half and half. Met.
- **Source map against the base.** 153 base lessons (module 1 unit 3 lessons 8 and 9, and module 4 unit 1 lessons 4
  and 5, are bundled); keep 146, merge 4, split 1, ours 4, cut 2, each with a reason. Base order kept; the myth days
  and the module 4 unit 2 assessment slot are explained. Met.
- **Reading foundations.** Long words: syllable retrieval, three- and four-syllable division, schwa and stress in
  weeks 1 to 6, sound. Word parts: finding 2. Fluency: finding 1. RF.4.3 on 160 days.
- **Writing across the year.** Process pieces in every unit, research in units 2 and 4, opinion in units 3 and 4,
  narrative in units 2 and 4. Met; the shares are stated, not ledgered as in grade 3 (low, no finding).
- **Readiness, timers, no outside readers, day totals.** As settled.
- **Calendar and leans.** Science unit 6 (school days 118 to 147) and unit 5 (97 to 117), social studies unit 5 (80
  to 103) and unit 4 (60 to 79) confirmed against calendar.csv; the bridges on days 39, 81 and 126 answer them. Met.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Word-reading scope and sequence explicit, with checks | Part: syllables met; word parts in finding 2 |
| Fluency practice and checks | Not met in the day rows (finding 1) |
| Grade 5 assumes foundations grade 4 does not finish | Met: day 160 hands on a portfolio, but finding 2 changes what it lists |
| Unit named by a topic and its texts | Met |
| Anchor texts on file, measured, with a reason for their place | Part: all to write; provisional records given |
| Long text read whole | Met (the verse novel, the chapter book) |
| Research and full-process writing more than once | Met |
| Formal discussion often | Met (about every ten days) |
| End task joins reading with writing or speaking on the topic | Met |
| Sensitive content has a teacher note and a sensitivity read | Met |

## What is right and should not be touched

- The retrieval table, row by row, with days.
- The bridges on days 39, 81 and 126.
- Discussions about every ten days, with roles fading.
- Installments for the whole long texts, in order.
- The explicit base exceptions (the myth days, the module 4 unit 2 assessment slot).
- Cold course checks on earlier-unit content.

## What I could not judge

- Text demand: the anchors are unwritten and unmeasured.
- The Haudenosaunee accounts in unit 3: left to the sensitivity agent's study.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| RF.4.4 and e4-fluency on every Tuesday and Thursday row | Gateway 1 fluency is must-pass | days.csv |
| Weeks 7, 8, 13, 15 and 17 to 18 teach new roots, grade 3 affixes retrieved inside them | RF.4.3a, L.4.4b; no reteaching | days.csv; scope-and-sequence.md |
| Assessment rows drop the read and spell transfer sample; day 74 probe becomes practice | Probes and checks carry it | days.csv |
| Day 153 drops full W.4.1 and L.4.1; day 158 carries them | No repeat within a week | days.csv; scope-and-sequence.md |
| Grade 3 hand-off marked confirmed | The grade 3 days exist | scope-and-sequence.md |
| Shorter period gets the two-session split | Match grade 5 | scope-and-sequence.md |

The frame wording (finding 6) is the lead's fix pass; the root inventory across the band is a call for the lead
(grade 5 report, Across the band).

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- Common Core State Standards for ELA, grade 4 (data/standards/ccss-ela-standards-full.txt).
- EL Education K-5 Language Arts (2017), grade 4 modules, read for ideas only.
- National Reading Panel (2000) and the WWC foundational skills guide (2016), from memory.

## For the source list

None.
