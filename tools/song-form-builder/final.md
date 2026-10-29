PASS
Counts: blockers 0, should fix 0, polish 5 (general 4, family 1)

# song-form-builder: Final look

Fresh cold agent, 2026-10-29. Bundle `tools/song-form-builder/song-form-builder.html`, 1,269,980 bytes (built
11:28, after src.html 07:35 and the clips 07:53, so current; not rebuilt). Driven with `scripts/drive.py`, held
clicks (0.12 s), Chrome on 9221 and 9222, iframe host on 8813 for 375. Frames, logs and scripts in
`S:/CurioClass-codex-scratch/final/song-form-builder/` (out1 default frames, out2 voice runs, out3 state frames,
out4 pace and Read runs). Every page was instrumented: each clip's start, end and cut (matched to its text by a
fingerprint of the bundled data URI), every `MS.play` start and end, and whether a clip was playing when music
started (`talking`) or music was playing when a clip started (`music`). No art: everything is drawn in code, so
step 2 (art against the spec) has nothing to check. No rule-5 content and no people, so no sensitivity agent.

## 1. Frames

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

## 2. Art

None in the tool (`art/prompts.json` has no entries; no `art:` tokens). Nothing to check.

## 3. Voice with the real clips

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

## 4. Full runs

As a solo student at 1366 (A_build, pace2_build, B_listen): the welcome names the shelf and the strip, playHow comes
when the strip has blocks, the form line lands right after the song, the end glow and A lifts show the shape. In
Listen the Yes / Not quite rhythm with the real voice feels lively; waits between parts are short (0.45 to 0.6 s).
As a teacher projecting at 1920x1080 (`buildmid_1920`, `full_1920`, `ldone_calm_1920`): letters and Form card are
large and readable; the lower half of the stage is empty (polish 4). At 375 (host) everything a student uses is in
order, top to bottom.

## 5. Contract

Bundle 1.27 MB with all 59 clips (under 2 MB). No console errors or exceptions in any tool run (the only messages
were the iframe host's own favicon 404 on port 8813, not the tool). No network requests
(`performance.getEntriesByType('resource')` empty). No em dashes in src.html or notes.md; privacy line on screen
("Your song is saved on this device only. Nothing leaves it.").

## Findings

### Blockers
None.

### Should fix
None.

### Polish
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

### Left open from Refine (not checked here)
- The Safari / Firefox first-Play question (audio context reported 'suspended' in the same tap) needs a non-Chrome
  browser; only Chrome was available. family:music-studio.
- At 375 the editor grid starts below the fold (`h375_editor`, one row shows); the student scrolls. Unchanged since
  Refine, where Done when 8 covered the strip, Play song and the Form card.
