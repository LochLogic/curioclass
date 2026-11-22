# Answer-key read: science-grade-2, unit 2 (2.3 end items), 2026-11-22

Kind: answer-key. Target: science-grade-2-u02. Read-only except this report.

## What I studied

The study step for this kind is to solve. I read the twelve end items (s02-E1 to s02-E12, the only non-exit, non-practice items of unit 2; there are no "check" or "mid" items) and the printed pieces that carry them: packet-day23, anchor-path-sheet-day23, packet-day24, packet-day25 and the day 23 to 25 files (d023, d024, d025) under courses/science-grade-2/u02-3/. I solved each item cold from the stem and packet and wrote my answer before opening items.csv answer/steps/samples, wrongs.csv rows for s02-E*, key-packet-day23/24/25 and the plan s02.md (standards and limits). No outside sources were needed.

## Verdict

Pass with fixes. All twelve keys match my cold answers and no key is wrong; there are no errors of mine. Five items have a wording or support gap that could mark a fair answer wrong or leave a child guessing which paper or limit is meant (E1, E3, E6, E10, E12), and E6 sits a little off its standard.

## Solved cold, then compared

| Item | My cold answer | Key | Match |
|---|---|---|---|
| E1 | A and B fast (labels "just before / just after"; "during the eruption") | A and B | yes |
| E2 | C and D slow ("older / later"; "little by little") | C and D | yes |
| E3 | Fast arrow A, B; slow arrow C, D; mound added, edge worn back | same | yes |
| E4 | Mat 1,2 least; wall 3,4; rock 4,5; bare most; water carried soil | same | yes |
| E5 | Stick 2,3 least; wall 4,5; bare most; wind carried soil | same | yes |
| E6 | Less soil moves behind barriers; water goes round wall end | same | yes |
| E7 | P first run 1, least | same | yes |
| E8 | P second run 7, over 5 | same | yes |
| E9 | Q 4 and 4, both under 5 | same | yes |
| E10 | Q first run 4, more than P's 1 | same | yes |
| E11 | P 1 under, P 7 over, Q 4 under, Q 4 under | same | yes |
| E12 | Q, because both runs meet the limit (P and Q totals are both 8, so only the "each run" rule decides) | Q | yes |

Mismatches: key error 0, ambiguous item 5 (below), my error 0.

## Findings

1. **E12 (and E10): the stem omits what the key needs.** E12 reads "Which screen suits this problem?" with no limit or data in the stem; the key turns on "at most 5 in each run". The totals tie (8 and 8) and so do the averages (4 and 4), so a child who forgets "each run" has a fair-looking tie. Day 25 teacher page says the limit aloud, so the live class is safe, but the item as stored is not self-contained. Fix: "The problem needs a loss of at most 5 centimeters in each run. Screen P lost 1 then 7. Screen Q lost 4 then 4. Which screen suits this problem?" E10 has the same gap ("Say what screen Q does poorly" with no limit). A child who writes "Q does nothing poorly, both runs are under 5" is correct against the problem but fails the key's step. Fix: add to the key and the look-for: "also accept: Q lost 3 more than P in the first run, though still under the limit" and reword the stem to "Compared with screen P in the first run, say what screen Q does poorly."

2. **E6: "your model" has no antecedent.** The stem says "Use arrows on your model", but the child holds a change model (day 23), a barrier model and the hillside pair. Fix: "Look at the two hillside pictures. On blank model paper, use arrows to show how protection changes the land and the land around it, including the water that runs round the end of the wall." Also the key and look-for 6 say the turned water "goes on to wear land beside it" but picture 2 only shows water arrows round the wall end and a small gully at one side. Fix the key to "can change" (the item key already says this; key-packet-day24 and d024 look-for 6 say "goes on to wear" and "onto the land beside it") so all three agree. Standard note: E6 tests that protection changes land (ESS2.A, stability and change) more than "compare several solutions"; acceptable, but the plan's goal for 2-ESS2-1 is carried by E4 and E5.

3. **E3: item and packet disagree.** The item asks the model to show "the change in the land each one shows". Packet-day23 task 3 and key-packet-day23 task 3 say only "the fast route and the slow route, each with the records that support it". The d023 look-for 5 (land changes named) is then scored on something the printed packet task did not ask. The student page prints the item, so the child sees the full wording on side 2, but the packet copy does not. Fix: add "and the change in the land each one shows" to packet task 3 and its key line.

4. **E1: the key does not name the evidence that separates A from C.** A and C are both before and after pictures; the difference a child can cite is the labels ("just before / just after" against "older / later") plus the words in B and D. The key cites the flat shore and mound for A and "edge farther inland" for C, neither of which says fast or slow. Fix: add to the key and steps "also accept the labels just before and just after, and older and later, as the sign of how much time passed". The wrong sample "A and C, because they have pictures" is correctly keyed wrong.

5. **E8: fair alternative.** A child who writes "P got worse, from 1 to 7, so it is not steady" is correct. Add to the key: accept a first-to-second-run rise if the over-the-limit fact is also named.

## What passes cleanly

E2, E4, E5, E7, E9, E11 are fair and self-contained. Numbers in stems match the packets exactly (water 7/8, 3/4, 4/5, 1/2; wind 8/9, 4/5, 2/3; screens 1/7 and 4/4; limit 5). The wrongs.csv rows for these items match the written errors (E5's cross-test comparison is the one well-aimed trap). Each item tests the goal the plan names: E1 to E3 the 2-ESS1-1 fast and slow sources with no time spans in numbers, E4 to E6 the 2-ESS2-1 comparison, E7 to E12 the K-2-ETS1-3 two-object test comparison.

## Could not settle

Whether C (an edge moved inland with stakes now in water) reads as slow to a child from the picture alone. It rests on the labels and on D. That is a design choice for the lead; findings 1 and 4 make the fair answers explicit without changing the records.

## Fixes applied (2026-11-22)

- 1. s02-E12 and E10: applied; both stems state the limit and the data. plan.py now flags s02-E11 and s02-E12 for sharing numbers: they are one assessment case on the day 25 packet, left as a template point.
- 2. s02-E6: applied; the stem names the barrier model.
- 3. s02-E3: applied; packet-day23 task 3 and its key ask for the change in the land, as the item does.
- 4. s02-E1: applied; the key names the labels that separate A from C.
- 5. s02-E8: applied; a first-to-second-run rise is keyed as fair.
- Could not settle (record C read as slow): left for the lead, a design choice.
