# Expert read: scope and sequence of English Language Arts, Grade 2

Course `english-language-arts-grade-2`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of the Codex read of the same course, which was not
opened. This report closes the band, so it ends with "Across the band".

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md (rules 1 to 11).
- Cold: docs/courses/english-language-arts-grade-2/scope-and-sequence.md, data/plans/english-language-arts-grade-2/days.csv
  (160 rows: goals, codes, assess values, the notes of every assessment and course day) and source-map.csv
  (350 rows).
- Beside them: the frame; the grade 2 rows of data/plans/ela-texts.csv; docs/courses/CALENDAR.md; the EL Education
  K-5 base: the grade 2 module assessment lessons and the grade 2 Skills Block cycle list, for ideas only; the
  kindergarten and grade 1 scopes and sequences for the hand-offs; for REPEAT tags,
  docs/reviews/frame-english-language-arts-grade-2-2026-11-14.md, frame-ela-k-2-fixes-2026-11-14.md and
  progression-ela-2026-11-13.md; the science and social studies grade 2 reads of this date.
- Gates: `plan.py check` passes this course and its frame (0 failures). `frame.py calendar`: ELA checks in weeks 15,
  16 and 32 (math 18, 19 and 29; science 17 and 28; social studies 14 and 31), no stagger break; nearest gaps to math
  14 and 13 school days. `stale.py check`: 0 failures.

## Verdict

The strongest of the three: it already applies the count-by-grade rule (retrieval, no readiness), keeps all 130
Skills Block lessons in source order with matched decodables, places every base topic lesson, splits revising from
editing, and bridges the later science pollinator unit. The faults are the band's two: the cumulative decoding and
fluency evidence is collected one-to-one twice within days (days 68 to 71 then 75; day 156 then 158), and end days
stack full performances, with day 156 at 18 codes and the mid-unit day 101 at 19. Fix those and it is ready.

## Findings, most serious first

### 1. Cumulative foundations evidence is collected twice, one-to-one, within days (serious; firm)

LAYER sequence. REPEAT yes (finding 1 of the kindergarten and grade 1 reads, this date).
- **What is wrong.** Day 156 observes all six RF.2.3 parts through cycle 26, spelling transfer and band reading with
  fluency; the year-end check on day 158 checks the same codes two days later. Mid-year, days 68 to 71 collect
  RF.2.3d to f and L.2.2d and e through cycle 12; day 75 checks RF.2.3a, b, d, e, f and L.2.2d and e again.
- **Why it matters.** Individual oral reading for a class takes most of two blocks. Doing it twice wastes that time
  and gives no new information.
- **Fix (days.csv days 68, 71 and 156; scope and sequence units 2 and 4 and course checks).** Remove the cumulative
  RF.2.3, RF.2.4 and L.2.2d and e evidence from days 68, 71 and 156; their foundations blocks stay flexible groups
  and regrouping. The course checks (days 75 and 158) carry the one-to-one evidence, and the unit records cite them.
  The cycle checks on lesson 5 of each cycle stay as they are.
- **Confidence.** Firm.

### 2. End days stack full performances (moderate; firm)

LAYER sequence. REPEAT new (the rule was added after the course was written).
- **What is wrong.** Day 156 asks for recount and moral, two comparisons and reason-to-point links in reading
  stations, beside the foundations above (18 codes). Day 68 asks for every word strategy, topic and paragraph focus,
  purpose, features and RL.2.5 (11 codes); day 71 for revising, all L.2.1 and L.2.2 parts and decoding (10). Days 30
  and 31 each join the informational book with question words, images, spelling and fluency (8 each).
- **Fix (days.csv; scope and sequence).** Unit 4: recount and moral on day 153, literary comparison on 154, the
  informational comparison and reasons on 156 (finding 1 removes its foundations). Unit 2: the L.2.4 strategies are
  already checked on day 57; day 68 keeps paragraph focus and RL.2.5 and draws the rest from day 57's record; day 71
  keeps the editing and conventions. Unit 1: the book on day 30, the reading and fluency evidence on day 31 and in the
  day 26 to 29 groups.
- **Confidence.** Firm.

### 3. Mid-unit day 101 carries 19 codes on a teaching foundations day (moderate; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 101 is the research write-up assessment (W.2.7, W.2.8, W.2.2, W.2.5), but its codes also
  name RF.2.3c to f, RF.2.4a to c, L.2.6 and SL.2.1a to c and SL.2.3. Its foundations block is a cycle 17 teaching
  lesson (L84), not a cycle check, and cycle 17's patterns are not finished.
