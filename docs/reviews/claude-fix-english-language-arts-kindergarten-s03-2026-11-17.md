Fix pass, english-language-arts-kindergarten unit 3 (s03.md), 2026-11-17.

Findings merged: 35 (assessment 16, sources 9, sequence 10; no finding was named by two lenses). Fixed 30 (some in part), rejected 5.
Held up: assessment 15 of 16 (one rejected), sources 5 of 9 fixed, 4 rejected or left to LEAD, sequence 10 of 10.
Gate: unitplan.py check, s03.md PASS (1796 of 1800 counted words).

Fixed (lens number): assessment 1 (T1 starts day 85 and never day 84, T2 keyed to the text read, T3 day 100 plus next sharing turns), 2 (SL.K.1a and b rows on day 86, day 87 rows marked children 16 to 30), 3 (day 116 W.K.2 row with four rows, letters and samples), 4 (exit 100), 5 (P2 sample), 6 (T2 Y item), 7 (exits 83 and 88; 82 kept), 8 (exits 111 and 118, no-reuse line), 9 (puts changed to hid, the, a and in confirmed mapped in unit 1), 10 (C2c, exits 106 and 115), 11 (P4 sample), 12 (P foil in exit 85, W follow-up in T1), 13 (C1 passage), 14 (exit 84), 15 (R0 rows), 16 (S1 connection cell on day 116). Sources 1 (04 credit), 2 (06 riddles), 3 (05 basis), 4 (measures), 5 (Skills Block line), 7 and 9 (key recheck, combined). Sequence 1 to 10 all applied (header and owner cells now "unit 3", retrieval row for pictures and words moved to day 81, day numbers, retell added on days 89 and 90, vocabulary row 21, supplies, unit 4 hand-off, day 107 repair reason, field 4 wording).

REJECTED: sources 6 | Facts checked names pages only for some animal facts; add a source for each or mark cards invented | Added source text for each fact would take research outside this fix and the folio already says each case is invented for practice; the 120-word headroom is used | over the word cap (the counted fields have 4 words left) | the writer's brief (field 10 word cap)
REJECTED: sources 8 | Name the image source for the day 83 and 103 photographs and add a state or district outdoor-supervision guide to the safety read | A new guide needs a search for a state source and about 25 counted words | over the word cap | the writer's brief (field 10 word cap)
REJECTED: assessment 7 (in part) | Exit 82 and exit 83 restate 01b and should change | The lens itself keeps 82 on roots and water, and 83 is already changed to remove the roots clause; 82 is left as a fresh two-fact case | none | none
REJECTED: sources 3 (in part) | Add the unit 3 archive link beside the other two | The unit 3 archive address is not on file and is not invented | none | none
REJECTED: sequence 7 (in part) | List the supplies in full including original tree photographs sources | Supplies line now names the added items; image source left to the LEAD | over the word cap | the writer's brief (field 8 cap)

LEAD:
- days.csv day 86 codes omit SL.K.1; day 83 omits W.K.7 and W.K.8; day 116 omits W.K.2; days 85 and 91 omit RL.K.1, RL.K.10, RI.K.1, RI.K.2, RI.K.10 and SL.K.2.
- days.csv has no sharing day for T3 other than day 100; decide where the other children take it.
- ela-texts.csv: gk-u3-06 title and form (four riddles, "Who Depends on Trees?") disagree with the plan; gk-u3-05 source says el-education-k5-2017 while the plan replaces the text; text set line 06 still prints "Who Depends on a Tree?" (generated).
- source-map.csv marks the seven Skills Block files "keep" while the plan replaces them with original readers.
- Decide whether unit 3 keeps one merged document or gets nine section plans (days.csv sections 3.1 to 3.9).
- Name the source of the day 83 and 103 tree photographs and add a state or district outdoor-supervision guide to the safety read; add a source for the animal facts in the folio and exits.
- Field 5 "Time: 2 rows below" line for day 86 is generated and now counts four rows after the added SL.K.1 rows; regenerate with the skeleton script.
