# Sequence read: social-studies-grade-4 (Grade 4), 2026-11-14

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, the social studies part of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md (rule 2),
  frame-write.md lesson 16, docs/GLOSSARY.md.
- Cold: docs/courses/social-studies-grade-4/scope-and-sequence.md and data/plans/social-studies-grade-4/days.csv (all 160
  days).
- Beside them: docs/courses/social-studies-grade-4/frame.md, the grade 3 and 4 rows of data/progressions/social-studies.csv,
  docs/courses/CALENDAR.md, data/plans/calendar.csv (grade 4, all subjects), the ELA grade 4 frame's unit table and
  cross-subject lines, and data/standards/ma-hss-2018.txt.
- Gates: `plan.py check` passes for this course (0 failures); `frame.py calendar` places the checks in weeks 8, 21 and 27
  with no stagger break; `stale.py check` fails only in us-history-ii/frame.md.
- For REPEAT: the non-Codex sequence reads in docs/reviews/, including my grade 3 read of today. I did not open the Codex
  reads.

## Verdict

A well-built year: units, days and checks match the frame and calendar.csv, every lettered part is on a day, the leans are
met or bridged, and using retrieval tasks only is the right call because every assumed row is a grade 3 row used the year
before. As in grade 3, the check days name only part of what each unit owns, which would leave the whole Canada and Mexico
standard and most of the regions' lettered parts unassessed; that needs fixing before unit plans. Day 142 holds too much,
and one order question in unit 5 is worth a swap.

## Findings, most serious first

### 1. The check days name only part of what each unit owns

- **LAYER** sequence. **REPEAT** yes (grade 3 sequence read, finding 1). **Confidence** firm (on the codes column); likely
  (on the harm).
- **What is wrong.** Owned codes absent from their unit's check day, most on no check in the year:
  - Unit 2 (day 37): MA.4.T1.3 (Canada and Mexico, the whole content standard), D1.5, D2.Eco.14, D4.5.
  - Unit 3 (day 58): MA.4.T2.3.
  - Unit 4 (day 78): MA.4.T3.2, MA.4.T3.3 (D2.His.9 is on course-level check 1, which is enough).
  - Unit 5 (day 102): MA.4.T4.1, MA.4.T4.3, MA.4.T4.4, MA.4.T4d.2, MA.4.T4e.2.
  - Unit 6 (days 120, 131): MA.4.T4a.2, MA.4.T4b.1, MA.4.T4b.5, MA.4.T4c.1, MA.4.T4c.4, MA.4.T4d.1, MA.4.T4d.5,
    MA.4.T4e.1, MA.4.T4e.5.
  - Unit 7 (day 159): MA.4.T4a.5, MA.4.T4b.2, MA.4.T4b.3, MA.4.T4c.2, MA.4.T4c.3, MA.4.T4d.3, MA.4.T4d.4, MA.4.T4e.3,
    MA.4.T4e.4, D2.Geo.9, D4.6.
- **Why it matters.** A busy unit-plan writer builds the check from the codes named. As written, Canada and Mexico, the
  movement west, immigration by choice and force, and four of the five regions' parts would be taught and never checked,
  against the bar's assessment items (C4, C8).
- **Fix.** On each unit's end check day (and day 120 for the part of unit 6 before it), list every owned code and lettered
  part from the frame's Units table: add the codes above to days 37, 58, 78, 102, 120 or 131 (states and maps parts to
  day 120, adaptation and resource parts to day 131) and 159. For product-judged codes (D4.5, D4.6 in the proposal), add
  to the note "judged from the unit's product with the unit rubric". The goal line of day 37 should name a Canada or
  Mexico task.

### 2. Day 142 carries four topics, two of them heavy

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Day 142 holds the Gold Rush, Chinese Americans, the Chinese Exclusion Act of 1882 and the wartime
  incarceration of Japanese Americans in one 40-minute lesson. Every other region gets one people-day with one story.
- **Why it matters.** Two exclusions by law, one of them the imprisonment of citizens, cannot be told plainly and with the
  people's own words in a quarter of a lesson each; the sensitivity read will find them rushed, and a rushed hard history
  is the fault the lens warns against.
- **Fix (settled here, no change to the unit's days).** Split day 142: day 142, the Gold Rush, Chinese Americans and the
  Exclusion Act of 1882; day 143, Japanese Americans in the West and wartime incarceration, from the people's own accounts
  (sensitivity read). Days 143 to 157 move to 144 to 158. Drop the review day 158 (Fluency) and open day 159's assessment
  with a short review. Update the scope and sequence's unit 7 paragraph (peoples 138 to 144, compared 145, hazards 146 to
  148 and so on; action 155 to 157).

### 3. The retrieval-only call is right; the bar's readiness wording does not fit it

- **LAYER** process. **REPEAT** yes (grade 6 and 7 sequence reads, the same question). **Confidence** firm (on the call);
  a judgment call (on the bar).
- **What is wrong.** The frame's Days bullet says a unit assuming a grade 3 row "opens with a readiness check"; the days
  carry retrieval tasks only (For the lead item 1 says so). Every assumed row is a grade 3 row, used the year before, so
  rule 2 gives retrieval. But the bar's C4 evidence names "the readiness check on each unit plan", and C8 asks for checks
  before teaching; a course with no readiness check reads as missing them.
