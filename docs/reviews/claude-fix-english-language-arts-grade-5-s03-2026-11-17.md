# Fix: english-language-arts-grade-5 unit 3 (s03.md), 2026-11-17

Gate: `unitplan.py check english-language-arts-grade-5` prints PASS for s03.md (1,248 of 1,250 counted words).

Findings merged: 30 (assessment 15, sources 8, sequence 9; assessment 1, 2 and 8 are one fault in the C and D texts). Fixed 19. Rejected 7. Lead 6 lines. Held up per lens: assessment 15 of 15, sources 1 of 8 was valid but is not mine (LEAD), 5 held but over the word cap, sequence 6 of 9 fixed in the plan, 3 sent to LEAD.

Fixed in s03.md:
- Assessment 1, 2, 8: C3, C4, D1, D2 rewritten on a bicycle rack, a class rabbit and a pond reopening (no archive, label, access or bus idea); D2 is now a second account of the same Monday reopening; keys, 101A to C and 118A wrong answers (H, I, J) updated; letters and minutes unchanged.
- Assessment 3: one scored product per standard. W.5.2 is scored once, on day 116, from the day 115 draft; 117A to E are record only. W.5.1 is the day 110 essay as corrected on day 111; the day 119 caption is evidence for W.5.4 and RI.5.9 only. 122A to E are record only with the day 110 samples.
- Assessment 4: analytic sentences removed from A and B; dated facts kept.
- Assessment 5: 88D given its own prompt and key (letter C), silent reading stated.
- Assessment 6: day 100 exit-table task now holds the vocabulary note; 122 RI.5.4 names account 04 for however.
- Assessment 7: "Inter means between" removed from the day 94 exit; new letter AL added after AK; L.5.4b wrong answer filed under AL; response groups updated.
- Assessment 9: 122A to E set to 0 minutes; the Time paragraph says what the 25 minutes hold.
- Assessment 10: ids renamed 121A to 121D and 123A to 123D.
- Assessment 11: opinion prompt names the reader.
- Assessment 12: 116D and 117D sample uses the chosen pair's own words. 116A Meets left as it is (generic, fits any pair).
- Assessment 13: 108C sample is now a link from the introduction to the first reason.
- Assessment 14: exit 115 drops "type and save"; exit 120 prints the partner's question.
- Assessment 15: letter A reworded.
- Sequence 1: field 2 now says where L.5.1d, L.5.1e, L.5.2b, L.5.2d, W.5.2, W.5.4, W.5.6 and SL.5.1 were taught or practised (units 1 and 2, from days.csv), and that day 118's unscored planning models SL.5.4 to SL.5.6.
- Sequence 3 (plan part): day 119 no longer carries a W.5.2 correction (the day 116 record is the one score), so the load question falls away.
- Sequence 4: text set days match days.csv.
- Sequence 5 (part): "Tools: None" replaced by devices (light), practise with feedback.
- Sequence 6: the 11 "Note (days.csv)" lines deleted.
- Sequence 8: "publish on day 122" now "verify the saved final copy on day 122".
- File was CRLF; saved as LF.

REJECTED: sources 2 | Field 10 should state why 03 and 04 are written by Curio Class (renewal search not done, 2026) and name a free place to look for a real 1947 report, with 03 and 04 as fallback | The fix needs about 25 words and only 2 remain under the cap, and choosing a real-report archive is a text-set decision for the lead | the word cap (UNIT-PLAN Length)
REJECTED: sources 3 | Abbott facts rest on a personal site that was inaccessible; name a free reachable source for each fact | Needs about 30 words of new sources and page checks I cannot make here, over the cap | the word cap (UNIT-PLAN Length)
REJECTED: sources 4 | Name free pages that check each period of 01 and the claims of 06 | Needs a list of pages in field 10, over the cap; the text agent's source file is the right home | the word cap (UNIT-PLAN Length)
REJECTED: sources 5 | Court-martial facts rest on one conference slide and the Louis claim on one booklet page; name the National Archives record and mark them to confirm | Needs new sentences in field 10, over the cap | the word cap (UNIT-PLAN Length)
REJECTED: sources 6 | The sensitivity read names "a Black historian of sport such as Louis Moore or Derrick White" with no page; name one free article or drop the clause | Dropping the clause removes a sensitivity-read instruction and naming a page needs a source I have not opened, so neither is mine to do | the writer's brief (verified or none; remove nothing)
REJECTED: sources 7 | Add one line listing each text with author, year, edition and rights basis | About 45 words against 2 left under the cap; field 10 already gives author and year for each original | the word cap (UNIT-PLAN Length)
REJECTED: sequence 9 | Field 3 should say what unit 2 must have taught for W.5.6 and the day 79 exchange | About 20 words against 2 left under the cap; field 2 now names W.5.6 as practised in units 1 and 2 | the word cap (UNIT-PLAN Length)

LEAD:
- Sources 1: decide whether 02 should be a checked excerpt of Robinson's 1949 testimony (a congressional record, rights to be confirmed by the text agent on the cited hearing page) instead of our paraphrase; if yes, ela-texts.csv, days.csv notes for 97 to 99, field 10 and items 108E and 108G change, and RI.5.8 would then be analysed on his own reasoning.
- Sources 8: the "accounts of the time use the words of their time" sentence sits in a generated frame line in field 10; no account of the time is in the unit, so the frame line should be revisited by the lead or the generator.
- Sequence 2: days.csv day 94 codes lack RI.5.4, L.5.4a and L.5.4b, which the plan and day 122 rows rely on; add them or move the practice day.
- Sequence 3: days.csv day 111 lacks W.5.1 and W.5.5 (the day 111 correction of the day 110 essay), and days 119 and 120 lack W.5.1 and W.5.4 for the caption and its revision; add them.
- Sequence 7: fix unit_skeleton.py so the source-map list prints "order conflict" only when the order_conflict column is not "None".
- Sequence 1 / Sources 7: confirm in scope-and-sequence that no earlier unit taught SL.5.4 to SL.5.6 (none of units 1 and 2 cite them in days.csv); if the writer wants a longer model than day 118's planning block, days.csv must say so.
