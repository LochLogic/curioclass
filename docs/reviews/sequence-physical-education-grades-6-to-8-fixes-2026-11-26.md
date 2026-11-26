# Fixes: scope and sequence of physical-education-grades-6-to-8, 2026-11-26

The fix pass after the Claude expert read (docs/reviews/sequence-physical-education-grades-6-to-8-2026-11-26.md), done
as build/scope-writes/AFTERCORE-FIX.md and docs/pipeline/briefs/sequence-fix.md say. The Codex read waits for the
usage reset (after 2026-11-30). Files changed: docs/courses/physical-education-grades-6-to-8/scope-and-sequence.md,
data/plans/physical-education-grades-6-to-8/days.csv (by
build/scope-writes/scratch/physical-education-grades-6-to-8/fix_2026-11-26.py) and
docs/courses/physical-education-grades-6-to-8/frame.md (wording only, by fix_frame_2026-11-26.py in the same
folder). Copies from before the pass are in that folder too (days-before-fix.csv, frame-before-fix.md).

Counts: applied 9 expert findings, 8 rows of the expert's "Settled by the expert" table, 3 expert "For the lead"
frame items, 4 writer "For the lead" items closed; not applied 0 (one fix applied in a different form, finding 1's
unit 12). Lead calls applied: 4, 6, 7, 9, 11 and the lead note on finding 4; not relevant here: 1 (no K to 5
specials), 2 (no unloaded base text), 3 (frame.py had no failures), 5, 8, 10, 12, 13 (nothing to change), 14 (no
band-year first day has a readiness check in its note only). Band items from the other PE reads: 1 (the CDC rescue
gap, same as finding 9). Defect rows logged: 11.

## Applied

- **Expert 1** (days.csv, .md): on the 64-session path each unit's main checked cue now has practice on a kept day:
  40 folds into 43 (catching on "give"), 59 into 61, 136 into 139 (swings on "rotate"), 211 into 213 (stick dribble).
  Unit 12: the read asked to keep 152 and drop 153 instead, but both were already dropped and every other unit 12 day
  is a protected first-teaching, closure-watch or last-Application day, so 152 stays dropped and its serve stations
  open day 155 (10 minutes on "toss, step"), the same fold form as the other units; the drop count stays 32. The
  Shorter path now states the rule "every unit keeps practice on its main checked cue on at least one kept day".
- **Expert 2** (days.csv): 166 into 170 (the rhythm form, S2.8.8), 58 into 62 (the no-one-out tag round, S2.8.1), 182
  into 186 (the week with rest days, S2.8.17), 19 into 21 (static holds in a training block, S2.8.14), 75 into 76 (the
  activity record, S4.8.3), the g6-catch-form cue check from 102 and 138 to 105 and 141, and 178's outdoor rules into
  186 with g6-rules-safe in its `retrieves`.
- **Expert 3** (days.csv, frame.md): day 23 adds "a stretch for the end of a training block: dynamic or static, and
  why" and takes about 8 minutes from the instant activity; day 131 asks one prompt per part of S2.8.11; day 229
  collects both method records (224 net, 226 invasion) and asks which change worked in each. The frame's unit 2, 10
  and 17 assessment cells reworded to match (lead call 4). On the 64-session path the net-game record moves from 224
  to 225 (5 minutes), so day 229's two records exist on both paths (own addition).
