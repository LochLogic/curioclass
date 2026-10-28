# Family: music studio

Four tools, grade 3 to 12 (music), share one sound engine: `kit/music-studio.js`, inlined with
`<script src="kit:music-studio"></script>` after `kit:curio`. The engine was first written by song-form-builder
(2026-10-28, version 1.0; 1.1 after its Refine round 1); this file is its reference. `MS.version` says which. Every function below exists in the engine and works as written.

## What the engine does (shared)

Pitch tables, four synthesized instruments and a clock that plays a list of notes on the audio clock, with a callback
per beat for a playhead. One global, `MS`. No network requests, no audio files, no dependencies. The sound parts are
lifted unchanged in sound from melody-maker's `src.html`; `MS.play` is new (the lookahead pattern of beat-buddies'
`startClock`: a 25 ms timer, a 150 ms horizon).

### Pitch

```js
MS.KEYS        // {C, D, F, G}: {semi (do above middle C), letter (C = 0 ... B = 6), sig (['F♯']), name}
MS.SCALES      // {major, penta, minor}: {name, home ('do' or 'la'), rows: [[semi above do, syllable, degree], ...]}
               //   penta rows: do re mi sol la do (high); minor starts on la below do (semi -3)
MS.COL         // syllable colors {do, re, mi, fa, sol, la, ti}: the common classroom bell colors
MS.freq(key, semi)          // Hz of the note `semi` semitones above do in `key`; do of C is middle C, 261.63 Hz
MS.rowSemi(scale, row)      // a scale row as semitones above do
MS.rowSyl(scale, row)       // and its syllable
MS.semi(name)               // a note name to semitones above middle C: 'C' 0, 'E' 4, 'G3' -5, 'C5' 12, 'F#4' 6, 'Bb' 10
                            //   (octave 4 when left out; # b ♯ ♭ all work; throws on anything else)
MS.LEN         // lengths in beats: s .25, e .5, de .75, q 1, dq 1.5, h 2, dh 3, w 4
```

### Writing notes

```js
MS.parse('E D C:h | C:e C:e - D', {scale})   // -> {events: [{beat, semi, dur}], beats}
MS.rows([0, 1, 2, null, 3], {scale, start, instr})   // scale-row numbers, one per beat -> events (with .beats)
```

`parse` reads note names: a token is a note name or `-` (a rest), then optionally `:` and a length (a `LEN` key or a
number of beats; default 1). `|` bar lines are ignored. `scale` multiplies every length (0.5 writes a 6/8 tune with an
eighth as 1). Rests leave a gap; `beats` is the total length. `rows` turns grid rows (null, undefined or `'-'` is a
rest) into one-beat events starting at `start` (default 0) in `scale` (default `'penta'`), each tagged with `instr`.
The list it returns also carries `.beats` (`start` plus the number of rows), so `MS.play` gives trailing rests and an
all-rest grid their time. Each note is one beat long: a tool with held notes builds its events itself.

### Sound

```js
MS.ctx()                    // the shared AudioContext, made on first use (call after a tap); resumes it; null if none
                            // (its own context, separate from the kit's Curio.audio)
MS.INSTR                    // {marimba, flute, piano, box}: {name (with an emoji), play(f, t, durSeconds, bus)}
MS.note(instr, key, semi, at = 0, dur = .4)   // one note now (or `at` s from now), dur in seconds
MS.pluck(f, t, decay, {gain, partials: [[ratio, level]], type, cutoff}, bus?)   // the plucked voice (marimba, piano, box);
                            //   t is on the audio clock (MS.ctx().currentTime)
MS.blow(f, t, d, bus?)      // the breathy voice with vibrato (flute)
MS.tick(t, bus?, accent?)   // a short wood click (the lead-in)
MS.chime(good)              // a rising arpeggio (true) or two falling notes (false)
```

Everything goes through one master gain (0.8) and a short room delay (130 ms, feedback 0.28, wet 0.22, lowpass
2400 Hz). `bus` is `{m, r}` (the dry and room sends) and defaults to the shared master and room. While the kit's
Sound button is off (`Curio.sound` false) every one of these is silent: `note`, `chime`, `pluck`, `blow`, `tick` and
every scheduled note. All of them make the context themselves when needed, so none fails before the first `ctx()`.

### The clock

