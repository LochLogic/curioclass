# Fixes: World History I unit plans (2026-11-14)

This fixer pass covers docs/courses/world-history-i/s01.md to s10.md. It works from two reads: the expert read (plan-world-history-i-2026-11-14.md) and the Codex read (plan-world-history-i-codex-2026-11-14.md). The order was the expert's "For the fixer" list first, then the Codex findings the expert did not cover.

**Gate:** `unitplan.py check world-history-i` passes all 10 units. `sequence.py check world-history-i` reports 0 failures. The day count (155) and the unit totals are unchanged.

**Count:** 52 findings: 44 expert findings (1.1 to 10.4) and 8 Codex findings (F1 to F8).
- 46 were applied in full.
- 5 were applied in part, because the rest sits in shared files or still needs reading.
- 1 was not applied, because it belongs to the skeleton (3.2).
- None was rejected outright.
- The expert's "For the structure pass" items and the Codex read's three process findings are listed below and were not applied here.

**Word cap.** unitplan.py caps the counted fields at 1,250 words, and every plan was within about 50 words of it.
- As the US Government fixer did, the dated background lines and source additions went into field 5, which is not counted. They sit under bold headings: "Teacher background, as of November 2026" or "Sources added, as of November 2026". Each heading names the day or item it serves.
- Final counts: s01 1249, s02 1218, s03 1220, s04 1184, s05 1219, s06 1249, s07 1244, s08 1205, s09 1213, s10 1243.

**Facts.** No 2025 to 2026 rulings, laws or official figures were added. These historical citations were checked on the web today:
- **Checked:**
  - the published Massachusetts framework's T3.2f wording ("restoration of temples destroyed in war");
  - the Todai-ji burning (1180) and Chogen's rebuilding;
  - the David Rumsey record for Ortelius's 1570 Turcici Imperii Descriptio;
  - the United States Holocaust Memorial Museum pages;
  - the Smithsonian NMAI Taíno exhibition dates;
  - the Government of Dominica's Kalinago news page;
  - the UNESDOC General History of Africa volume (pf0000060258);
  - the McGill Internet Archive copy of the 1669 Nieuhof translation;
  - the Fadli interview in Inside Indonesia (2024);
  - Legge's Mencius 1B.8 on Wikisource;
  - Britannica on the Buddha's dates.
- **Not found:** "Greenlee's Ottoman map" and "Mestika Latar's remembrance". Under the settled rule, both left the hooks, claims and assessments.

## Expert read: applied

