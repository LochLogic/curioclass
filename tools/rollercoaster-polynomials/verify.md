FIX (3 should fix, 4 nits, no blockers)

# Verify: rollercoaster-polynomials (2026-10-25)

Checked cold against spec.md, POLISH.md, BATCH-G11.md and docs/families/graphing.md. Draft bundle (`CURIO_DRAFT=1`), frames from scripts/shoot.py plus DOM dumps from headless Chrome, all kept in my scratchpad.

## What passed

- **Math, recomputed in numpy:** every Survey plan expands to its factored form. Plan 9 has real root 1 and roots plus or minus i. Plan 8 is 0 at 0.5. Every order's working track hits its listed numbers: C1 16 m; C2 32 m; C3 37.83 up, 25.7 deep; C4 73.61 up, 24.15 deep; C5 42.7 up, 18.56 deep; C6 22.78 on all three hills. Blueprints: B1 20; B2 20.75 and 12.6; B3 59.88 (about 60); B4 49.07 and 16.1. The tool's readouts match these to 0.1 m. The synthetic division tables are right for every plan: the multiply row, the sum row and the boxed remainder (for example Plan 4 at c = 5 gives -72, Plan 8 at 0.5 gives 0). The check tables agree at -2, 0 and 2. Multiplication steps match too: the degree 6 example expands to 0.01x⁶ + 0.06x⁵ − 0.17x⁴ − 1.08x³ + 0.79x² + 3.9x + 2.25, same as numpy.
- **Done when 1 to 8 all hold:** default track and readouts; touch and flat-cross signs either side of the zero; merge, refusing a merge past multiplicity 3, and Split (degree kept); the degree 6 cap greys buttons with a note; no zeros or one zero disables Ride and shows the right tip; typing 0 for a is refused and restores the last value; Ride with Motion on (readout, contact list) and off (contacts listed); Plan 3, 9 and 8 sequences; all six orders and four blueprints approve; a 10 percent wrong a does not match (4 percent does).
- **Keyboard:** footing arrows (0.5, or 0.1 with Snap off), keys 1/2/3 and Delete all work, and focus comes back to the rebuilt footing. Stake arrows and Enter work, and so does Enter on the page body in Survey. Focus ring uses `--focus`.
- **Contract and words:** one file, no network requests (the only URL is the SVG namespace). No em dashes in any tool, kit or doc file. "Curio" alone appears only as the JS API name. Voice lines are word for word the same in spec, `voice/lines.json`, `L` and `allLines()` (14 lines), with bank, voice and style set per the batch. Art: one prompt, `people: false`, no people asked for. Nothing in Survey or the blueprints gives the answer away (the factored form and the blueprint equation show only once solved or matched).
- **kit/graphing.js:** the API matches graphing.md (Plane options, fn/param/point/segment/label/trace/view/slider/clear/layer/onClick/onView, `lock`, `hit`, `shape: 'none'`, `body`, series dash patterns, Plane.fmt/fmtSig/roots/extrema/slider). It has no tool-specific code.
- **kit/theme-912.css:** sets all ten required variables plus the readout font, slider, `.btn`, `.sec` and `table.inst`. My computed WCAG ratios: ink/panel 14.7, muted/sec-bg 7.71, brand/sec-bg 8.21, brand-ink/brand 9.25, ok 9.73, warn 9.90, focus/panel 12.0, btn-line 3.65/3.44 (non-text, needs 3:1), gr-1..4 on gr-bg 7.46 to 9.83, tick text on the stage 8.89. All pass AA. bundle_tool.py inlines `kit:NAME` css.

## Findings

