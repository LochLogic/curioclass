# Home Front Mobilizer

## One idea
The student runs Los Angeles's war effort from December 1941 to 1945 a quarter at a time (retool an aircraft plant, staff a shipyard, keep a cannery going, set ration rules, run bond drives) while production and morale meters respond and official sources (posters, newsreel stills, government photographs) praise each quarter; but the official record is only part of the city: in February 1942 the Japanese American fishing village on Terminal Island is given 48 hours to leave, and then Little Tokyo empties under Executive Order 9066, which the student cannot stop, speed or use, and one family's story follows them to Manzanar in their own words; Black workers are shut out of plant jobs until protest and an executive order open them, Mexican American young men are attacked in the 1943 riots, braceros arrive to work the fields, and women who built the planes are laid off when the war ends; a record drawer sets official sources beside suppressed or overlooked ones (Dorothea Lange's photographs impounded by the Army, workers' letters, oral histories) and the student marks what each kind of evidence can and can't show; at the end the student writes how a worker, a plant owner, a Japanese American family and a government photographer each saw the same years, so an eleventh grader learns how interacting factors shaped people's perspectives and how to detect the limits of different kinds of historical evidence.

## Not like
- factory-floor (9, spec): a 19th-century mill. Here a wartime city.
- remembrance-archive (10, spec): Holocaust records. Here an American city's official and hidden record.
- suburb-boom (11, spec): postwar growth. Here the war years.
- movement-strategy-room (11, spec): organizers' choices. Here the record's blind spots.

