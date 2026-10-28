# Craft lens: biased-bot (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json; family doc docs/families/ml-lab.md and
the engine description in tools/teach-the-robot/spec.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
biased-bot` (177 KB). Ran scripts/audit_tool.py first, then drive.py shots at 1366x768, 1920x1080, 800x500, 760x900,
680x425 and 375x812 through `drive.py --host`.

Counts: blockers 0, should fix 2 (general 2, family 0), polish 7 (general 5, family 2), nits 2 (general 2)

## Contract (passes)

- One file, 177 KB, no network requests (the only URL in the bundle is the SVG namespace; no fetch, XHR, socket or
  beacon). No console errors or exceptions in any tool shot.
- Kit used for voice, motion, sound, chimes (`Curio.voice`, `Curio.wait`, `Curio.yes`). Engine used as the family
  doc says: `MLLab.rng` and `uni` for the cards, `train('knn', k 3, 64 grid features)`, `knn` for the pad read,
  `evaluate` with `groupBy` room, `view.groupBars`, `glyph`. The rasterizer and templates stay in the tool, as the
  spec says. Nothing re-implemented.
- `__tool.checkTable()` reproduces every row of the spec's results table, including 3/0/0 = 10, 10, 5 and the miss
  lists (Room 9's four 1s read as 4; 0/15/0 reads the other rooms' 1s as 7). Real clicks: start run = 10, 10, 6 with
  "Room 9: wrote 1, got tacos (4), 4 cards".
- Saving and reset: nothing is stored except the kit's `curio-motion` key. Privacy is stated on screen in both modes
  (rule 7). Start over clears jars, results, My cards, the pad and the "all right" flag, and speaks the ready hint.

## Should fix

1. **Focus lost when a jar hits its limit.** src.html:85 (`update`, `disabled('fewer-'+r ...)` / `'more-'+r`) sets
   the real `disabled` attribute on the button that has focus. Five presses of Room 12 More (to 30), by held click or
   by Enter, leave `document.activeElement` = BODY; the same for Fewer at 0 (shots b-more30, c-fewer0, kb-more). The
   focus ring disappears and a keyboard user's next Enter does nothing. Train and Run already use `aria-disabled` to
   keep focus; do the same here (or move focus to the jar's other button). BR1 lesson "Focus is kept when controls
   rebuild". **general**
2. **Tapping the current mode button cuts the welcome for good.** src.html:101 `setMode` always runs `V.hush()` and
   re-enters, even when `m === state.mode`. Tap the stage (welcome starts at 1.3 s), tap Lunch Line 1.5 s later: the
   log shows `lunchWelcome spoken`, then at 3.0 s `story dropped (hush)` and `story spoken`; the 8 s welcome was cut
   after about 1.6 s and, being marked said, never returns (shot same-mode-tap). Same with Tab then Enter on a fresh
   page (Tab counts as the first key, the welcome starts, Enter on Lunch Line cuts it 80 ms in: v-ft-key), and in
   Try Your Writing (writingWelcome cut, readHow restarted). Return early when the mode is unchanged. **general**

## Polish

3. **Engine: views draw at zero size.** kit/ml-lab.js:244 `host()` draws at `max(60, size)` when its element is
   hidden, and groupBars then makes negative widths: a `display:none` groupBars logs "attribute width: A negative value
   is not valid (-32)" (shot zero-size). This tool never hits it only because it parks `#results` off screen with
   `visibility:hidden` in write mode (src.html:16, `body.write-mode #results{position:absolute;top:-10000px;...}`)
   instead of hiding it. Engine change: skip drawing while the box is 0 wide or high and draw on the first real size
   (the ResizeObserver already fires then); clamp bar widths at 0. Then the tool can hide `#results` plainly. Update
   ml-lab.md in the same change. **family:ml-lab**
4. **groupBars before a run reads "0 of 0 right lunches" three times** (1366 default frame), and the tool forces its
   text size with `#bars text{font-size:11px!important}` (src.html:16) because the view has fixed 13 and 12 px text.
   Better: an `empty` text option ("No run yet") and a `size` option in groupBars, so siblings don't override with
   `!important`. **family:ml-lab**
5. **"− Fewer" wraps to two lines** ("−" over "Fewer") in every jar at 680x425, 1366x768 and 1920x1080 (the buttons
   are 44 to 50 px wide in a 350 px panel), while "+ More" fits on one. Better: icon-only minus and plus with the
   word under the jar, or "Fewer" without the sign. **general**
6. **Tray and "Wanted pasta" sticker sit on Bitsy's wheels** at 1366x768 and 1920x1080 (shots mixup-frame, s-1920:
   tray `ty = min(H-48, ry+70*rs)`, src.html:121). The mix-up, the moment the lesson hangs on, is half hidden.
   Better: place the tray beside the robot's slot side, clear of the body. **general**
