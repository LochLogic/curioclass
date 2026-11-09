# Myth Museum

## One idea
The student walks a museum where each Greek myth exhibit (a real public-domain object plus a short retelling) ends at an everyday phrase that points back to it, such as a Herculean task, an Achilles' heel, Pandora's box, the Midas touch, flying too close to the sun or an odyssey, and explains the phrase from the story; a second wing sets myths from different cultures side by side on one big question (where fire came from, why a great flood came), so they learn that old stories still live in our words and that people everywhere told stories about the same questions.

## Not like
- allusion-hunter (7, concept): allusions from many sources in ads and headlines. Same myths engine; here grade 4 Greek allusions and a compare wing.
- side-by-side-reader (spec): two texts of any genre. Here myths on one theme from different cultures.
- moral-of-the-story (2, concept): fable morals. Here myths and the phrases they gave English.
- idiom-illustrator (3-5, spec): idioms drawn literally. Here phrases explained from their source stories.
- theme-tracker (4, spec): theme in one tale. Here a pattern across cultures.

## Who and how
- Grade 4, ELA, module "Myths and Allusions" (Reading Literature). Standards: RL.4.4, RL.4.9.
- Driver: one student or a pair (tool.json `driver: "student"`). Every retelling, label and modern sentence is read on tap.
- Six Greek exhibits, two compare rooms (Fire, Flood), the gift shop quiz. tool.json `modes: []`, `minutes: "25-40"`, `grades_label: "Grade 4"`.
- Nothing is saved; `Print` prints the student's gift shop postcards (phrase, myth, meaning).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.4.4 | At each exhibit, read the retelling, then explain the phrase in a modern sentence by picking the story moment it comes from and the meaning | the phrase card with the story moment pinned | 2, 3 |
| RL.4.4 | Use the phrase in a new sentence of one's own | the student's sentence on the card | 3 |
| RL.4.9 | In each compare room, fill a grid for two myths (who, what happens, what it explains or teaches) and mark what is alike and different | the compare grid with alike and different marks | 4 |
| RL.4.4 | Gift shop quiz: tag each allusion in everyday sentences with its exhibit and its meaning there | tagged sentences | 5 |

## Screens and modes
Header (kit): title "Myth Museum"; `Lobby`, `Greek wing`, `Same Question, Many Stories`, `Gift shop`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A museum lobby with a modern sign: "Fixing this bug was a Herculean task." and Docent Ada, an owl in a docent's lanyard. First hint: "Tap the sign. What could it mean?" The first tap reads the sign; the welcome is queued after it (`welcomeAfter: true`).

**Greek wing.** Six exhibits in a hall map. Each exhibit: the object image with its label (title, maker, date, museum, credit line from the object record), a retelling of 150 to 250 words in three panels, and a phrase plaque with a modern sentence (a news headline, a coach's speech, a kid's text). The student:
1. Reads the retelling (tap to hear).
2. Pins the story moment the phrase comes from (three choices).
3. Picks what the phrase means in the modern sentence (three choices).
4. Writes a sentence of their own using the phrase (free text; the phrase must appear).

**Same Question, Many Stories.** Two rooms. Each room holds two myths told for Curio Class from published sources, each with its culture named and a short note about where the story comes from. A grid: Who is in it? What happens? What does it explain? What does it teach? The student fills it from chips, then marks alike and different rows with icons.
- Fire room: Prometheus (Greek) and the Water Spider (Cherokee).
- Flood room: Deucalion and Pyrrha (Greek, from Ovid) and Utnapishtim (Mesopotamian, from the Epic of Gilgamesh).

**Gift shop.** Ten everyday sentences ("My sister has the Midas touch with plants."). The student tags each phrase with its exhibit and picks its meaning in that sentence. Correct tags become postcards.

At 1366x768 the object and retelling fit side by side; at 680x425 they stack.

