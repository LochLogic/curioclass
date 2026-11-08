# Launch Pad handoff

Build only, 2026-11-03. No commits, branch operations or polish round.

## Layout and code

`src.html` began with the kit starter and uses Curio Class frame, theme-912, Curio.voice and the unchanged Plane engine.
The painted range and graph use their actual available pixel sizes. The graph stays the largest region at 1366x768
and 1000x625. At 760 wide the scene sits above the graph. On a phone both sit above the compact mission workbench.
In short landscape windows the hint and model notes move into telemetry, and Check work sits beside the inputs.
The same DOM controls remain in place through relayout, with deliberate focus moves using preventScroll.

The JavaScript contains nine mission records, a small arithmetic parser, exact-answer matching, a method workbench,
range drawing, Plane drawing and a requestAnimationFrame flight. Run generations cancel old flights immediately.
Flight time comes from the exact model. Accepted rounded answers use exact event times when played, so a rounded
landing answer does not leave a fast-moving ball several feet from ground. Two drone times receive 950 ms clock holds.
Motion off draws the full path immediately, retains the same real-time clock and shows still snapshots at events.
Completion records the chosen method and exact event answer in `curio-launch-pad`, with try/catch.

The curve and its root markers are hidden in unsolved Missions. The line height and tidied equation remain visible.
Factor checks expansion, including non-unit leading coefficients by normalization. Direct Square root is offered
when no linear term remains; otherwise it directs students to Complete the square. Complete the square validates
k and m, then both roots. Formula validates a, b, c, the discriminant call, then both roots. A final contextual answer
rejects negative times, launch time for mission 1, and the upward balcony crossing for mission 9.

## Art and voice

Six images were made with the built-in image tool during this build. Full prompts are in art/prompts.json; selected
raw PNGs are in art/raw and their free rekeyed WebP versions are bundled. The cold review replaced the balcony with a teenage catcher; that asset is marked people: true. The older lp-field-dusk
asset was preserved and is not used. The ruler measures the ball at the tube mouth. The launcher and base are
symbolic equipment below that reference; their own physical dimensions are not extra terms in the height equation.
The balcony rail is aligned to 40 ft using the inspected painting's rail position, and its glove aligns to the ball.

The narration queue uses the specified fixed lines and distinct repeatable event lines. Read uses the live hint.
No audio was recorded, as directed. Browser speech is the fallback, so the intended voice is not an embedded recording.

## Open question resolved

Use big-sister with the science-fair launch style line. This is the option the spec leans toward and avoids sharing
firm-captain with the more closely related Flight Planner. No other spec open questions were listed.

## Verification pointers

All build evidence is in `_scratch/launch-pad/`. `numbers.json` independently recomputes the nine missions, gravity,
extreme flight and four contrast ratios. `functional-results.json` records 50 passing assertions and exact event
heights. `keyboard-results.json` records a complete mission through real keyboard input with focus retained.
`size-frames`, `phone-fixed`, `special-frames` and the final audit folder contain visual evidence.

The stock drive key map cannot type digits, and the audit key map also lacks Home and End. Audit states therefore
seed text-box values through JS only, then use real held clicks for every transition and real drags for slider limits.
The separate keyboard script uses real CDP text input and key events without changing the shared driver or engine.
The original phone host's favicon 404 was a host-only issue; the bounded scratch host helper suppresses it with a
data icon and removes host.html after its shots. The delivered tool also has a data icon and no external requests.

## Engine changes wanted

None for kit/graphing.js or the shared kit. Optional test-helper improvement: scripts/drive.py's key map and
scripts/audit_tool.py's drive_keys should support digits, Home, End and Shift+Tab, so typed state paths need no text
seeding. This is outside the authorized write scope and was not changed.

## Next review

The cold reviewer should judge algebra explanations, the model's symbolic equipment, compact derivation readability,
browser narration timing, and whether the finished mission progression feels satisfying across a full class period.
This build includes a full nine-mission functional run, not a live classroom test or a cold review.


