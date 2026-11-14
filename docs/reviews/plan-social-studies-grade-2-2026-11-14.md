# Expert read: unit plans of Grade 2: Places and Peoples of the World

Course `social-studies-grade-2`, units 1 to 7 (s01.md to s07.md). Cold read, 2026-11-14, per
docs/pipeline/briefs/plan-read.md. I did not write these plans.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, docs/GLOSSARY.md,
  docs/pipeline/briefs/plan-read.md and plan-codex.md (the writer's brief), the social studies part of
  docs/ADOPTION-BAR-SUBJECTS.md (items 1 to 14 and "Fails if"), docs/courses/social-studies/STANDARD.md.
- In full: docs/courses/social-studies-grade-2/frame.md, scope-and-sequence.md, s01.md to s07.md;
  data/plans/social-studies-grade-2/days.csv (96 rows); the K-2 list of data/standards/c3-indicators.txt.
- The kindergarten read, docs/reviews/plan-social-studies-kindergarten-2026-11-14.md, for REPEAT tags and its
  "Settled by the expert" table, which I apply here and do not re-argue.
- Gates: `plan.py check` passes the course (sequence social-studies-grade-2: 0 failures); `unitplan.py check
  social-studies-grade-2` passes s01 to s07. No em dashes in any plan.
- The C3 PDF (NCSS rev. 2017), downloaded and read for every K-2 indicator the course cites: the codes in days.csv
  match their verbs (D2.Eco.13 is capital goods and human capital, D2.Eco.14 why people trade, D2.Eco.15 products
  made abroad and sold here and the reverse; D2.His.11 reads "from information within the source itself").
- Web checks this run: [Angel Island Immigration Station Foundation, "Sixteen Questions"](https://www.aiisf.org/vault/16questions)
  (Mock Ging Sing detained ten months in 1937 and 1938, interviewed 1984; Koon T. Lau, 1934, route Hong Kong,
  Shanghai, Yokohama, Hawaii, interviewed 1990: both as the plan says);
  [NPS Ellis Island oral history EI-89](https://www.nps.gov/elis/learn/education/oral-history-ei-89.htm) (Anna Zagar
  Klarich, 1920, joined her mother and aunt; the page says "Yugoslavia");
  [NASA Earth Observatory, Aletsch](https://science.nasa.gov/earth/earth-observatory/glacial-losses-in-the-swiss-alps-154043/)
  (1984 and 2024 Landsat images, credit Michala Garrison; its only stated cause is the warm summer of 2024);
  [Project Gutenberg 20638](https://www.gutenberg.org/ebooks/20638) (Mary Antin, From Plotzk to Boston, 1899);
  [NEA, Artemio Posadas](https://www.arts.gov/honors/heritage/artemio-posadas) (son huasteco, San Luis Potosí,
  settled in the San Francisco Bay Area in 1979, Heritage Fellow 2016). Not inspected: the Castle Rock 1911 map
  margins (the UT Austin image returned a small non-image file to curl), loc.gov images (blocked, as before),
  tn.gov (blocked, known).

## Course verdict

The seven plans are careful on content and honest about sources: every Massachusetts grade 2 code and every owned
C3 indicator has an item, invented sources are labelled invented, hard history is named, the action is the class's
own, and the facts I checked hold. The biggest risk is that units 1 to 6 ignore the K to 2 exit format the writer
was given (only unit 7 uses it) and load their assessment days past what seven-year-olds can do in 25 minutes,
sharpest in unit 3, which the scope and sequence asked to keep short. Unit 1 does define a start-of-year check,
but one that cannot run as written ("a few days before day 1", spoken items for every child); apply the
kindergarten format to the exits and the start-of-year check first, then trim the assessment days and complete the
sensitivity study lists.

Finding counts: course-wide 1 serious, 2 moderate, 2 minor; unit 1, 3 moderate, 2 minor; unit 2, 3 moderate,
1 minor; unit 3, 1 serious, 2 moderate, 1 minor; unit 4, 1 moderate, 2 minor; unit 5, 4 moderate, 4 minor;
unit 6, 2 moderate, 2 minor; unit 7, 1 moderate, 3 minor. Plus 6 items for the structure pass.

## Course-wide findings

### C1. Units 1 to 6 do not use the K to 2 exit format (serious)

LAYER plan. REPEAT yes (kindergarten C1; the writer's brief carried it as settled).
- **What is wrong.** s01 to s06 ask every child, in the last minutes, for written or spoken explanations, often
  three questions at once: s04 day 51 asks for maker and date, a culture judgment and a fact-or-opinion sort; s01
  day 12 asks for eleven labels; s05 day 69 asks three sourcing questions after a written claim. Only s07 field 5
  writes the two-part exit (a paper mark from every child, spoken reasons from a rotating group of about six).
- **Why it matters.** The section writer copies these tables into days; the teacher cannot hear or read thirty
  multi-part answers in two to five minutes, so the next-day responses fire on no evidence.
- **Fix.** s01 to s06, field 5, the paragraph above each "Daily evidence" table: replace it with s07's paragraph
  ("Each exit has two parts. In the final two minutes every child circles, points to, places a token on or draws
  one mark on a printed picture; the teacher reads the prompt aloud. Hear the spoken reason from a rotating group of
  about six during supported work, after teaching, so each child is heard about weekly. The record sheet names the
  rotation."). Then each exit row's first sentence becomes its mark task (circle the picture, the label, the true
  sentence), and its remaining questions become the rotating group's spoken "why". Grade 2 children may write one
  short word or label as the mark. Settled by the kindergarten read; applied here.

### C2. Assessment days carry more than 25 minutes can hold (moderate)

LAYER plan. REPEAT yes (kindergarten 4.1 and 6.1, load).
- **What is wrong.** Day 28 holds seven items plus an extra coastal photograph prompt; day 44 eight items across
  eleven codes and four panels; day 56 six items; day 70 seven items; each in 25 minutes, read aloud, for
  seven-year-olds who "read short texts on their own with support" (frame). The sharpest case is unit 3 (3.1).
- **Fix.** Per unit below (2.3's dropped photograph prompt, 3.1, 4.1, 5.4). The rule for the writer: an assessment
  day holds at most five linked tasks on one unseen packet; codes taught on one day and observed after teaching that
  day may be recorded from that day's retained work (the frame allows observation over the unit's last lessons).

### C3. The sensitivity study lists fall short of the frame (moderate)

LAYER plan. REPEAT yes (kindergarten 5.1).
- **What is wrong.** s04 to s07 write "at least five sources, at least two community voices", which lowers the
  frame's named list. Unit 5 has no immigration style guide and no Jewish community source for the Antin family, and
  its refugee guidance was "indexed only, full page blocked"; unit 6 names no foster-care source; unit 7 names no
  style guide on stereotypes of places and peoples, which the frame asks for.
- **Fix.** In each sensitivity paragraph, replace "at least five sources, at least two community voices" (and
  "Study at least five sources, including two community voices") with "every source the frame names for this unit,
  recorded as reached or not", and add the missing items named under 5.3, 6.4 and 7.4.

### C4. Tennessee rows say "blocked, not retried" (minor)

LAYER process. REPEAT yes (kindergarten C2).
- **Fix.** Each comparison table's Tennessee row reads "not yet compared; the 2024 PDF on tn.gov refuses automated
  reading" until the structure pass loads Tennessee's grade 2 lines.

### C5. The voice is still clipped in fields 2 and 3 (minor)

LAYER process. REPEAT yes (kindergarten C3).
- **What is wrong.** "Retain all four models; withdraw teacher pointing, not access to map information" (s01);
  "Revise region on 49: a physical region can cross country borders" (s04); "Item 5 continued" rows (s03). The
  brief asked for plain full sentences.
- **Fix.** None to the plans now; the section writer writes each move as one sentence with who does what. See "For
  the structure pass", item 6.

## Unit 1. Maps tell stories (days 1 to 16)

Sound map teaching; the projection facts are right (Mercator keeps local angles and enlarges high latitudes; Peters
keeps relative area), and scale stays in whole units.

### 1.1 The start-of-year check cannot run as written (moderate)

LAYER plan. REPEAT yes (kindergarten 1.2).
- **What is wrong.** Field 4 gives the check "a few days before day 1"; course day 1 is school day 2, so there are
  no such days. The four items are spoken questions with "Why?" for every child in ten minutes. Unit 1 does define
  the check's content (four grade 1 rows, keys, gap responses), which the brief asked for; only its running fails.
- **Fix.** s01 field 4, replace "Use this ten-minute start-of-year observation a few days before day 1 to prepare
  supports, without adding a course day. Accept pointing, speech and drawing." with "Give it in ten minutes on
  school day 1, the day before course day 1, as one printed page of four pictures. The teacher reads each prompt
  aloud and every child marks the page: circles what the square stands for (item 1), circles the direction word
  (item 2), circles the map that could show Boulder then (item 3), and circles land and draws a box round water
  (item 4). Item 3's 'why' is heard from the rotating group during days 1 to 3. Where school day 1 is not available,
  the teacher notes the four look-fors during days 1 to 3, as the kindergarten course does." Keep the table and
  the gap responses.

### 1.2 Item 5 asks a seven-year-old to read a 1911 survey margin, and never shows place of origin (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** D2.His.11 asks for maker, date and place of origin "from information within the source
  itself". The day 15 key for Castle Rock is "making place not stated in the supplied margins", with look-fors on
  edition and survey dates and "the director alone is not the cartographer". The place part is only ever met by
  "unknown", and the margin reading is adult archival work (rule d). The own-word line also says "using information
  supplied with it", which lets an archive caption count.
- **Fix.** s01 field 2, D2.His.11 line: "using information supplied with it" becomes "from information in the
  source itself". Field 5, item 5 and field 10: the assessment source becomes a printed source whose own words name
  all three, made large with a read-aloud transcript (a public-domain map or photograph whose imprint names maker,
  year and city, for one a published map's title block "Published by ..., [city], [year]"; the fixer chooses and
  confirms it). Keep "the margin does not say" as day 6's teaching case on the Boulder map. Drop the look-for
  sentence about the director.

### 1.3 Day 13 holds a yard survey, a picture graph, a route sketch and the map plan (moderate)

LAYER plan and data. REPEAT yes (kindergarten 3.1).
- **What is wrong.** Field 5 day 13 and item 4 add counting, a picture graph and a route sketch to the planning day;
  days.csv day 13 names none of them, and day 13 is the only teaching of a picture graph.
- **Fix.** Settled below. s01 field 5, day 13 row: "Observe a familiar room corner or yard. Count up to five of each
  of two kinds of visible features, draw a picture graph with one mark per feature, and sketch a route between three
  landmarks. Then plan the map." becomes "The class counts two kinds of features in the room together; each child
  draws the picture graph from the class counts, then plans the map." Item 4: drop the route sketch. days.csv day 13
  goal: "Plan a map of a familiar place (the school or a park): what to show, symbols for the key, a scale in paces;
  a picture graph of two kinds of features counted together".

### 1.4 Day 12's exit is the whole day's map (minor)

LAYER plan. REPEAT new.
- **Fix.** s01 field 5, day 12 row: the exit marks four places on a fresh outline from a word bank (one country, one
  ocean, the Great Lakes, one mountain range); the full labelled map is the day's work, collected.

### 1.5 Day 15's "comparing short answers" inside the assessment (minor)

LAYER plan. REPEAT new.
- **Fix.** s01 field 7, "five for comparing short answers on paper with pencils down" becomes "five for the
  teacher to hear any spoken choices not yet heard".

## Unit 2. Land, water and climate (days 17 to 29)

Sound: every continent has a named feature, the rain-shadow explanation is accurate, and no child must choose
against home.

### 2.1 The "new" street photograph is from 1941 (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** The frame asks for one main street "in an old and a new photograph". The plan pairs Brattleboro
  about 1905 with 1941, writes "Both dates are past" and an error G for "1941 called today". Children learn change
  between two old pictures; the course's cultural change never reaches the present.
- **Fix.** Settled below. s02 field 10 and item 5: add a present-day, openly licensed photograph of the same
  Brattleboro Main Street view (the fixer finds one with its licence and date); the pair is about 1905 and today,
  and 1941 becomes optional. Item 5's answer and look-for: "between about 1905 and 1941" becomes "between about 1905
  and today".

### 2.2 The glacier's cause rests on a page that does not state it (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Item 5's sample says "The explanation links ice loss with warming". The NASA page the plan
  cites gives only "a particularly warm summer in 2024" as a cause (checked this run); it does not explain forty
  years of loss. Day 24 is flagged "climate read for accuracy".
- **Fix.** s02 field 10, Aletsch bullet: add "The reason card states the long-term cause from a backed source that
  says it (Swiss glacier monitoring, GLAMOS, already in the study list, or a national science body), quoted in our
  own words; the NASA page supplies the images and the 2024 summer only."

### 2.3 Thirty preassembled paper globes (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Exits on days 17 to 20 and item 1 need every child to locate on "your globe"; field 8 calls for
  "preassembled paper globes" for all. Gored paper globes take an adult a long time each, and the frame promises
  printed materials a teacher can run.
- **Fix.** Settled below. s02 field 5 and field 8: each child's globe locations are heard at the class globe in the
  rotating group across days 17 to 27 (item 1's globe part is recorded from this); every child marks the flat map.
  Paper globes become optional. Also drop the extra coastal photograph prompt from the day 28 packet (C2).

### 2.4 People photographs on every continent are not in the study list (minor)

LAYER plan. REPEAT new.
- **Fix.** s02 field 10, sensitivity paragraph, add: "Check the present-day photographs of days 18 and 19 for
  stereotype (Africa shown only as desert and river, Asia only as rural), using a guide on representing places and
  peoples."

## Unit 3. Living with the land (days 30 to 45)

The action cycle is right: class-proposed options checked against published advice, a fair vote, minority reasons
recorded and a look-back that may find the action did not work.

### 3.1 Day 44 is the heaviest assessment of the year, in its heaviest week (serious)

LAYER plan. REPEAT yes (C2; scope and sequence "For the lead" 2 asked for a short assessment).
- **What is wrong.** Eight items, eleven codes, four panels, 25 minutes, on school day 66, with check 1 two days
  later. A writer will build a test most children cannot finish, and check 1 and two respond days follow in the same
  week.
- **Fix.** Settled below. s03 field 5: item 3 (D2.Geo.8.K-2) is recorded from day 32's retained comparison (the row
  already says "Retain each child's comparison"); item 7 (MA.2.T5.3, D2.Eco.13.K-2) from day 41's retained exit
  work; the Learning Card is cut and the Connections Map is cut down to the goods-and-services line item 6 needs.
  Day 44 keeps items 1, 2, 5, 6 and 8 on three panels in 25 minutes. Administration: "Seven linked tasks" becomes
  "Five linked tasks".

### 3.2 Earthquakes and hurricanes are not taught (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** days.csv day 33 and the scope and sequence teach "how floods, earthquakes and hurricanes affect
  people"; every source in the plan is one flood (Montpelier, July 2023).
- **Fix.** s03 field 10, add: "Day 33 adds two short original cards, one earthquake and one hurricane, each naming
  one effect on people and one way people helped, from federal readiness pages (USGS for the earthquake, NOAA or
  FEMA for the hurricane); Montpelier stays the worked case."

### 3.3 Children read sources marked "reference only, rights unconfirmed" (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** The Montpelier Flood Guide and the two recovery accounts are "reference only", yet day 33's exit
  says "After reading Flood Guide and both recovery accounts" and item 4 quotes "The Flood Guide says". Bar item 14:
  reference material is never copied into a page.
- **Fix.** s03 field 10, the Montpelier bullet: add "Children read Curio Class's own short cards written from these
  pages' facts (Flood Card, two Recovery Cards), each with the page's name, date and link as its source line; the
  pages themselves are not reproduced." Field 5: "Flood Guide" becomes "Flood Card" in day 33 and item 4.

### 3.4 Day 41 also carries the claim model (minor)

LAYER plan. REPEAT new.
- **Fix.** s03 field 2, "sourced reasoning on day 41" becomes "sourced reasoning at the start of day 43"; field 4,
  "Before day 41's claim model" becomes "Before day 43's claim model".

## Unit 4. Countries and trade (days 48 to 57)

Accurate on government: Japan's emperor does not govern and the Diet chooses the prime minister; Saudi kings inherit
rule. Trade runs both ways and services cross borders.

### 4.1 Day 55 is a second assessment day (moderate)

LAYER plan. REPEAT yes (C2).
- **What is wrong.** Day 55 ("the written answer") asks for a four-part comparison from unseen Country Cards B and
  an independent claim from unseen Trade Stories A, with no teaching. Country Cards B's "history" facts (a 1964
  railway opening, the 1992 Basic Law) are thin history for MA.2.T4.2.
- **Fix.** Settled below. s04 field 5: item 2b is recorded from day 51's comparison work on Country Cards A (an
  application day after teaching); Country Cards B is cut; day 55 holds the claim only. Country Cards A carries one
  plain history fact each: "Tokyo has been Japan's capital since 1868" and "The first Saudi state began at Diriyah
  in 1727; the kingdom took its name in 1932" (beside Japan's 1947 constitution). The fixer confirms both from the
  countries' own pages.

### 4.2 Item 6 (the claim) is missing from the item table (minor)

LAYER plan. REPEAT new.
- **Fix.** s04 field 5, add a table row: "56 | D4.1.K-2 | Construct an argument with reasons. | Item 6 (see
  look-fors) ... | section 4.1".

### 4.3 Saudi Arabia is the only unelected example and the only Muslim-majority country so far (minor)

LAYER plan. REPEAT new.
- **Fix.** s04 field 10, sensitivity paragraph, add: "Check that Saudi Arabia, the year's only Muslim-majority
  country before unit 7 and its only unelected government, is not read as the picture of Muslim or Arab life;
  Country Cards A shows present-day work, school and city life there."

## Unit 5. People on the move (days 58 to 71)

Strong: slavery through Venture Smith's own narrative (capture, family, work, freedom), Angel Island told at its
real lengths, "a nation of immigrants" with its limits, refugees without disclosure, no simulation.

### 5.1 Cherokee removal is named without its human cost, and the other nations are missing (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Nowhere does the plan say that many people died on the forced journey (BASELINE rule 5; bar
  item 12, "its facts and its human cost"). The scope teaches "the Cherokee and other Native nations"; no other
  nation is named. "Do Cherokee nations still govern?" is answered with two nations; the United Keetoowah Band of
  Cherokee Indians, in Oklahoma, is a third federally recognized Cherokee tribe (from memory; the agent confirms).
- **Fix.** s05 field 5 and 10, Cherokee Today: add "Thousands of Cherokee people died on the forced journey west in
  1838 and 1839; families grieved and rebuilt. The Muscogee (Creek), Choctaw, Chickasaw and Seminole nations were
  forced out too. Today three Cherokee tribes govern themselves: the Cherokee Nation and the United Keetoowah Band in
  Oklahoma, and the Eastern Band in North Carolina." Sensitivity study: the agent confirms each line from the
  nations' own pages.

### 5.2 No pair of independent real accounts is ever compared (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** D2.His.6 and the frame ask for "two accounts of one arrival compared, with the check that each
  teller had their own way of knowing". Day 68 compares Catherine's memory with its retelling; day 69 uses invented
  observers; day 70 pairs Antin A with Antin B, a Curio Class retelling of A. Children learn that a copy is one
  witness (good), but never compare two real tellers who each knew.
- **Fix.** s05 field 5: day 70 keeps Antin B as the copy check and adds one independent record of the same arrival
  (a dated shipping notice or passenger record of the Antin family's 1894 arrival in Boston, from a public-domain
  newspaper or archive; if none is reachable, the second telling in The Promised Land, 1912, with the item asking
  what both say and whether the same teller adds a new witness). Day 68's teaching pair becomes two real accounts of
  one Ellis Island arrival day if the agent finds one; otherwise the plan says plainly that the independent pair is
  first met on day 70.

### 5.3 The study list misses the frame's style guide and a Jewish voice (moderate)

LAYER plan. REPEAT yes (C3).
- **Fix.** s05 field 10, sensitivity paragraph: add an immigration style guide from a journalists' association (for
  one, the National Association of Hispanic Journalists' guidance; the agent confirms the address), a Jewish
  community or museum source on emigration from the Russian Empire for the Antin family, and a refugee agency's
  teaching guidance the agent can read in full (UNHCR's teaching materials as downloadable files, or another
  agency's), recorded as reached or not.

### 5.4 Day 69 also holds item 5 for every child (moderate)

LAYER plan. REPEAT yes (C2).
- **What is wrong.** Day 69 teaches corroboration, models a claim, asks for an independent claim and a three-part
  exit, and the plan adds item 5 orally for each child; days.csv puts item 5 on day 70 as "one spoken line".
- **Fix.** s05 field 5, Administration: replace "Collect item 5's examples orally during day 69's independent work,
  using unseen Example Cards below. Ask its limits question on 70." with "Item 5 is on day 70: each child circles the
  two Example Cards that support the phrase and the two groups it leaves out; the spoken line is heard during the
  independent work."

### 5.5 Anna's reunion is both the hook and a held-back exit (minor)

LAYER plan. REPEAT new.
- **Fix.** s05 field 2, hook: "Read her reunion memory" becomes "Read her memory of leaving home"; the reunion stays
  held back for day 65.

### 5.6 Day 64's exit compares two past views, not past and present (minor)

LAYER plan. REPEAT new.
- **Fix.** s05 field 5, day 64 row, add: "Then: what does the Cherokee Nation say about its homeland today?" so
  D2.His.4 compares past and present.

### 5.7 "Yugoslavia in 1920" (minor)

LAYER plan. REPEAT new.
- **Fix.** s05 field 5, day 63 row, add a teacher note: "In 1920 the country was the Kingdom of Serbs, Croats and
  Slovenes; it took the name Yugoslavia in 1929. The museum's page uses the later name."

### 5.8 The Antin move's pressure has no teacher note (minor)

LAYER plan. REPEAT new.
- **Fix.** s05 field 2, Limits: add "Teacher note: Jewish families in the Russian Empire lived under laws limiting
  where they could live and work; the Antins chose to move, under that pressure."

## Unit 6. Family stories and culture (days 72 to 81)

Careful: any trusted adult, a full school path with the teacher as teller, no status questions, declined answers
recorded as accurate, no costume or tasting.

### 6.1 "All of a community's people" is shown across two separate places (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** MA.2.T3.4 and the frame ask how all of one community's people (newcomers, long-time residents,
  Native nations) enrich it. Day 78 pairs Posadas in the San Francisco Bay Area with Cherokee Nation in Oklahoma
  and tells the teacher to keep them "in their own places"; the look-for meets with two communities, never one.
- **Fix.** Settled below. s06 field 5, day 78 row and look-for: the community is the class's own town (own-state
  method), from the interview timeline (newcomers and long-time residents) and the Native nation whose homeland it
  is, from that nation's own pages; Posadas and Cherokee Nation's language school are the worked examples taught
  first. Field 10: the sensitivity agent checks the own-nation step's guidance for schools whose nearby nation has no
  pages.

