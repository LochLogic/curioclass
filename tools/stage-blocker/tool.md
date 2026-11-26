# Stage Blocker: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 2 (general 1, family 1), should fix 16 (general 11, family 5), polish accepted 11

### stage-blocker: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames, lines and detail.
The Craft lens recomputed the sight, focus and body-position math independently (7,200 sightlines, 450 focus scores,
450 positions): no differences. No rule-5 content, so no sensitivity agent.

#### Blockers
1. **Delete beat freezes the tool** (C-1; general). Free stage: `sc().visited` is never trimmed, so `analyse()` throws
   on every render after a delete of a visited beat; nothing updates until a reload. Trim (or rebuild) `visited` on
   delete and guard `analyse()`.
2. **Focus and upstaging notes pass with the speaker's back to the house** (P-4; family:stage). A sweep of every
   position and 8 facings: 30 to 70% of drops meet a "has the focus" note with the actor full back; beat 7 passed with
   Ava full back and beat 3 "not upstaged" with Ava facing the back wall, both "Notes met on this beat". A check that
   passes the opposite of what it teaches is a misleading meter (REFINE Rounds). In the engine: a "has the focus" or
   "not upstaged" note also needs the actor open to the judging seat (profile or better, not three-quarter back or
   full back), and the failure's why text says so ("Ava has her back to the house"). Update the spec's note rule
   sentence and docs/families/stage.md in the same change.

#### Should fix
3. **Stage words are never taught on screen** (T-1; general). Stage right/left (and why SR is on the plan's left),
   up/downstage, the area codes, "upstaged", "cheat out", the five body positions. Add a short "Stage words" key in
   Block (one line each, a tiny figure for the body positions) and expand "cheat out" in the why text.
4. **Focus reasons are computed but never shown** (T-2; family:stage). `Stage.focus` returns reasons; show them for the
   selected actor and in the House list, and name the biggest gap in the focus why text.
5. **Position and status tags don't say whose they are** (T-3, P-3; family:stage). House view "full front" under Ava,
   who is full back; on the plan "hidden from A1" under Ben's token. Prefix with the name or initials (or a leader
   line), and say the seat on "upstaged (from B3)" (T-6 folded in).
6. **Enters and exits follow different rules** (T-4, P polish 5, T nit 9; family:stage). Enters use the wing or Door
   the actor waited in in the beat before, as exits do; nearest entrance only as the fallback. Dropping an actor into
   the house is not an exit by the wing on that side. One spec sentence changes (Interactions, "its nearest entrance").
