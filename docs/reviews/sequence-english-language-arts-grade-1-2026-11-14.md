# Expert read: scope and sequence of English Language Arts, Grade 1

Course `english-language-arts-grade-1`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of the Codex read of the same course, which was not
opened. The grade 2 report closes the band and carries "Across the band".

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md (rules 1 to 11).
- Cold: docs/courses/english-language-arts-grade-1/scope-and-sequence.md, data/plans/english-language-arts-grade-1/days.csv
  (160 rows: goals, skills, codes, assess values and the notes of the assessment and course days) and source-map.csv
  (372 rows).
- Beside them: the frame; the grade 1 rows of data/plans/ela-texts.csv; docs/courses/CALENDAR.md; the EL Education
  K-5 base: the grade 1 module assessment lessons, the M2U1 and M2U2 lessons, and the grade 1 Skills Block cycle
  overviews (cycle 11 in particular), for ideas only; the kindergarten scope and sequence for the hand-off; for REPEAT
  tags, docs/reviews/frame-english-language-arts-grade-1-2026-11-14.md, frame-ela-k-2-fixes-2026-11-14.md and
  progression-ela-2026-11-13.md.
- Gates: `plan.py check` passes this course and its frame (0 failures). `frame.py calendar`: ELA checks in weeks 16
  and 32 (math 19 and 30), no stagger break; nearest one-to-one gaps to math 16 and 10 school days. `stale.py check`:
  0 failures.

## Verdict

A careful sequence: the base topic lessons and all 130 Skills Block lessons are kept in order, foundations and
fluency appear every day, the science and social studies leans have their bridges, and later units open with
retrieval as the new rule wants. Three things need fixing: the year-end foundations evidence is collected one-to-one
twice in three days (day 155, then day 158), four end days stack full performances against the new end-days rule,
and cycle 11 drops "ou", which the base teaches there and the course's own readers will contain. Day 1's readiness
label also needs renaming under the count-by-grade rule.

## Findings, most serious first

### 1. Cumulative foundations evidence is collected twice, one-to-one, within days (serious; firm)

LAYER sequence. REPEAT yes (finding 1 of the kindergarten read, this date).
- **What is wrong.** Day 155 observes a full cumulative foundations performance (24 codes: RF.1.2, RF.1.3a to g,
  RF.1.4a to c, L.1.2d and e and more). The year-end check on day 158 repeats the full phonics read and spell three
  days later. The scope and sequence's "earlier sky and bird-body contexts" does not stop the repeat, because
  phonics skills are context-free. The same happens mid-year on a smaller scale: day 72 observes inflections and
  L.1.2d and e; day 76 checks RF.1.3f and L.1.2d and e again.
- **Why it matters.** One adult hears each child twice for no new information, about two class days of teacher time
  each window, in a grade where every other block also needs small groups.
- **Fix (days.csv days 72 and 155; scope and sequence unit 2 and 4 assessment paragraphs).** Day 155 becomes a small
  group check of the cycle 19 to 25 patterns only; day 72 keeps the cycle check of its own patterns. The full
  cumulative one-to-one stays in the course checks (days 76 and 158), which the unit 2 and unit 4 end-of-unit
  records cite for RF.1.3 and RF.1.4.
- **Confidence.** Firm.

### 2. End days stack full performances (moderate; firm)

LAYER sequence. REPEAT new (the rule was added after the course was written).
- **What is wrong.** Day 31: 19 codes, full foundations and fluency for every child plus editing. Day 33: 12 codes
  (the W.1.2 piece, SL.1.1a to c, SL.1.3, L.1.5a to d, L.1.6, plus the response). Day 155: 24 codes. Day 156: 14
  codes (all of L.1.1a to j, RL.1.9, RI.1.9 and a W.1.1 transfer).
- **Fix (days.csv; scope and sequence).** Spread them: unit 1, foundations across days 27 to 31 rotations, the W.1.2
  piece on its own day, L.1.5 observed in the word work of days 29 and 30; unit 4, grammar observed on editing days
  150 to 152, comparison on 153 and 154 (its fold-in work), foundations across 150 to 155 rotations after finding 1.
- **Confidence.** Firm.

### 3. Cycle 11 drops "ou" against the base order (moderate; firm)

LAYER base text. REPEAT new.
- **What is wrong.** The base's grade 1 cycle 11 introduces "ou" (out, cloud, found) beside the final blends. The
  scope and sequence omits it, saying the frame leaves it to grade 2; the frame does not say so. Later grade 1
  readers adapted from the base will hold ou words.
- **Why it matters.** A decodable with an untaught pattern is the lens's K to 2 error; children meet "out" and
  "found" with no mapping, or the readers must be rewritten.
- **Fix (item level, within RF.1.3).** Restore "ou" in cycle 11 as the base teaches it. The alternative is a recorded
  cut in the source map plus a scan of every later adapted reader for ou words; restoring is cheaper and keeps
  grade 2's cycle 7 as review, as the base designs it.
- **Confidence.** Firm.

### 4. Day 1 is labelled readiness; by the count-by-grade rule it is retrieval (low; firm)

LAYER frame and sequence. REPEAT yes (the science and social studies reads found the same stale readiness wording
in their grade 1 and 2 frames).
- **What is wrong.** Day 1 carries `assess=readiness` as a "frame exception". Kindergarten rows are the year before,
  so they get retrieval, not a readiness check. The frame's "baseline readiness check" and "later units open with a
  short readiness check on any kindergarten row" are stale. Units 2 to 4 already use retrieval (days 34, 79, 120).
