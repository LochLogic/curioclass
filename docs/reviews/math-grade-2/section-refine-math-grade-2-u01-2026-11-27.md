# Section refine: math-grade-2 unit 1 (u01-1 to u01-4), 2026-11-27

A fresh read of docs/courses/math-grade-2/u01-1.md to u01-4.md against the section plan bar. I rebuilt the skeletons
first (`section_skeleton.py math-grade-2 u1`). I ran this after the answer-key read of the same unit, whose report is
docs/reviews/math-grade-2/answer-key-math-grade-2-u01-2026-11-27.md. Its fixes are reconciled here.

**What I checked, and what passed.**
- **Exits and keys.** I solved every exit, key and worked case cold. Every listed wrong answer carries exactly one
  letter from the s01 register.
- **Day 1 retrieval.** The nine keys match s01's rows.
- **Minutes and turns.** Each day's part minutes add up to 60. Turn counts fit about 30 children: rotating six at 45
  seconds, 4½ minutes. The F interviews fit: 15 children at 2 minutes on days 17 and 18. The day 19 S and R block is
  37 minutes. The hand-backs land in named parts with the minutes to hold them.
- **Kinds and goals.** Every day states its kind and a goal in student words.
- **Caps and gates.** All four plans are under the cap (unitplan.py passes). There are no em dashes and no TODO(writer).

## Faults

| File | Fault | Fix, or rejected with why | Stage |
|---|---|---|---|
| u01-1.md field 8 | The first paragraph listed Grade 1 reserved cases by ledger nickname ("the two-row removal", "racks of 95", "the 52/54 and 53/54 response records"). A teacher cannot use that. | Rewritten in plain words: use the Grade 1 closing folder if it comes. A Grade 1 closing case comes back only as a reminder, and never as an exit, check or practice card. | prep (the prep note handed the writer the same list) |
| u01-1.md field 9 | E2 ("addition sentence", "subtraction sentence") and E12 ("number sentence") test a word the plans never name. The plans teach only "equation". | Field 9 now names number sentence as the Grade 1 word for an equation, and says what addition and subtraction sentences are. Ledger review row added. The stems are kept, because Grade 1 teaches the word and unit 2's exits use it. | write |
| u01-2.md field 2, u01-3.md field 2 | "The two-part check" names nothing a teacher can find. | Now "the day 11 parts check (`s01-P11-parts`)". | write |
| u01-4.md field 1 | E17 is a grouped count of a collection, coded 2.NBT.B.5 in items.csv, but field 1 did not list 2.NBT.B.5. | Added a 2.NBT.B.5 line for day 17, tied to days 5 and 6. | unit plan (day 17 is coded 2.OA.B.2 only) |
| u01-4.md field 3 | The F7 cue "How did you find that one?" named no fact. | Now "How did you find the third fact?" (9 + 5), matching items.csv and key-facts.md (from the answer-key read). | unit plan |
| u01-3.md, E14 | Its answer 9 equals Bo's 9 in the day 14 model. | Rejected. The given numbers (11 and 2) and the story are new, and rule 4 is about the given numbers and the story. | |
| u01-4.md, S14 | The wrong answer 26 could be lettered K instead of F. | Rejected. s01 and the register's F ("combines the given counts") fit. | |
| u01-1.md, E1 | 1 + 1 is an easy exit for grade 2. | Rejected as taste. It fits the day 1 goal ("small sums within 10") and is a transfer to a covered part. | |
| u01-4.md, day 19 | The marking part hands key-short-assessment.md to children. | Rejected as a fault. It comes after first marks are saved, keeps S11 and R with the teacher, and keeps originals visible. | |

**The answer-key read's fixes, reconciled here.**
- s01-F7: stem and key, key-facts.md, and the u01-4 field 3 lines.
- s01-S10a: key, key-assessment.md and key-short-assessment.md. No plan line printed the old key.

**Ledger.** The writer's rows cover the terms, models, routines and cases of all four sections, and the review rows
cite their sources. Changes:
- **Note fixed: E16 longer fold strip.** Was 13 folds, six fewer, 19. Now 12 folds, five fewer, 17.
- **Note fixed: F private six-fact check.** Was 8 + 7 and 15 - 7. Now 7 + 1 and 20 - 8, with keys 8, 12, 14, 7, 12, 6.
- **Note fixed: S8 circle and triangle box.** Was 18 shapes and 7 circles. Now 19 shapes and 8 circles, 11 triangles.
- **Added:** u01-1 term "number sentence" (student word), "review of math-grade-1 u05-1 [number sentence], planned
  only".

**Gates.**
- `unitplan.py check math-grade-2`: u01-1 to u01-4 PASS.
- `ledger.py check math`: 0 problems. Citation check: 0 planned-only findings, 0 unmatched.
- `gate.py --course math-grade-2`: 0 new failing findings. The 272 index-reports orphans were in the baseline. There are
  two new note lines (key piece word counts).

## Plan points (unit plan or data I may not edit)

1. **s01.md day 17 F row and field 5** still list 8 + 7 and 15 - 7 (answers 15 and 8). The plan, items.csv and the key
   use 7 + 1 and 20 - 8 instead; 8 + 7 is a day 4 practice fact. Update s01 to match.
2. **s01.md S8 row** says 18 shapes, 7 circles, wrong answer 25. items.csv and the key use 19 shapes, 8 circles, wrong
   answer 27. Update s01.
3. **s01.md and days.csv, day 17 codes.** Day 17 is coded 2.OA.B.2 only, but s01-X17 is coded 2.NBT.B.5 and the goal
   groups a collection with sums to 50. Add ~2.NBT.B.5, as days 5 and 6 have.
4. **s01.md F.** "Ask how one answer was found" leaves the fact open. The items now fix it to the third fact (9 + 5),
   and s01 could say so.

## Changed for the next unit

- A method question names its fact by position ("the third fact"), never "that one", and keeps the fact's numbers out
  of its stem.
- A key for an item that asks for an equation gives the equation first, then the value of the square.
- When a writer changes a reserved case's numbers, the ledger note changes in the same pass (E16, F and S8 were stale
  this unit).
- A stem that says "number sentence", "addition sentence" or "subtraction sentence" needs the word named as review of
  Grade 1 in the section plan (unit 2 exits use it).
- Write Grade 1 closing cases in plain words, as reminders only, never by ledger ids.
- Field 2 names a hand-off by its item id, not by a nickname.
- Used up: unit 1's reserved cases (E1 to E18, F, G, S1 to S14, R) are now correct in the ledger. Later units keep off
  them.