### 6.2 Memory M is "adapted" from a memoir without each sentence checked (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Memory M is labelled Mary Antin's memory "not her exact words" and states the mother's store in
  Chelsea, the father's Yiddish newspapers, a poem read to classmates and later printed by a Boston newspaper. A
  composed passage in a real person's voice is where invented detail slips in as a source. It is also the second
  Antin family source in two units, so the family is not wholly unseen.
- **Fix.** s06 field 5, Memory M: add "Before layout, each sentence is matched to a page of The Promised Land and the
  page numbers go in the source record; any sentence not found is cut. Label: 'Shortened from Mary Antin's words in
  The Promised Land, 1912.'" If fewer than five sentences survive, swap Memory M for an Ellis Island oral history not
  used in unit 5 (the agent's choice).

### 6.3 A family that did not move has no answer path (minor)

LAYER plan. REPEAT new.
- **Fix.** s06 field 5, Interview prompts, add: "'We have always lived here' (a Native family, or a family rooted
  here for generations) is a full answer; record it as given."

### 6.4 No foster-care source is named (minor)

LAYER plan. REPEAT yes (C3).
- **Fix.** s06 field 10, sensitivity paragraph: replace "foster-care alumni's published accounts" with a named
  source of foster youth's own published voices (for one, FosterClub's; the agent confirms the address).

