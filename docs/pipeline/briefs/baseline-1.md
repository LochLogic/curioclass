# Job: baseline 1, the whole-structure review ({part})

Added 2026-11-14 (PRODUCTION-PATH step 2, "Then baseline 1"). All four progressions and all 52 core course frames
exist, each frame read cold by the expert and by Codex, fixed band by band, lined up across subjects
(docs/reviews/frame-cross-subject-2026-11-14.md), and three reconciled with earlier work. Each of those reads looked
at one band. This review looks at the structure whole: what no band read could see. Do not repeat the band reads'
findings (docs/reviews/frame-*-2026-11-1[34].md and the fix reports); find what they could not.

You are the curriculum expert: read docs/agents/EXPERT.md and act as it says. Read AGENTS.md,
docs/PRODUCTION-PATH.md (steps 2 to 4), docs/GLOSSARY.md, docs/pipeline/briefs/frame-write.md (the format and its
lessons) and the lens for your part in docs/agents/lenses/. Run `python -X utf8 scripts/plan.py check` first; the
gates establish the coded placement and reference checks they implement (placement, owned and contributed standards,
day totals, the checks table, handoff ends, stale marks). They do not establish full standard meaning, within-year
availability, assessment completeness or the accuracy of unmarked status prose. Spend the read there.

## Parts
This brief runs as several readers, one part each. Your part: **{part}**.

**A subject column** (`subject=<subject>`): every frame of the subject, kindergarten to its last course, read side by
side with data/progressions/<subject>.csv and the subject's bar ({bar}).
- **The climb.** Each thread (a model, a practice, a kind of text, a kind of writing, an inquiry move, a lab skill)
  rises grade by grade with one wording, never repeats a grade's work at the same depth, never drops a step. Name
  any thread that stalls, jumps, doubles back or changes its name between grades.
- **Picks across the grades.** Texts, phenomena, cases, worked examples, countries and places: no repeats across
  grades unless on purpose and said; a fair spread of peoples, places and periods over K to 12.
- **Shape.** Units per course, days per unit, check and respond days, the time a day: where one grade breaks the
  pattern of its neighbours without a reason the frame gives.
- **Base text use.** Where a base text runs through several grades (IM, OpenSciEd, EL Education), its sequence is
  used the same way across them: what each frame keeps, merges or leaves out, and whether that is consistent.
- **Year-end and course-level checks.** Do they build across grades (what a grade 5 end check asks against grade 4)?

**B structure** (`subject=all`): the layers, the gates and the words, across all four subjects.
- **Alignment of layers.** Frames against progressions, progressions against standards, frames against
  data/courses.csv and the catalogue (the course id mismatch named in docs/reviews/frame-cross-subject-2026-11-14.md:
  recommend the fix), data/plans/frames.csv against the plan flow (scripts/plan_flow.py).
- **The gates.** What scripts/frame.py, progression.py, stale.py and plan.py check, what they miss that a reader
  found more than once today (the fix reports name repeats), and the cheapest gate rule that would catch each.
- **Vocabulary.** docs/GLOSSARY.md against what the frames actually say (unit, section, scope and sequence, exit
  ticket, check set, respond day, readiness check, bridge, lean): one name for one thing across subjects.
- **The grade as a whole.** For each grade, the four frames together: total minutes a day across subjects, weeks
  where two or three subjects put a major task or check in the same week, same-year leans that still assume the
  other subject teaches first.
- **The process.** The order of steps 3 and 4 in PRODUCTION-PATH.md against what the frames now hold: what the
  scope and sequence writers will need that no file gives them yet.

**C website** (`subject=site`): the website design check.
- Whether the site's structure (catalogue pages, topic pages, course and unit pages, the build scripts and data that
  make them; start from AGENTS.md and the scripts that build pages) still fits the hierarchy subject, course, unit,
  section, day. What a course frame's content would need from a course page, and what changes if the structure does
  not fit. Proposals only: nothing is rebuilt during planning unless Cory says.

## Report
docs/reviews/baseline-1-{slug}-{date}.md: what you read; a verdict (2 to 4 sentences); findings, most serious
first, each with the files and rows or units, what is wrong, why it matters and the exact fix (a file, a line or
cell, the new text); a table "Settled by the expert"; "For Cory" (only scope, money, people, audience, or a
proposal that changes the site); tag each finding LAYER (frame, progression, standard, base text, gate, site,
process) and REPEAT (yes if a band read already found that kind, else new).
Rules: no em dashes; "Curio Class" in full; no company names. Edit no file but your report. No git. Last message:
the verdict, the finding count, the report path.
