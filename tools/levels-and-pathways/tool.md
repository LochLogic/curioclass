# Levels and Pathways: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: levels-and-pathways

#### Built

November 1, 2026. Build only in S:/CurioClass-codex. No commit, branch change or polish round.
Completed the existing four-mode implementation using kit:curio and kit:dance, with one newly painted studio.
Added the painter manifest, renderer boundary, required notes sections, reached-state audit plan and current handoff.
Only tools/levels-and-pathways and _scratch/levels-and-pathways contain project changes from this build.
The offline HTML is generated from readable src.html; tool.draft.json remains stage built.

#### Numbers check

Recomputed before implementation in Scratch/prepare.py; results in numbers.json. No discrepancy with the spec's numbers.
Six moves times three levels = 18 shapes, with 36 A/B keyframes. Five eight-count levels = 40 counts.
At 96 beats per minute, eight counts last 5 seconds and the four-count lead-in lasts 2.5 seconds.
Sixteen-count trips last 9.6 seconds at 100 beats per minute or 8 seconds at 120.
Straight length = 80 floor units; ideal semicircle = 125.664; four-leg zigzag = 144.222.
Contrast ratios match: white/teal 5.10, teal/paper 4.79, ink/paper 14.43, muted/paper 6.04;
white/high 5.75, white/middle 5.13, white/low 5.02.
Checked 3,000 unequal-part allocations: each retains its exact computed 8-to-32-count budget and at least two counts per part.

#### Feel check

Played all modes, the full eight-round mystery, every pathway/way pair and mixed-level drawn dances using held inputs.
Best moment: the eighth mystery reveals a gallery of the class's eight different ribbons, including the closed circle, with a bow.
Flattest moments: the bare geometric room made waiting feel empty; the portrait layout interrupted play by hiding choices.
Changed them with a large painted studio, warm paper controls, quiet sunlight dust, and a portrait stage that reserves room for every choice.
Also stopped long-drag welcomes delaying the part names and moved drawn-part badges clear of the finished dancer and end badge.
The studio now matches the bar's level of finish. The temporary kit dancer is still the visual weak point, pending the owner's painter.

![Levels and Pathways beside Snowy Mail Route](S:/CurioClass-codex/_scratch/levels-and-pathways/feel-comparison.png)

#### Done when

1. PASS for the temporary kit figure: 18 distinct pose pairs; 36-keyframe contact sheet inspected; every Low interpolation sampled.
   Highest Low head = 0.572 body heights, below the 0.62 limit. Move and level calls precede the pose change and count-in.
2. PASS: a live level change first appears on the next count. Trace records all 40 routine counts in High, Middle, Low, Middle, High order.
3. PASS: all 12 pathway/way combinations completed with the selected settings, ribbons and end badges; fourth trip removes the oldest; Clean floor clears.
4. PASS: answers were disabled in all eight trips; a wrong answer replayed once; all exact rounds completed; fast final level answer retained eight full badges.
5. PASS for the requested basic shapes: real line, arc, zigzag, wave and tiny drags at 1366x768 and 680x425; keyboard Surprise path and mixed-level Dance it worked.
   The broader historical orientation suite was not rerun. Small-stage compound-wave recognition remains a shared-engine limitation.
6. PASS: new mode/action stops old play, clock, music and queued calls; interruption evidence in levels-results.json.
7. PASS in focused logs: once-per-load how lines, repeated move/level calls, Read priority and stale call cancellation. The final delayed-freeze test drops the cue as stale after Read; all 44 runtime lines match the voice manifest.
8. PASS: all STANDARDS sizes inspected, including 375x812 through host 8785, all modes, gallery, Motion off and grayscale.
   Fixed the 760x900 fold issue; all main choices are in view. Phone controls retain at least 60 pixels; mystery answers retain 72 pixels.
9. PASS for dance state and count timing; literal no-storage exception: the mandatory shared kit remembers curio-motion, as STANDARDS requires.
   No dance, drawing, progress or sound choice is stored. Motion and Sound do not change the count clock.

#### Wave lessons

- Hint and voice: PASS in focused tests, current-step hints and Read agree, including returning to an unanswered mystery with Sound off. The full mechanical voice aggregation remains incomplete.
- Focus and layout: permanent controls and part-button identities; deliberate focus uses preventScroll; no load focus. PASS: real Tab, Shift+Tab and Enter alone create, edit and dance a path, ending with focus on Dance it.
- Sizes: PASS, every listed viewport plus phone host; no short choice set hidden after the portrait fix.
- No giveaways: PASS, hidden trip has no ribbon or active level band; right pathway reveals neutral gold until the level answer.
- Honest numbers: PASS, the real beat clock drives counts and music; drawn parts share the exact bounded count total.
- Standards: PASS, movement cues, copied levels, observed mysteries, ribbon symbols and one drawn dance with per-part levels are implemented.
- Motion off: PASS, count poses and trails remain; dust and pulse loops stop. The audit calm frame was inspected; no full aggregate audit verdict is available.
- Short choice sets: PASS, all move, pathway, way and level options remain visible at the tested sizes.
- Resize mid-animation: PASS in the focused running-move resize from 1366x768 to 760x900 and back, with Sound and Motion off; the final full stress aggregation did not finish.
- First-tap welcome: PASS for calls and drawing, own action takes priority; no welcomeAfter; a drag hushes obsolete speech.
- Unknown stays unknown: PASS, mystery level remains undisclosed until chosen.
- One look, one meaning: PASS, blue prints, green band, amber stripes and matching level icons.
- Badge says what is true: PASS, actual part level and ribbon pathway; fast final answer preserves full gallery badges.
- Hint changes back: PASS in the focused Sound-off mode-resume test: the path question stays current and Read speaks it; Go remains correctly unavailable.
- No answer by copying words: PASS, the mystery hint lists all choices without revealing the observed one.

#### Audit leads

The one complete audit command was attempted on Chrome 9981 with host 8785 and a hard 2,400-second limit.
It reached that limit during later stress work. No audit.md was produced, so there is no lead list or clean verdict to claim.
All 73 generated PNGs were inspected, covering default sizes, three other modes, five reached states and Motion off.
Partial evidence and the timeout are in _scratch/levels-and-pathways/audit/ and audit-console.log.
After that stop, narrowed freeze expiry, an idle-only Levels welcome and current-step hint selection received focused checks.
The audit was not rerun, as instructed. Final mechanical voice/resize aggregation is left for the cold reviewer.

#### Frames looked at

Scratch is S:/CurioClass-codex/_scratch/levels-and-pathways.
- Bar frames: Snowy Mail Route and Beat Lab, bundled and opened from Scratch copies so their tool folders were untouched.
- initial-frames: three initial studio/layout frames.
- final-frames: all four modes at seven desktop/portrait sizes, gallery at every size, grayscale and Motion off.
- phone-frames: all four modes plus gallery at 375x812; targeted Draw/gallery replacements inspected after their fixes.
- drag-frames: all ten real-drag outcomes, individually inspected.
- play-frames: low stretch, routine finish, four ribbon trips, traveling slide, mystery rounds 1 and 6, full gallery, Draw parts and finish, calm resized run.
- pair-frames: all 12 completed pathway/way combinations, inspected in qa-pairs-a/b contact sheets.
- extra-frames and last-frames: pose sheet, way selection, mixed-level count-budget finish, compact gallery repair.
- audit: all 73 PNGs in nine eight-frame contact sheets plus the native calm frame, with selected native frames inspected separately.
- keyboard-frames/keyboard-only-dance.png; play-frames/silent-mystery-resume.png and freeze-expiry.png. Current result JSONs are in Scratch.

#### Art made

One generated image: an empty studio, made with the built-in image tool using the full saved house style and prompt.
No people were generated. No redraw was needed. Raw PNG and final 1600x900 WebP inspected at final size and in the tool.
Final art = 96,178 bytes, about 94 KiB. Final bundle = 743,230 bytes (about 726 KiB), under 2 MB..
art/prompts.json records drawn_by codex, people false for the studio, review, full prompt and OpenAI source credit.

#### Art still to paint

32 deferred dancer assets, all people true, with explicit art tokens, A/B move frames, gait phases, facings, readiness and bow.
Use makeStudioDancer and onMove to install the paintings while retaining kit timing, projection, poses and trails.
The owner's final decision is painted dancers; the kit figure is temporary for this build.

#### Engine changes wanted

kit/curio.js, init Motion handler: optional in-memory preference for tools requesting no persistence; no kit file changed.
kit/dance.js, readPath: broader small-stage orientation evidence is needed before changing recognition thresholds.
The existing shared-engine limitation is documented rather than hidden or improvised around.

#### Left open

