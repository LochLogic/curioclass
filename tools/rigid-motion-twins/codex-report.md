# Codex report: rigid-motion-twins

## Built

Tracks: all ten levels, three rigid moves, on-rock drag/tap setup, coordinate fields, exact landing, interruptible 600 ms motion, undo, proof cards, minimum-move stars, measurement evidence, five symmetry hunts and device progress.
Criteria: SSS, SAS, ASA, SSA and AAA on the painted field notebook, given-part marks, forward/back steps and the two SSA solutions.
Starter-based kit header, grade 9 to 12 theme, graphing Plane, Curio.voice, tones, Motion/Sound/Read, keyboard controls and responsive scene.
Deliverables include src.html, built tool.draft.json, notes, voice declarations, audit states, handoff, five finished images and preview.svg. No commit, publication or polish round.

## Numbers check

Independent script: `_scratch/rigid-motion-twins/spec-calculations.py`; results in numbers.json and contrast.json.
Footprint area 5.5; all nine vertex distance signatures distinct, so its correspondence is unique. All eight computed prints agree with the spec and stay inside the rock.
Symmetry totals: rectangle 3, square 7, parallelogram 1, trapezoid 1, hexagon 11.
Toe distances: √5 = 2.2360679775 and √10 = 3.1622776602.
Criteria squared sides 16, 10, 18; the three transformations give C = (7,4), (3,2), (9,2).
SSA: C = 53.464149° or 126.535851°; AC = 6.21152485 or 1.44891958. Displayed rounded values agree.
Nominal swatch contrast: brand/panel 13.946:1, brand/secondary 13.215:1, ink/brand 14.629:1, scene ink/sandstone 7.129:1, plaster/mud 7.127:1, mud/sandstone 3.853:1.
No numerical disagreement with the spec. General reflections can create non-half rational coordinates; handoff records that wording conflict.

## Facts checked

- Slides, turns and flips preserve lengths and angles; composition proves congruence: CCSS G-CO.A.2, A.4, A.5 and B.6, and Coxeter, Introduction to Geometry, chapter 3. The implementation uses orthogonal affine maps; every corresponding vertex must match.
- Single-motion classification, including glide reflections: Coxeter chapter 3 and Weisstein, MathWorld, Glide Reflection. Level 5 reverses orientation and its square is a nonzero translation, so it is neither a translation/rotation nor a single reflection.
- Polygon symmetry counts and the footprint's unique match: invented spec coordinates, independently enumerated in Python and checked in the browser.
- SSS, SAS and ASA: Euclid I.8, I.4 and I.26, Joyce edition; CCSS G-CO.B.7 and B.8. Given-part marks and three exact motions are shown in each construction.
- SSA is ambiguous in this example: the law-of-sines calculation above gives two valid positive triangles. Both are drawn from the same 40 degree ray and sides 5 and 4.
- AAA alone does not prove congruence: the displayed second triangle is exactly twice the first in each side, with identical angles.
- All footprint coordinates, distances and triangle positions: the invented spec data and independent script. No dinosaur species, age or real-site claim appears.

## Break it

39 deterministic browser checks passed in functional-results.json after fixing an angle-range guard that initially rejected turns.
The real drag landed level 1. Real keyboard input completed levels 1 to 3. Held clicks interrupted turns and folds correctly.
Cheapest attacks and outcomes:

- Apply without choosing geometry: initially natural defaults would solve levels 2 and 3 too cheaply. Centers and mirror endpoints now start blank. Real retest: zero turn moves and zero flip moves; no star.
- Zero slide, invalid angle, nonfinite coordinate, degenerate line and off-rock move: refused without a move or award.
- Wrong center on level 4: not landed. The half-point center lands.
- One flip on level 5: not landed. The two-move glide lands and is named.
- Extra moves before a landing: the three-move level 2 proof earns one star and is classified as the same 90 degree turn.
- Symmetry identity and repeated/reversed equivalent maps: do not increase the tray. A parallelogram reflection does not count.
- All six hexagon axes set by actual pointer taps: six distinct mirrors. The final targeted run reaches exactly 11 with the five rotations.
- Blind Not twins, mismatched corner pairs and equal corresponding lengths: all blocked. Real C-D and C′-D′ measurements produce 5 and 10 squared units and permit the call.
- Reload and Clear progress: stars survive the former; the latter remains empty after another reload. No external score, timer or hidden answer badge exists.

## Voice walk

