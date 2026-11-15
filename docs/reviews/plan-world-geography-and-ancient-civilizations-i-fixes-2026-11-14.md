# Fixes: world-geography-and-ancient-civilizations-i unit plans, 2026-11-14

Fixer pass on s01.md to s11.md. It applies the expert read (plan-world-geography-and-ancient-civilizations-i-2026-11-14.md) and the Codex read (plan-world-geography-and-ancient-civilizations-i-codex-2026-11-14.md). The expert's "For the fixer" list was applied first, in order, then the Codex findings the expert did not cover.

**Gates:**
- `python -X utf8 scripts/unitplan.py check world-geography-and-ancient-civilizations-i` passes all 11 units.
- `python -X utf8 scripts/sequence.py check world-geography-and-ancient-civilizations-i` reports 0 failures.

**Generated blocks:** after the days.csv and frame edits, the skel blocks and day lists were regenerated with scripts/unit_skeleton.py and copied in unchanged. This also added the skeleton's current "Taught and assessed in general form" line to every unit.

## Applied

### All units

- **Tennessee row:** now reads "Not yet compared; the 2024 standards PDF on tn.gov refuses automated reading."
- **Pipeline lines deleted (CW4)** from field 3 handoffs and "Still to make": "not inspected", "not seen", "unseen", "exists yet", "unwritten", "reads remain due", and "subject approach page absent".
- **Handoffs:** each now names the next plan, sNN.md (Codex 4).
- **Error-register footers (CW2):** reworded in s02 to s11 to "repair it in the next practice day's warm-up or inside supported work; protect the day's new teaching". Each footer also says a small group is taught inside supported work.

### days.csv

Day count (160) and unit totals are unchanged.

- **Day 79 goal and note (expert 6.x, Codex 5):** rowers' status is now uncertain. The goal reads "paid sailors and craftworkers, enslaved people in households and workshops, and how far rowers were free or enslaved is uncertain". The note reads "Slavery named plainly where documented; no role play".
- **Day 107 goal (expert 8.2):** authority added. It reads "test each source for origin, what the maker knew (authority), structure and context, and whether other sources agree".
- **Day 120 goal (Codex 8):** adds "and where a device is in the room the electronic map steps practised with feedback".
- **Day 135 note (Codex 9):** now "Returns to day 121's map construction with a dated hurricane track and settlement layer".

### frame.md

- **Row 6:** the same rower wording as day 79. The sensitivity cell reads "Slavery named plainly where documented."
- **Row 8 (expert 8.2):** deleted "(the sourcing questions; authority and the five source checks are grade 9's)".

### s01

- **Day 3 and the source card (Codex 1 and 2):**
  - Day 3 is labelled a constructed investigation.
  - The unidentified lake card T is replaced by the offshore-dust summary from the federal ocean agency, at about 5,000 years ago (checked in its PDF).
  - Day 8 values are labelled constructed practice data.
- **Field 4:** now "Start-of-year check: none needed; retrieval only". The readiness table and gap use are removed. The day 4 repair moves to warm-up or supported work.
- **Item 2 trimmed:** the receipt sub-task is cut, and receipt 322457 is noted as unused. The closing answer is one source, one inference and one limit.
- **Item 4 trimmed:** three placements, a count from 3 BCE to 2 CE, and one century.
- **Day 7:** supported work reads the Sahara maps. On day 8 the worked claim comes off display.
- **Tablet:** called the Drehem tablet, with the Met title "balanced account of Dugga" (11.217.3, about 2039 BCE). The expert read "Dugga" as a garble, but it is a personal name in the museum's title. I kept the title and named the find site.

### s02

- **Timing:** the paragraph now bounds the formats for items 1 and 3 (Codex 3).
- **Item 3c:** now two developments and a two-sentence claim. The expert suggested cutting 3b and 3c. I followed the settled rule "cut instances, never parts" from the other courses' reads, so every part stays assessed.
- **Day 11:** a miss goes to day 12's warm-up or supported work.
- **Day 12:** a five-minute retrieval with no bridge (CW2).
- **Object:** the restricted sickle insert is replaced by Met 548353, hollow-base point 26.253.59, chert, Fayum, about 7000 to 4500 BCE, public domain (record checked). The answer is updated to match.
- **White Sands:** the fact sheet is confirmed as USGS FS 2025-3046.

