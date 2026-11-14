# Plan read: social studies grade 5, units 1 to 10 (2026-11-14)

Expert cold read of docs/courses/social-studies-grade-5/s01.md to s10.md, written today by Codex from unit_skeleton.py skeletons. Fields between skeleton markers were treated as mechanical; findings on them are tagged skeleton or data.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/pipeline/briefs/plan-read.md, docs/agents/lenses/social-studies.md, docs/ADOPTION-BAR-SUBJECTS.md (social studies part), docs/courses/social-studies/STANDARD.md.
- docs/courses/social-studies-grade-5/frame.md, scope-and-sequence.md, s01.md to s10.md in full (fields 2 to 10 and day lists).
- data/plans/social-studies-grade-5/days.csv (all 160 rows), data/progressions/social-studies.csv (grade 3 to 5 rows used), data/standards/ma-hss-2018.txt (5.T1 to 5.T5).
- Earlier plan reads for kindergarten, grade 1, grade 3 and grade 4 (2026-11-14), for their settled tables.
- `plan.py check`: social-studies-grade-5 frame and sequence pass with 0 failures and one note (Seams does not name wh2-social-movements).
- Web checks, listed under Sources.

## Course verdict

Close to the bar, not at it. The content is largely accurate, the hard history is named plainly and taught with care (1619 framing, Stono, Mystic, removal, the Georgia secession declaration, Reconstruction violence, Jim Crow), and units hand on cleanly with carried models that really do return. What keeps it below the bar is one break of the lead's start-of-year rule in unit 1, end-of-unit assessments packed past their minutes in every unit (a repeat of grade 4), a unit with no daily evidence table (unit 6), and Native nations assessed in units 3, 4 and 7 without their own sources. None of this needs Cory; all of it is fixable in the plans and two data cells.

## Course-wide findings

**CW1. End-of-unit assessments carry more parts than their minutes hold.** Moderate. LAYER plan. REPEAT (grade 4 CW1; grade 3 settlement of about eight one-thing prompts in 30 minutes).
- s01 day 13: six questions, most multi-part, in 34 minutes. s02 day 25: eight multi-part items in 34. s03 day 42: Q2 carries a comparison, a historical claim, D3.4 and D4.1 in 7 minutes; Q4 a slogan plus three institutions in 3. s04 day 58: Q1 has seven components in 5 minutes; Q7 four skills in 6. s05 day 74: Q3 a to c in 4. s06 day 95: 40 minutes with Q2 to Q4 packed. s07 day 111: Q1 has five removal captions in 9. s08 day 125: Q4 many parts in 7. s09 day 141: Q1 asks four barriers and three institutions in 6, Q4 four named parts in 4.
- Why: an overpacked item reports speed, not understanding, and the teacher cannot tell which part was missed.
- Fix: apply the settled budget (about 1 minute per locate or date item, 2 per one-sentence explanation, 4 to 5 per constructed map, 8 per one-paragraph claim). Cut the number of instances, never the parts of a code. Each closing claim is one paragraph at 8 minutes, except where the unit's only claim item already has 13 (s09 Q6 is fine).

**CW2. Boilerplate "Since Time Immemorial is not used."** Minor. LAYER plan (template echo). REPEAT (grade 4 CW4).
- In field 10 of s01 to s08. Fix: delete the sentence in each.

**CW3. Tennessee wording.** Minor. LAYER plan. REPEAT (grade 4 settlement).
- s01 to s10 field 10 check-set tables say "Site known blocked; no retry", "Known blocked; no retry", "blocked, not retried" and similar. Fix: replace each Tennessee row's decision cell with "Not yet compared; the 2024 standards PDF on tn.gov refuses automated reading."

