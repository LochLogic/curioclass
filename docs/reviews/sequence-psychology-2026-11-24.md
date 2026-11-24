# Expert cold read: scope and sequence of Psychology (2026-11-24)

Job: docs/pipeline/briefs/sequence-read.md, course `psychology`, subject social studies (lens
docs/agents/lenses/social-studies.md; bar: the social studies part of docs/ADOPTION-BAR-SUBJECTS.md and the lens's
psychology line: every APA22 target and theme in a unit, priority areas weighted, no study without its sample and
replication record). The writer worked under docs/pipeline/briefs/sequence-write.md; read cold.

## What I read

- docs/courses/psychology/scope-and-sequence.md (all), data/plans/psychology/days.csv (all 160 rows),
  data/plans/psychology/source-map.csv (all 111 rows), docs/courses/psychology/DEFAULTS.md.
- docs/courses/psychology/frame.md (all, with the Units, Course-level checks, Cross-subject and For the lead sections).
- The psy- rows of data/progressions/social-studies.csv (assumes and cross_subject columns, and the notes of
  psy-heredity-environment, psy-sensation, psy-thinking, psy-social-cognition).
- data/standards/apa-hs-psych-2022.txt: all 141 targets and the seven themes, checked against every end-of-unit
  prompt list.
- docs/courses/CALENDAR.md (the grade 12 rows), data/plans/calendar.csv (psychology rows), data/plans/frames.csv
  (psychology row), and data/plans/english-language-arts-grade-12/days.csv days 133 to 160 (for the informed action's
  calendar claim).
- Earlier reads of the same layer for repeat tags: the sequence reads of Economics, US History II, US Government and
  Politics and World History II (2026-11-14); docs/reviews/frame-psychology-2026-11-16.md exists and was not re-argued.
- Gates, filtered to this course: `scripts/sequence.py check psychology`: 0 failures. `scripts/plan.py check`:
  psychology sequence 0 failures, frame 0 failures, "16 units, 160 days (156 in units, 4 for checks and respond
  days)" (the one plan.py failure printed belongs to another course). `scripts/frame.py calendar`: psychology checks
  in weeks 17 and 32, stagger breaks none. `scripts/stale.py check`: 0 failures.
- No outside source was fetched for this read. Findings rest on the standard text in the repo, the frame and the
  writer's own files; where a finding leans on teaching judgment it is marked so.

## Verdict

The scope and sequence is sound and close to ready: the units, days and owned rows match the frame, every unit opens
on its compelling question and closes on an unseen study with a respond day, the readiness and retrieval calls are
right by grade number for both placements, and the sensitive units carry their notes day by day. The biggest risk is
in the assessment reservations: about fifteen end-of-unit prompts ask for one part where the code names two or
three ("basic or applied" for a code that says both), and the mid-year check claims an intelligence code it does not
sample, so unit plan writers would build items that miss parts of owned codes. The one change that matters most is
to rewrite those prompt lists part by part (finding 1); the day 7 and day 9 swap (finding 2) is the one order fix.

## Findings, most serious first

### 1. End-of-unit prompts ask one part where the code names two or more (moderate; firm). LAYER sequence. REPEAT yes (a code met in part, World History II finding 1)

What is wrong. The brief asks that every end-of-unit task asks about each part of each code it lists. The prompt
lists in the end-day notes often turn the standard's "and" into "or", or name one of several parts:

