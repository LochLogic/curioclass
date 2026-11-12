# Naming scan, 2026-11-12

Asked by Cory: "I prefer accuracy and standardization. Let's go with the best known word for each thing we build and
lock it in both internally and externally. Please do a deep scan and let me know the best way forward. If fixes are
obvious, go ahead and make them. Ensure consistency across documentation."

The locked list is docs/GLOSSARY.md. This page is how it was found, what was fixed today, and the staged plan for
the rest.

## How the scan was done

Whole-word, case-insensitive counts of about 90 structural words in four places: docs/ (Markdown, not counting
docs/archive and docs/Return), scripts/, site/templates/, and the visible text of a full local build (6,231 pages,
built to a scratch folder, not dist/). Data file names and column headers were read directly. Counts below are
docs / scripts / templates / built pages. Counts of short words (unit, check, day) include every sense of the
word; the sense that matters is named in the notes.

"Best known" means the word a US teacher meets in common curricula and in curriculum reviews: Illustrative
Mathematics (course, unit, section, lesson, "Check Your Readiness", end-of-unit assessment, cool-down), Eureka
Math (module, topic, lesson, exit ticket), enVision (topic, lesson, quick check), and the review vocabulary of
EdReports and state adoption rubrics (scope and sequence, unit, lesson, assessment, the three aspects of rigor:
conceptual understanding, procedural fluency, application). From memory: no source was opened for this page.

## What was found

### The one real problem: the course levels are named off the standard

| Today | Size in grade 4 math | What it holds | What a US teacher calls a thing like it |
|---|---|---|---|
| course | 150 days | the year | course |
| spine (year spine) | 1 per course | every day in order, with reasons | **scope and sequence** (with a pacing guide inside it) |
| stretch | 18 per year, 3 to 15 days | a block of standards, a readiness check, an end check, a family note, a record sheet | **unit** (IM's units carry exactly these; enVision's topics are this size) |
| unit | 43 per year, 1 to 6 days | a plan, an opener, the days | **section** (IM), topic (Eureka) |
| day | 150 | one lesson or check | lesson; "day N" for its place |
| end check / check day | 18 / 18 | the stretch's assessment | **end-of-unit assessment** (IM, EdReports); assessment day |

"Stretch" is not a curriculum word; no teacher or reviewer would guess it. And the docs already slip: the spine's
row for stretch 11 reads "the pilot unit", LESSON-DAY.md listed the stretch's pieces "once per unit" (fixed today),
and SITE-DESIGN.md puts "stretch" in a public breadcrumb. Counts: stretch 1,977 / 108 / 1 / 45; unit 2,591 /
266 / 12 / 113; spine 587 / 26 / 0 / 8.

"Module" for the topic pages is the other half of the same knot: in Eureka Math a module is a whole unit of
several weeks. SITE-DESIGN.md already calls them topic pages. Module: 4,397 / 461 / 78 / 4,987.

### Every word, with its verdict

Verdicts: **keep** (it is the best-known word), **rename** (to the word in the glossary), **merge** (two words for
one thing become one), **decide** (a question for Cory).