**CW4. Prince Hall's 1777 petition is used five times.** Minor. LAYER plan. Judgment call.
- Unit 2 assessment source B, unit 3 day 27 retrieval, unit 4 hook, unit 5 hook plus days 62 and 67. Why: a strong source turns into a stock answer, and students can score on recall of it rather than reading.
- Fix: s05 field 2 hook, swap Hall for Benjamin Banneker's letter to Thomas Jefferson of 19 August 1791 (it argues from the Declaration's equality claim, which fits unit 5). Keep Hall in units 2 to 4.

**CW5. Identity labels on scholars.** Minor. LAYER plan.
- s01 field 10 calls Jared Hardesty a "Black historian". Nothing in his Western Washington University profile or publisher material says so. Fix: s01 field 10, old "Black historian Jared Hardesty on colonial labor", new "Jared Ross Hardesty on colonial New England slavery (Unfreedom, 2016)". If a Black-authored colonial source is wanted, add Lorenzo J. Greene, The Negro in Colonial New England (1942). General rule for the sensitivity lists: name scholars by work, not by a label we have not verified.
- Checked as right: Shirley Ann Wilson Moore is the credited author of the NPS chapter "Race, Slavery and Freedom: The Contagion of Liberty" (in Sweet Freedom's Plains, prepared for the National Park Service), used in s04 and s05.

## Unit 1 (s01)

**1.1 Start-of-year check breaks the lead rule.** Serious. LAYER plan. REPEAT (grade 4 item 1.1, lead rule of 2026-11-14).
- Field 4 sets a ten-minute, six-item sitting "a few days before day 1" on grade 4 rows. There is no sitting before day 1, and unit 1 has no readiness rows in days.csv.
- Fix: s01 field 4, replace the whole start-of-year block with: "**Retrieval only:** none needed; retrieval only. days.csv holds no readiness check before this unit; the retrieval tasks below are its before-teaching evidence." Keep the day 1 and day 10 retrieval rows unchanged.

**1.2 Q2 assumes every student researched Williams.** Moderate. LAYER plan.
- Day 8 lets each student choose Penn, Williams or Winthrop; the assessment asks all students to check a finding about Williams. Fix: Q2 reads "Check one finding about the founder you researched against the card for that founder"; the withheld packet supplies three founder cards (Penn, Williams, Winthrop), each with one corroborating and one complicating detail.

**1.3 Letters collide.** Moderate. LAYER plan.
- Source cards A to D and M, labour symbols F, H, I and E, and exit ids E1 to E12 share letters with error letters A to H, so "(E)" in a key can mean three things. Fix: number the source cards 1 to 5, mark labour symbols with words (field, household, craft, sea), and keep letters for errors only. Exit rows can keep E1 to E12 only if renamed X1 to X12.

**1.4 Card D cites standards as its sources.** Minor. LAYER plan.
- Card D lists "the anchor's MA.5.T1.3 and New York framework 4.3b". A standard is not a historical source, and check-set names do not belong in student copy. Fix: cite the 1629 Massachusetts Bay charter (Avalon Project) and an NPS or state archive page.

**1.5 E12 is too big for an exit ticket.** Minor. LAYER plan.
- A map, a claim and a D1.1 reason on a quarter page in two minutes. Fix: keep the map label only; move the claim to day 13.

**1.6 Mystic needs a plainer warning.** Minor. LAYER plan.
- Day 4 teacher note uses Underhill. His account justifies killing women and children. Fix: add "Underhill's account defends the killing of Pequot women and children; the class reads only the caption, which calls it a massacre."

**1.7 Name Metacom.** Minor. LAYER plan.
- Fix: wherever "King Philip's War" appears, add "(Metacom, also Metacomet, the Pokanoket Wampanoag sachem the English called King Philip)".

**1.8 Regional crop examples "from memory pending verification".** Minor. LAYER process. Fix: verify against the NPS and Colonial Williamsburg pages before section writing, then drop the flag.

CW1, CW2, CW3, CW5 apply.

## Unit 2 (s02)

**2.1 "Legal in every colony" needs Georgia's exception.** Minor. LAYER plan.
- Georgia's trustees banned slavery from 1735 until 1751. Fix: teacher explanation, add "Georgia barred slavery from 1735 to 1751, then allowed it; by 1755 it was legal in every colony."

**2.2 Q5 uses a 1795 example.** Minor. LAYER plan.
- The White House payroll naming James Hoban's enslaved carpenters is early republic, not colonial. Fix: use a colonial example, for example the enslaved workers recorded at Philipsburg Manor or the Royall House.

**2.3 Q3's sources are thin on work and family.** Minor. LAYER plan.
- A (Equiano's crossing) and B (Hall's petition) hold little on daily work; the item leans on M. Fix: give Q3 a source about labour and family, or narrow Q3 to what A and B show.

**2.4 Venture Smith from a course-host page.** Minor. LAYER plan. Fix: cite Documenting the American South (docsouth.unc.edu) for the 1798 Narrative.

**2.5 Day 15 retrieval missing from days.csv.** Minor. LAYER data.
- s02 names a ss4-choice-and-force retrieval task on day 15; the days.csv note does not. Fix: add "retrieval task on grade 4 ss4-choice-and-force" to day 15's note, or drop it from s02.

CW1, CW2, CW3 apply. Right: the 1619 framing, the 1662 and 1667 Virginia laws, the Equiano birthplace caveat, the oral-history label on the Cato account, and Hall kept apart from the freedom suits.

## Unit 3 (s03)

**3.1 No sensitivity study paragraph.** Moderate. LAYER plan and data.
- The frame names no study list for unit 3, and s03 has none, though days 28 and 34 are flagged and the Proclamation of 1763 and Pontiac's War are taught. Fix: add a paragraph naming the Delaware Nation, the Delaware Tribe of Indians, the Shawnee Tribe, the Absentee Shawnee Tribe, the Eastern Shawnee Tribe, the Seneca Nation, the Oneida Indian Nation and the Little Traverse Bay Bands of Odawa Indians, plus scholarship on Crispus Attucks; name Pontiac's War in the Proclamation teacher explanation. The frame gets a matching unit 3 cell (see the structure pass).

**3.2 Day 34 "a soldier's trial testimony" is not what the plan uses.** Minor. LAYER data.
- days.csv day 34 and the frame say a soldier's testimony; the plan uses a defense witness who is not identified as a soldier. Fix: use Captain Thomas Preston's account (a soldier's own account, 1770), or change the days.csv note to "a trial witness's testimony".

**3.3 The law-breaking claim lacks a law-breaking source.** Minor. LAYER plan. Judgment call.
- The closing claim on breaking a law uses the Stamp Act Congress resolutions and the Declaratory Act; neither shows law-breaking. Fix: add a short Boston Tea Party account (for example George Hewes's later recollection, labelled as later).

CW1, CW2, CW3 apply. Right: Parker and Barker as withheld Lexington accounts, the "Townsend" spelling handled, Revere's print credited as adapted from Pelham.

## Unit 4 (s04)

**4.1 Mohawk warriors taught and assessed without a Mohawk source.** Moderate. LAYER plan. REPEAT (settled: each nation from its own sources).
- Q3 and the teaching use Mohawk alliance with Britain; only Oneida and Onondaga sources are read. Fix: add a Mohawk nation's own history page (Saint Regis Mohawk Tribe, Six Nations of the Grand River, or the Mohawk Council of Akwesasne) to field 10 and to the day teaching it.

**4.2 Frame cell says retrieval where days.csv has a readiness check.** Minor. LAYER data (copied by skeleton into field 10).
- frame.md, unit 4 row, Sensitive topics: old "postwar prices and debts open with a short retrieval task on grade 3's money", new "postwar prices and debts follow the readiness check on grade 3's money (day 43)".

**4.3 The Declaration's slur is omitted without saying so.** Minor. LAYER plan.
- Rightly not printed. Fix: teacher note, add "The Declaration's list of grievances named Native nations as enemies with a slur; we describe that, we do not print it."

**4.4 Postwar deflation facts not yet verified.** Minor. LAYER process. Fix: verify before section writing.

CW1, CW2, CW3, CW4 apply. Checked right: Articles adopted 1777 and ratified 1781; the Dartmouth (Cuffe) petition of 10 February 1780; "Remember the Ladies", March 1776; the Northwest Ordinance's fugitive clause; New Jersey women voters to 1807.

## Unit 5 (s05)

**5.1 Sovereignty wording.** Minor. LAYER plan.
- Old "Native nations govern independently today", new "Native nations govern themselves as sovereign nations within the United States today."

**5.2 Heller on a day that already covers ten amendments.** Minor. LAYER plan. Judgment call.
- Fix: move Heller to a teacher background line: "District of Columbia v. Heller (2008) held the Second Amendment protects an individual right; checked 2026-11-14." Not student content.

**5.3 The slavery-teaching framework is unread.** Minor. LAYER process. Fix: the sensitivity agent reads Teaching Hard History: American Slavery (Learning for Justice) by hand or names another; the plan's note stays until then.

CW1 (Q3 a to c in 4 minutes), CW2, CW3, CW4 (hook) apply. Checked right: Davie's threat of 12 July 1787; Jefferson's letter to Madison of 20 December 1787; Madison's speech of 8 June 1789; Mason's section 10; the resolution of 25 September 1789.

## Unit 6 (s06)

**6.1 No daily exit or evidence table.** Moderate. LAYER plan (and skeleton, which does not require one).
- The only unit without one; plan-read's "every goal has an item" check cannot pass for days 80 to 94. Fix: add field 5's "Daily evidence for the section writer" table, one exit row per teaching day, each linked to an assessment item and error letter, in the format of s05 and s07.

**6.2 Sacagawea's nation stated as one account.** Moderate. LAYER plan. Sensitivity.
- The key says "She was Lemhi Shoshone." The MHA Nation (Hidatsa) holds a different account and spells her name Sakakawea. Fix: teacher explanation and key: "The Lemhi Shoshone and the Hidatsa of the MHA Nation tell different accounts of her origin; we teach both and do not score her nation." Add both nations' own pages to field 10.

**6.3 Cotton gin attribution.** Minor. LAYER data.
- frame.md unit 6 "Check set adds" and days.csv day 93 say "California grade 5, the cotton gin"; it is California 8.7.1. Fix both cells: "California 8.7.1 (grade 8), the cotton gin". The plan already flagged this for the lead.

CW1 (40 minutes on day 95 with no marking time named), CW2, CW3 apply. Checked right: Clementine Averill's "Letter from a Factory-Girl to Senator Clemens", Lowell, 6 March 1850, and "Factory Life As It Is" by An Operative, 7 November 1845 (Voice of Industry), both as printed on the NPS page cited; Lewis's journal of 16 May 1805; New Orleans fought after Ghent was signed and before ratification.

## Unit 7 (s07)

**7.1 Four Southeastern nations assessed without their own sources.** Moderate. LAYER plan. REPEAT (each nation from its own sources).
- Q1e and day 103 assess the Muscogee, Choctaw, Chickasaw and Seminole removals; field 10 says the other nations' pages "remain uninspected". Tecumseh rests on an Indiana state marker. Fix: add the Muscogee (Creek) Nation, Choctaw Nation of Oklahoma, Chickasaw Nation, Seminole Nation of Oklahoma and Seminole Tribe of Florida pages, the Eastern Band of Cherokee Indians and United Keetoowah Band beside the Cherokee Nation, and a Shawnee nation's page for Tecumseh.

**7.2 The Norfolk manifest needs an exact citation.** Minor. LAYER plan.
- "Use the Thomas Hunter's 1835 Norfolk-to-New Orleans record" cites only a NARA background page. The record is real: the schooner Thomas Hunter, Norfolk 17 October 1835 to New Orleans 11 November 1835, NARA M1895, roll 7. Fix: old "the Thomas Hunter's 1835 Norfolk-to-New Orleans record", new "the manifest of the schooner Thomas Hunter, Norfolk to New Orleans, October to November 1835 (NARA M1895, roll 7)". Read the names from the image before printing them.

**7.3 Cherokee removal and enslaved people.** Minor. LAYER plan. Hard history.
- Fix: teacher background line: "Some Cherokee slaveholders forced enslaved Black people west on removal; their descendants are the Cherokee Freedmen." Classroom wording is the sensitivity agent's.

CW1, CW2, CW3 apply. Checked right: the Mashpee resolutions of 21 May 1833 and the notice of 25 June 1833 (Daniel Amos, Israel Amos), both in Apess's 1835 Indian Nullification.

## Unit 8 (s08)

**8.1 The written-for-us historian paragraph needs a student-facing label.** Minor. LAYER plan.
- Packet H is an original "Curio Class historian paragraph" used for D2.His.17 (summarize a secondary work). Fix: print "Written by Curio Class for this task" on the student copy.

**8.2 Chesnut card overstates one fact.** Minor. LAYER plan.
- He is listed as the Kershaw member of a committee of the 1865 South Carolina Colored People's Convention and later sat in the 1868 constitutional convention and the state House; I could not confirm he signed the memorial. Fix: old "John A. Chesnut signed the 1865 South Carolina petition", new "John A. Chesnut of Kershaw District served at the 1865 South Carolina Colored People's Convention".

**8.3 Field 7 day 126 arithmetic reads wrongly.** Minor. LAYER plan. Fix: "Marking, five minutes; feedback, five; repair and retries, 30. Total 40."

**8.4 Study list lacks Reconstruction scholarship by Black historians and community archives.** Minor. LAYER plan. Fix: add the Colored Conventions Project and Thavolia Glymph's or Kidada E. Williams's work, named by work.

CW1, CW2, CW3 apply. Right: Meade at Gettysburg; the 13th Amendment's punishment exception named; the 15th's omission of sex; the Edisto petition of 28 October 1865; the Georgia declaration withheld and handled plainly.

## Unit 9 (s09)

**9.1 Packet D is not unseen.** Moderate. LAYER plan.
- The 1966 women organizers' statement is withheld source D on day 141, but field 2 names it in the day 140 closing claim and field 10 lists it for 136 to 139. Fix: field 2, closing claim, old "use Brown's ruling, the women organizers' 1966 statement and the current disability-law overview", new "use Brown's ruling, the 1965 Act and the current disability-law overview"; teach day 136 from a different women's movement document.

**9.2 "Who 1920 still left out" stays vague.** Moderate. LAYER plan. Accuracy and variety.
- Packet E says the amendment "did not itself change citizenship restrictions affecting other women" and names no one. Unit 9 has no Native or Asian American content. Fix: E's context and the day 132 teacher explanation add "Many Native people were not citizens until 1924, and some states kept Native people from voting until 1948 or later; Asian immigrant women could not become citizens until 1952." Add a Native nation or NMAI source to field 10.

**9.3 No current-law line on the Voting Rights Act.** Minor. LAYER plan. Current fact.
- Day 135 teaches the 1965 Act. Fix: teacher background line: "On April 29, 2026, in Louisiana v. Callais, the Supreme Court ruled 6 to 3 that Section 2 did not require a second majority-Black congressional district in Louisiana and struck that district down; it narrowed how Section 2 applies to maps without striking the section down (checked 2026-11-14)."

**9.4 Section 504 current line.** Minor. LAYER plan. Current fact.
- Fix: day 137 teacher line: "Section 504 and the ADA remain law; a federal case over parts of the 2024 Section 504 rule (Texas v. Kennedy, filed as Texas v. Becerra) has been in court through 2026 (checked 2026-11-14)."

**9.5 Weak source for Klan violence.** Minor. LAYER plan. Fix: replace the NPS "Reconstruction in the national capital area" page with an NPS or NMAAHC page on Reconstruction-era and Jim Crow violence.

CW1 (Q1 and Q4) applies. Right: Brown stated as a schools ruling, the 19th as a sex-discrimination bar, the 1964 and 1965 Acts kept distinct, the 504 sit-in with Black Panther and church support, Itliong and Filipino workers not labelled Latino, Stonewall not called the beginning, Obergefell stated as a ruling. Current facts checked: Dolores Huerta died 28 October 2026, so past tense is right; the March 2026 allegations against Cesar Chavez are real and the plan's handling (center workers, no hero celebration, sensitivity agent answers questions without detail) is right; the Davis petition was denied 10 November 2025.

## Unit 10 (s10)

**10.1 Printed topic sets cover only four topics.** Moderate. LAYER plan.
- MA.5.T5.8 says "African Americans, women, and others". The four printed sets (Brown, Montgomery, Voting Rights Act, ADA) include no women's, farmworker, Native or LGBTQ topic, though unit 9 taught them. Fix: add two printed sets from unit 9's content, for example the 19th Amendment or Title IX (1972), and the Delano grape strike and boycott, each with three distinct works and a documented opposing view.

**10.2 Callais line is incomplete.** Minor. LAYER plan. Current fact.
- "the Court rejected Louisiana's challenged district map" omits the holding. Fix: use the line in 9.3 in the Voting Rights Act topic set.

**10.3 Slavery framework on the unit 10 study list.** Minor. LAYER plan. Fix: replace with a civil rights era teaching source (for example the SNCC Digital Gateway's teaching pages).

Right: the readiness check on day 146 (ss3-deliberation) with reteach on 147 and 148 before the decision on 156; no counterclaim required; action boundaries (no cost, within the adult's authority, no private data, no political position, students choose); rubric separates political agreement and action success from the judgment; Section 201(a) paraphrase and 2 July 1964 date.

## Settled by the expert

| Question | Settled |
|---|---|
| Unit 1 start-of-year check | None needed; retrieval only. Day 1 and day 10 retrieval tasks stay. |
| Letters in unit 1 | Numbers for sources, words for labour symbols, letters for errors only. |
| Sacagawea's nation | Two accounts taught (Lemhi Shoshone, Hidatsa of the MHA Nation); her nation is not scored. |
| Day 34 testimony | Preston's own account, or the days.csv note changes to "a trial witness's testimony". |
| Cotton gin attribution | California 8.7.1 (grade 8). |
| Unit 5 hook | Banneker's 1791 letter replaces Hall. |
| Assessment minutes | The grade 4 budget applies to every unit (cite grade 4 CW1). |
| Scholar labels | Name scholars by work, not by unverified identity labels. |
| Unseen packets | A withheld source is not named in any teaching day or closing claim. |
| Who 1920 left out | Named: Native people (citizenship 1924, state bars later), Asian immigrant women (1952). |
| Voting Rights Act today | Dated Callais line in units 9 and 10. |

## For the fixer (in order)

1. s01 field 4: replace the start-of-year block with the "none needed; retrieval only" text (1.1).
2. All units: resize the end-of-unit assessments to the minutes budget (CW1).
3. s06 field 5: add the daily evidence table (6.1).
4. s09 field 2: change the closing claim sources; change day 136's women's movement document (9.1).
5. s03 field 10: add the sensitivity study paragraph (3.1). s04 field 10: add a Mohawk source (4.1). s07 field 10: add the Southeastern and Shawnee nations' pages (7.1).
6. s06: Sacagawea two accounts (6.2). s09: name who 1920 left out (9.2). s10: add two topic sets (10.1).
7. s01 Q2 founder cards and letter scheme (1.2, 1.3).
8. Current-fact lines: s09 9.3 and 9.4; s10 10.2; s05 5.2.
9. Data: days.csv day 15 note (2.5), day 34 note (3.2) if Preston is not used, day 93 note (6.3); frame.md unit 4 Sensitive topics cell (4.2), unit 6 Check set adds cell (6.3).
10. Minor plan edits: 1.4 to 1.7, 2.1 to 2.4, 3.3, 4.3, 5.1, 5.3, 7.2, 7.3, 8.1 to 8.4, 9.5, 10.3, CW4, CW5.
11. Delete "Since Time Immemorial is not used." in s01 to s08 (CW2); replace Tennessee rows (CW3).

## For the structure pass

- The skeleton or plan brief should require field 5's daily evidence table in every unit (s06 had none).
- Every unit needs a sensitivity study paragraph, and every nation taught or assessed needs its own source there; the frame's per-unit study list should have a unit 3 cell.
- Remove "Since Time Immemorial is not used" from whatever template seeds it.
- A check that every retrieval task named in a plan exists in days.csv (s02 day 15; s07 day 105 also names a ss4-choice-and-force retrieval absent from days.csv).
- A check that no withheld packet source is named on a teaching day or in a closing claim.
- Put the assessment minutes budget in the plan brief so it stops recurring.
- The skeleton printed "(no own-word line)" for codes in s04 that had own-word lines in s03 (D1.1, D2.His.10, D3.4, D2.His.16, D4.1); known, noted only.

## For Cory

None.

## What I could not judge

- The exact names on the Thomas Hunter manifest (image not read).
- Whether John A. Chesnut signed the 1865 memorial (committee listing found, signature not).
- Tennessee content (site refuses automated reading).
- Postwar deflation figures in unit 4 and crop examples in unit 1 (flagged by the plans themselves).
- Source images and leaflet scans the plans did not inspect.

## Sources

- Louisiana v. Callais, No. 24-109, decided 29 April 2026: https://www.supremecourt.gov/opinions/25pdf/24-109_21o3.pdf ; CRS summary https://www.everycrsreport.com/reports/LSB11431.html
- Dolores Huerta death, 28 October 2026: https://chicago.suntimes.com/obituaries/2026/10/28/dolores-huerta-influential-labor-leader-feminist-and-civil-rights-icon-dies-at-96
- Cesar Chavez allegations, March 2026: https://www.keranews.org/news/2026-03-18/allegations-emerge-against-cesar-chavez-marches-and-events-canceled
- Texas v. Kennedy (Section 504 rule): https://dredf.org/wp-content/uploads/2026/01/2026.01.28-Texas-v.-Kennedy-Joint-Statement.pdf ; https://lailluminator.com/2026/10/02/repub/disability-rights
- NPS, "Contagion of Liberty" chapter (Moore): https://www.nps.gov/articles/000/chapter-1-race-slavery-and-freedom-the-contagion-of-liberty.htm
- Jared Ross Hardesty, WWU: https://chss.wwu.edu/history/hardesj2
- NARA slave ship manifests (Thomas Hunter, M1895 roll 7): https://www.archives.gov/research/african-americans/slave-ship-manifests.html
- NPS Lowell letters (Averill; An Operative): https://www.nps.gov/articles/000/lyddie-chapter-12-i-will-not-be-a-slave.htm
- Apess, Indian Nullification (1835): https://www.gutenberg.org/cache/epub/12486/pg12486-images.html
- 1865 South Carolina Colored People's Convention: https://coloredconventions.org/items/show/570
- MA.5.T5.8 and T5.9 wording: data/standards/ma-hss-2018.txt

## Confidence

High on 1.1, 6.1, 9.1, CW1 to CW3 (read directly from the files). High on the web-checked facts above. Medium on 9.2 and 10.1 (variety judgments under the settled rule, not a standards failure). Medium on 8.2 (identity of the 1865 and 1868 Chesnut is inferred from name and district).

## For the source list

- NARA M1895 (coastwise manifests, New Orleans) as the citation form for internal slave trade records.
- Apess, Indian Nullification (Gutenberg 12486) for the Mashpee resolutions (21 May 1833) and notice (25 June 1833).
- Colored Conventions Project for Reconstruction-era Black political organizing.
