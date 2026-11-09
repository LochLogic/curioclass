# Codex review: launch-pad

## Played

Cold Grade 9 play covered Launch and all nine mission cards before reading codex-report.md, handoff.md, notes.md or src.html.
Eight cold flights verified; mission 5 correctly refused my trial answer "never" and requested complex notation.
The focused checks then verified the complex flight too. Best moment: one ball proves both 48-foot crossings.
Projected and compact views kept the graph prominent; the original generic completion was the flattest payoff.

## Findings fixed

- blocker (general), Missions / real(): -2^2 evaluated as +4 and passed Factor and the landing check. Corrected sign/power precedence.
- should fix (general), Complete the square: formula derivation was display-only. Mission 7 now checks three symbolic denominators.
- should fix (general), Formula voice: count instructions played over coefficient boxes. Added separate coefficient and discriminant lines.
- should fix (general), how(): the 2 s walk dropped tidy, root and answer instructions. Current-step instructions now start immediately, once.
- should fix (general), negative events: five submissions produced four spoken events. New events now take over; the rerun heard five.
- should fix (general), Clear missions: an active flight could re-save progress. Clearing now cancels and resets the active mission.
- should fix (general), balcony art: keyed residue and an absent catcher weakened the catch. Repainted it, marked people:true, aligned its rail.
- should fix (family:graphing), phone: high H labels were cropped. Adjusted tiny-label type/placement; 80 ft and 330 ft now fit.
- should fix (general), sources: corrected the dead OpenStax section and invalid NIST URL in notes and tool metadata; left the spec intact.
- polish (general), completion: retained the method, direction, exact event clock and model height as the student's earned record.
- polish (general), catch: the record now explains that the displayed ground time assumes no catch.
- polish (general), compact derivation: shortened and repositioned the explanation so it clears the height line and axes.

## Findings left

No known unfixed blocker. The final desktop re-shoot gap is recorded under Left open.
Nit: native mission selection truncates long names in narrow layouts; the complete setup remains visible.

## Break it

105 assertions passed in review-checks-fixed.json, using student-path controls and field submissions.

- Height gate: empty/wrong heights and repeated Check presses cannot advance. All four blank method paths remain unproved.
- Factor: blank/invalid pairs, p=q=0 and the -2^2 exploit fail; correct expansion succeeds. No score is banked at answer-ready.
- Square root: a negative magnitude fails; both signs are shown after valid work, and a negative event time is rejected.
- Completing the square: wrong k/m, missing roots and easy numeric derivation guesses fail; equivalent symbolic denominators pass.
- Formula: wrong coefficients, each wrong real-root count, single/missing roots and a lone complex root fail before Launch unlocks.
- Mission interpretation: launch-time zero, extra roots, one of two crossings, negative time and the upward catch fail.
- Mission 3 accepts reversed 3,1 and measures both at 48 ft; mission 5 requires 2 ± i and verifies a 64 ft peak below 80 ft.
- Mission 8 rejects 2.6 and accepts 2.64; mission 7 accepts 3.10. Accepted rounded times replay at the exact root, as the notes explain.
- Progress: interrupted/restarted flights cannot bank completion; Clear during flight stays clear after the old finish time.
- Explorer: slider extremes and sweeping are unscored. Zero launch, the 325 ft maximum peak and unreachable heights remain consistent.

Explorer deliberately supplies roots as the spec's checker; mission verification is supported practice, not evidence of unaided mastery.

## Voice walk

Held clicks: 0.12 s down, 2 s apart, default launch settings and Sound on. Logs are voice-*-result.json.
Main: default Launch, Missions, Write it, Tidy, Factor, Check work, Check answer, Launch.
Heard in order: wLaunch, wMissions, tidy, method, answer, launchNow, done, once each.
Formula side: wMissions, tidy, method, coeff, disc, root, answer, launchNow, done.
Complete-square side: wMissions, tidy, method, derive, root, answer, launchNow.

| Line group | Kind | Expected | Heard |
| --- | --- | --- | --- |
| Main welcomes and applicable how-to lines | welcome/how | once each | once each |
| Coefficients, discriminant, derivation, roots | how | once on applicable path | once |
| Negative-time response | event | five | five |
| Completion on main and Formula walks | event | one per completed flight | one |

New steps cut instructions whose controls have changed. Read retains priority; rapid switches, Read during speech and Sound-off Read were checked.
The final manifest matches all 14 fixed automatic narration lines. Recorded clips are absent; browser speech is the fallback.

## Facts checked

