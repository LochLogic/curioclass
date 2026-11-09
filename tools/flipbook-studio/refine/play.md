# Play lens: flipbook-studio (round 1)

Played twice: as a grade 7 student alone at home (blank book first, then the starters), and as a teacher projecting
at 1366x768 and 1920x1080. Frames are in `S:/CurioClass-codex-scratch/flipbook-studio/play/out/` (mine) and
`S:/CurioClass-codex-scratch/flipbook-studio/audit-r1/` (shared audit). Driven with `scripts/drive.py`, held clicks
(0.12 s), real drags on the page and on the hold handles.

What works well: the first screen invites a mark ("A little mark. A little motion."), the onion ghost arrives with
its own line right after New page or Copy page (d1-drawn-new, d2-copy: welcomeDraw dropped at the first stroke,
onionHow spoken once), the Real bounce spacing chart reads at a glance (state-bounce-time-1366x768), a hold drag while
the book loops changes timing at once and speaks holdChanged (t3-drag-while-playing), Ping-pong turns at both ends
without a doubled end drawing (t6-ping: 11,10 ... 1,0,1), and 24 per second keeps time (t5-24fps: 123 frames in
5115.6 ms against 5125 ms expected, under one frame). Print repeats held drawings (p1-print: Blink prints 11 cards,
8 + 1 + 1 + 1, numbered, staple margin, no paper texture).

## Findings

1. **Time mode, `-` / `+` and `Hold the key` while playing (src.html:1504-1505, 1146; `page()` follows the playing
   drawing).** While the book loops, the selected drawing is whichever one is on screen, so `+` changes a drawing
   picked by chance, and the `×N` readout between the buttons flickers with every drawing. Three `+` taps 2.5 s apart
   on Even bounce raised drawings 2, 8 and 12 (holds `1,2,1,1,1,1,1,2,1,1,1,2`), none of them chosen. `Hold the key`
   has the same problem. The spec says everything stays live while playing, and the handles do, but these two
   controls become a lottery, and they are the keyboard path to holds. Better: while playing, `-`, `+` and `Hold the
   key` act on the drawing the student last selected (keep a separate selection from the playing index), or name the
   drawing on the button area ("Drawing 5: ×1"). Seen: t9-hold-plus-playing.png and its log. **should fix**,
   general.

2. **Starter loaded: the hint and the spoken line say different things (src.html:1028-1029).** After Real bounce the
   voice says "Press Play, then load the other bounce from Starters and compare." The hint says "Tap Play to watch.
   Tap Time, then drag the hold handles." Read speaks the hint, so the Real versus Even comparison (the tool's core
   contrast) is never on screen, and a student with Sound off never meets it. Better: one sentence shown and spoken,
   and the compare step kept (for example the spoken line as the hint, with Time named after the compare). Seen:
   s1-starter-real-hint log (starterBounce spoken, hint differs). **should fix**, general (anything shown twice
   matches).

3. **Hint while playing names the mode you are in (src.html:528).** In Time, pressing Play sets the hint to "Drag a
   hold handle or tap Time to change the feel." Time is already pressed. Words should match the state: in Time,
   "Drag a hold handle or tap a preset to change the feel. Tap Stop to pause."; in Draw and Flip the current line
   fits. Seen: t4-time-playing-hint. **should fix**, general.

4. **Flip has no focus of its own (spec, Screens and modes: "the page fills the stage").** Flip lays out exactly like
   Draw: same page size, same strip at the same height, only the panel buttons change (state-mode-flip-1366x768,
   f1-flip-playing, state-live-flip-1920x1080). The spec's Flip is "the page alone, as big as the stage allows", the
   watching moment. Done when 6 still passes (the page is the biggest thing), so this is a missed moment, not a
   break. Better: in Flip shrink the strip to a slim progress row (numbers and the playing marker) and give the page
   the height. **polish**, family:none (this tool).