### s03

- **Muscat item:** re-keyed to May (39.6 C, 0.0 mm). January and March are not dry months in the weather table, so May replaces the suggested month. June is kept as a teacher note: 10.9 mm on 0.1 rain days, a single storm such as Gonu in June 2007. Students see the line "One storm can raise a month's average."
- **Field 2:** the compelling-question bullet is added.
- **Day 55:** the split line is added (expert 3.2).

### s04

- **Item 2a:** three developments (plow, mining, sail) and one growth link. The other five are checked by the day 41 and 42 exits. Codex asked for all eight cells; the expert's trim was followed.
- **Item 3a:** a printed six-name diagram; students circle three groups and draw one power arrow.
- **Item 3b:** two minutes.
- **Item 4a:** two minutes, with the contrast moved to the day 46 and 48 exits.
- **Look-fors:** updated to match. Row 3e moved after 3d.
- **Day 41:** a five-minute retrieval with no bridge; the repair is in day 42's warm-up.
- **Day 47:** the repair is inside supported work.
- **Sensitivity study:** historians of slavery come first.

### s05

- **Item 3:** Ramses II dropped; the day 59 exit checks him.
- **Item 6:** three placements, two achievements and two practices. Farming, surveying and astronomy are checked by the day 62 and 63 exits.
- **Look-fors:** updated.
- **Still to make:** adds a check that the Book of the Dead line is in 125A.

### s06

- **Item 3:** two markets.
- **Item 5:** the answer uses the uncertain-status wording for rowers (Codex 5).
- **Field 10:** the "unverified rower" sentence is removed. Met 241852 and 241837 were checked.

### s07

- **Item 4 (expert 7.1):** one commandment linked to a duty shared by rulers and ruled; three minutes.
- **Item 10 (expert 7.1):** the dated life, the hijra, the Qur'an and the five pillars by name, in four minutes. Ethics are checked by the day 95 exit. The expert named day 96, but day 95's exit is the one that checks ethics.
- **Item 9 (Codex 6):** new cards, unused in teaching: Deuteronomy 6:4, John 1:1 and 1:14, and Qur'an 112:1 to 4 (Pickthall wording checked). The answer, sample and reservation list are updated, and Romans 14:5 stays reserved for item 3. Item 9 now runs six minutes, and the assessment totals 39 of its 40 minutes.
- **Sensitivity sources (expert 7.2), added:**
  - the American Academy of Religion guidelines (2010);
  - the Council on Islamic Education guide for public school teachers (third edition, 1995);
  - the Orthodox Church in America's "An Introduction to the Bible" (2021).
- **Communities today (expert 7.3):** a dated card per faith from the Pew Research Center report of 9 June 2025, using its 2020 figures. A clause is added to the day 89, 92 and 96 exits. The figures:
  - Jews: about 14.8 million, most in Israel and North America;
  - Christians: about 2.3 billion, 28.8 percent;
  - Muslims: 25.6 percent, the fastest-growing major group.

### s08

- **Research packets (expert 8.1):** three vetted packets.
  - Alphabet: bowl 74.51.2286, the Met essay, and Steele 2020 in *Understanding Relations Between Scripts II*, from page 125, CC BY 3.0.
  - Egyptian calendar: Herodotus 2.4 in Macaulay's 1890 translation, and Belmonte 2009, ASP Conference Series 409, pages 116 to 117.
  - Base 60: YBC 7289, and MacTutor's "Babylonian numerals" (2000).
- **Look-fors for items 3 to 8:** written in general form, with one example per packet.
- **Greek alphabet account (expert 8.3):** the job-advert link is replaced by Steele.
- **Item 7:** includes authority (expert 8.2).
- **Exit tickets (expert 8.4, Codex 7):** a full table for days 100 to 111.
- **Closing claim:** generalised.

### s09

- **Task 5 (expert 9.1):** one Axum explanation and one route with a good each way. The China link moves to the day 125 exit, which already asks for it.
- **Task 6 (expert 9.1):** one sentence each on Ghana and Timbuktu, and one P1 and P2 explanation.
- **Look-fors:** updated.
- **Field 4, day 119 (expert 9.2):** a five-minute retrieval; the reteach is inside supported work.
- **Electronic tool (Codex 8):**
  - The tools line now reads "Offline map and graph maker, key tool; does not exist, specification required", with its requirements and its day 120 and 121 jobs.
  - Day 121 has two allocations. With the tool: 5, 15, 20, 5 and 5 minutes. Without it: the paper allocation.

