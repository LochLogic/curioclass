PASS WITH FIXES

# Score Keeper verify (2026-10-26, cold)

Checked against docs/agents/VERIFY.md, STANDARDS.md, BATCH-CS.md, spec.md and POLISH.md. Bundle:
`CURIO_DRAFT=1 python scripts/bundle_tool.py score-keeper` (193 KB). Driven in muted headless Chrome over CDP (own
port 9551, own profile, held 120 ms clicks, real keys, jittered drag), 375 wide through an iframe host page.

The core is right. Every number in the reference table recomputes, live and instant; the interpreter is data only; the
Watch pacing shows cause and effect well. One CSS bug puts log lines on top of the Step button, and a few fixed voice
lines can say something false in the Lab.

## Must fix

1. **"Same value" log lines float over Pause/Step and block them.** (Lab, rock takes 0, every hit; also every Reset lab,
   which logs "Reset lab: goal 20 → 20 (same value)".)
   Evidence: during a rock 0 run, `#log li.same` has `position: absolute` at 1139,108 (199x23 px), and
   `elementFromPoint` at the centre of `#step` returns that `LI.same`, not the button. The frame shows the pill
   "Rock hit: lives 3 → 3 (same value)" sitting across Pause and Step. Each one stacks on the same spot, and it drops
   out of the log list. Question 3 of the Lab ("Make a rock take 0") triggers it on every hit.
   Cause: the box tag style `.same{position:absolute;right:2%;top:4%;...}` (src.html:195) also matches the log row,
   which `addLog` gives `className = 'same'` (src.html:1243, styled again as `#log li.same` at :220). Rename one of
   the two classes, for example `li.sameval`, or scope the tag rule to `.vbox .same`.

## Should fix

2. **Fixed voice lines state the default amounts even when the dials have changed them.** Each plays once per page, so
   whichever Lab run comes first decides what the class hears.
   - Star adds 5, first catch: the log reads "score 0 → 5", but `catch1` says "the line score equals score plus one
     ran".
   - Rock takes 0, first hit: the log reads "lives 4 → 4 (same value)", but `hit1` says "That line took one away from
     lives".
   - Rock takes 2: lives ends at −1, then `endLives` says "Lives got to zero, so the game ended."
   Evidence: vlog from runs v_rock0_star5 and v_rock2 (rock 2 ends with the box showing −1).
   Cause: `narrate('catch1'|'hit1'|'endLives', ...)` only checks the mode (src.html:845-853). Give these lines a
   `valid` test that the line is true (amount is 1; lives is exactly 0), or skip them and leave them unsaid until it is.

3. **Narration lags many seconds behind its moment.** Lines queue in order and only check the mode, so after the Lab
   welcome and question line (about 12 s together), every "first" beat comes late.
   - Lab, Quick, rock takes 2: lives went to −1 at 15.8 s, and "Look at lives..." started at 31.3 s, after the result
     card was up. "Lives got to zero" started at 37.2 s, 20 s after the game ended.
   - Lab, Watch, defaults: the first catch at 5.5 s was narrated at 13.2 s.
   STANDARDS: "Drop a queued line whose moment has passed."
   Cause: `pump()` only drops lines whose `valid()` fails, and every game beat uses `modeIs(...)`. Stamp the game or
   event a line belongs to, and drop it once a later game starts, the result card is up, or N seconds have passed. Or
   hold the Lab question line until the first run ends.

4. **The "Goal!" sparkle covers the banner text, then leaves static stars behind.**
   Evidence: in run f_spark, sampled `.spark` centres: at +100 ms nine sparkles sit on a ring at full opacity, waiting
   for their delays. Once each one animates, it jumps to the banner centre (342,277) and pulses over the letters. In
   frame f_goal a sparkle sits on "oa" of "Goal!". After 2 iterations each one returns to the ring as a still star
   (in Play the banner stays up).
   Cause: the CSS `@keyframes spark` animates `transform: scale()`, which replaces the SVG `transform="translate(...)"`
   attribute (src.html:76, :1174). Put each spark polygon inside a translated `<g>` and animate only the polygon, and
   add `animation-fill-mode: both` with opacity 0 at both ends.

