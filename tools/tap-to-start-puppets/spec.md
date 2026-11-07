# Tap-to-Start Puppets

## One idea
Each felt puppet on the library's puppet stage holds a short strip of picture blocks that does nothing until its start block happens (a tap on the puppet, a tap on the drum, or another puppet finishing); the class says what the blocks will do and what will start them, taps, and watches the blocks light up one at a time as the puppet acts, and second graders build their own show and tell, step by step, how they built it and who helped.

## Not like
- robot-dance (K, built): Bolt follows a card sequence and trips on a wrong card; the class debugs. Here nothing is wrong or fixed: the class reads a finished program, predicts its end, and the new idea is the start block (nothing runs until its event).
- snowy-mail-route (1, built): arrow cards on a 2D town grid, predict where Pip stops, fix the card. Here the stage is one row of five spots, blocks also sing, spin, duck and pop up, there is no fixing, and from grade 1 on the question is what starts a program, not where it ends.
- loop-garden (2, built): repeat blocks and fewest-block stars. Here there are no loops and no stars; grade 2 builds freely and the work is telling how it was built.
- line-leader-picker (K-2, spec): a written rule runs a whole month and the outcome is people. Here a program runs once, when its event happens.
- morning-meeting-board (K-2, concept): picture signs as values that change. Here the blocks are actions and events, not stored values.
- input-or-output (2, spec): covering a gadget's input parts. Here a tap is an event that starts code, not a device part.
- puppet-show-feelings (K-2 arts, spec): one sock puppet, dials, reading feelings from movement in a cardboard theater. Here three felt puppets run code on a wooden library stage; no feelings, no dials, a different look (see Look and Art).

## Who and how
- Grades K-2, computer science, module "What the Code Does" (computer-science-k-2-what-the-code-does, Algorithms and Programming). Standards (CSTA 2026): EK-PRO-RD-06 (describe how a sequence of commands completes a task), E1-PRO-RD-06 (explain the function of code that includes an event and sequence), E2-PRO-RD-06 (explain the steps taken to create a program).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class answers out loud and a helper taps. Every question, choice and next step is spoken and every choice is a picture, so a child alone can play (BASELINE rule 4).
- Three modes, each with a small grade tag on its button: Watch and Say (K), What Starts It? (1), Build and Tell (2). Any mode works for any grade. tool.json `modes: ["Watch and Say", "What Starts It?", "Build and Tell"]`, `minutes: "10-30"`, `grades_label: "Grades K-2"`.
- Minutes: Watch and Say 10 to 15 (8 shows); What Starts It? 10 to 15 (10 scenes); Build and Tell 20 to 30.
- Not a personal prompt: "who helped" names a role (me, a friend, a grown-up), never a name. Build and Tell saves the show and its diary in localStorage (`tap-to-start-puppets-build`, try/catch) and its panel says "Your show is saved only on this device." (BASELINE rule 7). Nothing else is stored.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| EK-PRO-RD-06 | Watch and Say: hear the puppet's job, pick the mini stage that shows where the puppet will be when its 3 blocks are done, tap the puppet, then say what it did, block by block (Step plays one block a tap), before tapping Hear it | the strip's blocks light one at a time as the puppet acts; the job is met or missed (prop reached or not); check or "look again" on the picked mini stage | 2, 3 |
| E1-PRO-RD-06 | What Starts It?: read the start block on each of three strips and tap the thing that starts a named puppet (chains of 2 and 3 included); or pick who moves when a puppet finishes | waiting puppets wiggle and their start block pulses; a spark runs from a finished strip to the start block waiting for it; the explain line names each event in the chain | 4, 5 |
| E2-PRO-RD-06 | Build and Tell: build programs for the puppets (start blocks, up to 4 action blocks each), tag each change Me / A friend / A grown-up, then in Tell it say each step before revealing it, and tap each block to say what it does | the Build diary (one picture card per change and try, with its helper icon); the credits card revealing one step at a time with sentence starters; Mia's example | 6, 7 |

