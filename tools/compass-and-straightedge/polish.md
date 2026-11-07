# Polish: compass-and-straightedge (Codex fix, round 1)

Curiosity No. 09. Work stayed in the requested checkout and two allowed folders; no commits or refine edits.
Evidence paths below are relative to `_scratch/compass-and-straightedge/` unless named otherwise.
The initial harness run had a test-only `window.Curio` lookup error; it was corrected and all required before cases rerun before source fixes.

## Blocker

1. FIXED: Tangencies and crossing merges use the disclosed relative tolerances. The real six-circle walk changed from 15 to 13 points, with only A at the centre. `before-01-tangency.json`, `after-01-tangency.json`, `fix-before/01-tangency.png`, `fix-after/01-tangency.png`. `verified-tangent-scales.json`: 1,200 tangent cases, three scales, both argument orders, zero failures; a genuinely secant pair still returns two roots.

## Should fix

2. FIXED: Book coordinates map by similarities onto matching givens. All five relevant I pages have zero A/B placement error, and all four IV pages have zero centre/rim error (`final-book-map-numbers.json`). Default I.1 centres changed from -0.5/0.5 to 0/1. Unmatched studies have primed letters beyond the drawing; their reference extensions stay in that study (`fix-final-extra/detached-final.png`, `fix-verify/ghost-blank.png`, `ghost-angle.png`, `ghost-circle.png`).
3. FIXED: Ink, erase, brackets and tool changes use geometric names. Before: o9, p5, line. After: Inked the line from A to B; Erased point C and 2 dependent lines; Straightedge. See `before-03-language.json`, `after-03-language.json`, `verified-keyboard-announce.json`, and `fix-voice/evidence.json`.
4. FIXED: Reference points are lettered and their glyph bounds prevent collisions, including D/G/L in I.2 and E/F/H, D and V in the pentagon's separate compound drawings. Book and paper names agree, including the student's actual letters where a point already exists. I.2 changed from zero text nodes to five at step 7; at 680x425 the final letters measure 12 px high (`final-book-short-final.json`). The audit exposed a B′/H′ overlap at 680x425, corrected with measured glyph placement and leaders. Final Book checks at 680, 1366 and phone widths show no overlap; all 15 pages at both 680 and 1366 have zero label overlaps (`edge-after-book-pages-680.json`, `edge-after-book-pages-1366.json`). The pentagon transfer now explicitly names the longer part of the preceding golden division, avoiding an absent H (`fix-edge-after/copy-context-680.png`). Frames: `fix-polish/book-i2.png`, `book-pentagon-division.png`, `book-pentagon-circle.png`, `fix-final-extra/book-matched-letters.png`, `book-short-final.png`.
5. FIXED: Snapshots hold only drawing data. Undo and redo preserve the tool, Euclid switch, Extend, retained-opening switch, view and ghosts. The reproduced 0.7-unit jump is gone (`before-05-undo.json`, `after-05-undo.json`, `verified-undo-scope.json`).
6. FIXED: Readout text updates only when its value changes. Thirty pan steps went from 30 live-region mutations to zero (`before-06-live.json`, `after-06-live.json`, `final-live-final.json`).
7. FIXED: Pointer renders coalesce to one per animation frame, offscreen points skip labels, dense crossing labels suppress, dots share SVG paths, and the record is cached. At 1366x768, 60 circles and 2,101 points: p95 direct render 5.6 ms (before 40.8 ms); native 60-step pan p95 6.3 ms, maximum 7.1 ms. A burst of 100 requests produces one render. The 13-object hexagon p95 is 0.8 ms (`verified-dense-timing.json`, `verified-hexagon-timing.json`, `final-dense-pan.json`). These are desktop measurements, not a Chromebook hardware benchmark.
8. FIXED: The real steel edge rests under the strokes at the paper's bottom edge and aligns with a straightedge drag. The held drag recorded 20 distinct instrument transforms, immediately with Motion off (`polish-ruler-drag.json`). Resting frames: `fix-final-extra/triangle-1366.png`, `triangle-1920.png`, `hexagon-1920.png`; the old fixed strip across the working area is gone.
9. FIXED: Blank paper selects Point and displays L.blank until its first point. It stays silent until Read. `before-09-blank.json`, `after-09-blank.json`, `fix-polish/blank-phone.png`, `fix-voice/blank-silent-read.png`.
10. FIXED: Tags avoid label and point bounds. The original 680x425 and 375x812 overlaps with B are reproduced in `fix-before/10-tag-680.png` and `10-tag-phone.png`. Final frames: `fix-last/tag-680-final.png`, `phone-circles.png`; zero label intersections at 680 (`last-tag-680-final.json`), and the phone tag is below B, at y354.5, while B's label ends at y320.5.

