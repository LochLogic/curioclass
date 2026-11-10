# Scramble for Africa

## One idea
A map of Africa in 1870 opens drawn with its own states and peoples (Ethiopia, the Asante kingdom, the Sokoto Caliphate, the Zulu kingdom, Buganda, and many more), beside a ghost of the 1914 map in which only Ethiopia and Liberia remain independent; the student drags a year slider from 1870 to 1914 and taps regions to open four layers: who lived and ruled there, which European claim arrived and why (rubber, gold, cotton, rivalry, railways, the Berlin Conference of 1884-85), voices from the time (an African ruler's letter, a missionary, a colonial officer, a trader), and resistance (Adwa in 1896, the War of the Golden Stool in 1900, Samori Toure, Maji Maji, and the Herero and Nama genocide, told plainly); at each region a cause and effect panel links causes to short and long effects, and a final lasting-effects layer shows borders cutting through peoples, cash-crop and mining economies, and railways running only to the coast; the student ends by writing why two people at the time saw the same event so differently, so a ninth grader learns the interacting factors behind each perspective, the complex causes and effects of colonization, and how political and economic decisions reshaped places.

## Not like
- independence-timeline (10, concept): the way out of empire. Here the way in.
- empire-debate (11, concept): the U.S. debate over the Philippines. Here Africa from all sides.
- expansion-map (8, spec): one nation's growth on a slider. Here a continent claimed by many.
- region-compare (6, spec): regions compared today. Here how a region's borders were drawn.

## Who and how
- Grade 9, Social Studies (World History and Geography), module "Imperialism". Standards: D2.His.4.9-12 (analyze complex and interacting factors that influenced the perspectives of people during different historical eras), D2.His.14.9-12 (analyze multiple and complex causes and effects of events in the past), D2.Geo.5.9-12 (evaluate how political and economic decisions throughout time have influenced cultural and environmental characteristics of various places and regions).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Eight regions, four layers each, cause and effect panels, the lasting-effects layer, the two-views card. Extra: Perspective pairs (printable pairs of voice cards on the same event for discussion). tool.json `modes: ["Map", "Perspective pairs"]`, `minutes: "35-45"`, `grades_label: "Grade 9"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.4.9-12 | Open each voice card and tag the factors that shaped the view (faith, profit, sovereignty, race science, survival) | voice cards with factor tags; the two-views card | 2, 5 |
| D2.His.14.9-12 | Link each region's causes to short and long effects on its panel | the cause and effect panel per region | 3 |
| D2.Geo.5.9-12 | Turn on the lasting-effects layer and explain one border, one economy and one railway | borders over peoples, crop and mine maps, coast-bound rail lines | 4 |

## Screens and modes
Header (kit): title "Scramble for Africa"; `Map`, `Perspective pairs`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Africa in 1870, drawn full: states, kingdoms, caliphates and peoples labeled with their own names, trade routes and cities (Timbuktu, Kano, Kumasi, Zanzibar, Addis Ababa from 1886). Small European footholds on the coasts (Algeria, the Cape, Senegal, a few ports). A ghost of the 1914 map shows behind it. The welcome is queued (`welcomeAfter: true`): "In 1870 most of Africa was ruled by Africans. By 1914 almost all of it was claimed by Europe. How did that happen, and how did Africans respond? Drag the slider, or tap a region." First hint: "Tap a glowing region."

**Regions (focus: the map and the layer panel).** At 1366x768 the map fills the left two-thirds with the layer panel right; at 680x425 the panel is a sheet. Eight regions, each with four layers:
1. Ethiopia: Menelik II; his 1891 letter to European powers setting out Ethiopia's borders; Italy's claim; Adwa (March 1, 1896), where Ethiopia defeats Italy and stays independent.
2. The Asante kingdom (Gold Coast): gold and cocoa; British wars through the 1800s; the War of the Golden Stool (1900), led by Queen Mother Yaa Asantewaa.
3. West Africa's interior: Samori Toure's state resists France for nearly two decades until his capture in 1898.
4. The Sokoto Caliphate: British conquest by 1903; rule through local emirs.
5. The Congo: King Leopold II's Congo Free State (1885 to 1908); forced rubber collection and mass death; reports by missionaries and by Roger Casement (1904); Belgium takes over in 1908.
6. German East Africa: the Maji Maji war (1905 to 1907) against forced cotton growing; famine follows, and tens of thousands to hundreds of thousands die.
7. German South West Africa: the Herero and Nama genocide (1904 to 1908); a German order to drive out the Herero; deaths in the desert and in camps; Nama leader Hendrik Witbooi's letters; Germany formally called it genocide in 2021.
8. Southern Africa: the Zulu kingdom's victory at Isandlwana (1879) and later defeat; diamonds and gold; Cecil Rhodes and the British South Africa Company.
- Each region's European-claim layer names motives in plain words: raw materials (rubber, cotton, gold), markets, rivalry between powers, strategic routes, missionaries' aims, and the racist "civilizing" claims used to justify rule, named as claims.
- The Berlin Conference card (1884-85): European powers meet to set rules for claiming African land; no African ruler is invited.

**Voices (D2.His.4.9-12).** Each region holds two or three short voice cards (under 15 words quoted, credited) from different sides: African rulers and resisters (Menelik II, Hendrik Witbooi, Lobengula's 1888 letter to Queen Victoria), a missionary, a colonial officer, a trader. The student tags the factors that shaped each view: faith, profit, sovereignty, race science, survival, rivalry. Period sources that use racist language are paraphrased with a note, never quoted.

**Cause and effect panels (D2.His.14.9-12).** Per region: causes (economic, political, technological: steamships, quinine, the repeating rifle and machine gun, the telegraph) linked to short effects (conquest, forced labor, resistance) and long effects (borders, economies, languages). Each link needs a because.

**The lasting-effects layer (D2.Geo.5.9-12).** Switch it on to see: borders that split peoples (the Maasai between Kenya and Tanzania; the Ewe between Ghana and Togo; Somali people across four states); cash-crop and mining zones (cocoa, cotton, copper); railways that run from mines and farms to the coast rather than between African cities (the Uganda Railway to Mombasa). A note: in 1964 the Organization of African Unity agreed to keep colonial borders to avoid wars. The student explains one border, one economy and one railway in a line each.

**The two-views card (the aha).** The student picks one event (Adwa, the Berlin Conference, the Congo rubber system) and two voices on it, and writes why the two saw it so differently, naming the factors. Narrator: "The same map meant conquest to one person and ownership to another. The people who lived there had their own map already."

**The end.** The student's tagged voices, panels, lasting-effects lines and the two-views card. `Print` prints them.

**Perspective pairs (extra).** Printable pairs of voice cards on the same event for class discussion.

## Content
- The 1870 map with African states, the 1914 map, the slider; eight regions with four layers; about 20 voice cards; factor tags; cause and effect tiles; the lasting-effects layer; the two-views card.
- All people, events, dates, figures and quotes are real and sourced; death tolls are given as ranges with sources; racist period language is paraphrased, never quoted.
- African states and resistance are shown first and in full, not as blank space.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The slider moves claims onto the map year by year; regions open in any order.
- The lasting-effects layer opens after five regions' panels are linked.
- Keyboard: Tab to the slider, regions, layers, voice cards, tags and panels; arrows move the slider; Enter opens and places.
- With Motion off claims appear at once, without spreading.

## Look
- Accent `--brand` #6e4a14 ochre (header, the slider, the layer panel); gold #f4c542 (the open region, a linked tile); paper #faf5ea; ink #231805; muted #5c5244.
- Contrast (WCAG 2.1, computed): white on brand 7.92:1; brand on paper 7.28:1; ink on paper 16.04:1; muted on paper 7.03:1; ink on gold 10.72:1.
- Never color alone: each claim carries the power's name and a pattern; African states carry names; lasting-effects lines carry labels.
- Different from this batch (mill soot, cartographer blue, Atlantic indigo, field olive).

## Art
- Public domain (Library of Congress, British Library, ids checked at build): an 1870s map of Africa; a 1914 map of colonial claims; a print of the Battle of Adwa (Ethiopian painting); a photograph of Menelik II; a photograph of Hendrik Witbooi; the Berlin Conference engraving (1884); a Congo Reform Association page. Each with credit.
- Drawn in code: the base map, states, claims, the slider, lasting-effects lines.
- No images of atrocities; real faces only for real people.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the narrator and hints; `wise-mentor` as the reader of voice cards, introduced each time as "from" the writer, never playing them. `Curio.voice` with `scope: () => state.mode + ':' + state.region + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each layer card.
- event, whole, each voice card.
- how `tag`: "Tag the factors that shaped this view."
- how `panel`: "Link each cause to its effects, and give a because."
- how `lasting`: "Turn on the lasting-effects layer and explain one border."
- how `twoviews`: "Pick one event and two voices, then explain why they differ."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the year slider and two maps, region layers, voice cards with tags, cause and effect panels, the lasting-effects layer, the two-views card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag every voice "profit" | Each card checks its tags against the source; a missionary tagged only "profit" plays a reason line. |
| Panels | Link every cause to every effect | Each link checks and needs a because. |
| Lasting effects | Write one word per line | Each line must name a place and a decision. |
| Two views | Pick two voices from the same side | The card needs voices from different sides. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Layer card (whole), waits; voice card (whole).
2. `tag`; `panel`, for each region.
3. `lasting`.
4. `twoviews`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.4.9-12, D2.His.14.9-12 and D2.Geo.5.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Berlin Conference (1884-85), no African rulers present; by 1914 only Ethiopia and Liberia independent | Pakenham, "The Scramble for Africa" (Random House, 1991) | UNESCO, General History of Africa, vol. VII (1985) | yes |
| Adwa (March 1, 1896), Menelik II's victory over Italy; his 1891 border letter | Britannica, "Battle of Adwa" | Jonas, "The Battle of Adwa" (Harvard, 2011) | yes |
| The War of the Golden Stool (1900) and Yaa Asantewaa | Boahen, "Yaa Asantewaa and the Asante-British War of 1900-1" (2003) | Britannica, "Yaa Asantewaa" | yes |
| Samori Toure resisted France until 1898 | UNESCO, General History of Africa, vol. VII | Britannica, "Samory" | yes |
| The Congo Free State (1885-1908), forced rubber collection, the Casement Report (1904) | Hochschild, "King Leopold's Ghost" (Houghton Mifflin, 1998) | UK National Archives, Casement Report | yes |
| Maji Maji (1905-07) and its toll as a wide range | Iliffe, "A Modern History of Tanganyika" (Cambridge, 1979) | Britannica, "Maji Maji rebellion" | yes, as a range |
| The Herero and Nama genocide (1904-08); Germany's 2021 acknowledgment | German Federal Foreign Office statement (May 2021) | Olusoga and Erichsen, "The Kaiser's Holocaust" (Faber, 2010) | yes |
| The OAU's 1964 resolution keeping colonial borders; borders splitting peoples | OAU Cairo Resolution AHG/Res. 16(I) (1964) | Herbst, "States and Power in Africa" (Princeton, 2000) | yes |
| Steamships, quinine and the machine gun as tools of conquest | Headrick, "The Tools of Empire" (Oxford, 1981) | Pakenham (1991) | yes |
Backed twice: 10. Cut: 0.

Sensitivity note: genocide, forced labor and colonial violence are told plainly with sourced ranges and no images of atrocities; racist period language is paraphrased with a note, never quoted; African states and resistance lead every region. A fresh-agent read of every region and voice card is needed before build.

Checks run (Python, scratchpad r17, 2026-11-09): regions' key dates fall within 1879 to 1908 and the slider runs 1870 to 1914; the Congo Free State lasted 23 years (1885 to 1908); every region has voices from at least two sides; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and panel; at 680x425 sheet.
2. Voice cards are tagged with the factors behind each view, checked. (D2.His.4.9-12)
3. Each region's panel links causes to short and long effects. (D2.His.14.9-12)
4. The lasting-effects layer explains a border, an economy and a railway. (D2.Geo.5.9-12)
5. The two-views card compares voices from different sides. (D2.His.4.9-12)
6. The 1870 map shows African states in full before any claim.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: claims appear at once; no network requests.

## Open questions
- Sensitivity flag: genocide, forced labor, colonial violence and racist period sources (default used: told plainly with sourced ranges, no atrocity images, racist language paraphrased never quoted, African states first, fresh-agent read before build).
