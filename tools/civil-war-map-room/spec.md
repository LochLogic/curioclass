# Civil War Map Room

## One idea
On a war-room table lies a map of the United States in 1861 and a stack of dated folders; the child opens each folder in turn and the map animates that campaign (the blockade, Antietam and the Emancipation Proclamation in 1862, Gettysburg and Vicksburg in July 1863, the fall of Atlanta in 1864, Appomattox in 1865), then reads a short real letter from a soldier or civilian on each side, sees a photograph and two facts, and pins the turning point to the causes it shows (Vicksburg: control of the Mississippi; emancipation: about 180,000 Black soldiers joining the Union army); at the end a ranking board of five causes of Union victory (industry and railroads, the blockade, emancipation and Black soldiers, leadership, will to keep fighting) holds the pinned evidence, and the child writes a case for the most important one, then reads a closing card on the war's cost and the end of slavery, so an eighth grader learns to explain the causes and effects of turning points and to weigh the relative influence of several causes.

## Not like
- expansion-map (8, spec): territory over time. Here campaigns over four years.
- voices-of-freedom (8, spec): sources on slavery before the war. Here the war itself.
- reconstruction-amendments (8, spec): after the war. Here how it was won.
- constantinople-defense (7, spec): many causes of a fall. Here many causes of a victory.

## Who and how
- Grade 8, Social Studies (History), module "The Civil War". Standards: D2.His.14.6-8 (explain multiple causes and effects of events and developments in the past), D2.His.15.6-8 (evaluate the relative influence of various causes of events and developments in the past).
- Format: map. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Seven folders, pins, the ranking board, the case, the closing card. Extra: A historian's view (after ranking, the child compares with two historians' rankings and why they differ). tool.json `modes: ["Map room", "A historian's view"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.14.6-8 | Open each folder, read the effects, and pin the turning point to the causes it shows | the animated campaign; the pins with cause tags | 2, 3 |
| D2.His.15.6-8 | Rank five causes on the board with pinned evidence, then write a case for the top one | the ranking board; the case card | 4 |

## Screens and modes
Header (kit): title "Civil War Map Room"; `Map room`, `A historian's view`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A war-room table with the 1861 map: Union states, Confederate states, border states, railroads drawn in thin lines, rivers. A stack of seven dated folders and a tray of five cause tags. The welcome is queued (`welcomeAfter: true`): "In 1861, eleven states had left the Union to protect slavery, and war began. Four years later the Union had won. Why? Open the first folder." First hint: "Tap the top folder."

