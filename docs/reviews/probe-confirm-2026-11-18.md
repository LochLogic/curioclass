# Probe report: the confirm probe, ELA grade 11 and science grade 7 (2026-11-18, later.csv L78)

Cory's scope (2026-11-18, "Yes, let's work to the ready skeletons"): after L75 (the gate and skeleton session) and
L76 with L74 (rules, per-band DEFAULTS, unit edits), run one ELA section and one middle-school section with the lean
process, and scale if plan share is 35% or under. ELA had never been probed; grade 7 is the first middle-school band.

Process, as probe 4, with every reader a fresh Claude Sonnet agent:
- one writer per stage;
- no lens read of the section plans;
- one answer-key read that also fixed (after plan data, before days);
- one expert read per course;
- a fix pass that named its count.

What was made:

| Course | Section plans | Plan data and pieces | Days |
|---|---|---|---|
| english-language-arts-grade-11 | u01-1 (days 1 to 5), u01-2 (days 6 to 10) | Days 1 to 5: parts, items, wrongs, errors, words, wordlist, handbacks, materials, sources; readiness, opener, record, family note, Mather excerpt, dictionary entry cards, week words, sheets | d001 to d005 (50 min) |
| science-grade-7 | u01-1 (days 1 to 6), u01-2 (days 7 to 12) | Days 1 to 6, same set; observation, safety and record sheets, scenario cards, particle cards and mat | d001 to d006 (50 min) |

All 11 days pass `lesson.py check` and build. Both section plan sets pass `unitplan.py check`. `stale.py` shows
0 failures, and the day skeleton self-test passes. The only failures left are the known ones: the data/units.csv
lines, and exits not yet in data for later days.

## Result

| Measure (PROBE-GUARD) | ELA grade 11 | Science grade 7 | Line | Probe 4 |
|---|---|---|---|---|
| 1. Plan share of the expert read (rejected left out) | 6 of 13, 46% | 11 of 22, 50% | **Off** (over 35%) | 42%, 50% |
| 2. Other unit plans with a firm mark | 2 of 8 | 1 of 5 | **Watch**: 3 of 13 together, 23% | 6 of 11, 55% |
| 3. Template | small: two gate points, three brief lines | same | **On** | On |

No finding in either course had origin scope or frame. Measure 2 is docs/reviews/probe-confirm-measure2-2026-11-18.md.
11 of 13 units carry at least a weak mark, mostly content notes and reading pace in ELA.

**By the line Cory set, the probe does not clear: plan share is still over 35% in both courses.** Write this down
plainly before the detail below, because the detail is more encouraging than the headline. The detail must not be
read as moving the line.

## What changed since probe 4 (DERIVED, from the finding lists)

**The kinds the L74 to L76 rules aimed at mostly did not come back.**
- No hand-back lacked a slot. The skeleton's Hand-backs section showed no "NO PART NAMED" on any of the 11 days.
- No source stopped a day. Plan data checked sources once (plan-data.md step 4); the ELA texts came from library/ and
  Project Gutenberg.
- Exits were transfers, and the two section writers counted equipment and repair minutes (rule 1: 9 places in
  science, rule 2: 6, rule 5: 12).
- The repeats in science (9 of 22) are mostly minutes: a part that holds more than its minutes on days 1 and 6, and
  one if-many repair route. ELA had 2 repeats of 14.

**What fills the plan share now is the unit's data, written at plan data:**

| Where the plan-origin findings sit | ELA | Science |
|---|---|---|
| Item keys, stems and wrong answers in items.csv (after the answer-key read had fixed 13 in each course) | 3 | 5 |
| Shared pieces (a sheet that described itself instead of being a sheet) | 0 | 1 |
| Supplies in materials.csv (goggle cleaning) | 0 | 1 |
| The unit plan's own prose | 3 (content notes, a word's two senses, terms drifting on a reused passage) | 2 (a 0.7 g change on a 1 g scale, an if-many repair route) |
| Template (gate points) | 0 | 2 |

So the share is Off for a different reason than before. In probes 1 to 4 the unit plans could not be run in a
classroom (slots, equipment, hand-offs). Here they mostly can. The faults now are item keys that two reads still
had to catch.
- **ELA:** a key took the wrong referent, called a stated fact "implied", and leaned on later events.
- **Science:** items said the solid itself escapes, where the particles do.

Counted on unit-plan prose plus template alone, the share would be 3 of 13 (ELA) and 4 of 22 (science). That
recount is not the measure Cory set, and this report does not use it to decide.

