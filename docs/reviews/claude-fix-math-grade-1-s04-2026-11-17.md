# Fix: math-grade-1 unit 4 (s04), 2026-11-17

Findings merged: 16 (17 raw: assessment 8, sources 3, sequence 6; sources 3 and sequence 4 name the same unnamed routines). Fixed: 16, of which 4 only in part (see REJECTED and LEAD). Held up per lens: assessment 8 of 8, sources 3 of 3, sequence 5 of 6 fully usable (the sixth, 5, belongs to the skeleton). Gate: `unitplan.py check math-grade-1` PASS for s04.md. The file was CRLF; it is now LF as the brief requires.

Notes on how findings were applied:
- Assessment 1: three group numbers 48, 83, 66 with keys and the no-overhearing rule. Assessment 2: 62 changed to 92 throughout field 5. Assessment 3 and 8: day 89 and day 83 exits changed as asked (day 89 wrong answer now letter C). Assessment 4: thirds of about ten, and the one-sentence rule added. Assessment 5: owners set. Assessment 6: A to day 69, B to day 74, E to day 71. Assessment 7: four-group cap added.
- Sources 1: guide named for its general young-children safety and supervision guidance, small-piece rule marked ours, untested. Sources 2: "read for planning only, nothing quoted" and "no problems, wording or images are used" added. Sources 3 and sequence 4: pipeline phrases removed, plain sentences added, rounds named in the day 73, 80, 81 and 90 rows (day 73: unit 3 center days 60 and 66; day 80: day 79's ten minutes; day 81: day 73; day 90: days 77 and 78).
- Sequence 1: Limits sentence and "each sum as a ten-more step" added. Sequence 2: ten-less prompts added to the day 80 row (ten less than 95 and than 14) and the day 81 row (one from 90 to 99, one from 10 to 19). Sequence 3: Carried sentence added (unit 3 days 47 to 51 confirmed in days.csv). Sequence 6: day 92 practice blocks now one named task.

REJECTED: assessment 5 | Set owner of the 1.NBT.B.2c (decade) row to Section 4.2 | Decades and zero ones are taught in section 4.1 (days 69 and 70, nine tens, ninety), so 4.1 is the owner; the other rows were changed (B.2 to 4.2, B.3 to 4.4, C.5 to 4.3, B.2a to 4.5, B.2b to 4.2, C.6 stays 4.1) | UNIT-PLAN field 5 (owner is the section that teaches the item)
REJECTED: assessment 4 | Change the day 89 to 91 middle blocks to ten begin, twenty-five rotation, ten further | days.csv notes for days 89 to 91 fix the rotation at 20 minutes, and the proposed day 90 and 91 blocks (5 + 10 + 25 + 10) add to 50, not 45; the thirds wording and the one-sentence rule were applied instead | none (days.csv; see LEAD)

Small deviations (item-level choices): sequence 2 used ten less than 95 (85) instead of 94 (84) because 84 is in the day 90 exit; the second ten-less prompt went into day 81 (a mental-ten fluency day) rather than day 86.

LEAD:
- Day 89 to 91 rotation of 20 minutes for about ten children at seven explanations is tight; if the rotation is lengthened to 25, days.csv notes for days 89 to 91 and the U6 and field 5 rows must change together, taking the five minutes from further work (day 90 and 91 have only 5 spare after revisions).
- Add 1.NBT.B.2a to days.csv rows 69 and 87 and 1.NBT.B.2b to row 74 so generated codes match the Carried sentence.
- Skeleton field 10 sensitive-topics line says counting collections from home is optional, against field 8 and day 91 (request nothing from home); fix in the frame and unit_skeleton.py. Also put field 8's loose-piece supervision rule into the days.csv safety column for days 69 to 91.
- Ten more from 90 to 99 handoff after day 119 needs a scheduled unit 6 day (unit 6 days.csv and scope-and-sequence.md).
- Sources 2: name a free public host of the base-ten Progressions in place of the mathematicalmusings.org copy if one can be verified; none was checked in this job.
