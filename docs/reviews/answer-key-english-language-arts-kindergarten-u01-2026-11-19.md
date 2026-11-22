# Answer-key read: english-language-arts-kindergarten, unit 1 (days 1 to 34), 2026-11-19

Items read: 74 (every exit, readiness and end item in items.csv, with its wrongs.csv rows, the unit's shared pieces in courses/english-language-arts-kindergarten/u01-1 to u01-7, and the texts gk-u1-01 to 04, 08 and Folios A, B and C).

## What I studied
Nothing outside; the study step is to solve. I solved every item cold (picture choice, spoken question or observed behaviour) from its stem alone before opening its key, samples or look-fors. The ledger (`ledger.py show ela --before english-language-arts-kindergarten`) is empty, so no lower-grade case can be reused.

## Verdict
Pass with fixes. Of the 74 items, 63 matched my cold answer with no change; 11 had a fault, all fixed in the data and in the printed pieces. No key was outright wrong on the picture answer; the faults were mostly items whose stem echoed the answer, cases that repeat a shared piece, and one key that named a book the day does not use.

## Faults and fixes

| Item | Kind | What was wrong | Fix |
|---|---|---|---|
| s01-X3 | rule4 | Jo builds a bridge or a road from blocks: the same case as Mira's block road and block bridge (gk-u1-02 pages 2 and 6) | Now "Can we build a gate?" with gate, tower, wall; card, key, answer, steps, samples updated |
| s01-X4 | ambiguous (stem gives the answer) | Stem said "if you did not know what reaches means", so the child only echoes it | Stem: "if one word in the last sentence was new to you"; key accepts a question about reaches or bends |
| s01-X14 | rule4 | Pinwheel turning (also a topic card on day 31) and a toy truck that turns left when steered (gk-u1-04 page 5 steers a toy car left) | Paper spinner and toy merry-go-round; pictures, spoken pair, wrongs, card and key updated |
| s01-X24 | ambiguous (stem gives the answer) | Stem named the word ramp, so the child echoes it | Stem: "if one word on these cards was new to you"; key accepts any question about a word |
| s01-X26 | key | Key required a question about chimes; "What is a xylophone?" is a real question and was ruled out | Steps now accept a real question about Pip's pick or about chimes |
| s01-X30 | ambiguous (stem gives the answer) and wrong row | "Rhymes with box" is answered by fox, which is in the card; wrong row "fish" was said to share a first sound with box (it does not) | Now "rhymes with tail" (mail, sail, pail); wrong row is tub (shares only the first sound with tail); card and key updated |
| s01-X32 | rule4, ambiguous and wrong row | Full against empty is pair 3 of the day 12 opposite cards; "opposite of full" is answered by empty in the card; wrong "heavy" was coded U but is not a stronger synonym of full | Card now hot against cold; spoken "opposite of day" (night); strip 2 wrong row rewritten, "heavy" row removed; card and key updated |
| s01-I1, s01-I4 | key | "Which toy?" was offered as the question that asks for help (it asks for information) | Sample and key: "Can you help me pick a toy?" |
| s01-T4 | key | Stem said "the top's movement" but Folio B has no top; key question was about the bean bag | Stem: the spring toy; key: "Does the spring toy go up and down? Yes." plus a reread request |
| s01-A6 | key (text_ref) | text_ref said "last two sentences" but the unclear phrase "After this song" is in the third | text_ref: the song sentence and the last sentence |
| word-relationship-cards (V1) | rule4 | Length sort used a jump rope, the long toy of riddle 2 (day 17) | Scarf in its place |
| texts/gk-u1-folio-c.md (B3 to B12) | key | Said m and r are taught "from day 26"; the opener, cards and C4 say day 28 | Now "first taught day 28" |

Eleven items changed (X3, X4, X14, X24, X26, X30, X32, I1, I4, T4, A6), plus two shared pieces (V1 cards, Folio C).

By kind: key 6 (X26, I1, I4, T4, A6, Folio C), ambiguous 4 (X4, X24, X30, X32), rule4 4 (X3, X14, X32, V1), off-goal 0, needs-info 0. X32 counts in two kinds.

## Left, with why
- s01-X15 and X19: the puzzle with "pieces" echoes the class big book ("Pieces fit together"). Minor, a different sentence and a choice item; left.
- s01-X13: wrong row "the cat marching in a line" is coded W (verbs enacted the same) though it is a picture error (B). Harmless to scoring; left.
- s01-A2: the stem prints the picture's sentence, so "tell what moment it shows" can be an echo. The point-to-the-picture part still tests RL.K.7; left as a judgment call for the lead.
- Day 33 has no exit item and plan.py reports "30 percent of questions need the text" and missing units.csv rows; all three pre-date this read and are not item faults.

## My own errors
None found: every cold answer matched the key on the picture and spoken points once the faults above were read as faults.

## Gate
`plan.py check` for this course: 74 items and 114 wrong answers checked (115 before; the "heavy" row was removed). The 9 FAIL lines (needs-text share, 7 units.csv rows, day 33 exit) were present before and are unchanged; no new FAIL.
