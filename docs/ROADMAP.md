# Roadmap

Reworked 2026-11-22 to match docs/PRODUCTION-PATH.md and docs/HANDOFF.md. The text it replaced is in
docs/archive/ROADMAP-history-2026-11-22.md (older history: docs/archive/ROADMAP-history-2026-11-11.md); nothing in
either archive is current.

This file holds the order of work across every track, and nothing else. The current state and the next action:
docs/HANDOFF.md. How a course is made: docs/COURSE-RUN.md (the process) and docs/PRODUCTION-PATH.md (why the core is
planned top down). What Curio Class is for: docs/FOUNDATION.md and docs/VISION.md. The bar: docs/ADOPTION-BAR.md.
The words: docs/GLOSSARY.md. Each track's design detail stays in its own plan, linked below. When an item starts,
finishes or moves, update it here, then post it to the Review Desk's Roadmap tab
(`python -X utf8 scripts/desk_roadmap.py <out.json>`, then ArtifactData set stats/roadmap).

## Goal

Reach and craft together (Cory, 2026-10-28). As many teachers as possible should know Curio Class exists; nobody
needs to use a tool that does not fit their class, but every tool must be really good. Free for good: no paywall,
no accounts, no ads, no tracking.

The end goal is FOUNDATION section 1: a teacher can run any course on Curio Class from the first day to the last,
free, with no account, and the course would stand up to a state adoption review. The courses together cover what an
American public school teaches from kindergarten to grade 12. Every course is finished to the bar; breadth is where
the site ends up, not a reason to spread thin.

## Where it stands

State lives in docs/HANDOFF.md. Counts by course: docs/COURSES-STATUS.md (`python -X utf8 scripts/course_status.py`).
Tools by step: docs/BUILD-BOARD.md (`python -X utf8 scripts/board.py`). By stage: the Desk Dashboard's plan flow.
Parked work: data/plans/later.csv. In one line, on 2026-11-22: all 52 core courses are planned down to units, days are
written for kindergarten to grade 3 in science, social studies and ELA, and the site is not launched.

## The course work: the order

The order is docs/PRODUCTION-PATH.md, section 3 (Cory, 2026-11-13; BASELINE rules 24 and 25), and every course runs
by docs/COURSE-RUN.md (since 2026-11-20). In short:

1. **Core subjects first.** Math, ELA, science and social studies (52 core courses, plus 6 core electives that wait)
   come before every other subject. This sets the order, not the scope.
2. **Planned top down.** Progressions, course frames, scopes and sequences and unit plans for every core course
   before days, each layer reviewed, with Cory's go or no-go at each baseline. Social studies went first; science,
   ELA and math followed together. Grade 4 math's older work is reconciled into math's units (later.csv L13).
3. **Then days, a grade at a time** (COURSE-RUN stages 5 and 6): section plans, plan data and keys, then
   ledger-gated days and a retool before the next grade. A subject's first grade starts with a unit 1 probe.
4. **Then each course's finish** (COURSE-RUN stage 7): the course's checks as one assessment plan, a coherence pass,
   English learner supports, Art and voice, the tools its sections name, the final reads, and Cory's Sign-off.
   Before any course goes live: the watch items in later.csv L101.
5. **Then the subjects after the core**, from COURSE-RUN stage 1: first the 6 core electives, then the other
   subjects (PRODUCTION-PATH, "After the core subjects"). Stage 1 and the progressions are already done for every
   after-core subject.

Where each core subject stands in that order, as of 2026-11-22:

| Subject | Done | Waits on | Next |
|---|---|---|---|
| Social studies | All units planned; kindergarten to grade 3 days written and fixed | Nothing | Grades 4 and 5 and World Geography I, one lane of the next run |
| Math | Kindergarten to grade 3 Goal maps and section skeletons (later.csv L102) | Nothing | Kindergarten to grade 3, the other lane of the next run, with a unit 1 probe |
| Science | Kindergarten to grade 3 days written and fixed | Cory (later.csv L81) | Refine 1 and grades 4 and up, when Cory lifts the pause |
| ELA | Kindergarten to grade 3 days written and fixed | Not yet queued | Grades 4 and up, after the current run |

## The layers

What stands on what. Each layer is built on the ones under it and may not contradict them. A layer is made solid
enough to build on, then corrected by what is built on it; none is declared finished in the abstract (FOUNDATION
section 7, item 4). The state of each layer is in docs/HANDOFF.md and docs/COURSES-STATUS.md.

