# Expert read: scope and sequence of English Language Arts, Grade 3

Course `english-language-arts-grade-3`. Cold read, 2026-11-15, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of any Codex read of this course, which was not opened.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md.
- Cold: docs/courses/english-language-arts-grade-3/scope-and-sequence.md; data/plans/english-language-arts-grade-3/days.csv
  (160 rows: goals, skills, codes, assess values, the notes of every assessment, course and respond day, and of
  every skills-block week) and source-map.csv.
- Beside them: the frame; the grade 3 rows of data/plans/ela-texts.csv; data/progressions/ela.csv (the e2 and e3
  rows); data/plans/calendar.csv; the EL Education K-5 base at S:\CurioClass-sources\el-education-k5-2017, grade 3
  module zips (lesson lists and the assessment lessons), for ideas only; the grade 2 scope and sequence and days for
  the hand-off; the 2026-11-14 expert reads of ELA kindergarten to grade 2, for the standard and the REPEAT tags.
- Gates: `sequence.py check` for this course, 0 failures; the frame, 0 failures. `plan.py check` exits 1 only on
  english-language-arts-grade-6 (no scope and sequence yet), another course's work in progress. `frame.py calendar`:
  ELA checks in weeks 16 and 32 (math 12, 23, 31; science 9, 20, 30; social studies 14, 25, 28), no stagger break.
  `stale.py check`: 0 failures.

## Verdict

A careful, well-built year: every grade 2 row is retrieved on a named day, all 153 base lessons are placed in order
with only the two video lessons cut for a reason, the writing ledger and discussion schedule are explicit, the
bridges to science and social studies sit on the right days, and both course checks use cold texts on earlier
content. The faults are the ones the K to 2 reads found: the cumulative oral reading and long-word evidence is
collected one-to-one twice within days (days 75 and 76, then 78 and 79; day 150, then 158), and end days stack
performances (days 38, 75 and 158). Fix those two and it is ready; the rest is low.

## Findings, most serious first

### 1. Cumulative decoding and fluency evidence is collected twice, one-to-one, within days (serious; firm)

LAYER sequence. REPEAT yes (finding 1 of the kindergarten, grade 1 and grade 2 reads, 2026-11-14).
- **What is wrong.** Day 75 (unit 2 end) holds a word check on RF.3.3a, b and d; day 76 holds the individual poem
  recording on RF.3.4a to c. Course check days 78 and 79 then repeat the winter oral reading and long-word check on
  RF.3.3a, b, d and RF.3.4, "also drawing on the individual poem recording", two to four days later. In spring, the
  day 150 cumulative word check sits seven days before the spring check on day 158.
- **Why it matters.** A one-to-one reading for a class of 25 takes most of two blocks. Doing it twice in a week
  costs that time and gives no new information; it also tests the same words before the response day can act.
- **Fix (days.csv days 75, 76 and 150; scope and sequence unit 2, unit 4 and course checks).** Remove the RF.3.3
  and RF.3.4 evidence from days 75 and 76: the poem recording stays as practice and a performance, and for any
  child whose recording is clean it may stand as that child's check 1 fluency sample, so the day 79 rotation is
  shorter. Day 150's cumulative word check becomes regrouping practice; day 158 carries the spring long-word
  evidence. The five-minute cumulative checks on the other fifteenth days stay.
- **Confidence.** Firm.

### 2. End days stack performances (moderate; firm)

LAYER sequence. REPEAT yes (finding 2 of the K to 2 reads).
- **What is wrong.** Day 38 carries 23 codes: RL.3.1 to 3 and 7, RI.3.1, 2 and 7, RL.3.4, L.3.5a, all of L.3.4,
  SL.3.2, RF.3.3a and d, all of SL.3.1 and SL.3.3, beside publishing the bookmark. Day 75 carries 26: the revised
  essay, research notes, W.3.6, nine L.3.1 parts and the word check. Course day 158 carries 31: an article pair, an
  opinion paragraph, every L.3.1a to i and L.3.2a to g part, and the spring oral reading and long words; day 157
  asks for a packet of connected stories, a scene and a poem.
- **Why it matters.** The new end-day rule: no one end day asks for full performances on two or more expectations.
  A 60-minute lesson cannot sample all these parts fairly for each child, and the language set and oral reading
  compete for the same teacher.
