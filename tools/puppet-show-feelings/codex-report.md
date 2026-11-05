# Codex report: puppet-show-feelings

## Built
Three teacher-led K-2 modes in one offline file: the six-scene puppet story with three endings; Backstage with nine settings, audience reveal and six Try it targets; Like me with six personal connection prompts and a changeable ending vote. No commits or polish round.

## Numbers check
Recomputed all 27 nearest-prototype cases, all five hand-set ties, scene presets, feeling totals and contrast before implementation. All agree with the spec. Totals: sad 4, worried 7, calm 3, proud 3, happy 5, excited 5. Contrast: 5.2986, 4.9373, 14.9801 and 6.0570. Evidence: `numbers.json` in Scratch.
Tilt is 28/0/-18 degrees with 250 ms easing. Bounce is 0, 12 at 1.2 Hz, or 34 at 2.2 Hz before stage scaling. Babble uses 260/150/95 ms syllables and .85/1/1.15 pitch multipliers, two or three blips per syllable.

## Feel check
Best moment: change only the head from Down to Straight to Up and the same quiet line reads sad, calm and proud. The audience reveal makes the class commit to a reading first; Try it gives a specific check and spoken praise.
Flat moment 1: the compact ending tiles covered Pom. Moved them down to the ledge, keeping all three in view and Pom's head visible.
Flat moment 2: the tall tree was behind the curtain, so the stuck-kite scene did not show its cause. Redrew the park with the whole tree inside the opening and placed the kite in its branches.
Also redrew both open mouths from their closed references to preserve identity. Fixed tall-layout theater proportions and Like me's small puppet, then widened its ring so extreme tilts stay clear of cards. Ending kites now stay visible in front of Pom; the high kite clears the curtain. The Line button shows a scene miniature and the worried icon has raised inner brows.
Opened Snowy Mail Route and Beat Lab before building. The side-by-side `bar-comparison.png` and final theater frames show comparable scene richness: knit texture, layered cardboard, painted curtains, a leafy park and shelf art. Pom's continuous tilt and bounce are the main feedback, rather than a numeric display. A teacher-led whole-class conversation is still needed for the intended 15 to 20 minutes.

## Done when
1. PASS with compact layout interpretation: Pom is the central character at 1366x768 and 680x425. All nine controls stay visible. Short landscape uses side-by-side controls as STANDARDS directs; larger layouts put them below.
2. PASS: clicked every combination and compared all 27 results to the table; presets and scene settings recomputed. `gameplay.log`.
3. PASS: measured the 250 ms tilt transition and timing/pitch logs; bounce preserves phase while amplitude and frequency blend. `smoke.log`, `gameplay.log`.
4. PASS: changes interrupt old babble immediately, update the pose and hide the audience card. Tested during active playback.
5. PASS: all three endings reached with real clicks; choice scene alone disables Next, ending controls remain after choosing, Play again restarts.
6. PASS: all six targets met and cycled; all six praise events logged as spoken. `final-checks.log`.
7. PASS for queue behavior: Show logs scene, then babble, then question. Five-action Backstage run spoke each how-to once; audience events spoke at two-second pace. Read preserved a queued audience result. Sound quality has not been auditioned.
8. PASS: visible controls measured at least 60 px in every mode and required size. Chosen controls have a thick border and check, feeling icons include words.
9. PASS: Motion off stays stationary with immediate tilt, unchanged syllable durations and no infinite CSS animation. Keyboard and grayscale frames inspected.
10. FAIL for literal storage wording: tool makes no network calls and saves no lesson state. The shared kit persists Motion preference as required by the contract, an exception to the spec's literal nothing-saved wording. The iframe host's favicon 404 is outside the tool.

