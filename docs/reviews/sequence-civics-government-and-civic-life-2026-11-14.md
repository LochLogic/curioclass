# Sequence read: Civics, Government and Civic Life (grade 8), 2026-11-14

Expert cold read of the scope and sequence, per docs/pipeline/briefs/sequence-read.md. Independent of any other read of
this course's scope and sequence (the Codex read was not opened).

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, the social studies part of
  docs/ADOPTION-BAR-SUBJECTS.md (with the shared core and pass rule), docs/courses/social-studies/STANDARD.md.
- docs/courses/civics-government-and-civic-life/scope-and-sequence.md and
  data/plans/civics-government-and-civic-life/days.csv, cold, in full.
- Beside them: the frame (docs/courses/civics-government-and-civic-life/frame.md), the grade 8 rows of
  data/progressions/social-studies.csv and the rows they assume (ss5-revolution-causes, ss5-independence-war,
  ss5-constitution, ss5-civil-war, ss5-reconstruction-amendments, ss5-civil-rights-movements, ss7-rome-fall and their
  users), the grade 8 standards in data/standards/ma-hss-2018.txt, docs/courses/CALENDAR.md, the grade 8 rows of
  data/plans/calendar.csv, the English language arts grade 8 frame's lean rows, docs/pipeline/briefs/sequence-write.md,
  the frame read for this course, and this day's grade 6 and grade 7 sequence reads for REPEAT.
- Gates: `plan.py check` passes for this course (0 failures; the run exits 1 on one STALE note in
  docs/courses/us-history-ii/frame.md:78, not this course). `frame.py calendar`: grade 8 social studies checks in weeks
  10, 20 and 29 to 30; no stagger break. `stale.py check`: none here.

## Verdict

Sound and close to ready: every code and lettered part has a day, the year runs from roots to founding to the
Constitution, rights, federalism, the press and a real civic action, the frame read's fixes are carried into the days,
and the writing grows from a claim weighed against counterclaims (unit 1) to a court research report (unit 6) and a
proposal for an outside audience (unit 10). The biggest risk is again assessment stacking: all three course-level checks
repeat the end-of-unit assessment set a few days before. The writer's two flagged squeezes are real: unit 7's split
fits the days but lands its cut in the wrong place, and unit 10's assessment sits where rehearsal should be, with its
respond day after the presentation it should improve. Both are fixed by swaps inside the unit, with no day added.

## Findings

### 1. Each course-level check repeats the end-of-unit assessment held days before it

- **LAYER** sequence. **REPEAT** yes (grade 6 finding 1, grade 7 finding 1). **Confidence** likely.
- **What is wrong.** Day 46 (unit 3): "the branches and their checks applied to an unseen case"; day 49 (check 1, day
  2): "the branches and their checks applied to an unseen case". Day 94 (unit 6): "an amendment's change explained from
  an unseen document ... a short argument from an unseen opinion excerpt"; day 97 (check 2, day 2): "an amendment's
  change from an unseen document, and a short argument from an unseen opinion excerpt". Day 143 (unit 9): "an unseen
  claim read laterally, and an unseen editorial analysed"; days 145 and 146 (check 3): lateral reading of an unseen
  claim, and an unseen editorial analysed.
- **Why it matters.** Each check reports the unit just taught twice, two to four days apart, instead of what has
  lasted from the units before it. The pattern now runs through all three courses, so it is a brief-level habit.
- **Fix (no day moves).** Check 1's branches item uses a founding-era case from units 1 or 2 (the Articles'
  weaknesses, or a colonial grievance read as a separation-of-powers question). Check 2's amendment item takes an
  amendment from unit 4 or 5 (the Bill of Rights, the First Amendment), and its argument item an opinion excerpt tied to
  unit 4 or 5, not unit 6's cases. Check 3's lateral reading and editorial items take a claim or editorial on a unit 7
  or 8 topic (a state budget fight, an election claim). The process fix, for the lead: sequence-write.md can say that a
  course-level check's items for a skill the preceding unit has just assessed draw content from earlier units. Settled
  below.

### 2. Readiness checks where the rule calls for retrieval, and the reverse

