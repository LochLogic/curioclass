# Pause 4.E review (Fable, 2026-11-25)

Scope: sub-steps 4.A to 4.E as built (tag `pause-4e`, commit b4bc01898), the proposal
docs/reviews/consolidation/skel-copies-proposal.md, and 4.F to 4.K as planned. Read only: nothing in the repository was
changed except this file. Every number below came from a command I ran today; test copies and helper scripts lived in a
scratch folder outside the repository.

## Verdict: sound with changes

**In plain words.** The five steps built so far did what the plan said and broke nothing I could find: the course list,
the per-course ledgers and the row writer all check out against the real files. Three things in them need a fix before
any course is written again: old skeleton files are still sitting on disk where jobs will pick them up, two jobs
writing the same course's ledger at once can lose rows, and a few documents still describe the old layout. The proposal
to stop storing data copies in written plans is the right direction, but as drafted it would do two kinds of harm. The
plan checker reads those copies, so removing them makes 375 of 397 unit plans fail. And writers put real judgment
inside the marked blocks (how a standard splits across days, time budgets, one sensitivity note), which a mechanical
removal would delete. Most of the "drift" is not error at all: it is data that was added after the plan was written.
With a different sorting method, a third outcome for hand edits (move the judgment out of the block), the checker and
the public Front Office pages changed first, and a gate that proves every removed line can be rebuilt from data, the
removal is safe. It should run before 4.F, not after 4.G.

**How much of the drift is stale copy and how much is hand correction.** I re-rendered all 916 plans and compared line
by line (aligned by content, so a shifted block does not count twice). Of 63,244 block lines in plans, 7,760 differ from
a fresh render (12 percent); the fresh render also holds 27,365 lines the plans never had, nearly all of them data that
arrived at a later stage (item rows, source statuses, goal maps). I read 60 changed hunks drawn at random (30 unit
plans, 30 section plans) and traced four of them in git. Unit plans: 11 of 30 were hand edits inside the markers (8
carrying judgment, 2 real corrections or additions the data lacks, 1 set of writer-typed source rows). Section plans: 1
of 30 (a US spelling fix where days.csv still has the UK form). Weighted by hunk counts that is about 14 percent hand
edits among changed hunks, about 9 percent of all hunks; the rest are stale copies or data that came later. For the 236
drifted unit plans that have a clean generated baseline in git, a full three-way count gives 38 percent of differing
lines untouched since generation and 62 percent changed afterward, three quarters of those being source-map rows the
writer typed.

## Findings

### 1. The plan checker reads the blocks: removing them fails 375 of 397 unit plans (blocker for the sub-step as drafted)

**Evidence.** I wrote every plan with its blocks stripped to a scratch folder and ran `unitplan.check_file`,
`new_gates` and `check_section` on both versions. 375 of 397 unit plans gain failures, at least 8,200 new lines:
"code X not named in field 2" 3,915 (scripts/unitplan.py, the `# codes` check, reads all of field 2, and the code list
sits in a block), "source-map.csv row ... is not named in field 10" about 2,500, plus "has no stated weight", "does not
name the strand", "names no text set", "names no anchoring phenomenon", "performance expectation ... has no row".
Section plans: the header check at unitplan.py (`\*\*Days? (\d+)(?: to (\d+))?\.\*\*`) finds its line inside the Header
block that section_skeleton.py:226 to 238 writes. With blocks gone, 91 section plans gain a false "header says days"
failure (the pattern lands on another bold phrase) and the other 428 lose the check without a word. The proposal's
step 8 says only "word caps unchanged in effect".

**Change.** Before any block is removed, rewrite these checks in unitplan.py to read the data, or drop each check whose
only job was "the copy is present". Keep one header check that takes the section from the file name and days.csv. Run
the strip simulation again as the acceptance test: zero new unitplan lines.

### 2. Writers put judgment inside the markers; a mechanical removal deletes it (blocker for the sub-step as drafted)

