# Expert read: scope and sequence, Computer Science Grade 11 (2026-11-26)

Cold read of a scope and sequence written by a fresh Claude agent. Brief: docs/pipeline/briefs/sequence-read.md with
build/scope-writes/CS-READ.md.

## What I read

- docs/courses/computer-science-grade-11/scope-and-sequence.md and data/plans/computer-science-grade-11/days.csv (64 rows).
- docs/courses/computer-science-grade-11/frame.md; the grade 11 rows of data/progressions/computer-science.csv;
  data/plans/calendar.csv (US history I, grade 11); build/scope-writes/CS-BRIEF.md; docs/pipeline/briefs/sequence-write.md;
  docs/agents/EXPERT.md; docs/agents/lenses/computer-science.md; AGENTS.md. The grade 7 and grade 8 frames, only for the
  data sovereignty and data center cases this course recalls.
- Gates: `sequence.py check computer-science-grade-11` 0 failures. `frame.py check` 2 failures, both in the frame (the
  Cross-subject section does not name the us1-progressivism lean; frame.md line 332 has "until it is loaded" outside a
  Pending marker). `frame.py calendar` covers K to 8 only. `stale.py check` reports only the same frame line 332.
- Outside sources, by web search on 2026-11-26 (search results only, no page opened): reporting that the EEOC removed its
  AI technical assistance from eeoc.gov on 2025-01-27 (Cooley, 2025-02-21; National Law Review, 2026); reporting on The
  Dalles, Oregon data center water use (Oregonian figure via WaterWatch and DatacenterDynamics, 2022; OPB, 2026-01-15
  and 2026-01-23).

## Verdict

The scope and sequence is sound: units, days and owned ids match the frame exactly, trace comes before modify before
make on every programming row, every device day carries all four paths with a paper version, the readiness checks
sit on the right days, and the calendar and the us1-progressivism lean both check out. The biggest risk is unit 5's
hiring case. One of its two sources was withdrawn by its agency in January 2025, and the two sources together give
one view, not the two views the row asks for. The change that matters most is to date the EEOC document as withdrawn
and add a real second view. The other findings are small note and prompt fixes, with no day added.

## Findings, most serious first

**1. Unit 5's hiring case: one view, and a withdrawn source (day 50).** LAYER sequence (and frame, Sensitivity reads).
REPEAT new.
What is wrong: day 50 builds the hiring audit "from two dated sources with two views": the EEOC's 2023 technical
assistance and NIST SP 1270. Both say the same thing: algorithmic selection can carry bias and should be checked. That
is one view. The EEOC also removed that document, along with its 2022 ADA document, from eeoc.gov on 2025-01-27 (search
results, Cooley 2025-02-21 and National Law Review 2026; likely, not opened). Technical assistance created no duty of its
own, and the Title VII duty it explained still applies.
Why it matters: the bar and the row (g11-algorithm-ethics: "two views and a dated source for each") fail a society case
that has one view. A teacher who presents the document as current federal guidance teaches something false.
Fix: in day 50's note and the unit 5 prose, describe the EEOC source as "issued May 2023, removed from eeoc.gov January
2025; the Title VII duty it explained still stands". That removal is itself a good dated fact for the audit. Add a
second view from a dated, non-company source arguing that structured or algorithmic screening can make decisions more
consistent than unstructured human judgment, for example a government or university source the unit writer opens.
Keep NIST SP 1270 (still current, March 2022). The frame's Sensitivity reads pack and For the lead 5 list the EEOC
document too, so the lead should add the same dating there. Confidence: likely.