5. **The best1 line says "Now press Play again" in the Lab**, where the button reads "Run again". This is one of the
   builder's listed deviations. It is the spec's own wording, but a grade 3 student looks for a Play button that isn't
   there. Fix it with a Lab variant, or neutral wording ("press the button again"), before recording.

6. **No voice recordings yet.** `voice/` holds only lines.json, and the bundler warns for all 24 lines, so every line
   falls back to the browser voice. Run `scripts/voice.py score-keeper` (or localvoice) once items 2 and 5 settle the
   wording.

7. **The "empty" label on the value cards has low contrast.** `#8f808a` on `#fffaf4` is 3.6:1, at 14 px bold (AA
   needs 4.5:1 at that size). At 680x425 the word is also wider than the card, and the crate flaps clip it. Use
   `--muted` (6.6:1) and a smaller size or "?" in tiny cards.

## Nice to have

8. **The game is not dimmed during the final event block.** When the last catch or hit ends the game, `G.ended` is
   already true, so `frozen` is false and the dim stays off while that block, the end check and "when the game ends"
   run (trace: dim 0 from "when a rock hits you" at g20800 onward). The game is still stopped, so this is only a
   look, but it is the one event that breaks the pattern.
9. **The program text stays 15 px at 1920x1080**, in a 390 px card with a third of it empty. On a projector, the
   class reads the highlighted line from across the room. Scale the code font with the card (for example 18 to 20 px
   when w >= 1600).
10. **In compact Lab (800x500, 680x425) the card scrolls to the running line, and the event line that caused it can
   scroll off.** For example, "when lives is 0 or less" is centred while "when you catch a star" is out of view.
   Scrolling to the block's first line when it fits would keep the cause on screen.
11. **Lab question 1 asks "How long does the game last now?"** Nothing on screen gives a length, so students answer
   from "Stars caught 2, rocks hit 1". A "Lasted N drops" line on the result card would make it measurable without a
   HUD.
12. **With best at 0 changes, Check gives best the yellow "no" style**, the same look as "Look again". The text is
   right, but the spec says that card is "never marked wrong". A neutral grey style would match.
13. Small text and record issues:
   - notes.md says Watch is "about half a second per line"; lines run 0.7 s and event lines 0.5 s.
   - The spec's contrast list gives "dark text on #f5b83d glow 9.2:1". Ink on that colour is 8.6:1, and no text sits
     on it in the build.
   - art/prompts.json records the backdrop as `"aspect": "4:1"`, but the file is 1600x900 (16:9).

## Builder deviations (judged)

| Deviation | Verdict |
|---|---|
| Boxes start "empty" until the start lines fill them | Accept. The empty boxes make "when the game starts" visibly cause the values. Only the label contrast needs work (item 7). |
| Quick: lines shown 200 ms while the game keeps going | Accept. This is the spec. Boxes lag the game slightly at speed 5, as expected. |
| End checks highlighted 500 ms with a yes/no tag | Accept. The tag makes a test that is false visible, and it is good for the `if speed < 5` question. |
| "Solid white background" dropped from art prompts | Accept. The magenta-key cutouts are clean (checked on magenta). |
| Extra voice lines for the Play and Lab hints | Accept. STANDARDS asks for panel hints to be recordable. |
| Moves ignored while paused or during a Watch freeze; Autopilot may go down to 0.12 s per lane | Accept. Game time is frozen, so nothing is lost. Stepping the game in 16 ms steps for none, lives 9, speed 5 and rock 0 never needed more than the 0.25 s per lane rate. |
| Step with nothing queued runs the game to the next line | Accept. This is the spec. |
| Compact hides the log and scrolls the program card | Accept (see item 10). |
| best1 says "press Play again" while the Lab button reads Run again | Should fix (item 5). |
| Table wording "lives is 0 or less" / "score is goal or more" | Accept. It matches the program's own words and the result card. |

## What passed (evidence)

