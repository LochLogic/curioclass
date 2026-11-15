# Skeleton scripts review, 2026-11-15

Scope: scripts/unit_skeleton.py, scripts/unitplan.py, scripts/codex_units.py and the plan briefs, before Codex writes the science, ELA and math unit plans. Priorities: correct, robust, prevent the faults reviewers keep finding, lean. Line numbers are for the files as they now stand; "old" line numbers are from the copies taken before this review.

## What I checked

- Every reader of course data in unit_skeleton.py (frames.csv, days.csv, calendar.csv, the progressions, ela-texts.csv, source-map.csv) for what happens on a missing column, a short row or a non-number day.
- The layout of every math, ELA and science source map against the one layout of sequence-write.md rule 8 (`source,title,goals,standards,unit,days,decision,why,order_conflict,harms_learning[,url]`). None of the 21 maps on file is in that layout yet (the math-grade-4 map not opened, blind rule).
- Field 4 (readiness and retrieval) against rule 2 of sequence-write.md, counted by grade number.
- Field 5 (end-of-unit assessment) for time, codes assessed before taught, and child-by-child evidence within ten days.
- Fields 8 and 10 for lines that repeat the day list or field 2.
- The driver codex_units.py and the gate unitplan.py for how they call the skeleton.
- Skeleton output for every ELA, science and math course to a scratch folder, before and after, and social studies against the frozen baseline.

## Findings and changes

