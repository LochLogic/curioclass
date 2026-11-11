# Roadmap

The one plan for Curio Class: what is done, what comes next, and in what order. Consolidated 2026-10-28 from the
"Later phases" section of docs/PHASE0-PLAN.md, the Supply Closet roadmap, docs/agents/SCALE-PLAN.md,
docs/LIBRARY-PLAN.md, docs/SITE.md ("Not done yet") and docs/agents/roadmap/.

The foundation (what Curio Class is for, who it serves, its promises and assumptions): docs/FOUNDATION.md, the one home of layer 1 (2026-11-11). Why and where: docs/VISION.md (the north star, 2026-11-03). The quality bar for full courses: docs/ADOPTION-BAR.md
(state adoption is the bar we build to, Cory 2026-11-10; formal adoption is not pursued now). This file holds the order and the status. The design detail stays in each track's own plan, linked from its section.
When a roadmap item starts, finishes or moves, update it here first, then post it to the Review Desk's Roadmap tab
(`python scripts/desk_roadmap.py <out.json>`, then ArtifactData set stats/roadmap).

## Where it stands (2026-11-10)

| | Count |
|---|---|
| Tool concepts in the catalog | 805 |
| Live tools | 84 |
| Specs written | every tool: 559 waiting on Build (Sara wrote the last 431, 2026-11-08 to 11-10); 7 ASL tools held for the Sign Strip sample |
| Built, waiting on Refine | 119 at Self-check, 20 at Fix, 10 at Art and voice |
| Worksheets live | 1,008 of 7,116 planned (live 2026-11-03; trimmed from 8,947 on 2026-11-04) |
| Modules with Word Wall cards | 762 of 797 (4,413 cards), English and Spanish |
| Anchor charts / posters / Game Night games | 74 / 54 / 104 |
| Sub Day packets | 79 |
| Reading Room stories curated and processed | about 700, not live yet |

`python scripts/board.py` gives the live tool counts (docs/BUILD-BOARD.md).

## Goal

Reach and craft together (Cory, 2026-10-28). As many teachers as possible should know Curio Class exists; nobody
needs to use a tool that does not fit their class, but every tool must be really good. Free for good: no paywall,
no accounts, no ads, no tracking.

## The path from here (locked 2026-11-10, Cory; whole-site plan, reprinted the same day)

This section is the plan for the whole site. The tracks below hold the detail; where a track and this section
disagree, this section wins.

**End goal.** A teacher can run any course on Curio Class from the first day to the last, free, with no account, and
the course would stand up to a state adoption review (docs/ADOPTION-BAR.md, BASELINE rule 20). Every tool in it is
really good. A course is a grade of a subject or a high school course. Taken together, the courses cover what an
American public school teaches from kindergarten to grade 12: every grade of the core subjects, and the subjects
around them (arts, computer science, health and PE, world languages, English language development, library, career
and technical, social and emotional learning). Depth comes first: a course is finished before the next is started
(step 6), so breadth is where the site ends up, not a reason to spread thin.

**One measure, read three ways** (split 2026-11-11). For each course: standards taught in full, out of all its
standards. "Full on paper" is what the specs say. "Full and live" counts only what a teacher can open today.
"Verified" counts only live tools someone has played against the spec. Beside them, the days of instruction the
course's units cover out of about 180. A course is complete when the last three are full, not the first. All four
are in docs/agents/catalog/tables/measure.md; every step below moves them.

**Changed after a cold review (2026-11-11, Cory).** A fresh read of this plan found that it measured specs, not
courses, and queued a year of spec fixing across 93 courses before one course had been proved. Five changes, all
now in the steps below: (1) Sara's queue stops at batch 4 (docs/spec-fixes/NEXT.md); (2) the proof moves ahead of
further fixing and starts now with grade 4 math; (3) the measure is split as above; (4) every spec carries three
hooks an adoption review looks for and the teaching test did not ask for: a check the teacher can see, English
learner supports and access (docs/agents/SPEC.md); (5) the subjects outside the core (arts, computer science,
health and PE, world languages, ELD, library, CTE, SEL) stay in the end goal but are parked: no standard texts
wired, no specs fixed, no builds, until the core courses are proved. Science and social studies wait their turn
behind math and ELA. What the review said to keep: the build pause, the teaching test, one ledger, shape before
fix, and finishing a course before starting the next.

**What the review found (2026-11-10).** 63 tools read against the bar. Coverage and duplication are fine. The repeated
flaw: tools show the idea, then leave the student's own part of the standard thin, optional or passable by trial,
worst on the major work of a grade. The gap in shape: a module lists a cluster, gets one tool, and the rest of the
cluster is taught nowhere. Verdict: right raw material, fixable now, costly later.

### The layers (added 2026-11-11, Cory)

The six steps below say what happens in what order. The layers say what stands on what. Each layer is built on the
ones under it and may not contradict them. A layer is made solid enough to build on, then corrected by what is
built on it; none is declared finished in the abstract (the check rule looked solid until a spine showed it took a
fifth of the year).

| Layer | What it is | Its home | State |
|---|---|---|---|
| 1. Foundation | What Curio Class is for, who it serves, the promises, the bar, what we assume about the room, what a tool is for | docs/FOUNDATION.md | Gathered into one file 2026-11-11. Two open questions listed there |
| 2. Standards | What must be learned. Not ours to change | data/standards/ | Math and ELA texts wired. Science and the rest filed, wired when their courses open. Footnoted limits for math still to add |
| 3. Approach to teaching | How students learn here and why, with its sources. A short shared core for every subject, then one page per subject | docs/APPROACH.md, docs/APPROACH-MATH.md; evidence detail and source access in docs/APPROACH-SOURCES.md | **Second draft 2026-11-11**, revised once after the expert's cold read (docs/reviews/approach-2026-11-11.md). Cory settled the three decisions on Desk card q-approach the same day (teach first by default in grades 2 to 5, no countdown timer in any tool, SPEC.md rule renamed) and said to go forward without library access. Waiting on Cory: his read of the pages. Science and ELA pages when those courses open |
| 4. Progressions | What each grade inherits and hands on, per subject | data/sequence.csv, the spine's builds-on columns, a progression page per subject (first: docs/courses/math-3-5-progression.md) | Grades 3 to 5 math: second draft 2026-11-11 after the expert's cold read (docs/reviews/math-3-5-progression-2026-11-11.md); spine pointers and 15 sequence.csv links corrected; Cory said yes to its four points the same day (Desk card q-progression-math-4), now in the spine. The science review found errors in sequence.csv, still open |
| 5. Course spine | Every teaching day of a year, in order, with the reason | docs/courses/ | Grade 4 math approved. Grade 4 science and grade 6 ELA revised drafts |
| 6. Stretch and unit plan | The contract for each unit: what each day is for, where a tool is used and for what job, what the check asks | docs/courses/ (to be set with the first plans); rows in data/units.csv | None yet |
| 7. Lessons, tools, print, checks | What students and teachers touch | The shelves and tools | Building paused |

Running through every layer: the assessment system, and the supports for English learners, access, teachers and
families ("What a finished course holds").

**Open courses are an input, not a layer.** Well-reviewed open courses are read as evidence at layers 5 and 6,
course by course, by the curriculum expert. We write our own course (FOUNDATION, section 1).

**Decided in the same discussion (Cory, 2026-11-11), and now rules:**

1. We own the full course.
2. A unit plan for every unit of a course comes before that course's tools.
3. No tool is built or refined until a unit plan names its job.
4. Tools are key tools (built first; the course cannot run without them) or practice tools (lighter, added over
   time, same standard of correctness). A course is runnable when its key tools are live and print covers the rest.
5. Frequent cold reads by the curriculum expert are the main review at every layer. Human reads are rare and aimed.
6. Grades 3 to 12 assume one device per student, with a one-line projector path. A parent teaching one child at
   home is a named audience.
7. A teacher judges open work; tools give it structure and print carries rubrics and sample pieces.

