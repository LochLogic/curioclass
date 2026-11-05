# Design for a Friend handoff

Build only, 2026-10-31. No commits, shared kit edits, deployment, or polish round. All work is in this tool and `_scratch/design-for-a-friend/`.

## Structure

`src.html` starts from the kit starter. CSS lays out actual pixel-sized controls, rather than scaling a fixed canvas. Content tables FRIENDS, FEATURES, NEEDS, QUESTIONS, STEPS, and L precede state and behavior. `evaluate(who, list)` is the pure five-step task rule. Interview progress is independent for each friend; the shared app has its own four slots. Nothing is persisted except the kit's Motion setting.

Ask stores the exact quotes with each note. Follow-ups extend the original note. Need and wish notes share the same markup and color; blue fact cards differ. Polite yes appears only after testing the corresponding wish feature. A feature counts as Used if it meets a need in this task. All five steps run even after a snag.

The drive uses an incrementing cancellation token and 800 ms per step, with Lou, Ana, and Kofi sequentially in the shared mode. Every slot, shelf card, friend, tab, and mode stays live. `stopDrive()` invalidates the token before the pending timer resumes. Resizing changes only layout, leaving the model and timing intact.

Question, shelf, friend, tab, and slot button nodes stay stable while their contents update. Questions and placed shelf cards use aria-disabled with guards so focus stays on the control just used. Feature placement supports tap then slot, Enter then Enter, and a real pointer drag with an integer-coordinate jitter test. Focus moves with preventScroll only when opening or closing a board or leaving an introductory friend card.

At short heights the test phone rotates into a landscape prototype so its three live slots fit with the five-step path. Shared designs use a two-by-two slot grid in compact views. At 375 pixels the slots come before the shelf. The quote board is an overlay with Escape, Back, and contained Tab focus.

Compact shared boards expose one full-size Open notes button per interviewed friend. This opens all collected notes and their original quotes without cutting a small set of note buttons halfway off. Desktop boards retain their side-by-side notes. The dialog uses the work area's measured bounds on opening and resizing. The yes/no reflection stays beside the answer even when question four also triggers the time-up hint. The shared mode remembers its last Design/Test view as well as its slots and results.

## Voice

Curio.voice owns speech, Read, and the log. Hints change immediately in tool code; Read returns that exact text. How lines use V.heard through the kit's once-only mechanism. Event lines are the six friend result strings, polite, all-done, and all-snag. Result validity closes over the drive token. Ask stops a spoken instruction when its question controls cease to fit, and design edits stop obsolete event speech. No recordings were made; voice/lines.json contains the sixteen fixed strings for wise-mentor / Gacrux, with browser fallback in this build.

## Art and provenance

Seven new built-in imagegen images were made: garden-backdrop and six plant cutouts. Full prompts are in art/prompts.json, originals in art/raw, and final WebP images were processed only with art.py --rekey. The plant kit was inspected on warm paper at final size, including kohlrabi shape and magenta-key edges. The garden was inspected at full size and in the scene.

The three existing portrait WebP files were retained unchanged. Their original prompts, source, reference links, and pending review records were restored from HEAD and preserved. No new people, faces, or body parts were generated. Their previous pending owner review status remains pending. If a portrait is absent, the code's faceless silhouette works with its art token.

## Open questions resolved for this build

- Keep Lou, Ana, and Kofi as the three users, as the spec leans. Existing portraits are used; their pending owner review is not silently promoted to approved.
- Keep wise-mentor (Gacrux), as the spec leans, so spot-the-ai retains curious-librarian. The fixed voice manifest records this choice.

## Numbers and evidence

`_scratch/design-for-a-friend/setup.py` independently checks all 2,048 subsets, exact four- and five-card solution counts, empty-design snags, and ten WCAG contrast pairs. `numbers.json` records results. `checks.js` compares 6,144 browser evaluations and tests real drives, quote budgets, duplicate refusal, cancellation, restart, and mode persistence. Functional evidence, held-input voice logs, real drag, keyboard, grayscale, reduced-motion, and size frames are in Scratch. The bar tools were copied and bundled in Scratch to obey the write boundary.

`resize-results.json` checks actual viewport changes during both individual and shared drives; each finishes without exceptions or a stuck running state. `candidate-final-frames` covers the completed compact board/dialog, four-question reflection, full three-feature phone, shared plant preview, and restored shared result. Early geometry probes used a nonexistent test selector; that test helper was corrected before final checks. It was not an application exception.

