# Fixes: social-studies-grade-3 unit plans, 14 November 2026

The fixer applied two reads to docs/courses/social-studies-grade-3/s01.md to s07.md:

- the expert read, docs/reviews/plan-social-studies-grade-3-2026-11-14.md;
- the Codex read, docs/reviews/plan-social-studies-grade-3-codex-2026-11-14.md.

The expert's "For the fixer" list went first, in its order, and the Codex findings came after it.

Gate results:

- `python -X utf8 scripts/unitplan.py check social-studies-grade-3`: every unit passes (s01 to s07).
- `python -X utf8 scripts/sequence.py check social-studies-grade-3`: 0 failures. It was run because days.csv was edited.
- Day count and unit totals are unchanged.

## Settled rules applied in every unit

- **Assessment size.** Each 30-minute assessment now holds about eight prompts, and each prompt asks one thing. No more than three source sets are read aloud. Every other code part is judged from a saved product named in its row, so no part is asked twice and none is dropped (expert settled row 2).
  - The assessment days are 23, 47, 67, 88, 105, 120, 135 and 159.
  - Day 23 has nine prompts. Its two map prompts stay separate because they use different maps, and joining them would make one prompt ask two things.
- **Exit tickets.** Every exit ticket is now one question. Any further part of the day's task moved into that day's practice. Products collected on a day are labelled "Retained evidence, not an exit".
- **Tennessee rows.** Every Tennessee row now reads: "Not yet compared; the 2024 PDF on tn.gov refuses automated reading." s05 also keeps the French and Dutch map labels on day 94.
- **Made-up texts.** Made-up cases are labelled as made up. This applies to s03 (A, C and D), s04, s07 and the s07 day 160 task.
- **"?" faults.** All "?" characters that stood for quotation marks are restored; they were all in s04. A search across s01 to s07 and frame.md finds none left.
- **Writing rules.** No em dashes, and "Curio Class" is always written in full. The gate checks both.

## Findings applied

### s01, unit 1

- **1.4 voice pass.** s01 was rewritten in plain full sentences. It now has 1,112 counted words.
- **1.3 start-of-year check.** Field 4 now runs the check in the last ten minutes of day 1, after the hook. The reteach for Gap H is on day 2. The day 1 rows in days.csv and in the day list now match.
- **1.1 assessment size.** Day 23 now has nine prompts. The D1 parts are judged from the day 2 and day 20 records.
- **1.2 own place.** Q4 and Q5 now ask about the class's own region. The New England ring item was removed. Massachusetts and New England are worked examples only.
- **1.5 nation repeated in unit 4.** P1 and P2 use the Elwha River restoration in place of the Penobscot, from the National Park Service Elwha pages and the Lower Elwha Klallam Tribe's own page. The Penobscot stay in unit 4 only.
- **1.6 day 1 biography.** The hook now uses a local biography chosen by the teacher. The fallback is a card on Olmsted and the Back Bay Fens.
- **1.7 map already seen.** Q1 now uses a town map that was not used on days 7 to 9. The familiar map is judged from day 10.
- **Other.** The error register was reworded. The stale "Later plans remain unwritten" line was removed, which also covers Codex finding 2.

### s02, unit 2

- **2.1 assessment size.** Day 47 now has eight prompts over three packets: the local record, the own-state constitution card and the class decision record. These parts are judged from earlier records:

  | Part | Judged from |
  |---|---|
  | Civ.4 | day 34 |
  | The national part of Civ.3 | the day 41 card |
  | Civ.6 | day 36 |
  | Civ.11 | day 37 |
  | Civ.7, Civ.9 and Civ.10 | days 38 to 40 |
  | The Menominee part of Civ.5 | day 43 |
  | D1.1 and D1.2 | day 26 |
  | D1.4 | day 44 |

- **2.2 Massachusetts cases.** The Lexington and Boston budget records are now teaching material only. The local record has a Boulder council reserve.
- **2.3 living officeholder.** The Joe Pato biography and its campaign-page source line were removed. Day 35 now uses a documented historical local service biography chosen by the teacher. The fallback card is listed under Still to make.
- **2.4 Menominee constitution.** The tribe's Constitution and Bylaws were read and the key now matches them:
  - Article III gives the Legislature both legislative and executive powers.
  - Article IV sets up the Legislature.
  - Article V sets up the Judiciary.
  - The constitution was ratified in 1977 and revised in 1991, after the Restoration Act of 1973.

  The source line now cites the constitution PDF. The note about a conflicting adoption date was reduced to "No Menominee adoption year is assessed."
