# Sequence read: World Geography and Ancient Civilizations II (grade 7), 2026-11-14

Expert cold read of the scope and sequence, per docs/pipeline/briefs/sequence-read.md. Independent of any other read of
this course's scope and sequence (the Codex read was not opened).

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, the social studies part of
  docs/ADOPTION-BAR-SUBJECTS.md (with the shared core and pass rule), docs/courses/social-studies/STANDARD.md.
- docs/courses/world-geography-and-ancient-civilizations-ii/scope-and-sequence.md and
  data/plans/world-geography-and-ancient-civilizations-ii/days.csv, cold, in full.
- Beside them: the frame (docs/courses/world-geography-and-ancient-civilizations-ii/frame.md), the grade 7 rows of
  data/progressions/social-studies.csv and the rows they assume (ss5-constitution and its users), the grade 7
  standards in data/standards/ma-hss-2018.txt, docs/courses/CALENDAR.md, the grade 7 rows of data/plans/calendar.csv,
  docs/pipeline/briefs/sequence-write.md, the frame read
  docs/reviews/frame-world-geography-and-ancient-civilizations-ii-2026-11-13.md, and this day's grade 6 sequence read
  (docs/reviews/sequence-world-geography-and-ancient-civilizations-i-2026-11-14.md) for REPEAT.
- Gates: `plan.py check` passes for this course (`sequence world-geography-and-ancient-civilizations-ii: 0
  failure(s)`; the run exits 1 on one STALE note in docs/courses/us-history-ii/frame.md:78, not this course).
  `frame.py calendar`: grade 7 social studies checks in weeks 13, 24, 32; no stagger break. `stale.py check`: none here.

## Verdict

Sound: every code and lettered part has a day, the year runs in region and time order with the anchor's two stated
departures, the frame read's fixes (the Qin and Han dates, claim and evidence from unit 1, the held look-back) are all
carried into the days, and the writing grows from object claims to a report to a multi-cause argument with a named
counterclaim. The biggest risk is the same assessment stacking as grade 6: all three course-level checks repeat, nearly
word for word, the end-of-unit assessment set two or three days before. The one change that matters most is to source
each check's repeated skill from earlier units' content (finding 1); next, give the Peloponnesian War a day of its own
(finding 2).

## Findings

### 1. Each course-level check repeats the end-of-unit assessment held days before it

- **LAYER** sequence. **REPEAT** yes (grade 6 sequence read, finding 1). **Confidence** likely.
- **What is wrong.** Day 114 (unit 9): "ranked causes defended from an unseen source"; day 117 (check 2): "ranked causes
  defended from an unseen source". Day 155 (unit 12): "a multi-cause argument from unseen sources with the counterclaim
  named"; day 157 (check 3): "a multi-cause argument from two unseen sources with the strongest counterclaim named".
  Day 61 (unit 5): "a comparison of two societies from unseen sources"; day 64 (check 1): "a comparison of two societies
  with reasons". Around check 2 the grade also holds ELA 7's check (days 109 and 110, inside the research drafting
  days), the report hand-in (112), unit 9's assessment (114), check 2 (116, 117) and math 7's check (119).
- **Why it matters.** The check reports the unit just taught twice instead of what has lasted from the earlier units.
- **Fix (no day moves).** Check 1's comparison uses two societies from units 1 to 3 (the Indus and the Shang, say) with
  a unit 4 source, not the unit 5 pairing; check 2's ranked causes come from units 4 or 8 (the Qin's unification, or why
  Athens' assembly grew); check 3's multi-cause argument takes a question from units 2 to 9
  (why the Mauryan Empire held or why Athens lost the Peloponnesian War), not Rome's fall. Day 114: the report counts
  for MA.7.T4b.7, D2.His.17, D3.2 and D4.5, so the day's own task covers MA.7.T4b.5 and 6 only. Settled below.

### 2. Unit 9 gives three wars two and a half days while research has eight

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Day 102 carries the causes and results of both the Persian Wars and the Peloponnesian War, with
  Thucydides; day 103 carries Alexander's conquests and the ranking. MA.7.T4b.5 is the unit's analysis code (D2.His.15
  ranks causes), and the year's mid-year check tests it. The research run is days 105 to 112, then a claim day (113)
  that rests on the reports shared on day 112.
- **Why it matters.** Ranking causes needs causes taught; a 50-minute day cannot carry two wars and a source read. The
  likely day is a list, which is what the lens says ranking is meant to replace.
- **Fix (a day swap inside the unit).** Join day 112 (hand in and share) and day 113 (the claim on the compelling
  question): share in a short round, then write the claim. The freed day goes to the wars: day 102 the Persian Wars,
  day 103 the Peloponnesian War with Thucydides, day 104 Alexander and the ranking, myths moving to day 105 and research
  running 106 to 112. Settled below.

### 3. Unit 10 opens with a readiness check where the rule and the row call for a retrieval task

- **LAYER** frame. **REPEAT** yes (grade 6 sequence read, finding 2, the same question). **Confidence** firm.
- **What is wrong.** Day 121 is a readiness check on ss5-constitution, as the frame's Seams row says. The progression
  row itself (ss7-roman-republic) names the handoff "content revisited ... opens with a short retrieval task", and
  sequence-write rule 2 keeps readiness checks for rows idle two or more grades. ss5-constitution is idle for grade 6
  only. The writer asked for the rule's meaning (For the lead 2).
- **The right call.** "Idle two or more grades" means two or more whole grades with no use between the last use and
  this course. A grade 5 row met in grade 7 has one idle grade, so it opens with a retrieval task, the same treatment
  grade 6 gives its grade 4 rows (ss4-exploration, ss4-first-peoples-evidence). Readiness checks are left for real
  gaps of two grades or more.
