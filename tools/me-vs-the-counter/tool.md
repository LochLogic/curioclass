# Me vs the Counter: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: me-vs-the-counter

All check logs and frame folders below are under `_scratch/me-vs-the-counter/`.

#### Built
- Build only in `S:\CurioClass-codex`. No commits, branch changes or polish round.
- Two offline modes: Bounce Lab and Bounciest Ball. Four balls, live taps, physical bounce timing, Slow,
  paper counts, optimal tap matching, three retained tries per ball, prediction and an earned picture graph.
- Kit header/settings, `Curio.voice`, browser speech fallback and synthesized hit/tap sounds. No recordings made.
- Files: readable source, draft metadata at stage built, notes, narration manifest, art, audit states and handoff.
- Bundle: 471.1 KB, below 2 MB. No external resource attributes. Tool `host.html` removed.

#### Numbers check
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

#### Feel check
- Played the full four-ball round through actual keyboard input and a late-tap run through the live simulation.
- Best moment: fifteen late taps connect to fifteen sensor hits, making the accelerating final bounces visible.
- Flattest moments: waiting for a paper tally and returning from the chart. The glowing paper stepper, immediate
  hint changes, ball selection feedback and live Drop/Again controls address these; they remain quiet discussion beats.
- `feel-comparison.jpg` places the finished timeline beside Snowy Mail Route. The painted depth, textured
  equipment and ball materials hold up against that bar. Beat Lab was also opened and inspected.
- Existing bundled bar files were used to honor the prohibition on writes to other tools.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
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

#### Art made
- Nine new images, 222.8 KB finished art; 262.4 KB including the preserved old gym-wall image.
- Gym, pad, two stands, rubber ball, basketball, tennis ball, beanbag and computer. Full prompts in `art/prompts.json`.
- Built-in OpenAI image generation, raw images copied into `art/raw`, each finished through `art.py --rekey`.
- Both stands redrawn: removed a painted-in yellow ball and an unrelated gauge, then matched the open/closed pair.

#### Art still to paint
- `tap-hand`, marked people:true. The prescribed code-drawn silhouette is used; no people or body parts were generated.
- Open-question decision: retain the spec's leaning toward a reviewed painted hand, rather than making the icon permanent.

#### Engine changes wanted
None.

#### Left open
- Easy-coach recordings and listening review. Browser speech is the fallback; generated sounds were tested muted.
- A real kindergarten group has not tried the tool. Three large paper totals can make the mini results strip dense.
- Tiny stand cutout edge specks remain; no shared engine or painter service was changed.
- The full size sweep and physics run preceded final focused layout/voice repairs; only affected cases were rechecked.
- The full audit ran once to completion. Focused layout, Read, cable and repeat-tap repairs were checked separately; no second full audit.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: me-vs-the-counter

#### Played

Cold kindergarten/projector walk before builder notes or source; later continued through the chart and a keyboard-only round.
The accelerating bounces and paired timeline are strong. The original equal-total praise was misleading.
#### Findings fixed

- Blocker, general, compare/src.html: 15 rapid taps earned counting praise with only 2 matched hits.
  Praise now requires complete tap/hit matching; equal but mistimed totals get a truthful circles explanation.
- Blocker, general, paper/src.html: copying the visible sensor total earned the same praise. Equality is now neutral.
- Blocker, general, chart/src.html: trying every row earned first-choice praise. Corrections now explain the longest row,
  remember the first choice and omit the success chime. No score or saved best exists.
- Should fix, general, narration: sensor teaching was lost behind optional fast-hit speech; moved ahead of it,
  added it after the no-taps prompt, and put tap-along before ball-pick speech. Main-path logs confirm it is heard.
- Should fix, general, art: missing painted hand replaced the flat silhouette on both controls; marked people:true.
- Should fix, general, notes/metadata: corrected current FIBA attribution while preserving the mandated model.
- Should fix, general, compact results: three large tries crowded the prediction star. Anchor the table sticker
  over its ball picture, away from the count text; re-shot at 375, 680 and 1366 widths.
- Polish, general, chart: retain the student's prediction sticker beside the measured row; wrong rows gain a dashed cue.
#### Findings left

No confirmed blocker or should-fix remains in the reviewed implementation. The audit's phone host could not expose
its iframe context; separate 375 px checks provide the visual and interaction evidence, not a mechanical audit PASS.
#### Break it

- Rapid burst: real 120 ms held taps, 15 taps in about 2.5 s. Before: "Nice counting"; after: timing explanation,
  2 pairs, 13 missed and 13 extra. No counting praise or stored best.
- Paper copy/sweep: beanbag total copied with plus. After: paperSame, no skill praise. Both bounds clamp at 0 and 30;
  replacing a timed count hides the tap row instead of inventing times.
