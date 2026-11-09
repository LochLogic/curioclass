# Who Said That?

## One idea
A story's lines float down one at a time as speech bubbles and caption boxes, and the class drops each on the character who said it or on the storyteller; then the story plays back with every line in the voice of whoever it was given to, so a mistake is heard at once (Bear's deep voice saying "I'll bring the cheese!"), and in the second story the class finds out the storyteller is one of the characters: Duck tells it herself, so the caption boxes belong to Duck.

## Not like
- question-cube (k-2, spec): question words about a read-aloud. Here who is speaking or telling at each line.
- read-along-shelf (k-2, spec): reading books with fading help. Here a story taken apart line by line and played back by speaker.
- story-stage (k, spec): acting a folktale's events with puppets. Here voices and the narrator, not events.
- word-zoo (1, concept, same format): sorting words into habitats. Here sorting lines to speakers.
- context-clue-hunt (1, spec): word meaning from context. Here the speaker from context.

## Who and how
- Grade 1, ELA, module "Who Is Telling the Story?" (Reading Literature). Standard: RL.1.6.
- Driver: teacher on a projector or a pair at one device (tool.json `driver: "either"`). Every line is read when it floats in and on tap; speakers have pictures, so a pre-reader can follow (BASELINE rule 4).
- Two stories and a quiz: `The Picnic Plan` (a storyteller outside the story), `My Rainy Day` (Duck tells it), and `Who's Telling Now?`. tool.json `modes: []`, `minutes: "10-15"`, `grades_label: "Grade 1"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.1.6 | Sort each line to the character who said it or to the storyteller, using the bubble or box, the words "I" and "my", and what each character does | speakers' spots with pictures; a storyteller's book spot; bubbles and boxes | 2, 3 |
| RL.1.6 | My Rainy Day: work out that the storyteller is Duck (she says "My name is Duck" and "I"), and move the caption boxes to Duck | the storyteller spot asks "Who is it?"; the boxes' "I" words glow | 4 |
| RL.1.6 | Who's Telling Now?: the story pauses at six points; tap who is telling or talking at that point | the paused page with speakers | 5 |

## Screens and modes
Header (kit): title "Who Said That?"; `Stories`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A storybook garden: the two story books on a stump and the quiz card. First hint: "Tap The Picnic Plan to start." The first tap opens the story with its line; the welcome is queued after it (`welcomeAfter: true`).

**Sort.** Focus: the speakers' row at the bottom (each a character picture on a little stage, 200 x 220; the storyteller is an open book with a quill), and the line area above: one line at a time floats down (a speech bubble for talk, a rectangular caption box for telling), 700 x 160, and is read in a plain voice (a neutral read, the same for every line, so voice does not give it away). Drag it (or tap it, then a speaker) onto a speaker. It sits on that speaker's pile with no right or wrong shown yet. `Hear it again` re-reads the floating line. Ten lines per story.

**Play it back.** When all lines are placed: `Play our story`. Each line is played in the voice of the speaker it was given to, with that speaker's picture bouncing (Motion off: a glow). A line given to the wrong speaker sounds wrong in their voice, and at the end the narrator asks "Did anything sound funny?" Then `Check`: lines on the right speaker get a check; others shake and return to the line area to sort again. Play it back again until all are right.

**Who is telling? (My Rainy Day).** The storyteller spot is a book with a question mark. After the first sort, the narrator asks "Who is telling this story?" with five picks (Duck, Frog, Bear, a storyteller outside the story, nobody). The words "I", "me" and "my" in the caption boxes glow. Right (Duck): the book spot turns into Duck holding the book, and the caption boxes move to Duck's pile; play it back in Duck's voice.

**Who's Telling Now?** Both stories, paused at six points on a page (a line highlighted); the class taps who is talking or telling at that point.

At 1366x768 the speakers' row and the line area fit above the fold. At 680x425 speakers are 120 x 130 and the line is 560 x 120.

## Content
Both stories are written for Curio Class.

**The Picnic Plan** (speaker: line; B = bubble, C = caption box):
1. Storyteller, C: One sunny morning, Bear packed a big picnic basket.
2. Bear, B: "Who wants to come to my picnic?"
3. Duck, B: "Me! I'll bring the lemonade."
4. Mouse, B: "Me too! I'll bring the cheese."
5. Storyteller, C: The three friends walked to the top of the hill.
6. Duck, B: "Oh no! I forgot the cups for my lemonade!"
7. Storyteller, C: Mouse opened his tiny backpack.
8. Mouse, B: "I have three cups, just in case."
9. Bear, B: "Mouse, you think of everything!"
10. Storyteller, C: And the three friends had the best picnic ever.
Speakers: Bear, Duck, Mouse, Storyteller.

**My Rainy Day** (told by Duck):
1. Duck (telling), C: My name is Duck, and I love the rain.
2. Duck (telling), C: One morning, I woke up and saw big gray clouds.
3. Frog, B: "Duck! Come splash in the pond with me!"
4. Duck, B: "I'm coming, Frog!"
5. Duck (telling), C: I waddled to the pond as fast as I could.
6. Bear, B: "Brr! It's too wet for me. I'm going home to my cave."
7. Duck, B: "More rain for us, then!"
8. Duck (telling), C: Frog and I splashed until the sun came out.
9. Frog, B: "That was the best rainy day!"
10. Duck (telling), C: And it was. I can't wait for the next one.
Speakers: Duck, Frog, Bear, Storyteller (the book). First sort: caption boxes on the book are accepted as "telling"; then Who is telling? moves them to Duck.

**Who's Telling Now?** (story, line: right | the others on stage): Picnic 1: Storyteller | Bear, Duck, Mouse. Picnic 6: Duck | Bear, Mouse, Storyteller. Picnic 9: Bear | Mouse, Duck, Storyteller. Rainy 2: Duck | Frog, Bear. Rainy 3: Frog | Duck, Bear. Rainy 6: Bear | Duck, Frog.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Lines float in the story's order; `Skip` sends one to the back. A placed line can be dragged to another speaker before Check.
- The float-in read is neutral (one plain voice, no character voice), so the speaker must be worked out from the words and the shape.
- Check shows right placements only after Play it back, so the class hears first. Wrong ones return; the second Play it back plays only the story with corrections.
- In My Rainy Day, caption boxes put on Duck before the question are accepted, and the narrator says "You spotted it: Duck is telling this story!"
- Nothing is scored; each story gets a star when every line is right.

## Look
- Accent `--brand` #2f6b3a storybook green (header, the book spot, frames); gold #f4c542 (stars, checks); each character has its own picture and stage shape (Bear a round stage, Duck a puddle, Mouse a cheese wedge, Frog a lily pad, Storyteller a book); paper #f6faf4; ink #14241a; muted #4f5f53. Scene: a garden with a story stump.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 6.06:1; ink on paper 15.34:1; muted on paper 6.43:1; ink on gold 9.96:1.
- Never color alone: bubbles and boxes differ in shape (round with a tail, rectangle); speakers differ by picture and stage shape.
- Different from this batch (rose, plum, airmail blue, savanna) and the grade 1 and K-2 neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people.
- garden (1): "A sunny storybook garden with a tree stump holding two books, soft gouache, no text"; 16:9; cutout no.
- characters (Bear, Duck, Mouse, Frog x stand, talk, bounce = 12): "A friendly <brown bear / white duck / small gray mouse with a backpack / green frog> <standing / talking with an open mouth / bouncing>, soft gouache, plain white background"; 1:1; cutout yes.
- duck with book (1): "A white duck holding an open storybook, soft gouache, plain white background"; 1:1; cutout yes.
- story pictures (6, for the pages in Who's Telling Now?): "<a picnic on a hill / a bear packing a basket / a mouse with three cups / a rainy pond with a duck and frog / a bear walking home in rain / a sunny pond>, soft gouache"; 4:3; cutout no.
About 20 images. Drawn in code: bubbles, boxes, stages, the book spot, checks, every control.

## Voice
Narrator and storyteller: bank voice `gentle-storyteller`; characters: Bear `friendly-dad`, Duck `big-sister`, Mouse `hero-coach`, Frog `lively-host`; the neutral float-in read: `gentle-storyteller` reading plainly (style override "Read plainly and evenly"). None of these is used by the rest of this batch. `Curio.voice` with `scope: () => state.story + ':' + state.line`, `welcomeAfter: true`.
- event `story`: "{The Picnic Plan}!"
- how `welcome`: "Welcome! In a story, someone is always talking or telling. Let's find out who said each line."
- how `sortHow`: "Listen to each line. Who said it? Drop it on them. The book is for the storyteller."
- event, whole, `float`: the line, read plainly.
- event `placed`: a soft pop (sound).
- event, whole, `playback`: each line in its given speaker's voice.
- event `funny`: "Did anything sound funny?"
- event `checkYes` / `checkSome`: "Every line is right!" / "Some lines went to the wrong speaker. Try those again."
- event, whole, `whoTells`: "Who is telling this story?" event `whoYes`: "Yes! Duck is telling her own story. Look: I, me, my." event `whoNo`: "Listen: My name is Duck. Who says my name is Duck?"
- event `spotted`: "You spotted it: Duck is telling this story!"
- event, whole, `nowAsk`: "Who is talking right now?" / "Who is telling right now?" event `nowYes` / `nowNo`: "Yes!" / "Is it a bubble or a box?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Put every bubble on one character and every box on the storyteller | In The Picnic Plan boxes all go to the storyteller (4 of 10 right), but bubbles split three ways; random bubbles: 6 bubbles over 3 speakers in 90 right-count arrangements of 729 (computed), and only one is all right. |
| Sort | Go by voice | The float-in read is the same plain voice for every line. |
| Who is telling? | Pick the storyteller | It's wrong for My Rainy Day; the I, me, my words glow as the clue. |
| Who's Telling Now? | Pick the speaker who talked last | Pauses are spread so the answer changes each time (computed: Storyteller 1, Duck 2, Bear 2, Frog 1). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a story: `story`, `welcome` (queued, first time), `sortHow`, then the first `float` (whole).
2. Each drop: `placed`, then the next `float` (whole) after a 1 s pause.
3. Play our story: `playback` (whole, line by line), `funny`, then Check: `checkYes` or `checkSome`.
4. My Rainy Day: `whoTells` (whole), `whoYes` or `whoNo`, or `spotted`.
5. Who's Telling Now?: `nowAsk` (whole), `nowYes` or `nowNo`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.1.6 wording (identify who is telling the story at various points in a text) | thecorestandards.org, RL Grade 1 | CCSS ELA 2010 PDF | yes |
| Narrator: the one who tells the story; a first-person narrator is a character who tells it with I | Merriam-Webster, "narrator" and "first person" | ReadWriteThink, "Point of view" (NCTE) | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad b5, 2026-11-08): Picnic bubbles by speaker (Bear 2, Duck 2, Mouse 2), the 6-bubble assignment count 3^6 = 729 with one all right; Who's Telling Now? answer counts; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the speakers' row and the floating line show with no scroll; at 680x425 the same, smaller.
2. Picnic Plan: all ten lines check right only on their speakers; Play it back uses each given speaker's voice. (RL.1.6)
3. A wrong placement is heard in the wrong voice on Play it back and returns on Check.
4. My Rainy Day: Who is telling? takes only Duck; the caption boxes move to Duck and play in her voice. (RL.1.6)
5. Who's Telling Now?: each of the six pauses takes only its speaker. (RL.1.6)
6. The float-in read is one plain voice for every line.
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Pre-reader: every line is read on float-in and on tap; speakers have pictures.
9. Motion off: lines appear instead of floating, speakers glow instead of bouncing; no network requests; nothing saved.

## Open questions
- None for Cory.
