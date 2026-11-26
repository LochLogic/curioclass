# Fixes: scope and sequence of physical-education-grades-3-to-5, 2026-11-26

Fix pass on build/scope-writes/AFTERCORE-FIX.md and docs/pipeline/briefs/sequence-fix.md, applying the one read so far,
the Claude expert read docs/reviews/sequence-physical-education-grades-3-to-5-2026-11-26.md. The Codex read waits for
Codex's usage reset (after 2026-11-30). Files changed: docs/courses/physical-education-grades-3-to-5/scope-and-sequence.md,
data/plans/physical-education-grades-3-to-5/days.csv (rewritten by script,
build/scope-writes/scratch/physical-education-grades-3-to-5/fix_2026_11_26.py) and
docs/courses/physical-education-grades-3-to-5/frame.md (wording only, under lead calls 4 and 7). No unit, unit order,
day count or owned row changed.

**Counts.** Applied 19 / not applied 0. Expert: 10 findings, the days-by-load line and both For the lead items applied
(the short-path rule part goes to the structure pass, as the lead asked). Lead calls: 1, 4, 6, 7, 8 applied; 2, 3, 5, 9,
10, 11, 12, 13, 14 checked, nothing to change. Band items (the K to 2 and 6 to 8 expert reads): 2 applied. Own: 3.

## Applied

- **Expert 1** (days.csv, frame.md Ends cells, .md units 2, 7, 9, 10, 15, 16): each check now asks the whole code. Day
  20 catches at a middle and a high level; day 21 adds an underhand throw to a hoop beside the roll, each marked
  apart; day 71 ten jumps in two rope tasks (self-turned forward and one of the child's choice), each marked apart;
  days 89 and 124 add "names two activities that raise the heart rate"; day 99 passes to a partner moving a few steps,
  with the hands, then three with the feet; day 152 a sequence in two of the unit's styles, the second carried from
  day 151's closure watch (day 151's closure now records it); day 159 describes both games and where each comes from.
  The frame's matching Ends cells and the grade 4 mid-year check cell are reworded (lead call 4: an assessment cell
  asking only part of a code).
- **Expert 2** (days.csv, .md Shorter path, frame unit 17 cell): the weekly goal check now opens the warm-up of every
  unit 17 day from 164 to 171. The 64-session path in grade 5 drops 167 only in unit 17 (bar graph to 171), plus 200
  (unit 20, its card folds into day 201's opener) and 219 (unit 22), in place of 165 and 169: still 16 drops, seven
  sessions between baseline 163 and check 172. "Units at three drops" and the For the lead 1 item updated.
- **Expert 3** (days 36, 67; .md Shared cards, units 4 and 7): the goal steps card in its K to 2 grade 2 form, "my goal
  and one step; a helper and a check; a changed step" (SEL STANDARD section 7, the K to 2 read's wording), until grade
  4; the four-step form on days 137 and 163 on. Day 36 retrieves g2-goals.
- **Expert 4** (days 5, 81, 226, 227, 231; .md unit 23 and Sources not loaded; frame unit 1 and unit 23 cells and the
  Safety read bullet): rescue steps now cite a public safety source that states them, the Drowning Prevention
  Coalition of Palm Beach County's "Reach, Throw, Don't Go" page
  (https://discover.pbc.gov/drowningprevention/Pages/Reach-Throw-DontGo.aspx, opened 2026-11-26: call for help first,
  reach lying down with a long object so you are not pulled in, throw something that floats, never jump in). Day 226
  adds "shout for a grown-up first". The Red Cross WHALE Tales lesson 8, "Reach or Throw, Don't Go", returned 403 and
  stays a browser check. CDC's page is now cited for life jackets and supervision only. Day 5: a life jacket "on a boat
  or when playing in natural water". Day 81: neck pulse pressed gently, two fingers, one side only (from memory; the
  safety agent checks).
- **Expert 5** (days 32, 33, 34; .md Readiness bullet and units 3, 4; frame Readiness bullet, unit 3 and 4 cells, Seams
  intro and row): rule 2 governs and this read wins over the earlier frame read (lead note). The day 32 readiness check
  is dropped (`assess` cleared, its ten minutes return to the respond task); day 33's instant activity retrieves
  g1-heart-muscle (K to 2 grade 2 day 164) and `retrieves` lists it; day 34's reteach runs where the retrieval shows a
  gap.
