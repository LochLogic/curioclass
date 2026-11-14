# Sequence read: social-studies-grade-5 (Grade 5: The United States to the Civil War, and the Fight for Civil Rights), 2026-11-14

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, the social studies part of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md (rule 2),
  frame-write.md lesson 16, docs/GLOSSARY.md.
- Cold: docs/courses/social-studies-grade-5/scope-and-sequence.md and data/plans/social-studies-grade-5/days.csv (all 160
  days).
- Beside them: docs/courses/social-studies-grade-5/frame.md, the grade 3 to 5 rows of data/progressions/social-studies.csv,
  docs/courses/CALENDAR.md, data/plans/calendar.csv (grade 5, all subjects), the ELA grade 5 frame's unit table, and
  data/standards/ma-hss-2018.txt (MA.5.T1 to T5).
- Gates: `plan.py check` passes for this course (0 failures); `frame.py calendar` places the checks in weeks 16 and 29
  with no stagger break; `stale.py check` fails only in us-history-ii/frame.md.
- For REPEAT: the non-Codex sequence reads in docs/reviews/, including my grade 3 and 4 reads of today. I did not open the
  Codex reads.

## Verdict

The strongest of the three grade 3 to 5 courses: ten units in time order with stated reasons, every lettered part of the
Massachusetts grade 5 year on a day, hard history named plainly from the people's own words, and the readiness calls right.
Two fixes before unit plans: the check days name only part of what each unit owns (as in grades 3 and 4), and unit 3 teaches
the 1770 King Street shooting before the 1765 Stamp Act Congress while saying it runs in time order. The progression notes
for four rows still say "retrieval task" where the days rightly carry readiness checks.

## Findings, most serious first

### 1. The check days name only part of what each unit owns

- **LAYER** sequence. **REPEAT** yes (grade 3 and 4 sequence reads, finding 1). **Confidence** firm (on the codes column);
  likely (on the harm).
- **What is wrong.** Owned codes and lettered parts absent from their unit's check day, most on no check in the year:
  - Unit 2 (day 25): MA.5.T1.7a to d (only the parent is named).
  - Unit 3 (day 42): MA.5.T2.1a to d, MA.5.T2.2, MA.5.T2.3.
  - Unit 4 (day 58): MA.5.T2.5a to c, MA.5.T2.6, MA.5.T2.7, MA.5.T2.9.
  - Unit 5 (day 74): MA.5.T3.3, MA.5.T3.5, D2.Civ.1, D2.Civ.3.
  - Unit 6 (day 95): MA.5.T4.3a, MA.5.T4.3b, D2.Eco.6, D2.Eco.13, D2.Geo.11.
  - Unit 7 (day 111): MA.5.T4.5a to d, D2.His.5, D2.His.6, D2.Civ.14.
  - Unit 8 (day 125): MA.5.T5.5, D2.His.17.
  - Unit 10 (day 159): D1.1 to D1.5, D4.4, D4.7, D4.8.
- **Why it matters.** A busy unit-plan writer builds the check from the codes named. As written, the British Acts and the
  women of the boycotts (T2.1a, d), Shays' Rebellion, the Battle of New Orleans, the Trail of Tears and the Mashpee Revolt
  could be taught and never assessed, against the bar's assessment items (C4, C8).
- **Fix.** On each unit's end check day, list every owned code and lettered part from the frame's Units table: add the
  codes above to days 25, 42, 58, 74, 95, 111, 125 and 159. For unit 10's inquiry and action codes, keep them on day 159 and
  add to the note "D1 and D4 codes judged from the research log, claim and action with the unit rubric".

### 2. Unit 3 puts the King Street shooting before the Stamp Act Congress

- **LAYER** sequence. **REPEAT** yes (time order broken inside a unit, as in the grade 3 sequence read, finding 2).
  **Confidence** firm.
- **What is wrong.** Days 33 to 34 weigh two accounts of the 1770 King Street shooting; day 35 then teaches the Stamp Act
  Congress and the Sons of Liberty, both 1765. The scope and sequence says "the chain runs in time order" and the two-source
  skill sits "where the timeline reaches 1770", but the timeline has not reached 1770 if 1765 comes after.
- **Why it matters.** The unit's chain from war debt to fighting is the end-of-unit task (day 42). Students who meet the
  colonial response to the Stamp Act after the shooting lose the cause-and-effect order the unit is built to teach, and the
  day 29 cause-and-effect organizer (the bridge for ELA RI.5.3) is filled in the wrong order.
- **Fix (settled here, a swap inside the unit, no day cost).** Day 32: the Stamp Act Congress and the Sons of Liberty (was
  35). Day 33: source each document unprompted (was 32). Day 34: two accounts of the King Street shooting (was 33, with its
  RI.5.6 bridge note). Day 35: weigh the two accounts and write a claim (was 34). Day 36 onward unchanged. In the scope and
  sequence, rewrite the unit 3 paragraph: "the Acts, taxation and representation and the first colonial responses (28 to
  32); the two-source skill where the timeline reaches 1770 (33 to 35); then the Tea Party, the Suffolk Resolves and the
  fighting (36 to 37)".

### 3. The progression still says "retrieval task" where the days carry readiness checks

- **LAYER** progression, frame. **REPEAT** yes (the grade 6 and 7 sequence reads met the same question). **Confidence**
  firm.
