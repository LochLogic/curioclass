# Polish: living-pond (Codex fix, round 1)

Evidence is relative to `_scratch/living-pond/`. All listed frames were opened and inspected. The source is an open-ended Curiosity; its numerical ecosystem was preserved.

## Blocker
None in refine.md.

## Should fix
1. FIXED: Six plain event readings now use V.say, current-state validity, four-second expiry and a per-line 20-second cooldown. `fix-before/before-events.png` and `before-events.json` show the old silence; `voice-ice.json`, `voice-low.json`, `voice-winterkill.json`, `voice-heron.json`, `voice-turtle.json`, `voice-snails.json` each show one matching spoken event at 1366x768. Seven fixed lines match allLines and voice/lines.json. Browser speech remains the recording fallback.
2. FIXED: All seven dropdowns became six detented rotary switches and one decomposer lever, preserving values, defaults and shortcuts. Arrow keys, Home/End and printed accessible value text work. `before-default.json`: 7 selects; `after-default.json`: 0. `fix-targeted/final-rotary-keys.png` and `switches-all-ends.json` cover all values and roles at 1366x768.
3. FIXED: Separate Floating and Stems traces, chips and end labels show the cascade. `fix-before/before-cascade.png` versus `fix-after/after-cascade.png`, both 1366x768; at the same week floating = 43.03 clumps, stems = 0.744 clumps. The populations did not change, only their recording.
4. FIXED: Four stem-algae hitboxes anchor the snail/turtle food routes. `fix-before/before-turtle.png` versus `fix-after/after-turtle.png` at 1366x768; before 0 stem anchors, after 4 (`after-turtle.json`). Stem algae can also be inspected.
5. FIXED: The rim hint stays visible before interaction at 680x425, 800x500, 760x900 and 375x812 in the iframe host. Matching `fix-before/before-hint-*.png`, `before-phone.png` and `fix-after/after-hint-*.png`, `fix-phone-closeout/final-phone.png`; computed display changed from none to block at each width.
6. FIXED: First Add or Food sets the stocking flag before the hint's validity is tested. `before-add-hint.json` records the old late spoken hint; `after-add-hint.json` and `voice-food-first.json` have empty voice logs after those first actions, at 1366x768. A first non-stocking touch still speaks the hint once.
7. FIXED: Whole run has its own dark pressed fill. Before: white on transparent; after: white on rgb(11,79,86), 9.26:1 nominal contrast. `fix-before/before-whole.png` versus `fix-after/after-whole.png`, 1366x768.
8. FIXED: The oxygen arc has a red 0 to 3 band, actual ticks at 2 and 3, and the labels fish gasp / winterkill at every width. `fix-before/before-hint-680.png` versus `fix-final/final-short-ledger.png` at 680x425; `fix-after/after-default.png` at 1366x768 and phone closeout show the same marks. The Manual identifies the thresholds as model choices.
9. FIXED: Energy shows the last closed year beside the current year. `fix-before/before-year-boundary.png` versus `fix-after/after-year-boundary.png`, 1366x768. At week 52 the previous caught = 25136.25 and heat = 25756.49 remain visible (102.5 percent), while the new year starts at zero.
10. FIXED: Matter Enter follows the dot nearest the arrow-key drop point and shows weeks in its current pool. Matching `before-matter-key.json` / `after-matter-key.json`: pool 14 (Muck) became pool 1 (the targeted Floating algae). `fix-after/after-short-matter.png` shows Muck, 4 weeks here at 680x425; `matter-direct-breakdown.json` records a trip reaching Snails and Minnow without changing flows. Netting a tracked turtle and a turtle walking away both reset the outside wait to 0 weeks (`tracker-exit-wait.json`).
11. FIXED: Recorder, Matter, Energy, food-web and honesty sections start with plain explanations; exact model terms are inside optional details. Energy labels now say Algae kept, Plant eaters kept and using stored food. `fix-before/before-manual.png`, `fix-after/after-manual.png`, and `fix-regressions/regression-energy.png`, all 1366x768.
12. FIXED: The feeding finding now states six winterkill winters and 0.86 remaining minnows. `before-feeding-shade.json` reproduces those values; `fix-targeted/final-manual-finds.png` shows the corrected entry at 1366x768. No false promise that Some preserves the school remains in this entry.
13. FIXED: Every one of the ten findings names real-world scientific context and distinguishes its own model result. The Manual and metadata name licences or reference-only copyright status. `before-manual.json` versus `after-manual.json`, plus `fix-targeted/final-manual-finds.png` at 1366x768. Source verification is recorded below.
14. FIXED: Both the honesty paragraph and visible/accessible algae inspection explain carbon dioxide and water, sunlight, and the small nutrient share combined into Water & air. `before-manual.json` lacks this explanation; `fix-targeted/final-algae-inspect.png` and `final-algae-inspect.json` show it at 1366x768.
15. FIXED: Optional Shade history is off by default, with its own dash, chip and end label, scaled separately from 0 to 7. `before-default.json` has no Shade key; `fix-targeted/final-shade-history.png` shows 523 stored samples from 3.50 to 1.21, with Whole run enabled, at 1366x768. Population calculations are unchanged.
16. FIXED: Full-capacity messages use plurals. `before-full-status.json`: The pond is full of minnow. `after-full-status.json`: No room for more minnows. Matching frames in fix-before and fix-after are 1366x768; the same map covers snails, herons, turtles and nymphs.