- **The right call for this course: retrieval, as the days have it.** Apply For the lead item 1 as written.
- **Fix.** For the lead: either reword the bar's C4 evidence to "the readiness check or opening retrieval task on each unit
  plan", or have the unit-plan brief say the opening retrieval task is read by the teacher as an unmarked look at who
  needs help (it stays unmarked, as the glossary requires).

### 4. Unit 5 ends on the division over slavery after 1898

- **LAYER** sequence. **REPEAT** new. **Confidence** a judgment call.
- **What is wrong.** The war with Mexico ends on day 91 (1848); Alaska, Hawaii and Puerto Rico follow (92 to 94, 1867 to
  1898); then choice, force and "by the mid 1800s the country was divided over slavery's spread west" (96 to 98). The
  writer gives a reason (end on the division, which grade 5 picks up), but the land won from Mexico is what raised the
  question of slavery's spread, and the timeline runs backwards by fifty years at the end.
- **Fix (settled here, a swap inside the unit).** Days 92 to 94: many groups came by choice; people from Africa brought by
  force; the division over slavery's spread (were 96 to 98). Days 95 to 97: Alaska, Hawaii, Puerto Rico (were 92 to 94).
  Day 98: complete the growth map and timeline (was 95). The scope and sequence's unit 5 paragraph is rewritten to match;
  the grade 5 handoff is unchanged.

### 5. Day 83's canal set note

- **LAYER** sequence. **REPEAT** yes (stale or loose notes, as in the economics sequence read). **Confidence** likely.
- **What is wrong.** Day 83 uses ELA grade 4 unit 3's Erie Canal set "(its days 81 to 119, running now)". Day 83 is two
  days into that unit, so social studies may well reach the set first.
- **Fix.** Day 83 note: add "social studies may open the set before ELA does; read the one canal text, no second text".
- Outside this course: the ELA grade 4 frame's cross-subject SL.4.4 line says "here in unit 4, later", while its own unit
  table places SL.4.4 in unit 1. Social studies day 27's "SL.4.4 runs now" follows the unit table and is right; the ELA
  line is the stale one, for the lead.

## Checked and found right (do not undo)

- Units, day counts and dates match the frame and data/plans/calendar.csv; no look-back day is held, so no unit shifts.
- Every lettered part of MA.4.T4a to T4e is carried by a teaching day.
- Unit 6 (26 days) has its mid-unit assessment on day 120; no other unit is over 25 days. Response time is counted once.
- Course-level checks sit on CALENDAR.md's target weeks 8, 21 and 27, clear of the grade's math, science and ELA weeks.
- Leans: W.4.7 bridged on day 23, RI.4.6 on day 62, 4.MD.A.2 on days 5 to 6, science 4-ESS1-1 on day 43; math 4.NBT.B.4,
  science 4-ESS3-1 and 4-ESS3-2 come before their days.
- Unit 6 order (states placed before the maps, the Northeast as the worked case first) and unit 7's action placed after the
  traced policy, both with reasons.
- The war with Mexico from Mexican, Tejano, Californio, Native and US sides, with two accounts weighed (days 89 to 90).
- For the lead item 2 (science row days) is right; apply as written.
- Candidate cells are all settled on named days with no added day.

## Lens checklist, scope and sequence layer

| Lens line | Status |
|---|---|
| History in time order unless a reason is given | Met; unit 5's end is reasoned but worth the swap (finding 4) |
| More than one account of contested events | Met (days 89 to 90, the regions' peoples) |
| Values rule a to d | Met (day 90 under rule b) |
| No role play or simulation of hard history | Met |
| Native nations in the present, from their own pages | Met (days 82, 92 to 94, 138, 141) |
| Informed action once, chosen by students | Met (days 154 to 156) |
| Inquiry arc to a claim from sources each unit | Met |
| No family immigration or status questions | Met (day 143 note) |

## Settled by the expert

| Item | Settled as |
|---|---|
| Check day codes | Every owned code and lettered part named on its unit's check day |
| Day 142 | Split into two days; drop the review day 158 |
| Unit 5 end order | Choice, force and the division on 92 to 94; Alaska, Hawaii, Puerto Rico on 95 to 97; map 98 |
| Readiness versus retrieval | Retrieval only, as the days have it |
| Held look-back days | None held; no unit shifts |
| Day 83 note | Social studies may open the canal set first |
| For the lead items 1 and 2 | Apply as written |

## For Cory

None.

## What I could not judge

- Whether one day per region (unit 7) is enough for a school whose own region needs more; day 143 (the local thread)
  covers it in the general form.
- Facts on individual days (the Hawaiian petitions, the Exclusion Act's terms); the day writer checks them.

## Sources

- S:\CurioClass\docs\courses\social-studies-grade-4\scope-and-sequence.md; data\plans\social-studies-grade-4\days.csv;
  docs\courses\social-studies-grade-4\frame.md; data\progressions\social-studies.csv; docs\courses\CALENDAR.md;
  data\plans\calendar.csv; data\standards\ma-hss-2018.txt; docs\courses\english-language-arts-grade-4\frame.md.
- docs\pipeline\briefs\sequence-read.md, sequence-write.md; docs\agents\EXPERT.md; docs\agents\lenses\social-studies.md;
  docs\ADOPTION-BAR-SUBJECTS.md; docs\courses\social-studies\STANDARD.md.
