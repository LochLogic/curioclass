# US History II unit plans: fixes, 2026-11-14

This fixer pass covers docs/courses/us-history-ii/s01.md to s12.md. It applies the expert read (plan-us-history-ii-2026-11-14.md) and the Codex read (plan-us-history-ii-codex-2026-11-14.md). The expert's "For the fixer" list went first, in order. Every Codex finding the expert did not cover came after. Where the two reads disagreed, I followed the expert's "Settled by the expert" table, and each such case is named below.

Files changed: s01 to s12, frame.md, scope-and-sequence.md and data/plans/us-history-ii/days.csv. The day count and the unit totals did not change.

Gate: `python -X utf8 scripts/unitplan.py check us-history-ii` passes for all twelve plans. `python -X utf8 scripts/sequence.py check us-history-ii` reports 0 failures.

**Where the teacher lines went.** Each plan's new dated lines sit at the end of field 6, under "**Teacher background for the section plans, as of November 2026:**". This follows the US History I fixer and keeps them out of the word cap. Every 2025 or 2026 fact was checked against a primary, court or wire source. I used the US Government fixer's verified wording for Trump v. Cook, Trump v. Slaughter and Callais.

**Exit tables moved.** s08, s09 and s10 had their exit tables in field 2, so they counted toward the cap. I moved each table into a new "U3. Checks, written first" field after the day list, the format s07 already uses, and left a pointer in field 2. This made room for the new lines.

Counts: 83 findings applied (71 of the expert's 74, all 12 of Codex's). 3 were not applied, and 2 were applied in part.

## Applied: the expert's findings

### Course-wide

- **CW1 (sittings sized to their minutes).** This was applied through each unit's overload finding below. Every sitting now adds up to its minutes.
- **CW2 (dated lines).** This was applied through each unit's dated-line finding below.
- **CW3 (made-up captions).** One line now opens U3 in s04 to s08: "Every caption or display an exit asks students to correct is written by Curio Class for practice, and the page labels it so." s09 and s10's new U3 fields carry the same line.
- **CW4 (copyrighted texts).** A rights line was added to field 10 in s02 (Franklin), s04 (the testimony clips), s09 (the NOW, DREDF and Huerta pages) and s10 (Schlafly and the movement writers). s07 also got one, for Ransby's and Theoharis's books.
- **CW5 (seam days).** In frame.md, the Seams table now reads "in day 41's last ten minutes", "in day 56's", "in day 66's", "in day 102's" and "in day 113's". In days.csv, every reteach note now names the day of its readiness check: days 28, 44, 46, 51, 61, 68, 104, 115, 120 and 140. The expert named only 61, 68 and 104; the others had the same fault.
- **CW7 (sensitivity lists).** The frame.md "Sensitivity reads" list now has entries for:
  - unit 1: tenant and Chinese railroad-worker histories, the Sicangu Lakota Oyate, freedpeople's testimony;
  - unit 5: Korean and other non-Japanese survivors;
  - unit 9: Huerta's own words, the Oglala Sioux Tribe's pages;
  - unit 10: Iranian American, Afghan, Nicaraguan and Polish community histories, and both traditions' own sources;
  - unit 11: the Veterans History Project.

### Unit 1 (s01.md, days.csv, scope-and-sequence.md)

- **U1-1 (applied in part).** Field 4's Given line reads "day 1, the last ten minutes, after the hook (lead rule 2026-11-14)". E1 comes in the five minutes before the check. Day 2's station covers items 1 to 4, with overflow on day 3.
  - The U6 day 1 row is now: hook 8, teach 10, compare 17, E1 5, readiness 10.
  - The skeleton's carried line and field 2 now say "inside day 1's readiness check".
  - In days.csv, the day 1 and day 2 notes were changed.
  - In scope-and-sequence.md, line 13, the readiness table and line 55 now name day 1's last ten minutes.
  - Not applied: `assess` = readiness on day 1 (see "Not applied").