## Screens and modes
Header (kit): title "Tap-to-Start Puppets"; mode buttons (`.seg`, icon plus word plus grade tag, 60 px tall): `Watch and Say` (eye icon, "K"), `What Starts It?` (finger-tap icon, "1"), `Build and Tell` (stacked blocks icon, "2"); then `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), with an icon and a word.

Shared stage (all modes), drawn at real pixel size and re-laid per size:
- Theater (painted, top of the stage area): a wooden library puppet stage with indigo curtains; inside the opening the meadow backdrop; along its bottom the ledge the hand puppets rise from. Five felt dots on the ledge mark spots 1 to 5 (left to right, drawn in code, no numbers). Puppet cutouts stand on a spot; "down" means slid behind the ledge with only the top peeking (Frog's eyes, Dragon's horns, Moon's tip).
- The drum (painted cutout, 96 px) sits on the theater's left apron, outside the opening, in What Starts It? and Build and Tell only. Tapping it plays a drum tone and shakes it.
- Strip row (under the theater): one program strip per puppet on stage, each labeled with that puppet's face (60 px) on its left. A strip is a start block (hat shape, yellow, rounded top) then action blocks (square, blue). While a program runs, the block now running scales to 1.1, gets an outer pink ring with a paper gap and the engine's chevron pointer above it; finished blocks keep a small check under them until the run ends.
- Panel (right, 320 px at 1366): the hint (20 px) at top, then the mode's controls (below), then the footer.
- Focus: the theater while anything runs; the strips while the class reads. At 1366x768: header 56, theater 1046 x 440, strip row 200, panel 320 wide: all above the fold. At 680x425: header 44, panel 220 wide, theater 460 x 200, block tiles 44 px, scene text 10 px or more.

**On load and first tap.** Watch and Say opens on show 1: Frog on spot 2, the lily pad on spot 4, Frog's strip (When I'm tapped, Hop right, Hop right, Sing) under the theater, and three guess pictures in the panel. Nothing plays and nothing speaks before the first tap (kit). First hint: "Frog wants to get to the lily pad. Where will Frog be at the end? Tap a picture, or tap Frog to start." The first tap on a guess picture picks it and plays `guessed`; the first tap on Frog starts the run at once (sounds only); either way the kit then puts the welcome after it (`welcomeAfter: true`, so a one-tap start still hears what the stage is). The welcome may be cut (BASELINE 16); the premise (blocks tell a puppet what to do; it waits for its start block) lives in every mode's hint and Read, and in the first line of each mode.

### Watch and Say (K)
- One puppet on stage per show, its prop, its strip centered under it (start block plus 3 action blocks, tiles 96 px).
- Panel: three guess pictures stacked (each a 288 x 110 code-composited mini stage using the same cutouts: the puppet at a spot, up or down, with the prop), in a shuffled order each time the show opens; then `Step` (footsteps icon), `Hear it` (ear icon), `Play again` (circle arrow), `Next show` (gold, curtain icon).
- Flow: show opens (puppet at its start, `show` line). Guess (optional): tap a picture; it gets a thick border and a "my guess" pin. Tap the puppet (or its start block) to run. When the run starts the two unpicked pictures fade to 40 percent and lock; the picked one stays. Run ends: the stage holds the end state, the picked picture gets a check (green, check icon) or a "look again" ring and the true end picture (a fourth mini stage) slides in beside it; the job result shows as a code badge on the prop (a check or a small cross with the word "not yet").
- Step, Hear it and Play again are disabled until a run has ended (the hint never names them before). Step resets the puppet to its start and plays one block per tap (the block lights and its name is spoken); a fourth tap plays `stepDone`. Hear it plays the show's `why` line. Play again resets the stage and runs at once. Next show opens the next show (8 in order; after show 8, show 1 again with `allShows`).
- What the picture shows for each outcome: reach, the puppet stands on or with its prop and the prop's badge is a check; miss, the puppet stands one or more spots away (or still down behind the hill) and the badge says "not yet". Down and up differ at a glance in the mini stages (full puppet vs top peeking over the ledge).
- At 680x425: guess pictures 200 x 64 stacked; Step, Hear it, Play again icon-only with tooltips; Next show keeps its word.

### What Starts It? (1)
- Three puppets in fixed places (Frog spot 1, Dragon spot 3, Moon spot 5, all up), each with its strip under it (start block plus 2 in-place action blocks, tiles 84 px). The drum is on the apron.
- Ten scenes; each asks one question, of kind A or B, then stays open for free play.
- Kind A, "What starts {P}?": the answer is a tap on the stage (Frog, Dragon, Moon or the drum). Only the first tap after the question is judged; every tap acts truthfully at once (a tap-started puppet runs, the drum starts every drum-started puppet, finishes start their waiters). Panel: `Play again` (puts every puppet back up in place and clears marks) and `Next scene` (gold).
- Kind B, "When {X} finishes, who moves next?": panel shows three 120 px picture buttons: the faces of the two other puppets and Nobody (an empty felt spot). After a pick the tool starts X itself (a "Go" spark on X's start block, no finger on any trigger, so nothing about what starts X is shown), and the class watches who follows.
- Waiting: tapping a puppet whose start block is not "When I'm tapped" makes it wiggle once and its start block pulse; nothing runs.
- Chains: when a program's last block ends, a dotted spark runs from that strip's end to every start block showing that puppet's face, which then light and run. Two programs started by one drum tap run at the same time.
- Focus: the three strips and the stage together; the strips sit right under their puppets so each start block is next to the puppet it starts.
- At 680x425: strips 44 px tiles, the B face buttons 64 px in a row.

### Build and Tell (2)
- Same three puppets in their places (Frog 1, Dragon 3, Moon 5, all up), the drum, and the lily pad on spot 2. Each puppet's strip: start block plus up to 4 action blocks (tiles 60 px); empty slots dashed. One strip is selected (thick border, face ringed); tap a strip's face or any of its blocks to select it. Frog is selected on load. A new show: every puppet starts "When I'm tapped" with no action blocks.
- Panel: palette of start blocks (When I'm tapped; When the drum is tapped; When Frog finishes; When Dragon finishes; When Moon finishes; the selected puppet's own "finishes" block is hidden) and action blocks (Hop right, Hop left, Jump, Spin, Sing, Duck down, Pop up), 60 px tiles in a 4-column grid; under it the newest diary card with its idea row (`Me`, `A friend`, `A grown-up`, 60 px picture buttons: one child pointing to self; two children; an adult beside a child; code icons); then `Places` (curtains icon), `Tell it` (open book, gold), `Mia's show` (star book), `New show` (trash); footer "Your show is saved only on this device."
- Editing (robot engine strip): tap an action tile to add it at the end of the selected strip (or drag it into a slot); tap a start tile to set the selected puppet's start block; the engine's three card buttons (Move earlier, Take away, Move later) under the selected strip. A strip at 4 action blocks plays `full` and adds nothing.
- Running is the real thing: tap a puppet, tap the drum, and finishes start their waiters, exactly as in What Starts It? Puppets keep their places after a run (like real code); `Places` puts every puppet back to its spot, up. A hop past spot 1 or 5 wobbles at the edge and stays.
- Tell it (enabled once the diary holds 2 or more change cards): an overlay covers the theater with the credits card (paper card, title "How I built my show"), the diary as a row of face-down cards (up to 8 a page, page arrows), and the revealed card large in the middle. Panel during Tell: `Next` (gold), `Back`, `Curtain call`, `Close`. Each Next turns the next card over and plays its line. After the last card, `Curtain call` plays the whole show (the tool taps each tap-started puppet left to right with an animated finger, then the drum, 1.5 s apart; finishes follow) and the credits roll on the card. During Tell, a tap on a block in a strip makes the puppet do just that block and speaks its name, then the puppet returns.
- Mia's show: opens the same credits card for Mia's example (Content) with her Dragon program shown on stage, view only; `Back to my show` returns everything as it was.
- New show: a confirm card with two 120 px picture buttons, `Clear it` (trash) and `Keep it` (back arrow).
- At 680x425: palette tiles 44 px; the diary card shows only the newest card's icon and the idea row; Mia's show and New show fold into a `More` button (three dots) that opens them as a two-button card.

