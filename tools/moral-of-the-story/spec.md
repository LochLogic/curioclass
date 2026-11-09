# Moral of the Story

## One idea
At Nana Owl's storytelling table, every story is a hand of cards: first the class lays the event cards in order to tell the story back, then plays a lesson card and the one event card that teaches it, because a lesson is only won when the proof is in the story; the lesson cards come back to the hand after each round, and the class finds out that one lesson card can win two stories from opposite sides of the world (an Anansi tale from Ghana and a fable from ancient China both say no one knows everything).

## Not like
- story-map-treasure (1, spec): one story mapped with feelings, lesson and proof. Here six fables and folktales from five traditions as a card game, where lessons are reused across stories and one story can teach two lessons.
- story-stage (k, spec): acting a folktale on a puppet stage. Here recounting and finding the lesson.
- two-sides-theater (2, spec): two characters' points of view on one scene. Here the message of each whole story.
- author-s-mailbox (2, spec): the author's purpose in fact texts. Here the lesson in stories.
- myth-museum (4, concept): myths. Here fables and folktales for grade 2.

## Who and how
- Grade 2, ELA, module "Stories and Lessons" (Reading Literature). Standard: RL.2.2.
- Driver: a pair at one device or the teacher on a projector (tool.json `driver: "either"`). Every story page and card is read aloud (BASELINE rule 4).
- Six stories, each a round: The Lion and the Mouse and The Ant and the Grasshopper (Aesop, ancient Greece), Anansi and the Pot of Wisdom (Asante, Ghana; also told in the Caribbean), The Talkative Tortoise (Panchatantra, India; also a Jataka tale), The Monkey and the Crocodile (a Jataka tale, India; also in the Panchatantra), The Frog in the Well (the Zhuangzi, China). tool.json `modes: []`, `minutes: "15-25"`, `grades_label: "Grade 2"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.2.2 | Recount: lay five event cards in order (one decoy from another story is in the deal and must be left out) | the story strip; Nana retells along it | 2 |
| RL.2.2 | Play a lesson card and the event card that teaches it | the lesson and proof slots; a story card won | 3, 4 |
| RL.2.2 | Across stories: see a lesson card win two stories from different places | the lesson card's two stamps on the map of origins | 5 |

## Screens and modes
Header (kit): title "Moral of the Story"; `Stories`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A storyteller's table by lamplight with Nana Owl and a deck. A small world map on the wall shows where each story is told. First hint: "Tap the deck to hear the first story." The first tap starts the story with its line; the welcome is queued after it (`welcomeAfter: true`).

**Hear it.** Nana tells the story in six short pages (picture 720 x 405, one or two sentences each), with each word lit. The story's place and tradition show on a small tag ("Told by the Asante people of Ghana").

**Tell it back.** Six event cards are dealt face up (five from the story and one decoy from another story). Focus: the story strip, five slots, 1360 wide at 1366x768. Drag cards to slots (or tap, then a slot); the decoy goes on the discard tray. `Check`: right cards in right slots lock; the rest lift and wiggle. When all five lock, Nana retells along the strip.

**Find the lesson.** The class's lesson hand (six lesson cards, the same hand all game) fans at the bottom. Play a lesson card in the Lesson slot and one of the five locked event cards in the Proof slot, then `Play`. Right pair: the story card flips into the class's book, stamped with the lesson. Right lesson, wrong proof: "That lesson fits. Which event teaches it?" Wrong lesson: Nana asks the lesson's question ("Was anyone getting ready for later?").

**The lesson hand.** The six lesson cards return after each round. When a lesson card wins a second story, it gets a second stamp, and a thread on the wall map joins the two places.

**My book.** All won story cards with their lessons; a tap rereads the story's proof event.

At 1366x768 the strip, the deal and the hand fit above the fold. At 680x425 slots are 120 x 160 and the hand overlaps.

## Content
All retellings written for Curio Class from public-domain tellings. Each: five events in order | decoy | right lesson and proof (some stories accept two pairs).

**Lesson hand (six cards):** A. Even someone small can be a big help. B. Be kind, and kindness may come back to you. C. Work now so you are ready later. D. No one knows everything; there is always more to learn. E. Know when to stay quiet. F. Stay calm and think fast when you are in trouble.

1. **The Lion and the Mouse** (Aesop): A lion caught a little mouse. | The mouse begged, "Let me go, and one day I will help you." | The lion laughed and let him go. | Hunters caught the lion in a net. | The mouse chewed the ropes and set the lion free. Decoy: The turtle told the frog about the sea. Accepted pairs: A with "The mouse chewed the ropes"; B with "The lion laughed and let him go."
2. **The Ant and the Grasshopper** (Aesop): All summer, the ant carried food to her home. | The grasshopper sang and played. | "Why work so hard?" he laughed. | Winter came, and the grasshopper was cold and hungry. | The ant shared a little food, and the grasshopper said, "Next summer I will get ready too." Decoy: The tortoise opened his mouth to talk. Pair: C with "All summer, the ant carried food to her home."
3. **Anansi and the Pot of Wisdom** (Asante, Ghana): Anansi the spider gathered all the wisdom in the world into one pot. | He wanted to hide it at the top of a tall tree. | He tied the pot to his front, and he could not climb. | His little son Ntikuma said, "Tie it on your back, Father." | Anansi was so cross that the pot fell and broke, and wisdom spread everywhere. Decoy: The mouse chewed the ropes. Pair: D with "His little son Ntikuma said, 'Tie it on your back.'"
4. **The Talkative Tortoise** (Panchatantra; Jataka): The pond where Tortoise lived was drying up. | Two geese said, "Hold this stick in your mouth, and we will fly you to a new lake." | "Don't say a word," they warned. | People below shouted, "Look at that silly tortoise!" | Tortoise opened his mouth to answer, let go, and tumbled into a muddy marsh, far from his friends. Decoy: The grasshopper sang and played. Pair: E with "Tortoise opened his mouth to answer."
5. **The Monkey and the Crocodile** (Jataka; Panchatantra): Monkey shared sweet fruit with his friend Crocodile every day. | Crocodile's wife wanted to eat Monkey's heart. | Crocodile gave Monkey a ride across the river and told him the plan. | Monkey stayed calm and said, "My heart is up in my tree! Take me back to get it." | Back at the tree, Monkey jumped to safety. Decoy: Anansi tied the pot to his front. Pair: F with "Monkey stayed calm and said, 'My heart is up in my tree!'"
6. **The Frog in the Well** (Zhuangzi): A frog lived at the bottom of an old well. | He thought his well was the whole world. | A sea turtle came by and tried to climb in, but the well was too small. | The turtle told the frog about the sea, so wide and deep. | The frog was amazed; the world was much bigger than his well. Decoy: The lion laughed and let him go. Pair: D with "The turtle told the frog about the sea."
Shared lesson: D wins Anansi (Ghana) and the Frog (China). Deal order is fixed per story, never the event order.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tell it back: `Check` locks right placements only; the decoy in a slot lifts with "That's from another story!" There's no limit on checks; the round's first star counts a full strip on the first Check.
- Find the lesson: a story card is won with any accepted pair; Lion and Mouse accepts two and, when both are found, the card shows both stamps ("A story can teach more than one lesson").
- Lesson cards are never used up; that is the point of the hand.
- Stories are played in order 1 to 6; a story can be replayed from My book.

## Look
- Accent `--brand` #6d2e46 deep wine (header, card backs, frames); gold #f4c542 (stamps, stars, lamp glow); paper #fbf6f2; ink #24141a; muted #64525a. Scene: a lamplit storyteller's table.
- Contrast (WCAG 2.1, computed): white on brand 9.86:1; brand on paper 9.19:1; ink on paper 16.44:1; muted on paper 6.76:1; ink on gold 10.85:1.
- Never color alone: lesson cards have a letter-free icon each (a mouse paw, a heart, an acorn, a lantern, a finger on lips, a calm face) plus their words; card states have outlines and stamps.
- Each tradition's story cards carry a border pattern drawn in code from simple geometric motifs (no sacred symbols); the art for each story is in a shared warm gouache style so no tradition looks like a costume of another.
- Different from this batch (rain blue, velvet red, playground orange, lab purple).

## Art
Local FLUX (`scripts/localart.py`); every character is an animal, so no people art.
- table (1): "A cozy lamplit storyteller's table with a deck of cards and a small world map on the wall, soft gouache, no text"; 16:9; cutout no.
- Nana Owl (3, tell, listen, cheer): "A grandmotherly owl with a shawl <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- story pages (36, six per story): "<a lion holding a little mouse / a spider carrying a clay pot up a tree in a West African forest / two geese flying with a tortoise holding a stick / a monkey on a crocodile's back in a river in India / a frog at the bottom of an old stone well / ...>, warm storybook gouache"; 16:9; cutout no. The Anansi, Panchatantra, Jataka and Zhuangzi pages are reviewed in the fresh-agent sensitivity review for setting details (plants, pots, landscape) that fit the story's place.
- event card thumbnails reuse page art, cropped.
About 40 images. Drawn in code: cards, border motifs, slots, stamps, the map thread, controls.

## Voice
Bank voice `wise-mentor` as Nana Owl, who tells every story (unique in this batch). `Curio.voice` with `scope: () => state.story + ':' + state.step`, `welcomeAfter: true`.
- event `deck`: "Story one."
- how `welcome`: "Come sit by the lamp. Every story hides a lesson. First tell it back, then find the lesson and the part that teaches it."
- event, whole, `page`: the story page.
- event `origin`: "This story is told {by the Asante people of Ghana}."
- how `tellHow`: "Put the event cards in order. One card is from another story. Leave it out."
- event `decoy`: "That's from another story!"
- event `locked` / `notYet`: "Just right." / "Some cards need to move."
- event, whole, `retell`: the five events.
- how `lessonHow`: "Play a lesson card and the event that teaches it."
- event `won`: "Yes! {The mouse chewed the ropes}, so {even someone small can be a big help}."
- event `proofNo`: "That lesson fits. Which event teaches it?"
- event `lessonNo`: "{Was anyone getting ready for later?}"
- event `twice`: "This lesson won two stories, from {Ghana} and {China}. People all over the world tell it."
- event `two`: "A story can teach more than one lesson."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tell it back | Place cards at random | 6 cards for 5 slots: 720 ordered fills (computed), one right; the star needs it on the first Check. |
| Find the lesson | Try lesson cards in turn | 6 lessons x 5 proofs = 30 pairs per story (computed), 1 or 2 accepted; the lesson question names what to look for. |
| Shared lesson | Always play D | It wins 2 of 6 stories only. |
| Proof | Always the last event | The proof is the last event in 2 of 6 stories (computed: Lion and Mouse pair A, Tortoise). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the deck: `deck`, `welcome` (queued, first time), `origin`, then `page` (whole) per page.
2. Tell it back: `tellHow` (first time); Check: `locked` or `notYet`, `decoy`; then `retell` (whole).
3. Lesson: `lessonHow` (first time); Play: `won`, `proofNo` or `lessonNo`; `twice` when D wins its second story; `two` when Lion and Mouse gets both stamps.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.2.2 wording (recount fables and folktales from diverse cultures, and determine their central message, lesson or moral) | thecorestandards.org, RL Grade 2 | CCSS ELA 2010 PDF | yes |
| The Lion and the Mouse and The Ant and the Grasshopper are Aesop's fables (plots as retold) | Library of Congress, "The Aesop for Children" (1919) | Project Gutenberg, Aesop's Fables (Townsend translation) | yes |
| Anansi gathers wisdom in a pot, cannot climb with it tied in front, his son Ntikuma says tie it behind, the pot breaks and wisdom spreads; an Asante (Ghana) tale also told in the Caribbean | Barker and Sinclair, West African Folk-Tales (1917), "How Wisdom Became the Property of the Human Race" (Baldwin Project, mainlesson.com) | African Storybook / Global Storybooks, "Anansi and Wisdom" | yes |
| The talkative tortoise carried on a stick by birds falls when he speaks; told in the Panchatantra and as the Kacchapa Jataka | Ryder, The Panchatantra (1925) | Cowell, ed., The Jataka (1895 to 1907), No. 215 (sacred-texts.com) | yes |
| The monkey saves himself by saying his heart is in the tree; told in the Jataka (Sumsumara Jataka) and the Panchatantra (Book 4) | Cowell, ed., The Jataka, No. 208 | Ryder, The Panchatantra (1925), Book 4 | yes |
| The frog in the well and the sea turtle come from the Zhuangzi, chapter 17 "Autumn Floods" | Chinese Text Project (ctext.org), Zhuangzi, "Floods of Autumn" (Legge translation) | Giles, Chuang Tzu (1889), chapter 17 | yes |
Backed twice: 6. Cut: 0.

Changes from the old tellings, for the sensitivity review: the grasshopper is not left to starve (the ant shares a little, and he promises to get ready); the tortoise lands in a muddy marsh far from his friends instead of dying; the crocodile's wife's plan is told plainly with no eating shown. Tellings differ on small details (who gave Anansi the pot); ours keeps the common core: tied in front, the son says tie it behind.

Checks run (Python, scratchpad b7, 2026-11-08): 6P5 = 720 strip fills; 6 x 5 = 30 lesson pairs per story; D accepted in stories 3 and 6 only; proof positions per story (5 or 3, 1, 4, 5, 4, 4: last in 2 of 6); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the strip, deal and hand fit with no scroll; at 680x425 the same, smaller.
2. Tell it back: each story's five events lock only in order; the decoy never locks. (RL.2.2)
3. Find the lesson: each story's accepted pairs win and no other pair does. (RL.2.2)
4. Lion and Mouse accepts both A and B pairs and shows both stamps.
5. Lesson D wins Anansi and the Frog, gets two stamps, and the map thread joins Ghana and China. (RL.2.2)
6. Every story names its tradition and place on screen and aloud.
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Pre-reader: every page and card is read on tap.
9. Motion off: cards appear in place; no network requests; nothing saved.

## Open questions
- None for Cory.