## Unit 7. A country up close (days 82 to 93)

The one unit that applies the K to 2 exit format, and does it well. Every menu country has its own printed set, Japan
is the model outside the menu, and the Iceland page and the invented postcard test source choice cleanly.

### 7.1 Day 90's thirty digital turns cannot run (moderate)

LAYER plan. REPEAT yes (kindergarten 6.1, load).
- **What is wrong.** Thirty turns of about forty-five seconds in which an adult enters each child's claim and two
  facts on one device. Entering a claim and two facts takes an adult two minutes or more.
- **Fix.** Settled below. s07 field 5, thirty-minute path: "On 90, model the digital task for four minutes, then use
  twenty-four for thirty individual turns of about forty-five seconds" becomes "The digital entries are made in a
  rotation during supported work on days 89 and 90, about fifteen children a day, each child dictating and checking
  their own entry with the adult; on 90 the class practises presenting while the rotation runs."

### 7.2 Item 2's two facts answer the same supporting question (minor)

LAYER plan. REPEAT new.
- **What is wrong.** Page I's facts (catching fish, preparing fish) both answer the work question, so the item cannot
  show whether a child links facts to different supporting questions (D1.4).
- **Fix.** s07 field 5, Page I: add a second heading "People today" and the sentence "Most people in Iceland live in
  or near the capital, Reykjavík," from Statistics Iceland's population pages; item 2's answer names one fact for
  work and one for people.