- **Numbers.** I recomputed the reference table in Python from the spec's rules (sim.py). All 10 rows and the
  "run twice" row match the spec, and `__tool.run` matches mine exactly: drop, seconds, why, the five values, caught,
  hits and changes. Every drop's outcome matches the Autopilot plan (CCHCCMDCHC) in every row. Live runs give the same
  rows:
  - Lab defaults in Watch (54 s real): 8/0/3/8/20, "Ended because lives is 0 or less", "Stars caught 8, rocks hit 3".
  - Run again: same values, best "changed 0 times", goal 0.
  - rock 2: lives −1 in the box and "lives 1 → −1" in the log.
  - speed 5: `if speed < 5:` highlighted with "no", speed changed 0 times.
  - lives 1, and star 10 / star 5 (Goal).
  - The Notebook rows also match at 3x game speed, so the result does not depend on frame chunking.
- **Interpreter.** The VARIABLES ENGINE block has no DOM access. There is no `eval`, `new Function` or parsing, and
  only data is run. In the bundle, eval and new Function appear only in comments. There are no network requests
  (`performance.getEntriesByType('resource')` is empty after a Lab run plus the Notebook), and the only URL in the
  file is the SVG namespace.
- **Watch pacing.**
  - Each event line shows 500 ms and each line 700 ms; the line that just ran keeps its tint for 1 s.
  - The game dims while code runs and game time stops (G.t is constant through every freeze).
  - The value flies in an arc, the old card slides out, the box bumps and its counter ticks. "Same" shakes the card
    with a tag.
  - It is easy to follow and shows cause and effect clearly. A full catch freezes about 2.2 s, so a 21 s game takes
    about 54 s; fine for a lesson.
- **Pause and Step.** Pause froze mid-line, and each S press ran exactly one line (event, then `score = score + 1`,
  then each check). Space and S work, and G.t did not move while paused.
- **Keyboard only.**
  - Tab order: modes, Motion, Sound, Read, Play, ◀, ▶, Watch, Quick, Autopilot, Same sky, (Reset lab), five dials,
    Next, log.
  - The dials respond to the arrow keys.
  - I played a game with arrows, A and D, Space and S.
  - I ran the Lab from the keyboard and saved with Enter: focus landed on Save to notebook, then moved to Run again.
  - Focus was never on body.
- **Held clicks and voice.** Over three held-click sequences (Lab entry, Read, Sound off and on, mode switches), no
  line played twice. Read cut the welcome, and a first tap on Read or Sound skipped the welcome. Sound on queued the
  unsaid welcome. voice/lines.json equals `allLines()` (24 lines, same order); 22 lines are the spec's words, and two
  are hints from the spec.
- **Sizes.** I checked 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1366x657, 1280x600, 1920x1080, 760x900,
  760x600, and 375x667 and 375x812 in the host page.
  - Play/Pause, Step and the move buttons are on screen and uncovered at every size; there is no horizontal scroll.
  - Value digits are 39 px at 1366x768, 32 px at 1366x657, 29 px at 1280x600 and 25 px in the 680x425 preview.
    Program text is 15 px.
  - The backdrop's 16:9 image crops cleanly to its dunes and rock domes in the bottom strip at every size. The ship
    and rock are clear at 30 to 112 px and 22 to 72 px.
- **Motion off.** There is no flight, cards change in place with a ring, the twinkles stop and falls step by lane.
  Toggling Motion three times mid-run still gave the right result. Console was clean in every run.
- **Notebook.**
  - Two saved runs appear in the table and chart (bars 8 and 20, a dashed "goal" line and an aria label).
  - Check marked goal "Stayed the same", score and lives "Changing value", and speed (wrongly binned) "Look again".
    The counts equal the table sums (28/3/6/2/0).
  - Copy fell back to the "Select all and copy." box with tab-separated text and a plain minus.
  - Save notebook survived a new tab (rows, sorting and the What I found text all came back). Clear asks "Clear all
    saved runs?", empties localStorage and returns focus to Clear notebook.
  - At 30 runs, save is disabled with "Notebook full. Copy and clear it to keep going."
  - Drag works with jittered whole-pixel input, and the 1, 2 and 0 keys work on a focused card.
