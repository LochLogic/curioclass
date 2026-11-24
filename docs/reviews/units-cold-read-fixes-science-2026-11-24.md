# Science unit plans: cold-read fix pass, 2026-11-24

The fix pass on docs/reviews/units-cold-read-science-2026-11-24.md, with Cory's science Desk calls of 2026-11-24 applied
in the same pass. Science courses and the science ledger only. Written days (kindergarten to grade 3, grade 7 days 1 to
6) were not edited; changes they need are rows in data/plans/defects.csv (found_by "cold-read fix 2026-11-24").

Outcomes: 11 findings: fixed 5 (1, 2, 4, 5, 11), no change 6 (3, 6, 7, 8, 9, 10), of which 2 were already fixed by
today's regenerated lines (6, 8); 1 item for Cory (part of 5). Defect rows added: 7.

## Findings

| # | Finding | Outcome | What was done, and why |
|---|---|---|---|
| 1 | Exit is the practice again on a new case | Fixed | 50 Goal map exits rewritten as distinct checks of the day's goal (an explanation, a prediction, a judgment of a supplied plan or record, an error to find and fix), with the exit kind still matching the goal verb and the practice cell unchanged. Grade 7: the 11 named days (31, 34, 79, 85, 105, 112, 115, 119, 133, 138, 153) and 23 more rows whose exit opened with the practice's own verb (26, 32, 37, 47, 53, 55, 60, 69, 74, 87, 108, 111, 118, 120, 121, 122, 137, 140, 145, 146, 150, 151, 152). Grade 8: days 15, 35, 37, 67, 68, 81, 141. Biology: 28, 38, 60, 102, 107, and 152 (s10, same fault). Physics: 122, 138, 140. No days.csv exit cell held these exits (grade 7's exit column is blank for them; grade 8 and the high school courses have no exit column). Not done here: other same-verb rows outside the named list (about 60 across grades 4 to 6, 8 and the high school courses, many arguably sound) and the retooled practice-shape check, which is a scripts change for the lead. |
| 2 | Ledger has no rows for grades 4 to 11 | Fixed | `ledger.py seed science` with 1,367 unit-level rows (where = sNN, stage planned) for grades 4 to 8, Biology, Chemistry and Physics: each owned progression row's words as terms, its model_out as models (note: built here, or used and extended here), and each unit's anchoring phenomenon as a case. UK spellings normalized in the seeded text. Section writers add section-level rows later as the brief says. `ledger.py check science` is unchanged before and after: 0 planned-only findings, the same 2 unmatched grade 2 citations. |
| 3 | No handbacks.csv or materials.csv for most of grades 4 to 11 | No change | The cold read itself sequences this after the Codex draft run's grades 4 to 6 output is reviewed, so nothing is written twice; it is stage 5 plan data, not a unit-plan fix. |
| 4 | Source maps: harms_learning in prose, days with semicolons | Fixed | Grades 6, 7 and 8 source-map.csv: harms_learning reduced to yes, no or unclear (328 rows) with the reason moved to the end of `why` as "Harms learning: ...", and day cells space separated (195 rows). plan.py check for grade 7 went from 175 failures to 22; the 22 left are stage 5 items not yet written (15 days with no exit item, assessment days 13 and 22) and 4 sections missing from data/units.csv. |
| 5 | Grade 7 unit 1 reteaches grade 5's closed-system weighing | Fixed in the plan; defect row; progression for Cory | days.csv day 5 note now names the grade 5 s5-conserve-weight work (days 8 to 15) and says open and closed systems are review; s01 field 4 gains a day 5 recall task (three minutes, key and miss move); the s01 day list row matches days.csv. Days 5 and 6 are written: defect row. The progression change (s5-conserve-weight in s7-reactions-atoms' assumes) needs owner review per stage 2 Fix: For Cory. |
| 6 | "Progression skills owned" lines wrong | No change | Already fixed by today's regenerated owned lines (grade 6 s02 and s03, grade 8 s01, Physics s01 and grade 3 now list only owned rows, with review and later rows on their own lines). |
| 7 | Readiness where the rule says retrieval | No change | Grade 4 s04 and s06: the day 56 and day 93 notes give the reason (the later uses were retrieval only, or a different part of the row), so the readiness is a reasoned call. Grade 7 s01: the s6 rows are counted as readiness only because day 1's readiness note names their day 2 retrieval; a generator artifact already left for the lead (grade 7 F9). |
| 8 | Grade 6 s02 lists s4-light-eye under Builds on | No change | Already fixed by today's regeneration: s02 Builds on no longer lists it; the retrieval is unit 1 day 2, in s01. |
| 9 | Practice-only assumes links in grades 1 and 2 | No change | The cold read asks none; K to 3 is signed off. |
| 10 | Grade 12 electives have no unit plans | No change | Not a finding against the core courses. |
| 11 | UK spellings | Fixed | Chemistry day 5 "behavior" (days.csv and s01), Physics s09 day 138 "kilometers", Biology day 102 "center" (days.csv, s07 Goal map, day list, retrieval and look-for lines; "center and spread" for "centre/spread"). |