31 declared lines exactly match runtime allLines(). Gravel-ranger, speaker Algenib, is declared; no recordings were made, as the brief prohibits recording.
Main held-click path at a 2 second pace: Slide, Turn, Flip, Criteria, Next step, SSA.
Initial walk exposed queued turn/flip instructions being dropped behind stale speech. Actual tool changes now hush obsolete context.
Targeted retest starts slideHelp, turnHelp, flipHelp, wCriteria and ssa, in that order, with an empty final queue. Context changes intentionally cut the preceding line.
The first Tracks welcome may be skipped on an action's own line, per BASELINE 16; its instructions remain visible and reachable with Read.
Side path: Level menu to Self-twins, Flip, Criteria, AAA, Read. The log contains wSelf, wCriteria and Read, with stale lines cleared on context changes.
Browser speech uses the shared kit fallback. Log starts and cancellation were tested; an audible gravel-ranger performance is not claimed.

## Feel check

Best moment: the cast finishes its fold and slide, settles into the sunken print, and the student's coordinate rules become a congruence proof naming a glide reflection.
Two flat moments corrected during Build: natural prefilled centers made early puzzles automatic, so choosing the geometry is now required; six identical "one flip" entries made discovery feel uninformative, so the tray now names each axis or angle.
Proof cards now appear at the motion's exact endpoint, and their scroll panel returns to the top. A post-landing arrow and accidental SVG text selection were removed.
The sandstone, mud, plaster, notebook and river setting provide material depth without pretending to identify a fossil species. The second mode changes the reasoning rather than adding a new topic.
Compared with Beat Lab and Snowy Mail Route. Side-by-side evidence: `_scratch/rigid-motion-twins/feel-comparison.jpg`. The field station has a distinct, richly painted finish; Beat Lab remains denser and more open-ended by design.

## Done when

1. PASS: level 1 real drag and keyboard land in one move, two stars, exact (x + 9, y + 5) rule.
2. PASS: wrong origin half-turn fails; 180 degrees about (-1/2, 1/2) lands.
3. PASS: level 5 needs two allowed moves; the successful proof names a glide reflection.
4. PASS: level 2 three-move sequence gives one star and names the 90 degree origin turn.
5. PASS: square 7/7 only after four flips and three turns; parallelogram has only its half-turn.
6. PASS: real matching toe measurements show √5 and √10; only then does Not twins win.
7. PASS: SSS ends at C = (9,2); SSA draws AC 6.21 and 1.45.
8. PASS: visually inspected 1366x768 and 1000x625; the plane/notebook triangles dominate their stage.
9. PASS: deterministic and held-input interruption checks leave exact endpoints and the correct move history.
10. PASS: six actual snapped mirror-line setups work; targeted hexagon run shows Found 11 of 11.
11. PASS: real keyboard finishes levels 1 to 3; all required sizes retain the rock and move bar without page scroll. The proof/move record has its own scroll panel in short views.
12. PASS: reload/clear checks, no tool HTTP resources or console errors on the real-input run, no authored em dashes, Curio Class named in full. The separate temporary host's favicon 404 is a harness request, not a tool dependency; host.html was removed.

## Wave lessons

- Hint and voice: PASS after stale-speech fix; hints change synchronously, name the next control and remain readable with Sound off. Read uses the current hint. No action waits for speech.
- Focus and layout: PASS in keyboard and held-input runs. No load focus; rock focus persists, controls are stable DOM nodes, intentional focus uses preventScroll.
- Sizes and targets: PASS for HTML controls in required sizes; SVG math is rendered at real pixel size. Corners use nearest-point selection with a 46 px diameter hit neighborhood.
- No giveaways: PASS after removing prefilled solution geometry. No proximity meter, answer selector, hidden target code or free Not twins award.
- Honest numbers: PASS; invented, unitless scene; exact radicals/rational rules, symbolic non-quarter turns, tolerance documented.
- Standards: PASS for the specified transformation, symmetry, corresponding-parts and triangle-criteria activities. Family engine absent, documented below.
- Motion off: PASS, zero running animations in the explicit check; live CSS lamp animation is removed.
- Short choice sets: PASS; five criterion cards and four move choices remain visible, levels/shapes use native dropdowns.
- Resize mid-animation: PASS in real interruption checks and the completed audit stress pass, with no exceptions or stuck controls.
- Welcome timing: PASS; no deferred welcomeAfter in a two-mode tool.
- Unknown as unknown: PASS; no hidden-information simulation or premature result.
- One look, one meaning: PASS; solid plaster, dashed mud, ghost, guide and yellow measurement each have distinct visual roles.
- Badge truth: PASS; state checks determine every earned star and tray count.
- Hints reverse with state: PASS; level, card, mode, reset and tool selection update immediately.
- No answer by copying words: PASS; students specify geometry, not matching textual answer cards.

