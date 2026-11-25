# Step 4 full review (Fable, second read, 2026-11-25)

Scope: docs/CONSOLIDATION-PLAN.md draft 4 at commit 073f1e63d: the end goal and its 12 tests, the Word Wall
section, step 4 (4.0 to 4.13), how it sets up steps 5 and 6, the ground rules and the decisions. Read-only. Nothing
in the repository was edited, no gate, build or sync was run, and Gemini/Api.txt was not touched. Helper scripts and
one scratch skeleton render are in this folder (words.py, fm.py, orph.py, dangle.py, skel/). Counts are from those
scripts or from greps, and each says how it was made. Heuristic counts (regex over prose) are marked "about".

## Verdict

**On the right path, with changes.**

The core design is the right one for this project and should not be swapped: plain CSV and markdown in git as the
only source, with a generated index for "what uses this?". Every alternative I weighed loses something Curio Class
depends on (diffs Cory can read on GitHub, agents that read and write with file tools, a free host, no server). The
first Fable read was folded in correctly, with one gap (skeleton edits, finding 10). But draft 4 has four real
weaknesses, and they are not small:

1. **The words design (4.9 and the Word Wall conversion) is the weakest part of the plan.** The curriculum already
   keeps vocabulary in four places that 4.9 does not name, the proposed key collides on 432 of 3,769 keys in today's
   cards, and the conversion step would rebuild a live product, with pictures, Spanish and five consumers, from a
   table that has none of those columns.
2. **The plan makes things cheap to find and change, but not cheap to check.** The gates run over every course on
   every job, the hooks step 4 adds sit in `turn.py end`, which the real course runs do not use, and the gate runner
   overwrites the deploy folder.
3. **Several second homes and unowned piles are missed:** the per-subject ledger files (shared, rewritten whole, no
   lock), course identity (three id systems), day numbers in prose (about 140,000 mentions), docs/reviews (4,924
   files and the fastest growing folder), and 5,762 "pieces" that have no row in the fact map.
4. **Four of the 12 tests have no sub-step that builds them.**

Fix those, merge a few sub-steps, relax two ground rules, and step 4 is smaller than draft 4 and reaches the goal
more surely.

## Design alternatives considered

Judged for this project: agents write most content, hobby pacing, a free static host, review by git diff, Cory reads
on GitHub.

| Design | For | Against | Call |
|---|---|---|---|
| **The plan: CSV and markdown sources, generated index** | Diffs and blame work. Agents filter a CSV by day with ten lines of Python. Nothing to host. 59 courses of data and 3,471 lines of lesson.py already work this way | CSV edits by agents are fragile (the kit records two accidents, docs/pipeline/kit/common.txt:3); big shared files do not merge; relations need the index | **Keep** |
| **SQLite (or any database) as the source of truth** | Real keys, real joins, constraints | A binary file: no diff, no GitHub reading, no merge, every agent edit needs SQL and a lock. Loses git review, which is the only review there is | Reject as source. **Use it as the generated index** (finding 16) |
| **One record file per object** (a file per item, per ledger row, per word) | No shared file to collide on; trivially flat | 14,587 items, 34,173 ledger rows and 8,564 day rows today become about 57,000 files, about 570,000 at tenfold. GitHub lists 1,000 entries a folder. Agents would open hundreds of files to plan one unit | Reject. Days and pieces are already one file each, which is the right grain |
| **Frontmatter as the only source** (a day file carries its own plan row and items) | One file per day holds everything; no id joins | 6,457 of 8,564 planned days have no file yet, and the plan stage needs the table before the file. Course-wide checks (coverage, sequence, hand-backs) want tables. A rewrite of plan.py, lesson.py and the kit | Reject now. Take its one real lesson: agents should write CSV rows through a safe upsert command, not by hand |
| **Per-course files only, no shared tables** | Fits "three homes per course"; parallel agents never share a file | Cross-course reads need a loader | **Adopt for the ledgers** (finding 5). Keep the small cross-course tables |

So: the same design, with the index in SQLite, the ledgers split per course, and one safe way to write rows.

## Findings

### 1. The curriculum already has four homes for vocabulary; 4.9 adds a fifth and misses the one that matters (major)

**Concerns:** 4.0 row "No home for word definitions in the curriculum", 4.9, the fact map row "Words", the Word Wall
section ("the terms the ledgers already record as introduced").

