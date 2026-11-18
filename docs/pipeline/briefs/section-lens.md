# Job: read, then patch, the section plans of one unit (kindergarten probe, 2026-11-17)

Step 4 of "How section plans are authored" (PRODUCTION-PATH step 7): lens reads take a whole unit's sections at
once; the fix pass patches flagged fields and never rewrites. Reader and fixer are separate agents. The job names
the stage, the course and the unit (`uu`, two digits).

## Stage `read`

Read AGENTS.md; docs/courses/UNIT-PLAN.md ("The rules", "The section plan: fields, in order", "Length"); the unit
plan docs/courses/{course}/s{uu}.md; the frame's row and Sensitive topics lines for unit {uu}
(docs/courses/{course}/frame.md); the unit's days.csv rows (data/plans/{course}/days.csv); then every section plan
docs/courses/{course}/u{uu}-*.md and its skeleton in section-skeletons/.

Read four times, one lens at a time, finishing each before the next:

1. **assessment**: checks written first; each teaching day has evidence a kindergarten teacher can see or hear; exit
   questions asked aloud with their answer and wrong answers, one error letter each; rule 4 (no taught case,
   picture or number reused in a check); the readiness and unit items owned.
2. **sequence**: days follow days.csv (goal, kind, order); minutes add up inside the day length; what is carried
   is named and handed on; the handoff into the next section and from the previous one; nothing taught after a
   mid check in its section; the plan agrees with the unit plan or says why not.
3. **classroom**: a five-year-old can do it in 20 to 30 minutes; children are not asked to read; talk moves,
   supports, access, the two rooms (one parent and child, one projector); supplies are cheap and named.
4. **sensitivity and sources**: no child reports on home, family, money, body or religion, or is shown as the
   mistake; read-alouds and pictures are our own or public domain, never a copyrighted picture book; claims about
   real places and people are true; no em dashes, no company names.

Write one report, docs/reviews/section-lens-{course}-u{uu}-{date}.md: under a heading per lens, one line per
finding, numbered through the whole report, most serious first within each lens:
`N. [u{uu}-S field] what is wrong | why it matters | exact fix | origin=<section|unit|scope|frame|template>`
where origin is the highest layer that must change for the fix to hold (docs/pipeline/PROBE-GUARD.md). Then
`Count: N findings (assessment A, sequence S, classroom C, sensitivity and sources T).` Edit nothing else.

## Stage `fix`

Read the report, then each finding against the section plan, the unit plan and UNIT-PLAN. Judge, do not just
apply: readers over-report. Patch only the lines a finding names; never rewrite a field, never remove content to
make room (the cap is a reason to write the fix short or reject it). A finding whose fix needs the unit plan,
days.csv or any other file is not yours: list it under `LEAD:`.

Append to the same report a heading `## Fix` with one line per finding: `N. FIXED | REJECTED: why | LEAD: what`,
then `Count: fixed F, rejected R, lead L.` Edit only the section plans u{uu}-*.md and the report. Gate:
`python -X utf8 scripts/unitplan.py check {course}` must pass for your files; no em dashes.

## Both stages

No git commands of any kind. Python runs as `python -X utf8`. Never open: anything under .claude/, docs/Return/,
S:\CurioClass-spec2, data/closet/words, closet/words, data/media-manifest.txt, courses/math-4/, docs/courses/math-4/,
docs/courses/ela-6/, data/plans/math-4/, *-spine.md, data/units.csv, or any file with math-4 or ela-6 in its name.
Other agents work on other units at the same time: touch only your unit's files. Helper files go only in a folder
named for your job under the temp folder. Final message: one line,
`{course} u{uu} {stage}: <the Count line>`.
