# Consolidation plan: one flat product, then an architecture that scales

Status: draft 3, 2026-11-24, for Cory. Not approved; nothing in it has been done. Draft 1 was reviewed against the
repository by a fresh Fable agent the same day; its 16 findings are folded in (the review's evidence is summarized
where a finding changed the plan). Draft 3 takes Cory's comments of 2026-11-24: nothing old is left standing beside
the new model ("live things" now migrate, step 4.1), earlier decisions that change are listed (step 4.0), this
consolidation is the mass edit (the change workflow moves in, step 4.4), and his six decisions are recorded at the end. Built on a read-only census of 2026-11-24: every sibling folder, the Codex and
Antigravity homes on C:, the tool pipeline and the curriculum layers.

## Why

Hundreds of sessions across Claude, Codex and Antigravity worked in several folders. Some work exists in only one copy
outside the repository, stale plans sit beside current ones, and changing one thing (a text, a standard, a routine)
means searching thousands of files. After the curriculum is written there will be tens of thousands of files. The aim:
one folder (S:\CurioClass), one home per fact, nothing lost, and an architecture that makes later edits cheap and safe.

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
   them: `math-4` and `ela-6` (live plan ids), `data/units.csv` (plan.py), `data/modules.csv` (build_site.py and about
   30 scripts), `data/sequence.csv` (the site Map), `data/coverage.csv` and `data/concepts` (the catalog scripts,
   board.py, desk_stats.py), `section-skeletons/` and `day-skeletons/` (required by coursegen.py). Steps 1 to 3 leave
   them alone. Step 4.1 migrates each into the one curriculum model: the scripts that read it change first, the gates
   pass on the new source, and only then does the old file go to the archive, so nothing old is left standing beside
   the new. The two R2 manifests (`data/media-manifest.txt`, `data/docs-manifest.txt`) are the exception: they are
   the record of what is in the live bucket, not a duplicate of anything, so they stay committed and are changed only
   by sync_media.py.

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

The curriculum will grow tenfold. The architecture should make three things cheap: finding everything that uses a
thing, changing it everywhere by script, and knowing a change broke nothing. This consolidation is the mass edit that
architecture is built for: it touches every layer once, so the model, the tooling and the migrations land together,
and later work only follows the model.

The closest models are the open textbook and courseware platforms, not general documentation:

- **OpenStax**: modules with permanent ids, collections that order them, generated outputs never edited by hand.
- **Kolibri Studio and Khan Academy content trees**: every node has a stable content id kept apart from its position
  in the tree, so reordering or inserting moves nothing that links to it.
- **Sphinx and Antora** (documentation builds): links are written by id and the build fails on a broken one.
- **Wikidata**: opaque ids that carry no meaning that can change, and redirects when two items merge.
- **DITA** (technical publishing): typed topics and key-based links; its cautionary tale is over-reuse, where nobody
  dares edit a shared piece.

### 4.0 Earlier decisions that change, and what is rebuilt

Some of what exists is sound and is kept as it is: day files as markdown with frontmatter, the CSV plan data per
course (days, items, wrongs, parts, materials), the progressions, the gate scripts, the ledgers as the term record,
the kit for tool plumbing. These are rebuilt or replaced:

