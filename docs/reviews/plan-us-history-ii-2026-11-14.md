# Plan read: US History II, units 1 to 12 (2026-11-14)

Expert cold read of docs/courses/us-history-ii/s01.md to s12.md. Codex wrote them today from unit_skeleton.py skeletons. The read follows docs/pipeline/briefs/plan-read.md, unit by unit, with the course-wide questions from the lead's brief. The reader read units 1 to 4 directly and split units 5 to 8 and 9 to 12 between two forks of the same read, with the same brief and settled tables. The findings below are merged into one report.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/plan-read.md, docs/agents/lenses/social-studies.md and docs/GLOSSARY.md.
- docs/courses/us-history-ii/frame.md and scope-and-sequence.md, data/plans/us-history-ii/days.csv (all 160 rows) and the progression rows each plan cites.
- The social studies part of docs/ADOPTION-BAR-SUBJECTS.md (items 1 to 14, with core C1 to C16) and docs/courses/social-studies/STANDARD.md.
- s01.md to s12.md in full.
- The "Settled by the expert" tables in plan-social-studies-kindergarten, grade-1, grade-3 and grade-4 (2026-11-14), and the whole of plan-us-history-i-2026-11-14.md, which this course follows. Those rulings are applied here and cited, not re-argued.
- Gate: `python -X utf8 scripts/plan.py check` passes the course: 12 units, 160 days (154 in units, 6 for course-level checks and respond days), 0 failures.
- Web checks this run, listed under Sources at the end.

Severity follows cost. **Serious** means a student is taught or assessed wrongly, or a sensitivity failure reaches a classroom. **Moderate** means the plan cannot be run as written, a standard's part is weakly evidenced, or a fact is stale. **Minor** means wording, a missing teacher note or a data tidy. LAYER says where the fault lives (plan, skeleton, data or process). REPEAT is yes when an earlier read found the same kind of fault.

## Course verdict

The twelve plans are careful, well-sourced work. Every goal has an item, and unseen sources are held back for every assessment. Hard history (Tulsa, eugenics, the Holocaust, Nanjing, incarceration, My Lai, termination) is named plainly with no role play. The informed action is the student's own choice, through a safe route, and no campaign or party pages are used. Nothing found is serious. The course is not yet at the bar for four reasons, all fixable inside the existing days:
- Ten of the twelve end-of-unit sittings ask for more than their minutes hold. Three of them do so because the skeleton turned "one of" and "such as" lists into required parts.
- Unit 1's readiness check still sits before day 1.
- Several 2025 and 2026 facts are missing or written cryptically. The worst gaps are the Federal Reserve rulings and the new chair in unit 1, Dolores Huerta's and Gloria Steinem's deaths in unit 9, and the lapse of Section 702 in unit 11.
- Units 4 to 8 present made-up exit captions without saying they are made up.

## Course-wide findings

### CW1. Sittings ask more than their minutes hold (moderate; LAYER plan and skeleton; REPEAT yes, US History I CW1 and grade 4 "sized to their minutes")

Units 1, 2, 4, 5, 6, 7, 8, 9, 10 and 11 each have items well past the settled rate: about 1 minute per locate or date item, 2 per one-sentence explanation, 8 per paragraph claim. The worst is unit 1: about 70 minutes of work in 40. The fix is the same in every unit: cut instances, never parts, and do not re-ask a part that a product (R, S, W or P work) already scored. The exact cuts are given per unit.

In units 4, 8 and 11 the overload comes from the skeleton. It parsed MA.USII.T3.5 ("one event, one major battle, or one conference"), T5.1 and T5.5 ("such as") as required parts. US History I's ruling on "research one ... from the list" applies: assess the chosen case in depth and survey the rest.

### CW2. Dated present-tense lines missing or cryptic (moderate; LAYER plan; REPEAT yes, "current official facts" and US History I's 2025 to 2026 row)

The missing lines are in units 1, 2, 4, 5, 6, 7, 9, 10 and 11, and each is given per unit. Every line follows the settled form: "Checked 2026-11-14: ...". The line states the fact, is never argued by party, and no student is asked about status or identity.

### CW3. Made-up exit captions not labelled as made up (minor; LAYER plan; REPEAT yes, "nothing invented passed off as real")

Units 4 to 8 open exits with "a new caption", "a museum display says" or "a display says", but never say the caption is invented. A student will read it as a real artifact. Units 1 to 3 label their scenarios "fictional" and do this right, as does s06's E70 ("fictional exhibit").

**Fix:** add one line at the top of U3 in s04 to s08: "Every caption or display an exit asks students to correct is written by Curio Class for practice, and the page labels it so."

### CW4. Copyrighted modern texts planned as excerpts (minor; LAYER plan; REPEAT yes, US History I CW2)

The affected texts are B. C. Franklin's 1931 manuscript (unit 2), the USC Shoah Foundation and USHMM testimony clips (unit 4), DREDF, NOW and the Huerta biography (unit 9), and the Schlafly interview (unit 10).

**Fix:** add one line to each affected field 10: "Copyrighted or unpublished texts are excerpted only with written permission; otherwise attributed paraphrase." Federal records and public-domain originals stay as excerpts.

### CW5. The frame's seam table puts readiness checks on the units' first days (minor; LAYER plan (frame); REPEAT yes, readiness timing)

frame.md's Seams table says "readiness check on day 42", "on day 57", "on day 67", "on day 103" and "on day 114". The scope and sequence, days.csv and every plan correctly put each check in the previous day's last ten minutes. **Fix:** change each to "in day 41's (56's, 66's, 102's, 113's) last ten minutes".

days.csv days 61, 68 and 104 say "day 57 flagged" (and so on). **Fix:** change these to name the previous day's check.

### CW6. Voice is dense (minor; LAYER plan; REPEAT yes, US History I CW3)

Many lines are stacked noun phrases, for example "Withdraw prompts on 31 and 37; retain models for transfer". **Fix:** rewrite fields 2, 4 and 7 in plain full sentences at section-plan time. This does not block the unit plans.

### CW7. Sensitivity study lists: mostly right, three gaps (minor; LAYER plan (frame); REPEAT yes)

Each plan's "Sensitivity study required" paragraph covers what the frame names, and most add to it. The gaps are:
- The frame lists nothing for units 1 and 10. Each plan supplies its own list; the frame should carry them.
- Unit 5 omits Korean and other non-Japanese bomb survivors.
- Unit 11 omits veterans' oral histories.

The exact lines are in the unit findings.

## Unit 1: The economic toolkit (days 1 to 12)

