# Codex review: egg-carton-factory

## Played

Cold Grade 4 solo/projector play covered all modes and four Rush tasks before builder notes/source.
The rich shed, immediate re-packing and turned-pair glow are strong. Later held-input walks shipped each task kind correctly.

## Findings fixed

- Should fix, general, Rush voice: Every shape how-to was dropped behind the generic welcome on the two-second Pack/Ship path. Task instructions now lead.
- Should fix, general, Pack voice: queued fit/turn teaching now requires the same order to still fit; proof speech names both rows and columns.
- Should fix, general, Pack graphics: green shape labels disappeared into the painting. Added opaque paper plaques with green outlines.
- Should fix, general, assisted answers: six proof cartons overflowed the compact panel. Exact SVG cartons now fit a three-column grid; reading time follows text length.
- Should fix, general, persistence: a saved seal could reload with a partial shelf. All previously earned pairs now restore together.
- Should fix, general, extreme text: corrected singular egg, cup and full-column wording.
- Polish, general, finish: the final recap was overwritten. Banner and feedback now retain the student's own/helped totals.
- Polish, general, weakest art: flat Multiples cards now have shaded exact-layout carton drawings, paper shading and pin details.
- Should fix, general, compact seal: factors and the next action fell below the panel; phone focus could scroll the hint away. Reclaimed header space, paired Next/Reset controls and concise seal text now keep every factor and primary control in view.
- Should fix, general, result focus: disabled Ship dropped focus to the page. Help and shipping regions now receive focus until the next card. First-miss feedback receives focus, then returns it to the retry action. Checked answers lock during shipping; Multiple feedback names only visible controls. The old readout hides behind the help explanation.
- Should fix, general, active selection: re-entering the selected mode/card could reset unfinished work and cut its welcome. Current selections now preserve work and speech; obsolete fit speech stops when the new carton has gaps, with the search instruction retained in the hint.
- Should fix, general, numeric field: native spinner space clipped the largest order on narrow inputs. Adjacent Order buttons now provide stepping while 100 remains fully readable.

## Findings left

- Should fix, general, compact Order Board: its all-visible 10 by 10 layout has targets under 44 pixels. See Left open for the specification conflict.

## Break it

Independent drive evidence: `review-break-results.json` and final `post-break-results.json`: 2,323 assertions each, zero failures.

- Every shape: empty/partial shelves cannot earn credit; duplicates and turned copies cannot increase the count. Sweeping rows is the specified systematic search skill.
- Sort: all 27 assignments per variant tested, including all Prime, all Composite and odd-means-prime. One-row/one-column cartons do not prove composite; nontrivial rectangles do.
- Multiples: all eight Fills sets per variant, copied order/size counts, blanks, zero, 100, fractions, exponent notation and spaces tested. Only exact selected sizes and quotients pass.
- Decade: all 512 selections in each decade tested. All odds, all numbers, none, extra evens and omitted primes fail.
- Credit: first miss gives no credit; second miss is helped. Cancelling help or replaying cannot turn helped into own; misses survive rerolls.
- Explore-copy: leaving Rush changes the unfinished variant; seals and board remain hidden in Rush.
- Seal/board: independently enumerated all factor pairs 1 to 100. Reload now restores all five earned pairs for 36, matching its factor list.

## Voice walk

Held clicks: 120 ms, ordinary actions two seconds apart, default Sound on. Read final `last-voice-main-*.json` and `voice-repeat-*.json`.
Pack edge, row search and turn, Fill size/Run, Board, Rush row search/Ship:
`wPack, fitHow, sealComp, turnHow, wFill, fillYes, wBoard, everyHow, wRush, shipRight` started in that order.
Sort: `everyHow (cut), sortHow, wRush, shipRight`. Multiples: `everyHow, wRush (cut), sortHow (cut), multHow, shipRight`.
Decade: `everyHow (cut), wRush (cut), decadeHow, shipRight`. Cuts follow explicit shift/card navigation.
Count fields were populated through their input handlers. Explicit mode changes stop departed speech; no stale line followed the switch.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| fitHow, five fits | how | 1 | 1 |
| fillYes, five runs | event | 5 | 5 |

Read interrupted speech, worked with Sound off, and released immediately on mode change. Actual Achird recordings are absent; this is browser-speech timing evidence.

## Facts checked

