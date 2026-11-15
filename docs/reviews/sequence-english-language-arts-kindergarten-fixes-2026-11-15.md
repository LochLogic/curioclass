# Fixes: scope and sequence of english-language-arts-kindergarten, 2026-11-15

| Source | Applied | Not applied |
|---|---:|---:|
| Expert findings | 6 | 0 |
| Codex findings | 3 | 1 |
| Applicable lead calls | 9 | 0 |
| Applicable band themes | 9 | 0 |
| Own findings | 6 | 0 |
| **Total** | **33** | **1** |

The expert’s six settled-table judgments and Codex’s eight recommendations are incorporated or preserved, without counting them twice. Only the four owned files were edited. No git commands were used.

**Applied**

File names below refer only to this course’s owned files.

- **Expert 1:** days.csv and scope-and-sequence.md remove cumulative foundations collection from days 76 and 156; the course-check windows carry completion evidence.
- **Expert 2:** days.csv spreads closing performances across days 28 to 33, 64 to 75 and 148 to 156, with explicit small-group or individual allocations for 30 children.
- **Expert 3:** days.csv embeds added observations in teaching and performance days while retaining the base’s assessment slots as Check days. There are now 23 whole unit Check days.
- **Expert 4:** frame.md adds the continued-row exception; scope-and-sequence.md names initial evidence and completing records without moving ownership.
- **Expert 5:** scope-and-sequence.md explicitly retains required printed blending from day 85. Earlier taught-letter blending remains optional for unit planning.
- **Expert 6:** days.csv makes day 76 a pure response day, acting on records already collected.

- **Codex 2:** scope-and-sequence.md adds the completion table; days.csv retains day 63 RL.K.3 evidence, closes L.K.2 on day 117, and combines both digital contributions on day 156. RF.K.3 completion moves to the year-end window, following the expert.
- **Codex 3:** days.csv gives both roster halves identical course-check coverage and explicitly distinguishes new tasks from retained evidence.
- **Codex 4:** source-map.csv corrects day 64’s response description and documents the long-e postponement in all ten cycle 24/25 lesson rows.

- **Lead, Every subject 1:** scope-and-sequence.md lists the earlier-grade classification: none of the 29 kindergarten rows assumes an earlier-grade row.
- **Lead, Every subject 2:** days.csv and scope-and-sequence.md implement Collect once, sampled-code lists, explicit code parts, distributed performances and budgets for 30 children.
- **Lead, Every subject 3:** source-map.csv uses the required eleven-column layout. All 344 entries, original identifiers, paths and cut reasons remain.
- **Lead, Every subject 4:** scope-and-sequence.md gives minutes saved for every fold and totals against the frame.
- **Lead, Every subject 5:** goals and source-map descriptions use fresh wording. Comparison with the opening three pages of 266 unique held lesson PDFs found only a necessary letter-order match and a title-containing goal; that goal was rewritten.
- **Lead, Every subject 7:** frame.md and scope-and-sequence.md identify teacher-held timing as rotation pacing, without a child speed target.
- **Lead, ELA 1:** frame.md explicitly states that foundations continued across units are not re-checked for readiness.
- **Lead, ELA 6:** scope-and-sequence.md counts eight anchors, four informational and four literary, with each anchor cluster counted once.
- **Lead, ELA 11:** scope-and-sequence.md contains the course text record for all 21 catalogue entries, with missing manuscripts, measurements and clearances marked pending.

- **Band, K to 2, cumulative evidence:** frame.md states the shared Collect once convention; day notes name carried records.
- **Band, K to 2, end days:** performances are distributed instead of stacked on closing days.
- **Band, K to 2, observation load:** added observations use teaching days and per-child records.
- **Band, K to 2, continued foundations:** the completion table distinguishes first placement from completion.
- **Band, K to grade 1 handoff:** spoken long-vowel associations remain; independent silent-e and vowel-team decoding are not introduced.
- **Band, shorter period:** the existing shorter-period budget now accounts for 30 children and identifies its unverified timing limits.
- **Band, source-map consistency:** the kindergarten map uses the settled shared schema.
- **Band, course text record:** the record is filed within the owned scope-and-sequence.md.
- **Band, anchor denominator:** the record consistently excludes paired and short readings from the anchor count.