| Concept | Words in use today (docs / scripts / templates / built pages; where) | Best known | Verdict |
|---|---|---|---|
| a grade of a subject | course 2,029 / 403 / 7 / 0; also "class" for a worksheet list (WORKSHEETS-PLAN.md, /closet/worksheets/), and `course_id` = `math-k8` in data/courses.csv, a K-8 track | course | keep; the two code senses lag (stage 3) |
| the year's order | spine 587, year spine 23, scope and sequence 13, pacing guide 6 (math-4-spine.md, ROADMAP.md, DESK-ANSWERS.md) | scope and sequence | **decide** (A) |
| the long run of days | stretch 1,977 / 108 (math-4-spine.md, UNIT-PLAN.md, plan.py, lesson.py); stretch sheet 80 | unit | **decide** (A) |
| the short run of days | unit 2,591 / 266 (UNIT-PLAN.md, units.csv, `courses/<course>/uNN-N/`) | section | **decide** (A) |
| the topic pages | module 4,397 / 461 / 78 / 4,987 (/modules/, modules.csv, module.html) | topic | rename: page copy done today; URL and code staged (stage 3) |
| one day | lesson day 34, teaching day 29, day (LESSON-DAY.md, HANDOFF.md) | lesson; "day N" | merge to lesson (the materials) and day (the place); LESSON-DAY.md's file name lags |
| the per-tool plan | lesson plan 33 / 2 / 20 / 1,661 (LESSON-PLANS.md, plan.html) | lesson plan | keep; the course's version is the teacher page |
| teacher-facing day page | teacher page 182 / 17 / 6 | teacher page (lesson plan also fits, but it is taken) | keep |
| student-facing day page | student page 136 / 26 | student page | keep |
| end-of-day check | exit slip 35 / 2 (LESSON-DAY.md, course day files 170 times, lesson.py); exit ticket 14 / 2 / 7 (sub-day.html, SUPPLY-CLOSET-PLAN.md); exit question 105; "Exit check" as the tool lesson plan's last part (79 of 80 tools' plan.md, check_plans.py) and as a build step | exit ticket | merge to exit ticket (stage 1); "Exit check" stays the build step only |
| pre-unit check | readiness check 100 | readiness check (IM: "Check Your Readiness") | keep |
| unit's last check | end check 220; check day 52 | end-of-unit assessment; assessment day | **decide** (A) |
| fluency check | facts check | facts check | keep |
| the unit's teacher page | unit opener / opener 322 / 11; days.csv `opens` is the warm-up | unit opener (unit overview is as common) | keep; warm-up for `opens` |
| answers | answer key 35 / 6 / 19; key alone in LESSON-DAY.md | answer key | merge to answer key in prose (done in LESSON-DAY.md) |
| projector pages | display page 27, display, slides ("none") | display | keep |
| record of results | record sheet 98 | record sheet | keep |
| note home | family note 73 | family letter is as common | keep (it is 150 words; "note" is accurate) |
| sub support | Sub Day 52 / 14 / 13, sub-day, sub plan (closet/home.html), "sub day packet" (home.html); course: a packet per day (LESSON-DAY.md, ECOSYSTEM.md) vs one sub-ready day per unit (SITE-DESIGN.md) | sub plan | keep Sub Day packet (per tool) and sub-ready day (course); fixed the stale per-day wording today |
| order picture | Teaching map, teaching map, The Map (ROADMAP.md) | | keep **Teaching map** |
| grade and subject pages | Classrooms, grade rooms, subject wings (find.html, base.html) | grade page, subject page | retire into Find (stage 2) |
| tool groups | collections (public), family (code, `/collections/<family>/`) | collection | keep collection; "family" lags in code |
| tool feel | play style (public), format (code, formats.csv) | play style (no common teacher word) | keep; "format" lags in code |
| shelf and Shelves | shelf 481 / 38 / 52; the new door Shelves | shelf | keep: the door is Shelves, one named collection on it is a shelf |
| print shelves | Supply Closet | | keep |
| texts | Reading Room (public), library (URL and code) | | keep Reading Room; code lags |
| wonder | Curiosities (Instruments before 2026-11-05: no stale uses left) | | keep |
| play | Recess | | keep |
| standards words | standard 6,082; strand 44 / 52 (a math domain is shown as "Strand"); cluster (CCSS sense, career clusters, tool-overlap clusters); grade band 43 | standard, domain (math), strand (ELA), grade band | keep; "strand" as the generic grouping, noted in the glossary |
| tool marks | key tool 68, light tool 33, practice tool 48 (old name of light tool, and the role) | | keep key tool and light tool; "practice" only as a role (all current uses checked: clean) |
| tool role "lesson" | coverage.csv `lesson` column, BASELINE rule 21 | | **clashes** with a course lesson (stage 4) |
| day kinds | Understanding, Fluency, Use, Check, Respond (days.csv); "application" in the spines | conceptual understanding, procedural fluency, application | rename `Use` to Application (stage 1) |
| "Curio" alone | 82 / 27 hits, all `Curio.voice` and other code names or quoted rules | | clean |

