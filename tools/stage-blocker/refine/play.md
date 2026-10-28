# stage-blocker: Play lens (round 1, 2026-10-28)

Played cold as a grade 6-8 student alone at home and as a teacher projecting it, on the CURIO_DRAFT=1 bundle (156 KB).
Real held clicks (120 ms), whole-pixel jittered drags with jittered timing (8 to 50 ms steps), real keys including Q
and E (dispatched by hand), every STANDARDS size, 375 wide through `drive.py --host`. Placeholder art and the browser
voice not judged.

Counts: blockers 0, should fix 8 (general 5, family 3), polish 7, nit 4.

## What works

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

## Should fix

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

## Polish

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

## Nit

1. "Run again" shows on the button during the very first run (`state.ran` is set at start; run-mid1).
2. The beat 1 line reads `"'Meet me...` with a double then single quote; a direction line ("Ava reads the note:")
   would read better aloud.
3. Free stage still shows the "met, not met, not checked" legend with no notes.
4. Muting before the first tap, then Sound back on, speaks nothing: the welcome is dropped as stale and the upstaged
   line was marked silent while off (v-sound). The hint still shows it.

## Voice at a 2 s tap pace (held clicks)

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

## Frames looked at

Scratch `lens-sb-play/frames`: def-1366x768, def-680x425, def-800x500, def-1000x625, def-1280x720, def-1920x1080,
def-760x1000, walk-b2, walk-b3, walk-house-b3, z-house-tags, fix3-dragged, fix3-b4, keys-turned, keys-after,
tab-planfocus, run-entry, run-mid1, run-mid2, run-end, run-jump, solve-b5, solve-b7a, solve-b7-toggles, set-sofa,
set-tree, set-tablemoved, lights-tab, lights-spot, handle, hide-a1, hide-house-a1, ghost-plan, z-ghost-plan,
ghost-house, n375-default, n375-dragged, n375-scrolled, n375-house, n375-run, c680-drag, c680-chip, c680-house,
c680-run, free-start, free-beats, free-saved, free-reload2, free-cleared, free-run-end, ask, bus-start, bus-b2,
trophy-b1, trophy-house, house-a1-b5, house-bal, calm-run-b4, calm-stopped, v-turn; audit size-*.png and calm-1366x768.

## Audit pilot

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
