# Section refine: math-grade-1 unit 4 (u04-1 to u04-5), 2026-11-27

Read cold against docs/pipeline/briefs/section-write.md, docs/courses/UNIT-PLAN.md ("The rules", "The section plan: fields, in order", "Length"), DEFAULTS.md, the unit plan s04.md, the rebuilt skeletons and the prep notes. Before this pass, the same session ran the unit's answer-key read (docs/reviews/math-grade-1/answer-key-math-grade-1-u04-2026-11-27.md).

Checked and holding: every exit, key, worked case and listed wrong answer solved; one register letter per wrong; minutes add to 60 on all 24 days; the rotation of six heard runs 1 to 30 without a gap from day 69 to day 92, with all thirty papers handed back; the day-80 exit (one minute, then six children twice at 45 seconds, nine minutes, then two minutes) and the packet days (20 working minutes, ten children at two 45-second turns in 15 of 20 rotation minutes) fit; kinds, codes and student goals match days.csv; all seven field 5 rows are owned; signs are taught on day 83 before E83, "least" and "greatest" on day 85, "ten more", "ten less" and "mentally" on day 79, and "exchange" on day 87; there is no em dash, "gap" or TODO(writer); every file is under the cap (`unitplan.py check` PASS).

## Faults

| File | Fault | Fix or rejected | Stage |
|---|---|---|---|
| u04-1.md field 3 | P decade, P differences (two items) and Fresh subtraction trace had no "Shape:" line, so day 92's "see the Shape lines in section 4.1" pointed at nothing. | Added four Shape lines with Data ids s04-A89decade, s04-A89difference, s04-A89zero and s04-A92difference. | write (the prep notes gave them) |
| u04-2.md field 3 | P digit values had no Shape line. | Added one for s04-A89digit. | write |
| u04-5.md field 3 | P unit ten had no Shape line. | Added one for s04-A89unit. | write |
| u04-1.md day 69 | Exits 69 to 81 ask what goes on a "tag", but no day taught the word. | Day 69's synthesis writes the total on a paper tag and says that a tag is the label that tells how many. Ledger row added. | write |
| u04-4.md day 83 | E86, E89 and both comparison sets ask "What comparison...?", but the word was never named. | Day 83's model calls each signed statement a comparison. Ledger row added. | write |
| u04-1.md day 69 | "Unfold the separate sticks in A to check" was unclear. | Now reads "For the A contrast, unfold one stick to check that it is worth ten ones." | write |
| u04-2.md field 9 | "the kindergarten word expression from section 4.4, day 78" read as this grade's section 4.4. | Now reads "kindergarten section 4.4 (its day 78)". | write |
| u04-4.md E84, E85; u04-2.md E75 | The child slips and keys did not match field 3 and items.csv (combined stems, printed totals, identical middle pictures). | Fixed in the answer-key read: slips and keys rebuilt. Field 3 now matches them. | data |
| u04-2.md P teen (s04 field 5 row 7) | 17 as one ten and seven ones was already a unit 3 exit (E50). | Rejected: every teen from 11 to 19 already has such a case in kindergarten or units 1 to 3. The torn packing record is new, so rule 4 holds by case. | unit plan |
| u04-1.md E72 | The three-ten tray also appears as "thirty" on whole-ten-cards. | Rejected: the card names a decade and the exit removes tens. Different skill, different case. | none |
| u04-5.md P unit ten | Its "____ = ____" line has two blanks. | Rejected: one trade statement, one ask, one box to draw in. | none |
| u04-5.md E91 | s04-X91a's wrong row has no letter. | Rejected: it records a missing, unscored estimate, not a wrong answer. | none |

Ledger: I read the 133 unit 4 rows and they cover the terms, cases, models and routines the plans teach, including review rows marked "planned only" where the target is still planned. I added two rows, one `ledger.py add` call each with the day blank: u04-1 term "tag" and u04-4 term "comparison", both `--student-word`. `ledger.py check math`: 7,541 rows, 0 problems.

Gates: `unitplan.py check math-grade-1` passes u04-1 to u04-5 and s04 (its one FAIL is s03.md, another unit). `gate.py --course math-grade-1` shows no new FAIL from these edits. The FAIL lines it lists as new (13 in plan-math-grade-1 for s01, u01-1/family.md, s03.md) were there before this job. The stored baseline, build/gates/base-math-grade-1/, holds only index-reports.txt, so the other gates report "[no baseline file]" and count every line that already failed as new. This job never edited items.csv, s01.md, s03.md or family.md, and all were last changed before it began. The 334 orphan lines match the baseline. Template point: the gate stored a baseline for only one of its gates.

## Plan points

- s04.md field 5 "Collection and scoring" hears all seven explanations inside the 20-minute rotation, at about two minutes a child. Ten children then fill the whole 20 minutes and leave none for moves and notes. u04-5 instead hears the two mental directions at 45 seconds each (15 minutes) and the paper explanations in the next practice part. The section keeps its version; the unit plan line should match it.
- s04.md field 5 row 7 fixes the teen at 17 (see the rejected row above). Later unit plans should choose teen cases by picture and context.
- The data stage split s04-X75, s04-X84 and s04-X85 in items.csv without rebuilding their slips and keys. The answer-key read fixed this, but the data kit's line "Shared pieces and cards print exactly the items.csv stems" was not followed.

## Changed for the next unit

- When the data stage splits a stem into two or three ids, rebuild the child slip and the teacher key entries in the same job. The slip prints each items.csv stem, and each id gets its own key entry (exits 75, 84 and 85 were stale).
- Draw a sign box as a bordered box, never with □, the mark used for a unit square.
- Every end item in field 3 keeps its own "Shape:" line with its Data id, as exits do.
- A word an exit stem leans on (here "tag" and "comparison") is taught on or before that day and gets a ledger term row.
- Teens 11 to 19 all have a taught "ten and some ones" case by now. Later items keep rule 4 by using a new picture or context, never a remembered one.
