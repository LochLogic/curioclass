# Sound and Picture Book handoff

## Build scope

Build only in S:/CurioClass-codex. No commits, branch changes or polish round. Writes are confined to this tool and _scratch/sound-and-picture-book. The explicit instruction to stop when codex-report.md is written takes precedence over the brief's early-report instruction, so the report is the final file written.

## Structure

src.html starts with the kit starter's metadata, kit CSS and script, palette, scene and narration hook. The tool has a responsive linen desk, paper book, large painted scenes and navy controls. ART embeds each asset once; repeated pictures reuse its data URI. All 23 paintings were generated with the built-in image tool, then copied to art/raw and finished by scripts/art.py with --rekey only. Full prompts and provenance are in art/prompts.json. Scratch/image-paths.json maps the original generated files.

The book has three page records. A record stores place, planned event, pieces, background and action. Pieces use 1000 by 625 units with stable IDs, position, size, pose and flip. The main animal is marked separately, so Who can replace it across pages while retaining its placement and pose. At capacity, a page without a marked main animal converts its first animal, or otherwise its first piece, to the new main animal.

Rendering uses real viewport dimensions. Only the paper preserves 16:10; the app is not a scaled fixed canvas. Plan and Swap use three simultaneous thumbnails. Make and Play fit one large page. The editing bar and resize handle are code drawn. Thumbnails are display art; the actual editable pieces are buttons with keyboard movement and Delete. Chip swapping supports pointer dragging and a two-tap keyboard path. Full-page swaps use two page-number taps. Undo retains the latest ten snapshots in memory.

## Sound and narration

Six background sound recipes and eight action recipes use Web Audio. Random noise samples are bounded to one. A background bus rises over 300 ms; stopGroup fades and disconnects within 300 ms. The action bus peaks at 0.4 or less. Continuous noise uses a crossfaded buffer seam. Wind's filter sweeps from 300 to 900 Hz with a 0.2 Hz LFO. Birds, crickets, ticks and crackles use cancellable schedules. Sound audition stops the previous sound.

Play schedules the action 800 ms after a page starts. The once-only Play instruction waits until the action has finished. Mode and page changes hush narration and cancel old audio schedules immediately. Read stops current environmental audio before speaking. The background is lowered to half gain while Curio.voice is playing. Auto retains six-second timing with Motion off and stops at The end.

voice/lines.json requests gravel-ranger, speaker Algenib. No audio was recorded, as required by this Build. Browser speech is the current narration fallback, so the exact gravel-ranger voice remains unfulfilled. __tool exposes state, setMode, sample, allLines, vlog, vq, audioLog, actionUntil, validBook and swapSounds for checks.

## Saving

Every edit writes one validated book to curio-spb-book inside try/catch. A blocked write changes the visible status to For this visit. Storage unavailable, and leaves editing functional. A modal protects New book. Settings use the kit's shared Motion preference. No camera, upload, recording, microphone or network code is present.

## Spec decisions and ambiguities

- There is no explicit open-question list in this spec.
- The prompt requires the image tool, so the art was made with OpenAI gpt-image instead of the spec's older local FLUX route. All six landscapes, twelve animal poses and five props are present. No people were generated.
- Plan's three full card rows, three sets of page slots, header and forward action cannot all fit the 425-pixel preview with 60-pixel targets and substantial art. Plan therefore uses complete Who, Where and What happens trays at every size. Selecting a card closes its tray, then the page button or picture receives it. With no card selected, a page button opens its three slots for clearing. This keeps every option accessible and prevents hidden short lists.
- Make uses complete Place, Characters, Things, Background and Action trays. The two assigned sound summaries stay visible beside the page, or below it on phones. Sound trays show all six or eight options with separate 60-pixel audition buttons. This differs from keeping all fourteen sound selectors permanently beside the page.
- Both assigned sound chips use shape plus icon plus word. Actions are pill-shaped circles stretched for readable words. Backgrounds are rectangular. Color is supplementary.
- In short landscape previews, a selected piece's editing controls replace the bottom picture tray. Tap empty paper or press Escape to return to Place, Characters and Things. The page stays in place, and its selected animal is not covered by the editing strip.
- Suggested assignments of Thunder and Crickets are made through Make on page two, then replayed. The other two suggestions use Swap directly.
- Maximum background plus action bus gain is 0.60, exactly, rather than strictly below 0.60 as the Sources wording says. The rest of the stated timing, aspect and contrast calculations match.
- The requested bar tools already had bundled files. Their existing bundles were opened without rebundling, which would have written outside this task's boundary. Frames and a side-by-side comparison are in Scratch. Neighbor line-safari and sound-elevator have no handoff.md or refine.md; weekend-drawing-share has a handoff but no refine.md. Available neighbor source and handoff were read.

