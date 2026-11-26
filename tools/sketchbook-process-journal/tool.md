# Sketchbook Process Journal: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: sketchbook-process-journal

#### Built

- Offline Sample book, My book and Idea map, with the specified issue facts, tradition traits and seven-page Theo sample.
- Mouse, pen-pressure and touch drawing; four thumbnails; studies; revisions referencing earlier thumbnails; plan form; 24 named swatches; optional decision tags.
- Guarded automatic device saving, 20-step Undo, confirmed clearing and deletion, old-source preservation, 12-page limit, keyboard access and Curio.voice.
- Own light desk-and-paper scene, 15 generated illustrations, a quiet light animation and immediate drawing/selection feedback.
- Build only. No commits or polish round. Writes stayed in the two authorized folders. Existing bar bundles were opened without writing to those tools.

#### Numbers check

- `numbers-final.json` independently counts the actual sample tags: research 3, borrowed 2, broke 2, own 2, total 9.
- Contrast: brand/paper 6.434:1, white/brand 7.129:1, ink/paper 15.586:1, muted/paper 6.595:1. White node letters: research 6.656:1, broke 7.292:1, own 6.381:1.
- The spec's 1.9 MB storage estimate omits base64. Its conservative 48 drawings at 40 KiB become 2560 KiB as base64, before metadata. The actual book permits at most 40 drawings because pages 1 and 2 are fixed, giving 2133 KiB under that assumption. Storage failure is handled on screen.
- Source dates, Fahrenheit intervals, plastic tonnage and the 5 mm threshold are retained as supplied source inputs. Fahrenheit interval conversions were also recomputed in `numbers.json`; no new converted values were added to the UI.

#### Feel check

- Played Theo's complete book, opened every map decision, then made an issue/tradition choice, thumbnails, tags, study, revision and plan.
- Best moment: Theo's final cardboard still life beside its material and microplastic decisions, followed by seeing my own thumbnail enter the same source map.
- Flat moment 1: the raw paper texture competed with the text and art. A translucent cream layer now keeps its tooth without turning every page into visual noise.
- Flat moment 2: the compact drawing grid felt cramped and phone canvases overlapped. The phone now shows full-width boxes in a vertical strip; compact landscape rows keep a usable drawing size and scroll inside the working leaf.
- `comparison.png` places the tool beside Beat Lab. The large original art, paper, spine, desk and source map carry comparable visual weight while fitting this journal's purpose. Snowy Mail Route was also opened for immediate feedback and motion reference.
- This is an investigation studio, not a scored game. Its later depth is the student's studies, deliberate breaks and evidence-backed revisions, culminating in a specific plan and map.

#### Done when

1. PASS. The book occupies over 60 percent of the 1366-wide screen; book and map remain the dominant region at 680x425. Full-size frames and compact targeted frames were viewed.
2. PASS. Exactly nine sample nodes. All nine cards were opened with real held clicks and each Open this page reached the expected sample page.
3. PASS. Add page is locked until both choices are confirmed. The hint and narration do not name it while locked. The keyboard and student runs checked this.
4. PASS. Real jittered mouse strokes, CDP pen and touch input, compressed 800x600 saving and reload persistence passed. Undo restored the first drawing after undoing the latest 20 of 21 strokes. Physical pen hardware was not available.
5. PASS. All four tag kinds appear with shape, letter and linked source. Filter classes and visual dimming were checked, including the final old-tag opacity correction.
6. PASS. Changing the issue retained every existing tag and showed the previous research source gray with the old-issue label.
7. PASS. Twelve-page horizontal scrolling and fixed sources passed. Final 760 and 375 layout checks are recorded below.
8. PASS. Five held page adds had gaps of 2037, 2050, 2047 and 2058 ms. tagHow started once, no spoken how line repeated, both new broke-from tags started firstBreak, Read was logged and the post-Read mode change completed without errors.
9. PASS. All 15 final WebPs were opened and inspected; art tokens load. No people, human body parts or fake lettering; WPA bands are blank. The skull-image conflict was resolved as described in the handoff.

