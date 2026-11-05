# Codex report: cereal-ad-questions

## Built

- Built the three modes, eight switch combinations, original synthesized jingle, live part switches, class votes, SVG comparison chart, five message cards and eighteen day-scene hotspots.
- Added all required build files and ten generated paintings. The bundle is self-contained. No commits, branch changes, recordings or polish round.
- Source uses the kit controls, AudioContext and Curio.voice. Activity data stays in memory.
- All working commands after the initial read used a bounded child-process runner: bundle 120 seconds, drive batches 300 seconds, audit 2400 seconds.
- Only this tool and its Scratch were authored. Bar tools were copied and bundled in Scratch to avoid writing their folders.

## Numbers check

- Evidence: `_scratch/cereal-ad-questions/numbers.json`, recomputed with Python before the first bundle.
- Five shots times three seconds = 15 seconds. Sixteen beats at 132 beats per minute = 7.272727 seconds; two loops = 14.545455 seconds.
- The exact remaining tail is 0.454545 seconds, rather than the spec's rounded 0.4 seconds.
- Three scenes times four ads = 12 ads; three times two non-ads = 6. Vote bounds are zero through forty per bar; chart scale has a floor of ten.
- Supplied shelf heights convert to 58.42 and 121.92 centimeters. No extra height claim was added to the interface.
- Contrast: white/brand 7.3071, brand/paper 6.9331, ink/paper 16.2211, muted/paper 6.6131. All match the listed rounded values.
- The spec says eleven images but names ten. All ten named assets are present and used.

## Feel check

- Played the whole sequence through the ad comparisons, all five message interpretations and all eighteen discoveries using muted Chrome and real held input where narration races matter.
- Best moment: the bright selling scene becomes a quiet painted bowl while the class's own pairs of bars remain. The illustrative test poll used 28/4, 17/15 and 5/27, not a built-in result.
- Flat moment one: the box name initially floated off its blank panel. Repositioned it onto the package so the opening reads as one convincing product.
- Flat moment two: the portrait message TV made Comet too small and left a large gap above the trampoline. Stacked the scene and all five cards at 760 wide; the final frame is `postfix-frames/portrait-messages.png`.
- Also preserved whole bowls in wide TVs with contained paintings over a blurred painted surround, removed sign-covering discovery badges, and fixed compact sign wrapping.
- Compared with both bar tools. `_scratch/cereal-ad-questions/bar-comparison.png` places the Comet shot beside Beat Lab. This build has comparable visual depth for its younger audience; its replay value comes from changing reactions rather than a music sequencer's open-ended composition.
- Audio was muted for testing. No claim of headphone listening or a real K-2 classroom trial.

## Done when

1. PASS: TV is the largest object at 1366x768 and 680x425. Switches and voting controls remain visible. Default audit sizes are all clean.
2. PASS: all eight combinations completed at an elapsed 15000 milliseconds. See the eight `finished-*` checks in `functional-results.json`.
3. PASS at the browser node/state level: music disconnects synchronously and starts at the current beat, pictures swap immediately, Words returns on the next line, and Stop clears nodes. See `functional-rest-results.json` and `words-next-line.json`. Acoustic latency was not measured.
4. PASS: bounds, ownership and labeled SVG bars checked. A completed replay starts a fresh zero-count poll and replaces its previous bars; edits to the previous poll during playback are committed. See `replay-check.json`.
5. PASS: two completed Plain bowl polls each started the big-question event. `voice-behavior.json` records first=1, second=2 and no host speech during either ad interval.
6. FAIL in one content requirement: all fifteen part-button paths run three seconds and all five True? cards show/speak, but the Words clip contains only the opening slogan. Five complete spoken slogans cannot fit clearly into the required three seconds. The full ad contains all five.
7. PASS: all eighteen objects tested, four ads per scene, non-ads excluded from the counter, targets at least sixty pixels. The phone counter now has its own row.
8. PASS: host narration is gated during playback, Read stops playback first, how-to lines use the kit heard set, and two-second held-click checks are clean. Requested recorded performances remain unmade under the Build rule.
9. PASS: sixty-pixel controls, icons and words, visible focus and object names for intentionally hidden hotspots. Default and explicit message states were mechanically clean for target size.
10. PASS for offline operation, still shots with unchanged timing, and no activity saving. FAIL literally for "nothing is saved": the required shared kit persists only the Motion preference. Standing STANDARDS.md takes precedence.

## Wave lessons

- PASS, Hint and voice: hints change synchronously; Read uses the hint/open card; first actions proceed immediately. Two-second switch test started all five events.
- PASS, Focus and layout: stable controls, no load focus, held-click audit has no focus losses. Stop moves focus to Play; Escape restores the next-action hint. Sign-covering checkmarks were removed.
- PASS, Sizes: all eight required sizes across the three modes, including 375 in an iframe. Only affected portrait, phone and compact states were re-shot after repairs.
- PASS, No giveaways: object names do not reveal ad classification. Classification appears after a tap. This is an explorer and discussion tool, not a hidden-answer scoring game.
- PASS, Honest numbers: actual entered hands, shared chart scale with a floor of ten, no expected downward trend, no assumed class total.
- PASS, Standards: part switches teach Re7, message/evidence cards teach Re8, own-vote comparisons teach Re9, and daily scenes teach Cn11.
- PASS, Motion off: the audit found no endless animation; the still Comet frame retains the regular shot clock.
- PASS, Short choice groups: all five message choices and all three part controls are in view; no short-choice scroll panel.
- PASS, Resize mid-animation: audit stress produced no exceptions or stuck disabled controls. Subsequent portrait art fitting was checked in targeted frames.
- PASS, Welcome after first tap: an action's own event skips the welcome as required. Re-tapping an active mode no longer cuts its playing welcome.
- PASS, Unknown as unknown: unexplored objects have no discovered classification; the four-ad total is an explicit hunt goal from the spec.
- PASS, One look, one meaning: the glow means explored for either kind of object. Only ad discoveries affect the ad counter; the card states An ad! or Not an ad.
- PASS, Badge says what is true: current version changes live and Stop clears the playing badge. Votes name their completed owner in the hint when the parts change.
- PASS, Hint changes back: mode, place and modal-close paths restore appropriate instructions. Escape was checked with real keyboard input.
- PASS, No answer by copying: evidence and True? discussion do not use a matching-words scoring mechanic; daily classifications are revealed only after inspecting an object.

