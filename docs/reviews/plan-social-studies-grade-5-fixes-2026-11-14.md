# Grade 5 social studies unit plans: fixes, 2026-11-14

Inputs: the expert read (docs/reviews/plan-social-studies-grade-5-2026-11-14.md) and the Codex read (docs/reviews/plan-social-studies-grade-5-codex-2026-11-14.md). The expert's "For the fixer" list was worked in order first. Every Codex finding the expert did not cover was applied after that.

Gate: `python -X utf8 scripts/unitplan.py check social-studies-grade-5` passes all ten units. `python -X utf8 scripts/sequence.py check social-studies-grade-5` gives 0 failures. Capped word counts run from 1,232 to 1,249 of 1,250. The course still has 160 days, and every unit keeps its day total.

## Applied

### Across units

- **CW1, assessment minutes.** Every end-of-unit item now carries its own minutes, using the settled budget (about 1 minute per locate item, 2 per one-sentence explanation, 4 to 5 per constructed map, 8 per paragraph claim). Instances were cut, never parts of a code.
  - s01 Q1 to Q6 total 33 of 34.
  - s02 totals 35, including 3 minutes of reading.
  - s03 totals 35. The unit claim is now its own item, Q8, at 8 minutes.
  - s04 totals 35, and its packet is capped at 400 words.
  - s05 is split across two sittings (see below).
  - s06 totals 40. It now asks for one Adams development, two camps and one route segment.
  - s07: Q1 gets 12 minutes for five one-sentence items, and the total is 40.
  - s08: Q4 is split into a, b and c (2, 3 and 2 minutes).
  - s09: Q1 has 8 minutes, Q4 has 6 and Q6 has 9; the total is 40.
- **CW2.** "Since Time Immemorial is not used." is deleted in s01 to s08.
- **CW3.** Every Tennessee row in s01 to s10 now reads "Not yet compared; the 2024 standards PDF on tn.gov refuses automated reading."
- **CW4.** The s05 hook now uses Banneker's letter to Jefferson of 19 August 1791 (Founders Online), with a source row added. Hall stays in units 2 to 4 and on days 62, 67 and 72.
- **CW5.** s01 field 10 now reads "Jared Ross Hardesty on colonial New England slavery (Unfreedom, 2016)". Berry in s02 is also named by her work.
- **Stale handoffs (Codex structure item 4).** s03 to s08 now name the next unit's plan and its first day. Each still states that daily Tomorrow lines do not exist.

### s01

- **1.1.** Field 4 now reads "**Start-of-year check:** none needed; retrieval only." followed by the days.csv sentence. The retrieval rows for day 1 and day 10 are kept.
- **1.2 and Codex F1.**
  - Q2 reads "Check one finding about the founder you researched against that card".
  - Founder cards 6 (Penn), 7 (Williams) and 8 (Winthrop) were added, each with a corroborating and a complicating detail.
  - X8 now reads "two short sources about your chosen founder". Founder cards are added to Still to make.
- **1.3.** Source cards are numbered 1 to 5, labour symbols became words, letters are kept for errors only, and exits are renamed X1 to X12.
- **1.4.** Card 4 cites the 1629 Massachusetts Bay charter (Avalon) and the Rhode Island charter's assembly clause, not the standards.
- **1.5.** X12 is a map label only, and the claim is collected as day 12 evidence.
- **1.6.** The Underhill warning was added to X4.
- **1.7.** Metacom is named in Q1 and X5.

### s02

- **2.1.** Georgia barred slavery from 1735 until 1751. Days.csv day 18 and the frame were synced to match.
- **2.2 and Codex F4.** Q5's sample is now the Charleston tailor Thomas Fell's 1770 notice (South-Carolina Gazette and Country Journal, 9 October 1770), replacing the 1795 payroll.
- **2.3.** Q3 is narrowed to B plus panel M8 (family and petitioning).
- **2.4.** The Venture Smith link now points to Documenting the American South.
- **2.5.** The day 15 days.csv note now names the ss4-choice-and-force retrieval task.
- **Codex F2.** Field 5 holds full renderings of A (adapted from Equiano, chapter 2) and B (adapted from the 1777 petition). Panels M1 to M8 are written out and labelled as Curio Class originals.
- **Codex F3.** The day 18 goal in days.csv reads "Slavery legal in all thirteen colonies in the late colonial period (Georgia from 1751), and ownership widespread but uneven, many early leaders among them". The frame cell was synced.

