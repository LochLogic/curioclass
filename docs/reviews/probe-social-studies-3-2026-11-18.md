# Probe report: social studies, third probe, kindergarten (2026-11-18)

The third probe under docs/pipeline/PROBE-GUARD.md (later.csv L56), and the first kindergarten days ever written.
Scope agreed with Cory 2026-11-17: section plans for units 1 to 3 (days 1 to 30, about half of the course's
section plans so far) and days for units 1 and 2 (days 1 to 19), with our own read-alouds. Codex was out of tokens,
so Claude Sonnet agents wrote and read everything, every reader a fresh agent; Opus coordinated. The first two probes
are docs/reviews/probe-social-studies-2026-11-15.md and probe-social-studies-2-2026-11-15.md.

What was made: 7 section plans (u01-1 to u03-4, with a new section gate in unitplan.py), the course's
DEFAULTS.md, plan data for days 1 to 19 (items, wrongs, errors, materials, handbacks, sources), shared pieces
(openers, family notes, 6 read-alouds with picture sequences, card sets, record and readiness sheets) and days 1
to 19. Reads: section lens reads of all three units, an answer-key read after plan-data (new, from probe 2), an
expert read of each unit, one sensitivity read of both units; a fix pass after each.

## Result: Off on measures 1 and 2, On on measure 3.

| Measure | Reading | Band | Probe 1 / probe 2 |
|---|---|---|---|
| 1. Plan share | 35 of 68 day-read findings (51%) have origin unit, scope, frame or template | **Off** (over 35%) | 60% / 60% |
| 2. Unit plans changed | 13 of 19 early-grade units (68%) share a fault kind found here, leaving out the kindergarten-voice kind | **Off** (over 25%) | 88% / 42% |
| 3. Template or one unit | New values and gates, no shape change | **On** | On / Off |

No finding had origin scope or frame.

## Measure 1: plan share

Source: data/plans/defects.csv, course social-studies-kindergarten, rejected rows left out, one duplicate row (unit 2
expert 6, logged twice for its kind) counted once. MEASURED.

| Read | day | section | unit | template | Plan share |
|---|---|---|---|---|---|
| Expert, unit 1 (25) | 12 | 3 | 7 | 3 | 10 of 25, 40% |
| Expert, unit 2 (25 kept, 1 rejected) | 6 | 3 | 13 | 3 | 16 of 25, 64% |
| Sensitivity, both units (18) | 8 | 1 | 5 | 4 | 9 of 18, 50% |
| **Day reads together (68)** | 26 | 7 | 25 | 10 | **35 of 68, 51%** |
| Answer-key read, before days (24) | 3 | 12 | 9 | 0 | 9 of 24 (not in the measure) |

The answer-key read did its job: 24 key faults were found and fixed before a day was written, where in probe 2 keys
were the largest unit-origin kind (22) found after. The day reads found few key faults.

**Where the unit-origin findings sit.** Not in the unit plans' teaching. They are kindergarten classroom logistics
the plan and data did not carry: which children are heard on which day (a rotating six, a record column for it),
minutes that cannot hold the whole class (day 9 at 20 minutes for 30 children; repair slots stacked on full days;
four questions in forty seconds), pieces named but not made (the day 18 response sheet, three job cards for six
jobs), and story scenes with two actors so the key was unclear. Every unit 1 day moved from 20 to 30 minutes: the
content did not fit 20.

## Measure 2: unit plans changed

docs/reviews/probe-k-measure2-2026-11-18.md: the six fault kinds checked across kindergarten units 3 to 6 and the
grade 1 and grade 2 social studies units (19 units, one read, quotable lines only).

| Kind | Units of 19 |
|---|---|
| G1 spoken stems too long or with words five- and six-year-olds lack | 19 (loosely read for grades 1 and 2) |
| G2 minutes that cannot hold the whole class | 9 |
| G3 observation with no rotation or record column | 4 |
| G4 a piece named but not planned | 0 (no materials rows exist beyond K days 1 to 19, so not testable) |
| G5 mixed marking scales | 4 |
| G6 a story or case with ambiguous roles | 5 |
| **Any but G1** | **13 of 19, 68%** |

The early-grade unit plans were written for older-grade rhythms: minutes, observation and stems are the gap. This
is one rule set for K to 2, not 13 separate faults.

## Measure 3: template changes

All small, none changes the shape of a day or a plan:

