# Consolidation plan: one flat product, then an architecture that scales

Status: draft 3, 2026-11-24, for Cory. Not approved; nothing in it has been done. Draft 1 was reviewed against the
repository by a fresh Fable agent the same day; its 16 findings are folded in (the review's evidence is summarized
where a finding changed the plan). Draft 3 takes Cory's comments of 2026-11-24: nothing old is left standing beside
the new model ("live things" now migrate, step 4.1), earlier decisions that change are listed (step 4.0), this
consolidation is the mass edit (the change workflow moves in, step 4.4), and his six decisions are recorded at the end. Built on a read-only census of 2026-11-24: every sibling folder, the Codex and
Antigravity homes on C:, the tool pipeline and the curriculum layers.

Draft 4, 2026-11-25: steps 0 to 3 are done (reports in docs/reviews/consolidation/). Step 4 is rewritten after a
Fable read of it (docs/reviews/consolidation/step4-fable-read.md), and the end goal is defined as tests
("The end goal" below). Same day: linked words added as 4.9 (architecture only) and the Word Wall conversion
as a later step of its own. Step 4 has not started.

## Why

Hundreds of sessions across Claude, Codex and Antigravity worked in several folders. Some work exists in only one copy
outside the repository, stale plans sit beside current ones, and changing one thing (a text, a standard, a routine)
means searching thousands of files. After the curriculum is written there will be tens of thousands of files. The aim:
one folder (S:\CurioClass), one home per fact, nothing lost, and an architecture that makes later edits cheap and safe.

## The end goal: a flat, efficient, well-organized curriculum database

Added 2026-11-25 (Cory: "identify how we meet our end goal"). The curriculum is already a database: CSV tables per
course, markdown records with frontmatter, ids in `[[...]]` links. It is not yet flat, efficient or well organized,
because facts have more than one home, relations can only be found by searching, and some lists are built from the
tool catalog. Each word of the goal is defined below as tests that can be run, so "done" is a reading, not a feeling.

### What each word means

**Flat** (one place, one shape, one home per fact):