#### Wave lessons

- Hint and voice: PASS. Hints update with state, Read uses the visible current hint, compact instructions name Tags, disabled Add and final-page Next are not named. The five-add pace run passed.
- Focus and layout: PASS. No load focus; page picker focus after adding, deleting or clearing; dialogs restore focus. Keyboard-only journey passed eleven checks, including delayed Clear persistence. Compact modal/choice action fixes received targeted checks.
- Sizes: PASS for primary controls, with the phone secondary-panel limitation below. One full STANDARDS run, then only affected compact and phone states. Targets are 44 px; long editors deliberately scroll. See Left open for strict short-choice audit leads.
- No giveaways: PASS, not applicable to a scored puzzle. The student authors choices; there is no hidden correct answer or success meter.
- Honest numbers: PASS. Research dates remain visible, historical estimates are not represented as current totals, plan dimensions are labeled in cm and sample counts are computed from tags.
- Standards: PASS. Solo students generate alternatives, investigate contextual traditions, study and revise, and explain research/history connections in a final plan. No family engine is specified.
- Motion off: PASS. The decorative light stops, while drawing and navigation remain immediate. Calm and grayscale frames were viewed.
- Short choices in view: FAIL under the literal audit rule for map nodes; the spec requires a scrollable map. Issue/tradition pickers show all three cards. Choice confirmation and modal actions stay outside their scrolling content. Long page, palette and tag editors retain scrolling rather than shrinking type.
- Resize mid-animation: PASS. The final audit reported no exceptions or stuck controls. No moving simulation owns a stale geometry reference; canvas coordinates use current rectangles.
- First-tap welcome: PASS. Curio.voice owns first-tap ordering with mode scope and stale checks, without welcomeAfter. Sample navigation and page additions were exercised with held clicks.
- Unknown stays unknown: PASS. Empty drawings are blank, untagged working pages say Not tagged yet, and a Revision without earlier thumbnails says so.
- One look, one meaning: PASS. R square, T triangle, B split diamond and O circle remain distinct in grayscale. Old-source gray is labeled separately.
- Truthful badges: PASS. Saved reflects a successful write or the specified warning; chosen issue/tradition labels match committed choices. Plan completion checks title, medium, palette and statement.
- Hints change back: PASS. Page and mode navigation recompute the hint; the last sample page points to Prev page and See the map. Compact Tags returns to the current page instruction.
- No answer by copied wording: PASS, not applicable to a quiz. Research wording supplies evidence; students must draw, select an aspect and explain its relationship.

#### Audit leads

The one audit finished with 45 leads and 54 frames. It reported no console errors, infinite motion, resize exceptions or stuck controls.
The responses below cover all 35 size/state rows and the 10 counted walk findings. Full wording is in Scratch/audit-responses.md.
Navigation controls now retain DOM identity; the final stable-navigation.json check passed. The full audit was not rerun after repairs.

