# Expert cold read: course frame, Grade 5: The United States to the Civil War, and the Fight for Civil Rights (2026-11-13)

Brief: docs/pipeline/briefs/frame-read.md, {course} = social-studies-grade-5, {subject} = social-studies. The reader
did not write the frame and had no part of the conversation that made it.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; docs/ADOPTION-BAR-SUBJECTS.md section 1;
  docs/courses/social-studies/STANDARD.md.
- The frame, docs/courses/social-studies-grade-5/frame.md, in full; its line in data/plans/frames.csv (10 units, 160
  days); the 21 grade 5 rows of data/progressions/social-studies.csv; the grade 5 anchor text (MA.5.*,
  data/standards/ma-hss-2018.txt), every code and lettered part.
- Neighbours: docs/courses/social-studies-grade-4/frame.md (before), docs/courses/social-studies-grade-3/frame.md
  (threads handed across grade 4), and docs/courses/world-geography-and-ancient-civilizations-i/frame.md (after),
  its "Picked up from Grade 5" table; the K to 2 rows for earlier mentions of the same people.
- docs/reviews/progression-social-studies-2026-11-13.md and its codex and fixes reads.
- Gates: `python -X utf8 scripts/plan.py check` (social-studies-grade-5: 0 failures, 10 units, 160 days, 152 in
  units, 8 for checks and respond days); `python -X utf8 scripts/stale.py check` (0 failures). No base text.
- Not opened: anything under S:\CurioClass-sources\_calibration. No web sources fetched on this read.

## Verdict

