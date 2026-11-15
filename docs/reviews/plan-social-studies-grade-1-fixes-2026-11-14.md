# Fixes: unit plans of Grade 1: Leaders, Helpers and Communities

Course `social-studies-grade-1`, s01.md to s08.md, 2026-11-14. Applies the expert read
(docs/reviews/plan-social-studies-grade-1-2026-11-14.md) and the Codex read
(docs/reviews/plan-social-studies-grade-1-codex-2026-11-14.md). Expert "For the fixer" list first, in order, then the
Codex findings it did not cover.

**Gate:** `python -X utf8 scripts/unitplan.py check social-studies-grade-1` passes all eight units.
`python -X utf8 scripts/sequence.py check social-studies-grade-1` 0 failures (days.csv touched; 96 days, unit totals
unchanged). `frame.py check` and `plan.py check` 0 failures for the course.

**Count:** 27 findings applied (all 20 of the expert's, 7 of Codex's 12 in full, plus 3 Codex findings applied in
part under the expert's pattern); 2 not applied.

## Applied, expert read

| Finding | File | What changed |
|---|---|---|
| C1 K to 2 exit format | s01 to s07, field 5 | Each "Daily exit tickets" paragraph replaced with s08's two-part paragraph (each unit's own withholding sentences kept). Every exit row now opens "Mark: ..." with two pictures (the answer and the likely miss); the old question is the spoken why for the rotating six. Rows already on paper keep their task as the mark part (s02 days 11, 13 and 19, calendar and year-strip placement; s03 day 29, the written claim; s05 day 52, the sketch map; s05 day 53 and s06 day 66, the closing claim). "Items ... supply the day's evidence" rows unchanged. |
| C2 assessment days | s01 day 9, s02 day 18, s03 day 30, s04 day 40, s05 day 54, s07 day 79 | Administration paragraph: five minutes orientation, twenty-five for paper parts and spoken groups; the expert's exact sentence added; a "Paper parts" list names each item's circle, match, place or draw part. s02: item 2's tense evidence from the rotation on days 12 to 17 (field 7 marking line updated). s03: item 4's exchange in pairs inside each group of six. s01: item 6's spoken claim heard inside the groups. Rotation evidence from the two days before counts (s03 days 28 and 29, s04 38 and 39, s05 52 and 53, s07 77 and 78). |
| C3 one nation | s04 exit 37, contrast G, field 10 references and study; days.csv day 37 goal | Day 37 uses the Navajo Nation: President and Vice President and a Council of 24 delegates, four-year terms, named by office only, with an "As of November 2026" line (election November 3, 2026). Cherokee government pages replaced by navajo-nsn.gov, navajonationcouncil.org and the Navajo history page. Goal: "(a tribal chair, chief or president)" (field now quoted in the CSV); day list row updated. |
| C4 Tennessee rows | s01 to s08, field 10 | "Not yet compared; the 2024 PDF on tn.gov refuses automated reading." |
| C5 voice | none | No edit now, as the read says (section writer). |
| C6 skeleton | none | Structure pass (below). |
| 1.1 start-of-year check | s01 field 4 | "Given: ... before day 1" and "a few days before opening" removed. Now "Start-of-year check: none needed; retrieval only" (the brief's settled rule) followed by the expert's paragraph: the kindergarten record read before day 1, three access look-fors noted during days 1 to 3, no sitting, no score bars entry. Item table kept as look-fors; gap blocks now fed by the day 1, 3 and 6 retrieval tasks. Rule followed: both agree there is no sitting; the brief's wording supplies the gate line. |
| 1.2 D1.3.K-2 | s01 field 2, item 2 | Indicator line is now "Identify facts and concepts associated with a supporting question"; item 2's part cell "Identify facts and concepts (questions written as the row's practice)". D1.4.K-2 to the structure pass. |
| 1.3 item 2 sample | s01 item 2 | Does-not sample: "Is the show fun? Do I like it?" |
| 2.1 our own school | s02 field 10, field 2 | "Our own school first" paragraph added (shortened to fit the word cap: "Otherwise" stands for "Where none can be found without a library visit"); closing adds "The answer may be a plan of which sources to find." |
| 3.1 Huerta | s03 field 2 Limits, field 10; days.csv day 24 note | "As of November 2026" line: died October 28, 2026, taught in the past tense (1930 to 2026); Chavez named in one sentence as co-founder if a child asks; 2026 statements not taught. Sensitivity study: paid reader replaced by the March 18, 2026 statements as reported, an AP obituary and a free article by a Chicano historian the agent names. days.csv day 24 note prefixed; skeleton flag line and day list updated. The expert's OPB link returns 404, so the plan cites an NBC report of the same statement. |
| 3.2 day 23 exit | s03 exit 23 | Invented case is now a leader asking the council to build a school, with builders and families. |
| 5.1 Lenape nations | s05 contrast H, field 10 | "Government pages of Lenape nations today, among them the Delaware Nation and the Delaware Tribe of Indians in Oklahoma and the Stockbridge-Munsee Community in Wisconsin"; the Stockbridge-Munsee history page added to references and to the study ("three Lenape nations' sources"). |
| 5.2 water stand-in | s05 field 5, item 5 | Sentence added, in item 5's cell rather than field 8: field 8 is counted toward the 1,250-word cap and s05 had two words to spare. |
| 6.1 Nairobi | s06 fields 2, 5, 10 | Hook places are Sapporo, Singapore and Nairobi, Kenya; Cherokee Nation kept on day 60 only (field 10 now says day 60). Nairobi teaching-view rule added to the held-out paragraph. References note Nairobi's weather and languages (Kenya High Commission page); city government and ministry of education pages listed as still to read and added to the study. |
| 6.2 bald eagle | s06 field 6, contrast D | "Since December 2024 the bald eagle has been the national bird by law." |
| 6.3 data strips | s06 field 10 | Ten-square strips, "some" or "many", no percent sign. |
| 7.1 citizenship | s07 field 2, field 10 | "As of November 2026" teacher background line (Fourteenth Amendment, Supreme Court upheld June 30, 2026, Trump v. Barbara; not taught as a dispute), with Codex's addition that this covers children of parents here temporarily or without legal status. Field 10: blocked-brochure line replaced by the Fourteenth Amendment transcript and the opinion (syllabus read); opinion added to the study list. |
| 7.2 retrieval | s07 field 4; days.csv days 72 and 46 | s07 field 4 now "Retrieval only" with the day 72 row; s05 field 4 table gains a day 46 row (the globe retrieval moved out of the paragraph into it). days.csv notes and both day lists updated. |
| 8.1 day 87 | s08 fields 5, 7; days.csv day 92 note | Observation days: item 1 on 83, 2 on 85, 3 on 87, 4 on 88, 5 on 89, 6 on 90, 7 and 8 on 92. Day 92's minutes now name items 7 and 8; "Retain confirmed evidence from 83 to 90". Marking: "each of days 83, 85 and 87 to 90". The day 92 note in days.csv said "87 to 90"; changed to "83 to 90" to match (follows from 8.1). |
| 11 day lists | s03, s04, s05, s07, s08 | Changed days.csv rows (24, 37, 46, 72, 92) copied by hand into each "Day list" table; skeleton not rerun. |

