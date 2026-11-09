# Class Phone Call

## One idea
Ranger Sam phones the class from Pine Hollow Park with news, but the line is crackly: a static burst eats one key word in each sentence, and Sam only answers the question the class actually asks, so the class learns to listen for what is missing and pick the question word that gets it (What? Where? Who? When? Why? How?), filling a phone message pad one answer at a time while the phone passes from table to table.

## Not like
- turn-and-talk-wheel (k, concept): a back-and-forth with a talk buddy about a picture. Here the class questions a caller about news it cannot see, and the question word is the skill.
- question-cube (k-2, concept): a cube rolls the question word and the class answers about a read-aloud. Here the class chooses the question word to ask, and the caller answers.
- show-and-tell-spotlight (k-2, concept): the class is the speaker. Here the class is the listener and asker.
- owl-wants-more (k-2, concept): an owl asks the class for details. Here it runs the other way: the class asks the caller.
- usage-panel (11, draft, same format): a dictionary panel roleplay. Different band and look; here the role is a class taking a phone call.

## Who and how
- Grades K-2, ELA, module "Listening and Asking Questions" (Speaking and Listening). Standards: SL.K.3, SL.1.1, SL.1.2, SL.1.3, SL.2.1, SL.2.2, SL.2.3.
- Driver: teacher on a projector (tool.json `driver: "teacher"`). The class sits in four table groups (Owls, Foxes, Bears, Deer); the group holding the phone says its question out loud, then a helper taps that question card. Every question, choice and next step is spoken and every choice is a picture, so a child alone can play (BASELINE rule 4: alone, the turn badge just passes).
- Six calls, each 6 to 10 minutes. Steps per call: Listen and ask; Tell me more; Quiz; Take a message (grade 2 tag). tool.json `modes: []` (one flow; calls picked from the phone list), `minutes: "10-30"`, `grades_label: "Grades K-2"`.
- Not a personal prompt. Nothing is stored except which calls were finished on this page load (not saved).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.K.3 | When static eats a word, ask the question that gets it (or tap Say that again, then ask); tap "What does ___ mean?" when Sam uses a new word | a static burst over a blank in the caption; Sam's answer fills a message pad slot; the meaning card | 2, 3 |
| SL.1.3, SL.2.3 | Ask the question word that matches the missing piece (gather information); ask what a word means (clarify); in Tell me more, ask the follow-up that deepens the topic | wrong question words get "I didn't say that part" and the crackly line again; the follow-up answer adds a picture to the pad | 2, 4 |
| SL.1.1a, SL.2.1a | Agreed rules: one group holds the phone at a time; listen; wait your turn. The phone passes after each question | the Rules card (three pictures); the turn badge with the group's animal | 5 |
| SL.1.1b, SL.2.1b | Tell me more: pick the follow-up that builds on Sam's last answer, not the off-topic one | the two follow-up cards; an off-topic pick gets "Let's stay on the kite" | 4 |
| SL.1.1c, SL.2.1c | Ask to clear up confusion: Say that again and What does ___ mean? | the replayed line; the meaning card | 3 |
| SL.1.2 | Quiz: answer Sam's questions about key details with the message pad hidden | three picture answers per question | 6 |
| SL.2.2 | Take a message: put four picture cards in the order things happened and recount the call out loud before the pad reads it back | the message pad's four slots, numbered 1 to 4 | 7 |

