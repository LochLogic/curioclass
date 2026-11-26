# Design for a Friend: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: design-for-a-friend

#### Built

Grade 5 interview, prototype, and task-test studio for Maple Street Garden. Three independent four-question interviews feed quote-backed boards. Eleven features fit three individual slots or four shared slots. Five-step tests reveal actual use, snags, and polite agreement. Both modes retain their progress.

Built from the kit starter with Curio.voice, Motion, Sound, Read, tones, and fitting. No family engine. No commits, deployment, shared-file edits, or polish round. All writes stayed in the tool and its Scratch folder. Chrome 9980, 9981, and 9982; host 8785. Servers and browsers owned by this build were closed.

#### Numbers check

PASS. Independently enumerated all 2,048 feature subsets in `setup.py`: no three-card solution, exactly one four-card solution (Read aloud, Big buttons far apart, English and Spanish switch, Reminder you set), eight five-card solutions. All empty-design snags and ten contrast pairs match the spec. Browser evaluation checked 6,144 friend/subset combinations. Shared success took 12.092 seconds; Motion-off individual test took 4.060 seconds. No spec-number corrections.

#### Feel check

Best moment: Lou finishes with the apparently helpful Video lessons untouched, and his yellow wish receives the gray Polite yes stamp. The student's own question and feature choices make the reveal specific. The later shared round changes the problem: four slots must meet six needs, so Read aloud and Big buttons earn their value for two people.

Two flat moments changed during build: the marker was too small and simply jumped between steps, so it now travels visibly above the path; compact prototype and evidence views hid the payoff, so live 44-pixel slots, landscape test phones, and a work-area quote dialog keep the design and evidence readable. The four-note board and retained shared-result view received targeted checks after the mechanical audit snapshot.

Played the interview, unsuccessful redesign, successful redesign, and shared solution. Compared `bar-comparison.png` against Snowy Mail Route and inspected Beat Lab. The garden, cutout plants, cork boards, layered phone, moving portrait, stamps, and result table match the finish bar without borrowing either tool's scene. This is a deliberate classroom design activity, with its depth in interviewing different users and reconciling needs.

#### Done when

1. PASS: Lou questions 1 and 2 create two notes; follow-up appears only after 2; four questions disable every card. Functional assertions and four-question frames.
2. PASS: Ana's Points and badges wish uses exactly the same yellow note class and styling as needs, until tested. Ana Ask frames and markup check.
3. PASS: Big text plus Big buttons completes Lou; Big text alone snags only step 4 with the exact Delete quote. Real drives and evaluator assertions.
4. PASS: Big text, Big buttons, Video lessons completes Lou; Video is Never used and the asked wish gets Polite yes. Real drive, result frame, note assertions.
5. PASS: Exact shared four-card set completes all 15 steps; Read aloud and Big buttons are named as helping more than one. All subsets checked and real 12-second drive.
6. PASS: Kofi shortcut plus reminder completes; chat plus reminder snags step 4. Functional drive and rule assertions.
7. PASS: Five held actions at two-second gaps start ask, open-q, closed-q, design exactly once. Repeated real drives start success and snag events twice each. `input-verification.json`.
8. PASS: All question choices and Questions left visible at 1366x768 and 680x425. Results retain checks, exclamation marks, words, and step numbers in grayscale. Size and grayscale frames inspected.
9. PASS: Ask centers the portrait/newest bubble; Design centers the phone; Test centers the traveling marker above its five steps. Compact and desktop focus frames inspected.
10. PASS: Held slot and Back taps cancel with no result or event; Start restarts at step 1. Timed cancellation and restart assertions.
11. PASS: No instruction names a control unavailable in that moment. Result events recur, use drive-token validity, and are hushed on design changes. Read with Sound off speaks the current hint. Five-action and repeat-event logs checked.

#### Wave lessons

