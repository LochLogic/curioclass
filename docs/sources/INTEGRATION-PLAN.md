# Integration plan: from the source store to Curio Class days

Written 2026-11-13 (lead session), on Cory's ask to organize, catalog and plan integration once everything was
downloaded. The record of what each source is: [BASE-TEXTS.md](BASE-TEXTS.md). The evidence behind this plan:
`S:\CurioClass-sources\_catalog\analysis-math.md` and `analysis-science-ela-ss.md`.

Nothing here changes a page yet. Items marked **Cory** are scope calls; everything else is ready to start on his yes
to step 1.

## 1. What each subject draws on

| Subject | Grades | Draws on | Our share |
|---|---|---|---|
| Math | K to 8, Algebra 1, Geometry, Algebra 2 | IM base text: activities, contexts, planned questions, syntheses, practice ideas | unit order and plans, checks, keys, error register, At home, Other rooms, Tomorrow, all numbers and names |
| Math | precalculus, statistics, calculus | nothing | all |
| Science | 6 to 8 | OpenSciEd base text: anchors, lesson flow, investigations, readings, handouts | home or no-kit path, checks, keys, our display page in place of slides |
| Science | K to 5, 9 to 12 | OpenSciEd elementary and high school as reference (order, size of units, anchor ideas) | all |
| ELA | K to 5 | EL 2017 base text: lesson structure, protocols, Skills Block (K to 2), note-catchers | every text (trade books replaced), the questions and models on those texts, foundational skills in grades 3 to 5 |
| ELA | 6 to 12 | EL 6 to 8 as reference (module shape, assessment rotation) | all, on public-domain texts |
| Social studies | K to 12 | Massachusetts 2018 codes as content anchor, C3 skills; Investigating History and New York inquiries as reference | all |

## 2. How a source lesson becomes our days

The day format does not change: [courses/LESSON-DAY.md](../courses/LESSON-DAY.md). A source lesson feeds a day the
way an expert's notes would: the plan stays ours, the source supplies moves.

1. **Plan first.** The unit plan (`sNN.md`) and its data rows are written from our scope and sequence as now. The
   planner adds a `base` cell per day naming the source parts used (e.g. `im:4.3.7:warm-up,a1`,
   `osd:6.1:L3`, `el:4.1.1:L3`). One source lesson may feed two days, or one day may draw on two lessons.
2. **Pack.** A script reads the `base` cell, opens the source files in place in the store, strips what never carries
   over (BASE-TEXTS "Never carried over"), marks the parts used, fills the credit line and writes a writer pack to
   scratch. Nothing from the store is committed.
3. **Write.** The writer keeps the task idea, the order of moves and the planned questions; writes it in our voice;
   uses new names, contexts and numbers; cuts any lean on lessons our year has not taught; fits our minutes; and writes
   one line on what changed for the credit.
4. **Gate.** `lesson.py check` adds: credit present and matching `base`; no source name outside the credit; no source
   whose catalog flag is NC, SA, ND; a never-copy check against references (no shared run of 8 words); for science, a
   Safety and set-up section whenever materials name flames, heat, chemicals or glass.
5. **Read.** The cheap focused read and the expert read follow REVIEW-CADENCE.md, with three added questions: did the
   source activity teach the goal better than the plan alone, does anything lean on untaught lessons, does any wording
   read as the source's.

Per subject:
- **Math:** activity parts become "The day" with minutes kept; Student Facing tasks become items.csv rows with new
  numbers; Advancing Student Thinking feeds "if many get it wrong" and the error register. Slides and cover pages are
  not used. IM checks and assessments are behind sign-in: ours stay ours.
- **Science 6 to 8:** one OpenSciEd lesson becomes N days linked with `continues:`; its Learning Plan Snapshot breaks
  at "End of day N"; materials go to the header and Safety and set-up; procedures and handouts to the student page and
  data sheet; example student ideas to Words and supports and the wrong-answer register; videos and simulations are
  dropped or replaced. Spanish student editions are CC BY and can serve the Spanish copies.