## What was fixed today

Prose and page copy only. No URL, file name, data column, script identifier or id changed.

| File | Fix |
|---|---|
| site/templates/module.html, bench.html, standard.html, tool.html, map.html, closet/gens.html, closet/shelf.html, closet/word-grade.html, closet/word-wall.html, closet/_teach.html | "module" on screen becomes "topic" (eyebrow "Topic · Grade 4 · Math", "Topics" on standard pages, "this topic") |
| scripts/build_site.py | Shelf blurbs and the Word Wall count say "topic"; the search index labels a topic page "Topic" (search.html's sort follows) |
| scripts/gen_links.py, site/assets/gen/vocabulary.js, site/assets/gen/word-puzzles.js | Generator blurbs and field labels say "topic" ("Word Wall topic", "Add a second topic") |
| site/templates/pages/about-plain.html | Two places said "modules" and meant tools |
| site/templates/home.html, closet/home.html | "a sub day packet", "sub plans", "word walls", "game night" become Sub Day packets, Word Wall cards, Game Night |
| site/templates/map-region.html, standard.html | "teaching map" becomes Teaching map |
| docs/courses/LESSON-DAY.md | "Key" becomes "Answer key"; the per-stretch pieces (family note, record sheet, readiness and end checks) were listed "once per unit" and now say once per stretch, filed in the first unit's folder (as the folders already are); the Sub Day line follows Cory's later word (one sub-ready day per unit) |
| docs/ECOSYSTEM.md | Same Sub Day correction |
| docs/WORKSHEETS-PLAN.md | A worksheet list is a "class" on screen and was a "unit" in the prose; now "class" outside code spans |
| docs/SITE.md | The page table says topic page, with "module" named as the URL and code |
| docs/ROADMAP.md, docs/BUILD-PLAN.md | "The Map", "teaching map" become Teaching map |
| docs/GLOSSARY.md | New: the locked list |

Checks: `build_site.py --library --closet` to a scratch folder and `check_site.py` (6,235 pages, 0 broken links),
`check_generators.mjs` (26 generators ok), `plan.py check` and `lesson.py check` (passing, untouched).

## The staged plan for the rest

Each stage is one commit, done in one sitting, so no doc is ever half renamed.

| Stage | What | Cost | Risk and what breaks | Kind |
|---|---|---|---|---|
| **0. Decision A** | Cory answers the course-words question below | one Desk card | none | **Cory's** |
| **1. Lesson words** (main session, since day files and data/plans are gated) | "exit slip" to exit ticket in LESSON-DAY.md, the 8 course day folders and lesson.py's printed titles (its regex "slips showed many" must accept both until every day file moves); the tool lesson plan's last part "Exit check" to "Exit ticket" in check_plans.py's arcs and the 79 `tools/<id>/plan.md`; days.csv kind `Use` to `Application` with plan.py and lesson.py | about an hour plus a full gate run | lesson.py and check_plans.py fail until the scripts and files land together; built print pages change wording | work |
| **2. The four doors** (already planned in SITE-DESIGN.md) | Find replaces /classrooms/; "grade rooms" and "subject wings" retire; redirects from the old pages | part of the site build | covered by its own plan | work |
| **3. Topic URLs and code** | /modules/<id>/ to /topics/<id>/ (1,634 pages: 797 topic pages plus Word Wall and chart pages); one splat rule `/modules/* /topics/:splat 301` in `_redirects` (needs `check_site.py` to understand a splat, and build_site.py to write it, since redirects.csv is one row per path today); the search index field; then `module_id` to `topic_id` in data/modules.csv (rename the file), sequence.csv, tools-concepts.csv, tools.csv, coverage.csv, units.csv and about 460 script uses; the `module` word in about 4,400 doc lines | URL move: half a day. Column and identifier rename: a day, mostly scripted, every checker run | Search engines see 301s for a while (the topic pages are in the sitemap). Every script reading `module_id` breaks together; the scattered ones (shape_courses.py, tool_bins.py, check_worksheets.py, gen_links.py, generators reading words.json `modules`) are the risk. Old docs keep "module" unless swept | work; do the URL move with stage 2, the code rename later or never (the glossary already records the lag) |
| **4. Small internal clashes** | The tool role "lesson" (BASELINE rule 21, coverage.csv) clashes with a course lesson: rename the role "teach"; the worksheet code's `unit` (a class list) and courses.csv's `math-k8` "course" | an hour each | BASELINE is Cory's rule text: say the change on a card | work, with a line to Cory for BASELINE |
| **5. Course words** (only if A passes) | One scripted sweep, in this order so no word is ever double-booked: unit to section, then stretch to unit, then spine to scope and sequence, end check to end-of-unit assessment, check day to assessment day. Covers docs (about 4,500 lines, excluding reviews and archive, which keep their words as history), plan.py and lesson.py messages and printed headers, SITE-DESIGN.md's breadcrumb and pages, HANDOFF.md and DESK-ANSWERS.md (with the main session). Ids stay: `s11-...` item ids (never reused), `uNN-N` folders (they read as unit and section after the rename) and `sNN.md` | a day for the sweep, a read by the curriculum expert of UNIT-PLAN.md and LESSON-DAY.md after | High while half done, which is why it is one sitting. A prose rule ("a stretch with one unit has one merged document") must be rewritten by hand, not by search and replace. The reviews in docs/reviews keep the old words and need a one-line note at their top | work, once Cory says yes |

### Decision A for Cory: the course words

The question: rename the levels of a course to the words teachers and reviewers already use?

| | Option 1 (my pick) | Option 2 |
|---|---|---|
| The year's order | scope and sequence | spine |
| 3 to 15 days on a block of standards | unit | stretch |
| 1 to 6 days inside it | section | unit |
| The last-day check | end-of-unit assessment (assessment day) | end check (check day) |

Why option 1: a teacher opening /courses/math-4/ should not have to learn a word to find unit 3. Every reviewer
asks for "the unit" and "the scope and sequence" by name, and the bar is state adoption. The ids and folders do not
have to change. What it costs: one day's sweep (stage 5), and some of today's decisions read differently after it.
Two of them change in substance, not only in name, and need Cory's word with the yes:

1. **Sub-ready day "per unit".** Said when "unit" meant the short run (43 a year in grade 4 math). After the
   rename, "one per unit" would mean 18 a year. My pick: one per (new) unit, 18 a year, which is what a teacher
   expects and is lighter to write.
2. **"Pilot unit 11.1"** becomes unit 11 (it has one section). Nothing else about the pilot changes.

Option 2 keeps every approved document as written and leaves "stretch" on the public site, where SITE-DESIGN.md
already shows it.

## Changes needed in files this scan did not touch

- **docs/HANDOFF.md:** nothing wrong today. After Decision A, "pilot unit 11.1" and the stretch and unit wording
  throughout (stage 5). Point "names are being locked" (line 77) at docs/GLOSSARY.md as done.
- **docs/agents/decisions/DESK-ANSWERS.md:** history, leave as written; add the Decision A card and its answer when
  given.
- **docs/SITE-DESIGN.md:** "topic pages (today modules)" is right. It shows "stretch" in public: the course page's
  "how many stretches have full lessons", "every stretch and check", "a print button for the stretch", and the day
  page breadcrumb "course / stretch / unit / day N of 150". Under option 1 these read unit and section. "Lesson day
  page" reads "day page". "Sub-ready day per unit" needs the level settled (above). "Unit pieces" is fine.
- **courses/math-4 day files and data/plans (gated):** "slip" to exit ticket (stage 1, about 170 places); days.csv
  kind `Use` to `Application` (stage 1).
- **docs/agents/decisions/BASELINE.md:** rule 21's role "lesson" (stage 4).