- 1. 375x812 (iframe host), control below the fold: #seeMap "See the map ↗" top 842: Left open: duplicate phone panel button is below the fold; the equivalent Idea map header control is visible.
- 2. 375x812 (iframe host), control below the fold: #startOwn "Start my own book" top 893: Left open: duplicate phone panel button is below the fold; the equivalent My book header control is visible.
- 3. mode My book, Choose this issue below its scroll view: Fixed: issue/tradition confirmation stays outside the scrolling detail. Compact button bottom is 400 px within 425 px.
- 4. mode My book, compact panel hid Delete/Clear: Fixed: compact My book panel removes introductory text so all four action buttons stay visible; targeted 680 frames checked.
- 5. mode My book, control below the fold: #seeMap "See the map ↗" top 849: Left open: duplicate phone panel button is below the fold; the equivalent Idea map header control is visible.
- 6. mode My book, control below the fold: #deletePage "Delete page" top 900: Left open: occasional phone Delete/Clear actions follow the book; primary drawing, Add and mode controls remain visible.
- 7. mode My book, control below the fold: #clearBook "Clear book" top 951: Left open: occasional phone Delete/Clear actions follow the book; primary drawing, Add and mode controls remain visible.
- 8. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 9. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 10. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 11. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 12. mode Idea map, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 13. node-card, focus fell to the page after clicking #seeMap (click 1): Fixed: mode transitions focus the visible mode button with preventScroll; final map-focus.json passes.
- 14. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 15. node-card, modal actions outside its scroll view: Fixed: dialog actions have their own reserved row and the body scrolls; 680 and phone frames show both actions.
- 16. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 17. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 18. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 19. node-card, map nodes outside the current scroll view: Retained by spec: real-pixel columns and 44 px nodes require scrolling. Nodes stay keyboard reachable; all nine sample destinations and fixed sources were tested.
- 20. thumbnails, small target: #pad-0 "Thumbnail 1. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 21. thumbnails, small target: #pad-1 "Thumbnail 2. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 22. thumbnails, small target: #pad-2 "Thumbnail 3. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 23. thumbnails, small target: #pad-3 "Thumbnail 4. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 24. thumbnails, compact panel hid Delete/Clear: Fixed: compact My book panel removes introductory text so all four action buttons stay visible; targeted 680 frames checked.
- 25. tagged-map, focus fell to the page after clicking #seeMap (click 1): Fixed: mode transitions focus the visible mode button with preventScroll; final map-focus.json passes.
- 26. study, compact panel hid Delete/Clear: Fixed: compact My book panel removes introductory text so all four action buttons stay visible; targeted 680 frames checked.
- 27. plan-form, control with no name: #planTitle: Fixed: explicit aria-label added in addition to the wrapping label; final plan-accessible.json passes.
- 28. plan-form, control with no name: #planStatement: Fixed: explicit aria-label added in addition to the wrapping label; final plan-accessible.json passes.
- 29. plan-form, compact panel hid Delete/Clear: Fixed: compact My book panel removes introductory text so all four action buttons stay visible; targeted 680 frames checked.
- 30. clear-confirm, small target: #pad-0 "Thumbnail 1. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 31. clear-confirm, small target: #pad-1 "Thumbnail 2. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 32. clear-confirm, small target: #pad-2 "Thumbnail 3. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 33. clear-confirm, small target: #pad-3 "Thumbnail 4. Draw with a pointer. Arrow " 43x32: Fixed: compact drawing rows have a 150 px minimum; final compact thumbnail pads are about 140 by 104 px.
- 34. clear-confirm, tagHow dropped during Clear confirmation: Intentional stale drop: a confirmation dialog replaces the drawing instruction. It is not marked heard; Read and later page entry remain available.
- 35. compact-tagged-map, focus fell to the page after clicking #seeMap (click 1): Fixed: mode transitions focus the visible mode button with preventScroll; final map-focus.json passes.
- 36. Control walk, Sample See the map lost focus: Fixed: the arriving mode button receives focus; stable navigation DOM and map focus were verified.
- 37. Control walk, Sample Start my own book lost focus: Fixed: the arriving mode button receives focus; stable navigation DOM and map focus were verified.
- 38. Control walk, My book See the map lost focus: Fixed: the arriving mode button receives focus; stable navigation DOM and map focus were verified.
- 39. Control walk, Next page skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 40. Control walk, 2 Tradition skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 41. Control walk, 3 Thumbnails skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 42. Control walk, 4 Study skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 43. Control walk, 5 Revision skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 44. Control walk, 6 Revision skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.
- 45. Control walk, 7 Plan skipped welcome: Intentional per spec: welcomeSample is stale after a tab or Next page. It stays unmarked and can play on a later mode entry.

#### Frames looked at

