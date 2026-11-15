# Fixes: scope and sequence of math-grade-3, 2026-11-15

**Counts, applied / not applied:** expert findings 6/0; expert settlements 5/0; Codex findings 6/0; lead call groups 9/0; applicable band groups 8/0; own findings 7/0. Overlapping sources are counted separately.

Only the four owned files were edited. Eight units, their order, ownership and day counts remain unchanged: 160 days, including 144 unit days and 16 course-level days.

Below, `scope` and `frame` mean the owned Markdown files; `days` and `source map` mean the owned CSV files.

**Applied**

- **Expert 1:** days, restored instructional paragraphs to notes on days 73, 74, 75, 82, 85, 94, 100 and 110; corrected supplies and tools.
- **Expert 2:** days, scope and frame, added direct independent year-end fluency stations on days 152 and 153; day 160 hands on both dated records.
- **Expert 3:** days and scope, retained days 4 and 5 graph products; day 21 now uses short graph questions and one extended equal-groups task.
- **Expert 4:** scope and frame, verified all 23 prerequisites against the grade 2 day plan, removed obsolete missing-file claims and corrected readiness wording.
- **Expert 5:** days, rewrote goals 29, 106, 108, 109, 125, 144 and 145; updated corresponding original-day map text where applicable.
- **Expert 6:** source map, adopted the lead’s current layout and removed all 36 duplicate destinations.

- **Codex 1:** days, scope and source map, kept days 62 to 67 warm-ups on understood multiplication; related quotients begin day 68.
- **Codex 2:** days, scope and frame, moved prerequisite reconnections to first use, updated the ledger, Seams and Models, and retained later retrieval.
- **Codex 3:** days, scope and frame, required actual individual mass and liquid-volume measurements within days 122 to 124. Diagrams support interpretation only; inaccessible measuring remains pending.
- **Codex 4:** days and source map, repaired the eight misplaced paragraphs, added model names and substantive original-day reasons, and removed day 100’s stray code prefix.
- **Codex 5:** source map, deduplicated 36 destinations while preserving all 143 source lessons and retained order.
- **Codex 6:** scope and frame, replaced obsolete prerequisite evidence and grade 2 readiness directions throughout.

- **Lead, Every subject 1 and Math 1:** scope and frame, applied readiness by grade number, one prerequisite ledger and retrieval for all directly assumed grade 2 rows; removed the frame’s tilde code.
- **Lead, Every subject 2 and Math 2:** days, scope and frame, applied Collect once, explicit sampled codes, complete parts, bounded end-day performances and direct year-end fluency.
- **Lead, Every subject 3:** source map, converted all 175 rows to the required schema, preserving credits, reasons and source information.
- **Lead, Every subject 4:** scope, assigned 60 saved minutes to each of ten folds: 600 minutes total, yielding 150 meetings and 9,000 minutes.
- **Lead, Every subject 5 and Math 7:** days and source map, checked goals and notes against the public base text and rewrote identified wording.
- **Lead, Math 3:** days, scope and frame, replaced competing focus estimates with one instructional-minute calculation.
- **Lead, Math 4:** days, tagged every explicitly retrieved earlier-grade row in `skills`.
- **Lead, Every subject 7:** frame and scope, retained untimed private facts work; no countdown has a grounded purpose here.
- **Lead, Math 6:** frame and scope, retained math’s teaching dates and clarified supplying relationships without accelerating instruction.

- **Band, readiness:** scope and frame, applied the common grade-number method and removed stale evidence qualifications.
- **Band, fluency handoff:** days, added direct year-end evidence for both fluency standards.
- **Band, stacked performances and Collect once:** days and scope, retained products and individual records instead of reconstructing them.
- **Band, source-map consistency:** source map, used one schema and lesson-level decision vocabulary.
- **Band, our words:** days and source map, retained mathematical intent with independently written goals and adaptation notes.
- **Band, focus and retrieval metadata:** days and scope, assigned minutes once and recorded prerequisite row ids.
- **Band, shorter paths and class size:** scope and days, retained the draft timing limitation and planned observation rotations for 30 children.
- **Band, handoffs and base fidelity:** frame, scope and source map, preserved model progression, fraction limits, inclusive trapezoid wording and retained lesson order.

- **Own 1:** days, scope and frame, placed ruler retrieval on day 28, earlier than Codex’s proposed day 31, because day 28 already uses a ruler.
- **Own 2:** days, scope and frame, replaced broad course-check code lists with explicit sampled-code blueprints and minute budgets; historical records remain separate.
- **Own 3:** days and scope, made all five area-unit types explicit on day 37, supplied concrete tiling on day 76, retained the days 82 to 83 problem grid for day 90, and removed extra retrospective area codes from day 147.
- **Own 4:** days and scope, added maintained-fluency codes and skills where warm-ups use them, making the focus allocation traceable.
- **Own 5:** source map, corrected 22 decisions: allocating a source unit across course units is not a lesson split; lessons 3.3.8 and 3.3.9 merge, while 3.3.10 stays on day 47.
- **Own 6:** frame and scope, corrected science timing: graph-using unit 3 precedes weather analysis in unit 6.
- **Own 7:** scope, carried newly placed prerequisite retrieval with the shorter-year folds on days 7, 41 and 69.

**Not applied**

No finding was rejected. Expert 6’s older column prescription was superseded by the settled lead schema; its underlying layout finding was applied. Unrelated grade-specific and high school band items required no grade 3 changes.

**Settled, for DIGEST**

| Judgment | Reuse |
|---|---|
| Grade 2 prerequisites | All 23 are verified in the written grade 2 day plan and receive retrieval, not readiness. Classroom delivery was not verified. |
| Day 58 | Written computation plus short rounding prompts remains an acceptable end day. |
| Older graph evidence | Day 153 carries day 21’s graph record forward unchanged, including days 4 and 5 construction products. |
| Subtraction merge | Three source lessons still occupy days 46 to 47; lesson-level decisions are two merge rows and one keep row. |
| Facts | Untimed and private. Distinguish memory, efficient strategy and counting; unobserved facts remain unverified. |
| Measuring | Full coverage requires actual estimates and measurements in grams, kilograms and liters. Diagrams alone leave measuring pending. |
| Focus | Planned major work is 5,325/8,160 instructional minutes, 65.26 percent. Assessment and response are excluded; actual task minutes need verification during unit planning. |
| Shorter paths | Ten folds save 600 baseline minutes. The 45-minute and combined shorter-year adaptations remain draft timing proposals. |

**For the structure pass**

- **`docs/RUBRIC-MATH-K8.md`, line 35, Gateway 3 teacher-support evidence cell**
  - Old: `and a readiness check opening each unit.`
  - New: `and readiness checks or retrieval tasks selected and timed by sequence-write.md rule 2.`
  - Reason: the existing blanket requirement conflicts with the settled readiness rule.

No math-grade-3 edits are needed in `frames.csv`, `calendar.csv` or the progression ownership rows.

**For Cory**

None.

**Gates**

- `python -X utf8 scripts/sequence.py check math-grade-3`: **0 failures**.
- `python -X utf8 scripts/frame.py check math-grade-3`: **0 failures**.
- `python -X utf8 scripts/frame.py calendar`: completed; math checks remain in **weeks 12, 23 and 31**, with **no grade 3 stagger break**.
- Additional consistency checks confirmed 143 unique source lessons, all 160 days mapped, retained source order, prerequisite tags, minute totals and no em dashes in the four owned files.
