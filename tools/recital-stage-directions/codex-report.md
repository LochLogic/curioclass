# Codex report: recital-stage-directions

## Built

Built the offline grades 3-5 tool with Stage map, Recital and Your turn. Draft stage is built.
It uses the shared dance engine, Curio Class settings and Curio.voice. No shared files were edited intentionally,
no git operations were performed, no audio was recorded and no polish round was started.

Features include both viewpoints, nine areas, three identifiable dancers, drag/tap/keyboard placement,
eight optional calls, live costumes and lights, two 24-count pieces, clue replay, main ideas,
the eight-trait Compare board, three spoken room phrases and guarded device-only saving/reset.

Final bundle: 475,933 bytes, 464.78 KiB, below 2 MB. All owned browsers and servers are closed; host.html is absent.

## Numbers check

Independent calculations are in `_scratch/recital-stage-directions/numbers.py` and `numbers.txt`.

- 24 counts at 72 beats a minute = 20 seconds; at 104 = 13.846154 seconds.
- Followed the detailed Content value of 20 seconds for Autumn Leaves, rather than the earlier 15-18 second summary.
- Room phrases: 28 movement counts + 16 lead-in counts = 26.4 seconds at 100, or 33 seconds at 80, plus calls.
- Stage right mirrors from x 0-33.3333 to screen x 66.6667-100. Call 8 accepts UL, CL and DL, including shared areas.
- Spec contrast ratios recompute to 10.32, 15.59, 8.45, 12.87, 8.52 and 12.21 to one.
- All six dancer phrases total 24 counts. Sampled positions remain finite.
- Final sink samples decrease from head height 1.0173 to 0.5742 body heights without rising again.
- Jazz jump samples have one airborne star shape, then grounded landing and freezes. Anticipations precede 12 and 16.

## Feel check

Played the cycle through placement, calls, both full recital runs, clues, ideas, Compare and a complete slower room phrase.
Best moment: flipping a populated stage and seeing the guide's own hand identity and the dancer badges stay attached.
The student's lights and costumes also remain live while the recital continues.

Two flattest moments and changes:

- Both initially showed a small sample. It now presents two troupes of three, with each piece's saved production choices.
- Phone clue reading felt like scrolling through homework. Its shorter stage and fixed actions now keep all eight clues visible.

The bar comparison exposed a flat floor. Added shaded floorboards, seams, fasteners, velvet shading and actor contact shadows.
The theater uses both paintings prominently. The temporary kit figures remain the main visual limitation.

![Tool beside the bar tools](S:/CurioClass-codex/_scratch/recital-stage-directions/bar-comparison.png)

## Done when

1. FAIL under a strict always-visible-plan reading. Initial Stage map focus, toggle and plan pass at 1366, 680 and 375.
   Phone clue/idea reading deliberately hides the plan to fit the answer choices. See responsive limits in handoff.md.
2. PASS. Seats put stage left on screen right; reverse puts it on screen left. Geometry checks confirm hand identity
   and unchanged canonical dancer positions. The 800 ms camera transition is an approximation, not full 3D.
3. PASS. All eight reference calls pass; negative cases reject audience-left placements for call 8 and invalid call 4 counts.
   Straight center and diagonal formations retain exact area centers. Shared areas hold up to three dancers.
4. PASS. Held clicks changed costume, light, view and clue selection during Watch while its clock continued beyond count 15.
5. PASS. Correct clues replay into their count and freeze; wrong clues identify their absence. Both idea choices give feedback.
6. PASS. All eight traits were placed and checked. Each plays two counts; Both displays six figures in two groups.
7. PASS for sequencing and timing. Calls are awaited before lead-ins; a complete silent Slower run finished at 80.
   A sound change continued into count 3; Read stopped counting before speaking. Acoustic review remains open.
8. PASS. Five held selections at a two-second pace produced one spoken how line and four heard/silent repeats.
   Five correct checks produced five spoken event lines. Mode/step welcome validity is guarded.
9. PASS. Costume, light color, unlit UR, clue choices and a partial Compare board survived fresh tabs.
   Start over removed the storage item and reset choices; storage failures and malformed values are guarded.

## Wave lessons

- Hint and voice: PASS. Hints update synchronously, name current controls, and Read includes an active stage call.
- Focus and layout: PASS in targeted runs. Persistent controls retain focus; natural Tab/Enter/arrows solved call 1.
  Reverse arrows retained dancer focus. The guide moves within C and shrinks when it shares the area.
- Sizes: FAIL for the strict universal target/scrolling rule. Main actions fit; some perspective tiles are under 44 pixels,
  with 44-pixel plan alternatives. Phone production options and setup details still require page scrolling.
