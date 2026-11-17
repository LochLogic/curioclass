english-language-arts-grade-9 s04 fix report, 2026-11-17

Findings merged: 28 (assessment 8, sources 10, sequence 10; no fault named by two lenses). Fixed: 26 (some in part, see below). Held up per lens: assessment 8 of 8, sources 8 of 10 (S7 and S9 are lead items), sequence 10 of 10. Gate: `python -X utf8 scripts/unitplan.py check english-language-arts-grade-9` PASS for s04.md (1,248 words counted, cap 1,250; only 2 words of room remain outside fields 4, 5 and 6).

What changed, by finding:
- Assessment 1 to 8: C4 rewritten to test sufficiency (Washington's "I have spoken of my own experience" paragraph checked in library/up-from-slavery/text.md; J now producible) with the C4 look-for row and the field 7 group table (C4 no longer maps to O) matched; S2 and S3 answer-giving sentences cut; C2 now asks the student to state the central idea; E67 moved to the first-meal paragraph of The Cutting of My Long Hair; E71 and E74 rewritten with markable wrong answers and named details; P1 "does not meet" sample refits D; SL.9-10.1, L.9-10.4 and L.9-10.6 line added (scope and sequence names unit 1 day 20 for discussion and word strategies).
- Sources 1: Gutenberg ids added (10376, 2397, 73549 replacing the commercial link, 337). Every paragraph of the four library files was compared with the pg text in library/_sources and all matched, so the field says so.
- Sources 3, 5, 6, 8, 10: sensitivity edit ("[slur]" for the flag word, "paleface" as the author's own word), Washington teacher background (sources to choose), "invented for practice" label on S1 to S3, film file name, length and dramatization line, and Eastman limited to chapters read. All sit in field 5, which is uncounted.
- Sources 2: attribution marked "to confirm" with what to record (ERIC PDF was too large to fetch). Sources 4: "Day 67 present-day source: to make" in field 10.
- Sequence 1, 3, 5, 6, 9: T79 now teaches the three grade 9 speech steps first; 74 and 77 get the W.9-10.9b moves; 69 to 71 minutes stated; day 83 purpose stated; the 67 telegraph-pole paragraph is read aloud in the hook.
- Sequence 2, 4, 10: device route and P2 fallback, day 80 minute order and listener fallback, and the three-frames-only statement for RI.9-10.7 are in field 5.
- Sequence 7: "miscellany" moved to E73; "deplored" takes its place in the week 15 list.
- Sequence 8: handoff sentence corrected to six strong and four not retrieved here.

REJECTED: sources 7 | The Washington passage token count (1,874) differs from the reader's 1,919 and the passage has no ela-texts.csv row | The local file counts 1,867 words from "Finally the great day came" to "prepare my lessons", and the plan's 1,874 says it includes printed page labels, so the number is not wrong; the missing row is a LEAD, not a plan edit | none
REJECTED: sources 5 | Add Washington's passage and Hampton's page to field 10's sensitivity study list | Over the word cap (1,248 of 1,250 counted); the same content (teacher background for 82) is in field 5 instead | UNIT-PLAN "Length"
REJECTED: sequence 2, 4, 10 | Change field 8's supply and playback lines to match the P2 device route, the day 80 outside listener and the stills-only film evidence | Over the word cap for field 8, which is counted; the three statements are in field 5 and field 8 is left as it was | UNIT-PLAN "Length"

LEAD:
- ela-texts.csv row g9-u4-07 should read "Curio Class original, read aloud, ours" (invented for practice).
- ela-texts.csv has no row for Washington, Up from Slavery (1901, public domain by date, Gutenberg 2376, chapter III); the passage in library/up-from-slavery/text.md counts 1,867 words.
- ela-texts.csv rows for g9-u4-01, 03, 04, 08 can take Gutenberg 10376, 2397, 73549 and 337 as editions (library files match paragraph by paragraph).
- days.csv: no Understanding day for e9-sl-presentation (SL.9-10.4 to 9-10.6) before 81; the plan teaches the grade 9 steps in T79 only.
- days.csv: day 83 is a Check day with no new item; day 72 names a "playback cap 6 minutes" though the plan uses three stills.
- days.csv: add the "[slur]" and "paleface" teacher notes to days 67 and 68.
- days.csv or the plan for day 80: peer response is now a short swap inside the 15 minute block; confirm.
- data/plans/english-language-arts-grade-9/wordlist.csv does not exist; field 2's word table needs it (swap of "miscellany" for "deplored" belongs in it).
- source-map.csv is absent for this course.
- Answer-key and rights agents: confirm which Antin VIII paragraphs hold the passport, examination and letter (E69, T69); if the passport falls after paragraph 24, change E69 to the ticket-class and fee paragraphs.
- Present-day boarding-school source for day 67 (a tribal or tribal education page and a federal or museum page, with free links) is to make.
- ERIC ED332053 first-page title, author, year and publishing agency of the arrivals table are to confirm; the PDF exceeded the fetch limit.
- The intertitle wording at 32:00 of Deliverance is to be recorded from the file.
- Sensitivity study: a Black-led or university source for Washington's passage and Hampton's own history page are to choose.
