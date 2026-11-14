# Baseline 1 cleanup, 2026-11-14

The mechanical pass that applies the frame-side items of `docs/reviews/baseline-1-structure-fixes-2026-11-14.md` to
all 52 course frames, the progression CSVs and the three docs the report left for the next pass. One fixer worked alone.
Day totals per course are unchanged: units, days, minutes, per-week and weeks all match `data/plans/frames.csv`
from before the pass.

## Applied

### Stagger-rule week moves

| File | Change |
|---|---|
| docs/courses/math-kindergarten/frame.md | Checks section made a table. Year-end check moved before unit 8's last 5 days (week 31); unit 8 is 17 days, then 5 after the check (22 in all); a review row carries the 5 days. Days bullet and unit 8 text match |
| docs/courses/math-grade-1/frame.md | Checks as a table. Year-end check after unit 7 (week 30); unit 8, the review unit, follows as further respond time. Days bullet, unit row, For the lead and totals updated |
| docs/courses/math-grade-2/frame.md | The same, year-end check after unit 8 (week 29), unit 9 the review after it |
| docs/courses/math-grade-3/frame.md, math-grade-4, math-grade-5 | The year review split around check 3: "Year review, part 1" (3 days) before check 3 and "part 2" (5, 4, 4 days) after it, so check 3 falls in week 31. Closing line: "Four course-level check days, ... (three before check 3, N after it)"; the record line names the last review days |
| docs/courses/math-grade-6/frame.md | Check 1 moved after unit 4 (days 80 and 81), now units 1 to 4 with fraction division; check 2 weighted to units 5 and 6. Unit 3 text and the Cross-subject day list match (unit 4 days 60 to 79) |
| docs/courses/social-studies-grade-3/frame.md | Check 3 after unit 6 (week 28); unit 7 checked by its own end-of-unit assessment |
| docs/courses/social-studies-grade-4/frame.md | Check 1 after unit 2 (week 8), the first-peoples claim moved to check 2; check 3 after unit 6 (week 27), unit 7's peoples and hazards on unit 7's own assessment |
| docs/courses/science-grade-2/frame.md, social-studies-grade-2, science-grade-5 | Tool (a), a course that meets fewer than five days a week choosing its weeks: the Days bullet names the pin (science 2 check in week 17, social studies 2 check in week 14, science 5 check 1 in week 10) and the row labels carry the week. Science 5 Cross-subject wording follows ("overlapping the first weeks of unit 6", "about three weeks") |
| scripts/frame.py | `PINS` added (science-grade-2 day 40 on school day 84; social-studies-grade-2 day 46 on 68; science-grade-5 day 43 on 50). `school_day()` spreads days evenly between the pins. Needed because tool (a) could not be written in a frame alone; see "For the lead" |
| docs/courses/CALENDAR.md | The "Until the subject fixers ... apply them" sentence replaced by a line saying they are applied and how a pin works; the generated table is rewritten by `frame.py sync` |

### One checks-table shape in the 12 math frames

`| Check | After unit | Check days | Respond days | What it checks |` in math K to 8, algebra-i, algebra-ii and geometry
(high school rows "Check N (weeks)", 2 check days and 1 respond day each; grades 6 to 8 rows keep their day numbers in
the label, such as "Check 1 (day 80; respond day 81)").

### Ids and codes

| File | Change |
|---|---|
| docs/courses/science-grade-6/frame.md | Seams: chem-energy-accounting, chem-thermal-equilibrium, chem-reaction-rates, chem-equilibrium-design (particle row); phys-wave-particle-light, phys-em-radiation-effects (light row); chem-resources-hazards-climate-human (hazard row) |
| docs/courses/science-grade-7/frame.md | Seams: chem-nuclear-processes added |
| docs/courses/science-grade-8/frame.md | Unit 3 owned standards gain `~MS-PS3-5` |
| docs/courses/social-studies-grade-5/frame.md | Unit 8 names MA.5.T5.6a and MA.5.T5.6b as taught in unit 9 |
| docs/courses/science-grade-3/frame.md, science-grade-4, science-grade-5 | The "4n/3" estimate replaced by "school days come from docs/courses/CALENDAR.md and data/plans/calendar.csv"; Cross-subject school-day ranges recomputed from the calendar (science 3 units 3 and 4: school 47 to 98; science 4: social studies 4 unit 7 now 137 to 160, "near school day 48", unit 5 ends near 117) |

### Wording sweep (all 52 frames)