- **ELA K to 5:** agenda parts become "The day"; note-catchers and anchor charts become student and display pages; any
  part built on a trade book is rewritten on our text. EL lessons run 60 minutes, so one may span more than one day.
  Skills Block (K to 2) needs the least rewriting.

## 3. Pipeline changes (each small; none made yet)

1. `base` column in `data/plans/<course>/days.csv`; `plan.py check` validates its format and, when the store is
   present, that the files exist. Documented in data/plans/README.md.
2. `scripts/basepack.py`: the pack step above. Store root `S:\CurioClass-sources` by default, overridable; prints
   "skipped" when the store is absent so checks still run elsewhere.
3. `lesson.py check` gates listed in section 2 step 4.
4. `scripts/refcheck.py`: 8-word-run index of the reference folders in `_catalog\ngrams\` (excluding standards text
   and stock phrases); fails on a shared 8-word run, notes 6-word runs, reports the base-text overlap share without
   judging it.
5. Briefs: a "Base text" section in DAY-WRITER.md and the write brief; the three read questions in the cheap and
   expert briefs; LESSON-DAY rule 4 gets the credit forms.
6. Catalog: `build_catalog.py` refreshed for Algebra 2, the grade K flat layout and the "+CS" move; a drop-list flag
   per file.
7. Records: an IM line in `s04.md` section 10 ("No open course was read" becomes stale); a base-text row in
   docs/pilots/COST.md.

## 4. Order of work

1. **The unit 4 adaptation test (math).** Our unit 4 (adding and subtracting fractions, days 25 to 38) against IM
   grade 4 unit 3 lessons 7 to 12. Note the naming: IM's own unit 4 is decimals. Stage 1: days 25 to 28, one writer at
   a time, cheap and expert reads, then go or no-go. Stage 2: days 29 to 38. Days 36 to 38 have no IM lesson and stay
   ours, which gives an in-unit control.
   Go rule: writer tokens within 10 percent of unit 2 (194,000 per day, pack included); expert-only findings 3 per day
   or fewer; zero 8-word overlap with Eureka; zero rights findings. Tokens up but findings down: Cory's call.
2. **If go:** the remaining grade 4 math units take IM through the same pipeline. The day-to-lesson map is in
   analysis-math.md section 1. Order differences to plan around: IM multiplies fractions by whole numbers before
   adding them (cut those links); area and perimeter is spread over four IM places (unit 11 draws on all four).
3. **ELA and science pilots alongside** (per card `q-plan-after-11-1`, once 11.1 has its teacher read): one EL grade
   4 lesson set on a public-domain text (G4M1 "The Red Wheelbarrow" lessons need no text swap, a clean first test),
   and one OpenSciEd 6.1 lesson run through to days.
4. **Then other courses**, each starting with a fit table like analysis-math.md section 1 before any day is written.

## 5. For Cory

1. **Grades 6 to 8 science order.** Our current order (data/sequence.csv) puts topics in different grades from
   OpenSciEd (space in our 6 is their 8.4; signals in our 8 is their 6.5). FOUNDATION forbids stitching programs, so
   using the base well means redrawing grades 6 to 8 to OpenSciEd's 18 units (168, 170, 177 days of 45 minutes).
   Pick: redraw to OpenSciEd (recommended), or keep our order and use OpenSciEd lesson by lesson.
2. **Science equipment.** Every OpenSciEd unit assumes a kit (microscopes, magnets, flames, chemicals). Pick one
   default for a free site: household substitutes per item; a no-kit data path (often federal data) beside each
   hands-on day; or our own simulations. Recommended: household substitutes where safe, no-kit data path otherwise.
3. **Go-ahead** for the pipeline changes in section 3 and stage 1 of the unit 4 adaptation test.
4. Still open from before: whether math units 12 to 18 and the check days are queued now. Days 25 to 38 stay held
   until the test.
