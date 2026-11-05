# Sketchbook Process Journal build handoff

## Built
An offline journal with a read-only seven-page sample, a private 12-page working book and a source-linked idea map. No commits and no polish round.

## Source map
- `src.html` starts from the starter's document, kit includes and header. It uses its own light palette as the spec requires.
- `content.json` is loaded through the bundler's JSON token. It contains the exact issue facts, tradition contexts and traits, Theo's pages and nine tags. The source list is preserved there too.
- The inline script owns book navigation, guarded local saving, modal confirmation, choices, tags, canvas strokes, the plan form and the map. `window.__tool` exposes state, both books, data, art, counts, rendering, save and voice logs.
- `render` restores shared hint and status elements before rebuilding a page. The keyboard focus id is retained; deleting or clearing returns focus to the page picker.
- Every pad has a 1200 by 900 backing canvas. Pointer coordinates use its current real-pixel rectangle, and pen pressure changes the width. Pointer capture ends on up, cancellation or loss of capture.
- Undo stores at most 20 compressed lossless PNG snapshots per box in memory, not raw pixel buffers. Saved drawings are downscaled to 800 by 600 WebP at quality 0.6. Undo history does not survive reload.
- `renderMap` lays out 120-pixel columns and five lanes at real pixels. A fixed source column sits beside the horizontal scroller. Each source's outgoing links fan four pixels apart. Nodes stay in column order in the DOM.
- Filters retain positions and dim unmatched nodes and source links to 25 percent. Tradition includes borrowed and broke-from tags; Mine includes broke-from and own-idea tags.
- At compact widths the book shows one leaf and a Tags toggle. On phones the actual hint, Add page and save status move into the book. The four thumbnail boxes scroll vertically at full width with tools above them.

## Saving and privacy
The sole book key is `curio-sketchbook-journal`. Writes are debounced one second after edits, with an immediate save on leaving My book or the page. Storage access is guarded. A failed write keeps the full in-memory book and displays the specified warning. Clear book asks once and removes the key. No names, network requests, exports or device-transfer features.

The maximum source estimate omitted base64 expansion. Forty-eight 40 KB drawings take about 2.56 MB as base64 before the journal metadata, rather than 1.9 MB. Actual complexity determines size, so the failure message remains necessary.

## Decisions and open questions
- Retain the specified clear-teacher bank voice, Iapetus, pending an owner-side bank addition. The spec leans toward borrowing it for this build. Adding a grown-up voice and changing the shared bank are outside the permitted folders. No recording was made; browser speech supplies runtime narration.
- Cold review restored the spec's skull vanitas and bottle-skull thumbnail. Current people rules do not prohibit conventional skull symbols. No living figure is depicted; people flags remain false.
- Added one compact how-to line, openTags, so the narration names the visible Tags control before the hidden tag editor. The other fixed lines follow the spec. The queue is `Curio.voice` with mode scope, valid checks and visible-control requirements.
- A Plan becomes available after any Thumbnails page exists. Revision is allowed without one, as listed in Add page, and explicitly shows that no earlier thumbnails exist.
- Existing bar bundles were opened without rebundling them, because rebundling would write outside the two authorized folders. Beat Lab has no handoff or refine file here. Storyboard Studio's source and handoff supplied the built-neighbor context; no refine file was present.
- The report is written only at the end, following the user's explicit instruction to stop as soon as it is written.

## Art made
Fifteen finished WebP images, each below 80 KB and with long side 1000 pixels. Prompts, house style and provenance are in `art/prompts.json`; selected PNGs are under `art/raw/`. All were made with the built-in image tool and inspected at final size. The monarch painting was redrawn once: the first version's snowy alpine peaks were misleading, so the final shows a close oyamel fir-forest interior. WPA bands are blank. No people or human body parts appear.

## Checks and evidence
Everything is under `_scratch/sketchbook-process-journal/`.
- `prepare.py`, `numbers.json`: independent tag counts, exact palette contrast, storage accounting and Fahrenheit interval conversions. Source dates and measured estimates are inputs, not invented computations.
- `student_check.py`, `student/results.json`: 40 checks, including all sample node destinations, actual jittered mouse strokes, pen and touch input, 20-step Undo, saved image size, reload, tags, old-source retention, plan constraints, storage failure and the 12-page map. All passed with no console errors.
- `full/`: one full STANDARDS size pass plus the sample Plan, compact map, My book and grayscale. Every frame was opened. Targeted phone frames were repeated only after the overlapping canvas layout was corrected.
- `phone/`: 375 by 812 through the required host. Actual hint and save status are visible in the working book, with tools above the full-width pad. No horizontal document scroll. The phone runner removes its temporary host and closes its server.
- `keyboard/`: an entirely keyboard-driven issue, tradition, thumbnail, source tag, map node, cancellation, deletion and clear workflow. The first test attempt needed the driver's Enter key event corrected to include its character; no tool change was needed for that harness issue.
- `voice-pace.json`: five held page adds near two seconds apart, repeated broke-from events, Read and a mode change.
- `bar/`: opened Beat Lab and Snowy Mail Route. `comparison.png` places this tool beside Beat Lab.
- `audit/`: the one final mechanical audit. Its outcome and all lead dispositions belong in the final report.