- `bar/`: Beat Lab and Snowy Mail Route; `comparison.png`: side-by-side with Beat Lab.
- `early/`: three initial book/map frames, used to correct texture and compact sizing.
- `student/`: all seven workflow frames, including tagged thumbnails, revision, plan fields, old-source map and twelve-page map.
- `full/`: all 11 frames, including every desktop STANDARDS size, sample Plan, compact map, My book and grayscale.
- `phone/`: all three final 375x812 host frames, after the phone grid fix; the earlier affected frames were also inspected.
- `keyboard/keyboard-map.png`: final keyboard focus and filtered map. The first harness attempt required the driver's Enter event character, not a tool repair.
- `audit/`: all 54 PNGs viewed in seven QA sheets, with affected compact states also opened individually.
- `targeted/`: all eight frames; `final-checks/`: all five frames; `phone-final/`: all six frames; `last-hints/`: both limit-choice frames.

- `first-card/first-card.png`: final first-tap issue-card welcome suppression; zero stale welcome starts and no console errors.

#### Art made

- Fifteen finished illustrations made with the built-in OpenAI image tool. House style, prompts, drawn_by and provenance are in `art/prompts.json`; raw PNGs are in `art/raw/`.
- Total art: 1015.4 KiB. Every finished image is below 80 KiB; long side is 1000 pixels. Bundle: 1450.4 KiB, below 2 MB.
- One redraw: the monarch scene's misleading snowy alpine background became a close central Mexican oyamel fir-forest interior.

#### Art still to paint

None. The prohibited human skull imagery has intentional object substitutions; it is not waiting for generated people. Historical skull symbols remain in the text.

#### Engine changes wanted

None.

#### Left open

