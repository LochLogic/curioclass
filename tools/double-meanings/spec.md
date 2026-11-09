# Double Meanings

## One idea
The student sorts lines from stories, speeches and ads into four bins (Pun, Verbal irony, Analogy, Allusion), taps the one word that does the double work and writes its surface meaning and its hidden one, then presses Flatten to swap that word for a plain one and watches a tone gauge drop and the second meaning vanish ("The Importance of Being Earnest" becomes "The Importance of Being Serious", and the joke on the name Ernest is gone), so they learn that a double meaning lives in one chosen word and that it shapes both the meaning and the tone.

## Not like
- allusion-hunter (7, spec, this batch): hunting allusions in everyday texts. Here four kinds of double meaning in literature and speeches, grade 8.
- word-thermometer (6, spec): connotation on a scale. Here a word doing two jobs at once.
- simile-slam (5, spec): similes. Here puns, irony, analogy and allusion.
- satire-decoder (11, concept): a whole satire's said and meant. Here single lines.
- poetry-soundboard (7, spec, this batch): sound devices. Here meaning devices.

## Who and how
- Grade 8, ELA, module "Puns, Irony and Allusion" (Reading Literature, Reading Informational Text, Language). Standards: RL.8.4, RI.8.4, L.8.5 (a, b, c).
- Driver: one student; class mode is a "groan or grin" vote on student puns that lasts while the page is open (tool.json `driver: "student"`). Every card is read on tap.
- About 24 line cards from public-domain works and speeches, plus ads written for Curio Class. tool.json `modes: ["Sort", "Nonfiction lines", "My poster line", "Groan or grin"]`, `minutes: "20-30"`, `grades_label: "Grade 8"`.
- Nothing is saved; `Print` prints the sorted cards with both meanings.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.8.5a | Sort puns and verbal irony and write both meanings | the card in its bin with the double word lit | 2 |
| RL.8.4 | In story lines, show how the device shapes meaning and tone; Flatten proves it | the flattened line and the tone gauge | 3 |
| RI.8.4 | In speech and informational lines, the same for analogies and allusions to other texts (Lincoln's "house divided", a scientist's analogy) | the nonfiction cards with their source links | 4 |
| L.8.5b | Use the relationship in an analogy card to explain an unfamiliar word or idea | the analogy map (this is to that as...) | 4 |
| L.8.5c | Name what the Flatten swap loses in connotation | the before-and-after words with the student's note | 3 |
| L.8.5a | Write a poster line with a double meaning on purpose; flatten it yourself | the poster with its gauge | 5 |

## Screens and modes
Header (kit): title "Double Meanings"; `Sort`, `Nonfiction lines`, `My poster line`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A wordsmith's print shop with four type drawers labeled Pun, Verbal irony, Analogy and Allusion, a stack of line cards, a tone gauge on the wall and a press with a `Flatten` lever; the shop's owner, Augustina Pell, an elderly typesetter. First hint: "Tap the top card to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Sort.** The student drags a card to a drawer, taps the word or phrase doing the double work, and writes the surface meaning and the hidden one in two short boxes. Story and speech lines include:
- Pun: the title "The Importance of Being Earnest" (Oscar Wilde, 1895), earnest and the name Ernest; Jack's last line, "I've now realised for the first time in my life the vital Importance of Being Earnest."
- Verbal irony: Tom Sawyer's "Does a boy get a chance to whitewash a fence every day?" (Mark Twain, 1876), where Tom pretends a chore is a treat.
- Analogy and allusion: Abraham Lincoln's "A house divided against itself cannot stand" (1858), a comparison between a house and a nation and an allusion to the Gospels.
- Allusion: the opening of the Gettysburg Address, "Four score and seven years ago", which points back to 1776 and the Declaration of Independence.
- Ads written for Curio Class: a bakery's "We knead you", a shoe store's "Our prices won't run away", a dentist's "Our service is tooth-ly yours".
Hard cards fit two drawers (an allusion used ironically); the student picks one and writes why.

**Flatten.** The student pulls the lever; the keyed plain swap replaces the double word ("knead" to "need", "Earnest" to "serious"), the gauge drops from playful or pointed to flat, and the student notes what was lost (the joke, the bite, the echo of another text).

**Nonfiction lines.** Speech and science lines with analogies and allusions: Lincoln's house divided; the Gettysburg opening; a science writer's analogy written for Curio Class ("A cell's membrane is a security gate"). The student fills an analogy map (membrane : cell :: gate : ___) and says what the comparison helps a reader understand.

