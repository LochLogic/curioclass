# Answer-key read: science-grade-3 course checks (c1-, c2-, c3-), 2026-11-22

Kind: answer-key. Target: science-grade-3-checks. Course finish, docs/COURSE-RUN.md stage 7. Read-only except this report.

## What I studied

For an answer-key read the study step is to solve. I solved each item cold from its stem and its card text before reading its key, then compared.

- data/plans/science-grade-3/items.csv, filtered to item_id starting c1-, c2- or c3-: 63 items (c1: 17, c2: 25, c3: 21). Stems first, answers and steps only after my own answer was written.
- Cards: courses/science-grade-3/u02-3/cards-check-34-35.md and cards-repair-36.md (check 1); u04-4/cards-check-79-80.md and cards-repair-81.md (check 2); u06-4/cards-check-118-119.md and cards-repair-120.md (check 3). These taught me what the picture shows for each item.
- Day files d034, d035, d036 (u02-3), d079, d080, d081 (u04-4), d118, d119, d120 (u06-4), for marking counts, item placement and the "Expect" lines. data/plans/science-grade-3/days.csv for the codes each check says it covers.
- data/plans/science-grade-3/wrongs.csv rows for the same ids, checked that each wrong answer is wrong and that its error letter and note fit.
- Gate run, filtered as the brief allows: `sequence science-grade-3: 0 failure(s)`, then `science-grade-3: 874 items and 624 wrong answers checked, 21 failure(s)`. All 21 are "section N.N (science-grade-3-uNN-N) is not in data/units.csv" (one per section, 1.1 to 6.4). None names a check item. The lines after it are notes ("error X rests on memory, not a source"), not failures.

## Verdict

Pass with fixes. Of 63 items solved cold, 55 matched the key outright (listed below); 8 carry findings (2 key defects, 4 ambiguous or under-supported, 2 more with a code label error), plus count and consistency errors in the day files. No wrong-answer row in wrongs.csv is actually right.

## Solved and matched (no finding)

c1: E34a, E34b, E34c, E34d, E34e (7 cm, my cold answer was 7 to 9, key is inside it), E35a (claim A), E35b, E35c (claim E), E35d, E35e, P36-1, P36-2, X36e (answer), P36-4.
c2: E79a, E79c, E79e, E79f, E79g, E80a, E80b, E80d, E80e, E80f, E80g, E80h, P81-1, X81e, X81f (day 134), X81g, X81h, P81-2, P81-3.
c3: E118a, b, c, d, f, g, h (60 less 30 less 18 leaves 12), i, j (A and C), k (A), l; E119a (summer 34), E119b (summer 12, autumn south), E119c (4, 12, 5, 6), E119d, E119e; P120-1, P120-2, P120-3, X120d, P120-4.

Every wrongs.csv row I read is a real wrong answer, and each error letter's note names the right misconception.

## Findings

### Key error or key defect

1. **c3-E119f (key "many rainy days").** Stem: "What weather should you expect in a Tucson summer? Use the table." Key step: "says many rainy days". The source card gives "12 rainy days" for a whole season of about 90 days, with no unit named. A child who writes "some rainy days, 12, more than other seasons" is right and would be marked not shown. Fix the step to "gives the summer rainy days, 12 (the most of the four seasons)", and add "per season" to the Tucson source card line (Source card, by season: "spring 22 degrees Celsius, 4 rainy days ..." becomes "4 rainy days in the season").
2. **c2-E79d (fair alternative keyed wrong).** Stem: "Name one trait the seedlings share with their parents." The foxglove card says "oval, soft-haired leaves". Key step: "names soft, hairy leaves". A child who writes "oval leaves" is right and not credited. Fix the step to "names oval leaves or soft, hairy leaves". (c2-E79f already accepts either trait.)

### Ambiguous or under-supported items (fix the item)

3. **c2-E79b, the hatch day.** Stem: "Eggs are laid on day 70. When will they hatch?" Key: "The egg stage on the card lasted 12 days, so ... about day 82." The grasshopper card only shows "Day 0: an egg in soil. Day 12: a young hopper." It never says the egg stage lasted 12 days; the egg may have hatched any time up to day 12. A careful child can answer "by day 82". Fix the card line to "Day 0: an egg in soil. It hatches on day 12: a young hopper with no wings", or change the step to "about day 82, or by day 82".
4. **c1-P36-3, the question and the key do not line up.** The seesaw goes up, level, down, level, up, level, so "Where is it next?" is "down". The key says "Down" but gives as the reason that "the up turns are getting a little lower", and a step requires "says the next up turn will not be exactly 36 cm". The next turn is down, not up, so no child is asked about the next up turn, and the order-repeats reason that actually gives "down" is not in the steps. Fix: key reason "the order up, level, down, level repeats, so down comes after level"; step 2 becomes "says the order repeats". Keep the shrinking up turns as an optional extra.
5. **c1-X36e, "a stuck drawer".** Stem: "Jo pushes a stuck drawer from the front. Kim pushes it from the back, about as hard. ... Does it move? Say why." A child can answer "No, because it is stuck" and be right for the wrong reason, and "about as hard" is not "equal". The key wants cancelling arrows. Fix: "a drawer that slides easily" and "Kim pushes ... exactly as hard" (or "equally hard"), matching the key's "equal pushes".
6. **c3-E119g, the table is not required.** Stem: "Can one day differ from what you expect in a Tucson summer? Use the table." Key step: "says usual not certain, one day can differ". The step never asks for table evidence, so a child who ignores the table is marked shown. Fix: add "uses the table, such as 12 rainy days in a summer, so most summer days are dry" as a second step.

