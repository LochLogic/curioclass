# Codex report: me-vs-the-counter

All check logs and frame folders below are under `_scratch/me-vs-the-counter/`.

## Built
- Build only in `S:\CurioClass-codex`. No commits, branch changes or polish round.
- Two offline modes: Bounce Lab and Bounciest Ball. Four balls, live taps, physical bounce timing, Slow,
  paper counts, optimal tap matching, three retained tries per ball, prediction and an earned picture graph.
- Kit header/settings, `Curio.voice`, browser speech fallback and synthesized hit/tap sounds. No recordings made.
- Files: readable source, draft metadata at stage built, notes, narration manifest, art, audit states and handoff.
- Bundle: 471.1 KB, below 2 MB. No external resource attributes. Tool `host.html` removed.

## Numbers check
- Scratch `numbers.json` recomputes every displayed count, hit time, rebound height and listed contrast ratio.
- Fall: 0.6060915267 s. Counts: 15, 10, 6, 1. All tabulated hit times round as specified.
- First rebound heights: 1.458, 1.3005, 0.999045 and 0 m. Derived factors: 0.8498366 and 0.7450625;
  simulation uses the exact specified 0.85 and 0.745.
- Bouncy omitted flight: 0.249577741 s. It is below the cutoff but rounds to 0.250 at three decimals;
  the spec's 0.249 is a truncation. Basketball: 0.238647817 s; tennis: 0.207255395 s.
- Contrast: white/header 5.02, ink/paper 15.23, muted/paper 6.25, orange/paper 4.75,
  ink/plate 15.49, teal/plate 5.77, orange/plate 4.83, ink/gold 11.15, white/teal 6.00,
  focus/paper 6.34. Units: contrast ratios to 1.
- The spec's stochastic child-tapping statistic has no complete random-distribution/seed definition.
  It is not presented as a measured claim in the tool. Deterministic lag cases were reproduced directly.

## Feel check
- Played the full four-ball round through actual keyboard input and a late-tap run through the live simulation.
- Best moment: fifteen late taps connect to fifteen sensor hits, making the accelerating final bounces visible.
- Flattest moments: waiting for a paper tally and returning from the chart. The glowing paper stepper, immediate
  hint changes, ball selection feedback and live Drop/Again controls address these; they remain quiet discussion beats.
- `feel-comparison.jpg` places the finished timeline beside Snowy Mail Route. The painted depth, textured
  equipment and ball materials hold up against that bar. Beat Lab was also opened and inspected.
- Existing bundled bar files were used to honor the prohibition on writes to other tools.

## Done when
1. PASS: all four balls at normal speed, Slow and Motion off give 15/10/6/1. Logs in `physics-*-result.json`.
   Maximum observed hit delay was 16.8 ms at normal/calm speed and 7.7 physical ms in Slow, about one rendered frame.
2. PASS: live 0.35 s late bouncy pattern gives 15 pairs, zero rings. Skipping one tap gives 14 pairs,
   one missed hit and no extra. Tested 0, 0.15, 0.25 and 0.35 s lags on all balls (`matching-result.json`).
3. PASS: live trials reach same, more and fewer; a late tennis miss says fast, while an early bouncy miss
   does not (`compare-events.json`). Paper wording is intentionally specific to paper, without nonexistent rings.
4. PASS: paper stepper replaces the current try, clamps at 0 and 30, hides tap marks and uses the paper total.
   `round.js` verifies both limits and `paperLabel`; `paper-max-1366.png` was inspected.
5. PASS: a real four-ball round unlocks the chart only after all four counts. Rows have 15/10/6/1 dots.
   Wrong and correct rows respond. `round-result.json` and actual keyboard chart confirm this.
6. PASS: fourth try replaces oldest; the last three were 2,3,4 before paper edits. A held-click run hears
   the Again event (`input/voice.json`).
7. PASS: 1366 and 680 inspected during and after runs. Ball column sits between counters; the wide timeline
   becomes the dominant results area. Tall-narrow computer stretching was repaired and re-shot at 760 wide.
8. PASS: a mid-run tap increments immediately; Slow yields 0.201 physical s over 0.4 wall s. Rack and Again
   restart immediately. Mode switch stops/discards an unfinished try (`controls-result.json`).
9. PASS: all seven STANDARDS viewports plus 375x812 in a real iframe host. Drop, hand and counters remain visible.
   Main targets are at least 60 px; kit setting controls use its compact 44 px allowance. Final audit below.
10. PASS with narration limitation: held 120 ms clicks at two-second pace, Read with Sound off, empty final
    queue, no repeated how/welcome line, and a complete keyboard-only four-ball round. Console clean.
    Speech scheduling was checked with a timed speech stub; recorded voice and listening review remain pending.

## Wave lessons
- PASS Hint/voice: immediate state hints name the next control; Read uses that hint. Sensor how uses `V.heard`.
- PASS Focus/layout: stable button nodes, no load focus, reserved hint area, intentional focus uses preventScroll.
- PASS Sizes: actual-size relayout, 60 px primary targets, both preview extremes and iframe phone inspected.
- PASS No giveaways: prediction has equal ball cards and unknown counts. Graph appears after four measurements.
- PASS Honest numbers: equal 1.8 m drop stated onscreen; model assumptions and visibility cutoff in teacher notes.
- PASS Standards: students collect, compare, predict and interpret their own measured rows. No family engine applies.
- PASS Motion off: no infinite CSS animations; the physical clock remains unchanged and the hit frame shows the floor.
- PASS Short choices: all four rack balls, prediction choices and chart rows visible together.
- PASS Resize during animation: audit stress clean. A separate held-input run resized live tennis through 760,
  680 and 1366 wide, used Slow/Again, and finished at six hits without exceptions (`resize/result.json`).
