# Expert plan read: World History I, units 1 to 10 (2026-11-14)

Cold read by the curriculum expert of every unit plan of `world-history-i`, written by Codex today from `scripts/unit_skeleton.py` skeletons. This file is the only one edited.

## What I read

- Rules and lens:
  - AGENTS.md;
  - docs/agents/EXPERT.md;
  - docs/GLOSSARY.md;
  - docs/pipeline/briefs/plan-read.md;
  - the social studies lens;
  - the social studies part of docs/ADOPTION-BAR-SUBJECTS.md, items 1 to 14 with the pass rule;
  - docs/courses/social-studies/STANDARD.md.
- Course: docs/courses/world-history-i/frame.md, scope-and-sequence.md and TOOL-ASKS.md.
- Every unit plan, s01.md to s10.md, in full.
- Codex's write notes, docs/reviews/codex-write-world-history-i-s01 to s10-2026-11-14.md.
- Data:
  - data/plans/world-history-i/days.csv (all 160 rows; days 1, 2, 6, 14, 109, 117, 118 and 133 closely);
  - data/plans/world-history-i/source-map.csv (all 47 rows);
  - data/progressions/social-studies.csv rows cited by the plans.
- Settled tables of the earlier reads:
  - docs/reviews/plan-social-studies-grade-3-2026-11-14.md;
  - plan-social-studies-grade-4-2026-11-14.md;
  - plan-us-government-and-politics-2026-11-14.md.
- Web checks:
  - one search each for "Greenlee" Ottoman map and the Bandanese remembrance named in s09 (neither found);
  - the other facts checked below come from my own knowledge, cross-read against the plans' cited sources.
- `scripts/plan.py check` passes: 10 units, 160 days.

## Course verdict

The ten plans are well built. History is current and handled with care: devshirme, Luther's anti-Jewish writings, the Banda conquest, the slave-trade estimates (12.5 million embarked, 10.7 million arrived) and the Pueblo Revolt are named plainly and correctly. Base-text errors in ETSU are caught, and every faith and people is given its own voice, with a few gaps noted below. The source map, the CC BY 4.0 limits and the frame's "no base, partial base for units 7 to 10" are consistent.

The plans are not ready for section writers until three course-wide problems are fixed:
- every end-of-unit assessment is still over its minutes on the settled sizing rule;
- unit 1's readiness check sits before day 1, against the lead rule;
- unit 8's readiness has two different item sets, and two source names in units 7 and 9 cannot be traced to a real source.

Unit 1's day 14 also requires a device, against the frame's paper path.

## Findings by unit

Each finding gives what is wrong, why it matters and the fix, tagged LAYER (plan, skeleton, data or process) and REPEAT (yes means an earlier read already settled the rule, so the fix cites it; new means first seen here).

### Unit 1 (s01, days 1 to 14)