## Polish accepted

11. FIXED: A crossing note is a new line within its parent move, rather than an extra numbered move. `fix-last/log-sublines.png`, `last-log-sublines.json`: three record rows after the two circles, the third containing "They cut at C and D."
12. FIXED: Names after Z use numeric subscripts, with separators for multi-character endpoints. No AB or AA point names in the dense test. The classical pentagon reads N · M₁₂ and 1.6180 (`polish-density-labels.json`, `final-pentagon-method.json`, `fix-final-extra/pentagon-method.png`).
13. FIXED: Given, free, stroke anchors, selected, hovered and keyboard-cursor points retain labels. At low magnification other crossing labels hide; at higher magnification they require collision-free space. The 2,101-point frame has 12 essential labels (`verified-dense-timing.json`, `fix-verify/dense-timing.png`). Arrow selection was verified to reveal hidden N (`edge-after-density-keyboard-reveal.json`: false before, true after); hover and choice use the same required-label path.
14. FIXED: Exact closed chord cycles on the original circle identify IV.15 and IV.6 quietly. Hexagon: `verified-hexagon-timing.json`; square: `polish-square-note.json`, `fix-polish/square-note.png`. Incomplete cycles and radius alone do not suffice. No speech, tally or found list.
15. FIXED: Eight separate named entries in the Manual (`verified-manual-finds.json`, `fix-verify/manual-finds.png`).
16. FIXED: The triangle tag sits outside its triangle bounds, near the figure. `fix-last/triangle-log-final.png`, `fix-final-extra/triangle-1920.png`.
17. FIXED: Selected strokes use a 2.5 px red line and a soft 7 px halo. `fix-last/triangle-log-final.png`, `phone-circles.png`.
18. FIXED: Undo and redo use 22 px SVG icons. Runtime dimensions: `polish-hint-680.json`; final frame `fix-last/tag-680-final.png`.
19. FIXED: Manual remains modal for focus, anchored at left 24 px, bottom 80 px; phone uses left 12 px, bottom 138 px. `polish-manual-drawer.json`, `fix-final-extra/manual-1366.png`.
20. FIXED: Coarse pointers and touch/pen releases use 22 px on either side of a stroke. At 18 px distance, fine-pointer hit is null and coarse-pointer hit is the line (`polish-touch-band.json`).
21. FIXED: Keyboard rings appear after keys and clear on pointer input, including Book/Back to paper. `cursor-final.json`: 1 before the mouse, 0 after; `fix-cursor/cursor-clears-on-mouse.png`. The first attempted harness placed its key after the mouse clicks and correctly showed a ring; the corrected order proves the transition.
22. FIXED: Names start with Edge, Point and Erase, matching visible words. `polish-hint-680.json`.
23. FIXED: Phone zoom tag is at (19,22), clear of the compass, whose resting position is in the right margin. Initial and radius-retained frames: `fix-last/phone-rest.png`, `phone-circles.png`.
24. FIXED: Choosing a non-compass instrument hides the initial drag hint without adding speech. `polish-hint-680.json`, `fix-polish/hint-680.png`; ten rapid instrument changes added no welcome in `fix-voice/evidence.json`.
25. FIXED: Checked the scans' OCR. Volumes 00 and 03 confirm III-IX and X-XIII. Scan 02 metadata failed once; direct OCR retry succeeded, but its contents span the multi-volume contents list, so its link conservatively says Heath scan 02. Raw evidence: `data/fix/`; scripts: `fix_sources.py`, `fix_source_retry.py`. No unconfirmed range remains.
26. FIXED: `tools/compass-and-straightedge/notes.md` now names proof-tower for G-CO.C proofs and identifies this as the second G-CO.D card. The module map stays unchanged.

## Settled calls

Applied the Curiosity brief over lesson defaults: no welcome screen, goal, score, quiz, level, finish or kit header. The Book remains freely browsed. Measurement stays, with its honesty note. Margin identifications stay quiet. The full-screen sheet underneath controls and modal coverage are intentional. The original numerical threshold in spec.md stays untouched; the working tolerance is disclosed in the Manual and draft sources.

