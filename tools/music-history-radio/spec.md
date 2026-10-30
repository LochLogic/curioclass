# Music History Radio

## One idea
One tune, eleven eras: an original melody written for Curio Class comes through every station on an old radio dial re-arranged by that era's rules, so what changed from chant to hip hop (texture, rhythm, harmony, instruments, and how music traveled) is something you hear against a melody you already know.

## Not like
- art-through-time (9-12, wave 1): a walnut timeline of paintings you place by style. Here nothing is placed by default; you tune, listen and compare, and the thing that stays fixed is the tune.
- world-music-map (6-8, this group): music across places, tunings and cycles. This tool is one tradition's line through time, plus the American popular styles that grew from it and from African American music.
- song-form-builder (3-5, this group): form inside one song. Here the form never changes; the style does.
- orchestra-zoo, marching-band (built): instrument families and marching. Instruments here are era markers, not the lesson.
- beat-lab (9-12, built): you make the beat. Here the Mixing desk swaps whole eras' rules, not notes.
- sound-studio (grade 11 science): waves and frequency. This tool has no physics.

## Who and how
- Grade 9-12, music, module "Music History (Music)".
- Topic line: music history from chant to hip hop
- Driver: students with headphones, or the teacher on a projector. 15 to 30 minutes.
- Standards: NCAS MU:Re7 (how context shapes music and response), MU:Cn11 (relate music to its history and culture).
- Header: title, topic line, modes **Dial** (default), **Mixing desk**, **Mystery station**, then kit `motion`, `sound`, `read`. Link `kit:curio` then `kit:theme-912`.

## Screens and modes

### The radio (shared)
- The radio is a painted 1940s tabletop set (Art): dark bakelite body, a wide blank cream dial window and grille cloth. In code over the blank window: eleven station marks evenly spaced, the year printed under each, and a red needle. Painted knob cutouts sit on the body: the big tuning knob (it turns as the dial moves) and a smaller volume knob (the same image, smaller). A round "tuning eye" in code glows green and closes its gap when a station is locked. The radio sits on the painted living-room table backdrop (Art).
- Above the dial, a thin **true-time strip** from 800 to 2000 drawn to scale with a pin for each station; the pin of the tuned station is lit and is the only one with its year label. It shows how crowded the 1900s are compared with the 800 years before (at 300 px wide the 1978 and 1987 pins sit 2.2 px apart, so pins are 2 px ticks).
- Beside the radio, the **feature panel**: the station's painted postcard (Art; 4:3, about 160 px wide at 1366x768), station name and year, then five rows (Texture, Rhythm, Harmony, Instruments, How it traveled), each one sentence. A row that changed from the previous station gets a small "changed" tag.
- Under the panel, a **notation strip**: the first four bars of the tune as written for that era (neumes for chant; square notes for organum; modern staff from Renaissance on; a lead sheet with chord symbols from ragtime on; for hip hop a grid of pads). Drawn in code, simplified, labeled "how it might be written".