| Layer | What it is | Its home |
|---|---|---|
| 1. Foundation | What Curio Class is for, who it serves, the promises, the bar, what we assume about the room, what a tool is for | docs/FOUNDATION.md |
| 2. Standards | What must be learned. Not ours to change | data/standards/ |
| 3. Approach to teaching | How students learn here and why, with its sources: a shared core, then a page per subject | docs/APPROACH.md, APPROACH-MATH.md, APPROACH-ELA.md; science and social studies pages before their days (later.csv L27); sources in docs/APPROACH-SOURCES.md |
| 4. Progressions | What each grade owns, assumes and hands on, per subject | data/progressions/<subject>.csv; data/sequence.csv keeps the topic order |
| 5. Course frame and scope and sequence | What a course is, then every teaching day of its year in order, with the reason | docs/courses/<course>/frame.md and scope-and-sequence.md; data/plans/<course>/days.csv |
| 6. Unit and section plans | The contract for each unit and section: the checks written first, what each day is for, where a tool is used and for what job | docs/courses/UNIT-PLAN.md (fields, rules, caps); docs/courses/<course>/ |
| 7. Days, tools, print, checks | What students and teachers touch | docs/courses/LESSON-DAY.md; the shelves and tools; COURSE-RUN stages 5 to 7 |

Running through every layer: the assessment system, and the supports for English learners, access, teachers and
families (next section). Well-reviewed open courses and base texts are evidence at layers 5 and 6, never the course
itself (FOUNDATION section 1; PRODUCTION-PATH section 1, item 5).

## What a finished course holds

The list of what "finished" means, so no step can call a course done on tools alone. COURSE-RUN stage 7 checks it.

1. **A scope and sequence** that accounts for every day: 160 in a full-year course, 80 in a half-year course
   (docs/courses/CALENDAR.md; the frame sets the number). Each unit has its days, its reason for sitting where it
   does, what the grade before hands it and what the grade after needs from it. A day Curio Class has nothing for is
   listed as a gap day, never papered over.
2. **Sections for every day on the scope and sequence**, each pulling from the shelves, with daily plans and teacher
   pages.
3. **Every standard taught in full by a live tool or a section lesson**, and each of those tools verified: played
   against its spec, logged in docs/agents/catalog/verified.txt.
4. **Assessment at three sizes.** In every tool, the unaided check (SPEC.md hooks). In every unit, a short readiness
   check on the standards it builds on, a short written check as the unit goes, and an end-of-unit assessment with a
   key that says what each wrong answer means. In the course, the cumulative checks its scope and sequence names (a
   start-of-year check where it has one, then one each quarter and at year end), each followed by a respond day.
   Items come from the generators where they can, so a check can be redrawn; explain tasks and reading checks need
   fixed items in two forms. With no accounts, results live on a printable class record sheet and in score codes.
5. **English learner supports** in every tool (the hooks) and on every section's teacher page: the language the
   lesson asks for, the key words with their Word Wall cards, sentence frames for the talk and the writing.
6. **Access.** Every tool passes the hooks and an automated access check at the Finish check; one keyboard-only play
   is part of verifying it. Printables read in black and white.
7. **The agent reads** of FOUNDATION section 7, item 3 (answer key, safety, sensitivity, rights, Spanish), each by a
   fresh agent. No outside reader is planned (Cory, 2026-11-14).
8. **Honest public claims.** The course's pages say taught, practiced or shown per the ledger, never more.
9. **A fresh-agent read of the whole course** against the rubric on file, with every finding closed or listed. The
   reader is the curriculum expert (docs/agents/EXPERT.md), always run cold, after it researches outside sources.

Listed 2026-11-11; whether each is in or not-now is still Cory's to decide (also FOUNDATION, "Open questions"):

10. **Accessibility conformance to a named level**, for tools and for print files.
11. **A versioning and errata rule for a live course:** how a section is versioned, held steady for a school year
    and corrected.
12. **A course-level teacher guide with pacing options**, the shorter path among them.
13. **A state alignment document:** one worked crosswalk on the first finished course.
14. **Spanish student materials.** Family notes are already in English and Spanish; student pages are not. Cory
    2026-11-16: grow Spanish accessibility across the site after the core courses (later.csv L60).
15. **A print-volume count per student:** the pages a student uses in a year.

## Track 1: Tools

Detail: docs/BUILD-PLAN.md (the pipeline), docs/agents/SCALE-PLAN.md, docs/agents/REFINE.md, docs/agents/RUNBOOK.md,
docs/agents/decisions/BASELINE.md.

- **State.** Held since 2026-11-10: no Build, Refine or Codex queue builds, Community Plot Planner included. Live
  tools stay live as free-standing tools and claim no course coverage (BASELINE rule 26). The one exception is a fix
  that holds whatever happens (a wrong fact, a broken control on a live tool).
- **Waits on.** Tools come after days in the top-down order (PRODUCTION-PATH step 9): a course's key tools are built
  or rebuilt at its finish (COURSE-RUN stage 7) for the sections that name them, live and verified, with print
  covering the rest. No tool is built or refined until a section plan names its job (FOUNDATION section 6). No
  course has reached stage 7 yet.