## Wave lessons
- PASS: Hint and voice: checked immediate hints, Read, stale cancellation, `V.heard`, two-second actions and choice-scene disabled Next. Browser speech fallback only.
- PASS: Focus and layout: controls stay in place; reveal moves focus to Again before hiding; scene 5 moves it to an ending before disabling Next. No focus on load.
- PASS: Sizes: one full three-mode pass at all eight sizes, followed only by targeted repairs. All controls and hint visible.
- PASS: No giveaways: audience feeling stays hidden until asked and hides on every setting change. Try it is a requested practice target, not a concealed-answer quiz.
- PASS: Honest numbers: no score or diagnostic meter. Notes identify the table as a simplified classroom model.
- PASS: Standards: students read cues, direct cues, choose an ending and connect a feeling to their own experience. TH:Re7, TH:Re8 and TH:Cn10 each have an interaction. No family engine.
- PASS: Motion off: RAF keeps timing without displacement; the breeze loop is removed, not sped up.
- PASS: Short choices visible: all nine controls, six feeling cards and three ending options fit; no choice scroll panels.
- PASS: Resize during action: passed in the single audit: no exceptions and nothing left disabled.
- PASS: Delayed welcome: each mode has scoped welcome behavior and cancels stale work on entry or a meaningful first action.
- PASS: Unknown as unknown: hidden audience card gives no unasked result.
- PASS: One look, one meaning: consistent face-plus-word feelings and check-plus-border selections.
- PASS: Badge truth: audience card uses the current lookup; target check uses the same lookup.
- PASS: Hint restores: Show, Backstage, Try it and ending vote immediately restore the appropriate hint when their state changes.
- PASS: No copying answer words: students read the puppet before revealing the audience result. Like me is explicitly a named-feeling connection prompt.

## Audit leads
The single full audit exited successfully within its 40-minute limit, with 10 leads. All default sizes, Motion off and mid-action resizes were clean. The nine authored states covered all three modes at every size.

- Two `#feelings` keep-region leads: the ring parent deliberately contains an empty center around Pom. Replaced the parent keep with the six actual buttons. The final layout also widens the ring and keeps the tilted face clear; all six cards remain visible and at least 60 px.
- Four welcome leads, `#reveal`, `#back`, `#next`, `#again`: retained the chosen action's narration instead of queuing a stale welcome behind it. Back and Again narrate the visible premise themselves. Next and Show me deliver their requested result. This follows the shared voice priority rules.
- Three quick mode-tap leads: confirmed and fixed. A selected mode now returns without hushing its welcome. Each mode's welcome spoke once without a cut in the 0.7-second repeat check.
- One quick Next lead: the Whoosh event is intentionally interrupted when Next advances again. Returning it in the new scene would be stale and would violate the spec's immediate navigation rule.

The audit's automatic mode finder saw zero modes because it searches only inside headers. Authored states cover the separate navigation bar. Explicit checks also exercised all 27 settings, all six Like me cards and all three votes, including narration at a two-second pace.
After the audited bundle, final fixes received 21 targeted frames and checks, not a second full audit. They cover the mode guard, target praise, ending prop placement, new-kite redraw, Line pictures, worried icon and Like me ring. `quick-modes.log` confirms three praise events for three successive valid changes; the earlier synchronous probe in `repairs.log` returned before the queue pumped and is not used as speech evidence.

## Frames looked at
All build screenshots inspected, including full three-mode size set; compact choices and challenge; all three endings; all 27 settings result; voice, Read, focus and keyboard checks; Motion off; grayscale; tall layout fixes; generated art sheet; final tree redraw; and bar comparison. Also inspected all 81 audit frames and 21 final targeted frames: repair-frames (12), quick-mode-frames (4) and ring-frames (5).
Evidence is under `_scratch/puppet-show-feelings/`; logs include full-0/1, gameplay, smoke, final-voice, final-checks and tree.

## Art made
Ten final WebPs total 478.6 KB. The final self-contained bundle is 1145 KB, below 2 MB. Voice manifest: 88 unique lines. No placeholders.
Ten final images: theater, park, Pom and Dot closed/open, red kite, new kite, stick and shelf. Both open-mouth puppets, the park and the new kite were redrawn using references. No generated people. Prompt provenance and raw images are retained.

## Art still to paint
None. All ten specified images are used.

## Engine changes wanted
No runtime engine changes. Audit helper request: in `scripts/audit_tool.py`, extend `MODES_JS` with `nav .seg button` so its automatic mode walk finds the separate mode bar. No shared file was changed.

## Left open
The specified smooth-narrator / Algieba identity is in the voice manifest, but there are no recorded clips because the build instructions prohibit recording. Browser speech supplies narration. A later voice pass and speaker/headphone listening check remain; muted browser automation verifies queues and synthesis timing, not sound quality.
The 15 to 20 minute classroom pace and children's interpretation of the simplified cue model need a teacher-led trial. Build instructions and STANDARDS compact layout take precedence over the spec's below-stage wording at 680x425.
The full audit precedes the final targeted fixes and was not rerun, following the build brief. The audit mode-discovery limitation is documented above. All owned browsers and host servers are closed; the generated tool host.html was removed.