```js
const p = MS.play(events, {bpm: 100, lead: 0, key: 'C', instr: 'marimba', beats, exclusive: true,   // the defaults
  onStep: (i, info) => {},   // once per whole beat, in step with the sound; i < 0 during the lead-in;
                             //   info {beat, events (those starting in that beat)}
  onEnd: why => {}});        // 'end' after the last beat, or 'stop'
p.stop(); p.done /* promise of 'end' or 'stop' */; p.playing; p.bpm = 120; p.beat /* current, fractional */
MS.stop(); MS.playing
```

- `events` are `[{beat, semi, dur, instr}]`, with `beat` and `dur` in beats (fractions allowed) and `instr` defaulting
  to `opts.instr`, then marimba. `semi` is above do of `key`. The `{events, beats}` that `MS.parse` returns can be
  passed as it is.
- `lead` lead-in ticks sound before beat 0 (the first one accented); the default is 0, no lead-in.
- `beats` sets the length. When it is left out, the length is the list's own `.beats` (from `MS.rows` or `MS.parse`),
  else the end of the last event. A tool that joins several grids into one list loses `.beats`, so it passes `beats`
  itself (song-form-builder passes 8 per block): otherwise trailing rests and all-rest blocks get no time. Events at
  or after `beats` are not played.
- Setting `p.bpm` changes the tempo from now on, without a jump in the playhead (notes already inside the 150 ms
  horizon keep their times).
- Each player has its own gain bus, so `stop()` fades out (50 ms) even the notes already scheduled. A finished player
  lets its last notes ring.
- `exclusive` (default true) stops every running player first. With `exclusive: false` the new player runs alongside
  the others (layers). `MS.stop()` stops every running player, and `MS.playing` is true while any is running.
- The clock: when Sound is on and the audio context is running at the start, the play runs on the audio clock
  (`currentTime`), so callbacks stay in step with the sound. Otherwise (Sound off, no audio, or a context still
  suspended, for example a play started before any tap) it runs on the page clock and stays silent for that whole
  play, so a playhead never stalls. Turning Sound on mid-play takes effect from the next play.
- `MS.version` is the engine's version string ('1.1').

### Look

The engine draws nothing. Each tool draws its own grid, blocks and playhead. `MS.COL` is there for tools that color
notes by syllable (melody-maker); always write the syllable on the note too, so color is never the only signal.

## Sound rules (all siblings)

- No sound before a tap: browsers block it, and `MS.ctx()` is made on the first sound call.
- Respect the kit's Sound button: the engine already does; a tool's own extra sounds check `Curio.sound`.
- Never narrate over music: the tool hushes voice lines when play starts (`V.hush()`) and queues its result line for
  after `onEnd`; Read stops play first.
- Songs come from the public domain or are written for Curio Class, with a source in the spec. Music from a living
  culture or a Native tradition gets a sensitivity review before it ships.
- Nothing a student composes leaves the browser (localStorage at most).

## What each tool brings (its own)

| Tool | Grade | Its one idea (not shared) | Uses the engine |
|---|---|---|---|
| melody-maker | 3-5 | compose one 16-beat tune on a solfege grid, colored by syllable | keeps its own copy until it is next reworked (KIT.md); then `INSTR`, `SCALES`, `COL`, `play` |
| song-form-builder | 3-5 | sections as letters: change one A and every A changes; name AB, ABA, AABA and rondo; label six real songs by ear | `rows` (8 pentatonic rows in C), `parse` (the Listen songs as note names), `play` with `lead: 1`, live `bpm`, per-section `instr` |
| chord-explorer | 6-8 | harmony and cadences | keeps its own copy until it is next reworked |
| beat-lab | 9-12 | patterns A to H arranged into a produced track | keeps its own copy until it is next reworked |

Borrowers outside the family: music-history-radio's spec says to use this engine once it exists, instead of copying
melody-maker's `pluck` and `freq`.

## Rules for siblings

- Pitch, instruments and timing come from the engine. A sibling adds its own grid, scene and questions.
- New engine features go into the engine and this file in the same change, keeping existing calls working. Drums,
  swing and chords are not in the engine yet: the first tool that needs them adds them here (band-practice's spec names
  a separate `kit/rhythm.js` for drums).
- No two siblings use the same song as their main material without a reason in the spec.
