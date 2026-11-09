# Old Patterns, New Stories

## One idea
The student reads three short modern stories written for Curio Class that quietly borrow from old ones (a sixteen-year-old drone racer who flies too high, an underdog robotics team against a champion school, a new kid who keeps outwitting the boys who tease him), lays pattern cards under each until one fits (Icarus, David and Goliath, Anansi the trickster), pairs the old detail with the new one and marks each pair kept, changed or new, then plans a modern story of their own on a pattern they choose, so they learn how writers borrow themes, plots and character types from myths, folk tales and religious works and make them new.

## Not like
- shakespeare-remix (9, concept): a change log between Shakespeare and his source. Here modern stories on myth, folk tale and Bible patterns, grade 8.
- allusion-hunter (7, spec): short allusions in everyday texts. Here a whole story's pattern under a modern plot.
- setting-swap (7, spec): moving one story to a new setting. Here finding the old pattern first, then writing a new story on it.
- myth-museum (4, spec): Greek myths behind words. Here three traditions as story patterns.
- paragraph-surgeon (8, spec, this batch): the role of each sentence. Here pairs of old and new story details.

## Who and how
- Grade 8, ELA, module "Modern Takes on Classic Stories" (Reading Literature). Standard: RL.8.9.
- Driver: one student; class mode is a gallery of beat sheets sorted by pattern that lasts while the page is open (tool.json `driver: "student"`). Every story and card is read on tap.
- Three modern stories, six pattern cards (three keyed and three that fit partly or not at all: Pandora's box, the Tortoise and the Hare, Cinderella), and the planning studio. tool.json `modes: ["Stories", "My remix", "Gallery"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.
- Nothing is saved; `Print` prints the pairs and the beat sheet.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.8.9 (draws on a myth, traditional story or religious work) | Lay pattern cards under a story until one fits; say which details made it fit | the story with its pattern card and the student's reason | 2 |
| RL.8.9 (themes, events, character types) | Pair old details with new (Daedalus' warning and Dad's battery warning) and label each pair as theme, event or character type | the pair lines between the source card and the story | 3 |
| RL.8.9 (rendered new) | Mark each pair kept, changed or new and write what the change does for a modern reader | the pair labels and notes | 3 |
| RL.8.9 | Plan a modern story on a chosen pattern: what stays, what becomes new, why it matters now; write its opening | the beat sheet and opening | 4 |

## Screens and modes
Header (kit): title "Old Patterns, New Stories"; `Stories`, `My remix`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A long library table with three new paperbacks on one side and a deck of old, worn pattern cards on the other; the librarian, Ms. Adwoa Mensah, sits at the end. First hint: "Tap the first book to hear it." The first tap reads the story's opening; the welcome is queued after it (`welcomeAfter: true`).

**The three stories** (about 500 words each, written for Curio Class).
- "Ceiling": Kai, sixteen, races drones. His dad, who built the first one with him, warns him not to fly above the tree line where the wind takes it and the cheap battery drains. In the final, Kai climbs for the shot no one else will try, the battery dies, and the drone drops into the lake. Pattern: Icarus.
- "The Garage Team": four students from a small school build a robot in a garage and face the three-time champion school with a lab of its own. They win with a small, fast robot and one exact move. Pattern: David and Goliath.
- "The New Kid": Kofi moves to a new school; two older boys keep trying to make him look foolish, and each time he turns their trick back on them with a joke, a rule they forgot or a question; in the last scene his own trick goes too far and his little sister has to set it right. Pattern: Anansi the trickster.

**Stories.** The student reads a story, then drags pattern cards under it. Each card has a short retelling (tap to hear). A card that fits lights "fits" once the student taps two story details that match it; a partial card says "Some of this fits. What's missing?" Then the student draws pair lines between details on the card and in the story, labels each pair Theme, Event or Character type, and marks it Kept, Changed or New, with a short note on what the change does for a reader now ("The wax becomes a cheap battery, so the danger is something a reader could buy").

**My remix.** The student picks a pattern card and fills a beat sheet: what stays (the pattern's core), what is new (setting, characters, ending), and one line on why the change would matter to a reader now; then writes an opening scene of about 150 words.

**Gallery.** Beat sheets on the projector, sorted by pattern.

At 1366x768 the story and cards fit side by side; at 680x425 the cards are a drawer below.

## Content
- Modern stories written for Curio Class, with keyed details, pairs, labels and accepted alternates.
- Source cards: short retellings written for Curio Class.
  - Icarus, from Ovid's Metamorphoses, Book VIII (Riley translation, 1851): Daedalus warns his son to keep to the middle course, the wax melts when Icarus flies too high.
  - David and Goliath, from 1 Samuel 17 in the Hebrew Bible (King James text): the shepherd boy with a sling against the armored giant. Credited as "a story from the Hebrew Bible" and told as a literary source, with no religious claim.
  - Anansi, from Akan (Fante and Asante) storytelling of present-day Ghana, as written down in West African Folk-Tales (W. H. Barker and Cecilia Sinclair, 1917): "How Wisdom Became the Property of the Human Race", where Anansi tries to hide all wisdom in a pot and his son outwits him. The card says Anansi stories are a living tradition, told today in Ghana and the Caribbean.
  - Decoy cards: Pandora's box, the Tortoise and the Hare (Aesop), Cinderella (Perrault).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be moved and pairs redrawn at any time.
- With Motion off pair lines appear without drawing.

## Look
- Accent `--brand` #6b4e16 old-bronze (header, card backs, pair lines); gold #f4c542 (a fitting card, kept pairs); paper #f9f5ec; ink #221805; muted #5e5546. Scene: a warm library table by a window.
- Contrast (WCAG 2.1, computed): white on brand 7.70:1; brand on paper 7.08:1; ink on paper 16.07:1; muted on paper 6.74:1; ink on gold 10.75:1.
- Never color alone: pair labels have words (Kept, Changed, New) and different line patterns.
- Different from this batch (curtain red, slate blue, surgical green, council violet).

## Art
- Public domain (Art Institute of Chicago): 149019 "Daedalus and Icarus", Giulio Romano, early 1530s; 48948 "David and Goliath", Rembrandt van Rijn, 1655. Each image is viewed before use.
- People art goes to Gemini: Ms. Adwoa Mensah (a Ghanaian American woman in her fifties with reading glasses), 3 poses; "illustrated school librarian <pose>, soft gouache, plain white background"; 1:1; cutout yes. Story covers with people: Kai with a drone controller (a Native Hawaiian teen), the garage team (four mixed teens), Kofi with his sister (Ghanaian American children); 1 each, Gemini.
- Local FLUX (`scripts/localart.py`): a library table with books and cards (1); a spider on a web over a clay pot, drawn as a plain nature picture (1).
- Anansi art is a plain spider and pot only; no copying of Akan symbols, kente or Adinkra designs, and no sacred objects.
About 9 images. Drawn in code: pair lines, labels, beat sheet.

## Voice
Bank voice `calm-professor` as Ms. Mensah and the hint voice (unique in this batch); stories and source cards are read by `gentle-storyteller` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.story + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: "Each of these new stories is built on a very old one. Find the old story underneath, then show what was kept and what was made new."
- event, whole, `story`: the story or its opening.
- event, whole, `source`: the source card's retelling.
- event `fits`: "That one fits. Now draw the pairs."
- event `partial`: "Some of this fits. What's missing?"
- event `pairAsk`: "What does that change do for a reader now?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: story and card data with keyed details, the fit rule, pair lines with labels, the beat sheet. Myth records are not used; these cards are story patterns, not word origins.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fit | Drag every card under every story | A card fits only after two matching details are tapped; decoys never fit fully. |
| Pairs | Draw lines between random details | Each pair is checked against the keyed pairs and alternates. |
| Kept, changed, new | Mark everything Kept | Each pair's label is keyed; at least three pairs per story need a note. |
| Beat sheet | Retell the old story | "What is new" must change at least two of setting, characters or ending. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the first book: `story`, `welcome` (queued, first time).
2. Cards: `source` (whole) on tap; `fits` or `partial` when placed.
3. Pairs: `pairAsk` as it fires.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.8.9 wording | thecorestandards.org, Reading Literature Grade 8 | CCSS ELA 2010 PDF | yes |
| Daedalus warns Icarus to fly the middle course; the sun melts the wax when he flies too high (Ovid, Metamorphoses VIII) | Project Gutenberg eBook #26073, Riley translation (checked 2026-11-09) | Britannica, Daedalus | yes |
| David defeats Goliath with a sling and a stone (1 Samuel 17) | Project Gutenberg eBook #10, King James text (checked 2026-11-09) | Britannica, Goliath | yes |
| Anansi the spider is a trickster of Akan storytelling, and the stories are called spider stories; the wisdom-pot tale | Project Gutenberg eBook #66923, Barker and Sinclair 1917 (checked 2026-11-09) | Britannica, Anansi | yes |
| AIC 149019 (Giulio Romano) and 48948 (Rembrandt) are public domain | Art Institute of Chicago API, is_public_domain true (checked 2026-11-09) | Art Institute of Chicago artwork pages, CC0 | yes |
Backed twice: 5. Cut: 0.

Sensitivity note: the David and Goliath card is a literary source with no religious claim; Anansi is a living Akan tradition, credited by people and place, with no imitation of sacred or cultural designs; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b23, 2026-11-09): the Gutenberg files contain Daedalus' middle-course warning and the melting wax, "prevailed over the Philistine with a sling", and the wisdom-pot tale under "HOW WISDOM BECAME THE PROPERTY OF THE HUMAN RACE"; the AIC API returned both ids as public domain; each story has at least four keyed pairs covering theme, event and character type; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 story and cards fit; at 680x425 the cards are a drawer.
2. Cards fit only after two matching details; decoys say what's missing. (RL.8.9)
3. Pairs take labels (theme, event, character type; kept, changed, new) and notes. (RL.8.9)
4. My remix checks two changes and takes an opening scene. (RL.8.9)
5. Source cards credit their traditions as in Content.
6. Gallery works while the page is open; Print shows pairs and beat sheet.
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pair lines appear at once; no network requests.
9. The fresh-agent sensitivity review has passed the Anansi and David cards.

## Open questions
- None for Cory.