- **2.5 field 4 contradiction.** "A few days before opening" was deleted.
- **Other.** The San Marino caveat ("often called") was added to the note on the oldest constitution. Field 3's stale "unwritten" line was replaced.
- **Codex finding 4.** A supporting-question record was added on day 26.

### s03, unit 3

- **3.1 assessment size.** Day 67 now has eight prompts. D2.Eco.10 is judged from the day 66 savings record, now labelled retained evidence. D1.1 is judged from day 49 and D1.2 from day 50.
- **3.2 flour as a natural resource.** "Flour" became "wheat from a farm" in days.csv day 51, in frame.md line 143 and in the day list.
- **3.3 traders' words.** The Techiman traders' words are now credited to the Daily Graphic article of 24 June 2023. Owusu-Mensah's words are quoted there; Appiah's concerns are reported, not quoted. Field 10 names the article and the assembly's Facilities Record of November 2024. The decongestion notice is marked "date and terms to confirm before use".
- **Exits (C3).** All exits are one question.
- **Codex finding 4.** A supporting-question record was added on day 50.

### s04, unit 4

- **4.4 "?" faults.** The quotation marks in the sample table were restored first.
- **4.1 Aquinnah at the centre.** B is now a Narragansett Record, and A was updated to match. The Aquinnah Wampanoag were removed from unit 4. The worked Local Homeland and Contribution Records are now the Penobscot.
- **4.3 day 88 too heavy.** Day 88 now has eight prompts over three source sets. D1.1 is judged from the day 72 exit.
- **4.2 regional editions.** A "Regional editions" paragraph was added, covering the Northeast, Southeast, Midwest, Southwest and West. The four editions other than the Northeast are listed under Still to make.
- **Codex finding 4.** A supporting-question record was added on day 72. Day 86 is now retained evidence.

### s05, unit 5

- **5.1 one colony only.** The day 118 closing claim now uses Winslow's treaty account (Plymouth) and the Pamunkey Indian Tribe's history (Jamestown), in place of Aquinnah History. On day 120:
  - Q1: the student chooses one of the three leader pairs.
  - Q2: the war of 1622 from both sides, using the Waterhouse report and the Pamunkey account.
  - Q6: the ports of Salem and New Amsterdam, which are in two different colonies.
  - Q8: the claim must draw on two colonies, at least one of them not Plymouth.
  - Dossier B swaps its Massachusett and Sipayik cards for a St. Augustine card (Seloy) and a Jamestown card (Pamunkey).
  - Massachusetts Bay schooling is now a worked example on day 108.
- **5.2 assessment size.** Day 105 now has three prompts (M1 to M3). MA.3.T3.3 is judged from the day 95 and 96 exits, and MA.3.T4.1 with parts a to c from the day 100 to 103 records. Day 120 now has eight prompts (Q1 to Q8). These parts are judged from saved records:

  | Part | Judged from |
  |---|---|
  | The timeline | day 119 |
  | Puritan migration and its effects | day 106 |
  | The Winthrop leadership part | day 107 |
  | Housing and schooling | day 108 |
  | Continuity | day 110 |
  | Fishing and shipbuilding | day 113 |
  | D2.Geo.7 | day 116 |
  | D1.1 | day 90 |
  | D1.4 | day 117 |

  The first-half codes are judged from day 105 and its records. Any child who scored 0 gets one spoken prompt in day 119's review.
- **5.3 day 90 hook.** Day 90 now opens on the St. Augustine shore and the Florida Museum account of Seloy. Plymouth comes in its turn.
- **Codex finding 6, assessment size.** Covered by the 5.2 changes; see Disagreements.
- **Codex finding 7, Puritan leadership.** The Winthrop part (Winthrop's governing beside Metacom's defence of his people) is a retained record on day 107, judged for MA.3.T5.1. It does not imply that the two leaders negotiated.
- **Codex finding 8, the English account of 1622.** The account is now named as Edward Waterhouse's *A Declaration of the State of the Colony and Affaires in Virginia* (1622), using the VCU facsimile. It is named on day 99, in dossier A and in field 10, with its purpose and limits labelled. The passages are still to select.
- **Codex finding 9, Tennessee attribution.** The French and Dutch labels are now recorded as a Curio Class context addition, and no Tennessee grade 3 requirement is claimed. The change was made in field 10, in days.csv day 94, in frame.md line 145, and in the matching s05 mechanical lines (see the last section).
- **Codex finding 4.** A supporting-question record was added on day 90, using Codex's suggested idea.
- **Other.** Error register F now also cites the Pamunkey history.

