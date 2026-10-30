# Feeling Scarf Dance

## One idea
The scarf makes a feeling visible: the class builds a three-part dance for a feeling (a starting shape, a moving middle, an ending shape), a dancer performs it holding a long scarf whose flow (drifting, swirling, snapping, drooping) shows the feeling in the air, and then the screen keeps only the scarf as the class dances the same three parts with their own soft cloth.

## Not like
- levels-and-pathways (k-2, showdown, dance family): the class copies levels and pathways and the floor records them. Here the class invents the dance, the record is a scarf in the air, and the subject is a feeling with a beginning, middle and end.
- choreography-board (6-8, studio): revises 8-count phrases with devices on a timeline. Here there are three big parts and one choice each.
- puppet-show-feelings (k-2, story, this batch): the class reads a feeling from a puppet. Here the class makes a feeling with its own bodies.
- family-dance-night (k-2, explorer, this batch): watches dances from families and places. Here the dance is the class's own, about a feeling.
- beat-buddies (k-2, showdown): copies animal moves to a beat. Here the moves are chosen and the scarf, not the beat, is the point.

## Who and how
- Grade K-2, dance, module "Dancing a Feeling".
- Driver: teacher on a projector or smartboard; the class chooses together, then dances in the room (a scarf, a tissue, a dish towel or an empty hand all work). Half the class can perform for the other half. 15 to 25 minutes.
- Standards: NCAS DA:Cr2 (organize a dance with a beginning, middle and end), DA:Pr6 (perform for an audience), DA:Cn10 (connect a dance to a feeling from your own life).

