# Answer-key read: algebra-ii unit 1, section 1.1 (days 1 to 5), 2026-11-18

## What I studied

Nothing outside (answer-key kind). The study step is to solve. Before opening any key I solved cold, with my own
method, every item day 1 to 5 uses: s01-R1 to R3, X1 to X5, P3-1 to P3-6, P4-1 to P4-6 and W5. I then compared
each with the key and checked every wrongs.csv row by recomputing its shown answer and its register letter. I
also solved the worked examples and exits in docs/courses/algebra-ii/u01-1.md and u01-2.md (E6 to E10, item 4,
days 6 to 10), and checked the pieces in courses/algebra-ii/u01-1/ against items.csv. Rule 4 was checked by
listing every taught example's numbers (days 1 to 5, and 6 to 10 for u01-2) against every exit and check.

My cold answers matched the key on every number: R1 5; R2 linear 26, exponential 40.5; R3 2.5; X1 35 from chain 3;
X2 1500; X3 10/3 and 29; X4 80, 64, 51.2 with (3, 48) wrong; X5 38; P3 29, 162, 4, 40, 16, 13; P4 33, 250, 16, 3,
29, 567. All 35 wrong answers recompute as shown and carry one fitting letter (x rows are marked as having none).
The problems are in what the key covers, its domain, plan copies that went stale, and rule 4.

## Verdict

Pass with fixes. The arithmetic is right throughout, but the day 5 written task has a key for one of its four cards,
the day 5 exit key allows a bus to carry negative riders, and the section plan still holds an older day 2 exit.

## Findings

1. [s01-W5, data/plans/algebra-ii/items.csv] The key answers Card C only, but each pair takes any of situation cards A to D (Card D has two seeds, a different shape), so a teacher cannot mark three of four cards. | Make the answer cover A to D: A p(0) = 60, p(n) = p(n-1) - 5 for integers n from 1 through 12; B (after finding 3) g(0) = 4, g(n) = 3 g(n-1) for integers n at least 1; C as now; D t(1) = 3, t(2) = 4, t(n) = t(n-1) + t(n-2) for integers n at least 3; then the sentence. | origin=unit
2. [s01-X5, items.csv; E5 in u01-1.md] "v(n) = v(n-1) - 8 for integers n at least 1" gives v(9) = -2 riders, and 8 riders cannot get off when 6 remain after stop 8. The key teaches a domain the story does not allow, on the day whose goal is the domain. | Domain "integers n from 1 through 8" with the reason (v(8) = 6); fix the answer, steps and first sample in items.csv and the E5 answer in the plan. | origin=unit
3. [E2 in u01-1.md; "If S(3) = 135" in opener.md] The plan's exit is 5 squares tripling (answer 135, wrongs 14 and 45), but the item sheets use 12 squares times 5 (1500, wrongs 27 and 300). A teacher reading the plan or opener marks the wrong key. | Rewrite E2 in the plan to the item's numbers and wrongs; change the opener's illustration to the taught L(3) = 8. | origin=unit
4. [Card B, situation-cards.md] "3 plants in week 0, twice as many each week" is the day 2 taught pattern (3 squares at stage 0 that doubles, P(n) = 3(2)^n), so the day 5 written task can be answered from memory (rule 4). | Change to 4 plants in week 0 and three times as many each week (key in finding 1). | origin=unit
5. [E6 in u01-2.md] The exit table 2, 10, 50, 250 is exactly day 4's Rule Card 2 (start 2, times 5), so students may recall the answer without reading the recurrence. | Use s(0) = 4 and s(n) = 3 s(n-1); table printed 4, 12, 36, 100; the entry 100 should be 108, point (3, 108); wrongs: the entry 36 should be 20 since the pattern adds 8 (B); plotted at (4, 108) (C). | origin=section
6. [s01-P4-5 and P4-6, rule-cards.md Cards 5 and 6] "The first term is 9" with a table from n = 0: elsewhere "first" is the first index (chain 1, row 1), so a student can put 9 at n = 1 and shift every point, which the key (9, 13, ..., at n = 0) marks wrong. | Say "The term at n = 0 is 9" and "The term at n = 0 is 7" in the item stems and the cards. | origin=unit
7. [E3 in u01-1.md] The plan says "Table Q gives 47, 41, 35" but the item shows Q as the dots of a graph, so the plan misses that this exit checks a graph. | Use the item's wording: "The dots of graph Q are (0, 47), (1, 41) and (2, 35)." | origin=section

Count by origin: day 0, section 2, unit 5, scope 0, frame 0, template 0.

## Could not settle

Nothing that changes what a grade teaches. Finding 2 sets the bus domain by the story (8 stops); a teacher who
accepts "n at least 1" still sees the three look-fors met.

## Fix

1. Fixed: s01-W5 answer now covers cards A to D (items.csv).
2. Fixed: s01-X5 answer, steps and sample use integers n from 1 through 8; E5 in u01-1.md matches.
3. Fixed: E2 in u01-1.md rewritten to 12(5)^n with wrongs 27 and 300; opener.md illustration is now L(3) = 8.
4. Fixed: situation card B is 4 plants, three times as many each week (situation-cards.md).
5. Fixed: E6 in u01-2.md is s(0) = 4, times 3, table 4, 12, 36, 100, corrected point (3, 108).
6. Fixed: s01-P4-5 and P4-6 stems and rule-cards.md say "The term at n = 0 is ...".
7. Fixed: E3 in u01-1.md now names the dots of graph Q.

Gate: `plan.py check` shows 40 FAIL lines before and after, identical; the algebra-ii lines are the three known units.csv lines plus days 6 to 14 exit and source-map items outside this read.

Count: fixed 7, rejected 0, open 0; origin unit 5, section 2.