**Evidence.** From the line compare: 212 standard lines in 36 unit plans carry the writer's own split of a standard
across days where the data says "Parts, by verb: whole standard" (for example docs/courses/math-grade-1/s07.md,
"(a) distinguish defining from non-defining attributes, days 131 and 133 to 134; (b) ..."; math-grade-2/s04.md). At
least 40 "Time" lines in 26 unit plans hold a writer's minute budget in place of the generated sentence
(chemistry/s10.md, physics/s09.md). Writers replaced whole generated lines with their own ("Reused evidence:",
"Record allocation:" in english-language-arts-grade-12/s08.md and grade-6/s03.md). One line is a sensitivity note that
exists nowhere else: english-language-arts-grade-11/s09.md:281, "Franklin's satire contains a Native slur (in XIX) that
is omitted with a disclosed mark and never voiced", added inside the block in commit c8c45a5b4; `git log -S` finds it
in no data file and not in frame.md. One is a correction of the generator: english-language-arts-grade-3/s04.md says
"(continued from unit 1)" where the baseline skeleton (32380c382) and today's render both say "(begun here; unit 2
completes it (day 136 note))".

**Change.** Proposal step 2 needs three outcomes, not two: back-port to data (a fact the data has wrong or lacks), move
out of the markers into the plan's prose (judgment), or discard (a mistake). Parts splits and time budgets are
judgment and move to prose in the same field. The sensitivity note goes to the frame. Nothing leaves a block until its
line has one of the three marks.

### 3. Stale skeletons are still on disk, and jobs will reuse them (should fix, before any course run)

**Evidence.** 4.E untracked 2,763 files but left them on disk (27 section-skeleton folders, 23 day-skeleton folders).
Both generators refuse to overwrite: scripts/day_skeleton.py:546 and scripts/section_skeleton.py:512 return "kept
(exists; --force to rebuild)". docs/pipeline/kit/day.txt:7 runs `day_skeleton.py {COURSE} u{UNIT}` with no `--force`,
and the same file now tells jobs to "fix the data and rerun day_skeleton.py", which keeps the old file. coursegen.py:286
to 290 asks the lead to build section skeletons only when the folder is missing; when it exists it prints "check
section skeletons are current". I rendered science-grade-2 to a scratch folder: 16 of 16 section skeletons and 10 of 10
unit 1 day skeletons on disk differ from a fresh render. The files are now ignored, so git no longer shows that they
are old.

**Change.** Delete the on-disk skeleton folders now (history and `pre-step4` keep them). Make an ignored sidecar always
rebuild: drop the keep rule, or put `--force` in day.txt. Have section.txt build its own skeletons at job start, as
day.txt does, and have coursegen always emit the build line. One kit version bump.

### 4. Two jobs writing one course's ledger at once can lose rows (should fix, before 4.G allows side-by-side work)

**Evidence.** Before 4.D, `ledger.py add` appended one line. Now `_append` (scripts/ledger.py:108) reads the whole
course file and rewrites it through a fixed temp name, `ledger.csv.tmp`, with no lock; scripts/rows.py does the same
with `<table>.csv.tmp`. docs/pipeline/kit/common.txt:11 says "Other agents work in other units and courses at the same
time", so two jobs in one course is normal. Stress test in a scratch folder (LEDGER_DIR set, six processes, 40 adds
each): 191 adds crashed with PermissionError, 49 printed "added", 38 rows were in the file, so 11 rows were reported
written and lost. A gentler test (24 separate commands at once) lost none; the window is small but real.

**Change.** A lock file per target (create with O_EXCL, retry for a few seconds, clear a lock older than a minute), a
temp name unique to the process, and a retry on PermissionError, in one shared helper used by ledger.py and rows.py.
Add the race test to the self-tests. Until then AGENTS.md must not say side-by-side work in one course is safe.

### 5. The public Front Office pages show the block contents (should fix; the proposal lists this as unknown)

**Evidence.** scripts/front_office_docs.py:110 removes the marker comments and keeps what is between them;
build_site.py:1018 to 1021 builds the Front Office on every build. In build/gates/step4-E/dist/front-office/docs/
algebra-ii/u05.json I found the block text "Identify the effect on the graph of replacing", "Weight: supporting
(S-ID.B, F-BF.A)" and "Builds on (progression, assumes):". So stale copies ship on the live draft pages today, and
removing blocks changes those pages.