- No giveaways: FAIL for the specified main-idea title cue described below. Badge shapes and grid IDs reveal no call answers.
- Honest numbers: PASS. Beat rates and count totals are explicit; calculations and coordinate rules were recomputed.
- Standards: PASS. Solo actions teach area use/timing, production choices, movement evidence and comparison of the two pieces.
- Motion off: PASS in frames and source checks. Idle glow stops; the engine retains count pacing and steps poses by count.
- Short choices visible: FAIL for phone production choices. Clues and main-idea choices fit; secondary dress/light options scroll.
- Resize mid-animation: FAIL as a completed verification claim. Relayout preserves world state, but the mechanical audit
  did not finish its report. Live view/costume/light changes were checked separately; a cold resize recheck remains.
- Welcome put off past first action: PASS. No welcomeAfter; valid/needs guards prevent hidden-step and Compare welcomes.
- Unknown shown as unknown: PASS. Calls have no ticks before Check; unplaced Compare traits remain unassigned.
- One look, one meaning: PASS. Circle, square and triangle retain identity; ticks/crosses also carry words.
- Badge says what is true: PASS. Area status comes from placement; old call verdicts clear on Next call and reset.
- Hint changes back: PASS. Mode, step, piece and phrase changes update current hints/captions and clear stale results.
- No answer by copying words: FAIL. Autumn Leaves and its correct idea share leaves. Preserved the spec and documented it.

## Audit leads

Audit not finished. The single command reached its 40-minute limit during the control/voice walk.
It produced 81 PNGs but no audit.md, so there is no completed mechanical lead list to claim or dismiss.
Evidence and timeout record are in `_scratch/recital-stage-directions/audit/`.

Frame/source issues repaired during this build included mirrored negative-width rectangles, guide/actor collisions,
compact primary buttons below the fold, tiny setup-diagram text, phone action overlap, stale captions/hints,
looping sink/jump keyframes and hidden-control welcomes. Final targeted batches had zero console errors.
The full size sweep and audit were not repeated after these targeted repairs.

## Frames looked at

All manual shot batches were viewed as full frames or labeled contact sheets; all 81 audit PNGs were viewed in 14 sheets.
Scratch contains `early`, `early-fixed`, `checks`, `late-checks`, `sizes`, `phone-early`, `phone-final`,
`targeted`, `phone-targeted`, `final-checks`, `extra-targets`, `phone-last`, `phone-last-fixed`,
`phone-last-final`, `keyboard-only`, the audit frames and the two bar frames.

The size sweep covers 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a 375x812 iframe.
It includes all modes, reverse view, calls, clues, ideas, Compare, Motion off and grayscale.
Later shots rechecked only affected layouts or behavior. Both full recital completions preceded the final keyframe repair;
the repaired keyframes were then sampled independently and the final floor curl was rendered and inspected.

## Art made

Two images generated with the built-in imagegen tool: house-from-stage and recital-backdrop.
Both are used, copied into art/raw, processed only with free art.py --rekey, and inspected at 1400 pixels wide.
Total finished art: 217,670 bytes, 212.57 KiB. No redraws were needed. No people were generated.
Full prompts, house style and provenance are in art/prompts.json. Credit is in tool.draft.json and the source comment.

## Art still to paint

Fifteen deferred people:true pose sets cover the guide and recital dancers, including facings, sides, gait keyframes,
badges and costume variants. Detailed movement requirements include the one-way sink and pre-beat clap.
POSE_ART tokens and the renderer adapter keep the current kit figures replaceable. Painted dancers are the owner's final choice.

## Engine changes wanted

- kit/dance.js, floor().resize: make x0/x1 describe actual front-edge pixels for stage's d0=140 projection.
- kit/dance.js, floor projection/inverse and figure projection: add a documented orbit/mirror interface that retains
  hand identity and avoids negative-width decoration. The build uses a local adapter; details are in handoff.md.

## Left open

- The mechanical audit did not finish. This is a build, not a clean audit or a post-build review.
- Painted dancers remain intentionally deferred; the authorized kit figures are temporary.
- Browser speech is the current fallback for easy-coach/Umbriel. No recordings or human headphone review were made.
- Phone production/setup scrolling, small perspective hit regions and the hidden phone evidence plan need cold review.
- The camera orbit is approximated; the family catalog question remains outside the allowed write scope.
- The main-idea word cue needs a spec/teaching decision. A fresh content review passed the history and jazz study,
  with pre-beat accents and a clearly low ending pose implemented as requested.
