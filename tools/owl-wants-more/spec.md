# Owl Wants More

## One idea
Three young animal writers bring Otis the owl stories so thin they are only pencil sketches, and every question Otis asks (What color? Where? How did you feel?) is answered by a detail card that paints that part of the picture and adds those words to the story, so the class sees and hears a story grow from plain to full; then they polish the capitals and end marks, and Otis reads it aloud exactly as written, running out of breath where a period is missing.

## Not like
- class-phone-call (k-2, spec): the class asks a caller question words to gather news. Here a reader asks the class's writer questions, and the skill is answering with the detail that fits the question and the topic.
- little-book-press (k-2, spec): a child makes a whole book from blank pages. Here a short draft already exists and is revised: details added, then edited.
- show-and-tell-spotlight (k-2, concept): spoken details about an object. Here written details in a story.
- big-book-pointer (k, spec): Dot reads only where the class sends her. Here Otis reads a whole draft, and what changes his reading is punctuation.
- sentence-train (k, concept): builds one sentence with a capital engine and end caboose. Here capitals and end marks are fixed inside a finished story, and the result is heard.
- shakespeare-remix, personal-essay-studio, editors-in-the-margin (9-12, same format): revision studios for older writers. Here K-2 revision with pictures, one question at a time.

## Who and how
- Grades K-2, ELA, module "Adding Details and Fixing Sentences" (Writing). Standards: W.K.5, W.1.5, W.2.5, RF.1.1 (RF.1.1a).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class answers out loud and a helper taps. Every question, card and next step is spoken and every card is a picture, so a child alone can play (BASELINE rule 4).
- Modes: `Stories` (three built stories, each: Details, Your question, Polish) and `My story` (the class's own draft, typed by the teacher). tool.json `modes: ["Stories", "My story"]`, `minutes: "15-25"` per story, `grades_label: "Grades K-2"`.
- Privacy: My story drafts are saved only on this device (localStorage, try/catch), and My story says "Your stories are saved only on this device." (BASELINE rule 7). Not a personal prompt; teacher notes say a class story about home or family is the class's choice and the teacher types only what the class agrees to share.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.K.5 | With the teacher's guidance, answer Otis's question by picking the detail card that answers it | the right card paints its part of the sketch and its words slide into the story | 2 |
| W.1.5 | Keep the focus on the topic (an off-topic card is turned away); answer a friend's question in Your question; in My story, a classmate asks and the teacher types the class's answer | Otis: "That's not about your kite"; the friend's question card and its new sentence | 2, 3, 7 |
| RF.1.1a | Polish: capitalize the first word of each sentence (and I), and give each sentence its end mark (period, question mark, exclamation mark) | the story in big type; tapped words change case; end-mark slots; Otis's reading pauses, rises or runs on | 4, 5 |
| W.2.5 | Revise (Details, Your question) then edit (Polish) the same draft, and in My story revise and edit the class's own draft | the before and after drafts side by side at the end; the class's draft with Otis's notes | 6, 7 |

## Screens and modes
Header (kit): title "Owl Wants More"; mode buttons `Stories` and `My story`; `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** Stories mode, the bookshelf of three thin stories (each a sketch cover with its writer: Juno the fox, Pim the rabbit, Tess the turtle). Otis sits on a branch at the top left. First hint: "Otis wants a story! Tap Juno's story." The first tap on a story opens it and plays `open` (its own line); the welcome is queued after it (`welcomeAfter: true`). The premise ("Otis asks questions; your answers make the story better") is in the first hint of each story and in Read.

### Stories: Details (W.K.5, W.1.5)
- Focus: the picture (center left, 640 x 420), which starts as a pencil sketch, and the story strip under it (the draft in 30 px type, the current sentence underlined).
- Otis (cutout, 180 px, top left of the panel) asks one question per sentence, in order. Under the strip, four detail cards (150 x 130, painted picture plus two or three words): one answers the question, two answer a different question, one is about something else. Tap a card to hear it; `Use it` (check icon) adds it.
- Right card: the part of the picture it names paints in from pencil to color (Motion off: it appears), the words slide into the sentence (new words shown in the accent color, underlined), Otis hoots, and the line is read with the new words. Wrong-question card: Otis "That tells {where}. I asked {what color}." Off-topic card: "That's not about {your kite}. Let's stay on {the kite}." The card dims; the question repeats.
- At 1366x768: picture, strip and cards above the fold (header 56, picture 420, strip 90, cards 140). At 680x425: picture 330 x 215, strip 16 px, cards 76 px in one row.

### Stories: Your question (W.1.5)
- After Otis's three questions: "Now you be the friend. What do you want to ask {Juno}?" Three question cards (picture plus words, spoken on tap). The class picks one; the writer answers with a new sentence, which is added before the story's last sentence, and its cutout appears in the picture. Any pick is right (it is the class's question); the other two stay tappable to hear, not to use. `Next: Polish` (sparkle icon, gold) moves on.

### Stories: Polish (RF.1.1a, W.2.5)
- Focus: the story, full width, 34 px type, wrapped in up to four lines, each word a 60 px tall target, and a slot after each word (a thin gap that grows to a 44 x 60 target when Polish is on).
- Tap a word: its first letter flips between capital and small (a short flip). Tap a slot: a mark picker opens beside it with four picture buttons, `Period` (dot), `Question mark`, `Exclamation mark`, `No mark` (each spoken). `Read it, Otis` (owl and speaker icon) has Otis read the draft as written (Interactions). `Check` (magnifier) counts what is left: "3 fixes left." After two Checks with fixes left, `Show me` appears and each unfixed spot pulses once.
- When everything matches: the story gets a gold frame, Otis reads it (whole), and the `Before and after` card shows the thin draft and the polished story side by side, both read on tap.

### My story (W.1.5, W.2.5)
- Focus: Otis's notebook (900 x 420): the class's draft in 28 px type. The teacher types (an on-screen keyboard is not needed; the device keyboard).
- `Otis asks` (owl icon): Otis asks the next question from his bank (What color? Where? When? How did you feel? What did it sound like? How big? How did it feel to touch?), naming no sentence; the class answers aloud and the teacher types. `Friend asks` (two-children icon): a card reads "A friend asks a question. Type the answer into the story." `Read it, Otis` reads with the browser's voice (the hint says "This is the computer's voice."). `Check` counts sentences whose first word is small and sentences with no end mark. `Save` and `My stories` (up to 6, on this device); `New story`.

## Content
Each story: the thin draft, three Otis questions with four cards each (right first here; shown shuffled), three friend questions with their answers, and the polish draft. Cards: words plus a painted picture.

**Juno's Kite** (Juno the fox). Thin: "I have a kite. It flew. It got stuck. Can you help me get it down?"
- What color is your kite? red ("I have a red kite.") | in the park (where) | whoosh (sound) | I like pizza (off topic).
- Where did it fly? over the hill ("It flew over the hill.") | yesterday (when) | soft (touch) | my cat is gray (off topic).
- How did you feel when it got stuck? sad ("It got stuck, and I felt sad.") | tall (size) | at night (when) | I have a bike (off topic).
- Friend questions: Who was with you? "My grandpa was with me." | Where did it get stuck? "It got stuck in a big oak tree." | What did the wind sound like? "The wind went whoosh."
- Polish draft: "i have a red kite. it flew over the hill It got stuck, and I felt sad. can you help me get it down" (fixes: I, It, Can; a period after hill; a question mark at the end).

**Pim's Rain Day** (Pim the rabbit). Thin: "We went outside. We jumped. It was fun. Do you like puddles?"
- When did you go outside? after the rain ("We went outside after the rain.") | green (color) | loud (sound) | I lost a tooth (off topic).
- Where did you jump? in a big puddle ("We jumped in a big puddle.") | in the morning (when) | happy (feeling) | my mom has a car (off topic).
- What did it sound like? Splash! ("Splash! It was fun.") | under a tree (where) | cold (touch) | I like trains (off topic).
- Friend questions: Who went with you? "My sister went with me." | What did you wear? "I wore yellow boots." | What did you see? "We saw a worm."
- Polish draft: "we went outside after the rain We jumped in a big puddle. splash! it was fun. Do you like puddles" (fixes: We, Splash, It; a period after rain; a question mark at the end).

**Tess and the Puppy** (Tess the turtle). Thin: "I saw a puppy. It barked. I petted it. Can I keep it?"
- How big was it? tiny ("I saw a tiny puppy.") | on Sunday (when) | yip, yip (sound) | I have a hat (off topic).
- What did its bark sound like? yip, yip ("It barked, yip, yip!") | brown (color) | at the store (where) | the sun is hot (off topic).
- How did its fur feel? soft ("I petted it. Its fur felt soft.") | after school (when) | excited (feeling) | I can swim (off topic).
- Friend questions: Where were you? "We were at the park." | What was its name? "Its name was Biscuit." | Who was with you? "My dad was with me."
- Polish draft: "I saw a tiny puppy it barked, yip, yip! i petted it. its fur felt soft. Can I keep it" (fixes: It, I, Its; a period after puppy; a question mark at the end).

The friend's sentence is added, already correct, before the last sentence of the polish draft. Each polish draft has five fixes: three capitals and two end marks.

Picture changes: Juno: kite gray to red; the hill paints in; Juno's sad pose; friend: grandpa fox, the oak paints in, wind swirls (code lines). Pim: the sky clears and the rain clouds go; the puddle paints in; a splash cutout; friend: sister rabbit, yellow boots, a worm. Tess: a tiny puppy paints in; a "yip yip" burst (code, words in code); the puppy's fur paints soft; friend: park background paints in, a name tag (word in code), dad turtle.

## Interactions in detail
- Taps act at once; a new tap cuts a reading line. A story can be left any time; its state stays until `Start over` (in the story's panel) or page reload. Stories can be done in any order.
- Details: cards can be heard any number of times; only `Use it` checks. A used question cannot be undone (the picture keeps its color).
- Polish reading rules (Otis reads the current draft, sentence by sentence, from recorded clips): each sentence has three recorded readings (as a statement, a question, an exclamation). A sentence followed by a period plays its statement reading, then a 600 ms pause; a question mark plays the question reading; an exclamation mark the exclamation reading. No mark: Otis runs straight on into the next sentence with no pause, and at the end of the story gasps "Whew! I ran out of breath!" (`breath`). Capitals do not change the sound; a sentence that starts with a small letter makes Otis frown at that word for 1 s as he reads it (no line). A capital in the middle of a sentence (other than I and names) makes him tilt his head at it.
- Check: counts every difference from the polished story: missing or extra capitals and missing, extra or wrong marks. `Show me` appears only after two Checks with fixes left.
- My story: Check finds a sentence start that is a small letter (after a period, question mark or exclamation mark, and the first word) and a draft or paragraph that ends without a mark; it cannot judge details. Otis's question bank cycles, never repeating until all seven are used. Up to 6 saved stories, 600 characters each (the 601st is not taken; the hint says "This story is full.").
- Motion off: no painting in, flips or slides; new states appear at once on the same timing.

## Look
- Accent `--brand` #17666e twilight teal (header, Use it, new words); gold #f2c14e (Next, the gold frame); paper #f7f4ec; ink #1d2a2c; muted #4f5f61. Scenes: pencil gray on cream paper turning to warm watercolor as details land; Otis's branch at dusk.
- Contrast (WCAG 2.1, computed): white on brand 6.64:1; brand on paper 6.04:1; ink on paper 13.46:1; muted on paper 6.08:1; ink on gold 8.81:1.
- Never color alone: new words are underlined as well as teal; dimmed cards get a small x icon.
- Different from this batch (magenta, olive, red, violet) and batch 1 (plum, brick, pine, blue, amber).

## Art
Local FLUX (`scripts/localart.py`); no people. Each story has a pencil sketch and a painted version of the same scene, cut so a part can paint in alone (the builder masks the painted layer per part).
- otis-sit, otis-ask, otis-hoot, otis-read, otis-frown, otis-tilt: "A round friendly barn owl with big eyes <sitting on a branch / leaning forward asking / hooting happily / holding a book reading / frowning / tilting its head>, watercolor picture book style, plain white background"; 1:1; cutout yes; people no.
- juno-sketch, juno-color: "A young fox flying a kite on a grassy hill beside a big oak tree, <pencil sketch on cream paper / soft watercolor>"; 3:2; cutout no; the base picture (Juno and kite are separate cutouts).
- juno-happy, juno-sad, grandpa-fox, kite-gray, kite-red: the fox and kite cutouts ("A young fox <smiling / looking sad>, watercolor, plain white background"; "An old fox with a walking stick ..."; "A diamond kite with a long tail, <pencil sketch / red watercolor> ..."); 3:4 (kites 1:1); cutout yes.
- pim-sketch, pim-color: "A sidewalk beside a garden after rain with a big puddle, <pencil sketch / watercolor, clearing sky>"; 3:2; cutout no.
- pim-rabbit, sister-rabbit, yellow-boots, splash, worm, rain-clouds: cutouts, watercolor, plain white background; 3:4 or 1:1; cutout yes.
- tess-sketch, tess-color: "A grassy park path with a bench and trees, <pencil sketch / watercolor>"; 3:2; cutout no.
- tess-turtle, dad-turtle, puppy-sketch, puppy-tiny, puppy-soft: cutouts ("A tiny fluffy puppy <pencil sketch / watercolor / curled up with soft fluffy fur>"); 1:1; cutout yes.
- shelf: "A wooden bookshelf on a tree branch with three blank book covers, watercolor at dusk"; 16:9; cutout no; the Stories shelf.
- notebook: "An open notebook with lined paper on a wooden desk, a feather quill beside it, watercolor"; 16:10; cutout no; My story.
- card-art (36): one small painted picture per detail card and friend question ("<red>, a red paint swatch", "<over the hill>, a green hill", "<pizza>, a slice of pizza" ...), 4:3, cutout no; the builder lists all 36 from Content.
About 70 images, no people. Drawn in code: the story strip, slots, mark picker, wind swirls, sound bursts, words on the name tag, Check counts, every control.

## Voice
Bank voice `knowing-guide` (style "Say in a knowledgeable, friendly way, like a museum curator") as Otis, a kind and curious owl; the writers' answers use the same voice, named on screen with their faces. Not used by the K-2 ELA neighbors or batch 1. `Curio.voice` with `scope: () => state.mode + ':' + state.story + ':' + state.step`, `welcomeAfter: true`.
- event `open`: "{Juno} wrote a story! But it's so short, it's only a sketch."
- how `welcome`: "I'm Otis. I love stories, and I always want more! Answer my questions, and the story will grow."
- event, whole, `ask` (per question): Otis's question from Content, then "Tap a card to hear it. Then tap Use it."
- event `card` (tap): the card's words. event, whole, `yes`: the new sentence. event `noQuestion`: "That tells {kind}. I asked {kind}." event `noTopic`: "That's not about {topic}. Let's stay on {topic}."
- how `friendHow`: "Now you be the friend. What do you want to ask {Juno}? Tap a question."
- event, whole, `friendAnswer`: the writer's answer sentence.
- how `polishHow`: "Let's polish! Every sentence starts with a capital letter and ends with a mark. Tap a word to change its letter. Tap a space to add a mark."
- event `markName`: "Period." / "Question mark." / "Exclamation mark." / "No mark."
- event, whole, `reading`: the sentence clips (Interactions); event `breath`: "Whew! I ran out of breath!"
- event `left`: "{n} fixes left." (once per Check). event `showMe`: "Look for the spots that blink."
- event, whole, `polished`: "Beautiful! Now I can read every sentence." then the whole story.
- how `myHow`: "Type your class story in my notebook. Then tap Otis asks."
- event `otisAsks` (My story): the bank question. event `friendAsks`: "A friend asks a question. Type the answer into the story."
- event `myLeft`: "{n} sentences need a capital or a mark." / "Every sentence starts and ends right!"
Read speaks the hint, which names the current action and control, never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Detail card (W.K.5) | Guess; the biggest or first card; the most colorful card; elimination over a story | 1 right of 4 shuffled, one size; all three by chance 1 in 64 (computed); each question has its own four cards, so cards do not shrink across a story; a wrong card dims and the question repeats, so mashing just hears Otis say why. |
| On topic (W.1.5) | Pick any detail | Every question has an off-topic card that also sounds like a detail ("my cat is gray" answers a color question too); Otis turns it away by topic, not by question kind. |
| Your question | none needed | Any of the three is right (it is the class's question); not scored. |
| Polish Check (RF.1.1a) | Capitalize every word; put a period everywhere; tap until Check passes; Show me | Check counts extra capitals and marks too: capitalize-all adds 19, 15 and 14 wrong capitals; period-everywhere adds 20, 15 and 15 wrong marks (computed). Each mark slot has four choices and the right mark differs (period, question, exclamation in Pim's and Tess's). Show me waits for two Checks, and Otis reads every attempt aloud, so a wrong mark is heard (a flat question, a run-on). |
| My story Check | Put a mark after every word | Every word after a mark would then need a capital, and Check counts each small sentence start; it cannot judge details, and the tool says only what it checks. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a story: `open`, then `welcome` (first story only, queued), then `ask` (whole) for question 1. Next action is spoken in `ask`.
2. Details: card taps play `card`; Use it plays `yes` (whole) or `noQuestion`/`noTopic`. The next `ask` waits for `yes`.
3. Your question: `friendHow` (first), question taps read the question, a pick plays `friendAnswer` (whole); then the hint names Next: Polish.
4. Polish: `polishHow` (first), `markName` on picker taps, Read it plays `reading` (whole) and `breath` if earned; Check plays `left` or `polished` (whole).
5. My story: `myHow` (first), `otisAsks`, `friendAsks`, `myLeft`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.K.5, W.1.5, W.2.5 wording (respond to questions and suggestions from peers, add details, focus on a topic; strengthen writing by revising and editing, with guidance and support) | Common Core State Standards, Writing K, 1 and 2 pages, thecorestandards.org | CCSS ELA 2010 PDF, Writing Standards K-5 (production and distribution of writing) | yes |
| RF.1.1a wording (recognize the distinguishing features of a sentence: first word, capitalization, ending punctuation) | thecorestandards.org, Reading: Foundational Skills, grade 1 | CCSS ELA 2010 PDF, Reading Standards: Foundational Skills K-5 | yes |
| A sentence begins with a capital letter and ends with a period, question mark or exclamation point; the pronoun I is always capitalized | Merriam-Webster, "Capitalization" and punctuation guides | Purdue OWL, "Capital letters" and "End punctuation" | yes |
Backed twice: 3. Cut: 0. The stories, writers and Otis are our own.

Checks run (Python, scratchpad b2/owl.py, 2026-11-08): each polish draft has exactly five fixes (three capitals, two marks) and word lists that align with the polished story; capitalize-all and period-everywhere error counts as in the table; detail chance 1 in 64; contrast as in Look (b2/c.py).

## Done when
1. Focus and fold: at 1366x768 the picture, the story strip and the four cards show with no scroll; Polish fits the whole story above the fold; at 680x425 the focus and the next control show with 16 px or larger story text.
2. Details: each of the nine questions takes only its right card, which paints its part and adds its words; wrong-question and off-topic cards get their own lines. (W.K.5, W.1.5)
3. Your question: each friend question adds its sentence and cutout before the last sentence. (W.1.5)
4. Polish: Check counts every remaining difference, including extra capitals and marks; Show me appears only after two Checks with fixes left. (RF.1.1a)
5. Otis's reading follows the marks: pause at a period, rising at a question mark, run-on and `breath` where a mark is missing.
6. Before and after shows the thin and polished drafts of each story, both read on tap. (W.2.5)
7. My story: type, Otis asks (seven questions, no repeats until all used), Friend asks, Check, Save; reload restores saved stories; the privacy line shows. (W.1.5, W.2.5)
8. Tap while it plays: a card, word or mode tap during a line acts at once; no older line plays after a newer one.
9. Pre-reader: every card, question and next action is spoken; every choice is a picture.
10. Motion off: no painting in or flips, same pacing; no network requests.

## Open questions
- None for Cory.
