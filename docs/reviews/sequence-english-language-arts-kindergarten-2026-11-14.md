# Expert read: scope and sequence of English Language Arts, Kindergarten

Course `english-language-arts-kindergarten`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of the Codex read of the same course, which was not
opened. The grade 2 report closes the band and carries "Across the band".

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md (rules 1 to 11, including the two rules added after this course was written).
- Cold: docs/courses/english-language-arts-kindergarten/scope-and-sequence.md, data/plans/english-language-arts-kindergarten/days.csv
  (160 rows, every goal, code list, assess value and the notes of the assessment and course days) and
  source-map.csv (344 rows).
- Beside them: the frame (docs/courses/english-language-arts-kindergarten/frame.md); the kindergarten rows of
  data/plans/ela-texts.csv; docs/courses/CALENDAR.md and the grade K rows of the calendar; the EL Education K-5 base
  (S:\CurioClass-sources\el-education-k5-2017): the kindergarten module lessons that are assessments, and the K
  Skills Block cycle overviews, read for ideas only; for REPEAT tags, docs/reviews/frame-english-language-arts-kindergarten-2026-11-14.md,
  frame-ela-k-2-fixes-2026-11-14.md and progression-ela-2026-11-13.md; the science and social studies sequence reads
  of this date for the standard ("Settled by the expert", "Across the band").
- Gates: `plan.py check` passes this course and its frame (0 failures). `frame.py calendar`: ELA checks in weeks 16
  and 32 (math 17 and 31, science 14 and 29, social studies 15 and 30), no stagger break; the nearest one-to-one
  check gaps to math are 6 and 5 school days, so the rule holds at its edge. `stale.py check`: 56 files, 0 failures.

## Verdict

The plan is sound in its spine: every base lesson is placed in order, the foundations run the Skills Block's cycles
with daily practice and matched decodables, the texts are all placed, and the calendar and leans hold. What fails is
the assessment shape: the same adult hears every child one-to-one on the same letter, sound and decoding codes twice
within a few days (day 76 then day 77; day 156 then day 158), and several end days ask for full performances on many
expectations at once, which the new end-days rule forbids. Fix those two and lighten the observation load, and the
course is ready for unit plans.

## Findings, most serious first

### 1. Cumulative foundations evidence is collected twice, one-to-one, within days (serious; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 76 (kind Respond, assess observe) gathers RF.K.1a to d, L.K.1a, RF.K.3a, L.K.2c and
  RF.K.2a to c; the mid-year check on day 77 checks the same codes again. Day 156 observes RF.K.3b, RF.K.3d, RF.K.4,
  RF.K.3c and L.K.2d; the year-end check on day 158 checks the same set two days later.
- **Why it matters.** In kindergarten this evidence is heard one child at a time. Doing it twice costs roughly two
  extra class days of an adult's time per window, the second reading tells the teacher nothing new, and the children
  who need the time most wait longest.
- **Fix (days.csv days 76 and 156; scope and sequence, units 2 and 4 assessment paragraphs).** Drop the cumulative
  letter, sound and decoding observation from days 76 and 156. Those days keep only the unit's own small-group cycle
  check and the response. The course check (days 77 and 158) carries the one-to-one evidence for the continued rows,
  and the unit's end-of-unit record cites it.
- **Confidence.** Firm (from the code lists).

### 2. End days pile many full performances onto one day (serious; firm)

LAYER sequence. REPEAT new (the rule was added after the course was written).
- **What is wrong.** Day 32 asks for 14 codes (book types, parts and creators, group reading, L.K.5a to d, L.K.6,
  RL.K.1, RL.K.7); day 33 for 9 (individual print, letter, sound and rhyme evidence plus W.K.1); day 74 for 16
  (retell, word meaning L.K.4a and b, grammar L.K.1b to e, SL.K.4 to 6, phonemes RF.K.2d and e); day 76 for 11;
  day 156 for 15. Each asks for full performances on two or more expectations.
- **Why it matters.** Five-year-olds cannot give that much in one day, and one adult cannot hear it. The new
  end-days rule exists for exactly this case.
- **Fix (days.csv; scope and sequence assessment paragraphs).** Spread the performances over each unit's last
  teaching days in small-group rotations. Unit 2: phonemes into the cycle 10 and 11 foundations rotations on days 70
  to 73; grammar observed during drafting on days 70 and 71; retell in the day 64 response. Unit 1: concepts of
  print and book parts on days 28 to 31 in groups; W.K.1 on its own day. Unit 4: day 156 keeps one expectation after
  finding 1, the rest moves to days 150 to 154.
- **Confidence.** Firm.

### 3. The observation load is about a quarter of the year (moderate; likely)

LAYER sequence. REPEAT yes (the science and social studies K reads of this date found the same pattern).
- **What is wrong.** About 34 unit days carry an assess value, plus 4 course check days: units 1 and 3 are each
  about 27 percent assessment days. Much follows the base text, but days 28 to 33 add observation beyond the base's
  own assessment lessons (M1U3 L9 and 10, the performance task L11 and 12).