## Content
Greek exhibits (retellings written for Curio Class from public-domain sources; objects verified public domain at the museums on 2026-11-09):
1. Herakles, the twelve labors; phrase: a Herculean task. Object: Art Institute of Chicago 9696, "Tetradrachm (Coin) Depicting the Hero Herakles", 336 to 323 BCE.
2. Achilles, dipped in the river by his mother, all but his heel; phrase: an Achilles' heel. Object: The Met 416625, "Achilles and Hector", 1518.
3. Pandora and the jar; phrase: open Pandora's box. Object: Art Institute of Chicago 89885, "Pandora Opening her Box", 1809.
4. King Midas and the golden touch; phrase: the Midas touch. Object: The Met 437328, Nicolas Poussin, "Midas Washing at the Source of the Pactolus", about 1627.
5. Daedalus and Icarus; phrase: flying too close to the sun. Object: Art Institute of Chicago 149019, Giulio Romano, "Daedalus and Icarus", early 1530s.
6. Odysseus's ten-year trip home; phrase: an odyssey. Object: The Met 359855, Ugo da Carpi, "Penelope and Odysseus", about 1520 to 1527.
Compare rooms: Fire, Prometheus (Greek, from Hesiod; object: Art Institute of Chicago 81962, "Prometheus Taking Fire From Olympus") and the Water Spider who carried fire in a bowl on her back (Cherokee, as recorded in James Mooney's "Myths of the Cherokee", 1900, and as told by the Cherokee Nation). Flood, Deucalion and Pyrrha (Ovid, Metamorphoses, book 1) and Utnapishtim's boat (the Epic of Gilgamesh, tablet 11).
Rule for the Art step: each object image is viewed before use; any image with nudity or graphic violence is swapped for another verified public-domain object or a generated scene, and the swap is logged in the data file.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Object labels always show the museum and credit line; tapping opens the label in large type.
- Grid chips can be moved; alike and different marks are icons with words.
- Postcards print four to a page.

## Look
- Accent `--brand` #9c4321 vase terracotta (header, plaques, hall map); gold #f4c542 (pinned moments, postcards); paper #fcf4ef; ink #2b1208; muted #665249. Scene: a calm museum hall with columns.
- Contrast (WCAG 2.1, computed): white on brand 6.48:1; brand on paper 5.97:1; ink on paper 16.20:1; muted on paper 6.74:1; ink on gold 10.83:1.
- Never color alone: alike and different marks are icons with words; pinned moments are numbered.
- Different from this batch (garage blue, card crimson, lamp amber, editor green).

## Art
- Public-domain objects (7) from the Met and the Art Institute of Chicago open access, by the ids above, with the museums' credit lines.
- Local FLUX (`scripts/localart.py`): lobby (1); Docent Ada (4 poses: point, read, listen, smile), "A friendly owl museum docent with a lanyard <pose>, soft gouache, plain white background"; 1:1; cutout yes; retelling panels (6 exhibits by 3 panels, plus 4 compare myths by 2 panels = 26), "<scene>, painted in the style of a Greek red-figure vase, no text" for Greek myths; for the Water Spider and Utnapishtim, a plain storybook watercolor style (no imitation of a culture's sacred art): "a small water spider carrying a glowing coal in a woven bowl across a river at night, storybook watercolor, no text"; 4:3.
About 38 images: 7 museum objects and 31 generated.

## Voice
Bank voice `smooth-narrator` as Docent Ada and the retelling reader (unique in this batch). `Curio.voice` with `scope: () => state.room + ':' + state.exhibit + ':' + state.step`, `welcomeAfter: true`.
- event `sign`: "Fixing this bug was a Herculean task."
- how `welcome`: "Old stories still live in the words we use. The answer to that sign is in the Greek wing. Let's walk."
- event, whole, `retelling`: the panel's text.
- how `pinHow`: "Which part of the story does this phrase come from?"
- event `plaque`: the modern sentence.
- how `ownHow`: "Now use the phrase in a sentence of your own."
- how `compareHow`: "Two stories, one question. Fill in the grid, then mark what's alike and what's different."
- event `postcard`: "That one's going on a postcard."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
myths (`kit/myths.js`), new with this tool; this spec holds the full description so allusion-hunter (7) can reuse it. Pure parts in one marked block, exposed as `__tool.my`:
- **Myth**: `{id, culture, title, sourceNote, sourceEdition, panels:[{text, art}], moments:[{id, text}]}`. The culture and source note are required fields; the UI always shows them.
- **Allusion**: `{phrase, mythId, momentId, meaning, sentences:[{text, kind:'headline'|'speech'|'text'|'everyday', meaningHere}]}`. `my.find(text, allusions)` returns phrase matches with word-form tolerance (Herculean, Hercules-sized are listed forms, never guessed).
- **Object**: `{museum, objectId, title, maker, date, credit, image, publicDomain:true, viewed:true}`. `my.objectOk(o)` refuses a record without `publicDomain` and `viewed`.
- **Compare grid**: `my.grid(myths, rows)` returns a grid model with cells `{row, mythId, chips}` and `my.alikeDiff(grid)` returns the student's marks against the data's expected marks (advice, not a gate).
- **Tagger**: `my.tag(sentence, allusionId, meaningId)` returns `{phraseOk, meaningOk}`.
Allusion-hunter is expected to use Allusion, Object and Tagger with many sources; this tool uses all five parts.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Story moment | Guess | 3 choices; a wrong pin reads the moment it chose, so the reader hears why it doesn't fit. |
| Own sentence | Type the phrase alone | It must be in a sentence of 5 or more words; Docent Ada reads it back. |
| Compare grid | Fill chips randomly | Chips belong to one myth; wrong chips say which myth they're from. |
| Gift shop | Tag by guessing | Both the exhibit and the meaning must match; 10 sentences. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the sign: `sign`, `welcome` (queued, first time).
2. Exhibit: `retelling` (whole) per panel; `plaque`; `pinHow` (first time); `ownHow`.
3. Compare room: `compareHow`; retellings.
4. Gift shop: `postcard` for each correct tag.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.4.4 and RL.4.9 wording (RL.4.4 names allusions to significant characters in mythology, such as Herculean) | thecorestandards.org, Reading Literature Grade 4 | CCSS ELA 2010 PDF | yes |
| Phrase origins: Herculean, Achilles' heel, Pandora's box, the Midas touch, odyssey | Merriam-Webster, word history notes for each | Online Etymology Dictionary | yes |
| The Greek myths as told (labors of Herakles, Achilles' heel from later Roman-era tellings, Pandora's jar from Hesiod, Midas from Ovid, Daedalus and Icarus from Ovid, Odysseus from Homer) | Theoi Greek Mythology, source texts for each | Britannica, entries for each figure | yes |
| Cherokee: the Water Spider brings fire in a tusti bowl on her back | James Mooney, "Myths of the Cherokee" (1900), "The First Fire" (public domain, Project Gutenberg) | Cherokee Nation, cultural resources and storytelling | yes |
| Flood stories: Deucalion and Pyrrha (Ovid, Metamorphoses 1); Utnapishtim (Gilgamesh tablet 11) | Ovid, Metamorphoses, A. S. Kline translation (free online) | The British Museum, the flood tablet | yes |
| Museum objects are public domain, with the titles and dates given | The Met collection API object records (416625, 437328, 359855) | Art Institute of Chicago API records (9696, 89885, 149019, 81962) | yes |
Backed twice: 6. Cut: 2 (the Redon "Pandora" and the "Bronze Herakles", both public domain, are nudes, so they were not used).

Sensitivity note: the Cherokee story goes to the fresh-agent review and is credited to the Cherokee people with its source; no Native sacred art is imitated; each object image is viewed before use.

Checks run (Python, scratchpad b13, 2026-11-09): the seven object ids returned public domain with the titles and dates above from the Met and AIC APIs; each Greek exhibit has one phrase and three moments; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the object and retelling fit; at 680x425 they stack.
2. Each exhibit shows its object label and credit line, and its retelling reads by panel. (RL.4.4)
3. Phrase pins, meanings and own sentences work. (RL.4.4)
4. Compare rooms fill the grid and mark alike and different, with each culture named. (RL.4.9)
5. The gift shop tags 10 sentences and makes postcards. (RL.4.4)
6. `my.objectOk` refuses an object without public domain and viewed flags.
7. Postcards print.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no walking transitions between halls; no network requests.

## Open questions
- None for Cory.
