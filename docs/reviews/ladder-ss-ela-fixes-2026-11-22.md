# Social studies and ELA ladder run: sample fixes (2026-11-22)

Cory, 2026-11-21 (Desk q-ladder-ss-ela-1): fix the 95 sampled FIRM faults now, as with science, plus the L99 must-fix
items. One fresh Sonnet fix agent per course verified each finding in the 16 sample reports, then applied it at its
cause or rejected it with a reason. Each course's record is the "Fixes applied (2026-11-22)" section appended to its
two reports, docs/reviews/ladder-sample-COURSE-{a,b}-2026-11-21.md.

Provenance tags: MEASURED (gate output, token log), REPORTED (the fix agent's own count, spot-checked by the lead).

## FIRM findings

| Course | FIRM | Result (REPORTED) |
|---|---|---|
| Social studies K | 9 | all applied |
| Social studies grade 1 | 12 | all applied |
| Social studies grade 2 | 12 | applied; day 15 imprint and timing partly (15A stays provisional) |
| Social studies grade 3 | 15 | applied; day 88 Q3 and day 17 nation passage partly (made-up cards stand in) |
| ELA K | 10 | applied; day 134 goal and day 153 key partly; one rejected (car and fork only heard before) |
| ELA grade 1 | 15 | applied; day 92 partly; two rejected (a teacher model, a case that is in fact new) |
| ELA grade 2 | 8 | all applied |
| ELA grade 3 | 14 | all applied |

The short SOFT fixes in files already being edited were applied too. The rest are listed as left in each report.

## Follow-ups the lead sent back

- **Sources (every course).** Agents were sent back until no fact rested on Wikipedia or a search summary. Solid
  replacements were opened and recorded "checked: 2026-11-22". A fact no solid page could support was cut:
  - social studies grade 1: Lincoln's term dates; the Wickquasgeck and Broadway claim on day 49;
  - social studies grade 2: the "about 14 times" Greenland figure;
  - ELA grade 3: the New Mexico 1956 bookmobile start.
  ELA grade 3 day 19 is settled as April 1905, from two library and government pages.
- **Sensitivity.** Social studies grade 3 day 43's new exit had used "a made-up nation" with a Chief, on a Menominee
  government day. It now uses a made-up town with a council and a mayor, and has a hand-back row.
- **ELA K day 134.** The goal was widened to "ask a question about a detail" only after a model and pair practice
  were added to the day.
- **ELA grade 2.** The key moves pushed 31 Before class and page caps over (MEASURED by the lead's own gate run; the
  agent had reported 0). They were sent back and tightened; the count is back to the known 2 (days 94 and 95).

## Must-fix before live (L99)

1. **ELA grade 1 tales:** a fresh sensitivity read is done (docs/reviews/sensitivity-ela-g1-tales-2026-11-22.md).
   No must-fix for g1-u2-03. For g1-u2-04, the Wikipedia citation is out and two sources are in its row: the
   Shanghai city government page and a library page. All its Should-fixes are applied.
2. **Key lines in child pieces:**
   - Moved to teacher key pieces: social studies K 12, grade 1 1, grade 2 3, grade 3 9; ELA K 1, grade 2 33,
     grade 3 4 (REPORTED).
   - Left, judged not child-facing or not answer keys: map legends ("KEY (print this box)"), teacher-read cards,
     "key point" wording.
   - The lead's rescan finds 27 such lines left, all in those groups (MEASURED).
3. **Maathai:** the lead opened the Nobel Prize facts page, which states she "was the first African woman to receive
   the Nobel Peace Prize". The line is restored on page 9 of gk-u4-03 with a new row, nobel-maathai-facts. The nursery
   steps now rest on Goldman Prize and World Bank pages.

## Ledger

The lead applied nine `ledger.py note` changes the agents reported (-less, long and short vowels, busy, the day 134
goal, two exit cards, the day 25 skill, day 41 "who made it", President). Both ledgers check with 0 problems
(MEASURED).

Not applied, for L87, because no row exists to note: ELA grade 3 days 75 and 90, and the ELA K day 117 exit case.

## Gates (MEASURED, lead's run after all fixes)

| Course | plan.py FAIL | lesson.py FAIL |
|---|---|---|
| Social studies K | 19 | 2 |
| Social studies grade 1 | 26 | 19 |
| Social studies grade 2 | 25 | 8 |
| Social studies grade 3 | 48 | 40 |
| ELA K | 35 | 15 |
| ELA grade 1 | 41 | 0 |
| ELA grade 2 | 310 | 2 (after the cap fixes) |
| ELA grade 3 | 45 | 10 |

Every count equals its course's before count. All are known template points, or
"not in data/units.csv".

## Cost

About 1.89M agent tokens for the eight fixers and the tale reader (MEASURED, token log rows "samplefix").

## Process notes

- Agents again reported gate counts that missed failures they caused (ELA grade 2). The lead's own filtered run
  remains the check.
- A social studies grade 1 agent typed git once, read-only, and reported it.
- Several agents could not run the unfiltered gates while another agent's CSV was mid-edit. They used per-course
  wrappers in their tmp folders.