**Change.** Decide what a Front Office unit page shows once blocks are gone. My pick: one function renders a plan's
facts from data, used by the skeletons, by the writer's read view (proposal step 5) and by front_office_docs.py, so the
public page shows current facts beside the prose. Gate: build the site into scratch before and after and diff
front-office/docs/*.json; every changed line is explained.

### 6. Section blocks are partly copies of unit plan prose, and most section drift is data that came later (should fix)

**Evidence.** scripts/section_skeleton.py:269 (field 2 lines), :314 to :349 (field 5 assessment rows and goal map),
:369 to :382 (field 6 error register), :397 to :404 (field 8) and :486 to :501 (U3 to U11) quote the written unit plan
inside the markers. So the proposal's step 3 ("take those facts from data directly, since the blocks were rendered
from data") cannot apply to them: their owner is the unit plan, and section_skeleton must keep reading it. Two causes
are missing from the proposal's list: (d) the unit plan was edited after the section skeleton was cut
(algebra-ii/u01-1.md quotes "count 435 of 550 minutes, 79.09 percent"; the unit plan now says 465 and 84.55), and (e)
the pipeline order itself: items.csv rows, source statuses, credits and goal maps are written after the section plan,
so its block could never have held them. Of 90,510 fresh section lines, 23,777 are additions of this kind; in my
sample 29 of 30 changed section hunks were (d), (e) or later data edits.

**Change.** Add causes (d) and (e) to the sort. In the report to Cory, count "later data" apart from "stale", so the
headline number is the hand edits, not 860 of 916.

### 7. More readers and writers of the blocks than the proposal lists (should fix)

**Evidence.** Verified readers the proposal has: section_skeleton.py `field()` (:42), day_skeleton.py `unit_field()`
(:182), unitplan.py (:257, :340), unit_skeleton.py (:64). Missed:

- scripts/unitplan.py content checks (finding 1).
- scripts/front_office_docs.py:110 and :174 (finding 5).
- scripts/plan.py:1326 to 1329: the unit packet prints each plan whole for day writers, blocks included; :1117 to 1120
  counts plan words with only `gen:` tables removed.
- scripts/section_cuts.py:79 to 90 and :212 to 227: reads the plan header and rewrites its "Sections: ... Days by kind"
  line from days.csv, a data copy outside the markers.
- scripts/codex_units.py:75 and scripts/codex_unit_loop.py:107: run unit_skeleton.py to make sNN.md itself, so every
  new unit plan starts life with the markers in it. This is how blocks get into plans.
- scripts/goalmap.py:36 to 60 reads plan tables (writer tables; not affected, listed for completeness).
- Briefs and formats: docs/pipeline/briefs/section-write.md:13 ("Every line between `<!-- skel -->` markers is ..."),
  section-lens.md:12, docs/pipeline/kit/section.txt:3, docs/courses/UNIT-PLAN.md:311 and :324, docs/PRODUCTION-PATH.md
  :237 to 244.
- Not readers (checked): build_site.py other than through the Front Office, course_pages.py, lesson.py, course_status.py
  and plan_flow.py (they test that plan files exist), desk_*.py.

**Change.** The sub-step's reader list becomes this list. unit_skeleton.py must write a sidecar (as the section and
day generators do) instead of the plan file, or new plans will bring the markers back the next day. The briefs, the
blank copies in UNIT-PLAN.md and the kit change in the same commit as the strip.

### 8. Sorting causes from git history works for some plans only; sort by content instead (should fix)

**Evidence.** What holds: the 259 science, ELA and math unit plans were first committed as raw skeletons (32380c382,
"Unit skeletons for science, ELA and math (259 units)"; `TODO(writer)` present), so a clean baseline exists; 236 of the
drifted ones have it. The step 2 merge is `--no-ff`, and `git log --follow` and `git log -S` work across it (I used
both). What does not hold: the 138 social studies unit plans were first committed already written (0c571de6a, no TODO
lines), so 753 differing lines have no baseline. Blocks were re-rendered in place by script at least once (8dd354eed,
"regenerate 183 plans"), so blame on a block line mixes script and hand. Writing commits are bulk (80cd1a297 holds 11
courses), so a commit message never says which line was a hand edit. Section skeleton sidecars are in history up to
`pre-step4`, usually in the same commit as the plan (5dd703388), which gives section plans a baseline too.

**Change.** Replace proposal step 1 (`git log -L` or blame) with a content sort, per differing plan line:
1. the line is in today's fresh render: fine;
2. it is in the baseline (the first-commit skeleton for unit plans, the sidecar at the plan's writing commit for
   section plans), or `git log -S` finds its changed part in the history of the data files or the generator: stale
   copy, data wins;
3. it quotes unit plan prose (finding 6): owner is the unit plan, no action;
4. anything else: a hand edit, onto the review list with the three outcomes of finding 2.
Social studies unit plans take path 2 by pickaxe only, so expect a longer review list there.

### 9. The sub-step belongs before 4.F, not after 4.G (should fix)

**Evidence.** The plan's own rule in 4.K is "E before F, so the index never sees 2,763 files that are about to go";
the same holds for block text. Section blocks hold item links (`- [[s01-X1]] day 1 (exit)`, section_skeleton.py:352)
and thousands of day mentions, so the 4.F soft edges and the resolve and orphans baselines would be built on copies
and then change. 4.F's fifth report, `drift`, is this problem. 4.G stores gate baselines, and finding 1 shows 375 unit
plans move. Writing restarts when 4.G closes, and the first course run would add blocks to every new plan unless the
generators and briefs have already changed.

**Change.** Run it now as its own sub-step (4.E2 in the outline below), with a full gate run before and after, since
it is a data move under ground rule 3.

### 10. The proposal names no gate that proves nothing was lost (should fix)

**Change.** Three checks, all mechanical:
1. **Before the strip:** a "plan lines not in the fresh render" count, by plan, must be zero except lines on the
   signed review list. Then every removed line can be rebuilt from data, which is the proof. skel_drift.py needs a
   line-level mode aligned by content for this; its block-by-position compare counts shifted blocks twice (the census
   says so).
2. **The strip commit:** a script confirms that each file equals its old version with the marked spans removed and
   nothing else (text outside the markers byte for byte, apart from lines moved out under finding 2, which are listed).
3. **After:** unitplan, plan and lesson gates with no new lines; section and day skeletons rendered to scratch before
   and after, differences explained; the Front Office JSON diff of finding 5; then the guard: any `<!-- skel -->` in a
   written plan fails.

### 11. The ledger's course ladder is still a constant in ledger.py (should fix)

**Evidence.** The plan for 4.D says ledger.py takes a subject's courses from the course list. scripts/ledger.py:62 to
72 still holds `LADDER` by hand: social studies stops at grade 5, math lacks statistics and calculus, science lacks
earth-and-space-science and environmental-science. `add` refuses any course not on it (:125), and
scripts/consolidation_gates.py:47 checks four subject names typed in the runner. The same course-to-subject fact also
lives in coursegen.py:36, front_office.py:171 and plan_flow.py:338.

**Change.** Build LADDER from data/plans/course-list.csv (subject, then list order) in 4.F or the shared module of 4.H,
and have the gate glob data/plans/*/ledger.csv so no ledger file can sit unchecked.

