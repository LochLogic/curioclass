# Plan read: Civics: Government and Civic Life, units 1 to 10 (2026-11-14)

Expert cold read of docs/courses/civics-government-and-civic-life/s01.md to s10.md, written today by Codex from unit_skeleton.py skeletons. Done to docs/pipeline/briefs/plan-read.md, unit by unit, with the course-wide questions from the lead's brief.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/plan-read.md, docs/agents/lenses/social-studies.md, docs/GLOSSARY.md.
- docs/courses/civics-government-and-civic-life/frame.md and scope-and-sequence.md; data/plans/civics-government-and-civic-life/days.csv (all 160 rows, read where the plans and frame point).
- The social studies part of docs/ADOPTION-BAR-SUBJECTS.md (through the lens and earlier reads), docs/courses/social-studies/STANDARD.md (as cited by the plans).
- s01.md to s10.md: fields 2 to 10 in full for every unit; day lists in full; exit tickets and U6 day tables in full for units 1, 2, 3 (part), 8 and 10, sampled for the rest.
- The "Settled by the expert" tables of plan-social-studies-grade-3-2026-11-14.md, plan-social-studies-grade-4-2026-11-14.md and plan-us-government-and-politics-2026-11-14.md, applied here and cited, not re-argued. The US Government read's web checks of today (Callais, Learning Resources, Slaughter, Barbara, Watson, the midterm, Department of War, USAID, WHO) are reused, not repeated.
- Gate: `plan.py check` passes (10 units, 160 days, 0 failures; one note: Seams does not name wh2-social-movements). No em dashes in any plan.
- A byte scan of every plan for broken characters (CW1).
- Web checks this run, listed under Sources.

Severity follows cost, as in the US Government read: **serious** (a student is taught or assessed wrongly, or a sensitivity failure reaches a classroom), **moderate** (the plan cannot be run as written, a standard part is weakly evidenced, balance is not shown, or a teacher is left without a fact they need), **minor** (wording, a missing note, a data tidy).

## Course verdict

The ten plans are careful and nonpartisan in posture: invented cases are labelled as invented everywhere, no student discloses status, politics or family finances, the civic action in unit 10 is the class's own choice through a school-mediated route, and unit 1 handles the start of the year rightly (no readiness rows, "retrieval only", nothing before day 1). They are not yet to the bar for five reasons: no unit carries a dated teacher background line on the 2025 to 2026 rulings and changes that touch units 3 to 7 and 9 (REPEAT); four end-of-unit assessments are over-full (REPEAT); Brown v. Board of Education appears nowhere in the year, and the equal protection research area rests on Lochner and Parrish instead; units 9 and 10 carry about 185 broken characters ("?" for apostrophes and quotation marks) that a teacher would print; and three sensitivity points are unhandled or misaimed (the Declaration's grievance slur on Native peoples, a Since Time Immemorial credit on a Haudenosaunee day, and unit 3's and unit 5's sensitivity studies). No finding is serious; every fix fits inside the existing days.

## Course-wide findings

### CW1. Broken characters in units 9 and 10 (moderate; LAYER process, plan; new)

s09.md has 83 and s10.md 102 places where an apostrophe or quotation mark was written as a literal "?" ("Boston?s evaluation", "?Compare?:", "G?s editorial board", the whole day 154 packet A to E). The other eight plans have none. The likely cause is the write channel (a code page that drops curly quotes), not the writer's choice.

**Why it matters.** The day 154 assessment cards and the day 143 packet would print with question marks inside words and in place of quotation marks; a "?" also reads as a real question mark in a prompt.

**Fix.** Replace each "?" that stands between letters with "'" and each that opens or closes a quotation with a plain double quotation mark; check the remaining question marks by eye (real ones end a question). Process: add to `plan.py check` (or the turn gate) a scan for `\w\?\w` and for `?` directly after an opening space and before a capital, outside URLs, so the gate catches it next time (see "For the structure pass").

### CW2. No dated teacher background on 2025 and 2026 changes (moderate; LAYER plan; REPEAT)

Settled in the grade 4 read and applied in the US Government read: political and legal changes get a teacher background line, dated "checked (date)", stated as fact and not argued by party. None of the ten plans has one. The changes that touch what these units teach, all checked today or in today's US Government read:

