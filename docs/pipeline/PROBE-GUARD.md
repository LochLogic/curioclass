# The probe and the guard: what counts as on and off (pre-work P4)

Written 2026-11-13 for docs/PRODUCTION-PATH.md P4, before any plan is written, so no result is judged by a line
drawn after seeing it. Shown to Cory on the Desk (card q-probe-guard) before the first probe runs.

## In short

After a subject's units are planned, write a few real days from them and count how often a problem on a day had
to be fixed in the unit plan or above. A quarter is where the old grade 4 math plan stood. A fifth or less means
the plans are good; more than a third means fix the plans before going on. Two smaller checks ask whether the same
fix is needed in many units and whether the unit template itself must change. When: the probe runs after each
subject's units are planned (social studies first, after baseline 1 and before baseline 2); the guard runs once
every subject's units are planned, before full writing.

## What is measured

The **probe** (PRODUCTION-PATH step 4, and each subject in step 5) writes one section, 3 to 5 days, from a subject's
new unit plans and reads it the full way (writer, cheap read, expert read, fix, re-read). The **guard** (step 7)
does the same in every subject once all units are planned, before full writing. Both ask one question: were the
plans good enough to write from?

Every finding on a probe or guard day is logged in data/plans/defects.csv as now (layer `day`), and the reader
who fixes it adds its **origin**: the highest layer that had to change for the fix to hold. The origin goes at the
start of the `ref` cell as `origin=<layer>;` so the ledger keeps its columns.

| Origin | Meaning |
|---|---|
| day | Fixed inside the day; no plan file changed |
| section | The section plan changed (its days, minutes, examples) |
| unit | The unit plan or its cross-day files changed (hand-backs, materials, reserved examples, items, source map) |
| scope | The course's scope and sequence changed (a day moved, added or cut between units) |
| frame | The course frame or the progression changed (a topic moved between grades, a standard re-placed) |
| template | The unit or day template, a brief or a gate changed, so every later unit or day changes too |

## The three measures and their lines

**1. Plan share.** Findings with origin unit, scope, frame or template, as a share of all findings on the
probe's days (rejected findings left out).

- Baseline (MEASURED, 2026-11-13): grade 4 math days 25 to 28, written from the old unit 4 plan, had 51 findings;
  13 (25%) were cross-day or sent back to the plan (kinds sequence, hand-off and minutes, or naming another day).
  That count was made after the fact from kinds and wording, so it is a rough line, not an exact one. The re-plan
  of days 29 to 38 then caught 9 such problems in its own 10 days at planning time, which is what better plans
  should do.
- **On: 20% or less** (better than the old plan, as the re-plan should be).
- **Watch: over 20% and up to 35%.** Read the plan-origin findings; decide by measures 2 and 3.
- **Off: over 35%** (clearly worse than the old plan).
- Separately, **any finding with origin frame** is reported to Cory whatever the share, because it moves content
  between grades.

**2. Unit plans changed.** After the probe's fixes, the lead checks each plan-origin finding against the subject's
other unit plans (one read for the same fault, not a full re-read). Count the unit plans that need a change.

- **On: the probed unit only, or 10% or fewer of the subject's units.**
- **Off: more than 25% of the subject's units.** In between is Watch.

**3. Template or one unit.** Does any fix change the unit template, a brief or a gate?

- **On: no template change, or small ones only** (a field, a rule line, a gate check added), made once at baseline
  2 before the next subject copies the template.
- **Off: a change to the template's shape** (a section added or removed, a required table changed). At the guard,
  any template change is Off, because every subject has already used it.

## What each result leads to

| Result | At a probe | At the guard |
|---|---|---|
| All on | Baseline 2 (or the subject's closing review) as planned; the next subject starts | Full writing starts |
| Any watch, none off | The lead reads the plan-origin findings and records a call in the probe report: go on, or fix the units it names first | Same, and the call is noted on the Desk |
| Any off | The subject's units are corrected (and the template, if measure 3), then one more probe section before the next subject | The units are corrected before full writing; a second guard section is written after |

## Where the numbers go

Each probe and the guard gets a short report in docs/reviews/ (`probe-<subject>-<date>.md`, `guard-<date>.md`) with
the three measures, their bands and the findings counted. The lines here are not moved after a probe has run;
if they prove wrong, the change is recorded as a new version with its reason.

## Known limits

- Three to five days give 30 to 60 findings, so a share is only good to about 6 points either way. Measure 1's
  Watch band is wide for that reason.
- The baseline is one math unit. Social studies days may raise different findings; the first probe is also the
  first reading of what a social studies day costs to fix.
- Measure 2's "one read for the same fault" is the lead's judgment, not a gate.