## Final build audit and targeted repairs

One complete audit finished with 37 leads. Seven unnamed-input leads received explicit descriptive aria-labels;
seven repeated tiny-axis overlap leads were fixed with additional bottom space and a centered time label;
two welcome-cut leads were fixed by making a tap on the selected mode leave that mode and its narration intact.
Twenty visibility leads are hit-test artifacts: the transparent Plane hit area is returned beneath visibly drawn
tick text and the pointer-transparent unsolved-flight message. Reviewed all 73 audit captures in contact sheets,
plus compact, phone and completed-flight frames at full size. Nothing is physically covered there.
The remaining first-Launch welcome lead is intentional: the spec explicitly makes wLaunch stale on the first Launch.
No late welcome is queued over the flight. The original full audit is preserved, not relabeled as clean.

Targeted checks only followed these repairs: compact Factor, Complete the square and Formula; a 375 px iframe;
two 0.7-second held taps on each mode; and the exact (t - 3/2)² = 41/16 display. All passed with no console errors,
no axis-label overlaps, named fields and no welcome cuts. The full audit and full size sweep were not rerun.
Clear missions was separately tested from nine records to zero and through a fresh reload. Final bundle is
228,174 bytes. The task's Chrome ports 9970 and 9971 and host 8775 were confirmed closed; host.html is removed.

## Cold review changes, 2026-11-07

The arithmetic parser now applies exponentiation before a leading sign, including negative exponents.
Mission 7 Complete the square has a derive step: u = 2a, v = 4a squared, w = 2a. Inputs are checked for
equivalence across several nonzero a values. The graph withholds the filled identity during that step.
Formula narration separately names coefficients and the discriminant, in the matching screen state.
Clear missions resets an active mission flight before clearing, preventing it from immediately re-saving.
The final flight card keeps the chosen method and actual directional events as the earned result.

The redrawn balcony is 320 by 226 pixels after rekeying. Its horizontal top rail is 47 percent down;
the glove is 14 percent across. The scene moves that flight column left to keep the full painting in view.
The replacement raw image is balcony.png; the built-in image generator was used and art.py rekeyed it.
The installed default Python lacks numpy, so free rekeying uses existing S:/AI/tts/.venv/Lib/site-packages
on the default interpreter's sys.path, with no package installation or shared-file edits.

## Sensitivity

No culture, religion, hard history or body teaching. A newly illustrated teenage catcher has brown skin,
ordinary clothing and natural proportions. The fresh visual reviewer should check the small-size crop,
hands, glove pose and respectful depiction. No identity is presented as representative of a whole group.

## Cold review verification and audit

The independent review ran 105 passing functional/cheat assertions, held-click main and side voice paths,
keyboard completion, grayscale and Motion off. Evidence uses review-* names in Scratch; the builder's evidence stays.
How-to lines now start immediately when their controls appear, through V.how with now:true and V.heard gating.
Repeated negative-time events also use now:true. Read retains the queue helper's priority.

One full review audit finished on port 9961, host 8765: 46 leads, all 89 frames inspected. Forty-five visibility
rows are transparent SVG hit-test artifacts, confirmed visually. The first-Launch welcome skip follows BASELINE 16.
Motion off, control walks, five-click repetition, quick taps and resize stress were clean.
The frames also exposed cropped high target labels on phones. Tiny graphs now use 10 px target text at the line's
baseline; settled phone bounding checks and frames confirm the 80 ft and 330 ft labels fit. The mission 9 record
explains that ground time assumes no catch. Its final phone capture is clear and console-clean.

The final all-size audit precedes these small label/record changes. Desktop re-shoots failed twice with Chrome
timeouts and connection refusal; they were not retried again. The affected phone cases passed. This verification
gap is explicit in codex-review.md. No second full audit was run. All assigned ports were closed and host.html removed.
