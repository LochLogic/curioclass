# Reserve Designer: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: reserve-designer

#### Built
Plan, Stress test and Groups, using the kit starter, 9-12 theme and Curio.voice.
A painted 12 by 8 valley, full-price refunds, working-farm and restoration choices, wildlife crossings,
six live species rules, per-device saving, species overlays, deterministic single-loss futures and group models.
All authored files are confined to tools/reserve-designer and _scratch/reserve-designer. No commit or polish round.
All four spec questions were resolved toward the stated leaning in handoff.md.

#### Numbers check
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

#### Feel check
Played the reference designs through real held clicks, ran their futures, returned to refine, restored farms and tried Groups.
Best moment: all six field notes turn to checks, then the stress test isolates the southern chain into five cracked cells.
Flat moment 1: crowded compact status text pushed instructions out. Shortened status text and used two portrait columns.
Flat moment 2: compact Groups scenes were squeezed by repeated copy. Rearranged controls and kept the real finding beside the model.
The needs selector moved into the map header, keeping the plan controls and hint visible.
Groups is a short supporting investigation; the reserve's alternate connections provide the longer design challenge.
Compared with both bar tools. The final Groups frame is beside Beat Lab at the same scale below.
![Reserve Designer beside Beat Lab](../../_scratch/reserve-designer/feel-comparison.png)
The paintings, detailed tile patterns, flags, moving river and responsive field notes match the intended finish without copying either bar.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
Both bar frames; all four quick frames and their compact repair frames; all 21 full mode/size frames.
All nine special frames: farm menu, crossing, needs overlay, herd 1/20, alarm, Motion off, grayscale and keyboard.
All final targeted frames and affected-mode repair frames, three hosted phone frames, the art contact sheet and seven audit sheets covering 63 frames.
Native-size inspection included the compact stress result, farm menu, crossing menu, needs overlay and final partial-plan repairs.
See Scratch frame folders and audit-gallery-index.json for exact names.

#### Art made
21 finished WebP assets: 15 generated during this Build and six retained portraits. Art totals 557,892 bytes (544.8 KiB); the standalone bundle is 836,190 bytes (816.6 KiB).
Nine terrain tiles, two large landscapes and four animal/burrow cutouts generated during Build with the built-in imagegen tool.
Six supplied wildlife portraits retained. Full prompts/provenance: art/prompts.json; selected originals: art/raw.
Four cutouts re-keyed with despill after inspecting their edges. No redraws, downloaded images or recordings.
Map overlays, flags, cracks, mini maps, chart, compass, budget and preview are drawn in code.

#### Art still to paint
None.

#### Engine changes wanted
None. Shared kit and scripts were left untouched.

#### Left open
External source URLs were supplied by the spec and were not rechecked online during this offline Build.
The unverified Colorado crossing percentage is not displayed. Browser speech is the intentional fallback; no recording was made.
Phone field notes scroll vertically. Both Groups controls and scenes now fit side by side in the phone viewport.
Secondary compact bibliography, superscripts and future-strip labels retain small text; all main controls remain 44 px.
The 21-cell, 4.2-second pacing discrepancy is documented above and in handoff.md.
Final closure: all owned Chrome and host processes are closed; ports 9970-9977 and 8775 are free. Temporary host.html is absent. No commit, deployment or polish round was made.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: reserve-designer

#### Played

Grade 9 solo: empty map, connected lean reserve by held clicks, futures, weak links, farm/crossing menus and Groups at 1/10/20 elk.
Played before builder notes or source. Compact projection and all three modes checked at every standard size and hosted 375 wide.
The painted valley and live species feedback are strong; the single-loss test earns its payoff.

#### Findings fixed

- Should fix, general, Plan/Stress: stale stress totals survived a revision. Untested plans now reset their summary and Weakest cells pressed state.
- Should fix, general, Plan menus: clicking unbuyable land left another purchase menu open. Dismiss it first.
- Should fix, general, Show needs: potential elk corridors were dimmed until purchased. Highlight all potential route types and restate seasonal requirements.
- Should fix, general, Stress: empty Weakest cells and zero-new-loss narration implied cracks that did not exist. Give accurate empty guidance and a separate result line.
- Should fix, general, artwork: ovenbird eye mask was biologically misleading. Redrew it with Cornell's plain olive face, complete eye ring and crown stripe.
- Should fix, general, map art: road read as a narrow track. Redrew highway, bridge and wildlife crossing as a coherent, legible barrier and passage.
- Should fix, general, Craft: loss words overprinted crack symbols; slider focus crossed the label. Cleared those conflicts.
- Polish, general, flattest moment: selecting a future left generic directions. Its live hint now names the lost place, broken needs and Back to plan, with immediate sound.
- Should fix, general, 680x425 Stress: the new untested summary cut the hint off. Shortened it and the Run instruction; entry and revision now fit.
- Polish, general, Groups: the first prompt now asks for a 1-versus-20 comparison using displayed evidence.

