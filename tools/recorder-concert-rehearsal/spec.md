# Recorder Concert Rehearsal

## One idea
You run rehearsal for a four-player recorder group, and the next take changes exactly what your note named: name the right player, the right bar and the right fix ("Bea, cover the holes all the way in bar 2") and that one problem is gone; name the wrong player or say "sound better!" and the take comes back the same, so listening closely and giving one clear note is the whole skill.

## Not like
- band-practice (6-8, music): you play your own part against a band and see your timing. Here you never play during rehearsal; you listen, diagnose and coach four other players.
- song-form-builder (3-5, builder, same music engine): builds forms from section blocks. Here the music is fixed and the players are imperfect; the skill is hearing what is wrong.
- melody-maker (3-5, studio): composes on a scale grid. Nothing is composed here.
- note-ninja (3-5, arcade): names notes against a clock. No timer or score here.
- character-voice-booth (3-5, lab): compares your own voice takes. Here the takes are a group's, and you change them only through feedback.

## Who and how
- Grade 3-5, music, module "Ensemble Rehearsal and Concert (Music)".
- Topic line: leading a rehearsal
- Driver: students (headphones, solo or a pair) or teacher (projector; the class marks the checklist together by show of hands). 15 to 30 minutes.
- Standards: MU:Pr5 (use criteria and feedback to refine the ensemble take by take), MU:Pr6 (perform your own part at the concert, with concert manners), MU:Re9 (evaluate each take against the checklist).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit). Mode buttons: `Rehearsal` (default), `Concert`.

**Rehearsal.** Focus: the four players in the painted music room (stage, 16:9), each standing on a numbered spot with a name tag and badge; above them a bar strip `1 2 3 4` (Hot Cross Buns) or `1` to `8` (Au Clair de la Lune) with a playhead. Panel: the piece picker (`Hot Cross Buns`, `Au Clair de la Lune`, `New rehearsal` for random problems), the take counter ("Take 1"), the clipboard checklist, and the note builder.
- `Play take` (becomes `Stop`): a 4-click count-in, then the whole piece. The player who is playing a note lifts to the playing pose (cutout swap); the bar strip playhead moves.
- Listening tools (always live): tap a player to `Solo` them (the take replays with only that player; tap again for all); tap a bar number to `Loop bar` (that bar, everyone or the soloed player, until tapped again); `Score view` toggle: four lanes under the room, one per player, with each note drawn as a block against a light beat grid; a late note sits right of its line, a sharp note sits above its line with a small up arrow, a squeak shows a spark, a mid-phrase breath shows a gap with a breath mark. Score view starts off ("Listen first, then check your ears.").
- Clipboard checklist, four lines, each `OK` or `Needs work`: `Together` (everyone starts and ends at the same time), `Clear tone` (no squeaks, in tune), `Steady beat` (no rushing or dragging), `Phrasing` (breathe only at the ends of phrases).
- Note builder (opens after the take ends): `Who` (Juniper, Otis, Bea, Finn, Everyone), `Where` (a bar number, or Whole piece), then three note cards for the criterion chosen on the clipboard (Content: one fix, one fix for a different problem, one vague). `Give note` sends it; the players nod (cutout swap) and `Play take` plays the next take.
- After the take: a line says what changed, or that nothing did ("They tried, but nobody knew what to change."). When all problems are gone: "Ready for the concert." and `Go to the concert`.
- `Start over` (this piece, take 1 again).

**Concert.** Focus: the painted school stage with the four players and an empty fifth spot (yours), the audience as dark code silhouettes in rows in front. Three parts in order, each tappable:
1. `Stage manners`: four moments as picture cards (Content). Each offers two or three choices; the right choice plays its moment (the hall goes quiet, the players lift recorders together, a held bow) and a wrong one shows why in one line. All four must be met before the curtain opens (retries are free).
2. `Play with them`: your part as a scrolling line (written on a five-line staff, note names under each note, and the fingering diagram for the next note: B, A or G) over the group's clean final take of Au Clair de la Lune. A 4-click count-in, then 20 seconds. Play along on a real recorder, sing the note names or clap the rhythm (`How will you join?` chips set the label only). `Slower` plays it at 80 beats a minute. Nothing is recorded or listened to.
3. `Then and now`: two buttons, `First take` and `Final take`, play the group's take 1 and last take of each piece back to back (or tap either alone). A short card lists the notes you gave, in order.