The frame is sound and strong: every anchor code and lettered part is placed, the ten units run in time order with
reasons, the two-source skill is taught before anything checks it, and the values-rule calls (Worcester v. Georgia,
the seceding states' own words, the 2015 ruling) are made where they belong. The biggest risk is two pieces of
required content that sit only in "Check set adds" as candidates: the origins of slavery, which MA.5.T1.5 itself
requires, and the amendment process, which unit 8 says it needs from unit 5. The one change that matters most is
to make both firm parts of their units (2 and 5), and to give unit 9, the content the year's research rests on,
the days unit 10 does not need.

## Findings, most serious first

**1. The origins of slavery are a candidate, not content.** LAYER standard (row) and frame. REPEAT yes (missing
parts of standards in the progression reads). Confidence: firm (MA.5.T1.5: "Describe the origins of slavery").
Unit 2 lists "slavery's start in Virginia in 1619" only under "Check set adds" as a California candidate, and
ss5-slavery-colonies' notes never name the origins. A unit plan may drop a candidate; it may not drop an anchor
part, so as written the standard is taught in part. Fix: add to ss5-slavery-colonies' notes and unit 2's "What
students learn": "how slavery began in the English colonies: Africans brought to Virginia in 1619, and colony laws
from the 1660s that made slavery lifelong and passed it from mother to child, so that it became tied to race";
move the 1619 item out of "Check set adds" (leave enslaved people's resistance in the southern colonies there).
The unit writer checks the law dates against the record.

**2. Unit 8 relies on an amendment process that unit 5 only might teach.** LAYER frame. REPEAT new. Confidence:
firm. Unit 8's reason says it needs "unit 5's branches and amendment process for the amendments", and unit 8 owns
D2.Civ.12 (how people change rules and laws); unit 9 then teaches the 19th Amendment. But unit 5 carries the
amendment process only as a New York and Tennessee candidate. A model used before it is taught fails the read.
Fix: add "how an amendment is added (proposed by Congress, ratified by three-fourths of the states), with the Bill
of Rights as the first case" to unit 5's "What students learn" and to ss5-constitution's notes; drop it from unit
5's "Check set adds". (Settled below.)

**3. Unit 9 is short for what it holds; unit 10 has days to spare.** LAYER frame. REPEAT new. Confidence: a
judgment call. Unit 9 has 14 days for three rows (Jim Crow; women's suffrage from the 1860s to 1920; the
movements to 2015) plus the 1950s and 1960s movement's core events the frame adds (For the lead 1): about 4.7 days
a row and a century and a half of content, and it is the knowledge unit 10's research and check 2 rest on. Unit 10
has 16 days, teaches no new content, and splits about 11 for research and 5 for action. Unit 6 (17 days, four rows)
and unit 8 (14 days, two rows with ten codes and parts) are tight too but hold. Fix: unit 9 to 16 days, unit 10 to
14 (about 10 for research and critique, 4 for the action); the total stays 152 in units. (Settled below.)

**4. No row names the civil rights movement students learn before it serves as a model.** LAYER progression.
REPEAT new (raised by the frame writer, For the lead 1, not by an earlier read). Confidence: firm (MA.5.T5.9 cannot
be taught in full without it). Agreed with the frame and still open: ss5-civil-rights-movements' notes jump to how
the movement became a model. Fix as the frame says: add to the row's notes "The movement itself first: Brown v.
Board of Education (1954), the Montgomery bus boycott (1955 to 1956), the March on Washington (1963), the Civil
Rights Act of 1964 and the Voting Rights Act of 1965, with Rosa Parks, Martin Luther King Jr., Fannie Lou Hamer and
others"; then For the lead 1 becomes "done" and is removed.

**5. ss5-independence-war uses money with no money row behind it.** LAYER progression. REPEAT yes (handoff gaps in
the progression reads). Confidence: likely. The row owns D2.Eco.11 (inflation, deflation and unemployment after the
war, a farmer's debt taking more crops to repay). Money, prices and debt were last taught in ss3-money-saving, two
years earlier, and grade 4 carries no money content; the row assumes only ss3-founding-ideas. The progression
review said "grades 4 and 5 carry no money content" (row ss6-phoenician-trade); this read disagrees, since this row
is money content. Fix: ss5-independence-war `assumes` adds ss3-money-saving, "content revisited: opens with a short
retrieval task on what money and a price are and what a loan is"; ss3-money-saving `hands_on` adds
ss5-independence-war; this frame's "Picked up" table adds the line (unit 4).

**6. The sensitivity flags miss hard-history units.** LAYER frame. REPEAT new. Confidence: likely. Units 1, 2, 7 and
9 are flagged for the fresh-agent sensitivity read. Unit 8 (the Civil War, slavery's end, Reconstruction and the
violence against it), unit 6 (the Purchase and the nations who held the land; York, an enslaved man; Washington and
Jefferson as enslavers), unit 4 (Native and African people on both sides; who the Declaration left out) and unit 5
(the Three-Fifths Compromise) are not. Fix: one line in "The course in brief": "Every unit gets the fresh-agent
sensitivity read (bar item 12); units 1, 2, 6, 7, 8 and 9 carry Native or hard-history content and need the
qualified person's read when one is found"; add "Flagged for the sensitivity read" to units 4, 5, 6 and 8.

**7. One seam word disagrees with grade 6.** LAYER frame (the grade 6 frame). REPEAT new. Confidence: firm. Grade 5
hands on sourcing done unprompted and two accounts weighed by their sources (ss5-sourcing-corroboration, unit 3),
and grade 6's "Picked up" table agrees, but the same table calls ss6-hammurabi-code (its unit 4) "the first full
sourcing step". A grade 6 writer will reteach sourcing from the start. Fix (in the grade 6 frame): "the first full
sourcing step on an ancient source, at grade 5's depth: who, when, for whom, why, unprompted".

**8. Stale note.** LAYER process. REPEAT yes (stale notes in the progression reads). Confidence: firm. For the lead 4
says to run `frame.py sync` for grade 5; data/plans/frames.csv already holds `social-studies-grade-5,10,160`. Fix:
drop the item, or "frames.csv holds grade 5 (10 units, 160 days)".

## What is right and should not be touched

- Ten units in time order, with slavery in the colonies its own unit so MA.5.T1.7a to d gets full days, and unit
  3's chain ending when the British leave Boston so unit 4 opens on the Declaration.
- The two-source skill taught in unit 3 and kept out of every earlier task and check; no counterclaim asked
  (C3 places claims with counterclaims at D3.4.6-8).
- The seam tables match the rows and grade 6's "Picked up" table (apart from finding 7), including the retrieval
  tasks for the threads handed across grade 4.
- Values-rule calls: the seceding states' own declarations on the war's cause; Worcester v. Georgia and the 2015
  ruling stated as rulings; LGBTQ people where the history includes them, at grade level.
- Unit 10 kept for research and action only, with the movements taught as content first in unit 9.
- Day ranges in the calendar match the unit days exactly.

## What I could not judge

- The check-set candidates against California, Tennessee and New York text: unit-plan work, not reread here.
- The dates in finding 1's fix (the 1660s Virginia laws) rest on memory; the unit writer checks them.
- The ELA, math and science grade 5 frames are not written, so the calendar's "should teach it by" cannot yet be
  checked against them.

## Sources

- data/standards/ma-hss-2018.txt (MA.5.*, every lettered part): findings 1 and 4.
- C3 Framework 2013, from memory and the repo's ids: D2.Civ.12.3-5 and D2.Eco.11.3-5 (findings 2 and 5); D3.4.6-8
  for where the counterclaim begins.
- docs/reviews/progression-social-studies-2026-11-13.md: disagreed with on money (finding 5).
- Defects are not logged with `plan.py defect` on this read, because the caller allowed only the report to be
  written; the caller may log findings 1 to 8 with found_by `expert`.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| 1. The amendment process is taught in unit 5, not left as a candidate | Unit 8 and unit 9 need it, and the Bill of Rights is its first case (finding 2) | docs/courses/social-studies-grade-5/frame.md unit 5; data/progressions/social-studies.csv (ss5-constitution notes) |
| 2. Unit 9 has 16 days and unit 10 has 14 (about 10 research and critique, 4 action) | Unit 9 is the content the research rests on; unit 10 teaches nothing new (finding 3) | frame.md units 9 and 10, and the calendar's day ranges for unit 10 (days 147 to 160) |
| 3. For the lead 3 (ten units) stands as decided in the frame | Item level; each split has a stated reason | none |

## For Cory

- **Time a day (audience).** 160 days at about 40 minutes a day, as in grades 3 and 4; grade 5's load (21 rows,
  about 80 codes and parts) needs all of it. Whether schools give a daily block is yours.