- Painted dancers, explicitly assigned to the next painter by the owner.
- Three browser-voice fallback lines: revised Draw welcome, Clean floor and Clear. Existing recordings retained; no audio recorded in this run.
- Broader real-hand orientation/compound-path recognition suite, particularly squeezed waves on the smallest stages.
- The full audit timed out at 40 minutes without its final report. No full audit pass is claimed.
- The full size sweep and full audit were not repeated after the final voice predicates; only their affected cases and keyboard path were checked.
- host.html is absent. All Chrome/server ports used by this build are closed, verified across 9980 to 9987 and 8785.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: levels-and-pathways
#### Played
Cold as a K-2 child following cues and as a projecting teacher, before builder notes/source. Played all four modes,
wrong-answer replay, mixed-level drawn dance and all eight mysteries to the earned gallery. The floor ribbons are strong.
#### Findings fixed
- Blocker, general, people art: replaced the code figure with three painted guides in one articulated atlas and
  one dedicated gallery bow. Main, mirror and button figures are painted; the studio, pose library, clock and trails stay.
- Should fix, general, Mystery: immediate level answers cut or dropped right-path praise. Preserve it before the next reply.
- Should fix, general, Mystery return: the hint named disabled Go. Give a return cue, then name Go when available.
- Should fix, family:dance, Draw: lock level/way settings during Dance it so the planned badges and actual ribbon agree.
- Should fix, family:dance, Draw: hide the previous performer and shadow when editing or replacing a plan.
- Should fix, general, input: cancel unfinished pointer drawings on mode changes, Clear and Surprise path.
- Should fix, general, hint: a late Clean floor fade could overwrite the next mode's hint. Guard its run and mode.
- Should fix, general, phone: hints fell below the window. Remove the phone hint's unnecessary minimum height.
- Should fix, general, Draw: lines crossed badge targets and phone badges overlapped. Reserve full targets, avoid ink,
  separate leaders from button bounds and pack four phone badges together; use spare panel space for a taller Draw stage.
- Should fix, general, voice: rapid repeated Middle/Low calls lost events. Interrupt old setting speech with each new event,
  followed by one short next-control cue. A same-mode double tap now preserves its welcome and current work.
- Should fix, general, Read: starting a move cut Read. Preserve Read priority for ordinary actions; mode/reset can release it.
- Polish, general, quiet preparation: immediate warm mat response and four larger count-in dots use the existing beat clock.
- Polish, general, gallery: painted bow and accurate scene description keep the earned ending readable.
#### Findings left
- Polish, 375px four-part finish: the duplicate ribbon-end icon crowds Part 4's generous hit rectangle. The numbered cards
  remain distinct and the path is visible. This is the densest composition left after the bounded badge repair.
#### Flattest moment left
Returning to the star is a short necessary wait. The cue now explains it; the preparation that follows has a visible beat.
#### Graphics
Built-in image generation; full prompts in art/prompts.json and raw PNGs in art/raw. One three-guide atlas plus one bow
replaces 32 deferred pose requests. Both new assets have people true. The figure is swappable through PAINTED_CAST/paintDancer.
A fresh people-art reviewer passed the source cast, 36 articulated endpoints and bow; I inspected 48 gait phases,
the retained studio, mirror and icons in context. Natural skin/hair/body variety; no visible mobility aids in this small cast.
Seated-copy guidance remains. Final art 234.4 KiB; offline bundle 928.4 KiB on disk. Both bar tools compared side by side.
#### Audit
**Audit not finished:** the only review audit stopped at its 2400-second limit during stress checks. Partial audit.md has
30 leads and 77 frames. No second full audit. Its snapshots precede the final repairs.
- Seven phone hint/keep leads: fixed; affected defaults, freeze, ribbon and level question re-shot with hints in view.
- Five Draw line/overlap leads: fixed in the drawing plans. Rechecks sampled 24 seeded plans at each of 1280, 1366, 1920,
  680 and 375 widths without overlaps/crossings. Real four-part drags passed at 1366, 680 and 375; phone finish caveat above.
- Two repeated-event leads: Middle and Low now start 5/5 calls at a held 2-second pace; next-control cue starts once.
- Four quick mode-tap leads: one complete welcome, no cut, in each mode after the idempotent mode fix.
- Eleven missing-welcome leads after action-first taps: expected action speech priority under STANDARDS. Keep the action's
  own call; do not insert a late premise. Short, once-per-mode next-control cues address what to do next.
- One resize disabled-label lead: different random plans produced different accessible names. Seeded the fixture;
  actual 1366-to-760-to-1366 resize preserved the same parts and Enter-twice focus, with no exception.
The four-part audit fixture lacked a return expression during that run. Corrected it and verified real drags separately;
its original blank frames are not coverage. All audit frames and final affected frames were opened and inspected.
Every STANDARDS size, all modes, 375px iframe, Motion off, grayscale and keyboard-only Draw were checked before the audit.
Held voice checks: Stretch 5, atMiddle 5, copyMe 1, freeze 1; fast Mystery replies both survive. Read continues with Sound
on/off; with Sound on it finishes before the next full eight-count move. A mode change releases Read immediately.
Recomputed 18 move/level pairs, 36 endpoints, 40-count High/Middle/Low/Middle/High routine, 16-count trips and 8-32 drawn
counts; actual drags covered straight, curved, zigzag, tiny and four-part paths. Highest Low head is about 0.563 body heights.
Final bundle and inventory checks pass: 47 runtime strings match voice/lines.json, no external src/href dependencies,
required notes headings, no em dashes, people flags present. Final focused driver batches logged no browser errors.
#### Left open
Six lines use browser speech fallback; existing recordings stay, no audio recorded. Sound-off Read uses a conservative
speech-length estimate because kit exposes no completion event. A kit event would make that wait exact across voices.
Shared readPath retains its documented small-stage limit for very squeezed/shaky compound waves; no kit thresholds changed.
The kit stores its Motion preference; no dance, progress or drawing is stored. No classroom trial or second full audit.
No kit/spec/catalog edits or git commits. Work stayed within the two authorized directories; own Chrome/server closed.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1 merged 2026-11-04, polish not started)
Counts: blockers 0 (general 0, family 0), should fix 6 (general 4, family 2), polish accepted 11

### Refine: levels-and-pathways (round 2026-11-04, after the Codex rework)

The 2026-10-28 Refine is kept in refine-2026-10-28.md and refine-2026-10-28/ (it ran before Codex reworked the tool).
Lenses: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit: 13 leads, all wrong on the lenses' own
runs (an empty barrier line in the voice queue fooled it; see P10). Measure-first run: the lenses did not read
codex-report.md or codex-review.md.

#### Should fix

1. **Draw a path at 680x425 and 375 wide: the part badges stack and their leaders tangle** across the path and each
   other, so nobody can tell which badge changes which part. `drawParts()` leader routing. On small stages put each
   badge on or right beside its own part; a leader never crosses the ribbon or another leader. (Play 1, Craft 1) general
2. **The painted dancer breaks apart at Low**: kneeling Bend, Twist and Swing show thigh boxes, missing shins and
   skin patches at the knees; the low stand has forearms hanging as detached strips with green fringe at the
   fingertips; the head sinks in Low Swing; the low gallop is out of joint. Pieces overlap at the joints, fix the
   low-stand arms (hands on knees), re-despill the hands, limit the neck. (Play 2, Craft 2) family:dance
3. **DA:Pr4.1.2a is cited for pathways only**: the grade 2 expectation adds facings, symmetrical and asymmetrical
   shapes and circling versus turning, which no activity teaches. Move the code to choreography-board (or another
   dance sibling) in the spec, notes and header; do not add a thin activity to keep it. (Teaching 1) general
4. **The level guide looks like three big buttons and does nothing** when tapped. Make each band set the level, the
   same as the panel button (simplest for K-2), or restyle it so it no longer reads as a control. (Play 3) general
5. **The end of Mystery path names no next action**: after round 8 the hint and line should say "Tap Play again for
   new mysteries." (once spoken, then hint only). (Play 4) general
