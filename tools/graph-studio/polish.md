# Polish: graph-studio (Codex fix, round 1)

Curiosity No. 08. All 13 should-fix and 17 accepted polish items were reproduced or checked and observed fixed. No lesson flow was added. Work stayed in the two authorized folders; no commits or refine edits.

Evidence root: `S:/CurioClass-codex/_scratch/graph-studio/`. Unless stated otherwise, item frames are 1366x768. JSON beside each frame contains its measurements. `before3` uses the frozen original source to let the opening finish before reproducing the missing re-ink at every named size.

## Blocker

None on the merged list.

## Should fix

1. **FIXED, double roots.** A numerical turning point within a view-relative tolerance is also a zero; tolerance is capped at 1e-6 to avoid inventing roots in enormous windows. `(x-1.3)^2` now has both turn and zero at `(1.300, 0.000)` through three panned windows. A positive minimum remains positive. Before `before/s01-double-root`; [frame](../../_scratch/graph-studio/after/s01-double-root.png), `verify-a/numerical-regressions.json`, `audit-followup/bounded-zero-tolerance.json`.
2. **FIXED, fraction powers.** Parser metadata reduces literal integer fractions; odd denominators select the real root on negative bases in the shared evaluator. At -8: 1/3 gives -2, 2/3 gives 4; 0.5 remains undefined. Signed/reducible fractions and even denominators checked. Before `before/s02-fraction-domain`; [frame](../../_scratch/graph-studio/after/s02-fraction-domain.png). Manual and draft name both references and licences.
3. **FIXED, log titles.** Axes retain data units with “log scale”; ticks remain original coordinate values. Before `before/s03-log-labels`; [frame](../../_scratch/graph-studio/modes/setup-planets.png) and `after/s03-log-labels.json`.
4. **FIXED, redraw cost.** View/expression/parameter signatures cache features; input settles for 120 ms and ruler animation refreshes at 250 ms. Intersections compare the active pen with others. Identical cached eight-line redraw benchmark: 27.77 ms before, 3.25 ms after. Separate playing fixture: redraw 4.31 ms, steady frame mean 16.67 ms; maximum recorded interval including startup was 116.6 ms. `before/s04-eight-keypoints.json`, `after/s04-eight-keypoints.json`, [frame](../../_scratch/graph-studio/verify-a/cache-and-play-performance.png) and its JSON. These are this desktop's measurements, not Chromebook certification.
5. **FIXED, power buttons and hint.** Read, Sound and Motion preserve the first-run hint. Before `before/s05-power-hint`; [frame](../../_scratch/graph-studio/after/s05-power-hint.png), JSON `hint:true`, `hidden:false` after all three held clicks.
6. **FIXED, names.** Announcements are “Degrees”, “Radians”, “Log scale on x/y”, “Key points on” and “Square grid on”. Reset has its explicit axis-reset aria-label. Before `before/s06-announcements`; `verify-a/announced-control-names.json`, [frame](../../_scratch/graph-studio/verify-a/announced-control-names.png).
7. **FIXED, equal scales.** First polar/parametric ink on the untouched default window switches to Square; rose and Lissajous setups start square and contain the whole shape. Circle physical scale ratio: 1.7414 before, 1.0000 after. [frame](../../_scratch/graph-studio/after/s07-polar-square.png), `edges/first-polar-param.json`, `modes/setup-rose.png`, `modes/setup-lissajous.png`. Ordinary y input keeps its original default window.
8. **FIXED, sweep steps.** Coarse steps dwell on their min-anchored lattice; fine sweeps retain continuous travel. Rose samples changed from 4.583…6.708 to whole 5, 6, 7. A -2..8 ruler with step 3 stayed on 1 and 4. Before `before/s08-ruler-step`; [frame](../../_scratch/graph-studio/after/s08-ruler-step.png), `edges/ruler-lattice.json`.
9. **FIXED, fractional spoken exponents.** Squared/cubed matches exclude following digits, decimal points and scientific-literal continuations. 2.5 reads “to the power 2.5”; 3.1 reads “to the power 3.1”. Before `before/s09-fraction-speech`; `after/s09-fraction-speech.json` and the 34-check numerical run.
10. **FIXED, duplicate parameters.** Ordinary table/trace coordinates appear once. Named functions use `f(3.000) = 9.000` and `x | f(x)`; polar/parametric tables retain t, x, y; vertical equations use y, x. Before `before/s10-trace-table`; [frame](../../_scratch/graph-studio/after/s10-trace-table.png), `verify-a/numerical-regressions.json`.
11. **FIXED, input/output words.** Tape and desktop footer use “in x · out y”; polar/parametric forms name their input and outputs. Compact phone footer uses the accepted arrow notation. Before `before/s11-flow-labels`; [frame](../../_scratch/graph-studio/after/s11-flow-labels.png) and final phone footer frames.
12. **FIXED, live Table placement.** Table sits beside the tape at 1366 and 680, and above the tape at 375. The ruler is unobscured at all three sizes and changes the first result from 25.00 to 50.00. At 680 several rows now show. Before `before/s12-table-wide` and `before2/s12-table-680`; [frame](../../_scratch/graph-studio/edges/table-live-1366.png), [frame](../../_scratch/graph-studio/edges/table-live-680.png), [frame](../../_scratch/graph-studio/edges/table-live-375.png), matching JSON.
13. **FIXED, ink and carriage.** Typed curves, setups, fitted ink and loaded notebook pages restart a 1.2 s pen pass. Visible ink begins without spending the opening on off-screen segments. Live scrubs/rulers remain instant. Real held setup clicks started one quiet scratch source (gain 0.009), moved the carriage 524→380 px, then stopped it; Sound off started none and Motion off drew instantly. Before `before2/s13-pen-*` and `before3/s13-reink-*`; `after2/s13-reink-*`, [frame](../../_scratch/graph-studio/verify-b/pen-audio.png), `verify-b/pen-audio.json`, `target/typed-curve-ink.png`, `edges/saved-page-reink.json`. Rest clearance is 18 px at 1366x768, 680x425, 760x900 and the 375x812 iframe: `polish-final/pen-rest-*`.

