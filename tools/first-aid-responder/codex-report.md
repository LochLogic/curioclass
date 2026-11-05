# Codex report: first-aid-responder
## Built
- Local Build only: six school response scenes, CPR rhythm, five-card Field guide, optional timer, saved scene ghosts and a best CPR trace.
- The self-contained bundle is 460,755 bytes (450.0 KiB), under 2 MB. No commits, shared kit edits, audio recording or deployment.
- Scope and both open questions are resolved in handoff.md: six scenes, no overdose addition, Timer On by default.
## Numbers check
- Recomputed all source simulation settings, rail counts, timing constants and contrast ratios in Scratch/recompute.py and numbers.json.
- Slots: 6, 5, 6, 5, 5, 6. Five-second penalty, two-second pause threshold, two-minute round, 110/minute = 545.45 ms and 220 clicks.
- Contrast: mint/panel 10.30:1, mint/section 9.76:1, dark ink/mint 9.14:1, warning/section 9.90:1.
- Spec simulation claims do not fully reproduce. At 30 ms jitter, median scoring minimum after five warm-up intervals is 99.54%, but needle range reaches 122.23.
  At 50 ms minimum is 94.91%, at 80 ms 84.26%. Alternating extreme 30 ms errors can yield 99.10 or 123.60.
  The implementation keeps the actual median; it does not clamp the answer into the band.
- Current Red Cross gauze guidance is more qualified than the supplied scene. See handoff.md and linked sources in notes.md.
## Feel check
- Played all six scenes with held real clicks, including one unsafe choice in each, reversed shared ranks, and a clean ghost replay.
  Best moment: snapping the final step into place and earning an 8.2-second improvement over the earlier gym run.
- Flattest moment 1: the compact guide's Practice it link fell below the preview. Reduced its preview art height and spacing; final link bottom is 401 px at 680x425.
- Flattest moment 2: the 1920-wide CPR equipment looked small inside its instrument bay. Increased torso and dial sizing with viewport height.
- Full two-minute real-time run: 220 compressions, 110/min average, 98.6% in band, longest interval 0.6 s. The saved faint ghost trace reappeared next load.
- Side-by-side frame: Scratch/bar-comparison.png, First Aid Responder beside Beat Lab. Six painted settings and textured equipment hold up well.
  The code training silhouette is intentionally temporary and visibly less rich than the equipment paintings.
## Done when
1. PASS: all six briefings, correct rail counts and step count plus two unsafe cards, verified in 91 functional assertions.
2. PASS: reversed shared-rank pairs, rejected later ranks, five-second penalties, cross/reason and Never tray.
3. PASS: starts on first action, saves and reloads scene stamps, clear removes both records, Timer Off then On never saves that attempt.
4. FAIL on the always-in-band clause; PASS on the practical checks: at 110 with jitter, in-band fraction exceeds 95%; 90 is below target and a 3.5 s interval is counted as a pause.
   The spec's always-in-band requirement is mathematically inconsistent with its prescribed five-interval median.
5. PASS: the actual scheduler generates 220 audio-clock timestamps in 120 seconds; Sound Off stops the scheduler and all scheduled oscillators.
   The live full-round log contains 222 scheduled clicks including metronome warm-up before Start, not a windowed 120-second count.
