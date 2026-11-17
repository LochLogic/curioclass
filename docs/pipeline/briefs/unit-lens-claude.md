# Job: the second lens pass on one unit plan, run by Claude subagents (stand-in while Codex is out, 2026-11-17)

The same refine step as scripts/codex_unit_loop.py (three lens reads, then one fix, then the gate), split across two
agents so the reader is never the fixer. The job names the stage (`read` or `fix`), the course, the unit number
(`uu`, two digits) and the writer's brief for the subject. Today's date is in the job.

## Stage `read`

Follow docs/pipeline/briefs/unit-lens.md three times, once per lens, in this order: assessment, sources, sequence.
Fill its slots: {course}, {unit}, {uu}, {writer_brief}, and {lens} for each pass. Read the shared files once.
Each pass keeps to its own lens: finish one lens and write its report before starting the next, and do not carry a
finding over into another lens's report.

Write each report, exactly the "Your report" format of that brief, to
docs/reviews/claude-lens-<lens>-<course>-s<uu>-<date>.md (three files). Edit nothing else: not the unit plan, not
any CSV, not any other report.

Final message: one line, `<course> s<uu> read: assessment N, sources N, sequence N`.

## Stage `fix`

Follow docs/pipeline/briefs/unit-lens-fix.md, with these changes: the three lens reports are the
docs/reviews/claude-lens-<lens>-<course>-s<uu>-<date>.md files, and your report (the "Last message" that brief
describes, REJECTED lines included) is written to docs/reviews/claude-fix-<course>-s<uu>-<date>.md. Edit only
docs/courses/<course>/s<uu>.md and that report.

Judge, do not just apply. The readers over-report: expect to reject some findings (wrong on the facts, asks for
something UNIT-PLAN leaves to section or day plans, or would break a settled rule). Check each against the plan and
UNIT-PLAN before acting.

Never remove existing content to make room. The word cap is a reason to write a fix short or to reject a finding
(`REJECTED: ... | over the word cap ...`), never a reason to cut lines you were not asked to fix. Never delete the
section list (the `- **N.N.** title` lines), sensitivity or safety guards, limits, or hand-off lines. A finding that
needs days.csv, source-map.csv, a skeleton generator or another file is not yours: list it under a final heading
`LEAD:` in your report, one line each, and leave the plan as it is.

Final message: one line, `<course> s<uu> fix: merged N, fixed N, rejected N, lead N, gate PASS|FAIL`.

## Both stages

AGENTS.md rules hold. No git commands of any kind. No em dashes anywhere. Python runs as `python -X utf8`.
The blind list in unit-lens.md binds you: never open those paths. Other agents are working on other units at the same
time; if the gate fails on a file that is not yours, ignore it.

Temporary files: many agents share the temp and scratch folders, so put any helper script or note only in a folder
named for your job, `<scratchpad or temp>/lens-<course>-s<uu>/`, and never use a bare name like fix.py or s01.bak.
Never make a backup copy of the plan and never restore one: edit the plan in place, step by step, and re-read it.
