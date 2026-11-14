# Plan read: social studies grade 4, units 1 to 7 (2026-11-14)

Expert cold read of docs/courses/social-studies-grade-4/s01.md to s07.md, written by Codex today from skeletons made by scripts/unit_skeleton.py. Brief: docs/pipeline/briefs/plan-read.md. Reader: Claude, as the expert in docs/agents/EXPERT.md. I did not write these plans.

## What I read

- All seven unit plans in full: s01.md to s07.md.
- docs/courses/social-studies-grade-4/frame.md and scope-and-sequence.md in full; data/plans/social-studies-grade-4/days.csv, all 160 rows.
- data/progressions/social-studies.csv (the grade 3 and grade 4 rows) and the MA.4 lines of data/standards/ma-hss-2018.txt.
- docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16, social studies items 1 to 14 and "Fails if"), docs/courses/social-studies/STANDARD.md, docs/agents/lenses/social-studies.md, docs/GLOSSARY.md, AGENTS.md, docs/agents/EXPERT.md.
- The kindergarten and grade 1 plan reads of today (their "Settled by the expert" tables, and the grade 1 read in full as the format model).
- Web checks for current facts, listed under Sources at the end.

## Course verdict

The course is close to the bar. The seven units cover every Massachusetts grade 4 topic and its C3 skills. Goals have items, retrieval tasks sit where days.csv puts them, hand-ons between units are clean, and the facts I checked are right. Three things hold it back. First, the end-of-unit assessments are packed past what 35 or 30 minutes can hold (every unit, most sharply units 3, 4, 5, 6 and 7). Second, unit 1 still invents a readiness sitting "before day 1". Third, a handful of current facts and sensitivity sources are thin (Mexico and trade in 2026, the Whitman mission, Bosque Redondo, the national Inuit body). All are fixable inside the existing days. No finding needs Cory.

Severity follows cost: **serious** (a child is taught or assessed wrongly, or a sensitivity failure reaches a classroom), **moderate** (the plan cannot be run as written, or a standard part is weakly evidenced), **minor** (wording, a missing teacher note, a data tidy). Confidence: firm, likely, judgment call.

## Course-wide findings

### CW1. End-of-unit assessments do not fit their minutes (moderate, plan, firm)

**What is wrong.** Every end-of-unit assessment asks for every part of every listed code in one sitting, and several put a multi-paragraph argument inside it.

- Unit 3, day 49 area: Q5 asks two linked paragraphs in 9 minutes.
- Unit 4: Q6 asks two paragraphs in 10 minutes; Q4 asks two scaled timelines in 6.
- Unit 5: nine items; Q6 and Q7 share 7 minutes.
- Unit 6, day 131: five constructed state maps (F3a to F3e) in 13 minutes, plus an inquiry, a claim, economics and the capital in 16 (see 6.1).
- Unit 7, day 159: sixteen item rows in 30 minutes; the culture block asks five written sentences and underlining across 26 named groups in 9 minutes (see 7.1).

**Why it matters.** A grade 4 writer produces roughly one careful paragraph in 8 to 10 minutes. When time runs out, the last items (usually D3.4 and D4.1, the claim) go unanswered, and the record then shows a gap in the skill that the course most wants to see. Results become a measure of speed.

**Fix (all units).** One time rule, applied in each field 5 and field 7:
- About 1 minute per short locate or date item, 2 minutes per one-sentence explanation, 4 to 5 minutes per constructed map, 8 minutes for a one-paragraph claim.
- The end-of-unit claim for D3.4.3-5 and D4.1.3-5 is **one paragraph naming two sources**. A multi-paragraph argument is judged on the unit's closing day, where it already sits.
- Where the sum still exceeds the minutes, cut the number of instances, not the parts: one item per part, as days.csv says. Unit-specific cuts are in 3.2, 4.1, 5.6, 6.1 and 7.1.

LAYER plan (and process, see the structure pass). REPEAT: new to this course; the K and grade 1 reads did not meet written assessments of this length.

### CW2. Current official place names are not handled (minor, plan, firm)

**What is wrong.** Since 2025, US federal use names the Gulf of Mexico the "Gulf of America" and Denali "Mount McKinley" (Executive Order 14172; the Board on Geographic Names and GNIS list both; the Congressional Research Service update of 2026-09-15 still describes them as current). Denali National Park and Preserve keeps its name. Mexico and most other countries keep "Gulf of Mexico". The plans' maps (unit 1 continent maps, unit 6 M1 "Texas borders Mexico and the Gulf", unit 6 West and Southeast atlases, unit 7 hurricane cards) will show both features but no plan says what to print.

