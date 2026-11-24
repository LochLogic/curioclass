# Units read: Science, Grade 2 (2026-11-24)

COURSE-RUN stage 4, "Reads": all seven unit plans of `science-grade-2` read together, then fixed. Expert role
(docs/agents/EXPERT.md, lens docs/agents/lenses/science.md). Every finding below is a cross-unit one, or one a
single-unit read would not see.

## What was read

AGENTS.md; docs/COURSE-RUN.md stage 4; docs/agents/EXPERT.md; docs/agents/lenses/science.md; docs/courses/UNIT-PLAN.md;
docs/GLOSSARY.md (locked words). The course: frame.md, scope-and-sequence.md, data/plans/science-grade-2/days.csv,
s01.md to s07.md in order, the course's rows in data/progressions/science.csv. Continuity: science-grade-1 s08.md
(the last unit plan of grade 1) and science-grade-3 s01.md (the next grade's unit 1). To test what the days already
hold: items.csv, handbacks.csv and the written days 11, 27, 39, 40, 43, 48, 51, 60, 63, 64, 69, 71, 72 and 73. All 76
days of this course are written, so every plan fix the days contradict is logged under "Day faults", not pushed
onto them.

## Verdict

The course is sound as a year: seven phenomenon-led units in a clear arc (land and water, land change and design,
materials, change, then three life science units), every code taught before it is assessed, unit loads matching
days.csv to the day and kind, and every review entry pointing at a row already taught. The most serious fault is a
reuse across one unit's checks: the day 43 exit gives children the butter melt-and-reharden story that the day 46
end-of-unit argument then scores (rule 4), so a remembered answer would be scored as an argument. Three smaller
reuses of the same kind (the chick case on days 6 and 11, toast on day 47 and again as "unfamiliar" on day 74) and
one gate failure (day 62's kind) were also found; the plans are fixed, and the written days carry four day faults.

## Lead-list items worked

docs/reviews/lead-list-lens-pass-2026-11-17.md has no `## science-grade-2 sNN` sections: 0 LEAD items and 0 CAP
rejections to work.

## Findings

| # | Severity | Finding | Verdict |
|---|---|---|---|
| 1 | Serious | **Exit reuses the end-of-unit story (rule 4).** s04 day 43 exit (item s04-X43, Series B) is butter melted by an adult and hard again after cooling. Day 46 end items s04-E13, E14 and E22 score the same story: butter heated to liquid, cooled to solid, and a second butter sample with no cooling record. A child can answer the scored argument from memory of the exit. | **Fixed** in s04 goal map (day 43 exit names a coconut-oil series, never butter). **Day fault** (below). |
| 2 | Moderate | **Retrieval repeats a case, not a practice.** s02 day 11 retrieves s1-parent-offspring with "a young bird calling and an adult bringing food", the same case day 6 used five school days earlier, which day 6 itself models on grade 1's robin chick pages. The third sight of one story shows memory of the answer, not two-source practice. | **Fixed** in s02 field 4 (new case: ducklings following the adult; the adult sheltering them under its wings). **Day fault.** |
| 3 | Moderate | **A course check calls a practiced case unfamiliar.** Year-end day 74 (items c2-H74b, c2-H74d) argues from toast; the scope and sequence calls it unfamiliar, but toast is unit 4's day 47 retry case (s04-X47c, X47d) and named in the day 39 exit. Course checks must use new cases. | **Day fault** (day 74) and **for the structure pass** (scope and sequence wording). No unit plan change: unit 4's use came first and is in its own unit. |
| 4 | Gate | **Day list out of step with days.csv.** s06 day 62 read "Fluency"; days.csv now holds "Application". unitplan.py failed s06. | **Fixed**: s06 header recount (understanding 1, application 2, check 2, respond 1), day list cell and U6 row. |
| 5 | Low | **Exit kind labels drift from the exit shape.** s04 day 40 ("take apart and record") and s05 day 51 ("examine and plan") were labelled produce, but both exits are touch-only (s04-X40a/b, s05-X51b), as the goal map rows themselves say. Neither verb is on a list, so either kind is allowed; the label should say what the child does. The goal's "record" and "plan" are carried by the practice, not the exit. | **Fixed**: both relabelled recognise, matching the written days. |
| 6 | Low | **Goal map exit text wrong for day 69.** s07 said "Says which of two new shore cards shows more kinds"; the exit (s07-X69a/b) is two touches with "neither" as the key, and six say why. | **Fixed** in s07 goal map. |
| 7 | Low | **Two assessment days filed as teaching days.** days.csv gives days 23 and 24 kind Application though both are `observe` assessment days; units 3 and 4 file theirs as Check. So s02's goal map lists the two assessments as teaching days whose practice is the assessment itself, and the header shows check 1. | **For the structure pass** (days.csv change below), then s02 header and goal map follow. |
| 8 | Low | **days.csv and the scope and sequence say each child models either job; the plan and days do not.** s06, d063 and d064 put every child on the jay seed job (nine of ten points) and score pollen movement once, from the day 63 retrieval card on a familiar case. 2-LS2-2 reads "dispersing seeds or pollinating plants", so the jay model meets the standard. | **For the structure pass** (note wording). Plan no change: deliberate, and days agree. |
| 9 | Low | **Thin, identical retrieval.** s1-daylight-seasons is retrieved on days 16, 27 and 48 with the same "mark the longer bar" prompt, which tells the teacher little about the bar-graph reading those units need. | **No change**: days written; cost above value. Worth a look at the cross-grade continuity pass. |
| 10 | Low | **Two scoring rhythms in one year.** Units 1 to 4 score the unaided record and respond after; units 5 to 7 score a revised artifact after written feedback (unit 7 revises on its respond day). Each meets the field 5 rule. A teacher reading the year sees two regimes. | **No change**: for the stage 7 coherence pass to name once in the course's assessment plan. |
| 11 | Low | s05 field 3 says unit 4's day 47 hands on "repaired evidence accounts"; d048 says day 47 "hands on nothing". The practice (claim, evidence, reason) is carried; no artifact is. Both are true. | **No change.** |
| 12 | Low | **Continuity into grade 3.** science-grade-3 s01 field 3 (frame text) says grade 2's plant test was "the first overall" fair test. Grade 2's equal-slope trays (days 16 to 18) and towel tests (day 30) come earlier, and grade 1's light tests before that. | **For the structure pass** (grade 3 frame wording). |
| 13 | Style | UK spellings in the prose of the plans edited here. | **Fixed**: changed to US forms in s02, s04, s05, s06 and s07, outside generated blocks (11 words). |

Checked and clean: section day ranges and days by kind in every header match days.csv (after finding 4); every
review and "returns" entry points at a row already taught; handbacks.csv has no row with a missing day, and the two
carries across units (day 10 to 11, day 65 to 66) have both ends; continuity in from grade 1 (s1 rows retrieved at
the days the scope and sequence names; grade 1 s08 hands daylight charts to units 3 and 5, and both retrieve them);
the year's arc and model carries (patterns, stability and change, design cycle, data graph, structure and function,
claim and evidence, system model) each have an introducing and a reusing unit.

## Day faults

| Day | Fault | Fix |
|---|---|---|
| 43 | Exit s04-X43 Series B is butter melted and rehardened, the story day 46's end items score. | Replace Series B with coconut oil: solid in a cool room, melted by a grown-up in a warm bath, solid again after cooling. Change the item stem, answer and samples, the exit card and its key. |
| 11 | Retrieval cards repeat day 6's chick case (young bird calls, adult brings food). | New two-card case: ducklings following an adult in a line to the water; the adult spreading its wings over them in rain. Ask "Which fact helps the young stay safe?" Expect following the adult (card 1), sheltering under its wings (card 2). |
| 74 | Items c2-H74b and c2-H74d use toast, practiced on day 47 (and named on day 39). | Replace the toast record with a case unit 4 never used, for example a soft clay bead baked hard by a grown-up that stays hard after cooling and chilling; update the H74d answer list. |
| 40, 51 | Exits are touch-only for goals that say "record" and "plan" (the plan now labels them recognise). | Optional at the grade's cleanup: add a short spoken or drawn part (day 40: say which pieces moved; day 51: say what to look at next week). |

## For the structure pass

- **data/plans/science-grade-2/days.csv, days 23 and 24:** `kind` Application to Check (both are `assess` observe
  days, as days 36 and 45 already are). Then regenerate s02's day list, recount its header (application 5, check 3)
  and drop the two goal map rows.
- **data/plans/science-grade-2/days.csv, day 64 note:** "Each child models either job; all have learned both." to
  "Every child models the jay's seed job; pollen movement is checked on the day 63 retrieval card; both jobs are
  taught." Same change to the scope and sequence, unit 6 paragraph ("Both jobs are taught; each child may model
  either.").
- **docs/courses/science-grade-2/scope-and-sequence.md, "Course-level checks":** "argue from unfamiliar wax, toast and
  slowly frozen/thawed soft-fruit" to name the day 74 replacement case in place of toast.
- **science-grade-3 frame, unit 1 "Why this unit, here":** drop "grade 2's plant test was the first overall"; say
  grade 3's force test is the first of grades 3 to 5 and builds on grade 1 and 2 fair comparisons.

## For Cory

Nothing. No finding touches scope, audience, money or people.

## Settled by the expert

- Day 43 exit material: coconut oil in place of butter (a reversible heating and cooling change not used elsewhere in
  unit 4 or the year-end check); s04.md.
- Day 11 retrieval case: ducklings following and sheltering under the adult; s02.md.

## Gates

- `python -X utf8 scripts/unitplan.py check science-grade-2`: 23 PASS, 0 FAIL (was 1 FAIL, s06 day 62 kind, before
  the fix).
- `python -X utf8 scripts/sequence.py check science-grade-2`: 0 failures.
- `python -X utf8 scripts/goalmap.py audit science-grade-2`: runs; it prints the goal map beside each day's exit for
  reading and reports no failure lines. Its output was the source of findings 5 and 6.

## Sources

Repository only, as listed under "What was read". No outside source was opened for this read; the rule 4 and
continuity findings rest on the plans, items.csv and the written days.
