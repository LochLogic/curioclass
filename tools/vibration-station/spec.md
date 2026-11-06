# Vibration Station

## One idea
Every sound on this bench can be stopped with a hand and every sound can make rice jump, so the class sees the shake that makes a sound and the sound that makes a shake, then uses that same shake to talk to Sam across the yard on a cup phone they build, break and fix, and across the park on a drum code they invent.

## Not like
- sound-elevator (K-2 arts): high and low, loud and soft as music on an elevator. Here pitch is one small Bench line; the subject is the shake behind every sound, and nothing is a note to place.
- orchestra-zoo (K-2 arts): hear and name real instruments. Here nothing is named or guessed by ear; the class makes things shake and watches what the shake does.
- shadow-puppet-studio (grade 1, light): tests materials in a beam of light. Here sound only, and the device is built for talking far away, not for a show.
- secret-code-signals (grade 4): wave amplitude and wavelength, and codes compared for speed and errors. Here there are no wave measures; the drum code is three beat counts a first grader can tap, and the point is that a loud sound reaches far.
- three-pigs-lab (grade 2 lab): tests materials for strength and weather. Here the tests are about shaking and sound, and the lab book records predictions next to what was seen, with no "best" material.

## Who and how
- Grade 1, science, module "Sound and Vibration" (science-1-sound-and-vibration). Standards: 1-PS4-1, 1-PS4-4.
- Driver: teacher on a projector (tool.json `driver: "teacher"`). The class says guesses out loud, hums together, and says the cup-phone message; a child or the teacher taps. Every question, choice and next step is spoken and every choice is a picture with a word, so a child alone at home can play (BASELINE rule 4).
- Minutes: Bench 3 to 5; Find out 10 to 12; Reach Sam 12 to 15. Fits one long period or two short ones.
- No personal prompts. The optional microphone listens only while Mic is on; on screen under the Mic button: "The microphone only listens. Nothing is recorded or saved, and nothing leaves this device." (BASELINE rule 7). The lab book and Sam's progress are kept for this page load only (nothing stored).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1-PS4-1 vibrating materials make sound | Find out 1 to 3: predict, pluck a band and watch it blur while it sounds; pluck and hold it still and the sound stops; plan what to put on the drum (rice, sand, sticker) so its shake can be seen, then tap it | The band's blur and the sound arcs together; both vanish the instant the hand lands; rice or sand jumping on the drum skin, higher with the mallet | 3, 4 |
| 1-PS4-1 sound makes materials vibrate | Find out 4 and 5: hum (Hum button or the class into the Mic) and the wrap on the tube shakes; plan a fair test (move the pan so it does not touch the bowl), bang, and the rice on the bowl jumps with nothing touching it | Sprinkles dancing only while the hum sounds; rice jumping on a bowl that nothing touches, with a visible gap between pan and bowl | 4, 5 |
| 1-PS4-1 plan and conduct investigations, evidence | Each Find out page: a spoken question, a prediction locked before the test, the test the class runs, and the lab book page "We thought / We saw"; two of the five need a plan the class picks (Q3 what to put on, Q5 is it fair) | The lab book strip filling page by page; the end page sorts the five under the two claims | 3, 5 |
| 1-PS4-4 design and build a device that uses sound to communicate over a distance | Reach Sam: build a cup phone from parts (cup, pencil, string, knot, step back until tight), fix it three times (droopy, pinched, untied), test whisper, cup phone and drum at the yard and the park, pick the way to tell a secret, then design a drum code (a beat count for each of three pictures) and send three messages across the park | The string drawn tight or droopy with the shake running along it; Sam hearing or puzzled; the "Where can Sam hear us?" chart filling by tests; Sam acting on the beats | 6, 7, 8 |

