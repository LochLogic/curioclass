PASS
Counts: blockers 2 (general 1, family 1), should fix 16 (general 11, family 5), polish accepted 11

# stage-blocker: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames, lines and detail.
The Craft lens recomputed the sight, focus and body-position math independently (7,200 sightlines, 450 focus scores,
450 positions): no differences. No rule-5 content, so no sensitivity agent.

## Blockers
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

## Should fix
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

## Polish accepted
19. The eye gets a "rough guide" caption wherever it is drawn (Block inset, Run) (T-7).
20. The Note's preset: beat 2 is not "changed" on load; store it as the scene's layout or say "set by the script" (T-8, P-6).
21. House view figures bigger; use the view's space (P polish 2).
22. Run results list the failures first (P polish 3).
23. After a jump from Run to a failed note, the hint carries that note (P polish 4).
24. Multi-part why text doesn't repeat itself ("Sam is off stage. Sam is off stage.") (T nit 10).
25 to 29. The other polish items and nits in craft.md and play.md that touch only what the student sees, as the
    builder judges (list what you took in handoff.md).

## Settled calls
- Exit counts the wing the actor was sent to, and the Seat view is framed at 3.4 m: both builder calls stand (T agrees).
- Blocker 2 is decided by the integrator under BASELINE (a check must not pass the opposite of the lesson); the focus
  weights themselves stay as the spec gives them.

## Exit check, round 1

Cold check, 2026-10-28, on the CURIO_DRAFT=1 bundle (181,988 bytes, one file, the only URL is the SVG namespace, no
console errors or exceptions in any shot). drive.py on port 9950 with held clicks, real keys and a whole-pixel drag;
375 wide through `drive.py --host 9951` (host.html deleted after). Frames in my scratch folder `exit-sb/f1` to `f8`.

### Items 1 to 29
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

### Open
- **A. Free stage gets the scripted welcome** (should fix, general; a regression from item 7). On Free stage the hint
  is "Read the line and its notes. When the script says someone enters, drag them in from their wing." on load and
  until a first edit, and Read speaks it (frames free-default, free-default-680). Free stage has no notes and no stage
  directions; a solo student needs something like "Drag a cast member from a wing onto the stage." A Free stage
  welcome key (and its line in voice/lines.json) fixes it.
- **B. The All beats list jumps between beats** (should fix, general; BR1 lesson "nothing rebuilds under the
  pointer"). The rest of item 10. Reserve the notes list's height for the scene's longest beat, or put All beats
  above the notes.

### Regressions looked for
Default screen, Block, House, Run, Focus and Sightlines on (seat A1), Free stage, at 680x425, 800x500, 1000x625,
1280x720, 1366x768, 1920x1080, 760x900 and 375 (host): no sideways scroll, no control under 44 px, hint unclipped,
plan, Prev and Next in view (Done when 9). Motion off: no running animations. Polish only, not blocking: at 1366x768
the seat view sits in a band above the plan; the mini map's "Tap a seat" label covers the Door.

### Done when
1 pass (above). 2 pass: Ben at (-2.21, 1.5) hides Ava from A1 only, A5 clear, House from A1 tags her "hidden". 3 and 4:
bodyPos and focus scoring unchanged since the lenses' recompute; the open rule only adds a check. 5 pass: Ava moved in
beat 2 carries to beat 3, beat 4 (changed) keeps its own, beat 1 unchanged. 6 pass (Run, failures first, a tap opens
the beat). 7 pass. 8 pass (jittered drag, arrows, the plan is the 20th of 21 tab stops, after every panel control).
9 pass.

### Standard voice check (held clicks, Sound and Motion on, browser voice)
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

### Gate
1 Done when: pass. 2 standards: taught (Teaching lens; the stage words are now on screen). 3 solo defaults: **fail on
Free stage** (open A). 4 sensitivity: not needed. 5 no blocker or should-fix open: **fail** (A, B). 6 bundle clean:
pass. 7 voice counts: pass. Both open items are narrow; the integrator may fix them and send this check back.

## Exit check, round 2

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