**Folders (focus: the map and the folder).** At 1366x768 the map fills the center with the folder at the right; at 680x425 the folder is a sheet. Each folder: the campaign animates as arrows and lines (no battle scenes), then a short real letter (a few lines), a photograph, two facts and a "what it led to" line.
1. 1861, the blockade: the Union navy closes Southern ports; cotton exports collapse.
2. September 1862, Antietam: the bloodiest single day in American history (about 23,000 killed, wounded or missing); five days later Lincoln issues the preliminary Emancipation Proclamation.
3. January 1, 1863, the Emancipation Proclamation takes effect: freedom declared in Confederate-held areas; Black men may enlist; about 180,000 serve in the Union army by war's end. Britain and France stay out of the war.
4. July 1863, Gettysburg: Lee's invasion of the North is turned back.
5. July 4, 1863, Vicksburg: the Union controls the Mississippi River, splitting the Confederacy.
6. September 1864, Atlanta falls: Northern spirits rise and Lincoln wins reelection that November.
7. April 1865, Appomattox: Lee surrenders.
- Letters come from both sides and from civilians (Library of Congress and state archives), chosen for plain words, not glory.
- Facts panels include Union advantages (most of the nation's factories and about two-thirds of its railroad miles) and Confederate ones (defending home ground, skilled officers).

**Pins (D2.His.14.6-8).** After each folder the child pins it to one or more cause tags: industry and railroads, the blockade, emancipation and Black soldiers, leadership, will to keep fighting. Each pin needs a because line from tiles.

**The ranking board (the aha, D2.His.15.6-8).** Five causes with their pins. The child ranks them, then writes a case for the top pick: "The most important cause was ___, because ___. It mattered more than ___ because ___." Narrator: "Historians still argue about this ranking. What matters is the evidence you put behind yours."

**The closing card.** About 620,000 to 750,000 soldiers died; the 13th Amendment (1865) ended slavery in the whole country. No images of the dead.

**The end.** The map with all campaigns, the pins, the board and the case. `Print` prints them.

**A historian's view (extra).** Two historians' emphases (one stressing the North's resources, one stressing turning points and choices that could have gone the other way), and the child notes where their ranking agrees.

## Content
- Seven folders with animated campaigns, short real letters, photographs and facts; five cause tags; because tiles; the ranking board; the case card; the closing card; two historians' views.
- All events, letters, figures and photographs are real and sourced; figures are rounded and labeled "about".
- The war's cause (slavery) is stated plainly; no side is glorified; no images of the dead.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Folders open in order; the child can reopen any opened folder.
- Pins can move between causes until the board is ranked.
- Keyboard: Tab to folders, the map's campaign steps, tags and the board; Enter to open, pin and rank; arrows step through a campaign.
- With Motion off campaigns appear as finished arrows without moving.

## Look
- Accent `--brand` #35506b map slate (header, folders, the board); gold #f4c542 (the open folder, a pin); paper #f1f4f7; ink #0c1622; muted #525962.
- Contrast (WCAG 2.1, computed): white on brand 8.36:1; brand on paper 7.58:1; ink on paper 16.49:1; muted on paper 6.42:1; ink on gold 11.19:1.
- Never color alone: Union, Confederate and border states carry labels and patterns (plain, hatched, dotted); arrows carry labels.
- Different from this batch (dusk violet, claret, ballot green, prairie rust).

## Art
- Public domain (Library of Congress, ids checked at build): the 1861 "Scott's Great Snake" map; photographs of Antietam's Dunker Church (no bodies), Vicksburg's river bluffs, Atlanta's rail yards, the McLean House; a photograph of soldiers of the U.S. Colored Troops; the Emancipation Proclamation (National Archives). Each with credit.
- Drawn in code: the base map, campaign arrows, railroads, pins, the board.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the narrator; `clear-teacher` as the reader of letters, introduced each time as "from a letter by". `Curio.voice` with `scope: () => state.mode + ':' + state.folder + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each campaign summary.
- event, whole, each letter.
- how `pin`: "Pin this turning point to the causes it shows."
- how `rank`: "Rank the five causes, top to bottom."
- how `case`: "Write your case for the top cause."
- event, whole, the closing card.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the map with campaign animation, folders, pins, the ranking board, the case card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pins | Pin every folder to every cause | Each pin needs a because line, and the checks reject pins with no link (Gettysburg to the blockade). |
| Ranking | Rank in tray order | The tray shuffles; the case card needs evidence pinned to the top cause. |
| Case | Name a cause with no comparison | Print waits for the "mattered more than" line. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Campaign summary (whole), waits; letter (whole).
2. `pin`, after each folder.
3. `rank`; `case`.
4. Closing card (whole); `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.14.6-8 and D2.His.15.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Antietam the bloodiest single day, about 23,000 casualties; preliminary Emancipation Proclamation five days later | National Park Service, Antietam National Battlefield | National Archives, "The Emancipation Proclamation" | yes |
| About 180,000 Black soldiers served in the Union army | National Archives, "Black Soldiers in the U.S. Military During the Civil War" | National Park Service, "U.S. Colored Troops" | yes |
| Gettysburg (July 1 to 3, 1863) and Vicksburg (July 4, 1863) | National Park Service, Gettysburg and Vicksburg battlefield pages | American Battlefield Trust | yes |
| Atlanta fell September 1864 and helped Lincoln's reelection | Britannica, "Atlanta campaign" | McPherson, "Battle Cry of Freedom" (Oxford, 1988) | yes |
| The North held most of the nation's factories and about two-thirds of its railroad miles | McPherson (1988) | National Park Service, "The North and South compared" | yes |
| About 620,000 to 750,000 soldiers died | Hacker, "A Census-Based Count of the Civil War Dead," Civil War History (2011) | National Park Service, "Civil War casualties" | yes, as a range |
| Secession declarations named slavery as the cause | Avalon Project (Yale Law School), secession declarations | National Park Service, "Secession" | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: war deaths are given as numbers without images of the dead; slavery is named plainly as the cause of secession; letters from both sides are chosen for plain words, and neither side is glorified. A fresh-agent read of the letters is needed before build.

Checks run (Python, scratchpad r16, 2026-11-09): folders in date order (1861, September 1862, January 1863, July 1 to 3 1863, July 4 1863, September 1864, April 1865); every folder pins to at least one cause and every cause has at least one folder; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and folder; at 680x425 sheet.
2. Seven folders animate campaigns and show letters, photos and facts. (D2.His.14.6-8)
3. Pins link turning points to causes with because lines. (D2.His.14.6-8)
4. The board ranks five causes and the case compares two. (D2.His.15.6-8)
5. The closing card states the cost and the end of slavery.
6. A historian's view loads.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: finished arrows only; no network requests.

## Open questions
- Sensitivity flag: war deaths and slavery as the cause of the war (default used: numbers without images of the dead, slavery named plainly, letters from both sides chosen for plain words, fresh-agent read before build).
