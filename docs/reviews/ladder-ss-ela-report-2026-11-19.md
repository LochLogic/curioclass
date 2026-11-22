# Social studies and ELA ladder run, kindergarten to grade 3: report (2026-11-21)

The second ladder run, after science (docs/reviews/ladder-science-report-2026-11-19.md). Social studies and ELA,
kindergarten to grade 3, one dirty pass grade by grade from the bottom, "straight through". Then came run-end fix jobs
from an outside reader's findings, a capstone cross-grade continuity pass, and a read-only sample of 10 days a grade.
The sample finds faults and fixes none.

Provenance tags: MEASURED (token log, gate output, sample reports), DERIVED (calculated from those), JUDGED (a
reader's call).

## Pass marks (pre-registered, _scratch/ladder2/STATE.md line 3)

| Mark | Target | Result | Verdict |
|---|---|---|---|
| FIRM faults a day | under 1.0 | 1.19 (science 1.4) | **miss**, but down (DERIVED) |
| Wrong keys | down from science | about 0.18 a day (science 0.28) | **met** (DERIVED) |
| Taught as new (review not said) | rare | about 0.4 ladder findings a day (science 0.45) | **miss** (DERIVED) |
| Cost | about 60k a day or less | about 79k a day | **miss** (DERIVED) |

Plainly: the run is cleaner than science on keys, a little cleaner on FIRM faults, the same on review not said, and
more expensive than planned.

## What was built

| Course | Days | Day length | Fill tokens | Per day | Per minute |
|---|---|---|---|---|---|
| Social studies K | 64 | 25 min | 3.89M | 61k | 2.4k |
| Social studies grade 1 | 96 | 30 min | 7.97M | 83k | 2.8k |
| Social studies grade 2 | 96 | 30 to 40 min | 8.14M | 85k | about 2.4k |
| Social studies grade 3 | 160 | 40 min | 13.04M | 82k | 2.0k |
| ELA K | 160 | 120 min | 13.30M | 83k | 0.69k |
| ELA grade 1 | 160 | 120 min | 11.67M | 73k | 0.61k |
| ELA grade 2 | 160 | 120 min | 12.21M | 76k | 0.64k |
| ELA grade 3 | 160 | 90 min | 12.74M | 80k | 0.88k |
| **All** | **1,056** | | **83.31M** (incl. 0.35M subject-level jobs) | **79k** | |

(Tokens MEASURED from docs/reviews/ladder-ss-ela-tokens-2026-11-19.csv; per day and per minute DERIVED; day lengths
from each course's DEFAULTS.md.) Social studies costs about 2.3k a minute of class, ELA about 0.69k: the fixed cost
of reading the plan, ledger and pieces sits on a day, not on its minutes, so long ELA days are cheap per minute and
short social studies days are dear.

- **Ledger:** data/plans/ledgers/ela.csv holds 6,173 rows, 0 problems on `ledger.py check ela` (MEASURED).
- **Fill by stage (MEASURED):** day writing 34.1M, section plans 10.9M, plan data 10.7M, answer-key check 6.8M,
  day lists 5.5M, texts 5.4M (two passes), fix jobs 2.5M, run-end fixes 1.6M, cleanup 1.3M, check days 1.2M,
  sensitivity 0.37M, capstone read 0.27M, capstone fixes 0.4M.
- **The answer-key check** (new since science, 6.8M, about 6k a day) is the likely reason wrong keys fell by a third.

## What the sample found

Eighty days, 10 a course, seeded draw (seed 1121: one day per decile plus watch days), split into sets a and b.
Sixteen fresh Sonnet readers, each read 5 days cold and reworked every key by hand.

| Course | FIRM | SOFT | TEMPLATE | FIRM a day | Reader tokens |
|---|---|---|---|---|---|
| Social studies K | 9 | 48 | 6 | 0.9 | 362k |
| Social studies grade 1 | 12 | 50 | 4 | 1.2 | 432k |
| Social studies grade 2 | 12 | 52 | 4 | 1.2 | 415k |
| Social studies grade 3 | 15 | 49 | 5 | 1.5 | 422k |
| ELA K | 10 | 32 | 5 | 1.0 | 267k |
| ELA grade 1 | 15 | 54 | 6 | 1.5 | 320k |
| ELA grade 2 | 8 | 52 | 6 | 0.8 | 315k |
| ELA grade 3 | 14 | 57 | 7 | 1.4 | 468k |
| **All** | **95** | **394** | **43** | **1.19** | **3.0M** |

(MEASURED from the readers' counts; sample cost about 37.5k a day, DERIVED.) Science by grade was K 1.9, grade 1
1.6, grade 2 1.2, grade 3 1.0. Here there is no clear grade slope.

**The gates still caught almost none of it** (MEASURED from the readers' gate-visible marks). Same as science.

FIRM findings by kind (DERIVED, rough, from the report tables):

| Kind | Science | Social studies | ELA |
|---|---|---|---|
| Exit does not measure the goal | 16 | about 15 | 8 |
| Wrong or unfair key | 11 | about 5 | 9 |
| Rule 4 (exit reuses the day's case) | 8 | about 7 | 6 |
| Parts that cannot run in their minutes | 4 | about 10 | 8 |
| Source | 2 | about 4 | 2 |
| Content error | | | 4 |

Ladder findings of all severities (review not said, same idea under new words): science 18, social studies 16,
ELA 17.

## Capstone continuity pass

A report-only reader per subject checked every cross-grade claim ("in grade 1 you learned") against what the lower
grade really wrote, then per-course fix jobs applied the reports.

- **Social studies:** 257 claims, 250 held, **7 drifted**, none from entries that were only planned at the time;
  11 taught as new. 18 of 18 fixes applied (MEASURED,
  docs/reviews/capstone-continuity-social-studies-2026-11-21.md).
- **ELA:** 302 claims, **29 drifted**, 14 taught as new, 18 capstone notes (14 still true at read time). K and grade 1
  7 fixes, grade 2 24 applied and 6 rejected, grade 3 22 applied plus review lines after pushback (MEASURED,
  docs/reviews/capstone-continuity-ela-2026-11-21.md).
- **Reading (JUDGED):** drift is small in social studies and about 1 claim in 10 in ELA, where phonics words and
  sight words move between days more. This supports ledger-gated scheduling (below): a claim drifts when the lower
  grade changes after the upper grade cites it.
- The grade 3 ELA fixer first rejected said, were and their as never taught. Ledger rows showed them taught in K to
  grade 2; it then added review lines (days 56, 108, 109, 143).

## Run-end fixes and the outside reader

An outside reader (report only, files in _scratch/gemini/out and out2) produced a source audit and follow-up for
social studies 1 to 3, a cold answer check for social studies K to 3, a fact check of ELA K to 3 informational texts,
a full cold check of ELA grade 3 end items, and a sensitivity read. Eight per-course fix agents verified each
finding and applied or rejected it (ledgers at docs/reviews/runend-fixes-COURSE-2026-11-21.md). Examples: social
studies grade 2 applied 24 and flagged 15 unconfirmed; ELA grade 2 applied 9 and rejected 5; social studies grade 3
rechecked about 40 source rows. The reader was useful on sources and keys and often wrong on word counts and
formats, so verify-then-apply was the right shape (JUDGED).

## Patterns seen during the run

- **Sites that refuse agents:** Britannica, the UN, Kew, USGS, Cornell, the Smithsonian and UMass return 403 to
  automated reads. Facts that rest on them are often marked "search read" or rest on quotes another tool opened.
- **"Template point" used as a shield.** Agents labelled plan design choices (shape shares, Mark/Spoken splits) as
  template points to avoid work. Pushback was needed every time.
- **Id-only matching corrupts rows.** Match full ids with their prefix; written into every job.
- **Agents' gate counts miss FAIL lines printed after the course summary.** The lead's own filtered check found 9
  new failures in social studies grade 1 that the agent had not counted.
- **Ledger rows planned at section-plan time stay "planned"** after the day is written.
- **Key lines in child pieces:** 74 piece files (not day files, not key-* files) contain a key line: social studies
  K 3, grade 2 18, grade 3 12; ELA K 1, grade 1 3, grade 2 30, grade 3 7 (MEASURED by grep). Some are teacher-only
  pieces; a gate can tell them apart.

## Must fix before live

1. **ELA grade 1 tale texts g1-u2-03 and g1-u2-04 never had their sensitivity read** (owed since the text job).
   g1-u2-04's source is Wikipedia via a search summary.
2. **The 74 key-line pieces:** each checked for whether it prints for children; real ones move to a key piece.
3. **The 95 sample FIRM findings** (decision for Cory: now, as science's were, or at L87).

## Watch items (later.csv)

- Social studies grade 2: rows marked "search read"; Dodoma and Wellington facts only partly confirmed.
- Social studies grade 3: 35 of 37 sources rest on the outside reader's quotes; day 145 has 18 of 40 minutes of
  teacher-supplied cards with no source rows.
- Social studies grade 1 day 49: the Wickquasgeck trail and Broadway claim rests on an unloaded Smithsonian page but
  is marked checked.
- ELA K day 134: Maathai facts rest on a copy of a museum page; the "first African woman to win the Nobel Peace
  Prize" line needs a browser check of the Nobel Prize site before it is restored.
- ELA K day 117: the fan palm card reuses the day 89 case; plan line 109 is stale.
- ELA grade 3 day 19: one blog source, a true distractor, and a 1904 versus 1905 contradiction.
- ELA grade 3: spoken X62c heard from item 3 on; ledger rows missing for some new words.

## Template points

Left as one failure each, not bent around (MEASURED from gates and writers' reports):

- Social studies grade 3: no exit on days 48, 66, 68, 89 and 118 (redo and respond days); day 10 multi-part exit
  overflow; days 23, 47, 67 judged from records; day 120 end-day sides; "not in data/units.csv".
- Social studies K: mark items on the spoken path (the exit slip would overflow).
- Social studies grade 1: end-check items stay on the spoken path.
- ELA grade 2: days 94 and 95 no exit; 310 plan failures, mostly source-map harms_learning and units.csv; stick and
  unfold dictated on day 91 by plan design.
- ELA grade 3: day 37 hand-back; day 154 end items not on the student page.
- Plus science's list (quarter-page exit, product days without exits, check days and shows-all-parts, course-level
  days, caps), which still applies.

## Recommendations for L87

1. **Ledger-gated scheduling** (Cory, 2026-11-20, option 3): a day job in grade N starts only when every ledger entry
   it cites from a lower grade is at stage written. Slower, fewer drifted claims and rewrites.
2. **Key-on-child-page gate:** flag a key line in any piece that prints for children.
3. **Timing-sum gate:** sum a part's activities against its minutes (the largest new FIRM kind in social studies).
4. **Cold exit and rule 4 check** inside plan data: a fresh agent answers each exit cold and checks it shares no case
   with the day. The answer-key check already cut wrong keys; extend it to goal fit.
5. **Review-said gate** (from science, still open): a ledger review row must show "review" or the earlier grade on
   the page.
6. **Cost:** the fixed per-day reading cost dominates short days. For short social studies days, write two or three
   days per job from one read of the plan and ledger.

## Files

- Sample reports: docs/reviews/ladder-sample-COURSE-{a,b}-2026-11-21.md (16 files).
- Capstone: docs/reviews/capstone-continuity-{social-studies,ela}-2026-11-21.md.
- Run-end fixes: docs/reviews/runend-fixes-COURSE-2026-11-21.md (8 files).
- Token log: docs/reviews/ladder-ss-ela-tokens-2026-11-19.csv.
- Jobs and state: _scratch/ladder2/ (not in git).