- PASS First-tap welcome: no welcomeAfter; each action speaks or begins immediately, so welcomes do not arrive late.
- PASS Unknown as unknown: unmeasured results show question marks, never zero or a promised measured count.
- PASS One look/one meaning: sensor ticks/teal, tap marks/orange, missed/yellow ring, extra/gray ring, with two rows.
- PASS True badge: a star marks only the actual prediction; the graph highlight follows a row answer.
- PASS Reversible hints: mode, ball, chart and run changes replace the hint immediately.
- PASS No copied answer: prediction precedes data; the longest graph row is the lesson's measured evidence.

## Audit leads
- The single full audit finished with 28 leads. Its eight base size checks, Motion off, resize stress,
  console checks, Enter activation and five-click voice checks were clean. Original: `audit/audit.md` in Scratch.
- Fixed all zero-font leads for Slow and Start over in mode, prediction, data-result and chart states:
  icon-only controls now use real-sized icon spans and hidden word spans, retaining accessible names and 60 px targets.
- Fixed data-result 680 fair-caption/Counter-label overlap by spacing the caption and counter plate separately.
- Fixed data-result 680 Counter-label/number overlap by separating the label and screen-number positions.
- Fixed every prediction-star/count overlap, both compact and larger sizes, by placing the star as a corner sticker.
- Fixed quick taps on both mode buttons: selecting the active mode leaves its current narration playing.
- Fixed quick taps on all four rack balls: selecting the same idle ball gives feedback without cutting its instruction.
  Six 120 ms held-click pairs at a 0.7 s gap passed in `quick-checks/`, with no instruction cut.
- Kept practice-hand "nothing changed": the required 110 ms button response and soft tap finish before the audit's
  settled snapshot. Practice must not change the recorded count. Live tap recording is separately verified.
- Kept empty Start over "nothing changed": clearing an already empty mode is idempotent and still gives a tone.
- Kept seven skipped-first-welcome flags (four rack balls, Drop, Again, Slow): STANDARDS says an action with its own
  line skips the welcome unmarked. Bringing it back late would violate that rule. Mode entry remains available.
- Kept the quick-Drop tap-along cut: restarting immediately and dropping that line at the first hit are explicit
  spec requirements. The action hint remains available to Read, and a picked ball can teach the line before Drop.
- Targeted follow-up probes reused the audit's layout checker at 680, 800, 1000 and 1366 wide plus the 375 iframe.
  The confirmed overlap/tiny-text leads are gone. No full audit rerun was made after these focused repairs.

## Frames looked at
- `bars/`: Snowy Mail Route and Beat Lab at 1366x768.
- `early/`, `layout/`: first playable gym, result and compact question card. Initial compact header overflow repaired.
- `sizes/`: seven sizes, grayscale, Motion off, mid-drop 680, data result 680 and paper maximum 1366.
- `phone-early/`, `phone-latest/`, `phone-final/`: 375x812 defaults, prediction, paper results and chart.
- `checks/`: normal/slow/calm physics endpoints, full late-tap match, finished graph and interruption check.
- `targeted/`: portrait proportions, count result, compact chart, calm floor and completed late-tap timeline.
- `input/`: voice end, keyboard chart and the test-driver failure frame. Enter character dispatch was fixed in Scratch.
- `post/`, `audit-repairs/`, `read-race/`, `resize/`, `quick-checks/` and the final lead-probe frames were inspected.
  Probe-template debugging frames are included in the last QA sheets; that helper error was corrected in Scratch.
- Art sheet, both finished replacement stands, and the side-by-side feel comparison inspected.
- All 60 audit PNGs inspected on eight QA sheets, with compact paper/portrait/prediction frames opened separately.

## Art made
- Nine new images, 222.8 KB finished art; 262.4 KB including the preserved old gym-wall image.
- Gym, pad, two stands, rubber ball, basketball, tennis ball, beanbag and computer. Full prompts in `art/prompts.json`.
- Built-in OpenAI image generation, raw images copied into `art/raw`, each finished through `art.py --rekey`.
- Both stands redrawn: removed a painted-in yellow ball and an unrelated gauge, then matched the open/closed pair.

## Art still to paint
- `tap-hand`, marked people:true. The prescribed code-drawn silhouette is used; no people or body parts were generated.
- Open-question decision: retain the spec's leaning toward a reviewed painted hand, rather than making the icon permanent.

## Engine changes wanted
None.

## Left open
- Easy-coach recordings and listening review. Browser speech is the fallback; generated sounds were tested muted.
- A real kindergarten group has not tried the tool. Three large paper totals can make the mini results strip dense.
- Tiny stand cutout edge specks remain; no shared engine or painter service was changed.
- The full size sweep and physics run preceded final focused layout/voice repairs; only affected cases were rechecked.
- The full audit ran once to completion. Focused layout, Read, cable and repeat-tap repairs were checked separately; no second full audit.
