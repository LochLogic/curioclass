# song-form-builder: Craft lens (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/music-studio.js against
docs/families/music-studio.md, and kit/curio.js (voice). Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
song-form-builder` (104,896 bytes). Driven with `scripts/drive.py` (held clicks, 0.12 s), ports 9940 and 9942, the 375
host on 9941 (`--host`). Frames and logs in the lens scratch folder `lens-sfb-craft2/out` (sizes, h375, eng, focus,
calm, voice, voice2, voice3, vis, lans).

Counts: blockers 1, should fix 5, polish 4, nits 4.

## Contract

- One file, 104,896 bytes (well under 2 MB). Kit used: `Curio.voice`, `Curio.init`, the kit frame CSS, and
  `MS` from kit/music-studio.js; nothing re-implemented.
- No network requests: `performance.getEntriesByType('resource')` is empty after Play song, Listen and a phrase; the
  bundle has no fetch, XHR or URL loads.
- No console errors, warnings or exceptions in any shot (about 70 shots at every size, both modes, engine tests). The
  only log line was the 375 host page's own favicon 404, not the tool.
- `allLines()` (53) and voice/lines.json (53) match word for word, both ways. No `art:` tokens; prompts.json has no
  assets (everything drawn in code). No em dashes in src, notes, lines or spec; "Curio" only as `Curio.voice` and
  `Curio.init` in code. Privacy line on screen: "Your song is saved on this device only. Nothing leaves it."

## Engine against docs/families/music-studio.md (line by line, tested in the page)

Exists and behaves as written: `KEYS` (C D F G with semi, letter, sig, name), `SCALES` (major, penta 0 2 4 7 9 12,
minor from la -3, homes), `COL`, `LEN` (s .25 to w 4), `freq` (C do 261.63 Hz, G do 392.00, octave 523.26),
`rowSemi`, `rowSyl`, `semi` ('C' 0, 'E' 4, 'G3' -5, 'C5' 12, 'F#4' 6, 'Bb' 10, 'Eb' 3, 'B♭3' -2, 'F♯' 6; throws on 'H'),
`parse` (lengths, numbers, rests leave gaps, `|` ignored, `scale` .5 for 6/8, `beats` total), `rows` (null, undefined
and '-' rest, `start`, `scale` default penta, `instr` tag), `INSTR` (four, emoji names), `note`, `pluck`, `blow`,
`tick`, `chime`, `ctx`, `play`, `stop`, `playing`. Sound parts match melody-maker's src.html (same partials, gains,
decays, room delay 130 ms / .28 / .22 / 2400 Hz).

`MS.play` measured at 120 bpm, lead 2, beats 5: onStep -2, -1, 0 ... 4 at 0.08, 0.59, 1.09 ... 3.09 s, each within
10 ms of its oscillator start; lead ticks accented first; onEnd('end') at 3.59 s (lead plus `beats`, so a trailing
rest keeps its time); `done` resolves 'end'; `info.events` lists events starting in the beat (a 0.5-beat event shows
in step 0). `stop()` gives 'stop' and fades the player's bus; a new exclusive play stops the old one ('stop', then
the new one playing). Live `p.bpm`: beat 1.421 before and after the change, then +1.02 beats in 0.5 s at 120. Sound
off: the clock and onStep still run (-1, 0, 1, 2, 3), zero oscillators made; `note` and `chime` silent. Empty events
with lead 1: one tick step, then 'end'. Buses disconnect 4 s after the end.

## Findings

### Blocker

1. **src.html:716 (`startPlay`), Build Play song and Hear: `beats` is never passed to `MS.play`, so all-rest and
   trailing-rest beats get no time.** `startPlay` forwards only `bpm, lead, onStep, onEnd`; the `beats: ids.length * 8`
   from Play song (line 738) and `beats: 8` from Hear (line 752) are dropped, so the engine's default (end of the last
   note) applies. Seen: Blank starter, strip A A (all rests), Play song: the song ended 0.7 s after the tap (lead-in
   only), no playhead on either block, and "The same music every time. That's how verses work." spoken at once
   (voice3 r1_blank). A then B ending in five rests at 120 bpm: the form line came at 6.2 s instead of 8.5 s, the
   playhead never reached B's last five beats (r2_restend). Hear on an all-rest shelf section ended after 0.1 s
   (f6_hear). The spec's edge case "A block with all rests plays silence for its 8 beats" is broken, and Blank is the
   path to composing from scratch. Tag **family:music-studio** (a grid sibling hits the same trap: the doc could say
   "pass `beats` for a fixed-length grid").

### Should fix

2. **src.html:665-668, the linked line is dropped when Done comes before it starts.** Its `valid` needs
   `state.ed === ed`, and Done sets `state.ed = null`. In the first editor session the line waits behind editHow, so a
   student who taps one note and presses Done within about 4 s never hears "You changed A, so every A changed" (voice
   v4: Edit 0 s, note 2.1 s, Done 4.3 s, linked "dropped stale" at 5.1 s). That first session is the moment the line
   exists for (Done when 2). Keep it valid while the strip version from that edit stands and nothing plays, not only
   while the editor is open. Tag general.
3. **src.html:581, playHow plays while a shelf block is picked.** Its `valid` checks strip, play, editor and confirm
   but not `state.sel`. Seen (voice v1): after the welcome, "Press Play song to hear your form." started at 6.0 s,
   while A was picked (5.4 s) and the hint said "Now tap a space in the song strip to put your block there." The line
   no longer matches the screen. Add `!state.sel` (and `state.slot == null`). Tag general.
4. **src.html:788, Clear song does not clear the save.** It calls `localStorage.removeItem(SAVE)` and then
   `changed(false)`, which saves again; the stored sections (every note, twins, C and D) survive a reload (focus run:
   the save after Yes still held A, B, A′, C, D). notes.md says "Clear song also clears the save" and the spec says so
   too; on a shared laptop the next student gets the last one's sections. Either clear the sections too (and say so in
   the question) or reword the notes. Tag general.
5. **src.html:163 (`.cell`), the editor's focus ring is mostly hidden.** The kit's 4 px outline at offset 3 px is
   painted under the later sibling cells (2 px gaps, 1 px in the tight preview), so only the top and left half of the
   ring shows; on the top row and left column in the 680x425 preview the container's overflow clips that half too,
   leaving a sliver (vis kbfocus_cell680, kbfocus_cell680_top). Keyboard users lose their place in the grid. An inset
   ring (`.cell:focus-visible{outline-offset:-4px}`) or `position:relative; z-index:1` on focus fixes it. Tag general.
6. **kit/music-studio.js:144, 198, 203: `MS.stop()` and `MS.playing` lose players started with `exclusive: false`.**
   `current` holds only the newest player, so after `x1 = play(...)`, `x2 = play(..., {exclusive: false})`,
   `MS.stop()` stops x2 only, and `MS.playing` is false while x1 is still playing (eng: nonExclAfterStop [true, false,
   false]). The doc says "`MS.stop()` stops the current one; `MS.playing` says if one is running", and beat-lab's
   layered patterns are the first sibling likely to use `exclusive: false`. Keep a set of live players (stop all, playing
   if any), or document that non-exclusive players must be stopped by the caller. Tag family:music-studio.

### Polish

7. **docs/families/music-studio.md, the clock block: state the defaults.** The example reads `{bpm: 100, lead: 1, key:
   'C', instr: 'piano', beats, exclusive: true, ...}`, where bpm, key and exclusive are the defaults but `lead` is 0 and
   `instr` falls back to marimba (eng: defaultLeadSteps [0, 1, 2, 3], no lead-in). A sibling copying the line as
   defaults gets the wrong idea. Say "lead (default 0)" and use the default instrument in the example. Also: `version`
   is exported but undocumented; the kit comment says `bpm` changes "from the next beat on" while the doc (and the code)
   change it from now. Tag family:music-studio.
8. **docs/families/music-studio.md, Sound: `pluck`, `blow` and `tick` need `MS.ctx()` first and ignore Sound.** They
   use the shared context directly (TypeError before any `ctx()` call) and are not silenced by the Sound button, unlike
   `note` and `chime`. One line in the doc saves a sibling the surprise. Tag family:music-studio.
9. **kit/music-studio.js:145-146, the clock runs on the audio clock even with Sound off, and stalls while the context
   is suspended.** The doc says that with Sound off "the clock and its callbacks still run on the page clock"; in fact
   `play` makes an AudioContext and runs on `currentTime` whenever one can be made. If that context is suspended (a play
   before the first tap, or the OS suspending audio), `currentTime` stands still, `pump` never schedules past the first
   150 ms and the playhead and `onEnd` hang until it resumes. Fine for this tool (every play follows a tap); worth a
   page-clock fallback when `c.state !== 'running'`, or a doc line, before a sibling runs a silent demo. Tag
   family:music-studio.
10. **src.html:435 and 123, the "rest" label in a note sketch is tiny and squashed.** It is 9 px text in an SVG drawn
   with `preserveAspectRatio="none"`, so in the 680x425 strip and shelf it renders about 5 px tall and stretched (vis
   pick680). Draw the label as HTML over the sketch at 11 px or more, or a dash pattern. Tag general.

### Nits

11. src.html:229 (`#newsec`): at 1366x768 and 1920x1080 "＋ New section C" wraps so "C" sits alone on its own line
    (sizes def_1366x768). A non-breaking space before the letter keeps it together. Tag general.