## Polish accepted
1. FIXED: Latest log event is a quiet tank-rim readout; the full log stays in the Manual. `fix-after/after-events.png`, 1366x768, and `fix-final/final-short-ledger.png`, 680x425.
2. FIXED: Sun, kept food and named heat columns are labelled; fixed-adult heat belongs to the eater, and decomposition has its own column. `fix-targeted/final-heron-heat.png`, 1366x768; attribution numbers in `final-heron-heat.json`. Phone closeout separates the labels into three rows. Final eater metadata also attributes ordinary digestion to the eater, including fish-food heat. `energy-attribution-energy.json`: all respiration = 76.70810711193283, all named columns = 76.70810711193279; nymph digestion = 1.9511018345507336 and fish-food digestion = 2.8058484610706054 are included. Final frames: `fix-post-audit/final-energy-attribution-energy.png`, `fix-last-energy/energy-labels-*.png` and `fix-last-proof/clear-energy-labels-*.png`.
3. FIXED: A direct Muck-to-Water & air trip says broken down by decomposers. `matter-direct-breakdown.json` and `fix-final/matter-direct-breakdown.png`, 1366x768. Paths actually visiting the decomposer body pool retain that pool name.
4. FIXED: Ghost alpha is 0.35 with long dashes. `fix-after/after-cascade.png`, 1366x768; actual traces remain dark with distinct dashes.
5. FIXED: Counts omit 1 = 1, retain 1 = N only above one, and stay on one line in net mode. `fix-final/final-net-tray.png` and JSON: every count's scroll width equals its client width at 1366x768. Compact net layout is checked by the audit.
6. FIXED: Ice is thicker, edges extend inward, the water dims, and fish motion slows to 0.35 under ice. `fix-targeted/final-winter-three.png`, 1366x768. Colour changes remain when Motion is off.
7. FIXED: At 1280 and wider the legend is 13 px, chart end labels 12 px and meter labels 12 px, versus 10/11 px before. `fix-after/after-1280.png`, `after-default.png`, `after-1920.png`.
8. FIXED: Chart/meter rendering is cached until a change; Motion off skips idle tank drawing; a swipe builds one ghost on release. `performance-calm.json`: unchanged draw counts across 2 seconds. `performance-swipe.json`: six scoops, one ghost. Four-times CPU throttle: 180 frames, 1 above 25 ms, 59.67 fps (`fix-performance/throttle.json` and frame). This is a desktop test, not a Chromebook guarantee.
9. FIXED: Splash, net and ice use filtered noise buffers, retaining the 150 ms gate and Fast rule. `sound-buffer-evidence.json`: 0.13 s splash and 0.24 s ice, running AudioContext; `net-noise.json`: 0.18 s swish. No recorded audio or downloaded sound was added.
10. FIXED: At 680x425 the legend sits in the top plot margin, clear of the right end labels; 52 px of trace height remain. Oxygen value moved above the arc. `fix-before/before-hint-680.png` versus `fix-final/final-short-ledger.png`; `final-short-recorder.json` records the plot dimensions.
11. FIXED: The New dialog now labels its existing save action Save only. `fix-targeted/final-save-only.png`, 1366x768.
12. FIXED: Habitat closes on Escape and an outside tap at 680x425. `final-habitat-escape.json` and `final-habitat-outside.json` both report open false; matching fix-targeted frames were inspected.
13. FIXED: The station plate moved left of the right-hand reeds. `fix-after/after-default.png`, `after-hint-760.png` and phone closeout.
14. FIXED: At 680x425 Matter shows IN POND and trip; Energy shows caught and heat, with last-year values alongside. `fix-after/after-short-matter.png`, `fix-final/final-short-ledger.png`; Energy ledger is 38 px high, down from the tall six-line panel.
15. FIXED: Sleeping turtles are 95 px apart on the wide tank. `fix-targeted/final-winter-three.png` shows all three asleep without overlap at 1366x768. At 375x812 the three turtles are 87.6 px apart, each 77 px wide (`phone-three-asleep.json` and `fix-last-proof/phone-three-asleep.png`). The narrow arrangement keeps all three inside the tank.
16. FIXED: An unstocked Empty pond says NO TURTLE and NO HERON. `fix-after/after-empty.png`, 1366x768. Departures retain their actual walked/flew-off wording.
17. FIXED: The muck finding says 20 clumps (100 units). `fix-regressions/muck-finding-corrected.png` and JSON, 1366x768.
18. FIXED: Turtle and heron inspection both show arrows to Muck, matching the existing 30 percent transfers. `fix-after/after-turtle.png` and `after-heron.png`, 1366x768.
19. FIXED: Run/Hold has plain text and an action-specific accessible name, with no aria-pressed or Roman numeral. `fix-after/after-default.png` and source; keyboard focus frame confirms the controls remain reachable.
20. FIXED: Calendar Year uses Consolas/monospace. `fix-after/after-default.png`, 1366x768.
21. FIXED: Replay saves and restores its prior speed. `replay-restored.json`: restored Slow = 1, week 8, held; `fix-final/replay-restored.png`, 1366x768.
22. FIXED: Keyboard focus uses a 3 px inside outline. `focus-keyboard.json`: focus-visible true, offset -5 px; `fix-final/focus-keyboard.png`, 1366x768.

