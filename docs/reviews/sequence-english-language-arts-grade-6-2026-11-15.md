# Expert read: scope and sequence of English Language Arts, Grade 6

Course `english-language-arts-grade-6`. Cold read, 2026-11-15, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Read as it stands after Codex's reconcile; no reconcile report and no
Codex read was opened. First of the grade 6 to 8 band; the band section is in the grade 8 report.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md (rule 2 collect once and end days, rule 3 course checks, rule 8 source map).
- Cold: docs/courses/english-language-arts-grade-6/scope-and-sequence.md; data/plans/english-language-arts-grade-6/days.csv
  (160 rows: goals, codes, assess values and the notes of every assessment, course and respond day).
- Beside them: the frame; the g6 rows of data/plans/ela-texts.csv (g6-u1-01 to g6-u6-08); data/progressions/ela.csv
  (e5 and e6 rows and their assumes cells); data/plans/calendar.csv; the grade 5 and grade 4 days for the hand-off
  and the root inventory; the grade 5 expert read of 2026-11-15 for its band findings.
- Gates: `plan.py check` exits 0; `sequence.py check` for this course, 0 failures; `stale.py check`, 56 files, 0
  failures. `frame.py calendar`: ELA checks in weeks 12, 22 and 32 (math 16, 24, 32; science 18, 32; social studies
  15, 23, 32), no mid-year clash. A Codex run is writing other courses at the same time.

## Verdict

A careful sequence: the whole novella, two research projects, formal discussion at most every ten days, nine pieces
at three of each type, honest text records and real-date bridges. Its serious fault comes from a good change: the
units now end inside their own days, but the course checks kept the frame's content, so all three checks repeat a
task form the unit gave three to nine days before. Unit 2 gives the same cold set three times in fifteen days, two
end days stack talks with a full piece, and morphology lives in one unit and reteaches graph a third year. Fix
findings 1 to 3 and it is ready.

## Findings, most serious first

### 1. Every course check repeats a form the unit just gave (serious; firm)

LAYER sequence. REPEAT new (the collect-once rule reached the brief after this course was written).
- **What is wrong.** Check 1 day 60 is a cold editorial and recorded claim on RI.6.8 and SL.6.3, three days after
  day 57's cold rule article, editorial and recorded statement on the same codes. Check 2 day 109 is a cold script
  profile and chapter on RI.6.3, RI.6.5, L.6.4a to d, L.6.5b and L.6.2, three days after day 106 gave the same
  form and codes; day 110 asks an informative piece with a chart ten days after I2 on day 100. Check 3 day 158 is a
  cold set of accounts with a display and a heard explainer, six days after day 152's same form, plus a W.6.1a and
  b argument nine days after A3 on day 149.
- **Why it matters.** The brief now says a course-level check never repeats a task form given in the last two
  weeks, and a check within ten days reuses the record. Each repeat costs a period of a 160-day year and tells the
  teacher nothing the unit record did not; it also turns the check into a second end of the unit, the K to 5 fault
  of a course check repeating the unit's essay a week later.
- **Fix (days.csv days 59 to 62, 109 to 112, 157 to 160; scope and sequence "Course-level checks").** Each check
  reuses the just-ended unit's record for those codes and spends its items on earlier units' rows in a form the
  last two weeks did not use. Check 1: day 59 stays (RL.6.1 to 6.3, RI.6.1, RI.6.2 on unit 1 content); day 60
  drops the editorial and recorded claim and takes L.6.1 and L.6.2 sentence editing on a cold unit 1 passage plus a
  short W.6.9 evidence paragraph. Check 2: day 109 reuses day 106 for RI.6.3, 6.5 and L.6.4 and instead reads a
  cold argument on the unit 2 topic for RI.6.8; day 110's writing becomes a short argument (W.6.1 last assessed in
  the A2 product on day 56). Check 3: day 157 stays; day 158 drops the repeated accounts form and the argument,
  reuses days 149 and 152, and asks an informative explanation on unit 3 or 4 content (W.6.2 last assessed day 100).
  Changing what a check checks is a call for the lead.
- **Confidence.** Firm.

### 2. Unit 2 gives the same cold set three times in fifteen days (moderate; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** The mid-unit assessment on day 45, the end on day 57 and check 1 day 60 all ask a cold rule
  article, an editorial and a recorded statement on RI.6.2, 6.4, 6.6, 6.8, SL.6.3 and L.6.6. Unit 1 has the same
  shape on a smaller scale: the pilot slice check on day 6 and the mid on day 15 are the same form nine days apart.
