# Codex report: design-for-a-friend

## Built

Grade 5 interview, prototype, and task-test studio for Maple Street Garden. Three independent four-question interviews feed quote-backed boards. Eleven features fit three individual slots or four shared slots. Five-step tests reveal actual use, snags, and polite agreement. Both modes retain their progress.

Built from the kit starter with Curio.voice, Motion, Sound, Read, tones, and fitting. No family engine. No commits, deployment, shared-file edits, or polish round. All writes stayed in the tool and its Scratch folder. Chrome 9980, 9981, and 9982; host 8785. Servers and browsers owned by this build were closed.

## Numbers check

PASS. Independently enumerated all 2,048 feature subsets in `setup.py`: no three-card solution, exactly one four-card solution (Read aloud, Big buttons far apart, English and Spanish switch, Reminder you set), eight five-card solutions. All empty-design snags and ten contrast pairs match the spec. Browser evaluation checked 6,144 friend/subset combinations. Shared success took 12.092 seconds; Motion-off individual test took 4.060 seconds. No spec-number corrections.

## Feel check

Best moment: Lou finishes with the apparently helpful Video lessons untouched, and his yellow wish receives the gray Polite yes stamp. The student's own question and feature choices make the reveal specific. The later shared round changes the problem: four slots must meet six needs, so Read aloud and Big buttons earn their value for two people.

Two flat moments changed during build: the marker was too small and simply jumped between steps, so it now travels visibly above the path; compact prototype and evidence views hid the payoff, so live 44-pixel slots, landscape test phones, and a work-area quote dialog keep the design and evidence readable. The four-note board and retained shared-result view received targeted checks after the mechanical audit snapshot.

Played the interview, unsuccessful redesign, successful redesign, and shared solution. Compared `bar-comparison.png` against Snowy Mail Route and inspected Beat Lab. The garden, cutout plants, cork boards, layered phone, moving portrait, stamps, and result table match the finish bar without borrowing either tool's scene. This is a deliberate classroom design activity, with its depth in interviewing different users and reconciling needs.

## Done when

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

## Wave lessons

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

## Audit leads

Audit finished with exit 0 within 40 minutes. It reported 47 leads, all individually answered in `_scratch/design-for-a-friend/audit-dispositions.md`:

- 23 initial-card overlap/hidden-text leads: intentional rotated-paper geometry. Full-size frames confirm separated, legible text; the detector compares rotated cards as bounding rectangles.
- Eight quote-dialog/background overlaps: intentional modal layering. Underlying interview text is covered while the evidence dialog is open.
- One quote keep-region failure at 375: fixed with the work-area dialog. Four note targets and the quote now fit, confirmed by actual hosted geometry and inspection.
- Two compact phone overlaps: fixed by removing the redundant compact heading and grouping preview widgets. Phone, preview content, and live slots fit at 375 and 680, including three decorative extras.
- Nine missing-introduction leads: intentional. The spec makes the introduction stale on a friend tap. Direct tab changes also replace that introductory moment; no welcome is queued behind the action's new instruction.
- Four quick-tap Ask cuts: fixed. Idle repeats on the current friend/tab leave valid speech playing. Held double-taps for all three friends and initial Ask produce one uncropped instruction.

Motion, resize recovery, settled focus/Enter paths, and five-click narration repeats were clean. Mode-change panel movement is expected; rebuilt Interview buttons preserve focus on the chosen friend's strip. No application exceptions were found. The full audit was not repeated after targeted fixes.

## Frames looked at

Opened every PNG shot, using labeled contact sheets and full-size inspection of compact and corrected states. Scratch groups: `early`, `bars`, `frames`, `functional`, `inputs`, `inputs-extra`, `last-checks`, `live-controls`, `candidate-frames`, `candidate-final-frames`, `resize-frames`, `final-frames`, and `audit`. Full run covers all eight sizes, both modes, exhausted questions, pictures, failed and successful tests, Polite yes, shared result, open quotes, grayscale, Motion off, and keyboard placement. `bar-comparison.png` compares this tool with Snowy Mail Route; `plant-sheet.png` checks all six finished cutouts. Later `final-*` frames supersede affected earlier compact/dialog frames.

## Art made

Seven new built-in imagegen paintings: one layered garden backdrop and six botanically distinct cutouts. No people generated. Raw PNGs and full prompts retained; only `art.py --rekey <name>` processed them. No redraws were needed after final-size inspection. New art: 403,904 bytes (394.4 KiB); all ten WebPs including retained portraits: 492,082 bytes (480.5 KiB). Final self-contained bundle: 1,204,491 bytes (1176.3 KiB), under 2 MB; zero external runtime assets. SHA-256 `c56f0cb5ba27e082c76d18c3a866be19fa53de1b2b41bec715b9e85dbaa703cb`. Phone, feature icons, notes, path, stamps, and preview SVG drawn in code.

## Art still to paint

No missing nonpeople art. Lou, Ana, and Kofi portraits already existed and were retained byte-for-byte, with original source, reference, and pending review metadata. Their owner review remains pending; this build does not approve them. Faceless code silhouettes remain available if a portrait is absent.

## Engine changes wanted

None. Shared kit unchanged.

## Left open

Owner review of the three existing portraits; recorded voice production intentionally not performed. Sixteen fixed strings are ready for wise-mentor / Gacrux with browser fallback. Spec open questions resolved toward keeping three friends and keeping wise-mentor, recorded in handoff.

The mechanical audit was run once, with a 40-minute limit, against its frozen bundle. Corrections after its findings received only targeted checks; the full audit and full size run were not repeated. The final targeted drive batches were clean; the saved audit still describes the earlier snapshot. Early test-helper selector errors and one host favicon 404 were corrected; later hosted checks were clean. Initial read-only setup calls used tool return limits before hard subprocess deadlines were adopted for subsequent commands.