## Content
**Blocks** (icons drawn in code, white on blue; spoken names in quotes):
- Hop right "Hop right": one spot right (arrow over a hop arc). Hop left "Hop left". Jump "Jump": up and down in place (up arrow over a bar). Spin "Spin": one full turn in place (circle arrow). Sing "Sing": the puppet's tune, notes float up (music note). Duck down "Duck down": slides behind the ledge (down arrow onto a bar). Pop up "Pop up": rises from behind it (up arrow off a bar). Hop, Jump, Spin, Sing leave a puppet up or down as it was; Duck down and Pop up on a puppet already in that state just nod.
- Start blocks (hat shape, ink icons on yellow): When I'm tapped (a finger on the puppet's own face), When the drum is tapped (finger on a drum), When {Q} finishes ({Q}'s face with a small checkered flag).
- Tunes (code, `Curio.tone`, silent with Sound off): Frog three low bouncy notes; Dragon two low growly notes (sawtooth); Moon three high soft notes. Beat: 900 ms a block (Sing 900 ms too); Motion off: the puppet appears at each block's end state on the same beat.

**Watch and Say shows** (start spot, up or down; prop and its spot; blocks after "When I'm tapped"; end; guess pictures = end plus the two listed):
1. Frog, 2 up; lily pad 4; Hop right, Hop right, Sing; end 4 up (reaches). Others: 3 up, 5 up. Job: "Frog wants to get to the lily pad." why: "Two hops right, and Frog sang on the lily pad."
2. Dragon, 5 up; cave 1; Hop left, Hop left, Hop left; end 2 up (misses). Others: 5 up, 1 up. Job: "Dragon wants to go home to the cave." why: "Dragon hopped left three times. The cave is one more hop away."
3. Moon, 3 down behind a hill; hill 3 (Moon wants to be up above it); Spin, Sing, Jump; end 3 down (misses). Others: 3 up, 4 down. Job: "Moon wants to come up over the hill." why: "Moon spun, sang and jumped, but no block said Pop up. Moon stayed down."
4. Frog, 3 up; rain cloud above 3 (Frog wants to be down, out of the rain); Jump, Sing, Duck down; end 3 down (reaches). Others: 3 up, 2 up. Job: "Frog wants to hide from the rain." why: "Frog jumped, sang, then ducked down. No more rain on Frog!"
5. Dragon, 1 up; campfire 3; Hop right, Hop right, Hop right; end 4 up (misses). Others: 3 up, 5 up. Job: "Dragon wants to sit by the campfire." why: "Three hops right. That is one hop too many!"
6. Moon, 1 up; star 4; Hop right, Hop right, Hop left; end 2 up (misses). Others: 1 up, 4 up. Job: "Moon wants to visit the star." why: "Two hops right, then one hop back left."
7. Frog, 4 up; lily pad 3; Duck down, Hop left, Pop up; end 3 up (reaches). Others: 5 up, 3 down. Job: "Frog wants to sneak to the lily pad." why: "Frog ducked down, hopped left, and popped up on the lily pad. Peekaboo!"
8. Dragon, 3 up; rock 1; Hop left, Sing, Jump; end 2 up (misses). Others: 1 up, 4 up. Job: "Dragon wants to sing on the rock." why: "Dragon hopped left only once, then sang and jumped."
Reaches 3 of 8 (1, 4, 7).

**What Starts It? scenes** (start blocks; actions; question; answer). Order A1, B1, A2, B2, A3, B3, A4, B4, A5, A6.
- A1: Frog tap (Jump, Sing); Dragon drum (Spin, Sing); Moon tap (Sing, Jump). "What starts Dragon?" Drum.
- B1: Frog tap (Sing, Jump); Dragon after Frog (Jump, Spin); Moon after Dragon (Spin, Sing). "When Frog finishes, who moves next?" Dragon (then Moon, after Dragon).
- A2: Frog drum (Spin, Jump); Dragon tap (Sing, Spin); Moon drum (Jump, Sing). "What starts Dragon?" Dragon.
- B2: Frog drum (Jump, Jump); Dragon tap (Spin, Sing); Moon after Frog (Duck down, Pop up). "When Dragon finishes, who moves next?" Nobody.
- A3: Frog after Moon (Sing, Spin); Dragon tap (Jump, Sing); Moon drum (Spin, Jump). "What starts Frog?" Drum (Moon, then Frog).
- B3: Frog after Dragon (Spin, Jump); Dragon tap (Jump, Sing); Moon after Frog (Sing, Spin). "When Dragon finishes, who moves next?" Frog (then Moon).
- A4: Frog tap (Jump, Spin); Dragon drum (Duck down, Pop up); Moon after Frog (Sing, Jump). "What starts Moon?" Frog.
- B4: Frog tap (Sing, Spin); Dragon after Moon (Jump, Sing); Moon after Frog (Spin, Jump). "When Frog finishes, who moves next?" Moon (then Dragon).
- A5: Frog tap (Spin, Sing); Dragon drum (Jump, Spin); Moon after Dragon (Sing, Jump). "What starts Frog?" Frog.
- A6: Frog after Dragon (Jump, Sing); Dragon after Moon (Spin, Jump); Moon tap (Sing, Spin). "What starts Frog?" Moon (Moon, then Dragon, then Frog).
A answers: drum 2, the puppet itself 2, another puppet 2. B answers: Dragon, Nobody, Frog, Moon (one each). No scene has a loop.

**Explain templates** (A, built from the chain): tap: "{P}'s start block says: when I'm tapped." drum: "{P}'s start block says: when the drum is tapped." chain of 2: "{P} waits for {Q} to finish. {Q} starts when {trigger}." chain of 3: "{P} waits for {Q}. {Q} waits for {R}. {R} starts when {trigger}." ({trigger} = "you tap {R}" or "you tap the drum".)

**Mia's show** (Dragon; final program: When the drum is tapped, Sing, Hop left, Spin). Diary cards and their lines:
1. Start set to drum, Me: "First, Mia made Dragon start when the drum is tapped. That was her idea."
2. Added Hop left, Me: "Then she added Hop left."
3. Tried it: "Then she tapped the drum to try it. Dragon hopped left."
4. Added Sing, A friend: "Her friend Leo said, add Sing! So she added Sing."
5. Moved Sing earlier, A friend: "Leo helped again. She moved Sing before Hop left, so Dragon sings first."
6. Tried it: "She tried it again."
7. Added Spin, A grown-up: "Her teacher helped her add Spin at the end."
8. Tried it: "She tried it one more time. Dragon sang, hopped left and spun. The end!"

**Build diary** (one card per change; max 24 cards, then `diaryFull` once and edits are no longer logged): kinds add, take away, move (earlier or later), start set, tried it. Consecutive "tried it" cards merge into one; consecutive moves of the same block merge into one card with the net direction (a net of zero removes the card). Each change card has a helper tag (Me, A friend, A grown-up, or none, shown as "?"). A card is a picture: the puppet's face, then a plus, minus or swap mark, then the block's icon (start set: the hat icon); tried it: a finger icon with a spark.

**Tell lines for the class's own show** (templates): starter "First," for card 1, "Then," for the middle cards, "At the end," for the last. add: "{starter} you gave {P} {block}." take away: "{starter} you took {block} away from {P}." move: "{starter} you moved {P}'s {block} {earlier/later}." start: "{starter} you made {P} start {event phrase}." tried: "{starter} you tried it." Helper add-ons: Me "That was your idea." A friend "A friend helped." A grown-up "A grown-up helped." none: nothing spoken; the card shows "?". Event phrases: "when it is tapped", "when the drum is tapped", "when {Q} finishes".

## Interactions in detail
- Every tap acts at once, including during a run: a start event for a program already running restarts that program from its first block (Watch and Say and What Starts It? first put the stage back in place; Build keeps puppets where they are). Mode buttons, Next show, Next scene, Play again and Places stop all runs at once.
- Watch and Say: a guess can change until the run starts. Tapping the puppet with no guess runs it; the guess pictures fade and the result has no check (no "look again" either); the stage still shows the job badge. Tapping a block tile before or after a run speaks its name and wiggles the tile's icon (no puppet movement, so it cannot preview the end). Next show while a line plays drops the old show's lines.
- What Starts It? kind A: the first tap after the question is judged. Right (the named puppet starts, directly or by chain): `aRight` with the explain line, after the chain has run to the named puppet's start. Wrong: the tap still does what it does, then `aWrong` (one of three forms, see Voice). A second wrong tap: the named puppet's start block glows and a dotted line draws from it back along the chain to its trigger; `aShow`. When the named puppet finally runs, the explain line plays without the check. Further taps are free play; `waiting` plays once per puppet per scene.
- Kind B: a stage tap before any pick still acts (sandbox), but the three picture buttons fold away unanswered and no check or look again is given for that scene (as a K run with no guess); the hint becomes the Next scene line. Otherwise the three picture buttons lock after a pick; the tool runs X; at X's finish the waiter (if any) starts and the feedback line plays; the true answer's button gets a ring and, if different, the pick gets "look again". Play again resets and unlocks nothing (the question is answered); free play continues.
- Build: adding, removing, moving or changing a start block resets nothing on stage. A change logs a diary card and shows the idea row on it; tapping an idea button tags the newest untagged change card (it can be retagged by tapping another). Loops (Frog after Dragon and Dragon after Frog, or a 3-loop) are allowed; when a tap reaches a puppet in a loop, `loop` plays once per loop per load. `Tell it` with the selected run going stops the run first. Closing Tell returns to Build with nothing lost. Save after every change; on load, the saved show and diary come back and the hint is the try line.
- Extremes: a strip at 4 action blocks; a hop at spot 1 or 5 (edge wobble, `edge` once per puppet per load); Duck down on a down puppet (nod); a diary of 24 cards; Tell with 2 cards (Next, Next, then Curtain call); Curtain call with nobody tap- or drum-started (the card says "Nobody can start!" and `noStart` plays).
- Resizing mid-run keeps each puppet's spot and the run's beat.

## Look
- Accent `--brand` #4a3a8c velvet indigo (header, mode buttons, selected strip border, curtains match it); gold #f0b43c for Next show, Next scene, Tell it, Next; paper #f7f4ec; ink #1f1b2d; muted #5b566a; start blocks yellow #f2c14e with ink icons and a 2 px ink outline; action blocks blue #2d5f9a with white icons; running ring #c2255c outside the block with a 3 px paper gap; check green #2e7d4f with a check icon. Scene: warm honey wood, indigo velvet, a soft green meadow backdrop.
- Different from the K-2 CS neighbors and the puppet tool: line-leader-picker leaf green #1d6b3a, puppet-show-feelings jade #0b7a5f (cardboard and a red curtain; here wood and indigo).
- Contrast (WCAG 2.1, computed): white on brand 9.23:1; brand on paper 8.40:1; ink on paper 15.25:1; muted on paper 6.40:1; ink on gold 9.02:1; ink on start yellow 9.99:1; white on action blue 6.53:1; action blue edge on paper 5.94:1; running ring on paper 5.15:1 (non-text); check green on paper 4.59:1 (with an icon).
- Never color alone: start blocks are hat-shaped, action blocks square; running is ring plus scale plus chevron; right is a check icon, look again a ring with an eye icon.

## Art
One style for all: soft watercolor and colored pencil picture book, warm library light. Local FLUX (`scripts/localart.py`); no people. Hand puppets are seen from the waist up, lower edge hidden by the ledge (cut flat at the bottom).
- theater: "A small wooden tabletop puppet theater in a school library, honey wood frame, indigo velvet curtains tied back, a blank wooden sign board on top, the stage opening plain white, watercolor and colored pencil"; 16:9; cutout yes (opening cut out); people no; frames every mode.
- meadow: "A soft green meadow under an evening sky with a small pond on the right, gentle hills, watercolor and colored pencil, full frame"; 16:9; cutout no; people no; backdrop inside the opening.
- library-wall: "A cozy school library wall with wooden shelves of books with plain blank spines, warm light, watercolor and colored pencil, full frame"; 16:9; cutout no; people no; behind the theater.
- frog-rest, frog-sing, frog-wait: "A green felt frog hand puppet with big round button eyes and a wide smile, <mouth closed / mouth wide open singing / looking up with a curious tilt>, front view, flat bottom edge, watercolor and colored pencil, plain white background"; 3:4; cutout yes; people no; Frog's poses (wait = the waiting wiggle). Jump, hop, spin, duck are code transforms of the rest pose.
- dragon-rest, dragon-sing, dragon-wait: "A purple felt dragon hand puppet with soft green horns, small felt wings and a friendly face, <...the same three poses>"; 3:4; cutout yes; people no.
- moon-rest, moon-sing, moon-wait: "A pale yellow crescent moon puppet made of felt on a wooden stick, with a gentle sleepy face, <...the same three poses>"; 3:4; cutout yes; people no.
- Props (cutout yes, people no, plain white background): lily-pad 4:1 ("a round green felt lily pad with a pink flower"); cave 1:1 ("a small grey felt cave opening"); hill 4:1 ("a rounded green felt hill"); rain-cloud 4:3 ("a grey felt cloud with blue raindrops"); campfire 1:1 ("a felt campfire with orange flames and logs"); star 1:1 ("a yellow felt star on a string"); rock 4:3 ("a smooth grey felt rock"); drum 1:1 ("a small round hand drum with a wooden rim and a cream drumhead").
22 images, none with people. Drawn in code: blocks and icons, strips, spot dots, mini stages (composited from the cutouts), sparks, rings, the idea-row icons, the diary cards, the credits card, all controls and text.

## Voice
Bank voice `curious-librarian` (Aoede). Style line: "Say curiously and warmly, like a friendly school librarian running the puppet corner." She is the voice of the library stage; the puppets only sing (code tones). Not used by any K-2 CS neighbor (robot-dance lively-host, snowy-mail-route gentle-storyteller, loop-garden hero-coach, input-or-output big-sister, line-leader-picker friendly-dad, computer-builder bright-teacher) or by puppet-show-feelings (smooth-narrator), and not one of the last batch's five. `Curio.voice` with `scope: () => state.mode + ':' + state.item` (item = show, scene or tell page), `welcomeAfter: true`. Templates in braces are expanded by the builder over Content; every expansion goes in voice/lines.json. Repeats: how lines once per load then hint only; event lines every time unless noted.

Watch and Say:
- how `wWatch` (welcome; stale once a run ends): "Welcome to the library puppet stage! Each puppet has blocks. The blocks tell it what to do, one at a time."
- event, whole, `show` (show opens): "{job} Where will {P} be at the end? Tap a picture, or tap {P} to start."
- event `guessed` (each guess tap; stale when the run starts): "Good guess. Now tap {P} to start the blocks."
- event, whole, `reach` / `miss` (run ends): "{P} got to the {prop}!" / "{P} did not get to the {prop}."
- event `match` / `lookAgain` (after reach or miss, only if there was a guess): "Your picture matches the stage!" / "Look again. Your picture and the stage are different."
- event `sayIt` (after that, every show): "What did {P} do? Say it out loud, block by block. Then tap Hear it."
- how `stepHow` (first show only, after sayIt): "Tap Step to watch one block at a time, or tap Next show."
- event `stepName` (each Step): the block's name. event `stepDone` (Step past the last block): "That's all the blocks. {P} is done."
- event, whole, `why` (Hear it): the show's why line.
- event `blockName` (block tile tap): the block's name.
- event, whole, `allShows` (Next show after show 8): "That was all eight shows! Here is the first one again."

What Starts It?:
- how `wStarts` (welcome; stale on any stage tap): "Look at the start block at the front of each strip. A puppet waits until its start block happens."
- event, whole, `askA`: "What starts {P}? Tap it on the stage." event, whole, `askB`: "When {X} finishes, who moves next? Tap a face, or tap Nobody."
- event, whole, `aRight` (waits for the chain to reach P): "{P} started! " + explain.
- event `aWrong`: tapped puppet waiting: "{Q} is waiting too. Look at {P}'s start block, then tap again."; something else ran: "That started {Q}. {P} is still waiting. Look at {P}'s start block, then tap again."; drum with no listener: "Nobody was waiting for the drum. Look at {P}'s start block, then tap again."
- event `aShow` (second wrong): "{P}'s start block is glowing. Follow the dotted line, then tap there."
- event `bWatch` (B pick): "Let's watch {X}." event, whole, `bRight` / `bWrong` (at X's finish): "{Y} was waiting for {X}. You got it!" or "Nobody was waiting for {X}. You got it!" / "Look again. {Y} was waiting for {X}." or "Look again. Nobody was waiting for {X}."
- how `nextHow` (first answer only): "Tap Next scene for a new one."
- event `waiting` (once per puppet per scene, free play): "{Q} is waiting for {event phrase}."
- event, whole, `allScenes`: "That was every scene! Here is the first one again."

Build and Tell:
- how `wBuild` (welcome; stale once a block is placed): "Now you are the builder. Give each puppet blocks, try them, and keep track of who helped."
- how `pickHow` (stale once a block is placed): "Tap a block to give it to {P}. Tap a puppet's face to build for that puppet."
- event `added` (each add): "{block} for {P}." event `startSet`: "{P} starts {event phrase}."
- how `ideaHow` (first change card): "Whose idea was that? Tap Me, A friend, or A grown-up."
- event `tagged`: "Your idea!" / "A friend helped." / "A grown-up helped."
- how `tryHow` (first time a strip has an action block; stale once that puppet runs): "Now try it. {trigger}." ({trigger}: "Tap {P}", "Tap the drum", "Start {Q} first".)
- event `waiting` (once per puppet per change): as above. event `loop` (once per loop): "{P} is waiting for {Q}, and {Q} is waiting for {P}. Nobody starts!"
- event `edge` (once per puppet per load): "{P} bumped the edge of the stage." event `full` (once per puppet per load): "{P} has four blocks. Take one away to add another."
- how `tellReady` (after the 3rd change card): "When you're ready, tap Tell it to tell how you built your show."
- event `diaryFull` (once): "Your diary is full. Tap Tell it, or start a new show."
- Tell: how `tellFirst`: "What did you do first? Say it, then tap Next." how `tellNext`: "What did you do next? Say it, then tap Next." event, whole, `tellCard`: the card's line. event, whole, `tellEnd`: "That's how you built it! Tap Curtain call to watch your show." event, whole, `curtain`: "A puppet show by you." plus "Helpers: a friend." / "Helpers: a grown-up." / "Helpers: a friend and a grown-up." when tagged. event `noStart`: "Nobody can start! Give a puppet a tap or drum start block." how `blockHow` (after tellEnd, once): "Tap a block on a strip and say what it does."
- Mia: event, whole, `miaOpen`: "This is how Mia built Dragon's show. Listen, then tell it back." then `miaCard` 1 to 8 (Content), one per Next.
- event `clearAsk`: "Clear your whole show? Tap Clear it, or tap Keep it."

Read speaks the hint, which always names the current step's action and control and never names a disabled control (Step, Hear it, Play again before a run; Tell it before 2 cards).

## Family engine
Catalog family: none. But do not write a second card engine: use `kit/robot.js` (docs/families/robot.md) for each strip and its runner: one `Robot.program` per puppet (`max` 5: the start block is card 0 and is set by `replace(0, ...)`, never moved or taken away; `canEdit` false in Watch and Say and What Starts It?), `Robot.strip` with `layout: 'row'`, K-2 card buttons 60 px, and one `Robot.run` per puppet, `style: 'sequence'`, `beat: 900`, `exec` moving the puppet. The events (tap, drum, finishes) live in the tool: a finished run's `onEnd` fires the waiters. Several runners walk at once. If the engine needs a change for a fixed card 0, it goes into the engine and robot.md in the same change (robot.md rules).

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Watch and Say guess (EK-PRO-RD-06) | Guessing; the picture at the prop (the job's goal); "nothing changes" (the start picture); the picture farthest from the start; nearest; counting only right hops; treating every hop as right; first block only; last block only; the answer's position; peeking at a preview; mashing; doing nothing | Computed over the 8 shows (k2.py): guess 33 percent; at the prop 3 of 8 (38 percent, only 3 shows reach); start picture is offered in 4 shows and right only in show 3, where no Pop up is the lesson; farthest 6 percent; nearest 25 percent; first block only 38 percent; last block only 38 percent; every hop right fails all 3 shows with a left hop (2, 6, 8); counting only right hops scores 56 percent, all of it on shows 1 and 5 (only right hops, so counting them is reading the blocks), show 3 (no hops) and coin-flip ties on 6, 7, 8; it fails 2 and 4 outright. Picture order is shuffled each time a show opens; the mini stages are one size. Tile taps speak a name and never move the puppet. The guess locks when the run starts, and the true end appears only after. No guess means no check. There is no score to mash. |
| Step and Hear it describe (EK) | Hear it first, then repeat the model | The `sayIt` line asks the class first and Hear it is a separate tap, so the teacher controls order; the model is a check, not the task. Not scored. |
| What starts P (A, E1-PRO-RD-06) | Tap the named puppet (the common wrong answer); always the drum; always one puppet; guess; mashing; reading only P's own start block | (g1c.py) Named puppet right 2 of 6; drum 2 of 6; any one puppet 1 or 2 of 6; guess 25 percent; only the first tap is judged, so mashing earns one random first tap. Reading P's start block is the skill for direct starts, and it fails both chains whose source is not a tap (A3 and A6: tapping the face on the start block finds a waiting puppet and nothing runs). The dotted line and glow appear only after two wrong taps. |
| Who moves next (B, E1) | Always Nobody; the puppet to the right of X; any puppet with a "finishes" start block; guess; reading the answer off an earlier run | Nobody 1 of 4; to the right 1 of 4; any finishes block 38 percent (every B scene has a second waiting puppet that waits for someone else, so the face on the block must be X's); guess 33 percent. One question per scene and nothing runs before it, so no earlier run shows the answer; running it on the stage before picking folds the face buttons away with no check; the B demo starts X with a "Go" spark, not its trigger. |
| Build diary and Tell (E2-PRO-RD-06) | Tapping Next without saying anything; tagging every card "Me"; never tagging | Not scored by design (a sandbox and the CSTA boundary: explain verbally, sentence starters allowed). The prompt before each card asks the class to say the step first; the reveal is the check. Untagged cards show "?" and the card asks "Who had this idea?" on screen; the curtain credits list only the helpers tagged, so the teacher sees what was tagged. |

## Heard in order
Waits means the next line waits for it to finish; taps always act at once and never wait for a line.
1. Watch and Say, load: first tap on a picture: `guessed`, then `wWatch` (after it). First tap on Frog: the run plays (tunes only), then `wWatch` (welcomeAfter), then at the run's end `reach`/`miss` waits for it. Next action: in the hint and `guessed` ("tap Frog").
2. Each show: `show` (whole). A guess: `guessed`. The run: tunes only. Run ends: `reach` or `miss` (whole), then `match` or `lookAgain` (if guessed), then `sayIt`, then `stepHow` (first show only). Each waits for the one before. Next action spoken in `sayIt` (Hear it) and `stepHow`.
3. Step: `stepName` per tap (a new tap cuts it and speaks the next name); after the last, `stepDone`. Hear it: `why` (whole). Next show: drops the old lines, then `show`.
4. What Starts It?, each scene: `wStarts` (first scene, once), then `askA` or `askB` (whole, waits for wStarts). A taps: the chain runs; then `aRight` (whole, waits for the named puppet to start) or `aWrong`, and a second wrong `aShow`; after the first answer `nextHow`. B: pick, `bWatch`, X runs, then `bRight`/`bWrong` (whole) at X's finish, then `nextHow` (first time). Feedback always plays before Next scene's `askA`/`askB`, which waits for it.
5. Build: first tap on a tile: `added` (or `startSet`), then `ideaHow` (first change), then `wBuild` (welcomeAfter), then `tryHow`. Later changes: `added` or `startSet` only; a tag: `tagged`; after the 3rd change card: `tellReady`.
6. Tell: `tellFirst`, then each Next: `tellCard` (whole) then `tellNext` (first time only; hint after). After the last card: `tellEnd` (whole), then `blockHow`. Curtain call: `curtain` (whole) after the show ends. Mia: `miaOpen` (whole), then each Next `miaCard` (whole); a Next tapped while a card line plays turns the card at once and queues its line after the current one (it is not cut).
No line contains a bare letter or letter sound; block names are spoken as words.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| EK-PRO-RD-06 "Describe how a sequence of commands completes a task" (describe what happens when simple code runs, in own words) | CSTA, 2026 CSTA PK-12 Computer Science Standards (CC BY-NC-SA 4.0), statement and boundary statement, p. 56 | Same document, Appendix B, Kindergarten table, p. 189 (one official publisher; no second publisher exists for a new standard) | yes |
| E1-PRO-RD-06 "Explain the function of code that includes an event and sequence" (a tap or collision event starts an animation) | CSTA 2026, p. 56 | CSTA 2026, Appendix B, Grade 1, p. 190 | yes |
| E2-PRO-RD-06 "Explain the steps taken to create a program" (own ideas vs help from a peer or teacher; sentence starters allowed) | CSTA 2026, p. 56 | CSTA 2026, Appendix B, Grade 2, p. 191 | yes |
| Block programs for young children start with an event block such as a tap on the character | ScratchJr reference page (ScratchEd, Harvard): "Start on Tap" | Boston College DevTech ScratchJr Block Guide (sites.bc.edu/scratchjr/learn-block-guide) | yes |
| One character can start another's script (it sends a message; scripts waiting for it start) | ScratchJr reference page: Send Message, Start on Message | BC DevTech Block Guide, Start on Message | yes |
| One event can start several scripts at once | ScratchJr reference page: every script with that message color starts | Scratch Wiki, "When This Sprite Clicked" and broadcast blocks (each script wearing the hat runs) | yes |
| Blocks in a script run one at a time, in order | ScratchJr reference page | BC DevTech Block Guide | yes |
Backed twice: 7 (the three CSTA wordings from two places in the one official document, said so). Cut: 1 ("tapping a running sprite restarts its script": not confirmed by either source; the tool still restarts, as its own behavior, and never says it as a fact). "When Frog finishes" is the tool's stand-in for a message sent at a script's end; teacher notes say so. Puppet names, jobs and Mia's story are story content, not claims.

Checks run (Python, scratchpad ttp/k2.py, g1c.py, 2026-11-07):
- Watch and Say: every show's end state recomputed from its blocks; all three pictures distinct; reaches 3 of 8. Strategy rates in "Can it be beaten?" (the first draft let "nearest to the start" win 6 of 8 and "at the prop" 5 of 8; distractors and show 3 were changed until no strategy without reading the blocks beat 38 percent, and the two that hit 50 percent or more fail every show that tests the block they ignore).
- What Starts It?: no loops; every A question has exactly one tap target that starts the named puppet (checked over all four targets); every B answer unique. An earlier draft asked two questions per scene and the first run showed the second answer in 4 of 6 scenes; changed to one question per scene. A one-hat reader gets 4 of 6 A questions, failing both non-tap chains.
- Contrast ratios as in Look.

## Done when
1. Focus and fold: at 1366x768 the theater, the strip row, the hint and every mode's controls (guess pictures, Step, Hear it, Next show; B face buttons, Next scene; palette, idea row, Places, Tell it) show with no scroll; at 680x425 the theater, strips and the next action's control show with no scroll and text is 10 px or more.
2. Watch and Say: each of the 8 shows ends in the end state listed; the picked picture gets a check or look again and the true end appears only after the run; 3 shows reach and 5 miss, each with its badge. (EK-PRO-RD-06)
3. Describing: after every run `sayIt` asks the class first; Step plays one block a tap with its name; Hear it plays the why line only when tapped. (EK-PRO-RD-06)
4. What Starts It? A: tapping a waiting puppet only wiggles it; the drum starts every drum puppet together; finishes start waiters with a visible spark; only the first tap is judged; two wrong taps draw the dotted line; the explain line names every link of the chain (A3 and A6). (E1-PRO-RD-06)
5. B: the demo starts X with no trigger shown; who follows matches the strips; Nobody is right in B2. (E1-PRO-RD-06)
6. Build: start blocks and up to 4 action blocks per puppet; taps, drum and finishes run the class's own programs; loops play `loop`; each change logs one diary card (tries and same-block moves merge) with a helper tag; the show and diary survive a reload, with the on-device line shown. (E2-PRO-RD-06)
7. Tell it: every card is face down until Next; the prompt asks for the step before the reveal; card lines match the diary; Curtain call plays the show and lists only tagged helpers; Mia's show plays its 8 cards and returns to the class's show unchanged. (E2-PRO-RD-06)
8. Tap while it plays: tapping a puppet, the drum, Next show or a mode button during a run acts at once; no older line plays after a newer one; a restart starts from the first block.
9. Pre-reader: every question, choice and next action is spoken; every choice is a picture; a child alone with Sound on can play each mode without reading.
10. Voice: five Next shows in a row play `show` five times; `stepHow`, `nextHow`, `ideaHow`, `tryHow` play once each; `waiting` once per puppet per scene; no line names a disabled control.
11. Motion off: hops, spins, ducks and sparks appear at their end states on the same 900 ms beats; no network requests.

## Open questions
- None for Cory. Note for the integrator: this tool is family none in the catalog but uses `kit/robot.js` (a fixed start card, several runners at once); robot.md's tool table could list it after build.
