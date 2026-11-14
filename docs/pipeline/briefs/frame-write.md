# Job: write the course frames for {courses}

Added 2026-11-13 (PRODUCTION-PATH step 2). A course frame says what a course is: its grades, the standards and
progression skills it owns, its days, its units in order with a reason for each, its seams with the courses before
and after, and (where there is a base text) the source map. Its scope and sequence (step 3) then sets every day in
order, so a frame names no single day. You write the frames for adjacent courses so the seams between them line
up; other writers do the other bands at the same time, and the seam with a course outside your band is read
afterwards.

## Read first (in S:\CurioClass)
1. AGENTS.md, then docs/PRODUCTION-PATH.md, steps 2 to 4 only.
2. docs/agents/lenses/{subject}.md (the subject lens) and the subject's bar: {bar}
3. docs/pipeline/briefs/frame-read.md: what the two readers will check. Write to pass it.
4. The progression: data/progressions/{subject}.csv. Your courses own these rows: {rows}. Read the rows of the
   grade before and after your band too (the seams).
5. The standards: {standards}
6. The decisions: docs/agents/decisions/DESK-ANSWERS.md, entries dated 2026-11-12 and 2026-11-13 for {subject}.
7. What the progression reads left for the frames: the "For the course frames" sections of
   docs/reviews/progression-cross-2026-11-13.md and docs/reviews/progression-cross-codex-2026-11-13.md, and the
   progression reviews for {subject} (docs/reviews/progression-{subject}-*2026-11-13.md).
8. {extra}

## The file
One page per course: `S:\CurioClass\docs\courses\<slug>\frame.md`, where <slug> is given below. Sections, in order:

1. `# Course frame: <title>`, then one line: course id, grade or grades, "draft frame", and that the scope and
   sequence sets the days later.
2. `## The course in brief`, bullets, each starting with its bold label:
   - **Units.** the number of units (a bare number first, then any words).
   - **Days.** the number of teaching days (a bare number first), then the split: days in units, and days for
     course-level checks and respond days. The yardstick: a full-year course has 160 teaching days (a school year of
     about 180, less testing and breaks), a half-year course 80. A course may set fewer when what it owns does not
     need them (likely in kindergarten to grade 2, where social studies shares the day): say so and give the time a
     week it assumes. Never more without a reason.
   - **Standard.** how the course meets its standard (anchor, skills, check set, values rule).
   - **Base text.** the base text and its source map, or that the course has none and how sources are chosen.
   - Any other course-wide rule a unit writer must know (the inquiry arc, informed action, the reading level).
3. `## Seams`: two tables. "Picked up from <the course before>" (what it hands on, where this course picks it up)
   and "Handed on to <the course after>" (what this course hands on, what the next does with it). Take them from
   the progression's assumes and hands_on, not from memory. Kindergarten has no course before; the last course of
   the subject says where its threads end.
4. `## Models carried`: every model in the rows' model_in and model_out: where it comes from, the unit that
   introduces or first uses it, the units that use it again.
5. `## Units`: one table, columns exactly
   `| # | Unit and compelling question | Days | Skills | Owned standards | C3 | What students learn | Why this unit, here | Check set adds | Sensitive topics and teacher notes |`
   - **Skills:** the skill_id of every progression row the unit teaches, `; `-separated. Every row the course owns
     sits in exactly one unit. A unit that revisits an earlier row's skill names it in the text as review, never in
     this column.
   - **Owned standards:** the codes those rows own, as written in the rows.
   - **Why this unit, here:** why it is a unit and why it sits at this point (order of time, a skill or model it
     needs from an earlier unit, a seam).
   - Units in an order that uses a skill or model before it is taught fail the read.
6. `## Course-level checks`: where they fall (after which units), what each checks, the days they take.
7. `## Cross-subject`: every row's cross_subject lean, grouped by the other subject and grade: what this course
   needs, and when in this course's year. Same-year leans form the availability calendar (Codex's list, item 1):
   which unit of this course uses it and the earliest unit of the other course that may teach it, so the other
   subject's frame can honour it. The other subjects' frames are written later; record the need, do not guess
   their unit numbers.
8. `## For the lead`: anything that would change what a grade teaches beyond what the decisions settle, with your
   pick. Scope, money, people or audience questions go here, never decided by you.

## Rules
- The progression rows are the contract: place every owned row, change none. If a row is wrong, list it under "For
  the lead" with the fix; do not edit data/progressions/.
- Days fit what a unit owns: the read names a unit far over or under its share. Weigh the load notes in the rows,
  not equal shares per row.
- Sensitive content: name it in the unit's last column with a teacher note, following the lens and the values rule.
  No role play or simulation that puts a child in a victim's or perpetrator's place.
- No em dashes; "Curio Class" in full; no company names. Edit only your frame files. No git.
- Stale notes: a note that waits on other work starts `Pending(<file>, <file>#<text> or <plan node>):`; other
  work-status wording ("not yet placed", "to come") fails the gate. Run `python -X utf8 scripts/stale.py check`
  on your files before finishing.
- Run `python -X utf8 scripts/frame.py check <slug>` (the gate: sections, placement, owned standards, days;
  `python -X utf8 scripts/frame.py sync` first writes data/plans/frames.csv) and fix every FAIL.
- Check your own work with a short script in the scratchpad before finishing: every owned skill_id placed exactly
  once, every code in Owned standards found in those rows, days in units plus check days equal the total.

Final message, short: per course the units and days, the check result, the "For the lead" items, what you were
unsure of.
