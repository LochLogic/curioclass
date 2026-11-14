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

## Lessons from the social studies frames (added 2026-11-14)
The 15 social studies frames were read by the expert and by Codex and fixed (docs/reviews/frame-*-fixes-2026-11-13.md).
These findings came back course after course. Write so none of them comes back:
1. **A respond day after each course-level check,** counted in the course's days.
2. **Check-set cells start "Candidate: ...":** the unit plan settles them.
3. **The time a day is stated** (minutes per lesson, lessons a week), and why the day total fits it.
4. **Standards in full.** Every lettered part and every clarification a standard names is taught somewhere, and the
   unit that teaches it says so. A standard is never quietly narrowed to its headline.
5. **Each thread starts where it is first used.** A readiness check on an earlier grade's skill sits in the first
   unit that needs it; a model is introduced before any unit uses it.
6. **"First" claims are checked against the grade before** ("the first full sourcing step", "introduces"). One
   thread keeps one wording across grades.
7. **Both ends of every handoff.** Where the frame needs a link the progression lacks, write it under "For the
   lead" with the row change; the fixer edits both rows.
8. **Same-year cross-subject leans carry an "if later" line:** what the unit does if the other subject has not
   taught it yet (for example, the unit teaches the percent it needs itself).
9. **Days by load.** Weigh each unit's rows and notes; the readers named units short for what they own.
10. **Questions answerable from the unit.** A unit's compelling or driving question can be answered from the
    evidence the unit itself studies.
11. **Picks named, not left open,** where the standard allows (a worked case, a country, a text, a phenomenon), and
    chosen so they do not repeat another grade's picks.
12. **Sensitivity.** A "Sensitivity reads" line in the brief: every unit gets the fresh-agent read; units that need
    a community or qualified reader are named (who, and any pay, is Cory's).
13. **No math ahead of math.** A unit uses no number work the math progression has not taught by then (coin values,
    percent, negative numbers, scale).
14. **A paper path** beside any electronic tool, and no student account.
15. **No status lines about other files.** Stale wording in shared docs goes under "For the lead" with the
    replacement text.

## Rules
- The progression rows are the contract: place every owned row, change none. If a row is wrong, list it under "For
  the lead" with the fix; do not edit data/progressions/.
- Days fit what a unit owns: the read names a unit far over or under its share. Weigh the load notes in the rows,
  not equal shares per row.
- Sensitive content: name it in the unit's last column with a teacher note, following the lens and the values rule.
  No role play or simulation that puts a child in a victim's or perpetrator's place.
- No em dashes; "Curio Class" in full; no company names. Edit only your frame files. No git.
- Base texts: where the subject has one (IM for math, OpenSciEd for middle school science, EL Education for ELA K to
  5), the frame ends with a `## Source map` section: a table placing every base unit (and its lesson range) in one
  of the course's units, from the source store (S:\CurioClass-sources) and docs/sources/BASE-TEXTS.md; a base lesson
  left out is named with the reason. The day-level data/plans/<course>/source-map.csv comes with the scope and
  sequence (step 3), not now.
- Stale notes: a note that waits on other work starts `Pending(<file>, <file>#<text> or <plan node>):`; other
  work-status wording ("not yet placed", "to come") fails the gate. Run `python -X utf8 scripts/stale.py check`
  on your files before finishing.
- Run `python -X utf8 scripts/frame.py check <slug>` (the gate: sections, placement, owned standards, days;
  `python -X utf8 scripts/frame.py sync` first writes data/plans/frames.csv) and fix every FAIL.
- Check your own work with a short script in the scratchpad before finishing: every owned skill_id placed exactly
  once, every code in Owned standards found in those rows, days in units plus check days equal the total.

Final message, short: per course the units and days, the check result, the "For the lead" items, what you were
unsure of.
