# Social studies unit plans: structure pass, 2026-11-14

One pass over the "For the structure pass" items of the plan reads, the Codex reads and the fix reports for all 15
social studies courses (138 unit plans), plus each fix report's "Unverified" list. Items are de-duplicated and grouped
by target. Each is marked **applied** (and how) or **not applied** (and why). Only data and rule changes moved plans,
and those plan edits were kept small: skel copies brought into step with a changed own-word line, and a few
sentences brought into step with verified wording.

Gate results after every change:

- `python -X utf8 scripts/unitplan.py check social-studies`: 138 PASS, 0 FAIL.
- `python -X utf8 scripts/sequence.py check <course>` for every course whose days.csv changed (economics,
  social-studies-kindergarten, social-studies-grade-2, social-studies-grade-3, us-government-and-politics,
  us-history-i, us-history-ii, world-history-i): 0 failures each.
- The new gate checks were tested on scratch copies, never on the plans: a "?" inside a word fails; a merged document
  over 1,800 words fails; an observation code missing from field 5 fails.

## Ledger

### Scripts

**scripts/sequence.py**

- **Readiness on day 1 for unit 1 (lead rule 2026-11-14): applied.** A readiness mark on course day 1, when day 1 is
  in unit 1, is now accepted. Every other unit's first day still fails. The comment and the failure message now say
  "unit 1: the last ten minutes of day 1".

**scripts/unit_skeleton.py** (it never overwrites a written plan without --force, so none needs a re-run; the
docstring now says so)

- **"One of" and option lists turned into required parts: applied.** The new `is_choice` finds choice standards:
  "one of", "from the list", "choosing one", "research, report on, analyze, in or map one ...", or parts marked
  "option:" or "as an example agency". "One another" is excluded. It finds 13 of them: MA.7.T4b.7, MA.8.T5.6,
  MA.GOV.T2.8, MA.USI.T4.2, MA.USI.T7.5, MA.USII.T2.4, MA.USII.T3.5, MA.USII.T4.8, MA.WHI.T2.5, MA.WHI.T3.2,
  MA.WHII.T5.3, MA.WHII.T5.11 and MA.WHII.T7.1.
  - The new `parts_of` decides which parts a unit owes. If days.csv cites parts of the code anywhere in the course
    (the parts are assigned to units), a unit owes only the parts it cites. Otherwise a choice standard owes none and
    any other standard owes every part.
  - Field 2 prints a choice standard as "a choice standard, one option studied in depth and the rest surveyed (not
    each a required part)", with its options listed. Field 5 gives it one row.
- **"Such as" lists: applied.** An own-word line with "such as" gets the note "The "such as" list gives examples, not
  required parts."
- **Assigned parts (a part taught in another unit was still owed here): applied** through `parts_of`.
- **Sensitivity note cut off at its bracket: applied.** Field 10 now prints the days.csv note in full, because the
  bracket often names what to read.
- **Readiness lookback (WG-II day 119, a check two days back across a respond day): applied.** Field 4 now looks up
  to three days back, through respond and course-level days, as long as no other unit opens between. This matches
  READINESS_AHEAD in sequence.py.
- **Field 7 named unit 1's own day 1 check as "next unit's readiness": applied (guarded).**
- **Unit 1 with a day 1 readiness mark but no progression rows found: applied.** Field 4 now gives the day 1 "Given:"
  line and points to the day 1 note, instead of "none needed".
- **Already fixed before this pass** (the reports came from older skeletons): observe days in field 5, retrieval
  clauses, comma runs in day ranges, unit 1's Given line, and the general-form MA line.
- **Models carried, sorted by frame order: not applied.** It needs an order the frame data does not hold.
- **Own-place restriction: not applied.** It needs a marker in the frame that does not exist yet.
- **Section placeholder labels: not applied.** They are writer content, not mechanical.
- **Evidence map, packet manifest and shorter-path ledgers: not applied.** These are new data models for the
  production stage, not structure fixes.
- **Per-code minutes: not applied.** No data field holds minutes per code. The briefs now ask for minutes per item
  instead.

**scripts/unitplan.py**

