Fix pass, english-language-arts-grade-2 unit 3 (s03.md), 2026-11-17. Gate: `python -X utf8 scripts/unitplan.py check english-language-arts-grade-2` reports PASS for s03.md (1,250 of 1,250 counted words; the cap left room for only a few words, so the counted-field fixes were written short).

Findings merged: 33 (36 raw: assessment 15, sources 10, sequence 11; three pairs were the same fault: assessment 13 with sources 5 for the lost arrows, assessment 11 with sequence 6 for codes taught in unit 2, assessment 12 with sequence 2 for the paragraph conflict). Fixed: 29. Rejected: 4 pieces. Lead: 10 lines.

Per lens, how many held up (fully or in part): assessment 14 of 15 (14 only needs a lead), sources 8 of 10 (9 rejected, 10 lead), sequence 10 of 11 (11 lead).

What changed in s03.md:
- Field 1: deleted the eight-section line that matched no days.csv section.
- Field 2: paragraph conflict settled (the 98 assignment is R3, written from the day 99 check cards, scored 101; the poster is built from 01 on 105 with own notes); pollinator, adheres, damp, tremble, glide and swoop added to the word rows.
- Field 3: pipeline remark deleted; unit 4 days corrected to 143 to 146, 150 and 155.
- Field 4: five duplicate retrieval rows deleted.
- Field 5 (all owners now come from days.csv sections 3.2, 3.7, 3.11, 3.12): A1 key and score day, arrows restored, C1 card rewritten (no printed glosses, tendril on a separate dictionary strip), R2 cards changed to shaking-release and tongue-tip mechanisms, three parallel P3 to P5 forms with verses that no longer state the contrast, look-fors for P2 and P5, five parallel oral cards for RF.2.3a, b, e and f (been dropped, local pronunciations not counted as misses), P6 lists vary by day, wrong pictures in exits 89, 91, 95, 97, 98, 102, 105, 106, 109, 112 and 117 now show the named error, rows added for C2 on 115 and for C3 and the poster components on 117, minutes for 113 and 117, one-device rotation for 102 and 105, caption of the day 96 photograph marked to confirm with a non-visual alternative, a line saying RI.2.4, RI.2.5, RI.2.2, L.2.4, re- and -ful were taught in unit 2.
- Field 6: new column "What it shows" for every letter, column "Repair (day)" holds the repairs, blank line removed, letters AM (irregular word read as regular), AN (ending letters out of order), AO (vowel team swapped) and AP (meaning the words do not support) added; said filed under AM, mapel/stapel/washabel under AN, laun under AO, the poem under AP.
- Field 7: marking sentence, AM to AP in the windows, B in the 118 window; AB and AC repairs now say 84 only (103 names neither).
- Field 8: tools named with day, mark, job and verdict; supplies added; sting-allergy plan required before any outdoor look.
- Field 10: seven readers (not eight), ours and not adapted from base readers, written before day 78; licence file path given; mining bee caption now says it collects pollen.

REJECTED: sources 9 | The USDA brochure (pages 2, 3, 5) and the NPS page are named as fact sources but no fact is assigned to a page | Over the word cap (fix needs about 22 counted words in field 10 and the plan had 6 spare); the texts quote nothing from them and field 10 already says "Use facts" | the writer's brief (verified or none) and UNIT-PLAN field 10 length cap
REJECTED: sequence 8c | Days 86, 106 and 110 carry days.csv "Shorter-year fold-in" notes the plan never mentions | Over the word cap (about 13 counted words); the fold-in is already in days.csv and no scored record sits on those days | UNIT-PLAN Length (field 3 is counted)
REJECTED: assessment 1 (one clause only) | re- is not taught until cycle 15 (day 88), so the C1 item assesses an untaught prefix | Wrong on the facts: day 88 teaches decoding of un- and re- (RF.2.3d); the meaning of re- and -ful was taught in unit 2 (e2-prefixes-suffixes, listed in field 3), so the rest of finding 1 was fixed and replant and useful were kept | UNIT-PLAN field 5 (assess what was taught)
REJECTED: sequence 10 (explanatory sentence only) | Add a sentence saying glide and swoop are met first in the check verse and the verb contrast is taught with toss and throw style pairs on 85 | Over the word cap; glide and swoop were put in the day 86 word row instead so they are named and taught before 113 | UNIT-PLAN Length (field 2 is counted)

LEAD:
- days.csv and the day 117 table: L.2.5a, L.2.5b and L.2.6 poster rows and W.2.3 now sit in the 117 table, but days.csv codes for 117 list only SL.2.4, SL.2.5, SL.2.6, W.2.6 and RF.2.3c; days 83 (RI.2.7, RI.2.4, RI.2.5, RI.2.2, L.2.4), 113 (RL.2.10) and 117 (W.2.3, L.2.5, L.2.6) need the added codes (assessment 11, sequence 6).
- The generated "rows below to sample" counts for days 115 and 117 are now smaller than the tables (a row was added to 115, five to 117); regenerate if the gate ever checks them.
- days.csv lacks W.2.6 on days 102 and 105 (sequence 4).
- The 12 sections 3.1 to 3.12 have no titles; supply them (sequence 1).
- Create docs/courses/english-language-arts-grade-2/TOOL-ASKS.md for the shared word processor and the audio recorder (sequence 3).
- Day codes and kinds for 98, 104, 111, 112 and RL.2.10; L.2.4 needs a second practice day such as the weekly word-context task on 91; first teaching of L.2.3, SL.2.5 and W.2.3 sits on Application days (sequence 6 and 11).
- Day 118 note in days.csv says to retain cycle checks on days 42, 62 and 112 for RF.2.3b; remove 42 and 62 to match the plan (assessment 14).
- source-map.csv rows for the seven readers say "adapt where rights are cleared"; the plan now says they are new texts, not adapted. Update the decision, or supply the base reader licence evidence (sources 3).
- Write wordlist.csv and the ELA item rows (text_id, text_ref) in items.csv after the manuscripts exist; they are not yet in the course folder (sources 10).
- Someone must view the Mike Budd photograph and confirm pollen on the head hairs and none on the wings before day 96; the caption is marked to confirm (sources 6). The brochure and NPS pages have not been checked for any fact (sources 9).
- The question budget paragraph in field 5 predates the added rows and parallel cards and is not recounted.
