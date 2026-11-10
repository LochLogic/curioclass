# Inquiry Ladder

## One idea
A big question about the past, "Was the railroad good for our town?", hangs on a sign at the top of a ladder leaning on a water tower; the child first marks the words in it that people might not agree on ("good" for whom? does "our town" include the farmers outside it?), then opens real 1870s sources from one railroad town (a depot picture, a train timetable, a farmer's letter to the newspaper, a store owner's ad, a Grange poster) and builds a supporting question from each, which only holds as a rung if it helps answer the big question, joins two sources into one question, and reaches the top to see that the answer depends on who "good" is for, so a fourth grader learns how a big question is built from smaller ones and how sources feed them.

## Not like
- wonder-kite (1, spec): asking and sorting questions without sources at grade 1. Here building supporting questions from real sources.
- made-for-whom (4, spec, this batch): who a source was made for and how useful it is. Here which questions sources help answer.
- then-and-now-overlay (3, spec): what each kind of source tells about one street. Here questions about one change in a town.
- source-scout (concept): finding sources. Here using them to build questions.

## Who and how
- Grade 4, Social Studies (Inquiry and History), module "Inquiry Ladder". Standards: D1.2.3-5 (identify disciplinary ideas associated with a compelling question that are open to different interpretations), D1.3.3-5 (identify the disciplinary concepts and ideas associated with a supporting question that are open to different interpretations), D1.4.3-5 (explain how supporting questions help answer compelling questions in an inquiry), D2.His.12.3-5 (generate questions about multiple historical sources and their relationships to particular historical events and developments).
- Driver: one child alone (tool.json `driver: "student"`); `Read` reads every source and line. Controls 44 px or more.
- Four parts: Mark the words, Build rungs, Join two, The top. Extra: Your question (teacher template). tool.json `modes: ["Ladder", "Your question"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D1.2.3-5 | Tap the words in the big question that people might read differently, and pick the ideas behind them (money, jobs, travel, farming, town life) | "good" and "our town" lit with their "for whom?" cards; idea tags under the sign | 2 |
| D1.3.3-5 | For each rung, pick the key idea in the supporting question and mark it if it can be read more than one way ("faster" for people or for crops?) | the rung with its key idea underlined and a tag | 3 |
| D1.4.3-5 | Fit each supporting question on the ladder; a rung holds only if it helps answer the big question | rungs that click into place, and one that falls ("What color was the train?") | 4 |
| D2.His.12.3-5 | Build a question from each source, then one question that joins two sources | source cards beside the ladder, joined by a cord to their rung | 5 |

## Screens and modes
Header (kit): title "Inquiry Ladder"; `Ladder`, `Your question`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A tall wooden ladder against a town water tower, five empty rung slots, a sign at the top: "Was the railroad good for our town?" The welcome is queued (`welcomeAfter: true`): "Here's a big question about the past. Some words in it could mean different things to different people. Tap a word people might not agree on." First hint: "Tap a word in the question."

**Mark the words (focus: the sign).** Every word is tappable. "good" and "our town" light: "Good for whom? The store owners? The farmers? The people who drove wagons?" and "Does our town mean just the people in town, or the farms around it too?". Tapping "railroad" or "was": "Most people would agree on what that means. Look for a word that could mean different things." Then five idea tags appear; the child picks the ideas the question is about (money, jobs, travel, farming, town life; all can fit, at least two must be picked).

**Build rungs (focus: one source card and the question builder).** At 1366x768 the ladder sits left and the source and builder right; at 680x425 the source opens as a sheet over the ladder.
- Five source cards from one real railroad town around 1870 (items in Build notes). For each, the child reads the card (zoom and `Read` on the transcription) and builds a question from three tiles: a question starter (How did, Did, Who, Why did), a middle (the trains, the store, farmers, prices to ship crops, trips to the city) and an end (change, help, cost, sell more). Example questions that fit:
  - Depot picture: "How did the depot change what people did in town?"
  - Timetable: "Did faster trains help people reach the city?"
  - Farmer's letter (complaining about the price to ship grain): "Did the railroad charge farmers fair prices?"
  - Store ad (new goods "just arrived by rail"): "Did the railroad help stores sell more?"
  - Grange poster (farmers organizing): "Why did farmers join together against the railroad?"
- The child drags the question to a rung. It holds if it helps answer the big question; a question that doesn't ("What color was the train?") falls with "That's interesting, but does it help us know if the railroad was good for the town?" Then the child taps the key idea and marks it if it can be read two ways.

**Join two (focus: two source cards).** `Join two sources` opens: the child picks two cards and builds one question using both. Suggested pairs, all accepted: timetable and farmer's letter ("Did faster trains help farmers sell crops, even if shipping cost a lot?"), store ad and Grange poster ("Did the railroad help store owners more than farmers?"). It goes on the top rung.

**The top (end state).** The child climbs: each rung lights with its source. The sign changes to "Was the railroad good for our town? It depends who you ask." A for-whom chart shows store owners, travelers, farmers and wagon drivers with what the sources hint for each (the child taps each: "helped", "helped and hurt", "hurt", "not sure yet"). `Print` prints the ladder with all rungs, sources and the chart.

**Your question (extra).** The teacher types a big question and adds up to five sources (image plus a short transcription); tiles become free text. Nothing leaves the page.

## Build notes
- Sources come from one real Illinois or Iowa railroad town of the 1860s to 1870s, picked at build so that all of these exist in public domain: a depot photograph or engraving (Library of Congress or a state historical society), a railroad timetable (Library of Congress railroad maps and timetables), a farmer's letter and a store's ad from the town's newspaper (Chronicling America), and the 1873 Grange print "Gift for the Grangers" (Library of Congress). Each item's link goes in the credits.
- If one town lacks an item, the build uses the same state and decade and labels each item with its real town (see Open questions).

## Content
- Big question with two contested words and five idea tags; five sources with transcriptions; question tiles (4 starters, 10 middles, 6 ends); one falling question; one join; the for-whom chart.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Join two sources` shows only after four rungs hold. The for-whom chart shows only at the top.
- Keyboard: Tab through words, tiles and rungs; Enter to pick and place.
- With Motion off rungs appear without clicking in and the falling question disappears without falling.