- `piece: story` (read-aloud, picture sequence, cards; built as teacher prose).
- Item `path` **spoken**: exits, end items, readiness and lesson rows asked aloud with picture cards, never printed;
  plan.py and lesson.py accept it, the At home view names them in words.
- Teacher prose cap is 15 words a minute of the day's own length on ranged frames (a 25-minute day is 375).
- At home minutes scale for short days.
- Section plans are gated with their unit (unitplan.py: fields, day range, minutes per day, 1,600-word cap).
- DEFAULTS.md per course (kindergarten's holds the day shape; the lead added the At home and invented-cases lines
  from the sensitivity read).

Open template items, all rendering (later.csv): the kindergarten display page shows answers and is blank on spoken
days; student pages need 18pt and picture cues; "Scored from the work you handed in" and the write-nothing line
should stay off a child's page; the record sheet should mark "shown, shown with help, not yet seen" (one marking
language is in place, as 2, 1, 0).

## Back to the builders

| Probe | Expert findings | Repeats | Share |
|---|---|---|---|
| First (US History I 5.2) | 54 | 26 | 48% |
| Second (World History I 3.4) | 65 | 38 | 58% |
| Third (kindergarten units 1 and 2) | 51 | 24 | 47% |

Repeats fell, though kindergarten is far from the earlier courses, so most kinds were new anyway. Sensitivity found 1
repeat in 18. Where this probe's kinds go:

| Kind | Goes to |
|---|---|
| Minutes that cannot hold the class, stacked repairs | Section gate already sums minutes; add a rule line in section-write.md: count whole-class turns (children times seconds) |
| Who is heard which day | Rule in DEFAULTS (K) and the K to 2 frames: a rotating six with a record column, named in the section plan |
| Spoken stems | DEFAULTS (done for K); same line for grades 1 and 2 |
| Pieces named but not made | plan.py: a materials row names a file that must exist by the day's write |
| Ambiguous story roles | section-write.md: one actor per scene, the key names the actor |
| Keys | The answer-key read after plan-data stays: it worked |

## Process notes (for L69 and the next probe)

**Tokens (MEASURED, subagent totals as the harness reports them, docs/reviews/probe-k-tokens-2026-11-18.csv):** 33 agent runs,
5.07M tokens, about 184 agent-minutes.

| Stage | Tokens | Per unit of output |
|---|---|---|
| Section plans: write, lens read, fix, lead fix (3 units, 30 days) | 1.57M | 52k a planned day |
| Plan data, pieces, answer-key read and fix (19 days) | 0.97M | 51k a day |
| Day writing (19 days, 7 agents) | 1.24M | 65k a day |
| Expert reads, sensitivity read and their fixes (19 days) | 1.07M | 56k a day |
| Measure 2 read | 0.22M | |

So a finished kindergarten day cost about 225k tokens end to end (plans to fixed day; DERIVED). Writing is only
29% of it; reading in and reading over is the rest, as the 2026-11-17 note found for the lens pass. Writer agents
that took several days in one run were cheaper a day (the five-day section 1.3 run: 52k a day; two-day runs: 75k
to 90k). Longer runs per agent is the cheapest lever seen here.

**Other notes:**
- Sonnet in place of Codex wrote acceptable days, but every fix pass needed its job spelled out: one fixer handled
  2 of 26 findings until told to do all 26. Fix jobs should name the count to handle.
- The section gate caught real faults (minutes, day ranges) before days were written.
- Skeleton lessons go in docs/pipeline/DAY-SKELETON.md Lessons; writer template points are in the per-day notes
  (docs/reviews/probe-k-writer-points-2026-11-18.txt), summarised above.
- Card files printed their keys, which defeated the answer-key read's cold solve; keys now sit under "Key
  (teacher)".
- data/units.csv lacks rows for sections 1.1 to 1.3 and 2.1 to 2.4 (seven plan.py and lesson.py failures). The file
  is on the lead's blind list, so Cory adds them (later.csv).

## What happens next

The guard says Off: correct the units, then probe again before the next subject. For kindergarten and the early
grades the correction is rules, not rewrites: the K to 2 lines in the table above, then a pass over the 19 early
units for G2, G3, G5 and G6. The days 1 to 19 and the section plans for units 1 to 3 stand as the worked example
for early grades. Section plan u01-1 is on the Desk for Cory's sign-off as the example section plan.