- Chart: four measured counts required; unmeasured balls show ?. Trying beanbag, tennis, basketball, then bouncy
  now ends with corrected, never correct. All four evidence rows stay available; the graph is an unscored discussion.
- Repeated tennis measurements do not substitute for the unmeasured bouncy ball: the cold walk's chart stayed locked.
- Legitimate lag: live scheduled taps 0.35 s late give 15 pairs, no rings. One skipped tap gives 14 pairs,
  exactly one yellow ring, no extra. Pure matching also passes 0, 0.15, 0.25 and 0.35 s lag for every ball.
- Retention: fourth completed beanbag try leaves counts 2,3,4. Interrupted drops add no row.
- All four counts stay 15,10,6,1 at normal/Slow speed with Motion on/off. Maximum hit delays were
  16.50 ms normal, 7.80 ms Slow, 15.85 ms calm and 8.11 ms calm/Slow, within one rendered frame.
- Live controls: tap increments immediately; Slow advances about 0.19 model seconds in 0.4 wall seconds;
  rack selection restarts at zero, Again restarts, mode switch stops without saving unfinished work.
#### Voice walk

Real browser speech, Sound on, default speed, 120 ms holds, 2 s between ordinary actions; runs finish before results.
Path: practice hand, pick bouncy, Drop and count, paper edit, Bounciest Ball, predict tennis, explicitly pick/drop
all four balls, Show the chart, wrong row, longest row. `_scratch/me-vs-the-counter/review-voice/final.json`.
Heard order: w-lab, tap-along, bouncy, fewer, sensor, paperFewer, w-ball, drop-all, pickedBouncy, bouncy, paper,
pickedBasket, basket, pickedTennis, tennis, pickedBeanbag, beanbag, ready, pick-row, wrong, corrected.
Welcomes/selection lines can be cut by the next action; the sensor explanation completed. No stale result follows a new drop.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| tap-along, sensor | how | 1 each | 1 each |
| beanbag, same | result over 5 drops | 5 each | 5 each |
| again | result over 4 Again drops | 4 | 4 |

Read works with Sound off and after a mode change. All 38 fixed lines match the manifest; no recordings were made.
#### Facts checked

