# Polish: virtual-gallery (Codex fix, round 1)

Evidence root: `S:/CurioClass-codex/_scratch/virtual-gallery/`. Paths below are relative to that root.
Before frames and measurements are in `before/`; repaired frames and measurements are in `proof/`.
The required three door layouts pass, but an additional door-wall-only layout leaves the blocker open.

## Blocker

1. **NOT FIXED in full.** Widened the straight-ahead door view adaptively. The named back/side frame is now visible and outlined in `proof/last-door-back.png`, `last-door-sides.png`, and `last-door-side-anchor.png` at 1366x768. Before, the named side frame was outside the screen (`before/door-sides.png`; x=1490 on a 1366-wide screen). However, `proof/front-only-limit.png` reproduces a valid show entirely on the door wall: firstSeen() names Map of My Block, but the inward-facing frames cannot appear in a straight-ahead view. Widening alone cannot show their back-facing surfaces. Preserved the settled straight-ahead camera and the specified ranking rule; this needs a spec decision, detailed in handoff.md. A direct-state left-edge probe also did not paint, but bypassed the placement clamp by 3 cm; it is unconfirmed for a legal layout and is not counted as a pass.

## Should fix

1. **FIXED.** Hang unfolds the door wall with its door opening and pictures below the three-wall room. Before: four pictures painted while the status said six (`before/hang-1366.png`, `hang-760.png`). After: all six are visible at both named sizes in `proof/last-hang-1366.png` and `last-hang-760.png`. The unfolded walls share the same placement data and pointer coordinate mapping.
2. **FIXED.** Why and Show me are adjacent 44 px targets; rows are 64 px at 1366x768, with all nine visible, and 54 px in the 680x425 preview, with eight visible. Compare `before/checklist-1366.png` and `checklist-680.png` with the same names in `proof/`. Explanations open in a dialog instead of consuming a separate line in every row.
3. **FIXED.** Redrew all seven named works using built-in OpenAI imagegen, then art.py --rekey. Each is exactly 600x800, each below 50,000 bytes (largest: Crows, 49,372). Kitchen Window has a clean right jamb. Before: seven 800x622 files (`before-art.json`). After: `after-art.json`, `final-art.jpg`, `proof/select-1920.png` and `last-walk-1366.png`. Prompts and provenance are in art/prompts.json; raw PNGs are under art/raw/.
4. **FIXED.** All 14 portfolio cards have dimensions and theme tags, with the current brief's tag highlighted. `proof/offline-contract.json` records 14/14 cards with both fields. Compare `before/select-1920.png` with `proof/select-1920.png` and `select-final-1366.png`. Highlights also update when the custom theme changes or an imported work's tags change.
5. **FIXED.** Moved the duplicate label into a disclosure below the room. The work and its actual wall label stay unobstructed. Before overlap: `before/walk-1366.png`. After the same long note: `proof/last-walk-1366.png`; the reader begins at the room's bottom edge, with zero overlap.
6. **FIXED.** Squeezed labels retain a data-squeezed flag and visibility rule through every redraw and travel. Before: a vertical strip between touching frames in `before/squeezed-moving.png`. After: `proof/squeezed-moving.png` and `squeezed-stop.png`; the 6 px padded label remains hidden. Neighbor text is also blanked in Walk.
7. **FIXED.** Removed the <=1100 width rule that hid the sharp label, and drew the current label with readable screen text. Before/after: `before/walk-1000.png` versus `proof/last-walk-1000.png`, and the equivalent 680 frames. The 375x812 iframe also has one visible current wall label (`proof/phone-walk.png/json`).
8. **FIXED.** Empty Hang has its own emptyHang line and a workbench with no fictional selected work. Before: Creek After Rain and noWalk (`before/empty-hang.png/json`). After: `proof/empty-hang.png`, `voice-empty-side.json`; the hint and spoken welcome say the tray is empty and direct Select. Empty Show me uses that same guidance.
9. **FIXED.** Autoplay now awaits the jump voice promise and the normal two-second stop, whichever takes longer. Before: the first two completed jump lines were cut by hush (`before/jump-autoplay.json`). After: three of three finish without cuts in each Motion setting (`proof/jump-autoplay.json`, `jump-autoplay-calm.json`). With no jumps, eight stops still take 24.29 s (`eight-stop-timing.json`). Stop, Step, Back, Route and strip taps were also exercised; the strip tap selects stop 4 and stops autoplay immediately (`interrupt-strip.json`).
10. **FIXED.** #hint is the sole shared feedback live region; #announce is no longer live or written by feedback(). setHint avoids identical DOM writes, and a drag only changes its hint when wall/rounded position changes. Before: two live regions contained feedback (`before/*.json`, original feedback()). After: 35 stationary jitter samples produce one position hint and one final drop message (`proof/jitter-drag.json`), with no repeated position announcements. The separate own-image dialog status remains live for imports.
11. **FIXED as requested, not a new writing gate.** The Labels row starts with an explicit missing-note warning. Blank, whitespace-only and punctuation-only notes all retain it; a 26-word note still fails. `proof/check-causes-cheats.json` contains the results; `proof/checklist-680.png` shows the warning without opening Why. Nine measured ticks with blank notes remain possible by the settled call and are disclosed under Cheats tried.
12. **FIXED.** Line Why explains 145 cm as the tool's standing-viewer starting height, not Smithsonian guidance, and says the guide hangs small items lower for seated viewers (`proof/last-why-line.png`). Verified against [Smithsonian Guidelines for Accessible Exhibition Design, II.A](https://www.sifacilities.si.edu/sites/default/files/Files/Accessibility/accessible-exhibition-design1.pdf), PDF page 13. No new height was added to the screen. Notes explain the same distinction.

