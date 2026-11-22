# Answer-key read: english-language-arts-grade-2, unit 1, days 1 to 32

Kind: answer-key. Date: 2026-11-20 (file dated 2026-11-19 by the job). Reader: fresh agent that did not write the data.

## What I studied

Nothing outside the repository; for this kind the study step is to solve. I solved every item cold from its stem and the card or text it needs (texts g2-u1-c11, c18, c31a, c31b, c31c, rc1, rc4, rc5, g2-u1-02 for the day 26 question, and the unit's card pieces), and wrote my answers to a scratch file before I printed any answer, steps or samples column. I then compared. I checked rule 4 against the unit's shared pieces and texts (grep inside the unit folders) and against the lower-grade ledger (`ledger.py show ela --before english-language-arts-grade-2 --term ...`, filtered by term).

## Verdict

Pass with fixes. The keys were right on every item I solved (no key mismatch), but 11 items had faults in the item itself: cross-item answer leaks, a "why" with no stated reason, a card whose draft gave the answer away, a photograph item answerable without the photograph, two rule 4 near-reuses of a lower-grade case, a missing word list for a teacher-read item, and one key sample that used a fact the card does not give. All fixed in items.csv, wrongs.csv and the unit's shared pieces.

## Items read

84 items in items.csv (all of unit 1, days 1 to 32: 36 exit items, 48 end items), with their 100 wrongs.csv rows before my edits (101 after).

## Faults and fixes

| Item | Kind | What was wrong | Fix |
|---|---|---|---|
| s01-A2 | ambiguous (answer leak) | "Who made the sign?" names the sign, which is the answer to A3 "What did the class make?" asked next | Stem now "Who made something for the book corner?" Answer unchanged |
| s01-A6 | ambiguous | "Why did Mira print the words?" has no stated reason; "she said she could print the small letters" and "to make the sign" are both defensible | Stem now "Why did Mira stay by the table while the others chose paint?"; key accepts "She said she could print the small letters, so she stayed to print the words." |
| s01-A7 | ambiguous (answer leak, duplicate) | "How did Mira keep the paper from curling?" had the same answer as A8 (tape) and named the problem A8 and A9 ask about | Stem now "How did Mira make room for Leo to paint the border?" Answer: she moved her chair. Wrong row changed to "She asked the teacher to move the table." (A, contradicts the text) |
| s01-A39 | ambiguous (answer leak) | "Who returns books?" gives the word "books", the answer to A40 | Stem now "Who uses the return shelf?" Answer unchanged (pupils) |
| s01-A28 | needs-info | The ten words to read aloud were not named in the stem, only in the key | Stem now lists the ten words in a mixed order (loaf, snail, sigh, weed, crow, clay, shy, bead, tie, silly) so the read order does not group by sound; key unchanged |
| s01-A31 | needs-info | Key and sample said tools are "things they use in the garden"; card 4 never mentions a garden | Now "these are what they rinse and put away, like the spades" (key and sample) |
| s01-A23, A29, A35 | key (incomplete) | The stem asks why the note goes by the tap, on the shed door, by the door; the key answered only the purpose, and the card gives no reason for the place beyond the next pair reading the note | Key adds "the next pair reads it before starting" (A23 adds "at the tap") |
| s01-X8 | rule4 | Dry glue, from a lower-grade ledger case (grade 1 u01-2 day 9 glue stick repair cards; u01-5 glue stick) | Card now "The ribbon is too short, so Mira ties on a second piece. Wind lifts her paper, so she closes the window." Key, steps, samples and wrong row updated; cards-exits-7-12.md updated |
| s01-X12 | rule4 | "Pencil rolls" is a grade 1 u01-5 ledger case (pencils roll) | Card and ask now use a mitten that drops behind the shelf. Steps, samples updated; cards-exits-7-12.md updated |
| s01-X12c | key (too narrow) | Key accepted only the clear path; the picture also shows three stacks with legs fitted together | Key accepts either |
| s01-X23 | off-goal | The words already said "rolling stand", so the photograph was not needed (steps said "photograph or the second card"); day 23 goal and RI.2.7 need photograph details | Second card now "where pupils can move it"; ask adds "and what the photograph shows about the second globe"; key: high shelf versus movable, photograph shows a stand with four wheels. Steps, samples, one new wrong row ("sits on a table", A) and the wrong note updated; cards-exits-21-25.md updated |
| s01-X29 | ambiguous (answer given away) | The draft's own last sentence ("Open umbrellas dry faster.") was the key's ending, so a child could repeat it | Draft now "Drips fall onto a cloth on the floor."; suggestion "Explain what the cloth helps."; key "The cloth keeps the floor dry." Steps and samples updated; cards-exits-27-29.md updated |
| s01-X32d | key (too narrow) | E ("Say a fact from the card") listed one fact only | Key accepts any one fact of the card, with the old one as the example |

Every changed item was solved cold again after the edit; all new answers matched the keys.

## Rule 4

Shared pieces and texts of the unit: no item reuses a case, picture or numbers from them (checked cases such as crate, tent, window, shelf, basket, chairs, folder, word cards, mats, cubby, apron, peg, satchel, stencil, magnet, globe, envelope). Story scenes that share a word (pencil case, plant shelf, window desk) are different cases. Lower-grade ledger: two hits (X8 glue, X12 pencils), both replaced. No other term returned a lower-grade case (terms checked include truck, tent, kite, goat, pail, basket, umbrella, apron, cubby, satchel, stencil, magnet, globe).

## Section plan exit lines that no longer match items.csv

The section plans say items.csv is truth; I did not edit them (outside my files). Stale after this read:
- docs/courses/english-language-arts-grade-2/u01-2.md: E8 (glue and paper clips), E12 (pencil), and the day 11 row (line 81: "who made the sign", "why Mira printed the words", "how the corners were kept flat", and its key).
- u01-5.md: E23 (second card "rolling stand", ask, answer).
- u01-6.md: E29 (draft, suggestion, answer); the day 29 row for A28 says "Pattern Card's ten word-to-sound matches" and has no word list.
- The ask wording of E1 to E7, E9, E10, E13 to E15, E21, E22 and the exit lines of E16, E17, E20, E24, E25, E27, E28 still match items.csv; their answer lines are paraphrases, not conflicts.

## Left, with why

- s01-X32q (Q path): the dictated "The soap is on the sink." tests spelling by pattern (L.2.2d) while the item code is L.2.2e (reference use, which the R path tests). Left: the day 32 round four pairs Q with error Q (pattern) by design.
- s01-A33: "pail" has a homophone spelling "pale" a child may write from sound; the target is the taught ai pattern, and the plan names it. Left; teacher marks "pale" as not yet seen for the pattern.
- s01-A19: the stem says "first and second school articles"; the question card prints "02-a and 02-b". Same meaning; left.
- s01-X15 and A46 (diagram items): the words already give the order, but the standard asks what the diagram adds and the picture spec says the arrow adds order only. Left by design.

## My own errors

None that changed an outcome. I first suspected A28's "silly" (short i plus long e) and X15 and X32q; on reading the unit plans (y as a taught team, five labels with no short i) and the diagram specs, I left them.
