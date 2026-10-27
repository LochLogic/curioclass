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

Stage (drawn in code, re-laid per size):
- The gadget, big, on a plain counter: one of Tablet, Game set (controller plus a small TV), Smart speaker, Microwave.
  Its parts have round hotspots that pulse softly until tried once.
- Thin wires (drawn as soft lines inside a cutaway outline) run from every part to the Think chip (a small square chip
  with a bump-face of dots, no character).
- Info dots: blue dots travel along wires from an input into the chip; orange dots travel from the chip out to an
  output. Dots are the main visual: direction is the meaning (also shown by arrowheads).
- Under the gadget, the In, Think, Out board: three columns, "IN (input)" with an arrow pointing into a chip, "THINK"
  with the chip, "OUT (output)" with an arrow pointing out. Each part tried drops its small picture tile into its
  column. The touchscreen tile lands in both IN and OUT, joined by a little bridge.
Panel:
- `#hint`.
- Gadget picker: four 72 px tiles (tablet, controller, speaker, microwave).
- The job button for the current gadget, big (`.big-btn.gold`): "Video call" (phone icon), "Jump!" (up arrow),
  "Play a song" (music note), "Warm the soup" (bowl with steam).
- Cover It only: "Sticky note" (yellow square icon, a toggle: the next tapped part gets covered), "Peel off" (removes
  the note), and the prediction pair after a cover: "The gadget can't tell" (the gadget icon with a question mark) and
  "We can't tell" (an eye and an ear with a question mark).

### Mode 1: Try It (explore, opens first)
Tap a part: it does its own small thing and the dots show the direction (Content), and its tile drops into the board.
Press the job: the whole flow runs in order: inputs light and send blue dots in, the chip blinks, outputs light as
orange dots arrive. Every gadget's parts can be tried in any order; no score. When all of a gadget's parts are in the
board, a small "all found" check appears on its picker tile.

### Mode 2: Cover It (predict)
Pick a gadget; its board is shown already filled (or as filled so far). Tap Sticky note, then tap a part: a yellow
note slaps over it (a soft paper sound). Before the job runs, the class predicts: tap "The gadget can't tell" or "We
can't tell". Then press the job. Covered input: the blue dots stop at the note, the chip shows a question mark, and the
job gets stuck at that point. Covered output: the job runs, the orange dots disappear under the note, and the effect is
hidden (sound muffled to nothing, light hidden). The touchscreen covered: both. The result card says which it was and
the line explains. Prediction is optional: pressing the job without one just runs it.

## Content
Parts (name spoken; kind; tapping it in Try It; covered in Cover It):

Tablet. Job "Video call": your friend Otter (art) appears on screen and waves; your face square shows a cartoon of the
class (a drawn crowd of round dot-faces).
- Touchscreen: both. Tap: a finger ripple goes in (blue), the screen lights (orange). Covered: you can't tap Call and
  can't see the call. (Both: the gadget and we can't tell.)
- Camera: input. Tap: the camera dot sends a picture in; your face square appears. Covered: Otter sees a dark square
  ("Where are you?").
- Microphone: input. Tap: sound waves go in. Covered: Otter's ear has a question mark; your words never arrive.
- Speaker: output. Tap: a short hello sound comes out. Covered: Otter's mouth moves, but no sound.
Game set. Job "Jump!": the hero (a drawn square fox) runs right and jumps a log on the TV, lands, the controller buzzes.
- Joystick: input. Covered: the hero can't move.
- Jump button: input. Covered: the hero runs into the log and stops.
- Buzz motor: output (a little motor that shakes the controller). Covered: the game works, but your hands feel nothing
  (the shake lines are hidden).
