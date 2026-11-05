# Codex report: sound-and-picture-book

## Built

Built the offline K-2, teacher-led Sound and Picture Book in S:/CurioClass-codex. Plan, Make, Play and Swap are functional. The class can create a three-page book, arrange painted pieces, choose synthesized sounds, play it, swap sounds or whole pages, undo ten swaps and save automatically on this device.

The package includes src.html, tool.draft.json with stage built, notes.md, voice/lines.json, audit-states.json, handoff.md, art/prompts.json, 23 finished paintings and the generated sound-and-picture-book.html. No commits or polish round. Writes stayed within this tool and its Scratch folder.

The report is written last because the user's stop-on-report instruction takes precedence over the brief's early-report instruction.

## Numbers check

- Contrast recomputed: white/brand 10.358:1, brand/paper 9.335:1, ink/paper 14.574:1, muted/paper 5.994:1. These match the spec's rounded values.
- Maximum background plus action bus gain is 0.20 + 0.40 = 0.60. This is exactly 0.60, rather than strictly below it, and remains below the 1.0 clipping limit.
- Snore: 2 x 1.6 = 3.2 seconds. Starting at 0.8 seconds makes its scheduled end 4.0 seconds, before the six-second Auto turn.
- Page units: 1000 / 625 = 1.6 = 16 / 10. Focused final Make checks measured ratios from 1.59992 to 1.60000 at all desktop sizes, before and after selection.
- Artwork: 6 + 4 x 3 + 5 = 23 images. Background and action inventories contain six and eight sounds.
- The Sources sentence about suggested chips already being on the named pages is too broad. Thunder is a new assignment; Crickets begins on page three. Both assignments were performed through Make and played on page two.
- Evidence: Scratch/numbers.json, auto-evidence.json, session-evidence.json and final-checks.log.

## Feel check

Best moment: swapping the cave's Snap with the campsite's Snore while leaving the scared raccoon and cave unchanged. The visible sound chips make the revision clear, and replay gives the class a specific new story to tell.

First flat moment: the initial dense Plan layout overlapped its own cards. Complete Who, Where and What happens trays now leave three readable illustrated pages in view. Sample book gives a large painted result on the first tap.

Second flat moment: compact selection controls covered the animal, and selecting could change the paper's proportions. Make now reserves editing space in taller layouts; short previews replace the bottom picture tray with selection controls. Empty paper or Escape restores the picture tray. The paper keeps 16:10, and the selected animal stays visible.

The 23 gouache-and-ink paintings, linen desk, layered paper edges, sound previews and page curl give the book its own finish. Cutout edges were rekeyed to remove a magenta fringe. No painted placeholders remain.

Opened snowy-mail-route and beat-lab as the bars. Scratch/compare.jpg places the book's Play frame beside snowy-mail-route. The book is not visually plainer. Existing bar bundles were used because rebundling them would violate the write boundary.

Played the complete sample through The end, swapped its action sounds and replayed. Also checked all four suggested changes, original planning input, piece movement, resizing and the four-piece limit. Browser audio was muted as required, so this is not a headphone listening review.

## Done when

1. PASS: Make and Play focus on a large page at 1366x768 and 680x425. Swap shows three illustrated pages and readable chips. The compact heading/button overlap was fixed and measured with a three-pixel gap.
2. PASS: Sample pages contain the specified places, raccoon poses, lantern and sounds. Snap/Snore, pages 1/3, Thunder on page 2 and Crickets on page 2 were performed and played.
3. FAIL, listening verification open: all six looping recipes and eight one-shots execute without console errors. Continuous buffers have crossfaded seams. Actions started approximately 0.803 to 0.816 seconds after their page in the sampled logs. Audible loop seams have not been listened to.
4. PASS: Real chip dragging moved only sounds. Page-number taps moved pictures with their sounds. Wrong-kind input retained the book and showed the required line. Ten undos restored the original sound order after twelve swaps.
5. PASS: Page changes and mode switches act immediately. Old audio schedules cancel, with buses faded and disconnected within 300 ms. Auto stopped at page three's ending and did not advance past it.
6. PASS: A saved book survived a fresh tab/reload. Blocked storage still allowed making and playing, with an honest visit-only status. New book offers both confirmation choices.
7. PASS for queue behavior: five sound assignments at two-second held-click pacing started all five event names with one how line. Play narration waits for the action to finish, and Read stops foreground sound. The requested gravel-ranger identity is metadata until recordings exist.
8. FAIL for exact layout: controls meet the 60-pixel target in checked states, and sound summaries and Next page remain visible without scrolling. Complete choice trays replace the permanently inline card rows and fourteen sound selectors. Action chips are readable pills rather than exact circles. These deviations are retained in handoff.md.
9. PASS: final calm frame reported zero running animations. Curl, bob, sway and decorative glimmer stop; timing remains unchanged.
10. PASS: no camera, microphone, upload, recording or application network API. Art and kit code are embedded in one file. No external runtime resources are referenced.

## Wave lessons

