# Fixes: civics-government-and-civic-life unit plans, 2026-11-14

Sources applied: the expert read (plan-civics-government-and-civic-life-2026-11-14.md), its "For the fixer" list first, then every Codex finding the expert did not cover (plan-civics-government-and-civic-life-codex-2026-11-14.md). Where the two disagree, the expert's "Settled by the expert" table governs, and each case says which was followed.

Gate: `unitplan.py check` PASS on all ten units; `sequence.py check` 0 failures; `frame.py check` 0 failures (10 units, 160 days; day count and unit totals unchanged). Word counts outside the excluded spans run from 1,053 (s10) to 1,218 (s04), all under 1,250. The plans contain no em dashes and no company names in student, teacher or family text; the day lists were re-synced from days.csv and match.

## Applied

### Course-wide

- **CW1 broken characters (expert; Codex 11, 14).** In s09.md and s10.md, every "?" that stood for an apostrophe or quotation mark is restored, including nested quotes in s09 and s10 items. Only real question marks remain, and link targets are untouched.
- **CW2 current-check lines.** Dated "As of November 2026 (checked 2026-11-14)" teacher background lines are in s03, s04, s05, s06, s07 and s09. Where the word cap allowed, they sit in field 2; otherwise they sit in field 10 before "Still to make". Each line states the facts without a party verdict. One wording choice: case names that are company names (the tariff case of February 20, 2026, and the January 17, 2025 social media app ruling) are described without the name, under the no-company-names rule.
- **CW3 assessment sizing.** The settled sizing is about 1 minute per recall item, 2 per sentence, and 8 to 10 per paragraph. Instances are cut, not parts, and parts scored earlier come off the sitting.
  - s01 day 14: item 2 is a labelled grid; item 4 is a matching grid plus two sentences; the six items take 5, 4, 6, 5, 7 and 13 minutes.
  - s02 day 29: item 1 boxes are one phrase each; item 4 is a five-row matching grid; the items take 9, 7, 7, 9 and 10 minutes, plus three to check.
  - s03 day 46: item 4b is a matching grid; item 6 is cut to the national and British chart plus one sentence on local government, with the state and local cells scored on day 41. Day 41 now runs 5, 10, 15, 15 (independent) and 5 minutes. The day 46 items take 11, 5, 9, 6, 5 and 7 minutes, plus two to check. Field 7 marking includes day 41.
  - s04 day 62: item 1 is a partly drawn grid; the items take 8, 4, 4, 7 and 22 minutes.
  - s05 day 75: item 4 is retained from day 67 and item 10 from day 72; item 5 asks three examples. The remaining items take 9, 13 and 18 minutes, plus five to check. Field 7 marking and the U6 rows for days 67, 72 and 75 match.
  - s06 day 94: item 1 asks each amendment's change in a phrase, then one chosen amendment in full; item 3 asks one chosen law. The items take 8, 8, 11, 5 and 10 minutes, plus three to check.
- **CW4 sensitivity studies.**
  - s02: adds the national museum of African American history's teaching pages and a note to read Gordon-Reed in full.
  - s03: replaces the copied study with party platforms, advocacy organizations from several sides, and the Congressional Research Service overviews.
  - s05: starts with an immigration journalism style guide (NAHJ or SPJ).
  - s06: adds Teaching Hard History and the National Center on Disability and Journalism style guide.
  - s07: adds the Native American Journalists Association's Tribal Nations Media Guide and the treaty's hard history, including Leschi's execution.
- **CW5 "the lead".** s08 now reads "The teacher books unit 10's audience beyond the class by day 130 (frame)". In s10, field 10 and U11 now read "The teacher confirms the audience booked by day 130, the venue and the safe route before day 149".
- **CW6 exits.** Exits are cut to one question and one reason in s01 (days 3, 5, 7, 8, 11 and 12), s02 (days 16, 19 and 27) and s03 (day 33). Each second ask moves to the next day's warm-up, and the s01 line names those warm-ups.

