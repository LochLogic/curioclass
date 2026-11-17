# Fix report: english-language-arts-grade-9 unit 2 (s02), 2026-11-17

Findings merged: 27 (28 raised; assessment 1 and sequence 2 are the same RL.9-10.5 fault). Fixed: 25 (some in part, the rest under LEAD). Held up per lens: assessment 11 of 11, sequence 10 of 10, sources 6 of 7.
Main changes: P11 now scores a day 38 scar-story note (the day 31 exit is practice only); six new day 47 rows (L1 to L3, W1 to W3) and six new error letters (AI to AN); M3 moved to the fresh excerpt VII.25 to 30 (456 words) with every Meets example rewritten against it; M1 lets students choose moments; E2 moved to IV.14 and IV.16; day 36 and day 45 exit passages corrected; letters G, M, N, P re-filed; R2 and R3 accept wider repairs; day 46 is the sixth conference rotation; supplies, the Ovid numbering, the Tennyson edition and the Verne count corrected. The word cap (1,250) was the limit on the sources fixes, so a few were cut short or moved into field 5. The file had CRLF endings and is now LF.
Gate: `python -X utf8 scripts/unitplan.py check english-language-arts-grade-9` gives PASS for s02.md.

REJECTED: sources 1 | Add a free Project Gutenberg copy of Butler's 1900 Odyssey with its ebook number | The paragraph-numbering half is applied; the Gutenberg site was down and the ebook number could not be checked, and the plan has no words left under its cap for an unverified pointer | none
REJECTED: sources 7 | Add one free scholarly or museum page on enslaved women in the Odyssey to the sensitivity reads | No page was checked and the plan is at its 1,250-word cap; the Verne source line was reworded to "five sources to choose, two community-authored" | the word cap (UNIT-PLAN, Length)

LEAD:
- days.csv: add RL.9-10.5 to day 38 (the P11 note) and to day 30 (telling-frame work); day 31 is not the unit's only RL.9-10.5 touch any more.
- days.csv notes for days 39, 40, 45 and 46 should state the eight-minute conference window (42 and 43 do); the day 46 note should read "five earlier rotations plus today's", not "six earlier rotations".
- days.csv day 32: remove codes 3d and 3e (or keep them and note they are first tried, not modeled, that day); the day 32 note's oral objective-summary teaching is not in the plan (the plan teaches the summary on day 45).
- days.csv codes for the weekly derive/derivation/derivative slot (26, 31, 36, 41, 47) disagree with the L.9-10.4, 4b and 6 code days (26, 27, 31, 32, 37, 42, 47): reconcile.
- scope-and-sequence: record IV.13 to 19 (706 words) as the checked endpoint of the cold passage, or end it a sentence earlier (reserved size is 500 to 700 words).
- Rights record for the Bruegel image (days.csv day 40 "terms record"): the Commons file names the Royal Museums of Fine Arts of Belgium as holder and marks it public domain; confirm on the museum's collection page before it is named in the plan.
- Verne: name the translator and a free archive copy in the library record (not recorded in library/eighty-days).
- Ovid: confirm the Latin end line of the 583-word excerpt, and state the transcription's own licence (its Perseus header states none; credit is Perseus Project, Tufts, 1997 release).
- Day 32 exit asks for sensory detail and a reflective sentence (W.9-10.3d, 3e) before day 35 models them; the plan now says they are first tried that day. Cory or the lead may want the exit trimmed.