| Today | Problem | Becomes |
|---|---|---|
| A tool-era topic catalog (modules.csv, 815 modules; sequence.csv; coverage.csv, 2,400 rows; data/concepts; the shape files) beside the course model (progressions, frames, scopes, unit and section plans, days) | Cory's intent was always the reverse of what this catalog implies: the curriculum comes first and the tools are reshaped to it after the curriculum is done. No curriculum gate reads the catalog (plan.py, unitplan.py, lesson.py, coursegen.py, ledger.py, progressions and frames do not), but two curriculum-facing scripts lean on it: course_pages.py links a standard only if a tool module lists it, and course_status.py builds part of its course list from module placement | **The course model is the only curriculum model** (4.1). The two leaks are cut now; the catalog is frozen as tool-side data and is retired when the tools are reshaped to the finished curriculum |
| data/units.csv (60 rows, the math-4 pilot) read by plan.py | A third unit list beside frames.csv and days.csv | retired into frames.csv and days.csv; plan.py reads those |
| math-4 and ela-6 pilot ids beside math-grade-4 and english-language-arts-grade-6 | Two names for one course, two sets of folders | migrated to the full course ids, the old ids kept as aliases in the registry; turn.py jobs renamed |
| Unit plans that hold tables also kept in CSVs (the Codex run replaced some with pointers, which caused the carry-overs) | Two homes for the same facts | **CSV holds structured facts, markdown holds prose**; any table in a plan that repeats CSV data is generated from the CSV, never typed |
| section-skeletons/ and day-skeletons/ kept after the real plan or day is written | Two files per section or day, one stale | a skeleton is a working file: once its plan or day passes, it goes to the archive and coursegen.py accepts the written file in its place |
| Status in many places: day frontmatter `version:`, flow-status.csv, defects.csv, later.csv, Desk items, tool stage guessed from file names | No single answer to "where is this?" | **one status field per object** in its source (frontmatter for days, the stage CSV for tools, a column for plan rows); flow-status.csv, the dashboard and the Desk read it |
| Positional ids (day number), version-suffixed item ids | Ids change when the curriculum changes | stable ids (4.2) |
| One worktree per AI platform, a union merge rule in .git/info | Work splits and merges silently go wrong | one working folder, short branches, key-aware merges (steps 0 and 2) |
| About 41 top-level plan docs, rules restated across AGENTS.md, briefs and lenses | Agents read the wrong rule | one doc map; each rule stated once, and the mechanical rules become lint (4.6) |
| 122 scripts, several overlapping (plan.py, unitplan.py, lesson.py, lesson_course.py, coursegen.py) | Hard to know which gate is the gate | one command per job named in the doc map; overlapping scripts merged or retired as each migration touches them, not as a separate rewrite |

### 4.1 One curriculum model: the curriculum first, the tools after

Cory, 2026-11-24: the curriculum is the product, and the tools are reshaped to it after it is done; the tools never
give shape to the curriculum.

- **The curriculum graph.** Every curriculum object is a node with an id; every relation is an edge. Node types:
  standard, skill (progression node), course, unit, section, day, item, text, term, routine, source. Edges: day
  teaches skill, item checks standard, day reads text, term introduced on day, and so on. Its inputs are the
  standards files (data/standards/), the progressions, frames.csv and each course's plan data, and nothing tool-side.
- **Cut the two leaks now.** course_pages.py takes its known standards from data/standards/, not modules.csv.
  course_status.py builds its course list from frames.csv and the course catalog, and reports tools only as a count
  beside each course, never as what makes a course. Each change is checked by building the course pages and the status
  page before and after and comparing them.
- **Curriculum migrations**, one at a time, each with the scripts that read the old file changed first and before and
  after gates: units.csv into frames.csv and days.csv; the math-4 and ela-6 ids; the skeletons.
- **The tool catalog is frozen, not migrated.** modules.csv, sequence.csv, coverage.csv, data/concepts and the shape
  files stay where they are, read only by the tool side and the site's topic pages and Map, and no curriculum script
  may start reading them (a lint rule, 4.6). Nothing new is added to them.
- **After the curriculum is done** (a later.csv row): each tool is mapped onto the skills and days it serves, the
  topic pages become views over the curriculum graph, coverage becomes a query, and the catalog goes to the archive.
  Tools then show on the days that teach their skill.

### 4.2 Permanent ids

- **Ids carry no position.** A day's id is not its number (inserting a day would renumber every later id and every
  link). Each day gets a short opaque id minted once and stored in its frontmatter (`id:`); the day number, unit and
  section are attributes. The same holds for sections and units.
- **Versions are not ids.** An item's id is its stem without the version suffix (`s02-A6` for `s02-A6v2`); `v2` is
  its version. A revised item keeps its id.
- **The registry** (`data/registry.csv`: id, type, path, title, aliases, replaced_by, plus the pointer to the source
  that holds its status, owner and version) is generated from the files and CSVs by a script and never edited by hand.
  Legacy ids are aliases from day one. A retired object keeps its row with `replaced_by` set; an id is never reused.
- **No CSV is rewritten for prefixes.** Type prefixes (`text:`, `tool:`, `std:`) exist only in the registry and in
  prose links; CSV columns keep their bare ids.
