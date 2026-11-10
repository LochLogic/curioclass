# Catalog review (planned 2026-11-10)

Cory, 2026-11-10: with every tool specced or further along (7 ASL tools held), review the whole catalog for standards
coverage, duplication and curriculum value. Order and status: docs/ROADMAP.md, Now. Pilot run 2026-11-10 (see "Pilot results"); the full run waits on Cory's picks
(Desk card q-catalog-pilot).

The earlier passes (docs/agents/overlap/method.md, docs/agents/AUDIT.md) read one-line idea cards. This one reads the
specs, so it can check what each tool really does. It reuses their clash rule, tag style and scripts
(scripts/overlap/).

## What it answers

1. **Coverage.** For every standard code: which tools claim it, and which really teach it (the activity is named).
   Codes with no tool, codes only touched, codes with five or more tools.
2. **Duplication.** Tools that teach the same skill the same way in the same band (the clash rule, rerun on spec-level
   rows), and overlap with the other shelves: worksheet generators, printables, Recess games.
3. **Curriculum value.** For each tool, on evidence: is it on the core work of the grade, how deeply does it teach its
   standard, does the screen do something paper can't, and how costly is it to build. This feeds the adoption bar
   (docs/ADOPTION-BAR.md) and the build order.

## Steps

1. **Extract** (a cheaper model, about 12 specs an agent). One row per tool (brief: docs/agents/CATALOG-EXTRACT.md; packets from
   scripts/catalog_batch.py in docs/agents/catalog/batches/; rows as JSON lines in docs/agents/catalog/rows/):
   id, band, subject, module, each code with the activity that teaches it and a depth (taught, practiced, touched),
   skill key, action, setting (as in overlap/tags.csv), kind of work (understanding, fluency, real-world use), what the
   screen adds over paper, build cost class (simple, engine sibling, new engine, super), and flags (K-2 reading tool
   that prompts a guess from the picture or sentence; sensitive topic). Live tools are read from tool.json and notes.md
   as well as the spec. A cold second agent re-reads a 5 percent sample; rows that disagree send that batch back.
2. **Compute** (scripts/catalog_compute.py, no tokens; tables in docs/agents/catalog/tables/). Coverage tables per framework and grade; the clash rule; math time on the major
   work of each grade and the balance of kinds (needs a major-or-supporting mark on each cluster in
   data/standards/ccss-math-clusters.txt, licence checked first); cross-shelf overlap; a value score from the row.
3. **Judge** (the top model, flagged items only; files in docs/agents/catalog/judge/). Clash clusters, thin and uncovered codes, the lowest-value tools.
   Each gets a proposal: keep, keep with a spec note, reshape, move a code, hold, or cut.
4. **Decide.** Proposals go to Cory as Desk question cards with a pick, grouped by subject and band, the way the
   worksheet trim did (docs/agents/trim/).
5. **Apply.** Concept and spec edits, code moves (scripts/add_codes.py), a build order by value in data/waves.csv, and
   lessons into SPEC.md where a pattern repeats.

## Rules

- BASELINE rules 1 and 2 hold: nothing is merged or cut only to save work, and every code stays taught well. A tool is
  cut only when its codes stay covered by tools that teach them in full.
- Live tools never move; a planned tool changes instead. Reshape is the default fix.
- Curiosities and Recess are not scored on curriculum value. They are checked for coverage and duplication only.
- The extract agents read and report. Only the integrator edits data/ and specs, after Cory's picks.

## Pilot first

Grade 4 math and grade 6 ELA (the two unit-pilot courses): extract, compute, judge, and show Cory the tables and the
proposals. Tune the row format, then run the rest by subject and band. The pilot's tables are also the starting point
for those two year spines (ROADMAP Track 7, step 1).

## What it absorbs

The K-2 reading scan and the math focus and balance report (ROADMAP Now, item 8a and 8b) are columns and tables of
this review for tools. Worksheets, plans and Word Wall cards for K-2 reading still get their own short scan after it.

## Pilot results (2026-11-10)

36 tools: 13 grade 4 math, 23 grade 6 ELA (9 grade 6, 14 from the 6 to 8 band). Tables: catalog/tables/pilot-math-4.md
and pilot-ela-6.md. Judge files: catalog/judge/pilot-math-4.md and pilot-ela-6.md. Cory's questions: Desk card
q-catalog-pilot.

- **Coverage:** no standard without a tool. Math: 27 of 28 standards "taught" by the row, but the judge, reading by the
  parts of each standard's wording, found 17 of 29 full, 8 in part, 4 only shown; 10 of the 12 weak ones are major work.
  ELA: 4 standards need a spec fix (RL.6.7, RL.6.9, RI.6.1, W.6.3), W.6.1c to e has no tool, and three are year
  standards no one tool can teach (RL.6.10, RI.6.10, W.6.10).
- **Duplication:** none. The clash rule found nothing once the `generic` setting was ignored, and the judge read the
  close pairs as healthy second angles. Two things the tags missed: two tools build the citation for the student, and
  climbing-reads doubles the Reading Room.
- **Value:** the value table did not separate tools (see below). The judges' depth tables did.
- **Beatable checks:** 19 specs have a check a student could pass without the skill. A spec edit now is cheap.
- **Band tools:** of 14 tools for grades 6 to 8, 6 reuse one text for all three grades with a step added.
- **Math 4.MD.A and 4.NBT.B, ELA L.6.2:** two modules share one cluster and split it cleanly; the module codes should
  name the standards, not the cluster.

**The row needs to change before the full run.** The cold re-read agreed with the cheaper model on most labels
(math 13 of 15, ELA 9 of 19 with 7 more that the scale could not express), so the model is fine; the scale is too
coarse. Changes proposed by the judges (apply on Cory's yes, then re-run the 36 as the test):

- per code, `parts_missing` from the standard's own wording, and `items` (how many problems or rounds);
- who does the key step, the student or the tool; a new depth `shown` for when the tool does it;
- a check that can be beaten, or an activity only on an optional path, cannot be `taught`;
- for writing and talk: support (modeled, guided, none), check (tool key, tool rule, self-guide, teacher, none),
  on the main path or not;
- `paper_version` (partial on 35 of 36) becomes a named `paper_gap`; drop `minutes` (25 on nearly all); `kinds`
  defaults to 0; ELA gets `texts` (source, length) and `grade_split` (how grades differ);
- the tables must read `unsure`, where the real findings were filed.

## Cost (measured on the pilot, 2026-11-10)

Extract: 3 agents on the cheaper model, 130k to 148k tokens each for 11 to 13 specs (about 11k a tool, 3 to 4 minutes).
Judge: 2 agents on the top model, 144k and 161k. Compute: no tokens. The full catalog at this rate is about 64 extract
agents (about 9M tokens on the cheaper model) and about 40 judge agents (about 6M on the top model), in the range of
what 3 to 5 tools cost through the pipeline. The earlier estimate held.

