# Step 4 cold read (Fable, 2026-11-25)

Scope: docs/CONSOLIDATION-PLAN.md step 4 (4.0 to 4.7), with the ground rules and the decisions that bind it, checked
against S:\CurioClass at commit 4c5eb6911. Read-only: nothing was edited, no gate or writing script was run. The
only files read under data/ were opened read-only. Gemini/Api.txt was not touched.

## Verdict

**Ready with changes.** The direction holds: no curriculum gate reads the tool catalog, the two leaks are real,
`leans_on` is already a clean edge list, and the index and registry can be built with almost no risk. But five things
in step 4 are wrong about the repository as it stands, and each would cause damage or wasted work if carried out as
written: (1) math-4 is not a second name for math-grade-4, it is a different, older design of the course that the
briefs keep blind on purpose; (2) an opaque day id in frontmatter does not remove position, because the day number is
the key of every plan CSV, the ledgers, the file names and the item ids; (3) build_db.py deletes its database and
rewrites modules.csv on every run, so it is the wrong host for the index; (4) cutting the course_pages.py leak the way
4.1 says would create dead links; (5) frames.csv and the course catalog do not hold the 120 courses that
course_status.py reports. The 4.7 order should also flip: the small cuts first, the index next, ids last and smaller.
With those changes step 4 is about a third of its written size and safe to run.

## Findings

### 1. math-4 is a separate older course design, not an alias of math-grade-4 (major)

**Plan lines:** 4.0 table row "math-4 and ela-6 pilot ids beside math-grade-4 and english-language-arts-grade-6: two
names for one course ... migrated to the full course ids, the old ids kept as aliases in the registry; turn.py jobs
renamed"; 4.1 "Curriculum migrations"; ground rule 7 ("live plan ids").

**Found:**
- Both ids have their own data folder, with different content. data/plans/math-4/ holds 10 CSVs of the pilot (days.csv
  60 rows covering days 1 to 38 and 72 to 93, units numbered 1, 2, 3, 4, 9, 10, 11; items.csv 812 rows).
  data/plans/math-grade-4/ holds days.csv with 160 rows in 9 units plus C, and source-map.csv. frames.csv:28 gives
  math-grade-4 9 units. The pilot's unit 11 has no counterpart number in the new course.
- The docs folders collide file for file: docs/courses/math-4/ and docs/courses/math-grade-4/ both hold DEFAULTS.md,
  s01.md to s04.md, with different text (math-4/s01.md is "Days 1 to 6", math-grade-4/s01.md is "Days 1 to 8").
  Both data folders hold days.csv and source-map.csv.
- The separation is a standing rule, not an accident. docs/PRODUCTION-PATH.md:136 "Write blind, then reconcile"
  and :209 "Math's old work ... read against the new layers and changed where the review finds it, rather than kept
  because they exist". scripts/defaults.py:21 `BLIND = ('math-4', 'ela-6')`; scripts/front_office.py:33;
  scripts/codex_scopes.py:57-65; scripts/section_cuts.py:29 `SKIP = {'math-4'}`; about 14 briefs under
  docs/pipeline/briefs/ and docs/pipeline/kit/common.txt name docs/courses/math-4/ as a path writers must not open.
  later.csv L13 (open) holds the rework list: about 40 of 48 built days fit with edits, 6 check days need rewriting.
- The alias already exists where it is needed: scripts/frame.py:118 `LEGACY = {'math-4': 'math-grade-4'}`, the
  `legacy_plan_id` column of frames.csv, frame.py:681.
- "math-4-" is also the prefix of 13 tool-catalog module ids (data/modules.csv), which appear in coverage.csv (28
  lines), sequence.csv (24), tools-concepts.csv (13), data/closet/words/math.txt (66) and data/media-manifest.txt
  (66). The last two are never-touch files. Any scripted rename that matches the string `math-4` hits them.