- **Expert 6** (days 154, 197; .md units 16, 20): readiness-results lines added.
- **Expert 7** (day 1; .md unit 1): the hook is freeze tag at walking pace in a fixed marked area.
- **Expert 8** (days.csv, 209 notes; .md Equipment bullet): every unit's and check's space line now names a wet-day
  path.
- **Expert 9** (.md Readiness bullet): the g3-strike-tools check is said once to be part-level.
- **Expert 10** (.md Shared cards, Readiness): the 3 to 5 card words are cited to the SEL 3 to 5 frame's "Shared steps
  with health and PE" bullet; retrieval is "on the first day that needs it".
- **Expert, days by load** (.md unit 24): days 234 to 236 named as the band's spaced S1 review.
- **Expert, For the lead (frame Readiness and Seams for g1-heart-muscle)**: done in frame.md under lead call 7.
- **Lead call 1** (frame Course-level checks paragraph, For the lead 5; .md For the lead 3 dropped): PE is a special,
  so its shared check weeks are settled by CALENDAR.md rule 1.
- **Lead call 8** (days 18, 73 to 79, 193, 195; .md band bullet and units 2, 8, 19): begun ids written `~ID` in the
  codes column (`~SHAPE.S1.5.17`, `~SHAPE.S1.5.1; ~SHAPE.S1.5.5`, `~SHAPE.S3.5.6`); unit 8's empty codes are filled.
- **Lead call 6**: one defect row per finding logged with plan.py (14 rows: 11 expert, 3 writer).
- **Band item, K to 2 read** (goal steps wording): the K to 2 form is quoted as that read settled it ("my goal and one
  step").
- **Band item, 6 to 8 and K to 2 source lists** (CDC has no rescue content): matches finding 4; applied there.
- **Own** (.md Shorter path): "Units at three drops" had left out unit 21 (208, 210, 211); now 18, 19, 21.
- **Own** (lead call 14 re-run): no readiness check sits in a note with `assess` blank; nothing to set.
- **Own** (rule 2 re-run): the readiness rows are now g1-world-games, g2-foods-energy, g3-strike-tools (long-tool part)
  and g2-water-skills; every other earlier-grade row has a named retrieval day.

## Not applied

None. The read's ask that the frame allow an Application drop in any unit of 6 or more days is a rule change, left
for the structure pass (lead note).

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A row retrieved in the course before during its last year counts as last used then, so it gets retrieval, not readiness | Rule 2 by use, not by the row's own grade (g1-heart-muscle, K to 2 day 164) |
| A shared card used before the partner course grows it keeps the band-before form until the grown form is taught | One card per child, met first where the partner frame says |
| A weekly goal check sits in every warm-up of a multi-week goal unit, not only Fluency days | A short-path drop must never take the week's check |
| Rescue steps cite a public drowning-prevention page that states them; CDC "Preventing Drowning" is cited only for life jackets and supervision | CDC's page has no rescue content |
| Every movement day's space line names a wet-day path, "indoors as written" where the unit is indoor work | Bar criterion 5 |

## For the structure pass

- **Short path rule (frame.md Shorter path bullet, owner: the lead).** Old: "in grade 5, where Fluency is smaller, the
  short path may take one Application game day in a unit of 9 or more days instead." The scope now drops Application
  days in grade 3 (7, 18, 51, 59), grade 4 (87, 119) and grade 5 units 20 and 22 (200, 219). The read proposes: "where
  Fluency runs out, the short path may take one Application day in any unit of 6 or more days, never its last before
  the check." The lead decides; the scope's For the lead 1 carries the counts.
- **Lens spellings (lead call 13):** docs/agents/lenses/physical-education.md checked; no UK spellings found.
- **K to 2 unit 22**: if it cites CDC "Preventing Drowning" for rescue steps, it can use the same county page (the
  read's source-list note).
- **Codex read (after 2026-11-30)**: gets its own small fix pass.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check physical-education-grades-3-to-5`: 0 failures.
- `python -X utf8 scripts/frame.py check physical-education-grades-3-to-5`: 0 failures (unit days 74 a year; 24 units,
  240 days).
- `python -X utf8 scripts/frame.py calendar`: no break named for this course (PE grades 3 to 5 at weeks 18 and 26, a
  special under rule 1).
- `python -X utf8 scripts/plan.py check physical-education-grades-3-to-5`: 0 failures.