- **Expert 4** (days.csv, frame.md, .md; lead note): days 24, 79, 132 and 147 lose their readiness checks (`assess`
  blank, response time only, the note names why); retrieval added on day 25 (find a pulse, g4-pulse-body), 81
  (g4-reasons-strengths with g5-goal), 135 (g5-conflict-solve with health's conflict steps) and 151
  (g5-review-experiences), each in `retrieves`. Frame: the Readiness bullet lists only the true readiness checks and
  says why the four are retrieval; Seams rows for the four rows and the unit 3, 7, 11 and 12 cells reworded; the grade
  7 mid-year row no longer holds a readiness check. The read wins over the 2026-11-25 frame read on g4-pulse-body.
- **Expert 5** (days.csv): `retrieves` and the retrieval task add g5-fitt (day 26), g5-invasion-skills (day 53) and
  g6-strike-net-toward (day 113).
- **Expert 6** (.md): "A shorter period" added under Shorter path (35 to 40 minutes; two-day checks at six groups of
  about 3.5 minutes; one-check-day units 2, 15, 18, 21, 22 drop the focus block).
- **Expert 7** (days.csv, .md): the eleven bare earlier-year S3 codes on days 131, 173, 188, 216, 229, 239, 242, 254,
  266, 273, 284 are written with `~`; the .md says so under Course-level checks and on the grade 8 mid-year check.
- **Expert 8** (days.csv, .md): 209 folds into 211 and 280 into 282; day 169 marked "64-session path: dropped" (now 32
  drops in grade 7, 96 in all); the Shorter path sentence says the begun-toward days 83, 113, 178 are the only
  Understanding days cut.
- **Expert 9** (.md, days.csv, frame.md): "How the band runs" adds the court choice course-wide, health's disclosure
  steps and the puberty line (also in Sensitivity); day 25 and the .md use the same-day math wording ("beats in a
  minute" on day 25, ratio words from day 26), and the frame's unit 3 cell and math table row match; day 268 and unit
  21 say CDC's page lacks reach and throw rescues, so those steps are from memory until the safety agent names a free
  source; day 279 and unit 22 say Naadam is confirmed at UNESCO (2010) and the card names the rituals and imitates
  none; unit 9 (its stick station) added to the frame's safety-read list and day 113 notes "Safety read (sticks)".
- **Expert "For the lead"** (frame.md, lead calls 7 and 9): Readiness bullet and Seams (above); unit 9 on the
  safety-read list; the grade 8 mid-year row now checks units 16 and 17 and carries unit 15 from its held check by
  collect once.
- **Writer For the lead 2** (frame.md): closed by the row above. **4**: UNESCO kolo, capoeira and Naadam opened, so
  the frame's units 13 and 22 and its For the lead 5 now say the browser checks are closed and Naadam is confirmed;
  cumbia and capoeira's sensitivity read stay open. **5** (lead call 4): frame week ranges matched to the encoded
  days: unit 3 grade 6 weeks 8 to 12, unit 10 grade 7 weeks 8 to 12, unit 11 weeks 12 to 15, unit 14 weeks 26 to 31
  (three places), unit 15 weeks 1 to 14 with the held day in week 14. **6**: agreed by the read; dropped from the .md
  list. The .md's For the lead now holds two items (the 64 path, the open confirmations).
- **Band item** (PE 3 to 5 read, For the source list): the CDC page has no rescue content; applied as in expert 9.
- **Own (rule 2 re-run)**: bare cross-year codes scanned against the progression's owners: exactly the eleven of
  finding 7, none other. Every assumed earlier-grade row checked against its last use with one hop: g5-food-drink,
  g5-water-skills, g4-world-activities, g4-object-ideas and g3-stay-safe-own have no year-before use, so their
  readiness checks stand.

## Not applied

- None. Finding 1's unit 12 fix is applied as a fold into day 155 instead of "keep 152, drop 153", because 153 was
  already dropped (shown above).

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| On a reduced path, a dropped practice day that holds the unit's main checked cue, an owned part a kept check asks, or a kept-live use folds about 10 minutes into a named kept day of the same unit | The check needs practice between baseline and check; the drop count stays |
| A row a later row assumes counts as used in that later row's grade (one hop), so the next grade retrieves it, even where the frame counted the row's own grade | sequence-write.md rule 2 wins over frame wording |
| A later year's check that watches an earlier year's conduct code writes it with `~` | A year claims only its own rows |
| A same-day math lean uses the If-later wording on that day and the lean's words from the next day | "Finished first" means before the day, not on it |
| A course-level check two days after a held end-of-unit check carries that record by collect once and samples only the other units | Collect once (lead call 9) |

## For the structure pass

- None needed from this pass: no progression, frames.csv, calendar.csv or other shared file changes. The day count,
  units, owned rows and school days are unchanged. Lens spellings (lead call 13): docs/agents/lenses/physical-education.md
  shows no UK spelling by a search for the usual forms.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check physical-education-grades-6-to-8`: 0 failures.
- `python -X utf8 scripts/frame.py check physical-education-grades-6-to-8`: 0 failures (notes: unit days by year 90,
  90, 90; 22 units, 288 days).
- `python -X utf8 scripts/frame.py calendar`: no stagger break for this course (grade 6 weeks 16 and 32, grade 7 16
  and 32, grade 8 15 and 32).
- `python -X utf8 scripts/plan.py check physical-education-grades-6-to-8`: no failure.
- No em dashes in the three changed files.