- **Words.** There are no em dashes in the tool files. "Curio" appears only as "Curio Class" in visible text. Each
  claim about variables (a named box with one value; new value in, old gone; stored or changing) traces to the
  Code.org glossary, the Scratch Wiki or CSTA 1B-AP-09, and is plain grade 3 language.

## Re-verify

PASS WITH FIXES

Re-verified cold on 2026-10-26 against VERIFY.md and STANDARDS.md, including the new "Say how to act" rule. Bundle:
`CURIO_DRAFT=1 python scripts/bundle_tool.py score-keeper` (704 KB, no missing-clip warnings). I drove it in muted
headless Chrome over CDP with my own port (9591), profile and http host (8816). Clicks were held for 120 ms, keys were
real, and 375 wide ran through an iframe host page. The must-fix is gone and nothing regressed. What is left is in the
words: several waiting moments do not say what to press, and two Notebook lines say something untrue.

### Original items

1. **Fixed.** Same-value rows no longer sit over Step. I ran the Lab with rock takes 0 (6 hits, all "lives 3 → 3 (same
   value)"), then pressed Reset lab ("goal 20 → 20 (same value)"). Every 50 ms I checked `elementFromPoint` at the
   centres of go, step, left, right and resetLab, and none was ever covered (0 bad samples). The `.same` tags only ever
   appeared inside `.crate` (lives, goal). Log rows are `li.sameval`, `position: static`, and stay in the list.
2. **Fixed, one nit left.** catch1, endLives and the Lab best1 line are true for star 5 and 10, rock 0, 2 and 3, and
   speed 5. Rock 2 ends at −1 and the line says "zero or less". speed1 plays only when speed changed, so speed start 5
   never says it. The nit is new item N5: with rock takes 0, hit1 says "took the rock's amount away from lives" while
   lives stays 3.
3. **Fixed.** Lines now come late by seconds, not tens of seconds. Timelines (game event → voice start):
   - Watch defaults: hit 14.5 → 13.6 (it starts on the event line), speed 25.6 → 26.1, end 50.3 → 51.0.
   - Quick, rock 2, no wait for the welcome: lives went to −1 at 16.6 and "Look at lives" started at 21.2, 2.5 s after
     the result card. Before the fix it was 31.3. "Lives got to zero" was dropped, not played 20 s late.
   - Watch, rock 2: "Look at lives" starts the same moment as "lives 1 → −1" (50.2). Done-when 3 holds.
   - First catch and first hit lines that miss their 4 s window are dropped unmarked and play at a later catch or hit.
4. **Fixed.** In a star 10 Goal run I sampled all 10 sparkles every 40 ms. Each kept one position for its whole life,
   none was on the banner text, and each ended at opacity 0 (frame goal_1).
5. **Fixed.** The Lab says "Now press Run again" (L.best1Lab), and Play keeps "Play again". They share the once-only
   key best1.
6. **Fixed.** The bundler gives no "no recording" warnings. allLines() has 25 lines, equal to voice/lines.json word for
   word and in the same order.
7. **Fixed.** "empty" uses --muted on #fffaf4: 6.9:1 by my count (the builder's 6.6 is muted on paper). It fits at every
   size: 36 px of text in a 41 px card at 680x425, with nothing hidden under the crate front.
8. **Fixed.** The dim stays on through the final lines: 120 of 120 samples taken while busy after G.ended were dimmed.
   It is off only during "when the game starts", before the game begins, by design.
9. **Fixed.** Program text is 19 px at 1920x1080, 17 px at 1366x768 and 1366x657, 15 px at 1280 and 14 px in compact.
   No sideways overflow at any size, with the dials shown.
10. **Fixed at 800x500 and up, not at 680x425.** I sampled the running line every 40 ms. At 800x500 and 375x667 every
    line was in view together with its event line. At 680x425 the Lab program card is only about 3 lines tall, so a
    dial line (46 px) and its event line never fit together, and the code falls back to centring the line. Nit, since it
    is only the preview.
11. **Fixed.** The result card says "The game lasted 13 drops (20.8 seconds)." and matches my own simulation on every
    row. N4 below is a grammar slip in it.
