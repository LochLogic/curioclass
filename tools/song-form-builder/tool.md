# Song Form Builder: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 1 (general 0, family 1), should fix 10 (general 6, family 4), polish accepted 17

### song-form-builder: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.
The Teaching lens checked all six Listen songs note for note against its own transcriptions: all correct and public
domain. No rule-5 content, so no sensitivity agent.

#### Blockers
1. **Rests get no time** (C-B1; family:music-studio). src.html:716 `startPlay` never passes `beats` to `MS.play`,
   so an all-rest block and trailing rests are skipped: Blank starter with A A ends after the lead-in, Hear on an
   all-rest section ends in 0.1 s, a five-beat trailing rest cuts 8.5 s to 6.2 s and the playhead never reaches it.
   The spec's edge case says an all-rest block plays 8 beats of silence. Fix in the tool, and make the engine
   default safe (beats from the block length when not given) and say so in docs/families/music-studio.md.

#### Should fix
2. **Ode to Joy part 4 is A′ again, but there's no button for it** (T-S1; family:music-studio). A student who hears
   "same as part 2" is marked wrong, and the replay compares with part 1. Add "Same as A′" and a ▶ A′ button once A′
   is labeled (or the engine's general form: "same as any labeled part").
3. **Listen, wrong answer: 4.5 s before the side-by-side replay, with answers live** (P-S1; general). A second guess
   at a 2 s pace counts as the second miss and reveals the answer before the comparison plays (Done when 5). Lock
   the answers until the comparison starts (or play it at once), and with Sound off don't leave 4.5 s of silence.
4. **Start over is the big primary button in Listen and wipes everything with no Yes / No** (P-S2;
   family:music-studio). Make Play whole song the primary at the end, as the hint says; Start over secondary, with
   a Yes / No.
5. **First-screen line contradicts the hint** (P-S3; general). "Tap a block in the song strip..." shows under an
   empty strip while the hint says "Tap a block on the shelf". Say the shelf line until the strip has a block.
6. **The twin editor speaks the plain editHow line** (P-S4; family:music-studio). Beats 1 to 6 are locked; speak
   and show the twin's "change beats 7 and 8" version.
7. **The linked line is dropped if Done comes within ~4 s** (C-S2; general). src.html:665-668: "You changed A, so
   every A changed" is tied to the editor session and goes stale. Make it valid after Done (it belongs to the strip).
8. **"Press Play song" plays while a shelf block is picked** (C-S3; general). src.html:581 playHow ignores
   `state.sel`; the hint says "tap a space" at that moment. Match the line to the state.
9. **Clear song doesn't clear the save** (C-S4; general). src.html:788 removes the item, then `changed(false)` saves
   again, so every section survives a reload. Clear, then don't re-save until the next change.
10. **Grid focus ring covered by later cells** (C-S5; general). src.html:163; at 680x425 the top row and left column
    show a sliver. Raise the focused cell (z-index or outline-offset inward).
11. **`MS.stop()` and `MS.playing` see only the newest player** (C-S6; family:music-studio). kit/music-studio.js
    144/198/203: a player left running with `exclusive: false` can't be stopped and `playing` reads false. Track all
    players, or document `exclusive: false` as caller-managed and return a handle.

#### Polish accepted
12. Listen end lines: one clause per song tying the form to how it feels (T; MU:Re7.2's response half).
13. notes.md: one line that real A′ can vary more than "same start, new ending" (T).
14. Source line: Sarah Josepha Hale wrote Mary's words, not the melody (T nit, a fact).
15. notes.md: say Ode to Joy is the classroom version (in C, no tied anticipation) (T nit).
16. ABABA counted as a rondo: keep it, but the spoken "between new parts" line should fit it (T nit).
17. notes.md: quote the spoken Form line and list "A and its twin" among the card names (T nit).
18. A right answer in Listen gets a small on-screen and spoken lift (P).
19. The end of a Play gets a visible finish (P).
20. Playhead easier to see on a projector (P).
21. If the first tap is Hear, the welcome still gets its turn per the first-tap rule (P).
22. Form card: reserve less empty height; at 375 the shelf's Edit and Hear stay on screen (P).
23. At 1920, larger Form card text and a centered strip (P).
24. Listen reveal: replace "Press Stop to wait." with plain grade 3 words (P).
25. music-studio.md: the example implies lead 1 but the default is 0 (instrument default marimba); document `version` (C).
26. `pluck`, `blow`, `tick`: create the context themselves and respect Sound, or document both (C).
27. music-studio.md: the clock runs on the audio clock and stalls while the AudioContext is suspended; say so (C).
28. The "rest" label in the note sketches renders ~5 px and squashed; make it legible (C).

#### Spec open questions (not for the builder)
- An invitation to build AABA or a rondo (P polish; adds to the spec).

#### Settled calls
- The Listen songs are public domain and checked note for note; no sensitivity look needed (the builder's flag is closed).

#### Exit check, round 1

Fresh cold agent, 2026-10-28. Bundle `CURIO_DRAFT=1`: 106 KB, clean. Driven with `scripts/drive.py` (held clicks,
0.12 s) on port 9932, plus one Chrome on 9934 without the autoplay flag; frames and logs in the exit scratch folder
(`exit-sfb/out`, `exit-sfb/audit`). No console errors or exceptions in any tool run (one exception came from my own
test calling `place('C')` before C existed, not reachable from the UI). No network requests (resource list empty).
`allLines()` and voice/lines.json: 59 and 59, word for word. No em dashes; "Curio" only as `Curio.` in code.

##### Items
1. PASS. Blank starter, strip A A, Play song: 9.9 s from the tap (lead 1 + 16 beats at 100 = 10.2 s), the playhead on
   both blocks, the form line after the end. Hear on the all-rest B: 4.4 s measured after the hold (4.8 s from the
   press). Engine: `MS.play(MS.rows([-,-,-]))` takes its 1.5 s and ends 'end'; music-studio.md documents the default.
2. PASS. Ode to Joy part 4: "Same as A′" and "▶ A′" show once A′ is labeled; tapping it gives "Yes! A′ again: the
   same music." All six songs label to their forms with the new end lines (song0 to song5, ode).
3. PASS. Hot Cross Buns, wrong at part 2: answers aria-disabled at once (phase compare), part 1 plays at 0 s, part 2
   at 2.9 s, answers back at 5.35 s, then listenWrong. Sound off: the same timeline, no dead wait. A second miss reveals.
4. PASS. The big button is Hear it again while a part waits and Play whole song at the end; Start over is a small
   secondary button and asks "Start this song over?" Yes / No (No keeps both labels and returns focus).
5. PASS. Empty strip: "Your song strip: 8 spaces." under it (first1366, first680).
6. PASS. Make it A′, Edit A′: editTwinHow spoken ("Tap beats 7 and 8 ..."), hint matches (v_twin).
7. PASS. Edit, one note, Done at a 1 s pace: linked spoken at 14.7 s, after Done (v_linked).
8. PASS. Place A, then pick B: playHow dropped stale while B is picked (v_playsel); it comes once later (v_place5).
9. PASS. Clear, Yes: save is null, strip empty, sections back to A and B, focus on Clear.
10. PASS. Top-left cell at 680x425 by arrows: inset ring (offset -4 px, z-index 1), fully visible (gridfocus680).
11. PASS. Two players (one `exclusive: false`): `MS.playing` true; `MS.stop()` stops both.
12 to 17. PASS. End lines tie form to feeling (and shown on the card); notes.md has the A′ line, the classroom Ode
   line, the spoken Form line and "A and its twin"; sources say "words by Sarah Josepha Hale, 1830; traditional tune";
   ABABA shows "Most rondos bring a new part each time (A B A C A)."
18. PASS. A right answer shows "Yes! ..." and speaks it, with at least 1.1 s before the next part.
19. PASS. After ABA plays, both A blocks lift with an outline and the Form card glows for 1.8 s (aba_end).
20. PASS. Playing block gets a 5 px ink outline plus the moving column (midplay1920).
21. PASS. First tap Hear: welcome dropped at the tap, spoken at 6.2 s after the section ends (v_firsthear).
22. PASS. 375 host: shelf Edit and Hear in view on the first screen.
23. PASS. 1920x1080: Form letters 34 px, name 19 px, the strip centred.
24. PASS. "Here is the answer. Then the next part plays. Press Stop to pause."
25 to 27. PASS. music-studio.md: defaults line (lead 0, marimba), `version`, Sound-off and suspended context run on
   the page clock; `pluck`, `blow`, `tick` make the context and respect Sound (code read).
28. PASS. "rest" is HTML at 11 px, 18 px tall, not squashed (rest680).

##### Regressions looked for
Default screen at every size (audit frames), Build at 1366 and 1920 mid-play, the editor at 680x425, Listen mid-song,
the Start over question, Listen done at 760: nothing clipped or overlapping, no new console errors.

##### Gate
1. Done when 1 to 8: pass (1 aba_end; 2 v_linked and v_linked5; 3 ABA, ABACA, ABABA and the code's rule order; 4 twin
   lock and editTwinHow, code unchanged from the Teaching check; 5 all six songs; 6 counts below; 7 lines after onEnd,
   Read stops play; 8 audit sizes).
2. MU:Cr2, Cr3 and Re7 are taught by what the student does (Re7's response half now in Listen's end lines).
3. Solo defaults work: the first screen and every waiting moment name the next control.
4. No rule-5 content; no sensitivity agent needed.
5. No blocker or should-fix open.
6. Bundle 106 KB, no console errors, no network requests.
7. Voice counts right:

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| welcomeBuild (first tap shelf) | welcome | 1 | 1 |
| welcomeBuild (Sound off, on) | welcome | 1 | 1 |
| playHow (5 placements) | how | 1 | 1 |
| editHow (5 opens) | how | 1 | 1 |
| twinHow, editTwinHow | how | 1 each | 1 each |
| linked (5 sessions) | event | 5 | 5 |
| form line (5 plays to the end) | event | 5 | 5, each after the music |
| emptyStrip (5 Plays) | event | 5 | 5 |
| listenWrong (5 misses) | event | 5 | 5 |
| Read (during welcome, Sound off, during play) | read | hint | hint; play stopped |

Stale run (7 taps at 0.3 s, then Listen): playHow dropped by hush, editHow cut by the mode change, welcomeListen at
once; nothing late.

##### Left open (nits, not blocking)
- kit/music-studio.js `play`: the audio clock is used only when `ctx().state` is 'running' at that instant. Chrome
  reports 'running' synchronously inside a tap (checked without the autoplay flag: 17 oscillators on the first Play),
  but some browsers report a context made in the same call as 'suspended' until a tick later, which would make the
  very first Play silent there. Unverified; worth a look on Safari and Firefox in Final look. family:music-studio.
- Listen: pressing Stop during the short "Yes!" pause moves to the next part without playing it (the student then
  presses Hear it again). general.
- Known from round 1, not accepted: Tab order (Instrument and Done before the grid), one AudioContext shared with the
  kit, held notes in `rows`.

##### Audit pilot
- Leads confirmed: none were faults. The eight "below the fold" leads are real positions (Starter songs and Clear
  song at 680x425 and 800x500; Speed, Starter songs and Clear song at 375) but they are occasional controls under the
  main ones, which all show (Done when 8).
- Leads wrong: the eight above as faults (it cannot tell a main control from an occasional one).
- Clean rows confirmed: Motion off, focus on load, the one-click walk (no rebuild under the pointer), the 2 s
  five-click runs (playHow, editHow once; emptyStrip five).
- It missed: everything past one click (Listen answers, compare timing, the twin editor line, linked after Done,
  playHow while a block is picked, Clear's save, the grid focus ring, all-rest timing, the engine's multi-player stop),
  which is where all of round 1's items lived.

<!-- end part -->

<!-- part: refine/craft.md -->

### song-form-builder: Craft lens (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/music-studio.js against
docs/families/music-studio.md, and kit/curio.js (voice). Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
song-form-builder` (104,896 bytes). Driven with `scripts/drive.py` (held clicks, 0.12 s), ports 9940 and 9942, the 375
host on 9941 (`--host`). Frames and logs in the lens scratch folder `lens-sfb-craft2/out` (sizes, h375, eng, focus,
calm, voice, voice2, voice3, vis, lans).

Counts: blockers 1, should fix 5, polish 4, nits 4.

#### Contract

- One file, 104,896 bytes (well under 2 MB). Kit used: `Curio.voice`, `Curio.init`, the kit frame CSS, and
  `MS` from kit/music-studio.js; nothing re-implemented.
- No network requests: `performance.getEntriesByType('resource')` is empty after Play song, Listen and a phrase; the
  bundle has no fetch, XHR or URL loads.
- No console errors, warnings or exceptions in any shot (about 70 shots at every size, both modes, engine tests). The
  only log line was the 375 host page's own favicon 404, not the tool.
- `allLines()` (53) and voice/lines.json (53) match word for word, both ways. No `art:` tokens; prompts.json has no
  assets (everything drawn in code). No em dashes in src, notes, lines or spec; "Curio" only as `Curio.voice` and
  `Curio.init` in code. Privacy line on screen: "Your song is saved on this device only. Nothing leaves it."

#### Engine against docs/families/music-studio.md (line by line, tested in the page)

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

#### Findings

##### Blocker

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

##### Should fix

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

##### Polish

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

##### Nits

11. src.html:229 (`#newsec`): at 1366x768 and 1920x1080 "＋ New section C" wraps so "C" sits alone on its own line
    (sizes def_1366x768). A non-breaking space before the letter keeps it together. Tag general.
12. Listen at 375 (host): "↻ Hear again" ends 11 px below the fold while answering part 8 of Frere Jacques (lans_375);
    the Same / Almost buttons above it are in view. Tag general.
13. kit/music-studio.js:73: the engine makes its own AudioContext while the kit's `Curio.audio()` makes another; two
    contexts per page. Reusing the kit's would halve the setup. Tag family:music-studio.
14. kit/music-studio.js:61: `rows` makes one-beat notes only, so melody-maker's held notes (its `undefined` after a
    note) can't go through it when it moves to the engine; it will build events itself. A `hold` value in `rows` would
    cover it. Tag family:music-studio.

#### Access

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

#### Sizes (default, a full strip with a block chosen, the editor, and Listen at each)

680x425, 800x500, 1000x625 (compact), 1280x720, 1366x768, 1920x1080 (wide), 760x900 (stack), 375x812 (host): no
horizontal scroll at any size; hint, Play song (or Listen), the strip and the Form card are in view without
scrolling at every size; the bar's Hear, Make it A′ and Remove in view; editor grid fully in view in the compact
and wide boxes (tight mode at 680x425: 48x44 cells). Smallest text 11 px (the "picked" tag). At 760 and 375 the
page scrolls to the shelf and editor, as the stack design intends.

#### Voice check (held clicks, Sound on, Motion on)

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

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: song-form-builder (round 1)

Played cold as a grade 3-5 student alone at home and as a teacher projecting to a class. Bundle: `CURIO_DRAFT=1`,
100 KB, no console errors or exceptions in any run (the only log line was the host page's own favicon 404 at 375 wide).
Placeholder art and the browser voice are not reported.

Counts: blockers 0, should fix 4, polish 8, nits 4.

#### Frames looked at

All in the lens scratch folder (`lens-sfb-play2/out/`):
- f1: default, Rondo for Recess, a full 8-block strip with a twin, the editor open, Listen idle, Listen done
  (Frere Jacques), at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x1000.
- f2 and f11: 375 wide in the iframe host (`drive.py --host`): default, a real tap-to-place, editor open and scrolled,
  Listen mid-song (Frere Jacques, part 4 of 8), Listen done (Ode to Joy).
- f3 and f4: a solo ABA build at a 2 s held-click pace, playing to the end, mid-play playhead, an edit session of five
  taps, the twin flow (Make it A′, Edit, beat 7, Done, Play).
- f5: keyboard: full Tab order, place with Enter, arrows along the strip (both ends), the bar under the strip,
  the note grid (arrows, Space, Enter, Delete), Escape.
- f6 and f7: Listen at a 2 s pace (Hot Cross Buns with two wrong answers, Mary with one wrong answer, Sound on and
  Sound off, Row Row Row done at 680x425).
- f8: drags with whole-pixel jittered pointer paths (onto slot 6 of a 1-block strip, onto a filled slot, released
  mid-strip, released off the strip), Play with an empty strip, Read during play, Clear and starter confirms,
  ripple with Motion off and on, a strip block picked.
- f10: first-tap timing on fresh pages (stage, Read, Sound, Sound off then on, Hear, a mode button, New section, Tab).
- f12: five placements in a row and two full plays (Quick).

What works well: the first screen says what to do and the hint follows every step; placing by tap, drag and keyboard
all work (no gaps, replace, off-strip drop does nothing); arrows walk the strip and stop at both ends; linked copies
ripple (outline with Motion off) and the Form card counts "3 copies changed"; Read stops the music; the empty-strip
Play speaks "Put a block in the song strip first." and flashes the shelf; how lines spoke once in five actions
(playHow 1 of 5 placements) and the form line spoke on every finished play (2 of 2), about 1 s after the music ends,
never over it. Strip, Play song and the Form card are on screen without scrolling at every size, including 680x425
and 375 wide.

#### Should fix

1. **Listen, a wrong answer: the answer buttons stay live for about 4.5 s before the comparison plays, so the
   side-by-side replay is easy to skip.** (mode Listen; `answer()` awaits `listenWrong` with `wait: true` before
   `phraseDone(ck)`, while `phase` stays `'answer'`.) Seen in f6/f7 timelines: Mary, wrong tap at 22.4 s, replay of
   part 1 starts at 27.1 s; with Sound off the student sits 4.5 s in silence under "Listen again" with nothing playing.
   In Hot Cross Buns at a 2 s pace the student's second guess landed at 11.7 s, cut the line, and counted as the
   second miss, so the reveal came without the two phrases ever being heard side by side (spec Done when 5). Better:
   start the comparison at once (or the line and the comparison together, line shown and spoken after), and hold the
   answer buttons disabled until both phrases have played. **general** (any quiz with a feedback line before a
   replay).
2. **Listen: the biggest button on screen while answering is "↺ Start over", and it wipes the labels with no
   question.** (mode Listen, `#listen` once `phase !== 'idle'`; frames 375-listen, l2b-mary-wrong-680,
   1366x768-listendone.) A grade 3 student looking for "play it again" taps the big teal button and loses Frere
   Jacques at part 4 of 8. Build's Clear song asks Yes / No; Listen should match, or make the big button "↻ Hear
   again" while answering and move Start over to a small button by the Song picker. At the end of a song the hint
   says "Press Play whole song" but the big button is still Start over and Play whole song is the small one under the
   card. **family:music-studio** (Listen-style labeling).
3. **First screen: the line under the empty strip contradicts the hint.** (Build, `#barlab` default text.) With an
   empty strip it says "Tap a block in the song strip to hear it, twin it or remove it." while the hint says "Tap a
   block on the shelf". There are no blocks in the strip, and tapping an empty space does nothing. Seen in every
   default frame (f1 *-default, f11 680-clean-default, f2 375-default). Show nothing there (or "Your song strip:
   8 spaces") until the strip has a block. **general** (words match the state).
4. **Twin editor: the how line speaks the plain-section version.** (Build, `openEditor` speaks `editHow` "Tap the
   grid to change the notes. Every copy of this section changes too." for a twin as well.) Run v2-twin: after Make it
   A′ and Edit on A′, the spoken line tells the student to tap the grid, but beats 1 to 6 are locked; the hint and
   tip say beats 7 and 8. If the first Edit a student ever opens is a twin, that is the only time editHow plays. Speak
   the twin hint ("Tap the grid in beats 7 and 8 ...") for a twin, its own how key. **family:music-studio**.

#### Polish

1. **A right answer in Listen is flat.** Only a chime and the block appearing; the question line just changes to
   "Part 3 of 4" (f6 timeline 20.3 s). Better: a short shown line "Yes: new music, B." for a beat before the next
   part plays, so a student alone knows the guess was right and why. **family:music-studio**.
2. **The end of a play is flat.** After ABA plays, the form line is spoken but nothing on screen changes; the Form
   card already showed "Ternary" before Play (b2-aba-play). Better: when the song finishes, briefly mark the matching
   letters in the strip (the two A blocks lift or get a bracket "home ... home"), so the shape is seen as well as
   heard. **family:music-studio**.
3. **The playhead is hard to see on a projector.** A 6 px bar above the block and a 35% opacity column on the note
   sketch (v1b-midplay). Better: the playing block lifts or gets a thick outline, so a class can follow from the back.
   **family:music-studio**.
4. **A first tap on Hear (or anything that starts sound) loses the welcome for good.** (ft-hear: welcomeBuild
   dropped stale at the first tap and never comes back; the hint still shows it.) Hear is a natural first tap. Better:
   bring the skipped welcome once when that first sound ends. **general**.
5. **The Form card reserves a tall empty box.** About 120 px of white under "Put blocks in the song strip to see its
   form." at 1366x768 and 375 wide (f1 1366x768-default, f2 375-default). At 375 it pushes the shelf to the fold, so
   the shelf's Edit and Hear buttons start below the screen. Better: reserve less at narrow widths, or put the shelf
   above the long card text in the stack layout. **general**.
6. **Teacher on a projector: the Form card text is 14.5 px at 1920x1080 and the strip stops at 150 px blocks with a
   290 px gap on the right** (1920x1080-full8). The form name is the teaching moment; scale the card's name and
   letters up on big screens and centre the strip as Listen's is. **general**.
7. **"Press Stop to wait." in the Listen reveal hint is confusing for grade 3** (`H.lReveal`). Better: "Here is the
   answer. The next part plays next. Press Stop to pause." **family:music-studio**.
8. **A solo student runs out of reasons to keep building after one or two songs.** After ABA and one edit the hint
   loops "Press Play song again"; nothing invites trying AABA or a rondo. Better: one optional "Can you build a rondo?"
   line after the second play, or a small challenge list. This adds to the spec, so it goes to the spec's open
   questions, not the builder. **general**.

#### Nits

1. Keyboard: Tab from the note grid jumps out to the header, because Instrument and Done come before the grid. Done is
   one long Tab loop away; put Done after the grid in the tab order (f5 k2, k5). **general**.
2. "＋ New section C" wraps the letter onto its own line at 1366x768 and 800x500 (f1 defaults). **general**.
3. At 680x425 the empty strip is 2 rows of 4 (46 px blocks would fit in one row); the shelf then scrolls inside
   (scrollHeight 252, clientHeight 149, f11). It works; one row would give the shelf room. **family:music-studio**.
4. Listen done: the eight disabled Same / Almost buttons stay on screen under "All 8 parts labeled." (f1
   1366x768-listendone, f7 l4-row-done-680). Hide them at the end so Play whole song stands out. **family:music-studio**.

#### Voice at a 2 s tap pace (from the logs)

| line | kind | expected | spoken |
|---|---|---|---|
| welcomeBuild (first tap on the shelf, stage, New section, Tab) | welcome | 1 | 1 |
| welcomeBuild (first tap Read / Sound) | welcome | 0 | 0 (Read spoke the hint only; Sound off then on brought it once) |
| welcomeBuild (first tap Hear) | welcome | 1 later | 0 (polish 4) |
| playHow (5 placements) | how | 1 | 1 |
| editHow (5 grid taps) | how | 1 | 1 |
| linked A (5 grid taps, one session) | event | 1 | 1 (one queued copy dropped as newer) |
| twinHow | how | 1 | 1 |
| form line (2 and 3 plays) | event | each play | each play, about 1 s after the music |
| emptyStrip | event | 1 | 1 |
| listenWrong | event | 1 per miss | 1 (but see should fix 1) |
| reveal and song end lines | event | 1 | 1 |

No line played over the music. No stale line played after a mode change in these runs.

Note: `tools/song-form-builder/host.html` was already in the tool folder when this lens started (another lens's
`--host`); this lens's `--host` rewrote it with the same content and left it there, since another agent may still be
using it.

<!-- end part -->

<!-- part: refine/teaching.md -->

### song-form-builder: Teaching lens (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, tool.draft.json, voice/lines.json and kit/music-studio.js (parse, semi,
rowSemi). Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py song-form-builder` (100 KB). Driven with
`scripts/drive.py`, held clicks, 1366x768, 1280x720, 680x425. Frames and scripts in the lens scratch folder
(lens-sfb-teaching/out: dw1_play, dw2_edit, dw2_linked, dw4_twin, dw67, listen0 to listen5, listenwrong, listen_mid,
preview680, w1280). No console errors in any shot.

Counts: blockers 0, should fix 1, polish 2, nits 4.

#### Musical facts checked

- **Listen songs, note by note.** I wrote my own reference transcription of each song (in C, as sung in US classrooms)
  and parsed the tool's strings with a Python copy of `MS.parse` (lengths `e .5, dq 1.5, h 2, w 4`, numbers as beats,
  `scale .5` for 6/8). Every bar sums to its meter (4 beats; Row Row Row 3 quarter beats = one 6/8 bar), and every
  pitch and rhythm matches: Hot Cross Buns (E D C | x2 | C C C C D D D D | E D C), Mary (E D C D E E E, D D D, E G G /
  E D C D E E E E D D E D C), Twinkle (A: C C G G A A G F F E E D D C; B: G G F F E E D twice), Ode to Joy (both
  endings E. D D and D. C C; B phrase D D E C | D EF E C | D EF E D | C D G3), Row Row Row (C. C. | C D E. | E D E F |
  G.. | C5 x3 G x3 E x3 C x3 | G F E D | C..), Frere Jacques (C D E C | E F G | GAGF E C | C G3 C).
- **Engine pitches.** `semi()` gives C 0, D 2, E 4, F 5, G 7, A 9, G3 -5, C5 12 above middle C (261.63 Hz); the
  pentatonic rows are 0 2 4 7 9 12 (do re mi sol la high do). Right.
- **Forms.** A vs A′ compared bar by bar: Mary's A′ shares bar 1 and the start of bar 2, then a new ending; Ode to
  Joy's A′ differs only in bar 4. Hot Cross Buns AABA, Mary A A′, Twinkle ABA, Ode A A′ B A′ (AABA), Row Row Row
  ABCD, Frere Jacques AABBCCDD are the usual classroom analyses at the phrase lengths the spec chose.
- **Public domain.** All six are: Hot Cross Buns (English street cry, 18th century), Frere Jacques (French, 18th
  century), "Ah! vous dirai-je, maman" (published 1761), Mary Had a Little Lamb (words 1830, traditional tune), Row
  Row Row Your Boat (tune published 1881), Beethoven's Ninth (1824). Starter songs are original.
- **Form card rules.** Ran `analyze()` on 24 strips: AAA strophic; A A′ and A A′ A A′ twin; ABC, ABCD through-composed;
  AB binary; AABB binary repeated; ABA, B A B (with "Your B plays the A part. Your A plays the B part.") ternary;
  AABA and A A′ B A′ AABA; ABACA, ABABA, ABACABA rondo; ABBA, AAB, ABCA no special name; single block asks for more.
  All match the spec's order and wording. The ending check (`row % 5 == 0`) is do or high do: right.
- **Starter songs** match the spec (Sunny Day ABA ends on do; Rondo for Recess ABACA ends on do).

#### Standards (rule 2)

Module arts-3-5-form-and-composition: MU:Cr2, MU:Cr3, MU:Re7. This is the only tool on the module.
- **MU:Cr2 (organize and develop):** taught. Students write 8-beat sections on a solfege grid and arrange them into
  forms (Cr2.1a), documented as iconic notation: lettered, shaped blocks and the grid, saved (Cr2.1b).
- **MU:Cr3 (refine and complete):** taught for Cr3.1. The Form card gives criteria and feedback the student acts on
  ("A and B have the same notes", "A′ is still the same as A", "Ends away from do"), and the linked edit makes
  revising one section revise the whole song. Cr3.2 (present and describe expressive intent) lives only in the
  teacher's Talk about it questions.
- **MU:Re7 (perceive and analyze):** taught for Re7.2's structure half: Listen has students identify same, almost
  and new by ear. The "how structure shapes a response" half is thin in Listen (see polish 1). Re7.1 (choosing music
  for a purpose) is not touched; fine at anchor level, but worth naming in notes.

#### Done when

1. PASS. Held clicks A, B, A then Play song: playhead walked slots 0, 1, 2; card "A B A / Ternary form: away and
   back home."; spoken "A B A. You went away and came back home." after the music (dw1_play).
2. PASS. One cell in A's editor: both A slots changed (dataset keys and sketches), "2 copies changed"; the linked
   line spoken once over three edits (dw2_edit, dw2_linked).
3. PASS. All rules, including B A B as ABA, A A′ B A′ as AABA, ABACA as rondo (analyze run above).
4. PASS. A's beat 1 change reached A′; A's beat 7 change did not; A′'s beat 1 is locked with the chain tip; A′'s
   beat 8 is its own (dw4_twin).
5. PASS. All six songs labeled to their spec forms and end lines (listen0 to listen5); a wrong label replays the
   compared phrase (part 1) and then part 2 (listenwrong: phrase 0 at 4.7 s, phrase 1 at 7.5 s); two misses reveal
   "It's A again: exactly the same music."
6. PASS. playHow spoken once in the run, form line on each of three Plays (dw67).
7. PASS. Lines come after onEnd; Read during play stopped it (playing true, then false) and read the hint (dw67).
8. PASS. Strip, Play song and Form card on screen at 1366x768, 1280x720 and 680x425 (dw1_play, w1280, preview680).

#### Findings

##### Should fix

1. **Listen, Ode to Joy part 4 (src.html:829-838, 893-906): a correct ear gets "Not quite".** Part 4 is exactly
   A′ again (the same as part 2), but the buttons are only per base letter: Same as A, Almost A, New. A student who
   hears "that's part 2 again" and taps Same as A is marked wrong, and the replay compares part 4 with part 1, never
   with part 2, so the tool never confirms what the student actually heard. Better: once A′ is labeled, show a
   "Same as A′" button (and a ▶ A′ hear button) and accept it for a repeat of A′; or at least make the reveal and
   lAnswer say "A′ again counts as Almost A". Seen in listen3 and listen_mid; checked against the code paths.
   family:music-studio (Listen labeling format).

##### Polish

1. **Listen end lines name letters only (src.html:334-341); Re7.2's response half is left to the teacher.** Build's
   form lines already tie form to feeling ("You went away and came back home", "Ends on do: sounds finished"); Listen's
   end lines mostly just spell the letters. A solo student never hears how the form shapes the listening. Better: one
   clause per song on the card and in the end line, for example "Twinkle Twinkle is A B A. The tune comes home at the
   end, so it feels finished." and "Ode to Joy is A A′ B A′. B is the trip away; A′ brings you back." This is real
   teaching, not a thin add-on. family:music-studio.
2. **A′ is taught only as "same start, new ending" (spec, H.editTwin, L.reveal.twin, notes.md).** That is one kind of
   variation; real A′ sections can change rhythm or the middle too (Mary's A′ already changes the rhythm in bar 2).
   Better: one line in notes.md's Good to know: "In real music A′ can be any small change; this tool shows the most
   common one, a new ending." general.

##### Nits

1. **Sources, Mary Had a Little Lamb (tool.draft.json sources, src.html:18):** "Mary Had a Little Lamb (Sarah
   Josepha Hale, 1830)" sits in a list of public domain *melodies*; Hale wrote the words. The spec says "poem by". Say
   "words by Sarah Josepha Hale, 1830; traditional tune". general.
2. **Ode to Joy is the classroom version (spec, notes.md):** transposed to C and without Beethoven's tied
   anticipation into the last phrase. Fine for the grade; one phrase in notes ("the classroom version of Beethoven's
   tune, in C") keeps a music teacher from flagging it. general.
3. **ABABA is called a rondo (src.html:405, spec rule 7).** Inside the spec, and some texts accept it, but most
   grade 3-5 material defines rondo as A between *different* parts (ABACA); the spoken line "between new parts" is not
   quite true for ABABA, where B repeats. Optional: have ABABA's card add "Most rondos bring a new part each time
   (A B A C A)." family:music-studio.
4. **notes.md, A 5-minute start, step 2:** "listen to the Form card: 'Ternary form: away and back home.'" The card
   shows that text, but the voice says "A B A. You went away and came back home." Say "read the Form card" or quote
   the spoken line. Also the Two modes list of card names leaves out "A and its twin". general.

#### Guardrails and sensitivity

Grades 3-5, students or teacher: no K-2 rule. No hard history, no health topic, no scoring or timer (Listen keeps no
score). No cultural, Native or living-tradition music: all six songs are European or American public domain children's
and concert tunes; no sensitivity agent needed (rule 5). Teacher notes: no sensitive topics in these standards (rule 8).
Nothing in Listen gives the answer away: the current part shows only "?", its sketch and playhead dot stay hidden until
it is labeled, and the aria-label says "listening now".

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### song-form-builder: build handoff (2026-10-28)

#### What was built

- `src.html` (about 106 KB bundled): Build and Listen modes per the spec, on the new family engine.
- `kit/music-studio.js` (new, version 1.1 after Refine round 1) and `docs/families/music-studio.md` (its reference). No existing kit file
  was changed.
- `tool.draft.json` (stage built), `notes.md`, `art/prompts.json` (no art: everything is drawn in code),
  `voice/lines.json` (bank playful-friend, voice Laomedeia, all 59 strings from `__tool.allLines()`).

##### Layout

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

##### Voice

`Curio.voice` with `hint: false`: the tool owns the hint (`H` table), and Read speaks `hintText()` with ′ read as
"prime". How lines (`welcomeBuild`, `playHow`, `editHow`, `twinHow`, `welcomeListen`) are chosen by `V.heard`, with
`valid` and `needs`; the linked line once per editor session (marked inside `valid` when it starts); form lines,
sameNotes, emptyStrip, listenWrong, reveals and song end lines are events. Play calls `V.hush()`; result lines are
queued after `onEnd` and are valid only while the strip version is unchanged. `answer()` hushes, so a stale
listenWrong never plays after the next answer.

#### Engine API (kit/music-studio.js, global MS)

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

#### Done when (spec)

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

#### Refine round 1 (2026-10-28)

Fixed: the blocker (rests get their time: the tool passes `beats`, and the engine defaults to the list's `.beats`),
every should-fix (2 to 11) and every accepted polish (12 to 28); also the nits for "New section C" wrapping and the
answer buttons left on screen at the end of a song. Re-checked against BUILD.md's Wave lessons (BR1). Frames
re-shot at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375 (host), in Build, the
editor, Listen mid-song (Frere Jacques, Ode to Joy with A′), the Start over question and the end of a song: targets
44 px or more, nothing clipped, no horizontal scroll, the main controls in view. Not done: the Tab order nit (Done
before the grid) and the two engine nits (one shared AudioContext with the kit, held notes in `rows`); they were not
on the accepted list.

#### Deviations from the spec (on purpose)

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

#### Known gaps

- Keyboard: Tab reaches every control, arrows walk the strip and the grid, Delete makes a rest, Escape clears a
  pick. In the editor, Instrument and Done come before the grid in Tab order.
- Recordings are not made yet (`voice/lines.json` is ready).

#### Sensitivity (rule 5)

No Native or living-culture music. The Listen songs are public domain: Hot Cross Buns (English traditional), Frere
Jacques (French traditional), Twinkle Twinkle ("Ah! vous dirai-je, maman", France, 1761), Mary Had a Little Lamb
(1830), Row Row Row Your Boat (1881), Ode to Joy (Beethoven, 1824). The starter songs were written for Curio Class.
Refine's Teaching lens checked all six note for note and closed the flag: no sensitivity review needed.

#### For Cory

- The new shared engine `kit/music-studio.js` is ready for melody-maker, chord-explorer and beat-lab when they are next
  reworked; nothing existing was touched.
- One spec deviation worth a look: the Listen answer buttons live on the stage, not in the panel.
- The spec open question from Refine (an invitation to build AABA or a rondo) is left for the spec.
- Motion off: no infinite animation runs (the ripple, the playhead outline and the end-of-play lift are one-shot;
  the ripple and lift have their own calm rules).

<!-- end part -->

## Finish check

<!-- part: final.md -->

PASS
Counts: blockers 0, should fix 0, polish 5 (general 4, family 1)

### song-form-builder: Final look

Fresh cold agent, 2026-10-29. Bundle `tools/song-form-builder/song-form-builder.html`, 1,269,980 bytes (built
11:28, after src.html 07:35 and the clips 07:53, so current; not rebuilt). Driven with `scripts/drive.py`, held
clicks (0.12 s), Chrome on 9221 and 9222, iframe host on 8813 for 375. Frames, logs and scripts in
`S:/CurioClass-codex-scratch/final/song-form-builder/` (out1 default frames, out2 voice runs, out3 state frames,
out4 pace and Read runs). Every page was instrumented: each clip's start, end and cut (matched to its text by a
fingerprint of the bundled data URI), every `MS.play` start and end, and whether a clip was playing when music
started (`talking`) or music was playing when a clip started (`music`). No art: everything is drawn in code, so
step 2 (art against the spec) has nothing to check. No rule-5 content and no people, so no sensitivity agent.

#### 1. Frames

Looked at every one. Default screen at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and the
375 host (out1 `default_*`, out3 `h375_default`); Build mid-play (`buildmid_1366/680/1920/760`, `h375_buildmid`),
the end of a Play with the lift and glow (`buildend_1366`) and with Motion off (`buildend_calm_1366`); the editor
(`editor_680/800/760/1366/1920`, `h375_editor`), the twin editor (`twined_680`) and the strip bar with Make it A′
(`twinbar_1366`); the extreme of a full strip with A′, B′, C and D (`full_680/760/1366/1920`, `h375_full`); Listen
default (`listen_1366/680`), waiting for a label (`lmid_1366/680`, `h375_listen`), the side-by-side compare
(`lcompare_1366/680`), a reveal (`lreveal_1366`), Ode to Joy with the A′ answer row (`lode_1366`), the Start over
question (`lrestartq_760`) and the end of a song (`ldone_1366/680`, `h375_ldone`, `ldone_calm_1920` with Motion off).
Nothing clipped or overlapping, no text over a busy picture (there are none), no placeholders, no sideways scroll.
The main controls (strip, Play song or Listen / Hear it again, the Form card, the answers) are in view at every size.

#### 2. Art

None in the tool (`art/prompts.json` has no entries; no `art:` tokens). Nothing to check.

#### 3. Voice with the real clips

59 clips, one per line of `voice/lines.json`, all present, none extra; the bundle's clip map has exactly the 59
texts of lines.json, and `__tool.allLines()` returns 59. No browser-voice fallback fired in any run (speechSynthesis
was never called). Every spoken log entry is a lines.json text. Clip lengths 1.92 s to 8.56 s; each is under the
queue's hold cap (closest: line 6, 6.64 s against 7.22 s).

**Each clip says its line.** I can't listen, so I transcribed all 59 raw takes with local Whisper large-v3 and
compared word for word (`asr.json`). 47 match exactly; the other 12 differ only in spelling the transcriber chose
("ABA", "B'", "OK", "Frère", "Here" for "Hear", "a prime" for "A prime"), except two takes that use a contraction
(polish 3). One take was heard as "You changed uh, so every A changed" (line 4) by large-v3 but correctly by
whisper-base.en; worth one listen by ear (polish 2).

**Timing against the music (the tool plays music).** In every run, `talking` was 0 at every music start and
`music` was false at every clip start: no line ever played over the music.
- Build, Play song: the form line starts within 10 ms of the music's end, 5 of 5 (C_play5); ABA plays 15.1 s
  (1 lead + 24 beats at 100 bpm = 15.0 s).
- Hear on a shelf block as the first tap: the welcome waits for the section to end (4.9 s), then plays (D_hear).
- Listen, right answer: "Yes! ..." plays to its end (2.6 s), the next part starts 0.6 s later (B_listen).
- Listen, wrong answer: part 1, 0.35 s, part 3, then listenWrong right at the end of the music (B_listen,
  B2_reveal). Second miss: the reveal line plays out (3.3 s), the next part starts 0.47 s after it.
- Listen, end of a song: "Yes!" then the end line 0.16 s later, both whole (B_listen).
- Read during music (Build or Listen) stops the music first, then reads the hint (readplay_build, readplay_listen).
- Starting music always hushes a line in progress (the student's own action): welcomeListen cut when Listen is
  pressed early; the linked line cut when Play is pressed 3 s into it (pace2_edit).

**Counts with the clips** (held clicks; the 5x runs at a gap longer than the lines, plus 2 s pace runs):

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| welcomeBuild (first tap: slot, shelf pick, key) | welcome | 1 | 1 each |
| welcomeBuild (first tap Hear) | welcome | 1, after the music | 1, at the music's end |
| emptyStrip (first tap Play on an empty strip) | event | 1, no welcome | 1, no welcome |
| welcomeListen (first tap Listen mode) | welcome | 1 | 1 |
| Read as the first tap | read | hint only | hint only |
| Sound as the first tap | none | 0 | 0 |
| playHow (placements at 6.5 s and 2 s pace) | how | 1 | 1 |
| editHow (5 sessions) | how | 1 | 1, then silent 4 |
| linked (5 sessions) | event | 5 | 5 |
| form line (5 Plays) | event | 5 | 5, each after the music |
| twinHow, editTwinHow | how | 1 each | 1 each |
| right-answer lines, listenWrong, reveal, end line | event | every time | every time |

Stale run (6 taps 0.2 s apart, then Listen; E_stale): playHow dropped as newer, editHow dropped by the mode hush,
the build welcome cut, welcomeListen at once; nothing late. Read (F_read): Read cuts the welcome and speaks the hint;
Read with Sound off speaks; a mode change right after Read starts the next line at once. Order followed the actions
in every run.

**Liveliness reading** (`voice_liveliness.py`, semitone SD): one flag, line 52 "Listen to the music. Press Stop to
stop." (2.21, range 7.4, median 273 Hz). Judged: it can never be heard. It is the `lPlaying` hint, and Read stops
the music and moves Listen on before it speaks, so the hint is never `lPlaying` when Read runs (readplay_listen
read the next hint). The same holds for lines 46 (`playing`) and 47 (`hearing`). No redo needed. Everything else
is at 3.14 or more. Line 47's median pitch (338 Hz) is far above the voice's home (about 200 Hz), but it is also
never heard.

#### 4. Full runs

As a solo student at 1366 (A_build, pace2_build, B_listen): the welcome names the shelf and the strip, playHow comes
when the strip has blocks, the form line lands right after the song, the end glow and A lifts show the shape. In
Listen the Yes / Not quite rhythm with the real voice feels lively; waits between parts are short (0.45 to 0.6 s).
As a teacher projecting at 1920x1080 (`buildmid_1920`, `full_1920`, `ldone_calm_1920`): letters and Form card are
large and readable; the lower half of the stage is empty (polish 4). At 375 (host) everything a student uses is in
order, top to bottom.

#### 5. Contract

Bundle 1.27 MB with all 59 clips (under 2 MB). No console errors or exceptions in any tool run (the only messages
were the iframe host's own favicon 404 on port 8813, not the tool). No network requests
(`performance.getEntriesByType('resource')` empty). No em dashes in src.html or notes.md; privacy line on screen
("Your song is saved on this device only. Nothing leaves it.").

#### Findings

##### Blockers
None.

##### Should fix
None.

##### Polish
1. **The linked line comes late at a quick pace** (general). Build editor, pace2_edit: editHow (5.2 s) holds the
   queue, so "You changed A, so every A changed" starts only at 5.5 s, after Done, and a Play at 8.7 s cuts it 3.2 s
   in. At a slower pace it plays whole (C_edit5). The ripple still shows it. Option: a shorter editHow take, or let
   linked replace a how line still playing.
2. **Line 4 take: listen once by ear** (general). Whisper large-v3 heard "You changed uh, so every A changed";
   base.en heard it right. It is the line a student hears most (every edit session of A). If the first "A" is
   swallowed, `localvoice.py song-form-builder --redo 4 --takes 5`.
3. **Two takes use a contraction the line doesn't** (general, nit). Line 48 says "when you're finished" (text: "you
   are"), line 53 says "Here's the answer" (text: "Here is"); both models agree on 53. Meaning unchanged; redo only
   if exact wording matters.
4. **1920x1080: the lower half of the stage is empty** in Build and Listen (`buildmid_1920`, `full_1920`,
   `ldone_calm_1920`) (general). Bigger strip blocks there would help a projector. Not new since Refine.
5. **Recorded but unreachable lines** (family:music-studio, nit). Lines 46, 47, 52 (the while-playing hints) can't
   be spoken, since Read stops the music first. Harmless; worth a note in music-studio.md so the next tool doesn't
   spend time on their takes (and line 52's flat take needs no redo).

##### Left open from Refine (not checked here)
- The Safari / Firefox first-Play question (audio context reported 'suspended' in the same tap) needs a non-Chrome
  browser; only Chrome was available. family:music-studio.
- At 375 the editor grid starts below the fold (`h375_editor`, one row shows); the student scrolls. Unchanged since
  Refine, where Done when 8 covered the strip, Play song and the Form card.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)
- 2026-11-25: final.md folded in (last changed 2026-10-29)
