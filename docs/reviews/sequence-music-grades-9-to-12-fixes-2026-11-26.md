# Fixes: scope and sequence of music-grades-9-to-12, 2026-11-26

Fix pass on the Claude expert read docs/reviews/sequence-music-grades-9-to-12-2026-11-26.md, under
build/scope-writes/ARTS-FIX.md (the Codex read waits for Codex's usage reset after 2026-11-30 and gets its own small
pass then). Files changed: docs/courses/music-grades-9-to-12/scope-and-sequence.md and
data/plans/music-grades-9-to-12/days.csv (written by script with the csv module). frame.md is unchanged: no finding
changes the frame.

Counts: applied 12 of 12 expert findings (finding 12's CALENDAR render item goes to the structure pass) and all 8
rows of the expert's "Settled" table; 6 of 8 lead calls applied here (lead calls 4 and 8 needed no change);
0 band items (no arts expert read of 2026-11-26 has an "Across the band" section); 2 own findings. Not applied: 0
in full; 2 partial adjustments (below).

## Applied

- **Expert 1 (short path).** days.csv: every "Short path" clause rewritten by script. On the short path the mid-unit
  check, and the respond day that acts on it where there is one, is not held in every unit but unit 16, which keeps
  checkpoint 1 (495, with 496) and drops checkpoint 2 (518, 519). The note on each dropped check says the product is
  handed in at the end of the day it finishes on (named, with its short day) and scored after the session as the
  unit's baseline mark. Days not held: 32, 33, 64, 98, 99, 128, 129, 142, 143; 186, 187, 220, 260, 261, 288, 289,
  302, 303; 346, 347, 380, 417, 418, 448, 449, 462, 463; 518, 519, 545, 546, 574, 575, 608, 609, 624, 625. The merge
  is now an optimized partition per unit to the frame's short days a unit (unchanged): a short day holds at most
  three Understanding or Application days, at most two Understanding, never two step cards, never two works with a
  sensitivity note, at most five course days. Checks, respond days, critique and revision days, showings and
  readiness days stand alone. Checks still sit on short days 39, 40, 79 and 80 in every level. Result: the largest
  short day holds 5 course days (was 8). 0 to 2 teaching days a short day in Levels 1 and 2; one short day with 3 in
  Level 3, six in Level 4. scope-and-sequence.md: the "Days merge in pairs" sentence is replaced by the real rule,
  the list of days not held, and each unit's kept critique.
- **Expert 2.** days.csv day 376: Understanding, through-composed form in named steps with the step card on the
  Pathétique development or Ba Ban; "Words: through-composed". Day 377's goal opens with the seventh chord and
  secondary dominant drill. .md unit 13 says so.
- **Expert 3.** Day 547: the reviewer sings or plays one line from the peer's score before writing. Day 552: the
  reviewer performs the two passages the review cites (alone or with a partner, or played back from the score
  card). Both notes: "Performing practiced, not claimed", with the voice and no-solo controls. .md unit 17
  processes: "perform 547, 552".
- **Expert 4.** Fold-in swaps applied: 84 to 91, 120 to 125, 151 to 113, 244 to 251, 280 to 285, 307 to 267, 311
  to 295, 404 to 410, 467 to 451, in the notes and in the .md lists. A script check confirms that none of the 40
  fold-in days has a baseline look, and that none folds into a check, showing or folded day.
- **Expert 5.** Codes MU:Pr5.1.C.Ia on day 149, MU:Pr5.1.C.IIa on 309 and MU:Pr5.1.C.IIIa on 470, and the same
  codes in the .md End-of-unit lines of units 5, 10 and 15.
- **Expert 6.** .md senior fold: Level 1 days 154 to 158; Level 2 314 to 318; Level 3 475 to 478 (then 472);
  Level 4 632, 633, 635, 636, 637. It applies to a level taken in grade 12 at any level, never folds a showing,
  critique, revision or respond day, and the year-end check and its respond day move to the senior's last two days.
- **Expert 7.** Retrieval notes on every unit's retrieval day (50, 82, 118, 119, 168, 204, 205, 242, 243, 278,
  279, 328, 364, 365, 402, 403, 438, 439, 482, 538, 539, 562, 594, 595): "Opener (n minutes): retrieval of ...,
  five minutes each". Any reteach is ten minutes a row missed, in the next day's warm-up and first minutes, whole
  class if more than a third missed, otherwise a small group (UNIT-PLAN rule 6). Review days 162 and 322 say that
  retrieval is the day's drill. The Level 1 readiness notes (12, 48, 80, 116) now put the reteach in the warm-up of
  the unit's day 2 (14, 50, 82, 118). .md "Readiness and retrieval" states both.