## Settled calls
Applied all: event readings are factual, hint follows first non-stocking touch, the wooden log remains on the right, matter weights are unchanged, actual run numbers are preserved, switch values/defaults remain unchanged, shade history is optional, and no lesson structure was added. The Curiosity brief takes precedence over welcome/goal/score/finish audit conventions. No spec open question was changed. The old OpenStax licence error remains a spec-maintenance issue; the tool says current CC BY-NC-SA reference only.

## Cheats tried
- Oxygen: rapid Food taps stop at 30 units per week; overfeeding still causes low oxygen and winterkill. No score or pass can be earned by tapping.
- Swept all seven switches through every detent: all values and accessible labels match, matter remains 742.0. The oxygen meter stays a numeric model output, not a success badge.
- Net swipe at the limit: six removals, one pre-change ghost. Additional contacts do not exceed the swipe cap.
- Matter: keyboard targeting chooses an actual drawn dot; changing the target does not change the conservative transfer weights. A direct muck trip reached Snails and Minnow and recorded the wait.
- Voice: repeated Ice requests inside the cooldown produce one spoken Ice line. A Heron line queued behind winterkill is dropped stale after the heron is present again (`voice-stale-dropped.json`), with an empty queue.

## Voice walk
Held clicks used 0.12-second presses, with 2-second gaps. First Run: hint once. Natural model transitions were positioned immediately before the event, then advanced: ice at week 42, low oxygen at week 52, winterkill at week 101, heron departure at week 16, turtle departure at week 34, snails gone at week 69. Each matching event has one spoken log entry. First Add and Food produce no stale hint. Read retains the live calendar, oxygen, temperature, counts and dated latest log line; queued events cannot interrupt it. Files: fix-voice/*.png, voice-*.json, fix-final/voice-stale-dropped.png. No ranger clips were available; the existing offline browser voice supplies speech.

## The real material
No ecological dataset was downloaded, sampled or added. Original model and prose: Curio Class revision 018ace9b, CC BY 4.0 content and MIT code under the repository licences. All seven daily transfers, rates and thresholds are illustrative model choices. `fix-model-parity.json`: 27 habitat combinations times 520 weeks, zero population/oxygen drift, largest conservation error 5.60e-11 units.

Source pages were checked 2026-11-06. They are references only; no third-party text, figures or datasets were bundled. Manual and tool.draft.json record the same source names and reuse terms.

- Photosynthesis and body material: [OpenStax 8.1](https://openstax.org/books/biology-2e/pages/8-1-overview-of-photosynthesis) and [31.1](https://openstax.org/books/biology-2e/pages/31-1-nutritional-requirements-of-plants), CC BY-NC-SA 4.0 as confirmed in its current Preface; independently checked against [NOAA Ocean Exploration](https://origin.oceanexplorer.noaa.gov/ocean-fact/photochemo/), public-domain federal text. NOAA independently verifies sunlight, carbon dioxide and water; OpenStax 31.1 supplies the small mineral share. These are original plain explanations, not copied passages.
- Decay, blooms, shade and oxygen: [USGS Dissolved Oxygen and Water](https://www.usgs.gov/water-science-school/science/dissolved-oxygen-and-water), public-domain federal text, and [EPA Nutrient Pollution](https://www.epa.gov/nutrientpollution/effects-environment), federal reference with document-specific third-party exceptions; no media reused.
- Winterkill: [Minnesota DNR](https://www.dnr.state.mn.us/areas/fisheries/waterville/winterkill.html), copyright Minnesota DNR, reference only; corroborated by USGS decay/oxygen guidance. The page initially returned 403, then loaded successfully. The 3 and 2 mg/L thresholds remain model settings, not universal tolerances.
- Food-web cascades and energy: [Carpenter, Kitchell and Hodgson 1985](https://doi.org/10.2307/1309989), copyright American Institute of Biological Sciences, and OpenStax Biology 2e 46.1-46.3, CC BY-NC-SA 4.0, reference only. Lindeman 1942 remains a copyrighted provenance citation; the percentages are recomputed model results, not copied data or universal energy rules.
- Inherited shade: [Endler 1980](https://doi.org/10.1111/j.1558-5646.1980.tb04790.x), copyright Society for the Study of Evolution, reference only; selection mechanism checked with OpenStax 19.3. Guppies are the source organism; this minnow model does not claim to reproduce their experiments.
- Heron hunting: [Cornell Lab](https://www.allaboutbirds.org/guide/great_blue_heron/lifehistory) and [Audubon](https://www.audubon.org/field-guide/bird/great-blue-heron), copyrighted references only. The feeding/shade numbers are this model's own results.
- Existing species art and other natural-history citations were retained. No new images, software or audio were downloaded.

## Lesson creep check
`fix-creep.json` has two matches for level, both sea-level oxygen references. No goal, score, level progression, quiz, finish screen, kit header, praise, badge or sticker was introduced. There are no em dashes in src.html or the fixed voice lines.

## Engine changes wanted
No shared engine change was needed. Existing handoff requests about art rekey dependencies and drive.py letter-key support remain unchanged. The fix uses the existing kit voice queue and local Web Audio.

## Audit
The single audit finished successfully in 968 seconds (16 minutes 8 seconds), within the 2400-second limit. It reported 266 mechanical leads. All 42 audit frames were inspected through `fix-audit-contacts/` and compared with the targeted full-size frames. All 33 held-click rows had no errors and kept focus through Enter twice. Five-click and quick-tap probes were clean; resize stress found no exceptions or controls left disabled.

Every lead group is accounted for:
- Canvas overlaps: the instrument's controls and readouts intentionally sit over #pond, as the Settled calls say. No control-to-control overlap was reported.
- Phone TIME/LENS parent labels at 0 px: deliberately hidden; their rotary buttons have explicit accessible names and visible value text.
- Phone tray choices outside its scroll window: the specified scrolling specimen row; controls remain keyboard-reachable.
- Phone recorder choices outside #legend: confirmed and fixed. Seven 44 px keys now fit two rows with no horizontal overflow. `post-audit-phone-life.json`, `post-audit-phone-matter.json`, `post-audit-phone-energy.json` and `phone-shade-key.json` prove the bounds; `fix-last-proof/phone-shade-key.png` shows the optional shade line enabled.
- Ledger keep-region coverage: settled hit-test noise from noninteractive readouts over a canvas. The full-size frames show them plainly.
- Run/Speed/Tray hidden under Manual or Saved drawer: the intended modal/inert background, already settled.
- Hint out of view after interaction: the one-time hint has been dismissed, as intended.
- Welcome not heard/late: the Curiosity has a first-touch hint and factual event voice, not a lesson welcome. The accepted Add/Food suppression is separately verified. No welcome, goal, score or finish was added.

After the audit, its recorder-key lead and the manually confirmed heat-attribution/label lead received the scoped checks above, plus the two outside-tracker wait paths. No second full audit or lens pass was run. The final offline bundle is 744 KB, with clean scoped console logs and zero tool network requests. `fix-final-validation.json` records source/bundle hashes, the audited input hash, model parity, voice equality and closed ports. The full audit predates these scoped corrections; the report does not claim a second mechanical audit on them.

## Frames and verification
Frames for the final scoped corrections are in fix-post-audit, fix-last-proof and fix-last-energy. Earlier before/after evidence is retained, including unsuccessful harness fixtures. A mistaken selector in one Manual fixture and a screenshot-result filename collision were corrected and rerun; they were harness errors, not tool exceptions. The original painted art is unchanged. Reference frames of Beat Lab, Elements Inspector, Span and Spire and Pocket Universe were opened; their lesson-shaped elements were not copied.

## Left open
- Gravel-ranger recordings are not bundled; browser speech is the existing fallback.
- The historical claim that Some feeding keeps the school through ten winters is contradicted by the actual model. Per Settled calls, the fix reports winterkills instead of altering its flows.
- Four-times CPU performance was measured on this desktop, not on school Chromebook hardware.
- No questions were asked in this unattended run. Where there was a choice, the specified alternatives were used: retain the model; label Save only; use separate algae traces and an optional shade trace; use the settled factual event voice.
