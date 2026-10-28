# stage-blocker: Teaching lens (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, voice/lines.json, art/prompts.json, kit/stage.js and docs/families/stage.md.
Bundled with CURIO_DRAFT=1 (156 KB). Driven with scripts/drive.py (port 9942, own profile); frames and results in
the lens scratch folder (`shots1/`, `audit/`). Motion off for logic checks, held real clicks for Run.

Counts: blockers 0, should fix 5 (general 2, family 3), polish 3, nit 3.

## Standards on the module (TH:Cr1, TH:Pr5, TH:Cr3)

- **TH:Cr1** (Cr1.1.6-8 a staging challenges, b design challenges): taught. The director's notes are staging problems
  the student solves by placing, turning and lighting; the set shelf and lights grid are design choices; Free stage
  lets them generate their own scene.
- **TH:Pr5** (b technical elements; a acting techniques): b taught (area lights, Spot, set pieces change sightlines
  and focus). a is taught through body positions and cheating out, but only by trial; the words are never explained
  on screen (should fix 1). With that fixed it holds.
- **TH:Cr3** (rehearse, analyze, refine): taught. Run plays the scene, checks every note from all 16 seats, and a tap
  on a failed note opens its beat to revise.

No code needs to move.

## Done when

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

## Facts (against the spec's Sources)

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

## Builder's two calls

- **Exit counts the wing the actor was sent to: agree.** Exiting SR means going into the SR wing. Off stage from the
  door area fails with "Ben left by the Door, not the SR wing.", which teaches the right thing. The trouble is that
  enters now uses a different rule (should fix 4).
- **Seat view framed to 3.4 m: agree.** Recomputed with `Stage.view.camera`: a 3.0 m lamp post at y 0.3 and a tree at
  y 0.7 stay in frame from A1, A3, A5, B3, C3 and the balcony (tops at 86 to 213 px of 432). Only the top of the 5.5 m
  arch drops out of frame from B3, C3 and the balcony, and nothing there blocks a sightline, so no analysis changes.

## Findings

### Should fix

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

### Polish

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

### Nit

9. Dragging an actor off the front of the stage into the house counts as an exit by the wing on that side: Ben dropped
   at (-2, -3) meets "Ben exits SR". (family:stage)
10. Multi-part why text repeats itself: "Sam is off stage. Sam is off stage." (family:stage)
11. Arrow keys move a seated actor off the chair but keep the pose "sit" (Ava at (-1.2, 2.5), sitting on nothing, so
    her sightlines use a 1.2 m head). Dragging does switch to stand. (general)

## Giveaways and cheap solves

No predict or hidden-information mode; the live checks and why texts are coaching by design. Tried the cheap routes:
turning a speaker fully out clears "not upstaged" (that is cheating out, a real fix); "Ben does not hide Ava" is met by
taking Ben off stage, but the same beat's "Ben enters by the Door" stops that; focus can be won by darkening everyone
else (a real lighting choice). Nothing passes without the staging idea.

## Guardrails, sensitivity

Grade 6-8 theater, original scenes, no hard history, health or cultural content. Nothing for the sensitivity agent;
no rule 8 topics.

## Audit pilot

Confirmed: the "Seat view" chip over the "SL wing" label at 680x425 and 375 (seen on the frame); at 760x900 the
toggles and tabs fall below the fold (a real lead for Play). Wrong or expected: #insetLab "overlapping" #planWrap is
the inset box sitting over the plan's own area by design; span.bt "clipped" is a deliberate ellipsis with the full
line in the bar and the aria-label; the beat list below the fold is a long list, allowed. Did not check the h1 lead.

Missed (all of the teaching): every finding above. Canvas tags are invisible to it (should fix 3), it cannot see that
focus reasons are hidden, that the enter and exit rules disagree, or that the welcome leads into broken entrances.
Its walk stops at one click, so all nine Done-when checks still needed the lens's own drives.