### Dial (default)
- Focus: the radio, the biggest thing on the stage, with the dial window across its middle; the feature panel is second.
- Drag the knob or needle, or use **◀ Station** and **Station ▶**. Between stations you hear static mixed with the nearest station by signal strength: strength = 1 minus (distance from the mark divided by half the gap between marks); locked when the needle is within 15% of the gap from a mark (strength 0.7 or more; the tool's own choice). The music plays 8 bars, then loops after a two-beat gap.
- **Compare**: pins the current station as A; tune to a different station B and **Flip** turns on; Flip switches between A and B at the next bar line. **Compare** again clears A.

### Mixing desk
- Focus: the three knobs, the radio's painted knob cutout (Art) three times in a row on a code panel under the radio, each with its era name in code; the radio stays above them.
- **Beat** (tempo, meter, rhythm feel and drums), **Harmony** (chords and voicing rules), **Sound** (instruments, texture and room), each set to any era. Starts on Baroque, Baroque, Baroque.
- The feature panel shows which era each row comes from ("Rhythm: disco. Harmony: Baroque. Instruments: ragtime."); the postcard shows the Sound knob's era. A **Random mix** button and a **Reset** button.
- Rules for mixes: chant Beat means free rhythm (no drums); chant Harmony means the melody alone (or a drone if Sound is organum); hip hop Sound with a non-hip-hop Beat still loops bars 1 and 2 as a sample.

### Mystery station
- Focus: the true-time strip, enlarged to the full stage width above the covered radio; the pin is dragged there.
- A set of six rounds, each a different station picked at random. The dial, postcard and panel are covered; the station plays. Drag the pin onto the true-time strip (or use the arrow keys, 10 years a step) and press **Tune in**. The cover lifts, the gap in years is shown ("You said 1840. It was 1900, 60 years off."), and the panel highlights the two rows that gave it away (set per station in Content). **Next station** starts the next round.
- After six: "Set done. Within 50 years: 4 of 6." and **New set**. A count only; nothing saved.

## Content

### The tune: "The Traveler" (original, written for Curio Class)
4/4, 8 bars, quarter notes unless marked (h half, dh dotted half). Scale degrees in C major pentatonic (1 C, 2 D, 3 E, 5 G, 6 A, 8 high C).

| Bar | Notes | Chord |
|---|---|---|
| 1 | 1 2 3 5 | C |
| 2 | 6 5 3h | Am |
| 3 | 3 5 3 2 | Em |
| 4 | 2dh, rest | G |
| 5 | 1 2 3 5 | C |
| 6 | 6 8 6 5 | F |
| 7 | 5 3 2h | G |
| 8 | 1dh, rest | C |

### Stations (year: arrangement; feature rows; Mystery giveaways)
1. **Chant, about 900.** Same degrees on D Dorian (D E F A B high D), one line sung on "ah" by a male choir in unison, free rhythm (each note 0.4 to 0.9 s, longer at phrase ends), long church reverb. Texture: one melody, no harmony (monophony). Rhythm: follows the words, no beat. Harmony: none. Instruments: voices only. How it traveled: memorized and sung; neumes (marks above the words) reminded singers of the shape; Guido of Arezzo's staff lines came about 1025. Giveaways: Texture, Rhythm.
2. **Organum, about 1200 (Notre Dame, Paris).** A low voice holds D under tune bars 1 to 3 and A under bar 4 (then the same for bars 5 to 8, ending on D) while the tune moves above in long-short pairs (rhythmic mode 1: half then quarter in 3/4). The tune's quarter notes pair up as long, short; each half or dotted half becomes one full 3/4 bar; so tune bars 4 and 8 take one 3/4 bar, the others two, 14 bars in all, and each tune bar keeps its own held note. Texture: a held voice under a moving one. Rhythm: repeating long-short patterns. Harmony: open fifths and octaves. Instruments: voices. How it traveled: written in manuscripts for the cathedral; Perotin's four-voice Viderunt omnes was sung at Christmas 1198. Giveaways: Harmony, Texture.
3. **Renaissance, about 1500.** Recorder consort (four voices). Bars 1 and 2: the tenor imitates the first four notes an octave lower two beats later; bars 3 to 8: four voices in chords; a 4-3 suspension in bar 7 (C held over G, falling to B). Texture: voices imitate, then move together. Rhythm: gentle, steady. Harmony: full triads, careful dissonance. Instruments: recorders. How it traveled: printed music; Petrucci's Odhecaton (Venice, 1501) was the first book of part music printed with movable type. Giveaways: Texture, Instruments.
4. **Baroque, about 1720.** Harpsichord plays the tune; cello plus harpsichord left hand play continuo, a steady eighth-note bass on the chord roots in octaves; trills on the long notes in bars 4 and 7; bars 5 to 8 repeat softly as an echo (terraced dynamics: loud, then suddenly soft). Texture: tune over a busy bass line. Rhythm: driving and steady. Harmony: chords built on the bass. Instruments: harpsichord, cello. How it traveled: written for courts and churches, sold as printed parts; Bach's Brandenburg Concertos are dated 1721. Giveaways: Instruments, Rhythm.
5. **Classical, about 1785.** Fortepiano: tune in the right hand, Alberti bass in the left (root, fifth, third, fifth as eighths), gradual crescendo through bars 5 and 6, light ending. Texture: clear tune and accompaniment. Rhythm: balanced four-bar phrases. Harmony: simple I, IV, V. Instruments: early piano. How it traveled: public concerts and printed sonatas for home players; Mozart's easy sonata K. 545 (1788) uses this bass. Giveaways: Texture, Harmony.
6. **Romantic, about 1850.** Concert grand: wide broken chords spanning two octaves in the left hand; rubato (slow down 25% into bars 4 and 8, push 10% faster through bars 5 and 6); bar 3 becomes A7, bar 4 D7 then G7 with a fermata, bar 2 Am7; big swell to bar 6. Texture: rich, singing tune. Rhythm: flexible time. Harmony: colorful chromatic chords. Instruments: full grand piano. How it traveled: pianos in middle-class homes; the one-piece cast iron frame (Babcock, 1825) made bigger, louder pianos possible. Giveaways: Rhythm, Harmony.
7. **Ragtime, about 1900.** Upright piano slightly out of tune (two voices 8 cents apart); left hand stride (low root on beats 1 and 3, chord on 2 and 4); right-hand notes moved to eighth positions 1, 2, 4 and 6 of each bar so they land off the beat (syncopation), a held note lasts to the bar's end. Texture: tune over oom-pah. Rhythm: syncopated over a steady march beat. Harmony: I, IV, V with passing chords. Instruments: upright piano. How it traveled: sheet music for home pianos and player-piano rolls; Scott Joplin's Maple Leaf Rag (1899) sold widely. Ragtime grew from African American music. Giveaways: Rhythm, Instruments.
8. **Swing, about 1938.** Big band at 150 bpm with swung eighths (long-short, 2:1); walking bass (a quarter-note line through the chord); ride cymbal and hi-hat closing on 2 and 4; brass stabs on the "and" of 2 in bars 2, 4 and 6; chords become C6, Am7, Em7, G7, F6; the 3 in bars 1 and 5 scoops up from E flat (a blue note). Texture: sections answering each other. Rhythm: swing. Harmony: sixth and seventh chords. Instruments: brass, saxes, rhythm section. How it traveled: 78 rpm records, radio broadcasts and dance halls; Benny Goodman's 1938 Carnegie Hall concert, with arrangements by Fletcher Henderson and an integrated band. Swing comes from African American jazz. Giveaways: Rhythm, Instruments.
9. **Rock and roll, about 1956.** Backbeat (snare on 2 and 4), boogie bass in eighths (root, root, 3, 3, 5, 5, 6, 6), chords C F C G C F G C, the tune on an overdriven electric guitar, short slap-back echo. Texture: small band, loud guitar. Rhythm: strong backbeat. Harmony: three chords. Instruments: electric guitar, bass, drums. How it traveled: 45 rpm singles (RCA, 1949), jukeboxes and DJs on radio. Rock and roll grew from rhythm and blues, made by Black artists such as Sister Rosetta Tharpe, Chuck Berry and Little Richard. Giveaways: Rhythm, Instruments.
10. **Disco, about 1978.** 120 bpm, four on the floor (kick on every beat), open hi-hat on the offbeats, octave-jumping synth bass, string pad, tune on a synth lead; original chords as sevenths. Texture: layered dance groove. Rhythm: steady pulse for dancing. Harmony: seventh chords. Instruments: drums, synth, strings. How it traveled: DJs in clubs and 12-inch singles made for dancing, from New York's Black, Latino and gay club scenes. Giveaways: Rhythm, How it traveled.
11. **Hip hop, about 1987.** Bars 1 and 2 of the Classical station, filtered, with record crackle and lowered bit depth, looped under all 8 bars as a sample; the tune itself plays on top as chopped notes of that same fortepiano sample, pitched to each note, so the melody still comes through; boom bap drums at 92 bpm (kick on 1 and the "and" of 2, snare on 2 and 4, swung sixteenth hats); a scratch at bars 4 and 8; no rap. A line on the panel: "An MC would rap over this beat. This station plays the beat only." Texture: loop plus drums. Rhythm: heavy, laid-back beat. Harmony: whatever the sample has. Instruments: turntables, sampler, drum machine. How it traveled: DJs at Bronx block parties (DJ Kool Herc, 1973), mixtapes, then records and radio. Hip hop was created by Black and Latino youth in the Bronx. Giveaways: Instruments, Texture.

### Sound recipes (synthesized, no samples)
Built on the kit sounds (see Family engine). Choir "ah": two detuned saws through band-pass filters at 700 and 1100 Hz with 5 Hz vibrato. Recorder: sine plus a little breath noise. Harpsichord: bright `pluck`, fast decay. Cello and organum voice: filtered saw with slow attack. Fortepiano: melody-maker's piano, shorter decay. Grand: piano with longer decay and two detuned partials. Brass: saw with a filter that opens on each note. Electric guitar: saw through a WaveShaper. Synth bass: square; pad: three detuned saws. Drums: beat-buddies `SND`. Crackle: sparse noise clicks. Rooms: convolver with generated noise impulses (church 4 s, hall 2 s, room 0.6 s, dry).

## Interactions in detail
- Tuning plays nothing until **Power** (a code button with a lamp, on the radio body) is pressed once (audio needs a gesture); Power then stays on. A locked station starts at bar 1 at once; the first time a station is heard, its ident is spoken over bar 1 with the music ducked to 40% and brought back up when the line ends. Nothing waits for the voice.
- Static level follows the needle every frame; turning fast sweeps the static like a real dial. With Motion off, the needle jumps station to station and static plays for 300 ms.
- Everything stays live while music plays: a drag, Station button or key moves the needle in the same frame, Space stops at once, and a new lock restarts at bar 1. Only Compare's Flip and the Mixing desk knobs wait for the next bar line, so the tune stays in step; the knob itself turns at once and its new era shows on the panel at once, marked "next bar".
- Compare flips between A and B at the next bar line (both tempos are shown).
- Keyboard: ◀ and ▶ change station, Space plays or pauses, C pins Compare, F flips, M opens the Mixing desk; knobs are sliders with arrow keys; all controls are reachable by Tab.
- Read: feature rows are read in order after the ident when Read is on.
- Loop lengths (8 bars plus the two-beat gap): swing 13.6 s, disco 17.0 s, hip hop 22.2 s, chant 10 to 24 s; every station loops in under 30 s and plays until stopped, because it is a radio.
- Sizes: at 1366x768 the radio, true-time strip and feature panel are visible without scrolling, the radio the largest; at 680x425 the radio and panel fit with text at least 11 px and the postcard hides; at 760 and 375 wide the panel moves under the radio and the dial scrolls sideways inside its window.

## Look
- Accent (`--brand`) #4fd18b, the green of the radio's magic tuning eye, on dark bakelite (changed from #ff5a5f "on air" red, which sat beside storyboard-studio's #ff6b6b tally red): background #1b1916, panel #26231f, ink #f1ead8, muted #b3a993; code over the painted dial window: dial text #2b2418 and needle #b8232b on cream #f3e3b5 (the window is painted to match; a cream fill sits under the text so contrast holds); tuning eye #4fd18b; dial lamp glow #f2a93b.
- Contrast (rechecked in Python): brand on background 9.04:1, on panel 8.06:1; buttons use dark text #1b1916 on brand 9.04:1; ink 14.62:1; muted 7.53:1 (6.71:1 on panel); dial text on cream 12.03:1; needle on cream 4.97:1; tuning eye 9.04:1 (the same green; a non-text mark that also changes shape, never color alone).
- 9-12 theme base with these colors on `:root`. Minimal celebration: the tuning eye closes when a station locks; nothing else.
- Different from art-through-time (walnut and burgundy), world-music-map (plum on paper), band-practice (cyan on near-black), theory-gym (blue on maple), song-form-builder (teal on light), sound-studio (green), beat-lab (orange on black), storyboard-studio (tally red on screening-room dark), gallery-critique (pink), virtual-gallery (lime on white walls).

## Art
Local FLUX (`scripts/localart.py`), no people. 14 images, none for Gemini. Rooms and objects are painted; the dial marks, needle, tuning eye, true-time strip, notation strips, pads and feature rows are drawn in code.
- mhr-radio: "A 1940s tabletop radio seen straight on, dark brown bakelite body with rounded top corners, a wide blank cream glass dial window across the middle, a woven tan grille cloth panel above it, two empty round knob sockets below the window, warm lamp light, painterly realism, plain white background"; 16:10; cutout yes; people no; the radio in every mode; dial marks, years, needle, eye and Power are drawn over it in code.
- mhr-knob: "A round dark brown bakelite radio knob seen straight on from the front, a ridged grip around its edge, one small cream pointer line, painterly realism, plain white background"; 1:1; cutout yes; people no; the tuning and volume knobs (rotated in code) and the three Mixing desk knobs.
- mhr-room: "A cozy 1940s living room corner at evening, a polished walnut side table across the foreground with an empty top, a fringed lamp glowing warm amber, patterned wallpaper softly out of focus, painterly realism"; 16:9; cutout no; people no; the stage backdrop, the radio standing on the table.
- Station postcards, 11 images, shared prompt "<scene>, vintage travel postcard painting, warm muted colors, soft light, an empty, quiet place"; 4:3; cutout no; people no; the top of the feature panel, covered in Mystery. Scenes:
  - mhr-pc-chant: a candlelit stone monastery cloister with round arches and an empty wooden lectern holding a large closed book.
  - mhr-pc-organum: the soaring Gothic stone interior of Notre Dame cathedral in Paris, tall pointed arches and colored light from a rose window over an empty stone floor.
  - mhr-pc-renaissance: four wooden recorders of different sizes lying on a dark green cloth beside a closed leather-bound book.
  - mhr-pc-baroque: an ornate painted harpsichord with its lid raised and a cello leaning beside it in a palace room with gilded walls and tall windows.
  - mhr-pc-classical: an elegant early wooden fortepiano with slim legs in a pale Viennese salon, a candelabra on top.
  - mhr-pc-romantic: a large black grand piano in a Victorian parlor, lace curtains, a vase of flowers, gaslight glow.
  - mhr-pc-ragtime: an upright piano in a parlor corner around 1900, a stack of sheet music with plain blank covers on top, a player piano roll in an open box.
  - mhr-pc-swing: an empty 1930s ballroom bandstand with gleaming trumpets, trombones and saxophones resting on stands, art deco lights over a polished dance floor.
  - mhr-pc-rocknroll: a glowing chrome 1950s jukebox with colored light tubes and a blank front panel, in a diner beside a red vinyl booth.
  - mhr-pc-disco: a mirror ball throwing spots of light over an empty dance floor of glowing colored squares in a 1970s club.
  - mhr-pc-hiphop: two turntables and a drum machine on a folding table at an outdoor city block party at dusk, brick apartment buildings and a tall speaker stack behind.

## Voice
Bank voice: `news-reader` (a broadcaster's read for station idents; unused by any neighbor or other spec in this batch). Style from the bank. Uses `Curio.voice`, scope = mode.
- welcome (how; first Dial entry; stale once a station locks): "Press Power, then drag the tuning knob or tap Station to find a station."
- ident, one per station (how; the first time that station locks; spoken over bar 1 with the music ducked; stale when the dial leaves that station): "You're tuned to 900. Plainchant." / "1200. Notre Dame organum." / "1500. The Renaissance." / "1720. The Baroque." / "1785. The Classical era." / "1850. The Romantic era." / "1900. Ragtime." / "1938. Swing." / "1956. Rock and roll." / "1978. Disco." / "1987. Hip hop." After the first time each is shown, not spoken.
- compareHow (how; first Compare press; stale once a second station locks): "Station A is pinned. Now turn the dial to a second station."
- flipHow (how; the first time Flip turns on; stale when Flip is pressed): "Press Flip to switch between the two stations at the next bar."
- deskHow (how; first Mixing desk entry; stale once a knob turns): "Turn the Beat, Harmony or Sound knob to another era. The change starts at the next bar."
- mysteryHow (how; first Mystery round; stale once the pin moves): "Listen, then drag the pin to the year you hear and press Tune in."
- mysteryResult (event; every Tune in; stale when Next station is pressed): "It was" plus the year and era ("It was 1900. Ragtime."); the gap in years is on screen only.
- setDone (event; every finished set; stale on New set): "Set done. Your count is on the screen."
- Only idents and mysteryResult are spoken while music plays, over ducked music; the how lines play over the static or before Power.

## Family engine
none. The tool borrows sounds and timing from built tools: melody-maker's `pluck` piano recipe and `freq`, beat-buddies' `audio()` chain, `SND` drums and `startClock` lookahead scheduler (25 ms timer, 0.15 s horizon), extended with swing (delay every second eighth to 2/3 of the beat) and rubato (a per-bar tempo curve). Once `kit/music-studio.js` and `kit/rhythm.js` exist (specified in song-form-builder and band-practice), use them instead of copies.

## Sources
- National Core Arts Standards, Music MU:Re7, MU:Cn11: https://www.nationalartsstandards.org/
- Chant, neumes and Guido of Arezzo's staff (about 1025): Britannica, "Gregorian chant" and "Guido d'Arezzo", https://www.britannica.com/art/Gregorian-chant
- Notre Dame organum, rhythmic modes, Perotin's Viderunt omnes (1198): Britannica, "Organum" and "Perotin", https://www.britannica.com/art/organum
- Petrucci's Odhecaton (1501), first part music printed from movable type: Britannica, "Ottaviano dei Petrucci"; Library of Congress Music Division.
- Basso continuo and terraced dynamics; Brandenburg Concertos (1721): Britannica, "Baroque music" and "Brandenburg Concertos".
- Alberti bass (named for Domenico Alberti); Mozart Sonata K. 545 (1788): Britannica, "Alberti bass", https://www.britannica.com/art/Alberti-bass
- Rubato and the iron-framed piano (Alpheus Babcock, 1825): Britannica, "Piano"; Smithsonian National Museum of American History.
- Ragtime, Scott Joplin, Maple Leaf Rag (1899), sheet music and piano rolls: Library of Congress, "Ragtime" collection, https://www.loc.gov/collections/ragtime/
- Swing, Goodman's Carnegie Hall concert (January 16, 1938), Fletcher Henderson's arrangements: Smithsonian National Museum of African American History and Culture, https://nmaahc.si.edu/; Britannica, "Swing".
- Rock and roll roots in rhythm and blues; Sister Rosetta Tharpe, Chuck Berry, Little Richard; RCA 45 rpm single (1949): NMAAHC; Britannica, "Rock and roll".
- Disco, 12-inch single, New York club scenes: Britannica, "Disco".
- Hip hop origins, DJ Kool Herc's 1973 Bronx party, sampling and boom bap: NMAAHC; Smithsonian Anthology of Hip-Hop and Rap (Smithsonian Folkways, 2021), https://folkways.si.edu/
- "The Traveler" and every arrangement: written for Curio Class; the styles are general practice, no copyrighted melody or recording is used.
- Number checks (Python, 2026-10-29): every tune bar sums to 4 beats (bars 4 and 8 with a one-beat rest); beats 1 and 3 of every bar are chord tones; 24 notes. Organum: the old "half then quarter in 3/4" did not say how 8 bars of 4/4 map; long-short pairing gives 14 bars of 3/4 (2, 2, 2, 1, 2, 2, 2, 1), now written in. Hip hop: the old station looped only bars 1 and 2, so bars 3 to 8 of the tune never sounded and Done when 1 could not pass; the chopped-sample melody fixes it. Signal strength: 1.0 at a mark, 0.7 at the 15% lock edge, 0 at the midpoint. Loops: swing 13.6 s, disco 17.0 s, hip hop 22.2 s, chant 9.6 to 23.6 s plus the gap. True-time strip: the 1978 and 1987 pins are 2.2 px apart at 300 px and 6.8 px at 900 px, so pins are thin ticks with one label. Mixing desk: 11 cubed is 1331 combinations. Contrast ratios in Look recomputed.

## Done when
1. All eleven stations play "The Traveler" recognizably (same contour, all 8 bars, hip hop included) with the arrangement rules above, each checked by ear against its feature rows.
2. Static mixes by signal strength between marks; the tuning eye closes only when locked (within 15% of the gap).
3. Compare flips at the bar line and both stay in step; Flip is off until a second station is tuned.
4. Mixing desk: all 1331 Beat, Harmony and Sound combinations play without errors (checked by script); the panel names each row's era.
5. Mystery: six rounds, the gap in years and the two giveaway rows show; the count is correct; New set starts over; nothing is stored.
6. Focus: the radio is the largest thing in Dial and Mixing desk at 1366x768 and 680x425; the strip spans the stage in Mystery.
7. A tap while music plays: dragging the knob, a Station button or Space changes what is heard in the same frame; only Flip and the desk knobs wait for the bar line, and their new era shows on screen at once.
8. Idents are spoken once per station over ducked music, never delaying it, then shown only; how lines once each; no line names Flip while it is off.
9. Radio, strip and panel visible without scrolling at 1366x768 and 1280x720; preview readable at 680x425; no sideways page scroll at 375.
10. All 14 images load and none shows a person or fake lettering.

## Open questions
- The stations follow European concert music to 1850, then American popular styles. World-music-map covers other places, so this tool keeps that line. Is that the arc you want, or should a station from outside it (for example West African drumming as a root of the American stations) be added?
