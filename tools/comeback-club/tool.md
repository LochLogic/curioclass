# Comeback Club: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Exit check before 2026-10-27

<!-- part: verify.md -->

### Verify: brain-gym (cold, 2026-10-26)

(History. The tool was renamed Not Yet Gym, then renamed Comeback Club 2026-10-26; it now lives in tools/comeback-club.
Names, paths and save keys below are as they were when each pass ran.)

**Verdict: FIX** (2 blockers, 6 should-fix, nits below)

How checked: draft bundle `tools/brain-gym/brain-gym.html` (fresh, same timestamp as src.html) in muted headless Chrome on
private port 9677, real held mouse clicks (120 ms) and real keys over CDP, 375 wide through an iframe host served from my
temp dir on 8991. Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600, 375x812, 375x667,
every mode, every room, extremes (stage 5, 12 stripes, all goals done, summit). Python recompute of every Light Mat and
Number Lift rung. No console errors or exceptions in any run, no network requests, `check_tools.py` reports it as draft.
Art and voice are not generated yet (expected): the gym backdrop shows the placeholder.

#### Blockers

##### B1. Memory Mirror (and any scene tap) loses taps when the scene re-renders during a press
- Where: `src.html:808` (tapPad sets a 260 ms timer that calls `render()`), `render()` at `:1092` replaces `sv.innerHTML`,
  input is on `click` at `:1510`. If a render lands between pointerdown and pointerup, the pressed `<g>` is gone, no click
  reaches it, and the tap vanishes.
- Repro: Memory Mirror rung 3 (5 pads). After playback, tap the right pads with a 120 ms hold at about 3 taps a second
  (160 ms between release and next press). 8 of 8 trials ended in a false "Not yet" (a lost tap makes the next correct
  tap wrong). At 0.3 s gaps or slower every trial solved. Taps logged: sequence `[1,2,1,3,3]`, clicks received
  `pad-1, pad-1, pad-3`.
- Why blocker: a child who remembers the pattern and taps it quickly is told "Not yet". That is the opposite of the
  tool's one idea (a mistake costs nothing and is information), and it hits the core room.
- Fix: act on `pointerdown` for scene targets (keep `keydown` for Enter/Space), or remember the `data-k` from pointerdown
  and act on pointerup over the same key, or stop re-rendering the whole SVG for the 260 ms flash (toggle a class on the
  one pad). Re-test with held clicks at 3 to 4 taps a second.

##### B2. Number Lift can soft-lock: both buttons greyed, moves left, no reset
- Where: `liftMove` `:857-879`, greyed rule `:861`, hint `:944`.
- Repro: Number Lift rung 1 (+3, +5, target 11, limit 5): press +5 four times. Floor 20, "Moves: 4 of 5", both buttons
  read "Can't go there" (aria-disabled). No move is possible, so the move limit is never reached and the lift never
  resets. Same on rung 6 (x2, +1): +1 x2 x2 +1 x2 x2 reaches 20 in 6 of 8 moves, both buttons greyed. I'm stuck, then
  "Just try again", only closes the cards (floor stays 20, moves stay 4). Use a hint then says "Try the glowing button
  next." with nothing glowing (`liftPath` returns null).
- Also from floors 9, 10 and 12 to 20 on rung 1, and 12 to 20 on rung 6, the target can no longer be reached, so the hint
  again promises a glow that is not there (moves still burn down to the reset, so that part is only confusing).
- Fix: after each move, if the target is unreachable from the current floor (BFS returns null) treat it like out of
  moves: a not-yet with a line like "This floor can't get back to the target. The lift went back to floor zero." and
  reset to 0. Make "Just try again" in Number Lift and Light Mat reset the puzzle to its start. In `giveHint`, if there is
  no path, say that instead of "Try the glowing button next."

#### Should fix

##### S1. Light Mat fewest-press solves complete the Number Lift goal
- Where: `pressSq` `:837` passes `{fewest}`; `solve` `:714` does `G.few++` for any room.
- Repro: once Number Lift is open, pick "Reach a floor in Number Lift in the fewest moves.", go to Light Mat, press the
  solution squares. Goal done, reflection card, without touching Number Lift.
- Fix: `if (info.fewest && me.kind === 'lift') G.few++`. (Also decide whether Light Mat should show the "Fewest moves!"
  hint at all; the spec only gives the star to Number Lift. Harmless if kept.)

