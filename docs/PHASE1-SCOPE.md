# Phase 1: Module Map (K-12, all subjects)

Status: FIRST DRAFT, 2026-10-22. 533 modules across 10 subjects and 13 grades.
The tool starter template is parked (templates/parked-tool-starter.html) so design stays open.

## What a module is

A module is a unit-sized topic a teacher would teach over days to a few weeks, and the smallest thing a Curio Class tool is built for.
- Math, ELA, Science and Social Studies: one row per grade (or per course in high school).
- Arts, Health/PE, CS, CTE, SEL: one row per grade band (K-2, 3-5, 6-8, 9-12), because these standards are written in bands.
- World Languages: rows by proficiency level (Novice, Intermediate, Advanced). The grade is only the typical span.

## Standards used (national baselines)

| Subject | Baseline | Code style in data |
|---|---|---|
| Math | Common Core State Standards for Mathematics | cluster, e.g. `3.NF.A`, `A-REI.B` |
| ELA | Common Core ELA | standard range, e.g. `RL.4.2`, `RF.K.1` |
| Science | NGSS | performance expectation, e.g. `MS-PS1-4` |
| Social Studies | C3 Framework | dimension + band, e.g. `D2.His.6-8` |
| Arts | National Core Arts Standards | anchor, e.g. `VA:Cr2` |
| Health / PE | NHES / SHAPE America | standard number |
| Computer Science | CSTA K-12 | identifier, e.g. `2-AP-13` |
| World Languages | ACTFL proficiency | level |
| CTE / Finance | Advance CTE; Jump$tart | framework name |
| SEL | CASEL | competency |

Codes are at cluster or standard level. They have not yet been checked line by line against the source documents (see To do).

## Files

| File | What |
|---|---|
| `data/modules/*.txt` | Source of truth, one line per module: `grade|course|strand|title|description|standards` |
| `data/courses.csv` | 37 courses. In K-8 the "course" is the grade-level subject. In 9-12 it's the real course (Algebra I, Biology...). |
| `data/grade_subjects.csv` | Grade-to-subject-to-course map, the "database of grades to subjects" (212 rows) |
| `data/modules.csv` | Generated, with stable module_id like `science-7-chemical-reactions` |
| `data/curioclass.db` | Generated SQLite with every table plus `module_grades` (one row per grade a module covers) |
| `scripts/build_db.py` | Validates (field count, course exists, grade fits course, unique ids), rebuilds, prints coverage |

Rebuild after any edit: `python scripts/build_db.py`

## Coverage (modules per grade, band modules counted in each grade they span)

```
subject              k   1   2   3   4   5   6   7   8   9  10  11  12
math                 9  10   9  10  11  10  10   8  10  11   9   8  19
ela                  8   8   8   9   9   8   9   9   8   8   7   7   7
science              5   5   6   7   7   7   8   8   8  15   9   8   5
social-studies       5   5   5   5   5   5   7   8   8   4   5   8  16
arts                 7   7   7   8   8   8  10  10  10  10  10  10  10
health-pe            6   6   6   6   6   6   6   6   6   6   6   6   6
computer-science     3   3   3   4   4   4   5   5   5   6   6   6   6
world-languages      5   5   5   5   5   5   9   9   9  11  11  11  11
cte                  .   .   .   .   .   .   3   3   3  11  11  11  11
sel                  2   2   2   2   2   2   2   2   2   2   2   2   2
```
Grade 12 looks heavy because it holds the electives (Precalc, Stats, Calc, Gov, Econ, Psych). Grade 9 science looks heavy because Biology and Earth Science are both placed there.

## Judgment calls (please review)

1. **Middle school science split.** NGSS is written for grades 6-8 as a band. I used a common split: 6 = Earth/space plus cells, 7 = chemistry plus ecology, 8 = physics plus heredity and evolution. States vary, so the site should also let teachers browse by band.
2. **Social studies sequence.** Follows the most common US pattern: expanding horizons K-3, state history 4, early US 5, ancient world 6, medieval world 7, US to 1877 in 8, modern world 9-10, US since 1877 in 11, government and economics in 12. Texas, California and others differ, and state mapping can come later.
3. **High school math** follows the traditional Algebra I / Geometry / Algebra II path, not the integrated Math 1-2-3 path. The modules work for both.
4. **SEL** is included but thin (8 modules) pending your decision on whether it's in scope.
5. **World Languages** has Spanish only. French and others reuse the same levels.
6. **Not included yet:** AP-only courses beyond Stats and Calc, ESL/ELD, Library/Research, state-specific history beyond placeholders, and Special Education adaptations (handled as a tool design rule, not as modules).

## To do before Phase 2

- [ ] Cory reviews the judgment calls above
- [ ] Spot-check standard codes against the source PDFs (CCSS, NGSS, C3, CSTA), at least 10% per subject
- [ ] Decide SEL in or out; decide which languages after Spanish
- [ ] Optional: add top-5 state crosswalks (TX TEKS, CA, FL B.E.S.T., NY, VA SOL), since they cover a large share of US students
