# Fixes: scope and sequence of visual-arts-grades-9-to-12, 2026-11-26

Fix pass on the Claude expert read docs/reviews/sequence-visual-arts-grades-9-to-12-2026-11-26.md, under
build/scope-writes/ARTS-FIX.md (the Codex read waits for Codex's usage reset after 2026-11-30 and gets its own small
pass then). Files changed: docs/courses/visual-arts-grades-9-to-12/scope-and-sequence.md,
data/plans/visual-arts-grades-9-to-12/days.csv (written by script with the csv module; 48 rows changed, 640 rows,
no day added or removed) and docs/courses/visual-arts-grades-9-to-12/frame.md (four cells, where finding 1 (c),
finding 4 and one stale line ask for it; no unit, order, owned row or day count changed).

Counts: expert findings 13 of 13 applied (finding 7 with two open picks left to the lead, finding 8 settled by lead
call 2), all 15 rows of the expert's "Settled" table applied (two rows adjusted, below). Lead calls: 1, 2, 5, 7 and 8
applied here; 3 already met; 4 and 6 needed no change. Band items: 0 (no arts expert read of 2026-11-26 has an
"Across the band" section; the shared items are the lead calls). Own findings: 5 applied. Not applied in full: 3
(below).

## Applied

- **Expert 1 (Level 4 series).** days.csv: day 530 and day 562 notes say the series continues as homework sketchbook
  time and in unit 18's studio sessions where the project grows from it; day 635 (a duplicate of day 633's second
  talk) is now "Series studio: the next work of the series made toward its final state, the checkpoint calendar
  updated" (Application, VA:Cr2.1.IIIa, hazard note); day 559 and day 639 goals and notes take the new items (a fresh
  timed study with a written revision decision, a defense of one of two given readings of a unit 16 work; a plan for
  continuing the series and a defended change on one exhibited piece). frame.md Course-level checks: the Level 4
  mid-year and year-end cells rewritten to the same items, on new evidence. scope-and-sequence.md: unit 16 and unit
  19 text, the check table rows and the Level 4 line under "Owned codes no course-level check samples".
- **Expert 2.** days.csv: the content of days 487 and 488 swapped: day 487 writes and checks the hazard card, day 488
  holds the material trials and the baseline look (first group), day 489 the second group. The 6+7 and 8+9
  short-path merges still hold. .md unit 16 says so.
- **Expert 3.** days.csv: baseline looks (first group, second group) on days 16/19, 48/49, 87/88, 125/126, 171/172,
  248/251, 289/291, 333/336, 443/444, 537/539, 570/572, 606/609; removed from days 15, 47, 170 and 331; units 8, 13
  and 14 keep theirs, unit 16's moved with finding 2. None sits on an Understanding day or a fold-in day (scripted).
  .md: a "Baseline looks" line under the unit shape.
- **Expert 4.** days.csv: day 340 weighs one image use and one material or tool choice that affects others; day 353's
  second case is a materials or tools case; day 358's sitting adds a short second prompt on a materials or tools
  choice. frame.md unit 12 evidence line: "and one materials or tools choice weighed" added to the VA:Cr2.2.IIIa
  item. .md unit 12 names the days of both parts.
- **Expert 5.** days.csv: day 332 is Understanding, the series medium at Level 3 in named steps by medium group with
  step and hazard cards (hazard note); the six-thumbnail drill moves to day 333's opener; day 348 points back to day
  332's techniques. .md unit 12 order line.
