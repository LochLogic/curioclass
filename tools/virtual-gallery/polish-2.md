# Polish: virtual-gallery (Codex fix, round 2)

Outcome: blocker 1 repaired and proved; should-fix 8 remains partly open after the final audit exposed three empty Show me branches. No complete exit-gate pass is claimed.

Evidence root: `S:/CurioClass-codex/_scratch/virtual-gallery/round2/`; paths below are relative to it unless stated otherwise.
The active handoff is refine.md's ROUND 2 verdict and appended exit check. Twelve should-fix items and thirteen accepted polish items were already closed there. They were not reintroduced to manufacture before frames. New changes address blocker 1, its linked accepted polish 1, accepted polish 13, and an additional corner case of should-fix 7 found during regression checks. The previous report stays in polish-1.md.

## Blocker

1. **FIXED for the reproduced failures.** At 1366x768, `before/door-left-corner.png` shows bare plaster for legally clamped Kitchen Window x=577 despite its in-window DOM box; `before/door-only.png` names Map of My Block and its JSON passes Anchor although the work is behind the visitor. Kept the left Walk wall's descendants in 3D, fixing Chrome's clipping of its flattened far-end frame. A four-way runtime probe isolated that cause: only preserve-3d painted it. Applied this only to the left wall, since applying it everywhere introduced a back-wall texture seam. `final-sizes/corner-1366.png` shows the actual painting and outline; the equivalent 680, 800, 1000, 1280, 1920 and 760 frames also paint it. The door camera remains straight ahead. firstSeen() excludes both door-wall segments, returning null when nothing is in view; Anchor then fails, there is no cone or false work announcement, and the readout explains why. `supplement/door-only.png`, `door-only-checklist.png` and `cheats.json` prove that case. Back wall full, back wall empty, and starred left-side layouts are in `final-sizes/mode-walk.png`, `supplement/door-sides.png`, and `side-anchor.png`. The teapot at left x=520 did paint before this repair in this run; that individual manifestation was not reproduced, and is not claimed as a separate new fix. Its after frame remains painted.

## Should fix

These are prior-round closures from the cold exit check, preserved here. Where the original fault is absent, no new before/after repair is claimed.

1. **FIXED, prior repair preserved.** The unfolded door wall and door gap remain; `supplement/hang-760.png` shows all six door-wall works at 760x900; `final-sizes/mode-hang.png` shows the room and cutaway at 1366x768. Hang's wall compositing was left alone.
2. **FIXED, prior repair preserved.** `final-sizes/mode-checklist.png` shows all nine rows and both buttons at 1366x768; `supplement/checklist-680.png` shows eight rows, with Flow under the fold as the exit check accepted.
3. **FIXED, prior repair preserved.** `art.json`: all seven named files are 600x800 and below 50,000 bytes; largest is Crows, 49,372. Kitchen Window's clean right jamb is visible in the current Select and stop frames. No art was regenerated this round.
4. **FIXED, prior repair preserved.** Current Select frames show dimensions and tags on cards, with home highlighted (`final-sizes/default.png`, `mode-select.png`).
5. **FIXED, prior repair preserved.** The duplicate label remains a disclosure below the stage; `supplement/stop-1366.png` shows the painting and its wall label unobstructed.
6. **FIXED, prior repair preserved.** The persistent data-squeezed rule and resetWallLabels remain unchanged. Historical before/after proof is `_scratch/virtual-gallery/before/squeezed-moving.png` and `proof/squeezed-moving.png`; the exit check confirmed the closure. No new squeezed-label fix is claimed.
7. **FIXED, prior repair preserved.** `supplement/stop-1000.png` and `stop-680.png` retain the readable sharp wall label at the two named sizes.
8. **NOT FIXED in full.** Empty Hang itself has the correct emptyHang welcome and no fictional work title, as current audit frames confirm. However, the final audit found that empty Checklist Show me for Selection, Theme and Labels loses focus after entering Hang. showProblem() then targets controls which empty Hang does not render. Code inspection also confirms that the empty Labels branch overwrites the correct empty hint with Tap Label to edit although Label is absent. This is a remaining instance of the original empty Show me problem. Preserved the brief's one-pass/audit-last boundary and reported this new lead openly instead of claiming an unproved post-audit repair. The exact local follow-up is in handoff.md and the Audit section.
9. **FIXED, prior repair preserved.** `jump-voice.json` records two of two jump lines spoken without a cut, starting at 7545 and 12708 ms. Autoplay awaited both; `voice-shots/jump-voice.png` shows the completed two-jump walk. Normal timing and immediate transport logic were not changed.
10. **FIXED, prior repair preserved.** #hint remains the only shared feedback live region, and setHint plus rounded-position drag filtering remain unchanged. The separate import status stays live. The exit check confirmed this closure; no new screen-reader repair is claimed.
11. **FIXED, prior repair preserved as a warning.** `cheats.json` confirms six blank notes still show the warning and a 26-word note fails. Nine mechanical ticks with blank notes remain possible by the settled call, openly recorded below.
12. **FIXED, prior repair preserved.** The Line Why still calls 145 cm the tool's standing starting height, not Smithsonian guidance, and explains the lower small-item guidance for seated viewers. `cheats.json` includes the complete unchanged explanation. No new factual number or source was introduced.

