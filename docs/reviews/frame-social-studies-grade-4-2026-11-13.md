# Expert cold read: course frame, Grade 4: North America, Its Land and Peoples (2026-11-13)

Brief: docs/pipeline/briefs/frame-read.md, {course} = social-studies-grade-4, {subject} = social-studies. The reader
did not write the frame and had no part of the conversation that made it.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; docs/ADOPTION-BAR-SUBJECTS.md section 1;
  docs/courses/social-studies/STANDARD.md.
- The frame, docs/courses/social-studies-grade-4/frame.md, in full; its line in data/plans/frames.csv (7 units, 160
  days); the 17 grade 4 rows of data/progressions/social-studies.csv; the grade 4 anchor text (MA.4.*,
  data/standards/ma-hss-2018.txt), every code and lettered part.
- Neighbours: docs/courses/social-studies-grade-3/frame.md (before) and docs/courses/social-studies-grade-5/frame.md
  (after), with their rows; the grade 2 frame for Ellis Island and Angel Island.
- Cross-subject: docs/courses/math-4-spine.md (4.MD.A.2 in unit 15, days 124 to 131; 4.NBT.B.4 in unit 9, days 72 to
  77) and docs/courses/science-4-spine.md (4-ESS3-1 in unit 2, days 13 to 31; 4-ESS1-1 in unit 6, days 80 to 87;
  4-ESS3-2 in unit 8, days 97 to 104).
- docs/reviews/progression-social-studies-2026-11-13.md and its codex and fixes reads.
- Gates: `python -X utf8 scripts/plan.py check` (social-studies-grade-4: 0 failures, 7 units, 160 days, 150 in
  units, 10 for checks and respond days); `python -X utf8 scripts/stale.py check` (0 failures). No base text.
- Not opened: anything under S:\CurioClass-sources\_calibration. No web sources fetched on this read.

## Verdict

The frame is sound: every anchor code and lettered part is owned and placed, the order follows the anchor and
time, the region sub-topics are grouped by theme with a stated reason, and the cross-subject calendar matches the
grade 4 math and science spines on file. The biggest risk is unit 5, where "each gain told with the peoples whose
lands changed hands" names only Native nations of the continent and Mexico, and leaves out Native Hawaiians,
Alaska Native peoples and Puerto Ricans, whose lands are three of the six gains the unit teaches. The one change
that matters most is to name those peoples and the 1893 overthrow of the Hawaiian Kingdom in unit 5 and its row.

## Findings, most serious first

**1. Unit 5 leaves out three peoples in the history it teaches.** LAYER frame and progression (ss4-westward-growth).
REPEAT new. Confidence: likely (MA.4.T4.2 names Alaska, Hawaii and Puerto Rico; values rule c and bar item 12;
the 1993 Apology Resolution, Public Law 103-150, from memory, acknowledges the US part in the 1893 overthrow). The
unit's gains include Alaska (1867), Hawaii (1898) and Puerto Rico (1898), but the row and the frame tell each gain
"with the Native nations and the people of Mexico". A student learns that Hawaii "was gained" with no word of the
Hawaiian Kingdom, Queen Liliuokalani or Native Hawaiians today; this is the "group present in the history left
out" fail of bar item 11. Fix: add to ss4-westward-growth's notes and unit 5's "What students learn": "Alaska
bought from Russia in 1867 with no say for the Alaska Native peoples who lived there; the Hawaiian Kingdom
overthrown in 1893 by a group of businessmen backed by US sailors, and Hawaii annexed in 1898 although many Native
Hawaiians signed petitions against it; Puerto Rico taken in the war with Spain in 1898. Alaska Native peoples,
Native Hawaiians and Puerto Ricans today." Add the overthrow to unit 5's sensitive topics column and flag it for
the sensitivity read. The unit writer checks each fact against the record.

**2. ss4-states-and-statehood uses the founding ideas without assuming them.** LAYER progression and frame (seam).
REPEAT yes (handoff gaps in the progression reads). Confidence: firm. MA.4.T4a.3 asks why statehood beat being a
British colony in the 1700s, which needs ss3-founding-ideas (unfair treatment, representation, consent of the
governed). The row assumes ss3-timeline, ss3-home-region and ss3-state-constitution only, and the grade 3 and grade
5 frames both say grade 4 teaches no founding content, so ss5-independence-war's retrieval treats the ideas as
two years cold. Fix: ss4-states-and-statehood `assumes` adds ss3-founding-ideas, with "opens with a short
retrieval task: what colonists said was unfair and what consent of the governed means"; ss3-founding-ideas
`hands_on` adds ss4-states-and-statehood; this frame's "Picked up from Grade 3" table adds the line (unit 6); the
paragraph under "Handed on to Grade 5" changes "Grade 4 teaches no founding, money or slavery-trade content" to
"Grade 4 keeps the founding ideas in use in unit 6 (ss4-states-and-statehood) and teaches no money or
slavery-trade content". The grade 3 report (finding 4) carries the matching seam fix.

**3. branches-of-government is called new in grade 4.** LAYER frame and progression. REPEAT yes (model gaps in the
progression reads). Confidence: firm. The models table says "New in grade 4 (names only)", but grade 3 unit 2
compares the state constitution with the US Constitution's three parts, and unit 6 teaches what a constitution is
for. Fix: the models table reads "From ss3-state-constitution (three parts named); unit 6 (ss4-national-capital)
names the buildings and who works in each"; ss4-national-capital `model_in` adds branches-of-government (the grade 3
report, finding 5, adds the grade 3 `model_out`).