## Polish accepted

1. **FIXED, fit rates.** Census 1790–1860 exponential readout gives ×1.030 per year, 3.0 percent; NOAA line gives 1.672 ppm per year. [frame](../../_scratch/graph-studio/after2/p-data-fit.png), [frame](../../_scratch/graph-studio/verify-b/fit-line-rate.png). Independent decimal recomputation is in `independent-numbers.json`.
2. **FIXED, log R².** Both fit summary and result state “log space, not comparable with a line's”. `after2/p-data-fit.png/json`.
3. **FIXED, e entry.** Manual says to set n's maximum to 1000. Actual ruler setup reaches 2.716923932…; [frame](../../_scratch/graph-studio/polish-final/manual-e-1000.png) and JSON.
4. **FIXED, handles.** “Axes” and “Setups · Notebook”; contents retained. [frame](../../_scratch/graph-studio/sizes/default-1366x768.png) and all size frames.
5. **FIXED, number tabs.** Hover/focus/drag highlight the matching digits; a 24 px real drag changes the middle 2 by two steps. Native Tab focus selects character 8; moving the pointer away retains its highlight. Alt gives tenths and appears in the name/title. [frame](../../_scratch/graph-studio/verify-a/scrub-highlight.png), `polish-final/hover-token.json`, `polish-final/focus-token-keyboard.json`, [frame](../../_scratch/graph-studio/target/focused-token-persists.png).
6. **FIXED, race opening.** Setup enables Key points. Bottom labels lift clear of ticks and the edge; both positive intersections show, near 1.078 and 58.77. [frame](../../_scratch/graph-studio/verify-b/race-key-labels.png) and `modes/setup-race.png`.
7. **FIXED, Read for the ear.** Trace values are spoken only during tracing; “x equals 1, y equals 1” has no padded zeros. `verify-a/voice-walk.json`.
8. **FIXED, projected type.** At width 1280 and above, ticks, curve pen numbers, key labels and tape line labels are 12 px; engraving/end-cap captions/footer are 11 px and numeric end caps 12 px. `polish-final/font-readouts.json`, `modes/setup-parabola.png`, [frame](../../_scratch/graph-studio/polish-final/eight-pen-labels.png).
9. **FIXED, bars refusal.** `|x|` says “Use abs(x) for absolute value.” [frame](../../_scratch/graph-studio/edges/absolute-value-message.png).
10. **FIXED, first tap.** A tap retains its number node through click, so the hint starts at once. At 0.1 s after the held tap, before vlog was empty; after vlog already contains one spoken hint at 1371 ms. `before2/p05-number-tap.json`, `after2/p05-number-tap.json`.
11. **FIXED, data units.** Native pointer movement produces “year 1992 · 371.7 ppm”; trace and axis labels likewise carry the bundled units. [frame](../../_scratch/graph-studio/verify-b/units-co2.png) and JSON. Planets use AU and Earth years.
12. **FIXED, paper focus.** Inset 3 px outline, offset -4 px, visible on all four paper edges after actual Tab/Shift-Tab. [frame](../../_scratch/graph-studio/sizes/paper-focus.png) and JSON.
13. **FIXED, pen numbers.** All eight curve ends have their tape pen number. [frame](../../_scratch/graph-studio/polish-final/eight-pen-labels.png).
14. **FIXED, exponent notation.** Ticks show `6.00×10^18`, feature/readout exponents use ×10^ notation, and the double-root zero prints 0.000. `verify-b/race-key-labels.png`, `after/s01-double-root.png`.
15. **FIXED, initial coordinates.** Cursor output is blank until pointer movement. All eight `sizes/default-*.json` contain an empty cursor; native movement is checked in the data-units case.
16. **FIXED, 760x900 overlap.** Compact rail caption is omitted; carriage parks clear of power and the maker's plate remains intact. [frame](../../_scratch/graph-studio/sizes/default-760x900.png), `polish-final/pen-rest-760.png` (18 px clearance).
17. **FIXED, alias warning.** Warning sits below the y title, retaining the title and its own text. [frame](../../_scratch/graph-studio/edges/alias-focus.png) and `after2/p-focus-alias.png`.

