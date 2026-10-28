# stage-blocker: Craft lens (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, handoff.md, voice/lines.json, art/prompts.json, kit/stage.js and
docs/families/stage.md (line by line against the engine). Bundled with `CURIO_DRAFT=1` (156 KB, 162,826 bytes).
Audit first (`scripts/audit_tool.py`, ports 9980/9981), then `scripts/drive.py` on port 9982 with real held clicks,
jittered whole-pixel drags and real keys; 375 wide through my own iframe host served from the scratch folder (port
9983, the tool folder untouched). Frames and logs in the lens scratch folder (`audit/`, `s1/`, `v/`, `f/`, `r/`, `k/`,
`d/`, `sz/`, `t/`, `fo/`). Placeholder art and the browser voice not reported.

**Counts:** blockers 1 (general 1), should fix 6 (general 4, family 2), polish 4 (general 3, family 1), nits 4.

## Blocker

1. **src.html `analyse()` (line 409) and `$('delBeat').onclick` (line 825), Free stage: Delete beat freezes the tool.**
   `sc().visited` keeps the index of every beat looked at and is never trimmed, so after Delete beat `beats()[i]` is
   undefined and `analyse()` throws on every render. `renderNow` stops at its first line: the beat counter stays
   "Beat 2 of 3" with 2 beats left, a dropped actor's token does not move, the hint and notes stop updating, until a
   reload. Seen: Free stage, Add beat twice, Prev beat, Delete beat; then `place('kai', 0, 3)`: the plan token stayed
   at the same pixel spot, and `Uncaught TypeError` in `analyse` on each render (shots `k-del`, `del-crash`). Any
   delete after visiting the last beat triggers it. Fix: drop and shift visited indexes (and `results`, `metOnce`,
   `touched`) on delete, or skip indexes past the end. **general**

## Should fix

2. **Focus lost when controls change (BR1 lesson).** Keyboard checks, `document.activeElement` after each:
   - Run (Enter on `#runBtn`): the button disables itself while running, focus falls to BODY and stays there after the
     run ends (shots `run-focus`, `run2`). Move focus to Stop on start and back to Run (or the summary) at the end.
   - A note in the Run results (Enter): `jumpTo` hides the Run panel, focus falls to BODY (`results-focus`). Focus the
     beat's notes or the current beat button with `preventScroll`.
   - Prev beat / Next beat to the first or last beat (Enter x6): focus falls to BODY (`k-next`, `k-prev`). The
     handlers test `$('next').disabled` right after `goBeat`, but `render()` is deferred to the next frame, so the
     button is not disabled yet and the hand-off to the other button never runs. Same pattern on Delete beat
     (line 828). Test the index, not the disabled flag.
   **general**
3. **src.html keyboard move (line 916): an actor walks off a chair still sitting, or onto a chair still standing.**
   The arrow-key path copies `x, y, on, sitOn` from `Stage.free` but never updates `pose` (the drag path,
   `placeActor`, does). Ava (sitting on chair1), three ArrowLeft: `{x: -1.7, pose: 'sit', sitOn: null}`, and the
   seat view draws her sitting on the bare floor; Ben moved by ArrowUp onto chair2: `{pose: 'stand', sitOn:
   'chair2'}`, a standing actor inside a chair whose chair no longer counts in his sightlines (`kbd-chair`,
   `kbd-onto-chair`). Route the keyboard move through `placeActor`. **general**
4. **kit/stage.js `plan()` pointer (lines 747-750) and `update()`: the plan rebuilds under the pointer.** A tap on an
   empty spot or a seat calls `onPick(null)` / `onSeat`, the tool re-renders on the next frame and `svg.innerHTML`
   replaces the element under the pointer, so no `click` is delivered. Curio.voice decides the first-tap welcome on
   that click and falls back after 1.5 s: the welcome came 1.5 s after the tap (pointerdown 1211 ms, welcome 2718 ms;
   seat tap 1212 / 2725), against about 0.1 s for a tap on an actor or a button (1208 / 1342) (shots
   `f-plan-empty`, `f-plan-seat`, `f-plan-actor`, `f-next`). Fix in the engine: `setPointerCapture` on every
   pointerdown (the click then lands on the svg), or keep the hit element. director-s-chair inherits it.
   **family:stage**