- **Fix (days.csv; scope and sequence units 1 and 2 and check 2).** Unit 1: the listening and discussion evidence
  (SL.3.1, SL.3.2, SL.3.3) moves into the small-group discussion on day 36 or 37; the word samples come from the
  day 30 word check and the day 35 small groups; day 38 keeps the reading suite and the bookmark. Unit 2: spread day 75 over
  days 74 to 76, the essay and notes on 74, W.3.6 and the language parts on 75 (finding 1 removes the RF). Check 2:
  the language item set moves to day 157 (selected and short answers, beside the cold stories), so day 158 keeps the
  article pair, the opinion paragraph and the spring rotation.
- **Confidence.** Firm.

### 3. The long-word path is late and has no named catch-up route (low; judgment call)

LAYER sequence. REPEAT new.
- **What is wrong.** Multisyllable decoding (RF.3.3c) starts only in week 17, after the affixes. Children who miss
  the grade 2 vowel-team or syllable-type screen in week 1 get "conference-time groups", with no named sequence.
- **Why it matters.** Gateway 1 word reading (1g to 1n) is must-pass and asks for explicit, systematic teaching;
  grade 3 is the last grade where a child still short on grade 2 phonics gets a full year of it.
- **Fix (scope and sequence, weekly word sequence; days.csv notes, weeks 1 to 4).** Name the route: children below
  the screen work grade 2's cycles for their gap in the Monday, Wednesday and Friday independent-reading twenty
  minutes, retested at the day 15 and 30 cumulative checks. Optionally start two-syllable division (closed and open,
  VC/CV) in week 5 so three-syllable work in week 17 builds on it.
- **Confidence.** Judgment call on the timing; firm that a route needs a name.

### 4. Anchors are 75 percent literary (low; judgment call)

