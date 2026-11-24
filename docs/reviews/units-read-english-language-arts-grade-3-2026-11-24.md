# Units read: english-language-arts-grade-3, 2026-11-24

COURSE-RUN stage 4 Reads. One expert reader (ELA lens) read all four unit plans together, then fixed them.

## What was read

- AGENTS.md, docs/COURSE-RUN.md stage 4, docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/courses/UNIT-PLAN.md, docs/GLOSSARY.md.
- Frame, scope and sequence, data/plans/english-language-arts-grade-3/ (days.csv, items.csv, wrongs.csv, handbacks.csv, source-map.csv, wordlist.csv).
- Unit plans s01 to s04 and the section plans u0N-M (generated owner tables).
- Written days in courses/english-language-arts-grade-3/ where a plan claim needed checking (d007, d040 to d051, d123, d154 and the texts folder).
- data/progressions/ela.csv rows for e2, e3 and e4; the grade 2 unit 4 plan; the grade 4 unit 1 plan.
- docs/reviews/lead-list-lens-pass-2026-11-17.md, items for sections s01 to s04.

## Verdict

The four units make a sound year: the arc runs from routines and story response (unit 1) through research and the first published piece (unit 2), opinion and reports (unit 3), to two-text comparison and the year-end spoken product (unit 4), and grade 2 hands on and grade 4 picks up every row cleanly. The real faults were bookkeeping in field 5: owner placeholders on every row and rows that had drifted from items.csv, which meant the plan's end-of-unit table did not describe the checks the days actually give. Unit 4's paired water text was still listed as a federal page when the written text is our own original, a rights and identity mismatch now fixed in the plan. Three teaching gaps sit in the written days and are logged as day faults.

## Findings

| # | Severity | Finding | Outcome |
|---|---|---|---|
| 1 | High | Field 5 Owner column was a placeholder ("section 1.1", "section 2.1", "to write with section") in all four plans. | Fixed: owners now match the section plans' generated owner tables (the section that taught the code last); rows those tables do not cover keep the day's section. |
| 2 | High | Field 5 rows drifted from items.csv in s02 (days 46, 51, 60, 71, 75, 76), s03 (115) and s04 (145); day 51 reused day 46's "cautious" item. | Fixed: rows rewritten to match items.csv. |
| 3 | High | s04 listed g3-u4-03 as "How Water Treatment Works", federal public domain; the written text is "How a Town Cleans Its Water", a Curio Class 2026 original whose facts follow the federal page. Day 154 page B quotes the federal page. | Fixed in field 10 and field 2 (days listed, browser check named for P154B). Shared-file parts for the structure pass. |
| 4 | Medium | s02 recording schedule said finals on 43 to 50; days.csv and the written days hold windows on 40, 42, 44, 47, 49 and 50. | Fixed: field 5 row, schedule paragraph and table rewritten; field 8 recording days corrected. |
| 5 | Medium | s04 field 4 day 123 retrieval cited earlier course use on 98; days.csv puts e2-compare-texts on 93. | Fixed in plan. Day fault: d123 has no compare-texts retrieval task. |
| 6 | Medium | Unit 2: L.3.5a to c and RL.3.4 are taught only on day 40 and checked on 46, with no practice between. | Day fault. |
| 7 | Medium | Unit 2: recording clips scored on 51 with only an oral replay comment; no written feedback or revision chance first. | Day fault (plan row now states the rule). |
| 8 | Low | s01 pacing line did not say day 7 retrieves the grade 2 care family and dictionary forms, as d007 does. | Fixed. |
| 9 | Low | s02 field 2 did not say L.3.4a to d and L.3.2g were taught in unit 1 and only checked here; field 3 did not date the last use of unit 1 charts. | Fixed. |
| 10 | Low | s02 field 8 "Tools: None" while the days use a recorder, a shared keyboard and a keyword search. | Fixed: tools named with their jobs and the local, teacher-selected page rule. |
| 11 | Low | s02 field 10 did not record that Gutenberg 27175 failed and the classic-literature.net transcription was used. | Fixed; browser check noted. |
| 12 | Low | s04 lacked: response counted once (field 7), where continued parts were taught (field 2), weak RI.3.3 and RI.3.8 handoffs (field 3), a water safety line (field 8). | Fixed. |
| 13 | Low | s04 field 10 rows for g3-u4-01, 02 and 05 still said "to write". | Fixed: written. |
| 14 | Low | days.csv skill and note gaps, ela-texts.csv titles and author, wrongs.csv letter, unit_skeleton.py false "order conflict", handback gaps. | For the structure pass (below). |
| 15 | None | Arc and continuity: grade 2 unit 4 hands on cleanly; grade 4 unit 1 retrieves all grade 3 rows; writing balance informative 10 (plus 1 recording), narrative 10, opinion 9; field 7 error groups complete. | No change: sound. |

