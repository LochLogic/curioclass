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

Stage: a workbench under a warm spotlight (backdrop art: workshop), drawn machines on top, re-laid per size.

Panel: `#hint`, then the mode's controls.

### Mode 1: Machine Shop (explore, opens first)
The ten machines sit on two shelves, paired side by side (pair partners next to each other). Tap a machine: it moves to
the bench and does its job (Content), with sound. Then "Open it up" (screwdriver icon) slides its front off:
- A rule machine shows a rule card: a big card with a picture rule ("press 1 2 3 4, then the door opens") and a small
  pencil and a person-shaped sticker (a plain silhouette) meaning "a person wrote this rule". Under it: "Same every
  time".
- An AI machine shows its example pile: a tall stack of mini cards fanning out (faces, car trips, spoken words, dog
  pictures, cartoons watched) that keeps scrolling up, then three of them light up and a dotted line connects what
  they share (the pattern). Under it: "Learned from lots of examples".
"Try a new one" (on AI machines only): the machine meets something new and guesses from its pattern: usually right,
once in a while funny-wrong (Content). On a rule machine, "Press it again" does exactly the same thing again.
"Back to shelf" (arrow) returns.

### Mode 2: AI or Not? (showdown)
The ten machines come one at a time in a fixed mixed order. For each: the machine does its job, the narrator asks;
the class votes; the teacher taps "AI" (sparkle icon) or "Not AI" (gear icon). Then "Open it up" reveals the inside as
in Machine Shop, and the answer line plays. A row of ten light bulbs at the top lights gold for a matching guess and
stays plain (not red) for a miss; no teams. After machine 10: all ten shown as five pairs, each pair with its two
insides, and the closing line. "Play again" (circular arrow) resets.

## Content
Pairs (rule machine first; job shown; inside; Try a new one):
1. Key-code door (a door keypad): press 1 2 3 4, the door opens. Rule: "Press 1 2 3 4. Then open." Wrong code: stays
   shut. | Face unlock phone: a phone looks at a face (a simple cartoon face drawn in code) and unlocks. Pile: many
   faces; pattern: eyes, nose and mouth in their places. New one: the owner wearing a hat (still unlocks); a cat
   (stays locked).
2. Talking teddy: squeeze it, it says one of three things ("I love you", "Let's play", "Night night"), always one of
   those three, in turn. Rule card shows the three sound bubbles and an arrow round them. | Smart speaker: a child
   voice asks "What sound does a cow make?" and it answers "A cow says moo." Pile: many voices saying many words;
   pattern: the sound of the word "cow". New one: "What sound does a duck make?" ("A duck says quack."); funny-wrong:
   "What sound does a cloud make?" ("Hmm, I'm not sure about that one.").
3. Elevator: press 3, it goes to floor 3. Rule: "Press a number. Go to that floor." | Map app: picks a way to the
   park and the route bends around a red traffic jam. Pile: many car trips at many times of day; pattern: this street
   is slow after school. New one: a rainy day trip picks a new way.
4. Camera button: press, it takes a picture. Rule: "Press. Take a picture." | Photo finder: you tap "dog" and it pulls
   every dog photo from a pile of photos. Pile: many pictures labeled dog and not dog; pattern: four legs, ears, a tail.
   New one: a new puppy photo (found); funny-wrong: a fluffy mop (it guesses dog, the class laughs: AI can be wrong).
5. TV remote: press 5, channel 5. Rule: "Press a number. Show that channel." | Video app picks the next cartoon. Pile:
   what lots of kids watched, and what they watched next; pattern: kids who watched one dinosaur show often watch
   another. New one: after a space cartoon, it suggests another space cartoon.
