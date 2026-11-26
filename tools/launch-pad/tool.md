# Launch Pad: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: launch-pad

#### Built

Build only. Launch explorer and nine ordered Missions, four algebra methods, exact expression parser, contextual
root choice, real-time flight, event clock holds, local mission records and Clear missions. Uses the kit starter,
Curio.voice, theme-912 and the unchanged Plane family engine. No commits or polish round.

#### Numbers check

PASS. Independently recomputed in check_math.py, evidence numbers.json. All nine tidied equations, roots,
discriminants and peaks match the spec. Longest flight 8.2569390943 s; maximum peak 325 ft. Standard gravity
32.1740485564 ft/s² versus the model's 32. Contrast: coral on panel 6.751:1, section 6.397:1, graph 7.142:1;
brand-ink on coral 7.102:1. No spec arithmetic corrections were needed.

#### Feel check

Drove the complete nine-mission sequence and all four solving methods, then a keyboard-only mission. The best
moment is mission 3: the clock holds at 1.00 s and 3.00 s, and both heights are 48 ft, with the ball and curve
showing the two parts of one flight. The balcony catch then makes choosing a root matter.

The two flattest early moments were a form that clipped at small sizes and a static, empty flight display.
Changed the compact workbench to put Check beside its inputs, moved notes beside the graph, and gave Launch a
live progressive trace, painted ball, coral trail, event ring and exact clock hold. Drone blink and bob add quiet life.
Later rounds change the algebra: double root, impossible height, drop, completed square, irrational roots and
downward-only catch. The flight is the payoff rather than a score or confetti.

Opened bundled Snowy Mail Route and Beat Lab before implementation. Looked at feel-comparison.png, with this
tool's first flight beside Beat Lab. The range has rich painted depth and material details; the mathematical plane
stays clear and precise. This was a build feel check, not a cold review or a 20-minute classroom trial.

#### Done when

1. PASS: mission 2 Factor p=5, q=-1; -1 rejected with before-launch reason; 5 accepted; event at 5.00 s, h=0.
2. PASS: mission 3 accepts reversed 3,1; exact events at 1 and 3, both h=48.
3. PASS: mission 4 Formula discriminant 0 and one pass; mission 5 discriminant -4, complex pair accepted;
   the flight event peaks at 2 s, 64 ft, below the drone.
4. PASS: mission 7 Complete the square k=3/2, m=41/16; radical roots and (6+sqrt(41))/4 pass; 3.10 passes.
5. PASS: mission 8 Factor gives no-pair advice; Formula exact roots pass; 2.64 accepted, 2.6 rejected.
6. PASS: mission 9 rejects 0.8486 as upward; 2.6514 accepted; exact flight event h=40. Painted rail aligns to 40.
7. PASS: explorer v=64, h0=0 gives H=48 at 1 and 3; H=80 gives never.
8. PASS: visually inspected 1366x768 and 1000x625; the plane is the largest stage region beside the scene.
9. PASS: live restart returns clock to zero immediately; slider change cancels the old flight and redraws.
10. PASS: nine saved records survive reload; Clear removes them and a fresh reload stays empty. Motion off
    draws the full path with the same clock. Sizes, controls, keyboard, console and narration checks pass
    within the targeted-recheck limits below. No external request attributes exist in the bundle.

functional-results.json has 50 passing assertions. Event times use exact roots after an accepted rounded answer.

#### Wave lessons

- Hint and voice: PASS, current hints name controls and update synchronously. Read uses the hint. Curio.voice
  separates how-to from repeatable events, checks validity and uses V.heard. Action handlers do not wait on speech.
- Focus and layout: PASS, no focus on load; keyboard mission retained focus into p, answer and Launch. Deliberate
  focus uses preventScroll. Stable method and action buttons do not rebuild under the pointer.
- Sizes: PASS, all seven standalone sizes plus 375x812 in an iframe inspected in both modes. Compact and phone
  work areas were repaired before the audit. All controls use at least 44 px targets.
- No giveaways: PASS, mission curve, peaks, flight times and crossing markers stay hidden until solving/launch.
  A correct method reveals roots only after the student's algebra checks. Launch is intentionally a checker.
