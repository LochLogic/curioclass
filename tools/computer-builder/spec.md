# Computer Builder

## One idea
Every computer part has one power: put a part on the desk and the computer gains it (the screen lights up, the speakers sing), leave it off and the class sees and hears exactly what the computer can't do.

## Not like
- robot-dance (K showdown): that is the order of steps and finding the wrong step in a dance. Here there are no steps or sequences; the class reasons about which part does which job.
- bee-bot-garden (1 puzzle): arrow paths on a grid. No grid, no movement commands here.
- loop-garden (2 puzzle, live): repeat blocks and fewer-blocks stars. No code, no stars, no score here.
- input-output-machine (2 sandbox): the student's real key presses, clicks and voice turned into output, with the words "input" and "output". Here nothing reads the real microphone or camera, the words input and output are never taught (only shown as in and out arrows on the cables), and the point is naming parts and matching them to jobs.
- secret-keeper (K sort): private information. This tool leaves account safety (the module's other standard) to another tool.
- pattern-finder, teach-the-robot, class-snack-vote: AI training and voting data; no overlap.

## Who and how
Grade 1, computer science. Driver: teacher on a projector or smartboard; the class answers out loud. 10 to 20 minutes.
Module codes (CSTA 2026, as the module lists): E1-SYS-HW-11 (hardware). E1-SYS-SE-12 (keeping accounts safe) is not
covered by this tool. CSTA K-12 CS Standards (2017) equivalents: 1A-CS-02 (name common hardware and what it does),
1A-CS-03 (describe a hardware problem using the right words, in the Missing mode), 1A-CS-01 (operate devices, lightly).
K-1 reads nothing: every control has an icon, every fixed line is voiced, targets are at least 60 px.

## Screens and modes
Header (kit): title "Computer Builder", three mode buttons with icon plus word: **Build** (wrench), **Jobs**
(clipboard with a star), **Missing** (magnifying glass); then **Motion**, **Sound**, **Read** (ids motion, sound, read).

Stage, the same in every mode: a pale classroom wall (art: backdrop) above a wooden desk drawn in code. The desk has
seven slots, each a dashed ghost outline of its part (shape only, so the class can guess where things go):
camera on a mini tripod (back left), left speaker, screen on a stand (center back), right speaker, computer box (tower,
right), microphone on a little stand (front left), keyboard (front center), mouse (front right). The two speakers are
one part. Bubbles the goldfish (art) sits in a bowl at the far left edge of the desk. Each placed part gets a cable
drawn as a soft curve to the box's back; with no box, cables end in a loose plug lying where the box would be.

Panel (right; below the stage under 760 px wide): the hint paragraph (id hint), then the mode's controls.

**Build (explore, the default mode).** Panel shows the parts shelf: seven picture tiles (part drawing plus its name),
2 columns. Tap a tile: the part flies to its slot (400 ms arc), its cable draws in, it does its little power show and
the narrator names it. Tap the tile again (now marked with a green check and "on desk") or drag the part off the desk:
it flies back to the shelf and its cable retracts. Tap a placed part on the desk to try it (see Interactions). Buttons
under the shelf: **Clear desk** (broom icon, all parts back) and **All in one** (laptop icon; shown but disabled with a
lock until all seven are on the desk; it pulses once when it unlocks).
- All in one view: the desk parts slide together and morph (600 ms) into a big laptop drawing; panel shows **Laptop**
  and **Tablet** (segmented, icons) and **Back to desk** (arrow). Hotspots on the drawing (round, 64 px, softly
  pulsing): screen, keyboard, touchpad, speaker grilles, microphone holes, camera dot, and the hidden brain (tap the
  middle of the base: an x-ray window opens showing a chip). Tablet has: touchscreen, pop-up keyboard (tapping shows an
  on-screen keyboard sliding up), speakers, microphone, camera, brain.

**Jobs (builder test).** Desk starts empty. Panel shows six job cards (picture icons drawn in code, 2 x 3), the shelf
below them, and a big green **Try it!** button (play icon). Pick a job card: it enlarges into a banner at the top of the
stage, the desk clears, the narrator reads the job. The class says which parts it needs; the teacher taps them onto the
desk (same shelf behavior as Build). **Try it!** runs the job. Jobs done get a check mark on their card (no score).
After a success, **Next job** (arrow) appears beside Try it.

**Missing (troubleshooting game).** Desk starts fully built. Panel shows Nibbles' round marker (seven small plug icons,
done ones filled), a big **Start** button (play icon; becomes **Next round** after a round is solved) and nothing else.
Start: a starry blanket drops over the desk ("Close your eyes!"), Nibbles the cartoon mouse (art) scurries behind the
desk, the blanket lifts ("Open your eyes!"), and the computer tries that round's job by itself. Something fails. The
class says which part is unplugged; the teacher taps that part on the desk.