12. **Fixed.** best with 0 changes gives `fb note`: grey #f1edf0 with ink and "Try a run that beats best.", in either bin.
13. **Fixed.** notes.md says 0.7 s and 0.5 s, the spec says 8.6:1 (I computed 8.59), and prompts.json says 16:9 for the
    1600x900 backdrop. The spec's Art section still says "4:1" for the backdrop (nit).

### Regression checks (all pass)

- **Numbers.** I wrote my own simulation from the spec's rules (mysim.py). It reproduces all 10 reference rows and the
  "run twice" row. `__tool.run` matches it on those and on 5 extra cases (score 15 + star 5, score 10 + star 10, rock 3,
  lives 9 + rock 0, speed 4). Live Lab runs give the same rows in Watch, Quick and Motion off.
- **Done when 1 to 10.** All hold.
  - Pause plus four S presses ran one step each.
  - G.t moves only on a Step with nothing waiting (an accepted deviation).
  - The Notebook shows 2 runs and 2 bars. Save notebook survived a reload, including the What I found text.
  - Clear asks "Clear all saved runs?" with focus on No. Yes empties localStorage, and focus returns to Clear notebook.
- **Sizes.** I checked 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600, 1366x657 and
  1280x600, plus 375x667 and 375x812 in the host page. At each I checked Play idle, Play running, Lab idle, Lab running,
  the result card and the Notebook.
  - Go, Step and the move buttons are always on screen and uncovered, and there is no horizontal scroll.
  - Value digits are 25 to 46 px, and no label is clipped.
  - The result card never scrolls, stays inside the game, and no toast covers it.
  - The dial value box keeps its 34 px minimum width.
- **Keyboard only.** I played with the arrows, A, D, Space and S, switched to the Lab, and set all five dials with arrow
  keys and Home/End. The dials lock while a game runs.
  - Enter on Run put focus on Save to notebook when the result card came up. Enter saved, focus moved to Run again, and
    Enter ran again.
  - In the Notebook I sorted with 1 and 2 and checked with Enter.
  - Focus was on body only while Tab wrapped past the end of the page (browser behaviour).
- **Held clicks and voice.**
  - Read as the first tap gave no welcome. Lab, then Play, gave each welcome once.
  - With Sound off a whole run queued nothing, and Sound on queued nothing already said.
  - Read during a queued pause line dropped that line.
  - No line played twice in any run.
- **Contract.** The console was clean in every run. The only failed request was the test server's /favicon.ico; the
  tool itself made no network requests. eval and new Function appear only in comments. No em dashes, and "Curio" appears
  only as "Curio Class".

### New findings

N1. **Waiting moments that do not say what to press** (should fix, STANDARDS "Say how to act"). I walked each wait as a
student who can't read the screen. Suggested lines are below; each needs a voice clip and a hint that matches.
   - Play, before the first game (hint and w1): neither says to press Play or how to steer. Hint: "Press **Play** to
     start. Move the ship with the arrow buttons or the arrow keys. Watch which line changes each box." w1 could end
     "Press Play to start, and steer with the arrow buttons."
   - Play, game over: the hint goes back to the plain Play hint, and best1 ("press Play again") is said only once per
     page. Give the game-over state its own hint: "Game over. Press **Play again** and watch which boxes start over."
   - Lab, idle (hint, labW and the question lines): the hint only reports ("Autopilot plays the same sky..."). labW
     names the dials but not Run, and the questions name a change but not the control. Hint: "Turn one dial with − and
     +, then press **Run**." Question line pattern: "Start lives at 1: press the minus on lives, then press Run. How long
     does the game last now?"
   - Lab, result card: nothing says to save. Hint and line: "Press **Save to notebook** to keep this run, then **Run
     again** or turn a dial."
   - Notebook (nbW, which is also the hint): "Sort each variable" does not say how. Suggested: "Drag each card into a
     bin, or press Same or Changed on it. Then press Check with my runs."
   - Already fine: Pause ("Press Step to run one line at a time") and the Clear notebook Yes / No question.
