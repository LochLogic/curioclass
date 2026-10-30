# Input or Output?

## One idea
Stick a sticky note over any part of four everyday gadgets and run its job: cover an input and the gadget can't find
out what you want, cover an output and the gadget still does the job but you can't see or hear it, so "input" and
"output" become "who can't tell: the gadget, or us?".

## Not like
- computer-builder (1, built): put desktop computer parts on a desk to give the computer powers, and find the
  unplugged part. It never teaches the words input and output and stays on a desktop computer. Here there is no desk or
  building: four everyday gadgets (tablet, game controller, smart speaker, microwave), the words input and output on
  screen and spoken, parts that are both (the touchscreen), and the class predicts before each covered run.
- spot-the-ai (1, this group): how a machine decides (rule or learned pattern). Here the "think" chip is a plain box;
  the question is what goes in and comes out.
- teach-the-robot (2), loop-garden (2): AI training and repeat blocks; no hardware.
- traffic-light-coder (3, this group): sensors appear there as rule chips; here sensors are the inputs you can cover.

## Who and how
- Grade 2, computer science. Module: Input and Output (Systems and Security).
- Topic line: computer inputs and outputs
- Driver: teacher on a projector; the class predicts out loud or with thumbs, a helper taps parts.
- 10 to 20 minutes. tool.json: driver "teacher", minutes "10-20", modes ["Try It", "Cover It"], grades_label "Grade 2".
- Standards (CSTA 2026 ids from the module): E2-SYS-HW-11 (hardware). E2-SYS-SE-12 (online actions have consequences)
  is not covered by this tool (secret-keeper and internet-journey carry that thread). 2017 crosswalk: 1A-CS-02 (name
  common hardware and what it does), 1A-CS-03 (describe basic hardware problems).
- Reads nothing: icons on every control, every fixed line voiced, 60 px targets (part hotspots 72 px).

## Screens and modes
Header (kit): title "Input or Output?", small line "In, think, out"; mode buttons "Try It" (pointing finger) and
"Cover It" (sticky note); Motion, Sound, Read.

Stage (painted gadgets on a painted counter, diagram parts in code, re-laid per size; see Art):
- The gadget, big, on the counter (art: kitchen-counter): one of Tablet, Game set (controller plus a small TV), Smart
  speaker, Microwave. Its parts have round hotspots (code rings) that pulse softly until tried once. Screens and
  displays are blank in the paintings; what they show is drawn in code.
- A cutaway outline (code) over the gadget shows thin wires as soft lines from every part to the Think chip (a small
  square chip with a bump-face of dots, no character, code). Parts that sit inside (buzz motor, door switch, heater)
  are small painted cutouts shown in the cutaway.
- Info dots (code): blue dots travel along wires from an input into the chip; orange dots travel from the chip out to
  an output. Dots are the main visual: direction is the meaning (also shown by arrowheads).
- The In, Think, Out board (code): three columns, "IN (input)" with an arrow pointing into a chip, "THINK" with the
  chip, "OUT (output)" with an arrow pointing out. Each part tried drops its small picture tile (a crop of the painted
  gadget at that part, or the inside-part cutout) into its column. The touchscreen tile lands in both IN and OUT,
  joined by a little bridge.
Panel:
- `#hint`.
- Gadget picker: four 72 px tiles showing the gadget cutouts (tablet, controller, speaker, microwave).
- The job button for the current gadget, big (`.big-btn.gold`): "Video call" (phone icon), "Jump!" (up arrow),
  "Play a song" (music note), "Warm the soup" (bowl with steam).
- Cover It only: "Sticky note" (yellow square icon, a toggle: the next tapped part gets covered), "Peel off" (removes
  the note), and the prediction pair: "The gadget can't tell" (the gadget icon with a question mark) and "We can't
  tell" (an eye and an ear with a question mark).

### Mode 1: Try It (explore, opens first, with the tablet)
Focus: the gadget with its hotspots and moving dots, the largest thing at the stage center; the board sits beside it
in wide layouts and under it in tall ones, never larger than the gadget.
Tap a part: it does its own small thing and the dots show the direction (Content), and its tile drops into the board.
Press the job: the whole flow runs in order: inputs light and send blue dots in, the chip blinks, outputs light as
orange dots arrive. Every gadget's parts can be tried in any order; no score. When all of a gadget's parts are in the
board, a small "all found" check appears on its picker tile.