**U1-1. Readiness check placed before day 1 (moderate; LAYER plan, data and skeleton; REPEAT yes, US History I U1-1).**
- *What is wrong:* field 4 says "**Given:** the start-of-year check, before day 1" and "Give these four items in ten minutes a few days before opening". Unit 1 has a readiness row (ss8-public-budget, last used in grade 8), so the lead rule of 2026-11-14 applies: the check is the last ten minutes of day 1, after the hook, with the reteach on day 2 or 3.
- *Why it matters:* a teacher cannot give a check on a day that does not exist, and day 1's U6 row has no ten minutes for it.
- *Fix:*
  - Day 1's U6 row becomes: hook 8, teach choice 10, compare 17, E1 5, readiness check 10.
  - Item 1's reteach moves from "immediately after day 1's hook" to day 2's station, beside items 2 to 4. Overflow goes to day 3's warm-up.
  - days.csv day 1 needs `assess` = readiness and a new note.
  - The day 2 note, scope-and-sequence.md line 55 and the unit 1 row of the readiness table change to match.
  - The skeleton's carried line ("in the start-of-year check before day 1") does not match the frame, which says "inside day 1's readiness check". That line goes to the structure pass.

  Exact text is in "For the fixer" 1 to 4.

**U1-2. Assessment overload (moderate; LAYER plan; REPEAT yes, CW1).**
- *What is wrong:* day 11 gives 40 minutes to work that takes about 70 at the settled rate.
  - A2 (7 minutes) asks for a choice, seven matches, a conflict, a systems comparison, four roles and who gains or pays.
  - A3 (8 minutes) asks for definitions, two shifted equilibria, profit and risk, and new issue against resale.
  - A7 (5 minutes) asks for the Civil War's three effects plus four technology cards, each with a consequence.
  - A8 (2 minutes) asks for an 1893 judgment from two sources plus a policy distinction.