### 12. The gate runner's compare can miss a break (should fix, in 4.G)

**Evidence.** scripts/consolidation_gates.py `compare` prints only lines new in the after run. A gate that prints
less, changes exit code or disappears is not flagged, and output is cut at 40 lines a gate (:117). `NOISE` (:33) drops
any line holding "took " or "elapsed". lesson_course.py exits 0 always (its own header), so "26 known non-zero gates"
says nothing about lesson failures. Summary lines carry counts, so every data change shows as "new lines" that are
only lower counts (22 in step4-C/compare-step4-before.txt); a reader learns to skim them. Not in the runner:
`rows.py --self-test`, the whole `lesson.py check` that AGENTS.md names as the gate, `front_office.py check`. The
`p.name != 'ledgers'` test at :38 is a leftover.

**Change.** In gate.py: compare exit codes and the set of gates, parse the count lines (a count that rises is the
failure, a count that falls is reported once), no line cap in the stored compare, and add the missing self-tests.

### 13. Leftovers of 4.B in live documents and one script (should fix)

**Evidence.** docs/pipeline/kit/draft-fix.txt:3 still tells jobs that "section ... not in data/units.csv" is known and
to ignore it. data/plans/README.md:58 lists a units.csv mismatch as a failure plan.py reports. scripts/
coverage_ledger.py:178 still prints "data/units.csv holds the units and only live ones count" into the measure table,
and `unit_days` (:121) is now always empty, so its column is dead. data/plans/later.csv L71 is still open and asks for
new units.csv rows. docs/GLOSSARY.md:38 names the file. Twelve briefs name it in blind lists (the 4.B commit says
data/homes.csv replaces those in 4.H). Two side effects: `frame.meta('math-4')` now returns the math-grade-4 frame
through `legacy_plan_id` (scripts/frame.py:645), so the pilot's hand-back horizon is 160 days from a frame it was never
planned against; and the check "section N: units.csv says X days, days.csv has N" went with no replacement (it only
ever ran on the pilot).

