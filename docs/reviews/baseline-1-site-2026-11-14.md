# Baseline 1, part C: the website design check (2026-11-14)

Reader: the curriculum expert (docs/agents/EXPERT.md), part C (`subject=site`) of docs/pipeline/briefs/baseline-1.md.
Proposals only: no file but this report was edited, nothing was rebuilt.

## What I read

- AGENTS.md; docs/HANDOFF.md (top blocks, "The folders", "How to work here"); docs/PRODUCTION-PATH.md steps 2 to 9;
  docs/GLOSSARY.md; docs/agents/EXPERT.md; docs/pipeline/briefs/baseline-1.md.
- The site design and build: docs/SITE-DESIGN.md (approved direction, 2026-11-12), scripts/build_site.py (catalogue
  load, grade, subject, standard and topic pages), scripts/build_db.py, scripts/lesson.py (build paths), wrangler.jsonc,
  site/templates/module.html, data/courses.csv, data/modules.csv (797 topics), data/units.csv, data/redirects.csv,
  data/plans/frames.csv, data/plans/math-4/days.csv, courses/math-4/ and build/lessons/math-4/ (folder shapes).
- scripts/frame.py (what the gate parses), docs/reviews/frame-cross-subject-2026-11-14.md ("Course ids"),
  docs/reviews/naming-scan-2026-11-12.md (Decision A).
- Course frames: math-grade-4 (whole), science-grade-7, english-language-arts-grade-10, us-history-i,
  us-government-and-politics, social-studies-kindergarten (headings, first lines, Units tables), and the **Days.**
  bullet of all 52.
- `python -X utf8 scripts/plan.py check`: no frame failures (notes only).
- Two small scripted counts (not saved): topic standards against the frames' Owned standards columns.

## Verdict

The approved site design (SITE-DESIGN.md) fits the course and the day, but not the hierarchy the frames now hold:
it has no unit page, its section URL still says `unit-<n.n>` from before the rename, course-level check and review
days have no place, and nothing joins a subject to its per-year courses. The built site is topic-first and keyed on
the catalogue's band ids (`math-k8`, `ss-k5`), so it has no course layer yet, which is as planned. Every fix is
small and data-led: write the frames' unit rows to CSV, use the frame slug in course URLs, add a unit page, and let
standard and topic pages say which course and unit teach them now, from the frames, before any day exists.

## Findings, most serious first

### 1. No unit page; the section URL uses the retired word
LAYER site. REPEAT new.
- **Where:** docs/SITE-DESIGN.md, "Page types": course page, day page, "Section page: `/courses/<course>/unit-<n.n>/`".
- **What is wrong:** the locked hierarchy is course, unit, section, day (GLOSSARY, 2026-11-12). The design has
  pages for course, section and day only; units exist only as rows that open on the course page. The section URL
  `unit-11.1` is the pre-rename word, so a teacher reading "unit 11" on a course page lands on a URL that names a
  section. The glossary puts the readiness check, end-of-unit assessment, record sheet, family note and sub-ready
  day at the unit, and every frame's Units table (10 columns, the same in all six frames read) carries the
  compelling question, what students learn, why here and teacher notes per unit. None of it has a page.
- **Why it matters:** the unit is what reviewers and teachers ask for by name (naming-scan Decision A). Without a
  unit page the per-unit pieces have nowhere to live, and the section page would have to carry them.
- **Fix:** in SITE-DESIGN.md replace the "Section page" subsection with:
  > ### Unit page: `/courses/<course>/unit-<n>/`
  > The unit's compelling question, its days and day range, what students learn, why this unit here, the standards
  > it owns, supplies and teacher notes; then the readiness check, the end-of-unit assessment, the record sheet, the
  > family note (English and Spanish), the sub-ready day, its sections with their days, and the unit's print bundle.
  >
  > ### Section page: `/courses/<course>/unit-<n>/section-<m>/`
  > The section's goal, its days, its opener and its print bundle. Small: most teachers arrive from the unit page.

  and change the day page breadcrumb to "course / unit / section / day N of 160". Day URLs stay flat
  (`/courses/<course>/day-<n>/`). The site is not launched, so no redirect is needed.

