# Question Cube

## One idea
Two teams take turns rolling a giant question cube after a read-aloud; whatever word lands on top (Who, What, Where, When, Why, How) is the question, every answer card on offer is really in the book, so only the question word tells which one fits, and a team earns its second point only by lighting the one sentence that proves it.

## Not like
- class-phone-call (k-2, spec): the class chooses which question word to ask a caller. Here the cube chooses the question and the class answers it from a text it can see, with proof.
- meet-the-book-makers (k, spec): tap the page that shows a detail the class picked. Here the proof is one sentence in a projected text, and the question word does the sorting.
- alike-and-different-books (k-2, spec): two books prove cards by flipping to a page. Here one text, a cube and two teams.
- because-bridge (k-2, concept): reasons that support a point. Here any question word, including why.
- big-book-pointer (k, spec, same format): Dot the mouse reads word by word. Here whole sentences and question words.
- socratic-seminar-board (10, spec, same format): a talk map for older students. Here a K-2 team game.

## Who and how
- Grades K-2, ELA, module "Question Words and Key Details" (Reading Informational Text). Standards: RI.K.1, RI.1.1, RI.1.2, RI.1.3, RI.2.1, RL.2.1, RL.2.3.
- Driver: teacher on a projector (tool.json `driver: "teacher"`); two teams, Team Sun and Team Moon, talk it over and say their answer; a helper taps. Every question, card and sentence is spoken and every card is a picture, so a child alone can play as one team (BASELINE rule 4: alone, both turns are theirs).
- Two read-alouds: `Sea Otters` (fact text, K-2: RI codes) and `Nia's Sandcastle` (story, grade 2 tag: RL.2.1, RL.2.3). tool.json `modes: []` (texts picked from the shelf), `minutes: "15-25"` per text, `grades_label: "Grades K-2"`.
- Not a personal prompt. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.K.1, RI.1.1, RI.2.1 | Answer the rolled who, what, where, when, why or how question about Sea Otters by picking the card that fits the question word, then light the sentence that proves it; on the You ask face, ask the other team a question | the cube's top face and question; three answer cards, all from the text; the proving sentence glows | 2, 3, 6 |
| RI.1.2 | Gold face Mostly about: pick the main topic, then retell two key details aloud with a frame and light each one | the topic card in the center; two lit sentences | 4 |
| RI.1.3 | Gold face Connect: pick how two pieces of information are connected (the kelp and the sleeping otter) and prove it | three connection cards; the proving sentence | 4 |
| RL.2.1 | Answer the six question faces about Nia's Sandcastle and prove each | as above, story text | 2, 3 |
| RL.2.3 | Gold faces How did Eli respond? and How did Nia respond? to the wave: pick and prove each character's response | three response cards, one of them the other character's response | 5 |