**1.1 Serious. The readiness check sits before day 1.** LAYER plan and data. REPEAT yes (the US Government read's settled row).
- **What is wrong:** Field 4 places the check "in the start-of-year check, within a few days before opening the unit".
- **Why it matters:** The lead rule of 2026-11-14 forbids any sitting before day 1.
- **Fix, s01 field 4:** Replace the "Given" line with: "Given: day 1, the last ten minutes, after the hook. Day 1's exit ticket moves to the five minutes before the check. Reteach on day 2, in the first ten minutes, as already planned."
- **Fix, days.csv day 1 note:** Old: "is served by the start-of-year check before this day". New: "is given in this day's last ten minutes, after the hook; reteach on day 2".
- **Fix, days.csv day 6 note:** Old: "uses the start-of-year check's readiness items (ss7-europe-geo)". New: "uses day 1's readiness items (ss7-europe-geo)".
- **Fix, scope-and-sequence.md:** Line 9, change "in the start-of-year check" to "in day 1's last ten minutes". Line 34, replace "the start-of-year check, before day 1, on grade 7's Europe maps" with "day 1's last ten minutes, after the hook, on grade 7's Europe maps; reteach on day 2".

**1.2 Serious. Day 14's assessment is over its minutes and needs a device.** LAYER plan. REPEAT yes (grade 4 read: assessments sized to their minutes; parts scored on product days come off the sitting).
- **What is wrong:**
  - A6 asks for an enduring issue, two supporting questions, a source plan and a paragraph claim with a counterclaim, all in 11 minutes. On the rule, that is 20 or more.
  - A5 asks for five checks on two sources in 9 minutes.
  - A4 asks for three displays in 8 minutes.
  - The sitting comes to about 60 minutes against 45.
  - A4a's D2.Geo.1 row requires work in the offline editor, which does not yet exist (TOOL-ASKS.md). That breaks the frame's paper path, which records paper as map construction only.
- **Fix, s01 field 5:**
  - Score D1.5's source plan from day 4's plan, and score D3.1 and the claim from day 13's closing claim. A6 keeps one supporting question and one source choice, 5 minutes.
  - A5 keeps the five checks on one unseen source, with one corroboration question on the second, 9 minutes.
  - A4 keeps the map and one of the timeline or comparison chart, and drops the device requirement. Score D2.Geo.1's technology part from day 10's display, using the frame's paper wording.
  - Re-total the sitting to 45 minutes.

**1.3 Moderate. Exit tickets test invented cases, not the day's history.** LAYER plan and process. REPEAT new.
- **What is wrong:**
  - E1 and E3 to E13 use invented societies or documents, so Han and Rome, the Bantu migrations and Srivijaya are never checked.
  - Several exits are four or five parts long; E4 is the worst.
  - E11 (a 350 CE register) and E12 (a 450 CE inscription) look like real sources but carry no label.
- **Why it matters:** Bar item 7 asks exits to use the skill on course content. The lens rules out skills practised on content the course does not teach. An unlabelled realistic invention can be taken as real.
- **Fix:** Rewrite each exit as one question on the day's taught content, with at most two parts. Where an invented case stays, print "invented for practice" on the student page.

**1.4 Minor. The community voices for the Bantu content do not fit.** LAYER plan. REPEAT yes (Native and Indigenous peoples each from their own sources).
- **What is wrong:** The sensitivity study names an Indonesian ministry page and a Buddhist author as the community voices for the Bantu migrations.
- **Fix:** Add African scholarship, for example Kairn Klieman or Jan Vansina on Bantu history, together with an African institution's published account.

**1.5 Minor. Two rights claims are unchecked.** LAYER plan. REPEAT yes (citations exact).
- **What is wrong:** The Turin map image's licence and the Schoenbrun chapter's DOI and CC BY claim are not verified.
- **Fix:** Verify both before section writing, or mark them "to verify" in field 10.

**Checked correct:**
- Res Gestae (U1), Pliny 6.26 (U2) and Ashoka's thirteenth rock edict (U3).
- Every piece of arithmetic in the exits and the assessment.

### Unit 2 (s02, days 15 to 29)

**2.1 Serious. The assessment is over its minutes.** LAYER plan. REPEAT yes.
- **What is wrong:**
  - A2 asks for six origin bands with two linked teachings each, which is twelve explanations, in 12 minutes.
  - A1 asks for three diffusion networks, six means of spread and model M in 10 minutes.
- **Fix:** A2 asks for one central teaching per faith plus the timeline. Score A1b from day 25's product, and cut instances, not parts.

**2.2 Moderate. The Ethiopian case does not show what T2.4 needs.** LAYER plan. REPEAT new.
- **What is wrong:** The evidence for Indigenous practice surviving inside Christianity in Ethiopia is language and reused sites (Yeha, Yared's chant). That shows inculturation, not Indigenous religious practice continuing. Pre-Christian Aksumite religion was largely South Arabian in form.
- **Fix:** Keep the Mali griot evidence. Replace the Ethiopian case with a better-documented one, or relabel it "Christian practice in Ethiopian forms".

**2.3 Moderate. Each faith rests on one community voice.** LAYER plan. REPEAT yes (varied voices, each from its own sources).
- **What is wrong:** Each faith has a single community source:
  - Judaism: Chabad, which is Orthodox;
  - Hinduism: the Hindu American Foundation, an advocacy group whose position on caste is contested;
  - Buddhism: a Theravada site, although the spread taught is mostly Mahayana.
- **Fix:** Add a second voice from a different stream for each: a Reform or Conservative Jewish body; a Hindu academic or temple source; a Mahayana source.

**2.4 Minor fixes.** LAYER plan. REPEAT new.
- The Buddha's dates are given as sixth to fifth century BCE. Add a teacher background line: "Most current scholars place the Buddha's life about 480 to 400 BCE; older books give about 563 to 483."
- R5's error letter should be C, not A.
- A6's unseen source is about Justinian, whom the Byzantine depth-route students already studied. Add a fairness note, or offer a second unseen source for that route.
- E27 and E28 use invented rulers. Rewrite them on the chosen empire (see 1.3).

**Checked correct:** the readiness check on day 15.

### Unit 3 (s03, days 30 to 48)

**3.1 Serious. Day 35's historians were not read.** LAYER plan. REPEAT yes (citations exact).
- **What is wrong:**
  - Day 35's teaching rests on Levtzion and Niane, but only Levtzion's abstract was read (Journal of African History, 1963, doi 10.1017/S002185370000428X).
  - The plan calls Niane "inaccessible", but the UNESCO General History of Africa, volume IV, is openly available on UNESDOC.
- **Fix, s03 field 10:**
  - Read Niane's chapter on Mali in volume IV and the whole of Levtzion's article.
  - Name the primary chain behind the Mansa Musa account: al-Umari, c. 1337 to 1338, writing from Cairo informants; Ibn Khaldun; Ibn Battuta.

**3.2 Moderate. The skeleton prints standard options the unit does not teach.** LAYER skeleton. REPEAT new; it also appears in s04.
- **What is wrong:** Field 2 and the field 5 table expand MA.WHI.T3.2 into options c to l, each marked "deferred".
- **Why it matters:** It adds noise and suggests the unit owns options it does not teach.
- **Fix:** Covered under "For the structure pass".

**3.3 Moderate. The assessment is tight.** LAYER plan. REPEAT yes.
- **What is wrong:** A1 asks for five definitions plus an application in 6 minutes. A2d has five components in 4 minutes.
- **Fix:** Three definitions with one application. Split A2d, or score part of it from the closing claim.

**Checked correct:**
- the Catalan Atlas (1375, Cresques);
- Ibn Battuta at Taghaza and the role of Ibn Juzayy;
- the Yuan dynasty from 1271, and Zheng He in the early Ming;
- Rabban Sauma, 1287 to 1288;
- Great Zimbabwe's gold reaching the coast through Sofala and Kilwa;
- the readiness check on day 30.

### Unit 4 (s04, days 49 to 62)

**4.1 Serious. A8's unseen source does not test the blueprint.** LAYER plan. REPEAT new.
- **What is wrong:** A8 uses Magna Carta clause 20, from the same document taught on day 55. It does not show the blueprint's other half, how subjects saw a ruler.
- **Fix, s04 field 5:** Replace S1 with an original summary of the 1275 petition of the peasants of Ategawa estate, Kii province, to the estate's proprietor about the steward's demands. Paraphrase only, because modern translations are under copyright, and leave out the graphic threat. The other option is a comparable petition in subjects' own voice.

**4.2 Serious. The assessment is overloaded.** LAYER plan. REPEAT yes.
- **What is wrong:**
  - A1 asks for four explanations in 5 minutes.
  - A7 has about ten components in 8 minutes.
  - A6 asks for a map plus a four-way comparison in 6 minutes.
- **Fix:** Score the comparison from day 56's product and the day 61 claim. A6 keeps the map and one comparison. A7 keeps half its instances.

**4.3 Moderate. Mexica sacrifice and the Triple Alliance are thin.** LAYER plan. REPEAT yes (dated background lines).
- **What is wrong:** Human sacrifice is not planned beyond notes, and A4 leaves out the Triple Alliance.
- **Fix:**
  - Add a teacher background line: "Excavations by Mexico's national institute of anthropology and history at the Huei Tzompantli, 2015 to 2020, show sacrifice on a large scale, including women and children. Early Spanish totals are inflated; teach the scale from archaeology."
  - Name the Triple Alliance (Tenochtitlan, Texcoco, Tlacopan) in A4's answer.

**4.4 Minor fixes.** LAYER plan. REPEAT new.
- Add background lines:
  - "feudalism" as a contested label (Brown 1974; Reynolds 1994);
  - "Mongol yoke" as a later Russian term (Halperin; Ostrowski).
- Complete the mediation notes for Guaman Poma (1615) and the Codex Mendoza (about 1541): who made each, for whom, and when.

**Checked correct:**
- Machu Picchu as a royal estate;
- the Classic Maya, about 250 to 900;
- the Mongol attacks on Japan, 1274 and 1281;
- Lanxi Daolong;
- Guo Xi's Early Spring, 1072;
- Henry IV and Gregory VII, 1076;
- the readiness check on day 49.

### Unit 5 (s05, days 63 to 74)

**5.1 Moderate. The assessment is overloaded.** LAYER plan. REPEAT yes.
- **What is wrong:** A4 asks for five stages, exports, supply and demand, and a limit in 6 minutes. A2 asks for four rows plus a map in 7 minutes.
- **Fix:** A4 keeps three stages and the limit. Score A2's map from its teaching day.

**5.2 Moderate. The "Arab Agricultural Revolution" is treated as settled.** LAYER plan. REPEAT yes (dated background lines).
- **Fix, add a background line:** "Watson's 'Arab Agricultural Revolution' (1974, 1983) is debated. Decker (2009) and Squatriti (2014) question its scale; teach the crops' movement, not a settled revolution."

**5.3 Minor. The closing claim hears no Islamic scholar in their own voice.** LAYER plan. REPEAT new.
- **What is wrong:** The closing claim's sources are all European or Latin, though the frame's teacher note asks for Islamic scholars' own voices.
- **Fix:** Add al-Khwarizmi's own preface to the Algebra (Rosen's 1831 translation, public domain, already listed in s02).

**Checked correct:**
- al-Qarawiyyin, 857 or 859, as mosque learning;
- Oxford teaching from 1096 and its corporation by 1231;
- Hogendijk on the lost Arabic arithmetic;
- the Diamond Sutra, 868;
- the note that neither scholar worked in Cordoba;
- the readiness check on day 63.

### Unit 6 (s06, days 75 to 89)

**6.1 Moderate. The assessment is over its minutes.** LAYER plan. REPEAT yes.
- **What is wrong:** A1 to A7 total 45 minutes with reading included. A7 asks for six consequences plus an overall judgment in 8 minutes, against about 14 on the rule.
- **Fix:** A7 evaluates one consequence of each kind for one catastrophe and gives one overall judgment, or takes the plague half from day 87's product.

**6.2 Moderate. The Muslim community voice is one popular video.** LAYER plan. REPEAT yes (varied voices).
- **What is wrong:** The only Muslim community source is a Yaqeen Institute video whose title presents Salahuddin as a legend. It is a single, celebratory, popular source.
- **Fix:** Keep it as one community perspective. Add a Muslim scholarly source, and use Ibn al-Athir and Ibn al-Qalanisi beside Usama as medieval Muslim voices (Gabrieli's Arab Historians of the Crusades; summarize, under copyright).

**6.3 Minor. The Choniates translation is cited from a course reader.** LAYER plan. REPEAT yes (citations exact).
- **What is wrong:** The link is a course reader on a personal MIT page. The translation is most likely Magoulias's (Wayne State University Press, 1984), which is under copyright.
- **Fix, field 10:** Cite "Nicetas Choniates, O City of Byzantium, trans. H. J. Magoulias (1984); summarize only."

**Checked correct:**
- the Spyrou et al. 2022 study of Kyrgyzstan burials from 1338 to 1339;
- the dates in E77;
- S1's claim that Mexica bondage was generally not inherited;
- Equiano's birthplace dispute noted;
- the uses of Anna Komnene and Choniates;
- the plague chapter from OpenStax World History volume 1 (CC BY);
- the Barker, Kloss and Schiel chapters (CC BY 4.0);
- the readiness check on day 74.

### Unit 7 (s07, days 94 to 109)

**7.1 Serious. Unit 8's readiness has two item sets.** LAYER plan. REPEAT new.
- **What is wrong:** s07 field 4 gives R8.1 and R8.2 (Taino, Kalinago, Lenca and Miskito; a colonial sale law). s08 field 4 gives R1 to R4 for the same ten minutes on day 109, with different keys and different repair days.
- **Why it matters:** A teacher cannot tell which to give. Section 8.1's writer and 7.4's writer will build different checks.
- **Fix:** s08 owns its readiness. In s07, after "In its final ten minutes give unit 8's readiness items", replace "below" and the R8.1 and R8.2 table with "(s08 field 4, R1 to R4)". If R8.1's people names are wanted, move them into s08 R3's key as an extension.

**7.2 Serious. "Greenlee's Ottoman map" cannot be traced.** LAYER plan. REPEAT yes (nothing invented passed off as real; citations exact).
- **What is wrong:** The day 94 hook and the day 107 closing claim rest on "Greenlee's Ottoman map". It appears nowhere in field 10's sources, and a search found no such map.
- **Fix:** Name the map in full (maker, title, date, holding institution, licence) and add it to field 10. If it cannot be found, replace it with a dated map with a known licence, for example an Ottoman or European map from an open-access museum collection, or an original Curio Class map of Ottoman expansion, 1300 to 1566.

**7.3 Moderate. The assessment is over its minutes.** LAYER plan. REPEAT yes.
- **What is wrong:** A5 (seven minutes) and A7 (six) are each paragraph-sized chains, 8 to 10 minutes each on the rule. A1 asks for order, location, expansion and governance in 4 minutes.
- **Fix:**
  - A5 keeps Luther, Calvin and the English separation, and drops "effects" (scored from day 107's claim).
  - A7 uses two of its three examples.
  - A1 drops the map location, which is scored from E94.

**7.4 Moderate. The Spanish Armada is used before it is taught.** LAYER plan. REPEAT new.
- **What is wrong:** A7 and its look-for use the Armada (1588). Day 106's cards and E106 name only the French religious wars and the Anabaptists.
- **Fix:** Either add a dated Armada card (1588) to day 106's case set, or change A7's third example to "the French Wars of Religion (1562 to 1598)" and edit the look-for to match.

**7.5 Moderate. The sensitivity study has no Jewish institution's voice on Luther.** LAYER plan. REPEAT new.
- **What is wrong:** The frame asks for Jewish institutions' published accounts of Luther's writings. Field 10 has only a Leo Baeck Institute catalogue record and the 1994 ELCA declaration, which is a Lutheran voice.
- **Fix:** Add, for example, the United States Holocaust Memorial Museum's account of Luther's 1543 tract and its later use. Name S2's author in full: "the Church Council of the Evangelical Lutheran Church in America, Declaration to the Jewish Community, 18 April 1994".

**7.6 Moderate. The Renaissance and print selections are from memory.** LAYER plan. REPEAT yes (citations exact).
- **What is wrong:** The Renaissance primary selections (Leonardo, Michelangelo, Christine, Erasmus, Durer) and Murner's print were "selected from memory, not opened".
- **Fix:** Open and cite editions before section 7.3 is written: Christine's City of Ladies in a public-domain translation, or a summary; Erasmus's Praise of Folly; Durer's Melencolia I (1514) from an open-access museum record. Mark each as unverified until then.

**7.7 Minor fixes.** LAYER plan. REPEAT new.
- Give the base-text corrections exactly, as background lines: "Council of Trent met 1545 to 1563"; "Wycliffe died 1384; Hus was burned at Constance in 1415".
- Add a background line on Mughal exports: "Textiles dominate the evidence; shipbuilding at Surat is documented; firearms exports are thinly evidenced. Teach the standard's list as a claim to test."
- Mark 1299 as Osman's traditional date in A1.
- Several exits have four parts (E95, E96, E98). Trim each to two (see 1.3).

**Checked correct:**
- the Luther letter, 31 October 1517;
- Suleiman's reign, 1520 to 1566;
- Guru Nanak before 1526;
- the Passional (1521) and Murner (1522);
- Basawan's Alexander and Plato folio (Met, open access);
- the Jesuit approval, 1540;
- no readiness check before unit 7, which is correct.

### Unit 8 (s08, days 110 to 125)

**8.1 Moderate. The unseen trader's place is not named.** LAYER plan. REPEAT new.
- **What is wrong:** S1's summary says "supply author, dates, place" but names no place. Phillips's 1693 to 1694 Hannibal voyage traded at Whydah (Ouidah, Bight of Benin), not in Kongo.
- **Why it matters:** Students testing interpretation I about Kongo need to see that this is evidence from another region.
- **Fix, S1 bullet:** Add "at Whydah (Ouidah), in the Bight of Benin, in 1694". In A5's answer, add "S1 comes from the Bight of Benin, so it tests I's first clause about coastal rulers, not Kongo directly". Cite the 1732 printing in Churchill's Collection of Voyages and Travels, volume 6.

**8.2 Moderate. Two key sources are cited from weak copies.** LAYER plan. REPEAT yes (citations exact).
- **What is wrong:** Afonso's 1526 letters are cited from a teacher's Weebly PDF, and the 1609 decree from a blog.
- **Fix:** Cite a recognized edition: Brasio, Monumenta Missionaria Africana, volume 1, for the Portuguese originals, with a named English translation; and a named published translation of the 1609 edict. Keep original summaries.

**8.3 Moderate. The Taino rest on one organization.** LAYER plan. REPEAT yes (varied voices).
- **What is wrong:** The Taino are represented by one organization (UCTP), and the Kalinago are absent.
- **Fix:** Add the Smithsonian National Museum of the American Indian's Taino exhibition materials (2018 to 2019) and a Kalinago Territory source (Dominica).

**8.4 Minor. Day 118's goal says "West African".** LAYER data. REPEAT new.
- **What is wrong:** Kongo is West Central African, as the plan's own limits say.
- **Fix, days.csv day 118 goal:** Change "the trade's effect on West African states" to "the trade's effect on West and West Central African states".

**8.5 Minor. A3 is tight.** LAYER plan. REPEAT yes.
- **What is wrong:** A3 asks for four boxes plus three named explanations in 10 minutes.
- **Fix:** Score "exchange both ways" from day 122's table.

**Checked correct:**
- Legazpi's base, 1565, and Manila, 1571;
- Goa, 1510, and Malacca, 1511;
- the Pueblo Revolt, 1680, and the return in 1692;
- encomienda as a tribute and labor grant;
- Potosí in Bolivia;
- the 12.5 and 10.7 million estimates (Trans-Atlantic Slave Trade Database, 1501 to 1866);
- the invented 240 and 204 example (15 percent);
- Núñez Muley, 1567;
- the readiness check on day 109 (s08's own items), and the assessment timing.

### Unit 9 (s09, days 126 to 137)

**9.1 Moderate. The hook's Bandanese remembrance cannot be traced.** LAYER plan. REPEAT yes (nothing invented passed off as real).
- **What is wrong:** The hook and closing claim rest on "Mestika Latar's remembrance, Song from Another Land". The plan says the film and its translation were unseen, and a search found neither.
- **Fix:** Verify the work and its maker through The Banda Journal project (Muhammad Fadli). If it cannot be confirmed, use what was read, the Fadli interview in Inside Indonesia (2024), and label it plainly. Keep Des Alwi as the second Bandanese author.

**9.2 Moderate. The unseen source's page is unverified.** LAYER plan. REPEAT yes (citations exact).
- **What is wrong:** U's letter terms (every eight years, one hundred men, twenty to court) match the 1656 Qing reply. But printed page 268 of the e-rara compilation was "found in search text, scan unverified".
- **Fix:** Open the scan and record the edition and page. Otherwise cite Nieuhof, An Embassy from the East-India Company (London, 1669), with its page.

**9.3 Moderate. A1 is overloaded.** LAYER plan. REPEAT yes.
- **What is wrong:** A1 asks for shipping, migration, investment, global links, a coercive cost, Bandanese survival and three supported fields in 7 minutes.
- **Fix:** Score the coercive cost and Bandanese survival from E128, and move 3 minutes from A2 (16) to A1.

**9.4 Minor fixes.**
- **Latitude and longitude are retrieved before they are taught.** LAYER plan. REPEAT new. The frame says the latitude-longitude model is first used in unit 9, but day 133's retrieval asks students to explain it. Fix: "retrieve grade 7's grid; teach the latitude-longitude model in the first ten minutes".
- **Day 133's note names Russia.** LAYER data. REPEAT new. The source map puts ch. 3's Russia passage on day 141. Fix, days.csv day 133 note: change "(Russia, Ming, Tokugawa)" to "(Ming, Tokugawa)".
- **The Dutch Republic's mixed faiths need a line.** LAYER plan. REPEAT new. Add: "The Dutch Republic held large Catholic, Mennonite and Jewish minorities; 'Protestant middle class' is the standard's label, not a claim that faith caused wealth."

**Checked correct:**
- the Banda conquest, 1621;
- Venus's phases also fitting the Tychonic model;
- Kepler's use of Tycho's data;
- Hooke, 1665;
- the Nieuhof embassy, 1655 to 1657, published 1665;
- Kaempfer in Japan, 1690 to 1692, published 1727;
- the Maragha scholarship and the transmission caution;
- the timing, which totals 50 minutes.

### Unit 10 (s10, days 138 to 155)

**10.1 Moderate. The argument's length does not fit its drafting minutes.** LAYER plan. REPEAT new.
- **What is wrong:** W asks for 650 to 850 handwritten words, with 35 minutes of drafting on day 148 and 25 minutes of revision on day 150. Grade 9 composing by hand runs at about 10 to 15 words a minute.
- **Fix:** Set W to "about 500 to 700 words". Let day 147's 30 minutes include an outline with evidence placed, so the multi-page aim holds without adding a day.

**10.2 Moderate. A1 and A2 are overloaded.** LAYER plan. REPEAT yes.
- **What is wrong:** A1 asks for chronology, three causes, change, two clauses and a misconception in 11 minutes. A2 asks for four philosophies, each with an example, a source of legitimacy and a limit, plus S2 and a two-criteria evaluation, in 14 minutes.
- **Fix:** A2 asks for legitimacy only for each philosophy and evaluates against one criterion. A1 takes the chronology order from E138's work.

**10.3 Moderate. Mencius comes from memory.** LAYER plan. REPEAT yes (citations exact).
- **What is wrong:** Mencius, the Mandate's main source on day 140 and in error C, is "blocked, from memory".
- **Fix:** Cite Legge's translation (1861, public domain) of Mencius 1B.8, on killing "the fellow Zhou", and read it before section 10.2.

**10.4 Minor. W's model uses a 1911 source.** LAYER plan. REPEAT new.
- **What is wrong:** W's model answer cites the 1911 Catholic Encyclopedia on the Penal Laws, a dated and partisan account.
- **Fix:** Use it as a period perspective only, and add a current history of the Penal Laws if one is cited.

**Checked correct:**
- the dates 1642, 1649, 1660, 1688 and 1689;
- the Nakaz, 1767, sections 9 and 13;
- Locke's sections 95 and 98;
- Wheatley to Occom, 1774;
- "Indians not taxed";
- the Constitution and Bill of Rights dates;
- Spirit of the Laws, 1748;
- the safety of the informed action;
- the minutes on days 146 to 153, which hold.

### Course-wide (from the source map, handoffs and voice)

- **Base text and source map.** Every ETSU row has a decision and a reason. The cuts are justified (units 1 to 6 have no base, and chapter 1's Americas and Asia are taught from the peoples' own sources). Chapter 8's Russia passage is bounded as background. Licence handling is right: CC BY 4.0 text and maps only, each image checked, one credit per adapted day. The frame's "no base, partial base" matches STANDARD.md. No finding.
- **Handoffs.** These are clean, except for 7.1 (the duplicate unit 8 readiness). Units 9 and 10 correctly use retrieval only.
- **Voice.** Plain full sentences throughout. Field 4's daily-evidence tables in units 7 to 9 are dense but readable.
- **Check set.** New York and Tennessee are unverified in most units. That is known and not mine to fix.

## Settled by the expert

| Question | Ruling | Applies to |
|---|---|---|
| Unit 1's readiness check | Day 1's last ten minutes, after the hook; day 1's exit moves before it; reteach on day 2. Nothing sits before day 1. | s01, days.csv 1 and 6, scope-and-sequence lines 9 and 34 |
| Sizing of end-of-unit assessments | The grade 4 rule, cited and not re-argued: about 1 minute per recall item, 2 per one-sentence explanation, 4 to 5 per constructed map, 8 to 10 per paragraph. Product-day parts come off the sitting. Cut instances, never parts. | all ten units |
| Exit tickets | One question on the day's taught content, at most two parts. An invented case is allowed only with "invented for practice" printed on the student page. | all units, worst in 1, 2 and 7 |
| Paper path for D2.Geo.1 | No assessed part needs a device. Day 14 scores the technology part from day 10, paper as construction only. | s01 |
| Unit 4's unseen source | The Ategawa peasants' petition (1275), or an equivalent subjects' own voice; never a passage from a taught document. | s04 A8 |
| Owner of a readiness check | The unit being readied owns its items; the earlier unit's plan points to them. | s07 and s08 |
| A source that cannot be traced | It does not appear in a hook, a claim or an assessment until maker, date, holder and licence are named. | s07 Greenlee, s09 Bandanese remembrance |
| The Buddha's dates | Teach about 480 to 400 BCE, with the older dating noted. | s02 |
| Using the base text | Partial base for units 7 to 10 is consistent with "no base text"; the source map rows stand. | course |

## For the fixer

Exact edits, in order:

1. **s01 field 4, days.csv days 1 and 6, scope-and-sequence lines 9 and 34:** the readiness edits in 1.1.
2. **s01 field 5:** resize the assessment and take the device out of it, as in 1.2.
3. **s07 field 4:** remove the R8.1 and R8.2 table and point to s08 field 4 (7.1).
4. **s07 hook, closing claim and field 10:** name or replace "Greenlee's Ottoman map" (7.2).
5. **s09:** verify or replace the Bandanese remembrance (9.1).
6. **Resize the assessments** (2.1, 3.3, 4.2, 5.1, 6.1, 7.3, 8.5, 9.3, 10.2), cutting instances, not parts, and re-totalling each sitting to its minutes.
7. **s04 A8:** replace S1 with the Ategawa petition summary (4.1).
8. **s07 day 106 or A7:** the Armada fix (7.4).
9. **s08 S1 and A5:** add Whydah and the Churchill citation (8.1).
10. **Background lines:**
    - 2.4, the Buddha's dates;
    - 4.3, the Huei Tzompantli and the Triple Alliance;
    - 4.4, feudalism and the "Mongol yoke";
    - 5.2, the Watson debate;
    - 7.7, Trent, Wycliffe and Hus, and Mughal exports;
    - 9.4, the Dutch Republic's minorities.
11. **Sources:**
    - s02 second voices (2.3);
    - s02 Ethiopian case (2.2);
    - s03 Niane and Levtzion (3.1);
    - s05 al-Khwarizmi (5.3);
    - s06 Muslim sources and Magoulias (6.2, 6.3);
    - s07 USHMM and the full ELCA name, Renaissance editions (7.5, 7.6);
    - s08 Afonso, 1609, Taino and Kalinago (8.2, 8.3);
    - s09 Nieuhof page (9.2);
    - s10 Legge's Mencius and the Penal Laws (10.3, 10.4);
    - s01 Bantu voices, Turin and Schoenbrun (1.4, 1.5).
12. **Exits:** rewrite to one question on the day's content, two parts at most, with the label rule (1.3, 2.4, 7.7).
13. **days.csv:** day 118 goal (8.4) and day 133 note (9.4). Also s09 day 133 retrieval wording (9.4).
14. **s10 W length** (10.1). **s02 R5 letter** and **A6 fairness note** (2.4).

## For the structure pass

- **unit_skeleton.py option expansion (3.2).** When a parent standard has lettered options, print only the options the unit's days.csv rows cite, in both field 2 and the field 5 table. Never print "deferred" options. This is seen in s03 and s04.
- **Exit rule in the Codex unit-plan brief.** Add the exit rule from the settled table. Codex wrote invented-case exits in units 1 and 2, and multi-part exits throughout.
- **Readiness ownership.** When a unit's respond day carries the next unit's readiness, the skeleton should fill the earlier plan with a pointer ("give s0N field 4's items"), not a heading Codex fills with its own items (7.1).
- **Assessment sizing in the brief.** Every unit claimed "45 minutes" while over on the settled rule. Put the per-item minutes and the "product-day parts come off the sitting" rule into the plan brief, so the writer totals by rule rather than by declaration.
- **Untraceable sources.** Before a plan is marked written, a source in a hook, claim or assessment must appear in field 10 with maker and licence. A check could flag a named source in field 2 or 5 that field 10 does not contain.
- **Day 1 wording.** The skeleton's "before day 1" wording is known and already being fixed in the script. The days.csv notes for days 1 and 6 and the scope and sequence still carry it (1.1).

## For Cory

None. No scope, money, people or audience question arose.