## Polish accepted

1. **NOT FIXED in full.** Replaced the decorative triangle with a floor-level projection toward the named frame and added its double outline. The back/side layouts show the outline and untinted artwork (`proof/last-door-*.png`). The door-wall-only case from blocker 1 cannot show the named frame, so that case still lacks a visible outlined target.
2. **FIXED.** At 680x425 the duplicate reader is below the room, and the show card is compact. The current work and sharp label are clear: `proof/last-walk-680.png`.
3. **FIXED.** Neighboring label paper stays, but its tiny text is blank in Walk. `proof/last-walk-1366.png` and `squeezed-moving.png` show no magnified text smears.
4. **FIXED.** The control says Route: clockwise/counterclockwise; the active hint explicitly says the visitor follows tray order. `proof/interrupt-direction.json` and `jump-autoplay.png`.
5. **FIXED.** The end recap compares First seen with the starred work. Both title fields are visible in `proof/eight-stop-timing.json` and `jump-autoplay.png`.
6. **FIXED.** Anchor's Show me names the frame edge closest to straight ahead from the door and tells the student to move the anchor there (`proof/show-anchor.png/json`). The door-wall-only specification limit still applies.
7. **FIXED.** selectMore now ends with Star the one you most want seen. A held Add to show as the first tap speaks it once, with no cut (`proof/voice-add-first.json`). Updated voice/lines.json.
8. **FIXED.** Numbers and the anchor star precede the title in the same text container. Both are fully visible at 1366 and 680 (`proof/last-walk-1366.png`, `last-walk-680.png`).
9. **FIXED.** The Hang band says wheelchair user's eye level. Teacher notes carry the same distinction (`proof/last-hang-1366.png`; Smithsonian II.A).
10. **FIXED.** Avoided a second sentence-ending period after a title that already has one, including selection feedback and the recap. The Kitchen Window anchor case passes in `proof/check-causes-cheats.json`.
11. **FIXED.** Order titles wrap at word boundaries. Compact cards place the image above the title, so Laundromat is fully visible in `proof/last-walk-680.png`.
12. **FIXED.** Flow says 0 jumps in tray order (1 allowed), with singular grammar for one jump. `proof/checklist-1366.png` and `check-causes-cheats.json`.
13. **NOT FIXED / incomplete proof.** Wall choices use short wall names and retain their dimensions in the select title. Desktop Plan is verified in `proof/hang-plan-1366.png`. Tray captions were shortened further to text such as 4★ hung, but the final audit failed before producing the required 680x425 frame of that final text. The earlier change to wrapping is not enough evidence to claim the final compact caption fixed.
14. **FIXED.** The slider's accessible text includes cm and inches on render and input. A sweep reaches 170 cm, 66.9 in. Print uses plan-floor-print instead of duplicating plan-floor-main. Both assertions pass in `proof/check-causes-cheats.json`.
15. **FIXED.** Map of My Block is 48,422 bytes; Fire Escape Garden is 48,842 bytes. Inspected both at card and large detail size (`proof/art-big-blockmap.png`, `art-big-fireescape.png`) and in `final-art.jpg`. `after-art.json` records the sizes.

## Settled calls

