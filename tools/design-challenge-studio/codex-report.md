# Codex report: design-challenge-studio

## Built

Four open stations for three Grade 12 engineering challenges. Two browser simulations, an editable tree and sort, four saved designs, weighted scaling, live Flip finder and a session-only Why box. Own challenge persists locally and has a clear control.
Kit starter, Curio.voice and the 9-12 theme. No network requests, recordings, commits, deployment or polish round. Authored project files stayed in the two authorized folders. Generated images were copied from the image tool's default delivery location.

## Numbers check

Independent Python: all 256 room sets; all 1,296 four-criterion weight combinations. Browser room values match Python exactly. Worked totals 60.0, 96.1, 95.5, 39.9 and all three specified flips pass.
Insulation rounds to 37.10, versus 37.09 in one spec line. The named art list contains twenty assets, despite saying twenty-one. Spec left unchanged.
0.81 pounds per kWh converts to 0.3674098 kilograms, consistent with rounded 0.367. 6,500 feet converts to 1,981.2 meters, consistent with about 2,000 meters. Social statistics were retained from the supplied spec, not re-derived from source datasets.
Contrast: brand/panel 11.61:1; brand/section 11.00:1; brand-ink/brand 12.18:1; text/card 13.12:1; muted/card 7.25:1.

## Feel check

Best moment: lower the hours weight from three to two and Design 3 takes the top tag, while Flip finder immediately reveals the changed priorities.
Flat moment 1: cause placement originally just moved text. Added a short snap animation, a matching tone and illuminated intervention chips, without grading student-authored cards.
Flat moment 2: water protection initially changed abruptly and crowded the last bar. Kept stable bar elements for animated fills, added painted ordered steps, and corrected the space budget.
Played the student path through tree placement and checking, sorting, testing options, saving designs and flipping the winner. Later designs require a different trade-off, rather than repeat a fixed quiz.
Compared the 1366 prototype with Beat Lab side by side in S:/CurioClass-codex/_scratch/design-challenge-studio/bar-comparison.jpg. The studio's large painted context and dimensional intervention tiles meet the visual bar while retaining an evidence-focused instrument layout. Snowy Mail Route was also bundled in Scratch and opened as the feedback reference.

## Done when

1. PASS: baseline 38.6408 degrees, 7.00 hours, 7.30 kWh.
2. PASS: AC 26.5394 degrees, zero hours, 31.0103 kWh. Saved AC row is excluded with named electricity and budget failures.
3. PASS: specified set costs $3,900; 33.8225 indoor, 31.3225 feels-like, 3.55 hours, 6.88 kWh. Trees give 3.50 hours and not ready.
4. PASS: fans 8.98 kWh; fans with lights off 6.88 kWh.
5. PASS: cloudy chlorine [0,0,2,2]; settle then chlorine [1,0,3,3]; microfilter then chemical [4,4,4,4]. Words match the spec's scale.
6. PASS: Design 2 top at 96.1 versus 95.5. Flip targets [2,2,4,none] for hours, feels-like, cost, ready. All-zero tie. Real keyboard flip reaches Design 3.
7. PASS: Check tree explicitly marks Students are too loud as not part of the heat problem.
8. PASS: tree, sort, chart and comparison table dominate their respective stages at 1366 and 680.
9. PASS: thirty immediate option changes peaked at 6.6 ms including redraw. The model has no animation lock; flip highlighting is a replaceable CSS effect.
10. PASS: actual reload retained title, branches, placed custom card, criteria and saved design. Clear removed the localStorage key. Why was absent from storage.
11. PASS for all twenty named images and visible station tabs/main actions at 1366 and 375. FAIL for the literal twenty-one count: no twenty-first asset is named in the spec. All twenty named assets were inspected and contain no people.
12. PASS: held clicks at two-second pace gave each how line once over five changes, all three fail events spoke, and one design used wTradeEmpty, never wTrade. Read interrupted and read the current hint. Browser speech fallback; no listening review of recorded Gacrux clips because recording was prohibited.

## Wave lessons

