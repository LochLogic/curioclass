# Push the Pumpkin

## One idea
On a fall farm path every push leaves a flag where the thing stopped, so a kindergarten class sees with their own eyes that a bigger push sends it farther, a push from the other side sends it the other way and a push can stop it, then judges with a thumbs up or down whether their own ramp and board design really got the ball into the barn.

## Not like
- shade-builder (K science, builder): designs shade against the sun and compares heat. Here the design changes how a ball moves, and the class judges each run from where the ball stopped.
- vibration-station (grade 1 science, lab): same predict-then-test rhythm and lab-book pages. Here every test is two lanes side by side, compared by stop flags and counted fence posts, the record is a barn-wall board of flags, and the design part is a field puzzle the class judges, not a device they build and fix. Its own voice and accent.
- tug-of-war-arena (grade 3): balanced and unbalanced forces read from arrows. Here one push at a time and no force arrows to add; each test changes strength or direction, never both (the K-PS2-1 boundary).
- marble-ramp-trials (grades 3-5 computer science): times a marble on a ramp to see data vary. Here no timing; the ramp is a design piece that makes a ball faster.
- magnet-maze (grade 3): steers a ball with magnets it never touches. Here only touching pushes and pulls (K-PS2 leaves magnets out).
- me-vs-the-counter (K computer science): counts a bouncing ball. Here the ball is pushed and how far and which way it goes is the point.
- curling-stones (grade 11): F = ma predicts stopping distance. Here no numbers beyond counting fence posts.

## Who and how
- Kindergarten, science, module "Pushes and Pulls" (science-k-pushes-and-pulls). Standards: K-PS2-1, K-PS2-2.
- Driver: teacher on a projector (tool.json `driver: "teacher"`). The class says guesses out loud and shows thumbs; the teacher or a child taps. Every question, choice and next step is spoken, and every choice is a picture with one word, so a child alone at home can play (BASELINE rule 4).
- Minutes: Push 3 to 5; Find out 10 to 12; Barn 10 to 15. One long period or two short ones.
- No personal prompts. Nothing is stored; flags, pages and tries last for this page load only.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K-PS2-1 strength | Push: give the ball, pumpkin or wagon a Small, Medium or Big push. Find out 1 and 2: predict, run two tries that differ only in push size, then tap the one that went farther | Two lanes, each with a stop flag; post dots under each flag after a miss; Big always beyond Medium beyond Small for one object | 3 |
| K-PS2-1 direction | Push: push to the barn, push to the gate, pull the wagon. Find out 3 and 4: predict which way before the test | The wagon rolling the other way when Jo moves to the other side; the wagon following Jo on a pull | 4 |
| K-PS2-1 stopping a moving thing | Find out 5: the ball rolls past Jo, then Jo gives the rolling ball a small push back | The ball stopping at Jo's hands, its flag beside her | 4 |
| K-PS2-1 plan a fair investigation | Find out 2: pick the try two that changes only the push (pumpkin) over the one that changes the push and the object (ball) | An unfair run plays but is rejected with the reason; only the fair run fills the page | 5 |
| K-PS2-2 analyze whether a design works as intended | Barn 1 to 3: place a ramp, bale or board, roll, judge each run with a thumbs up or down from where the ball stopped, change the design; after a success, watch a no-piece ghost ball beside the real one and say what the piece changed (faster, or which way) | The ball's stop spot and trail; the door shut until the class judges; the try strip of designs with "we said / it was"; the ghost race | 6, 7 |