## Who and how
- Grade 11, Social Studies (U.S. History), module "World War II and the Home Front". Standards: D2.His.4.9-12 (analyze complex and interacting factors that influenced the perspectives of people during different historical eras), D2.His.10.9-12 (detect possible limitations in various kinds of historical evidence and differing secondary interpretations).
- Format: tycoon. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Sixteen quarters, three plants, two meters, about twenty-four record items, four perspectives, the write-up. The incarceration is told through evidence and is never a lever. Extra: Record only (the record drawer and perspectives without the management layer, for a shorter lesson). tool.json `modes: ["City at war", "Record only"]`, `minutes: "40-50"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.10.9-12 | In the record drawer, mark what each source can and can't show and pair official with overlooked sources | the drawer with paired items; the can and can't tags | 2 |
| D2.His.4.9-12 | Fill the four perspectives with the factors that shaped each (race, class, wartime fear, patriotism, pay) | the four perspective cards; the factor tiles | 3 |
| D2.His.4.9-12 and D2.His.10.9-12 | Write the closing comparison and name what the official record would hide | the write-up | 4 |

## Screens and modes
Header (kit): title "Home Front Mobilizer"; `City at war`, `Record only`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A drawn map of Los Angeles in December 1941: an aircraft plant, a shipyard at the harbor, a cannery on Terminal Island, downtown and Little Tokyo's First Street. A radio on the desk. The welcome is queued (`welcomeAfter: true`): "The country is at war. This city has to build planes and ships fast. You'll run it, and you'll also see what the official story left out. Tap the aircraft plant." First hint: "Tap the aircraft plant."

**Quarters (focus: the city).** At 1366x768 the map fills the left with the quarter card and meters right; at 680x425 the card is a sheet. Each quarter the student sets three choices (retool or hire, a ration rule, a bond drive) and the meters move by stated rules. An official source reports the quarter (a poster, a newsreel still, a government photograph).
- December 1941 to mid-1942: retooling; ration books; the first bond drives.
- Black workers: plants refuse to hire them for skilled jobs despite Executive Order 8802 (June 1941), until protest and the Fair Employment Practice Committee's Los Angeles hearings (October 1941) and continued pressure open some jobs.
- Women: by 1944 about 6 million more women are working nationwide; in late 1945 many are laid off as plants cut back and men return.
- Braceros: the Bracero Program (August 1942) brings Mexican farmworkers.
- June 1943: servicemen attack young Mexican American and Black men in the "Zoot Suit Riots".
- Little Tokyo empties; by 1943 Black families arriving for war jobs live there, and it is called Bronzeville.

**Executive Order 9066 (never a lever).** February 19, 1942: the order is signed. On February 25, Terminal Island's Japanese American residents are given 48 hours to leave; by spring Little Tokyo's families are sent to assembly centers and then camps such as Manzanar. The quarter card shows it as an event; no meter rises from it, no choice touches it. One family's story follows them through the camp years in their own words from published oral histories (Densho, permissions checked). About 120,000 people of Japanese ancestry on the West Coast were incarcerated, about two-thirds of them U.S. citizens.

**The record drawer (D2.His.10.9-12).** Official items paired with overlooked or suppressed ones: a war bond poster with a worker's letter about the plant's color line; an Army newsreel still with Dorothea Lange's 1942 photographs of the removal, impounded by the Army and not widely seen until decades later; a government photograph of Manzanar beside Ansel Adams's 1943 Manzanar photographs and a family's oral history; a celebrated "Rosie" poster beside a 1945 layoff notice. For each item the student tags what it can show and what it can't (who made it, for whom, what was cut out).

**Four perspectives (D2.His.4.9-12).** A worker, a plant owner, a Japanese American family, a government photographer. The student fills each with factor tiles (race, class, wartime fear, patriotism, pay, the law) and one piece of evidence.

**The write-up (the aha).** "The official record shows ___. It hides ___. The family saw these years as ___; the plant owner saw them as ___, because ___." Narrator: "Both records are true. Only one of them was meant to be seen." Then the epilogue: Korematsu v. United States (1944), the Commission on Wartime Relocation (1983) and the Civil Liberties Act of 1988, with a formal apology and $20,000 to each living survivor.

**The end.** The city, the drawer tags, the four perspectives and the write-up. `Print` prints them.

**Record only (extra).** The drawer and perspectives without the quarter layer.

## Content
- Sixteen quarter cards with stated meter rules, about twenty-four real record items (credited, excerpts under 15 words), one family's published oral history with permission, four perspectives with factor tiles, the write-up and epilogue.
- The incarceration is never a game lever: no meter, choice, score or speed is tied to it.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each quarter waits for three choices; event cards (9066, the riots, the layoffs) play whole and can't be skipped or changed.
- The record drawer opens after February 1942 and stays open.
- Keyboard: Tab to the map, choices, meters, the drawer and the perspectives; Enter to choose and tag.
- With Motion off meters jump to their values and the map changes without fading.

## Look
- Accent `--brand` #4a5320 olive drab (header, the quarter card, meters); gold #f4c542 (the choice in hand, a tagged item); paper #f5f6ee; ink #171a08; muted #56594b.
- Contrast (WCAG 2.1, computed): white on brand 8.24:1; brand on paper 7.57:1; ink on paper 16.25:1; muted on paper 6.60:1; ink on gold 10.87:1.
- Never color alone: meters carry numbers; tags carry words; official and overlooked items carry labels.
- Different from this batch (Senate rust, brain magenta, web teal, civic blue).

## Art
- Public domain photographs (National Archives War Relocation Authority records for Lange; Library of Congress for Adams's Manzanar; Office of War Information posters; ids checked at build). Each with credit.
- Densho photographs only with permission, checked at build.
- Local FLUX (`scripts/localart.py`): the 1941 city scene from above (1, 16:9) and an empty plant floor (1, 16:9).
- No generated images of incarcerated people; only real photographs.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the city narrator and hints; `gentle-storyteller` as the reader of the family's words and the record items, introduced each time as "from" the source. `Curio.voice` with `scope: () => state.mode + ':' + state.quarter + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `quarter`: "Make three choices for this quarter."
- event, whole, each official report.
- event, whole, each event card.
- event, whole, each family passage.
- how `tag`: "Tag what this source can and can't show."
- how `perspective`: "Fill this perspective with what shaped it."
- how `write`: "Write what the official record hides."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the quarter stepper with stated rules, the meters, event cards, the record drawer, perspectives, the write-up.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Drawer tags | Tag every item "propaganda" | Each tag checks against the item's maker and purpose; personal sources have limits too. |
| Perspectives | Put the same factors on all four | Each card needs one factor and one piece of evidence that fits that person. |
| Write-up | Repeat the official record | It needs one hidden thing from the drawer. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `quarter`; official report (whole).
2. Event cards (whole), waits; family passage (whole).
3. `tag`; `perspective`.
4. `write`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.4.9-12 and D2.His.10.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Executive Order 9066 (February 19, 1942); about 120,000 incarcerated, about two-thirds citizens | National Archives, "Executive Order 9066" | National Park Service, Manzanar National Historic Site | yes |
| Terminal Island residents given 48 hours (February 1942) | Densho Encyclopedia, "Terminal Island" | National Park Service, "Terminal Island" | yes |
| Lange's 1942 photographs impounded by the Army | Gordon and Okihiro, "Impounded" (Norton, 2006) | National Archives, War Relocation Authority photographs | yes |
| Adams's Manzanar photographs (1943) | Library of Congress, "Suffering Under a Great Injustice" | National Park Service, Manzanar | yes |
| Executive Order 8802 (June 25, 1941) and the FEPC Los Angeles hearings | National Archives, "Executive Order 8802" | Flamming, "Bound for Freedom: Black Los Angeles in Jim Crow America" (California, 2005) | yes |
| The Bracero Program (1942) and the June 1943 riots | Bracero History Archive (Smithsonian and partners) | Los Angeles Public Library, "Zoot Suit Riots" | yes |
| Little Tokyo became Bronzeville | Japanese American National Museum | Los Angeles Conservancy | yes |
| Women's wartime work and 1945 layoffs | U.S. Department of Labor, Women's Bureau (1946) | National WWII Museum, "Women in the War" | yes |
| Korematsu (1944); the Civil Liberties Act of 1988, apology and $20,000 per survivor | Korematsu v. United States, 323 U.S. 214 (1944) | National Archives, Civil Liberties Act of 1988 | yes |
Backed twice: 10. Cut: 0.

Sensitivity note: the incarceration of Japanese Americans is told through evidence and the family's own words, never as a game lever; no generated images of incarcerated people; the riots are named without images of beatings. A fresh-agent read is needed before build.

Checks run (Python, scratchpad r21, 2026-11-09): sixteen quarters from 1942 to 1945; Terminal Island's notice came 6 days after the order; the 1988 act came 46 years after the order; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and quarter card; at 680x425 sheet.
2. Paired record items are tagged for what each can and can't show. (D2.His.10.9-12)
3. Four perspectives each have factors and evidence. (D2.His.4.9-12)
4. The write-up names something the official record hides. (D2.His.4.9-12, D2.His.10.9-12)
5. No meter, choice or score is tied to the incarceration.
6. No generated images of incarcerated people.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: meters jump; no network requests.

## Open questions
- Sensitivity flag: Japanese American incarceration, racial exclusion and the 1943 riots (default used: told only through evidence and the family's own words, never a lever, real photographs only, no images of beatings, fresh-agent read before build).
- The idea card names "one West Coast city" (default used: Los Angeles, for Terminal Island, Little Tokyo and Bronzeville in one place).