6. PASS: a 120 ms pointer press counts once. Held-Space repeat events add only one compression; the keyboard-only run reaches and activates the chest.
7. PASS: rail/deck dominate scenes; chest/dial dominate CPR at 1366x768 and 680x425. See final-scene and final-cpr frames.
8. PASS: first card cuts its stale briefing and acts immediately; Stop ends the round; the chest accepts 220 timed inputs with the metronome active.
9. PASS: all modes include the certification and 911 panel footer. Art plate inspected: no people or red cross emblems.
10. PASS: laptop rail/deck/clock fit; phone chest is 169 px, metronome bottom 806.4 px in the 375x812 iframe. Phone scene deck is two columns.
11. PASS: Curio.voice event/how behavior, stale predicates and Read priority; held 2-second pace log is in Scratch/voice-log.json.
## Wave lessons
- Hint/voice: PASS: immediate tool-owned hints, focus-card full text, Read context, valid checks, how-line memory from V.heard, action never waits for speech.
- Focus/layout: PASS: no load focus; card DOM stays in place; focus moves deliberately with preventScroll; hint has reserved space on laptops.
- Sizes: PASS for primary controls; every required size inspected, Read enlarged to 44 px, gauge labels at least 10 px. Phone utility controls remain below the fold.
- No giveaways: PASS: shuffled uniform cards, ranks absent from visible choices, wrong choices cost time and show their reason.
- Honest numbers: PASS: penalty labeled, real median retained, average includes pauses; method described in teacher notes. Rate displayed to one decimal near boundaries.
- Standards/family: PASS: NHES.S7 is practiced through safe response decisions and corrections; no family engine specified.
- Motion off: PASS: standby light stops, card/chest animations stop; clocks and training duration remain unchanged. Zero infinite animations in the calm probe.
- Short choices: PASS: full deck remains visible on laptop and preview; phone uses the prescribed two-column list.
- Resize mid-animation: PASS in the single audit, no exceptions or stuck controls. Later pointer-drag changes have targeted drag coverage.
- Welcome timing: PASS: mode-specific welcomes and first-tap actions use the kit; stale briefings are hushed on the first action.
- Unknown as unknown: PASS: unfilled slots and missing rate display no invented answer; no responder outcomes are simulated beyond the spec.
- One look, one meaning: PASS: target band has words, success has a check, unsafe moves have a cross and Never tray.
- Badge truth: PASS: only accepted steps fill the rail; partial CPR rounds are labeled and cannot win a best.
- Hint changes back: PASS: each mode/scene re-establishes its current instructions immediately.
- No answer by copying: PASS: situation describes the event; it does not name the first required action.
## Audit leads
- One audit completed in about 21 minutes: 47 leads, 82 frames. No tool runtime errors, resize exceptions, stuck controls or infinite calm animations.
- All 47 leads are accounted for below. The full audit was not repeated after these bounded build fixes.
- 17 phone utility-control leads: retained with explanation. Timer, Restart, All scenes and Clear follow the primary two-column scene list.
  Clear also follows CPR results. These secondary controls require phone scrolling; this remains a cold-review layout tradeoff.
- 5 phone hint leads: fixed by moving the existing hint into a reserved header row. Guide hint top 158.4 px, bottom 192.4 px.
- 9 chest/caption overlap leads: intentional caption over the full pad hit area in compact layouts. Caption now has pointer-events:none.
  It does not cover the chest target or intercept taps.
- 3 clipped rail-label leads: intentional two-line shortening. Full action title is now on the actual label; the finish explanation remains available.
- 3 compact finish keep-region leads: fixed. Next bottom is 406 px at 680x425; both finish buttons and the full finish card fit.
- 1 phone-summary keep-region lead: fixed. Completion brings the summary into view, measured top 677.4 px, bottom 811.5 px.
- 6 scene-entry welcome leads: intended kit behavior. Opening a scene skips the stale picker welcome and speaks that scene's briefing and order instruction.
- 3 rapid same-mode welcome cuts: fixed by preserving an already open mode. Three held double-tap checks, 0.7 s apart, finished with zero welcome cuts.
- Additional visual/functional fixes: pointer-capture dragging passes correct and wrong real drags; focused hint clears the clock by 5 px;
  gauge labels measure 10.42 px in preview and 11.16 px at 760 wide; unknown rate has no needle until measurable.
- The test HTTP server logged a connection reset during shutdown. This is a test-host teardown message, not a tool exception.
## Frames looked at
- Beat Lab and Snowy Mail Route reference frames, 1366x768, bundled only in Scratch.
- All seven desktop/preview sizes in each mode, plus 375x812 hosted in Chrome; calm, grayscale and keyboard frames.
- Six completed student scenes, compact completion and CPR partial summary, real-time two-minute summary, ghost replay, blocked-storage run.
- New equipment and all six retained backgrounds in Scratch/art-plate.png. All generated screenshot contact sheets were inspected.
- All 82 audit PNGs inspected through the 21 sheets in Scratch/audit-sheets; targeted build-fixes, last, phone and footer-probe PNGs inspected individually.
## Art made
- Two new equipment images from the built-in image tool, six retained painted school backgrounds, eight placed paintings total.
- Finished art: 238,670 bytes (233.1 KiB). Bundle: 450.0 KiB. Prompts/provenance in art/prompts.json; new raw originals in art/raw/.
- No redraws. Both new cutouts were rekeyed with holes and despill to remove magenta edging.
## Art still to paint
- fa-manikin, owner-reviewed body-form image. The asset is marked people: true and its token is reserved; a faceless code training silhouette is used.
- Retained field painting has a school lawn and cooler rather than the specified blocking sled/shade tent. Retained kitchen has no pan.
## Engine changes wanted
None.
## Left open
- The full audit predates the final targeted fixes. Its original leads and the later evidence are preserved for cold review.
- Current Red Cross add-gauze qualification needs spec-owner reconciliation before release. Source wording was preserved.
- AHA's full 2024 first aid page and the supplied CDC heat URL were not retrievable. Red Cross heat guidance and the other named pages were checked.
- No recordings: firm-captain is specified in voice/lines.json; narration currently uses the kit's browser-voice fallback.
- All owned Chrome/server processes closed; no listeners on 8795 or 9990 through 9997. host.html is absent.
