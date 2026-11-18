# Answer-key read: science-grade-5, unit 1, section 1.1 (days 1 to 4), 2026-11-18

Kind answer-key, per docs/pipeline/briefs/sensitivity-read.md. Origins per docs/pipeline/PROBE-GUARD.md.

## What I studied

Nothing outside the repository; the study step for this kind is to solve.
- data/plans/science-grade-5/items.csv (s01-R1, X1, X2a, X2b, X3a, X3b, X4a, X4b; end items E1 and E2 only as the day "shows" cells name them) and wrongs.csv: read the stems first, worked each (the arithmetic, the dot counts, the fair-test choices, the six-piece rebuild) before reading the answer and steps cells.
- docs/courses/science-grade-5/u01-1.md and u01-2.md, courses/science-grade-5/u01-1/ (nine pieces), days.csv, errors.csv, handbacks.csv, s01.md (unit plan row for day 1, fields 5 and 8).
- Honesty note: the section plans were read before the key cells, so the plan's own exit answers were in view while I solved. My own answers matched every item key where a key exists (85-71 = 14 and 71; 58, 60-58 = 2, 86-60 = 26; 9 dots and 8 dots kept; any two of stick, place, sun time). The faults below are in what the items ask, how the pieces agree, and the plan text.

## Verdict

Pass with fixes. The arithmetic and dot-count keys are right, but the day 1 weight test cannot be carried out as keyed, the plan and the data disagree on what two tickets ask, and days 5 to 7 have no keyed items at all.

## Findings