5. **Empty book: Time and Flip invite Play on nothing (src.html:538-541).** A student who opens Flip or Time first on
   the blank book is told "Press Play to flip the book" or "Drag a hold handle ... Then press Play"; Play runs a
   single blank page with ticks, then the playing hint asks them to drag a hold handle (f2-empty-flip, f3-empty-time).
   Better: when no drawing has strokes, the hint in Time and Flip says "Draw on the page in Draw, or tap Starters for a
   ready-made book." **polish**, general.

6. **A first tap on New page, Copy page, Delete page or Clear page on the blank page gets no line (audit lead,
   confirmed in code: insertPage and the delete/clear handlers set `drawTouched`, so `welcomeValid` fails, and with a
   blank previous page there is no onionHow).** The hint still shows welcomeDraw, so the screen is right; only the
   spoken premise is lost for a student who starts on a button. Mild; Draw is mostly entered by drawing. **polish**,
   general.

7. **Try this, card 1 has no first move with the hold controls (why dialog, "fewer frames at the top").** Real
   bounce is already all on ones, so the hold handles cannot give the top fewer frames; the student must think of On
   twos first, or delete drawings. A grade 7 student alone tried the handles, hit 1, and stops. Better: "Start on
   twos, then give the top drawings 1 frame and the floor drawing 4." Also each card could carry a "Load Real bounce"
   style button; now the student must close the dialog, open Starters and confirm the replace. Seen:
   state-timing-help-1366x768. **polish**, family:none.

8. **Projected, the numbers that teach are the smallest text (readout 12 px, hint 13 px at every size).** At
   1920x1080 the readout "12 drawings, 12 frames, 1.0 seconds at 12 per second" is the line a teacher points at, and
   it is 12 px under a 1600 px stage (state-live-flip-1920x1080). Better: scale `#readout` and `#hint` up on large
   windows (about 16 px at 1920). **polish**, general.

9. **Compact sizes: the lone `Tools` / `Timing` / `Options` button is a half-width cell beside empty space, and
   Undo hides inside it (680x425, 800x500).** Undo is a control a drawer uses every few seconds; at the preview size
   it is two taps away (size-680x425, state-mode-flip-680x425, state-bounce-time-680x425). Better: put Undo next to
   Tools on that row (the space is there). **polish**, general.

10. **Drawing while the book plays does nothing and says nothing.** In Draw with Play on, the cursor stays a
    crosshair and a stroke is silently ignored (src.html:1320); the hint talks about holds. Better: a not-allowed
    cursor while playing, or the hint "Tap Stop to draw." **nit**, general.

Nothing found on: the default screen at every size, every mode button, the extremes (hold ×6, hold ×1, 6 and 24 per
second, 48 drawings, Blink's ×8 starter hold with its "starter" label), Motion off, the starter library, Ping-pong,
Step and Back, the onion legend (solid before, dashed after reads without color).

## Audit pilot

- **Confirmed:** welcome not heard after a first tap on New page, Copy page, Delete page, Clear page and Play
  (finding 6; Play on a blank book is finding 5). Eraser "not heard" is fine: it speaks its own line. Starters and New
  book "cut (hush)" are fine: they open a dialog, and the starter line follows.
- **Wrong:** "count and word disagree: 1 seconds" matched inside "0.1 seconds"; the readout's plural is right.
  "Choices cut short by a scroll panel" on `#film` is the drawing strip, which scrolls sideways by design (spec) and
  keeps the selected tile in view; it is not a short choice set. The keep-region leads on starter-library and
  timing-help are the modal dialogs covering the page, as expected.
- **Missed:** `-`, `+` and Hold the key hitting whichever drawing is playing (finding 1, the worst); the starter hint
  and spoken line disagreeing (2); "tap Time" shown while in Time (3); Flip with no layout of its own (4); empty-book
  Play (5); the Try this card with no first move (7). None of these is mechanical: each needs a run with a goal in
  mind.