- **LAYER** frame. **REPEAT** yes (grade 6 finding 2, grade 7 finding 3, the same rule). **Confidence** firm.
- **What is wrong.** The days open five units with a readiness check, each "as the frame sets". Under sequence-write
  rule 2, read as two or more whole grades idle between the last use and this course:
  - Day 1, ss7-rome-fall's counterclaim move: used in grade 7, the year before. Retrieval task.
  - Day 16, ss5-revolution-causes and ss5-independence-war: idle in grades 6 and 7. Readiness check, right. But
    ss5-constitution is listed with them, and grade 7 used it (ss7-roman-republic). It should leave this check.
  - Day 31, ss5-constitution: used in grade 7 and again in this course's unit 2. Retrieval task.
  - Day 77, ss5-civil-war, ss5-reconstruction-amendments, ss5-civil-rights-movements: idle in grades 6 and 7.
    Readiness check, right. The writer is right here; the progression handoff text for ss8-amendments-civil-war, which
    says retrieval, is what is wrong.
  - Day 100, ss5-constitution: used this year in units 2 and 3. Retrieval task.
- **The right call (the writers' disagreement with the frames).** The rule, not the frame, governs. Readiness checks
  are for real gaps of two grades or more (days 16 and 77); anything used the year before or already this year opens
  with a retrieval task (days 1, 31 and 100).
- **Fix.** days.csv: day 1 opens "Retrieval task on naming the strongest counterclaim (grade 7)", assess blank; day 16
  drops ss5-constitution from the goal and note; days 31 and 100 open with a retrieval task, assess blank. frame.md:
  the Seams rows and unit cells for units 1, 3 and 7 say retrieval task. data/progressions/social-studies.csv: the
  handoff for ss8-haudenosaunee-influence (on ss7-rome-fall) says retrieval; the handoff for ss8-amendments-civil-war
  says readiness check. Settled below.

### 3. Unit 7: the squeezed split fits, but the cut lands in the wrong place

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** The frame's about 5/3/6/6 cannot fit unit 7's twenty days with its opening and assessment days;
  the writer's total is right. But the cut overloads day 113 ("Tax-supported services, and public goods and spillovers
  shown on a supply-demand graph; a sample pay stub's withholding"), which is three ideas and a graph in 50 minutes.
  And the compelling question, "who should decide, the nation, the state or the town?", is bolted onto the end of
  day 117, a budget-weighing day, so the unit's central argument gets a few minutes.
- **Why it matters.** Public goods and spillovers on a graph is D2.Eco.8's whole demand; done in a third of a day it
  becomes a definition. A compelling question answered in the last minutes is not argued.
- **Fix (a day swap inside the unit).** Day 100 turns from a readiness check into a retrieval task (finding 2), which
  frees room: fold day 108's federal, state and local duties (MA.8.T6.7) into day 100 beside MA.8.T6.1, since both are
  "who does what". Answer the compelling question at the end of day 112, which already asks whether each procedure does
  its job, and is where the evidence sits. Split day 113 into two days: public goods and spillovers on the graph; then
  tax-supported services and the pay stub. Day 117 keeps the budget weighing only. The split becomes about 5/3/4/6
  (state and local government over four days, the budget over six); the frame note should read "about 5/3/4/6".
  Settled below.

### 4. Unit 10: the assessment takes the rehearsal's place, and its respond day comes after the presentation

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Days 154 (build) and 155 (rehearse) are followed by the end-of-unit assessment on day 156, then
  the presentation on day 157, then the respond day on day 158. The assessment breaks the run from rehearsal to
  presentation, and the reteaching it prompts arrives after the one product it could improve.
- **Why it matters.** The respond day exists to act on what the assessment showed; here nothing can be acted on. And
  the day before a presentation to a school board or an official is the day students most need for final revision.
- **Fix (a day swap inside the unit).** All the analysis the assessment tests (three levels, levers, procedures) is
  taught by day 153. So: days 149 to 153 as now; 154 end-of-unit assessment; 155 respond day; 156 build the proposal;
  157 rehearse and revise; 158 present; 159 follow up; 160 look-back. The frame's "by about day 157" holds within its
  "about"; if the teacher has booked day 157, days 156 and 157 merge build and rehearse and the presentation stays on
  157. The frame read's earlier worry stands: a look-back two days after the presentation may come before any reply,
  which the day's goal already allows ("or what is still pending"). Settled below.

### 5. Day 12 asks for counterclaims answered in full with no model before it

- **LAYER** sequence. **REPEAT** new. **Confidence** a judgment call.
- **What is wrong.** Day 11 teaches judging whether historians' evidence is enough; day 12 asks students to "write a
  claim ... weighed against the counterclaims, each answered in full". No day shows what answering a counterclaim in
  full looks like, and ELA 8's counterclaim work comes later (by about day 62).
- **Why it matters.** The lens asks that no claim be required before it is modelled. This is the year's first written
  argument, and the move is new at this length.
- **Fix.** Day 12 opens with a short worked model: concede what the counterclaim's evidence shows, then answer it with
  stronger evidence. No day added. Settled below.

## Days by load

Teaching days follow the owned parts: unit 1's roots over the Greek, Roman, English and Haudenosaunee strands with a
claim day; unit 2's causes, the Declaration and the Articles; unit 3's text, branches, implied powers and judicial
review; unit 4 and 5's rights with the Bill of Rights cases; unit 6's amendments, civil rights laws and the research
run; unit 8's elections and parties; unit 9's press and news literacy. The two runs under load are unit 7's day 113
(finding 3) and unit 10's last week (finding 4).

## The calendar and leans

- Checks on target weeks 10, 20 and 29 to 30 (days 48 to 51, 96 to 99, 145 to 148), check 3 before unit 10 as
  CALENDAR.md sets. ELA 8 (89, 90, 125, 126), math 8 (70, 116) and science 8 (75) share no school day with them.
- Leans checked against calendar.csv and the ELA 8 frame: ELA 8's argument with counterclaims in unit 2 (days 31 to
  62) before civics leans on it after day 62; the research routine taught in ELA 8 unit 3's first two weeks (63 to 76)
  before civics unit 6 (77) uses it, with publishing held to about day 84; point of view and editorial claims before
  unit 9. All met.