### s10

- **Task 2 (expert 10.1):** the seven mainland countries, Hispaniola's two, Guatemala City and Santo Domingo, and the sentence. The location key is updated.
- **COPINH (expert 10.2):** attributed as "COPINH, a Lenca community organization in Honduras".
- **Miskitu protocol:** its authoring body is named as MASTA (Mosquitia Asla Takanka), October 2012, from the PDF's credits page.
- **Field 4 (expert 10.3):** adds "not the modelling minutes".

### s11

- **Task 5 (expert 11.1):** the credit line is added to the key and the look-fors.
- **Task 2 (expert 11.2):** eight named countries, with French Guiana marked as a territory. The other four are located in atlas practice on 144.
- **Quito (expert 11.3):** "about 0 degrees latitude and 78 degrees west".
- **ONAMIAP (expert 11.4):** described as a national organization of Andean and Amazonian Indigenous women in Peru, not an Aymara-led body.
- **Error B source (expert 11.6):** now cites the populated-place map data used on 133 and 144.
- **Day 146 exit (Codex 10):** gives Acre's dated periods.
- **Background (Codex 10, expert 11.6):** names the Brazilian Amazon monitoring area and adds "estimated" to 3,335 square kilometres.

## Not applied

- **Second Lenca-authored source (expert 10.2):** no current site of a Lenca organization's own (ONILH, MILPAH) was found. It is listed in s10's "Still to make".
- **Aymara-led organization's page (expert 11.4):** none with a current site was found; aymara.org is an archive with unclear authorship. It is listed in s11's "Still to make".
- **Protestant educational page (expert 7.2):** an Orthodox page was added instead, which meets the expert's "Protestant or Orthodox". A Protestant page stays in s07's "Still to make".
- **TOOL-ASKS.md entry (Codex 8):** outside this pass's files. See the structure pass.
- **Empty "Days flagged" skeleton entries (expert CW3; s06 day 75, s08 day 100, s09 day 118, s11 day 143):** these are generated, so I left them. See the structure pass.
- **Progression and scope-and-sequence wording (Codex 5 and 9, expert 8.2):** these are shared files. See the structure pass.

## Unverified

- **Book of the Dead 125A versus 125B** for "I have not encroached on the fields" (s05): the UCL page refused automated reading.
- **Storage jar 74.51.2298a,b** (s06): the "ownership" reading of its inscription is to confirm against the museum record before print.
- **Steele 2020** (s08): the chapter's end page is not confirmed (the OAPEN PDF was blocked).
- **s08 calendar and base-60 packets:** each still needs its second secondary account.
- **Council on Islamic Education guide** (s07): read from a third-party copy of its excerpt; its current edition was not seen.

## For the structure pass

- **data/progressions/social-studies.csv:**
  - ss6-phoenician-trade: give the rowers' status as uncertain, to match day 79;
  - ss6-research-contribution: authority belongs at grade 6, not deferred to grade 9;
  - ss6-caribbean-central-geo: delete "first map they make from data" (day 121 comes first).
- **scope-and-sequence.md line 68:** give the rowers' status as uncertain.
- **docs/courses/world-geography-and-ancient-civilizations-i/TOOL-ASKS.md:** add the offline map and graph maker. It needs four-row data entry, a keyed map, a labelled bar graph, accessible symbols, offline use, no accounts or outside storage, and an unaided mode. Its jobs: day 120 practice with feedback, day 121 unaided.
- **scripts/unit_skeleton.py (CW3):** write a "Days flagged" entry only when the note holds a sensitivity flag. It currently leaves empty entries for s06 day 75, s08 day 100 and s11 day 143, and in s09 a bare base note.
- **"Carried" tags (CW5):** handle them as the expert's read describes.
- **Planning data and gates, the Codex read's structure-pass items:**
  - track source reservations by passage;
  - give each source card an evidentiary status;
  - have the plan check require a full daily exit table;
  - label provisional section numbers;
  - correct the data's "first written law code" for Hammurabi;
  - refresh the sensitivity lists against the data;
  - keep the 45-minute route unresolved.

## For Cory

None.