- Hint and voice: PASS. Immediate hint updates, V.heard how-once behavior, real held two-second input, repeating events, current-hint Read, and cancellation logs.
- Focus and layout: PASS. Stable question, feature, friend, slot, and tab nodes; no load autofocus; keyboard feature-to-slot placement; reserved footer. Mode/view transitions deliberately move or hide panels.
- Sizes: PASS. Eight STANDARDS sizes including hosted 375, with compact live slots and all eleven shelf choices. Full size run once, targeted reshoots for affected fixes.
- No giveaways: PASS. Wishes and needs look alike before test; question cards carry no kind badges; no solution meter. Repeated tests are the intended prototype iteration and expose which features were used.
- Honest numbers: PASS. Four questions and three/four slots identified as this tool's limits in notes; actual step outcomes, not an estimated accessibility score.
- Standards: PASS. Solo students elicit perspectives, build, test, and revise for multiple users. Both specified E5 codes and 2017 crosswalk addressed in teacher notes.
- Motion off: PASS. No running infinite animations, instant answer reveal, unchanged four-second timing. Calm frame and animation inspection.
- Short choices in view: PASS. All available questions and all eleven features remain visible, including 680 and 375. Compact shared boards expose full-size Open notes buttons; every note and its quote is available in the work-area dialog.
- Resize mid-animation: PASS. Audit resized every listed state and active walk control without exceptions or stuck controls; separate individual/shared mid-drive checks also pass.
- No late welcome: PASS. Scope-aware welcome validity; first-action and voice logs show no delayed welcome. Direct initial Ask-tab speech corrected in targeted build fix.
- Unknown as unknown: PASS. Uninterviewed shared boards explicitly say Not interviewed yet and offer Interview.
- One look, one meaning: PASS. Yellow notes, blue facts, gray Polite yes; done and snag use consistent glyphs plus words.
- Badge says what is true: PASS. Used stamps derive from actual needs and steps, not placement alone; wishes and Weather are Never used.
- Hint changes back: PASS. Friend, tab, mode, reset, design edit, result, and cancellation update from current state.
- No answer by copying words: PASS. Friends' quotations describe experiences; shelf cards name functions. Open/leading kinds and successful combination are not labeled in advance.

#### Audit leads

Audit finished with exit 0 within 40 minutes. It reported 47 leads, all individually answered in `_scratch/design-for-a-friend/audit-dispositions.md`:

- 23 initial-card overlap/hidden-text leads: intentional rotated-paper geometry. Full-size frames confirm separated, legible text; the detector compares rotated cards as bounding rectangles.
- Eight quote-dialog/background overlaps: intentional modal layering. Underlying interview text is covered while the evidence dialog is open.
- One quote keep-region failure at 375: fixed with the work-area dialog. Four note targets and the quote now fit, confirmed by actual hosted geometry and inspection.
- Two compact phone overlaps: fixed by removing the redundant compact heading and grouping preview widgets. Phone, preview content, and live slots fit at 375 and 680, including three decorative extras.
- Nine missing-introduction leads: intentional. The spec makes the introduction stale on a friend tap. Direct tab changes also replace that introductory moment; no welcome is queued behind the action's new instruction.
- Four quick-tap Ask cuts: fixed. Idle repeats on the current friend/tab leave valid speech playing. Held double-taps for all three friends and initial Ask produce one uncropped instruction.

Motion, resize recovery, settled focus/Enter paths, and five-click narration repeats were clean. Mode-change panel movement is expected; rebuilt Interview buttons preserve focus on the chosen friend's strip. No application exceptions were found. The full audit was not repeated after targeted fixes.

#### Frames looked at

Opened every PNG shot, using labeled contact sheets and full-size inspection of compact and corrected states. Scratch groups: `early`, `bars`, `frames`, `functional`, `inputs`, `inputs-extra`, `last-checks`, `live-controls`, `candidate-frames`, `candidate-final-frames`, `resize-frames`, `final-frames`, and `audit`. Full run covers all eight sizes, both modes, exhausted questions, pictures, failed and successful tests, Polite yes, shared result, open quotes, grayscale, Motion off, and keyboard placement. `bar-comparison.png` compares this tool with Snowy Mail Route; `plant-sheet.png` checks all six finished cutouts. Later `final-*` frames supersede affected earlier compact/dialog frames.

#### Art made

