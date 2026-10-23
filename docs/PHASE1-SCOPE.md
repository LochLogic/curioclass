# Phase 1: Module Map (K-12, all subjects)

Status: DECIDED, 2026-10-22. 586 modules across 12 subjects and 13 grades. Every module has at least one standards code, and every code is checked against its framework's official list at build time.
The tool starter template is parked (templates/parked-tool-starter.html) so design stays open.

## What a module is

A module is a unit-sized topic a teacher would teach over days to a few weeks, and the smallest thing a Curio Class tool is built for.
- Math, ELA, Science and Social Studies: one row per grade (or per course in high school).
- Arts, Health/PE, CTE, SEL: one row per grade band (K-2, 3-5, 6-8, 9-12), because these standards are written in bands.
- Computer Science: one row per grade K-5 and per band for 6-8 and 9-12, matching the 2026 CSTA standards.
- World Languages: rows by proficiency level (Novice, Intermediate, Advanced). The grade is only the typical span.

## Standards alignment: why "national", not "federal"

There are no federal K-12 content standards. Federal law (ESSA, and earlier the Department of Education Organization Act) bars the federal government from setting curriculum, and each state adopts its own standards. The highest level that exists is the **national consensus framework** for each subject, written by states, teachers or professional associations. Most state standards are adopted from or modeled on these. That is our alignment target everywhere, which keeps us from tying the site to any one state.

Where a subject has no national framework (Precalculus, Statistics, Calculus), the top level is the College Board AP course framework, which every state recognizes.

| Subject | Framework (version) | Code level in our data | Example | Verified against |
|---|---|---|---|---|
| Math | Common Core State Standards for Mathematics (2010) | cluster | `3.NF.A`, `A-REI.B.4` | Cluster list per grade and domain from corestandards.org (from memory, spot-checked) |
| ELA | Common Core ELA (2010) | standard | `RL.4.2`, `RF.K.1` | Strand rules: RL/RI/W 1-10, SL/L 1-6, RF only K-5 (RF.1-2 only K-1), no RL.8 |
| Science | NGSS (2013) | performance expectation | `MS-PS1-4` | Every PE code in the official NGSS All-DCI PDF (exact match) |
| Social Studies | C3 Framework (2013, rev. 2017) | Dimension 2 indicator | `D2.His.14.6-8` | Indicator list from the official C3 PDF |
| Arts | National Core Arts Standards (2014) | discipline + anchor | `VA:Cr2`, `MU:Re7` | 11 anchors x 5 disciplines |
| Health | National Health Education Standards (3rd ed., 2024) | standard 1-8 | `NHES.S3` | SHAPE America 2024 release |
| PE | SHAPE America National PE Standards (2024) | standard 1-4 | `SHAPE.S2` | 2024 release (cut from 5 to 4 standards) |
| Computer Science | **2026 CSTA PK-12 CS Standards** (released July 2026) | standard | `E3-PRO-VD-06`, `MS-SYS-NT-34` | All 196 identifiers extracted from the official 2026 PDF |
| World Languages | ACTFL Proficiency Guidelines; World-Readiness Standards | level / goal area | `ACTFL.Novice Mid`, `WRS.Cultures` | Closed list |
| CTE | Advance CTE Modernized Career Clusters (2024, 14 clusters) | framework | `CTE.Career Clusters` | 2024 framework (replaced 16 clusters) |
| Personal Finance | National Standards for Personal Financial Education (2021) | standard area | `NSPFE.Managing Credit` | 6 areas |
| Psychology | APA National Standards for HS Psychology | pillar | `APA.Cognition` | Pillar names |
| SEL | CASEL framework | competency | `CASEL.Self-Management` | 5 competencies |
| English learners | WIDA ELD Standards Framework (2020) | standard + key language use | `WIDA.ELD-4`, `WIDA.Argue` | 5 standards, 4 key language uses |
| Library / research | AASL National School Library Standards (2018) | shared foundation | `AASL.Curate` | 6 foundations |
| Precalc / Stats / Calc | College Board AP course frameworks | unit | `AP-STAT.U5` | Unit numbers |

