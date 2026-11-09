# Polish: levels-and-pathways (Codex fix, round 1)

Evidence paths below are relative to `_scratch/levels-and-pathways/`. This is not an exit PASS. Instructions and quiz integrity are reported separately: under the requested cheat gate, items 5, 6 and 14 remain NOT FIXED because blind enumeration can fill a Mystery dot, even though their requested narration changes are observed.

## Blocker

None listed.

## Should fix

1. FIXED: replaced remote annotation cards and routed leaders with badges directly on their own parts. A joint placement search separates compact targets. Before: `fix-before-parts-real/before-parts-680.png` and `fix-before-parts-real/before-parts-375.png`, real pointer drags. After: `fix-ui-final/ui-final-parts-680.png` and `fix-ui-final/ui-final-parts-375.png`, same four-part geometry at 680x425 and 375x812. Zero leaders and zero overlapping hit rectangles; all four targets are 64x64, with 11 px minimum numbers. The 1366 layout was also checked.
2. NOT FIXED: reproduced Bend, Twist, Swing, idle Low and Low Gallop at 1366x768 in `fix-before/before-low-*.png`. Rounded trouser underpainting, folded-leg depth ordering, a hand-only green-alpha filter, knee-contact rest-arm angles and a neck limit improve specific seams. `fix-targeted/final-low-*.png` still shows a cropped kneeling silhouette and imperfect articulation. I do not claim a complete painted-rig repair. A trial arm underpainting was removed because it weakened the otherwise stronger standing artwork.
3. FIXED: DA:Pr4.1.2a removed from the standards claims in the source header, spec and notes; its move to choreography-board is written in the spec, notes and handoff. Header claim count is zero. The merged Teaching review identifies the missing grade 2 expectations; the named source remains National Core Arts Standards, Dance (2014), in spec Sources. No receiving sibling or catalog file was edited because those paths are outside scope.
4. FIXED: the held High guide tap changes selected and shown levels to high, with aria-pressed true (`after-guide.json`). Bands select levels in Levels, Pathways and Draw. Mystery instead shows a display scale without individual card borders or keyboard controls; its target is hidden. Phone guide controls measure at least 60x61. Final 1366 frames: `final-mode-levels.png`, `final-mode-paths.png`, `final-mode-mystery.png`, `final-mode-draw.png`. Part/guide accessibility is no longer hidden inside an image role.
5. NOT FIXED under the cheat gate: the requested ending is observed. `fix-extra/gallery-1366.png`, `fix-extra/gallery-680.png` and `fix-extra/gallery-375.png` show "Tap Play again for new mysteries." The matching JSON logs record replayHow once, after the bow enables Play again. However, blind enumeration still fills a Mystery dot; see Cheats tried.
6. NOT FIXED under the cheat gate: the hint defect itself is corrected. Before: `fix-before/before-mystery-trip.png`, Go disabled while its name remains in the hint. After: `fix-after/after-mystery-trip.png` and `after-mystery-trip.json`, watching hint while Go is aria-disabled true. watchTrip is spoken once on the natural walk. The retained guessing route prevents a full FIXED claim under the requested gate.

## Polish accepted

7. FIXED: Middle now says "Middle level. Stand up, not too high and not too low." in runtime, lines.json and the spec table. atMiddle is spoken once in `fix-walk/main.json`; the full walk used held clicks with 2-second gaps.
8. FIXED: High lifts the whole painted figure while toe tips remain anchored, rather than reading only through raised arms. `fix-regression/high-rise.png` and `high-rise.json`: an additional 11.036 px heel rise at 1366x768. The same transform applies to guides, mirror and button rigs.
9. FIXED: Levels names staying in one place; Pathways opens "Now we travel!" Notes name nonlocomotor and locomotor. Final short Levels welcome heard once in `welcome-final.json`; Pathways heard once in `fix-walk/main.json`. The welcome also includes copying in bubble space.
10. NOT FIXED: empty queue barriers are removed from newRun and afterRead. The full walk has zero blank voice-log entries, and Read retains priority (`read-priority.json`). The kit exposes no Read-completion promise, so count-ins still use its conservative duration cap. The exact public API addition is in handoff and Engine changes wanted below. No kit file was edited.
11. FIXED: Support at home now has three tool-specific activities possible tonight: paper pathway and walking, sky/table/grass shapes, and curved around a chair then straight back. Seated/hand alternatives remain. Verified in notes.md.
12. FIXED: notes explicitly distinguish sitting/kneeling/lying for moves in place from a deep crouch when traveling. Verified in notes.md.
13. FIXED: older ribbons have separate, fully opaque badges at staggered positions along their own ribbons. `fix-regression/three-ribbons.png` shows three readable badges after three real trips. `three-ribbons.json`: three badges, each 58.8x28, with disjoint rectangles. They no longer fade with the older ribbon groups.
14. NOT FIXED under the cheat gate: circleCurved is heard exactly once after round 7's correct answer in `fix-walk/main.json`; the natural walk frame is `fix-walk/circle-round-7.png`. The requested teaching cue works, but blind enumeration still advances the same Mystery progress check.
15. FIXED: removed the separate Copy me wait and put its meaning in the welcome. The first move takes its first shape immediately during its call. `after-first-move.json` observes the Twist shape at 294 ms from the test timestamp, including the held press, instead of the reproduced roughly 8-second wait.
16. FIXED: no start star is drawn in the gallery. `gallery-1366.json`, `gallery-680.json`, `gallery-375.json` each report zero gold-star polygons; their frames show the fifth ribbon's full beginning. The natural eight-round gallery is also in `fix-walk/gallery.png`.
17. FIXED: the studio SVG is a labeled group. `access-keyboard.json` shows Part 1 and Part 2 as unignored buttons in Chrome's accessibility tree, with full labels. Enter twice cycles low to middle and retains part focus. Frame: `access-keyboard.png`.

