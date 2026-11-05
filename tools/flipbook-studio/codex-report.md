# Codex report: flipbook-studio

## Built

Built the self-contained Draw, Time and Flip studio from the kit starter, with editable vector starters, onion skins, whole-stroke erasing, per-page Undo/Redo, live holds and fps, clock-based playback, device saving and timed paper printing. Draft stage is built. No commits or separate polish round.

Open questions resolved: omit GIF; retain Print pages as the explicitly described paper flipbook craft. Preserve Blink's specified eight-frame opening hold as an exception to the six-frame editor limit. Full reasoning is in handoff.md.

## Numbers check

Independent computation: _scratch/flipbook-studio/numbers.json. All published contrast ratios match: 4.91, 5.30, 13.88, 5.54, 9.79, 4.46 and 3.16. Legend text uses the muted text color with full-strength colored dots.

Readouts: ones 12 frames / 1.0 s; twos 24 / 2.0 s; Blink 11 / 0.9 s; nervous Blink 5 / 0.4 s; Ease the ends 18 / 1.5 s. Standard maximum: 288 frames, 48.0 s at 6 fps, 12.0 s at 24 fps, 36 print sheets. Rightmost ball geometry reaches x=890.

Two spec conflicts remain explicit: Blink's 8-frame hold exceeds the general limit; squashed floor drawings require center y=632 for radius 28 and bottom y=660, whereas the unsquashed formula gives 620. The spec was left untouched.

## Feel check

Best moment: dragging a hold during playback changes the ball's feel without changing a stroke. Copying a page and drawing over its ghost also gives an immediate, tangible result.

Flattest moment 1: compact controls could crowd the paper. Secondary controls now open in a tools drawer while the page, strip and Play remain visible. Nested dialogs return focus to Tools.

Flattest moment 2: many copied drawings put chart numbers on top of one another. Collision-free labels and light leaders now retain all 48 numbers, even at 680x425. A hold drag also locks automatic strip following until release.

Played the draw/copy/erase/revise/time/flip sequence with real mouse input and touch drawing. Compared the studio beside Beat Lab in _scratch/flipbook-studio/bar-comparison.png. Both bar tools were bundled into scratch and opened before implementation. The painted table, paper stack, curl and material detail hold up beside the reference.

## Done when

1. PASS: real mouse and CDP touch strokes; whole-stroke erasing; Undo restores and Redo removes. See mouse-results.json, eraser-results.json and touch-results.json.
2. PASS: before/after ghosts are blue/green under current strokes in Draw; absent in Time, Flip and the print DOM. Keyboard and mode frames inspected.
3. PASS: all three required readouts independently recomputed and asserted. Blink retains its explicit eight-frame starter exception.
4. FAIL for the literal floor-center formula: Real bounce drawings 3 and 9 use y=632 to satisfy the specified squash and floor contact. Real probes 0,1,3,11 and Even probes 0,1,3,11 were checked; all other tested coordinates and the bunched/even chart behavior pass.
5. PASS: hold edits leave stroke JSON unchanged. At 24 fps, 124 frames advanced over 10.33 loops against 124.8144 expected, an error of 0.8144 frame.
6. PASS: every required desktop/preview size was viewed in all three modes. Paper stays within the measured painted glass. Time retains both chart/page and hold strip.
7. PASS: real held-handle dragging while playing updates timing and preserves artwork; Stop is immediate. A 24-fps compact drag had zero strip movement during the gesture.
8. PASS: Blink prints 11 numbered frames over 8+3 cards, with cut and staple marks. Standard maximum produces 36 sheets. Paths are black, with no painted texture or ghosts.
9. PASS: touch artwork survived reload; confirmed New book saved one empty page; full-storage failure and recovery were asserted.
10. PASS: page, strip, selected thumbnail and Play fit all required sizes. Independent 375-pixel host checks passed with no horizontal overflow; middle selection stayed visible through Time, Draw and Flip.
11. PASS: one onionHow start across five held Copy page actions. Three timing changes at a two-second pace each started holdChanged; newer changes and Stop cut stale speech. Read and mode-switch logs show no delayed queue hang.

The functional suite passed 41/41 assertions. Supplementary real-input, storage, printing, focus, voice, limit and responsive checks are retained in scratch.

## Wave lessons

