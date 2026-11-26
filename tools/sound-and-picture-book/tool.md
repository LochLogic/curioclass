# Sound and Picture Book: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: sound-and-picture-book

#### Built

Built the offline K-2, teacher-led Sound and Picture Book in S:/CurioClass-codex. Plan, Make, Play and Swap are functional. The class can create a three-page book, arrange painted pieces, choose synthesized sounds, play it, swap sounds or whole pages, undo ten swaps and save automatically on this device.

The package includes src.html, tool.draft.json with stage built, notes.md, voice/lines.json, audit-states.json, handoff.md, art/prompts.json, 23 finished paintings and the generated sound-and-picture-book.html. No commits or polish round. Writes stayed within this tool and its Scratch folder.

The report is written last because the user's stop-on-report instruction takes precedence over the brief's early-report instruction.

#### Numbers check

- Contrast recomputed: white/brand 10.358:1, brand/paper 9.335:1, ink/paper 14.574:1, muted/paper 5.994:1. These match the spec's rounded values.
- Maximum background plus action bus gain is 0.20 + 0.40 = 0.60. This is exactly 0.60, rather than strictly below it, and remains below the 1.0 clipping limit.
- Snore: 2 x 1.6 = 3.2 seconds. Starting at 0.8 seconds makes its scheduled end 4.0 seconds, before the six-second Auto turn.
- Page units: 1000 / 625 = 1.6 = 16 / 10. Focused final Make checks measured ratios from 1.59992 to 1.60000 at all desktop sizes, before and after selection.
- Artwork: 6 + 4 x 3 + 5 = 23 images. Background and action inventories contain six and eight sounds.
- The Sources sentence about suggested chips already being on the named pages is too broad. Thunder is a new assignment; Crickets begins on page three. Both assignments were performed through Make and played on page two.
- Evidence: Scratch/numbers.json, auto-evidence.json, session-evidence.json and final-checks.log.

#### Feel check

Best moment: swapping the cave's Snap with the campsite's Snore while leaving the scared raccoon and cave unchanged. The visible sound chips make the revision clear, and replay gives the class a specific new story to tell.

First flat moment: the initial dense Plan layout overlapped its own cards. Complete Who, Where and What happens trays now leave three readable illustrated pages in view. Sample book gives a large painted result on the first tap.

Second flat moment: compact selection controls covered the animal, and selecting could change the paper's proportions. Make now reserves editing space in taller layouts; short previews replace the bottom picture tray with selection controls. Empty paper or Escape restores the picture tray. The paper keeps 16:10, and the selected animal stays visible.

The 23 gouache-and-ink paintings, linen desk, layered paper edges, sound previews and page curl give the book its own finish. Cutout edges were rekeyed to remove a magenta fringe. No painted placeholders remain.

Opened snowy-mail-route and beat-lab as the bars. Scratch/compare.jpg places the book's Play frame beside snowy-mail-route. The book is not visually plainer. Existing bar bundles were used because rebundling them would violate the write boundary.

Played the complete sample through The end, swapped its action sounds and replayed. Also checked all four suggested changes, original planning input, piece movement, resizing and the four-piece limit. Browser audio was muted as required, so this is not a headphone listening review.

#### Done when

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

#### Wave lessons

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

#### Audit leads

The one full audit completed in 24.03 minutes with 62 leads. Every lead is dispositioned in Scratch/audit-dispositions.md. Its 55 PNGs were inspected in fourteen contact sheets.

- Fixed empty-page label/folio collisions, the compact Swap heading overlap, Sample focus and workspace-to-Play focus.
- Fixed rapid active-tab welcome cuts, modal closing narration, stale ordinary help delaying current events, and the long sound-tray hint.
- Retained animal/lantern transparent-bound overlap as an intentional scene relationship; painted objects and their centers remain selectable. Selected pieces and their Size handles sit above neighbors. At maximum size 460, a real drag left the handle fully inside the page at 60 by 60 pixels.
- Modal coverage of inactive art and its background hint is intentional. Read uses the modal hint; the future audit fixture keeps that active hint.
- Resize-disabled piece leads compared timestamp IDs across different loads. Sample IDs are now 1 through 4; actual buttons were enabled and no resize exception occurred.
- Welcome-not-heard rows for Sample, New book and card trays are required first-tap own-line behavior. The Play instruction was recorded as spoken but classified as how, not welcome, because it waits for the action.
- The audit reported no small targets, horizontal scrolling, console exceptions, endless calm animation, control jumps or failed Enter-twice paths. Every five-click repetition row was clean.

