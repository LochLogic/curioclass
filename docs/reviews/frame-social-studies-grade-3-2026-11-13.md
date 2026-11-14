# Expert cold read: course frame, Grade 3: Communities Then and Now (2026-11-13)

Brief: docs/pipeline/briefs/frame-read.md, {course} = social-studies-grade-3, {subject} = social-studies. The reader
did not write the frame and had no part of the conversation that made it.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; docs/ADOPTION-BAR-SUBJECTS.md section 1;
  docs/courses/social-studies/STANDARD.md; docs/courses/social-studies/grade-3-outline.md.
- The frame, docs/courses/social-studies-grade-3/frame.md, in full; its line in data/plans/frames.csv (7 units, 160
  days); the 27 grade 3 rows of data/progressions/social-studies.csv; data/progressions/social-studies-excluded.csv.
- The anchor text for grade 3 (data/standards/ma-hss-2018.txt, MA.3.*) and the C3 3-5 ids
  (data/standards/c3-indicators.txt, ids only); all 72 C3 3-5 indicators checked for an owner in grades 3 to 5.
- Neighbours: docs/courses/social-studies-grade-2/frame.md (before), docs/courses/social-studies-grade-4/frame.md
  (after), and the grade 5 and grade 6 frames for the threads handed past grade 4; the grade 1 frame for the
  dormant grade 1 rows; the grade 4, 5 and 1 to 2 rows that receive or feed grade 3.
- data/plans/later.csv (L5); docs/reviews/progression-social-studies-2026-11-13.md and its codex and fixes reads.
- Gates: `python -X utf8 scripts/plan.py check` (social-studies-grade-3: 0 failures, 7 units, 160 days, 150 in
  units, 10 for checks and respond days; the civics and economics frames fail a frames.csv sync, not this course);
  `python -X utf8 scripts/stale.py check` (16 files, 0 failures). No base text, so no source map.
