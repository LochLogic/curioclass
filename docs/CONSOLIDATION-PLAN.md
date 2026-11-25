# Consolidation plan: one flat product, then an architecture that scales

Status: draft 6, 2026-11-25, for Cory. Steps 0 to 3 are done (reports in docs/reviews/consolidation/). Step 4: 4.A
to 4.E are built and pushed (Cory's block-one go, 2026-11-25); work is paused at tag `pause-4e` for Cory's read of
draft 6, and 4.E2 waits for his go. History: draft 1 (2026-11-24) was read by a fresh Fable
agent and its 16 findings folded into draft 3 with Cory's comments and six decisions; draft 4 rewrote step 4 after a
second Fable read (step4-fable-read.md), defined the end goal as tests and added the words architecture; draft 5 folds
in the full Fable review of step 4 (step4-full-review.md: 18 findings, 10 rule changes), Cory decision 9; draft 6
folds in the pause-4e review (pause-4e-review.md: 18 findings, 2 blockers) and Cory's skel choice, decision 10.

## Why

Hundreds of sessions across Claude, Codex and Antigravity worked in several folders. Some work exists in only one copy
outside the repository, stale plans sit beside current ones, and changing one thing (a text, a standard, a routine)
means searching thousands of files. After the curriculum is written there will be tens of thousands of files. The aim:
one folder (S:\CurioClass), one home per fact, nothing lost, and an architecture that makes later edits cheap and safe.

## The end goal: a flat, efficient, well-organized curriculum database

Cory, 2026-11-25: "identify how we meet our end goal". The curriculum is already a database: CSV tables per course,
markdown records with frontmatter, ids in `[[...]]` links. It is not yet flat, efficient or well organized, because
facts have more than one home, relations can only be found by searching, some lists are built from the tool catalog,
and checks run over everything every time. Each word of the goal is defined below as tests that print a number, so
"done" is a reading, not a feeling.

**The design stays files in git** (second Fable review, 2026-11-25, which weighed a database as the source, one file
per object, and frontmatter as the only source, and rejected each for this project): CSV and markdown are the only
source, because diffs, GitHub reading and git review are the only review there is, agents work with file tools, and
the host is free and static. A generated SQLite index (ignored, rebuilt in seconds) answers the questions files
cannot. Agents write CSV rows through one safe command, not by hand.

### What each word means

**Flat** (one place, one shape, one home per fact):

1. One working folder, S:\CurioClass, one branch line. *Done in steps 0 to 3.*
2. Every course has the same homes and nothing else: `data/plans/<course>/` for structured facts (CSV, including its
   own ledger after 4.D), `docs/courses/<course>/` for plan prose (frame, scope and sequence, unit and section plans,
   the course's reviews after 4.H), `courses/<course>/` for the days, their pieces and their texts. Shared homes:
   data/standards/, data/progressions/, data/plans/ for the few cross-course tables, the shared format docs in
   docs/courses/*.md. *Test:* the index's `layout` report against data/homes.csv (4.F, 4.H).
3. One home per fact. data/homes.csv (4.H) names the owner of every kind of fact; anything else that holds it is
   generated from the owner and marked so, or gone. *Test:* the `drift` report (skel blocks) and the homes check
   leave no fact with two hand-kept homes.
4. No curriculum list is built from the tool catalog. *Test:* the catalog lint (4.G) passes, with one named exception
   until the standards pages are rebuilt (course_pages.py `known_standards`, later.csv).

**Efficient** (cheap to find, cheap to change, cheap to check):

5. Any object is found by id, and `uses.py <id>` answers "what uses this?" in seconds across all courses, including
   soft mentions in prose (4.F).
6. Any change runs as a script with a dry run and an impact list (docs/CHANGES.md, 4.H), and CSV rows are written
   through `rows.py upsert`, never by hand (4.D).
7. One gate command, `gate.py`, scoped to what changed: `--course`, `--changed`, `--all` (4.G). Mechanical rules are
   lint, not reader tokens.
8. Generated things are never edited by hand and never stored twice. *Test:* the generated-file guard in lint, read
   from data/homes.csv (4.G, 4.H).

**Well organized** (every piece is accounted for and connected):

9. Every relation resolves: each `leans_on`, CSV id column and `[[...]]` link points at something that exists.
   *Test:* the `resolve` report, failing on anything not in its baseline file (4.F).
10. Every object has one status, read from one source. *Test:* the `status` report (4.F); the file's own state wins,
    flow-status.csv keeps only what no file can show.
11. Every retired id is recorded and never reused (data/ids-retired.csv, 4.H), and a day number is permanent once its
    course's scope and sequence is signed off.
12. Nothing is orphaned: no day without a days.csv row, no piece no day leans on, no plan row without a frame unit.
    *Test:* the `orphans` report (4.F).

`gate.py` writes each test's count to `data/plans/goal-tests.csv` (test, count, date), which SCALE.md and the Desk
read (4.J, step 6).

### The fact map (one owner per fact)

The human-readable copy; data/homes.csv (4.H) is the machine-readable owner that lint and the scripts read, and
HANDOFF links to it rather than copying it.

| Fact | Owner (hand-kept) | Generated from it |
|---|---|---|
| Which courses exist: id (the frame slug), title, subject, grade or band, core, catalog id, term, status | data/plans/course-list.csv (4.C) | COURSES-STATUS.md, the Desk course list, frames.csv (join) |
| A course's units, days, minutes and why | docs/courses/<course>/frame.md | frames.csv and calendar.csv (a join with the course list, `frame.py sync`, gated by `frame.py check`) |
| Standards and their codes | data/standards/ | index nodes; standards pages after the curriculum (later.csv) |
| Skills, handoffs, and the words planned per skill | data/progressions/ (`words` column) | index nodes and edges |
| Days, items, wrongs, parts, materials, sources | data/plans/<course>/*.csv | skeletons (ignored), `gen:` tables, index |
| A day's teaching | courses/<course>/<section>/dNNN.md | lesson pages, PDFs |
| Pieces a day hands out or reads from (openers, exit cards, keys, family notes, practice sheets) | courses/<course>/<section>/<name>.md, reached through `leans_on` | lesson pages, PDFs |
| What was taught when, including each word a day introduces and its meaning as taught | data/plans/<course>/ledger.csv (4.D) | coverage reads, "day uses word" edges, the "words today" box |
| A word's student-facing definition and fun fact, by sense and grade band | the word table (4.I; name from Desk q-word-names-1) | highlighted words, the "words today" box, later the Word Wall |
| What a course asks tools for | docs/courses/<course>/TOOL-ASKS.md | index edges to tools (step 5) |
| Status of a day or plan | the file's own state (frontmatter `version:`, ledger `stage`) | index `status` report; flow-status.csv only for what no file shows |
| Retired and merged ids | data/ids-retired.csv (4.H) | registry |
| Where every kind of file lives and who writes it | data/homes.csv (4.H) | lint, turn.py and kit lists, HANDOFF link |
| Grade bands and subject ids | data/bands.csv and one shared module (4.H) | every script that needs a band |
| Parked work | data/plans/later.csv | Desk Dashboard |
| What is in the live bucket | the two R2 manifests (sync_media.py) | none |

### How we get there

| Stage | Meets tests | When |
|---|---|---|
| Steps 0 to 3: one folder, rescue, Codex merge, cleanup | 1 | done 2026-11-25 |
| Step 4, block one (4.A to 4.G) | 4, 5, 6, 7, 9 and 12 as reports, 10 | done 2026-11-25; curriculum writing may restart |
| Step 4, block two (4.H to 4.J) | 2, 3, 8, 11; all 12 printed as numbers | after block one; touches no course data |
| Step 5: tool records only; tools join the index | keeps tools outside the curriculum homes | after step 4, may run beside course work |
| Step 6: close, counts in SCALE.md from goal-tests.csv | the tests recorded as a baseline | after step 5 |
| As each course is written or next reviewed | each report becomes a failing gate for that course; old item suffixes stripped; resolve baseline worked off | ongoing, by the course run |
| After the curriculum is done: the tool reshaping stage | the tool catalog retired; topic pages, coverage, standards pages and the Word Wall become views over the index | later.csv |

The consolidation does not make every old file pass every test at once. It builds the tests and the tools, makes the
shared structure pass, and turns each per-course report into a failing gate as that course is written or reviewed,
so new work can only land flat.

### Words: from the days, not from the tool catalog (Cory, 2026-11-25; revised after the second Fable review)

The curriculum already keeps vocabulary in four places: ledger `term` rows (13,484, each with its course, day and
meaning as taught), the progressions' `words` column (per skill), wordlist.csv in six ELA courses, and the Word
Wall's cards (data/closet/words, 4,413 cards keyed by tool topic). The chain is stated once:

- **Planned** by skill in the progressions, **introduced** on a day in the ledger (the record of which day teaches
  which word, with the teacher-facing meaning), **defined** for students in the word table, by sense and grade band.
- **"Day uses word" comes from the ledger,** so the backlog ("introduced in the ledger but undefined") exists today
  with no marks at all. A `[[word:<sense>|shown form]]` mark only places the highlight in the text, and lint checks
  that a marked word has a ledger term row in that course. No marking pass over old days.
- **Print first.** Days are print pages: a "words today" box on the student sheet is drawn from the day's ledger
  terms and the word table. The popup (keyboard, screen reader, phone) is designed later.
- **The key is a sense id plus band,** because one word can mean two things in one band (432 of today's Word Wall
  word-and-band pairs have differing definitions; `family` in arts and in social studies). Bands come from
  data/bands.csv.

**The Word Wall** is a live tool-side product (pictures, Spanish, examples, five consumers: topic word pages, the wall
pages, the topic hub, Sub Day packets, the worksheet word bank). It stays frozen with the tool catalog, and
data/closet/words keeps its never-touch rule whole:

1. **Now (4.I):** a one-time read-only import copies each card's word and definition into the word table as candidate
   rows (status "from the Word Wall, unread", `from` naming file and topic). Collisions and span-grade topics go to a
   review list, never guessed. Writers then often find a definition waiting.
2. **At the tool reshaping stage,** with the topic pages: the Word Wall becomes a view over the word table. Pictures,
   examples and Spanish move as their own tables keyed by sense id, the art's R2 keys move through sync_media.py,
   and walls for subjects with no days yet keep their cards until those subjects are written.

### What is not part of the goal

- A database as the source, or a server. The index is a generated view.
- Opaque day ids or a renumber script (a day number is permanent after scope sign-off), a general batch-edit
  framework, interchange exporters, reading-level lint, sampled reads, the word popup: each waits for its first real
  need (later.csv rows added in 4.A).

## Ground rules for every step

1. **Serial.** One step at a time, in the order below. Each step ends with a short report and Cory's go before the
   next starts. Inside step 4, one go covers block one (4.A to 4.G), with stops only where a count decides a choice
   (the skel drift report, the words Desk card); block two (4.H to 4.J) gets its own go.
2. **Nothing is lost.** For tracked files, git history and the step's tag are the archive: they leave with `git rm`
   and the commit names them. Untracked files that leave the repository go to `S:\CurioClass-archive\<what>-<date>\`
   and get a row in the archive index (`S:\CurioClass-archive\INDEX.csv`: archived_path, old_path, size, sha256 of
   each file or of a folder's file list, date, step, reason); a move is a copy, a hash check, then removal of the
   source. Paths that cannot be read are listed in the step report as skipped, with Cory's OK.
3. **Before and after, scoped.** Each step and each step 4 sub-step records the gates and runs them again after; a
   step is done only when no new failure appears. One full run (`gate.py --all` plus the site built into a scratch
   folder with the deploy flags) at the start and end of step 4 and after any data move (4.C, 4.D, 4.E); between,
   each sub-step runs the scope it touches, and its "after" is the next one's "before". Only summary.csv and the
   compare are committed; raw dumps stay in an ignored folder. Gates that rewrite tracked files (COURSES-STATUS.md,
   BUILD-BOARD.md) are committed or restored before the step's own commit, so a step never ends with a dirty tree.
   Since 4.G the runner is `scripts/gate.py --all --site --save <step>` (consolidation_gates.py wraps it); a full run takes about 5 minutes.
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
   desk_stats.py) and `data/concepts/` (the catalog scripts). The skeleton folders are not live data: they become
   ignored working files a job regenerates (4.E). The
   math-4 pilot folders are not live plan ids but old work held blind until its reconcile (later.csv L13); they are
   never renamed. Step 4 changes each live thing the same way: the scripts that read it change first, the gates pass on
   the new source, and only then does the old file go to the archive (or, for generated files, is removed), so
   nothing old is left standing beside the new. The frozen tool catalog includes the Word Wall, the worksheets and
   the topic pages: none of it changes in step 4. The two R2 manifests (`data/media-manifest.txt`,
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

Draft 5, 2026-11-25. Rewritten twice from cold Fable reads of the repository: docs/reviews/consolidation/
step4-fable-read.md (12 findings, folded into draft 4) and step4-full-review.md (18 findings and 10 rule changes,
all folded in here by Cory's decision 9). The second read judged the design the right one and found four weaknesses
in draft 4: the words design missed the vocabulary the curriculum already keeps, nothing made checks cheaper, several
second homes and unowned piles were missed (the shared ledgers, course identity, day numbers in prose, docs/reviews,
pieces), and four of the 12 tests had no builder.

Step 4 makes three things cheap: finding everything that uses a thing, changing it everywhere by script, and knowing
a change broke nothing. The models are the open courseware platforms (OpenStax, Kolibri and Khan content trees:
stable ids kept apart from position, generated outputs never edited by hand), the documentation builds (Sphinx,
Antora: links by id, the build fails on a broken one) and Wikidata (redirects on merge). DITA is the cautionary tale:
over-reuse, and machinery built before its first real use. Step 4 builds only what the curriculum already needs.

**How it runs.** Ten sub-steps, A to J, one commit each. Cory gives one go for block one (A to G) and stops it only
where a count decides a choice (the skel drift report in E); block two (H to J) touches no course data. Sizes are
lead-session working time with gates: S under two hours, M half a day, L a day. Each commit's report says which gate
counts are expected to change and why.

### 4.0 What changes, and what is kept

Kept: day files as markdown with frontmatter, the CSV plan data per course, the progressions, the gate scripts, the
kit for tool plumbing, `course + day` as the day key (permanent after scope sign-off), `[[...]]` as the link syntax,
files in git as the only source.

| Today | Problem | Becomes |
|---|---|---|
| The gate runner skips unitplan, frame, sequence, check_site and the skeleton self-tests, builds the site with no flags into dist/ (the deploy folder, deleting the live Closet and Reading Room there), and commits about 130 raw dumps a run | Gates do not test what ships, leave a deploy trap, and swell docs/reviews | 4.A |
| The turn.py queue is 33 math-4 pilot jobs, 5 shown as ready; course runs actually use coursegen's job files | A worker who asks turn.py for a job gets a pilot job | 4.A (queue archived), 4.G (one queue format) |
| data/units.csv (59 rows, pilot only) read by plan.py | 479 ignored failure lines in 21 courses | 4.B |
| The 120 courses exist only as course_status.py's placement of tool modules; three ids per course (`math-4`, `math-grade-4`, `math-k8`), joins by slugged title, two subject spellings, frames.csv fed by constants in frame.py | No owner for the course list; a live `math-4` collision counts the pilot's 22 files as math grade 4 plans | 4.C |
| One ledger file per subject (up to 1.66 MB), rewritten whole by ledger.py with no lock | Two agents in one subject can lose rows; past GitHub's table view; breaks "homes per course" | 4.D |
| Agents edit CSVs by hand (the kit records truncations) | Fragile writes | 4.D (`rows.py upsert`) |
| 2,763 tracked skeletons, all stale against a fresh render, and the day kit lets jobs edit them | Generated files edited by hand and stored twice | 4.E |
| `<!-- skel -->` blocks in 917 written plans feed every new skeleton below them | A stale block spreads | 4.E (drift report before the next course run) |
| No way to ask "what uses this?"; about 140,000 day-number mentions in prose | Changes need searching thousands of files | 4.F |
| Gates run over every course on every job; hooks live in `turn.py end`, which course runs do not use; AGENTS.md contradicts the kit | Checks get slower with every course | 4.G |
| Second homes: the never-touch list, the gate list, grade bands (six scripts), subject spelling, pins and weeks, the fact map, status; no record of retired ids; version-suffixed item ids; docs/reviews has 4,924 files, 3,619 in one folder | Rules and lists drift apart; GitHub stops listing at 1,000 | 4.H |
| No student-facing definitions; vocabulary in four places | Highlighted words would have no owner, or a fifth | 4.I |

Cut from step 4: draft 4's 4.5 (course_pages leak). Passing the rendered standards set still links only standards a
tool module lists, so it renamed the dependency without removing it; the pages are hidden and off the deploy. Its
later.csv row holds the real fix (a standards page for every code a frame owns), and the catalog lint names
course_pages.py `known_standards` as its one exception.

### 4.A Gates that test what ships (M)

- scripts/consolidation_gates.py adds `unitplan.py check`, `frame.py check`, `sequence.py`, the skeleton scripts'
  `--self-test`, and `check_site.py`. Every site build sets CURIO_DIST (build_site.py:17) to a scratch folder and uses
  the deploy flags plus courses (`--library --closet --courses`), then check_site.py on that folder. dist/ is never
  touched by a gate.
- Raw dumps go to an ignored folder; only summary.csv and the compare output are committed.
- Main is tagged `pre-step4` and the tag pushed. A `step4-before` baseline is recorded.
- The 33 pilot rows of data/pipeline/jobs.csv go out of the queue (git history keeps them, ground rule 2).
- The deferred items get their later.csv rows: the standards pages, opaque ids if ever wanted, reading-level lint,
  sampled reads, interchange exporters, the word popup, the Word Wall conversion, WEEKS and PINS if they outgrow 4.C.

### 4.B Retire data/units.csv (S)

plan.py drops the section-row check and takes the hand-back horizon from the course's `days` in frames.csv;
lesson_course.py drops its ignore rule; coverage_ledger.py's guarded read goes; the file leaves with `git rm`.
Expected: about 479 failure lines disappear and several `plan-<course>` gates go from exit 1 to 0. The `modules`
column is tool-side and is not carried over.

### 4.C The course list as data (M to L)

- `data/plans/course-list.csv`, 120 rows, generated once from today's course_status.py output, then owned by hand:
  id (the frame slug for all 120; new slugs in the same style for the 62 without frames), title, subject (one
  spelling), grade or band, core, catalog_id, term, status (active or shelved).
- frame.md owns units, days, minutes and the why; frames.csv becomes a pure join of the two, still gated by
  `frame.py check`. COURSE_ROWS' filters, COURSE_META, TERM and LEGACY leave frame.py. WEEKS and PINS get one owner,
  the frame's Days bullet, parsed, or a later.csv row if that is more than an hour.
- course_status.py builds from the list and attaches module and tool counts only as attributes; its placement rules
  read the list. course_status.py and plan_flow.py join on the id, not the title; `plan_count` stops reading
  docs/courses/<key>/, which ends the `math-4` collision.
- Test: COURSES-STATUS.md before and after is identical apart from the date line and the math grade 4 plan count
  (31 to 9, the pilot's 22 files no longer counted); plan_flow.py and the Desk show the same courses.
- Then the pilot: data/plans/math-4/ and docs/courses/math-4/ stay, named in the HANDOFF doc map as "pilot, kept
  blind, reconciled under later.csv L13" (Cory may archive them instead). The ela-6 leftovers, math-4-spine.md and
  science-4-spine.md leave docs/courses/ (course_status.py's `<key>-spine.md` read goes with them). No string rename
  of `math-4`, ever: it is also the prefix of 13 tool module ids.

### 4.D Ledgers per course, and one safe way to write rows (M)

- `data/plans/<course>/ledger.csv`, split from the four subject files by the `course` column (keys unchanged).
  ledger.py loads a subject by globbing its courses (the course list gives the subject); `write_all` writes only the
  course it changed, through a temp file and `os.replace`. `ledger.py check` before and after prints the same lines.
- `scripts/rows.py upsert <course> <table> --key ...`: the one way the kit asks agents to write a CSV row, with the
  same temp-file write (`plan.py defect` is the precedent). The kit's hand-edit instructions point at it.
- Built 2026-11-25 (e7ad0d3d8, kit version 4). Left open, done in 4.E2 step 0: the subject ladder is still a constant
  in ledger.py (statistics, calculus, two sciences and social studies above grade 5 are missing), and writes take no
  lock (pause-4e review findings 4 and 11).

### 4.E Skeletons are ignored working files (S)

- `docs/courses/*/day-skeletons/` and `section-skeletons/` go in .gitignore and are untracked in one commit (`git rm
  -r --cached`; history and `pre-step4` keep them). A job regenerates what it needs, as day.txt:7 already says, and
  day.txt loses the line that lets a job edit skeletons (a kit version bump). coursegen.py's folder test changes at
  most one line.
- The generator's UK spellings (day_skeleton.py:81 and :221, fixed only in the generated copies) are fixed in the
  generator.
- A report-only drift check re-renders the `<!-- skel -->` blocks in written plans and lists drift. It runs before the
  next course run starts, since those blocks feed new skeletons; Cory picks the fix from the count.
- Built 2026-11-25 (b4bc01898, tag `pause-4e`): 860 of 916 written plans differ from a fresh render. The pause-4e
  review read the drift line by line: most of it is data that arrived after the plan was written; about 14 percent
  of changed hunks are hand edits (a 60-hunk sample). Cory's choice (decision 10): stop storing the copies; 4.E2. The
  skeleton files are still on disk and the generators keep an existing file, so 4.E2 step 0 finishes this sub-step.

### 4.E2 Plans hold judgment only; facts render from data (L, its own go, before 4.F)

Cory, 2026-11-25: "Stop storing the copies at all. Written plans keep only the judgment prose. The mechanical fields
are rendered from data whenever they're needed: in skeletons, in the site build, and in a read view for writers. Each
fact then lives in one place, so drift can't come back." The design is the pause-4e review's outline
(docs/reviews/consolidation/pause-4e-review.md); a data move, so full gate runs before and after.

0. **Finish 4.D and 4.E first** (review findings 3, 4, 11, 13, 14, 15): delete the on-disk skeleton folders (history
   and `pre-step4` keep them); ignored sidecars always rebuild (no keep rule), section.txt builds its own skeletons
   at job start and coursegen always emits the build line; one shared write helper for ledger.py and rows.py (a lock
   per target file, a temp name unique to the process, a retry), with a race test in both self-tests; ledger.py takes
   its ladder from course-list.csv and the gate globs data/plans/*/ledger.csv; rows.py refuses `ledger` and path
   separators, splits on line feeds only, and gains `delete`, `--value-file` and `check`; the 4.B leftovers
   (draft-fix.txt, data/plans/README.md, coverage_ledger.py's dead column, later.csv L71, GLOSSARY.md) are fixed and
   the twelve brief blind lists go on the 4.H task list by name. Kit version 5.
1. **Line-level census.** skel_drift.py compares by content, not block position, and sorts each plan line that is
   not in today's fresh render: (a) it is in the plan's baseline skeleton (the first-commit skeleton for unit plans,
   the sidecar at the writing commit for section plans) or `git log -S` finds its change in the data or generator
   history: a stale copy, data wins; (b) it quotes unit plan prose (section plans): its owner is the unit plan, no
   action; (c) anything else: a hand edit, onto the review list. Counts are reported by cause (later data, stale, unit
   plan prose, hand), so the headline is the hand edits. Social studies unit plans have no baseline and take (a) by
   pickaxe only.
2. **Stop for Cory** with the hand list, each line pre-marked with one of three outcomes: back-port to data (a fact the
   data lacks or has wrong), move out of the markers into the plan's prose (judgment: standard splits, time budgets,
   allocations), or discard (a mistake). Source-map rows typed by writers are one mechanical check (the plan's
   decision equals source-map.csv). The ELA grade 11 sensitivity note goes to the frame. Nothing leaves a block until
   its line has a mark.
3. **Apply the list.** Back-ports through rows.py (frame and standards files by hand, listed); moves to prose by
   script in one commit; word caps rechecked.
4. **Change every reader and writer of the blocks** (review finding 7): unitplan.py's checks read data, and each check
   whose only job was "the copy is present" is dropped; one header check takes the section from the file name and
   days.csv. One `plan_facts` renderer is shared by the skeletons, the writer's read view, plan.py's unit packet and
   front_office_docs.py, so the Front Office shows current facts beside the prose. unit_skeleton.py writes a sidecar,
   never the plan file (codex_units.py and codex_unit_loop.py follow). section_skeleton.py keeps reading unit plan
   prose. The briefs (section-write.md, section-lens.md), kit section.txt, UNIT-PLAN.md's blank copies and
   PRODUCTION-PATH.md change in the strip commit.
5. **Prove, then strip.** Before: the count of plan lines not in the fresh render is zero except lines on the signed
   list. The strip commit: a script confirms each file equals its old text with the marked spans removed and nothing
   else (moved lines listed). After: unitplan, plan and lesson gates with no new lines (the strip simulation on
   scratch copies is the acceptance test: today it adds 8,200 lines, it must add none); section and day skeletons
   rendered to scratch before and after, differences explained; the Front Office JSON diffed before and after.
6. **Spelling.** The three generators' UK spellings are fixed in the strip commit.
7. **Guard.** A `<!-- skel -->` marker in a written plan fails the gate; skel_drift.py retires. The two copies kept
   outside markers (each unit plan's header line and its "Day list (from days.csv, do not edit)") stay as the only
   allowed in-file copies: they are already gated against days.csv. data/homes.csv names them in 4.H.
8. Full gate run and compare, as after any data move.

- Built 2026-11-25 (kit version 6). Cory's answer to q-skel-hand-1: judge each hand line on merit, use earlier work
  where it is better, let data win where data is better. Five judge passes signed docs/reviews/consolidation/step4-E2/
  hand-list.csv (`final`, `final_why`): discard 1438, move 235, back-port 168. Back-ports went through rows.py, plus
  frame and unit plan table cells by hand ("Licence" to "License" in three math source maps). Renderer fixes found by
  the judges: kept-evidence notes that say "not", reuse sources only from earlier days, the field 5 Time line counting
  only a day's own minutes. scripts/plan_facts.py is the one renderer behind every reader (unitplan.py, plan.py,
  front_office_docs.py, the writer's read view `plan_facts.py <course> <file>`). scripts/skel_strip.py removed 9,464
  blocks from 916 plans (62,998 lines; 246 moved lines kept as prose). Proof: 3,112 section and day renders before and
  after differ only by moved lines now shown as prose. Moved standards lines that repeated the rendered standard were
  cut down to the writer's parts split (91 lines), which brought six unit plans back under the 1,600-word cap. 403
  bold-label paragraphs that Markdown joined onto the list item above got a blank line; three orphan sub-bullets got a
  label. Front Office JSON before and after: the moved judgment lines appear and list wrapping changes; nothing is
  lost. Guard: the `skel-guard` gate (`skel_strip.py --guard`) and unitplan.py check fail on any marker in a plan.
  skel_drift.py and skel_census.py retired (copies in S:\CurioClass-archive\skel-tools-2026-11-25\). Gates: step4-E2-0
  26 non-zero, step4-E2-final 25. The only new lines are shifted line numbers and the math K day 36 item gap (later.csv
  L122). Left open: L122 to L124 (items for codes the facts now show, a US spelling sweep of plan prose, math 8 source
  days in the renderer).

### 4.F The index, and the five reports (L)

- `scripts/index.py` builds `data/index.db` (SQLite, git-ignored, rebuilt on every gate run: the scans take seconds)
  from curriculum sources only: the course list, standards, progressions, frames, each course's plan CSVs and
  ledger, day and piece frontmatter (`leans_on:`, `version:`), and `[[...]]` links. `--csv` dumps it for reading.
  build_db.py is not used (it deletes its database and rewrites modules.csv each run).
- Node key: type plus course plus local id (`item:english-language-arts-grade-1:s01-X2`); bare item ids repeat
  across courses. Day nodes are derived (`day:<course>:d042`). Node types include pieces. The tables are left open to
  a `tool` type, which step 5 fills; the bridge is TOOL-ASKS.md.
- **Soft edges:** "day N" mentions in a course's own plans and scope, and bare item ids in prose, typed `mentions`,
  shown by `uses.py`, never failing a gate.
- `scripts/uses.py <id>` lists what uses an object by course and day; `uses.py --changed` lists what depends on the
  files changed since the last commit.
- **Five reports,** one flag each: `resolve` (every `leans_on`, CSV id and `[[...]]` link; "when it exists:" is the
  one allowed unresolved form), `orphans` (days with no plan row, pieces no day leans on: 451 today, plan rows with
  no frame unit), `layout` (against data/homes.csv once 4.H lands), `status` (one answer per object: the file's own
  state wins, flow-status.csv keeps only what no file shows; tool status joins in step 5), `drift` (the 4.E2 marker
  guard plus a check of the two gated in-file copies).
- index.py reads ledgers by globbing course folders, takes subjects from course-list.csv, skips the math-4 pilot by
  name and treats the ten subject folders under docs/courses (arts, health and the rest) as known.
- Each report starts from a baseline file of today's known misses (for example 28 handbacks rows and about 224 prose
  item mentions that do not resolve), so new breaks fail from day one and old ones are worked off by course.
- Built 2026-11-25. scripts/index.py builds data/index.db in about 20 seconds: 43,110 nodes and 299,251 edges
  (226,858 hard). Codes resolve against every standards file, so elective outcome lists count too. Skill ids resolve
  against any subject's progression, because cross-subject rows exist. scripts/uses.py `<id>` and `--changed` group
  uses by course and day; soft edges are marked. Baseline data/index-baseline.csv: resolve 7 known misses (11
  lines: three bad item codes and four missing leans_on targets), orphans 386 pieces, layout waits for homes.csv
  (4.H), status 0 contradictions (412 flow-status rows only restate a written plan, to drop in 4.H), drift 0. Prose
  item ids are soft, so the review's "about 224" is shown by uses.py and never fails. Gates `index-reports` and
  `selftest-index` were added to the runner. The misses are worked off under later.csv L125.

### 4.G One gate command (M)

- `scripts/gate.py --course <id> | --changed | --all` runs plan, lesson_course, ledger, unitplan and frame checks,
  the index reports and lint for that scope, and prints new lines against a stored baseline. turn.py, the lead,
  coursegen's gate lines and the consolidation runner all call it; consolidation_gates.py becomes `gate.py --all`
  plus the site build. Its compare also flags a gate that disappears, an exit code that changes and a count that
  rises (a count that falls is reported once); no line cap in the stored compare; the self-tests of rows.py and the
  write helper, `lesson.py check` and `front_office.py check` join the gates. The kit's `{PLANGATE}` and
  `{LESSONGATE}` become `gate.py --course`.
- `scripts/lint.py`, inside gate.py: the catalog check (no curriculum script opens a tool catalog file, one named
  exception), the never-touch guard and the generated-file guard (from data/homes.csv once 4.H lands), and the three
  style checks (em dash, "Curio Class" in full, a US spelling list) in about ten lines, run over what generators print
  as well as finished pages.
- One queue format: coursegen's job files. jobs.csv retires with the pilot.
- AGENTS.md's first section is rewritten to current practice: the gate is `gate.py`; who commits (the lead, or a
  queued job's end); side-by-side work is allowed in different courses, never on the same files, which is safe once
  ledgers are per course (4.D) and their writes take a lock (4.E2 step 0); common.txt says the same.
- **Curriculum writing may restart when 4.G closes.** H to J and step 5 touch no course data.
- Built 2026-11-25 (kit version 7). scripts/gate.py `--course`, `--changed`, `--all [--site]`, `--baseline`,
  `--save`, `--only`, `compare`, `list`; a course run takes about 20 seconds. Its compare flags a gate that is gone
  (it reads an older run's summary.csv from docs/reviews/consolidation when build/gates has none, which caught the
  pilot math-4 gates dropping out: the gate keeps the pilot course in scope although the index leaves it out), an
  exit code change, a failing count that rises or falls, and each new line. scripts/lint.py holds the catalog,
  never-touch, generated (silent until homes.csv) and style checks; style lines carry a count per file, not line
  numbers, so moved lines are not new. turn.py `end` and `start` run `gate.py --course` for the job's course;
  consolidation_gates.py is a thin wrapper over `gate.py --all --site --save`. The kit's `{PLANGATE}` and
  `{LESSONGATE}` became `{GATE}` in eight templates and coursegen's sweep gates; AGENTS.md's first section and
  common.txt describe the gate, who commits and side by side work in different courses. data/index.db is written
  through a per-process temp file. jobs.csv and turn.py's queue stay working until the pilot retires. Run step4-G
  (205 gates) against step4-E2-final: no change in any gate that ran before except a build note; the two new gates,
  the whole-repo lesson check (5,470 FAIL lines) and lint style (4,210 lines, mostly UK spellings in finished pages),
  are stored as the `--all` baseline and worked off under later.csv L126.

### 4.H Homes and ids (M)

- `data/homes.csv`: path pattern, kind (source, generated and ignored, generated and committed, state, frozen,
  never-touch), owner script, check. It includes plan prose ("judgment only; marker guard"), the skeleton sidecars
  (generated, ignored, always rebuilt), the ten subject folders under docs/courses, and the two gated in-file copies
  of 4.E2 step 7. The brief blind lists that still name data/units.csv are replaced from it here: plan-codex.md,
  plan-codex-ela.md, plan-codex-math.md, plan-codex-science.md, plan-codex-read.md, prework-codex-read.md,
  progression-write.md, section-lens.md, section-write.md, unit-calendar-fix.md, unit-correct.md, unit-lens.md,
  unit-lens-fix.md and unit-ruling-fix.md (14, in docs/pipeline/briefs/). It replaces the never-touch and gate lists in AGENTS.md, turn.py and the kit,
  and the source and generated list of draft 4. lint reads it; HANDOFF links it.
  - **Generated, committed for reading on GitHub:** docs/COURSES-STATUS.md and docs/BUILD-BOARD.md, regenerated by
    the lead at session end or a queued job's end; the date line is left out of any comparison; no failing gate.
  - **Generated, committed, gated by their own check:** frames.csv, calendar.csv, modules.csv.
  - **Frozen tool catalog, inside which sit the Word Wall, the worksheets and the topic pages:** data/modules/,
    modules.csv, tools-concepts.csv, sequence.csv, coverage.csv, data/concepts/, docs/agents/catalog/shape/,
    data/closet/.
  - **State, changed only by its script:** the two R2 manifests.
- One shared module for grade bands (from data/bands.csv) and subject ids, imported by the curriculum scripts; it
  absorbs ledger.py's ladder, coursegen.SUBJECTS, plan_flow.PFILE and the mapping in front_office.py.
- `data/ids-retired.csv`: committed, append-only (old_id, new_id or blank, date, reason); the registry is generated
  from the index plus this file, never committed.
- Item versions: "a revised item keeps its id; the version goes in the `version` column" (data/plans/README.md), and
  a plan.py check fails a new suffixed id unless it is on a baseline of today's 636. Old suffixes are stripped as each
  course is next reviewed.
- **Day numbers are permanent once a course's scope and sequence is signed off.** A course changes by rewriting a day
  in place or trading content inside a section; the year has a fixed length, so an insert always removes a day
  somewhere. A true renumber is a course rewrite, planned as one.
- **docs/reviews home rule:** per-job reports go to `docs/reviews/<course>/`; cross-course reports stay at the top;
  when a course is signed off its per-job reports are zipped to the archive with one summary left. The 1,305
  committed raw gate dumps under docs/reviews/consolidation/ leave with `git rm` (the tag keeps them).
- **Generated, not committed:** build/, dist/, tool bundles, data/index.db, the registry, data/curioclass.db, the
  skeleton folders. Large media stays out of git (art/raw, voice/raw, library art), backed up to X: and R2.
- Sources as we go (Cory decision 5) stays a writing rule in the briefs, not lint.
- `docs/CHANGES.md`, one page: request (a step, later.csv or the Desk), impact (`uses.py`), a script with
  `--dry-run` and a diff summary, `gate.py`, one log line. Errata waits for a course that is taught.

### 4.I Words: the architecture, not the links (M, after the Desk card)

See "Words: from the days, not from the tool catalog" in the end goal.

1. **The Desk card first** (q-word-names-1): the feature's name, the table's name (not words.csv: twelve courses
   already have a words.csv of banned patterns), the sense id rule, the link form, what a course that spans bands
   does, and what becomes of the six wordlist.csv files.
2. The word table with its loader: sense id, word as shown, band (from data/bands.csv), definition, fun fact, the fun
   fact's claim-level source (Cory decision 5), status, from.
3. lesson.py learns `[[word:<sense>]]` and `[[word:<sense>|shown]]`; a mark with no row for the day's band renders as
   plain text, so it can never break a page.
4. The index's "day uses word" edges come from ledger term rows; lint checks that a marked word has a ledger term row
   in that course. Two reports: introduced but undefined (the backlog), defined but never used.
5. The read-only import of Word Wall definitions as candidate rows, collisions and span-grade topics to a review list.
6. Print and popup design, and who writes definitions (reading level per band, a fresh-agent sensitivity read of fun
   facts), are later.csv rows.

### 4.J Close step 4 (S)

`gate.py --all` against `pre-step4`, the site built into scratch with the deploy flags, and the 12 tests printed as
numbers into data/plans/goal-tests.csv (goal test 3 reads the marker guard count, which prints 0). The step report
lists every count that moved and why.

Then a full-scope Fable review (Cory, 2026-11-25), before step 5 starts: a cold read of the whole repository and
the step report, not anchored on the plan's own claims. It answers three questions: did step 4 come out as intended
(each sub-step's goal and the 12 end-goal tests, read from the data, not from the Built notes); is the project in a
better place overall than at `pre-step4` (for writers, the lead, the gates, the site and the next 118 courses), and
what got worse; and is there anything major to address now, before step 5 and before curriculum work runs at scale.
Findings go to docs/reviews/consolidation/step4-close-review.md and are brought to Cory with a recommendation each;
step 5 waits for his read.

### 4.K Order

A first, because everything after is judged by it. B, then C before the pilot folders change (the plan count cell
moves). D before G, since side-by-side work is only safe once ledgers are per course. E before F, so the index never
sees 2,763 files that are about to go; E2 before F for the same reason (the index and its baselines would otherwise
count block copies), and before writing restarts, so no new plan is born with markers. G closes block one.
Order: A, B, C, D, E, E2, F, G, H, I, J, then the close review. 4.E2 needs its own go and stops once, at its hand list (step 2); F and G
then run under the block-one go. H, then I (it alone waits on a design answer), then J.

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
   different schema) is left alone or retired in the same commit, said explicitly. Tool stage then joins the index's
   `status` report (4.F). This comes before any folder is flattened, which removes the reason to flatten in a hurry.
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
   two files. Until the last tool is flattened, board.py and the gates support both shapes. Before any of this, index.py
   fills its `tool` nodes (4.F), with edges from each course's TOOL-ASKS.md, so a tool's scattered pieces in the
   repository and the archive are found by `uses.py`, not by a one-off listing.
6. **Pilots.** Cipher Vault (about 40 pieces in four places), Living Pond and one tool just past Spec go through 1 to 5
   by hand before the rule applies to new work.

## Step 6: close

Switch the scheduled tasks back on (only those Cory still wants), fill the after counts in docs/funding/SCALE.md from
data/plans/goal-tests.csv, refresh the Desk, update HANDOFF.md (linking data/homes.csv rather than copying the fact
map), AGENTS.md and the memory notes, and write a short record of what moved where (git history and the archive index
hold the detail).

## Decisions taken (Cory, 2026-11-24)

1. build/: untracked on main and on draft/codex before the merge (step 0.4).
2. Tether Drift: a Recess game, not ready; kept as a side project (step 1 table, later.csv row).
3. The 45 Flash research packets: checked, no later use; archived with SPEC.md's packet line and RESEARCH-PACKET.md.
4. The visible kit frame becomes optional (step 5.3) once the contract scripts pass.
5. Sources as we go: every piece names its sources, checkable specifics (numbers, dates, names, scientific and
   historical facts in informational texts and in tools) carry a claim-level source; not every statement. A writing
   rule, not lint, applied when a file is next written or touched (step 4.H's homes rule keeps it in the writing briefs).
6. Gemini/Api.txt stays where it is, untouched, for when tool work resumes.
7. The scale of the project is recorded for later marketing in docs/funding/SCALE.md: the before counts now, the
   after counts at step 6.
8. Curriculum first: the tools never shape the curriculum; they are reshaped to it once it is done (step 4.C, the course list as
   data, and step 5 scope).
9. Draft 5 (Cory, 2026-11-25: "Let's fold it all in"): every finding and rule change of the full Fable review of step
   4 is taken, including tracked files archived by git (rule 2), scoped gate runs (rule 3), one go for block one
   (rule 1), curriculum writing restarting when 4.G closes, the Word Wall route (read-only import in 4.I, conversion
   at the tool reshaping stage, never-touch rule kept whole), and cutting draft 4's course_pages step to later.csv.
10. Skel copies (Cory, 2026-11-25, Desk card q-skel-drift-1): stop storing data copies in written plans; plans keep
    only judgment prose, facts render from data in skeletons, the site build and a writer read view. Before it was
    built, a pause point (tag `pause-4e`) and a Fable review of 4.A to 4.E and the proposal; draft 6 folds the review
    in as 4.E2, before 4.F.