Applied all: visible card tags; blank-note warning rather than a new requirement; existing honest allTicked and welcomeWalk lines; normal 1 s moves/2 s stops except jump narration; straight-ahead door camera; Show me remains on ticked rows. Kept keyboard placement, Motion-off timing, growing/night themeShort, privacy wording, and tray visit order. Left the listed spec open questions unchanged. Unattended choice: preserved the explicit camera/ranking directions rather than silently resolving their door-wall conflict.

## Cheats tried

- Six home-tagged works, lights on, Auto space, copy First seen into Star, and statement x: all nine measured checks pass with a missing-note warning. This is the settled mechanical-check limitation, not evidence of meaningful writing or a good show. A stronger gate remains outside this fix scope.
- Blank notes, spaces, then punctuation: each keeps the warning. One-letter notes remove it, because the brief does not assess meaning. A 26-word note fails; 25 passes. Punctuation-only titles and statements fail; a 101-word statement fails. These cases are in `proof/check-causes-cheats.json` (25/25 assertions).
- Swept one wall's line through all 51 values while another used wall stayed at 145: only 142 through 148 pass. A wrong star fails; copying the displayed First seen into Star passes by the settled spec. Switching one light off fails; leaving one chosen work unhung fails Selection; unrelated neighbors fail Flow. Visible tags and Auto space remain explicit assists.
- Extra geometry attempts: the right side-edge layout paints its named frame (`proof/last-door-edge-right.png`). The direct-state left probe at 580 cm does not paint despite an in-window DOM box, but overran the normal clamp by 3 cm and needs a legal-placement re-check. All works on the door wall passes Anchor while its target is invisible. This is why blocker 1 and polish 1 are NOT FIXED in full; bounding boxes alone were not accepted as paint evidence.
- New numbers were recomputed in `numbers.json`: theme counts 6/5/5/4/2, door sides 340 cm, eight widest framed works plus gaps 685 cm, spacing spreads 14.29% and 16.54%, and 137 cm = 53.94 in. The spec's old 745 cm total remains unchanged, with the correction already documented in handoff.md.

## Voice walk

Held clicks, 0.12 s holds and 2 s gaps: welcomeSelect, selectMore, welcomeHang, lightHow, labelHow, welcomeWalk, firstSeen, welcomeChecklist in action order (`proof/voice-main.json`). selectMore speaks once across six Add actions; a separate six-visible-card path confirms six selected (`voice-six-visible.json`). First Add by itself hears the full new star instruction once (`voice-add-first.json`). Empty Hang hears emptyHang once; leaving the mode at 2 s cancels it as stale, and Show me restores the correct empty hint (`voice-empty-side.json`). Jump autoplay speaks all three event lines without cuts in both Motion settings. All 37 allLines() strings equal voice/lines.json, with no extras or omissions.

## Engine changes wanted

None. The unresolved door-wall case needs a specification decision about visibility or looking back, not a shared-kit edit.

## Audit

**Audit not finished.** Invoked exactly once, last, with a 2,400 s outer command limit, debug port 9921, host port 8725, and profile chrome-prof-fix. It exited on the driver's internal 60 s DevTools timeout while enabling a domain on the first size tab, before saving any stages or audit.md. No saved audit leads exist to assess, and no audit pass is claimed. The brief requires stopping instead of re-running it.

Final bundle is about 1.1 MB. Syntax check passes; source lines are at most 160 characters; no em dashes. The offline-contract probe records zero HTTP resources and loaded images. Actual keyboard deltas were +5/-25 cm, Delete returned the work, and Enter re-hung it. All immediate transport actions pass. A test-harness selector typo and Chrome connection failures were isolated and retried; successful logs are retained. The phone host's one favicon 404 belongs to scripts/drive.py's bare host page, not the bundled tool. The named fix sizes, phone iframe, grayscale and all four modes at 1366 were inspected, but exhaustive audit size/state/resize/voice coverage remains incomplete. No second audit or post-audit browser run was started. The failure is also recorded in `audit-failure.txt`. All assigned Chrome ports and host port 8725 were verified closed; host.html is absent. Four initial read-only bootstrap commands lacked an explicit process deadline; subsequent commands used limited.py with command-specific deadlines.

## Left open

- Blocker 1 and its linked cone/outline polish item remain open for the door-wall-only case; the left-edge direct-state probe also needs a legal-placement check. The three named back/side layouts pass. Do not approve this as a complete blocker fix.
- Polish 13's final compact tray-caption proof and the full audit remain incomplete. The code changes are present, but no unseen result is marked FIXED.
- The spec's own open questions, including meaningful writing, locking the star, VA:Pr6 depth and art provenance wording, were not changed.
- No recordings were generated; the draft continues using browser speech, as before this fix.
