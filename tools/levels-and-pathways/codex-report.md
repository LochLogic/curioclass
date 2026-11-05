# Codex report: levels-and-pathways

## Built

November 1, 2026. Build only in S:/CurioClass-codex. No commit, branch change or polish round.
Completed the existing four-mode implementation using kit:curio and kit:dance, with one newly painted studio.
Added the painter manifest, renderer boundary, required notes sections, reached-state audit plan and current handoff.
Only tools/levels-and-pathways and _scratch/levels-and-pathways contain project changes from this build.
The offline HTML is generated from readable src.html; tool.draft.json remains stage built.

## Numbers check

Recomputed before implementation in Scratch/prepare.py; results in numbers.json. No discrepancy with the spec's numbers.
Six moves times three levels = 18 shapes, with 36 A/B keyframes. Five eight-count levels = 40 counts.
At 96 beats per minute, eight counts last 5 seconds and the four-count lead-in lasts 2.5 seconds.
Sixteen-count trips last 9.6 seconds at 100 beats per minute or 8 seconds at 120.
Straight length = 80 floor units; ideal semicircle = 125.664; four-leg zigzag = 144.222.
Contrast ratios match: white/teal 5.10, teal/paper 4.79, ink/paper 14.43, muted/paper 6.04;
white/high 5.75, white/middle 5.13, white/low 5.02.
Checked 3,000 unequal-part allocations: each retains its exact computed 8-to-32-count budget and at least two counts per part.

## Feel check

Played all modes, the full eight-round mystery, every pathway/way pair and mixed-level drawn dances using held inputs.
Best moment: the eighth mystery reveals a gallery of the class's eight different ribbons, including the closed circle, with a bow.
Flattest moments: the bare geometric room made waiting feel empty; the portrait layout interrupted play by hiding choices.
Changed them with a large painted studio, warm paper controls, quiet sunlight dust, and a portrait stage that reserves room for every choice.
Also stopped long-drag welcomes delaying the part names and moved drawn-part badges clear of the finished dancer and end badge.
The studio now matches the bar's level of finish. The temporary kit dancer is still the visual weak point, pending the owner's painter.

![Levels and Pathways beside Snowy Mail Route](S:/CurioClass-codex/_scratch/levels-and-pathways/feel-comparison.png)

## Done when

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

## Wave lessons

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

## Audit leads

The one complete audit command was attempted on Chrome 9981 with host 8785 and a hard 2,400-second limit.
It reached that limit during later stress work. No audit.md was produced, so there is no lead list or clean verdict to claim.
All 73 generated PNGs were inspected, covering default sizes, three other modes, five reached states and Motion off.
Partial evidence and the timeout are in _scratch/levels-and-pathways/audit/ and audit-console.log.
After that stop, narrowed freeze expiry, an idle-only Levels welcome and current-step hint selection received focused checks.
The audit was not rerun, as instructed. Final mechanical voice/resize aggregation is left for the cold reviewer.

## Frames looked at

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

## Art made

One generated image: an empty studio, made with the built-in image tool using the full saved house style and prompt.
No people were generated. No redraw was needed. Raw PNG and final 1600x900 WebP inspected at final size and in the tool.
Final art = 96,178 bytes, about 94 KiB. Final bundle = 743,230 bytes (about 726 KiB), under 2 MB..
art/prompts.json records drawn_by codex, people false for the studio, review, full prompt and OpenAI source credit.

## Art still to paint

32 deferred dancer assets, all people true, with explicit art tokens, A/B move frames, gait phases, facings, readiness and bow.
Use makeStudioDancer and onMove to install the paintings while retaining kit timing, projection, poses and trails.
The owner's final decision is painted dancers; the kit figure is temporary for this build.

## Engine changes wanted

kit/curio.js, init Motion handler: optional in-memory preference for tools requesting no persistence; no kit file changed.
kit/dance.js, readPath: broader small-stage orientation evidence is needed before changing recognition thresholds.
The existing shared-engine limitation is documented rather than hidden or improvised around.

## Left open

- Painted dancers, explicitly assigned to the next painter by the owner.
- Three browser-voice fallback lines: revised Draw welcome, Clean floor and Clear. Existing recordings retained; no audio recorded in this run.
- Broader real-hand orientation/compound-path recognition suite, particularly squeezed waves on the smallest stages.
- The full audit timed out at 40 minutes without its final report. No full audit pass is claimed.
- The full size sweep and full audit were not repeated after the final voice predicates; only their affected cases and keyboard path were checked.
- host.html is absent. All Chrome/server ports used by this build are closed, verified across 9980 to 9987 and 8785.
