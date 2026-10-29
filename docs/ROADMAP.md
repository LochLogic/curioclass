# Roadmap

The one plan for Curio Class: what is done, what comes next, and in what order. Consolidated 2026-10-28 from the
"Later phases" section of docs/PHASE0-PLAN.md, the Supply Closet roadmap, docs/agents/SCALE-PLAN.md,
docs/LIBRARY-PLAN.md, docs/SITE.md ("Not done yet") and docs/agents/roadmap/.

This file holds the order and the status. The design detail stays in each track's own plan, linked from its section.
When a roadmap item starts, finishes or moves, update it here first.

## Where it stands (2026-10-28)

| | Count |
|---|---|
| Tool concepts in the catalog | 797 |
| Live tools | 76 |
| Specs written | 198 more (of the 721 not yet built) |
| Modules with Word Wall cards | all, English and Spanish |
| Anchor charts / posters / Game Night games | 74 / 54 / 104 |
| Sub Day packets | 76 (one per live tool) |
| Reading Room stories curated and processed | about 700, not live yet |

`python scripts/board.py` gives the live tool counts (docs/BUILD-BOARD.md).

## Goal

Reach and craft together (Cory, 2026-10-28). As many teachers as possible should know Curio Class exists; nobody
needs to use a tool that does not fit their class, but every tool must be really good. Free for good: no paywall,
no accounts, no ads, no tracking.

## Track 1: Tools (the main work)

Detail: docs/BUILD-PLAN.md (the pipeline), docs/agents/SCALE-PLAN.md (the order), docs/agents/RUNBOOK.md (how a
session runs it), docs/agents/decisions/BASELINE.md (Cory's standing rules).

1. **Now:** the network-help-desk single-tool test with the Codex builder (docs/agents/BATCH-BR.md, "Resume here").
2. **Then spec waves** of about 30 to 50 tools, one subject or band at a time, each with its own overlap check.
3. **Art overnight per wave**, right after the spec check (docs/ART.md).
4. **Builds stream** in small mixed Build and Refine waves (docs/agents/REFINE.md), then build-only waves per family
   once its Refine counts fall. At most about 3 to 4 agents.
5. **Voice nights per refined group** on the Forge, the same nights as art.
6. **Reviews per wave** on the Review Desk. Cory reviews every K-2 and sensitive tool in full and spot-checks about
   one in four of the rest (10 to 20 hours a week available, Cory 2026-10-28).
7. **Each new tool also ships** its lesson plan, Sub Day exit file and (from Track 2, item 2) its module's anchor chart.

### Held-back collections (their own waves)

- **ASL:** graphics only, no video or photos (Cory, 2026-10-27). Design path in docs/agents/roadmap/ASL-SIGN-STRIP.md.
  Next step is the three-sign sample (THANK-YOU, NAME, WHERE) when Cory asks for it. No ASL tool is specced or built
  before that.
- **Spanish:** needs a native-speaker review.
- **Hard history:** extra care and teacher guidance; a fresh review agent clears it (BASELINE rule 5).
- **growing-up-q-a:** Cory reviews it personally before any live push (BASELINE).

### Queued tool ideas

"Fact-check a chatbot" (generative AI) and a resume builder (near term), from BASELINE rule 10. New ideas go into
data/concepts/*.txt for a later spec wave.

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
5. **The Map** (Phase F, last): regions, trails and a standards view. Research is done (docs/MAP-RESEARCH.md);
   drafting is next when its turn comes.

**Still owed, any time:** a real-printer test of every print format, the Spanish native review, family game
play-tests.

## Track 3: Reading Room

Detail: docs/LIBRARY-PLAN.md. About 700 stories are curated and processed into readable text. Next:

1. **Pilot:** ten stories in the 3-5 band end to end (format, reader, pipeline).
2. **Enrich and verify** in waves of about 50: word help, questions, teacher notes, then a cold verify agent.
3. **K-2 read-aloud** as the voice bank allows.
4. Later: the Excerpts shelf and the Speeches and Documents collection.

## Track 4: The site

Detail: docs/SITE.md. Open items: the www.curioclass.org redirect, dark mode, preview images for bench tools, and a
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

## Track 6: Going public

The repo (LochLogic/curioclass) goes public once development is much further along (Cory, 2026-10-28). Before that:
a clean README, the license files, and no private data in history.

## Late and far back

- **Worksheet Generator** (late, parked 2026-10-26): click-only practice sheets per module with checked answer keys.
  Design in docs/SUPPLY-CLOSET-PLAN.md. Comes after the closet shelves. Word check was its first slice.
- **Classroom projects by standard** (future input): an off-screen project per module from Cory's notes.
  docs/agents/roadmap/CLASSROOM-PROJECTS.md.
- **Read-aloud for grades 3-12** in the Reading Room (end of the roadmap).
- **Instrument learning paths** (far back, parked 2026-10-25): one tool per instrument with 10 to 12 levels on a shared
  engine (mic pitch detection, Web MIDI, Note Ninja staff). Recorder first, then keyboard, ukulele, guitar, voice;
  band instruments only partly (a browser can't see the player's hands or hear mouthpiece shape well enough to
  correct it). Own shelf under Arts and Music.