- Not opened: anything under S:\CurioClass-sources\_calibration. No web sources fetched on this read (see "What I
  could not judge").

## Verdict

The frame is sound: every grade 3 row is placed once, the seven units run in a defensible order (place, civics,
economics, the nations, first meetings and colonies, founding ideas, the community), the day calendar adds up, and
the own-place method, informed action and hard-history notes are well judged. The biggest risk is that three
anchor standards are taught only in part (conversion in MA.3.T5.2, why towns grew in MA.3.T6.1, the voyage in
MA.3.T4.1), and that unit 5's named leaders and war still lean on New England in the one year built to avoid that.
The one change that matters most is to add the missing parts of those three standards to the rows and to unit 5
and unit 7, and rotate unit 5's leaders and war case across its three colonies.

## Findings, most serious first

**1. Three anchor standards are taught only in part.** LAYER standard (rows) and frame. REPEAT yes (the progression
reads found missing parts of standards). Confidence: firm (the anchor text in data/standards/ma-hss-2018.txt).
- MA.3.T5.2 names "lost land, disease, conversion, and conflicts". Unit 5 and ss3-early-colonies teach land loss,
  disease and war but never conversion. A writer building from the row will leave it out, and the check cannot
  test it.
- MA.3.T6.1 asks how far the province extended **and why its towns and cities grew in the 1700s**. Unit 7 and
  ss3-community-history keep only "a historical map of their own state". The growth half is gone.
- MA.3.T4.1 asks how the Pilgrims traveled; the frame and ss3-early-colonies give "who came and why" but not the
  voyage.
- Fix: add to ss3-early-colonies' notes and unit 5's "What students learn": "how the colonists crossed the
  Atlantic (the Mayflower's voyage as one case)" and "some colonists pressed Native people to give up their own
  beliefs and ways (conversion, for example the praying towns), told plainly with what the nations say of it".
  Add to ss3-community-history's notes and unit 7: "from a historical map, how far the student's state, colony or
  territory reached at one date and why its first towns grew where and when they did (a river, a harbor, a road
  or railroad, a mine)". Taught in general form, since a western state's 1700s may be a Native or Spanish story.

**2. Unit 5 still leans on New England.** LAYER frame. REPEAT new. Confidence: likely (adoption bar item 13; the
lens's "replaced grade 3 year keeps Massachusetts-only content"). The unit picks three colonies on three coasts, but
four of its five named leaders are New England's (Massasoit, Metacom, Bradford, Winthrop; only Wahunsenaca is
not), Winthrop leads a colony the unit does not study, and the one war named is King Philip's War, which grade 5
unit 1 teaches again with the Pequot War (MA.5.T1.1). A Virginia or Florida class meets its own coast only as a
name. Fix: rotate the leaders by colony (Bradford and Massasoit for Plymouth; John Smith and Wahunsenaca for
Jamestown; Pedro Menendez de Aviles and a Timucua leader named in the record for St. Augustine, the name checked by
the unit writer), drop Winthrop from grade 3, and make the conflict case the 1622 war between the Powhatan nations
and Jamestown, with King Philip's War named as a second case only if the unit plan's days allow. Grade 5 then
teaches the New England wars without repeating grade 3. (Applied as "Settled by the expert" 4.)

**3. D2.Civ.5 is owned in unit 2 but finished in unit 6.** LAYER frame. REPEAT new. Confidence: likely. D2.Civ.5.3-5
asks for the origins, functions and structure of government with reference to the US Constitution, state
constitutions and other systems. ss3-state-constitution owns it in unit 2, where the frame says the US
Constitution is "met only as the other plan"; its origin and purpose are taught in unit 6 (ss3-founding-ideas),
whose row does not carry D2.Civ.5. Read as written, the standard is taught in part in each unit and in full in
neither. Fix: keep the row in unit 2 (For the lead 2, settled below); add "D2.Civ.5 (completed: where the US
Constitution came from, set beside unit 2's state constitution)" to unit 6's C3 column as practised, and change
unit 6's "what a constitution is for" to "what a constitution is for, reviewed from unit 2, now for the
national plan".

**4. The "Handed past grade 4" paragraph is wrong on two counts.** LAYER frame (seam), with progression fixes in the
grade 4 and grade 5 reports. REPEAT yes (handoff gaps in the progression reads). Confidence: firm.
- "Grade 4 teaches no founding ... content": ss4-states-and-statehood teaches MA.4.T4a.3, why statehood beat
  being a British colony in the 1700s, which rests on ss3-founding-ideas (unfair treatment, representation,
  consent).
- "Money returns in ss6-phoenician-trade": ss5-independence-war owns D2.Eco.11 (inflation, deflation,
  unemployment after the war), which needs ss3-money-saving's idea of money and price.
- Fix: rewrite the paragraph: "ss3-founding-ideas (unit 6) is kept in use by ss4-states-and-statehood and picked
  up by ss5-independence-war and ss5-constitution; ss3-money-saving (unit 3) returns in ss5-independence-war
  (inflation and deflation, with a retrieval task) and ss6-phoenician-trade". The models table's budget line reads
  "money returns in ss5-independence-war and ss6-phoenician-trade". The progression review's line that "grades 4
  and 5 carry no money content" (progression-social-studies-2026-11-13.md, row ss6-phoenician-trade) is wrong on
  this point; this read disagrees with it.

**5. The three branches are used in grade 3 but carry no model.** LAYER progression. REPEAT yes (model gaps in the
progression reads). Confidence: firm. Unit 2 compares the state constitution with "the US Constitution's three
parts (lawmakers, a leader, judges)" and unit 6 teaches what a constitution is for, yet no grade 3 row lists
branches-of-government, and the grade 4 frame calls the model "new in grade 4". A grade 4 writer will reteach the
names as new. Fix: ss3-state-constitution `model_out` adds branches-of-government (named as three parts, what each
does left to grade 5); the frame's "Models carried" table adds a line for it (unit 2, used again in unit 6, handed
to ss4-national-capital); ss4-national-capital `model_in` adds it (see the grade 4 report, finding 3).

**6. Who picks unit 4's regions and nations is left to no one.** LAYER process. REPEAT new. Confidence: firm.
ss3-first-nations-region's note says the worked examples come "from five regions settled in the course frame"; the
frame says "the frame does not choose them" and points at later.csv L5, whose "when" ("The grade 3 course frame is
written") has now come. Each note points at the other. Fix: the regions are settled below (grade 4's five
regions); rewrite the row's note to "worked examples from five regions (grade 4's Northeast, Southeast, Midwest,
Southwest and West), the nations in each picked under later.csv L5 from their own published materials"; change
L5's "when" to "Before the grade 3 unit 4 plan" and its title to "Pick the nations for grade 3 unit 4's five
regions"; the frame's Pending note in unit 4 keeps its marker and names the regions.