- All four learning actions match [CCSS 4.OA.B.4](https://www.thecorestandards.org/Math/Content/4/OA/) and [Illustrative Mathematics](https://tasks.illustrativemathematics.org/4.OA-2), checked live.
- Prime has exactly two positive factors; composite has a nontrivial pair; 1 is neither: [Math is Fun](https://www.mathsisfun.com/prime-composite-number.html), checked live.
- Two is the only even prime; odd composites and all three decade prime sets: [Math is Fun prime list](https://www.mathsisfun.com/prime_numbers.html), checked live plus independent enumeration.
- Turned pairs repeat; the search stops when the smaller side passes its partner: [Math is Fun factor search](https://www.mathsisfun.com/numbers/factors-all-tool.html), checked live plus enumeration.
- Every 1-to-100 factor list, all 36 Rush variants, square 36's five shapes/nine factors, maximum six shapes and smaller side at most ten: `review-numbers.json` and independent browser checks.
- 72/6=12, 72/8=9; 70/4=17 remainder 2; all other displayed counts/remainders: independent integer division, under the CCSS factor/multiple definition above.
- The real 30-egg, 5-by-6 flat: [Miller Manufacturing](https://miller-mfg.com/products/egg-flats-30-count-5-x-6-package-of-12), checked live. Other layouts are explicitly fictional shed cartons.
- Gus and the farm orders are fictional, consistently stated in the footer and notes. Notes open with the three required sections.

## Sensitivity

Four flagged people assets show the same fictional older farmer. Fresh inspection found consistent identity, friendly expressions, natural hands and no stereotype.
No cultural tradition, Indigenous content, religion, hard history or body instruction is claimed. No added cultural review issue identified.

## Flattest moment left

The middle of a six-shape factor search is methodical. It remains the intended systematic search; the later Sort, Multiples and Decade tasks supply variety.

## Graphics

All 15 paintings inspected in a contact sheet and scenes, including the full truck, hen poses and Gus poses. All four people flags confirmed.
Kept the coherent warm artwork. Improved the code-drawn cards, label plaques and assisted proof set; no painting was weakened or removed.
Art: 449.7 KiB. Bundle: 700.7 KiB. `review-comparison/sheet-0.png` places this tool beside Snowy Mail Route; Beat Lab was also opened.
All required widths inspected, including 375 in the host; grayscale, Motion off, keyboard input, one/100 eggs, short fills, seals and final recap checked.

## Audit

Audit not finished: the 40-minute cap interrupted resize stress. The partial `review-audit/audit.md` preserves 429 leads and 120 frames; the exact old bundle is `review-audit-bundle.html`.

- Completed every listed size/state, Motion off, all four mode control walks, ten five-click samples and ten quick-tap samples. Full resize-stress coverage is not claimed.
- Four hundred rows confirm the single compact-board target conflict, left open below.
- Repaired the confirmed compact seal/hint visibility, shipping focus, active-selection welcome interruption and assisted-caption overlap leads. Scoped geometry, real-click frames and cheat replays verify the repairs.
- Passive readout hit-test coverage and hints behind the inert reset dialog are false positives. Conditional Ship wording describes a later enabled step, exactly as specified.
- The three first-tap welcome skips follow baseline rule 16. Rapid Order changes stop obsolete speech; keeping the old fit statement would contradict the new carton.
- No application errors in completed checks. The iframe host's favicon 404 and timeout shutdown stack are harness output. An earlier Chrome connection loss was retried smaller. A duplicate late drive attached to the existing owned browser and disconnected when its original run closed it; all eight final frames, four voice logs and 2,323-check result were saved.
- No second audit. Owned browsers/server closed after checks.

Sealed-order geometry passed at 680 and 375 for 36, 60, 72 and 100: hint, full factor set and all primary controls visible; targets at least 44 pixels. Re-shot each affected compact mode and both result-focus states.
Recomputed contrast: ink/paper 14.79:1, muted/paper 6.59:1, white/brand 6.40:1, new label/paper 9.55:1. [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); `review-palette.json`.

## Left open

- The review rule prohibits changing a conflicting spec. Kept its whole compact board instead of adding navigation or scrolling; documented the target limitation in notes/handoff.
- Spec totals are inaccurate: 15 assets and 36 variants, not 14/27. Some correct counts equal shown sizes (48/6=8, 54/6=9); exact quotient checking remains correct.
- No audio was recorded, per build rules. Browser speech was exercised; the named bank voice still needs its production recordings.
- Initial read-only commands and two initial shell-parsing failures lacked a full wrapper; all bundle, drive and audit checks had explicit caps.
- Only authorized tool/Scratch paths written; no commits. Host page removed and owned Chrome/server processes closed. Stop after this report.