- *Fix:*
  - A2: the seven-goal matching grid, one conflict sentence and two of the four role cases (the student's choice); drop the systems comparison to one sentence. 10 minutes.
  - A3: one graph with the demand shift; one sentence on the supply shift; profit and new issue in one sentence each. 8 minutes.
  - A7: the Civil War card plus one 19th-century and one 20th-century technology card (the student's choice). 6 minutes. T1.10 and T1.9b are "such as" lists.
  - A8: one 4-minute item judging Cleveland's repeal from both sources and naming missing evidence. Day 10's argument already scores T1.11.
  - A1, A5 and A6 drop to 6, 3 and 3 minutes, with A6's diagram supplied as a labelling task.
  - New totals: A1 6, A2 10, A3 8, A5 3, A6 3, A7 6, A8 4 = 40.

**U1-3. The Federal Reserve taught with no 2026 line (moderate; LAYER plan; REPEAT yes, CW2).**
- *What is wrong:* the compelling question asks who should steer the economy, and day 8, E8 and A6 teach that elected leaders do not vote on rates. In 2026 the Fed's independence was itself a live court question. On June 29, 2026, in Trump v. Cook, the Supreme Court, 5 to 4, let Governor Lisa Cook stay in office while her case goes on, on narrow due-process grounds; the Congressional Research Service reads the ruling as upholding the for-cause protection. The same day, Trump v. Slaughter let the President remove a Federal Trade Commission member. Kevin Warsh was sworn in as chair on May 22, 2026.
- *Why it matters:* a grade 12 student asked who steers the Fed will meet these facts outside class.
- *Fix:* add to field 10 and day 8's teacher notes: "Checked 2026-11-14: Fed governors may be removed only for cause. In Trump v. Cook (June 29, 2026) the Supreme Court, 5 to 4, let Governor Lisa Cook stay in office while her case continues, ruling on narrow grounds. The same day, in Trump v. Slaughter, it let the President remove a Federal Trade Commission member, so the Fed's protection is now treated as different from other agencies'. Kevin Warsh became chair on May 22, 2026, succeeding Jerome Powell. Stated as fact, not argued by party."

**U1-4. Exits ask too many instances (minor; LAYER plan; REPEAT yes, exit size).**
- E9 asks for five cases, each with a link and a consequence. **Fix:** one 19th-century and one 20th-century case, the student's choice, with the Civil War card in the key.
- E2 asks for two proposals with four aspects each, plus two classifications. **Fix:** one proposal with goal, role and payer, plus one classification.

**U1-5. Railroad harms named only as "displaced communities" (minor; LAYER plan; REPEAT yes, "Native nations varied").**
- *What is wrong:* the A7 and E9 keys say "harming displaced communities and exploiting workers". The sensitivity study already names the Sicangu Lakota Oyate and the Chinese railroad workers.
- *Fix:* key text: "rail links expanded markets while taking Native nations' lands (for example the Lakota nations') and relying on dangerous, underpaid labor, including Chinese workers on the Central Pacific".

Correct as written:
- The asset arithmetic: $84, $54.60 and $68.25; a loss of $11.75, or 14.69 percent.
- The equilibria: $4 and 50, $6 and 70, $5 and 40.
- FOMC voting: seven governors and five presidents.
- Roosevelt's March 12, 1933 address.
- Cleveland's August 1893 message, with the note that no Fed existed in 1893.
- The rounded S&P series, labelled as fictional approximations.

Not re-checked: the Comptroller's 1893 regional suspension figures. Confirm them at production.

## Unit 2: Tradition and modernity (days 13 to 25)

**U2-1. A1 to A10 overload (moderate; LAYER plan; REPEAT yes, CW1).**
- *What is wrong:* ten items, most asking two or three explanations, get 20 minutes. A2 alone asks for four contributions, and A8 asks for three links plus a goal and a limit. The total is about 40 minutes.
- *Fix:* each of A1 to A10 asks one thing in about 2 minutes:
  - A2: Hughes or Hurston, plus one business or patron.
  - A8: connect two of the Klan, Tulsa and the Great Migration, plus one limit.
  - A10: the three-way match plus one sentence.
  - A1, A4, A5 and A7: drop their second question.
  - Keep A0 at 20 minutes.

**U2-2. B. C. Franklin's 1931 manuscript planned as a closing-claim source (moderate; LAYER plan; REPEAT yes, CW4).**
- *What is wrong:* field 2 lists "Franklin" among the four sources for day 23, and day 19 reads it. The manuscript was unpublished until NMAAHC acquired it in 2015, and Franklin died in 1960. Under United States law an unpublished work is protected for life plus 70 years, so it is in copyright through 2030. The plan says only "rights pending".
- *Fix:* field 10: "Franklin's 1931 manuscript is unpublished and in copyright through 2030: attributed paraphrase from the NMAAHC account, or excerpts only with written permission. For a quoted Tulsa primary source, use the 1921 public-domain press and Red Cross relief records."

**U2-3. Tulsa without a present-tense line (minor; LAYER plan; REPEAT yes, CW2).**
- *Fix:* day 19 teacher note: "Checked 2026-11-14: Viola Ford Fletcher died on November 24, 2025, at 111, leaving Lessie Benningfield Randle as the last known survivor (confirm her status at production). The Oklahoma Supreme Court dismissed the survivors' lawsuit in June 2024. In 2025 Tulsa's mayor announced a goal of raising $105 million for descendants by 2026 (confirm what was raised at production)."

**U2-4. Exits too large (minor; LAYER plan; REPEAT yes, exit size).**
- E18 asks for three yes-or-no claims plus a three-way distinction. **Fix:** two claims plus the quota-against-refugee distinction.
- E21 asks for three cases, each with a date and a concern. **Fix:** two of the three, the student's choice.

**U2-5. Item i has no primary source chosen (minor; LAYER plan; REPEAT new).**
- *What is wrong:* day 16's LGBTQ source is the NYC LGBT Historic Sites page (reference only), and the student-facing records are "still to select".
- *Fix:* field 10: "Select a dated public-domain record before lesson writing, for example a 1920s New York newspaper report or a police record of a Harlem drag ball, framed under values rule c."

**U2-6. Numbering skips A11 (minor; LAYER plan; REPEAT new).** "Collect day 23's independent argument as A12." **Fix:** rename it W23 to match units 3 and 4.

Correct as written:
- The Scopes conviction, reversed on a technicality.
- Buck v. Bell, never formally overruled.
- Lawrence 1912, Boston 1919, and Sacco and Vanzetti (1921 trial, 1927 execution).
- The 1924 act's tribal-property proviso.
- 43 Stat. 153.
- Page (1922) and Coolidge (December 6, 1923).
- Hughes and Hurston texts now in the public domain.
- The A'Lelia Walker site link (the Dark Tower stood where the Countee Cullen library is).
- Day 25's readiness check in its last ten minutes.

## Unit 3: Depression and New Deal (days 26 to 39)

**U3-1. A3 short by about five minutes (minor; LAYER plan; REPEAT yes, CW1).** Eleven matches and an explanation in 8 minutes. **Fix:** A1 17 minutes, A3 11. The total stays at 40.

**U3-2. The Oneida Nation reused as the unit's Native pointer (minor; LAYER plan; REPEAT yes, grade 3 settlement 4 and "Native nations varied").**
- *What is wrong:* field 10 says "Study the Oneida Nation's issue briefs", but unit 2 day 18 already uses the Oneida Nation.
- *Fix:* point to the Confederated Salish and Kootenai Tribes' own pages. They were the first nation to adopt a constitution under the 1934 act, in 1935. Keep the Since Time Immemorial content as written.

**U3-3. The 1930s removals lack a range and an official line (minor; LAYER plan; REPEAT yes, "death tolls and contested counts as a range").**
- *Fix:* day 30 teacher note: "Estimates of people removed to Mexico in the 1930s run from about 400,000 to about 1 million, many of them United States citizens; historians disagree on the count. California apologized in law in 2005 (the Apology Act for the 1930s Mexican Repatriation Program)."
- Confirm the range against Balderrama and Rodriguez at production.

**U3-4. Deposit insurance "today" without a date (minor; LAYER plan; REPEAT yes, CW2).**
- *Fix:* day 36 note: "Checked 2026-11-14 (confirm at production): standard coverage is $250,000 per depositor, per insured bank, per ownership category; insurance does not cover stocks or other investments."

**U3-5. G31 has 10 minutes for a four-relationship, three-scale judgment (minor; LAYER plan; REPEAT new).** The plan intends day 31 to finish day 29's draft, but does not say so. **Fix:** field 5, G31: "completes the evaluation drafted on day 29".

Correct as written:
- Lebergott's unemployment figures (20.1, 14.3 and 19.0), with the work-relief definition.
- America First in 1940 and Lindbergh in 1941, signposted.
- The CIO's 1935 committee told apart from its 1938 congress.
- Social Security's occupational exclusions kept apart from a racial rule, with the disputed intent noted.
- Chapter 26 kept apart from monetarism.
- Readiness on day 25 with the station on day 28.

## Unit 4: Isolation, fascism and the Holocaust (days 42 to 56)

**U4-1. Overload from T3.5 parsed as six required parts (moderate; LAYER plan and skeleton; REPEAT yes, US History I U4-2 and its "research one" settlement).**
- *What is wrong:* MA.USII.T3.5 asks for one event, or one battle, or one conference, from primary sources, and S49 scores that one study. The skeleton made a to f required parts, so day 55 adds A4a to f (about 18 minutes of work in 13). A2 (8 minutes) and A3 (3 minutes for seven labels plus a reason) are also short.
- *Fix:*
  - A4 becomes one sequence item: order six dated cards (Rhineland, Austria and Munich, the pact and Poland, Nanjing, Midway, Yalta and Potsdam), then one sentence on a case the student did not study in depth. 8 minutes.
  - A2 gets 10 minutes and A3 gets 6. A1 stays at 16.
  - Nanjing is still named plainly on day 47 and in E47.

**U4-2. China missing from the map of the Allies (minor; judgment call; LAYER plan; REPEAT new).** The standard lists four Allies. **Fix:** a teacher line and A3 key: "China fought Japan from 1937 and was a major Allied power; it is on the 1942 map though the standard's list omits it."

**U4-3. Special units without present-tense lines (minor; LAYER plan; REPEAT yes, CW2).**
- *Fix:* day 50 note: "Checked 2026-11-14: in early 2025 some Defense Department pages on the Navajo Code Talkers were taken down, and an Air Force training video on the Tuskegee Airmen was dropped; both were restored after objections. Print any federal page on the day it is used. Confirm which Code Talkers are living at production."
- Peter MacDonald's status could not be confirmed this run.

**U4-4. Exits too large (minor; LAYER plan; REPEAT yes, exit size).**
- E50 asks for three accounts plus the Navajo source. **Fix:** two accounts of the student's choice, plus the Navajo source.
- E45 asks for three linked explanations. **Fix:** two, plus who declared war.

**U4-5. Testimony clips under copyright (minor; see CW4).** Gerda Blachmann Wilchfort and the Shoah Foundation's Xia Shuqin clip.

Correct as written:
- The 1935 to 1939 dates.
- Midway (four carriers to one).
- The December 8 and 11 declarations.
- Mussolini 1922 and Hitler 1933.
- Hull (March 23, 1938), the December 17, 1942 declaration and the October 1, 1946 judgment.
- The St. Louis passengers received by four countries.
- Six million Jews murdered, with the other groups named distinctly.
- Readiness on day 41 with stations on 44, 46 and 51.
- Unit 5's item on day 56.

## Unit 5: The home front and the bomb (days 57 to 66)

**U5-1. Assessment overload (moderate; LAYER plan; REPEAT yes, CW1).**
- *What is wrong:* day 65's items need about 46 minutes at the settled rate, against 40. A2d asks for five roles, A2e for two countries and three legal moments, and A3 for four nuclear developments plus the treaty.
- *Fix:*
  - A2d: two roles (one civilian, one uniformed) plus one inequality.
  - A2e: one US and one Canadian detail, plus Korematsu against 1988; 2018 goes in the key.
  - A3: two of the four developments plus the 1963 treaty. W64 already scores the synthesis.

**U5-2. Field 4 names the wrong first day (minor; LAYER skeleton; REPEAT new).** Old: "day 1 opens with the hook". New: "day 57 opens with the hook".

**U5-3. Reteach note names the wrong day (minor; LAYER data; REPEAT yes, CW5).** days.csv day 61. Old: "day 57 flagged". New: "day 56's check flagged".

**U5-4. Exits too big (minor; LAYER plan; REPEAT yes, exit size).**
- E58: Randolph and the pilot against one other role.
- E59: one US and one Canadian detail plus Korematsu against 1988.

**U5-5. Korematsu needs a precise line (minor; LAYER plan; REPEAT yes, CW2).**
- *Fix:* field 10: "In Trump v. Hawaii (2018), an opinion upholding a travel order, Chief Justice Roberts wrote that Korematsu was gravely wrong the day it was decided and has no place in law under the Constitution. Fred Korematsu's conviction was vacated in 1983. Stated as the Court said it."
- Confirm the wording against the opinion at production.

**U5-6. Survivors need a present-tense line (minor; LAYER plan; REPEAT yes, CW2 and CW7).**
- Field 10: "Checked 2026-11-14: Nihon Hidankyo, the survivors' organization, received the 2024 Nobel Peace Prize. Certified survivors fell below 100,000 in 2025 (99,130 at March 31, 2025; average age about 86)."
- Add Korean and other non-Japanese victims and survivors to the sensitivity study.

**U5-7. Museum memory on day 63 (minor; LAYER plan; REPEAT yes, US History I U9-5).** Teacher line: "Checked 2026-11-14: in August 2025 the White House announced a review of Smithsonian exhibition texts. Print any museum page on the day taught and date it."

**U5-8. Unlabelled captions (minor; CW3).** E57 to E63.

Correct as written:
- About 120,000 incarcerated.
- Order 8802, with the march called off.
- Korematsu upheld exclusion, not every detention measure.
- Public Law 100-383 (August 10, 1988) and Canada's 1988 redress.
- WASP pilots served as civilians.
- The Franck Report's demonstration proposal.
- The 1963 treaty's limits.
- The proposed 1995 exhibit kept apart from the one that opened.
- Readiness on day 56 with the reteach on day 61.

## Unit 6: The Cold War at home and abroad (days 67 to 83)

**U6-1. Assessment overload (moderate; LAYER plan; REPEAT yes, CW1).**
- *What is wrong:* day 82 holds about 55 minutes of work in 40.
- *Fix:*
  - A1 keeps source A's purpose and limit and one comparison (Marshall). NATO, the Warsaw Pact and Korea become three 1-minute date items.
  - A2 cuts to three flashpoints of the student's choice.
  - A7 keeps the roots, the evidence against guilt by association and the Lavender Scare. R80 already scores Smith and Kameny.
  - The freed minutes go to A5 and A6 (14 together).

**U6-2. Present-tense lines (minor; LAYER plan; REPEAT yes, CW2).**
- Day 80: "In 2009 the director of the Office of Personnel Management apologized to Frank Kameny. On January 9, 2017 the Secretary of State apologized for the department's past firings of gay employees. Congress has passed no formal apology."
- Day 78: "The Menominee were restored in 1973 and the Klamath Tribes in 1986, without their reservation land. In 2024 the four lower Klamath River dams were removed after decades of tribal advocacy, and salmon returned that fall."

**U6-3. Exits too big (minor; LAYER plan; REPEAT yes).**
- E71: two of three flashpoints.
- E77: one place within the city or suburb, plus one link to the rural fringe.

**U6-4. Unlabelled captions (minor; CW3).** E67, E68, E72 and E76 to E80.

Correct as written:
- Kennan against Novikov (1946).
- NSC-68 (April 7, 1950), reserved for the assessment.
- NATO 1949, the Warsaw Pact 1955 and the 1953 armistice.
- NASA and the education act, both 1958.
- Shelley (1948), and the GI Bill's practical exclusions.
- Smith 1950, the censure 1954 and Kameny's firing in 1957.
- Termination kept apart from relocation, and the Since Time Immemorial role play replaced.
- Readiness on day 66 with the reteach on day 68.

## Unit 7: The civil rights movement and its laws (days 86 to 102)

**U7-1. Affirmative action stops at 2023 (moderate; LAYER plan; REPEAT yes, CW2).**
- *What is wrong:* days 95 and 96 and A8 stop at the 2023 admissions ruling, and Executive Order 11246 has since been revoked.
- *Fix:* field 10 and the day 95 notes: "Checked 2026-11-14: on January 21, 2025 an executive order revoked Executive Order 11246 (1965), ending affirmative action plan duties for federal contractors. Duties for veterans and people with disabilities under separate laws remain. Stated as fact, not argued by party."

**U7-2. Assessment overload (moderate; LAYER plan; REPEAT yes, CW1).**
- *What is wrong:* day 101 has nine tasks in 42 minutes. A8 asks for six cells in 5 minutes, A6 for four dated events with their demands in 5, and A2 for seven elements in 4.
- *Fix:*
  - A8 keeps fair housing, 2023, Shelby, Callais and Obama (7 minutes). R96 already scores the disparity fields.
  - A6 becomes four 1-minute date items plus one demand explained (6 minutes).
  - A2 keeps the three organizations. R87 scores the roots.
  - A1 drops to 8 minutes.

**U7-3. Claudette Colvin died on January 13, 2026 (minor; LAYER plan; REPEAT yes, "current official facts").** Day 90 teaches Browder v. Gayle without its plaintiffs. **Fix:** a day 90 line naming Aurelia Browder, Susie McDonald, Claudette Colvin and Mary Louise Smith, with: "Colvin was arrested at 15 in March 1955 and died on January 13, 2026, at 86."

**U7-4. Exits too big (minor; LAYER plan; REPEAT yes).**
- E95: Shelby and Callais only; 2023 moves to E96.
- E92: two events plus the 1968 point.

**U7-5. Unlabelled captions (minor; CW3).** E86, E88, E89, E95 and E97.

Correct as written:
- Callais (April 29, 2026, 6 to 3), matching US History I U8-2.
- Shelby struck down section 4(b) only.
- Mendez was decided below the Supreme Court.
- Katzenbach (1966) reserved for the assessment.
- The census shares and their limits.
- METCO (1966) and the June 21, 1974 Boston finding.
- Milliken, Keyes and Swann told apart.
- Boston taught as a national case beside three other regions (bar item 13).
- King's copyright flagged.
- Day 102's readiness check for unit 8.

## Unit 8: Presidents and the war in Vietnam (days 103 to 113)

**U8-1. No day table for days 103 to 109 (moderate; LAYER plan; REPEAT new).**
- *What is wrong:* s08 has no U3 to U11 fields and no minutes for days 103 to 109.
- *Why it matters:* a day writer cannot see the teaching minutes, the model holder, the withdrawal day, or how day 104's reteach station fits.
- *Fix:* add a "Section 8.1" block with a U6 day table in s07's format, every row totalling 50 minutes. Show day 104's ten-minute station in place of the warm-up and the first guided minutes. Add U9 (supports) and U10 (two rooms).

**U8-2. Exits check recall, not a skill on a source (moderate; LAYER plan; REPEAT yes, bar item 7).**
- *What is wrong:* E103 to E109 are yes-or-no fact corrections.
- *Fix:* each exit uses a short unseen passage and asks for a sourced correction with a reason. For example, E104: "From the October 22, 1962 address, name two options Kennedy describes and why he chose the quarantine."

**U8-3. B112 overload, with T5.1's "such as" list parsed as parts (moderate; LAYER plan and skeleton; REPEAT yes, CW1).** 18 minutes for about 23 minutes of work.
- *Fix:*
  - Johnson: two of the four programs, plus the tension with escalation.
  - Nixon: China and the Watergate tape; arms control goes in the key.

**U8-4. No immigration-status line (minor; LAYER plan; REPEAT yes, US History I U7-4).** Fields 9 and 10: "No student is asked about their own or their family's immigration status or story, in class or on any page."

**U8-5. Nixon address cited from the Nixon Foundation (minor; LAYER plan; REPEAT yes, "no campaign or party sources" and "exact citations").** Cite the Public Papers text at the Nixon Presidential Library or the American Presidency Project instead.

Correct as written:
- Kent State (May 4, 1970; four killed, nine wounded).
- The 26th Amendment kept apart from the draft.
- 1972 kept apart from 1979.
- Saigon fell under Ford.
- The 1965 act ended national-origins quotas.
- My Lai named plainly.
- Readiness on day 102 with the reteach on day 104.
- Unit 9's items on day 113.
- Vietnamese, Hmong and Cambodian experiences kept distinct.

## Unit 9: Movements for rights since the 1960s (days 114 to 123)

**U9-1. Huerta's death given as a cryptic line, and Steinem's death missing (moderate; LAYER plan; REPEAT yes, CW2, and grade 1's Huerta settlement).**
- *What is wrong:* field 10 says only "Huerta's foundation reports October 28, 2026".
- *Fix:* replace that line with: "Dolores Huerta died on October 28, 2026, at 96; Gloria Steinem died on September 3, 2026, at 92. Both are taught in the past tense. In March 2026 Huerta said publicly that Cesar Chavez had sexually assaulted her decades earlier. This is not a unit topic; if a student raises it, the teacher states it once as her public account, and Chavez's role in the movement is still taught from the record."
- Add Huerta's own words to the sensitivity study.

**U9-2. Survey items overloaded (moderate; LAYER plan; REPEAT yes, CW1).**
- *What is wrong:* each survey item gets 3 minutes but asks for three to five corrections plus an explanation.
- *Fix:*
  - Each item asks for two corrections and one sentence of evidence (about 4 minutes); every option a to f keeps one item.
  - Day 122 becomes: orientation 5, A122 22, survey 20, marking 3.

**U9-3. A122's "document from a movement" is a president's statement (moderate; LAYER plan and data; REPEAT new).**
- *What is wrong:* the transfer source is Bush's ADA signing statement, or Nixon's 1970 message. Both are government responses, not movement documents.
- *Fix:*
  - Field 5, "A122 source reservation": add a reserved excerpt of about 120 words by a movement member, from the public hearing record. For Bush: disability advocates' 1989 ADA testimony. For Nixon: Earth Day organizers' 1970 testimony. Cite each exactly; verify at production.
  - The president's text stays as the "result" document.
  - The context card reports context only.

**U9-4. Options a and b stop before the 2025 and 2026 rulings (moderate; LAYER plan; REPEAT yes, CW2).**
- *Fix:* field 10: "Checked 2026-11-14: in United States v. Skrmetti (June 18, 2025) the Supreme Court upheld Tennessee's ban on certain medical treatments for transgender minors. In West Virginia v. B.P.J. and Little v. Hecox (June 30, 2026), 6 to 3, it held that neither Title IX nor the Equal Protection Clause requires states to let transgender girls play on girls' teams. Stated as decided (values rule a); not argued by party; no student is asked about identity."
- The Title IX recodification of September 29, 2026 is already recorded correctly.

**U9-5. Options c and d lack dated lines (moderate; LAYER plan; REPEAT yes, CW2).**
- *Fix:* field 10: "Checked 2026-11-14: in February 2026 the EPA rescinded its 2009 greenhouse gas endangerment finding and the federal vehicle greenhouse gas standards; the rescission is challenged in the D.C. Circuit. Sackett v. EPA (2023) narrowed which wetlands federal water law covers. In June 2026 the Education Department agreed to move day-to-day management of special education grants and monitoring to HHS; IDEA's guarantee of a free appropriate public education is unchanged in law, and the move is contested."

**U9-6. Massachusetts as the wetlands case every student answers (minor; LAYER plan; REPEAT yes, grade 3 settlement 3).** In S-d, replace "Massachusetts wetland statute" with "federal wetland permits under the 1972 water law (with one state's wetland act as an example)".

**U9-7. Wounded Knee 1973 with no present-day nation (minor; LAYER plan; REPEAT yes, "Native nations varied").** Option f look-for: "the 1973 occupation took place on the Pine Ridge Reservation of the Oglala Sioux Tribe, which governs there today". Take it from the tribe's own pages, and add those pages to the sensitivity study.

**U9-8. Copyrighted accounts (minor; CW4).**

**U9-9. Voice (minor; CW6).**

Correct as written:
- Dobbs overruled Roe and Casey, not Obergefell.
- The Davis cert denial (November 10, 2025).
- O'Connor (1981; died 2023).
- IDEA renamed in 1990.
- Alcatraz 1969, and Wounded Knee 1973 kept apart from 1890.
- Opposition taken from dissents and testimony, not party pages.
- The Suquamish Tribe is not reused elsewhere.
- Readiness on day 113, and the capstone choice on day 123.

## Unit 10: Liberals, conservatives and the end of the Cold War (days 124 to 134)

**U10-1. The two traditions do not have equal movement sources (moderate; LAYER plan; REPEAT new).**
- *What is wrong:* liberalism rests on Johnson only. Day 127's conservative voices rest on a Schlafly interview that is reference only, and campaign speeches are out under the settled "no campaign or party sources" rule.
- *Fix:* field 10: use public-domain movement voices from the Congressional Record or hearings for each side, for example a union leader's testimony and a conservative senator's floor statement, cited exactly. Friedman, Buckley, Harrington and Schlafly appear as attributed paraphrase only.

**U10-2. B133 overloaded, with a strand outside the standard (minor; LAYER plan; REPEAT yes).**
- *What is wrong:* B133 asks for deregulation, which T5.3 does not name.
- *Fix:* drop deregulation from B133; it is still taught on day 128 and usable in W132. Move the 5 review minutes to B133. New split: directions 3, reading 9, A 12, B 17, C 9.

**U10-3. Iran-Contra not named (minor; judgment call; LAYER plan; REPEAT new).** Add one teacher sentence to field 10 from the State Department's Central America milestone: "The Iran-Contra affair (1985 to 1987) tested the legal limits of anti-communist policy."

**U10-4. Frame sensitivity list has no unit 10 entry (minor; LAYER plan (frame); REPEAT new, CW7).** frame.md, "Sensitivity reads": add "unit 10, Iranian American, Afghan, Nicaraguan and Polish community histories, and both traditions' own sources". This copies the plan's own list.

**U10-5. Retrieval assumes Economics (minor; LAYER process; REPEAT new).** For a student who skips Economics, the Soviet collapse was last met two grades back. The plan prints the task for everyone, so s10 needs no change. The point goes to the structure pass.

Correct as written:
- Carter died December 29, 2024.
- Johnson's State of the Union of January 17, 1968.
- The strike remarks of August 3, 1981.
- The INF remarks of 1987.
- The Great Inflation kept apart from tax policy.
- 1989 kept apart from 1991.
- Day 134's readiness check, with its minutes adding to 50.

## Unit 11: The United States since 1990 (days 135 to 145)

**U11-1. A144 and B144 overloaded (moderate; LAYER plan and skeleton; REPEAT yes, CW1).**
- *What is wrong:* B144 asks for about 30 minutes of work in 24. A144 asks for six elements in four sentences.
- *Fix:*
  - A144: "one trend of the student's choice (computer and internet, or genome) with one consequence or limit, then one change and one continuity in immigration". T5.5 says "such as".
  - B144: keep the surveillance judgment and counterclaim, the attacks in one sentence, and one outcome per war.
  - Hamdi and Boumediene move out of the sitting. They are not named parts, and W143 already scores them.

**U11-2. Surveillance and ACA lines are unverified or cryptic (moderate; LAYER plan; REPEAT yes, CW2).** Replace both with:
- "Checked 2026-11-14: Section 702 of FISA, reauthorized in April 2024, lapsed on June 12, 2026 after short extensions failed; collection under certifications approved in March 2026 continues into 2027. Confirm any later reauthorization at production."
- "The Affordable Care Act remains law; its enhanced premium tax credits expired on December 31, 2025. Confirm any later change at production."
- Add a COVID-19 death figure from the CDC, with its date, confirmed at production.

**U11-3. Iraq outcome card rests on a British inquiry (minor; LAYER plan; REPEAT new).** Use the Iraq Survey Group's 2004 key findings, a federal record, cited exactly. The 2016 UK inquiry stays optional.

**U11-4. "First post-Cold War use of force" is loose (minor; LAYER data and frame; REPEAT new).** Panama (December 1989) came earlier. In days.csv day 140 and the frame's unit 11 row, change "as the first post-Cold War use of force" to "fought as the Cold War ended".

**U11-5. Day 139 lacks a dated self-government line (minor; LAYER plan; REPEAT yes).** "Haaland v. Brackeen (2023) upheld the Indian Child Welfare Act." Use the present tense for the Cherokee Nation's courts and council.

**U11-6. Veterans' voices missing from the sensitivity study (minor; CW7).** Add the Library of Congress Veterans History Project.

Correct as written:
- The 9/11 Commission's finding on Iraq.
- Hamdi (2004) and Boumediene (2008) taught as distinct.
- Bush's 2006 and Obama's June 2, 2015 statements, one from each party.
- PCLOB 2014.
- The emergency's end on May 11, 2023.
- Genome dates 2003 and 2022.
- Readiness on day 134 with the station on day 140.
- The ELA 12 calendar: source list day 135, a second contrary source in day 143's exit, draft day 145.

## Unit 12: Capstone (days 148 to 160)

**U12-1. Day 156's outside audience cannot be run by one teacher (moderate; LAYER plan; REPEAT new).**
- *What is wrong:* the plan needs six parallel panels with outside listeners.
- *Why it matters:* a D4.3 score would rest on school logistics (C14).
- *Fix:* field 5, "Presentation evidence":
  - The beyond-class audience is required for one form only. The default is the printed briefing, sent through the school to a named reader.
  - Peer panels are the contrasting audience for the talk.
  - Replace "mark the outside-audience criterion pending, not met" with "the briefing's delivery record meets the outside-audience criterion".

**U12-2. Standalone paper has no writing time (moderate; LAYER plan; REPEAT yes, US History I U4-4).** Field 5, "Collection and time": "Standalone: day 147's review ends with an outline checkpoint; the draft is written mostly outside class, about three hours across days 148 to 153; where homework is not possible, the briefing of equal weight is the product."

**U12-3. Codes mislabelled (minor; LAYER data and plan; REPEAT new).**
- days.csv day 157 note: add "Practised: D4.7.9-12, D4.8.9-12".
- Exits 148 to 150: change Evidence to "D3.1 to D3.4 (practised)".

**U12-4. Museum source named loosely (minor; LAYER plan; REPEAT yes, "exact citations").** Use the Marian Anderson Historical Society's own name, as its page states.

Correct as written:
- Executive Order 9981 (July 26, 1948) and Freedom to Serve (1950), both federal.
- U159 and E152 labelled as written for the course.
- The action scored on reasoning, not position.
- The ten-day path keeps both critiques, both forms, the action, the assessment and the respond day.
- The ELA 12 pairing (talk day 156, paper day 158, no second draft).

## Course flow and the start-of-year check

Each unit picks up what the last promised:
- Unit 1's chain returns on days 26, 126 and 138.
- Unit 2's day 25 holds unit 3's readiness check.
- Unit 3 hands to course-level check 1 and day 41's check for unit 4.
- Day 56 holds unit 5's bomb item, and day 66 holds unit 6's.
- Unit 6's flashpoint map runs through units 8 and 10.
- Day 102 holds unit 8's check and day 113 unit 9's.
- The capstone question is chosen on day 123, the source set grows on days 128 and 135, and the counterclaim sources come on days 132 and 143.
- Readiness days match the scope and sequence (25, 41, 56, 66, 102, 113 and 134).

The breaks:
- Unit 1's start-of-year check sits before day 1 (U1-1).
- The frame's seam table names the wrong days (CW5).
- Unit 8 has no day table (U8-1).

Unit 1 has a readiness row, so the lead rule puts the check in day 1's last ten minutes. "None needed; retrieval only" applies to no unit 1 here.

## Settled by the expert

| Question | Ruling | Where it binds |
|---|---|---|
| Unit 1's readiness check | Lead rule 2026-11-14 applied, as in US History I: the last ten minutes of day 1, after the hook; E1 moves before it; all four items are retaught at day 2's station, with overflow on day 3. | s01 fields 4 and U6; days.csv days 1 and 2; scope-and-sequence.md line 55 and the readiness table |
| "One of" and "such as" lists (T3.5, T5.1, T5.5, T1.9b, T1.10) | US History I's "research one" ruling extended: the chosen case is assessed in depth; the rest are surveyed, at most one short item or a sequence grid on the sitting. | s01 A2 and A7, s04 A4, s08 B112, s11 A144 |
| Parts already scored by a product | When R, S, W or P work scores a part, the sitting asks at most a 1-minute recall or a one-sentence item on it. | s01 A8, s06 A7, s07 A2 and A8, s11 B144 |
| Exit size | Settled earlier and applied: at most two instances, the student picks the rest. | s01, s02, s04 to s07 |
| Made-up captions | Every caption or display to be corrected is labelled on the page as written by Curio Class for practice. | s04 to s08 U3 |
| Unpublished and copyrighted texts | Rights run from the author's death for unpublished work (life plus 70); excerpt only with permission, otherwise attributed paraphrase. Extends US History I's "modern historians" row. | s02 (Franklin), s04, s09, s10 |
| People who died in 2025 or 2026 | Past tense with the date. A 2026 public statement (Huerta's) is stated once as the person's account if raised, not a unit topic. Grade 12 application of the grade 1 Huerta settlement. | s02 (Fletcher), s07 (Colvin), s09 (Huerta, Steinem) |
| 2025 to 2026 law and events | Settled earlier and applied: a dated teacher line, stated as fact, never argued by party (Trump v. Cook and Warsh; EO 11246; Skrmetti, B.P.J. and Hecox; the endangerment finding; Section 702; ACA credits). | s01, s07, s09, s11 field 10 |
| Survey items on an assessment day | Each surveyed option keeps one item: two corrections and one evidence sentence, about 4 minutes. | s09 field 5 |
| A movement transfer document | A movement-authored public record sits beside the government's "result" record; the teacher's card gives context only. | s09 A122 |
| The capstone's beyond-class audience | Met by one form, by default the printed briefing routed through the school; peer panels are the contrasting audience. | s12 field 5 |
| Unit 3's Native pointer | The Confederated Salish and Kootenai Tribes, not the Oneida Nation (used in unit 2). Applies grade 3 settlement 4. | s03 field 10 |
| Contested counts | Settled earlier and applied: a range with its source (the 1930s removals). | s03 day 30 |
| China on the Allied map | Shown and keyed as an Allied power, though the standard's list omits it. | s04 A3 and day 46 |

## For the fixer

In order. "Old" is the exact current text where short.

1. s01 field 4. Old: "**Given:** the start-of-year check, before day 1 (served in unit 1, which defines it)." New: "**Given:** day 1, the last ten minutes, after the hook (lead rule 2026-11-14)." Old: "Give these four items in ten minutes a few days before opening." New: "Give these four items in the last ten minutes of day 1; E1 comes in the five minutes before." Old: "Item 1 receives this sequence immediately after day 1's hook. On day 2, combine overlapping gaps from items 2 to 4" New: "On day 2, combine the gaps from items 1 to 4".
2. s01 U6 day 1 row: hook 8; teach choice 10; compare 17; E1 5; readiness check 10. Field 2 carried skeleton line: "in the start-of-year check before day 1" to "inside day 1's readiness check".
3. days.csv day 1: `assess` = readiness. Note, old: "is served by the start-of-year check before this day:" New: "is given in this day's last ten minutes, after the hook:". Day 2 note, old: "students who missed the start-of-year check's readiness items" New: "students day 1's readiness check flagged".
4. scope-and-sequence.md line 13: "and for unit 1 in the start-of-year check" to "and for unit 1 in the last ten minutes of day 1, after the hook". Readiness table, unit 1: "Start-of-year check: ss8-public-budget" to "Day 1, last ten minutes: ss8-public-budget". Line 55: "the start-of-year check, before day 1," to "the last ten minutes of day 1, after the hook,".
5. s01: U1-2 (new item times), U1-3 (Fed line), U1-4, U1-5.
6. s02: U2-1, U2-2 (Franklin rights line), U2-3, U2-4, U2-5, U2-6 (A12 to W23).
7. s03: U3-1 (A1 17, A3 11), U3-2 (CSKT), U3-3, U3-4, U3-5.
8. s04: U4-1 (A4 as a sequence item; A2 10, A3 6), U4-2, U4-3, U4-4, CW3 line, CW4 line.
9. s05: U5-1, U5-2, U5-4 to U5-7, CW3 line; days.csv day 61 (U5-3).
10. s06: U6-1 to U6-3, CW3 line; days.csv day 68 reteach note to name day 66's check.
11. s07: U7-1 to U7-4, CW3 line.
12. s08: U8-1 (add the section block), U8-2, U8-3, U8-4, U8-5, CW3 line; days.csv day 104 note to name day 102's check.
13. s09: U9-1 to U9-7, CW4 line.
14. s10: U10-1 to U10-3, CW4 line; frame.md sensitivity list (U10-4).
15. s11: U11-1 to U11-3, U11-5, U11-6; days.csv day 140 and frame.md unit 11 row (U11-4).
16. s12: U12-1, U12-2, U12-4; days.csv day 157 and the exit table (U12-3).
17. frame.md Seams table: "on day 42", "on day 57", "on day 67", "on day 103", "on day 114" to "in day 41's last ten minutes", "in day 56's", "in day 66's", "in day 102's", "in day 113's" (CW5). frame.md sensitivity list: add unit 1 (tenant and railroad-worker histories, the Sicangu Lakota Oyate, freedpeople's testimony, as s01 lists) and unit 5's Korean survivors.
18. CW6 voice: at section-plan time, not now.

## For the structure pass

- unit_skeleton.py parses "one of" lists (MA.USII.T3.5) and "such as" lists (T1.9b, T1.10, T5.1, T5.5) into required parts. The US History I report found the same with "research one" (T4.2, T6.3, T7.2, T7.5). The skeleton should mark them "choose one; survey the rest".
- unit_skeleton.py writes "day 1 opens with the hook" in field 4 for every unit (s05). It should name the unit's first day. Its unit 1 carried line says "start-of-year check before day 1" where the frame says "day 1's readiness check".
- The template has no "Dated lines (checked YYYY-MM-DD)" sub-field (proposed in US History I). It would have caught the cryptic Huerta, ACA and Section 702 lines.
- The template should require a U6 day table for every section, so a plan like s08 cannot leave days out. A gate in plan.py could check that every unit day has a minute row.
- The readiness rule counts optional half-year courses (Economics; Government for unit 7) as "earlier this year". Proposed rule: an optional course does not reset the readiness clock, and the unit prints the items for every student. s10 already does this.
- days.csv reteach notes on days 61, 68 and 104 name the unit's first day as the check day. The writer copied the frame's seam wording; a gate could check that a reteach note names a day with `assess` = readiness.
- A gate could require one frame sensitivity entry per unit (units 1 and 10 have none).
- D4.7 and D4.8 have no own-word lines. This is known for D4.3 to D4.5; add them when the action day is coded.

## For Cory

None. Every finding fits inside the existing days, scope and standards.

## For the source list

New this run: Trump v. Cook and Trump v. Slaughter (June 29, 2026); Warsh's swearing-in (May 22, 2026); the Fletcher obituary (November 2025); West Virginia v. B.P.J. and Little v. Hecox (June 30, 2026); the Title IX recodification (Federal Register 2026-19929); the EPA rescission of the endangerment finding (February 2026); the Section 702 lapse (June 2026); the special education agreement with HHS (June 2026); the Huerta and Steinem obituaries (2026); Colvin's obituary (January 2026); and nippon.com's hibakusha figures (2025).

## Sources (web checks, November 14, 2026)

- Trump v. Cook: https://www.faegredrinker.com/en/insights/publications/2026/6/supreme-court-decides-trump-v-cook and https://www.everycrsreport.com/reports/LSB11449.html
- Warsh sworn in: https://newsonair.gov.in/kevin-warsh-takes-oath-as-chairman-of-us-federal-reserve/ and https://www.deseret.com/politics/2026/05/22/president-trump-clarence-thomas-federal-reserve-kevin-walsh-interest-rates/
- Tulsa, Fletcher's death and the lawsuit: https://www.nbcnews.com/news/nbcblk/1921-tulsa-race-massacre-survivor-viola-ford-fletcher-dies-age-111-rcna245942
- Navajo Code Talkers (living status not confirmed): https://www.ksl.com/article/news/us/navajo-code-talker-samuel-sandoval-dies-3-left-from-group/50449458
- Callais: https://www.everycrsreport.com/reports/LSB11431.html
- Colvin: https://www.pbs.org/newshour/politics/claudette-colvin-who-helped-spark-civil-rights-movement-by-refusing-to-move-bus-seats-dies-at-86
- Executive Order 11246 revoked: https://www.faegredrinker.com/en/insights/publications/2025/1/president-trump-revokes-executive-order-11246
- Hibakusha figures: https://www.nippon.com/en/japan-data/h02464/
- Lavender Scare apologies: https://www.npr.org/sections/thetwo-way/2017/01/09/508966318/state-department-apologizes-for-decades-of-anti-lgbt-discrimination
- Klamath dams: https://kvia.com/cnn-other/2024/09/01/the-largest-dam-removal-project-in-the-us-is-completed-a-major-win-for-indigenous-tribes/
- Smithsonian review: https://www.goodmorningamerica.com/news/story/white-house-conduct-review-smithsonian-museum-exhibitions-ensure-124592673
- Huerta: https://thegrio.com/2026/10/28/dolores-huerta-civil-rights-labor-leader-dies-96/ and https://www.aarp.org/events-history/dolores-huerta-obit-united-farm-workers/
- Steinem: https://axios.com/2026/09/03/gloria-steinem-dies-92-feminist-icon
- B.P.J. and Hecox: https://constitutioncenter.org/blog/supreme-court-allows-state-laws-regulating-transgender-athletes
- Title IX recodification: https://www.federalregister.gov/documents/2026/09/29/2026-19929/recodification-of-title-ix-rules
- Endangerment finding: https://www.morganlewis.com/pubs/2026/02/epa-rescinds-2009-endangerment-finding-eliminates-federal-vehicle-greenhouse-gas-standards
- Special education to HHS: https://www.disabilityscoop.com/2026/06/16/ed-department-strikes-deal-to-offload-special-education/32051/
- Section 702: https://www.opb.org/article/2026/06/13/fisa-702-a-key-u-s-spy-tool-has-lapsed-now-what
- ACA credits: https://www.healthaffairs.org/content/forefront/extending-enhanced-premium-tax-credits-things-stand

From memory, not re-checked this run, marked "confirm at production" above:
- the Trump v. Hawaii wording on Korematsu;
- Skrmetti (2025), Sackett (2023) and Brackeen (2023);
- the 1930s removal range and the California 2005 apology act;
- the FDIC coverage figure;
- the 2025 Defense Department page removals;
- the Comptroller's 1893 figures;
- the CDC COVID-19 count;
- the Iraq Survey Group findings.
