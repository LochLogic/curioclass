PASS (exit check 2026-11-06)
Counts: blockers 0 (general 0, family 0), should fix 9 (general 8, family 1), polish accepted 14

# Refine: flipbook-studio

Lens files: `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity file; no lens found a sensitive
topic). Not a Curiosity: judged as a lesson tool. Frame roots: Teaching `S:/CurioClass-codex-scratch/flipbook-studio/teaching/frames/`,
Play `S:/CurioClass-codex-scratch/flipbook-studio/play/out/`, Craft `S:/CurioClass-codex-scratch/flipbook-studio/craft/frames/`,
shared audit `S:/CurioClass-codex-scratch/flipbook-studio/audit-r1/`. Integrator spot-checked items 1, 3 and 4 in
src.html (confirmed: the play loop moves `state.index` at src.html:1190 and `-`/`+` act on `page()` =
`state.pages[state.index]`; `save()` catch calls `V.say('tooBig')` on every failed save; `printBook()` hushes in
`finally` right after `window.print()`).

## Blocker
(none)

## Should fix
1. **`-`, `+` and `Hold the key` hit whichever drawing is playing.** src.html:1504-1505 (`changeHold(page().hold±1)`),
   preset `key` src.html:1146; the play loop sets `state.index` (src.html:1190). While the book loops, three `+` taps on
   Even bounce raised drawings 2, 8 and 12, none chosen; the `xN` readout between the buttons flickers. Seen:
   `play/out/t9-hold-plus-playing.png` and its log. Fixed: keep a selected drawing separate from the playing index;
   while playing, `-`, `+` and `Hold the key` act on the drawing the student last selected, and the readout between
   the buttons names it ("Drawing 5: x1") and stays still. Hold handle drags already work and must keep working. (general)
2. **On ones and on twos are taught at film's 24 per second, but every starter runs at 12.** Why note src.html:457-460,
   preset `twos` src.html:1144, notes.md "A 5-minute start". On twos at 12 gives 6 new drawings a second: the Real
   bounce just plays slow and choppy, the opposite of "still look smooth". Seen: `teaching/frames/t9-twos-12.png`,
   `audit-r1/state-timing-help-1366x768.png`. Fixed: say it where the student acts. Why note gains a sentence like
   "At 12 per second, this book on ones already looks like film on twos. To see film's twos, tap 24, then On twos."
   After the On twos preset at 12 per second or less, the hint names the result ("On twos at 12 per second: 6 new
   drawings a second. Tap 24 to see film's twos."). notes.md's 5-minute start says the same (tap 24 first). Do not
   change the starters' fps (see open questions). (general)
3. **`tooBig` is spoken again on every change while storage fails.** src.html:557-564 `save()` catch. With setItem
   throwing, five actions 2.5 s apart spoke it 5 times (twice within 170 ms) and pushed out onionHow both times.
   Seen: `craft/frames/f1-toobig` and log. Fixed: speak it once per failure run; speak again only after a save has
   worked and then failed again (the footer warning and hint stay). Students on locked-down school browsers hit this
   on every mark. (general)
4. **The `printed` line can never be heard.** src.html:1416-1424 `printBook()`: `V.say` queues, `window.print()` blocks,
   then `finally { finishPrint() }` runs `V.hush()` before the line starts. Seen: `craft/frames/b7-print` log
   "printed dropped hush". Fixed: speak the line before opening print (start print after the line has begun, e.g. a
   short timeout or awaiting the line start), or speak it after `afterprint` as the next step; either way the hint
   and the line say the same words. (general)
5. **Starter loaded: the hint and the spoken line disagree.** src.html:1028-1029. Real/Even bounce speak "Press Play,
   then load the other bounce from Starters and compare." while the hint shows "Tap Play to watch. Tap Time, then
   drag the hold handles." Read speaks the hint, so the Real versus Even comparison (the core contrast) never shows,
   and a student with Sound off never meets it. Seen: `play/out/s1-starter-real-hint` log. Fixed: one sentence,
   shown and spoken: the hint shows the starterBounce line (keep the compare step). (general)
6. **The bowling ball Try this card asks for a move the hold controls cannot make.** src.html:466. Real bounce holds
   all start at 1, so "fewer frames at the top" gives "This hold is already 1 frame" (src.html:1119-1124) and a solo
   student stops. Seen: tried by Teaching and Play; `audit-r1/state-timing-help-1366x768.png`. Fixed: give the card a
   first move with the hold controls, e.g. "Make the Real bounce feel like a bowling ball: tap On twos, then give the
   top drawings 1 frame and the floor drawings 4." (Play's wording; it keeps the card about timing only). Update the
   same card in notes.md if it is there. (family:flipbook, merged with Play 7 tagged family:none)
7. **"Hold the key" uses a word the tool never teaches, and nothing asks the student to plan (MA:Cr2.1).** src.html:341
   and the Why dialog. Cr2.1.6-8 is "organize/design, propose, and evaluate ... plans"; the tool has organizing and
   evaluating but no planning step, and "key" is undefined. Seen: code read of every control and card. Fixed: one Why
   sentence defining a key drawing (the drawings that mark where a move starts, turns and ends; Williams, "Keys,
   extremes and breakdowns") and one Try this card that plans before drawing, e.g. "Plan a jump: draw the start, the
   top and the landing first (your keys), then add the drawings in between with onion skin, closer together near the
   top." Add the matching line in notes.md and the source. (general)
8. **The playing hint says "tap Time" while in Time, and says nothing about drawing while playing.** src.html:528.
   Seen: `play/out/t4-time-playing-hint`. Fixed: the playing hint follows the mode. In Time: "Drag a hold handle or
   tap a preset to change the feel. Tap Stop to pause." In Draw: "Tap Stop to draw." (a stroke is silently ignored
   while playing, src.html:1320; also show a not-allowed cursor on the page while playing). In Flip the current line
   fits. (general; folds in Play nit 10)
9. **Empty-state line fails contrast.** `#empty span`, src.html:91-94: #84786a on #fbf6ea at 12 px is 3.99:1 (under
   4.5:1, paper grain lowers it more). Seen: `craft/frames/a-default-1366`. Fixed: use the spec's muted #6b6258
   (5.54:1). (general)