## Checks and remaining review

Scratch contains number calculations, original image paths, inspected art sheet, one full all-size/mode run, raw drag and keyboard scenarios, auto-play and narration evidence, storage tests, focused fixes and the one final mechanical audit. Chrome ports 9990 through 9993 and host port 8795 were used, with muted Chrome. No other ports were selected.

The first phone host emitted two favicon 404s from drive.py's wrapper, not from the bundled tool. A data favicon was added to the temporary host for the targeted phone recheck, which reported zero errors. Temporary host.html is removed by the host wrapper.

The full size run was not repeated after the phone-only spacing and decorative Motion fixes. Targeted phone frames and a Motion-off frame verified those fixes. One Plan fixture initially hit a duplicate hidden ID; unused hidden card rows were removed, and a real held-click recheck placed Pond on the Middle page and spoke Middle: Pond.

A keyboard-only run used Tab, Enter and arrow keys to enter Make, enter Play, turn all three pages and reach The end. Both suggested assignments were checked with real held clicks: Thunder on page two and Crickets on page two. A Sound-off frame retained the chips and displayed the speaker slash.

During the final audit, all 55 captured PNGs were inspected in fourteen contact sheets. The empty thumbnails' large words were observed to clip on phones, so their type was reduced and their redundant folio hidden. Animal cutouts were also rekeyed with despill and holes options after a magenta fringe was spotted; the revised cave scene was inspected at laptop size. These narrow presentation fixes do not constitute a second polish round or a second full audit.

The original audit-state filter used 375 instead of 375x812 for three explicit modal/end states, excluding those phone variants in this audit. The filter is corrected for the next reviewer. Separate phone shots cover the sound tray, ending and New book confirmation. A later phone batch reused the audit's host on the assigned port and logged a wrapper favicon 404; its page states were still inspected. The bundled tool's own data favicon and file-based checks have no resource errors.

The sound recipes, cancellation and event timing were checked programmatically in muted Chrome. No claim of headphone listening or acoustic fidelity review is made. The next workflow is a cold Build review, not an automatic polish round.

## Audit outcome and focused repairs

The single audit completed with 62 leads. Scratch/audit-dispositions.md answers every lead by category, including each affected state and size. There were no small targets, horizontal scroll leads, console exceptions, control jumps, endless calm animations or failed Enter-twice paths. Every five-click repetition row was clean. Full audit was not repeated after repairs.

Focused checks fixed Sample book focus, mode-navigation focus, the short Swap heading overlap, empty-page labels, modal narration, and repeated active-tab welcomes. Repeated held taps 0.7 seconds apart now leave each allowed Plan, Make and Swap welcome spoken once without a cut. Five sound assignments at a two-second pace started all five names with one how line. The shortened sound hint fits the 425-pixel preview.

Make reserves its editing strip so selecting a piece does not change the paper's aspect or move the page under the pointer. Its child painting follows page units independently of its 60-pixel minimum hit target. The focused compact check measured a 60-pixel hit target and a 42.66-pixel painting against a 42.67-pixel unit calculation. A real drag still moved the animal and retained the 16:10 page. All desktop Make sizes were rechecked after this repair, and the affected phone modes and selected state were inspected again.

The audit's two resize-disabled leads compared timestamp-derived sample IDs across different loads. The sample now has deterministic IDs 1 through 4. User pieces retain generated stable IDs. Actual piece buttons were enabled, and no resize exception was found.

The exact requested inline selector layout and circular action-chip silhouette remain deviations: complete trays and readable pill-shaped action chips are used. These are explicitly retained for cold review, not called clean passes. Browser narration remains a fallback, and audio has not had a headphone listening review.

## Engine changes wanted

None. No kit files were changed.

## Final package

The final bundle is 1,550.67 KiB, including 1,100.72 KiB of finished art. Source lines are at most 158 characters. The voice manifest uses the standard bank and voice fields: gravel-ranger and Algenib. All owned Chrome/server listeners were closed, and host.html is absent.

The final compact resize check reached size 460 with a fully visible 60 by 60 pixel handle. Selected pieces sit above their neighbors, and the handle is kept within the page even near an edge. Its real drag completed without console errors.

One Sources sentence is broader than the sample data: Thunder is not already on page two, and Crickets begins on page three. Their suggestions are new assignments through Make. The source spec was left unchanged.
