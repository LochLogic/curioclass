# song-form-builder: build handoff (2026-10-28)

## What was built

- `src.html` (about 106 KB bundled): Build and Listen modes per the spec, on the new family engine.
- `kit/music-studio.js` (new, version 1.1 after Refine round 1) and `docs/families/music-studio.md` (its reference). No existing kit file
  was changed.
- `tool.draft.json` (stage built), `notes.md`, `art/prompts.json` (no art: everything is drawn in code),
  `voice/lines.json` (bank playful-friend, voice Laomedeia, all 59 strings from `__tool.allLines()`).

### Layout

- Wide (1000 px or wider and 700 px or taller): stage left, panel right. Compact (600 px or wider, w/h at least 1.25):
  a 260 px panel (300 px from 900 px wide). Stack (below that, including 760 and 375): panel `display: contents`, in
  the order hint, Play song, Form card, then the stage, then the rest of the panel.
- The stage is laid out in real pixels per size (`relayout()` sets `--cols --bh --lf --cw --ch --sw --pad --gap`).
  In the short compact box the editor uses a tight mode (no beat numbers or tip, 1 px cell gaps); at 375 a narrow mode.
- Build stage, top to bottom: the strip (8 slots, persistent buttons updated in place), the block bar (Hear, Make it
  A′, Remove), then the shelf or the editor (6 by 8 grid, instrument select, Done).
- Panel: hint, Play song / Stop, Form card (letters, name, line, ending note, "Your B plays the A part", copies count),
  then the song select (Listen), Speed, Starter songs, Clear song with a Yes / No confirm.
- Listen: the big panel button is Listen, Stop, Hear it again (a part waits for its label) or Play whole song (the
  end). The stage holds the phrase strip, then the answers (Same as X, Almost X, Hear X per letter used; Same as X′
  and Hear X′ per labeled twin; New), then Start over, which asks Yes / No in place.

### Voice

`Curio.voice` with `hint: false`: the tool owns the hint (`H` table), and Read speaks `hintText()` with ′ read as
"prime". How lines (`welcomeBuild`, `playHow`, `editHow`, `twinHow`, `welcomeListen`) are chosen by `V.heard`, with
`valid` and `needs`; the linked line once per editor session (marked inside `valid` when it starts); form lines,
sameNotes, emptyStrip, listenWrong, reveals and song end lines are events. Play calls `V.hush()`; result lines are
queued after `onEnd` and are valid only while the strip version is unchanged. `answer()` hushes, so a stale
listenWrong never plays after the next answer.

## Engine API (kit/music-studio.js, global MS)

```
COL, SCALES {major, penta, minor}, KEYS {C, D, F, G}, LEN, INSTR {marimba, flute, piano, box}
freq(key, semi), rowSemi(scale, row), rowSyl(scale, row), semi('G3') -> -5
parse('E D C:h | -', {scale}) -> {events, beats}
rows(notes, {scale, start, instr}) -> events (with .beats)
ctx(), pluck(f, t, decay, opts, bus), blow(f, t, d, bus), note(instr, key, semi, at, dur), tick(t, bus, accent), chime(good)
play(events or {events, beats}, {bpm, lead, key, instr, beats, exclusive, onStep(i, info), onEnd(why)})
  -> {stop(), done, playing, bpm (get, set live), beat}
stop() (every player), playing (any), version '1.1'
```

Silent with Sound off (pluck, blow and tick too), but the clock and callbacks still run on the page clock. Each player has its own bus, so Stop silences notes
already scheduled. Full reference: `docs/families/music-studio.md`.

## Done when (spec)

1. A, B, A then Play song: three sections in order with the playhead; Form card says ternary. PASS.
2. One note of A changes every A (sketches and sound; slots ripple); the linked line once per edit session. PASS.
3. Every Form card rule gives its line, including BAB as ABA, AA′BA′ as AABA, ABACA as rondo (also ABABA, ABACABA,
   AABB, ABC, AAA, A A′, ABBA as no special name). PASS.