- **Standards.** The human code stays (RL.1.2, with the publisher in the registry). A `case_guid` column is added when
  the 1EdTech CASE identifiers are imported, since CASE identifies items by GUID, not by code.

### 4.3 The "what uses this?" index

- `scripts/index.py` extends build_db.py's database (one file, `data/curioclass.db`): the graph's nodes and edges.
  Version 1 edges come from `leans_on:`, the CSV id columns and existing relative markdown links; no new syntax is
  needed to start.
- `scripts/uses.py <id>` lists everything that uses an object, by course and day; `uses.py --changed` lists what
  depends on the files changed since the last commit.
- **Gate.** Every `leans_on` path and every id in a CSV column resolves. It starts as a report and becomes a failing
  gate after one clean run.
- **Prose links by id.** `[[text:g1-u2-c47]]` is added where the build needs a rendered title, and lesson.py learns to
  render it in the same commit. Plain paths in prose are converted by one scripted pass during this step (4.4), since
  every day is touched anyway when its id is minted.

### 4.4 The change workflow, built now and used by this consolidation

Every change to published material, starting with the migrations of 4.1 and the id pass of 4.2, goes: request (the
step of this plan, later later.csv or the Desk) to impact list (`uses.py`) to scripted batch edit with a dry run and a
diff report to gates to an errata entry with the course version (finished-course item 11). A mass edit is a script
with a dry run, as bots do on Wikipedia, never hundreds of hand edits. Building it first means every later step of
this plan runs through it, so it is tested on real work before the curriculum grows.

### 4.5 Source and generated

- Source: markdown, CSV, scripts, art and voice. Generated and not committed: build/ (step 0), tool bundles (already
  ignored), the registry, the index, any plan table generated from CSV (4.0).
- Generated but committed: docs/COURSES-STATUS.md and docs/BUILD-BOARD.md, because HANDOFF links them and people read
  them on GitHub. A gate fails when either is out of date.
- State, committed, changed only by its script: the two R2 manifests (sync_media.py).
- Large media stays out of git (art/raw, voice/raw, library art), backed up to X: and R2.

### 4.6 Writing aids from large datasets

- **House rules as a linter.** No em dashes, "Curio Class" in full, US spelling, reading level by grade, banned
  phrases, step names from docs/GLOSSARY.md, no curriculum script reading the tool catalog: one style check runs on every file, in the spirit of the Vale linter
  documentation teams use. Readers stop spending tokens on what a script can catch. Built in this step.
- **Structure first, prose second.** Plans and days are written into shapes generated from data (unit plan skeletons
  already are); the generated tables of 4.0 extend this.
- **Sources as we go (Cory decision 5).** Every text, day and tool names its sources at the level of the piece, and
  checkable specifics carry a claim-level source: numbers, dates, names, scientific and historical facts in
  informational texts and in tools. Ordinary sentences, stories and teacher moves do not. Applied when a file is next
  written or touched, not as a pass over old files.
- **Sampled reads by risk** (new authors, new kinds of day, low gate margins), checked against a gold set, as large
  labeled datasets are checked. Designed here, first used when the Codex draft review resumes (paused by Cory).
- **Interchange later, shaped now.** The graph's fields are chosen so exports need no rework: Common Cartridge for
  schools' learning platforms, QTI for items, LRMI and schema.org alignment metadata for day pages. The Learning
  Commons Knowledge Graph's standards crosswalks could be imported rather than rebuilt (license terms checked first).
  The exporters themselves wait for a school that needs them.

### 4.7 Order

4.4 (the workflow) and 4.3 (the index) first, since everything after runs through them; then 4.2 (ids minted by one
scripted pass, prose links converted in the same pass); then the 4.1 leak cuts and migrations one at a time; then 4.6
(the linter). Each lands with before and after gates and its own commit.

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
5. Sources as we go, at the level of step 4.6: every piece names its sources, checkable specifics carry their own;
   not every statement.
6. Gemini/Api.txt stays where it is, untouched, for when tool work resumes.
7. The scale of the project is recorded for later marketing in docs/funding/SCALE.md: the before counts now, the
   after counts at step 6.
8. Curriculum first: the tools never shape the curriculum; they are reshaped to it once it is done (step 4.1, step 5
   scope).