1. [s01-X1 (b), wrongs s01-X1 D, errors D, s01.md day 1 row, opener] The fair test is "weigh the same dry bottle with and without the trapped air", but a bottle cannot be weighed without its air; no classroom can make that weighing, so the key (Plan 1) names a procedure no child can do, and the item does not test the day 1 goal (weigh a ball before and after pumping). | Ask the test on a soccer ball: Plan 1 weigh the ball, pump more air into the same ball, weigh it again; Plan 2 weigh two different balls, one flat and one pumped. Update the key, steps, the D wrong example, errors D, the day 2 hand-back, s01.md, the opener and the plan ticket. | origin=unit
2. [u01-1.md section 3, tickets for days 2 and 4 (and the 1 and 3 wording)] The plan asks "dried thin or weighed wet?" (day 2) and "how should soil, seeds and water be recorded?" (day 4) with prose answers; the items are numeric (85 g to 71 g, answer 14 g and 71 g; 58, 60, 86, answer 58, 2, 26). A teacher following the plan would ask and mark a different question from the one the key and gate check. Ticket 3 also differs (plan has no 9 and 5 dots, asks "how to make a fair comparison" against the item's "name two things"). | Replace the plan's four ticket stems and answers with the items' stems and answers. | origin=section
3. [days 5 to 7, tickets E5, E6, E7 in u01-2.md] They have no rows in items.csv or wrongs.csv, so no key is checked by the gate (plan.py check already fails days 5, 6, 7 for this). The plan answers read right on a cold solve. | Add keyed rows and wrong-answer rows for the three tickets (needs writing the stems into the item schema, which is outside the days 1 to 4 patch). Left open. | origin=unit
4. [records-n1-n4.md N3 against u01-1.md section 5] The record says the syringe goes from 40 mL to 12 mL and the first shadow is 100 cm; the plan says 20 mL to 12 mL and 40 cm. A child's hand cannot press a closed syringe from 40 mL to 12 mL (about 3.3 times the pressure, roughly 9 kgf on a 60 mL plunger), and it asks for a plunger or cap to fail. | Make the record read 20 mL, 12 mL and 40 cm, matching the plan. | origin=unit
5. [readiness-pieces.md heading and last line; opener.md "How the days run" paragraph] Both say day 2 rebuilds the same six card pieces; the day 2 plan, days.csv and the supplies use six large interlocking blocks. | Say day 2 uses six large blocks rebuilt the same way; readiness-pieces serves day 1 only. | origin=unit
6. [u01-1.md section 4 table, rows D, H, J, K; section 8 day 3 warm-up] The table puts the repairs in "day 2's reopen", "day 4's opening" and "day 3's opening". handbacks.csv and errors.csv already place them: D at the start of Rebuild (the plan "reopen" has no part), J and K as two minutes in Squeeze and compare, H as three minutes inside Plant beans. Day 3 has no minutes for the repair or the day 1 reopen the warm-up promises (the parts add to exactly 45). | Move the table rows to the hand-back places; add the two-minute reopen and J or K repair into the first minutes of day 3's 23-minute block. | origin=section
7. [u01-1.md day 4, Plant beans] "Groups confirm the soil is dry" gives no test, but the key weights (dry soil on the log) depend on dry soil, and soil air-dried on a tray for two days may still be damp. | Add the check: crumbly, pale, not sticking to a clean dry finger, else use the prepared dry sample. | origin=section
8. [u01-1.md days 2, 3, 4 against unit plan field 8] Field 8 requires nonlatex gloves for soil and impact protection for compression, but day 3's syringe squeeze names no eye protection, days 2 and 4 name no gloves, and day 4's squeezed bottle is not described as empty and capped. | Add eye protection to the day 3 safety part, gloves to the soil steps on days 2 and 4, and "sealed, empty, capped" to the bottle. | origin=section
9. [items s01-X2a, X2b, X4b; s01-X3b] The four exit rows are coded 5-PS1-1 (matter is made of bits too small to see) but test, in turn, rebuilding six pieces without loss (X2a), subtracting grams to find water (X2b), taring and recording added grams (X4b) and holding a shadow reading fair (X3b); none asks for a particle model. | Recode X2a to s2-pieces-new-object and X2b and X4b to s5-conserve-weight (the frame's own skill codes). X3b has no matching code in the frame and is kept as is, named here. | origin=unit
10. [u01-1.md section 3 and day lines, u01-2.md section 3 and day lines] The plan names the exit tickets E1 to E7, but in items.csv E1 and E2 are the day 16 unit assessment items and the exit tickets are X1 to X4; days.csv "shows" cells then read as if day 1 exits tested the day 16 items. | Name the tickets X1 to X4 (u01-1) and X5 to X7 (u01-2) in the plans, with a line saying so. | origin=section

Count by origin: day 0, section 4, unit 6, scope 0, frame 0, template 0 (10 findings).

## Could not settle

- Whether the two-day tray drying leaves the potting soil dry enough (finding 7 adds a test, not a time). A trial with the real soil is needed before the day 4 key weights are trusted.
- Items for days 5 to 7 (finding 3): to be written by a builder, not patched here.

## Fix

1. Fixed: items X1 stem, answer and steps, wrongs X1 D, errors D (example and if_many), handbacks D, s01.md day 1 row, opener, u01-1 ticket X1 and the D rows now use the soccer-ball test.
2. Fixed: u01-1 tickets X1 to X4 carry the items' stems and answers.
3. Open: X5 to X7 need keyed rows; not written in this patch.
4. Fixed: records-n1-n4.md N3 now 20 mL, 12 mL, 40 cm.
5. Fixed: readiness-pieces.md and opener.md name six large blocks for day 2.
6. Fixed: table rows D, H, J, K moved to the hand-back places; day 3 gets the two-minute reopen and repair.
7. Fixed: day 4 dryness test added.
8. Fixed: day 3 eye protection, gloves on days 2 and 4, empty capped bottle on day 4 added in the plan.
9. Fixed: X2a, X2b, X4b recoded; X3b kept.
10. Fixed: tickets renamed X1 to X7 in u01-1.md and u01-2.md with a naming line.

Count: 9 fixed, 0 rejected, 1 open (10 findings). plan.py check for science-grade-5 matches the earlier 19 known failures; lesson.py check passes on the unit 1.1 pieces.
