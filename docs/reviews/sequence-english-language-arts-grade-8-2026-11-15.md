# Expert read: scope and sequence of English Language Arts, Grade 8

Course `english-language-arts-grade-8`. Cold read, 2026-11-15, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of any Codex read of this course, which was not opened.
This report closes the grade 6 to 8 band, so it ends with "Across the band".

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md.
- Cold: docs/courses/english-language-arts-grade-8/scope-and-sequence.md; data/plans/english-language-arts-grade-8/days.csv
  (160 rows, with the codes and notes of every assessment, course and respond day, and every word-part day).
- Beside them: the frame; the g8 rows of data/plans/ela-texts.csv (g8-u1-01 to g8-u5-06); data/progressions/ela.csv
  (e7 and e8 rows); data/plans/calendar.csv; the grade 7 days, to confirm the hand-off; the grade 8 frame read of
  2026-11-14, only for the status of the RL.8.9 question.
- Gates: `plan.py check` exits 0; `sequence.py check` for this course, 0 failures; `stale.py check`, 0 failures.
  `frame.py calendar`: ELA checks in weeks 18, 25, 26 and 32 (math 14, 24, 32; science 15, 32; social studies 10,
  20, 29, 30), no mid-year clash. A Codex run is writing other courses at the same time.

## Verdict

The best of the three. Ends are spread over three or four days, each check moves to earlier units' topics,
independent reading is recorded once for literary (day 155) and once for informational (day 157), the argument
answers counterclaims, and the long nonfiction feature is read whole. It still breaks the new collect-once rule:
the sequence changed the checks' topics but not their forms, so check 2 day 125 and check 3 day 157 repeat what
days 121 and 147 asked days before. Every mid rehearses its end, and word parts are four whole words on one day.
Fix findings 1 and 2 and it is ready.

## Findings, most serious first

### 1. Two course checks, and part of a third, repeat a form the unit just gave (serious; firm)

LAYER sequence. REPEAT yes (grade 6 and 7 finding 1).
- **What is wrong.** Check 2 day 125 asks RL.8.9, RL.8.4 and RL.8.5 on a cold modern story, its source and
  contrasting forms, four days after day 121 asked the same codes on a cold retelling, source and poem and play
  extracts. Check 3 day 157 asks RI.8.7 and SL.8.2 on one story in two media ten days after day 147's cold article,
  recording and advertisement, and RI.8.5 and RI.8.3 four days after day 153's cold paragraph analysis. Check 1 day
  90 asks RI.8.2 (central and supporting ideas, summary) four days after day 86 asked it on a cold article. The
  sequence moved each check to an earlier unit's topic, which is right, but a new topic in the same form is still the
  same task form.
- **Why it matters.** A course-level check never repeats a task form given in the last two weeks, and a check within
  ten days reuses the record.
- **Fix (days.csv days 90, 125, 127, 157, 159; scope and sequence "Course-level checks").** Day 90 reuses day 86 for
  RI.8.2 and keeps RI.8.1, RI.8.9 and L.8.2 (last day 60). Day 125 reuses day 121 for RL.8.4 and RL.8.5 and asks
  RL.8.9 as one sustained W.8.9a literary-analysis piece comparing a modern story with its source on the unit 1
  topic, a form unit 4 did not use (its end was short responses); day 127 responds to it. Day 157 reuses days 147
  and 153, keeps the unseen RI.8.10 text with directions only, and adds RI.8.1 and RI.8.4 (last days 28 and 60) on
  it. Day 158 stays: its editorials, verbals and moods were last assessed on days 61 and 29. Changing what a check
  checks is a call for the lead.
- **Confidence.** Firm.

### 2. Every mid-unit assessment rehearses its end (moderate; firm)

LAYER sequence. REPEAT yes (grade 6 finding 2, grade 7 finding 2).
- **What is wrong.** Unit 3's mid on day 75 asks RI.8.2, L.8.4a to d and L.8.5b on a fresh federal paragraph; the
  end on day 86 asks the same codes on a cold article eleven days later. The other units do the same at 12 to 15
  days: day 15 and day 28 (RL.8.1, 8.2, 8.3, 8.6, RI.8.1), day 46 and days 60 to 61 (RI.8.4, 8.6, 8.8, 8.9, L.8.6,
  SL.8.3), day 108 and days 121 and 123 (RL.8.9, 8.4, 8.5, 8.7, L.8.5), day 141 and day 153 (RI.8.5, 8.3).
- **Why it matters.** Outside the ten-day reuse window, so not a breach, but each unit gives the same cold set twice;
  the mid should show what to teach next on the rows taught so far.
- **Fix (days.csv days 15, 46, 75, 108, 141).** Each mid samples the rows taught before it and, for broad codes, the
  existing draft, as the sequence already does for writing; the end carries the rest. Unit 3 is the one to change
  first: day 75 keeps RI.8.2 and research decisions, and L.8.4 and L.8.5b wait for day 86.
