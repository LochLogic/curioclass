# Levels and Pathways

## One idea
The dancer's feet paint the floor: every trip leaves a ribbon whose shape is the pathway (straight, curved, zigzag) and whose color and pattern is the level (high, middle, low), so the class can read a dance after it happened, guess a hidden one by drawing it in the air, and draw a new one for the dancer to follow.

## Not like
- animal-moves (K-2 PE, built, movement family): animals, one locomotor skill each, a freeze game; its Mix it up names high and low as a challenge card. Here no animals and no freeze: the subject is where the body goes in space, and the floor keeps a record of it (the ribbon).
- beat-buddies (K-2 music, built): steady beat with animals and freezes. Here the music is only a background; space is the subject.
- robot-dance (K computer science, built): moves done in place, in order, to find a bug. Here every trip travels, there is no sequence to fix, and the answer is a shape on the floor.
- line-safari (K-2 art, built): names straight, curvy and zigzag lines drawn on a savanna. Same words on purpose (teachers can link them), but here the line is made by a body traveling and the class makes it with their own bodies.
- robot-mouse-mail (grade 1 CS): arrow commands on a grid. Here paths are drawn freehand on an open floor, no grid, no commands.
- target-toss (K-2 PE): a throwing experiment. story-dress-up (K-2 theater): acting out a story. No shared mechanic.
- Dance siblings: dance-pattern-puzzle (patterns hidden in a sequence of move cards), choreography-board (phrases on a timeline, revised with devices), dance-styles-explorer (styles, traces and critique). None draws or reads pathways on the floor.

## Who and how
- Grade K-2, arts (dance), module "Moving Bodies (Dance)".
- Topic line: locomotor and nonlocomotor movement
- Driver: teacher on a projector or smartboard. The class stands in their own "bubble space" and copies; pathways are followed in the room (gym, cleared space) or in place by marching the shape.
- Minutes: 10-20. tool.json modes: ["Levels", "Pathways", "Mystery path", "Draw a path"]; driver "teacher"; grades_label "Grades K-2".
- Standards (NCAS dance): DA:Cr1.1.Ka (respond in movement to a cue: the narrator and the music), DA:Cr1.1.Kb (explore different ways to do basic locomotor and nonlocomotor movements by changing at least one element of dance: level, pathway, way of moving), DA:Pr4.1.Ka (change levels), DA:Pr4.1.1a (straight, curved and zigzag pathways), DA:Pr4.1.2a, DA:Cr1.1.2b (explore locomotor and nonlocomotor movement by changing the elements of dance: Draw a path, one drawn dance changing level part by part); also DA:Re7.1.Kb (Mystery path: describe observed dance movement, its pathway and level), DA:Cr3.1.Kb and DA:Cr3.1.2b (ribbon floor maps as symbols for pathways and levels), DA:Pr5.1.Kb (start and stop on cue), SHAPE.S2 (movement concepts: levels and pathways).
- K-2 reads nothing: every control has an icon, every fixed line is voiced, targets are 60 px or more (72 px for answer buttons).

## Screens and modes
Header: title "Levels and Pathways", small line "Locomotor and nonlocomotor movement", mode buttons (`.seg`, keys 1 to 4) **⬆ Levels**, **〰 Pathways**, **❓ Mystery path**, **✏ Draw a path**, then kit `motion`, `sound`, `read`. Stage left, panel right; under 1000 px wide the panel goes below with its buttons first (STANDARDS.md "Sizes").

Stage (all modes, drawn in code at real pixel size per layout): a dance studio in three-quarter view. A wide light wood floor plane, a back wall with a long mirror strip and a barre, two soft window patches of light on the floor. On the left wall the **level guide**: three stacked bands with an icon and a word each, High (cloud), Middle (table), Low (grass tuft). The band the dancer's body is in glows. A count strip along the bottom of the stage: 8 dots, the current count lit (no words).

