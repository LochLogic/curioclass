# Polish: flipbook-studio (Codex fix, round 1)

Evidence paths below are relative to `_scratch/flipbook-studio/`. Every should-fix was reproduced before editing at 1366x768 with `scripts/drive.py`. Before frames: `fix-before/s01-*` through `s09-*`. Accepted polish used after frames and measurements. The final report is written only after checking, honoring the user's stop trigger; this draft was maintained in Scratch during work.

## Blocker

None in refine.md.

## Should fix

1. FIXED. Playback and student selection now have separate indexes. The baseline reproduction used Real bounce with the same twelve x1 holds; the reviewer used Even bounce. Both use the same timing controls and playback path. Three live plus taps changed only selected drawing 5 from x1 to x4, with a stable named readout; before they changed drawings 4, 6 and 11. `fix-before/s01-selected-live.png`, `fix-after/s01-selected-live.png`. Additional live minus and Hold the key tests changed only drawing 7 and drawing 5 respectively: `fix-functional/check-selection-minus.png`, `check-selection-key.png` and matching JSON.
2. FIXED. Why and the 5-minute start distinguish film's 24 fps twos from the starter's 12 fps twos. The preset hint explicitly says 6 new drawings per second at 12, and names 24 as the next action. Starters remain 12 fps. `fix-before/s02-twos.png`, `fix-after/s02-twos.png`, `fix-after/s07-planning.png`, `fix-voice/read-twos.png`; 24 displayed duration combinations checked in `check-numbers-sweep.json`.
3. FIXED. Warning speech is triggered only on transition into failed storage, and rearms after a successful save. Baseline: 5 spoken starts for 5 failed saves. After: 1 for the same five-copy sequence, with the persistent warning still visible. A separate five-action run, success, then new failure produced exactly 2 warning starts, one per failure run: `fix-target/check-storage-recovery.png`, `check-storage-recovery.json`. No repeated warning displaced onion guidance in the after-copy run.
4. FIXED. Print now awaits its narration before opening print, and Sound off prints without a speech delay. Baseline `printed` was dropped by hush; the real headless print path now logs one spoken `printed` and `printing:false`: `fix-last/print-real.png`, `print-real.json`. The hint is the same sentence. A simulated afterprint-only approach was rejected because real headless Chrome did not emit afterprint. Physical printer output was not tested.
5. FIXED. Bounce starters use the exact starterBounce sentence for both hint and speech, preserving the comparison instruction. `fix-before/s05-starter.png`, `fix-after/s05-starter.png`; the held-click log in `before-starter.json` now contains the matching after-state sentence. The file name predates the recheck; the baseline mismatch is preserved in the before frame and progress notes.
6. FIXED. The bowling card and notes now begin with On twos, then prescribe top=1 and floor=4. Applying it gave holds `[1,2,2,4,2,2,1,2,2,4,2,2]`, 26 frames, and identical artwork. `fix-before/s06-bowling.png`, `fix-after/s06-bowling.png`, `fix-functional/check-bowling.png`, `check-bowling.json`.
7. FIXED. Why defines key drawings and the new optional card plans start, top and landing before in-betweens; the same activity and Richard Williams source are in notes. `fix-before/s07-planning.png`, `fix-after/s07-planning.png`, `fix-target/s07-plan-card.png`. Source: Richard Williams, The Animator's Survival Kit (2001), "Keys, extremes and breakdowns", as named in the Refine item. No additional scored planning gate was added.
8. FIXED. Playing hints now follow Draw, Time and Flip. Draw says Tap Stop to draw and uses a not-allowed cursor. Time names hold handles and presets. `fix-before/s08-playing-draw.png`, `s08-playing-time.png`, their matching `fix-after/` frames and computed cursor `not-allowed`.
9. FIXED. Empty-state text uses #6b6258. Contrast rose from 3.994:1 to 5.543:1 on #fbf6ea, independently computed in `fix-numbers.json`. `fix-before/s09-contrast.png`, `fix-after/s09-contrast.png`.

## Polish accepted