- Honest numbers: PASS, no air and g=32 ft/s² appear on screen. Exact clock times and model heights agree.
- Standards: PASS, missions exercise factoring, square roots, completing a square, discriminants and complex roots;
  completing a square also displays its general identity leading to the formula. Family engine remains unchanged.
- Motion off: PASS, path appears immediately; clock and event-hold timing stay the same. Infinite blink/bob loops stop.
- Short choices: PASS, all four methods stay visible, with a native select for the nine missions.
- Resize mid-animation: PASS, full audit stress was clean: no exceptions and nothing left disabled.
  Flight geometry rebuilds from the current exact t without cancelling it.
- Late welcome: PASS, no welcomeAfter. Welcomes have current-state validity checks and are dropped on mode changes.
- Unknown as unknown: PASS, the hidden-flight message marks the unsolved graph explicitly.
- One look, one meaning: PASS, solid blue flight and dashed lavender height line, plus labeled ring events.
- Truthful badges: PASS, mission checks appear only after a completed flight, not after entering an answer.
- Hint changes back: PASS, modes and mission changes set the next hint immediately; slider changes restore launch guidance.
- No copying words: PASS, before solving there are no answer choices or visible roots to match to the question.

#### Audit leads

One full audit completed, 37 leads, evidence audit/audit.md. Original report preserved. No second full audit.

- FIXED, 7 unnamed-field leads: p, q, k, m, a, b, c now have descriptive aria-labels. Targeted compact and
  phone checks confirm every active field has a name; wrapped visual labels remain in place.
- FIXED, 7 repeated axis-overlap leads: default phone, mode Missions (680 and phone), Factor (680), Square
  (680), Formula (680), and upper speed (phone) all shared the tiny axis margin. Increased its bottom margin
  and centered time (s). Targeted 680 and 375 checks found zero overlaps with numeric ticks; frames inspected.
- FIXED, 2 quick-tap welcome cuts: tapping the selected mode no longer calls hush or resets that mode.
  Real held taps 0.7 s apart on each mode produced a spoken welcome and zero cuts.
- NOT A VISUAL DEFECT, 20 visibility rows: each of mode Missions, Factor, Square and Formula lists the same
  five hit-test categories: tick 40, tick 60, tick 20, graph-lock block and its bold heading. The transparent Plane
  hit area is returned by elementFromPoint underneath those visibly drawn texts. Full-size compact/phone frames
  and contact sheets confirm no covering surface or clipped text. No engine change was made.
- INTENTIONAL, 1 first-Launch welcome lead: the spec says wLaunch is stale on the first Launch. A first tap
  launches immediately, with tone, ball, curve and clock; its stale welcome is not played late.

Full audit: all standalone default sizes clean, phone default only the repaired axis lead; Motion off clean;
resize stress clean, no exceptions or controls left disabled; held-click walk console clean; five-click 2 s
voice repetitions clean. Repairs received targeted rechecks only, not another full audit or size sweep.

#### Frames looked at

Scratch: both bar frames, art-contact.png, first and second playable frames, all 14 size-frames,
phone-frames and phone-fixed, special-frames, keyboard.png, functional-frames and feel-comparison.png.
All 73 audit PNGs reviewed in audit-contacts, with key compact, phone and completed-flight frames also opened
at full size. All six repair-frames, repair-phone-frames, and four final-target-frames were opened.
Screenshots and all profiles stay in Scratch.

#### Art made

Six generated paintings, no redraws: field-dusk, launcher, foam-ball, drone, brick-texture, balcony. 92,076 bytes
of new WebP art (89.9 KiB); 104,840 bytes including the preserved older unused field. Built-in image tool used,
full prompt set in art/prompts.json, raw selections in art/raw, finished art/<name>.webp. Final bundle: 228174 bytes (222.8 KiB), under 2 MB.

#### Art still to paint

None. No people were generated. Recorded narration remains absent as directed; browser speech is the fallback.

#### Engine changes wanted

None for the kit or family engine. Optional helper request: add digits, Home, End and Shift+Tab to drive.py's key
map and audit_tool.py's drive_keys. The state audit seeds typed box values through JS because its map lacks digits;
every transition is a real held click, and slider limits use real drags. A separate real keyboard run verified typing.

