PASS WITH FIXES

# Verify: code-tracer (Code Tracer, grade 4, Trace the Code)

Checked cold on 2026-10-26 against docs/agents/VERIFY.md, STANDARDS.md (including the new "Say how to act" rule) and
BATCH-CS.md. Build: `CURIO_DRAFT=1 python scripts/bundle_tool.py code-tracer` (102 KB, one file). Test rig: my own CDP
driver, muted headless Chrome on port 9571, held clicks (120 ms), real keys, host page for 375 wide. Voice recordings
do not exist yet (BUILD.md says do not record), so the voice log shows which clips start, with the timeout standing in
for clip length.

## What passed

- **Engine, recomputed.** An independent Python tracer parses the spec's own program text (not the tool's data) and
  runs all 12 levels and the 13 Workbench programs. Every step (line, variable, value, round text, yes/no, skipped
  lines, says) matches `__tool.trace(n)` with 0 differences. Steps/guesses: 4/4, 4/4, 4/4, 4/4, 5/5, 6/6, 10/6, 8/5,
  12/9, 4/4, 6/6, 13/9 (program 13: 7/7), all as the spec says. Star steps (2, 2, 3, 4, 4, 4, 9, 7, 10, 3, 4, 12) and
  note answers (6 No, 9 Yes, 12 Yes) match the content table. Done-when 7: level 8 with repeat 6 and `* 5` gives
  14 steps ending at 15625; program 13 says 8 then 3.
- **Hostile programs and overrides** (45 tries): out-of-range, float, NaN, string, array, `__proto__`, `constructor`,
  unknown ids, duplicate ids, unknown operators (`**`, `toString`), unknown comparisons, extra keys, negative and huge
  literals, deep nesting, empty and cyclic bodies, 31 lines, 400+ steps, overflow, unset variables, HTML in a note. Every
  one is refused with a plain reason or stopped with a "Stopped:" row; nothing throws from the engine, HTML is escaped.
  No `eval` or `new Function` anywhere (only in comments), the engine block has no DOM access, no network requests
  (only the page itself; the favicon 404 came from my test server), console clean in every run.
- **Done when** 1, 2, 3, 5, 7, 9, 10 pass outright; 4, 6 and 8 pass apart from the findings below. Level 1 with right
  guesses: chip slides from the code line to the dashed cell, check and "matched", tally 4 of 4, stamp, dot fills,
  Next glows. Level 4 guess 9 on step 4: 4 bold over a struck 9, W4 in the hint, `why4` clip starts. Level 10 and
  level 12 round 4: Yes/No replaces the keypad, line 5 dims with "skipped", the ▶ goes to line 6. Note checks give
  the right N line, the right answer turns green, Next stays disabled until answered. Keyboard only finished level 9
  9 of 9 (digits, Enter, Y), focus never left on a hidden control, 3 px blue ring with white inner ring shows on the
  slate card and on paper. Workbench: stepper by mouse and keyboard (Enter, arrows, Escape returns focus), "?" tag,
  line 12 once, Back/Step both ways, Reset numbers restores 8 and removes the tag, Predict mode works.
- **Motion off:** no chip, the cell gets the orange outline, same timing (1462 ms vs 1449 ms for a step plus a repeat
  row), stamp has no drop. **Print:** only title, program (dark on white) and the full table; pending row hidden.
- **Voice:** `voice/lines.json` equals `allLines()` (32 lines, same order) and the spec's 14 + 12 + 6 lines word for
  word, all under 200 characters. Held clicks: first tap on a keypad key, dot or mode button queues the welcome
  after the click; first tap Run line (empty) plays line 14 and skips the welcome; first tap Read or Sound skips it;
  Read stops the welcome and later lines wait for Read; Sound off queues nothing, Sound on queues the welcome. Only
  line 14 ever repeats.
