english-language-arts-kindergarten s01 fix (2026-11-17)

Findings merged: 16 (assessment 7, sources 3, sequence 7; sequence 7 and the days.csv half of assessment 1 are one finding). Fixed: 14 (partial on sequence 2). Rejected: 1 (the second half of sequence 2). Lead: 7. Held up: assessment 7 of 7, sources 1 of 3 as plan changes (the other 2 are data or outside checks), sequence 6 of 7 as plan changes (sequence 7 is lead only).

What changed in s01.md
- Assessment 1: RF.K.1d letter-name row added to the day 29, 30 and 31 tables.
- Assessment 2: A2 now shows all three pictures and names the sentence, not the position. Folio A is now a puppet story (Emi asks to see Sol's puppet), so A1, A2, A4, A5 and A6 were rewritten to match.
- Assessment 3: error R sample now names counting the sounds of puppet as beats.
- Assessment 4: day 32 V1 to V4 and V7 use fresh stimuli (length sort, wet/dry and loud/quiet, stop/go, shiny, hop/creep/stomp, any describing word on the page); U3 day 32 card matched; register W reworded to cover any contrasting action verbs.
- Assessment 5: Folio B is now Bouncing Toys (not push, pull or turn), with a line that 03 and 04 teach other movements; T1 to T4 rewritten.
- Assessment 6: T3 uses AD; V2 adds an AE sample; AD repair no longer names toward and away.
- Assessment 7: sample reads "h n or n h (AA)".
- Sources 1: bow and arrow guard put in U6 day 23 (no pretend aiming, the taking retold as "someone took it", picture replaced), because field 10 and 8 are inside the word cap. Field 8 already points to field 10; the guard is in the day 23 row.
- Sequence 1: field 2 now says opposites and word use are taught on day 12; U6 day 12 begins with teaching them.
- Sequence 2 (part): U6 now replaces prompt 6 for five minutes with onset and rime blending and segmenting on days 25 to 27, on words not used in C5.
- Sequence 3: field 2 notes that day 16 also drafts the opinion.
- Sequence 4: a day 29 sentence gives waiting children 10 minutes to revise the portrait, no reteaching.
- Sequence 5: U6 day 33 adds a two-exchange partner share of the opinion drawing, unscored.
- Sequence 6: I1 and I3 are 3 minutes each, I2 is 0 added minutes observed throughout; day 29 rows follow.

Gate: python -X utf8 scripts/unitplan.py check english-language-arts-kindergarten: PASS s01.md (it had gone to 1887 words; two fixes were moved to uncounted U6 and wording was kept short to stay under the 1800 cap).

REJECTED: sequence 2 (days 29 to 31 clause) | Add oral onset and rime practice on days 29 to 31 as well as days 25 to 27, replacing prompt 6 | Days 28 to 31 are the common-battery window, where the plan says the battery replaces the usual foundations prompts, so there is no prompt 6 to replace and no free five minutes; days 25 to 27 were fixed | the unit plan's own battery rule (field 5 and U6 foundations paragraph)

LEAD:
- days.csv codes: add RF.K.1d to days 28 to 31 and RF.K.2c to day 32 (clears the generated "owned codes on no assessment day" line).
- data/plans/ela-texts.csv: fill rights ("CC BY 4.0, EL Education K-5 Language Arts 2017; adapted, art replaced") and edition (05: M1 U2 L2 to L3; 06: M1 U2 L3 to L4; 07: M1 U1 L1 supporting materials) for gk-u1-05, 06 and 07; the plan's text-set rows still say "not stated".
- Open the Office of Head Start Active Supervision page and confirm the headings "Set Up the Environment" and "Position Staff" and the accessed date; change only the quoted headings if they differ.
- days.csv day 16: add W.K.1 to the codes.
- days.csv day 29: add W.K.2 revision to the codes or note.
- days.csv day 16 Read list: add gk-u1-08 (U6 day 16 uses p04).
- Day 33 is kind Application with a record-only goal; decide whether to change its kind (U6 now gives it an unscored partner share).
