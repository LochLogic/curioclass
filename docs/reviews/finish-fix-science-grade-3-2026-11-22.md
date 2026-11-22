# Finish fix: science-grade-3 (2026-11-22)

Course finish, COURSE-RUN stage 7, one fix pass over ten fresh-reader reports. Each report now ends with a "Fixes applied (2026-11-22)" section, one line per finding.

## Counts per report

| Report | Applied | Rejected | Left |
|---|---|---|---|
| Answer key, unit 1 | 8 and 2 smaller | 0 | 0 |
| Answer key, unit 2 | 8 | 3 (two part relabels, the "x" code) | 0 |
| Answer key, unit 3 | 13 | 0 | 1 (old source dates, for the lead) |
| Answer key, unit 4 | 4 and 2 minor | 0 | 0 |
| Answer key, unit 5 | 6 | 0 | 2 (For Cory) |
| Answer key, unit 6 | 4 | 0 | 0 |
| Answer key, course checks | 11 and 3 minor | 0 | 2 minor (fine as written) |
| Safety | 15 of 15 | 0 | 0 |
| Sensitivity | 3 medium, 4 low | 0 | 1 low and 2 could-not-settle (For Cory) |
| Cold read | 6 (findings 1, 4, 9, 10, 12, 15) | 0 | 9 |
| Part E, US spelling | 157 words in course files, 34 items.csv cells | | |

New item: s02-P29-13 (the light-pull user criterion) so that s02-E5's third point has printed work behind it.

## Safety page

courses/science-grade-3/safety.md, 887 words: the stop rule, eye protection and its Z87.1 impact rating, hand washing, allergies (latex, foods, pollen, mold and dust), plants, seeds, soil and the mold rule, the mealworms, outdoor looks and adult ratios, the weather record and the sun, heat and lamps, electricity, magnets and small parts, glass, clean-up, each with its days. Named in docs/courses/science-grade-3/DEFAULTS.md. Sources: G5 (NSTA elementary safety, reread 2026-11-22), G69 (CDC mold), G70 (CDC animals), G71 (CPSC magnets, browser check).

## Gates (filtered to this course)

- plan.py check: before 21 FAIL, after 21 FAIL, all "section N.N (science-grade-3-uNN-N) is not in data/units.csv" (known). Items 874 to 875.
- lesson.py check: before 0 FAIL lines; after 0 FAIL lines (387 lines, every day 0 failures).

## For Cory

1. **Scoring design (cold read finding 2; unit 5 answer key "could not settle").** Only revised earlier products are scored; the fresh check days (32 minutes) score nothing. Options: (a) keep as is and say plainly in each unit plan that the score measures work after feedback; (b) score the fresh check-day work on the same sheets and record the revised products beside it as repair evidence; (c) score both, fresh work as the unit score and revision as a separate repair mark. My pick: (b), because it records what a child does alone on a new case.
2. **One change per revision (unit 5).** A child with three "not yet" marks can recover only one. Options: (a) keep one change; (b) allow one change per marked component; (c) keep one change but score only the components the feedback touched. My pick: (b).
3. **Feedback load (cold read finding 3).** 3 minutes a child twice a unit, papers due back the next day. Options: (a) one six-tick look-for checklist and one question stamp, 1 minute a child; (b) keep full notes but return scored fresh papers one day later, in day 98's Return slot (and the matching days in units 2 and 4); (c) both. My pick: (c). No wording changed here, since every return window ties to the scoring choice above.
4. **Day 82, a family that sees Earth's age differently (sensitivity L3).** Options: (a) add the report's line ("People bring different ideas. In science class we look at what the rocks and fossils show."); (b) get an outside read first, since no science teachers' body's page opened; (c) leave day 82 as is. My pick: (b).
5. **"Utqiagvik" or "Utqiaġvik" in student text.** The borough's own pages use the plain form. Options: keep the plain form (my pick), or teach the community's letter.

## For the lead: sweep

- s02.md interaction score and lid brief disagreed with the printed day 29 records (section plan stage); s02.md now matches the days.
- s03.md section 4 readiness table described cards never printed (section plan stage); fixed.
- u05-1.md anchor said "ferns and palms", which G42 does not state (section plan stage); fixed.
- Error registers in s01 to s05 rest on memory (unit plan stage, cold read 6).
- s05.md section 3 still says no day 81 Tomorrow line exists (unit plan stage, cold read 8).
- No course check returns to 3-LS4-2 or 3-LS4-3, and 3-PS2-4 gets only a respond day (scope stage, cold read 5).
- data/units.csv lacks the 21 sections (data, cold read 7).
- sources.csv G12 and G14 to G18 carry checked: 2026-11-19 (unit 3 key read).
- Ledger: no entry change needed from this pass.

## Left

- Cold read 11 (a second static case): days 19 to 21 and 31 sit at their 675-word caps and it is a section plan addition; days 23 and 29 already add the balloon and the rubbed straw.
- Cold read 13 (day 97 groups): a section-plan routine shared with day 98 in unit 6.
- Cold read 14 (living records start inside unit 2): section plan stage.
- Cold read 2 and 3: For Cory above.
- UK spellings in plan docs outside the course folder (s05.md and others): fix when next edited.

## Browser check

- https://www.cpsc.gov/Safety-Education/Safety-Guides/Toys/Magnets (403): the safety page and the magnet row say small strong magnets are dangerous if swallowed. sources.csv G71.