## Polish accepted

1. **FIXED.** The named corner painting is visible and marked in `final-sizes/corner-1366.png`; the projected floor cone and outline still track the named back/side frame. Door-only now names nothing, draws no cone and passes no Anchor (`supplement/door-only.png/json`). This closes both manifestations linked to blocker 1.
2. **FIXED, prior repair preserved.** The show card stays compact and Label details remains below the stage at 680x425 (`supplement/stop-680.png`).
3. **FIXED, prior repair preserved.** Neighbor cards remain blank paper, without magnified text smears (`voice-shots/jump-voice.png`).
4. **FIXED, prior repair preserved.** The control remains Route: clockwise, and the active hint explains tray order. No visit-order semantics were changed.
5. **FIXED, prior repair preserved and null case corrected.** The completed walk compares First seen with the star (`voice-shots/jump-voice.png`). The comparison now requires a real first-seen id, so null/null cannot claim a match.
6. **FIXED, prior repair preserved.** Show me still explains the frame edge closest to straight ahead. Anchor Why now explicitly explains that door-wall works are behind the visitor, and the no-view result directs a back or side wall.
7. **FIXED, prior repair preserved.** selectMore still includes Star the one you most want seen, and lines.json still matches allLines(). The previous first-Add proof and cold exit check remain the evidence for that trigger; this round's main walk logs its expected stale drop when Hang is entered quickly.
8. **FIXED, prior repair preserved.** Number and star remain on the first title row; current six-work Walk and 680x425 Hang frames show them.
9. **FIXED, prior repair preserved.** The workbench still says wheelchair user's eye level (`final-sizes/mode-hang.png`).
10. **FIXED, prior repair preserved.** Kitchen Window's Anchor result has one full stop after a.m.; the same punctuation helper is used by the revised first-seen result.
11. **FIXED, prior repair preserved.** Order titles still wrap only at word boundaries; the current six-work 1366 frame and prior cold 680 proof retain that closure.
12. **FIXED, prior repair preserved.** Flow remains 0 jumps in tray order (1 allowed), visible in `cheats.json` and the current Checklist frame.
13. **FIXED.** Before, the 680x425 selector visibly read Back wal (`before/wall-plan-680.png`). It now reads Back, Right, Door R, Door L, Left, with full selected names in its accessible label and full names/dimensions in its title. At 680, the 63 px outside width leaves a conservative 35 px text budget; the longest choice measures 30.93 px. At 1366 with Plan open, that budget is 56 px (`picker-fit-680.json`, `picker-fit-1366.json`; matching inspected after frames). All remain 44 px targets. Updating retained controls also refreshes the full descriptions, rather than leaving a stale wall name. Tray captions remain complete at 680, as the exit check had already confirmed.
14. **FIXED, prior repair preserved.** The center-line slider retains cm/inch aria-valuetext on render and input; print retains plan-floor-print. Neither path was changed.
15. **FIXED, prior repair preserved.** `art.json`: blockmap 48,422 bytes; fireescape 48,842 bytes. Current Select frames retain their detail; no recompression this round.

## Settled calls

Applied all: card tags, missing-note warning instead of a new writing gate, honest allTicked and welcomeWalk wording, one-second moves and two-second stops except jump narration, straight-ahead door camera, Show me on every row, keyboard placement, Motion off, growing/night themeShort, privacy and tray visit order. The unattended door-wall decision follows the exit check's explicit interpretation: exclude surfaces behind the arriving visitor. All listed spec open questions remain outside this fix. No shared files, refine.md or refine/ files were edited; no git commits.

## Cheats tried

- Star each of the six door-wall works: zero Anchor passes.
- Reverse the order and sweep all 51 center-line settings, trying every star each time: zero Anchor passes.
- Add a visible left-wall work but keep a door-wall star: Anchor fails. An unhung star and an empty/null star also fail.
- Copy the displayed First seen id into Star: Anchor passes, as the settled calls explicitly allow. This is not a prediction gate and this repair does not claim to assess the student's intent.
- Six home-tagged works, Auto space, all lights, copying First seen, and statement x still produce nine measured ticks. The six-missing-notes warning remains. This is the accepted meaning-check limitation, not proof of a thoughtful exhibition. A 26-word note still fails. All ten scoped assertions are true in `cheats.json`.
- The offline probe recorded zero HTTP resources; all 37 allLines() strings match lines.json exactly.

## Voice walk

