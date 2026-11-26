# Biome Atlas: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: biome-atlas

#### Built

Build only, completed 2026-10-30. No commits, branch changes or polish round.
Read, Key and Change are implemented in the offline biome-atlas.html bundle.
Includes 13 stations, branching answers, comparison checking, biome reveals, saved progress and painted succession.
The kit supplies the frame, Motion, Sound, Read, tones and Curio.voice.
Teacher notes, lesson plan, preview, prompts, voice lines, audit states and handoff are included.
tool.draft.json has stage built and status beta.
Browser narration is the intentional fallback; no audio was recorded.
Open questions follow the spec's leaning: one deliberate miss, HS-LS2-6 only, approximate succession times.

#### Numbers check

PASS: independent Python recomputed every monthly array, all 13 annual T/P pairs, summer shares, dry lines and base results.
PASS: 12 matches and Dodge City's sole miss, using the spec's real-biome assignments.
PASS: all 11 listed what-if checks, independently and through the browser key.
PASS: all ten full recovery runs measured 7.977 to 8.081 seconds.
PASS: contrast is 7.37:1 brand/panel, 6.98:1 brand/section, 7.73:1 ink/brand; lowest pin-letter contrast is 5.17:1.
Numeric discrepancy retained: 8 years / 200 steps = 0.04 years.
The 0.3-year grassland milestone falls between manual positions 0.28 and 0.32; Play crosses it continuously.
FAIL, source verification: an independent WWF polygon point lookup was not completed. Supplied biome assignments were retained.
Reproduction script and numerical JSON: S:/CurioClass-codex/_scratch/biome-atlas/numbers_check.py and numbers-rechecked.json.

#### Feel check

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

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

All four mode/focus frames at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812.
All 65 audit PNGs were inspected in contact sheets; compact and phone audit sheets retained native frame sizes.
Also inspected first-playable frames, timing frames, functional frame, grayscale, Motion off, all-station labels and keyboard.
Inspected real scrub, running rain change, fire restart, climate extrema, repeated voice-result and blocked-storage frames.
Final follow-ups: three map sizes, phone Key/Change/Reveal, both ground fades, pin focus, persistence, layer codes and clearing zero.
All frames and recipes remain in S:/CurioClass-codex/_scratch/biome-atlas/.
Owned Chrome processes and servers were closed. host.html is removed.

#### Art made

20 new succession assets, with three redraws: 23 generated takes. The ten original scene cards are retained.
All 30 painted assets ship inline. Art totals 1,358,692 bytes.
Final bundle: 1,975,350 bytes, below 2,000,000 bytes.
Raw selected art and rejected first takes are preserved in art/raw.
Every new image was generated with the image tool and processed only with art.py --rekey.
No people, external image downloads or placeholder assets remain.

#### Art still to paint

None.

#### Engine changes wanted

No family or kit engine change.
Shared audit tooling: scripts/audit_tool.py, MODES_JS should additionally discover main .seg[aria-label="Mode"] button.
Audit.steps should reject a missing/non-array drag result instead of silently replacing it with an empty list.
The exact reasons and workarounds are in handoff.md. Shared files were not edited.

#### Left open

Independent WWF ecoregion point lookup remains required for source verification.
The spec's 200-step rule prevents selecting the 0.3-year milestone exactly; this is documented rather than silently changed.
The completed audit is a pre-follow-up snapshot with the scope limits above, not a claim of zero mechanical leads.
Narration recordings were intentionally not made in Build. The bank direction is preserved and browser speech works.
Tree layers look softer at the largest size because the full thirty-image set stays inside the bundle budget.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: biome-atlas

#### Played

Cold Grade 12 solo play before builder notes: Read, wrong and correct Key paths, Reveal, Clearing, Play, rewind and a rain shift. Then read through projected examples, including Dodge City's miss. The large climograph and painted reveals are strong; recovery originally felt softer and flatter.

#### Findings fixed

- Blocker, general, Key: Real biomes disclosed untried answers. Each real pin now stays unknown until that station's Reveal.
- Should fix, general, Key: the dry-month chart outlined the answer months. It now outlines the whole year for that question.
- Should fix, general, Key: incorrect Dodge City comparisons could blame the model. Wrong paths now get a numerical-check explanation and their own spoken event.
- Should fix, general, Craft: comparison feedback shrank into a clipped strip. Fixed flex sizing, compact Key station details and short-screen spacing. Open phone feedback now fits in view.
- Should fix, general, Craft: answer buttons and map pins rebuilt after actions. Reuse answer buttons; preserve pin elements when map dimensions stay unchanged. Focus remains usable.
- Should fix, general, Voice: old station speech and stale welcomes could outlive their state. Station changes hush; welcome eligibility and fallback validity now match the current state.
- Should fix, general, Voice: quick repeated mode or pristine Reset taps cut welcomes. Redundant taps now leave the current line playing.
- Should fix, general, Craft: checked feedback followed mode switches. It now belongs to Key only.
- Should fix, general, Craft: all-station chart labels overlapped, and shifted labels/accessibility values used base climate. Labels now avoid collisions and follow the current dot.
- Should fix, general, Graphics: 480 px cutouts blurred across the landscape. Re-exported all twenty at 1400 px, quality 72; redrew the sparse tropical canopy as a closed, layered forest.
- Polish, general, Play: recovery lacked an earned visible result. Added the next approximate milestone, a progress edge and a specific same-climate completion, retaining the required eight-second run.
- Polish, general, Craft: captions covered low plants and early year labels collided. Reserve a measured caption band and space tick labels in pixels.
- Polish, general, Voice: first Place could speak an obsolete welcome. It now gives its own next-action instruction; Check and layer changes also give sound feedback.