## Screens and modes
Header: title, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`, icon plus word): `Build` (blocks icon, default), `Watch` (eye), `Your turn` (scarf), `Share` (hands clapping). Every control is 60 px or more with an icon and a word.

**Build.** Focus: the dance strip, three big part cards across the stage, `Start`, `Middle`, `End`, each showing its choice as a still figure icon (Dance.icon) or a move icon, with the feeling banner over them. Rows of choices sit under the strip; the part being chosen is outlined.
- `Feeling`: five buttons, each a face icon and word: `Happy`, `Sad`, `Calm`, `Mad`, `Surprised`. Choosing one tints the backdrop and the scarf (Look) and loads its music.
- `Start shape` and `End shape`: five shape buttons (figure icons): `Tiny ball`, `Tall tower`, `Wide star`, `Twisty`, `Lean`.
- `Middle move`: six move buttons (icon of the scarf trace): `Float`, `Swirl`, `Zap`, `Melt`, `Shiver`, `Leap`.
- `Feeling idea` (light bulb) fills the three parts with the feeling's suggestion (Content); the class can change any part.
- `Watch it` (gold) when all three parts are chosen.

**Watch.** Focus: the dancer (code figure) and the scarf in the middle of the stage, on a grassy hilltop under a big sky (painted backdrop, tinted by the feeling), the dancer about 55% of the stage height. Under the stage: the three part cards small, with the playing part lit; count dots (16, grouped 4 + 8 + 4). Bar: `Play` / `Stop` (gold), `Again`, `Slow` (toggle, plays at 70% speed). The part cards stay live: tapping a different shape or move on a small card's menu changes the dance while it plays.

**Your turn.** Focus: the scarf alone, big, drawn as it moves in Watch but with the dancer hidden (a faint ghost at 12% shows where the hand is), the part word huge over it (`Start`, `Middle`, `End`), and the count dots. Bar: `Go` (gold: count-in 4, then 16 counts of music), `Stop`, `Mirror` (toggle: flips left and right so the class follows like a mirror). After the last count the screen says "Freeze!" and holds 3 s of quiet.

**Share.** Focus: the audience card, four big "I saw..." chips: `I saw a clear start`, `I saw the middle move`, `I saw a clear end`, `I felt it: <feeling>` (with the feeling's face). The teacher taps the ones the audience names; each lights with a check. `Swap` (two arrows) clears them for the other half of the class. `Go again` jumps to Your turn.

## Content
**Feelings** (face icon; scarf color and pattern; music, original, made with Dance.music; idea as Start, Middle, End):
- Happy: sun yellow #f2b632 with dots; 112 bpm, 4/4, bright pluck melody C major, claps on 2 and 4; Wide star, Leap, Tall tower.
- Sad: rain blue #4f7fbf with long stripes; 66 bpm, 4/4, piano and pad in D minor, no drums; Lean, Melt, Tiny ball.
- Calm: sea green #4aa38a with waves; 72 bpm, 3/4, pad and soft chimes on beat 1; Tall tower, Float, Wide star.
- Mad: fire red #c43c2c with zigzags; 100 bpm, 4/4, low drum stamps on 1 and 3, bass in A minor; Twisty, Zap, Tiny ball.
- Surprised: purple #8a5cc6 with stars; 96 bpm, 4/4, plucked notes with a sudden stop on count 4 of each 4; Tiny ball, Zap, Wide star.

**Shapes** (Dance.poses; held 4 counts):
- Tiny ball: `Dance.level('curl', 'low')`.
- Tall tower: `Dance.level('reach-up', 'high')`.
- Wide star: `arms-wide`.
- Twisty: `twist`.
- Lean: `bend-side`.

**Middle moves** (8 counts; the scarf hand is the right hand, `rHa`):
- Float: arms rise and fall slowly in big arcs, `dyn: 'smooth'`, two keyframes per 2 counts, stepping slowly to the side and back.
- Swirl: the dancer turns in place (facing 0 to 360 over 4 counts, twice) with the scarf arm out, `dyn: 'swing'`.
- Zap: sharp arm punches up, out, down and across, one per count, `dyn: 'sharp'`.
- Melt: from standing, slowly sinks to sitting over 8 counts, arms sliding down, `dyn: 'collapse'` in two halves.
- Shiver: small fast shakes of the arms and shoulders in place, `dyn: 'shake'`.
- Leap: the `leap` gait across the hill and back.

**Scarf.** A chain of 24 points (verlet, 6 constraint passes a frame) hanging from the right hand, 1.1 body heights long, with gravity, light air drag and a slight breeze; drawn as a ribbon 0.06 body heights wide, tapering at the end, filled with the painted silk texture tinted the feeling color and its pattern drawn over it.

**Share chips** as in Screens.

## Interactions in detail
- Build: choices can be made in any order; `Watch it`, Watch's `Play` and Your turn's `Go` are disabled until all three parts and a feeling are chosen (the hint names what is missing).
- Watch: Start holds its shape for 4 counts (the dancer breathes, the scarf settles), Middle plays 8 counts, End holds 4 counts. A change while it plays rebuilds the dance from the current count: the dancer tweens to the new shape or move within 200 ms and the count keeps going; the part card updates at once. Changing the feeling while playing changes the music from the next count (at most 0.9 s at 66 bpm) and the tint and scarf at once.
- `Slow` sets the clock to 70% speed from the next count. `Stop` stops music and dancer at once; `Again` restarts from count 1.
- Your turn: count-in clicks 4, then the same 16 counts; the scarf moves exactly as in Watch (the same run, dancer hidden). `Mirror` flips at once. At the end: "Freeze!" and 3 s still; no score, ever.
- One run at a time (dance.md rule): Go, Play, Again and mode switches stop the old clock, music and voice first.
- Nothing is saved; the built dance stays while the page is open.
- Motion off: the dancer and scarf jump to one pose per count (the scarf hangs straight down from the hand in each pose); counts, music and part words keep their timing.
- Keyboard: Space plays or stops, 1 to 5 pick a feeling, S, M and E jump to the Start, Middle and End choice rows.

## Look
- Accent (`--brand`) #a0197e scarf fuchsia (header, Play, outlined part). Paper #fcf6fa, ink #2a1626, muted #6a5464. The figure in soft grey-violet (`top: '#5b4a6e'`, `bottom: '#2f2a3a'`, skin and hair from the dance.md defaults) so the scarf is the brightest thing on stage. Backdrop tint by feeling: a 25% color wash of the scarf color over the painted sky.
- Scarf colors always come with their pattern (dots, stripes, waves, zigzags, stars) and the feeling face and word on the strip.
- Contrast (WCAG 2.1, computed): white on brand 7.15:1; brand on paper 6.71:1; ink on paper 15.87:1; muted on paper 6.43:1.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8, act-it-out #7d2e7f, levels-and-pathways #00798c.

## Art
Local FLUX (`scripts/localart.py`). No people: the dancer is the dance engine's code figure (no face).
- hilltop: "A wide grassy hilltop under a huge open sky with soft clouds, a few wildflowers, gentle morning light, soft painted picture book landscape, the hilltop flat and open in the lower third"; 16:9; cutout no; people no; the `square` floor's backdrop in Watch (tinted in code by feeling).
- silk: "Close-up of smooth pale silk fabric with soft flowing folds and sheen, full frame, even light"; 1:1; cutout no; people no; a full-frame texture clipped to the scarf ribbon and tinted in code.
2 images, none with people. Drawn in code (the engine): the dancer, the floor, the count dots; and the scarf ribbon, which has to bend and flow every frame, so it cannot be a painted cutout.

## Voice
Bank voice `soft-breath` (Enceladus), style "Say softly and calmly, like a mindfulness teacher". A calm guide for a feelings dance. Not used by any K-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, sound-elevator hero-coach, act-it-out gentle-storyteller, levels-and-pathways warm-teacher) or by another K-2 spec in this batch. `Curio.voice` with `scope: () => state.mode`. Music rule ("speak now and wait"): lines play before Play or Go starts the music, never over the counts; a line queued during a run waits (`valid: () => !state.running`) or is dropped when stale.

- how, welcome (Build; stale when a feeling is tapped): "Let's make a dance about a feeling. First, tap a feeling."
- event, feeling tapped: "Happy." / "Sad." / "Calm." / "Mad." / "Surprised." then once per page load (how): "How does your body show that feeling? Tap a start shape."
- how, start chosen first time (stale when a middle move is tapped): "Now pick a middle move. How does the feeling move?"
- how, middle chosen first time (stale when an end shape is tapped): "Last, pick an end shape. How does the feeling finish?"
- event, all three chosen: "Your dance has a start, a middle and an end. Tap Watch it."
- event, Feeling idea: "Here is one idea. You can change any part."
- how, welcome (Watch; stale when Play is tapped): "Watch the scarf. Tap Play."
- event, a Watch run ends: "Did the scarf show the feeling? How?"
- how, welcome (Your turn; stale when Go is tapped): "Get your scarf, or use your hand. Find your start shape. Tap Go."
- event, the run's end: "Freeze! Hold your end shape. And breathe."
- how, welcome (Share; stale when a chip is tapped): "Audience, what did you see? Tell the dancers."
- event, each chip tapped: "A clear start!" / "The middle move!" / "A clear end!" / "You felt it!"
- event, Swap: "Swap! Dancers, sit down. Audience, find your start shape."
- Read speaks the hint, which always names the next step and button.

## Family engine
Dance (`kit/dance.js`, docs/families/dance.md), though the catalog lists this tool with no family: the figure, floor and timing must come from the engine rather than a second figure. Uses: `Dance.floor(svg, 'square', {backdrop})`, one `Dance.dancer` (colors in Look), `Dance.poses` and `Dance.level` for the five shapes, `Dance.dyn` (smooth, swing, sharp, collapse, shake), the `leap` gait, `Dance.phrase` (three steps: 4, 8, 4 counts), `Dance.clock` with `countIn: 4`, `Dance.play`, `Dance.music` (the five tracks in Content), `Dance.counts` (16 dots) and `Dance.icon` for the shape buttons. The scarf is this tool's own code (it reads `d.world('rHa')` every frame). The builder adds this tool to the "What each tool brings" table in dance.md.

## Sources
- National Core Arts Standards, Dance, grades K to 2 (DA:Cr2, DA:Pr6, DA:Cn10): https://www.nationalartsstandards.org
- Beginning, middle and end as the first dance form for young children, and scarves as a prop that makes movement quality visible: Gilbert, A. G. (2015), Creative Dance for All Ages, 2nd ed., Human Kinetics.
- Movement qualities (smooth, sharp, swinging, collapsing, shaking, suspended) as the elementary "energy" words: Laban-based dance education, as in NDEO, "Standards for Dance in Early Childhood" (https://www.ndeo.org).
- All music is original, made in code.
- Checks run (Python, 2026-10-29): 16 counts plus a 4-count count-in at each tempo: Happy 112 bpm 8.6 s (10.7 s with count-in), Sad 66 bpm 14.5 s (18.2 s), Calm 72 bpm 13.3 s (16.7 s), Mad 100 bpm 9.6 s (12.0 s), Surprised 96 bpm 10.0 s (12.5 s); every run is under 20 s. Scarf: 24 links over 1.1 body heights is 0.046 body heights a link. All five shapes and the leap gait are names in `Dance.poses` and `Dance.gaits` (checked in kit/dance.js). Contrast ratios as listed.

## Done when
1. Focus: at 1366x768 and 680x425 the dancer and scarf are the central, largest thing in Watch, and the scarf alone fills Your turn; the part word is readable.
2. Every feeling, five shapes at start and end and six middle moves play a 16-count dance (4, 8, 4) with no console error.
3. Each middle move gives the scarf a visibly different flow (Float drifts, Swirl circles, Zap snaps, Melt droops, Shiver flutters, Leap streams), checked in frames.
4. Tap while it plays: changing a part, the feeling, Slow or Mirror during a run shows at once (the dancer tweens within 200 ms, the card updates), and Stop stops everything at once.
5. No line is spoken over the music; lines queued during a run play after it or are dropped.
6. Your turn shows the scarf moving exactly as in Watch, with the dancer hidden, and ends with Freeze and 3 quiet seconds.
7. Share chips light and speak every time; Swap clears them.
8. How-to lines are spoken once in a run of five actions.
9. Every control is 60 px or more with an icon and a word; Play and Go are visible without scrolling at every size in STANDARDS.md.
10. Motion off: one pose per count, the scarf hangs straight; music and counts keep time. No network requests; nothing is saved.
