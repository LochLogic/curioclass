# Main Idea Pinboard

## One idea
On a detective's corkboard, the student writes the main idea of a short text on a card and pins the exact sentences that prove it with string, and a coverage meter shows whether the card is big enough to cover the key details and whether each pin proves the card or only repeats it, so they learn that a main idea is something the text has to back up; at grade 5 the text holds two main ideas and the board needs two cards, and at every grade the pinned lines become a short summary the student edits.

## Not like
- main-idea-umbrella (2, spec): an umbrella sized over raindrops. Here pinned exact sentences, who-what-why questions, author's support at grade 4 and two main ideas at grade 5.
- headline-writer (3, spec): a headline and three proof details for a news story (RI.3.2). Here RL.3.2 fables, RI.4.2, RI.5.2 and quoting.
- quote-picker (4, concept): choosing quotes for the student's own paragraph. Here proving an author's main idea.
- claim-court (5, concept): judging evidence quality. Here coverage of key details.
- because-bridge (K-2, spec): reasons on a bridge. Same evidence engine, older texts.

## Who and how
- Grades 3-5, ELA, module "Main Idea with Text Evidence" (Reading). Standards: RL.3.1, RI.3.1, RL.3.2, RI.4.2, RI.4.8, RI.5.1, RI.5.2, W.5.9.
- Driver: one student or a pair (tool.json `driver: "student"`). Every sentence is read on tap.
- Grade picker sets the texts: grade 3 (two fables, two articles), grade 4 (two articles, one with an author's point), grade 5 (three articles with two main ideas each). tool.json `modes: []`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints the board and summary.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.3.1, RI.3.1 | Answer two who-what-why questions by pinning the line that answers each | the question cards with their pinned lines | 2 |
| RL.3.2 | Fables: recount the events (order three event cards) and pin the lines that carry the central message | the message card with pins | 3 |
| RI.4.2 | Write the main idea card, pin supporting sentences, watch the meter | the coverage meter lighting key details | 4 |
| RI.4.8 | Grade 4 point articles: pin each reason under the author's point and the evidence under each reason | a point card with reason and evidence pins | 5 |
| RI.5.1 | Grade 5: pins become exact quotes, and each pin is tagged "says it" (stated) or "shows it" (inference) | quote cards with a tag | 6 |
| RI.5.2 | Grade 5: two main idea cards, each with its key details | two cards, two meters | 6 |
| W.5.9 | Build a summary paragraph from the pinned lines and edit it | the summary card | 7 |

## Screens and modes
Header (kit): title "Main Idea Pinboard"; `Texts`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A detective's office with a corkboard, a desk lamp and Detective Mole in a trench coat. First hint: "Tap a case file to open a text." The first tap opens the text with its line; the welcome is queued after it (`welcomeAfter: true`).

**Board.** The text on the left (sentences numbered, tap to hear and to pin), the corkboard on the right with an empty main idea card. The student types the card (up to 20 words) or, at grade 3, may choose from three cards (one too small, one too big, one right) and see each tested on the meter.

**Pinning.** Tap a sentence, then the card: a pin and a string join them. The meter (a row of key-detail lights, 3 to 5 per text from the pack's key) lights for each pinned sentence the key rates 3 for the card's idea. A pinned sentence that only restates the card (the evidence engine's `repeats` check against the card text) turns gray with "This says the idea again. What proves it?" A pin the key rates 0 shows "One reading doesn't see this here."

**Card size.** The card text is checked for size with the pack's key-word groups: a card that matches only one key detail gets "Too small: this is one detail"; one with none of the text's key words gets "Too big: what is this text mostly about?" The meter shows both failing; the student revises.

**Who-what-why** (all grades). Two questions per text; pin the answering line.

**Grade 4 point articles.** The card becomes "The author's point" with reason slots; under each reason, pin the evidence (a fact, a number, an example).

**Grade 5.** Two cards; pins are word ranges (exact quotes, shown with quotation marks), each tagged "says it" or "shows it".

**Summary.** `Make summary` turns the card and the strongest pins into three draft sentences in the student's own editing box; the student edits (the helper flags a sentence that copies 8 or more words in a row from the text: "Put it in your own words or quote it").

At 1366x768 the text and board fit side by side; at 680x425 the board is a tab.

## Content
Texts (sentences numbered; facts sourced):
- Grade 3 fables (Aesop, public domain in the 1919 Library of Congress tellings, lightly retold): "The Crow and the Pitcher" (message: little by little does the trick); "The North Wind and the Sun" (kindness works better than force).
- Grade 3 articles (original): "Sea Otters Use Tools" (otters float on their backs and crack shellfish with rocks) and "How Beavers Build Dams".
- Grade 4 articles (original): "Our Town Needs More Trees" (author's point: plant more street trees; reasons: shade cools streets, trees soak up rainwater, trees give birds homes; evidence from sources) and "Where Do Monarchs Go?" (main idea plus details: eastern monarchs fly to central Mexico for winter and lay eggs on milkweed).
- Grade 5 articles (original), two main ideas each: "Coral Reefs" (why reefs matter; what harms them); "The Erie Canal" (how it was built; what it changed); "Volcano Watchers" (how scientists watch volcanoes; why warnings matter).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pins can be removed by tapping the string's end; the meter updates.
- Checks are advice; nothing is refused; the meter is the feedback.
- Exact quotes at grade 5 are selected by tapping first and last words, with no words skipped in between.

## Look
- Accent `--brand` #6b4423 cork brown (header, card frames, strings); gold #f4c542 (meter lights, the lamp); paper #fbf6f0; ink #24160b; muted #62574c. Scene: a cozy detective office with a corkboard.
- Contrast (WCAG 2.1, computed): white on brand 8.48:1; brand on paper 7.89:1; ink on paper 16.36:1; muted on paper 6.54:1; ink on gold 10.81:1.
- Never color alone: meter lights carry a check and the detail's short name; gray pins carry the note.
- Different from this batch (film-set red, curtain plum, notecard green, blueprint blue).

## Art
Local FLUX (`scripts/localart.py`), animal detective, no people.
- office (1): "A cozy cartoon detective office with a corkboard and desk lamp, soft gouache, no text"; 16:9; cutout no.
- Detective Mole (4, think, pin, magnify, cheer): "A friendly mole detective in a trench coat with a magnifying glass <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- spot art (14, one per text: a crow at a pitcher, a sea otter with a rock, a beaver dam, a tree-lined street, kids at a pool, monarchs, a reef, a canal boat, a volcano with sensors); 4:3; cutout no.
About 19 images. Drawn in code: corkboard, cards, pins, strings, meter.

## Voice
Bank voice `knowing-guide` as Detective Mole (unique in this batch). `Curio.voice` with `scope: () => state.text + ':' + state.step`, `welcomeAfter: true`.
- event `case`: "Case file: {Sea Otters Use Tools}."
- how `welcome`: "Every text has a main idea, and the text has to prove it. Write the idea on the card, then pin the lines that prove it."
- event, whole, `sentence`: the tapped sentence.
- how `pinHow`: "Tap a sentence, then tap the card to pin it."
- event `repeats`: "This says the idea again. What proves it?"
- event `small` / `big`: "Too small: this is one detail." / "Too big: what is this text mostly about?"
- event `covered`: "Every key detail is lit. Case closed!"
- how `summaryHow`: "Now edit your summary. Keep it short, in your own words."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
evidence (`kit/evidence.js`), described in full in tools/theme-ledger/spec.md, exposed as `__tool.ev`. This tool uses: Source pack (each text with a key rating sentences 0 to 3 per claim), Spans (whole sentences at grades 3 and 4; word ranges at grade 5, no skips), Claims (the main idea card; `ev.claimCheck` for the too-short card), Evidence links (pins), checks (`repeats` against the card text, `offKey`), Strength (`ev.coverage` for the meter), Board view. Not Ledger, Series, Draft or Sides. Card size (too small, too big) is this tool's own check on the pack's key-word groups.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Meter | Pin every sentence | The meter lights only key-rated pins, but pinning all would light them; so the board caps pins at the number of key details plus one, and off-key pins show their note. |
| Card size | Copy the title onto the card | Titles are short; `claimCheck` returns topic (under 5 words or no verb) and the card asks for a whole idea. |
| Who-what-why | Guess pins | One line answers each; wrong pins show the line that does. |
| Says it or shows it | Tag all "says it" | Each grade 5 text has at least two inferences in its key (checked). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a case file: `case`, `welcome` (queued, first time).
2. Tap a sentence: `sentence` (whole). First pin: `pinHow`.
3. Pins: `repeats`, `small`, `big` as they fire; all lit: `covered`.
4. Summary: `summaryHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| The eight standards' wording | thecorestandards.org, Reading and Writing Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Sea otters use rocks to crack open shellfish, often resting on their backs | Monterey Bay Aquarium, sea otter facts | NOAA Fisheries, sea otter species page | yes |
| Beavers build dams of sticks and mud that make ponds | US Fish and Wildlife Service, beaver | National Park Service, beavers | yes |
| Street trees shade and cool streets and soak up rainwater | USDA Forest Service, urban forests | US EPA, heat island cooling strategies (trees) | yes |
| Coral reefs shelter many sea species; warming water causes bleaching | NOAA Ocean Service, coral reefs | US EPA, coral reefs and climate | yes |
| The Erie Canal opened in 1825 and linked the Hudson River to Lake Erie | New York State Canal Corporation, history | National Park Service, Erie Canalway | yes |
| Eastern monarchs winter in central Mexico and lay eggs on milkweed | US Fish and Wildlife Service, monarch butterfly | National Park Service, monarch migration | yes |
| Scientists watch volcanoes with seismometers, gas and ground-movement sensors | USGS Volcano Hazards Program | Smithsonian Global Volcanism Program | yes |
| "The Crow and the Pitcher" and "The North Wind and the Sun" are Aesop fables in public-domain tellings | Library of Congress, The Aesop for Children (1919) | Project Gutenberg, Jacobs, The Fables of Aesop | yes |
Backed twice: 9. Cut: 1 (a "Why Cats Purr" article; the science is not settled, so it was dropped).

Checks run (Python, scratchpad b11, 2026-11-09): pin cap equals key details plus one; each grade 5 key has at least two inference spans; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the text and board fit; at 680x425 the board is a tab.
2. Who-what-why questions accept the answering line. (RL.3.1, RI.3.1)
3. Fables need ordered events and message pins. (RL.3.2)
4. The meter lights key details; repeat pins gray; card size notes fire. (RI.4.2)
5. Grade 4 point articles take reason and evidence pins. (RI.4.8)
6. Grade 5 takes two cards, exact quotes and says-it or shows-it tags. (RI.5.1, RI.5.2)
7. The summary is drafted from pins and flags long copied runs. (W.5.9)
8. Print shows the board and summary.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: strings appear without swinging; no network requests.

## Open questions
- None for Cory.