**My poster line.** The student writes a line for a school poster with a double meaning, marks the double word, writes both meanings, then flattens it; the poster passes when the student confirms the flat version loses the second meaning.

**Groan or grin.** Student puns on the projector; the class votes.

At 1366x768 the drawers and card fit; at 680x425 the drawers are a row below the card.

## Content
- Public-domain lines (exact wording from the sources): The Importance of Being Earnest (Project Gutenberg #844), The Adventures of Tom Sawyer (Project Gutenberg #74), Lincoln's House Divided speech (1858) and Gettysburg Address (1863).
- Ads, the science analogy and the keyed plain swaps written for Curio Class.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Flatten can be undone.
- With Motion off the lever doesn't move; the gauge shows its new label at once.

## Look
- Accent `--brand` #7d2e5a print-shop plum (header, drawers, lever); gold #f4c542 (the double word, the gauge's lively band); paper #fbf2f7; ink #2a0c1d; muted #665062. Scene: a warm old print shop.
- Contrast (WCAG 2.1, computed): white on brand 8.71:1; brand on paper 7.94:1; ink on paper 16.38:1; muted on paper 6.63:1; ink on gold 11.05:1.
- Never color alone: the double word is underlined and bold; the gauge has words (flat, playful, pointed).
- Different from this batch (gym brick red, field olive, studio violet, chat teal).

## Art
- People art goes to Gemini: Augustina Pell (a white woman in her eighties with an ink apron and type in hand), 3 poses; "illustrated elderly typesetter <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): print shop with type drawers (1); a whitewashed fence with a bucket and brush, no people (1); a bakery window poster (1).
About 6 images. Drawn in code: drawers, cards, gauge, lever.

## Voice
Bank voice `wise-mentor` as Augustina Pell (unique in this batch); speech lines are read by `news-reader` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: "Each of these lines says two things at once. Find the word doing the double work, then flatten it and hear what's lost."
- event, whole, `card`: the tapped card.
- event `flat`: the flattened line, then "Flat. What did it lose?"
- event `twoDrawers`: "This one could go in two drawers. Pick one and say why."
- event, whole, `poster`: the poster line.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: keyed drawers with two-drawer alternates, double-word keys, Flatten swaps and gauge, analogy maps.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Guess drawers | Each card is keyed; wrong drawers ask for both meanings first. |
| Double word | Tap the longest word | The double word is keyed; another tap says "Which word is doing two jobs?" |
| Meanings | Write the same thing twice | The two boxes must differ by at least three words. |
| Poster | Write a plain line | Flatten must change the line; the student marks the double word. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the top card: `card`, `welcome` (queued, first time).
2. Flatten: `flat`.
3. Hard cards: `twoDrawers` as it fires.
4. My poster line: `poster` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.8.4, RI.8.4, L.8.5 wording | thecorestandards.org, Grade 8 | CCSS ELA 2010 PDF | yes |
| Wilde's title and Jack's last line, The Importance of Being Earnest (1895) | Project Gutenberg eBook #844 (checked 2026-11-09) | Folger or Penguin edition notes on the earnest and Ernest pun | yes |
| Tom Sawyer's line "Does a boy get a chance to whitewash a fence every day?" | Project Gutenberg eBook #74 (checked 2026-11-09) | Mark Twain Project or Library of America text of Tom Sawyer, chapter 2 | yes |
| "A house divided against itself cannot stand" (Lincoln, 1858), echoing the Gospels (Mark 3:25) | National Park Service, Lincoln Home, House Divided speech | Abraham Lincoln Online, House Divided speech | yes |
| "Four score and seven years ago" counts back 87 years to 1776 and the Declaration | Library of Congress, Gettysburg Address | National Park Service, Gettysburg Address | yes |
| Definitions of pun, verbal irony, analogy and allusion | Merriam-Webster, each entry | Purdue OWL, literary terms | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad b22, 2026-11-09): the Gutenberg files contain "Importance of Being Earnest" as Jack's last line and the whitewash line; 1863 minus 87 is 1776; every card's flatten swap removes the keyed double word; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 drawers and card fit; at 680x425 the drawers are a row below.
2. Cards sort with a tapped double word and two meanings. (L.8.5a)
3. Flatten swaps the word, drops the gauge and takes a loss note. (RL.8.4, L.8.5c)
4. Nonfiction lines and analogy maps work. (RI.8.4, L.8.5b)
5. My poster line flattens and is confirmed. (L.8.5a)
6. Groan or grin works while the page is open.
7. Print shows sorted cards with both meanings.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: lever and gauge don't move; no network requests.

## Open questions
- None for Cory.
