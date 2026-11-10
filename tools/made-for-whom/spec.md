# Made for Whom?

## One idea
Four real sources from the same years of settlement in Nebraska open one at a time from folders on a desk (an 1872 railroad poster selling land, a settler's letter home, a town newspaper's editorial, and the words of Standing Bear of the Ponca Nation in 1879), and for each the child reads clues inside it to infer who it was made for and why, uses a highlighter to mark what the maker's view put in and a map to see what it left out (the poster shows land for sale but not the nations who lived there), then ranks the four for a given question and finds that the same source can be the most useful for one question and the least useful for another, so a fourth grader learns to ask who made a source, for whom, and why before trusting it.

## Not like
- inquiry-ladder (4, spec, this batch): building questions from sources. Here judging each source's maker, audience and purpose.
- then-and-now-overlay (3, spec): what each kind of source shows about one street. Here how a maker's view shapes a source.
- history-article-review (5, concept): judging secondary articles. Here primary sources at grade 4.
- capsule-from-1965 (1, spec): reading objects for clues. Here reading words and pictures for audience and purpose.

## Who and how
- Grade 4, Social Studies (History), module "Made for Whom?". Standards: D2.His.6.3-5 (describe how people's perspectives shaped the historical sources they created), D2.His.11.3-5 (infer the intended audience and purpose of a historical source from information within the source itself), D2.His.13.3-5 (use information about a historical source, including the maker, date, place of origin, intended audience, and purpose to judge the extent to which the source is useful for studying a particular topic).
- Change from the idea card: the Native perspective is the fourth core source, not an extra, as the card's flag suggests, so the settlement story is never told only by settlers.
- Driver: one child alone, or the teacher on the projector (tool.json `driver: "either"`). `Read` reads every source. Controls 44 px or more.
- Three parts: Open the folders, Highlight and check, Rank. tool.json `modes: ["Folders", "Rank"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.11.3-5 | For each source, tap three clues inside it, then pick its audience (people back East thinking of moving, a family member, the town's readers, a judge and the public) and purpose (sell, share news and feelings, persuade, defend rights) | the source with clue marks and the audience and purpose cards | 2 |
| D2.His.6.3-5 | Highlight words that show the maker's view, then open the map layer to see what the poster left out | highlighted words; the map of the nations whose homelands the land was | 3 |
| D2.His.13.3-5 | For three questions, rank the four sources from most to least useful and pick a reason (maker, date, place, audience, purpose) | the ranking strip under each question, the reason tags | 4, 5 |

## Screens and modes
Header (kit): title "Made for Whom?"; `Folders`, `Rank`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A wooden desk with four closed folders labeled 1 to 4, a magnifier and a highlighter. The welcome is queued (`welcomeAfter: true`): "These four sources are from Nebraska in the 1870s. Each was made by someone, for someone, for a reason. Open the first folder." First hint: "Tap folder 1."

**Folders (focus: the open source).** At 1366x768 the source fills the center with tools on the right; at 680x425 tools sit in a bottom bar. Each source shows maker, date and place in a tag (tap to read), the image, and a plain-words transcription.
1. The poster (Library of Congress, Printed Ephemera Collection, 1872): the Burlington and Missouri River Railroad's "Iowa and Nebraska lands" poster offering land on ten years' credit. Clues: big prices and easy terms, "Millions of acres", where to write to buy. Audience: people back East and in Europe thinking of moving. Purpose: to sell railroad land.
2. The letter (Library of Congress, Prairie Settlement: Nebraska Photographs and Family Letters, 1862-1912; Nebraska State Historical Society): a letter by a homesteading family member in Fillmore County, 1870s, to family back home, about the sod house, the cold, crops and missing home (the build picks one letter and transcribes a short passage). Clues: "Dear", private worries, family news. Audience: family. Purpose: share news and feelings.
3. The editorial (Chronicling America, a Nebraska town paper, 1870s, picked at build): an editorial urging more settlers to come and praising the town's future. Clues: "our town", "every newcomer", strong opinions. Audience: the town's readers and people who might move there. Purpose: persuade.
4. Standing Bear's words (1879): in court in Omaha, Standing Bear of the Ponca Nation, whose people had been forced from their homeland on the Niobrara River, spoke for his right to be treated as a person under the law; reporters printed his words, and the judge ruled that a Native man is a person under U.S. law. The transcription gives a short passage, including "I am a man. The same God made us both." Clues: "I", "my people", "our land". Audience: the judge and the public. Purpose: defend his people's rights.
- Picking audience and purpose: three choices each. A wrong pick: "Look at your clues again. Who would read this?"

**Highlight and check.** In each source the child highlights words that show what the maker wanted readers to think. Then `Check the map` opens a map layer of 1870s Nebraska with the homelands of the Pawnee, Omaha, Ponca, Otoe-Missouria and Lakota nations. On the poster: "The poster shows land for sale. It doesn't show that this was the homeland of nations who lived here. Why might the railroad leave that out?" (three reasons; any is accepted, then the narrator: "The railroad wanted to sell land. A poster that showed whose homeland it was would have sold less.")

**Rank (focus: one question and four cards).** Three questions, one at a time:
- "What was a family's first winter on the prairie like?" (Most useful: the letter, made by someone who lived it, for family, with no reason to sell.)
- "Why did people move to Nebraska?" (Most useful: the poster and the editorial, which show what people were promised; the letter shows why one family came.)
- "What happened to the nations who already lived there?" (Most useful: Standing Bear's words; least: the poster, which leaves them out.)
- The child drags the four cards into order and taps a reason tag for the top card. The tool accepts orders where the most useful card is right and the least useful is not the most useful one. Narrator after the third: "The poster was the most useful source for one question and the least useful for another. A source's usefulness depends on your question."
- `Print` prints the four sources' cards (maker, date, place, audience, purpose) and the three rankings.

## Content
- Four sources with tags, transcriptions, three clues each, audience and purpose choices; a map layer of nations' homelands in the 1870s; three questions with acceptable rankings.
- Transcriptions keep the original words in short passages, with hard words explained in a tap.

## Build notes
- The build confirms each item's catalog link and public-domain status: the 1872 poster (Library of Congress Printed Ephemera Collection, Portfolio 134, Folder 13), one Oblinger family letter from the Prairie Settlement collection, one Nebraska editorial from Chronicling America (1870s), and a contemporary printed account of Standing Bear's 1879 words (newspaper or Thomas Tibbles's account).
- The homelands map is drawn from the Nebraska State Historical Society's and the National Museum of the American Indian's published maps, checked against each nation's own published history where available.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A folder opens only after the one before is done. `Check the map` shows only after highlighting. The Rank part opens after all four folders.
- Keyboard: Tab to clues and words, Enter to mark; arrow keys move a card in the ranking.
- With Motion off folders open without sliding.

## Look
- Accent `--brand` #3d4a5c archive slate (header, folder tabs, tags); gold #f4c542 (the highlighter, the top rank, a clue mark); paper #f3f4f7; ink #11161e; muted #575c66.
- Contrast (WCAG 2.1, computed): white on brand 9.00:1; brand on paper 8.19:1; ink on paper 16.50:1; muted on paper 6.10:1; ink on gold 11.16:1.
- Never color alone: highlighted words are also underlined; ranks carry numbers.
- Different from this batch (inquiry rust, learn-and-earn teal, economy map blue, bill maroon).

## Art
- Public domain (credited): the poster, the letter page, the newspaper page, a printed page of Standing Bear's account (4 images). A photograph of Standing Bear is used only if its public-domain status and the Ponca Tribe of Nebraska's published use are confirmed at build; otherwise none.
- Local FLUX (`scripts/localart.py`): the desk with folders (1, 16:9).
- Drawn in code: the map layer, tags, clue marks, the highlighter, cards and the ranking strip.
About 5 images. No people art made for this tool.

## Voice
Four bank voices, each unique in this batch: `wise-mentor` as the narrator, who also reads Standing Bear's words as a quotation ("Standing Bear said: ..."); `lively-host` reads the poster; `gentle-storyteller` reads the letter; `news-reader` reads the editorial. `Curio.voice` with `scope: () => state.mode + ':' + state.folder + ':' + state.part`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each source's transcription.
- how `clues`: "Tap three clues that show who this was made for."
- how `audience`: "Who was it made for? Why? Tap one of each."
- how `highlight`: "Highlight words that show what the maker wanted you to think."
- how `map`: "Tap Check the map."
- event, whole, `left-out` and its follow-up.
- how `rank`: "Drag the sources in order, most useful first."
- event, whole, `depends`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the folder sequence, clue taps, the highlighter, the map layer, and the ranking with accepted orders.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Audience and purpose | Pick the first choice | Choice order shuffles; a wrong pick sends the child back to the clues. |
| Highlighter | Highlight everything | Highlighting more than half a passage says "Pick just the words that try to make you think something." |
| Rank | Use the same order for all three | The poster is most useful for one question and least for another, so one order can't pass all three. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Each folder: transcription (whole), waits; `clues`; `audience`.
2. `highlight`; `map`; `left-out` (whole).
3. Rank: `rank` per question; after the third: `depends` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.6, 11 and 13 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The 1872 Burlington and Missouri River Railroad poster offered Iowa and Nebraska land on ten years' credit and is in the Library of Congress | Wikimedia Commons file record, "Iowa and Nebraska lands" (Library of Congress Printed Ephemera Collection, Portfolio 134, Folder 13), found 2026-11-09 | Loughborough University poster archive record, "Iowa and Nebraska Lands Poster" | yes |
| The Library of Congress holds Nebraska homesteaders' family letters in "Prairie Settlement: Nebraska Photographs and Family Letters, 1862-1912" | Library of Congress collection page | Nebraska State Historical Society, Oblinger family papers | partly (build confirms the item) |
| In 1879 Standing Bear won a ruling in Omaha that a Native American is a person under U.S. law, after the Ponca were forced from their Niobrara homeland | National Park Service, "Standing Bear" (Homestead National Historical Park) | Nebraska State Historical Society (History Nebraska), "Standing Bear" | yes |
| Pawnee, Omaha, Ponca, Otoe-Missouria and Lakota homelands covered what became Nebraska | History Nebraska, "Native Americans in Nebraska" | National Museum of the American Indian, Native Knowledge 360 | yes |
| Railroads received land grants and sold land to settlers with advertising posters | Library of Congress, "Railroads and the settlement of the West" classroom materials | National Archives, "Pacific Railway Act" | yes |
Backed twice: 5. Cut: 0. The letter item rests on one collection record found in search; the build confirms it before use.

Sensitivity note: settler sources often erased the people who lived on the land. Here the erasure is named plainly, the map shows the nations' homelands, and a Native source is a core source that speaks for itself. A fresh-agent read of the transcriptions, map and narrator lines is needed before build.

Checks run (Python, scratchpad r7, 2026-11-09): each source has exactly one right audience and purpose among three; across the three questions the poster ranks first or second for one and last for another; no single order passes all three; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 source and tools fit; at 680x425 tools are a bottom bar.
2. Each source's audience and purpose take only the right picks. (D2.His.11.3-5)
3. Highlights and the map layer show what the poster left out. (D2.His.6.3-5)
4. Each question accepts only rankings with the right top card and a reason tag. (D2.His.13.3-5)
5. The narrator's "depends" line plays after the third question. (D2.His.13.3-5)
6. Every source shows its maker, date, place and credit.
7. `Check the map` and the Rank part are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no sliding folders; no network requests.

## Open questions
- Sensitivity flag: Standing Bear's words are a core source and the narrator reads them as a quotation (default used: no photograph unless its status is confirmed; the Ponca Tribe of Nebraska's own published history is checked before build; fresh-agent read of all lines).
