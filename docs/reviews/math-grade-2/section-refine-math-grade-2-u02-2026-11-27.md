# Section refine: math-grade-2 unit 2 (sections 2.1 to 2.4), 2026-11-27

Fresh reader. Read u02-1.md to u02-4.md whole, the rebuilt skeletons (`section_skeleton.py math-grade-2 u2`), the
goal map rows, the handbacks rows for days 20 to 38, the prep notes where a line needed them, and the ledger filtered
by term. The answer-key read of the same unit ran first in this session
([answer-key-math-grade-2-u02-2026-11-27.md](answer-key-math-grade-2-u02-2026-11-27.md)); its fixes are reconciled here.

Checked and holding: every exit, key, worked case and listed wrong solved; one letter per wrong; minutes add to 60 on
all 19 days; turn counts (six heard a day, 45 seconds each plus 30 seconds of notes, rotating 1 to 30, two-minute E
conferences on days 36 and 37 fit their 30 minutes, day 38's 14 two-minute stories plus F fit 38 minutes); a hand-back
to all 30 each day; each day's goal in student words with its kind; Shape lines on every exit; owed items (E, T, S1 to
S14 in 2.4, M and F owned by 2.3 and given in 2.4); terms taught before tested (decompose a ten day 24, addend day 27,
number sentence named as Grade 1 review on days 20 and 33 before X21, X22 and X33); `unitplan.py check` passes all four
under the cap.

## Faults

| File | Fault | Fix or rejected | Stage |
|---|---|---|---|
| u02-1.md day 20 | Unit 1 retries named by nicknames, "E17 retries" and "E18 retries". | Named by item id: `s01-X17` with A in round 1 or G in round 2; `s01-X18a` and `s01-X18b` with C or E in round 1 (matches handbacks.csv). | write |
| u02-1.md day 21 | Return and repair said "The first ten are inside independent work", which reads as if it overlapped the next part. | Plain split: first ten minutes Unit 1 rounds 3 and 4, last ten X20 D and H; others follow their pictured slips. Minutes unchanged. | write |
| u02-1.md and u02-4.md field 4, D | The D contrast (19 tiles, 4 triangles, 15 squares) echoed Unit 1's reserved S8 box of 19 shapes and its S7 square tiles, on the day Unit 1 retries return; u02-1 field 8 itself withholds "shape-box variants". | Both rows now use 16 crayons, 4 short, 12 long, wrong 16 + 4 = 20. errors.csv changed in the key read. | unit plan |
| u02-3.md day 29 | The plan told the teacher to replace the first and third printed fact prompts before copying; the page still printed 7 + 5 and 8 + 3 against items.csv's 4 + 4 and 3 + 10. | Page and key piece fixed in the key read; the plan line now just names the two facts. | write |
| u02-3.md day 32 | The two comparison slips (59 and 24 stars, 41 and 72 pins) were written inside Model but run in Practice. | Moved into the Practice line. | write |
| u02-3.md day 33 | "Recall the name Day 14 Al and Bo tabs" used a ledger entry as prose. | "Recall Al and Bo from the day 14 tabs by name only, then set up the relation again with fresh loops." | write |
| u02-4.md field 3, S10 | Stem out of sync with items.csv; no counts or key. | Rewritten from items.csv (key read, field3). | write |
| exit-28.md (piece) | X28's page lacked 74 − 39. | Caption added (key read, needs-info). | write |
| u02-4.md day 34 and X34 | Both use the name Kim. | Rejected: a name only; the object, numbers and question differ. | write |
| u02-3.md day 32 | Practice splits 73, X36's answer. | Rejected: X36 gives 55 and 18; practice keeps the first part 49 to 52, so that pair never shows. | write |
| u02-4.md X34 | "Show you are right" may read as two asks. | Rejected: one ask, the day's MP.1 plan-and-check goal, with Plan and Check spaces. | write |

Ledger (`ledger.py show math --course math-grade-2 --term ...`): the writer's case, model, routine and most term rows
are present and match the plans. Fixed: noted "Day 20 partition of 19 tiles" as withdrawn and added "Day 20 partition
of 16 crayons" (u02-1). Added the missing term rows: total, unknown, equation (u02-1, each "review of math-grade-2
u01-1 ..., planned only"), addend (u02-2, new, `--student-word`), first (u02-4, new, pairs with the existing then).
`ledger.py check math`: 0 problems.

Swept changes checked: no method question refers to "that one"; equation keys give the equation first (X21, X22,
X33, S items); reserved-case ledger notes match the fresh S1, S2, S7, S8, S9, S11 and T numbers; "number sentence" is
named as Grade 1 review in 2.1 and 2.3; Grade 1 and Unit 1 closing cases are in plain words (the two nicknames above
were the exceptions, now fixed); field 2 hand-offs use item ids; no unit 2 exit or check uses a Unit 1 reserved case.

Gates: `unitplan.py check math-grade-2` passes u02-1 to u02-4; `ledger.py check math` 0 problems; `gate.py --course
math-grade-2` 0 failing findings against the baseline (one new note line, exit-28's word count). No em dash, no
TODO(writer).

## Plan points

- s02.md field 5 still lists the older closing cases (T's tray of 8 + 5 − 4, S1 and S2 trays, S7 round and square
  tiles, S8 circle and triangle set, S9 color tiles, S11 24 + 13). items.csv, the pages and section 2.4 use fresh
  versions, so section 2.4 has to say "use the fresh versions". The unit plan should take the items.csv cases.
- T's look-for asks for a check its stem does not name; the page's Check box carries it. If the unit plan wants the
  check scored, say so in its look-fors as answer format, not as a second ask.
- The register's D example was changed in errors.csv (see above); s02.md holds no copy of the old text.

## Changed for the next unit

- A plan never tells the teacher to fix a printed piece by hand: change the piece and items.csv together (the day 29
  fact prompts were left for the teacher and never changed).
- Every number a key rests on is printed or read on the child's page (X28 lacked its subtraction).
- Teaching contrasts and register examples keep off earlier units' reserved cases too, not only exits and checks. Unit
  1's shape box of 19 (S8) and its square tiles (S7) are used up for teaching as well.
- Name an earlier unit's retries by item id (`s01-X17`), never by a ledger nickname (E17).
- A field 3 line for an assessment item copies its stem from items.csv word for word.
- Used up: unit 2's reserved cases (X20 to X37, E-add, E-sub, T, M, S1 to S14, F1 to F4, and the withdrawn 19-tile
  contrast). Later units keep off them.
