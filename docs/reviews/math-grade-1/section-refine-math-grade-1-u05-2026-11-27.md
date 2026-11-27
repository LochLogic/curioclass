# Section refine: math-grade-1 unit 5 (u05-1 to u05-4), 2026-11-27

I ran the refine after the cold answer-key read of the same unit (docs/reviews/math-grade-1/answer-key-math-grade-1-u05-2026-11-27.md).
The skeletons were rebuilt first (`section_skeleton.py math-grade-1 u5`). Every exit, key, worked case, contrast and
retry in fields 3, 4 and 6 was solved cold, and each agrees with the plan. Each wrong answer carries one letter from
s05's register. Part minutes add to 60 on all 15 days. The exit hearing fits: six children at 40 seconds is 4
minutes after 1 or 4 private minutes. The P5 rotations fit: 15 children at 60 seconds is 15 minutes on days 108 and
109. The rotation runs 19 to 24 on day 96 through 13 to 18 at day 110 closure, and every unheard child gets the
paper back with a mark. Day kinds, owed code 1.NBT.C.4, the readiness items and P1 to P5, P5-link and F all match
the unit plan and skeletons. Every end item has its Shape line and Data id. All four plans pass the caps.

## Faults

| File | Fault | Fix or rejected | Stage |
|---|---|---|---|
| u05-2.md, day 100 | E100 asks "What does 37 plus 6 look like after a trade?", but no day teaches children the word "trade" (unit 4 taught "exchange"), and the ledger had no term row | Day 100 Model now says "trade" for the move (ten loose ones go, one stick comes, the same amount, like unit 4's exchange). Ledger term row added | write |
| u05-1.md, day 96 | Day 96 teaches "number sentence", and exits 98, 106 and 107 ask for number sentences, but there was no ledger term row | Ledger term row added; plan text already fine | write |
| u05-3.md, day 105 | E105's slip labels a path "Add on", and the teacher reads that a child "adds in parts", but day 105 never names adding on for children | Day 105 Model now says "add on" for starting with all of 75. Ledger term row added | write |
| u05-3.md, day 107 | "the comparison record": the course term "comparison" (unit 4) means a signed statement such as 54 > 42 | Now "the check record" | write |
| u05-2.md, field 3 E102a | "Show a 45 start card"; item and slip show a start picture (from the key read) | Now "a 45 start picture" | write |
| u05-4.md, F | F asks for a "new count label"; the plan reviews label checking, but the section had no review row for "label" | Ledger review row added (planned only) | write |
| u05-3.md, E107 | Ends at 100, like the day 107 practice endpoint 64 + 36 = 100 | Rejected: the day's goal is the endpoint, and the given numbers 85 and 15 are new | write |
| u05-4.md, E109 | Books context, like the day 109 cart practice | Rejected: new numbers and layout, the plan keeps the shelf layout off the cart cards, and an application day keeps its context | write |
| u05-1.md, day 96 retrieval | 42 as four tens and two ones also appears in unit 4 day 79 practice | Rejected: a retrieval task, and rule 4 binds exits and assessment items | write |
| u05-3.md, E105 | The teacher reads "like units" aloud | Rejected: day 97's Like-unit pairs teaches it with pieces, and a ledger term row exists | write |

Ledger rows added (one `ledger.py add` call each, day blank): u05-1 term "number sentence" (student word), u05-2
term "trade" (student word, builds on u04-5 exchange, planned only), u05-3 term "add on" (student word), u05-4
term "label" (review of u01-2, planned only). The writer's other rows (terms, models, routines and the reserved
exit and end cases of all four sections) match the plans. No lower-grade row cited without "planned only" while
still planned.

Gates: `unitplan.py check math-grade-1` passes u05-1 to u05-4. `ledger.py check math` reports 7692 rows, 0
problems. `gate.py --course math-grade-1` reports 0 new failing findings against the baseline. The plans have no em
dash and no TODO(writer).

## Plan points

- s05.md field U3 still lists retired exits: day 96 (62 + __ = 65 and 34 + __ = 84), 97 (31 + 26), 98 (42 + 15),
  101 (69 + 4) and 104 (39 + 25). Plans, items.csv and the ledger hold 53 + 3 and 34 + 50, 22 + 44, 62 + 34, 39 + 9
  and 29 + 57. U6 day 96 gives 25 practice minutes, while the plan has 22 with an 8-minute exit. Refresh the unit
  plan from data.
- P1 (54 + 3) and P4 (23 + 34) both total 57. u05-4 tells the teacher to judge each addend's tens and ones, so I
  kept it. A later revision could give P4 a different total.
- The key piece builder joins the Shown and Not yet seen samples with a period after text that already ends in one.
  I fixed the 25 entries by hand; the script (the lead's) will bring the fault back on a rebuild.
- The ledger case row "E109 Mina's two shelves" names a child the stem no longer names (its note says unnamed). A
  rows-only fix belongs to the lead.

## Changed for the next unit

- Any word an exit stem leans on gets a line on or before that day that teaches it, plus a ledger term row. This
  pass added "number sentence" (day 96), "trade" (day 100), "add on" (day 105) and a review row for "label".
  Later units review them in the same words.
- Key pieces print one period between the Shown and Not yet seen samples. A wrongs note gives the reason only, never
  the shown answer or the letter again.
- When a teacher note says to cover the start group, the slip draws the added pieces outside the start frame.
- "Comparison" means a signed statement (unit 4). Call a record used for checking a "check record".
- Cases now used up: 65 + 12 = 77 (day 99 retry, days 107 and 109 practice), 65 + 26 = 91, 44 + 8 (days 102 and
  110), and 100 as ten tens (64 + 36, 85 + 15).