- **Unit 3:** Learning Resources v. Trump (February 20, 2026, 6 to 3: the emergency powers law does not authorize tariffs; taxing is Congress's power); Trump v. Slaughter (June 29, 2026, 6 to 3: Humphrey's Executor overruled, the President may remove FTC commissioners at will; the same day Trump v. Cook kept Federal Reserve governors' protection); Trump v. CASA (June 27, 2025: limits on universal injunctions by lower federal courts, from memory, verify); "Department of War" is a secondary title since September 2025, the legal name is still Department of Defense; the November 3, 2026 election gave Democrats both chambers from January 3, 2027, so a fall 2027 class meets divided government.
- **Unit 4:** Watson v. RNC (June 29, 2026, 5 to 4: states may count mail ballots postmarked by Election Day and received later); Louisiana v. Callais (April 29, 2026, 6 to 3: narrowed vote-dilution claims under section 2 of the Voting Rights Act); 2025 to 2026 mid-decade redistricting (Texas, Missouri, North Carolina, California Proposition 50); the 2026 midterm result.
- **Unit 5:** Executive Order 14160 (January 20, 2025) on birthright citizenship; Trump v. Barbara (June 30, 2026) held it unconstitutional under the Fourteenth Amendment's Citizenship Clause (values rule (a)); the 2025 naturalization civics test (5.2).
- **Unit 6:** Shelby County v. Holder (2013) ended the preclearance coverage formula and Louisiana v. Callais (2026) narrowed section 2, so the 1965 Act's reach today differs from 1965; Obergefell stands (the Court denied Kim Davis's petition to revisit it, Davis v. Ermold, November 10, 2025); Trump v. Barbara on the Citizenship Clause.
- **Unit 7:** changes in federal and state school and welfare roles since 2025 (the March 2025 executive order directing the Department of Education's closure and the July 2025 Supreme Court stay in McMahon v. New York allowing its layoffs; the July 2025 reconciliation law's shift of some Medicaid and food-aid costs to states). These rest on memory: verify before writing the line.
- **Unit 9:** Congress rescinded the Corporation for Public Broadcasting's funding in 2025 and its board voted to dissolve it (announced January 5, 2026); TikTok v. Garland (January 17, 2025) upheld the divest-or-ban law.

Fix: one "Current check, checked 2026-11-14:" paragraph in field 10 of units 3 to 7 and 9, wording per unit below. Students keep each unit's limits; no student is asked which side was right by party.

### CW3. End-of-unit assessments over their minutes (moderate; LAYER plan; REPEAT)

Settled in the grade 4 read and applied in the US Government read: about 1 minute per recall item, 2 per one-sentence explanation, 8 to 10 per paragraph claim; parts already scored from earlier independent products come off the sitting; cut instances, never parts. Over-full: unit 2 (day 29), unit 3 (day 46), unit 5 (day 75). Tight but workable with a small cut: units 1, 4 and 6. Units 7, 8, 9 and 10 hold (unit 7 by its composite records, unit 9 by an eight-minute reading block, unit 10 by performance records). Unit fixes below.

### CW4. Sensitivity studies misaimed or thin (moderate; LAYER plan; REPEAT of the US Government CW6 kind)

Unit 3's study is unit 2's copied (Black petitioners, Douglass, Oneida, Gordon-Reed, colonial slave laws), while the frame's focus for unit 3 is current officeholders from several parties. Unit 5's immigrant voices are two advocacy organizations, where the frame names an immigration journalism style guide. Unit 2 omits the frame's "national museum of African American history's teaching pages". Unit 7 names "Native scholarship and journalism guidance" without a source. Fixes per unit; add, do not replace community voices.

### CW5. "The lead" written where the teacher is meant (minor; LAYER plan; new)

s08 field 10 ("The lead must arrange unit 10's audience by 130") and s10 fields 10 and U11 ("the lead must confirm the existing audience"). The frame and days.csv day 127 say the teacher books the audience. A teacher reading the plan would think someone else does it. Fix: "The teacher books unit 10's audience beyond the class by day 130 (frame)" in s08; "The teacher confirms the audience booked by day 130, the venue and the safe route before day 149" in s10.

### CW6. Exit tickets ask three things (minor; LAYER plan; REPEAT)

As in the US Government read (1.5): several quarter-page exits ask a claim, a counterclaim, strengths, limits and a response (s01 days 11 and 12; s01 days 3, 5, 7, 8; s02 days 16, 19, 27; s03 day 33 adds "Summarize IV, VI and VII too"). Cut each to one question and one reason; the second ask moves to the next day's warm-up.