- **Facts:** every on-screen claim about tracing, variables, repeat, if and notes matches the named sources
  (assignment right side first and `#` comments: Python Tutorial 3.1-3.2; a set replaces the old value: Scratch Wiki;
  loop/conditional: Code.org glossary; trace tables: Isaac CS, BBC Bitesize). CSTA 2026 ids are in
  `data/standards/csta-2026-ids.txt` and `data/modules.csv` row computer-science-4-trace-the-code. No em dashes; "Curio"
  only as "Curio Class". Language fits grade 4.
- **Cause and effect:** in Trace nothing moves until the student commits, the running line pulses, the value chip flies
  from the end of that code line into its cell (400 ms), the line gets a tick and the ▶ moves on: followable and clearly
  causal. Workbench Slow (1200 ms) and Quick (500 ms) are both followable; repeat rows light the repeat line 700 ms.

## Must fix

1. **Prompt label reads "is temp is more than 80?"** (Trace and Workbench Predict, every if step of levels 10, 11, 12).
   Seen on screen at every size: "Line 4: is temp is more than 80?", "Line 4: is lives is more than 0?". Spec:
   "Line 4: is temp more than 80?". Cause: `promptLabel()` writes `is ${a} ${TraceEngine.WORDS[op]} ${b}` and
   `WORDS['>']` is already "is more than". Use "more than" / "less than" there (keep WORDS for the screen-reader text).

## Should fix