## Polish accepted
10. **Flip gets its own layout.** Spec: Flip is "the page alone, as big as the stage allows"; now it lays out exactly
    like Draw (`audit-r1/state-mode-flip-1366x768.png`, `play/out/f1-flip-playing`). In Flip, shrink the strip to a slim
    progress row (numbers and the playing marker) and give the page the height. Keep Done when 6 and 10. (family:none)
11. **Empty book: Time and Flip invite Play on nothing.** src.html:538-541 (`play/out/f2-empty-flip`, `f3-empty-time`).
    When no drawing has strokes, the hint in Time and Flip says "Draw on the page in Draw, or tap Starters for a
    ready-made book." (general)
12. **Blink spacing chart shows one stray dot.** drawChart src.html:650; all four centers are (480, 350)
    (`teaching/frames/t7-blink-time.png`). When every dot coincides, draw one dot and a caption: "These drawings do not
    travel: the change is in shape, so timing does all the work." (family:flipbook)
13. **Ease the ends on a loop slows only one top.** preset `ease` src.html:1145. After the preset, the hint says what it
    did: "Ease the ends slowed the first and last drawings of the book. For a bounce, hold each top drawing longer by
    hand." (family:flipbook)
14. **Readout and hint are the smallest text when projected.** `#readout` 12 px, `#hint` 13 px at every size
    (`audit-r1/state-live-flip-1920x1080.png`). Scale both up on large windows, about 16 px at 1920 wide. (general)
15. **Compact sizes hide Undo inside Tools.** 680x425 and 800x500 (`audit-r1/size-680x425.png`,
    `state-mode-flip-680x425.png`): the lone Tools/Timing/Options button sits beside empty space. Put Undo next to
    Tools on that row. (general)
16. **Blue pencil matches the onion "before" ghost; Red matches the chart.** Blue pencil and onion before are both
    #2f6fd6; Red and the chart are both #c8341a (`craft/frames/e1-blue-pencil-onion`, `e2-red-pencil-chart`). Shift
    Blue pencil to an indigo or cyan clearly apart from the ghost (keep it at or above 3:1 on the page), and give the
    chart dots a light outline ring so they read as an overlay; the chart stays in the accent (spec Look). (family:drawing)