Held clicks, 0.12 s holds and 2 s gaps, following Select, Add, Hang, placement, Light, Walk: welcomeSelect, welcomeHang, lightHow, welcomeWalk, then firstSeen were spoken in action order (`voice-main.json`). The initial welcome was cut by the next action, permitted by baseline rule 16; selectMore became stale when Hang was entered, and lightHow was cut when Walk was entered. The changed firstSeen event itself spoke once, whole, at 13841 ms, naming the visible Kitchen Window. The door-only side path heard welcomeWalk and Read, with zero firstSeen announcements (`voice-door-only.json`). Both autoplay jump events finished whole, followed by walkComplete (`jump-voice.json`). No narration strings were added or removed; browser speech remains the draft fallback.

## Engine changes wanted

None. The geometry, selector and visibility repairs are local to the tool.

## Audit

Completed exactly once in 1922.75 seconds, exit 0, with a 2400-second outer limit, Chrome port 9911, host port 8715 and this round's chrome-prof-fix profile. Full report: `fix-audit/audit.md`. This is a completed audit with open findings, not an exit-gate pass.

All eight initial sizes are clean. The saved modes and states were inspected in 100 audit PNGs, packed in `audit-contact/`; the repaired legal corner, corner stop and door-only states remain correct. Motion off, ten five-held-click checks, ten two-quick-tap checks and mid-action resize recovery are clean, with no runtime exceptions or controls left disabled. The earlier focused offline probe recorded zero tool HTTP resources. The phone drive's favicon 404 belonged to its bare host page.

Every one of the 25 leads is answered below; the grouped counts sum to 25:

- **4 compact-checklist scroll rows, accepted limitation:** Checklist and Clear confirm, at 680x425 and 375x812. Eight checks fit in the preview; the empty phone checklist leaves Statement and Flow below the fold. The exit check accepts most checks fitting compact sizes. No claim that all nine are initially visible on a phone.
- **3 covered #hint rows, expected:** Label, Statement and Clear dialogs intentionally put the inactive footer behind native modal backdrops. The settled calls explicitly preserve these.
- **6 miniature-text rows, expected:** intro-panel text and title, plus two door-cutaway wall labels and their titles, measured at 3 to 8 local CSS pixels before the room transform. These are the miniature Hang rendering already accepted by the cold exit check. Full text remains in editors and print; Walk's readable screen labels are separately verified, including squeezed corners.
- **4 order-title clip rows, intended ellipses:** side-first-seen, legal-left-corner, all-door-wall and legal-left-corner-stop at 1366x768. The strip intentionally limits titles to two lines. Full titles remain in the enclosing buttons' accessible names and the current readable labels. No mid-word wrapping regression was seen.
- **4 lower-card focus rows, settled probe behavior:** Wave Bowl, Fire Escape Garden, Rain on the Window and Map of My Block were clicked at their unscrolled off-fold centers. The exit check explicitly distinguishes these from dead controls. No change to the working scrolled or keyboard path.
- **1 first-Add welcome row, settled:** Add to show replaces the welcome with selectMore, which includes the star instruction. Accepted by polish 7 and baseline rule 16; not a newly lost premise.
- **3 real empty Show me focus losses, NOT FIXED:** Selection, Theme and Labels enter empty Hang and then target controls absent from that panel. Source inspection also confirms that the empty Labels path replaces the correct empty hint with Tap Label to edit, although Label is absent. These are not the off-fold portfolio probes. The local repair is to handle an empty chosen list first in showProblem(), retain L.emptyHang and focus an enabled Select control with preventScroll, while preserving Statement and chosen-but-unhung guidance. The exact follow-up and reproduction sizes are in handoff.md. Kept the brief's single-pass/audit-last boundary; no unverified post-audit repair or second audit was claimed.


## Left open

- The spec's open questions, including deeper VA:Pr6, meaningful writing and locking the star, remain unchanged.
- Empty Checklist Show me for Selection, Theme and Labels has three real focus losses. The empty Labels hint also names an absent control. These remain open under should-fix 8; they are not the settled off-fold portfolio focus probes.
- The teapot x=520 disappearance did not reproduce in this browser run; its before and after frames both paint. The sibling legal corner failure did reproduce and is visibly repaired.
- Four initial read-only bootstrap commands lacked an explicit subprocess deadline. All subsequent shell commands used the bounded scratch runner; bundles were limited to 120 seconds, drive batches to 300 seconds, and the single audit to 2400 seconds. One malformed test setup and one shell-quoting error were corrected before accepting their evidence; failed frames were not counted as proof. Pillow was loaded from the existing scratch package folder after the default Python lacked it.
- The phone host generated one favicon.ico 404 from scripts/drive.py's host page, not from the bundled tool. There were no tool console errors in the successful focused batches. All 64 focused PNGs were inspected, including superseded diagnostic variants; final evidence is identified explicitly. The final bundle is 1,120,120 bytes. Source has no em dashes and no line over 160 characters.

All task Chrome and host ports were verified closed; host.html is absent. No second audit or post-audit browser run was started.