No second full audit was run after repairs. Focused evidence is in final-checks.log, phone-final.log, postfix.log, voice-final.log, mode-voice.log and the piece/handle fixtures. The explicit phone-state filter was corrected from 375 to 375x812 for the next reviewer; separate shots cover those phone states.

#### Frames looked at

Inspected all manual PNGs directly or in contact sheets: early-frames, full-frames, function-frames, supplement-frames, fix-frames, extra-frames, final-frames, final-check-frames, postfix-frames, voice-final-frames, mode-voice-frames, piece-scale-frames and handle-final-frames.

Coverage includes every mode and size, empty pages, the sample, sound trays, New book, The end, all suggested changes, selected pieces, real drags, a maximum Size handle, keyboard-only navigation, Sound off, Motion off and grayscale. All 55 audit frames and both bar frames were also inspected.

#### Art made

23 original images made with the built-in image tool: six landscapes, twelve animal poses and five props. All are used. Full prompts and drawn_by codex are in art/prompts.json; originals are in art/raw. No people were generated.

Finished art: 1,100.72 KiB. Final bundle: 1,550.67 KiB, below 2 MB. No redraws were needed. Animal edges were rekeyed with despill and holes options, using only the free --rekey pipeline. Source has normal line breaks and a maximum line length of 158 characters.

#### Art still to paint

None.

#### Engine changes wanted

None. No kit files were changed.

#### Left open

- Exact inline selectors and circular action-chip shapes differ from the spec, as described above and in handoff.md.
- No recorded narration was made, as required by Build. The gravel-ranger / Algenib manifest has 127 lines; browser speech is the current fallback.
- Headphone listening, environmental timbre and audible loop-seam review remain open.
- The full audit predates the focused repairs. Cold Build review is next; no polish round was started.
- Early phone wrapper batches emitted favicon 404s and the audit host logged connection resets when tabs closed. Final owned-host phone checks and focused file-based checks reported zero console errors. These were test-wrapper events, not bundled-tool requests.

All owned Chrome and server processes were closed. host.html is absent. No git commit was made.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: sound-and-picture-book

#### Played

Cold K-2 solo/classroom walk: Plan, Sample book, Make, all three Play pages, The end, sound swap and replay before opening the builder's report, handoff, notes or source. Warm, inviting paintings; the sound exchange needed a clearer physical payoff. Also walked original planning with held 120 ms clicks at a two-second pace, and tested it as a projected class activity.

#### Findings fixed

- **Blocker, general, Undo:** an old full-book snapshot erased a later picture edit. Actual picture/sound edits now clear earlier swap history with a visible explanation; selecting an unchanged piece retains Undo. Pond survives the original Cave/edit/Undo reproduction; ten consecutive swaps still undo.
- **Blocker, general, capacity:** Who could turn the first prop into an animal when a page held four things. It now leaves the complete book unchanged and asks for room in Make. The four-prop path passed at 680x425, 1366x768 and 375x812.
- **Should fix, general, Make voice:** Plan's character placement caused Make's introduction to be dropped. The introduction now fits the actual page and is heard on the normal planning path.
- **Should fix, general, Read:** a native modal blocked the header Read button. Every choice tray now has its own Read using the same queue. It stops an audition, reads current instructions, and retains Read priority over a new sound assignment.
- **Should fix, general, voice catalog:** fixed Read hints and finite card/sound variants were absent from allLines. Synchronized the 224-line manifest; audition hints also stop claiming Listening when the audition ends.
- **Should fix, general, false changes:** equal sounds and identical pages claimed Swapped and consumed Undo. Both now explain the unchanged result without a history entry. Chip/page selection clears the other selection, and Sample clears pending cards and old change text.
- **Should fix, general, Plan:** compact pages hid the assigned What happens cards, and a modal blocked card drag targets. Page buttons now retain the event icon/word; dragging exposes the pages. Real tap and native drag are rechecked.
- **Should fix, general, suggestions:** custom books were told to swap absent Snap/Snore chips. Suggestions now fit current contents, name the controls to use, and are narrated when shown.
- **Should fix, general, editing:** keyboard limits differed from dragging, and edge/resize positions cropped paintings. Shared limits retain whole pieces. Accessible pose labels now change with the painting.
- **Should fix, general, audit frames/voice:** a Size handle covered the animal's face on compact and phone screens; it now finds nearby clear space while staying 60 x 60 and inside the paper. Plan-slot dialogs were silent; their instructions now speak once. Selection also speaks its matching editing help once.
- **Polish, general, Play/Craft:** chips and pages now travel to their exchanged positions for 420 ms, with immediate state changes and no control lock. Motion off skips/cancels the exchange.
- **Polish, general, art:** redrew the scared turtle to match the happy turtle's warm shell, spotted skin and rounded limbs. Kept the other 22 paintings, paper layers, linen, page curl and scene layout.