17. **Heavy books get slow.** `changed()` repaints all thumbnails; `save()` writes the whole book on every stroke end,
    hold step and reorder; points saved at full float precision (src.html:1305-1308). At the spec's limits a render
    took 67 ms, a reorder 109 ms, the save 3.86 M characters (`craft/frames/d1-heavy`). Repaint only the changed
    thumbnail, round saved points to 0.1 unit, debounce the save during a drag. Old saved books must still load.
    (general)
18. **notes.md says "the spec".** "Good to know": rewrite as "The Blink starter opens with an 8-frame hold on its first
    drawing (a calm blink). Editing it switches to the 1 to 6 frame range." (general)
19. **notes.md Support at home: a rolled ball does not start slow.** Replace with "Drop a ball and let it bounce. Watch
    where it seems to hang at the top and where it rushes at the floor, then compare with Real bounce." (general)
20. **Nit: "twos are half the drawing".** src.html:459: "half the drawings". (general)
21. **Nit: a missed erase still pushes an undo step.** src.html:1331-1334: push only when a stroke is removed, so Undo
    never appears to do nothing. (general)
22. **Nit: tapping the hold track rounds to the wrong cell.** src.html:885 `Math.round(x/15)`: use the cell tapped
    (`Math.ceil`, clamped 1 to 6); handle drag unchanged. (family:drawing)