### Label, count and consistency errors

7. **c1-X36f and c1-X36g are coded 3-PS2-1 but test design criteria.** They ask who needs what and for a checkable criterion, which is 3-5-ETS1-1 (day 36 lists it in codes and in skill s3-design-problem). days.csv row 36 also says "criteria = c1-X36e", but X36e is the drawer; the criteria items are X36f and X36g. Fix the code column to 3-5-ETS1-1 and the shows line to "criteria = c1-X36f c1-X36g".
8. **c2-X81g and c2-X81h are coded 3-LS1-1 (part revise) but test flock help, 3-LS2-1.** Fix the code to 3-LS2-1 and the part to match.
9. **Marking item counts in the day files.** d119 Marking says "mark the six items"; the day has seven (E119a to E119g). d080 Marking says "mark the seven items"; the day has eight (E80a to E80h, since E80h was added). Fix to "seven" and "eight".
10. **d080 "At home" Expect line.** `Why do flamingos feed together?` Expect: "Many birds stir the water and many eyes watch." Panel 2 says nothing about stirring the water, so an answer from the card would not match. Change to "Many eyes watch, so more birds can feed."
11. **days.csv row 80 "shows".** It lists c2-E80d, E80e, E80f, E80g and omits c2-E80h, which the day does give. Add E80h.

### Minor, no change needed unless you want it tight

- **c1-X36f key wording.** "need the flap to stay shut so that the seed stays dry". The stem is about wind, not rain. "So the wind cannot blow the flap open and spill the seed" fits the stem better.
- **c2-E80c.** The key says the chicks (64 to 80 cm) show the family "like their long-legged parents of about 100 cm". The chicks are shorter than their parents, as ten-week chicks would be. The stem's own line "Both zoos have long legs" is what carries the family evidence; the key reads fine if you keep to that line.
- **c2-E80f stem versus card.** The stem says the flock "walks to the other end"; the card says "the deep end". A child will map them. Consider using "deep end" in the stem.
- **c3-E118e.** "Fish bones of two kinds" and "Gar F lives nowhere now": the card never says that one of North Cut's two kinds is Gar F. The key assumes it ("Only Gar F is extinct"). Add "One kind is Gar F" to the North Cut line.
- **c1-E35d.** The key and card work, but the printed picture must show which side the second magnet is on, with red facing red in record 1, or arrow direction cannot be read. Check the printed board.

## Three worst

1. c1-P36-3 (finding 4): the stem asks for the next turn, the key marks the next up turn.
2. c2-E79b (finding 3): the hatch day depends on a number the card does not state.
3. c3-E119f (finding 1) with c2-E79d (finding 2): fair child answers keyed wrong.

## Could not settle

Nothing that changes what a grade teaches. The Tucson numbers are invented and stated as such on the cards, so no source row is needed; I checked no outside facts.

## Fixes applied (2026-11-22)

1. Applied: the c3-E119f step and answer give 12 rainy days in the season; the source card says "in the season".
2. Applied: c2-E79d accepts oval leaves or soft, hairy leaves.
3. Applied: the grasshopper card now says "It hatches on day 12".
4. Applied: the c1-P36-3 key and steps use the repeating order; shrinking up turns optional; the F wrongs row reworded.
5. Applied: c1-X36e: a drawer that slides easily, pushed exactly as hard; repair card 36 matches.
6. Applied: c3-E119g adds a table-evidence step.
7. Applied: c1-X36f and X36g are code 3-5-ETS1-1, part define; days.csv day 36 shows criteria = c1-X36f c1-X36g.
8. Applied: c2-X81g and X81h are code 3-LS2-1, part protect.
9. Applied: d119 "seven items", d080 "eight items".
10. Applied: the d080 At home Expect line.
11. Applied: days.csv day 80 shows adds c2-E80h.
Minor: the X36f answer is now about the wind; E80f says "deep end"; the North Cut card names Gar F. E80c and E35d left (fine as written; the printed board was not checked here).