## Audit leads

- One full audit completed: `_scratch/cereal-ad-questions/audit/audit.md`, 53 leads. All eight initial sizes, Motion off, resize stress and five-click voice repetitions were clean. No full post-repair audit was run.
- 38 sign/hotspot overlap leads: intentional labels on their tappable objects. Labels have no pointer interception and now paint above the glow. Final compact Street and Store frames show legible signs.
- 5 phone counter overlap leads: FIXED with a separate counter row. `phone-counter-check.json` confirms its top is below the place buttons; final phone frame inspected.
- 2 covered-hint keep-region leads: intentional modal coverage. The modal contains the current answer or confirmation, and Read speaks that content. Both dialogs and their Close/Keep paths remain reachable.
- 5 first-action welcome-not-heard leads: correct standing-rule behavior for Music, Pictures, Words, Play and Start over, each of which has its own action or line. No late welcome was added.
- 3 quick same-mode welcome cuts: FIXED by preserving the active mode on a repeated tap. `same-mode-check.json` records one uncut welcome.
- Audit limitation: its MODES_JS only recognizes controls under a header. This tool's separate navigation was not auto-detected, so the automatic per-control walk covered the initial mode. Explicit state frames, the size matrix, fifteen clip paths and eighteen hotspot inputs covered the other modes independently.
- Other build fixes after the audit: stale card welcome interruption, Stop label/focus, Escape hints, portrait painting proportions, sign badges/wrapping, and fresh replay vote ownership. Targeted checks passed; this is not a second full audit.
- The first live-music-off probe failed and was repaired by disconnecting the audio bus. A later host-speech test window extended beyond the ad boundary; correcting it to the actual start time produced an empty during-ad host log.
- An initial phone harness favicon 404 was eliminated with a data favicon. Final phone and targeted batches report zero errors.

## Frames looked at

All paths below are under `S:/CurioClass-codex/_scratch/cereal-ad-questions/`.

- `bar-frames/`: Snowy Mail Route and Beat Lab. `first-frames/`: laptop and compact initial builds.
- `frames/`: all 24 desktop/iframe mode-size frames, individually or in `contact/0.png` through `3.png`.
- `extra-frames/`: calm Comet, grayscale, keyboard, class-chart payoff, both compact dialogs, Street, Store and voice pace.
- `final-frames/`: SVG payoff, plain compact, painted toy card and clean phone harness.
- `audit/`: all 57 frames, reviewed in `contact-audit/0.png` through `9.png`; compact vote and phone-limit frames also opened full size.
- `postfix-frames/`: portrait messages/day, compact and phone Store, Stop label, Escape, same-mode double tap and card interruption.
- `sign-frames/`: final compact Store and Street. `voice-frames/`: repeated Plain bowl question and next-line Words. `replay-frames/`: replay vote replacement. `asset-frames/`: final edge-cleaned Comet and toy reveal.
- Every final painting was inspected, including keyed cutouts with edge despill. Rejected animal-filled splash/table drafts and the store safety pictogram were replaced.

## Art made

- Ten generated images, 841370 bytes total, about 821.7 KiB. No people in the final paintings.
- Final bundle is about 1169.1 KiB, under two million bytes; exact size is in `static-results.json`.
- Three redraws: splash and table to remove unintended animals; Store edit to remove the human safety pictogram.
- Source credits OpenAI gpt-image. Exact prompts, provenance and redraw counts are in `art/prompts.json`; originals are under `art/raw/`.

## Art still to paint

None of the ten named assets. The spec's unnamed eleventh image is a count discrepancy, not a placeholder.

## Engine changes wanted

- No required kit change. Optional `kit/curio.js` Motion initialization/handler option for in-memory preferences would resolve future no-persistence specs.
- `scripts/audit_tool.py`, MODES_JS: support mode navigation outside a header so automatic walks include these modes. No shared file was changed.

## Left open

- Owner decision on five spoken slogans versus a three-second Words clip. Current clip uses the opening line, and part controls share a persistent evidence strip rather than appearing inside each selected card.
- The plain-bowl-start host line is not spoken, to honor the higher-priority rule that host speech never overlaps an ad. The after-vote big question is implemented and tested.
- Requested news-reader and excited-announcer recordings were not made. Browser voice identity, offline voice availability and the final long slogan's pacing need listening review.
- The shared Motion preference persists, as required by the standing standard; votes and discoveries do not.
- The full audit predates the listed targeted repairs. Cold review remains the next step.
- Procedural deviations: numeric recomputation and bar-tool opening occurred after initial source authoring, before the first playable checks. The first read used the tool wait rather than the later child-process timeout wrapper. The report is intentionally last under the user's stop-on-report instruction.
- Owned Chrome sessions and host server were closed; tool-folder host.html was removed. No git commits and no polish round.