## Settled calls

- Applied the merged trace/table item once (should fix 10) and the ink/scratch item once (should fix 13).
- Data, Manual and Notebook keep their drawer layout; only Table moved over paper to keep the tape usable.
- Square changes are limited to polar/parametric default input and those two setups; ordinary y defaults stay unchanged.
- Hint/tags over paper, a dismissed hint after action, intentional drawers and internal Manual/Data scrolling stay. Phone Add keeps its plus icon.
- Census sensitivity wording is unchanged. There is no sensitivity.md; the fresh sensitivity review and module-standards moves remain the integrator's open questions.
- The Curiosity brief wins over lesson norms: no welcome screen, goal, score, level, quiz, finish or kit header was added.
- Unattended choices followed the list's lean: Axes, Setups · Notebook, paper-side Table, 12 px scrub steps, and coarse lattice dwells.

## Cheats tried

- No score/check/quiz exists to pass. Mathematical counterexamples were used instead.
- Double root under three pans: still found; a nearby positive minimum did not become zero. A huge 6×10^18 y window prompted a tolerance cap; the positive minimum 1 stays 1 and has no zero in the final follow-up.
- Odd/even, signed and reducible literal fractions, decimal approximations, and 0^0: correct real values or undefined; 13 domain cases pass.
- Coarse ruler on a non-dividing step (min -2, max 8, step 3): every observed value stayed on its lattice.
- Pins at x=1 and 3 on x² give 4.000; coincident pins give undefined. Empty input, poles, sinc hole, 1000x oscillations and 1e99x stayed responsive; no false hole at the poles. `verify-a/numerical-regressions.json`, `polish-final/extreme-instrument.json`.

## Voice walk

Held clicks at roughly 2 s gaps: number tab, Read, Read, Trace, Read. Vlog shows one automatic “Drag the 2 up or down.” at 1360 ms; explicit Reads repeat the current hint at 3487 and 5627 ms; after Trace, Read at 9908 ms includes “At x equals 1, y equals 1.”
The fractional exponent path reads “y equals x to the power 2.5”. Read/Sound/Motion retain the hint. Audible recordings are absent; muted Chrome telemetry verifies starts/text and cancellation, not a physical speaker audition.
`voice/lines.json` equals `allLines()`: one fixed line. The audit's five-click and quick-tap checks for Number, Motion and Read are clean. A first tap may cut/skip the hint under BASELINE 16.

## Engine changes wanted

None. Kit files were unchanged; scratch uses the kit's audio context and Sound/Motion state.

## Audit

