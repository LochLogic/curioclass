# Spot the AI

## One idea
Ten everyday machines come in look-alike pairs (a key-code door and a phone that opens when it sees your face, a
talking teddy and a smart speaker); the class guesses which ones use AI, then opens each machine up to find either a
rule card that a person wrote, or a huge pile of examples it learned a pattern from.

## Not like
- teach-the-robot (2, spec): the class trains Kip with examples and watches it improve. Here the class trains nothing:
  it sorts real-world machines, and the reveal is what is inside each one (a written rule or learned examples).
- robot-dance (K): a robot that follows cards exactly. Here following a rule is the "not AI" side, shown as a contrast.
- computer-builder (1): the parts of a computer. Here the machines' insides are shown as ideas (rule card, example
  pile), not parts.
- input-or-output (2, this group): what goes in and out of gadgets. Here the question is how a machine decides.
- me-vs-the-counter, secret-keeper (this group): counting data, privacy. No overlap.

## Who and how
- Grade 1, computer science. Module: What Is AI? (Algorithms and Programming).
- Topic line: what AI is and how it learns patterns
- Driver: teacher on a projector. The class votes with hands (sparkle hands for AI, fists for a rule machine); the
  teacher taps the class's choice and then opens the machine.
- 10 to 20 minutes. tool.json: driver "teacher", minutes "10-20", modes ["Machine Shop", "AI or Not?"],
  grades_label "Grade 1".
- Standards (CSTA 2026 ids from the module): E1-ALG-ML-02, E1-SOC-HU-15. No 2017 AI standard; teachers can use AI4K12
  Big Idea 3 (computers can learn from data) and 1A-IC-16 (how computing changes how people live).
- Reads nothing: icons on every control, every fixed line voiced, 60 px targets.

## Screens and modes
Header (kit): title "Spot the AI", small line "A rule, or a pattern?"; mode buttons "Machine Shop" (wrench and gear
icon) and "AI or Not?" (spotlight icon); Motion, Sound, Read.

Stage: the painted workshop (art: workshop) with a spotlight cone drawn in code over the bench; the painted machines
(art: machine kit) sit on two painted shelves (art: shelf, used twice) and on the bench; re-laid per size. Screens,
keypad numbers, the elevator's floor number and every word are drawn in code over the machines' blank surfaces.

Panel: `#hint`, then the mode's controls.

### Mode 1: Machine Shop (explore, opens first)
Focus: the machine on the bench under the spotlight, the largest thing at the stage center; once opened, its inside
(rule card or example pile) takes the center beside it at the same size, and the shelves shrink to a strip along the
top. The ten machines sit on two shelves, paired side by side (pair partners next to each other). Tap a machine: it
moves to the bench and does its job (Content), with sound. Then "Open it up" (screwdriver icon) slides its front off:
- A rule machine shows a rule card (code): a big cream card with a picture rule built from the machine's own cutout and
  arrows ("press 1 2 3 4, then the door opens"), a small pencil and a person-shaped sticker (a plain silhouette icon)
  meaning "a person wrote this rule". Under it: "Same every time".
- An AI machine shows its example pile: a tall stack of mini cards fanning out (faces, car trips, spoken words, dog
  pictures, cartoons watched; Content says which are painted) that scrolls up for about 3 s, then three of them light
  up and a dotted line connects what they share (the pattern). Under it: "Learned from lots of examples".
"Try a new one" (on AI machines only): the machine meets something new and guesses from its pattern: usually right,
once in a while funny-wrong (Content). On a rule machine, "Press it again" does exactly the same thing again.
"Back to shelf" (arrow) returns.

### Mode 2: AI or Not? (showdown)
Focus: the machine on the bench under the spotlight at the stage center, then its inside beside it after the reveal;
the row of bulbs is a thin strip at the top. The ten machines come one at a time in a fixed mixed order. For each: the
machine does its job, the narrator asks; the class votes; the teacher taps "AI" (sparkle icon) or "Not AI" (gear
icon). Then "Open it up" reveals the inside as in Machine Shop, and the answer line plays. A row of ten light bulbs at
the top lights gold for a matching guess and stays plain (not red) for a miss; no teams. "Next" (arrow) brings the next
machine. After machine 10: all ten shown as five pairs, each pair with its two insides, and the closing line. "Play
again" (circular arrow) resets.

