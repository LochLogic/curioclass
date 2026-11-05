# Codex report: biome-atlas

## Built

Build only, completed 2026-10-30. No commits, branch changes or polish round.
Read, Key and Change are implemented in the offline biome-atlas.html bundle.
Includes 13 stations, branching answers, comparison checking, biome reveals, saved progress and painted succession.
The kit supplies the frame, Motion, Sound, Read, tones and Curio.voice.
Teacher notes, lesson plan, preview, prompts, voice lines, audit states and handoff are included.
tool.draft.json has stage built and status beta.
Browser narration is the intentional fallback; no audio was recorded.
Open questions follow the spec's leaning: one deliberate miss, HS-LS2-6 only, approximate succession times.

## Numbers check

PASS: independent Python recomputed every monthly array, all 13 annual T/P pairs, summer shares, dry lines and base results.
PASS: 12 matches and Dodge City's sole miss, using the spec's real-biome assignments.
PASS: all 11 listed what-if checks, independently and through the browser key.
PASS: all ten full recovery runs measured 7.977 to 8.081 seconds.
PASS: contrast is 7.37:1 brand/panel, 6.98:1 brand/section, 7.73:1 ink/brand; lowest pin-letter contrast is 5.17:1.
Numeric discrepancy retained: 8 years / 200 steps = 0.04 years.
The 0.3-year grassland milestone falls between manual positions 0.28 and 0.32; Play crosses it continuously.
FAIL, source verification: an independent WWF polygon point lookup was not completed. Supplied biome assignments were retained.
Reproduction script and numerical JSON: S:/CurioClass-codex/_scratch/biome-atlas/numbers_check.py and numbers-rechecked.json.

## Feel check

Best moment: clear Berlin, let the forest recover, then reduce rain by 50 percent and watch the late path become grassland.
The live card now shows 285.1 mm, the climate dot moves, and the Was / Key now says pair explains the changed destination.
The Dodge City forest/prairie reveal supplies the strongest surprise in Key.

Flattest moment 1: the first clearing and fire pictures already contained regrowth.
Changed: redrew bare soil, burned ground and scarred soil so the disturbance has a convincing starting point.

Flattest moment 2: Place on chart felt empty in the shortest preview because its destination inset was hidden.
Changed: fitted Climate space into short Read layouts and added the 600 ms dot flight.
Small Key layouts also gained a compact evidence chart; result narration now takes priority over an older instruction.

Compared the full-size atlas reveal beside the owner's Beat Lab frame, and opened Snowy Mail Route as the feedback bar.
The painted scene pair and instrument layout carry the finish. Large-screen succession trees remain softer than the scene cards.
Comparison: [side-by-side frame](S:/CurioClass-codex/_scratch/biome-atlas/feel-comparison.png).

## Done when

1. PASS: all station arrays and annual totals match; Kasama's plotted axis begins Jul. Numerical JSON and Read frames.
2. PASS: correct traversal of all 13 stations yields 12 matches, one Dodge City miss and tally 12 of 13.
3. PASS: Dodge City's D is 546.0 mm; its comparison is 558.9 mm is more than 546.0 mm.
4. PASS: Kumasi has four dry months and seasonal forest; Quillayute's 40.2 mm summer minimum gives temperate rainforest.
5. PASS: all 11 climate checks, including Utqiagvik +6 degrees giving boreal forest.
6. PASS: Berlin ends with oak/hickory at zero offsets; minus 50 percent rain ends in grassland with the might-stall note.
7. PASS: all ten biome stories run in about eight seconds; Kasama's shoots and full grass were separate observed phases.
8. PASS: Read chart, Key question, Reveal pair and Change landscape dominate their modes at 1366x768 and 680x425.
9. PASS: real jittered Years drag pauses; rain drag leaves Play running; Fire resets immediately and playback continues.
10. PASS: a real held Layer click produced all 13 correct biome letters and fills. layer-codes.json and its frame.
11. PASS: modes, station and focus fit at laptop and phone sizes; all 30 source assets load and contain no people.
12. PASS: held two-second input runs spoke each how-to once; match, miss and shifted each spoke twice.
The unkeyed Change hint names Go to Key; it does not name disabled recovery controls.
Evidence: build-evidence.json plus the Scratch functional, timing, input, voice and final-frame files.

## Wave lessons