- Hint and voice: PASS. Hints update synchronously and name controls. Read speaks the current hint; how-to selection uses V.heard and the kit queue.
- Focus and layout: PASS. Stable controls retain focus; nested modal return is verified. Hint space is reserved. Sound now has a fixed width and caused zero header shift.
- Sizes and targets: PASS. All STANDARDS sizes, 375 host, and 44-pixel controls checked; no clipping found in inspected final frames.
- No giveaways: PASS, not an assessment. There are no hidden answers, scores or solution meters.
- Honest numbers: PASS. Computed readouts, explicit Blink exception, and truthful feedback when holds or fps already match.
- Standards: PASS. Solo students develop artwork, refine timing for intent, and use animation production tools. No family engine applies.
- Motion off: PASS. Audit found no infinite animation; playback continued with the same clock and no curl lift.
- Short choices: PASS. Four starters fit the compact dialog. The sideways frame strip is the explicitly specified editable book sequence.
- Resize mid-animation: PASS. Completed audit stress checks found no exceptions or controls left disabled.
- First-tap welcome: PASS with the spec's stale rules. Page actions and Play deliberately invalidate the Draw welcome; there is no late welcomeAfter queue.
- Unknown as unknown: PASS, not a diagnostic activity; no concealed states are represented as known.
- One look, one meaning: PASS. Ghosts have labeled colors; holds also have numbers; gray label leaders differ from the vermilion motion path.
- Truthful badges: PASS. Counts reflect stored holds and fps; unchanged presets no longer claim new timing.
- Hints change back: PASS. Mode entry, Stop and limits restore an appropriate next action.
- No word-matching answers: PASS, an open studio with no answer cards.

## Audit leads

Ran the audit once, on Chrome 9991 with host 8795. It completed within 40 minutes: _scratch/flipbook-studio/audit/audit.md. No console exceptions, focus losses or resize failures were reported. Its 35 leads are answered below; the frozen audit precedes the targeted fixes.

- Four tiny-text leads: FIXED. Hidden footer branding now uses a hidden span, with visible text at 10 px. Final compact frame and computed-style check pass.
- Seven “1 seconds” leads: false positives. The regex matches the fractional suffix of “0.1 seconds”; the measurement and plural are correct.
- Two phone-context/hint leads: audit infrastructure could not locate its iframe context. Independent drive.py host runs at the same assigned port verified the actual 375-pixel document, visible hint, controls and zero runtime errors.
- Three sideways-strip leads: intentional, required book timeline scrolling, in bounce-time and page-limit. Selection is brought into view after mode changes and resizing.
- Ten covered keep-region leads: intentional native modal coverage in starter-library and timing-help. Dialog choices and Close remain usable; the background book is deliberately inert.
- Five skipped-welcome leads: intentional stale behavior after New page, Copy page, Delete page, Clear page or Play. This follows the spec; the current hint and Read remain available.
- One minimum-hold dead-control lead: FIXED with immediate limit feedback. The held-click check confirms hold 1 and an actionable hint.
- Three same-mode quick-tap cuts: FIXED by making mode re-selection preserve the current narration. The two-tap recheck logged one welcome start and zero cuts.

Also fixed the Sound label's header shift, bounded print speech to the print operation, and verified unchanged presets/fps without changing the book. Only affected cases were re-shot; the full size matrix and audit were not rerun.

## Frames looked at

Scratch folders inspected: bar-frames, first-frames, test-frames, interaction-frames, voice-recheck-frames, final-frames, extreme-frames, targeted-frames, post-frames and phone-frames; also touch.png and bar-comparison.png.

Viewed all 21 full-size matrix frames, final five phone frames, grayscale, Motion off, starter/help dialogs, 48-page extremes, the print preview and all 61 audit size/state/calm frames through six contact sheets. Both finished WebP paintings were inspected at final size.

## Art made

Two original generated paintings: fb-desk and fb-paper. Art totals 98,480 bytes, about 98.5 KB; recorded voice is 0 KB. Final bundle is 219,983 bytes, about 220.0 KB against the 2,000 KB goal. Neither image needed redrawing. No painted people.

## Art still to paint

None. The schematic Blink face and all editable drawings are intentionally vector strokes, as the spec requires.

## Engine changes wanted

None. Shared kit, scripts and documentation were not modified.

## Left open

- The two numerical spec conflicts above need the cold reviewer's attention. Floor contact was prioritized; Blink's explicit starter timing was preserved.
- Narration uses browser speech fallback. The friendly-dad / Achird manifest is ready; no audio was recorded, as instructed.
- Print layout was checked in the browser, not on a physical printer.
- The audit's 375-pixel context detector remains unverified; separate actual iframe checks passed.
- Initial read-only brief/memory commands completed without hard deadlines. Subsequent shell commands used explicit bounded runners.
- The host cleanup helper initially left three processes running. Their exact flipbook-studio host command lines were verified and those processes were closed. Final ports 8795, 9990, 9991 and 9992 are closed; host.html is removed. The scratch helper now terminates and waits on its server handle.
- Report written last to honor the user's stop trigger. No further round follows this file.