- **What is wrong.** Days 15, 44, 60 and 147 are readiness checks on grade 3's ss3-sea-trade, ss3-money-saving,
  ss3-rules-rights and ss3-deliberation, none of which grade 4 uses. The frame's seams (For the lead item 2) and the
  progression notes say each opens "with a short retrieval task": ss5-slavery-colonies (from ss3-sea-trade),
  ss5-independence-war (from ss3-money-saving), ss5-constitution (from ss3-rules-rights) and ss5-informed-action (from
  ss3-deliberation).
- **The right call for this course: readiness checks, as the days have them.** A row last used two grades back, by a
  third grader, needs a check that tells the teacher who has it. Each check sits so the reteach falls before the day that
  needs it (day 54 for prices, day 156 for the decision). Retrieval tasks stay for grade 4 rows and the grade 3 rows grade
  4 kept in use (founding ideas, levels of government), as written.
- **Fix.** Apply For the lead items 1 and 2 as written. In data/progressions/social-studies.csv, in the notes of the four
  rows named, change "opens with a short retrieval task" for the grade 3 row named to "opens with a readiness check on the
  unit's first day (the row sat idle across grade 4)". The grade 3 read's process note on rule 2's wording ("last used two
  or more grades back") covers the rule itself.

## Checked and found right (do not undo)

- Units, day counts and dates match the frame and data/plans/calendar.csv; no look-back day shifts a unit. Day 73 (review
  for course-level check 1) is held inside unit 5's sixteen days, which is the right call: it costs no unit day elsewhere
  and readies the check.
- Every lettered part of MA.5.T1 to T5 is carried by a teaching day. MA.5.T5.6a and 6b sit in unit 9 as the frame sets.
- No unit is over 25 days, so no mid-unit assessment is needed. Each unit has one respond day; the two course-level checks
  have two each, matching calendar.csv. Response time is counted once.
- Course-level checks sit on CALENDAR.md's target weeks 16 and 29, clear of the grade's math, science and ELA weeks.
- Leans: ELA RI.5.3 bridged on day 29, RI.5.6 on day 33 (day 34 after finding 2), W.5.1 on day 72, RI.5.8 on day 108; W.5.7
  and W.5.1 are met before unit 10; math 5.G.A.1 and science 5-ESS3-1 are handled on days 84 to 86 and 92.
- Unit 1 opens on relations (days 2 to 6) before why colonies were founded, out of strict time order, with a stated reason
  (the relations answer the unit question). Leave it.
- Unit 2 ends on freedom sought and won; unit 7 shows Cherokee self-government (day 99) before the Removal Act; unit 9
  teaches the African American movement before the movements modelled on it. All reasoned and right.
- No counterclaim asked anywhere (C3 places it in grades 6 to 8). Values rule a on days 101 and 139, rule b on day 115.
- Candidate cells: all settled; the dropped unit 5 candidate (a later amendment) has its reason.
- Only one Fluency day in the year (day 73). Grade 5 units close on a claim and an assessment from sources, which does the
  review's work; leave it.

## Lens checklist, scope and sequence layer

| Lens line | Status |
|---|---|
| History in time order unless a reason is given | Missed in unit 3 (finding 2); unit 1 reasoned; met elsewhere |
| More than one account of contested events | Met (days 4, 5, 33 to 34, 104, 114 to 116) |
| Values rule a to d | Met (days 101, 115, 139) |
| No role play or simulation of hard history | Met (days 19, 37, 47, 102, 106, 107 notes) |
| Native nations in the present, from their own pages | Met (days 6, 102, 103) |
| Informed action once, chosen by students | Met (days 155 to 158) |
| Inquiry arc to a claim from sources each unit | Met |
| Personal finance light touch | Met (day 54) |

## Settled by the expert

| Item | Settled as |
|---|---|
| Check day codes | Every owned code and lettered part named on its unit's check day |
| Unit 3 order | Stamp Act Congress day 32; sourcing 33; King Street 34; weigh and claim 35 |
| Readiness versus retrieval | Readiness on days 15, 44, 60, 147, as written; progression notes follow the days |
| Held look-back days | None shift a unit; day 73 stays inside unit 5 |
| Unit 1 order | Leave, reasoned |
| For the lead items 1 and 2 | Apply as written |

## For Cory

None.

## What I could not judge

- Facts on individual days (the 1660s law dates, postwar deflation figures); the day writers are already told to check them.
- Whether unit 9's eleven teaching days carry its four movements at depth; the counts are close to the load and the unit
  plan will show it.

## Sources

- S:\CurioClass\docs\courses\social-studies-grade-5\scope-and-sequence.md; data\plans\social-studies-grade-5\days.csv;
  docs\courses\social-studies-grade-5\frame.md; data\progressions\social-studies.csv; docs\courses\CALENDAR.md;
  data\plans\calendar.csv; data\standards\ma-hss-2018.txt; docs\courses\english-language-arts-grade-5\frame.md.
- docs\pipeline\briefs\sequence-read.md, sequence-write.md; docs\agents\EXPERT.md; docs\agents\lenses\social-studies.md;
  docs\ADOPTION-BAR-SUBJECTS.md; docs\courses\social-studies\STANDARD.md.
