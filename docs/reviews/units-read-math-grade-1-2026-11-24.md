# Units read: math-grade-1, 2026-11-24

COURSE-RUN stage 4, Reads. The expert read all eight unit plans together, then fixed them.

## What was read

AGENTS.md; docs/COURSE-RUN.md stage 4; docs/agents/EXPERT.md; docs/agents/lenses/math.md; docs/courses/UNIT-PLAN.md; docs/GLOSSARY.md. Course: frame.md, scope-and-sequence.md, data/plans/math-grade-1/days.csv (all 160 rows), s01.md to s08.md in full, the m1 rows of data/progressions/math.csv. Continuity: docs/courses/math-kindergarten/s08.md and docs/courses/math-grade-2/s01.md (headers, limits, handoffs). Lead list: docs/reviews/lead-list-lens-pass-2026-11-17.md, sections "## math-grade-1 s01" to "s08" (23 items, no CAP rejections).

## Verdict

The eight plans form a sound arc: data and stories, then facts, tens, addition within 100, measurement and the full story table, geometry and time, then spaced review, with retrieval-only entry from kindergarten and handoffs grade 2 already expects. The one real gap was 1.NBT.C.5 ten more from 90 to 99, which unit 4 handed on and no unit picked up; unit 6 now teaches, practises and samples it. Most remaining faults sit in days.csv, frame.md and the skeleton generator, not in the plans, and are listed for the structure pass.

## Findings

| # | Severity | Unit | Finding | Verdict |
|---|---|---|---|---|
| 1 | major | s04, s06 | 1.NBT.C.5 ten more from starting numbers 90 to 99 (results 100 to 109) was never taught, practised or assessed. s04 called the handoff "not yet scheduled"; the progression row places the skill in units 4 and 6. | Fixed. s06 U6 day 119 models ten more than 94 with one ten-strip (104), day 120 practises it, Goal map practice shapes for 119 and 120 updated, record N (day 128) adds "Say ten more than 96; key 106". s04 Limits and Returns now point at unit 6. days.csv codes are for the structure pass (below). |
| 2 | moderate | s02 | Goal map day 20 practice shape said "marks the missing change on a number line", against s02 Limits and the frame (no number line in grade 1). | Fixed: "on a drawing". |
| 3 | moderate | s05 | U8 retrieval stayed within 10, yet day 100 needs make-ten sums within 20 (lead item s05-3). | Fixed: days 97 to 99 include one within-20 make-ten sum, such as 8 + 5. |
| 4 | minor | s03, s06 | The 2011 operations Progressions draft was cited on a third-party host in s03 and s06 but on the authors' host in s01 and s02. | Fixed: s03 and s06 now cite the same commoncoretools link as s01 and s02. |
| 5 | moderate | s07 | days.csv notes for 139, 140 and 146 and scope-and-sequence (lines on days 135 to 140, day 146 and the year-end row) say every day 139 comparison product completes or is scored in the 1.G.A.3 record; the plan scores that part only through fresh supplement S1 because day 139 is first teaching. The plan is right. | For the structure pass. |
| 6 | moderate | s08 | Field 2 says children solve all twelve story subtypes across 154 to 156, but the days.csv goals name only missing change (154), missing part (155) and comparison difference (156). | For the structure pass (goal wording, lead item s08-2). |
| 7 | minor | all | The skel Weight line names an outside organization in teacher text ("Student Achievement Partners"). | For the structure pass (unit_skeleton.py). |

Cross-unit checks with no fault: response slots and hand-backs (units 1 to 8, including unit 6 to unit 7 on 129 to 130 and unit 7 to days 149 to 150) have both ends; review entries point at taught rows; unit loads match days.csv; kindergarten rows enter as retrieval only; grade 2 unit 1 expects descriptive status on the hardest story subtypes, which unit 8 keeps.

## For the structure pass

days.csv (data/plans/math-grade-1/days.csv):
- Days 20 and 25 codes: remove 1.OA.D.7 (the exits no longer claim it). (s02)
- Day 54 kind: first teaching of three-addend stories; retype Understanding, or keep Application if the lead judges the stories applied. (s03)
- Day 57 note: "days 41 and 55" to "days 54 and 55". (s03)
- Day 68 codes: add 1.OA.D.8. Section labels in s03 cut across the arcs; re-cut at the next skeleton run. (s03)
- Codes: add 1.NBT.B.2a to rows 69 and 87; add 1.NBT.B.2b to row 74. (s04)
- Safety column, days 69 to 91: "Keep loose pieces out of mouths; adults count pieces back in." (s04)
- Safety column, days 96 to 109: the same loose-piece line. (s05)
- Days 119 and 120 codes: add 1.NBT.C.5. Day 128 codes: add 1.NBT.C.5 (record N samples it). Optional: one ten-more-from-the-90s prompt in the day 148 note and the scope-and-sequence year-end row. (finding 1)
- Day 113 supplies: add number cards (handwritten paper cards as a no-kit stand-in). (s06)
- Day 119 kind: retype Understanding (new content: crossing 100 and ten more from the 90s). (s06)
- Day 120 codes: add 1.NBT.C.4. (s06)
- Day 128 supplies: two unlabelled paper strips 6 and 14 units long, identical paper units, blank mats. (s06)
- Days 139, 140 and 146 notes, and scope-and-sequence.md (unit 7 paragraphs and the year-end row): say the day 139 comparison is descriptive first-teaching evidence and the scored part comes from S1 on day 146. (s07, finding 5)
- Days 137 to 140 supplies: add "clear overlays or tracing-paper copies (two stacked paper copies as a no-kit stand-in)"; drop "blunt scissors" (adults precut; children do not cut). Day 146 supplies: printed clock faces and paper matching wholes. (s07)
- Day 135 kind: first teaching of flat composites (the plan treats 135 flat work as first-teaching practice); retype Understanding. (s07)
- Days 154 and 156 goals: widen to the subtypes field 2 assigns, for example 154 "Find the missing start, change or result in joining and removing stories" and 156 "Show an unknown comparison difference, bigger or smaller quantity with labelled bars". (s08, finding 6)
- Days 155 and 156 tools: add "tape diagram". (s08)

Other shared files:
- frame.md and scripts/unit_skeleton.py: replace "Counting collections from home is optional; the class supply is the default" with "Request no collections from home; use the class supply." Also check the skel field 10 run-on that joins it to "Standards in full: 1.NBT.B.2a, 1.NBT.B.2b." (s04)
- data/plans/math-grade-1/source-map.csv: Food Drive row decision "keep" to "change" (the plan changes the context). (s05)
- scripts/unit_skeleton.py: the Weight line should name the file only, not the organization (finding 7); the s07 skel field 2 line "draw analog hands for half-hours on 142 and both times on 144" and the skel supplies "blunt scissors" follow from the days.csv fixes above. (s07)

## For Cory

None.

## Lead-list items worked

23 items: fixed 2 (s04 90-to-99 handoff, s05 within-20 retrieval); for the structure pass 19 (s02 1, s03 3, s04 2, s05 2, s06 4, s07 5, s08 2); no change 2 (s04 days 89 to 91 rotation: 120 seconds a child, ten children in 20 minutes, unheard parts recorded missing; s04 NBT 2015 host: no verified free authors' copy found offline, the citation already marks the third-party host, read only). No CAP rejections.

## Gates

- `python -X utf8 scripts/unitplan.py check math-grade-1`: PASS s01 to s08.
- `python -X utf8 scripts/sequence.py check math-grade-1`: 0 failures.
- `python -X utf8 scripts/goalmap.py audit math-grade-1`: no FAIL or WARN lines.