### 2. Course-level days have no place in the hierarchy
LAYER site, process. REPEAT new.
- **Where:** every frame's "Course-level checks" (math-grade-4: 4 check days, 4 respond days, 7 year-review days;
  ELA 9 to 11, US History I, World History I: 12 days; algebra-i: 9); data/plans/math-4/days.csv columns
  `stretch,unit`; SITE-DESIGN day page breadcrumb and "The year at a glance".
- **What is wrong:** between 4 and 15 days a course sit in no unit and no section. days.csv requires a `stretch` and
  a `unit` for every day, and the day page breadcrumb assumes both.
- **Why it matters:** the scope and sequence writers (step 3) will number these days and need a value to put in the
  two columns; the site needs a row for them in the year at a glance and a breadcrumb that does not invent a unit.
- **Fix:** (a) PRODUCTION-PATH step 3 and the scope and sequence brief: course-level days carry `stretch` = `C` and
  `unit` = blank in days.csv. (b) SITE-DESIGN, year at a glance: "Course-level checks, respond days and review days
  appear as their own rows in teaching order, between the units they follow." (c) Day page: "A course-level day's
  breadcrumb is course / Course-level check N / day."

### 3. Course URL slug: three ids for one course
LAYER site. REPEAT yes (frame-cross-subject-2026-11-14, "Course ids").
- **Where:** GLOSSARY "course" row and SITE-DESIGN (`/courses/math-4/`); frame slugs (`math-grade-4`); data/courses.csv
  (`math-k8`); topic page "Course" line (site/templates/module.html line 19, from `courses.csv`).
- **What is wrong:** the design's URL uses the old plan id; the frames use the per-year slug; the catalogue uses a
  band id that cannot name a year.
- **Why it matters:** the course URL is the one id a teacher sees and bookmarks; it should be fixed once, before
  launch, and be the same id as data/plans/<slug>/.
- **Fix:** course URLs are `/courses/<frame slug>/` (`/courses/math-grade-4/`, `/courses/us-history-i/`). In
  GLOSSARY, "course" row, code name cell: "`math-grade-4` (the frame slug) in docs/courses/, data/plans/ and
  `/courses/<slug>/`. Lag: `math-4` in courses/ and data/plans/ until math's turn (step 5); data/courses.csv
  `course_id` is the catalogue id". In SITE-DESIGN, replace `/courses/math-4/` and `/courses/math-4/day-74/` with
  `/courses/math-grade-4/...`. The catalogue to slug mapping is part B's (catalog_id column); the site reads it.

### 4. The course page lacks what a frame says
LAYER site. REPEAT new.
- **Where:** SITE-DESIGN "Course page" items 1 to 6, against the frame sections Seams, Cross-subject, Course-level
  checks, Source map and the **Days.** bullet.
- **What is wrong:** the design shows units, status and cards, but not: the course before and after this one (Seams:
  "Picked up from" and "Handed on to"); the courses alongside in the same year (Cross-subject); the course-level
  check plan; the credit for the base text (math-grade-4 adapts a CC BY text across 122 lesson days; CC BY needs the
  credit somewhere a reader sees it, and the light per-day credit alone does not name the whole); and the course's
  shape (minutes a day, days a week, full year or half: us-government-and-politics is 80 days, ELA K to 2 is about
  120 minutes in two blocks).
- **Why it matters:** a teacher placing a student or planning a year needs the before and after; a family needs the
  minutes and days a week for the 36-week home calendar the design promises; the credit is a licence term.
- **Fix:** add to SITE-DESIGN course page item 5: "Before and after: the course this one builds on and the course
  it leads to, each linked. Alongside: this grade's other core courses, with the weeks where they lean on this one."
  Add a card to item 4: "The shape: minutes a day, days a week, the year or half year, and the course-level checks
  with the units they follow." Add to item 6: "Credits: the base text, its licence and a link, once for the course."
  Public columns of a frame's Units table: unit and compelling question, days, what students learn, why this unit
  here, owned standards, supplies. Internal only: Skills ids, C3 cell text beyond the practices, Check set adds,
  For the lead.

