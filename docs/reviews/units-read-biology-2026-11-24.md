# Units read: biology, 2026-11-24

COURSE-RUN stage 4. All ten unit plans were read together as one course.

## What was read

- AGENTS.md; docs/COURSE-RUN.md stage 4; docs/agents/EXPERT.md; docs/agents/lenses/science.md; docs/courses/UNIT-PLAN.md; docs/GLOSSARY.md.
- docs/courses/biology: frame.md, scope-and-sequence.md, s01.md to s10.md in full (skel blocks and day lists set aside).
- data/plans/biology/days.csv (kind counts, notes for course days 44 to 46, 76 to 78, 156 to 160 and other noted days); the bio-* rows of data/progressions/science.csv.
- Continuity: grade 8 unit 6 (days 132 to 158) and Chemistry s01.

## Verdict

The course holds together. The arc runs from body systems to a final fishery design unit, each unit's model is carried into the next one, the computational model is introduced in unit 5 and comes back in unit 10, and the handoffs in from grade 8 and out to Chemistry line up. The one serious fault was the day 123 readiness check, which existed in two different versions. The rest were exit shapes in the goal maps that had drifted from the written exit tickets, leftover self-marking text in unit 4, and returns missing from units 3 and 9. All of these are fixed. No day files exist yet, so there are no day faults.

## Findings

| # | Severity | Unit | Finding | Verdict |
|---|---|---|---|---|
| F1 | Serious | s08, s09 | The day 123 readiness check had two different versions. s08 gave a buffer versus concrete edge and a paving runoff design; s09 field 4 gave pond designs and a planted-strip test plan. Every other boundary follows one rule: the next unit's field 4 is the authority and the earlier plan points to it. | Fixed: s08's paragraph is now a pointer to s09 field 4 (gaps go to day 124). |
| F2 | Moderate | s01 to s07, s09, s10 | Nine plans link to docs/courses/biology/TOOL-ASKS.md, which does not exist. | For the structure pass. |
| F3a | Minor | s02 day 21 | The goal map exit said "new seedling case", but the exit ticket is an animal tissue with a constant cell count (the seedling is the practice). | Fixed: row exit shape. |
| F3b | Minor | s05 day 58 | The verb is "notice and propose", but the exit was recognise ("picks a likely reason") while the ticket asks students to propose. | Fixed: produce, "Proposes one reason for the key change". |
| F3c | Minor | s06 day 81 | The exit ticket asks students to write a question and name evidence, but the map said recognise ("picks"). | Fixed: produce, matching the ticket. |
| F3d | Minor | s07 day 98 | The exit shape (a well-supported case) did not match the ticket, which is a conflicting-evidence case. | Fixed: row exit shape. |
| F3e | Minor | s07 day 101 | The exit shape said lake fish; the ticket uses seedlings in shade, and the lake fish are the practice. | Fixed: row exit shape. |
| F3f | Minor | s10 day 152 | The verb "identify" is recognise and the map says sort, but the ticket asked for a formal written recommendation, which repeats the day's writing practice. | Fixed: the ticket is now a three-claim sort with a key (B). |
| F4 | Minor | s04 field 7 | Leftover self-marking text ("students mark against the key", "hands up confirms") contradicted the field's own plan, in which every item is teacher-judged and scored before class on day 57. | Fixed: one sentence remains, saying that error letters set the groups. |
| F5a | Minor | s03 returns | The returns left out course check day 45 (HS-LS1-5, HS-LS1-7) and Chemistry unit 1 day 1, which retrieves conserved atoms and food molecules. | Fixed: both added. |
| F5b | Minor | s09 returns | The returns left out course check day 157 (HS-ETS1-1, HS-ETS1-3) and its response on day 160. | Fixed: added. |
| F6 | Low | days 102, 126 | The sequence gate notes that two Fluency days carry the first course use of HS-LS4-3 and HS-ETS1-3. Both read as practice of skills taught in grade 8 or Algebra I. | No change; listed for the structure pass as a judgment call. |
| F7 | Low | s02 day 24 | The scored leaf-repair packet follows the same seedling story (repair, transport, a matched DNA segment) as the drafts on days 21 to 23. This risks rule 4 on story reuse. | No change: the numbers and the organ are new and the packet is the unit's scored synthesis. Check again when the day 24 file is written. |

Checks that passed:
- Arithmetic in the items for units 4, 5, 6, 7 and 10, and the unit 9 timings.
- The plan headers match the kind counts in days.csv (149 unit days plus course days).
- The readiness rows match the scope register, and the copies on days 25, 112 and 140 are the same in both units.
- The handoffs in from grade 8 (common ancestry and coevolution, retrieved on days 69, 95 and 113) and out to Chemistry units 1, 9 and 10.
- No unit repeats another unit's goals, and no review entry points at a row not yet taught.

## Day faults

None. No day skeletons or day files exist for biology.

## For the structure pass

1. Create docs/courses/biology/TOOL-ASKS.md with one heading per linked tool: body feedback; DNA-to-protein code; sealed-jar gas; energy pyramid and carbon reservoir; population model; cross and meiosis; natural selection; river and dam trade-off; fishery and species protection.
2. Optional, judgment call: decide whether days 102 and 126 in data/plans/biology/days.csv stay Fluency. They carry the first course use of HS-LS4-3 and HS-ETS1-3, and the plans treat both as practice of earlier-taught skills. The current reading is to keep them as they are.

## For Cory

None.

## Lead-list items worked

0. docs/reviews/lead-list-lens-pass-2026-11-17.md has no biology sections and no CAP rejections for biology.

## Gates (after fixes)

- `unitplan.py check biology`: PASS on all ten plans.
- `sequence.py check biology`: 0 failures. There are two notes, on days 102 and 126 (see F6).
- `goalmap.py audit biology`: it lists the goal map rows and flags nothing.
