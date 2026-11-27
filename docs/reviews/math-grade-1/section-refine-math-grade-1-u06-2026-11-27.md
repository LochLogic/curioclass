# Section refine: math-grade-1 unit 6 (u06-1 to u06-5), 2026-11-27

I ran the refine after the cold answer-key read of the same unit
(docs/reviews/math-grade-1/answer-key-math-grade-1-u06-2026-11-27.md) and reconciled both sets of fixes.

What I checked:

- **Exits, keys and wrongs.** Every exit, key, worked case, contrast and retry in fields 3, 4 and 6 was solved cold
  against the final files. Each wrong answer carries exactly one letter from s06's register.
- **Minutes and turns.** Part minutes add to 60 on all 18 days. The hearing rotation of six children a day covers
  about 30 children, and each child not heard gets the paper back with a mark.
- **Goals, codes and items.** Day goals are in student words, and kinds, owed codes, days and the S, L, M, N and F
  items match the unit plan and skeletons.
- **Asks and cap.** Every stem asks one thing and every item has its Shape line. Words outside fields 3, 4 and 6
  run from 620 (u06-5) to 741 (u06-1), under the 1,600 cap.

## Faults

| File | Fault | Fix or rejected | Stage |
|---|---|---|---|
| u06-4.md, u06-5.md, field 3 | Ten exit and check cases reused unit 2 exit families or the unit 3 E50 exit (X121a, X121b, X122, X127b, S3, S6, S7, S8, S10, S15; found by the key read) | New cases in data, pieces and keys; field 3 lines synced | write |
| u06-4.md, day 121, 122 | The field 6 stem and Shape copies still said "removes twelve units", "four triples", "both nine-unit pieces" and "three six-unit groups" | Synced to items.csv | write |
| u06-5.md, day 126 | The field 6 stem for S15 still read "Black has eight more cubes than tan." | Now "Black has one more cube than tan." | write |
| u06-1.md L, u06-4.md day 125, u06-5.md day 126 | L-compare used X and Y from L-order with a fixed strip equal to Z, so the order answer settled the comparison | New strips V and W with a fixed six-unit strip in the L paragraph, L-compare and both Shape copies | unit plan |
| u06-4.md, E123a | The key took only ? − 5 = 12; 17 − 5 = 12 after finding the start is also a true situation equation | Key accepts both (from the key read) | write |
| u06-3.md, E118 | The field 3 line asked only for a star on the shared square | Now "Shade it and give it the same small star" to match the redrawn slip | write |
| ledger, u06 case rows | After the fixes the notes of L, E121, E122, E123, E127, S6, S7, S8, S10 and S15 gave the old numbers, and S3's reserved row named "two pairs of leaves" | Notes reset with `ledger.py note`. The two-pairs row is marked withdrawn, and a new S3 row "one pair of leaves" was added | write |
| u06-4.md, field 9 | "Grade 1 section 4.1 has tag at planned only; demonstrate it here", though day 115 in 6.2 already reviews tag | Rejected: the sentence is true (the u04-1 row is at stage planned), and the citation check passes. Pointing to day 115 instead would be taste | write |
| u06-2.md field 9, u06-3.md E120b Shape | "Gap" appears where children compare | Rejected: both mean a space between pieces that should meet, the kindergarten 3.4 term. Comparisons say "difference" throughout | write |
| u06-3.md, AN-more | Ten more than 96 is coded 1.NBT.A.1, while ten more is 1.NBT.C.5 | Rejected here: the unit plan sets the code (s06 line 102). Listed as a plan point | unit plan |
| u06-4.md, S5, S11 to S14 | Their families appear in earlier practice or models, though not in unit 2 exits | Rejected as a single-item fix: few teen families are left. Listed as a plan point | unit plan |

Ledger rows: one `ledger.py add` call, `math math-grade-1 u06-4 "" case "S3 one pair of leaves on the final board"`
(reserved; ? + 2 = 17, fifteen first). Twelve `ledger.py note` calls reset the notes of these entries:

- L retained length record
- E121, E122, E123 and E127
- S3 one arriving leaf, and S3 two pairs (now withdrawn)
- S6, S7, S8, S10 and S15

The writer's other rows (terms, models, routines and the reserved exit and end cases of all five sections) match the
plans. No lower-grade row was cited without "planned only".

Gates:

- `unitplan.py check math-grade-1`: PASS on s06 and u06-1 to u06-5.
- `ledger.py check math`: 7,855 rows, 0 problems; citation check 0 and 0.
- `gate.py --course math-grade-1`: 529 failing lines, the same as the baseline, with 0 failing findings and 3 new
  notes (word counts of the edited key pieces).
- No em dash and no open writer marker in the changed files.

## Plan points

- s06 line 52: L-compare's "fourth strip equal to Z" with X and Y lets L-order give the answer. The unit plan should
  name new strips, as the section now does.
- s06 line 102: AN-more ("ten more than 96") is coded 1.NBT.A.1; ten more belongs to 1.NBT.C.5.
- s06 field 5: the S1 to S15 table keeps its first numbers (for example S3 ? + 4 = 13), while the section and data
  use other cases. The unit plan should say the section sets the numbers, or carry the section's.
- Grade 1 needs a family budget: teen addition families within 20 are nearly used up by units 1 to 3 exits and
  models. S5, S11, S12, S13 and S14 still hit families from earlier practice or models.

## Changed for the next unit

- Teen families within 20 are nearly used up by units 1 to 3. Before choosing an exit or check fact, look it up in
  the family index, including the unit's own exits and their inner steps.
- An indirect-comparison item needs new strips, not the order item's strips, or the order answer gives it away.
- When a picture shows one square in two views, shade the square as well as starring it.
- Key lines print a period before "Error".
- A start-unknown key accepts the solved situation equation (17 − 5 = 12) beside ? − 5 = 12.
- When a data number changes, update the piece, the key, wrongs, field 3, the field 6 stem and Shape copy, and the
  ledger case note in the same pass.