### Levels (opens first)
- Stage: the dancer stands center on a round bubble-space mat.
- Panel: **Level** row of three 72 px buttons (cloud **High**, table **Middle**, grass **Low**; Middle on at start). **Move** grid of six 72 px buttons with a mini dancer pose each: **Stretch**, **Twist**, **Bend**, **Swing**, **Shake**, **Curl**. Then **🎢 Up and down** (a 40-count routine, see Content) and **🎲 Surprise** (random move and level).
- Tap a move: the narrator calls it ("Stretch! Low level, close to the floor."), a 4-count count-in shows on the dots, then the dancer does the move for 8 counts at the chosen level and holds still on count 8 ("And freeze!"). Tap a level while a move runs: the dancer changes level on the next count and the narrator says the level.

### Pathways
- Stage: a gold star spot at the front left of the floor (start) and the dancer on it.
- Panel: **Pathway** row (72 px, icon is the line itself): **Straight**, **Curved**, **Zigzag**. **Way to move** row: **Walk**, **Skip**, **Gallop**, **Slide** (mini dancer pose each). **Level** row as in Levels. **▶ Go** (big gold), **🧽 Clean floor**.
- Go: the narrator says the pathway and the way ("A zigzag pathway. Let's skip."), count-in, then the dancer travels the pathway over 16 counts; the ribbon appears under the feet as the dancer goes. At the end the dancer turns to the class and the ribbon gets its pathway icon at its end. Up to three ribbons stay on the floor (older ones fade to 50 percent); a fourth trip clears the oldest. The dancer walks back to the star at the start of the next Go.

