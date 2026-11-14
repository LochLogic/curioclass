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
| 2 | 15 to 16, 32 | 18 to 19, 29 | 17, 28 | 14, 31 |
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
| K | english-language-arts-kindergarten | Check 1 week 16, Check 2 week 32 | 32 |
| K | math-kindergarten | Mid-year course-level ch week 17, Year-end course-level ch week 31 | 31 |
| K | science-kindergarten | Course-level check, mid- week 14, Course-level check, year week 29 | 28 |
| K | social-studies-kindergarten | 1, mid-year week 15, 2, year-end week 30 | 29 |
| 1 | english-language-arts-grade-1 | Check 1 week 16, Check 2 week 32 | 32 |
| 1 | math-grade-1 | Mid-year course-level ch week 19, Year-end course-level ch week 30 | 32 |
| 1 | science-grade-1 | Course-level check, mid- week 15, Course-level check, year week 29 | 28 |
| 1 | social-studies-grade-1 | 1, mid-year week 14, 2, year-end week 31 | 31 |
| 2 | english-language-arts-grade-2 | Check 1 weeks 15 to 16, Check 2 week 32 | 32 |
| 2 | math-grade-2 | Mid-year course-level ch weeks 18 to 19, Year-end course-level ch week 29 | 32 |
| 2 | science-grade-2 | Course-level check, mid- week 17, Course-level check, year week 28 | 28 |
| 2 | social-studies-grade-2 | 1, mid-year (week 14) week 14, 2, year-end week 31 | 30 |
| 3 | english-language-arts-grade-3 | Check 1 week 16, Check 2 week 32 | 32 |
| 3 | math-grade-3 | Check 1 week 12, Check 2 week 23, Check 3 week 31 | 30 |
| 3 | science-grade-3 | Course-level check 1 week 9, Course-level check 2 week 20, Course-level check 3 week 30 | 30 |
| 3 | social-studies-grade-3 | 1 week 14, 2, mid-year week 25, 3, year-end (week 28, be week 28 | 32 |
| 4 | english-language-arts-grade-4 | Check 1 week 16, Check 2 week 32 | 32 |
| 4 | math-grade-4 | Check 1 week 12, Check 2 week 23, Check 3 week 31 | 30 |
| 4 | science-grade-4 | Course-level check 1 week 10, Course-level check 2 week 19, Course-level check 3 week 30 | 30 |
| 4 | social-studies-grade-4 | 1 (week 8, after unit 2) week 8, 2, mid-year week 21, 3, year-end (week 27, be week 27 | 32 |
| 5 | english-language-arts-grade-5 | Check 1 week 17, Check 2 week 32 | 32 |
| 5 | math-grade-5 | Check 1 week 11, Check 2 week 22, Check 3 week 31 | 30 |
| 5 | science-grade-5 | Course-level check 1 (we week 10, Course-level check 2 week 21, Course-level check 3 week 30 | 30 |
| 5 | social-studies-grade-5 | 1, mid-year week 16, 2, year-end week 29 | 32 |
| 6 | english-language-arts-grade-6 | Check 1 week 12, Check 2 week 22, Check 3 week 32 | 32 |
| 6 | math-grade-6 | Check 1 (day 80; respond week 16, Check 2 (day 118; respon week 24, Check 3 (days 158 and 15 week 32 | 32 |
| 6 | science-grade-6 | Course-level check 1, mi week 18, Course-level check 2, ye week 32 | 32 |
| 6 | world-geography-and-ancient-civilizations-i | 1 (mid-year) week 15, 2 (mid-year) week 23, 3 (year-end) week 32 | 32 |
| 7 | english-language-arts-grade-7 | Check 1 week 12, Check 2 week 22, Check 3 week 32 | 32 |
| 7 | math-grade-7 | Check 1 (day 45; respond week 9, Check 2 (day 119; respon week 24, Check 3 (days 158 and 15 week 32 | 32 |
| 7 | science-grade-7 | Course-level check 1, mi week 14, Course-level check 2, ye week 32 | 32 |
| 7 | world-geography-and-ancient-civilizations-ii | 1 (mid-year) week 13, 2 (mid-year) week 24, 3 (year-end) week 32 | 32 |
| 8 | english-language-arts-grade-8 | Check 1 week 18, Check 2 weeks 25 to 26, Check 3 week 32 | 32 |
| 8 | math-grade-8 | Check 1 (day 70; respond week 14, Check 2 (day 116; respon week 24, Check 3 (days 158 and 15 week 32 | 32 |
| 8 | science-grade-8 | Course-level check 1, mi week 15, Course-level check 2, ye week 32 | 32 |
| 8 | civics-government-and-civic-life | 1 (mid-year) week 10, 2 (mid-year) week 20, 3 (year-end) weeks 29 to 30 | 32 |
| 9 | english-language-arts-grade-9 | Check 1 week 13, Check 2 week 20, Check 3 week 32 | 31 |
| 9 | algebra-i | Check 1 (weeks 12 to 13) weeks 12 to 13, Check 2 (week 22) week 22, Check 3 (week 32) week 32 | 32 |
| 9 | biology | Course-level check 1 week 9, Course-level check 2, mi week 16, Course-level check 3, ye week 32 | 31 |
| 9 | world-history-i | 1, course-level check (w week 10, 2, mid-year course-level weeks 18 to 19, 3, year-end course-level week 32 | 31 |
| 10 | english-language-arts-grade-10 | Check 1 week 9, Check 2 week 18, Check 3 week 32 | 31 |
| 10 | geometry | Check 1 (week 10) week 10, Check 2 (week 21) week 21, Check 3 (week 32) week 32 | 32 |
| 10 | chemistry | Course-level check 1 week 11, Course-level check 2, mi weeks 20 to 21, Course-level check 3, ye week 32 | 31 |
| 10 | world-history-ii | 1, course-level check (w weeks 8 to 9, 2, mid-year course-level weeks 18 to 19, 3, year-end course-level week 32 | 32 |
| 11 | english-language-arts-grade-11 | Check 1 week 16, Check 2 week 24, Check 3 week 32 | 31 |
| 11 | algebra-ii | Check 1 (weeks 14 to 15) weeks 14 to 15, Check 2 (weeks 22 to 23) weeks 22 to 23, Check 3 (week 32) week 32 | 32 |
| 11 | physics | Course-level check 1 week 13, Course-level check 2, mi week 22, Course-level check 3, ye week 32 | 31 |
| 11 | us-history-i | 1 (week 10) week 10, 2, mid-year (weeks 19 to week 19, 3, year-end (week 32) week 32 | 31 |
| 12 | english-language-arts-grade-12 | Check 1 week 11, Check 2 week 17, Check 3 week 25 | 32 |
| 12 | economics | 1, midpoint week 23, 2, final week 32 | 32 |
| 12 | us-government-and-politics | 1, midpoint week 8, 2, final week 15 | 16 |
| 12 | us-history-ii | 1 week 8, 2, mid-year (days 84 and week 17, 3, year-end week 30 | 32 |

Stagger rule breaks (K to 5 by week, 6 to 8 by school day before the finals week): none.
<!-- /gen -->