Showdown order (mixed so the class can't just alternate): face unlock, teddy, elevator, photo finder, map app,
key-code door, camera button, smart speaker, video app, TV remote (AI, rule, rule, AI, AI, rule, rule, AI, AI, rule).
Words on screen for the teacher: "AI (artificial intelligence): a computer that learned patterns from lots of examples
and uses them to guess." "Rule: steps a person wrote; the machine does the same thing every time."
Teacher note shown under "Open it up" the first time: "Real machines can mix both. In this tool each machine is the
kind shown."

## Interactions in detail
- Machine jobs are short (2 to 4 s) animations with synthesized sounds (beeps, a door creak, an elevator ding, a
  shutter click); the teddy's and the speaker's words are fixed lines in the same bank voice (see Voice).
- Open it up is disabled until the job animation ends; in AI or Not? it is disabled until a vote is tapped.
- A vote can be changed until Open it up is pressed. After the reveal the bulb lights or not; "Next" (arrow) appears.
- The example pile scroll is about 3 s; Motion off shows the pile as a still fan with the three pattern cards
  outlined, same timing.
- Try a new one cycles through that machine's new examples in order, then starts over.
- Machine Shop and AI or Not? keep their own state for the page load. Nothing saved except the kit Motion setting.
- Keyboard: Tab order mode buttons, header, shelf machines (or vote buttons), Open it up, Try a new one, Next or Back.
  A and N keys vote AI and Not AI in the showdown.
- Sizes: the machine, the vote buttons and Open it up visible without scrolling at every size; at 680x425 the shelves
  become one scrolling row of 64 px machine tiles and the bench fills the stage.

## Look
- Band K-2, own `:root`: `--paper #f6f7fb`, `--ink #1a2233`, `--muted #545d70`, `--line #dde1ec`, `--brand #1e3a5f`
  (steel navy, the accent; header), spotlight gold `--gold #ffd84d` for bulbs, Open it up and the AI vote,
  `--focus #c2410c` with a white inner ring.
- Scene: workbench wood #b98a5a, wall from the backdrop with a spotlight cone (white 14 percent). Rule cards are cream
  #fff8e6 with ink; example piles are white mini cards with navy outlines.
- Neighbors: teach-the-robot grape, computer-builder cobalt, robot-dance magenta, loop-garden green; siblings post red,
  gym orange, evergreen, teal blue, charcoal amber. Dark steel navy with spotlight gold is new; it is much darker and
  greyer than computer-builder's cobalt.
- Contrast: white on header 11.5:1; ink on paper 14.85:1; muted on paper 6.17:1; brand on paper 10.74:1; ink on gold
  11.5:1; gold on navy 8.32:1; focus on paper 4.84:1. AI and Not AI differ by icon and word too.

## Art
- workshop: "A cozy cartoon workshop wall with pegboard and empty shelves, a wooden workbench across the bottom, warm
  light, no objects on the bench, flat bright illustration"; 16:9; cutout no; people no; Cloudflare FLUX
  (scripts/cfart.py); stage backdrop.
The ten machines, their insides, rule cards, example piles (simple shape faces drawn in code: circles with dot eyes,
no real people), the mop and puppy, and preview.svg (face unlock phone opened beside a key-code door) are drawn in
code. 1 image.

## Voice
Bank voice `curious-librarian` (Aoede), "Say curiously and warmly, like a friendly school librarian": wonder about
what is inside each machine. Not used by a neighbor (teach-the-robot playful-friend, robot-dance lively-host,
computer-builder bright-teacher, loop-garden hero-coach) or a sibling.
How (once per page load, then hint only):
1. welcome Machine Shop: "Welcome to the Machine Shop! Some machines follow rules. Some learned from lots of examples. That's AI."
2. "Tap a machine to see what it does. Then tap Open it up to look inside."
3. "AI machines can try something new. Tap Try a new one."
4. welcome AI or Not?: "Let's play AI or Not! Watch the machine. Then vote with your hands."
5. "Sparkle hands if you think it's AI. Fists if it follows a rule. Then tap the class's vote."
6. "Now tap Open it up!"
Machine lines (events, when the machine does its job; stale when another machine is chosen): 7. "A door with number
buttons." 8. "A phone that opens when it sees your face." 9. "A teddy bear that talks when you squeeze it." 10. "A
speaker that answers questions." 11. "An elevator." 12. "A map that finds a way to the park." 13. "A camera button."
14. "A photo finder that finds all the dog pictures." 15. "A TV remote." 16. "A video app that picks the next cartoon."
In-machine voices (events): 17. "I love you!" 18. "Let's play!" 19. "Night night!" 20. "What sound does a cow make?"
21. "A cow says moo." 22. "What sound does a duck make?" 23. "A duck says quack." 24. "What sound does a cloud make?"
25. "Hmm, I'm not sure about that one."
Reveals (events, on Open it up): 26. "It's a rule! A person wrote it. It does the same thing every time." 27. "It's
AI! It learned a pattern from lots and lots of examples." 28. "You spotted it!" (vote matched) 29. "Tricky one! Let's
look again." (vote missed) 30. "Uh oh! It guessed dog, but that's a mop. AI guesses from patterns, and sometimes it's
wrong." 31. "It does exactly the same thing again. That's a rule." 32. "That's all ten! Rules come from people. AI
learns patterns from examples."
Which line when: showdown machine: its job line (7 to 16), then 5 (how, first time only), vote, 6 (how, first time),
reveal 26 or 27, then 28 or 29. Read speaks `#hint`.

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

## Done when
1. Machine Shop: all ten machines do their job and open to the right inside (rule card or example pile).
2. Try a new one gives each AI machine's examples in order, including the mop and the cloud question; Press it again
   repeats a rule machine exactly.
3. AI or Not?: ten machines in the listed order; votes can change before the reveal; bulbs light only on a match; no
   red, no buzzer; the end screen shows five pairs.
4. Every size in STANDARDS.md: machine, vote buttons and Open it up visible without scrolling; 60 px targets.
5. Voice: welcomes and how lines once; job, reveal and in-machine lines every time and dropped when stale; Read and
   Sound rules pass with held clicks.
6. Keyboard (Tab, Enter, A, N) plays the whole showdown with visible focus.
7. Motion off keeps timing (still pile fan); console clean through both modes.
