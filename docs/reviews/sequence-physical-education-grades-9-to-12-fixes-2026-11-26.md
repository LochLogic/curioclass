# Fixes: scope and sequence of physical-education-grades-9-to-12, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-physical-education-grades-9-to-12-2026-11-26.md), as
build/scope-writes/AFTERCORE-FIX.md asks. The Codex read waits for Codex's usage reset (after 2026-11-30) and gets its
own small pass then. The other PE expert reads of 2026-11-26 (K to 2, 3 to 5, 6 to 8) have no "Across" section, and
none of their findings or lead items touches grades 9 to 12.

Counts: applied 8 of 8 expert findings (finding 6 by lead call 14), 4 frame wording fixes (3 from expert findings under
call 4, 1 from the scope's own For the lead 2), 4 lead calls applied (4, 9, 10, 14); not applied 0. Band items: none.
The days.csv edits were made with a script (build/scope-writes/scratch/physical-education-grades-9-to-12/fix_2026_11_26.py;
the pre-fix copy is days-before-fix.csv beside it). 54 rows changed; no unit, day count, kind or owned row moved.

## Applied

- **Expert 1 (serious), days.csv and scope-and-sequence.md.** On the 64-session path a named kept day now absorbs each
  dropped day's only practice: day 10 (from 9: partners and the courtesy card, the S3.12.1 and S3.12.2 record; codes
  added), day 34 (from 32: one before-and-after change, S2.12.13 added), day 49 (from 48: one tactic per game, S2.12.1
  and S2.12.2 added), day 131 (from 129 and 130: control leg with the checklist, S3.12.6 added), day 154 (from 143 and
  145: the expressive block, S4.12.1 added; and a repeated hard moment, S4.12.8 added), day 147 (from 148 and 151: a hard
  moment with the strategy used and judged, S4.12.8 added). The drop days' notes now name the kept day instead of "its
  cue returns in the next instant activity". The .md's Shorter path has a new absorb table.
- **Expert 2, days.csv.** All 24 check and respond days (38 to 40, 78 to 80, 118 to 120, 158 to 160, 198 to 200, 238 to
  240, 278 to 280, 308 to 310) carry a joined space, gear and wet-weather line for the units each samples (day 158:
  the teacher-checked route in groups, water, shade, cold and heat rules, indoor map course; dry land only for the life
  jacket station).
- **Expert 3, days.csv, .md and frame.md.** Day 155 adds "for each block the health part it builds and the interest it
  matches"; day 158 adds what the student would change in their own pace at a control (the individual half of
  S3.12.7); day 308 adds one technology and one food choice with reasons and a "what would you try next" item on a
  pictured challenge, and S3.12.1 is dropped from days 308 and 309 and from the .md check table; days 172, 173, 198,
  199, 252, 253, 278 and 279 say each student is marked on the S1 code (and on 172 and 173 the S2 tactic code) that
  matches the chosen activity, claimed only as used in new settings. The frame's grade 10 and grade 12 year-end cells
  are reworded to match (call 4).
- **Expert 4, days.csv and .md.** Day 145 and day 147 tag S4.12.3 and S4.12.4 with a private log line on the health
  part and the interest; day 154 tags S4.12.9 with the reflection's two examples drafted; day 100 tags S2.12.11 (what
  the block could give an adult); day 101 tags S2.12.5 (how the plan could shape a week after school). Unit 12's .md
  paragraph says so.
- **Expert 5, days.csv, .md and frame.md.** Day 137's source line now names CDC for life jackets and currents, the
  National Weather Service "Cold Water Hazards and Safety" page (opened 2026-11-26) for cold-water shock and
  hypothermia, and reach and throw rescues "from memory, the safety agent to confirm". The frame's unit 11 sources cell
  and its Safety read bullet say the same (call 4); the .md's Sources not loaded line too.
- **Expert 6, lead call 14, days.csv and .md.** Days 81, 161 and 241 (each a band year's first day after a
  course-level respond day) now carry assess = readiness; the "assess blank" wording is gone from their notes and the
  .md unit 7, 13 and 19 paragraphs; the scope's For the lead 1 is dropped.
- **Expert 7, days.csv.** Day 180's SEL line is dropped; day 93 now says "PE first: SEL 9 to 12 unit 14 (grade 11) may
  open with this rest-and-sleep plan as retrieval".
- **Expert 8, days.csv.** g8-striking-fielding-play added to day 42's retrieves (note: unit 3's target golf swing gives
  the setting); g11-fitting-challenge added to day 296's retrieves (note names unit 15).
- **Own (from the scope's For the lead 2), frame.md.** The Seams row for g8-fitness-dance-apply into unit 7 now reads
  Retrieval (grade 9 uses it through the rows built on it), matching day 82.
- **Lead calls 9 and 10, frame.md.** The Course-level checks paragraph now states collect once (a check within ten
  days of a unit's end reuses its record unscored), that S4.12.9 has no check after it and the scored reflections of
  units 12 and 24 are its evidence, and that a chosen-activity station marks the matching code. The scope's For the
  lead 4 and 5 are dropped as settled.
- **Call 4, frame.md.** The Shorter path bullet adds that a named kept day absorbs a dropped day's only practice.
- **Defects logged** with plan.py: 8 expert rows on days.csv, 3 expert and 1 writer row on frame.md, all fixed,
  made-at scope.

## Not applied

- None. Lead call 1 (specials) does not touch 9 to 12 (finals week only). Calls 2, 3, 5, 8, 11 and 12 had no case here;
  the twelve "standard None is on no day" notes for units 13 to 24 stay (call 12). Call 13: docs/agents/lenses/
  physical-education.md has no UK spellings found by a search for the common forms.

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| A short path drop that holds an owned part's only practice names the kept day that absorbs it, in both notes and in a Shorter path table; caps stay | Every band course with a 64-session path |
| A chosen-activity check marks the one S1 (and S2) code matching the student's activity, not all four | PE 9 to 12 grades 11 and 12, any choice-based check |
| Check and respond days carry the joined space line of the units they sample | All PE scopes |
| Readiness on a band year's first day after a course-level respond day: assess = readiness (lead call 14), including a leave-out fallback (days 161, 241) | Band courses |

## For the structure pass

- docs/agents/LEAD-ITEMS (or wherever the gate item lives): "Gate: allow a readiness check on a level's first day" is
  done by lead call 14; close it.
- Source list: add National Weather Service, "Cold Water Hazards and Safety", https://www.weather.gov/safety/coldwater
  (free, opened 2026-11-26): cold shock and hypothermia, advice for the person in the water (from the expert read's
  For the source list). A rescue-teaching source (a national lifesaving body's page) is still needed before unit 11's
  plan; the safety agent names it.
- Browser check at grade close: the IOC history page and the National Football Museum's 1863 laws page (unit 9).
- The scope's remaining For the lead item (Fluency share below a third in product units) stays for the lead.

## For Cory

- Nothing.

## Gates

- `python -X utf8 scripts/sequence.py check physical-education-grades-9-to-12`: 0 failures; 12 notes "standard None is
  on no day" for units 13 to 24 (call 12, left).
- `python -X utf8 scripts/frame.py check physical-education-grades-9-to-12`: 0 failures; notes: 74 unit days a year,
  24 units, 320 days (296 in units, 24 for checks and respond days).
- `python -X utf8 scripts/frame.py calendar`: no PE 9 to 12 lines; no frame change here moves a day or week.
