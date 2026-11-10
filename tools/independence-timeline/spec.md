# Independence Timeline

## One idea
A 1945 world map colored mostly by empire sits above an empty timeline running to 1975, under the question "How did the United Nations grow from 51 members to 144 in thirty years?"; the student drags event cards for eight independence stories (India and Pakistan, Indonesia, Ghana, Algeria, Kenya, Vietnam, Egypt, Mozambique) onto the timeline (first movement, key protest or war, the handover, the first years after) and the map recolors as each nation forms; each card carries a short source in a leader's or an ordinary person's words; the student tags each story's means of change (negotiation, mass nonviolence, armed struggle, or a mix) and a compare view lines the paths up by cost, speed and outcome; at the end a before-and-after panel for each country shows what changed and what stayed after the flag went up (borders drawn by empires, export economies, languages of rule, Partition's displacement), and the student writes which path's result surprised them, so a tenth grader learns change and continuity across the era, compares means of changing societies, and sees how colonial and national decisions reshaped places.

## Not like
- scramble-for-africa (9, spec): how empire arrived. Here how it ended.
- movement-strategy-room (11, concept): U.S. civil rights choices. Here eight nations' paths.
- ideas-that-spread (9, spec): revolutions of 1776 to 1825. Here independence after 1945.
- expansion-map (8, spec): one country growing. Here empires shrinking.