**Found:**
- **The ledgers.** data/plans/ledgers/*.csv hold 13,484 `term` rows (science 3,309, ELA 4,267, math 3,499, social
  studies 2,409). Each has course, section, day, the word and a `note` that is the meaning as taught, for example
  `science-kindergarten,u01-1,,term,push,a hand moves an object away from itself,planned`. 6,379 are at stage
  `written` and every one of those names its day. ledger.py:40 defines the kind: "term: a word students are taught
  to use". This is already the "day teaches word" edge, with a working definition, for every written day.
- **The progressions.** data/progressions/*.csv have a `words` column: 19,768 entries, 7,727 distinct, per skill and
  grade (science.csv row sk-push-pull: "push; pull; strong; gentle; direction; move; stop; roll").
- **Per-course word lists.** data/plans/<course>/wordlist.csv in 6 ELA courses, 1,025 rows (unit, word, text_id,
  week, when), asked of the writer by unit_skeleton.py:862.
- **The Word Wall cards.** 4,413 cards, 3,108 distinct words. 1,394 of those words also appear as ledger terms.
- **A name collision.** data/plans/<course>/words.csv already exists in 12 courses and means something else: a list
  of banned patterns (`pattern,use,reason`). A shared `data/plans/words.csv` beside twelve
  `data/plans/<course>/words.csv` files of a different shape is the opposite of "one shape".

**Why it matters:** 4.9 asks writers to mark words by hand in day files so the index can learn which day uses which
word. The ledger already knows, for 6,379 rows, without touching a day. A hand mark is then a second home for the
same edge, and 2,107 existing days would need a marking pass to catch up. Worse, the ledger `note` and the new
`definition` are two hand-kept statements of what a word means in a course, and nothing ties them.

**Change:**
- State the chain once, in the fact map: progression `words` (planned, by skill) to ledger `term` row (introduced,
  by course and day, teacher-facing meaning) to the word table (student-facing definition, by sense and band).
- The index builds "day uses word" edges **from the ledger term rows first**. `[[word:...]]` is then only a display
  anchor (where on the page the word lights up), and lint checks that a marked word has a ledger term row in that
  course. The "marked but undefined" backlog becomes "introduced in the ledger but undefined", which exists today
  with no marks at all.
- Print first. Curio Class days are print pages. A "words today" box on the student sheet can be drawn from the
  day's ledger terms with no inline marks, so the popup design can wait without blocking the feature.
- Name the file anything but words.csv (for example `data/plans/vocabulary.csv`), and fold wordlist.csv into the
  design card q-word-names-1 as a third thing to name.

### 2. The key "word plus grade band" collides today (major)

**Concerns:** 4.9 "Key: word plus grade band".

**Found (words.py over data/closet/words and data/modules.csv, read-only):** the 4,413 cards make 3,769 distinct
(word, band) pairs with the bands check_words.py:29 uses. **479 pairs hold more than one card, and 432 of them have
differing definitions.** 256 of those cross subject files. Some are true second senses: `soft` in K to 2 is "a
quiet sound" (science, arts) and "not hard; nice to touch" (ELD); `family` is "a group of instruments that make
sound the same way" (arts) and "people who love and care for each other" (social studies); `balance` in 6 to 8 is
visual weight and also ensemble volume. Others are the same sense worded twice (`warm colors`, `tempo`), which is
exactly the duplication one table should remove. 4.9 itself names `table` and `cell` as two-meaning words, as a
reason not to highlight by machine, but then keys the table as if a word had one meaning per band. Also,
lesson.py:48-51 only matches `[A-Za-z0-9-]+` inside brackets, and 4.9 gives no rule for a phrase ("balanced
forces", "life cycle") or an inflected form ("forces" in the sentence, "force" in the table).

**Why it matters:** with this key the conversion script must drop or merge 432 definitions by guess, and the first
writer who needs the second sense of `cell` has no way to say which.

**Change:** key the table by a **sense id plus band**. The sense id is a slug, with a short tag only when a second
sense exists (`cell`, `cell-biology`; `table`, `table-data`). Columns: sense id, word as shown, band, definition,
then the rest. The link is `[[word:<sense id>]]` with an optional shown form, `[[word:force|forces]]`. Take the
bands from data/bands.csv (k2, 35, 68, 912), which is what check_words.py already caps definitions by (DEF_CAP,
check_words.py:21), and write the band function once (finding 13). State what a course that spans bands does.

### 3. The Word Wall conversion rebuilds a live product from a thinner table, and is placed too early (major)

**Concerns:** "The Word Wall, rebuilt from the curriculum"; the "How we get there" row; 4.9 last bullet; the
never-touch rule.

**What the code does today:**
- Source: data/closet/words/<subject>.txt, 12 files, pipe-separated, one card a line:
  `module_id|word|definition|example|picture|es_word|es_definition|es_example` (check_words.py:6, :19). All 4,413
  cards have Spanish. 2,291 pictures are `svg:` diagrams drawn by wordsvg.py from data/closet/words/diagrams.py
  (4,595 lines), 1,558 are paintings, 564 have none. Art is closet/words/art/<module_id>/<slug>.webp, 3,849 tracked
  files, served from R2 by the Worker (wrangler.jsonc `run_worker_first: "/topics/*/words/art/*"`; 3,848 lines of
  data/media-manifest.txt).
- build_site.py loads cards only with `--closet` (:336) and stops the build on a bad list (:338-340). Consumers:
  1. /topics/<id>/words/, one print page per topic with five formats and three languages, plus a CSV download
     (:488-506). 762 topics have cards.
  2. /closet/word-wall/ and one page per grade, band and language (:590-654), grouped by module grade.
  3. the topic hub page (:479-485), 4. the Sub Day packet of each tool (:533), 5. the worksheet generators' word
     bank, closet/worksheets/make/words.json (:718-723).
- It is live: docs/SUPPLY-CLOSET-PLAN.md:4 says the words went live 2026-10-27 and deploy builds use
  `--library --closet`.

**Found against the plan:**
- The proposed table has word, band, definition, fun fact, source, status, from. It has no example, no picture, no
  Spanish and no topic. Converting "each old card into a row" loses five of eight card fields, or the table grows
  them and stops being a simple definition list.
- "Assigns a grade band from the topic's grade": 1,493 cards (34 percent) sit on modules whose grade is a span
  (6-8, 9-12, k-12). Those all go to the review list.
- "A word is on a grade's wall because a day teaches it": 1,433 cards (32 percent) are in subjects with no day
  written and none planned soon (arts 395, computer science 364, health and PE 184, ELD 130, world languages 120,
  CTE 109, library 73, SEL 58). Under the new rule those live walls empty out.
- Art and R2 keys are by module id. The plan archives data/closet/words but says nothing about closet/words/art,
  diagrams.py, the manifest (a never-touch state file) or the four other consumers.
- The plan calls this "the same leak as the course list". It is not. Nothing in the curriculum reads
  data/closet/words (the only readers are build_site.py, the check_words scripts and the word art scripts). It is a
  tool-side product keyed by tool-side ids, as designed, and it sits inside the frozen catalog.
- The consolidation gate builds the site with no flags (consolidation_gates.py:36), so no gate run has ever built a
  Word Wall page. "The before and after pages are compared" has no gate under it today (finding 8).

**Why it matters:** this is the only step in the plan that edits a live, public, finished feature, it is scheduled
while the tool catalog is frozen, and its stated benefit (writers find definitions waiting) does not need it.

**Change:**
- **Do not lift the never-touch rule.** Reading is not touching. A one-time, read-only import copies each card's
  word and definition into the word table as candidate rows (`status: from the Word Wall, unread`, `from:` file and
  topic), with collisions and span grades sent to a review list. data/closet/words stays the frozen source of the
  live Word Wall, so there is no second hand-kept home: one side cannot change.
- **Move the real conversion** to the stage the plan already has for this kind of work: "After the curriculum is
  done: the tool catalog retired; topic pages, coverage and standards pages become views over the index". The Word
  Wall by topic is a topic page. It converts with them, when topics themselves are redrawn from the curriculum.
- When it does convert, the table is not the whole card. Keep pictures, examples and Spanish as their own tables
  keyed by sense id (one fact each), and plan the R2 key move as part of sync_media.py's work.

### 4. Two job systems, and the hooks step 4 adds sit in the one that is not used (major)

**Concerns:** AGENTS.md "Taking a turn"; 4.2; 4.11 "runs on changed files in `turn.py end`"; 4.12 "regenerated ...
by `turn.py end`"; test 7 "one command per job".

**Found:**
- data/pipeline/jobs.csv was last changed on 2026-11-12 (git log). All 33 rows are the math-4 pilot.
- Every course run since 2026-11-20 comes from scripts/coursegen.py, which writes numbered job files and a
  queue.txt into an `--out` folder (coursegen.py:1-20), not jobs.csv. Its kit says the opposite of AGENTS.md:
  docs/pipeline/kit/common.txt:1 "No git commands at all", :11 "Other agents work in other units and courses at the
  same time", :9 "the lead re-runs the filtered gates after you". AGENTS.md says "Never two at once" and "Every job
  runs inside a turn". The Codex draft run used a third runner (codex_draft.py).
- `turn.py end` runs `plan.py check` and `lesson.py check` with no course (turn.py:36, :91-96): every course,
  twice a job (once at start for the base, once at end), then `lesson.py build --pdf` for everything (turn.py:240).
  lesson_course.py:4-6 exists because "the full check prints every day of every course through Chrome". At tenfold
  the turn gate does not finish in useful time.
- The base failure list is stored in data/pipeline/turn.json and committed. The baseline is about 6,000 FAIL lines
  today (math-kindergarten alone prints 4,425, docs/reviews/consolidation/step3-after/summary.csv).

**Why it matters:** 4.2 empties the queue but leaves AGENTS.md describing a mechanism the runs do not use. The
linter and the status-page refresh that 4.11 and 4.12 hang on `turn.py end` would never fire in a course run. And
"cheap to check" is one third of "efficient", yet no sub-step makes a check cheaper.

**Change:** add one sub-step, "one gate entry point". `scripts/gate.py` with `--course <id>`, `--changed` (courses
touched since a commit, from the index) and `--all`. It runs plan, lesson_course, ledger, unitplan, frame, the
resolve check and lint for that scope, prints new lines against a stored baseline, and is what turn.py, the lead,
coursegen's gate lines and the consolidation runner all call. consolidation_gates.py becomes `gate.py --all` plus
the site build. Then rewrite AGENTS.md's first section to what is true: who commits (the lead, or `turn.py end` for
a queued job), when agents may work side by side (different courses, never the same files), and that the gate is
`gate.py`. Pick one queue format (coursegen's) and retire jobs.csv with the pilot.

### 5. The ledgers are one shared file per subject, rewritten whole, with no lock (major)

**Concerns:** test 2 (data/plans/ledgers/ as a shared home); the fact map row "What was taught when"; scale.

**Found:**
- Four files hold every course of a subject: ela.csv 1.66 MB, science.csv 1.47 MB, social-studies.csv 1.36 MB,
  math.csv 0.79 MB; 34,173 rows. A written course adds about 1,600 to 1,950 rows (ELA kindergarten 1,946, grade 1
  1,912, grade 2 1,869). Thirteen ELA courses written is roughly 4 MB in one file.
- ledger.py:87-91 `write_all` opens the subject file for write and dumps every row. No temp file, no replace, no
  lock. The kit's own CSV rule (common.txt:3) says never to do this, after "a writer once truncated handbacks.csv".
  Two agents in one subject at once (the plan of record: social studies grades 4 and 5 with World Geography I)
  can lose each other's rows silently.
- These are the files step 2 had to rebuild by key, because a line merge concatenated 1,538 planned and 4,093
  written rows (plan, step 2).
- Every row already carries `course`. The files are past the size where GitHub draws a CSV as a table (as I recall
  its limit, about half a megabyte; open one in the browser to confirm), so Cory cannot read them there now.

**Why it matters:** this is the one place where "three homes per course" is broken for the fastest growing data,
and where parallel work can destroy data without any gate noticing.

**Change:** one sub-step: `data/plans/<course>/ledger.csv`. ledger.py's `path()` (ledger.py:73) and readers load a
subject by globbing its courses (the course list gives the subject, finding 6); `write_all` writes only the course
it changed, through a temp file and `os.replace`. The split is mechanical (group by the `course` column), keys do
not change, and `ledger.py check` before and after must print the same lines. The same safe-write helper should
back every CSV write the kit asks agents to make (`plan.py defect` is the precedent): one `rows.py upsert
<course> <table> --key ...` replaces hand edits and removes the class of accident the kit warns about.

### 6. Course identity: 4.4 creates the list but leaves three id systems and a split owner (major)

**Concerns:** 4.4; fact map rows "Which courses exist" and "A course's units and why".

**Found:**
- Three ids for one course. course_status.py builds keys as `f'{s}-{g}'` (:49), so math grade 4 is `math-4`, the
  same string as the pilot folder. frame.py's slug is `math-grade-4`. The catalog id is `math-k8` (data/courses.csv,
  77 rows, several rows standing for many courses).
- The join is by slugged title: course_status.py:97-99 `frame_id(title)`, plan_flow.py:56-59.
- The collision is live: `plan_count(fid, key)` (course_status.py:107-109) counts docs/courses/<frame slug>/ plus
  docs/courses/<key>/, so docs/COURSES-STATUS.md:49 shows "Math, Grade 4 ... 31" plans: 9 real ones plus the 22
  pilot files in docs/courses/math-4/. If Cory takes 4.2's option to archive the pilot folders, that cell changes,
  and 4.4's test ("identical apart from the date line") depends on which was done first.
- frames.csv is not generated from frame.md alone, as the fact map says. Its subject, grade and catalog_id come
  from constants in frame.py (COURSE_ROWS :64-95, COURSE_META :97-116), term from TERM (:120), weeks from WEEKS
  (:123), and calendar.csv also reads days.csv (frame.py:334-383) and PINS (:128). PINS and WEEKS are also written
  in each frame's Days bullet (frame.py:126-127 comment; docs/courses/science-grade-2/frame.md:23): two hand-kept
  homes.
- Subject has two spellings: `ela` and `english-language-arts` (plan.py:711, coursegen.py:36, lesson.py:144).
- 4.4's row has "id" and "title". For the 58 framed courses the title is also the frame's H1 (frame.py row_of
  `f['title']`), so title gets two homes unless one is declared the copy.

**Change to 4.4:**
- The id column **is the frame slug** for all 120 rows (new slugs minted for the 62 without frames, in the same
  style). Add `status_key` only as a throwaway column if the one-time generation needs it, then drop it.
- course-list.csv owns id, title, subject (one spelling), grade or band, core, catalog_id, term, status. frame.md
  owns units, days, minutes and the why. frames.csv becomes a pure join of the two, still gated by `frame.py check`.
  COURSE_ROWS' grade and prefix filters, COURSE_META, TERM and LEGACY leave frame.py. WEEKS and PINS get one owner
  (the frame's Days bullet, parsed) or go to a later.csv row if that is more than an hour.
- course_status.py and plan_flow.py join on the id, not the title, and `plan_count` stops reading
  docs/courses/<key>/.
- Do 4.4 **before** the pilot decision in 4.2 takes effect, or make the 4.4 test say which cell is expected to
  move.

### 7. Day numbers live in about 140,000 prose mentions; the promised `renumber` cannot follow them (major)

**Concerns:** 4.8 "a scripted `renumber` ... rewrites days.csv, the day-keyed CSVs, the ledgers, the file names and
`leans_on` together"; test 5.

**Found (grep, pattern `days? N( to N)?`):** about 10,400 mentions in the 58 scope-and-sequence.md files, about
91,300 in written unit and section plans (skeleton folders excluded), about 39,200 under courses/. Some cross
courses: scope files cite other grades' days ("Grade 2 days 60 to 64", about 75 such). About 1,070 piece files
carry day numbers in their names (cards-exits-1-5.md, packet-day3.md). Item ids carry the day too (first read,
finding 2).

**Why it matters:** the first read was right that opaque ids would not buy position-free days. But draft 4 now
promises a cheap renumber, and that promise is false: a script can renumber tables, not sentences. And
`uses.py day:<course>:d042` will miss most of what really depends on that day unless prose mentions are indexed.

**Change:**
- Replace the renumber promise with the rule that is true: **a day number is permanent once the course's scope and
  sequence is signed off.** A course changes by rewriting a day in place or trading content inside a section. The
  year has a fixed length anyway (frames.csv `days`), so an insert always removes a day somewhere. If a true
  renumber is ever needed it is a course rewrite, planned as one.
- index.py adds **soft edges**: regex mentions of "day N" in a course's own plans and scope, and bare item ids in
  prose, typed `mentions` so they never fail a gate but do show in `uses.py`.

### 8. The gate runner overwrites the deploy folder and never builds the live Supply Closet (major)

**Concerns:** ground rule 3; 4.1.

**Found:** consolidation_gates.py:36 runs `build_site.py` with no flags into dist/. Without `--closet` and
`--library` the build deletes dist/closet and dist/library (build_site.py:975-980), and wrangler.jsonc:2 warns
"both flags, or the live site loses those pages". wrangler deploys ./dist. The documented deploy line rebuilds
first (docs/SITE.md:66), so this bites only if someone deploys straight after a gate run, but each gate run leaves
that trap set. And because cards load only under CLOSET_LIVE (build_site.py:336), no consolidation gate has built
the Word Wall, a worksheet, the Reading Room or check_words. 4.1 adds `--courses` "into a scratch output folder (a
flag is added if the build has none)": it has one already, the CURIO_DIST environment variable (build_site.py:17).

**Change to 4.1:** every gate build sets CURIO_DIST to a scratch folder and uses the deploy flags plus `--courses`
(`--library --closet --courses`), followed by check_site.py on that folder. The gate then tests what ships and
never touches dist/.

### 9. Four of the 12 tests have no builder, and "pieces" have no owner row (major)

**Concerns:** the end goal tests against 4.1 to 4.13.

| Test | The plan says | What is missing |
|---|---|---|
| 2, layout | "built with the 4.11 linter" | 4.11 lists four checks; none is a layout check. docs/courses/ root also holds math-4-spine.md, science-4-spine.md, math-3-5-progression*.md and NEXT-SPINES.md, and course folders hold DEFAULTS.md (59), TOOL-ASKS.md (14), STANDARD.md (10), APPROACH.md (9): the check needs a list of allowed names |
| 8, generated never hand-edited | 4.12 | 4.12 is a list in a doc. No marker, no check. Proof it is needed: day_skeleton.py:81 and :221 print "practises" and "practised", while all tracked skeletons read "practices": the UK spelling was fixed in the generated copies and left in the generator |
| 10, one status per object | 4.7 "the stage CSV for tools" | That file is step 5.1 and does not exist in step 4. For days, the fact map names `version:`, but ledger rows have their own `stage` that gates day jobs (ledger.py gate), and 82 day files have no `written` ledger row. flow-status.csv (648 rows, hand-kept, 640 "done") is a third status for plans |
| 12, orphans | "an orphan report from the index" | No sub-step builds it, and its list misses pieces |

**Pieces.** Section folders hold 5,762 files that are not day files (openers, exit cards, keys, family notes,
readiness sheets, practice sheets), against 2,107 days; 5,247 have frontmatter. The fact map has no row for them
and 4.7 names no node type. **451 are leaned on by no day** (orph.py: family.md 55, key-exits 36, exit 22,
practice 21 and others), which is either an orphan or a missing `leans_on`.

**Change:** index.py owns all five reports as one script with one flag each: `resolve`, `orphans` (including
pieces no day leans on), `layout` (from an allowed-homes table, finding 13), `status`, `drift` (skel blocks). Add
a fact map row "Pieces a day hands out or reads from: courses/<course>/<section>/<name>.md, owned by hand, reached
through `leans_on`". Say in 4.7 that tool status joins in step 5.1, and which of version, ledger stage and
flow-status wins for a day and for a plan (my pick: the file's own state wins, flow-status keeps only what no file
can show, such as "read by the expert").

### 10. Skeletons: every tracked copy I regenerated is stale, and jobs may edit them by hand (major, and simpler than 4.6)

**Concerns:** 4.6; 4.12.

**Found:**
- I regenerated day skeletons into scratch (`day_skeleton.py <course> all --out`, nothing tracked written) for
  science-grade-3 and social-studies-grade-2: **207 of 207 tracked skeletons differ** from a fresh render, ignoring
  line endings. For English language arts grade 1, 141 of 154 differ. The differences are real: an item id changed
  after writing (`s01-X4` is now `s01-X4b`), source rows rechecked, practice items added, new "Reserved for day"
  lines, and the spelling noted above.
- docs/pipeline/kit/day.txt:36 lets a job edit "the day skeletons of your days". So a tracked skeleton is not
  purely generated, and "the script rebuilds it" is not exactly true. This is the one point of the first read
  (its finding 9) that draft 4 did not carry over.
- 2,032 day skeletons and 731 section skeletons are tracked.
- The `<!-- skel -->` blocks matter more than 4.6 says. section_skeleton.py:42-47 and day_skeleton.py:182-188 read
  fields of the written unit plan, skel content included. A stale block in a plan flows into every new skeleton
  made below it.

**Change:** do not track them at all. Add `docs/courses/*/day-skeletons/` and `section-skeletons/` to .gitignore,
`git rm -r --cached` them in one commit (history keeps them), and drop the edit permission from day.txt (a kit
version bump). A job regenerates what it needs, as day.txt:7 already says. That replaces per-file bookkeeping
("removed when its plan or day passes") with one rule, and test 12's skeleton clause is true forever. Keep the
report-only drift check for skel blocks, and run it before the next course run starts, since those blocks feed
new work.

### 11. docs/reviews is the largest and fastest growing pile and has no home rule (major for scale)

**Concerns:** tests 1 to 3 (which only cover "curriculum files"); ground rule 3 ("Gate outputs go to
docs/reviews/consolidation/<step>/").

**Found:** docs/reviews has 4,924 tracked files, more than any course. 3,619 sit directly in the one folder;
GitHub lists the first 1,000 entries of a folder, so Cory cannot browse it there now. 1,971 are per-job
`codex-write-*` reports (about five a section). 1,305 are raw gate dumps under docs/reviews/consolidation/ from
steps 0 to 3. Draft 4 would add about 130 files per gate run, twice per sub-step, for 13 sub-steps: about 3,400
more. At tenfold curriculum the job reports alone pass 40,000 files in one folder.

**Change:** a home rule in the fact map. Per-job reports go to `docs/reviews/<course>/` (a fourth course home, or
under docs/courses/<course>/reviews/), cross-course reports stay at the top, and when a course is signed off its
per-job reports are zipped to the archive with one summary left behind. Raw gate dumps are not committed: keep
summary.csv and the compare output, write the rest to an ignored folder. The existing 1,305 can be `git rm`'d in
the same commit (the tag `pre-step4` keeps them).

### 12. The resolve gate will not start clean (minor)

**Concerns:** 4.7 "After one clean run ... becomes a failing gate".

**Found (dangle.py, pilot excluded):** 28 handbacks.csv rows name an item that is not in items.csv. About 202 item
id mentions in 27 plan files and 22 in 12 day or piece files do not resolve (regex count; English language arts
grade 4 u01-5.md names s01-X18 and s01-X22, for example). `shows` (8,414 ids) and wrongs.csv (13,352) are clean.
The whole scan took 3.8 seconds, and the `leans_on` scan 0.2 seconds.

**Change:** start the gate with a baseline file of today's known misses, as 4.8 does for item suffixes, so new
breaks fail from day one and old ones are worked off by course. The timings say the index can be rebuilt on every
gate run: no incremental build, no cache to go stale.

### 13. Second homes the 4.0 table and the fact map still miss (minor each, major together)

| Fact | Hand-kept homes today |
|---|---|
| The never-touch list | AGENTS.md:44, turn.py:35 (NEVER_TOUCH), docs/pipeline/kit/common.txt:1, and the plan |
| The gate list | consolidation_gates.py:31-37, turn.py:36, AGENTS.md ("The gates are"), ground rule 3 |
| Grade bands | data/bands.csv, check_words.py:29, defaults.py:25, course_status.py:23, gen_links.py:30, library_check.py:19 (the words key depends on this) |
| Subject spelling | `ela` and `english-language-arts` (finding 6) |
| Pins and short years | frame.py:123-128 and each frame's Days bullet (finding 6) |
| The fact map itself | the plan now; "the fact map in HANDOFF" at step 6; data/plans/README.md says its own version; HANDOFF's doc map; 4.12's list |
| What a word means | ledger `note`, Word Wall card, the new table (findings 1 to 3) |
| Day and plan status | `version:`, ledger `stage`, flow-status.csv (finding 9) |

**Change:** merge 4.12 and the fact map into **one machine-readable table**, `data/homes.csv`: path pattern, kind
(source, generated and ignored, generated and committed, state, frozen, never-touch), owner script, check. lint.py
reads it for the layout test, the generated-file guard and the never-touch guard; turn.py and the kit read it
instead of their own lists; HANDOFF links to it instead of copying it. One band function and one subject id live
in a small shared module that the curriculum scripts import.

### 14. 4.5 meets the letter of test 4 but not its substance (minor: cut it)

Passing course_pages.py "the set of standards pages build_site.py renders" still links only standards that a tool
module lists (build_site.py renders them from modules.csv). The dependency is renamed, not removed. The pages are
hidden, noindexed and kept off the deploy (build_site.py:188-196), so nothing is hurt today. Cut 4.5 from step 4,
keep its later.csv row for the real fix, and let the catalog lint carry one named exception (course_pages.py:298
`known_standards`). Test 4 then reads honestly: "passes, with one listed exception until the standards pages are
rebuilt".

### 15. The linter: three of its four checks find nothing in the curriculum today (minor)

No file under courses/, docs/courses/ or data/plans/ contains an em dash (grep, 0 files), and 23 scripts already
check for one. The check with real work to do is the fourth (no curriculum script opens a catalog file), plus the
ones the tests need and 4.11 lacks: layout, generated-file guard, never-touch. Spelling should scan what generators
print (finding 9), not only finished pages. Build lint.py as part of gate.py (finding 4), from homes.csv
(finding 13), and keep the three style checks as ten lines, not a project.

### 16. Build the index as SQLite, not two CSVs (minor, cheap to choose now)

4.7 picks nodes.csv and edges.csv "so they diff and need no database". They are ignored files, so they are never
diffed in review, and Python ships sqlite3. The plan's own later stages are queries: walls by unit and grade,
standards pages, coverage, "what depends on the files I changed". With CSV each of those is a hand-written join;
with one ignored `data/index.db` each is one SQL statement, for agents too, which saves tokens every time someone
asks a question. The first read's objection was to build_db.py's file, not to SQLite. Keep `--csv` as a dump flag.

### 17. Small false or stale statements in the text (minor)

- Line 3: "Status: draft 3 ... Not approved; nothing in it has been done", above a paragraph saying steps 0 to 3
  are done. A living doc should state it once, as it stands.
- "What is not part of the goal" points at "later.csv rows, step 4.13", but 4.13 is the order and says the rows go
  in the 4.2 commit.
- Fact map: "frames.csv, calendar.csv (`frame.py sync`)" as generated from frame.md alone (finding 6).
- 4.0 and the Word Wall section: "the same leak as the course list" (finding 3).
- 4.2 archives "the ela-6 spine files"; math-4-spine.md and science-4-spine.md stay in docs/courses/, outside any
  course home, and course_status.py:124 still reads `<key>-spine.md` as a "draft" scope.
- Ground rule 3's cost: the last full run took 4 to 5 minutes by file times (step3-after, 01:14:56 to 01:19:00),
  two of them the site build. With 4.1's additions, before and after, a sub-step costs 10 to 15 minutes of gates.
  That matches the estimate, but half of it is avoidable (see "Rules to change").

### 18. What steps 5 and 6 need from step 4 (minor)

- **5.1 before 4.7's tool status,** or 4.7 says "tools join the index in step 5.1" (finding 9).
- **Step 5's "per-tool index of where its scattered pieces are"** should be `index.py` with tool nodes, not a second
  indexer. Leave the node and edge tables open to a `tool` type now.
- **The bridge from curriculum to tools already exists:** docs/courses/<course>/TOOL-ASKS.md in 14 courses, written
  from unit plan field 8. Give it a fact map row ("what a course asks tools for") and an edge type, so "tools are
  reshaped to the curriculum" has data to start from. The days.csv `tools` column is not that bridge: its 291
  distinct values are classroom instruments ("scientific calculator", "number-line"), none a tool folder.
- **Step 6** should not copy the fact map into HANDOFF (finding 13), and its "baseline of the tests" needs each
  test to print one number: have gate.py write `data/plans/goal-tests.csv` (test, count, date) so SCALE.md and the
  Desk read it.

## Rules to change

| Rule | Change | Consequence |
|---|---|---|
| Ground rule 3: full gates before and after every sub-step, outputs committed | One run per sub-step: the "after" of one is the "before" of the next. Scope by what changed: a sub-step that writes nothing tracked (index, reports) needs only its self-test; a script-only change runs the gates that script feeds; the full run is for the start, the end and any sub-step that moves data. Commit summary.csv and the compare, not the dumps | Roughly halves gate time and stops adding about 260 files a sub-step. Risk: a scoped run misses a side effect; the full run at the end of step 4 against `pre-step4` catches it |
| Ground rule 2: nothing is deleted, every leaving file gets a hash-checked copy and an INDEX row | For **tracked** files, the pushed tag and git history are the archive: `git rm`, and one line in the step report naming the tag. The copy-and-hash rule stays for untracked and ignored material, which git cannot bring back | Skeletons, gate dumps and retired data files leave in seconds. Nothing becomes unrecoverable |
| "No curriculum work runs until step 6 closes" (HANDOFF:9) | Curriculum work may resume when the step 4 sub-steps that move curriculum data are closed (A to G below). Step 5 (tool records) and the Word Wall touch tools/ and closet/, disjoint from course homes, and can run as side work | Writing restarts days or weeks sooner. HANDOFF also notes Codex Pro ends 2026-11-30; whether that matters is Cory's call. Risk: step 5 lands while a course run is open, so the two must not share a commit |
| Never touch data/closet/words; "Cory lifts the rule for that step only" | Keep the rule whole. Import by reading. Move the conversion to the tool reshaping stage | The live Word Wall cannot break during the consolidation. Definitions are available to writers at once |
| AGENTS.md: "Every job runs inside a turn", "Never two at once" | Rewrite to current practice: one gate command, who commits, and when side-by-side work is allowed (different courses, per-course files) | The rules file stops contradicting the kit. Needs finding 5 first, or two agents in one subject still share a ledger file |
| One commit per sub-step, with Cory's go between steps | Keep one commit per sub-step. Ask for one go for the whole of step 4's first block (A to G), with a stop only where a count decides a choice (skel drift, the words card) | Fewer waits, same rollback |
| The frozen tool catalog | Keep it, and say the Word Wall, the worksheets and the topic pages are inside it | Removes the one planned exception |
| 4.8: a `renumber` script when first needed | A day number is permanent after scope sign-off | Honest about cost. Protects about 140,000 prose mentions |
| 4.9: mark words by hand; no automatic highlighting | The ledger term rows are the record of which day teaches which word; a hand mark only places the highlight | No marking pass over 2,107 days; the backlog report works today |
| Skeletons "removed when their plan or day passes" | Skeleton folders are git-ignored working files; jobs do not edit them | One rule, no bookkeeping, 2,763 files gone at once |

## Recommended step 4

Sizes are lead-session working time, gates included. S is under two hours, M is half a day, L is a day.

| # | Sub-step | Replaces | Size |
|---|---|---|---|
| A | **Gates that test what ships.** Widen the runner (unitplan, frame, sequence, check_site, skeleton self-tests); every site build goes to a scratch folder through CURIO_DIST with `--library --closet --courses`; stop committing raw dumps; record `step4-before`; tag `pre-step4`. Archive the 33 pilot jobs and add the deferred later.csv rows in the same commit | 4.1, 4.2 | M |
| B | **Retire data/units.csv** as written | 4.3 | S |
| C | **The course list as data,** with the frame slug as the id, one subject spelling, frames.csv as a join, the title join and the `math-4` key removed. Then the pilot folders: named in the doc map, or archived if Cory chooses | 4.4, rest of 4.2 | M to L |
| D | **Ledgers per course,** with a safe write, and `rows.py upsert` for the other course CSVs | new (finding 5) | M |
| E | **Skeleton folders ignored and untracked;** kit day.txt loses the edit line; skel-block drift report | 4.6 | S |
| F | **The index in SQLite,** `uses.py`, soft edges, and the five reports (resolve, orphans, layout, status, drift) with baselines; tool nodes left open | 4.7, parts of 4.11 and 4.12 | L |
| G | **`gate.py`:** one entry point with `--course`, `--changed`, `--all`, calling the checks, the index reports and lint; turn.py and the consolidation runner call it; AGENTS.md's first section rewritten | new (finding 4), 4.11 | M |
| H | **`data/homes.csv` and the ids rules:** the fact map and 4.12 as one table that lint reads; ids-retired.csv; the item suffix rule with its baseline; the day-number rule; the docs/reviews home rule; docs/CHANGES.md, one page | 4.8, 4.10, 4.12 | M |
| I | **Words, architecture only.** First the Desk card (names, the sense key, bands). Then the table with its loader, `[[word:id|shown]]` in lesson.py, edges from ledger terms, the two backlog reports, and the read-only import of Word Wall definitions as candidate rows | 4.9 | M, after the card is answered |
| J | **Close step 4:** full gates against `pre-step4`, the 12 tests printed as numbers | part of step 6 | S |

Cut from step 4: 4.5 (to later.csv, with a named lint exception). Moved out: the Word Wall conversion (to the tool
reshaping stage). Curriculum writing can restart after G; H to J do not move course data.

Order notes: A first because everything after is judged by it. C before the pilot folders move (finding 6). D
before G, since side-by-side work is only safe once ledgers are per course. E before F so the index never sees
2,763 files that are about to go. I last, because it is the only sub-step waiting on a design answer.

## Claims checked that held up

- **The first read's findings are folded in correctly:** the pilot is held apart with no rename (4.2), no opaque day
  ids (4.8), the index is not in build_db.py's database (4.7), the course list is data (4.4), the registry is split
  into a committed retired-ids file and a generated view (4.8), the order is flipped (4.13), units.csv is a deletion
  (4.3), item suffixes get a rule and a baseline only (4.8), 4.10 and 4.11 are thin, the status pages have no
  failing gate and the frozen list is corrected (4.12). The one gap is hand-edited skeletons (finding 10).
- **Day files are structurally clean.** 2,107 day files, every one with frontmatter; header course and day match
  the path in all of them; none lacks a days.csv row; lesson.py:354 already checks header section against days.csv.
- **`[[word:...]]` is safe to add.** lesson.py:48-51: the item pattern does not match a colon, so an unknown
  prefix prints as typed and fails nothing today; lesson.py:668, :3286 and :3348 already strip any `[[...]]` before
  counting words.
- **`leans_on` is a clean edge list:** 20,789 entries, 7,084 distinct targets, and it scans in 0.2 seconds.
- **`shows` and wrongs.csv ids resolve** (8,414 and 13,352 ids, 0 misses), so most of the resolve gate is green now.
- **The days.csv `tools` column is not a catalog leak** (classroom instruments only).
- **Nothing in the curriculum reads data/closet/words;** the Word Wall is tool-side only.
- **The jobs.csv queue is 33 pilot rows** (3 done, 30 waiting), untouched since 2026-11-12, so emptying it loses
  nothing in use.
- **units.csv, the 120-course claim, the course_status placement rules and frames.csv's 58 rows** are as 4.0 says.
- **The Word Wall is keyed by tool topic** (module_id is the first field of every card, and all 4,413 resolve to
  data/modules.csv), as the plan says.
- **Ground rule 7's exception for the two R2 manifests is right:** they are state, and the word art keys in them are
  one more reason not to move the cards now.
- **The gate runner exists and matches ground rule 3;** its lesson gates always exit 0 by design
  (lesson_course.py:7), so comparing by new lines, as `compare` does, is the right method, not exit codes.
