# Codex report: launch-pad

## Built

Build only. Launch explorer and nine ordered Missions, four algebra methods, exact expression parser, contextual
root choice, real-time flight, event clock holds, local mission records and Clear missions. Uses the kit starter,
Curio.voice, theme-912 and the unchanged Plane family engine. No commits or polish round.

## Numbers check

PASS. Independently recomputed in check_math.py, evidence numbers.json. All nine tidied equations, roots,
discriminants and peaks match the spec. Longest flight 8.2569390943 s; maximum peak 325 ft. Standard gravity
32.1740485564 ft/s² versus the model's 32. Contrast: coral on panel 6.751:1, section 6.397:1, graph 7.142:1;
brand-ink on coral 7.102:1. No spec arithmetic corrections were needed.

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

Scratch: both bar frames, art-contact.png, first and second playable frames, all 14 size-frames,
phone-frames and phone-fixed, special-frames, keyboard.png, functional-frames and feel-comparison.png.
All 73 audit PNGs reviewed in audit-contacts, with key compact, phone and completed-flight frames also opened
at full size. All six repair-frames, repair-phone-frames, and four final-target-frames were opened.
Screenshots and all profiles stay in Scratch.

## Art made

Six generated paintings, no redraws: field-dusk, launcher, foam-ball, drone, brick-texture, balcony. 92,076 bytes
of new WebP art (89.9 KiB); 104,840 bytes including the preserved older unused field. Built-in image tool used,
full prompt set in art/prompts.json, raw selections in art/raw, finished art/<name>.webp. Final bundle: 228174 bytes (222.8 KiB), under 2 MB.

## Art still to paint

None. No people were generated. Recorded narration remains absent as directed; browser speech is the fallback.

## Engine changes wanted

None for the kit or family engine. Optional helper request: add digits, Home, End and Shift+Tab to drive.py's key
map and audit_tool.py's drive_keys. The state audit seeds typed box values through JS because its map lacks digits;
every transition is a real held click, and slider limits use real drags. A separate real keyboard run verified typing.

## Left open

- Cold review and live classroom use have not happened. Browser speech was log-tested, not listening-reviewed.
- The full audit predates the small input-label, axis-margin and selected-mode repairs. Targeted checks passed.
- All task Chrome/server processes are closed and host.html is removed.
- The equipment below the ball's initial height is symbolic; its physical size is not another height term.
- The 375 px graph and derivation are compact. The workbench keeps its controls visible and usable.
- The spec's voice question is resolved toward big-sister; see handoff.md.
- The report was held until all build checks finished because the user explicitly required stopping when it is written.