- The whole turn.py queue is the pilot: data/pipeline/jobs.csv has 33 rows, all math-4, 3 done and 30 waiting, with
  pilot day ranges (unit 5 is "39-41"; in math-grade-4 unit 5 has 19 days). `turn.py status` today shows
  math-4-u05-plan, -u06-, -u07-, -u08-plan and math-4-d025-write as **ready**. Renamed to math-grade-4 they would
  point at the wrong days.
- ela-6 is not a live plan id at all. There is no data/plans/ela-6 and no courses/ela-6; what is left is
  docs/courses/ela-6/RIGHTS.md (one file, and later.csv L14 says none of its texts fits a frame unit) and
  docs/courses/ela-6-spine.md.

**Why it matters:** a rename merges two designs into one folder, overwrites or collides s01 to s04 and DEFAULTS,
puts the old work inside the folder that blind writers must work in, and risks the never-touch files. Renamed jobs
would hand a worker the wrong unit. And a worker who runs `turn.py start --role planner` today is given a pilot job.

**Change to the plan:** replace the "migrate the ids" row with "math-4 and ela-6 are old work, held apart until the
reconcile (L13, L14)". Now: (a) cancel or archive the 33 queue jobs, so the queue is empty and honest; (b) leave the
math-4 folders where they are, named in the doc map as "pilot, blind, reconciled under L13", or move them whole to
the archive if Cory wants them out of sight (his call: the L13 reconcile then reads them from the archive); (c) move
ela-6/RIGHTS.md and the three old spine files to the archive or mark them the same way. The pilot retires by content
when math grade 4 is reconciled, and its special cases (plan.py:197 and :702, unitplan.py:359 and :371,
section_cuts.py:29, frame.py LEGACY) go in that commit. No string rename of `math-4`, ever.

### 2. An opaque day id in frontmatter does not make days position-free (major, and over-built)

**Plan lines:** 4.2 "Ids carry no position ... Each day gets a short opaque id minted once and stored in its
frontmatter (`id:`) ... The same holds for sections and units"; "No CSV is rewritten"; 4.7 "ids minted by one
scripted pass".

**Found:**
- No day has an `id:` today (2,114 day files; keys are day, course, unit, version, materials, print, credit,
  leans_on; scripts/lesson.py:25).
- The day number is the join key everywhere: days.csv in 59 courses (8,564 rows), items.csv (24 files, 14,587
  rows, column `day`), source-map.csv (44 files), errors.csv, sources.csv, the four ledgers (34,177 lines, column
  `day` and `where`), calendar.csv (first_day, last_day), the file name `dNNN.md`, and 20,789 `leans_on` path
  entries that name those files. Only 2,114 of the 8,564 planned days have a file to hold frontmatter.
- Item ids carry position themselves: in all 13,292 items with the usual stem, the `sNN` equals the item's unit, and
  in 5,244 of 5,273 practice items the number after `P` equals the day (for example `s11-P90-1` is unit 11, day 90).
  There are 30,417 `[[item id]]` references in courses/.
- Unit and section plans (docs/courses/<course>/sNN.md, uNN-S.md) have no frontmatter, and section folders are named
  by position (courses/<course>/u01-1/), so "the same holds for sections and units" has no home yet.
- Item ids are unique only inside a course: 1,648 ids appear in more than one course (`s01-X2` is in 15). A
  registry keyed on a bare id cannot work; the key must be course plus id.

**Why it matters:** after the pass, inserting a day would still renumber every CSV row, file name, `leans_on` path
and item id after it. The pass touches 2,114 files (1,691 of them Codex drafts marked "not ready" whose review is
paused) and buys nothing that `course + day` does not already give. This is the DITA lesson applied to ids: cost now,
benefit only if a much larger re-keying follows.

**Change to the plan:** drop the frontmatter pass from step 4. The registry gives every object a derived id
(`<course>/d042`, `<course>/s02-A6`, `text:gk-u1-01`), marked as legacy from day one, and resolves aliases. Write
down the real rule that makes insertion cheap, and build it only when the first insertion is needed: a scripted
`renumber` in the change workflow that rewrites days.csv, the day-keyed CSVs, the ledgers, the file names and
`leans_on` together, with a dry run. If Cory still wants opaque ids, the home is a column in days.csv (the source for
all 8,564 days), not frontmatter, and it is a separate later step, not part of this consolidation.