The detail of each is in docs/FOUNDATION.md. Still open: the device assumption for K to 2, and what happens to
existing tools and specs that no unit plan asks for.

**The unit plan.** Fixed fields, not a fixed length: a 5-day unit fits one page, and two pages is the ceiling. It
is a contract, not the lesson. Fields are set when the approach is written and tried on three units first.

**What this changes in step 4.** The order inside "Prove one course" is now:

| # | Piece | Done when |
|---|---|---|
| 4a | The approach: a shared core of about two pages and a page for math, each claim with its source | The curriculum expert has read it cold and its findings are closed; Cory has said yes |
| 4b | The grades 3 to 5 math progression around grade 4 | Every grade 4 stretch names what grade 3 hands it and what grade 5 needs, checked against the standards' own progressions |
| 4c | The unit plan fields, tried on three units of grade 4 math, the pilot (unit 11.1, area and perimeter) among them | The expert has read the three; the fields are fixed |
| 4d | Unit plans for the other 40 units of grade 4 math | Every unit has a plan; every tool a plan asks for is marked key or practice; existing specs with no plan asking for them are counted |
| 4e | The key tools named from the plans. The three approved on 2026-11-11 (Community Plot Planner, Fraction Wall Duel, Road Trip Logbook) stand unless the plans show a better first three, in which case that goes to Cory | A build order for key tools, by value |
| 4f | The pilot unit built to the bottom, with its key tools, then the reads: verified play, the rubric read, the expert, a working teacher | As in the step 4 row below |

Where the step 4 row below and this table disagree, this table wins.

### The shape we build to

| Piece | What it is | Rule |
|---|---|---|
| **Course** | A grade of a subject | Gets a year spine: its units in order, with the reason for the order |
| **Stretch** | A run of units on one idea (added 2026-11-11) | Owns the readiness check, the end check and, in ELA, the text set and word list |
| **Unit** | A 1 to 5 day package inside a course | Points at modules and picks from every shelf. Owns only the order, the teacher pages and what no shelf has. Has a unit plan (two pages at most) before any of its tools is built |
| **Module** | One teachable topic, and the hub page every shelf hangs from | Split only when it holds two unrelated topics, and then properly. Its standards are spelled out, never a bare cluster |
| **Tool** | One screen piece | Carries only the codes it teaches on its main path, and a role: lesson, see why or practice. Built only when a unit plan names its job, which also marks it key or practice. Major work in math, ELA and science gets two or three tools |
| **Shelves** | Word Wall, charts, Game Night, Sub Day, lesson plans, worksheets, generators, Reading Room, The Map | Keep their keys. Worksheets and generators are the home of fluency and extra practice; the Reading Room is the home of year-long reading |
| **Ledger** | data/coverage.csv | One row per standard per course: where it is taught in full. The one home of a coverage claim and the source of the measure |
| **Recess, Curiosities** | Play and wonder | Outside the bar. They claim no standard |

Rules: BASELINE 21 (the teaching test, roles) and 22 (modules, depth on major work). How the shelves fit:
docs/ECOSYSTEM.md. Decisions: docs/agents/decisions/DESK-ANSWERS.md, 2026-11-10.

### The six steps

**Tool building is paused** (Build, Refine and the Codex queue) except for the three grade 4 math tools of step 4.
Fixes that hold whatever happens (a wrong fact, a broken control on a live tool) are the other exception.