### 5. Unit facts and course shape exist only as prose
LAYER site, gate. REPEAT new.
- **Where:** docs/courses/<slug>/frame.md Units tables; data/plans/frames.csv (`course,units,days` only); the
  **Days.** bullet (biology: "50-minute lessons, five a week, 32 weeks"; us-history-i: "A full year", no minutes;
  ELA 1: "about 120 minutes, five days a week, in two blocks").
- **What is wrong:** a course page builder would have to parse markdown tables and free wording. AGENTS.md says
  course facts live in data/plans/<course>/ as CSV.
- **Why it matters:** the site, the step 3 writers and the part B grade totals all need the same numbers; prose
  drifts and the gate cannot check it.
- **Fix:** extend `frame.py sync` to write data/plans/<slug>/units.csv (`unit,title,question,days,skills,standards`)
  from the Units table, and add columns to data/plans/frames.csv: `minutes,per_week,term` (term = year or half).
  `frame.py check` fails a frame whose **Days.** bullet gives no minutes or no days a week. The site reads these
  files, never the frame.

### 6. Day URLs by position will break when days are renumbered
LAYER site. REPEAT new.
- **Where:** SITE-DESIGN day URL `/courses/<course>/day-<n>/`, "Pick up where you left off"; math-grade-4 frame
  (9 units) against the held data/plans/math-4/days.csv (section 11.1 is days 89 to 93 of the old order).
- **What is wrong:** the day number is a position. The new frame already moves the built days; after launch any
  inserted or merged day renumbers every later URL and every saved "pick up" spot.
- **Why it matters:** teachers bookmark and share days; a silent shift lands them on the wrong lesson.
- **Fix:** keep `day-<n>` (teachers speak in day numbers), and add to SITE-DESIGN "Rules the design keeps": "Day
  numbers are fixed per edition of a course. When a scope and sequence renumbers days after launch, the build
  writes a data/redirects.csv row for each moved day from build/lessons/<course>/days-map.csv (day number to day
  file id), and Pick up where you left off stores the day file id, not the number."

### 7. Standard and topic pages can link to units now
LAYER site. REPEAT new.
- **Where:** SITE-DESIGN "Standard and topic pages (changed)" and "Build order" step 3 (Used in, after days).
- **What is found:** 523 of the 543 core topics in data/modules.csv share at least one standard with a unit's Owned
  standards in the 52 frames; 279 of them touch more than one unit. Of the 20 with no match, 12 are grade 12 math
  elective topics (no core course, expected), and math-4-adding-and-multiplying-fractions lists the parent codes
  4.NF.B.3 and 4.NF.B.4 while the frame owns the lettered parts.
- **Why it matters:** "Used in" need not wait for days: a teacher on a topic or standard page can see "Taught in
  Grade 4 Math, unit 3 (lessons coming)" today, which is honest and makes the course layer visible.
- **Fix:** Build order step 3 becomes "Used in, first at unit level from data/plans/<slug>/units.csv, then at day
  level as days are written". The match treats a parent code as covered by its lettered parts (the progression
  gate's rule).

### 8. About 20 K to 8 topics sit in a grade whose course does not teach them
LAYER site. REPEAT new.
- **Where:** data/modules.csv `grade` against the frames' Owned standards. Science: science-6-earth-sun-moon-system
  and science-6-gravity-and-the-solar-system (owned in grade 8), science-7-states-of-matter (grade 6),
  science-7-senses-and-the-brain (grade 8), science-8-analog-and-digital-signals and
  science-8-natural-hazards-and-human-impact (grade 6), science-8-human-impact-on-earth and
  science-8-evidence-of-rising-temperatures (grade 7). Social studies, for example
  social-studies-5-indigenous-peoples-of-north-america (grade 3), social-studies-2-money-saving-and-trade (grade 1),
  social-studies-1-old-objects-as-sources (K and 2), social-studies-4-inquiry-ladder (3 and 5).
