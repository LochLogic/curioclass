# Sequence fixes: social studies grades 3 to 5, 2026-11-14

The fix pass on the expert and Codex sequence reads of 2026-11-14 for social-studies-grade-3, social-studies-grade-4 and
social-studies-grade-5, with the lead's four settled calls for all 15 courses and Cory's standing calls. Files changed, per
course: docs/courses/<course>/scope-and-sequence.md, data/plans/<course>/days.csv and docs/courses/<course>/frame.md. No
course has a source-map.csv. No day was added; every unit keeps its frame total and calendar dates.

Reads applied:

- docs/reviews/sequence-social-studies-grade-3-2026-11-14.md and sequence-social-studies-grade-3-codex-2026-11-14.md
- docs/reviews/sequence-social-studies-grade-4-2026-11-14.md and sequence-social-studies-grade-4-codex-2026-11-14.md
- docs/reviews/sequence-social-studies-grade-5-2026-11-14.md and sequence-social-studies-grade-5-codex-2026-11-14.md
- the For the lead items in each scope and sequence

## Gates

| Command | Result |
|---|---|
| `sequence.py check social-studies-grade-3` | 0 failures |
| `frame.py check social-studies-grade-3` | 0 failures |
| `sequence.py check social-studies-grade-4` | 0 failures |
| `frame.py check social-studies-grade-4` | 0 failures |
| `sequence.py check social-studies-grade-5` | 0 failures |
| `frame.py check social-studies-grade-5` | 0 failures |
| `plan.py check` | exit 0; 52 frames, 0 catalogue failures; no course reports a failure |
| `frame.py calendar` | no stagger break; grade 3 to 5 social studies check weeks unchanged (grade 4: 8, 21, 27; grade 5: 16, 29) |

## The lead's settled calls, as applied here

1. **Readiness or retrieval.** Grade 3: readiness checks stay for grade 1 rows idle across grade 2; grade 2 rows open as
   retrieval tasks. Grade 4: retrieval only (every assumed row is a grade 3 row); the frame's Days bullet now says so.
   Grade 5: readiness checks on days 15, 44, 60 and 147 (grade 3 rows idle across grade 4); the frame's Days bullet and
   two Seams rows now say so. The progression notes that say otherwise are listed under For the structure pass.
2. **Held days.** None of the three courses holds a day that shifts a unit. Grade 5's day 73 (review for check 1) stays
   inside unit 5. No check week moved.
3. **Checks after an assessment.** Every course-level check in grades 3 to 5 falls two days after an end-of-unit
   assessment. Each check's items for that unit's skills now draw content from earlier units, and each scope and
   sequence and frame says so for that check (grade 3: days 69 to 70, 122 to 123 and 137 to 138; grade 4: days 39 to 40,
   104 to 105 and 133 to 134; grade 5: days 76 to 77 and 143 to 144).
4. **Each part of each code.** Every end-of-unit, mid-unit and course-level check day lists every code it assesses. Its
   goal gives a short prompt per part, and its note says "every part of each listed code asked once". Codes judged from a
   product (grade 3 unit 7, grade 4 units 2 and 7, grade 5 unit 10) are scored with the unit rubric, and the note says so.

## Grade 3 (social-studies-grade-3)

Applied 13 of 14. Not applied: 1 (Codex 5, where the two reads disagree). Expert 5 also goes to the structure pass.