- **Confidence.** Firm on the pattern; the split is a judgment call.

### 3. Word parts are four whole words on one day (moderate; firm)

LAYER sequence and progression. REPEAT yes (grade 6 and 7 finding 4).
- **What is wrong.** Day 66 teaches L.8.4b through toxic, adulterate, pharmacy and preserve; days 75, 86 and 126
  assess it. No root or affix set is named, and no grade 6 or 7 part is retrieved.
- **Why it matters.** L.8.4b asks for Greek or Latin affixes and roots as clues (its own examples are precede, recede,
  secede). Whole words teach meanings, not a clue students can carry to a cold text on day 86 or 126.
- **Fix (days.csv day 66 and the weekly language slots; vocabulary section weeks 14 and 26).** Day 66 teaches tox,
  pharm, serv, ad- and ced from those words and the standard's examples, after a two-minute retrieval of grade 7's
  demos and logy; a three-minute weekly slot carries one part from the week's anchor. No day added.
- **Confidence.** Firm.

### 4. The anchors lean informational past the target (low; judgment call)

LAYER sequence. REPEAT new.
- **What is wrong.** 58.3 percent informational by record, 66.7 percent by work, against about 55. The sequence
  says so plainly and does not relabel.
- **Fix.** None in this sequence; the lead sets one band denominator (see Across the band).
- **Confidence.** Judgment call.

### 5. The grade 7 hand-off is marked unverified, and it is now verifiable (low; firm)

LAYER sequence. REPEAT yes (grade 7 finding 6).
- **What is wrong.** The sequence says grade 7's days.csv was absent. It exists, and every e7 row is used there (the
  fewest: e7-present-salient 4 days, e7-commas-spelling 5). Retrieval is right throughout.
- **Fix (scope and sequence prerequisites).** Mark the e7 placements confirmed. ss7-greek-myth is a social studies
  row I did not check against grade 7 social studies.
- **Confidence.** Firm.

### 6. Small slips (low; firm)

LAYER frame and sequence. REPEAT yes.
- The frame still calls the following check the unit's end for units 3 to 5, says readiness for grade 7 rows, and
  calls unit 1's one-sitting narrative a "readiness sample" (it is retrieval, as day 11 says). Fix at the next frame
  touch.
- Day 29 holds an observed discussion and brief explanations of verbals, voice and mood. The explanations are short
  and done while the teacher rotates, so I leave it; if the trial shows the explanations take more than fifteen
  minutes, move them to day 30.

## What the collect-once rule changes

- Days 90, 125 and 157 (finding 1). Days 89, 126 and 158 are clear: day 89's cold story is 61 days after day 28; day
  126's argument is 67 days after day 59 and its L.8.4 tasks 40 days after day 86.
- Mids narrow (finding 2), though none breaks the ten-day window.
- Day 155 (RL.8.10) and day 157 (RI.8.10) are both unseen reads with directions only, two days apart. They are
  different expectations and the only independent records of each; keep both.
- Readiness by grade number changes nothing (finding 5).

## Judged items the brief named

- **Texts against the catalogue.** Every id placed (g8-u1-01 to g8-u5-06) matches ela-texts.csv in title, author, use
  and status. Mather, the Wiley bulletins and Barnham are "to confirm", and the sequence uses them only as supported
  paired excerpts. The Nasreddin edition is unconfirmed and the sequence says so. Source map: no base, none written.
  Met.
- **Argument, research, literary analysis.** Arguments answer counterclaims (W.8.1a, the marker process piece and the
  check 2 piece), and the talk argument integrates media. Research taught on days 72 to 76, published day 84, run
  again on days 134 to 140. Literary analysis runs as daily W.8.9 paragraphs and the unit 1 suspense essay, which is
  filed as informative under W.8.2; finding 1's day 125 adds the band's one sustained literary-analysis piece under
  W.8.9a. Writing 34.8/34.8/30.4 by composition day. Met.
- **Complexity and balance.** Novella 35,000 to 45,000 words; the long law-making feature, long poem and full play
  read whole. Balance finding 4.
- **Vocabulary and morphology.** Weekly eight-word lists with returns are good; morphology finding 3.
- **RL.8.9 and religious works.** Open with Cory already (frame read of 2026-11-14); the sequence places myths and folk
  tales only, which is right while it is open. Not a new item.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Unit named by a topic and its texts | Met |
| Anchor texts on file, with a reason for their place | Part: to write or to choose; twelve planning records |
| Long text read whole | Met (novella, feature, poem, play) |
| Text complexity rises from the grade before | Met |
| About 55 informational, 45 literary | Over (finding 4) |
| Writing about 35/35/30 | Met |
| Research taught, then used | Met |
| Formal discussion often | Met (sixteen, at most ten days apart) |
| End task joins reading with writing or speaking | Met |
| Morphology across the year | Not met (finding 3) |
| Sensitive content has a teacher note | Met |