| Finding | File | What changed |
|---|---|---|
| 1.1 readiness timing | s01 field 4 and day list; days.csv days 1 and 6 | The check is now given in the last ten minutes of day 1, after the hook (lead rule, 2026-11-14). Day 1's exit moves to the five minutes before it, and the reteach is on day 2. The day 6 note now reads "uses day 1's readiness items". Scope-and-sequence lines 9 and 34 are not my file (structure pass). |
| 1.2 day 14 sizing and device | s01 fields 5, 8 | Each part is resized by the settled rule. Administration: read 5, A1 7, A2 4, A3 7, A4 8, A5 9, A6 5, total 45. Parts are now scored from earlier work: T1.5c from E7, the D2.Geo.1 technology part from day 10, D1.5 from day 4, D1.1 and D3.1 from day 13, and maps and art from G12. A4 is the map and timeline, on paper. A5 is five checks plus one corroboration question. A6 is cut to two parts. Field 8 now says only day 10 needs a device and day 14 needs none. |
| 1.3 exits | s01 field 4 | E1 to E13 were rewritten on each day's content, with two parts at most. E7, E8, E11 and E12 are labelled "invented for practice". |
| 1.4 Bantu voices | s01 fields 5, 10 | The sensitivity study now leads with South African History Online, Vansina (JAH 36, 1995) and Klieman (2003). |
| 1.5 rights claims | s01 field 10 | The Turin licence and Schoenbrun's DOI and CC BY are both marked "to verify" (see Unverified). |
| 2.1 sizing | s02 field 5 | A1 is 8 minutes, one means per faith, with A1b scored from day 25. A2 asks for one teaching per faith. A3 is 6 minutes. Total: A1 8, A2 12, A3 6, A4 7, A6 12, total 45. |
| 2.2 Ethiopian case | s02 field 5 | Ethiopia is relabelled "Christian practice in Ethiopian forms" and moved to teaching only. A4 uses U1's Mali (medieval) card and a dated later Kongo card (1500s to 1600s, Thornton, JAH 25, 1984). |
| 2.3 second voices | s02 field 5 | The background names a second voice per faith: a Reform Jewish body, a Hindu academic or temple source, and a Mahayana source. Addresses are still to confirm. |
| 2.4 minor | s02 fields 4, 5 | R5's error letter changes from A to C. The Buddha is now "about the fifth century BCE", with a background line giving both datings. An A6 fairness note is added for the Byzantine depth route. E22, E27 and E28 are rewritten on the day's content, and E25 is labelled invented. |
| 3.1 Niane and Levtzion | s03 field 10 | The row now cites UNESDOC pf0000060258, chapter 6. It lists the selection fields still required and the al-Umari chain (written in the late 1330s to 1340s, partly from Cairo informants). Nothing is written from memory. |
| 3.3 sizing | s03 field 5 | A1 asks for three of the five terms (teacher's pick, rotated across forms) plus one application. A2d keeps European contact and the Yuan and Ming achievements. Chinggis to Khubilai and the Silk Roads are scored from day 44's claim. E31 is rewritten and E35 is labelled invented. |
| 4.1 Ategawa | s04 field 5 | A8 and S use the 1275 Ategawa petition as a T3.2f row. It is addressed to the proprietor temple, Jakurakuji, and the threat is omitted. Magna Carta clause 20 is freed for teaching. |
| 4.2 sizing | s04 field 5 | A1 is three boxes in 4 minutes, with paper money from E50. A2 is 6 minutes. A6 is the map plus one comparison; the four-way comparison comes from days 56 and 61. A7 is four short explanations; Parliament comes from day 61. |
| 4.3 Huei Tzompantli and the Triple Alliance | s04 field 5 | A4's answer names the Triple Alliance. A background line gives the Huei Tzompantli finds (dug from 2015, past 2020, more than 650 skulls by 2023, women and children among them). |
| 4.4 minor | s04 field 5 | Background lines added: feudalism as a debated term (Brown 1974, Reynolds 1994), the "Mongol yoke" debate (Halperin, Ostrowski), and mediation notes for the Codex Mendoza (about 1541) and Guaman Poma (about 1615). |
| 5.1 sizing | s05 field 5 | A2's map is scored from E68. A4 asks for three stages, the student's choice; supply and demand comes from E71. The total stays at 45. |
| 5.2 Watson | s05 field 5 | A background line: Watson's thesis is debated (Decker 2009, Squatriti 2014). Teach the evidenced movement of crops and irrigation. |
| 5.3 al-Khwarizmi | s05 field 2 | The closing claim adds his own preface (Rosen's 1831 translation, public domain). |
| 6.1 sizing | s06 field 5 | A7 covers the 1204 sack only: three consequences and an overall judgment. The plague's three consequences are scored from day 87's claim. S5's second pair is kept for the day 89 retry. |
| 6.2 Muslim voices | s06 field 5 | Ibn al-Athir and Ibn al-Qalanisi via Gabrieli (summarize only), plus one Muslim scholarly account, still to choose. |
| 6.3 Choniates | s06 field 5 | Cites Magoulias's translation (Wayne State University Press, 1984), to confirm against the reader. |
| 7.1 readiness owner | s07 field 4 | The R8.1 and R8.2 table is removed. Day 109 now points to s08 field 4, R1 to R4. |
| 7.2 Greenlee | s07 hook, claim, field 5 | Replaced by Ortelius, Turcici Imperii Descriptio (Antwerp, 1570). The David Rumsey record is CC BY-NC-SA, or a public-domain scan from another holder may be used. |
| 7.3 sizing | s07 field 5 | A1 drops location (from E94). A5 drops effects (from day 107). A7 asks for two of three examples. |
| 7.4 Armada | s07 field 5 | A7 uses the French Wars of Religion (1562 to 1598) instead of the Armada. The Armada is neither taught nor assessed. |
| 7.5 Jewish voice | s07 fields 5 | The USHMM pages on Christian persecution of Jews and on blood libel are added. S2 now names the ELCA's Church Council in full. |
| 7.6 Renaissance selections | s07 field 10 | Marked unverified, from memory. A public-domain text and an open-access museum record are to be opened for each before section 7.3. |
| 7.7 minor | s07 fields 4, 5 | Trent 1545 to 1563, Wycliffe 1384 and Hus 1415 are added as base-text corrections. The Mughal exports line and A1's note that 1299 is Osman's traditional date are added. E95, E96 and E98 are trimmed to two parts. |
| 8.1 Whydah | s08 field 5 | A5's answer, its look-for and S1 now name Whydah (Ouidah), the Bight of Benin, 1694, and Churchill's Collection, volume 6, to confirm. |
| 8.2 weak copies | s08 field 5 | Afonso's letters are cited in Brasio, MMA volume 1 (1952), with an English translation to choose. The 1609 edict is to be cited in a named published translation. The field 10 copies are reading copies only. |
| 8.3 Taíno and Kalinago | s08 field 5 | The NMAI exhibition (28 July 2018 to 12 November 2019) is added. The Kalinago source is the Government of Dominica's news page until a council or community page is found. |
| 8.4 day 118 | days.csv 118; s08 day list | The day 118 goal now reads "West and West Central African states". |
| 8.5 A3 | s08 field 5 | "Exchange both ways" is scored from day 122's table. |
| 9.1 Bandanese remembrance | s09 hook, claim, fields 5, 10 | The untraced "Mestika Latar's remembrance" is replaced by the Fadli interview (Inside Indonesia, 2024). It is labelled as a modern interview with the Banda Journal's photographer, not a descendant's account. Song from Another Land is identified as a 2021 short film by Fadli and Fatris MF; it is unseen and not used. Des Alwi stays as the Bandanese author, and E128 now names him. The sensitivity study asks for Banda Eli descendants' own accounts, still to find. |
| 9.2 Nieuhof page | s09 field 5 | U now cites Nieuhof, An Embassy from the East-India Company (London, 1669, trans. Ogilby), in the McGill Internet Archive copy, scan leaf 166, printed page about 133, to confirm. The e-rara page 268 citation is dropped. |
| 9.3 A1 | s09 field 5 | The coercive cost and Bandanese survival are scored from E128. Timing: A1 10, A2 13, A3 12, A4 10, plus 5 marking, total 50, as before. The look-fors are updated. |
| 9.4 minor | s09 fields 2, 4, 5 and day list; days.csv 133 | Day 133 now retrieves grade 7's grid and teaches latitude and longitude in the first ten minutes. The base reads "ETSU ch. 3 (Ming and Tokugawa); the Russia passage belongs to day 141". The Dutch Republic minorities line is added word for word. E128, E129, E130 and E132 are labelled invented. |
| 10.1 W length | s10 field 5 | W is now "about 500 to 700 words". Day 147's 30 minutes end with an outline that places each piece of evidence. A background line gives the reason. |
| 10.2 A1 and A2 | s10 fields 4, 5 | E138 now orders the five events (two parts), and A1's chronology is scored from it. A2 asks only for each philosophy's source of legitimacy and evaluates against one criterion, accountable power. The table rows and look-fors are updated. |
| 10.3 Mencius | s10 fields 5, 6, 10 | Cites Mencius 1B.8 in Legge's 1861 translation (public domain, Wikisource), read today. Error C now cites it. |
| 10.4 Penal Laws | s10 fields 5, 10 | The 1911 Catholic Encyclopedia is labelled a period perspective only, in W's model and the sensitivity study. A current scholarly history is to be chosen (see Unverified). |
| Great Schism citation (with Codex F4) | s02 skel, comparison table, day 24 row; frame.md day 24; days.csv 24 | The citation changes from New York 9.5 to 9.6a. The Tang stays at 9.5c. |

## Codex read: applied

| Finding | File | What changed |
|---|---|---|
| F1 unit 1 coverage | s01 fields 4, 5 | G12 is added as a scored day 12 artifact: the Turin mining map and an unseen Sanchi image. E7's chart is the T1.5c evidence. This follows both reads. |
| F2 A4 construction (in part) | s01 fields 5, 8 | A4 is the map and timeline only, on paper, at 8 minutes. The TOOL-ASKS.md day 14 allowance is not my file (structure pass). |
| F3 religious continuity | s02 field 5 | Applied with 2.2. The Codex read suggested Ogunnaike's 2026 page, which could not be opened, so a dated Kongo card on Thornton was used instead. The medieval card and the later card are kept distinct. |
| F4 Schism | as above | Applied. |
| F5 historian selection (in part) | s03 field 10 | The source chain and the required fields are recorded. The passage reading itself is still to do before section writing. |
| F6 Todai-ji rebuilding | s04 fields 2, 4, 5 and day list; days.csv 52 | Temple rebuilding is restored through the day 52 goal, E52 and A2: burned in 1180, rebuilt under Chogen, the Buddha in 1185, the hall about ten years later. The data/standards file and the progression row are shared (structure pass). |
| F7 readiness | s07 | Applied with 7.1. Both reads agree. |
| F8 day 133 note | days.csv 133; s09 day list | Applied with 9.4. |

**Where the reads differed:**
- **Unit 1:** the expert's sizing rule was followed, together with Codex's G12 and E7 artifacts. The two fit together.
- **Unit 2:** the expert's relabel was followed. Codex's dated later card was kept as a type, with a source that could be traced instead of Ogunnaike.
- **Unit 9:** the Codex read called Latar "traceable through the interview". The expert's settled rule on untraced sources was followed: the interview is used under its own name, and the film stays out.

## Not applied

- **Expert 3.2 (skeleton option expansion):** the change belongs in unit_skeleton.py (structure pass).
- **Expert 1.1, scope-and-sequence.md lines 9 and 34, and the line 111 "West African" wording:** not my file.
- **Codex F2, TOOL-ASKS.md day 14 allowance:** not my file.
- **Codex F3, Ogunnaike cards:** the source could not be verified (403, not found).
- **Codex F5, the full historian passage selection:** still to read. The fields are recorded.

## Unverified

- The Ogunnaike July 2026 page (not opened).
- The Todai-ji Great Buddha Hall completion date of 1195, which the official site does not state; the plan says "about ten years later".
- The volume of Churchill's Collection (6) for Phillips.
- Brasio's MMA page numbers, which come from secondary citations.
- Nieuhof's printed page (about 133) on the McGill scan.
- The details of Thornton (JAH 25, 1984), which has not been read.
- The Turin papyrus licence (CC0?), and Schoenbrun's DOI and CC BY.
- Vansina (1995) and Klieman (2003), which were not read.
- The Kalinago source, which is government news only; no council site was found.
- Song from Another Land (2021), which is unseen.
- Magoulias as the reader's translator.
- English translations still to choose: Afonso's 1526 letters, the 1609 edict, a Muslim scholarly account of the Crusades, a current history of the Penal Laws, and the second voices for each faith in unit 2.
- The Renaissance text and image editions (s07).

## For the structure pass

- **unit_skeleton.py:** print only the lettered options a unit's days cite (expert 3.2). Distinguish owned, reviewed and deferred options (Codex process 3).
- **Codex unit-plan brief:** add the exit rule (one question, at most two parts, "invented for practice" printed) and the assessment sizing rule (per-item minutes; product-day parts come off the sitting).
- **Readiness ownership:** the skeleton should fill an earlier unit's respond day with a pointer to the readied unit's items.
- **Untraceable sources:** add a check that no hook, claim or assessment names a source without a maker, date, holder and licence.
- **docs/courses/world-history-i/scope-and-sequence.md:** day 1 readiness wording at lines 9 and 34; "West and West Central African states" at line 111.
- **TOOL-ASKS.md:** day 14 needs no device; the device minutes are on day 10 (Codex F2).
- **data/standards/ma-hss-2018.txt:** T3.2f lacks "restoration of temples destroyed in war". The wh1-song-kamakura row in data/progressions/social-studies.csv needs the same part (Codex F6).
- **Comparisons:** finish the New York and Tennessee comparison records against the stored New York framework (Codex process 1).
- **Shorter path:** budget or mark the 45-minute shorter route as unvalidated (Codex process 2).
- **Source list:** add the Todai-ji pages, the Ortelius and Rumsey record, the USHMM pages, the NMAI exhibition, the Fadli interview and Legge's Mencius.

## For Cory

None.
