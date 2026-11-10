# Remembrance Archive

## One idea
A quiet archive room holds four folders, each a real person, family or place in the Holocaust and the Second World War: the Frank family in Amsterdam, the Kovno ghetto in Lithuania as recorded in Avraham Tory's secret diary and George Kadish's hidden photographs, the French village of Le Chambon-sur-Lignon where people sheltered Jewish children, and the Ohrdruf camp as U.S. soldiers and General Eisenhower found it in April 1945; the student opens a folder and reads its items in time order, and every item has a source card (who made it, when, where, for whom and why) that the student fills before rating how useful the item is for the folder's question (for example "What could ordinary people know, and when?"), with perpetrator documents shown only inside that framing; a context strip with a map and timeline places each item in the wider war and the Holocaust, in which about six million Jews were murdered; at the end the student answers the folder's question with the three items they judged most useful and writes a reflection that stays on the device, so a tenth grader learns how time and place shaped events, the factors behind victims', rescuers', bystanders' and perpetrators' views, and how to judge a source's usefulness for a question. There are no points, timers or game mechanics.

## Not like
- voices-of-freedom (8, spec): the family sibling for U.S. slavery sources. Here the Holocaust.
- missing-voices-archive (11, concept): gaps in an archive of the 1918 flu. Here what the sources say and who made them.
- unlabeled-archive (7, spec): dating unlabeled sources. Here judging labeled sources for a question.
- two-space-races (11, spec): two sides writing one story. Here every kind of witness.