5. **kit/stage.js `houseView` and `plan` vs docs/families/stage.md: the doc promises shapes the engine does not
   draw, and director-s-chair needs them.** Line by line, every documented function, field and default exists and
   behaves as written, with these exceptions:
   - `frame: 'proscenium' | 'thrust' | 'arc' | 'open'`, documented as "how the surround and curtain line draw", is
     read in one place only: the plan's dashed curtain line for `'proscenium'` (line 597). The House view never reads
     it; thrust, arc and open draw exactly like a proscenium without its walls.
   - The House view assumes the audience sits at negative y: the stage's front face is drawn only along the outline
     box's `y0` edge (line 878, governed by an undocumented `frontFace`), prism faces are shaded "toward the house" as
     -y (line 923), and a back wall is always drawn (no way to leave it out). Plan entrance arrows always point
     sideways by the sign of x (line 615), so an upstage house entrance draws its arrow along the back wall.
   director-s-chair's spec has side seats (Noh waki-shomen at (-8, 2.7), Globe yard side at (-9, 3)), a raised stage
   seen from the side (Noh 0.9 m, Globe 1.5 m: no side face will draw), an open commedia trestle (no back wall wanted)
   and upstage house entrances (Greek door (0, 23), Globe doors (-4, 8) and (4, 8)). Either make `frame` and these
   cases real (front faces on every outline edge that faces the seat, a `backWall: false`, an entrance `dir`), or cut
   the doc's `frame` line and list the limits so director-s-chair's builder knows to add them. **family:stage**
6. **Seat targets on the House and Run seat map (and pieces on the plan) are under 44 px.** The welHouse line and hint
   send the student to them ("Tap another seat dot"). Measured from `mini().seats`: neighboring seats are 21 px apart
   at 680x425 and 39 px at 1366x768 (hit radius 14 px), and C3 and Balcony are 8 px apart at 680x425 and 15 px at
   1366x768, so Balcony is near impossible to tap there; on the Block plan C3 and Balcony are 22 px apart at
   680x425. A chair is 10 px square at 680x425 and 18 px at 1366 on the plan (8 px slack around it). Next seat and
   `[ ]` are the fallbacks, but the line names the dots. Give the seat map a minimum spacing (or a larger map in
   House), push the balcony's `planAt` farther from row C, and give small pieces a 22 px minimum hit radius.
   **general**
7. **src.html `$('clear').onclick` (line 855): Clear wipes the scene with no ask.** One tap beside "Save on this
   device" empties localStorage (as the spec says) and also throws away the blocking in memory, beats and names
   included, with no confirm and no undo (shot `clear`: Kai back off stage at once). A student can lose a class
   period's work to a mis-tap. Reuse the "Leave this scene?" ask pattern ("Clear Free stage? This removes it from this
   device and resets the stage."). **general**

## Polish

8. **Hint words vs state after a fix.** `hintKey()` falls back to the welcome until the student has placed an actor
   (`placedOnce`), and turning, posing or lights don't count. In The Note beat 3, turning Ava out of the upstaged
   position makes the hint go back to "Drag the cast from the wings onto the stage. Then tap a seat..." while the
   student is mid-fix and Ben and Ava are both on stage (`v2-turn`). Count any edit (`editNow`) as started, so the
   hint moves on to "Tap Next beat...". **general**
