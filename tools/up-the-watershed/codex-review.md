# Codex review: up-the-watershed

## Played

Played cold as a Grade 12 solo student before reading the builder's report, handoff or source: all three cases, wrong accusations, evidence selection, logbook and Fix-it. The dry/storm contrast is strong; collecting samples initially felt flat. Later checks covered three saved alternatives, explanations and reloads, plus projector and narrow layouts.

## Findings fixed

- **blocker, general, Claim/share():** the downstream treatment plant was credited with sediment at upstream S7. Its share is now zero there; dry background is correctly 40.7 percent. Confirmed in the whole-creek frame and independent calculations.
- **blocker, general, Fix-it:** leaving during the calculation could replace Cases instructions with a late cleanup result. Mode exit now cancels the pending test. Mode-exit and toggle-interruption checks retain the correct hint and empty gauges.
- **should fix, general, Claim:** feedback carried between case files and survived evidence edits. Verdicts are isolated by case and invalidated when evidence changes.
- **should fix, general, Claim:** the 20 percent criterion was buried in notes. The initial instruction now states it before submission and fits the preview.
- **should fix, general, compact Fix-it:** effects and who-pays details depended on hover or accessibility descriptions. The visible Fix details control exposes every intervention to touch and keyboard users.
- **should fix, general, phone gauges:** hidden row labels made dry, storm and change values ambiguous. Labels remain visible; storm closure says Closed with its dirty-water explanation.
- **should fix, general, phone Sample:** Make claim was partly below the fold after kits ran out. The compact header preserves the full map and puts Make claim's bottom at 804 px in the 812 px iframe.
- **should fix, general, map:** dry/storm flags touched circles or source labels. Explicit gaps and compact label positions now separate all 22 flags at every checked size.
- **should fix, general, voice:** exhaustion and over-budget feedback could wait behind obsolete instructions. Kit warnings and budget-threshold events now take priority and name enabled next actions.
- **should fix, general, empty panels:** empty evidence referred directly to hidden sampling controls; an empty over-budget portfolio suggested disabled testing. Instructions now name Close, the needed mode and the reachable action.
- **should fix, general, dialogs:** native modal behavior made the header Read button inert. Each dialog now has a working Read control, verified with held clicks and Sound off.
- **should fix, general, Logbook:** No flow and Not modeled acquired measurement units. Their absence is now stated plainly.
- **should fix, general, field photos:** cover cropping removed useful scene context, including cattle's feet. Whole photographs now fit within a viewport-based height cap.
- **polish, general, sampling:** added a shaded vial-fill beat alongside the ripple and immediate results. A dry Pipe leaves the vial empty; Motion off removes movement.
- **polish, general, art:** the cattle miniature read as terrain at 40 px. Redrew it with recognizable animals, retaining the painted field-guide style.

## Findings left

No identified blocker or should-fix remains.

- **nit, general, specified precision:** E alone produces exactly 0.0475 mg/L dry phosphorus. The UI displays 0.047, matching the spec's binary-rounded example. Kept the requested display; raw goal checks are unaffected.

## Flattest moment left

Once all three fixed datasets are known, returning to the same samples has limited replay value. The competing cleanup portfolios remain the stronger ending. Added no new cases or replay system beyond the spec.

## Graphics

Checked all 22 assets, their map/card placements, all seven full field-photo views and the relevant final sizes. Redrew one asset with built-in OpenAI image generation: `art/uw-i-cattle.webp`; full prompt and provenance are in `art/prompts.json`. Processed through `art.py --rekey uw-i-cattle`. No missing art or people images. Preserved the case paintings, miniature set, textures and flowing map. Compared the finish with the isolated Snowy Mail Route and Beat Lab references.

Art: 478,038 bytes. Final offline bundle: **763,460 bytes (745.6 KiB)**. Source has 1,620 lines, none over 160 characters, and no em dashes.

## Audit

Ran the full audit **once**, on Chrome 9961 with host 8765. It completed in **2,302 seconds (38 minutes 22 seconds)** with **285 leads**. All have dispositions in `_scratch/up-the-watershed/review-audit-dispositions.csv`; inspected all 67 audit frames.

Fixed 19 flag-spacing leads, one phone next-action lead and two stale-instruction leads. The other 263 are explained overlays, auxiliary phone footer scrolling, the deliberately locked Fix-it mode, modal-return behavior, an empty restart and a second tap landing on the newly opened map. Scoped checks confirm that closing notes restores a complete welcome and the old Open case coordinates open the Geese photo, appropriately hushing the prior instruction.

Re-shot affected states only. Final flag probes show 22 flags and zero circle/label intersections at every STANDARDS size. Phone controls, dialog Read, complete photos, three-plan persistence and session-only Why notes pass. No browser console errors, warnings or exceptions in the final batches. The full audit predates these final repairs and was not repeated.

Independent Python computations agree with the browser on all modeled samples and all 512 portfolios: 4,692 comparisons. Exactly two portfolios within $3 million meet all goals, both using the advisory. Advisory, lake-failing and $4.1 million over-budget outcomes were checked. Keyboard-only input solved Muddy creek; grayscale and Motion off were inspected. Contrast: primary button text 6.68:1; main text 14.70:1.

| Line | Kind | Expected | Observed |
|---|---|---|---|
| Sample / Claim welcome | once | 1 each in five taps | 1 each |
| Solved | event | 5 | 5, queue drained |
| Last kit / Out of kits | event | each occurrence | 2 each at 2 s pace; 1 each in final rapid cycle |
| Over budget | event | 2 crossings | 2 |

All 20 registered lines match `voice/lines.json`. Evidence, counts, frame manifests and hashes are in Scratch. All started Chrome and host processes are closed; `host.html` is removed. No commits or shared-kit changes.

## Left open

- Narration remains browser fallback; the specified bank timbre has no recordings. No audio was recorded, as required.
- Classroom engagement and the intended lesson duration were not measured.
- The initial instant rules-read command lacked an explicit deadline. Subsequent shell commands and all substantive checks used deadlines.