#### Findings left

No additional confirmed implementation blocker or should-fix remains from this pass. Exact inline card/sound layouts and circular action chips remain the documented spec conflict described under Left open; recorded-voice identity and audible seam verification are still open.

#### Break it

- No score, meter, quiz, best score or reflection gate exists. The end is a navigation invitation, with no mastery claim. Blank playback is explicitly allowed by the spec.
- Tried bypassing disabled Make it through mode tabs and racing empty pages to The end: creative blank playback works as specified, with no badge or learning credit. The proper three-place path enables Make it.
- Tried a fifth piece: four remain and the limit is explained. The same check protects every Characters/Things choice.
- Tried Who on a page already holding four props: all three pages remain byte-for-byte unchanged, with an actionable explanation. This closes the alternative route around the capacity check without deleting a prop.
- Tried wrong-kind sound swaps by taps and a real jittered drag: book unchanged, no Undo entry, explanatory feedback.
- Tried identical sounds and identical blank pages: no Swapped praise and no Undo entry after the fix.
- Tried rapid repeated swaps and ten undos after twelve changes: history exhausts cleanly and the tested sound order is restored. Tried switching to Make and editing before Undo: new work survives and old Undo is disabled with an explanation.
- Tried loading Sample while a different Who card was pending: the sample remains Raccoon and the pending card clears.
- Tried blocked storage: editing remains usable with a visit-only status. Persistence and both New book choices are checked in the final targeted batch.
- Choosing every sound is artistic exploration, with no hidden answer or score to farm. All six backgrounds and eight actions are exercised separately; sound-only swaps retain the pictures, while whole-page swaps retain pictures and their sounds together.

#### Voice walk

Default Sound on; Who > Fox > Beginning > Where/Forest/Beginning > Where/Cave/Middle > Where/Campsite/End > Make it > Background/Rain/Close > Action/Splash/Close > Play book > Next > Next > Next > Swap. Held clicks, two-second gaps. Repeated after the audit repairs. Evidence: Scratch/main-post-audit.json.

Spoken in order: card instruction, Fox, Where instruction, Forest card, Beginning: Forest path, Cave card, Middle: Cave, Campsite card, End: Campsite, That's a plan, prepared-picture Make instruction, sound-tray instruction, Rain, Splash, Play instruction, The end, Swap instruction, applicable Thunder suggestion. No dropped how-to in the final walk. First-tap Plan welcome is legitimately skipped for the card tray's own instruction; its premise remains in the initial hint and Read.

| Line | Kind | Expected starts | Observed starts |
|---|---|---:|---:|
| Card-tray instruction, four openings | how | 1 | 1 |
| Make / Play / Swap introductions | how/welcome | 1 each | 1 each |
| Sound-tray instruction | how | 1 | 1 |
| Rain / Birds, five assignments | event | 3 / 2 | 3 / 2 |
| Plan-slot instruction, three openings | how | 1 | 1 |
| Editing instruction, five selections | how | 1 | 1 |

Side path: Make > Action > Snore audition > tray Read > Thunder assignment. Read starts, stops Snore, and Thunder waits until Read finishes. Header Read also works with Sound off. All logged spoken/read texts match the manifest. No queued mode how-to failed to start on the tested main path. Later actions can cut a started introduction; its full instruction stays in the hint/Read. Chrome is muted as required; this establishes queue/timing behavior, not a listening-quality verdict.

#### Facts checked