**2. End marks on teaching days 28 and 61 are no longer needed.** LAYER sequence, process. REPEAT new.
What is wrong: days 28 and 61 carry `assess` = `end` as "part 1" of an end-of-unit assessment only so the gate would
pass. Since the lead fix of 2026-11-26, sequence.py accepts the course-level check on days 33 and 62, the day right
after each unit's last day, as that unit's end-of-unit assessment.
Why it matters: an `end` mark on a revision lesson tells the unit planner to write a sitting there, and it breaks the
frame's "no score comes from a lesson that first teaches a row" reading for day 28's half of S1-DSC-VZ-11.
Fix: blank `assess` on days 28 and 61. Keep the note's hand-in line ("the revised chart / design document is handed in
today and scored once after the course-level check") and drop "End-of-unit assessment, part 1". In the .md, remove
unit 3's "Day 28 carries `assess` = end ..." sentence and the "(The gate asks ...)" clause, do the same for unit 6, and
delete For the lead 1. Confidence: firm.

**3. Several end and check tasks miss a part of a code (days 21, 53, 62).** LAYER sequence. REPEAT yes.
What is wrong:
- Day 21 lists S1-SWD-TR-07, but nothing in it judges generated test suggestions, which is a taught part (row note; day
  13). Its HS-PRO-RD-18 prompts also name flaw, reliability and ownership but not fit to the requirement.
- Day 53 has no prompt on what the audit could not see, which is a part of g11-algorithm-ethics taught on day 49.
- Day 62's HS-SOC-HI-39 item asks for "one change with its reason and who it affects" but not how the change encourages
  innovation and cuts risk, which is the standard's core.
Why it matters: rule 2 requires a prompt per part on every end and check task, so a student can be scored "met" on a
code without showing its central part.
Fix (no minutes added; each is a short prompt inside the sitting):
- Day 21 note: add "two supplied generated test suggestions: keep, change or drop, with the reason" and "fit to the
  requirement".
- Day 53 note: add "one thing the audit could not see".
- Day 62 note and the .md: "propose one change, say how it encourages innovation and cuts a named risk, with one piece
  of evidence and who it affects".
Confidence: firm.

**4. Two views and a dated source are not named on days 58, 59 and 60.** LAYER sequence. REPEAT new.
What is wrong: g11-policy-change asks for two views and a dated source for the existing policy, and g11-emerging-solution
asks for two views and a dated source for the main claim. Day 57 dates the law, but day 58 (the proposal) and days 59
and 60 (the design document) say nothing about two views or a dated source.
Why it matters: these rows are the year's last society evidence, and the lens's "society content with one view only"
error would pass unseen into the unit plan.
Fix: day 58 note: "the proposal weighs two views (one who would gain, one who would bear the cost) and cites the law
with its date". Day 59 note: "research names a dated source for the main claim about the technology". Day 60 note:
"benefits and harms from two views". Confidence: firm.

**5. Safety lines are missing from most security days (days 1 to 3, 6 to 8, 34).** LAYER sequence. REPEAT yes.
What is wrong: the frame says "The scope and sequence copies these lines into each security and device day". Only days
4 and 5 carry the full lines. Day 3 has "no attack steps", and days 1, 2, 6, 7, 8 and day 34's flaw item carry none.
Why it matters: the security days are where a student is most likely to try something on a real system. The
sensitivity read checks for these lines day by day.
Fix: add to each of those days' notes the short form: "Safety: the toy system or described case only; no scanning, no
attack steps, no test of a real school or home system; a student who knows of a real flaw tells the teacher privately
and never tries it." Confidence: firm.

**6. Day 56 states an unchecked water figure as fact.** LAYER sequence. REPEAT new.
What is wrong: day 56's note says "a city whose data centers draw about a third of its water". The .md admits no page
was opened. Search results (2026-11-26, not opened) agree on about 29 percent in 2021, from city records released after
the 2022 settlement of the city's suit against a newspaper. They put the share nearer a third in later reporting (OPB,
2026-01-15), which the city's mayor publicly disputed (OPB, 2026-01-23). The city's 2026 plan to draw more water from
national forest land is a current development with two views already on record.
Why it matters: the case must be accurate and current, and the dispute is the two views the row needs.
Fix: day 56's note should read "about 29 percent of city water in 2021 (city records released after a 2022
settlement); later reporting puts it near a third and the city disputes parts of that reporting; figures checked by
search 2026-11-26, to be opened by the unit writer". Keep "told without the company". The unit writer opens the city's
pages and one news report, and records the results in APPROACH-SOURCES. Confidence: likely.