1. **"Say how to act" (new STANDARDS rule): five waiting moments only ask or report.** Walked every wait as a student
   who can't read the screen:
   - Predicting a number (line 2): names action and control. OK. Empty Run line (line 14): OK.
   - **If step, line 5** "This line asks a question. Is it true? Choose yes or no." Names Yes/No but not Run line, and
     Yes/No here only choose (choose-then-Run). Suggest: "This line asks a question. Is it true? Tap Yes or No, then
     press Run line."
   - **After a ★ step** the hint is the W line (W1 to W12) while the tool waits for the next guess (or, on levels 4
     and 12 style last steps, for Next). W lines explain but never say what to do. After a miss on a non-star step the
     hint goes back to line 2 (fine; line 4 in the tip only reports). Suggest: keep the W line as the spoken line but
     show it in the tip box, and keep `#hint` on the action line (2, 5 or the level-done line), or add one fixed line
     "Read why, then type your next guess and press Run line." after each W line.
   - **Note check, line 8** "Now test the note. Does the note tell the truth about what happened?" Only asks.
     Suggest: "Now test the note. Does it tell the truth about what happened? Tap Yes or No on the note card."
   - **Level done, line 9** "Traced! Your table is a record of every step the program took." Reports; the tool waits
     for Next. Suggest: "Traced! Your table is a record of every step the program took. Press Next for a new program."
     Same for the **N lines** after a note answer (N2, N4, N6 only ask, N3 and N5 only report): suggest one fixed
     follow-up line, "Press Next for a new program.", queued after the N line (level 12: "Press Workbench to change
     the numbers.").
   - **Workbench welcome, line 11** "...then step through and watch the table." Name the control: "Tap a number in the
     code to change it, then press Step and watch the table."
   - **Line 12** "You changed the code. Is the note still true? Notes don't change by themselves." Only asks. Suggest:
     "You changed the code. Press Step to run it, then check: is the note still true?"
2. **"skipped" tag clipped on the code card.** Level 12 round 4 (Done-when 4's moment): line 5's tag shows as "skip"
   cut off at the card edge at 680x425, 800x500, 1000x625, 1280x720, 1280x600, 1366x768, 1366x657 and 760 wide
   (frames L12_after_r4, S_*_L12if; `.lines` scrollWidth > clientWidth). Cause: `fitCode()` sizes the card from the
   longest code line but not the ~70 px tag that `decorate()` appends after an indented body line. Count the tag in
   the width, or put the tag in the gutter/under the line.
3. **"Traced!" stamp covers the newest row.** On levels 9 and 12 (and any table that fills the page) the stamp sits on
   the final Says value ("0 matched") at every size but 1920x1080 (frame L12_note_wrong; overlap measured). The spec
   wants the newest row visible. Cause: `#stamp` is absolute at right 16 px, bottom 34 px over the scrolling table.
   Give the table bottom padding equal to the stamp height when the level is done (the auto-scroll then lifts the last
   row above it), or move the stamp up over the table header area.
4. **Level stuck after a mode switch on the last step.** Run the last line, then press Workbench within the 300 ms land
   wait and come back: all rows are filled and the tally says 4 of 4, but `T.done` is false, so no stamp, no dot, no
   note check, no Next glow, and the panel shows "Type your guess" with nothing to type (frame E_race). Cause:
   `runLine()` returns on the generation change after `V.i` has advanced, and `setMode()` only resumes repeat rows. In
   `setMode`/`showMode`, call `finishLevel()` when `!T.done && !T.steps[T.i]` (or finish the level before the wait).
5. **Keyboard: Enter after opening a level from its dot restarts it.** Tab to a level dot and press Enter: focus stays
   on the dot, digits still type into the guess, but the next Enter re-opens the level and wipes the guess (T.i stays
   0). Same with focus on Restart. Cause: the Enter handler only runs the line when focus is on the keypad, Yes/No,
   Run line or off a button. Move focus to Run line after a dot opens a level, or let Enter run the line from the level
   dots when a guess is typed.
6. **Carried values fail AA.** `--carry #868c94` on the sheet is 3.24:1 (3.10:1 on the pending-row tint), at 13 to
   15 px. These grey values are what the student reads to predict ("use the newest value in each column"). The spec's
   contrast list leaves this pair out. `#6b7179` gives 4.71:1 on the sheet and 4.50:1 on the pending tint.
7. **Tip feedback depends on Sound.** Lines 3, 4 and 13 appear in the tip box only when `say1()` queues the clip. With
   Sound off, a miss shows no "Not quite. Read the line again..." text at all (checked: tip empty after a Sound-off
   miss). Track "first match/miss/shown shown on screen" separately from the voice queue.
8. **680x425 Workbench transport row overflows.** Back, Play and Restart labels are wider than their 39 px buttons:
   "Pla" runs into the Restart icon and "Restar" is cut (frame W_680x425_p12; scrollWidth > clientWidth for back,
   play, wbrestart; Restart also slightly at 800x500 and 1000x625). Hide the `.w` labels in compact as the phone layout
   does, or use a 2 x 2 grid.
9. **Targets under 44 px.** Phone header buttons 40 px tall, phone keypad 42 px, Just show me 30 to 32 px tall at 760
   wide and in compact, Workbench number chips 22 px wide in compact, 30 px on the phone and 34 to 36 px at 1000 and
   760 wide, level dots 40 px in compact. (Compact keypad keys at 36 px are allowed by the spec.)

## Nice to have

1. `__tool.trace(99)` and `trace(0)` throw a TypeError instead of returning a refused step (debug API only; the engine
   itself refuses everything).
2. Keys typed while a line animates (up to about 1.4 s when a repeat row follows) are dropped silently; a fast typist
   loses digits. Buffer them, or flash the pending cell.
3. Skipped lines are struck through as well as dimmed; in print the "skipped" tag is hidden, so the strike reads as
   deleted code. The spec asked for dim plus tag; consider dropping the strike or printing the tag.
4. Line 10 plays only when all 12 levels are traced, not "after level 12" as the spec says. Truthful to its words
   ("You traced all twelve programs"); say so in notes.md.
5. With a long voice backlog (welcome is about 9 s) a missed ★ line can be dropped before it plays (W12 was dropped
   when the note was answered quickly). Allowed by STANDARDS; worth knowing when the clips are recorded.
6. Level title "Copy, not link": "link" is not grade 4 vocabulary ("Copy, not a twin"?).

## Builder's deviations

| Deviation | Verdict |
|---|---|
| Check column only when the program has a repeat or an if | Accept: no empty column on levels 1 to 6 |
| 760 keypad has 12 keys plus Run line | Accept: 0 to 9, minus and delete are 12; the spec's 13 is an arithmetic slip |
| Workbench numbers above 20 get range 0 to 100 | Accept: 0 to 20 cannot hold temp 75 or 80; the 312500 maximum still holds |
| Yes/No is choose-then-Run line | Accept (same commit gesture as numbers, gives a projector class time), but the hint must say "then press Run line" (should-fix 1) |
| Next level usable any time except during a note check or on level 12 | Accept: all levels are open by spec |
| Pending row hides carried values | Accept: the values sit in the row right above; keeps the dashed box clear |
| Level 4 hint stays on the W line after the level ends | Accept for Done-when 3, but see should-fix 1 (the wait has no action) |
| Tip box shows lines 3, 4, 13, 14; tally in the table footer | Accept, except the tip's dependence on Sound (should-fix 7) |
| Workbench panel puts buttons before the program list | Accept: STANDARDS says controls before long lists |
| Lines whose moment has passed are dropped | Accept: STANDARDS rule |
| Welcome plays before "shown" if the first tap is Just show me | Accept: the welcome is more useful; "shown" still played (at 13.9 s, still valid) |
| Two-row phone header, 2 to 3 table rows at 375x667 | Accept: newest row, keypad and Run line all visible in the sticky bar |
| 680x425 Workbench code card scrolls sideways for the longest line | Accept; in my runs no program needed it (programs 5, 9, 11, 12, 13 fit), only program 13's note scrolls down |

## Sizes checked

680x425, 800x500, 1000x625, 1280x720, 1366x768, 1366x657, 1280x600, 1920x1080, 760x1000, 760x700, and 375x667 and
375x812 in an iframe host. Each in level 12 at the round 4 if step, level 9 mid-trace and the Workbench (program 9 and
12): code card, newest row, keypad or Yes/No and Run line are visible without scrolling at every size; code text 14 px
or more everywhere (24 px at 1366x768); no page scroll sideways.

## Re-verify

PASS WITH FIXES

Checked cold on 2026-10-26 after fix round 1. Build: `CURIO_DRAFT=1 python scripts/bundle_tool.py code-tracer` (105 KB, one file; missing recordings ignored, the voice is being recorded). Rig: my own CDP harness, muted headless Chrome on port 9691 with the cache off, a local server and iframe host page on 8979, held clicks (120 ms), real keys.

### The 16 items

| Item | Status | How I saw it |
|---|---|---|
| Must fix 1, prompt wording | Fixed | "Line 4: is temp more than 80?" on screen (levels 10 to 12 and Workbench Predict); WORDS still used for screen-reader text |
| Should fix 1, say how to act | Fixed in Trace, one gap in the Workbench (new item 2) | Walked every wait: number step (2), if step (5), empty Run line (14), ★ step (W line in the tip, hint keeps 2 or 5), level done (9b on levels 1-5, 7, 8, 10, 11), note check (8), N1 to N6 (all end with Next or Workbench), Workbench entry (11), number changed (12), Predict (2 and 5) |
| Should fix 2, skipped tag | Fixed | Fits on its line, or wraps under it at 680x425 and 800x500, at all 12 sizes (tag right edge measured inside the card, `.lines` never scrolls sideways) |
| Should fix 3, stamp | Fixed | Last row visible and clear of the stamp on levels 9 and 12 at every size, including 375 wide |
| Should fix 4, mode switch on the last step | Fixed | Motion on: switching during the land wait finishes the level (stamp, dot, 4 of 4, Next glows). Motion off: the line in flight is dropped and the last step waits again (3 of 4, consistent). Mid-level race on level 7 resumes cleanly |
| Should fix 5, Enter after a dot, Restart or Next | Fixed | Focus goes to Run line; typing 5 then Enter runs the new level's first line in all three cases |
| Should fix 6, carried values | Fixed | `--carry #6b7179`: 4.71:1 on the sheet, 4.50:1 on the pending row, 4.70:1 on the newest row |
| Should fix 7, tips without Sound | Fixed, with an edge case (nit 1) | With Sound off the first miss, match and shown tips appear once each; vlog stays empty; Sound on then queues the welcome |
| Should fix 8, Workbench transport at 680x425 | Fixed | 2 x 2 grid, labels fit; no clipped button text at any size |
| Should fix 9, 44 px targets | Fixed | No visible button under 44 px at any size except the compact keypad keys: 54x36 at 680x425 and 66x36 at 800x500. **Accepted:** the spec allows 36 px compact keys, each key has more area than 44x44, keyboard typing works there, and full screen gives 46 to 50 px keys |
| Nice 1, trace() input | Fixed (nit 3) | 0, 99, -1, "x", null, `__proto__`, {} each return one refused step; no throws |
| Nice 2, keys during an animation | Fixed (nit 2) | A digit typed while a line lands, or during a repeat row, lands in the next guess |
| Nice 3, skipped lines | Fixed, but see new item 4 | Dim plus tag, no strike; print shows the tag |
| Nice 4, line 10 in notes | Fixed | notes.md says all 12 in one visit |
| Nice 5, W lines | Fixed | W lines queue once per level (why2, why4, why6, why8, why12 all started in one full run) |
| Nice 6, level 4 title | Fixed | "Just a copy" |

### No regressions

- **Engine:** my independent Python tracer (it parses the spec's program text) matches `__tool.trace(n)` with no differences for all 12 levels and program 13. Steps and guesses are 4/4, 4/4, 4/4, 4/4, 5/5, 6/6, 10/6, 8/5, 12/9, 4/4, 6/6, 13/9. Stars and note answers match. Level 8 with repeat 6 and `* 5` gives 14 steps ending at 15625; program 13 says 8 then 3; out-of-range overrides are refused.
- **Voice:** `voice/lines.json` equals `allLines()` (33 lines, 9b added). Every line is in the spec word for word and under 200 characters, with no em dashes.
- **Full play-through by held clicks:** all 12 levels, with misses on even ★ steps and a wrong note on level 6. No line started twice. First tap: a key, dot or Motion queues the welcome; an empty Run line plays 14 only; Read and Sound skip the welcome; Sound off then on queues it. Read stops the welcome, and a match during Read waits for it. An empty Run line never piles up line 14.
- **Keyboard only:** level 9 finished 9 of 9 (Tab to dot 9, Enter, digits, Enter, Y). Focus ring is 3 px blue with a white ring; focus ends on the note card. The Workbench rescues focus to Back when Step or Play turns off.
- **Motion off:** no chip, same timing (1430 ms vs 1444 ms for a step plus a repeat row). Print shows only the title, program and table. Console clean apart from my server's favicon 404, and the only request is the page itself.
- **Sizes:** checked all ten STANDARDS sizes plus 375x667 and 375x812 in the host page. At each one the code card, Run line and keypad or Yes/No are visible. The newest row is visible in Trace, code is 14 px or more (24 px at 1366x768), and the page never scrolls sideways. The exceptions are items 1 and 3 below.

### Remaining and new items

1. **Should fix (new, likely a regression from the tag fit): at 1000x625 the trace table is cut off on the right in levels 11 and 12.** Steps: open 1000x625, play level 12 to the end (or level 11). The Says column is clipped: "✓ matche" is cut at the page edge, and `#tw` scrolls sideways by 15 px (level 12) and 21 px (level 11). The code card takes 329 px and the page gets 315 px. No other size or level overflows. Cap the code card so the page keeps its table width, or wrap the tag under the line at this size as compact does.
2. **Should fix: the end of a Workbench program names a control that is off.** Steps: Workbench, program 1, press Step until the footer says "The program is done." The hint is still line 11, "...then press Step and watch the table." (or line 12, "Press Step, then check..." after a change, with Predict on or off), but Step and Play are disabled. A child who can't read hears or reads "press Step" and nothing happens. Add a fixed line for this wait, for example "The program is done. Press Restart to run it again, or tap a number to change it.", and add it to lines.json and the spec.
3. **Should fix: on a phone the wait's control or newest row sits behind the fixed bar.**
   - At the end of levels 6, 9 and 12 the Note check card is below the fold at 375x667 and 375x812. Yes sits at 737 to 785 px while the bar top is at 600 px (812: 795 to 843 vs 745). The hint "Tap Yes or No on the note card" is behind the bar at 667. Steps: host page `?w=375&h=667`, finish level 6.
   - Workbench with Predict on at 375x667: the dashed prediction cell is behind the keypad bar for programs 9, 10, 12 and 13 (cell top 494 to 582, bar top 429). At 375x812 the same happens for program 13 (582 vs 574). Workbench program 13 at 375x667 without Predict also has its newest row partly behind the bar (597 to 626 vs 604).
   - Fix: in the phone layout, while the note check waits, put the note card in the fixed bar, or scroll it into view. In Workbench Predict, shrink the table or scroll the page so the pending row clears the bar.
4. **Should fix (new): faded skipped lines fail AA.** `.ln.skip .txt{opacity:.8}` turns `#9aa7b4` into `#828f9c` on slate: 4.09:1, below 4.5:1 for the 14 to 18 px code (it passes only at 24 px as large text). The spec promises 5.5:1. Drop the opacity. `#9aa7b4` with the "skipped" tag already reads as faded beside `#e8eef3`.

### Nits

1. If a student's first match, miss or Just show me falls on a level's last step, the tip shows for about 0.3 s. Then `finishLevel()` clears it (`if (!T.whyHint) setTip('')`), and because it is already marked seen it never shows again. With Sound off that student never sees it. Steps: Sound off, level 1, run steps 1 to 3 by script, press Just show me on step 4.
2. Digits typed during an animation are kept, but Enter typed during one is dropped, so "2 Enter" typed quickly leaves 2 in the box waiting.
3. `__tool.trace(1.5)` and `trace(2**32+1)` return program 1 (the `| 0` coercion). Debug API only.
4. `preview.svg` (and `previewSVG()`) still draws carried values in the old `#868c94`.
5. Print: the running line's gutter number prints in `#dfe7ee`, almost invisible on white (`.ln.run .no` isn't overridden in the print sheet).
6. At 680x425 in Trace, the hint under the keypad is cut off at the bottom of the panel. It is still spoken, and Read works.
7. After the first traced level, line 7 (hash-sign notes) plays after 9b, so the last thing heard only reports. The same goes for a spoken W line after a missed ★ step. In both cases the hint on screen names the action and Read speaks it, so I accept this.

## Fixes 2

Fix round 2, 2026-10-26, by the build agent. Rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py code-tracer` (the size now includes the recorded clips). Checked with my own CDP harness: headless Chrome on port 9541 with its own profile, `--mute-audio` and the cache off, plus a local server on 8806. Phone sizes were checked through the iframe host page.

### Should fix

1. **The table no longer scrolls sideways.** A guard runs after every table render and whenever the table or its box changes size (a ResizeObserver). It does nothing while a line is landing. If the table is wider than its box, it squeezes in steps:
   - 1: tighter cells, and "matched" wraps under its check mark
   - 2: the "skipped" tag goes under its line, so the code card narrows
   - 3: smaller table type (values 13 px)

   The squeeze resets on each level and on a new window size, but not when only the bar changes. Checked all 12 levels by held-key play at 680x425, 800x500, 1000x625, 1024x768, 1280x720, 1280x600, 1366x768, 1366x657, 1920x1080, 760x1000, 375x667 and 375x812 with Motion off. I also checked 680x425, 1000x625, 1366x768 and both phone sizes with Motion on. After every step there is no sideways scroll in the table or the code card, the "skipped" tag stays inside the card, and the last row is visible and clear of the stamp. At 1000x625, levels 11 and 12 use step 1; at 680x425, levels 9 and 10 use step 3.
2. **New line 11b**, "The program is done. Press Restart to run it again, or tap a number to change it.", is both the hint and the spoken line when a Workbench program reaches its end (Step or Play), with or without Predict. It is spoken once, and Back, Restart or a number change bring back 11 or 12. It is in spec.md and lines.json (34 lines). It has no recording yet.
3. **Phone:** when the layout settles after a level ends, or the bar changes size, the page scrolls so the note card sits above the fixed bar. In the Workbench, the pending prediction row (or the newest row) is kept above the bar. Results:
   - Levels 6, 9 and 12 at 375x667 and 375x812: the whole note card is above the bar.
   - Workbench with Predict on, programs 1, 9, 10, 12 and 13, and with Predict off, programs 1 and 13: the cell is above the bar at both sizes.
4. **The skipped-line opacity is gone.** Skipped code keeps `#9aa7b4`. The line gets the darker `--slate2` band (`#1a252f`), which raises the contrast, and keeps the "skipped" tag.

### Nits

1. finishLevel no longer clears the tip, so a first match, miss or Just show me on the last step stays on screen (checked with Sound off, level 1, Just show me on step 4).
2. Enter typed during an animation is held like digits and runs the line when the animation ends. Typing "3 Enter 5 Enter" quickly runs two lines.
3. `trace()` refuses anything that is not an integer from 1 to 13: `trace(1.5)`, `trace(2**32+1)` and `trace('3')` each return one refused step.
4. The carried values in `previewSVG()` now use `#6b7179`. preview.svg was regenerated from it.
5. In print, the running line's gutter number (and every gutter number) prints `#111`.
6. 680x425: Restart, Next and Print now sit under the hint, so the hint is fully in view while a guess waits (hint bottom 423, panel bottom 425). Restart, Next and Print are reached by scrolling the panel (its scrollbar is hidden so the keys keep 54 px) until the level ends, when the keypad leaves.

### Don't nag (new standing rule)

How-to lines are spoken the first time only, and later they update the hint silently. Line 14 (empty Run line) was the one that repeated; it is now spoken the first time only, and the tip and the box shake show it after that. The others already played once per page load: 2, 5, 8, 9b, 11 and 12, and the new 11b plays once too. spec.md says this under "Which line when".

### Regression

Engine cases, level flows (1, 4, 6, 7, 10, 12, empty), keyboard level 9, Tab, Workbench flow, voice order, Motion off, print, edge input, the how-to, race, focus and key-buffer checks and the 44 px targets all ran again with the same results as fix round 1. The one change: the Workbench end now shows 11b. Console clean apart from the scratch server's favicon 404. `voice/lines.json` equals `allLines()`. No em dashes.

## Integrator fix (2026-10-27)
The plan agent found the Workbench table stuck at its smallest type (12 px cells, 11 px headers) after program 13, even at
1920x1080. Cause: a value sliding into its cell pokes past the table's edge for about 400 ms, so `guardTable()` saw an
overflow and raised the squeeze to 3. The squeeze only ever went up, so nothing brought it back down. Fix: `guardTable` starts from 0 on every check, and it
waits for running animations in the table to finish before measuring. Rechecked:
- Program 13 stepped to the end: no squeeze at 1366x768, 1920x1080 or 680x425, at full size (15, 17 and 13 px).
- Trace level 9 at 680x425 still squeezes to step 3 (a real overflow). Levels 11 and 12 at 1000x625 and level 12 at
  375x667 now need no squeeze.
- No sideways scroll in the table or the page at any of these sizes, and 0 console errors.
