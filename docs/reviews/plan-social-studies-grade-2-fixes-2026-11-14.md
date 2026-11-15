# Fixes: social-studies-grade-2 unit plans, 2026-11-14

Fixer pass on s01.md to s07.md. Inputs: the Claude expert read (plan-social-studies-grade-2-2026-11-14.md), applied first in its "For the fixer" order, then the Codex read (plan-social-studies-grade-2-codex-2026-11-14.md) for what the expert did not cover.

**Gate.** `python -X utf8 scripts/unitplan.py check social-studies-grade-2` passes s01 to s07. days.csv was touched, so `python -X utf8 scripts/sequence.py check social-studies-grade-2` was also run: 0 failures. The day count and unit totals are unchanged. The counted words per plan are now 1225, 1202, 1202, 1161, 1245, 1234 and 1239, all under 1,250. There are no em or en dashes and no damaged "?" characters in the plans or days.csv.

**Counts.** Expert: 37 findings, 35 applied in full, C5 applied in part, and 5.5 not applied (Codex 6 was used instead). Codex: 11 findings, 10 applied (1, 5 and 9 in the course files only, with their shared records sent to the structure pass), and 7 applied in part.

## Disagreements and which rule was followed

- **Start-of-year check (expert 1.1 against the brief).** The expert placed it on "school day 1". I followed the brief's settled rule instead. The check takes the last ten minutes of day 1, after the hook, and the reteach falls on day 2 or 3.
- **Anna (expert 5.5 against Codex 6).** The expert wanted her "memory of leaving home" read as the hook. The NPS page holds no leaving memory, only the reunion, food, curtains and cookies. I followed Codex 6: the reunion is the hook, and the food embarrassment is held back for day 65. This still meets the expert's aim that no passage is used twice.
- **Day 90 and 91 turns (expert 7.1 against Codex 10).** I followed the expert's settled rotation: about fifteen digital entries a day during supported work on days 89 and 90. Codex 10's day 91 arithmetic needed a fix as well. Each child's spoken presentation is now recorded at the device during the rotation. Day 91 becomes thirty showings of about thirty seconds, each with one listener question. That gives ten minutes for any response, sixteen for the showings, two for transitions and two for the exit, which makes thirty.
- **Exit format.** I applied the kindergarten read's settled K to 2 format, which the expert table also settled. The same paragraph now appears in every unit.

## Findings applied

**Course-wide (expert)**

- **C1. Exit format.** s01 to s06, field 5. The K to 2 paragraph is added above every "Daily evidence" table. Every exit row is rewritten as a mark from every child plus a reason heard from the rotating group. s07 already had this.
- **C2. Assessment load.** Applied through 1.5, 2.3, 3.1, 4.1, 5.4 and 7.1 below.
- **C3. Sensitivity lists.** s02 to s07, field 10. "At least five sources" becomes "every source the frame names for this unit, recorded as reached or not". The missing guides are added under 2.4, 4.3, 5.3, 6.4 and 7.4.
- **C4. Tennessee rows.** Every unit now reads "Not yet compared; the 2024 PDF on tn.gov refuses automated reading."
- **C5. Voice.** Applied in part: the lines I touched in fields 2, 3, 8 and 10 now read as full sentences (see "Findings not applied").

**Unit 1 (s01)**

- **1.1.** Field 4: one printed page of four pictures, in the last ten minutes of day 1. Item 3's "why" is heard from the rotating group on days 2 and 3, and the reteach is on day 2 or 3. Item 4 is now "circle the land, box the water".
- **1.2.** Castle Rock 1911 is replaced by J. H. Colton's Vermont map (New York, 1855; public domain, Commons). The look-fors are rewritten. The field 2 D2.His.11 line now reads "from information in the source itself". The field 10 source is updated.
- **1.3.** Item 4 and the day 13 row: the route sketch is dropped, and the picture graph comes from class counts. The days.csv day 13 goal and its Day list row are changed to match.
- **1.4.** Day 12's exit is four labels on a fresh outline. The full map is collected as the day's work.
- **1.5.** Field 7, day 15: the five minutes are for the teacher to hear any spoken choices not yet heard.
- **Codex 1 (Mercator).** The days.csv day 10 goal now says small shapes are kept and large shapes and sizes change. The Day list row is synced.
- **Codex 2.** Field 8 gains a language support paragraph.
- **Codex 3.** Day 16 adds the student self-check strip.

**Unit 2 (s02)**