### s06, unit 6

- **6.1 day 135 Q2 asks six things.** Q2 was split into Q2a (what the Constitution and the Bill of Rights each do, and one right) and Q2b (who usually voted, and New Jersey's exception until 1807). Q1 was also split into Q1a and Q1b, so that each prompt asks one thing. Day 135 now has seven prompts. These parts are judged from earlier records:
  - the difference between citizenship, voting and equal rights, from the day 131 sort;
  - constitutional origins, from day 128;
  - Q4 now asks only for one similarity and one difference.
- **6.2 day 136 Massachusetts only.** The day 136 glosses now come from the class's own state constitution. Massachusetts 1780 Articles V and IX are the reserve.
- **6.3 two dates in one month.** Day 134 now uses the Constitution signed in 1787 and the Bill of Rights ratified in 1791.
- **C7 stale line.** "Its plan is unwritten." was deleted.
- **Codex finding 10, day 132.** Day 132 now has a retained five-row record covering the Liberty Bell, the Statue of Liberty, the anthem, Independence Day and the 1777 flag resolution. For each one, the child gives why it was made and what it stands for, plus one change from original purpose to later meaning. The day runs 5 minutes of retrieval, 20 of teaching, 8 of discussion and 7 for the record. The exit ticket stays one question.
- **Codex finding 4.** A supporting-question record was added on day 125.

### s07, unit 7

- **7.1 Boston, not our community.**
  - Q2 now uses an unseen historical map of the class's own state. Buell's 1784 map is the Massachusetts reserve, and Carleton's 1798 map is the worked example.
  - Q5 now answers the compelling question from E, an unseen local source, together with one project source.
  - Q1 and Q3 are labelled a transfer case. The Boston edition is one of five regional editions, and a Massachusetts class takes an edition other than Boston.
- **7.2 Q1 asks for everything.** Q1 now asks for two groups and one change, from two sources. The population comparison moved to the day 145 retained record.
- **7.3 Massachusett repeated from unit 5.** Field 10 now says the class's day 142 source is the local nation's own page. The Massachusett account is the Boston worked case and transfer card only.
- **7.4 Boston population figure.** The figure is now labelled "City of Boston estimate, 2024", 673,822, with the Census Bureau's Vintage 2024 figure of 673,458 noted beside it. It moved from the withheld packet to the Boston worked case on day 145. The withheld cards D (the 1906 market photograph) and F (population) are no longer used in the assessment.
- **7.5 hook.** The hook now opens on an old image of the class's own town. The Long Wharf engraving is the fallback.
- **Codex finding 11, own-community research.** Two portfolio components were added, each with look-fors and examples, and both are scored on day 159 without adding time to its thirty minutes:
  - P0a, MA.3.T1.2: own-community research from days 142 and 145 to 147.
  - P0b, MA.3.T6.1: the own-state historical map from days 143 to 144.

  The withheld-packet sentence was replaced with Codex's wording.
- **Exits (C3).** All exits are one question. Days 144, 145, 148 and 150 to 157 are labelled "Retained evidence, not an exit".
- **Codex finding 4.** A supporting-question record was added on day 141.

## Findings not applied, and disagreements

- **Codex findings 1, 3 and 6, assessment size.** Codex asked for fresh assessment components given on earlier days. The fixer followed expert settled row 2 instead: parts are judged from products the unit already makes, and no new sitting is added on an earlier day. Every row names its source day.
- **Expert 1.3 and settled row 1, the start-of-year check.** The expert's settlement puts the check outside the social studies period, with the day 1 exit standing in where no slot exists. The fixer followed the rule in the fix brief instead: the check runs in the last ten minutes of day 1 after the hook, and the reteach is on day 2.
- **Expert 1.1, joining day 23's Q1 and Q3.** Not joined. The two prompts use different maps, and a joined prompt would ask two things. Day 23 therefore has nine prompts.
- **Expert 2.1, the D1 records.** s02 judges D1 from the day 26 and day 44 records, which are already saved products, rather than the "day 45 claim" the expert named.
- **Expert 5.2, where M4 and M5 are observed.** The expert named days 103 and 104. The fixer used the days where those codes are taught and saved (days 95 and 96 for MA.3.T3.3, and days 100 to 103 for MA.3.T4.1), because day 104 is a timeline day.
- **Expert 5.2, the timeline.** For s05, the timeline is judged from day 119's retained timeline record rather than day 117. Day 119 is where the timeline product is made; day 117's product is the supporting-question link.
- **Expert C5, the Massachusett across units 5 and 7.** The nation still appears in unit 5 teaching (Smith's account, days 95 and 96) and as unit 7's Boston worked and transfer case only. This follows the expert's own 7.3 fix. Moving it out of unit 7 altogether is left to the structure pass if it is wanted.
- **Codex finding 7, wording.** Codex's three-leader Q5a was not used as written. The expert's "choose one pair" won, and the Winthrop part is covered by the day 107 record.

## Unverified

These are not written as fact in the plans.

- **Techiman dates.** The decongestion notice date (15 February 2026) and the market opening (11 November 2024) come from search snippets only, because the tecma.gov.gh pages do not load. B's "November 2024" date for the Facilities Record rests on the same snippets and is to be confirmed before printing.
- **Narragansett council.** That the Tribal Council is elected was not confirmed on the tribe's pages, so the plan does not say it.
- **Elwha.** That the Lower Elwha Klallam Tribe sought the dams' removal was not confirmed on the tribe's page, so the plan calls the tribe a restoration partner only.
- **Tennessee crosswalk.** Codex's codes 7.62 and 8.01, which place French and Dutch colonies in later grades, could not be read (403). The plans claim no Tennessee requirement either way.
- **Boston population.** The Census figure of 673,458 for Vintage 2024 and the 1980 count of 562,994 were confirmed through secondary summaries only.
- **Waterhouse passages.** The report, its date and the VCU record were confirmed. Its passages are not selected yet.
- **Florida Museum account.** The Seloy account was read on 14 November 2026. Its "flaming arrows" detail is not used.

## For the structure pass

1. The expert's items 1 to 7:
   - a skeleton line for own-place codes;
   - an assessment cap and a one-question exit rule in the Codex brief;
   - the day 51 days.csv and frame fix, which is already done here;
   - a check for stray "?" characters;
   - generating field 3 "Returns" so it cannot go stale;
   - the Tennessee row template;
   - the rule against living officeholders in the sensitivity brief.
2. scope-and-sequence.md line 23 still says the start-of-year check runs "before day 1". docs/courses/UNIT-PLAN.md still says a unit 1 readiness check "is served by the start-of-year check, given before the unit opens". Both should say "the last ten minutes of day 1, after the hook".
3. scope-and-sequence.md line 71 still says "Candidate (Tennessee 2024 grade 3, New France and New Netherland on the map)". It should match the corrected frame and days.csv wording.
4. Codex P1: complete the Tennessee comparison from the 2024 crosswalk once it can be read. Also take Codex's process items:
   - a part-to-evidence blueprint;
   - telling earlier-collected parts apart from assessment-day tasks;
   - recording edition and code in comparisons;
   - checking the shorter routes against retained evidence days;
   - aligning the template and checker on where daily evidence goes;
   - noting that the gate checks structure only.
5. The days.csv assessment notes for days 23, 47, 67, 88, 105, 120, 135 and 159 say "every part of each listed code asked once". Day 120's note also says the first-half codes "return as one short prompt each". The plans now meet these notes by judging parts from saved products (settled row 2), not by asking each part on the day. The note wording could be updated to say so.
6. The regional transfer editions now promised in s04 and s07 need building: four more for each unit.

## Mechanical fields changed

- **data/plans/social-studies-grade-3/days.csv**
  - Day 1 note: the check is "given in the last ten minutes of this day after the hook".
  - Day 51 goal: "(a bakery's wheat from a farm, its bakers and its ovens)".
  - Day 94 note: "Curio Class context addition; no Tennessee grade 3 requirement claimed".
- **frame.md**
  - Line 143: day 51 wording.
  - Line 145: the unit 5 check-set wording.
- **Matching mechanical lines in the unit files**
  - s01 day list, day 1.
  - s03 day list, day 51.
  - s05 skeleton "Check set adds" line.
  - s05 day list, day 94.

## For Cory

None.
