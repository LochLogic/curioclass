# Course and unit pages from the frames (2026-11-14)

Cory's answer on Desk card q-baseline-1 (docs/agents/decisions/DESK-ANSWERS.md, 2026-11-14): (1) write the website
check's design changes into docs/SITE-DESIGN.md now; (2) build course and unit pages for all 52 core courses from the
frames now, hidden from the live site until he says. Nothing was deployed, nothing was pushed, no git was run.

## What changed in docs/SITE-DESIGN.md

Every change is marked "Approved 2026-11-14" (with Desk card q-baseline-1 at the top and on the main headings).

- A top note listing the changes and pointing here; the status line now says the hidden frame-only pages exist.
- Course URL: `/courses/<frame slug>/` (`/courses/math-grade-4/`); band ids never name a course (finding 3).
- Course page: a **shape** card (minutes, days a week, year or half, weeks, the checks and the units they follow);
  **course-level rows** in the year at a glance; **before, after and alongside**; a **credits** line, with the
  interim wording below (findings 2 and 4). A paragraph names the frame's public columns and says planning language
  never reaches a page.
- Day page: day URLs stay flat; breadcrumb course / unit / section / day N of 160; a course-level day's breadcrumb is
  course / Course-level check N / day (findings 1 and 2).
- **Unit page** `/courses/<course>/unit-<n>/` added; **section page** moved to `/courses/<course>/unit-<n>/section-<m>/`,
  the old `unit-<n.n>` form retired (finding 1); unit pieces folder `courses/<course>/sNN/`, read from section N.1
  until a course moves them (finding 10).
- Standard and topic pages: "taught in ... unit N" from the units before days exist; topic grades follow the owning
  course after each subject's scope and sequence (findings 7 and 8).
- **Find: courses**: `/courses/` by subject and grade; grade and subject pages open with their courses (finding 9).
- **Hidden until shown**: how the hiding works and how to lift it.
- Rules the design keeps: **day numbers fixed per edition**, redirects from days-map.csv, Pick up stores the day
  file id (finding 6).
- Build order: new step 0 (these pages, approved); step 1 is now day pages course by course; step 3 Used in at unit
  level first (findings 7 and 11).

## The generator

`scripts/course_pages.py` (new). It reads data/plans/frames.csv and each docs/courses/<slug>/frame.md through
scripts/frame.py (`parse`, `table`, `calendar`, `school_day`, `week`), so it uses the same parsing and the same school
calendar as the frame gate. It renders with the site's Jinja templates, `base.html`, `macros.html` and curio.css.

```
python -X utf8 scripts/course_pages.py check          # read all 52 frames, run the copy checks; writes nothing
python -X utf8 scripts/course_pages.py build [DIR]    # write /courses/ into a built site (default CURIO_DIST or dist/)
python scripts/build_site.py --courses                # the same pages inside a whole-site build
```

Each run deletes and rewrites the whole `courses/` folder of the target, so a changed frame re-runs cleanly.
`check --dropped` prints every sentence it held back.

