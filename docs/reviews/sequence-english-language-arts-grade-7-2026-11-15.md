# Expert read: scope and sequence of English Language Arts, Grade 7

Course `english-language-arts-grade-7`. Cold read, 2026-11-15, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of any Codex read of this course, which was not opened.
The band section is in the grade 8 report.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md.
- Cold: docs/courses/english-language-arts-grade-7/scope-and-sequence.md; data/plans/english-language-arts-grade-7/days.csv
  (160 rows, with the notes of every assessment, course and respond day).
- Beside them: the frame; the g7 rows of data/plans/ela-texts.csv (g7-u1-01 to g7-u6-05); data/progressions/ela.csv
  (e6 and e7 rows); data/plans/calendar.csv; the grade 6 days, to confirm the hand-off.
- Gates: `plan.py check` exits 0; `sequence.py check` for this course, 0 failures; `stale.py check`, 0 failures.
  `frame.py calendar`: ELA checks in weeks 12, 22 and 32 (math 9, 24, 32; science 14, 32; social studies 13, 24, 32),
  no mid-year clash. A Codex run is writing other courses at the same time.

## Verdict

A sound year: the salmon novella read whole, research taught on the smallpox unit and used again on the Klamath,
argument that now acknowledges opposing claims, and formal discussion at most every ten days. The serious fault is
the one grade 6 has: each course check repeats a form the unit gave three to seven days before, now against the
collect-once rule. The unit 3 end repeats its mid, one end day stacks two performances, and word parts are taught
on one day. Fix findings 1 and 2 and it is ready.

## Findings, most serious first

### 1. Every course check repeats a form the unit just gave (serious; firm)

LAYER sequence. REPEAT yes (grade 6 finding 1; the K to 5 course check repeating the unit).
- **What is wrong.** Check 1 day 58 is a cold article on RI.7.1 to 7.3, three and four days after day 54 (RL.7.9 and
  RI.7.3 on a cold pair) and day 55 (RI.7.2, SL.7.2, L.7.1); RI.7.2 is assessed on days 43, 55 and 58. Check 2 day
  109 assesses RI.7.6 on cold smallpox articles four days after day 105's cold pair on RI.7.6. Check 3 day 158 asks
  RI.7.8 and SL.7.3 on a cold editorial and talk four and five days after days 153 (RI.7.5, RI.7.8) and 154 (SL.7.3
  hearing), and a W.7.1a and b argument seven days after the one-sitting argument on day 151.
- **Why it matters.** A course-level check never repeats a task form given in the last two weeks, and a check within
  ten days reuses the record. Each repeat spends a period for no new information.
- **Fix (days.csv days 58, 109, 158 and their respond days; scope and sequence "Course-level checks").** Day 58
  reuses days 54 and 55 for RI.7.2 and RI.7.3 and asks instead L.7.1 and L.7.2 sentence editing and a W.7.9 evidence
  paragraph on a cold unit 1 passage. Day 109 reuses day 105 for RI.7.6 and keeps RI.7.9 and RI.7.4 on smallpox
  (unit 3 ended day 84). Day 158 reuses days 151, 153 and 154, drops the editorial, talk and argument, and samples
  RI.7.2 and RI.7.3 (last day 58) on a cold unit 4 or 5 informational text with a short W.7.2 explanation. Changing
  what a check checks is a call for the lead.
- **Confidence.** Firm.

### 2. The unit 3 end repeats its mid eleven days later (moderate; firm)

LAYER sequence. REPEAT yes (grade 6 finding 2).
- **What is wrong.** The mid on day 73 assesses RI.7.9, RI.7.4, L.7.4a to d, L.7.5b and L.7.6 on cold smallpox
  articles; the end on day 84 assesses the same codes in the same form.
- **Why it matters.** The mid should steer teaching, not rehearse the end; eleven days is one day past the
  reuse window and gives the teacher little new.
- **Fix (days.csv day 73).** Day 73 samples RI.7.4 and L.7.4a to d only, the rows taught by then; RI.7.9 and L.7.6
  wait for day 84.
- **Confidence.** Firm on the repeat; the split is a judgment call.

### 3. Day 29 stacks an observed discussion with a cold response (moderate; firm)

LAYER sequence. REPEAT yes (the K to 5 overloaded end days).
- **What is wrong.** Unit 1's end runs day 27 (cold two-view story), day 28 (narrative product) and day 29 (observed
  discussion, a fresh nonfiction response and the log), two full performances on one day.
- **Fix (days.csv days 29 and 30).** Day 29 keeps the observed discussion; the nonfiction response moves to day 30's
  first half, with the response to days 27 to 29 in its second half. No day added.
- **Confidence.** Firm.

### 4. Word parts are taught on one day (moderate; firm)

LAYER sequence and progression. REPEAT yes (grade 6 finding 4).
- **What is wrong.** L.7.4b (Greek or Latin affixes and roots) is taught on day 65 with vacca, immunis, epi, demos,
  pan and logy, and not returned to. Grade 6's parts are not retrieved.
- **Why it matters.** One day does not make roots a clue students reach for in cold reading; the standard and the
  rubric expect use across the year.