## Who and how
- Grade 10, Social Studies (World History, Civics and Geography), module "Decolonization and Independence". Standards: D2.His.2.9-12 (analyze change and continuity in historical eras), D2.Civ.14.9-12 (analyze historical, contemporary, and emerging means of changing societies, promoting the common good, and protecting rights), D2.Geo.5.9-12 (evaluate how political and economic decisions throughout time have influenced cultural and environmental characteristics of various places and regions).
- Format: timeline. Driver: one student alone, or groups each presenting one country (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Eight stories with four cards each, the recoloring map, path tags, the compare view, eight before-and-after panels, the surprise card. Extra: Group present (each group takes one country and prints its story, tags and panel for a short talk). tool.json `modes: ["Timeline", "Group present"]`, `minutes: "35-45"`, `grades_label: "Grade 10"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.14.9-12 | Tag each story's means of change, then compare paths by cost, speed and outcome | path tags; the compare view | 3 |
| D2.His.2.9-12 | Place cards on the timeline, then sort each country's before-and-after items into changed and continued | the timeline; the before-and-after panels | 2, 4 |
| D2.Geo.5.9-12 | On the map, mark one border, one economy and one language decision for a country and its lasting effect | the map layers: borders, export crops and mines, languages of rule | 4 |

## Screens and modes
Header (kit): title "Independence Timeline"; `Timeline`, `Group present`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A 1945 world map shaded by empire (British, French, Dutch, Portuguese, Belgian) with labels, and an empty timeline from 1945 to 1975. A counter shows United Nations members: 51. The welcome is queued (`welcomeAfter: true`): "In 1945 much of the world was ruled from Europe. By 1975 the United Nations had nearly three times as many members. How did they get there? Pick a country." First hint: "Tap a country card."

**The stories (focus: the timeline and the map).** At 1366x768 the map is above and the timeline below with the card stack right; at 680x425 the stack is a sheet. Four cards per story, each with a short source (under 15 words quoted, credited):
1. India and Pakistan: the Salt March (1930) and Quit India (1942); Gandhi on nonviolence; independence and Partition (August 14 and 15, 1947); some 14 to 15 million people displaced and hundreds of thousands to as many as two million killed, told as numbers and a survivor's line.
2. Indonesia: Sukarno and Hatta proclaim independence (August 17, 1945); war with the Netherlands; transfer of sovereignty (December 27, 1949).
3. Ghana: Kwame Nkrumah and "Positive Action" (1950), strikes and boycotts; elections; independence (March 6, 1957); Nkrumah's words at midnight.
4. Algeria: war with France (1954 to 1962); the FLN; women in the war (Zohra Drif's memoir); torture by the French army, later acknowledged by French presidents; independence (July 5, 1962); about a million European settlers leave.
5. Kenya: land taken for settlers; the Kenya Land and Freedom Army (called Mau Mau by the British) from 1952; detention camps and the Hola killings (1959); in 2013 Britain paid compensation to more than 5,000 Kenyans and said it "sincerely regrets" the abuses; independence (December 12, 1963).
6. Vietnam: Ho Chi Minh's declaration (September 2, 1945) opening with words from the U.S. Declaration of Independence; war with France; Dien Bien Phu (1954); the Geneva division; war with the United States; unification (1975 to 1976).
7. Egypt: nominal independence (1922); the Free Officers (1952); British troops leave; Nasser nationalizes the Suez Canal (July 26, 1956) and the Suez Crisis follows.
8. Mozambique: FRELIMO founded (1962); armed struggle from 1964; Portugal's Carnation Revolution (April 25, 1974); independence (June 25, 1975) under Samora Machel.
- As cards land, the map recolors and the UN counter climbs to 144 by 1975.

**Path tags and compare (D2.Civ.14.9-12).** The student tags each story: negotiation, mass nonviolence, armed struggle, or a mix (most are mixes; India's nonviolence and its Partition violence, Ghana's strikes and elections, Kenya's war and negotiation). The compare view lines up the eight by cost (lives, displacement), speed (years from first movement to handover) and outcome (who held power after). A note: means of change today include these and others (courts, international pressure, elections).

**Before and after (the aha, D2.His.2.9-12, D2.Geo.5.9-12).** For each country a panel of items to sort into Changed (flag, leaders, citizenship, schooling) and Continued (borders drawn by empires; export economies like Ghana's cocoa; French or English as the language of government; Partition's refugees and the Kashmir dispute). On the map the student marks one border, one economy and one language decision and its lasting effect. Then the surprise card: "The path that surprised me was ___ because ___."

**The end.** The timeline, the map, the tags, the compare view and the panels. `Print` prints them.

**Group present (extra).** Each group prints one country's story, tags and panel for a short talk.

## Content
- Eight stories with 32 cards and sources, the recoloring map, the UN counter, path tags, the compare view, eight before-and-after panels with about six items each, the surprise card.
- All people, events, dates, figures and quotes are real and sourced; death tolls are ranges with sources; violence, including torture and Partition killings, is told plainly in words and numbers without images.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards snap to their year; a wrong placement plays a reason line.
- Stories open in any order; the compare view opens after five are placed.
- Keyboard: Tab to cards, the timeline, the map, tags and panels; arrows move a card; Enter places and sorts.
- With Motion off the map recolors at once.

## Look
- Accent `--brand` #8a3d12 terracotta (header, the timeline, cards); gold #f4c542 (the card in hand, a new nation on the map); paper #fbf3ec; ink #2b1205; muted #625046.
- Contrast (WCAG 2.1, computed): white on brand 7.62:1; brand on paper 6.94:1; ink on paper 16.06:1; muted on paper 6.94:1; ink on gold 10.84:1.
- Never color alone: empires carry names and patterns; new nations carry names and years.
- Different from this batch (wallet maroon, workbench green, sea teal, circuit violet).

## Art
- Public domain or openly licensed photographs (Library of Congress, National Archives, national archives of the countries where open, ids checked at build): Gandhi on the Salt March (1930); Nkrumah at independence (1957); Sukarno reading the proclamation (1945); Ho Chi Minh (1946); Nasser (1956); Samora Machel (1975). Each with credit.
- Real faces only for real people; ordinary participants appear through their words, not drawn faces.
- Drawn in code: the map, the timeline, the counter, the compare view, the panels.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the narrator and hints; `news-reader` as the reader of sources and dates, introduced each time as "from" the speaker, never playing them. `Curio.voice` with `scope: () => state.mode + ':' + state.story + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each card.
- event, whole, each source.
- how `place`: "Drag each card to its year on the timeline."
- how `tag`: "Tag how this independence was won."
- how `compare`: "Compare the paths by cost, speed and outcome."
- how `panel`: "Sort what changed and what stayed, then mark it on the map."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the timeline, the recoloring map with the UN counter, path tags, the compare view, before-and-after panels, the surprise card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Timeline | Drop cards anywhere | Each card snaps only to its year. |
| Tags | Tag every story "mix" | Each tag must cite one card as evidence for each means named. |
| Panels | Put everything in Changed | Each item checks; "borders drawn by empires" in Changed plays a reason line. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Card (whole), waits; source (whole).
2. `place`; `tag`, for each story.
3. `compare`.
4. `panel`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.9-12, D2.Civ.14.9-12 and D2.Geo.5.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| UN membership: 51 in 1945, 144 in 1975 | United Nations, "Growth in United Nations membership" | U.S. Department of State, Office of the Historian, "Decolonization of Asia and Africa" | yes |
| Partition: about 14 to 15 million displaced; deaths from hundreds of thousands to about two million | Khan, "The Great Partition" (Yale, 2007) | 1947 Partition Archive; Britannica, "Partition of India" | yes, as a range |
| Indonesia's proclamation (1945) and transfer of sovereignty (1949) | U.S. Department of State, Office of the Historian | Britannica, "Indonesian Revolution" | yes |
| Ghana: Positive Action (1950), independence March 6, 1957 | Britannica, "Kwame Nkrumah" | BBC, "Ghana's independence" archive | yes |
| Algeria: war 1954-62, French army torture acknowledged by later French presidents, independence July 5, 1962 | Horne, "A Savage War of Peace" (1977; NYRB, 2006) | Elysee statements (2018 on Maurice Audin; 2021 on Ali Boumendjel) | yes |
| Kenya: the Emergency from 1952, detention camps, Hola (1959), the 2013 settlement for more than 5,000 claimants | Elkins, "Imperial Reckoning" (Holt, 2005) | UK Foreign Secretary's statement to Parliament (June 6, 2013) | yes |
| Vietnam: the 1945 declaration quoting the U.S. Declaration; Dien Bien Phu and Geneva (1954) | U.S. Department of State, Office of the Historian | Britannica, "Ho Chi Minh" | yes |
| Egypt: the 1952 revolution and the Suez Canal nationalization (July 26, 1956) | U.S. Department of State, Office of the Historian, "Suez Crisis" | Britannica, "Suez Crisis" | yes |
| Mozambique: FRELIMO (1962), the Carnation Revolution (April 25, 1974), independence (June 25, 1975) | Britannica, "Mozambique: independence" | Newitt, "A History of Mozambique" (Indiana, 1995) | yes |
Backed twice: 10. Cut: 0.

Sensitivity note: Partition violence and colonial wars, including torture in Algeria and Kenya, are told plainly with sourced ranges and no images; ordinary participants speak through their own words, never drawn faces. A fresh-agent read of every card is needed before build.

Checks run (Python, scratchpad r18, 2026-11-09): handover years in order (1947, 1949, 1956, 1957, 1962, 1963, 1975); UN members grew by 93 from 1945 to 1975; four cards per story, 32 in all; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map, timeline and stack; at 680x425 sheet.
2. Cards snap to their years and the map and counter update. (D2.His.2.9-12)
3. Path tags cite evidence and the compare view lines up cost, speed and outcome. (D2.Civ.14.9-12)
4. Before-and-after panels sort change and continuity, with one border, economy and language decision marked. (D2.His.2.9-12, D2.Geo.5.9-12)
5. The surprise card prints.
6. Group present prints one country's set.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: instant recoloring; no network requests.

## Open questions
- Sensitivity flag: Partition violence and colonial wars, including torture in Algeria and Kenya (default used: told plainly with sourced ranges, no images, ordinary participants through their words only, fresh-agent read before build).