The mechanical audit ran once, finished within its 40-minute limit, and reported 47 leads. `_scratch/design-for-a-friend/audit-dispositions.md` answers each one: 23 rotated-card rectangle false positives, eight intentional dialog-over-background overlaps, nine intentionally stale introduction cancellations, and seven corrected phone/quote/rapid-tap leads. Its Motion, resize, and settled keyboard checks were clean. The raw report is `audit/audit.md`; it describes the pre-fix bundle. Only affected views and controls were checked afterward, including hosted 375 geometry and 0.7-second held double-taps. The full audit was not repeated.

An idle repeat tap on the current friend or tab leaves valid narration playing. During a running test the same tap still takes the cancellation path. Compact preview extras become a small row of widgets, preserving their effect without intruding into feature slots. All three slots stay at least 44 pixels high. Final frames are collected in `final-frames`; final verification and static asset checks are reproducible with `verify-final.py` and `static-check.py`.

## Engine changes wanted

None. The shared kit is unchanged.

## Cold review repairs, 2026-11-03

The cold review played all friends and both modes before reading the build report.
The interview, feature rules, slot budgets, and existing rich garden scene are retained.

Loaded portrait images now hide their fallback SVG, which previously showed an extra
head and shoulder behind Kofi. All six plants were rekeyed with holes/despill; kohlrabi
was redrawn with built-in OpenAI imagegen. The full replacement prompt is in
art/prompts.json; raw art is art/raw/plant-kohlrabi.png. The existing people review
metadata is preserved. A fresh contact sheet is _scratch/design-for-a-friend/review-art.png.

updateHint prioritizes a selected feature in either view and explains how to free a
full slot. Shared results name Back to design. displayedStep keeps a restored result
at the final step. Opening evidence cancels a running drive and obsolete narration.
The existing mock phone now shows a missed Save, a Delete tap, and a missed reminder.
The shared result table adds the current friend's portrait, step, and quote as a
caption; individual table cells retain text and accessible snag descriptions.
H centralizes Read hints. allLines and voice/lines.json now contain all 58 narration
and hint variants, including each feature name and each friend's result instruction.

Independent checks are review-numbers.json and review-functional.json in Scratch.
The latter compares all 6,144 friend/subset combinations and exercises the requested
designs, question budgets, cancellation, restart, saved views, and placement hints.
review-frames holds the affected laptop/preview, keyboard, grayscale, and calm views.
review-recheck-frames supersedes the affected preview and null-state checks. Its
functional run passed all 22 assertions with no console errors. Held input starts
ask/open-q/closed-q/design once each and lou-done/lou-snag five times each; Read works
with Sound off. Whole-pixel jittered drag places a feature, and keyboard placement
retains visible focus on slot 1. Motion off took 4.074 seconds for five steps.
The final review audit and any narrow repairs are recorded in codex-review.md.

The review audit finished once within its 40-minute deadline, with 32 leads and
no application errors, resize exceptions, or stuck controls. Dispositions are
_scratch/design-for-a-friend/review-audit-dispositions.md. Its 22 tilted-card
rectangle leads were visually false positives, and nine introductory welcome
warnings reflect the spec's stale-on-friend-entry rule.

The rapid initial Ask lead was real: showing Reset shifted the tabs, so a second
same-position tap hit Test. Reset now retains an invisible footprint before a
friend is chosen, with a stable minimum width. Before/after rectangles are equal
at 1366 and 680; real fixed-point double taps keep Ask's one uncut instruction.
Direct Test entry now speaks its existing Start hint once with state validity.

A held click behind the quote sheet also changed the interview and left stale
notes. boardBackground makes the panel, friend/tab strip, and other stage children
inert while the sheet is open. The kit header controls stay live. Back/Escape
restore work and focus; quote selection and Read with Sound off still work.
The quote audit state now selects an actual note, and direct Test has its own state.

Only these final affected paths were re-shot at 1366, 680, and hosted 375 after
the audit. review-final-frames and the modal/Ask JSON probes hold the evidence.
The full audit was not repeated. Final bundle is 1,208,534 bytes (1180.2 KiB).

## Next

The separate cold review can inspect the compact layouts and voice evidence, and the owner can review the retained portraits. This build does not begin that review or a polish round.
