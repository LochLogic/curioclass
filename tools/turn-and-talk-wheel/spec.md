# Turn and Talk Wheel

## One idea
A spinning wheel picks a picture and a talk move, Kiki the parrot and Bo the bear cub act out a tiny conversation that keeps or breaks that move (Bo talks over Kiki, wanders off topic, or Kiki mumbles), the class judges it, and then the class holds its own three-exchange talk with Kiki about the same picture, with a turn light that shows whose turn it is.

## Not like
- class-phone-call (k-2, spec): the class asks question words to fill gaps in a caller's news. Here the skill is the conversation itself: turns, topic, keeping it going, asking again, voice.
- show-and-tell-spotlight (k-2, spec): one speaker, one audience, detail stars. Here a back-and-forth between two talkers.
- question-cube (k-2, spec): answering questions about a text. Here a talk, with one quick key-detail check.
- big-book-pointer, rhyme-time-rumble (k, same format): print rules; sounds. Here speaking and listening.

## Who and how
- Kindergarten, ELA, module "Talk It Over" (Speaking and Listening). Standards: SL.K.1 (a, b), SL.K.2, SL.K.6.
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class judges by thumbs and talks with Kiki out loud; a helper taps. Every line, question and choice is spoken and every choice is a picture, so a child alone can play (BASELINE rule 4).
- tool.json `modes: []`, `minutes: "5-15"` (one spin is about 4 minutes), `grades_label: "Kindergarten"`.
- Privacy: the optional `Hear me` meter listens to loudness only; nothing is recorded or saved, and the meter says "Kiki only listens for how loud. Nothing is recorded." (BASELINE rule 7). Not a personal prompt; Kiki's questions are about the picture.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.K.1a | Judge whether Bo took turns or talked over Kiki; in Your turn, talk only when the turn light is on the class's side | the two-bubble judge cards; the turn light | 2, 5 |
| SL.K.1b | Your turn: three exchanges with Kiki (answer, answer her follow-up, then ask her a question); judge which reply keeps a talk going | three exchange bubbles that fill; Kiki's follow-up | 3, 5 |
| SL.K.2 | Did you catch it?: answer a key-detail question about what Kiki said; judge when to ask "Can you say that again?" or "What does it mean?" and hear the answer | three picture answers; Kiki's clear repeat or explanation | 3, 4 |
| SL.K.6 | Judge Kiki's whisper and shout against a just-right voice; in Your turn, the Hear me meter shows if Kiki can hear the class | three voice cards (a tiny mouth, a huge mouth, a just-right mouth); the meter and Kiki cupping her ear | 4, 6 |
| SL.K.1 (topic) | Judge whether Bo stayed on topic | on-topic and off-topic cards | 2 |

