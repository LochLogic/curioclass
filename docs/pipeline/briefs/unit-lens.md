# Job: one focused read of one unit plan, through one lens ({lens}), {course} unit {unit} (Codex)

You read docs/courses/{course}/s{uu}.md through ONE lens and report what is wrong. You edit no file: your last
message is your findings, and a fixer applies them after two other lens reads. A narrow read done fully is the job;
do not drift into the other lenses (named below so you can skip them).

Read first: AGENTS.md, docs/courses/UNIT-PLAN.md (the fields and their rules), the writer's brief
{writer_brief} (its settled rules hold), the unit plan, its rows of data/plans/{course}/days.csv and
source-map.csv, and docs/courses/{course}/scope-and-sequence.md for this unit. Run
`python -X utf8 scripts/unitplan.py check {course}` and include any failure or note for s{uu}.md.

## The lenses

**assessment** (yours if {lens} = assessment): field 5 items, field 6 error register, field 7 groups and the daily
exit table.
- Each error letter holds one misconception (no two claims joined; no "D or I" or "(D, I)" on one wrong answer).
- Each wrong answer sits under the letter whose text describes it; every letter used is in the register.
- Each answer key, sample and look-for is right (work every key yourself before reading it) and would not pass a
  wrong answer; a sample says no more than its source or stimulus holds.
- Nothing is scored from work made the day the topic is first taught, or from work made in the same period that
  scores it. Scored work is made on an earlier day and gets written feedback and a chance to revise before the score;
  that feedback and revision may fall on the scoring day itself, before the score (UNIT-PLAN field 5). Do not report
  a revision on the scoring day as a fault.
- A day exit gives a fresh stimulus (a new case, source, problem or text); it does not rehearse an end item or redo the
  day's worked example with the nouns swapped.
- Field 7: every error letter has a group and a repair that is not the next worked example.

**sources** (yours if {lens} = sources): field 10 and every text, source or data set the unit names.
- Verified or none: every text the days will quote names where its words can be checked for free (a free text
  archive, a government or museum page, the publisher's own page). A text found only in paid editions is named and
  described, never quoted, from a free secondary source.
- No end item or exit is built on our own summary of a source where the source itself is needed.
- Science: every investigation's materials are school-safe and named; data sets have a source. ELA: every anchor and
  paired text has an edition and a rights note; excerpt lengths fit the rights. Math: every outside task or context
  names its source; no invented statistic is presented as real.
- No company names in student, teacher or family copy; images or people named have a source.

**sequence** (yours if {lens} = sequence): fields 1 to 4 and the day list.
- Every owned standard or code is taught, practised and checked inside the unit (or the plan says where else).
- Minutes add up on every day; check and respond days match days.csv; the day list matches days.csv.
- Ask for minute-by-minute day budgets, daily exits or day plans only where UNIT-PLAN puts them in the unit plan; a
  unit of several sections leaves them to its section plans. The day list is generated: a fault in it or in days.csv is
  a finding for the lead (say so), not something the fix step can change.
- Hand-offs: what the unit needs from earlier units is named and was taught there (scope-and-sequence); what later
  units need is left in place.
- Science: the anchoring phenomenon or design problem drives the days, and each performance expectation has its three
  dimensions. ELA: the text set builds knowledge; writing and speaking tasks follow the texts. Math: clusters carry
  their stated weight; practice builds from concrete to abstract where the grade needs it.

## Your report (last message)

One line per finding, numbered, most serious first:
`N. [field] what is wrong | why it matters | exact fix`
Then one line: `Count: N findings (lens {lens}).` If you find nothing, say `Count: 0 findings (lens {lens}).` and why
the unit holds. No em dashes. Do not open: docs/courses/ela-6/, docs/courses/ela-6-spine.md, docs/courses/math-4/,
docs/courses/math-4-spine.md, docs/courses/math-3-5-progression*.md, docs/courses/science-4-spine.md,
docs/courses/NEXT-SPINES.md, data/plans/math-4/, data/units.csv, courses/, im-g4-draft-map.csv,
docs/reviews/*reconcile*, *math-4*, *ela-6*. No git.
