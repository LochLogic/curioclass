# Ladder sample, science-grade-3, set b (re-sample, 2026-11-22)

Reader: a fresh reader, read-only. Days: d020, d043, d067, d091, d113. Each day was read cold with the day before it, its section plan block, DEFAULTS.md, its days.csv, items.csv and wrongs.csv rows, the unit's errors.csv rows and the shared pieces its leans_on names.

Gates (filtered, as allowed): lesson.py check shows 0 failures on all five days. plan.py check shows 21 FAIL lines for science-grade-3, every one "section N.N (science-grade-3-uNN-N) is not in data/units.csv" (one per section plan, none about these days); sequence line 0 failures.

## Days read

| Day | File | Kind | Verdict |
|---|---|---|---|
| 20 | courses/science-grade-3/u02-1/d020.md | Application | Runs in 45 minutes and the investigation is sound, but both exit items replay the day's own two trials, so the exit shows recall, not transfer. |
| 43 | courses/science-grade-3/u03-2/d043.md | Understanding | Clear, well paced, keys hold; one definition (likeness) does not fit the seedling sort that uses it. |
| 67 | courses/science-grade-3/u04-2/d067.md | Understanding | Teachable and keys hold; "mate" and "chick" are never glossed, a card leaks the exit idea, and the exit measures only one of the day's goals. |
| 91 | courses/science-grade-3/u05-2/d091.md | Application | Printed vine goal card contradicts the key (tokens sit inside the goal line); exit repeats the practice shape. |
| 113 | courses/science-grade-3/u06-4/d113.md | Fluency | Sound content and clean hand-offs; the 10-minute wall turn has zero slack for 30 children. |

## Checked by hand

- Day 20: both exit keys reworked. X20 (turning one of two pulling magnets puts like ends, red to red, face to face) is correct. X20b (steel still pulled toward either end of a flipped magnet) is correct for a steel screw. P20-2, P20-3, P20-4 and P20-5 keys agree with the unit plan. Timing sums to 45. Investigate: six two-magnet tries at about 40 seconds (4 minutes) plus ten end-near-clip holds at about 20 seconds (3.3 minutes) plus writing fits 12 minutes. Judged only (no source needed): induced pull on steel by either pole.
- Day 43: X43, X43b and K, P keys reworked (goat card: long ears and brown nose alike, patches none, one and two vary; kitten card: pointed ears inherited, white paws the variation). All hold. No real-world number or species fact is claimed. Timing sums to 45.
- Day 67: all arithmetic keys (9 against 3 leaves; 10 of 12; 9 of 12 nests; 11 of 15 pairs) hold. Shelf sort key agrees with the six statement cards. Fact "a real study of house finches also found females preferring brighter males" rests on sources.csv G27 (International Ornithological Congress proceedings paper, url given, status "checked: 2026-11-19", not 2026-11-22). I did not reopen it; I could only judge the fact (it matches the well-known female-choice finding). Timing sums to 45.
- Day 91: vine case, exit X91 (strips: 4 tokens, 8 plants, 6 visits against goals 7 and 5 and limit 5 tokens: met; whole patch: 6 tokens, breaks the token limit and the no-whole-patch limit: not met), P91-1 and product S (side pool meets 7 of 10 wet plants, 5 egg clusters, 6 tokens, path dry; ditch plug 5 tokens, 8, 6, path floods) all reworked. X91, P91-2 and P91-3 keys are right. P91-1 key conflicts with the printed vine goal card (finding 1). Timing sums to 45.
- Day 113: X113 (one July of 11 hot days against a 30-year range of 3 to 9: not a change of climate) and X113b (7 to 2 scorched benches for 5 tokens, limit 6: met; model only) hold. Timing sums to 45 on paper, but see finding 2.

## Findings, most serious first

