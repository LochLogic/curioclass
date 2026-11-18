# Fix: math-kindergarten unit 1 (s01.md), 2026-11-17

Findings merged: 18 (assessment 8, sources 5, sequence 5), no overlaps. Fixed 18, rejected 0. Held up: assessment 8 of 8, sources 5 of 5, sequence 5 of 5.
Gate: `unitplan.py check math-kindergarten` PASS for s01.md.

Notes on the fixes:
- Letter C reworded; new letter E (judging by looks) added after D with a day 10 example and repair; E10 now eight plates over four spoons, E11 lists "rings eight" under E.
- Day 18 boats and kites are cut paper pieces; field 7 maps letters A to E to repairs and says which day each record is classified; written-feedback shape added to the record.
- Repairs A and B reworded so they differ from the day 1 routine and the day 12 model.
- Sources: safety guide described by what it covers (age-label and swallowable-piece checks are ours); the 2019 Progressions licence is written as not confirmed in this read (the PDF was not re-opened); credits, activity-text reading and original-art lines added; family note carries the small-items line.
- Arcs recut to days 1 to 5, 6 to 9, 10 to 15 and 16 to 18; oral counting to ten by day 11 and the day 14 limit added.
- The file was CRLF and stays CRLF.

REJECTED: none

LEAD:
- days.csv has an empty `safety` column on every day; add a safety line for days 1 to 5 and 17 (loose pieces).
- Confirm the merged U3 and U6 document for a five-section kindergarten unit is deliberate (UNIT-PLAN limits merged documents to one-section units).
- days.csv codes day 14 as K.CC.B.4a only although its goal connects the last word to how many.
- If the 2019 Progressions PDF licence line is to be stated as CC BY 4.0, someone must read it on the PDF itself.