- **Word cap (UNIT-PLAN.md said 1,800 for merged documents, the gate enforced 1,250): applied.** The gate now
  enforces the rule as written in UNIT-PLAN.md, "Length", and that list is now named as the one home of the caps.
  - 1,250 words applies to every `sNN.md`, outside fields 4, 5 and 6, the day list and skel blocks.
  - 1,800 words applies to a merged one-section document (`## U3.` to `## U11.` after the day list), outside the same
    and U3, U4 and U6.
  - Before this pass the gate counted everything after "## Day list" as day list, so U5 and U7 to U11 were never
    counted. They are counted now.
  - Every merged document (civics s01 to s10, us-history-ii s01 to s10) passes. The docstring line that said "the
    merged 1,800 does not apply" is gone.
- **"?" for lost apostrophes, quotes and accented letters: applied.** A "?" between word characters, a "?" opening a
  word, or U+FFFD fails the line. Markdown links, URLs and code spans are skipped. No current plan has a hit.
- **Choice standards and assigned parts: applied** through `sk.parts_of` and `required_codes(rows, allrows)`, for
  both field 2 and field 5. The gate only asks for less than before, so every plan still passes.
- **Observation days (K and grade 1 observe rows) had no coverage check: applied.** Each code of an observe day must
  appear in the code cell of a numbered field 5 item row, and that row must have an item of at least three words.
  This matches the `| # | Code and part | Prompt |` tables the plans use.
- **Field order check: applied.** It now compares only the numbered unit fields, so the U headings do not break it.

### Briefs

- **plan-codex-science.md, NGSS base: applied.** One line under "Science settled", citing DESK-ANSWERS.md 2026-11-14:
  - NGSS is the base for every science course, NGSS wording governs, and the crosscutting concepts stay in.
  - Massachusetts 2016 STE is a crosswalk only: a plan may note where it folds, splits or regrades a code, and never
    drops an NGSS code to match it.
- **Unit 1 readiness wording in every brief: applied.** The retired "unit 1 is served by the start-of-year check"
  is replaced by the day 1 rule in plan-codex.md, plan-codex-math.md, plan-codex-ela.md, plan-codex-science.md,
  plan.md, plan-codex-read.md, sequence-write.md (rule 2, which now notes that sequence.py accepts it) and
  frame-write.md.
- **Repeat lessons folded into plan-codex.md: applied.** Each was merged into the bullet it extends where one exists:
  - assessment minutes per item, kept inside the day's real minutes, with product parts made earlier taken off the
    sitting, and no reteaching on an assessment day;
  - the exit rule: one question, at most two parts, invented cases printed "invented for practice";
  - write UTF-8 with LF line endings, never "?" for a lost character (the gate fails it);
  - check days.csv before naming a day; no pipeline notes in a plan;
  - name the measure behind any population figure;
  - no living officeholder as a biography subject;
  - dated "As of" background for living institutions and leaders, renamed places and court rulings, after a news
    search of the last 24 months that includes deaths; give the vote and what was decided (a stay is not a merits
    ruling);
  - study every source the frame names and record each as reached or not reached;
  - Tennessee: do not write about the blocked site, and claim no requirement the standard does not show;
  - Since Time Immemorial: where a unit does not use it, say nothing about it (this replaces the "is not used"
    boilerplate).
- **Repeat lessons in the math, ELA and science briefs: applied where they fit.** Each brief got a block of six
  lines: UTF-8 and "?", the exit rule with the K to 2 default, assessment minutes, checking days.csv, no pipeline
  notes, and dated background. The subject-specific social studies lessons (Tennessee, Since Time Immemorial, Native
  nations, campaign pages) were left out of those three briefs.
- **"The local New York framework path": not applied.** The reads do not state it clearly enough to write as a rule
  without inventing one. It is for the lead to state.

### Template and glossary

- **UNIT-PLAN.md, field 4 and the blank copy: applied.** Unit 1's check, where unit 1 has readiness rows, takes the
  last ten minutes of day 1 after the hook, and days.csv marks day 1 `readiness`. Every other unit's day 1 stays
  clean.
- **UNIT-PLAN.md, "Length": applied.** It now names itself as the one home of the caps and says what the gate
  enforces (see unitplan.py above).
- **GLOSSARY.md, readiness check row: applied.** Same wording.
- **A standing "Dated background (as of date)" slot, and the K to 2 exit default in the template: not applied.**
  Both now sit in the briefs, where the writer reads them. A template field would make every unit of every subject
  carry the slot. That is a lead call on the template, not a mechanical fix.

### Data