| Step | What | Done when | Cory decides |
|---|---|---|---|
| 1. Rules. **Done 2026-11-10** | The teaching test and six rule edits are in SPEC.md, REFINE.md and docs/TOOL-CONTRACT.md. Common Core math and ELA texts and the major-work marks are filed in data/standards/. The other subjects' texts are filed there too (CSTA 2026 as ids only) but not yet wired into the packets or the ledger | A new spec or lens cannot pass a tool that fails the test | Nothing |
| 2. Read. **Read and maps done 2026-11-10.** Wiring the other subjects' texts is parked (2026-11-11): science and social studies when their courses come up, the rest after the core is proved | Every spec read with row format 2: the 36 pilot tools again as the test, then all the rest by subject and band (about 64 cheaper-model agents). Scripts build the ledger and one map per course, and flag two-topic modules | Every course has its map and its measure | Nothing |
| 3. Shape, one course at a time (was step 4; moved ahead of fixing 2026-11-10) | From the maps, by rule, for one course: module standards spelled out, spec notes applied, second and third tools listed for major-work modules, supporting tools that wait, tools to cut, merge or give a new role, and a build order by value. The two proving courses first. One file per course in docs/agents/catalog/shape/ | data/modules.csv, the specs, the ledger and the build order agree with the map for that course | One Desk card per course, exceptions only: reshape, hold, cut, new tool, split a module |
| 4. Prove one course (was step 5; moved ahead of further fixing 2026-11-11). **Starts now, grade 4 math first** | Sara closes the specs of the two proving courses, then the band, grade 5 and grade 3 math (NEXT.md, batches 1 to 4), and stops. In step with her: the grade 4 math year spine; three tools built from fixed specs (building resumes for these three only; the token plan's side-by-side trial runs on them); one full unit pulling from every shelf, with its assessment and supports; each built tool played against its spec and logged in catalog/verified.txt; a real adoption rubric filed in docs/ (source and licence checked) and the unit read against it by a fresh agent; then a working teacher reads the unit, and one class uses it if we can arrange that. Grade 6 ELA follows the same path | Cory can open one unit and see the bar met, a teacher outside the project has read it, the measure shows standards verified, not only full on paper, and the cost of one tool and one unit is written down. The course itself is done when it meets "What a finished course holds" | The spine, which three tools, who the teacher is, then the pilot review |
| 5. Fix what the proof keeps (was step 4) | Whatever the proof changed goes into SPEC.md, the fix list and the shape script first. Then Sara's queue reopens course by course in the order NEXT.md holds, and the live tools in each course are fixed. Ahead of that, only fixes that hold whatever happens: a wrong fact or a broken control on a live tool. The shelf fixes in docs/ECOSYSTEM.md can run any time. Built tools waiting on Refine are not fixed now | Every live tool in a proved course passes the test or carries an honest role | Nothing, unless a fix changes what a tool teaches |
| 6. Scale by course | Build and Refine resume in value order: finish a course before starting the next, major work first, core subjects before the rest. A course is finished when it meets "What a finished course holds", and the gap table below is checked at the end of each | Course by course, the measure reaches full and verified and unit days reach the spine's total | The order of courses |

### What a finished course holds (added 2026-11-11)

The measure says how far a course is. This list says what "finished" means, so no step can call a course done on
tools alone. Grade 4 math is the first course held to it (step 4), and the list is corrected by what that proof
finds.

1. **A year spine** that accounts for every teaching day: about 150 (180 less testing and school events; the number
   is set on each spine). Each unit has its days, its reason for sitting where it does, what the grade before hands
   it and what the grade after needs from it. A day Curio Class has nothing for is listed as a gap day, never
   papered over.
2. **Units for every day on the spine**, each pulling from the shelves, with daily plans and teacher pages.
3. **Every standard taught in full by a live tool or a unit lesson**, and each of those tools verified: played
   against its spec, logged in docs/agents/catalog/verified.txt.
4. **Assessment at three sizes.** In every tool, the unaided check (SPEC.md hooks). In every stretch (a run of
   units on one idea; changed from "every unit" on 2026-11-11 after the expert reviews, so checking stays near a
   tenth of the year), a short readiness check on the standards it builds on, a short written check as the stretch
   goes, and an end check with a key that says what each wrong answer means. In the course, the cumulative checks
   its spine names (a start-of-year check where the spine has one, then one each quarter and at year end), each
   followed by a respond day. Items come from the generators where they can, so a check can be redrawn; explain
   tasks and reading checks need fixed items in two forms. With no accounts, results live on a printable class record sheet and in score codes.
5. **English learner supports** in every tool (the hooks) and on every unit's teacher page: the language the lesson
   asks for, the key words with their Word Wall cards, sentence frames for the talk and the writing.
6. **Access.** Every tool passes the hooks and an automated access check at the Finish check; one keyboard-only
   play is part of verifying it. Printables read in black and white.
7. **One outside read.** A working teacher has read at least one unit of the course and their notes are filed in
   docs/pilots/ with what changed because of them.
8. **Honest public claims.** The course's pages say taught, practiced or shown per the ledger, never more.
9. **A fresh-agent read of the whole course** against the rubric on file, with every finding closed or listed. The
   reader is the curriculum expert (docs/agents/EXPERT.md): a standing role, always run cold, that researches outside
   sources before it judges. It also reads every spine and every pilot unit, and its reports are kept in docs/reviews/.

### Gaps found, and how each closes (2026-11-11)

Every gap the two reviews and the cold review found, with the step that closes it. A gap leaves this table only
when its "closed when" is true. Nothing here is closed by a sentence in a plan.

| Gap | How it closes | Step | Closed when |
|---|---|---|---|
| The measure counted specs, not what ships | Four columns: full on paper, full and live, verified, unit days | Done | In measure.md now. 254, 10, 0, 0 across the site |
| Tools are about seven hours of a course; no unit exists in data | data/units.csv (one row per unit: course, order, days, modules, status) feeds the Unit days column; only live units count. The spine budgets every teaching day | 4 for the pilot unit, 6 per course | A course's unit days reach its spine's total |
| The proof came after a year of fixing | Proof is step 4 and runs beside Sara's batch 1 | Done | Grade 4 math meets "What a finished course holds" for one unit, then the year |
| A built tool may not match its spec | Each tool is played against its spec's Standards map and Done when lines, once with keyboard only, and logged in verified.txt with the date. A mismatch is fixed in the build or the spec, whichever is wrong | 4 for three tools, then every tool as its course comes up | Verified equals Full and live for the course |
| About 220 built or live tools were made before the teaching test | Not fixed now. Each is fixed, re-read and verified when its course comes up. Until then its public pages claim only what the ledger says (next row) | 5, 6 | No live tool in a finished course fails the test |
| The public site claims more than the ledger supports | Tool pages and /standards/ pages take their wording (teaches, practices, shows) from data/coverage.csv by script | 5, for proved courses first | A script check fails the build when a page claims more than the ledger |
| The read is 80 percent reliable, and one re-read was never checked | Every re-read gets a top-model spot-check of one spec in five; under 80 percent agreement the course is read again. Verified play is the final word, not the read | Standing (FINAL-REVIEW.md) | Each finished course has its spot-check figure in its shape file |
| Outside math and ELA, a course's standards count is only what its modules list | measure.md marks those courses with a star. When science, then social studies, come up, the full standard text is wired in first, so the count is every standard of the grade | Before each of those subjects opens | No starred course is quoted as a share of its standards |
| Assessment was one short check per unit | Three sizes, item 4 of the finished course | Tools: now. Stretch checks: 4. Cumulative checks: 6 | The pilot unit ships with its stretch's readiness and end checks; a finished course has every cumulative check its spine names, each with a respond day |
| English learner supports were named and in no step | Item 5 of the finished course | Tools: now. Units: 4 | The pilot unit's teacher page carries all three parts |
| Access was a font and contrast bar | Item 6 of the finished course. The automated check joins the Finish check in docs/agents/ when building resumes | Hooks: now. Check: with the three proof tools | The three proof tools pass both |
| Coherence across grades was one line | Each spine row names the earlier standards it builds on and where Curio Class teaches them. A script builds a progression table per subject (domain by grade, from the standard texts and the ledger), read at every Shape | Grade 4 math spine: 4. The table: before step 6 | No unit in a finished course builds on a standard taught nowhere below it, or the gap is named |
| No teacher or class had seen any of it | A working teacher reads the pilot unit (Cory's mom, a grade 2 teacher; Cory asks her); one class if it can be arranged. Every unit page carries a short feedback link. Findings are filed in docs/pilots/ | 4, then standing | Item 7 of the finished course. Two teachers before step 6 opens |
| No evidence that it works | Not claimed. A one-page logic model (what the course does, why it should work, what would show it) is written with the pilot unit, which is the lowest tier a federal evidence review accepts. A study waits for a partner | 4 | The logic model is on file and nothing public claims results |
| The bar on file is our summary, compiled from one Blueprint and Claude's knowledge | docs/RUBRIC-MATH-K8.md: the EdReports K-8 math criteria v2.0, linked and summarised in our own words (all rights reserved, so no copy). The expert read the evidence guide on 2026-11-11 and confirmed the 65 percent line. The pilot unit is read against it | 4 | The fresh-agent read cites the rubric's own indicators, and the 65 percent figure is confirmed or corrected |
| The reviewer of a spec was the person who fixed it | Three readers after Sara: verified play, a fresh agent, a teacher | 4 | In FINAL-REVIEW.md now |
| Builds and units are the constraint, not specs | The proof records what one tool and one unit cost in tokens and days. Step 6 sets how many courses a season holds from that, in the open. After batch 4 Sara's time goes to unit pieces, not more specs | 4 | The cost of one course is written in this file before step 6 opens |
| Subjects outside the core have thin reads and umbrella codes | Parked, in the goal. Each opens only with its standard text wired and a fresh read | After the core is proved | Its first course meets the finished course list |
| The eight mathematical practices are in no spec, unit or ledger column (found in the rubric, 2026-11-11) | Each unit names the one or two practices it builds and the task that builds each; the spine shows all eight are met over the year. Not added to tool specs until the pilot shows where they belong | 4 (pilot unit), 6 | The pilot unit names its practices; a finished course's spine covers all eight |
| Nothing checks the balance of understanding, fluency and application (rubric) | Each unit's plan marks every day as mostly one of the three; the spine totals them per stretch | 4, 6 | The pilot unit has all three, and the spine shows none missing where a standard calls for it |
| Check items do not name their standard, and no check says what to do next (rubric) | Every item on a unit or course check carries its code; every key ends with "if many missed this, do that" | 4 | The pilot unit's two checks do both |
| No extension for students ready for more (rubric) | Each unit has one deeper task on the same standard, never next year's content | 4, 6 | The pilot unit has one |
| No family note or supplies list (rubric) | Each unit has a half-page note for families and a list of what the room needs | 4, 6 | The pilot unit has both |
| No assessment accommodations or reading-level supports (rubric) | Each check says how to give it read aloud, with more time, or with a model allowed, without changing what it tests; word problems come in a plainer-language version | 4, 6 | The pilot unit's checks and problems do both |
| Loose ends from spelling out module standards | 113 cluster pages under /standards/ are gone and 296 added, with no redirects; scripts/check_plans.py reports 14 of 80 plans with problems; check_concepts stops on unknown module social-studies-3-5-road-trip-atlas | Before the next site build | Redirects are in data/redirects.csv and both checks pass |

**Resume here (left 2026-11-11, night): steps 4a and 4b are drafted and expert-read. 4a: docs/APPROACH.md and docs/APPROACH-MATH.md, second drafts; Cory answered q-approach (teach first by default in grades 2 to 5; no countdown timer in any tool; SPEC.md rule renamed; no library access) and still owes a read of the pages. 4b is done: docs/courses/math-3-5-progression.md, with findings in math-3-5-progression-findings.md; Cory said yes to its four points (pilot area numbers within what students can multiply, with area returning in stretches 12 to 14; a facts check in days 1 to 6 and before day 94; the decimals rule; the third rounding day), all written into the spine. Next: 4c, the unit plan fields tried on three units (the pilot 11.1 among them), then 4d the other 40 plans, 4e key tools, 4f the pilot unit. Also owed: three data/modules.csv description notes; the science and ELA rubric files and the ELA text plan (now on Sara's list); Cory's final yes on the science and ELA spines. Sara works NEXT.md batches 1 to 4, then docs/courses/NEXT-SPINES.md (drafts, each with an expert read: grade 3 and 5 math spines, science and ELA rubric files and approach pages, the ELA text plan, then more math spines); unit pieces wait for 4c.** All 800 tools have a row in row format
2 (docs/agents/catalog/rows/, 71 packets, about 12 million tokens on the cheaper model), and the ledger is rebuilt:
data/coverage.csv and docs/agents/catalog/tables/measure.md. Across every course's standards: 213 full, 368 nearly,
404 part, 1,102 practice only, 276 shown, 37 none. By tool: 70 teach every code they carry, 177 teach at least one
in full, 178 teach in part, 338 are practice only, 37 only show or claim. The two commonest reasons a tool falls
short: its only check is a small-choice pick with free retries (601 tools list one; 322 of them teach nothing in
full), and the tool does the standard's key step for the student (236 tools). High school math has no standard
taught in full, and science 9 to 12 almost none.

How far to trust it (top-model spot-check of 36 tools, 115 codes, each judged cold first): 80 percent of depth calls
agree; of the misses, 14 are the read too strict and 9 too generous. Math and social studies are sound (85 and 100
percent) and no math "taught" was inflated, so those counts are a floor. ELA taught counts are a floor too: the
read calls a multiple-choice check guessable even where the spec closes it or a second check stands. Science is
right within one step. In computer science, arts, CTE and world languages the codes are umbrellas with no filed
wording, so per-code counts mean little there and each "taught" needs a hand check.

Known limits, to fix before the maps are trusted outside math and ELA: (1) the packets and the ledger use only the math and ELA
texts, so no other course has an expected list and "none" cannot show; the other subjects' texts are filed in
data/standards (CSTA 2026 as ids only, wording still owed) and need wiring into catalog_batch.py and
coverage_ledger.py, science first; (2) the beatable
rule in CATALOG-EXTRACT.md needs three tests added (is trial really cheaper than thinking, does the spec's own
table close it, does a second check stand) and a tie-break for two-part standards; (3) rows that say shown with a
keyed check and an activity the student types are contradictions to grep for.

The maps are written (2026-11-10): `python scripts/catalog_maps.py` builds one map per subject in
docs/agents/catalog/tables/ (map-<subject>.md, index maps.md) and sorts every spec in spec-sort.csv. The sort: 70
fine, 558 small addition, 172 rework; 62 have a thin or missing spec. By stage: of 83 live tools, 3 fine, 54 small
addition, 26 rework; of 146 built, 7, 103, 36. The two proving courses: grade 4 math has 13 tools (2 fine, 10 small
addition, 1 rework) and 27 standards (4 full, 6 nearly, 15 part, 1 practice only, 2 shown); grade 6 ELA has 9 tools
(1 fine, 7 small addition, 1 rework) and 43 standards (4 full, 6 nearly, 17 part, 14 practice only, 2 shown). The
maps are on the Desk as card q-maps-1.

The spec fix list (2026-11-10): `python scripts/spec_fixes.py` builds docs/spec-fixes/ (start at its README.md):
one file per course naming, tool by tool and code by code, which kind of fix each spec needs and the exact parts
the read found missing; fix-list.csv for sorting; done.txt as the hand-kept log. Sara owns the fixes for the whole
spec catalog (Cory, on the Desk), proving courses first, then the 26 live rework tools, then course by course.
After a course's specs are all fixed, the specs are read again and Sara gives the course a final review against
the end standard (docs/spec-fixes/FINAL-REVIEW.md). Cory's other two answers on card q-maps-1: fix the 26 live
rework tools first in step 3 and leave the built ones until their course comes up; leave high school math until
grade 4 math has proved the pattern.

Sara's first batch (2026-11-10, branch spec/sara, merged to main the same night): both proving courses are logged
fixed in docs/spec-fixes/done.txt, 22 tools. Grade 4 math, 13 tools: 11 specs changed, community-plot-planner a
small change, unit-ladder logged fine and unchanged. Grade 6 ELA, 9 tools: 8 specs changed, argument-x-ray logged
fine and unchanged. None is reviewed yet. Left for later by her notes: new source and fact rows to confirm at Build
(debate-prep-desk, summary-squeeze, source-sorter), sensitivity reads at final review (perspective-camera,
sentence-remixer), the line plot scale choice not added to skate-park-angles, and three built tools whose code now
trails the spec (skate-park-angles, egg-carton-factory, and any other marked built). The other 778 specs are not
started.

Re-read after the fixes (2026-11-10, late; packets math-4-1 and ela-6-1, cheaper model, under the tightened
beatable rule and two-part tie-break now in CATALOG-EXTRACT.md). Grade 4 math went from 4 full, 6 nearly, 15 part, 1
practice only, 2 shown to 25 full, 3 nearly (4.NBT.A.3, 4.MD.B.4, 4.G.A.1); every code on all 13 specs now reads
taught and no guessable check is listed. Grade 6 ELA went from 4 full, 6 nearly, 17 part, 14 practice only, 2 shown
to 16 full, 7 nearly, 9 part, 10 practice only, 1 shown. What is left in grade 6 ELA is mostly not a spec problem:
nine tools cannot carry 43 standards, so the gaps (RL.6.7, RL.6.9, RI.6.3, RI.6.6 to RI.6.9, W.6.1 to W.6.6,
W.6.10, SL.6.2, SL.6.5, L.6.2, L.6.4, L.6.6) rest on the grade 6 to 8 band tools, whose specs are not fixed yet
(see the correction below). Still open on the fix list for the 22: argument-x-ray (a tag-and-scan
check with free reruns, no model, few items; Sara had logged it fine), skate-park-angles (one code under five
items), unit-ladder (spec too thin to judge; Sara had logged it fine). Treat the math result as the reader's view,
not a verdict: it is one pass by the cheaper model on freshly rewritten specs, and the final review is the check.
Site-wide after the rebuild: 254 full, 370 nearly, 375 part, 1,093 practice only, 271 shown, 37 none; specs 88 fine,
542 small addition, 170 rework.

Order changed (Cory, 2026-11-10, late): Shape now runs before fixing, one course at a time, because a fix to a
tool that Shape then cuts or re-roles is wasted, and grade 6 ELA showed that fixing specs cannot close a gap that
is really a shape question. Sara works the courses Shape has been through. Three courses are shaped, one file
each in docs/agents/catalog/shape/, one Desk card each (q-shape-math-4, q-shape-ela-6, q-shape-math-5): grade 4
math, grade 6 ELA and grade 5 math. Correction from shaping grade 6 ELA: its gap is not too few tools. The course
is 23 tools, nine in grade 6 modules (fixed) and fourteen in grade 6 to 8 band modules (not fixed), and every large
gap sits on a band tool. A course is its own modules plus every band module that carries one of its standards.
Sara's next batch is those fourteen band specs, then grade 5 math (seven specs that do not wait on a Desk answer).
Across those three courses Shape cuts nothing; Cory approved five second lesson tools on the Desk (two in
grade 4 math, one in grade 6 ELA, two in grade 5 math; DESK-ANSWERS.md), and a sixth (a grade 4 line plot tool) is
re-asked after he sent "do not split" back. Grade 3 math is shaped too (shape/math-3.md, card q-shape-math-3): the
most loaded course so far, 37 codes on ten tools, four second tools proposed. The rule for a module with two topics
(one module, two tools when the topics sit in separate modes or cannot both fit one sitting) is in that file.

All courses shaped, 2026-11-11. Cory approved all four grade 3 second tools (nine approved in all) and the
two-topic rule. scripts/shape_courses.py then shaped the other 89 courses by rule: one file per course in
docs/agents/catalog/shape/, plus shape.csv (one row per tool per course), hand.txt (the four courses shaped by hand,
never overwritten) and decisions.csv (Desk answers and hand overrides; edit it when Cory answers a shape card, then
rerun). What the script decides: load (codes with lettered parts against minutes), a second tool where a tool over
four codes cannot be fixed inside one sitting (20 minutes in K and 1, 25 in grade 2, 35 from grade 3, with five
minutes of slack), two-topic math modules by the time test, and the spell-out of math module standards (99 more
modules now list their own standards in data/modules.csv; the ledger is unchanged by it). What it does not decide:
anything that needs a spec read. Results: no tool cut or merged anywhere; six second tools on the Desk (grade 6 math
Smoothie Lab, grade 8 math Transformation Dock, grade 5 ELA Fact Fusion and Slow-Mo Writer, grade 11 ELA Personal
Essay Studio, and the re-asked grade 4 line plot tool); 41 loaded tools where nothing reads as taught yet, so the
spec is fixed first and judged again; 9 too close to call, fixed inside the tool; high school math candidates
listed but not asked. Outside math and ELA the files count load and propose nothing: those reads are rough and
the standard texts are not wired in. Band tools are never split from a grade file; their specs get a path per grade.

Next, in this order (rewritten 2026-11-11 after the cold review): (1) Sara works docs/spec-fixes/NEXT.md,
batches 1 to 4, adding the three hooks to every spec she touches, and stops there. (2) Claude drafts the grade 4
math year spine from data/sequence.csv, the shape file and the focus marks, for Cory's review. (3) When Cory has
answered q-proof-math-4 (which three tools, who the teacher reader is), those three tools are built from their
fixed specs, played against the spec and logged in catalog/verified.txt, and the area and perimeter pilot unit is
written around them. (4) A published adoption rubric is filed in docs/ with its source and licence, and a fresh
agent reads the unit against it; then the teacher reads it. (5) After Sara's batch 1, Claude re-reads the two
proving courses, the top model spot-checks one spec in five, and she runs FINAL-REVIEW.md. (6) When Cory answers
an open shape card, add a line to shape/decisions.csv and rerun shape_courses.py and spec_fixes.py. Not next:
wiring other subjects' standard texts, fixing specs beyond batch 4, any build beyond the three tools.
Everything it needs: docs/agents/CATALOG-EXTRACT.md, docs/agents/CATALOG-REVIEW.md, docs/agents/catalog/.

### What every other track does meanwhile

| Track | Until grade 4 math is proved (step 4) | After the proof |
|---|---|---|
| 1. Tools | Paused, except the three grade 4 math proof tools and fixes that hold whatever happens. Held collections, queued ideas and the Codex queue wait | Resumes for the two pilot courses, then by course |
| 2. Supply Closet | Carries on: worksheet waves, generators, the Word Wall diagram pass, Break Box read. Its shelf fixes can land any time. Charts and teacher-guide links wait for building to resume, since they ride with a tool | Each unit names what it pulls from the closet. The module kit and Sub Day lite follow the unit pilot |
| 3. Reading Room | Add the text record and topics to the story format, then the ten-story pilot. It can run beside the proof | Topic sets are written into the ledger for the standards they carry; enrich waves follow the course order |
| 4. The site | Page changes that the fixes need. Open items (www redirect, dark mode, request page) any time | The Map shows the measure per stop. A course page links its spine and units |
| 5. Outreach and funding | Funding contacts carry on with what is live. No wide announcement yet | The two proven courses are what gets shown; teacher channels open after the proof |
| 7. Curriculum | The grade 4 math spine, one pilot unit and its checks (step 4) | It is step 6: spines, units, then Tracks and the Binder once several courses are full. The state crosswalk comes after that |
| 9. Recess and Curiosities | Wait with tool building, since they use the same pipeline. Design work (Recess's look, picking first games) can go on | Built in their own small waves beside the course work, never counted in the measure |
| 8. Beyond School, 10. Languages | Wait | Start only after several courses are full, or, for the first Languages wing, when a partner says yes |

### Decisions, kept few

What Cory is asked, in order: the Shape exception cards (open now); the proof card (q-proof-math-4: which three
tools, who the teacher is, which rubric, Sara's work after batch 4); the grade 4 math spine and the pilot unit; the
order and number of courses in step 6, once the cost of one is known. Everything else runs on these defaults: a spec note that makes a tool pass
the teaching test is applied without asking; a code follows the tool that really teaches it; year-long standards go
to the spine; nothing is cut to save work (rule 1). The depth rule (two or three tools on major work) applies to
math, ELA and science; other subjects only need each tool to pass the test or state its role. Questions go on the
Review Desk as cards with a pick.

## Now (set 2026-11-03, Review Desk q-plan cards)

1. **Codex:** Nonsense Words and Sight Words (grade 2 teacher request) first, then keyword-fishing and input-or-output.
   Nonsense Words is live with a pattern picker (short vowels to word endings, plus mixes) over an 894-word bank
   checked by fresh agents.
2. **Finish a cohort before more builds** (BASELINE rule 14): Credit Card Builder, Image Transformer, Data Policy
   Council, Puppet Show Feelings, World Music Map and Near and Far, end to end under the new review (people art,
   audit that saves as it goes, preflight). Repeat problems go in an issue ledger and become kit or brief fixes. A
   preflight and the ledger are adopted now; a per-tool learning contract and readiness-as-a-checklist are tried on
   this cohort and kept only if Refine counts fall.
3. **Then scale back up:** Codex builds resume with at most about 10 built and unreviewed. People art is filled for the
   11 tools missing it (314 images), each set on a contact sheet for Cory plus a fresh representation check.
4. **Worksheets, generator first (Cory, 2026-11-03):** the 15 generators reviewed well. Module pages and Sub Day pages
   now link the generators that fit each module with its settings filled in (scripts/gen_links.py), and the authored
   sheets a module has. Concept-list rows a generator can make are backed by it (the row keeps its title and place in
   the year, its link opens the generator preset): the first sift kept 26 of 746 math, science and social studies rows,
   which said the generators rarely replaced a written sheet as they stood. 2026-11-04: the settings the reviewers
   wished for were built (and a coordinate-plane generator, 16 in all), a second sift took the backed rows to 83; the
   remaining wish list is in docs/SUPPLY-CLOSET-PLAN.md, Generators. Later 2026-11-04: an assessment of every unwritten
   row (docs/agents/WORKSHEET-GAPS.md) chose 10 more generators where the gaps are biggest (arts rubrics and frames,
   world languages, music, statistics, algebra, finance, code, K-2 number, grammar), 26 in all, and a strict sift took
   the backed rows to 676. About 4,900 rows need a writer whatever we build. Authored waves
   continue for K-2 and the interpretive subjects. Cory still reviews the live shelf; the rest of wave 2 and wave 3
   follow at a slower pace.
5. **Housekeeping (from the 2026-11-03 cleanup):** after 2026-11-07, delete the staged temp folder
   `C:\Users\Cory\AppData\Local\Temp\claude\_to_delete-2026-11-03` (about 1 GB of old session scratch). Also delete
   the merged branches (`git push origin --delete audit/states codex/biased-bot`, `git branch -D audit/states`) and
   merge `claude/hopeful-dirac-qck82o` (worksheets wave 2) when that session finishes.
6. **Catalog review (planned 2026-11-10, Cory; docs/agents/CATALOG-REVIEW.md). Pilot run 2026-11-10, picks accepted; the full read is step 2 of the path above.** Pilot (36 tools, grade 4 math and grade 6 ELA): no standard without a tool and no duplicates; the issue is depth (math: 17 of 29 standard rows taught in full), and the row format must change before the full run. Every tool is specced
   or further along (7 ASL tools held), so the whole catalog is reviewed for standards coverage, duplication and
   curriculum value, from the specs this time. A cheaper model writes one row per tool, scripts make the tables, the
   top model judges only what the tables flag, and proposals come to Cory as Desk cards with a pick. Pilot on grade 4
   math and grade 6 ELA first, then the rest by subject and band. It gives the bench a build order by value, and it
   takes in checks 8a and 8b below for tools.
7. **Token plan (planned 2026-11-10, Cory; docs/agents/TOKEN-PLAN.md). Evidence pack script built and checked on two tools 2026-11-10; the three-tool quality trial runs at step 5 of the path above, on the first tools Refine resumes with.** Token cost is the biggest limit
   on growth; savings must not reduce quality. The agent logs show that re-read context, not new context, is most of
   a lens's cost, and that the Exit check and Finish check together cost about as much as the three lenses. Changes to
   try: script the counting checks, one evidence pack a round, heavy files kept out of context, a spec pre-check, and
   model tiers. Each is trialled beside the current flow on three tools and kept only if it misses no blocker or
   should-fix.

   **Order:** replaced by "The path from here" above (2026-11-10). Items 1 to 3 here (the Codex queue, the cohort,
   scaling builds back up) are paused with it.
8. **Adoption-bar checks (new 2026-11-10, docs/ADOPTION-BAR.md; a and b for tools are done by step 2 of the path above; the rest waits behind it):** three checks that
   are cheap now and costly to backfill. None of them changes the tool pipeline or holds up a build. For tools, a and
   b are now part of the catalog review; what is left of each is a short scan of the other shelves after it.
   - **a. K-2 reading scan.** A fresh agent reads every K-2 reading tool, plan, worksheet and Word Wall card for
     prompts that tell a child to guess a word from the picture or the sentence instead of sounding it out. Findings
     go in a short report; fixes go through the normal Fix step.
   - **b. Math focus and balance report.** For each math grade, how much of what we have (tools, worksheets, planned
     rows) sits on the major work of the grade, and how it splits between understanding, fluency and real-world use.
     Needs a major-or-supporting mark on each cluster in data/standards/ccss-math-clusters.txt (from the published
     focus documents, licence checked first) and a one-word kind on each tool and sheet. The report shows thin
     spots; it changes nothing by itself.
   - **c. Reading Room fields.** Add the text record and topics to the story format before the ten-story pilot
     (docs/LIBRARY-PLAN.md, "Reading level" and "Topic sets"), so the enrich waves fill them in as they go.

## Track 1: Tools (the main work)

Detail: docs/BUILD-PLAN.md (the pipeline), docs/agents/SCALE-PLAN.md (the order), docs/agents/RUNBOOK.md (how a
session runs it), docs/agents/decisions/BASELINE.md (Cory's standing rules).

1. **Now:** review the two Codex single-tool tests with Cory (docs/agents/BATCH-BR.md, "Resume here").
2. **Then spec waves** of about 30 to 50 tools, one subject or band at a time, each with its own overlap check.
3. **Art overnight per wave**, right after the spec check (docs/ART.md).
4. **Builds stream** in small mixed Build and Refine waves (docs/agents/REFINE.md), then build-only waves per family
   once its Refine counts fall. At most about 3 to 4 agents.
5. **Voice nights per refined group** on the Forge, the same nights as art.
6. **Reviews per wave** on the Review Desk. Cory reviews every K-2 and sensitive tool in full and spot-checks about
   one in four of the rest (10 to 20 hours a week available, Cory 2026-10-28).
7. **Each new tool also ships** its lesson plan, Sub Day exit file, (from Track 2, item 2) its module's anchor chart,
   and the three opening sections of its teacher notes: What it teaches, Key skills, Support at home (docs/agents/BUILD.md).
8. **Backfill those three sections on built tools** (Cory, 2026-10-30). Every tool built before the rule, live or on
   the bench, is listed in docs/agents/notes-backfill.txt: 92 at the start. Add the sections to a tool's notes.md, then
   take it off the list. An empty list means the check covers every tool. Small batches by band, each read against the
   real tool so nothing is generic; K-2 and sensitive tools get extra care on the home ideas.
9. **Try Google Antigravity's Claude Opus 4.6 as a builder** (Cory, 2026-10-30). It takes the Build and Polish slots
   the way Codex does (docs/agents/CODEX.md); Refine, merging and deploys stay in the main session. One simple tool
   first, in its own worktree, with Cory starting each round in Antigravity. The first run shows whether it can run
   the project's scripts and drive Chrome, and how far its usage limits reach. Judge it on Refine counts, next to Codex.

Shared code is grown from finished tools: a kit engine is promoted only after three finished tools use the same code
(BASELINE rule 13; the meta analysis names art-museum, rhythm and instruments as the first candidates). Older tools pick
it up later and only when needed.

### Held-back collections (their own waves)

- **ASL:** graphics only, no video or photos (Cory, 2026-10-27). Design path in docs/agents/roadmap/ASL-SIGN-STRIP.md.
  Next step is the three-sign sample (THANK-YOU, NAME, WHERE) when Cory asks for it. No ASL tool is specced or built
  before that.
- **Spanish:** needs a native-speaker review.
- **Hard history:** extra care and teacher guidance; a fresh review agent clears it (BASELINE rule 5).
- **growing-up-q-a:** Cory reviews it personally before any live push (BASELINE).

### Queued tool ideas

"Fact-check a chatbot" (generative AI) and a resume builder (near term), from BASELINE rule 10. Road Trip Atlas (Cory, 2026-11-03): travel point A to B past landmarks, with hours and days and miles compared with familiar distances; queued in data/concepts/social-studies.txt. New ideas go into
data/concepts/*.txt for a later spec wave.

### Cross-linking (standing, from 2026-11-03)

Every build ends by cross-linking (docs/BUILD-PLAN.md step 5): new tools, closet items, word wall additions and future
collections are linked from where people look and link onward to what they pair with. Each major milestone on this
roadmap closes with a cohesion pass: walk the site from the home page, grade and subject pages, module pages and the
Supply Closet, and fix dead ends, orphans and missing links before the milestone counts as done.

## Track 2: Supply Closet

Detail: docs/SUPPLY-CLOSET-PLAN.md. Live: Foundation, Sub Day, Word Wall, Anchor Charts and Posters, Family Game
Night, Word check, closet search, Take home, words CSV. What is left, in order:

1. **A quality diagram pass on 9-12 Word Wall cards.** 779 of the 1333 grade 9-12 cards print "Draw it" and have no
   picture prompt, so each card needs a decision first. Good quality only (Cory, 2026-10-27): a card gets a diagram
   only when the drawing clearly shows the idea; anything doubtful stays "Draw it".
   - Pilot: computer science (82 cards), CTE (66), math and science (10). Cory sees contact sheets of the whole pilot
     before anything ships.
   - Then, if it holds up: the diagram-friendly corners of ELA, social studies, arts and health.
   - Each picked card gets an `svg:` prompt in its word file and a spec in `diagrams.py`; no new tooling.
2. **Anchor charts ride along with each new tool.** After `plan.md` and `exit.md`, the build writes
   `data/closet/charts/<module-id>.md` if the module has none (layout, English and Spanish parts, `[[blank]]` words).
   `scripts/check_charts.py` and `build_site.py` already handle it.
   - Pipeline files to change: docs/agents/PLAN.md (a step after `exit.md`), docs/LESSON-PLANS.md (a short "Anchor
     chart" section) and `scripts/board.py` (a **Chart** column next to **Sub**).
   - These are tool-workflow files: a handoff for the tools chat, or made between waves, never from the closet side
     while a wave runs.
   - The first tool built in a module writes its chart; later tools leave it alone unless it misses a big idea.
   - A module whose tool never leaves the bench gets no chart; a small backfill batch can cover those later.
3. **Teacher-guide links, Part 2.** Tool pages and lesson plans link back to their module's Word Wall, chart and
   games. Same handoff as item 2, and it can travel with it.
4. **Print the module kit, and Sub Day lite.** One checklist on the module page that prints words, chart, game and
   Sub Day together, and a generic Sub Day for modules without a tool. Built together; waits to see how fast charts
   arrive.
5. **Break Box** (new 2026-10-31, Cory): a shelf of school-break activities for kids home while parents work. 30
   one-to-two-hour, screen-free, fun-and-imagination projects per grade, K-12 (390 sheets), each a one-page sheet
   like Sub Day: the idea, materials, goals, "I can" objectives, steps, twists, safety and a note for the grown-up.
   Written to the child's reading level from grade 3; K-2 sheets are run by a grown-up. Detail and the sheet
   framework: docs/BREAK-BOX-PLAN.md; drafts in docs/break-box/, checked by `scripts/check_breaks.py`.
   - **Done:** the framework and the draft sheets for all 13 grades.
   - **Done 2026-11-03:** shelf live with 390 sheets (`data/closet/breaks/`, `/closet/break-box/`).
   - **Still open:** Cory's read (all K-2 and anything with heat, tools or going out; one in four of the rest),
     Spanish, and the extras in the plan (a "pick for me" filter, a printable break-week pack).
6. **Worksheets** (new 2026-10-31, Cory): printable student worksheets to go with tools and modules, as a Supply Closet
   shelf. Paper is fine here, since paper is the product. Scoped 2026-11-01: 40 to 50 authored sheets per class (a
   grade of a subject, a high school course, or a language level), 215 classes, 8,947 sheets, each with a teacher
   page and answer key. Detail: docs/WORKSHEETS-PLAN.md; concept lists in docs/worksheets/, checked by
   `scripts/check_worksheets.py`.
   - **Done 2026-11-01:** concept lists for all 215 classes (8,947 sheets), checker clean.
   - **Trimmed 2026-11-04 (Cory):** 1,831 unwritten rows cut to about 30 hand-written sheets a class, generator sheets on
     top (7,116 rows left). Fresh agents proposed the cuts (docs/agents/trim/, rules in BRIEF.md, checked by
     `scripts/trim_check.py`), Cory approved them as proposed, `scripts/trim_apply.py` removed them. Row numbers are
     ids (sheet links use them), so lists now have gaps; the class page shows 1..N. Thin areas it left: end of this
     roadmap.
   - **Now:** Cory reviews the lists (French has no modules yet; ASL waits on the ASL sign-strip sample; hard history sheets
     get the fresh review).
   - **Pilot done 2026-11-01:** the shelf (`/closet/worksheets/`, a page for each of the 215 classes, one shared viewer
     with student copy and answer key) and 10 built sheets across K-Algebra I, checked by `scripts/worksheets.py`.
   - **Wave 1 done 2026-11-01:** 398 more sheets (two per class: the first and one mid-year), 408 built in all across
     204 classes (world languages held). Every student copy prints within its limit (K 1 page, others 2).
   - **Wave 2 mostly done:** 600 of 700 written (1,008 in all). The rest is a later batch.
   - **Live 2026-11-03** (Cory: the site is not announced, so he reviews it live).

7. **Teacher Desk** (new 2026-11-03): **shelf live 2026-11-03** at /closet/teacher-desk/ with the **Desk Dock**
   (/closet/teacher-desk/dock/): a timer, a 12-sound board, a noise meter and a group maker on one projector screen,
   all sound made in code. Claude built it by hand as its own page, not through the tool pipeline (Cory: purpose built
   for its job). Not yet checked: how the sounds and the noise meter behave on a real classroom laptop.
   **Classroom Music** (live 2026-11-03, /closet/teacher-desk/music/): eight original pieces in four sets (work time,
   quiet time, clean-up, game show), every note generated in the browser as it plays (motif melodies from a seeded
   random source, so each run differs), so there is no recording to license: it ships under the site's own licence.
   Stop-after timer with a fade and an end chime, volume, keys 1 to 8, dark screen. Levels checked offline (no
   clipping); Cory to judge by ear. Next: a game-show quiz board.
   **Printables shelf** (built 2026-11-03, /closet/printables/): 17 settable, print-ready pages drawn by one engine,
   site/assets/printables.js (paper: handwriting, lined, graph, dot; math and letters: number lines, hundreds chart,
   alphabet strips and cards; organizers in English, Spanish or both: Venn, KWL, story map, cause and effect, main idea,
   T-chart, sequence, Frayer word map; classroom: name plates, certificates). Spanish labels checked by a fresh agent.
   **Research Cards** (live 2026-11-03, grown to 50 the same day, /closet/research-cards/): a K-2 intro to research,
   50 two-page cards (13 people, 13 places, 12 things, 12 animals) from data/research-cards.json plus a blank "my own
   topic" card. Page 1 is a three-paragraph read, quick facts, words to know and a talk prompt; page 2 has find-it
   questions, draw and label, I wonder and sources. Hard history is stated plainly but briefly, and each card stays
   positive. Facts and sensitivity checked by fresh agents. Photos are public domain or CC0 only
   (site/assets/research/, source and licence in CREDITS.json, listed in docs/ART-STATUS.md); a card without one shows
   its emoji. Cross-linked: each card lists its module ids, so K-5 module pages show a Research Cards row, and the
   Library and Research Skills modules show the whole set.
   Next ideas: Word Wall bingo and flash cards, a quiz-show board and scoreboard for the Teacher Desk.
8. **Learning Supports** (new 2026-11-03): tools for learners who need extra support, worded carefully but
   confidently. Each says what approach it follows (for example decodable nonsense words used in structured
   literacy) and that it is practice, not a diagnosis or treatment; a fresh agent reviews the wording. Nonsense Words
   is its first tool. A site-wide accessibility bar (dyslexia-friendly font, high contrast, reduced motion) follows
   the cohort kit fixes. An IEP goal bank is parked until a special-education reviewer is found.
9. **The Map** (Phase F): BUILT 2026-11-03. A teaching map for teachers and admins, tucked away as "Teaching map" in
   the footer's Browse column, not the top nav: /map/ (regions by subject and grade, shaded by how much is ready), a
   page per region (/map/<subject>/<grade>/, a trail of stops with pins, planned stops drawn as outlines, a plain list
   below, a vertical trail on phones) and a "where this sits" strip on /standards/<code>/ pages. Upkeep: one row per
   new module in data/sequence.csv (order, builds_on, basis); the build warns, and does not fail, when a module has
   none, and draws it at the end of its region. Everything else is derived from existing data at build time
   (scripts/teaching_map.py). Cory spot-checks one region per subject.

**Still owed, any time:** a real-printer test of every print format, the Spanish native review, family game
play-tests.

## Track 3: Reading Room

Detail: docs/LIBRARY-PLAN.md. About 700 stories are curated and processed into readable text. Next:

1. **Pilot:** ten stories in the 3-5 band end to end (format, reader, pipeline). The format gains a text record and
   topics first (Now, item 8c; docs/ADOPTION-BAR.md).
2. **Enrich and verify** in waves of about 50: word help, questions, teacher notes, the text record and topics, then
   a cold verify agent. Stories that share a topic are shown together as topic sets.
3. **K-2 read-aloud** as the voice bank allows.
4. Later: the Excerpts shelf and the Speeches and Documents collection.

## Track 4: The site

Detail: docs/SITE.md. File limit (static assets cap at 20,000 files): solved 2026-11-03 by moving the pictures
(Reading Room and Word Wall art, about 10,200 files) to the R2 bucket curioclass-media, served at the same URLs by
worker/index.js. Before each deploy run scripts/sync_media.py, which uploads new pictures. The "On the bench" tab and
/bench/ page were removed 2026-11-03 (Cory: not useful); sketched tools still show on module pages. Classrooms (2026-11-03): the Grades and Subjects
pages are combined into one page, /classrooms/ ("Pick a classroom": grade rooms and subject wings, every chip and tile
a direct link); /grades/ and /subjects/ redirect there, and the grade and subject pages crumb back to it. The top nav
is Classrooms, Supply Closet, Search, About; the Reading Room left the nav and stays in the footer and the Supply
Closet. The home eyebrow now reads "Free for everyone, always". Open items: the
www.curioclass.org redirect, dark mode, and a
request page for teachers (the About page email does this for now).

## Track 5: Outreach and funding (new 2026-10-28)

Detail: docs/funding/ (one-pager, cost sheet, prospect list).

1. **Funding:** Cory's aim is a first philanthropic grant of about $10,000 to speed up the build. The cost sheet and
   one-pager are the ask; the prospect list is who to send them to. Emails go out from Cory.
2. **Donation page, later:** a catalog of buttons. Coffee $7.25, lunch $20, local outreach $100, national outreach
   $1,000, a tier between (about $2,500, "fund a collection"), international development and outreach $15,000. The
   top tiers are "get in touch" rather than one-click. The page says plainly whether gifts are tax-deductible.
3. **Reach without tracking:** Cloudflare's server-side request counts (no cookies, no page code) and teacher
   stories by email. Never student analytics.
4. **Teacher channels** (from docs/PHASE0-PLAN.md section 6): OER Commons and state OER repositories, Merlot, free
   listings that point back here, teacher subreddits and groups, ed social media. First users: Cory's family of
   teachers.

## Track 6: Going public (done)

The repo (LochLogic/curioclass) has been public since 2026-10-28. The site is live but not announced; outreach is
Track 5.

## Track 7: Curriculum (merged 2026-11-03: units, then Tracks, then the Binder)

From single tools to complete courses a teacher can run start to finish, one ladder. This track is where the
adoption bar applies (docs/ADOPTION-BAR.md, BASELINE rule 20): reviews judge a whole course, so the year's shape
comes before the units that fill it.

1. **Year spine** (new 2026-11-10; what it must hold is item 1 of "What a finished course holds"; starts after the catalog review's pilot on the same two courses, Now item 6, whose
   coverage tables it builds on): for each pilot course (grade 4 math, grade 6 ELA), one page that puts the
   year's units in order and says why each sits where it does: what it builds on, what it sets up, and for math,
   how much of the year goes to the major work of the grade. It starts from data/sequence.csv and the module list,
   and names the gaps. Units are cut from the spine, not gathered from whatever parts are finished. Cory reviews
   both spines before the unit pilot is written.
2. **Units** (the capstone, Cory 2026-11-03): worksheets, handouts, topics and ready-made prompts packaged into a 1 to
   5 day, mostly non-tech unit, with daily plans, a partner game, a short assessment and optional practice drills
   (math facts and the like). Projector slides (warm-up, launch, turn and talk, exit ticket) are one part of a unit day.
   Each day opens and closes by saying where it sits in the unit and the year.
   **Pilot:** grade 4 area and perimeter and a grade 6 argument essay; Cory reviews both before a unit wave.
   - **Teacher pages that teach the teacher** (tried on the pilot, 2026-11-10): each unit says why its main model or
     picture was chosen, what students tend to get wrong with a key that shows what each wrong answer means, and how
     to shorten or stretch a day without making it easier. Kept for the unit wave, and offered to tool lesson plans,
     only if Cory finds them useful in the pilot.
   - **Judged against the bar:** each pilot unit gets a fresh-agent read against the matching part of
     docs/ADOPTION-BAR.md, and the findings go to Cory with the unit.
   - Hands-on work uses things a classroom or home already has, or names a cheap stand-in (docs/agents/STANDARDS.md).
3. **Tracks:** units in a year's order with pacing for each subject and grade, grown from the year spines (the
   vision's Tracks idea; the public name is to be workshopped when it ships, keeping "Curio Class" whole).
4. **The Binder:** export a course as a link, a zip or an LMS course cartridge. The cartridge carries content only;
   nothing in it sends rosters, sign-ons or grades anywhere.

Later: score codes (a code and QR a student shows the teacher, scanned on the teacher's own device; never called
proof or cryptographic) and the state standards crosswalk. The crosswalk starts with one state outside the Common
Core as the test (the state picked when it starts), as a mapping layer over modules and data/sequence.csv, with CASE
as the file format in and out (docs/ADOPTION-BAR.md). The second reader (a teacher) that PHASE1-SCOPE left open is now part of step 4: a working
teacher reads the pilot unit, and the alignment of its standards is one of the things they are asked about.

## Track 8: Beyond School (new 2026-11-03, late)

Modules past K-12: ACT/SAT-style practice first, then one trade (electrical, plumbing or automotive), then
certification prep such as security fundamentals. Titles never use trademarks or branded material; bar exam prep
comes last and needs expert review.

## Track 9: Recess, the games shelf (new 2026-11-07, concept stage)

A treat from the teacher: when kids are fully done, they go to Recess and play. Mentally stimulating games with
educational undertones that never feel like class. Real games where the thinking is the fun: you get better at the game by getting better at the skill
(untangle as graph planarity, match-3 as chemical bonding, tower defense as the immune system). Original games only:
a genre's mechanic is fine, a specific game's name, art or levels never are. Cory is sold on the idea (2026-11-07).
Named Recess, rules set (2026-11-07): open to all, grade bands shown not enforced, best scores saved on the device with arcade-style initials, no class on the screen. Next: Recess's look, then pick the first games from the research pass (docs/GAMES.md,
docs/agents/research/GAMES-RESEARCH.md), then spec them like any tool.

## Track 10: Languages (new 2026-11-07, later stage of site growth)

A Languages section with wings, each grown on its own:

1. **Native languages of this land (first wing, partner-led).** Starts as an archive and grows into a mid-level
   learning tool (a sound-and-word library, themed phrase sets, practice games on that library, teacher and family
   pages), heading toward a course only if the partner community wants one. Hand talk (Plains Indian Sign Language)
   belongs here, shown by real signers. Rules: one language and one community at a time; the community decides what
   is public and owns its material; nothing is gathered from archives without permission, and nothing is written or
   filled in by AI. Keeping the languages alive comes first, and the wing serves that. Starts only when a partner says
   yes; the conversation opener is drafted (not public).
2. **Later wings:** Latin-alphabet languages (Spanish, French, Latin and others), then Cyrillic-script languages, and
   more as the site grows. These can use licensed or public-domain material and the same engines as the first wing.

Needs more thought before anything is built (Cory, 2026-11-07): how the section relates to the existing world
languages modules, what "mid-level" means in lessons, and which engines are shared across wings.

## Late and far back

- **Worksheet Generator**: no longer late. Live since 2026-11-03 and now the first path for procedural practice (see Now, item 4). Design in docs/SUPPLY-CLOSET-PLAN.md.
- **Classroom projects by standard** (future input): an off-screen project per module from Cory's notes.
  docs/agents/roadmap/CLASSROOM-PROJECTS.md.
- **Class Cast** (parked 2026-11-03): live class sync through a relay. Only with funding and someone to keep a server
  running.
- **Read-aloud for grades 3-12** in the Reading Room (end of the roadmap).
- **Instrument learning paths** (far back, parked 2026-10-25): one tool per instrument with 10 to 12 levels on a shared
  engine (mic pitch detection, Web MIDI, Note Ninja staff). Recorder first, then keyboard, ukulele, guitar, voice;
  band instruments only partly (a browser can't see the player's hands or hear mouthpiece shape well enough to
  correct it). Own shelf under Arts and Music.

## Thin areas after the worksheet trim (2026-11-04, deal with later)

Cory approved the trim as proposed and set these aside for later. Each is a list to look at again, not a decision.

- **ELA, one-sheet modules:** 97 ELA modules (spread across K-8, 6 to 13 a grade; only one in grades 9-12) now have a single sheet, because ELA
  units have many small modules. The checker floor dropped from 2 sheets a module to 1 so the trim could land
  (`MIN_PER_MODULE` in scripts/check_worksheets.py). Choose: give those modules a second sheet back (about 97 rows,
  from the cut lists in docs/agents/trim/ela.csv), or accept one and set the floor back to 2 elsewhere.
- **Read and respond cuts:** the reading sheets took heavy cuts outside ELA: health 39, dance 22, science 20,
  computer science 18, media arts 18, world languages 16. Check that each unit still has some reading in it.
- **Source analysis cuts:** 12 in social studies (plus a few elsewhere), though no unit lost its only one.
- **ASL culture readings:** 33 ASL rows cut, some of them Deaf culture readings. Review with the ASL work (sign-strip
  sample) before those units are built.
- The cut rows stay in docs/agents/trim/<subject>.csv (title, type, module, reason) for any of these to come back.
