# Codex report: reserve-designer

## Built
Plan, Stress test and Groups, using the kit starter, 9-12 theme and Curio.voice.
A painted 12 by 8 valley, full-price refunds, working-farm and restoration choices, wildlife crossings,
six live species rules, per-device saving, species overlays, deterministic single-loss futures and group models.
All authored files are confined to tools/reserve-designer and _scratch/reserve-designer. No commit or polish round.
All four spec questions were resolved toward the stated leaning in handoff.md.

## Numbers check
PASS: independent Python counts F24, G20, W9, A20, T4, R7, H11, B1.
PASS: 700 independent browser/Python rule and cost fixtures, including restored farms and lost cells.
PASS: lean $2,950k, 14 purchases, six needs met, $1,050k left, 0 of 14 futures; elk fails in 13.
PASS: working-farm corridor $2,750k, 12 purchases, all six met, 0 of 12 futures; elk fails in 11.
PASS: refined $4,000k, 19 purchases, 14 of 19 futures. Weak cells, zero-based: (4,5), (5,5), (6,7), (6,8), (6,9).
PASS: 1 - 0.8^n gives 20.0%, 67.2%, 89.3%, 98.8% for n = 1, 5, 10, 20.
Discrepancy: the budget can afford 21 cells, so 200 ms per future can take 4.2 s, rather than the spec's four-second maximum.
The prescribed pace and prices were retained. The checked 19-cell plan takes 3.8 s.
Not independently reproduced: search-start counts and $3,000/$3,500 bests, which lack seeds and witness plans. None is shown.
Contrast: accent/panel 5.17:1; dark ink/accent 5.42:1; ordinary text/panel 14.70:1.
Dark inner outlines against the lightest painted-tile pixels range from 6.80:1 to 12.98:1.
The double line, flags, patterns and accessible names carry meaning alongside color.
Evidence: numbers.py, numbers.json, functional-evidence.json, post-audit-evidence.json and build-evidence.json in Scratch.

## Feel check
Played the reference designs through real held clicks, ran their futures, returned to refine, restored farms and tried Groups.
Best moment: all six field notes turn to checks, then the stress test isolates the southern chain into five cracked cells.
Flat moment 1: crowded compact status text pushed instructions out. Shortened status text and used two portrait columns.
Flat moment 2: compact Groups scenes were squeezed by repeated copy. Rearranged controls and kept the real finding beside the model.
The needs selector moved into the map header, keeping the plan controls and hint visible.
Groups is a short supporting investigation; the reserve's alternate connections provide the longer design challenge.
Compared with both bar tools. The final Groups frame is beside Beat Lab at the same scale below.
![Reserve Designer beside Beat Lab](../../_scratch/reserve-designer/feel-comparison.png)
The paintings, detailed tile patterns, flags, moving river and responsive field notes match the intended finish without copying either bar.

## Done when
1. PASS: empty map has zero met; both lean and farm-corridor plans meet six; held-click evidence records exact spending.
2. PASS: 0/14 and 14/19; exactly the five required weak cells, independently and in the browser.
3. PASS: fifth restoration refused with the 16 farms reason; farm-on still allowed; overspending reports remaining amount and price.
4. PASS: one bank activates its river cell; bridge absent with one side and present with both sides protected.
5. PASS: ten painted elk and 89%; all eight prairie dogs dive, and a repeated alarm restarts the three seconds.
6. PASS: map is largest in Plan/Stress at 1366 and 680; painted habitats dominate Groups cards.
7. PASS: Weakest cells and Back respond during playback; resize does not lock the run; the herd changes immediately.
8. PASS: a keyboard purchase survives reload; no plan code, transfer or export feature exists.
9. PASS: all 96 cells have names and a keyboard route; arrows stop at boundaries; Enter opens and buys; focus returns without scrolling.
10. PASS: primary controls visible at 1366 and 680; phone map cells are wider than 26 px with no horizontal page overflow.
11. PASS: farm how-to starts once in five repeated actions; all-six event starts twice for two transitions; stale menu speech stops on close.
12. PASS: all 21 images load, no people, no external resource URLs, no em dashes in authored files.
Partial-plan repair: futures name only newly broken needs; an already-unmet need is not presented as a loss caused by the test.