## Screens and modes
Header (kit): title "Question Cube"; `Books` (shelf icon); `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The shelf: two book covers (Sea Otters, Nia's Sandcastle), big, each with its picture; the cube sits between them. First hint: "Pick a book. Tap Sea Otters or Nia's Sandcastle." The first tap opens that book and plays `open` (its own line); `Read the book` then starts on its own after the welcome (`welcomeAfter: true`), so the first path is hear the book, then roll. The rules ("Roll the cube, answer the question, then prove it in the book") are in the hint and Read until the first answer.

**The game screen** (both books).
- Focus while answering: the cube (code-drawn 3D cube, 200 px, faces with code icons: Who a face, What a box with a question mark, Where a map pin, When a clock, Why a light bulb, How a hand turning a gear; gold faces: a star) and, beside it, the question bubble (26 px) and three answer cards (190 x 150, painted picture plus words, spoken on tap).
- Focus while proving: the book strip: the text as numbered sentence panels, two rows (7 or 8 panels, 240 x 175 each, a small painting over the sentence in 20 px type). Tapping a panel reads its sentence.
- Top bar of the stage: the score (Team Sun: a code-drawn sun and its points; Team Moon: a moon), and the turn badge (whose turn, 80 px).
- Panel (right, 300 px): hint, `Roll` (gold, cube icon, 120 px), `Read the book` (open book), `Hear it again` (ear), `Pass` (arrow), `New game` (circle arrow).
- 1366x768: header 56, score 50, cube row 240, book strip two rows 380: all above the fold. At 680x425: the cube 110 px, cards 120 x 96, the book strip one row of four with `<` `>` to see the rest (the hint says "Swipe or tap the arrows to see more of the book").

**A turn.** Tap `Roll`: the cube tumbles (1.2 s; Motion off: it shows its new face at once with a click sound) and lands on a face this book has not used yet. The question is read (`question`, whole). The team talks, then taps a card. Right: 1 point, the card flies to the team's side, `rightAnswer`, then the prove step: "Now prove it! Tap the sentence that tells." Right sentence: it glows gold, it is read, +1 point (`proved`). Wrong sentence: it is read, `notProof` ("That sentence doesn't tell {it}. Try another."), and the team may try once more; a second miss shows the proving sentence with no point. Wrong card: `wrongAnswer` explains by question word ("A rock is a what, not a where."), the card dims, and the other team may steal by picking from the two left (1 point, no proof step); then the proving sentence is shown and read. The turn passes.

**Gold cube.** When all six faces are done for a book, the cube turns gold (a flip), with three faces repeated twice: for Sea Otters, Mostly about, Connect and You ask; for Nia, Eli responds, Nia responds and You ask. Rolling works the same.
- Mostly about (RI.1.2): three topic cards (sea otters, kelp, rocks). Right: the card sits center, then "Tell two details about sea otters. Then tap the two sentences." The team says two details aloud, then lights two sentences: any two of the seven count (every sentence is a key detail of this short text); 1 point for the topic, 1 for two lit sentences. `Say it` plays the frame: "This book is mostly about sea otters. It tells that ___ and ___."
- Connect (RI.1.3), Eli responds and Nia responds (RL.2.3): three cards and a proof, as a normal face.
- You ask (RI.K.1, RI.1.1, RI.2.1): "Your team asks a question! Pick a question word, then ask the other team about the book." Six question-word buttons; the team picks one and asks aloud; the other team answers aloud and taps the sentence that proves it; the asking team taps `Good answer` (thumbs up) or `Try again` (thumbs sideways); a good answer with a lit sentence gives the answering team 1 point and the asking team 1 point for the question.

**End.** When the gold faces are done: the score, both teams cheered (`final`), and `Other book` / `Play again`.

## Content
**Sea Otters** (our own text; 7 sentences, 91 words):
1. Sea otters live in the ocean near the shore.
2. They float on their backs in beds of kelp, a tall seaweed.
3. At night, a sea otter wraps itself in kelp so it will not drift away while it sleeps.
4. Sea otters dive to the sea floor to find food, like crabs, clams and sea urchins.
5. An otter uses a rock to crack open a hard shell.
6. Sea otters have very thick fur that keeps them warm in cold water.
7. A mother otter carries her baby, called a pup, on her belly.
Faces (question; right card and proof; two other cards from the text):
- Who: Who carries the baby otter? a mother otter (7) | a crab | in the ocean
- What: What does an otter use to crack open a shell? a rock (5) | at night | a mother otter
- Where: Where do sea otters live? in the ocean near the shore (1) | a rock | at night
- When: When does an otter wrap itself in kelp? at night (3) | on the sea floor | thick fur
- Why: Why do sea otters stay warm in cold water? They have very thick fur. (6) | They float on their backs. | They dive to the sea floor.
- How: How does a sea otter find food? It dives to the sea floor. (4) | It wraps itself in kelp. | It floats on its back.
- Mostly about: sea otters (right) | kelp | rocks.
- Connect: How are the kelp and the sleeping otter connected? The kelp keeps the otter from drifting away. (3) | The otter eats the kelp. | The kelp keeps the otter warm.

**Nia's Sandcastle** (our own text; 8 sentences, 76 words):
1. On Saturday morning, Nia built a sandcastle at the beach.
2. Her little brother, Eli, helped her pat the sand.
3. Then a big wave rushed up and knocked down the tower.
4. Eli started to cry.
5. Nia took a deep breath.
6. "We can build it again, farther from the water," she said.
7. They carried wet sand up the beach in a red bucket.
8. This time the waves could not reach it, and Eli put a shell on top.
Faces:
- Who: Who helped Nia build? Eli, her little brother (2) | a big wave | at the beach
- What: What knocked down the tower? a big wave (3) | Eli | on Saturday morning
- Where: Where did they build the second castle? farther from the water (6) | a red bucket | on Saturday morning
- When: When did Nia build the sandcastle? on Saturday morning (1) | a shell | farther from the water
- Why: Why did the second castle stay standing? The waves could not reach it. (8) | Eli put a shell on top. | They used a red bucket.
- How: How did they carry the wet sand? in a red bucket (7) | with a deep breath | in their hands
- Eli responds: How did Eli feel and act when the wave knocked down the tower? He started to cry. (4) | He took a deep breath. | He laughed.
- Nia responds: What did Nia do after the wave knocked down the tower? She took a deep breath and made a plan to build again. (5 or 6) | She started to cry. | She went home.

## Interactions in detail
- Every tap acts at once; a tap on Roll while the cube tumbles lands it at once. A tap cuts any line at once; `whole` only means the next queued line waits for it. The question can be replayed with `Hear it again`.
- The cube lands only on faces this book has not used; the last plain face lands for sure. Faces done show a check on the cube's net (a small unfolded cube under the score, code-drawn).
- Proof tries: 2 per answer. A steal has no proof step.
- `Pass` gives the turn away with no points (for a team that wants the other team's help).
- `Read the book` reads every sentence in order with its panel glowing (about 30 to 36 s; a tap on any panel or control stops it and acts). It is always available.
- `Books` returns to the shelf; the score and used faces of each book stay until `New game`.
- Motion off: no tumbling, flying or flipping; same timing.

## Look
- Accent `--brand` #a3195b deep magenta (header, question bubble edge, Roll); gold #ffd23f (gold cube, the proving glow, Roll fill); paper #fff7fb; ink #2a1320; muted #6b4a5a. Scene: a sunny classroom rug corner (painted) behind the cube; the book panels are cream cards.
- Teams: Sun in warm orange outline with a sun icon; Moon in deep blue outline with a moon icon (icons, not color alone).
- Contrast (WCAG 2.1, computed): white on brand 7.38:1; brand on paper 7.01:1; ink on paper 16.45:1; muted on paper 7.25:1; ink on gold 11.99:1.
- Different from this batch (teal, olive, red, violet) and batch 1.

## Art
Local FLUX (`scripts/localart.py`); no people (Nia and Eli are drawn as young raccoons, so the story has no people art).
- rug-corner: "A sunny classroom reading rug with pillows and a low bookshelf, warm gouache, the center of the rug clear"; 16:9; cutout no; the backdrop.
- cover-otters: "A sea otter floating on its back in kelp holding a shell, warm gouache picture book cover, a blank band at the top for a title"; 3:4; cutout no. cover-nia: "Two young raccoons, a big sister and a little brother, building a sandcastle at the beach, warm gouache picture book cover, a blank band at the top"; 3:4; cutout no.
- otter-1 to otter-7: one painting per sentence ("Sea otters near a rocky shore"; "Sea otters floating on their backs in a kelp bed"; "A sea otter asleep, wrapped in kelp, at night under stars"; "A sea otter diving to the sea floor among crabs, clams and sea urchins"; "A sea otter on its back cracking a shell on a rock on its belly"; "A close view of a sea otter's thick brown fur in cold water"; "A mother sea otter floating with her pup on her belly"); 4:3; cutout no.
- nia-1 to nia-8: one per sentence (the raccoons building on a sunny Saturday morning; little brother patting sand; a big wave knocking the tower down; little brother crying; big sister taking a deep breath; big sister pointing up the beach, talking; both carrying wet sand in a red bucket; the dry castle up the beach with a shell on top); 4:3; cutout no.
- card art (36): small paintings for each answer card (a crab, a rock, a starry night sky for "at night", a red bucket, and so on), 4:3, cutout no; the builder lists all from Content. Cards use their own small paintings, not crops of the sentence panels.
About 55 images, no people. Drawn in code: the cube and its icons, the cube net, the score, sun and moon icons, the question bubble, glows, every control.

## Voice
Bank voice `lively-host` (style "Say with lively energy, like a friendly game show host"): the host of the cube game. Not used by K-2 ELA neighbors or batch 1. `Curio.voice` with `scope: () => state.book + ':' + state.face + ':' + state.step`, `welcomeAfter: true`.
- event `open`: "{Sea Otters}! Great pick."
- how `welcome`: "Welcome to Question Cube! First we hear the book. Then roll the cube, answer the question, and prove it in the book."
- event, whole, `sentence` (Read the book and panel taps): the sentence.
- how `rollHow`: "Team {Sun}, tap Roll!"
- event, whole, `question`: "{Who}! {question}" then "Tap a card to hear it."
- event `card`: the card's words.
- event `rightAnswer`: "Yes! One point for Team {Sun}. Now prove it! Tap the sentence that tells."
- event, whole, `proved`: "That sentence proves it! Another point!" event `notProof`: "That sentence doesn't tell {it}. Try another." event `shownProof`: "Here's the sentence that tells: {sentence}."
- event `wrongAnswer`: "{A rock} is a {what}, not a {where}. Team {Moon}, can you steal it?" (per question word: who is a person or animal; what is a thing; where is a place; when is a time; why is a reason; how is a way of doing it)
- event `steal` / `noSteal`: "Stolen! One point for Team {Moon}." / "Not this time."
- event `turn`: "Team {Moon}'s turn. Tap Roll!"
- event `gold`: "All six faces done! The cube turns gold."
- event, whole, `topicAsk` / `detailsAsk`: "What is this book mostly about?" / "Tell two details about sea otters. Then tap the two sentences."
- event, whole, `sayIt`: "This book is mostly about sea otters. It tells that {detail} and {detail}."
- event, whole, `youAsk`: "Your team asks a question! Pick a question word, then ask Team {Moon} about the book."
- event, whole, `final`: "Game over! Team Sun has {n}, Team Moon has {m}. You both found the answers in the book!"
Read speaks the hint, which always names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Answer card | Guess; pick any card that is in the book; the biggest or first card; elimination | All three cards are in the book (or a plausible reason or response), so "it's in the book" never picks; only the question word does (who, what, where, when, why, how kinds differ); one size, shuffled; a wrong card goes to the other team as a steal, so guessing gives points away; chance 1 in 3. |
| Proof | Guess; tap every panel; match the card picture to a panel picture | 1 in 7 or 1 in 8, two tries; card pictures are their own paintings, not panel crops; tapping panels reads them, which is the real way to find proof. Answer and proof by chance: 1 in 21 and 1 in 24 (computed); expected guessing points per turn 0.38 against 2 for a right, proved answer. |
| Who helped Nia | the name heard most | Eli is in sentences 2, 4 and 8 (computed); only sentence 2 says he helped. |
| Why (Nia) | the picture with the shell on top | "Eli put a shell on top" is in the same sentence and is the common wrong answer; it is not why the castle stood. |
| Responses (RL.2.3) | Pick the response heard in the story | Each set includes the other character's real response (Eli cried, Nia took a breath); only matching the character to the response passes. |
| Mostly about | Guess; the word heard most | 1 in 3; kelp is in two sentences and rocks in one, sea otters is the topic of all seven. The two-details point needs two lit sentences: any two count by design (all are key details). |
| You ask | Award each other points | Judged by the class; both points need a lit proving sentence for the answer. Low stakes by design. |
| Doing nothing / Pass | Wait out the turn | No points are earned without an answer; Pass gives the turn away. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a book: `open`, then `welcome` (queued), then Read the book: `sentence` 1 to n (whole each), then `rollHow`.
2. Roll: `question` (whole). Card taps: `card`. Pick: `rightAnswer` or `wrongAnswer`; the prove step's hint follows `rightAnswer`. Proof: the sentence, then `proved` or `notProof`; after two misses `shownProof` (whole). A steal: `steal`/`noSteal`, then `shownProof`. Then `turn`.
3. Gold: `gold`, then gold-face lines (`topicAsk`, `detailsAsk`, `sayIt`, `youAsk`) as reached; feedback for each answer plays before the next ask.
4. End: `final` (whole).
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.K.1, RI.1.1, RI.1.2, RI.1.3, RI.2.1, RL.2.1, RL.2.3 wording (ask and answer questions about key details; who, what, where, when, why and how; main topic and key details; connection between two pieces of information; how characters respond to major events and challenges) | Common Core State Standards, ELA, RI and RL pages for K, 1 and 2, thecorestandards.org | CCSS ELA 2010 PDF, Reading Standards K-5 | yes |
| Sea otters live in coastal ocean waters near shore | NOAA Fisheries, "Sea otter" species page | Monterey Bay Aquarium, "Sea otter" animal page | yes |
| Sea otters rest floating on their backs, often in kelp, and wrap in kelp to keep from drifting while they sleep | Monterey Bay Aquarium, "Sea otter" | National Wildlife Federation, "Sea otter" | yes |
| Sea otters dive to the sea floor for prey such as crabs, clams and sea urchins | NOAA Fisheries, "Sea otter" | U.S. Fish and Wildlife Service, "Southern sea otter" | yes |
| Sea otters use rocks as tools to crack open shells | Monterey Bay Aquarium, "Sea otter" | National Geographic Kids or National Wildlife Federation, "Sea otter" | yes |
| Sea otters have very thick fur that keeps them warm (they have no blubber) | NOAA Fisheries, "Sea otter" | Monterey Bay Aquarium, "Sea otter" | yes |
| A mother sea otter carries her pup on her belly | U.S. Fish and Wildlife Service, "Southern sea otter" | National Wildlife Federation, "Sea otter" | yes |
Backed twice: 7. Cut: 0. Nia's Sandcastle is our own story.

Checks run (Python, scratchpad b2/cube.py, 2026-11-08): each right answer's key words appear in exactly one sentence, its proof (Eli appears in 2, 4 and 8; only 2 says he helped, so Who is checked against sentence 2); text lengths 91 and 76 words, read times about 36 s and 30 s at 2.5 words a second; answer plus proof by chance 1 in 21 and 1 in 24; expected guessing points per turn 0.381 and 0.375; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the cube, the question, the three cards and the whole book strip show with no scroll; at 680x425 the cube, cards and four panels show, with arrows for the rest.
2. Every plain face, in both books, takes only its right card; wrong cards play the question-word line and offer a steal. (RI.K.1, RI.1.1, RI.2.1, RL.2.1)
3. Every proof accepts only its sentence (Nia responds accepts 5 or 6), two tries, then the sentence is shown.
4. Gold faces: Mostly about takes sea otters and two lit sentences; Connect takes only the kelp answer and sentence 3. (RI.1.2, RI.1.3)
5. Eli responds and Nia responds each take only that character's response. (RL.2.3)
6. You ask: the asking team picks a question word; points need a lit sentence and a Good answer tap. (RI.K.1, RI.1.1, RI.2.1)
7. The cube lands only on unused faces, and the score adds up by the rules (answer 1, proof 1, steal 1).
8. Tap while it plays: a tap on Roll during a tumble lands it at once; any card or panel tap during a line acts at once; no older line plays after a newer one.
9. Pre-reader: every question, card and sentence is spoken; every card is a picture.
10. Motion off: no tumbling or flying, same timing; no network requests; nothing saved.

## Open questions
- None for Cory.
