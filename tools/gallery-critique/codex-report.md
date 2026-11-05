# Codex report: gallery-critique

## Built

- Offline Gallery Critique for grades 9-12: Choose, four-round Panel and editable, printable Record.
- Three authentic museum paintings, three seats, 36 panel claims, eight evidence targets per painting and four judgment lenses.
- Own sentence builders, up to three own claims per round, challenges with replies, current-round undo and forward-only rounds.
- Kit theme-912, Motion, Sound and Curio.voice. No recordings, commits, branch operations, shared-file edits or polish round.
- Files and generated assets are in tools/gallery-critique/. Scratch holds all test scripts, profiles, frames and audit evidence.

## Numbers check

- Scratch numbers.json independently recomputes three claims per round, one per seat, supported word totals 98/101/95 and Curator seeds 45/55/41.
- Longest sentence in those panel-only Curator seeds is 14 words, rather than the spec's stated 16. All remain within 25 words.
- Contrast: pink on panel 8.484:1; on section 8.039:1; on fallback wall 8.899:1; dark ink on pink 9.051:1.
- Browser checks covered every panel claim against every target, supported Judge lenses and wrong lenses.
- Additional arithmetic confirms one claim per seat/round, nonempty meanings, Judge support subsets and own-review upper bounds below 64 words.
- Live textarea checks: 101-word label warns; 26-word sentence warns; 151-word review warns. Print stays enabled.

## Feel check

- Completed every painting/seat combination through Finish, plus a complete student path using only keyboard input.
- Best moment: refusing an unsupported claim, challenging its actual flaw, and seeing the speaker concede in words before moving on.
- Flattest first-build moment: the opening paintings overflowed their mounts and taps missed. Natural-image fitting restored a clear gallery wall.
- Second flat moment: dense own-claim controls squeezed the floor. Compact menus, receipts after pinning and explicit Next round focus restored the pace.
- Compared the finished Panel beside Beat Lab in Scratch feel-comparison.jpg. The large original, lit plaster, gilt frame and painted emblems hold up.
- The teaching changes each round: identify objects, analyze relationships, support readings, then argue through different criteria. No score or confetti.

## Done when

| Spec item | Result and evidence |
|---|---|
| 1. Exact panel evidence and challenge reasons | PASS. 999 functional assertions across all nine painting/seat sessions, including every target and wrong reasons. |
| 2. Wrong-round Pin refused | PASS. Functional checks and stagger test preserve state and show laterRound. |
| 3. Judge lens gates | PASS. Wrong lenses refuse Pin; own judgments use the supplied lens support tables. |
| 4. Editable role products and counts | PASS. All three products seed from the record; edits survive Back/Record; live boundary cases checked. |
| 5. Floor and own claim required | PASS. Next round remains disabled until both requirements hold; Finish opens Record. |
| 6. Painting is the focus | PASS. Reviewed laptop and 680x425 frames; all three originals are framed in Choose. |
| 7. Stagger can be skipped without swallowing action | PASS. Synchronous pointerdown plus clicked action reveals all cards and acts in the same frame. |
| 8. Voice queue and repetition | PASS. Held runs logged one Panel welcome, five pinned events and five struck events; stale miss events drop correctly. |
| 9. Required sizes and print | PASS. Reviewed every required size; fixed Record toolbar; black-on-white print views inspected. |
| 10. Eight images, no generated people, no saved work | PASS. All eight active assets inspected; only shared Motion preference can persist. |

## Wave lessons

| BUILD.md lesson | Check |
|---|---|
| Hint and voice | PASS. Immediate state-owned hints, kit queue, held clicks at two-second pace and keyboard Read path. |
| Focus and layout | PASS. No load focus; card controls remain stable; pin/cancel/undo return to visible controls. |
| Sizes | PASS. 44-pixel targets, corrected links and 72 passing native evidence-center checks. |
| No giveaways | PASS. No score, correctness badge or answer-revealing support overlay. Evidence names identify regions, not valid claims. |
| Honest numbers | PASS. Counts are exact word/sentence counts, with limits stated in words. No estimated meter. |
| Standards | PASS. Solo students describe/analyze, interpret and judge, then edit their own supported critique. |
| Motion off | PASS. Audit found nothing running forever; calm frames inspected. |
| Short choices stay visible | PASS. Compact floor uses Previous/Next; all three challenge reasons are visible together. |
| Resize mid-animation | PASS. Audit clean; final selected-pin and mid-zoom resize tests preserve state without errors. |
| Welcome never lands late after first-tap event | PASS. Curio.voice handles the first tap; welcome validity follows the screen. |
| Unknown stays unknown | PASS. No hidden factual clues are represented as known. Unsupported claims remain unresolved. |
| One look, one meaning | PASS. Written On the record and explicit challenged reasons distinguish outcomes without color alone. |
| Badge says what is true | PASS. Status follows validated support or the exact challenge reason; undo reopens the claim. |
| Hint changes back with state | PASS. Cancel, undo, round change, Record and Back set fresh hints immediately. |
| No answer by copying words | PASS. Students connect a spoken claim to visible picture evidence, then distinguish three kinds of flaw. |