- **Fix.** Day 121: assess blank, goal "Rome on a map and how its location supported its power"; day 124 opens "Open
  with a retrieval task on grade 5's branches of government, then ..."; note "Retrieval task on ss5-constitution
  (grade 5, idle in grade 6)". Scope and sequence unit 10 and the frame's Seams row, Models row and unit 10 cell to
  say retrieval task. Settled below.

### 4. Unit 10's compelling question has two days of content behind it

- **LAYER** sequence. **REPEAT** new. **Confidence** a judgment call.
- **What is wrong.** "Could the Roman Republic have been saved?" is argued on day 131 from day 125 ("Julius Caesar and
  the crisis of the Republic") and day 126 (Augustus). The causes a student needs for a counterfactual (the land
  question and the Gracchi, armies loyal to their generals, civil wars before Caesar) are not named on any day.
- **Why it matters.** With only Caesar and Augustus, the likely answer is "no, Caesar took over", one defensible
  answer, which the lens marks as a failed question.
- **Fix.** Day 125's goal: "The Republic in crisis: land and the Gracchi, armies loyal to their generals, civil wars,
  and Julius Caesar". No day added. Settled below.

### 5. The held look-back day and the generated calendar differ by one day

- **LAYER** process. **REPEAT** yes (grade 6 sequence read, finding 7). **Confidence** firm.
- **What is wrong.** Day 120 is unit 8's look-back, at the start of unit 10 as the frame sets; unit 9 runs 101 to 115
  and check 2 runs 116 to 117 here, while calendar.csv shows 102 to 116 and 117 to 118.
- **The right call: keep days.csv.** The check stays in its target week 24, math 7's check (day 119) and ELA 7's (109,
  110) still share no day with it, and no lean window moves across a unit boundary. The look-back comes 26 school days
  after the action (day 94), which suits a reply from the principal or council.
- **Fix.** As for grade 6: frame.py reads unit and check ranges from days.csv once one exists. No change here.

## Days by load

Teaching days follow the owned parts: unit 2's four parts at 4, 5 and 2 days with a claim day; unit 4's Qin (4),
routes (3) and supply and demand (4, with all four applications D2.Eco.6 names); unit 8's five democratic ideas over
three days, the action over three plus the look-back, Athens and Sparta over three. Unit 5 gives Buddhism east, Heian
Japan and the China, Korea and Japan encounters one day each, which is thin for MA.7.T2c.1's "growth in Japan from the
6th to 13th century" but inside the anchor's light weight on the topic; left as is. The one run under load is unit 9's
wars (finding 2).

## The calendar and leans

- Checks on target weeks 13, 24 and 32; ELA 7 (57, 58, 109, 110), math 7 (45, 119) and science 7 (67) share no school
  day with them.
- Leans checked against calendar.csv: math 7's rational number unit (69 to 91) before unit 7's offsets, with day 84's
  bridge; math 7 percent (47 to 68) before unit 11; ELA 7 unit 3 research and roots (61 to 86) before units 9 and 11;
  ELA 7 unit 4 (87 to 108) beside unit 8, the democracy question kept here; ELA 7 unit 5 allusions after unit 9;
  ELA 7's argument work before unit 12. All met.

## Candidate cells

All settled: the Persian opener placed (day 101), Homer in short retellings inside day 104 (it moves to day 105 with
finding 2, still at no added day), the Han and Rome comparison inside day 153. Agreed with each.

## The lens checklist (scope and sequence layer)

| Line | Met, missed or not applicable |
|---|---|
| A unit question answerable without the unit's sources, or with one defensible answer | Met, except unit 10 as the days stand (finding 4); units 7 and 11 answer theirs on the assessment, which is enough |
| History out of time order with no reason | Met: Japan past 500 CE and time zones with Europe carry the anchor's reason |
| A contested event given one telling only | Met: the Indo-Aryan question as a scholarly question, Ashoka's missionaries against conversion claims, fall or transformation, Thucydides as one source |
| Writing from sources once a year or never building from short to long | Met: object claim (day 9), short claims each unit, the report (unit 9), the multi-cause argument (unit 12) |

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Check items for the repeated skill draw on earlier units (check 1: units 1 to 3 societies; check 2: ranked causes from units 4 or 8; check 3: a question from units 2 to 9) | A check measures what lasted | days.csv days 64, 117, 157; scope-and-sequence.md check sections |
| Day 114 tests MA.7.T4b.5 and 6; the report counts for the research codes | Cuts a double test in a stacked week | days.csv day 114 |
| Unit 9: share and claim joined; the Persian Wars, the Peloponnesian War and Alexander one day each | Ranking needs the causes taught | days.csv days 102 to 113; scope-and-sequence.md unit 9 |
| Unit 10 opens with a retrieval task on day 124, not a readiness check on day 121 | One idle grade; the row and rule 2 agree | days.csv days 121, 124; scope-and-sequence.md unit 10; frame.md Seams, Models, unit 10 |
| "Idle two or more grades" means two whole grades with no use between | Answers For the lead 2, consistent with grade 6 | sequence-write.md rule 2 wording (the lead's) |
| Day 125 names land and the Gracchi, loyal armies and civil wars | The compelling question needs more than one answer | days.csv day 125 |
| Keep the held look-back on day 120; the calendar follows days.csv | Same week, no stagger change | none here (frame.py) |

## For Cory

Nothing. Every finding is an item-level or process choice.

## What I could not judge

Whether math 7 teaches signed addition at days 69 to 77 exactly (calendar.csv gives only its unit, 69 to 91); day
84's bridge covers either case. Outside sources were not re-fetched on this run; none of the findings rests on one.