| Finding | Status | What changed |
|---|---|---|
| Expert 1, Codex 1: assessment days cover only part of each unit | Applied | days.csv: end days 23, 47, 67, 88, 120, 135 and 159 and mid-unit day 105 list every owned code, with a prompt per part. Day 120 asks the first-half codes as one short prompt each. Day 159 scores the biography, share-out and action with the unit rubric. S&S: each unit's assessment bullet and an assessment-rule line. |
| Expert 2: unit 5 colonies in reverse order | Applied | days.csv: St. Augustine 97 (compressible), Jamestown and the 1622 war 98 to 99, Plymouth 100 to 103, timeline review 104 (compressible), mid-unit assessment 105 with all first-half codes. Day 106 notes that the mid-unit response opens it. S&S unit 5 paragraph rewritten; frame unit 5 cell puts the colonies in founding order. |
| Codex 5: keep case order and explain it | Not applied | The reads disagree. I took the expert's swap: it costs no day, time order is the lens default for the unit that introduces the timeline, and it puts St. Augustine inside the mid-unit assessment. Codex's aim, a founding date on the shared timeline at each case, is met because the cases now run forward in time. |
| Expert 3: biography thread on two days only | Applied | days.csv: short biography reads on days 35, 54, 83, 107 and 130 (ss3-biography), no added day. S&S biography thread line. |
| Expert 4: day 78 leaves the Cherokee only in Oklahoma | Applied | Day 78 names the Eastern Band of Cherokee Indians in North Carolina today. |
| Expert 5: rule 2 wording ("idle two or more grades") | Applied in the days; wording to the structure pass | The readiness checks stay as written. Settled call 1 states the rule. The brief's wording is listed below. |
| Expert 6: a stale lean note | Applied | Day 86 note: ELA is running now. |
| Codex 2: day goals lose requirements | Applied | Day 20 adds an idea open to two readings (D1.3), modelled first. Day 103 adds Samoset (Abenaki sachem) and the Abenaki/Wabanaki. Day 113 adds colonial barter. Day 83 starts from one contribution of a nation near the school, from its own materials. Frame unit 4 and unit 5 cells match. |
| Codex 3: no model for two-source writing | Applied | Day 19 models a claim from two very short sources. Days 20 and 117 rehearse naming both sources and how each supports the claim. |
| Codex 4: day 28's "three branches at each level" | Applied | Day 28 names national and state branches and the leaders at three levels. Day 43 describes the tribal government from its own constitution, with no three-branch template. The frame's unit 2 candidate cell is corrected. |
| Codex 6: stale operational notes | Applied, one part to the structure pass | Reteach notes say days 26, 50 and 126. Frame Cross-subject unit 7 is days 141 to 160. Frame sensitivity list adds unit 2. The compressible note says the school-grounds drawing moves into day 9 if day 10 folds. The grade 3 outline line is listed below. |
| For the lead 1 and 2 (frame unit 7 days; unit 2 sensitivity) | Applied | Frame edited. S&S For the lead now reads "None open". |
| Settled 3 | Applied | Check 1 (69 to 70) asks unit 3's opportunity cost on a unit 1 or 2 case. Check 2 (122 to 123) builds the timeline from unit 1 and 4 events, and part 2 uses a unit 4 nation (MA.3.T2.3b; D2.Geo.6). Check 3 (137 to 138) asks the founding idea on unit 2's government and the claim on units 4 and 5, and day 137's codes are filled in. S&S checks table, a settled-3 sentence, and frame check rows 1 to 3. |

## Grade 4 (social-studies-grade-4)

Applied 13 of 14. Not applied: 1 (Codex For Cory, held on the grade 3 precedent). Expert 3 also goes to the structure pass.

