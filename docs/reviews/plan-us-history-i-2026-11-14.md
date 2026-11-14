# Plan read: US History I, units 1 to 9 (2026-11-14)

Expert cold read of docs/courses/us-history-i/s01.md to s09.md. Codex wrote them today from unit_skeleton.py skeletons. Done to docs/pipeline/briefs/plan-read.md, unit by unit, with the course-wide questions from the lead's brief.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/plan-read.md, docs/agents/lenses/social-studies.md and docs/GLOSSARY.md.
- docs/courses/us-history-i/frame.md and scope-and-sequence.md; data/plans/us-history-i/days.csv and source-map.csv; data/progressions/social-studies.csv (the rows the course cites); data/standards/ma-hss-2018.txt (the USI and NML rows).
- The social studies part of docs/ADOPTION-BAR-SUBJECTS.md (items 1 to 14, with core C12 to C16) and docs/courses/social-studies/STANDARD.md.
- s01.md to s09.md in full, and Codex's write notes for each unit (docs/reviews/codex-write-us-history-i-s0N-2026-11-14.md).
- The "Settled by the expert" tables in plan-social-studies-grade-3-2026-11-14.md, plan-social-studies-grade-4-2026-11-14.md and plan-us-government-and-politics-2026-11-14.md, applied here and not re-argued.
- Gate: `python -X utf8 scripts/plan.py check` passes the course: 9 units, 160 days (148 in units, 12 for course-level checks and respond days), 0 failures. Exit 255 was the PowerShell stderr artifact.
- Web checks this run, listed under Sources at the end.

Severity follows cost. **Serious** means a student is taught or assessed wrongly, or a sensitivity failure reaches a classroom. **Moderate** means the plan cannot be run as written, a standard part is weakly evidenced, or a fact is stale. **Minor** means wording, a missing teacher note or a data tidy. LAYER says where the fault lives. REPEAT is yes when an earlier read found the same kind.

## Course verdict

The nine plans are serious, well sourced work: every goal has an item, unseen sources are reserved for every assessment, invented teaching texts are labelled as invented, and slavery, removal, Reconstruction terror, exclusion, lynching and empire are taught plainly and without role play. Since Time Immemorial is used as settled (days 25, 104 and 105, content kept, one credit line). The course is not yet to the bar for four reasons: one serious currency gap (unit 6 teaches birthright citizenship with no line on Trump v. Barbara, decided June 30, 2026); unit 1's readiness check still sits before day 1; most end-of-unit assessments ask for more parts than their minutes hold; and several facts and interpretations are stale (Fiske and Becker as "the experts", Dunning as a second interpretation, "more than 100" dead at Colfax, missing dated lines on McGirt, Callais and the Alien Enemies Act). All are fixable inside the existing days.

## Course-wide findings

### CW1. Assessments ask for more parts than their minutes hold (moderate; LAYER plan; REPEAT yes, grade 4 and US Government "assessments are sized to their minutes")

Units 1, 2, 4, 5, 7, 8 and 9 each have at least one item well past the settled rate (about 1 minute per locate or date item, 2 per one-sentence explanation, 8 per paragraph claim). Codex flagged the 40-minute loads itself. The fix in every unit is the same: cut instances, never parts, and move a closing synthesis that the unit already scored on an application day off the sitting. Exact cuts are given per unit.

### CW2. Copyrighted modern scholarship quoted into CC BY pages (moderate; LAYER plan; REPEAT new)