Seven new built-in imagegen paintings: one layered garden backdrop and six botanically distinct cutouts. No people generated. Raw PNGs and full prompts retained; only `art.py --rekey <name>` processed them. No redraws were needed after final-size inspection. New art: 403,904 bytes (394.4 KiB); all ten WebPs including retained portraits: 492,082 bytes (480.5 KiB). Final self-contained bundle: 1,204,491 bytes (1176.3 KiB), under 2 MB; zero external runtime assets. SHA-256 `c56f0cb5ba27e082c76d18c3a866be19fa53de1b2b41bec715b9e85dbaa703cb`. Phone, feature icons, notes, path, stamps, and preview SVG drawn in code.

#### Art still to paint

No missing nonpeople art. Lou, Ana, and Kofi portraits already existed and were retained byte-for-byte, with original source, reference, and pending review metadata. Their owner review remains pending; this build does not approve them. Faceless code silhouettes remain available if a portrait is absent.

#### Engine changes wanted

None. Shared kit unchanged.

#### Left open

Owner review of the three existing portraits; recorded voice production intentionally not performed. Sixteen fixed strings are ready for wise-mentor / Gacrux with browser fallback. Spec open questions resolved toward keeping three friends and keeping wise-mentor, recorded in handoff.

The mechanical audit was run once, with a 40-minute limit, against its frozen bundle. Corrections after its findings received only targeted checks; the full audit and full size run were not repeated. The final targeted drive batches were clean; the saved audit still describes the earlier snapshot. Early test-helper selector errors and one host favicon 404 were corrected; later hosted checks were clean. Initial read-only setup calls used tool return limits before hard subprocess deadlines were adopted for subsequent commands.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: design-for-a-friend

#### Played
Grade 5 solo walkthrough of all three interviews, evidence boards, failed and successful prototypes, Polite yes, and shared design before reading the builder's files. Replayed the class/projector path. Listening and testing feel purposeful; the garden and portraits are strong.

#### Findings fixed
- **Should fix, general, src.html avatar:** fallback silhouettes showed behind loaded portraits, giving Kofi an extra head/shoulder. Hide the SVG after the painting loads; preserve it for missing images.
- **Should fix, general, src.html updateHint:** live test-shelf selection still said to start testing; full phones named nonexistent empty slots; shared results omitted the next action. Hints now describe placement, making room, and Back to design immediately.
- **Should fix, general, shared Test drive:** only colored cells changed, hiding the person and their snag. The existing table now shows the active portrait, step, words, and a current-cell outline; snag descriptions have accessible labels.
- **Should fix, general, phone preview:** missed Save, tapped Delete, and a missed reminder looked much like success. The mock screen now shows those actual outcomes with words and symbols, retaining the five-step rule and timing. Compact controls wrap inside the phone.
- **Should fix, general, evidence overlay:** a running test and narration continued behind the board. Opening evidence now cancels them and keeps the next-action hint stable.
- **Should fix, general, voice:** Read hints were absent from the manifest. Centralized hints and their named variants now match allLines and all 58 entries in voice/lines.json.
- **Should fix, general, initial navigation:** revealing Reset moved Ask under a double tap, so the second tap hit Test and cut the instruction. Reserved the Reset footprint; all three tab rectangles now remain identical before/after entry at 1366 and 680. Real fixed-point double taps stay in Ask with one uncut instruction.
- **Should fix, general, direct Test entry:** the hint named Start but no instruction spoke. The existing Start hint now speaks once with current-state validity; five held taps produced exactly one start.
- **Should fix, general, quote dialog:** a real background click spent a question and left the sheet stale. Background work areas are now inert while it is open. Held clicks stay blocked on laptop/phone; Back and Escape restore controls and focus, and Read still speaks the board hint with Sound off.
- **Polish, general, restored results:** returning to a completed drive reset the marker and mock screen to step 1. Restored results now show step 5.
- **Polish, general, art:** redrew the weakest plant, kohlrabi, with a clear botanical silhouette; cleaned magenta fringes and gaps in all six plant cutouts. Preserved the garden and portraits.
- A null-state regression in the preview repair was caught and fixed before the final audit. The affected functional and held-input checks then passed without console errors.

#### Findings left
- No confirmed blocker or should-fix remains open.
- **Polish, general:** recorded narration is unavailable; this review obeyed the instruction not to record audio. Browser speech remains the fallback.

