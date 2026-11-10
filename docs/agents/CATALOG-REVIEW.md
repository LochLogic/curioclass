# Catalog review (planned 2026-11-10)

Cory, 2026-11-10: with every tool specced or further along (7 ASL tools held), review the whole catalog for standards
coverage, duplication and curriculum value. Order and status: docs/ROADMAP.md, Now. Not started.

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

1. **Extract** (a cheaper model, about 12 specs an agent). One row per tool in docs/agents/catalog/rows.csv:
   id, band, subject, module, each code with the activity that teaches it and a depth (taught, practiced, touched),
   skill key, action, setting (as in overlap/tags.csv), kind of work (understanding, fluency, real-world use), what the
   screen adds over paper, build cost class (simple, engine sibling, new engine, super), and flags (K-2 reading tool
   that prompts a guess from the picture or sentence; sensitive topic). Live tools are read from tool.json and notes.md
   as well as the spec. A cold second agent re-reads a 5 percent sample; rows that disagree send that batch back.
2. **Compute** (scripts, no tokens). Coverage tables per framework and grade; the clash rule; math time on the major
   work of each grade and the balance of kinds (needs a major-or-supporting mark on each cluster in
   data/standards/ccss-math-clusters.txt, licence checked first); cross-shelf overlap; a value score from the row.
3. **Judge** (the top model, flagged items only). Clash clusters, thin and uncovered codes, the lowest-value tools.
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

## Cost (estimate, 2026-11-10)

764 specs average 16 KB, about 3M tokens of text read once on a cheaper model, plus a few dozen judge agents. Roughly
what 3 to 5 tools cost to take through the pipeline. Measure the pilot and correct this line.