New templates: `site/templates/courses/index.html`, `course.html`, `unit.html`, `_style.html` (page styles from the
site's colour and type variables; phone layout under 760px; print hides the header and footer).

Small changes to existing files, all inert unless the course pages are shown:
- `scripts/build_site.py`: `--courses` flag (imports course_pages only then); calls `course_pages.build` before the
  search index; `course_pages.hide` after `_headers` and `.assetsignore` are written; grade and subject pages get
  `courses_here` (empty until shown); search entries only when shown.
- `site/templates/base.html`: a Courses menu and footer link only when `courses_shown`.
- `site/templates/browse.html`: a Courses list at the top of grade and subject pages only when `courses_here`.
- `scripts/check_site.py`: while `courses/*` is in .assetsignore, fails if any other page, the sitemap or the
  search index points into /courses/.

### What a page shows, and what it leaves out

Only the frame's public columns: unit and compelling question (title, question, anchor split out), days, What
students learn, Why this unit here, Owned standards (linked to the site's standard page where one exists), and the
teacher notes column as "Notes for the teacher". Course-level checks come from the Course-level checks table
(label, check, respond and review days, What it checks) placed by `frame.calendar`. Inside those cells, any aside in
parentheses, clause or sentence with planning language (base text, base lesson, rows, agents, card ids, file paths,
candidate check sets, skill ids, cycles, lesson numbers) or a company or standards-document name is dropped; model ids
(`map-key`) print as words. Counts kept and dropped: What students learn 1254 / 69, Why this unit 828 / 191, teacher
notes 1041 / 334, What it checks 255 / 5, anchors 169 / 1. Seven units have no "Why" left and their pages skip that
heading. The course lede is generated from data ("Grade 9 science: 10 units over 160 days, from ... to ..."), because
the frames' brief bullets are planning text.

Not shown yet (nothing in CSV to show honestly): the alongside courses' lean weeks (the Cross-subject tables are
prose), placement cards, Pick up where you left off, Start at day 1, sections and days.

### Credits line (item-level choice, please confirm)

The brief allowed the open project name only as SITE-DESIGN's credit rules allow; SITE-DESIGN had no rule and the
ELA K to 5 frames say the base text's name is never used on a page, so every course page uses the fallback:
- 18 courses with a base text: "Written by Curio Class. Many of this course's days will be adapted from an openly
  licensed curriculum, used under CC BY 4.0 and changed by Curio Class; each adapted day carries its own credit
  line." Those are math K to 8, Algebra I, Geometry, Algebra II (base: Illustrative Mathematics K-12 Math, 1st
  edition), science 6 to 8 (OpenSciEd Middle School 2022) and ELA K to 2 plus 3 to 5 (EL Education K-5 Language Arts,
  2017).
- The other 34: "Written by Curio Class. Where a day draws on an openly licensed or public-domain source, that day
  carries its own credit line." (Partial bases named in frames, such as a retired open college text or state units,
  are not named.)

## Where the pages are

