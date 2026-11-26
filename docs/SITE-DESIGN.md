# Site design: the course-first Curio Class

**Status: direction approved by Cory 2026-11-12; mock-ups seen and liked the same day. Not built yet, except the hidden frame-only course and unit pages (2026-11-14).** This page is
the design the build follows. [SITE.md](SITE.md) is how today's site is built; where the two differ, this page is
where the site is going and SITE.md is where it is. Decisions behind it: DESK-ANSWERS, 2026-11-12, "homeschool
parents and the site's shape" and "the home check".

Mock-ups (private design canvas, three boards: the Grade 4 Math course page, day 74 with its six views, and where
every piece lives): https://claude.ai/artifact/ReGX8xmhDNBCBEKwhVzLzT

**Approved 2026-11-14 (Cory, Desk card q-baseline-1):** the website check's design changes
([reviews/baseline-1-site-2026-11-14.md](reviews/baseline-1-site-2026-11-14.md), findings 1 to 11) are written in below,
each marked "Approved 2026-11-14": course URLs use the frame slug, a unit page, section pages nested under their unit,
a place for course-level days, the course page showing what the frame says (shape, before, after and alongside,
course-level checks, a credits line), day addresses that survive renumbering, and courses on the find pages. Course and
unit pages for all 52 core courses are built now from the frames, hidden until Cory says (see "Hidden until shown").
How they were built: [reviews/site-course-pages-2026-11-14.md](reviews/site-course-pages-2026-11-14.md).

Words on this page follow [GLOSSARY.md](GLOSSARY.md); where they differ, the glossary wins. The course words were settled
on 2026-11-12 (Desk card 112, `q-course-level-names`): a **unit** is the long run of days on a block of standards, a
**section** is the short package inside it, and the year's order is the **scope and sequence**. URL slugs may lag.

## What changed

Curio Class began as a library of tools. It is now a set of full courses, and tools are one ingredient of a lesson
day. Teachers stay the main readers. Homeschool parents use the same courses through an At home view of every day
(homeschool option 1). Nothing that exists today is removed; it moves to one of four doors.

## The four doors

| Door | Job | Holds |
|---|---|---|
| **Courses** | Teach a course, day by day. The heart of the site | Course pages, unit, section and day pages, unit pieces, sub-ready days, print and offline bundles |
| **Find** | Something for tomorrow, by any route | Search, standards, topic pages (at /topics/, moved from /modules/), grades, subjects. Grade rooms and subject wings fold in here |
| **Shelves** | Everything usable on its own | Tools, the Supply Closet (anchor charts, Break Box, Game Night, printables, research cards, Teacher Desk, Word Wall, worksheets, the per-tool Sub Day packets), the Reading Room, collections |
| **Explore** | Curiosity and play, mostly for students | Curiosities (the shelf now, the full entrance once all are built), Recess, play styles |

The footer keeps About, Why free, Using Curio Class, a new Teaching at home page, Accessibility, License, Privacy and
Contact. Beyond School, Class Cast, the IEP bank and score codes get a home when they ship.

The home page has two equal front doors, "Teach a course" and "Find something for tomorrow", and a smaller Explore
door.

## Page types

### Course page: `/courses/<course>/` (for example `/courses/math-grade-4/`)

`<course>` is the frame slug (GLOSSARY, "course"), the same id as docs/courses/<slug>/ and data/plans/<slug>/; the
catalogue's band ids (`math-k8`) never name a course URL. (Approved 2026-11-14, Desk card q-baseline-1, finding 3.)

In order, as on the mock-up's first board:

1. Breadcrumb (Courses / Grade 4 / Math), the course name, one paragraph on what the year covers, and the promise:
   free, no sign-up, prints, works offline.
2. **Pick up where you left off** (the last day opened, kept in the browser on this device only, never sent
   anywhere) and **Start at day 1**.
3. **Honest status**: how many units have full lessons today, and that the rest show their standards, tools
   and printables until lessons come. Never imply a finished course that is not.
