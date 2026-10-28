PASS
Counts: blockers 1 (general 0, family 1), should fix 10 (general 6, family 4), polish accepted 17

# song-form-builder: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.
The Teaching lens checked all six Listen songs note for note against its own transcriptions: all correct and public
domain. No rule-5 content, so no sensitivity agent.

## Blockers
1. **Rests get no time** (C-B1; family:music-studio). src.html:716 `startPlay` never passes `beats` to `MS.play`,
   so an all-rest block and trailing rests are skipped: Blank starter with A A ends after the lead-in, Hear on an
   all-rest section ends in 0.1 s, a five-beat trailing rest cuts 8.5 s to 6.2 s and the playhead never reaches it.
   The spec's edge case says an all-rest block plays 8 beats of silence. Fix in the tool, and make the engine
   default safe (beats from the block length when not given) and say so in docs/families/music-studio.md.

## Should fix
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

## Polish accepted
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

## Spec open questions (not for the builder)
- An invitation to build AABA or a rondo (P polish; adds to the spec).

## Settled calls
- The Listen songs are public domain and checked note for note; no sensitivity look needed (the builder's flag is closed).

## Exit check, round 1

Fresh cold agent, 2026-10-28. Bundle `CURIO_DRAFT=1`: 106 KB, clean. Driven with `scripts/drive.py` (held clicks,
0.12 s) on port 9932, plus one Chrome on 9934 without the autoplay flag; frames and logs in the exit scratch folder
(`exit-sfb/out`, `exit-sfb/audit`). No console errors or exceptions in any tool run (one exception came from my own
test calling `place('C')` before C existed, not reachable from the UI). No network requests (resource list empty).
`allLines()` and voice/lines.json: 59 and 59, word for word. No em dashes; "Curio" only as `Curio.` in code.

### Items
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

### Regressions looked for
Default screen at every size (audit frames), Build at 1366 and 1920 mid-play, the editor at 680x425, Listen mid-song,
the Start over question, Listen done at 760: nothing clipped or overlapping, no new console errors.

### Gate
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

### Left open (nits, not blocking)
- kit/music-studio.js `play`: the audio clock is used only when `ctx().state` is 'running' at that instant. Chrome
  reports 'running' synchronously inside a tap (checked without the autoplay flag: 17 oscillators on the first Play),
  but some browsers report a context made in the same call as 'suspended' until a tick later, which would make the
  very first Play silent there. Unverified; worth a look on Safari and Firefox in Final look. family:music-studio.
- Listen: pressing Stop during the short "Yes!" pause moves to the next part without playing it (the student then
  presses Hear it again). general.
- Known from round 1, not accepted: Tab order (Instrument and Done before the grid), one AudioContext shared with the
  kit, held notes in `rows`.

### Audit pilot
- Leads confirmed: none were faults. The eight "below the fold" leads are real positions (Starter songs and Clear
  song at 680x425 and 800x500; Speed, Starter songs and Clear song at 375) but they are occasional controls under the
  main ones, which all show (Done when 8).
- Leads wrong: the eight above as faults (it cannot tell a main control from an occasional one).
- Clean rows confirmed: Motion off, focus on load, the one-click walk (no rebuild under the pointer), the 2 s
  five-click runs (playHow, editHow once; emptyStrip five).
- It missed: everything past one click (Listen answers, compare timing, the twin editor line, linked after Done,
  playHow while a block is picked, Clear's save, the grid focus ring, all-rest timing, the engine's multi-player stop),
  which is where all of round 1's items lived.
