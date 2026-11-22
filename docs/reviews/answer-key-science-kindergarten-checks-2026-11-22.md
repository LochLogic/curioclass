# Answer-key read: science-kindergarten checks (mid-year days 29 to 31, year-end days 62 to 64)

Date: 2026-11-22. Kind: answer-key. Target: science-kindergarten-checks.

## What I studied
The study step for this kind is to solve. I solved all 57 course-level items cold (every items.csv row with an id starting c1-, since the course has no c3- rows and the c2- rows are the year-end set) from the stem alone, then opened the key, steps, samples and wrongs rows, and then the card files that give them:
- data/plans/science-kindergarten/items.csv and wrongs.csv (rows filtered by prefix): the stems, keys and wrong-answer rows.
- courses/science-kindergarten/u03-2/cards-check-mid.md and d029.md, d030.md, d031.md: forms A and B, records A and B, day 31 exit cards.
- courses/science-kindergarten/u06-2/cards-check-end.md, d062.md, d063.md, d064.md: meadow map, change cards, class chart rule, day 64 exit cards.
- data/plans/science-kindergarten/parts.csv: the standard tags for the items.

All items are teacher-judged and spoken (touch, point, say), so "solving" meant stating the answer a kindergartner should give from the cards as described.

## Verdict
Pass with fixes. All 57 keys match my cold answers on the card facts (counts, record squares, day pairs, row differences, and the forecast cards all agree between stem, card file and key), with no key error found. Six items are ambiguous or thinly cued and need small wording fixes, listed below.

## Solved and matched
c1-K1 to K5, W1 to W3, F1 to F4, P29-1, P29-2, X31a to X31d; the form B twins (c1-K1b to P30-2); c2-N1 to Nw (except N1, below), M1 to Mw, C1 to Cw, D1 to Dw, P62-1, P63-1, T62, X64a to X64d. Checked numerically: record A cloudy 2,3,5,6,9,10 is six; record B windy 2,4,5,8,9 is five; month rows 7 against 4 and 8 against 5 both leave three over; day pairs warmer, warmer, cooler (A) and cooler, warmer, cooler (B) match the W2 keys; X31b (cooler, cooler, warmer) and X64d (warmer, cooler, cooler) both have a cooler afternoon to touch.

## Findings

1. **c2-N1, item ambiguous.** Stem: "a child filling a cup ... Touch each living thing that is taking in water." Key: "The sparrow, the seedling and the child." A child filling a cup has not yet taken in water, so a fair child could leave the child out (or a careful one could argue the sparrow is only standing at a puddle). The key's own logic (all living things shown need water) is right, but the picture does not show intake. Fix: card to "a child drinking from a cup" (cards-check-end.md Water cards) and stem unchanged.

2. **c1-T1, item ambiguous (and tag).** Stem: "Did the softer push do what people want? Touch yes or no, then touch the try that did not." Results are yes, yes, no. Key: "It did mostly, two tries out of three: yes" but the steps say "touches yes for two tries and no for one", which is not one yes/no answer. Fix: stem "Did the softer push work most of the time? Touch yes or no, then touch the try that did not", and make the step "touches yes, then points to the third try". Separately the row is tagged K-2-ETS1-1 (define a problem) while the item judges a tried solution (the PS2-2 / test-and-judge skill that c1-X31d tests); consider retagging, or say it is deliberately a transfer item.

3. **c2-X64a, item ambiguous.** Stem: "A pet rabbit and a bean plant share a sunny porch ... Touch what both of them need." Key: water only. The word "sunny" cues the sunlight card, and a child who learned that living things live in sun can fairly touch it, while the course teaches light as a plant need only. Fix: drop "sunny" from the stem ("share a porch"), and add to the key that sunlight and soil are plant needs only, so they are not both.

4. **c2-M3, picture does not show what the key needs.** Key: "stream water, air, land for a food garden and trees for wood." The meadow map shows water, sun, air, soil marks and a house on the hill, but no garden or wood mark. Fix: key to "lines to water, air, soil or land, and the trees; any one place resource the map shows is accepted", or add a garden bed and a wood-pile mark to the map.

5. **c1-K1 and c1-K1b, fair alternative incomplete.** When the child picks "how hard", the fair test also keeps the push direction the same, but no keep card shows direction and the key does not ask for it. This is not wrong, only partial. Fix: add one line to the key: the direction need not be touched; the item tests that the car and lane are kept. No card change needed.

6. **c2-D3 and c2-Dw, key not tied to the chart.** The key reads "such as some afternoons warmer and some cooler" and "such as more cloudy days than rainy days", examples written before the class chart exists. The day card rule guarantees one cooler afternoon in D3, so the key can say so. Fix: D3 key "one afternoon cooler, the others as the chart shows; not always the same", and Dw "a pattern the teacher wrote from the chart before class". D1 and D2 keys are correctly deferred to the chart.

## Other checks
- Fair alternatives keyed wrong: none besides items 1 to 3. c2-N4 key (apple to the child) is the intended match from the N3 cards, though an apple could plausibly go to another animal; the preceding N3 pairing makes the intended match clear, so I leave it.
- Skill tested matches the named skill for every other item, including the count, month-compare and pattern items against K-ESS2-1, the forecast items against K-ESS3-2, and the place items against K-ESS3-1.
- wrongs.csv: each sample wrong answer is a plausible child error and none is a fair correct answer; c1-W3, c1-F2 and c1-X31d wrong rows (and the form B twins) carry no register letter by design.
- Gate (filtered): 13 FAIL lines, all "section X.Y is not in data/units.csv" for every unit; this is the same for all units of the course and is not an item defect. The sequence line reports 0 failures.

## Could not settle
Whether c1-T1 should keep the K-2-ETS1-1 tag as a deliberate transfer item or be retagged (a plan design choice for the lead).

## Fixes applied (2026-11-22)

- 1. c2-N1: applied. Stem now says "a child drinking from a cup", so the child takes in water; key, card and print updated.
- 2. c1-T1: applied. Stem "Did the softer push work most of the time?", answer, steps and samples updated. The K-2-ETS1-1 tag is left for the lead.
- 3. c2-X64a: applied. "Sunny" dropped from the stem; key says sunlight and soil are plant needs only.
- 4. c2-M3: applied. Key and steps accept any resource the map shows.
- 5. c1-K1, c1-K1b: applied. Key adds "keep the push direction the same".
- 6. c2-D3, c2-Dw: applied. Keys tied to what the class chart shows.
- Also: c1-F3, c1-F3b, c1-X31c samples, wrongs and card say "stay out until thunder" (sensitivity M1); errors.csv example matched. c1-F3 and c1-F3b still carry two asks in one stem: listed for the lead.