- **Expert 6.** days.csv: day 237 (Cr1.1 item from a different piece of the student's own Level 1 portfolio), day 397
  (Cr1.2 theme drawn from unit 12), day 559 (reading item on a unit 16 work) goals and notes. .md: the blanket
  sentence replaced by one line per check saying where its items come from; table rows for Levels 2 and 3 mid-year.
  The frame cells' new wording is under "For the structure pass" (lead call 7).
- **Expert 7.** .md Shorter path: one merge rule written (at most one first teaching of a technique or hazard card a
  merged day; join making, fluency and revision days; check, respond and critique days never merge; on a 1+2 merge
  the retrieval moves to the next short day's opener) and every unit's merges re-picked by an optimized partition to
  the frame's short-day counts (unchanged), with group size at most 4 and a penalty on joining a technique day with
  two others. Units 2 to 19 all meet the rule. Units 6 and 11: kept at 3 short days with the placement checklist
  filled from brought work (the expert's second option, no frame change); unit 1: see Not applied.
- **Expert 8 and lead call 2.** .md: a "four processes" line (each level holds all four, a unit at least those its
  frame row names); day 537 adds two-minute compositional thumbnails (unit 17 "create 7"); unit 19 "create 35";
  For the lead 2 marked settled. Units 5, 10 and 15 keep their frame processes.
- **Expert 9.** .md "Senior calendar" for all four levels (finish by level day 155; the 150-day finish by the same
  rule) and the line that on the 10-days-short year the checks fall on level days 149 and 150.
- **Expert 10.** .md: each Level heading names its id set.
- **Expert 11.** days.csv day 49 "Start routes one and two", day 50 "Start route three"; .md unit 3 names the days.
- **Expert 12.** days.csv day 156: "would shape your own awareness of the social or political question it raises".
- **Expert 13.** .md: respond days (goal "Respond: ...") removed from the responding lists of every unit, with the
  rule stated (Level 4 critiques held as respond days stay responding); the Level 4 fold-in row in day order; the
  senior Level 4 five are 496, 503, 516, 523, 542; day 12's va-g8-ideas retrieval moved to day 10 (before the
  critique), readiness table updated; the Level 4 readiness note kept on day 482, For the lead 1 marked settled.
- **Lead call 1.** The 10-days-short year is 10 course days a level (already so); the 149 and 150 check line added
  and the band-wide minutes total dropped.
- **Lead call 5 and 8.** .md: school days counted inside each level (level day n is school day n of that year,
  week = (level day - 1) // 5 + 1), `school_day` left blank (frame.py's band count gives the same week inside each
  level), stated once; every unit and check falls in the frame's weeks (frame.py check and calendar pass).
- **Lead call 7.** Days 237, 397 and 559 draw their items from earlier units' content in a different form; frame
  wording for the Levels 2 and 3 cells goes to the structure pass. The Level 4 cells were changed in frame.md because
  finding 1 asks for exactly that.
- **Own 1.** days.csv day 527: "set up for showing at the mid-year check" was stale (the check no longer shows the
  series); now "at the unit's end".
- **Own 2.** frame.md unit 16 row: "Showing: the series in progress at the mid-year check" changed to "at the unit's
  end" for the same reason.
- **Own 3.** Senior calendar: the expert's lists folded days 125 (Level 1) and 443 (Level 3), which finding 3 makes
  baseline days. Days 153 (practice items move to day 154's opener) and 452 fold in their place.
- **Own 4.** Unit 16's baseline: two groups (488, 489), as every other unit now has.
- **Own 5.** Re-ran the rule 2 lists by script: every owned id on an end day in its own level (sequence.py); no
  baseline on a first-teaching or fold-in day; every fold-in a Fluency day with no assess; every short-path merge
  free of check, respond and critique days; the earlier-grade table matches the `retrieves` column after the day 12
  move. Nothing else found.

## Not applied

- **Expert 7, unit 1 (the bridge).** The rule cannot hold in unit 1's 6 short days: days 1 to 9 re-teach six grade 8
  techniques (pencil value, charcoal value with its hazard card, contour and gesture, one-point perspective, the
  color wheel with wet clean-up, the looking routine) and days 10 to 12 cannot merge, so one technique a day needs 9
  short days, and the bar's 10 percent cap on days outside the standards allows the bridge at most 8 of 80. The scope
  keeps the frame's 6 with merges 1+2+3+4; 5+6+7; 8+9 (one material family a day, dry before wet, two re-taught
  techniques a day at most) and puts the pick to the lead (below).
- **Expert 7, units 6 and 11 count.** The expert left the lead a pick (4 short days each, or the checklist from
  brought work). The scope uses the second, which needs no frame change; the 4-day option stays open for the lead.
- **Expert 8, units 5, 10 and 15.** No creating day added: lead call 2 settles that a unit need not claim all four.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A 9 to 12 course counts school days inside each level and leaves `school_day` blank | Levels are taken in separate years; frame.py's band count gives the same week inside each level |
| A Level 4 check never rescores the series or the essay; it takes a fresh study, a plan, a defended change or a reading on earlier-unit work | "No artifact is scored twice" |
| A student-chosen material's hazard card is written and checked the day before its first trials | Hazard card before any new material |
| Baseline looks sit on two practice days (one group each), never a first-teaching or fold-in day | Two marks a unit; no score on a first-teaching day |
| Short-path merges: at most one first teaching of a technique or hazard card a merged day, found by an optimized partition to the frame's counts | Fits a 45-minute session; counts unchanged |
| Senior fold-ins never take a baseline day | Keeps the two marks a unit |
| A respond day is tagged only by the process it reteaches | Lens: a respond day acts on a check |
| A check right after a unit draws that unit's ids from an earlier unit's content (the student's own Level 1 piece, a unit 12 theme, a unit 16 work) | Checks that do not repeat; lead call 7 |

## For the structure pass

1. docs/courses/visual-arts-grades-9-to-12/frame.md, Course-level checks, Level 2 mid-year cell. Old: "and a new open
   problem posed from a given earlier work (VA:Cr1.1.IIa)". New: "and a new open problem posed from a different
   piece of the student's own Level 1 portfolio than the one used in unit 8 (VA:Cr1.1.IIa)".
2. Same table, Level 3 mid-year cell. Old: "and a series plan for a new theme that follows or breaks a named norm
   (VA:Cr1.2.IIIa)". New: "and a series plan for a new theme drawn from unit 12 (the pattern-study era or the
   student's unit 12 theme) that follows or breaks a named norm (VA:Cr1.2.IIIa)".
3. build/scope-writes/ARTS-BRIEF.md, Arts notes, "The four processes" bullet. Old: "appear in every unit's days; the
   .md says on which days." New: "appear in each year or level (lead call 2, 2026-11-26); each unit touches at least
   the processes its frame row names, and the .md says on which days."
4. Lead pick, unit 1 short path (frame.md "The 80-day short path" bullet and unit 1's "Short path: 6 days"): keep 6
   with two re-taught grade 8 techniques a short day (as the scope now has), or cut contour and gesture and the color
   wheel from the short-path bridge and teach each at its first need in units 2 and 3 (one technique a day then fits
   in 6). Raising the bridge to 9 short days would break the bar's 10 percent cap.
5. Lead pick, units 6 and 11 short path: keep 3 short days with the checklist from brought work (as now), or give
   each 4 (units 7 and 12 to 15 short days; frame.md unit rows and the short-path bullet change together).
6. data/plans/calendar.csv: regenerate with `frame.py calendar` at commit (no unit or check day moved here).

## For Cory

- Nothing new. The frame's open picks still stand: two levels in one room (frame For the lead 4) and the supplies
  ceiling (frame For the lead 7).

## Gates

- `python -X utf8 scripts/sequence.py check visual-arts-grades-9-to-12`: 0 failures (notes only: units 1, 6, 11 and
  16 to 19 own no id, as the frame sets).
- `python -X utf8 scripts/frame.py check visual-arts-grades-9-to-12`: 0 failures; 19 units, 640 days, 156 unit days a
  level.
- `python -X utf8 scripts/frame.py calendar`: no failure; grades 9 to 12 have no stagger rule beyond the finals week,
  and this course breaks none.
- `python -X utf8 scripts/stale.py check`: 0 failures.
- `python -X utf8 scripts/gate.py --course visual-arts-grades-9-to-12`: 0 failing lines for the course; it refuses
  with "no baseline" (lead call 4: the lead sets the baseline at commit), and its index-reports step exits non-zero on
  data/plans/science-grade-3/days.csv day 12 (changed since its sign-off), not this course.
