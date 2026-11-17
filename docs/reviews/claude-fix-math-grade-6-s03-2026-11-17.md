math-grade-6 s03 fix, 2026-11-17

Findings merged: 24 (assessment 9, sources 6, sequence 9; sources 6 and sequence 8 are the same fault as one finding, so 23 distinct plus the shared E41 point counted once under assessment 4 and sources 2). Fixed 23 (3 in part), rejected 0 outright, lead 4.

Held up per lens: assessment 9 of 9, sources 6 of 6, sequence 9 of 9.

Fixed in docs/courses/math-grade-6/s03.md:
- Assessment 1 (E48): second offer is now $14 for 8 feet; answer is first, $18 versus $21; K is the second-offer choice.
- Assessment 2 (P1): key now reads "4 quarts is 1 gallon, so 1 gallon; P1 is finished after P3". C kept.
- Assessment 3: S2(a) and P4 no longer name the whole or 100 percent; kept as a look-for.
- Assessment 4 and sources 2 (E41): ribbon of 250 centimetres, answer 2.5 metres and the string; C is 25,000 metres. The paper clip length is no longer asserted. The inch half of the old item is gone because of the two-part limit.
- Assessment 5: owners set by where the work is taught (3.2 for M1, M2, P2, P3, S1; 3.3 for P4, S2; 3.1 for M3, P1, S3).
- Assessment 6: day 50 and day 51 repair split written into field 7.
- Assessment 7: M1 reworded, "per one" now a look-for only.
- Assessment 8: E56 (b) replaced by "18 is 40 percent of what"; answer 45; wrong 7.2 (G).
- Assessment 9: E59 (a) cut to two unit rates and the 10-minute count; C item (8 minutes in seconds) moved to a day 59 repair item in field 7.
- Sources 1: edition named (Illustrative Mathematics Grade 6, first edition, CC BY 4.0), extraction remark deleted. No year is given because none is on file.
- Sources 3 (in part): conversion line added in field 10, "from memory", National Institute of Standards and Technology pages named, link marked to be confirmed, US liquid quart stated.
- Sources 4 (in part): scissors on day 42 named; the UK link is marked unchecked and a US teacher is told to follow the school's own rule. No US guide was named because none could be verified.
- Sources 5: line added to P3 that paint figures are not real.
- Sources 6 and sequence 8: handoff remark reworded.
- Sequence 1 (in part): field 8 now gives each tool's mark, days, jobs, "fits, needs no spec" and "No key tool"; U6 evidence cells carry "Tool, job". No TOOL-ASKS link, because the file does not exist (see LEAD).
- Sequence 2: day 46 retrieval no longer plots; repair is repeated addition.
- Sequence 3: hook now says crate.
- Sequence 4: arcs rewritten to days 50 to 54 and 55 to 59.
- Sequence 5: limits now allow tenths and hundredths and decimal division by scaling a table (unit 5 owns the algorithm, confirmed in the scope and sequence).
- Sequence 6: MP6 and MP2 given days and tasks.
- Sequence 7: supplies named (ruler with both units, string, day 41 objects, grid paper on days 54 and 57).
- Sequence 9: tape meaning on days 49 and 58 added to Carried.

Gate: python -X utf8 scripts/unitplan.py check math-grade-6 gives PASS for s03.md.

REJECTED: none

LEAD:
- Create docs/courses/math-grade-6/TOOL-ASKS.md for the paper instruments (double number line, ratio table, tape diagram, area model) and then link it from field 8 (sequence 1).
- days.csv notes for days 49, 57, 58 and 59 carry "On a 45-minute period ..." boilerplate while the course period is 50 minutes; the skeleton Practices line stops at "MP2" (unit_skeleton.py or days.csv).
- days.csv names three tools on days 49, 58 and 59, over the two-parts-a-day limit of UNIT-PLAN rule 8; the U6 tags say "paper tools of the student's choice" on those days.
- The National Institute of Standards and Technology link and a US school cutting-tools guide still need verifying and adding to field 10.