### 7.3 Africa has two menu countries, Europe three (minor)

LAYER plan. REPEAT new.
- **Fix.** Settled below. s07 field 10 menu: Italy is replaced by Egypt (source lead: CAPMAS, Egypt's statistics
  agency). Africa then has three and Europe two.

### 7.4 No stereotype guide in the study list (minor)

LAYER plan. REPEAT yes (C3).
- **Fix.** s07 field 10, sensitivity paragraph, add the frame's "style guide on avoiding stereotypes of places and
  peoples" by name (for one, the Native American Journalists Association's reporting guides for the Indigenous
  communities named, and a published guide on representing other countries; the agent confirms both).

## Settled by the expert

| Choice | Reason, in one line | File it touches |
|---|---|---|
| Kindergarten exit format applied to grade 2 (mark from every child, spoken reason from a rotating group of about six) | Settled by the kindergarten read; s07 already uses it | s01 to s06, field 5 |
| Start-of-year check: one printed page, ten minutes, school day 1; else look-fors noted in days 1 to 3 | Course day 1 is school day 2; no days exist "before day 1" | s01, field 4 |
| Unit 1 item 5 uses a source whose own words name maker, year and city | D2.His.11 at grade 2 needs a place it can find | s01, fields 2, 5, 10 |
| Day 13: picture graph from class counts, no route sketch | One new representation, inside the day | s01 field 5; days.csv day 13 goal |
| Brattleboro pair is about 1905 and today | The frame asks for an old and a new photograph | s02, fields 5 and 10 |
| Globe locations heard at the class globe in rotation; paper globes optional | Thirty assembled globes is not a printed material | s02, fields 5 and 8 |
| Unit 3 items 3 and 7 recorded from days 32 and 41; day 44 keeps five tasks | Week 14 load; both are observed after teaching | s03, field 5 |
| Day 33 adds one earthquake and one hurricane card | Taught in full per days.csv | s03, field 10 |
| Item 2b from day 51's work on Country Cards A; Cards B cut; day 55 is the claim | Day 55 had become a second assessment | s04, field 5 |
| Unit 5 item 5 on day 70 as a circle task plus spoken line | days.csv places it there; day 69 is full | s05, field 5 |
| Day 78's community is the class's own town with its Native nation | MA.2.T3.4 asks about one community's people | s06, field 5 |
| Digital entries in a rotation across days 89 and 90 | Thirty adult-typed entries cannot fit one day | s07, field 5 |
| Iceland Page I gains one people-today fact | Item 2 must tell two supporting questions apart | s07, field 5 |
| Menu: Egypt in, Italy out | Africa three, Europe two | s07, field 10 |