Not in the repository and not in dist/. They are generated: 450 pages, 1 `/courses/` index, 52 course pages,
397 unit pages. The checked preview was built into a copy of the current dist/ in the session scratchpad
(`C:\Users\Cory\AppData\Local\Temp\claude\912539a76ace91d0\6b988c7a-6d6e-40cb-8945-fae6fa21ae03\scratchpad\preview\`),
which a reboot may clear. To look locally: `python scripts/build_site.py --courses` then `python scripts/serve.py`
and open http://127.0.0.1:8411/courses/ (or `course_pages.py build` into any built copy).

## How they are hidden, and how to show them

Hidden in five independent ways while `SHOWN = False` in scripts/course_pages.py:
1. Built only with `--courses`; the deploy command (`--library --closet`) and `--preview` never build them.
2. `<meta name="robots" content="noindex, nofollow">` on every page, and `X-Robots-Tag: noindex, nofollow` for
   `/courses/*` in `_headers`.
3. Not in sitemap.xml or search-index.json; no menu, footer, grade, subject or other page links to them.
4. `courses/*` added to dist/.assetsignore, so a deploy of a `--courses` build still uploads none of them.
5. check_site.py fails if anything public points into /courses/.

To show them: set `SHOWN = True`, add `--courses` to the deploy command in wrangler.jsonc's comment and SITE.md,
rebuild, run check_site.py. Then the noindex, header and .assetsignore line go, and the pages join the sitemap,
search, the menu, the footer and the grade and subject pages. Note the file count: a full build with the courses is
19,468 files (19,018 without them) against Cloudflare's 20,000 limit.

Nothing already published changes: a full build with `--library --closet --courses` and one without `--courses`
are byte-identical outside `courses/`, `_headers` and `.assetsignore`.

## Check results

- `python -X utf8 scripts/plan.py check`: exit 0, no frame failures (notes only).
- `python -X utf8 scripts/lesson.py check`: exit 0, 0 failures.
- `python -X utf8 scripts/course_pages.py check`: exit 0; 52 courses, 397 units, 450 pages; every unit has a
  question and a What students learn; no em dash, "Curio" alone or listed name.
- Rendered-page scan of all 450 pages: no em dash, no "Curio" alone, no company or standards-document name, every
  page noindex.
- `python scripts/check_site.py` on the preview: 6,685 pages, 0 broken internal links, 0 external loads, the new
  hidden-course guard passes; sitemap and search index hold no /courses/ path.
- `python scripts/check_safety.py`: all tools clean.
- **The whole-site build stops today on data errors that are not from this work**: `build_site.py` exits on
  worksheet rows (ss-2 #5, ss-4 #6, ss-5 #6, us-hist-8 #1, us-hist-hs #1, world-geo-6 #25, world-hist-7 #6,
  world-hist-hs #1: "no such row in the concept list" or a title mismatch) and, with `--closet`, on
  `social-studies.txt:30 culture` (Word Wall definition 13 words, cap 12). So the current deploy command would fail
  too. For the comparison builds a scratch test harness (outside the repository) turned those stops into warnings.
- Preview in the app's browser pane: the courses index, Biology, Math Grade 4, US Government and Politics, Science
  Kindergarten, social studies grade 3 unit 1 and ELA grade 11 unit 2, at phone width (333 to 375 px, no sideways
  scroll) and desktop (1280 px). The site has no dark mode yet (SITE.md, "Not done yet"), so under a dark colour
  scheme the pages render light, like every other page.

Teacher-note wording that mentions time: some ELA check descriptions say "No timer" and some high school ELA checks
describe "timed" writing in their teacher notes. Nothing counts down on these pages; flagging for a look.

## Screenshots

In `C:\Users\Cory\.claude\projects\S--\6b988c7a-6d6e-40cb-8945-fae6fa21ae03\tool-results\`:
- `mcp-Claude_Browser-blob-1794673768053-cz7emy.jpg` courses index, phone
- `mcp-Claude_Browser-blob-1794673774193-eg2035.jpg` Biology course page top, phone
- `mcp-Claude_Browser-blob-1794673774194-oh6r71.jpg` Biology year at a glance, phone
- `mcp-Claude_Browser-blob-1794673781427-qyo1ep.jpg` Biology course-level check row, phone
- `mcp-Claude_Browser-blob-1794673785068-1iu8qb.jpg` social studies grade 3 unit 1, phone
- `mcp-Claude_Browser-blob-1794673807194-drlia3.jpg` courses index, desktop
- `mcp-Claude_Browser-blob-1794673807194-9s8qof.jpg` Math Grade 4 course page, desktop
- `mcp-Claude_Browser-blob-1794673807194-4wqd3g.jpg` Math Grade 4 year at a glance with checks, desktop
- `mcp-Claude_Browser-blob-1794673832546-7d7yh3.jpg` ELA grade 11 unit 2, dark scheme requested, phone
- `mcp-Claude_Browser-blob-1794673832546-9o55bu.jpg` US Government and Politics, dark scheme requested, phone
- `mcp-Claude_Browser-blob-1794673832546-11t7qk.jpg` Science Kindergarten, dark scheme requested, mobile preset

## Not done, and questions for Cory

1. **Credits line**: name the base text once on the course page (BASE-TEXTS credit-line form), or keep "an openly
   licensed curriculum"? The ELA K to 5 frames say its name is never used on a page.
2. **The site build is blocked** by the worksheet and Word Wall data errors above (another worker's area).
3. Not touched: docs/courses/math-4/, docs/courses/ela-6/, data/plans/math-4/, data/units.csv and the top-level
   courses/ folder. Grade 4 math's held draft days (old order, build/lessons/math-4/) are not linked; its course page
   says Lessons coming like every other, which is true of the new frame.
4. Frame text is filtered by pattern, not rewritten. A teacher-facing read of a few unit pages per subject is worth
   doing before showing them; anything that reads like planning should be fixed in the frame or added to `PRIVATE`.
5. "Alongside" lists the grade's other courses but not yet the weeks where they lean on this one (needs the
   Cross-subject tables in CSV, finding 5).
