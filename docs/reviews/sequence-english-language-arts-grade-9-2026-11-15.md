# Expert read: scope and sequence of English Language Arts, Grade 9

Course `english-language-arts-grade-9`. Cold read, 2026-11-15, per docs/pipeline/briefs/sequence-read.md, with
{subject} = ela and {bar} = docs/RUBRIC-ELA.md. Independent of any Codex read of this course, which was not opened.
First of the grade 9 to 12 band; the band summary is in the grade 12 report.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/ela.md; docs/RUBRIC-ELA.md; docs/GLOSSARY.md; the brief and
  docs/pipeline/briefs/sequence-write.md (rules 2, 3, 8 and 10 above all).
- Cold: docs/courses/english-language-arts-grade-9/scope-and-sequence.md; data/plans/english-language-arts-grade-9/days.csv
  (160 rows, with every assessment, course-check and respond day in full).
- Beside them: the frame (Units and Checks tables); the grade 9 rows of data/plans/ela-texts.csv; the e8 and e9 rows
  of data/progressions/ela.csv; docs/CALENDAR.md; the grade 7 and 8 days, to count readiness; the grade 8 expert read
  of 2026-11-15 and its "Across the band".
- Gates: `plan.py check` exits 0; `sequence.py check` for this course, 0 failures; `stale.py check`, 56 files,
  0 failures. `frame.py calendar` lists K to 8 only; for 9 to 12 CALENDAR.md sets week 32 as finals week and no other
  rule, so no stagger question arises. A Codex run is writing math courses at the same time.

## Verdict