| Finding | Status | What changed |
|---|---|---|
| Expert 1, Codex 1: assessment days cover only part of each unit | Applied | End days 15, 37, 58, 78, 102, 131 and 159 and mid-unit day 120 list every owned code with a prompt per part. Day 120 has the map made, not only read. Day 159 covers five regions and four disaster regions. Units 2 and 7 products are scored with the unit rubric. S&S assessment bullets rewritten. |
| Expert 2, Codex 3 (unit 7): day 142 carries four topics | Applied | Day 142: West peoples, the Gold Rush, Chinese Americans and the Exclusion Act. New day 143: Japanese Americans and wartime incarceration, from their own accounts. Old days 143 to 157 shift to 144 to 158. The old review day 158 is dropped, and day 159 opens with a short review. This merges the expert's split with Codex's contributions, so each community's contributions come before exclusion. |
| Expert 3: retrieval only is right; the bar's wording | Applied in the frame; bar wording to the structure pass | Frame Days bullet now says retrieval task (frame-write lesson 16). |
| Expert 4: unit 5 ends on the division after 1898 | Applied | Choice, force and the division over slavery on days 92 to 94; Alaska, Hawaii and Puerto Rico on 95 to 97; the map on 98. S&S unit 5 paragraph. |
| Expert 5: day 83 canal set | Applied | Day 83 note: social studies may open the canal set before ELA does, one canal text only. S&S candidate line. The ELA grade 4 frame line the expert named already reads "(taught here in unit 1)", so it needs no edit. |
| Codex 2: goals narrow the performance | Applied | Route tracing on one accumulating map on days 66, 69, 71 and 72. Clue-based audience and purpose inference on days 62 and 63 (and 78). Day 85 compares two motives, men's and women's, with trail and settlement life. Day 122 is a question-led investigation of two supplied sources. Days 138 to 143 name each region's groups and one contribution each. Day 145 covers people, goods and ideas. |
| Codex 3 (unit 6): local load | Applied | Capitals spread by region over days 108 to 110 and retrieved on 119 and 130. Supplied base maps and bounded atlas sets on days 114 to 118. Day 117 teaches the Long Walk before it is mapped. |
| Codex 4: writing growth unstated | Applied | Notes on days 14, 35, 56, 76, 100, 129 and 158 (claim days after the shift) and 156 to 157 (the proposal). S&S writing-growth line. |
| Codex 5: no shorter route | Applied | 14 compressible days (8, 13, 22, 34, 36, 55, 57, 75, 77, 98, 101, 119, 128, 130), with the folding rule in the S&S. No assessment, respond or sole-code day is compressible. |
| Codex For Cory: the shorter route's time assumption | Not applied (not raised) | Cory settled the model for grade 3 ("as picked", 2026-11-14, in the grade 3 frame): compressible days on the 40-minute daily block. Grades 4 and 5 follow it, so no new audience question arises. A less-than-daily timetable would be new scope, and no read asks for it. |
| Codex 6: review flags and "first" claims | Applied | Sensitivity notes on days 49, 50, 51, 54, 71, 140 and 146 to 150. S&S: "first claim weighing archaeological migration theories". Unit 4 sourcing described as a deepening of grade 3 and unit 2 work. |
| For the lead 1 and 2 (Days bullet; science row days) | Applied | Frame Days bullet. Science rows read days 42 to 59 and 137 to 160. S&S For the lead now reads "None open". |
| Settled 3 | Applied | Check 1 (39 to 40) asks fact and opinion on unit 1's land and rivers. Check 2 (104 to 105) asks cause and effect on unit 4's exchange. Check 3 (133 to 134) has a map of a Canadian province or Mexican state and a claim on units 3 to 5. S&S table, a settled-3 sentence, and frame check rows 1 to 3. |

## Grade 5 (social-studies-grade-5)

Applied 14 of 15. Not applied: 1 (Codex For Cory, as for grade 4). Expert 3's progression notes go to the structure pass.