- Ideal fall, g=9.8 and the height/time relation: [OpenStax 2.7](https://openstax.org/books/college-physics-2e/pages/2-7-falling-objects).
  Independent fall time 0.6060915267 s; counts 15,10,6,1; all listed hit times reproduced.
- Bounce energy decreases: [OpenStax 8.5](https://openstax.org/books/college-physics-2e/pages/8-5-inelastic-collisions-in-one-dimension).
  Model factors 0.90,0.85,0.745,0, constant-factor extrapolation, 0.25 s cutoff and matching window are spec choices.
  First heights 1.458,1.3005,0.999045,0 m. The omitted bouncy flight is 0.249577741 s, not rounded 0.249 s.
- Basketball: [FIBA Basketball Equipment 2024](https://refereeing.fiba.basketball/en/rule-zone/basketball-equipment),
  section 2.4: 1.8 m drop, 1.035 to 1.085 m underside rebound. Spec's older 1.2 to 1.4 m range is not current.
- Tennis Type 2: [ITF 2026 Appendix I](https://www.itftennis.com/media/7221/2026-rules-of-tennis-english.pdf), 135 to 147 cm;
  [ITF 2026 Technical Booklet](https://www.itftennis.com/media/15639/2026-technical-booklet.pdf), 254 cm rigid-block test.
- Collect, display and use measured data: [CSTA](https://csteachers.org/pk12standards/) plus the repository's
  EK-DAT-DC-08, EK-DAT-DI-09, EK-DAT-IM-10 module identifiers. Activities collect taps/sensor counts, compare formats,
  predict, then use the longest measured row. Notes open with the three required sections and workable home activities.
- Simulation-only claims (sensor counts every contact; Slow preserves counts; same-height fair comparison; beanbag
  has one initial contact) verified in source and live runs. Notes explicitly distinguish this from real measurements.
#### Sensitivity

No culture, religion or hard history. One people image, tap-hand, is marked people:true. Final people-art review should
check five-finger anatomy, child age impression, warm brown skin and respectful representation. No stereotype found.
#### Flattest moment left

Waiting for a paper tally is still deliberately quiet. The chart payoff now reconnects the class's prediction
with its measured row; correcting a guess invites comparison rather than unearned praise.
#### Graphics

Kept the painted gym, textured equipment, balls, lighting, movement and timeline. Added tap-hand through imagegen,
then art.py --rekey with despill/holes; checked final cutout and its actual 65 px button use, plus all other images.
Every art token has a finished asset. Whole set is coherent; old unused gym-wall retained. Bundle about 498 KB.
Inspected all STANDARDS widths, 375 iframe, grayscale, calm, prediction/result/chart, paper extremes and keyboard focus.
Viewed current Snowy Mail Route and Beat Lab beside tool frames in review-sheets/targets-0.jpg; this scene is not plainer.
WCAG ratios recomputed: white/header 5.02, ink/paper 15.23, muted/paper 6.25, orange/paper 4.75,
teal/plate 5.77, focus/paper 6.34. Pictures, labels, side and ring shapes supplement color.
#### Audit

Single final audit completed within its 40 minute limit, exit 0, with 12 leads. No second audit.
Evidence: `_scratch/me-vs-the-counter/review-audit/audit.md`; all 54 audit PNGs inspected on nine contact sheets.
Desktop sizes/states, targets, focus, Motion off, five-click voice checks and resize stress are clean.

- Seven skipped-first-welcome leads: allowed by BASELINE rule 16; the action's own instruction wins, hint/Read remain.
- Quick Drop cuts tap-along: explicitly stale at the first hit per spec. Ball selection can teach it before Drop;
  the main-path and repeated completed-drop logs confirm instruction availability. Never delay the drop to finish speech.
- Two "nothing changed" leads: source gives practice unrecorded 110 ms feedback; empty Reset is idempotent.
  Normal/audit walks are live. The very-low-delay feedback capture failed twice, so that probe remains inconclusive.
- Two phone-host leads: audit iframe context lookup failed, so its missing-hint message is not evidence of a missing
  tool hint. Dedicated drive.py host checks at 375 px cover default/Read, prediction, settled chart, paper maximum
  and three large tries for every ball. No shared audit code was changed.
  This last extreme confirmed the table-sticker overlap; the single CSS repair was checked at 375, 680 and 1366.
All review Chrome processes and the host are closed; assigned ports are closed and host.html is absent.
#### Left open

- Cold-order limitation: the initial walk omitted bouncy after predicting tennis, so the chart correctly stayed locked.
  Builder notes were opened before the missing measurement and chart continuation. Initial play observations were cold.
- The first read-only documentation commands had no hard process deadline; subsequent commands used bounded wrappers.
- Spec-owner decision: update the basketball model or preserve its mandated e=.85 and ten hits. No spec change made.
- Easy-coach recordings and audible listening review remain production work; this pass used real browser speech logs,
  not a speech stub. A live kindergarten group has not tested it.
- Physics batch initially exceeded the driver's 60 s evaluation limit; smaller normal/Slow/calm cases all pass.
- Keyboard browser startup was retried once with an isolated profile and completed. Phone host favicon 404 was
  external to the iframe tool; the host was removed. No tool console errors were observed in the completed checks.
- The post-audit low-delay practice-feedback capture timed out twice and lost Chrome before the Reset fixture.
  Stopped that probe. Neither result is claimed as a passed visual check; normal control and audit walks were clean.
- Edits confined to the named tool and Scratch; no commits, shared engine changes, registrations or publishing.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: Me vs the Counter

Build only, 2026-11-03. No commits. No polish round.

#### Structure

`src.html` starts from the kit starter. The kit supplies header settings, sound, browser narration and the voice queue.
CSS re-lays the gym and equipment at actual screen dimensions. It does not scale a fixed scene. The controls precede
the scene in the DOM; explicit tab order follows rack, Drop, hand, Again, Slow, paper stepper, chart rows and chart.
The stand's rendered width and left position are calculated from the column height so its claw follows the ball.
The ball's initial center is 14.5 percent down that column, matching the painted claw. `drawCable` reads the mat
and computer bounds on a relayout rather than keeping a fixed cable endpoint. The fair-test caption sits above
the stand so its words remain readable in the small preview.

The `BALLS` table contains the four specified factors. Hit schedules are computed from square root of 3.6 / 9.8,
retaining bounce flights at least 0.25 seconds. `sync` integrates wall time with a speed of one or one-half, so Slow
changes speed immediately. `frame` logs scheduled and actual hit times in `__tool.state.hitLog` and drives counts,
lights, squashes and pitched ticks. Motion off retains the same clock.

`match` is a dynamic program maximizing in-order pairs, then minimizing total absolute time gap. The asymmetric
window is 0.15 seconds early to 0.40 seconds late. Live tap times are already physical seconds, including Slow.
The final one-second recording window uses physical time, so it lasts two wall seconds in Slow.

Each mode retains finished rows in memory. Interrupted trials are discarded. Rows retain at most three class counts.
A paper stepper replaces the current try's count and hides the tap row, because paper tallies have no timestamps.
Paper comparisons use explicit paper wording rather than directing children to rings that are no longer drawn.
Changing a ball while idle clears the current comparison but preserves completed table rows.

`Curio.voice` uses easy-coach / Umbriel in `voice/lines.json`. No audio was recorded, as directed. Browser speech is
the current fallback. All static narration is enumerated by `__tool.allLines`. Token checks, mode scope and hush
drop stale results when a run restarts. `V.heard` guards the one-time sensor explanation.
Paper changes preserve a ball-result line already playing, replace queued obsolete comparisons, and stop an old
comparison if its totals have changed. Read remains protected by the kit.

#### Art and open-question decision

Nine new non-person illustrations were made with the built-in image tool. Their full base prompts and revision
instructions are in `art/prompts.json`; originals are in `art/raw`. The drop stands were redrawn after the first
closed image included a yellow ball and the first open image changed the stand into a gauge. The accepted pair
has an empty claw and consistent equipment. All finished assets passed through `scripts/art.py --rekey`.
The old `gym-wall.webp` and its original prompt were preserved; the new full gym image is used in the stage.

Cold review resolved the open question toward the spec's painted hand. The current people rule permits this.
`tap-hand` now has a five-fingered painted palm, warm brown skin and an orange cuff, made with OpenAI image generation.
It is marked `people: true`, processed with `art.py --rekey` using `holes` and `despill`, and displayed on the hand
button and Me plate. The final people-art review should check anatomy, age impression, skin tone and representation.

#### Model notes

Recomputed counts and times match the spec. The bouncy ball's next omitted flight is 0.249577741 seconds; this is
below 0.25 but rounds to 0.250 at three decimal places, rather than the spec's truncated 0.249. Do not round it
before testing the cutoff. The exact specified factors take precedence over rounded factors derived from standards.
The noisy-child statistic in Sources is illustrative; its random distribution and seed are not fully specified.

#### Engine changes wanted

None. Shared kit, docs and scripts were not changed.

#### Review next

Read the completed codex-report.md for measured results and mechanical audit leads. Check narration by listening
when easy-coach recordings are available, and try the tap-along with a real kindergarten group. This build makes
no claim of classroom observation. Tiny cutout edge specks on the stand may merit a painter's cleanup later.

#### Cold review repairs, 2026-11-07

Equal totals receive counting praise only when every live tap matches a hit. Paper equality and timing mismatches
get neutral, truthful comparisons. This prevents rapid taps or copying the visible total from claiming counting skill.
The chart retains its prediction sticker. Its first chosen row is remembered for the current experiment; correcting
a wrong row gets an explanatory line, without first-choice praise or its chime. It remains an unscored discussion.
The table's prediction sticker is anchored over the ball picture, away from three large class-count entries.
The tap-along instruction precedes the ball-pick instruction. The sensor explanation precedes the optional fast-hit
observation after comparison, and is also available after the no-taps paper prompt. `V.heard` still governs once-only speech.

#### Sensitivity

One people asset: `tap-hand`, explicitly marked `people: true`. No cultural, religious or historical claim is made.
Inspect the painted child's hand for anatomy and respectful representation in the final people-art review.

#### Source correction

FIBA's current 2024 equipment document uses 1.035 to 1.085 m rebound measured at the underside, from a 1.8 m drop.
The spec's 1.2 to 1.4 m reference used a top-of-ball convention. Keep the explicitly mandated factor 0.85 and ten
model hits until the spec owner changes the model. Notes and metadata now distinguish it from a certification claim.

#### Final build checks

The full audit finished with 28 leads; all base sizes, calm mode, resize stress, console and keyboard activation
checks were clean. The report records each lead's disposition. Fixed compact caption/count overlaps, moved the
prediction star out of text flow, and replaced zero-font button words with real icon spans and hidden labels.
Repeated taps on an active mode or the same idle rack ball preserve its current instruction. A quick Drop still
restarts immediately and makes the tap-along line stale, as required. Read is protected from the first-hit hush.
Focused layout probes after repairs are clean at 680, 800, 1000, 1366 and 375 through an iframe. Six quick held-click
pairs passed without cutting their instructions. The original full audit was not repeated after these focused fixes.

#### Cold review verification

The single final audit completed within the 40 minute limit with 12 leads. Desktop sizes/states, focus,
repeated clicks, calm mode and resize stress were clean. The audit's phone iframe context lookup failed;
separate 375 px host frames and Read logs cover the default, prediction, chart, paper maximum and three large tries.
This last extreme found a prediction-sticker/count collision. Only that CSS anchor changed after the audit;
the fixed table was re-shot at 375, 680 and 1366, with no overlapping sticker/text bounds or console errors.
The main voice walk and five completed counted drops used real browser speech logs, not a speech stub.

Two very-low-delay practice-feedback capture attempts lost Chrome before the Reset fixture; these are inconclusive,
not visual passes. Normal/audit control walks were clean. Preserve that limitation for the next reviewer.
The cold-order limitation and first documentation-command timeout omission are recorded in codex-review.md.
All review Chrome processes and the verified 8745 host were closed. No review ports remain open, and host.html is absent.
Evidence and the reviewed frames are in _scratch/me-vs-the-counter/review-*.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
