# Units read together: math-grade-2, 2026-11-24

COURSE-RUN stage 4 (Reads). Expert read of all nine unit plans as one course.

## What I read

AGENTS.md; docs/COURSE-RUN.md stage 4; docs/agents/EXPERT.md; docs/agents/lenses/math.md; docs/courses/UNIT-PLAN.md; docs/GLOSSARY.md; docs/courses/math-grade-2/frame.md and scope-and-sequence.md; data/plans/math-grade-2/days.csv (all 160 rows); s01.md to s09.md in order (fields 1 to 10 and goal maps); the grade 2 rows of data/progressions/math.csv; the grade 1 last unit plan (s08); the grade 3 unit 1 plan (fields 2 to 4). Lead list docs/reviews/lead-list-lens-pass-2026-11-17.md has no math-grade-2 section.

## Verdict

The course holds together well: the respond chain, retrieval days, MP days, model progression (ruler to number line to three-digit line, tapes from unit 1 to unit 9) and the base text order all line up across units, and continuity in from grade 1 is sound. The main course-level fault is assessment load: units 3 to 6 re-score maintained codes (2.OA.A.1 above all) on teaching days the focus ledger counts, which conflicts with the scope and sequence's reuse rule. Five goal map rows drifted from their goal verbs and are fixed. The grade 3 end of the grade 2 handoff record is missing.

## Findings

| # | Severity | Finding | Verdict |
|---|---|---|---|
| F1 | Moderate | Maintained codes re-scored in units 3 to 6. s03 day 57 adds F (2.NBT.B.5) and S1 to S13 (2.OA.A.1); s04 adds Q items for 2.OA.A.1 and 2.MD.B.5 plus F, collected on days 70 to 72, which days.csv does not mark observe and counts as 55 major minutes; s05 adds F on day 80 and L (2.MD.B.6) on day 89, neither on the day 89 codes; s06 day 110 adds L1, L2, N, F, A4, R1 to R14 and T from teaching days 105 to 108, while the day 110 row lists only 2.MD.C.7, C.8, G.A.1, G.A.3. Source: the 2026-11-16 lens-assessment pass. 2.OA.A.1 ends up fully scored in units 2, 3, 4 and 6 plus day 90, against "Reused individual records inform support and the handoff without another collection or score". | For the structure pass (shared file and a course-wide call). Not edited in the plans, since that would reverse a lens decision piecemeal. |
| F2 | Minor | Exit drift from goal verbs. Day 50 (s03) goal plans one or two calculations, exit was one-step only. Day 121 (s07) strengthen addition, exit only picked a method. Day 127 (s07) choose and justify, exit had no justification. Day 160 (s09) row said "fix a flaw" but the written exit has no flaw; it asks for both steps, the unknown and a check. | Fixed: four goal map rows rewritten (s03 50, s07 121 and 127, s09 160), practice shapes kept different from exits; 121 exit kind now produce (strengthen takes either). |
| F3 | Nit | s01 day 6 practice "roll-and-race game" implies speed in a fluency practice set without time pressure. | Fixed: "roll-and-move game". |
| F4 | Minor | Cross-grade hand-back with one end missing. Grade 2 day 160 builds a grade 3 handoff record (facts inventory, within-100 fluency notes, unresolved gaps); grade 3 s01 field 4 never reads it, while grade 2 s01 does read the grade 1 facts record. | For the structure pass (another course's file). |
| N1 | Note | s08 days 137 to 140 teach arrays but carry only 2.OA.B.2 codes. They are observe days, and s08 says so. | No change. |
| N2 | Nit | s08 supplies list "counters or dried beans" beside "replace swallowable pieces with large paper counters". | No change; the replacement line governs. Optional tidy for the day writer. |
| N3 | Nit | s01 error register lists K before J. | No change; order carries no meaning. |

## For the structure pass

1. F1, choose one and apply course-wide:
   - (b), recommended: maintained-code items in units 3 to 6 (s03 day 57 F and S items; s04 days 70 to 72 Q and F items; s05 day 80 F and day 89 L items; s06 days 105 to 108 and day 110 L1, L2, N, F, A4, R, T items) feed response groups, the day 90 course check and the grade 3 handoff, not the end-of-unit score. Add one line to field 5 of s03 to s06: "Items on maintained codes are maintenance evidence for response groups and the handoff, not part of this unit's score."
   - (a): mark days 70, 71, 72, 80, 105, 106, 107 and 108 `observe` in data/plans/math-grade-2/days.csv, add the maintained codes to the day 89 and day 110 code lists, and recount the focus ledger in scope-and-sequence.md.
2. F4: in docs/courses/math-grade-3/s01.md field 4, add "Read the grade 2 handoff record from grade 2 day 160 (facts inventory, within-100 fluency notes, unresolved gaps) if supplied."

## Day faults

None: no days are written for math-grade-2.

## For Cory

None.

## Lead-list items worked

0 (no math-grade-2 section in the lead list).

## Gates (after fixes)

- unitplan.py check math-grade-2: PASS, s01 to s09.
- sequence.py check math-grade-2: 0 failures; one note, day 1 2.OA.B.2 Fluency on the first course day (expected: retrieval of a taught grade 1 skill).
- goalmap.py audit math-grade-2: 143 goal map rows audited, no failures.