#### Left open

- Cold review and live classroom use have not happened. Browser speech was log-tested, not listening-reviewed.
- The full audit predates the small input-label, axis-margin and selected-mode repairs. Targeted checks passed.
- All task Chrome/server processes are closed and host.html is removed.
- The equipment below the ball's initial height is symbolic; its physical size is not another height term.
- The 375 px graph and derivation are compact. The workbench keeps its controls visible and usable.
- The spec's voice question is resolved toward big-sister; see handoff.md.
- The report was held until all build checks finished because the user explicitly required stopping when it is written.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: launch-pad

#### Played

Cold Grade 9 play covered Launch and all nine mission cards before reading codex-report.md, handoff.md, notes.md or src.html.
Eight cold flights verified; mission 5 correctly refused my trial answer "never" and requested complex notation.
The focused checks then verified the complex flight too. Best moment: one ball proves both 48-foot crossings.
Projected and compact views kept the graph prominent; the original generic completion was the flattest payoff.

#### Findings fixed

- blocker (general), Missions / real(): -2^2 evaluated as +4 and passed Factor and the landing check. Corrected sign/power precedence.
- should fix (general), Complete the square: formula derivation was display-only. Mission 7 now checks three symbolic denominators.
- should fix (general), Formula voice: count instructions played over coefficient boxes. Added separate coefficient and discriminant lines.
- should fix (general), how(): the 2 s walk dropped tidy, root and answer instructions. Current-step instructions now start immediately, once.
- should fix (general), negative events: five submissions produced four spoken events. New events now take over; the rerun heard five.
- should fix (general), Clear missions: an active flight could re-save progress. Clearing now cancels and resets the active mission.
- should fix (general), balcony art: keyed residue and an absent catcher weakened the catch. Repainted it, marked people:true, aligned its rail.
- should fix (family:graphing), phone: high H labels were cropped. Adjusted tiny-label type/placement; 80 ft and 330 ft now fit.
- should fix (general), sources: corrected the dead OpenStax section and invalid NIST URL in notes and tool metadata; left the spec intact.
- polish (general), completion: retained the method, direction, exact event clock and model height as the student's earned record.
- polish (general), catch: the record now explains that the displayed ground time assumes no catch.
- polish (general), compact derivation: shortened and repositioned the explanation so it clears the height line and axes.

#### Findings left

No known unfixed blocker. The final desktop re-shoot gap is recorded under Left open.
Nit: native mission selection truncates long names in narrow layouts; the complete setup remains visible.

#### Break it

105 assertions passed in review-checks-fixed.json, using student-path controls and field submissions.

- Height gate: empty/wrong heights and repeated Check presses cannot advance. All four blank method paths remain unproved.
- Factor: blank/invalid pairs, p=q=0 and the -2^2 exploit fail; correct expansion succeeds. No score is banked at answer-ready.
- Square root: a negative magnitude fails; both signs are shown after valid work, and a negative event time is rejected.
- Completing the square: wrong k/m, missing roots and easy numeric derivation guesses fail; equivalent symbolic denominators pass.
- Formula: wrong coefficients, each wrong real-root count, single/missing roots and a lone complex root fail before Launch unlocks.
- Mission interpretation: launch-time zero, extra roots, one of two crossings, negative time and the upward catch fail.
- Mission 3 accepts reversed 3,1 and measures both at 48 ft; mission 5 requires 2 ± i and verifies a 64 ft peak below 80 ft.
- Mission 8 rejects 2.6 and accepts 2.64; mission 7 accepts 3.10. Accepted rounded times replay at the exact root, as the notes explain.
- Progress: interrupted/restarted flights cannot bank completion; Clear during flight stays clear after the old finish time.
- Explorer: slider extremes and sweeping are unscored. Zero launch, the 325 ft maximum peak and unreachable heights remain consistent.

Explorer deliberately supplies roots as the spec's checker; mission verification is supported practice, not evidence of unaided mastery.

#### Voice walk