12. Listen at 375 (host): "↻ Hear again" ends 11 px below the fold while answering part 8 of Frere Jacques (lans_375);
    the Same / Almost buttons above it are in view. Tag general.
13. kit/music-studio.js:73: the engine makes its own AudioContext while the kit's `Curio.audio()` makes another; two
    contexts per page. Reusing the kit's would halve the setup. Tag family:music-studio.
14. kit/music-studio.js:61: `rows` makes one-beat notes only, so melody-maker's held notes (its `undefined` after a
    note) can't go through it when it moves to the engine; it will build events itself. A `hold` value in `rows` would
    cover it. Tag family:music-studio.

## Access

- Keyboard: Tab order is header, panel (hint, Play song, Form card, Speed, Starter songs, Clear song), shelf, strip,
  bar, editor, as the spec asks. Strip arrows move between spaces (slot 0 to slot 1). Grid arrows, Enter and Delete
  work; a locked twin beat shows the chain tip.
- Focus when controls hide or rebuild (all held, focus2 run): Remove on the last block moves focus to that empty space;
  Remove of a middle block keeps it on Remove; Remove of the only block goes to space 1; Make it A′ goes to Edit on
  the A′ shelf block; Edit goes to the grid; Done returns to that block's Edit; Escape with focus on Hear goes to the
  space; the fourth section (D) moves focus to its block as the New button hides; Clear asks with focus on No, then
  returns to Clear; a starter load returns to the select; answering New as the fourth letter in Listen (New hides)
  moves to Hear again; Start over and Stop keep focus on Listen. Nothing ever fell to the page body.