- **Next.** When the first course reaches stage 7: its key tools, taken from the three bins (BASELINE rule 26), then
  its light tools; the tool-step leftovers are later.csv L39.
- **Waiting with tools:** the teacher-notes backfill (docs/agents/notes-backfill.txt, checked by scripts/check_tools.py);
  the held collections (ASL after later.csv L93 and the sign-strip sample, docs/agents/roadmap/ASL-SIGN-STRIP.md;
  Spanish after its review; hard history after a fresh review, BASELINE rule 5; growing-up-q-a after Cory's own read);
  queued ideas in data/concepts/*.txt (fact-check a chatbot, a resume builder, Road Trip Atlas); shared kit engines,
  promoted only after three finished tools use the same code (BASELINE rule 13).
- **Cross-linking, standing.** Every build ends cross-linked (BUILD-PLAN step 5). Each major milestone closes with a
  cohesion pass: walk the site from the home page, grade and subject pages, topic pages and the Supply Closet, and
  fix dead ends, orphans and missing links before the milestone counts as done.

## Track 2: Supply Closet

Detail: docs/SUPPLY-CLOSET-PLAN.md. The shelves are on the site (built with `--closet`, docs/SITE.md). The closet is
not held by rule, but no closet wave has run since 2026-11-10; the course runs hold the work. Each section names
what it pulls from the closet (docs/ECOSYSTEM.md). In order:

1. **Word Wall diagram pass on grades 9 to 12** (779 cards print "Draw it"): pilot on computer science, CTE, math and
   science, with contact sheets to Cory before anything ships. Not started.
2. **Anchor charts ride along with each new tool.** Waits on tools (Track 1).
3. **Teacher-guide links, part 2** (tool pages and lesson plans link to their topic's Word Wall, chart and games).
   Travels with item 2.
4. **The topic kit and Sub Day lite.** Waits to see how fast charts arrive.
5. **Break Box** (docs/BREAK-BOX-PLAN.md): 390 sheets on the shelf since 2026-11-03. Open: Cory's read, Spanish,
   the plan's extras.
6. **Worksheets** (docs/WORKSHEETS-PLAN.md): 1,008 built of 7,116 planned rows. Open: Cory's read of the lists, the
   last 100 of wave 2, the thin redrawn social studies courses (later.csv L8), and the thin areas at the end of this
   file.
7. **Teacher Desk** (Desk Dock, Classroom Music, Printables, Research Cards: on the shelf since 2026-11-03). Open: a
   check of the sounds and noise meter on a real classroom laptop, Cory's ear on the music. Next pieces: a game-show
   quiz board, Word Wall bingo and flash cards.
8. **Learning Supports** (Nonsense Words first). How Curio Class serves students with disabilities is later.csv L54.
9. **Teaching map.** Hidden since 2026-11-12; it returns as a picture of the scopes and sequences once courses are
   built (docs/SITE-DESIGN.md).

Still owed, any time: a real-printer test of every print format, the Spanish read (later.csv L48), family game
play-tests.

## Track 3: Reading Room

Detail: docs/LIBRARY-PLAN.md. About 700 stories are processed into readable text; the Reading Room is reached from the
footer and the Supply Closet. It is not the source of course texts below the higher grades (docs/ECOSYSTEM.md, Cory
2026-11-12). Nothing holds it by rule, and nothing has run since 2026-11-10. Next, in order:

1. **Pilot:** ten stories in the 3 to 5 band end to end, after the format gains a text record and topics.
2. **Enrich and verify** in waves of about 50, with topic sets.
3. **K-2 read-aloud** as the voice bank allows.
4. Later: the Excerpts shelf and the Speeches and Documents collection.

## Track 4: The site

Detail: docs/SITE.md and docs/SITE-DESIGN.md. Not launched. Course and unit pages for all 52 core courses are built
but hidden (scripts/course_pages.py, `SHOWN = False`). Day pages will be one source file per day, published as one
page per section (settled 2026-11-15). Pictures live in the R2 bucket; run scripts/sync_media.py before each deploy.

- **Waits on:** finished courses, for the course pages to show.
- **Any time:** the www.curioclass.org redirect, dark mode, a request page for teachers.
- **Before launch:** the credits line wording (later.csv L21), the Front Office banner when Cory raises it (L70); a
  year-at-a-glance page per grade is to be decided after the days are written (L18).

## Track 5: Outreach and funding

Detail: docs/funding/ (one-pager, cost sheet, prospect list, CONTACTS.md).

1. **Funding:** a first philanthropic grant of about $10,000. Emails go out from Cory. Before any letter uses the
   "first free, complete K-12 curriculum" claim: later.csv L16.
2. **Donation page, later:** a catalog of buttons, coffee $7.25 to international development and outreach $15,000;
   the top tiers are "get in touch". The page says plainly whether gifts are tax-deductible.
3. **Reach without tracking:** server-side request counts and teacher stories by email. Never student analytics.
4. **Teacher channels** (OER Commons, state OER repositories, Merlot, teacher groups) and any wide announcement wait
   for the launch.

## Track 6: Going public

The repo (LochLogic/curioclass) has been public since 2026-10-28. The site is not launched or announced; outreach is
Track 5.

## Track 7: Curriculum

The course work above. The rungs, each grown from the one before:

1. **Scope and sequence:** done for the 52 core courses (layer 5).
2. **Sections and days:** COURSE-RUN stages 5 and 6, written to the lesson-day template (docs/courses/LESSON-DAY.md).
3. **Tracks:** sections in a year's order with pacing for each subject and grade (the public name is workshopped
   when it ships, keeping "Curio Class" whole). Waits on several finished courses.
4. **The Binder:** a course exported as a link, a zip or an LMS course cartridge, content only; nothing in it sends
   rosters, sign-ons or grades anywhere. Waits on several finished courses.

Later: score codes (a code and QR a student shows the teacher; never called proof or cryptographic) and the state
standards crosswalk (one state outside the Common Core first, CASE as the file format; docs/ADOPTION-BAR.md; item 13
above).

## Track 8: Beyond School (new 2026-11-03, late)

Topics past K-12: ACT/SAT-style practice first, then one trade (electrical, plumbing or automotive), then
certification prep such as security fundamentals. Titles never use trademarks or branded material; bar exam prep
comes last and needs expert review.

## Track 9: Recess and Curiosities

- **Recess** (docs/GAMES.md): outside the bar, it claims no standard. Seven games are live; which ones is GAMES.md,
  "On the shelf now". Cargo Hold is spec only. Games run in their own small waves beside the course work and go live
  one at a time as each passes Sign-off.
- **Curiosities** (docs/CURIOSITIES.md, locked 2026-11-04): wait with tool building, since they use the same
  pipeline. The entrance comes after all are built; the Art Studio idea is parked (later.csv L11).

## Track 10: Languages

World languages are shelved: the progression is Spanish only (2026-11-22), and ASL waits on later.csv L93. A later
Languages section grows in wings (Cory, 2026-11-07):

1. **Native languages of this land (first wing, partner-led).** An archive that grows into a mid-level learning tool
   (a sound-and-word library, phrase sets, practice games, teacher and family pages), toward a course only if the
   partner community wants one. Hand talk (Plains Indian Sign Language) belongs here, shown by real signers. One
   language and one community at a time; the community decides what is public and owns its material; nothing is
   gathered from archives without permission, and nothing is written or filled in by AI. Starts only when a partner
   says yes.
2. **Later wings:** Latin-alphabet languages, then Cyrillic-script languages, on the same engines.

Needs more thought before anything is built: how the section relates to the world languages topics, what
"mid-level" means in lessons, and which engines are shared across wings.

## Late and far back

- **Classroom projects by standard** (future input): docs/agents/roadmap/CLASSROOM-PROJECTS.md.
- **Class Cast** (parked 2026-11-03): live class sync through a relay. Only with funding and someone to keep a server
  running.
- **Read-aloud for grades 3 to 12** in the Reading Room (end of the roadmap).
- **Instrument learning paths** (parked 2026-10-25): one tool per instrument on a shared engine, recorder first.
- The Worksheet Generator is no longer late: live since 2026-11-03, the first path for procedural practice
  (docs/SUPPLY-CLOSET-PLAN.md).

## Thin areas after the worksheet trim (2026-11-04, deal with later)

Cory approved the trim as proposed and set these aside for later. Each is a list to look at again, not a decision.

- **ELA, one-sheet topics:** 97 ELA topics (spread across K-8, 6 to 13 a grade; only one in grades 9-12) now have a single sheet, because ELA
  classes have many small topics. The checker floor dropped from 2 sheets a topic to 1 so the trim could land
  (`MIN_PER_MODULE` in scripts/check_worksheets.py). Choose: give those topics a second sheet back (about 97 rows,
  from the cut lists in docs/agents/trim/ela.csv), or accept one and set the floor back to 2 elsewhere.
- **Read and respond cuts:** the reading sheets took heavy cuts outside ELA: health 39, dance 22, science 20,
  computer science 18, media arts 18, world languages 16. Check that each class still has some reading in it.
- **Source analysis cuts:** 12 in social studies (plus a few elsewhere), though no class lost its only one.
- **ASL culture readings:** 33 ASL rows cut, some of them Deaf culture readings. Review with the ASL work (sign-strip
  sample) before those classes are built.
- The cut rows stay in docs/agents/trim/<subject>.csv (title, type, module, reason) for any of these to come back.