## Settled calls

Applied: no sensitivity lens was added, no new activity or topic was added, the rich studio/cast/ribbon design is retained, and the existing Done when content remains. The prior contract/voice verdict was a starting point, not proof for the changed bundle. The spec's open question was left untouched. No fresh lens pass was run.

## Cheats tried

- Blindly tap all pathway answers during travel: zero solved, step remains go. Guide High and Next before answering: zero solved, round 0 remains the path question. Hidden level inspection: shownLevel null, no revealed level badge, guide unavailable as an answer control. Natural-run record: `fix-walk/main.json`.
- Cheapest successful bypass: wait through required replays and try choices in turn. Curved, Straight, High, Middle fills the first progress dot without identifying either movement. `all-options-cheat.json` and `fix-cheat-retry/all-options-cheat.png` show attempts and solved [true]. The first broader sweep exceeded the driver's 60-second evaluation bound; one smaller retry completed and exposed the bypass.
- Spec decision followed unattended: keep the eight exact rounds, unlimited wrong-answer replays and no wrong-answer count. Closing enumeration would require changing that teaching/check design. I did not add lives, attempts, a new assessment or a new score. This is why the Mystery-related items above remain NOT FIXED under the requested gate.

## Voice walk

The natural path used real held clicks and 2-second gaps: Levels welcome, Stretch/Middle, Low, freeze, Pathways welcome, Straight/Walk, ribbon, Mystery welcome, watching cue, eight path/level answers, circle teaching cue, gallery. `fix-walk/main.json` records eight solved, zero runtime errors, zero external requests and zero blank entries. wLevels, wPaths, wMystery, watchTrip, atMiddle, circleCurved and allDone each started once. The later shorter Levels welcome and separated replayHow were individually rechecked in `welcome-final.json` and all three gallery JSONs.

Side path: Draw welcome, Surprise path, part names, tapPart, danceIt, in `voice-side.json`. Read before Twist keeps the move's real lines queued behind Read, with no empty stopper. All 49 runtime strings equal voice/lines.json. Twelve lines use browser fallback because recordings are absent; no audio was recorded.

## Engine changes wanted

`kit/curio.js`, Curio.voice return object: add `waitForRead: () => readP`, resolving on natural Read completion or hush, including Sound off. Then afterRead can await that public method instead of the conservative cap. No engine edit made. The Low painted kneeling repair remains art/renderer work, not a claimed engine fix.

## Checks and frames

Final bundle: 871,289 bytes (about 851 KiB), below the 2 MB goal. Final four-mode 1366x768 and accessibility run: zero runtime exceptions and zero external HTTP requests. Before/after and regression frames were viewed individually and in contact-0.jpg through contact-5.jpg. Motion off, grayscale and the Beat Lab/Snowy Mail Route comparison frames are in fix-regression. The studio retains its richer surfaces; the weak Low silhouette is explicitly open.

Best moment: the eight-ribbon gallery. Flattest moments: the first move's silent preparation, shortened here, and the Low kneeling silhouette, still open. Optional nits touched: stale pose requests are marked deferred; the spec's art and voice descriptions match the painted rig and changed cues. Other nits are left alone.

Commands: bounded reads/checks, 120-second bundles, 300-second drive batches, and one 2400-second audit. The first three short read calls lacked an explicit process timeout; subsequent shell commands were bounded. Early failed reproduction attempts selected a directory or the host rather than its iframe; corrected before the part-badge repair. Early host favicon 404s were test-host requests and were removed from later runs with a data favicon.

## Audit

Audit not finished. The single audit was started with a 2400-second process limit on Chrome 9911 and host 8715. The session was cut off before it completed; the restarted session did not run a second audit. Saved report: `fix-audit/audit.md`.

The seven direct viewport sizes, 680x425 through 1920x1080 plus 760x900, were clean. Pathways, Mystery and Draw mode-entry checks reported nothing new. Completed movement/drawing states, resize stress and the control/voice walk were not finished. The partial report's placeholder "clean" text in later sections is not evidence those stages passed.

Both saved leads are answered: (1) "iframe context not found" at 375x812 is an audit coverage failure; there is no audit phone frame. Separate drive.py iframe frames and numbers in fix-ui-final demonstrate the targeted phone badge and guide changes, but do not replace the missing full phone audit. (2) "no #hint element" comes from that same unread iframe context, not an observed missing tool hint: default-375.json and the phone frames show the real #hint. The final four-pixel phone hint-padding adjustment was bundled before the audit, but the audit failed to measure it, so its final full-viewport fit remains unconfirmed. These are recorded gaps, not a clean audit claim.

The restart verified that source, bundle, spec, notes, voice, audit states and refine.md still matched the saved pre-audit SHA-256 manifest. No browser/server was restarted because the remaining work was reporting. The temporary tool host.html is absent.

## Left open

Low painted articulation (2), the successful Mystery enumeration route affecting 5, 6 and 14 under the requested gate, and a public Read-completion signal (10). The integrator must move the grade 2 standard in shared catalog/receiving-tool files outside this session's scope. The interrupted full audit and final phone hint-fit measurement also remain open. No git commit. refine.md and refine/ were not edited. No deployment or upload.