**7. Two threads start later than the units that use them.** LAYER frame. REPEAT new. Confidence: firm.
- "A short biography read in most units" runs from unit 1, but the readiness check for the dormant grade 1 row
  ss1-leaders sits with ss3-biography in unit 7. Fix: move the ss1-leaders readiness check to the first biography
  read (unit 1 or 2) and say so in the grade 1 seam line.
- "A timeline in every history unit (taught in unit 5)": unit 4 is a history unit and comes first. Fix: "a
  timeline in every history unit from unit 5 on; unit 4 places events as before and after, then and now".

**8. The sensitivity flags are uneven.** LAYER frame. REPEAT new. Confidence: likely. Units 4 and 5 are flagged for
the fresh-agent sensitivity read; units 1 (Native nations present in the place), 6 (who was left out of
citizenship) and 7 (the nations, enslaved workers and newcomers in the town's history) carry the same kinds of
content and are not. The bar (item 12) has the read cover every unit, so a writer who takes the flags as the list
will skip three. Fix: one line in "The course in brief": "Every unit gets the fresh-agent sensitivity read (bar
item 12); units 1, 4, 5 and 7 carry Native content and also need the qualified person's read when one is found";
add "Flagged for the sensitivity read" to units 1, 6 and 7.

**9. Unit 5's compelling question frames land loss as a shortage of space.** LAYER frame. REPEAT new. Confidence: a
judgment call. "Was there room for everyone?" invites the answer "yes, there was plenty of land", which turns the
record (land taken by war, by deeds the nations read differently, by settlement past agreed lines) into a question
of room. The lens asks that a hard fact never be softened until it is false. Fix: "Could the colonists and the
Native nations have shared the land?" It keeps more than one defensible answer and puts the choices on people.
Grade 5 unit 1 asks "Whose land was it, and who decided?", so the two questions do not repeat.

**10. Stale notes.** LAYER process. REPEAT yes (stale notes fixed in the progression reads). Confidence: firm.
- For the lead 5 says to run `frame.py sync` for grade 3 (7 units, 160 days); data/plans/frames.csv already holds
  `social-studies-grade-3,7,160`. Fix: drop the item, or "frames.csv holds grade 3 (7 units, 160 days)".