- PASS, Hint and voice: hints update immediately; Read follows the current page or modal. Curio.voice handles once-only how lines and Read priority. Current events replace stale help, with validity checks for cards, sounds, poses and suggestions.
- PASS, Focus and layout: no focus is taken on load. Sample retains focus; workspace mode navigation moves focus to its persistent mode button. Pointer dragging keeps its node. Some workspace contents rebuild after release with focus restored by ID; this is disclosed in the audit disposition.
- PASS, Sizes: all eight STANDARDS sizes were checked, including 375 through an iframe. The affected Make layouts, selected states and phone layouts received focused rechecks after repairs.
- PASS, No giveaways: this is a generative story builder with no hidden answer, score or answer-revealing meter.
- PASS, Honest numbers: no unexplained estimate or rating is presented. Gains, timing, aspect and contrast were recomputed.
- PASS, Standards: planning cards generate ideas, three pages organize them, swaps refine them, and playback combines pictures and sounds. No family engine is specified.
- PASS, Motion off: zero running animations in the final calm check; art remains visible.
- PASS, Short choices: complete trays show every option together, rather than hiding a short list in a scroll panel. The short sound hint fits inside the viewport.
- PASS, Resize mid-animation: the audit found no actual resize exceptions or locked controls. Its two piece-ID comparisons were false matches across fresh loads; the sample now has deterministic IDs.
- PASS, Late welcome: no welcomeAfter. First taps with their own lines skip the generic welcome. Play's instruction waits for its action. Repeated active tabs no longer cut their own welcome.
- PASS, Unknown as unknown: empty pages are cream paper with their page word, not an invented completed scene.
- PASS, One look and one meaning: background rectangles and action pills have icons and words; selected state also uses aria-pressed.
- PASS, Truthful badges: sound labels, storage status, selected poses and page numbers reflect the actual book.
- PASS, Hint changes back: closing or escaping a tray restores the main hint and hushes modal speech. Mode and page changes replace it immediately.
- PASS, No copied-answer shortcut: there is no diagnosis puzzle or answer matching. The class makes and revises its own choices.

## Audit leads

The one full audit completed in 24.03 minutes with 62 leads. Every lead is dispositioned in Scratch/audit-dispositions.md. Its 55 PNGs were inspected in fourteen contact sheets.

- Fixed empty-page label/folio collisions, the compact Swap heading overlap, Sample focus and workspace-to-Play focus.
- Fixed rapid active-tab welcome cuts, modal closing narration, stale ordinary help delaying current events, and the long sound-tray hint.
- Retained animal/lantern transparent-bound overlap as an intentional scene relationship; painted objects and their centers remain selectable. Selected pieces and their Size handles sit above neighbors. At maximum size 460, a real drag left the handle fully inside the page at 60 by 60 pixels.
- Modal coverage of inactive art and its background hint is intentional. Read uses the modal hint; the future audit fixture keeps that active hint.
- Resize-disabled piece leads compared timestamp IDs across different loads. Sample IDs are now 1 through 4; actual buttons were enabled and no resize exception occurred.
- Welcome-not-heard rows for Sample, New book and card trays are required first-tap own-line behavior. The Play instruction was recorded as spoken but classified as how, not welcome, because it waits for the action.
- The audit reported no small targets, horizontal scrolling, console exceptions, endless calm animation, control jumps or failed Enter-twice paths. Every five-click repetition row was clean.

No second full audit was run after repairs. Focused evidence is in final-checks.log, phone-final.log, postfix.log, voice-final.log, mode-voice.log and the piece/handle fixtures. The explicit phone-state filter was corrected from 375 to 375x812 for the next reviewer; separate shots cover those phone states.

## Frames looked at

Inspected all manual PNGs directly or in contact sheets: early-frames, full-frames, function-frames, supplement-frames, fix-frames, extra-frames, final-frames, final-check-frames, postfix-frames, voice-final-frames, mode-voice-frames, piece-scale-frames and handle-final-frames.

Coverage includes every mode and size, empty pages, the sample, sound trays, New book, The end, all suggested changes, selected pieces, real drags, a maximum Size handle, keyboard-only navigation, Sound off, Motion off and grayscale. All 55 audit frames and both bar frames were also inspected.

## Art made

23 original images made with the built-in image tool: six landscapes, twelve animal poses and five props. All are used. Full prompts and drawn_by codex are in art/prompts.json; originals are in art/raw. No people were generated.

Finished art: 1,100.72 KiB. Final bundle: 1,550.67 KiB, below 2 MB. No redraws were needed. Animal edges were rekeyed with despill and holes options, using only the free --rekey pipeline. Source has normal line breaks and a maximum line length of 158 characters.

## Art still to paint

None.

## Engine changes wanted

None. No kit files were changed.

## Left open

- Exact inline selectors and circular action-chip shapes differ from the spec, as described above and in handoff.md.
- No recorded narration was made, as required by Build. The gravel-ranger / Algenib manifest has 127 lines; browser speech is the current fallback.
- Headphone listening, environmental timbre and audible loop-seam review remain open.
- The full audit predates the focused repairs. Cold Build review is next; no polish round was started.
- Early phone wrapper batches emitted favicon 404s and the audit host logged connection resets when tabs closed. Final owned-host phone checks and focused file-based checks reported zero console errors. These were test-wrapper events, not bundled-tool requests.

All owned Chrome and server processes were closed. host.html is absent. No git commit was made.