## Screens and modes
Header (kit): title "Turn and Talk Wheel"; `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The wheel (code-drawn, 420 px) with ten slices, each showing a painted picture and a talk-move icon, fills the left of the stage; Kiki perches on top. First hint: "Tap Spin to pick a picture and a talk move." The first tap on `Spin` (gold, wheel icon, 120 px) spins the wheel (2 s; Motion off: it ticks to its slice at once) with its own line (`spin`); the welcome is queued after it (`welcomeAfter: true`). The wheel lands on a slice not yet played (the last one for sure).

**A spin** has four steps, in order, shown as four step dots under the stage.
1. Watch. Focus: the talk stage (center, 800 x 420): Kiki (left) and Bo (right) on two stools, speech bubbles above them (drawn in code, words shown and spoken). The scene plays (lines in Content). `Watch again` (loop icon) replays it.
2. Judge. The move's question and two or three judge cards (200 x 160, picture plus words, spoken on tap). Right: a check, `judgeYes`, and the fix plays (Bo apologizes and waits, Kiki says it again clearly, Kiki explains the word, or Kiki tries a just-right voice). Wrong: `judgeNo` with the reason, the card dims, the question stays.
3. Did you catch it? A key-detail question about what Kiki said and three picture answers. Right: `catchYes`. Wrong: `catchNo` and Kiki's line replays (whole), the question stays.
4. Your turn. The turn light (a code lamp between Kiki and the class side, with a parrot icon or a children icon) shows whose turn it is. Exchange 1: Kiki asks (`ask1`); the light turns to the class; the class answers aloud; the helper taps `We answered` (speech bubble icon). Exchange 2: Kiki's follow-up (`ask2`); the class answers; `We answered`. Exchange 3: "Now you ask me a question!" Three question cards (picture plus words, spoken on tap); the class picks one; Kiki answers it (`kikiAnswer`). Each exchange fills one of three bubbles at the top. Then `talkDone` and the slice gets a star on the wheel.
- `Hear me` (ear and mic icon, off by default): during the class's turns, a loudness bar fills toward a picture of Kiki's ear; below a quiet level for 2 s Kiki cups her ear (`louder`, once per turn); above a loud level she covers her ears (`softer`, once per turn). The bar is a guide only (microphones differ).
- At 1366x768: header 56, the talk stage 420, the judge or answer cards 180, step dots 30: above the fold; the wheel shrinks to a 160 px badge at the top left after the spin. At 680x425: stage 460 x 230, cards 110 px.
- After all ten slices: `allStars` and `Spin again` clears the stars.

## Content
Each slice: picture | move | Watch scene (K = Kiki, B = Bo) | Judge question: right card / other cards | fix | key-detail question: right / others | Kiki's question | follow-up | three class questions with Kiki's answers.

1. **snowman | Take turns.** K: "I built a snowman! It has a carrot nose and a red hat." B (starting while K is still talking, bubbles overlap): "I built one too and mine is bigger and" K: "Bo, I wasn't done!" Judge "Did Bo take turns?": Bo talked over Kiki / Bo waited his turn. Fix: B: "Sorry, Kiki. You go first." K finishes: "It has a carrot nose and a red hat." Catch "What is the snowman's nose?": a carrot / a button / a stick. Ask "What would you put on a snowman?" Follow "Tell me more! Why that?" Class Q: "What color is your hat?" "It's red, like a strawberry!" / "Did your snowman melt?" "Not yet. It's still cold out!" / "Who helped you?" "My big brother helped me roll the snowballs."
2. **birthday cake | Take turns.** K: "My birthday cake had blue frosting." (B waits, a short pause) B: "Mine had strawberries! What did yours taste like?" K: "Vanilla!" Judge "Did Bo take turns?": Bo waited his turn / Bo talked over Kiki. Fix: none (B nods). Catch "What color was the frosting?": blue / red / green. Ask "What kind of cake do you like?" Follow "Ooh! What does it taste like?" Class Q: "How old are you?" "I'm six in parrot years!" / "Did you get presents?" "I got a shiny bell." / "Who came to your party?" "All my bird friends came."
3. **puppy | Stay on topic.** K: "My puppy likes to chase balls." B: "I had cereal for breakfast." K: "Hmm. We were talking about my puppy." Judge "Did Bo stay on topic?": No, he talked about something else / Yes, he talked about the puppy. Fix: B: "Oops. Does your puppy bring the ball back?" K: "Every time!" Catch "What does the puppy chase?": balls / cats / cars. Ask "What can a puppy do?" Follow "What else can it do?" Class Q: "What's your puppy's name?" "Her name is Peaches." / "Is your puppy big?" "She's tiny, like a loaf of bread." / "Does your puppy sleep with you?" "She sleeps in a basket by my perch."
4. **rain boots | Stay on topic.** K: "I jump in puddles with my rain boots." B: "My boots are yellow. They keep my feet dry!" Judge "Did Bo stay on topic?": Yes, he talked about boots and rain / No, he talked about something else. Fix: none. Catch "What does Kiki jump in?": puddles / leaves / snow. Ask "What do you wear when it rains?" Follow "Where do you go in the rain?" Class Q: "What color are your boots?" "Green, like a frog!" / "Did you get wet?" "Just my tail feathers." / "Do you have an umbrella?" "Yes, a tiny one with dots."
5. **slide | Tell me more.** K: "I went down the big slide today." Judge "Which one keeps the talk going?": "Tell me more! Was it fast?" / "Okay." / "I'm hungry." Fix: B: "Tell me more! Was it fast?" K: "So fast! I flapped all the way down!" Catch "Where did Kiki go?": down the big slide / on the swings / in the sandbox. Ask "What do you like to play on at recess?" Follow "Tell me more! What do you do there?" Class Q: "Were you scared?" "A little, then I laughed!" / "Did you go again?" "Five more times!" / "Who went with you?" "Bo went down right after me."
6. **garden | Tell me more.** K: "We planted seeds in our garden." Judge "Which one keeps the talk going?": "What did you plant?" / "Hmm." / "I like trucks." Fix: B: "What did you plant?" K: "Sunflowers! They grow taller than me." Catch "What did they plant?": seeds / rocks / shoes. Ask "What would you grow in a garden?" Follow "What color is it?" Class Q: "Do you water them?" "Every morning, with a little can." / "When will they grow?" "In a few weeks, if it's sunny." / "Can you eat sunflowers?" "The seeds, yes! Birds love them."
7. **fire truck | Say it again.** K (muffled, as if her mouth is full): "Mmf fire truck mmf siren mmf." Judge "What should Bo do?": "Can you say that again, please?" / Nod and smile / Walk away. Fix: B: "Can you say that again, please?" K (clear): "The fire truck has a loud siren." Catch "What does the fire truck have?": a loud siren / wings / a sail. Ask "What does a fire truck do?" Follow "What sound does it make?" Class Q: "Is it red?" "Bright red, with a ladder on top." / "Where does it live?" "At the fire station." / "Who drives it?" "A firefighter drives it."
8. **moon | Say it again (what does it mean?).** K: "The moon has craters." Judge "Bo doesn't know craters. What should he say?": "What does craters mean?" / "Cool." / "The moon is a cookie." Fix: B: "What does craters mean?" K: "Craters are big round holes. Space rocks crashed into the moon and made them." Catch "What does the moon have?": craters / trees / lakes. Ask "When can you see the moon?" Follow "What shape was it?" Class Q: "Can people go to the moon?" "Yes! Astronauts have walked there." / "Is the moon hot?" "Hot in the sun and very cold in the dark." / "Why does the moon change shape?" "We see different parts of its sunny side."
9. **drum | Just-right voice.** K (a whisper): "I can play the drum." Judge "How was Kiki's voice?": Too quiet / Too loud / Just right. Fix: K (just right): "I can play the drum." Catch "What can Kiki play?": the drum / the piano / the flute. Ask "What sound would you like to make?" Follow "Show me with a just-right voice!" Class Q: "Is the drum loud?" "Boom! But I play softly too." / "Who taught you?" "My grandpa." / "Can I try?" "Sure! Tap it with me!"
10. **kite | Just-right voice.** K (a shout): "MY KITE FLEW SO HIGH!" Judge "How was Kiki's voice?": Too loud / Too quiet / Just right. Fix: K (just right): "My kite flew so high!" Catch "What did Kiki fly?": a kite / a plane / a balloon. Ask "Where would you fly a kite?" Follow "Tell me more! What color kite?" Class Q: "Did it get stuck?" "Only once, in a tree." / "Was it windy?" "Very windy!" / "What shape is it?" "A diamond with a long tail."

## Interactions in detail
- Every tap acts at once; a tap during a scene stops it (Watch again replays it). Steps go in order; the step dots can jump back to Watch.
- Judge and Catch: a wrong card dims and stays tappable to hear; the question stays until the right pick.
- Your turn is not checked: `We answered` moves on whenever the teacher taps it; if the class needs a moment, the light simply stays on their side. Kiki never speaks during the class's turn.
- Hear me: needs the microphone; refused, the button shows "Microphone off" and nothing else changes. `louder` and `softer` play at most once per class turn.
- The wheel never lands on a played slice until all ten have stars; then `Spin again` clears them.
- Motion off: no spinning, flapping or bubble pops; the same steps on the same timing.

## Look
- Accent `--brand` #1a5f8a cobalt (header, turn light frame, Spin edge); gold #f7c948 (Spin, stars); paper #f5fafd; ink #13232e; muted #4c5d68. Scene: a sunny classroom corner with two stools and a rug.
- Contrast (WCAG 2.1, computed): white on brand 6.89:1; brand on paper 6.55:1; ink on paper 15.28:1; muted on paper 6.50:1; ink on gold 10.25:1.
- Never color alone: the turn light shows a parrot or children icon; judged cards get check or x icons.
- Different from the K ELA neighbors and the other four in this batch (emerald, barn red, slate, brown).

## Art
Local FLUX (`scripts/localart.py`); no people.
- talk-corner: "A sunny classroom corner with two small wooden stools on a round rug, warm gouache, the middle clear"; 16:9; cutout no.
- kiki (6 poses): "A bright green parrot with a yellow chest, <perched happily / talking with a wing raised / mouth full and muffled / whispering behind a wing / shouting with beak wide / cupping a wing to her ear>, warm gouache, plain white background"; 1:1; cutout yes; on the left stool, all visible.
- bo (5 poses): "A small brown bear cub in overalls, <listening / talking excitedly / looking sorry / raising a paw to ask / nodding>, warm gouache, plain white background"; 3:4; cutout yes; on the right stool.
- slice pictures (10): snowman, birthday cake with blue frosting, puppy with a ball, yellow rain boots in a puddle, playground slide, garden with seed packets, red fire truck, the moon with craters, a drum, a diamond kite; "<object>, warm gouache, plain white background"; 1:1; cutout yes; on the wheel and as the talk-stage backdrop prop.
- judge pictures (8): two bears talking over each other; a bear waiting with a raised paw; a thought bubble with breakfast cereal; a thought bubble with the puppy; a bear walking away; a smiling nod; a tiny mouth; a huge open mouth (and a just-right smile); 4:3; cutout no.
- answer pictures (20): the catch answers not already drawn (a button, a stick, red and green cake swatches, cats, cars, leaves, snow, swings, a sandbox, rocks, shoes, wings, a sail, trees, lakes, a piano, a flute, a plane, a balloon); 1:1; cutout yes.
About 49 images, no people. Drawn in code: the wheel and move icons, speech bubbles, the turn light, exchange bubbles, step dots, the Hear me bar, every control.

## Voice
Bank voice `easy-coach` (style "Say in an easy-going, encouraging way, like a relaxed sports coach") as Kiki; Bo uses the same voice slightly faster (recorded as his own clips, named on screen with his face). Not used by K ELA neighbors or batch 1 or 2. Kiki's whisper, shout and muffled lines are recorded as such. `Curio.voice` with `scope: () => state.slice + ':' + state.step`, `welcomeAfter: true`.
- event `spin`: "Round and round! Where will it stop?"
- how `welcome`: "Hi! I'm Kiki. Let's practice talking together: taking turns, staying on topic, and using a just-right voice."
- event, whole, `landed`: "{Snowman}! And our talk move is {take turns}."
- event, whole, `scene`: the Watch lines in order.
- event, whole, `judgeAsk`: the judge question, then "Tap a card."
- event `card`: the card's words. event `judgeYes`: "Yes!" then the fix lines (whole). event `judgeNo`: per move: "Look again. Did Bo wait until I was done?" / "What were we talking about?" / "Does that help me tell more?" / "Bo couldn't hear me. What should he do?" / "Listen again to my voice."
- event, whole, `catchAsk`: the key-detail question. event `catchYes`: "You caught it!" event `catchNo`: "Listen again." then Kiki's line.
- how `yourTurnHow`: "Now it's our talk! When the light points to you, it's your turn."
- event, whole, `ask1`, `ask2`: Kiki's question and follow-up. event `askMe`: "Now you ask me a question! Tap one, then ask it out loud." event, whole, `kikiAnswer`: her answer.
- event `louder` / `softer`: "I can't hear you. A little louder?" / "Whoa, that's loud! Just right, please."
- event `talkDone`: "What a great talk! Three turns each." event `allStars`: "Every slice has a star! You're great talkers."
Read speaks the hint, which names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Judge | Guess; always pick the "bad" card; always the "good" one | Each move has one slice where it is broken and one where it is kept (take turns, stay on topic), or different right answers (too quiet, too loud), so a fixed habit gets half; Tell me more and Say it again have three cards with one right; a wrong card stays open with a reason. |
| Catch | Guess; the picture shown on the wheel | 1 in 3; the slice picture is never an answer card (the answers are parts or details: a carrot, puddles, a siren). |
| Your turn | Tap We answered without talking | Not scored; it is the class's talk, led by the teacher; the star is a record, not a win. |
| Hear me | Shout | Shouting gets Kiki's `softer`; the meter asks for just right, not loudest. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Spin: `spin`, `welcome` (queued, first spin), then `landed` (whole), then `scene` (whole).
2. Judge: `judgeAsk` (whole); card taps `card`; a pick `judgeYes` with the fix (whole) or `judgeNo`.
3. Catch: `catchAsk` (whole) waits for the fix; then `catchYes` or `catchNo`.
4. Your turn: `yourTurnHow` (first), `ask1` (whole), class turn, `ask2` (whole), class turn, `askMe`, card taps, `kikiAnswer` (whole), `talkDone`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.K.1a, SL.K.1b, SL.K.2, SL.K.6 wording (agreed-upon rules for discussions, listening and taking turns; continue a conversation through multiple exchanges; confirm understanding by asking and answering questions about key details and requesting clarification; speak audibly and express thoughts clearly) | thecorestandards.org, Speaking and Listening K | CCSS ELA 2010 PDF, Speaking and Listening Standards K-5 | yes |
| The moon's craters were made by impacts of space rocks (asteroids, meteoroids) | NASA Science, "Moon: Craters" | Lunar and Planetary Institute, "Lunar craters" | yes |
| Astronauts have walked on the moon (Apollo, 1969 to 1972) | NASA, "Apollo program" | Smithsonian National Air and Space Museum, "Apollo" | yes |
| The moon is very hot in sunlight and very cold in darkness | NASA Science, "Moon facts" | Lunar and Planetary Institute, "Moon temperatures" | yes |
| The moon's phases are the changing view of its sunlit half | NASA Science, "Moon phases" | National Weather Service / NOAA, "Moon phases" | yes |
| Sunflower seeds are eaten by birds and people | Cornell Lab of Ornithology, "Bird feeding: seeds" | University of Illinois Extension, "Sunflowers" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad b3, 2026-11-08): judge right answers per move (take turns: talked over, waited; topic: off, on; voice: too quiet, too loud), so a fixed card wins at most half of a move's slices; slice pictures never appear among catch answers; contrast as in Look (b3/c.py).

## Done when
1. Focus and fold: at 1366x768 the talk stage, the cards and the step dots show with no scroll; at 680x425 the stage and cards show.
2. Judge: all ten slices take only their right card, and each fix plays. (SL.K.1a, SL.K.1)
3. Catch: all ten take only their right picture; a wrong pick replays Kiki's line. (SL.K.2)
4. Say it again and the moon slice: the muffled line is unclear and the repeat clear; the meaning is explained. (SL.K.2)
5. Your turn: the turn light points to the class only during their turns; three exchange bubbles fill; Kiki answers each class question card. (SL.K.1a, SL.K.1b)
6. Voice slices and Hear me: the whisper, shout and just-right clips differ clearly; louder and softer play at most once per turn; a refused microphone leaves the rest working; the privacy line shows. (SL.K.6)
7. The wheel lands only on unplayed slices; stars mark played ones.
8. Tap while it plays: a card or step tap during a scene acts at once; no older line plays after a newer one.
9. Pre-reader: every line, question and choice is spoken; every choice is a picture.
10. Motion off: no spinning or pops, same pacing; no network requests; nothing saved.

## Open questions
- None for Cory.
