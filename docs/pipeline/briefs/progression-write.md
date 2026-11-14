# Job: write the {subject} progression rows for grades {band}

Added 2026-11-13 (Cory: "write blind, then reconcile"). You write part of Curio Class's {subject} progression
(PRODUCTION-PATH step 1): one row per skill, the data every later layer (course frames, scopes and sequences,
units, days) is built from. Other writers do the other grade bands at the same time; a stitcher joins the bands,
then a reconciler compares the result with older work.

## Write blind
You may not open earlier Curio Class planning for this subject: anything under docs/courses/, docs/reviews/ or
data/progressions/ about {subject}, and data/units.csv, data/sequence.csv and courses/ (written days). They are
compared with your rows afterwards by a separate reconcile step (docs/pipeline/briefs/progression-reconcile.md), so
the progression is decided by the standards and the evidence, not by what happened to be written first.
{blind_extra}

## Read first (in S:\CurioClass)
1. AGENTS.md, then docs/PRODUCTION-PATH.md, the Step 1 part only.
2. docs/agents/lenses/{subject}.md (the subject lens: the errors a reader looks for).
3. The subject's bar: {bar}
4. docs/pipeline/briefs/progression-read.md: what the two readers will check. Write to pass it.
5. The standards: {standards}
6. The course list: data/courses.csv rows for {subject}. {courses}
7. Evidence for order: {evidence}

## The file
One CSV, UTF-8, header exactly
`strand,grade,skill_id,standard,assumes,hands_on,model_in,model_out,words,cross_subject,notes`
to `S:\CurioClass\data\progressions\parts\{part}.csv`.

- **strand:** {strands} (one per row).
- **grade:** {grades}.
- **skill_id:** lower case, hyphens, prefix by grade: {prefixes}. Unique, short, stable.
- **standard:** `; `-separated codes exactly as in the standards file. {coverage}
- **assumes / hands_on:** `; `-separated skill ids, both ends written: if A hands_on B, B assumes A. Assumes point
  only at an earlier grade, hands_on only at a later one, and a handoff is the real prerequisite (a skill used),
  not just an earlier topic. Prefer the next grade; a skip needs a reason in the notes. Across bands leave the
  cells empty and write the edges file instead.
- **model_in / model_out:** the thinking tools carried through the grades. model_in = models the row uses;
  model_out = models it hands on. A row introduces a model by having it in model_out without model_in. No row uses
  a model no earlier grade hands on and no row of its own grade introduces. Shared names: {models}. Add a name only
  when none fits, and say so.
- **words:** the key words the row teaches, at the grade's reading level.
- **cross_subject:** `math:<CCSS code> (reason)`, `ela:<CCSS code> (reason)`, `social-studies:<skill id or code>
  (reason)` or `science:<NGSS code> (reason)`, a real code at or before this grade. Empty when there is no real lean.
- **notes:** never blank. What the skill is, concretely enough that a unit writer builds the right days: the content,
  the reasoning that grows, the limits (the standard's own boundary statements where it has them). Safety and
  sensitive topics get "Teacher note: ...".

Size: one row per teachable skill, usually 1 to 4 standards each; roughly 12 to 30 rows per grade.

## The edges file
`S:\CurioClass\data\progressions\parts\{part}-edges.md`: "Needs from earlier grades" (row id and the skill it
needs, one line each) and "Hands on to later grades" (row id and what it gives).

## Rules
No em dashes; "Curio Class" in full; no company names. Edit only your files under data/progressions/parts/. No
git. Check your own work with a short script in the scratchpad before finishing (codes real, coverage, both ends of
in-band handoffs, models rule, no blank notes). Anything that would change what a grade teaches beyond what the
subject's decisions already settle: do not decide it; list it under "For the lead" with your pick.

Final message, short: rows per grade, coverage result, new model names, the "For the lead" list, what you were
unsure of.