### Mystery path (showdown)
- Stage: the floor shows a faint sparkle ("magic floor"); round dots (8) at the top right, filled for solved rounds.
- Panel: **▶ Go** (starts the round's trip), then the answer step: three 72 px buttons **Straight**, **Curved**, **Zigzag**; after a right answer, three level buttons **High**, **Middle**, **Low**. **👁 Watch again**, **⏭ Next** (enabled once both answers are right), **↺ Play again** (after round 8).
- The dancer travels with no ribbon. The class draws the path in the air with one finger and calls it out; the teacher taps what most of the class says. Right: chime, the ribbon paints in along the whole trip (1.5 s), the right button glows. Wrong: soft tone, "Let's watch it again", the trip replays once on its own; the teacher can tap again. Then the level question the same way.
- After round 8: the **Ribbon gallery**: all 8 ribbons on the floor together, the dancer bows.

### Draw a path
- Stage: empty floor with the star. A pencil cursor over the floor.
- Panel: **Level** row, **Way to move** row, **▶ Dance it**, **🎲 Surprise path**, **🧽 Clear**.
- Drag from the star across the floor (pointer, touch or pen): a dashed line follows the finger. On release the line is split into parts (Interactions), each part redrawn smooth with its pathway icon floating over it, and the narrator names the parts in order ("First, straight. Then zigzag."). Each part's badge is a button: tapping it gives that part the next level, so one drawn dance can change level part by part (Refine changes). **Dance it**: the dancer dances the path part by part, each at its own level, in the chosen way, painting the ribbon. **Surprise path** builds a random path of 2 or 3 parts (this is also the keyboard path).

## Content
Nonlocomotor moves (8 counts each, a 2-count A to B loop four times; the level changes the shape):
| Move | High | Middle | Low |
|---|---|---|---|
| Stretch | on tiptoes, both arms reach straight up | standing, arms stretch wide to the sides | sitting, legs long, reaching toward toes |
| Twist | on tiptoes, arms up, twist side to side | standing, arms out, twist side to side | kneeling, hands on hips, twist side to side |
| Bend | on tiptoes, arms up, bend side to side like a tree | standing, bend forward and come back up | sitting, bend forward over the legs and back up |
| Swing | arms swing side to side over the head | arms swing forward and back like a swing | crouching, arms swing low near the floor |
| Shake | on tiptoes, shake both hands high | standing, shake the whole body | crouching, shake hands near the floor |
| Curl | on tiptoes, hug yourself tight, then open | standing, curl into a round shape, then open | small ball on the floor, then open |
Up and down: one move (the last one chosen, Stretch at start) for 8 counts each at High, Middle, Low, Middle, High (40 counts), narrator calls each level as it changes.

Ways to move (16 counts per trip; the engine's gait cycle for each):
| Way | Tempo | Middle | High | Low |
|---|---|---|---|---|
| Walk | 100 beats a minute | normal steps, arms relaxed | on tiptoes, arms up | knees bent, body low, hands near knees |
| Skip | 120 (swung) | step-hop, alternate feet, arms swing | higher hops, arms reach up | small low skips, knees bent |
| Gallop | 120 (swung) | same foot leads, other foot catches up | on toes, arms up | knees bent, low |
| Slide | 100 | sideways, step-together, facing the class | on toes, arms out high | knees bent, arms low |
Slide always faces the class and travels sideways along the path; the others face the way they travel.

Pathways (floor units 0 to 100 across, 0 to 60 deep; star at x 10, z 50 front):
- Straight: from the star to x 90 along the front, 16 counts.
- Curved: a half-circle arc bulging to the back of the floor, star to x 90.
- Zigzag: 4 legs alternating front and back (corners at x 30, 50, 70), star to x 90.

Ribbon: High is sky blue #1565c0 dotted tiptoe footprints joined by a thin line; Middle is green #2e7d32 a solid band; Low is amber #b45309 a wide band with diagonal stripes. Pattern and the level icon at the ribbon's end carry the meaning, never color alone.

Mystery rounds (pathway, way, level): 1 Straight, Walk, Middle. 2 Zigzag, Walk, High. 3 Curved, Slide, Middle. 4 Straight, Gallop, Low. 5 Curved, Skip, High. 6 Zigzag, Slide, Low. 7 Curved (a full circle that ends back on the star), Walk, Low. 8 Zigzag, Gallop, Middle.

Music: one original, cheerful studio tune (piano, soft bass, light shaker) synthesized in the page, played at the way's tempo; Levels uses 96 beats a minute; a 4-click count-in before every move or trip.

## Interactions in detail
- One dancer action at a time: a new move, Go or Dance it stops the current one at once (run token; nothing from the old run speaks or ticks again).
- Levels: tapping the same move again restarts it. Surprise never picks the same move and level twice in a row.
- Pathways: Clean floor fades all ribbons in 0.5 s. Changing pathway, way or level while the dancer travels takes effect on the next Go.
- Mystery: answer buttons are disabled while the dancer travels (aria-disabled, visibly dimmed) and enabled when the trip ends. Watch again replays without ribbon. The class gets a filled dot when both answers are right; there is no wrong-answer count and no score beyond the 8 dots. Leaving the mode keeps the round; Play again resets to round 1.
- Draw a path, splitting the line (the tool's own rule): smooth the samples, simplify the polyline (tolerance 2 percent of floor width), then: a corner turning 60 degrees or more is a sharp corner; two or more sharp corners in a row, each leg shorter than 30 floor units, make one **zigzag** part; a stretch between sharp corners whose total gentle turning is 30 degrees or more is **curved**; anything else is **straight**. At most 4 parts (the last parts merge into the 4th). A line shorter than 15 units gets "Draw a longer pathway". The line is clamped to the floor. Counts: 16 per 100 units of length, at least 8, at most 32.
- A drag that does not start on (or within 8 units of) the star still works: the path starts with a straight part from the star to where the finger went down.
- Motion off: the dancer shows each count's pose without in-between motion and slides in steps along the path; the ribbon, music, counts and lines keep the same timing.
- Sound off: no music or voice; count dots and the count-in dots carry the timing.
- Nothing is saved.

## Look
- Accent `--brand` #00798c (studio teal). Paper #f3f9f8, ink #13282b, muted #4e6266, line #cfe3e1, focus #6b4fbb, panel #ffffff; floor wood #e9d3b0 to #d9b98a, back wall #eef6f5, mirror #dbe9ee.
- Contrast: white on accent 5.10:1; accent on paper 4.79:1; ink on paper 14.43:1; muted on paper 6.04:1; ink on floor wood #e9d3b0 10.55:1; white on the level colors High 5.75:1, Middle 5.13:1, Low 5.02:1 (level button labels sit on those colors).
- The dancer: drawn in code from simple shapes (rounded capsule limbs, oval head with no face, a teal top and charcoal leggings), 2 px darker outline, about 40 percent of the stage height at Middle.
- Different from animal-moves (blue #1f6fb2), beat-buddies (red-orange #c2482f), line-safari (orange #c0612b), robot-dance (magenta #b0206a), target-toss (purple #6b3fa0) and the dance siblings (cobalt, mint, lilac).

## Art
none: drawn in code (studio, dancer, ribbons, icons). The dancer is simple shapes, so people: false.

## Voice
`warm-teacher` (Sulafat): "Say warmly and clearly, like a kind kindergarten teacher talking to the whole class." Different from animal-moves (hero-coach), beat-buddies and robot-dance (lively-host), line-safari and target-toss (bright-teacher), orchestra-zoo (playful-friend). Every fixed line is voiced.
| Key | Kind | Line | Stale when |
|---|---|---|---|
| wLevels | how | Let's dance at three levels: high, middle and low. Tap a move, and copy the dancer! | mode left |
| wPaths | how | A pathway is the line you make when you travel. Tap a pathway, then tap Go, and follow the dancer! | mode left or trip started |
| wMystery | how | The magic floor hides the pathway. Tap Go, watch the dancer, then draw the pathway in the air with one finger. | mode left or trip started |
| wDraw | how | Draw a pathway on the floor with your finger. Start at the star. Then tap Dance it. | mode left |
| copyMe | how | Copy me! Stay in your own bubble space. | move ended |
| stretch, twist, bend, swing, shake, curl | event | Stretch! / Twist! / Bend! / Swing! / Shake! / Curl! | another move started |
| atHigh | event | High level. Reach up to the sky! | another move or level |
| atMiddle | event | Middle level. Stay in the middle. | another move or level |
| atLow | event | Low level. Get close to the floor. | another move or level |
| freeze | event | And freeze! | move ended over 1 s ago |
| upDown | event | High, middle, low, middle, high. Follow me up and down! | routine stopped |
| straight, curved, zigzag | event | A straight pathway. / A curved pathway. / A zigzag pathway. | trip started |
| walk, skip, gallop, slide | event | Let's walk. / Let's skip. / Let's gallop. / Let's slide sideways. | trip started |
| ribbon | event | Look at the floor! The ribbon shows our pathway. | next trip started |
| askPath | how | Which pathway was it? Draw it in the air, then tap straight, curved or zigzag. | round changed |
| askLevel | how | Which level was the dancer? Tap high, middle or low. | round changed |
| rightPath | event | Yes! Here's the ribbon. | round changed |
| rightLevel | event | Yes! That's the level. | round changed |
| nextHow | how | Tap Next for a new mystery. | round changed |
| wrong | event | Hmm, let's watch it again. | replay ended |
| allDone | event | Eight mysteries solved! Look at all our ribbons. | mode left |
| firstStraight, firstCurved, firstZigzag | event | First, straight. / First, curved. / First, zigzag. | path redrawn |
| thenStraight, thenCurved, thenZigzag | event | Then straight. / Then curved. / Then zigzag. | path redrawn |
| tooShort | event | Draw a longer pathway, from the star across the floor. | path redrawn |
| tapPart | how | Tap a number to change that part's level. | path redrawn |
| danceIt | how | Now tap Dance it, and follow the dancer! | path cleared |
| surprise | event | Here's a surprise pathway! | path redrawn |
| doneDraw | event | Great dancing! Draw a new one, or dance it again. | path redrawn |
- Calls play as sequences (`V.say(['stretch', 'atLow'])`, `V.say(['zigzag', 'skip'])`, the part names in order), each with `wait: true` before the count-in starts, so the dancer never moves under a call.

## Family engine
**dance** (`kit/dance.js`). No dance tool is built yet; this spec, the lowest grade sibling, holds the full description. Siblings: dance-pattern-puzzle, choreography-board, dance-styles-explorer.
- **One figure for the site.** Dancers use the jointed pose format of the movement engine (`Move.figure`, fitness-circuit spec): a pose is a set of joint angles (head tilt, trunk lean, trunk twist, shoulders, elbows, hips, knees, ankles for tiptoe or flexed) plus body angle for floor shapes. Whichever family is built first puts the figure in `kit/movement.js`; `kit/dance.js` loads after it and adds the rest below.
- `Dance.dancer(svg, {top, bottom, badge, scale})`: a dancer from simple shapes (no face), colors per tool, an optional shape badge on the chest (circle, square, triangle, diamond) so dancers never differ by color alone. Root position on the floor (x, z), facing (front, three-quarter, side, back, or any angle), mirror (left for right).
- `Dance.poses`: the shared named pose library, each tool adding its own: stand, reach-up, arms-wide, bend-fwd, bend-side, twist, curl, crouch, kneel, sit, lie, lunge, plie, releve, passe, arabesque, star-jump, tuck-jump, clap, point, kick, stamp, step, hop, contraction, release, bow.
- `Dance.level(pose, 'high' | 'middle' | 'low')`: the level modifier. High rises to the toes and lifts the arms; low bends the knees deep and leans the trunk forward. A pose may name its own high and low versions (Stretch low is sitting), which win.
- `Dance.gaits`: walk, skip, gallop, slide, run, hop, march, leap as stepping cycles that travel along a path at a given number of counts.
- `Dance.dyn`: six energy qualities as timing curves between keyframes: **smooth** (even), **sharp** (arrives in the first fifth of the count and holds), **swing** (eases down through the bottom and up), **suspend** (slows and hangs at the top), **collapse** (holds, then drops fast), **shake** (small fast jitter around the pose).
- `Dance.phrase(steps)`: a list of steps `{poses, counts, level, dyn, side, facing, travel}`; `side: 'L'` mirrors; `travel` is a floor path covered during the step.
- `Dance.clock(bpm, {meter: 3 | 4 | 6, countIn: 4})`: one count clock with `onCount`, pause, resume, seek, stop and a run token; a tempo change takes effect on the next count.
- `Dance.play(dancers, phrases, {clock, offsets, loop})`: drives one or more dancers; `offsets` delays each dancer by counts (canon).
- `Dance.floor(svg, view)`: `'studio'` (three-quarter floor, this tool), `'square'` (an outdoor dance platform in front of a backdrop image), `'stage'` (proscenium audience view with depth rows), `'void'` (dark space). Floor units map to the screen per view; depth sets scale.
- `Dance.trail(dancer, {mode})`: `'ribbon'` (a floor ribbon under the feet, styled by level, this tool), `'exposure'` (ghost copies every half count plus traced hand and foot paths), `'off'`; `trail.points` keeps the record.
- `Dance.music(track, clock)`: synthesized loops locked to the clock (kick, snare, hat, clap, shaker, wood block, bass, piano, pluck, pad, foot taps and stamps, count-in clicks), silent with Sound off. Each tool lists its own tracks.
- `Dance.counts(el, clock)`: the count strip (dots or numbers, current count lit, phrase number).
- Motion off: keyframes without tweening, trails still build; clock, music and lines unchanged.
Levels and Pathways feeds it: the `'studio'` view, ribbon trails, 6 nonlocomotor moves at 3 levels, 4 gaits at 3 levels, 3 pathways plus drawn paths, the Mystery rounds, one music track.

## Sources
- National Core Arts Standards, Dance (2014), grade K to 2 performance standards for DA:Cr1.1 and DA:Pr4.1 (levels; straight, curved and zigzag pathways; locomotor and nonlocomotor movement): https://www.nationalartsstandards.org/
- Levels (high, middle, low), pathways (straight, curved, zigzag), personal space, locomotor and nonlocomotor movement as dance concepts: Anne Green Gilbert, Creative Dance for All Ages, 2nd ed. (Human Kinetics, 2015), the dance concepts chapters; and Perpich Center for Arts Education, "The Elements of Dance" (Body, Action, Space, Time, Energy).
- Walk, skip, gallop and slide as K-2 locomotor skills, with cues (same foot leads in a gallop; slide sideways step-together): SHAPE America, National Standards and Grade-Level Outcomes for K-12 Physical Education (2014), S1.E1: https://www.shapeamerica.org/standards/pe/
- The six energy qualities in the engine (smooth or sustained, sharp or percussive, swing, suspend, collapse, shake or vibratory): Perpich Center, "The Elements of Dance", Energy section.

## Done when
1. Levels: every move at every level (18) has its own shape, the level guide band that glows matches the dancer, and the call is spoken before the dancer moves.
2. Changing level mid-move switches on the next count; Up and down runs 40 counts in the order High, Middle, Low, Middle, High.
3. Pathways: each pathway with each way leaves the right ribbon shape, with the level's color and pattern and the icon at its end; a fourth trip clears the oldest ribbon.
4. Mystery: answers are disabled while the dancer travels; a right path answer paints the ribbon, a wrong one replays the trip once; the 8 rounds match Content and end in the Ribbon gallery.
5. Draw a path: a plain line is one straight part, a smooth arc is curved, a three-corner scribble is zigzag, a tiny line gets tooShort; Surprise path works from the keyboard alone.
6. A new action stops the old run at once: no old call, count or music follows.
7. How-to lines are spoken once per load; move, level, pathway and answer lines speak every time.
8. At 1366x768 and 1920x1080 the floor, the dancer and the main row of buttons are visible together; at 1000x625 the preview reads (button icons clear, no text under 10 px); at 375 wide the buttons stay 60 px.
9. Motion off and Sound off keep the same timing; nothing is stored.

## Refine changes (round 1)
- Reading a drawn line moved into the kit (`Dance.readPath`, rules in docs/families/dance.md): two or more sharp corners that turn left and right in turn make a zigzag at any leg length up to about 60 floor units; a smooth arch or an S is one curved part; a straight, zigzag, arch line names three parts. Test table with real drags in handoff.md.
- Draw a path, levels part by part: after drawing, each part's badge shows its number, pathway icon and level icon, and the class taps the badge (a 64 px button on the floor) to give that part the next level (high, middle, low). The panel Level row sets every part at once (it shows pressed only when all parts match). Dance it performs each part at its own level, the ribbon changing pattern and color part by part and the level guide following. Surprise path gives its parts mixed levels and never crosses itself. New how line `tapPart`, said once after the first part names.
- Every Low keyframe is on the floor (sitting, kneeling back on the heels or lying), clearly under every Middle one from the front; Stretch at Low is a straddle sit and reach, Bend at Low a side bend kneeling on the heels.
- Move buttons have one fixed icon per move with a motion mark; Mystery round dots sit beside the mirror (or on the back edge of the floor); the gallery puts each ribbon in its own cell with its badge on top and the dancer bows at the side.
- Voice: `rightLevel` is the event "Yes! That's the level." and `nextHow` the how-to "Tap Next for a new mystery." (said once); Mystery's welcome is the line for the round's step; round 8 goes to the gallery at once with its line after the Yes; the hint names the next action after a freeze or a trip.
- Mystery path cites DA:Re7.1.Kb (describe observed movement), not Ka. The grade 1 and 2 Re7.1 codes leave this module (see handoff.md).

## Refine changes (round 2)
- A drawn line is read as it looks on screen (`Dance.readPath` with the floor), so a straight, curved or zigzag shape reads the same drawn side to side, front to back or on a slant; a corner needs a real tip, so the top of a wave or an S is never a corner. Real-drag table in handoff.md.
- Low Curl is a seated tuck that opens into a seated star: no in-between of any Low move lifts the head over 0.62 of standing, and changing from one Low move to another passes through the seated tuck.
- A level answered while the right pathway is still painting counts exactly as a slow answer (full badge, round 8 gallery badge, Next line).
- Part badges in Draw a path take the first clear spot on the stage, off the dancer and the level guide.
- The gallery bow is a hip fold turned toward the ribbons, so it reads as a bow from the front.
- Standards: DA:Cr1.1.2b is cited (one drawn dance that changes level part by part). DA:Cr3.1.1b (several types of movement shown by picture or symbol) moves off this module: the way of moving stays one choice per path, because a way icon on every part badge would crowd the badges on a K-2 projector and at 375. Recorded in handoff.md for the integrator.

## Open questions
- The pose figure is shared with the PE movement family (fitness-circuit). This spec puts it in `kit/movement.js` and has `kit/dance.js` build on it, so the site has one dancer model. OK, or should dance keep its own figure?