## Wave lessons
PASS Hint and voice: synchronous hints, Read uses current hint, kit how/event distinction, held clicks and repeat logs.
PASS Focus and layout: stable grid/control nodes, no load focus, dialog focus trap, preventScroll on deliberate focus.
PASS Sizes: all required viewports and hosted phone; ordinary controls are 44 px; the spec allows 26 px map cells.
PASS No giveaways: no supplied solution is exposed. This is an open design model with full refunds as specified.
PASS Honest numbers: fictional thresholds and prices, independent-watch assumption, source finding and single-loss horizon are explicit.
PASS Standards: reserve design/refinement, simulation testing and hands-on group comparison all have student actions.
PASS Motion off: zero active CSS animation; two of ten elk watching; dog timing retained; stress instant as explicitly specified.
PASS Short choices: farm and crossing actions are all visible in their popover; no choice list is hidden in a scroll panel.
PASS Resize mid-animation: active stress run resized, then stopped immediately with Back; no exception or locked controls.
PASS Welcome order: no welcomeAfter; an active mode tap is a no-op and does not cut its welcome.
PASS Unknown state: unprotected land and unmet needs remain explicit; model results are not called forecasts.
PASS One look/meaning: flags/double outlines are protection; dashed cracks are weak links; dark cell/loss word is a selected future.
PASS Truthful badges: field-note checks come from the evaluator; partial-plan labels distinguish existing gaps from new loss.
PASS Hint reversal: mode changes update immediately; closing overlays and returning to Plan restore relevant instructions.
PASS No copied-answer puzzle: no diagnosis quiz or answer-by-word-matching mechanic is present.

## Audit leads
One full audit completed in about 32 minutes: 63 frames, 108 leads, no runtime errors.
Detailed item-by-item answers: [audit-leads.md](../../_scratch/reserve-designer/audit-leads.md).
Fixed: Read/Plan target widths, phone Read clipping, 10 px statuses, active hint placement, phone Back/Alarm visibility and Back focus.
Fixed: zero-sized formula captions became real 10 px spans; compact model and citation text is entirely inside its card.
Fixed from frame inspection: partial-plan loss labels, stale cell captions and instructions left behind when a menu closes.
Retained small secondary text: 9 px survey eyebrow, 9 px bibliography, mathematical superscripts and 8-9 px future thumbnails.
Accepted diagnostics: mobile icon-only buttons have visible 17 px glyphs and accessible names; first-cell welcomes intentionally go stale.
Accepted interruptions: Clear cancels speech; resizing dismisses a popover and returns focus, rather than leaving a run locked.
All repeated-action and quick-tap checks were clean except the deliberate Clear interruption.
Final targeted checks cover 96 keyboard cells, menu closure, same-mode welcomes, two all-six events, a farm completing all six and rapid alarms.
The full audit was not repeated. Only affected modes, sizes and interactions were re-shot after repairs.

## Frames looked at
Both bar frames; all four quick frames and their compact repair frames; all 21 full mode/size frames.
All nine special frames: farm menu, crossing, needs overlay, herd 1/20, alarm, Motion off, grayscale and keyboard.
All final targeted frames and affected-mode repair frames, three hosted phone frames, the art contact sheet and seven audit sheets covering 63 frames.
Native-size inspection included the compact stress result, farm menu, crossing menu, needs overlay and final partial-plan repairs.
See Scratch frame folders and audit-gallery-index.json for exact names.

## Art made
21 finished WebP assets: 15 generated during this Build and six retained portraits. Art totals 557,892 bytes (544.8 KiB); the standalone bundle is 836,190 bytes (816.6 KiB).
Nine terrain tiles, two large landscapes and four animal/burrow cutouts generated during Build with the built-in imagegen tool.
Six supplied wildlife portraits retained. Full prompts/provenance: art/prompts.json; selected originals: art/raw.
Four cutouts re-keyed with despill after inspecting their edges. No redraws, downloaded images or recordings.
Map overlays, flags, cracks, mini maps, chart, compass, budget and preview are drawn in code.

## Art still to paint
None.

## Engine changes wanted
None. Shared kit and scripts were left untouched.

## Left open
External source URLs were supplied by the spec and were not rechecked online during this offline Build.
The unverified Colorado crossing percentage is not displayed. Browser speech is the intentional fallback; no recording was made.
Phone field notes scroll vertically. Both Groups controls and scenes now fit side by side in the phone viewport.
Secondary compact bibliography, superscripts and future-strip labels retain small text; all main controls remain 44 px.
The 21-cell, 4.2-second pacing discrepancy is documented above and in handoff.md.
Final closure: all owned Chrome and host processes are closed; ports 9970-9977 and 8775 are free. Temporary host.html is absent. No commit, deployment or polish round was made.