23. **Nit: canvas label promises arrow keys on an unfocusable canvas.** src.html:369: reword to match (e.g. "Arrow keys
    Left and Right step pages") or make the stage focusable; arrows already work from the page. (general)

## Settled calls
- Welcome after a first tap on New page, Copy page, Delete page or Clear page (Play 6, audit lead): not a bug. The spec
  makes welcomeDraw stale when a page button is tapped, and the hint still shows it. Do not change.
- Audit leads "count and word disagree: 1 seconds" (it read "0.1 seconds"), keep-region covered in starter-library and
  timing-help (modal dialogs), and "choices cut short" on `#film` (the strip scrolls sideways by spec): all three lenses
  agree these are wrong. Do not change.
- Bowling card wording (item 6): Teaching offered "delete one top drawing in Draw", Play "start on twos". Took Play's,
  so the card stays about timing with the hold controls, as the Even bounce card is.
- Ones/twos (item 2): fixed in words and hints, not by changing the starters' fps (that is a Content change).
- Chart color (item 16): the spec puts the chart in the accent; fix by outlining dots and moving Blue pencil, not by
  recoloring the chart.
- Keep: the voice line set (12 lines, matched both ways), Ping-pong without a doubled end drawing, the 24 per second
  clock, print with repeated held drawings, Motion off and Read behavior. All lenses passed these.

## To the spec's open questions
- Should the bounce starters open at 24 per second on twos, so "on twos" is true by default (Teaching 1)? This changes
  Content and every readout check in Done when 3.
- If the planning Try this card (item 7) is judged too thin for MA:Cr2.1.6-8, give Cr2.1 a 6-8 home in another tool of
  the module (storyboard-studio is 9-12) per BASELINE rule 2.

## Not taken
- Teaching 4, an intent goal in the Blink starter line and a Try this card shown in Time: changes a spoken line (voice
  regen) and adds panel content; the Blink card already asks "calm or startled?". Revisit in round 2 if Teaching still flags it.
- Play 7 second half, a "Load Real bounce" button on each Try this card: new controls in the dialog, not needed once
  the card has a first move.
- Craft nit 9, 10 to 11 px labels: all pass contrast; a size pass across the tool is not cheap or clearly right here.

## Exit check (2026-11-06)

Cold exit check by Claude on the current bundle (232,975 bytes). Fresh audit: `S:/CurioClass-codex-scratch/flipbook-studio/exit/audit-r2/`
(Chrome 9731, host 8914, exit 0). Own frames and logs: `S:/CurioClass-codex-scratch/flipbook-studio/exit/frames/` and
`exit/x*.json` (shots in `exit/shots.json`, real held clicks at 1366x768 unless named).

### Should fix
1. FIXED. Even bounce, drawing 5 selected, Time, playing, three held `+` taps 0.4 s apart: holds became
   `[1,1,1,1,4,1,1,1,1,1,1,1]` while the playing index was elsewhere (11). The readout sampled every 50 ms read only
   "Drawing 5: x1" to "x4", no flicker to other drawings (`x1-plus-playing.png`, `x1.json`). Hold the key then `-` while
   playing on Real bounce drawing 3 changed only drawing 3 (`x1b.json`). A real handle drag on drawing 4 still sets 5.
2. FIXED. On twos at 12 shows "On twos at 12 per second: 6 new drawings a second. Tap 24 to see film's twos." (`x2.json`).
   Why note has the "At 12 per second ... tap 24, then On twos" sentence (`x2-why.png`, src.html:476-479); notes.md
   5-minute start says tap 24 first. Starters stay at 12.
3. FIXED. setItem throwing, five held actions 2.5 s apart (hold, hold, Copy page, hold, hold): tooBig spoken once; after a
   good save and a new failure, once more (`x3.json`). Footer warning stays.
4. FIXED. Real Print path (headless Chrome): "printed" logged as spoken, printing false after, hint the same words
   (`x4.json`). `finishPrint()` no longer hushes; print waits for the line when Sound is on.
5. FIXED. Real bounce from the Starters dialog: hint and spoken line are both the starterBounce sentence with the compare
   step (`x5.json`).
6. FIXED. Card reads "tap On twos, then give the top drawings 1 frame and the floor drawings 4." After On twos every hold is
   2, so 1 and 4 are both reachable; tops (y 140) are drawings 1 and 7, floors (y 632) 4 and 10 (`x6.json`). notes.md matches.
7. FIXED. Why defines key drawings; "Plan a jump" card present in bundle and notes.md, with the Williams source.
8. FIXED. Playing hints: Draw "Tap Stop to draw." with cursor not-allowed; Time "Drag a hold handle or tap a preset ...";
   Flip keeps its line (`x8a/b/c.json`).
9. FIXED. `#empty span` color #6b6258 (src.html:111).

Fixed: 9 of 9 should-fix. Polish spot-checked in bulk: 10 (Flip slim numbered strip, page fills the stage,
`r-1920-flip.png`), 11 (empty hint src.html:568), 12 (one ringed dot plus caption, `r-blink-time.png`), 13 (ease hint
src.html:1244), 15 (Undo beside Tools at 680x425, `r-compact-680.png`), 16 (Blue pencil #3b3da8), 20, 22 (`Math.ceil` on
track tap), 23 (canvas label) all present. 14, 17, 18, 19, 21 taken on polish.md's evidence and a notes.md read; not re-measured.

### Regressions
None found. Default screen, Time (playing and Blink), Flip at 1920x1080 and the 680x425 compact layout look right; no
console errors in any of 16 driven shots or the audit.

### Gate
1. Done when: the checks tied to the fixes pass (readout arithmetic, holds 1 to 6, Flip page size, print); nothing else
   changed since round 1 lenses passed them. Pass.
2. Codes: MA:Cr2.1.6-8 now has a planning card and key drawings taught; Cr3.1 and Pr5.1 unchanged. Pass.
3. Solo defaults: starters, hints and the bowling card all lead to a doable next move. Pass.
4. Sensitivity: not required (no lens found a sensitive topic). Pass.
5. No blocker or should-fix open. Pass.
6. Bundle: 232,975 bytes (under 2 MB), no console errors, no external URLs or fetch in the bundle, no em dashes. Pass.
7. Voice: the 12-line set unchanged; tooBig once per failure run, printed and starterBounce heard once each. Pass.

## Audit pilot
- Leads: 32, the same set as round 1's audit. Confirmed none as defects: 8 "1 seconds" (reads "0.1 seconds"/"1.0 seconds",
  settled), 4 sideways film strip (by spec), 10 modal keep-region (Starters and Why dialogs), 10 welcome-after-first-tap
  (settled stale-welcome rule; Time and Flip on a blank book now hint Draw or Starters by item 11).
- Leads wrong: all 32, as above.
- Missed: the audit cannot see items 1, 3 and 4 (selection while playing, repeated tooBig, print speech); they needed
  targeted drives. It also reports no network column, so the network check here is a bundle read.