- **Why it matters.** The mid should tell the teacher what to teach next, not rehearse the end; three like sittings
  read as test preparation and spend about two periods.
- **Fix (days.csv days 6, 15, 45; scope and sequence units 1 and 2).** Day 45 samples only the rows taught by then
  (RI.6.2, RI.6.4, L.6.6) on one cold article, with the editorial and recording left to day 57. Day 15 reuses the
  day 6 record for the codes day 6 took and samples only what was taught since. Finding 1 removes the day 60 repeat.
- **Confidence.** Firm.

### 3. Two end days stack a performance with a full piece (moderate; firm)

LAYER sequence. REPEAT yes (the K to 5 overloaded end days).
- **What is wrong.** Day 84 finishes the unit 3 talks and also asks a full W.6.2a to f cold explanation with a chart,
  which duplicates the report collected on day 81. Day 152 finishes the unit 6 talks and asks the cold accounts task.
- **Why it matters.** The end-days rule: no one end day asks for full performances on two or more expectations. A
  class still presenting cannot also write a cold full piece in 50 minutes.
- **Fix (days.csv days 84 and 152).** Day 84 drops the cold explanation; the day 81 report carries W.6.2a to f. Day
  152 keeps the talks only; the cold accounts task moves to day 153, the first unit 6 day after the talks.
- **Confidence.** Firm.

### 4. Graph is retaught a third year, and morphology lives in one unit (moderate; firm)

LAYER sequence and progression. REPEAT yes (the K to 5 roots retaught).
- **What is wrong.** Unit 4 teaches graph, gram, script, scrib, phon and glyph on day 90; graph was taught in grades
  4 and 5 (photo and graph in both). If the band list in the grade 5 read is adopted (grade 4 holds scrib), scrib is
  retaught too. Outside unit 4, word parts return only on day 147.
- **Why it matters.** L.6.4b asks for Greek or Latin affixes and roots as clues, used on new words across the year.
  One unit with a revisit leaves five months with no word-part work and spends grade 6 time on known parts.
- **Fix (days.csv day 90 and the weekly sentence slots; scope and sequence vocabulary section).** Day 90 retrieves
  graph and scrib in two minutes and teaches gram, phon, glyph and new grade 6 parts (aud, ject, tract or the L.6.4b
  examples audience, auditory, audible). Each week from unit 2 on, a three-minute word-part retrieval inside the
  existing sentence slot uses a word from that week's anchor. No day is added.
- **Confidence.** Firm.

### 5. The novella is shorter than grade 5's novel, and the frame says it climbs (moderate; firm)

LAYER frame. REPEAT new.
- **What is wrong.** The frame says the novella was lengthened "so the band's whole texts climb" from grade 5's
  novel. Grade 5's novel is 30,000 to 40,000 words with a 15,000 to 20,000-word biography read whole; grade 6's
  novella is 25,000 to 30,000, and grade 6 has no long informational work read whole.
- **Why it matters.** The rubric wants text demand to rise; a dip at the door of middle school, under a sentence
  that says the opposite, will mislead the writer.
- **Fix (frame unit 1; scope and sequence unit 1 text record).** Set the novella at 35,000 to 40,000 words, which
  fits days 1 to 25 at the stated reading budget, or correct the sentence. Give unit 3's forecasting explainer set
  one long whole informational piece. The lead decides the frame change.
- **Confidence.** Firm on the numbers; the length is a judgment call.

### 6. Grade 5's spring records are not picked up (low; firm)

LAYER sequence. REPEAT yes (the grade 5 hand-off).
- **What is wrong.** Grade 5 day 160 hands on a word-part record and runs spring oral-reading checks on days 157 and
  158. Grade 6 days 7 to 10 collect one-minute samples from every child again and never name the word-part record.
- **Fix (days.csv days 7 to 10 and 90; scope and sequence fluency paragraph).** Days 7 to 10 sample only students
  with no grade 5 record or a flagged one. Day 90 starts from the word-part record.
- **Confidence.** Firm.

### 7. Retrieval waits for the last ten minutes of unit ends (low; likely)

LAYER sequence. REPEAT new.
- **What is wrong.** Every assumed e5 row is retrieved in the last ten minutes of days 32, 62, 86, 112 and 136; day
  86 holds about six rows in ten minutes.
- **Fix (days.csv).** Move each retrieval to the first day the row is used, as grade 8 does; keep the unit-end slot
  for what is left.
- **Confidence.** Likely.

### 8. Small slips (low; firm)