## Brief's other checks

- **Order.** Sound: mystery, founding words, 1906 food law and research, myths, gene news.
- **Assessments.** Every unit is over 25 days and has a mid; every end is inside the unit, spread over three or four
  days with no stacked performances (days 27 to 29, 59 to 61, 85 to 87, 121 to 123, 147 and 153 to 155).
- **Readiness and retrieval.** All e7; retrieval at first use. Finding 5.
- **Checks that do not repeat.** Finding 1.
- **Standards in full.** Lettered parts listed with parents; no gap found.
- **Days by load.** 30, 32, 26, 32, 28 as framed.
- **Calendar and leans.** Weeks 18, 25 to 26 and 32 meet CALENDAR.md. The day 84 publication against civics' research
  (days 77 to 95) is flagged for the lead by the sequence; I agree it needs coordination, not a unit move.
- **Candidate cells.** Inside existing days.
- **Shorter path.** Given, with ten named fold-in days.
- **Source map.** Not applicable.
- **Stale notes.** Findings 5 and 6.

## What is right and should not be touched

Spread end days, check topics moved to earlier units, separate independent-reading records, retrieval at the point
of use, parallel-group talks with teacher rotation, the honest anchor counts and the grade 9 boundary note.

## What I could not judge

- Text demand: all anchors unwritten or unchosen.
- Whether 35,000 to 45,000 words fits days 1 to 18; the sequence rightly leaves it to a timed check.
- ss7-greek-myth's grade 7 social studies use.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Mids sample rows taught so far; day 75's word strategies wait for day 86 | Mid is not a rehearsal | days.csv |
| Day 66 teaches tox, pharm, serv, ad-, ced after grade 7 retrieval; weekly word-part slot | Morphology across the year | days.csv; scope-and-sequence.md |
| Grade 7 hand-off marked confirmed | The grade 7 days exist | scope-and-sequence.md |
| Day 29 left as is, with a timing watch | Brief explanations, not a second performance | none |

Check content (finding 1), the band anchor denominator (finding 4) and the unit 5 audience (the sequence's own
item) are calls for the lead.

## For Cory

None new. RL.8.9 and religious works is already with Cory.

## Sources

- Common Core State Standards for ELA, grade 8 (data/standards/ccss-ela-standards-full.txt).
- docs/RUBRIC-ELA.md; the grade 5 expert read of 2026-11-15.

## For the source list

None.

## Across the band

- **Course checks repeat the unit's forms in all three grades.** Grade 6 days 60, 109, 110, 158; grade 7 days 58,
  109, 158; grade 8 days 90, 125, 157. One cause: the sequences added in-unit ends but kept the frames' check
  content. One rule for the band, written into the three frames' check wording: a check reuses the just-ended unit's
  record and spends its items on earlier units' rows in a form not given in the last two weeks. Grade 8 day 158 and
  grade 6 day 59 are the models.
- **Mids rehearse ends** in all three (grade 6 days 6 and 15, 45 and 57; grade 7 days 73 and 84; grade 8 every unit).
  Mids sample what has been taught.
- **End days stack** in grades 6 (days 84, 152) and 7 (day 29); grade 8 spreads them and is the model.
- **Morphology thins after grade 5.** Grade 6 has one unit and reteaches graph a third year; grade 7 one day; grade 8
  four whole words. Extending the grade 5 read's band list: grade 6 gram, phon, glyph, aud; grade 7 demos, logy, pan,
  epi, immun; grade 8 tox, pharm, serv, ced; each grade retrieves the last grade's parts in two minutes and carries
  a three-minute weekly slot. The lead adopts the list once, in the progression.
- **Long text.** Grade 5 30,000 to 40,000 words plus a biography read whole; grade 6 25,000 to 30,000 with no long
  informational whole (the dip); grade 7 30,000 to 35,000; grade 8 35,000 to 45,000 plus a long feature. Only grade 6
  needs a change.
- **Anchor denominators differ.** Grade 6 counts works (52.2 percent; 66.7 by record), grade 7 counts records (58),
  grade 8 gives both (58.3 and 66.7). The lead should fix one count for the band, by work, and set the target
  against it.
- **Writing.** Argument climbs well: supported claims (6), acknowledged opposing claims (7), answered counterclaims
  (8). Research twice a year in every grade, with standard citation from grade 7. Literary analysis is daily
  paragraphs in every grade; the band has no sustained literary-analysis piece until finding 1's day 125, so the lead
  may want one per grade.
- **Hand-offs.** 5 to 6, 6 to 7 and 7 to 8 are all retrieval, every assumed row used in the grade before; grades 7
  and 8 still say the earlier days were missing. Grade 6 does not take up grade 5's word-part and oral-reading
  records.
- **Stale frame wording** in all three frames: readiness for prior-grade rows, and the following check as the unit's
  end. One sweep at the next frame touch.
- **Source maps.** None in the band; no base text.