- PASS, hint and voice: hint changes synchronously; Read uses it; how-to deduplication and event repetition checked.
- PASS, focus and layout: no focus on load; Key focuses its answer deliberately; pin activation and redraw preserve focus.
- PASS, sizes: every STANDARDS size checked, including the real 375 px iframe. Phone chips measure 44.42 by 44 px.
- PASS, no giveaways: unknown pins use question marks and unkeyed Change hides art. Real biomes is explicit opt-in.
- PASS, honest numbers: model omissions, approximate years, uniform what-if shifts and off-axis dots are explained.
- PASS, standards: students compare stable-climate recovery with a changed-climate destination themselves.
- PASS, Motion off: no infinite animation; timing logic is unchanged.
- PASS, short choice sets: all 13 number chips are visible together. Clear my progress is a secondary footer action.
- PASS, resize mid-action: the audit reported no exceptions and no controls left disabled.
- PASS, first-tap welcome: no welcomeAfter; a pin's own Place on chart instruction supersedes the stale welcome.
- PASS, unknown means unknown: neutral unkeyed pins and the empty locked landscape were inspected.
- PASS, one look/one meaning: bar, line, biome code and selected-ring meanings remain consistent; grayscale frame checked.
- PASS, truthful badges: Match/Miss compares the prediction with the supplied biome; tally also requires correct comparisons.
- PASS, hint changes back: station/mode/reset changes update it immediately; climate reset restores the current values.
- PASS, no answer by word copying: comparison questions require the displayed numbers; biome names arrive at the prediction.

## Audit leads

Ran audit_tool.py once, on port 9991 with host port 8795. It completed within its 30-minute cap.
It reported 82 leads. Every reported lead has an individual response in [audit-leads.md](audit-leads.md).
Actionable fixes: map caption clearance, pin spacing/hit behavior, restored pin focus, real hidden labels and 10 px captions.
Pin centers were then checked at 680, 1366 and 375 widths: all 13 were hittable in every frame.
Footer leads are secondary Clear my progress scrolling, not hidden answer choices. Reset remains visible.
Pin-welcome leads follow the required first-tap rule: Place on chart speaks instead.
Quick Reset/mode cuts intentionally hush speech; the standing rule marks a line heard when it starts.
Motion-off and resize-stress sections were clean; targeted follow-up shots had zero console errors.
The audit preceded the final focused fixes. It was not rerun.

Audit scope limits: header-only mode discovery misses these panel tabs.
Explicit states covered Key and Change; separate held-input runs covered their result events.
The first extrema recipes omitted the outer return and therefore kept zero offsets.
Recipes are corrected for the reviewer; independent what-if, real-drag and extrema tests supply the missing evidence.

## Frames looked at

All four mode/focus frames at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812.
All 65 audit PNGs were inspected in contact sheets; compact and phone audit sheets retained native frame sizes.
Also inspected first-playable frames, timing frames, functional frame, grayscale, Motion off, all-station labels and keyboard.
Inspected real scrub, running rain change, fire restart, climate extrema, repeated voice-result and blocked-storage frames.
Final follow-ups: three map sizes, phone Key/Change/Reveal, both ground fades, pin focus, persistence, layer codes and clearing zero.
All frames and recipes remain in S:/CurioClass-codex/_scratch/biome-atlas/.
Owned Chrome processes and servers were closed. host.html is removed.

## Art made

20 new succession assets, with three redraws: 23 generated takes. The ten original scene cards are retained.
All 30 painted assets ship inline. Art totals 1,358,692 bytes.
Final bundle: 1,975,350 bytes, below 2,000,000 bytes.
Raw selected art and rejected first takes are preserved in art/raw.
Every new image was generated with the image tool and processed only with art.py --rekey.
No people, external image downloads or placeholder assets remain.

## Art still to paint

None.

## Engine changes wanted

No family or kit engine change.
Shared audit tooling: scripts/audit_tool.py, MODES_JS should additionally discover main .seg[aria-label="Mode"] button.
Audit.steps should reject a missing/non-array drag result instead of silently replacing it with an empty list.
The exact reasons and workarounds are in handoff.md. Shared files were not edited.

## Left open

Independent WWF ecoregion point lookup remains required for source verification.
The spec's 200-step rule prevents selecting the 0.3-year milestone exactly; this is documented rather than silently changed.
The completed audit is a pre-follow-up snapshot with the scope limits above, not a claim of zero mechanical leads.
Narration recordings were intentionally not made in Build. The bank direction is preserved and browser speech works.
Tree layers look softer at the largest size because the full thirty-image set stays inside the bundle budget.

