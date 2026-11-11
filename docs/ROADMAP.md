# Roadmap

The one plan for Curio Class: what is done, what comes next, and in what order. Consolidated 2026-10-28 from the
"Later phases" section of docs/PHASE0-PLAN.md, the Supply Closet roadmap, docs/agents/SCALE-PLAN.md,
docs/LIBRARY-PLAN.md, docs/SITE.md ("Not done yet") and docs/agents/roadmap/.

Why and where: docs/VISION.md (the north star, 2026-11-03). The quality bar for full courses: docs/ADOPTION-BAR.md
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
really good. A course is a grade of a subject or a high school course.

**One measure.** For each course: standards taught in full, out of all its standards, counting tools, units,
worksheets and the Reading Room together. It goes on the Desk, and every step below moves it.

**What the review found (2026-11-10).** 63 tools read against the bar. Coverage and duplication are fine. The repeated
flaw: tools show the idea, then leave the student's own part of the standard thin, optional or passable by trial,
worst on the major work of a grade. The gap in shape: a module lists a cluster, gets one tool, and the rest of the
cluster is taught nowhere. Verdict: right raw material, fixable now, costly later.

### The shape we build to

| Piece | What it is | Rule |
|---|---|---|
| **Course** | A grade of a subject | Gets a year spine: its units in order, with the reason for the order |
| **Unit** | A 1 to 5 day package inside a course | Points at modules and picks from every shelf. Owns only the order, the teacher pages and what no shelf has |
| **Module** | One teachable topic, and the hub page every shelf hangs from | Split only when it holds two unrelated topics, and then properly. Its standards are spelled out, never a bare cluster |
| **Tool** | One screen piece | Carries only the codes it teaches on its main path, and a role: lesson, see why or practice. Major work in math, ELA and science gets two or three tools |
| **Shelves** | Word Wall, charts, Game Night, Sub Day, lesson plans, worksheets, generators, Reading Room, The Map | Keep their keys. Worksheets and generators are the home of fluency and extra practice; the Reading Room is the home of year-long reading |
| **Ledger** | data/coverage.csv | One row per standard per course: where it is taught in full. The one home of a coverage claim and the source of the measure |
| **Recess, Curiosities** | Play and wonder | Outside the bar. They claim no standard |

Rules: BASELINE 21 (the teaching test, roles) and 22 (modules, depth on major work). How the shelves fit:
docs/ECOSYSTEM.md. Decisions: docs/agents/decisions/DESK-ANSWERS.md, 2026-11-10.

### The six steps

**Tool building is paused** (Build, Refine and the Codex queue) until step 5. Fixes to live tools in step 3 are the
one exception.

| Step | What | Done when | Cory decides |
|---|---|---|---|
| 1. Rules. **Done 2026-11-10** | The teaching test and six rule edits are in SPEC.md, REFINE.md and docs/TOOL-CONTRACT.md. Common Core math and ELA texts and the major-work marks are filed in data/standards/. Not filed yet: science and the other subjects' standard texts | A new spec or lens cannot pass a tool that fails the test | Nothing |
| 2. Read. **Next** | Every spec read with row format 2: the 36 pilot tools again as the test, then all the rest by subject and band (about 64 cheaper-model agents). Scripts build the ledger and one map per course, and flag two-topic modules | Every course has its map and its measure | Nothing |
| 3. Fix what is built | The live-tool fixes in the order in DESK-ANSWERS, then whatever the read finds in the other live tools. The shelf fixes in docs/ECOSYSTEM.md: pages, search, plans and Sub Day show a tool's own codes; worksheets join by module id; The Map counts a stop ready when its lesson tool is live. The 149 built tools waiting on Refine are not fixed now; the new Teaching lens catches them when Refine resumes | Every live math, ELA and science tool passes the test or carries an honest role, and a module can hold a second tool without any page showing a wrong code | Nothing, unless a fix changes what a tool teaches |
| 4. Shape | From the maps, by rule: module standards spelled out, spec notes applied, second and third tools listed for major-work modules, supporting tools that wait, worksheet presets and Reading Room sets written into the ledger, and a build order by value (data/waves.csv) | data/modules.csv, the specs, the ledger and the build order all agree with the maps | One Desk card per subject, exceptions only: reshape, hold, cut, new tool, split a module |
| 5. Prove one course | Grade 4 math and grade 6 ELA (Track 7): the year spine, then one pilot unit each, pulling from every shelf, read by a fresh agent against docs/ADOPTION-BAR.md. Building resumes for these two courses only. The token plan's side-by-side trial runs on the first three tools | Cory can open one unit of each and see the bar met | The two spines, then the pilot review |
| 6. Scale by course | Build and Refine resume in value order: finish a course before starting the next, major work first. Each finished course gets its spine, units and a full row on the measure | Course by course, the measure reaches full | The order of courses |

**Resume here: step 2.** First jobs, in order: teach scripts/catalog_compute.py to read row format 2 and the filed
texts in data/standards/ (it still reads docs/agents/catalog/math-focus.csv); build data/coverage.csv; re-run the 36
pilot tools and compare with the pilot judge files; then the full read. Everything it needs:
docs/agents/CATALOG-EXTRACT.md, docs/agents/CATALOG-REVIEW.md, docs/agents/catalog/.

### What every other track does meanwhile

| Track | Until step 5 | From step 5 on |
|---|---|---|
| 1. Tools | Paused, except the step 3 fixes. Held collections, queued ideas and the Codex queue wait | Resumes for the two pilot courses, then by course |
| 2. Supply Closet | Carries on: worksheet waves, generators, the Word Wall diagram pass, Break Box read. Its shelf fixes land in step 3. Charts and teacher-guide links wait for building to resume, since they ride with a tool | Each unit names what it pulls from the closet. The module kit and Sub Day lite follow the unit pilot |
| 3. Reading Room | Add the text record and topics to the story format, then the ten-story pilot. It can run beside steps 2 to 4 | Topic sets are written into the ledger for the standards they carry; enrich waves follow the course order |
| 4. The site | The step 3 page changes. Open items (www redirect, dark mode, request page) any time | The Map shows the measure per stop. A course page links its spine and units |
| 5. Outreach and funding | Funding contacts carry on with what is live. No wide announcement yet | The two proven courses are what gets shown; teacher channels open after step 5 |
| 7. Curriculum | Nothing before step 5 | It is steps 5 and 6: spines, units, then Tracks and the Binder once several courses are full. The state crosswalk comes after that |
| 9. Recess and Curiosities | Wait with tool building, since they use the same pipeline. Design work (Recess's look, picking first games) can go on | Built in their own small waves beside the course work, never counted in the measure |
| 8. Beyond School, 10. Languages | Wait | Start only after several courses are full, or, for the first Languages wing, when a partner says yes |

### Decisions, kept few

What Cory is asked, in order: the step 4 exception cards (one per subject); the two year spines and the pilot units
in step 5; the order of courses in step 6. Everything else runs on these defaults: a spec note that makes a tool pass
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

1. **Year spine** (new 2026-11-10; starts after the catalog review's pilot on the same two courses, Now item 6, whose
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
as the file format in and out (docs/ADOPTION-BAR.md). Also open (from PHASE1-SCOPE): a second reader (a teacher)
checks best-fit standards alignment for one subject.

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