10. FIXED. Flip uses a 55 px strip with 44 px numbered buttons, selected border and separate playing underline. At 1366x768 the page is 650.4 by 487.8 px, versus Draw's 634.5 by 475.9. `fix-target/p10-flip.png`, `p10-flip.json`. All three modes passed at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x760 and the 375x812 iframe. Page, strip, Play and hint are in bounds, with document scroll [0,0], in all 25 measured states: `fix-validation.json`, `fix-sizes/`, `fix-phone/`. Frames were inspected individually or on contact sheets.
11. FIXED. Empty Time and Flip now direct the student to Draw or Starters; their invalid Play welcomes are suppressed. `fix-polish/p11-empty-time.png`, `p11-empty-flip.png` and matching JSON.
12. FIXED. Blink's four centers are all `[480,350]`; the chart draws one ringed dot and shows the shape-change explanation. `fix-polish/p12-blink.png`, `p12-blink.json`.
13. FIXED. Ease the ends explicitly describes the first and last drawings and asks for manual holds at each bounce top. Holds remain `[3,2,1,1,1,1,1,1,1,1,2,3]`. `fix-polish/p13-ease.png`, `p13-ease.json`.
14. FIXED. At 1920x1080, both readout and hint compute to 16.128 px. `fix-polish/p14-large.png`, `p14-large.json`.
15. FIXED. Compact Undo is beside Tools, with a 44 px height at both 680x425 and 800x500. The 680 undo action removed the newly added stroke and exposed one Redo step. `fix-polish/p15-undo-680.png`, `p15-undo-800.png`, `fix-functional/check-undo-visible.png` and matching JSON.
16. FIXED. New Blue pencil is indigo #3b3da8, 8.050:1 on the page. Previous-page onion remains blue. Chart dots remain vermilion and have a light outline ring. Old blue strokes still load unchanged. `fix-polish/p16-blue-onion.png`, `p16-red-chart.png`, `fix-numbers.json`.
17. FIXED. Artwork edits repaint one thumbnail; holds and fps repaint none. Reorders reuse existing canvases. Input and legacy points round to 0.1 drawing unit. A 48-page, 400-stroke-per-page legacy book loaded in full and saved from 4,350,113 to 2,078,073 characters. Ten steady renders measured 0.1-0.7 ms; reorder 12.4 ms; an artwork change cleared only `thumb-2`. A real hold drag with 18 samples now saves once on release. `heavy-seed.json`, `heavy-measure.json`, `drag-save.json`, `fix-target/heavy-measure.png`, `fix-last/drag-save.png`. Measurements are this machine, not a universal speed guarantee.
18. FIXED. Good to know now describes the calm Blink opener and the 1 to 6 editor directly, with no reference to "the spec". Verified in notes.md.
19. FIXED. Support at home now asks families to drop and bounce a ball, observe the hang at the top and rush at the floor, then compare with Real bounce. Verified in notes.md.
20. FIXED. Why says "half the drawings". `fix-after/s07-planning.png`.
21. FIXED. A missed erase leaves undo length 0 rather than adding an empty step. `fix-polish/p21-missed-erase.png`, `p21-missed-erase.json`. A sampled real erase then Undo gave removed=0 strokes, undo=1, restored=1 stroke (`erase-hit-undo.json`, `fix-final-targets/erase-hit-undo.png`).
22. FIXED. A real tap in the second track cell now selects hold 2; handle dragging still uses its existing rounding. `fix-last/p22-track-cell.png`, `p22-track-cell.json`. Earlier synthetic drags hit the handle or sent a move after the tap; those intermediate checks are retained and are not the passing evidence.
23. FIXED. The canvas label now says "Arrow keys Left and Right step pages" without promising canvas focus. Keyboard Step twice already reached drawing 3 with focus retained and no document scroll (`keyboard-flip.json`). Two actual ArrowRight keys also reached drawing 3; the returned label matches the revised wording (`arrows-final.json`, `fix-finish/arrows-final.png`).

## Settled calls

- Applied: retained the permitted first-tap welcome behavior for page operations, modal keep-region behavior, horizontal scrolling film strip and decimal seconds wording.
- Applied: used the timing-only bowling recipe, preserved 12 fps starters, moved Blue pencil rather than the accent chart.
- Retained the 12-line voice manifest, Ping-pong's no-double-end implementation, clock, held-frame print construction, Motion off and Read. `fix-numbers.json` confirms all 12 manifest lines equal the source table. A 120-frame/10-loop clock check at 24 fps took 5022.7 ms, error 0.545 frame (`check-24-clock.json`); no clock code changed.
- Left the spec's two open questions and Not taken items alone.

## Cheats tried

- Repeated live plus taps: only the selected drawing changed. Two additional patterns, live minus after On twos and live Hold the key, also changed only the selected drawing.
- Swept all 6 editable hold values against all 4 frame rates in deliberately scrambled hold order: all 24 frame/seconds totals agreed with independent arithmetic. No score, meter award, quiz, correctness badge or completion gate exists (`awards:0`). Presets are creative timing controls, not evidence of a learned skill.
- Applied the bowling recipe without redrawing: it changes timing only, with no automatic pass claim. Planning remains an optional making activity, not a gate that can be passed by clicking every choice.
- Repeated failed saves with both page copies and hold increments, then recovered and failed again: warnings speak once per continuous failure; visible warning persists until recovery.
- Track tap and hold drag: second cell gives 2; drag reaches 6 and saves once. Held prints still construct 24 cards on 3 sheets from 12 drawings on twos (`check-print-held.json`).

## Voice walk

Held clicks were 0.12 s with a 2 s pace, Sound on; Chrome was muted as required. Logs record spoken starts, not a human listening session. No recordings were made or regenerated.

