# Answer-key read: social-studies-grade-4, unit 2

Job 023, kit version 14. Requested report date: 2026-11-25. Attempted 2026-11-26.

## Verdict

Fail, incomplete: the required baseline gate exited 2 before any content edits. This report records an interrupted attempt, not a completed answer-key review or a finding that the items are sound.

## What I studied

- `docs/pipeline/briefs/sensitivity-read.md`, sections 1 to 3: the answer-key study step requires recorded independent solutions before comparison.
- `docs/GLOSSARY.md`: the course uses unit, section, exit ticket, and end-of-unit assessment.
- `docs/courses/social-studies-grade-4/DEFAULTS.md`: 40-minute days, 350 student words, and 15 words per student sentence.
- `docs/pipeline/briefs/section-write.md`: new assessment cases, counted individual turns, and one marking scale per record.
- `data/plans/social-studies-grade-4/items.csv`, filtered to days 17 to 38 and exit, readiness, or end records: 56 items listed and read. There are no readiness records in this range.
- Student exit cards, the day 37 assessment and source packet, day 38 response cards, retained-work prompts, and the eight associated assessment SVGs: read to identify the information supplied to students.

The required solve-first study step was not completed. No external factual source was checked.

## Baseline blocker and stop

The literal required gate command first failed with `PermissionError: [WinError 5] Access is denied` when starting child checks. This installation reports `C:/Program Files/LibreOffice/program/python-core-3.12.14`, a directory, as `sys.executable`.

A process-local rerun set `sys.executable` to the actual launcher returned by `shutil.which('python')`, then ran the same gate through `runpy`. No repository script was changed. It ran 12 gates and printed 74 failing lines, all categorized as `lint-social-studies-grade-4: style UK spelling`. These counts cannot establish whether any line is new because no baseline was stored.

The gate then printed:

> FAIL baseline not stored: these gates crashed (lesson-social-studies-grade-4.txt, plan-social-studies-grade-4.txt); run with the project python (C:\Program Files\LibreOffice\program\python.EXE)

Both named logs end with `ModuleNotFoundError: No module named 'markdown'`. The gate's baseline-storage function exits 2 on this condition. The job explicitly requires stopping on exit 2, so no course data or pieces were edited and no baseline was forced.

Evidence: `build/gates/now-social-studies-grade-4/plan-social-studies-grade-4.txt` and `build/gates/now-social-studies-grade-4/lesson-social-studies-grade-4.txt`. These are gate output, not a successful baseline.

## Fault table

| Item | Kind | What was wrong | Fix | Stage that made it |
|---|---|---|---|---|
| Not determined | Not assessed | Review stopped before a valid cold-solve comparison. | Resume with working gate dependencies and a fresh reader. | Not assigned |

No content-fault counts are established for key, ambiguous, off-goal, rule4, needs-info, two-asks, or key-on-child-page. Zero confirmed findings must not be read as zero faults. No item was changed or re-solved.

## Own errors

An inventory command excluded `answer` but accidentally printed `steps` and `samples`. Its delayed output appeared before independent answers were recorded. Treat all 56 items as exposed to answer guidance for purposes of assigning a fresh cold reader. The later card reading cannot be represented as an uncontaminated cold solve.

The first attempt also looked for `DEFAULTS.md` at the repository root; the correct course-specific file was subsequently read.

## Could not settle

- All 56 independent solutions, comparisons with answer keys, and wrongs.csv diagnostics remain incomplete.
- Shared-piece and lower-grade case reuse, goal and standard alignment, sentence limits, split-item needs, marking scales, and individual-turn timing remain unverified.
- Section plan field 3 exit-line mismatches were not established. The data writer must receive that list after a completed read.
- Factual source tracing and safety checks remain incomplete. No page was opened, refused, or newly marked checked; no browser-check list was established.
- A final gate showing no new FAIL was not obtained.

## Files changed

Only this report. No items.csv, wrongs.csv, shared piece, key piece, source row, or plan was changed. No helper folder was created and no stray empty folder was observed.