LAYER frame. REPEAT yes (the writer's own For the lead 2).
- **What is wrong.** Eight anchors: six literary (three picture-book stories, the frog poems, the pourquoi tale, the
  chapter book) and two informational (the frog book, the water book). The frame asks for half and half.
- **Fix (data/plans/ela-texts.csv; frame unit 1 and 4 cells).** Designate g3-u1-06 (the packhorse librarians
  article) and g3-u4-02 (the region walk article) as anchors: six to four, and each unit then has an informational
  anchor. No text or day changes.
- **Confidence.** Judgment call; the lead's fix pass.

### 5. Frame readiness wording is stale (low; firm)

LAYER frame. REPEAT yes (finding 7 of the grade 2 read).
- **What is wrong.** The frame's unit 1 cell and its "Which row sits where" paragraph still say "Readiness checks:
  the fall oral reading check, grade 2's wh-questions and simple and compound sentences". Under the grade-number
  rule these rows were used in grade 2, so they get retrieval, which the scope and sequence rightly schedules.
- **Fix (frame).** Replace with "Retrieval: grade 2's wh-questions and simple and compound sentences; the fall oral
  reading check is a diagnostic".
- **Confidence.** Firm.

### 6. The shorter period has no minute budget (low; firm)

LAYER sequence. REPEAT yes (finding 6 of the grade 2 read).
- **What is wrong.** The shorter path folds ten days for a short year, but a school with a shorter daily period
  gets no minute split of the 60-minute lesson and 30-minute skills block.
- **Fix (scope and sequence, shorter path).** Add the split grade 5 uses: two sessions (60 plus 30, or 45 plus 45),
  the ten-minute word lesson and the twice-weekly rereading kept whole; a single short period with no other
  literacy time goes to the lead.
- **Confidence.** Firm.

### 7. Source-map layout differs across the band (low; firm)

LAYER process. REPEAT yes (the grade 2 read, Across the band).
- **What is wrong.** This map's header is base_module, base_unit, base_lesson, stretch, day, decision, reason,
  source; grades 4 and 5 use other orders and names.
- **Fix.** One layout for every course, the columns sequence-write rule 8 names (see the grade 5 report, Across
  the band).
- **Confidence.** Firm.

### 8. Small slips (low; firm)

LAYER sequence. REPEAT new.
- Teaching-day codes cells list 15 to 26 codes because the skills-block parents ride along; that overstates what a
  day carries. List only the codes the day teaches or assesses, with the skills-block codes on their own days.
- The writer's For the lead 1 asks for a course text record outside its permitted files; it is still unmet.

## What the two new rules change

- **Readiness counts by grade number.** Nothing in the sequence: every e2 row was used in grade 2 and is retrieved.
  Only the frame wording (finding 5).
- **End days.** Days 38, 75 and 158 change (finding 2).

## Judged items the brief named

- **Texts against the catalogue.** 25 rows (g3-u1-01 to 08, u2-01 to 07, u3-01 to 05, u4-01 to 05), all placed;
  titles, authors, uses and statuses match. g3-u1-08 is "to confirm" and the sequence uses it only after rights are
  confirmed. Met, with finding 4.
- **Source map against the base.** 153 base lessons (module 2 unit 3 lessons 11 and 12, and module 4 unit 3 lessons
  8 to 10, are bundled downloads); 151 keep, 2 cut (the video lessons, with a reason), 2 ours. Order kept, each base
  assessment on its day. Met.
- **Reading foundations.** Long words, affixes and fluency run in the 30-minute skills block, with five-minute
  cumulative checks every fifteenth day and fall, winter and spring screens. RF.3.3 on 124 days, RF.3.4 on 61.
  Met, with findings 1 and 3.
- **Writing across the year.** A ledger at 30/35/35 opinion, informative and narrative, process pieces in every
  unit, research in units 2 and 4. Met.
- **Readiness, timers, no outside readers, day totals.** As settled.
- **Calendar and leans.** Science unit 3 (school days 47 to 73) and unit 4 (74 to 98), social studies unit 5 (90 to
  121) confirmed against calendar.csv; the bridges on days 1, 26, 54 and 58 answer them. Met.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Word-reading scope and sequence explicit, with checks | Met (finding 3 on the catch-up route) |
| Fluency practice and checks | Met (finding 1 on the doubling) |
| Grade 4 assumes foundations grade 3 does not finish | Met: day 160 hands on the long-word and fluency record |
| Unit named by a topic and its texts | Met |
| Anchor texts on file, measured, with a reason for their place | Part: most to write; provisional records given; balance in finding 4 |
| Long text read whole | Met (the chapter book, unit 3) |
| Research and full-process writing more than once | Met |
| Formal discussion often | Met |
| End task joins reading with writing or speaking on the topic | Met |
| Sensitive content has a teacher note and a sensitivity read | Met |

## What is right and should not be touched

- Retrieval of every grade 2 row, by id, with its day.
- The writing ledger and the discussion schedule.
- The bridges on days 1, 26, 54 and 58 for the leans the calendar shows are later.
- Course checks on cold texts from an earlier unit's content.
- The ten fold-in days for a short year, none an assessment.
- Base order kept; the two video lessons cut with a reason.

## What I could not judge

- Text demand: the anchors are unwritten and unmeasured.
- Whether the frog and water texts are accurate science: the text agent's read.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Days 75, 76 and 150 drop cumulative decoding and fluency evidence | Course checks carry it | days.csv; scope-and-sequence.md |
| A clean poem recording may stand as a child's check 1 fluency sample | Saves rotation time, no new task | scope-and-sequence.md, check 1 |
| Day 38 evidence spread to days 30, 35 to 37 | End-days rule | days.csv |
| Day 75 spread over days 74 to 76 | End-days rule | days.csv |
| Check 2 language set moves to day 157 | End-days rule | days.csv; scope-and-sequence.md |
| Named catch-up route for children below the grade 2 screen | Gateway 1 systematic teaching | scope-and-sequence.md; days.csv weeks 1 to 4 |
| Shorter period gets the two-session split | Match grade 5 | scope-and-sequence.md |

The frame wording (finding 5) and the anchor designations (finding 4) are the lead's fix pass.

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- Common Core State Standards for ELA, grade 3 (data/standards/ccss-ela-standards-full.txt).
- EL Education K-5 Language Arts (2017), grade 3 modules, read for ideas only.
- National Reading Panel (2000) and the WWC foundational skills guide (2016), from memory.

## For the source list

None.