## Engine changes wanted
None. Kit, scripts, docs, other tools and the voice bank were not changed.

## Review cautions
This is a plain pencil journal. A selected palette describes the planned work; it does not recolor strokes. Tags are optional and can represent a student's argument rather than a scored answer.

The complete 12-page map requires scrolling. On compact screens its lanes also require vertical scrolling; the count and hint stay outside that scroller. The fixed source list scrolls vertically with the map, while remaining stationary during horizontal scrolling.

Plan fields and long tag editors scroll inside their paper leaf. Drawing tools stay sticky on that leaf. A phone exposes one thumbnail at a time in the vertical drawing strip. These are deliberate space tradeoffs, not a claim that every secondary control fits at once.

Source dates and environmental claims follow the supplied spec. No outside fact-checking or recorded-voice listening was performed in this build.

## Final audit and targeted build corrections
The one audit completed with 45 leads and 54 PNGs. All 54 frames were viewed in seven QA sheets; affected compact states were also opened individually. No console errors, infinite animations, resize exceptions or controls left disabled were reported. Every lead is answered in the report and `_scratch/sketchbook-process-journal/audit-responses.md`.

After the audited bundle, choice buttons moved outside their scrolling details, modal actions gained a reserved row, compact drawing rows gained a useful minimum size, and the short-landscape My book panel reclaimed space from its introduction. Navigation buttons and the page picker keep their DOM identity; mode changes move focus to the visible mode button. Plan fields now have explicit accessible names. Map sources and nodes share vertical scrolling, and gray old-source nodes still dim to exactly 25 percent when filtered out. Clear cancels pending saves, and an empty book keeps the storage key removed. Reconfirming a choice in a full book no longer names disabled Add page.

The final targeted checks passed with zero console errors. Stable navigation, mode focus, accessible field names, map alignment, old-tag opacity, delayed clearing and twelve-page source fixation have saved JSON results. The keyboard journey passed eleven checks. Six final phone frames cover the affected choices, study, plan, node dialog and the right end of the twelve-page map. The full audit was not rerun.

Queued how-to lines also check the exact waiting moment: opening an issue/tradition card invalidates its earlier welcome, selecting an aspect invalidates tagHow, and showing Tags invalidates openTags. The final held-tap voice pace was repeated after these validity checks changed.

The authored phone audit-state entries originally used `375` rather than `375x812`, so six optional authored phone states were skipped. Default, both automatic modes, the sample plan and sample node dialog still received the audit's phone checks. The configuration is corrected for the cold review; targeted phone checks cover the omitted editing layouts.

Remaining mechanical leads are the expected scrolling map topology, duplicate phone panel actions below the fold, less frequent phone Delete/Clear actions below the book, the confirmation dialog's deliberate stale how-to drop, and the spec-mandated welcome that becomes stale on first navigation. Visible header modes provide the duplicate actions. These are disclosed limits, not a claim of a clean audit.

## Cold review repairs, 2026-11-04
- Restored the two key skull images with the built-in image tool. Prompts and raw PNGs are in art; finished files use art.py --rekey. Other strong art stays.
- A new tag immediately shows its source mark and aspect as a small receipt on the existing tag card. Motion off removes its highlight animation.
- Thumbnail map previews and node cards compose all four drawing boxes, including when the first one is empty. No extra saved image is needed.
- Empty maps, compact Tags/Page hints and the enabled Add page tooltip now match their controls. Resize across layout breakpoints updates the layout after an active stroke ends.
- Save status stays Saving while a write is pending. Invalid stored structure gives a recovery message and leaves the stored copy alone until the student edits. Full/blocked storage still preserves in-memory work.
- Deleting a referenced thumbnail page selects an available earlier thumbnail. An undrawn reference displays Not drawn yet instead of a broken image.
- Pointer completion cannot commit a detached canvas into a different page.
- The current cold-review audit and evidence are in Scratch/review-audit and Scratch/interactive-results.json. See codex-review.md for the final outcome.
- Final audit-frame repairs reveal the first decision inside the existing map scrollers and name scrolling in welcomeMap; short node dialogs give source/note room beside smaller art. Clear book resets a prior recovery warning after successful removal. Only those views were rechecked after the single audit.

Cold-review closeout: the single audit completed with 41 leads and 65 viewed frames. Repeated speech, quick taps and resize stress were clean. Lead dispositions are in Scratch/review-audit-responses.md. Targeted map/dialog/recovery rechecks passed, all nine voice lines match, the final bundle is 1432.1 KiB, and test Chrome processes, host server and temporary host.html are closed/removed.