**7. Day 16 uses "the values the class set" before any day sets them.** LAYER sequence. REPEAT new.
What is wrong: day 16 judges the program against "the values the class set (privacy, access)", but no earlier day of
unit 2 has the class set them.
Why it matters: this uses something before it is taught. The planner would have to squeeze the value-setting into a
judging day.
Fix: day 10's note should say "the class sets two values on the specification sheet (the overdue list shows titles,
never borrowers' names; plain messages and keyboard use), about five minutes". Day 16 then applies them. Settled below.
Confidence: firm.

**8. Shorter path: folding day 56 leaves no student-written chain before the check.** LAYER sequence. REPEAT new.
What is wrong: in the shorter year, day 56 folds into day 55 "as the chain's worked example". Day 55 is a class-built
diagram, so in the shorter year no student writes their own "who is affected and why" before day 62 scores it.
Why it matters: HS-SYS-IM-37's "why" part loses its only practice.
Fix: in the Shorter path table, the "What is kept" cell for day 56 should read "The case is the chain's worked example,
and day 55's exit ticket is each student's own written link: one group affected and why". Confidence: likely.

**9. Day 54's readiness check is overloaded for students who did not take grade 10.** LAYER sequence (frame-set). REPEAT
new.
What is wrong: in ten minutes, day 54 asks for two grade 8 items for every student plus five grade 10 rows for
non-takers: seven items.
Why it matters: about 80 seconds an item yields noise, not a reading that can shape day 55.
Fix: one page of six one-minute items: kiosk users (g8-design-for-all); one data center claim (grade 8 debate); one
upload traced (g10-network-diagram); one policy placed on a timeline (g10-history-policy); one emerging technology's
benefit and harm with whose choice it was (g10-emerging-impacts and g10-human-choices together); one role matched to a
skill (g10-career-skills). Settled below. Confidence: judgment call.

**10. Unit 4's device days do not name pair roles (days 40 to 43).** LAYER sequence. REPEAT new.
What is wrong: the frame places IC5 (pair roles that switch at the halfway signal) in unit 4, but days 40 to 43 do not
mention it. Unit 2 (day 14) and unit 1 (day 5) do.
Why it matters: the lens flags "pair work with no roles, or one student at the keyboard all period".
Fix: add "driver and navigator switch at the halfway signal (IC5)" to the notes of days 40 to 43. Confidence: firm.

**11. Day 40 reads like a make day before the make.** LAYER sequence. REPEAT new.
What is wrong: day 40 "trains the model" as Application. That fits as the guided first run on a supplied set, with day
42 as the modify and day 43 as the pair's own make. The goal does not show that.
Fix: day 40's goal should open "Predict which 7s the model will miss, then train it on the supplied training pile by
the pseudocode lines". Keep the kind (it is a guided build, not a trace). Confidence: judgment call.