## Content
Pairs (rule machine first; job shown; inside; Try a new one):
1. Key-code door (art: keypad-door-shut, keypad-door-open): press 1 2 3 4, the door opens. Rule: "Press 1 2 3 4. Then
   open." Wrong code: stays shut. | Face unlock phone (art: face-phone): the phone looks at a face (art: face-owner, on
   its screen) and unlocks. Pile: many faces (art: face-crowd, cut into mini cards); pattern: eyes, nose and mouth in
   their places. New one: the owner wearing a hat (art: face-owner-hat; still unlocks); a cat (art: cat-face; stays
   locked).
2. Talking teddy (art: talking-teddy): squeeze it, it says one of three things ("I love you", "Let's play", "Night
   night"), always one of those three, in turn. Rule card shows the three sound bubbles and an arrow round them. |
   Smart speaker (art: tall-speaker): a child voice asks "What sound does a cow make?" and it answers "A cow says moo."
   Pile: many voices saying many words (sound-wave cards drawn in code); pattern: the sound of the word "cow". New one:
   "What sound does a duck make?" ("A duck says quack."); funny-wrong: "What sound does a cloud make?" ("Hmm, I'm not
   sure about that one.").
3. Elevator (art: elevator): press 3, it goes to floor 3 (the floor number counts up in code on its blank display,
   then a ding). Rule: "Press a number. Go to that floor." | Map app (art: car-screen): picks a way to the park and the
   route (drawn in code on the blank screen) bends around a red traffic jam. Pile: many car trips at many times of day
   (route cards drawn in code); pattern: this street is slow after school. New one: a rainy day trip picks a new way.
4. Camera button (art: camera): press, it takes a picture (a white flash). Rule: "Press. Take a picture." | Photo
   finder (art: laptop): you tap "dog" and it pulls every dog photo from a pile of photos. Pile: many pictures labeled
   dog and not dog (art: photo kit, labels in code); pattern: four legs, ears, a tail. New one: a new puppy photo
   (found); funny-wrong: a fluffy mop (it guesses dog, the class laughs: AI can be wrong).
5. TV remote (art: tv-remote beside retro-tv): press 5, channel 5 (the number shows in code on the blank TV screen).
   Rule: "Press a number. Show that channel." | Video app (art: kid-tablet) picks the next cartoon. Pile: what lots of
   kids watched, and what they watched next (art: cartoon kit); pattern: kids who watched one dinosaur show often watch
   another. New one: after a space cartoon, it suggests another space cartoon.
Showdown order (mixed so the class can't just alternate): face unlock, teddy, elevator, photo finder, map app,
key-code door, camera button, smart speaker, video app, TV remote (AI, rule, rule, AI, AI, rule, rule, AI, AI, rule).
Words on screen for the teacher: "AI (artificial intelligence): a computer that learned patterns from lots of examples
and uses them to guess." "Rule: steps a person wrote; the machine does the same thing every time."
Teacher note shown under "Open it up" the first time: "Real machines can mix both. In this tool each machine is the
kind shown."

## Interactions in detail
- Machine jobs are short (2 to 4 s) animations with synthesized sounds (beeps, a door creak, an elevator ding, a
  shutter click); the teddy squashes in code when squeezed; the teddy's and the speaker's words are fixed lines in the
  same bank voice (see Voice).
- Controls stay live while a job or the pile scroll plays. Open it up during a job finishes the job at once and opens
  the machine; Try a new one or Press it again during the pile scroll stops it at once; Back to shelf or another
  machine stops everything at once. In AI or Not? Open it up stays disabled (dimmed) until a vote is tapped; the vote
  buttons are live during the job.
- A vote can be changed until Open it up is pressed. After the reveal the bulb lights or not; Next appears.
- Motion off shows the pile as a still fan with the three pattern cards outlined, same timing.
- Try a new one cycles through that machine's new examples in order, then starts over.
- Machine Shop and AI or Not? keep their own state for the page load. Nothing saved except the kit settings.
- Keyboard: Tab order mode buttons, header, shelf machines (or vote buttons), Open it up, Try a new one, Next or Back.
  A and N keys vote AI and Not AI in the showdown.
- Sizes: the machine, the vote buttons and Open it up visible without scrolling at every size; at 680x425 the shelves
  become one scrolling row of 64 px machine tiles and the bench fills the stage.

## Look
- Band K-2, own `:root`: `--paper #f6f7fb`, `--ink #1a2233`, `--muted #545d70`, `--line #dde1ec`, `--brand #1e3a5f`
  (steel navy, the accent; header), spotlight gold `--gold #ffd84d` for bulbs, Open it up and the AI vote,
  `--focus #c2410c` with a white inner ring.
- Scene (asked of the painter): warm wood bench and shelves, a blue-grey pegboard wall; spotlight cone in code (white
  14 percent). Rule cards are cream `#fff8e6` with ink; example piles are white mini cards with navy outlines.
- Neighbors: teach-the-robot grape, computer-builder cobalt, robot-dance magenta, loop-garden green; siblings post red,
  gym orange, evergreen, teal blue, charcoal amber. Dark steel navy with spotlight gold is new; it is much darker and
  greyer than computer-builder's cobalt.
- Contrast (computed): white on header 11.5:1; ink on paper 14.85:1; muted on paper 6.17:1; brand on paper 10.74:1;
  ink on gold 11.5:1; gold on navy 8.32:1; focus on paper 4.84:1. AI and Not AI differ by icon and word too.

## Art
Local FLUX (`scripts/localart.py`) unless marked people; one flat, bright picture-book style, asked for in one session.
- workshop: "A cozy cartoon workshop, a blue-grey pegboard wall with hooks, a long bare wooden workbench across the
  bottom, warm light pooling in the middle, flat bright picture-book illustration"; 16:9; cutout no; people no; stage
  backdrop.
- shelf: "A single plain wooden wall shelf with two metal brackets, seen straight on, flat bright picture-book
  illustration, plain white background"; 4:1; cutout yes; people no; used twice for the two shelves.
- Machine kit (12 pieces, one prompt: "A single [machine], front view, bright friendly colors, flat bright
  picture-book illustration, plain white background"); 1:1 unless noted; cutout yes; people no; on the shelves and the
  bench, and small on the rule cards and the end screen. Every screen, display and key is blank so code can draw on it:
  keypad-door-shut (a blue front door with a small number keypad of blank keys beside the handle; 3:4),
  keypad-door-open (the same door swung open; 3:4), face-phone (a phone standing upright with a blank dark screen and a
  small camera dot), talking-teddy (a soft brown teddy bear sitting, a round speaker patch on its tummy), tall-speaker
  (a tall fabric-covered cylinder smart speaker with a blank glowing band near the top), elevator (an elevator front
  with shiny closed doors, a blank display above and a panel of round blank buttons; 3:4), car-screen (a car dashboard
  with a large blank navigation screen and the top of a steering wheel), camera (a chunky red camera with a big shutter
  button), laptop (an open silver laptop with a blank screen), retro-tv (a chunky retro television with rounded
  corners, wooden sides and a blank screen), tv-remote (a TV remote with rows of round blank buttons; 3:4), kid-tablet
  (a tablet in a chunky green rubber case with a blank screen).
- face-owner: "A cheerful child's face, head and shoulders, looking straight ahead, flat bright picture-book
  illustration, plain pale background"; 1:1; cutout no; people: true (Gemini, `scripts/art.py`, Cory reviews); on the
  face phone's screen when it unlocks, and the first card in its pile.
- face-owner-hat: the same child wearing a red knit hat; 1:1; cutout no; people: true (Gemini, Cory reviews); Try a
  new one.
- face-crowd: "A neat four by three grid of small head-and-shoulders portraits of different smiling people of many ages
  and skin tones, flat bright picture-book illustration"; 4:3; cutout no; people: true (Gemini, Cory reviews); cut along
  the grid into the face phone's twelve mini cards.
- cat-face: "A curious tabby cat's face looking straight ahead, flat bright picture-book illustration, plain pale
  background"; 1:1; cutout no; people no; Try a new one (stays locked).
- Photo kit (7 pieces, one prompt: "A square snapshot of [subject], flat bright picture-book illustration, soft plain
  background"); 1:1; cutout no; people no; the photo finder's pile and its new ones: photo-beagle, photo-poodle,
  photo-spotted-dog, photo-cat (a sleeping cat), photo-ball (a red ball on grass), photo-puppy (a fluffy golden puppy),
  photo-mop (a fluffy grey mop head on a stick, shaggy like a dog).
- Cartoon kit (5 pieces, one prompt: "A cheerful scene from a children's cartoon show, [scene], flat bright
  picture-book illustration"); 16:9; cutout no; people no; the video app's pile thumbnails and its pick: cartoon-dino-a
  (a friendly green dinosaur in a jungle), cartoon-dino-b (two baby dinosaurs hatching from eggs), cartoon-space-a (a
  little rocket flying past a ringed planet), cartoon-space-b (a round green alien waving from the moon), cartoon-ocean
  (a smiling whale in blue water).
Rule cards, sound-wave and route mini cards, the spotlight, bulbs, labels, numbers, screen contents and preview.svg
(face unlock phone opened beside a key-code door, built from the cutouts) are drawn in code. 30 images, 3 with people.

## Voice
Bank voice `curious-librarian` (Aoede), "Say curiously and warmly, like a friendly school librarian": wonder about
what is inside each machine. Not used by a neighbor (teach-the-robot playful-friend, robot-dance lively-host,
computer-builder bright-teacher, loop-garden hero-coach) or a sibling. `Curio.voice`, `scope: () => state.mode`. Read
speaks `#hint`. Every line below is fixed text.
How (spoken the first time its moment comes, then hint only):
1. w-shop (Machine Shop entered; stale on the first machine tap): "Welcome to the Machine Shop! Some machines follow
   rules. Some learned from lots of examples. That's AI."
2. pick (queued after 1; stale on the first machine tap): "Tap a machine on the shelf to see what it does."
3. open (first job in Machine Shop ends; stale on Open it up): "Now tap Open it up to look inside."
4. try-new (first AI machine opened in Machine Shop; stale on Try a new one): "AI machines can try something new. Tap
   Try a new one."
5. again (first rule machine opened in Machine Shop; stale on Press it again): "A rule machine does the same thing
   every time. Tap Press it again."
6. back (after the first Try a new one or Press it again; stale on Back to shelf): "Tap Back to shelf to pick another
   machine."
7. w-show (AI or Not? entered; stale on the first vote): "Let's play AI or Not! Watch the machine. Then vote with your
   hands."
8. vote (first showdown job starts, after 7; stale on a vote): "Sparkle hands if you think it's AI. Fists if it follows
   a rule. Then tap AI or Not AI."
9. open-show (first vote tapped; stale on Open it up): "Now tap Open it up!"
10. next (first showdown reveal line ends; stale on Next): "Tap Next for the next machine."
Machine lines (event, when the machine does its job; stale when another machine is chosen):
11. "A door with number buttons." 12. "A phone that opens when it sees your face." 13. "A teddy bear that talks when you
squeeze it." 14. "A speaker that answers questions." 15. "An elevator." 16. "A map that finds a way to the park."
17. "A camera button." 18. "A photo finder that finds all the dog pictures." 19. "A TV remote." 20. "A video app that
picks the next cartoon."
In-machine voices (event, as the job or new one plays; stale when another machine is chosen):
21. "I love you!" 22. "Let's play!" 23. "Night night!" 24. "What sound does a cow make?" 25. "A cow says moo."
26. "What sound does a duck make?" 27. "A duck says quack." 28. "What sound does a cloud make?" 29. "Hmm, I'm not sure
about that one."
Try a new one (event, each time that new one plays; stale on the next tap):
30. (hat) "It still knows your face, even in a hat!" 31. (cat) "A cat! That face doesn't match, so it stays locked."
32. (rain) "Rain makes the roads slow. It picks a new way." 33. (puppy) "A new puppy! It never saw this one, but it
found it." 34. (mop) "Uh oh! It guessed dog, but that's a mop. AI guesses from patterns, and sometimes it's wrong."
35. (space) "You watched a space cartoon. It picks another space cartoon."
Reveals and results (event; stale on Next, Back to shelf or another machine):
36. (Open it up, rule machine) "It's a rule! A person wrote it. It does the same thing every time." 37. (Open it up,
AI machine) "It's AI! It learned a pattern from lots and lots of examples." 38. (vote matched) "You spotted it!"
39. (vote missed) "Tricky one! Let's look again." 40. (Press it again) "It does exactly the same thing again. That's a
rule." 41. (after machine 10; stale on Play again) "That's all ten! Rules come from people. AI learns patterns from
examples. Tap Play again to play once more."
Which line when: Machine Shop: the job line (11 to 20) with its in-machine voice, 3 the first time; on Open it up, 36
or 37, then 4 or 5 the first time. Showdown: the job line, 8 the first time; vote; 9 the first time; on Open it up, 36
or 37, then 38 or 39; 10 the first time.

## Family engine
none.

## Sources
- CSTA 2026 ids from data/standards/csta-2026-ids.txt; CSTA 2017 1A-IC-16: https://csteachers.org/k12standards/
- AI4K12 Five Big Ideas, Big Idea 3 "Learning: computers can learn from data": https://ai4k12.org/
- Face unlock learned from examples: Apple Platform Security, "Face ID security" (neural networks trained on over a
  billion images): https://support.apple.com/guide/security/sece151358d1/web
- Map routes from learned traffic patterns: Google, "Google Maps 101: How AI helps predict traffic and determine routes"
  (2020): https://blog.google/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/
- Speech recognition learned from recorded speech: Hinton et al., "Deep Neural Networks for Acoustic Modeling in Speech
  Recognition", IEEE Signal Processing Magazine 29(6), 2012.
- Recognizing objects in photos learned from labeled pictures: Krizhevsky, Sutskever and Hinton, "ImageNet
  Classification with Deep Convolutional Neural Networks", NeurIPS 2012.
- Video recommendations learned from what people watched: Covington, Adams and Sargin, "Deep Neural Networks for
  YouTube Recommendations", RecSys 2016.
- Rule machines (keypad lock, elevator, camera button, remote, a three-phrase toy) and all scenes are simplified,
  original to Curio Class; the teacher note says real products can mix rules and AI.
- Checks run (Python, 2026-10-29): the showdown order holds 5 AI and 5 rule machines, each pair is one rule and one AI,
  and no kind comes more than twice in a row; every contrast ratio in Look recomputed with the WCAG 2.1 formula and
  matches.

## Done when
1. Machine Shop: all ten machines do their job and open to the right inside (rule card or example pile).
2. Try a new one gives each AI machine's examples in order with lines 30 to 35 and 26 to 29, including the mop and the
   cloud question; Press it again repeats a rule machine exactly.
3. AI or Not?: ten machines in the listed order; votes can change before the reveal; bulbs light only on a match; no
   red, no buzzer; the end screen shows five pairs.
4. Focus: at 1366x768 and 680x425 the machine on the bench is the largest thing at the stage center, and after Open it
   up its inside sits beside it at the same size; the bulbs and shelves stay small.
5. Tap while it plays: Open it up mid-job opens at once; Try a new one or Back to shelf mid-scroll acts at once; a vote
   during a job is recorded at once; no stale line plays afterwards.
6. Every size in STANDARDS.md: machine, vote buttons and Open it up visible without scrolling; 60 px targets.
7. Voice: how lines once each; job, in-machine, new-one and reveal lines every time and dropped when stale; line 9
   never plays before a vote (Open it up is disabled until then); Read and Sound rules pass with held clicks.
8. Keyboard (Tab, Enter, A, N) plays the whole showdown with visible focus.
9. Motion off keeps timing (still pile fan); console clean through both modes.

## Open questions
- Three images show people (the phone owner, the owner in a hat, and the grid of faces), all waiting on Cory. The face
  is the point of face unlock, so they stay people; fine, or should the owner be shown another way?
- The first draft had no spoken lines for the hat, cat, rainy day, puppy and space new ones; lines 30 to 33 and 35 were
  added so every example a K-2 class sees is voiced.
