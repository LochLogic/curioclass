# Fix report: social-studies-grade-2 unit 4 (s04), 2026-11-17

Merged 25 findings (assessment 10, sequence 6 plus one lead item, sources 9). Fixed 21 (item 2 only in part), rejected 4, lead 2. Per lens, findings that held up: assessment 9 of 10 (item 2 half), sequence 3 of 6, sources 9 of 9. Gate: `python -X utf8 scripts/unitplan.py check social-studies-grade-2` PASS for s04.md (about 1,250 words, at the cap, so every fix was written short).

Notes on what changed: field 7 now marks by component and has a component-to-move table in four groups (J, L, P, Q repaired from daily exits only). New letter R added after Q; I and K narrowed to one claim each; B reworded to colour versus the key. Trade Stories B no longer prints reasons or direction. Item 6 gets Source Card D (maker and date missing). Day 48, 49, 50, 52, 53, 55 exits rewritten to fresh stimuli that touch each day's goal. Reteach lines follow the warm-up plus small group rule. Sources: blocked-site remarks removed, dates marked to confirm from a page read in full, Tennessee row replaced, African count, as-of line, image rule, Basic Law articles, community sources first, population claim removed, day 51 captions made Curio Class originals.

REJECTED: assessment 2 | Item 2 and Country Cards C should use new invented countries instead of Japan and Saudi Arabia because a remembered day 49 to 51 answer passes | Item 2 and item 2b score MA.2.T4.2 on the unit's two named countries and the contrast (elected versus hereditary) is the standard's content; swapping countries breaks the 2b link and the cap leaves no room (the service swap to a fire station and clean water was made) | none
REJECTED: sequence 3 | D2.Geo.11 is first taught inside application day 53, so model the maker, carrier, seller, user chain on day 52 | days.csv puts Geo.11 on 53 and 54 only; moving teaching to day 52 changes the skeleton and is a lead decision (listed under LEAD) | none
REJECTED: sequence 4 | MA.2.T4.1 has no return between day 48 and day 56; add returns on 53 and 55 | Field 2 already carries map keys to day 53; further returns are day-plan content, and there is no word room | none
REJECTED: sequence 5 | Day 54 is overloaded; write a core path and move the sourced-claim model to day 55 | Day budgets are left to section plans for this unit, and moving content between days is not allowed in a fix | none

LEAD:
- days.csv and scope-and-sequence: add D4.1.K-2 to days 55 and 56, D2.His.11.K-2 and D3.2.K-2 to day 51; the scope and sequence says day 55's answer is scored while the plan scores day 56; regenerate the skeleton.
- days.csv: D2.Geo.11 has no understanding day before application day 53 (sequence 3); decide whether a teaching day or note should move earlier.
