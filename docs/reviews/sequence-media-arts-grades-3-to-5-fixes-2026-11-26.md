# Fixes: scope and sequence of media-arts-grades-3-to-5, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-media-arts-grades-3-to-5-2026-11-26.md), done as
build/scope-writes/ARTS-FIX.md and docs/pipeline/briefs/sequence-fix.md say. The Codex read waits for Codex's usage
reset (after 2026-11-30) and gets its own small pass then. Files changed: docs/courses/media-arts-grades-3-to-5/scope-and-sequence.md
and data/plans/media-arts-grades-3-to-5/days.csv. frame.md is not changed (no finding asked for a frame edit this
pass may make; the frame changes are listed for the structure pass).

Counts: applied: expert 9 (findings 1 and 3 to 9 in full, finding 2 inside the frame's counts; all nine rows of
the "Settled by the expert" table), lead calls 7 (1, 2, 3, 5, 6, 7, 8; 1, 6 and 7 checked with no change needed;
4 and 9 do not touch this course), own 1. Not applied: expert 3 (finding 2's frame rebalance and finding 10, both
sent to the structure pass; finding 11, settled by lead calls 5 and 8).
Band items: no other arts expert read has an "Across the band" section; one item from the media arts K to 2 read
(its finding 4) bears on this course and is listed for the structure pass.

## Applied

- **Expert 1** (Pr6 "b" ids taught before scored). days.csv: day 61 teaches MA:Pr6.1.3b (the watching crew's
  notice, the run's experience, one result, one better way, on the screening-plan card), code added; day 124 teaches
  MA:Pr6.1.4b, code added, kind Fluency to Application (sequence.py noted a first teaching on a fluency day); day
  185 adds the teacher's modeled comparison of two results, MA:Pr6.1.5b added; day 189 presents the printed news
  sheet to a partner crew and logs one result, MA:Pr6.1.5b added; day 191's talk item compares the two logged
  results; day 63's opener no longer teaches "sharing results". .md: units 4, 8 and 12 Arc and Assessment.
- **Expert 2, inside the frame's counts.** .md Shorter path: units 3, 7 and 11 rows rewritten as settled (the
  unscored viewing joins the revision session; a second demonstration session). Unit 12 takes the read's in-count
  fallback (day 183's gathering into the making session, day 185's formats into the rehearsal session; the opening
  session two works and one technique). A paragraph says units 4 and 8 keep the overload until the frame change.
- **Expert 3** (interview used before taught). days.csv: content of days 182 and 183 swapped (school_day, unit and
  stretch kept); day 183's note says it uses day 182's interview steps; day 184's note reads "days 180 and 182".
  .md unit 12 Arc, Why this order and Processes (Produce 182, Connect 183).
- **Expert 4** (parts of codes). days.csv goals of days 51 (three ideas, two or more tools or materials; one
  invented online case sorted fair or unfair), 62 (the school-subject fact named), 63 (experience, result,
  improvement), 94 (combined after a test, goal and showing kept), 113 (one test, showing in mind), 160 (goal and
  audience, model tested with its result), 177 (goal and audience; trade card of the 1880s for a named community);
  day 143's note (one fact of the form's history). .md Course-level checks table and unit 4's assessment line.
- **Expert 5** (same-year retrieval). days.csv `retrieves` and a five-minute warm-up note on days 41, 58, 105,
  120, 170, 186. .md: "Same-year retrieval" table under Readiness and retrieval.
- **Expert 6** (criteria card on a finished sequence). days.csv: day 172 keeps the revision only (MA:Cr3.1.5b,
  ma-g5-make); day 175 holds the kept criteria card on a classmate's finished sequence, with its minutes. .md unit 11
  Arc, Assessment, Processes (Respond adds 175) and the once-a-week unit 11 check session; For the lead item 4.
- **Expert 7.** days.csv: sensitivity lines on days 147 and 167 as written.
- **Expert 8.** days.csv: notes of days 48 and 110 now the talk check day form. .md "Rotating look-fors": "never
  end-of-unit check-day items; a mid-year check samples their 'examine' part by a fresh sort or case on paper."
- **Expert 9.** .md Shorter path: the baseline look's last group is observed in the next day's opener when a fold
  day ends it (days 5, 37, 68, 82, 102, 134, 149).
- **Lead call 1.** Checked: the fold table already names 4 fold days a year (two weeks, four meetings) and gives
  one reading only. No change.
- **Lead call 2.** .md "The four processes": each year touches all four, each unit at least the processes the
  frame names, never through an id outside the unit's rows; this course happens to carry all four per unit.
- **Lead call 3.** .md Course-level checks: "Codes not sampled on a course-level check" paragraph naming every
  unsampled code with the reason.