**4. Unit 3's timeline spans 15,000 years before the to-scale timeline is taught.** LAYER frame. REPEAT new.
Confidence: likely. ss4-first-peoples-evidence uses the timeline model on evidence "about 15,000 years ago or
earlier", but grade 3 taught years, decades and centuries, unit 4 first draws a timeline to scale, and deep time
(millennia) is grade 6's (ss6-timeline-deep-time). A writer who asks grade 4 students to build that line in unit 3
asks for a scale nobody has taught. Fix: unit 3 reads a given timeline marked in thousands of years and places two
or three dates on it; students do not build one; add this line to unit 3's "What students learn" and to the row's
notes. (Settled below.)

**5. MA.4.T4d.5 is taught in part.** LAYER standard (row). REPEAT yes (missing parts of standards in the progression
reads). Confidence: firm. The standard asks the Southwest map to show "Native peoples' movements and reservations";
ss4-state-maps and unit 6 keep "homelands and reservations" and drop the movements. Fix: ss4-state-maps' notes and
unit 6 read "Native nations' homelands, movements (forced ones included, such as the Navajo Long Walk of 1864) and
reservations today, from the nations' own pages", with the Long Walk added to unit 6's sensitive topics column.

**6. The sensitivity flags are uneven.** LAYER frame. REPEAT new. Confidence: likely. Units 3 and 4 are flagged; unit
5 (the war with Mexico, slavery, land taken from Native nations and Mexico, and after finding 1 the overthrow in
Hawaii) and unit 7 (exclusion and wartime incarceration, Native nations in each region) are not. The bar has the
read cover every unit, so the flags read as a list will mislead. Fix: one line in "The course in brief": "Every
unit gets the fresh-agent sensitivity read (bar item 12); every unit names Native nations or Indigenous peoples,
and units 3, 4, 5 and 7 carry the most"; add "Flagged for the sensitivity read" to units 5 and 7.

**7. Stale note.** LAYER process. REPEAT yes (stale notes in the progression reads). Confidence: firm. For the lead 4
says to run `frame.py sync` for grade 4; data/plans/frames.csv already holds `social-studies-grade-4,7,160`. Fix:
drop the item, or "frames.csv holds grade 4 (7 units, 160 days)".

## What is right and should not be touched

- Every MA.4 code and lettered part is owned by a placed row, and the theme split of the region sub-topics (unit
  6 land, maps and resources; unit 7 peoples and hazards) has a stated reason.
- The war with Mexico taught in its time in unit 5, from Mexican, Tejano, Californio, Native and US sides, with
  the record settling what it can.
- Unit 4's history set (Norse, Columbus and the Taino, Cortes and the Mexica, Cartier, de Soto or Coronado) and
  conquest named plainly.
- The cross-subject calendar is right against the spines on file: 4.NBT.B.4 (math days 72 to 77) comes before
  unit 6; 4-ESS3-1 (science days 13 to 31) before unit 6; 4-ESS3-2 (science days 97 to 104) before unit 7;
  4.MD.A.2 (math days 124 to 131) and 4-ESS1-1 (science days 80 to 87) come later and each has a bridge.
- Day ranges in the calendar match the unit days exactly; checks wait for what they test.
- The informed action (a hazard product checked against official advice) is safe, local and the students' choice.

## What I could not judge

- The check-set candidates against California, Tennessee and New York text: unit-plan work, not reread here.
- The facts in finding 1's fix rest on memory and on the anchor's own list; the unit writer checks them against
  the record (the 1993 resolution's text is public domain at congress.gov).

## Sources

- data/standards/ma-hss-2018.txt (MA.4.*, every lettered part): findings 1, 2 and 5.
- docs/courses/math-4-spine.md and docs/courses/science-4-spine.md: the cross-subject calendar.
- Public Law 103-150 (1993), from memory: finding 1.
- Defects are not logged with `plan.py defect` on this read, because the caller allowed only the report to be
  written; the caller may log findings 1 to 7 with found_by `expert`.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| 1. Unit 3 reads a given timeline in thousands of years and places two or three dates; students do not build it | The to-scale timeline is taught in unit 4 and deep time in grade 6 (finding 4) | docs/courses/social-studies-grade-4/frame.md unit 3; data/progressions/social-studies.csv (ss4-first-peoples-evidence notes) |
| 2. The Navajo Long Walk (1864) is the worked case of a forced movement on the Southwest map | It is the anchor's region and a well-documented case with the Navajo Nation's own materials (finding 5) | frame.md unit 6; social-studies.csv (ss4-state-maps notes) |
| 3. Unit 5's three added cases are Alaska (1867), the Hawaiian Kingdom's overthrow (1893) and annexation (1898), and Puerto Rico (1898) | They are the gains MA.4.T4.2 itself lists (finding 1) | frame.md unit 5; social-studies.csv (ss4-westward-growth notes) |
| 4. For the lead 2 (the grade 4 history set) stands as decided in the frame | Item level, inside MA.4.T3.2 and T3.3 | none |

## For Cory

- **Time a day (audience).** The same question as grade 3: 160 days at about 40 minutes a day. The frame's load
  (17 wide rows, five regions twice) needs the full year; whether schools give it is yours.