6. **The Mystery hint names the dimmed Go during the trip**: on Go, the hint becomes the watching step ("Watch the
   dancer. Draw the pathway in the air with your finger."). (Play 5) general

#### Polish accepted

7. "Middle level. Stay in the middle." gets a body cue, for example "Middle level. Stand up, not too high and not too
   low." (new line in lines.json and the spec voice table). (Teaching 2, Play 6) general
8. High reads only by the arms: a visible rise of the whole figure (heel lift), or a small hop in Shake High.
   (Teaching 3) family:dance
9. Name locomotor and nonlocomotor once: "These moves stay in one place." in the Levels welcome, "Now we travel!" in
   Pathways, and a notes line. (Teaching 4) general
10. Empty barrier lines in the voice queue (`newRun()`, `afterRead()`): use `V.hush()` / `V.dropQueued()` and a kit
    way to wait for Read, so the log holds only real lines. (Craft 3) general
11. Support at home rewritten to be about this tool and doable tonight (draw a pathway on paper and walk it; sky,
    table, grass freeze; curved around a chair, straight back). (Teaching 5) general
12. Notes: low is on the floor for moves in place and a deep crouch when traveling. (Teaching 6) general
13. Older ribbons keep readable end badges (stagger them or place each at its ribbon's middle). (Teaching 7)
    family:dance
14. Mystery round 7: after the right answer, once, "A circle is a curved pathway too!" (Teaching 8) general
15. The first move takes about 8 s from tap to motion: fold Copy me into the Levels welcome, or let the dancer take
    the move's first shape as the call ends. (Play 7) general
16. The gallery start star covers the fifth ribbon: hide it in the gallery or shift the row. (Play 8) family:dance
17. Part badges sit inside the `role="img"` stage, so screen readers miss them: move them to a group outside it.
    (Craft 4) general

#### Nits (optional)

- "Which level was the dancer?" could read "Was the dancer high, middle or low?" (Teaching 9)
- Small 30 px zigzags and loops clamped at the left edge read wrong in `Dance.readPath` (Teaching 10, family:dance)
- Close the spec's open question on sharing the dancer with PE: BASELINE w1-21 settles it (Teaching 11)
- A Low trip's end badge touches the crouched dancer (Play 9)
- 760x900 Draw a path leaves about 120 px unused under the panel (Play 10)
- Tab order in Levels at 1366x768 differs from the visual order (Craft 5)
- A part badge tap says "Get close to the floor" when nobody dances yet; "Part 1, low." fits better (Craft 6)
- 31 superseded `dancer-*` entries in art/prompts.json: remove or mark deferred (Craft 7)
- Spec voice table and its "Art: none" line are out of date (Craft 8)

#### Settled calls

- Rule 5 does not apply. Every Done when passes (Teaching). Voice counts right (Craft). Contract clean at 946 KB.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: levels-and-pathways (round 1)

Cold Craft lens on the CURIO_DRAFT=1 bundle (946 KB). Frames and logs are in
`<scratchpad>/refine/levels-and-pathways/craft/` (folders A, B, C, D, E; shots files shotsA to shotsD; resize_check.py).
The shared audit (audit-r1) was read, not re-run.

Counts: blockers 0, should fix 2, polish 2, nit 4.

#### Findings

##### Should fix

1. **Draw a path, small sizes: badge leader lines tangle across the path and each other.** (general)
   Where: Draw a path, `drawParts()` leader routing (src.html about 2383 to 2396), at 680x425 (the tool page preview)
   and 375 wide. What: with a four-part path, badges 1 to 4 are stacked up on the back wall and their thin black
   leaders run as long elbows and boxes that cross the drawn pathway and each other; it is not possible to see which
   badge belongs to which part, which is the whole point of the numbered badges. At 1366x768 the same path is clean
   (short leaders, one per side). How seen: audit frames `state-four-part-drawn-path-680x425.png` and
   `state-four-part-drawn-path-375x812.png`, zoomed in `craft/zoom-4part-375.png`; compared with the 1366x768 frame.
   Better: when a leader cannot be short and clear, put the badge on the part (or number the part itself on the line)
   rather than routing a long leader; a leader should never cross the ribbon line or another leader.

2. **Painted dancer rig: low-level shapes show cut-out seams.** (family:dance)
   Where: `paintDancer()` puppet pieces (src.html 804 onward) with the kit poses, Levels and Pathways at Low. What:
   at Low the articulated painted pieces read as separate flat strips: the low stand at the end of a Low trip has both
   forearms hanging as detached rectangles from the shoulders to below the knees, with green fringe left at the
   fingertips; kneeling Bend and Twist at Low show the thighs as two blunt boxes with cut ends and a forearm strip
   sticking up behind the shoulder. On a projector this looks broken, and Low is the level the class copies most
   carefully. Middle and High shapes read well. How seen: audit `state-ribbon-finished-1366x768.png` (zoom
   `craft/zoom-lowstand.png`), my `D/M3-low-skip-end-1366.png` (zoom `craft/zoom-m3.png`), `D/M4-updown-mid.png`
   (Up and down at Low, Bend), `D/M6-low-twist-1366.png`, and `D/M2-low-walk-mid-1920.png` (low gallop mid-stride,
   torso and leg pieces visibly out of joint). Better: fix the low-stand arm pose (hands on knees, elbows bent) and
   the kneel joints so pieces overlap at the joints, and re-despill the hand edges.

##### Polish

3. **The tool queues an empty "barrier" line in the voice queue.** (general)
   Where: `newRun()` (`V.say('', {now:true, valid:() => false})`, src.html 1517) and `afterRead()` (693, plus the
   `readUntil` polling for Read with Sound off). What: every new action logs an event line with no text as
   "dropped, stale". It works (no line was lost in my runs), but it bends the kit instead of using it, and it fooled
   the audit into reporting "Stretch: event line lost, spoken 0 of 5, dropped 5: stale" when Stretch was in fact
   spoken 6 of 6 at a 2 s pace (`A/A3-rep-stretch-2s.json`). Better: use `V.hush()` / `V.dropQueued()` and a kit
   way to wait for Read (or add one to the kit), so the log holds only real lines.

4. **Part badges sit inside an SVG with `role="img"`.** (general)
   Where: `#sv role="img"` (src.html 209) holds the `.part` badges with `role="button"`. What: children of an img
   role are presentational, so a screen reader does not expose the part buttons or their good labels ("Part 1,
   zigzag, low level. Change its level"). Keyboard use works (Tab reaches them, Enter cycles the level, focus ring
   shows: `D/K3-draw-keyboard.png`, `D/K4-draw-keyboard-enter.json`). Better: put the badges in a group outside the
   img role (or drop the role from the stage and label the scene another way).

##### Nit

5. **Tab order differs from the visual order in Levels at 1366x768.** (general) Up and down and Surprise show first
   (`.go-row{order:-1}` in `wide.short`), but Tab reaches High, Middle, Low first (`D/K2-tab9.json`: the 9th Tab is
   Middle). Harmless for a teacher, but the order could match.
6. **Tapping a part badge speaks "Low level. Get close to the floor." while no dancer is on stage.** (family:dance)
   `cyclePart()` uses the same level line as Levels (`A/A5-rep-part.json`, 5 of 5 spoken, correct as an event). In
   Draw a path nobody is dancing yet, so "Get close to the floor" asks the class to move before Dance it. A short
   "Part 1, low." style line would fit the moment better.
7. **Stale art entries.** `art/prompts.json` still has 31 `dancer-*` entries (people: true, deferred: false, no
   art) marked superseded by painted-dancers; no `art:` token uses them. Remove or mark them deferred so tools and
   checkers do not count them as pending people art.
8. **Spec Voice table is out of date.** spec.md lists wDraw as "Draw a pathway on the floor with your finger. Start
   at the star. Then tap Dance it." and has no rows for clean, clear, returnStar, chooseMove, pathReady; the code and
   lines.json agree with each other (see Lines below), so only the spec needs the update. The spec's "Art: none,
   people: false" also no longer matches the painted cast.

#### Checks that passed

**Contract.** One file, 946 KB (under the 2 MB goal). No network requests: no fetch, XHR, import(), links,
WebSocket or http URLs in the bundle (the `voice:*` clip token is left for the voice step, expected). Kit used:
`Curio.voice`, `kit/dance.js` (clock, music, trails, readPath, floor), kit Motion, Sound, Read. No console errors or
exceptions in any of my 33 driven shots or in the audit.

**Access.** Every control 60 px or more at every STANDARDS size (audit sizes and states clean; part badges have a
64 x 64 hit area). Visible focus on tiles, mode buttons and part badges (`D/K2-tab9.png`, `D/K3-draw-keyboard.png`).
Keyboard: Tab reaches modes, Motion, Sound, Read, then the panel; Draw a path is fully usable from the keyboard
(Surprise path, then Tab to a part badge, Enter cycles its level). Nothing takes focus on load (`D/K1-tab1.json`:
first Tab lands on Levels). Color is never alone: level buttons carry cloud, table and grass glyphs and words;
ribbons differ by pattern (dotted prints, solid, wide stripes) and end badges; Mystery right answers get a star.
Motion off: no endless animation (audit), the move keeps its count-in and timing (`D/M1-calm-mid-move.png`). Sound
off then on brings the skipped welcome once; Read works with Sound off.

**Resize lead checked.** The audit's "#d-surprise ... left disabled" lead is a random-path artifact: with a seeded
Surprise path, the enabled controls before and after a 1366x768 to 760x900 and back resize are identical, and no
exception fires (`resize_check.py`, `E/`).

**Lines.** All 47 strings in `L` equal `voice/lines.json` word for word and in order; `__tool.allLines()` returns 47.
Hints are set from the same strings (composite move hints "Stretch! Middle level. Stay in the middle." are the two
lines joined). No line names a disabled or hidden control in any run (askPath, askLevel, nextHow, wMystery and
danceIt carry `needs`).

**Art.** Every `art:` token in src.html (sunlit-studio, painted-dancers, painted-gallery-bow) has a prompts.json
entry; the two people images are `people: true`, drawn by Codex with a fresh review note (rule 11). No local-model
people.

**Words.** No em or en dashes in src.html, notes.md, lines.json, prompts.json or spec.md; "Curio Class" never
"Curio" alone; classroom-safe. Privacy: nothing is saved; notes say the shared Motion setting is kept on this device.

#### Standard voice check

Driven with `scripts/drive.py`, held clicks (0.12 s), Sound and Motion on, 1366x768, logs from `__tool.vlog`.

##### 1. Repeats (each action five times in a row, gap longer than its lines)

| line | kind | expected | spoken | run |
|---|---|---|---|---|
| atHigh (tap High) | event | 5 | 5 | A1, gap 4 s |
| chooseMove "Tap a move, and copy the dancer!" | how | 1 | 1 (4 silent) | A1 |
| stretch | event | 5 | 5 | A2, gap 15 s |
| atMiddle (move call) | event | 5 | 5 | A2 |
| copyMe | how | 1 | 1 (4 silent) | A2 |
| freeze | event | 5 | 5 | A2 |
| wLevels (after a move ends) | how | 1 | 1 (3 silent) | A2 |
| skip (way) | event | 5 | 5 | A6, gap 4 s |
| zigzag (pathway) | event | 5 | 5 | A6 |
| pathReady "Tap Go, and follow the dancer!" | how | 1 | 1 (9 silent) | A6 |
| straight, walk (Go call) | event | 5 each | 5 each | B1, gap 22 s |
| ribbon | event | 5 | 5 | B1 |
| wPaths after a trip | how | 0 more | 0 (silent or dropped) | B1 |
| rightPath | event | 5 | 5 | B3, five rounds |
| rightLevel | event | 5 | 5 | B3 |
| askPath, askLevel, nextHow | how | 1 each | 1 each (4 silent) | B3 |
| returnStar | how | 1 | 1 (3 silent) | B3 |
| wMystery after Next | how | 0 more | 0 (4 silent) | B3 |
| wrong | event | every accepted wrong | 3 of 3 accepted | B2 (taps 2 and 4 landed during the replay, when the answers are rightly disabled) |
| surprise (path) | event | 5 | 5 | A4, gap 7 s |
| part names (firstX, thenX) | event | every path | every path (13 of 13) | A4 |
| tapPart | how | 1 | 1 (4 silent) | A4 |
| danceIt | how | 1 | 1 (silent after) | A4, A5 |
| atLow/atHigh/atMiddle (part badge) | event | 5 | 5 | A5 |
| stretch at a 2 s pace | event | 6 | 6 | A3 (audit's "0 of 5" was the empty barrier line, finding 3) |

##### 2. Stale lines

Fast taps 0.35 s apart: Stretch, Twist, Low, Surprise, Pathways, Curved, Go, Clean floor (`C/S1`); and Draw a path,
Surprise path, Low, Dance it, Surprise path, Mystery path, Go, Levels (`C/S2`). Every line was either cut by the next
action or dropped as newer, hush or chain; no Levels line played after Pathways opened, no part names after Low, no
Mystery line after Levels. The last line in each run matched the screen (clean; wLevels).

##### 3. First-tap timing (fresh page each)

| first tap | heard | ok |
|---|---|---|
| the stage | wLevels within 0.14 s | yes |
| Stretch (own line) | Stretch! / Middle level, then copyMe; wLevels after the move ends (17 s) | yes |
| Pathways mode button | wPaths within 0.12 s | yes |
| Read | the hint only, no welcome after | yes |
| Sound | nothing; Sound back on 3 s later brings wLevels once | yes |
| a key (Tab) | wLevels | yes |
| High (own line), then Sound off and on | atHigh, chooseMove; wLevels once on Sound on | yes |
| mode entries Draw, Mystery, Levels | wDraw, wMystery, wLevels, once each | yes |

##### 4. Read

Read during "Twist!" cut it at once and spoke the hint; the move's next line waited for Read (`C/R1`). Read with
Sound off spoke (`C/R2`). Mode change right after Read started wMystery 0.13 s after the tap (`C/R3`). Read during a
trip did not stop the trip; ribbon followed at the trip's end (`C/R4`).

##### 5. Order

In every log the spoken lines follow the taps in order; no older action's line followed a newer one.

**Voice check verdict: counts right.**

#### Audit pilot

**Leads confirmed:** none of the 13.

**Leads that were wrong:**
- "Welcome not heard" after a first tap on High, Middle, Low, the six moves, Up and down and Surprise (11 leads):
  these controls speak their own line, which is what REFINE step 3 asks for; the premise is not lost, because the
  tool queues wLevels when the first move ends (`C/F2`, 17 s) and Sound off and on brings it (`C/F7`).
- "Stretch: event line lost, spoken 0 of 5, dropped 5: stale": Stretch was spoken every time (6 of 6 at 2 s,
  `A/A3`); the dropped entries are the tool's empty barrier line (finding 3).
- "#d-surprise left disabled after resize": the missing name was a part badge label from a different random path;
  a seeded rerun shows identical enabled controls and no exception.

**What it missed:**
- The leader-line tangle in Draw a path at 680x425 and 375 wide (finding 1): its check for lines drawn across labels
  passed, but leaders crossing the path and each other are not checked.
- The painted rig's seams at Low (finding 2): art and pose quality are outside what it can see.
- The SVG `role="img"` wrapping the part buttons (finding 4).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: levels-and-pathways (round 1)

Fresh, cold run on the CURIO_DRAFT=1 bundle (levels-and-pathways.html, 2026-11-04). Played twice: as a K-2 student alone
at home (taps only, listening to the narrator, reading nothing), and as a teacher projecting it at 1366x768 and 1920x1080.
Frames: the shared audit (audit-r1/) plus my own in the scratch folder
`scratchpad/refine/levels-and-pathways/play/frames/` (driven by play/run.py and run2.py with held clicks and real drags,
ports 9771/9772, own profiles). Every frame named below was looked at.

**Counts: blockers 0, should fix 5, polish 3, nit 2.**

#### What works

- The first screen says what to do (hint and welcome name "Tap a move"), every mode's welcome names its control, and
  the hint moves on to the next action after each waiting moment: after a freeze it returns to the Levels how line
  (ms-late), after a trip to the Pathways how line (ms-pathlate), after a drawn path to "Now tap Dance it"
  (dr-zz-settled), after a right answer to "Tap Next" (my-solved). Read reads the current hint.
- Don't-nag holds: how lines go silent on repeat (Copy me, askPath after a replay), event lines speak every time
  ("Stretch!" 5 of 5 at a 2 s pace, st5 log).
- Mystery path gives nothing away: no ribbon, no level-guide glow and no spoken pathway or way during the trip
  (my-trip, my-r2trip); the ribbon painted in after a right path answer stays a neutral cream until the level is
  answered (audit state-mystery-level-question). Answer buttons dim while the dancer travels and during a replay
  (my-wrong).
- Draw a path reads real drags well: a jittery three-corner scribble is one zigzag (dr-zz-settled), a half-circle
  drag is one curved part (dr-arc), a 5-unit stub gets tooShort and its hint (dr-tiny). Part badges cycle levels and
  the ribbon changes per part (db-badge1, db-badge2).
- Pathways: the dotted preview of the chosen pathway before Go is a good teaching touch; a fourth trip clears the
  oldest ribbon and older ones fade (pa-t4end). Calm mode keeps the count timing (calm-mid at 9 s is on count 6, as
  with Motion on).
- The Ribbon gallery is a real payoff: eight ribbons in cells with their badges and a bow (gal-end).

#### Findings

##### Should fix

1. **Draw a path, four parts at small sizes: badge leader lines tangle across the drawing.** Mode Draw a path, the
   four-part drawn path at 680x425 and 375 wide. The four badges stack in a 2x2 block over the back of the floor and
   their black elbow leader lines run across the path and across each other (badge 1, the front straight part, sits
   over the back part; badge 4's leader runs under badge 3 and down the right side). A teacher on the tool-page preview,
   or a student on a phone, cannot tell which badge belongs to which part, and tapping a badge is how a part's level
   changes. At 1366x768 the same path puts each badge next to its part (audit state-four-part-drawn-path-1366x768).
   Seen: audit state-four-part-drawn-path-680x425.png and -375x812.png, zoomed in play/frames/z-375parts.png and
   z-680parts.png. Better: on small stages put each badge on or right beside its own part (a smaller badge over the
   floor near the part's midpoint), with short straight leaders that never cross another part. **family:dance**
   (part-badge placement in Draw a path).
2. **The painted dancer breaks apart in kneeling Low poses.** Mode Levels, Low level, Bend, Twist and Swing (kneeling
   back on the heels). The leggings end at the knee with orange skin-colored patches showing at both knee joints, the
   shins vanish so the legs read as stumps, and the elbows show jagged cut edges; in Low Swing the head sinks into the
   shoulders. On a projector the dancer looks broken, not kneeling (POLISH, Art: never crop a character mid-body, hard
   edges read as broken). Seen: lv-bendtolow.png (zoom z-bendlow.png), lowm-twist.png and lowm-swing.png (strip
   z-low-strip.png). The same cut-arm look shows, milder, on the Mystery dancer's shoulders while walking
   (z-mytrip.png). Better: a kneeling leg piece (thigh with the folded shin and foot behind) or a joint overlap so no
   gap shows, and a neck limit in Low Swing. **family:dance** (painted cutout figure on the dance pose engine).
3. **The level guide looks like three big buttons but does nothing.** Stage left, every mode. High, Middle and Low are
   tall rounded cards with borders, an icon and a word, the active one filled and pointed at: they look just like the
   level buttons in the panel and are the biggest targets on screen. A K-2 child alone taps Low there and nothing
   happens (the tap only plays the welcome). Seen: guide run, a held tap at (60, 225) left the level on middle;
   frame guide-tapguide.png. Better: make each band set the level (same as the panel button), or restyle it so it no
   longer looks like a control (no card border, one scale strip). **general** (a display that looks like a control).
4. **The end of Mystery path does not say how to go on.** Mode Mystery path after round 8, the Ribbon gallery. The hint
   and line are "Eight mysteries solved! Look at all our ribbons." and Play again is the only control; nothing names
   it, so a non-reader alone is left at a still screen (STANDARDS, Say how to act). Seen: gal-end.png, gal-end680.png,
   gal-end760.png; hint text in the gal log. Better: after the bow, the hint (and a once-only how line) says "Tap Play
   again for new mysteries." **general**.
5. **The Mystery hint names a dimmed control during the trip.** Mode Mystery path, after Go, while the dancer travels
   (16 counts, more than 10 s). The hint still reads "The magic floor hides the pathway. Tap Go, watch the dancer, then
   draw the pathway in the air with one finger." while Go is dimmed; the same in round 2 (STANDARDS: the hint changes
   when the state changes; no line names a disabled control). Seen: my-trip.png, my-r2trip.png. Better: on Go the hint
   becomes the watching step, for example "Watch the dancer. Draw the pathway in the air with your finger."
   **general**.

##### Polish

6. **"Middle level. Stay in the middle." is unclear for K-2.** Levels, Pathways and Draw a path, the atMiddle line. To
   a five-year-old "stay in the middle" means the middle of the room, not a body height, and it is the line heard most
   (Middle is the default level). High and Low each name a body action ("Reach up to the sky", "Get close to the
   floor"). Better: a body cue such as "Middle level. Stand up, not too high and not too low." Seen: lv and ud logs
   (spoken on every Middle move and every Middle step of Up and down). **general** (needs a new clip).
7. **The first move takes about 8 s from tap to motion.** Levels, the first move on a fresh page: "Stretch!", the level
   line and "Copy me! Stay in your own bubble space." play in turn, then a 4-click count-in, and the dancer stands still
   in her idle pose the whole time (tap at 1.3 s, Copy me ends near 9 s; lv-countin.png and lv-mid.png show the same
   pose). Middle Stretch also starts from almost the idle pose, so the first move a class sees barely changes
   (z-ms-strip.png). For K-2 this first wait is where attention drops. Better: fold Copy me into the Levels welcome so
   the first move has two short calls, not three, or let the dancer take the move's first shape as the call ends.
   **general**.
8. **The gallery star covers a ribbon.** Mystery path, Ribbon gallery: the start star sits on the left end of the
   fifth ribbon (curved, high), hiding its first prints at 1366x768 and 680x425. Better: hide the star in the gallery or
   move the second row right. Seen: gal-end.png, gal-end680.png. **family:dance** (gallery layout).

##### Nit

9. **A ribbon's end badge touches the dancer.** Pathways, a Low trip that ends at the right: the pathway badge at the
   ribbon's end sits on the crouched dancer's arm (audit state-ribbon-finished-1366x768, pa-t4end.png).
   **family:dance**.
10. **760x900 leaves the stage short.** In Draw a path at 760x900 the stage is about 225 px tall with about 120 px of
    empty space under the panel (db-n760.png); drawing in that strip is cramped. Let the stage take the spare height.
    **general**.

#### Not findings (checked)

- Low Shake is a lying-on-the-back shake with legs and arms up (z-shake-strip.png): it reads as a real low shape, not a
  fall, and the reflection matches. The spec's Content table still says "crouching"; that is for the Teaching lens.
- The low slide (a wide squat, arms out) and the low walk end pose read as low, and the mirror matches (z-slide.png).
- Mirror reflections matched the dancer in every frame I checked.
- Pathways: after a trip the hint moves from the ribbon line to the Pathways how line once the line ends (about 3 s);
  frames taken sooner show the ribbon line, which is right for that moment.

#### Audit pilot

Leads confirmed:
- Welcome "not heard" after a first tap on a level or move button: true, but by design and not a finding. A first tap
  on High speaks the level, then the short how "Tap a move, and copy the dancer!" (first-high log); a first tap on
  Stretch brings the full welcome back right after the freeze (lv log, 17.5 s). The student is never left without the
  next action.
- Its clean rows for sizes and states (overlap, fold, targets) held in every frame I re-shot.

Leads that were wrong:
- "#d-surprise left disabled after a resize mid-action": not reproduced. Surprise path, then 1366 to 760x900 and back
  mid-narration: no control or part badge is aria-disabled afterwards, the same as the plain run (rs and plain logs).
  The source never disables d-surprise.
- "Stretch: event line lost, spoken 0 of 5": wrong. Five held taps 2 s apart spoke "Stretch!" five times (st5 log); the
  "dropped, stale" rows it counted are the tool's blank stopper entries (an empty V.say with valid false).

What it missed:
- The leader-line tangle in Draw a path at 680x425 and 375 (finding 1): its "lines drawn across labels" check passed
  because the lines cross the drawn path and each other, not a label.
- The painted-figure seams in kneeling poses (finding 2), the level guide that looks like buttons (finding 3), the
  gallery end with no next action (finding 4) and the hint naming a dimmed Go during a Mystery trip (finding 5): none
  are in its states or checks.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: levels-and-pathways (round 1)

Cold read of spec.md, src.html, notes.md, tool.draft.json, art/prompts.json and voice/lines.json, then the bundled
draft (CURIO_DRAFT=1) driven in muted headless Chrome (port 9761/9762, own profile) with real held clicks, real drags
and keys. Frames and logs: `scratchpad/refine/levels-and-pathways/teaching/` (f/, poses/, poses-sheet.png).

Counts: blockers 0, should fix 1, polish 7, nit 3.

#### Findings

##### Should fix

1. **DA:Pr4.1.2a is cited for pathways only** (spec "Who and how"; notes.md line 49; src.html header comment).
   general. The repo holds codes only (`data/standards/ncas-performance-standards.txt`), so I checked against the NCAS
   text as I know it: the grade 2 expectation is clear directionality and intent in locomotor and nonlocomotor moves
   that change body shapes, facings and pathways, plus symmetrical and asymmetrical shapes and circling versus turning.
   The tool gives grade 2 the same straight, curved and zigzag pathways it gives grade 1 (DA:Pr4.1.1a); facings,
   symmetry and circling versus turning are not done by any student activity. Under rule 2 and the K-2 span call
   (gf-04), either move the code to a dance sibling that can teach it well (choreography-board is the likely home) or
   have the integrator confirm the official wording first and record why pathways alone carry it. Don't add a thin
   activity just to keep the code. How seen: read the code list against every mode played below.

##### Polish

2. **"Middle level. Stay in the middle." gives no body cue** (src.html line 266, `atMiddle`; voice/lines.json).
   general. High says "Reach up to the sky!" and Low says "Get close to the floor.", but "the middle" of what? A
   kindergartner copying the dancer gets nothing to do. Better: "Middle level. Feet on the floor, between the sky and
   the ground." (a new clip; the spec voice table changes with it). How seen: line list and run logs.
3. **High reads only by the arms** (family:dance; poses-sheet.png, mid-after-high.png). Every High keyframe is
   "on tiptoes", but from the front the painted shoes look flat and the head rises only about 16 px on a 320 px figure
   (head y 194 at High against 210 at Middle, 1366x768). Twist, Bend and Shake High differ from Middle mostly by arms
   up, so the class can learn "high = arms up" rather than "the whole body rises". Better: a visible heel lift (a
   small rise of the whole figure, or a three-quarter turn of the feet), or a tiny hop in Shake High.
4. **Locomotor and nonlocomotor are never named to the class** (header subtitle; notes "Talk about it"). general.
   The topic line promises the distinction, and the modes split it cleanly (Levels stays in place, Pathways travels),
   but nothing spoken or shown says "these moves stay in your bubble space, these moves travel". Better: one how line
   in each welcome ("These moves stay in one place." / "Now we travel!") and a matching notes line.
5. **Support at home is thin and not about this tool** (notes.md lines 16 to 18). general. "Make a high shape and a low
   shape together using comfortable arm movements" is vague, and no idea uses pathways on the floor or a drawn map,
   the heart of Pathways and Draw a path. Better, all doable tonight: "Draw a pathway on paper (straight, then
   zigzag), then walk it across the room." / "Call sky, table or grass and freeze in a shape at that level." / "Walk a
   curved pathway around a chair, then a straight one back."
6. **Notes say low is on the floor; the traveling dancer crouches** (notes.md line 47). general. In Levels every Low
   keyframe sits, kneels or lies, but in Pathways and Mystery the Low walk, gallop and slide are a deep crouch
   (paths-trip4.png, mys4-travel, mys6-travel). A teacher reading the note then watching a crouched trip sees a
   mismatch. Better: "Low level is close to the floor: on the floor for moves in place, a deep crouch when traveling."
7. **Older ribbons lose their end badges** (family:dance; paths-trip3.png). All three pathways end at x 90, z 50, so
   the newest badge covers the older two: three ribbons on the floor, one badge. The pattern still carries the level,
   but the class can't read an older ribbon's icon pair when the teacher asks "which one was the zigzag?". Better:
   stagger older badges (or put each at its ribbon's start or middle).
8. **Round 7's circle is answered "Curved" with no word on why** (Mystery round 7; mys7 frames and the gallery).
   general. A full circle back to the star is a good stretch, but the answer button shows an arch and the class may
   hesitate. A one-time line after the right answer ("A circle is a curved pathway too!") turns it into a teaching
   moment.

##### Nit

9. **"Which level was the dancer?"** (src.html line 280, `askLevel`). general. Reads oddly aloud; "Which level did the
   dancer dance at?" or "Was the dancer high, middle or low?" Needs a new clip.
10. **Small zigzags and clipped loops read wrong** (family:dance, `Dance.readPath`). A screen zigzag of 30 px corners
    (about a child's quick scribble at 1366x768) read as one curved part (draw-scr-small-zig.png); 40 px read zigzag.
    A loop drawn around the star runs off the left edge, is clamped to a straight edge and reads curved, straight,
    curved (draw-big-circle.png); the same loop drawn to the right of the star reads one curved part. A shallow
    diagonal zigzag (74 degree turns on the floor, flatter on screen) read as four straight parts (draw-diag-zig.png),
    which is defensible from how it looks. Edge cases only.
11. **The spec's open question is already settled** (spec.md "Open questions"). general. BASELINE "Specific calls"
    says levels-and-pathways must not share one dancer figure with PE (w1-21); the question asking whether to share it
    should be closed in the spec.

#### Teaching checklist

**1. Standards taught by something the student does.**

| Code | Taught by | Verdict |
|---|---|---|
| DA:Cr1.1.Ka (respond in movement to a cue) | copying the narrator, the count-in and the music in every mode | taught |
| DA:Cr1.1.Kb (change one element) | Levels: same move at three levels; Pathways: path, way and level | taught |
| DA:Cr1.1.2b (combine, changing elements) | Draw a path: levels per part, Dance it (trace changed level at count 5) | taught |
| DA:Pr4.1.Ka (levels) | Levels, Up and down | taught |
| DA:Pr4.1.1a (straight, curved, zigzag pathways) | Pathways, Mystery, Draw a path | taught |
| DA:Pr4.1.2a | pathways only | finding 1 |
| DA:Re7.1.Kb (demonstrate or describe observed movement) | Mystery: draw it in the air, name it, then the level | taught |
| DA:Cr3.1.Kb and 2b (symbol or map for a pathway) | Draw a path: the class draws the map; ribbons and badges as symbols | taught |
| DA:Pr5.1.Kb (start and stop on cue, own space) | count-in, "And freeze!", bubble space line | taught |
| SHAPE.S2 (movement concepts) | levels and pathways throughout | taught |

**2. Done when.**

| # | Check | Result |
|---|---|---|
| 1 | 36 keyframes shot (6 moves, 3 levels, A and B; poses-sheet.png): every one its own shape, Low all on the floor; guide band = `shownLevel` = chosen level on every count; the call ("Stretch!", "Low level...") logs at 3.0 to 4.3 s and the pose tween waits for it | pass (finding 3 on how High reads) |
| 2 | High tapped at count 3 of Twist: trace middle, middle, middle, high x5; Up and down: 40 counts, 8 each High, Middle, Low, Middle, High, each level line on its count | pass |
| 3 | Four trips (zigzag skip high, curved gallop low, straight slide middle, zigzag walk low): ribbon shape per path, level color and pattern, icon at the end; after trip 4 the first ribbon is gone, two older at half | pass (finding 7) |
| 4 | All 8 rounds played: rounds match Content; answer buttons dimmed and disabled in every travel sample (572 samples); wrong path replays once without ribbon; right path paints in; wrong level replays; gallery after round 8 with the bow | pass |
| 5 | Real drags: straight line one straight; half-circle arc curved; three-corner zigzag zigzag; tiny line tooShort; S wave one curved; straight then zigzag two parts; off-star start gets a lead straight part. Keyboard only: focus Surprise path, Enter, then Dance it, Enter | pass (finding 10) |
| 6 | Twist tapped at count 3 of Stretch: old counts stop at 3, only the new run counts; mode switch mid-Bend: no new counts, no music, no lines in 6 s | pass |
| 7 | Three moves in a row: copyMe spoken 1, silent 2; wLevels spoken once; move, level and freeze lines spoken every time | pass |
| 8 | Not re-shot: the audit's size rows are clean at all eight sizes (60 px targets, fold, 375 host) | pass on the audit |
| 9 | Curved walk trip measured 12000 ms with Motion on, 11999 ms Motion off, 11999 ms Sound off (4 + 16 counts at 100 bpm = 12.0 s); localStorage holds only `curio-motion`, stated in notes | pass |

**3. Facts.** Recomputed: tempos (walk and slide 100, skip and gallop 120 swung, Levels 96) match the spec; a trip is
4 + 16 counts; Draw counts 16 per 100 units clamped 8 to 32; zigzag corners at x 30, 50, 70; round 7 circle center
(25, 35.5), radius 20.86, so z 14.6 to 56.4 on the floor, as the code comment says. Notes and tool.draft.json match
the spec's Sources and the tool's behavior, apart from finding 6.

**4. Giveaways.** None. In Mystery the level guide stays blank through every trip (`shownLevel` null in all 572
samples, the stage description names no level), the hidden ribbon is invisible until a right path answer, the painted
ribbon is plain (no level pattern) until the level is answered, every trip ends at the same spot (x 90) except the
circle, and the dancer ends in a plain stand. Level answers only show after the path is right.

**5. Language and notes.** Plain and short for K-2, every line voiced. Findings 2, 4, 5, 6, 9. No sensitive topics
in these standards; the notes' adaptation line for children who can't kneel or go on tiptoe is good.

**6. Guardrails.** Teacher led, no points or timers; Mystery's 8 dots and gallery are fine for this topic.

**7. Sensitivity.** Nothing cultural, Native or hard-history; rule 5 does not apply. The painted guides are people art
(rule 11), marked `people: true` with a recorded review; that is Craft's check.

#### Audit pilot

Leads confirmed:
- Welcome not heard on a first tap of a level, a move, Up and down or Surprise: confirmed, but the premise comes back:
  wLevels is logged `silent, early` on load and then spoken right after the first move's freeze (19.6 s in the Low
  Stretch run). Not a teaching gap.
- Size and state rows clean: my own frames at 1366x768 in every mode agree; I cited the audit for Done when 8.

Leads that were wrong:
- "Stretch: event line lost (spoken 0 of 5, dropped 5: stale)". Five held taps 2 s apart: "Stretch!" spoken 5 of 5,
  each followed by "Middle level". The 5 dropped entries are the tool's empty-key barrier item (`key: ""`), not the
  Stretch line; the audit counted them as the event.

Not checked by me: the `#d-surprise` left disabled after a mid-action resize (Craft and Play's area).

What it missed (teaching, outside what it can see): the grade 2 code covered only by pathways (1), the middle-level
line with no body cue (2), High reading by arms only (3), locomotor and nonlocomotor never named (4), the home ideas
(5), the low-level note against the crouched trips (6), hidden older badges (7), and the drawn-path edge readings
(10).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: levels-and-pathways (Codex fix, round 1)

Evidence paths below are relative to `_scratch/levels-and-pathways/`. This is not an exit PASS. Instructions and quiz integrity are reported separately: under the requested cheat gate, items 5, 6 and 14 remain NOT FIXED because blind enumeration can fill a Mystery dot, even though their requested narration changes are observed.

#### Blocker

None listed.

#### Should fix

1. FIXED: replaced remote annotation cards and routed leaders with badges directly on their own parts. A joint placement search separates compact targets. Before: `fix-before-parts-real/before-parts-680.png` and `fix-before-parts-real/before-parts-375.png`, real pointer drags. After: `fix-ui-final/ui-final-parts-680.png` and `fix-ui-final/ui-final-parts-375.png`, same four-part geometry at 680x425 and 375x812. Zero leaders and zero overlapping hit rectangles; all four targets are 64x64, with 11 px minimum numbers. The 1366 layout was also checked.
2. NOT FIXED: reproduced Bend, Twist, Swing, idle Low and Low Gallop at 1366x768 in `fix-before/before-low-*.png`. Rounded trouser underpainting, folded-leg depth ordering, a hand-only green-alpha filter, knee-contact rest-arm angles and a neck limit improve specific seams. `fix-targeted/final-low-*.png` still shows a cropped kneeling silhouette and imperfect articulation. I do not claim a complete painted-rig repair. A trial arm underpainting was removed because it weakened the otherwise stronger standing artwork.
3. FIXED: DA:Pr4.1.2a removed from the standards claims in the source header, spec and notes; its move to choreography-board is written in the spec, notes and handoff. Header claim count is zero. The merged Teaching review identifies the missing grade 2 expectations; the named source remains National Core Arts Standards, Dance (2014), in spec Sources. No receiving sibling or catalog file was edited because those paths are outside scope.
4. FIXED: the held High guide tap changes selected and shown levels to high, with aria-pressed true (`after-guide.json`). Bands select levels in Levels, Pathways and Draw. Mystery instead shows a display scale without individual card borders or keyboard controls; its target is hidden. Phone guide controls measure at least 60x61. Final 1366 frames: `final-mode-levels.png`, `final-mode-paths.png`, `final-mode-mystery.png`, `final-mode-draw.png`. Part/guide accessibility is no longer hidden inside an image role.
5. NOT FIXED under the cheat gate: the requested ending is observed. `fix-extra/gallery-1366.png`, `fix-extra/gallery-680.png` and `fix-extra/gallery-375.png` show "Tap Play again for new mysteries." The matching JSON logs record replayHow once, after the bow enables Play again. However, blind enumeration still fills a Mystery dot; see Cheats tried.
6. NOT FIXED under the cheat gate: the hint defect itself is corrected. Before: `fix-before/before-mystery-trip.png`, Go disabled while its name remains in the hint. After: `fix-after/after-mystery-trip.png` and `after-mystery-trip.json`, watching hint while Go is aria-disabled true. watchTrip is spoken once on the natural walk. The retained guessing route prevents a full FIXED claim under the requested gate.

#### Polish accepted

7. FIXED: Middle now says "Middle level. Stand up, not too high and not too low." in runtime, lines.json and the spec table. atMiddle is spoken once in `fix-walk/main.json`; the full walk used held clicks with 2-second gaps.
8. FIXED: High lifts the whole painted figure while toe tips remain anchored, rather than reading only through raised arms. `fix-regression/high-rise.png` and `high-rise.json`: an additional 11.036 px heel rise at 1366x768. The same transform applies to guides, mirror and button rigs.
9. FIXED: Levels names staying in one place; Pathways opens "Now we travel!" Notes name nonlocomotor and locomotor. Final short Levels welcome heard once in `welcome-final.json`; Pathways heard once in `fix-walk/main.json`. The welcome also includes copying in bubble space.
10. NOT FIXED: empty queue barriers are removed from newRun and afterRead. The full walk has zero blank voice-log entries, and Read retains priority (`read-priority.json`). The kit exposes no Read-completion promise, so count-ins still use its conservative duration cap. The exact public API addition is in handoff and Engine changes wanted below. No kit file was edited.
11. FIXED: Support at home now has three tool-specific activities possible tonight: paper pathway and walking, sky/table/grass shapes, and curved around a chair then straight back. Seated/hand alternatives remain. Verified in notes.md.
12. FIXED: notes explicitly distinguish sitting/kneeling/lying for moves in place from a deep crouch when traveling. Verified in notes.md.
13. FIXED: older ribbons have separate, fully opaque badges at staggered positions along their own ribbons. `fix-regression/three-ribbons.png` shows three readable badges after three real trips. `three-ribbons.json`: three badges, each 58.8x28, with disjoint rectangles. They no longer fade with the older ribbon groups.
14. NOT FIXED under the cheat gate: circleCurved is heard exactly once after round 7's correct answer in `fix-walk/main.json`; the natural walk frame is `fix-walk/circle-round-7.png`. The requested teaching cue works, but blind enumeration still advances the same Mystery progress check.
15. FIXED: removed the separate Copy me wait and put its meaning in the welcome. The first move takes its first shape immediately during its call. `after-first-move.json` observes the Twist shape at 294 ms from the test timestamp, including the held press, instead of the reproduced roughly 8-second wait.
16. FIXED: no start star is drawn in the gallery. `gallery-1366.json`, `gallery-680.json`, `gallery-375.json` each report zero gold-star polygons; their frames show the fifth ribbon's full beginning. The natural eight-round gallery is also in `fix-walk/gallery.png`.
17. FIXED: the studio SVG is a labeled group. `access-keyboard.json` shows Part 1 and Part 2 as unignored buttons in Chrome's accessibility tree, with full labels. Enter twice cycles low to middle and retains part focus. Frame: `access-keyboard.png`.

#### Settled calls

Applied: no sensitivity lens was added, no new activity or topic was added, the rich studio/cast/ribbon design is retained, and the existing Done when content remains. The prior contract/voice verdict was a starting point, not proof for the changed bundle. The spec's open question was left untouched. No fresh lens pass was run.

#### Cheats tried

- Blindly tap all pathway answers during travel: zero solved, step remains go. Guide High and Next before answering: zero solved, round 0 remains the path question. Hidden level inspection: shownLevel null, no revealed level badge, guide unavailable as an answer control. Natural-run record: `fix-walk/main.json`.
- Cheapest successful bypass: wait through required replays and try choices in turn. Curved, Straight, High, Middle fills the first progress dot without identifying either movement. `all-options-cheat.json` and `fix-cheat-retry/all-options-cheat.png` show attempts and solved [true]. The first broader sweep exceeded the driver's 60-second evaluation bound; one smaller retry completed and exposed the bypass.
- Spec decision followed unattended: keep the eight exact rounds, unlimited wrong-answer replays and no wrong-answer count. Closing enumeration would require changing that teaching/check design. I did not add lives, attempts, a new assessment or a new score. This is why the Mystery-related items above remain NOT FIXED under the requested gate.

#### Voice walk

The natural path used real held clicks and 2-second gaps: Levels welcome, Stretch/Middle, Low, freeze, Pathways welcome, Straight/Walk, ribbon, Mystery welcome, watching cue, eight path/level answers, circle teaching cue, gallery. `fix-walk/main.json` records eight solved, zero runtime errors, zero external requests and zero blank entries. wLevels, wPaths, wMystery, watchTrip, atMiddle, circleCurved and allDone each started once. The later shorter Levels welcome and separated replayHow were individually rechecked in `welcome-final.json` and all three gallery JSONs.

Side path: Draw welcome, Surprise path, part names, tapPart, danceIt, in `voice-side.json`. Read before Twist keeps the move's real lines queued behind Read, with no empty stopper. All 49 runtime strings equal voice/lines.json. Twelve lines use browser fallback because recordings are absent; no audio was recorded.

#### Engine changes wanted

`kit/curio.js`, Curio.voice return object: add `waitForRead: () => readP`, resolving on natural Read completion or hush, including Sound off. Then afterRead can await that public method instead of the conservative cap. No engine edit made. The Low painted kneeling repair remains art/renderer work, not a claimed engine fix.

#### Checks and frames

Final bundle: 871,289 bytes (about 851 KiB), below the 2 MB goal. Final four-mode 1366x768 and accessibility run: zero runtime exceptions and zero external HTTP requests. Before/after and regression frames were viewed individually and in contact-0.jpg through contact-5.jpg. Motion off, grayscale and the Beat Lab/Snowy Mail Route comparison frames are in fix-regression. The studio retains its richer surfaces; the weak Low silhouette is explicitly open.

Best moment: the eight-ribbon gallery. Flattest moments: the first move's silent preparation, shortened here, and the Low kneeling silhouette, still open. Optional nits touched: stale pose requests are marked deferred; the spec's art and voice descriptions match the painted rig and changed cues. Other nits are left alone.

Commands: bounded reads/checks, 120-second bundles, 300-second drive batches, and one 2400-second audit. The first three short read calls lacked an explicit process timeout; subsequent shell commands were bounded. Early failed reproduction attempts selected a directory or the host rather than its iframe; corrected before the part-badge repair. Early host favicon 404s were test-host requests and were removed from later runs with a data favicon.

#### Audit

Audit not finished. The single audit was started with a 2400-second process limit on Chrome 9911 and host 8715. The session was cut off before it completed; the restarted session did not run a second audit. Saved report: `fix-audit/audit.md`.

The seven direct viewport sizes, 680x425 through 1920x1080 plus 760x900, were clean. Pathways, Mystery and Draw mode-entry checks reported nothing new. Completed movement/drawing states, resize stress and the control/voice walk were not finished. The partial report's placeholder "clean" text in later sections is not evidence those stages passed.

Both saved leads are answered: (1) "iframe context not found" at 375x812 is an audit coverage failure; there is no audit phone frame. Separate drive.py iframe frames and numbers in fix-ui-final demonstrate the targeted phone badge and guide changes, but do not replace the missing full phone audit. (2) "no #hint element" comes from that same unread iframe context, not an observed missing tool hint: default-375.json and the phone frames show the real #hint. The final four-pixel phone hint-padding adjustment was bundled before the audit, but the audit failed to measure it, so its final full-viewport fit remains unconfirmed. These are recorded gaps, not a clean audit claim.

The restart verified that source, bundle, spec, notes, voice, audit states and refine.md still matched the saved pre-audit SHA-256 manifest. No browser/server was restarted because the remaining work was reporting. The temporary tool host.html is absent.

#### Left open

Low painted articulation (2), the successful Mystery enumeration route affecting 5, 6 and 14 under the requested gate, and a public Read-completion signal (10). The integrator must move the grade 2 standard in shared catalog/receiving-tool files outside this session's scope. The interrupted full audit and final phone hint-fit measurement also remain open. No git commit. refine.md and refine/ were not edited. No deployment or upload.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Levels and Pathways handoff

#### Fix pass, November 4, 2026

The active merged list is refine.md. The fix evidence is in _scratch/levels-and-pathways/fix-before,
fix-before-parts-real, fix-after, fix-targeted, fix-extra and fix-walk. The final status belongs to polish.md.
No kit files, catalog files or sibling tools were edited. No commit was made.

Part controls now sit on their own parts, without leaders. Compact placements are planned together along the
actual part geometry so all four 64-pixel targets remain separate. The studio SVG is a labeled group instead
of an image role, exposing its controls. Guide bands select levels outside Mystery; Mystery disables them.

The painted rig adds rounded underpainting, folded-leg depth ordering, a hand-only green-alpha filter and
a head/neck limit. Low rest hands use solved knee-contact angles. The kneeling silhouette still needs an
art-quality check: these are corrections to an articulated T-pose, not newly painted kneeling illustrations.
No new raster or new people artwork was generated in this pass.

DA:Pr4.1.2a is removed from this tool's claims in src.html, spec.md and notes.md. Move it to choreography-board
for full teaching of facings, symmetrical and asymmetrical shapes, and circling versus turning. The integrator
must update the shared catalog and the receiving tool because those paths are outside this session's scope.

Copy me and bubble space are folded into the Levels welcome. The first move shape appears during the call.
The new Middle cue names body height. Mystery immediately shows the watching hint, teaches that a circle is
curved after round 7, and names Play again only after the gallery bow enables it. Runtime and lines.json
contain 49 identical fixed lines. Changed and added text uses browser voice fallback; no recording was made.

Mystery retains the spec's eight exact rounds and unlimited wrong-answer replays. It measures completion,
not demonstrated mastery. Blind answer enumeration must be reported honestly if it fills a progress dot;
do not add attempts, lives, a new task or a new scoring rule without a spec decision.

Cold review completed November 3, 2026 in S:/CurioClass-codex. No commit. See codex-review.md for the review outcome.

#### Files and structure

src.html uses kit:curio and kit:dance. Permanent panel controls precede the stage in DOM order.
The script holds the narration table, six move libraries, pathways and eight exact Mystery rounds, the painted rig,
panel handlers, studio, run lifecycle, drawing recognition and responsive layout. Nothing in kit was changed.
The offline bundle is levels-and-pathways.html. tool.draft.json stays at stage built.

#### Painted guides and swapping the figure

The single art/painted-dancers.webp atlas contains three adult guides: varied skin tones, hair and body shapes,
consistent teal clothing and cream shoes. Every person-containing asset has people true. The source sheet and
36 articulated move endpoints received a fresh people-art review. The raw painting is art/raw/painted-dancers.png.
The full built-in imagegen prompt is in art/prompts.json. The original studio painting is retained.

PAINTED_CAST contains landmarks and clip boundaries in the final 1536 by 707 atlas. paintDancer attaches painted
segments to a Dance.dancer model's projected joints. The model group is hidden; its clock, skeleton, grounding,
trails and pose library remain authoritative. The painted head keeps its shape under forward bends. Torso width
follows facing and twist. The main figure, its clipped mirror reflection and the button poses all use the atlas.
setCast swaps only the painted renderer. Each mode uses one consistent guide throughout its trips.

To replace a guide, replace the atlas and that guide's landmarks/clip bounds in PAINTED_CAST, then recheck standing,
raised arms, forward bend, floor shapes and travel. Separate static paintings for every keyframe are unnecessary. One separate painted-gallery-bow cutout keeps the
finished gallery bow readable when a flat puppet torso would be too foreshortened. It appears only at the bow
endpoint; the model still owns its timing, position, mirror projection and shadow.
The former 32 pose requests remain in the manifest as superseded history pointing to this compact rig.

#### Review repairs

- Right-path praise survives an immediate level answer, including when it has not begun playing yet.
- During a Mystery return, the hint says to watch the dancer return, then names Go only when it is available.
- A running drawn dance locks its level/way selectors, so its planned badges and actual ribbon remain consistent.
- Editing or replacing a drawn path hides the previous performer and shadow until Dance it is tapped again.
- Mode changes, Clear and Surprise path cancel an unfinished pointer drawing safely.
- Clean floor cannot overwrite the next mode's hint after its fade completes.
- Badge placement reserves the complete 64-pixel hit areas, avoids the full drawn lines and separates leaders
  from interactive bounds. Four phone badges are packed together. Draw uses its spare phone panel space for
  a taller stage and two annotation rows; controls and hint still fit at 375 by 812.
- Repeated idle settings speak every event, then give one short next-control cue per mode.
- Re-selecting the current mode does nothing, preserving its welcome and the student's work.
- Ordinary moves/settings preserve Read priority; mode changes and resets can release it. The kit's private
  Read promise is joined through its voice queue while Sound is on. Sound off uses the helper's conservative
  speech-length allowance because the kit exposes no Read completion event. Both paths received held-click checks.
- The quiet preparation is lifted with an immediate warm mat response and four large real-clock count-in dots.
  Motion off preserves the same timing and static cues.

#### Teaching and timing

Six moves at three levels retain 36 A/B endpoints. Low shapes remain seated, kneeling or lying; the highest Low
keyframe head is about 0.563 body heights including the head radius. Levels uses 96 beats per minute.
Up and down retains 40 counts, High, Middle, Low, Middle, High. Walk and Slide use 100 beats per minute;
Skip and Gallop use 120. All trips retain 16 counts and a four-count preparation.
Draw counts use largest-remainder allocation with two counts reserved per part, totaling exactly 8 to 32 counts.
The ribbon's colors, patterns and icons remain redundant. Mystery reveals neutral gold before the level answer.
Mystery round 7 is the full curved circle, and all eight rounds end in the ribbon gallery.

#### Narration and storage

Curio.voice owns Read, once-per-load how lines and repeated event lines. All 47 runtime strings match lines.json.
Existing recordings are retained. Six lines use browser fallback: Draw welcome, Clean floor, Clear, return-to-star,
choose-a-move and Go cues. No audio was recorded. No dance, drawing or progress is stored or sent anywhere.
The shared Motion control still remembers its setting on this device, as the standing standards require.

#### Standards decisions

BASELINE w1-21 keeps dance's figure separate from PE. Mystery teaches DA:Re7.1.Kb. Draw a path supports
DA:Cr1.1.2b through different levels in one dance. DA:Cr3.1.1b is not claimed: one way of moving is chosen per path.
The prior spec routes grade 1 and 2 Re7 expectations to the dance siblings. Catalog and spec were not edited.

#### Engine changes wanted

kit/curio.js, Curio.voice return object: add `waitForRead: () => readP`. The returned promise must resolve
when Read finishes or hush cancels it, also with Sound off. Then the tool's afterRead can await that public
method instead of a conservative duration cap. Empty queue barrier lines have been removed locally; this
remaining dependency is not fixed here. No kit change was made.

kit/curio.js, init Motion handler: optional in-memory preference for tools that request no persistence, while
retaining the shared Motion control. No kit change made. Dance.readPath retains its documented limit for finely
squeezed or shaky compound waves on small stages. Do not loosen shared thresholds from a few passing examples.
An explicit Read completion event would remove the Sound-off timing estimate. The four-part phone finish is
still the densest composition: its duplicate ribbon-end icon lies close behind Part 4's generous hit area.
The numbered cards remain readable and do not overlap each other. Keep this as polish for a later pass.

#### Evidence

All current review evidence is under _scratch/levels-and-pathways: cold-frames, review-frames, functional-frames,
drag-review-frames, size-frames and review-audit. Driver scripts and machine-readable results are there too.
Use codex-review.md for the exact audit result and remaining limitations. The builder report describes its earlier
build only and is not current review evidence. This review used Chrome 9950 to 9957 and host 8755 only.
The single review audit reached its 2400-second bound with 30 leads and 77 frames; it did not finish stress checks.
Its snapshots precede final repairs. Focused checks answered its real leads; no second full audit was run.
The four-part audit drag fixture lacked a return expression during that run. It is corrected, and actual pointer
drags at 1366 by 768, 680 by 425 and 375 by 812 verified four parts separately. The random mixed-plan fixture is
now seeded so resizing compares the same labels. A deterministic resize and Enter-twice check preserves focus.

#### Interrupted fix audit

The November 4 fix audit was started once with a 2400-second limit, Chrome 9911 and host 8715. The session cut off
after seven clean direct viewport sizes and the three mode-entry checks. It did not finish the later states,
resize stress or control walk. The 375x812 audit iframe could not be attached; its missing-hint lead is secondary
to that unread context. Independent phone drive frames exist, but the final four-pixel phone hint-padding
adjustment has no final full-viewport measurement. The resumed session verified unchanged saved artifacts and
finished reporting without a second audit. See polish.md and _scratch/levels-and-pathways/fix-audit/audit.md.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: refine.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-04)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
- 2026-11-25: earlier round refine-2026-10-28 moved to S:/CurioClass-archive/tool-rounds-2026-11-25/levels-and-pathways
- 2026-11-25: earlier round refine-2026-10-28.md moved to S:/CurioClass-archive/tool-rounds-2026-11-25/levels-and-pathways