| Day | Code (standard text) | Prompt as written | Part missed |
|---|---|---|---|
| 12, 13 | SI.2.1 (the five methods: experiments, correlational studies, surveys, case studies, naturalistic observation) | the proposal (one design); day 13 does not list SI.2.1 | four of the five methods |
| 13 | SI.1.3 (why both basic and applied research, with people and with animals, is worth doing) | "basic or applied, people or animals" | the second of each pair |
| 24 | BIO.1.2 (the parts of a neuron, and how a signal passes) | "a signal across the synapse" | the parts of a neuron |
| 35 | PER.2.2 (depth cues that need two eyes and those that need one) | "a depth cue" | one of the two kinds |
| 46 | CON.2.3 (theories of why we sleep and why we dream) | "two theories compared" | sleep or dream, whichever is not asked |
| 54 | LRN.1.2, LRN.2.2 (clinical and experimental examples) | "its experimental or clinical use" | one of the two |
| 71 | LAN.1.3 (how children acquire language and the theories of how) | "a theory of acquisition" | acquisition itself, and the theories set against each other |
| 102 | MOT.2.1 (eating and sexual behavior) | "eating (no weights or calories)" | sexual motivation |
| 102 | MOT.2.2 (achievement and affiliation) | "achievement or affiliation" | one of the two |
| 102 | MOT.4.2 (culture and gender) | "a cultural or gender" influence | one of the two |
| 149 | DIS.1.5 (the person, the family and society) | "an effect on family or society" | the person, and one of the other two |
| 139 | HLT.1.3 (bodily and psychological results) | "a health result" | one of the two |
| 139 | HLT.1.4 (bodily, thinking and behavioral ways of coping) | "a coping way with its evidence" | two of the three |

Why it matters. The unit plan writes its items from these notes. A busy writer reads "basic or applied" and writes
one item, so the owned code is checked in part and the record says it is met. MOT.2.1 is the one a writer is most
likely to drop on purpose, since sexual motivation is the sensitive half; it still needs an item, set as research on
a made-up finding.

Fix (settled below, item level). Rewrite each prompt with "and" as the standard has it, one short prompt per part
(no day added): day 13 adds "SI.2.1: match each of the five methods to a question it can and cannot answer" and
"why basic and why applied research, and why with people and why with animals (SI.1.3)"; day 24 "the parts of a
neuron and a signal across the synapse"; day 35 "a two-eye and a one-eye depth cue"; day 46 "a theory of sleep and a
theory of dreams, each with its evidence"; day 54 "an experimental and a clinical example of each"; day 71 "a stage
of acquisition and two theories compared"; day 102 "eating and sexual motivation, each as a research finding on a
made-up case, within the school's policy (MOT.2.1)", "achievement and affiliation (MOT.2.2)", "a cultural and a
gender influence (MOT.4.2)"; day 149 "an effect on the person, the family and society"; day 139 "a bodily and a
psychological result (HLT.1.3)" and "a bodily, a thinking and a behavioral way of coping (HLT.1.4)".

### 2. Day 7 teaches the replication crisis in significance terms two days before significance is taught (moderate; likely). LAYER sequence. REPEAT yes (used before taught, Economics finding 5)

What is wrong. Day 7's reading turns on "97 percent of the originals reported a significant result, about 36
percent of the replications did" and on smaller replicated effects. Significance in words and effect size are first
taught on day 9. The pooled class data collected on day 6 also wait three days for the statistics day.

Why it matters. Students meet the course's central evidence for theme A without the idea it rests on, and the
teacher has to pre-teach significance in the replication lesson, which crowds it.

Fix (settled below, a day swap inside the unit). Swap the work of days 7 and 9: day 7 becomes descriptive statistics
on the day 6 class data, graphs, correlation against causation, significance in words with effect size (SI.4.1 to
SI.4.3, retrieval of the three Algebra I rows and of math:alg2-experiments-significance, which now opens on the day
that uses it, not on day 6); day 8 stays ethics; day 9 becomes replication and the crisis (SI.2.3, themes A and B),
read with significance and effect size in hand, leading straight into day 10's news study. Update the scope's
readiness table ("days 5 and 6" becomes "days 5 and 7"; "day 9" becomes "day 7"), the unit 1 arc sentence ("data
analysis comes last" becomes "the statistics come straight after the class task, so the replication crisis is read
with significance and effect size in hand"), the day 1 note's "retrieval on day 9" and the source map (2.3 on day 7;
the unit 1 `ours` row lists 9; 10-14).

### 3. The mid-year check claims an intelligence code it does not sample, and the year-end goal claims more than its codes (moderate; firm). LAYER frame and sequence. REPEAT new