#### Flattest moment left
After all four shared features work, another identical run has little surprise. The shared portrait/quote makes the first test more human; further depth would require changing the fixed scenario, so none was added.

#### Graphics
Checked all ten images in their actual scenes and the finished plant/people contact sheet. One built-in OpenAI imagegen redraw, plant-kohlrabi; raw art saved at tools/design-for-a-friend/art/raw/plant-kohlrabi.png, full prompt in art/prompts.json. Six plant cutouts rekeyed using art.py --rekey only. All three people assets retain people:true and their existing pending owner-review metadata. No missing art tokens. Art: 479.3 KiB. Bundle: 1180.2 KiB, about 1.21 MB. Compared the existing Snowy Mail Route and Beat Lab frames (review-bar-comparison.jpg); retained the rich studio finish.

#### Audit
Finished once with exit 0 within the 40-minute limit, Chrome 9961 and host 8765. All eight sizes, the nine states in its frozen plan, Motion off, control walks, repeats, rapid taps, and resize stress completed. No application errors or stuck controls. Opened all audit PNGs directly or in labeled contact sheets; compact result and phone frames also inspected directly.

All 32 leads answered in Scratch/review-audit-dispositions.md: 22 tilted-card rectangle false positives; nine welcome warnings where the introduction correctly becomes stale; one real fixed-point Ask interruption, repaired. The Test row also exposed missing first-entry speech; the quote frames prompted the confirmed background-click repair. Only affected paths were re-shot afterward at 1366x768, 680x425, and hosted 375x812. The full audit was not repeated after these final narrow repairs.

Independent checks: 6,144 friend/subset outcomes; exactly one successful four-feature set, none of three, eight of five; empty snags and all ten contrast ratios match the spec (lowest 5.02:1). All 22 functional assertions pass. Keyboard Enter placement keeps slot focus; whole-pixel jittered drag places a feature; grayscale keeps checks, exclamation marks, and words; Motion off preserves the 4.074-second test.

| Voice line | Kind | Expected starts | Actual starts |
|---|---|---:|---:|
| ask, open-q, closed-q, design | how | 1 each | 1 each |
| lou-done | event, five drives | 5 | 5 |
| lou-snag | event, five drives | 5 | 5 |
| direct Test instruction | how, five taps | 1 | 1 |

Held clicks used 0.12 seconds; the five-action run used two-second gaps. Results were deliberately restarted while their narration played; obsolete speech stopped. Read matched the current hint with Sound off. All 58 possible Read/narration lines match the manifest exactly.

#### Left open
Existing owner review of Lou, Ana, and Kofi remains pending; the review-art.png contact sheet in Scratch includes them. No kit or spec changes. No commits. All owned browsers and host servers closed; no host.html remains. No actual classroom or audible headphone test. The initial read-only rules command lacked a hard timeout; every subsequent shell command used a deadline.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Design for a Friend handoff

Build only, 2026-10-31. No commits, shared kit edits, deployment, or polish round. All work is in this tool and `_scratch/design-for-a-friend/`.

#### Structure

`src.html` starts from the kit starter. CSS lays out actual pixel-sized controls, rather than scaling a fixed canvas. Content tables FRIENDS, FEATURES, NEEDS, QUESTIONS, STEPS, and L precede state and behavior. `evaluate(who, list)` is the pure five-step task rule. Interview progress is independent for each friend; the shared app has its own four slots. Nothing is persisted except the kit's Motion setting.

Ask stores the exact quotes with each note. Follow-ups extend the original note. Need and wish notes share the same markup and color; blue fact cards differ. Polite yes appears only after testing the corresponding wish feature. A feature counts as Used if it meets a need in this task. All five steps run even after a snag.

The drive uses an incrementing cancellation token and 800 ms per step, with Lou, Ana, and Kofi sequentially in the shared mode. Every slot, shelf card, friend, tab, and mode stays live. `stopDrive()` invalidates the token before the pending timer resumes. Resizing changes only layout, leaving the model and timing intact.

Question, shelf, friend, tab, and slot button nodes stay stable while their contents update. Questions and placed shelf cards use aria-disabled with guards so focus stays on the control just used. Feature placement supports tap then slot, Enter then Enter, and a real pointer drag with an integer-coordinate jitter test. Focus moves with preventScroll only when opening or closing a board or leaving an introductory friend card.