- Projectile model, feet/seconds and contextual roots: [OpenStax Elementary Algebra 2e 10.4](https://openstax.org/books/elementary-algebra-2e/pages/10-4-solve-applications-modeled-by-quadratic-equations).
- Peak/vertex interpretation: [OpenStax 10.5](https://openstax.org/books/elementary-algebra-2e/pages/10-5-graphing-quadratic-equations-in-two-variables).
- Completing the square, formula derivation, discriminant and complex solutions: [OpenStax 9.2](https://openstax.org/books/intermediate-algebra-2e/pages/9-2-solve-quadratic-equations-by-completing-the-square) and [9.3](https://openstax.org/books/intermediate-algebra-2e/pages/9-3-solve-quadratic-equations-using-the-quadratic-formula).
- A-REI.B.4a/4b coverage checked against [Common Core HSA-REI](https://www.thecorestandards.org/Math/Content/HSA/REI/).

Independent substitution into that model, with the spec's assigned parameters, is saved in review-numbers.json:

| Mission | Recomputed roots and event |
| --- | --- |
| 1 | 0, 4; return at 4 s |
| 2 | −1, 5; land at 5 s |
| 3 | 1, 3; both at 48 ft |
| 4 | repeated 2; peak 64 ft |
| 5 | 2 ± i; no real time, peak 64 < 80 ft |
| 6 | ±3; keep 3 s |
| 7 | (t − 3/2)² = 41/16; (6 ± √41)/4; landing 3.100781 s |
| 8 | (5 ± √31)/4; landing 2.641941 s |
| 9 | (7 ± √13)/4; ascending 0.848612, catch 2.651388 s |

- Standard gravity: 9.80665 m/s², or 32.1740485564 ft/s², from [NIST Appendix B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8). The screen explicitly uses the no-air, 32 ft/s² model.
- Extreme flight: 8.256939 s, peak 325 ft, independently recomputed. Each root substitution residual was below 1e-10.
- Contrast, using [W3C WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html): coral/panel 6.75:1, coral/section 6.40:1, button ink/coral 7.10:1, new record text at least 9.10:1.

## Sensitivity

No cultural, religious, hard-history or body-teaching content. A fresh art reviewer should inspect the new teenage catcher's hands, glove pose, ordinary clothing and small-size crop. The figure represents one friend, with no group claim.

## Flattest moment left

Entering a, b and c is the quietest remaining beat. Kept because signed-coefficient identification is part of the specified method.

## Graphics

All six used paintings were inspected individually and in scene; balcony was redrawn with built-in imagegen and free art.py rekeying.
Raw replacement: art/raw/balcony.png; finished: art/balcony.webp; full prompt: art/prompts.json. Used art totals 101.4 KiB.
Kept the painted field, textured equipment, drone life, progressive trace and instrument styling. Compared with the existing Beat Lab and Snowy Mail Route reference frames.
Bundle: 247428 bytes (241.6 KiB). All art tokens resolve; no missing painting remains. The legacy lp-field-dusk image stays unused.

## Audit

One full audit finished, exit 0: _scratch/launch-pad/review-audit/audit.md. All 89 audit frames were opened in 23 contact sheets, with compact/phone leads also opened full size.
Disposition: 45 visibility rows are transparent SVG hit-test artifacts, visually confirmed; the first-Launch welcome skip follows BASELINE rule 16 and the spec.
The frames separately exposed the cropped phone height label, now repaired. Final phone captures show both labels inside the graph and the catch record unclipped, with no console errors.
Default sizes, listed work states, Motion off, held controls, five-click repetition, quick taps and resize stress passed within the audit's mechanical scope.
Keyboard-only completion retained focus on Launch; grayscale kept solid/dashed and direction/word distinctions. Notes open with the required three sections.
No second full audit was run. The final tiny-label and catch-note changes received phone rechecks; their desktop recheck failed as recorded below.

## Left open

- Desktop re-shoots after the final small label/record changes failed twice with Chrome timeout/connection refusal. Per the command retry rule, stopped that check. Phone rechecks passed; the earlier full all-size audit is preserved.
- Browser speech was log-tested, not listened to. Keep the spec's big-sister choice for future recording.
- Protocol deviation: initial reads and some short metadata operations lacked explicit command timeouts. Bundle, drive batches and the 40-minute audit were bounded.
- Draft stayed in Scratch until completion to honor the requested stop as soon as codex-review.md is written.
- Folder confirmed S:\CurioClass-codex; writes stayed in the tool and its Scratch folder. No git commits. All assigned ports were closed and host.html removed.
