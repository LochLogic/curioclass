# Trade Island build handoff

## Structure

src.html derives from the kit starter. It has responsive scene and notebook styles, the pure island and policy models, then persistent UI controls and Curio.voice integration. There is no family engine for these models. The offline artifact is trade-island.html; tool.draft.json stays stage built for cold review. Assembly fragments, number checks, frame scripts and evidence live in _scratch/trade-island. Future edits can be made directly in readable src.html.

## Model details

Wren maximizes exact baskets before comparing whole baskets with 50; ties choose fewer fishers. Pell's consumption only includes an accepted trade it can still cover. Worker changes never block on the boat. Season state is separate. Both-better speech is queued after Wren's reply, then the first prediction reveal.

Policy uses analytic market-clearing solutions for the allowed lever domain. Do not round before surplus, earnings, reef or factory-choice calculations. Factory owners remain Pell residents. A currency swing suppresses both Growth totals. Pins capture their value and active policies at pin time; Save rechecks structure. Passing a structure check does not establish the truth of the argument.

## Open questions and build decisions

- The sole spec open question requests sensitivity review of the nine people and invented cultures. Keep the islands fictional; make the varied people art, mark every people asset, and leave the independent review with evidence for the cold reviewer.
- The spec says 21 images but enumerates 22. Made all 22, including nine people. The explicit user and CODEX-BUILD art instruction overrides BUILD's older Do not draw art sentence and older Gemini-only wording. Credit OpenAI gpt-image.
- STANDARDS outranks the spec. Retained no focus on load; a prediction moves focus to the worker slider using preventScroll. The spec requests load focus while BUILD's wave lesson prohibits it.
- The spec says doing nothing leaves bars on their outlines, but specifies 50 Pell fishers and best-alone outlines at 60. Used the exact specified default: 100 baskets now against a 120-basket outline. Wren starts on its outline.
- The default's parenthesized 300 fish and 100 baskets only applies to Seasons 1 and 2. Storm and Motor boats use their actual production rates at the specified 50-fisher default.
- Scene tokens round to the nearest five workers, explicitly labeled; all numeric results use the exact slider count. This resolves single-worker increments with five-worker figures.
- The specified desktop table height cannot contain ten separate 44px pin rows plus 64px portraits. Used two island columns, six Pell rows and four Wren rows. Compact sizes page by island and combine each island's five card metrics in a selector and Pin button, keeping the 44px targets.
- Compact Policy has a Real case page with Back to levers, preserving the historical card when the entire desk cannot fit beside it. At 1000px the strip, all cards and both group columns remain visible. Compact Case places the structure-check explanation in the right panel so five evidence pins and the privacy statement fit beside Save.
- The user says stop when codex-report.md is written, so the working report lives in Scratch until the final write. This overrides the early-report-file instruction without sacrificing ongoing records.
- Voice metadata is wise-mentor. The no-recording instruction means browser fallback; the exact bank timbre is not guaranteed.
- The spec cites chapters 19 and 20 of OpenStax Principles of Economics 3e. Those chapter numbers belong to Microeconomics 3e. Verified and linked the same topics in Economics 3e chapters 33 and 34; the spec remains untouched.
- On a 375px phone, Policy puts levers before the evidence ledger to keep the main controls visible. The compact two-column lever desk keeps all six Pell group pins in view at 375x812; its Real case button opens the historical comparison. Phone Case puts its two return controls before the sheet. Cost inputs share a row on compact and phone layouts; the prediction card folds away while Cost is open and returns with its state intact. Longer student writing can scroll vertically. Landscape compact mode retains the desk and ledger side by side.

## Sensitivity

Nine people images show varied adults with practical clothing and tools. Neither skin tone nor gender determines economic success. No real cultural costume, religion or Indigenous identity is asserted. The left stone town and right timber town are model settings, not cultural rankings. Basic and Strong labor rules are fictional; the Cambodia card describes a historical agreement without mapping Wren to Cambodia. Inspect people for anatomy, stereotypes and equal agency; the contact sheet is _scratch/trade-island/art-sheet.png. A fresh review passed all nine people. Its suggestion is implemented beside historical cards: Historical comparison. Pell and Wren are fictional. Details are in _scratch/trade-island/sensitivity-review.md.

## Engine changes wanted

None. No shared files changed.

## Build verification

The single full audit completed, with 27 leads dispositioned in codex-report.md. Arithmetic has 294 pure checks plus 54 integrated UI assertions. Focused audit repairs cover label/footer bounds, phone controls, accessible writing, held-click result speech and real dragging. The full audit was not repeated. Evidence and frame lists stay in Scratch. Sound recovery uses the current Cost page and only marks the Storm explanation heard after an actual spoken event.

## Next

Read codex-report.md for the completed build checks and remaining limits. No polish round, git commit or deployment belongs to this run.

## Cold review changes, 2026-11-07

Cold play preceded reading this handoff, the build report, notes and source. Review evidence uses `review-*`, `cold-*`,
`find-frames/` and `post-frames/` in Scratch, leaving build evidence intact. No shared file or git history was changed.

Case now requires explicit Pell and Wren references and a pinned group/measure topic from each. This closes the unrelated
fifteen-word-list pass while preserving the stated structure-only check, both stances and the original pin gates. It does
not judge causation or the truth of the argument. The Save button itself shows success/storage failure at compact sizes.

`clearResults()` stops invalid result speech on deal, Cost and writing edits, while preserving Read. Factory changes drop
queued stale events. `allLines()` enumerates the variable Wren/Cost outcomes for the 792-line production inventory;
it is evaluated for recording/checking, not during normal play. Browser fallback remains; no clips were recorded.

The winning banner now shows each island's basket increase above best alone. Desktop bar numbers are larger. Worker
figures are spaced in perspective and the harbor retains its aspect ratio. The compact banner/sign geometry is checked
separately. All original art is retained except the redrawn storm overlay. Its full prompt is in `art/prompts.json`,
raw in `art/raw/storm.png`, generated with built-in imagegen, then processed by `scripts/art.py --rekey storm`. The
previous raw is preserved in `_scratch/trade-island/storm-before.png`. All nine people assets remain people:true.

The Ricardo source link now opens chapter 7 using Econlib's preface-offset query. Notes link the USTR quota facts and
Reuters exporter-share reporting. The washer card now explicitly labels the consumer cost per job as annual.

Independent review recomputation reproduces 597/0/1,931 winning trade combinations and all 72 policy settings to 1e-8.
See `codex-review.md` for the final single-audit disposition and remaining limits. No new modes or topics were added.

The review audit completed once in 36.9 minutes. Its real empty-Case feedback clipping is repaired by showing the
evidence-reference prompts only after meaningful writing and pins exist. Focused frames confirm the full seven-item
empty-case list at 680x425. Compact Islands now keeps the five-workers-per-token key in view. An uncovered deal stops
an in-flight cargo crossing immediately. Growth's accessible description warns about exchange rates only when they
actually differ from the baseline. All 27 final adversarial assertions pass; all 72 policy scenarios remain in parity.
The nine final repair frames live in `audit-fix-frames/`; the single audit is `review-audit/audit.md`. No second audit ran.