- **2.1.** The pair is "about 1905 and today". Today's photograph is the 2019 Zuckerman Commons photo (CC BY 4.0), with a July 2026 alternative named. The 1941 photograph is optional. The details are in field 5 under "Item 5 sources".
- **2.2.** The Aletsch cause now rests on the Swiss Glacier Bulletin 2025 (GLAMOS), which states it. The card wording is our own.
- **2.3.** Items 1 and 2 record globe locations from the rotation at the class globe. Paper globes are optional (field 8), and the coastal photograph prompt is dropped.
- **2.4.** The sensitivity paragraph uses the C3 wording and adds a stereotype check against Randolph and DeMulder (2008).
- **Codex 3.** Day 29 adds the self-check strip.

**Unit 3 (s03)**

- **3.1.** Item 3 is recorded from day 32's retained work and item 7 from day 41's. The Day column stays 44 because the checker needs it, and the text names the recording day. The Learning Card is cut, and the Connections Map shrinks to goods and services, so the packet has three panels and day 44 has five linked tasks.
- **3.1, days.csv.** The day 44 note and the plan's copies of it are updated.
- **3.2.** Field 5 gains "Day 33 cards", which adds one earthquake card (USGS FAQ) and one hurricane card (ready.gov).
- **3.3.** Children read Curio Class's own Flood Card and two Recovery Cards, written from the Montpelier pages' facts. The pages themselves are not reproduced.
- **3.4.** The claim model moves to the start of day 43, in fields 2 and 4. A stray "|" line is also removed.

**Unit 4 (s04)**

- **4.1.** The closing claim uses Trade Stories A only. Item 2b is recorded from day 51's four-row comparison on Country Cards A, and Country Cards B is removed. Day 55 is the claim only. The days.csv notes for days 51, 55 and 56 are updated.
- **4.1, Country Cards A.** It gains two history facts:
  - "In 1868 the city of Edo was renamed Tokyo, and the emperor moved there in 1869."
  - "The first Saudi state began at Diriyah in 1727. The kingdom took the name Saudi Arabia in 1932."
- **4.2.** An item 6 row (D4.1) is added at day 56.
- **4.3.** The sensitivity paragraph gains a Saudi caution: the card shows present-day life and is not a picture of all Muslim or Arab life.
- **Codex 4.** Day 51's exit is the four-category comparison.
- **Codex 5.** The days.csv day 52 goal now uses the plan's wider trade reason. The frame.md unit 4 rationale and the skel "Why this unit" line now read "trade follows from the resources, skills and products places have".

**Unit 5 (s05)**

- **5.1.** Field 5 gains "Cherokee Today" lines: about 4,000 of 16,000 Cherokee died; the other nations forced west are named; and the three federally recognised Cherokee tribes. Each line cites its source. The UKB is added to the frame.md and skel sensitive lines.
- **5.2.** The fallback is used, because no independent record of the 1894 arrival was found. Item 7 adds Antin C, from The Promised Land (1912), marked as the same teller and not a new witness. The plan states plainly that no pair of independent real tellers is compared yet.
- **5.3.** The sensitivity list gets the C3 wording plus NAHJ 2025, YIVO and UNHCR, each recorded as reached or not.
- **5.4.** Item 5 moves to day 70, as a circle task plus a spoken line.
- **5.6.** Day 64's exit is the Cherokee Nation's homeland today.
- **5.7.** The day 63 teacher note gives the Kingdom of Serbs, Croats and Slovenes, which became Yugoslavia in 1929.
- **5.8.** A teacher note on the pressure behind the Antins' move sits in field 5, Antin A. Field 2 points to it.
- **Codex 6.** The held-back day 65 task uses Anna's embarrassment over food, which is in her account. The hook uses the reunion.
- **Codex 7.** The Present Card says "a recent account", and Rahaf is dated to her 2018 interview.

**Unit 6 (s06)**

- **6.1.** The day 78 row and look-for now use the class's own town (own-state method). The newcomers and long-time residents come from the interview timeline, and the Native nation from its own pages. Posadas and the Cherokee Nation immersion school are taught first as worked examples. The field 2 line is adjusted. Field 10 asks the sensitivity read to check the guidance for a school whose nearby nation has no pages.
- **6.2.** Memory M gets a check step: each sentence is matched to a page of The Promised Land and its page number is recorded, and any sentence not found is cut. The new label is "Shortened from Mary Antin's words in The Promised Land, 1912." If fewer than five sentences survive, the memory is swapped for an Ellis Island oral history not used in unit 5.
- **6.3.** The interview prompts add: "We have always lived here" (a Native family, or a family rooted here for generations) is a full answer to the where and when questions, and it is recorded as given.
- **6.4.** FosterClub is named as the foster youth voice source.
- **Codex 8.** The day 77 card now gives the reason: "teaches songs in her new town so neighbors can sing together". The answer key records the reason separately from the means.
- **Codex 9.** The days.csv day 77 and 78 goals drop the universal wording, and the Day list is synced.