- "N teaching days" to "N course days" in the Days bullet: 22 frames.
- "Four / Six check days" to "course-level check days": 12 frames (ELA 3 to 8, science 3 to 5, social studies 3 to 5),
  plus math 3 to 5 in their own edit (15 in all).
- End-of-unit line added to the Days bullet: biology, chemistry, physics, english-language-arts-grade-6.
- Readiness line (frame-write lesson 16) added: algebra-i, algebra-ii, geometry, biology, ELA 3 to 6, math 1 to 6,
  science-grade-1 (15 frames).
- Identification line on all 52: "Course `<slug>` (catalogue id `<id>`)"; 13 frames had their old id (the slug)
  in the id slot (ELA 9 to 12, math 3 to 8, science 6 to 8). Civics keeps "kept from the old list".

### Docs

| File | Change |
|---|---|
| docs/courses/UNIT-PLAN.md | Rule 5 now "Unit plans follow the subject-wide order in PRODUCTION-PATH steps 3 and 4. A preceding unit need not have written lessons. Section plans follow step 7, except the probe section." Field 7 "The respond half" became **Response allocation** ("Name the marking time and the response time separately. State whether response occurs within the assessment day or on later respond days, and count it once."), keeping the marking-step text without "inside the period"; the intro says "the response allocation"; the blank copy heading is "## 7. Response allocation" with a marking and response time line. A line under the unit plan field list names the math-only fields (the *Math fills* parts of unit field 2 and section fields 1, 3 and 8). History lines 418 and 434 keep "respond half" |
| data/plans/README.md | New section "Scope-stage and calendar files": the scope-stage `days.csv` columns `day,stretch,unit,kind,goal,skills,codes,assess,school_day,note` with the stretch `C`, kind and assess values; `frames.csv` and `calendar.csv` with their columns, written by `frame.py sync` |

### Literacy codes moved to `lit:`

| File | Rows | Codes moved |
|---|---|---|
| data/progressions/science.csv | 122 | 382 |
| data/progressions/social-studies.csv | 58 | 103 |

Each "Also meets (literacy, no added days; ...): ..." and "Literacy also met (Common Core literacy in history and
social studies, no added days): ..." sentence was removed from notes and its codes appended to cross_subject as
`lit:<code>` with the cell's "; " separator, other entries kept. No row owns an RST, RH or WHST code in its standard
column, so none stayed there. CRLF and quoting kept (round-trip tested before the write). Frames that list these
codes as also-met keep them.

## Not applied, with the reason

- **algebra-i, algebra-ii, geometry "teaching days".** They say "Focus is counted on teaching days", the glossary's
  day kind, not a course-day count; changing it would change the meaning. So 22 of the report's 25 frames changed.
- **ELA K to 5 per-base-unit lines.** Already present (applied by the subject fixers); nothing to add.
- **Two science rows keep RST.11-12.8 in notes:** phys-wave-particle-light and phys-em-radiation-effects explain a
  literacy lean ("RST.11-12.8, not RI.11-12.8"). That is a reason, not "also meets" wording, so it stays; the code
  itself moved to `lit:` from their also-meets sentence.

## For the lead

1. **scripts/frame.py changed** beyond the frame-only scope: `PINS` is the only way to express tool (a) for the three
   grades that could not clear the rule otherwise (science 2, social studies 2, science 5).
2. **Back-to-back assessments in math 1 and 2.** Unit 7 (math 1) and unit 8 (math 2) keep their own end-of-unit
   assessment right before the year-end check. The scope and sequence writer should place them so the two do not
   fall on adjacent days, or fold one into the other.
3. **Social studies grade 2 rate.** The pin puts more than 3 lessons a week in the early weeks; 96 days over 31
   calendar weeks already exceeds 3 a week, so this is an existing tension, not a new one.

## Gates (all after the last change)

| Command | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 52 courses; calendar.csv 674 rows, 52 courses |
| `python -X utf8 scripts/frame.py check` | 52 frames, 0 failures, no notes beyond the unit and day summaries (no citation drift beyond 3 days) |
| `python -X utf8 scripts/frame.py calendar` | Stagger rule breaks: none |
| `python -X utf8 scripts/progression.py check science` | 198 rows, 0 failures, no `lit:` notes |
| `python -X utf8 scripts/progression.py check social-studies` | 384 rows, 0 failures, no `lit:` notes |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |
| `python -X utf8 scripts/plan.py check` | exit 0; frames 0 catalogue failures; math-4 812 items, 1161 wrong answers, 0 failures |