## The rules round (done after the result, as probe 4 said: the remaining kinds go into the rules)

- **docs/pipeline/briefs/section-write.md:**
  - two extensions in science: a reading inside the instrument's step, and clean-up supplies and minutes;
  - four English rules (11 to 14): content notes name what texts contain, about 120 words a minute in class, one
    sense of a word at a time, and fixed terms on a reused passage.
- **docs/pipeline/briefs/plan-data.md:**
  - a Keys paragraph: exact quotation and referents from the sentence, stated against implied, no leaning on later
    events, science keys right about what moves, no worked-example structure in an exit, pieces are sheets;
  - an `opens_min` line: it counts only the parts after the warm-up.
- **scripts/defaults.py:** the same science and English lines. The 27 generated science and ELA DEFAULTS.md files
  were regenerated; kindergarten social studies keeps its own.
- **Unit corrections:** a Sonnet agent fixed the measure 2 marks, as the Fix section of the measure 2 report shows:
  every X, every E1 content note and the science clean-up lines.

## Measure 3: template and skeleton points

The skeletons ran unchanged in a fourth subject (ELA) and a fourth band (grade 7). Section skeletons, day skeletons
and the new Hand-backs section all worked. Points the writers and readers hit:

| Point | Where | Status |
|---|---|---|
| A blank piece passes `lesson.py check` with teacher prose or a printed key on it | lesson.py | LEAD (science finding 13), later.csv |
| Answer room is sized for grade 4: one 26-character line per exit part; grade 6 and up needs three lines | lesson.py page builder | LEAD (science finding 6), later.csv |
| `opens_min` meant "after the warm-up" in lesson.py, "including the warm-up" in plan data | plan-data.md | fixed (brief line; science days.csv aligned) |
| An end item placed on a day with no assessment stopped the skeleton (science E3, a kept product) | data | fixed by the lead (moved to day 22); the skeleton caught it as designed |
| An adapted day's credit line takes room from the quarter-page exit ticket | lesson.py page builder | note; the fix pass shortened stems |
| Exits cannot be `path` group; a group sheet uses `spoken` so no per-student ticket builds | README | note |
| Another day's item still cannot be named as [[id]] (kindergarten probe point 3) | day skeleton | open, as before |

## Tokens (MEASURED, subagent totals, docs/reviews/probe-confirm-tokens-2026-11-18.csv)

13 agent runs, 2.22M tokens.

| Stage | ELA grade 11 (5 days) | Science grade 7 (6 days) |
|---|---|---|
| Section plans 1.1 and 1.2 | 183k (10 planned days) | 181k (12 planned days) |
| Plan data and pieces | 121k | 116k |
| Answer-key read and fix | 175k | 172k |
| Day writing | 215k | 89k |
| Expert read | 80k | 231k |
| Fix pass | 203k | 258k |
| **Total** | **977k, 195k a finished day** | **1.05M, 174k a finished day** |
| Measure 2 read (both) | 199k | |

DERIVED:
- **Cheaper a day than probe 4** (251k science grade 5, 217k Algebra II); one more day a section spreads the reading-in.
- **The section stage stays cheap:** 15k to 18k a planned day.
- **Writing is still the small part:** 22% (ELA), 9% (science). The science day writer was fast and the fix pass
  paid for it (258k).

## Recommendation

The line is not met, so the plan does not scale on this probe. The rules round above is already in. The choice of
what comes next is Cory's (Desk card q-probe-confirm-1):

- **(a), recommended:** one more confirm probe of the same size (about 2M tokens) in a course neither probe has
  touched, with the new Keys paragraph at plan data. Scale only if it is On. 2M is a small price against full
  writing at about 180k a day.
- **(b):** scale a first wave now with the answer-key and expert reads kept on every section. Key faults would be
  caught where they are made, at the same cost a day. This accepts that plan share stays over the line.

Cory's other items stand: L71 (units.csv rows), L77 (soil trial, source A1).

## Files

- Section plans: docs/courses/english-language-arts-grade-11/u01-1.md, u01-2.md; docs/courses/science-grade-7/u01-1.md, u01-2.md
- Days: courses/english-language-arts-grade-11/u01-1/d001 to d005; courses/science-grade-7/u01-1/d001 to d006
- Reads:
  - answer-key-english-language-arts-grade-11-u01-2026-11-18.md
  - answer-key-science-grade-7-u01-2026-11-18.md
  - expert-english-language-arts-grade-11-u01-1-2026-11-18.md
  - expert-science-grade-7-u01-1-2026-11-18.md
  - probe-confirm-measure2-2026-11-18.md