### 3. build_db.py is the wrong host for the index (major)

**Plan line:** 4.3 "`scripts/index.py` extends build_db.py's database (one file, `data/curioclass.db`)".

**Found:** scripts/build_db.py:96-99 rewrites data/modules.csv on every run (it is generated from data/modules/*.txt
and data/modules/kept-ids.csv); :101-102 does `db_path.unlink(missing_ok=True)` and rebuilds from scratch; :104
loads only the tool catalog CSVs (grades, bands, subjects, courses, grade_subjects, tool-types, tools, modules).
The file is git-ignored (.gitignore:1), dated 2026-11-13, and stale: it holds 797 modules while modules.csv has 814.
Nothing reads the database: the only mentions of `curioclass.db` in scripts/ are in build_db.py itself.
build_db.py is called by scripts/overlap/stage_merge.py:71 and wave_standards.py:106.

**Why it matters:** an index living in that file is wiped whenever a tool-side script runs build_db.py, and running
build_db.py to refresh the index would rewrite modules.csv, which 4.1 freezes. It also puts the curriculum graph
inside the tool catalog's database, the reverse of the rule in 4.1.

**Change to the plan:** the index is its own generated, ignored file (for example `data/index.db`, or plain
`data/index/nodes.csv` and `edges.csv`, which diff and need no database), built only by index.py from curriculum
sources. build_db.py is left alone as tool-side. Add `data/index.db` or the folder to .gitignore in the same commit.

### 4. Cutting the course_pages.py leak as written creates dead links (major)

**Plan line:** 4.1 "course_pages.py takes its known standards from data/standards/, not modules.csv."

**Found:** scripts/course_pages.py:298-303 `known_standards()` reads the `standards` column of modules.csv, and
:324 uses it only to decide whether a code gets an `href='/standards/<slug>/'`. That set is exactly the set of
standards pages the site builds: scripts/build_site.py:125-128 and :343-357 render one `/standards/<slug>/` page per
code that a module lists. I counted 1,651 slugs from modules.csv and 1,651 folders under dist/standards/. So the
function answers "does a page exist to link to", not "is this a real standard". data/standards/ holds 32 files in
several layouts (tab-separated .txt, .csv, "-words" files) and many more codes than 1,651.

Also: the course pages are built only with `--courses` (build_site.py:193) and are hidden (course_pages.py:39
`SHOWN = False`). The consolidation gate runs `build_site.py` with no flag (scripts/consolidation_gates.py:36), so
the before and after gates never build a course page.

**Why it matters:** swapped as written, every owned standard with no tool gets a link to a page that does not exist.
Nothing is live yet because the pages are hidden, but the comparison the plan asks for would show hundreds of new
links and pass anyway, and the dead links would ship on the day SHOWN flips.

**Change to the plan:** pick one of two, and say which. (a) Small: build_site.py passes course_pages the set of
standards pages it actually renders, so the dependency is on "pages built", not on modules.csv by name. (b) Larger,
and the real fix for "curriculum first": build_site.py renders a standards page for every code a course frame owns
(from data/standards/ plus the frames), with tools listed where there are any; then course_pages links all of them.
Either way, the check is `build_site.py --courses` into a scratch dist before and after, plus a link check over the
course pages, and that command is added to the step's gate list by hand.

### 5. frames.csv and the course catalog do not contain the 120 courses course_status.py reports (major)

**Plan lines:** 4.0 "course_status.py builds part of its course list from module placement"; 4.1 "builds its
course list from frames.csv and the course catalog, and reports tools only as a count".

**Found:** it is not part of the list, it is the list. scripts/course_status.py:32 loads modules.csv, :46-68
`place(m)` turns each module into a course key, and :71-76 creates every `info` entry from a module; :77-89 only
fill in per-grade and split rows that no module reached. The last gate run prints "courses 120 core4 58"
(docs/reviews/consolidation/step3-after/summary.csv:6). data/plans/frames.csv has 58 rows (the core courses only)
and data/courses.csv has 77 rows, several of them one row for many courses ("math-k8, Grade-level Math, k-8"). The
62 non-core courses (per band, per grade for computer science and library) exist nowhere except as the result of
placing modules, with the rules hard-coded at course_status.py:22-27. scripts/plan_flow.py:31 runs
course_status.py and joins on its titles, and the Desk reads the result.

A related second home the 4.0 table misses: frames.csv is itself generated. `frame.py sync` writes it from each
docs/courses/<course>/frame.md plus constants in frame.py (COURSE_META, COURSE_ROWS, LEGACY, frame.py:118 and
:669-677), and `frame.py check` fails when it disagrees. The plan treats frames.csv as a source to migrate things
into.

**Why it matters:** the cut cannot be made until a real list of the 120 courses exists. Done as written, the status
page drops to 58 courses or the count shifts, plan_flow.py and the Desk shift with it, and "compare before and after"
has no fixed point.

**Change to the plan:** first write the course list as data: one row per course as a school would schedule it (id,
title, subject, grade or band, core, catalog_id, status active or shelved), 120 rows, generated once from today's
course_status.py output and then owned by hand. frame.py's COURSE_META and course_status.py's BY_GRADE, PER_GRADE,
SPLIT and ONE_ROW rules read it. Then course_status.py builds from that list and attaches module and tool counts as
attributes. The after page must be identical to the before page except for nothing; that is the test. List frames.csv
and calendar.csv under 4.5 as "generated but committed, gated by frame.py check".

### 6. The registry is described two ways that cannot both be true (major)

**Plan lines:** 4.2 "The registry (`data/registry.csv` ...) is generated from the files and CSVs by a script and
never edited by hand ... A retired object keeps its row with `replaced_by` set; an id is never reused"; 4.5
"Generated and not committed: ... the registry, the index".

**Found:** a file that is rebuilt from what exists and is not committed cannot remember an object whose file has gone
to the archive, an alias, or a `replaced_by`. The repository already has two small hand-kept files of exactly this
kind: data/redirects.csv (old url, new url; build_site.py:1050-1057) and data/modules/kept-ids.csv
(build_db.py:29-34).

**Why it matters:** the first retirement or merge after step 4 would silently lose its alias on the next rebuild,
which is the failure the registry exists to prevent.

**Change to the plan:** split it. `data/ids-retired.csv` (or `aliases.csv`): committed, append-only, hand or script
written, columns old_id, new_id or blank, date, reason. The registry: generated, not committed, built from the live
files plus that file. State the id key as `type` plus course plus local id (finding 2), since bare item ids repeat
across courses.

### 7. The 4.7 order should flip, and two sub-steps need splitting (major, order and size)

**Plan line:** 4.7 "4.4 and 4.3 first ... then 4.2 ... then the 4.1 leak cuts and migrations ... then 4.6".

**Found and recommended order:**
1. **Queue cleanup and the pilot decision** (finding 1). One commit, a few files. Removes a live hazard.
2. **The 4.1 cuts that need no index.** Each touches one or two scripts and is fully covered by a before and after
   run: units.csv (finding 8), the course list and course_status.py (finding 5), course_pages.py (finding 4), the
   skeletons reclassified (finding 9). One commit each. Doing these first means the index is not built over data
   that is about to go (60 units.csv rows, 2,763 skeleton files, the pilot).
3. **4.3 the index and `uses.py`, report only.** It writes nothing tracked, so it needs no before and after gates at
   all, only its own self-test. `leans_on` is nearly clean already: 20,789 entries in 2,107 files, 38 unresolved,
   and those are "when it exists:" entries that lesson.py:529 and :831 already police. The resolve gate can go live
   quickly, with "when it exists:" as the one allowed form.
4. **4.4 as a one-page rule plus the registry and retired-ids file** (findings 6 and 11).
5. **4.6 linter, small** (finding 11).
6. **4.2 ids:** only what survives finding 2.

**Sizes:** as written, 4.2 is one commit over 2,114 day files plus a prose-link pass. If any of it is kept, split by
course (22 courses have day files) so one gate run localizes a failure. The prose-link pass is far smaller than the
plan assumes: outside frontmatter there are 55 path mentions in 42 files under courses/, so "every day is touched
anyway" is not a reason to bundle it. "The 4.1 migrations" is three unrelated changes and must be three commits at
least.

**Gate coverage gap:** scripts/consolidation_gates.py:31-37 runs plan.py check, lesson_course.py, ledger.py check,
check_tools.py, check_safety.py, board.py, course_status.py and build_site.py. It does not run `unitplan.py check`,
`frame.py check`, `sequence.py`, `check_site.py`, `build_site.py --courses`, or the skeleton scripts' `--self-test`.
Step 4 changes exactly the things those cover (frames.csv, plan docs, course pages, skeletons). Add them to the gate
list before 4.1 starts. turn.py's own gate is `plan.py check` and `lesson.py check` compared by FAIL line
(turn.py:36, :91-96, :237-239): a change that only removes failure lines is safe for it.

### 8. units.csv is pilot-only and already produces 479 ignored failures; it cannot go "into frames.csv" (minor to fix, worth doing first)

**Plan lines:** 4.0 "data/units.csv (60 rows, the math-4 pilot) read by plan.py ... retired into frames.csv and
days.csv; plan.py reads those".

**Found:** data/units.csv has 59 rows, all math grade 4 (columns unit_id, subject, grade, order, title, days,
modules, status). plan.py:718-719 loads the rows for the course's subject and grade, :521 uses their day total to
allow hand-backs to days not yet planned, and :1008-1015 fails every section that has no row. Because only the pilot
has rows, every other course fails: 479 "is not in data/units.csv" lines across 21 courses in the last gate run
(docs/reviews/consolidation/step3-after/plan-*.txt), and scripts/lesson_course.py:19 and :51 exists to ignore
exactly that line. coverage_ledger.py:121-125 also reads it (tool side, guarded by an exists check). frames.csv is
one row per course written by `frame.py sync`, so it has no place for section rows. Each section's day count is
already derivable from days.csv (`unit` column), and its title lives in the section plan.

**Why it matters:** this is the cheapest real win in step 4, and it is a deletion, not a migration. Framing it as a
move into frames.csv invites a new column that frame.py sync would overwrite.

**Change to the plan:** "units.csv is deleted: plan.py drops the section-row check (:1008-1015) and takes the
hand-back horizon (:521) from the course's `days` in frames.csv; lesson_course.py drops KNOWN;
coverage_ledger.py's block goes; the file goes to the archive." Expect about 479 failure lines to disappear and
several `plan-<course>` gates to change exit code from 1 to 0; say so in the step report so the comparison is read
correctly. The units.csv `modules` column (pilot sections to tool modules) is tool-side data and is not carried over.

### 9. Skeletons are generated files; archive rows for them are waste, and coursegen.py barely reads them (minor)

**Plan lines:** ground rule 7 "`section-skeletons/` and `day-skeletons/` (required by coursegen.py)"; 4.0 "once its
plan or day passes, it goes to the archive and coursegen.py accepts the written file in its place".

**Found:** coursegen.py:286-290 only tests whether docs/courses/<course>/section-skeletons/ is a directory, to choose
the wording of a lead reminder. It never mentions day-skeletons. The real readers are the briefs:
docs/pipeline/briefs/section-write.md:13, section-lens.md:12, and docs/pipeline/kit/day.txt:7 and :36 (the day job
runs `day_skeleton.py` itself and may edit its skeletons). Both scripts say their output is deterministic and can be
rebuilt (day_skeleton.py:12-14, section_skeleton.py:6-8). 2,763 skeleton files are tracked in 20 folders.

A second home the 4.0 table misses: 917 written unit and section plans carry `<!-- skel -->` blocks, which are
copies of CSV data frozen at writing time. unitplan.py only strips them when counting words (:257, :340); no gate
compares them with the data. This is a different mechanism from the `<!-- gen: -->` tables of plan.py:1287-1302,
which today are used only by the pilot (22 files in docs/courses/math-4) and two history courses.

**Why it matters:** a hash-checked archive move with index rows for 2,763 files that one command rebuilds is cost
with no return. And "tables are generated, never typed" has two marker systems to reconcile, which the plan does not
size.

**Change to the plan:** class the skeleton folders as generated (4.5). When a section or day passes its gate the
sidecar is deleted with `git rm`, no archive row (git history keeps it, and the script rebuilds it). The briefs keep
working because a job regenerates what it needs. coursegen.py needs a one-line change at most. For the skel blocks:
add one line to the 4.0 row saying which marker wins (my suggestion: keep both for now, add a report-only check that
re-renders skel blocks and lists drift, and decide after seeing the count). Do not regenerate 917 plans in step 4.

### 10. Stripping item version suffixes costs more than it returns now (minor, over-building)

**Plan line:** 4.2 "An item's id is its stem without the version suffix (`s02-A6` for `s02-A6v2`)".

**Found:** 636 of 14,587 items carry a suffix (4.4 percent), in 7 of 24 courses: ELA grade 1 (198), kindergarten
(126), grade 3 (115), grade 2 (92), math-4 (90), world-history-i (13), science-grade-5 (2). Three spellings exist:
`s10-E2v2`, `s03-X42-v2`, `s06-P107-scale-v2`. In no file does the unsuffixed stem also exist, and no stem has more
than one version, so stripping is collision-free today. The suffixed ids are referenced in 473 files (day files,
plan docs, day skeletons, plan CSVs). No script mints or parses the suffix; it is a writer habit
(data/plans/README.md:36 shows it in an example).

**Why it matters:** safe, but it rewrites items.csv, wrongs.csv and several hundred day files to change 4 percent of
ids, most of them in drafts awaiting review, and 90 of them in the pilot.

**Change to the plan:** in step 4 do only the cheap half: a `version` column rule in data/plans/README.md ("a revised
item keeps its id; the version goes in the column"), a plan.py check that fails a new id ending in `v<digit>` unless
it is on a baseline list of the 636, and registry aliases. Strip the old ones when each course is next reviewed.

### 11. 4.4 and 4.6 should be thin (minor, over-building)

**Plan lines:** 4.4 "built now ... every later step of this plan runs through it"; 4.6 "one style check runs on
every file ... Built in this step"; "Sampled reads ... Designed here"; "Interchange later, shaped now".

**Found:** the house-rule load on curriculum files is light today: zero files under courses/ or docs/courses/
contain an em dash; unitplan.py:295 already fails one in plans. There is no generic batch-edit tool, and step 2
already produced one purpose-built mover (archive_move.py, per the step 2 report). The Codex review that sampled
reads would serve is paused. No school has asked for an export.

**Why it matters:** a workflow framework written before its first three real uses, and a linter over tens of
thousands of files, are the kind of build the plan itself warns about. Curriculum writing is the priority.

**Change to the plan:** 4.4 is one page in docs/ (request, `uses.py` list, script with `--dry-run` that prints a
diff summary, gates, log line) and no new code beyond what each migration needs; errata waits for a course that is
taught (ROADMAP.md:111 lists it as finished-course item 11, not yet a rule). 4.6 linter: one script with four checks
that are cheap and mechanical (em dash, "Curio Class" in full, a US spelling word list, the "no curriculum script
opens the tool catalog" import check), run on changed files inside turn.py's `end` and on everything in the
consolidation gate. Reading level, banned phrases, sampled reads and interchange field choices move to later.csv rows.

### 12. 4.5: the "out of date" gate will fail every day, and small count errors (minor)

**Plan lines:** 4.5 "Generated but committed: docs/COURSES-STATUS.md and docs/BUILD-BOARD.md ... A gate fails when
either is out of date"; ground rule 7 and 4.0 counts.

**Found:**
- course_status.py:209 stamps today's date into the page, so a byte comparison fails the day after any run. Both
  pages also change when a tool moves stage, which a curriculum job did not cause and may not fix (AGENTS.md: do
  only your job).
- Ground rule 7 says board.py and desk_stats.py read coverage.csv and data/concepts. They read
  data/tools-concepts.csv (board.py:92, desk_stats.py:37), which is not in the frozen list of 4.1. coverage.csv is
  read by catalog_compute.py, catalog_maps.py, coverage_ledger.py and shape_courses.py; data/concepts by
  check_concepts.py, apply_ideas.py, rename_tools.py and scripts/overlap/.
- The frozen list names modules.csv, but the source is data/modules/*.txt with kept-ids.csv; modules.csv is
  generated by build_db.py. docs/agents/catalog/shape/shape.csv (990 rows, read by course_status.py:34,
  tool_bins.py, shape_courses.py, spec_fixes.py) is the "shape files" and should be named by path.
- Counts are line counts with the header: modules.csv has 814 modules, coverage.csv 2,399 rows, units.csv 59,
  sequence.csv 797. There are 129 scripts now (115 in scripts/, 14 in subfolders) and 35 top-level docs after step 3.

**Change to the plan:** the two status pages are regenerated and committed by the lead at the end of a session or by
`turn.py end` (as `plan.py tables` already is, turn.py:232), with the date line left out of any comparison; no
failing gate. Correct the frozen list to: data/modules/ (source), modules.csv, tools-concepts.csv, sequence.csv,
coverage.csv, data/concepts/, docs/agents/catalog/shape/.

## Claims checked that held up

- **No curriculum gate reads the tool catalog.** plan.py, unitplan.py, lesson.py, lesson_course.py, coursegen.py,
  ledger.py, sequence.py, the three skeleton scripts, section_cuts.py and defaults.py contain no read of
  modules.csv, sequence.csv, coverage.csv, tools-concepts.csv, shape.csv or data/concepts. frame.py and
  plan_flow.py read data/courses.csv only.
- **The two leaks are the only two.** course_pages.py:300 and course_status.py:32-34 are the only curriculum-facing
  reads of modules.csv and shape.csv.
- **"About 30 scripts" read modules.csv:** 24 in scripts/ plus 6 in scripts/overlap/. sequence.csv is read by
  build_site.py and teaching_map.py only (the site Map).
- **plan.py reads data/units.csv** (plan.py:718), and the file is the math-4 pilot only.
- **build_db.py exists** and data/curioclass.db is its output (9 tables, tool catalog only).
- **Days have no `id:` yet;** every day file has frontmatter with a `version:` field. Note that `version:` is printed
  in page footers (lesson.py:2003, :2968) and read for "not ready" (lesson.py:529), so it is both status and print
  text when the "one status field" row is carried out.
- **Version-suffixed item ids exist** in the form the plan quotes, and stripping them is collision-free today.
- **`leans_on` works as an edge source:** 20,789 entries, 38 unresolved, all of the allowed "when it exists" kind.
- **`[[...]]` is already the house link syntax** (30,417 uses for items; `[[fig:id]]` and `[[note:id]]` prefixes at
  lesson.py:541-547), so `[[text:...]]` fits. lesson.py:547 must learn the new prefix in the same commit, as the
  plan says.
- **build/ is ignored and the site ships dist/;** the union merge rule and the sibling worktrees are gone (step 0
  to 3 reports, .gitignore).
- **The before and after gate runner exists** (scripts/consolidation_gates.py) and matches ground rule 3; its last
  run shows 103 gates at exit 0 and 25 at exit 1 as the baseline.
- **Skeleton scripts are deterministic and rebuildable,** as 4.0 implies.
- **The math-4 alias in frames.csv exists** (`legacy_plan_id`), and nothing published on the site or in the R2
  manifests uses the pilot course id (0 hits for `courses/math-4` in docs-manifest.txt, media-manifest.txt and
  redirects.csv).
