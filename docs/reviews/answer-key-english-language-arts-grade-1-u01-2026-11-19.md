# Answer-key read: english-language-arts-grade-1, unit 1, days 1 to 33

Kind: answer-key. Date: 2026-11-19. Reader: a fresh reader who did not write the data.

## What I studied

Nothing outside (answer-key brief, section 1). I solved every item cold from the stem and the student card text in items.csv (printing stems only), recorded my answer, and only then opened the answers, samples, wrongs.csv rows, the shared pieces in courses/english-language-arts-grade-1/u01-*/ and the texts g1-u1-01 to g1-u1-04. The lower-grade ledger was checked term by term (`ledger.py show ela --before english-language-arts-grade-1 --term ...`).

## Items read

86 (exit and end items for days 1 to 33; X8, X19 and X32 do not exist in items.csv), with all 122 wrongs.csv rows.

## Verdict

Pass with fixes. Nearly all items matched my cold answer; the faults below are small and are fixed in items.csv, wrongs.csv and the shared pieces that print the items.

## Faults

| Item | Kind | What was wrong | Fix |
|---|---|---|---|
| s01-X12 | rule4 | The card says the wagon "tips over" and a picture is "the wagon tipped". "tips" is a day 27 observation word (A30, Card F) that the unit plan says must not appear on any exit card. | Card, picture, answer, samples and two wrongs now say "falls over" / "fallen over". Piece u01-3/cards-exits-10-14.md changed to match. |
| s01-X21 | ambiguous, rule4 | Picture 2 was "a ball rolling away"; a tray with low sides could also hold a ball (day 23 card says a tray's sides stop balls), so two pictures could be right. It also repeats the "rolling" case of the day 21 job menu. | Picture 2 is now "a cat asleep on a chair". Piece u01-5/cards-exits-21-24.md changed to match. |
| s01-X29 | ambiguous | The card has three statements ("measures our paper", marks, straight edge) but asks for two facts; "measures our paper" is a true fact that the key rejected. | First sentence is now the topic: "A ruler is a tool for our paper." The two facts are the marks and the edge. Piece u01-7/cards-exits-28-33.md changed to match. |
| s01-A28, A29, A30 | ambiguous (passable by elimination) | Card F picture 2 was a cat beside an upright cup; the stem names the pup, so the child could answer without reading. | Picture 2 is now a pup beside an upright cup. Piece u01-6/card-f-and-item-cards-day27.md changed to match. |
| s01-A37 (card V in A33 to A38) | ambiguous (answer given away by the card) | Card V said "Her little scoop is bigger than the tiny scoop beside it", so "which is smaller" was answered by the card, not by knowing the words (L.1.5d). | Card V now says "Her little scoop sits beside the tiny scoop." A37 asks "Point to the little scoop and to the tiny scoop. Which one is smaller?" A33 to A38 stems and piece u01-7/word-card-v-and-sort-cards-day29.md changed to match. |
| s01-A41 | key | Stem "Who clears the path?" but the key answer was a sentence ("Nana rakes the leaves into a pile"), and the wrong "a strap" was not from any card. | Answer is "Nana (she rakes the leaves into a pile, and the path is clear)"; sample "Nana."; wrong is now "The rake." (a thing, not who), error A. |
| s01-A7 (wrong) | ambiguous | Wrong "Why is the sofa green?" named a sofa color the picture never gives. | Now "Why is the rug green?" (the pictured green rug, a detail the words do not give), same error A. |

## Checked and left

- Rule 4 against the ledger: the ELA ledger holds nothing below grade 1 that these items reuse as a case. Kindergarten has a "ramp cards (Mo and Lee)" exit case; Card C (ramp and barrel, A42 to A44, A51, A52) is a different scene, so I left it. Lead may choose to rename the ramp if it wants the object itself kept out.
- A33 sorts sieve and flour, words from Card A (day 8) and the kitchen article. It is a word sort, not a reuse of the cook and sieve scene, and the section plans ask for it, so I left it.
- X28 and X22 can be passed by repeating or pointing to a sentence of the card; this is the intended recognition task for these exits, so left.
- Wrongs: error letters and notes match their stems; X31's blank error letter is by design (no error letter).

## Section plan field 3 lines that no longer match items.csv

items.csv is the truth; these plan lines (docs/courses/english-language-arts-grade-1/) still show old cases or wording and were not edited:

- u01-3 E12 (line 101): "the wagon tips"; now "falls over".
- u01-5 E21 (line 110): pictures list "a ball rolling away"; now "a cat asleep on a chair".
- u01-5 E23 (line 112): card and wrong say "blocks"; items.csv says "balls" ("A tray's sides stop balls rolling away"; wrong "It stops the balls rolling").
- u01-6 E25 (line 144): "blocks", "blocks sliding off"; items.csv says "counters". 
- u01-6 E26 (line 145): card "Your paper bin holds our books. How will I take one out?"; items.csv: "Our paper bin holds our books. Its sides are tall, so a hand cannot reach in."
- u01-6 E27 (line 146): "blocks"; items.csv says "counters".
- u01-7 E29 (line 187): card first sentence "A ruler measures our paper."; now "A ruler is a tool for our paper."
- u01-7 E30 (line 188): answer "without dropping them"; items.csv answer says "without losing them" (samples also give dropping; harmless).
- u01-7 E31 (line 189): strips about a clip; items.csv uses "The folder holds paper." and a folder picture.
- u01-7 E33 (line 190): watering can, roots and spray; items.csv uses a tub with a hole near the top, rain running out versus rain on the lid.

E1 to E11, E13 to E18, E20, E22, E24 and E28 match.

## My own errors

None found: on all 86 items my cold answer fitted the key or the mismatch was a real fault above. Where an open item has many right answers (X2, X6, X26, A1, A3, A9, A44) I judged the key's sample list, not a single string.

## Gates

`plan.py check`, filtered for english-language-arts-grade-1: before and after output are identical (10 pre-existing FAIL lines about units.csv, source-map.csv and the 7 percent text-dependent share; no new FAIL).

## Could not settle

Whether the 7 percent "needs the text" share (pre-existing FAIL) should be fixed in this unit; the unit's exits are spoken cards by design.