| Finding | Status | What changed |
|---|---|---|
| Expert 1, Codex 1: assessment days cover only part of each unit | Applied | End days 13, 25, 42, 58, 74, 95, 111, 125, 141 and 159 list every owned code and lettered part (MA.5.T1.7a to d, T2.1a to d, T2.2, T2.3, T2.5a to c, T2.6, T2.7, T2.9, T3.3, T3.5, D2.Civ.1, 3, T4.3a and b, D2.Eco.6, 13, D2.Geo.11, T4.5a to d, D2.His.5, 6, D2.Civ.14, T5.5, D2.His.17, and the claim codes). Each goal has a prompt per part, Codex's blueprint items included. Day 159: the portfolio (D1 and D4 codes) judged with the unit rubric, plus an unseen-source task (D2.His.13). S&S assessment bullets rewritten. |
| Expert 2: King Street before the Stamp Act Congress | Applied | Day 32: the Stamp Act Congress and the Sons of Liberty (was 35). Day 33: sourcing unprompted (was 32). Day 34: King Street in two accounts, with the RI.5.6 bridge (was 33). Day 35: weigh and claim (was 34). S&S Leans line now says day 34. |
| Codex 5 (unit 3): name the two-pass design | Applied together with the expert's swap | The reads differ on remedy, not aim. The swap restores time order in the detailed pass at no cost. Day 30 is now named as the first-pass overview of the Acts (1764 to 1774), and days 32 to 37 are marked as returns on the shared timeline. "The year's first contested event" is removed. |
| Expert 3, Codex 7 (readiness): readiness checks stay; the frame and progression say retrieval | Applied (frame); progression to the structure pass | Frame Days bullet: readiness check on the first day (units 2, 4, 5 and 10) for grade 3 rows idle across grade 4, and retrieval for the rest. The Seams rows for ss3-sea-trade and ss3-money-saving now say readiness check. |
| Codex 2: unit 6 economics | Applied | Day 90 carries D2.Eco.6 and D2.Eco.13 and links investment in machines and in workers' learning to productivity and later income. Day 91 keeps only D2.Geo.11. Day 92 separates costs inside the work from effects on people outside the deal, adding an external benefit (a clearly labelled example). Days 89 to 93 mark each benefit and cost short term or long term. Day 94's claim weighs them, and day 95 asks it. |
| Codex 3: unit 10 explanations and models | Applied | Day 147 asks why the question matters beyond the class. Day 148 opens with a model and a guided revision and asks how each supporting question helps. Day 151 opens with a model usefulness judgment. Day 154 opens with a model critique. Day 155 compares individual and collective strategies on local, regional and global cases. Notes name the supported attempt and the independent evidence. The S&S line now reads "No new historical survey content is introduced; the unit teaches and applies the remaining inquiry skills." |
| Codex 4: unit 2's "rising order" | Applied | S&S sentence replaced with Codex's wording. Day 21: skilled work and being hired out did not end enslavement. Day 22 sets completed indentures or service against manumission and freedom suits, and keeps Prince Hall's petitions apart from the Freeman and Walker cases. |
| Codex 5 (unit 7): Trail of Tears before Mashpee | Applied | Days 102 and 103 swapped: Mashpee 1833 on day 102, the Trail of Tears 1838 on day 103. S&S unit 7 paragraph. |
| Codex 5 (unit 9): movement-based order | Applied | The S&S says unit 9 runs in time order through 128 to 135, is movement-based from 136 to 139, and uses a parallel timeline. The expert found the order right, so the days are unchanged. |
| Codex 6: no shorter path | Applied | 9 compressible days (3, 8, 18, 40, 53, 56, 70, 82, 152), with the folding rule in the S&S (151 days keep every code). No readiness, assessment or respond day is compressible. Day 73 is left full, per settled call 2. |
| Codex For Cory: time assumption | Not applied (not raised) | As grade 4: this follows Cory's grade 3 call. |
| Codex 7: sensitivity flags | Applied | Units 3 and 10 added to the S&S overview and the frame's sensitivity bullet. Notes added on days 21 to 25, 34, 101, 111, 118 to 121, 141, 144, 147, 150 and 159. |
| Codex settled: day 31 government development | Applied | Day 31: how legislatures, town meetings and charters of rights developed and helped lead to revolution. |
| Codex settled: day 51 eight leaders | Applied | Day 51 note: brief profiles, then one focused comparison of two. S&S unit 4 line. |
| For the lead 1 and 2 | Applied | Frame Days bullet and Seams rows. S&S For the lead now reads "None open" and quotes the two items. |
| Settled 3 and 4 | Applied | Check 1 (76 to 77) uses a document and two accounts from units 3 or 4, the timeline, and a map from unit 1 or 4. It asks none of unit 5's own skills, and D2.His.16 is added to day 76. Check 2 (143 to 144) weighs causes of an event from units 3 to 7 and asks continuity and change for free and enslaved African Americans from the 1700s to 1877 (units 2, 7 and 8). Day 144 adds D4.1 and a sensitivity note. S&S table and sentence; frame check table rows 1 and 2. |

## Settled

| Course | Item | Settled as |
|---|---|---|
| All three | Check day codes | Every owned code and lettered part on its unit's assessment day, a prompt per part; product codes by unit rubric |
| All three | Course-level checks after an assessment | Items for that unit's skills on earlier units' content, said in the S&S and frame |
| All three | Shorter path | Compressible days on the 40-minute daily block (grade 3: 20, grade 4: 14, grade 5: 9), following Cory's grade 3 call; no question to Cory |
| Grade 3 | Unit 5 order | Expert swap into founding order, over Codex's keep-and-explain |
| Grade 3 | Readiness | Readiness for grade 1 rows idle across grade 2; retrieval for grade 2 rows |
| Grade 3 | Day 28 | National and state branches; local and tribal governments from their own descriptions |
| Grade 4 | Day 142 | Two days (Gold Rush and Chinese Americans; Japanese Americans); old review day 158 dropped |
| Grade 4 | Unit 5 end | Choice, force and the division 92 to 94; Alaska, Hawaii, Puerto Rico 95 to 97; map 98 |
| Grade 4 | Readiness | Retrieval only; frame Days bullet corrected |
| Grade 5 | Unit 3 order | Stamp Act Congress 32, sourcing 33, King Street 34, weigh 35; day 30 named as the first-pass overview |
| Grade 5 | Unit 7 order | Mashpee 102, Trail of Tears 103 |
| Grade 5 | Readiness | Days 15, 44, 60, 147 stay readiness checks; frame corrected; progression to the structure pass |
| Grade 5 | Unit 6 economics | Both productivity indicators on day 90; day 92 separates internal costs from spillovers; short and long term carried to day 95 |
| Grade 5 | Unit 2 freedom routes | Legal-status wording; Prince Hall's petitions kept apart from the court cases |

