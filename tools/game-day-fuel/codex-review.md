# Codex review: game-day-fuel
## Played
Cold grade 10 student run before opening builder notes: first edit, diagnostic flag, notes, all four athletes and final whistles. Then replayed at 1x and checked projection and compact layouts. Strong equipment art and an engaging timing premise; final chart collapsed.
## Findings fixed
- Should fix, general, grid keyboard: Delete moved focus to an arrow-inert food chip; keep the cell focused after Delete. Board navigation now scrolls only its own region and has proper accessible rows.
- Should fix, family:food, final result: edits silently replaced a tested final whistle with an untested outcome. Revised plans now say Forecast until replayed.
- Should fix, general, result: compact layouts hid the below-15 crossing time. Keep it in the result heading.
- Should fix, family:food, art: cheese pizza had pepperoni and three whole-wheat bread assets looked white. Redrew pizza, toast, PB and J, turkey in the same soft illustration style.
- Should fix, general, phone shelf: its extra meal-edit row pushed food names below the panel. Rebalanced phone rows with targets and paintings retained.
- Should fix, general, voice: a Game-day edit queued a Plan-only instruction, and old result/flag speech survived changed values. Gate howFlag to its visible Plan context; hush stale contextual speech on edits, timing moves and flag changes. Before/after logs and frames confirm the repair.
- Polish, general, final whistle: the chart collapsed at the payoff. Reserve more chart space, show the plan's wake/start/finish route, and name forecast versus replay strokes.
- Polish, family:food, notes: correct the Tab guidance, expose serving tooltips, label the example dataset and add sensitive-discussion context.
## Findings left
- Should fix, family:food, source provenance: independent FDC IDs for the 17 new rows remain unresolved. The spec supplies no gram recipes for composite servings; inventing matching IDs or changing the supplied dataset would be unsound. See Left open.
## Flattest moment left
Routine weekly maintenance is still the flattest stretch. Different athlete schedules supply the spec's later twists; no new game mechanic was added. The improved final-whistle chart now lands clearly.
## Graphics
All 35 images checked on dark contact sheets and at display size; four redrawn, none missing, no people. Native prompts and provenance are in art/prompts.json; rekey only. Bundle 866.6 KiB (887,447 bytes), below 2 MB. Preserved gear, backdrop and other food art. Compared with both bar tools; review-comparison.png is in Scratch.
## Audit
One final audit completed in about 32 minutes, exit 0: 52 leads, 62 frames inspected in 16 contact sheets. Report: _scratch/game-day-fuel/review-audit/audit.md. No second audit.
- Fixed the real revised-forecast voice lead. Targeted checks also confirm obsolete result/flag speech now stops and no Plan howFlag is queued in Game day. Added the regression path to audit-states.json; that new state was checked directly after the audit.
- Grid-scroll leads: the specified seven-day board, with pinned labels and energy bars, intentionally scrolls. The short athlete and filter choices stay visible.
- Side-scroll leads: the diagnostic list is intentionally scrollable, with its summary before the list. The spec requires its top at 1366, not ten simultaneous flag buttons.
- Welcome skips on Clear/removal: their own instruction correctly wins; the Typical week welcome is stale. Sound and Read suppression follow the kit rules. No late welcome was added.
- Restart at wake: correctly idempotent. Foods 12-14 were outside the default shelf viewport; all three add immediately through real held clicks after Meals exposes them. Remaining off-screen shelf rows use the same working add handler.
- Rebuilt controls retain focus. Mode/slider layout shifts are intentional. Audit reports no small-target, overlap, clipped-text, console, stuck-disabled or infinite-animation defect. Repeat and quick-tap checks are clean.
Scoped checks cover all STANDARDS sizes, both modes, empty/full meals, fifth-food refusal, copy, save/load, real drag, live edits, Pause, grayscale and Motion off. Own native frames and affected post-audit frames were opened.
Independent sums reproduce every core spec value. 1x replays finish in 21.67 / 26.01 / 12.01 / 7.01 s; outcomes 39 / 35 / 26 / 27 percent. Ana without the pre-game snack finishes at 26 percent.
All 29 fixed lines match the bank. Read with Sound off and rapid scope changes checked. Browser fallback remains, with no recordings made.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| strong | event | 5 | 5 |
| again | how | 1 | 1 |

Accent contrast: 8.01:1 on panel, 7.59:1 on secondary background, button ink 8.02:1. Group text: 7.63 to 10.62:1. Status words and glyphs remain legible in grayscale.
## Left open
Exact FDC verification needs specified serving weights and recipes upstream; retained all 30 core rows exactly and disclosed the limitation. Kept the spec's explicitly dated 2020-2025 tables. No kit changes, external deployment or commits. Review evidence is in _scratch/game-day-fuel/review-*.
Process exception: the first two read-only inspection commands completed without explicit timeouts. Every later command used bounded execution. One combined timing probe exceeded drive.py's internal 60-second call limit; the single smaller retry split it into four successful athlete runs.
