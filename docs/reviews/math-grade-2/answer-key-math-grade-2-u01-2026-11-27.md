# Answer-key read: math-grade-2 unit 1 (days 1 to 19), 2026-11-27

A fresh read of the packet build/sections/packets/math-grade-2-u01.md, made before I read the plans, keys or prep notes
for the refine. Study step: I solved every item cold from its stem first and wrote my answers down (in
_scratch/sections/math-grade-2-u01-key/cold.md). For the picture items, field 3 prints the set-up and the key on one
line, so I solved those from the set-up numbers and the exit pieces children hold.

**Items read:** 57 (the packet's exit and end rows: X1a to X18b, F1 to F7, G1 to G5, S1 to S14 with S10a/b and
S11a to d, R1 and R2). I also checked s01-X6c, a practice row in the day 6 Exit box that field 3 counts as the third
exit fact. Its key, 6, is right.

**Verdict:** pass with fixes. Every computed key matched my cold answer. Two items needed a fix: one named no fact, and
one key did not give the equation its stem asks for.

## Faults

| Item | Kind | What was wrong | Fix | Stage |
|---|---|---|---|---|
| s01-F7 | needs-info | "How did you find that one?" names no fact. The key said "the selected saved fact", so the item could not be keyed or checked cold. | Stem now "How did you find the third fact?" (9 + 5, the fact the samples already use). Answer and steps name it. Fixed in items.csv, courses/math-grade-2/u01-4/key-facts.md (adult card and key) and the two field 3 lines of u01-4.md. The stem leaves out 9 and 5, because the gate fails two items with the same numbers (F3). | unit plan (s01 says "ask how one answer was found"), carried into section plan and data |
| s01-S10a | key | The stem asks for an equation, but the key led with the number: "6; 10 + □ = 16 is one matching equation." Every other S key gives the equation first. | Key now "16 - 10 = □ or 10 + □ = 16; the square is 6. Accept equivalent equations for the same unknown." Fixed in items.csv, key-assessment.md and key-short-assessment.md. | data |

No key errors in the computed values. No two-part stems are left: every follow-up is already its own item (X1, X2,
X6, X11, X12, X16, X18, S10, S11). The 10-word limit for printed grade 2 stems does not bind, because every exit and end
stem is read aloud. X13 (26 words) and X14 are long but each asks one thing.

**Field 3 sync.** Every field 3 cue line in the packet matched its items.csv stem. The only change is the F7 line
above, made to follow the new stem.

**Rule 4.** I ran `ledger.py show math --before math-grade-2 --term` for spool, ticket, fold, bookplate, zipper, cone,
map, cover, vote, button, pebble, leaves, clip, envelope, flag, tread, sign and the bare facts 9 + 8, 16 - 9, 9 + 5,
6 + 6, 12 - 6 and 15 - 9. I also listed the numbers printed in every practice piece of u01-1 to u01-4. No item reuses
a taught case or its numbers. The near cases I looked at:
- S5 (19 clips, 12 left) beside Grade 1 day 30 (19 clips and 15 sleeves).
- S1 (5 buttons on a tray, 4 added) beside kindergarten E1 (four buttons to a tray).
- X14's answer 9 beside Bo's 9 in the day 14 model.

Each has a different story, different given numbers and a different answer, so none is a reuse.

**Facts.** No item rests on an outside fact. All are arithmetic on given or class-collected counts, so no sources.csv
row is needed and none was checked.

**Keys on child pages.** No exit piece prints a key. key-short-assessment.md goes to children on day 19, but only
after their first marks are saved, and it keeps the S11 and R keys with the teacher. That is the plan's self-marking
step, not a leak.

**Considered and kept.** The S14 wrong answer 26 is lettered F, as in the unit plan. K would also fit, but F
("combines the given counts") is what the register and s01 say. s01-X17 is coded 2.NBT.B.5 while day 17 is coded
2.OA.B.2: listed as a plan point in the refine report.

## My own errors

- I first took s01-X6c to be missing from items.csv, because the packet lists only exit and end rows. It is a practice
  row in the Exit box. I dropped that fix before writing any rows.
- My first F7 stem, "How did you find 9 + 5?", repeated F3's numbers and the gate failed it. It is now "the third fact".

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