- TV screen: output. Covered: the game plays, but we can't see it (only the sound).
Smart speaker. Job "Play a song": a child voice says "Play a song"; the light ring spins; "Twinkle, Twinkle, Little
Star" plays (synthesized, public-domain melody).
- Microphone: input. Covered: the light ring stays dark and nothing plays: it never heard you.
- Volume button: input. Covered: the song plays, but you can't make it louder (the plus press does nothing).
  (Covering an input that this job doesn't need is a good surprise: the job works.)
- Speaker: output. Covered: the light ring shows it heard you and the notes pile up behind the note; no sound.
- Light ring: output. Covered: the song plays, but we can't see that it was listening.
Microwave. Job "Warm the soup": close the door, press 3 0 Start, the display counts 0:30 to 0:00 (shown 6 times faster),
the light is on, the heater warms (steam), then beep beep beep.
- Keypad: input. Covered: it can't tell how long, so nothing starts.
- Door switch: input (it feels when the door is shut). Covered: the microwave can't tell the door is shut, so it will
  not start: a safety rule, it never heats with the door open.
- Display: output. Covered: it heats; we can't see the time.
- Beeper: output. Covered: it finishes; we don't hear that it's done (the soup sits).
- Inside light: output. Covered: it heats; we can't see the soup.
- Heater: output (the part that makes the microwaves that warm food). Tap only; it is inside, so it can't be covered
  (the note bounces off with a "That part is inside" line).
Words on screen: "Input: how a gadget finds things out." "Output: how a gadget shows us or does things."

## Interactions in detail
- One note at a time: covering another part moves the note. Peel off removes it. Switching gadget peels it off.
- The job button is disabled while a job runs (about 4 to 6 s); parts are not tappable during a job.
- Prediction check: input covered and "The gadget can't tell": match; output covered and "We can't tell": match;
  touchscreen covered: either prediction matches, and the result says both. A match gets a soft chime and line; a
  miss gets the "Let's look" line, never a buzzer. No score is kept.
- The volume button note case: the job works, the result card says "The job didn't need that input."
- Try It tiles: each part's tile drops in once; tapping a tried part again replays its little effect only.
- Each mode keeps its state per gadget for the page load. Nothing saved except the kit Motion setting. No real
  microphone or camera is ever used: everything is pretend and drawn.
- Keyboard: Tab order mode buttons, header, gadget tiles, job, Sticky note, Peel off, prediction buttons, then part
  hotspots. Enter taps.
- Motion off: dots are drawn as a still dotted trail with arrowheads for the same time, the note appears without the
  slap; timing and sound the same.
- Sizes: the gadget with all hotspots, the job button and the prediction buttons visible without scrolling at every
  size; the In, Think, Out board can sit beside the gadget in wide layouts and under it in tall ones; at 680x425 it
  shrinks to three icon columns.

## Look
- Band K-2, own `:root`: `--paper #f3f9fb`, `--ink #132a31`, `--muted #4c636b`, `--line #d3e5ea`, `--brand #0e6f86`
  (teal blue, the accent; header), input blue `#1f5fbf`, output orange `#b8500b`, sticky note `#ffe066`,
  `--focus #c2410c` with a white inner ring, `--gold #ffd23f` for the job button.
- Neighbors: computer-builder cobalt, loop-garden green, teach-the-robot grape, score-keeper raspberry,
  internet-journey violet; siblings post red, gym orange, evergreen, steel navy, charcoal amber. Teal blue on a light
  kitchen counter is new among them.
- Contrast: white on header 5.77:1; ink on paper 14.08:1; muted on paper 5.98:1; brand on paper 5.43:1; input blue
  text on paper 5.73:1; output orange text on paper 4.71:1 (20 px or more); white on input blue 6.09:1; white on output
  orange 5.01:1; ink on sticky note 11.48:1; focus on paper 4.87:1. In and out also differ by arrow direction and
  column, not only color.

## Art
- otter-call: "A friendly cartoon otter waving hello, head and shoulders, as if on a video call, plain soft blue
  background, flat bright style"; 1:1; cutout no; people true (character, Codex scripts/gptart.py, Cory reviews); shown
  inside the tablet screen during the call.
Gadgets, parts, wires, dots, notes, the game hero, the crowd of dot-faces and preview.svg (the microwave with a note on
its keypad and dots stopping at it) are drawn in code. 1 image.

## Voice
Bank voice `big-sister` (Leda), "Say in a friendly, youthful way, like a helpful older student": an older kid showing
younger ones how gadgets work. Not used by a neighbor here (computer-builder bright-teacher, loop-garden hero-coach,
teach-the-robot playful-friend, score-keeper friendly-dad, internet-journey smooth-narrator) or a sibling.
How (once per page load, then hint only):
1. welcome Try It: "Every gadget takes things in, thinks, and gives things out. Let's look inside!"
2. "Tap a part to see which way the dots go. Blue dots go in. Orange dots come out."
3. "Now press the big button to run the whole job."
4. welcome Cover It: "Let's cover a part with a sticky note and see what happens."
5. "Tap Sticky note, then tap a part."
6. "Who can't tell now, the gadget or us? Tap your guess. Then press the big button."
Part names (events, on tap in Try It; stale on the next tap): 7 to 23, one per part: "Touchscreen. It's an input and an
output!", "Camera. Input.", "Microphone. Input.", "Speaker. Output.", "Joystick. Input.", "Jump button. Input.", "Buzz
motor. Output.", "TV screen. Output.", "Microphone. Input." (speaker gadget shares line 9), "Volume button. Input.",
"Light ring. Output.", "Keypad. Input.", "Door switch. Input. It feels when the door is shut.", "Display. Output.",
"Beeper. Output.", "Inside light. Output.", "Heater. Output. It warms the food." (17 distinct lines; the builder
numbers them 7 to 23).
Results (events, after a covered job; stale when the note moves or the gadget changes):
24. "You covered an input. The gadget can't find out what it needs, so it's stuck."
25. "You covered an output. The gadget still did the job. We just can't see or hear it."
26. "The touchscreen is both! Now the tablet can't feel your finger, and we can't see the screen."
27. "The microwave can't tell the door is shut, so it won't start. That keeps you safe."
28. "The job didn't need that input, so it still worked."
29. "Your guess was right!" 30. "Let's look at the dots again."
31. "That part is inside. We can't cover it, but it's an output: it warms the food."
32. "You found every part on this gadget!" (event, Try It)
Which line when: covered job: 29 or 30 (if predicted), then 24, 25, 26, 27 or 28. Read speaks `#hint`.

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
- Gadget drawings and job scripts are simplified and original to Curio Class.

## Done when
1. Try It: every part of all four gadgets plays its effect with dots in the right direction and drops its tile in the
   right column (touchscreen in both).
2. Each job runs its full flow; all parts found shows the check.
3. Cover It: every coverable part gives the covered result in Content; the heater refuses the note; volume button
   gives line 28.
4. Predictions match or miss by the rule in Interactions; no score anywhere.
5. Every size in STANDARDS.md: gadget hotspots, job button and prediction buttons visible without scrolling; 60 px
   targets.
6. Voice: how lines once in five actions; part names and results every time and dropped when stale; Read and Sound
   rules pass with held clicks.
7. Keyboard only covers, predicts and runs a job; Motion off keeps timing; no real microphone or camera permission is
   ever requested; console clean.
