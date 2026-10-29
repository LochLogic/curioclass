PASS (re-check 2026-10-29: blocker 1 and should-fix items 2 and 3 fixed and verified, no regressions)

# stage-blocker: Final look

Cold Final look, 2026-10-29, on the bundle in the worktree (tools/stage-blocker/stage-blocker.html, 427,404 bytes,
built after src.html). All 15 recorded clips (local Qwen3-TTS, firm-captain) are embedded, keyed by their text. Each is
byte-identical to voice/<sha1>.mp3, and the 15 keys match voice/lines.json and `L` in src.html exactly.
drive.py ran on Chrome port 9242 and audit_tool.py on 9241. 375 wide ran through a copy of the bundle with a host page
in my scratch folder, served on 8815, so the tool folder was not touched. Frames are under
S:/CurioClass-codex-scratch/final/stage-blocker/: f/ = frames, v/ = voice runs, audit/ = audit frames and audit.md.
Every Chrome and server I started is closed. There are no art files: the plan, seat view, figures and set are drawn
in code and art/prompts.json has no assets, so check 2 covers the drawn pictures.

## Blockers

1. **"Has the focus" passes with the actor in the dark** (family:stage). This is The Trophy, beat 1, at its default
   state. Coach stands on the upstage platform in USC, and USC is off by default (USR, USC and USL are all 0).
   The House view tags him "Co full front, in the dark" but still puts the eye on him ("the eye goes here", focus 5:
   +3 speaking, -3 in the dark, +2 full front, +1 on a level...). The note "Coach has the focus" shows a check on load,
   so beat 1 reads as done before the student touches it.
   - The eye stays on Coach in the dark in beat 3 as well (f/house-1920-sel.png). That note, "Riley has the focus",
     fails correctly.
   - A page sweep turned every light off on each focus beat in the three scenes. Trophy beat 1 stays met with the
     whole stage dark.
   - Why it is a blocker: a note that passes while the speaker cannot be seen teaches the opposite of the light rule
     that the tool itself shows. This is the same class as refine blocker 2 ("a check must not pass the opposite of
     the lesson"), and REFINE Rounds says a misleading meter is a blocker.
   - Frames: f/house-trophy-b1-default.png, f/block-trophy-b1-default.png, f/lights-off-trophy-1366.png.
   - Fix direction: a "has the focus" note also needs the actor lit (half, full or in the spot). The why text could
     read "Coach is in the dark (USC is off). Light USC or use the spot." Change the spec's note-rule sentence, the
     engine and docs/families/stage.md together, as for blocker 2. The handoff already says the coach "has to be lit
     by the student for some beats", so this fix makes the scene do what was intended.
   - The default for beat 1 then fails, with a clear fix to make (light USC).

## Should fix

2. **After a run, the results list is below the fold** (general). The run-end hint says "Tap a note to jump to its
   beat." At 1366x768 the first two failures show under the seat grid. At other sizes no note can be seen:
   - At 680x425 and 800x500 the 5 x 3 seat grid and Balcony fill the panel, so no note is in view. At 800x500 only
     the top of "4 of 11 notes met" shows.
   - In the stacked layouts (760x900, and 375 through the host) the results start at about 880 px or lower.
   - A solo student hears "Some notes need work. Tap a note" and sees nothing to tap.
   - Frames: f/run-end-680.png, f/run-end-800x500.png, f/run-end-760x900.png, f/run-end-375.png; compare
     f/run-end-1366.png.
   - Fix direction: once a run has finished, put the result summary and list above the seat grid, or fold the grid
     into a "Change seat" row, or scroll the panel to the results with preventScroll on the page.
3. **Tapping the mode button you are already on cuts that mode's welcome for good** (general). `setMode` always calls
   `V.hush()`, even when the mode does not change. The welcome is marked said when it starts, so it never comes back.
   - The audit's two quick taps, 0.7 s apart, cut welBlock, welHouse and welRun mid-line ("never heard whole":
     audit/audit.md, "Two quick taps").
   - The real clips run 2.8 s (welRun) to 5.8 s (welBlock), so a child's double tap easily cuts one, and the first
     tap on Block, which is already on, is a likely first tap.
   - Fix direction: return early from setMode when the mode does not change (`m === state.mode` and not running),
     so there is no hush and no new welcome.