What is wrong. Day 81 lists APA22.INT.2.3 (the reliability and validity evidence for intelligence test scores) and
sets its unit 8 item as "validity and reliability asked of a memory or perception measure". That item samples
SI.2.5, already on the list; it says nothing about intelligence test scores. The frame's checks table asks for this,
so the fault starts there. No course-level check then samples unit 8 at all, since day 159 lists no INT code. Day
159's goal says "short items from each unit", but its codes carry units 1, 5, 6 and 9 to 16 only (units 2, 3, 4, 7
and 8 appear only through themes C and E).

Why it matters. Rule 2 says a check lists only what it samples. The report a teacher reads would show INT.2.3
checked twice when it was checked once, and unit 8 (the course's hard-history unit) would never come back.

Fix (settled below). Day 81 drops INT.2.3 and its note says "unit 8 is not resampled here, two days after its
sitting; it returns at year end". Day 159 adds one unit 8 item set in later content: stereotype threat and its mixed
record read as one measured effect of stereotypes in unit 13's content (INT.3.2). Day 159's goal reads "short items
from each of units 9 to 16, and items on units 1, 5, 6 and 8 set inside later content", matching its codes. The
frame's checks table, row 1, changes its sentence the same way (For the lead).

### 4. The year-end check repeats the task form of the last two unit sittings (moderate; likely). LAYER sequence. REPEAT yes (a check repeating a recent task form, World History II finding 4)

What is wrong. Rule 2: a course-level check never repeats a task form given in the last two weeks. Day 159's lead
task is "one unseen study ... judged with the research-design model, with short items", the same form as day 149
(an unseen study of diagnosis or prevalence, short items) and day 157 (an unseen treatment trial summary, short
items), both inside the ten school days before it. At mid-year, day 81's "unseen data graph" sits two days after day
79's "unseen ... score report", which a student reads the same way. The scope says only that the proposal and the
informed action forms are not repeated.

Why it matters. Students see the same task three times in ten days, and the year-end check measures how well they
know that one format rather than whether the year's thinking transfers.

Fix (settled below). Day 159's lead task becomes a corroboration task: an unseen claim in the news set against two
short unseen study summaries that disagree, judged with the research-design and biopsychosocial models (the form
last used in unit 1 and on the informed action, more than two weeks back); the short items and theme items stay.
Day 79's sitting reads "an unseen testing-history source" (drop "or score report"), so day 81's graph is not a
repeat. The scope's check sections say so in one line each.

### 5. Five days hold more than one lesson's work (moderate; likely). LAYER sequence. REPEAT yes (crowded days, Economics finding 3, US History II finding 3)

What is wrong, with the counts.
- Day 72: the hook, the construct (INT.1.1) and five theories weighed by evidence (g, fluid and crystallized,
  multiple, triarchic, emotional), while day 73 holds one target (INT.1.3).
- Day 93: the hook and six accounts of motivation (drive reduction, arousal, incentives, intrinsic and extrinsic,
  self-determination, the hierarchy of needs against its evidence).
- Day 116: the obedience studies, their variations, the partial replication, the archival reanalyses, and the
  prison simulation with its critique: two classic studies and three critiques.
- Days 58 and 119: each first-teaches its target and its check-set case (wrongful convictions; the corrected
  bystander account and newer research) and also writes a claim-evidence-reasoning paragraph.

Why it matters. A 50-minute day that first-teaches five theories, or two classic studies with their critiques, ends
with the critique cut, and the critique is what this course promises (the values rule and the lens's "no study
without its replication record").

Fix. Day 72 and 73 (settled below): day 72 keeps the hook, the construct and general, fluid and crystallized
intelligence; multiple intelligences, the triarchic theory and emotional intelligence move to day 73, weighed by
evidence beside how differences bear on everyday life (day 73 adds INT.1.2). For the unit plans to confirm, not
settled here: day 93 keeps the hook with drive reduction, arousal and incentives, and the unit plan places
intrinsic and extrinsic motivation and self-determination beside the mindset evidence on day 96; day 116's prison
simulation moves to day 115 under deindividuation, or the unit plan shows both studies and their critiques fit; days
58 and 119 either shorten the paragraph to a three-sentence claim-evidence-reasoning exit or move it to the next
day's opening.

### 6. The source map leaves most order changes inside units unrecorded (minor; firm). LAYER base text. REPEAT yes (World History II finding 7)

What is wrong. The brief keeps the base text's order unless a reason is given, and the scope says "where the course
order differs from the book's ... the row gives the reason". The rows give it for the chapter moves only. Inside
units, these rows change the book's order with `order_conflict` blank: 2.4 before 2.3 (ethics before analyzing
findings, days 8 and 9); 3.3 before 3.2 (days 15 and 16); 4.6 before 4.2 (day 38); 7.3 and 7.4 before 7.2 (language
after problem solving, days 64 to 68); 8.4 before 8.3 (day 57); 11.6 and 11.4 before 11.2, 11.3 and 11.5 (days 104
to 107); 15.3 before 15.2 (days 142 and 144); 16.2 and 16.3 before 16.1 (day 154).

Why it matters. Small, but the source map is the record an adopter or a later reviewer checks first, and the
scope's sentence claims more than the rows hold.

Fix (settled below). Fill `order_conflict` and `harms_learning` on those rows with the reasons the arcs already
give (for example 15.3: "models before classification, so a label is read with the model that explains it"; no) and
recheck them after the day 7 and 9 swap in finding 2, which puts 2.3 back before 2.4.

### 7. Two Shorter path folds do not say where their work goes (minor; likely). LAYER sequence. REPEAT new

What is wrong. The fold of day 116 into day 115 names the obedience study, one critique and the variations, but not
the prison simulation and its critique, which the frame requires and day 116 holds; on the shortened year it has
no home. The fold of day 60 spreads a 50-minute practice set over the warm-ups of days 61 to 71, but DEFAULTS.md
keeps a warm-up for one repair of at most five minutes, so the two compete for the same slot.

Why it matters. A teacher on the shorter year would drop the prison simulation without knowing it was required, and
the warm-ups would overrun.

Fix (settled below). The day 116 row adds "the prison simulation and its critique become the at-home reading, with
one exit question on day 115". The day 60 row reads "the set spread over the exit tickets and at-home work of days
63 to 71, never in a warm-up that holds a repair". The rest of the section is right: the folds track the standard's
priority areas (units 3, 4 and 7's language days and unit 11 are non-priority), the total is 500 minutes against
160 days, and no fold takes a draft, feedback, revision, end, respond day or a day of units 14 to 16.

### 8. Loose and stale lines (minor; firm). LAYER sequence and frame. REPEAT yes (stale notes appear in most earlier reads)

- Day 14's note lists the four Biology rows only; for a grade 11 class, science:bio-sources-of-variation joins the
  check (the scope and day 21 say so). Add "Grade 11 placement: plus science:bio-sources-of-variation."
- The frame tells the counselor before the course opens and before units 9, 12, 13 and 14 to 16. No day or scope
  line places the first telling, and before unit 9 only day 89 says it. Day 1's note adds "the counselor was told
  before the course opened, with units 9, 12, 13 and 14 to 16"; day 82's note adds "counselor told today, before
  unit 9".
- The family notes for unit 10 (day 95) and unit 13 are not tied to a day ("before this day"; "went home with unit
  12"). Name the day: day 93 for unit 10, day 121 for unit 13, as day 42 does for unit 4.
- Day 117's note "Government (fall) met public opinion and polarization" is true only for a grade 12 class. Add "for
  a grade 12 class; a grade 11 student meets polarization here first".
- Frame, not the scope: the frame's list of ELA 12 research milestone days (135, 145, 147, 150 to 156, 158) is stale
  against ELA 12's days.csv (its mid-unit check is day 142 and an end day is 159; 135, 145 and 147 are Application
  days). Days 137 and 138 stay clear either way, so nothing moves.
- Frame, not the scope: British spellings ("behaviour" in unit 15's compelling question, which data/plans/calendar.csv
  already carries; also "colour", "labelled", "modelling", "practise", "behavioural", "organisation", "centre",
  "ageing", "catalogue"). The scope and days use US spelling; the frame should too before the unit plans copy it.
- Frame, not the scope: the senior-calendar bullet says an early-end fold drops "one Application day of study
  reading", but units 9 to 13 have no such day (every candidate is Understanding), and the scope folds one
  Understanding day each. The frame sentence reads "merging that unit's check-set day, or for unit 11 its lightest
  owned day, into a neighbor".

## The lens checklist, scope and sequence layer

| Line | Met? |
|---|---|
| A unit question can be answered without the unit's sources, or has one defensible answer | Met: each question needs the unit's studies, and units 5, 8, 10, 11 and 12 set disagreeing evidence side by side |
| History out of time order with no reason | Met: unit 8 puts testing history before the statistics with a reason; unit 9 runs the life span in order, emerging adulthood last with a reason |
| A contested event given one telling | Met: every classic study is read with its critique on the same day (Little Albert, Bobo doll, marshmallow, facial feedback, basic emotions, Asch, Milgram, the prison simulation, the bystander case, implicit bias, serotonin) |
| Writing from sources once a year, or not building short to long | Met: a paragraph (day 10), the proposal (11 and 12), paragraphs (58, 75, 119), the informed action (137 and 138) |
| Psychology: an APA22 target or theme with no unit | Met: all 141 targets and 7 themes on a day and an end day (gate and my count) |
| Psychology: priority areas not weighted in the days | Met: the priority units run at about one teaching day a target; the Shorter path folds come from non-priority areas or check-set days |
| Psychology: a study taught without its sample and replication record | Met at this layer: every named classic study carries its replication or critique in the note; the unit plans carry the samples |
| Inquiry arc and informed action once a year | Met: unit 14, student-chosen, two days, look back on day 160 |
| Sensitive and hard history named in the notes | Met: every flagged day in the scope's Sensitivity list has its note; eugenics named plainly with Buck v. Bell, the dissent and Skinner |

## The brief's checks, briefly

- Order inside each unit: met except finding 2.
- Assessments: an end per unit, response time once on a respond day, no mid-unit needed (no unit over 25 days);
  parts: finding 1.
- Readiness or retrieval: right for both placements. Grade 12: the US History I, Algebra II and Algebra I (through
  one hop) rows are grade 11, so retrieval; the four Biology rows and s8-senses-brain are grade 9, so readiness on
  days 14 and 25 (respond days, the day before each unit). bio-sources-of-variation (grade 11 through Physics) is
  retrieval on day 21; bio-homeostasis-feedback is retrieved on days 39 and 131 as used earlier this year. No unit
  checks a year-before row or retrieves an older one; no readiness check sits on a first day or more than a day
  ahead. Grade 11: the Algebra I check on day 1 after the hook is the right call under the math-lean rule.
- Checks that do not repeat: both checks draw the just-assessed unit from earlier content and say so (findings 3 and
  4 on what they claim and their forms).
- Standards in full: every owned code on a day (the course owns no lettered codes).
- Days by load: unit loads follow the frame; finding 5 for days inside units.
- Calendar: checks in weeks 17 and 32 as CALENDAR.md sets; no same-year lean (all leans are earlier-grade core
  courses); the informed action is clear of ELA 12's milestones.
- Candidate cells: all 16 settled, 5 kept at 1 day (days 3, 90, 96, 116, 124), 11 kept at 0 days inside an owned day.
- Shorter path: present and sound except finding 7.
- Source map: every section placed or cut with a reason; finding 6 for order.
- Stale notes: stale.py clean; finding 8.

## What is right and should not be touched

- The readiness and retrieval table, with the grade 11 placement written out row by row.
- The writing thread and the claim-evidence-reasoning model returning across the year.
- The two-part end assessments in units 1 and 14 (a revised product plus a sitting), with feedback by the next
  lesson.
- The look back on the informed action on day 160, three weeks after it is shared, which gives it time to land.
- The mental health notes repeated on every day of units 14 to 16, the counselor tellings on each respond day before
  a flagged unit, and the help list going home.
- The informed action kept clear of ELA 12's research milestone days.

## What I could not judge

- Whether each named replication record is current as of today: the frame dates it 2026-11-16 and gives the unit
  writer the recheck; I did not fetch the studies.
- The fit of minute budgets inside each day (the unit plans set them).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Rewrite the end-day prompt lists part by part, as in finding 1 (days 12 or 13, 24, 35, 46, 54, 71, 102, 139, 149) | each part of each code gets a prompt; no day added | data/plans/psychology/days.csv |
| Swap the work of days 7 and 9 (statistics on day 7, replication on day 9); math:alg2-experiments-significance retrieval moves from day 6 to day 7 | significance and effect size taught before the replication crisis uses them | days.csv; scope-and-sequence.md (readiness table, unit 1 arc); source-map.csv (2.3 and the unit 1 ours row) |
| Day 81 drops APA22.INT.2.3; day 159 adds APA22.INT.3.2 set in unit 13 content; day 159's goal names the units its codes carry | a check lists only what it samples, and unit 8 returns once | days.csv; scope-and-sequence.md (both check sections) |
| Day 159's lead task becomes a news claim set against two disagreeing unseen study summaries; day 79 reads "an unseen testing-history source" only | no course-level check repeats a form from the last two weeks | days.csv; scope-and-sequence.md (units 8, check 1, check 2) |
| Multiple intelligences, the triarchic theory and emotional intelligence move from day 72 to day 73 (day 73 adds INT.1.2) | day 72 held a hook and five theories, day 73 one target | days.csv |
| Fill order_conflict and harms_learning on rows 2.4, 3.3, 4.6, 7.2, 8.4, 11.2 to 11.6, 15.2, 15.3 and 16.1 | the base order is kept unless a reason is given | data/plans/psychology/source-map.csv |
| Shorter path: day 116's fold places the prison simulation as at-home reading; day 60's fold uses exits and at-home work, not warm-ups | nothing required lost, no clash with the repair slot | scope-and-sequence.md |
| The loose lines in finding 8 that touch days.csv (days 1, 14, 82, 93, 117, 121) | notes match the frame's rules | days.csv |

## For the lead

- The writer's item 1 (unit 8's "the day before the mid-year check"): agree. The frame cell reads "set as the last
  sitting before the mid-year check"; the scope already does this.
- The writer's item 2 (TOOL-ASKS.md): agree that the scope should not write it. In the courses that have one, the
  unit plan writes it (docs/pipeline/briefs/plan.md and the plan-codex briefs own TOOL-ASKS.md). The frame's Tools
  bullet reads "the unit plans write TOOL-ASKS.md from them". The writer's list of tools is partial (it leaves out
  the study-graph reader, signal-detection score sheet, synapse diagram, word-list task, inventory comparison,
  critique reader, information-piece template and treatment-evidence table); the frame's list is the one to use.
- From this read, frame lines for the frame's owner: the checks table row 1 (finding 3), the stale ELA 12 milestone
  list, the British spellings and the early-end fold sentence (finding 8).

## For Cory

None.

## Sources

- data/standards/apa-hs-psych-2022.txt (the American Psychological Association's 2022 national standards for high
  school psychology, in our own words in the repo): every part check in finding 1.
- docs/courses/psychology/frame.md and data/progressions/social-studies.csv: units, rows, leans, readiness counts.
- docs/courses/CALENDAR.md, data/plans/calendar.csv, data/plans/english-language-arts-grade-12/days.csv: the
  calendar checks.
- Earlier sequence reads in docs/reviews/ (Economics, US History II, US Government and Politics, World History II,
  2026-11-14): repeat tags only.

For the source list: nothing new.
