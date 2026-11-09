# Polish: virtual-gallery (Codex fix, round 3 narrow follow-up)

Active list: refine.md's updated first-line verdict and Exit check round 2. The prior completed reports remain polish-1.md and polish-2.md. Evidence root for this pass: `_scratch/virtual-gallery/round3/`.

## Blocker

1. **FIXED, prior closure retained.** The cold round 2 exit check confirms every door layout, including legal far-left frames and the door-only null result. This pass changes no camera, ranking, art, cone or frame styling. Default/mode and legal-left-corner regression frames recheck the retained presentation.

## Should fix

1. **FIXED, prior closure retained.** Door cutaway and its real placement data are untouched.
2. **FIXED, prior closure retained.** Two-column checklist and compact scrolling allowance are unchanged.
3. **FIXED, prior closure retained.** Seven portrait replacements and Kitchen Window crop are unchanged.
4. **FIXED, prior closure retained.** Card dimensions and highlighted theme tags are unchanged.
5. **FIXED, prior closure retained.** Label details stays below the stage; readable stop label placement is unchanged.
6. **FIXED, prior closure retained.** Persistent squeezed-label visibility is unchanged.
7. **FIXED, prior closure retained.** Readable labels, including squeezed-corner stop labels from round 2, are unchanged.
8. **FIXED.** Reproduced Selection, Theme and Labels Show me on an empty show with real 0.12-second held clicks at 1366x768 and 680x425. All six before measurements record focus BODY; Labels names the absent Label control. Added one early empty-show guard in showProblem(), before per-work selection or target lookup. Every empty non-Statement request now enters Hang, retains L.emptyHang and focuses the enabled Select mode button with preventScroll. Statement and chosen-work paths bypass this guard. Six inspected after frames in after/ repeat the exact before clicks and sizes. Every after JSON records focus m-select and the exact emptyHang hint; all before JSONs recorded BODY. No phantom Label or wall picker is rendered. The final audit control table also records rebuilt, focus kept for Selection, Theme and Labels Show me, including its two Enter presses; the three dedicated states add no leads at either named size.
9. **FIXED, prior closure retained.** Jump narration timing and immediate transport code are unchanged.
10. **FIXED, prior closure retained.** Shared live region and rounded drag-message filtering are unchanged.
11. **FIXED, prior closure retained.** Missing-note warning and settled format-only checks are unchanged.
12. **FIXED, prior closure retained.** Standing start and seated-viewer guidance are unchanged; no fact or number was added.

## Polish accepted

1. **FIXED, prior closure retained.** Cone and outline geometry unchanged.
2. **FIXED, prior closure retained.** Compact overlays unchanged.
3. **FIXED, prior closure retained.** Neighbor label text blanking unchanged.
4. **FIXED, prior closure retained.** Route naming and tray order unchanged.
5. **FIXED, prior closure retained.** End recap and null guard unchanged.
6. **FIXED, prior closure retained.** Anchor explanation unchanged for shows with works; empty Anchor gets the same truthful empty guidance as before.
7. **FIXED, prior closure retained.** selectMore retains its star instruction.
8. **FIXED, prior closure retained.** Strip numbering and stars unchanged.
9. **FIXED, prior closure retained.** Wheelchair eye-level wording unchanged.
10. **FIXED, prior closure retained.** Title punctuation helper unchanged.
11. **FIXED, prior closure retained.** Word-boundary wrapping unchanged.
12. **FIXED, prior closure retained.** Flow wording unchanged.
13. **FIXED, prior closure retained.** Short wall choices, complete tray captions and accessible full wall names unchanged.
14. **FIXED, prior closure retained.** Slider valuetext and print pattern id unchanged.
15. **FIXED, prior closure retained.** Compressed image assets unchanged.

## Settled calls

Applied unchanged: visible tags, blank-note warning rather than a new writing gate, existing allTicked and welcomeWalk lines, walk timing, straight-ahead camera, Show me on every row, keyboard placement, Motion off, themeShort and privacy. No spec open question was implemented. Unattended choice follows the exit check's narrow direction: direct every empty non-Statement request to the existing Select control. No shared file, refine.md or refine/ edit, and no git commit.