## Polish

4. **The seat view leaves a dead band in House and Run at 1366x768, 1920x1080 and 760x900** (general; this was the
   exit check's known polish, and it is more visible now that the tool is finished). The perspective view ends at the
   stage floor, then about 190 px (1366) to 260 px (1920) of empty dark sits above the caption. A teacher projecting
   at 1920x1080 sees the actors in the top 60% of the stage area. Better would be to frame the view to the whole
   area, or to set the caption and mini map right under the floor. Frames: f/house-1366.png, f/house-1920-sel.png,
   f/run-mid-1366.png, audit/state-mode-run-760x900.png.
5. **A Run of The Note takes about 37 s of mostly still frames** (general). The beat holds are max(2200,
   1400 + 75 per character of line and direction), so beat 1 holds 8.2 s. From "Places, please" (5.5 s) to runSome
   (42.4 s) is about 37 s with no actor voices, only captions. As a solo student it felt slow on the default blocking,
   where little moves. A shorter hold (about 1200 + 55 per character) or a "Skip to notes" control would keep the
   payoff close. Frames: f/run-t13.png, f/run-t16.png, f/run-t21.png, f/run-t30.png.
6. **Unlit actors look almost lit in the House view** (family:stage). Coach "in the dark" is drawn a shade darker
   than the others but plainly visible. A clearly dimmed figure (and dimmed tag) would show the light lesson the
   notes check. Frame: f/house-trophy-b1-default.png. This goes with blocker 1.

## Nits

7. **runSome sounds level** (voice). The liveliness reading flags line 9, "That's the run. Some notes need work...",
   at semis-sd 2.88, just under the 3.0 line (range 9.9 against 12 to 21 for the rest). A calm read fits a "needs
   work" result, so this is optional: `localvoice.py stage-blocker --redo 9` if Cory hears it as bored. Line 11,
   "Notes met on this beat." (1.92), is a short line and above its 1.5 threshold.
8. **Pitch spread across takes, a lead to check by ear.** Lines 4 (hidden), 9 (runSome) and 14 (running) sit at a
   median of 139 to 153 Hz, against 92 to 121 Hz for the other twelve, about 6 semitones higher. It may only be
   delivery. Listen once that they sound like the same captain.
9. **Dragging an actor who is not in the script yet still gets praise.** Dragging Gran onstage in beat 1 (she
   enters in beat 5) speaks "Notes met on this beat.", because beat 1's notes are about Ava. The praise is true but
   off the point (v-first-drag-b1 log).
10. **A first tap on Next beat skips the premise.** That tap plays "placed", and welBlock is not heard until the next
    mode entry (audit walk row 6, "not heard"). This is the kit's rule for a tap with its own line, and it was
    accepted at the exit check.

## Checks

### 1. Frames (all looked at)
- **Default:** at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900 (f/default-*.png), and 375
  (audit/size-375x812).
- **Block:** with Sightlines and Focus on (f/block-rays-focus-1366.png).
- **House:** at 1366, 680 and 1920, at beat 3 and on Bus Stop beat 6.
- **Run:** mid-run at 9, 13, 16, 21 and 30 s; the end with notes to fix at 1366, 800, 680, 760 and 375; Bus Stop
  end; all notes met end (f/run-good-end-1366.png).
- **Free stage:** at 1366 and 375.
- **Extremes:** lights all off on The Trophy; Motion off mid-run (f/motion-off-1366.png).
- **Audit:** every mode at every size.
- **Results:** no text over a picture without a chip; the position tags, eye caption and "Seat B3" chips are white
  or orange on near-black (AA). No placeholder anywhere, no sideways scroll, no clipped hint.
- The audit's "text hidden under canvas.st-house" leads for #insetLab, #insetEye and #planWrap are false: the chips
  draw above the inset in every frame.
- The audit's 760x900 and 375 "below the fold" leads are the long lists and seat grid in the stack, by design, except
  the Run results (item 2).

### 2. Pictures (drawn in code)
- One consistent flat look across the plan, the inset, the House view and the mini map: rounded figures with
  initials, solid set blocks, the warm stage floor.
- Facts are right: stage areas from the actor's view (SR on the plan's left), the door flat opening, the platform
  level, the five body positions tagged per seat.
