# Codex review: traffic-light-coder
## Played
Before builder notes: Grade 3 student play of the live crossing, all five starting jobs, two solved jobs and replay.
Then finished the remaining three UI fixes, checked projection frames and walked Teaching, Play and Craft.
The ambulance rule moving to the top remains the strongest moment; the painted street is worth keeping.
## Findings fixed
- **Blocker, family:robot, teaching, src.html/summarize:** a missing yellow rule could produce “Rule 0”.
  Attribution now follows the light cycle active at ambulance arrival, including earlier-cycle cases.
  `audit-fixed-arrival-cause.png` verifies Rule 5; the standard ambulance case still names Rule 1.
- **Should fix, general, play, paused Watch hints:** calls said to watch a street that was stopped.
  Walker and ambulance hints now name Step and Play immediately; Read uses those hints.
- **Should fix, general, craft, narrow layout:** test controls followed the street and disappeared while editing.
  Hint and controls precede the street; test controls remain visible while the rules scroll.
- **Should fix, general, graphics:** the three specified walkers were temporary silhouettes.
  Painted and integrated all three, with natural skin/hair variation, backpack detail and correct travel facing.
- **Should fix, general, craft, compact unsafe reports:** the added trace pushed return/replay controls out of view.
  Repaired after audit: all three unsafe lines and Back to rules fit at 680, 800, 1000, 760 and 375 widths.
- **Polish, general, play, report:** the failed Rush Hour result was a large empty receipt of numbers.
  Added the student's actual car-light intervals, with words/patterns; content-sized cards reveal some street.
  Compact unsafe reports keep their existing replay chronology; the other reports retain the light trace.
- **Polish, general, notes:** stated that saved kit settings never leave the device.
## Findings left
- **Polish, general:** stacked narrow pages still require vertical scrolling to reach every rule and card action.
  Primary test controls now stay visible. Five/six-rule internal scrolling is explicitly permitted by the spec.
- **Nit:** no further cosmetic changes accepted; the original street, cars, signals and palette remain intact.
## Flattest moment left
A program with no matching rule waits to the 120-street-second cap. Skip to report is available throughout.
The flat failed report was lifted; this remaining wait is the specified test behavior.
## Graphics
Checked all 12 finished images, the three people cutouts at scene size, grayscale, and all 89 audit frames.
Retained the nine original paintings; added walker-red, walker-yellow and walker-green using built-in imagegen.
Prompts/provenance: `art/prompts.json`; originals: `art/raw/`; finished assets: `art/*.webp`.
All three people assets have `people: true`; contact sheet: `_scratch/traffic-light-coder/walkers-contact.png`.
Matched the warm gouache set; no text artifacts or stereotypes found. Compared with both bar-tool frames.
Art: 232.0 KiB. Final offline bundle: 432.8 KiB.
## Audit
One audit completed within 40 minutes using Chrome 9941 and host 8745; no second full audit.
79 leads: 8 addressed (compact report fit/clipping geometry), 61 narrow-scroll leads retained,
2 permitted six-rule scroll leads retained, 8 first-tap welcome skips required by the spec retained.
Every lead has an indexed response in `_scratch/traffic-light-coder/review-audit-responses.md`.
Motion off, held clicks, repeated speech, rapid taps and resize stress were clean; no audit console errors.
Eight targeted final frames passed with zero console errors. Rechecked only the affected layouts and attribution.
Independent Python results match 14 browser programs, including every Rush Hour variant and ambulance order.
Recomputed 35 / 3.5 = 10 seconds and all seven contrast ratios (minimum 5.333:1).
Keyboard-only Job 3 was edited, tested and passed with visible focus. Unsafe replay paused at 18.5 s on Rule 4.
Wave lessons checked: immediate hints, stable focus, targets, short choices, no giveaways, honest numbers,
standards practiced, Motion off, resize, truthful badges and first-tap timing. Notes open with the required sections.

| Spoken line | Kind | Expected | Observed |
|---|---|---|---|
| w-jobs | welcome | 1 | 1 |
| miss | event across five tests | 5 | 5 |

Evidence: `_scratch/traffic-light-coder/review-final-validation.json`, `review-numbers.json`,
`browser-numbers.json`, `keyboard-review.json`, `voice-review.json`, and `audit-fix-frames/`.
## Left open
Narration uses browser fallback; no audio was recorded, as instructed. No classroom/headphone test was performed.
Narrow-page scrolling remains as described above. The optional shared runner finishNow request stays in handoff.
People contact sheet is available for the owner's pre-ship review. This review does not publish the tool.
Only the tool and its Scratch folder were written; no commits or shared-engine changes.