4. A twin's first 6 beats follow its parent, its last two do not (tested: locked cells don't change; parent edits
   reach the twin's beats 1 to 6 only). PASS.
5. Listen: all six songs label to their forms and end lines; a wrong label replays the compared phrase, then the
   current one. PASS.
6. How lines once in five actions in a row (playHow and editHow spoken once); form lines on every Play, dropped when
   the strip changes. PASS.
7. No line over the music (hush on play, lines after onEnd); Read stops play (tested). PASS.
8. Strip, Play song and the Form card visible without scrolling at 1366x768, 1280x720 and 680x425 (also 800x500,
   1000x625, 1920x1080, 760 and the 375 host). Targets 44 px or more everywhere, nothing clipped. PASS.

## Refine round 1 (2026-10-28)

Fixed: the blocker (rests get their time: the tool passes `beats`, and the engine defaults to the list's `.beats`),
every should-fix (2 to 11) and every accepted polish (12 to 28); also the nits for "New section C" wrapping and the
answer buttons left on screen at the end of a song. Re-checked against BUILD.md's Wave lessons (BR1). Frames
re-shot at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375 (host), in Build, the
editor, Listen mid-song (Frere Jacques, Ode to Joy with A′), the Start over question and the end of a song: targets
44 px or more, nothing clipped, no horizontal scroll, the main controls in view. Not done: the Tab order nit (Done
before the grid) and the two engine nits (one shared AudioContext with the kit, held notes in `rows`); they were not
on the accepted list.

## Deviations from the spec (on purpose)

- The shelf shows directly in compact layouts rather than behind a Shelf button: it fits.
- Listen's answer buttons sit on the stage under the strip, not in the panel: at 680x425 the panel had no room, and
  the answers belong next to the phrases. "Hear A" is written "▶ A" (aria-label "Hear A"). The spec's Hear again
  is the big panel button while a part waits ("Hear it again"); Play whole song takes that button at the end.
- A labeled twin gets its own Same as A′ and ▶ A′ buttons (Ode to Joy's part 4 is A′ again).
- Clear song (after a Yes) also puts the sections back to the first ones and removes the save.
- First load: Sunny Day's sections on the shelf with an empty strip, so the first action is building.
- Twins appear on the shelf after their parent (that is where Edit lives).
- A single block (n = 1) gives no form line (nothing to compare yet); the card asks for more blocks.
- Listen plays at a fixed 100 bpm on piano, so only the music differs between phrases.
- Listen strip slots are display only (not buttons).
- While the editor is open the strip is inert (the bar and slots are not targets), so the short compact box fits.

## Known gaps

- Keyboard: Tab reaches every control, arrows walk the strip and the grid, Delete makes a rest, Escape clears a
  pick. In the editor, Instrument and Done come before the grid in Tab order.
- Recordings are not made yet (`voice/lines.json` is ready).

## Sensitivity (rule 5)

No Native or living-culture music. The Listen songs are public domain: Hot Cross Buns (English traditional), Frere
Jacques (French traditional), Twinkle Twinkle ("Ah! vous dirai-je, maman", France, 1761), Mary Had a Little Lamb
(1830), Row Row Row Your Boat (1881), Ode to Joy (Beethoven, 1824). The starter songs were written for Curio Class.
Refine's Teaching lens checked all six note for note and closed the flag: no sensitivity review needed.

## For Cory

- The new shared engine `kit/music-studio.js` is ready for melody-maker, chord-explorer and beat-lab when they are next
  reworked; nothing existing was touched.
- One spec deviation worth a look: the Listen answer buttons live on the stage, not in the panel.
- The spec open question from Refine (an invitation to build AABA or a rondo) is left for the spec.
- Motion off: no infinite animation runs (the ripple, the playhead outline and the end-of-play lift are one-shot;
  the ripple and lift have their own calm rules).
