# The Curio Class school calendar

One calendar for every course, so a frame, a scope and sequence and a day plan can say "week 14" and mean the same week. The numbers here are positions in a school year, not dates: a school sets its own start, holidays and testing days, and the calendar stays the same.

Settled 2026-11-14 (baseline 1 structure findings 4 and 6). The gate is `scripts/frame.py`; `python -X utf8 scripts/frame.py sync` rewrites `data/plans/calendar.csv` and the table at the end of this file, and `python -X utf8 scripts/frame.py calendar` prints the course-level check weeks and any break of the stagger rule.

## The words

| Word | Meaning |
|---|---|
| School day | One of the 160 teaching days of the year, numbered 1 to 160. The calendar has no holidays, testing days or half days: a school lays its own year over these 160. |
| Week | Five school days in a row: week 1 is school days 1 to 5, week 32 is school days 156 to 160 (week = (school day - 1) // 5 + 1). |
| Course day | One meeting of one course, numbered from 1 in that course's frame. In a course that meets every school day, course day and school day are the same number. |
| Year | 160 school days, 32 weeks. |
| Half-year course | 80 school days, 16 weeks: the fall half is school days 1 to 80, the spring half 81 to 160. |

A frame counts course days. Only the calendar turns them into school days and weeks.

**36 weeks and 32.** A real school year is about 36 weeks (about 180 days); this calendar numbers the 160 days a
course teaches over 32 weeks, leaving the rest for a school's own testing, holidays and events. Cory's 2026-11-12
call on the home path named "a 36-week numbered calendar"; whether the home calendar spreads the 160 days over 36
weeks or numbers these 32 is not settled yet (continuity review 2026-11-14, E5).

## How a course meets

| Course | Meets | Weeks it spreads over |
|---|---|---|
| ELA, math and social studies, every grade; science 6 to 12 | Every school day | 32 |
| Science 3 to 5 | Four days a week | 30 (120 course days), so the year ends with two weeks free for the other subjects' year-end checks |
| Science and social studies K to 2 | Fewer than five days a week, as their frames set | Science K 29, grade 1 29, grade 2 28; social studies K 30, grade 1 31, grade 2 31 (the `WEEKS` table in `scripts/frame.py`), so their year-end checks come before ELA's and math's |
| US Government and Politics | Every school day, fall half | 16, school days 1 to 80 |
| Economics | Every school day, spring half | 16, school days 81 to 160 |

A course with D course days spread over W weeks puts course day n on school day `start + ceil(n x 5W / D)`, so its days fall evenly across its weeks. Once a scope and sequence is written, its `data/plans/<course>/days.csv` may give each day a `school_day` column, and that column wins. From 2026-11-14 `scripts/frame.py` builds that course's rows of `data/plans/calendar.csv` from its days.csv (`days_calendar`): each day on its `school_day` where filled and on the even spread otherwise, a unit's or a check's days cut into separate rows wherever another day falls between, so a held day (a look-back taught weeks later, an on-the-day holiday lesson) shows in its own week. A course with no days.csv, or one whose check days do not match its frame's Course-level checks table, is still read from its frame.

## Course-level checks across a grade (the stagger rule)

A course-level check is a check that sits outside every unit and covers several units (GLOSSARY). Each one is followed by its respond day or days.

1. **K to 5, one teacher.** No school week holds the course-level check days of two subjects. A grade's year-end checks fall in four different weeks: science and social studies first (weeks 28 to 30), math in week 31, ELA in week 32.
2. **K to 2.** The ELA and math one-to-one checks fall in different weeks and at least five school days apart, because one adult hears every child alone.
3. **6 to 8, a teacher per subject.** No school day holds two subjects' mid-year check days. Week 32 is a finals week, as in high school, and may hold every subject's year-end check.
4. **9 to 12.** Week 32 (and week 16 for a half-year course) is a finals week. No other rule.
5. **The tools, in this order.** (a) A course that meets fewer than five days a week chooses its weeks. (b) Review days split around a check. (c) A check moves to the other side of the unit next to it, and its "What it checks" cell changes with it. A unit never moves to make room for a check.

The frame-side moves that bring every K to 8 grade inside the rule are listed per frame in `docs/reviews/baseline-1-structure-fixes-2026-11-14.md`. They were applied on 2026-11-14 (docs/reviews/baseline-1-cleanup-2026-11-14.md), and `frame.py calendar` shows no break. Tool (a) is written as a pin in `PINS` in scripts/frame.py: a course day placed on a chosen school day, with the days before and after it spread evenly. Three courses use one (science grade 2, social studies grade 2, science grade 5), each named in its frame's Days bullet.

## Target weeks, K to 8

The weeks each course-level check falls in. A scope and sequence places its checks on these weeks.

| Grade | ELA | Math | Science | Social studies |
|---|---|---|---|---|
| K | 16, 32 | 17, 31 | 14, 29 | 15, 30 |
| 1 | 16, 32 | 19, 30 | 15, 29 | 14, 31 |
| 2 | 15 to 16, 32 | 18 to 19, 29 | 20, 28 | 14, 31 |
| 3 | 16, 32 | 12, 23, 31 | 9, 20, 30 | 14, 25, 28 |
| 4 | 16, 32 | 12 (or 9), 23, 31 | 10, 19, 30 | 8 (or 12), 21, 27 |
| 5 | 17, 32 | 11, 22, 31 | 10, 21, 30 | 16, 29 |
| 6 | 12, 22, 32 | 16, 24, 32 | 18, 32 | 15, 23, 32 |
| 7 | 12, 22, 32 | 9, 24, 32 | 14, 32 | 13, 24, 32 |
| 8 | 18, 25 to 26, 32 | 14, 24, 32 | 15, 32 | 10, 20, 29 to 30 |

## Read from the frames

<!-- gen:calendar -->
| Grade | Course | Course-level check days (weeks) | Units end (week) |
|---|---|---|---|
| K | dance-grades-k-to-2 | Year K mid-year (week 18 week 18, Year K year-end (week 26 week 26 | 32 |
| K | media-arts-grades-k-to-2 | Year K mid-year (week 21 week 21, Year K year-end (week 27 week 27 | 32 |
| K | music-grades-k-to-2 | Year K mid-year (week 19 week 19, Year K year-end (week 25 week 25 | 32 |
| K | theater-grades-k-to-2 | Year K mid-year (week 19 week 19, Year K year-end (week 27 week 27 | 32 |
| K | visual-arts-grades-k-to-2 | Year K mid-year (week 18 week 18, Year K year-end (week 26 week 26 | 32 |
| K | computer-science-kindergarten | Course-level check, mid- week 12, Course-level check, year week 27 | 32 |
| K | english-language-arts-kindergarten | Check 1 week 16, Check 2 week 32 | 32 |
| K | english-language-development-grades-k-to-2 | Kindergarten mid-year (w week 18, Kindergarten year-end (w week 28 | 32 |
| K | health-grades-k-to-2 | Kindergarten mid-year ch week 12, Kindergarten year-end ch week 27 | 26 |
| K | library-and-research-skills-kindergarten | 1, mid-year week 13, 2, year-end weeks 27 to 28 | 26 |
| K | math-kindergarten | Mid-year course-level ch week 17, Year-end course-level ch week 31 | 31 |
| K | physical-education-grades-k-to-2 | Kindergarten mid-year (w week 18, Kindergarten year-end (w week 28 | 32 |
| K | science-kindergarten | Course-level check, mid- week 14, Course-level check, year week 29 | 28 |
| K | social-and-emotional-learning-grades-k-to-2 | Kindergarten mid-year ch week 11, Kindergarten year-end ch week 26 | 32 |
| K | social-studies-kindergarten | 1, mid-year week 15, 2, year-end week 30 | 29 |
| 1 | dance-grades-k-to-2 | Year 1 mid-year (week 17 week 17, Year 1 year-end (week 25 week 25 | 32 |
| 1 | media-arts-grades-k-to-2 | Year 1 mid-year (week 21 week 21, Year 1 year-end (week 27 week 27 | 32 |
| 1 | music-grades-k-to-2 | Year 1 mid-year (week 17 week 17, Year 1 year-end (week 25 week 25 | 32 |
| 1 | theater-grades-k-to-2 | Year 1 mid-year (week 20 week 20, Year 1 year-end (week 27 week 27 | 32 |
| 1 | visual-arts-grades-k-to-2 | Year 1 mid-year (week 18 week 18, Year 1 year-end (week 26 week 26 | 32 |
| 1 | computer-science-grade-1 | Course-level check, mid- week 13, Course-level check, year week 27 | 32 |
| 1 | english-language-arts-grade-1 | Check 1 week 16, Check 2 week 32 | 32 |
| 1 | english-language-development-grades-k-to-2 | Grade 1 mid-year (week 1 week 18, Grade 1 year-end (week 2 week 28 | 32 |
| 1 | health-grades-k-to-2 | Grade 1 mid-year check ( week 11, Grade 1 year-end check ( week 27 | 26 |
| 1 | library-and-research-skills-grade-1 | 1, mid-year week 13, 2, year-end week 28 | 27 |
| 1 | math-grade-1 | Mid-year course-level ch week 19, Year-end course-level ch week 30 | 32 |
| 1 | physical-education-grades-k-to-2 | Grade 1 mid-year (week 1 week 18, Grade 1 year-end (week 2 week 28 | 32 |
| 1 | science-grade-1 | Course-level check, mid- week 15, Course-level check, year week 29 | 28 |
| 1 | social-and-emotional-learning-grades-k-to-2 | Grade 1 mid-year check ( week 9, Grade 1 year-end check ( week 26 | 32 |
| 1 | social-studies-grade-1 | 1, mid-year week 14, 2, year-end week 31 | 31 |
| 2 | dance-grades-k-to-2 | Year 2 mid-year (week 17 week 17, Year 2 year-end (week 25 week 25 | 32 |
| 2 | media-arts-grades-k-to-2 | Year 2 mid-year (week 21 week 21, Year 2 year-end (week 27 week 27 | 32 |
| 2 | music-grades-k-to-2 | Year 2 mid-year (week 17 week 17, Year 2 year-end (week 25 week 25 | 32 |
| 2 | theater-grades-k-to-2 | Year 2 mid-year (week 17 week 17, Year 2 year-end (week 27 week 27 | 32 |
| 2 | visual-arts-grades-k-to-2 | Year 2 mid-year (week 17 week 17, Year 2 year-end (week 26 week 26 | 32 |
| 2 | computer-science-grade-2 | Course-level check, mid- week 11, Course-level check, year week 26 | 32 |
| 2 | english-language-arts-grade-2 | Check 1 weeks 15 to 16, Check 2 week 32 | 32 |
| 2 | english-language-development-grades-k-to-2 | Grade 2 mid-year (week 1 week 17, Grade 2 year-end (week 2 week 27 | 32 |
| 2 | health-grades-k-to-2 | Grade 2 mid-year check ( week 11, Grade 2 year-end check ( week 27 | 26 |
| 2 | library-and-research-skills-grade-2 | 1, mid-year week 13, 2, year-end week 27 | 26 |
| 2 | math-grade-2 | Mid-year course-level ch weeks 18 to 19, Year-end course-level ch week 29 | 32 |
| 2 | physical-education-grades-k-to-2 | Grade 2 mid-year (week 1 week 17, Grade 2 year-end (week 2 week 27 | 32 |
| 2 | science-grade-2 | Course-level check, mid- week 20, Course-level check, year week 28 | 27 |
| 2 | social-and-emotional-learning-grades-k-to-2 | Grade 2 mid-year check ( week 10, Grade 2 year-end check ( week 26 | 32 |
| 2 | social-studies-grade-2 | 1, mid-year (week 14) week 14, 2, year-end week 31 | 30 |
| 3 | dance-grades-3-to-5 | Year 3 mid-year (week 17 week 17, Year 3 year-end (week 26 week 26 | 32 |
| 3 | media-arts-grades-3-to-5 | Year 3 mid-year (week 17 week 17, Year 3 year-end (week 26 week 26 | 32 |
| 3 | music-grades-3-to-5 | Year 3 mid-year (week 15 week 15, Year 3 year-end (week 24 week 24 | 32 |
| 3 | theater-grades-3-to-5 | Year 3 mid-year (week 17 week 17, Year 3 year-end (week 27 week 27 | 32 |
| 3 | visual-arts-grades-3-to-5 | Year 3 mid-year (week 18 week 18, Year 3 year-end (week 26 week 26 | 32 |
| 3 | computer-science-grade-3 | Course-level check, mid- week 11, Course-level check, year week 26 | 32 |
| 3 | english-language-arts-grade-3 | Check 1 week 16, Check 2 week 32 | 32 |
| 3 | english-language-development-grades-3-to-5 | Grade 3 mid-year (week 1 week 19, Grade 3 year-end (week 2 week 27 | 32 |
| 3 | health-grades-3-to-5 | Grade 3 mid-year check ( week 15, Grade 3 year-end check ( week 29 | 28 |
| 3 | library-and-research-skills-grade-3 | 1, mid-year week 13, 2, year-end week 29 | 28 |
| 3 | math-grade-3 | Check 1 week 12, Check 2 week 23, Check 3 week 31 | 30 |
| 3 | physical-education-grades-3-to-5 | Grade 3 mid-year (week 1 week 18, Grade 3 year-end (week 2 week 26 | 32 |
| 3 | science-grade-3 | Course-level check 1 week 9, Course-level check 2 week 20, Course-level check 3 week 30 | 30 |
| 3 | social-and-emotional-learning-grades-3-to-5 | Grade 3 mid-year check ( week 10, Grade 3 year-end check ( week 26 | 32 |
| 3 | social-studies-grade-3 | 1 week 14, 2, mid-year week 25, 3, year-end (week 28, be week 28 | 32 |
| 4 | dance-grades-3-to-5 | Year 4 mid-year (week 17 week 17, Year 4 year-end (week 26 week 26 | 32 |
| 4 | media-arts-grades-3-to-5 | Year 4 mid-year (week 17 week 17, Year 4 year-end (week 25 week 25 | 32 |
| 4 | music-grades-3-to-5 | Year 4 mid-year (week 15 week 15, Year 4 year-end (week 24 week 24 | 32 |
| 4 | theater-grades-3-to-5 | Year 4 mid-year (week 17 week 17, Year 4 year-end (week 26 week 26 | 32 |
| 4 | visual-arts-grades-3-to-5 | Year 4 mid-year (week 17 week 17, Year 4 year-end (week 25 week 25 | 32 |
| 4 | computer-science-grade-4 | Course-level check, mid- week 11, Course-level check, year week 24 | 32 |
| 4 | english-language-arts-grade-4 | Check 1 week 16, Check 2 week 32 | 32 |
| 4 | english-language-development-grades-3-to-5 | Grade 4 mid-year (week 1 week 15, Grade 4 year-end (week 2 week 29 | 32 |
| 4 | health-grades-3-to-5 | Grade 4 mid-year check ( week 14, Grade 4 year-end check ( week 29 | 28 |
| 4 | library-and-research-skills-grade-4 | 1, mid-year week 14, 2, year-end week 29 | 28 |
| 4 | math-grade-4 | Check 1 week 12, Check 2 week 23, Check 3 week 31 | 30 |
| 4 | physical-education-grades-3-to-5 | Grade 4 mid-year (week 1 week 18, Grade 4 year-end (week 2 week 26 | 32 |
| 4 | science-grade-4 | Course-level check 1 week 10, Course-level check 2 week 19, Course-level check 3 week 30 | 30 |
| 4 | social-and-emotional-learning-grades-3-to-5 | Grade 4 mid-year check ( week 15, Grade 4 year-end check ( week 26 | 32 |
| 4 | social-studies-grade-4 | 1 (week 8, after unit 2) week 8, 2, mid-year week 21, 3, year-end (week 27, be week 27 | 32 |
| 5 | dance-grades-3-to-5 | Year 5 mid-year (week 18 week 18, Year 5 year-end (week 26 week 26 | 32 |
| 5 | media-arts-grades-3-to-5 | Year 5 mid-year (week 18 week 18, Year 5 year-end (week 25 week 25 | 32 |
| 5 | music-grades-3-to-5 | Year 5 mid-year (week 15 week 15, Year 5 year-end (week 24 week 24 | 32 |
| 5 | theater-grades-3-to-5 | Year 5 mid-year (week 18 week 18, Year 5 year-end (week 27 week 27 | 32 |
| 5 | visual-arts-grades-3-to-5 | Year 5 mid-year (week 18 week 18, Year 5 year-end (week 26 week 26 | 32 |
| 5 | computer-science-grade-5 | Course-level check, mid- week 18, Course-level check, year week 25 | 32 |
| 5 | english-language-arts-grade-5 | Check 1 week 17, Check 2 week 32 | 32 |
| 5 | english-language-development-grades-3-to-5 | Grade 5 mid-year (week 1 week 18, Grade 5 year-end (week 2 week 28 | 32 |
| 5 | health-grades-3-to-5 | Grade 5 mid-year check ( week 15, Grade 5 year-end check ( week 28 | 27 |
| 5 | library-and-research-skills-grade-5 | 1, mid-year week 14, 2, year-end week 28 | 27 |
| 5 | math-grade-5 | Check 1 week 11, Check 2 week 22, Check 3 week 31 | 30 |
| 5 | physical-education-grades-3-to-5 | Grade 5 mid-year (week 1 week 18, Grade 5 year-end (week 2 week 26 | 32 |
| 5 | science-grade-5 | Course-level check 1 (we week 10, Course-level check 2 week 21, Course-level check 3 week 30 | 30 |
| 5 | social-and-emotional-learning-grades-3-to-5 | Grade 5 mid-year check ( week 15, Grade 5 year-end check ( week 26 | 32 |
| 5 | social-studies-grade-5 | 1, mid-year week 16, 2, year-end week 29 | 32 |
| 6 | dance-grades-6-to-8 | Year 6 mid-year (week 17 week 17, Year 6 year-end (week 32 week 32 | 31 |
| 6 | media-arts-grades-6-to-8 | Year 6 mid-year (week 17 week 17, Year 6 year-end (week 32 week 32 | 31 |
| 6 | music-grades-6-to-8 | Year 6 mid-year (week 19 week 19, Year 6 year-end (week 32 week 32 | 31 |
| 6 | theater-grades-6-to-8 | Year 6 mid-year (week 17 week 17, Year 6 year-end (week 32 week 32 | 31 |
| 6 | visual-arts-grades-6-to-8 | Year 6 mid-year (week 17 week 17, Year 6 year-end (week 32 week 32 | 31 |
| 6 | computer-science-grade-6 | Course-level check, mid- week 19, Course-level check, year week 32 | 31 |
| 6 | english-language-arts-grade-6 | Check 1 week 12, Check 2 week 22, Check 3 week 32 | 32 |
| 6 | english-language-development-grades-6-to-8 | Grade 6 mid-year (week 1 week 17, Grade 6 year-end (week 3 week 32 | 32 |
| 6 | health-grades-6-to-8 | Grade 6 mid-year check ( week 17, Grade 6 year-end check ( week 32 | 31 |
| 6 | library-and-research-skills-grades-6-to-8 | 1, mid-year, grade 6 week 20, 2, year-end, grade 6 week 31 | 29 |
| 6 | math-grade-6 | Check 1 (day 80; respond week 16, Check 2 (day 118; respon week 24, Check 3 (days 158 and 15 week 32 | 32 |
| 6 | physical-education-grades-6-to-8 | Grade 6 mid-year (week 1 week 17, Grade 6 year-end (week 3 week 32 | 31 |
| 6 | science-grade-6 | Course-level check 1, mi week 18, Course-level check 2, ye week 32 | 32 |
| 6 | social-and-emotional-learning-grades-6-to-8 | Grade 6 mid-year check ( week 15, Grade 6 year-end check ( week 32 | 31 |
| 6 | world-geography-and-ancient-civilizations-i | 1 (mid-year) week 15, 2 (mid-year) week 23, 3 (year-end) week 32 | 32 |
| 7 | dance-grades-6-to-8 | Year 7 mid-year (week 17 week 17, Year 7 year-end (week 32 week 32 | 31 |
| 7 | media-arts-grades-6-to-8 | Year 7 mid-year (week 17 week 17, Year 7 year-end (week 32 week 32 | 31 |
| 7 | music-grades-6-to-8 | Year 7 mid-year (week 19 week 19, Year 7 year-end (week 32 week 32 | 31 |
| 7 | theater-grades-6-to-8 | Year 7 mid-year (week 17 week 17, Year 7 year-end (week 32 week 32 | 31 |
| 7 | visual-arts-grades-6-to-8 | Year 7 mid-year (week 17 week 17, Year 7 year-end (week 32 week 32 | 31 |
| 7 | computer-science-grade-7 | Course-level check, mid- week 16, Course-level check, year week 32 | 31 |
| 7 | english-language-arts-grade-7 | Check 1 week 12, Check 2 week 22, Check 3 week 32 | 32 |
| 7 | english-language-development-grades-6-to-8 | Grade 7 mid-year (weeks  weeks 17 to 18, Grade 7 year-end (week 3 week 32 | 32 |
| 7 | health-grades-6-to-8 | Grade 7 mid-year check ( week 17, Grade 7 year-end check ( week 32 | 31 |
| 7 | library-and-research-skills-grades-6-to-8 | 3, mid-year, grade 7 week 18, 4, year-end, grade 7 week 31 | 29 |
| 7 | math-grade-7 | Check 1 (day 45; respond week 9, Check 2 (day 119; respon week 24, Check 3 (days 158 and 15 week 32 | 32 |
| 7 | physical-education-grades-6-to-8 | Grade 7 mid-year (week 1 week 17, Grade 7 year-end (week 3 week 32 | 31 |
| 7 | science-grade-7 | Course-level check 1, mi week 14, Course-level check 2, ye week 32 | 32 |
| 7 | social-and-emotional-learning-grades-6-to-8 | Grade 7 mid-year check ( week 15, Grade 7 year-end check ( week 32 | 31 |
| 7 | world-geography-and-ancient-civilizations-ii | 1 (mid-year) week 13, 2 (mid-year) week 24, 3 (year-end) week 32 | 32 |
| 8 | dance-grades-6-to-8 | Year 8 mid-year (week 17 week 17, Year 8 year-end (week 32 week 32 | 31 |
| 8 | media-arts-grades-6-to-8 | Year 8 mid-year (week 17 week 17, Year 8 year-end (week 32 week 32 | 31 |
| 8 | music-grades-6-to-8 | Year 8 mid-year (week 19 week 19, Year 8 year-end (week 32 week 32 | 31 |
| 8 | theater-grades-6-to-8 | Year 8 mid-year (week 17 week 17, Year 8 year-end (week 32 week 32 | 31 |
| 8 | visual-arts-grades-6-to-8 | Year 8 mid-year (week 17 week 17, Year 8 year-end (week 32 week 32 | 31 |
| 8 | computer-science-grade-8 | Course-level check, mid- week 15, Course-level check, year week 32 | 31 |
| 8 | career-exploration-grades-6-to-8 | Course-level check 1, mi week 16, Course-level check 2, ye week 32 | 32 |
| 8 | english-language-arts-grade-8 | Check 1 week 18, Check 2 weeks 25 to 26, Check 3 week 32 | 32 |
| 8 | english-language-development-grades-6-to-8 | Grade 8 mid-year (week 2 week 20, Grade 8 year-end (week 3 week 32 | 32 |
| 8 | health-grades-6-to-8 | Grade 8 mid-year check ( week 17, Grade 8 year-end check ( week 32 | 31 |
| 8 | library-and-research-skills-grades-6-to-8 | 5, mid-year, grade 8 week 16, 6, year-end, grade 8 week 31 | 29 |
| 8 | math-grade-8 | Check 1 (day 70; respond week 14, Check 2 (day 116; respon week 24, Check 3 (days 158 and 15 week 32 | 32 |
| 8 | physical-education-grades-6-to-8 | Grade 8 mid-year (week 1 week 17, Grade 8 year-end (week 3 week 32 | 31 |
| 8 | science-grade-8 | Course-level check 1, mi week 15, Course-level check 2, ye week 32 | 32 |
| 8 | social-and-emotional-learning-grades-6-to-8 | Grade 8 mid-year check ( week 16, Grade 8 year-end check ( week 32 | 31 |
| 8 | civics-government-and-civic-life | 1 (mid-year) week 10, 2 (mid-year) week 20, 3 (year-end) weeks 29 to 30 | 32 |
| 9 | computer-science-grade-9 | Course-level check, mid- week 17, Course-level check, year week 32 | 31 |
| 9 | english-language-arts-grade-9 | Check 1 week 13, Check 2 week 20, Check 3 week 32 | 31 |
| 9 | english-language-development-grades-9-to-12 | Grade 9 mid-year (week 1 week 17, Grade 9 year-end (week 3 week 32 | 32 |
| 9 | health-grades-9-to-12 | Mid-course check (week 7 week 7, End-of-course check (wee week 16 | 16 |
| 9 | library-and-research-skills-grades-9-to-12 | 1, grade 9 mid-year week 15, 2, grade 9 year-end week 31 | 29 |
| 9 | algebra-i | Check 1 (weeks 12 to 13) weeks 12 to 13, Check 2 (week 22) week 22, Check 3 (week 32) week 32 | 32 |
| 9 | physical-education-grades-9-to-12 | Grade 9 mid-year (week 1 week 16, Grade 9 year-end (week 3 week 32 | 31 |
| 9 | biology | Course-level check 1 week 9, Course-level check 2, mi week 16, Course-level check 3, ye week 32 | 31 |
| 9 | social-and-emotional-learning-grades-9-to-12 | Grade 9 mid-year check ( week 15, Grade 9 year-end check ( week 32 | 31 |
| 9 | world-history-i | 1, course-level check (w week 10, 2, mid-year course-level weeks 18 to 19, 3, year-end course-level week 32 | 31 |
| 10 | computer-science-grade-10 | Course-level check, mid- weeks 15 to 16, Course-level check, year weeks 31 to 32 | 31 |
| 10 | career-pathways-grades-9-to-12 | Course-level check 1, mi week 14, Course-level check 2, ye week 32 | 32 |
| 10 | english-language-arts-grade-10 | Check 1 week 9, Check 2 week 18, Check 3 week 32 | 31 |
| 10 | english-language-development-grades-9-to-12 | Grade 10 mid-year (week  week 17, Grade 10 year-end (week  week 32 | 32 |
| 10 | library-and-research-skills-grades-9-to-12 | 3, grade 10 mid-year week 15, 4, grade 10 year-end week 31 | 29 |
| 10 | geometry | Check 1 (week 10) week 10, Check 2 (week 21) week 21, Check 3 (week 32) week 32 | 32 |
| 10 | physical-education-grades-9-to-12 | Grade 10 mid-year (week  week 16, Grade 10 year-end (week  week 32 | 31 |
| 10 | chemistry | Course-level check 1 week 11, Course-level check 2, mi weeks 20 to 21, Course-level check 3, ye week 32 | 31 |
| 10 | social-and-emotional-learning-grades-9-to-12 | Grade 10 mid-year check  week 15, Grade 10 year-end check  week 32 | 31 |
| 10 | world-history-ii | 1, course-level check (w weeks 8 to 9, 2, mid-year course-level weeks 18 to 19, 3, year-end course-level week 32 | 32 |
| 11 | computer-science-grade-11 | Course-level check, mid- week 18, Course-level check, year week 32 | 31 |
| 11 | english-language-arts-grade-11 | Check 1 week 16, Check 2 week 24, Check 3 week 32 | 31 |
| 11 | english-language-development-grades-9-to-12 | Grade 11 mid-year (week  week 17, Grade 11 year-end (week  week 32 | 32 |
| 11 | library-and-research-skills-grades-9-to-12 | 5, grade 11 mid-year week 11, 6, grade 11 year-end week 31 | 29 |
| 11 | algebra-ii | Check 1 (weeks 14 to 15) weeks 14 to 15, Check 2 (weeks 22 to 23) weeks 22 to 23, Check 3 (week 32) week 32 | 32 |
| 11 | physical-education-grades-9-to-12 | Grade 11 mid-year (week  week 16, Grade 11 year-end (week  week 32 | 31 |
| 11 | physics | Course-level check 1 week 13, Course-level check 2, mi week 22, Course-level check 3, ye week 32 | 31 |
| 11 | social-and-emotional-learning-grades-9-to-12 | Grade 11 mid-year check  week 15, Grade 11 year-end check  week 32 | 31 |
| 11 | us-history-i | 1 (week 10) week 10, 2, mid-year (weeks 19 to week 19, 3, year-end (week 32) week 32 | 31 |
| 12 | computer-science-grade-12 | Course-level check 1, af week 12, Course-level check 2, ye week 28 | 32 |
| 12 | english-language-arts-grade-12 | Check 1 week 11, Check 2 week 17, Check 3 week 25 | 32 |
| 12 | english-language-development-grades-9-to-12 | Grade 12 mid-year (week  week 16, Grade 12 year-end (week  week 32 | 32 |
| 12 | library-and-research-skills-grades-9-to-12 | 7, grade 12 mid-year week 13, 8, grade 12 year-end week 31 | 29 |
| 12 | calculus | Check 1, mid-year (week  week 17, Check 2 (weeks 24 to 25) weeks 24 to 25, Check 3, year-end (week  week 32 | 32 |
| 12 | precalculus | Check 1 (week 10, days 4 week 10, Check 2 (weeks 20 to 21, week 20, Check 3 (week 32, days 1 week 32 | 32 |
| 12 | statistics | Check 1 (weeks 9 to 10) week 9, Check 2 (weeks 18 to 19) weeks 18 to 19, Check 3 (weeks 30 to 31) week 30 | 32 |
| 12 | physical-education-grades-9-to-12 | Grade 12 mid-year (week  week 16, Grade 12 year-end (week  week 28 | 32 |
| 12 | earth-and-space-science | Course-level check 1 week 11, Course-level check 2, mi week 21, Course-level check 3, ye week 32 | 31 |
| 12 | environmental-science | Course-level check 1 week 11, Course-level check 2, mi week 21, Course-level check 3, ye week 32 | 31 |
| 12 | social-and-emotional-learning-grades-9-to-12 | Grade 12 mid-year check  week 15, Grade 12 year-end check  week 32 | 31 |
| 12 | economics | 1, midpoint week 23, 2, final week 32 | 32 |
| 12 | psychology | 1, mid-year week 17, 2, year-end week 32 | 32 |
| 12 | us-government-and-politics | 1, midpoint week 8, 2, final week 15 | 16 |
| 12 | us-history-ii | 1 week 8, 2, mid-year (days 84 and week 17, 3, year-end week 30 | 32 |
| 9-12 Level 1 | dance-grades-9-to-12 | Level 1 mid-year (week 1 week 17, Level 1 year-end (week 3 week 32 | 32 |
| 9-12 Level 2 | dance-grades-9-to-12 | Level 2 mid-year (week 1 week 17, Level 2 year-end (week 3 week 32 | 32 |
| 9-12 Level 3 | dance-grades-9-to-12 | Level 3 mid-year (week 1 week 17, Level 3 year-end (week 3 week 32 | 32 |
| 9-12 Level 4 | dance-grades-9-to-12 | Level 4 checkpoint 1, mi week 15, Level 4 checkpoint 2, ye week 28 | 32 |
| 9-12 Level 1 | media-arts-grades-9-to-12 | Level 1 mid-year (week 1 week 16, Level 1 year-end (week 3 week 32 | 32 |
| 9-12 Level 2 | media-arts-grades-9-to-12 | Level 2 mid-year (week 1 week 16, Level 2 year-end (week 3 week 32 | 32 |
| 9-12 Level 3 | media-arts-grades-9-to-12 | Level 3 mid-year (week 1 week 16, Level 3 year-end (week 3 week 32 | 32 |
| 9-12 Level 4 | media-arts-grades-9-to-12 | Level 4 mid-year checkpo week 16, Level 4 year-end (week 3 week 32 | 32 |
| 9-12 Level 1 | music-grades-9-to-12 | Level 1 mid-year (week 1 week 16, Level 1 year-end (week 3 week 32 | 32 |
| 9-12 Level 2 | music-grades-9-to-12 | Level 2 mid-year (week 1 week 16, Level 2 year-end (week 3 week 32 | 32 |
| 9-12 Level 3 | music-grades-9-to-12 | Level 3 mid-year (week 1 week 16, Level 3 year-end (week 3 week 32 | 32 |
| 9-12 Level 4 | music-grades-9-to-12 | Level 4 mid-year (week 1 week 16, Level 4 year-end (week 3 week 32 | 32 |
| 9-12 Level 1 | theater-grades-9-to-12 | Level 1 mid-year (week 1 week 17, Level 1 year-end (week 3 week 32 | 32 |
| 9-12 Level 2 | theater-grades-9-to-12 | Level 2 mid-year (week 1 week 16, Level 2 year-end (week 3 week 32 | 32 |
| 9-12 Level 3 | theater-grades-9-to-12 | Level 3 mid-year (week 1 week 16, Level 3 year-end (week 3 week 32 | 32 |
| 9-12 Level 4 | theater-grades-9-to-12 | Level 4 mid-year (week 1 week 16, Level 4 year-end (week 3 week 32 | 32 |
| 9-12 Level 1 | visual-arts-grades-9-to-12 | Level 1 mid-year week 16, Level 1 year-end week 32 | 32 |
| 9-12 Level 2 | visual-arts-grades-9-to-12 | Level 2 mid-year week 16, Level 2 year-end week 32 | 32 |
| 9-12 Level 3 | visual-arts-grades-9-to-12 | Level 3 mid-year week 16, Level 3 year-end week 32 | 32 |
| 9-12 Level 4 | visual-arts-grades-9-to-12 | Level 4 mid-year week 16, Level 4 year-end week 32 | 32 |

Stagger rule breaks (K to 5 by week, 6 to 8 by school day before the finals week): grade K week 12 (computer-science-kindergarten, health-grades-k-to-2); grade K week 18 (dance-grades-k-to-2, english-language-development-grades-k-to-2, physical-education-grades-k-to-2, visual-arts-grades-k-to-2); grade K week 19 (music-grades-k-to-2, theater-grades-k-to-2); grade K week 26 (dance-grades-k-to-2, social-and-emotional-learning-grades-k-to-2, visual-arts-grades-k-to-2); grade K week 27 (computer-science-kindergarten, health-grades-k-to-2, library-and-research-skills-kindergarten, media-arts-grades-k-to-2, theater-grades-k-to-2); grade K week 28 (english-language-development-grades-k-to-2, library-and-research-skills-kindergarten, physical-education-grades-k-to-2); grade 1 week 13 (computer-science-grade-1, library-and-research-skills-grade-1); grade 1 week 17 (dance-grades-k-to-2, music-grades-k-to-2); grade 1 week 18 (english-language-development-grades-k-to-2, physical-education-grades-k-to-2, visual-arts-grades-k-to-2); grade 1 week 25 (dance-grades-k-to-2, music-grades-k-to-2); grade 1 week 26 (social-and-emotional-learning-grades-k-to-2, visual-arts-grades-k-to-2); grade 1 week 27 (computer-science-grade-1, health-grades-k-to-2, media-arts-grades-k-to-2, theater-grades-k-to-2); grade 1 week 28 (english-language-development-grades-k-to-2, library-and-research-skills-grade-1, physical-education-grades-k-to-2); grade 2 week 11 (computer-science-grade-2, health-grades-k-to-2); grade 2 week 17 (dance-grades-k-to-2, english-language-development-grades-k-to-2, music-grades-k-to-2, physical-education-grades-k-to-2, theater-grades-k-to-2, visual-arts-grades-k-to-2); grade 2 week 25 (dance-grades-k-to-2, music-grades-k-to-2); grade 2 week 26 (computer-science-grade-2, social-and-emotional-learning-grades-k-to-2, visual-arts-grades-k-to-2); grade 2 week 27 (english-language-development-grades-k-to-2, health-grades-k-to-2, library-and-research-skills-grade-2, media-arts-grades-k-to-2, physical-education-grades-k-to-2, theater-grades-k-to-2); grade 3 week 15 (health-grades-3-to-5, music-grades-3-to-5); grade 3 week 17 (dance-grades-3-to-5, media-arts-grades-3-to-5, theater-grades-3-to-5); grade 3 week 18 (physical-education-grades-3-to-5, visual-arts-grades-3-to-5); grade 3 week 26 (computer-science-grade-3, dance-grades-3-to-5, media-arts-grades-3-to-5, physical-education-grades-3-to-5, social-and-emotional-learning-grades-3-to-5, visual-arts-grades-3-to-5); grade 3 week 27 (english-language-development-grades-3-to-5, theater-grades-3-to-5); grade 3 week 29 (health-grades-3-to-5, library-and-research-skills-grade-3); grade 4 week 14 (health-grades-3-to-5, library-and-research-skills-grade-4); grade 4 week 15 (english-language-development-grades-3-to-5, music-grades-3-to-5, social-and-emotional-learning-grades-3-to-5); grade 4 week 17 (dance-grades-3-to-5, media-arts-grades-3-to-5, theater-grades-3-to-5, visual-arts-grades-3-to-5); grade 4 week 24 (computer-science-grade-4, music-grades-3-to-5); grade 4 week 25 (media-arts-grades-3-to-5, visual-arts-grades-3-to-5); grade 4 week 26 (dance-grades-3-to-5, physical-education-grades-3-to-5, social-and-emotional-learning-grades-3-to-5, theater-grades-3-to-5); grade 4 week 29 (english-language-development-grades-3-to-5, health-grades-3-to-5, library-and-research-skills-grade-4); grade 5 week 15 (health-grades-3-to-5, music-grades-3-to-5, social-and-emotional-learning-grades-3-to-5); grade 5 week 18 (computer-science-grade-5, dance-grades-3-to-5, english-language-development-grades-3-to-5, media-arts-grades-3-to-5, physical-education-grades-3-to-5, theater-grades-3-to-5, visual-arts-grades-3-to-5); grade 5 week 25 (computer-science-grade-5, media-arts-grades-3-to-5); grade 5 week 26 (dance-grades-3-to-5, physical-education-grades-3-to-5, social-and-emotional-learning-grades-3-to-5, visual-arts-grades-3-to-5); grade 5 week 28 (english-language-development-grades-3-to-5, health-grades-3-to-5, library-and-research-skills-grade-5); grade 6 day 82 (english-language-development-grades-6-to-8, physical-education-grades-6-to-8); grade 6 day 83 (dance-grades-6-to-8, media-arts-grades-6-to-8, physical-education-grades-6-to-8, theater-grades-6-to-8, visual-arts-grades-6-to-8); grade 6 day 84 (health-grades-6-to-8, physical-education-grades-6-to-8); grade 7 day 83 (dance-grades-6-to-8, media-arts-grades-6-to-8, physical-education-grades-6-to-8, theater-grades-6-to-8, visual-arts-grades-6-to-8); grade 7 day 84 (health-grades-6-to-8, physical-education-grades-6-to-8); grade 8 day 83 (dance-grades-6-to-8, media-arts-grades-6-to-8, physical-education-grades-6-to-8, theater-grades-6-to-8, visual-arts-grades-6-to-8); grade 8 day 84 (health-grades-6-to-8, physical-education-grades-6-to-8).
<!-- /gen -->