## For the fixer (exact edits, in order)

1. s01 to s06, field 5: the exit paragraph and each exit row's first sentence, per C1.
2. s01: field 4 start-of-year paragraph (1.1); field 2 D2.His.11 line and field 5 item 5 and field 10 source (1.2);
   field 5 day 13 row and item 4 (1.3); day 12 row (1.4); field 7 day 15 marking (1.5).
3. days.csv day 13 goal (1.3); then bring the plan's Day list row into line (do not rerun the skeleton).
4. s02: item 5 and field 10 present-day photograph (2.1); field 10 Aletsch cause (2.2); fields 5 and 8 globes and the
   day 28 photograph prompt (2.3); sensitivity paragraph (2.4).
5. s03: field 5 items 3 and 7 and the packet (3.1); field 10 day 33 cards (3.2); Flood Card wording (3.3); fields 2
   and 4 claim model day (3.4).
6. s04: field 5 item 2b and Country Cards A history facts (4.1); item 6 row (4.2); sensitivity paragraph (4.3).
7. s05: Cherokee Today lines (5.1); day 68 and 70 accounts (5.2); sensitivity list (5.3); administration (5.4); hook
   (5.5); day 64 row (5.6); day 63 note (5.7); Limits note (5.8).
8. s06: day 78 row and look-for (6.1); Memory M check and label (6.2); interview prompts (6.3); sensitivity list
   (6.4).
