# SEL ownership form: a pedagogical check (2026-11-21)

## What I read

AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/sel.md, docs/courses/sel/STANDARD.md in full, and in
scripts/progression.py the docstring, codes(), other_grade(), the ownership and `~` handling, the handoff (assumes and
hands_on) checks and lean_timing. Career education's STANDARD.md was searched for its SEL leans only. No SEL
progression file exists yet (data/progressions/sel* is absent). No outside sources were read; judgments about spiral
teaching rest on the lens and on my own knowledge (from memory).

## Verdict: HOLDS WITH CHANGES

Band owners at the last grade (160 owned rows) is the right ownership form, and the 520-row alternative is not
needed. One part of the recommendation does not hold as written: `assumes` should not name "the same sub-skill in the
band before". It should name the same sub-skill in the year before. The left-out-unit rule also needs one word
changed. Two cautions for frame writers follow.

## Reasons

**1. Last grade or first grade, and what a teacher loses.** Last is right. The depth ladder (STANDARD section 3) puts
the band's full depth in its last year, and the gate already treats ownership that way: ELA band codes are "owned by
the band's last grade, started with ~CODE in the earlier one", and health and PE are owned where "first fully met".
Owning at the first grade would claim full depth in a year that teaches only the school-day version. A kindergarten
or grade 6 teacher does not lose a target, provided the target is the row and not the standard flag. The row (its
words, steps, models, notes and exit ticket) is what a teacher and a frame writer use; `~` only says the standard
is credited elsewhere. The risk is a reader taking "~" as "lesser" or "a mention". The wording below says a `~` row
is a full teaching row with its own check at its year's depth.

**2. Spiral teaching and "a school may leave out a unit".** The form supports the spiral, because every grade still
has its own row for all 40 sub-skills (13 x 40 = 520 rows exist either way; 160 is only the owned subset). Two
defects in the details:

- "Same sub-skill in the band before" is wrong for three of the four bands. Grade 4 and grade 5 would assume grade 2,
  skipping grade 3, and grade 5 (the owner) would not assume grade 4, though the ladder says grade 4 adds a second
  point of view and grade 5 adds a cost or pressure on top of it. That drops the real dependency inside the band, and
  the gate would raise a "skips grades" note on each such handoff. The year-before chain (K to 1 to 2 to 3 and so on)
  passes the gate as it stands: `~` rows are ordinary rows, and assumes only needs an earlier-grade row with the
  matching hands_on.
- "The previous year's owner row" does not hold for a grade 4 unit. Its owner row is grade 2, a picture-and-aloud
  level, while the real prerequisite is grade 3 (a named strategy with steps). Grade 2 is too low a floor. The rule
  should be "the previous year's row for that sub-skill, owner or `~`", and, where that unit was left out, the nearest
  earlier year that was taught. A readiness item that must work after a gap should check the one-step form of the
  skill, and its row note should say so. The gate cannot check this (it knows nothing of left-out units), so the
  frame writer and reviewer carry it.

**3. Leans from career education and library.** Leans work, with one habit needed. lean_timing accepts a skill id
(the grade of that row) or a standard code (the earliest grade of any row that owns or `~`-contributes). A lean by
code is satisfied from kindergarten, so the "taught by then" check says nothing. A lean by an owner row's id (grade 5,
say) wrongly fails a grade 4 career row that SEL has in fact taught since grade 3. Leans should name the SEL row of
the year whose depth is needed, which can be a `~` row. Career's STANDARD already says leans are named "by progression
row id", which fits.

**4. What could mislead a frame writer.**

- "160 rows" read as the row count. There are 520 rows; 160 own. A writer may skip the `~` rows or write them as thin.
- A `~` row's one-line note being all the row says. Its words, steps, models and notes must be written in full.
- "Full depth" at the last grade being taken to mean the earlier years teach less of the skill. They teach the same
  skill with fewer pressures; the grade table says each grade teaches all 40 once.
- The depth ladder restarts at each band's first year (grade 3, 6, 9), so the handoff from the previous band's owner
  row is the one real step up and should be said in the grade 3, 6 and 9 notes.

**The codes() whitespace collapse.** It does not change the choice of form, but it blocks the gate for either form.
`CASEL.Social Awareness.1`, `CASEL.Relationship Skills.1` and `CASEL.Responsible Decision-Making.1` all become one
code each (`CASEL.Social`, `CASEL.Relationship`, `CASEL.Responsible`), so 24 of the 40 sub-skills (SO, RS, RD) cannot
be told apart. A row also cannot name SO1 uniquely, because the standard column is checked against that collapsed
list. Under the 160-row form the collapsed codes would be flagged "owned by grades 2, 5, 8, 12", which would be a
false alarm. Until codes() splits on the tab only (as scripts/standards.py does), the gate can neither confirm one owner
per sub-skill nor catch a missing one for those 24. SA and SM (Self-Awareness, Self-Management) have no space and are
unaffected. The fix is needed before the first SEL progression is checked, whichever form is chosen.

## Replacement for the recommendation (the "Ownership, for the progression" paragraph)

**Ownership, for the progression.** Recommended: one owned row per sub-skill per band, so 40 sub-skills by four bands
is 160 owned rows. A band's owner year is its last grade (2, 5, 8 and 12), the year the sub-skill is met at the band's
full depth. Every grade year still has its own row for all 40 sub-skills (520 rows in all), and the other years of the
band carry the id as `~ID`. A `~` row is a full teaching row, not a lesser one: it has its own words, steps and exit
ticket at its year's depth, and a one-line note on how that year differs. Each row's `assumes` names the same
sub-skill in the year before (a `~` row or an owner row; kindergarten assumes nothing for it), so a band's later years
build on its earlier ones and the first year of a band builds on the previous band's owner row. The grade table below
stays the placement, and every year still teaches all 40 once. Other subjects' leans name the SEL row of the grade
whose depth they need. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-1) The choice waits on Cory (the
alternative is changing the layer 4 gate so that each sub-skill is owned once per grade year).

Also in section 5, item 6, change "(its readiness item rests on the previous year's owner row)" to "(its readiness item
rests on the previous year's row for that sub-skill, or, if that unit was left out too, the nearest earlier year that
was taught, and checks only the one-step form)".

Not covered: whether career education and library lean by id or code in practice (their progressions were not read),
and the codes() fix itself (known, not made here).
