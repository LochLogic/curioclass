# Roadmap

The one plan for Curio Class: what is done, what comes next, and in what order. Consolidated 2026-10-28 from the
"Later phases" section of docs/PHASE0-PLAN.md, the Supply Closet roadmap, docs/agents/SCALE-PLAN.md,
docs/LIBRARY-PLAN.md, docs/SITE.md ("Not done yet") and docs/agents/roadmap/.

Why and where: docs/VISION.md (the north star, 2026-11-03). This file holds the order and the status. The design detail stays in each track's own plan, linked from its section.
When a roadmap item starts, finishes or moves, update it here first, then post it to the Review Desk's Roadmap tab
(`python scripts/desk_roadmap.py <out.json>`, then ArtifactData set stats/roadmap).

## Where it stands (2026-11-03)

| | Count |
|---|---|
| Tool concepts in the catalog | 800 |
| Live tools | 83 |
| Specs written | 238 more, plus 11 built and waiting on voice |
| Built by Codex, waiting on review | about 80 (8 reviewed) |
| Worksheets live | 1,008 of 8,947 planned (live 2026-11-03) |
| Modules with Word Wall cards | 762 of 797 (4,413 cards), English and Spanish |
| Anchor charts / posters / Game Night games | 74 / 54 / 104 |
| Sub Day packets | 79 |
| Reading Room stories curated and processed | about 700, not live yet |

`python scripts/board.py` gives the live tool counts (docs/BUILD-BOARD.md).

## Goal

Reach and craft together (Cory, 2026-10-28). As many teachers as possible should know Curio Class exists; nobody
needs to use a tool that does not fit their class, but every tool must be really good. Free for good: no paywall,
no accounts, no ads, no tracking.

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
   sheets a module has. Next: concept-list rows that a generator can make are backed by it (the row keeps its title and
   place in the year, its link opens the generator preset), then about 10 more generators where the lists are thickest
   and really procedural (place value, decimals and percents, ratios, integers and order of operations, angles and
   coordinates, statistics, phonics and spelling, grammar, unit conversions, balancing equations). Authored waves
   continue for K-2 and the interpretive subjects. Cory still reviews the live shelf; the rest of wave 2 and wave 3
   follow at a slower pace.
5. **Housekeeping (from the 2026-11-03 cleanup):** after 2026-11-07, delete the staged temp folder
   `C:\Users\Cory\AppData\Local\Temp\claude\_to_delete-2026-11-03` (about 1 GB of old session scratch). Also delete
   the merged branches (`git push origin --delete audit/states codex/biased-bot`, `git branch -D audit/states`) and
   merge `claude/hopeful-dirac-qck82o` (worksheets wave 2) when that session finishes.

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

1. **Pilot:** ten stories in the 3-5 band end to end (format, reader, pipeline).
2. **Enrich and verify** in waves of about 50: word help, questions, teacher notes, then a cold verify agent.
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

From single tools to complete courses a teacher can run start to finish, one ladder:

1. **Units** (the capstone, Cory 2026-11-03): worksheets, handouts, topics and ready-made prompts packaged into a 1 to
   5 day, mostly non-tech unit, with daily plans, a partner game, a short assessment and optional practice drills
   (math facts and the like). Projector slides (warm-up, launch, turn and talk, exit ticket) are one part of a unit day.
   **Pilot:** grade 4 area and perimeter and a grade 6 argument essay; Cory reviews both before a unit wave.
2. **Tracks:** units in a year's order with pacing for each subject and grade (the vision's Tracks idea; the public
   name is to be workshopped when it ships, keeping "Curio Class" whole).
3. **The Binder:** export a course as a link, a zip or an LMS course cartridge.

Later: score codes (a code and QR a student shows the teacher, scanned on the teacher's own device; never called
proof or cryptographic) and the state standards crosswalk. Also open (from PHASE1-SCOPE): a second reader (a
teacher) checks best-fit standards alignment for one subject.

## Track 8: Beyond School (new 2026-11-03, late)

Modules past K-12: ACT/SAT-style practice first, then one trade (electrical, plumbing or automotive), then
certification prep such as security fundamentals. Titles never use trademarks or branded material; bar exam prep
comes last and needs expert review.

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