- **Fix (days.csv day 65 and the weekly language slots; scope and sequence vocabulary section).** Day 65 opens with a
  two-minute retrieval of grade 6's gram, phon and script; a three-minute weekly word-part slot from unit 3 on uses
  a word from that week's anchor (demos in unit 4, logy in unit 6). No day added.
- **Confidence.** Firm.

### 5. The anchor balance may lean literary once the bundles are opened (moderate; judgment call)

LAYER sequence. REPEAT new.
- **What is wrong.** By register row the anchors are seven informational and five literary (58 percent). Opened into
  works, the poem and play sets give twelve literary against six informational originals plus federal pages whose
  count is not stated, so the informational share is unknown and could fall under half.
- **Why it matters.** The rubric for grades 6 to 8 asks about 55 percent informational; the count should be checkable.
- **Fix (scope and sequence anchor counts).** Give both counts, by record and by work, as grade 8 does, and name the
  federal pages placed as anchors. The lead reconciles the band denominator.
- **Confidence.** Judgment call.

### 6. The grade 6 hand-off is marked unverified, and it is now verifiable (low; firm)

LAYER sequence. REPEAT yes (the grade 5 read's finding 5).
- **What is wrong.** The sequence says grade 6's days.csv was absent, so last uses are unverified. It exists; every
  e6 row is used there (the fewest: e6-read-vs-watch 4 days, e6-compare-genres 6, e6-pronouns 6).
- **Fix (scope and sequence prerequisites).** Mark the retrieval placements confirmed.
- **Confidence.** Firm.

### 7. Stale frame wording (low; firm)

LAYER frame. REPEAT yes.
- The frame says "readiness tasks" for grade 6 rows, treats the check after units 2, 4 and 6 as the unit's end, and
  says no run is longer than 48 unit days; units 1 and 2 run 56. The sequence flags the last. Fix at the next frame
  touch.

## What the collect-once rule changes

- Days 58, 109 and 158 (finding 1). Days 57 (30 days after day 27's two-view story) and 157 (26 days after unit 5's
  end) are clear.
- Day 73 narrows (finding 2).
- Readiness by grade number changes nothing: all assumed rows are e6 and used in grade 6 (finding 6).

## Judged items the brief named

- **Texts against the catalogue.** Every id in the sequence (g7-u1-01 to g7-u6-05) is in ela-texts.csv with the same
  use and status. Source map: no base named, none required. Met.
- **Argument, research, literary analysis.** Arguments acknowledge opposing claims (W.7.1a); research taught in unit
  3 with standard citation, used again in unit 6; daily W.7.9 paragraphs. Writing by piece is a third each; by
  composition day 29/39/32, argument a little light against 35 but inside a reasonable band. Met.
- **Complexity and balance.** Novella 30,000 to 35,000 words, above grade 6. Balance finding 5.
- **Vocabulary and morphology.** Finding 4.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Unit named by a topic and its texts | Met |
| Anchor texts on file, with a reason for their place | Part: to write or to choose |
| Long text read whole | Met (the novella) |
| Text complexity rises from the grade before | Met |
| About 55 informational, 45 literary | Unclear (finding 5) |
| Writing about 35/35/30 | Met by piece |
| Research taught, then used | Met |
| Formal discussion often | Met |
| End task joins reading with writing or speaking | Met |
| Morphology across the year | Not met (finding 4) |
| Sensitive content has a teacher note | Met |

## Brief's other checks

- **Order.** Sound: novella, Dust Bowl, smallpox research, Athens, marathon poems and play, Klamath.
- **Assessments.** Mids in units 1 to 3 (over 25 days); ends inside each unit. Findings 1 to 3.
- **Readiness and retrieval.** All e6; finding 6.
- **Checks that do not repeat.** Finding 1.
- **Standards in full.** Lettered parts listed; no gap found.
- **Days by load.** 30, 26, 26, 22, 22, 22 as framed.
- **Calendar and leans.** Weeks 12, 22, 32 meet CALENDAR.md.
- **Candidate cells.** Inside existing days.
- **Shorter path.** Given.
- **Source map.** Not applicable.
- **Stale notes.** Findings 6 and 7.

## What is right and should not be touched

The whole novella, the research cycle with real source judgment, the move from supported claims to acknowledged
opposing claims, discussion every ten days, and the honest text records.

## What I could not judge

- Text demand: anchors unwritten and unmeasured.
- The federal pages' count until they are chosen.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 73 samples RI.7.4 and L.7.4 only | Mid is not a rehearsal | days.csv |
| Day 29's nonfiction response moves to day 30 | End-days rule | days.csv |
| Day 65 retrieves grade 6 parts; weekly word-part slot | Morphology across the year | days.csv; scope-and-sequence.md |
| Grade 6 hand-off marked confirmed | The grade 6 days exist | scope-and-sequence.md |
| Anchor counts given both ways | Checkable balance | scope-and-sequence.md |

Check content (finding 1) and the band anchor denominator (finding 5) are calls for the lead.

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- Common Core State Standards for ELA, grade 7 (data/standards/ccss-ela-standards-full.txt).
- docs/RUBRIC-ELA.md.

## For the source list

None.
