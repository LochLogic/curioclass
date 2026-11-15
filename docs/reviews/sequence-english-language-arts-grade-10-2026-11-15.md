# Expert read: scope and sequence of English Language Arts, Grade 10

Course `english-language-arts-grade-10`. Cold read, 2026-11-15, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of any Codex read of this course, which was not opened.
The band summary is in the grade 12 report.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md.
- Cold: docs/courses/english-language-arts-grade-10/scope-and-sequence.md; data/plans/english-language-arts-grade-10/days.csv
  (160 rows, with every assessment, course-check and respond day in full).
- Beside them: the frame's Checks table; the grade 10 rows of data/plans/ela-texts.csv; the e9 and e10 rows of
  data/progressions/ela.csv; docs/CALENDAR.md; the grade 9 days, to confirm the hand-off; the Algebra I frame, for
  the scatter-plot readiness row.
- Gates: `plan.py check` exits 0; `sequence.py check` for this course, 0 failures; `stale.py check`, 0 failures.
  `frame.py calendar` covers K to 8 only; CALENDAR.md sets week 32 as finals week for 9 to 12. A Codex run is writing
  math courses at the same time.

## Verdict

The strongest text plan in the band so far: Frankenstein and All Quiet on the Western Front read whole, Julius Caesar
with its Plutarch source, a seminal set from the Declaration to Four Freedoms, and research that climbs from grade 9's
short projects to a sustained one. Its weakness is the course checks: all three re-collect codes their units recorded
two to five days before, and check 3 stacks eight informational codes with an essay. Part of check 2's overlap is
written into the frame. Fix findings 1 and 2 and it is ready.

## Findings, most serious first

### 1. All three course checks re-collect what the unit just recorded (serious; firm)

LAYER sequence (and frame for check 2). REPEAT yes (grade 6 to 9 pattern).

What is wrong:
- Check 1, day 44, lists RI.9-10.1, 2, 3, 5 and 10 three to four days after days 40 and 41 recorded them at unit 2's
  end.
- Check 2, days 86 to 88, lists RL.9-10.4, RL.9-10.9 and L.9-10.5 two days after day 84, and W.9-10.1a to e five days
  after day 83's Julius Caesar argument.
- Check 3, day 157: finding 2.

The topics moved to earlier units; the codes did not.

Why it matters: collect once. A check inside ten days reuses the record; re-collecting spends teacher scoring and a
period on evidence already in hand.

Fix: day 44 reuses days 40 and 41 for RI.3 and RI.5 and keeps RI.1, RI.2 and RI.10 on the cold text. Days 86 to 88
reuse day 84 for RL.4 and L.5 and day 83 for W.9-10.1, and keep RL.9-10.9 only if the frame insists. The frame's check
2 names transformation of a source and cumulative word choice right after unit 4, which is unit 4's own work, so the
frame line itself is a call for the lead.

### 2. Check 3's day 157 packs too much (moderate; firm)

LAYER sequence. REPEAT new.

What is wrong: day 157 lists eight RI codes plus W.9-10.9b and a 35-minute essay, and RI.9-10.8 was recorded on day
155.

Fix: reuse day 155 for RI.8; put RI.3, RI.4 and RI.5 in the 15-minute items; let the essay carry RI.1, RI.2 and RI.6
with W.9-10.9b and W.9-10.10.

### 3. Day 44 holds items and a full essay in one period (low; judgment call)

LAYER sequence. REPEAT new.

What is wrong: sorting items plus a full on-demand essay in 50 minutes.

Fix: with finding 1's reuse, the items shrink to about ten minutes and the essay has forty.

### 4. Mid day 14 asks what end day 27 asks (moderate; firm)

LAYER sequence. REPEAT yes (mids rehearse ends).

What is wrong: both list RL.9-10.1, 2, 3 and 5 on Frankenstein.

Fix: day 14 samples RL.1 and RL.3 on the chapters read so far; RL.2 and RL.5 on the whole novel wait for day 27.

### 5. Word parts are named but not taught (moderate; firm)

LAYER progression. REPEAT yes.

What is wrong: L.9-10.4b is listed on many days, but no word family is named, and the weekly lists are whole words.

Fix: as in the grade 9 report, one band list of derivational families in data/progressions/ela.csv, new families only
this year, retrieval of grade 9's in two minutes, and a weekly three-minute slot.

### 6. The grade 9 hand-off is marked unverified, and it is now verifiable (low; firm)

LAYER sequence. REPEAT yes (grade 8 finding 5).

What is wrong: the sequence says the grade 9 day map is absent. It exists, and every e9 row the sequence uses is
placed there.

Fix: mark the hand-off confirmed; e9 rows get retrieval at first use, as the days already do.

### 7. Scatter-plot readiness rests on a course with no day map yet (low; judgment call)

LAYER sequence. REPEAT new.

What is wrong: day 127 checks readiness on m8-scatter-plots. That is right by grade number today, but Algebra I unit
3 (two-variable statistics, days 47 to 59) will use it in grade 9.