### Mode 2: Cover It (predict)
Focus: the gadget with the yellow note on it at the stage center; after a covered job, the result card sits where the
board was, beside the gadget, so the stuck dots or the hidden effect stay in view.
Pick a gadget; its board is shown already filled (or as filled so far). Tap Sticky note, then tap a part: the note
(art: sticky-note) slaps over it (a soft paper sound). Before the job runs, the class predicts: tap "The gadget can't
tell" or "We can't tell". Then press the job. Covered input: the blue dots stop at the note, the chip shows a question
mark, and the job gets stuck at that point. Covered output: the job runs, the orange dots disappear under the note, and
the effect is hidden (sound muffled to nothing, light hidden). The touchscreen covered: both. The result card says
which it was and the line explains. Prediction is optional: pressing the job without one just runs it.

## Content
Parts (name spoken; kind; tapping it in Try It; covered in Cover It):

Tablet (art: tablet). Job "Video call": your friend Otter (art: otter-call) appears on screen and waves and says
hello; your face square in the corner shows the class (art: class-wave).
- Touchscreen: both. Tap: a finger ripple goes in (blue), the screen lights (orange). Covered: you can't tap Call and
  can't see the call. (Both: the gadget and we can't tell.)
- Camera: input. Tap: the camera dot sends a picture in; your face square appears. Covered: Otter sees a dark square
  ("Where are you?").
- Microphone: input. Tap: sound waves go in. Covered: Otter's ear has a question mark; your words never arrive.
- Speaker: output. Tap: a short hello comes out. Covered: Otter's mouth moves, but no sound.
Game set (art: game-controller, game-tv). Job "Jump!": the hero (art: hero-fox) runs right and jumps a log (art:
game-log) on the TV over a simple game ground drawn in code, lands, the controller buzzes (shake lines in code).
- Joystick: input. Covered: the hero can't move.
- Jump button: input. Covered: the hero runs into the log and stops.
- Buzz motor: output (a little motor that shakes the controller; art: buzz-motor in the cutaway). Covered: the game
  works, but your hands feel nothing (the shake lines are hidden).