- No lettering problems; no people pictures or art tokens.
- Only miss: unlit actors are barely dimmed (item 6).

### 3. Voice with the real clips
- **Clip lengths:** 1.48 s to 5.80 s, with lead silence of about 0.17 s and tails of 0.03 to 0.19 s.
- **Lines tied to the screen:** Run awaits runStart (2.77 s) before cue 1, so nothing overlaps a caption. No clip
  ran past its moment or into the next line in any log, and no line was cut except by a newer action (stale run) or
  the double tap (item 3).
- **Every clip says its line:** the clips are keyed by their text and match lines.json and `L` exactly. I could not
  transcribe the takes; no Whisper is installed here.
- **Liveliness:** run with the official script against the main repo's voice/raw (the worktree has no raw/). It
  flags line 9 only (item 7).

Standard voice check (held clicks, Sound and Motion on):

| Line | Kind | Run | Expected | Spoken |
|---|---|---|---|---|
| placed | how | Next x6, 7 s apart | 1 | 1, then silent (heard) |
| upstaged | how | Next x6 (beat 3) | 1 | 1 |
| lastBeat | how | Next x6 | 1 | 1 |
| welHouse | welcome | House/Block x3 | 1 | 1 |
| welBlock | welcome | House/Block x3 | 1 | 1 |
| welRun | welcome | Run, then Run x5 | 1 | 1 |
| runStart | event | Free stage Run x5, 13 s apart | 5 | 5 |
| runFree | event | Free stage Run x5 | 5 | 5 |
| runSome | event | The Note, Bus Stop | 1 per run | 1 per run |
| runGood | event | The Note solved | 1 | 1 |
| beatMet | event | a drag that meets a beat | 1 | 1 |

- **Stale:** Next x3 at 0.2 s, then House, then Block. upstaged is dropped (newer) and placed is hushed. welHouse
  starts at once and is cut by Block. welBlock is dropped as stale, because the hint has moved on. Nothing plays
  after its moment.
- **First tap, one fresh page per kind:**
  - Read speaks only the hint.
  - Sound says nothing; Sound off and on brings welBlock once.
  - House gives welHouse only.
  - An empty plan spot or a tab gives welBlock at about 1.33 s.
  - Next gives placed only.
  - A first drag gives its own lines (beatMet, then placed).
- **Read:** Read during welHouse stops it and reads. Block straight after starts welBlock at once. Read with Sound
  off reads.
- **Stop:** Stop during "Places, please", then Block, gives welBlock.
- **Order:** spoken lines followed the actions in every run.

### 4. Full runs
- **As a solo student:** I read beat 1, dragged an actor, stepped through beats, ran the scene and read the notes,
  then applied the exit check's solution: all 11 notes met, "Every note is met. That's a show." played, and focus
  landed on Run again. Flat or confusing spots: the dark-Coach check (blocker 1), results out of view at
  small sizes (item 2), and the slow run (item 5).
- **As a teacher projecting at 1920x1080:** the figures and tags read well and the caption is large enough. The dead
  band under the floor wastes the screen (item 4).

### 5. Contract
- Bundle is 427 KB, under 2 MB, with all 15 clips in.
- No console errors or exceptions in any drive or audit shot; the only console entry was my own host page's
  favicon 404.
- The only URL in the bundle is the SVG namespace; no network requests.
- Motion off: nothing runs forever (audit "calm" clean); the run jumps between beats.
- Resized mid-action: clean.

## Re-check, round 1 fixes (2026-10-29)

This re-check reads tools/stage-blocker/final-fix.md as claims and covers the changes in kit/stage.js, src.html,
spec.md and docs/families/stage.md, on the rebuilt bundle (431,701 bytes, 15 clips). Frames are in
S:/CurioClass-codex-scratch/final/stage-blocker/rc/. 375 was checked through my scratch copy of the bundle served
on 8815.