The source lesson-creep scan found zero score, level, goal, sticker, badge, correct, wrong, try again, complete or well done hits. The 60 points hits refer to geometric points, the point tool or point arrays, never scoring (`fix-static.json`).

## Cheats tried

There is no score or pass condition. Tested the instrument instead: tangent roots in both orders across three scales; a close secant that must retain two roots; Undo/Redo after switches, pan and Book ghosts; repeated render bursts; 60-circle pan; the 47-object classical pentagon with no free points and a collapsed opening. It returns five equal sides and diagonal/side 1.6180339887498931 (`final-pentagon-method.json`). The Book never adds anchors, and blank and given-angle references leave the student's point count unchanged (`verified-ghost-blank.json`, `verified-ghost-angle.json`).

## Voice walk

Held real clicks for 120 ms, with two-second action gaps and real, whole-pixel jittered drags. `fix-voice/evidence.json`: initial hint once; Read with named ink row once; Read with named erase row once; Read on blank paper with Sound off once. Ten rapid switches add no automatic welcome. The brackets test announces the circle's centre and through-point. allLines equals all 14 unchanged bank lines; zero exceptions and zero HTTP requests. Existing missing recordings use the stated browser-speech fallback; this run checks its start log in muted Chrome, not recorded audio quality.

| Line | Kind | Expected | Logged |
|---|---|---:|---:|
| Drag from A to B | initial hint | 1 | 1 |
| Ink read, with current instrument and measurement | requested Read | 1 | 1 |
| Erase read, with dependent construction | requested Read | 1 | 1 |
| Blank paper, Sound off | requested Read | 1 | 1 |
| Extra welcomes after instrument switches | automatic | 0 | 0 |

## The real material

