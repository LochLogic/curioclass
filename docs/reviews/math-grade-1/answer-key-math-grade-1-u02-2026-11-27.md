# Answer-key read: math-grade-1 unit 2 (days 17 to 39), 2026-11-27

Fresh reader; I did not write this data. Work came from build/sections/packets/math-grade-1-u02.md, plus the child and teacher pieces opened item by item.

## What I studied

- The study step for this kind is to solve. I solved every item from its stem and its printed picture: counting the drawn objects in each exit, booklet and strip piece, and working the arithmetic and the story role myself. Then I compared with the key.
- docs/pipeline/kit/notes/grade-1.txt: printed stems are 10 words or fewer unless the teacher reads them aloud. docs/courses/math-grade-1/DEFAULTS.md: stems are spoken, one ask each.
- docs/pipeline/briefs/sensitivity-read.md sections 1 and 2, kind `answer-key`.

## Verdict

Pass with fixes. All 55 keys are arithmetically right and match their pictures. One item was ambiguous as printed and one field 3 line had drifted from its item. Both are fixed.

## Items read

55 in all: the 54 exit and end rows in the packet, plus s02-X33c. That item is the day 33 Exit box question, filed as `practice` and so left out of the packet. I opened it because the plan and the key print it.

Here is how I checked the pictures against the keys. Each exit, booklet and strip piece was parsed and its drawn objects counted per labeled row. Every count matched its item: 12 and 7 kites; 14 and 3 birds; 11 and 19 stars; 18 and 12 flags; 14 striped and 6 spotted fish; 4 circles of 13; three mats of 14, 14 then 5, and 24 for E25; 5 shown of 20; 13 triangles and 1 square; 16, 1 and 3 choices; 18 leaves and 10 flowers; 10 and 10 cups; 20 spoons and 10 forks; 20 triangles and 12 circles; 13 stay and 7 leave; a 20-star mat; 19 pins and 18 tags; 4 then 20 lanterns; 14, 4 and 2 choices. On the Equality strip, each side's picture equals the value of its expression, and the crossed marks match the subtracted amounts.

## Faults

| Item | Kind | What was wrong | Fix | Stage that made it |
|---|---|---|---|---|
| s02-X27 | ambiguous | The picture prints thirteen triangles and one square unpaired, and the stem read only "Which triangles have no partner?" As printed, every triangle has no partner, so ringing all thirteen was a true answer to the words. Yet the key scores it as error E. The pairing step the key needs ("after one valid pair") was not in the ask. | The stem is now "Pair the square with one triangle. Which have no partner?" (10 words, one answer: the other twelve). Changed in items.csv, courses/math-grade-1/u02-3/exit-27.md, courses/math-grade-1/u02-3/key-exits.md and the E27 line of docs/courses/math-grade-1/u02-3.md field 3. The key, wrongs row (E, all 13), handbacks, day and goal are unchanged. | section plan (stem written there; data carried it) |
| s02-X32 | field3 | The field 3 line read "What fact tells the difference?" but the item, the exit page and the key read "What fact tells the triangle difference?" | Field 3 E32 line now quotes the item's stem. | data (reworded the stem without syncing the plan) |

I answered the changed item cold again. After pairing the square with any one triangle, twelve triangles have no partner. Ringing all thirteen now ignores the instruction, which is error E. One right answer.

## Checked and not faults

- **Rule 4.** I ran `ledger.py show math --before math-grade-1` for kite, bird, star, flag, bell, fish, tile, counter, brush, leaves, cup, spoon, lantern, cushion, ticket, pin and tags, and filtered out this unit and later units. No lower-grade case uses the same object with the same numbers. The nearest are kindergarten's "ten kites one moved", "six paint pots and nine brushes", "eight flags, three stored" and "six trays/eight tags", all with different numbers. Unit practice pieces use other cases: comparison cards with clips 15 and tags 11 and pegs 14 and holes 12; data cards with knots 13, loops 2 and waves 4; the art display with lines 12, dots 2 and curls 3; animal cards with 10 curled and 3 stretched cats; the picture game with Jo's 17, 6 and 11 cards; and cover cards with 17 tabs and 12 covered. No exit or end item matches these.
- **s02-S31a.** 11 + 3 is also the bare count-on card in courses/math-grade-1/u01-4/counting-check.md (days 14 to 16). That piece is in an earlier unit of the same grade, so it falls outside rule 4's scope as worded (this unit or a lower grade). The case also differs: a flag story here, a bare count there. Left as is; noted for the lead.
- **Captions.** The "Leave" and "Stay" captions on E33a and E35 and "Arrive" on E19, E31a and E34 name the pictured action, not the label or number asked for. I judged them not a giveaway. On E25 the removal mat's before panel shows the same fourteen shapes, but it adds an action the story does not have. I judged it a fair distractor, keyed to the static mat.
- **Two asks.** None left. E30a and E30b, S30a to S30d, Q34a to Q34f and N35a to N35f are already one ask per item.
- **Stem length.** Every stem is read aloud. All are 10 printed words or fewer except the six Q34 and N35 stems, which lead with the printed equation the teacher reads.
- **Off-goal.** None. Each item's code and part fit its day's goal and the section field 3 line.
- **Key on a child's page.** None. Exit, booklet and strip pieces print only stems, givens and empty boxes. Keys are in courses/math-grade-1/u02-1/key-assessment.md and the four key-exits.md pieces, which the child pieces name as teacher-only.
- **Field 3 sync, otherwise.** Every other exit and end stem appears verbatim in its section's field 3, and the keys and wrong answers agree. The A39 records are scoring rows, keyed through key-assessment.md.
- **Facts.** No item rests on an outside fact: all are invented scenes and within-20 arithmetic. Each child-held piece traces to its own sources.csv row: s02-exit-17 to s02-exit-38, s02-exit-25-b, s02-exit-25-c, s02-exit-box-33, the s02-story-booklet rows, s02-equality-strip and s02-unknown-strip (all status "written"). Each day traces to its s02-base-NN row (checked 2026-11-27).

## Could not settle

- The operations progression row (s01-count-progression) lists days 1 to 16 only. Unit 2's problem types (join, separate, part-whole, compare, unknown positions) rest on the same progression. It is an s01 row, outside this job's edit scope, so it goes to the lead. No item's key depends on it.

## My own errors

- At first I took s02-X33c to be missing from items.csv, because the packet holds only exit and end rows and the plan and key print E33c. The row exists (check `practice`, the Exit box convention also used by s01-X11c and s01-X15c), with its wrongs and handbacks rows. Not a fault.
- The packet prints each key beside its stem, so "cold" solving rested on working each item before reading its answer cell. I worked each one myself, but the layout could not prevent seeing the answer.
- My first rewrite of X27 had 11 words, over the grade 1 limit of 10. I shortened it to 10 before finishing.

## Changed for the next unit

- An exit picture printed "unpaired" or "unmatched" needs the pairing step in the stem, or the not-yet-seen answer is a true reading of the words.
- Exit box items are filed as `practice` and the key packet leaves them out. Read them anyway, because they are judged and printed.
- After a data-stage stem rewording, quote the new stem in field 3 in the same pass.