Sound and careful. The texts climb from grade 8 in demand, not just length (the Odyssey in large parts, Romeo and
Juliet whole), the seminal US documents are real (Washington's Farewell Address, the Gettysburg Address), and the
year holds a sustained literary argument. The weak point is the course checks: check 3 re-collects codes from days
earlier and puts the timed argument on the issue students just wrote about for 17 days, and check 2 adds RI.9-10.9
the frame does not ask for. Fix findings 1 to 3 and it is ready.

## Findings, most serious first

### 1. Check 3 re-collects what unit 8's end just recorded (moderate; firm)

LAYER sequence. REPEAT yes (the grade 6 to 8 pattern).

What is wrong: day 156 lists RL.9-10.3, RL.9-10.4 and L.9-10.5 on a cold poem, two to four days after day 152 (the
motive chart) and day 154 (annotations) recorded the same codes.

Why it matters: the collect-once rule says a check inside ten days reuses the record. Re-collecting costs a period of
teacher scoring and tells nothing new.

Fix: on day 156 mark RL.9-10.3, RL.9-10.4 and L.9-10.5 "record from days 152 and 154"; keep RL.9-10.1, RL.9-10.2 and
RL.9-10.10 on the cold poem, which is new evidence.

### 2. The timed argument rewrites unit 6's essay (moderate; firm)

LAYER sequence. REPEAT yes (check topic).

What is wrong: days 157 and 158 set the cold argument and the timed on-demand argument on school start time, unit 6's
own issue, which students researched and wrote about for 17 days.

Why it matters: a course check moves to a new topic. On the same issue the timed piece measures memory of the process
essay, not argument on demand.

Fix: a new question drawn from earlier-unit knowledge. Unit 7's honeycreeper threats fit ("should people intervene to
save a species"): unit 7 kept them as context and asked for no solution, so the knowledge is there and the claim is
fresh.

### 3. Check 2 adds a seminal-document pair the frame does not name (moderate; firm)

LAYER sequence. REPEAT new.

What is wrong: day 97 adds RI.9-10.9 with "a second seminal US document on unit 4 journeys and belonging". The frame's
check 2 does not list RI.9-10.9, day 94 already assessed it, and the sequence itself flags that a fitting second
document may not exist.

Why it matters: an unframed code on a check is extra collection, and a forced pairing makes a weak item.

Fix: drop RI.9-10.9 from day 97 and rely on day 94's record.

### 4. Word parts are one day (moderate; firm)

LAYER progression. REPEAT yes (grade 6 to 8 finding).

What is wrong: L.9-10.4b (patterns of word change, as in analyze, analysis, analytical) is taught on day 9 and
assessed on day 20. The weekly word lists are whole words (impunity, connoisseur, credulity), with no named word
families and no later word-change practice. The grade 8 parts (tox, pharm, serv, ced) get no retrieval.

Why it matters: the lens asks for morphology across the year, and the rubric's vocabulary line is about patterns, not
one lesson.

Fix: name four to six derivational families in data/progressions/ela.csv on the one band list (new roots only each
year, per the lead call), retrieve the grade 8 parts on day 9, and keep a three-minute weekly word-family slot.

### 5. Check 1 does not say the cold story comes from outside the US (low; firm)

LAYER sequence. REPEAT new.

What is wrong: day 64 lists RL.9-10.6 (point of view from world literature outside the US) on unit 1 or 2 content, but
does not say the cold text must be from outside the US.

Fix: add "cold story from outside the United States" to the day 64 note.

### 6. Mid day 33 asks what end day 48 asks (low; firm)

LAYER sequence. REPEAT yes (mids rehearse ends).

Fix: day 33 samples the theme trace on the books taught so far; the objective summary waits for day 48.

### 7. Lead the balance with the anchor count (low; firm)

LAYER sequence. REPEAT yes.

What is wrong: the sequence gives three balances (59.5/40.5 by days, 61.5 expanded). The lead call is anchors only.

Fix: report 13 informational and 10 literary anchors, 56.5% informational, and drop the other two figures or put them
in a note.

## What the collect-once rule changes

- Day 156: RL.9-10.3, RL.9-10.4 and L.9-10.5 reuse days 152 and 154 (finding 1).
- Days 157 and 158: a new topic (finding 2).
- Day 158 lists W.9-10.1a to e eight days after day 150's process argument. The form differs (on demand against process),
  but the codes are re-collected inside ten days. Either day 158 keeps only W.9-10.10 (range of writing, timed) and reuses
  day 150 for W.9-10.1, or the lead rules that on-demand writing counts as a new form. Call for the lead.
- Day 97: drop RI.9-10.9 (finding 3).
- Already right: day 83 reuses days 72 and 75; day 115 reuses day 107; day 158 reuses day 153's research record.

## Judged items the brief named

- **Texts against ela-texts.csv.** Every unit's anchors have rows with title, author, use and status. Independent books
  are named only for unit 1; later units say "student choice from the list". Call for the lead whether the list is
  needed now or at days.
- **Writing progression from grade 8.** Grade 8 answered counterclaims; grade 9 develops claim and counterclaim fairly
  with strengths and limits (W.9-10.1b) in unit 6, and the Romeo and Juliet literary argument is the year's sustained
  literary analysis. A real climb.
- **Research.** Short research twice, the second feeding the argument. Taught, then used.
- **Text complexity.** Climbs in demand: epic verse in translation, a full Shakespeare play, 18th and 19th century
  speeches.
- **Balance.** Finding 7.
- **Seminal documents.** RI.9-10.9 on the Farewell Address and the Gettysburg Address. Met.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| Unit named by a topic and its texts | Met |
| Anchor texts on file, with a reason for their place | Met |
| Long text read whole | Met (Romeo and Juliet; the Odyssey in large parts) |
| Text complexity rises from the grade before | Met |
| About 55 informational, 45 literary | Met by anchors (56.5) |
| Writing about 35/35/30 | Met |
| Research taught, then used | Met |
| Formal discussion often | Met |
| End task joins reading with writing or speaking | Met |
| Morphology across the year | Not met (finding 4) |
| Sensitive content has a teacher note | Met |

## Brief's other checks

- **Order.** Sound: suspense stories, the Odyssey, stories in translation, four lives in print and film, union speeches, the school-start argument, island birds, Romeo and Juliet.
- **Assessments.** Every unit over 25 days has a mid; ends are spread and inside their units. No end day asks for full
  performances on two expectations.
- **Readiness and retrieval.** Day 50 readiness for e4-grammar and e6-pronouns is right by grade number: grade 5
  retrieved e4-grammar and grade 7 retrieved e6-pronouns, so grade 9 is readiness for both. Grade 8 rows get retrieval
  at first use. Hand-off from grade 8 confirmed against the grade 8 days.
- **Checks that do not repeat.** Findings 1 to 3.
- **Standards in full.** Lettered parts listed with parents; no gap found.
- **Days by load.** As framed; `sequence.py check` passes.
- **Calendar.** Week 32 finals week holds check 3.
- **Candidate cells.** Inside existing days.
- **Shorter path.** Given, with named fold-in days. Good.
- **Source map.** Not applicable: no outside base; texts are public domain, US government works or originals.
- **Stale notes.** The frame's readiness wording predates the grade-number count; the days follow the count.

## What is right and should not be touched

Romeo and Juliet whole, the Odyssey in large parts, weekly word lists for every week, the Farewell and Gettysburg pairing, the literary argument, the
record reuse on days 83, 115 and 158, readiness counted correctly on day 50, and the shorter path.

## What I could not judge

- Whether the Odyssey translation chosen reads at grade 9 demand: the edition is to confirm.
- How long the sustained literary argument runs in classroom time against its days.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 156 reuses days 152 and 154 for RL.3, RL.4 and L.5 | Collect once | days.csv |
| Days 157 and 158 move to a new question on unit 7 knowledge | A course check moves to a new topic | days.csv |
| RI.9-10.9 dropped from day 97 | Not in the frame; day 94 holds the record | days.csv |
| Band word-family list plus grade 8 retrieval and weekly slot | Morphology across the year | data/progressions/ela.csv; days.csv |
| Day 64 cold story from outside the US | RL.9-10.6 names world literature | days.csv |
| Day 33 samples the theme trace only | Mid is not a rehearsal | days.csv |
| Balance reported by anchors, 56.5 | Lead call: anchors only | scope-and-sequence.md |

Day 158's W.9-10.1 inside ten days of day 150 and the independent-book list are calls for the lead.

## For Cory

RL.9-10.9 names "the Bible" as an example source a later author draws on, the same question as RL.8.9 and religious
works. The plan uses Ovid and Tennyson and does not need the Bible. Not decided here; it joins the RL.8.9 question.

## Sources

- Common Core State Standards for ELA, grades 9 to 10 (data/standards/ccss-ela-standards-full.txt).
- docs/RUBRIC-ELA.md; the grade 8 expert read of 2026-11-15.

## For the source list

None.
