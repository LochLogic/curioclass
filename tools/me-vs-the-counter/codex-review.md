# Codex review: me-vs-the-counter

## Played

Cold kindergarten/projector walk before builder notes or source; later continued through the chart and a keyboard-only round.
The accelerating bounces and paired timeline are strong. The original equal-total praise was misleading.
## Findings fixed

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
## Findings left

No confirmed blocker or should-fix remains in the reviewed implementation. The audit's phone host could not expose
its iframe context; separate 375 px checks provide the visual and interaction evidence, not a mechanical audit PASS.
## Break it

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
## Voice walk

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
## Facts checked

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
## Sensitivity

No culture, religion or hard history. One people image, tap-hand, is marked people:true. Final people-art review should
check five-finger anatomy, child age impression, warm brown skin and respectful representation. No stereotype found.
## Flattest moment left

Waiting for a paper tally is still deliberately quiet. The chart payoff now reconnects the class's prediction
with its measured row; correcting a guess invites comparison rather than unearned praise.
## Graphics

Kept the painted gym, textured equipment, balls, lighting, movement and timeline. Added tap-hand through imagegen,
then art.py --rekey with despill/holes; checked final cutout and its actual 65 px button use, plus all other images.
Every art token has a finished asset. Whole set is coherent; old unused gym-wall retained. Bundle about 498 KB.
Inspected all STANDARDS widths, 375 iframe, grayscale, calm, prediction/result/chart, paper extremes and keyboard focus.
Viewed current Snowy Mail Route and Beat Lab beside tool frames in review-sheets/targets-0.jpg; this scene is not plainer.
WCAG ratios recomputed: white/header 5.02, ink/paper 15.23, muted/paper 6.25, orange/paper 4.75,
teal/plate 5.77, focus/paper 6.34. Pictures, labels, side and ring shapes supplement color.
## Audit

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
## Left open

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
