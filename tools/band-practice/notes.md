## What it teaches

Students perform one part of an ensemble, evaluate their timing, and change how they listen and rehearse. They can distinguish early from late taps and test whether they hold a tempo when accompaniment disappears.

## Key skills

- Listen to other parts while keeping your own rhythm.
- Read a one-bar rhythm and perform it without automatic correction.
- Use timing evidence to choose what to practice next.
- Keep a steady pulse through silence and rejoin an ensemble.

## Support at home

- Clap a steady beat together. Have one person stop for four counts, then come back together.
- Take turns tapping a simple pattern while the other keeps a pulse on a table.
- Listen to a familiar song and name which instrument helps you keep time.

## Five-minute start

Use headphones. Pick Drums in Hallway Funk, press Play, and calibrate or Skip. Listen to the one-bar count-in, then tap Space on beats 2 and 4. Press Stop, inspect the trace, and try again while listening especially to the bass.

## Modes

Rehearse loops the eight-bar progression until Stop. Part, Speed, Song, and Who you hear change immediately. A divider marks a new take when the listening conditions change. The trace retains earlier dots; the summary describes the newest take.

Solo break is twelve bars: four with the band, four with only your own taps, then four with the band again. Its summary estimates drift in milliseconds per bar and tempo in beats a minute. A sparse part or uneven performance may not establish a trend.

Ghost race locks the song's original tempo for eight bars. Bests are saved separately by song and part on this device. The score averages absolute timing errors, counting every missed note as 150 milliseconds. Finish the race to save a ghost. Extras are listed separately and do not enter that specified score.

After Solo break, the stage desk shows drift, estimated tempo and the landing beside the pad. After Ghost race, it shows the race error including missed-note penalties, the previous ghost and whether a new best was saved. Changing Song, Part or Speed while stopped clears the old take so its evidence is never relabeled as the new setup.

## Talk questions

- Which part helped you keep time? What changed when you muted it?
- Did your break trend match what you felt while playing?
- What would you change for your next take, and what evidence supports that choice?
- Could a take have a low timing error and still leave holes in the music?

## Good to know

The tool synthesizes all music locally, using the audio clock. Your part is removed from the band, so your taps supply it and missed notes leave holes. There is no microphone recording. Calibration and ghost records stay in localStorage on this device; Clear bests and Reset calibration remove them.

Three original eight-bar songs teach different ensemble jobs: Hallway Funk, Night Bus, and Waltz for the Rain. The part card uses sixteenth-note cells; bold numbered cells mark beats. The moving cell is a one-bar reference, not a note highway.

Positive offset means early: expected time minus corrected tap time. Negative means late. A circle is within 25 ms; a triangle points up for early and down for late. From 26 to 60 ms is "a little" early or late; larger offsets are early or late. An x means a missed note; gray ticks mark extras. These thresholds are instructional choices written for Curio Class, not universal musical standards.

Each matching window is at most 150 ms and at most half the nearest neighboring note gap. During the silent break the matching window moves by the last matched offset; the displayed offset still compares with the original band clock. Offscale dots retain their numeric error. The first tap in bar 9 has no 150 ms matching cap. A landing within 60 ms is "right with them."

In small views, crowded offscale annotations use a range and tap count so numbers do not cover the trace. Hover over the trace for the individual offscale values, which are also in its accessible description. Triangles still mark every note at the appropriate edge.

Drift uses a least-squares line through matched offsets over bars 5 to 8, or the last four rehearsal bars. At least four matched notes are needed. A trend must exceed 60 ms over four bars and the two-sided 95 percent Student t threshold before it is called rushed or dragged. A smaller trend is held steady; an unsupported larger one is too uneven to tell. Tempo is band tempo divided by the slope of tap time against expected time. The four observations from one-note-per-bar parts have limited statistical power. A very large timing change between sparse notes may also fall outside the matching window.

Calibration plays eight clicks at 100 beats a minute, 4.2 seconds from first to last. It drops the first two taps and takes the median latency of the last six. If any of those taps is more than 60 ms from the median, it keeps the previous calibration. Accepted latency is clamped to minus 50 through 300 ms. The shared `curio-tap-latency` value is stored in seconds. The default is Web Audio outputLatency, then baseLatency, then zero.

"One drop" is a reggae drum pattern leaving beat 1 empty and placing kick and snare together on beat 3. "Skank" describes short offbeat reggae chords. Night Bus uses the exact beats 2 and 4 keyboard pattern specified for this tool. A waltz has three beats to the bar, here with bass on beat 1.

## Standards and sources

MU:Pr5 is practiced by comparing takes and changing rehearsal conditions based on timing evidence. MU:Pr6 is practiced by performing an unquantized part with the ensemble and rejoining after silence.

- National Core Arts Standards, Music MU:Pr5 and MU:Pr6: https://www.nationalartsstandards.org/
- Web Audio API clock, latency, and output timestamps: https://www.w3.org/TR/webaudio/
- Reggae: https://www.britannica.com/art/reggae-music
- One drop rhythm: https://en.wikipedia.org/wiki/One_drop_rhythm
- Waltz: https://www.britannica.com/art/waltz
- Songs, timing thresholds, and teaching examples: Curio Class Band Practice specification.

Illustrations generated with OpenAI gpt-image, edited for Curio Class. No people appear in the illustrations. Voice bank: easy-coach (Umbriel); fixed lines are ready for recording and currently use the kit browser voice fallback.