## For the structure pass

1. **data/progressions/social-studies.csv, row ss5-slavery-colonies, notes.**
   - Old: "Handoff kind: from ss3-sea-trade (grade 3) is content revisited: this row reteaches it at its own depth and opens with a short retrieval task."
   - New: "Handoff kind: from ss3-sea-trade (grade 3) is content revisited: this row reteaches it at its own depth and opens with a readiness check on the unit's first day (the row sat idle across grade 4)."
   - Why: expert grade 5 finding 3 and settled call 1.
2. **Same file, row ss5-independence-war, notes.**
   - Old: "From ss3-money-saving (grade 3) (skips 1 grade because grade 4 carries no money content) is content revisited: the postwar prices open with a short retrieval task on what money and a price are and what a loan is."
   - New: "From ss3-money-saving (grade 3) (skips 1 grade because grade 4 carries no money content) is content revisited: the unit opens with a readiness check on its first day on what money and a price are and what a loan is (the row sat idle across grade 4)."
   - The ss3-founding-ideas sentence in this row stays as it is.
3. **Same file, row ss5-constitution, notes.**
   - Old: "from ss3-rules-rights (grade 3) (skips 1 grade because the courses between do not teach it) is content revisited: this row reteaches it at its own depth and opens with a short retrieval task;"
   - New: "from ss3-rules-rights (grade 3) (skips 1 grade because the courses between do not teach it) is content revisited: this row reteaches it at its own depth and opens with a readiness check on the unit's first day (the row sat idle across grade 4);"
   - The ss3-founding-ideas clause in this row stays as it is.
4. **Same file, row ss5-informed-action, notes.**
   - Old: "Handoff kind: from ss3-deliberation (grade 3) is content revisited: this row reteaches it at its own depth and opens with a short retrieval task."
   - New: "Handoff kind: from ss3-deliberation (grade 3) is content revisited: this row reteaches it at its own depth and opens with a readiness check on the unit's first day (the row sat idle across grade 4)."
5. **docs/courses/social-studies/grade-3-outline.md, line 95.**
   - Old: "(Mashpee Wampanoag, Cherokee,"
   - New: "(Penobscot, Cherokee,"
   - The grade 3 frame and day 77 name the Penobscot Nation as the Northeast worked case. Cite the November 14 baseline fix and this report, and keep the historical review records (Codex grade 3 finding 6).
6. **docs/ADOPTION-BAR-SUBJECTS.md, line 60 (C4), evidence cell.**
   - Old: "the readiness check on each unit plan"
   - New: "the readiness check or opening retrieval task on each unit plan"
   - Why: expert grade 4 finding 3. A course whose assumed rows are all from the year before carries retrieval tasks only, and as written it reads as missing evidence.
7. **docs/pipeline/briefs/sequence-write.md, line 54 (rule 2).**
   - Old: "where it assumes an earlier grade's row idle two or more grades"
   - New: "where it assumes an earlier grade's row last used two or more grades back"
   - Why: expert grade 3 finding 5, in settled call 1's own words. A grade 1 row skipped across grade 2 is idle one grade but was last used two grades back. The rest of the line stays.
8. **No change needed:** docs/courses/english-language-arts-grade-4/frame.md. The SL.4.4 line the expert grade 4 read named (finding 5) already reads "by its unit 2 (taught here in unit 1)", which matches its unit table.

## For Cory

None. Codex's grade 4 and grade 5 For Cory item (the shorter path's time assumption) is not raised. Cory settled the model for grade 3 on 2026-11-14: compressible days on the 40-minute daily block. Grades 4 and 5 use the same model, and no read asks for a less-than-daily version.

## For the source list

These were opened by the Codex reads. Add any not already in APPROACH-SOURCES:

- California HSS standards PDF: https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf
- New York Complex Societies inquiry: https://c3teachers.org/wp-content/uploads/2024/04/NewYork_5_Complex_Societies.pdf
- Investigating History grade 4 and grade 5 course overviews (doe.mass.edu/investigatinghistory), the guidebook assessment section
- National Park Service, St. Augustine town plan: https://www.nps.gov/places/st-augustine-town-plan-historic-district-st-augustine-florida.htm
- A municipal government page used as a local-structure example (Arlington, Massachusetts, town governance)