**Unit 7 (s07)**

- **7.1 and Codex 10.** The field 5 thirty-minute path is rewritten as set out under "Disagreements" above. Other changes:
  - Item 4 names where the spoken record is made, and the exit rows for days 89 and 91 are adjusted.
  - Revisions are allowed through day 91, and the latest work is scored.
  - The days.csv notes for days 89, 90 and 91 are updated, and the Day list is synced.
- **7.2.** Page I gains the heading "People today" and the sentence "Most people in Iceland live in or near the capital, Reykjavík." Its source is Statistics Iceland, the population on 1 January 2024 (about 63 percent in Greater Reykjavík). The page says "most" because the office later revised its 2024 estimate. Item 2's answer and sample now name one fact for work and one for people.
- **7.3.** Egypt replaces Italy in the menu, with CAPMAS (https://www.capmas.gov.eg/) as the lead.
- **7.4.** The sensitivity list adds two stereotype guides: the Indigenous Journalists Association's reporting guides (formerly NAJA) and Randolph and DeMulder (2008).
- **Codex 11.** The Kenya lead is now the KNBS repository record for Kenya Facts and Figures 2026, marked as Codex asked. Its licence is CC BY-NC 4.0, so it is used as reference only.

## Findings not applied, with reasons

- **Expert 5.5.** It asks for a memory the source does not contain. Codex 6's version was applied instead (see above).
- **Expert C5, in part.** Only the lines touched in this pass were rewritten as full sentences. A whole-plan rewrite of fields 2 and 3 would break the 1,250-word cap in five plans. The model sentence the expert proposes for UNIT-PLAN.md is a shared-file change (structure pass item 6).
- **Codex 7, Omar part.** The UNHCR page for Omar's resettlement in Luxembourg in 2015 returned 403, so that date is not written. Omar keeps the existing "recent account" dating.
- **Codex 1, 5 and 9, shared parts.** The progression rows and the scope-and-sequence wording are shared files, so they go to the structure pass.
- **Day 28 goal.** The goal's "a photograph" is the assessment's own unseen photograph, not the dropped coastal prompt, so no change is needed.

## Unverified (not written as fact)

- Omar's 2015 resettlement in Luxembourg: the UNHCR page returned 403.
- The Colton 1855 Vermont map: whether its imprint is legible at print size. The packet notes it as still to confirm.
- The Brattleboro photographs: whether the 1905 and today views match the same street. This is noted as still to confirm.
- The Antins' 1894 arrival: the dates conflict (May 8 against August 28), from secondary sources only. No arrival date is written.
- The Saudi and Tokyo pages: confirmed only through indexed text of the MOFA pages, plus the Edo-Tokyo Museum.
- FosterClub, UNHCR Teaching About Refugees, and the KNBS booklet: reached only through search or a repository description, not read in full. Each is marked as reached, not read.

## For the structure pass

- **data/progressions/social-studies.csv.** Make the same changes to these rows:
  - ss2-projections: the Mercator wording (Codex 1).
  - ss2-trade-world: the wider trade reason (Codex 5).
  - ss2-culture-migration: drop the universal culture and shared-goal wording (Codex 9).
- **scope-and-sequence.md.** Carry the same wording for days 10, 52, 77 and 78, and the day 90 digital-version wording (now a rotation over days 89 and 90).
- **The day 90 goal.** It still says the digital version is made on day 90. The day 89 and 90 notes now record the rotation; the goal's own wording waits for the canonical records above.
- **Expert structure items 1 to 6, unchanged:**
  - unitplan.py: check the K to 2 exit format.
  - unitplan.py: warn on assessment load.
  - frame.md "Models carried": time order for continuity-change and timeline. Not done here because the skel copies would change.
  - plan-codex.md: the source-count wording.
  - Tennessee: a working route to the grade 2 lines.
  - UNIT-PLAN.md: model sentences for the Teaching and Carried lines.
- **Codex structure items 1 to 7, unchanged:**
  - Compare every mechanical goal and note against days.csv.
  - A conditional response budget in the plan brief.
  - A student self-check field.
  - Keep source leads apart from inspected evidence.
  - Make the frame's island-memory rights wording item by item.
  - Keep the 86-lesson route unvalidated.
  - Read and scan as UTF-8.
- **unitplan.py.** It requires an item row's Day column to be the assessment day. That forced s03's items 3 and 7, recorded on days 32 and 41, to stay listed under 44. A "recorded on" column would show this honestly.

## For Cory

None.
