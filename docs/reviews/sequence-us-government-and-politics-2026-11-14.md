# Sequence read: us-government-and-politics (United States Government and Politics, half year), 2026-11-14

Expert cold read per docs/pipeline/briefs/sequence-read.md. Independent of any other read of this scope and sequence.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the social studies part of
docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md; docs/courses/us-government-and-politics/frame.md;
docs/courses/us-government-and-politics/scope-and-sequence.md; data/plans/us-government-and-politics/days.csv (all 80
rows); the gov-* rows and the ss8 rows they build on in data/progressions/social-studies.csv; the MA.GOV and MA.NML lines
of data/standards/ma-hss-2018.txt; docs/courses/CALENDAR.md and the grade 12 rows of data/plans/calendar.csv; the
English Language Arts grade 12 frame's leans on Government (docs/courses/english-language-arts-grade-12/frame.md);
docs/pipeline/briefs/sequence-write.md (rule 2); docs/GLOSSARY.md (readiness check, retrieval task); the earlier frame
read docs/reviews/frame-us-government-and-politics-2026-11-13.md.

Gates: `plan.py check`: sequence us-government-and-politics 0 failures, frame 0 failures. `plan.py check` as a whole
exits 1 on one stale note in docs/courses/us-history-ii/frame.md (not this course). Every unit's first and last day in
days.csv matches data/plans/calendar.csv. CALENDAR rule 4: week 16 is the half's finals week and may hold checks; no
other rule for grades 9 to 12, none broken.

## Verdict

A sound fall half: the anchor's order is kept, every MA.GOV and MA.NML code and every owned C3 indicator is on a named
day and in its unit's end-of-unit assessment, each assessment opens with an unseen source, and unit 9 writes both routes
(optional outside expert, a paper path complete on its own) into the same seven days, as Cory settled. The biggest risk
is the informed action's timing: a letter or comment sent on day 76 or 77 is looked back on by day 80, three school days
later, so the look back will almost always record silence. The one change that matters most: send the team's first
contact with the named office in unit 8 (day 68) and match the action route to a real meeting date, so day 80 has a
response to look back on.

## Findings, most serious first

### 1. The look back on the action comes three school days after it (moderate; likely). LAYER sequence. REPEAT new

**What is wrong.** Day 76 (no expert route) has the team "write to a named office by letter through an adult"; day 77
takes the action (a public comment, a letter sent through an adult, a proposal); day 80 holds the look back on "what
changed, the response or its absence". A letter sent through an adult on day 77 reaches the office about day 79. A
public comment needs a public meeting, and nothing in unit 8 or 9 checks when the local body next meets.

**Why it matters.** The bar's informed-action item asks for an action and a look back at what happened. The frame
already says no visible change is needed, so the action still counts; but a look back on silence every year teaches
that officials never answer, which is the wrong civic lesson, and a team whose meeting falls after day 80 cannot take
the comment route at all.

**Fix (days.csv rows 66, 68, 77, 80; scope-and-sequence.md unit 8 and unit 9 arcs).** (a) Day 66, after the team picks
its issue: "find the body that decides it and the date of its next public meeting" (one added clause, no added time;
the paper path uses a printed agenda the teacher supplies). (b) Day 68: one of the three gathering routes becomes "an
information request to the named office, sent through an adult", so a reply has about two and a half weeks to arrive by
day 80. (c) Day 77: the public comment route is taken at the meeting found on day 66 where it falls in weeks 15 and 16,
or given as a written comment the body accepts in place of speaking (most local bodies take written comment). (d) Day
80 looks back on both the day 68 request and the day 77 action. Confidence: likely (mail and meeting timing; written
public comment practice from memory of typical town and school board rules, not checked for any one state).

### 2. "Outside collaborator" is still required in four places (moderate; firm). LAYER frame. REPEAT new