- TV screen: output. Covered: the game plays, but we can't see it (only the sound).
Smart speaker (art: puck-speaker). Job "Play a song": a child voice says "Play a song"; the light ring (code, over the
painted blank band) spins; "Twinkle, Twinkle, Little Star" plays (synthesized, public-domain melody).
- Microphone: input. Covered: the light ring stays dark and nothing plays: it never heard you.
- Volume button: input. Covered: the song plays, but you can't make it louder (the plus press does nothing).
  (Covering an input that this job doesn't need is a good surprise: the job works.)
- Speaker: output. Covered: the light ring shows it heard you and the notes pile up behind the note; no sound.
- Light ring: output. Covered: the song plays, but we can't see that it was listening.
Microwave (art: microwave-open, swapped for microwave-shut when the door closes; soup-bowl inside). Job "Warm the
soup": close the door, press 3 0 Start, the display (code, on the blank display) counts 0:30 to 0:00 shown 6 times
faster (5 s), the inside light is on, the heater warms (steam in code), then beep beep beep.
- Keypad: input. Covered: it can't tell how long, so nothing starts.
- Door switch: input (it feels when the door is shut; art: door-switch in the cutaway). Covered: the microwave can't
  tell the door is shut, so it will not start: a safety rule, it never heats with the door open.
- Display: output. Covered: it heats; we can't see the time.
- Beeper: output. Covered: it finishes; we don't hear that it's done (the soup sits).
- Inside light: output. Covered: it heats; we can't see the soup.
- Heater: output (the part that makes the microwaves that warm food; art: heater in the cutaway). Tap only; it is
  inside, so it can't be covered (the note bounces off with a "That part is inside" line).
Words on screen: "Input: how a gadget finds things out." "Output: how a gadget shows us or does things."

## Interactions in detail
- One note at a time: covering another part moves the note. Peel off removes it. Switching gadget peels it off.
- Jobs run about 4 to 6 s. Every control stays live while a job runs and responds at once: the job button restarts the
  job from the start; a gadget tile switches gadget and stops the job; in Try It a part tap stops the job and plays
  that part; in Cover It, Sticky note, Peel off or a prediction button stops the job at once (no result card) and the
  class presses the job again.
- Prediction check: input covered and "The gadget can't tell": match; output covered and "We can't tell": match;
  touchscreen covered: either prediction matches, and the result says both. A match gets a soft chime and line; a miss
  gets the "Let's look" line, never a buzzer. No score is kept.
- The volume button note case: the job works, the result card says "The job didn't need that input."
- Try It tiles: each part's tile drops in once; tapping a tried part again replays its little effect only.
- Each mode keeps its state per gadget for the page load. Nothing saved except the kit settings. No real microphone or
  camera is ever used: everything is pretend and pictured.
- Keyboard: Tab order mode buttons, header, gadget tiles, job, Sticky note, Peel off, prediction buttons, then part
  hotspots. Enter taps.
- Motion off: dots are drawn as a still dotted trail with arrowheads for the same time, the note appears without the
  slap, the hero jumps between three still positions; timing and sound the same.
- Sizes: the gadget with all hotspots, the job button and the prediction buttons visible without scrolling at every
  size; at 680x425 the board shrinks to three icon columns beside the gadget.

## Look
- Band K-2, own `:root`: `--paper #f3f9fb`, `--ink #132a31`, `--muted #4c636b`, `--line #d3e5ea`, `--brand #0e6f86`
  (teal blue, the accent; header), input blue `#1f5fbf`, output orange `#b8500b`, sticky note `#ffe066`,
  `--focus #c2410c` with a white inner ring, `--gold #ffd23f` for the job button.
- Scene (asked of the painter): a pale tiled kitchen wall and a light wood counter, gadgets in silver, white and soft
  greys, so the blue and orange dots stand out.
- Neighbors: computer-builder cobalt, loop-garden green, teach-the-robot grape, score-keeper raspberry,
  internet-journey violet; siblings post red, gym orange, evergreen, steel navy, charcoal amber. Teal blue on a light
  kitchen counter is new among them.
- Contrast (computed): white on header 5.77:1; ink on paper 14.08:1; muted on paper 5.98:1; brand on paper 5.43:1;
  input blue text on paper 5.73:1; output orange text on paper 4.71:1 (20 px or more); white on input blue 6.09:1;
  white on output orange 5.01:1; ink on sticky note 11.48:1; focus on paper 4.87:1. In and out also differ by arrow
  direction and column, not only color.

## Art
Local FLUX (`scripts/localart.py`) unless marked people; one flat, bright picture-book style, asked for in one session.
Every screen, display and light band is painted blank so code can draw on it.
- kitchen-counter: "A bright kitchen corner seen straight on, a pale blue tiled wall and a long clear light wood
  counter across the lower third, soft daylight, flat bright picture-book illustration"; 16:9; cutout no; people no;
  stage backdrop.
- tablet: "A plain silver tablet standing upright, a large blank dark screen, a small camera dot at the top edge, a
  tiny microphone hole and a speaker grille along the bottom edge, flat bright picture-book illustration, plain white
  background"; 4:3; cutout yes; people no; the tablet gadget and its picker tile.
- otter-call: "A friendly cartoon otter waving hello, head and shoulders, plain soft blue background, flat bright
  picture-book illustration"; 1:1; cutout no; people no; inside the tablet screen during the call.
- class-wave: "A happy group of young children waving at the camera in a bright classroom, flat bright picture-book
  illustration"; 4:3; cutout no; people: true (Gemini, `scripts/art.py`, Cory reviews); the "your face" square.
- game-controller: "A chunky blue game controller seen from above, a joystick on the left and one big round red button
  on the right, flat bright picture-book illustration, plain white background"; 4:3; cutout yes; people no.
- game-tv: "A slim flat-screen TV on a low wooden stand with a blank dark screen, flat bright picture-book
  illustration, plain white background"; 16:9; cutout yes; people no; the game set's screen (game drawn on it in code).
- hero-fox: "A small cute cartoon fox running, side view, a video game hero, flat bright picture-book illustration,
  plain white background"; 1:1; cutout yes; people no; runs and jumps on the TV (arc in code).
- game-log: "A short cartoon log lying on its side, flat bright picture-book illustration, plain white background";
  4:1; cutout yes; people no; the obstacle on the TV.
- puck-speaker: "A round puck-shaped smart speaker, a blank pale band around its top edge, a fabric grille on its side,
  a tiny microphone hole and a small plus button, flat bright picture-book illustration, plain white background"; 1:1;
  cutout yes; people no; light ring drawn in code on the band.
- microwave-open: "A white microwave oven with its glass door swung open, an empty inside with a round glass plate, a
  blank display and a keypad of blank buttons on the right, flat bright picture-book illustration, plain white
  background"; 4:3; cutout yes; people no.
- microwave-shut: the same microwave with the door closed; 4:3; cutout yes; people no; swapped in when the door shuts.
- soup-bowl: "A white bowl of orange soup, flat bright picture-book illustration, plain white background"; 1:1; cutout
  yes; people no; inside the microwave (steam in code).
- Inside-part kit (3 pieces, one prompt: "A single small [part], flat bright picture-book illustration, plain white
  background"); 1:1; cutout yes; people no; shown in the cutaway and as board tiles: buzz-motor (a tiny metal motor
  with an off-center weight on its shaft), door-switch (a small black switch with a metal lever), heater (a metal box
  with cooling fins).
- sticky-note: "A single square yellow sticky note with one corner gently curled, blank, flat bright picture-book
  illustration, plain white background"; 1:1; cutout yes; people no; the note over a covered part.
Hotspot rings, the cutaway outline, wires, dots, the Think chip, the board and its crops, screen contents, labels and
preview.svg (the microwave cutout with a note on its keypad and dots stopping at it) are drawn in code. 16 images, 1
with people.

## Voice
Bank voice `big-sister` (Leda), "Say in a friendly, youthful way, like a helpful older student": an older kid showing
younger ones how gadgets work. Not used by a neighbor here (computer-builder bright-teacher, loop-garden hero-coach,
teach-the-robot playful-friend, score-keeper friendly-dad, internet-journey smooth-narrator) or a sibling.
`Curio.voice`, `scope: () => state.mode`. Read speaks `#hint`. Every line below is fixed text.
How (spoken the first time its moment comes, then hint only):
1. w-try (Try It entered; stale on the first part tap): "Every gadget takes things in, thinks, and gives things out.
   Let's look inside!"
2. tap-part (queued after 1; stale on the first part tap): "Tap a part to see which way the dots go. Blue dots go in.
   Orange dots come out."
3. job (after the first part's effect; stale on the job button): "Now press the big gold button to run the whole job."
4. gadget (first job in Try It ends; stale on a gadget tile): "Tap a gadget picture to try another one."
5. w-cover (Cover It entered; stale when a note lands): "Let's cover a part with a sticky note and see what happens."
6. cover (queued after 5; stale when a note lands): "Tap Sticky note, then tap a part."
7. guess (first note lands; stale on a guess or the job button): "Who can't tell now, the gadget or us? Tap The gadget
   can't tell, or We can't tell. Then press the big gold button."
8. again (first result line ends; stale on Sticky note, Peel off or a gadget tile): "Tap Sticky note to cover a new
   part, or Peel off to take it away."
Part names (event, on tap in Try It; stale on the next tap): 9. "Touchscreen. It's an input and an output!"
10. "Camera. Input." 11. "Microphone. Input." (tablet and speaker) 12. "Speaker. Output." (tablet and speaker)
13. "Joystick. Input." 14. "Jump button. Input." 15. "Buzz motor. Output. It shakes the controller." 16. "TV screen.
Output." 17. "Volume button. Input." 18. "Light ring. Output." 19. "Keypad. Input." 20. "Door switch. Input. It feels
when the door is shut." 21. "Display. Output." 22. "Beeper. Output." 23. "Inside light. Output." 24. "Heater. Output.
It warms the food."
In-gadget voices (event; stale when the job stops or the gadget changes): 25. Otter: "Hello!" (speaker tapped, or the
call job when the speaker is not covered) 26. Otter: "Where are you?" (call job with the camera covered) 27. "Play a
song." (the song job; spoken even when the microphone is covered, which is the point)
Results (event, after a covered job; stale when the note moves, a new job starts or the gadget changes):
28. "You covered an input. The gadget can't find out what it needs, so it's stuck."
29. "You covered an output. The gadget still did the job. We just can't see or hear it."
30. "The touchscreen is both! Now the tablet can't feel your finger, and we can't see the screen."
31. "The microwave can't tell the door is shut, so it won't start. That keeps you safe."
32. "The job didn't need that input, so it still worked."
33. "Your guess was right!" 34. "Let's look at the dots again."
35. (heater tapped with Sticky note on) "That part is inside. We can't cover it, but it's an output: it warms the
food."
36. (Try It, last part of a gadget found; stale on the next tap) "You found every part on this gadget!"
Which line when: covered job: 33 or 34 (if predicted), then 28, 29, 30, 31 or 32, then 8 the first time. Door switch
gives 31, volume button 32, touchscreen 30, other inputs 28, other outputs 29.

## Family engine
none.

## Sources
- CSTA K-12 CS Standards (2017) 1A-CS-02, 1A-CS-03: https://csteachers.org/k12standards/ ; 2026 ids from
  data/standards/csta-2026-ids.txt.
- Input and output definitions, touchscreen as both: Code.org CS Fundamentals glossary (input, output):
  https://code.org/curriculum/docs/k-5/glossary ; BBC Bitesize KS2 Computing, "Input and output devices":
  https://www.bbc.co.uk/bitesize/topics/zf2f9j6
- Microwave door interlocks stop the microwaves when the door opens, and the magnetron makes the microwaves: US FDA,
  "Microwave Oven Radiation": https://www.fda.gov/radiation-emitting-products/resources-you-radiation-emitting-products/microwave-oven-radiation ;
  21 CFR 1030.10 (safety interlocks): https://www.ecfr.gov/current/title-21/chapter-I/subchapter-J/part-1030/section-1030.10
- "Twinkle, Twinkle, Little Star": melody "Ah! vous dirai-je, maman" (France, 1761), public domain.
- Gadget scenes and job scripts are simplified and original to Curio Class.
- Checks run (Python, 2026-10-29): the microwave's 30 s countdown at 6 times speed takes 5.0 s, inside the 4 to 6 s job
  length; 17 coverable parts plus the heater, each mapped to one result line (8 inputs to 28 except door switch 31 and
  volume button 32, 8 outputs to 29, touchscreen 30); the first draft counted 17 distinct part lines, but the
  speaker's microphone and speaker repeat the tablet's, so there are 16 (9 to 24); every contrast ratio in Look
  recomputed with the WCAG 2.1 formula and matches.

## Done when
1. Try It: every part of all four gadgets plays its effect with dots in the right direction and drops its tile in the
   right column (touchscreen in both).
2. Each job runs its full flow; all parts found shows the check and line 36.
3. Cover It: every coverable part gives the covered result in Content; the heater refuses the note; volume button
   gives line 32.
4. Predictions match or miss by the rule in Interactions; no score anywhere.
5. Focus: at 1366x768 and 680x425 the gadget with its dots is the largest thing at the stage center, and the result
   card never covers it.
6. Tap while it plays: mid-job, the job button restarts at once, a part tap (Try It) plays that part at once, a gadget
   tile switches at once, and Sticky note or Peel off (Cover It) stops the job with no result card and no stale line.
7. Every size in STANDARDS.md: gadget hotspots, job button and prediction buttons visible without scrolling; 60 px
   targets.
8. Voice: how lines once in five actions; part names, in-gadget voices and results every time and dropped when stale;
   Read and Sound rules pass with held clicks.
9. Keyboard only covers, predicts and runs a job; Motion off keeps timing; no real microphone or camera permission is
   ever requested; console clean.

## Open questions
- class-wave (a class of children waving, the "your face" square on the call) is the one picture with people, waiting
  on Cory. Keep it, or show the class some other way?