- **Expert 8.** Day 417: the defended reading (day 406's interpretation), codes MU:Re8.1.C.IIIa. Day 418 acts on
  it, same code. The expression map stays scored at the end (434). .md unit 14 mid-unit line rewritten.
- **Expert 9.** .md candidate cells renamed to the frame's wording. Units 5, 10 and 15: "a Native American or
  Asian (or African) performance or performer's recording for the critique sitting", dropped as a day because no
  recording is in hand that is public domain, openly licensed or a Curio Class original and has no ceremonial use.
  Each stays a unit plan option at no day. Unit 7: "an African or Asian text setting", dropped, since Level 2
  already carries Egypt, China and Hindustani rhythm.
- **Expert 10.** The retrieves cells of days 161 and 321 are cleared, and their rows are added to 162 and 322.
- **Expert 11.** .md For the lead 3 (stale shared-doc item) deleted and the list renumbered.
- **Expert 12.** Day 459's goal now reads "how the music's expressive aim comes across". Day 242 is set "beside
  the singer's and composer's published words or a scholar's page". Day 452's note adds the placed-student option.
  Each "## Level n" heading now has its standards line, and the unit headings are "###". The CALENDAR render item
  goes to the structure pass.
- **Lead call 1.** .md: "Ten course days a level (10 school days, this course meets daily)". There was no second
  reading to drop.
- **Lead call 2.** .md "How this file reads": each level holds all four processes, each unit touches the processes
  its frame row names, no day claims an id outside its unit's owned rows, and practice without a claim is noted as
  such (unit 17's performing).
- **Lead call 3.** The unsampled-codes list with reasons stands as written. No frame change proposed.
- **Lead call 5.** .md: school_day counts inside each level (1 to 160), because the levels are taken in separate
  years.
- **Lead call 6.** Notes on check days 159, 239, 319, 399, 479, 559 and 639 now say that the items are new (unseen
  excerpts or fresh prompts), never the unit's own prompt type on the same work. Day 79 already said so.
- **Lead call 7.** Checked: no course-level check re-asks items of a unit assessed one to three days before. Day 79
  samples unit 2's ids, not unit 3's. 159, 319 and 479 sample units 3 and 4 (or 8 and 9, 13 and 14), and 559 and
  639 sample units 16 to 18. No change.
- **Lead call 8.** The formula is now stated once in the .md: week = (school_day - 1) // 5 + 1. By script, every
  unit's first and last weeks match the .md and the frame, and every check sits in week 16 or 32.
- **Own 1.** Dropping day 417 on the short path: the defended reading is written on day 406, so its note hands the
  reading in at the end of day 406 (short day 44), not at the end of the making day before the check.
- **Own 2.** Rule 2 lists re-run. Level 1 readiness covers the grade 8 rows (frame For the lead 2 stands), and
  Levels 2 to 4 retrieve the level before on day 2 or 3. Every check code is taught before its check, including day
  417's MU:Re8.1.C.IIIa (taught 402 to 406), and MU:Pr4.3.C.IIIa stays on 411, 412, 416 and 434. Collect once: the
  carried records on 79, 159, 239, 399 and 559 stand. End days and our words: no fault found. No em dash in either
  file.

## Not applied

- None in full. Two adjustments to expert 1, with the reason:
  - Units 3, 8 and 13 have no respond day after their mid-unit check (the critique day follows it), so only the
    check day is not held there. Levels 1 to 3 free 9 days each, not 10. The counts still fit inside the frame's
    short days a unit.
  - A five-course-day ceiling on a short day was added to the expert's rule. Without it the optimizer packed eight
    Fluency and Application days into Level 4's last practice day (631 to 638).

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| On an 80-day path a unit of 25 short days or fewer drops its mid-unit check and the respond day that acts on it; the product is handed in at the end of the day it finishes on and scored after the session as the baseline mark | sequence-write rule 2 asks for a mid-unit check only in units over 25 days; frees the time the cap needs |
| A short day: at most 3 Understanding or Application days, at most 2 Understanding, one step card, one sensitive work, 5 course days; checks, respond, critique, revision, showing and readiness days stand alone | expert 1, plus the five-day ceiling |
| Level 4 checkpoint critique days that answer a dropped checkpoint are not held when the unit keeps another critique (552, 582, 618) | frame short-path keep list: one critique, one revision, one respond day a unit |
| A practiced process with no claim is written "practiced, not claimed" in the note and listed in the unit's process line | lead call 2 |
| Retrieval openers run five minutes a row; the reteach goes in the next day's warm-up, and a Level 1 readiness reteach in the unit's day 2 warm-up | expert 7, UNIT-PLAN rule 6 |

## For the structure pass

- docs/courses/CALENDAR.md, the generated 9-12 rows (lines 257 to 260): the check labels are cut at 24 characters
  ("Level 1 mid-year (week 1 week 16"). Fix the label render in `scripts/frame.py sync` so it reads "Level 1 mid-year
  (week 16), Level 1 year-end (week 32)". The weeks themselves are right. This is the expert's item; the lead owns
  the script.
- docs/courses/music-grades-9-to-12/frame.md For the lead 6 (ADOPTION-BAR-SUBJECTS.md arts row stale): close it.
  The arts row already says the NCAS checking and the 63 strand ids were completed 2026-11-21 (expert 11).
- Optional, for the lead (the frame is not wrong): frame.md "The short path." bullet, after "and one respond day.",
  could add "A unit of 25 short days or fewer drops its mid-unit check on this path (unit 16 keeps its first)." The
  scope states it now.
- Still open from the scope's For the lead 1: unit 18's check set should name the day 574 checkpoint.

## For Cory

- Nothing new. The supplies ceiling (frame For the lead 7) still waits on the Desk.

## Gates

- `python -X utf8 scripts/sequence.py check music-grades-9-to-12`: 0 failures. Notes only: units 1, 6, 11 and 16 to
  19 own no standard, as before.
- `python -X utf8 scripts/frame.py check music-grades-9-to-12`: 0 failures.
- `python -X utf8 scripts/frame.py calendar`: no 9 to 12 rows printed and no stagger break. No frame change was
  made, so none is expected.