- Euclid, Heath's 1908 translation: public domain in the US. [Scan 02](https://archive.org/details/thirteenbookseu02heibgoog), [scan 00](https://archive.org/details/thirteenbookseu00heibgoog), [scan 03](https://archive.org/details/thirteenbookseu03heibgoog). Fetched 2026-11-06, complete available OCR, no sampling and no new OCR prose incorporated. Existing enunciations and postulates remain the supplied specification's wording. Geometry of the triangle, collapsing-compass copy, golden division and pentagon is independently recomputed in the retained construction replay; IV.6 and IV.15 were also checked against [Joyce's Euclid IV.6](https://mathcs.clarku.edu/~djoyce/elements/bookIV/propIV6.html) and [IV.15](https://mathcs.clarku.edu/~djoyce/elements/bookIV/propIV15.html), verification only, no text or artwork copied.
- Existing historical facts: [MacTutor biographies](https://mathshistory.st-andrews.ac.uk/Biographies/), [text licence CC BY-SA 4.0](https://mathshistory.st-andrews.ac.uk/Miscellaneous/copyright/). Facts paraphrased, no licensed article prose or imagery incorporated. Rechecked Wantzel, Gauss, Lindemann and Mascheroni on 2026-11-06. Independent verification: [Wantzel's 1837 paper catalogue](https://www.numdam.org/item/JMPA_1837_1_2__366_0/), [Gauss diary research](https://epubs.siam.org/doi/10.1137/25M1806491), [Mohr-Mascheroni proof](https://math.ch/norbert.hungerbuehler/publications/A_Short_Elementary_Proof_of_the_Mohr-Mascheroni_Theorem.pdf), [regular polygon theorem](https://webpages.ciencias.ulisboa.pt/~pjfreitas/pdfs/DividingTheCircle.pdf), and [Lindemann biography](https://www.deutsche-biographie.de/sfz51526.html?language=en). Verification only; no copyrighted text, figures or datasets imported.
- Original calculations, new tolerance and numerical readouts: Curio Class engine, MIT code; original text and diagrams CC BY 4.0, as repository LICENSE and LICENSE-CONTENT.md state. No external dataset or library was added. Named source and licence remain in the Manual and tool.draft.json.

Additional saved-reference probe: malformed placement metadata changed from accepted to rejected, and a legacy save without that metadata now advances from two to three ghosts without an exception (`edge-before-saved-reference-context.json`, `edge-after-saved-reference-context.json`).

## Engine changes wanted

None needed for these fixes. The existing optional kit power-label formatter request remains in handoff.md; the kit was not edited.

## Audit

The single full audit finished within its 2,400-second limit: `fix-audit/audit.md`, 381 leads. It includes the new I.2 and golden-division states. No second full audit or three-lens review was run. The final Book-only follow-up was bundled and checked with 12 scoped shots; `fix-validation-manifest.json` records both the audited bundle hash and final bundle hash.

| Leads | Disposition |
|---|---|
| 194 sheet/control overlaps | Intentional full-bleed sheet underneath controls, per the settled call. Frames inspected. |
| 135 controls covered by drawers | Intentional native modal coverage, including drawer headings and bodies. Frames inspected. |
| 39 SVG text-size flags | The audit reports font size in SVG user units. Final actual text bounds are about 12 px high at 680 and phone widths, 16 px at 1366. The opening figure is now measured after its drawer opens too. |
| 7 first-tap welcome omissions | Allowed Curiosity behaviour under BASELINE 16. Instrument hints remain reachable through Read; no new welcome is added. |
| 1 Manual scroll flag | Sources are links after the Manual's prose, not a short set of instrument choices. The Manual scrolls, with Close in its sticky heading. |
| 2 hint visibility flags | The saved default and blank-paper frames visibly show the required hints in the paper. Initial hints intentionally disappear after action; current hints remain on Read. See `fix-audit/state-blank-paper-680x425.png`, `fix-last/phone-rest.png`, and `fix-voice/evidence.json`. |
| 1 B′/H′ overlap | Confirmed at 680x425, fixed by glyph-bound placement, re-shot at 680, 1366 and 375. `fix-edge-after/golden-680.png`, `golden-1366.png`, `golden-phone.png`; all three return zero intersections. |
| 1 iframe-context error and 1 missing-hint flag | Audit harness failed to enter the phone iframe, so that part is not claimed as audited. Independent drive.py host runs at 375x812 cover default, circles, blank paper, I.2 and both pentagon subfigures. Their frames and numbers are preserved. |

Motion off and resize checks were clean; every held-click control row reports no errors and no unintended movement, and the keyboard Enter follow-ups pass. The repeated- and quick-click sections are clean. All 27 audit frames and all four final Book contact sheets were inspected.

Final bundle: 106,696 bytes, with no syntax, external-resource, draft-field or notes-section failures in the scoped check_tools.py checks (`fix-static.json`). Zero source em dashes. Targeted driver batches report zero tool console errors; the initial before host's favicon 404 was a test-host issue, removed in the host harness. Voice capture records no HTTP requests.

## Frames looked at

All targeted before/after, polish, verification, final size/mode and voice frames were inspected, including the 19 contact sheets in `fix-gallery-checks/` and the six native final frames in `fix-last/`. Final cursor and both permitted model frames were inspected in `fix-cursor/`. Models were actually used (Beat Lab play/stop; Elements Inspector element and zoom controls). No other tool was changed. The 14 edge-case frames were inspected through `fix-gallery-edge/`, including both before frames and all 12 final scoped shots.

## Curiosity check

The four short-test answers remain yes: open drawing invites unassigned play, the real construction has adult depth, geometry is the working interface, and the instrument needs no score or finish. This fix preserves the three lenses' short-test verdict rather than claiming a new cold review. Compare `fix-last/triangle-log-final.png` beside `fix-cursor/model-elements.png`; Beat Lab was also opened and played.

## Left open

Cleanup limitation: debug ports 9910, 9911, 9912 and 9913 are closed and tools/compass-and-straightedge/host.html is removed. The detached local Python host on 8715 still responds. Windows returned `ERROR: Access denied` to termination of the verified `python scripts/drive.py compass-and-straightedge --host 8715` processes. Identified PIDs: 16768, 27300, 38720, 41340, 48100, 49672, 59992 and 62032. Exact commands and errors are in `fix-server-cleanup.json`; no permission bypass or unrelated process termination was attempted.


The spec's module-reach question is deliberately unchanged, as refine.md directs. The existing recordings are still absent; the spec's browser-speech fallback remains. No claim of a Chromebook hardware benchmark. Optional recognitions beyond I.1, IV.6 and IV.15 were not added, as only cheap, sure detections were requested.

The report was assembled in Scratch and copied to polish.md only after all checks, honoring the user's explicit stop condition over the early-report instruction. Unattended decisions followed the brief: unmatched studies get their own primed letters; unconfirmed scan ranges are omitted; no confirmation was requested.