What changed in this check:
- **Computer Science rebuilt** on the 2026 CSTA standards. The 2017 codes are now superseded, and K-5 is grade-level instead of banded (CS went from 26 to 34 modules).
- **Social Studies** moved from band labels (`D2.His.6-8`, which isn't a real code) to specific C3 indicators for all 82 modules.
- **PE** remapped to the 2024 four-standard set. **CTE** updated from 16 to 14 clusters, so "Health Science Careers" became "Healthcare and Human Services Careers".
- **ELA** ranges like `RL.K.1-3` expanded to real codes. **Math** fixed one wrong cluster (4.MD), and the 12 Precalc/Stats/Calc modules that had no code now carry AP unit codes.
- `scripts/standards.py` holds every registry, and the build now fails on any code that isn't real.

Limits of this check: it proves every code **exists** and is in the right grade band. Whether each code is the **best** match for its module was reviewed by hand, but not by a second reader. The CCSS Math cluster list comes from memory, spot-checked, not from a machine-readable official file.

## Files

| File | What |
|---|---|
| `data/modules/*.txt` | Source of truth, one line per module: `grade|course|strand|title|description|standards` |
| `data/courses.csv` | 37 courses. In K-8 the "course" is the grade-level subject. In 9-12 it's the real course (Algebra I, Biology...). |
| `data/grade_subjects.csv` | Grade-to-subject-to-course map, the "database of grades to subjects" (212 rows) |
| `data/modules.csv` | Generated, with stable module_id like `science-7-chemical-reactions` |
| `data/curioclass.db` | Generated SQLite with every table plus `module_grades` (one row per grade a module covers) |
| `scripts/standards.py` | Official code registries for every framework |
| `scripts/check_codes.py` | Lists any module code that isn't a real code |
| `data/standards/csta-2026-ids.txt` | All 196 CSTA 2026 identifiers |
| `scripts/build_db.py` | Validates (fields, course, grade fits course, unique ids, every code real), rebuilds, prints coverage |

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
computer-science     3   3   3   3   4   4   7   7   7   7   7   7   7
world-languages     10  10  10  10  10  10  17  17  17  20  20  20  20
cte                  .   .   .   .   .   .   3   3   3  11  11  11  11
sel                  2   2   2   2   2   2   2   2   2   2   2   2   2
eld                  5   5   5   5   5   5   5   5   5   5   5   5   5
library              2   2   2   2   2   2   2   2   2   2   2   2   2
```
Grade 12 looks heavy because it holds the electives (Precalc, Stats, Calc, Gov, Econ, Psych). Grade 9 science looks heavy because Biology and Earth Science are both placed there.

## Decisions (Cory, 2026-10-22)

| # | Question | Decision | What it means for the site |
|---|---|---|---|
| 1 | Middle school science | Keep the 6/7/8 split **and** a "Grades 6-8 Science" band view | Browse by grade or by band |
| 2 | Social studies order | Keep the common US sequence **and** browse by topic | Every module findable by topic, whatever grade a state teaches it in |
| 3 | High school math | Traditional Algebra I / Geometry / Algebra II, findable by topic and standard | Integrated Math 1-2-3 teachers search by topic or standard code |
| 4 | SEL | In, as a light shelf | 8 modules; not a build priority |
| 5 | World languages | Spanish **and American Sign Language** | ASL: 9 modules on the same proficiency levels, plus fingerspelling, sign parameters, classifiers and Deaf culture. ASL tools get reviewed by Deaf educators before release. |
| 6 | Gaps | Add **English learners** and **library/research skills** | English learners: 20 modules on WIDA. Library: 8 modules on AASL. AP-only courses and state crosswalks stay out for now. |

Site requirements from these decisions: browse by grade, by band, by topic and by standard code.

## To do before Phase 2

- [x] Cory decided the judgment calls (2026-10-22)
- [x] Check every standards code against official framework lists (2026-10-22)
- [ ] Optional: a second reader (a teacher) checks best-fit alignment for one subject
- [x] SEL in (light); languages: Spanish + ASL
- [ ] Later (not Phase 1): state crosswalks (TX TEKS, CA, FL B.E.S.T., NY, VA SOL), since they cover a large share of US students