**data/plans/\*/days.csv**

- **Day 1 `assess` = `readiness` where the unit 1 plan gives its check on day 1: applied.** Eight courses: economics,
  kindergarten, grade 2, grade 3, US Government and Politics, US History I, US History II and World History I. Only
  the one cell was edited; every other byte is unchanged. The other seven courses give no unit 1 check, and their
  day 1 stays blank: civics, grades 1, 4 and 5, WG-I, WG-II and WH-II.
- **Retired "start-of-year check" wording: applied.** Grade 3 notes on days 1 and 2, and US History II day 130
  (Economics' check is now "unit 1 readiness check ... the last ten minutes of its day 1"), with the matching plan
  and scope sentences.

**data/progressions/social-studies.csv**

- **The "about a billion Hindus" figure: applied.** It now reads "nearly 1.2 billion Hindus practiced it in a 2020
  estimate (Pew Research Center, published 9 June 2025; recheck when a newer estimate appears)". It was verified in
  the WG-II fixes.
- **A scan for other stale figures: no others found.** The only other population figures are the Slave Voyages
  counts (12.5 million embarked, 10.7 million survived), which are settled history.
- **"Readiness on the unit's first day" wording in 13 rows: applied** ("before the unit opens"). The rows are
  ss5-slavery-colonies, ss5-independence-war, ss5-constitution, ss5-informed-action, us2-depression,
  us2-isolation-fascism, us2-atomic-bomb, us2-cold-war-origins, us2-vietnam, us2-social-movements,
  us2-terrorism-response, gov-ideals-gap and gov-rights-cases.
- **Wording brought into step with the fixed plans: applied.**
  - wh2-social-movements: the check is in the last ten minutes of WH II day 107, used on day 117.
  - ss8-federal-state-powers: inherent powers of self-government, with institutions that vary.
  - ss6-phoenician-trade: the rowers' status is uncertain.
  - ss6-research-contribution: authority is checked at grade 6 depth.
  - ss6-caribbean-central-geo: drops the "first map from data" claim.
  - ss5-slavery-expansion: "traced state by state".
  - ss5-constitution: individual rights and responsibilities.
  - wh1-song-kamakura: temples restored.
  - ss2-projections: Mercator wording.
  - ss2-trade-world: why buyers trade.
  - ss2-culture-migration: "shared with other people in the receiving community".
- **ss1-supporting-questions, adding D1.4.K-2 to grade 1: not applied.** It would add a code to days.csv and to the
  plans, which is beyond a small plan edit. D1.4.K-2 is already taught in grade 2. This is for the lead.
- **ss4-state-maps exploration wording: not applied.** It is a content judgment, not mechanical.

**data/standards/ma-hss-2018.txt** (own-word lines; skel copies in the plans synced with the same words)

- **Applied where a fix report checked the line against the framework.**
  - MA.K.T1.3: adds justice.
  - MA.8.T5.4: race, gender and disability.
  - MA.5.T3.1: individual rights and responsibilities.
  - MA.5.T5.1: "Trace, state by state".
  - MA.5.T1.7c: Elizabeth Freeman, Quock Walker and Prince Hall.
  - MA.WHI.T3.2f: temple restoration.
  - MA.7.T3b.1: the Aboriginal peoples of Australia and the Māori of Aotearoa New Zealand.
  - MA.6.T3b.4e: the Code of Hammurabi as an early surviving written law collection, with the framework's own phrase
    kept in brackets.
- **Plans synced:** civics s06, grade 5 s05 and s07, kindergarten s02, WG-I s04, WG-II s06, and WH-I s03 and s04.
- **Not applied, because they need the framework PDF read line by line:** MA.4.T4.2, MA.4.T4d.5, MA.USI.T4.2c,
  MA.USI.T5.4, MA.WHII.T4.6, MA.WHII.T4.9 and MA.5.T1.5. Downloading the PDF needs Cory's permission, so it was not
  fetched.

**data/standards/c3-indicators.txt**

- **Own-word lines for the C3 codes: not applied.** The file holds ids only: none of its 283 codes has a line, and all
  283 are used in social studies days.csv. Writing the lines needs the C3 framework text, which is not on file, and
  downloading it needs permission. Candidate wording already sits in each plan's field 2. With the text on file,
  this is one data pass.

### Scope and sequence pages

- **Applied.**
  - us-history-i and world-history-i: unit 1 readiness on day 1. us-history-i also gets the draft feedback timing.
    world-history-i also gets "West and West Central African states".
  - grade 3: unit 1 readiness on day 1. The Tennessee candidate is relabelled as a Curio Class context addition, with
    no Tennessee requirement claimed.
  - grade 5: day 72 timeline review, days 73 and 74 as two Check days, and the cotton gin as California 8.7.1,
    grade 8.
  - grade 2: the community goal (77 and 78), "Days 89 and 90 add a digital version", and "made in a rotation".
  - civics: Franklin's 1751 letter; Plessy and Brown.
  - WG-I: the Phoenician workers' statuses.
  - us-history-ii: Economics' unit 1 readiness check.
- **Frame.md seams: not applied.** These are the grade 2 models order, the grade 5 cotton gin and soldier testimony,
  and the wh2-social-movements handoff in the civics and grade 5 frames. Frames sit upstream of the plans and need a
  frame read. They are for the next frame pass.

### Wording across courses

- **Trump v. Barbara and Trump v. Cook: applied.** The verified wording from the US Government fixes report is:
  - Cook was a 5 to 4 stay denial while the case goes on, not a merits holding.
  - Barbara's judgment was 6 to 3, with five justices joining the constitutional reasoning.

  Civics s03 and s05 were brought into line. Civics s06, grade 1 s07, US Government s04 and s05, US History I s06,
  US History II s01 and the economics frame already agreed. This closes the vote-count items in the civics and
  grade 1 Unverified lists.

### Not applied, other

- **The Declaration's slur, as one shared teacher note across courses: not applied.** It is content wording for the
  sensitivity read, not structure.
- **A social studies approach page, and localization boilerplate: not applied.** Each is a new document, outside a
  structure pass.

## Unverified (for the production stage)

Each item is written in the plans as hedged, as "check before teaching", or not at all. "Confirm by" says what would
settle it.

| Course | Unit | Item | Confirm by |
|---|---|---|---|
| Civics | s09 | Which 2025 law rescinded the public broadcasting funding | The enrolled act on congress.gov |
| Civics | s07 | Medicaid cost shifts in the July 2025 budget law | The enrolled act, or a CBO or CRS summary |
| Civics | s07 | Leschi's execution detail | A tribal or state archive source |
| Civics | (Prop 13 day) | The "about 65 percent" result | The California official statement of vote, 1978 |
| Civics | (sources) | Brutus page (403 here); Teaching Hard History redirect; NAJA guide not fetched | Open each page by hand |
| Economics | s08, s09 | The consumer finance agency's status in 2025 and 2026 | The court docket and the agency's own site |
| Economics | (tax unit) | A free federal direct filing service for the 2027 season | IRS announcement |
| Economics | (trade unit) | A section 122 surcharge after the February 2026 ruling | Federal Register or a USTR notice |
| Economics | (money unit) | Any Federal Reserve rate change in September 2026 | FOMC statements page |
| Economics | (tax unit) | The 2026 tax-table figure of 993 | The published 2026 tax table |
| Economics | (competition unit) | Appeal status of the September 2025 search remedies | The court docket |
| Grade 1 | (Nairobi day) | "Cool highland weather" | A Kenya Meteorological Department page |
| Grade 1 | (Navajo day) | President, Vice President and Council delegate terms; 2026 result | The Navajo Nation's own pages (opvp.navajo-nsn.gov, the Council site) |
| Grade 2 | (refugee day) | Omar's 2015 resettlement in Luxembourg (UNHCR 403) | The UNHCR page, opened by hand |
| Grade 2 | (maps) | Colton 1855 Vermont map legible at print size | A test print |
| Grade 2 | (then and now) | Brattleboro 1905 and today views are the same street | A view matched against the street |
| Grade 2 | (immigration) | The Antins' 1894 arrival date (May 8 against August 28) | A ship manifest |
| Grade 2 | (world) | Saudi and Tokyo pages; FosterClub, UNHCR Teaching About Refugees, KNBS booklet reached, not read | Read each in full |
| Grade 3 | (markets) | Techiman notice and opening dates | The tecma.gov.gh pages, or a Ghana News Agency report |
| Grade 3 | (Narragansett) | The Tribal Council is elected | The Narragansett Indian Tribe's own pages |
| Grade 3 | (Elwha) | The Lower Elwha Klallam Tribe sought the dams' removal | The Tribe's own page |
| Grade 3 | (colonies) | Tennessee codes 7.62 and 8.01 | The Tennessee standards PDF, opened by hand (no requirement is claimed) |
| Grade 3 | (Boston) | Census figures 673,458 (Vintage 2024) and 562,994 (1980) | census.gov tables |
| Grade 3 | (Waterhouse) | Passages not selected yet | Selection at production |
| Grade 4 | (Billy Frank Jr.) | Statue dedication | The Capitol or tribal announcement |
| Grade 4 | s04 day 71 | St. Lawrence Iroquoian kinship note | The sensitivity read, with the nations' own sources |
| Grade 4 | s03 | Ute Mountain Tribal Park wording | The Ute Mountain Ute Tribe's page |
| Grade 4 | (various) | Equiano birthplace debate; Buffalo Soldiers note; Oregon Trail claim, day 86 | A scholarly or NPS source each |
| Grade 4 | s06, s07 | Unit 7 strip and exit statements; unit 6 atlas features (from memory) | The claim-to-source table filled at production |
| Grade 5 | s09 | Texas v. Kennedy final judgment | The court docket |
| Grade 5 | s01 | Penn card office-clause detail | The Frame of Government text |
| Grade 5 | s04, s07 | Saint Regis Mohawk page; EBCI and Choctaw pages linked, not read | Read each nation's page in full |
| Grade 5 | s07 | Thomas Hunter manifest names | The manifest image |
| Grade 5 | s06 | A Lemhi Shoshone or Shoshone-Bannock source | The sensitivity agent names one |
| Grade 5 | s07 | Connecticut 1848 and New Jersey 1860 bondage | State archives, or the NPS |
| Grade 5 | s09 | Native voting dates of 1948 and 1957 | State records, or the NCAI page in full |
| Grade 5 | s09, s10 | Chisholm, union history, UC San Diego, NPS ratification and anti-suffrage pages checked live, not read | Read each in full |
| Grade 5 | s06 day 85 | Great Falls at about 47 N, 111 W | USGS GNIS |
| Grade 5 | s01, s04 | Regional crops; postwar deflation | A USDA source; a historical price series |
| Kindergarten | (sources) | The Indigenous Journalists Association guides page | Open the page |
| Kindergarten | (holidays) | The Italian American heritage line rests on an advocacy source | A neutral news or survey source |
| Kindergarten | (photographs) | South Texas, Dead Ox Flat and Great Seal Hand Press images not inspected | Look at each on loc.gov by hand |
| US Government | s01 | Fall 2026 framework topic numbers for ideologies and socialization | The course framework PDF |
| US Government | s01 | Census 2024 Table 5 cells (52.5, 77.2, 82.5) | The census table, cell by cell |
| US Government | s05 | Press-pool appeal decided on the merits | The court docket |
| US Government | (Congress) | 2026 midterm seat counts | The House Clerk and Senate pages once certified |
| US Government | (bureaucracy) | FSMA enforcement rider | The enrolled act's text |
| US History I | s06 | Black Hills award amount | A wire or Treasury source |
| US History I | s03 | Tulsa agreement ruled invalid, 8 to 1 | The Oklahoma Supreme Court opinion |
| US History I | (Colfax) | The "about 150" upper bound | An independent scholarly source |
| US History I | s09 | Acting Archivist's name and dates | archives.gov |
| US History I | (empire) | Jones Act, March 2, 1917; Philippine independence, July 4, 1946 | The statute; the treaty |
| US History II | (Tulsa) | Lessie Benningfield Randle as the last known living survivor; trust total against its goal | Wire report; the trust's report |
| US History II | (WWII) | Living Navajo Code Talkers after August 2026 | The Navajo Nation's announcements |
| US History II | (recent) | Little v. Hecox disposition; CDC COVID-19 death count and date | The slip opinion; the CDC data page |
| US History II | (1893) | Comptroller's count of 158 suspended banks | The 1893 Comptroller report |
| US History II | (Iraq) | A federal URL for the Iraq Survey Group key findings | govinfo.gov |
| US History II | s10, A122 | Movement hearing excerpts; G77 sheets; Oglala Sioux Tribe page URL | Selection at production; the tribe's site |
| WG-I | s05 | Book of the Dead 125A or 125B | The UCL page, opened by hand |
| WG-I | s06 | Jar 74.51.2298a,b "ownership" reading | The museum record |
| WG-I | s08 | Steele 2020 end page; second account for the calendar and base-60 packets | The OAPEN PDF; one more secondary source each |
| WG-I | s07 | Council on Islamic Education guide, current edition | The publisher's copy |
| WG-II | (Harappa) | H-1533 in Kenoyer and Meadow | The paper's PDF |
| WG-II | s09 | The Dipylon jug as a prize jug | The museum record |
| WG-II | (Ashoka) | Rock Edict XIII and Mahavamsa XII mission details | A scholarly translation |
| WG-II | (Rome) | Date of Cassiodorus Variae I.27 | A modern edition |
| WH-I | (various) | Ogunnaike page; Todai-ji hall date of 1195; Churchill's Collection volume; Brasio page numbers; Nieuhof page | Open each source |
| WH-I | (various) | Thornton 1984; Vansina 1995; Klieman 2003 not read; Turin papyrus and Schoenbrun licences | Read each; check the licence pages |
| WH-I | (various) | Kalinago source; Song from Another Land; Magoulias as translator; translations to choose; s07 editions | Selection at production |
| WH-II | (Iran) | Ceasefire date (April 7 or 8); memorandum place and terms | A second wire report; the text |
| WH-II | (Gaza) | Status after June 2026; displacement share; who brokered | Wire or UN sources |
| WH-II | (Namibia) | 2021 joint declaration ratified or not | The German or Namibian government |
| WH-II | s02 P3 | Return of Owners of Land share and page | The source page |
| WH-II | (Syria; aid) | Government after Assad; aid-cut effects on malaria | Wire, WHO or UNAIDS sources |
| WH-II | (sources) | GAO-02-426 Appendix I; PopuList edition; Tiananmen Mothers statement date | Open each |
| WH-II | (older facts) | Armenian and Holodomor recognitions; Nanjing, Hiroshima and Nagasaki figures; 1938 laws; Mau Mau 5,228; Hidankyo 2024; USA FREEDOM Act; Budapest Memorandum | One check each at section writing |
| WH-II | (sources) | Haitian and Andean institutions; day 48 archives; JIMENA; Palestinian oral history; Indigenous declaration article | Read each |
| All with MA codes | (field 2) | Seven own-word lines not yet checked against the framework (listed under Data) | The 2018 MA framework PDF, once its download is approved |
| All | (field 2) | C3 own-word lines missing for all 283 codes | The C3 framework text, once its download is approved |

Resolved in this pass: the Trump v. Barbara and Trump v. Cook vote counts (civics and grade 1 lists). See "Wording
across courses".

## For Cory

- **Two downloads, if you want the own-word lines finished:** the C3 framework PDF (for 283 C3 lines) and the 2018
  Massachusetts history and social science framework PDF (for seven lines). Both are free public files. Neither was
  fetched, because a download needs your yes. Everything else in this pass was within the lead's rules.

## Closed 2026-11-14

The two open data items are closed, using the framework text Cory approved downloading (extracted copies in
S:\CurioClass-sources\_inbox\standards-2026-11-14).

- **data/standards/c3-indicators.txt:** all 283 indicators now carry one own-word line (tab after the id, the same
  format as ma-hss-2018.txt, so scripts/unit_skeleton.py reads them). Each was written from the indicator text in the
  NCSS PDF, in plain words and not copied. The header now gives fetched 2026-11-14 and says the lines are own words.
- **data/standards/ma-hss-2018.txt:** the 7 lines were checked against the framework text and corrected.
  MA.4.T4.2 (names how each territory was gained), MA.4.T4d.5 (sources, settlements and movements of Native peoples
  with current reservation lands, 1600s to 1800s), MA.USI.T4.2c ("compulsory" added), MA.USI.T5.4 ("policies",
  short- and long-term impact, the framework's battle list), MA.WHII.T4.6 (USSR in 1922, the New Economic Plan as the
  framework names it, personality cult, power struggle), MA.WHII.T4.9 (economic, social and political conditions, in
  their own countries) and MA.5.T1.5 ("legal status", leaders named). A header note records the pass.
- **Checks:** unit_skeleton.py on social-studies-grade-3 unit 2 (scratch output only) now shows the C3 lines;
  unitplan.py check social-studies passes all 138.