**Why it matters.** A teacher or parent will check a federal map and see a different name; a printed map with only one name looks either out of date or partisan. Value rule (b): state the fact.

**Fix.** Add one teacher-note line to s01.md field 6 teacher notes, and carry it in s06.md field 8: "Label the gulf 'Gulf of Mexico (named the Gulf of America in United States federal use since 2025)' and the peak 'Denali (Mount McKinley in United States federal use since 2025)'. State both as facts of naming; do not ask students which is right." Map-makers print both labels.

LAYER plan. REPEAT: of the current-facts settlement in the K and grade 1 reads.

### CW3. Tennessee rows say "blocked site not retried" (minor, process, firm)

Every field 10 comparison table (s01 to s07) says "Tennessee 2024 | STANDARD.md governs; blocked site not retried." Replace in each with: "Not yet compared; the 2024 standards PDF on tn.gov refuses automated reading. STANDARD.md governs." LAYER process. REPEAT: grade 1 read, the same wording fix.

### CW4. Clipped voice in a few repeated lines (minor, plan, firm)

The prose is mostly full sentences a teacher can read quickly. Three repeated lines are not:
- "Since Time Immemorial is not used." (field 10, every unit). A teacher does not know what this is. Replace with: "Washington State's Since Time Immemorial curriculum is not used; it is written for Washington nations."  Or delete the line; it is a note to the writer, not the teacher.
- "Step back on 144 and 157." and the like in each field 2 "Teaching" bullet. Write "On 144 and 157 students work without a teacher model."
- Field 2 "Teaching:" bullets list verbs without objects in places (s01 "model reading a source's maker, date, audience and purpose"; see 1.2).
LAYER plan. REPEAT: clipped voice, K and grade 1 reads.

### CW5. Current facts need a teacher background line, not student content (minor, process, likely)