- **What is wrong:** the grade cell drives the grade pages and the Word Wall grade pages, so a grade 6 science
  teacher following the course finds a topic the course teaches in grade 8.
- **Fix:** after step 3 for each subject, set each topic's `grade` to the grade of the course that owns its standards
  (a band such as `3-5` where two grades share it); module ids stay (data/modules/kept-ids.csv). A small gate in
  check_site.py notes any core topic whose grade has no owning frame.

### 9. Find pages do not show courses
LAYER site. REPEAT new.
- **Where:** scripts/build_site.py lines 278 to 304 (grade and subject pages built from topics, keyed by
  data/courses.csv band ids); SITE-DESIGN "The four doors" (Find folds in grades and subjects).
- **What is wrong:** the subject level of the hierarchy is a list of topics by grade; nothing lists a subject's
  courses in order, or a grade's four courses together.
- **Fix:** add to SITE-DESIGN under Find: "`/courses/` lists the core courses by subject (columns) and grade (rows),
  high school courses at their typical grade. A grade page opens with its core courses, then its topics. A subject
  page opens with its courses K to 12 in order, then topics by grade."

### 10. Unit pieces live in the first section's folder
LAYER site. REPEAT new.
- **Where:** courses/math-4/u01-1/, u02-1/, u03-1/, u11-1/ hold family.md, readiness.md and record.md; later sections
  do not.
- **What is wrong:** a unit page builder would have to know that unit pieces sit in section N.1.
- **Fix:** when step 4 plans units, unit pieces go in `courses/<course>/sNN/` (matching the `s` item ids and plan
  files `sNN.md`); the held grade 4 folders move at math's turn. Until then the builder reads section N.1.

### 11. The build order starts with one course though 52 frames exist
LAYER process. REPEAT new.
- **Where:** SITE-DESIGN "Build order" step 1 (grade 4 math only, behind `--courses`).
- **What is wrong:** written when grade 4 math was the only planned course. A frame-only course and unit page for
  all 52 core courses is now possible from findings 5 and 7, behind the same flag.
- **Why it matters:** seeing the 52 courses as pages tests this design against every subject (half-year courses,
  ELA's two blocks, course-level days) before step 3 writers fix the day shape.
- **Fix:** proposed new step 0: "Frame-only course and unit pages for the 52 core courses, behind `--courses`,
  every unit marked Lessons coming. Not deployed." Cory's call (below).

## Settled by the expert

| Item | Choice | Why |
|---|---|---|
| Day URL form | Keep `day-<n>`, frozen per edition, redirects on renumber | Teachers speak in day numbers; bookmarks must survive |
| Section URL | Nested under its unit, `section-<m>` | Mirrors the hierarchy; the section number is unit.m |
| Course-level day marker | `stretch` = `C`, `unit` blank | One letter, no clash with unit numbers |
| Public frame columns | Question, days, what students learn, why here, standards, supplies | The rest is planning language |
| Topic to unit match | Parent code covered by lettered parts | Same rule as the progression gate |
| Unit pieces folder | `courses/<course>/sNN/` | Matches the `s` ids that never change |

## For Cory

1. **SITE-DESIGN changes (findings 1, 2, 4, 6, 9):** a unit page, nested section URLs, course-level rows, before,
   after and alongside on the course page, a credits line, and day numbers fixed per edition. These change the
   approved design, so they wait for your yes.
2. **Frame-only course pages (finding 11):** build all 52 core course and unit pages from the frames now, behind a
   flag, not deployed, so you can see the structure across subjects before step 3? Or keep grade 4 math first as
   the design says.

## What I could not judge

How the 36-week home calendar maps courses that meet fewer than five days a week (kindergarten social studies, 64
days): the frames give days, not days a week, for those. Finding 5's columns would settle it.