- Clear-teacher/Iapetus remains the planned bank voice. No audio was recorded or listened to. Runtime speech uses the browser voice. A grown-up bank voice is an owner-side follow-up, as noted in the spec.
- The full map scrolls horizontally, and compact layouts also scroll its lanes vertically. The source column stays fixed during horizontal scrolling. Long tag and plan fields scroll inside their leaf.
- Environmental source claims follow the supplied spec; no external source-verification pass was performed.
- The full audit predates the final targeted corrections and was not rerun. Six authored phone states used an incorrect size name in that audit configuration and were skipped; the file is corrected for cold review, and targeted phone frames cover issue, tradition, drawing, study, plan, dialog and the twelve-page map.
- Temporary host.html was removed and every Chrome/server started by these checks was closed. No git operation changed the checkout.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: sketchbook-process-journal
#### Played
Cold, as a grade 11 student: all seven Theo pages before reading the builder, then my own issue, tradition, thumbnails, study, revision, plan and map. The paper, art and final cardboard painting are strong; tagging originally felt like form filling.
#### Findings fixed
- Should fix, general, art/vanitas-a and sample-thumbs: the vessel/oval substitutions broke the visible skull-to-fish progression. Redrew both with the specified skull symbols; inspected raw, WebP and displayed pages. Prompts and images are saved in art using the built-in image tool and art.py --rekey.
- Should fix, general, src.html/pagePicture: the map and decision cards ignored thumbnails 2 to 4. They now compose all four boxes, including when box 1 is empty.
- Should fix, general, My book: compact Tags/Page guidance, empty-map instructions, Add page tooltip and pending-save status could contradict the visible state. Corrected them and updated guidance across layout breakpoints after the active stroke ends.
- Should fix, general, restore/clear: malformed saved structure could break the editor. Validate it, preserve the stored copy until editing, explain recovery, and reset the warning after successful Clear book. Quota failure still retains in-memory work.
- Should fix, general, Revision: deleting a referenced thumbnail left the picker and picture inconsistent; blank references showed a broken image. Rebind to an available earlier thumbnail and show Not drawn yet for empty work.
- Should fix, general, drawing: guard pointer completion so a detached canvas cannot write to another page.
- Should fix, general, compact node dialog: artwork hid the decision source/note on opening. Short node cards now reserve room for that information.
- Should fix, general, phone map: no mark was initially visible. Reveal the first decision inside the existing map scrollers and explicitly name scrolling in the map hint/voice.
- Should fix, general, content.json: the inherited storage estimate omitted fixed pages and base64. Corrected the arithmetic; no environmental research cards changed.
- Polish, general, tag card: each new or changed cause now leaves a small shaped source receipt beside its aspect, with a restrained highlight and immediate sound. Motion off removes the animation.
#### Findings left
No runtime blocker or should-fix remains in the checked scenarios.
- Polish: phones place duplicate map/book actions and occasional Delete/Clear controls below the book. Header modes and Add page remain visible; drawing tools stay with the pad.
- Spec constraint: small maps and drawing workspaces scroll at real size. This is authored work, not hidden answer choices. Sources stay fixed horizontally, and keyboard nodes remain in page order.
#### Flattest moment left
Writing the final statement is still the slowest step. It earns a specific plan and map, but the plain pencil pad is intentionally a planning tool. No extra feature was added.
#### Graphics
All 15 images checked at use size and in an art sheet; no living people or lettering. WPA bands stay blank. The two redraws restore the lesson without flattening the strong desk, texture, lighting or historical media. Bundle: 1432.1 KiB, below 2 MB.
Beat Lab and Snowy Mail Route were opened as the finish bar without writing to their folders; Scratch/review-comparison.jpg places frames beside each other.
#### Audit
One final audit finished within the 40-minute limit: 41 leads and 65 viewed frames. No console errors, infinite motion, resize exceptions, stuck controls, repeated how lines or rapid-tap failures. Each lead is answered in Scratch/review-audit-responses.md. Three phone-entry leads were repaired; the remaining scrolling/secondary-control leads and seven spec-mandated stale welcomes are explained there. The audit preceded the narrow map/dialog/recovery fixes; only affected views were re-shot afterward. No second audit or review pass.
Targeted evidence: repairs/, post-audit/, interactive-results.json, pointer-results.json and review-numbers.json in Scratch. All captured frames were viewed.
Keyboard editing, mouse/pen/touch events, 20-step Undo, reload persistence, quota failure, old-source labels, filters, plan completion and all nine node destinations checked.
Sample tags independently counted: research 3, borrowed 2, broke 2, own 2, total 9. Brand/paper 6.434:1, ink/paper 15.586:1, muted/paper 6.595:1.
| Voice line | Kind | Expected | Started |
|---|---|---|---|
| tagHow, five page adds | how | 1 | 1 |
| firstBreak, five triggers | event | 5 | 5 |
| updated welcomeMap, final entry/re-entry | welcome | 1 | 1 |
Read and the following mode change were logged. Sound and stale welcomes were covered by the audit. Voice text and manifest match.
Done when 1-9 passed in the checked scenarios: dominant spread/map, nine correct sample destinations/counts, gated Add, drawing/Undo/save, four shaped tag kinds/filter, old tags retained, twelve-page fixed sources, voice counts and all 15 images.
Wave lessons: hints, focus, sizes, truthful states, resize, unknown/blank work, grayscale marks, standards and Motion off checked. No scored puzzle, hidden answer, numeric success meter or moving simulation applies here.
#### Left open
- No narration was recorded or listened to; the specified clear-teacher identity remains in the manifest, with browser speech at runtime. Changing the shared bank is outside the allowed folders.
- Cultural check: fresh scoped review in Scratch/sensitivity.md found no stereotypes or cultural blocker. Primary-source checks and limits are in Scratch/source-checks.md.
- Spec concern retained: Theo's prescribed T5 note names a table, while the trait names careful rendering of costly objects. The specified sample tag and nine-node counts were preserved.
- No classroom trial or physical pen hardware test. No commits. Only the two authorized folders were written. Temporary hosts and test Chrome processes were closed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Sketchbook Process Journal build handoff

#### Built
An offline journal with a read-only seven-page sample, a private 12-page working book and a source-linked idea map. No commits and no polish round.