- **Why it matters.** Whole check days in kindergarten displace teaching; the base embeds most of its observation in
  teaching lessons.
- **Fix (days.csv, scope and sequence).** Where the base lesson teaches, mark the observation as embedded: the small
  group format with a per-child record, as the science reads settled, on a teaching day, not a Check day. Keep whole
  Check days for the base's own assessment lessons.
- **Confidence.** Likely (the count is firm; how many become embedded is a unit plan call).

### 4. Rows owned in one unit and completed in a later one (low; firm)

LAYER frame. REPEAT yes (the writer's own For the lead item 1).
- **What is wrong.** Unit 1 owns RF.K.1d, RF.K.3a and L.K.2c, which are completed in unit 2; RF.K.3b is completed in
  unit 4. The frame's "teaches it ... and checks it" sentence reads as if that cannot happen.
- **Fix.** No ownership change: the frame's foundations clause (each row sits where its first element is taught,
  later units say "continued") already permits it. The scope and sequence names, per continued row, the completing
  day (77 or 158). The frame's "Where a row sits" sentence gets a one-line foundations exception (frame wording,
  the lead's fix pass).
- **Confidence.** Firm.

### 5. Printed blending starts late (low; judgment call)

LAYER base text. REPEAT new.
- **What is wrong.** Printed VC and CVC blending begins on day 85 (week 17), though eight letters are known by day 32
  and all 26 by day 75. This is the base order.
- **Fix.** Optional: a unit plan may add short printed VC and CVC blending with taught letters from cycle 5. Leaving
  the base order is defensible.
- **Confidence.** Judgment call.

### 6. Day 76 responds to evidence it gathers itself (low; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 76 is kind Respond and also observes. A response day should answer evidence already in hand.
- **Fix.** Finding 1 removes most of the observation; mark any left on day 75 and keep day 76 a pure response.
- **Confidence.** Firm.

## What the two new rules change

- **Readiness counts by grade number.** Nothing: kindergarten has no earlier grade, and no day is marked readiness.
- **End days.** Days 32, 33, 74, 76 and 156 change (finding 2), helped by finding 1.

## Judged items the brief named

- **Texts against the catalogue.** 21 rows (8 anchors, 4 literary and 4 informational; 8 on file, 12 to write, 1 to
  choose), every one placed in days.csv; gk-u3-04 and gk-u3-07 are used once each. The scope and sequence counts
  match. Met.
- **Source map against the base.** Every base lesson is placed, in order (keep 283, ours 39, cut 20, merge 2); Labs
  cut with a reason; third-party items cut; decodables mapped. Met.
- **Foundations order.** The K Skills Block cycles in order with daily practice, matched decodables and a cycle check
  each cycle. Met (finding 5 is optional).
- **Readiness timing, timers, one device and paper path, day totals.** As settled; nothing raised.
- **Calendar and leans.** Met; the shorter-year flag on the calendar is correct.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Phonics scope and sequence present and tied to decodables | Met |
| A pattern used in decodable text before it is taught | Met (none found) |
| Unit named by a topic and its texts | Met |
| Anchor texts on file, measured, with a reason for their place | Part: 12 to write, measures follow the texts |
| Texts lean to one kind | Met: 4 literary and 4 informational anchors |
| Long text read whole | n/a at K (read-aloud whole books) |
| Research and full-process writing more than once | Met |
| Formal discussion often | Met |
| End task joins reading with writing or speaking on the topic | Met |
| Sensitive content has a teacher note and a sensitivity read | Met |

## What is right and should not be touched

- The base order kept lesson by lesson, with the Labs hour cut for the two-hour day.
- The mid-year retell on The Magic Bow (unit 1) rather than a unit 2 story: it avoids re-testing the just-assessed
  text. Kept.
- The shorter path: a specific 100-minute budget and 10 fold-ins, none assessed.

## What I could not judge

- Text demand: most texts are still to write.
- Whether 120 minutes is real in a kindergarten day: settled by Cory, not judged.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Days 76 and 156 drop cumulative foundations observation | The course check two days on carries it | days.csv; scope-and-sequence.md |
| End-day performances spread over the last teaching days in groups | New end-days rule | days.csv days 28 to 33, 64 to 76, 150 to 156 |
| Observation embedded on base teaching days, per-child record | Same as the science and social studies K reads | days.csv |
| No ownership change for continued foundations rows; name the completing day | Frame foundations clause | scope-and-sequence.md |
| Mid-year retell on The Magic Bow | Fresh to the unit 2 assessment | days.csv day 78 |
| Printed blending left in base order (optional earlier start) | Base order is defensible | n/a |

The frame wording in finding 4 is the lead's fix pass, not settled here.

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- Common Core State Standards for ELA, kindergarten (data/standards/ccss-ela-standards-full.txt).
- EL Education K-5 Language Arts (2017), kindergarten modules and K Skills Block, read for ideas only.
- National Reading Panel (2000) and the WWC foundational skills guide (2016), from memory, for systematic phonics.

## For the source list

None.