- **Own 1:** frame.md and days.csv remove the new year-end opinion task, which repeated the recent card form; its existing record goes into the handoff without another score.
- **Own 2:** days.csv collects unit 3 reading, spelling and chaining evidence once across days 110 to 113, 115 and 116; day 117 reuses it.
- **Own 3:** days.csv aligns observation codes with sampled or explicitly retained evidence and removes stale assessment directions.
- **Own 4:** days.csv protects fold days 114 and 149. Foundations observations avoid day 114; card-revision evidence is recorded on day 148, leaving day 149 as unassessed rehearsal.
- **Own 5:** days.csv and the course text record identify planned constituent selections within set-valued catalogue entries.
- **Own 6:** frame.md changes the card’s reason wording to “may include,” preserving kindergarten’s optional-reason boundary.

**Not applied**

- **Codex 1, replacement manuscripts and completed complexity evidence:** not completed. The authorized files are the frame, scope and sequence, days and source map. The course record now documents the missing work, but replacement manuscripts, selected poems, measured lengths, verified section breaks, passage-specific supports and finished-task timing remain outstanding. No invented measurements or manuscript locations were supplied. This finding remains open.

**Settled** (for DIGEST)

| Judgment | Reuse |
|---|---|
| Units and ownership | Keep four units of 34, 42, 39 and 39 days; 160 course days overall. |
| Continued strands | Record initial evidence and a named completing window; do not introduce readiness checks between units. |
| Cumulative foundations | Collect once in the course window; reuse matching recent cycle evidence without another performance or score. |
| Roster halves | Same complete coverage, with different reserved cold passages of matched demand. |
| Mid-year retell | Keep The Magic Bow; retain the earlier weather-story evidence separately. |
| Long e and blending | Long e begins on day 151; required printed blending begins on day 85. |
| Digital completion | Day 156 combines each child’s day 75 typing and day 155 audio contributions. |
| Shorter year | Ten unassessed folds save 1,200 minutes at 120 minutes per meeting, producing 150 meetings; calendar coordination remains necessary before use. |
| Text record | Planned demand is not completed manuscript evidence. Missing texts and measurements remain explicit. |

**For the structure pass**

No changes are needed to progression ownership, frames.csv, unit day counts or the current calendar for this course.

In **data/plans/ela-texts.csv**, update only the `note` cells below for course `english-language-arts-kindergarten`. Preserve statuses and anchor classifications.

Define this exact text as **R**:

`Course record: docs/courses/english-language-arts-kindergarten/scope-and-sequence.md#course-text-record.`

For nonempty old notes, the new value is **old note + `; ` + R + one space + suffix**. For empty notes, it is **R + one space + suffix**.

| text_id | Old note | Exact suffix |
|---|---|---|
| gk-u1-08 | `Frame names the routine, not the poems; public domain or Curio Class poems` | `Planned constituents: gk-u1-08-p01 to gk-u1-08-p07 and gk-u1-08-book. Constituent manuscript records pending.` |
| gk-u2-01 | `Drawn on recent US government weather pages for children (frame); those pages credited` | `Planned constituents: gk-u2-01-a to gk-u2-01-e. Constituent manuscript records pending.` |
| gk-u2-02 | Empty | `Planned constituents: gk-u2-02-a and gk-u2-02-b. Constituent manuscript records pending.` |
| gk-u3-01 | Empty | `Planned constituents: gk-u3-01-a and gk-u3-01-b. Constituent manuscript records pending.` |
| gk-u3-05 | Empty | `Planned constituents: gk-u3-05-a and gk-u3-05-b. Individual adaptation records pending.` |
| gk-u4-01 | Empty | `Planned constituents: gk-u4-01-a and gk-u4-01-b. Constituent manuscript records pending.` |
| gk-u4-02 | Empty | `Planned constituents: gk-u4-02-a and gk-u4-02-b. Constituent manuscript records pending.` |

These are planning identifiers. Do not change any text’s status to on file or invent measurements before its manuscript exists.

**For Cory**

None.

**Gates**

- `python -X utf8 scripts/sequence.py check english-language-arts-kindergarten`: **0 failures**, including source-map layout.
- `python -X utf8 scripts/frame.py check english-language-arts-kindergarten`: **0 failures**; four units, 160 days.
- `python -X utf8 scripts/frame.py calendar`: **passed**. Kindergarten ELA remains in weeks **16 and 32**, with no stagger break and ELA/math gaps of six and five school days.
- Scoped consistency checks passed: unit totals preserved, identical roster coverage, ten unassessed folds, 344 source-map entries, 139 topic lessons, 130 foundations lessons and no em dashes.