#### Source map
- `src.html` starts from the starter's document, kit includes and header. It uses its own light palette as the spec requires.
- `content.json` is loaded through the bundler's JSON token. It contains the exact issue facts, tradition contexts and traits, Theo's pages and nine tags. The source list is preserved there too.
- The inline script owns book navigation, guarded local saving, modal confirmation, choices, tags, canvas strokes, the plan form and the map. `window.__tool` exposes state, both books, data, art, counts, rendering, save and voice logs.
- `render` restores shared hint and status elements before rebuilding a page. The keyboard focus id is retained; deleting or clearing returns focus to the page picker.
- Every pad has a 1200 by 900 backing canvas. Pointer coordinates use its current real-pixel rectangle, and pen pressure changes the width. Pointer capture ends on up, cancellation or loss of capture.
- Undo stores at most 20 compressed lossless PNG snapshots per box in memory, not raw pixel buffers. Saved drawings are downscaled to 800 by 600 WebP at quality 0.6. Undo history does not survive reload.
- `renderMap` lays out 120-pixel columns and five lanes at real pixels. A fixed source column sits beside the horizontal scroller. Each source's outgoing links fan four pixels apart. Nodes stay in column order in the DOM.
- Filters retain positions and dim unmatched nodes and source links to 25 percent. Tradition includes borrowed and broke-from tags; Mine includes broke-from and own-idea tags.
- At compact widths the book shows one leaf and a Tags toggle. On phones the actual hint, Add page and save status move into the book. The four thumbnail boxes scroll vertically at full width with tools above them.

#### Saving and privacy
The sole book key is `curio-sketchbook-journal`. Writes are debounced one second after edits, with an immediate save on leaving My book or the page. Storage access is guarded. A failed write keeps the full in-memory book and displays the specified warning. Clear book asks once and removes the key. No names, network requests, exports or device-transfer features.

The maximum source estimate omitted base64 expansion. Forty-eight 40 KB drawings take about 2.56 MB as base64 before the journal metadata, rather than 1.9 MB. Actual complexity determines size, so the failure message remains necessary.

#### Decisions and open questions
- Retain the specified clear-teacher bank voice, Iapetus, pending an owner-side bank addition. The spec leans toward borrowing it for this build. Adding a grown-up voice and changing the shared bank are outside the permitted folders. No recording was made; browser speech supplies runtime narration.
- Cold review restored the spec's skull vanitas and bottle-skull thumbnail. Current people rules do not prohibit conventional skull symbols. No living figure is depicted; people flags remain false.
- Added one compact how-to line, openTags, so the narration names the visible Tags control before the hidden tag editor. The other fixed lines follow the spec. The queue is `Curio.voice` with mode scope, valid checks and visible-control requirements.
- A Plan becomes available after any Thumbnails page exists. Revision is allowed without one, as listed in Add page, and explicitly shows that no earlier thumbnails exist.
- Existing bar bundles were opened without rebundling them, because rebundling would write outside the two authorized folders. Beat Lab has no handoff or refine file here. Storyboard Studio's source and handoff supplied the built-neighbor context; no refine file was present.
- The report is written only at the end, following the user's explicit instruction to stop as soon as it is written.

#### Art made
Fifteen finished WebP images, each below 80 KB and with long side 1000 pixels. Prompts, house style and provenance are in `art/prompts.json`; selected PNGs are under `art/raw/`. All were made with the built-in image tool and inspected at final size. The monarch painting was redrawn once: the first version's snowy alpine peaks were misleading, so the final shows a close oyamel fir-forest interior. WPA bands are blank. No people or human body parts appear.