Several units teach institutions that changed in 2025 and 2026 (Mexico's courts, trade among the three countries, federal disaster aid). The plans state structure correctly but give the teacher nothing for the obvious question. The fixes are in 2.1, 2.2 and 7.4. For the structure pass: the plan writer's brief should ask for a "current facts, checked on (date)" line wherever a unit teaches a living institution, a named living leader or a court ruling.

LAYER process. REPEAT: current facts (Huerta, birthright citizenship) in the K and grade 1 reads.

## Unit 1 (s01, days 1 to 11 and so on): the land and its maps

### 1.1 Start-of-year check invents a sitting before day 1 (moderate, plan, firm)

**What is wrong.** Field 4 gives two oral or paper items "a few days before day 1". Course day 1 is school day 1; there are no days before it. Both rows checked (ss3-map-skills, ss3-globe-grid) were taught the year before, so by the course rule (scope-and-sequence: "readiness checks: none; all are retrieval tasks") they get retrieval tasks, and those already sit on days 1 and 12 in days.csv. Item 2 also cites D2.Geo.10.3-5, which is not in this unit's skills.

**Why it matters.** The task asks unit 1 to define the start-of-year check. As written, a teacher either loses day 1 to a test or skips it; neither is what the course intends. It also duplicates the day 1 retrieval task.

**Fix.** s01.md field 4, replace the "a few days before day 1" block with:

"**Start-of-year check.** No separate sitting. Before day 1 the teacher reads the grade 3 record sheet if one came with the class. During days 1 to 3 note, for each child: reading support needed for a source card, how the child prefers to answer (spoken, written, pointing), and from the day 1 retrieval task whether the child can point to a map's title, key, compass rose and scale. These notes set groups for the day 1 and day 12 gap blocks. Nothing is scored."

Keep the gap blocks, fed by the day 1 and day 12 retrieval tasks. Delete the D2.Geo.10.3-5 citation.

LAYER plan. REPEAT: grade 1 item 1.1 and the K settlement (start-of-year check duplicating retrieval).

### 1.2 Day 1 models unit 4's step-up (minor, plan, firm)

Field 2 "Teaching: model reading a source's maker, date, audience and purpose" puts audience and purpose (for whom and why, which unit 4 introduces with exploration accounts) on day 1. Change to "model reading a source's maker and date". LAYER plan.

### 1.3 Day 6 exit does not give the scale value (minor, plan, firm)

The day 6 exit asks a distance from a bar scale but the prompt does not state the bar's value. Add "each bar is 60 kilometres" to the prompt. LAYER plan.

### 1.4 Exit 11 key is vague (minor, plan, firm)

The answer key "use the named living nation example" names nothing. Write the nation into the key (for example "the Navajo Nation, a government today"), or better, a nation not used elsewhere in the course (see 6.4). LAYER plan.

### 1.5 Day 3's Native nations are all from the United States (minor, plan, likely)

At a continental scale, day 3 names nations from Navajo and Cherokee pages only. Add a First Nation or Inuit example (for example Inuit of Nunavut, from Nunavut Tunngavik or Inuit Tapiriit Kanatami) so the continent is shown as continental. LAYER plan. REPEAT: Native content leaning on one nation (K and grade 1).

Checked correct: coordinates (40N 120W; 50N 100W; 30N 110W; 20N 90W; 60N 130W); Q1 arithmetic (3 cm is 1,200 km, about 750 miles); exit 5 (200 km); the Denver library east of the South Platte.

## Unit 2 (s02): three countries, research and trade

### 2.1 Sensitivity sources do not match the frame (moderate, plan, firm)

**What is wrong.** Field 10 "Community sources first" lists the Assembly of First Nations, an "Inuit children's page" at inuitcircumpolar.com, the Métis National Council and fiob.online.
- The Inuit Circumpolar Council is international (Canada, Greenland, Alaska, Chukotka). Canada's national Inuit organization is Inuit Tapiriit Kanatami (ITK). The frame asks for national organizations.
- FIOB is a binational organization of Oaxacan Indigenous migrants. It is a good source, but it is not "the Indigenous peoples of Mexico", and the frame names INPI. The plan names neither INPI nor a community source inside Mexico.
- Métis governance has more than one body; the Manitoba Metis Federation left the Métis National Council in 2021 (from memory; the sensitivity reader should confirm).
- Mexico's constitution has recognized Afro-Mexican peoples since 2019; day 23's "people and languages" research does not mention them.

**Why it matters.** Day 23 is flagged for the sensitivity read "from their own and their governments' pages". As listed, Canada's Inuit appear through an international body and Mexico's Indigenous peoples through a migrant organization in the United States.

**Fix.** s02.md field 10, replace the "Inuit children's page" link with Inuit Tapiriit Kanatami (itk.ca); label FIOB "a binational organization of Oaxacan Indigenous migrants"; add INPI (gob.mx/inpi) and one community-run source inside Mexico; add to the sensitivity study: "Métis governance today (the Métis National Council and the Manitoba Metis Federation), and Afro-Mexican recognition in Mexico's constitution (2019)." On day 23 add one line: "Mexico's constitution also recognizes Afro-Mexican peoples."

LAYER plan. REPEAT: Native nations from their own sources (K and grade 1 settlement).

### 2.2 Day 24's Mexico card needs 2025 to 2026 facts (minor, plan, firm)

Day 24's table compares heads of government, lawmakers and courts. Not wrong, but the teacher needs current facts: Mexico's 2024 judicial reform led to the first popular election of judges on 1 June 2025; nine elected Supreme Court justices (down from eleven) took office on 1 September 2025, for single 12-year terms. Current heads: President Claudia Sheinbaum (since October 2024), Prime Minister Mark Carney (since March 2025; majority government since spring 2026), King Charles III. The ine.mx page may predate the reform.

**Fix.** s02.md field 5, after the day 24 government anchor, add: "Teacher background, checked 2026-11-14: Mexico's Supreme Court justices have been elected by popular vote since 2025 (nine justices, seated 1 September 2025). Canada's prime minister is Mark Carney and the head of state King Charles III; Mexico's president is Claudia Sheinbaum. Check these before teaching." Refresh the Mexico research card against the current court page. LAYER plan.

### 2.3 Trade is taught with no current background (minor, plan, firm)

The limit "not tariffs" is right for students. But a teacher teaching Canada-Mexico-United States trade in 2026 will be asked about tariffs. Facts: the Supreme Court held on 20 February 2026 (Learning Resources, Inc. v. Trump, with Trump v. V.O.S. Selections) that IEEPA does not authorize tariffs; other tariffs continue under other laws. At the USMCA (CUSMA, T-MEC) joint review on 1 July 2026 the United States did not agree to renew, so the agreement stays in force to 2036 with yearly reviews.

**Fix.** s02.md field 2 Limits, append: "Teacher background, checked 2026-11-14: the three countries trade under USMCA (Canada calls it CUSMA, Mexico T-MEC), which stays in force after the July 2026 review, now with yearly reviews. In February 2026 the Supreme Court ruled that one emergency law does not let the president set tariffs. If students ask, state these as facts and return to specialization; no debate." LAYER plan. REPEAT: current court rulings (K and grade 1).

### 2.4 Corroboration model listed in reverse time (minor, data and skeleton, firm)

The skeleton's "Carried" line renders corroboration as first used in unit 4 and used again in unit 2. The order comes from frame.md's models-carried table, which lists Unit 4 as first use. Either the frame row is wrong (corroboration is first used in unit 2's research) or the skeleton reads it backward. Fix frame.md's corroboration row so unit 2 is first use, then re-render; flag to the structure pass. LAYER data. 

Note, no fix: the bicycle case D, E and F is invented and labelled as invented; acceptable. Day 28 presentation timing holds.

## Unit 3 (s03): first peoples and early societies

### 3.1 Assessment Q5 asks two paragraphs in 9 minutes (moderate, plan, firm)

Instance of CW1. **Fix.** s03.md field 5 Q5: make it one paragraph naming two sources (D3.4, D4.1), 8 minutes; move the linked second paragraph to the closing day's claim, which already judges extended writing. Re-total field 7. LAYER plan.

### 3.2 Mesa Verde has many associated tribes (minor, plan, likely)

The plan speaks for Mesa Verde through Hopi and the Indian Pueblo Cultural Center. The park lists 26 associated tribes, including the Ute Mountain Ute, whose lands hold Ute Mountain Tribal Park. Add to the teacher note: "Mesa Verde has 26 associated tribes today, including Pueblo nations and the Ute Mountain Ute; the sources here speak for some of them." LAYER plan.

Checked: Cahokia Mounds is still a State Historic Site (and a UNESCO World Heritage Site); federal bills for a National Historical Park have not passed, and a 2025 Senate bill (S. 1516) would only start a study. Q4's key is correct. White Sands footprints 21,000 to 23,000 years (2021, re-dated 2023); the 12,600-year corridor date; Cooper's Ferry about 16,000 years; exit 49 arithmetic. Native nations vary well across the unit (Hopi, Pueblos, Osage).

## Unit 4 (s04): exploration and encounter

### 4.1 Q4's timeline scale cannot show the overlap it asks for (moderate, plan, firm)

**What is wrong.** Q4's timeline runs 1400 to 1600 at 10 cm per century. Placements then need millimetres (1492 at 9.2 cm), and the Coronado and Cartier bars come out only a few millimetres long (at 1 mm per year, Coronado's 1540 to 1542 expedition is 2 mm). A child cannot draw or read overlap at that size. Exit 73 taught whole centimetres. Q4 also asks two timelines in 6 minutes (CW1).

**Fix.** s04.md field 5 Q4: keep the century line (1400 to 1600) for the landings only, and add an aligned zoom strip 1530 to 1550 at 1 cm per year for the Coronado and Cartier overlap. Key: placements on the century line accepted within 2 mm; on the zoom strip within 1 cm. Allow 8 minutes. LAYER plan.

### 4.2 Wendake does not speak alone for the St. Lawrence Iroquoians (minor, plan, likely)

Add a teacher note: "The St. Lawrence Iroquoian towns Cartier visited were gone by about 1600. Several nations today, including the Huron-Wendat and the Mohawk, count them as kin; no single nation's account is the whole story." LAYER plan.

### 4.3 Plan retrieval on days 65 and 73 is not in days.csv (minor, data, firm)

The plan adds retrieval tasks on 65 (ss3-early-colonies) and 73 (ss3-timeline); days.csv notes for those days do not carry them. Add "retrieval task on grade 3 ss3-early-colonies" to day 65's note and "retrieval task on grade 3 ss3-timeline" to day 73's note. LAYER data. REPEAT: retrieval notes missing in days.csv (grade 1).

### 4.4 L'Anse aux Meadows has an exact date (minor, plan, firm)

Q2's teacher background could add the current fact: tree rings show the wood was cut in 1021 CE (Kuitems and others, Nature, 2021). One line in field 5. LAYER plan.

Checked correct: Q4 arithmetic; Cortés's second letter (1520, to Charles V); the Tlaxcalteca as allies; Hawikuh and the A:shiwi (Zuni), 1540; Cartier's peoples.

## Unit 5 (s05): growth, choice and force

### 5.1 Q3 uses the Whitman mission with no teacher note (moderate, plan, firm)

**What is wrong.** Q3 asks students to use Narcissa Whitman's missionary purpose as a motive for moving west, while the unit's hook centres the Cayuse, Umatilla and Walla Walla (Confederated Tribes of the Umatilla Indian Reservation). There is no teacher note on the Whitman mission, the 1847 measles epidemic that killed many Cayuse, the killings at the mission that followed, or the hanging of the Cayuse Five. The sensitivity study does not ask for the CTUIR account of the Whitmans. Washington State voted in 2021 to replace its Marcus Whitman statue in the National Statuary Hall with Billy Frank Jr. (Nisqually), which shows how contested the Whitman story is today.

**Why it matters.** A child reading Q3 meets the Whitmans as a neutral motive example, in a unit whose own hook is the nation most harmed by that mission. A Cayuse or Umatilla family would find this one-sided; it fails the lens's "both sides of a forced move" check.

**Fix.** Either pick another documented woman's motive for Q3 (for example a family letter from the 1840s trail), or keep Q3 and add to field 6 teacher notes: "The Whitman mission is told differently by the Cayuse, Umatilla and Walla Walla. In 1847 a measles epidemic killed many Cayuse; some blamed the mission, and the Whitmans and others were killed. Five Cayuse men were hanged in 1850. Use the Whitmans only for what they said they wanted, beside the Confederated Tribes' account." Add to the sensitivity study: "the Confederated Tribes of the Umatilla Indian Reservation's account of the Whitman mission (Tamástslikt Cultural Institute)". LAYER plan.

### 5.2 Mojibake in names (minor, plan, firm)

"Guti?rrez" and "Ram?n" in fields 5 and 10 should be "Gutiérrez" and "Ramón". Fix every instance. LAYER plan.

### 5.3 Equiano's African birth is debated (minor, plan, likely)

Day 93 uses Olaudah Equiano's narrative of capture in Africa. Some historians (Vincent Carretta) found records giving his birthplace as South Carolina. Add a teacher note: "Historians debate whether Equiano was born in Africa; his book is still a widely read account of the Middle Passage." Or use Venture Smith's narrative. LAYER plan.

### 5.4 Day 93 retrieval answer overstates (minor, plan, firm)

The key "legal in all European colonies" is too broad for the grade 3 row. Change to "legal in all thirteen colonies". LAYER plan.

### 5.5 Hawaii items rest on one case, with no settling record (minor, plan, likely)

Q8 and Q9 both rest on Hawaii only. Add to the teacher note the 1993 Apology Resolution (Public Law 103-150), in which Congress acknowledged the United States' role in the 1893 overthrow, as the official record. Consider moving Q9 to another case of the unit so two items do not share one claim base. LAYER plan.

### 5.6 Nine items in 35 minutes (minor, plan, firm)

Instance of CW1: Q6 and Q7 share 7 minutes. Apply the CW1 rule and re-total field 7. LAYER plan.

Checked correct: Q2 dates; Q6 (Gadsden Purchase, 1853); Q7 (Colorado formed partly from the Mexican Cession); Article VIII; Vermont 1791. Not verified: day 86's claim that "the Oregon Trail was not moved away from the reservation as promised" (see What I could not judge).

## Unit 6 (s06): the states and regions

### 6.1 Day 131 asks five constructed maps in 13 minutes (moderate, plan, firm)

**What is wrong.** Field 7 gives "maps 13" on day 131, which holds F3a to F3e, five constructed state maps from atlases (title, scale, compass, key, cities and features each). Day 120 gives 23 minutes to its own map set. Five maps cannot be built in 13 minutes; F3d (New Mexico, with dated homeland layers and a forced-movement arrow) alone is a 5 minute task.

**Why it matters.** The day 131 note says the first-half codes "return as one short prompt each". Five full maps is not a short prompt.

**Fix.** s06.md field 5: on day 131, ask each student for one full constructed map (F3d, the Southwest, since MA.4.T4d.5 has the most parts), and for the other four regions one map-part prompt each (for example "add the scale and key to this partly drawn Wisconsin map"). Field 7: maps 5 plus 4 for the short prompts. If every region must keep a full map, judge four of them from the region maps students make on days 114 to 118, which the plan already collects. LAYER plan.

### 6.2 Bosque Redondo was also a Mescalero Apache confinement (minor, plan, firm)

F3d and the day 117 teacher note show Bosque Redondo as Navajo confinement only. The Mescalero Apache were confined there too, from 1863. Add to the day 117 teacher note and to F3d's key: "The Mescalero Apache were also held at Bosque Redondo." Add the Mescalero Apache Tribe's own account to the sensitivity study. LAYER plan.

### 6.3 Navajo carries both unit 1 and unit 6 (minor, plan, judgment call)

Unit 1 uses the Navajo Nation as its living-nation example, and unit 6's Southwest maps (F3d, the Arizona map) both use Navajo homelands. For one of the two unit 6 maps, use another Southwest nation (for example a Pueblo nation for the New Mexico map, or the Tohono O'odham for Arizona), or change unit 1's example (see 1.4). LAYER plan. REPEAT: Native nations varied across units (K and grade 1 settlement).

