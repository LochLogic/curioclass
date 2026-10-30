# Parade and Bedtime Music

## One idea
The same tune can belong to a parade or to bedtime: after the class sorts eight short tunes into the moments they fit and names the clue (fast or slow, loud or soft), two big dials turn the parade march itself slower and softer while the street outside melts into a moonlit bedroom, so speed and loudness are heard as the clues that did the sorting.

## Not like
- beat-buddies (k-2, showdown): keeps a steady beat and freezes when the music stops. Here nobody keeps the beat; the class listens for the mood and the moment a tune fits.
- sound-elevator (k-2, sandbox): high and low notes on an elevator, loud and soft as a glow. Here loud and soft (with fast and slow) are reasons a tune fits a moment, and they reshape a whole tune.
- orchestra-zoo (k-2, explorer): which instrument is it. Here the instrument does not matter; the moment does.
- name-song-practice (k-2, studio, this batch): the class makes and sings its own song. Here the class only listens, sorts and turns dials.
- song-form-builder (3-5, builder): arranges sections. Here a tune never changes its notes; only how fast and how loud it is played.

## Who and how
- Grade K-2, music, module "Music for Every Moment".
- Driver: teacher on a projector or smartboard; the class listens, votes with hands, names clues out loud, and may sway or march at their seats. 15 to 20 minutes.
- Standards: NCAS MU:Re8 (interpret: expressive qualities like dynamics and tempo show a mood), MU:Re9 (evaluate: say what you like and why), MU:Cn11 (relate music to daily life: music for bedtime, parades, birthdays, rain).

## Screens and modes
Header: title, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`, icon plus word): `Sort` (basket icon, default), `Turn it` (dial icon). Every control is 60 px or more with an icon and a word.

**Sort.** Focus: the four moment scenes in a 2 by 2 grid filling the stage: `Bedtime` (moon), `Parade` (drum), `Birthday` (cake), `Rainy day` (umbrella), each a painted scene with its icon and word on a banner. Above them, a row of eight tune cards (`Tune 1` to `Tune 8`), each a big round button with a music-note icon and its own shape mark (circle, square, triangle, star, heart, diamond, moon, cloud) so cards differ by more than color. A fifth small basket at the end of the row, `Somewhere else` (question mark), takes a tune the class wants to place in its own moment.
- Tap a tune card: it plays once (6 to 13 s) and its note icon bounces on each beat; the card grows and lights while it plays. Tap it again to stop.
- Drag a card (or tap the card, then tap a scene) into a scene: it sits in the scene's corner, and the clue tray opens under the grid: five chip pairs, `Fast` / `Slow`, `Loud` / `Soft`, `High` / `Low`, `Bouncy` / `Smooth`, `Happy` / `Sad` (each with an icon: hare and snail, big and small speaker, up and down arrow, ball and wave, sun and rain cloud).
- Tap a chip: the narrator says whether the tune has it (see Content). Each tune keeps the chips it earned as small badges on its card.
- `Composer's note` (pencil icon) on a placed card shows which moment the tune was written for, as a gentle reveal: "I wrote this one for bedtime." It never says the class was wrong; a different moment is fine if they can say why.
- Each card has a heart (60 px) for `Our favorite`; one heart at a time.

**Turn it.** Focus: the big scene, which is the Parade street on the left half fading into the Bedtime bedroom on the right; a painted toy drum and a teddy bear stand in the front. Two huge dials below the scene, `Speed` (hare at the top end, snail at the bottom) and `Loudness` (big speaker, small speaker), each with plus and minus buttons (60 px) and a value bar of filled dots. A meter across the top of the scene, from `Parade` (drum icon) to `Bedtime` (moon icon), with an arrow that shows where the tune sits now. Buttons: `Play` / `Stop` (big, gold), `March again` (back to 120 and 9).
- While it plays, the tune loops, the drum bounces on every beat and the teddy rocks, both scaled by the meter (the drum's bounce shrinks as the arrow moves to Bedtime, the teddy's rock grows). The scene cross-fades with the arrow: the street at Parade, the bedroom at Bedtime, a dusk mix between.

