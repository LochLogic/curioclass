# How the shelves fit together (planned 2026-11-10)

Cory, 2026-11-10: the helpers built around the tools (Sub Day, Word Wall, worksheets, charts, games and the rest) are
worth keeping, and they must move with the larger change of shape (docs/ROADMAP.md, "The path from here"; BASELINE
rules 21 and 22). This file says how every shelf hangs together, what the change does to each, and the order of the
fixes. Survey of the code and data: 2026-11-10 (findings at the end).

## Three things, three keys

| Thing | What it is | Key | Changes? |
|---|---|---|---|
| **Module** | A topic a class spends a few days on. The hub page every shelf links from | `module_id`, about 762 public URLs | **One teachable topic.** Split only when it holds two unrelated topics, and then properly (below). Its list of standards is rewritten in place, from a cluster to the standards inside it |
| **Tool** | One screen-based lesson, see-why or practice piece | `tool_id` | Gains a role and its own list of codes: only the ones it teaches on its main path |
| **Unit** (new, Track 7) | A 1 to 5 day package for a course, in the year's order | `unit_id` (to be designed at the unit pilot) | Points at modules and picks items from the shelves. It owns nothing but the order, the teacher pages and what no shelf has |

**The correction this makes to the locked plan:** rule 22 and step 4 said modules would be split so each names its
standards. The survey shows `module_id` is the key for the Word Wall (4,413 cards, 719 art folders), anchor charts,
Game Night, The Map, the research cards and about 762 live pages, and no script renames a module. Splitting would
break or orphan all of them. So a module is never split just to reach standard-level detail: its standards are
spelled out in place, a second or third tool joins the same module, and a new module is made only for a standard
with no topic home. Same goal (an untaught standard shows), no breakage.

**When a module is split (Cory, 2026-11-10).** Keeping modules whole is the rule because a module is a topic, not
because splitting is hard. It is split only when it holds two unrelated topics, and then properly: a split script, redirects for the old pages, and its Word Wall, chart and games divided by hand. It is never split just to reach standard-level detail; the ledger does that.
The step 2 read flags candidates (a guess of one to two dozen: 21 math modules mix domains, such as
`math-4-angles-and-line-plots`). They come to Cory as exceptions in step 4. The 38 core band modules that span
grades lean toward staying whole; the unit pilot tests that.

## One ledger of who teaches what

`data/coverage.csv` (new, built in step 2 and kept by script): one row per standard per course, saying where it is
taught in full: which tool (and its role), which generator preset or worksheet rows carry the fluency, which Reading
Room set, which unit. It is the one home for a coverage claim and the source of the one measure on the Desk.

Every shelf that prints standards reads them from the tool or the ledger, not from the module:

- tool pages, the search index and the standards pages show a tool's own codes (today each tool shows every code of
  its module, which rule 21 forbids once a module holds three tools);
- lesson plans and Sub Day packets take their `focus` from the tool's codes (today the check requires a module code,
  and the build stops if it is not one);
- old coverage scripts (scripts/overlap/coverage.py, standards.py) are retired in favor of the ledger.

## Shelf by shelf

| Shelf | Keyed to | Under the change | Work |
|---|---|---|---|
| Lesson plans | tool | Stays one per tool, for teachers who use one tool on its own, with a link to the course days that use it. No per-tool plan is written for a course's key tool (Cory, 2026-11-12). For a `see why` or `practice` tool the plan is where `unit_adds` lives: the talk, the writing, the worksheet to pull | Check focus against the tool's codes |
| Sub Day packets | tool, or a course day | For a day inside a course, generated from that lesson day (Cory, 2026-11-12). Per-tool packets stay for tools used outside a course. Best for `lesson` tools (a substitute needs the tool to carry the teaching); a `see why` tool's packet names the worksheet that completes it | Same check; pull words by module as now |
| Word Wall | module | Unchanged, because modules do not move. A second tool in a module shares the same wall | None |
| Anchor charts | module | Unchanged. "The first tool built writes the chart" becomes "the module's `lesson` tool writes it" | One line in the plan brief |
| Game Night | module | Unchanged. The family sheet names the module's `lesson` tool, not "the first built tool" | Template line |
| Research cards | module | Unchanged | Add a checker (none today) |
| Worksheets | course, row, module title | Now the named home of fluency volume and extra practice, recorded in the ledger. The join by module title is fragile (four modules share a title today) | Join by `module_id`; add each preset or row to the ledger |
| Generators | rules on subject, strand, grade | Same role as worksheets for fluency. A `practice` or `see why` tool links to its preset | Record preset per standard in the ledger |
| Reading Room | story | **Not the source of course texts below the higher grades** (Cory, 2026-11-12: its stories at mid and lower levels are mostly very old or from other countries and cultures, "fine for a reading room but id like something newer and more relatable for course content"; card `q-course-texts`, answered the same day: grades 9 to 12 may anchor on it; K-8 only as a paired or optional read). It stays a shelf for independent reading. The named home of year-long reading and topic threads. Needs the `record`, `topics` and code fields the plan already describes (ROADMAP item 8c) | Fields before the ten-story pilot |
| The Map | module | A stop is "ready" when its `lesson` tool is live, not any tool. Later it shows the measure per stop | Small build change |
| Related tools | derived | Inside a module, show siblings first and in order: see why, do it, use it | Small build change; a `role` and order column on tools |
| Posters, Break Box | band or grade | Unaffected | None |
| Recess, Curiosities | their own | Outside the bar. They take the role `curiosity` or `recess` and claim no code, so the ledger never counts them | One line in rule 21 |
| Units, Tracks, Binder | new | Designed at the unit pilot (path step 5): a unit lists its modules, then for each day the tool, the plan, the worksheet rows, the Word Wall words, the chart, the game and the reading it uses | A unit data shape, tried on two units |

## Order (inside the path)

1. **Step 1 (rules), now:** one spelling for math codes (`4.NBT.B.5`, with the cluster letter, which the site's
   validator already expects); the standard texts filed; roles for Recess and Curiosities.
2. **Step 2 (read):** the read writes each tool's own codes and role, and builds the ledger.
3. **Step 3 (fix what is built):** switch tool pages, standards pages, search, plan and Sub Day checks to tool codes;
   join worksheets by module id; the Map and family-sheet lines. Each is small, and all are needed before a module
   holds a second tool.
4. **Step 4 (shape):** module standards rewritten in place; the few two-topic modules split properly, once Cory
   agrees each; second and third tools added to major-work modules;
   worksheet presets and Reading Room sets written into the ledger.
5. **Step 5 (prove one course):** the unit shape, on grade 4 math and grade 6 ELA, pulling from every shelf.

## Words

"Unit" means two things today: the worksheet shelf calls a course (`ela-3`, `algebra-1`) a unit, and Track 7 calls a
1 to 5 day package a unit. From now a course is a **course** and a unit is the Track 7 package. Worksheet URLs keep
their ids; only the wording in docs and pages changes, as each is next touched.

## What the survey found (2026-11-10)

- 797 modules: 795 hold one tool, one holds two, one holds three. The module page already lists every tool, plan,
  sheet and game of a module, so a second tool shows correctly with no change.
- 133 of 144 math modules list a bare cluster. 213 of 1,457 codes sit on more than one module.
- Loud failures if a module id changed: lesson plan focus check, Word Wall, charts, Game Night (the build stops).
  Silent ones: worksheets joined by title, research cards, The Map (a warning only).
- Not affected by anything here: tool URLs, worksheet URLs, Map URLs, Break Box, posters, Reading Room, Recess.
- Nothing in data names a unit yet, and nothing records that a generator carries a standard's fluency.