### By unit

- **s01.**
  - 1.1: the days.csv day 9 note no longer carries a Since Time Immemorial credit.
  - 1.2: the day 10 goal is now "Franklin's 1751 letter" (days.csv only; see the structure pass).
  - 1.3 and 1.4 are done as listed above.
  - Field 4 keeps "Start-of-year check: none needed; retrieval only", and nothing sits before day 1.
  - Codex 1: Rakove (2005) is added as the verified critical account on the U6 day 11 row and in field 10; Tooker is marked as unread background.
- **s02.**
  - 2.1: a teacher note on the Declaration's grievance slur is in field 2 Limits, the days.csv day 17 and 19 notes, and frame.md's Sensitive content bullet. It is summarized for students, named as a slur by the teacher, not read aloud, and used on day 19 as evidence of exclusion.
  - 2.2 and 2.5 are done as listed above.
  - 2.3: the field 4 repairs now run repair A in day 16's first ten minutes and repair B in day 17's warm-up, and the U6 rows for days 16 and 17 match.
  - 2.4: the phantom day 16 retrieval row is deleted.
  - Codex 2: the Brutus link now points to teachingamericanhistory.org, because the old PDF returned 404.
- **s03.**
  - 3.1 to 3.3 are done as listed above.
  - 3.4: the expert's settled wording is used in the item 4b key, the exit 39 key and the U6 day 39 row: "Most armed services sit in the Department of Defense (the Coast Guard in Homeland Security)". Codex 3's clause that the Navy holds the Marine Corps is added.
  - Codex 4 is folded into the expert's 3.3 fix (see "Not applied").
- **s04.** 4.1 (current check) and 4.3 are done. 4.2: the Libertarian platform (section 3.6) sits beside the Green one, and the platforms are labelled 2024.
- **s05.**
  - 5.1: field 2 adds birthright citizenship (Executive Order 14160 and Trump v. Barbara, June 30, 2026).
  - 5.2: the 2025 civics test, for filings on or after October 20, 2025, is dated beside the 2008 test.
  - 5.3 and 5.4 are done as listed above.
  - Codex 6: item 11 and source N add the context for EO 9981's political risk, namely the Senate filibuster threat and resistance inside the military. The text states that nearly all units were integrated by the end of the Korean War.
- **s06.**
  - 6.1 (Settled table): area b is Plessy (1896) and Brown (1954). Lochner and Parrish move to an extension card, and the item 5b sample, field 10 links (govinfo), the days.csv day 82 and 85 notes, the U6 day 82 row and frame.md unit 6 area b all follow.
  - 6.2 to 6.4 are done.
  - Codex 7: Title VII (section 703(a)(1)) is added beside Title II in item 3, source Q, the answer guide and day 82.
  - Codex structure 1 (classroom side): field 2 carries the T5.4 race, gender and disability categories.
- **s07.**
  - 7.1 (current check) is done. The Department of Education order and McMahon v. New York (July 14, 2025) are included, as is the SNAP administrative-cost shift from FY2027.
  - 7.2: the budget is described as adopted for the class's own town or state, and Boston FY26 is only a worked example.
  - 7.3 is done.
  - Codex 8: item 9 now uses a new fictional card T, labelled fictional and reserved for item 9.
- **s08.**
  - 8.1 (Settled table): Proposition 13 (June 6, 1978) is the historical conservative-side case in field 2, item 2's sample (same verbs for both sides), field 10's source, U3, U6 days 121, 122 and 127, and exit 127. The Tea Party page is used for stated goals only.
  - 8.2 is done.
  - Codex 10: exit 124 now uses an unseen bakery, job bank and union wages case, reserved from teaching.
- **s09.**
  - 9.1 and 9.2 are done.
  - 9.3: a note on the Boston program's status is added; the evaluation stays a dated worked example.
  - Codex 12: exit 135 now uses an unseen canceled town meeting case.