LAYER frame and sequence. REPEAT yes (stale frame wording, as in K to 5).
- The frame still says "readiness tasks" for grade 5 rows and treats the check after units 2, 4 and 6 as the unit's
  end; the sequence rightly follows the brief. The frame's unit 6 candidate placement is also stale. Fix the frame
  wording at the next frame touch.
- Day 6 has kind Check and a blank assess value; give it `mid` or, after finding 2, practice.
- Anchor share: 23 anchors, 52.2 percent informational, depends on counting eight poems and four explainer parts
  one by one; by register row it is 66.7 percent. Name one denominator (see the grade 8 band section).

## What the collect-once rule changes

- Checks 1, 2 and 3: days 60, 109, 110 and 158 (finding 1). Days 59 and 157 are clear: day 157's poem and story
  come 23 days after day 134.
- Unit 1 day 15 reuses day 6; unit 2 day 45 narrows (finding 2).
- Days 7 to 10 reuse the grade 5 oral-reading record (finding 6), the one-to-one evidence the rule names first.
- Readiness by grade number changes nothing: every assumed row is e5 and is used in grade 5, so retrieval is right.

## Judged items the brief named

- **Texts against the catalogue.** Every id in the sequence (g6-u1-01 to g6-u6-08) is in ela-texts.csv with the
  same use; most are "to write" or "to choose"; King, Stevenson, Rossetti and Cline are on file. The free long-book
  options are old public-domain titles, rightly flagged as a resource question. Met.
- **Source map.** The frame names no base; no source-map.csv is required. Met.
- **Argument, research, literary analysis.** Three arguments climbing from claim to supported claim; two research
  projects, the first taught on unit 3's sittings and used again in unit 6; daily W.6.9 paragraphs and a literary
  response on the novella. Met.
- **Complexity and balance.** Finding 5 and finding 8.
- **Vocabulary and morphology from grade 5.** Finding 4 and finding 6.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Unit named by a topic and its texts | Met |
| Anchor texts on file, with a reason for their place | Part: to write; provisional records given |
| Long text read whole | Met (the novella); no long informational whole (finding 5) |
| Text complexity rises from the grade before | Not met (finding 5) |
| About 55 informational, 45 literary | Met by one count, not by another (finding 8) |
| Writing about 35/35/30 | Met (three of each type) |
| Research taught, then used | Met (units 3 and 6) |
| Formal discussion often | Met (at most every ten days) |
| End task joins reading with writing or speaking | Met |
| Morphology across the year | Not met (finding 4) |
| Sensitive content has a teacher note | Met |

## Brief's other checks

- **Order.** Sound: novella, Hammurabi, forecasting research, writing systems, storm poems and play, Galveston.
- **Assessments.** Every unit has a mid where over 25 days (units 1 and 2) and an end inside its days. Findings 1 to 3.
- **Readiness and retrieval.** All e5; retrieval right; placement finding 7.
- **Checks that do not repeat.** Finding 1.
- **Standards in full.** Lettered parts listed; no gap found.
- **Days by load.** Sound; 32, 26, 24, 22, 24, 20 match the frame.
- **Calendar and leans.** Weeks 12, 22, 32 meet CALENDAR.md; no stagger clash.
- **Candidate cells.** Placed inside existing days; none adds a day.
- **Shorter path.** Given (40-minute period and ten fold-in days).
- **Source map.** Not applicable.
- **Stale notes.** Finding 8.

## What is right and should not be touched

The whole novella, discussion at most every ten days, the two research projects, the protected typing sittings,
the real-date bridges to social studies and science, and text records that say what is unwritten.

## What I could not judge

- Text demand: the anchors are unwritten and unmeasured.
- Whether the free long-book options are good enough for a grade 6 reading room.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 15 reuses day 6; day 45 samples only rows taught by then | Collect once; mid is not a rehearsal | days.csv; scope-and-sequence.md |
| Day 84 drops the cold explanation; day 152's accounts task moves to day 153 | End-days rule | days.csv |
| Day 90 retrieves graph and scrib and teaches new parts; weekly three-minute word-part slot | No reteaching | days.csv; scope-and-sequence.md |
| Days 7 to 10 sample only students without a grade 5 record | Collect once | days.csv |
| Retrieval moves to first use | Retrieval at point of need | days.csv |
| Day 6 assess value set | Data | days.csv |

Check content (finding 1) and the novella length (finding 5) are calls for the lead.

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- Common Core State Standards for ELA, grade 6 (data/standards/ccss-ela-standards-full.txt).
- docs/RUBRIC-ELA.md and the grade 5 expert read of 2026-11-15.

## For the source list

None.
