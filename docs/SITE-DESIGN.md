# Site design: the course-first Curio Class

**Status: direction approved by Cory 2026-11-12; mock-ups seen and liked the same day. Not built yet.** This page is
the design the build follows. [SITE.md](SITE.md) is how today's site is built; where the two differ, this page is
where the site is going and SITE.md is where it is. Decisions behind it: DESK-ANSWERS, 2026-11-12, "homeschool
parents and the site's shape" and "the home check".

Mock-ups (private design canvas, three boards: the Grade 4 Math course page, day 74 with its six views, and where
every piece lives): https://claude.ai/artifact/ReGX8xmhDNBCBEKwhVzLzT

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

### Course page: `/courses/<course>/` (for example `/courses/math-4/`)

In order, as on the mock-up's first board:

1. Breadcrumb (Courses / Grade 4 / Math), the course name, one paragraph on what the year covers, and the promise:
   free, no sign-up, prints, works offline.
2. **Pick up where you left off** (the last day opened, kept in the browser on this device only, never sent
   anywhere) and **Start at day 1**.
3. **Honest status**: how many units have full lessons today, and that the rest show their standards, tools
   and printables until lessons come. Never imply a finished course that is not.
4. Four cards: where to start (placement from the readiness checks), the year plan (school calendar or a 36-week
   home calendar), print or download (per section: a PDF bundle or an offline folder), how this course teaches.
5. **The year at a glance**: every unit and check in teaching order, with day range, standards and a status
   pill (Full lessons, Partly built, Lessons coming). A unit opens into its sections and numbered days, each day
   with its goal and kind of day, plus the unit pieces (opener, readiness check, record sheet, family note, sheets)
   and a print button for the unit.
6. Side cards: Teaching at home (the same course with one child: At home view, placement, 36-week calendar,
   record sheet as portfolio); Out tomorrow (the unit's sub-ready day); tools in this course (each with the days
   that use it); help make it better (report a problem, corrections list, try a unit with your class).

### Day page: `/courses/<course>/day-<n>/` (for example `/courses/math-4/day-74/`)

Breadcrumb (course / unit / section / day N of 150), the day's title, the "I can" goal, minutes, standards, kind of
day, version label ("draft 1, not yet taught" until a taught run), previous and next day. Then six views of one
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

### Section page: `/courses/<course>/unit-<n.n>/`

The section's goal, its days, its pieces and its print bundle. Small: most teachers arrive from the course page.

### Tool page (changed): `/tools/<id>/`

Keeps its own page and stays usable alone. Adds **Used in**: the course days that use it, by link. A tool
planned for a course but not built says which day waits for it.

### Standard and topic pages (changed)

A standard lists the course days that teach it first, then topics and tools. A topic page
lists the course days on it, then its tools and shelf pieces.

## Decided at the home check (Cory, 2026-11-12)

1. **Teaching map: hidden now, back later.** It no longer shows on the site (build flag `--map` brings back the
   old one for a local look). Once the courses are built it returns, reimagined as a picture of the scopes and sequences and
   courses. Its data (`data/sequence.csv`) is kept.
2. **Sub Day: one sub-ready day per unit** in each course (18 a year in grade 4 math), written with the unit, that a substitute can run from the
   page with its printables. The per-tool Sub Day packets stay on the Supply Closet shelf.
3. **Names: the best-known word for each thing, locked inside and out.** A deep scan of the names in use writes
   GLOSSARY.md and a staged plan for renames ([reviews/naming-scan-2026-11-12.md](reviews/naming-scan-2026-11-12.md)).
   The same day the course levels took the words teachers know (card 112): unit, section, scope and sequence.

## Rules the design keeps

- No accounts, no tracking. "Pick up where you left off" lives in the browser only; the page works when storage is
  blocked.
- No timers, scores or ranks on anything a student sees, including the Project view. The Teacher Desk timer is a
  teacher's tool on the shelf.
- Every page prints and works offline; a section downloads as one folder.
- Honest status everywhere: a day not yet taught says so; a course not yet built says what it has today.
- Every day page carries "report a problem"; fixes are listed in the open on the course's corrections page.
- Tools are ingredients: a day links its tool, and the tool links back.
- Curio Class is never shortened; no company names; no claims of review or endorsement.

## Build order (proposed, not yet approved)

1. **Course and day pages for grade 4 math**, behind a `--courses` flag like the Reading Room was: `build_site.py`
   reads `courses/` and `data/plans/`, and wraps the six pages `lesson.py` already builds as the views of one day
   page. Nothing changes on the live site until Cory has seen it built.
2. **The four doors**: new nav and home page; Find folds in grades, subjects, standards, topics and the classroom
   pages; Shelves and Explore get index pages. Old URLs stay or redirect (`data/redirects.csv`).
3. **Used in** back-links on tool, standard and topic pages.
4. **The renames** from the naming scan, staged with redirects.
5. **Community pieces**: report a problem (the existing contact form with the page filled in), the corrections
   page, try a unit sign-up.
6. **At home view and sub-ready days**, as the lesson writers add those blocks to each unit.
