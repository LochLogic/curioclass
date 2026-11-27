# Section refine: math-grade-1 unit 8 (u08-1, u08-2, u08-3), 2026-11-27

I did this refine in the same session as the unit 8 answer-key read
(answer-key-math-grade-1-u08-2026-11-27.md), and after it, so the item fixes there and the plan fixes here are one
set. I rebuilt the skeletons with `section_skeleton.py math-grade-1 u8` first.

I checked these and found no fault: the part minutes on all ten days add up to 60, and day 151 puts its hook before
the warm-up. Each section counts turns: six heard per exit in 30-second turns, two minutes for cues, a rotation by
name that covers all 30 children, and a hand-back for children not heard. Observation blocks say what the other
children do. Every item has a Shape line and a goal in student words, and every day has its kind. Codes and days
match the unit plan and skeletons. All three plans are under the 1,600-word cap. The repair routes (A to 152 and
156, B to 154, C to 155, D to 157, E to 158, F to 159, G to 160) fit the slots they name.

## Faults

| File | Fault | Fix or rejected | Stage |
|---|---|---|---|
| u08-1.md | E153a moved one from a 4 to fill a 9, the same move as the day 153 error B contrast in field 4 (rule 4). | Fixed: groups 9, 5, 1 and 3, key 4 + 1 + 3 = 8, B wrong 5 + 1 + 3 = 9. Field 3 line and paper master changed. | write |
| u08-2.md | E154's start (2 + 3 + 4 = 9) equaled its change (9), so a child copying the start passed. | Fixed: the ending is one packet of ten and five loose, the change is 6, and C is 15. Field 3 line and paper master changed. | write |
| u08-3.md | E158 listed 719 (F) as its wrong, but the stem asks for marks that fix the loose squares. | Fixed: the wrong is now crossing out one square for the new stick (E). | write |
| u08-3.md | R1a gave no wrong answer with a letter ("assign a letter only if ..."). | Fixed: E, circles one loose square. The all-seventeen circle stays a note with no letter. | write |
| u08-3.md | s08-P160-response-b asked "How does 54 fit these pictures?" when 54 does not fit. | Fixed: "Does 54 match these pictures?", key No (53), wrong G "Yes, 54 has five tens." | write |
| u08-3.md | After the two fixes above, the section meets E but field 4 had no E row. | Fixed: added an E row. The contrast is 157's three ten-sticks shown on separate stock. The repair shares the F ten minutes of 159 Candidate practice. errors.csv E `if_many` says the same. | write |
| u08-3.md | The E160 stem leans on "riddle", which was never named for children. | Fixed: field 9 names a riddle on 160 as two clues a partner uses to find a hidden number. Ledger term row added. | write |
| u08-1.md | E151 (3 + 3 + 1) and E152 (1 + 3 + 4, or 4 + 4) repeat families within ten. | Rejected: days 151 and 152 are within-ten fluency days, and every family within ten is already used. The three-part pictures are new cases that no day teaches. | write |
| u08-2.md | Field 4 C contrast says "She" for Rin. | Rejected: Rin is an invented actor, and the line is clear. | write |

Ledger (`ledger.py`, one call each, day blank):

- Changed the notes of the E153a and E154 case rows to the new numbers.
- Added term rows: riddle (u08-3), joining (u08-2), take away (u08-2, review of math-kindergarten u04-2 day 68) and
  comparing (u08-2, review of math-kindergarten u04-3 day 76).
- I checked the writer's other rows (cases E151 to E160, R1, R2, the practice cases, and the terms tag, comparison,
  number sentence, clue and ten-stick). They match the final plans.

The answer-key read also rebuilt eight child and teacher pieces that were stale against items.csv (see its report).

Gates:

- `unitplan.py check math-grade-1` passes u08-1, u08-2 and u08-3. Its 4 FAIL lines on s08.md were there before.
- `ledger.py check math`: 0 problems.
- `gate.py --course math-grade-1`: 0 new failing findings.
- No em dash and no TODO(writer) in the three plans.

## Plan points

These are faults in the unit plan or in data I may not edit:

- **s08.md, field 5 goal map (line 74).** It fails `unitplan.py`: "no item row names 1.NBT.B.2 / 1.NBT.B.2c in its
  code cell" for observation days 158 and 159. The R1 and R2 rows give the code only as "content 1.NBT.B.2", and
  1.NBT.B.2c is named nowhere.
- **s08.md, U3 exit table.** It still holds the first-draft exits (7 + 2, 10 − 7, 8 + 7 and 13 − 6, flags 9 to 15,
  and so on). The section plans replaced them for rule 4 reasons, and the table no longer matches any section.
- **s08.md, field 7 fresh response task.** "Test candidate 54" led the section to write a stem that took the answer
  for granted. The field could say "does 54 match".
- **R2 (s08.md field 5) uses 68 and 69, and the fresh response uses 53.** 68 already appears as a number in E99
  (61 + 7 = 68) and in the unit 4 comparison 72 > 68. 53 appears in unit 5 P3 and unit 6 E114a. These are numbers,
  not cases, and the unit plan fixes them, so I left them.

## Changed for the next unit

- When the data stage changes an item, rebuild the child slip, the Exit box and the teacher key in the same job.
  Here five pieces in two sections still printed retired numbers.
- Check that an exit's answer differs from every quantity given in its picture. A change of nine from a start of
  nine passes a child who copies the start.
- A stem must not take its answer for granted ("How does 54 fit" when it does not). Ask "Does ... match".
- For an item that asks for a mark or a fix, list wrong answers that are marks, not numerals.
- The numbers in field 4 contrasts are taught cases. No exit may reuse them, even with one group changed around them.
- New ledger term rows (riddle, joining, take away, comparing) are the words later units use.
