# Game Day Fuel: build handoff

## Cold Codex review, 2026-10-31
The reviewer played all four athletes before reading this file or the build report. Review changes are in the tool only; evidence is under `_scratch/game-day-fuel/review-*`.

Delete now retains the meal cell so repeated removal and arrow navigation keep working. Grid rows now have explicit accessible row containers. Keyboard navigation scrolls the board itself instead of moving the whole page. The teacher notes describe the actual Tab order and include a fictional-athlete discussion boundary.

The final whistle keeps a larger chart on school laptops. Compact gear cards retain the illustrations; a concise result route shows wake, start and finish values. The solid replay and dashed forecast are named on screen. Editing a finished plan explicitly labels the outcome Forecast until the next replay. The below-15 crossing time stays in the result heading even when compact layouts hide explanatory paragraphs.

Four food illustrations were redrawn with OpenAI gpt-image and processed with the free `art.py --rekey` path: whole-wheat toast, turkey sandwich, PB and J, and plain cheese pizza. Brown bread, the cut sandwich and cheese-only topping now match their records. All other art and the equipment-room setting stay intact. Native titles expose each shelf serving.

Independent checks re-sum all 30 rows against the spec and reproduce all four fuel results, plus Ana without the pre-game snack. The spec's composite serving recipes and gram amounts remain unspecified; individual FDC matches cannot honestly be inferred from those names. Values remain the explicit spec dataset, with that provenance limitation retained rather than invented IDs.

No kit changes, recordings, commits or feature additions. The review report records the single final audit's disposition.

The review audit completed with 52 leads and 62 frames. Its real voice lead exposed planning-only howFlag being queued during a Game-day edit. It now queues only in Plan when no flag is selected. The scoped re-check also confirmed old result and flag speech surviving an edit after its numbers changed; edits and timing moves now hush those contextual lines, and changing flags replaces their old narration. Fixed lines and the voice bank are unchanged. Post-audit evidence is in post-voice-fix.log and the two voice-invalidation JSON files in Scratch. The added flag-after-edit audit state documents that regression path for the next review; only its affected path was rechecked here, with no second audit.

## Layout and code
`src.html` starts from the kit starter and uses `kit:curio` and `kit:theme-912`. It contains the responsive equipment-room header, week board, shelf, labels, flags, SVG timeline, replay, dialogs and event handlers. `foods.json` bundles through `json:foods`; it keeps the 15 Label Detective nutrient keys and adds MyPlate groups and slotKind. The 13 reused food records and paintings are copied exactly. The family has no separate engine or family document.

The 17 new rows use `null` for nutrients the spec does not supply. Unknown micronutrients are never presented as zero. The seven nutrients actually taught have the supplied values. The out-of-fuel voice omits "in the second half" because a cleared plan can cross the threshold before play; the result card gives the first model crossing time, including the pre-game hours.

`simulate()` produces minute samples to 10 pm, including post-game meals. The replay uses those samples only through the final whistle. `valueAt()` interpolates the live clock. Per-meal carbohydrate contributions are cached before the integration loop. Edits rebuild the model while preserving clock and running state. During foods contribute over play regardless of their fixed flag time.

`flags()` returns all ten named checks and affected days. The pre-game check includes both endpoints. Recovery requires one qualifying meal, rather than adding several meals. Selected-day values use the sibling's FDA rounding and DV references. Energy bars, flag calculations and the model use exact sums.

Plans are validated when loaded. Unknown food IDs are rejected; excess servings are capped, times clamp to legal windows, and removed slot foods are retained in a Moved note. Athlete changes load that athlete's saved plan or its starter. Copy day matches slot names and preserves unmatched food in Moved notes.

Small previews keep stage and panel side by side. The week board scrolls vertically and horizontally inside its frame, with pinned row labels, day headers and energy summaries. Small-screen Week tools opens the existing actions in a dialog. Game day adds an accessible food-removal strip; meal editing stays live during replay. The main board is intentionally not scaled down into tiny targets.

Meal labels use two rows, avoid collisions and connect back to their true time with stems. Moving a nudged label retains its initial pointer offset so it does not jump. At compact sizes the clock moves above the chart and the Meal time slider replaces the removal strip while Move meal is active. Leaving Game day clears Move meal state.

## Open questions resolved
1. Use Game Day Fuel as written, retaining Nutrition and fitness planning as the topic line.
2. Keep the 2020–2025 calorie and food pattern tables explicitly identified by the spec. Switching editions would change the lesson's supplied targets and checks, so this build does not silently replace them.
3. Keep all athletes fictional and omit a student-specific week. Store no student information.

## Art
Preserved all 17 existing new-food paintings. Copied the 13 Label Detective paintings unchanged. Generated four missing sport-gear sets and one equipment-room backdrop using the built-in image tool. Prompts, provenance and dimensions are in `art/prompts.json`; raw generated PNGs are in `art/raw/`. Keyed and sized only with `scripts/art.py game-day-fuel --rekey <name>`. No people are present. No recordings were made; the kit falls back to browser speech using the easy-coach line style.

## Engine changes wanted
None.

## Build audit
The single full audit completed in 1,797.2 seconds and produced 71 leads. Its 57 size/state frames were reviewed in contact sheets, with the real overlap cases opened at native resolution. Motion off, resize stress, console checks, focus and Enter paths completed without errors or stuck controls.

The two preview-axis collisions and three compact morning-meal collisions were fixed and re-shot at the affected sizes. Compact results now occupy the clock row, and meal text has an explicit line height. Repeated taps on an active mode, selected athlete or unchanged Typical week no longer cut the welcome. Four representative quick-tap voice checks now finish without a cut.

Grid and diagnostic-list scroll leads are intentional under the specified compact layout. First-action welcome skips after Clear or food removal follow the standing first-tap rule: the action's own how line wins, and the old Typical week welcome is stale. Restart at wake is intentionally idempotent. Food controls outside the shelf viewport work after scrolling or filtering; a real Chocolate milk click after the Drinks filter was verified.

Final targeted checks also cover the pre-game below-15 crossing time, consuming Moved items when placed, Read returning to Plan context, and empty-filter recovery instructions. `audit-final-diff.txt` in Scratch records changes after the full audit snapshot. The whole audit was not repeated. The selected athlete's idle light, like the live-clock light, explicitly stops with Motion off.

## Review priorities and limitations
- Independent FDC-ID verification of the 17 new typical-serving rows remains open. Composite foods have no precise recipe or gram amounts in the spec, so an exact USDA match cannot be inferred honestly. Values were retained from the supplied table; no IDs were fabricated.
- Full-size planning shows the upper meal rows at once and scrolls for later meals. Keeping every food-removal control at least 44 px takes more vertical space than the complete week fits in a preview. The energy summaries remain pinned.
- The Moved note lists foods for manual placement from the shelf. It is not counted until placed.
- Built-in narration uses browser speech until the owner records the provided fixed lines. The report records actual queue tests separately from audio quality.
- Build only. No git commits and no separate polish round.
