# Field Trip Slideshow

## One idea
A slideshow is made by a crew: after the class aquarium trip, the class takes each job in turn and gets its one skill right (Camera picks the clear photo, Sound keeps the music under the speaker's words, Speaker matches one true sentence to each slide), then sets up the room so families can really see and hear, and presents, with a dress rehearsal that shows exactly which job still needs a fix.

## Not like
- sound-and-picture-book (k-2, studio, this batch): sounds tell a made-up story. Here the show is a true recount, and the sound job is about volume under a speaker.
- hallway-art-museum (k-2, builder, this batch): shows objects in a hallway. Here the work is a timed show with jobs, a room and an audience.
- virtual-gallery (9-12, builder): hangs a portfolio and tests a visitor walk. Here the tests are a K-2 crew's three skills and a dark enough room.
- brand-builder, stage-blocker (6-12, builder): design and staging for older students. Here every job has one skill a five-year-old can check.
- art-passport (k-2, explorer): looks at art. Here the class makes a presentation.

## Who and how
- Grade K-2, media arts, module "Presenting Media Together".
- Driver: teacher on a projector or smartboard; the class splits into crews (Camera, Sound, Speaker, Room), each crew chooses for its job while the others watch, then the class presents. 25 to 35 minutes, or one job a day.
- Standards: NCAS MA:Pr5 (practice roles and skills to present media), MA:Pr6 (present media and share it with an audience), MA:Cn10 (make media about a shared experience).
- Media rule: no camera, upload or recording. The "photos" are paintings; the takes are made from them in code.

## Screens and modes
Header: title, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`, icon plus word): `Camera` (camera), `Sound` (speaker), `Speaker` (microphone), `Room` (chair), `Show` (play). Every control is 60 px or more with an icon and a word. A crew badge strip under the header shows the four jobs with a check when each is done.

**Camera.** Focus: three takes of one slide side by side, big (each about 30% of the stage width), labeled `Take A`, `Take B`, `Take C`. One is clear, one is blurry, one has a problem from the slide's list (cut off, too dark, glare). Above: the slide's number of 6 and its subject word. Tap a take: it grows to fill the stage with `Use this one` (gold) and `Back to takes`. Using a take puts it in the slide strip at the bottom (6 slots). A take with a problem gets a gentle note (Content) and a "Try another take" button; it can still be used.

**Sound.** Focus: the current slide, big, with two level bars beside it drawn in code: `Voice` (a microphone icon, fixed) and `Music` (a music note icon, five steps). Buttons: `Softer` and `Louder` for the music (60 px), `Test it` (gold): plays the speaker's sample sentence for this slide (narrator voice) over the music at the chosen level, with a word-by-word highlight under the slide. A listening face drawn in code beside the bars (an ear and a check, a question mark or a cross) shows how clear the words are at this level.

**Speaker.** Focus: the slide strip big (two rows of three), each slide with an empty speech-bubble slot. Six sentence cards below (with an icon each). Tap a card, then a slide (or drag): the sentence goes into the bubble. A wrong match gets "Is that about this picture? Look again." and the card returns. When all six match, a practice card appears: "Stand tall. Look at the families. Say it loud and clear." with `We practiced` (check).

**Room.** Focus: the classroom (painted), side view, with the pull-down screen, the projector on its cart, three rows of chairs and a speaker's spot. Controls (each a big toggle with an icon and word): `Lights` (On, Dim, Off), `Screen` (Up, Down), `Chairs` (Face the screen, Face the door), `Speaker spot` (In the beam, Beside the screen, Behind the chairs), `Volume` (Soft, Medium, Loud). The projector beam (code) shows the first slide on the screen, washed out by the lights; a speaker silhouette marker (a code star with a microphone, not a person) in the beam casts a shadow on the slide.

**Show.** Focus: the slideshow, full stage: title slide "Our Aquarium Trip" (code text over the aquarium entrance painting), then the six chosen takes, each with its sentence in a small caption strip (for the speaker child or teacher to read) and the music at the chosen level. Bar: `Dress rehearsal` (clipboard), `Present` (gold), `Back slide`, `Next slide`, `End show`.
- Dress rehearsal: a checklist card, one row per job, each with a check or a note naming the job and the fix ("Camera: slide 3 is blurry. Tap Camera to fix it."). Rows: Camera (6 clear takes), Sound (music level 1 to 3), Speaker (6 matches and practiced), Room (lights Dim or Off, screen Down, chairs Face the screen, speaker Beside the screen, volume Medium).
- Present: the show plays one slide at a time; the teacher taps Next slide when the speaker is done. After the last slide, a "Thank you for coming!" slide and a soft applause (code).

## Content
**Slides** (painting; subject; problem take; sentence; icon):
1. Moon jellies glowing in a blue tank; jellyfish; too dark; "Jellyfish have no bones and no brain."; jelly icon.
2. A red octopus on the glass; octopus; cut off (only two arms show at the edge); "An octopus has eight arms, and it can change color."; octopus.
3. A green sea turtle swimming; sea turtle; glare (a white flash over its head); "Sea turtles breathe air. They swim up to the top for a breath."; turtle.
4. A shark gliding over a glass tunnel; shark; cut off (the tail only); "Sharks grow new teeth all their lives."; shark.
5. Seahorses in seagrass; seahorse; too dark; "Seahorse dads carry the babies."; seahorse.
6. Penguins on rocks by the water; penguin; glare; "Penguins are birds that cannot fly, but they swim fast."; penguin.
Each slide's takes, in a fixed shuffled order per slide (clear at A, B or C): clear (the painting); blurry (CSS blur 6 px, scaled); the problem take: too dark (brightness 0.35), cut off (the painting shifted 70% sideways so the subject leaves the frame), glare (a white radial gradient at 85% over the subject).
**Camera notes:** blurry: "That one is blurry. Can you see the <subject> clearly?"; too dark: "That one is too dark. Families won't see the <subject>."; cut off: "Part of the <subject> is cut off."; glare: "A flash bounced off the glass."
**Clear take line:** "Clear, and the <subject> is in the middle. Good camera work!"

**Sound levels** (music relative to the voice): 1 = -24 dB, 2 = -18, 3 = -12, 4 = -6, 5 = 0. Faces: 1 to 3 check ("I can hear every word"); 4 question mark ("Some words are hard to hear"); 5 cross ("The music covers the words"). Start at 5. Music: an original calm "aquarium" loop made in code (soft pad in D major, slow arpeggio in a sine bell, bubble blips), 72 bpm, 8 bars.

**Room rules** (the screen picture and the check): Lights On washes the slide to a 2.5 to 1 contrast, Dim to 4.2, Off to 10.5 (computed from an ambient wash of 0.6, 0.25 and 0.05 over a slide from 0.05 to 1.0); Dim and Off pass. Screen Up: the beam lands on the board behind (the picture warps and fades); Down passes. Chairs facing the door: the chair cutouts flip; fail. Speaker In the beam: a shadow on the slide; Behind the chairs: the speaker marker is far from the families' view (fail with "Families can't see the speaker"); Beside the screen passes. Volume Soft: "The back row can't hear"; Loud: "Too loud for a classroom"; Medium passes.
**Room notes:** "The lights wash out the picture. Try Dim or Off." / "Pull the screen down." / "Turn the chairs to face the screen." / "The speaker is in the beam and makes a shadow." / "Families can't see the speaker back there." / "The back row can't hear." / "Too loud for a classroom."

## Interactions in detail
- Jobs can be done in any order, and redone; the crew badge gets a check when its job's rule passes (Camera: all six slides use their clear take; Sound: level 1 to 3 chosen and Test it played once; Speaker: six matches and We practiced; Room: all five rules pass).
- Camera: the slide advances after `Use this one` (with `Next slide` and `Back slide` on the takes screen to move freely). Using a problem take shows its note but keeps it; the badge stays unchecked until it is replaced.
- Sound: Softer and Louder change the music level at once, also during Test it (the gain ramps over 50 ms; the face updates at once). Test it plays at most 6 s; tapping it again restarts.
- Speaker: the six cards can go on any slide; only the matching one stays.
- Room: every toggle updates the picture at once; the lights dim over 400 ms (Motion off: at once).
- Show: Present works even if checks fail (teachers decide); Dress rehearsal is a picture of what is ready, never a score. Next slide during a caption line cuts it.
- Tap while anything plays: any button acts at once (Test it, applause, a slide change, the light fade).
- Nothing is saved; the crew's work stays while the page is open. `New show` (in Show, with `Yes, start over` and `Keep it`) clears all jobs.
- Keyboard: arrows move slides in Camera and Show; Tab order is takes, then bar.

## Look
- Accent (`--brand`) #155e75 deep aquarium blue (header, gold buttons' border, crew checks). Paper #f1f7f8, ink #13262c, muted #4d6268. Slides sit on a dark frame #0b1c22 like a screen. Notes in warm sand cards #fbf1dc with an icon, never color alone.
- Contrast (WCAG 2.1, computed): white on brand 7.27:1; brand on paper 6.71:1; ink on paper 14.46:1; muted on paper 5.95:1.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8, act-it-out #7d2e7f, levels-and-pathways #00798c.

## Art
Local FLUX (`scripts/localart.py`). No people (the aquarium photos show animals only; the room has empty chairs).
- 6 slide paintings, each "<subject>, inside a public aquarium, seen through the glass, bright and clear, the animal in the center, soft realistic painted illustration"; 16:10; cutout no; people no; Camera takes (the problem takes are made in code from these), Speaker and Show: moon jellyfish glowing in a deep blue tank; a red octopus pressed against the glass with its arms spread; a green sea turtle swimming toward the viewer; a shark gliding over a curved glass tunnel; two seahorses holding seagrass with their tails; four penguins standing on rocks by the water.
- entrance: "The entrance of a public aquarium with a big blue arch, a blank sign above the doors, fish shapes on the glass, sunny day, soft realistic painted illustration"; 16:10; cutout no; people no; the title slide (the words are code).
- classroom: "An empty elementary classroom seen from the side, a whiteboard wall at the left, three rows of small chairs, windows with blinds, soft painted illustration, the left wall clear"; 16:9; cutout no; people no; Room backdrop (lights dimmed in code).
- screen-up, screen-down: "A pull-down projector screen on a wall bracket, <rolled up / pulled down, blank white>, soft painted illustration, plain white background"; 3:4; cutout yes; people no.
- projector: "A classroom projector on a small rolling cart, side view, soft painted illustration, plain white background"; 1:1; cutout yes; people no; the beam is code.
- chair: "A small blue school chair, side view, soft painted illustration, plain white background"; 1:1; cutout yes; people no; placed in three rows and flipped in code to face either way.
12 images, none with people. Drawn in code: the takes' blur, darkness, crop and glare, level bars and the listening face, the beam and shadow, the speaker marker, captions, checklists.

## Voice
Bank voice `science-narrator` (Charon), style "Say in a clear, informative way, like a nature documentary narrator". Fits an aquarium show, and it voices the speaker's sample sentences in the Sound test. Not used by any K-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, sound-elevator hero-coach, act-it-out gentle-storyteller, levels-and-pathways warm-teacher) or by another K-2 spec in this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.slide`.

- how, welcome (Camera; stale when a take is tapped): "Camera crew, pick the best photo for each slide. Tap a take to look closer."
- event, Use this one: the clear take line or the take's note (Content).
- event, all six clear: "Six clear photos. Camera crew, great job!"
- how, welcome (Sound; stale when Test it is tapped): "Sound crew, the families must hear the speaker. Tap Test it and listen."
- event, Test it: the slide's sentence (6 lines), spoken over the music at the chosen level (this line is the test, so it plays with the music).
- event, after Test it: "I can hear every word." / "Some words are hard to hear." / "The music covers the words." (by level)
- how, first unclear test (stale when Softer is tapped): "Tap Softer, then Test it again."
- how, welcome (Speaker; stale when a card is placed): "Speaker crew, find the true sentence for each picture. Tap a sentence, then a slide."
- event, wrong match: "Is that about this picture? Look again."
- event, all six: "Every slide has its sentence. Now practice: stand tall, look at the families, and say it loud and clear."
- how, welcome (Room; stale when a toggle is tapped): "Room crew, set up so every family can see and hear. Change the lights, screen, chairs, speaker spot and volume."
- event, each room note when its toggle makes it fail, and "The room is ready!" when all pass.
- how, welcome (Show; stale when Dress rehearsal or Present is tapped): "Tap Dress rehearsal to check every job. Then tap Present."
- event, each checklist note (first failing row only, so one line a rehearsal) or "Every job is ready. Showtime!"
- event, the end slide: "Thank you for coming to our aquarium show!"
- Read speaks the hint, or the open note.

## Family engine
none

## Sources
- National Core Arts Standards, Media Arts, grades K to 2 (MA:Pr5, MA:Pr6, MA:Cn10): https://www.nationalartsstandards.org
- Jellyfish have no bones and no brain (a nerve net): NOAA Ocean Service, "What are jellyfish made of?" (https://oceanservice.noaa.gov/facts/jellyfish.html).
- Octopuses have eight arms and change color: Monterey Bay Aquarium, "Giant Pacific octopus" (https://www.montereybayaquarium.org/animals/animals-a-to-z/giant-pacific-octopus).
- Sea turtles breathe air at the surface: NOAA Fisheries, "Green Turtle" (https://www.fisheries.noaa.gov/species/green-turtle).
- Sharks replace teeth throughout life: Florida Museum of Natural History, "Shark teeth" (https://www.floridamuseum.ufl.edu/discover-fish/sharks/); NOAA Fisheries.
- Male seahorses carry the young in a brood pouch: Smithsonian Ocean, "Seahorses" (https://ocean.si.edu).
- Penguins are flightless birds that swim fast: Monterey Bay Aquarium, "African penguin"; National Geographic Kids, "Penguins".
- Background music under speech should sit well below the voice (about 10 dB or more) for clear words: Armstrong, M. (2016), "From Clean Audio to Object Based Broadcasting", BBC R&D White Paper WHP 324. The tool's levels are a classroom simplification.
- Ambient light washes out a projected image (contrast = (white + ambient) / (black + ambient)): standard projection contrast, e.g. InfoComm/AVIXA projected image contrast guidance (ANSI/INFOCOMM 3M-2011). The ambient numbers are illustrative.
- Checks run (Python, 2026-10-29): music levels as gain: -24 dB 0.063, -18 dB 0.126, -12 dB 0.251, -6 dB 0.501, 0 dB 1.000; levels 1 to 3 are at least 12 dB under the voice. Room contrast with a 0.05 to 1.0 slide: ambient 0.6 gives 2.5 to 1, 0.25 gives 4.2 to 1, 0.05 gives 10.5 to 1. Every slide has exactly one matching sentence (6 of 6), and each slide's problem take differs from blur. Contrast ratios as listed.

## Done when
1. Focus: at 1366x768 and 680x425 the three takes fill the Camera stage, the slide fills the Sound and Show stages, and the room fills the Room stage with readable controls.
2. Every slide has a clear, a blurry and a problem take, the clear one in a fixed varied place, and each take gives its note.
3. Sound faces follow the level table; Softer and Louder during Test it change the music within 50 ms.
4. All six sentences match only their slides.
5. Every room toggle changes the picture at once, and all five rules pass only in the combination in Content.
6. Dress rehearsal names the first failing job and its fix; Present works whether or not every check passes.
7. Tap while it plays: Next slide, Test it again or a mode switch during a line or the music acts at once.
8. How-to lines are spoken once in five actions; notes and results every time.
9. Every control is 60 px or more with an icon and a word; the crew badge strip and each job's main button are visible without scrolling at every size in STANDARDS.md.
10. Motion off: no light fade, no zooms; no camera, microphone or network request anywhere.