- **Fix.** Keep the ten-minute foundations placement screen; it is good practice. Name it the start-of-year
  placement screen with retrieval, and set the assess value accordingly. The frame wording is the lead's fix pass.
- **Confidence.** Firm.

### 5. The shorter period has no minute budget (low; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Kindergarten gives a specific 100-minute version; grade 1 says only what to trim.
- **Fix.** Give the same kind of budget (for example 45 topic and 55 foundations minutes) and name what each block
  drops. The ten shorter-year fold-ins are fine (none assessed).
- **Confidence.** Firm.

### 6. The end-of-unit response sits in the last 20 minutes of the observe day (low; judgment call)

LAYER sequence. REPEAT new.
- **What is wrong.** Days 33, 75, 119 and 157 hold both the last observation and the response. A child heard late
  that day has no response.
- **Fix.** Where the next day is in the same unit, the response takes its first minutes; otherwise finish the
  observation in the first half of the day.
- **Confidence.** Judgment call.

### 7. Two base assessment lessons are softened (low; likely)

LAYER base text. REPEAT new.
- **What is wrong.** Day 60 (base M2U2 L11) is a rehearsal, though the base's assessment is L11 and 12; the base's
  M4U3 assessment lessons 5 to 7 appear only as an observation on day 147.
- **Fix.** Either mark day 60 as the first part of the mid-unit assessment, or give the source map a reason for the
  change. Day 147 is acceptable if the source map says the evidence moves to the closing window.
- **Confidence.** Likely.

### 8. Catalogue rows lag the plan (low; firm)

LAYER sequence (catalogue). REPEAT new.
- **What is wrong.** g1-u4-05 is "to confirm"; its base title is "Birds as Human Helpers". The sky and bird poems are
  "to choose" in the catalogue, but the scope and sequence chooses Curio Class originals. g1-u1-04 is still "to
  choose".
- **Fix.** Update the catalogue title and statuses in the fix pass; choose g1-u1-04 before unit 1's plan.
- **Confidence.** Firm.

### 9. The frame's source map names the wrong base unit for the pourquoi tales (low; firm)

LAYER frame. REPEAT new.
- **What is wrong.** The frame says the tales replace texts in "Module 2, unit 2". The base's literary lessons are in
  M2U1 (RL lessons, retelling), its informational ones in M2U2. The scope and sequence correctly puts the tales on
  days 36 to 48 (M2U1 lessons).
- **Fix.** Frame wording: "Module 2, unit 1".
- **Confidence.** Firm (checked in the base lessons).

## What the two new rules change

- **Readiness counts by grade number.** Day 1's readiness label becomes retrieval with a placement screen; the
  frame's readiness wording goes (finding 4). Later units already comply.
- **End days.** Days 31, 33, 155 and 156 change (finding 2), helped by finding 1.

## Judged items the brief named

- **Texts against the catalogue.** 17 rows, all placed in days.csv; three catalogue lags (finding 8).
- **Source map against the base.** Topic keep 145, split 1, ours 7; foundations keep 130, ours 24 (consolidation);
  handwriting 26; readers 25; Labs and media cut 8 with reasons. In order. Met, except finding 3 and finding 7.
- **Foundations order.** Systematic and cumulative, daily, matched decodables, a cycle check each cycle. Met except
  "ou" (finding 3).
- **Readiness, timers, device and paper path, day totals.** As settled.
- **Calendar and leans.** Science 1-ESS1-1 and 1-LS1-1 are taught before ELA leans on them; the social studies lean
  has its bridge. Met.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Phonics scope and sequence present and tied to decodables | Met |
| A pattern used in decodable text before it is taught | Missed: "ou" (finding 3) |
| Unit named by a topic and its texts | Met |
| Anchor texts on file, measured, with a reason for their place | Part: most to write |
| Texts lean to one kind | Met |
| Long text read whole | Met |
| Research and full-process writing more than once | Met |
| Formal discussion often | Met |
| End task joins reading with writing or speaking on the topic | Met |
| Sensitive content has a teacher note and a sensitivity read | Met |

## What is right and should not be touched

- All 130 Skills Block lessons in order, with 24 consolidation blocks.
- Retrieval openings on days 34, 79 and 120.
- The fluency skill on every day.
- The pourquoi tales read in the M2U1 lessons.

## What I could not judge

- Text demand: most texts are unwritten.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Days 72 and 155 keep only their cycle checks; course checks carry the cumulative one-to-one | No repeated hearing | days.csv; scope-and-sequence.md |
| End-day performances spread over the last teaching days | New end-days rule | days.csv days 27 to 33, 150 to 157 |
| "ou" restored in cycle 11 | Base order; the readers hold ou words | days.csv cycle 11 days; source-map.csv |
| Day 1 named a placement screen with retrieval | Kindergarten is the year before | days.csv day 1 |
| Shorter period gets a minute budget | Match kindergarten | scope-and-sequence.md |
| g1-u4-05 titled "Birds as Human Helpers"; poems marked Curio Class original | Plan already chose | data/plans/ela-texts.csv |

The frame wording (findings 4 and 9) is the lead's fix pass, not settled here.

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- Common Core State Standards for ELA, grade 1 (data/standards/ccss-ela-standards-full.txt).
- EL Education K-5 Language Arts (2017), grade 1 modules and Skills Block, read for ideas only.
- National Reading Panel (2000) and the WWC foundational skills guide (2016), from memory.

## For the source list

None.
