# Job: write the unit plan for unit {unit} of {course} (course days {first} to {last})

Write the unit plan for unit {unit}, to docs/courses/UNIT-PLAN.md, as docs/courses/{course}/s{uu}.md. Unit plans
follow the subject-wide order in PRODUCTION-PATH steps 3 and 4: every unit of the subject is planned before the probe,
and a preceding unit need not have written lessons. Section plans (docs/courses/{course}/u{uu}-N.md) follow in step 7,
except the section chosen for the probe, which the lead names.

Read first, in this order: docs/GLOSSARY.md; docs/courses/UNIT-PLAN.md (some of its fields are math only; it says
which); the course frame docs/courses/{course}/frame.md (unit {unit}'s row, its seams, models and cross-subject
leans); the course's scope and sequence (docs/courses/{course}/scope-and-sequence.md and its rows in
data/plans/{course}/days.csv: unit {unit}'s days, its reserved assessment slots, and the units around it); the
progression rows the unit owns (data/progressions/{subject}.csv); docs/APPROACH.md and the subject's approach page;
the subject lens docs/agents/lenses/{subject}.md and the subject's bar ({bar}); docs/courses/{course}/DEFAULTS.md and
TOOL-ASKS.md where they exist. Model on the newest planned unit plans of the same subject; until a subject has one,
on docs/courses/math-4/s03.md for the shape only.

Read the unit plan before yours and the one after (if written): the plan before's "carried" list is yours to keep or
change, and its last day's goal is where yours starts.

Every goal names the item that shows it: each day's exit and each end-of-unit assessment item, and which part of
the standard each covers (rule 19: the whole standard). The end-of-unit assessment sits inside the unit's days, and
the plan names its response time once (the same day or a later respond day). A readiness check, where the scope
and sequence reserves one (assess = readiness), is given before the unit opens, in the last ten minutes of the
previous unit's last day or of the respond day between the two units (unit 1: the last ten minutes of day 1, after
the hook), so its results shape day 1; day 1 of every other unit stays clean for the hook and the compelling
question (settled 2026-11-14, see DESK-ANSWERS). Rows used the year before or earlier the same year open as a
retrieval task inside a day instead (sequence-write.md rule 2). Your plan's readiness field names the day it is given;
plan the next unit's ten minutes on your last day. No number fact or list on an exit or assessment item may come from
a taught row. Anything that is a question of scope, money, people or audience goes to Cory in your report; everything
else you decide.

Do not write data rows or day files: the plan-data job does that after an expert reads your plan. Stay under the
word caps in UNIT-PLAN.md.

Last message (under 200 words): files written, decisions the expert should look at, questions for Cory.