## Look
- Accent `--brand` #8c3b2a water tower rust (header, the ladder rails, the sign); gold #f4c542 (a lit word, a holding rung, the join cord); paper #fbf3f0; ink #2a0f09; muted #62524d.
- Contrast (WCAG 2.1, computed): white on brand 7.57:1; brand on paper 6.91:1; ink on paper 16.38:1; muted on paper 6.77:1; ink on gold 11.03:1.
- Never color alone: holding rungs show a check; contested words get a dotted underline and a "for whom?" card.
- Different from this batch (learn-and-earn teal, made-for-whom slate, economy map blue, bill maroon).

## Art
- Public domain (credited): five source images (see Build notes).
- Local FLUX (`scripts/localart.py`): the water tower and ladder scene (1, 3:4 at 1366x768 crop).
- Drawn in code: rungs, the sign, tiles, cards, the cord, the chart.
About 6 images. No people art.

## Voice
One bank voice, unique in this batch: `curious-librarian` as the narrator and reader of every source. `Curio.voice` with `scope: () => state.mode + ':' + state.part + ':' + state.source`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each word's "for whom?" line or the "most people would agree" line.
- how `ideas`: "Pick the ideas this question is about."
- event, whole, each source transcription.
- how `build`: "Build a question from this source with the tiles."
- how `rung`: "Drag your question to the ladder."
- event, whole, `falls`.
- how `key`: "Tap the key idea. Could it mean two things?"
- how `join`: "Tap Join two sources and pick two cards."
- event, whole, `top`: "It depends who you ask."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: tappable sign words, the tile question builder with a fit check against the big question's idea tags, the ladder, the join, the for-whom chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Contested words | Tap every word | Words most people agree on say so; the step needs both contested words found. |
| Rungs | Build any question | A question holds only if its middle and end connect to a picked idea tag; off-topic ones fall. |
| Join | Pick the same source twice | The second pick must be a different card. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Words: lines (whole); `ideas`.
2. Each source: transcription (whole), waits; `build`; `rung`; `falls` if needed; `key`.
3. `join`; top: `top` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D1.2, D1.3, D1.4 and D2.His.12 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Railroads helped towns that got a depot grow, brought goods to stores, and let farmers ship crops to city markets | Library of Congress, "Railroads in the late 19th century" (classroom materials) | Smithsonian National Museum of American History, "America on the Move" | yes |
| Farmers in the 1870s formed the Grange and protested high railroad shipping prices | Library of Congress, "Gift for the Grangers" (1873) and Grange classroom materials | Nebraska Studies (NET), "The Grange" | yes |
| Illinois, Iowa, Minnesota and Wisconsin passed "Granger laws" in the 1870s to limit rail and grain rates | Wikipedia, Granger Laws (checked 2026-11-09) | Encyclopaedia Britannica, "Granger movement" | yes |
| Chronicling America newspapers before 1930 are free to use | Library of Congress, Chronicling America "About" and rights | Library of Congress, copyright and primary sources guide | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r7, 2026-11-09): tiles make at least one fitting question per source; "What color was the train?" matches no idea tag; at least two join pairs fit; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 ladder and builder fit; at 680x425 the source is a sheet.
2. "good" and "our town" light with their cards; agreed words say so. (D1.2.3-5)
3. Each rung's key idea can be marked. (D1.3.3-5)
4. Only questions that connect to the big question hold. (D1.4.3-5)
5. Each source makes one rung, and one rung joins two sources. (D2.His.12.3-5)
6. Every source shows its credit.
7. `Join two sources` is never named before it shows.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no rung or fall motion; no network requests.

## Open questions
- Which real town supplies the five sources (default used: the build picks one Illinois or Iowa railroad town of about 1870 with all five public-domain items; if one is missing, it uses the same state and decade and labels each item's real town).