### s03

- **3.1.** A sensitivity study paragraph was added. It names the Delaware Nation, Delaware Tribe of Indians, Shawnee Tribe, Absentee Shawnee Tribe, Eastern Shawnee Tribe, Seneca Nation, Oneida Indian Nation and Little Traverse Bay Bands of Odawa Indians, then Kachun's First Martyr of Liberty (2017). The frame's unit 3 Sensitive cell gained one sentence.
- **3.2.** The day 34 note in days.csv and the frame now read "a trial witness's testimony", and the day list was synced.
- **3.3.** The closing claim adds George Hewes's Tea Party recollection (published 1834, decades later), with a source row.
- Pontiac's War (1763) was added to the teacher explanation.

### s04

- **4.1.** The Saint Regis Mohawk Tribe culture and history page was added for day 50, and packet P now draws on the Oneida and Mohawk histories.
- **4.2.** The frame's unit 4 Sensitive cell now reads "follow the readiness check on grade 3's money (day 43)".
- **4.3.** A teacher note was added on the Declaration's slur: described, not printed.
- **Codex F5.** E51 now uses two fresh profiles and asks how their contributions differed.

### s05

- **5.1.** The text now reads "Native nations govern themselves as sovereign nations within the United States today."
- **5.2.** Heller was removed from Limits. A teacher background line was added: "District of Columbia v. Heller (2008) held the Second Amendment protects an individual right; checked 2026-11-14." The source row is marked teacher background only.
- **Codex F6.**
  - Q1 asks what responsibility Article VI places on officeholders, and the key gives the oath or affirmation.
  - The day 63 exit now asks what the President's oath (Article II) requires, and the teacher explanation names it.
  - The scoring and look-for lines include the responsibility.
- **Codex F7.** Q6 is now Article V's thresholds plus a ten-case Bill of Rights chart with a key, covering the Ninth and Tenth Amendments accurately. The cases are made up and labelled as such.
- **Codex F8.** The assessment is split, and the unit keeps its 16 days.
  - **Day 72** stays Application. It adds the timeline in its last ten minutes and D2.His.1.3-5, and that exit row moved from day 73 to day 72.
  - **Day 73** becomes Check, assess = end, part 1 (Q1 to Q4).
  - **Day 74** is Check, part 2 (Q5 to Q7).
  - **Day 76's note** now reads "assessed on days 73 and 74".
  - **Header kinds** now read: understanding 10, application 3, check 2, respond 1.
  - **Field 7:** each sitting has 2 minutes of directions, 35 of work and 3 of collection. Day 75 has 5 minutes of feedback, 5 of checking and 30 of response.
  - Error H now points to day 72. The day list was synced to days.csv.

### s06

- **6.1.** A daily evidence table was added in field 5: one exit for each teaching day 80 to 94, each linked to its Q item and error letter.
- **6.2.** The teacher explanation and the Q2 key now say "The Lemhi Shoshone and the Hidatsa of the MHA Nation tell different accounts of Sacagawea's origin; we teach both and do not score her nation." Field 10 adds the NPS "Mandan, Hidatsa and Arikara histories of Sacagawea" page and the Sacajawea Center (Salmon, Idaho, in Lemhi Shoshone homeland).
- **6.3.** The cotton gin is now attributed to "California 8.7.1, grade 8" in the frame, days.csv day 93 and the s06 skeleton lines. The "Lead: correct..." sentence was removed.
- **CW1 (day 95).**
  - Items are resized to 40 minutes, and each item and source is read aloud inside that item's minutes.
  - Marking time is now named on day 96: five minutes of feedback, five of marking and 30 of repair.
- **Codex F9.** Error C now reads "Latitude measures how far east or west a place lies", and the correction distinguishes latitude from longitude.

### s07