## Applied, Codex read (not covered by the expert)

| Codex finding | File | What changed |
|---|---|---|
| 1 two-part exits | s01 to s07 | Same as C1. Codex's day 5 paper and oral split used for s01 day 5. |
| 2 and 3 sentence frames | s01, s02, field 5 | Frames added as a "Sentence frames for English learners" paragraph after Accommodations, not in field 8: field 8 counts toward the word cap. |
| 5 Addams key | s03 item 3 | Sample no longer claims safer places resulted; it ends "Neighbors could get help from the group", and a note says a claimed result is partly shown. |
| 8 south | s05 item 3 | "Which direction is Reed from the fields?" added; key adds "south". |
| 9 symbol evidence | s06 field 5 | Paper format for items 3 to 5 (link to a meaning picture, mark the detail), ambiguous marks need speech, one record column per component, the daily six chosen by missing components, days 66 and 67 for what is unresolved, nothing secure from a name or tune match alone. |
| 10 citizenship | s07 | Merged into 7.1 above. |
| 11 Titcomb | s07 item 2 | "planned a book wagon" in place of "planned routes". |
| 12 frequency | s08 and every new exit paragraph | "about once weekly per child" became "about once every five course days (about every one and a half to two school weeks)". |
| 4, 6, 7 redistribution (in part) | s03, s04, s05, s07 | Where the reads disagree I followed the expert's "Settled by the expert" table: spoken parts in five groups of six on the assessment day, or from the rotation on the two days before. Codex's earlier collection days (s03 days 26 to 29, s04 days 35 to 38, s05 days 45 to 52, s07 days 69 and 75 to 76) are applied only where they fall in those two days, and in s05, where model use on day 46 and the day 52 map already counted. |

