Social-studies-grade-3 s04 fix, 2026-11-17

Findings merged: 29 (assessment 12, sources 9, sequence 8; no fault was named by two lenses). Fixed 26 (three in part), rejected 3 (one more in part), lead 2. Held up per lens: assessment 10 of 12, sources 9 of 9, sequence 7 of 8. Gate: `unitplan.py check social-studies-grade-3` PASS for s04.md (the word cap needed trimming: additions in counted fields were kept short, and two sentences were placed in field 5, which is uncounted).

Notes on the fixes that were partial or judged:
- Assessment 6: E added to the day 85 exit and field 7 gets lines for exits 78 (I or P) and 85 (E). N was not added (see REJECTED).
- Assessment 8: day 77 and day 80 exits reworded as proposed. Day 80 still has no named 3c measure beyond the location passage; days.csv codes were not changed.
- Sources 1: Aquinnah ancestral-lands paragraph is now for A alone; 75 and 82 use the long-presence paragraphs; exit 87 uses the settlement paragraph alone, with homeland shading placed at the Aquinnah end of Noepe.
- Sources 5: the Grignon page has an inline transcript with no time marks, so the card now says that and gives the preceding sentence and the check date. The textbook line now reads "had wild rice in the fall, Grignon says."
- Sources 7: Kappler is named as the check text in the D record, marked not yet reached. Navajo 1868 treaty clause was deleted (sources 2), so only the 1854 treaty needed a check text.
- Sources 3 and 4: one sentence in the daily exit tickets paragraph says reserved passages are original summaries and exit maps are drawn by Curio Class.
- Sources 9: line added in field 10 naming what was not reached.
- Sequence 5: only "No sensitivity read completed." was deleted.

REJECTED: assessment 6 (part) | Add N ("two copies count as two sources") as a "Not yet" cell in the day 85 exit | The day 85 exit gives a photograph and a note that are independent by design, so no student answer to it can show N; filing a wrong answer under a letter it cannot come from corrupts the repair groups | UNIT-PLAN field 6 (a wrong answer is filed only under a letter whose text describes it)
REJECTED: assessment 7 | Day 75's exit repeats Q2 plus Q3 and day 86's exit repeats Q8, so narrow day 75 to the homeland versus present-land distinction and day 86 to picking between two supplied claims | A day exit must measure every named part of the day's goal; day 75's goal names the nations and their homelands and day 86's goal is writing a claim from named sources, and each exit uses a fresh map or source pair, as UNIT-PLAN rule 4 asks (new story, same error) | UNIT-PLAN rule 4; writer's brief (an exit measures every named part of the day's goal)
REJECTED: assessment 9 | Q4 and Q6 restate the Makah idea day 81 teaches (settle near water to boat and fish), so ask something day 81 did not teach | Day 81 teaches the permanent village of Deah and its exit is an invented bay case; Q4 and Q6 test transfer of the idea to an unseen record (C), and rule 4 bars reusing a story, not an idea; field 5 already states that no assessment camp or passage is used on 81. Q4 was still reworded to ask for the season and the activity, which also repaired the wrong-answer letters | UNIT-PLAN rule 4; writer's brief (withheld source never used on a teaching day)
REJECTED: sequence 5 | Delete "No lessons or specs seen" from field 10 and "No last-day lesson or Tomorrow line exists" from field 3 as pipeline notes | UNIT-PLAN field 10 asks what was not seen, and the field 3 sentence is a real handoff fact (the same sentence stands in units 1 to 3); only the status line "No sensitivity read completed" was a pipeline note and was deleted | UNIT-PLAN field 10

LEAD:
- Line 3 of s04.md (the comment "Skeleton from scripts/unit_skeleton.py ...") is the generator's instruction; the skeleton generator should stop printing it. It is left in place here.
- data/plans/social-studies-grade-3 source-map.csv (or sources.csv) needs rows for the Aquinnah paragraph change (long-presence for 75 and 82, ancestral lands for A only, settlement paragraph for 87), the Kappler check text for the 1854 treaty, and the removal of the Navajo 1868 treaty.