## Audit leads

- The single full audit completed in 1186.7 seconds with 104 leads and 47 reviewed frames.
- Every original audit row has a numbered answer in Scratch audit-disposition.md.

| Original lead group | Count | Disposition |
|---|---:|---|
| Closed disclosure geometry | 39 | Fixed by explicitly hiding closed text. |
| Small museum links | 6 | Fixed; measured 44 pixels at all affected sizes. |
| Painting beneath evidence buttons | 7 | Intended overlay; background zoom control disabled during pinning. |
| Nearby evidence targets | 5 | Adaptive spacing with leaders; all 72 native target centers pass. |
| Challenge chooser over base card | 35 | Covered content hidden; reason focus and Cancel/Escape return fixed. |
| Unnamed product | 1 | Role-specific accessible name added. |
| Full editor required in initial short Record | 2 | Intentional scrolling transcript; corrected the overly strict keep region. |
| Record actions below or covered | 6 | Fixed toolbar; compact, laptop and phone measurements pass. |
| Compact pager focus | 3 | Focus moves to the visible claim when a pager endpoint disables. |

- Read skipping a welcome and Sound cutting it are the required kit behavior. Sound-related header movement was fixed.
- Motion off, resize recovery, runtime checks, repeated how lines and quick taps were clean.
- Re-ran affected checks only. The original audit remains the earlier snapshot; no second full audit was run.

## Frames looked at

- Bundled and opened Snowy Mail Route and Beat Lab from copies in Scratch before building; neither tool folder was written.
- Final Choose and Panel at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 in an iframe host.
- Analyze, Interpret and Judge at compact, laptop and phone sizes; pinning, zoom, grayscale, Motion off, full Record and print styling.
- Functional, keyboard, held-click voice, live writing-limit and edited-text discard frames.
- Reviewed the audit's 47 frames in contact sheets, with critical compact/advanced frames also opened at full size.
- Scratch final-frames/, checks/, extra/, live-checks/, voice-frames/, audit/, keyboard-*.png and feel-comparison.jpg are the evidence.

## Art made

- Five new images, 78.7 KiB: gc-wall, gc-critic, gc-curator, gc-artist and gc-visitor.
- Reused the three existing authentic CC0 museum originals, all with long side 1400 pixels. No museum image was generated or altered.
- Eight active WebP assets total 366.0 KiB; final bundle 605681 bytes (591.5 KiB), below 2 MB.
- Built-in imagegen used. Full prompts and drawn_by:codex are in art/prompts.json; originals in art/raw/ and final assets in art/.
- All WebP files including retained legacy portraits total 403.5 KiB.
- Inspected every processed asset. No redraw was needed. Existing legacy portraits remain unused and were not generated during this build.

## Art still to paint

None for the active design. All newly generated pictures contain only places or objects.

## Engine changes wanted

- kit/art-museum.js and docs/families/art-museum.md are absent. Used the existing Art Style Match adapter as a tool-local workaround.
- Add the shared frame, zoomTo, unzoom, pins, label, pair and dispose APIs. Add selectable pins with autoZoom:false and onPin.
- Exact requested changes and reasons are in handoff.md. No kit or family-document files were written.

## Left open

- The shared art-museum engine and family document still need promotion from the local adapter.
- Long Record text and its editor scroll on short screens; Print, Back and New panel remain visible.
- The final audit dispositions include targeted repairs rather than a repeated full audit.
- Narration uses the browser voice fallback; the calm-professor manifest has no recordings because this build forbids recording.
- The supplied Gulf Stream visible-evidence reading and supplied support tables are retained; both open-question decisions are in handoff.md.
- Source is 1122 lines, maximum 151 characters. All test Chrome instances and servers are closed; ports 9970-9977 and 8775 are free; host.html is absent.
- Build only. Report written last to honor the user's explicit stop instruction.