## Content
Parts (name on tile; shelf order): computer box, screen, keyboard, mouse, speakers, microphone, camera.
In or out (cable dot direction when the part works): keyboard, mouse, microphone, camera send dots IN toward the box
(teal circles); screen and speakers get dots OUT from the box (orange stars). The box itself blinks its lights.

Try-it shows in Build (each needs the box; the show runs when the part is tapped on the desk):
- Box: power light and three little lights blink in turn, a gear spins in a window on its side, low hum (Curio.tone 110 Hz, 0.4 s).
- Screen: lights up showing a desktop drawn in code (sky gradient, four round icons: paintbrush, music note, camera, ABC).
- Keyboard: the next key of H, E, L, L, O presses down (key highlight), click tone, the letter appears big on the screen;
  after O the word stays 2 s, then clears. Real keyboard letters A to Z typed by the teacher also show (up to 10, then clear).
- Mouse: the mouse slides on the desk, an arrow on the screen follows a curve and leaves a rainbow stroke; three
  taps make three strokes, the fourth clears.
- Speakers: cones pulse, a 5-note tune (C5 E5 G5 E5 C6, 0.18 s each), music notes float out of both speakers.
- Microphone: "Everyone, say hello!", then a sound wave bounces on the mic for 2.5 s (animated, not listening), then the
  speakers answer "Hello, class!" (narrator line, as the computer's voice) and, if the screen is there, a speech bubble
  with a waving hand icon appears on it.
- Camera: a flash, a shutter click (two short tones), and the screen shows the art "bubbles-photo" in a white frame.

Jobs (card icon; parts needed; the full run when it works):
1. Watch a cartoon (TV icon): box, screen, speakers. A sun bounces over green hills on the screen for 4 s with the tune.
2. Write a word (pencil and ABC): box, keyboard, screen. HELLO types itself letter by letter on the screen.
3. Paint a picture (paintbrush): box, mouse, screen. The arrow paints a rainbow and a sun on the screen.
4. Say hello to the computer (waving hand): box, microphone, speakers. Wave on the mic, then "Hello, class!" from the speakers.
5. Take a picture of Bubbles (camera and fish): box, camera, screen. Flash, then the photo on the screen.
6. Video chat with the panda at the zoo (panda face): box, camera, microphone, screen, speakers. The panda art waves on
   the screen, a soft squeak plays, the camera light glows and the mic wave bounces.

Missing rounds (job tried; part unplugged):
1. Watch a cartoon; speakers. 2. Write a word; screen. 3. Paint a picture; mouse. 4. Say hello; microphone.
5. Take a picture of Bubbles; camera. 6. Watch a cartoon; screen. 7. Watch a cartoon; computer box.

All in one facts (each hotspot's line, below): a laptop has the screen, keyboard, touchpad (its mouse), speakers,
microphone and camera built in, with the brain inside; a tablet's touchscreen is both screen and pointer, its keyboard
appears on the screen, and it also has speakers, a microphone, a camera and a brain inside.

## Interactions in detail
- Part show while working: the part glows yellow (#ffd23f ring), its cable dots flow (in or out) for the length of the show.
- No box on the desk: tapping any other placed part makes it wiggle, its dots run to the loose plug and pop as a small
  gray "?" puff; narrator says the no-box line. The screen with no box stays dark.
- Box present, screen missing: keyboard, mouse and camera shows still run their dots to the box, the box blinks, then
  the no-screen line. Microphone with no speakers: the wave runs, then the no-speakers line (no answer plays).
- Speakers need only the box. Screen needs only the box.
- Placing a part names it (every time; a part placed again within 3 s of removal is not named again). Removing a part
  plays a soft whoosh (two falling tones), no line.
- All seven placed for the first time per visit to Build: the all-built line, then the All in one line; the button unlocks.
- Jobs: Try it with an empty desk says the empty-desk line. Otherwise the job runs with what is there: every present
  needed part does its bit (the cartoon plays silently with a crossed-out speaker icon when the speakers are missing;
  HELLO keys press with nothing on screen when the screen is missing). Then the narrator says the symptom line of the
  first missing part in this order: box, then the job's parts in the order listed in Content. Only that part's ghost
  slot pulses (blue, 3 times). If the box is missing, nothing moves at all. On success: needed parts glow, extra
  parts dim and show a small "Zzz", the success line plays, then the rest line if there were extras.
- Picking another job mid-run stops the run and speech, then starts the new job. All six jobs checked: the six-jobs
  line once per visit.
- Missing: during a round the shelf is hidden; taps on the desk before the job finishes are ignored. Wrong part tapped:
  it does its Build show (it works!) and its wrong line plays. Right part tapped: Nibbles pops out holding the plug,
  squeaks (two high tones), plugs it back, the found line plays, then the job runs fully with its success line. Seven
  rounds in order; after round 7 the all-fixed line, and Start begins round 1 again.
- Mode switch, Clear desk, Back to desk: stop speech and animation, drop queued lines (kit stop + the collision-lab hush pattern).
- Read: stops speech and says the hint text (always the latest fixed line shown in the hint).
- Keyboard only: shelf tiles, job cards and panel buttons are buttons (Enter or Space). Placed desk parts and hotspots
  are buttons too, tab order panel first, then desk parts left to right. Letter keys type on the screen only in Build.
- Motion off: parts appear in their slots without flying, cable dots become a steady arrow on the cable for the same
  time, no blanket drop (it fades), Nibbles appears and vanishes. Timing stays the same.
- Sizes: draw the stage at real pixel size and re-lay it out per size (no scaled fixed design). At 1366x768 and below
  about 900 px tall, keep stage and panel side by side with a compact panel (shelf tiles 72 px, job cards 64 px).
  Under 760 px wide: stage on top, then Try it or Start, then shelf (4 columns) and job cards (3 columns), all at
  least 60 px. Desk slots keep their order at every size.

## Look
Accent `--brand: #2049b8` (cobalt). Neighbors: loop-garden is garden green with blue, purple and orange blocks; this is
a cobalt workbench with warm wood. `:root`: --paper #f4f6fd, --ink #1c2340, --muted #55607f, --line #cfd8f6,
--focus #c2410c, --brand #2049b8, --btn #ffffff, --btn-line #cfd8f6, --head-ink #ffffff, --panel #ffffff.
Scene: wall #e9eefb (behind art), desk wood #d9a86c with a #b8834a edge, glow #ffd23f, in dots #08606a, out stars
#9a3209, ghost outlines #454e6e dashed, Try it button #17703d. Parts are friendly rounded shapes: off-white plastic
#f7f7fb with #1c2340 outlines and cobalt details. Font: 'Trebuchet MS' bold for names, like the K-2 tools.
Contrast: white on brand 7.76; brand on paper 7.19; ink on paper 14.26; muted on paper 5.78; ink on glow 10.66;
ink on wood 7.16; white on Try it green 6.14; focus ring on paper 4.80. Graphics (need 3), on wood #d9a86c / light wood
#e7bf89 / wood gradient ends #e4b77f and #d4a265 / wall #e9eefb / paper #f4f6fd: in dots #08606a 3.38 / 4.22 / 3.94 and
3.17 / 6.26 / 6.73; out stars #9a3209 3.45 / 4.31 / 4.01 and 3.23 / 6.38 / 6.86; ghost outline #454e6e 3.80 / 4.76 / 4.43
and 3.57 / 7.04 / 7.57 (5.0 on wood through its own #ffffff55 fill). Color is never the only signal: dots and stars differ in shape
and direction, done jobs have a check, the unlocked button loses its lock.

## Art
Parts, cables, desk, screen contents, job icons, laptop and tablet: drawn in code (SVG). Images (6):
- backdrop: a sunny classroom wall with a pegboard holding a few colorful tools, a window with a blue sky and a small
  plant, flat soft pastel illustration, blank surfaces; 16:9; cutout no; people no; Cloudflare FLUX.2 (cfart.py);
  cover-fit behind the desk, top two thirds of the stage.
- bubbles-bowl: an orange cartoon goldfish in a round glass bowl with a pebble bottom, front view; 1:1; cutout yes;
  people no; Codex (gptart.py) base for the character set; on the desk, left edge.
- bubbles-photo: the same orange cartoon goldfish close up, smiling, swimming among green water plants, full frame;
  4:3; cutout no; people no; Codex with "ref": "bubbles-bowl" (character match); shown on the screen as the photo.
- nibbles: a small gray cartoon mouse with big round ears and a pink nose, standing on hind legs, grinning cheekily;
  1:1; cutout yes; people no; Codex with "ref": "bubbles-bowl", "ref_mode": "style"; peeks from behind the desk.
- nibbles-plug: the same gray cartoon mouse holding a black cable plug in both front paws; 1:1; cutout yes; people no;
  Codex with "ref": "nibbles" (character match); shown when the unplugged part is found.
- panda: a cartoon giant panda sitting among bamboo, holding a bamboo stalk and waving one paw, full frame; 4:3; cutout
  no; people no; Codex with "ref": "bubbles-bowl", "ref_mode": "style"; on the screen for the zoo video chat.
No other tool in the CS batch uses a goldfish, a mouse character, a panda or this backdrop.

## Voice
Bank `bright-teacher` (Autonoe): "Say brightly and cheerfully, like an upbeat first grade teacher". Fits a grade 1
build-it lesson; neighbors use hero-coach (loop-garden) and lively-host (robot-dance). Every fixed line:

Build
- Let's build a computer! Tap a part on the shelf to put it on the desk.
- The computer box! The brain is inside. It does the thinking.
- The screen! It shows us pictures and words.
- The keyboard! Its keys send letters to the computer.
- The mouse! It moves the arrow on the screen.
- The speakers! They make sounds and music.
- The microphone! It listens to sounds.
- The camera! It takes pictures.
- Hum, hum! The brain is thinking.
- Hello, screen! Look at the pictures.
- Tap, tap! Look, a letter!
- Move and click! The arrow paints a rainbow.
- La la la! Music from the speakers.
- Everyone, say hello!
- Hello, class!
- Smile, Bubbles! Click!
- Nothing happened! The parts need the computer box. The brain is inside it.
- The computer got it, but there's no screen to show it!
- The computer heard you, but it has no speakers to answer.
- We built a whole computer! Tap each part on the desk to try it.
- Some computers squeeze all the parts into one. Tap All in one!
- A laptop has all the parts inside! Tap a circle to find a part.
- A tablet has the parts inside too! Tap a circle to find a part.
- Here's the screen.
- Here's the keyboard.
- This touchpad is the mouse. Slide your finger on it.
- The speakers hide here.
- These tiny holes are the microphone.
- This tiny dot is the camera.
- The brain is hiding inside!
- The touchscreen is the screen and the mouse. Your finger does the pointing!
- The keyboard pops up on the screen.

Jobs
- Let's give our computer a job! Tap a job card.
- Job: watch a cartoon! What parts do we need?
- Job: write a word! What parts do we need?
- Job: paint a picture! What parts do we need?
- Job: say hello to the computer! What parts do we need?
- Job: take a picture of Bubbles the fish! What parts do we need?
- Job: video chat with the panda at the zoo! What parts do we need?
- The desk is empty! Tap some parts first.
- Nothing works! Every computer needs a brain.
- Nothing to see! We need a part that shows pictures.
- No sound! We need a part that makes sound.
- No letters! We need a part with keys.
- The arrow won't move! We need a part that moves the arrow.
- The computer can't hear us! We need a part that listens.
- The computer can't see! We need a part that takes pictures.
- It works! We watched a cartoon with the box, the screen and the speakers.
- It works! We wrote a word with the box, the keyboard and the screen.
- It works! We painted with the box, the mouse and the screen.
- It works! The microphone heard us and the speakers answered.
- It works! The camera took a picture, and the screen shows it.
- It works! We can see and hear the panda, and the panda can see and hear us!
- Some parts got a rest. That's OK!
- Six jobs done! You're computer builders!

Missing
- Oh no! Nibbles the mouse likes to unplug things. Tap Start to find what's wrong.
- Close your eyes!
- Open your eyes! Let's try a job.
- Which part is unplugged? Tap that part on the desk.
- The computer box works! Tap a different part on the desk.
- The screen works! Tap a different part on the desk.
- The keyboard works! Tap a different part on the desk.
- The mouse works! Tap a different part on the desk.
- The speakers work! Tap a different part on the desk.
- The microphone works! Tap a different part on the desk.
- The camera works! Tap a different part on the desk.
- Nothing happened! This part needs the brain. Tap a different part on the desk.
- You found it! Let's plug it back in.
- You fixed every one! Nibbles is all out of tricks.

How-to lines (every time the tool waits for the child, the next step and where to tap is said and stays in the hint)
- Tap a part on the shelf.
- Tap the computer box on the shelf.
- Tap a part on the shelf, or tap a part on the desk to try it.
- Tap a part on the desk to try it, or tap All in one.
- Tap another circle, or tap Back to desk.
- Tap a job card.
- Tap the parts on the shelf. Then tap Try it.
- Tap Next job, or tap any job card.
- Tap Start.
- Tap Next round.
- Tap Start to play again.

Missing rounds reuse the Jobs symptom and success lines. Order in a round: Open your eyes, symptom, Which part. Hint
text shows the latest line, so it always ends on the how-to step. A line that only reports or asks (a part's name, its show,
a no-box or no-screen line, a job, a symptom, a success, a spot) is followed by the how-to line for that moment (Build: shelf,
box, build or full by what is on the desk; All in one: circle; Jobs: job card, parts then Try it, or Next job; Missing:
Start, Next round or play again); a newer tap drops a how-to line that has not started. Lines that already name the step
(the welcomes, All built, Tap All in one, the laptop and tablet lines, Which part, the works lines) need none. A first tap
on the locked All in one counts as an ordinary tap, so the welcome plays; welcome per mode once after the first tap (collision-lab queue rules in STANDARDS.md).
In round 7 (box unplugged) the computer box's wrong line can't happen; tapping any other part powers nothing on (dots stop at the box with a "?" puff) and plays "Nothing happened! This part needs the brain. Tap a different part on the desk."

## Family engine
none

## Sources
- CSTA K-12 Computer Science Standards (2017), 1A-CS-01, 1A-CS-02, 1A-CS-03: https://csteachers.org/k12standards/
- Module codes E1-SYS-HW-11, E1-SYS-SE-12: data/modules.csv (CSTA-2026 list in data/standards/csta-2026-ids.txt).
- Screen, keyboard, mouse, speakers, microphone, webcam and the computer case, and what each does: GCFGlobal Computer
  Basics, "Basic Parts of a Computer": https://edu.gcfglobal.org/en/computerbasics/basic-parts-of-a-computer/1/
- The processor (CPU) as "the brain of the computer", inside the case: GCFGlobal, "Inside a Computer":
  https://edu.gcfglobal.org/en/computerbasics/inside-a-computer/1/ (grade 1 wording "the brain" is deliberate).
- Laptops have a built-in screen, keyboard, touchpad, speakers, webcam and microphone: GCFGlobal, "Laptop Computers":
  https://edu.gcfglobal.org/en/computerbasics/laptop-computers/1/
- Tablets use a touchscreen instead of a mouse, an on-screen keyboard, and have cameras, microphones and speakers:
  GCFGlobal, "Mobile Devices": https://edu.gcfglobal.org/en/computerbasics/mobile-devices/1/
- Hardware, input and output (in and out arrows): Code.org CS Fundamentals glossary: https://code.org/curriculum/docs/k-5/glossary
- Giant pandas eat bamboo (panda art): Smithsonian's National Zoo, Giant panda: https://nationalzoo.si.edu/animals/giant-panda

## Done when
1. In Build, tapping each of the seven tiles puts that part in its slot with its naming line (voice log shows the
   clip), and tapping the tile again returns it; no part ever lands in the wrong slot.
2. With only the keyboard and screen on the desk, tapping the keyboard gives the no-box line and the screen stays
   dark; adding the box makes the keyboard type H, then E on the next tap, with teal dots flowing toward the box.
3. Microphone with box but no speakers says the no-speakers line and plays no "Hello, class!".
4. All in one stays locked until all seven parts are placed, then opens the laptop; every laptop and tablet hotspot
   says its line; Back to desk returns the built desk.
5. Jobs: watch a cartoon with box and screen only plays the cartoon silently, then says "No sound! ...", and only the
   speaker slot pulses; adding the speakers and Try it gives the success line; an extra keyboard gets "Zzz" and the rest line.
6. All six jobs can be finished and checked; the six-jobs line plays once.
7. Missing: all seven rounds play in order; a wrong tap shows that part working plus its wrong line; the right tap
   brings Nibbles with the plug, then the full job runs; after round 7 Start restarts at round 1.
8. Held clicks (press, ~120 ms, release) on the first tap, Read during a line, mode switch mid-line and Sound off and
   on all follow the STANDARDS voice rules; no line plays twice or gets cut off by a queued line.
9. Keyboard only reaches and runs every control; Motion off removes flying, dots and blanket drop but keeps timing.
10. Every STANDARDS size: shelf tiles, job cards and Try it or Start visible without scrolling, scene text 10 px or
    more in the 680x425 preview, 60 px targets at 375 wide; console clean; file under 2 MB with clips inlined.