**What is wrong.** Cory settled that the outside expert is optional (frame, For the lead 1, 2026-11-14). The scope and
sequence's For the lead 2 catches one stale place, the course-level check 2 row. Three more remain: the frame's
inquiry-arc bullet ("Teams choose their local issue in unit 8 and arrange their outside collaborator before unit 9
begins"); the unit 9 row's teaching cell, which says students "collaborate through digital tools with an outside
expert" with no "optional"; and days.csv row 73, which says "outside collaborator if the teacher has arranged one" where
the scope and sequence says "outside expert".

**Why it matters.** A unit writer reading the frame first plans an outside contact as required and writes the paper
route as a lesser path, which is what Cory's call ruled out.

**Fix.** Accept For the lead 2 and extend it: (a) frame inquiry-arc bullet: "and arrange their outside collaborator
before unit 9 begins" becomes "and, where the teacher arranges an optional outside expert, the contact is set before
unit 9 begins"; (b) frame unit 9 row: "students collaborate through digital tools with an outside expert and other
contributors" becomes "students collaborate with contributors (classmates, and an outside expert where the teacher
arranges one), an adult mediating any outside contact; without one, NML.T5.5 is met in part, said plainly to the
teacher"; (c) days.csv row 73: "outside collaborator" becomes "outside expert".

### 3. Day 70 tests making a report and an editorial by reading a past policy (moderate; likely). LAYER sequence. REPEAT new

**What is wrong.** Day 70's end-of-unit assessment is "an unseen past policy and its record", and it lists MA.NML.T5.1
to T5.3 (gather information with advanced searches and interviews, write a factual report, write an editorial with a
visual). Those are production standards; a reading task on an unseen policy cannot show them.

**Why it matters.** C1 counts a code as assessed only when the task asks the student to do what the code says. As
written, T5.1 to T5.3 are taught on days 68 and 69 and never assessed.

**Fix (days.csv row 70; scope-and-sequence.md unit 8 assessment bullet).** Keep the unseen policy task for T4.6, T4.7,
NML.T4.4 and D2.Civ.13, and add: "with the day 68 search log and the day 69 report and editorial scored on the course
rubric for NML.T5.1 to T5.3". This mirrors unit 9, where the portfolio is scored beside the unseen case. No day added.

### 4. Unit 2's readiness check has no reteach path (minor; likely). LAYER frame. REPEAT new

**What is wrong.** Day 7 opens with a readiness check on three grade 8 rows (ss8-declaration, ss8-articles-convention,
ss8-ratification-debate) "with no reteach lesson, because the unit rereads the documents in full". Days 7 and 8 do
reread the Declaration and the Constitution, but day 9 says "Federalist 51 and Brutus No. 1 retrieved from grade 8":
it assumes those two essays rather than rereading them.

**Why it matters.** A student new to Curio Class, or one who missed grade 8's ratification unit, meets day 9 cold on
two dense essays. Unit 1 handles the same case with a reteach station (day 2); unit 2 should too.

**The right call for this course (the readiness versus retrieval question).** Readiness checks are right here in units
1 to 6 and 8: every ss8 row is idle two or more grades for a student in grade 11 or 12 (rule 2), and none was checked
earlier in the half. Unit 7's look back on wh2-wwii-consequences (grade 10) is rightly a retrieval task. Unit 2 keeps
its check, scoped to what the unit does not reteach.

**Fix.** Accept For the lead 1, amended. Frame prior-knowledge row's last cell: add "; readiness check inside the
unit's first day, scoped to Federalist 51 and Brutus No. 1 (the Declaration and the Constitution are reread in full),
with a reteach station on day 9 for students the check flags". Days.csv row 9 note: add "Reteach station: Federalist 51
and Brutus No. 1 in brief, for students the day 7 check flags."

### 5. Day 2 holds two lessons and day 3 holds none of the anchor's (minor; likely). LAYER sequence. REPEAT new

**What is wrong.** Day 2 carries T1.3 (forms of government), T1.4 (theories: republicanism, pluralism, elitism) and
D2.Civ.2 tested against participation data, plus unit 1's reteach station. Day 3 carries only the check-set addition
on ideologies, with no code.

**Fix (days.csv rows 2 and 3).** Day 2: forms of government compared (T1.3) and political ideologies and socialization
(the check-set addition). Day 3: the theories tested against evidence of who takes part (T1.4, D2.Civ.2.9-12). The
ideology addition still counts as 1 of 7. Settled by the expert (a swap inside the unit).

### 6. Day 31 compares the UN Security Council before unit 7 teaches the UN (minor; firm). LAYER sequence. REPEAT new

**What is wrong.** Day 31 sets a decision procedure "at a town council, a state legislature, Congress and the UN
Security Council" side by side; the UN is taught on day 59.

**Fix (days.csv row 31 note).** Add: "The Security Council given in a one-paragraph brief (fifteen members, five
permanent with a veto); taught in full on day 59." Day 59's note gains "Retrieval task: the Security Council procedure
from day 31."

## The calendar and the held look-back day