#### Checks and evidence
Everything is under `_scratch/sketchbook-process-journal/`.
- `prepare.py`, `numbers.json`: independent tag counts, exact palette contrast, storage accounting and Fahrenheit interval conversions. Source dates and measured estimates are inputs, not invented computations.
- `student_check.py`, `student/results.json`: 40 checks, including all sample node destinations, actual jittered mouse strokes, pen and touch input, 20-step Undo, saved image size, reload, tags, old-source retention, plan constraints, storage failure and the 12-page map. All passed with no console errors.
- `full/`: one full STANDARDS size pass plus the sample Plan, compact map, My book and grayscale. Every frame was opened. Targeted phone frames were repeated only after the overlapping canvas layout was corrected.
- `phone/`: 375 by 812 through the required host. Actual hint and save status are visible in the working book, with tools above the full-width pad. No horizontal document scroll. The phone runner removes its temporary host and closes its server.
- `keyboard/`: an entirely keyboard-driven issue, tradition, thumbnail, source tag, map node, cancellation, deletion and clear workflow. The first test attempt needed the driver's Enter key event corrected to include its character; no tool change was needed for that harness issue.
- `voice-pace.json`: five held page adds near two seconds apart, repeated broke-from events, Read and a mode change.
- `bar/`: opened Beat Lab and Snowy Mail Route. `comparison.png` places this tool beside Beat Lab.
- `audit/`: the one final mechanical audit. Its outcome and all lead dispositions belong in the final report.

#### Engine changes wanted
None. Kit, scripts, docs, other tools and the voice bank were not changed.

#### Review cautions
This is a plain pencil journal. A selected palette describes the planned work; it does not recolor strokes. Tags are optional and can represent a student's argument rather than a scored answer.

The complete 12-page map requires scrolling. On compact screens its lanes also require vertical scrolling; the count and hint stay outside that scroller. The fixed source list scrolls vertically with the map, while remaining stationary during horizontal scrolling.

Plan fields and long tag editors scroll inside their paper leaf. Drawing tools stay sticky on that leaf. A phone exposes one thumbnail at a time in the vertical drawing strip. These are deliberate space tradeoffs, not a claim that every secondary control fits at once.

Source dates and environmental claims follow the supplied spec. No outside fact-checking or recorded-voice listening was performed in this build.

#### Final audit and targeted build corrections
The one audit completed with 45 leads and 54 PNGs. All 54 frames were viewed in seven QA sheets; affected compact states were also opened individually. No console errors, infinite animations, resize exceptions or controls left disabled were reported. Every lead is answered in the report and `_scratch/sketchbook-process-journal/audit-responses.md`.

After the audited bundle, choice buttons moved outside their scrolling details, modal actions gained a reserved row, compact drawing rows gained a useful minimum size, and the short-landscape My book panel reclaimed space from its introduction. Navigation buttons and the page picker keep their DOM identity; mode changes move focus to the visible mode button. Plan fields now have explicit accessible names. Map sources and nodes share vertical scrolling, and gray old-source nodes still dim to exactly 25 percent when filtered out. Clear cancels pending saves, and an empty book keeps the storage key removed. Reconfirming a choice in a full book no longer names disabled Add page.

The final targeted checks passed with zero console errors. Stable navigation, mode focus, accessible field names, map alignment, old-tag opacity, delayed clearing and twelve-page source fixation have saved JSON results. The keyboard journey passed eleven checks. Six final phone frames cover the affected choices, study, plan, node dialog and the right end of the twelve-page map. The full audit was not rerun.

Queued how-to lines also check the exact waiting moment: opening an issue/tradition card invalidates its earlier welcome, selecting an aspect invalidates tagHow, and showing Tags invalidates openTags. The final held-tap voice pace was repeated after these validity checks changed.

The authored phone audit-state entries originally used `375` rather than `375x812`, so six optional authored phone states were skipped. Default, both automatic modes, the sample plan and sample node dialog still received the audit's phone checks. The configuration is corrected for the cold review; targeted phone checks cover the omitted editing layouts.

Remaining mechanical leads are the expected scrolling map topology, duplicate phone panel actions below the fold, less frequent phone Delete/Clear actions below the book, the confirmation dialog's deliberate stale how-to drop, and the spec-mandated welcome that becomes stale on first navigation. Visible header modes provide the duplicate actions. These are disclosed limits, not a claim of a clean audit.

#### Cold review repairs, 2026-11-04
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

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
