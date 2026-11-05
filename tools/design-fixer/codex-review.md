# Codex review: design-fixer

## Played

Cold Grade 7 exploration of Studio and all ten Fix briefs before reading the builder's files. Repaired Bake Sale with real dragging and keyboard input, used the earned wipe, and checked projector/preview use. Squint and the live seesaw are strong.

## Findings fixed

- **Blocker, general, Contrast:** covered text could still earn All text readable and Fixed. Replaced unreliable detached-SVG shape queries with cached Canvas Path2D masks; sample preceding backgrounds and later occlusion. Covered text now fails and gets a move/Bring forward explanation. Confirmed in `review-followup/review-covered-text.png`.
- **Should fix, general, Studio:** Biscuit stayed locked without a client brief. Locks now apply only in Fix. Studio Bigger changed its width from 460 to 483; Fix pointer/key attempts kept it unchanged.
- **Should fix, general, selection:** small text had small targets. Added 44-pixel hit regions, actual-content priority where they overlap, and a part menu for unambiguous small/covered-part selection. Keyboard selected the Robotics date. Pale swatch boundaries now contrast 4.82:1 against the panel.
- **Should fix, general, typography:** forced stretching flattened letters and box height overstated cap height. Fit natural letter shapes, match the glyph masks, and use fitted cap height for readability thresholds. Rechecked size extremes and all ten reference repairs.
- **Should fix, general, voice/hints:** selection instructions could remain queued after an edit; Squint easing overwrote newer hints; returning to sharp in Fix gave Studio wording. Fixed validity and synchronous hints. All 51 fixed Read/narration lines match the manifest.
- **Should fix, general, part-menu narration:** a welcome held up the menu's selection instruction until an edit expired it. The kit only recognizes buttons for speaks; a local picker-focus validity guard now suppresses that welcome. Recheck: selectHow spoken once, welcome not spoken, no stale selection drop.
- **Should fix, general, comparison:** covered parts remained in Tab order, Squint stayed active without affecting the wipe, and Hint could name the hidden Before and after button. Removed background parts from Tab/accessibility content, dimmed the inert editor, disabled Squint, and made Hint describe the wipe. Opening/closing comparison hushes the previous view's speech.
- **Should fix, general, annotations:** compact comparison labels covered the title; gap labels could cover the date or clip at the page edge. Comparison labels now sit on the mat margins. Gap labels stay within the paper and omit collisions. Checked 680, 800, 1000, laptop, narrow and hosted-phone frames.
- **Polish, general, play/art:** lifted the flat rhythm repair with live edge-gap dimensions beside selected repeated parts. Added brief goal/stamp ink impressions, absent with Motion off. Redrew the severe angular cat as a smoother sitting pet with a curled tail. Kept the desk and every poster part.

## Findings left

- **Should fix, general, spec conflict:** short previews require panel scrolling; the specified 375-pixel phone stack puts tools and Read's hint below the first screen. All 44-pixel editing controls cannot fit alongside the required poster, five meters and brief in a 680x425 box. Kept the specified layouts and documented the conflict rather than changing the spec. Main laptop tools and hint fit at 1280x720 and 1366x768.

## Flattest moment left

**Polish, general:** Library Book Swap still needs repeated individual font/color edits. The part menu makes selection easier; an auto-fix or a new activity would change the specified play.

## Graphics

Checked the desk painting at final size and all ten vector posters. Retained the strong painting; redrew Biscuit in code because poster colors/geometry must remain measurable. No missing art tokens or people assets. Painting: 130.1 KiB. Final offline bundle: **274,158 bytes (267.7 KiB)**.

## Audit

Ran once, last, on Chrome 9931 and host 8735 with a 40-minute process-tree limit. Completed in **29.7 minutes**, with **329 raw leads**; inspected all **75 frames**. Evidence: `_scratch/design-fixer/review-audit/audit.md`.

Confirmed and repaired the picker instruction drop and comparison/annotation problems above. Remaining mechanical leads group into transparent expanded hit-region overlaps, the intentional wipe overlay, and the documented phone/preview scrolling. The comparison's covered parts are now excluded from Tab/accessibility content. Clear progress scrolling is a utility-row lead, not a hidden answer set.

Welcome misses on self-speaking controls are required first-tap behavior; Fix's welcome is present as a how line. Start over on a pristine poster intentionally changes nothing. Audit repeat/rapid-tap checks were clean; resize stress found no exceptions or stuck controls; Motion off had no infinite animation.

| Voice check | Expected | Observed |
|---|---:|---:|
| Selection instruction, five selections | 1 | 1 |
| Balance result, five new goal ticks | 5 | 5 |
| First Sound tap | 0 | 0 |
| First part-menu selection after repair | 1 selection, 0 welcome | 1 selection, 0 welcome |

Independent Python recomputed D65 pull/weight, tilt, repeated gaps and palette/locked constraints; all ten starts remain unsolved and all ten reference repairs meet their goals. WCAG pairs agree at 1.129829, 1.429077 and 7.903111. Module codes VA:Cr1, Cr2, Cr3 and Re8 have solo activities; notes open with the required three sections.

Only affected screens/voice paths were re-shot after audit repairs. Final drives had no console errors or warnings. No second full audit, commits, shared-source changes or out-of-scope writes. Owned Chrome/server processes closed; host.html removed.

## Left open

- The layout conflict above needs a spec decision, not a hidden exception.
- Browser narration remains the fallback; the brief prohibits recording audio.
- Contrast uses finite sampling and can miss extremely small overlaps. Pull/weight use editable box area as specified; a tick is a model check, not an aesthetic verdict.
- Spec arithmetic: 18.7 / 24 is 0.77917, not 0.8. Kept the stated 3 percent and 2.4 percent thresholds.
- Kit change wanted is detailed in handoff.md: Curio.voice's first-tap target lookup should include native selects/inputs when matching speaks. The tool has a working local guard; the shared kit was untouched.