9. s07: day 90 path (7.1); Page I (7.2); menu (7.3); sensitivity list (7.4).
10. Every unit: the "at least five sources" sentence (C3); the Tennessee row (C4).

## For the structure pass

1. scripts/unitplan.py: for a K to 2 course, fail field 5 when its daily evidence paragraph has no rotating-group
   wording. The format was in the writer's brief and still missed six of seven units. REPEAT yes.
2. scripts/unitplan.py: warn when an assessment day lists more than five items, or when a K to 2 exit row asks more
   than one question of every child. REPEAT yes.
3. frame.md "Models carried": the continuity-change and timeline rows put the first use in the later unit ("First
   used: unit 5 ... Used again: unit 2 uses it in review first"), so the skeleton prints "used again here: Unit 2
   ... (from: Unit 5)" in s02 and "introduced or first used here" in s05. Write each row in time order (continuity
   change: kindergarten and grade 1, then units 2 and 5; timeline: grade 1, then units 5 and 6). REPEAT new.
4. docs/pipeline/briefs/plan-codex.md: replace any implied minimum with "study every source the frame names for the
   unit; record each as reached or not". REPEAT yes.
5. Tennessee: load the grade 2 lines (ids and own words) by a route that works, as the kindergarten read asked.
   REPEAT yes.