- **s10.**
  - 10.1 and 10.2 are done.
  - 10.3: field 6 now has four cells per row; each "wrong beside right" sentence moved into its row, and the paragraph is removed.
  - 10.4: scoring now reads "secure (all look-fors), developing (partial) or missing (absent or contradicted)".
  - Codex 13: field 5 now scores the print and oral components from either path and records the digital component separately. On the paper route the digital component is recorded as awaiting demonstration; with a device, one shared offline version records each student's design decision. Field 8 matches.
- **frame.md.** The Sensitive content bullet is updated (2.1). The unit 6 area b now reads Plessy and Brown. The civil rights handoff row adds wh2-social-movements (the expert's seams note and Codex structure 7).

## Not applied

- **Expert 1.2 and 6.1, the scope-and-sequence.md parts** (the unit 1 Franklin label and the unit 6 topics). That file is outside the brief's editable list, so both go to the structure pass. days.csv and frame.md carry the change.
- **Codex 9 (more composites in unit 7).** I followed the expert, whose CW3 says unit 7 holds by its composite records.
- **Codex 4 (item 6 as a full independent task) and Codex 5 (retain item 5 from day 68).** I followed the expert's CW3 rule (cut instances, retain earlier scored parts).
  - Unit 3 item 6 is trimmed, and its state and local cells move to independent work on day 41.
  - In unit 5, items 4 and 10 are retained, from days 67 and 72. Item 4 is retained from day 67, not day 66, because day 67 teaches the seven roles. Item 5 is cut to three examples.
- **The expert's suggested logging with `plan.py defect`.** That logging is not in this brief's allowed actions, so these fixes are logged in this report only.

## Unverified

- The vote counts in Trump v. Barbara and Trump v. Cook: the sources disagree, so the plans omit them.
- Which 2025 law rescinded the Corporation for Public Broadcasting's funding: the sources differ, so s09 says only "in 2025". The board's dissolution vote (announced January 5, 2026) was confirmed.
- Medicaid cost shifts in the July 2025 budget law were not confirmed against a primary source and are left out of s07.
- The detail on Leschi's execution in s07 rests on general knowledge, not a source read this session.
- I did not read the Proposition 13 pamphlet text itself; only the UC Law SF archive record (ca_ballot_props/850) was found. The about 65 percent result needs a check against the official statement of vote.
- The Brutus page at teachingamericanhistory.org refused my fetch (403). The Codex read reports that it loads.
- The Teaching Hard History page now redirects to the Learning for Justice archive site, and the NAJA guide page was not fetched.

## For the structure pass

- scope-and-sequence.md needs two changes:
  - unit 1 topics: "Franklin's 1751 letter on a colonial union (three years before his Albany Plan)";
  - unit 6 area b: Plessy and Brown in place of "later 14th Amendment cases".
- The MA.8.T5.4 paraphrase in data/standards/ma-hss-2018.txt omits the race, gender and disability categories (Codex structure 1).
- A broken-character gate (expert CW1; Codex structure 4). It should scan for `\w\?\w` and for "?" opening a quote, outside link targets. The root cause of the s09 and s10 damage (likely a non-UTF-8 shell write) should be found so the brief names a safe write path.
- A standing "Current check (date):" line in the template (UNIT-PLAN.md) for social studies.
- One shared teacher note on the Declaration's grievance slur for every course that reads the Declaration.
- Codex structure items:
  - 2: explicit composite records naming evidence day, conditions, parts and location;
  - 3: the checker should parse U3 to U11 separately rather than as part of the day list span;
  - 5: a source-selection status field (verified, catalogue-only, indexed-only, unread);
  - 6: real shorter-path allocations for the 45-minute route.

## For Cory

None. The paper-only route for D4.3 is handled at item level: the digital component is recorded as not yet demonstrated, never scored from a storyboard.