## Content
**Tunes** (all original, made in code with Web Audio; name; written for; tempo, meter; loudness gain; sound; notes as pitch(beats)):
1. Starlight Hush; Bedtime; 66 bpm, 3/4; 0.10; music box (sine with a soft bell attack), pad below. Melody: E5 D5 C5 | D5 E5 G4 | E5 D5 C5 | C5(3). Pad: C3+G3, G2+D3, C3+G3, C3+G3 (one per bar).
2. Rocking Boat; Bedtime; 58 bpm, 4/4; 0.12; low hum (triangle, slow attack). G3 A3 B3 D4 | B3 A3 G3(2) | G3(4).
3. Big Drum March; Parade; 120 bpm, 4/4; 0.48; brass (sawtooth through a low-pass at 1800 Hz, short notes at 60% of the beat), kick on 1 and 3, snare on 2 and 4. C4 C4 E4 G4 | C5(2) G4(2) | A4 A4 G4 E4 | F4 D4 C4(2).
4. Banner Wave; Parade; 112 bpm, 2/4; 0.40; piccolo (sine with light vibrato, an octave up), snare in eighths. G5 G5 | A5 B5 | C6 B5 | A5 G5 | E5 G5 | A5 G5 | D5 E5 | G5(2).
5. Candle Cheer; Birthday; 108 bpm, 3/4; 0.25; bright pluck, claps on beats 2 and 3. C4 E4 G4 | E4 G4 C5 | B4 A4 G4 | C5(3).
6. Party Hop; Birthday; 128 bpm, 4/4; 0.30; pluck plus bouncy bass on every beat, clap on 2 and 4. C4 E4 G4 E4 | F4 A4 G4(2) | C5 B4 A4 G4 | F4 E4 D4 C4.
7. Drip Drop; Rainy day; 84 bpm, 4/4; 0.14; high plucks in eighths (staccato, like drips) over an A minor pad. A5 E5 C5 E5 A5 E5 C5 E5 | G5 D5 B4 D5 G5 D5 B4 D5 | F5 C5 A4 C5 F5 C5 A4 C5 | E5 B4 G#4 B4 A4(2) (bar 4 eighths, then A4 held).
8. Window Gray; Rainy day; 70 bpm, 4/4; 0.12; soft low piano (two sines with a quick decay), smooth. D3 F3 E3 D3 | C3(2) A2(2) | Bb2 C3 D3 F3 | E3(2) D3(2).

**Clue table** (what each tune has; "middle" means neither chip of the pair):
| Tune | Speed | Loudness | High/Low | Bouncy/Smooth | Happy/Sad |
|---|---|---|---|---|---|
| 1 | Slow | Soft | High | Smooth | Happy |
| 2 | Slow | Soft | Low | Smooth | Happy |
| 3 | Fast | Loud | middle | Bouncy | Happy |
| 4 | Fast | Loud | High | Bouncy | Happy |
| 5 | middle | middle | middle | Bouncy | Happy |
| 6 | Fast | middle | middle | Bouncy | Happy |
| 7 | middle | Soft | High | Bouncy | Sad |
| 8 | Slow | Soft | Low | Smooth | Sad |
Rules used to fill it: Fast is 100 bpm or more, Slow is 70 or less; Loud is gain 0.35 or more, Soft is 0.15 or less; High is more than half the melody notes at or above C5, Low more than half below C4; Bouncy is detached notes or a strong beat, Smooth is held, joined notes; Sad is minor.

Chip answers: has it: "Yes! It is <chip word>." ; the other side of the pair: "Listen again. Is it <chip word>, or <other word>?" (and the card plays again); middle: "It is in the middle. Try another clue."

**Turn it numbers.** Speed 50 to 140 bpm in steps of 10 (10 dots). Loudness 1 to 10; gain = 0.08 x 1.25^(level - 1), so 0.08 at 1 and 0.60 at 10. Meter position p = average of (speed - 50) / 90 and (loudness - 1) / 9, from 0 (Bedtime) to 1 (Parade). p of 0.7 or more: "Parade"; 0.3 or less: "Bedtime"; between: "In between". Start: 120 and 9 (p = 0.83, Parade).