Day 80 holds unit 9's respond day and the look back. It is unit 9's own last day in calendar.csv (days 74 to 80), so it
shifts no unit. Check 2 on day 72 (week 15) with unit 9 in weeks 15 and 16 is allowed: week 16 is a finals week that
may hold checks, not one that must. I considered moving check 2 after unit 9 with CALENDAR tool (c) so the final sits
in the finals week; I do not recommend it, because the look back would then fall two days after the action and the
respond day would no longer confirm each team's plan before unit 9. Keep as written. If a lead later moves it,
`frame.py sync` must rerun so calendar.csv follows.

## Checked and found right (do not undo)

- Standards in full: every MA.GOV T1.1 to T5.8 code (all lettered parts of T2.8, T2.10 and T4.6) and every MA.NML code
  the frame names is on a teaching day and in its unit's end-of-unit assessment; owned C3 indicators (D2.Civ.1, 2, 4, 5,
  6, 7, 9, 11, 13 and D4.8) are on days. D2.Civ.8, 10 and 12 are practised, owned in other grades.
- Unit 9 both routes: the same seven days carry the digital and the paper route; the paper route is complete; the
  expert is optional; NML.T5.4 and T5.5 are each said to be met in part where they are, plainly to the teacher. Right.
- Every end-of-unit assessment opens with an unseen source or case. Informed action once a year (unit 9), with a
  declining route that still completes a civic action.
- Order inside units: founding documents before the gap; powers before the Commerce Clause cases; branches before the
  checks under strain; rights before press; parties before media; policy process before the team's issue.
- Check set: 5 of 7 added days used, each with its source named.
- English Language Arts grade 12 leans: its units 6 and 7 assume Government units 2 to 5 and 8 in the fall; all fall
  before the matching ELA days. Day 69's lean on ELA 12 unit 2 (argument by about day 38) holds.
- Values: no student asked about family voting, beliefs, immigration status or housing; parties given equal sources.
- No timers shown; 50-minute days; no student account or public posting.

## Lens checklist, scope and sequence layer

| Line | Met? |
|---|---|
| Unit question answerable without the unit's sources, or one defensible answer | Met: all nine are open |
| History out of time order with no reason | Met: history is used as cases, each dated |
| A contested event with one telling | Met: majority and dissent on day 28 and 29; both sides at each mock hearing |
| Writing from sources once a year or never builds short to long | Met: day 61 argument, day 69 report and editorial, day 75 position papers |

## Candidate cells

| Cell | Settled in the draft | My read |
|---|---|---|
| Political ideologies and socialization (unit 1) | Kept, 1 day, day 3 | Kept, swapped to day 2 (finding 5) |
| The Commerce Clause cases (unit 3) | Kept, 1 day, day 18 | Right |
| Congress, committees and a bill's path (unit 4) | Kept, 2 days, days 23 and 24 | Right |
| The Electoral College and state election rules (unit 6) | Kept, 1 day, day 50 | Right |
| Roosevelt's 1937 court plan (unit 4) | Kept inside T2.10a, day 30 | Right |
| Policy process stages (unit 8) | Kept inside T4.7, day 66 | Right |
| Contacting officials and public meetings (unit 9) | Kept inside T4.8, day 74 | Right; the meeting date is found on day 66 (finding 1) |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 2 and day 3 swap: forms and ideologies on day 2; theories against participation data on day 3 | Day 2 held two lessons and a reteach station | data/plans/us-government-and-politics/days.csv rows 2, 3 |
| Meeting date found on day 66; information request sent on day 68; written comment allowed on day 77 | Gives the look back on day 80 a response window | days.csv rows 66, 68, 77, 80 |
| Days 68 and 69 products scored in the day 70 assessment for NML.T5.1 to T5.3 | Production standards need a production task | days.csv row 70 |
| Reteach station for Federalist 51 and Brutus No. 1 on day 9 | Day 9 assumes the essays rather than rereading them | days.csv row 9 |
| Security Council brief on day 31, retrieved on day 59 | Used before taught | days.csv rows 31, 59 |
| Check 2 stays on day 72 | Moving it would cut the look-back window further | calendar.csv unchanged |

## For Cory

None. (Finding 2 carries out Cory's 2026-11-14 call in the frame's wording; nothing changes scope, money, people or
audience.)

## Sources

- data/standards/ma-hss-2018.txt (Massachusetts 2018, ids and our words): every code checked against the days.
- C3 Framework (NCSS 2013, rev. 2017): indicator ids from the frame and the progression rows.
- Local public-comment practice (written comment accepted by most town, county and school boards): from memory, not
  checked for any one state; the unit plan should confirm for the student's own place.

Confidence: findings 1, 3, 4 and 5 likely; 2 and 6 firm.