| Day | Severity | Kind | What is wrong | The exact fix | Stage that made it | Script gate would catch |
|---|---|---|---|---|---|---|
| 91 | FIRM | key | vine-case-91.md prints the goal as "at least 4 of 8 shrubs show again, and 5 bird visits, within 6 tokens", with the limit only "the soil stays whole". The P91-1 key (and the trial table columns "Goal met? Limit met?") marks "Dig out all roots" as goal met (8 shrubs, 9 visits) and limit missed. By the printed card, 9 tokens is outside "within 6 tokens", so the goal is missed, and a child who reads the card right gets the key "wrong". It also contradicts days 88 to 90, X91 and product S, where tokens are a limit. | In vine-case-91.md write "Goal: at least 4 of 8 shrubs show again and 5 bird visits. Limits: within 6 tokens; the soil stays whole." Change the teacher line to "meets both counts and both limits". Keep the P91-1 key as it is. | section plan / kit piece | no |
| 113 | FIRM | timing | "Thirty children at 20 seconds each fill the 10 minutes": 30 x 20 s = 10 minutes exactly, with no walking, no hand-over and no card to find. With the 2-minute anchor and the 4-minute read-back the part cannot stay in 23 minutes. | Place cards in three waves of ten at the wall (10 children x 20 s = 3.5 minutes a wave) with the other two waves writing P113-4, or cut to 15 seconds a child and say "place without a word" is allowed. Leave 1 minute of slack. | day (copied from section plan 10 minutes) | no |
| 20 | FIRM | rule4 | Both exit items replay the day's own two trials. X20 is "two magnets pull, one is turned, which ends face when they push apart", the class's P20-2 / P20-5 result (red faces red pushes apart). X20b is a steel screw near a flipped magnet, the day's steel check (P20-3) with the screw in place of the clip. Neither asks for a transfer (DEFAULTS: "a new case that needs the day's idea, not the worked example"), so a child who watched the lesson can answer without thinking. | Make X20 a new case: for example a magnet hung from a bar between two other magnets, red end outward, one side pulls, ask what the other side shows and why. Make X20b a non-magnet or a brass key near a flipped magnet, so steel against "any metal" (error B, day 21) is not pre-taught but the either-end idea must be applied. Redraw card 1 and card 2 in cards-exits-17-22.md. | section plan (E20a, E20b) | no |
| 91 | SOFT | rule4 | X91 is the practice shape again: two responses, goals, limits and tokens, "which has merit" (P91-1). Only the story (mice and seed plants) and the numbers changed. The shape rule is broken. | Change the shape: give one response with a count, a token cost and a broken limit, and ask "what would you change so it has merit". | section plan | no |
| 43 | SOFT | content | The chart defines likeness as "a trait the young share with their parents". P43-5 and the 8-minute sort then mark the seedlings' "leaf shape" as L, but the day says the picture names no parents. A child who follows the definition cannot mark L. The teacher's patch ("like the kind") is spoken, not on the chart. | Define likeness as "a trait young of one kind share (with named parents when a record names them)", or key P43-5 as "like the kind" and do not letter it L. Edit resemblance-chart.md and the items row. | section plan | no |
| 67 | SOFT | words | "mate" and "chick" are first taught here (ledger) but no step in the day glosses them. The shelf "find a mate" and the exit rest on mate. Grade 3 readers may not have it. | Add one spoken line in the 10-minute block: "A mate is the partner a bird picks to have young with. A chick is a young bird." Add both to the printed shelf headers' help line. | section plan / day | no |
| 67 | SOFT | key-on-child-page | The chick card (held by pairs) says "This is a separate record from the choices." That is the idea X67 and X67b test (a pair record is not a young record), so the card hands over the exit key. | Cut the second sentence from shrub-finch-cards.md. Keep it in the teacher notes. | kit piece | no |
| 67 | SOFT | exit-goal | The goal is to compare thorn evidence and a mate-choice case. X67 and X67b ask only whether pair counts show young (lizards, a case with the same split as finch pairs against the chick card). The thorn half and the hawk cost are not measured. | Keep X67b as the spoken item; make X67 a one-line compare: "Thorns kept 3 leaves, clipped lost 9. What does it show, and what does it not show?" | section plan | no |
| 67 | SOFT | content | Statement card 6, "Females chose by looking at the males", is an inference, not a record: no card states it. Sorting it as a find-a-mate record teaches that an explanation counts as a record, against the day's point. | Replace it with a record such as "Females chose the bright male at the same table at 3 of 4 visits (invented)", or delete the card and the sort becomes five cards. | section plan | no |
| 67 | SOFT | source | sources.csv G27 (house finch female choice) is "checked: 2026-11-19". The standard is 2026-11-22 and the fact is stated aloud to children. | Reopen the url, record `checked: 2026-11-22`. If it will not open, keep the fact with status "browser check". | data | yes (date) |
| 20 | SOFT | timing | Exit is 3 minutes: read two cards aloud, write alone, then 3 to 4 children answer aloud. About 4 minutes of work. Class table, 5 minutes, holds 4 minutes of hearing six children plus posting and the Ask. | Take 1 minute from Revise arrows (5 to 4) for the exit, or hear only 2 children aloud. | day | no |
| 43 | SOFT | timing | Exit is 3 minutes: card read twice, write alone, kneel by two children (1 minute), then 3 to 4 aloud (X43b). About 4 minutes. | Merge the kneeling answers into the aloud answers (kneel only at the written answers), or take 1 minute from the 5-minute chart revision. | day | no |
| 43 | SOFT | rule4 | X43 (kittens: pointed ears alike, white paws different, "use trait and inherited") has the shape of P43-2 and the chart frame "alike in ___; different in ___" on the goat card. Only the animal changed. | Use a case where the likeness is among the young but the parents' trait is hidden, so "inherited" needs the record, or ask the child to write one question a family record would answer. | section plan | no |
| 43 | SOFT | ladder | Variation within a kind was taught in grade 1 as "young are not exact copies" and "variation among young and among adults" (ledger u03-1 day 25). Day 43 teaches "variation" as a new word without naming grade 1's idea. | In the 12-minute block say: "In grade 1 you said young are not exact copies. The word for that is variation." | section plan | no |
| 20 | SOFT | other | turn-table.md has "Our gap (whole cm): ____" but the day says 4 cm for every group. | Print "Gap: 4 cm" on the turn table or write "the group's chosen gap" in the day. | kit piece | no |
| 20 | SOFT | other | The ledger rows for day 20's exit still say "a steel bolt on a tray leaning toward a magnet red end, then the blue end" (the old exit). The exit has since changed. | Rerun ledger entry for d020 after the exit fix. | data | no |
| 91 | SOFT | other | The student page prints its own two-row table with Shrubs and Visits columns while trial-table.md (leans_on, printed per pair) has a single "Count" column. Two tables for one job. | Drop trial-table.md from d091's print and leans_on, or use it with two count columns. | kit piece | yes (print list against student page) |
| 91 | SOFT | other | Feedback load: "3 minutes a child after class", six look-fors for 30 children is 90 minutes for a teacher with no prep time. | Mark with a three-line tick sheet (supported, not yet, one question) and write the question for the weakest ten only. | section plan | no |
| 113 | SOFT | other | The safety line says clean-up is 3 minutes; the day's Clean-up part is 2 minutes (the unit plan has 3 with a shorter consensus part). | Make the safety line say 2 minutes. | day | no |
| 113 | SOFT | other | The P113-3 sample answer uses Birch Flat, which the class first meets on day 114. It is not "a record the class has seen". | Use Manaus or the class's own town card from day 104. | data | no |
| 113 | SOFT | rule4 | X113 is the same case as day 103 and 104 (one year against the many-year range), new place and numbers only. The anchor sentence spoken in the day is the answer. | Use two places with different ranges and ask which one this month would be unusual for. | section plan | no |
| 113 | SOFT | other | Product H revision depends on six written notes per child written after day 112, about the same load as day 91. | Same fix as day 91: tick sheet plus short notes for the ten weakest. | section plan | no |
| 113 | TEMPLATE | other | The Fluency kind text says "no writing is drafted, revised or edited", but a day whose goal is "revise the consensus model" and whose product H part revises written work cannot honor it. The plan chose revision on purpose. | Allow "revise a model or a product the child already wrote" in the Fluency kind for science review days, or change the kind to Application. | kit (template) | no |