- Hint and voice: PASS, immediate hints, state-valid welcome keys, kit Read and queue, current-state event guards, held-input logs.
- Focus and layout: PASS for stable toggles, sort controls and weights. Mode tabs and action buttons stay mounted. Keyboard tree placement and weight changes retain focus. Dialog close is handled by the browser and returns to its connected trigger.
- Sizes and targets: PASS for main controls at all eight required sizes, including a true 375 by 812 iframe. Minimum button and number-field targets are 44 pixels. Compact sliders retain 44-pixel height.
- No giveaways: PASS within the specified explorer format. No hidden-answer quiz or score farming was added. Fit-linked chips are explicitly required by the spec.
- Honest numbers: PASS, model assumptions and invented costs are labeled; unknown custom-design values display No value and cannot set a scale.
- Standards: PASS, a solo student performs decomposition, criteria/constraints, simulation and weighted evaluation. No family engine applies.
- Motion off: PASS, no infinite animations remained in the driven calm state; button timing and voice stay unchanged.
- Short choices: PASS for initial tree decks, classroom interventions and water sources/steps in compact layouts. Longer feedback, model detail and wide custom tables can scroll inside their regions.
- Resize mid-animation: PASS, completed audit reported no exceptions or disabled controls left behind. Room redraws are synchronous and the ResizeObserver reconstructs the chart at actual pixels.
- Welcome after first action: PASS, no welcomeAfter queue; each station welcome has a current-state guard.
- Unknown as unknown: PASS, missing new custom criteria are excluded rather than treated as evidence of zero.
- One look, one meaning: PASS, line dash patterns and word ratings survive grayscale; pass/fail and top/tie always use words.
- True badges: PASS, ready, electricity failure, top and tie come from current numeric state.
- Reversible hints: PASS, tab entry immediately replaces the hint and direct actions name the next available control.
- No answer by copied words: PASS, tree feedback appears after Check; the broader task is constructing and defending an open design decision.

## Audit leads

The full attempt on Chrome 9981 lost its connection during resize after sixty frames. One smaller retry on unused Chrome 9987 completed with the optional control walk omitted. Both attempts used host port 8785 on loopback address 127.0.0.2; shared audit code was not edited.
Completed report: S:/CurioClass-codex/_scratch/design-challenge-studio/audit-retry/audit.md. Nineteen grouped leads: eighteen fixed and one false positive. Every entry is answered in S:/CurioClass-codex/_scratch/design-challenge-studio/audit-dispositions.md.

- Fixed three phone card overlaps by bounding scrollable card text and giving Start its own row. Briefs are keyboard focusable.
- Fixed Start focus loss in all seven state recipes by focusing the first station tab with preventScroll.
- Fixed the forty-three-pixel constraint input with a hard forty-four-pixel minimum; checked at both 375 and 760.
- Added an explicit Why aria-label matching its existing associated label.
- Fixed six water bar/result overlap leads at 680 and 800 by reserving bar height and compacting step/source controls. All four bars and all treatment choices stay visible; result detail can scroll.
- The phrase Design 1 becomes top is a design identifier, not a count mismatch. This is the one false positive.
Targeted follow-up checks reuse the audit's PAGE_JS for affected states only. Their small-target, overlap and unnamed-control lists are empty, with visible unclipped hints and no page overflow. Final keyboard, Escape and held-click Clear checks pass. The full matrix was not repeated a third time.
S:/CurioClass-codex/_scratch/design-challenge-studio/audit-snapshot-to-final.diff and final-tool.html preserve the completed audit snapshot-to-delivery changes.

## Frames looked at

Both bar frames; all first, check, functional, extreme, voice, last-functional, matrix, focused-fix, audit, post-audit and valid final phone frames, directly and in labeled contact sheets. S:/CurioClass-codex/_scratch/design-challenge-studio/frames-looked-at.json lists the frame paths. Invalid phone frames from the other build and the file-origin experiment were identified as test-harness failures and are not passes.
The complete size matrix ran once. Only states affected by a fix were re-shot. Final phone result detail may scroll within the stage while all intervention controls and the primary action remain visible. Compact Flip finder scrolls separately so Why stays visible.

## Art made

Sixteen new named paintings with the built-in image tool; four existing paintings retained. Two treatment images redrawn once for key spill. All fourteen object assets were re-keyed with the approved free art.py form, with despill and holes processing as appropriate.
Twenty final WebPs, 384,148 bytes (375.1 KiB). Bundle 699,463 bytes (683.1 KiB), below 2 MB. Prompts and raw originals are preserved. preview.svg is drawn in code.

## Art still to paint

None among the named assets. The spec's count discrepancy needs an editorial decision, not an invented extra asset.

## Engine changes wanted

No kit change. handoff.md also requests checkpoint reports before resize stress so interrupted audits retain completed leads. Optional audit mode-discovery improvement in handoff.md: recognize the spec's station navigation below the header so mode control walks can reach it automatically. Explicit states and separate input tests cover it here.

## Left open

The full automated control walk has no completed aggregate report because the first audit connection closed during resize; the successful smaller retry omitted that walk. Separate held-input, keyboard, voice, drag and functional checks passed. Cold review can repeat the full walk. Source claims were used as supplied without internet refresh. New recorded narration was intentionally not made. The spec names twenty images while saying twenty-one. Cold review is next; no polish or commit was started.

All build-owned Chrome and host processes are closed; tools/design-challenge-studio/host.html is absent. The other build's 127.0.0.1 host was left alone. Closure evidence: S:/CurioClass-codex/_scratch/design-challenge-studio/closure.json.