- Targets: every visible control 44 px or more at every size (the strip spaces during editing are 47x40 but inert,
  `aria-disabled` and not tab stops). Color is never the only signal: letters and shapes on every block, syllables on
  every cell.
- Motion off (`calm`): the ripple becomes a still outline for 320 ms, then clears; no animation with infinite
  iterations runs in either setting, also during play (calm_ripple, motion_ripple, calm_later, calm_play).
- Sound off: the song and playhead still run silently; no oscillators made; Read still speaks.

## Sizes (default, a full strip with a block chosen, the editor, and Listen at each)

680x425, 800x500, 1000x625 (compact), 1280x720, 1366x768, 1920x1080 (wide), 760x900 (stack), 375x812 (host): no
horizontal scroll at any size; hint, Play song (or Listen), the strip and the Form card are in view without
scrolling at every size; the bar's Hear, Make it A′ and Remove in view; editor grid fully in view in the compact
and wide boxes (tight mode at 680x425: 48x44 cells). Smallest text 11 px (the "picked" tag). At 760 and 375 the
page scrolls to the shelf and editor, as the stack design intends.

## Voice check (held clicks, Sound on, Motion on)

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| welcomeBuild (first tap on the shelf) | welcome | 1 | 1 (at 0.13 s) |
| playHow (5 placements in a row) | how | 1 | 1 (one queued copy dropped "newer") |
| editHow (5 Edit opens) | how | 1 | 1, then silent x4 |
| twinHow (4 Make it ′) | how | 1 | 1, then silent x3 |
| linked (5 edit sessions, gap 2 s) | event | 5 | 4 (first dropped stale, finding 2) |
| linked (2 sessions, 3 notes each) | event | 2 | 2 (once per session) |
| form "A B. Two parts." (5 Plays to the end) | event | 5 | 5, each after the music |
| emptyStrip (5 Plays, empty strip) | event | 5 | 5 |
| listenWrong (5 wrong answers, Frere Jacques) | event | 5 | 5 |
| Frere Jacques end line | event | 1 | 1 |

- Stale lines: pick, place, Play, Stop, Edit, a note, Listen within 2 s (gap 0.2 to 0.35 s): playHow cut by Play,
  editHow cut by the mode change, welcomeListen at once; nothing played after its moment. Place, place, Play at gap
  0.3 s: playHow dropped ("newer", then "hush"). The one stale case is finding 3 (playHow while a block is picked).
- No line over the music: every form line starts after the song's onEnd; a welcome on a first tap that starts music
  (Play, Hear, Listen) is dropped, not delayed into the music.
- First tap: the stage background gets the welcome at 0.12 s; the Listen mode button gets only welcomeListen; Read
  speaks only the hint; Sound says nothing, and Sound back on brings the welcome only when it fits (empty strip);
  Play on an empty strip gets only emptyStrip; a key (Tab) decides the welcome too.
- Read: during the welcome it stops it and reads the current hint ("Now tap a space..."); with Sound off it still
  reads; during Play song it stops the music first, then reads; a mode change right after Read starts welcomeListen at
  once (0.13 s after the tap).
- Order: spoken lines follow the actions in every run.
