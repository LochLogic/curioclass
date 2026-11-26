# Fixes: Social and Emotional Learning, Grades K to 2 frame (2026-11-25)

One fix pass (COURSE-RUN stage 3) on docs/courses/social-and-emotional-learning-grades-k-to-2/frame.md, from the expert read (docs/reviews/frame-social-and-emotional-learning-grades-k-to-2-2026-11-25.md, 15 findings) and the Codex read (docs/reviews/frame-social-and-emotional-learning-grades-k-to-2-codex-2026-11-25.md, 8 findings). Files changed: the frame, data/progressions/sel.csv, docs/courses/sel/STANDARD.md, docs/courses/sel/APPROACH.md, and frames.csv, calendar.csv and CALENDAR.md through sync.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 66 courses; calendar.csv 962 rows |
| `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-k-to-2` | 0 failures (18 units, 192 days: 180 in units, 12 check and respond days; 60 unit days a year) |
| `python -X utf8 scripts/progression.py check sel` | 520 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files, 0 failures |

## Findings

21 applied (three of them in part), 2 rejected.

| Read | # | Verdict | What changed, or why not |
|---|---|---|---|
| Expert | 1 | Applied | Health seam rewritten from the written health K to 2 frame: real units and weeks, who teaches first, what the second does. SEL grade 1 unit 9, unit 12 and grade 2 units 16 and 17 now open with health's earlier step as retrieval where the school runs health, and teach it where it does not. New "Shared steps" in STANDARD section 7. Health-side edits are the lead's (For the lead 4). |
| Expert | 2 | Applied | New "Inside the 20 minutes" bullet: about 4 minutes opening (retrieval inside it), 13 teaching, 3 close; at most three new sub-skills per Understanding session; unit 2 group 3 gets two Understanding sessions. APPROACH field 4 notes the shorter K to 2 opening. |
| Expert | 3 | Applied | Departure kept; the case and a pick are under For Cory below. Other bands decide their sizes from their minutes with the same rule. |
| Expert | 4 | Applied in part | Checks relabeled mid-year and year-end; unit 6 of K and grade 1 is sampled by the next year's mid-year check (items named); grade 2 unit 18 hands on to grade 3 readiness. Moving the year-end check to week 32 is Cory's call (For Cory). |
| Expert | 5 | Applied | RS3 at grade 2 (unit 18 and its row): an invented partner from another place brings one sourced way of sharing work, shown as one child's way. |
| Expert | 6 | Applied | SA2 (unit 17): an invented bilingual teammate models the culture and language strength. SO7 (unit 13): the chance a situation offers is taught beside what it asks. Rows and grade 3 note updated. |
| Expert | 7 | Applied | New "Leave-out" bullet: a later unit that uses a left-out unit's card teaches its one-step form in the first ten minutes and claims none of its sub-skills; cards and the units that need them listed. Rule added to STANDARD section 5 item 6. |
| Expert | 8 | Applied | Evidence bullet: the end-of-unit rehearsal is seen across the last Application and the Check session; short path and private rehearsal options named. |
| Expert | 9 | Applied | Safety bullet names the CPSC public playground safety handbook for the movement games. |
| Expert | 10 | Applied | One I-statement: "I feel ___ when ___. I need ___." (health kindergarten's words) in K to 2; grade 2 adds "What do you need?" and a fair end; grade 3 adds "because". Frame units 9 and 15, sel.csv rows g1 to g3, APPROACH field 9. |
| Expert | 11 | Applied | Unit 11 now plays acchi muite hoi, the game the class does not know, taught by the friend (Japan Foundation, Erin's Challenge lesson 7, read 2026-11-25; the Web Japan page is a browser check). Ampe kept in kindergarten with its sources under Base text; the PE grade 1 repeat is the lead's pick (PE swaps). |
| Expert | 12 | Applied | Kindergarten units 2, 3, 5 and 6 name their retrieval (unit 2: none, with the reason). |
| Expert | 13 | Applied | New "Evidence base" bullet: no study stands behind this course; logic model pointer. |
| Expert | 14 | Applied | Stale lines gone: "being written now", "check 1/2", the old For the lead list; STANDARD intro and section 2 now say frames are written from 2026-11-25, one band frame with a Year column, scope one year at a time; "catalogue" and "behaviour" made US spelling. |
| Expert | 15 | Rejected | The brief says do not move check weeks for after-core clashes. Clashes listed below for the lead's calendar pass. |
| Codex | 1 | Rejected (labels applied) | Moving the checks to the year's middle and end would put them in core check weeks (K 14 to 18 and 29 to 32, grade 1 14 to 16, 19 and 29 to 32, grade 2 14 to 20 and 28 to 32; calendar.csv), which the course-run rule forbids. Kept after units 2 and 5, labeled mid-year and year-end, with unit 6 sampled next year; Codex's three-a-week option is option (c) for Cory. |
| Codex | 2 | Applied | The three exact fixes (SA2 unit 17, SA5 values in unit 14 with an unseen item, RS3 sourced partner in unit 18) and the matching sel.csv notes. |
| Codex | 3 | Applied | Same as expert 7 (Leave-out bullet and STANDARD rule). |
| Codex | 4 | Applied in part | AASL codes cannot go in sel.csv standard cells: progression.py fails ("not in the standards files"; tried and reverted). They are named in the grade 2 owner rows' notes, in units 14, 17 and 18 and the Standard bullet with a Pending note; validator support is For the lead 3. |
| Codex | 5 | Applied | Same as expert 1, plus the shared model in STANDARD section 7. |
| Codex | 6 | Applied | No "carried unchanged": a check records only newly sampled evidence; unit sheets thrown away at unit end, a check's sheet kept only to its respond session. |
| Codex | 7 | Applied | Game sources named under Base text; the "no ritual meaning" claim removed. |
| Codex | 8 | Applied in part | STANDARD and the frame fixed. The ADOPTION-BAR-SUBJECTS SEL row is not a file this pass may edit (For the lead 11). |

## Pattern notes for the other SEL frames

- Fit both course-level checks inside 64 sessions, after units 2 and 5 or wherever the core check weeks leave room, and say how the last unit is sampled.
- Budget the session minutes in the frame; cap new sub-skills per Understanding session to what the minutes hold.
- Owner-year rows must teach every part of the code (culture in RS3 and SA2, chance in SO7, values in SA5).
- Cite STANDARD section 7 "Shared steps" and the written health and PE frames' real units; never "being written".
- List leave-out bridges; name every unit's retrieval; cite game sources at frame time; pick a game the class does not know.

## Left for the lead

1. AASL ids: scripts/progression.py and scripts/frame.py accept AASL.V.D.1, V.D.2 and III.D.2 for SEL rows.
2. Health K to 2: listening card opens with the talk turn card's steps; I-statement, refusal second push and goal rungs cite STANDARD section 7; health rows gain cross_subject leans to SEL.
3. PE K to 2: Ampe repeats in grade 1 unit 14 (pick: PE swaps in another Ghanaian game); calm card picture in grade 1 unit 11; goal rungs in K unit 6 and grade 2 unit 16.
4. Spanish family notes need a translation read brief.
5. Band "k-2" is outside frame.py's K to 8 clash check; weeks placed by hand.
6. DESK-ANSWERS log lines: shared steps, "I need" wording, leave-out bridge rule.
7. ADOPTION-BAR-SUBJECTS SEL row's stale owed clause.
8. After-core check clashes (SEL not moved):
   - Week 26, K, 1 and 2: SEL year-end check with visual arts' year-end check.
   - Week 27, grade 1: SEL respond with health's year-end check.
   - Week 27, grade 2: SEL respond with health's, PE's and English language development's year-end checks.
   - Week 11, grade 2: SEL respond with health's mid-year check.

## For Cory

1. **Unit sizes (scope).** q-fix-sel-1 set units of 11 and 10 (short path 5 and 6), which fills all 64 sessions and leaves none for the mid-year and year-end checks the 2026-11-25 rule requires. This frame uses 11 and 8 (kindergarten 12 and 8; short path 5 and 5, kindergarten 6 and 4, plus 2 for checks), freeing 4 sessions a year. Each group still gets Understanding, Fluency and Application. Alternatives: 68 sessions a year, or fold the checks into unit Check sessions (no separate check). Pick: accept for K to 2, and let each other band set its sizes from its minutes under the same rule.
2. **Year-end check placement (scope).** Core check weeks fill weeks 28 to 32, so the year-end check sits after unit 5 (week 26) and unit 6 is sampled by its own assessment and next year's mid-year check. Options: (a) allow week 32, shared with core checks; (b) as now; (c) three sessions in some weeks. Pick: (b).
3. **Supply ceiling (money).** About $55 to $60 a year printing plus about $21 once, for 30 children; no ceiling is set. Pick: set none until the first unit plans price it.