9. **Labels overlap on the plan at the preview sizes.** The "Focus: a rough guide" chip covers "Balcony (12 m back)"
   at 680x425 and 375 (`blk-680x425`, `blk-375host`); the "Seat view" chip covers "SL wing" at 680x425, 800x500 and
   375 (audit lead, confirmed on `size-800x500`); with Focus on, Ava's score "4.5" sits under Ben's token when he
   stands 1.3 m upstage of her (`blk-680x425`). Move the chips into the plan's padding and let a score give way to a
   token as area labels already do. **general** (the score label part lives in kit/stage.js)
10. **760x900 (stack): the Block tools are a scroll below the plan.** Plan, Prev and Next fit (Done when 9 passes),
   but the toggles start at 902 px and the Actor tab's Turn and pose buttons further down (audit; `size-760x900`):
   a student turning an actor scrolls between button and plan each time. About half the plan's height is the house
   (rows A to C and the balcony); in stack layout a shorter house band (or rows drawn closer) would bring the Actor
   tools up. **general**
11. **Engine has no path within a beat.** `Stage.play` tweens straight from one snapshot to the next; director-s-chair's
    commedia lazzo ("starts, stops, turns back and starts again three times") needs waypoints or sub-beats. Say in
    the doc which, before director-s-chair is built. **family:stage**

## Nits

- docs/families/stage.md does not list `frontFace` (house), the `focus` note's own `seats` override, that
  `Stage.view.camera` takes a seat object (an id string fails), or the `stopped` getter on `Stage.play`. docs/KIT.md
  does not list `kit/stage.js` yet (handoff says so). **family:stage**