Checked correct: admission dates (PA and NJ 1787; MD 1788; Ohio 1803; Florida and Texas 1845; Iowa 1846; Oregon 1859; Utah 1896; Arizona 1912; Alaska and Hawaii 1959; Maine 1820; Vermont 1791; RI 1790; Michigan 1837, as the plan's own note corrects); spans 109, 125, 139 and 100; the territories' delegate powers stated as law. The plan's note that "the anchor dates Michigan to 1838" points at a source I could not find in frame.md, days.csv or the progression file; the plan itself uses 1837, which is right.

## Unit 7 (s07): the regions, peoples and hazards

### 7.1 Day 159 holds sixteen items in 30 minutes (moderate, plan, firm)

**What is wrong.** Field 7 gives cultures 9, hazards 6, movement and catastrophes 6, policy 5, argument 4. The culture block alone asks five written sentences plus underlining across 26 named groups on five strips that must first be read aloud. M1 and M2 ask three explanations from two diagram sets in 6 minutes. P2 asks a New Zealand reading and comparison inside 5 minutes with P1.

**Fix.** s07.md field 5: for C1 to C5, keep the underlining on all five strips (it checks every named group) and ask a written sentence on two strips only (the West, which has the most groups, and the student's own region or the Southeast). Allow cultures 8, hazards 6, M1 and M2 8, P1 and P2 8. Make A1 one paragraph (CW1) and judge its longer form from day 158's closing claim, which field 5 already collects. Re-total field 7 to 30. LAYER plan.

### 7.2 Day 141's soldiers are a hard case on a Native nations day (minor, plan, firm)

Day 141's caption: "African American soldiers helped establish communities around Southwestern army posts." These were the Buffalo Soldiers, who also served in the army's campaigns against the Apache and other nations. Day 141 is flagged "Native nations" for the sensitivity read. Add a teacher note: "The Buffalo Soldiers built posts and towns and also fought in the army's wars against Apache and other nations. Teach both." Add the topic to the field 10 sensitivity study. LAYER plan.

### 7.3 The strips name groups the sensitivity study does not source (minor, plan, likely)

The regional strips and exits name Somali, Hmong, Vietnamese, Cuban, Arab American, Filipino and Japanese American communities, plus Spanish mission labor in California. The sensitivity study sources Native nations, Chinese American (CHSA) and Japanese American (Densho) archives, and the CDC. The plan says strip examples are "from memory pending verification". Add to the field 10 sensitivity study: "one community-owned source for each immigrant community named on a strip or exit (for example the Filipino American National Historical Society, a Hmong American museum or center, a Somali community organization in Maine), and a California Native nation's account of the missions." The cherokee.gov link is the Eastern Band of Cherokee Indians; say so, since there are three federally recognized Cherokee nations. LAYER plan.

### 7.4 Federal disaster aid is under review in 2026 (minor, plan, likely)

The retrieval on day 152 and the response teaching name "national disaster aid". In May 2026 the FEMA Review Council recommended moving disaster recovery toward states, with lump-sum grants and higher thresholds for federal declarations; most changes need Congress, and I found no later outcome. **Fix.** s07.md field 6 teacher notes, add: "Teacher background, checked 2026-11-14: the federal government's disaster role (FEMA) is under review. Before teaching day 152, check the current FEMA and state emergency pages and teach who decides now. No debate." LAYER plan. REPEAT: current facts.

Checked correct: Johnstown (1889; rain plus the South Fork Dam failure; the plan rightly avoids claiming a court finding); Florida's building code path (Andrew 1992, study commission 1996, laws 1998 and 2000, statewide code in force 2002); Christchurch's 2011 consultation and August 2011 draft plan; Japan's Reconstruction Agency 2013 account; the 1882 exclusion law as described; the incarceration and the 1988 apology; Allensworth; Eatonville; Biddy Mason. Retrieval days 137, 152 and 155 match days.csv. Unit 6's day 132 response and course days 133 to 136 hand on cleanly.

## Settled by the expert

| Question | Ruling | Where it binds |
|---|---|---|
| When is readiness given, and what is unit 1's start-of-year check? | Settled earlier (K and grade 1 reads): readiness in the last ten minutes of the previous unit; unit 1 by the start-of-year check. For grade 4, the start-of-year check is the grade 3 record plus access notes from days 1 to 3, no separate sitting; the gap blocks are fed by the day 1 and day 12 retrieval tasks. | s01 field 4 (1.1) |
| How long may an end-of-unit assessment run? | Its minutes in field 7, with about 1 minute per locate or date item, 2 per one-sentence explanation, 4 to 5 per constructed map, 8 per one-paragraph claim. The D3.4 and D4.1 claim on the assessment is one paragraph with two named sources; longer arguments are judged on the closing day. Cut instances, never parts. | every field 5 and 7 (CW1) |
| How are renamed places labelled? | Both names, as facts: the common name first, the United States federal name in brackets with its year. No student vote on which is right. | maps in s01, s06, s07 (CW2) |
| How are 2025 to 2026 political and legal changes handled? | A teacher background line, dated "checked (date)", stated as fact and not argued; students keep the unit's limits. Settled earlier as "current official facts" (K and grade 1). | s02, s07 (2.2, 2.3, 7.4) |
| Native nations across units | Settled earlier: varied across units, each from its own sources. Applied here to Navajo (1.4, 6.3), Inuit (2.1) and the Mescalero Apache (6.2). | s01, s02, s06 |
| Observation and spoken evidence | Settled earlier: never the only teaching minutes of a new skill; spread across the unit. Grade 4 uses written exits, so the grade 1 exit-format findings do not apply. | none here |
| Tennessee wording | Settled earlier (grade 1): "Not yet compared; the 2024 standards PDF on tn.gov refuses automated reading." | every field 10 (CW3) |

## For the fixer

Exact edits, in order. Nothing here adds days.

1. s01.md field 4: replace the "a few days before day 1" block with the start-of-year check text in 1.1; delete the D2.Geo.10.3-5 citation.
2. s01.md field 2 Teaching: "maker, date, audience and purpose" to "maker and date" (1.2).
3. s01.md day 6 exit: add "each bar is 60 kilometres" (1.3).
4. s01.md exit 11 key: name the nation (1.4); day 3: add an Inuit or First Nation example (1.5).
5. s01.md field 6 teacher notes and s06.md field 8: add the dual-label line from CW2.
6. s02.md field 10: ITK for the Inuit page; label FIOB; add INPI and a source inside Mexico; add the Métis and Afro-Mexican lines to the sensitivity study; day 23 Afro-Mexican line (2.1).
7. s02.md field 5: day 24 teacher background line (2.2). Field 2 Limits: trade background line (2.3).
8. frame.md models-carried, corroboration row: unit 2 first use, unit 4 used again; re-render s02 and s04 "Carried" lines (2.4).
9. s03.md field 5 Q5 to one paragraph, 8 minutes; re-total field 7 (3.1). Field 6: Mesa Verde tribes line (3.2).
10. s04.md Q4: century line plus 1530 to 1550 zoom strip, tolerances, 8 minutes (4.1); St. Lawrence Iroquoian note (4.2); Q2 1021 CE line (4.4).
11. days.csv day 65 and day 73 notes: add the retrieval tasks (4.3).
12. s05.md: Whitman teacher note and sensitivity source, or replace Q3 (5.1); fix "Gutiérrez" and "Ramón" (5.2); Equiano note (5.3); day 93 key "all thirteen colonies" (5.4); 1993 Apology Resolution (5.5); re-total field 7 (5.6).
13. s06.md day 131: one full constructed map plus four map-part prompts; field 7 maps 9 (6.1). Day 117 note and F3d key: Mescalero Apache (6.2). One Southwest map to another nation (6.3).
14. s07.md day 159: C sentences on two strips, underlining on all; field 7 re-totalled (7.1). Day 141 note (7.2). Field 10 sensitivity sources (7.3). Field 6 FEMA background line (7.4).
15. Every field 10: Tennessee wording (CW3); "Since Time Immemorial" line rewritten or removed (CW4).

## For the structure pass

- **Assessment time budget.** Add the CW1 minutes rule to the plan writer's brief (docs/pipeline/briefs/) and to UNIT-PLAN.md field 7, so field 7 sums are checked against item counts. A check script could flag any assessment table with more than about one row per 2.5 minutes.
- **Models-carried order.** scripts/unit_skeleton.py should sort "from" and "used again" by unit number, or reject a frame row whose first use comes after a later use (2.4).
- **Retrieval notes in days.csv.** A check that every retrieval task a plan names exists in days.csv notes, and the reverse (4.3). REPEAT from grade 1.
- **Current facts line.** The plan writer's brief asks for a "current facts, checked on (date)" teacher line wherever a unit teaches a living institution, a named living leader, a renamed place or a court ruling (CW2, CW5).
- **Tennessee wording.** Change the template text that produces "blocked site not retried" (CW3).
- **Encoding.** The writer's output path turned é and ó into "?" in s05. Check the write step's encoding (5.2).

## For Cory

None.

## What is right

- Every MA.4 standard and every listed C3 indicator has an item, and days.csv's "every part of each listed code asked once" holds across all seven units.
- Retrieval tasks sit on the days days.csv names, and the plans treat grade 3 rows as retrieval, not readiness, as scope-and-sequence says (except unit 1, 1.1).
- Invented and constructed sources are labelled as such everywhere; no invented source is passed off as real.
- Error registers are real errors, and most items have wrong answers keyed to error letters that tell them apart.
- Hard history is named plainly with dignity: removal, slavery, exclusion, incarceration with the apology, mission labor, the Long Walk.
- Disaster content follows the limits: no reenactment, no family disclosure, adults handle emergencies, sending a proposal is the student's and teacher's choice.
- Hand-ons between units are clean; each unit's response day leads into the next unit's retrieval.

## What I could not judge

- Day 86's claim that the Oregon Trail was not moved away from the Umatilla reservation as promised. Needs the CTUIR's own account.
- Whether Billy Frank Jr.'s statue has been installed in the National Statuary Hall yet (the law passed in 2021; a July 2026 report covers Olympia only). The 5.1 fix does not depend on it.
- Métis governance details beyond 2021, from memory.
- Tennessee 2024, not readable by automation.
- The many regional strip examples in s06 and s07 that the plans mark "from memory pending verification"; the ones I knew are right.

## Sources (web checks, 2026-11-14)

- Supreme Court tariff ruling, 20 February 2026: National Law Review, "US Supreme Court holds IEEPA does not authorize presidential tariffs"; Faegre Drinker summary of Learning Resources, Inc. v. Trump and Trump v. V.O.S. Selections.
- USMCA joint review, 1 July 2026: White & Case insight alert; Greenberg Traurig, "USMCA joint review triggers annual reviews but does not alter current trade benefits".
- Mexico's elected Supreme Court, 1 September 2025: Euronews and Africanews, "Mexico's new Supreme Court takes office"; Human Rights Watch, 1 September 2025.
- Canada's prime minister: pm.gc.ca (news to 5 November 2026); AP via WTOP, April 2026 majority.
- Geographic names: Congressional Research Service IF12881, updated 2026-09-15; Department of the Interior press release on Mount McKinley.
- Cahokia: Department of the Interior testimony on S. 1211 (117th Congress); S. 1516 (119th Congress), a study bill.
- Whitman statue: Northwest Public Broadcasting, "Statue honoring Billy Frank Jr. to replace Marcus Whitman at U.S. Capitol"; KNKX, 2026-07-26.
- FEMA Review Council, May 2026: Michigan Public, 2026-05-07; Maryland Matters, 2026-05-07.

## Confidence

Firm on CW1, 1.1, 4.1, 6.1 and 7.1 (arithmetic of the plans' own minutes and scales). Firm on the dated current facts above. Likely on the sensitivity source gaps (2.1, 5.1, 6.2, 7.2, 7.3). Judgment call on 6.3.

## For the source list

- Inuit Tapiriit Kanatami, itk.ca (Canada's national Inuit organization).
- INPI, gob.mx/inpi.
- Tamástslikt Cultural Institute (CTUIR) for the Whitman mission and the Oregon Trail.
- Mescalero Apache Tribe, for Bosque Redondo.
- Public Law 103-150 (1993 Apology Resolution).
- Kuitems and others, Nature 2021, on the 1021 CE date at L'Anse aux Meadows.
- CRS IF12881, Trump Administration Actions: Geographic Naming.
