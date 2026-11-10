# Missing Voices Archive

## One idea
The student opens Philadelphia's archive on the 1918 flu, a drawer of twenty official items (the mayor's and health director's notices, the main daily newspaper, the closing order of October 3, 1918, the count of the dead) and tags whose words each item holds; on a city map the neighborhoods light up where voices exist and stay dark where they don't, and a "story so far" panel writes the history these sources alone would tell (a parade, a closing order, brave officials, an epidemic that passed); then the student writes supporting questions about the dark places ("What did nurses see?" "What did the Black press report?" "How did Italian families in South Philadelphia hear the news?"), and each good question opens a second drawer of real sources that exist but are rarely used (visiting nurses' reports, the Philadelphia Tribune, a foreign-language paper, a family letter, death records by ward), so the story panel rewrites itself, and the student notes what changed, what new questions came up, and which gaps no source can fill, so an eleventh grader learns how the sources that survive limit the history we can tell, and how questions about sources lead to more sources and new questions.

## Not like
- remembrance-archive (10, spec): the Holocaust in documents. Here the gaps in one city's archive.
- behind-the-podcast (11, spec): checking a finished work. Here building a fuller story.
- decades-explorer (11, spec): then and now memory. Here who left records at all.
- unlabeled-archive (7, spec): sorting unlabeled items. Here finding who is missing.

## Who and how
- Grade 11, Social Studies (U.S. History), module "Missing Voices Archive". Standards: D2.His.8.9-12 (analyze how current interpretations of the past are limited by the extent to which available historical sources represent perspectives of people at the time), D2.His.12.9-12 (use questions generated about multiple historical sources to pursue further inquiry and investigate additional sources), D1.4.9-12 (explain how supporting questions contribute to an inquiry and how, through engaging source work, new compelling and supporting questions emerge).
- Format: explorer. Driver: one student alone, or groups taking different neighborhoods (tool.json `driver: "either"`). `Read` reads every item. Controls 44 px or more.
- Twenty official items, about fifteen hidden items behind five question themes, the voice map, the story panel, the final note. Extra: Neighborhoods (groups each take a part of the city and pool their finds). tool.json `modes: ["Archive", "Neighborhoods"]`, `minutes: "35-45"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.8.9-12 | Tag each item's speakers and read the story the official drawer alone tells | the voice counter; the dark map; the story so far | 2 |
| D2.His.12.9-12 | Write questions about the first sources that unlock the second drawer | the question box; the second drawer opening by theme | 3 |
| D1.4.9-12 | Note how each question moved the inquiry and which new questions the new sources raised | the inquiry trail; the final note | 4 |

## Screens and modes
Header (kit): title "Missing Voices Archive"; `Archive`, `Neighborhoods`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** An archive reading room. A wooden drawer marked "Philadelphia, Influenza, 1918" holds twenty items. A 1918 ward map of the city sits beside it, all gray. A counter reads "Voices: officials 0, editors 0, nurses 0, families 0". The welcome is queued (`welcomeAfter: true`): "This is what the city kept. Read it, and notice who is doing the talking. Tap the first item." First hint: "Tap the first item in the drawer."

**The official drawer (focus: the item and the map).** At 1366x768 the drawer and item fill the left with the map and counter right; at 680x425 the map is a sheet. The twenty items are real and dated: the Liberty Loan parade of September 28, 1918, with about 200,000 people in the streets; health director Wilmer Krusen's notices; the order of October 3 closing schools, churches, theaters and saloons; daily death counts, with more than 4,500 deaths in the week ending October 16; the main paper's reassurances and appeals for nurses; the reopening at the end of October. For each item the student tags the speaker (official, editor, doctor, nurse, family, clergy, worker) and the neighborhood. The map lights wards where a voice speaks; most stays dark. The story panel writes: "The city's leaders acted, the people obeyed, and the epidemic passed."

**Questions (D2.His.12.9-12, D1.4.9-12).** A question box: the student writes a question about the dark places and picks the item that raised it. A question that names a group or place and asks what, how or why opens the matching theme in the second drawer:
1. Nurses: Visiting Nurse Society reports of homes with whole families sick and no one to cook.
2. The Black press: the Philadelphia Tribune on Black nurses turned away at first and on care in Black neighborhoods.
3. Immigrant families: a foreign-language paper's notices (Italian or Yiddish, translated, original shown) and the crowded wards of South Philadelphia.
4. Families: a letter or diary from a household (from a historical society collection, permissions checked).
5. The dead: death records by ward, showing where the toll fell heaviest.
- After each opening, the inquiry trail asks: "What new question does this raise?"

**The rewritten story (the aha).** The story panel rewrites itself with each new source: the toll fell unevenly; nurses and neighbors did much of the caring; some voices are still missing (children, the very poor, people who left no writing). The final note: "The first drawer told ___. The new sources changed it by ___. A gap no source can fill is ___, because ___." Narrator: "An archive is not the past. It is what someone decided to keep."

**The end.** The tagged items, the lit map, the inquiry trail and the note. `Print` prints them.

**Neighborhoods (extra).** Groups each take wards, open their themes and pool their finds on one map.

## Content
- Twenty official items and about fifteen second-drawer items, all real, dated and credited, with short excerpts; the 1918 ward map; the story panel's four versions; the inquiry trail; the note template.
- Philadelphia is the city; every item is checked for survival and permissions before build.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A theme opens only from a question that names a group or place and asks what, how or why; a plain yes or no question gets a hint to reword.
- Keyboard: Tab to items, tags, the map, the question box and the second drawer; Enter to tag and open.
- With Motion off wards light without fading.

## Look
- Accent `--brand` #2f5d62 archive teal (header, the drawer, tags); gold #f4c542 (the item open, a lit ward); paper #eff5f5; ink #0a1d20; muted #4f5a5b.
- Contrast (WCAG 2.1, computed): white on brand 7.34:1; brand on paper 6.65:1; ink on paper 15.75:1; muted on paper 6.47:1; ink on gold 10.68:1.
- Never color alone: lit wards carry a count and a pattern; tags carry words.
- Different from this batch (gilded bronze, decade violet, suburb green, press red).

## Art
- Public domain (Library of Congress Chronicling America for the Evening Public Ledger, National Archives, the Philadelphia City Archives, ids checked at build): newspaper pages of 1918; the parade; an emergency hospital; Red Cross nurses. Each with credit.
- The 1918 ward map redrawn in code from a city atlas.
- Local FLUX (`scripts/localart.py`): the archive reading room (1, 16:9).
About 8 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the archivist narrator and hints; `gentle-storyteller` as the reader of the items, introduced each time as "from" the source. `Curio.voice` with `scope: () => state.mode + ':' + state.drawer + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each item.
- how `tag`: "Tag who is speaking and where."
- event, whole, each story panel version.
- how `ask`: "Write a question about a dark place on the map."
- how `trail`: "What new question does this raise?"
- how `note`: "Write what changed and what is still missing."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the drawers, tags, the voice map, the question gate, the story panel, the trail. Items live in a marked data block `/* PRIMARY-SOURCES DATA: begin */ ... /* end */` in the same shape as voices-of-freedom and remembrance-archive.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag everyone "official" | Each tag checks against the item's author. |
| Questions | Type a group name only | The gate needs what, how or why plus a group or place. |
| Note | Say "more sources" | It needs one change and one gap with a reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Item (whole), waits; `tag`.
2. Story panel (whole); `ask`.
3. Second-drawer item (whole); `trail`.
4. `note`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.8.9-12, D2.His.12.9-12 and D1.4.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Liberty Loan parade (September 28, 1918), about 200,000 people | University of Michigan Center for the History of Medicine, Influenza Encyclopedia, "Philadelphia" | College of Physicians of Philadelphia, History of Vaccines, "Philadelphia 1918" | yes |
| The closing order of October 3, 1918; Wilmer Krusen as health director | Influenza Encyclopedia, "Philadelphia" | Barry, "The Great Influenza" (Viking, 2004) | yes |
| More than 4,500 deaths in the week ending October 16 | Influenza Encyclopedia, "Philadelphia" | Barry (2004) | yes |
| Visiting Nurse Society work in 1918 | Barbara Bates Center for the Study of the History of Nursing, University of Pennsylvania | Influenza Encyclopedia, "Philadelphia" | yes |
| Black nurses at first turned away; care in Black neighborhoods | Gamble, "There Wasn't a Lot of Comforts in Those Days," Public Health Reports (2010) | Philadelphia Tribune, October 1918 (microfilm, checked at build) | yes |
| The toll fell unevenly by ward and group | Influenza Encyclopedia, "Philadelphia" | Gamble (2010) | yes |
| The Evening Public Ledger 1918 issues are public domain and digitized | Library of Congress, Chronicling America | U.S. Copyright Office, Circular 15A on terms | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r20, 2026-11-09): the closing order came 5 days after the parade; twenty official items and five themes of three items each; every theme maps to at least one dark ward; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 drawer and map; at 680x425 sheet.
2. All twenty items are tagged and the official story is shown. (D2.His.8.9-12)
3. Questions open themes in the second drawer. (D2.His.12.9-12)
4. The inquiry trail records new questions, and the note names a change and a gap. (D1.4.9-12)
5. Every item shows its source and date.
6. Translated items show the original beside the translation.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fading; no network requests.

## Open questions
- The idea card flags a data source (default used: Philadelphia, with each second-drawer item checked for survival and permissions before build; if a theme can't be filled with real items, the theme is cut rather than invented).