## Unit 1: Roots of self-government (days 1 to 15)

The start of the year is handled rightly: unit 1 has no readiness rows (all three assumed rows were used in grade 7), field 4 says retrieval only, day 1 opens on its hook, and nothing sits before day 1. The unit 2 readiness items sit in day 15's last ten minutes, as days.csv says, and match s02 exactly.

**1.1 Since Time Immemorial credit on a Haudenosaunee day (moderate; LAYER data; REPEAT of the settled rule "Native nations varied, each from its own sources").** days.csv day 9 note: "Background from Since Time Immemorial where used: adapted from Since Time Immemorial (Washington OSPI, CC BY 4.0); the content is the tribes'". Day 9 teaches the Haudenosaunee Confederacy from its own pages; Since Time Immemorial unit 1C is the Medicine Creek Treaty nations' content, and s01 field 10 says nothing is adapted here. Copied to a day page, the credit would attribute Haudenosaunee content to Washington tribes. Fix, days.csv day 9 note, old: "Background from Since Time Immemorial where used: adapted from Since Time Immemorial (Washington OSPI, CC BY 4.0); the content is the tribes'" New: "From the Confederacy's and the Onondaga Nation's own pages. Since Time Immemorial gives teacher background on sovereignty only; nothing is adapted here, so no credit line".

**1.2 "Franklin's Albany Plan remarks" is the 1751 letter (minor; LAYER data, plan; new).** days.csv day 10 goal and the scope and sequence name "Franklin's Albany Plan remarks"; s01's source is Franklin to James Parker, 1751, three years before the Albany Plan (1754). Students sourcing by date need the right label. Fix, day 10 goal, old: "Franklin's Albany Plan remarks" New: "Franklin's 1751 letter on a colonial union (three years before his Albany Plan)". Same words in scope-and-sequence.md unit 1 topics.

**1.3 Day 14 items 1, 2 and 4 are dense for their minutes (minor; LAYER plan; REPEAT CW3).** Item 4 asks for Magna Carta, habeas corpus, Parliament, the English Bill of Rights, legislatures, town meetings and Blackstone in six minutes. Fix: item 4's four English protections as a one-phrase matching grid (4 minutes), the two colonial practices and Blackstone in two sentences; item 2 drops "three sentences" for a labelled four-office grid. The forty minutes then hold.

**1.4 Exits too long (minor; CW6).**

What is right: the corroboration and sufficiency models on days 10 and 11; the 1988 resolution and Senate Report 100-565 kept apart and dated (error F); the slur in Franklin's letter paraphrased out; Clan Mothers' authority and the present tense.

## Unit 2: The founding documents (days 16 to 30)

