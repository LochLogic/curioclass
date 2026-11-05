# Reserve Designer handoff

Build only. No commits, deployment or polish round.

## Source map
src.html begins with the kit starter frame and uses kit:curio and kit:theme-912.
Styles define an actual-pixel responsive map and two Groups habitat scenes.
MAP, SPECIES and L hold the content. evaluate uses four-neighbor flood fill, explicit riverbanks and the bridge gate.
Stable cell and species nodes preserve focus. transact validates spending and farm restoration before changing the plan.
Stress results are fully calculated before their 200 ms playback. Back, Weakest cells and thumbnails cancel playback immediately.
The __tool hook exposes state, calculations, transactions, mode changes and Curio.voice logs for review.

## Open questions resolved
- Keep the fixed $4,000k budget. No teacher setting added.
- Omit the unverified Colorado SH 9 percentage. The crossing explanation uses no collision statistic.
- Keep purchased working farms as connected protected land, consistent with the supplied checked plans.
- Keep warm-teacher (Sulafat), restyled as a land trust guide. No audio recording was made.

## Interpretation details
Displayed rows and columns are one-based; supplied reference-plan coordinates are zero-based.
Water activated by a protected bank and the gated river bridge contribute to connected habitat, including bear area.
Stress loss removes protection, with the fixed land-type loss label. It does not spread fire or add simulated neighboring development.
Working farmland keeps its farm edge effect until restored. Crossings always cost $500k.
The Groups poses use deterministic pseudo-independent watch draws, avoiding different outcomes from unseeded randomness.
Motion off uses exactly rounded 20 percent watching and instant stress results, as the spec explicitly requests.

## Art
Six supplied FLUX portraits retained. Fifteen missing images generated with the built-in imagegen tool during Build.
Full prompts and provenance are in art/prompts.json; originals are in art/raw. Finished WebP files are used by the art bank.
Map, flags, outlines, compass, cracks, budget and future maps are drawn in code.

## Engine changes wanted
None. Shared engines and scripts were not changed.

## Review next
Cold review against spec.md and codex-report.md. Source links were supplied by the spec, not rechecked over the network during Build.
Review the six inherited wildlife portraits for biological detail at larger sizes.
All test scripts, frames and numeric evidence are in _scratch/reserve-designer.

## Build verification notes
Seven standard desktop sizes, all three modes, a hosted 375-pixel iframe, keyboard buying, reload,
four restores plus a fifth refusal, overspending, all reference plans and their stress results were checked.
Seven hundred independently generated rule/cost fixtures matched the browser implementation.
Five farm-menu actions at two-second spacing spoke the how-to once; two distinct all-six transitions spoke twice.
Motion off has no active CSS animation and fixes ten elk to two watchers. Alarm re-press resets the three-second shelter period.
Compact previews keep controls and hints in view; the phone map is first and has cells wider than 26 pixels.
Phone field notes scroll vertically. Groups keeps both compact painted cards and their controls side by side.
The stress thumbnail strip scrolls horizontally inside its own bounds.
Cutout key fringes were reduced with the existing art.py despill option.

## Spec discrepancy
The stated 200 ms pace is retained. The budget can buy 21 cells, so maximum playback is 4.2 seconds,
rather than the spec's approximate four-second maximum. The 19-cell checked plan remains 3.8 seconds.
No prices or rules were changed to force the smaller duration.


## Final audit and targeted repairs
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

## Cold review repairs
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
