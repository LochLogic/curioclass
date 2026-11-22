# Answer-key read: science-kindergarten unit 5 (end items W1 to W3, D1 to D3), 2026-11-22

Kind: answer-key. Target: science-kindergarten-u05. Date: 2026-11-22. Course finish (docs/COURSE-RUN.md stage 7).

## What I studied

The brief's study step for an answer-key read is to solve cold; nothing outside was read. Files used:
- data/plans/science-kindergarten/items.csv, unit 5 rows with check = end (17 items: W1a, W1b, W2a to W2d, W3a to W3c, D1a, D1b, D2a to D2c, D3a, D3b). No unit 5 row has check "mid" or "check"; exit and practice rows were out of scope.
- data/plans/science-kindergarten/wrongs.csv rows for those items.
- docs/courses/science-kindergarten/s05.md (the plan's field 5 and error register).
- courses/science-kindergarten/u05-2/: cards-assessment-warmth, caption-strips, cards-assessment-cover, mat-warmth, mat-cover, d052, d053, d054 (set-up parts), key-assessment-warmth, key-assessment-cover. Solved from the cards, mats and stems first; keys and answer columns opened after.

## Verdict

Pass with fixes. Fifteen of 17 items solve cleanly and match the key. W3a cannot be answered from the records the cards collect, and several item stems (W2, D3a, W3b) leave the ask under-specified, so a fair child answer can be scored wrong or unscorable.

## Solved cold, then compared

Because the warmth answers rest on dated captions the teacher collects, "solved" means the answer follows the stem, the cards and the records' form. No mismatch was a key error on fixed content.

- W1a: sand pair (card S). Matches. Alternative: none, cards O, R, W are the other matched pairs but the day offers only S beside U.
- W1b, W2a to W2d: follow the caption. Match, ties included. Ambiguity found (finding 2).
- W3a: could not solve (finding 1).
- W3b, W3c: a sunny and shaded pair at one look where the sunny was warmer; "look again" if all tie. Match. Notes in finding 3.
- D1a: roof over the patch. Match. D1b: one roof piece, one support. Match; paper or a folded strip are fair roof and support choices and the key accepts a roof and a support, so nothing fair is keyed wrong.
- D2a to D2c: roof over patch and open side; roof blocks the sunlight; less warm. Match, with finding 4.
- D3a, D3b: follow the touch. Finding 5.

Mismatches: key error 0, item ambiguous 4 (W3a, W2, D3a, D2c), my error 0.

## Findings

1. **W3a is unanswerable from the cards (item ambiguous; worst).** Stem: "touch the earlier look or the later look, whichever its record says was warmer. Touch both looks if the record says about the same." cards-assessment-warmth, "Collecting the records", records only "sunny warmer", "shaded warmer" or "about the same" for each sunny vs shaded pair at each look. No record compares the morning sunny sample with the afternoon one, so no caption on card T says which look "was warmer", and the key "as card T's captions say" has nothing to read. A child's touch of "later" is neither right nor wrong. Fix: recast W3a on what the records do hold: "For each sunny sample, touch the look where the sunny one was warmer than its shaded match. Touch both looks if both say sunny warmer, and neither if both say about the same." Update the answer column, steps and samples, key-assessment-cover/warmth W3a line, the s05.md field 5 line ("Touch the earlier or later look for each sunny sample") and the mat's last box ("earlier look or later look, for each sunny sample"). Keep the idea that later does not always win: it now shows as a morning-only or afternoon-only result. If a time-order comparison is wanted, the collecting step must add an observer line such as "the sunny sample felt warmer at the afternoon look than at the morning look", never inferred.
2. **W2a to W2d never say what is marked (item ambiguous).** Stem: "mark the sunny one, the shaded one or about the same". The question word is missing; the mat cells are blank. Cards-file wording is the same. Fix: "mark which felt warmer: the sunny one, the shaded one or about the same", for all four rows, in items.csv and cards-assessment-warmth.
3. **W3b: "Touch the pair" has no set to choose from, and the key lets "pair" be tied or shaded-warmer.** The mat offers a box "sunny pair at one look" with no card list. If a card shows the shaded sample warmer (the file allows it), a pair that does not show the sun did it is still a valid touch by the stem. Fix: "Touch a pair where the sunny one felt warmer, and show the sun did it", and add to the key: a pair whose caption is "shaded warmer" or "about the same" is not keyed right, shown with help, no letter. Also error H is listed against W3b in s05.md (field 6 table) and against W3c in the key and wrongs.csv; keep one place, W3c, and fix the s05.md row.
4. **D2c: the stem gives away error F.** "After both sit out in the sun, will your covered patch be warmer or less warm" already states the shared time, so a child cannot say "it will be cool as soon as it is on" in answer to it, and the key step "says after both sit out" is read back from the stem. Fix: "Will your covered patch be warmer or less warm than the open patch? When will you check?" or move error F to a follow-up question; otherwise F is never elicited at D2c.
5. **D3a: three marks under each patch, no rule for both "warmer".** "Under each, mark how it felt: warmer, less warm or about the same." Warmer than what is not stated, and a child may mark both "warmer", which the key does not score. s05.md field 3 says "Mark which felt warmer". Fix: "Mark the patch that felt warmer; if they felt the same, mark both about the same." Match the mat labels. Add to the key and D3b: if the covered patch felt warmer, record it as the result, keep the touch as the key, and the "why" is no clear cause shown or a note that the patches did not start alike.
6. **W1a error C cannot be observed.** The stem asks only for a touch; the wrong sample ("touches the rock and water pair and says they prove it") needs a statement the stem does not ask for. Fix: add "Say why" as a spoken follow-up, or define a touch of the unlike pair as shown with help, error C when the child says so, as the wrongs note already says for B.

## Standards check

Each item tests the goal the plan names: W1 (fair comparison) and W2 to W3 (record, reasoning) for K-PS3-1; D1 to D3 for K-PS3-2. W3a currently tests reading a caption that does not exist (finding 1). W1b repeats the morning sand cell of W2a; harmless but it spends 30 seconds of a three-minute group, so either drop W1b or keep it as the cue for W2.

## Three worst

1. W3a, no record answers it.
2. W2, the ask lacks "warmer".
3. D3a and D2c, the stem undercuts the key (both-warmer marks; error F unreachable).

## Could not settle

The real captions for cards S, O, R, W, U, T are the teacher's own and are not in the repository, so I cannot check key against caption. The keys say "follow the caption", which is sound.

## Gate

plan.py check (filtered): science-kindergarten 355 items, 296 wrong answers, 13 failures. All 13 FAIL lines are "section X.Y (science-kindergarten-uNN-N) is not in data/units.csv" for units 1 to 6 (including 5.1 and 5.2); none concerns an item or a key.

## Fixes applied (2026-11-22)

- 1. W3a unanswerable: applied. Recast to "touch the look where it felt warmer than its shaded match"; wrongs, card, key and s05.md W3 row updated.
- 2. W2a to W2d: applied. Stems say "mark which felt warmer".
- 3. W3b pair: applied. Stem reworded; key says what to do with a tie or shaded-warmer pair; a what-to-accept line added to the key.
- 4. D2c gives away error F: applied. Split into D2c ("Will your covered patch be warmer or less warm than the open patch?") and new D2d ("When will we know?"); F wrongs and handback moved to D2d; a blank-letter wrongs row on D2c; cards, key and day 53 print updated.
- 5. D3a both warmer: applied. Stems and keys reworded; day 54 line matched.
- 6. W1a error C: applied. Error C only when the child says the pair proves it.
