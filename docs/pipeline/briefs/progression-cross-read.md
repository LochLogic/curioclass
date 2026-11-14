# Job: expert read across all four core progressions

You are the curriculum expert. Read docs/agents/EXPERT.md first and act as it says, then the four subject lenses in
docs/agents/lenses/ (math, ela, science, social-studies). Each subject's progression has already had its own cold
read and fix pass (docs/reviews/progression-<subject>-*.md); do not repeat them. This read is the cross-subject
column: what no single-subject read could see.

Read data/progressions/social-studies.csv, science.csv, ela.csv and math.csv (columns
`strand,grade,skill_id,standard,assumes,hands_on,model_in,model_out,words,cross_subject,notes`; lists are "; "
separated; `~CODE` marks a row that contributes to a standard another row owns). Run
`python -X utf8 scripts/plan.py check` first; the gate already proves every cross_subject reference exists and is
owned. Spend your read on what it cannot check.

Check, with row ids and grades:
- **Timing of leans.** Every cross_subject lean uses a skill the other subject has taught by then, at the depth
  needed (not only named). Look hardest where subjects meet: science and math (measurement and units, graphs,
  ratios and rates, negative numbers, exponents and scientific notation, linear and exponential functions,
  statistics, algebra in Chemistry and Physics, trigonometry and vectors in Physics); social studies and math
  (timelines and number lines, maps and scale, percentages, economics graphs, data); ELA and both (reading
  informational text, argument and claim-evidence-reasoning, research and citation, writing to sources). A row
  that needs a skill the other subject teaches a year or more later is a finding, with the fix (move, add a
  just-in-time teach in the row's notes, or lower the demand).
- **Missing leans.** Places where two subjects clearly teach the same thing in the same or nearby grade and
  neither row says so (double teaching, or a chance to reinforce). Name the pairs worth wiring; skip the trivial.
- **One name for one thing.** The same model, practice or term named differently across subjects (for example
  claim-evidence-reasoning, data-graph against dot-plot or histogram, timeline against number-line), or one term
  defined two ways. Pick one name or say why two are right.
- **Load per grade.** Rows per grade across all four subjects together, and any grade where several subjects peak
  at once or where a hard new idea lands in two subjects in the same year. Rows are not days; say what the course
  frames should watch.
- **Topic threads.** ELA knowledge topics and social studies and science content: where a reading topic set
  matches what that grade studies in science or social studies, and where it repeats or clashes.
- **Sensitive and hard topics** (evolution, climate, slavery and genocide, puberty and health where they appear)
  handled at matching ages and with the same stance across subjects.

- **Stale notes.** Run `python -X utf8 scripts/stale.py check`; it catches marked ones. Look for the rest: any
  note, plan note or review result that says something is not yet done, placed, written or decided when the
  repository shows it is. Each is a finding (LAYER process, the fix is the rewritten note).
Write docs/reviews/progression-cross-{date}.md: what you read (files, row counts); a verdict (2 to 4 sentences);
findings, most serious first, each with the skill ids in each subject, what is wrong, why it matters and the exact
fix (a row edit where possible: which file, which row, which column, new value); a table "Settled by the expert"
for choices you decide; a short list "For Cory" (only what changes what a grade teaches, scope, money, people or
audience); a table of rows per grade per subject; and a list "For the course frames" (what step 2 must handle,
not a progression fix). Tag each finding LAYER (progression, standard, base text or process) and REPEAT (yes if
the same kind as an earlier read in docs/reviews/, else new).

Rules: no em dashes; "Curio Class" in full. Edit no file but your report. Last message: the verdict, the finding
count, the report path.