**For the lead (frame, not this file):** the two `frame.py check` failures (name the us1-progressivism lean in
Cross-subject; put frame.md line 332's "until it is loaded" inside a Pending marker), and the EEOC dating in the frame's
Sensitivity reads and For the lead 5 (finding 1).

## Checked and sound (do not undo)

- **Order inside units.** Unit 1 runs trace (day 4) then modify then make (day 5) then transfer (6) then revise (7).
  Unit 2 runs specification, case kinds, unit and integration traced, modify (13), make (14), run and debug from the
  first failure (15), then generated code traced (17) before it is tested. Unit 3 runs modify (25), make (26),
  conventions (27), revise (28). Unit 4 has the data review before the build, the rebalance after the first
  comparison, and the final pile sealed until day 44. Each arc reaches its compelling question.
- **Readiness and retrieval.** These are on days 1 (after the hook), 9, 22, 35, 47 and 54, never on a unit's first day
  after unit 1. g9-data-and-people (grade 9) and g8-design-for-all (grade 8) get readiness for every student, by grade
  count. Grade 10 rows open as retrieval with a worked example on the first-use day. Every first-use day in the
  Seams table carries its retrieval. The grade 7 sovereignty case goes to every student as a card. It is four grades
  back and grade 7 may swap that case set, so the writer's call is right.
- **Ids.** All 12 Foundational and 4 Specialty I ids sit on days in their frame units. No id is claimed outside the
  frame. The contributes ids (~HS-ALG-PS-03, ~HS-PRO-PD-14, ~HS-SOC-HU-44, ~HS-SOC-CE-45) are marked as used.
- **Days outside the standards.** 4.5 of 50 days, on the frame's named halves and wholes.
- **school_day.** The formula is stated once and every day matches it. Unit 1 falls in weeks 1 to 5, unit 2 in 5 to 11,
  unit 3 in 12 to 16, the mid-year check in week 17 (respond day in week 18), unit 4 in 18 to 24, unit 5 in 24 to 27,
  unit 6 in 28 to 31, and the year-end check in weeks 31 and 32.
- **Lean.** US history I unit 8, The Progressive Era, runs weeks 25 to 28 (calendar.csv). Day 57 is in week 29, so no
  bridge is owed.
- **Device and paper.** Every device day names the four paths and its paper version. HS-ALG-ML-08 and HS-DAT-DI-25 are
  marked part met without a device. No live generated-text tool is used.
- **Course-level checks.** Day 34 samples units 1 and 2 in new forms, 6 and 11 weeks after the end days (rule 2's
  two-week window met). Day 63 samples units 4 and 5. S1-AIN-DD-02 is named with its reason under rule 3. Day 46
  scores it in full, and the writer's optional frame fix would take minutes from HS-ALG-ML-08's claim item, so the
  frame should stay as is (settled below).
- **Washington 70A.500 RCW** (2006 c 183) was checked at source by the writer.

## Lens checklist (scope and sequence layer)

| Lens line | Status |
|---|---|
| All five concept areas taught | Met (systems and security, programming, data, algorithms and design with ML, society) |
| AI inside concepts, not one late unit | Met (unit 4 on unit 3's data work, unit 5 audits it) |
| Read, then modify, then make | Met on every programming row; day 40 wording, finding 11 |
| Unplugged path in every unit | Met |
| Debugging taught as a method | Met (day 15, first failure traced; mixed practice by error letter) |
| Pair roles that switch | Part met: unit 4 missing, finding 10 |
| Society with dated cases and two views | Missed on days 50, 58 to 60, findings 1 and 4 |
| Id below or past its boundary, or claimed by mention | Met (the frame's Out lines are kept) |
| Specialty only where the unit already goes that far; no S2 | Met |
| No claim that coding improves general thinking | Met (none found) |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 10 sets the two class values on the specification sheet (about 5 minutes) | Day 16 uses them | data/plans/computer-science-grade-11/days.csv |
| Day 54 readiness: six one-minute items, g10-emerging-impacts and g10-human-choices in one item | Seven items do not fit ten minutes | days.csv (day 54 note) |
| Days 28 and 61: blank `assess`, keep the hand-in line | The gate now accepts the following C check | days.csv; scope-and-sequence.md |
| S1-AIN-DD-02 stays off the course-level checks, named with its reason | Scored in full on day 46; adding it would cut HS-ALG-ML-08's item | scope-and-sequence.md (no change) |
| Day 56 water figure: 29 percent in 2021 from city records, later share disputed | The figure tied to records; the dispute is the second view | days.csv (day 56 note) |
| Day 40 goal opens with a predict step | Shows the guided first run before day 43's make | days.csv (day 40 goal) |

## For Cory

Nothing. Every finding is an item-level fix inside the frame.

## For the source list

- The EEOC's 2023 Title VII technical assistance on software and algorithms: removed from eeoc.gov 2025-01-27 (search,
  Cooley 2025-02-21, cooley.com; National Law Review 2026, natlawreview.com). Not opened.
- The Dalles water use: WaterWatch of Oregon (waterwatch.org) and OPB (opb.org, 2026-01-15 and 2026-01-23). Search
  results only, not opened.