N2. **The Notebook welcome says "Here are your runs" when there are none** (should fix). Entering the Notebook with 0
   runs speaks nbW and shows it as the hint (t_voice A5). For 0 runs use something like "No runs yet. Go to the Lab,
   press Run, then press Save to notebook."
N3. **"Nice work. Your runs are the evidence." plays after a wrong sort** (should fix). With the cards in Stayed the
   same, Check marked four "Look again" and still said "Nice work" (t_voice C). Say it only when every card is right;
   otherwise say something like "Look again at the cards marked Look again, then press Check again."
N4. **"The game lasted 1 drops (3 seconds)."** (should fix, small). Score start 15 with star 5, or score 10 with star 10,
   ends at drop 1 (checked live and with `run`). Use "1 drop".
N5. **hit1 with rock takes 0** (nit). This is question 3's setup. The first hit says "took the rock's amount away from
   lives" while the box shows 3 → 3 with a "same" tag. It is true (the amount is 0), but it sounds like lives changed.
   Either say it only when lives changed and let same1 cover the 0 case, or reword it to "The lives line ran and took
   the rock's amount from lives."
N6. **Small record and look items** (nit). The spec's Art section still says the backdrop is 4:1. The Lab log keeps
   Play's "Game started" rows after a mode switch, under the title "Lab log". At 680x425 the Lab program card shows only
   about 3 lines (see item 10).

## Fixes

Builder's record of the fixes for the Re-verify findings (2026-10-26). New and changed lines are unrecorded: the
bundler warns "no recording yet" for 19 lines until voice is recorded. allLines() equals voice/lines.json (29 lines).

- **N1 (say how to act).** The hint now follows the waiting moment (hintNow()):
  - Play before a game: "Press **Play** to start. Move the ship with the arrow buttons or the arrow keys. Each box is a
    **variable**: watch which line changes it." w1 ends "Press Play to start, and steer with the arrow buttons or the
    arrow keys."
  - Play game over: new hint and line over1, "Game over. Press Play again and watch which boxes start over.", said
    after every game, not once per page. best1 is now just "Score was more than best, so best saved it." (best1Lab is
    gone).
  - Lab idle: hint "Turn one dial with its minus and plus buttons, then press **Run**. ..."; labW names the minus and
    plus buttons and Run; each of the seven questions names the dial and says to press Run.
  - Lab result card: new hint and line result1, "Press Save to notebook to keep this run. Then press Run again, or turn
    a dial first.", said on each result card until the first save.
  - Notebook: nbW is "Here are your runs. Drag each card into a bin, or press Same or Changed on it. Then press Check
    with my runs."
- **N2.** With no saved runs the Notebook says and shows nb0: "No runs yet. Go to the Lab, press Run, then press Save
  to notebook." Clear notebook switches the hint to it.
- **N3.** "Nice work..." plays only when every card is right. With any "Look again", fix1: "Some cards say Look again.
  Move each one to the other bin, then press Check with my runs again." With no wrong card but one not in a bin, fix2:
  "Put every card in a bin, then press Check with my runs again." Both play on every Check that needs them.
- **N4.** "1 drop" and "1 second" are singular.
- **N5.** hit1 is now "Ouch, a rock. The lives line ran and took the rock's amount from lives." and is not said when
  the rock takes 0 (same1 covers that run).
- **N6.** Switching modes clears the log, so each mode keeps its own. spec.md's backdrop note says 16:9 (1600x900).
  The 680x425 program card is left as is.

Checks rerun in muted headless Chrome (own port 9521, profile and http host 8802): N1 to N5 driven live (two Play
games each said over1; result1 once before the first save and not after; rock 0 gave no hit1; "1 drop (3 seconds)";
nb0 with no runs, nbW with runs; a wrong sort gave four "Look again" plus fix1, the right sort gave "Nice work"); the
Lab log was empty after leaving Play. Sizes 1920x1080, 1366x768, 680x425, 375x667 and 375x812 (Play, Lab running,
result card, Notebook): every control on screen, no horizontal scroll, no small targets, no clipped text. Earlier
regression sets (steps and pause, the if line, notebook and Clear, keyboard path, Motion off, Quick, safety, voice
queue) all pass with a clean console.
