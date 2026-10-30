# Cartoon Soundtrack Mixer

## One idea
Score a 24-second silent cartoon on a timeline under the picture, then tap Mood Swap while it plays: the same frames keep running but the sound jumps between your score and a funny, a scary and a sad one, so you see that the music, not the drawing, decides whether a cat in a storm is a joke, a fright or a heartbreak.

## Not like
- sound-and-picture-book (K-2, A1's band): a story book where recorded sounds go with pictures. Here the student builds a timed score with tempo, loudness and instrument for each scene, and compares moods live.
- beat-lab (9-12, studio): produces a full track from patterns. Here there is no beat-making; each scene gets one cue shaped by four plain choices, plus sound effects placed on the picture.
- song-form-builder and melody-maker (3-5): write or arrange melodies. Here the melodies are made for you; the student chooses how they are played.
- music-history-radio (9-12): music eras. Here the history is one card about silent-film pianists.
- place-mood-makeover (this band): mood from the picture itself. Here the picture never changes; only the sound does.
- flipbook-studio (6-8): timing of drawn frames. Here the frames are fixed and the timing is the music's.

## Who and how
- Grade 3-5, media arts and music, module "Sound and Picture Together (Media Arts)".
- Topic line: scoring a silent cartoon
- Driver: students (headphones, solo or a pair) or teacher (projector; the class votes on each scene's mood). 15 to 30 minutes.
- Standards: MA:Pr4 (combine music, effects and moving pictures into one work), MA:Cn10 (score from your own idea of the story), MU:Re8 (name how tempo, dynamics and timbre carry the mood), MU:Cn10 (your choices and reasons as the composer), MU:Cn11 (music's job in film, and the silent-film pianists who did it live).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit). Mode buttons: `Theater` (default), `Score it`, `Mood Swap`.

**Theater (the opener).** Focus: the painted theater piano beside a small movie screen (16:9 stage). The cartoon plays once silent on the screen (`Play silent`, 24 s). A card beside it: "Before movies had sound, a pianist or organist in the theater played along, live, to fit each scene. Many used books of music sorted by mood, so they could flip to a storm or a chase in seconds." `Hear it three ways` plays scene 2 (the storm, 6 s) three times in a row under the Funny, Scary and Sad scores, naming each. `Start scoring` switches to Score it.

**Score it (the studio).** Focus: the movie screen (top, 16:9, the biggest thing) and the timeline under it (two tracks, 24 s, four scenes of 6 s each marked by thin lines and scene names).
- Music track: four blocks, one per scene. Tap a block to open its shaper in the panel: `Feel` (Bright, Dark, Creepy: which melody set plays), `Tempo` (Slow, Medium, Fast), `Loudness` (Soft, Medium, Loud), `Instrument` (Piano, Tuba, Strings, Xylophone), `Style` (Smooth, Bouncy). Each block shows its choices as small words and an instrument icon. Or tap a preset chip on the block (`Tiptoe`, `Chase`, `Lullaby`, `Storm`, `March`, `Mystery`; Content) to set all five at once.
- Effects track: an effects shelf in the panel with ten sound effects (Content). Drag one onto the effects track (or tap it, then tap the timeline) at a time; it snaps to 0.25 s and shows as a labeled chip with its length. Drag a chip to move it, drag it off the track or tap it and `Remove` to delete. Up to 16 effects.
- `Play` (becomes `Stop`) plays picture and sound together from the playhead; tap or drag on the timeline ruler to move the playhead (scrubbing shows the frame). `Play scene` plays just the selected scene.
- `My cartoon is...` chips (Funny, Scary, Sad, Sweet, Exciting): the student's intended mood, used in Mood Swap and the write-up.
- `Clear score`.

**Mood Swap.** Focus: the movie screen, full stage width, with four big switch buttons under it: `Yours`, `Funny`, `Scary`, `Sad`. `Play` starts the cartoon; tapping a switch at any moment changes the sound at once while the picture keeps running (the old music fades in 80 ms, the new score enters at the same time position). A strip under the switches shows the current score's choices for the scene that is on screen ("Scene 2, Scary: Dark, Fast, Loud, Strings, Smooth + thunder") so the student can name what changed.
- `Write it`: a card with two starters: "My cartoon is ___. The music in scene ___ makes it feel that way because the tempo is ___, it is ___ (soft or loud) and the ___ sounds ___." and "The ___ score turns it into a different story because ___." Saved on this device.
- `Class guess`: hides the switch labels; plays one score chosen at random (Funny, Scary, Sad or Yours); the class guesses, then `Show` names it.

## Content
**The cartoon** ("Whiskers and the Storm", original, black and white, 24 s; times are the start of each beat):
- Scene 1 "Fence" (0 to 6 s): night, the cat walks along the fence from left to right (walk cycle, two poses, 4 steps a second at the painted scale); at 4.5 s it stops and looks up at the moon.
- Scene 2 "Storm" (6 to 12 s): clouds slide over the moon; at 7.0 s a lightning flash (the frame flashes white for 120 ms, Motion off: a 300 ms gray tint); at 7.2 s the cat's fur puffs (startled pose) and it jumps down from the fence (8.0 to 8.6 s); rain starts at 8.0 s (code streaks); the cat runs to the porch (9 to 12 s).
- Scene 3 "Box" (12 to 18 s): on the porch, the cat freezes (listening pose) at 13 s; the box on the porch wobbles at 14 s and 15.5 s; at 16 s a tiny kitten peeks out of the box.
- Scene 4 "Home" (18 to 24 s): the cat carries the kitten through a cat door (18 to 20 s), then the two curl up by a window with rain on the glass (20 to 24 s), the last 1.5 s fades to black.

**Effects** (made in code; name, length): Thunder (2 s), Rain (loops while placed, 3 s chip, can be stretched to 6 s), Tiptoe steps (1 s), Running steps (1 s), Boing (0.5 s), Slide whistle down (0.75 s), Meow (0.75 s), Tiny mew (0.5 s), Door creak (1 s), Heartbeat (2 s).

**Cue sets** (the melodies a block plays; generated in code, 2-bar loops in 4/4 repeated to fill 6 s at the block's tempo; scale rows as in `MS.SCALES`):
- Bright: major, do mi sol mi re fa la sol, then mi sol do' sol fa re ti, do (two bars of eighths).
- Dark: natural minor from la: la do mi do ti re fa mi, then do mi la mi re ti si la (si is the raised seventh).
- Creepy: a slow chromatic crawl: sol fi fa mi, mi fa fi sol (half steps) over a low drone on do.
Tempo: Slow 66, Medium 104, Fast 152 beats a minute. Loudness: Soft 0.35, Medium 0.6, Loud 0.9 (gain). Style: Smooth notes last 95% of their length, Bouncy 40%.
Presets: Tiptoe (Bright, Medium, Soft, Xylophone, Bouncy); Chase (Bright, Fast, Loud, Piano, Bouncy); Lullaby (Bright, Slow, Soft, Strings, Smooth); Storm (Dark, Fast, Loud, Strings, Smooth); March (Bright, Medium, Loud, Tuba, Bouncy); Mystery (Creepy, Slow, Soft, Strings, Smooth).

**Ready-made scores** (scene 1 / 2 / 3 / 4, then effects with times):
- Funny: Tiptoe / March (Tuba) / Tiptoe / Chase. Effects: Tiptoe steps 1.0 s, Boing 7.2 s, Slide whistle 8.0 s, Running steps 9.0 s, Meow 13.0 s, Tiny mew 16.0 s.
- Scary: Mystery / Storm / Mystery / (Creepy, Slow, Soft, Piano, Smooth). Effects: Heartbeat 1.0 s, Thunder 7.0 s, Rain 8.0 s (to 12 s), Door creak 14.0 s, Tiny mew 16.0 s.
- Sad: (Dark, Slow, Soft, Piano, Smooth) / (Dark, Medium, Medium, Strings, Smooth) / (Dark, Slow, Soft, Piano, Smooth) / Lullaby. Effects: Rain 6.0 s (to 12 s), Thunder 7.0 s, Tiny mew 16.0 s, Rain 20.0 s (to 24 s).
The starting score in Score it is blank (no blocks set: the cartoon plays silent until a block is shaped).

## Interactions in detail
- Sound is the music-studio engine. It needs two new instruments in the engine (made there, with its doc): `tuba` (a low brass voice an octave below the written row: sawtooth through a 700 Hz lowpass, soft attack) and `strings` (two detuned sawtooths, 120 ms attack, 1800 Hz lowpass). Piano uses `INSTR.piano`, Xylophone `INSTR.marimba` with a shorter decay. Effects are this tool's own Web Audio (noise bursts for thunder and rain, short clicks for steps, sine glides for boing and slide whistle, a formant glide for meows, a slow sawtooth sweep for the creak, low sine thumps for the heartbeat).
- Playback: one clock for picture and sound. Each music block is scheduled as its own `MS.play` with `exclusive: false` at its scene's start; effects are scheduled on the same audio clock. The picture is drawn from the clock's time, so picture and sound never drift. Sound off: the picture still plays on the page clock.
- Every control is live while it plays: changing a block's Tempo, Loudness, Instrument, Feel or Style changes that block from the next note (under 150 ms) if it is playing; moving or adding an effect ahead of the playhead schedules it; Stop stops at once; a Mood Swap switch changes the score at once (the incoming score starts mid-cue at the current time, never waiting for a bar line).
- Scrubbing while stopped shows the frame at that time; scrubbing while playing jumps there and keeps playing.
- Effects that would run past 24 s are clipped at 24 s. A chip dropped onto another chip at the same time nudges right by 0.25 s; two effects may overlap in time (they sit in two lanes of the effects track).
- Narrow screens: under 600 px wide the timeline shows 30 px a second and scrolls with the playhead (the playhead stays in the middle third); every chip has a 44 px tall grab area.
- Keyboard: Space plays or stops; 1 to 4 select a scene's block; arrows move a selected effect by 0.25 s; Delete removes it. Tab order: panel, then blocks, then effects.
- Saved on this device (localStorage `cartoon-soundtrack-mixer`): the score, the intended mood and the write-up. `Clear score` clears the score.
- Voice lines never play over the cartoon: `Play` hushes the voice, and result lines wait for the end.

## Look
- Silent-film theater, dark: paper #17120d (near black), raised panels #2a221a, ink #efe6d4 (cream), muted #b3a68e, accent (`--brand`) #e9b949 marquee gold with #17120d text on gold buttons. Block colors by Feel, each also with its word and a pattern: Bright #f2d27a (plain), Dark #8fb6f0 (diagonal lines), Creepy #c9a2e8 (dots); effect chips #9fd8a8 with dark text and an icon. The cartoon itself is black and white with film grain (code) inside a thin gold frame.
- Contrast: dark text on gold 10.19:1; gold on paper 10.19:1; cream on paper 15.01:1; muted on paper 7.76:1; cream on panel 12.62:1; gold on panel 8.57:1; dark text on Bright 12.65:1, on Dark 8.96:1, on Creepy 8.70:1, on effect chips 11.39:1.
- Different from neighbors: song-form-builder teal, melody-maker burnt orange, flipbook-studio red on charcoal, storyboard-studio coral on maroon, character-voice-booth brass on slate (this is a near-black sepia with marquee gold).

## Art
Local FLUX, no people. Style line: "1920s black and white rubber hose cartoon style, bold ink outlines, flat gray tones" (cartoon pieces); "warm painted look, soft stage light" (theater).
- theater-piano: "an old movie theater from the 1920s, an upright piano with sheet music on its stand and an empty piano stool in front of a small glowing blank movie screen, velvet curtains, warm lamp light"; 16:9; Theater mode.
- bg-fence-night: "a wooden backyard fence running across the picture at night, a big round moon, rooftops behind, rubber hose cartoon style"; 16:9; scenes 1 and 2 (storm made in code: darkening, clouds, rain, flash).
- cloud: "a single fluffy storm cloud, rubber hose cartoon style"; 4:1; cutout yes; slides over the moon.
- bg-porch: "a wooden porch with steps and a cardboard box on it, a door with a small cat door, rubber hose cartoon style"; 16:9; scene 3 and the start of 4.
- bg-window: "inside a cozy room, a round rug in front of a window with rain on the glass, rubber hose cartoon style"; 16:9; scene 4.
- Cat cutouts (one pose each, "a black and white cartoon cat with big white eyes, rubber hose cartoon style, <pose>"), 1:1, cutout yes: cat-walk-a (walking, front paw forward), cat-walk-b (walking, back paw forward), cat-look (standing, looking up), cat-puff (startled, fur puffed, tail straight up), cat-jump (leaping down, legs stretched), cat-run (running fast, stretched out), cat-listen (frozen, ears up, one paw raised), cat-carry (walking, holding a small kitten gently by the scruff), cat-curl (curled up asleep around a small kitten).
- kitten-peek: "a tiny cartoon kitten peeking over the edge of a cardboard box, rubber hose cartoon style"; 1:1; cutout yes.
- box: "a cardboard box with open flaps, rubber hose cartoon style"; 1:1; cutout yes (wobbles in code).
- 15 generated images, none with people. Drawn in code: rain, lightning, film grain, fades, the timeline, blocks, chips, icons, the switch bar, all text.

## Voice
Bank voice `upbeat-guide` (Zephyr), style "Say brightly and clearly, like an upbeat tour guide": a theater usher showing you to the piano bench. Not used by any 3-5 arts neighbor or another tool in this band. `Curio.voice` with `scope: () => state.mode`.
- welcomeTheater (how; entering Theater; stale when Play silent or Hear it three ways is tapped): "Long ago, movies had no sound. Tap Play silent to watch this one the way the audience did."
- threeWays (how; after Play silent ends; stale when Hear it three ways is tapped): "Now tap Hear it three ways. Same storm, three kinds of music."
- welcomeScore (how; entering Score it with a blank score; stale when a block is shaped): "Tap a music block under a scene. Then pick its feel, tempo, loudness and instrument."
- effectsHow (how; after two blocks are shaped; stale when an effect is placed): "Drag a sound effect onto the timeline where it should happen. Then tap Play."
- welcomeSwap (how; entering Mood Swap; stale when Play is tapped): "Tap Play. While it runs, tap Funny, Scary or Sad to swap the music."
- swapName (event; each switch tap during play, only after the cartoon ends so it never talks over it; stale when Play starts again): "That was the scary score." (dropped if another switch is tapped first)
- writeHow (how; after the first full play in Mood Swap; stale when Write it is tapped): "Which music fits your story? Tap Write it and name the tempo, the loudness and the instrument."
- guessShow (event; after Show in Class guess): "That was the sad score."

## Family engine
music-studio (`kit/music-studio.js`): `MS.SCALES` and `MS.freq` for the three cue sets (key C), `MS.play` with `exclusive: false` per block on one start time, live `p.bpm`, `MS.INSTR.piano` and `marimba`, the master and room buses. Adds `tuba` and `strings` to `MS.INSTR` (in the engine and its doc, keeping existing calls working) and a per-player gain (Loudness) if the engine has none. Its own: the cartoon, the effects, the timeline and Mood Swap.

## Sources
- Silent films were shown with live music, from a single pianist or organist to an orchestra, often improvised or chosen from cue sheets and mood-music collections: Library of Congress, "Silent Film Music" research guide and the "Motion Picture Music" collection notes, https://www.loc.gov/ ; Rick Altman, Silent Film Sound (Columbia University Press, 2004).
- Mood-music books sorted by mood (storms, chases and more) for theater players: Erno Rapee, Motion Picture Moods for Pianists and Organists (G. Schirmer, 1924), public domain scan at IMSLP, https://imslp.org/wiki/Motion_Picture_Moods_(Rapee,_Erno)
- Tempo, dynamics and timbre as the elements that carry mood in film music: National Core Arts Standards, Music, MU:Re8 grade 3 to 5 examples, https://www.nationalartsstandards.org/
- Rubber hose animation as the 1920s cartoon style: Smithsonian Magazine, "The rubber hose style of early animation" coverage, and Library of Congress National Screening Room notes on 1920s cartoons, https://www.loc.gov/collections/national-screening-room/ (named as a style; the cartoon is original).
- The cartoon, cues and scores are written for Curio Class.
- Checks run (Python, 2026-10-29): timeline scale at each size (24 s across about 62% of the stage width on wide screens): 680 wide 27 px a second, 1366 wide 35, 1920 wide 50, 375 wide only 14, so narrow screens get the 30 px a second scrolling timeline and 44 px grab areas; a 2-bar loop of eighths is 7.3 s at 66 (a 6 s block plays 82% of it), 4.6 s at 104 and 3.2 s at 152, so every block loops or cuts cleanly at its scene line. Contrast ratios with the WCAG 2.1 formula.

## Done when
1. Focus: at 1366x768, 680x425 and 375 wide the movie screen is the largest thing and the timeline sits under it without scrolling the page.
2. A tap on Funny, Scary or Sad while the cartoon plays changes the sound within 150 ms and the picture never stops or jumps.
3. Changing a playing block's tempo, instrument or loudness is heard on the next note.
4. Effects land where dropped (within 0.25 s) and sound at that time on every play; the ready-made scores' effects hit the flash at 7.0 s and the kitten at 16.0 s.
5. Picture and sound stay in step for the whole 24 s at all three tempos (the frame time and the audio time differ by under 50 ms at the end).
6. No voice line plays during the cartoon; swapName waits until it ends.
7. Motion off: the flash becomes a gray tint, the cat still moves between poses on time.
8. The score and write-up survive a reload; `Clear score` empties them.
9. How lines are spoken once in a run of five edits.

## Open questions
- None for Cory.