- For the lead 4 says Ghana "unless the grade 1 or grade 2 frame uses Ghana"; neither does (grade 2's report
  country is each student's own choice). Fix: "Ghana (no earlier grade fixes a country)".
- grade-3-outline.md "Open for the frame and the expert read" still lists the unit 3 country (decided in the
  frame) and the unit 4 regions (settled below). Its unit table's C3 column disagrees with the frame and the rows
  (unit 1 lists D2.Geo.3, which grade 4 owns; unit 4 lists D2.His.2 and 3, owned in units 5 and 7; unit 6 lists
  D2.Civ.3 and 5, owned in unit 2). Fix: mark the two open items decided with where, and add one line over the
  units table: "Superseded for codes, days and placement by docs/courses/social-studies-grade-3/frame.md".

## What is right and should not be touched

- The unit order and its reasons; unit 4 before unit 5 so students know who was here, and are here now, before
  Europeans arrive.
- The seam tables are taken from the rows and match grade 2's hand-on table row for row, including grade 2's note
  about not repeating the storm-readiness problem.
- Every grade 3 C3 3-5 code has an owner, and every C3 3-5 indicator has an owner somewhere in grades 3 to 5.
- MA.3.T6.2's exclusion is recorded with its reason and its grade 5 home.
- Checks ask skills on content, and nothing is checked before it is taught.
- The availability calendar's day ranges match the unit days exactly, with a bridge for each lean.
- The values-rule notes: no family addresses, immigration status or money facts asked; no reenactment; enslaved
  people named as people; the feast from the record and from Wampanoag people today.
- For the lead 3 (cite the lettered parts MA.3.T2.3a to d, T4.1a to c, T5.5a to c on the rows): agreed, still
  open, a progression fix.

## What I could not judge

- The check-set candidates against California, Tennessee and New York text: not reread here; they are unit-plan
  work. The Timucua leader's name and the 1622 war's framing rest on memory and are for the unit writer to check
  against the record.
- Whether 40 minutes a day is real for grade 3 schools: an audience question (For Cory).

## Sources

- data/standards/ma-hss-2018.txt (MA.3.*, MA.4.T4a.3, MA.5.T1.1): the standards read for findings 1, 2 and 4.
- data/standards/c3-indicators.txt (ids) and the C3 Framework 2013 from memory for the wording of D2.Civ.5.3-5
  and D2.Eco.11.3-5 (finding 3, 4).
- docs/reviews/progression-social-studies-2026-11-13.md: earlier read, disagreed with on money (finding 4).
- Defects are not logged with `plan.py defect` on this read, because the caller allowed only the report to be
  written; the caller may log findings 1 to 10 with found_by `expert`.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| 1. ss3-state-constitution stays in unit 2 (For the lead 2) | The levels of government just taught are the frame the state constitution sets up; unit 6 completes D2.Civ.5 for the national plan (finding 3) | docs/courses/social-studies-grade-3/frame.md |
| 2. Unit 3's country is Ghana, a present-day market town | No earlier grade fixes a country; not Canada or Mexico (grade 4). The unit plan keeps it apart from ancient Ghana, which grade 6 teaches (ss6-west-africa-trade) | frame.md (For the lead 4) |
| 3. Unit 4's five regions are grade 4's five: Northeast, Southeast, Midwest, Southwest, West | Grade 4 builds on the same regions; the nations in each stay under later.csv L5 | frame.md unit 4; data/progressions/social-studies.csv (ss3-first-nations-region notes); data/plans/later.csv L5 |
| 4. Unit 5's leaders and war rotate by colony: Bradford and Massasoit; John Smith and Wahunsenaca; Menendez de Aviles and a Timucua leader from the record; the 1622 Powhatan war as the conflict case; Winthrop dropped | Own-place rotation (bar item 13); grade 5 teaches King Philip's War and the Pequot War | frame.md unit 5; social-studies.csv (ss3-early-colonies notes) |
| 5. Unit 6's teacher note cites West Virginia State Board of Education v. Barnette (1943) beside "no student is required to perform a patriotic act" | Values rule (a); grade 1's frame and ss1-national-symbols already cite it | frame.md unit 6 |
| 6. "A timeline in every history unit from unit 5 on" | Unit 4 precedes the timeline row (finding 7) | frame.md, The course in brief |

## For Cory

- **Time a day (audience).** Grades 3, 4 and 5 each assume 160 days at about 40 minutes every day, while grade 2
  assumes three lessons a week (96 days). The frame's pick (keep 160, with about 20 days marked compressible in the
  scope and sequence) is sound for the content; whether schools give grade 3 a daily block is yours.