- The held look-back days shift no unit boundary across a lean window or a check week, so the right call is the same
  as grades 6 and 7: keep days.csv as written; frame.py should build calendar.csv's ranges from days.csv once one exists.

## Candidate cells

All settled: Blackstone on day 7; the civics test on half of day 65; incorporation on day 80; Federalist No. 51 and
Brutus No. 1 placed on day 25 (unit 2). Agreed with each.

## Other checks

- The student's own state: taught by method with several states as worked examples, Massachusetts one of them, and
  each state's own pages linked. Right for a national course.
- Native nations as present-day governments (Cory's call) are carried on days 103 and 104, from the nations' own pages.
- Values rule: the flag salute cases (day 87) say Barnette stands over Gobitis; the 2015 marriage ruling (day 83) stands
  as decided law, taught without asking a student's own views.
- Since Time Immemorial is listed in docs/BASE-TEXTS.md (CC BY 4.0).

## The lens checklist (scope and sequence layer)

| Line | Met, missed or not applicable |
|---|---|
| A unit question answerable without the unit's sources, or with one defensible answer | Met; unit 7's question needs its own time (finding 3) |
| History out of time order with no reason | Met: the roots unit runs back from the founders' own reading, a stated reason |
| A contested event given one telling only | Met: the Haudenosaunee influence question with both historians' sides; Black historians' scholarship on the founding and on Reconstruction |
| Writing from sources once a year or never building from short to long | Met: claim on day 12, short claims each unit, the research report (unit 6), the proposal (unit 10) |

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Check items for the repeated skill draw on earlier units (check 1: units 1 or 2; check 2: units 4 or 5; check 3: units 7 or 8) | A check measures what lasted | days.csv days 49, 97, 145, 146; scope-and-sequence.md check sections |
| Days 1, 31 and 100 open with a retrieval task; days 16 (without ss5-constitution) and 77 keep a readiness check | Rule 2: readiness only for two idle grades | days.csv days 1, 16, 31, 77, 100; frame.md Seams and unit cells; social-studies.csv handoffs for ss8-haudenosaunee-influence and ss8-amendments-civil-war |
| Unit 7 at about 5/3/4/6: day 108 into day 100, the compelling question on day 112, day 113 split in two, day 117 budget only | Day 113 overloaded; the question needs its evidence day | days.csv days 100 to 117; scope-and-sequence.md unit 7; frame.md unit 7 note |
| Unit 10: assessment 154, respond 155, build 156, rehearse 157, present 158 | Feedback before the product; rehearsal next to the presentation | days.csv days 154 to 158; scope-and-sequence.md unit 10 |
| Day 12 opens with a worked model of answering a counterclaim | No claim move asked before it is modelled | days.csv day 12 |
| Keep the held look-back days; the calendar follows days.csv | No check week or lean window moves | none here (frame.py) |

## For Cory

Nothing. Every finding is an item-level or process choice.

## What I could not judge

Whether a school board or official can be booked for day 158 rather than 157; the fix leaves room for either.
Outside sources were not re-fetched on this run; none of the findings rests on one.