Units 4 and 5 (and unit 1's historiography line) plan to quote McPherson, Freehling, Foner, Lane, Blight and Baynton, all in copyright; Du Bois's *Black Reconstruction* (1935) has an uncertain renewal status. Bar item 14 forbids copying reference-only material. **Fix:** every modern historian appears as an attributed paraphrase in our own words ("Eric Foner argues that ..."), or is replaced by a public-domain or openly licensed interpretation (for example the National Park Service Reconstruction theme study by Downs and Masur, 2017, a federal work). Add one line to each affected field 10: "Modern historians are paraphrased with attribution, never quoted."

### CW3. Voice is often dense and nominalized (minor; LAYER plan; REPEAT yes)

Many lines read as stacked noun phrases ("Evaluate removal using Worcester, forced removal and continuing nationhood"; "Withdraw completed graphs on 115 and sentence prompts on 120"). A teacher reading quickly needs plain full sentences with a subject and a verb. **Fix:** at section-plan time, rewrite field 2 "Teaching" and "Carried" lines and field 7 response lines as full sentences. Not a blocker for the unit plans.

### CW4. Subject approach page absent (minor; LAYER process; REPEAT yes)

Every unit says "No subject approach page ... exists." For the structure pass, not the fixer.

## Unit 1: The road to revolution and independence (days 1 to 20)

**U1-1. Readiness check placed before day 1 (moderate; LAYER plan and data; REPEAT yes, lead rule 2026-11-14, US Government CW1).** Field 4 says "**Given:** the start-of-year check, before day 1" and "during the start-of-year check, no more than a few days before day 1", and its use-of-results places item 1's reteach on "day 1 after the hook". Unit 1 has four readiness rows, so the lead rule applies: the check is the last ten minutes of day 1, after the hook, with reteach on day 2 or 3. *Why it matters:* a teacher cannot give a check on a day that does not exist. *Fix:* field 4 lines 80 and 81 (new text in "For the fixer" 1). Day 1's exit ticket moves to the five minutes before the check. Items 1 to 3 are retaught on days 2 and 3. Item 4 (significance, wh1-renaissance) stays retaught on day 14, before day 16 uses it. The same wording in days.csv (days 1, 4 and 16 notes) and scope-and-sequence.md (lines 9 and 33) changes with it. The skeleton's own "before day 1" wording is known and being fixed in the script.

**U1-2. Assessment overload (moderate; LAYER plan; REPEAT yes).** Task 3 asks for four British policies, each from three viewpoints, in 7 minutes (twelve explanations, about 24 minutes at the settled rate). The D3.1 source item stacked onto Task 7's 8 minutes also leaves the paragraph claim short. *Fix:* Task 3 keeps all three viewpoints but on two policies: the Proclamation of 1763 and one Act of the student's choice. Move the D3.1 item to its own 3 minutes, taken from the cut in Task 3.

**U1-3. The hook and day 1 exit use Massachusetts only (moderate; LAYER plan; REPEAT yes, grade 3 settlement "own place").** The hook and E1 rest on the 1641 Massachusetts Body of Liberties, provisions 68 (deputies) and 74 (town selectmen); both verified. Bar item 13: no state's own history taught as if it were every student's. *Fix:* pair it with a second colony's assembly, the Virginia House of Burgesses or Pennsylvania's 1701 Charter of Privileges, and let E1 use either.

**U1-4. Dated historiography presented as "the experts" (moderate; LAYER plan; REPEAT new).** Day 16 to 18 material gives John Fiske (1891) and Carl Becker (1918) as the experts on whether the Revolution was radical. Both are early; Fiske's Anglo-Saxon framing is now rejected. *Fix:* add a teacher background line, in our own words: "Fiske and Becker are early historians. Since the 1990s historians such as Gordon Wood, Gary Nash and Alan Taylor have argued over how radical the Revolution was and for whom; Fiske's racial framing is rejected." Students may still read Fiske and Becker as historiography (public domain), labelled as early.

**U1-5. Petition quote from a modernized transcription (minor; LAYER plan; REPEAT new).** The 1777 Prince Hall petition is quoted as "natural & inalienable right", which is the National Constitution Center's modernized text; the original reads "Unaliable". *Fix:* use the original spelling, or add "(spelling modernized)" after the quote.

**U1-6. "Odawa" without a nation (minor; LAYER plan; REPEAT yes, "Native nations varied").** Several Odawa nations exist today (for example the Little Traverse Bay Bands of Odawa Indians and the Little River Band of Ottawa Indians in Michigan). *Fix:* name the nation whose sources the day uses, in the present tense.

Correct as written: Saratoga 1777, the French alliance 1778, Crispus Attucks, Phillis Wheatley, and Cornplanter's 1790 address.

## Unit 2: A new nation (days 21 to 34)

**U2-1. Task 5 overload (moderate; LAYER plan; REPEAT yes).** Task 5 asks for about nine presidential policies, two consequences each, plus the first parties, in 10 minutes. *Fix:* one policy per president (Washington, Adams, Jefferson), each with both its domestic and foreign effect, plus the parties: about 8 minutes.

**U2-2. Alien Enemies Act: no dated line (moderate; LAYER plan; REPEAT yes, "dated teacher background lines").** Day 30 teaches the Alien and Sedition Acts as history. The Alien Enemies Act of 1798 is the one still in force: it was used against German nationals in 1917 and 1918 (unit 9's home front) and invoked in March 2025. The Fifth Circuit en banc dismissed W.M.M. v. Trump as moot on August 13, 2026, leaving the peacetime question undecided. *Fix:* field 10, add: "Checked 2026-11-14: of the 1798 acts, the Alien Enemies Act is still law. It was used in both world wars and invoked in March 2025; the Supreme Court required notice and a chance to go to court (2025), and the main appeal ended as moot in August 2026 without deciding whether the Act applies in peacetime. Taught as fact, not argued by party; no student is asked about status."

**U2-3. Task 4 needs sources students cannot hold (minor; LAYER plan; REPEAT new).** Task 4 asks for "two of its sources" from the student's chosen pathway, with no notes allowed. *Fix:* reprint short excerpts of both pathways' sources on the sitting page.

**U2-4. Northwest Ordinance without Native nations (minor; LAYER plan; REPEAT yes, "Native nations varied").** *Fix:* add a teacher line that the territory was the homelands of nations including the Shawnee, Miami, Delaware (Lenape) and Potawatomi, and that article 3 promised "the utmost good faith" toward them, a promise broken within a decade (Fallen Timbers 1794, Greenville 1795).

**U2-5. NML.T2.1 could use a dated line (minor; LAYER plan; REPEAT yes).** *Fix:* one teacher line on how platforms and AI-generated text change how news reaches readers, dated 2026-11-14.

Correct as written: ratification votes (Massachusetts 187 to 168, Virginia 89 to 79, New York 30 to 27), the Freedom's Journal quote, and the Since Time Immemorial day 25 credit line.

## Unit 3: Democracy and removal (days 35 to 50)

**U3-1. McGirt without its sequels (moderate; LAYER plan; REPEAT yes, "dated teacher background lines").** The unit names McGirt v. Oklahoma (2020) in the present tense but nothing after it. *Fix:* field 10, add: "Checked 2026-11-14: Oklahoma v. Castro-Huerta (2022) let states prosecute non-Indians for crimes against Indians in Indian country. In City of Tulsa v. O'Brien (December 2024) Oklahoma's criminal appeals court let cities ticket tribal citizens, against the Tenth Circuit's Hooper ruling; in June 2025 Tulsa settled with the Muscogee (Creek) Nation, accepting tribal jurisdiction in its municipal cases. The reservation itself stands." One teacher sentence in class, as settled for Castro-Huerta in US Government.

**U3-2. "Became US residents" understates the treaty (minor; LAYER frame and data; REPEAT new).** The frame and days.csv day 43 say Mexican citizens "became US residents". Under the Treaty of Guadalupe Hidalgo, articles VIII and IX, those who stayed became US citizens unless they chose to keep Mexican citizenship within a year; their rights, especially land titles, were unequally honored. *Fix:* frame.md and days.csv day 43: "who became US residents" to "who became US citizens under the treaty, with rights unequally honored".

Correct as written: assessment minutes (16 + 14 + 10 = 40), the Reynolds and Mitchell maps, and the Van Buren distinction for the Cherokee removal.

## Unit 4: Reform, industry and slavery (days 51 to 71)

**U4-1. Assessment overload (moderate; LAYER plan; REPEAT yes).** Items run 4, 10, 8, 4, 9 and 5 minutes. Item 5 asks for all five reform strands, with 5e alone covering three writers and six themes, in 9 minutes; item 2 has six prompts in 10. *Fix:* item 5 becomes one short survey prompt per strand (five sentences, 10 minutes) with the researched strand already scored on its product day; item 2 cuts to four prompts.

**U4-2. MA.USI.T4.2 parsed as five required parts (moderate; LAYER skeleton and data; REPEAT new).** T4.2 says "research one ... from the list below", so a to e are choices. The skeleton made them parts, and the plan assesses all five in depth. *Fix:* one deep research strand (the student's choice, scored on its product day) and one survey sentence per other strand. Report the parsing to the structure pass; the same pattern appears in T7.5 (unit 9) and T7.2 and T6.3 (unit 8).

**U4-3. Records that read as real sources (moderate; LAYER plan; REPEAT yes, "exact citations", "nothing invented passed off as real").** The plan uses "anonymous financial records", teacher-made "loan and insurance entries" and a "machinery order and shipping entry" to show Northern ties to slavery. Unlabelled, students will take them as documents. *Fix:* use real public records with citations (for example the California Department of Insurance Slavery Era Insurance Registry), or label each one "Made for practice by Curio Class, based on [cited source]".

**U4-4. Reform paper has no length (moderate; judgment call; LAYER plan; REPEAT new).** The "several-page" paper gets only days 66, 67 and 69 of history time. *Fix:* "about 1,000 words", matching unit 9's 800 to 1,000, so schools without ELA 11 can finish it.

**U4-5. Douglass passage described wrongly (minor; LAYER plan; REPEAT new).** Chapter XI's passage is one paragraph (checked on Project Gutenberg); "When I got through with that job" begins a sentence, not a paragraph, and the text reads "a plenty of work". *Fix:* describe the excerpt as "sentences omitted, marked with an ellipsis" and keep the original wording.

**U4-6. Period institution names (minor; LAYER plan; REPEAT new).** Names such as "feeble-minded" appear in period sources. *Fix:* a teacher note that these are period terms, now offensive, read once in the source and not reused, following the disability language guide.

Correct as written: Sojourner Truth from Marius Robinson's 1851 report, not Frances Gage's 1863 version.

## Unit 5: Sectional crisis, war and Reconstruction (days 72 to 96)

**U5-1. Drafts without feedback time (moderate; LAYER process and data; REPEAT new).** Scope and sequence promises "at least two school days" between drafts, but essay 1's drafts sit on days 81 and 82 and essay 2's on 91 and 92. Codex flagged this. *Fix (settled):* essay 1, swap inside the unit so day 82 is the Lost Cause, day 83 the war's consequences and day 84 the final draft. Essay 2: the two-day gap stays from draft 1 (88) to draft 2 (91); before the final on 92, overnight feedback on one criterion. Amend scope-and-sequence.md line 76 to match.

**U5-2. Assessment sizing (moderate; LAYER plan; REPEAT yes).** Item 2 asks for four causal links and a trigger in 4 minutes. *Fix:* cut instances elsewhere (two battles, not three, in item 4; fewer consequence boxes in item 6) and give item 2 8 minutes.

**U5-3. Colfax toll given as "more than 100" (moderate; LAYER plan; REPEAT new).** Estimates run from about 60 to about 150; recent work favors the low end (Lane, 2008: 62 to 81; a July 2026 Journal of the Civil War Era essay argues 62 to 80). Fifty-nine bodies were buried by state officials. *Fix:* R2 key and day 86: "at least 60 Black men were killed, and perhaps many more; historians' estimates range from about 60 to 150". State it as a range with its source.

**U5-4. Dunning as the second interpretation (moderate; LAYER plan; REPEAT new).** P2 sets Dunning School work beside a modern account as two interpretations to weigh, which gives a racist account equal standing (values rule b). *Fix:* the second interpretation is a modern account (the NPS Reconstruction theme study, public domain, or an attributed Foner paraphrase). Dunning stays only on day 87 as historiography: how sources and racism shaped an account later overturned.

**U5-5. Copyrighted historians (moderate; see CW2).**

Correct as written: James Henry Gooding's letter of September 28, 1863, the Hayes quote, and April 1877 for South Carolina and Louisiana.

## Unit 6: Citizenship, the West and Jim Crow (days 97 to 109)

**U6-1. Birthright citizenship taught without the 2026 ruling (serious; LAYER plan; REPEAT yes, "dated teacher background lines").** The unit teaches the 14th Amendment and United States v. Wong Kim Ark (1898) with no dated line. On June 30, 2026 the Supreme Court decided Trump v. Barbara (No. 25-365), 6 to 3, Chief Justice Roberts writing, holding the 2025 executive order limiting birthright citizenship unlawful, consistent with Wong Kim Ark. A student told only of 1898 is taught an incomplete current fact on a live question. *Fix:* field 10 and the day's teacher notes: "Checked 2026-11-14: in Trump v. Barbara (June 30, 2026) the Supreme Court, 6 to 3, held that the 2025 order limiting birthright citizenship was unlawful, keeping the rule of Wong Kim Ark. Stated as the law, under values rule (a); not argued by party; no student is asked about status."

**U6-2. Wounded Knee medals (moderate; LAYER plan; REPEAT yes).** *Fix:* day 103 teacher line: "Checked 2026-11-14: in September 2025 the Secretary of Defense announced that the Medals of Honor given for Wounded Knee would stand, after a 2024 review panel's recommendation. Lakota nations and others had asked that they be rescinded."

**U6-3. Boarding school reports (moderate; LAYER plan; REPEAT yes).** *Fix:* day 104 to 105 teacher line: "Volume II of the federal Boarding School Initiative report (July 2024) counted at least 973 children who died at federal Indian boarding schools, and says the true number is higher. The President apologized on behalf of the United States on October 25, 2024." The 973 figure is confirmed this run; confirm the apology date at production.

**U6-4. Black Hills award in the present tense (moderate; LAYER plan; REPEAT yes).** United States v. Sioux Nation (1980) is taught correctly but stops there. *Fix:* "The Lakota nations have refused the award, saying the Black Hills are not for sale; the money remains in a federal trust account, now worth more than $2 billion (confirm the figure at production)."

**U6-5. Huckleberry Finn chapter 31 (minor; LAYER plan; REPEAT new).** The chapter's letter scene contains the slur. *Fix:* excerpt only Huck's deliberation, ending before the slur, with a teacher note.

**U6-6. Unseen packet built from summaries (minor; LAYER plan; REPEAT new).** Several reserved cards are our summaries. Bar item 7 needs the original passages before shipping. *Fix:* field 5: "replace each summary with the original passage, cited".

**U6-7. Item 4 paragraph in 6 minutes (minor; LAYER plan; REPEAT yes).** Settled rate is 8. *Fix:* take 2 minutes from the item with the most date items.

Correct as written: Cumming (1899), Elk v. Wilkins (1884), Yick Wo (1886), Wong Kim Ark (1898), Minor v. Happersett (1875), the 1855 and 1870 naturalization acts, the Sioux Nation ruling (about one-tenth of adult men signed in 1876), and Howard's charter of March 2, 1867.

## Unit 7: Industry and newcomers (days 110 to 122)

**U7-1. Item 3 overload, with a closing transfer that repeats day 120 (moderate; LAYER plan; REPEAT yes).** Item 3 asks for seven rows (source, motive, work), a railway paragraph and a recruiter comparison in 18 minutes, about 24 minutes of work. The 5-minute "closing transfer" asks for a paragraph claim with counterclaim and limit (settled 8), and the closing claim was already written on day 120. *Fix:* drop the closing transfer from day 121 (keep its prompt as a day 122 transfer task) and give item 3 23 minutes. Totals stay at 45.

**U7-2. Exits ask too much for three minutes (minor; LAYER plan; REPEAT yes).** E116 (four groups, motive and job each), E117 (three groups), E114 (three parts) and E142-style lists. *Fix:* E116 two groups chosen by the student; E117 two of three; E114 asks why workers organized and the Triangle link only.

**U7-3. Lee Chew's chapter title carries a slur (minor; LAYER plan; REPEAT new).** In Holt's 1906 collection the chapter is titled with a term now a slur. The frame says slurs are not printed. *Fix:* field 5 and 10: cite it as "Lee Chew's life story, in Holt (1906)", and add a teacher note that the original title uses a slur and is not printed or read aloud.

**U7-4. Immigration status not named in the safety note (minor; LAYER plan; REPEAT new).** With 2025 to 2026 enforcement in the news, students in mixed-status families need the rule stated. *Fix:* family note and field 10 teacher note: "No student is asked about their own or their family's immigration status or story, in class or on any page."

Correct as written: the Edison lamp patent 223,898 (1880), Sherman sections 1 and 2 split between teaching and assessment, the 1894 Strike Commission report, Allen and Korean recruitment to Hawaii, the 1943 exclusion repeal, and the care not to invent railroad work for the Korean narrator.

## Unit 8: The Progressive Era (days 123 to 139)

**U8-1. Item 6 carries the whole closing claim (moderate; LAYER plan; REPEAT yes).** In 11 minutes item 6 asks for a Washington and Du Bois comparison, Niagara, the NAACP, Wells, a judgment by 1920, migration and Red Summer, and then a paragraph answering the compelling question with counterclaim and limit. Item 4 likewise asks five occupations plus an organization's formation, aims and tactics in 7. *Fix:* item 6 keeps the comparison, one organization's tactics (student's choice of Niagara, NAACP or Wells) and the judgment (11 minutes); the compelling-question paragraph moves to day 139's first 8 minutes as the closing claim, which fits the response day's revision block. Item 4 asks for two occupations of the student's choice plus the organization.

**U8-2. Callais checked but not given to the teacher (moderate; LAYER plan; REPEAT yes, "dated teacher background lines").** Field 10 says the 2026 Callais opinion was checked, but day 132 ("who still could not vote after 1920") has no line. *Fix:* "Checked 2026-11-14: in Louisiana v. Callais (April 29, 2026) the Supreme Court, 6 to 3, held that Section 2 of the Voting Rights Act did not require Louisiana's second majority-Black district, narrowing how Section 2 can be used against district maps. Not projected backward onto 1920; stated as law, not argued by party."

**U8-3. "Fact-checking today" needs a dated line (minor; LAYER plan; REPEAT yes).** Day 125 compares Progressive investigation with fact-checking today. *Fix:* "Checked 2026-11-14: in 2025 some large platforms ended third-party fact-checking in the United States and moved to user-written notes; name the practice, not the company."

**U8-4. Pay stub read backward (minor; LAYER plan; REPEAT new).** E127's present-day pay stub with withholding could suggest 1913 workers paid that way. *Fix:* teacher line: "The 1913 income tax reached only a few percent of households; wage withholding began in 1943."

**U8-5. Native voter case in 1920 (minor; LAYER plan; REPEAT new).** P5's "Native woman without United States citizenship" is right for many, but by 1920 a large share of Native people were already citizens through allotment, military service or treaty. *Fix:* the case card dates her and names her nation, and the key adds "many Native people were citizens before 1924; the Indian Citizenship Act of 1924 covered the rest, and states still blocked voting".

**U8-6. One class-wide research topic where the standard says "choose" (minor; judgment call; LAYER plan; REPEAT yes, see U4-2).** T7.2 and T6.3 say research one policy and one organization, "choosing one of the listed topics". The plan fixes the 1906 law and the National Woman Suffrage Association for everyone. *Settled:* a teacher may choose one topic for the class; that meets "research one". Item 2 and item 4 wording says "your researched policy" and "your researched organization" so a teacher who lets students choose can reuse it.

Correct as written: Guinn v. United States (1915, and the plan rightly catches an outside page that says 1910), United States v. Johnson (1911), the 1938 act, the 1869 and 1876 suffrage dates, Wells's *A Red Record* (1895), Zitkala-Sa as Yankton Dakota, Roosevelt's 1913 eugenics letter handled by paraphrase, the 2022 Emmett Till Antilynching Act, and the informed action (student's choice, adult contact only, a reasoned choice not to act earns the same credit).

## Unit 9: Empire, news and the First World War (days 140 to 155)

**U9-1. Item E carries the closing claim in 7 minutes (moderate; LAYER plan; REPEAT yes).** E asks for the Fourteen Points, the League, failed ratification and then both halves of the compelling question with counterclaim and limit. *Fix:* E keeps the diplomacy (7 minutes); the two-halves answer moves to day 155's first 8 minutes, before the review, and is scored there as the unit's closing claim. D (five minutes, three sources, four elements) cuts to the 369th and one rights tension.

**U9-2. E142 asks five policies in three minutes (minor; LAYER plan; REPEAT yes).** *Fix:* two of the five, the student's choice; the survey key covers the rest.

**U9-3. Present-tense lines for the places named (minor; LAYER plan; REPEAT yes, "Native nations varied", dated lines).** *Fix:* field 10 teacher lines: "The Philippines has been independent since July 4, 1946. The United States still leases Guantanamo Bay under the 1903 agreement; the Platt Amendment was repealed in 1934. Puerto Ricans have been US citizens since the Jones Act of March 1917. In 1993 Congress apologized for the 1893 overthrow of the Hawaiian Kingdom (Public Law 103-150)."

**U9-4. Maine inquiries (minor; LAYER plan; REPEAT new).** Card C names the 1898 inquiry and Rickover (1976) but not the 1911 inquiry, which also found an external explosion. *Fix:* add "a second Navy inquiry in 1911 also proposed a mine; later studies disagree", so students see three findings, none naming a culprit.

**U9-5. Day 145 website work needs a dated line (minor; LAYER plan; REPEAT yes).** The lesson asks who is responsible for a federal site. *Fix:* "Checked 2026-11-14: in 2025 the Archivist of the United States was removed and an acting Archivist named, and several federal agencies edited or removed web pages. Print the About page on the day taught; a government domain shows who publishes, not that a page is complete."

**U9-6. Native and Puerto Rican service in 1917 to 1918 (minor; LAYER plan; REPEAT new).** Day 149 could connect unit 8's voter cases: thousands of Native men served while many were not citizens, and Choctaw soldiers sent coded messages in 1918. *Fix:* one survey line; no added day.

**U9-7. T7.5 parsed as eleven required parts (minor; LAYER skeleton; REPEAT yes, see U4-2).** Here the plan sized the eleven survey items to 22 minutes, so the sitting works. Keep, and report the parsing to the structure pass.

Correct as written: the August 1868 Alaska payment, Liliʻuokalani's 1898 protest, Cuba's 1906 to 1909 occupation, the Treaty of Paris articles I to III, Beveridge's Senate speech of January 9, 1900, the Anti-Imperialist League platform (1899), Schenck with Brandenburg in the teacher note, the 1917 and 1918 laws kept separate, the 369th, about 675,000 US influenza deaths, the clearly labelled invented 1898 news pair, the debate's 50 minutes, and the year-end hand-on to days 156 to 160.

## Course flow

Each unit picks up what the last promised. Unit 1 hands significance and lateral reading to units 2 and 9; unit 5's Reconstruction amendments open unit 6 and unit 8's readiness check (day 122); unit 7's Triangle fire opens unit 8 (day 124); unit 8's investigation feeds unit 9's news days (144 to 146). Readiness checks match scope and sequence (days 19, 34, 50, 71, 96 and 122). The only broken promise is the draft spacing in unit 5 (U5-1).

## Settled by the expert

| Question | Ruling | Where it binds |
|---|---|---|
| When is unit 1's readiness check given? | Lead rule 2026-11-14 applied: the last ten minutes of day 1, after the hook; day 1's exit moves to the five minutes before it; items 1 to 3 retaught on days 2 and 3, item 4 on day 14. | s01 field 4; days.csv days 1, 4, 16; scope-and-sequence.md lines 9 and 33 |
| Unit 5's draft spacing | Essay 1: day 82 Lost Cause, day 83 consequences, day 84 final draft (swap inside the unit). Essay 2: two days from draft 1 to draft 2; overnight one-criterion feedback before the final. | s05; days.csv days 82 to 84; scope-and-sequence.md line 76 |
| Closing claims inside a sitting | When the compelling-question paragraph does not fit the sitting's minutes, it moves to the first 8 minutes of the respond day, scored there. | s07 day 121 and 122, s08 day 138 and 139, s09 day 154 and 155 |
| "Research one ... from the list" standards (T4.2, T6.3, T7.2, T7.5) | One deep research topic (class or student choice) plus a survey sentence per other listed case; the listed cases are not all required parts. | s04, s08, s09; skeleton parsing to the structure pass |
| Interpretations that weighed racist accounts | Dunning, Fiske's racial framing and the Lost Cause appear only as historiography to be tested, never as one of two views to weigh. | s01, s05 |
| Death tolls and contested counts | Given as a range with its source, never a single number as data. | s05 Colfax; any later count |
| Modern historians | Attributed paraphrase only; no quotation into CC BY pages. | s01, s04, s05 |
| Exit size | An exit asks at most two instances in its three minutes; the student picks when there are more. | s07, s09 |
| 2025 to 2026 law and events | Settled earlier, applied: a dated teacher line, stated as fact, never argued by party (Barbara, Callais, Alien Enemies Act, McGirt sequels, Wounded Knee medals). | s02, s03, s06, s08, s09 field 10 |

## For the fixer

In order. "Old" is the exact current text where short.

1. s01 field 4, line 80. Old: "**Given:** the start-of-year check, before day 1 (served in unit 1, which defines it)." New: "**Given:** day 1, the last ten minutes, after the hook (lead rule 2026-11-14)."
2. s01 field 4, line 81. Old: "Give four short items in ten minutes during the start-of-year check, no more than a few days before day 1." New: "Give four short items in the last ten minutes of day 1, after the hook; day 1's exit ticket moves to the five minutes before the check." Old: "Day 1 begins with the hook, never with this check." New: "Items 1 to 3 are retaught on days 2 and 3; item 4 on day 14, before day 16 uses it." Change item 1's reteach from "day 1 after the hook" to "day 2".
3. s01 line 97 and days.csv days 4 and 16 notes: "opened at the start-of-year check" to "opened at day 1's readiness check".
4. days.csv day 1 note. Old: "unit 1's readiness check is served by the start-of-year check before this day:" New: "unit 1's readiness check in this day's last ten minutes, after the hook:".
5. scope-and-sequence.md line 9. Old: "and for unit 1 in the start-of-year check" New: "and for unit 1 in the last ten minutes of day 1, after the hook". Line 33. Old: "Readiness: the start-of-year check, before day 1," New: "Readiness: the last ten minutes of day 1, after the hook,".
6. s06 field 10 and day 98 to 99 teacher notes: add the Trump v. Barbara line (U6-1).
7. s01: U1-2 (Task 3 to two policies; D3.1 own 3 minutes), U1-3 (second colony in the hook and E1), U1-4 (historiography line), U1-5 ("Unaliable" or "spelling modernized"), U1-6 (name the Odawa nation).
8. s02: U2-1 (Task 5), U2-2 (Alien Enemies Act line), U2-3 (reprint pathway excerpts), U2-4 (Northwest Ordinance line), U2-5 (dated news line).
9. s03: U3-1 (McGirt sequels line). frame.md and days.csv day 43: "who became US residents" to "who became US citizens under the treaty, with rights unequally honored" (U3-2).
10. s04: U4-1 (item 5 to one prompt per strand; item 2 to four prompts), U4-2 (T4.2 as one deep strand), U4-3 (real records or "Made for practice" labels), U4-4 ("about 1,000 words"), U4-5 (Douglass description), U4-6 (period terms note).
11. s05: U5-1 (days.csv rows 82 to 84 swapped: 82 Lost Cause, 83 consequences, 84 essay 1 final; move the retrieval note from 84 to 83; s05 fields to match; scope-and-sequence.md line 76: "Written feedback is returned between every draft, with at least two school days to write it" to "Written feedback is returned between every draft: at least two school days before each second draft, and overnight feedback on one criterion before essay 2's final"), U5-2 (item 2 to 8 minutes, cuts in items 4 and 6), U5-3 (Colfax range), U5-4 (modern second interpretation; Dunning to day 87 historiography), CW2 line in field 10.
12. s06: U6-2, U6-3, U6-4 dated lines; U6-5 (chapter 31 excerpt); U6-6 (originals for summaries); U6-7 (item 4 to 8 minutes).
13. s07: U7-1 (drop closing transfer from 121, item 3 to 23 minutes, transfer to day 122), U7-2 (exit sizes), U7-3 (Lee Chew citation and note), U7-4 (status line).
14. s08: U8-1 (item 6 and item 4 cuts; closing paragraph to day 139's first 8 minutes, shrink day 139's revising block by 8), U8-2 (Callais line), U8-3, U8-4, U8-5 lines, U8-6 ("your researched" wording).
15. s09: U9-1 (E and D cuts; two-halves answer to day 155's first 8 minutes, shrink its review block), U9-2, U9-3, U9-4, U9-5, U9-6.
16. CW3 voice: at section-plan time, not now.

## For the structure pass

- unit_skeleton.py parses "research one ... from the list" standards (MA.USI.T4.2, T6.3, T7.2, T7.5) into required parts. They are choices; the skeleton should mark them "choose one; survey the rest".
- The template has no field for dated teacher background lines, so each plan puts them in field 10 under different headings ("Currency checked", "Accuracy notes"). A fixed "Dated lines (checked YYYY-MM-DD)" sub-field would make them findable when they go stale.
- Scope and sequence states draft-spacing promises that days.csv does not check. A gate rule in plan.py (draft days at least two school days apart, or flagged) would have caught U5-1.
- The subject approach page for social studies is still absent (CW4).
- A rights ledger template for excerpts (public domain, CC BY, reference only) would carry CW2 into production.

## For Cory

None. Every finding is inside existing days, scope and standards.

## For the source list

New sources used this run, for data/sources if kept: the Journal of the Civil War Era essay on the Colfax toll (2026), the Federal Indian Boarding School Initiative Volume II (2024), and the Trump v. Barbara and Louisiana v. Callais opinions (2026).

## Sources (web checks, November 14, 2026)

- Prince Hall petition, National Constitution Center transcription: https://constitutioncenter.org/the-constitution/historic-document-library/detail/prince-hall-petition-to-the-massachusetts-legislature
- Massachusetts Body of Liberties (1641): https://history.hanover.edu/texts/masslib.html
- Douglass, *Narrative*, Project Gutenberg: https://www.gutenberg.org/cache/epub/23/pg23.txt
- Tulsa and Muscogee (Creek) Nation settlement, June 2025: https://newson6.com/story/685b6b63f58080e914c8c2de/city-of-tulsa-agrees-to-settle-lawsuit-filed-by-the-muscogee-creek-nation-affirming-tribal-jurisdiction-in-municipal-criminal-cases
- City of Tulsa v. O'Brien and municipal jurisdiction: https://www.hppr.org/hppr-news/2025-08-15/some-oklahoma-towns-still-ticket-tribal-citizens-in-violation-of-a-u-s-supreme-court-ruling
- Trump v. Barbara (June 30, 2026): https://constitutioncenter.org/blog/supreme-court-strikes-down-trumps-birthright-citizenship-executive-order-in-landmark-decision and https://www.faegredrinker.com/zh/insights/publications/2026/6/supreme-court-decides-trump-v-barbara
- Wounded Knee medals (September 2025): https://www.mprnews.org/story/2025/09/26/hegseth-says-wounded-knee-soldiers-will-keep-their-medals-of-honor and https://www.militarytimes.com/news/pentagon-congress/2025/09/26/hegseth-says-wounded-knee-soldiers-will-keep-their-medals-of-honor/
- Boarding School Initiative Volume II (July 2024): https://www.doi.gov/pressreleases/secretary-haaland-announces-major-milestones-federal-indian-boarding-school and https://sourcenm.com/2024/07/30/at-least-973-native-american-children-died-at-u-s-run-boarding-schools-between-1871-1969/
- Colfax toll: https://www.journalofthecivilwarera.org/2026/07/how-many-died-in-the-colfax-massacre/ and https://64parishes.org/?p=60369
- Louisiana v. Callais (April 29, 2026): https://www.faegredrinker.com/en/insights/publications/2026/4/supreme-court-decides-louisiana-v-callais and https://constitutioncenter.org/blog/the-supreme-courts-callais-decision-sets-new-framework-for-racial-gerrymandering
- Alien Enemies Act litigation, W.M.M. v. Trump dismissed as moot (August 13, 2026): https://www.aclu.org/cases/wmm-v-trump and https://www.stevevladeck.com/p/244-the-end-of-the-alien-enemies

Not re-checked this run, marked "confirm at production" above: the Black Hills trust figure and the date of the 2024 boarding school apology.
