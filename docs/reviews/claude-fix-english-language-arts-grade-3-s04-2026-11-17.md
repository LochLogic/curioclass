Fix report: english-language-arts-grade-3 unit 4 (s04.md), 2026-11-17. Edited: docs/courses/english-language-arts-grade-3/s04.md only (file also normalized from CRLF to LF).

Findings merged: 35 (assessment 16, sources 10, sequence 11; assessment 4 and sequence 1 are one finding, assessment 2 and sequence 6 share the 137 and 154 minutes). Fixed or partly fixed: 25. Rejected: 10 (whole or part). Lead: 7.
Held up per lens: assessment 16 of 16 (13 and 15 in part), sources 8 of 10 (6, 8, 9 not applied; 4 is a lead item), sequence 9 of 11 (1, 4, 8, 9, 10 in part or not applied; 3 and 11 lead only).
The merged-document word count stood at 1,794 of 1,800, so counted-field fixes were written to net zero and the rest rejected over the cap. Gate: `python -X utf8 scripts/unitplan.py check english-language-arts-grade-3` PASS for s04.md (1,799 words counted).

Main changes: O04 samples added under the 144 W.3.1a to d rows; 152 L.3.2b now scores the I11 address block; 154 ledger minutes reconciled; skills conference limited to RF.3.3c, RF.3.3d, RF.3.4b; SL.3.1a to d now taken from 141 and SL.3.2, SL.3.3 from 149; P124, P135 and E135 glosses removed; P131A and B each given a differing detail; E122, E124, E126, E128, E129, E131, E135, E138, E141, E144, E145, E146, E148, E154, E156 and E125 reworked; fresh nouns in the 145 and 152 scored items; letter AU added, R and AD reworded, U/V filing on 152 W.3.2a fixed; Owner column now names sections; field 7 audio and 146 repair timing fixed; U6 minute splits for 125, 136, 137, 138, 140, 146, 151, 155 (P135 revision moved to 136 repair ten; C137 L.3.4 rows and story strip moved to 138 reading); P154A cites Table 16; P154B names the first list and the complexity check is required before RI.3.10 use; news link removed; Population Growth checked-only-against-source-store statement; Water on Earth figures must cite free agency pages.

REJECTED: assessment 13 | AC and AD (the 153 W.3.6 and 154 RI.3.10 errors) are teacher recording notes and should leave the student register and field 7 groups | AD was reworded to a real student misconception matching its 154 wrong answer ("relies on the teacher reading the passage to supply its meaning") and AC already describes a child counting watching as typing; dropping both would orphan the letters cited in those rows | none
REJECTED: assessment 15 | add the sentence "Response is counted once: on respond days 125, 132 and 136, and inside check days 145 and 156" to field 7 | over the word cap (field 7 is counted and the plan sits at 1,799 of 1,800); the audio-feedback contradiction and the 146 repair timing were fixed | UNIT-PLAN Length
REJECTED: sequence 4 | add a sentence listing where RI.3.3, RI.3.5, RI.3.8, L.3.1a, L.3.1f, L.3.5a, W.3.2b to d, W.3.4 and W.3.6 were taught earlier | over the word cap (about 35 words); the false 121 sentence was replaced with "taught in unit 2; 122 and 127 continue them" | UNIT-PLAN Length
REJECTED: sequence 1 | add to field 2 that 149 and 151 hold the discussion, listening, recording and revision records | over the word cap; the ledger and the 149 paragraph now name where each record is made, and the days.csv change is a lead item | UNIT-PLAN Length
REJECTED: sequence 8 | change the g3-u4-03 text row to list the rereads on 130, 137 to 138, 146 and 150 to 151 | over the word cap | UNIT-PLAN Length
REJECTED: sequence 9 | mark each handoff in field 3 as strong or weak and name RI.3.3 and RI.3.8 as weak | over the word cap (about 20 words) | UNIT-PLAN Length
REJECTED: sequence 10 | add a safety and limits line to field 8 | over the word cap; the limits already stand in field 7, field 10 and the 150 and 156 notes | UNIT-PLAN Length
REJECTED: sources 6 | name the elementary science safety guide the safety read will use and repeat the limits in field 8 | over the word cap | UNIT-PLAN Length
REJECTED: sources 8 | list the independent reading set (titles, editions, rights) under still needed | over the word cap | UNIT-PLAN Length
REJECTED: sources 9 | add a sentence that only lesson structure was used and the trade book is replaced | field 10 already says trade books were not read or paraphrased and the base is the 2017 lesson structure; restoring the cut titles is a lead item | none

LEAD:
- days.csv: add SL.3.1a to d, SL.3.2 and SL.3.3 to 149 (note naming the formal discussion) and SL.3.4, SL.3.6, L.3.3b and W.3.6 revision to 151, then regenerate (sequence 1).
- days.csv: change the 154 goal to "Independently compare two water texts and record the support used" (sequence 3).
- data/plans/english-language-arts-grade-3/wordlist.csv: write it for unit 4 from the field 2 week table (sequence 11).
- ela-texts.csv g3-u4-03: update title, source, status "on file" and edition, and the 126 and 134 goal wording that says "town-treatment text" (sources 4).
- ela-texts.csv g3-u4-01 todo: manuscript lists every figure with its named free agency source and access date; unsourced figures cut (sources 5).
- source-map.csv: restore the cut base-lesson titles (sources 9).
- Text agent list: complexity checks of P154A and P154B; confirm the Population Growth free public copy, an elementary science safety guide title and year, and the independent reading set (sources 1, 6, 8, 10).