## Cory's calls applied (2026-11-24)

1. **Kindergarten goggles.** s01 cost line, s03 and s05 safety lines, the scope and sequence materials note and the frame
   now say the school supplies the child-sized Z87.1 splash goggles, with the dated photographs (no trial) where a school
   has none. The course safety page is a written page: defect row.
2. **Kindergarten costs.** Accepted at $42 as about $40: the scope and sequence table now shows unit 4 at $10 (as its
   plan says) and a $42 total, and the frame's allocation list matches. No trim.
3. **Grade 6 safety guide.** All six units cite NSTA's Safety and School Science Instruction with the line "Teachers also
   follow their own district's science safety rules"; unit 6's state handbook cite is replaced.
4. **Grade 7 units 2 and 3 materials.** Unit 2 trimmed from $255 to $175: no new balance or graduated vessel (unit 1's
   balance and a kitchen measuring cup), gloves for the one salt handler per group and the teacher (120, not 400), school
   soap and towels; one child $62. Unit 3 trimmed from $80 to $63: 50 glucose strips, not 100, and goggle wipes only.
   The scope and sequence rows for units 2 and 3 now match the plans (class 175 and 63, one child 62 and 37), the year
   totals read 506 and 163, and two stray cells in the unit 3 and 6 rows were removed.
5. **Grade 1 unit 4.** Day 30, the review day that repeated the band test on a box drum, is now the first
   reverse-direction teaching day (Understanding): a teacher-run speaker beside a tissue strip, sound off and on twice,
   answering day 29's question; the drum moves into day 31's stopping test, and day 32 becomes the second
   reverse-direction day before day 33's assessment. Changed: days.csv day 30; s04 header counts, storyline, carried
   line, exit-question context, Goal map row, materials line, generated tools-and-safety block and day list; the scope
   and sequence unit 4 text and its shorter path (nine folds, 59 meetings, minutes recomputed). Exit X30 and the items
   are unchanged. Defect rows: d029 (Tomorrow line), d030 (rewrite), d031 (drum now first appears), d032 (second
   reverse day) and section plan u04-1.md.

## For Cory

- **Progression assumes for s7-reactions-atoms (finding 5).** (a) Add s5-conserve-weight to its assumes, so the grade 7
  unit 1 readiness table and the continuity checks see grade 5's weighing (my pick); (b) keep the link only as the day 5
  note and plan recall. Owner review is the stage 2 Fix rule for any progression change.

## Gates (after the edits)

- `python -X utf8 scripts/unitplan.py check`: 720 PASS, 0 FAIL (1 physics s10 note, as before).
- `python -X utf8 scripts/sequence.py check <course>`: 0 failures for science-kindergarten, science-grade-1,
  science-grade-6, science-grade-7, science-grade-8, biology, chemistry and physics.
- `python -X utf8 scripts/goalmap.py audit <course>`: runs clean for the same eight courses.
- `python -X utf8 scripts/ledger.py check science`: exit 0; citation check unchanged (2 unmatched, grade 2, existing).
- `python -X utf8 scripts/plan.py check`: science-grade-1 13 failures before and after (the known sections not in
  data/units.csv); science-grade-7 175 to 22. `scripts/frame.py check science-grade-1`: 0 failures.
- `python -X utf8 scripts/lesson.py check`: science-grade-1 unit 4 days report 0 failures with the new days.csv.