- **Lead calls 5 and 8.** .md "Meeting days": the wrong parenthetical (frame.py "each year onto its own 160-day
  calendar") replaced with the band-wide count; the week formula and "filled school_day wins, not re-counted to
  calendar.csv" stated once. Checked by script: every unit and check falls in the frame's weeks (year 3 units 1-7,
  8-16, 18-25, 27-32, checks 17 and 26; year 4 1-7, 8-16, 18-24, 26-32, checks 17 and 25; year 5 1-8, 9-17, 19-24,
  26-32, checks 18 and 25).
- **Lead calls 6 and 7.** Checked: no check repeats the same item within two weeks; each course-level check
  carries the unit just before unscored, and no frame cell re-asks items a unit gave one to three days before. No
  change.
- **Own 1.** .md For the lead item 6 points to this report for the three items waiting on the structure pass.

## Not applied

- **Expert 2, the frame rebalance** (year 3: 7, 8, 6, 7; year 4: 7, 8, 6, 7; year 5: 8, 8, 5, 7 sessions). The
  read sends it to the lead as a frame change; the once-a-week counts are the frame's. Listed below.
- **Expert 10** (30-minute period's talk items). It bends APPROACH "Kinds of day"; the read leaves it to the lead.
- **Expert 11** (two school-day counts). Settled by lead calls 5 and 8: days.csv's band-wide count stands and
  calendar.csv is regenerated at commit.

## Settled

| Judgment | Reason | Where |
|---|---|---|
| A day that first teaches a new id while practicing another is Application, not Fluency | sequence.py flags first teaching on a fluency day | day 124 |
| Swapping two days' content keeps day, unit and school_day | the week and the frame's day counts stay | days 182, 183 |
| A kept-card check day's minutes: set-up 4, card 20, self-check 5, clean-up 3, slack 8 | the card is the day's student task | day 175 |
| Units 4 and 8 keep the overload until the frame changes; only unit 12 takes the in-count fallback | the read gives a fallback for unit 12 only, and no unscored day folds in 4 or 8 | Shorter path |

## For the structure pass

1. **docs/courses/media-arts-grades-3-to-5/frame.md, "The once-a-week path" bullet** (expert 2). Old: "Sessions on
   that path: year 3, units of 7, 9, 6 and 6; year 4, units of 7, 9, 6 and 6; year 5, units of 8, 9, 5 and 6". New:
   "Sessions on that path: year 3, units of 7, 8, 6 and 7; year 4, units of 7, 8, 6 and 7; year 5, units of 8, 8, 5
   and 7; each ideas-and-crew unit (2, 6, 10) merges its two check sessions into one, and each screening unit (4, 8,
   12) has two demonstration sessions." Then the scope's Shorter path rows become: unit 2: merge 30-31; unit 6: merge
   94-95; unit 10: merge 160-161; unit 4: 53-55 and 56-57; unit 8: 115-116 and 117-118; unit 12: 179-181 and 182-185.
   The weeks hold with every check on its week (worked for year 5 in the read). The year 3 pause sentence ("unit 4's
   last five sessions in weeks 28 to 32") becomes "last six".
2. **docs/courses/arts/APPROACH.md, "Kinds of day"** (expert 10): name one stated exception for the 30-minute
   period: the end-of-unit talk groups sit on the unit's revision day only (no critique runs there), and that day's
   rotating marks move to the two earlier making days. Then the scope's "A shorter period" paragraph changes to
   match.
3. **frame.md, Course-level checks table** (expert 4, item wording now beyond the frame cells): year 3 year-end:
   "a fresh two-idea plan" to "a fresh plan with three ideas using at least two tools or materials", and the talk
   item adds "and one invented online case sorted fair or unfair with a reason"; year 4 year-end: "two quick plans
   combined" to "two quick plans combined, with one test named and the showing in mind"; year 5 year-end: "a fresh
   proposal for a new audience with one test named" to "a fresh proposal with its goal and audience and one test
   named", and the talk item adds "and one way its form differs from a trade card of the 1880s, for a named
   community (public or invented)".
4. **frame.md, Course-level checks table labels** (scope For the lead item 2): "Samples units 1 to 3" to "Samples
   units 1 and 2; carries unit 3" (and 5 to 7, 9 to 11 the same).
5. **Band item from the media arts K to 2 read, finding 4** (year-end check placed before the screening unit for a
   stagger reason that rule 1 has made stale for specials). The same reason stands in this frame ("CALENDAR.md
   stagger tool c"), and the cost is the unsampled rows named in the scope. Option for the lead, for all media arts
   K to 8 frames together: move each year-end check to week 32, after the screening unit, so it may sample the make
   and judge rows; otherwise strike the stale reason. Bears on later.csv L107.
6. **docs/courses/CALENDAR.md**: note that K to 8 band courses count `school_day` across the band (lead call 5).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check media-arts-grades-3-to-5`: 0 failures, no notes.
- `python -X utf8 scripts/frame.py check media-arts-grades-3-to-5`: 0 failures.
- `python -X utf8 scripts/frame.py calendar`: no stagger break for this course (arts are specials in K to 5); check
  weeks unchanged (17 and 26, 17 and 25, 18 and 25).