## Not applied

- **8.2 (expert), s08 sensitivity study.** s08 already has a "Sensitivity study owed" paragraph (field 10) naming both community sources first, the federal savings page and further sources, and checking unpaid care, bank access, optional giving and privacy. The read's premise is wrong; nothing added.
- **Codex 8 (fixer list), recheck every look-for against the packet.** Done only for the two mismatches the reads named (Addams, Titcomb) and for the minute budgets the new paragraphs set. A full packet recheck needs the packets, which are still to make; it belongs with the section writer.

## Unverified

- Nairobi as "cool highland weather": the long and short rains and English and Kiswahili were confirmed (Kenya High Commission page and search results); "cool" rests on memory. The plan's field 10 names only the rains and languages.
- Navajo Nation President and Vice President term of four years: inferred from the 2022 and 2026 election cycle and an incumbent seeking a second term in 2026 reporting (Navajo Times, KJZZ); the Nation's own President page (opvp.navajo-nsn.gov) was not read. Council delegates' four-year terms rest on secondary sources (an ombudsman summary and an encyclopedia); the Council's own page gives 24 delegates but no term. The plan says "same four-year cycle". The section writer should confirm both on the Nation's own pages.
- The vote count in Trump v. Barbara: reports say 6 to 3, while the Congressional Research Service summary shows a five-justice majority with Justice Kavanaugh concurring in the judgment. No count is written in the plan.
- The 2026 Navajo presidential result (reported as contested, recount called): not written; the plan names offices only.

Verified and written: Huerta's death on October 28, 2026 at 96 (AP via WTTW and member stations); her March 18, 2026 statement (NBC); Trump v. Barbara, decided June 30, 2026 (the Court's slip opinion syllabus, read); bald eagle national bird law, December 24, 2024 (AP, OPB, PBS); Stockbridge-Munsee Community includes Munsee Lenape people (the Community's own history timeline).

## For the structure pass

1. scripts/unit_skeleton.py line 870 and scripts/unitplan.py line 188: add `observe` to the assessment filters (expert C6 and structure item 1; Codex structure item 1). The unitplan gate passing does not check observation items.
2. The one-section unit and its U fields (expert structure item 2); Codex structure item 5 (single sections of nine to thirteen days shown as provisional).
3. The K to 2 two-part exit and observation default in a file writers read (UNIT-PLAN.md social studies fill or the plan brief), with listening frequency worked out from the course's meeting days (expert item 3; Codex items 2 and 3, an evidence map per part).
4. data/progressions/social-studies.csv, ss1-supporting-questions: add D1.4.K-2 and cite it on days.csv days 1 and 21 (expert item 4).
5. plan.py could flag a K row in `assumes` with no "Retrieval task" note in the course (expert item 5).
6. The plan brief's sensitivity line: search the news for each person a unit names (expert item 6).
7. Tennessee: Codex reached an official 2024 crosswalk on tn.gov (Codex structure item 4); the comparison load itself is the structure pass's.
8. The word cap (1,250 outside fields 4 to 6) pushed two of the reads' additions into field 5 and forced small trims in s02, s03, s05 and s07 field 10 and field 3 wording. The cap may need room for dated teacher background lines.
9. Codex structure item 6: precise source records (author, date, reuse, inspection status) per source.

## For Cory

None.