- **1. Focus needs light: fixed.**
  - Default Trophy beat 1 fails "Coach has the focus" with "Coach is in the dark (USC is off). Light USC or use the
    spot." In both the plan and the House view the eye goes to Riley, not to the dark Coach (rc/trophy-house-1366.png,
    -680, -1920, -375, rc/trophy-block-focus-1366.png).
  - USC at half meets the note, and the eye goes to Coach with focus 9 (rc/trophy-house-usc-lit-1366.png).
  - All lights off: no eye on anyone (rc/trophy-house-dark-1366.png).
  - Defaults in all three scenes: no focus note is met, and the notes met by default are the plain ones (seen, lit,
    on the platform, the crate seen, Ben's preset Door entrance, Maya not upstaged while Leo is off).
  - Every beat can still be solved: I replayed the fix agent's solutions through `__tool.place/turn/light` in fresh
    pages and then did a real Run with held clicks. The Note ended 11/11, Bus Stop 12/12 and The Trophy 12/12, with
    runGood spoken each time.
  - The spec sentence, the engine (`focus` dark flag, `leader` skips dark and hidden actors, the `focus` check) and the
    family doc agree.
- **2. Run results in view: fixed.**
  - After a real run the summary sits at the top of the panel at 1366x768 (80 px), 680x425 and 800x500 (56 px), and
    calm 680x425 (56 px). In the 760x900 stack it is at 154 px. At 375 it is at the top of the iframe page.
  - The first failing notes are in view each time, and focus stays on Run again (rc/run-end-*.png).
  - Free stage, which has no notes, does not scroll, and its hint is runFree.
  - Nit: at 1366x768, where the results already fitted, the scroll now hides the hint and Run again. Focus is still
    on Run again, so Enter works. `block: 'nearest'` would keep them in view there.
- **3. Same-mode tap: fixed.** Block, House and Run each tapped twice 0.7 s apart speak their welcome once, with no
  hush. Tapping Run mode during a run leaves the run going. Stop, then Block, gives welBlock (rc/v logs).
- **Dark actors (polish 6): done.** In the dark a figure is drawn at 30% with a gray rim. The initials and face marks
  are light (#f2f2f5) on the dimmed colors, clearly AA in the frames. Half and full light are unchanged.
- **Small print:** Stage words ("A focus note also needs the actor in light.") and the House panel ("Nobody in the
  dark gets the eye.") wrap cleanly. There is no sideways scroll at 375 (scrollWidth 375) or at 680x425
  (rc/words-375.png, rc/words-680.png, rc/house-small-680.png, rc/house-small-375.png). Contrast is the panel's
  normal small text.
- **Standard voice check, re-run:** results are the same as in the first pass.
  - Next x6: placed 1, upstaged 1, lastBeat 1.
  - House/Block x3: one welcome each.
  - Free stage Run x5: runStart 5, runFree 5.
  - Stale run: upstaged is dropped (newer), placed is hushed, welHouse starts at once, welBlock is dropped as stale.
  - First taps:
    - Read: reads the hint only.
    - Sound off and on: brings welBlock once.
    - House: welHouse.
    - The plan or a tab: welBlock at about 1.34 s.
    - Next: placed only.
  - Read during welHouse stops it, and Block right after starts welBlock at once. Read with Sound off reads.
  - Order follows the actions every time.
- **No regressions** in the frames the fixes touch: House and Run at every size I used, Block focus bars, Free stage
  run end. No console errors; the only entry was the favicon 404 from my host page.
- Open items, none blocking: polish 4 and 5 and nits 7 to 10 from the first pass are still as they were (the polish
  items are known and not done), plus the scroll nit above.
- **audit_tool re-run** (audit2/, 80 leads, against 83 before): the only change is that the three "two quick taps" cuts
  are now clean. Every other lead is the same as in the first pass and was already judged there (false canvas-overlap
  leads, long lists in the stack). Motion off and resize are clean; there are no exceptions.