One full audit, port 9921, host 8725, hard 40-minute limit, completed. All 33 audit frames were inspected. Its 23-control walk has no errors, focus loss or unintended control jumps; repeat/quick Read checks are clean; Motion off and resize checks are clean.
Two confirmed layout causes were corrected after that single audit: Next is now at least 44×44 at all eight required sizes, and phone sampling is one line clear of controls. All follow-ups are in `audit-followup/`; no second audit or lens run was made. The audit is the pre-follow-up snapshot.
Every lead, including individual first-tap welcome leads, is answered in [audit-dispositions.md](../../_scratch/graph-studio/audit-dispositions.md). Intentional drawer coverage and the established hint/tag treatment were retained per Settled calls; ruler end caps use internal tape scrolling while the frequent-use slider stays visible.
Final bundle: 136,489 bytes. Scoped repository check functions report no errors. The site-wide check command was not run because it bundles other tools; its actual checker functions were applied to a Scratch copy with draft metadata. No external resource entries in the tested offline/default/data paths; no em dashes. Lesson search hits only mathematical points, sample points and their code variables.

## The real material

- No datasets were downloaded or changed. Exact original arrays were compared; hashes and independent calculations are in `independent-numbers.json`. New data gathering time was zero.
- NOAA GML: all 67 annual means, 1959–2025, ppm; retained source check dated 2026-11-05. Public domain under [GML's disclaimer](https://gml.noaa.gov/about/disclaimer.html); [annual means](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt). Independent line slope 1.671965839 ppm/year, R² 0.9805554803; quadratic R² 0.9994830149.
- US Census Bureau: unchanged decennial counts rounded to 0.01 million, retained versions/coverage notes. US government work, public domain; [Historical Population Change](https://www.census.gov/data/tables/time-series/dec/popchange-data-text.html) and [Statistical Abstract 2012](https://www2.census.gov/library/publications/2011/compendia/statab/131ed/tables/12s0002.pdf). The 1790–1860 subset's fitted annual factor is 1.029950249, 2.9950249 percent.
- NASA: unchanged eight rounded J2000 semimajor axes and approximate sidereal periods, AU/Earth years; public-domain US government data; [planetary fact sheets](https://nssdc.gsfc.nasa.gov/planetary/planetfact.html). Original sampling and Saturn rounding retained.
- Rational-power convention rechecked 2026-11-06 against [OpenStax College Algebra 2e 1.3](https://openstax.org/books/college-algebra-2e/pages/1-3-radicals-and-rational-exponents), current CC BY-NC-SA 4.0, and independent [MathWorld Cube Root](https://mathworld.wolfram.com/CubeRoot.html), copyright Wolfram Research. References only: no restricted text, images or datasets copied. Parser implementation, drawings and synthesized scratch are original Curio Class code under MIT.
- Growth and the e limit use the existing OpenStax chapter 6 reference, current CC BY-NC-SA 4.0, without copied content. `(1+1/1000)^1000 = 2.716923932…` is independently recomputed. Named sources/licences are in the Manual and tool.draft.json.

## Frames looked at

All produced PNGs in `before/`, `before2/`, `before3/`, `after/`, `after2/`, `verify-a/`, `verify-b/`, `sizes/`, `modes/`, `edges/`, `polish-final/`, `target/`, `fix-audit/` and `audit-followup/` were inspected through labeled contact sheets; the named root, domain, log, circle, table, focus, race and phone follow-up frames were also opened directly where needed. The 1366 regression run covers all six setups and five drawers. Eight default sizes, grayscale and keyboard frames are retained. Beat Lab and Elements Inspector were opened/used as the permitted material/density references; frames are in `polish-final/`.

## Left open

- No merged blocker, should-fix or accepted polish item remains open. Spec open questions and Census sensitivity review are unchanged; this report is not the fresh exit verdict.
- School Chromebook hardware, physical screen readers and audible speech/scratch audition were unavailable. The initial maximum frame interval is reported above; no universal 60 fps guarantee is claimed. Browser audio requires a user gesture, so initial pre-gesture ink is silent.
- Initial read-only discovery commands lacked hard timeouts; the recursive inventory was interrupted. Subsequent shell work uses explicit subprocess limits (120 s bundle, 300 s drive, 2400 s audit).
- A test batch initially overlapped the preceding Chrome shutdown and failed its connection; it was retried as smaller serial batches. An early host favicon 404 was removed. Completed product batches have no console errors. All owned test Chrome/server processes have ended.