- `plan()`'s header comment lists `names` in its state; nothing reads it. **family:stage**
- Stop leaves Block on the beat the run stopped at (`finishRun` restores the start beat, `stopRun` doesn't).
  **general**
- `loadFree` sanitizes cast names but trusts the saved snapshots (their names go into `innerHTML` in the House
  list); a malformed save would throw on every render until Clear and a reload. Self-only. **general**

## Checked and fine

- **Contract:** one file, 162,826 bytes; no URL but the SVG namespace; no fetch, no image loads; localStorage only
  `curio-stage-blocker` (and the kit's `curio-motion`); kit:curio and kit:stage inlined, nothing re-implemented. No
  console errors on any frame except the Delete beat crash.
- **Sight and focus math against the doc and spec:** 150 random snapshots of The Note (cast anywhere on stage, random
  facings and poses, a platform, a tree, random lights and spot), all 16 seats, recomputed in Python by an
  independent method (dense sampling along each ray against cylinders, rotated boxes, round parts and walls; face
  points as written). 7,200 actor sightline statuses: 7,197 agreed at 1,500 samples per ray and all 3 grazing cases
  agreed at 40,000. 450 focus scores from B3 (every weight in spec "Focus" and doc "Analysis"): 0 differences. 450
  body positions: 0 differences. Upstaged, check and its 15 note types read against the doc's table: as written.
- **Redraw cost during drags:** with Free stage's six actors on stage, a tree, a sofa and a platform, Sightlines and
  Focus on, 61 jittered whole-pixel pointermoves: median 1.0 ms, p90 1.3, max 2.0 ms per move (plan SVG rebuild,
  sight, focus and the inset canvas). `renderNow` with every Note beat visited: 1.0 to 1.3 ms. No concern, even on a
  slow school laptop.
- **Drag** with jittered pointer input lands (Kai dropped where released, then `Stage.free` spacing). Arrow keys
  move 0.25 m, Q and E turn 45 degrees left and right, `[ ]` cycle actors, pieces and the spot, Delete sends off
  stage. Turn handle and Face partner math checked against the facing convention.
- **Keyboard and focus visibility:** tab order is header, scene, Prev, Next, toggles, the Beats tab, beat list, then
  the plan (panel before seat dots: Done when 8). Visible 4 px focus outline on buttons, a ring on the plan; tabs
  use roving tabindex with arrow keys. Nothing takes focus on load (audit).
- **Saving:** Save writes, a reload restores Free stage (Kai at (1, 2), renamed Nadia), Clear removes the key (Done
  when 7); the privacy sentence is on screen.
- **Motion off:** nothing runs forever (audit); Run with Motion off jumps each cross but keeps every beat's time.
- **Sizes:** every STANDARDS size framed in Block, House and Run (`sz/`, audit `size-*`), 375 through an iframe host:
  no sideways scroll, hint unclipped, plan text 10 px or more (plan labels 11 px, tags and scores 10.5 px, House tags
  12 px). Beat-list ellipses are deliberate (full text in each aria-label).
- **Words:** no em dashes in src, engine, family doc, notes, lines or tool.draft.json; "Curio Class" only;
  classroom-safe; storage stated as this device only. Art: none (`assets: []`), nothing to check.
- **Lines:** the 13 strings of `allLines()` equal `voice/lines.json` word for word; the 10 spec lines are among
  them (lastBeat, lastFree and running are the builder's additions, in both).

## Standard voice check

Drive with held clicks (0.12 s), Sound on, Motion on, browser voice.

| Line | Kind | Run | Expected | Spoken |
|---|---|---|---|---|
| welBlock "Drag the cast..." | welcome | Next beat x6 (6 s gap); mode round trip | 1 | 1 (each run) |
| welHouse "This is what one seat sees..." | welcome | House, Block, House, Block | 1 | 1 |
| welRun "Tap Run to watch..." | welcome | Run, Block | 1 | 1 |
| upstaged "Someone is upstaged..." | how | Next beat x6 (reaches beat 3) | 1 | 1 |
| upstaged | how | Turn left x5 on beat 3 (in and out of upstaged) | 0 more | 0 |
| beatMet "Notes met on this beat." | event, once per beat by spec | the turn that met beat 3's note | 1 | 1 |
| runStart "Places, please..." | event | Run x2 | 2 | 2 |
| runSome "That's the run..." | event | Run x2 | 2 | 2 |

- **Stale:** Next beat x3 at 0.2 s, then House, then Block: the upstaged how was dropped by the mode change (`hush`,
  unmarked), welHouse played at once; nothing played after its moment.
- **First tap:** a key on the plan, Next beat, or a tap on an actor: welcome within 0.1 s. House: only welHouse.
  Read: only the hint. Sound: nothing; Sound off and on brings the skipped welcome once. A tap on an empty spot or a
  seat on the plan: welcome 1.5 s late (finding 4).
- **Read:** during welHouse it stops the line and reads the hint; with Sound off it reads. Read in Run with results
  speaks the hint and up to six failed notes.
- **Order:** spoken lines followed the actions in every run. The audit's five-clicks pass (ten controls) was clean.

## Audit pilot

**Confirmed leads:** "Seat view" chip over "SL wing" (680x425, 800x500, 375); the 760x900 toggles and tabs below
the fold (polish 10); 375 tabs below the fold (a phone, expected). The first-screen sizes, Motion off, focus on load
and the five-click voice pass matched what I found by hand.
**Wrong leads:** `#insetLab` overlapping `#planWrap` (the inset sits in the plan's reserved padding by design);
`span.bt` "clipped text" (deliberate ellipsis, full text in aria-label); h1 "clipped" in compact and narrow (visually
hidden on purpose); beat-list buttons "below the fold" at 680x425 to 1366x768 (inside the scrolling panel, as the
kit's needs rule allows).
**Missed (all past one click or not mechanical):** the Delete beat crash (blocker), focus lost on Run, results and
Prev/Next at the ends, the keyboard chair pose bug, the late first-tap welcome on the plan, tiny seat-map targets
(SVG circles are not counted as controls), "Focus: a rough guide" over the Balcony label (shown only with Focus on),
Clear without an ask, the engine and doc gaps, and the sight and focus math. Suggestion: the walk could press Enter on
each control and record `document.activeElement` (it would have caught the Run and Prev/Next focus losses), and count
SVG elements with pointer handlers as targets.