#### Findings left

- Should fix, spec/source: the WWF point query puts Niamey in West Sudanian savanna, rather than the named ecoregion in the spec. Kredarica's regional forest polygon does not verify local alpine vegetation. Retained the supplied categories because changing the spec is forbidden; notes disclose the limits.
- Polish, general: Clear my progress remains in the scrollable footer at some sizes. The equivalent Reset stays visible; this is not a hidden answer choice.
- Polish, general: narration uses browser speech. Recording audio is outside this brief.

#### Flattest moment left

Thirteen key traversals can still become routine. Kept the specified branching structure and Dodge City's deliberate surprise; no extra challenge or topic was added.

#### Graphics

Checked all thirty paintings in contact sheets and mode/stage frames. One canopy redraw; twenty sharper exports. No people, missing assets or placeholders.
Built-in imagegen prompt and selected raw: art/prompts.json and art/raw/ba-k-tropical-canopy.png. Finished asset: art/ba-k-tropical-canopy.webp.
Final art: 5,758,650 bytes. Bundle: 7,848,991 bytes, about 7,849 decimal KB (7,665 KiB). The required Size line explains the full-screen art in notes.md.
Opened the existing Beat Lab and Snowy Mail Route bundles as finish references; preserved the atlas's richer landscape cards and instrument layout.

#### Audit

Ran audit_tool.py once, last, on Chrome 9941 and host 8745, with a 2400-second process-tree limit. It finished: 57 leads, 89 PNGs inspected. Motion off, repeat clicks, console checks and resize stress had no errors or stuck controls.
Confirmed and fixed: 9 chart-label rows, 1 phone-feedback row and 4 quick-tap speech rows. Also repaired the walk's rebuilt pin elements and a manually confirmed stale Key welcome.
Answered the other groups: 14 footer/short-choice rows concern the secondary reset duplicate; 15 SVG/path rows concern circular bounding-box corners; 14 missing welcomes correctly yield to the first action's own instruction.
Focused rechecks only: zero label overlaps at 680, 800, 1000, 1280 and 1366; all thirteen pin centers hittable and elements stable at 1000, 1280 and 1366; phone feedback ends at 779.7 of 812 px; all four quick-tap cases preserve speech. Completed-Key re-entry speaks Reveal. No console errors.
The audit misses panel modes in automatic mode discovery. Explicit states covered Key and Change; separate held-input checks covered their controls and narration. No second full audit was run.
Evidence and grouped responses: _scratch/biome-atlas/audit-responses.md, review-audit/, post-audit-frames/ and post-*.json.

| Voice check | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| placeIt, five station actions | how | 1 | 1 |
| first Place instruction | how | 1 | 1 |
| match | event | 5 | 5 |
| miss | event | 5 | 5 |
| shifted, nine boundary changes | event | 9 | 9 |

Full voice-line parity passed. Keyboard-only play reached Reveal with tally 1 of 1; grayscale inspected. Calm recovery measured 7.90 seconds. Real Years input pauses Play; climate input leaves Play running.

#### Left open

