# Glossary: the locked words

Set 2026-11-12 from the naming scan (docs/reviews/naming-scan-2026-11-12.md), on Cory's rule: "the best known word
for each thing we build", the same word inside and outside. One row per thing we build. New prose, page copy,
script messages and Desk cards use the word in the first column. A code name (file, URL, column, id) may lag behind
its word; where it does, the row says so and why, and the staged plan in the review says when it moves.

Two rules sit above the table:

- **"Curio Class" in full**, always. `Curio.*` (the kit's code namespace, `kit/curio.js`) is code, not a name.
- **The build steps keep their names:** Idea, Spec, Build, Self-check, Refine, Fix, Exit check, Art and voice,
  Finish check, Sign-off, Live (docs/agents/decisions/BASELINE.md). Because "Exit check" is a step, nothing a
  student sees is called an exit check.

**Awaiting Cory:** the four rows marked **Pending** under "The course" (one question, for a Desk card). Until he
answers, write the word in the "today" brackets, and every other row on this page uses today's words too ("stretch"
for the long run of days, "unit" for the short one). Do not start the rename by hand: "unit" would change meaning
halfway through the docs. The review gives the proposal and the reasons.

## The course

| Word | What it is | Do not call it | Code name and URL, if different |
|---|---|---|---|
| **course** | One grade of one subject (grade 4 math) or one high school course. What a teacher runs from day 1 to the last | class (worksheets), program, track | `math-4` in `courses/`, `data/plans/`, `/courses/<course>/`. Lag: `data/courses.csv` `course_id` (`math-k8`) is a subject track across grades, not a course; the worksheet code calls a course-sized list a `unit` |
| **Pending: scope and sequence** (today: spine, year spine) | Every day of a course's year in order, with the reason for the order, the standards and the pacing | spine, year spine, pacing guide (a pacing guide is the calendar only), map | `docs/courses/<course>-spine.md` |
| **Pending: unit** (today: stretch) | A run of days (3 to 15 in grade 4 math) on one block of standards, opened by a readiness check and closed by an end check | stretch, module, topic, chapter | Lag for good: item ids `s11-...` and plan files `sNN.md` keep the `s`; ids are never reused (LESSON-DAY rule 8) |
| **Pending: section** (today: unit) | A short package of days (1 to 6) inside a unit, with its own plan and opener | unit (once renamed), part (taken by "part of a standard"), topic, lesson set | Lag: folders `courses/<course>/uNN-N/` and `data/units.csv` |
| **Pending: end-of-unit assessment**, short **unit assessment** (today: end check); **assessment day** (today: check day) | The check on a stretch's last day, on every part of every standard the stretch teaches | end check, unit test, quiz | `items.csv` `check` = `end`; `days.csv` `kind` = `Check` |
| **day** | One numbered day of a course's year (day 90 of 150), of any kind | lesson day, period | `d090.md`; `/courses/<course>/day-<n>/` |
| **lesson** | What one teaching day ships: teacher page, student page, exit ticket, answer key, display | lesson day | The template is docs/courses/LESSON-DAY.md (file name lags) |
| **teaching day, assessment day, respond day** | The kinds of day. A teaching day is understanding, fluency or application; a respond day acts on an assessment | check day (see the pending row above) | `days.csv` `kind`: `Understanding`, `Fluency`, `Use` (lag: the rigor word is **application**), `Check`, `Respond` |
| **warm-up** | The first minutes of a day | opener (that is the unit's teacher page), opening | `days.csv` `opens`, `opens_min` |
| **goal** (on screen and paper: the "I can" line) | What the day is for, in student words | objective, target | `days.csv` `goal` |
| **unit opener** | The teacher page for a unit (a section, if the pending words pass): the content at an adult's level, why this model, the common errors, the supply list | unit overview, intro | `opener.md` in each unit folder |
| **readiness check** | The short check given before a stretch opens, on what it builds on | pre-test, diagnostic, pre-assessment | `items.csv` `check` = `readiness`; `readiness.md` |
| **facts check** | The multiplication facts check of grade 4 math, given in days 1 to 6 and before day 94 | fluency test, timed test | `facts-check-N.md` |
| **sub-ready day** | One day per unit in each course, written with the unit, that a substitute can run from its page (Cory, 2026-11-12). Which level "unit" means here goes with the pending question | Sub Day (that is the per-tool packet), sub plan | Not built |
| **at home** block | The one-child path every day carries for a parent teaching at home | homeschool version, home track | Not built |
| **Teaching map** | The picture of every course's order. Hidden now; returns, reimagined, once the courses are built | The Map, teaching map (lower case t in a name) | `/map/`, build flag `--map`, `data/sequence.csv` |

## Inside a lesson

| Word | What it is | Do not call it | Code name, if different |
|---|---|---|---|
| **teacher page** | The page the teacher reads the night before; it runs the day | lesson plan (that is the per-tool page), script | `<day>-teacher.html` |
| **student page** | The one sheet each student works on, both sides at most | worksheet, handout, student sheet | `<day>-student.html` |
| **exit ticket** | The quarter-page check at the end of a teaching day, four to a sheet; one question on it is an **exit question** | exit slip, exit check (a build step), cool-down | Lag: course day files, LESSON-DAY.md and `lesson.py` say "exit slip" until stage 1; `items.csv` `check` = `exit` |
| **answer key** (short **key** in code and file names only) | Every answer, its working and what each wrong answer means | key (in prose: it clashes with key tool and `judged` = `key`) | `<day>-key.html` |
| **display** | The projector pages, generated in the order of the teacher page | slides, deck, presentation | `<day>-display.html` |
| **slides** | None. We do not make them | | |
| **record sheet** | The class list where a teacher records each exit ticket and check, one per stretch; also the portfolio at home | gradebook, tracker | `record.md` |
| **family note** | The short note home, one per stretch, English and Spanish | parent letter, newsletter | `family.md` |
| **common errors** (inside the project: **error register**) | The lettered wrong ways of thinking a stretch expects, and what to do about each | misconceptions list | `errors.csv`, `wrongs.csv` |
| **materials** | What to print and gather, per student and per class | supplies list (fine in prose) | the `materials` header line |
| **worked example**, **fix-it**, **practice**, **challenge** | The kinds of question inside a lesson | | `items.csv` `check` = `example`, `fix`, `practice`, `challenge` |

## The site: four doors

| Word | What it is | Do not call it | URL and code name, if different |
|---|---|---|---|
| **Courses** | The door for teaching a course day by day | Curriculum, Lessons | `/courses/` (not built) |
| **Find** | The door for something for tomorrow: search, standards, topics, grades, subjects | Browse, Classrooms | Not built. Today's `/classrooms/` page, its **grade rooms** and **subject wings**, fold in here and those three names retire |
| **Shelves** | The door for everything usable on its own: tools, the Supply Closet, the Reading Room, collections | Library (that is the Reading Room's code name), catalog | Not built. One named collection on it is **a shelf** (the Word Wall shelf) |
| **Explore** | The door for curiosity and play: Curiosities, Recess, play styles | Fun, Games | Not built |
| **topic** (topic page) | One subject-and-grade topic with its tools, worksheets, Word Wall, anchor chart and more, tied to its standards | module | Lag: `/modules/<id>/` (1,634 pages), `module_id` in data and scripts, `data/modules.csv`, the search index's `m` field |
| **standard** | One code of a standards document (4.MD.A.3); **part of a standard** is one verb's worth of it | objective, outcome | `/standards/<code>/`; `parts.csv` |
| **strand** | The grouping above a standard that a topic page shows: a domain in math and science, a strand in ELA, a discipline in the arts | domain (fine when quoting a math document) | `modules.csv` `strand` |
| **grade band** | K-2, 3-5, 6-8, 9-12 | span, level | `bands.csv`, `band` |
| **framework** | A standards document (CCSS-M, NGSS) | | `frameworks` |

## The shelves

| Word | What it is | Do not call it | URL and code name, if different |
|---|---|---|---|
| **tool** | One interactive page that works offline as a single file | app, game (unless it is one), activity, interactive, module, instrument | `/tools/<id>/` |
| **key tool**, **light tool** | A unit plan's mark: the tool a day is planned around, or a lighter one built from templates | practice tool (the old name of light tool; "practice" is a role) | `days.csv` `mark` |
| **role**: lesson, see why, practice | What a tool does (BASELINE rule 21) | | `coverage.csv` columns. The role "lesson" clashes with a course lesson; see the review, stage 4 |
| **lesson plan** | The one-period plan for one tool, on its tool page | teacher page (that is the course's) | `/tools/<id>/plan/`; its last part is still headed "Exit check" (stage 1 renames it exit ticket) |
| **Sub Day packet** | The five-page print packet for one tool, for a substitute, on the Supply Closet shelf | sub day (lower case), sub plan, sub packet | `/tools/<id>/sub/`, `/closet/sub-day/`, `exit.md` |
| **on the bench** | Planned, not built yet | coming soon, draft | `bench.html` |
| **Ready to use** | The page of every built tool | | `/tools/` |
| **collection** | Tools of one kind across grades | family (that word is for parents) | Lag: `/collections/<family>/`, `family` column |
| **play style** | How a tool feels to use (arcade, showdown) | format | Lag: `/styles/`, `format`, `data/formats.csv` |
| **Supply Closet** | The print shelves that go with the tools | closet (fine in code) | `/closet/` |
| **printables** | Anything made to print; also the name of the Printables shelf (templates and paper) | | `/closet/printables/` |
| **worksheet** | A printed page of practice questions with its answer key, listed by class on the Worksheets shelf | sheet (fine in prose once named), student page | `/closet/worksheets/`; a class's list is a `unit` in the worksheet code (lag) |
| **worksheet generator** (on screen: "Make a sheet") | Makes a new worksheet and key each time | maker, builder | `/closet/worksheets/make/`, `site/assets/gen/` |
| **Word Wall**, **anchor chart**, **poster**, **Research Card**, **Game Night** (Family Game Night), **Break Box**, **Teacher Desk** (its tool: the **Desk Dock**) | The named shelves | word walls, game night (lower case), the Desk (that is the Review Desk) | `/closet/...` |
| **Reading Room** | The texts to read on screen or in print | library (on screen) | Lag: `/library/`, `library` in code |
| **Curiosities** | Wonder pieces for students, outside the bar | Instruments (the old name) | |
| **Recess** | Play, outside the bar | | `/recess/` |
| **score code** | The code a student shows to report a tool result | score, grade | |

## Words for the work, inside only

| Word | What it is | Do not call it |
|---|---|---|
| **spec** | The written design of one tool, before Build | brief (a brief is what an agent is handed) |
| **concept** | A tool's row in `data/tools-concepts.csv` (the Idea step's output) | idea card |
| **unit plan**, **stretch sheet** | The two planning documents (docs/courses/UNIT-PLAN.md). If the pending course words pass, they become the section plan and the unit plan | |
| **reading pack** | One stretch's pack for an agent (`plan.py pack`) | |
| **wave** | A batch of builds | |
| **Review Desk** (the Desk) | Cory's queue of cards | Teacher Desk (that is a shelf) |
| **gate** | A script check that fails the build | |
| **piece** | Generic: any one built thing. Never a category on screen | |
