# Answer-key read: math-grade-1 unit 4 (days 69 to 92), 2026-11-27

Kind: answer-key (docs/pipeline/briefs/sensitivity-read.md sections 1 and 2). Target: build/sections/packets/math-grade-1-u04.md, the unit's items.csv and wrongs.csv rows and the child slips they print on.

## What I studied

Nothing outside, as the brief says for this kind: the study step is to solve. I solved all 54 items cold from their stems and the child slips (exit-69 to exit-91, packet-values, packet-relations, packet-mental). I counted the scattered pictures by script (exit-69 is 70, exit-74 is 43, exit-86 is 33 and 37, exit-91 is 49). Only after that did I open the answers, wrongs and teacher keys.

## Items read

54 items: 28 exits (s04-X69 to s04-X91b) and 26 end items (s04-A89digit to s04-A92difference). Every key matched my cold answer. I checked all 74 wrongs rows: each one's value follows from its stated error, and each carries one register letter. The exception is s04-X91a's row, which records a missing estimate (accuracy unscored) and has no letter, correctly.

## Faults

| Item | Kind | What was wrong | Fix | Stage |
|---|---|---|---|---|
| s04-X75, s04-X75b | two-asks | Exit-75 still printed the old combined stem "What amount does each digit stand for?", and the teacher key held one combined entry with a Shape line no item has. items.csv already holds two items. | The slip prints both items.csv stems, and its note says to read them one at a time. key-exits.md (u04-2) now has an s04-X75 entry and an s04-X75b entry, built from items.csv and wrongs.csv. | data |
| s04-X84, s04-X84b, s04-X84c | two-asks | Exit-84 printed one combined stem, "What signs make this whole row read correctly?", for three items. The key held one combined entry. | The slip prints the three items.csv stems, one per sign box. The key has three entries. | data |
| s04-X84b (and X84, X84c) | ambiguous | Each group printed its total (46, 81, 81, 69), and the two middle groups were drawn the same way. The labels and the matching pictures gave away "=", and the listed A wrong (counting the left rods as ones) could not happen. Field 3 asks for unlabeled groups with the two 81s laid out differently. | Rebuilt the picture strip with no totals. The first 81 is two banks of four upright rods with the single set apart above. The second is eight horizontal rods with the single below. Recounted: 46, 81, 81, 69. Keys: <, =, >. | data |
| s04-X85, s04-X85b, s04-X85c | two-asks | Exit-85 printed only X85's stem above "____ □ ____ □ ____". The b and c stems and the fixed 27 □ 62 and 62 □ 65 links were missing. The key held one combined entry, with a D wrong (27 > 62 > 65) that no wrongs row has. | Rebuilt the slip: the order line, a fold line, then each of the b and c stems with its own fixed link. The note says to keep the fold under until an order is written. The key has three entries. | data |
| s04-X69 | ambiguous | The stem asks for "the count on this tag", but the slip's answer line read "Count", so the child saw no tag. | The line now reads "Tag". | data |
| s04-X86, s04-X89 | ambiguous | The sign box was drawn with □, the same mark as a unit square. On exit-89 it sat between the two pictures, where a child could count it as a one. | The box is now drawn with a border. | data |

Field 3 sync: every stem quoted in the field 3 lines of u04-1 to u04-5 matches items.csv, so no field 3 line needed a fix. The refine pass added the missing Shape lines for six end items (see its report).

Rule 4: I cross-checked every item's numbers against the unit's teaching pieces by script, then read each hit in context. The hits were day numbers, font sizes, record rows or different cases, such as 50 − 20 and 70 − 50 on removal-cards against 90 − 40 and 60 − 40. I searched the lower-grade ledger for "ten", "compar" and "estimat", and checked the unit 2 and unit 3 teen cases from the sweep. No item reuses a taught case, picture or number set. One point rejected with reasons: s04-A89teen's 17 as one ten and seven ones was already a unit 3 exit (E50). But every teen from 11 to 19 already has such a case in kindergarten or units 1 to 3. The torn packing-record picture is new, so rule 4 holds by case. Whole-ten-cards shows three tens named thirty, and s04-X72b removes three tens. Naming and removal are different skills and different cases, so I did not count that as a fault.

Facts: no item rests on an outside fact. Every slip is "Invented for practice". This unit's sources.csv rows (s04-base-01 onward) are base-lesson credits only. No key appears on a page children hold. Keys sit in key-exits.md (one per section) and key-packet.md, and the slips only point to them in the teacher note.

Off-goal and needs-info: none. Each item tests its day's goal and codes in days.csv. DEFAULTS.md sets no stem word limit beyond "one ask in a child's words", and no stem asks two things. The longest is s04-X81: three short sentences, one question.

Changed items answered cold again against the final files: exit-69 (seven tens, tag 70); exit-75 (20; 6); exit-84 (46 < 81; 81 = 81; 81 > 69); exit-85 (27, 62, 65; 27 < 62; 62 < 65); exit-86 (33 < 37); exit-89 (56 > 55). A script confirms that every exit stem is printed exactly as items.csv has it, and that all 54 items have a matching key heading. The only stems not printed are the six whispered mental starts (s04-A89more to s04-A91less), which come from key-packet.md by design.

Gate: `python -X utf8 scripts/gate.py --course math-grade-1` shows no new FAIL in unit 4. The FAIL lines it calls new (13 in plan-math-grade-1 for s01 card stems and s01-X6b, u01-1/family.md in lesson, s03.md in unitplan) were there before this job. The stored baseline, build/gates/base-math-grade-1/, holds only index-reports.txt, so those gates report "[no baseline file]" and count every line that already failed as new. Each file those lines name was last changed before this job began: items.csv at 06:52, before the packet was cut at 06:59, and the others on 11-25 or 11-26. The 334 orphan lines match the baseline. Template point: the gate stored a baseline for only one of its gates.

## My own errors

On first read I flagged s04-X85b and s04-X85c as giving away X85's order, since their stems name the pairs. I withdrew that: field 3 has the sign strip covered until each child has written an order, and the rebuilt slip now folds there. I made no key errors.

## Changed for the next unit

- When the data stage splits a stem into two or three ids, rebuild the child slip and the teacher key entries in the same job. The slip prints each items.csv stem, and each id gets its own key entry (exits 75, 84 and 85 were stale).
- Draw a sign box as a bordered box, never with □, the mark used for a unit square.
- Every end item in field 3 keeps its own "Shape:" line with its Data id, as exits do.
- A word an exit stem leans on (here "tag" and "comparison") is taught on or before that day and gets a ledger term row.
- Teens 11 to 19 all have a taught "ten and some ones" case by now. Later items keep rule 4 by using a new picture or context, never a remembered one.