7. **Full-size queue jumps and forgets.** src.html:117 `start=state.running?Math.min(20,Math.floor(state.done/10)*10):0`
   applies when not compact too, so at 1366x768 the 30-card queue drops to cards 11 to 30 once 10 are served ("13 of
   30 served" shows 20 cards), then snaps back to all 30 at the end; after a run no card shows whether it was read
   right. Better: keep all 30 when they fit, and mark each served card with a small tick or the food it got (shape,
   not color). **general**
8. **Keyboard pen and screen readers miss the read.** Lifting the keyboard pen (Space, src.html:149) never calls
   `hint(true)`, so a keyboard student never hears "Press Bitsy, read it!" (the pointer path does, on pointerup);
   and `#guess` ("Bitsy reads: 4") is not live, so with Sound off a screen reader gets only "Compare the three
   look-alikes", not the guess. Better: speak the how on pen lift; put the guess in the live hint or make `#guess`
   `aria-live`. **general**
9. **Lunch-line card badges are tiny with color off.** The queue cards carry only an 8 px glyph (r = 4, src.html:117)
   and no name; in a grayscale frame at 680x425 and 375 the circle and square are hard to tell apart. Done when 7
   still passes through the jars, bars and viewer (shot s-gray). Better: badge radius 6 or more, or a room number
   under each card in the wide layout. **general**

## Nits

10. "Room 9 got 1 right lunches out of 10." (and Room 12 / Room 3 at 1): the fixed lines for 1 say "lunches"; the
    bars say "1 of 1 right lunches" early in a run. "1 right lunch". Lines and voice/lines.json together. **general**
11. The pad canvas is `role="img"` but takes keys (src.html:20); `role="application"` with the same label tells a
    screen reader it is interactive. **general**

## Access (passes, except items 1, 8)

Tab order: Lunch Line, Try Your Writing, Motion, Sound, Read, Train, Run, then each jar and its live buttons, Start
over (disabled Fewer buttons skipped). Visible 3 px focus ring. The viewer takes focus on Close, traps Tab between
Close and the card grid, Escape closes it and returns focus to its jar. Skip moves focus to Run when it disappears;
Stop keeps focus (same button). Train keeps focus while busy (`aria-disabled`). Nothing takes focus on load. Audit:
no target under 44 px at any size. Rooms are shape plus name in jars, bars, viewer and look-alikes.

## Lines (pass)

`__tool.allLines()` returns 58 lines and voice/lines.json holds the same 58, word for word, in the same order. Spec
lines 1 to 11 match the code text exactly; the 17 extra hint lines are the panel hints Read speaks. No em dashes in
src.html, notes.md, lines.json or tool.draft.json; "Curio Class" never shortened in text. Every line under 200
characters. Each spoken line was compared with the frame state in the runs below; none names a hidden or disabled
control (`needs` on every how line; `under` needs `#jar-9`).

## Standard voice check (1366x768, Sound on, Motion on, held clicks 120 ms)

| Line | Kind | Action x5 | Expected | Spoken |
|---|---|---|---|---|
| change "Press Train Bitsy, then run..." | how | More (Room 9) x5, gap 4 s | 1 | 1 |
| Room 12 got 10 / Room 3 got 10 / Room 9 got 6 | event | Run + Skip x5, gap 14 s | 5 each | 5 each |
| under "Some students got the wrong lunch..." | event | same runs | 5 | 5 |
| read1 "Bitsy read a 1." | event | Bitsy, read it! x5, gap 4 s | 5 | 5 |
| teachHow "If Bitsy got it wrong..." | how | same | 1 | 1 |
| learned "Bitsy learned your card." | event | It's a 7 x5, gap 4 s | 5 | 5 |
| same "More cards from the same rooms..." | event | Room 12 to 30, Train, Run (real clicks) | 1 | 1 |
| all "Every room got the right lunch..." | event | 15/6/0 run | 1 | 1 |
| flip "Now a different room..." | event | 0/15/0 after all-right | 1 | 1 |
| inspectEmpty (viewer on an empty jar) | how | first tap on Room 9 jar | 1 | 1 |

- Stale (gap 0.2 s: Run, Skip, More, Train, Try Your Writing, Lunch Line, Start over): Room 3 and Room 9 results and
  under dropped by hush at the More tap; lunchWelcome and story dropped stale on return (results exist); "ready"
  spoken after Start over, matching the screen. No line played after its moment.
- First tap: stage tap gives lunchWelcome at 0.15 s, then story; Run (a `speaks` button) gives nothing until its
  results; Try Your Writing gives only writingWelcome; a jar gives only its viewer line; Read speaks the hint only;
  Sound says nothing, and Sound back on brings lunchWelcome once. Tab then Enter: see should-fix 2.
- Read: Read during the welcome cuts it and speaks the hint (story dropped); with Sound off Read still speaks; a mode
  change right after Read starts writingWelcome at once.
- Order: every run's lines follow the actions in order.
- Audit walk (five clicks 2 s apart on every speaking control): clean.

## Layout (passes)

Run, Train Bitsy and every jar button are on screen without scrolling at 680x425, 800x500, 1000x625, 1280x720,
1366x768, 1920x1080, 760x900 and 375x812 (host). The hint is unclipped at all of them. In Try Your Writing the pad,
Bitsy read it and the teach buttons are on screen at 375 (pad top 319, 300 px), and the read scrolls the sight panel
into view at 680x425. Results scroll inside the panel in the 680x425 preview and at 375, as the notes say. Motion off:
no animations at all 2.5 s into a run.

Frames looked at: audit size-* and calm frames; f1 a to m; f2 s-write-375ish, s-write-1366, s-write-760,
s-midrun-680, s-midrun-1366, s-viewer9-1366, s-gray, s-1920; f3 h375-write, h375-results, h375-viewer; f5
mixup-frame (scratch folder lens-bb-craft).

## Audit pilot

- Confirmed: none of its 11 leads were real. All 11 were the 375 overlaps between the scrolled results panel and the
  stage SVG text; the panel clips its overflow, so they are false (frame size-375x812). Its clean rows for targets,
  fold, hint, focus on load, Motion off and the five-click voice walk matched my own runs.
- Missed (needs more than one click or a look at the frame): focus lost when More reaches 30 or Fewer reaches 0;
  re-tapping the current mode cutting the welcome; the engine's zero-size drawing; the tray and sticker over Bitsy
  mid-run; the wrapped "− Fewer" label (wrapped, not clipped). It could test a disabled-under-focus check after
  repeated clicks and a same-mode re-tap, and should ignore overlaps that a scrolling ancestor clips.