6. docs/courses/UNIT-PLAN.md: give one model sentence for the Teaching and Carried lines ("On day 27 the teacher
   stops writing the claim; each child writes it, with the frame on the table"). REPEAT yes.

## For Cory

None.

## What is right and should not be touched

- Every lettered part of MA.2.T1 to MA.2.T5.3 and every owned C3 indicator has an item with a meets and a
  does-not sample; parts are scored separately, never averaged away.
- Invented sources are labelled invented everywhere (Willow Garden, Coast and Ridge, Cedar Inlet, Trade Stories,
  Forced Case, Postcard P); real sources carry maker, date and rights.
- Hard history: Venture Smith's own narrative, Angel Island at its real lengths from the interviewees, "a nation of
  immigrants" with Native nations and enslaved Africans named, refugees with no disclosure, no simulation.
- The informed action: options from the class, checked against published advice, a vote that records minority
  reasons, and a look-back that does not claim a poster prevented a flood.
- Unit 6's school interview path and unit 7's exit format.

## What I could not judge

- The Castle Rock 1911 map margins (image not reachable from here); moot if 1.2 is taken.
- The Brattleboro photographs and the Chelsea school photograph (not inspected).
- Whether a public-domain record of the Antin family's 1894 arrival exists online (5.2 gives a fallback).
- Tennessee's grade 2 lines (blocked).

## Sources

- [C3 Framework, NCSS, rev. 2017 PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): every K-2 indicator's verb; 1.2.
- [AIISF, Sixteen Questions](https://www.aiisf.org/vault/16questions): Mock Ging Sing and Koon T. Lau facts in unit 5.
- [NPS, Ellis Island oral history EI-89](https://www.nps.gov/elis/learn/education/oral-history-ei-89.htm): Anna, 5.5 and 5.7.
- [NASA Earth Observatory, Aletsch](https://science.nasa.gov/earth/earth-observatory/glacial-losses-in-the-swiss-alps-154043/): 2.2.
- [Project Gutenberg 20638](https://www.gutenberg.org/ebooks/20638): Antin's 1899 account, 5.2.
- [NEA, Artemio Posadas](https://www.arts.gov/honors/heritage/artemio-posadas): 6.1.
- From memory, not fetched: the deaths on the Cherokee removal and the United Keetoowah Band's federal recognition
  (5.1); the Kingdom of Serbs, Croats and Slovenes renamed in 1929 (5.7); Tokyo as capital from 1868 and the first
  Saudi state at Diriyah in 1727 (4.1); most Icelanders living in the capital area (7.2).

Confidence: C1, 1.1, 3.1, 7.1 likely (classroom arithmetic); 2.2, 3.2, 3.3 firm; 5.1 firm on the deaths, likely on
the third tribe; 5.2, 6.1, 7.3 judgment calls; the rest likely.

## For the source list

- aiisf.org/vault pages and nps.gov/elis oral history pages are readable by WebFetch.
- science.nasa.gov Earth Observatory pages are readable and state image credits.
- maps.lib.utexas.edu topo images answered curl's HEAD with 200 but returned a small non-image file on a full GET;
  a browser is likely needed to inspect map margins.
