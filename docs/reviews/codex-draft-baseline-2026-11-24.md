# Codex draft run: baseline, 2026-11-24

The Codex draft run (scripts/codex_draft.py, branch draft/codex, later.csv L105) was ended softly on 2026-11-24 at Cory's
call: the `_draft\STOP` file let running jobs finish and started no new ones. Every lane ended by 16:33. This sheet is
the baseline for whatever review comes next. Nothing here is on main.

## What the run made

246 jobs, 240 commits, about 2.3 billion tokens in (mostly cached). Every piece is "draft 1, not ready".

| Course | Days written | Section plans | Lane state at stop |
|---|---|---|---|
| math-kindergarten | 160 of 160 | all | course done; math grade 1 was next |
| science-grade-4 | 120 of 120 | all | course done |
| science-grade-5 | 120 of 120 (days 1 to 4 are the main probe days) | all | grade fix job was next |
| social-studies-grade-4 | 160 of 160 | all | course done |
| social-studies-grade-5 | 51 of 160 | units 1 to 4 | day 4.2 last |
| english-language-arts-grade-4 | 38 of 160 | unit 1 and plan data through unit 2 | lane stopped by Cory 2026-11-23 |

Jobs the runner skips by design (reads, key reads, fixes after reads, cleanups, retool stops) were never run. No day has
had a cheap read or an expert read.

## Merge of main into the draft (commit bd20bc418)

The drafts were written on the unit plans of 2026-11-22. Main's stage 4 fixes of 2026-11-24 are now merged in, so the
drafts sit on today's unit plans.

- Unit plan conflicts (9 files) were merged word by word: Codex's day kind relabels and US spelling, together with main's
  minute, cost, supply and exit fixes. The science grade 4 unit 2 kind count was recounted from the merged table.
- The CSV union merge rule had duplicated whole files where both sides edited (days.csv, ela-texts.csv, the ELA and
  science ledgers). Those CSVs were re-merged by key: rows matched by day, item or text id, cells merged, deletions kept.
  Where both sides changed one list-like cell (supplies, safety, a note), the cell keeps Codex's value plus main's
  additions. ELA grade 4 anchor measures keep Codex's word counts plus main's lowered targets. `ledger.py check` passes
  for ela, science, social studies and math.

### Carry-overs: main fixes the draft days do not show yet

Codex had replaced these unit plan tables with a pointer to the day files, so main's fixes inside them must be carried
into the days and items by the review:

1. math-kindergarten s04: the day 64 exit (K.OA.A.1) now asks "tell how many beads altogether", answer six altogether.
2. math-kindergarten s06: the day 104 exit now writes the numeral on a blank label and counts on from fourteen to
   seventeen; error H, restarts at one.
3. math-kindergarten s08: day 136's ten geometry center minutes include revising day 136 unit 7 transfers (s07 field 7).
4. math-kindergarten s05: day 89's teacher first models moving one cube between parts (the one fluency-day exception).
5. math-kindergarten s02 and s08 exit wording (sorting into categories and writing counts) changed on main; check the
   matching days' exits.
6. science-grade-4 day 23: main relabeled it Application; the written day is a Fluency day.

## Gates after the merge, and after the mechanical fixes

Failures not counting the known "not in data/units.csv" line. Sequence check: 0 failures in all six courses.

| Course | After merge | After mechanical fixes | Largest remaining kinds |
|---|---|---|---|
| math-kindergarten | 4,425 | 4,425 | 4,194 pairs of items share a stem (557 rows, 87 stems); 73 day files print an item of another day |
| science-grade-4 | 29 | 29 | 8 exit numbers reused from practice; 7 days show an item that is not their exit |
| science-grade-5 | 127 | 127 | 92 days lack a "Shared shape" note; 6 student pages over two sides |
| social-studies-grade-4 | 180 | 175 | 96 judged written tasks never handed back; 29 days show an item that is not their exit |
| social-studies-grade-5 | 141 | 114 | 51 days lack a "Shared shape" note; 14 tasks never handed back |
| english-language-arts-grade-4 | 601 | 451 | 127 source-map order conflicts need harms_learning; 40 goal phrases; 35 shared stems; 34 exit text ids with no ela-texts row |

### Mechanical fixes made (data only, no content judgment)

- ELA grade 4: `judged` filled on 91 items (key where the row computes its answer, else teacher).
- ELA grade 4: 32 materials rows given the day that names them in used_days.
- ELA grade 4, social studies grades 4 and 5: `opens_min` set to the opening part's minutes on 60 days (it had counted
  every part up to the exit, which broke both the plan and lesson gates).
- ELA grade 4: 2 judged tasks added to their next day's existing return row.

### Left for the review (each needs a reading)

- Math kindergarten's shared stems are one systemic fault, not 4,194: the items keep their case (the picture, the
  collection) only in steps and answers, so "Which group has fewer?" repeats across days. Each item needs its case in
  its stem, read from its day. One pass per unit fixes the whole class.
- Hand-backs with no return row (social studies 4 and 5): the receiving day needs a slot and minutes for them.
- "Shared shape" notes (science 5, social studies 5, ELA 4): name the practice shape against the exit's, a reading of each day.
- ELA grade 4 source-map order conflicts (harms_learning yes, no or unclear) and exit text ids without an ela-texts row.
- Everything a gate cannot see: no day has been read. A sample day (science grade 4 day 16) was complete and well built,
  but its prose was clipped, its family note said "students 18 or older receive it" in grade 4, and it carried planning
  notes ("Honor day 15's Tomorrow") on the teacher page.

## Next

Paused here at Cory's call. The plan on the table: a probe read of one section per course to size fixing against
rewriting, then the reads and fixes (Claude reads, Codex applies fixes while Pro lasts to 2026-11-30), then a merge
into main per course.