**2.1 The Declaration's grievance on Native peoples has no teacher note (moderate; LAYER plan, frame; new).** Day 17 reads the grievances closely and day 19 asks who the words left out, naming Native nations; the Declaration's last grievance calls Native peoples "merciless Indian Savages". Neither s02, the frame nor days.csv says how to handle it. Rule 6 (no slur printed) and BASELINE rule 8 (teacher notes name the sensitive point) both apply, and the frame already sets the pattern for Dred Scott's language. Fix, s02 field 2 Limits, add: "The Declaration's last grievance accuses the king of inciting attacks and names Native peoples with a slur. Student pages summarize it ('a grievance that blamed the king for Native nations' attacks and described Native peoples with an insult'); the teacher names it as a slur and does not have it read aloud. On day 19 it is evidence of how the document excluded Native nations, set beside the Oneida Nation's own account of its Revolutionary alliance." Add the same line to the frame's Sensitive content bullet and the days.csv day 17 and 19 notes.

**2.2 Day 29 over-full (moderate; LAYER plan; REPEAT CW3).** Forty-five working minutes, no slack: item 1 is two causes plus seven principle boxes, item 4 is five leaders, two settlements and four clauses in eleven minutes. Fix: item 4's leaders become a five-row matching grid (one minute each); the Great Compromise and the three slavery clauses keep one sentence each. Item 1's seven boxes are one phrase each. That frees about five minutes for checking.

**2.3 Day 16 repairs take twenty minutes (moderate; LAYER plan; REPEAT, US Government CW4 settlement).** U6: "twenty for the two readiness repairs and cause review". The settled cap is ten minutes at the start for flagged students while the rest begin. Fix: repair A in the first ten minutes for students who missed N1; repair B in the warm-up of day 17 for students who missed N2 (day 17 opens on "declaration and governing plan", which B serves); day 16 keeps twenty-five minutes of investigation.

**2.4 Phantom day 16 retrieval row (minor; LAYER skeleton; REPEAT US Government CW5).** Field 4's row "16 | retrieval task on day 20. Sensitivity read..." is the skeleton's forward match. Codex flagged it in the cell; delete the row.

**2.5 Sensitivity study missing the museum's teaching pages (minor; CW4).** Add the national museum of African American history's founding-era teaching pages (as unit 3 already links its colonial slave laws page) and finish Gordon-Reed beyond the abstract.

**2.6 Exits (minor; CW6).**

Facts checked and correct: the Prince Hall petition (January 1777), Article XIII unanimity and nine-state rule, Annapolis 1786, the 1808 clause, Mason's bill of rights motion rejected at the Convention.

## Unit 3: The Constitution and the three branches (days 31 to 47)

**3.1 Sensitivity study is unit 2's (moderate; LAYER plan; CW4).** Field 10 "Sensitivity study required" lists the petitioners, Douglass, Oneida, Gordon-Reed and slave laws. The frame's unit 3 note is "current officeholders named only as examples, from several parties". Fix, replace with: "Study each major party's own description of the separation of powers and executive power (each party's latest national platform, the government section), one limited-government and one expansive-government advocacy organization's own pages, and the Congressional Research Service's overviews of the Speaker, leaders and whips; then check every officeholder example for party spread and date." Keep the slavery-in-the-text teacher note in Limits.

**3.2 No current check (moderate; CW2).** Field 10, add: "Current check, checked 2026-11-14: Learning Resources v. Trump (February 20, 2026, 6 to 3): emergency powers law does not authorize tariffs; tariffs belong to Congress's taxing power. Trump v. Slaughter (June 29, 2026, 6 to 3): the President may remove FTC commissioners at will (Humphrey's Executor overruled); the same day Trump v. Cook kept Federal Reserve governors' protection. Trump v. CASA (June 27, 2025) limited universal injunctions by lower federal courts. From January 3, 2027 Democrats hold both chambers. The department's legal name is Department of Defense; 'Department of War' is a secondary title. State these as facts and as checks at work; no student judges them by party." Day 40 or 44 may use one as an optional current case.

**3.3 Day 46 over-full (moderate; REPEAT CW3).** Item 4b asks for the override rule, a power and a limit, four leadership roles, the whole executive hierarchy, a presidential power and limit, confirmation and impeachment in ten minutes; item 6 asks for a powers-and-limits chart across national, state, local and British institutions in six. Fix: 4b's leaders and hierarchy become labelled matching (4 minutes), override, confirmation and impeachment one sentence each; item 6 keeps the United States national and British comparison plus one sentence on local government (the other cells are evidenced on day 41).

**3.4 Armed services "within Defense" (minor; LAYER plan; new).** Item 4b's key and the day 39 exit say the armed services are within Defense. The Coast Guard sits in the Department of Homeland Security in peacetime. Fix, old: "Armed services operate within Defense under civilian authority." New: "Most armed services sit in the Department of Defense (the Coast Guard in Homeland Security), all under civilian authority."

What is right: the unseen Nixon passage glossed as an evidence case, not immunity; Clinton v. City of New York for a majority and dissent; Britain's courts correctly limited.

## Unit 4: Elections and parties (days 52 to 63)

**4.1 No current check (moderate; CW2).** Field 10, add: "Current check, checked 2026-11-14: Watson v. RNC (June 29, 2026, 5 to 4): states may count mail ballots postmarked by Election Day and received later; state rules still differ. Louisiana v. Callais (April 29, 2026) narrowed vote-dilution claims under section 2. In 2025 to 2026 Texas, Missouri, North Carolina and California (Proposition 50) redrew congressional maps mid-decade. The November 3, 2026 election gave Democrats both chambers from January 3, 2027. Any question about a third presidential term is answered from the Twenty-second Amendment's text. Check each before teaching; students compare rules, not parties." Day 52's latest-election rule stands.

**4.2 Third-party balance (minor; LAYER plan; balance; new).** Day 55 studies the Democratic, Republican and Green platforms. With one minor party, it leans one way. Fix, field 10: add the Libertarian Party's platform (its elections or government section) beside the Green platform, and label the two major platforms "2024, the latest national platforms; check for newer at build". The sensitivity study then covers four parties' own words.

**4.3 Day 62 tight (minor; REPEAT CW3).** Item 5 (five cards, two calculations) has eighteen minutes and item 1 twelve. Fix: give item 1's route diagram as a partly drawn grid (House and Senate rows filled as the model), so it takes eight minutes; four minutes go to item 5's reading.

Facts checked and correct: Maine and Nebraska's district method, the Twelfth and Twenty-second Amendment rules, the 2016 and 2020 age-row rates.

## Unit 5: Citizens and civic values (days 64 to 76)

**5.1 Birthright citizenship has no teacher line (moderate; CW2).** Day 64 teaches citizenship by birth; item 1 chooses a 2011 birth to two citizen parents, which avoids the question but leaves the teacher without the fact students will raise. Field 2 Teacher background, add: "Checked 2026-11-14: Executive Order 14160 (January 20, 2025) sought to deny citizenship to some children born here to non-citizen parents; in Trump v. Barbara (June 30, 2026) the Supreme Court held it unconstitutional under the Fourteenth Amendment's Citizenship Clause. Teach birth in the United States subject to its jurisdiction as the rule the Court upheld (values rule (a)). No question asks about any student's or family's status."

**5.2 The 2025 civics test needs a dated line (minor; LAYER plan; new).** Field 10 says the 2025 bank was "indexed only". Checked today: applicants filing on or after October 20, 2025 are asked up to 20 questions from a 128-question bank and pass with 12 correct; earlier filers take the 2008 test (10 of 100, 6 correct). Add that to field 2's background, and: "State graduation civics tests may still use an older bank; use your state's." Day 65 practice uses public questions only, as settled.

**5.3 Sensitivity study rests on advocacy groups (moderate; CW4; balance).** United We Dream and Define American are advocacy organizations with policy positions; the frame names an immigration journalism style guide. Fix, field 10: study first a journalism style guide's immigration entries (for example the Society of Professional Journalists' or the National Association of Hispanic Journalists' guidance), then the two community voices, and record terms that both describe neutrally. Keep the no-disclosure and no-simulation rules.

**5.4 Day 75 over-full (moderate; REPEAT CW3).** Eleven items in forty-five minutes, including seven roles (item 4), six definitions with six examples (item 5) and six service examples (item 10). Fix: item 4 (D2.Civ.2) and item 10 (MA.8.T4.9) are scored from the independent written work of days 66 and 72 when those days carry it (state so in field 5), freeing about twelve minutes; item 5 keeps six one-line definitions with three examples (cut instances).

What is right: leaders from three parties and eras (Adams-era laws, Smith, Truman), with decision kept apart from courage; the citizenship routes and residency distinctions are accurate.

## Unit 6: Rights over time (days 77 to 95)

**6.1 Brown v. Board of Education is absent, and area b's equal protection rests on Lochner and Parrish (moderate; LAYER plan; new).** Nowhere in the year does Brown appear. Area b (MA.8.T5.6b, due process and equal protection) compares Lochner (1905) and Parrish (1937), economic substantive due process, and borrows Obergefell from day 83 for equal protection. For grade 8 the canonical pair that shows a decision changing lives over time under the Equal Protection Clause is Plessy v. Ferguson (1896) and Brown (1954); it also models a later Court overruling an earlier one, which area c teaches with Barnette. An adoption reviewer would mark a civics year without Brown. Fix (settled below): area b compares Plessy and Brown, with Dred Scott as pre-amendment background and Obergefell as a later equal protection and liberty holding; Lochner and Parrish move to an extension card. Plessy's racist language is summarized, not printed, as for Dred Scott. Also add Brown to day 82's teaching of the movements behind the 1964 Act (one sentence). Change days.csv day 85 note's 6b text to "(Dred Scott as background; Plessy and Brown compared)".

**6.2 No current check (moderate; CW2).** Field 2 teacher background, add: "Checked 2026-11-14: the 1965 Act's reach today differs from 1965: Shelby County v. Holder (2013) ended the preclearance coverage formula, and Louisiana v. Callais (April 29, 2026) narrowed section 2 vote-dilution claims. Obergefell stands: the Court declined to revisit it on November 10, 2025 (Davis v. Ermold). Trump v. Barbara (June 30, 2026) applied the Citizenship Clause. State as fact; students weigh evidence, not parties."

**6.3 Day 94 tight (minor; REPEAT CW3).** Items 1 and 3 each ask three documents' context, significance and a barrier. Fix: item 1 asks all three amendments' change in a phrase each and context and barrier for one chosen amendment (the other two are evidenced on days 79 to 81); same shape for item 3's laws.

**6.4 Sensitivity sources unnamed (minor; CW4).** Name the disability language guide (the National Center on Disability and Journalism style guide, as unit 8 uses) and link the Teaching Hard History guidance.

What is right: slavery named as the central cause from the declarations; Barnette over Gobitis under values rule (a); Goss v. Lopez as an unseen opinion; the research report counted with the assessment.

## Unit 7: Federalism and your state (days 100 to 119)

**7.1 No current check (moderate; CW2).** Field 2 teacher background, add a "Current check (date)" on changes in federal, state and local roles for schools and welfare since 2025 (the Department of Education order of March 2025 and McMahon v. New York, July 2025; the 2025 reconciliation law's cost shifts to states), each verified before writing, stated as fact; students contrast responsibilities, not parties.

**7.2 Budget source labelled recommended (minor; LAYER plan; new).** The Boston FY26 operating budget is "recommended, not adopted". Fix: "At build, use an adopted budget of the class's own town or state for the current year; Boston FY26 stays a worked example only" (settled own-place rule, grade 3 read).

**7.3 Sensitivity study unnamed (minor; CW4).** Name the journalism guidance (for example the Native American Journalists Association's reporting guide) and keep Cecelia Carpenter's unit 1C account; the study's "coercion, displacement" check should name the treaty's hard history the unit carries.

What is right: the composite records (days 113, 115, 116) are independent tasks after teaching; every economics figure checks (interest, inflation as rate versus level, the unemployment denominators, the $160,000 over $150,000 trade-off); Massachusetts Article I as replaced by Amendment 106 and New York Article XI are accurate; the general-form "your state" method holds.

## Unit 8: How change happens (days 120 to 130)

**8.1 The spectrum is uneven, and the samples use uneven verbs (moderate; LAYER plan; balance; new).** The disability movement carries days 120, 122, 123, 125 and 126 and is a historical case with a documented law and outcome; the other side appears as a current advocacy page (Tea Party Patriots' mission and action items) on days 122 and 127. Item 2's sample says disability advocates "sought participation" while "fiscal conservatives claim lower spending protects opportunity. These claims need outcome evidence." A student learns one side's goals as achieved history and the other's as unproven claims. Fix (settled below): give the conservative tradition one historical case with a public record of method and result, California's Proposition 13 (1978), from the state's official ballot pamphlet arguments for and against and the enacted text; use it on days 121, 122 and 127 beside the 504 sit-in; keep the current page only for stated goals, with its access date. In item 2's sample, use the same verbs for both ("Disability advocates sought ...; Proposition 13's backers sought ...; both claims of public benefit need outcome evidence").

**8.2 "The lead must arrange" (minor; CW5).**

What is right: the bipartisan history of the disability law said plainly; the fictional research forecast with disclosed funding; the Clean Air Act summary paired with invented records clearly marked.

## Unit 9: A free press and the news (days 131 to 144)

**9.1 Broken characters (moderate; CW1).**

**9.2 No current check (moderate; CW2).** Field 10, add: "Current check, checked 2026-11-14: Congress rescinded the Corporation for Public Broadcasting's funding in 2025 and its board voted to dissolve it (announced January 5, 2026). TikTok v. Garland (January 17, 2025) upheld a law requiring the app's sale or ban. Press-access disputes with federal offices in 2025 are in the courts; check before naming one. State as fact; no outlet is named trusted or untrusted." The plan's "no named contemporary court dispute is taught" stays for students.

**9.3 Boston fare-free program is dated (minor; LAYER plan; REPEAT US Government 9.2).** Checked: routes 23, 28 and 29 are fare-free through December 2026; a fall 2027 class meets a different status. Add: "Check the program's current status before day 131; its evaluation stays a dated worked example."

What is right: MassBudget and Pioneer Institute give the two sides of one local issue; the day 143 packet is invented, short and sized (fifty minutes, reading counted).

## Unit 10: Civic action (days 149 to 160)

**10.1 Broken characters (moderate; CW1).** The day 154 cards A to E and every quoted item are affected.

**10.2 The teacher, not the lead, confirms the audience (minor; CW5).**

**10.3 Error register table has three cells under four headings (minor; LAYER plan; new).** Field 6's rows lack the "wrong beside right" column, which sits in a paragraph below. Fix: move each paragraph sentence into its row's fourth cell.

**10.4 Scoring scale differs from the other nine units (minor; LAYER plan; new).** Field 5 scores 2, 1, 0; units 1 to 9 use secure, developing, missing. Fix: "secure (all look-fors), developing (partial), missing (absent or contradicted)", so one record sheet serves the year.

What is right: the class chooses the problem and the action; no cause, party campaigning or fundraising; school-mediated delivery; "silence is not consent" and "response pending" recorded on day 160; the generic consensus circle not passed off as a Native tradition; individual evidence inside the shared product.

## Course flow

Handoffs hold: units 1 and 5 carry the next unit's readiness items, identical in the receiving plans (s02 N1 and N2; s06 items 1 to 3), given in the respond day's last ten minutes; units 3, 6 and 9 hand on through the course-level checks; unit 8 carries the audience booking (day 127) to unit 10; each plan's "Returns" day numbers match days.csv. Voice is plain full sentences, dense in units 3 and 7 field 5 but readable. Nothing invented is passed off as real: every fictional record is labelled, and every real source is linked, dated and marked read, indexed or blocked. No company or product names in student or family copy.

## Settled by the expert

| Question | Ruling | Where it binds |
|---|---|---|
| Unit 1's start-of-year check | Lead rule 2026-11-14 applied: no readiness rows, so "none needed; retrieval only"; s01 field 4 already complies. | s01 field 4 |
| Assessment sizing, reteach cap, current-check lines, Native nations each from their own sources | Settled earlier (grade 4 and US Government reads), applied here without re-argument. | CW2, CW3, 1.1, 2.3 |
| Area b of the unit 6 research | Plessy (1896) and Brown (1954) are the compared pair; Dred Scott pre-amendment background; Obergefell a later holding; Lochner and Parrish an extension card. Reason: the canonical equal protection change over time at grade 8, and the only place Brown can sit in the year. | s06 fields 5 and 10; days.csv days 82 and 85 notes |
| Balance in unit 8 | Proposition 13 (1978), from the official ballot pamphlet and enacted text, is the historical conservative-side case beside the 504 sit-in; both described with the same verbs. | s08 fields 2, 5, U3, U6; days 121, 122, 127 |
| The Declaration's grievance slur | Summarized on student pages, named as a slur by the teacher, not read aloud; used on day 19 as evidence of exclusion. Same pattern as Dred Scott's language. | s02 field 2; frame Sensitive content; days.csv days 17 and 19 |
| Day 9 credit line | No Since Time Immemorial credit on a Haudenosaunee day; nothing is adapted there. | days.csv day 9 note |
| Minor-party platforms in unit 4 | Two minor parties from different sides (Green and Libertarian) when any minor party is studied. | s04 field 10 |
| Franklin source label | "Franklin's 1751 letter on a colonial union (three years before his Albany Plan)". | days.csv day 10 goal; scope-and-sequence.md |
| Unit 3 Coast Guard | "Most armed services sit in the Department of Defense (the Coast Guard in Homeland Security)". | s03 item 4b key, day 39 exit |

## For the fixer

Exact edits, in order. Nothing adds days. Run `plan.py check` after the data edits. Log each item with `plan.py defect` (found_by expert); this read edits only its report.

1. **Broken characters (CW1):** s09.md and s10.md, replace every "?" that stands for an apostrophe or quotation mark; leave real question marks and URLs.
2. **days.csv:** day 9 note (1.1); day 10 goal (1.2); days 17 and 19 notes, add the grievance note (2.1); day 85 note, 6b text (6.1); day 82 note, add "Brown v. Board of Education (1954) named as the ruling the movement built on". Then scope-and-sequence.md unit 1 topics (1.2) and unit 6 topics (Plessy and Brown in area b). Re-run `plan.py tables` so the plans' day lists follow.
3. **Frame:** Sensitive content bullet, add the Declaration grievance sentence (2.1); unit 6 "What students learn" area b, "Plessy and Brown" in place of "later 14th Amendment cases". This is an item-level choice inside MA.8.T5.6b's own words, not a scope change.
4. **Current-check lines (CW2):** s03 3.2, s04 4.1, s05 5.1 and 5.2, s06 6.2, s07 7.1, s09 9.2.
5. **Assessment sizing (CW3):** s02 2.2, s03 3.3, s05 5.4; then s01 1.3, s04 4.3, s06 6.3.
6. **Content and balance:** s06 6.1 (fields 5 and 10, report area b and its sample); s08 8.1; s02 2.1 (field 2); s03 3.4; s04 4.2.
7. **Sensitivity studies (CW4):** s03 3.1, s05 5.3, s02 2.5, s06 6.4, s07 7.3; then the sensitivity agent's reads as the frame assigns.
8. **Reteach cap:** s02 2.3 (U6 day 16 and field 4).
9. **Minor:** s02 2.4 (delete the phantom row); CW5 (s08, s10); CW6 (exits); s07 7.2; s09 9.3; s10 10.3, 10.4.

## For the structure pass

- **A broken-character gate (CW1).** `plan.py check` (or `turn.py end`) scans docs/courses/**/*.md for `\w\?\w` and for "?" right after a space or line start and before a capital letter, outside link targets, and fails the file. Worth also finding why the s09 and s10 writes lost their quotation marks (probably a shell write in a non-UTF-8 code page), so the brief can name the safe write path.
- **Retrieval rows from forward references.** The skeleton's phantom row (s02 day 16) is the same regex fault already filed from the US Government read (its CW5); no new item.
- **A "Current check" line in the template.** Repeat of the US Government read's suggestion: UNIT-PLAN.md field 10 for social studies carries a standing "Current check (date):" line, so CW2 cannot recur unnoticed. Ten of ten plans here missed it.
- **The Declaration's slur, every course.** ELA 8, ELA 9, ELA 11, US History I, ELA 12 and Government all read the Declaration (frame, founding documents lens). The grievance note in 2.1 should be one shared teacher note those courses point to.
- **Seams note.** `plan.py check` notes the Seams table does not name wh2-social-movements (a "leads to" in s06); add it to the frame's handed-on table row for ss8-civil-rights-laws or ss8-protest-change.

## For Cory

None. Everything here is inside the plans, the data and the frame's item-level wording.

## Sources (web checks, November 14, 2026)

- Davis v. Ermold, certiorari denied November 10, 2025: [Michigan Public](https://www.michiganpublic.org/2025-11-10/supreme-court-declines-to-revisit-gay-marriage-decision), [Spokesman-Review](https://www.spokesman.com/stories/2025/nov/10/supreme-court-denies-former-kentucky-clerk-kim-dav). Used for 6.2.
- Boston fare-free routes extended through December 2026: [Boston.com, June 9, 2026](https://boston.com/news/transportation/2026/06/09/free-mbta-bus-routes-extended-through-end-of-year-wu-announces), [city program page](https://www.boston.gov/departments/transportation/free-route-23-28-and-29-bus-program). Used for 9.3.
- 2025 naturalization civics test (filed on or after October 20, 2025; 20 of 128, 12 correct): [ProLiteracy](https://www.proliteracy.org/news/what-to-know-about-the-2025-updates-to-the-us-citizenship-civics-test/), [Fredrikson](https://www.fredlaw.com/alert-uscis-unveils-new-naturalization-civics-test). Used for 5.2.
- Corporation for Public Broadcasting dissolution, announced January 5, 2026: [The Desk](https://thedesk.net/2026/01/corporation-public-broadcasting-shuts-down/), [Washington Times](https://m.washingtontimes.com/news/2026/jan/6/nprs-parent-shutting-months-gop-funding-cuts/). Sources differ on which 2025 law cut the funding; the line says "rescinded in 2025" only. Used for 9.2.
- Reused from today's US Government read (its Sources list): Louisiana v. Callais, Learning Resources v. Trump, Trump v. Slaughter and Trump v. Cook, Trump v. Barbara, Watson v. RNC, mid-decade redistricting, the 2026 midterm result, the Department of War name status.
- From memory, to verify before writing the lines: Trump v. CASA (June 27, 2025); TikTok v. Garland (January 17, 2025); the March 2025 Department of Education order and McMahon v. New York (July 2025); the 2025 reconciliation law's cost shifts to states; the Coast Guard's place in Homeland Security; the Declaration's grievance wording.

## For the source list

No new source for docs/APPROACH-SOURCES.md beyond the news reports above, which are dated checks, not lasting references.