7. **The Block welcome and hint lead a solo student wrong, and the hint sticks** (T-5, P-1, C polish 8; general). The
   welcome says "Drag the cast from the wings" on beat 1 of a scene where one actor is alone, and the hint stays on it
   through beats, fixes and set edits until an actor is dropped, so the last-beat Run hint never shows. The welcome
   points at the script ("Read this beat and its notes; when the script says someone enters, drag them in from their
   wing"), and the hint follows the state (`V.heard`, not "has placed an actor").
8. **The director's notes disappear while you block** (P-2; general). Every pick or drag switches the panel to Actor
   or Set, hiding the notes just as a note turns to a check. Keep the notes and beat icons in view (a pinned strip, or
   don't switch tabs on a drag).
9. **Free stage Run ends with "Every note is met. That's a show." when there are no notes** (P-5; general). Say a line
   that fits an empty note list.
10. **The panel jumps between beats** (P-6; general, BR1 lesson). Toggles and tabs move 20 to 40 px and the beat list
    18 px under the pointer. Reserve the line box's height.
11. **Clear wipes the scene with one tap, no ask** (P-7, C-7; general). Ask Yes / No, and set it apart from Save.
12. **Free stage names lose accents and spaces** (P-8; general). `nameIn` keeps letters of any script, spaces and
    hyphens ("José", "Maria Lopez").
13. **Focus falls to the page body** (C-2; general, BR1 lesson). After Run, after tapping a Run result note, and when
    Prev or Next reaches the first or last beat (the handler tests `disabled` before the render), and Delete beat.
    Keep focus on a sensible control each time.
14. **Arrow-key moves skip the pose update** (C-3, T nit 11; general). The keyboard path calls the same sit/stand rule
    as `placeActor`.
15. **The plan rebuilds under the pointer** (C-4; family:stage). A tap on an empty spot or seat gets no click and the
    first-tap welcome comes 1.5 s late. `setPointerCapture` on every pointerdown (engine).
16. **Engine and family doc disagree** (C-5; family:stage). `frame` (thrust, arc, open) is documented but the House
    view never reads it, and the House view assumes the audience at -y. Integrator call: don't build them now
    (director-s-chair's spec decides what it needs); document exactly what the engine draws today and list the rest
    under "Not yet" in docs/families/stage.md (C polish 11, path within a beat, goes in the same list).
17. **Targets under 44 px, and a small stage** (C-6, P polish 1; general). Seat dots on the House and Run map (21 px
    apart at 680x425; C3 and Balcony 8 px apart), chairs on the plan 10 to 18 px, actor tokens 11 px radius because
    the house rows take about 60% of the plan. Give the stage more of the plan and the seats real 44 px targets (or a
    seat list), as the welcome asks students to tap them.
18. **Overlapping labels and the stacked fold** (P polish 7, C polish 9 and 10; general, BR1 lessons). The Seat view and
    "Focus: a rough guide" chips cover "SL wing" and "Balcony (12 m back)" at 680x425, 800x500 and 375; at 760x900 and
    375 the toggles and tabs fall below the fold. Move the chips; in the stack put the main Block controls before the
    long lists.

#### Polish accepted
19. The eye gets a "rough guide" caption wherever it is drawn (Block inset, Run) (T-7).
20. The Note's preset: beat 2 is not "changed" on load; store it as the scene's layout or say "set by the script" (T-8, P-6).
21. House view figures bigger; use the view's space (P polish 2).
22. Run results list the failures first (P polish 3).
23. After a jump from Run to a failed note, the hint carries that note (P polish 4).
24. Multi-part why text doesn't repeat itself ("Sam is off stage. Sam is off stage.") (T nit 10).
25 to 29. The other polish items and nits in craft.md and play.md that touch only what the student sees, as the
    builder judges (list what you took in handoff.md).

#### Settled calls
- Exit counts the wing the actor was sent to, and the Seat view is framed at 3.4 m: both builder calls stand (T agrees).
- Blocker 2 is decided by the integrator under BASELINE (a check must not pass the opposite of the lesson); the focus
  weights themselves stay as the spec gives them.

#### Exit check, round 1

Cold check, 2026-10-28, on the CURIO_DRAFT=1 bundle (181,988 bytes, one file, the only URL is the SVG namespace, no
console errors or exceptions in any shot). drive.py on port 9950 with held clicks, real keys and a whole-pixel drag;
375 wide through `drive.py --host 9951` (host.html deleted after). Frames in my scratch folder `exit-sb/f1` to `f8`.

##### Items 1 to 29
1. Delete beat: fixed. Free stage, Add beat x2, Prev, Delete: "Beat 2 of 2", a later place moves the token, no
   exception; deleting down to one beat moves focus to Add beat.
2. Open to the house: fixed. Swept all 10 focus and not-upstaged notes in the three scenes (every 0.5 m position x 8
   facings, 2,128 drops each): met 31 to 63 percent, and **0** met drops with the actor three-quarter or full back
   from A3, B3 or C3 (focus) or B3 (not upstaged). Why text: "From B3, Ava's back is to the house (full back)." The
   Done-when 1 solution (beat 3 Ben to (-2.3, 3.2), Ava turned to 270, profile from B3; beat 4 Ben to (-3, 1.5); beat
   5 Gran to (3, 1.5); beat 7 Ben off, Ava to (-0.5, 1.5) facing out) meets all 11 notes; the default still fails "Ava
   is not upstaged" with the fix text. Spec sentence, engine and family doc agree.
3. Stage words: a "Stage words" key in Block (SR/SL and why SR is the plan's left, up/downstage, areas, upstaged,
   cheat out, five body-position figures); "cheat out" expanded in the why. Fixed.
4. Focus reasons: in the Actor status, the House list and the focus why ("Biggest gap", ties named). Fixed.
5. Tags: "Av sitting", "Av upstaged (from B3)", House "Be full front" / "Av full back". Fixed.
6. Enters: Leo from his SR slot to (1, 2) meets "Leo enters SR"; Ben from behind the Door meets "enters by the Door"; a
   drop into the house sends Ben back with a live message and no exit. Fixed (as the changed spec sentence says).
7. Welcome and hint in the scripted scenes: fixed (the hint follows the state; the last-beat hint shows). But see open
   item A.
8. Pinned notes: the beat's notes stay above the Actor, Set and Lights tabs (seen at 375 too). Fixed.
9. Free stage Run end: the runFree line and hint. Fixed.
10. Panel jumps: the toggles and tabs now hold still over every beat of all three scenes (362 / 414 px). **Still
    open:** the All beats list moves with the notes list above it: its top runs 566 to 786 px at 1366x768 (The Note
    588 to 786, Bus Stop 566 to 713, The Trophy 606 to 786), so tapping a beat in the list moves the list under the
    pointer by up to about 200 px (the lens measured 18). Open item B.
11. Clear asks "Clear Free stage?" with Yes / No, set apart from Save; No keeps it, Yes empties memory and
    localStorage; focus goes to No, then back to Clear. Fixed.
12. Names: **right.** "José" stays "José" (initials "Jo") and "Maria Lopez" stays "Maria Lopez" (initials "ML") in the
    cast buttons, speaker list, line box, plan token, Actor status, House list, the save and after a reload. Also kept:
    Zoë, Ñandú, Jean-Luc, 李小龙; "Ana  Bel" becomes "Ana Bel"; digits and markup are stripped; 12-character cap. Nit:
    "O'Neil" gets the initials "O'".
13. Focus: Run (Enter) puts focus on Stop, the end on Run again; a Run result (Enter) lands on its beat button with the
    note in the hint; Next x6 ends on Prev, Prev x6 ends on Next; Delete beat keeps it. Fixed.
14. Arrow keys: Ava off chair1 by ArrowLeft x3 stands (sitOn null); Ben onto chair2 by ArrowUp sits. Fixed.
15. First tap on an empty plan spot: the welcome at once (1343 ms for a tap at about 1200 ms; was 2.7 s). Fixed.
16. Family doc matches kit/stage.js on everything I checked (the focus and not-upstaged open rule, enters and exits,
    initials in tags, pointer capture and the synthetic click, frontFace, camera takes a seat object, `stopped`, a
    "Not yet" list with frame, backWall, entrance arrows and path within a beat). Fixed.
17. Targets: actors and small pieces get a 22 px hit radius (44 px); House and Run have a 5 x 3 seat button grid plus
    Balcony (44 px); the stage is larger on the plan (tokens 13 px radius at 1366x768). Plan seat dots in Block are
    still 17 to 36 px apart, but Seat (cycle) and the seat grids cover them. Fixed.
18. Overlaps and fold: "Focus: a rough guide" sits top left, clear of Balcony; no chip over "SL wing" at 680x425,
    800x500 or 375; at 760x900 the toggles and tabs are above the fold (793 and 845 of 900). Fixed.
19 to 29. Eye caption in the inset and Run; beat 2 "set by the script", no changed dot; House figures bigger; failures
    first in Run; the jump hint carries the note; no repeated why ("Leo is off stage. Sam is off stage."); "Run" then
    "Run again"; Stop returns to the start beat; the beat 1 direction; the Free stage legend; score labels clear of
    tokens. All seen.

##### Open
- **A. Free stage gets the scripted welcome** (should fix, general; a regression from item 7). On Free stage the hint
  is "Read the line and its notes. When the script says someone enters, drag them in from their wing." on load and
  until a first edit, and Read speaks it (frames free-default, free-default-680). Free stage has no notes and no stage
  directions; a solo student needs something like "Drag a cast member from a wing onto the stage." A Free stage
  welcome key (and its line in voice/lines.json) fixes it.
- **B. The All beats list jumps between beats** (should fix, general; BR1 lesson "nothing rebuilds under the
  pointer"). The rest of item 10. Reserve the notes list's height for the scene's longest beat, or put All beats
  above the notes.

##### Regressions looked for
Default screen, Block, House, Run, Focus and Sightlines on (seat A1), Free stage, at 680x425, 800x500, 1000x625,
1280x720, 1366x768, 1920x1080, 760x900 and 375 (host): no sideways scroll, no control under 44 px, hint unclipped,
plan, Prev and Next in view (Done when 9). Motion off: no running animations. Polish only, not blocking: at 1366x768
the seat view sits in a band above the plan; the mini map's "Tap a seat" label covers the Door.

##### Done when
1 pass (above). 2 pass: Ben at (-2.21, 1.5) hides Ava from A1 only, A5 clear, House from A1 tags her "hidden". 3 and 4:
bodyPos and focus scoring unchanged since the lenses' recompute; the open rule only adds a check. 5 pass: Ava moved in
beat 2 carries to beat 3, beat 4 (changed) keeps its own, beat 1 unchanged. 6 pass (Run, failures first, a tap opens
the beat). 7 pass. 8 pass (jittered drag, arrows, the plan is the 20th of 21 tab stops, after every panel control).
9 pass.

##### Standard voice check (held clicks, Sound and Motion on, browser voice)
| Line | Kind | Run | Expected | Spoken |
|---|---|---|---|---|
| welBlock | welcome | House/Block x3 | 1 | 1 |
| welHouse | welcome | House x3 | 1 | 1 |
| welRun | welcome | Run x2 | 1 | 1 |
| placed | how | Next x6 | 1 | 1 (then silent, heard) |
| upstaged | how | Next x6 (reaches beat 3) | 1 | 1 |
| lastBeat | how | Next x6 | 1 | 1 |
| beatMet | event, first time per beat | Turn left x5 on beat 3 | 1 | 1 |
| runStart | event | Run x5 (Free stage) | 5 | 5 |
| runFree | event | Run x5 (Free stage) | 5 | 5 |

Stale: Next x3 at 0.2 s, House, Block: upstaged dropped (newer), placed dropped (hush), welHouse at once, nothing
after its moment. First tap: Read speaks only the hint; Sound says nothing, and Sound off and on brings the welcome
once; House gives only welHouse; an arrow key on the plan gives the welcome at once; so does a tap on an empty plan
spot. Read during welHouse stops it and reads; a mode change right after lets welBlock start at once; Read with Sound
off reads. Order followed the actions in every run. Counts right.

##### Gate
1 Done when: pass. 2 standards: taught (Teaching lens; the stage words are now on screen). 3 solo defaults: **fail on
Free stage** (open A). 4 sensitivity: not needed. 5 no blocker or should-fix open: **fail** (A, B). 6 bundle clean:
pass. 7 voice counts: pass. Both open items are narrow; the integrator may fix them and send this check back.

#### Exit check, round 2

Scoped re-check, 2026-10-28, of open items A and B and the initials nit (handoff "Exit check round 1 fixes"), on a fresh
CURIO_DRAFT=1 bundle (177 KB). drive.py on port 9950, held clicks; 375 through `drive.py --host 9951` (host.html
deleted after). Frames in my scratch folder `exit-sb/r2`. No console errors (only the host page's favicon 404).

- **A. Free stage welcome: fixed.** On load at 1366x768 and 680x425 the hint is "Drag an actor from a wing onto the
  stage. Then pick the speaker and type their line under Beats." First tap on a tab or on an empty plan spot: welFree
  spoken once at once (1356 ms). Read speaks only that hint. After placing an actor the hint moves on to lastFree.
  welFree is in L, allLines() and voice/lines.json (15 lines, word for word); its clip is not recorded (expected).
- **B. All beats holds still: fixed.** Its top over every beat: 1366x768 The Note 785 (786 on beat 7), Bus Stop 713,
  The Trophy 785 (786 on beat 5); 680x425 755 / 682 / 755, no change at all; 375 host 1009 / 955 / 1027 (1028 on one
  beat). Also unchanged after edits that add and remove why texts in The Note. 1 px wobble only.
- **Initials: fixed.** O'Neil "On", Jean-Luc "Je", José "Jo", Maria Lopez "ML", Ñandú "Ña", R2D2 "R2", "-" "?";
  the Free stage name box and cast disc show "On" for O'Neil. Family doc says letters and digits only.
- **No regressions** in the frames they touch: Block at 680x425 beat 3 (toggles and tabs in view), The Note beat 7
  with three failing notes and All beats below, Free stage after Add beat, 375 Block. Voice: Next x6 in The Note
  gives placed 1, upstaged 1, lastBeat 1 (placed then silent), as in round 1.
- Polish, not blocking: `placedOnce` is page-wide, so a student who has worked in The Note and then opens Free stage
  gets lastFree ("Tap Add beat ... or tap Run") instead of welFree on an empty stage. welFree is dropped there, not
  marked heard.

Gate: every Done when, standards, solo defaults, bundle and voice counts hold, and no blocker or should-fix is open.
PASS.

<!-- end part -->

<!-- part: refine/craft.md -->

### stage-blocker: Craft lens (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, handoff.md, voice/lines.json, art/prompts.json, kit/stage.js and
docs/families/stage.md (line by line against the engine). Bundled with `CURIO_DRAFT=1` (156 KB, 162,826 bytes).
Audit first (`scripts/audit_tool.py`, ports 9980/9981), then `scripts/drive.py` on port 9982 with real held clicks,
jittered whole-pixel drags and real keys; 375 wide through my own iframe host served from the scratch folder (port
9983, the tool folder untouched). Frames and logs in the lens scratch folder (`audit/`, `s1/`, `v/`, `f/`, `r/`, `k/`,
`d/`, `sz/`, `t/`, `fo/`). Placeholder art and the browser voice not reported.

**Counts:** blockers 1 (general 1), should fix 6 (general 4, family 2), polish 4 (general 3, family 1), nits 4.

#### Blocker

1. **src.html `analyse()` (line 409) and `$('delBeat').onclick` (line 825), Free stage: Delete beat freezes the tool.**
   `sc().visited` keeps the index of every beat looked at and is never trimmed, so after Delete beat `beats()[i]` is
   undefined and `analyse()` throws on every render. `renderNow` stops at its first line: the beat counter stays
   "Beat 2 of 3" with 2 beats left, a dropped actor's token does not move, the hint and notes stop updating, until a
   reload. Seen: Free stage, Add beat twice, Prev beat, Delete beat; then `place('kai', 0, 3)`: the plan token stayed
   at the same pixel spot, and `Uncaught TypeError` in `analyse` on each render (shots `k-del`, `del-crash`). Any
   delete after visiting the last beat triggers it. Fix: drop and shift visited indexes (and `results`, `metOnce`,
   `touched`) on delete, or skip indexes past the end. **general**

#### Should fix

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

#### Polish

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

#### Nits

- docs/families/stage.md does not list `frontFace` (house), the `focus` note's own `seats` override, that
  `Stage.view.camera` takes a seat object (an id string fails), or the `stopped` getter on `Stage.play`. docs/KIT.md
  does not list `kit/stage.js` yet (handoff says so). **family:stage**
- `plan()`'s header comment lists `names` in its state; nothing reads it. **family:stage**
- Stop leaves Block on the beat the run stopped at (`finishRun` restores the start beat, `stopRun` doesn't).
  **general**
- `loadFree` sanitizes cast names but trusts the saved snapshots (their names go into `innerHTML` in the House
  list); a malformed save would throw on every render until Clear and a reload. Self-only. **general**

#### Checked and fine

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

#### Standard voice check

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

#### Audit pilot

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

<!-- end part -->

<!-- part: refine/play.md -->

### stage-blocker: Play lens (round 1, 2026-10-28)

Played cold as a grade 6-8 student alone at home and as a teacher projecting it, on the CURIO_DRAFT=1 bundle (156 KB).
Real held clicks (120 ms), whole-pixel jittered drags with jittered timing (8 to 50 ms steps), real keys including Q
and E (dispatched by hand), every STANDARDS size, 375 wide through `drive.py --host`. Placeholder art and the browser
voice not judged.

Counts: blockers 0, should fix 8 (general 5, family 3), polish 7, nit 4.

#### What works

- The 5-minute start in notes.md plays as written: beat 3 opens upstaged with the fix text, dragging Ben level or
  turning Ava out (Turn left x4, or Q) clears it and "Notes met on this beat." plays once.
- Drags with jitter land where dropped (Ben to -1.99, 2.99 for a target of -2.0, 3.0); the turn handle snaps to 45
  degrees; shelf drag-to-plan, tap-to-add, Rotate, Remove, light cycling and the Spot drag all work.
- Keyboard: Tab reaches every panel control before the plan (21 stops); on the plan `[` `]` pick, arrows move 0.25 m
  with a spoken position in the live region, Q/E turn 45 degrees with the new body position, Delete exits by the
  nearest entrance, an arrow brings an off-stage actor back on. Focus ring on the plan is clear.
- Run: "Places, please" waits, cue tags, captions, 1400 + 75 ms per character holds (The Note runs about 38 s),
  Motion off jumps without losing time, Read during a run speaks hint and caption, Stop works and focuses Run.
  Results list every note with the why; tapping one opens its beat in Block on the Beats tab.
- Free stage: rename, lines, Add beat, Save, reload restores, Clear empties localStorage; privacy line shown.
  Scene change asks, Leave and Stay work, each scene keeps its blocking.
- No console errors in any run (the only 404 was the host page's favicon).

#### Should fix

1. **The Block hint stays on the welcome until an actor is dropped.** general. Where: `hintKey()` (src.html:420),
   `firstPlaced()`. "Drag the cast from the wings onto the stage. Then tap a seat..." stays on beats 2, 4 and 7 while a
   student steps through (v-next run), after beat 3 is fixed by turning Ava (v-turn: hint back to the welcome), and
   after adding set pieces or lights (set, lights runs). The "last beat, tap Run" hint never shows unless something
   was dropped. Worse, on beat 1 of a scripted scene the right move is to leave Ben and Gran off: following the hint
   puts an actor on stage who must enter later. Better: a scripted-scene welcome that names the real first step ("Read
   the line, then tap Next beat. Fix any note with a cross.") and any edit (turn, pose, light, piece) counts as placed.
2. **The director's notes disappear while you block.** general. Where: `pick()` (src.html:633) switches to the Actor or
   Set tab on every plan pick or drag, and the notes and beat icons live only on the Beats tab. Seen in fix3-dragged,
   keys-turned, solve-b7a: the note the student is working on is hidden at the moment it turns to a check; the only
   feedback is the spoken praise and plan tags. At 680x425 the notes are below the fold in any tab. Better: keep the
   current beat's note icons and short text visible above the tabs (under the line), or stop auto-switching tabs.
3. **Body position and status tags don't say whose they are.** family:stage. Where: kit/stage.js `tag()` (plan, about
   line 672) and the house view tags. House view, beat 3 from B3: "full front" sits directly under Ava, who is full
   back; her "full back" tag is pushed below onto the apron face (walk-house-b3, z-house-tags; also from A1,
   the balcony and 680x425). On the plan, Ava's "sitting" and "hidden from A1" tags sit under Ben's token when he
   stands just downstage, so it reads as Ben hidden (ghost-plan, z-ghost-plan). Better: initials in each tag ("Av full
   back") or a short leader line, and plan tags that move clear of other tokens.
4. **Focus and upstaging notes pass with the speaker's back to the house.** family:stage. Sweep of all 7 "has the
   focus" notes over stage positions and 8 facings: 47 to 83 percent of drops meet the note, and with the actor facing
   full back from B3 still 30 to 70 percent (facing barely matters: speaking +3 and the cross +1.5 outweigh body
   position). Played: beat 7, dragging Ava downstage left her full back and "Ava has the focus" turned to a check with
   "Notes met on this beat." (solve-b7a, status line "full back from B3"). Beat 3: bringing Ben level clears "Ava is not
   upstaged" while Ava still faces the back wall, with praise (fix3-dragged). A student can meet these by dropping the
   actor anywhere and watching for the check, and learns the opposite of "open to the house". Better: "has the focus"
   also needs the actor not three-quarter or full back from the focus seats (or body position weighted more), and
   the beat-3 praise waits until the speaker is not full back. The weights are spec content: the integrator decides
   between an engine rule and a spec open question.
5. **Free stage Run ends with "Every note is met. That's a show."** general. Where: `hintKey()` (src.html:415) treats
   an empty result list as all met. The panel says "No director's notes in this scene." at the same time, and Read
   speaks the wrong hint (free-run-end). Better: a Free stage end hint ("That's your scene. Tap a beat in Block to
   change it, or Run again.").
6. **The panel jumps between beats.** general (BR1 wave lesson, reserve heights). Toggles and tabs move 20 to 40 px as
   the line box changes height (direction line, wrapping): measured 342, 321, 361, 321 px over four beat changes; the
   beat list shifts 18 px under the pointer when one of its own buttons is tapped (audit: 8 and 14 of 23 controls
   moved). A student reaching from Next beat to the Actor tab misses. Better: reserve the line box for a direction
   plus two lines.
7. **Clear wipes Free stage with one tap and no undo.** general. Where: `#clear` (src.html:855), same style and row as
   Save. The in-memory scene goes too (freeS2: cast and beats reset at once). Better: the same ask pattern as scene
   change ("Clear Free stage? Your actors and lines are removed from this device.").
8. **Free stage names lose accents and spaces.** general. Where: `nameIn` (src.html:832), `[^A-Za-z]`. "José" becomes
   "Jos", "Maria Lopez" becomes "MariaLopez" (free1). A student naming a character after a friend or family member will
   notice. Better: allow any letter (`\p{L}`), a space, hyphen and apostrophe, still 1 to 12 characters, initials from
   the first letters.

#### Polish

1. **The stage is small on the plan.** family:stage. The house rows take about 60 percent of the plan's height: at
   1366x768 the stage is about 365x255 px and actor tokens are 11 px radius (also 11 px at 680x425 and 375); at
   1920x1080 half the plan is empty house. In stack layouts this pushes the toggles and tabs below the fold (760x900:
   toggles at 902 px; 375: tabs at 820 px), so turning an actor means scrolling the plan away. Better: draw the house
   rows closer on the plan (rays drawn to the drawn seat dots) so the stage gets about twice the room.
2. **The House view wastes its space.** family:stage. Figures are about 70 px tall in a 1000x430 view at 1366x768 and
   about 40 px at 680x425, where the "Be" and "Av" initials overlap (c680-house). A projected class sees mostly black
   proscenium. Better: frame the camera on the actors and pieces present, not the 10 m opening.
3. **Run results bury the failures.** general. Met notes are listed first in beat order; at 1366x768 the first cross is
   at 570 px and most failures need a scroll (run-end). Better: failures first, or met notes collapsed to one line.
4. **After a jump from Run, the hint doesn't carry the note.** general. Tapping a failed note lands in Block with the
   generic hint; the why is only in the notes list (run-jump). Better: the hint names the note's fix once.
5. **"Enters by the Door" fails when Ben was dragged from behind the Door.** family:stage. Dropping him downstage left
   gives "Ben came on nearest the SR wing, not the Door." though he came out of the Door (ghost). Better why: "Ben
   first stands nearest the SR wing. Bring him on near the Door, then cross on the next beat."
6. **Beat 2 shows the "changed" dot on load.** general. The legend says "a beat you changed", but the preset made it
   (def frames). Better: no dot for preset beats until the student edits them.
7. **The Seat view chip covers the "SL wing" label** at 680x425, 800x500 and 375 (def-680x425, n375-default). Move the
   chip into the house area or shift the label.

#### Nit

1. "Run again" shows on the button during the very first run (`state.ran` is set at start; run-mid1).
2. The beat 1 line reads `"'Meet me...` with a double then single quote; a direction line ("Ava reads the note:")
   would read better aloud.
3. Free stage still shows the "met, not met, not checked" legend with no notes.
4. Muting before the first tap, then Sound back on, speaks nothing: the welcome is dropped as stale and the upstaged
   line was marked silent while off (v-sound). The hint still shows it.

#### Voice at a 2 s tap pace (held clicks)

| line | kind | expected | spoken |
|---|---|---|---|
| welBlock | welcome | once per scope | 1 (v-next, v-seat, v-turn) |
| upstaged | how | once, dropped when stale | dropped stale at 2 s pace, spoken on return (v-next); spoken once (v-turn) |
| beatMet | event | every met beat the student changed, stale dropped | spoken 4 of 5 in the solve run, 1 dropped as stale after a 1 s Next |
| placed / lastBeat / lastFree | how | once | once each |
| welHouse / welRun | welcome | once per mode entry scope | once each over 6 mode switches (v-mode) |
| runStart / runSome | event | each run | each run |
| Read | read | cuts the welcome, speaks the hint | yes (v-read); in Run speaks hint and caption |

No line named a hidden or disabled control; no line played after its moment.

#### Frames looked at

Scratch `lens-sb-play/frames`: def-1366x768, def-680x425, def-800x500, def-1000x625, def-1280x720, def-1920x1080,
def-760x1000, walk-b2, walk-b3, walk-house-b3, z-house-tags, fix3-dragged, fix3-b4, keys-turned, keys-after,
tab-planfocus, run-entry, run-mid1, run-mid2, run-end, run-jump, solve-b5, solve-b7a, solve-b7-toggles, set-sofa,
set-tree, set-tablemoved, lights-tab, lights-spot, handle, hide-a1, hide-house-a1, ghost-plan, z-ghost-plan,
ghost-house, n375-default, n375-dragged, n375-scrolled, n375-house, n375-run, c680-drag, c680-chip, c680-house,
c680-run, free-start, free-beats, free-saved, free-reload2, free-cleared, free-run-end, ask, bus-start, bus-b2,
trophy-b1, trophy-house, house-a1-b5, house-bal, calm-run-b4, calm-stopped, v-turn; audit size-*.png and calm-1366x768.

#### Audit pilot

Confirmed leads: the Seat view chip over "SL wing" (680x425, 800x500, 375); the panel jumping on beat taps (8 and 14 of
23 controls moved, should fix 6); toggles and tabs below the fold at 760x900 and 375 (real, folded into polish 1);
Motion off clean; first-tap lines and five-tap repeats clean, matching my own runs.

Wrong or noise: the clipped h1 at compact sizes (visually hidden on purpose), the clipped beat titles (a designed
ellipsis; the full line is in the line box), insetLab over planWrap (the inset sits on the plan by design), and the
beat list below the fold at preview sizes (not a main control).

Missed (everything past one click): the hint stuck on the welcome, notes hidden on the Actor tab, tags not tied to
their actor in House and plan, the Free stage end hint, Clear with no ask, name mangling, and focus and upstaging notes
met with the speaker full back by sweeping. The walk also could not reach the upstaged, hidden, beatMet and lastBeat
lines (they need an edit first), so I counted those by hand.

<!-- end part -->

<!-- part: refine/teaching.md -->

### stage-blocker: Teaching lens (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, voice/lines.json, art/prompts.json, kit/stage.js and docs/families/stage.md.
Bundled with CURIO_DRAFT=1 (156 KB). Driven with scripts/drive.py (port 9942, own profile); frames and results in
the lens scratch folder (`shots1/`, `audit/`). Motion off for logic checks, held real clicks for Run.

Counts: blockers 0, should fix 5 (general 2, family 3), polish 3, nit 3.

#### Standards on the module (TH:Cr1, TH:Pr5, TH:Cr3)

- **TH:Cr1** (Cr1.1.6-8 a staging challenges, b design challenges): taught. The director's notes are staging problems
  the student solves by placing, turning and lighting; the set shelf and lights grid are design choices; Free stage
  lets them generate their own scene.
- **TH:Pr5** (b technical elements; a acting techniques): b taught (area lights, Spot, set pieces change sightlines
  and focus). a is taught through body positions and cheating out, but only by trial; the words are never explained
  on screen (should fix 1). With that fixed it holds.
- **TH:Cr3** (rehearse, analyze, refine): taught. Run plays the scene, checks every note from all 16 seats, and a tap
  on a failed note opens its beat to revise.

No code needs to move.

#### Done when

| # | Check | Result |
|---|---|---|
| 1 | Default The Note fails "Ava is not upstaged" with fix text; can be fully met | PASS. Beat 3 why: "Ben stands 1.3 m upstage, so Ava shows full back from B3. Bring Ben down level with Ava, or have Ava cheat out." Solved all 11 notes (Ben to (-2.3, 3.2) and Ava turned 270 in beat 3; Ben to (-3, 1.5) in beat 4; Gran to (3, 1.5) in beat 5; Ben Off stage, Ava to (-0.5, 1.5) facing 0 in beat 7). Also solved Bus Stop and The Trophy to 0 open notes. |
| 2 | Ben between A1 and Ava hides her from A1 only | PASS. Ben at (-2.21, 1.5): A1 hidden (5 of 5 points, by Ben), A5 clear, all 14 other seats clear; "Ben covers Ava from seat A1."; House view from A1 tags Ava "hidden" (ghost). |
| 3 | Body positions in 45 degree steps | PASS. Recomputed by hand for three places and two seats (B3, A1), all 8 facings each, e.g. (0.07, 3.57) from A1: facing 0 is 42.7 degrees off, one-quarter; 315 is 2.3 degrees, full front. All 48 match. |
| 4 | Speaker full back or light off moves the eye | PASS. Ava level with Ben in beat 3: facing out 7.5 vs 5.5 (Ava leads); full back 4.5 vs 5.5 (Ben leads). Light off is -3 against half +1, a 4 point swing. Note: in a set-up where the speaker leads by more (Gran 10.5 vs 4.5), full back alone does not move the eye, which is the model working, not a fault. |
| 5 | Carry forward | PASS. Ava moved in beat 2 moves in beat 3; beat 4 (changed) keeps its own; 5 to 7 copy beat 4; beat 1 unchanged. |
| 6 | Run: captions, cue tags, note list, tap opens beat | PASS. Real Run 34 s: "Places", Cue 1 to Cue 7 with captions and stage directions, "4 of 11 notes met", tapping the 5th note opened Block, Beats tab, beat 3, with its note and why. |
| 7 | Free stage save, reload, Clear | PASS. Renamed Kai to Maxwell, saved; a fresh tab restored Maxwell at x 1; Clear set the key to null; a later tab starts as Kai. |
| 8 | Jittered drag, arrow keys, tab order | PASS. Whole-pixel jittered drag put Gran at (2.99, 1.5), "Gran enters SL" met; Down, Down, Left moved Ava 0.5 m and 0.25 m; panel controls come before #planWrap in tab order. |
| 9 | Plan, Prev, Next in view; 10 px text | PASS by the audit: none listed below the fold at 680x425, 1366x768 or 760x900; no text under 10 px. |

#### Facts (against the spec's Sources)

- Stage right is negative x, drawn on the screen's left with the house at the bottom: the actor's right facing the
  house. Seat 1 is house left, same side. Area grid USR..DSL, light grid ordered the same. Correct (Dean and Carra).
- Five body positions, names and order, 45 degree bands centred on 0/45/90/135/180. Correct.
- Upstaging: partner 1 m or more upstage, speaker three-quarter or full back from B3 and turned toward the partner.
  Matches the spec and the source idea.
- Focus weights match spec Content term by term. One addition: an actor who entered this beat gets the +1.5 "crossed"
  term ("entered"); it is in the family doc, not the spec. Fine as a rough-guide choice.
- Sizes in notes.md (10 m opening, 7 m deep, seats 3 m apart, balcony 12 m) match the code. The 5-minute start's
  claims check out: beat 3 from B3 has Ava full back, Ben full front, eye on Ben (5.5 vs 4.5).
- "Places, please", "House to half", "Cue 4: GO" are real calling phrases.

#### Builder's two calls

- **Exit counts the wing the actor was sent to: agree.** Exiting SR means going into the SR wing. Off stage from the
  door area fails with "Ben left by the Door, not the SR wing.", which teaches the right thing. The trouble is that
  enters now uses a different rule (should fix 4).
- **Seat view framed to 3.4 m: agree.** Recomputed with `Stage.view.camera`: a 3.0 m lamp post at y 0.3 and a tree at
  y 0.7 stay in frame from A1, A3, A5, B3, C3 and the balcony (tops at 86 to 213 px of 432). Only the top of the 5.5 m
  arch drops out of frame from B3, C3 and the balcony, and nothing there blocks a sightline, so no analysis changes.

#### Findings

##### Should fix

1. **No on-screen teaching of the stage words.** (general) Where: Block mode, plan labels, notes, why texts.
   What: the tool's topic is stage directions, but nothing on screen says that stage right is the actor's right
   facing the house (the left of the plan), that downstage is toward the house, what USR or DSC stand for, what
   "upstaged" means, what "cheat out" means (in the why text "have Ava cheat out"), or what the five body positions
   are. A solo grade 6 student can match the label "SR wing" without learning why it sits on the left. How seen: read
   every string in src.html and the frames; the only explanation is the teacher talk question in notes.md. Better: a
   short "Stage words" key in Block (one line each: stage right/left, up/downstage, the area codes, upstaged, cheat
   out, body positions with a tiny figure), and expand "cheat out" in the why text ("turn Ava partly out to the house
   while she still talks to Ben"). This is what makes TH:Pr5 a (acting technique) taught rather than stumbled on.
2. **Focus reasons are computed but never shown.** (family:stage) Where: Focus toggle bars, House "From this seat"
   list, Run. What: `Stage.focus` returns reasons ("+3 speaking; +2 light full; +2 full front; +1 downstage; +1.5
   entered; +1 space around them") but the student only sees a number (Gran 10.5). Emphasis by light, level, body
   position, movement and gaze is the content; with a bare number the student can only guess and check. How seen:
   `reasons` is not referenced in src.html; frames of House and Focus. Better: show the reasons for the selected
   actor (Actor status line) and in the House list, and in the focus why text name the biggest gap ("Ben gets +2
   full front; Gran is full back").
3. **House view position tags don't say whose they are.** (family:stage) Where: House view, The Note beat 3, seat B3
   (frame `shots1/start-b3-house.png`). What: Ben stands behind seated Ava; Ben's "full front" tag lands right under
   Ava's figure and Ava's "full back" is pushed below it, so the tag under Ava's back reads "full front". Body
   positions are a teaching target and this teaches the wrong one. Better: prefix the tag with the initials or a
   color chip ("Av full back"), or draw a leader line to the figure.
4. **Enters and exits follow different rules.** (family:stage) Where: `Stage.check` enters vs exits. What: exits use
   the wing the actor went to; enters use the entrance nearest where the actor lands, ignoring the wing they visibly
   came from. Leo dragged from his SR wing slot to (1, 2) fails "Leo enters SR" with "Leo came on nearest the SL wing,
   not the SR wing." How seen: drive check `entexit`. Better: enters uses the wing (or Door) the actor waited in in the
   beat before, the same rule as exits; the nearest entrance stays the fallback. This changes one sentence of the
   spec's Interactions ("its nearest entrance is X"), not what the tool teaches.
5. **The Block welcome tells a solo student to do the thing that breaks the scene.** (general) Where: welcome and
   first hint, "Drag the cast from the wings onto the stage." What: in Bus Stop, beat 1 is Maya alone; a student who
   follows the line and drags Leo or Sam on in beat 1 carries them into every beat, and "Leo enters SR" then fails
   with "already on stage before this beat". In The Note the preset on beat 2 hides this differently: an actor placed
   in beat 1 vanishes again in beat 2. How seen: carry rules in src.html plus the beat 1 frames. Better: the welcome
   points at the script: "Read this beat and its notes. Tap Next beat; when the script says someone enters, drag them
   in from their wing."

##### Polish

6. **"upstaged" on the plan doesn't name its seat.** (family:stage) The sightline tags say "hidden from A1"; the
   upstaged tag just says "upstaged", although it is judged from B3. With Ava turned to 135 and the seat set to A5,
   her status reads "profile from A5" next to "upstaged". Better: "upstaged (from B3)".
7. **The eye has no "rough guide" label in Block's seat inset or in Run.** (general) The House panel and the Focus
   toggle say it; the inset and the Run view show the eye with no note. Better: a small "eye: rough guide" caption
   wherever the eye is drawn.
8. **The Note's preset makes beat 2 "changed" before the student touches it.** (family:stage) Moving Ava in beat 1
   doesn't carry into beat 2 (she snaps back to the chair), and beat 2 shows the changed dot from the start. Better:
   store the preset as the scene's own layout for beat 2 and leave `changed` off, or say in the beat list "set by the
   script".

##### Nit

9. Dragging an actor off the front of the stage into the house counts as an exit by the wing on that side: Ben dropped
   at (-2, -3) meets "Ben exits SR". (family:stage)
10. Multi-part why text repeats itself: "Sam is off stage. Sam is off stage." (family:stage)
11. Arrow keys move a seated actor off the chair but keep the pose "sit" (Ava at (-1.2, 2.5), sitting on nothing, so
    her sightlines use a 1.2 m head). Dragging does switch to stand. (general)

#### Giveaways and cheap solves

No predict or hidden-information mode; the live checks and why texts are coaching by design. Tried the cheap routes:
turning a speaker fully out clears "not upstaged" (that is cheating out, a real fix); "Ben does not hide Ava" is met by
taking Ben off stage, but the same beat's "Ben enters by the Door" stops that; focus can be won by darkening everyone
else (a real lighting choice). Nothing passes without the staging idea.

#### Guardrails, sensitivity

Grade 6-8 theater, original scenes, no hard history, health or cultural content. Nothing for the sensitivity agent;
no rule 8 topics.

#### Audit pilot

Confirmed: the "Seat view" chip over the "SL wing" label at 680x425 and 375 (seen on the frame); at 760x900 the
toggles and tabs fall below the fold (a real lead for Play). Wrong or expected: #insetLab "overlapping" #planWrap is
the inset box sitting over the plan's own area by design; span.bt "clipped" is a deliberate ellipsis with the full
line in the bar and the aria-label; the beat list below the fold is a long list, allowed. Did not check the h1 lead.

Missed (all of the teaching): every finding above. Canvas tags are invisible to it (should fix 3), it cannot see that
focus reasons are hidden, that the enter and exit rules disagree, or that the welcome leads into broken entrances.
Its walk stops at one click, so all nine Done-when checks still needed the lens's own drives.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### stage-blocker: build handoff (2026-10-28)

#### What was built

- `src.html` (bundled as `stage-blocker.html`, CURIO_DRAFT=1), `tool.draft.json` (stage "built"), `notes.md`,
  `art/prompts.json` (no art: plan, seat view, figures and set drawn in code), `voice/lines.json` (firm-captain,
  Alnilam, 15 lines after the round 1 exit check; clips not generated yet, the browser voice stands in).
- New family engine `kit/stage.js` (global `Stage`) and family doc `docs/families/stage.md` (every option).
  director-s-chair reuses it. `docs/KIT.md` does not list stage.js yet (outside my write scope).

#### How src.html is laid out

Content (catalog, the proscenium house, scenes with notes), building a scene's beats (`buildScene`: start snapshot,
carry, then `preset` edits such as Ben dropped upstage of Ava in beat 2), state, voice (`L`, `hintKey()` picks the
hint; `setHint()` speaks a how-to the first time it comes up), views (plan, inset seat view, house view, mini plan),
panel renderers, editing (`editNow` = Stage.edit on the current beat + carry), beats/seats/tabs/modes, Run, Free
stage, wiring, keyboard on the plan, layout (`relayout`), start. `window.__tool` has hooks for tests (place, turn,
light, check, finishRun, plan(), house(), vlog...).

#### Decisions (settings, not facts)

- Facing is absolute: 0 faces straight out (-y). Body positions are measured to whichever seat is chosen.
- Default lights: downstage row full, center half, upstage off (so The Trophy's coach on the upstage platform has to
  be lit by the student for some beats).
- Wing slots: off-stage actors wait two to a row in their wing; an actor whose home is the Door waits behind it.
- `exits` counts the wing the actor was sent to (`actor.wing`), falling back to the nearest entrance; dragging Ben
  into the SR wing is an SR exit.
- Seat view inset: width clamp(26% of the stage area, 150, 440 px), beside the plan or above it when the plan keeps
  74% of its size, else a "Seat view" chip. "Focus: a rough guide" sits top left in Block, top right in House and Run.
- Seat camera frames the playing area up to 3.4 m (`fitPts`), not the whole 5.5 m opening, so figures read larger.
- Praise ("Notes met on this beat") only on a beat the student changed. The hint gives "upstaged" and "hidden"
  priority over the welcome, but only once the student has edited or changed beat (`state.placedOnce`).
- Area and piece labels give way to actor tokens on the plan; the SR/SL entrance arrows are quiet (the wings are
  labeled).

#### Tricky parts

- Run awaits the "Places, please" line (`wait: true`), then holds each beat max(2200, 1400 + 75 per character).
- Free stage autoloads a save on start; buildScene + saved cast and beats.
- A how-to line that starts playing just before a mode switch is cut by V.hush and counts as heard (the hint and Read
  still have it).

#### Refine round 1 (2026-10-28)

Every blocker, should-fix and accepted polish item in refine.md is done; details per item are in the builder's report.
Decisions made along the way (settings, not facts):

- Open to the house (blocker 2): "has the focus" fails first if the actor is three-quarter or full back to A3, B3 or
  C3; "not upstaged" also needs the actor open to B3. Engine, spec sentence and docs/families/stage.md changed together.
- Enters (item 6): the wing or Door the actor waited in during the previous beat (`P.wing`), the nearest entrance only
  when that is not known. A drop into the house (y < 0) is refused and the actor goes back where it was.
- Plan space (item 17): the house rows are compressed on the plan (rows at -1, -1.85, -2.7 m, balcony at -3.85 m;
  `planAt` rays keep the true seat positions for the maths, with a faint dotted link). The little map uses the far
  layout (HOUSE_MAP). House and Run get a 5 x 3 seat button grid plus Balcony instead of "Next seat".
- House view frames the scene (`state.fit` from `sceneFit()`: every on-stage actor and piece over all beats, at least
  5 m wide), so figures are bigger and the camera does not jump between beats.
- First tap (item 15): pointer capture on every pointerdown, plus a synthetic click from the plan when the tapped
  element was redrawn away before pointerup, so the kit's first-tap welcome hears the tap (about 1.2 s, was 2.7 s or
  dropped as stale).
- Stack layout (item 18): mode panels come before the scene row and the long lists; the plan height leaves the tabs row
  in view at 760x900.

Polish taken from 25 to 29:
- 25 "Run again" is the label only after a finished run (the first run says "Run").
- 26 Stop puts you back on the beat you started the run from.
- 27 Beat 1 of The Note gets a direction ("Ava reads the note aloud, then looks up.") and the quote marks inside the
  line are gone; spec changed to match.
- 28 The beat-list legend says what the marks mean, worded for Free stage when there are no notes.
- 29 Focus score labels move below the bar when another token covers their usual spot.

Left open: clips for the changed lines (welBlock, welHouse) and the new runFree are not recorded; docs/KIT.md still
has no stage.js row; muting before the first tap (kit nit 4) is the kit's; "enters" accepts an actor who waited in SL
wing but first appears at DSR (the check reads where they waited, not the path).

#### Exit check round 1 fixes (2026-10-28)

- A. Free stage has its own welcome, `welFree` ("Drag an actor from a wing onto the stage. Then pick the speaker and
  type their line under Beats."), chosen by `welKey()` in hintKey and the kit welcome; it is in L, so allLines() and
  voice/lines.json have it (clip not recorded yet).
- B. The notes list keeps one height across a scene's beats (`reserveNotes`): measured with every beat's notes and
  their real whys showing, per scene, beat count and panel width, re-measured after each edit (never mid-drag),
  grow-only. Beats with no notes say "No notes on this beat." in scenes that have notes. All beats now holds still
  (The Note and The Trophy 785 px, Bus Stop 713 px at 1366x768; 1009 px at 375; also after edits).
  Chose this over moving All beats above the notes, which would push the notes far down the panel.
- Nit: `Stage.initials` keeps letters and digits only ("O'Neil" gives On, "Jean-Luc" Je); family doc says so.

<!-- end part -->

## Finish check

<!-- part: final.md -->

PASS (re-check 2026-10-29: blocker 1 and should-fix items 2 and 3 fixed and verified, no regressions)

### stage-blocker: Final look

Cold Final look, 2026-10-29, on the bundle in the worktree (tools/stage-blocker/stage-blocker.html, 427,404 bytes,
built after src.html). All 15 recorded clips (local Qwen3-TTS, firm-captain) are embedded, keyed by their text. Each is
byte-identical to voice/<sha1>.mp3, and the 15 keys match voice/lines.json and `L` in src.html exactly.
drive.py ran on Chrome port 9242 and audit_tool.py on 9241. 375 wide ran through a copy of the bundle with a host page
in my scratch folder, served on 8815, so the tool folder was not touched. Frames are under
S:/CurioClass-codex-scratch/final/stage-blocker/: f/ = frames, v/ = voice runs, audit/ = audit frames and audit.md.
Every Chrome and server I started is closed. There are no art files: the plan, seat view, figures and set are drawn
in code and art/prompts.json has no assets, so check 2 covers the drawn pictures.

#### Blockers

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

#### Should fix

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

#### Polish

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

#### Nits

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

#### Checks

##### 1. Frames (all looked at)
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

##### 2. Pictures (drawn in code)
- One consistent flat look across the plan, the inset, the House view and the mini map: rounded figures with
  initials, solid set blocks, the warm stage floor.
- Facts are right: stage areas from the actor's view (SR on the plan's left), the door flat opening, the platform
  level, the five body positions tagged per seat.
- No lettering problems; no people pictures or art tokens.
- Only miss: unlit actors are barely dimmed (item 6).

##### 3. Voice with the real clips
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

##### 4. Full runs
- **As a solo student:** I read beat 1, dragged an actor, stepped through beats, ran the scene and read the notes,
  then applied the exit check's solution: all 11 notes met, "Every note is met. That's a show." played, and focus
  landed on Run again. Flat or confusing spots: the dark-Coach check (blocker 1), results out of view at
  small sizes (item 2), and the slow run (item 5).
- **As a teacher projecting at 1920x1080:** the figures and tags read well and the caption is large enough. The dead
  band under the floor wastes the screen (item 4).

##### 5. Contract
- Bundle is 427 KB, under 2 MB, with all 15 clips in.
- No console errors or exceptions in any drive or audit shot; the only console entry was my own host page's
  favicon 404.
- The only URL in the bundle is the SVG namespace; no network requests.
- Motion off: nothing runs forever (audit "calm" clean); the run jumps between beats.
- Resized mid-action: clean.

#### Re-check, round 1 fixes (2026-10-29)

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

<!-- end part -->

<!-- part: final-fix.md -->

### stage-blocker: Final look round 2 fixes (2026-10-29)

Frames and drive files: S:/CurioClass-codex-scratch/final/stage-blocker-fix/ (f/ = frames). Chrome 9281/9282, host 8819, all closed; host.html deleted. Bundle 431,701 bytes, 15 clips in, voice/lines.json equal to allLines() (15 lines, no line text changed, voice files untouched), no console errors (only the host page's favicon 404).

1. Focus needs light (blocker): kit/stage.js `focus()` now marks `dark` on an actor with no area light and no spot, `leader()` never picks a dark or hidden actor (so the eye in the plan and the House view agrees with the note), and a `focus` note fails first with "Coach is in the dark (USC is off). Light USC or use the spot."; docs/families/stage.md ("Lit for the eye" next to "Open to the house", the focus row, focus/leader signatures) and the spec's "Has the focus" sentence changed together; the House panel and Stage words small print say it too. Backward compatible (one new field, same API). Verified: Trophy beat 1 default fails with that why and the eye goes to Riley, not dark Coach (f/trophy-b1-block-focus-1366.png, f/trophy-b1-house-default-1366/680/1920.png, f/trophy-house-375.png); USC to half gives Coach the eye and the note (f/trophy-b1-house-uscLit-1366.png); all lights off shows no eye (f/trophy-lights-off-house-1366.png). A random search per beat, replayed through `__tool.place/turn/light` and checked with `__tool.check`, meets every note in The Note (11/11), Bus Stop (12/12) and The Trophy (12/12) (solve.json). Defaults: no focus note is met in any scene's default; the notes met by default are the honest ones (seen, lit, on the platform, the crate seen, Ben's preset Door entrance, Maya not upstaged while Leo is off).
2. Run results in view (should fix): finishRun scrolls the summary (`#runSum`) to the top of the panel or page with scrollIntoView, smooth with Motion on and instant with Motion off; focus stays on Run again (preventScroll). Verified real runs: summary at the top and the first notes in view at 680x425, 800x500, 1366x768, 760x900 (list bottom-aligned, starts at 180 px) and 375 through the host (f/run-end-*.png, run-end-680x425-calm.png).
3. Same-mode tap (should fix): setMode returns early when the mode does not change (`setMode(m, force)`; start-up calls it with force). Verified: a first tap on Block, and House or Run tapped twice 0.7 s apart, each speak their welcome once with no hush (mode-tap-*.png logs).
4. Dark actors (polish): in the House view a figure in the dark is drawn at 30% (was 50%), with a gray rim so its shape reads on the floor and light initials and face marks (9.1:1 to 11.5:1 on the six dimmed colors); half and full light are unchanged. Verified in the Trophy frames above.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)
- 2026-11-25: final.md folded in (last changed 2026-10-29)
- 2026-11-25: final-fix.md folded in (last changed 2026-10-29)