- **Why it matters.** "codes" on an assessment row is evidence reserved for that task; this reserves decoding
  evidence mid-cycle and discussion evidence on a writing day.
- **Fix (days.csv day 101).** Keep W.2.7, W.2.8, W.2.2, W.2.5, L.2.2d and e. Drop the RF codes (the day 102 cycle
  check holds them) and observe SL.2.1 and SL.2.3 on days 99 and 100.
- **Confidence.** Firm.

### 4. The response sits inside the observe day (low; judgment call)

LAYER sequence. REPEAT yes (finding 6 of the grade 1 read, this date).
- **What is wrong.** The final 15 minutes of day 118 is the only response for days 117 and 118; day 138's first ten
  minutes responds on a cycle check day.
- **Fix.** Finish the recordings on day 117 and the first half of day 118, so the response has evidence for every
  child. Day 138 is fine as written.
- **Confidence.** Judgment call.

### 5. Two base assessment lessons become application days (low; likely)

LAYER base text. REPEAT new.
- **What is wrong.** Base M3U2 L11 (day 98) and M4U3 L8 and L10 (days 150 and 152) are assessment lessons in the
  base; here they are unassessed, and the evidence moves to days 99 to 101 and 153 to 156.
- **Fix.** Acceptable as a consolidation; give each a reason in source-map.csv so the unit plan does not rebuild the
  base assessment.
- **Confidence.** Likely.

### 6. The shorter period has no minute budget (low; firm)

LAYER sequence. REPEAT yes (finding 5 of the grade 1 read, this date).
- **What is wrong.** It says what to trim and then hands a shorter period to the lead. Kindergarten gives a budget.
- **Fix.** Give a 100-minute version (for example 45 topic, 55 foundations) with what each block drops; leave only a
  period under that to the lead. The ten fold-ins are good (none assessed).
- **Confidence.** Firm.

### 7. Frame readiness wording is stale (low; firm)