1. **A source map in an older layout crashed the skeleton or silently dropped lines.** Old unit_skeleton.py:1288 indexed `r['unit']`, so every math map (which has `course_unit`) stopped with `KeyError: 'unit'` and a traceback; a map that happened to have a `unit` column but not the rest would have lost its base-text lines without a word. Change: `read_csv(path, need)` (unit_skeleton.py:82) checks the header and every row and raises `DataError` naming the file, the columns it has, the columns it needs and the missing ones; `source_map` (unit_skeleton.py:563) adds "The source map is not yet in the one layout of sequence-write.md rule 8; convert it first." **Decision: the skeleton stops for that course.** A plan written without its base-text lines would fail unitplan's field 10 source check later and be rewritten, so going on only spends a Codex run. Verified: all 21 maps now stop with the message and no traceback; self-test "old-layout source map stops".
2. **Other data faults gave tracebacks.** days.csv, calendar.csv, the progression, frames.csv and ela-texts.csv are now read with their required columns (constants near unit_skeleton.py:368 and the readers), a non-number day names the row, and main() reports `unit_skeleton: <course> unit N not written: <file: what>`. An unknown unit number names the real units. Verified by self-test (missing column, non-number day, short row).
3. **unitplan.py traceback on the same maps.** Old unitplan.py:306 called `sk.source_rows`, which now raises. Change: unitplan.py:350 and 366 catch `DataError` per course and per file and print `path:-: cannot check: <file: columns>` and a FAIL line; the docstring lists it. Verified on a copied skeleton under science-grade-6 (its map is old): one clear FAIL line.
4. **codex_units.py used the social studies brief for every subject.** Old codex_units.py:55 always passed plan-codex.md ("the social studies course"). Change: `brief_for` picks plan-codex-<subject>.md where it exists. Old line 45 ran units 1 to N, not the real unit numbers; now it uses unit_skeleton's own unit list. A skeleton that cannot be made printed a CalledProcessError traceback; now it prints the skeleton's message and "STOPPED: no skeleton". Verified: math, ela and science map to their own briefs, social studies to plan-codex.md.
5. **Rule 2 by last use was not computed (the fault reviewers keep finding).** New `earlier_rows` (unit_skeleton.py:1083): for every row the unit assumes, its last use (the highest grade whose days.csv teaches or assesses it, this course's earlier days counting as this year; a retrieval or readiness day is not a use), the rule (retrieval, or readiness when last used two or more grades back) and whether days.csv names it. Field 4 now prints a skel table `Row | Owned | Last used | Rule says | days.csv names it` and one TODO grouping the disagreements (unit_skeleton.py:1454), telling the writer to plan inside existing time, never add a day, and list each under "For the lead". Faults also caught: a row missing from the progression, owned in a later grade, taught later in this course, not taught in this course, an unreadable earlier days.csv. Verified by self-test (K row last used in K is readiness in grade 3; a grade 2 retrieval day is not a use; a grade 2 teaching day makes it retrieval). Real example: science-grade-3 unit 2 assumes sk-push-pull, last used in kindergarten, which days.csv treats as retrieval.
6. **Retrieval tasks missed in math, ELA and science notes.** Old unit_skeleton.py:922 matched only the social studies shapes, so a note "Retrieve s2-compare-designs" was missed and field 4 said "no retrieval task". Now `retrieval_clauses(..., broad=True)` for non-social-studies courses; identical clauses on several days are one row with their days. A rule-2 retrieval row no note names gets one TODO row "inside existing time".
7. **Field 5 had no time, untaught or collect-once lines.** New skel lines per assessment day: Time (minutes from frames.csv, less ten when the next unit's readiness check sits on that day, rows to sample); codes assessed before any teaching day cites them (`taught_before`, a lettered part counts its parent); child-by-child evidence within ten days (`evidence_pairs`, the same assessment spread over a unit excluded) with a collect-once TODO unless the later note says reuse. Verified by self-test; on real data: 5 evidence pairs, 3 collect-once TODOs, 0 untaught codes.
8. **ELA rights printed as bare "TODO".** Old unit_skeleton.py:1302 wrote `rights: TODO` (not the marker, so the gate never caught it). Edition and rights now sit on the field 2 text set lines, "not stated" when empty; field 10 points there instead of repeating the list.
9. **Fields 8 and 10 repeated the day list.** Supplies, tools and safety are grouped by item with day runs; goal and note matches give day numbers only; science field 8 points to field 10 for the frame's safety column; field 10 sensitivity days by number. Social studies keeps its full lines.
10. **Lettered parts each assessment owes:** already computed (`parts_of`, one row per part in field 5); no change needed.

Also: `--help` prints the usage; `--self-test` runs 19 checks (unit_skeleton.py:1665); the print line gives TODO count, words and about-token cost per skeleton; header kinds include unknown kinds.

Briefs: plan-codex-math.md, plan-codex-ela.md and plan-codex-science.md gain a "Computed lines in the skeleton" block; the science brief no longer says statements and dimensions are not on file (data/standards/ngss-pe-dimensions.csv holds them); plan-read.md and plan-codex-read.md ask readers to check the field 4 table was followed and evidence collected once. CRLF endings kept.

## Weighed and not done

- **Word or token cost per skeleton as a stored field:** printed per skeleton on write instead; a stored number would go stale.
- **The Part text in field 5:** left as is; it is the own-word line and the gate depends on the row shape.
- **Math leaning on later reading or other subjects:** field 3 cross-subject lines already do it from the progression; not computed further.
- **End days overloaded:** covered only by the Time line and rows to sample; a minutes estimate per item would be invented.
- **Checks claim only what they sample:** enforced by one row per code and part; no extra check.
- **Quiet retrieval rows as rows:** kept (296 TODO rows across ELA and science). Each is a real rule 2 gap; one line per unit would hide which row.

## Social studies frozen

Regenerated all 15 courses (138 files) with `--out` to scratch after the last edit and diffed against skel-ss-base: zero differences. Two runs of all ELA, science and math courses are identical (deterministic).

## Size

ELA and science, 119 skeletons: 478,795 words before, 488,386 after (+2 percent); TODO markers 3,460 to 4,411. Field 4 rose from 6,129 to 51,738 words (the uncounted table); fields 8 and 10 fell by about 43,000 words together.

## Samples (before, then after)

Science, science-grade-3 unit 2 (no source map), field 4:
- Before: `**Given:** none (days.csv holds no readiness check before this unit and no retrieval task in its days).`
- After: `| sk-push-pull | grade K | grade K (science-kindergarten, last day 31) | readiness | not named by id |`, `| s2-compare-designs | grade 2 | grade 2 (science-grade-2, last day 59) | retrieval | retrieval, day 25 |`, and `TODO(writer): days.csv and rule 2 disagree: sk-push-pull (last used grade K) wants a readiness check, and days.csv holds no readiness check for this unit. ...`; field 5 gains `- **Time:** 45 minutes a day (data/plans/frames.csv); 2 rows below to sample.`

ELA, english-language-arts-grade-9 unit 2, field 2 and field 10:
- Before (field 10): `- Ulysses, Alfred Tennyson (1842); edition: not stated; rights: TODO`
- After (field 2): `- g9-u2-02 (paired): Ulysses, Alfred Tennyson (1842); whole, literary; status: on file; edition: not stated; rights: not stated`; field 10: `- **Texts:** author, year, edition and rights of each are in the text set of field 2 (data/plans/ela-texts.csv).`

Math: no math map parses, so every math course now stops with the map message (before: `KeyError: 'unit'` traceback). Sample from a scratch `--data-dir` copy of math-grade-3 days.csv without its map, unit 2, field 4:
- Before: `**Given:** none (days.csv holds no readiness check before this unit and no retrieval task in its days).`
- After: `| m2-count-skip-1000 | grade 2 | grade 2 (math-grade-2, last day 102) | retrieval | not named by id |` with a retrieval TODO row for it, and the day 23 and 27 retrieval notes now found.

## For the lead

- Convert the 21 math, ELA and science source maps to the one layout before skeletons run (none is converted yet).
- 40 units have rows rule 2 says want a readiness check that days.csv does not give; the plans will list them, but days.csv is where they are fixed.
- 296 rule-2 retrieval rows have no task named in days.csv; the writer adds one inside existing time.
- Blind rule: early in this review I printed field 4 of my own scratch skeleton of english-language-arts-grade-6 unit 1 (generated from its days.csv) while sizing the table. I did not open its data or docs by hand. Decide whether that read matters for the grade 6 comparison.
