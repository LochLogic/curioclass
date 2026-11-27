# Answer-key read: math-grade-1 unit 5 (days 96 to 110), 2026-11-27

Kind `answer-key` (docs/pipeline/briefs/sensitivity-read.md sections 1 and 2). Fresh reader: I did not write this data.
Packet: build/sections/packets/math-grade-1-u05.md, cut 2026-11-27 08:59:55.

## What I studied

Nothing outside: the study step is to solve. I printed the 25 stems alone (helper in
_scratch/sections/math-grade-1-u05-key/), opened only the child slips the stems point to (readiness.md, exit-96 to
exit-109, addition-record.md, fresh-transfer.md) and solved each one before opening items.csv answers, samples,
look-fors or any key piece.

## Items read: 25

2 readiness (R96a, R96b), 16 exits (X96a to X109, with X96a/b and X102a/b as split pairs), 7 end items (AP1 to AP5,
AP5-link, AF). My cold answers: 10 and 6; 42; 56; 84; 66; 96; 68; 43; 48; No (49); Yes (50); 81; 86; 74 both ways;
13 ones make the seventh ten, 73; 100; 72; 67 books; 57; 56; 53; 57; 83; a link from the circled ten to 70 + 13;
75 squares. Every key agrees with mine. All 41 wrongs rows recompute to their shown value and carry one letter from
the unit's register (A to E), each fitting the error it names.

## Faults

| Item | Kind | What was wrong | Fix | Stage |
|---|---|---|---|---|
| s05-AP1 to s05-AP5 | key | The five first wrongs notes repeated the shown answer and the letter ("Counts five strips as five singles, obtaining 12 (D)."), so key-assessment.md printed "12 (D). ... 12 (D)." | Rewrote the five notes as the reason only and rebuilt the five lines in u05-4/key-assessment.md | data |
| all 25 items | key (print) | Every teacher key entry printed ".." between the Shown and Not yet seen samples | Removed the extra period in 25 entries across six key pieces of u05-1 to u05-4 | data |
| s05-X102a, s05-X102b | ambiguous (picture) | The 45 start frame on exit-102.md enclosed the added ones. Covering the start group, as the teacher note says, also hid the added ones, and an open panel read as one group | Narrowed the start frame (width 268 to 213) in both panels so the added ones sit beside it, as the picture label already says | data |
| s05-X102a | field3 | u05-2 field 3 said "Show a 45 start card"; the item and slip show a start picture | The line now says "a 45 start picture" | section plan |

No other field 3 exit line differs from its item in numbers, key or wrong answers.

Checked and kept:

- **Rule 4.** All 22 given pairs of the exits and end items are reserved ledger rows. No teaching piece of the unit
  (aria labels and printed text, plus a pattern search of units 1 to 5 and kindergarten pieces) shows any of them.
  `ledger.py show math --before math-grade-1` with terms such as "53" finds no kindergarten addition case. X107
  (85 + 15) ends at 100 like the day 107 practice endpoint 64 + 36. I kept it: the day's goal is the endpoint, and the
  given numbers are new. R96a uses a new scattered picture for sixteen. R96b's 42 appears in unit 4 practice, but
  it is a retrieval item, and rule 4 binds exits and assessment items.
- **Facts.** No item rests on an outside fact. X109 and AF are invented and the slips say so aloud. Unit 5's
  sources.csv rows s05-base-01 to s05-base-09 (the base lessons) were the ones I checked. The register's sources say
  "From memory".
- **Keys on child pages.** No child piece prints a key. exit-106 prints 60 + 13 = 73 on purpose: the item asks what
  the given lines do, and the key says the printed total is no evidence.
- **Length and asks.** Every stem is one spoken ask. The longest (X109, 23 words, story and question) is within the
  grade's 100-word page. The swept points hold for unit 5: split pairs have their own slip stems and key entries; no
  □ appears; every end item has its Shape line and Data id; "tag" is reviewed on day 96.

Gate: `python -X utf8 scripts/gate.py --course math-grade-1` reports 0 new failing findings against the baseline
(one new note line: the size of key-assessment.md).

## My own errors

None in the answers. My picture-count helper first reported five added ones in X102a's panel because it counted the
start group's five ones too. I corrected that by reading the raw shapes: four added in panel a, five in panel b.

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