- Planning ideas, organizing a model, revising content, and combining media: [NCAS Media Arts at a Glance, K-2 Cr1, Cr2, Cr3, Pr4](https://www.nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf). These are practiced in Plan, page order, Make/Swap revision, and playback respectively. This tool teaches selected practices, not every performance standard in each family.
- Sound can affect a picture's perceived meaning: Michel Chion, [Audio-Vision, Projections of Sound on Image](https://pzacad.pitzer.edu/~mma/teaching/ms52/readings/audio-vision3-13.pdf), added value. The scan identifies Columbia University Press, 1994, translated/edited by Claudia Gorbman. No universal emotional response is claimed.
- Beginning/middle/end: the three-part design of this book, not a claim that every good story follows that order. Corrected the welcome accordingly.
- Contrast, recomputed with [W3C WCAG 2.1 contrast/luminance definitions](https://www.w3.org/TR/WCAG21/#dfn-contrast-ratio): white/brand 10.358:1, brand/paper 9.335:1, ink/paper 14.574:1, muted/paper 5.994:1. All meet AA for normal text.
- Spec timing/counts independently recomputed: 1000/625 = 16/10; 6 + 12 + 5 = 23 assets; Snore 2 x 1.6 = 3.2 s, beginning at .8 s ends at 4.0 s before a 6 s Auto turn. The .20 + .40 = .60 calculation is a bus-gain sum, not a measured waveform guarantee. Evidence: Scratch/review-numbers.json and audio logs.
- Offline/save/sound provenance: source inspection finds embedded original illustrations, synthesized Web Audio, localStorage in try/catch, and no fetch, socket, upload, camera, microphone or external runtime URL. The sample's named pieces, poses and sounds were checked against spec Content. No biology, health, safety, legal or financial lesson is presented.

#### Sensitivity

None: an invented animal story with unnamed woodland settings; no people, cultures, religion, Indigenous content, hard history or human-body teaching. All 23 assets are marked people:false. The campground belongs to the fictional animal story and does not require a missing human cast.

#### Flattest moment left

Planning several cards still takes repeated tray openings. The complete trays preserve large targets and all choices; Sample book remains a vivid first-tap entry. The weaker swap payoff was lifted without reducing the art or play.

#### Graphics

Inspected all six backdrops at 1000 x 625, all twelve animal poses and five props, cutout edges, actual Make/Play/Swap frames, Motion off and grayscale. One style, no placeholders or people. Redraw: art/raw/turtle-scared.png > art/turtle-scared.webp, built-in imagegen with turtle-happy reference, finished through art.py --rekey only; full prompt/provenance in art/prompts.json. Bundle 1557.43 KiB; finished art 1099.28 KiB. Opened both snowy-mail-route and beat-lab bar frames; comparison in Scratch/review-bar-comparison.png. Kept the book's rich finish.

#### Audit

The one full audit completed within 40 minutes: 33 reported leads, 68 inspected PNGs, all eight STANDARDS sizes, all modes, populated/selected/end/dialog/extreme states. Chrome 9961, host 8765; targeted checks used 9960. No small targets, horizontal scroll, application exceptions, unintended control shifts, failed Enter-twice paths, repeated how-to faults, quick-tap faults or resize-stress failures. Motion off had no infinite animation.

Disposition: transparent animal/lantern hit-box overlap and native-modal coverage of inactive art are intentional. Play's actual how-to is classified as how rather than welcome; Sample, New book and card trays use their own first-tap lines under BASELINE 16. The three genuinely silent page-slot paths and the obscuring Size handle were fixed afterward. The original audit is preserved; targeted frames at 680x425, 1366x768 and 375x812 verify the repairs. Real resizing reached 460; keyboard resizing reached 80 and 460. Main voice path repeated, with no unspoken queued how-to. The final Who guard also received a separate three-size check. No second full audit. Detailed disposition: Scratch/review-audit-disposition.md; measurements: Scratch/review-postfix-measurements.md.

Wave lessons checked: current hint/Read, first-tap timing, focus retention, all-size targets/fold, full short choice sets, calm timing, resize during actions, unknown empty pages, distinct chip meanings, truthful labels and restored hints. Hidden-answer/giveaway/copied-answer and misleading-estimate cases are inapplicable: no assessment or estimate exists. Standards map to actual planning, arranging, revising and playback activities.

An early reload-inside-evaluation fixture failed and was retried successfully with a state-reset fixture. Final drive batches reported zero application console errors. The temporary phone host emitted connection-reset messages when tabs closed; this was host cleanup, not a bundled-tool request or browser exception. All owned browser/server ports were verified closed; tools/sound-and-picture-book/host.html is absent.

#### Left open

- Complete choice trays and pill-shaped action chips remain intentional deviations from exact inline selectors/circles. The 60 px K-2 targets, complete short choice sets, substantial picture and 425 px preview cannot all support fourteen permanently inline sound choices. STANDARDS sizing/readability wins; no kit or spec was changed.
- Recorded Algenib/gravel-ranger clips are absent. Browser narration remains the fallback because CODEX-BUILD.md forbids recording audio in this work. A production voice pass and headphone loop-seam/timbre listening remain open; muted automation cannot honestly certify them.
- No questions were asked in the unattended session. Kept the spec's defaults, existing compact-layout compromise and six-second timing. No git commits. Writes confined to this tool and Scratch; the restarted session continued the same evidence and fix pass.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Sound and Picture Book handoff

#### Build scope

Build only in S:/CurioClass-codex. No commits, branch changes or polish round. Writes are confined to this tool and _scratch/sound-and-picture-book. The explicit instruction to stop when codex-report.md is written takes precedence over the brief's early-report instruction, so the report is the final file written.

#### Structure

src.html starts with the kit starter's metadata, kit CSS and script, palette, scene and narration hook. The tool has a responsive linen desk, paper book, large painted scenes and navy controls. ART embeds each asset once; repeated pictures reuse its data URI. All 23 paintings were generated with the built-in image tool, then copied to art/raw and finished by scripts/art.py with --rekey only. Full prompts and provenance are in art/prompts.json. Scratch/image-paths.json maps the original generated files.

The book has three page records. A record stores place, planned event, pieces, background and action. Pieces use 1000 by 625 units with stable IDs, position, size, pose and flip. The main animal is marked separately, so Who can replace it across pages while retaining its placement and pose. At capacity, a page without a marked main animal reuses an existing animal. If its four pieces are all things, Who leaves the whole book unchanged and asks for room in Make.

Rendering uses real viewport dimensions. Only the paper preserves 16:10; the app is not a scaled fixed canvas. Plan and Swap use three simultaneous thumbnails. Make and Play fit one large page. The editing bar and resize handle are code drawn. Thumbnails are display art; the actual editable pieces are buttons with keyboard movement and Delete. Chip swapping supports pointer dragging and a two-tap keyboard path. Full-page swaps use two page-number taps. Undo retains the latest ten snapshots in memory.

#### Sound and narration

Six background sound recipes and eight action recipes use Web Audio. Random noise samples are bounded to one. A background bus rises over 300 ms; stopGroup fades and disconnects within 300 ms. The action bus peaks at 0.4 or less. Continuous noise uses a crossfaded buffer seam. Wind's filter sweeps from 300 to 900 Hz with a 0.2 Hz LFO. Birds, crickets, ticks and crackles use cancellable schedules. Sound audition stops the previous sound.

Play schedules the action 800 ms after a page starts. The once-only Play instruction waits until the action has finished. Mode and page changes hush narration and cancel old audio schedules immediately. Read stops current environmental audio before speaking. The background is lowered to half gain while Curio.voice is playing. Auto retains six-second timing with Motion off and stops at The end.

voice/lines.json requests gravel-ranger, speaker Algenib. No audio was recorded, as required by this Build. Browser speech is the current narration fallback, so the exact gravel-ranger voice remains unfulfilled. __tool exposes state, setMode, sample, allLines, vlog, vq, audioLog, actionUntil, validBook and swapSounds for checks.

#### Saving

Every edit writes one validated book to curio-spb-book inside try/catch. A blocked write changes the visible status to For this visit. Storage unavailable, and leaves editing functional. A modal protects New book. Settings use the kit's shared Motion preference. No camera, upload, recording, microphone or network code is present.

#### Spec decisions and ambiguities

- There is no explicit open-question list in this spec.
- The prompt requires the image tool, so the art was made with OpenAI gpt-image instead of the spec's older local FLUX route. All six landscapes, twelve animal poses and five props are present. No people were generated.
- Plan's three full card rows, three sets of page slots, header and forward action cannot all fit the 425-pixel preview with 60-pixel targets and substantial art. Plan therefore uses complete Who, Where and What happens trays at every size. Selecting a card closes its tray, then the page button or picture receives it. With no card selected, a page button opens its three slots for clearing. This keeps every option accessible and prevents hidden short lists.
- Make uses complete Place, Characters, Things, Background and Action trays. The two assigned sound summaries stay visible beside the page, or below it on phones. Sound trays show all six or eight options with separate 60-pixel audition buttons. This differs from keeping all fourteen sound selectors permanently beside the page.
- Both assigned sound chips use shape plus icon plus word. Actions are pill-shaped circles stretched for readable words. Backgrounds are rectangular. Color is supplementary.
- In short landscape previews, a selected piece's editing controls replace the bottom picture tray. Tap empty paper or press Escape to return to Place, Characters and Things. The page stays in place, and its selected animal is not covered by the editing strip.
- Suggested assignments of Thunder and Crickets are made through Make on page two, then replayed. The other two suggestions use Swap directly.
- Maximum background plus action bus gain is 0.60, exactly, rather than strictly below 0.60 as the Sources wording says. The rest of the stated timing, aspect and contrast calculations match.
- The requested bar tools already had bundled files. Their existing bundles were opened without rebundling, which would have written outside this task's boundary. Frames and a side-by-side comparison are in Scratch. Neighbor line-safari and sound-elevator have no handoff.md or refine.md; weekend-drawing-share has a handoff but no refine.md. Available neighbor source and handoff were read.

#### Checks and remaining review

Scratch contains number calculations, original image paths, inspected art sheet, one full all-size/mode run, raw drag and keyboard scenarios, auto-play and narration evidence, storage tests, focused fixes and the one final mechanical audit. Chrome ports 9990 through 9993 and host port 8795 were used, with muted Chrome. No other ports were selected.

The first phone host emitted two favicon 404s from drive.py's wrapper, not from the bundled tool. A data favicon was added to the temporary host for the targeted phone recheck, which reported zero errors. Temporary host.html is removed by the host wrapper.

The full size run was not repeated after the phone-only spacing and decorative Motion fixes. Targeted phone frames and a Motion-off frame verified those fixes. One Plan fixture initially hit a duplicate hidden ID; unused hidden card rows were removed, and a real held-click recheck placed Pond on the Middle page and spoke Middle: Pond.

A keyboard-only run used Tab, Enter and arrow keys to enter Make, enter Play, turn all three pages and reach The end. Both suggested assignments were checked with real held clicks: Thunder on page two and Crickets on page two. A Sound-off frame retained the chips and displayed the speaker slash.

During the final audit, all 55 captured PNGs were inspected in fourteen contact sheets. The empty thumbnails' large words were observed to clip on phones, so their type was reduced and their redundant folio hidden. Animal cutouts were also rekeyed with despill and holes options after a magenta fringe was spotted; the revised cave scene was inspected at laptop size. These narrow presentation fixes do not constitute a second polish round or a second full audit.

The original audit-state filter used 375 instead of 375x812 for three explicit modal/end states, excluding those phone variants in this audit. The filter is corrected for the next reviewer. Separate phone shots cover the sound tray, ending and New book confirmation. A later phone batch reused the audit's host on the assigned port and logged a wrapper favicon 404; its page states were still inspected. The bundled tool's own data favicon and file-based checks have no resource errors.

The sound recipes, cancellation and event timing were checked programmatically in muted Chrome. No claim of headphone listening or acoustic fidelity review is made. The next workflow is a cold Build review, not an automatic polish round.

#### Audit outcome and focused repairs

The single audit completed with 62 leads. Scratch/audit-dispositions.md answers every lead by category, including each affected state and size. There were no small targets, horizontal scroll leads, console exceptions, control jumps, endless calm animations or failed Enter-twice paths. Every five-click repetition row was clean. Full audit was not repeated after repairs.

Focused checks fixed Sample book focus, mode-navigation focus, the short Swap heading overlap, empty-page labels, modal narration, and repeated active-tab welcomes. Repeated held taps 0.7 seconds apart now leave each allowed Plan, Make and Swap welcome spoken once without a cut. Five sound assignments at a two-second pace started all five names with one how line. The shortened sound hint fits the 425-pixel preview.

Make reserves its editing strip so selecting a piece does not change the paper's aspect or move the page under the pointer. Its child painting follows page units independently of its 60-pixel minimum hit target. The focused compact check measured a 60-pixel hit target and a 42.66-pixel painting against a 42.67-pixel unit calculation. A real drag still moved the animal and retained the 16:10 page. All desktop Make sizes were rechecked after this repair, and the affected phone modes and selected state were inspected again.

The audit's two resize-disabled leads compared timestamp-derived sample IDs across different loads. The sample now has deterministic IDs 1 through 4. User pieces retain generated stable IDs. Actual piece buttons were enabled, and no resize exception was found.

The exact requested inline selector layout and circular action-chip silhouette remain deviations: complete trays and readable pill-shaped action chips are used. These are explicitly retained for cold review, not called clean passes. Browser narration remains a fallback, and audio has not had a headphone listening review.

#### Engine changes wanted

None. No kit files were changed.

#### Cold review, 2026-11-06

The cold review played the sample book and swaps before reading the builder files. Evidence and bounded command helpers are in Scratch with review- prefixes. The final findings are in codex-review.md.

Fixed data loss: save(swapOnly=false) clears the swap history after a subsequent picture or sound edit. lastSavedBook compares the serialized book, so selecting a piece without changing it retains Undo. Swaps and Undo call save(true). This prevents an old full-book snapshot from deleting newer work; up to ten consecutive swaps still undo. The Swap panel explains when edits cleared the history.

Make now chooses its spoken introduction from the actual page: empty, characters without a setting, or a planned picture ready for sound. It no longer drops the mode's how-to merely because Plan already placed the main character. Read and the visible hint use the same text. The welcome describes this book's three parts rather than making a universal claim about good stories.

Equal sound chips and identical pages do not create a false Swapped event or consume history. Starting a chip selection clears page selection and vice versa. Suggestions are filtered against the current book and narrated when shown. Sample resets pending cards and prior change text. Keyboard movement uses the same edge limits as dragging, and the piece's accessible pose label updates with its image.

The flat swap moment now shows the two chips or pages traveling to their exchanged positions for 420 ms. State changes immediately; no control is locked. Motion off skips or cancels this motion. The scared turtle was redrawn with the built-in image tool to match the happy turtle's shell, rounded limbs and spotted skin, then finished with art.py --rekey turtle-scared. Its full prompt and reference are in art/prompts.json. No other paintings were replaced.

Choice dialogs contain their own Read button: a native modal blocks the header Read control. It stops the audition first, then calls the same V.read helper. Audition hints return to the sound instructions when playback finishes. Read-only fixed hints and all finite card/sound variants are catalogued in allLines and the voice manifest. A shared clampPiece also keeps whole paintings inside the paper while moving or resizing, including old saved edge positions.

Plan's page buttons show each assigned What happens card as an icon and word, so the compact layout does not hide that part of the plan. Starting a native card drag closes its tray after Chrome captures the drag image, exposing the otherwise inert page drop targets. Tap-card-then-page remains available.

The single review audit completed within its 40-minute limit with 33 mechanical leads and 68 inspected frames. Scene-box overlaps and native-modal coverage are intentional. Play's introduction is classified as how, so its missing-welcome flag is a classification lead; Sample, New book and card trays use their own first-tap lines under BASELINE rule 16.

Two confirmed audit findings received targeted repairs afterward: page-slot dialogs now speak their instructions once; Size handles choose a nearby clear corner instead of covering the animal's face. The handle stays 60 by 60 and inside the paper, follows outward drag directions and retains its keyboard focus/limits. A press keeps the piece steady. Selection speaks its own editing help once, and editing stops any audition before narration. Checks at 680x425, 1366x768 and 375x812 measured no overlap with the selected piece, a real resize reached 460, and keyboard resizing reached both 80 and 460. The main voice walk was repeated. No second full audit was run.

The final capacity guard also prevents Who from silently replacing a prop on a page already holding four things. The existing four-piece limit now rejects that change without modifying any page. This was checked separately from the audit. Current narration manifest: 224 distinct lines; recordings remain absent. Final review evidence and limitations are recorded in codex-review.md.

No questions were asked during the unattended review. Existing complete choice trays and pill-shaped action chips were retained under the spec's target-size and readability priorities; exact inline layouts remain a documented spec conflict. Narration recordings were not generated because CODEX-BUILD.md forbids recording audio during this work. The bank identity remains a production-voice limitation.

#### Final package

The final bundle is 1,550.67 KiB, including 1,100.72 KiB of finished art. Source lines are at most 158 characters. The voice manifest uses the standard bank and voice fields: gravel-ranger and Algenib. All owned Chrome/server listeners were closed, and host.html is absent.

The final compact resize check reached size 460 with a fully visible 60 by 60 pixel handle. Selected pieces sit above their neighbors, and the handle is kept within the page even near an edge. Its real drag completed without console errors.

One Sources sentence is broader than the sample data: Thunder is not already on page two, and Crickets begins on page three. Their suggestions are new assignments through Make. The source spec was left unchanged.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