- **7.1.** Field 10 adds the Muscogee (Creek) Nation, Choctaw Nation of Oklahoma, Chickasaw Nation, Seminole Nation of Oklahoma, Seminole Tribe of Florida, Eastern Band of Cherokee Indians, United Keetoowah Band and Shawnee Tribe pages.
- **7.2.** The citation now reads "the manifest of the schooner Thomas Hunter, Norfolk to New Orleans, October to November 1835 (NARA M1895, roll 7)", with an instruction to read the names from the image.
- **7.3.** The Cherokee Freedmen line was added to the teacher explanation.
- **Codex F10.**
  - Q3 opens with the Codex wording and traces state by state from dated captions: Vermont 1777, Pennsylvania 1780, Massachusetts and New Hampshire 1783, Rhode Island and Connecticut 1784, New York 1799, New Jersey 1804. Each first measure is kept apart from final freedom.
  - The packet captions, key and sample were rewritten.
  - The day 105 exit now retrieves Pennsylvania and Massachusetts from unit 2.
  - NPS "Northern Unfreedom" was added to field 10.

### s08

- **8.1.** The student copy of H is printed "Written by Curio Class for this task".
- **8.2.** The card now reads "John A. Chesnut of Kershaw District served at the 1865 South Carolina Colored People's Convention".
- **8.3.** Day 126 reads: marking, five minutes; feedback, five; repair and retries, 30. Total 40.
- **8.4.** The study list adds the Colored Conventions Project, Thavolia Glymph's Out of the House of Bondage (2008) and Kidada E. Williams's I Saw Death Coming (2023).

### s09

- **9.1.**
  - The closing claim now uses Brown, the 1965 Act and the disability-law overview.
  - Day 136 is taught from Shirley Chisholm's "Equal Rights for Women" (21 May 1969).
  - The 1966 statement is marked as withheld for day 141.
- **9.2.** E's context now names who 1920 left out: Native citizenship came in 1924, and state bars on Native voting lasted until 1948 or later. Most Asian immigrants could not become citizens until 1952. An NCAI Native voting page was added for day 132.
- **9.3.** A Callais line was added, starting "As of November 2026".
- **9.4.** A Section 504 line was added, starting "As of November 2026"; the case's final outcome is stated as unconfirmed.
- **9.5.** The Klan source is now the Senate Historical Office's "The Enforcement Acts of 1870 and 1871" (see below).

### s10

- **10.1.** Two topic sets were added, each with three works and a documented opposing view.
  - **19th Amendment:** National Archives text; NPS on Black women and the 19th; NPS ratification by state. The opposing view is NPS "Anti-Suffragism in the United States".
  - **Delano grape strike and boycott:** the NPS "Workers United" history; the union's history page; the UC San Diego farmworker documentation project. The opposing view is the growers' refusal to negotiate, as documented in the NPS history.
- **10.2.** The Callais line is completed, starting "As of November 2026".
- **10.3.** Teaching Hard History is replaced by the SNCC Digital Gateway, and the 403 note is removed.
- **Codex F11.** The day 149 exit now uses the Codex wording, and the full grid stays P4 evidence.

## Not applied

- **1.8, the regional crops check.** This is a process step: verify against the NPS and Colonial Williamsburg pages before section writing. I found only secondary study sites, so the "from memory" flag stays in s01 field 10.
- **4.4, the postwar deflation facts.** This is a process step before section writing and was not verified here.
- **5.3, the slavery-teaching framework.** This is a process step for the sensitivity agent. The s05 note that it remains unread stays.
- **Codex F6 and F10, the shared-file parts.** Correcting the MA.5.T3.1 and MA.5.T5.1 paraphrases, and the progression wording, in data/standards and data/progressions is not mine. They are listed under the structure pass. The plans carry the missing parts in field 5 and the teacher explanations.
- **Codex F8, the scope-and-sequence update.** This is a shared file and is listed under the structure pass.

## Where the reads disagreed, and what I followed

- **s01 field 4 label.** The expert wrote "**Retrieval only:** none needed...". I used "**Start-of-year check:** none needed; retrieval only.", following the brief's lead rule. Both pass the gate.
- **s02 Q5.** Codex only rewrote the 1795 sample's wording, while the expert asked for a colonial example. I followed the expert, using the verified 1770 Fell notice in place of the expert's Philipsburg or Royall suggestions.
- **Georgia (2.1).** The expert's "by 1755 it was legal in every colony" is not supported. Georgia legalized slavery from 1 January 1751 (New Georgia Encyclopedia), so the text says 1751.
- **Who 1920 left out (9.2, and the settled table).** The expert's "Asian immigrant women could not become citizens until 1952" is too broad. Chinese immigrants could naturalize from 1943, and Filipino and Indian immigrants from 1946; the 1952 Act ended the remaining racial bars. The text says "most Asian immigrants could not become citizens until 1952".
- **Callais (9.3, 10.2).** I did not use the expert's "narrowed how Section 2 applies to maps". The text follows the slip opinion syllabus: the Act did not require the second district, that district was an unconstitutional racial gerrymander, and Section 2 still stands, read more narrowly.
- **The Klan source (9.5).** The expert asked for an NPS or NMAAHC page, but no NPS page on this topic was found and NMAAHC refuses automated reading. I used the Senate Historical Office page, which is also a federal source.
- **s06 day 95 (CW1).** The expert wanted marking time named. Day 95 stays 40 minutes unaided, because the unit's parts need the full time at the settled budget, and marking is named on day 96. s07 and s09 follow the same pattern.