4. Four cards: where to start (placement from the readiness checks), the year plan (school calendar or a numbered
   home calendar; "36-week" in Cory's 2026-11-12 call, see docs/courses/CALENDAR.md), print or download (per section: a PDF bundle or an offline folder), how this course teaches.
   Plus **the shape** (Approved 2026-11-14, finding 4): minutes a day, days a week, the year or the half year and its
   weeks, and the course-level checks with the units they follow (from data/plans/frames.csv `minutes_min`,
   `minutes_max`, `per_week`, `weeks`, `term`, and the frame's Course-level checks table).
5. **The year at a glance**: every unit and check in teaching order, with day range, standards and a status
   pill (Full lessons, Partly built, Lessons coming). A unit opens into its sections and numbered days, each day
   with its goal and kind of day, plus the unit pieces (opener, readiness check, record sheet, family note, sheets)
   and a print button for the unit. Each unit row links to its unit page.
   **Course-level rows** (Approved 2026-11-14, finding 2): course-level checks, respond days and review days appear
   as their own rows in teaching order, between the units they follow, with their days, weeks and what they check.
   **Before, after and alongside** (Approved 2026-11-14, finding 4): the course this one builds on and the course it
   leads to, each linked (the same subject's courses one grade down and one grade up; high school courses at their
   usual grade); alongside, this grade's other core courses, with the weeks where they lean on this one once the
   frames' Cross-subject tables are in CSV.
6. Side cards: Teaching at home (the same course with one child: At home view, placement, numbered home calendar,
   record sheet as portfolio); Out tomorrow (the unit's sub-ready day); tools in this course (each with the days
   that use it); help make it better (report a problem, corrections list, try a unit with your class).
   **Credits** (Approved 2026-11-14, finding 4): one line, once for the course, for its base text: the licence and
   its link, in the credit-line form of [sources/BASE-TEXTS.md](sources/BASE-TEXTS.md). Until Cory confirms naming
   a base text on a course page (BASE-TEXTS allows the name only inside a credit line; the ELA K to 5 frames say it
   is never used on a page), the line reads "adapted from an openly licensed curriculum, used under CC BY 4.0 and
   changed by Curio Class; each adapted day carries its own credit line". A course with no base text says it is
   written by Curio Class and that a day drawing on an open or public-domain source carries its own credit.

Only a frame's public columns reach a page: the unit and its compelling question, days, what students learn, why
this unit here, owned standards, and the teacher notes (supplies, sensitive topics). Skills ids, C3 cell text beyond
the practices, Check set adds, For the lead, Seams and Models tables, and the source map stay inside, and planning
language inside a public cell (base text, rows, agents, card ids, file paths) never reaches a page.

### Day page: `/courses/<course>/day-<n>/` (for example `/courses/math-grade-4/day-74/`)

Day URLs stay flat under the course. Breadcrumb (course / unit / section / day N of 160; Approved 2026-11-14,
finding 1); a course-level day's breadcrumb is course / Course-level check N / day (Approved 2026-11-14, finding 2).
Then the day's title, the "I can" goal, minutes, standards, kind of
day, version label (the day file's version line, for example "draft 1, signed off 2026-11-23, not yet taught"), previous and next day. Then six views of one
page, as tabs that also work as plain links with no script:

| View | What it is | Source today |
|---|---|---|
| Teach | The hour in parts, each opening to its full script; side cards for before class, materials, errors to watch for, other rooms | `build/lessons/.../dNNN-teacher.html` |
| Project | What the class sees, full screen, one screen per part; nothing counts down | `dNNN-display.html` |
| Student | The student page, both sides, and large print | `dNNN-student.html`, `-student-large.html` |
| Key | Answers and the wrong answers to expect; teachers only, never on student pages | `dNNN-key.html` |
| Print | Every printable for the day, one link each, and the whole day or section as one PDF | the `print` header line |
| At home | The same lesson with one child in 30 to 40 minutes: what to say where the class talks in pairs, which items to do, home swaps for supplies | the At home block (LESSON-DAY.md), built as `dNNN-home.html` (days 89 to 93 so far) |

Foot: report a problem with this day, corrections to this course, the unit's sub-ready day, the version.

### Unit page: `/courses/<course>/unit-<n>/` (Approved 2026-11-14, Desk card q-baseline-1, finding 1)

The unit's compelling question, its days and day range and weeks, what students learn, why this unit here, the
standards it owns, supplies and teacher notes; then the readiness check, the end-of-unit assessment, the record sheet,
the family note (English and Spanish), the sub-ready day, its sections with their days, the course-level check that
follows it if any, and the unit's print bundle. Until its days are written the page says "Lessons coming" and shows
what the frame holds; the pieces it will hold are listed as coming. Unit pieces will live in `courses/<course>/sNN/`
(matching the `s` ids); until a course moves them, the builder reads them from section N.1's folder (finding 10).

### Section page: `/courses/<course>/unit-<n>/section-<m>/` (Approved 2026-11-14, finding 1)

The section's goal, its days, its opener and its print bundle. Small: most teachers arrive from the unit page. The
old form `unit-<n.n>` used the pre-rename word and is retired (GLOSSARY: unit, section); the site is not launched, so
no redirect is needed.

### Tool page (changed): `/tools/<id>/`

Keeps its own page and stays usable alone. Adds **Used in**: the course days that use it, by link. A tool
planned for a course but not built says which day waits for it.

### Standard and topic pages (changed)

A standard lists the course days that teach it first, then topics and tools. A topic page
lists the course days on it, then its tools and shelf pieces. Before days exist, both say which course and unit teach
it ("Taught in Grade 4 Math, unit 3, lessons coming"), matched through the units' owned standards, a parent code
counting as covered by its lettered parts (Approved 2026-11-14, finding 7). Once each subject has its scope and
sequence, a core topic's grade becomes the grade of the course that owns its standards (finding 8).

### Find: courses (Approved 2026-11-14, Desk card q-baseline-1, finding 9)

`/courses/` lists the core courses by subject (columns) and grade (rows), high school courses at their typical grade.
A grade page opens with its core courses, then its topics. A subject page opens with its courses K to 12 in order,
then topics by grade.

### Hidden until shown (Cory, 2026-11-14, Desk card q-baseline-1)

The course and unit pages are built now, for all 52 core courses, and stay hidden from the live site until Cory says:
only `python scripts/build_site.py --courses` (or `python -X utf8 scripts/course_pages.py build <dir>`) builds them;
the deploy command has no `--courses`, and `--preview` does not build them either. While `SHOWN = False` in
scripts/course_pages.py they carry `noindex, nofollow`, an `X-Robots-Tag` header, no sitemap, search, menu or find
page entry, and `courses/*` in dist/.assetsignore, so even a deploy of a `--courses` build uploads none of them;
check_site.py fails if any other page, the sitemap or the search index points into /courses/. To show them: set
`SHOWN = True`, add `--courses` to the deploy command, rebuild, check.

### The Front Office: `/front-office/` and Show Your Work: `/front-office/show-your-work/` (Cory, 2026-11-17)

For administrators and policy readers, from a state department of education down to a teacher: the whole curriculum
top to bottom, and how it is built. Not a teacher or student page, so the print-and-offline rule bends here: the pages
load data as you browse, and the reader prints the open view only.

- **The Front Office** shows the six layers as a flow with counts, a skill ladder per subject (strand by grade), every
  course by grade, and a reader drawer. Each view has its own link (`#subject/course/unit`).
- **Show Your Work: The process** (Cory, 2026-11-20): the public form of docs/COURSE-RUN.md: the five-step loop (make, check, fix, improve, close), fixed where it began, one grade at a time, and what each layer is checked for. Arrows are CSS or hand-placed SVG; the trace diagram has a tall version under 680px.
- **Every document reads in the drawer** (Cory, 2026-11-19: "read from the progressions and course frames all the
  way to the days"): the full skill ladder by grade (`#subject/ladder/grade`), each course frame and scope and
  sequence (`#subject/course/frame`, `/scope`), each unit plan (`/unit/plan`), section plan (`/unit/s/1.2`) and
  written day (`/unit/d/12`), formatted, with previous and next links that walk the layers in order. Days not yet
  written show as planned. The blind-list courses have no documents here.
- **Cleaned before posting.** scripts/front_office_docs.py drops internal sections, day front matter (materials and
  print stay), file paths, dates of production, skill and item ids and sentences naming internal steps, then a last
  gate drops any line with an internal word. `check` fails the build on anything that gets past it.
- **Wording:** describe checks, never checkers. No mention of who or what did the work, and nothing that implies it
  was human made. Review summaries are cleaned before they are posted; base texts are cited here properly.
- **Files:** the two pages, one JSON per subject and one ladder JSON per subject are static assets (about 10 files
  however large the curriculum grows). The documents (one `course.json` per course, one JSON per unit with
  documents; days live inside their unit's JSON) are stored in the R2 bucket beside the pictures (Cory, 2026-11-19):
  dist/.assetsignore keeps them out of the asset upload, scripts/sync_media.py uploads changed ones and deletes
  removed ones (data/docs-manifest.txt, by content hash), and worker/index.js serves them at the same addresses.
  The page asks for `?v=<build hash>`, so each copy caches for a year and a new build is never stale. The host cap
  counts uploaded files only (scripts/check_site.py skips what .assetsignore keeps back).
- **Built by** scripts/front_office.py on every build.
- **Draft, now linked:** linked from the site footer (About column) since 2026-11-19. Still a draft banner,
  `noindex, nofollow`, and no sitemap or search entry. When to drop the banner and noindex is Cory's call (later.csv
  L70).

## Decided at the home check (Cory, 2026-11-12)

1. **Teaching map: hidden now, back later.** It no longer shows on the site (build flag `--map` brings back the
   old one for a local look). Once the courses are built it returns, reimagined as a picture of the scopes and sequences and
   courses. Its data (`data/sequence.csv`) is kept.
2. **Sub Day: one sub-ready day per unit** in each course (9 a year in grade 4 math, one per unit of its frame), written with the unit, that a substitute can run from the
   page with its printables. The per-tool Sub Day packets stay on the Supply Closet shelf.
3. **Names: the best-known word for each thing, locked inside and out.** A deep scan of the names in use writes
   GLOSSARY.md and a staged plan for renames ([reviews/naming-scan-2026-11-12.md](reviews/naming-scan-2026-11-12.md)).
   The same day the course levels took the words teachers know (card 112): unit, section, scope and sequence.

## Rules the design keeps

- No accounts, no tracking. "Pick up where you left off" lives in the browser only; the page works when storage is
  blocked.
- No scores or ranks on anything a student sees, including the Project view, and no timer without a grounded
  purpose (a pace cue, a movement game, classroom management; BASELINE rule 30). The Teacher Desk timer is a teacher's tool on the shelf.
- Every page prints and works offline; a section downloads as one folder.
- Honest status everywhere: a day not yet taught says so; a course not yet built says what it has today.
- Every day page carries "report a problem"; fixes are listed in the open on the course's corrections page.
- **Day numbers are fixed per edition of a course** (Approved 2026-11-14, finding 6). When a scope and sequence
  renumbers days after launch, the build writes a data/redirects.csv row for each moved day from
  build/lessons/<course>/days-map.csv (day number to day file id), and Pick up where you left off stores the day file
  id, not the number.
- Tools are ingredients: a day links its tool, and the tool links back.
- Curio Class is never shortened; no company names; no claims of review or endorsement.

## Build order (proposed, not yet approved; step 0 approved 2026-11-14)

0. **Frame-only course and unit pages for the 52 core courses**, behind `--courses`, every unit marked Lessons
   coming, not deployed (Approved 2026-11-14, Desk card q-baseline-1, finding 11). Built 2026-11-14 by
   scripts/course_pages.py; hidden as above.
1. **Day pages, course by course**, behind the same `--courses` flag: the builder reads `courses/` and
   `data/plans/`, adds sections and days to the unit pages as the scope and sequence and day writing land, and wraps
   the six pages `lesson.py` already builds as the views of one day page. Nothing changes on the live site until Cory
   has seen it built.
2. **The four doors**: new nav and home page; Find folds in grades, subjects, standards, topics and the classroom
   pages; Shelves and Explore get index pages. Old URLs stay or redirect (`data/redirects.csv`).
3. **Used in** back-links on tool, standard and topic pages: first at unit level from the frames' units, then at day
   level as days are written (Approved 2026-11-14, finding 7).
4. **The renames** from the naming scan, staged with redirects.
5. **Community pieces**: report a problem (the existing contact form with the page filled in), the corrections
   page, try a unit sign-up.
6. **At home view and sub-ready days**, as the lesson writers add those blocks to each unit.