## Screens and modes
Header (kit): title "Vibration Station", mode buttons (`.seg`, icon plus word, 60 px): `Bench` (workbench icon, default), `Find out` (magnifier), `Reach Sam` (cup phone); then `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), with an icon and a word. Sound arcs (code-drawn curved lines spreading from whatever is sounding, size by loudness) show every sound even with Sound off, so the evidence never depends on hearing.

**On load and first tap.** Bench opens with all four stations still and quiet. Nothing speaks before the first tap (kit). First hint: "Tap a rubber band to pluck it." A first tap on a band plucks it at once (sound, blur, arcs) and queues `bandSeen`, so the welcome is skipped (BASELINE 16); what the welcome said is in the hint and Read. A first tap anywhere else that has no line of its own gets `welcome`.

**Bench** (explore). Focus: the four stations, all live. Layout at 1366x768: stage about 1036 x 700 holding a painted workbench; four stations in a 2 x 2 grid, each about 500 x 330, every control inside its station:
- Band box (top left): a shoebox with three bands (thin, middle, fat) drawn in code across its hole. Tap a band to pluck it; or drag it sideways and let go (the pull distance sets the blur width and loudness, 3 steps). `Hold still` (painted hand picture) pinches the last plucked band.
- Rice drum (top right): painted drum body, skin and rice drawn in code. Two beater pictures beside it: `Finger tap` (soft) and `Mallet` (big). `Hold still` lays a hand flat on the skin.
- Hum tube (bottom left): a painted cardboard tube with an elbow; its top end has clear wrap (code) with sprinkles. `Hum` (mouth picture) plays the hum while held (keyboard: held Space or Enter).
- Pan and bowl (bottom right): a painted pan and spoon a hand's width from a glass bowl with wrap and rice (code). `Bang` (spoon picture) strikes the pan; `Hold still` grabs the pan.
- Panel (330 px): hint (22 px), then `Mic` (microphone icon, on/off) with the privacy line under it, then `Find out` (gold, magnifier), shown after any two stations have sounded.
- At 680x425: panel 210 px; the grid stays 2 x 2 with stations about 230 x 180; beater, Hum, Bang and Hold still buttons 44 px; the privacy line folds to "Listens only. Nothing saved." with the full line in Read.

**Find out** (five investigations in order). Focus: one station, large, in the middle of the stage (about 760 x 500); above it the question card (picture plus words, 64 px tall); under it the lab book strip (five page thumbnails, 120 x 80; a filled page shows its "We saw" picture). Panel: hint, then the step's choices: two prediction cards (150 x 130, picture plus words), or plan tiles, then `Next` (gold, arrow) after a result. A tap on a filled lab book page reopens that investigation from its question (the page is replaced by the new run). Steps per investigation: question, predict, (plan), test, result. The station's controls are hidden until the prediction is tapped, so a test cannot run before the guess, and the station draws still (Mic ignored) until the test step.
1. Q1 band: "Will the band shake when it makes a sound?" Cards: shaking band (code icon, zigzag blur) "It will shake" / still band "It will stay still". Test: pluck any band. Result: blur plus arcs.
2. Q2 band: "If we hold the band still, will the sound keep going?" Cards: ear with arcs "The sound keeps going" / ear with arcs crossed "The sound stops". Test: pluck, then `Hold still` while it rings (the band rings 4 s in this tool). Result: blur and arcs end on the same frame the hand lands.
3. Q3 drum: "When we tap the drum, does it shake?" Cards: drum with zigzag "It shakes" / drum plain "It stays still". Plan: "We can't see a drum shake. What can we put on it?" Tiles: `Rice`, `Sand`, `Sticker` (painted pictures). Then test: `Finger tap` or `Mallet`. Rice or sand: bits jump (higher with the mallet). Sticker: the drum sounds, nothing can be seen moving; the class picks again.
4. Q4 hum: "Will our hum make the wrap on the tube shake?" Cards: tube with jumping sprinkles "It will shake" / still sprinkles "It will stay still". Test: hold `Hum`, or with Mic on, the class hums for 1 s above the hum level. Result: wrap wobbles and sprinkles dance while the sound lasts and settle when it stops.
5. Q5 pan and bowl: "Can the pan's sound make the rice jump, with nothing touching the bowl?" Cards: jumping rice "The rice will jump" / still rice "The rice will stay still". Plan: the pan starts pressed against the bowl. Tiles: `Move the pan` (arrow picture) and `Bang` (spoon). Bang while touching: rice jumps, result `r5touch`, the page records "Pan touching: we couldn't tell". Move the pan: it slides to a clear gap (a hand's width, gap outlined), then Bang: rice jumps.
After Q5 the end page opens over the stage: two claim cards side by side, "Shaking makes sound" (pages 1, 2, 3) and "Sound makes things shake" (pages 4, 5), each page with "We thought" and "We saw" pictures. Buttons: `Reach Sam` (gold), `Bench`.
At 680x425: the station about 400 x 250, question card 40 px, lab book strip folds to five dots (filled dots for done pages), prediction cards 90 x 80 side by side in the panel.

**Reach Sam** (five steps, a step strip of five icons at the top of the stage). Focus: the string between our cup (bottom left foreground, held in painted hands) and Sam, across a painted scene. Stage: the yard (steps 1 to 4) or the park (step 3's Park tests and step 5). Panel: hint, then the step's buttons, then `Next` (gold) when a step ends.
1. Build: tray in the panel: `Paper cup` and `Tin can` (pick one, both work), `Pencil` (pokes the hole), `String` (threads it), `Knot` (ties it). Each lights in turn. Sam ties his end, then `Step back` (Sam walks right by 1 m a tap; dragging Sam also works) until the string is drawn straight; past the string's length Sam stops. `Talk` (mouth picture): the class says "Hello, Sam!" and a shake (a small code wiggle) runs along the string to Sam's cup.
2. Fix it: three scenes. Each has Ben (Sam's little brother) standing near the string, both knots in view and Sam at some distance. Exactly one fault per scene, drawn at random (with replacement) from: droopy (Sam has walked in, the string sags), pinched (Ben's fingers on the string), untied (the string end lies on the grass by Sam's cup). Buttons: `Talk`, `Talk louder` (megaphone). Tappable on the stage: Sam (steps back), Ben (lets go), Sam's knot (ties it). Flow: Talk, Sam is puzzled, then the class looks and taps. The first tap after `cantHear` is the one recorded: right, the fix plays and the scene card says "We found it"; anything else, the shake view turns on, the wiggle runs from our cup and stops at the fault (which gets a ring), and the scene card says "Sam's string showed us". Then the fault is tapped and fixed and Talk works.
3. Where can Sam hear us? Chart in the panel: rows `Yard`, `Park` (pictures), columns `Whisper`, `Cup phone`, `Drum` (pictures), cells 80 x 64, empty until tested. Tap a place (the stage changes), then a way. Results: Yard whisper: Sam puzzled (ear crossed). Yard cup phone: Sam hears (ear with arcs), nobody else. Yard drum: Sam hears and two neighbor kids pop up over the fence (ear with arcs plus a "many ears" icon). Park whisper: ear crossed. Park cup phone: our string runs out at the bench halfway (string-end icon). Park drum: Sam hears. `Next` lights when all six are filled.
4. The secret (yard): the chart stays in the panel. Three picture buttons on the stage: `Whisper`, `Cup phone`, `Drum`. The first pick is recorded on the step card.
5. Drum code (park): the code card on the stage, top: three message pictures (`Lunch` plate, `Play` ball, `Home` house), each with four dot tiles (1, 2, 3, 4 beats, drawn as dots). The big drum in the foreground; Sam far right. When all three have a count and none repeat, the first message card flies to the stage center. The class taps the drum; each beat sends arcs across the park; 1.5 s after the last beat Sam acts.
What the picture shows for every outcome: heard, Sam's cup at his ear and a smile, then a cheer; not heard, Sam's hand cupped, head tilted (puzzled pose); droopy, string sagging to the grass; pinched, Ben's fingers on the string; untied, the loose end on the grass; secret out, the neighbor kids over the fence; drum right, Sam runs to the picnic table, kicks the ball, or walks to the house; drum wrong, Sam does the other message's action; not in the code, Sam shrugs.
At 680x425: the chart cells 52 x 44; step strip icons 28 px; code card dot tiles 44 px; the drum 120 px.

## Content
**Bench sounds** (Web Audio in the tool, played only when Curio.sound is on and after the first tap): thin band 330 Hz, middle 220 Hz, fat 147 Hz plucks (decay 4 s, louder by pull step 1 to 3); drum thump about 110 Hz with a short noise burst (finger soft, mallet 2.5 times louder, decay 1.5 s); hum a filtered buzzy tone about 150 Hz while held; pan clang (bright noise burst plus 600 to 1400 Hz partials, decay 2 s). `Hold still` cuts the held object's sound in 60 ms and its blur, arcs and jumping bits on the same frame. These are a tool's sounds, not claims.
**Shake drawing** (a picture, not a measure): band blur width 6, 12 or 18 px by pull step; drum skin and wrap draw no visible bend at 1366 px except the bits on them; bits jump to a height by loudness (finger 8 px, mallet 24 px; pan 20 px; hum 6 to 20 px by Mic level, 14 px with the Hum button). Real shakes are much faster than the drawing; the tool never states a speed.
**Mic**: level from the input's RMS, smoothed over 100 ms; under 0.02 nothing moves; 0.02 to 0.06 the wrap jitters and bits twitch 2 px; above 0.06 the bits jump by level. Room noise can move them; that is still sound making the wrap shake.
**Find out pages**: page n shows the prediction picture under "We thought" and the result picture under "We saw" (Q3 also "We put on: rice"; Q5 also "First test: pan touching, we couldn't tell" when that happened).
**Reach Sam**: string 15 m; yard Sam at 12 m when tight; park Sam at 60 m; the park bench (string end) at 15 m. Messages and actions: Lunch "Lunch is ready" (Sam runs to the picnic table), Play "Come play ball" (Sam kicks the ball), Home "Time to go home" (Sam walks to the house). The three sends come in a shuffled order. Messages are pictures with one word each.

## Interactions in detail
- Every tap acts at once: a pluck during a line plays its sound and blur; a fix tap during `cantHear` is taken (it counts as the first tap). No animation blocks a control. Sam's walks take 0.8 s (Motion off: he appears at the end spot on the same beat).
- Bench: a pluck on a ringing band restarts it; Hold still with nothing sounding does nothing and plays nothing. Hum stops when released or when focus leaves. Mic: on tap, the browser asks; on refusal or no device (or an iframe without permission), Mic turns off and `micOff` plays; Hum still works. The tool's own hum is muted while Mic is on, so the speakers do not feed the mic.
- Find out: a prediction tap locks the card (the other greys and cannot be tapped) and shows the test controls. Q2: Hold still before a pluck plays `r2early`; after the ring has ended plays `r2late`; neither fills the page. Q3: the sticker run plays the drum, shows no motion, plays `r3sticker`, and the sticker comes off; Rice and Sand stay tappable. Q5: Bang while touching fills nothing, plays `r5touch` and lights Move the pan. Next is shown only after a page fills. Reopening a page clears its prediction.
- Reach Sam step 1: Talk before the knot plays `talkLoose`; Talk while slack plays `talkSlack`. Step back past 12 m (yard) plays `stepMax`. Step 2: a tap on Ben when he is not pinching, on Sam when the string is tight, or on a tied knot plays `notThat` with its name, then the shake view. Talk louder never fixes: Sam stays puzzled and the shake view turns on. Doing nothing changes nothing. Step 3: re-testing a filled cell replays it. Step 5: dot tiles may be changed until the first send; a repeat count plays `codeSame` and the card waits. More than 4 beats or a count not in the code plays `samNone`. A wrong count that is another message plays `samWrong`. The same message card stays until Sam does it right.
- Mode switch hushes speech; each mode keeps its place in this page load. `Next` on the last Reach Sam step shows the end card with `Bench` and `Find out`.

## Look
- Accent `--brand` #9b2f6e berry (header, mode buttons, step strip); gold #f2b632 for Next, Find out and the end buttons; paper #fbf6ee; ink #2a2230; muted #5f5566; bench wood #d9b98c; shake and sound arcs #1d6f7a; sky #cfe6f2; "not heard" cross #b23a2a. Different from sound-elevator indigo #3d4fa8, orchestra-zoo and habitat-hunt greens (#2f7a4a, #3f6b2f) and estimation-station red #9c3520.
- Contrast (WCAG 2.1, computed): white on brand 6.94:1; brand on paper 6.45:1; ink on paper 14.25:1; muted on paper 6.55:1; ink on gold 8.40:1; ink on bench 8.23:1; arcs on paper 5.41:1; white on arcs 5.82:1; ink on sky 11.86:1; cross red on paper 5.53:1; arcs on bench 3.12:1 (non-text, over 3:1). Heard and not heard differ by shape (arcs vs a cross), never by color alone.

## Art
One style: bright painted picture book, a sunny school science corner and a backyard. People go to Gemini with `people: true` and onto Cory's contact sheet with the fresh representation check (BASELINE 11). Everything else may use local FLUX. Text on signs and cards stays in code.
- bench-backdrop: "A sunny classroom science corner with a long wooden workbench, a pegboard wall with blank labels, a window with plants"; 16:9; cutout no; people no; Bench and Find out.
- shoebox: "An open cardboard shoebox seen from the front at a slight angle, a round hole cut in the lid"; 4:3; cutout yes; bands drawn in code across the hole.
- drum-body: "A small red toy drum with gold rim and rope lacing, side view, plain top edge"; 4:3; cutout yes; the skin and rice are code.
- elbow-tube: "A cardboard tube with an elbow bend, the low end open toward the viewer, the high end pointing up"; 3:4; cutout yes; wrap and sprinkles are code.
- pan and spoon: "A shiny metal cooking pan, side view" 4:3, and "a metal spoon" 4:1; cutout yes, separate so the spoon can swing.
- glass-bowl: "A clear glass mixing bowl, side view"; 4:3; cutout yes; wrap and rice are code.
- beaters: "A wooden drum mallet with a felt head" 1:1, cutout yes. Plan tiles: "a small pile of white rice", "a small pile of golden sand", "a shiny star sticker", 1:1 each, cutout yes.
- hands (people yes): "A child's hand pinching, side view", "a child's hand lying flat, palm down", "two child's hands holding a paper cup, seen from behind", "two child's hands holding a tin can, seen from behind"; 1:1 each; cutout yes; Hold still and our cup.
- cups: "A white paper cup" and "a clean tin can with a smooth rim", side view, 3:4, cutout yes; pencil "a yellow pencil" 4:1 cutout yes; build tray and Sam's cup.
- yard: "A grassy backyard with a wooden fence on the left, a slide in the middle distance, a picnic table and a house far right, afternoon light"; 16:9; cutout no; steps 1, 2, 3 (Yard), 4.
- park: "A wide green park seen from one end, a wooden bench nearby, trees, a picnic table and a small house far away"; 16:9; cutout no; steps 3 (Park), 5.
- big-drum: "A big bass drum on a stand with a mallet, three-quarter view, blank drum head"; 1:1; cutout yes; step 3 Drum and step 5.
- sam (people yes, a 7-year-old, all poses full body, 3:4, cutout yes, scaled down in the park so all of him shows): standing with a cup at his ear, puzzled with a hand cupped to his ear, cheering, shrugging, walking, running toward the viewer's right, kicking a ball, waving. Sam's look is decided at the contact sheet.
- ben (people yes, a 4-year-old, 3:4, cutout yes): standing with hands at his sides, pinching a string at chest height.
- neighbors (people yes, 4:1, cutout yes): two children peeking over a fence top.
- message pictures: "a plate with a sandwich and an apple", "a red and white ball", "a small house with a red door"; 1:1; cutout yes; code card and messages.
25 images plus Sam's 8 poses and Ben's 2; people images: 4 hands, 8 Sam, 2 Ben, 1 neighbors. Drawn in code: bands, skins, wrap, rice, sand, sprinkles, the string and its wiggle, sound arcs, ear icons, prediction icons, chart, dot tiles, step strip, lab book.

## Voice
Bank voice `curious-librarian` (Aoede). Style: "Say curiously and warmly, like a friendly school librarian wondering out loud with a class." Different from orchestra-zoo (playful-friend), sound-elevator and habitat-hunt (Puck), three-pigs-lab (gentle-storyteller) and melt-or-not (clear-teacher). `Curio.voice` with `scope: () => state.mode + ':' + state.step`. Templates in braces are expanded by the builder; every expansion is in lines.json.

Bench (how lines once each; none repeat on later plucks):
- how `welcome` (stale after any station sounds): "Welcome to Vibration Station! Let's make things shake, and listen. Tap a rubber band to pluck it."
- how `bandSeen` (first pluck): "See the band shake? The shake makes the sound. Tap Hold still to stop it."
- how `bandStill` (first Hold still on a ringing band): "Still band, no sound!"
- how `pitch` (after both the fat and the thin band are plucked): "The fat band makes a lower sound. The thin band makes a higher sound."
- how `drumHow` (first drum tap): "Tap, and the rice jumps! The drum shakes when it makes a sound. Try the mallet."
- how `drumBig` (first mallet): "A bigger hit makes a bigger shake, and a louder sound."
- how `humHow` (first Hum or first Mic hum), whole: "Put your fingers on your throat and hum. Feel the shake? Our hum makes the wrap shake, and the sprinkles dance."
- how `panHow` (first Bang): "Bang! Nothing touched the bowl, but the rice jumped. The sound made it shake."
- how `micOn`: "The microphone is on. Everyone hum together, and watch the sprinkles."
- event `micOff` (once per cause): "The microphone is not working here. Press and hold Hum instead."
- how `benchNext` (after two stations): "Tap Find out to test it like a scientist."

Find out:
- event, whole `q1` to `q5`: the question as in Screens ("Will the band shake when it makes a sound?" ...), each followed in the same clip by "Say your guess out loud, then tap a picture." for q1 only; later questions end "Tap a picture." 
- event `predicted` (each prediction): "We think: {card words}."
- event per test (each opening of the test step): `t1` "Tap a band to pluck it, and watch." `t2` "Pluck a band. Then tap Hold still while it rings." `t3plan` (whole) "We can't see a drum shake. What can we put on it? Tap rice, sand or the sticker." `t3` "Now tap the drum with the finger or the mallet." `t4` "Press and hold Hum, and everyone hum!" (Mic on: "Everyone hum together, now!") `t5plan` (whole) "Look. The pan is touching the bowl. Is that a fair test? Tap Move the pan, or tap Bang."
- event, whole results: `r1` "The band shook, and we heard it. Shaking makes sound!" `r2` "We held it still, and the sound stopped. No shake, no sound!" `r3` "The {rice / sand} jumped! The drum shakes when it makes a sound." `r4` "Our hum made the wrap shake, and the sprinkles danced. Sound makes things shake!" `r5` "Nothing touched the bowl, and the rice jumped. The pan's sound made it shake!"
- event `match` after a result that fits the prediction: "Just like we thought!"; `surprise` otherwise: "A surprise! Now we know."
- event `r2early`: "Pluck it first. Then tap Hold still while it rings." event `r2late`: "The sound already stopped. Pluck again, then tap Hold still fast."
- event `r3sticker`: "The sticker is stuck on, so we can't see it jump. Tap rice or sand."
- event, whole `r5touch`: "The rice jumped. But the pan was touching the bowl, so the bang could shake it right through the pan. We can't tell! Tap Move the pan." event `moved`: "Now nothing touches the bowl. Tap Bang!"
- how `nextHow` (first result; stale when Next is tapped): "Tap Next."
- event, whole `claims` (end page): "We found out two things. Shaking makes sound. And sound makes things shake!" then how `toSam`: "Tap Reach Sam to use sound to talk far away."

Reach Sam:
- how, whole `samWelcome` (mode entry, step 1): "This is Sam. Sam is all the way across the yard. Let's build a cup phone to talk to Sam! Tap a cup."
- event `cupPaper` / `cupCan`: "A paper cup. Its bottom can shake. Tap the pencil." / "A tin can. Its bottom can shake. Tap the pencil."
- event `poked`: "Now tap the string to push it through." event `threaded`: "Tap the knot, so the string can't slip out." event `tied`: "Sam tied his end too. Tap Step back until the string is tight."
- event `tight`: "The string is tight! Tap Talk, and everyone say: Hello, Sam!" event `stepMax`: "That's as far as the string goes."
- event `talkLoose`: "Tie the knot first. Tap the knot." event `talkSlack`: "Sam can't hear. The string is droopy. Tap Step back."
- event, whole `heard`: "Sam heard you! Your voice shook the cup, the cup shook the string, and the string shook Sam's cup."
- event, whole `fixScene` (each Fix scene): "Tap Talk, and everyone say: Meet me at the slide!"
- event, whole `cantHear`: "Sam can't hear! Look at the string. Then tap the thing that needs fixing."
- event `fixSag` "Yes! The string was droopy. Sam steps back. Now tap Talk." `fixPinch` "Yes! Ben was holding the string still. Now it can shake. Tap Talk." `fixKnot` "Yes! The string came out of Sam's cup. Sam ties it. Tap Talk."
- event `louder`: "Talking louder didn't help." event `notThat`: "Ben isn't touching the string." / "The string is already tight." / "That knot is tied."
- event, whole `lookWiggle` (after `louder` or `notThat`): "Watch the shake go down the string. See where it stops? Tap that."
- event `heardFix`: "Sam heard you!" event, whole `fixDone`: "You fixed it three times. A cup phone needs a string that is tight and free to shake."
- how, whole `chartHow`: "Where can Sam hear us? Tap a place. Then tap whisper, cup phone or drum."
- event results: `whYard` "Sam can't hear a whisper from across the yard." `cupYard` "Sam hears the cup phone, and only Sam!" `drumYard` "Boom! Sam hears the drum. So does everyone next door." `whPark` "Too far! Sam can't hear a whisper." `cupPark` "Our string isn't long enough to reach across the park." `drumPark` "Boom! The drum is loud enough to reach Sam across the park."
- event `chartFull`: "Our chart is full. Tap Next."
- event, whole `secretAsk`: "Here is a secret: the treasure is under the slide. Look at our chart. Tap the best way to tell only Sam."
- event `secretCup` (whole) "The cup phone! Only Sam heard the secret." `secretDrum` "Boom! Oh no, everyone next door heard. Tap another way." `secretWhisper` "Sam can't hear a whisper that far. Tap another way."
- how, whole `codeHow`: "Sam is across the park, and the cup phone can't reach. Let's make a drum code! For each picture, tap how many beats."
- event `codeSame`: "Two pictures have the same beats. Sam can't tell them apart. Change one." event `codeReady`: "Our code is ready."
- event, whole `sendAsk`: "Tell Sam: {Lunch is ready / Come play ball / Time to go home}. Look at our code, then tap the drum."
- event, whole `samRight`: "{k} beats! Sam {runs to lunch / kicks the ball / walks home}." `samWrong`: "{k} beats means {other message} in our code, so Sam {other action}. Look at the code and tap again." `samNone`: "{k} beats isn't in our code. Sam shrugs. Look at the code and tap again."
- event, whole `samEnd`: "Sam got all three! We used sound to talk far away."
Read speaks the hint, which always names the step's action and control and never a hidden one (no Next before a result, no Move the pan after it moved). Repeats: `notThat` once per thing per scene; `codeSame` once per change; results every time.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Find out predictions (not scored) | Guessing; always the first card; changing the guess after seeing; the answer on screen | Nothing is awarded for a right guess; the page records "We thought" next to "We saw", and `surprise` is a normal ending. The card locks on tap and the test controls only appear after it, so no result can be seen first; the station draws still (Mic ignored) until the test step, and card order is shuffled per question. |
| Find out pages fill (evidence) | Doing nothing; mashing Next; mashing Hold still; tapping a filled page | Next is hidden until the page fills, and the page fills only from the test action (Q2 needs a pluck, then Hold still while it rings: early and late taps play `r2early` / `r2late` and fill nothing). Doing nothing leaves the hint on the test. |
| Q3 plan (what to put on the drum) | Guessing; elimination; tile position | Two of three work (rice, sand), so a guess often works, and that is fine: any loose bits are a good plan. The sticker run is itself a test the class watches (sound, no visible jump) and the page keeps "We tried: sticker"; nothing is scored for the first pick. |
| Q5 fair test | Always Move the pan; Bang at once; elimination | Bang while touching gives a jump but `r5touch` (whole) names why it can't count and the page records "Pan touching: we couldn't tell"; the page fills only from a Bang with the gap. Always moving the pan is the fair test itself; the line says why. |
| Cup phone works (build) | Talk before tying; Talk while droopy; mashing Step back | Sam hears only with the knot tied and the string straight (talkLoose, talkSlack); Step back stops at the string's length (`stepMax`), so mashing ends tight, which is the build step the class watches happen. |
| Fix it, first tap (recorded "We found it") | Guessing among Sam, Ben, knot, Talk louder; always the same fix; elimination across scenes; the common wrong answer (talk louder); doing nothing | Four targets: a guess is right 1 in 4, and only the first tap counts. Faults are drawn with replacement, so knowing the first two scenes says nothing about the third (simulated: 1 in 3). Ben, both knots and Sam are always in view, so presence gives nothing away; the fault shows only as how the string looks. Talk louder never fixes. Doing nothing: Sam stays puzzled. After a miss the shake view shows where the shake stops, so the scene still teaches, and the card says "Sam's string showed us". |
| Chart cells | Guessing; the answer on screen | A cell is empty until that test is run; no cell shows a result before its test. |
| The secret (first pick recorded) | Guessing (1 in 3); reading the chart | Reading the chart is the skill (choosing a design from test evidence); a wrong pick plays its outcome (secret out, or not heard) before the next pick. |
| Drum code is usable | All the same count | `codeSame` blocks the code until all three differ; any three different counts is a valid design. |
| Sam acts right (each send) | Mashing the drum; always one beat; reading the line for the count; the common wrong answer (another message's count) | Mashing gives a count over 4 (`samNone`) or a random one (1 in 6 right for counts 1 to 6); one beat fits only one message, and sends are shuffled; `sendAsk` never says the count, only the message and "look at our code"; another message's count makes Sam do that thing, seen at once. |

## Heard in order
Taps always act at once; "waits" means the next line waits for this one to finish.
1. Bench load, first tap on a band: pluck sound, then `bandSeen`. First tap elsewhere without a line of its own: `welcome`. Later firsts at each station: `bandStill`, `pitch`, `drumHow`, `drumBig`, `humHow` (whole), `panHow`, each after its own sound starts; then `benchNext` after the second station. Mic: `micOn` or `micOff`.
2. Find out, each question: `qN` (whole; the cards are live while it plays), the class answers out loud, tap a card: `predicted` (waits for `qN`), then `tN` or the plan line (waits). Next action spoken: the test or plan step.
3. Q3 plan: `t3plan` (whole), a tile: sticker plays `r3sticker` after the drum sound; rice or sand play `t3`, then the drum tap plays `r3` (whole), then `match` or `surprise`, then `nextHow` (first time). Feedback always plays before Next's new `qN`, which waits for it.
4. Q2: `t2`, pluck, Hold still: `r2` (whole) then `match` / `surprise`; or `r2early` / `r2late` and the step stays.
5. Q5: `t5plan` (whole); Bang while touching: `r5touch` (whole); Move the pan: `moved`; Bang: `r5` (whole), `match` / `surprise`. End: `claims` (whole), then `toSam`.
6. Reach Sam build: `samWelcome` (whole), `cupPaper` or `cupCan`, `poked`, `threaded`, `tied`, (`stepMax`), `tight`, Talk: `heard` (whole), `nextHow`.
7. Each Fix scene: `fixScene` (whole), Talk, `cantHear` (whole; a tap during it is taken and its line waits for it). Right: `fixSag` / `fixPinch` / `fixKnot`. Wrong: `louder` or `notThat`, then `lookWiggle` (whole), then the fix line on the fault tap. Talk: `heardFix`. After scene 3: `fixDone` (whole), then `nextHow`.
8. Chart: `chartHow` (whole), each test: its result line after its sound (whisper, phone or boom); `chartFull` after the sixth.
9. Secret: `secretAsk` (whole); a pick: its line; a wrong pick's line names the next action.
10. Code: `codeHow` (whole), (`codeSame`), `codeReady`, then `sendAsk` (whole, waits for `codeReady`); the drum beats; 1.5 s after the last beat Sam acts and `samRight` / `samWrong` / `samNone` (whole) plays; the next `sendAsk` waits for it. After three: `samEnd` (whole).
No line contains a bare letter or a sound spelled out; beat counts are spoken as words.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| 1-PS4-1 and 1-PS4-4 wording; examples: plucking a stretched string, paper near a speaker; cup-and-string telephones and a pattern of drum beats as devices | NGSS, nextgenscience.org, 1-PS4 (performance expectations and clarification statements) | NGSS@NSTA Hub, 1-PS4-1 and 1-PS4-4 pages | yes |
| Sound is made by things that vibrate; a plucked string vibrates | University of Manchester, Mathematics of Waves and Materials, "Dancing Sprinkles" guide | Exploratorium, Science Explorer "Ear Guitar" | yes |
| Stopping the shake (pinching the string) stops or weakens the sound | Exploratorium, "Ear Guitar" ("pinch the string ... your friend won't hear your voice as well") | Panasonic Kids School, Library of Wonders, "The Wonder of Sound" (pinching the string stops it carrying sound) | yes |
| Sound makes stretched wrap shake and rice or sprinkles on it jump; banging a pan near the bowl does this | Manchester "Dancing Sprinkles" (bang a baking sheet "as close as you can to the bowl without touching it") | Tinkercast, Wow in the World, "The Dancing Rice Experiment" | yes |
| Louder sounds make bigger shakes (more movement) | Manchester "Dancing Sprinkles" | Little Bins for Little Hands, "Dancing Sprinkles" | yes |
| Your voice comes from vocal folds in your throat shaking | NIDCD, "Taking Care of Your Voice" | The Voice Foundation, "Understanding How Voice is Produced" | yes |
| A thicker band makes a lower sound | Science Buddies, "Rubber Band Guitar" | Smithsonian Science Education Center, "Match the Pitch" | yes |
| A cup phone works only with a tight string; the voice shakes the cup bottom, the string carries the shake to the other cup | Exploratorium, "Ear Guitar" (loose string: vibrations die out) | Scientific American, Bring Science Home, "Talk through a String Telephone" | yes |
| A whisper is quiet (about 30 dB near you) and sound gets weaker with distance, so a louder sound reaches farther | CDC hearing loss noise guidance (whisper 30 dB, talk 60 dB) and Tioga County PA noise chart (quiet whisper at 3 feet 30 dB) | The Physics Classroom, "Intensity and the Decibel Scale" (inverse square fall-off); OpenStax College Physics 17.3 | yes |
Backed twice: 9. Cut: 3 (a string touching a fence stops a cup phone: one source only, so the fence fault became "untied"; a heavy block on a drum won't jump: physics unclear, replaced by the sticker; drum signalling traditions such as West African talking drums: not added, so no cultural content needs review). Sam, Ben, distances and string length are story values.

Checks run (Python, scratchpad vs_check.py, 2026-11-06):
- Contrast ratios as listed in Look.
- Audibility model (inverse square, -20 log10 r from 1 m): whisper 30 dB is 8 dB at 12 m and below 0 at 60 m (under a yard's background); a big drum taken at 90 to 95 dB at 1 m is 54 to 59 dB at 60 m, above a park's background; so the six chart results hold. No decibel number is shown on screen.
- Codes: 64 ways to give counts 1 to 4 to three messages, 24 with no repeat; all 24 are accepted.
- Mashing a send: a random count of 1 to 6 hits the right message 1 in 6; always one beat fits one message in three.
- Fix it: faults drawn with replacement, "guess the kind not yet seen" hits the third scene 1 in 3 (100,000 runs), same as chance; first-tap guessing 1 in 4; Talk louder 0.
- Q2 timing: the 4 s ring gives a projector class time to tap Hold still; early and late taps fill nothing.

## Done when
1. Focus: at 1366x768 the active station (Find out) or the string with Sam (Reach Sam) is the biggest thing on the stage; prediction cards, plan tiles, Hum, Bang, Hold still, Talk, Talk louder, Step back, the chart and Next are all above the fold; at 680x425 the station or string, its controls and the hint show without scrolling, text 10 px or more.
2. Bench: every station sounds with arcs; Hold still stops the sound and the blur or jumping on the same frame; the fat band sounds lower than the thin; the mallet makes higher jumps than the finger; Mic refused falls back to Hum with `micOff` and the privacy line is shown.
3. 1-PS4-1 (shaking makes sound): Q1 to Q3 each lock a prediction before the test, fill their page only from the test, and Q2 rejects early and late Hold still taps; Q3's sticker shows no jump and keeps the page empty.
4. 1-PS4-1 (sound makes things shake): Q4 sprinkles move only while the hum (button or Mic) lasts; Q5 with the pan touching records "we couldn't tell" and fills only after Move the pan and Bang with a visible gap.
5. The end page sorts pages 1 to 3 and 4 and 5 under the two claims with "We thought" and "We saw" pictures.
6. 1-PS4-4 build: Talk fails before the knot and while droopy, works once tight; Step back stops at the string's length.
7. Fix it: Ben, both knots and Sam are in every scene; the fault is drawn at random with replacement; Talk louder never fixes; a missed first tap turns on the shake view that stops at the fault; the scene card records the first tap honestly.
8. Chart and code: cells fill only by tests with the six results above; the secret plays each pick's outcome; a repeated beat count is blocked; each send makes Sam do the matching message, another message, or shrug; `sendAsk` never speaks the count.
9. Tap while it plays: plucking during `qN`, or tapping Ben during `cantHear`, acts at once, and no older line plays after a newer one; every result line plays before the next question.
10. Pre-reader: every question, choice and next step is spoken; every choice is a picture with a word; a child alone with Sound on finishes Find out and Reach Sam without reading. With Sound off the arcs and ear icons carry every result.
11. Voice: five plucks in a row speak `bandSeen` once; five wrong drum sends speak `samWrong` or `samNone` each time; no line names a hidden control.
12. Motion off: blur, jumps, walks and wiggles show their end states on the same beats; no network requests.

## Open questions
- None for Cory. People art (hands, Sam, Ben, the neighbor kids) goes to the contact sheet and the fresh representation check (BASELINE 11). No cultural, Native or hard-history content, so no sensitivity review is needed.