## Unverified

- **Texas v. Kennedy.** Its final status is unconfirmed. A September 2026 joint motion for final judgment exists, but I could not confirm whether judgment was entered. The s09 line says "outcome unconfirmed".
- **s01 founder cards.** The Penn card's office clause detail, the Frame of Government and the Laws Agreed Upon in England, is from memory.
- **Saint Regis Mohawk page (s04).** It exists, but its Revolution content was not read in full.
- **Thomas Hunter manifest (s07).** The citation comes from the expert read and was not opened here, and the names must be read from the image.
- **Nation pages added in s07.** They were linked after a response check only, not read.
  - The Eastern Band of Cherokee Indians site (ebci.com) did not answer from here.
  - The Choctaw Nation link is its home page because the history page refused automated reading.
- **Lemhi Shoshone account (s06).** No Lemhi Shoshone tribal government page was found. The Sacajawea Center is a community center in the Lemhi homeland, not a tribal government. The sensitivity agent should confirm the source, or name a Lemhi Shoshone or Shoshone-Bannock page.
- **Northern abolition (s07).** Connecticut's final date (1848) and New Jersey's remaining bondage in 1860 are from memory. NPS "Northern Unfreedom" confirms only the first-law dates.
- **Native voting (s09).** The 1948 Arizona and New Mexico dates and the 1957 Utah date rest on secondary and news sources. The NCAI page was not read in full.
- **New s09 and s10 sources.** The Chisholm speech page, the union history, the UC San Diego project, the NPS ratification-by-state page and the anti-suffragism page were checked as live, not read in full. The anti-suffragism content is from search excerpts.
- **Great Falls (s06 day 85 exit).** "About 47 degrees north, 111 degrees west" is from memory.
- **Regional crops (s01) and postwar deflation (s04).** Both are as above.

## For the structure pass

- **Shared standards and progression wording.**
  - Restore the full requirements of MA.5.T3.1 ("rights and responsibilities") and MA.5.T5.1 ("state by state") in data/standards and data/progressions/social-studies.csv.
  - Regenerate the skeleton fields afterwards.
  - Correct the MA.5.T1.7c line that groups Hall with freedom suits, and check MA.5.T1.5's paraphrase against the day 18 wording.
- **scope-and-sequence.md.**
  - Show unit 5 as two Check days (73 and 74), with the timeline on day 72.
  - Sync the day 18 goal (Georgia from 1751) and day 34 ("a trial witness's testimony").
  - Change the day 93 cotton gin to California 8.7.1 (grade 8).
- **Template.** Remove "Since Time Immemorial is not used" from whatever template seeds it.
- **Skeleton and brief.**
  - Require field 5's daily evidence table in every unit.
  - Put the assessment minutes budget into the plan brief.
  - Require a sensitivity study paragraph, with each nation's own source, in every unit, plus a frame cell per unit.
- **Retrieval check.** Check that every retrieval task named in a plan exists in days.csv. s07 day 105 names a ss4-choice-and-force retrieval and Pennsylvania and Massachusetts retrieval that days.csv does not carry.
- **Withheld packets.** Add a check that no withheld packet source is named on a teaching day or in a closing claim, plus the Codex packet manifest (source, locator, rendering, word count, use, rights).
- **Tennessee.** Fetch the February 2024 crosswalk named in the Codex read by hand, then fill the Tennessee rows.
- **Placeholders.** Section placeholders (one section per unit) and "candidate 151-day route" wording, per Codex structure items 5 and 6.
- **Skeleton own-word lines.** The skeleton prints "(no own-word line)" for codes that have own-word lines in other units (expert note).

## For Cory

None.