Held clicks: 0.12 s down, 2 s apart, default launch settings and Sound on. Logs are voice-*-result.json.
Main: default Launch, Missions, Write it, Tidy, Factor, Check work, Check answer, Launch.
Heard in order: wLaunch, wMissions, tidy, method, answer, launchNow, done, once each.
Formula side: wMissions, tidy, method, coeff, disc, root, answer, launchNow, done.
Complete-square side: wMissions, tidy, method, derive, root, answer, launchNow.

| Line group | Kind | Expected | Heard |
| --- | --- | --- | --- |
| Main welcomes and applicable how-to lines | welcome/how | once each | once each |
| Coefficients, discriminant, derivation, roots | how | once on applicable path | once |
| Negative-time response | event | five | five |
| Completion on main and Formula walks | event | one per completed flight | one |

New steps cut instructions whose controls have changed. Read retains priority; rapid switches, Read during speech and Sound-off Read were checked.
The final manifest matches all 14 fixed automatic narration lines. Recorded clips are absent; browser speech is the fallback.

#### Facts checked

- Projectile model, feet/seconds and contextual roots: [OpenStax Elementary Algebra 2e 10.4](https://openstax.org/books/elementary-algebra-2e/pages/10-4-solve-applications-modeled-by-quadratic-equations).
- Peak/vertex interpretation: [OpenStax 10.5](https://openstax.org/books/elementary-algebra-2e/pages/10-5-graphing-quadratic-equations-in-two-variables).
- Completing the square, formula derivation, discriminant and complex solutions: [OpenStax 9.2](https://openstax.org/books/intermediate-algebra-2e/pages/9-2-solve-quadratic-equations-by-completing-the-square) and [9.3](https://openstax.org/books/intermediate-algebra-2e/pages/9-3-solve-quadratic-equations-using-the-quadratic-formula).
- A-REI.B.4a/4b coverage checked against [Common Core HSA-REI](https://www.thecorestandards.org/Math/Content/HSA/REI/).

Independent substitution into that model, with the spec's assigned parameters, is saved in review-numbers.json:

| Mission | Recomputed roots and event |
| --- | --- |
| 1 | 0, 4; return at 4 s |
| 2 | −1, 5; land at 5 s |
| 3 | 1, 3; both at 48 ft |
| 4 | repeated 2; peak 64 ft |
| 5 | 2 ± i; no real time, peak 64 < 80 ft |
| 6 | ±3; keep 3 s |
| 7 | (t − 3/2)² = 41/16; (6 ± √41)/4; landing 3.100781 s |
| 8 | (5 ± √31)/4; landing 2.641941 s |
| 9 | (7 ± √13)/4; ascending 0.848612, catch 2.651388 s |

- Standard gravity: 9.80665 m/s², or 32.1740485564 ft/s², from [NIST Appendix B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8). The screen explicitly uses the no-air, 32 ft/s² model.
- Extreme flight: 8.256939 s, peak 325 ft, independently recomputed. Each root substitution residual was below 1e-10.
- Contrast, using [W3C WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html): coral/panel 6.75:1, coral/section 6.40:1, button ink/coral 7.10:1, new record text at least 9.10:1.

#### Sensitivity

No cultural, religious, hard-history or body-teaching content. A fresh art reviewer should inspect the new teenage catcher's hands, glove pose, ordinary clothing and small-size crop. The figure represents one friend, with no group claim.

#### Flattest moment left

Entering a, b and c is the quietest remaining beat. Kept because signed-coefficient identification is part of the specified method.

#### Graphics

All six used paintings were inspected individually and in scene; balcony was redrawn with built-in imagegen and free art.py rekeying.
Raw replacement: art/raw/balcony.png; finished: art/balcony.webp; full prompt: art/prompts.json. Used art totals 101.4 KiB.
Kept the painted field, textured equipment, drone life, progressive trace and instrument styling. Compared with the existing Beat Lab and Snowy Mail Route reference frames.
Bundle: 247428 bytes (241.6 KiB). All art tokens resolve; no missing painting remains. The legacy lp-field-dusk image stays unused.

#### Audit

One full audit finished, exit 0: _scratch/launch-pad/review-audit/audit.md. All 89 audit frames were opened in 23 contact sheets, with compact/phone leads also opened full size.
Disposition: 45 visibility rows are transparent SVG hit-test artifacts, visually confirmed; the first-Launch welcome skip follows BASELINE rule 16 and the spec.
The frames separately exposed the cropped phone height label, now repaired. Final phone captures show both labels inside the graph and the catch record unclipped, with no console errors.
Default sizes, listed work states, Motion off, held controls, five-click repetition, quick taps and resize stress passed within the audit's mechanical scope.
Keyboard-only completion retained focus on Launch; grayscale kept solid/dashed and direction/word distinctions. Notes open with the required three sections.
No second full audit was run. The final tiny-label and catch-note changes received phone rechecks; their desktop recheck failed as recorded below.

#### Left open

- Desktop re-shoots after the final small label/record changes failed twice with Chrome timeout/connection refusal. Per the command retry rule, stopped that check. Phone rechecks passed; the earlier full all-size audit is preserved.
- Browser speech was log-tested, not listened to. Keep the spec's big-sister choice for future recording.
- Protocol deviation: initial reads and some short metadata operations lacked explicit command timeouts. Bundle, drive batches and the 40-minute audit were bounded.
- Draft stayed in Scratch until completion to honor the requested stop as soon as codex-review.md is written.
- Folder confirmed S:\CurioClass-codex; writes stayed in the tool and its Scratch folder. No git commits. All assigned ports were closed and host.html removed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Launch Pad handoff

Build only, 2026-11-03. No commits, branch operations or polish round.

#### Layout and code

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

#### Art and voice

Six images were made with the built-in image tool during this build. Full prompts are in art/prompts.json; selected
raw PNGs are in art/raw and their free rekeyed WebP versions are bundled. The cold review replaced the balcony with a teenage catcher; that asset is marked people: true. The older lp-field-dusk
asset was preserved and is not used. The ruler measures the ball at the tube mouth. The launcher and base are
symbolic equipment below that reference; their own physical dimensions are not extra terms in the height equation.
The balcony rail is aligned to 40 ft using the inspected painting's rail position, and its glove aligns to the ball.

The narration queue uses the specified fixed lines and distinct repeatable event lines. Read uses the live hint.
No audio was recorded, as directed. Browser speech is the fallback, so the intended voice is not an embedded recording.

#### Open question resolved

Use big-sister with the science-fair launch style line. This is the option the spec leans toward and avoids sharing
firm-captain with the more closely related Flight Planner. No other spec open questions were listed.

#### Verification pointers

All build evidence is in `_scratch/launch-pad/`. `numbers.json` independently recomputes the nine missions, gravity,
extreme flight and four contrast ratios. `functional-results.json` records 50 passing assertions and exact event
heights. `keyboard-results.json` records a complete mission through real keyboard input with focus retained.
`size-frames`, `phone-fixed`, `special-frames` and the final audit folder contain visual evidence.

The stock drive key map cannot type digits, and the audit key map also lacks Home and End. Audit states therefore
seed text-box values through JS only, then use real held clicks for every transition and real drags for slider limits.
The separate keyboard script uses real CDP text input and key events without changing the shared driver or engine.
The original phone host's favicon 404 was a host-only issue; the bounded scratch host helper suppresses it with a
data icon and removes host.html after its shots. The delivered tool also has a data icon and no external requests.

#### Engine changes wanted

None for kit/graphing.js or the shared kit. Optional test-helper improvement: scripts/drive.py's key map and
scripts/audit_tool.py's drive_keys should support digits, Home, End and Shift+Tab, so typed state paths need no text
seeding. This is outside the authorized write scope and was not changed.

#### Next review

The cold reviewer should judge algebra explanations, the model's symbolic equipment, compact derivation readability,
browser narration timing, and whether the finished mission progression feels satisfying across a full class period.
This build includes a full nine-mission functional run, not a live classroom test or a cold review.


#### Final build audit and targeted repairs

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

#### Cold review changes, 2026-11-07

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

#### Sensitivity

No culture, religion, hard history or body teaching. A newly illustrated teenage catcher has brown skin,
ordinary clothing and natural proportions. The fresh visual reviewer should check the small-size crop,
hands, glove pose and respectful depiction. No identity is presented as representative of a whole group.

#### Cold review verification and audit

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

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