## Screens and modes
Header (kit): title "Class Phone Call"; `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), with an icon and a word.

Stage, drawn at real pixel size and re-laid per size:
- Left: the classroom phone (painted cutout of a big friendly desk speakerphone, 300 px) with a light that pulses while Sam talks, and above it the caption strip: the current sentence in large type (28 px), the eaten word shown as a jagged static blank (drawn in code) until it is answered.
- Right: the message pad (painted spiral notepad, 520 x 440 at 1366x768): the call's title, then slots. Each gap's slot shows only "?" and a pencil until answered, then Sam's answer picture and two or three words, and the question card's icon that got it. The pad never shows which question word a blank needs.
- Bottom: the question cards row, six cards 120 x 120: `Who` (a face), `What` (a box with a question mark), `Where` (a map pin), `When` (a clock), `Why` (a light bulb), `How` (a hand turning a gear). A seventh card, `What does it mean?` (a book with a question mark, gold), appears beside them after Sam says the call's new word, labeled with that word.
- Panel (right, 320 px): the hint (20 px), the turn badge (the group's animal, 80 px), `Say that again` (looping arrow and ear), step buttons, the phone list (`Calls`), footer.
- Focus: the caption strip and the question cards while the class asks; the pad while answers fill; the quiz pictures in Quiz. At 1366x768: header 56, phone and caption 300, cards row 140: all above the fold. At 680x425: phone 120, caption 16 px, pad 300 x 230, cards 64 px in one row, the meaning card replacing the last if needed.

**On load and first tap.** The phone rings (code ring tone, after the first tap; before it, the phone shows a ringing picture and the hint). First hint: "The phone is ringing! Tap Answer." The first tap on `Answer` (green phone icon, 120 px, on the phone) starts call 1 (its own line), and the welcome (the rules) is queued after Sam's first sentence (`welcomeAfter: true`). The Rules card (Listen: ear; One at a time: one finger; Wait your turn: raised hand) shows beside the pad for call 1 and is reachable from the panel (`Rules`, three-picture icon) later.

**Listen and ask.** Sam says the call's sentences in order (Content). A sentence with a gap plays with a static burst over the eaten word and stops; the caption shows the static blank; `askHow` (first time) or the hint names the cards. The group says its question; the helper taps a card:
- Right card: Sam repeats the question word and answers ("Where? In the tallest pine tree!"); the blank fills; the pad slot fills; the phone passes to the next group; Sam goes on to the next sentence.
- Wrong card: Sam: "{Word}? I didn't say that part yet. The crackly part was:" and the gap sentence plays again with the static. The phone passes. After two wrong cards on one gap, the right card wiggles once (a hint, no words), and the next tap is judged again.
- `Say that again`: the last sentence plays again, static included; then (first time per call) `againTip`: "The phone is still crackly. Ask me a question about the part you missed!"
- `What does it mean?`: Sam explains the call's new word (Content); the card stays for the rest of the call.
- A sentence with no gap just plays; the next follows after it.

**Tell me more** (after the last gap): two follow-up cards, each a picture plus a few words, spoken when tapped once and asked when tapped again (first tap = hear it; second tap or `Ask it` = ask): one builds on Sam's news, one is off topic (Content). On topic: Sam answers and the pad gets one more picture. Off topic: `offTopic` ("Ha! Let's stay on the {topic}."), and the card fades; the on-topic card stays.

**Quiz** (after Tell me more): the pad slides away (hidden, so answers are not on screen). Sam asks two questions; each shows three picture answers (shuffled each time), spoken when tapped once, chosen on `This one` or a second tap. Right: check, `quizYes`. Wrong: `quizNo`, the class may try again (the wrong picture fades). After the second question, the pad comes back with every slot filled.

**Take a message** (grade 2 tag "2"; after Quiz; optional, `Skip` beside it): four picture cards of what happened, shuffled under the pad, and four numbered slots on the pad. The class recounts out loud, then taps the cards in order into slots 1 to 4. `Read the message` (pad and pencil icon) reads it back as one message; out-of-order cards get a "look again" ring and stay movable, and the message is read only when all four are in order (`msgYes`). Grades K and 1 can skip it.

**End of a call.** `callDone`, a check on that call in the phone list, and `Next call` (gold). The phone list lets the teacher open any call at any time.

## Content
Every call: Ranger Sam at Pine Hollow Park. Sentences in order; [gap] marks the eaten word with its card and Sam's answer.

**Call 1, The Runaway Kite.**
1. "Hello, class! This is Ranger Sam at Pine Hollow Park. Something blew away this morning. It was a [gap]!" What: "What? A kite! A red kite with a long tail."
2. "A girl named Mia was flying it by the pond. Then the wind pulled it right out of her hands."
3. "Now it's stuck way up [gap]." Where: "Where? In the tallest pine tree in the park!"
4. "But don't worry. [gap] came to help." Who: "Who? The fire crew, with their tall ladder!"
New word: crew: "A crew is a team of people who work together."
Tell me more: on topic "Did Mia get her kite back?": "She did! It has a little rip, but it still flies." Off topic "What's your favorite color?"
Quiz: "What blew away?" kite (right), hat, balloon. "Where did it get stuck?" pine tree (right), roof, pond.
Message order: kite flying by the pond; wind pulls it away; kite stuck in the tree; fire crew with a ladder.

**Call 2, The New Baby Goat.**
1. "Hello, class! Ranger Sam here. We have big news at the park farm. A baby goat was born [gap]!" When: "When? Last night, just before midnight!"
2. "A baby goat is called a kid. Her mother's name is Clover."
3. "The kid is tiny, and she can already [gap]." What: "What can she do? She can stand up and walk!"
4. "She needs a name. We will choose it [gap]." How: "How? The children who visit will vote!"
New word: kid: "A kid is a baby goat. People call children kids too!"
Tell me more: "What does the baby goat look like?": "She's white, with one brown ear." Off topic: "Do you have a big red bike at home?"
Quiz: "When was she born?" at night, a moon (right), in the morning, a sun, at lunch, a sandwich. "How will they choose her name?" a vote (right), names in a hat, Sam picks.
Message order: Clover the goat in the barn; the baby goat born at night; the kid stands and walks; children vote on a name.

**Call 3, The Turtle Crossing.**
1. "Hello, class! It's Ranger Sam. I had to stop my truck today. A [gap] was crossing the road!" What: "What? A turtle! A little box turtle."
2. "It was walking very slowly toward the pond, its habitat."
3. "I stopped my truck [gap]." Why: "Why? Because cars could hurt it, and turtles move slowly."
4. "Then I helped it across the road, [gap]." How: "How? I carried it gently, the same way it was going. If you see a turtle on a road, tell a grown-up."
New word: habitat: "A habitat is the place where an animal lives and finds its food."
Tell me more: "Was the turtle big or small?": "Small! About as big as my hand." Off topic: "Can I have a snack?"
Quiz: "Why did Ranger Sam stop?" cars could hurt the turtle (right), Sam was sleepy, to eat lunch. "Which way did Sam carry it?" the way it was going (right), back where it came from, into the truck.
Message order: a turtle on the road; Sam stops the truck; Sam carries it gently; the turtle reaches the pond.

**Call 4, The Big Storm.**
1. "Hello, class! Ranger Sam calling. Last night we had a big storm with lots of [gap]." What: "What? Wind! Very strong wind, and rain."
2. "The wind knocked a big tree down [gap]." Where: "Where? Right across the Blue Trail!"
3. "So the Blue Trail is closed. It will open again [gap]." When: "When? On Saturday, after we cut the tree away."
New word: trail: "A trail is a path through the woods."
Tell me more: "Was anyone hurt?": "Nobody was hurt. Everyone stayed safe inside." Off topic: "I like pizza with lots of cheese!"
Quiz: "What knocked the tree down?" wind (right), a bear, a truck. "When will the trail open?" Saturday (right), tonight, next year.
Message order: a storm with wind and rain; a tree falls on the trail; the trail is closed; workers cut the tree away.

**Call 5, The Owl Nest.**
1. "Hello, class! Ranger Sam here. High up in a hollow tree, I found a nest of baby [gap]!" What: "What? Owls! Baby owls."
2. "Baby owls are called owlets. There are three of them."
3. "We put up a rope so people stay back, [gap]." Why: "Why? So the owl family can rest. Many owls sleep in the day and hunt at night."
4. "You can still see them, [gap]." How: "How? With binoculars, from the bench by the sign!"
New word: owlets: "Owlets are baby owls."
Tell me more: "What do the owlets look like?": "Fluffy and gray, like little cotton balls with big eyes." Off topic: "Is it my birthday?"
Quiz: "How many owlets are there?" three owlets (right), one, five. "Why is there a rope?" so the owls can rest (right), for a race, to fly kites.
Message order: Sam finds a hollow tree; three owlets in the nest; a rope keeps people back; people watch with binoculars.

**Call 6, Tracks in the Snow.**
1. "Hello, class! It's Ranger Sam. This morning there was new snow, and I found tracks [gap]." Where: "Where? All around the picnic tables!"
2. "Each track had four toes. They went in a line, one in front of the other."
3. "Then I saw who made them. It was a [gap]!" Who: "Who? A red fox, looking for food."
4. "The fox was out [gap]." When: "When? Very early, before the sun came up."
New word: tracks: "Tracks are the marks feet leave in snow or mud."
Tell me more: "Did the fox find food?": "It sniffed under the bird feeder, hunting for mice. Then it ran into the woods." Off topic: "My shoes are new!"
Quiz: "Who made the tracks?" a fox (right), a deer, a duck. "Where were the tracks?" by the picnic tables (right), on the roof, in the pond.
Message order: new snow at the park; tracks by the picnic tables; a red fox early in the morning; the fox runs into the woods.

Gap words over all six calls: What 5, Where 3, When 3, How 3, Who 2, Why 2 (18 gaps).
Table groups (turn order): Owls, Foxes, Bears, Deer (painted animal badges; any group count from 2 to 4 is set in `Groups` under Rules, default 4).

## Interactions in detail
- Every tap acts at once. A card tap while Sam is talking cuts his line (V.hush of the line playing) and answers, so a quick class never waits; Say that again cuts and replays.
- Only gaps are judged. A card tapped when no gap is open (during a no-gap sentence) makes Sam say `notYet` once per call ("Wait for the crackly part, then ask!") and nothing passes.
- The phone passes after every judged card tap (right or wrong) and after Tell me more and each Quiz answer; the badge animates to the next group (Motion off: it swaps).
- The meaning card can be tapped any number of times; each tap replays the meaning (an event).
- Quiz: answer pictures are shuffled every time the question opens; the pad is hidden until both questions are answered.
- Take a message: tapping a placed card sends it back to the row; `Read the message` with an empty slot plays `msgEmpty`.
- Phone list: opening another call mid-call hushes everything and starts that call's ring; nothing carries over except the turn badge.
- Extremes: every card wrong on one gap (the wiggle hint after two, then free asks); Say that again tapped many times (the tip line once per call); Sound off (captions still show every sentence, static as a jagged blank, and the cards and pad work the same).
- Nothing is saved.

## Look
- Accent `--brand` #2d6a4f pine green (header, Answer, turn badge ring); gold #f0b43c for Next call, the meaning card, Read the message; paper #f5f8f2; ink #17241d; muted #4f5f56. Scene: a sunny classroom wall with a corkboard and a big window onto pines; the pad is yellow lined paper.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 5.96:1; ink on paper 15.00:1; muted on paper 6.31:1; ink on gold 8.65:1.
- Never color alone: the static blank is a jagged shape; right answers get a check icon; the turn badge is an animal picture plus its group name.
- Different from the K-2 ELA tools specced so far and this batch (plum, brick, blue, amber; letter-lanterns indigo).

## Art
Local FLUX (`scripts/localart.py`) in one bright gouache style; Ranger Sam is only a voice (never shown), so no people except where Content puts them in the message pictures (Gemini, `people: true`, Cory reviews).
- classroom: "A sunny classroom wall with a corkboard and a big window looking out on pine trees, gouache, the corkboard empty"; 16:9; cutout no; people no; backdrop.
- phone: "A big friendly cream desk speakerphone with a round speaker grill and one green button, gouache, plain white background"; 1:1; cutout yes; people no.
- notepad: "A yellow lined spiral notepad lying flat, blank, gouache"; 4:3; cutout no; people no; the message pad (text and pictures in code over it).
- group badges owl, fox, bear, deer: "A round badge with a friendly <animal> face, gouache, plain white background"; 1:1; cutout yes; people no.
- Message pictures, 24 (four per call, from Content's message orders), plus quiz pictures that differ from them (kite, hat, balloon; pine tree, roof, pond; moon, sun, sandwich; vote box, hat of names; road turtle; bear, truck; calendar Saturday; one, three, five owlets; fox, deer, duck); 4:3 for message pictures, 1:1 for quiz pictures; cutout no; people yes on: Mia with the kite, the fire crew, children voting, workers cutting the tree, people with binoculars (Gemini); the rest no.
About 50 images; 5 with people. Drawn in code: the question card icons, the static blank, captions, pad slots and numbers, the turn badge frame, the Rules card icons, all controls.

## Voice
Bank voice `gravel-ranger` (style "Say warmly with a gravelly voice, like an old park ranger telling stories"): Ranger Sam is the whole voice of the tool. Not used by any K-2 ELA tool specced so far or by the other four in this batch. The static burst is a code noise sound laid over a gap in the clip: each gap sentence is recorded twice, whole and with the eaten word replaced by a pause the length of the word, and the noise plays in that pause. `Curio.voice` with `scope: () => state.call + ':' + state.step`, `welcomeAfter: true`. Repeats: how lines once per load then hint only; event lines every time.
- event, whole, `sentence`: each Content sentence (gap version until answered).
- how `welcome` (after call 1's first sentence): "Before we talk, three phone rules: listen, one group at a time, and wait your turn. The phone goes around the tables."
- how `askHow` (first gap of the session): "Oh no, the phone crackled! Which part did you miss? Say your question, then tap the card: Who, What, Where, When, Why or How."
- event, whole, `answer`: Sam's answer for that gap (Content), which starts with the question word.
- event `wrongQ`: "{Word}? I didn't say that part yet. The crackly part was:" then the gap sentence.
- event `againTip` (once per call): "The phone is still crackly. Ask me a question about the part you missed!"
- event, whole, `meaning`: the new word's meaning.
- how `meanHow` (first time the meaning card appears): "Don't know a word? Tap What does it mean?"
- event `notYet` (once per call): "Wait for the crackly part, then ask!"
- event `turn` (each pass, short): "{Group}, your turn!"
- how `moreHow` (Tell me more, first time): "Now ask me more about it. Tap a card to hear it, then tap it again to ask."
- event, whole, `more`: the on-topic answer. event `offTopic`: "Ha! Let's stay on the {topic}."
- how `quizHow` (first time): "My turn to ask! Tap a picture to hear it, then tap This one."
- event, whole, `quizAsk`, `quizYes` ("Yes! You were listening."), `quizNo` ("Not quite. Think back to what I said.").
- how `msgHow` (Take a message, first time): "Let's take a message. Tell the call out loud, then tap the pictures in order."
- event, whole, `msgRead` (all in order): "Message: " then the four message lines in order (one per picture). event `msgLook`: "Some pictures are out of order. Look at the rings." event `msgEmpty`: "Fill every box first."
- event, whole, `callDone`: "Thanks, class! Great listening. Bye for now!"
Read speaks the hint, which names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Question word for a gap (SL.K.3, SL.1.3, SL.2.3) | Always the same card; cycling every card; guessing; reading the pad slot's label; tapping before the gap | Computed over 18 gaps: the best single card (What) fills 5 of 18; a fixed order of all six takes 3.4 asks per gap on average, every wrong one answered with "I didn't say that part" and the crackly line again, and each wrong ask passes the phone, so the group loses its turn; guess 1 in 6. Pad slots show only "?" until filled, never the needed word. Taps outside a gap are not judged. Not scored; the wiggle hint after two misses keeps the call moving. |
| Tell me more (SL.1.1b, SL.2.1b) | Guess; the longer card; the first card | Guess 50 percent; card order shuffled; lengths computed: the longer card is the on-topic one in 3 of 6 calls and the shorter in 3 of 6 (a first draft let "pick the longer" win 5 of 6, so three off-topic cards were lengthened). An off-topic pick is answered with why ("Let's stay on the kite"), which is the lesson. |
| Quiz (SL.1.2) | Guess; reading the pad; picking any picture heard in the call; position | Guess 1 in 3 (all 12 right by chance 2 in a million); the pad is hidden during the quiz; every quiz has at least one wrong picture that was heard in the call or is from the same place (pond, roof, a duck), so "something I heard" fails; positions shuffle every time. |
| Take a message (SL.2.2) | Guess the order; the order shown; the picture with more in it | Guess 1 in 24; cards are shuffled under the pad; it is read only when all four are in order, after the class has said it. |

## Heard in order
Waits means the next line waits for it to finish; taps always act at once and never wait for a line.
1. Load: tap Answer: ring stops, `sentence` 1 (whole, gap version), then `welcome`, then `askHow` (first gap). Next action spoken in `askHow`.
2. Each gap: the right card: `answer` (whole), `turn`, then the next `sentence` waits for both. A wrong card: `wrongQ` then the gap sentence (whole), then `turn`. Say that again: the last sentence, then `againTip` (once per call).
3. New word said: `meanHow` (first time) after that sentence; a meaning tap: `meaning` (whole).
4. Tell me more: `moreHow` (first time); first tap on a card speaks the card's question; second tap: `more` (whole) or `offTopic`.
5. Quiz: `quizHow` (first), `quizAsk` (whole); a picture tap speaks its name; This one: `quizYes` or `quizNo`; the second `quizAsk` waits for the feedback.
6. Take a message: `msgHow` (first); Read the message: `msgRead` (whole) or `msgLook` or `msgEmpty`. Then `callDone` (whole).
No line contains a bare letter or letter sound. Sound off: every sentence still shows as a caption, with the static blank.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.K.3, SL.1.1 (a to c), SL.1.2, SL.1.3, SL.2.1 (a to c), SL.2.2, SL.2.3 wording | Common Core State Standards, ELA, SL/K, SL/1, SL/2 pages, thecorestandards.org | CCSS ELA 2010 PDF, Speaking and Listening K to 5 (the official document) | yes |
| A baby goat is called a kid, and kids stand and walk within minutes to hours of birth | Penn State Extension, "Kidding management" (goat birth and newborn care) | University of Maryland Extension, Small Ruminant Program, "Kidding" | yes |
| A turtle on a road should be moved in the direction it was heading; children should tell an adult rather than handle it near traffic | Massachusetts Division of Fisheries and Wildlife, "Turtles crossing roads" | Ontario Turtle Conservation Centre, "Helping turtles cross the road" (in the direction it is going, only when safe) | yes |
| Box turtles move slowly and live near ponds, woods and fields | Smithsonian National Zoo, "Eastern box turtle" | National Wildlife Federation, "Eastern box turtle" | yes |
| Baby owls are called owlets; many owls rest in the day and hunt at night | Cornell Lab of Ornithology, All About Birds (owl species pages) | National Audubon Society, owl guide pages | yes |
| Red fox tracks show four toes and fall nearly in a straight line, one in front of another | Massachusetts Audubon, "Animal tracks: red fox" | Elbroch, Mammal Tracks and Sign (2003), red fox (four toes, direct-register trot in a narrow line) | yes |
| Red foxes hunt small animals such as mice and are active at dawn and dusk | Smithsonian National Zoo, "Red fox" | National Wildlife Federation, "Red fox" | yes |
Backed twice: 7. Cut: 1 ("owls sleep in the day": not true of every owl, so Sam says "many owls"). Ranger Sam, Pine Hollow Park and the call stories are our own writing.
Teacher notes: the turtle call's safety line ("tell a grown-up") is on purpose; the Groups setting changes how many tables share the phone.

Checks run (Python, scratchpad b1/phone.py, 2026-11-08): gap words 18 (What 5, Where 3, When 3, How 3, Who 2, Why 2); best single card 28 percent; fixed-order cycling 3.39 asks per gap; quiz all-guess 0.000002; message order 1 in 24; Tell me more card lengths (on, off) 26/27, 34/35, 28/19, 16/33, 29/18, 22/17, so longer wins 3 of 6. Contrast ratios as in Look.

## Done when
1. Focus and fold: at 1366x768 the phone, the caption with its static blank, the pad and all six (or seven) question cards show with no scroll; at 680x425 the caption, the cards and the turn badge show with no scroll and text is 10 px or more.
2. Every gap in all six calls fills only with its right card; a wrong card replays the crackly sentence; the pad never shows the needed word. (SL.K.3, SL.1.3, SL.2.3)
3. Say that again replays with static and the tip plays once per call; the meaning card appears after the new word and explains it. (SL.K.3, SL.1.1c, SL.2.1c)
4. Tell me more answers the on-topic card and turns the off-topic one aside with "Let's stay on the ...". (SL.1.1b, SL.2.1b, SL.2.3)
5. The phone passes after every judged tap; the badge shows the group's animal and name; the Rules card shows on call 1. (SL.1.1a, SL.2.1a)
6. Quiz: the pad is hidden; pictures shuffle; right gets a check. (SL.1.2)
7. Take a message reads back only in order, after all four cards are placed. (SL.2.2)
8. Tap while it plays: a card tap while Sam talks cuts him and answers; no older line plays after a newer one.
9. Pre-reader: every sentence, question card, choice and next action is spoken; every choice is a picture; a child alone can finish a call.
10. Voice: `askHow`, `moreHow`, `quizHow` play once each; `answer` and `sentence` lines play every time; Sound off still shows every caption.
11. Motion off: no badge or pad animation, same pacing; no network requests; nothing saved.

## Open questions
- None for Cory.