## Who and how
- Grade 10, Social Studies (World History), module "World War II and the Holocaust". Standards: D2.His.1.9-12 (evaluate how historical events and developments were shaped by unique circumstances of time and place as well as broader historical contexts), D2.His.4.9-12 (analyze complex and interacting factors that influenced the perspectives of people during different historical eras), D2.His.11.9-12 (critique the usefulness of historical sources for a specific historical inquiry based on their maker, date, place of origin, intended audience, and purpose).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Four folders of about eight items each, source cards, usefulness ratings, the context strip, the folder answer, the reflection. Extra: Teacher notes (context, discussion guidance, support for students who are affected, and how to handle questions about denial, printable). tool.json `modes: ["Archive", "Teacher notes"]`, `minutes: "40-50"`, `grades_label: "Grade 10"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.11.9-12 | Fill each item's source card (maker, date, place, audience, purpose), then rate its usefulness for the folder's question with a reason | the source card; the usefulness scale with a reason line | 2 |
| D2.His.4.9-12 | Tag each maker's position (victim, rescuer, bystander, perpetrator, liberator) and the factors that shaped the view | the position tag; factor tags | 3 |
| D2.His.1.9-12 | Place each item on the context strip and name what was particular to that town and year | the map and timeline; the "only here, only then" line | 4 |

## Screens and modes
Header (kit): title "Remembrance Archive"; `Archive`, `Teacher notes`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A quiet archive reading room: a long table, a lamp, four folders, each labeled with a person or a place and a question. A note: "This archive holds real documents, photographs and testimony about the Holocaust, the murder of about six million Jews by Nazi Germany and its collaborators, and about the war. Some items are hard to read. There is no score here. Take your time." The welcome is queued (`welcomeAfter: true`): "Every item here was made by someone, for someone, for a reason. Pick a folder." First hint: "Tap a folder."

**Folders (focus: the open item).** At 1366x768 the item fills the center with its source card right; at 680x425 the card is a sheet.
1. The Frank family, Amsterdam. Question: "How did life change for a Jewish family in an occupied country, step by step?" Items: a 1941 family photograph; a 1941 Dutch decree barring Jews from public places (perpetrator document, framed); Anne's diary (1942 to 1944) and her own 1944 revisions after a radio call to keep diaries; Miep Gies's later testimony; a 1944 deportation list from Westerbork; Otto Frank's postwar account. Anne and her sister Margot died at Bergen-Belsen in early 1945.
2. The Kovno ghetto, Lithuania. Question: "What could ordinary people know, and when?" Items: Avraham Tory's diary, kept in secret for the ghetto's council; George Kadish's photographs, taken with a hidden camera; the Jager Report (December 1, 1941), an SS officer's own count of killings in Lithuania (perpetrator document, shown as a short text excerpt inside the framing); a survivor's testimony; a map of the ghetto.
3. Le Chambon-sur-Lignon, France. Question: "Why did some people risk their lives to help?" Items: Pastor Andre Trocme's sermons and letters; a refugee child's later testimony; a forged identity card; Yad Vashem's recognition of the village as Righteous Among the Nations (1990).
4. Ohrdruf, Germany, April 1945. Question: "Why did the people who found the camps insist on recording them?" Items: a U.S. Army Signal Corps photograph of soldiers and townspeople (chosen without visible bodies); Eisenhower's April 15, 1945 letter to General Marshall about seeing the camp so he could testify if anyone later called it propaganda; a soldier's letter home; a newsreel still.
- For each item the student fills the source card from tiles and the item's own clues, then rates usefulness (very, somewhat, a little) for the folder's question with a reason. A historian's note follows each rating.
- Perpetrator documents appear only as framed text with their source card; no Nazi propaganda images or symbols are shown.

**Positions and factors (D2.His.4.9-12).** For each maker the student tags a position (victim, rescuer, bystander, perpetrator, liberator) and factors (fear, faith, ideology and antisemitism, orders, family, what they could know). Notes explain that positions could change.

**The context strip (D2.His.1.9-12).** A map of Europe and a timeline from 1933 to 1945 place each item: the occupation of the Netherlands (1940), the invasion of the Soviet Union and mass shootings (1941), the deportations (1942 to 1944), the liberation of camps (1945). For each folder the student writes one "only here, only then" line.

**The folder answer (the aha).** The student answers the folder's question with the three items they rated most useful and says why each helps. Narrator: "We know what happened because people wrote, photographed and testified, sometimes at great risk. Knowing who made each item tells us what it can show."

**The reflection.** A "why it matters" box; a note on screen says it stays on this device and is not sent anywhere.

**The end.** The source cards, ratings, the strip and the answers. `Print` prints them, and prints the reflection only if the student chooses.

**Teacher notes (extra).** Context, discussion guidance, support for students who are affected, and how to answer questions about denial, printable.

## Content
- Four folders, about 30 items with source cards from USHMM, the Anne Frank House, Yad Vashem, the National Archives and the Eisenhower Library, permission checked item by item; the context strip; tags; the answer and reflection boxes; teacher notes.
- No generated images of victims; no images of bodies; no Nazi propaganda images or symbols; perpetrator documents only as framed short text.
- No points, timers or game mechanics.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Folders open in any order; items within a folder open in time order.
- Ratings are not graded right or wrong; the historian's note follows each.
- Keyboard: Tab to folders, items, source card fields, ratings, tags and the strip; Enter to open and pick.
- With Motion off nothing fades or slides.

## Look
- Accent `--brand` #4d4640 archive gray (header, folders, cards); gold #f4c542 (the open item's frame only); paper #f6f4f1; ink #1a1714; muted #5a5550.
- Contrast (WCAG 2.1, computed): white on brand 9.27:1; brand on paper 8.44:1; ink on paper 16.26:1; muted on paper 6.71:1; ink on gold 10.97:1.
- Never color alone: positions carry words; the strip carries dates and places.
- Different from this batch (night navy, podcast plum, campaign green, orbit indigo). Plain and quiet, with lots of space.

## Art
- Public domain or licensed archival items only, each permission checked at build: USHMM Photo Archives (George Kadish photographs); Anne Frank House (photographs, permission required); National Archives (Signal Corps photographs, Eisenhower's letter); Yad Vashem (recognition documents, permission required). Each with credit.
- No generated images of people. Local FLUX (`scripts/localart.py`): the empty reading room only (1, 16:9).
About 20 items.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator and hints; `wise-mentor` as the reader of testimony and diary excerpts, introduced each time as "from" the writer, never playing them. `Curio.voice` with `scope: () => state.mode + ':' + state.folder + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each item's plain note.
- event, whole, each excerpt.
- how `card`: "Fill the source card: who made it, when, where, for whom and why."
- how `rate`: "Rate how useful this item is for the folder's question, and why."
- how `strip`: "Place this item on the map and timeline."
- how `answer`: "Answer the folder's question with your three most useful items."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
primary-sources (no engine or family doc on main yet). This tool keeps its item data (id, folder, maker, date, place, audience, purpose, kind, excerpt, plain note, permission and credit, position, linked strip event) as plain data in one marked block, `/* PRIMARY-SOURCES DATA: begin */ ... /* end */`, the same shape as voices-of-freedom, so a family engine can take both later. Tool-only code: the reading room, folders, source cards, ratings, the context strip, the answer and reflection.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Source card | Guess every field | Each field checks against the item's record, with a pointer to the clue. |
| Rating | Rate everything "very useful" | Each rating needs a reason line that names the question. |
| Answer | Pick any three items | The answer needs a "why it helps" line for each item. |
This tool has no score; the checks keep the work honest without making it a game.

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Plain note (whole), waits; excerpt (whole).
2. `card`; `rate`.
3. `strip`.
4. `answer`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.9-12, D2.His.4.9-12 and D2.His.11.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| About six million Jews murdered | United States Holocaust Memorial Museum, Holocaust Encyclopedia | Yad Vashem, "The Holocaust" | yes |
| The Frank family, the diary, Westerbork, deaths at Bergen-Belsen in early 1945 | Anne Frank House | USHMM, "Anne Frank" | yes |
| Avraham Tory's Kovno diary and George Kadish's photographs | Tory, "Surviving the Holocaust: The Kovno Ghetto Diary" (Harvard, 1990) | USHMM, "Kovno" and Kadish collection | yes |
| The Jager Report (December 1, 1941) | USHMM, Holocaust Encyclopedia, "Einsatzgruppen" | Yad Vashem, document archive | yes |
| Le Chambon-sur-Lignon recognized as Righteous Among the Nations (1990) | Yad Vashem, Righteous Among the Nations | USHMM, "Le Chambon-sur-Lignon" | yes |
| Ohrdruf liberated in April 1945; Eisenhower's April 15 letter to Marshall | Dwight D. Eisenhower Presidential Library | USHMM, "Ohrdruf" | yes |
| The context: occupation (1940), shootings (1941), deportations (1942-44), liberation (1945) | USHMM, Holocaust Encyclopedia timeline | Yad Vashem, timeline | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: genocide is the subject; items are archival with permissions checked one by one; no generated images of victims, no images of bodies, no Nazi images or symbols; perpetrator documents appear only as framed short text; the reflection stays on the device; teacher notes include support guidance. A fresh-agent read of every item is needed before build.

Checks run (Python, scratchpad r19, 2026-11-09): four folders, each with items in date order; the strip runs 1933 to 1945; every folder has at least two maker positions; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 item and source card; at 680x425 sheet.
2. Every item's source card is filled and its usefulness rated with a reason. (D2.His.11.9-12)
3. Makers are tagged by position and factors. (D2.His.4.9-12)
4. Each item sits on the context strip with an "only here, only then" line per folder. (D2.His.1.9-12)
5. The folder answer uses three items with reasons; the reflection stays on the device.
6. No score, timer, game mechanic, generated victim image or Nazi image appears.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: nothing fades or slides; no network requests.

## Open questions
- Sensitivity flag: the Holocaust told through real documents, testimony and perpetrator records (default used: archival items with permissions checked one by one, no generated victim images, no bodies, no Nazi images, perpetrator documents only as framed text, teacher notes with support guidance, fresh-agent read before build).