## Interactions in detail
- One sound at a time: playing a tune stops any other. A tap on any control while a tune plays acts at once (a new card, a drag, a chip, a mode switch, Stop).
- Turn it: the dials change the sound at once. The scheduler looks ahead 100 ms; a speed change re-times every unplayed note from the current point in the tune, so the new speed starts within 100 ms, never at the next bar. Loudness ramps the gain over 50 ms. The meter arrow, cross-fade, drum and teddy follow every change at once.
- Crossing into Bedtime (p goes from above 0.3 to 0.3 or less) speaks the lullaby line; crossing into Parade (from below 0.7 to 0.7 or more) speaks the march line; both every time they happen (event), each stale after a further dial change.
- Fast and soft (140 and 1) or slow and loud (50 and 10) both land In between (p = 0.5): the narrator line for In between asks what the class hears ("Hmm, in between. Is it a parade, or bedtime?") once per page load (how), then only the hint changes.
- Sort keeps cards where they are when switching modes (memory only). `Start over` (Sort bar, with `Yes, start over` and `Keep it`) puts every card back in the row and clears badges and the heart.
- Sound off: tunes still animate their note icons silently, and a line under the cards says "Turn Sound on to hear the tunes." Before the first tap nothing plays (kit rule).
- Motion off: no bounce, rock or cross-fade animation; the scene switches between street, dusk and bedroom in three steps; the meter arrow still moves.
- Keyboard: 1 to 8 play tunes, arrows turn the selected dial, Space plays or stops in Turn it.

## Look
- Accent (`--brand`) #5b3596 twilight violet (header, Play, lit cards). Paper #f7f5fb, ink #211a2e, muted #5f5670. Scenes: parade street in bunting reds and yellows, bedroom in deep blue #24305e and moonlight cream, birthday in pinks, rainy day in grey-blues. Tune card shape marks white on violet.
- Contrast (WCAG 2.1, computed): white on brand 8.77:1; brand on paper 8.11:1; ink on paper 15.50:1; muted on paper 6.36:1.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8, act-it-out #7d2e7f, levels-and-pathways #00798c.

## Art
Local FLUX (`scripts/localart.py`). No people. One soft watercolor picture-book style.
- moment-bedtime: "A cozy child's bedroom at night, a small bed with a patchwork quilt, a big window with a round moon and stars, a soft lamp glow, soft watercolor picture book illustration"; 16:10; cutout no; people no; Sort scene and the right side of Turn it.
- moment-parade: "A small town main street ready for a parade, colorful bunting and balloons, flags on lampposts, a sunny sky, an empty road down the middle, soft watercolor picture book illustration"; 16:10; cutout no; people no; Sort scene and the left side of Turn it.
- moment-birthday: "A kitchen table set for a birthday party with a frosted cake with candles, wrapped presents, paper party hats and streamers, soft watercolor picture book illustration"; 16:10; cutout no; people no; Sort scene.
- moment-rain: "A rainy day seen through a window with raindrops on the glass, a pair of red rain boots and a yellow umbrella by the door, grey sky, soft watercolor picture book illustration"; 16:10; cutout no; people no; Sort scene.
- toy-drum: "A small red and gold toy marching drum with two drumsticks resting on top, soft watercolor picture book illustration, plain white background"; 1:1; cutout yes; people no; bounces on the beat in Turn it.
- teddy: "A soft brown teddy bear sitting, slightly sleepy, soft watercolor picture book illustration, plain white background"; 1:1; cutout yes; people no; rocks on the beat in Turn it.
6 images, none with people. Drawn in code: tune cards, shape marks, chips, dials, the meter, the dusk blend and the bouncing note icons.

## Voice
Bank voice `friendly-dad` (Achird), style "Say in a relaxed, friendly way, like a kind dad helping with homework". Fits a tool about everyday family moments. Not used by any K-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, sound-elevator hero-coach, act-it-out gentle-storyteller, levels-and-pathways warm-teacher) or by another K-2 spec in this batch. `Curio.voice` with `scope: () => state.mode`. The narrator never talks over a playing tune: every line waits (`valid: () => !state.playing`) except the dial crossing lines in Turn it, which play over the music (they are about it) at the music's level, ducked by 6 dB while spoken.