Independent Python matched every monthly spec input, all thirteen base outcomes, all eleven what-if checks and Dodge City's 546.0 mm dry line. The 12-of-13 tally is verified against the supplied assignments, not thirteen independently observed local vegetation records.
Regional source evidence: _scratch/biome-atlas/review-ecoregions.json, queried from [UNEP-WCMC's WWF layer](https://data-gis.unep-wcmc.org/server/rest/services/Hosted/Terrestrial_Ecoregions_of_the_World/FeatureServer/0). The spec/source discrepancies above need a spec decision.
The spec's 200 divisions put the approximate 0.3-year milestone between 0.28 and 0.32; Play crosses it. Kept that rule.
Writes stayed in tools/biome-atlas/ and its Scratch folder. No commits, shared engine edits or new review round. Owned Chrome processes and servers are closed; host.html is absent.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Biome Atlas handoff

Built by another chat, then cold-reviewed on 2026-11-03. No commits.

#### Cold review, 2026-11-03

One review pass, no commits. Read codex-review.md for the final evidence and audit limits.
The old builder report describes the pre-review build. Preserve the rich landscape card set.
Cold review redrew ba-k-tropical-canopy using the built-in imagegen tool and its full prompt in art/prompts.json.
All twenty cutouts were re-exported at 1400 px and quality 72 from their raw paintings to repair full-screen softness.
The generated canopy raw file is art/raw/ba-k-tropical-canopy.png; no paid art.py generation was used.
Comparison results no longer shrink to a clipped row; Key uses a compact station summary.
Map Real biomes waits for each station's Reveal. The dry-month question outlines the whole year instead of the answer months.
Wrong-answer misses use their own spoken event and explanation, including at Dodge City.
Answer buttons are reused between questions; station changes hush stale speech; check feedback stays inside Key.
Recovery shows a progress edge, the next approximate stage and a specific same-climate completion result.

The single review audit completed with 57 leads. Its unchanged report is in _scratch/biome-atlas/review-audit/audit.md.
Post-audit corrections separate all-station chart labels, fit opened feedback on phones, preserve pin nodes and avoid cutting speech on repeated mode/empty Reset taps.
Welcome eligibility is checked before queuing so a completed Key gets its current Reveal instruction.
Plants sit above a measured caption band; tick labels use pixel spacing. Active climate labels and accessible chart values follow the shifted dot.
Focused rechecks only followed these corrections. No second full audit or new review round was run.

Source evidence is in _scratch/biome-atlas/review-ecoregions.json and review-numbers.json.
The UNEP-WCMC WWF point query confirmed the broad category for most stations, but contradicts Niamey's named ecoregion.
Kredarica's polygon is Dinaric Mountains mixed forests, not an elevation-resolved alpine tundra observation.
The spec's assignments remain unchanged, as required when a repair would change the spec. Notes disclose the limitation.

#### Source map

src.html starts from the kit starter and uses kit:curio plus kit:theme-912.
Its sections are responsive styles, stable controls, climate calculations, a branching key, real-pixel SVG charts, succession stage data, layer rendering and event handlers.
stations.json preserves the spec's monthly inputs. world.json is the bundled land outline.
The hidden art bank holds the ten existing landscape cards. K holds the twenty new painted cutouts.
Curio.voice owns speech, Read, how-to deduplication and event logs.
window.__tool exposes state, calculations and interactions for review.

#### Tricky parts

All calculations retain precision until display rounding. Southern stations reorder months only for plotting.
Wrong answers take a real branch and are checked after completion.
Each station has one saved record, including its comparison correctness and Reveal status.
At zero climate offsets the recovery destination is the real biome. Nonzero offsets use the key.
The timeline uses the larger source/destination span, 200 slider divisions, and an eight-second run.
Layer updates use CSS transitions; Motion off removes transitions without changing timeline duration.

#### Open questions resolved

- Keep Dodge City as the sole intentional miss, following the spec's leaning.
- Teach only HS-LS2-6. Do not add HS-ESS2-4.
- Keep rounded succession timings, visibly labeled approximate.

#### Engine changes wanted

Shared audit tooling only: scripts/audit_tool.py, MODES_JS.
Extend its selector with main .seg[aria-label="Mode"] button, preserving the existing header selectors.
The spec places mode tabs in the panel; header-only discovery misses them and cannot launch mode-specific control walks.
Explicit audit states and held-input tests cover the panel modes in this build. No shared file was changed.

#### Review next

Cold review against spec.md and codex-report.md. Do not begin polish or deploy from this build.


#### Build verification and boundaries

The ten original, unprefixed biome cards are retained. Twenty ba-k cutouts were generated during this build.
Bare soil, burned ground and scarred soil were each redrawn once. Raw originals and rejected first takes remain in art/raw.
The cutout ground strips use opacity for the spec's half and fifth descriptions; plant multipliers control height.
Short landscape layouts keep the main controls visible. Climate space remains in Read; Key and Change can hide that secondary inset in the shortest previews.
In Change, __tool.keyResult reports the live climate key. state.keyResult preserves the student's original prediction.
All 13 base results and 11 what-if results matched independent Python calculations.
Measured playback was about eight seconds for all ten biome stories.
Detailed screenshots and test JSON are in S:/CurioClass-codex/_scratch/biome-atlas.

#### Source verification still open

The monthly station values and real-biome assignments come from spec.md.
An independent WWF ecoregion polygon point lookup was not completed: that dataset is not bundled in this worktree.
Do that source check in cold review. Do not treat the supplied ecoregion assignments as independently reverified here.
No network data was downloaded during Build.

#### Numeric and audit recipe notes

The 8-year grassland span divided into 200 steps gives 0.04-year increments.
The approximate 0.3-year milestone lies between manual positions 0.28 and 0.32; Play crosses it continuously.
The spec's 200-step rule was retained.
The audit-state drag field requires a function body with an explicit return.
The initial audit recipes omitted it, so its named min/max snapshots stayed at zero offsets.
Those recipes are corrected for the next run. Separate real-drag and extrema frames cover the slider behavior.

#### Additional audit helper change wanted

scripts/audit_tool.py, Audit.steps: require a drag result to be an array with at least two points.
Report an invalid drag recipe instead of silently converting an undefined result to an empty array.
No shared tooling was changed in this build.

#### Evidence files

build-evidence.json records final bundle bytes and hashes, independent result checks, timing and viewport geometry.
audit-leads.md answers all 82 reported audit leads individually.
The full mechanical audit and all screenshot recipes remain in the supplied Scratch folder.
Change-mode T and P readouts track the active offsets; Read and Key retain the published station normals.
No commits or polish round were started.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