Independent Python and browser checks match the three supplied plans: costs, six-species results, 0/14, 0/12 and 14/19 futures and the five exact weak cells.
Farm cap, overspending, bank/bridge gates, reload, live interruption controls, keyboard buying and all 96 arrow-key cells passed.
Notes retain the required opening sections; HS-LS2-7, HS-LS4-6 and HS-LS2-8 have corresponding student actions.

#### Findings left

- Nit, general: small secondary bibliography, survey eyebrow and future-map captions remain. Primary instructions and controls stay readable.
- No blocker or should-fix left. The known spec conflict and browser narration limitation remain below.

#### Flattest moment left

Groups remains a short supporting comparison after the richer reserve-design investigation. No extra feature or topic was added.

#### Graphics

All 21 images checked in the contact sheet and their actual scene placements; no people or missing art tokens.
Four redraws made with built-in imagegen, then art.py --rekey: rd-ovenbird and the highway/bridge/crossing tiles.
Full prompts: art/prompts.json. Selected raw PNGs and finished WebPs are in art/raw and art.
Biological reference: [Cornell Ovenbird identification](https://www.allaboutbirds.org/guide/Ovenbird/id).
Art 568.9 KiB; bundle 850.4 KiB. The paintings and detailed survey scene were retained.

#### Audit

Single final audit completed in about 32 minutes: 67 frames, 69 leads, no runtime errors; Chrome 9951, host 8755.
Dispositions: 2 clipping leads fixed; 25 secondary-text nits kept; 2 icon diagnostics, 37 welcome diagnostics, 2 menu-resize diagnostics and 1 Clear interruption accepted.
Every repeated-click row passed. Post-audit checks fixed clipping and the stale pressed state; menus reopened with no disabled actions.
Only affected frames were re-shot. The full audit was not rerun after those scoped repairs. One-cell results now say 1 future.
Evidence: [raw audit](../../_scratch/reserve-designer/review-audit/audit.md), [lead dispositions](../../_scratch/reserve-designer/review/audit-dispositions.md), and review Scratch frames/JSON.
Voice counts, held clicks (starts):

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| farmChoice | how | 1/5 | 1/5 |
| crossing | how | 1/5 | 1/5 |
| allSix | event | 5/5 | 5/5 |
| alarm | event | 5/5 | 5/5 |
| stressDone | event | 5/5 | 5/5 |
| stressNoWeak | event | 5/5 | 5/5 |

Read with Sound off, immediate welcome after Read-to-mode change, and rapid stale-line cancellation passed.
Motion off: 2 of 10 watchers, zero running animations, instant stress result, dog shelter retains three seconds.
Grayscale protection remains clear through double outlines, flags, patterns and state words. Phone cells measured 28.4 px.

#### Left open

- Spec conflict retained: the fixed budget can buy 21 cells; 200 ms each takes 4.2 seconds, above its stated four-second maximum.
- Supplied search counts and lower-budget bests lack seeds/witness plans. No optimality claim or solution is exposed to students.
- Narration uses the browser fallback; recordings were prohibited. Some short-lived lines are intentionally stopped when their state ends.
- The supplied NPS prairie-dog and OpenStax URLs did not load in the web reader; those source routes remain unverified.
- The temporary drive host's favicon 404 belonged to the wrapper, not the standalone tool. The tool itself embeds its favicon.
- Map-first taps skip the Plan welcome under the spec's stale-on-cell-click rule; the current instructions remain available through Read.
- No commits, shared-kit changes or writes to other tool folders. Owned Chrome/host processes closed; ports 9950, 9951 and 8755 checked free; host.html absent.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Reserve Designer handoff

Build only. No commits, deployment or polish round.

#### Source map
src.html begins with the kit starter frame and uses kit:curio and kit:theme-912.
Styles define an actual-pixel responsive map and two Groups habitat scenes.
MAP, SPECIES and L hold the content. evaluate uses four-neighbor flood fill, explicit riverbanks and the bridge gate.
Stable cell and species nodes preserve focus. transact validates spending and farm restoration before changing the plan.
Stress results are fully calculated before their 200 ms playback. Back, Weakest cells and thumbnails cancel playback immediately.
The __tool hook exposes state, calculations, transactions, mode changes and Curio.voice logs for review.

#### Open questions resolved
- Keep the fixed $4,000k budget. No teacher setting added.
- Omit the unverified Colorado SH 9 percentage. The crossing explanation uses no collision statistic.
- Keep purchased working farms as connected protected land, consistent with the supplied checked plans.
- Keep warm-teacher (Sulafat), restyled as a land trust guide. No audio recording was made.

#### Interpretation details
Displayed rows and columns are one-based; supplied reference-plan coordinates are zero-based.
Water activated by a protected bank and the gated river bridge contribute to connected habitat, including bear area.
Stress loss removes protection, with the fixed land-type loss label. It does not spread fire or add simulated neighboring development.
Working farmland keeps its farm edge effect until restored. Crossings always cost $500k.
The Groups poses use deterministic pseudo-independent watch draws, avoiding different outcomes from unseeded randomness.
Motion off uses exactly rounded 20 percent watching and instant stress results, as the spec explicitly requests.

#### Art
Six supplied FLUX portraits retained. Fifteen missing images generated with the built-in imagegen tool during Build.
Full prompts and provenance are in art/prompts.json; originals are in art/raw. Finished WebP files are used by the art bank.
Map, flags, outlines, compass, cracks, budget and future maps are drawn in code.

#### Engine changes wanted
None. Shared engines and scripts were not changed.

#### Review next
Cold review against spec.md and codex-report.md. Source links were supplied by the spec, not rechecked over the network during Build.
Review the six inherited wildlife portraits for biological detail at larger sizes.
All test scripts, frames and numeric evidence are in _scratch/reserve-designer.

#### Build verification notes
Seven standard desktop sizes, all three modes, a hosted 375-pixel iframe, keyboard buying, reload,
four restores plus a fifth refusal, overspending, all reference plans and their stress results were checked.
Seven hundred independently generated rule/cost fixtures matched the browser implementation.
Five farm-menu actions at two-second spacing spoke the how-to once; two distinct all-six transitions spoke twice.
Motion off has no active CSS animation and fixes ten elk to two watchers. Alarm re-press resets the three-second shelter period.
Compact previews keep controls and hints in view; the phone map is first and has cells wider than 26 pixels.
Phone field notes scroll vertically. Groups keeps both compact painted cards and their controls side by side.
The stress thumbnail strip scrolls horizontally inside its own bounds.
Cutout key fringes were reduced with the existing art.py despill option.

#### Spec discrepancy
The stated 200 ms pace is retained. The budget can buy 21 cells, so maximum playback is 4.2 seconds,
rather than the spec's approximate four-second maximum. The 19-cell checked plan remains 3.8 seconds.
No prices or rules were changed to force the smaller duration.


#### Final audit and targeted repairs
One full audit completed in about 32 minutes, with 63 frames and 108 leads. No runtime errors were reported.
The raw audit and individual dispositions are in Scratch. No second full audit was run.
Repairs made during and after the audit were checked only on affected paths and viewports:
shared visible hint node, phone control order, minimum 44 px controls, 10 px status text,
compact model/citation fit, all-cell keyboard traversal, boundary keys and Back focus.
Partial futures distinguish newly broken needs from pre-existing gaps. Cell captions update after every transaction.
Closing a menu restores the current Plan instruction; successful transactions preserve their own result hint.
Curio.voice.playing is a text string. Stale menu speech is stopped before the transaction, so it cannot discard an all-six event.
Quick actions stop stale welcomes. Repeated alarms restart speech and the shelter timer without waiting for the prior welcome.
Menu dismissal on resize is deliberate: focus returns to the originating cell; reopen it to choose an action.
Small bibliography text, exponents and secondary future labels remain smaller than the primary controls and instructions.
The spec supplies no loss word for a purchased highway crossing; the tool uses Closed, with the same single-cell loss rule.
The stated random-search start counts and lower-budget bests cannot be independently reproduced without seeds and witness plans.
None of those search or optimality claims is shown to students.

#### Cold review repairs
Played all modes before reading this handoff or the builder report. Review evidence lives in _scratch/reserve-designer/review.
Redrew the ovenbird against Cornell's identification description: plain olive face, complete eye ring and orange crown stripe.
Redrew the highway, bridge and wildlife overpass as a coherent, more legible roadway set. New prompts and originals are in art.
Source changes: revised plans reset the displayed stress summary; an empty Weakest cells request directs the student to Plan.
Clicking an unbuyable cell dismisses any previous purchase dialog. Selected futures now explain their losses in the live hint.
Lost-cell text hides the crack and crossing symbol to avoid overprinting. The herd slider keeps its focus outline inside its target.
Groups now explicitly asks students to compare herd sizes 1 and 20 as evidence. No new mode, topic, transfer or export feature.
The known 21-cell / 4.2-second spec discrepancy remains; changing the fixed prices or prescribed 200 ms pace is outside this repair.
The elk needs overlay now includes every potential corridor type, including unprotected wetlands and working farms.
The loss-free partial-plan result uses stressNoWeak rather than narrating cracks that do not exist; voice/lines.json matches.
Targeted held-click counts: farmChoice 1/5, crossing 1/5, alarm 5/5, allSix 5/5, stressDone 5/5 and stressNoWeak 5/5 starts.
Read worked with Sound off, and a mode change after Read started its welcome immediately. Rapid actions left no stale queued lines.
The cold audit completed once, in about 32 minutes: 67 frames and 69 leads, with no runtime errors.
Its confirmed compact Stress entry/revision hint clipping was fixed by shortening the untested summary and Run instruction.
One-cell results now say "1 future". Audit dispositions and scoped post-audit frames are in the review Scratch folder.
The scoped revision recheck also caught Weakest cells retaining its pressed style after a purchase invalidated the test.
render now synchronizes that button with weakShown. Both resize-dismissed menus reopened normally with zero disabled actions.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