- how, welcome (Sort; stale once a card is tapped): "Music fits the moments of our day. Tap a tune card to listen."
- how, after the first tune ends (stale when a card is placed): "Where does it fit? Drag the card to bedtime, a parade, a birthday or a rainy day."
- how, first card placed (stale when a chip is tapped): "What is the clue? Tap a clue word."
- event: each chip answer in Content, every tap.
- event, Composer's note: "I wrote this one for <moment>." (4 lines), then once per page load (how): "Could it fit somewhere else too? Tell why."
- event, heart: "That's our favorite! What do you like about it?"
- how, welcome (Turn it; stale when Play is tapped): "Here is the parade march. Tap Play. Then turn the dials."
- how, after the first dial change while playing (stale on the next dial change): "Watch the street. Keep turning."
- event, crossing into Bedtime: "Now it's a lullaby! Slow and soft fits bedtime."
- event, crossing into Parade: "It's a march again! Fast and loud fits a parade."
- how, first In between at the extremes (above): "Hmm, in between. Is it a parade, or bedtime?"
- Read speaks the hint (the current step) or the open card's chip answer.

## Family engine
none

## Sources
- National Core Arts Standards, Music, grades K to 2 (MU:Re8, MU:Re9, MU:Cn11): https://www.nationalartsstandards.org
- Tempo and dynamics as expressive qualities, and lullabies as slow, soft and smooth: Trehub, S. E., and Trainor, L. J. (1998), "Singing to infants: lullabies and play songs", Advances in Infancy Research 12, 43 to 77; marches at about 120 beats a minute: US Army Field Manual 3-21.5, Drill and Ceremonies, quick time 120 steps a minute.
- All eight tunes are original melodies written for this tool (no public-domain or copyrighted tune is quoted; none is "Happy Birthday").
- Checks run (Python, 2026-10-29): tune lengths at their tempos: 1 is 10.9 s, 2 is 12.4 s (12 beats at 58), 3 is 8.0 s, 4 is 8.6 s, 5 is 6.7 s, 6 is 7.5 s, 7 is 11.4 s, 8 is 13.7 s; Big Drum March at 50 bpm loops in 19.2 s. Gains: level 1 0.080, 5 0.195, 9 0.477, 10 0.596 (17.4 dB span). Meter: (120, 9) p 0.83 Parade; (140, 10) 1.00 Parade; (50, 1) 0.00 Bedtime; (70, 3) 0.22 Bedtime; (140, 1) and (50, 10) 0.50 In between; (110, 7) 0.67 In between; (80, 4) 0.33 In between. The clue table was checked against its own rules: melody notes at or above C5 are 0.90 (tune 1), 0, 0.08, 1.00, 0.20, 0.07, 0.72, 0 of each melody, and below C4 are 0, 0.88, 0, 0, 0, 0, 0, 1.00, so 1, 4, 7 High, 2, 8 Low, the rest middle; tempos 66, 58, 70 are Slow; 120, 112, 128 Fast; 108 and 84 middle. Gains 0.40 and 0.48 are Loud; 0.10 to 0.14 Soft; 0.25 and 0.30 middle. Contrast ratios as listed.

## Done when
1. Focus: at 1366x768 and 680x425 the four scenes fill the Sort stage and every tune card is a 60 px target; in Turn it the scene and both dials are visible without scrolling.
2. Every tune plays its notes at its tempo and loudness, and no two play at once.
3. Every chip answer matches the clue table for all eight tunes (40 chip pairs).
4. Tap while it plays: a dial tap during Big Drum March changes the tempo within 100 ms and the meter, scene, drum and teddy at once; a new card during a tune stops the old one at once.
5. Turning both dials down crosses into Bedtime and speaks the lullaby line every time; turning back up speaks the march line.
6. (140, 1) and (50, 10) both show In between.
7. The narrator never starts a line over a playing tune in Sort; how-to lines are spoken once in a run of five actions.
8. Composer's note never says "wrong"; a card can sit in any scene or in Somewhere else.
9. Sound off: no audio, the note icons still bounce, and the Sound hint shows. Motion off: three-step scene change.
10. No network requests; nothing is saved.
