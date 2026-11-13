# Job: expert cold read of the course frame of {course}

You are the curriculum expert. Read docs/agents/EXPERT.md first and act as it says, then the subject lens
docs/agents/lenses/{subject}.md and the subject's bar (math: docs/RUBRIC-MATH-K8.md; ELA: docs/RUBRIC-ELA.md;
science: docs/RUBRIC-SCIENCE.md; social studies: section 1 of docs/ADOPTION-BAR-SUBJECTS.md and
docs/courses/social-studies/STANDARD.md). Read cold the frame docs/courses/{course}/frame.md and its rows in
data/plans/frames.csv, and, where the course has a base text, data/plans/{course}/source-map.csv. You did not write
them. Read beside them the progression rows for the course's grades (data/progressions/{subject}.csv) and the
frames of the course before and after it in the same subject. Run `python -X utf8 scripts/plan.py check` first; the
gate settles what it checks, so spend your read on what it cannot.

The data you must check:
- **Owned skills:** every progression skill owned by the course's grades is placed in exactly one of its units,
  and no unit teaches a skill another grade owns without a reason (review or extension, named as such).
- **Standards in full:** every standard the course owns is taught in full somewhere in its units; a standard
  taught only in part is a finding.
- **Units and reasons:** each unit has a reason that holds (why it is a unit, why it sits where it does); units in
  an order that uses a skill or model before it is taught are a finding.
- **Days:** the course's days (frames.csv) fit a school year with room for course-level checks and respond days;
  each unit's days fit what it owns (a unit far over or under its share is named with the counts).
- **Source map** (base-text courses only): every base lesson is placed in one unit or listed as left out with a
  reason; unit edges and day counts follow the base text's own order unless a reason is given; no NC or reference
  source is mapped (docs/sources/BASE-TEXTS.md).
- **Seams:** what the frame before hands on is picked up here, and what this frame hands on matches the next one.
- **Cross-subject:** where the course leans on another subject, that subject's frame for the same grade teaches it
  first.
- **The lens checklist** for the course frame layer: each line met, missed or not applicable.

Write docs/reviews/frame-{course}-{date}.md: what you read; a verdict (2 to 4 sentences); findings, most serious
first, each with what is wrong, why it matters and the exact fix; a table "Settled by the expert"; a short list
"For Cory" (scope, money, people or audience only). Tag each finding LAYER (frame, progression, standard, base text
or process) and REPEAT (yes if the same kind as an earlier read in docs/reviews/, else new).

Edit no file but your report. Last message: the verdict, the finding count, the report path.