##### S2. Stage-up line "I feel stronger at this already!" is too close to the brain-as-muscle claim
- Where: `L.stageUp` `:287`, voice/lines.json.
- Judgment: Bix is a brain, in a gym, getting gear as points rise; a brain saying "I feel stronger" is exactly the
  picture BATCH-SEL and the spec's own Coach's corner note rule out ("Do not say the brain ... gets 'stronger' like a
  muscle"). The spec lists this line, so it needs a spec edit too, but voice is not recorded yet, so it is cheap now.
- Suggested wording (first person, about skill and practice): "All that practice is paying off!" or "Practice is
  paying off. Look at my new gear!"
- Related nit: stage 4 name "Strong mover" (`:256`) leans the same way; "Smooth mover" keeps the dance-move idea.

##### S3. Pattern Ladder "Break it into parts" hint is wrong on the bracket rungs
- Where: `TIPS.pattern.parts` `:327`, "Look at the labels under the pattern."
- Repro: rungs 1, 3 and 8 draw brackets above the repeats, no labels under (frame pat-parts-3). The hint still says
  labels under.
- Fix: two lines, e.g. jumps: "Look at the jumps under the pattern." and brackets: "Look at the brackets. Each one shows
  the part that repeats." Add both to lines.json.

##### S4. At 375x667 the strategy tray covers the answer choices
- Where: `relayout` `:1620-1630`. Stack stage height is clamped to 340; the tray is about 210 px; `Hh = max(200,
  340 - 210)` draws a 200 px scene behind a 130 px window.
- Repro: 375x667 iframe, Pattern Ladder, tap a wrong choice: the choices sit under the tray (frame n375x667-pattern).
  375x812 is fine.
- Fix: in stack layout, grow the stage by the tray height when the tray opens (or set the minimum on the visible part,
  not on `Hh`), so the scene and tray both fit; the page may scroll, the choices must not be covered.

##### S5. Keyboard: after I'm stuck, focus stays on the panel and the cards are behind it
- Where: `$('stuck').onclick` `:1566`; `trayBuild` only moves focus if it was already in the tray (`:1060`).
- Repro: Tab to I'm stuck, Enter: the cards open, the next Tab goes to Back to gym. The cards come earlier in the DOM,
  so a keyboard user must Shift+Tab back through the puzzle to reach them.
- Fix: when I'm stuck opens the cards (and after a keyboard not-yet), focus the first card; Escape already returns focus
  to I'm stuck.

##### S6. The name "Brain Gym" (decision for Cory)
- "Brain Gym" is the registered name of a commercial movement program (Brain Gym International, Dennison) that schools
  know and that is widely cited as unsupported by evidence. A tool that is careful not to overstate brain claims, under
  that exact name, invites a teacher to assume it is that program, and the name could draw a trademark complaint.
- Suggestion: keep Bix and the gym look, rename the title, e.g. "Bix's Comeback Gym" or "Practice Gym". The concept title
  comes from `data/tools-concepts.csv:265`, whose description also says "mistakes make it stronger"; reword that too if
  it is shown anywhere.

#### Nits

- `H.goalsHave` ("You have a goal already...") `:307` is unreachable, confirmed: with a goal set the board renders only
  the active card (`goalsScene` `:1384`), so `pickGoal` with a different id cannot fire by mouse or keyboard. Drop it from
  `H` so it leaves `allLines()` and lines.json (it would be recorded for nothing).
- Comeback without a strategy: pressing I'm stuck and closing it, then solving, scores +3 and a stripe (`:700`), so a
  student can open I'm stuck before every rung and out-earn a first-try solve threefold. This is what the spec says, and
  it is generous rather than punishing; flag only in case Cory wants a comeback to need a real not-yet or a card.
- "Finish 3 rungs in one room in a row" counts replays of the same rung (`state.streak` `:706`); replaying rung 1 three
  times meets it. Count distinct rungs if it should mean three different rungs.
- Memory "Break it into parts" on rung 1 (3 pads) chunks as 2 then 1 (`chunks` `:778`); the spec says chunks of 2 or 3.
  Play 3 as one chunk (or 3 straight) for that rung.
- Entering a room by keyboard drops focus to body (the door is gone after render); focus the first puzzle target.
- Stage tab order puts the six Coach's corner cards (and up to six goal cards, nine mat squares) before the panel
  buttons; STANDARDS asks for panel controls first. Short lists, so minor.
- Locker at 680x425: sticker labels are 9.5 px and "Slow down and check" wraps into the row below; goal cards at 680 mix
  sizes ("Make 2 comebacks." renders larger than its neighbors because fitText fits each card alone).
- Pattern rung 9 choices at 680x425 are 55 px tall (spec: 60 px in rooms for the projector); fine in full screen.
- Panel goal line reads "Goal: Make 2 comebacks. 0 of 2 comebacks." Consider "Goal: Make 2 comebacks (0 of 2)."
- Print: no print styles. The header prints white on white and the stage SVG is cropped at the page edge (print-room,
  print-locker). Not a printing tool, so optional: a small `@media print` that hides header buttons and fits the SVG.
- Bix's hit box in the gym runs 2 px below the viewport at 1280x720 and up (shadow only).

#### Checked and fine

- Done when 1: Gym opens with Pattern Ladder and Memory Mirror open, three locked; a locked door rattles, hint "This
  room opens when you finish a goal. Go to Goals to pick one.", Pick a goal shows; tapping Bix plays `a-hop` with the
  bubble.
- Done when 2: wrong choice greys with "Not yet" (aria-label "Not yet: blue square"), cards slide up, face "thinking"
  (hand on chin, frame focus-notyet); Know-how only ever added (`addKH`; loadSave clamps at 0).
- Done when 3: not-yet, Break it into parts, solve: 0 to 4 Know-how and 1 stripe; first try +1; replay +0 ("Solved
  again! Replays are free practice."); goal finish +5.
- Done when 4: goals cb2, cards3, lnh opened Light Mat, Number Lift, Summit Circuit in order, each with the reflection
  card ("Light Mat is open now."); a fourth goal gives "Goal done! You did just what you set out to do."
- Done when 5: recomputed by brute force (512 press sets) and BFS: all 7 Light Mat starts have exactly the listed unique
  solution and fewest; all 7 Number Lift rungs match their fewest. Following the hint glow in the browser solved every
  Light Mat, Number Lift and Summit rung in exactly the fewest moves, with the star on every lift. Light Mat at the limit
  resets to its start with "Out of moves..."; Number Lift at the limit returns to 0 as a not-yet. (Except B2.)
- Done when 6: taps during playback ignored (pads read "Watch", aria "Star, watch"); Watch again replayed the identical
  sequence; timings traced: normal 0.7 s on, 0.3 s gap; Slow down 1.4 s on, 0.6 s gap; Break it into parts on 8 pads
  played 3, 3, 2 with an extra 1 s between chunks. (Except B1.)
- Done when 7: Save Bix then reload kept Know-how 23, 3 stripes, stage 2, Light Mat open, Mint, and showed "Welcome
  back!"; reload without Save started fresh (only `curio-motion` in storage); Start over asks first, focuses Yes, clears
  `curio-brain-gym`, returns to Gym stage 1.
- Done when 8: mode switch hushes and the next welcome plays; Read logs the current hint; Sound off queues nothing and
  Sound on queues the welcome; first tap on a door plays only the room line (welcome skipped unmarked); first tap on Read
  marks nothing. Motion off: no Bix move, no confetti (0 vs 48 pieces with motion), breathing still 3 s intro then six
  4.0 s phases, then "Ready to try again?".
- Done when 9: at every size listed the puzzle, I'm stuck, Back and all six cards are inside the viewport, no horizontal
  scroll anywhere (scrollWidth equals width at every size, 375 included). Except S4 at 375x667.
- Done when 10: no em or en dashes in src.html, notes.md, tool.draft.json, lines.json; every "Curio" in src.html is the
  kit's `Curio` object; no on-screen brain-grows claim (S2 is spoken).
- Lines: `allLines()` and voice/lines.json match exactly (88 each).
- Focus: 4 px orange ring with an ink halo on both HTML buttons and SVG targets. Orange on ink 6.3:1; the ink halo on
  paper 14.05:1, on the tray 14.64:1, on the cork board 5.86:1, on the Light Mat blue 3.05:1; in the header the orange
  sits on violet at 3.52:1. All at or above 3:1. Arrows move within doors, choices, pads and the 3x3 mat (row and column),
  Enter and Space tap, keys 1 to 3 switch modes, Escape closes the cards.
- Contrast of text: white on header 8.29:1, on buttons 6.17:1; muted on paper 6.29:1; white on Target tag 5.77:1.
- Copy reads at grade 3-5 level; Coach's corner cards say "practice helps", nothing about the brain growing; Take three
  breaths is one pause; nothing asks a student to disclose anything; no typing anywhere.
- One file, 129 KB, all metas present, no external src or url.

#### Re-verify (cold, 2026-10-26, after the rename to not-yet-gym)

**Verdict: FIX** (0 blockers, 4 should-fix, nits below). Both earlier blockers and all six earlier should-fix items are fixed.

How checked: rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py not-yet-gym` (1315 KB, under 2 MB; 89 clips inlined, no
external src, href or url, no em or en dashes, no "Brain Gym" anywhere in the bundle). Muted headless Chrome on private port 9851,
real held mouse clicks (80 to 120 ms), real keys and CDP touch events; 375 wide through an iframe host on 9111 served from my temp
dir. Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600, 375x812, 375x667, each in 13 states (gym,
pattern not-yet with cards, pattern parts, memory, memory/light/lift with cards, lift parts and slow, goals, plan, locker at stage 5
with 12 stripes, flipped fact, Ask a friend). Print to PDF of a room and the Locker. No console errors, exceptions or network
requests in any run (only the iframe host's own favicon 404).

##### Earlier findings, re-checked

- B1 fixed. Scene targets act on pointerdown (`src.html:1537`). Memory Mirror rung 3: 10 of 10 quick runs solved (6 at 120 ms
  hold and 160 ms gap, 4 at 80 ms hold and 120 ms gap); rung 6 (8 pads) at about 4 taps a second solved. Taps during playback
  are still ignored (pads read "Watch"); Watch again replays the same sequence. But see R2 (touch).
- B2 fixed. Number Lift rung 1, +5 then +5: floor 10 cannot reach 11, so a not-yet with "This floor can't get back to the
  target. The lift went back to floor zero." and the lift returns to 0. Rung 6 +1 x2 x2 +1 x2 then x2 to 20: same reset. Just try
  again now resets both Light Mat (start state, 0 moves) and Number Lift (floor 0, 0 moves). Following the hint glow solved all six
  lift rungs and the Summit lift in exactly the fewest moves with the star, and all six Light Mat rungs in the fewest presses;
  Light Mat at the limit resets to its start as a not-yet.
- S1 fixed: with "Reach a floor in Number Lift in the fewest moves." active, a fewest Light Mat solve leaves `G.few` at 0.
- S2 fixed: the stage-up line is "All that practice is paying off!"; stage 4 is "Smooth mover"; no stronger, grow or muscle copy
  on screen, in lines.json or in the clips ("strong learners" on fact card 4 is the spec's text).
- S3 fixed: rungs 1, 3 and 8 say "Look at the brackets. Each one shows the part that repeats."; jump rungs keep the labels line.
- S4 fixed: at 375x667 the stage grows by the tray height; the choices sit above the tray and are not covered (frame
  375x667-pattern-notyet). I'm stuck and Back to gym then sit below the fold while the cards are open, which is fine (the cards
  and the puzzle are what is needed then).
- S5 fixed: I'm stuck by keyboard focuses Try a new way; Escape returns focus to I'm stuck.
- S6 fixed in the tool: title, meta description, header, welcome line and its clip say "Not Yet Gym"; save key
  `curio-not-yet-gym`. But see R4 for the catalog.
- Nits fixed: goalsHave dropped (89 lines); "Finish 3 rungs in one room in a row" counts distinct rungs; Memory rung 1 parts plays
  as one chunk of 3; entering a room by keyboard focuses the first choice; Locker sticker labels 11 px or more at 680x425; the goal
  line reads "Goal: Make 2 comebacks (0 of 2)."; print styles hide the header buttons and fit the stage (one page each, dark on
  white); Bix's hit box stays inside the viewport.

##### Should fix

###### R1. Keyboard focus drops to body after most tray and panel actions
- Where: tray click handler `src.html:1087-1099`, `closeTray` `:1045`, `leaveRoom` `:686`, `$('next').onclick` `:1607`,
  `pickPlan` `:1010`, `changeGoal` `:1015`, `reflect` `:1033`, `yesOver` `:1620`.
- Repro (keyboard, Enter on each): a strategy card (Use a hint, Slow down, Try a new way and so on), the cards' close button, Just
  try again, Skip on the breathing card, Show a friend's idea, Next rung, Back to gym (panel and the Room complete tray), a plan
  card, Change goal, a reflection card, Yes, start over. After each, `document.activeElement` is `body` and the next Tab starts
  again at the Gym mode button. Only I'm stuck, Escape, Start over and Cancel, goal cards, facts and doors keep focus.
- Fix: one helper that, after a tray closes or a panel button disappears, focuses the next sensible target: the first puzzle
  target (or I'm stuck) in a room, the door of the room just left on the map, the active goal card in Goals, the first door after
  Start over, the first puzzle target after Next rung.

###### R2. A scroll swipe that starts on a target counts as a tap (regression from the B1 fix)
- Where: `sv.addEventListener('pointerdown', ...)` `src.html:1537`; `#sv` has `touch-action:manipulation`, so the page still pans.
- Repro: 375x667 iframe host with touch emulation, Pattern Ladder rung 1: touchstart on a wrong choice, move up 140 px, touchend.
  The page scrolled 125 px and the choice greyed out as "Not yet" with the strategy cards open. In the stack layout (phones,
  tablets, touch Chromebooks in a narrow window) a child scrolling past the puzzle picks answers or adds Memory pads by accident,
  which is the B1 harm (a false "Not yet") by another route.
- Fix: keep pointerdown for mouse and pen; for `pointerType === 'touch'` remember the `data-k` on pointerdown and act on pointerup
  only if the finger moved less than about 10 px (drop it on `pointercancel`). Keying by `data-k`, not by the element, still
  survives a re-render between press and release, so B1 stays fixed.

###### R3. "Keep going after 5 not-yets" finishes without the reflection card
- Where: `retry()` `src.html:694-698` calls `goalCheck()` before the answer is judged; `solve()` then reaches `closeTray()`
  (`:738`), and `notYet()` opens the cards tray, so the reflect tray that `goalCheck` just opened is replaced at once.
- Repro: pick "Keep going after 5 not-yets." with a plan, reach 4 of 5, then in Pattern Ladder a wrong choice, close the cards,
  the right choice. The goal is done (+5 Know-how, Summit Circuit opens) but no "Goal done! What helped most?" card shows; the hint
  reads "A comeback! Press Next rung when you're ready." and the panel says "No goal yet." (frame goal3b-keep5). Done when 4 asks
  for the reflection card each time. The same overwrite happens when the goal ends on a wrong answer, and when "Use 3 different
  strategy cards." ends on Ask a friend (the friend tray is replaced by the reflection).
- Fix: in `retry()` only count (`S.G.keep++`), and run the goal check after the puzzle action settles (end of `solve`, `notYet`
  and `useCard`), or have the tray keep a pending reflection on screen until it is answered or skipped.

###### R4. The concept source still says "Brain Gym" and "mistakes make it stronger"
- Where: `data/concepts/electives.txt:132` reads `sel-3-5-growth-mindset-and-goals|Brain Gym|creature||Train a brain character
  through challenges; mistakes make it stronger and goals unlock new areas.` `scripts/check_concepts.py --write` rebuilds
  `data/tools-concepts.csv` from these files, so its next run turns row 265 back into Brain Gym: the tool id stops matching its
  folder, and the site shows the trademarked name and the muscle claim again. Also stale until regenerated: `docs/BUILD-BOARD.md:20`
  (written by board.py) and the built site in `dist/` (a `/tools/brain-gym/` bench page; the grade 3, 4, 5 and 3-5 pages say
  "Brain Gym").
- Fix: change electives.txt line 132 to `Not Yet Gym` with the csv's new description ("practice and comebacks level it up and
  goals unlock new areas"), run `check_concepts.py --write`, `board.py` and `build_site.py`, and confirm no `brain-gym` path or
  "Brain Gym" text remains in dist.

##### Nits

- Gym backdrop: no people anywhere (checked the chosen `art/gym-hall.webp` and all three candidates). It sits well behind the 40
  percent white overlay and the drawn floor from 375 to 1000 wide, but at 1366 and 1920 the picture's own climbing wall and a white
  shelf of orange objects peek out beside the drawn Summit climbing wall (frames 1366x768-gym, 1920x1080-gym), so two climbing
  walls show, one half hidden. Anchor the slice so the right edge crops (for example `preserveAspectRatio="xMinYMid slice"`), or
  regenerate without the wall and shelf, since the scene draws its own. Art review in prompts.json is still "pending" for Cory.
- Goals board at 680x425: the last line of "Remember a 5-step pattern in Memory Mirror." and of "Reach a floor in Number Lift in
  the fewest moves." crosses the card's bottom edge at the 11 px floor, and card text sizes still differ ("Make 2 comebacks." is
  larger). Use three columns for 7 or 8 cards in short boxes, or fit all cards to one shared size.
- Pattern rung 9 choices are 54 px tall at 680x425 and at 375 wide (spec asks 60 px in rooms); fine in full screen.
- Light Mat still shows "Fewest moves! Press Next rung when you're ready." though only Number Lift has the star (harmless).
- Stage targets still come before the panel buttons in Tab order (doors, then Bix, then the panel).
- Not user-facing, stale after the rename: `spec.md:3` says "Folder and id stay brain-gym for now" and `spec.md:158` names the
  save key `curio-brain-gym`; `voice/local.json` keeps three old keys ("Welcome to the Brain Gym!...", "I feel stronger at this
  already!", the dropped goalsHave line).

##### Checked and fine

- Done when 1: two open doors, three locked ("Light Mat, locked"); a locked tap gives the goal hint and Pick a goal; tapping Bix
  plays `a-hop` with a bubble.
- Done when 2: a wrong choice greys with "Not yet" (aria "Not yet: blue square"), the cards open, the face is `thinking`;
  Know-how only rises.
- Done when 3: not-yet, Break it into parts, solve: 0 to 4 Know-how and 1 stripe; first try +1; replay +0 ("Solved again!
  Replays are free practice."); I'm stuck then solve +3 and a stripe (the spec's rule).
- Done when 4: cb2, cards3 and keep5 opened Light Mat, Number Lift and Summit Circuit in that order; room goals join the board
  only once their room opens; reflection cards for cb2, cards3 and lnh (except R3).
- Done when 5 and 6: as above under B1 and B2.
- Done when 7: Save Bix, reload: Know-how 23, 3 stripes, stage 2, Light Mat open, Mint, "Welcome back!"; Start over asks first,
  focuses Yes, clears the key; reload without Save starts fresh (only `curio-motion` stored).
- Done when 8: mode switches hush and queue the next welcome; the first tap on a door plays only its room line; Read logs the hint
  and marks nothing; Sound off queues nothing and Sound on queues the mode's welcome. Motion off: no Bix move, 0 confetti (48 with
  motion), breathing intro 3.0 s then six phases 4.0 s apart, then "Ready to try again?".
- Done when 9: at every size the puzzle, I'm stuck (while the cards are closed) and all strategy cards are inside the viewport,
  the tray never covers a scene target, no horizontal scroll, scene text 11 px or more.
- Done when 10: no brain-grows claim; no em dashes in src.html, notes.md, tool.draft.json or lines.json.
- Voice: `allLines()` equals voice/lines.json exactly (89 lines, same order); every line has its clip (89 mp3, no orphans), clip
  rates 8.8 to 18.4 characters a second (none cut off); in a session of 8 spoken lines, 8 clips played and the browser voice was
  never used.
- Focus ring: 4 px orange with the ink halo on SVG targets and tray buttons (frames focus-door, focus-card); arrows move within a
  group.

#### Re-verify 2 (cold, 2026-10-26, after fix round 2)

**Verdict: FIX** (0 blockers, 1 should-fix, nits below). R2, R3 and R4 are fixed. R1 is fixed on every click path, but one timer path is left (R5).

How checked: rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py not-yet-gym` (1318 KB, under 2 MB, no "no recording yet"
lines). Own muted headless Chrome on private port 9991 and an http server on 9211, both from my temp dir, both stopped by process id
at the end. Real held mouse clicks (80 to 120 ms), real keys, and real CDP touch events with mobile emulation (5 touch points,
pointer coarse) at 375x667 and 375x812. Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 760x600, 375x812,
375x667, each in 10 states (gym, pattern not-yet with cards, memory and light with cards, lift parts, summit, goals, plan tray,
reflection tray, locker at stage 5 with 12 stripes and a flipped fact). No console errors, exceptions or outside network requests in
any run (only my own server's favicon 404). `check_tools.py` lists it as draft.

##### Earlier findings, re-checked

- R1 mostly fixed (`focusNext`, `src.html:1661`). By keyboard (Enter on each): every strategy card, the cards' close, Just try
  again (pattern, light, lift), Watch again (tray and scene), Skip on the breathing card, Ask a friend and Show a friend's idea, Next
  rung, rung buttons, Back to gym (panel and Room complete), goal card, plan card, Make a plan, Change goal, reflection card and Skip,
  Save, swatches, Start over, Cancel and Yes, start over. None leaves focus on body: in a room it lands on the first live puzzle target
  (or I'm stuck during Memory playback), on the map on the door just left, in Goals on the active goal card, after Yes on the first
  door. Greyed lift buttons and the lift's dead-floor reset keep focus. What is left is R5.
- R2 fixed (`src.html:1555-1571`). A 140 px touch swipe starting on a wrong Pattern choice: the page scrolled 125 px (375x667) and
  182 px (375x812), no choice greyed, no cards. A swipe starting on a door: the page scrolled, the room was not entered. A 6 px jitter
  tap still counts (choice greyed, cards open); touch taps close the cards and solve (+3, 1 stripe). Memory rung 3 by touch taps
  (80 ms hold, 160 ms gap) solved at both sizes.
- B1 still fixed with the mouse: Memory rung 3, 10 of 10 quick runs solved (6 at 120 ms hold and 160 ms gap, 4 at 80 ms and 120 ms);
  rung 6 at about 4 taps a second, 3 of 3. A tap during playback is ignored (pad aria "Star, watch", position stays 0).
- R3 fixed. "Keep going after 5 not-yets" ending on a right answer: the reflection card shows ("Goal done! What helped most?"), +5,
  Light Mat opens. Ending on a wrong answer: the cards stay up (`pendRef`) and the reflection follows when they close (by a card, by
  Back to gym on the map, by a mode switch to Locker, or by a rung button). "Use 3 different strategy cards" ending on Ask a friend:
  the friend tray stays, Show a friend's idea shows the bubble and then the reflection. Ending on Take three breaths: the reflection
  opens when the breathing ends. "Make 2 comebacks" ending on the last rung: Room complete shows, then the reflection after Back to
  gym. Real play of cb2, cards3 and keep5 opened Light Mat, Number Lift and Summit Circuit in that order, each with its "... is open
  now." line.
- R4 fixed: `data/concepts/electives.txt:132` and `data/tools-concepts.csv:265` read "Not Yet Gym" with "practice and comebacks level
  it up"; `docs/BUILD-BOARD.md` and `dist/` have no "Brain Gym" or `brain-gym` (dist has `tools/not-yet-gym`; the grade 3, 4, 5, 3-5,
  bench, SEL, creature and CASEL pages say Not Yet Gym).
- Earlier nits now fixed: the goals board at 680x425 (all eight cards fit at one shared size); Pattern rung 9 choices are 72 px tall
  at 680x425 and 375 wide (were 54); spec.md now names the folder and save key `not-yet-gym`.

##### Should fix

###### R5. Focus drops to body when the breathing card ends on its own
- Where: `endBreath` `src.html:988-998` closes the tray from a timer; `focusNext` only runs after a button click (`:1676`).
- Repro (keyboard): in Pattern Ladder, Enter on I'm stuck, Enter on Take three breaths (focus goes to Skip), then wait the 27 s. The
  tray closes, Skip is removed and `document.activeElement` is body; the next Tab starts again at the Gym mode button. Same when that
  card finishes a goal: the reflection card opens with focus on body. Letting the breaths run is the card's normal use (Skip is the
  exception), so every keyboard user who takes this card loses their place. Same harm as R1, on the one path the click hook misses.
- Fix: at the end of `endBreath` (not the quiet path), call `focusNext()` when focus was in the tray, as the click path does.

##### Nits

- When a pending reflection opens after the cards or friend tray close (`closeTray` `:1048`), the panel hint keeps the puzzle hint
  (for example "Say it out loud: circle, square...") instead of "Goal done! What helped most? Tap a card, or Skip.", so Read speaks
  the old hint. Set `H.reflect` there.
- Gym backdrop at 1920x1080: the picture's own white shelf still peeks out behind Number Lift, and its climbing wall shows at the
  right edge beside the drawn Summit wall (frame s-1920x1080-gym). Art review is still pending for Cory.
- Light Mat still shows "Fewest moves! Press Next rung when you're ready." though only Number Lift has the star (harmless).
- Stage targets still come before the panel buttons in Tab order.
- Not user-facing: `voice/local.json` keeps three old keys ("Welcome to the Brain Gym!...", "I feel stronger at this already!", the
  dropped goalsHave line).

##### Checked and fine (regression sweep)

- Done when 1: two open doors, three locked ("Light Mat, locked"); a locked tap gives "This room opens when you finish a goal. Go to
  Goals to pick one." and Pick a goal; tapping Bix plays `a-hop` (with motion on).
- Done when 2 and 3: a wrong choice greys ("Not yet: blue square"), the cards open, the face is `thinking`; not-yet, Break it into
  parts, solve: 0 to 4 Know-how and 1 stripe; first try +1; replay +0 ("Solved again! Replays are free practice.").
- Done when 4: as under R3.
- Done when 5: following the hint glow with real clicks solved all six Light Mat rungs (1, 2, 2, 3, 4, 5 presses) and all six
  Number Lift rungs (3, 3, 2, 4, 5, 6 moves, star on each) in exactly the fewest, and the Summit lift in 5 with the star. Light Mat at
  its limit (5 presses on rung 1) resets to `#.#...#.#` as a not-yet; Number Lift rung 2 at its limit returns to floor 0 as a not-yet.
- Done when 6: timings traced on rung 6: normal 0.7 s on, 0.3 s gap; Slow down 1.4 s on, 0.6 s gap; Break it into parts 3, 3, 2
  with about 1.3 s between chunks; Watch again replays the same sequence.
- Done when 7: Save Bix then reload: Know-how 26, 3 stripes, stage 2, all rooms, Mint, "Welcome back! Let's keep practicing.";
  storage holds only `curio-not-yet-gym` (plus `curio-motion` once Motion is pressed); Start over focuses Yes, then clears the key and
  returns to Gym; reload without Save starts fresh with nothing stored.
- Done when 8: mode switches hush and play the new mode's welcome once; Read logs and speaks the current hint; Sound off queues
  nothing, and Sound on does not repeat a welcome already said. Motion: with no reduced-motion preference Bix hops and the Summit
  gives 48 confetti pieces; Motion off (stored "calm"): no Bix move, 0 confetti, breathing intro 3.0 s then six phases 4.0 s apart,
  then "Ready to try again?" at 27.0 s.
- Done when 9: at all ten sizes and states, no horizontal scroll, every puzzle target and door inside the viewport and never under
  the tray, every tray button inside the viewport, I'm stuck visible while the cards are closed, no scene target under 44 px, scene
  text 11 px or more (frames s-<size>-<state>).
- Done when 10 and words: no em or en dashes in src.html, notes.md, tool.draft.json, lines.json or the bundle; no "stronger",
  "grow", "muscle" or "neuron" in anything a user sees (notes.md only says the tool never claims the brain grows like a muscle;
  "strong learners" on fact card 4 is the spec's text); no "Brain Gym" in the bundle, src, notes, tool.draft.json, lines.json, the
  catalog or dist; every "Curio" in src.html is the kit object.
- Voice: `allLines()` equals voice/lines.json exactly (89 lines, same order), 89 mp3 clips, none missing; the new welcome and
  stage-up clips were re-recorded after the rename. In one session 16 lines started, 16 clips played, and the browser voice was never
  used.
- Print: a room and the Locker each print to one page, header buttons hidden, dark on white.

#### Integrator fix (R5)

endBreath now remembers whether focus was inside the tray and calls focusNext() after the tray closes, so a breathing card that ends on its own timer hands focus back to the puzzle (checked in headless Chrome: after the 27 s card, focus was on the first choice, not the page body). The reflection-hint nit was left as is.

<!-- end part -->

## Art and voice

<!-- part: art-plan.md -->

### Comeback Club art plan

(Renamed from Not Yet Gym on 2026-10-26; Cory picked "Comeback Club" from the Name table below.)

Cory's review: "name is okay but im sure there is a better one. graphics could use a bit for work". Today the one image
is the FLUX backdrop `art/gym-hall.webp` (50 KB); Bix, Dot, the doors, the climbing wall, the room views, the goal board
and the locker are drawn in code. This plan paints Bix and Dot (gpt-image-2 through Codex) and gives every scene a
painted setting (Cloudflare FLUX), while keeping everything that carries text, state or accessibility in code. Prompts
are in `art/prompts.json` (20 new entries after `gym-hall`, which stays as it is). Nothing is drawn or wired yet.

#### Bix: six paintings, five colors, gear on top

Bix has six faces (`bix()` face branches, src.html 589-607), five color swatches (`COLORS`, 272-273), four pieces of gear
that drop on by stage (`gearOf`, 553) and a headband that shows the comeback stripe count (573-581). Painting every
combination is out of the question, so:

- **One painting per face, in a pale neutral.** Bix is painted near-white with lavender-grey shading and dark plum limbs.
  The tool tints the image to the chosen swatch with an SVG multiply filter, one per color, defined once in `render()`'s
  `<defs>`: `<filter id="tint-pink" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="r 0 0 0 0 0 g 0 0 0 0 0 b 0 0 0 0 0 1 0"/></filter>`
  with r, g, b = the swatch / 255. Dark plum lines and eyes stay dark; the pale body takes the color with its shading.
  (Pink #f6b3c8 is 0.96, 0.70, 0.78; Mint #9fe3c9 is 0.62, 0.89, 0.79.) The ink-on-swatch contrast ratios in spec.md
  hold, since the body ends up the swatch color or a little darker in shade only.
- **Gear stays separate.** The headband stays code (it shows 0 to 10 stripes or "x12"), drawn as a slightly curved strip
  between two anchor points on the forehead instead of clipped to the old `BLOB` path. Sneakers, gym bag and medal
  become small FLUX cutouts placed at anchors. All four keep the `a-drop` stage-up animation.
- **Anchors.** After each pick, measure and store per painting, as fractions of the image:
  `ANCHOR['bix-cheer'] = {fx, fy, bandL, bandR, bandY, chest, shoulder, handL, handR, bodyH}` (feet center, band line,
  medal point, bag strap start, hands for juggling, and the body height so all six paintings draw the body at one
  scale even though cheer's raised arms make its image taller).

| Face (spec) | When (src.html) | Painting | Notes |
|---|---|---|---|
| happy (idle) | Gym map 1169, Locker 1485, room default | `bix` | also the arms-down frame of jumping jacks |
| focused | room with a puzzle showing (696, 991) | `bix-focused` | |
| thinking | after a not-yet (701) | `bix-thinking` | hand under chin; curious, never sad |
| cheer | comeback (730), goal done (1027) | `bix-cheer` | arms up; also the arms-up jacks frame and the juggling pose |
| proud | first-try solve (731) | `bix-proud` | thumbs up |
| calm | breathing card (973) | `bix-calm` | under the `a-breathe` scale |

##### Moves (stage taps, `act` 1535) with paintings

- hop, spin, cartwheel, big jump, breathe: whole-figure CSS transforms on `.bxw`, as now (136-158). No change.
- jumping jacks: today `.armsd` / `.armsu` swap two code arm groups (140-143). With paintings, `.armsd` holds the
  `bix` image and `.armsu` the `bix-cheer` image, same steps(1) keyframes.
- juggling: shows `bix-cheer` while `.a-juggle` runs, code balls (`.balls`, 146-152) re-aimed at the hand anchors.

##### Changing faces

Two `<image>` elements in the Bix group (outgoing and incoming); the incoming one fades in over 250 ms and the outgoing
one fades out, driven by the existing `anim()` / `animAttr()` pair so a re-render mid-fade continues instead of
restarting (a new `anims.face = {from, to}`). When Motion is off (`Curio.reduce`), the swap is instant and no move
animations play, exactly as today. The stage-up glow (`#bxglow`, 1115) stays code.

#### Assets

Codex = `python scripts/gptart.py comeback-club <names>` (gpt-image-2, the only source for characters with faces or hands;
these are `"people": true` so the FLUX scripts skip them). FLUX = `python scripts/cfart.py comeback-club <names>`
(Cloudflare FLUX.2 klein, free; it uses the `"sd"` prompt and adds "No people."). Cutouts are on green (none of them is
green; Dot is lilac, the climbing wall's green holds sit inside the panel and survive the key because the cutout keeps
interior pixels, but check them).

| # | Name | Source | Replaces (src.html) | Display size (CSS px) | Output | Budget (WebP) |
|---|---|---|---|---|---|---|
| 1 | bix | Codex | `bix()` 554-617 and `BLOB` 548-552, happy face | Gym 80-260 tall, room 64-190, Locker 90-420 | 1:1, h 480, q 72, cutout | 22-30 KB |
| 2 | bix-focused | Codex, ref bix | same, focused face | same | same | 22-30 KB |
| 3 | bix-thinking | Codex, ref bix | same, thinking face and arm | same | same | 22-30 KB |
| 4 | bix-cheer | Codex, ref bix | same, cheer face and arms up; jacks up frame | same | same | 22-30 KB |
| 5 | bix-proud | Codex, ref bix | same, proud face and thumbs up | same | same | 22-30 KB |
| 6 | bix-calm | Codex, ref bix | same, calm face | same | same | 22-30 KB |
| 7 | dot | Codex, ref bix (style) | `dot()` 618-624 | 32-95 tall | 1:1, h 240, q 72, cutout | 8-12 KB |
| 8 | door | FLUX | door rect, inner panel and knob in `gymScene` 1146-1149 | 56-132 x 84-210 | 9:16, h 360, q 70, cutout; tinted per room | 10-14 KB |
| 9 | padlock | FLUX | code padlock 1154-1156 | 20-40 | 1:1, h 120, q 72, cutout | 3-5 KB |
| 10 | climb-wall | FLUX | Summit wall rect and holds 1139-1143 | 70-165 x 40-120 | 16:10, w 400, q 70, cutout | 12-18 KB |
| 11 | sneaker | FLUX | code shoes in `bix()` 561-563 (one image, mirrored) | 10-90 wide | 4:3, w 128, q 72, cutout | 4-6 KB |
| 12 | gym-bag | FLUX | code bag in `bix()` 565-566 (strap stays a code line) | 25-130 wide | 4:3, w 200, q 72, cutout | 5-9 KB |
| 13 | medal | FLUX | code medal in `bix()` 609 | 15-110 tall | 3:4, h 160, q 72, cutout | 4-7 KB |
| 14 | room-pattern | FLUX | flat `#roomBg` gradient in `roomScene` 1187 | full stage | 16:10, w 1280, q 58 | 22-32 KB |
| 15 | room-memory | FLUX | same | full stage | same | 22-32 KB |
| 16 | room-light | FLUX | same | full stage | same | 22-32 KB |
| 17 | room-lift | FLUX | same | full stage | same | 22-32 KB |
| 18 | room-summit | FLUX | same (Summit rungs) | full stage | same | 22-32 KB |
| 19 | board-cork | FLUX | cork fill and 70 speckles in `goalsScene` 1406-1409 | inner board rect | 16:10, w 1024, q 56, texture | 30-40 KB |
| 20 | locker-room | FLUX | locker row and floor in `lockerScene` 1474-1478 | full stage | 16:10, w 1280, q 58 | 28-40 KB |

Codex images: 7 first draws (bix first, alone; the five variants with plain `"ref": "bix"` so it is the same character;
Dot with `"ref_mode": "style"` so it is a different character drawn the same way). Allow 2-3 redraws, most likely for
the thumbs-up hand or a variant that drifts off the pale body color. FLUX: 13 assets, free, about 3 candidates each.

#### Size

Measured 2026-10-26: `python scripts/bundle_tool.py not-yet-gym` (now comeback-club) gave `not-yet-gym.html` at 1,352,634 bytes
(1,321 KB; the script prints 1319). The limit (`scripts/check_tools.py`) is 2 x 1024 x 1024 = 2,097,152 bytes, so
**headroom today is 744,518 bytes (727 KB of bundle, about 545 KB of WebP after base64)**. Of today's bundle, recorded
speech is 1,145 KB of base64 and the gym-hall image 67 KB.

| | New art as files | In the bundle (x 4/3) | Bundle after | Headroom after |
|---|---|---|---|---|
| Target (middle of each budget) | 419 KB | 559 KB | about 1,880 KB | about 168 KB |
| Every asset at its cap | 491 KB | 655 KB | about 1,976 KB | about 72 KB |

Both are under the 600 KB guide and under 2 MB. Removing the vector Bix, Dot, door, wall and padlock code saves a few
KB more. If it gets tight: drop a painting to quality 66 with `art.py --rekey` (free); drop `board-cork` (keep the code
cork, 35 KB); or set `"kbps": 16` in `voice/lines.json` (speech is most of the bundle; that roughly halves it if the
lines are recorded above 16 kbps today). `gym-hall` stays, so nothing is freed there.

#### Draw order

1. `bix` alone (Codex). Pick it (`python scripts/localart.py comeback-club --pick bix:20`) so `art/raw/bix.png` exists for
   the refs. Check it tints well: try it under the pink and mint filters before going on (pale, evenly lit body, no
   pink patches, no text).
2. The five variants and Dot:
   `python scripts/gptart.py comeback-club bix-focused bix-thinking bix-cheer bix-proud bix-calm dot`
   Look at all six Bix side by side: same body shape, same size of body, all front facing, thinking never sad.
3. FLUX objects and scenes (free, 3 candidates each):
   `python scripts/cfart.py comeback-club door padlock climb-wall sneaker gym-bag medal --n 3`
   `python scripts/cfart.py comeback-club room-pattern room-memory room-light room-lift room-summit board-cork locker-room --n 3`
   Pick with `localart.py --pick name:<k>` (FLUX candidates are k 9 to 11).
4. Review every image (Bix hands and faces, no lettering anywhere, rooms plain in the middle), set `review` in
   prompts.json.

#### Wiring notes (phase 2)

- `bix(o)` keeps its signature `{x, y, h, face}`: it places `art:bix-<face>` (happy uses `art:bix`) by the feet anchor,
  scaled by `bodyH`, with `filter="url(#tint-<color>)"`; then the band strip, sneakers, bag and medal at anchors.
  The `deco`, `.bxw` and animation classes stay where they are.
- `dot()` becomes one `<image href="art:dot">` placed by its feet.
- Doors: the painted door is tinted with a per-room filter (five filters plus a "locked" grey one, built from
  `ROOMS[room].door` and the existing `mix(..., '#c7c2d3', .65)`); the plaque, labels, star and padlock image draw on
  top. The `a-rattle` group wraps the image too.
- Rooms: `roomScene` draws `art:room-<P.room>` full frame (slice) with a `#fbf7ff` rect at about .55 on top, then the
  floor strip, title and puzzle as now. Summit rungs use `room-summit`.
- Gym map: keep `gym-hall`. Optional, free: lower the white overlay (1126) from .4 to about .25 and the code floor
  (1128) from .92 to about .6 so the painted wood shows through.
- Goals: `board-cork` is clipped to the inner board rect (`<clipPath>` with the rx 8 rect), slice.
- Locker: `locker-room` full frame (xMidYMax slice) with a light paper overlay; the code floor band can go if the
  painted floor lines up at 74% height, otherwise keep it at reduced opacity.
- Check every size in STANDARDS.md (680x425 preview, 1366x768, 375 wide): Bix in the room corner at 64 px must still
  show its face; the tinted door must keep the plaque readable.
- Update spec.md (Art, Look, "drawn in code" lines), notes.md (Good to know), the src.html header comment (lines 20-21)
  and tool.json sources: add "Illustrations generated with OpenAI gpt-image, edited for Curio Class" and the
  Cloudflare FLUX.2 klein (Apache 2.0) credit next to the FLUX.1-schnell one. Rebuild preview.svg
  (`scripts/preview.py comeback-club`), it shows the vector Bix.

#### What stays vector

- The headband and its stripes or "x12" count; the stage-up glow; juggling balls; confetti.
- Every puzzle: pattern items, Memory Mirror pads (shape plus name, never color alone), the Light Mat squares, the Number
  Lift car and buttons, rung labels and brackets. These carry state and must stay crisp and accessible.
- The door name plaques and labels, goal cards, Done column, sticker wall and icons, Coach's corner cards, speech
  bubbles and banners: all text.
- The floor strips and baseboards where a painted floor would not line up across stage shapes.

#### Name

Not renaming anything; these are options for Cory. "Brain Gym" is out (registered to Brain Gym International). Also
avoided: "The Power of Yet" (Dweck's talk title and a Sesame Street song), "Brainology" (a Mindset Works product),
"Unstuck" (an existing self-help app) and anything with "Level Up" (crowded in app marks). Checked by web search on
2026-10-26: no trademark or kids app found for the five new names below. That is a quick check, not a clearance; a
USPTO search in class 41 (education) and 9 (software) is the real one before a rename.

| Name | Why |
|---|---|
| Not Yet Gym (keep) | Says the idea in two words ("not yet" means still learning); already live, voiced and in every file. |
| Bix's Comeback Gym | Names the mascot and the core rule: comebacks are worth more than first tries. The verify report suggested it. |
| Comeback Climb | The journey up to Summit Circuit plus the comeback stripes; no "gym" or "brain" baggage at all. |
| Comeback Club | Short, friendly, sounds like something a class joins; a student design project used it, no mark found. |
| Practice Gym | Plainest and most honest about what the tool claims (practice helps); easy for a teacher to search for. |
| Second Try Gym | Kid-readable version of the "not yet" idea; puts the moment after a mistake in the title. |

If Cory picks one with "Comeback", the welcome line ("Welcome to the Not Yet Gym!") and the title need re-recording
(one voice line, `voice.py`).

Decision 2026-10-26: Cory picked **Comeback Club**. Title, id, folder, save key and the welcome line changed; the
welcome line still needs recording.

#### Questions for Cory

1. Bix's five color swatches: tinting one pale painting works but each swatch is a tint, not a hand-painted color. OK,
   or cut the swatches to fewer (or none) and paint Bix in one color?
2. Gear (sneakers, bag, medal) from free FLUX next to a Codex Bix may not match in style. Accept and redraw if it
   clashes, or spend 3 more Codex images on gear with `"ref_mode": "style"`?
3. "Dot" is also the hedgehog in walk-in-their-shoes (3-5, a neighbor). Fine, or give the friend another name later
   (no rename now)?
4. Gym hall: keep `gym-hall` with a lighter overlay (free), or also redraw it?

<!-- end part -->

## Log

- 2026-11-25: verify.md folded in (last changed 2026-10-26)
- 2026-11-25: art-plan.md folded in (last changed 2026-10-26)