1. One working folder, S:\CurioClass, one branch line. *Done in steps 0 to 3.*
2. Every course has the same three homes and nothing else: `data/plans/<course>/` for structured facts (CSV),
   `docs/courses/<course>/` for plan prose (frame, scope and sequence, unit and section plans), `courses/<course>/`
   for the days and their texts (`texts/`). Plus four shared homes: data/standards/, data/progressions/, data/plans/ledgers/, and
   data/plans/ for the cross-course tables (course list, frames, calendar, later, defects); the shared format docs
   in docs/courses/*.md (LESSON-DAY, UNIT-PLAN, CALENDAR) are templates, not course content. *Test:* a layout check
   lists any curriculum file outside these homes (built with the 4.11 linter).
3. One home per fact, written down. The fact map (below) names the owner of every kind of fact; anything else that
   holds it is either generated from the owner and marked so, or gone. *Test:* the 4.6 drift report and the 4.12
   list leave no fact with two hand-kept homes.
4. No curriculum list is built from the tool catalog. *Test:* the 4.11 linter's catalog check passes, and the course
   list, course pages and status page read curriculum sources only (4.4, 4.5).

**Efficient** (cheap to find, cheap to change, cheap to check):

5. Any object is found by id: `uses.py <id>` answers "what uses this?" in seconds, across all courses (4.7).
6. Any change runs as a script with a dry run and an impact list, never as hand edits across files (4.10).
7. One command per job, named in the doc map; mechanical rules are lint, not reader tokens (4.11).
8. Generated things are never edited by hand and never stored twice (4.12).

**Well organized** (every piece is accounted for and connected):

9. Every relation resolves: each `leans_on`, CSV id column and `[[...]]` link points at something that exists
   (the 4.7 resolve gate, failing).
10. Every object has one status, read from one source, visible in the index (4.7).
11. Every retired id is recorded and never reused (4.8).
12. Nothing is orphaned: no day without a days.csv row, no plan row without a frame unit, no skeleton left after
    its plan passes. *Test:* an orphan report from the index, added to the gates after its first clean run.

### The fact map (one owner per fact)

| Fact | Owner (hand-kept) | Generated from it |
|---|---|---|
| Which courses exist | data/plans/course-list.csv (4.4) | COURSES-STATUS.md, the Desk course list |
| A course's units and why | docs/courses/<course>/frame.md | frames.csv, calendar.csv (`frame.py sync`) |
| Standards and their codes | data/standards/ | index nodes; standards pages after the curriculum (4.5) |
| Skills and handoffs | data/progressions/ | index nodes and edges |
| Days, items, wrongs, parts, materials, sources | data/plans/<course>/*.csv | skeletons, `gen:` tables, index |
| A day's teaching | courses/<course>/<section>/dNNN.md | lesson pages, PDFs |
| What was taught when | data/plans/ledgers/ | coverage reads |
| Status of a day | its frontmatter `version:` | index, flow-status reads |
| Retired and merged ids | data/ids-retired.csv (4.8) | registry |
| Words: definitions and fun facts by grade band | data/plans/words.csv (4.9) | highlighted words on day pages; the Word Wall, after its conversion |
| Parked work | data/plans/later.csv | Desk Dashboard |
| What is in the live bucket | the two R2 manifests (sync_media.py) | none |

### How we get there

| Stage | Meets tests | When |
|---|---|---|
| Steps 0 to 3: one folder, rescue, Codex merge, cleanup | 1 | done 2026-11-25 |
| Step 4 (4.1 to 4.13) | 3 (drift report), 4, 5, 6, 7, 8, 9, 10, 11, and 2 and 12 as reports | next |
| Step 5: tool records only, plumbing standardized | keeps tools outside the curriculum homes | after step 4 |
| Step 6: close, counts in SCALE.md, the fact map in HANDOFF | the tests recorded as a baseline | after step 5 |
| Word Wall conversion ("The Word Wall, rebuilt from the curriculum" below): the old cards become rows of the word table, the Word Wall becomes a view over it, data/closet/words goes to the archive | one home for every definition | its own step after step 6, before writing resumes in earnest, with Cory lifting the never-touch rule on data/closet/words for that step only |
| As each course is written or next reviewed | 2 and 12 move from report to failing gate per course; old item suffixes stripped; skel drift fixed by the rule Cory picks | ongoing, by the course run |
| After the curriculum is done | the tool catalog retired; topic pages, coverage and standards pages become views over the index | later.csv |

The consolidation does not try to make every old file pass every test at once. It builds the tests and the tools,
makes the shared structure pass, and turns each per-course test from a report into a failing gate as that course
is written or reviewed, so new work can only land flat.

### The Word Wall, rebuilt from the curriculum (Cory, 2026-11-25)

Today the Word Wall's cards (data/closet/words, one file per subject) are keyed by tool topic, so its words come from
the tool catalog rather than from what the days teach: the same leak as the course list (4.4). Once 4.9 is in place a
Word Wall is built the other way round:

- **Words come from the days.** A word is on a grade's wall because a day teaches it: the `[[word:...]]` marks and the
  terms the ledgers already record as introduced.
- **One definition per word and grade band, with its source,** in the word table. A fix is made once and shows on the
  day page, the student sheet and the wall.
- **Walls by unit and by grade are queries** over the index, and each card can link back to the days that use it.
- **The backlog is a report:** "marked but undefined" (4.9) is exactly the list of cards still to write.

**The conversion,** its own step after step 6 and before writing resumes in earnest, so writers who mark a word often
find its definition waiting:

1. Cory lifts the never-touch rule on data/closet/words for this step only.
2. A script turns each old card into a row of the word table, with `from` naming its source file and topic, and
   assigns a grade band from the topic's grade. Cards it cannot place, and words that need a second definition for a
   younger or older band, go to a review list rather than being guessed.
3. The Word Wall pages are built from the table. The before and after pages are compared; any difference is listed
   and explained in the step report.
4. data/closet/words goes to the archive, with ids-retired.csv rows for any card id that changes.

### What is not part of the goal

- Moving to a real database server. Plain files in git stay the source: they diff, review and back up as they are,
  and the index is a generated view that can be loaded into SQLite whenever a query needs it.
- Opaque ids, a general batch-edit framework, interchange exporters, reading-level lint and sampled reads: each
  waits for its first real need (later.csv rows, step 4.13).

## Ground rules for every step

1. **Serial.** One step at a time, in the order below. Each step ends with a short report and Cory's go before the
   next starts.
2. **Nothing is deleted.** What leaves the repository goes to `S:\CurioClass-archive\<what>-<date>\` and gets a row in
   the archive index (`S:\CurioClass-archive\INDEX.csv`: archived_path, old_path, size, sha256 of each file or of a
   folder's file list, date, step, reason). A move is a copy, a hash check, then removal of the source. Paths that
   cannot be read (the Codex sandbox dependency folders return "Permission denied") are listed in the step report as
   skipped, with Cory's OK; they are rebuildable.
3. **Before and after.** Each step records the gates before it starts and runs them again after:
   `plan.py check` and `lesson_course.py` per course with plan data, `ledger.py check` per subject, `check_tools.py`,
   `check_safety.py` (the CI gate on push), `board.py`, `desk_stats.py`, `course_status.py`, and the site build.
   A step is done only when no new failure appears. Gate outputs go to `docs/reviews/consolidation/<step>/`. Some gates
   rewrite tracked files (course_status.py writes docs/COURSES-STATUS.md, board.py writes docs/BUILD-BOARD.md, the
   lesson build writes build/); those files are committed or restored before the step's own commit, so a step never
   ends with a dirty tree.
4. **Rollback.**
   - Inside git: each step is one commit or a short series. Before step 0 ends, main is tagged
     `pre-consolidation-2026-11` and the tag is pushed. The Codex merge lands as `git merge --no-ff`, so
     `git revert -m 1` undoes it. Archive tags (`archive/<branch>`) are pushed before any branch is removed.
   - Outside git (folder moves, worktree removal, scheduled task changes, `.git/info` edits): `git revert` does not undo
     these. Their rollback is the archive index row plus the hash-checked copy, and each step report lists them.
5. **Ignored files first.** Before any worktree or folder is removed: `git status --ignored`, and unique ignored
   material is copied out (lesson of 2026-11-09).
6. **Secrets stay put.** `Gemini/Api.txt` looks like a credential. It is not opened, moved or archived; Cory decides.
7. **Live things are migrated, never just moved.** These look old but the deploy, the gates or the pipeline read
   them: `data/units.csv` (plan.py), `data/modules.csv` (build_site.py and about 30 scripts; generated from
   data/modules/*.txt), `data/sequence.csv` (the site Map), `data/coverage.csv`, `data/tools-concepts.csv` (board.py,
   desk_stats.py) and `data/concepts/` (the catalog scripts), and the skeleton folders (read by the briefs). The
   math-4 pilot folders are not live plan ids but old work held blind until its reconcile (later.csv L13); they are
   never renamed. Step 4 changes each live thing the same way: the scripts that read it change first, the gates pass on
   the new source, and only then does the old file go to the archive (or, for generated files, is removed), so
   nothing old is left standing beside the new. The two R2 manifests (`data/media-manifest.txt`,
   `data/docs-manifest.txt`) are the exception: they are the record of what is in the live bucket, not a duplicate of
   anything, so they stay committed and are changed only by sync_media.py.

## The order

0 freeze and clean tree, 1 rescue, 2 the Codex merge, 3 clean up, 4 architecture, 5 tools, 6 close. The Codex merge
comes before the cleanup because the cleanup edits scripts and docs the draft branch also changed (scripts/codex_draft.py,
docs/courses), and every commit main gains first widens the merge.

## Step 0: freeze, snapshot, clean tree

1. **Nothing else runs.** turn.py status shows "Turn: free"; no Codex or Antigravity session is open.
2. **Scheduled tasks, both kinds, paused and listed** so they are switched back on at the end:
   - Windows Task Scheduler: CurioClass-CodexDraft, CurioClass-CodexRun-2, CurioClass-CodexRun-Once (all Ready),
     plus DriveBackup-Weekly, which is not paused.
   - Claude app scheduled tasks: curio-br2-resume, curio-habitat-hunt-voice, sara-spec-55 (checked in the app).
3. **Backup.** The X: backup holds S:\CurioClass, S:\CurioClass-draft, S:\CurioClass-codex, S:\CurioClass-agy and
   S:\CurioClass-gemini. If X: is short of space (it filled on 2026-09-24), first make a one-off copy of the unique
   pieces in step 1.
4. **Clean tree on main and every worktree.** Main shows 103 modified and about 2,546 untracked files today (101
   math-4 build files, docs-manifest.txt, COURSES-STATUS.md, build/lessons for 16 courses, 31 Codex review stubs,
   this plan). The draft worktree has 81 untracked build files and the agent worktree one build folder. Fourteen of
   main's untracked build files are files draft/codex adds, so the merge would stop on them. The build/ decision
   (Cory decision 1, taken: untrack it) lands here:
   - **Untrack build/.** The site never reads build/ (build_site.py, course_pages.py and sync_media.py
     ship dist/), only 548 build files are tracked on main, and AGENTS.md's "build/ is committed" is already untrue in
     practice. build/ goes into .gitignore on main and on draft/codex (one commit each, `git rm -r --cached build`),
     so the merge does not add 3,022 more.
   - docs-manifest.txt: whatever sync_media.py last wrote is the truth; commit it as it is.
   - COURSES-STATUS.md: regenerate and commit.
   - The 31 review stubs: untracked files, so archived as a file move, not a commit.
5. **Git settings into the repository.** The union merge rule lives in `.git/info/attributes`
   (`data/plans/*/*.csv merge=union`): unversioned, shared by every worktree, lost on a re-clone. It is removed (step 2
   relies on that). The lines in `.git/info/exclude` (drafts/, /_scratch/, /_queue.txt, _runner/, /_draft/,
   ANTIGRAVITY-PROMPTS.txt, FLASH-RESEARCH-PROMPT.txt) move into .gitignore so a clone behaves the same.
6. **Archive index created**, the census recorded as its first entries, the before-gates recorded, and main tagged and
   the tag pushed.

## Step 1: rescue what exists in only one place

Each item is copied into its home in the repository, checked (check_safety.py on every rescued tool), committed.
Sources stay until step 3 archives them.

| Item | From | To |
|---|---|---|
| Earthquake Table (Curiosities No. 14) | S:\CurioClass-agy\earthquake-table.html | tools/earthquake-table/source/, linked to docs/CURIOSITIES.md; stage set from what it is (a build, unchecked) |
| Tether Drift | S:\CurioClass-agy\tether-drift.html | a Recess game, not ready (Cory decision 2): tools/tether-drift/source/ with stage Build, not in data/recess.json and not on the site, a later.csv row "side project, finish when Recess work resumes" |
| Six Gemini sequence reads of 2026-11-24 | S:\CurioClass-gemini\reports\sequence-*-gemini-read.md | docs/reviews/ beside their gemini-fixes ledgers |
| Time Tides data pipeline | C:\Users\Cory\.gemini\antigravity\brain\6fbd6632...\ (assemble_atlas.py, build_data.py, build_bios.py, stories_data.py, raw_geojson, cliopatria zip, bios cache) | tools/time-tides/pipeline/ (scripts and small data in git; large raw data in pipeline/raw/, ignored like art/raw) |
| All raw art and voice | every tools/*/art/raw and tools/*/voice/raw in every worktree and S:\CurioClass-codex | hash-compared against main, folder by folder; anything missing or different is copied in. Known so far: chess, equation-balancer, globe-theatre-stage, star-life-story and thesis-workshop have no raw folder on main; mole-bakery has 14 raw files in codex and 6 on main |
| Class Phone Call build | agy/build branch | tools/class-phone-call/ (src.html, art, voice, reports), at the stage its reports support |
| docs/agents/AGY-BUILD.md | agy/build branch | archive (Antigravity's build brief; anything still a rule is already in docs/agents) |
| 45 Flash research packets | agy/build branch | archive (Cory decision 3, checked): all 45 are for social studies tools whose specs Sara already wrote from scratch (2026-11-10), half their quotes were not on the cited page and 95 of 265 links were dead, and docs/agents/SPEC.md already tells spec writers to research from scratch. No later use found. SPEC.md's packet line and RESEARCH-PACKET.md go to the archive with them |
| Main's own ignored work | _scratch/ (596 MB: goalmap, l87, ladder, ladder2, probe4, probe5, scifix, sara-check and more) and drafts/ (desk, paste-ready, private, gemini) | inventoried folder by folder; each goes to the repository, the archive, or stays, in a list Cory sees. Known: drafts/desk/desk.html and snap.json go to desk/ (the Desk page source, with a README on publishing it); _scratch/ladder/gen.py goes to scripts/ (HANDOFF names it) |
| Approach Principles PDF | S:\CurioClass-spec2\shots\ | docs/ beside APPROACH.md if it is that document's print, else archive |
| Codex generated images (5.6 GB, 2,651) | C:\Users\Cory\.codex\generated_images | archive only, with a map of image to tool where the Codex session logs show it; not in git |
| Codex skills (curio-class-build-only, -calibration-review, -cold-review) | C:\Users\Cory\.codex\memories\skills\ | archive |
| Codex _runner and _scopes logs (290 MB) | S:\CurioClass-codex\ | archive |
| Unmerged branch tips | claude/hopeful-dirac-qck82o (7 commits, worksheets wave 2), origin/audit/states, codex/biased-bot | diffed against main by content, not path; anything main lacks is listed for Cory before the branches are tagged in step 3 |

After: the site build, check_tools.py and board.py show the rescued tools; nothing else changes.

## Step 2: merge the Codex draft

draft/codex is 243 commits ahead of main; main was last merged into it at bd20bc418 (2026-11-24). The dry run with
`git merge-tree` reports **zero conflicts, and that is the danger**: with the union rule, data/plans/ledgers/math.csv
merges as a straight concatenation (main's 1,538 planned rows for 11 courses plus the draft's 4,093 written rows for
math-kindergarten, 5,631 lines), so math-kindergarten keeps 83 stale "planned" rows beside its "written" rows. A clean
merge is not taken as a correct one.

1. **List the surface.** `git diff --name-only` on both sides since the merge base, intersected. Today the
   intersection is data/plans/ela-texts.csv, ledgers/ela.csv and ledgers/math.csv; it is recomputed on the day.
2. **Union rule gone** (step 0.5) before any merge.
3. **Merge main into draft/codex** in S:\CurioClass-draft. Every file in the intersection that is a CSV is rebuilt by
   key with a script, not taken from git's result: rows matched by their key (ledger: course, where, kind, entry;
   ela-texts: text_id), main's rows for courses the draft did not touch, the draft's rows for its courses, planned rows
   promoted through `ledger.py` rather than concatenated. Assertions: one header, no duplicate keys, row counts equal to
   the per-key expectation.
4. **The same duplicate-key assertion** runs over every data/plans/*/*.csv the draft touched (61 files), since the
   union rule shaped all of them.
5. **Gates on the branch**, per course, compared with the baseline sheet
   (docs/reviews/codex-draft-baseline-2026-11-24.md). No new failures beyond the baseline.
6. **Draft status.** Every Codex day already carries `version: draft 1, not ready, not yet taught` in its frontmatter.
   The field the Desk, course_status.py and the gates read is named in the step report and confirmed to show these
   days as unread drafts, not finished days.
7. **Carry-overs.** The six carry-overs of the baseline sheet go to defects.csv; its review classes go to later.csv
   (L105 updated).
8. **Land on main** as `git merge --no-ff draft/codex`, every gate on main, push.
9. **Archive the draft folder.** `git status --ignored` in S:\CurioClass-draft: _draft (251 MB of logs and usage.csv)
   and _scratch (4.6 GB; the texts-out CSVs checked against main first) go to the archive. Then the worktree is removed
   and the branch tagged and pushed.

The review of the drafts stays paused, as Cory decided; this step only puts them in one place.

## Step 3: clean up

One commit each, in this order:

1. **Stale plan docs.** POLISH, PHASE0-PLAN, PHASE2-CONCEPTS, BREAK-BOX-PLAN, ART-STATUS and similar: anything still in
   force moves into the living doc that owns it, then the doc goes to the archive. HANDOFF.md gets one doc map saying
   which doc owns what. The two old stashes are exported as patches to the archive, then dropped.
2. **Paths to sibling folders.** board.py (`CODEX = ROOT.parent / 'CurioClass-codex'`), codex_queue.py,
   codex_runner.py, codex_scopes.py, codex_draft.py and the Start-*.bat launchers stop reading S:\CurioClass-codex,
   -draft and -spec2. Retired scripts go to the archive.
3. **Merged worktrees and branches.** S:\CurioClass-codex (codex/queue), S:\CurioClass-spec2 (spec/sara),
   S:\CurioClass-electives, the .claude/worktrees agent worktree (its one commit is superseded on main), and the old
   branches: tag (the origin tip where it differs from the local one, as for audit/states), push the tag, copy ignored
   files out, remove the worktree, archive the folder. The "never touch S:\CurioClass-spec2" line goes from AGENTS.md
   and from HANDOFF's folder table.
4. **Loose folders.** S:\CurioClass-agy, S:\CurioClass-gemini, S:\dq\library (a redundant copy, hash-checked first),
   empty temp folders (S:\tmp\ladder_u03, S:\ladder-tmp-x), C:\Users\Cory\.gemini\antigravity\scratch (farlight and
   resonance copies, diffed against tools/farlight and tools/ripple). S:\Notes is checked against main first.
5. **Stays where it is, on purpose.** S:\CurioClass-sources (reference texts kept outside the repository for rights),
   the apps' own data on C: (Codex sessions, Antigravity cache), Temp render outputs (rebuildable).
   S:\CurioClass-archive gets a README and the index; the 927,635-file old-worktree folder is zipped to one file.

## Step 4: architecture for scale

Revised 2026-11-25 after a cold Fable read of draft 3's step 4 against the repository
(docs/reviews/consolidation/step4-fable-read.md, 12 findings). The direction held: no curriculum gate reads the
tool catalog, the two leaks are real, and `leans_on` is already a clean edge list. Five claims were wrong about the
repository and are corrected below (the math-4 pilot is not an alias, day ids in frontmatter would not remove
position, build_db.py wipes its database, the course_pages cut would make dead links, frames.csv does not hold the
120 courses). The order is flipped: small cuts first, then the index, then the thin rules. Step 4 is about a third of
draft 3's size.

The curriculum will grow tenfold. Step 4 makes three things cheap: finding everything that uses a thing, changing it
everywhere by script, and knowing a change broke nothing. The models are the open courseware platforms (OpenStax,
Kolibri and Khan content trees: stable ids kept apart from position, generated outputs never edited by hand), the
documentation builds (Sphinx, Antora: links by id, the build fails on a broken one) and Wikidata (ids that carry no
meaning that can change, redirects on merge). DITA is the cautionary tale: over-reuse, and machinery built before its
first real use. Step 4 builds only what the curriculum already needs.

Every sub-step below is one commit (or one per course where noted), with the before and after gates of ground rule 3,
and its report says which gate exit codes are expected to change and why.

### 4.0 What changes, and what is kept

Kept as it is: day files as markdown with frontmatter, the CSV plan data per course (days, items, wrongs, parts,
materials, source-map, errors, sources), the progressions, the gate scripts, the ledgers as the term record, the kit
for tool plumbing, `course + day` as the day key, `[[...]]` as the house link syntax.

| Today | Problem | Becomes (sub-step) |
|---|---|---|
| The consolidation gates skip unitplan.py, frame.py check, sequence.py, check_site.py, the `--courses` build and the skeleton self-tests | Step 4 changes exactly what those cover | added to the gate runner first (4.1) |
| The turn.py queue is 33 math-4 pilot jobs, 5 shown as ready | A worker who asks for a job gets a pilot job with pilot day ranges | queue emptied, jobs archived (4.2) |
| math-4 (pilot) beside math-grade-4; ela-6 leftovers | Not two names for one course: math-4 is an older design kept blind on purpose until the reconcile (later.csv L13); ela-6 is one rights file and a spine | held apart, named in the doc map; no rename, ever (4.2) |
| data/units.csv (59 rows, math-4 pilot only) read by plan.py | Every other course fails it: 479 ignored failure lines in 21 courses | deleted, plan.py takes its horizon from frames.csv (4.3) |
| The 120 courses exist only as the output of course_status.py placing tool modules | The course list is built from the tool catalog | `data/plans/course-list.csv`, 120 rows, owned by hand; course_status.py builds from it (4.4) |
| course_pages.py links a standard only if a tool module lists it | The link set is really "standards pages that exist", and those are built from modules | build_site.py hands course_pages the set it renders (4.5) |
| section-skeletons/ and day-skeletons/ kept after the real plan or day is written (2,763 tracked files) | A second file per section or day; rebuildable by one command | classed as generated working files, `git rm` once their plan or day passes (4.6) |
| `<!-- skel -->` blocks in 917 written plans: CSV data frozen at writing time | A second home no gate compares | a report-only drift check; the fix is decided after the count (4.6) |
| No way to ask "what uses this?" | Every change means searching thousands of files | the index and `uses.py`, report only, then a resolve gate (4.7) |
| No record of retired or merged ids | An alias is lost the first time a file moves | `data/ids-retired.csv`, append-only, and a generated registry (4.8) |
| Version-suffixed item ids (636 of 14,587, three spellings) | Ids change when an item is revised | a rule and a check on new ids; old ones stripped as each course is next reviewed (4.8) |
| No home for word definitions in the curriculum; the Word Wall's cards (data/closet/words) are keyed by tool topic | Highlighted words and definitions would have no owner, or a second one | a word node type, one owner table, and `[[word:...]]` links that are safe before any definition exists (4.9) |
| Mass edits done by hand or by one-off scripts | No dry run, no impact list | one page of change workflow (4.10) |
| House rules restated across AGENTS.md, briefs and lenses | Readers spend tokens on what a script can catch | a four-check linter (4.11) |
| Generated files committed beside sources with no marking | Hand edits land in generated files | one source and generated list (4.12) |

### 4.1 Widen the gates

scripts/consolidation_gates.py adds `unitplan.py check`, `frame.py check`, `sequence.py`, `check_site.py`, the
skeleton scripts' `--self-test`, and `build_site.py --courses` into a scratch output folder (a flag is added if the
build has none) followed by a link check over the course pages. A new baseline is recorded (`step4-before`) before
4.2 starts, and main is tagged `pre-step4` and the tag pushed, as step 0 tagged the start.

### 4.2 Empty the pilot queue; hold the pilot apart

- The 33 rows of data/pipeline/jobs.csv go to the archive (`pilot-queue-2026-11-25`); the queue is empty and honest.
- The math-4 folders (data/plans/math-4/, docs/courses/math-4/) stay where they are, named in the HANDOFF doc map as
  "pilot, kept blind, reconciled under later.csv L13". Cory may instead send them whole to the archive; the reconcile
  then reads them from there.
- docs/courses/ela-6/RIGHTS.md and the ela-6 spine files go to the archive (L14 says none of their texts fits a frame
  unit).
- The pilot's special cases (plan.py, unitplan.py, section_cuts.py, defaults.py, frame.py LEGACY) stay until math
  grade 4 is reconciled and go in that commit. No string rename of `math-4`: it is also the prefix of 13 tool module
  ids, some in never-touch files.

### 4.3 Retire data/units.csv

plan.py drops the section-row check and takes the hand-back horizon from the course's `days` in frames.csv;
lesson_course.py drops the ignore rule that existed for it; coverage_ledger.py's guarded read goes; the file goes to
the archive. Expected: about 479 failure lines disappear and several `plan-<course>` gates change exit code from 1
to 0. The `modules` column (pilot sections to tool modules) is tool-side and is not carried over.

### 4.4 The course list as data

- `data/plans/course-list.csv`: one row per course as a school would schedule it (id, title, subject, grade or band,
  core, catalog_id pointing at data/courses.csv, status active or shelved), 120 rows, generated once from today's
  course_status.py output, then owned by hand.
- course_status.py builds its list from it and attaches module and tool counts as attributes only; the placement
  rules hard-coded in it (BY_GRADE, PER_GRADE, SPLIT, ONE_ROW) and frame.py's COURSE_META read the list.
- Test: docs/COURSES-STATUS.md before and after is identical apart from the date line; plan_flow.py and the Desk
  show the same courses.

### 4.5 Cut the course_pages leak

build_site.py passes course_pages.py the set of standards pages it actually renders, so the dependency is "pages
built", not modules.csv by name. Checked by the `--courses` build and link check of 4.1. The real curriculum-first
fix, a standards page for every code a course frame owns, is the site work that follows the finished curriculum
(later.csv row, with the topic pages as views).

### 4.6 Skeletons are generated

The skeleton folders are listed as generated (4.12). When a section or day passes its gate its skeleton is removed
with `git rm` (no archive row: git history keeps it and the script rebuilds it). coursegen.py's folder test changes
at most one line; the briefs keep working because each job regenerates what it needs. For the `<!-- skel -->` blocks
in written plans: a report-only check re-renders them from the CSVs and lists drift; Cory decides the fix from the
count. No plans are regenerated in step 4.

### 4.7 The "what uses this?" index

- `scripts/index.py` writes its own generated, git-ignored files, `data/index/nodes.csv` and `edges.csv` (plain CSV
  so they diff and need no database), from curriculum sources only: standards, progressions, frames, the course list,
  each course's plan CSVs, the day frontmatter (`leans_on:`, `version:`), the ledgers and `[[...]]` links.
  build_db.py is not used: it deletes its database and rewrites modules.csv on every run, and it is tool-side.
- Node key: type plus course plus local id (`item:english-language-arts-grade-1:s01-X2`), since bare item ids repeat
  across courses (1,648 of them). Day nodes are `day:<course>:d042`, derived, not minted.
- Each node carries its status as read from its one source (frontmatter `version:` for days, flow-status.csv for
  plans, the stage CSV for tools), so "where is this?" has one answer without moving any status field now.
- `scripts/uses.py <id>` lists everything that uses an object, by course and day; `uses.py --changed` lists what
  depends on the files changed since the last commit.
- Report only at first; it writes nothing tracked. After one clean run, "every `leans_on` path and every CSV id
  resolves" becomes a failing gate, with "when it exists:" as the one allowed unresolved form (38 today).

### 4.8 Ids: retired list, registry, item versions

- `data/ids-retired.csv`: committed, append-only, columns old_id, new_id (blank when retired), date, reason. Every
  archive move or merge of a curriculum object adds a row. An id is never reused.
- The registry is generated, not committed: the index's nodes plus that file, so aliases survive any rebuild.
- Item versions: data/plans/README.md gets the rule "a revised item keeps its id; the version goes in the `version`
  column", and plan.py fails a new id ending in a version suffix unless it is on a baseline list of today's 636.
  Old suffixes are stripped when each course is next reviewed, recorded in ids-retired.csv.
- No opaque day ids now. `course + day` stays the key. When the first real insertion of a day is needed, a scripted
  `renumber` (dry run first) rewrites days.csv, the day-keyed CSVs, the ledgers, the file names and `leans_on`
  together, through the 4.10 workflow. Opaque ids, if ever wanted, live in a days.csv column, as a separate step.

### 4.9 Words: the architecture for linked words, not the links

Cory, 2026-11-25: build the architecture for highlighted words with definitions and fun facts; write no individual
links or definitions in step 4.

- **The owner:** `data/plans/words.csv` (working name until the naming card below is answered), committed, created
  with its columns and no rows: word, grade band, definition, fun fact, source of the fun fact (a claim-level source,
  Cory decision 5), status, and a `from` column for where a row was converted from (used by the Word Wall
  conversion). Key: word plus grade band, so kindergarten "energy" and grade 8 "energy" are two rows.
- **The link:** lesson.py learns `[[word:<word>]]` in the same commit, as it knows `[[fig:]]` and `[[note:]]`. A word
  with no row for the day's grade band renders as plain text, so a mark can never break a page and words can be marked
  before any definition exists.
- **The index:** word nodes and "day uses word" edges (4.7). Two reports, never failing gates: marked but undefined
  (the definition backlog) and defined but never used.
- **The rules:** one paragraph in docs/CHANGES.md and in the writing briefs on how to mark a word (mark it by hand
  where it is taught; no automatic highlighting, since words with two meanings, such as table and cell, would be
  marked wrong).
- **Waiting on design, not built here** (later.csv rows): how a marked word prints (a popup does not print; for
  example a small "words today" box on the student sheet), the popup's keyboard, screen reader and phone behavior, and
  who writes definitions (reading level per grade band, a fresh-agent sensitivity read of fun facts).
- **Naming:** the feature, the file and the link prefix get locked names in docs/GLOSSARY.md before the commit; one
  Desk question card with a pick, q-word-names-1 (word, term, vocabulary and Word Wall are all in use somewhere
  today).
- **The Word Wall** (/closet/word-wall/, source data/closet/words, never touched) stays frozen with the tool catalog.
  Its cards are converted into the owner table in a later step of its own (the end goal's "How we get there"), after
  which the Word Wall is a view over the table.

### 4.10 The change workflow (one page)

docs/CHANGES.md: request (a step of this plan, later.csv or the Desk), impact list (`uses.py`), a script with
`--dry-run` that prints a diff summary, the gates, one log line. No framework code beyond what each migration needs.
Errata with course versions waits for a course that is taught (ROADMAP finished-course item 11).

### 4.11 The linter (four checks)

`scripts/lint.py`: no em dashes, "Curio Class" in full, a US spelling word list, and no curriculum script opening a
tool catalog file. It runs on changed files in `turn.py end` and on everything in the consolidation gate. Reading
level, banned phrases, sampled reads and interchange field choices go to later.csv rows.

Sources as we go (Cory decision 5) stays a writing rule, not lint: every text, day and tool names its sources at the
level of the piece, and checkable specifics (numbers, dates, names, scientific and historical facts in informational
texts and in tools) carry a claim-level source. Applied when a file is next written or touched, not as a pass over old
files.

### 4.12 Source and generated

- **Source:** markdown, CSV, scripts, art and voice.
- **Generated, not committed:** build/, dist/, tool bundles, data/index/, the registry, data/curioclass.db, any plan
  table generated from CSV, skeletons once their plan or day passes.
- **Generated and committed, gated by their own check:** frames.csv and calendar.csv (`frame.py sync`, `frame.py
  check`), modules.csv (from data/modules/*.txt by build_db.py).
- **Generated and committed for reading on GitHub:** docs/COURSES-STATUS.md and docs/BUILD-BOARD.md, regenerated by
  the lead at session end or by `turn.py end`; the date line is left out of any comparison and there is no failing
  gate (a curriculum job must not have to fix a tool stage).
- **State, changed only by its script:** the two R2 manifests (sync_media.py).
- **Frozen tool catalog,** read only by the tool side and the site's topic pages and Map: data/modules/ (source),
  modules.csv, tools-concepts.csv, sequence.csv, coverage.csv, data/concepts/, docs/agents/catalog/shape/.
- Large media stays out of git (art/raw, voice/raw, library art), backed up to X: and R2.

### 4.13 Order

4.1, 4.2, 4.3, 4.4, 4.5, 4.6 (the cuts, each small and fully covered by the gates), then 4.7 and 4.8 (built over
data that is no longer about to move), then 4.9 (words), then 4.10, 4.11 and 4.12. The deferred items get their later.csv rows in the
4.2 commit.

## Step 5: tools, plumbing standardized and play left free

Cory's rule: the back end and the curriculum are optimized for efficiency; what a child sees and plays is not
standardized into one design pattern. Large creative companies work this way: Pixar runs one pipeline under films that
look nothing alike, Nintendo shares engines under games that each feel different, LEGO standardizes only how bricks
connect, and Supercell gives small teams a shared platform and freedom over the game.

| Layer | Standardized? | What is in it |
|---|---|---|
| Plumbing (the kit) | Yes, as behavior | saving and resume, reduced motion, sound and speech, accessibility (keyboard, screen reader, contrast, 44 px targets), offline, the read-aloud engine, no tracking, a performance budget and a loading hook (the loading screen itself is the tool's) |
| Contract (tool.json and the record) | Yes, as data | id, grades, standards, skills, round length, declared modes, teacher notes and plan, pipeline stage, credits |
| Play (src.html, art, voice) | No, on purpose | the world, the mechanic, the look, the palette, the type, the layout, the menus, the sounds, the jokes, the win moments |
| Play rules Cory chose | Yes, as rules, not as code | say how to act (every waiting moment names the next action, spoken once, then a hint), the variety rule |

What changes now and what waits (curriculum first, Cory 2026-11-24): items 1 and 5 are record keeping and land in this
consolidation, so nothing about a tool gets lost; items 2 to 4 and 6 change tools themselves and wait until tool work
resumes after the curriculum, alongside reshaping the tools to it.


1. **The stage CSV first.** A new `data/tool-stages.csv` (tool id, stage, date, the record that proves it) becomes
   where board.py and desk_stats.py read the stage, instead of guessing from file names. data/tools.csv (2 rows, a
   different schema) is left alone or retired in the same commit, said explicitly. This comes before any folder is
   flattened, which removes the reason to flatten in a hurry.
2. **The kit contract becomes behavior, not layout.** Three controls with the ids motion, sound and read, reachable,
   44 px and labelled, plus the tool's modes declared in tool.json. audit_tool.py (which today finds modes through
   `header .seg button`, excludes controls by `el.closest('header')` and assumes the kit ids) and curio.js bind to the
   ids and the declared modes, not to the header element. These script changes land and pass on the three pilot tools
   first.
3. **Then the visible frame becomes optional (Cory decision 4, taken).** The header, the stage-plus-panel grid, `.panel`, `.hint` and
   `.big-btn` (curio.css, docs/KIT.md) become defaults a tool may restyle or drop, as long as the contract in 2 holds.
4. **A sameness check, the opposite of a design system.** At Refine, the tool is compared with the tools of its grade
   band on look, voice and world; too close fails. Mechanics are compared only within a family, since the family
   engines (number line, graphing and the rest) share a mechanic by design.
5. **Flatten the record, not the tool, and only after Spec.** idea.md and spec.md stay as they are (the build briefs
   and queues name spec.md). A tool past Spec gets one record, `tools/<id>/tool.md`, holding everything after Spec (build
   report, self-check, refine, fix, exit check, art and voice, finish check, sign-off) and a dated log, plus `checks/`
   for its super-check scripts. Earlier rounds (polish-1, refine-2026-10-28, codex-report-1) go to the archive. This
   applies to new work now and to a tool when it next moves, not as one rewrite: 564 tools are at Spec and are one or
   two files. Until the last tool is flattened, board.py and the gates support both shapes. Before any of this, one
   pass writes a per-tool index of where its scattered pieces are (in the repository and the archive), so nothing
   waits to be found.
6. **Pilots.** Cipher Vault (about 40 pieces in four places), Living Pond and one tool just past Spec go through 1 to 5
   by hand before the rule applies to new work.

## Step 6: close

Switch the scheduled tasks back on (only those Cory still wants), fill the after counts in docs/funding/SCALE.md, refresh the Desk, update HANDOFF.md, AGENTS.md and
the memory notes, and write a short record of what moved where (the archive index holds the detail).

## Decisions taken (Cory, 2026-11-24)

1. build/: untracked on main and on draft/codex before the merge (step 0.4).
2. Tether Drift: a Recess game, not ready; kept as a side project (step 1 table, later.csv row).
3. The 45 Flash research packets: checked, no later use; archived with SPEC.md's packet line and RESEARCH-PACKET.md.
4. The visible kit frame becomes optional (step 5.3) once the contract scripts pass.
5. Sources as we go, at the level of step 4.11: every piece names its sources, checkable specifics carry their own;
   not every statement.
6. Gemini/Api.txt stays where it is, untouched, for when tool work resumes.
7. The scale of the project is recorded for later marketing in docs/funding/SCALE.md: the before counts now, the
   after counts at step 6.
8. Curriculum first: the tools never shape the curriculum; they are reshaped to it once it is done (steps 4.4 and 4.5, step 5
   scope).