- **U1-2.** The items were resized: A2 (grid, one conflict, two of four roles), A3 (one graph, one sentence), A5, A6, A7 (three cards) and A8 (4 minutes, with day 10's argument scored). The timing now totals 40, with a "such as" ruling note. The look-fors match.
- **U1-3.** A Federal Reserve teacher line covers four points:
  - removal for cause;
  - Trump v. Cook (June 29, 2026): a 5 to 4 refusal to let the President remove a governor while her case goes on, a stay denial and not a merits holding;
  - Trump v. Slaughter (June 29, 2026, 6 to 3);
  - Warsh sworn in as chair on May 22, 2026.
- **U1-4.** E2 and E9 were cut to two instances each.
- **U1-5.** The railroad key names Lakota lands and the Chinese workers on the Central Pacific.

### Unit 2 (s02.md)

- **U2-1.** A1, A4, A5 and A7 now ask one thing each. A2 asks for Hughes or Hurston plus one business or patron. A8 asks for two of three plus a limit, and A10 for a match plus one sentence. Each takes about 2 minutes. The keys and look-fors match.
- **U2-2.** Franklin's 1931 manuscript is unpublished and in copyright through 2030. It is used as attributed paraphrase from the NMAAHC account, and quoted Tulsa sources come from 1921 public-domain records.
- **U2-3.** Day 19 teacher line covers:
  - Fletcher's death on November 24, 2025, at 111;
  - Randle's status, to confirm;
  - the Oklahoma Supreme Court's dismissal of June 12, 2024;
  - the $105 million trust goal announced June 1, 2025.
- **U2-4.** E18 was trimmed. E21 now asks for two of three cases.
- **U2-5.** Item i now has a dated public-domain record to select, framed under values rule c.
- **U2-6.** A12 was renamed W23 everywhere.

### Unit 3 (s03.md)

- **U3-1.** The day 38 split is now A1 17, A2 12, A3 11.
- **U3-2.** The Oneida pointer was replaced by the Confederated Salish and Kootenai Tribes' pages.
- **U3-3.** A day 30 line gives the removals as a range, about 400,000 to more than 1 million, and dates California's 2005 apology act.
- **U3-4.** A day 36 line gives the $250,000 FDIC wording as of November 2026.
- **U3-5.** "G31 completes the evaluation drafted on day 29."

### Unit 4 (s04.md, days.csv)

- **U4-1.** A4 is now one sequence item of six undated cards, labelled as written by Curio Class for practice, plus one sentence on a case not studied for S49. The split is A1 16, A2 10, A3 6, A4 8, with the research-one ruling noted.
- **U4-2.** China was added to A3, its key and the day 46 teacher line.
- **U4-3.** A day 50 line covers the March 2025 removal of the Defense Department's Code Talker pages and the January 2025 Air Force video pull, both restored. It also names two living Code Talkers as of August 2026.
- **U4-4.** E45 now asks for two of three spaces and is labelled. E50 asks for two accounts plus the Navajo source.
- **U4-5.** A CW4 line follows the testimony rights note.
- **CW3 line** added.

### Unit 5 (s05.md, days.csv)

- **U5-1.** A2d now asks for two roles. A2e asks for one United States and one Canadian detail plus Korematsu against 1988, with 2018 in the key. A3 asks for two of four developments plus 1963.
- **U5-2.** Field 4 now says "day 57 opens with the hook". The stale line "Unit 6's plan is not yet written." was removed.
- **U5-3.** The days.csv day 61 note now names day 56's check.
- **U5-4.** E58 and E59 were trimmed.
- **U5-5.** The day 59 line gives the Trump v. Hawaii quote and the 1983 vacatur of Korematsu's conviction.
- **U5-6.** The day 62 line covers Nihon Hidankyo's 2024 Nobel Peace Prize and the survivor figures (99,130 at March 31, 2025; about 91,000 at the end of March 2026). The sensitivity study now includes Korean and other non-Japanese survivors.
- **U5-7.** The day 63 line dates the Smithsonian review to August 2025.
- **U5-8.** Covered by the CW3 line.

### Unit 6 (s06.md, days.csv)

- **U6-1.**
  - A1 now asks for source A's purpose, one limit and a Marshall comparison, plus three 1-minute date items.
  - A2 asks for three flashpoints of the student's choice.
  - A7 asks for the roots, evidence against guilt by association, and the Lavender Scare, because R80 already scores Smith and Kameny.
  - Day 82 now runs A1 9, A2 5, A3 3, A4 2, A5 and A6 together 14, A7 7. The look-fors and scoring note match.
- **U6-2.** The day 78 line covers the Menominee (1973), the Klamath (1986, without reservation land), and the 2024 dam removal with salmon returning that fall. The day 80 line covers the 2009 OPM apology and the January 9, 2017 State Department apology, and notes that Congress has passed no apology.
- **U6-3.** E71 now asks for two of three flashpoints. E77 asks for one place in the city or a suburb plus one link to the rural fringe.
- **U6-4.** Covered by the CW3 line. In days.csv, the day 68 reteach note names day 66's check.

### Unit 7 (s07.md)

- **U7-1.** A days 95 and 96 line: EO 14173 (January 21, 2025) revoked EO 11246; the veteran and disability duties under separate laws remain.
- **U7-2.**
  - A8 now covers fair housing, 2023, Shelby, Callais and Obama in 7 minutes; R96 scores the disparity fields.
  - A6 is now four 1-minute dates plus one demand, 6 minutes.
  - A2 asks for the three organizations, 3 minutes.
  - A1 drops to 8 minutes. The total is 42.
- **U7-3.** The day 90 line names the four Browder plaintiffs and Colvin's arrest at 15. It gives her death on January 13, 2026, at 86.
- **U7-4.** E95 now covers Shelby and Callais only; the 2023 ruling moves to E96. E92 asks for two campaigns plus the 1968 point.
- **U7-5.** Covered by the CW3 line. The stale line "Unit 8 is unwritten." was removed.

### Unit 8 (s08.md)

- **U8-1.** New U3 to U11 fields were added. They include a Section 8.1 U6 table for days 103 to 113 with every row totalling 50 minutes, using Codex's split: opening 5, teaching 15, sources 20, synthesis 5, exit 5. Day 104's readiness station takes the first 10 minutes. Days 110 to 113 keep field 5's and field 7's allocations. U9 and U10 were written.
- **U8-2.** E103 to E109 are now sourced, structured exits on short unseen passages (see Codex 7).
- **U8-3.** B112's Johnson panel asks for two of four programs plus the tension with escalation. The Nixon panel asks for China and the tape, with arms control in the key. The panels run 5, 7 and 6 minutes.
- **U8-4.** The immigration-status line was added to fields 9 and 10 and to U9.
- **U8-5.** The Nixon address is now cited from the American Presidency Project. I checked that the URL is the April 30, 1970 text.
- **CW3 line** added in the new U3.

### Unit 9 (s09.md)

- **U9-1.** Field 6 now gives Huerta's death (October 28, 2026, at 96) and Steinem's (September 3, 2026, at 92). It states Huerta's March 2026 statement once, as her public account. Her own words were added to the sensitivity study.
- **U9-2.** Each survey item now asks for two corrections plus one sentence of evidence. Day 122 now runs orientation 5, A122 22, survey 20, marking 3.
- **U9-3.** A reserved movement-authored hearing excerpt sits beside each president's text: the 1989 ADA testimony and a 1970 Earth Day organizer's testimony, both still to select. The president's text stays the result document.
- **U9-4.** The Skrmetti line uses the verified B.P.J. and Hecox wording: "neither Title IX nor the Equal Protection Clause bars states from limiting girls' teams to biological females".
- **U9-5.** A line covers the endangerment finding rescission (February 2026, challenged in the D.C. Circuit), Sackett (2023), and the June 2026 agreement moving special education management to HHS.
- **U9-6.** S-d and option d now use federal wetland permits under the 1972 water law, with one state's act as the example.
- **U9-7.** The option f look-for adds Pine Ridge and the Oglala Sioux Tribe. The tribe's own pages were added to the sensitivity study.
- **U9-8.** Covered by the CW4 line.

### Unit 10 (s10.md, frame.md)

- **U10-1.** Field 10 sets public-domain hearing and Congressional Record voices for both traditions, still to select. Friedman, Buckley, Harrington and Schlafly are used as attributed paraphrase only.
- **U10-2.** Deregulation was dropped from B133. The split is now directions 3, reading 9, A 12, B 17, C 9.
- **U10-3.** An Iran-Contra teacher sentence was added to field 6, for day 131.
- **U10-4.** Added to the frame.md sensitivity list.

### Unit 11 (s11.md, days.csv, frame.md)

- **U11-1.** A144 asks for one chosen trend plus a change and a continuity. B144 keeps the surveillance judgment and counterclaim, the attacks in one sentence, and one outcome per war. Hamdi and Boumediene moved out of the sitting because W143 scores them.
- **U11-2.** New lines on Section 702 (lapsed June 12, 2026; certifications run to about March 2027), the ACA credits (expired December 31, 2025), and COVID deaths ("more than 1.2 million", to take from the CDC at production).
- **U11-3.** The Iraq card now uses the Iraq Survey Group's findings, cited through the govinfo record of the October 6, 2004 Senate Armed Services hearing. The UK inquiry is optional.
- **U11-4.** Day 140 and the frame's unit 11 row now read "fought as the Cold War ended".
- **U11-5.** The Brackeen (2023) line was added, and the Cherokee Nation is taught in the present tense.
- **U11-6.** The Veterans History Project was added to the sensitivity study.

### Unit 12 (s12.md, days.csv)

- **U12-1.** One form meets the beyond-class audience: by default, the printed briefing sent through the school. Peer panels are the contrasting audience. The briefing's delivery record now meets the criterion, replacing "pending, not met".
- **U12-2.** The standalone writing-time line was added.
- **U12-3.** The Evidence cell for exits 148 to 150 now reads "D3.1 to D3.4 (practised)". The days.csv day 157 note now reads "Practised: D4.7.9-12, D4.8.9-12."
- **U12-4 (applied in part).** The page's own header reads "National Marian Anderson Museum", with "MAHS" used throughout. The citation now gives that name and says it is published by the Marian Anderson Historical Society.

## Applied: the Codex findings

1. **s03 and frame.md.** The unit 3 rationale now points the Keynesian account to Principles of Economics 2e chapter 25 and the monetary account to the Federal Reserve history.
2. **days.csv day 53** (and s04's day list). The goal is now "Wartime liberation of the camps, survivors' immediate needs, and the postwar Nuremberg trials".
3. **days.csv day 49.** The goal now reads "agree, differ or leave uncertainty".
4. **s06 G77.** G77 is a new collected D2.Geo.8 component on day 77, with look-fors and samples. It is counted once, and A6's look-fors keep proposed changes apart from observed ones. Field 10 names the records to use: census urbanized-area layers for 1950 and 1960 (Census Bureau maps or NHGIS) and USGS historical topographic quadrangles. Both are still to confirm and print.
5. **s07 and days.csv day 90.** Day 90 now practises D2.His.5. E90 asks for one feature of the 1957 setting, for example Faubus's use of the National Guard.
6. **s08 day table.** See U8-1.
7. **s08 exits.** E104 contrasts Cuba with a Vietnam advisory decision. E105 is a four-card match, labelled as written by Curio Class. E109 asks for one gain, one abuse and the 1979 point. E106 was applied in part (see "Not applied").
8. **s09 E116.** E116 adds the East Los Angeles walkouts and the International Hotel campaign. Day 116 now has synthesis 2 and exit 8.
9. **days.csv day 140** and frame.md. The Gulf War goal was corrected (with U11-4).
10. **s12.** A ten-session table for the ten-day option keeps 95 writing minutes (25, 30 and 40).
11. **s12 C151.** A one-child fallback was added: an argument written by Curio Class for practice, with two excerpts. It is also on the field 10 production list.
12. **s12 E152.** The actor is now named in the claim, and the key gives February 26 and April 9, 1939.

Codex's structure item 6 (stale "unwritten" lines in s05 to s07, and day 132 changed to 131 in s06) was also applied.

**Disagreements, and which read I followed.** For units 1 and 2, Codex reported no finding where the expert found overload and oversized exits. I followed the expert, under the settled sizing rules. For E106, I followed the settled exit-size rule (see "Not applied").

## Not applied

- **U1-1, the day 1 `assess` cell.** sequence.py rejects `assess = readiness` on day 1. I left the cell blank, as the US History I and US Government fixers did, and the notes carry the timing.
- **CW6 and U9-9 (voice).** These wait for section-plan time, as the expert's item 18 directs.
- **U10-5 (the Economics retrieval).** The expert says s10 needs no change; it goes to the structure pass.
- **Codex 7, E106 (applied in part).** Codex asked for Tonkin, Tet and My Lai in one five-minute exit. Under the settled exit-size rule, E106 keeps Tonkin and Tet, and My Lai stays in day 106's teaching and records.
- **Codex "For Cory" (sections as placeholders).** This is the skeleton's one-section placeholder, a structure question rather than scope, money, people or audience. It goes to the structure pass.

## Unverified

None of these is written as fact in the plans. Each is marked to confirm at production.

- Lessie Benningfield Randle's current status as the last known living Tulsa survivor.
- The living Navajo Code Talkers after August 2026.
- Little v. Hecox's exact disposition, beyond the shared holding.
- The CDC's exact COVID-19 death count and its date.
- The Comptroller's 1893 count of 158 suspended national banks, which comes from a later report and was not checked against the 1893 page.
- A direct federal URL for the Iraq Survey Group's key findings; only the 2004 hearing record was found.
- The total raised by Tulsa's Greenwood trust against its June 2026 goal.
- The specific movement hearing excerpts for A122 (ADA 1989, Earth Day 1970) and the s10 movement voices, which are not yet selected.
- The G77 records' exact sheets, and the Oglala Sioux Tribe's page URL.

## For the structure pass

- **unit_skeleton.py, list parsing.** It parses "one of" lists (T3.5) and "such as" lists (T1.9b, T1.10, T5.1, T5.5) into required parts. It should mark them "choose one; survey the rest".
- **unit_skeleton.py, stock lines.**
  - It writes "day 1 opens with the hook" in every unit's field 4. It should name the unit's first day.
  - Its unit 1 carried line says "start-of-year check before day 1". The frame says day 1's readiness check.
- **sequence.py** rejects `assess = readiness` on day 1, against the lead rule of 2026-11-14 for unit 1. Either allow it on day 1, or record where unit 1's readiness check is marked.
- **Template.** It needs a dated-lines slot. Every fixer has used the end of field 6 for these.
- **U6 table gate.** The template should require a U6 day table for every section. plan.py or unitplan.py could check that every unit day has a minute row (Codex 1, expert). s08, s09 and s10 had no U-fields at all.
- **Composite assessment components.** Each should name its collection day, independent work, source record, criteria and minutes (Codex 2).
- **Optional courses and the readiness clock.** An optional half-year course should not reset the readiness clock (U10-5).
- **Reteach notes.** A gate could check that each reteach note names a day whose `assess` is readiness (CW5).
- **Sensitivity entries.** A gate could require one frame sensitivity entry per unit.
- **D4.7 and D4.8** have no own-word lines.
- **Localization boilerplate.** s10 and s11 carry the "class's own place" lines on national standards (Codex 3). Restrict it to the standards designated for own-state treatment.
- **Source records.** Source-dependent assessment records should name a document before an assessment counts as fully specified (Codex 4).
- **Shorter paths.** They need their own time ledger (Codex 5).
- **Tennessee comparisons.** These are still unverified (Codex 7).
- **Section placeholders.** The skeleton labels each whole unit as one section (Codex's "For Cory" item).

## For Cory

None.