**Change.** Fix draft-fix.txt and README.md now, close L71, and add the blind lists by name to the 4.H task list so
they are not forgotten.

### 14. The state documents do not say where the work stands (should fix)

**Evidence.** docs/HANDOFF.md:9 and docs/CONSOLIDATION-PLAN.md:3 to 4 both say step 4 "has not started" and waits for
Cory's go. The plan's 4.E still says "No plans are regenerated in step 4", which Cory's choice replaces. `git grep
q-skel-drift` finds the card only in step4-E/skel-drift.md: the decision is not in docs/agents/decisions/
DESK-ANSWERS.md, which AGENTS.md requires. data/plans/README.md has no line for `<course>/ledger.csv`. The tree at
`pause-4e` shows one untracked file, the proposal itself.

**Change.** One commit: plan status line and 4.E text, HANDOFF line, the decision log entry, the README line, and the
proposal (or its successor) tracked.

### 15. rows.py holds up on every real file; a few edges to close (nice to have)

**Evidence.** I ran `rows.records` over all 339 CSVs under data/plans: every file parses to the same records as
Python's csv reader and joins back byte for byte. Five files mix line endings (math-4/parts.csv, math-4/words.csv,
social-studies-grade-2/parts.csv and source-map.csv, flow-status.csv); rows.py writes the header's ending, which is
safe. Edges, none present today: a lone quote mark inside an unquoted field makes the splitter join two records;
`str.splitlines` also splits on U+2028 and form feed; a UTF-8 byte order mark would make every column "not in the
header". The command does not refuse `ledger` as a table or a table name with `..` in it, has no delete, and a value
with a line break is awkward to pass on a command line. Only common.txt points at it; no brief in
docs/pipeline/briefs does.

**Change.** Refuse `ledger` and path separators, add `rows.py delete` and a `--value-file` option, split on `\n` only,
and add a `rows.py check` (records equal the csv reader's, one line ending) to the gates.

### 16. 4.C: small departures from the plan, all workable (nice to have)

**Evidence.** course_status.py still places courses from the tool catalog first and then joins the list by
`catalog_key`, with assertions both ways; the plan said the list comes first. course-list.csv has five columns the plan
did not name (catalog_key, rows, weeks, pins, legacy_plan_id). The list passes my checks: 120 rows, no duplicate id or
catalog_key, 118 active and 2 shelved, 58 with `rows`, all 58 frames in the list. Pins and weeks moved to the list
rather than being parsed from the frame's Days bullet; the commit says each frame still names its pin in prose, and I
found no check that the two agree. docs/courses holds ten subject-level folders that are not courses (arts,
career-education, computer-science, eld, health, library, physical-education, sel, social-studies, world-languages)
beside math-4. docs/courses/math-4-spine.md stayed (the commit says why).

**Change.** Name the extra columns in the fact map. Give the subject folders a row in data/homes.csv so the layout
report does not flag them. Either drop pins from frame prose or add a frame.py check that they agree.

### 17. The 4.E census note is wrong on one point, and one spelling fix was free (nice to have)

**Evidence.** skel-drift.md says day_skeleton.py could be fixed because "day skeletons are not copied into plans". But
section_skeleton.py:420 prints `dk.KIND_MEANS`, so the 4.E fix changed section blocks: plans say "Practises what
earlier days taught", the render now says "Practices" (the phrase is in 78 plan files). section_skeleton.py:456
"practised" is on a writer TODO line, outside any block, and could have been fixed with no drift.

**Change.** None needed once blocks are removed; fix all three generators in the strip commit.

### 18. Two data copies sit outside the markers and are already gated (nice to have)

**Evidence.** Every unit plan has a header line ("Days 96 to 109 ... Sections: ... Days by kind: ...") and a closing
"## Day list (from days.csv, do not edit)" (unit_skeleton.py:2075). unitplan.py:150 to 161 fails a plan whose day list
or header disagrees with days.csv, and section_cuts.py re-syncs the header. These are copies too, but they cannot
drift without a failure. AGENTS.md also describes `<!-- gen:... -->` tables as the standing mechanism; only 24 files
use them (22 in the math-4 pilot, us-history-i and world-history-i).

**Change.** Decide once: either these two stay as the only allowed in-file copies, listed in data/homes.csv as
"generated in place, gated", or they go with the blocks. Staying is cheaper and loses nothing. Reword the AGENTS.md
line on `gen:` tables in 4.G.

## Revised outline for the skel-copies sub-step (4.E2, before 4.F)

0. **Clean up 4.E first** (finding 3): delete on-disk skeleton folders, sidecars always rebuild, kit version 5.
1. **Line-level census.** Extend skel_drift.py to compare by content and to sort each differing plan line by the four
   paths of finding 8. Output: counts by cause (later data, stale, unit plan prose, hand) and the hand list.
2. **Stop for Cory** with the hand list, each line pre-marked back-port, move to prose, or discard. Expect roughly 500
   to 900 lines outside source-map rows, plus the source-map rows as one mechanical check (plan decision equals
   source-map.csv `decision`).
3. **Apply the list.** Back-ports through rows.py (and the frame or standards files by hand, listed); moves to prose
   by script, one commit, word caps rechecked.
4. **Change the readers** (finding 7): unitplan.py checks read data; unit_skeleton.py writes a sidecar; one
   `plan_facts` renderer shared by the skeletons, the writer's read view and the Front Office; plan.py's unit packet
   prints facts from data plus prose; section_skeleton.py keeps reading unit plan prose.
5. **Prove, then strip** (finding 10): the zero count, the strip commit with its byte check, the three after-checks.
6. **Briefs, UNIT-PLAN.md blank copies, kit** changed in the strip commit; generators' UK spellings fixed.
7. **Guard:** a marker in a written plan fails the gate; skel_drift.py is retired.
8. Full gate run and compare, as after any data move.

## Changes to 4.F to 4.K

- **4.F.** Runs after 4.E2. The `drift` report becomes the marker guard plus a check of the two gated in-file copies
  (finding 18). index.py reads ledgers by globbing course folders and takes subjects from course-list.csv (finding 11).
  It must skip the math-4 pilot by name and treat the ten subject folders under docs/courses as known (finding 16).
- **4.G.** gate.py takes the compare fixes of finding 12 and the new self-tests. The locking helper of finding 4 lands
  here at the latest, before AGENTS.md says side-by-side work is allowed; the sentence should say "different courses",
  or "one course" only once the lock exists, and common.txt:11 must agree with it. The kit's `{PLANGATE}` and
  `{LESSONGATE}` (coursegen.py:42 to 44, still an unfiltered run piped through awk) become `gate.py --course`.
  draft-fix.txt loses its units.csv line (finding 13).
- **4.H.** data/homes.csv gains rows for plan prose ("no data copies; marker guard"), skeleton sidecars (generated,
  ignored, always rebuilt), the subject folders, and the two gated in-file copies. The twelve brief blind lists that
  name data/units.csv are replaced here, as the 4.B commit promised. The shared module for subject ids absorbs LADDER,
  coursegen.SUBJECTS, plan_flow.PFILE and the mapping in front_office.py:171.
- **4.I.** No change in design. It depends on findings 4 and 11: "day uses word" comes from ledger term rows, so the
  ledger must be safe to write and must cover every course before the word reports mean anything.
- **4.J.** Goal test 3 names "the `drift` report (skel blocks)"; reword it to the marker guard count, which should
  print 0.
- **4.K.** Order becomes A, B, C, D, E, E2, F, G, H, I, J. E2 before F for the same reason E is before F. The state
  documents (finding 14) are brought up to date before E2 starts.

## Checked and found sound

- 4.A: the runner builds the site into build/gates/<step>/dist with `--library --closet --courses` and never touches
  dist/; raw output is ignored; jobs.csv holds only its header; later.csv has L114 to L121.
- 4.B: plan.py, lesson_course.py, coverage_ledger.py and codex_scopes.py no longer read the file; the 958 lines went as
  forecast.
- 4.C: course-list.csv is consistent with frames.csv and with every course folder under data/plans and courses/.
- 4.D: `rows.py --self-test` passes; `ledger.py check math` runs clean on the split files; no script or brief still
  reads data/plans/ledgers/ (the three mentions left are dated records).
- 4.E: .gitignore holds both patterns; coursegen's folder test already handles a missing folder; skel_drift.py writes
  nothing and rendered all 916 plans without an error, and my rerun on three courses matched its method.
- Gate history: step4-D and step4-E compares show one new line each, the build path.