- Main walk in `voice-main.json`: welcomeDraw, onionHow, welcomeTime, spacingHow, holdChanged, welcomeFlip, printed, each once. The final drawn-book walk (`voice-main-drawn.json`) started onionHow, welcomeTime, holdChanged, welcomeFlip and printed once each, in that order. The first drawing made welcomeDraw stale, as permitted. At the 2 s pace, later actions cut several long how lines; printed completed without a cut. Only one drawing had strokes, so spacingHow correctly had no three-dot trigger on this path.
- Starter comparison walk: starterBounce once, with exactly matching hint (`fix-after/s05-starter.png`).
- Storage walk: tooBig once across five failed actions, then once more after successful recovery and a fresh failure (`check-storage-recovery.json`).
- Side walk in `voice-side.json`: starterBlink, welcomeTime, welcomeDraw, then Read speaks eraserHow. The fast Why entry drops stale spacing speech; Read correctly replaces a pending eraser line. These unrelated cuts are retained honestly, not presented as full uninterrupted clips.
- Final real print recheck: printed starts once before print and finishes without a hush cut (`print-real.json`).

## Visual and play regression

Best moment: changing a live hold changes the feel while the same ball drawings keep moving. The two flat moments addressed were Flip repeating Draw's layout and the bowling card leading into a minimum-hold dead end; Flip now has the slim progress row and the card has an achievable first move. The painted table, paper grain, onion guides and responsive hold bars are retained. Compared the final desk with the existing bar-tool bundles at the same 1366x768 size: `fix-last/print-real.png`, `bar-beat-lab.png`, `bar-snowy-mail-route.png` and `fix-last-sheet-0.png`. Their existing bundles were read without writing to either tool. The desk remains detailed and does not look plainer. Grayscale, Motion off, keyboard Step and direct arrows were inspected in `fix-finish/` and `fix-voice/`.

Final bundle: 232,975 bytes, no external load URLs, no source em dashes. `fix-validation.json` records the SHA-256. Targeted drive runs had no product console errors. The generated phone host initially requested a missing favicon; a data favicon in that temporary test host removed the 404 in `fix-phone-clean/`. The host was removed and its server closed.

## Engine changes wanted

None. All fixes are tool-local.

## Audit

Completed once, last, within the 40 minute limit, using Chrome 9911 and host 8715. Exit code 0. Report: `fix-audit/audit.md`. The audit's copied bundle and the delivered bundle have the same SHA-256. No product console errors, focus failures or resize exceptions were reported. Motion off passed. Nine controls passed five held clicks, and eleven passed the quick-tap check.

All 32 leads are accounted for:

- Eight size leads, "1 seconds": the visible text is "0.1 seconds". This is the explicitly settled decimal-parsing false positive. The default frame and readout measurements confirm it.
- Four sideways-strip leads: bounce-time at 680x425 and 1366x768, delete-pauses-book, and page-limit. These are the specified horizontally scrolling film strip. Selected drawings and main controls stay in view; do not flatten the strip or remove drawings to silence this flag.
- Ten modal keep-region leads: Starters and Why each cover #page, #play, #readout and #hint, plus a duplicate #page entry quoting the new chart caption. These are the settled intentional modal overlays, also visible in our own `fix-before/s07-planning.png` and `fix-after/s07-planning.png`. The extra caption wording does not change the cause. No desk control is meant to be used through a modal.
- Ten first-tap welcome leads: #m-time and #m-flip on a blank book intentionally suppress an invitation to Play nothing (item 11); #eraser speaks its own eraserHow instead of welcomeDraw, confirmed in the audit's spoken column and repeat check; #new-page, #copy-page, #delete-page and #clear-page follow the explicitly settled stale-welcome rule; #play acts at once and cuts welcome; #starters and #new-book open dialogs and hush desk guidance. In each case, the fitting hint and Read remain available. BASELINE rule 16 permits the skip or cut. These are not missing necessary instructions.

No new unresolved product lead was found. Resize stress finished cleanly after the repeat checks. The audit's Chrome and host were closed on normal completion. It was not rerun.

## Left open

- No changes were made to refine.md or refine/, and no git commits were made. Writes are confined to tools/flipbook-studio/ and _scratch/flipbook-studio/.
- Initial brief reads used the command tool's yield setting before the terminating subprocess wrapper was added. All build, drive, diagnostic and audit commands thereafter have explicit terminating limits: 2 minutes bundle, 5 minutes drive batch, 40 minutes audit; short reads 15-30 seconds.
- One Chrome connection reset was retried as smaller batches, which completed. Test corrections and intermediate failures remain in Scratch. The initial after-test reused three before-named JSON paths; baseline PNGs were preserved, and observed before counts were recorded in report-progress.md.
- Existing browser speech fallback remains; no recorded clips exist. Physical printed paper was not checked.
- Existing spec conflicts remain: Blink's explicit eight-frame opening hold and the squashed floor center at y=632 so its bottom meets y=660. No new decision or feature was inferred from unanswered questions.
