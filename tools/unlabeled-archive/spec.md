# Unlabeled Archive

## One idea
An archivist leaves a note with a question ("What did Europeans know about the Americas by 1650?") and a box of four real sources whose labels have been lost: a printed letter in Latin, a silver coin, a map fragment and a picture print; the child picks one, finds a clue (the old spelling of the letter's words, the mint mark and king's name on the coin, California drawn as an island on the map, an engraver's signature on the print), checks it against a reference shelf (a list of rulers and their years, a timeline of how maps drew California, a list of printers' and engravers' marks, a dictionary of old spellings), and fills the label (maker, date range, place, intended audience), with later sources needing two references; then they rate each source's usefulness for the archivist's question with reasons from its label, and learn that a beautiful source can be weak for a given question, so a seventh grader learns to infer a source's maker, date, place and audience from other sources, and to judge how relevant and useful a source is.

## Not like
- historians-disagree (7, spec): secondary accounts. Here real primary objects.
- source-scout (5, spec): fact and opinion. Here dating and placing sources.
- evidence-corkboard (8, spec): building an argument. Here labeling the evidence first.
- museum-label-writer (6, spec): writing a label for visitors. Here working out what the label should say.

## Who and how
- Grade 7, Social Studies (History), module "Unlabeled Archive". Standards: D2.His.11.6-8 (use other historical sources to infer a plausible maker, date, place of origin, and intended audience for historical sources where this information is not easily identified), D2.His.13.6-8 (evaluate the relevancy and utility of a historical source based on information such as maker, date, place of origin, intended audience, and purpose).
- Format: puzzle. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Four sources, the reference shelf, four labels, the usefulness ratings. Extra: A second box (four new sources for a new question about Asia and Europe by 1650). tool.json `modes: ["Box one", "Box two"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.11.6-8 | Find a clue on each source, check it on the reference shelf, and fill maker, date range, place and audience | the magnifier on the clue; the matching reference card; the filled label | 2, 3 |
| D2.His.13.6-8 | Rate each source High, Some or Low for the archivist's question with a reason from its label | the usefulness rack with four rated sources and reasons | 4 |

## Screens and modes
Header (kit): title "Unlabeled Archive"; `Box one`, `Box two`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** An archive reading room: a gray archival box, cotton gloves, a magnifier, a reference shelf with four books, and a note on the table. The welcome is queued (`welcomeAfter: true`): "The archivist's note asks: what did Europeans know about the Americas by 1650? But this box lost its labels. Open the box and pick a source." First hint: "Tap the box."

**The sources (focus: the source and the magnifier).** At 1366x768 the source fills the center with the shelf right and the label card below; at 680x425 shelf and label are sheets. Each is a real object (ids checked at build), shown large; the child drags the magnifier to find clues (two or three per source, one a red herring).
1. A printed letter in Latin: Columbus's letter about his first voyage, printed in Rome in 1493. Clues: the Latin words for "islands lately found"; the printer's name at the end. References: the old-spelling dictionary; the printers' marks list. Label: maker Christopher Columbus (writer) and a Rome printer; date 1493; place Rome; audience educated readers across Europe.
2. A silver coin: a Spanish piece of eight from the mint at Potosí (in today's Bolivia), from the reign of Philip IV. Clues: the mint mark P; the king's name and number. References: the rulers list (Philip IV ruled Spain 1621 to 1665); the mints list. Label: the Potosí mint, 1621 to 1665, Potosí, for trade and paying royal debts.
3. A map fragment: part of a map of North America with California drawn as an island. Clues: the island; English place names. References: the map timeline (most printed maps drew California as part of the mainland until the early 1620s, then often as an island until the 1700s); the engravers' marks list. Label: an English mapmaker (Henry Briggs's map of 1625 is the target); date 1622 to about 1650; London; English readers of travel books. Two references needed.
4. A picture print: an engraving of a village of Algonquian people on the coast of today's North Carolina, after the watercolors of John White, published by Theodor de Bry in Frankfurt in 1590. Clues: the engraver's signature; Latin captions. References: the engravers' marks list; the old-spelling dictionary. Label: de Bry after John White; 1590; Frankfurt; European readers buying travel books. Two references needed.
- A wrong guess plays the clue's question back ("When did Philip IV rule? Check the rulers list.").

**The usefulness rack (the aha, D2.His.13.6-8).** The child rates each source for the archivist's question: High, Some or Low, with a reason built from the label (date, audience, purpose). The rack accepts reasons, not just ratings: the Columbus letter shows what Europeans first read in 1493 (High for "first knowledge"); the coin shows Spain minting silver in the Americas (Some, it tells about wealth, not what people knew); the map shows a mistake many Europeans believed (High, mistakes count as knowledge); the de Bry print is beautiful and widely sold, but it was made by a European engraver who never crossed the ocean, reshaping White's paintings (Some to High, with its limits). Narrator: "A source can be beautiful and still answer a question only in part. Its maker, date and audience tell you how far to trust it."

**The end.** Four labels, the rack and the reasons. `Print` prints them as an archive finding aid.

**Box two (extra).** Four sources for "What did Europeans know about Asia by 1650?".

## Content
- Four real sources with two or three clues each (one a red herring), a reference shelf of four books with dated entries, four answer labels with accepted ranges, the usefulness rack with reason tiles, the second box.
- The archivist is made up and labeled; every source and reference entry is real and checked at build.
- The de Bry print is shown with a note that it is a European image of Algonquian people, made from another artist's paintings.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Dates are entered as a range; any range inside the accepted window passes, and the label shows how narrow it is.
- References open as books with tabs; the child taps an entry to pin it to the label as proof.
- Keyboard: Tab to the box, sources, clues (each clue is a focusable hotspot), the shelf and the label; Enter to pick and pin.
- With Motion off the magnifier moves without zooming.

## Look
- Accent `--brand` #3d5a4c archive green (header, the box, the shelf); gold #f4c542 (a found clue, a pinned reference); paper #f1f5f2; ink #0f1d16; muted #525a55.
- Contrast (WCAG 2.1, computed): white on brand 7.59:1; brand on paper 6.90:1; ink on paper 15.80:1; muted on paper 6.46:1; ink on gold 10.69:1.
- Never color alone: clues carry a ring and a number; ratings carry words.
- Different from this batch (printer's sepia, Philadelphia navy, canal blue, signal orange).

## Art
- Public domain, real objects (ids and rights checked at build): the 1493 Rome printing of Columbus's letter (Library of Congress, Rosenwald Collection); a Potosí piece of eight of Philip IV (American Numismatic Society or Smithsonian National Numismatic Collection); Henry Briggs's 1625 map "The North part of America" (Library of Congress or Stanford's California as an Island collection); de Bry's 1590 engraving of the village of Secotan (Library of Congress). Each with credit.
- Local FLUX (`scripts/localart.py`): the reading room (1, 16:9).
- People art goes to Gemini with `people: true`: the archivist (1; cutout yes).
- Drawn in code: the magnifier, shelf books, label cards, the rack.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the archivist; `clear-teacher` as the reference books and narrator. `Curio.voice` with `scope: () => state.mode + ':' + state.source + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `clue`: "Drag the magnifier over the source to find a clue."
- event, whole, each clue found.
- how `shelf`: "Open a reference book and pin the matching entry."
- how `label`: "Fill the label: maker, date, place, audience."
- how `rate`: "Rate this source for the question and give a reason."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the source viewer with clue hotspots, the reference shelf, the label card with ranges, the usefulness rack.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Labels | Guess wide date ranges | A range wider than the window plays "Can a clue narrow it?" and the label shows the width. |
| References | Fill labels without pinning | Each label needs a pinned reference as proof; two for the later sources. |
| Rack | Rate everything High | Each rating needs a reason tile from the label, and the coin's High plays "Does a coin show what people knew?" |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `clue`; clue found (whole).
2. `shelf`; `label`.
3. `rate`, for each source.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.11.6-8 and D2.His.13.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Columbus's letter on the first voyage, printed in Rome in 1493 in Latin | Library of Congress, "Columbus letter" (Rosenwald Collection) | Encyclopaedia Britannica, "Christopher Columbus: the first voyage" | yes |
| Potosí's mint and the piece of eight; Philip IV ruled 1621 to 1665 | Smithsonian National Numismatic Collection, Spanish colonial coinage | Britannica, "Philip IV (Spain)" | yes |
| California drawn as an island on many maps from the 1620s; Briggs's 1625 map | Library of Congress, "California as an Island" | Stanford Libraries, Glen McLaughlin Map Collection, "California as an Island" | yes |
| De Bry's 1590 engravings after John White's watercolors of Algonquian people | Library of Congress, de Bry's "America" | British Museum, John White drawings | yes |
| De Bry reshaped White's images for European buyers | British Museum, John White drawings | Britannica, "Theodor de Bry" | yes |
Backed twice: 6. Cut: 0.

Sensitivity note: the de Bry print shows Algonquian people through a European engraver's eyes; a note says so, and the rack treats its limits as part of the lesson. A fresh-agent read of that note is needed before build.

Checks run (Python, scratchpad r14, 2026-11-09): every label's answer window sits before 1650, the archivist's date (1493; 1621 to 1665 overlaps, accepted to 1650; 1622 to 1650; 1590); sources 3 and 4 need two references each; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 source, shelf and label; at 680x425 sheets.
2. Each source has findable clues, one a red herring. (D2.His.11.6-8)
3. Four labels fill with pinned references and checked ranges. (D2.His.11.6-8)
4. The rack rates four sources with reasons. (D2.His.13.6-8)
5. The de Bry note shows.
6. Box two loads.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no zooming; no network requests (all images bundled).

## Open questions
- Sensitivity flag: the de Bry print shows Algonquian people through a European engraver's eyes (default used: a plain note on its limits, fresh-agent read before build).