At short heights the test phone rotates into a landscape prototype so its three live slots fit with the five-step path. Shared designs use a two-by-two slot grid in compact views. At 375 pixels the slots come before the shelf. The quote board is an overlay with Escape, Back, and contained Tab focus.

Compact shared boards expose one full-size Open notes button per interviewed friend. This opens all collected notes and their original quotes without cutting a small set of note buttons halfway off. Desktop boards retain their side-by-side notes. The dialog uses the work area's measured bounds on opening and resizing. The yes/no reflection stays beside the answer even when question four also triggers the time-up hint. The shared mode remembers its last Design/Test view as well as its slots and results.

#### Voice

Curio.voice owns speech, Read, and the log. Hints change immediately in tool code; Read returns that exact text. How lines use V.heard through the kit's once-only mechanism. Event lines are the six friend result strings, polite, all-done, and all-snag. Result validity closes over the drive token. Ask stops a spoken instruction when its question controls cease to fit, and design edits stop obsolete event speech. No recordings were made; voice/lines.json contains the sixteen fixed strings for wise-mentor / Gacrux, with browser fallback in this build.

#### Art and provenance

Seven new built-in imagegen images were made: garden-backdrop and six plant cutouts. Full prompts are in art/prompts.json, originals in art/raw, and final WebP images were processed only with art.py --rekey. The plant kit was inspected on warm paper at final size, including kohlrabi shape and magenta-key edges. The garden was inspected at full size and in the scene.

The three existing portrait WebP files were retained unchanged. Their original prompts, source, reference links, and pending review records were restored from HEAD and preserved. No new people, faces, or body parts were generated. Their previous pending owner review status remains pending. If a portrait is absent, the code's faceless silhouette works with its art token.

#### Open questions resolved for this build

- Keep Lou, Ana, and Kofi as the three users, as the spec leans. Existing portraits are used; their pending owner review is not silently promoted to approved.
- Keep wise-mentor (Gacrux), as the spec leans, so spot-the-ai retains curious-librarian. The fixed voice manifest records this choice.

#### Numbers and evidence

`_scratch/design-for-a-friend/setup.py` independently checks all 2,048 subsets, exact four- and five-card solution counts, empty-design snags, and ten WCAG contrast pairs. `numbers.json` records results. `checks.js` compares 6,144 browser evaluations and tests real drives, quote budgets, duplicate refusal, cancellation, restart, and mode persistence. Functional evidence, held-input voice logs, real drag, keyboard, grayscale, reduced-motion, and size frames are in Scratch. The bar tools were copied and bundled in Scratch to obey the write boundary.

`resize-results.json` checks actual viewport changes during both individual and shared drives; each finishes without exceptions or a stuck running state. `candidate-final-frames` covers the completed compact board/dialog, four-question reflection, full three-feature phone, shared plant preview, and restored shared result. Early geometry probes used a nonexistent test selector; that test helper was corrected before final checks. It was not an application exception.

The mechanical audit ran once, finished within its 40-minute limit, and reported 47 leads. `_scratch/design-for-a-friend/audit-dispositions.md` answers each one: 23 rotated-card rectangle false positives, eight intentional dialog-over-background overlaps, nine intentionally stale introduction cancellations, and seven corrected phone/quote/rapid-tap leads. Its Motion, resize, and settled keyboard checks were clean. The raw report is `audit/audit.md`; it describes the pre-fix bundle. Only affected views and controls were checked afterward, including hosted 375 geometry and 0.7-second held double-taps. The full audit was not repeated.

An idle repeat tap on the current friend or tab leaves valid narration playing. During a running test the same tap still takes the cancellation path. Compact preview extras become a small row of widgets, preserving their effect without intruding into feature slots. All three slots stay at least 44 pixels high. Final frames are collected in `final-frames`; final verification and static asset checks are reproducible with `verify-final.py` and `static-check.py`.

#### Engine changes wanted

None. The shared kit is unchanged.

#### Cold review repairs, 2026-11-03

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

#### Next

The separate cold review can inspect the compact layouts and voice evidence, and the owner can review the retained portraits. This build does not begin that review or a polish round.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