Outcome counts: fixed 13, day fault 3 (findings 5 to 7; finding 5 also fixed in plan), for the structure pass 1 group (14 items below), no change 1.

Word counts after fixes (cap 2,300): s01 1,763; s02 1,877; s03 1,800; s04 1,872.

## Day faults

- Unit 2, day 44 or 45: add a skills-block reread practising L.3.5a to c and RL.3.4 before the day 46 check.
- Unit 2, days 40 to 50: add a written note on each child's clip card and a reread chance in a later window before the day 51 score.
- Day 123: add the e2-compare-texts retrieval task (compare main points in two short sidebars, matched rows if missed), as field 4 states.

## For the structure pass

- days.csv:
  - day 30: add SL.3.5 and RF.3.4a to c;
  - days 2 and 3: kind Understanding to Check or Application (judgment call);
  - day 28 goal: "Check reading of the Washington panel; practise an explanatory paragraph";
  - day 7 note: say care, careful and careless are retrieval;
  - add RF.3.3a to 45, RL.3.3 to 47, RI.3.2 and RI.3.7 to 56, L.3.1b and L.3.1c to 58, 59, 64 and 73;
  - days 66 to 74 product note: the essay body is days 69 and 70; day 71 is a separate paragraph;
  - day 51: drop g3-u2-02;
  - add RL.3.2 to 99; RF.3.3d, L.3.2e, L.3.2f, W.3.10 and W.3.4 to 106; L.3.2c to 113;
  - day 107: drop SL.3.4, SL.3.6 and L.3.3b;
  - add SL.3.1a to d, SL.3.2 and SL.3.3 to 149; SL.3.4, SL.3.6, L.3.3b and W.3.6 to 151;
  - day 134 goal: "town water-cleaning text", not "water-agency explanation".
- ela-texts.csv: g3-u4-03 title "How a Town Cleans Its Water", author Curio Class (not the federal agency); g3-u2-05 title (one myth and one fable, not "Short myths"); g3-u2-07 title (the glass frog only, not "three unusual frogs"). This also regenerates the s04 field 10 skel rows.
- wrongs.csv: s02-A43 error "x" is not a register letter; set it to the intended letter.
- scripts/unit_skeleton.py: prints "order conflict" for any non-empty order_conflict column; this course's column holds "Source order kept" prose, so every row reads as a conflict. Treat that value as no conflict.
- handbacks.csv: exits with no hand-back: s01-X39, s03-X119, s04-X124, s04-X152, s04-X154 (minor).
- Section plans u04-5 and u04-6 quote the old text name "How Water Treatment Works".
- s04 field 3 generated table lists e2-compare-texts last day 98; days.csv has it on 93. Check the generator.

## Lead-list items worked

From docs/reviews/lead-list-lens-pass-2026-11-17.md, sections s01 to s04:

- Fixed: 11 (s01 day 7 pacing; s02 L.3.4 and L.3.2g carry, tools line, chart last use, Gutenberg note, recording windows; s04 response counting, continued parts, weak handoffs, safety line, g3-u4-03 row).
- Settled, no change: 5 (unit 4 wordlist has 73 rows; source-map titles present; cap items moot under the raised caps; s02 fixed wording, texts now written; s04 day 154 goal adequate).
- Open, for the lead (browser checks and sources, not plan text): 8 (name the sensitivity sources; browser checks for the caption, the Babbitt tale, the National Park Service page, Gutenberg 27175, the Ovid edition, the read.gov Aesop title page and the CDC page; a drama safety source and an elementary science safety guide; the Oz transcription source; text 04 facts sources and a cited source for the Peter Pan concern; P154A and P154B complexity checks; a free public copy of Population Growth; the independent reading set).

## Gate results

- unitplan.py check english-language-arts-grade-3: 39 PASS, 0 FAIL (s01 to s04 and all section plans).
- sequence.py check english-language-arts-grade-3: 0 failures; 11 notes (standard stems such as RF.3.4 or W.3.2 on no day in a unit, carried by their lettered parts).
- goalmap.py audit english-language-arts-grade-3: reading aid, exit 0; read for exit and practice drift against goal verbs, no drift beyond the findings above.

## For Cory

- None of scope, money or people. One audience note: unit 4 now rests on our own water-cleaning text, with one federal page quoted on day 154; that keeps rights simple but means the facts check is ours to stand behind.