## Content
Players (painted animal cutouts; badge shape and color so color is never alone): Juniper, a rabbit (circle, #a33a2a); Otis, an owl (square, #2f6b8f); Bea, a badger (triangle, #7a4f9a); Finn, a fox (diamond, #f0b54a with ink).

Pieces (written in G for soprano recorder, notes B, A, G; the recorder sounds an octave above written, so written G4 plays at 783.99 Hz, A 880.00, B 987.77; `MS.parse` lengths, e eighth, h half, w whole):
- Hot Cross Buns (traditional), 4/4, 88 beats a minute, 4 bars: `B A G:h | B A G:h | G:e G:e G:e G:e A:e A:e A:e A:e | B A G:h`. Phrases end at bars 1, 2 and 4.
- Au Clair de la Lune (traditional, France), first half, 4/4, 96 beats a minute, 8 bars: `G G G A | B:h A:h | G B A A | G:w | G G G A | B:h A:h | G B A A | G:w`. Phrases end at bars 4 and 8.

Problems (each take is built from the active problems; each has who, where, the criterion it breaks, the change in sound, and the one note that fixes it):
| id | criterion | sound | fixing card |
|---|---|---|---|
| late | Together | one player starts 150 ms late on the first note | "<Name>, watch me and breathe in on my count." (Where: bar 1 or Whole piece) |
| squeak | Clear tone | one player's G in the named bar has a squeak (a short, high overblown note, 0.15 beat, an octave and a fifth up) | "<Name>, cover the holes all the way with the pads of your fingers." |
| sharp | Clear tone | one player's notes in the named bar are 40 cents sharp (frequency times 1.0234) | "<Name>, blow gently, like warm air on your hand." |
| rush | Steady beat | everyone speeds up through the eighth notes of bar 3 (Hot Cross Buns only): the bar takes 2.37 s instead of 2.73 s | "Everyone, keep the beat steady in bar 3. Feel the eighths, don't hurry." |
| breath | Phrasing | one player breathes in the middle of a phrase: the note before the named point is cut short by half a beat | "<Name>, take your breath at the end of the phrase, not in the middle." |
Wrong-fix cards are the fixing cards of the other problems under the same criterion; for Together and Phrasing the wrong fix is "<Name>, play louder." Vague cards: "Sound better!", "Try harder, everyone.", "That wasn't great. Again!"

Scripted rehearsal (Hot Cross Buns): late (Otis), squeak (Bea, bar 2), rush (Everyone, bar 3). Scripted rehearsal (Au Clair de la Lune): sharp (Finn, bar 2), breath (Juniper, bar 3), late (Bea). `New rehearsal`: three different problems drawn at random from the five, each with a random player and a fitting bar (rush only in Hot Cross Buns bar 3; breath only at a point inside a phrase).

Stage manners (moment, choices, right answer, why line):
1. "The audience is still talking." Start playing / Wait for quiet, recorders ready / Shush them. Right: wait. "Waiting tells the audience the music is about to start."
2. "Before the first piece." Each player plays a long A alone and together to check they match / Skip it / Play the hardest bar fast. Right: the long A. "Tuning first means the group sounds like one."
3. "Between the two pieces." Recorders down, stand still, eyes on the leader / Wave to family / Practice the next piece. Right: still. "Still bodies keep the audience's attention on the music."
4. "After the last note." Hold still a moment, then bow together / Run off / Bow one at a time. Right: hold, then bow together. "The bow says thank you. Together looks like a group."

Fingering diagrams (soprano recorder, baroque or German fingering both use these for B, A, G): B thumb hole and hole 1; A thumb and holes 1 and 2; G thumb and holes 1, 2 and 3 (all left hand).

## Interactions in detail
- Sound: the music-studio engine's flute voice (`MS.blow`) with vibrato depth halved for a recorder; each player is panned slightly (-0.45, -0.15, 0.15, 0.45) so Solo is not the only way to place a sound. Count-in uses `MS.tick`. Takes: Hot Cross Buns 10.9 s plus a 2.7 s count-in; Au Clair de la Lune 20 s plus 2.5 s.
- A note fixes a problem only when Who matches the culprit (or Everyone for rush), Where matches the problem's bar (or Whole piece for late), and the card is the fixing card. Anything else changes nothing. A right fix aimed at a player without that problem changes nothing for them either ("Juniper already covers the holes.").
- Marking the checklist is optional; it filters the note cards to that criterion. The checklist resets each take. With no criterion marked, `Give note` shows all cards.
- During a take every control stays live: Stop stops at once; Solo, Loop bar and Score view switch on the next scheduled note (under 150 ms, the engine's horizon); a tap on a player or bar during a take does what it says immediately, never at the next bar line. Starting a take hushes any voice line; the take's result line is queued for after it ends.
- Takes are counted, never scored. Fewest possible takes per scripted piece: 4 (three notes, then a clean take).
- Motion off: players swap poses without the lift; the playhead jumps by beat.
- Saved on this device (localStorage `recorder-concert-rehearsal`): the notes given and each piece's first and last take settings (problem lists, not audio), for Then and now. `Start over` clears that piece.
- Keyboard: Space plays or stops; 1 to 4 solo a player; Tab order: panel, then players, then bars.
- Sizes: the room and players fit 16:9 at real pixels; at 680x425 Score view replaces the room's lower third rather than adding height, and the panel is compact (Play take, checklist as four small toggles, note builder in one row); at 375 wide the panel stacks under the stage with `Play take` first.

## Look
- Accent (`--brand`) #5a6b14 spring olive. Paper #f7f6ea, ink #1f2414, muted #5c6150, clipboard #e8d9a8 with ink text, panel white. Player colors in Content.
- Contrast: white on brand 5.92:1; brand on paper 5.45:1; ink on paper 14.63:1; muted on paper 5.89:1; ink on clipboard 11.30:1; ink on white 15.90:1; white on Juniper 6.57:1, Otis 5.80:1, Bea 6.15:1; ink on Finn 8.64:1.
- Different from neighbors: song-form-builder teal, melody-maker burnt orange, note-ninja indigo, band-practice cyan on dark, orchestra-zoo green (#2f7a4a is a cooler green).

## Art
Local FLUX, no people (the players are animals). Style line: "warm painted storybook look, soft light, friendly animal characters, for a grade 4 music lesson".
- music-room: "a cheerful elementary school music room, four empty music stands in a row on a wooden floor, a piano against the wall, a blank chalkboard, a window with plants, xylophones on a shelf"; 16:9; cutout no; Rehearsal stage.
- school-stage: "an elementary school stage seen from the audience, red velvet curtains open, five empty music stands, warm stage lights, a wooden floor"; 16:9; cutout no; Concert.
- Player cutouts, two poses each ("<animal>, standing upright, full body, <pose>, holding a plain wooden recorder"), 3:4, people no:
  - juniper-play, juniper-rest: a small brown rabbit with a red scarf; playing pose (recorder to its mouth, paws on the holes) and resting pose (recorder held down in front).
  - otis-play, otis-rest: a round gray owl with a blue bow tie; same two poses.
  - bea-play, bea-rest: a badger with a purple cardigan; same two poses.
  - finn-play, finn-rest: a red fox with a yellow vest; same two poses.
- A nod is the rest pose tipped 6 degrees for 300 ms in code (no extra art).
- 10 generated images, none with people. Drawn in code: the audience silhouettes (rounded heads and shoulders, no faces), name tags, badges, bar strip, playhead, Score view lanes, staff, notes, fingering diagrams, checklist, all text.

## Voice
Bank voice `big-sister` (Leda), style "Say in a friendly, youthful way, like a helpful older student": the older student who usually runs this group and is handing you the clipboard. Not used by any 3-5 arts neighbor or another tool in this band. `Curio.voice` with `scope: () => state.mode + ':' + state.piece`.
- welcomeRehearsal (how; entering Rehearsal at take 1; stale when Play take is tapped): "You're leading rehearsal today. Tap Play take and listen to the group."
- markHow (how; after the first take ends; stale when a checklist line is tapped): "What needs work? Tap Needs work on the clipboard."
- noteHow (how; after the first mark; stale when Give note is tapped): "Now pick who, which bar, and one note card. Then tap Give note."
- toolsHow (how; after the second take, if Solo was never used; stale when a player is tapped): "Not sure who it was? Tap a player to hear them alone."
- fixed (event; after a take where the note fixed a problem; stale when the next take starts): "That fixed it. Otis came in right on time." (built from the problem)
- noChange (event; after a take that changed nothing; stale when the next take starts): "They tried, but nobody knew what to change."
- notThem (event; a right fix sent to the wrong player; stale on the next take): "Juniper already does that. Listen again: who was it?"
- ready (event; first clean take of a piece): "That's a clean take. You're ready for the concert."
- welcomeConcert (how; entering Concert; stale when a manners card is answered): "Before the curtain opens, help the group with stage manners. Tap a choice."
- playHow (how; Play with them opens; stale when its Play is tapped): "Pick how you'll join, then tap Play. Watch the note names as they scroll."
- each manners why line (event; after a choice; stale on the next choice).

## Family engine
music-studio (`kit/music-studio.js`, docs/families/music-studio.md): `MS.parse` for both pieces (key G), `MS.play` with `lead: 4` (count-in), `exclusive: true`, `onStep` for the playhead, live `p.bpm` for `Slower`; `MS.blow` for the recorder voice and `MS.tick` for the count-in. Each player's take is its own event list (`exclusive: false` for the four layers on one start time, or one merged list with `instr` per player). This tool needs two small engine additions, made in the engine and its doc: fractional `semi` in `MS.freq` (the sharp problem, plus 0.4) if it is not already allowed, and a per-event `pan`. Hot Cross Buns is also one of song-form-builder's Listen songs; it is used here as the first piece because it is the first song nearly every recorder class learns (B, A and G only), which the family rule asks a spec to say.

## Sources
- Hot Cross Buns and Au Clair de la Lune: traditional, public domain (Au Clair de la Lune, French folk song, printed in the 18th century); melodies as taught on recorder: Library of Congress, Songs of America, https://www.loc.gov/collections/songs-of-america/ ; "Au clair de la lune", IMSLP, https://imslp.org/wiki/Au_clair_de_la_lune
- Soprano recorder fingerings for B, A, G and that it sounds an octave above written: American Recorder Society, "Recorder fingering charts", https://americanrecorder.org/ ; Aulos/Yamaha soprano recorder fingering chart.
- Too much breath makes a recorder go sharp and squeak; uncovered holes cause squeaks; gentle "warm air" breath: Yamaha Music, "How to play the recorder" guide, https://www.yamaha.com/ ; Walter van Hauwe, The Modern Recorder Player, vol. 1 (Schott, 1984).
- Rehearsal criteria (together, tone, steady beat, phrasing) and concert etiquette (wait for quiet, tune, stillness, bowing together): NAfME, "Concert Etiquette" resources, https://nafme.org/ ; National Core Arts Standards, Music, MU:Pr5 and MU:Pr6 grade 3 to 5, https://www.nationalartsstandards.org/
- Checks run (Python, 2026-10-29): G5 783.99 Hz, A5 880.00 Hz, B5 987.77 Hz; 40 cents is a factor of 1.0234 (B5 sharp is 1010.85 Hz); Hot Cross Buns at 88 is 10.91 s (13.64 s with the count-in), Au Clair de la Lune at 96 is 20.0 s (22.5 s), both under 30 s; 150 ms late is 0.22 beat at 88; bar 3 at 115% speed takes 2.37 s instead of 2.73 s. Contrast ratios with the WCAG 2.1 formula.

## Done when
1. Focus: at 1366x768, 680x425 and 375 wide all four players, the bar strip and `Play take` are on screen without scrolling; with Score view on, the room still shows every player.
2. Each scripted problem is audible in its take and visible in Score view at its player and bar.
3. A right note to the right player and bar removes exactly that problem; a vague card, a wrong player or a wrong bar leaves the next take identical (a test compares the two event lists).
4. Each scripted piece can be cleaned in 4 takes; `New rehearsal` always draws three solvable problems.
5. While a take plays, Stop, Solo, Loop bar and Score view act within 150 ms, and no voice line plays over the music.
6. Concert: the curtain opens only after all four manners moments are met; Play with them scrolls in time at 96 and at 80.
7. Then and now plays take 1 and the last take of each piece.
8. How lines are spoken once in a run of five takes; fixed and noChange are spoken after every take they fit.
9. Nothing is recorded or listened to; nothing but notes and problem lists is stored.

## Open questions
- None for Cory.
