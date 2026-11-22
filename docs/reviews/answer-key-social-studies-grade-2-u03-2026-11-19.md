# Answer-key read: social-studies-grade-2, unit 3, days 30 to 45

Kind: answer-key (docs/pipeline/briefs/sensitivity-read.md sections 1 to 3). No outside study; the study step is to solve.

## Items read

72 items: 41 exit items (X30 to X45h, days 30 to 43 and 45) and 31 end items (E1 to E31, day 44), with their 73 wrongs.csv rows, the exit card files (u03-1, u03-2, u03-3, u03-4), the Advice Cards C and D, Recovery Card 2, the day 44 packet and the day 45 fresh task cards. There are no readiness items in unit 3 (section 3.1 says so). Cold answers are in S:/CurioClass/_scratch/ladder2/tmp/social-studies-grade-2-key-u3/my-answers.txt, written before items.csv answers and wrongs.csv were opened.

Cold-solve limit: the day 30 to 36 exit card files print their key under the cards, and I opened them whole before solving. Days 30 to 36 are therefore not fully cold; days 37 to 45 and the day 44 packet were solved cold with the key sections cut off. Where a day 30 to 36 item matched the key I checked it by reasoning from the card text, not from memory of the key.

## Verdict

Pass with fixes. The keys were right on every item except one phrase (X45b); the faults were ambiguity, reused cases, a missing source line and one weak causal chain, all fixed below.

## Faults

| Item | Kind | What was wrong | Fix |
|---|---|---|---|
| X30b | rule4 | A ditch from a stream to fields is the case taught in unit 1 day 5 (Alder Farm Map, ledger row). | New case: a town drains a wet, muddy field for a ball field; answer: the field is dry and can be played on. Wrong row and card file updated. |
| X37, X37b | ambiguous | The weaver could use river reeds (woven mats and baskets), so X37 had two right answers; a later grade 2 unit (u07-2, day 86) has Reedmark weavers using reeds. | Fresh Cards worker "weaver" is now "knitter"; X37b answer is the knitter; card file and key updated. |
| X38b | rule4 and ambiguous | Melted bench repeats the taught melted-pan case; "where did the metal come from" also had a second true answer (originally from a mine). | "Did the new bench need new metal dug out of the ground? Say how you know." Answer: no, same metal from the old bench. |
| X38c | rule4 and ambiguous | Fuel pumped into a tank repeats the taught tank-at-a-station case and the day 39 fuel line; "where did it come from" has the deeper answer, oil from the ground. | "Did the dock make new fuel? Say how you know." Answer: no, already made, moved from the drum. |
| X41b | key | Key said "more honey" but "more" is not in the card or the ask. | Answer and look-for: honey. |
| X45b | key | Key did not list the answer the picture most plainly shows (the road behind the wall is dry). | Answer now names waves stopped and the dry road. |
| X45d | rule4 | Room 9 (a vote, a hung message, no slips) is the day 42 teaching case, Room 2, with a new number. | New case: one slip that says I read it. Answer: hung, at least one person read it, cannot say everyone did. Wrong row, card and key updated. |
| E12 | ambiguous | "The natural resource the boatbuilders use": the yard also burns coal and keeps pond fish, so all three are used by the yard. | "...the natural resource the boats are made from: trees, coal or pond fish." Packet line updated. |
| E22 and packet caption | needs-info | Connections Map caption sends advice "to animal keepers in the city", but no city is on the map. | "to animal keepers at Cedar Inlet." |
| E25, E27, E28 | ambiguous and off-goal | Learning B showed a clay water test as the learning, then a wheel stand: nothing linked the learning to the invention, so "invented because of what the potter learned" had no basis. Also "the picture" was three pictures, the key named a thought bubble inside one. | Picture 1 now shows the potter spinning clay on a flat board, bubble: the lump turning round. Key for E25: the first picture with its bubble; E28: round bowls. |
| E31 | needs-info | Item asks who made the card, but the packet cards print only "invented for practice". | Packet header: every card also prints "Made by Curio Class". |

Items solved to the key with no fault: X30, X31, X31b, X32, X32b, X33, X33b, X34, X34b, X35, X35b, X36, X36b, X37c, X37d, X38, X39, X39b, X40, X40b, X40c, X41, X42, X42b, X43 to X43d, X45, X45c, X45e to X45h, E1 to E11, E13 to E24, E26, E29, E30.

Every changed item was solved again cold after the change (X30b dry field to play on; X37b knitter; X38b no, same metal; X38c no, already made and moved; X41b honey; X45b waves stop, road dry; X45d hung, one person read it, not everyone; E12 trees; E25 first picture; E28 round bowls) and matches the new key.

## Left, with reasons

- E1 to E4 are largely answered by restating the Inlet Map caption read aloud (sheltered bay, more landing space, marsh where birds fed). That is the unit's design for a source-set assessment, so I left it; it is a question for the lead whether the caption should say less.
- X35b offers a three-way choice where two options (poster size, vote count) are weak; a child can pass by elimination. Left: the vote count is the taught wrong idea (E), and the plan chose three ways to stop a yes or no guess.
- X45c and Community B (E6, E7): arrow length plus the key shows near and far. This follows day 32 teaching (the key says which arrow is near and far) and differs from X32, which uses equal arrows by design. Left.
- X45 (Stony Lake) has the same reason to settle as X30 (fish and boats on a lake). It is a different place and the item is a fresh task, so left.
- X43d "one hard thing about digging the ditch" is on D4.1 but is answerable from common sense; it matches the day 43 frame ("one hard thing"), so left.
- X38 wrong-answer note (G, "renewable taken to mean it cannot run out") fits the plan's G wording loosely; left.
- Section plans (not mine to edit) still use old names or old stems: u03-1.md lines 55, 56, 205 to 207 (Pine Lake Town, Dry Flats; they carry a rename note); u03-3.md lines 66, 78, 252 (Harbor Map, Cook Card); u03-4.md lines 67, 78, 228 (Harbor Map) and 205 (Marsh Farm, now Meadow Farm). The exit lines in field 3 for X30b, X37b, X38b, X38c, X41b, X45b, X45d, E12, E25 and E28 no longer match items.csv (they describe the old cases); u03-1.md field 3 X30b, u03-3.md X37 to X38c and X41b, and u03-4.md X45b, X45d need updating. The ledger rows for u03 (case lists) also carry old names (Pine Lake Town, Dry Flats Card, Cook Card, Marsh Farm).
- plan.py check reports 12 FAIL lines, all "section X.Y is not in data/units.csv" for every section; none is new and none is an item or wrongs failure (units.csv was not mine to edit).

No stem relies on a picture or card that does not exist: every card named (Reed Lake Town, Windy Shore, Hill Farm, Library Flood Case, School Message Case, Advice Cards C and D, Room 4, Action Record, Fresh Cards, Garden and Wire, apple-juice chain, Towns A and B, Beekeeper, Room 6, Hill Path, Stony Lake, Meadow Farm, Cotton Town, Valley Road and the five packet cards) has a printed description. The sources marked weak or unread (30B, 30C, 32B, 33D, 37B, 38C) back background only; no item rests on a fact from them beyond what the stem itself states.

## My own errors

None against the key. One process slip: I opened the day 30 to 36 card files with their keys before solving (see above).