## Cheats tried

All nine empty-show Show me buttons were swept with real held clicks, returning to Checklist between each: zero chosen works and zero passing checks afterward (empty-showme-sweep.json). No title, note, statement or placement was synthesized. Two further paths were tried at both 1366 and 680: empty Statement stays focused on its enabled editor button and still fails its unwritten check; selecting a work with a 26-word note and tapping Labels Show me focuses the real editor and still fails Labels. The settled copy-First-seen, blank-note warning and meaning-check limitations remain unchanged.

## Voice walk

Held clicks at 0.12 seconds with 2-second gaps: empty-welcome.json records emptyHang spoken once, whole, at the empty Show me destination. voice-empty.json records the same line and Read repeating that exact hint; the Read press intentionally interrupts the automatic welcome. Normal main path: welcomeSelect, welcomeHang, lightHow, welcomeWalk, firstSeen in order (voice-main.json); the early Select welcome and lightHow are cut by later student actions, and the queued selectMore becomes stale on Hang, as the settled baseline permits. No line falsely names Label in empty Hang. All 37 allLines() strings equal voice/lines.json; no narration text was changed.

## Engine changes wanted

None. The fix is local to showProblem().

## Audit

Completed exactly once in 1961.08 seconds (32 minutes 41 seconds), exit 0, within the 2400-second outer limit. Chrome port 9911, host port 8715, profile round3/chrome-prof-fix. Full report: `fix-audit/audit.md`. All 106 audit PNGs were inspected in `audit-contact/`.

Eight initial sizes are clean, including the phone iframe. The three added empty Show me states have no leads at 1366x768 or 680x425. In the full Checklist control table, Selection, Theme and Labels Show me now all say rebuilt, focus kept; the later Enter presses are also clean. The former three real focus losses are gone. Motion off, ten five-held-click checks, ten two-quick-tap checks and mid-action resize recovery are clean. No runtime exceptions or controls left disabled. The focused offline probe recorded zero HTTP resources and all 37 voice declarations match allLines().

The remaining 22 leads are the settled cases below. Counts cover every saved row:

- **4 compact checklist scroll rows:** Checklist and Clear confirm at 680x425 and 375x812. Flow is under the fold in the preview; Statement and Flow are below it in the empty phone checklist. The exit check accepts most rows fitting compact sizes. No claim of nine initially visible on a phone.
- **3 covered-hint rows:** Label, Statement and Clear dialogs intentionally put the inactive footer behind their native modal backdrops. Preserved as the settled calls require.
- **6 miniature-text rows:** intro panel and its title, plus two cutaway wall-label cards and their titles, measured at 3 to 8 local CSS pixels. These are the scaled Hang rendering already settled by the exit check; editors and print retain the full text, and Walk's readable labels remain separate.
- **4 order-title clipping rows:** side-first-seen, legal-left-corner, all-door-wall and legal-left-corner-stop at 1366x768. Intentional two-line ellipses; whole titles remain in the parent buttons' accessible names and current readable labels. No mid-word wrap regression.
- **4 off-fold portfolio focus probes:** Wave Bowl, Fire Escape Garden, Rain on the Window and Map of My Block were clicked at unscrolled off-fold centers. These are the settled audit probes, not the three empty Show me failures repaired here.
- **1 first-Add welcome row:** Add to show replaces the welcome with selectMore, whose star instruction is retained. Accepted by polish 7 and baseline rule 16.

No new actionable lead remains from this audit. No second audit, post-audit code repair or post-audit browser run was started.


## Left open

No reopened blocker or should-fix remains in this narrow follow-up. The spec open questions and settled meaning-check limitations remain unchanged. All 31 focused PNGs were inspected: before, after, checks, voice and regression folders. Default and every mode were re-shot at 1366x768; the legal left corner remains painted. Keyboard recovery at 680x425 moves to Select on Enter with focus retained. Bundle: 1,120,376 bytes; no focused console errors, zero HTTP resources in the offline probe, maximum source line 160 characters, no em dashes. Every command in this follow-up used a process deadline.

All task Chrome and host ports were verified closed. host.html is absent. No second audit or post-audit browser run was started.