Fix: none now; switch day 127 to retrieval once the Algebra I days exist.

### 8. The kept West African story has no catalogue row (low; firm)

LAYER base text. REPEAT new.

Fix: add a row in data/plans/ela-texts.csv with author or teller, rights basis and a sensitivity note before days.
It also fixes the balance count (the sequence counts it; the catalogue does not).

### 9. Lead the balance with the anchor count (low; firm)

LAYER sequence. REPEAT yes.

What is wrong: the sequence gives 56/44 with the uncatalogued story and 39/61 by days. The catalogue's anchors are 10
informational and 7 literary, 58.8% informational.

Fix: report the anchor count only, per the lead call.

## What the collect-once rule changes

- Day 44 reuses days 40 and 41 for RI.3 and RI.5 (finding 1).
- Days 86 to 88 reuse day 84 for RL.4 and L.5 and day 83 for W.9-10.1 (finding 1).
- Day 157 reuses day 155 for RI.8 and sheds codes (finding 2).
- Already right: independent-reading checkpoints on days 82, 110, 123 and 136 feed the check 3 conference rather than a
  new log.

## Judged items the brief named

- **Texts against ela-texts.csv.** All anchors have rows except the West African story (finding 8).
- **Writing progression.** Grade 9 answered one counterclaim; grade 10 weighs several (unit 5 war speeches, unit 6
  liberty) and holds a sustained analytic essay on Frankenstein plus the Julius Caesar literary argument. Five process
  pieces across all three types. A climb.
- **Research.** Short research in unit 2, sustained research in unit 7. A climb from grade 9.
- **Text complexity.** Frankenstein (about 75,000 words) and All Quiet (about 60,000) whole; Julius Caesar whole.
  Demand rises from the Odyssey and Romeo and Juliet.
- **Balance.** Finding 9.
- **Seminal documents.** RI.9-10.9 on the Declaration, Harper, Anthony, Chief Joseph and Four Freedoms. Met.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Unit named by a topic and its texts | Met |
| Anchor texts on file, with a reason for their place | Part: one kept text uncatalogued (finding 8) |
| Long text read whole | Met (two novels, one play) |
| Text complexity rises from the grade before | Met |
| About 55 informational, 45 literary | Over a little (58.8) |
| Writing about 35/35/30 | Met |
| Research taught, then used | Met |
| Formal discussion often | Met |
| End task joins reading with writing or speaking | Met |
| Morphology across the year | Not met (finding 5) |
| Sensitive content has a teacher note | Met, except finding 8 |

## Brief's other checks

- **Order.** Sound: Frankenstein, life science from Huxley to cloning, colonial rule, Julius Caesar, persuaded to war,
  liberty, rising seas.
- **Assessments.** Mids in every long unit; ends spread inside their units; no end day asks for two full performances.
- **Readiness and retrieval.** e9 rows by retrieval; m8-scatter-plots readiness (finding 7). Hand-off finding 6.
- **Checks that do not repeat.** Findings 1 and 2.
- **Standards in full.** Lettered parts listed; no gap found.
- **Days by load.** As framed; `sequence.py check` passes.
- **Calendar.** Check 3 in week 32 finals week.
- **Candidate cells.** Inside existing days.
- **Shorter path.** Given.
- **Source map.** Not applicable: no outside base.
- **Stale notes.** Finding 6; the frame's readiness wording predates the grade-number count.

## What is right and should not be touched

Weekly vocabulary for all 32 weeks, the two whole novels, Julius Caesar with Plutarch, the seminal set, the research
climb, the independent-reading checkpoints and the Frankenstein essay.

## What I could not judge

- The West African story's text and its fit: not on file.
- Whether All Quiet's translation is public domain where the plan needs it; the rights check sits with the catalogue.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Days 44, 86 to 88 and 157 reuse records inside ten days | Collect once | days.csv |
| Day 157 sheds codes into items and essay | One period, one performance | days.csv |
| Day 14 samples RL.1 and RL.3 only | Mid is not a rehearsal | days.csv |
| Band word-family list and weekly slot | Morphology across the year | data/progressions/ela.csv; days.csv |
| Grade 9 hand-off marked confirmed | The grade 9 days exist | scope-and-sequence.md |
| Day 127 readiness kept until Algebra I days exist | Right by grade number today | none |
| Balance reported by anchors, 58.8 | Lead call: anchors only | scope-and-sequence.md |

The frame's check 2 content (finding 1) is a call for the lead.

## For Cory

Check 2, day 86, uses Paradise Lost as Frankenstein's source under RL.9-10.9. It is a religious epic retelling
Genesis, so it raises the same question as RL.8.9 and RL.9-10.9's Bible example. Not decided here.

## Sources

- Common Core State Standards for ELA, grades 9 to 10 (data/standards/ccss-ela-standards-full.txt).
- docs/RUBRIC-ELA.md; the grade 8 and grade 9 expert reads of 2026-11-15.

## For the source list

None.
