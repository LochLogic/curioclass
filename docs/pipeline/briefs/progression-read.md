# Job: expert cold read of the {subject} progression (all grades)

You are the curriculum expert. Read docs/agents/EXPERT.md first and act as it says, then the subject lens
docs/agents/lenses/{subject}.md, then the subject's bar (math: docs/RUBRIC-MATH-K8.md; ELA: docs/RUBRIC-ELA.md;
science: docs/RUBRIC-SCIENCE.md; social studies: section 1 of docs/ADOPTION-BAR-SUBJECTS.md and
docs/courses/social-studies/STANDARD.md). Read cold data/progressions/{subject}.csv and the notes beside it. Do not open the subject's earlier
course pages under docs/courses/ or earlier reviews of them (a progression is read blind; the reconcile report,
docs/reviews/progression-{subject}-reconcile-*.md, may be read last, to see what it changed). You did
not write them. Run `python -X utf8 scripts/plan.py check` first and read its progression lines (if it cannot run, for
a missing module, run `python -X utf8 scripts/progression.py check {subject}`, which needs nothing outside the
standard library); the gate settles what it checks, so spend your read on what it cannot.

The data you must check, row by row where it says so:
- **Ownership:** every skill has one owning grade (the gate checks it is unique; you check it is the right grade
  against the standard and the base text's own order, and that no standard is owned in part with the rest lost).
- **Coverage:** every standard of every grade is named by at least one skill; list any that is not, and any skill
  that names no standard without a reason in its notes.
- **assumes and hands_on:** each `assumes` points at a skill an earlier grade teaches and that is the real
  prerequisite (not just an earlier topic); each `hands_on` is picked up by the next grade. A handoff that skips a
  grade, or a skill assumed two grades before it is taught, is a finding.
- **Models:** `model_in` and `model_out` follow one model (number line, tape diagram, timeline, map scale, a
  science model) through the grades without a gap, and no grade uses a model before the grade that introduces it.
- **Words:** `words` are taught before they are used, at a reading level that fits the grade.
- **cross_subject:** every lean on another subject names a skill that subject owns at or before that grade (for
  example a grade 6 science graph against grade 6 math). A lean on nothing is a finding.
- **Pace through the grades:** one grade carrying far more skills than its neighbours, or a strand that stops and
  starts again, is named with the counts.
- **The lens checklist** for the progression layer: work through it and mark each line met, missed or not
  applicable.

- **Stale notes.** Run `python -X utf8 scripts/stale.py check`; it catches marked ones. Look for the rest: any
  note, plan note or review result that says something is not yet done, placed, written or decided when the
  repository shows it is. Each is a finding (LAYER process, the fix is the rewritten note).
Write docs/reviews/progression-{subject}-{date}.md: what you read (files, row counts); a verdict (2 to 4
sentences); findings, most serious first, each with the skill ids, what is wrong, why it matters and the exact fix
(a row edit where possible); a table "Settled by the expert" for choices you decide; a short list "For Cory"
(anything that changes what a grade teaches, scope, money, people or audience). Tag each finding LAYER
(progression, standard, base text or process) and REPEAT (yes if the same kind as an earlier read in
docs/reviews/, else new).

Edit no file but your report. Last message: the verdict, the finding count, the report path.