## Audit leads

One final audit completed in about 22 minutes, on the pre-repair bundle retained in audit/host/tool.html. It produced 35 leads. Every state/size, held control click, five-click sequence and resize stress check completed; there were no console errors, exceptions or stuck controls. No second full audit was run.
Grouped dispositions account for all 35 leads:

- 14 compact rock-label leads (including the self-twin A): fixed with measured label placement that avoids ticks and neighboring labels. Targeted final checks at 680, 800 and the 375 iframe are clean.
- 6 unnamed-coordinate-input leads (four fields, with two repeated on Self-twins): fixed with explicit names; targeted Turn and Flip checks are clean.
- 2 stale disabled-Next-step voice leads (Criteria end and AAA): fixed with step-specific follow-ups and state-aware mode-return hints. Final SSS, SAS, ASA and AAA checks name available controls.
- 1 C/F transition-label lead: the destination label temporarily yields near arrival; the exact endpoint shows C = F. The final fast-step check is clean.
- 2 duplicate SSA A/B labels: shared vertices are labeled once; the final SSA check is clean.
- 1 hidden-proof lead: the audit-state fixture omitted return from its drag path. The fixture is corrected; the separate real, whole-pixel jittered drag earns and displays the proof at 680 width.
- 7 first-tap welcome leads: accepted under BASELINE 16. Each action starts its own instruction or feedback, and the premise remains in the hint and Read. No deferred welcomeAfter is used.
- 2 same-mode quick-tap welcome cuts: fixed by ignoring a mode selection that is already active. The targeted repeated Criteria tap starts one welcome with no cut.

Ten final data-only checks of repaired views have zero mechanical flags. The first readout fixture needed its leading newline and keep placeholder corrected; these were harness errors, not tool errors. The 14 final native-input frames are console-clean. The final bundle differs from the audit snapshot only by the documented repairs; see final-static-check.json.

## Frames looked at

All 30 pre-audit PNGs in bar-frames, initial-frames, functional-frames, functional-frames-fixed, full-frames, input-walk and targeted-frames were opened and inspected. Full sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and the 375x812 iframe. Both modes, SSA, AAA, earned proofs, six hexagon mirrors, keyboard runs, grayscale and Motion off are included.
All 84 audit PNGs were inspected in 14 overview sheets, with four lead frames opened at full size. All 14 final post-frames PNGs were opened individually. Total inspected: 128 saved PNGs, plus finished art and the side-by-side comparison.

## Art made

Four new built-in OpenAI image generations: plaster, mudstone, riverside trackway and notebook. Existing sandstone retained and reviewed. All five appear in the tool; all have people false.
Five final WebPs total 315.11 KB. Recorded voice: 0 KB. The final single-file HTML is 748.00 KB, against the 2 MB goal. Its SHA-256 is 51eb30d6ffe384dd0842ce3c321e24b5b6ce3686580a6a8b9c54ce416ac0c6d1.
All new PNGs are in art/raw, their full prompts/provenance in art/prompts.json, and final WebPs were made with art.py --rekey only. No paid art command or audio recording was run.
Trackway edge trim removes a small corner signature-like artifact. No image required a redraw. All finished assets were inspected.

## Art still to paint

None. No people assets are required. The declared narration remains unrecorded, intentionally.

## Engine changes wanted

Missing kit/transformations.js and docs/families/transformations.md: provide the spec's shared Motion, classification, symmetry, animation and MoveBar API. Tool-local adapter uses the existing graphing Plane; no kit file changed. Exact migration points are in handoff.md.

## Left open

- No recorded Algenib audio; browser voice availability and offline pronunciation vary by device.
- No separate first-load overlay; trackway art is used as the large scene and banner. Handoff documents this and the Read/layout/engine/spec conflicts.
- The full screenshot batch timed out once before saving a frame. Its one smaller retry in two batches completed; later checks were targeted, not another full sweep.
- Write-boundary deviation: following the reference-bundle instruction regenerated the two ignored reference HTML bundles before its conflict with the user's stricter write boundary was recognized. No reference source or shared kit file was changed. No commit was made.
- The proof card and long move list require their internal scroll panel in short previews. Main controls and the rock remain in view.
- Chrome ports 9980 through 9987 and server port 8785 were verified closed after testing. The temporary host.html was removed.
