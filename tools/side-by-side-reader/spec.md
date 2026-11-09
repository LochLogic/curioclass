# Side by Side Reader

## One idea
Two texts open side by side on a reading table with a middle lane labeled "Both", and the student drags details into the middle when the texts share them or keeps them on their own side when they differ, tagging each one, then names what each text's build does and presses Rebuild to retell one text in the other's shape, so they learn that comparing texts means seeing what they share, where they part, and why the shape of each one matters.

## Not like
- alike-and-different-books (K-2, concept): sorting into hoops. Here texts read in full, tagged details, and structure at grade 5.
- myth-museum (4, concept): allusions to myths. Here whole pairs compared.
- structure-spotter (3, concept): one paragraph's structure. Here whole-text structure across two texts.
- mood-in-the-pictures (3-5, spec): one text in three media. Here two different texts.
- moral-of-the-story (2, spec): one lesson shared by two stories, played as a card. Here full comparison lanes with tags and structure.

## Who and how
- Grades 3-5, ELA, module "Comparing Texts Side by Side" (Reading). Standards: RL.3.9, RI.3.9, RL.4.9, RI.4.9, RL.5.5, RI.5.5.
- Driver: one student or a pair (tool.json `driver: "student"`). Every sentence is read on tap.
- Three shelves, each a full lesson so each code gets its depth: Same Characters (grade 3, RL.3.9), Same Topic (grades 3 to 5, RI.3.9, RI.4.9, RI.5.5), Same Tale, Many Places (grade 4, RL.4.9); RL.5.5 has its own Whole and Part task on the Same Characters pair. tool.json `modes: []`, `minutes: "20-30 per shelf"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints the two-column chart.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.3.9 | Same Characters: drag theme, setting and plot details from two stories about the same characters to Both or a side | the three lanes filled with tagged cards | 2 |
| RI.3.9 | Same Topic: drag key points and details from two honeybee texts | the lanes, tagged fact | 3 |
| RI.4.9 | Same Topic: answer a question using both texts (a two-sentence answer with one detail from each) | the answer card with two source pins | 4 |
| RL.4.9 | Same Tale: compare the pattern of events and theme in two tellings of one tale type from different cultures | the event strips lined up and a theme card | 5 |
| RI.5.5 | Same Topic: name each text's structure (chronology, question and answer) and press Rebuild | the rebuilt text beside the original | 6 |
| RL.5.5 | Whole and Part: pick the chapter that sets up the problem, the one that turns it, and explain how one chapter fits the whole story | chapter strip with roles | 7 |

## Screens and modes
Header (kit): title "Side by Side Reader"; `Shelves`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A library reading table with two open books, a green middle lane, and Mr. Basil the tortoise, the reading-room librarian. Three shelves. First hint: "Tap a shelf to open two books." The first tap opens the pair with its line; the welcome is queued after it (`welcomeAfter: true`).

**Reading table.** Focus: two text columns (each 420 wide; sentences tap to hear) with the lane between them. Below, a tray of 10 to 14 detail cards per pair (in data, each with its true lane and tag). Drag a card to Left, Both or Right; then pick its tag (character, setting, plot, theme, fact, structure). `Check` lights each card: right lane and tag, right lane wrong tag, or wrong lane, with the sentence(s) that show why highlighted in the texts.

**Same Characters (grade 3).** Two original Curio Class stories about Pip and Toot, a hedgehog and a mole: "The Lost Map" (they find their way using what each is good at) and "The Big Rain" (they save the garden together). Shared theme: friends are stronger together; different settings and plots.

**Same Topic (grades 3 to 5).** Two honeybee texts: "A Year with the Hives" (a beekeeper's diary, in time order) and "Bee Questions, Bee Answers" (a question-and-answer page). Grade 3 drags facts; grade 4 adds the both-texts question ("How do bees get ready for winter?"); grade 5 names the structures and presses Rebuild, which shows the diary rewritten as questions and answers, and the student picks what the time order made clear that the Q and A didn't (the order of the year).

**Same Tale, Many Places (grade 4).** Two clever-small-animal tales from two cultures: "The Hare and the Lion" (India, Panchatantra) and "The Hare of Inaba" (Japan, Kojiki). Event strips line up under both texts: a small animal is in a fix; it makes a plan; it tricks the big animals using their pride; then the endings part. The student drags event cards onto the strips and picks the theme card for each tale.

**Whole and Part (grade 5, RL.5.5).** "The Big Rain" in four short chapters; the student assigns roles (sets up, raises the problem, turns it, wraps up) and finishes "Chapter 3 fits the whole story because..." from tiles.

At 1366x768 two columns, the lane and the tray fit; at 680x425 the columns become tabs over the lane.

## Content
- Same Characters: two original stories, 10 to 12 sentences each; 12 cards (4 Both, 4 Left, 4 Right).
- Same Topic: two original texts, 10 to 12 sentences each, all bee facts sourced; 14 cards. Facts: worker bees are female; bees make honey from nectar; bees do a waggle dance to share where flowers are; in winter honeybees cluster together to stay warm; a hive has one queen; bees pollinate many crops.
- Same Tale, Many Places: "The Hare and the Lion" (Panchatantra, India; public domain in Arthur W. Ryder's 1925 translation): a lion eats one animal a day; the hare, late on purpose, says another lion is in the well; the lion leaps at his reflection. "The Hare of Inaba" (from the Kojiki, Japan): a hare wants to cross the sea, tricks sea creatures (told as crocodiles or sharks) into lining up so he can "count" them, and brags before he reaches shore. Shared pattern: a small animal outwits big ones by playing on their pride. Different endings: the lion is fooled and the threat ends; the Inaba hare boasts too soon, is hurt, and is healed by a kind god, so its theme adds "don't brag before you're safe". This difference is the RL.4.9 point. 12 cards per pair.
- Retellings for Curio Class: no animal dies on screen; the lion's leap ends with a splash and the story says he was never seen again in that forest; the Inaba hare's hurt is told as "the sharks pulled out his fur" and he is healed.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be moved until `Check`; after, wrong cards wobble and stay movable.
- Tags are a second step after each drop and can be changed by tapping the card.
- The both-texts answer needs one pin from each text: the student taps a sentence in each column to pin it.
- Rebuild is a reveal, not a quiz; the pick after it has reasons.

## Look
- Accent `--brand` #2f5d3a reading-table green (header, lane, shelves); gold #f4c542 (pins, lit cards); paper #f5f9f4; ink #13231a; muted #4f5e53. Scene: a calm library reading table with lamps.
- Contrast (WCAG 2.1, computed): white on brand 7.64:1; brand on paper 7.18:1; ink on paper 15.38:1; muted on paper 6.45:1; ink on gold 10.06:1.
- Never color alone: lanes are labeled (Left book title, Both, Right book title); tags have icons.
- Different from this batch (gallery plum, planetarium navy, radio orange, story teal).

## Art
Local FLUX (`scripts/localart.py`), animal characters only.
- table (1): "A calm library reading table with two open books and green lamps, soft gouache, no text"; 16:9; cutout no.
- Mr. Basil (4, read, point, nod, think): "A kind old tortoise librarian with reading glasses <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- covers (6): "<book cover art: a hedgehog and a mole with a map / ...>, soft gouache, no text"; 3:4; cutout no.
- tale scenes (8): the hare and lion at the well, the hare on the line of sharks; style per tale ("Indian miniature painting inspired, soft colors" / "Japanese woodblock print inspired, soft colors"), avoiding sacred figures (the kind god is shown as a warm light only).
About 19 images. Drawn in code: lanes, cards, tags, strips, pins.

## Voice
Bank voice `curious-librarian` as Mr. Basil and as the reader of all texts (unique in this batch). `Curio.voice` with `scope: () => state.shelf + ':' + state.task`, `welcomeAfter: true`.
- event `open`: "Two books: {The Lost Map} and {The Big Rain}."
- how `welcome`: "Welcome to the reading table. Read both, then drag each detail to Both if the books share it, or to its own side if they don't."
- event, whole, `sentence`: the tapped sentence.
- how `tagHow`: "What kind of detail is it? Tap a tag."
- event `checked`: "{9} in the right lane. Tap a wobbling card to see why."
- how `answerHow`: "Answer the question with one detail from each text. Tap a sentence in each to pin it."
- event `rebuild`: "Same facts, new shape. What did the time order make clear?"
- how `wholeHow`: "Give each chapter its job. Then tell how chapter three fits."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Lanes | Put everything in Both | About a third of cards belong in Both (4 of 12 or 5 of 14); the rest light wrong (checked). |
| Tags | One tag for all | Each pair uses at least four tags (checked). |
| Both-texts answer | Pin two sentences from one text | It needs one pin per column. |
| Chapter roles | Guess | 24 orders of four roles, 1 right; wrong roles show the chapter's key line. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a shelf: `open`, `welcome` (queued, first time).
2. Tap a sentence: `sentence` (whole). Drop a card: `tagHow` (first time).
3. Check: `checked`.
4. Same Topic: `answerHow`; grade 5 Rebuild: `rebuild`. Whole and Part: `wholeHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.3.9, RI.3.9, RL.4.9, RI.4.9, RL.5.5, RI.5.5 wording | thecorestandards.org, Reading Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Honeybee facts (female workers, nectar to honey, waggle dance, winter cluster, one queen, crop pollination) | USDA, honey bees and pollinators | Penn State Extension, honey bee biology | yes |
| "The Hare and the Lion" (the hare tricks the lion with its reflection in a well) is a Panchatantra tale; Ryder's 1925 translation is public domain | Project Gutenberg, Ryder, The Panchatantra | Britannica, Panchatantra | yes |
| The Hare of Inaba appears in the Kojiki: a hare tricks sea creatures (wani, told as crocodiles or sharks) into a bridge by counting them, is skinned, and is healed by Ōkuninushi | Kokugakuin University, Encyclopedia of Shinto, Inaba no shirousagi | Britannica, Kojiki | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: two cultural tales go to the fresh-agent review (rule 5); the Inaba tale involves a Shinto deity, shown only as light; endings softened as in Content.

Checks run (Python, scratchpad b9, 2026-11-08): Both share per pair; tags used per pair at least 4; one-lane answer score; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 both columns, lane and tray fit; at 680x425 columns are tabs.
2. Same Characters: cards check lane and tag with why-highlights. (RL.3.9)
3. Same Topic: fact cards check. (RI.3.9)
4. The both-texts answer needs one pin per text. (RI.4.9)
5. Same Tale: event strips line up and the theme difference is named. (RL.4.9)
6. Rebuild shows the diary as Q and A, then the pick with reasons. (RI.5.5)
7. Whole and Part assigns chapter roles and finishes the fit sentence. (RL.5.5)
8. Print gives a two-column chart.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: cards don't wobble (an outline marks them); no network requests.

## Open questions
- None for Cory.