LAYER frame. REPEAT yes (the writer's For the lead item 1; the science and social studies reads found the same).
- **What is wrong.** The frame's "baseline readiness check" and "short readiness check on any grade 1 row". The
  scope and sequence rightly uses retrieval.
- **Fix.** Frame wording: "unit 1 opens with retrieval of grade 1's foundations and fluency rows and a short
  placement screen; later units retrieve the grade 1 rows they lean on". The lead's fix pass.
- **Confidence.** Firm.

### 8. Small slips (low; firm)

LAYER sequence. REPEAT new.
- The scope and sequence says "day 77 retrieves applicable grade 1 routines" for unit 3, but day 77 is the mid-year
  response; move that retrieval to day 78's note.
- The poems (g2-u1-03, g2-u3-03, g2-u4-06) are "to choose" in the catalogue while the plan chooses Curio Class
  originals: update the statuses. g2-u4-02's second telling is still open: name it before unit 4's plan.

## What the two new rules change

- **Readiness counts by grade number.** Nothing in the sequence: it already follows the rule, and no kindergarten row
  sits idle through grade 1. Only the frame wording (finding 7).
- **End days.** Days 30, 31, 68, 71 and 156 change (finding 2), with day 101 (finding 3).

## Judged items the brief named

- **Texts against the catalogue.** 15 rows, all placed. Literary anchors in units 1 and 4, informational anchors in
  every unit, literary paired texts throughout; the plan rightly declines a numerical balance until grouped rows are
  written. Met, with the status lags in finding 8.
- **Source map against the base.** Topic keep 142, split 1 (M2U3 L12, revise and edit), ours 10; foundations keep 130
  in order, ours 24; decodables 26 (25 readers and the poem); Labs cut 16 with a reason. Met.
- **Foundations order.** Cycles 1 to 26 in source order, five lessons each, a cycle check on lesson 5, daily
  decodable reading and fluency, prefixes held to their cycles. Met.
- **Base assessments.** M1U1 L11, M1U2 L6 and 7, M1U3 L5, M2U1 L8 and 9, M2U2 L12, M2U3 L10 to 12, M3U1 L6, M3U3 L10
  to 12, M4U1 L11 and 12, M4U2 L6 and L8 to 10, M4U3 L11 and 12 all carry assessments. Met, except finding 5.
- **Readiness, timers, device and paper path, day totals.** As settled.
- **Calendar and leans.** Science pollination is later (weeks 24 and 25) and bridged on days 78 and 88; social studies
  accounts and claims come first. Met.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Phonics scope and sequence present and tied to decodables | Met |
| A pattern used in decodable text before it is taught | Met |
| Grade 3 assumes foundations grade 2 does not finish | Met: the year-end record hands on supported and independent reading separately |
| Unit named by a topic and its texts | Met |
| Anchor texts on file, measured, with a reason for their place | Part: all to write; provisional records given |
| Long text read whole | Met (the school story, days 1 to 10) |
| Research and full-process writing more than once | Met |
| Formal discussion often | Met (turn, pair, link, clarify) |
| End task joins reading with writing or speaking on the topic | Met |
| Sensitive content has a teacher note and a sensitivity read | Met |

## What is right and should not be touched

- Retrieval, not readiness, with the grade 1 ids in the day notes.
- Revising and editing on separate days; the typed class piece and the audio stories as the two digital tools.
- The bridges for the later science unit.
- Independent and supported reading recorded apart.

## What I could not judge

- Text demand: every prose text is unwritten.
- The Quechua and Mexican tale sources: left to the sensitivity agent's study, rightly.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Days 68, 71 and 156 drop cumulative decoding and fluency evidence | Course checks carry it | days.csv; scope-and-sequence.md |
| End-day performances spread over the last teaching days | New end-days rule | days.csv days 26 to 31, 68 to 71, 153 to 156 |
| Day 101 keeps only the writing and research codes | Evidence matches the task | days.csv day 101 |
| Day 118 response follows recordings finished earlier | Every child has evidence to answer | days.csv days 117 and 118 |
| Base M3U2 L11 and M4U3 L8 and L10 kept unassessed, with reasons | Consolidated into the windows | source-map.csv |
| Shorter period gets a 100-minute budget | Match kindergarten | scope-and-sequence.md |
| Poems marked Curio Class original | Plan already chose | data/plans/ela-texts.csv |

The frame wording (finding 7) is the lead's fix pass.

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- Common Core State Standards for ELA, grade 2 (data/standards/ccss-ela-standards-full.txt).
- EL Education K-5 Language Arts (2017), grade 2 modules and Skills Block, read for ideas only.
- National Reading Panel (2000) and the WWC foundational skills guide (2016), from memory.

## For the source list

None.

## Across the band

- **One assessment fault runs through all three.** Each course collects the cumulative letter, sound, decoding and
  fluency evidence one-to-one in its last unit window and again in the course check days later (K days 76 and 156,
  grade 1 days 72 and 155, grade 2 days 68 to 71 and 156). One rule fixes it: the course check carries the
  cumulative one-to-one; unit windows keep cycle checks of their own patterns. Write it once in the frames' shared
  assessment wording.
- **End days.** All three stack performances (K days 32, 33, 74, 76, 156; grade 1 days 31, 33, 155, 156; grade 2
  days 30, 31, 68, 71, 156, with day 101). Same fix each time: spread over the unit's last teaching days, in small
  groups in K and grade 1.
- **Observation load** is heaviest in kindergarten (about a quarter of the year) and falls by grade 2. Embedded
  observation on teaching days, with a per-child record, is the shared answer, as in the science and social studies
  reads.
- **Continued foundations rows** are owned where they open and completed later in every grade (RF.K.3b, RF.1.3,
  RF.2.3 and RF.2.3d). The frames' foundations clause permits it; each scope and sequence should name the completing
  day, as grade 2 does.
- **Readiness wording.** Grade 1 labels day 1 readiness; grades 1 and 2 frames carry stale readiness words. Grade 2's
  sequence is the model.
- **Hand-off, K to grade 1.** Kindergarten hears long vowels only; grade 1 teaches silent e and the vowel teams and
  retrieves the K rows on day 1. Sound.
- **Hand-off, grade 1 to grade 2.** Grade 2 cycles 1 to 5 review grade 1's syllable types and teams (ai, ay, ee, ea,
  igh, ie, oa, ow) and day 1 retrieves the e1 rows by id. Sound, with one gap: grade 1 drops "ou" from its cycle 11
  (grade 1 finding 3). If it is restored, grade 2's cycle 7 (oi, oy, ou, ow) stays review plus new, as the base
  designs it; if not, grade 2's unit 2 plan must teach ou as new in cycle 7.
- **Hand-off, grade 2 to grade 3.** Day 160 records the hand-off with independent and supported reading apart, which
  answers the lens line on grade 3 assuming unfinished foundations.
- **Shorter period.** Only kindergarten gives a minute budget; grades 1 and 2 should match it.
- **Source-map schemas differ** in all three (K: base, source_lesson, course_unit, course_day; grade 1: source,
  edition, block, module, base_unit, cycle, lesson, stretch, day; grade 2: source, block, base_module, base_unit,
  base_cycle, base_lesson, stretch, day). Pick one for the band so tools and readers can compare them (low).