## Screens and modes
Header (kit): title "Push the Pumpkin"; mode buttons (`.seg`, icon plus word, 60 px): `Push` (open hand, default), `Find out` (magnifier), `Barn` (barn); then `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 and 44 px at 680x425, each a picture with one word. Layout at 1366x768: stage about 1036 x 700 on the left, panel 330 px on the right, hint at the top of the panel (22 px). At 680x425 the panel is 210 px, stage and panel stay side by side.

**On load and first tap.** Push opens with the ball at the middle of the path, Jo standing at its gate side, Medium and Push to the barn picked. Nothing speaks before the first tap (kit). First hint: "Tap Go to give the ball a push." A first tap on `Go` pushes at once and queues `firstPush`, so the welcome is skipped (BASELINE 16); what it said is in the hint and Read. A first tap anywhere else without its own line gets `welcome`.

**Push** (explore). Focus: the path with the object, Jo and the stop flags; it fills the stage. The painted path runs left to right across the middle: a gate at the left end, the barn at the right end. Fence posts (code, 13 of them, one every 76 px, the middle post marked as the start) stand behind the path; the object starts at the middle post. Panel, top to bottom: hint; `Ball`, `Pumpkin`, `Wagon` (pictures 90 x 90); `Small`, `Medium`, `Big` (code arrows of three lengths, 90 x 70); `To the barn` (Jo on the gate side, arrow toward the barn), `To the gate` (Jo on the barn side, arrow toward the gate), `Pull` (Jo by the barn holding the handle; shown only when Wagon is picked); `Go` (gold, 300 x 80, Jo picture); `Clear flags` (broom, 60 px). A choice tap moves Jo and redraws the arrow at once. Each Go: Jo's push pose, the object rolls (the wagon's wheels turn, the pumpkin turns slowly), and a flag (navy pin with a small picture of the object and the push arrow) is planted where it stopped. Up to 8 flags stay; the oldest fades. The object slides back to the middle post 0.8 s after it stops.
At 680x425: object tiles 52 x 44, size and side tiles 52 x 44 in rows of three, Go 190 x 48, flags 20 px.

**Find out** (five tests in order; step strip of five pumpkin icons at the top of the stage, done ones filled). Focus: two lanes, one above the other, each about 1036 x 270, with the same post marks, a start post in the middle and a "Try 1" or "Try 2" badge (picture of the object and its push) at the left end. Above them the question card (picture plus words, 64 px). Panel: hint, then the step's picture cards (150 x 110, up to three, order shuffled per test) or plan cards, then `Go` (gold) for the next try, then `Next` (gold, arrow) after a result. The cards for a prediction lock when tapped (the others grey and cannot be tapped); `Go` appears only after the prediction (or the plan) is in.
1. Q1 ball, push size. Try order random: small then big, or big then small. Cards: `Small push` (short arrow), `Big push` (long arrow), `Same` (two equal arrows) for "Which ball will go farther?". Go twice, then compare: both lanes' badges hide and the class taps the ball that went farther. A wrong tap shows dot counts (one dot per post from the start) under each flag; the first tap is recorded honestly.
2. Q2 pumpkin, fair test. Try 1 is the pumpkin with a random size (Small or Big). Predict: "Will the other push send the pumpkin farther?" Cards `Farther`, `Not as far`, `Same`. Plan: two try-two cards, `Pumpkin` with the other size and `Ball` with the other size. Go runs Try 1, then Try 2. An unfair Try 2 rolls, then `unfair` plays, the lane clears and the plan cards come back with the Ball card greyed. Fair: compare tap as in Q1.
3. Q3 wagon, direction. Try 1: Jo pushes the wagon to the barn (Medium). Then the question: Jo walks to the barn side. Cards `To the barn`, `To the gate`, `Stays still`. Try 2 rolls it to the gate.
4. Q4 wagon, pull. Try 1: Jo pushes it to the barn from the gate side. Question: Jo stands on the barn side holding the handle. Cards `Toward Jo`, `Away from Jo`, `Stays still`. Try 2: Jo walks backward 2 posts toward the barn and the wagon follows.
5. Q5 ball, stopping. The ball starts at the gate end and rolls toward Jo (standing 2 posts on the barn side). Try 1: Jo steps aside and the ball rolls past to 5 posts. Question: Jo will give the rolling ball a small push back. Cards `Keeps going`, `Stops`, `Goes back`. Try 2: Jo pushes as it reaches her and it stops at her hands.
After each test the two lanes shrink into a flag card pinned on the "Our tests" barn wall (shown after Q5). End page: three groups, each card with "We thought" and "We saw" pictures: "Bigger push, farther" (1, 2), "Other side, other way. A pull brings it close" (3, 4), "A push can stop it" (5). Buttons `Barn` (gold), `Push`.
At 680x425: lanes about 400 x 150, question card 40 px, cards 90 x 70, step strip icons 28 px.

**Barn** (three puzzles; level strip of three barn icons in the panel). Focus: the farm field seen from high above at an angle (about 1036 x 610), with a dirt path left to right, Jo at the left end and the ball beside her; under it the try strip (1036 x 80): one small card per try, the design's piece icons and, once judged, "we said" thumb and "it was" icon (barn with ball, or ball outside). Panel: hint, level strip, the tray (piece tiles 130 x 100, 2 x 2), `Roll` (gold, ball picture), `Next` (gold) after a level ends. Placing: tap a tray piece (it lifts), then tap a glowing spot; every spot that piece may use glows (never only the right one). Tap a placed piece to put it back in the tray. Drag also works. One of each piece. Roll: Jo gives her push, the ball rolls (about 3 s) leaving a trail of dots every 0.2 s (spread dots mean fast). When it stops, `Roll` is replaced by `Yes` (thumbs up) and `Not yet` (thumbs down), 140 x 100 each, until the class judges. Only then does the door open (worked) or a dark dashed ring circle the ball (not worked). Pieces stay; after judging, `Roll` comes back.
- Level 1 "Get the ball into the barn". Barn at the right end, door at post 6; Jo's push is Small. Tray: `Ramp`, `Bale`. Spots: Start (ramp only: the ball starts at the ramp's top), post 3 and post 4.5 (ramp or bale; a ramp there makes the ball roll up it).
- Level 2 "Turn the ball into the barn". Barn above the path with its door over post 4; a pond at the path's right end; a pumpkin patch along the bottom. Push Medium. Tray: `Board up`, `Board down` (a plank slanted to turn the ball up toward the barn or down toward the patch), `Bale`. Spots: posts 2, 4, 6. One board at a time.
- Level 3 "Knock down the buckets". Barn above the path, door over post 5, three stacked tin buckets just inside. Push Small. Tray: `Ramp`, `Bale`, `Board up`, `Board down`. Spots: Start (ramp), posts 3, 5, 7.
After a worked level 1 or 2, the ghost race plays (a faded ball runs the no-piece path beside the real ball, at the same time), then two analysis cards: level 1 `Faster` (spread dots) / `Slower` (close dots); level 2 `Which way` (curved arrow) / `How fast` (speed lines). First tap recorded; then `Next`.
What the picture shows for every outcome: short, the ball stops on the path one post before the door; up ramp, it climbs part way, rolls back and stops before the ramp; bounce, it hits the bale and rolls back 1 post; wall, it turns and stops against the barn wall beside the door; patch, it turns down and stops among the pumpkins; pond, a splash and the ball floats; hay, it rolls past the barn into a hay pile at the path's end; wobble, the buckets rock and stay stacked; worked, the ball rolls through the doorway (level 3: the buckets tumble). The door and the buckets show their result state only after the judging tap, except the tumble and wobble, which are the data.
At 680x425: field about 440 x 260, try strip folds to a row of 24 px dots (filled when judged), tray tiles 60 x 50, thumbs 90 x 60.

## Content
**Push distances** (posts from the start, then a random +-0.15): Ball 1.5 / 3 / 5; Wagon 1 / 2 / 3.5; Pumpkin 0.5 / 1.5 / 2.5 for Small / Medium / Big. Pull: the wagon follows Jo 2 posts. Rolls slow evenly to a stop; a roll lasts 0.9 s + 0.3 s per post (all under 2.5 s). These are a tool's values, not measured claims; only their order is taught.
**Barn outcomes** (rule table; the ball meets pieces in path order and the first piece it reaches decides):
- Level 1: no piece, short (stops at post 5); ramp at Start, worked; Start ramp plus a bale, bounce off the bale; ramp at 3 or 4.5 with no Start ramp, up ramp (stops at 2.5 or 4); bale at 3 or 4.5, bounce (stops at 2 or 3.5). 10 designs, 1 works.
- Level 2: nothing, pond; Board up at 4, worked; Board up at 2 or 6, wall; Board down anywhere, patch; bale first, bounce. 22 designs, 2 work (Board up at 4, with or without a bale after it).
- Level 3: without the Start ramp the ball reaches post 6: Board up at 3, wall; Board up at 5, wobble; nothing, short (stops at 6). With the ramp: Board up at 5, worked; Board up at 3 or 7, wall; nothing, hay; Board down, patch; bale first, bounce. 44 designs, 2 work.
**Jo**: a farm kid about six years old. **Names on screen**: Ball, Pumpkin, Wagon, Small, Medium, Big, To the barn, To the gate, Pull, Go, Ramp, Bale, Board up, Board down, Roll, Yes, Not yet.

## Interactions in detail
- Every tap acts at once. A Go during a roll ends that roll on the spot (its flag is planted where it would have stopped) and starts the new push. Choice tiles change Jo and the arrow at once, even mid-roll. Motion off: the object appears at its stop spot after the same roll time; Jo shows the push pose then the stand pose.
- Push: Pull is hidden unless Wagon is picked; picking Ball or Pumpkin while Pull is on switches to To the barn. Clear flags removes all flags. Lines in this mode never repeat.
- Find out: Go is hidden until the prediction (and in Q2 the plan) is in, so no try runs before the guess; the compare tap is live only after Try 2 stops; badges return after the compare. Next shows only after a page fills. A mode switch keeps the test's place for this page load; a pinned card tapped on the barn wall reopens that test from its question.
- Barn: Roll with no pieces is allowed (and asked for on level 1). Tapping a spot that is not glowing does nothing. While the ball rolls, tray and spots stay live: a change takes effect at the next Roll and the spot shows it at once. Roll during a roll restarts it. After 6 tries without success, the hint adds the level's goal again ("We need the ball to go faster" / "to turn" / "to go faster and turn"); it never names the piece or the spot. Reset: switching to Barn returns to the first unfinished level with its pieces as left.

## Look
- Accent `--brand` #b04a00 pumpkin orange (header, mode buttons, step strip); hay gold #f0c34a for Go, Roll, Next; paper #fdf7ec; ink #2b2118; muted #64574a; path #c9a272; field #8fb55a; sky #d8ecf5; flags and post dots navy #174a6e; miss ring ink, dashed. Different from vibration-station berry #9b2f6e, estimation-station brick #9c3520, line-leader-picker green #1d6b3a and bus-stop blue #2b4c7e.
- Contrast (WCAG 2.1, computed): white on brand 5.49:1; brand on paper 5.15:1; ink on paper 14.77:1; muted on paper 6.56:1; ink on gold 9.46:1; ink on path 6.67:1; ink on field 6.69:1; ink on sky 12.93:1; white on navy 9.37:1; navy on path 3.97:1 and on field 3.98:1 (non-text, over 3:1). Worked and not worked differ by shape (open door versus dashed ring), never by color alone.

## Art
One style: bright painted picture book, a sunny fall farm. Jo goes to Gemini with `people: true` and onto Cory's contact sheet with the fresh representation check (BASELINE 11); everything else may use local FLUX. Labels stay in code.
- farm-path: "A sunny fall farm with a long straight dirt path running left to right across the middle, a split-rail fence behind it, a wooden gate at the far left, orange trees and pumpkins in the grass"; 16:9; cutout no; Push. The barn at the right end is the barn-side cutout.
- farm-lanes: "Two straight parallel dirt lanes running left to right across a grassy fall field, low hay bales at both ends, orange trees far behind"; 16:9; cutout no; Find out.
- barn-field: "A grassy autumn farm field seen from high above at an angle, a straight dirt path running left to right across the lower middle, trees along the edges"; 16:9; cutout no; Barn, all levels.
- barn-side: "A red wooden barn seen from the side, big open doorway facing left"; 3:4; cutout yes; the right end of the Push path.
- barn-top: "A red wooden barn seen from high above at an angle, a big doorway in the front wall" and barn-door: "a red wooden barn door with white cross boards"; 4:3 and 3:4; cutout yes; door slides open.
- pond 4:3, pumpkin-patch 4:1, hay-pile 4:3, tin-bucket 1:1 (stacked three by code, each tumbles on its own): all seen from high above at an angle, cutout yes.
- ball: "A red rubber playground ball" 1:1; pumpkin: "A round orange pumpkin with a short green stem" 1:1; wagon-body: "A red toy wagon from the side, long black handle pointing forward" 16:9; wagon-wheel: "A black toy wagon wheel with a silver hub" 1:1; all cutout yes; the wheels turn separately.
- ramp: "A short wooden ramp seen from high above at an angle, sloping down to the right" 4:3; bale: "A rectangular golden hay bale tied with two strings, seen from high above at an angle" 4:3; board: "A long wooden plank standing on its edge, seen from above at an angle" 4:1 (rotated 40 degrees either way in code); cutout yes; field pieces and tray tiles.
- jo (people yes, about six, boots and a fall jacket, full body side view, 3:4, cutout yes, flipped in code for the other side): standing ready, small push (arms out, light lean), big push (deep lean, back foot pushing), pulling a wagon handle (walking backward, arm out), stepping aside, cheering. Jo's look is decided at the contact sheet.
19 images plus Jo's 6 poses. Drawn in code: fence posts, post dots, flags, arrows, trail dots, spots, lanes' badges, thumbs, cards' icons, step and level strips, try strip, rings.

## Voice
Bank voice `upbeat-guide` (Zephyr). Style: "Say brightly and clearly, like an upbeat guide showing a class around a farm." Different from vibration-station (curious-librarian), three-pigs-lab (gentle-storyteller), melt-or-not (clear-teacher), habitat-hunt (Puck) and me-vs-the-counter (easy-coach). `Curio.voice` with `scope: () => state.mode + ':' + state.step`. Braces are expanded by the builder; every expansion is in lines.json. Numbers are spoken as words.

Push (how lines once each, never repeated):
- how `welcome` (stale after the first Go): "Welcome to the farm! Let's push and pull. Tap Go to give the ball a push."
- how `firstPush` (first stop): "The flag shows where it stopped. Now tap Big, then tap Go."
- how `bigFar` (first time a flag lands beyond a smaller push's flag for the same object): "A bigger push sent it farther!"
- how `sideHow` (after the third Go if the side never changed): "Tap To the gate, then tap Go."
- how `otherWay` (first push to the gate): "Jo pushed from the other side, so it went the other way!"
- how `wagonHow` (Wagon first picked): "A wagon has a handle. Tap Pull, then tap Go."
- how `pulled` (first pull): "A pull brings the wagon toward Jo. A push sends it away."
- how `heavy` (first pumpkin flag when a ball flag of the same size exists): "The pumpkin is heavy, so the same push moves it less."
- how `findOut` (after five Go taps): "Tap Find out to test pushes like a scientist."

Find out (all event unless marked):
- whole `q1`: "Which ball will go farther: the one with a small push, or the one with a big push? Say your guess, then tap a picture."
- `predicted` (each prediction): "We think: {card words}." `try1` / `try2` (each Go step): "Tap Go for try one." / "Tap Go for try two."
- whole `compare` (Q1, Q2): "Tap the {ball / pumpkin} that went farther." `cmpRight`: "Yes! That one went farther." `cmpWrong`: "Look again. Count the dots to each flag. Then tap the one that went farther."
- whole `r1` / `r2`: "The big push sent the {ball / pumpkin} farther!" then `match` "Just like we thought!" or `surprise` "A surprise! Now we know."
- whole `q2`: "Does a different push change how far the pumpkin goes? Say your guess, then tap a picture." whole `planAsk`: "Try one is the pumpkin with a {small / big} push. Tap the try two that changes only the push."
- whole `unfair`: "We changed the push and the thing we pushed. We can't tell which one made the difference! Tap the other try two." `fair`: "Only the push changed. That's fair! Tap Go."
- `q3pre`: "Jo pushes the wagon to the barn. Tap Go." whole `q3`: "Now Jo is on the other side. Which way will the wagon go? Tap a picture." whole `r3`: "Jo pushed from the other side, so the wagon went the other way!"
- `q4pre`: "Jo pushes the wagon to the barn again. Tap Go." whole `q4`: "Now Jo holds the handle and pulls. Which way will the wagon go? Tap a picture." whole `r4`: "The pull brought the wagon toward Jo. A push sends things away. A pull brings them close."
- `q5pre`: "Here comes the ball! Jo steps out of the way. Tap Go." whole `q5`: "This time Jo gives the rolling ball a small push back. What will happen? Tap a picture." whole `r5`: "Jo's push stopped the ball! A push can stop something that is moving."
- how `nextHow` (first filled page; stale when Next is tapped): "Tap Next."
- whole `claims` (end page): "We found out! A bigger push sends things farther. A push from the other side sends them the other way. A pull brings them close. And a push can stop a rolling ball." then how `toBarn`: "Tap Barn to help the ball get into the barn."

Barn:
- whole `b1`: "Jo can only give the ball a small push. Can we get it into the barn? First, tap Roll and watch." `goal1` (first not-worked judgment on level 1): "We need the ball to go faster."
- how `judgeHow` (first stop of the mode): "Did it work? Tap Yes or Not yet." (level 3 card text: "Did the buckets fall?")
- verdicts: `yesRight` "Yes! It worked!" `noRight` "Right, not yet." `yesWrong` "Look where the ball is. It didn't work yet." `noWrong` "Look! It did work!"
- cause (after a not-worked verdict): `cShort` "It stopped before the barn." `cUp` "Rolling up the ramp slowed it down." `cBounce` "It bumped the bale and rolled back." `cWall` "It turned, but it hit the barn wall." `cPatch` "It turned the wrong way, into the pumpkins." `cPond` "Splash! It rolled into the pond." `cWobble` "The buckets wobbled, but they didn't fall. The ball was too slow." `cHay` "It rolled right past the barn, into the hay."
- how `fixHow` (first not-worked verdict of the mode): "Change our design. Tap a piece, then tap a glowing spot. Then tap Roll." event `fixAgain` (later not-worked verdicts): "Change something, then tap Roll."
- whole `a1`: "Watch both balls. The faded one has no ramp. Did the ramp make the ball go faster or slower? Tap a picture." `a1Fast` "Faster! The ramp made the ball go faster." `a1Slow` "Look again. The ramp ball got ahead. The ramp made it go faster."
- whole `b2`: "Now the barn is up here, and the pond is down the path. Tap Roll and watch where the ball goes." `goal2`: "We need the ball to turn into the barn."
- whole `a2`: "Watch both balls. What did the board change: which way the ball went, or how fast? Tap a picture." `a2Way` "Yes! The board turned the ball. It changed which way it went." `a2Fast` "Look again. The board turned the ball. It changed which way it went."
- whole `b3`: "Last one! Knock down the buckets in the barn. Jo's push is small again. Tap Roll and watch." `goal3`: "We need the ball to go faster, and to turn."
- whole `barnEnd`: "We did it! The ramp made the ball faster, and the board turned it. Our design works!"
- `nextHow` as above.
Repeats: verdicts and causes every time; `goalN` once per level, then hint only; no line names a hidden control (no Go before a prediction, no Roll while thumbs show, no Pull unless Wagon is picked).

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Find out predictions (not scored) | Guessing; always the first card; changing it after seeing; the answer on screen | Nothing is awarded; the card locks on tap and Go appears only after it, so no try runs first; card order shuffled per test; `surprise` is a normal ending. |
| Compare tap, Q1 and Q2 (first tap recorded) | Guessing (1 in 2); always the lower lane; tapping the lane with the big-push badge; mashing both | Which try is big is random (Q1 order random, measured 50.2% try one over 10,000 runs; Q2 first size random), so lane position says nothing. The badges hide during the compare, so only the flags tell. Only the first tap is recorded; a miss shows dot counts and the class taps again. |
| Q2 fair plan | Guessing (1 in 2); card position; picking the ball because it goes far | The unfair run plays, then `unfair` names why it can't count and the page stays empty; only the pumpkin card fills it. Positions shuffled. |
| Find out pages fill | Doing nothing; mashing Go or Next | Go is hidden until the prediction (and plan) is in; Next is hidden until a page fills; pages fill only from the tries and, in Q1 and Q2, a right compare tap. |
| Barn verdict (Yes / Not yet, recorded per try) | Guessing (1 in 2); always Yes; always Not yet; a cheer or open door before the tap; the common wrong answer (almost counts) | The door stays shut and no cheer or check plays until the tap. Always Yes fails on near misses built into each level: level 1's first roll stops one post short of the door, level 2's walls stop beside the door, level 3's slow ball makes the buckets wobble and stay. Always Not yet is corrected on the run that works (`noWrong`). The try strip shows "we said" beside "it was" for every try. |
| Level complete | Trying every design; always the same piece; the right spot glowing | Every allowed spot glows, never just the right one. Random no-repeat designing takes about 5.5, 11.5 and 22.5 tries on average (1 of 10, 2 of 22, 2 of 44 designs work), and each try needs its own judged verdict, so brute force still makes the class read every outcome. The goal line names the need (faster, turn), never the piece or spot. |
| Analysis cards after levels 1 and 2 (first tap recorded) | Guessing (1 in 2); the common wrong answer (level 2 "how fast") | The ghost race is the data: the ramp ball pulls ahead; the board ball turns while the ghost runs to the pond. A wrong pick plays its "Look again" line naming what the race showed; the first tap stays recorded. |

## Heard in order
Taps always act at once; "waits" means the next line waits for this one to finish.
1. Push load: first tap Go, the roll starts, `firstPush` when it stops. First tap elsewhere without its own line: `welcome`. Later firsts: `bigFar`, `sideHow`, `otherWay`, `wagonHow`, `pulled`, `heavy`, each after its roll stops; `findOut` after the fifth.
2. Find out Q1: `q1` (whole; cards live while it plays); card tap: `predicted` (waits for `q1`), `try1`; Go: roll; `try2`; Go: roll; `compare` (whole); tap: `cmpRight` or `cmpWrong` (then the retap: `cmpRight`); `r1` (whole), `match` or `surprise`, `nextHow` (first time). The next `q2` waits for them.
3. Q2: `q2` (whole), card: `predicted`, `planAsk` (whole); plan card: `fair` or the run then `unfair` (whole) and the cards again; then as Q1 from `try1` (Try 1 runs before the fair Try 2), `r2` (whole), `match` / `surprise`.
4. Q3, Q4, Q5: `qNpre`; Go: roll; `qN` (whole) after it stops; card: `predicted`, `try2`; Go: roll; `rN` (whole), `match` / `surprise`. After Q5: `claims` (whole), then `toBarn`.
5. Barn level 1: `b1` (whole); Roll; stop: `judgeHow` (first time only; later the card text and hint ask); thumb: verdict, then cause if not worked, then `goal1` (first time) and `fixHow` or `fixAgain`. Worked: `yesRight` or `noWrong`, then the ghost race starts after the verdict, `a1` (whole) waits for it to end; card: `a1Fast` or `a1Slow`, `nextHow`.
6. Level 2: `b2` (whole), as level 1 with `goal2`, `a2`, `a2Way` / `a2Fast`.
7. Level 3: `b3` (whole), as level 1 with `goal3`, no analysis; worked: verdict, then `barnEnd` (whole).
Feedback for an answer always plays before the next question, which waits for it. No line contains a bare letter.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| K-PS2-1 and K-PS2-2 wording; examples: pulling with a string, a person pushing, a person stopping a rolling ball, objects colliding; strengths or directions but not both at once; no magnets; design examples: move a set distance, follow a path, knock down objects; a ramp to speed it up, a structure to turn a ball; friction not assessed | NGSS, nextgenscience.org, K-PS2 Motion and Stability (performance expectations, clarification and boundary statements) | NGSS@NSTA Hub, K-PS2-1 and K-PS2-2 pages | yes |
| A bigger push (force) makes a bigger change in motion, so the same object goes faster and farther | NASA Glenn Research Center, "Newton's Second Law of Motion" | The Physics Classroom, "Newton's Second Law" | yes |
| An object starts moving in the direction it is pushed or pulled; a pull moves it toward the puller | NASA Glenn, "Newton's Laws of Motion" (force and acceleration share a direction) | OpenStax, University Physics vol. 1, 5.3 Newton's Second Law | yes |
| A push against a moving object's motion slows or stops it | The Physics Classroom, "Newton's Second Law" (acceleration opposite to motion slows it) | OpenStax, College Physics 4.3 | yes |
| The same push moves a heavier object less | NASA Glenn, "Newton's Second Law" | The Physics Classroom, "Newton's Second Law" | yes |
| A ball rolling down a ramp speeds up; rolling up it slows | The Physics Classroom, "Inclined Planes" | NGSS K-PS2-2 clarification (ramp increases speed) | yes |
| A slanted wall or board changes the direction of a rolling ball; a ball bounces back off something in its path | NGSS K-PS2-2 clarification (a structure that turns a ball) and K-PS2-1 (objects colliding push on each other) | The Physics Classroom, "Momentum and Collisions" | yes |
| A faster ball pushes harder in a collision, so it can knock things down that a slow one only rocks | The Physics Classroom, "Momentum and Impulse Connection" | OpenStax, College Physics 8.2 Impulse | yes |
Backed twice: 8. Cut: 2 (a hay bale gives a big bounce: hay is soft, so the bounce is kept small at 1 post and no line says how much; pulling a pumpkin by its stem: not a safe or real way to move one, so Pull is wagon only). Jo, post counts, distances and the farm layout are story values; no line says "friction".

Checks run (Python, scratchpad ptp_check.py, 2026-11-06):
- Contrast ratios as listed in Look.
- Push distances with +-0.15 noise: the smallest gap between two sizes of one object is 0.7 post (53 px), so Big always lands beyond Medium beyond Small; the farthest roll is 5.15 posts, inside the 6-post half path. Roll times 1.05 to 2.4 s.
- Q2 unfair run: pumpkin small 0.5 versus ball big 5, so the unfair try looks like a huge win, which is why it must be rejected.
- Lane randomization: big try in lane one 50.2% of 10,000 runs.
- Barn rule tables enumerated: level 1, 10 designs, 1 works; level 2, 22 designs, 2 work; level 3, 44 designs, 2 work; outcomes per level as in Content (level 3: 17 bounce, 11 patch, 7 wall, 4 short, 2 wobble, 1 hay, 2 worked). Random no-repeat search: 5.5, 11.5, 22.5 tries on average.
- Always Yes is wrong on the first roll of every level (short, pond, short); level 3's natural first fix (Board up at 5, no ramp) is the wobble near miss.

## Done when
1. Focus: at 1366x768 the path (Push), the two lanes (Find out) or the field (Barn) is the biggest thing; every tile, Go, cards, tray, Roll, thumbs and Next sit above the fold; at 680x425 the scene, its controls and the hint show without scrolling, text 10 px or more.
2. Push: Big lands beyond Medium beyond Small for each object every time; To the gate sends it the other way; Pull shows only for the wagon and the wagon follows Jo; flags stay (8 at most) and Clear flags works.
3. K-PS2-1 strength: Q1 and Q2 lock a prediction before Go appears; the compare hides the badges, records the first tap and shows dots after a miss; which lane is big varies across reloads.
4. K-PS2-1 direction and stopping: Q3 rolls the wagon to the gate, Q4's wagon follows Jo, Q5's first ball rolls past and the second stops at Jo's hands; each page fills only from its tries.
5. K-PS2-1 plan: in Q2 the ball try two runs, plays `unfair` and leaves the page empty; only the pumpkin try two fills it.
6. K-PS2-2 judging: after every Barn roll the door stays shut and no cheer plays until Yes or Not yet; the try strip records "we said" and "it was"; level 1's first roll stops one post short and level 3's no-ramp board run wobbles the buckets.
7. K-PS2-2 analysis: every outcome in Content draws as listed; every allowed spot glows; after levels 1 and 2 the ghost race plays before the analysis cards, and the first card tap is recorded.
8. Tap while it plays: Go during a roll plants the flag and starts the new push; a tile tap mid-roll moves Jo at once; Roll during a roll restarts it; no older line plays after a newer one; every result plays before the next question.
9. Pre-reader: every question, choice and next step is spoken; every choice is a picture with one word; a child alone with Sound on finishes Find out and Barn without reading.
10. Voice: five Go taps speak `firstPush` once; five not-worked Barn verdicts speak the verdict and cause each time; no line names a hidden control.
11. Motion off: rolls, the ghost race, the door and the buckets show their end states on the same beats; no network requests.

## Open questions
- None for Cory. Jo (six poses) goes to the contact sheet and the fresh representation check (BASELINE 11). No cultural, Native or hard-history content, so no sensitivity review is needed.