1. **Survey, post value labels overlap** (src.html:802-805). How seen: frame s_p4posts (Plan 4, posts at -5..5 by halves). "−7.88" (x = 0.5) is printed over "−12" (x = 0, a cut post). The "−72" label at x = 5 is right-aligned onto the post at x = 4.5, next to "−46.88". The stagger only alternates on the half-step parity, and every cut label shares y = 580 or 30. Should fix.
2. **Ride with Motion off: the car can't be seen** (src.html:704-705, 680-684). How seen: frame b_ridecalm. The car is placed at End, tilted to the slope there (84 degrees on that track), on the `front` layer under the End footing diamond, so it disappears into the footing and the tunnel cut. With Motion on, the finished ride also leaves the car on top of the End diamond (b_rideend). Should fix (place it just inside End, or level it on the platform).
3. **Medium and narrow windows** (src.html:23-24, 46). How seen: an iframe host at 760 and 375 px wide (narrow.png). From 760 px the two-column layout leaves the stage about 360 px wide. The plane scales to about 0.4, so tick text is about 5 px and the 60 px footing and stake targets shrink to about 24 px, under the 44 px rule (Done when 9). At 375 px the zero rows overflow and the Remove buttons are clipped at the right edge. Laptops at full width are fine (1024x768 frame is fine). Should fix.
4. **Merge tip lost** (src.html:508-510 against 633-636). Merging the only two zeros sets "Merged: ..." and then `update()` replaces it with "A ride needs two ground points...". The tip should say both, or keep the merge first. Nit.
5. **Footing at x = -6** (b_edges): the diamond covers the "0" y-tick label, and the Start platform is clipped off the plane (only the label shows). Nit.
6. **theme-912.css:7 comment** says gr colors are "7.5:1 or more", but gr-1 on gr-bg is 7.46. Nit (still passes).
7. **Blueprint reveal text is stale** across cards while hidden (`#cReveal` keeps B1's equation when B2 opens; `hidden`, so nothing shows). Harmless. Nit.

## Not defects, but open

- The art (night-fairground) is not painted yet: the draft placeholder shows faintly behind the stage. None of the 14 voice lines are recorded yet. tool.draft.json correctly keeps the tool on the bench.

## What I could not check

Tones, chime and Read voice (headless, not listened to); real pointer drags (I used keyboard and the `__tool` helpers); screen reader output. The 760 px target sizes are estimated from the frame scale.

## Re-verify

PASS (all 3 should-fix and 4 nits fixed; 3 new nits, no blockers)

Cold re-check, 2026-10-25. Rebundled with `CURIO_DRAFT=1` (469 KB). Frames from scripts/shoot.py and an iframe host at 375, 760 and 1024 px (headless Chrome will not shrink its window below about 500 px), with DOM measurements, all in my scratchpad.

### Earlier findings

1. **Survey post labels overlap:** fixed. Frame p4posts (Plan 4, posts at -5..5 by halves): every label now has its own box (src.html:820-840 places them against all earlier labels). "−7.88" sits below "−12", "−72" sits clear above "−46.88" next to the x = 5 post. All 21 values readable.
2. **Car hidden after a ride:** fixed. `parkCar` (src.html:688-692) sets the car level on the End platform. Seen in ridecalm (Motion off) and rideend (Motion on, after the run): car upright and clear of the End diamond.
3. **Medium and narrow windows:** fixed. Two columns only from 1000 px (src.html:24-26). At 760 the stage is 760 wide, the plane near full size, footing targets 60x60 px. At 375 the footing targets are 46x46 (hit radius scales with the stage, src.html:684-687), page scrollWidth 375, zero rows wrap with Remove fully visible, no control under 44 px. At 1024 targets are 49x49.
4. **Merge tip lost:** fixed. Merging the only two zeros now shows "Merged: x = 4 now has multiplicity 2 (touches and turns back). A ride needs two ground points to start and end." (checked live).
5. **Footing at x = -6:** fixed. Frame edges: the "0" y-tick is clear of the diamond and the Start platform moves to the inner side, fully on the plane (same for End at 6).
6. **theme-912.css comment:** fixed, now "7.4:1 or more (gr-1 7.46:1)".
7. **Stale blueprint reveal:** fixed. `openCard` clears `#cReveal` (src.html:1016).

### No regressions

- Default Build screen at 1400, 1024, 760 and 375: matches the earlier pass (equation, zero rows, readouts, 32 m at x = 0).
- Survey Plan 3 end to end: footing at −1, double check, footing at 2; fog lifts, factored form "(x + 1)²(x − 2)", check table equal at −2, 0, 2.
- Commission C1 with a = −0.375, zeros −2 and 2: all four lines met, APPROVED stamp, 15 m readout.
- Art and voice inlined: `night-fairground.webp` (1600x914, dusk fairground, no people) inlined as `data:image/webp`, no draft stand-in. `"voice:*"` replaced with 14 `data:audio/mpeg` clips, one per line of voice/lines.json, keyed word for word. No em dashes in src.html, notes.md or theme-912.css.

### New nits

8. **Parked car covers the "End" label** (src.html:688-692, frame rideend and ridecalm): after a ride the car sits over the station label, so "End" is gone until the next edit. Nit.
9. **Plan 4 "−1.13" label touches the multiplicity badge** of the found footing at x = 2 (frame p4posts): footing badges are not in the label collision set. Still readable. Nit.
10. **Ride readout spacing collapses** (src.html:681): the triple spaces render as one, so it reads "x = 4 P(x) = 0 height 0 m, at ground level Arrived at End." Needs separators (comma or line break). Nit.

Still not checked: tones, chime and the recorded voice played aloud, real pointer drags, screen reader output. At 375 px the plane draws at about 0.4 scale, so tick text is about 4 px. Targets still meet 44 px, and students use laptops, so I did not count it as a finding.