## Ladder

The grade gap caused one repeated problem: **words that come back in a later grade with a new name for an old idea**. Day 43 teaches "variation" (grade 1: "young are not exact copies"; "variation among young" in the ledger) as if new, without naming the grade 1 idea; day 67 teaches "mate" and "chick" without a gloss, though grade 1 and K have no entries for them. Everything else lines up: the grade names its reviews in the ledger's words (day 43 "review of grade 1", day 90 "you met this in kindergarten: sunlight warms water"), and review claims I checked hold in the day written (day 20 "red end / blue end" from day 17, day 91 "merit" from days 87 to 90, day 113 "range over many years" from day 103). No day assumes something no lower grade or earlier unit taught: day 20 uses "toward and away" for what day 17 calls "attract and repel" and does not use the term attract or repel itself, which is consistent. No exit reuses a lower-grade case. The grade used lower grades well.

## Counts

| Day | FIRM | SOFT | TEMPLATE |
|---|---|---|---|
| 20 | 1 | 3 | 0 |
| 43 | 0 | 4 | 0 |
| 67 | 0 | 5 | 0 |
| 91 | 1 | 3 | 0 |
| 113 | 1 | 4 | 1 |
| All | 3 | 19 | 1 |

(The plan.py FAIL lines "section not in data/units.csv", 21 for the course, are a data gap in units.csv, not counted above.)

## Browser check

None.

## Fixes applied (2026-11-22)

Cleanup agent, grade close.

FIRM findings
- Day 91 key: applied. vine-case-91.md now reads "Goal: at least 4 of 8 shrubs show again and 5 bird visits. Limits: within 6 tokens; the soil stays whole." and the day's goal line and the pair text match; the P91-1 key was right and is unchanged.
- Day 113 timing: applied. The wall turn is three waves of ten at 15 seconds a child, the other waves start P113-4 at their desks, with 1 minute of slack.
- Day 20 rule 4: applied. X20 is now a new case (a hung magnet's red end pulled to a held magnet: which end is close); X20b is a claim to judge (a steel nail, "the blue end will push it away"). No brass case, since day 21 teaches it. Cards, day, plan and days.csv synced.

SOFT findings
- Day 91: rule 4 (X91 shape), the second table (trial-table), and the feedback load left.
- Day 43: likeness definition fixed in the resemblance chart (applied); exit timing, rule 4 and the grade 1 variation line left.
- Day 67: "mate" and "chick" glossed (applied); the chick card line cut (applied); statement card 6 replaced by a record (applied, items row synced); exit-goal left; G27 reopened, the page states the preference, status now "checked: 2026-11-22" (applied).
- Day 20: turn table prints "Gap: 4 cm" (applied); exit timing left; the ledger rows for the d020 exit need a rerun by the lead.
- Day 113: clean-up said as 2 minutes (applied); P113-3 sample uses Manaus (applied); X113 rule 4 and the product H note load left.
- Template point (day 113, Fluency kind text against a revision day): left, a template matter for the lead.

Key-line results: see the set a report; no key lines in the days of this set beyond those listed there.

Gates: see the set a report (same course run). plan.py 118 before and 118 after, unchanged. Browser check: none.
