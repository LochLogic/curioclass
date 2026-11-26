# Gallery Critique: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: gallery-critique

#### Built

- Offline Gallery Critique for grades 9-12: Choose, four-round Panel and editable, printable Record.
- Three authentic museum paintings, three seats, 36 panel claims, eight evidence targets per painting and four judgment lenses.
- Own sentence builders, up to three own claims per round, challenges with replies, current-round undo and forward-only rounds.
- Kit theme-912, Motion, Sound and Curio.voice. No recordings, commits, branch operations, shared-file edits or polish round.
- Files and generated assets are in tools/gallery-critique/. Scratch holds all test scripts, profiles, frames and audit evidence.

#### Numbers check

- Scratch numbers.json independently recomputes three claims per round, one per seat, supported word totals 98/101/95 and Curator seeds 45/55/41.
- Longest sentence in those panel-only Curator seeds is 14 words, rather than the spec's stated 16. All remain within 25 words.
- Contrast: pink on panel 8.484:1; on section 8.039:1; on fallback wall 8.899:1; dark ink on pink 9.051:1.
- Browser checks covered every panel claim against every target, supported Judge lenses and wrong lenses.
- Additional arithmetic confirms one claim per seat/round, nonempty meanings, Judge support subsets and own-review upper bounds below 64 words.
- Live textarea checks: 101-word label warns; 26-word sentence warns; 151-word review warns. Print stays enabled.

#### Feel check

- Completed every painting/seat combination through Finish, plus a complete student path using only keyboard input.
- Best moment: refusing an unsupported claim, challenging its actual flaw, and seeing the speaker concede in words before moving on.
- Flattest first-build moment: the opening paintings overflowed their mounts and taps missed. Natural-image fitting restored a clear gallery wall.
- Second flat moment: dense own-claim controls squeezed the floor. Compact menus, receipts after pinning and explicit Next round focus restored the pace.
- Compared the finished Panel beside Beat Lab in Scratch feel-comparison.jpg. The large original, lit plaster, gilt frame and painted emblems hold up.
- The teaching changes each round: identify objects, analyze relationships, support readings, then argue through different criteria. No score or confetti.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

- Bundled and opened Snowy Mail Route and Beat Lab from copies in Scratch before building; neither tool folder was written.
- Final Choose and Panel at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 in an iframe host.
- Analyze, Interpret and Judge at compact, laptop and phone sizes; pinning, zoom, grayscale, Motion off, full Record and print styling.
- Functional, keyboard, held-click voice, live writing-limit and edited-text discard frames.
- Reviewed the audit's 47 frames in contact sheets, with critical compact/advanced frames also opened at full size.
- Scratch final-frames/, checks/, extra/, live-checks/, voice-frames/, audit/, keyboard-*.png and feel-comparison.jpg are the evidence.

#### Art made

- Five new images, 78.7 KiB: gc-wall, gc-critic, gc-curator, gc-artist and gc-visitor.
- Reused the three existing authentic CC0 museum originals, all with long side 1400 pixels. No museum image was generated or altered.
- Eight active WebP assets total 366.0 KiB; final bundle 605681 bytes (591.5 KiB), below 2 MB.
- Built-in imagegen used. Full prompts and drawn_by:codex are in art/prompts.json; originals in art/raw/ and final assets in art/.
- All WebP files including retained legacy portraits total 403.5 KiB.
- Inspected every processed asset. No redraw was needed. Existing legacy portraits remain unused and were not generated during this build.

#### Art still to paint

None for the active design. All newly generated pictures contain only places or objects.

#### Engine changes wanted

- kit/art-museum.js and docs/families/art-museum.md are absent. Used the existing Art Style Match adapter as a tool-local workaround.
- Add the shared frame, zoomTo, unzoom, pins, label, pair and dispose APIs. Add selectable pins with autoZoom:false and onPin.
- Exact requested changes and reasons are in handoff.md. No kit or family-document files were written.

#### Left open

- The shared art-museum engine and family document still need promotion from the local adapter.
- Long Record text and its editor scroll on short screens; Print, Back and New panel remain visible.
- The final audit dispositions include targeted repairs rather than a repeated full audit.
- Narration uses the browser voice fallback; the calm-professor manifest has no recordings because this build forbids recording.
- The supplied Gulf Stream visible-evidence reading and supplied support tables are retained; both open-question decisions are in handoff.md.
- Source is 1122 lines, maximum 151 characters. All test Chrome instances and servers are closed; ports 9970-9977 and 8775 are free; host.html is absent.
- Build only. Report written last to honor the user's explicit stop instruction.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: gallery-critique

#### Played

Grade 11 solo Critic, Rain, all four rounds to Finish before reading builder notes. Strong original paintings and satisfying concessions; the finished piece initially felt buried. Also checked projector layouts and all nine painting/seat combinations through programmatic UI actions.

#### Findings fixed

- Should fix, general, own pin: miss feedback named Challenge, unavailable for student claims. Added a specific revision instruction and event line.
- Should fix, general, Challenge: reasons covered the sentence being evaluated. A native keyboard-trapping dialog now repeats the sentence, with Escape and focus return.
- Should fix, general, sentence menus: the whole sentence stayed hidden during composition. Each menu change now shows it immediately in the hint.
- Should fix, general, voice inventory: fixed Read hints, panel statements and replies were absent. Added them to allLines and the manifest; their sets match (94 fixed texts or segments).
- Should fix, general, Record: the action toolbar covered the editor or its label at short sizes. Moved actions outside the scroll section and reserved their own height.
- Should fix, general, compact pinning: an evidence message overlapped disabled zoom. Hide zoom while pinning.
- Should fix, family:art-museum, compact artwork: the separate zoom row and tall label squeezed the painting. Reclaimed their height with zoom beside a two-row label, retaining every label fact.
- Polish, general, Finish: the student's earned editable piece was below the long transcript. Finish now reveals and focuses it; 680x425 retains the editor, counts and actions together.
- Polish, family:art-museum, emblems: narrow Artist badge and green cutout edges weakened the set. Redrew Artist, preserved its native alpha and rekeyed the other three emblems with despill.

#### Findings left

- No confirmed blocker or should fix remains after targeted repairs. The scope limitations below stay explicit.

#### Flattest moment left

Resolving three cards in each round still repeats the same mechanics. The round's task changes, but relation choices in Analyze remain a bounded support-table exercise, as specified.

#### Graphics

Inspected all eight active images and three unused legacy portraits. Preserved the authentic originals, gilt frames, spotlight wall and painted object set. All people assets are marked. One redraw, three cleaned cutouts. Active art 357.6 KiB; bundle 584.4 KiB (598466 bytes).
Built-in imagegen final: art/raw/gc-artist.png, processed to art/gc-artist.webp. Prompt is in art/prompts.json. Compared fresh screenshots of Scratch copies of Beat Lab and Snowy Mail Route; kept the gallery's richer museum setting.

#### Audit

One full run completed in 1377 seconds, within the 40-minute limit, Chrome 9951 and host 8755. All 39 leads are dispositioned in Scratch review-audit-disposition.md. Confirmed toolbar and pin-message overlaps were fixed; overlays, circular target boxes, transcript scrolling and numbered-spot grammar explain the other leads.
All 50 audit frames inspected. Resize, Motion off, control walk, five held clicks and quick taps completed without runtime errors or stuck controls. The audit precedes its targeted repairs; it was not rerun.
Independent checks: 940 assertions with no failures; exact supports/reasons/lenses and all nine work/seat finishes; real 101-word/26-word/151-word editor warnings; printing stays enabled.
Every STANDARDS size inspected, including 375-wide iframe; Motion off has zero infinite animations; grayscale, keyboard-only Describe-to-Analyze and black-on-white print styling checked.
Voice: five pinned events spoken five times; welcome at most once, skipped when stale; Read works with Sound off and mode changes clear it. No tool runtime errors. One favicon 404 belonged to the temporary drive host wrapper.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| pinned | event | 5 | 5 |
| welcomePanel, already stale in this run | how | 0 | 0 |
| Read with Sound off | read | 1 | 1 |

Targeted repairs: all 72 evidence centers clickable; ten Record views have clear toolbar boundaries and hittable actions. Challenge Read works with Sound off. Compact painting, pin message, Finish and print frames re-shot and inspected. Test ports closed and host.html removed.
Numbers: supported words 98/101/95; Curator seeds 45/55/41; maximum sentence 14 words, rather than the spec's 16. Contrast pink/panel 8.48, pink/section 8.04, dark/pink 9.05.

#### Left open

- Narration uses browser speech; recordings remain unavailable under the no-recording rule.
- The absent shared art-museum engine remains a documented local adapter. No kit changes or new interpretation topics added.
- Analyze relationships and interpretations use the supplied finite support tables, not unrestricted assessment of an argument.
- No classroom test or listening review of recordings was possible. No git commits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Gallery Critique build handoff

#### Cold review changes

- Challenge reasons now use a native modal dialog containing the original sentence. It traps focus, supports Escape,
  and returns focus to Challenge or Withdraw challenge. The card's delegated click handler still resolves reasons.
- Failed own pins have their own event line, pointing to Cancel and menu revision. Menu changes show the complete
  sentence immediately in the hint. The voice inventory now includes fixed Read hints, panel claims and replies.
- Finish scrolls the existing Record to the editable role product and focuses it without page scrolling. Opening
  Record during a panel still starts at the transcript. Compact textareas are 110 pixels tall so the payoff fits.
- The Artist emblem was redrawn with built-in imagegen and native transparency. Its manifest uses native_alpha:true
  and cutout:false to preserve its alpha during art.py --rekey. Other active object emblems now use despill:true.
- Audit states include the finished product and an own-pin miss. Review evidence is in Scratch with review prefixes.
- The final audit confirmed Record toolbar overlap. The toolbar is now outside the scrolling Record section, which
  reserves its own 64-pixel action area. Recheck these frames directly; the single full audit predates this repair.
- During pinning the disabled zoom button is hidden, leaving the evidence-status message clear in compact layouts.
- Short landscape Panels put zoom beside a compact two-row wall label. Removing its separate top row gives the
  artwork substantially more height without shrinking controls or omitting the artist, date or medium.
- The challenge dialog describes its quoted sentence to screen readers and includes Read claim, reusing V.read(),
  because native modal focus makes the header's Read control unavailable until the dialog closes.
- No shared engine, specification, other tool, or git history was changed.

Cold review verification: one full audit completed in 1377 seconds with 39 leads; all are dispositioned in Scratch.
Targeted post-repair checks pass all 72 evidence centers and ten Record views, dialog Read with Sound off,
compact art, Finish and print frames. The voice manifest matches 94 fixed texts or segments. All test ports are
closed and host.html is removed. The full audit was not repeated after its confirmed repairs.

Original build record follows. codex-report.md describes that earlier snapshot; codex-review.md records the cold review.

#### Structure

- src.html starts from the kit starter, adds theme-912 and the gallery-specific wall, frames, speech cards and record.
- content.json, loaded through the bundler's json token, holds the three work records, 36 claims, 21 image spots,
  element tables, meaning tables and judgment tables. A separate image-token map in src.html is necessary because
  bundle_tool.py substitutes art before it expands JSON. Do not move the three active art tokens into JSON alone.
- Curio.voice owns the narration queue. The tool owns the visible hint, and Read adds the currently selected card.
  Event lines are pinned, missPin, laterRound, wrongLens, struck, missChallenge and recordReady.
- state holds only in-memory work. It is never serialized. The kit may remember the shared Motion preference.
- The Gallery Critique-local Museum adapter is based on the existing sibling adapter in
  tools/art-style-match/lib/museum.min.js, read in full during the build. No shared file was changed.
- Normal painting taps zoom to the tapped point. While pinning, the whole image returns, the eight evidence targets
  appear, and only the active claim's Done/Cancel or the own-claim Done/Cancel can resolve the pin.
- Evidence buttons use a small repulsion layout when image details cluster. A leader and dot retain the exact
  evidence anchor when its numbered ring moves. Resize preserves the same buttons, focus and selected evidence.
- The Gulf Stream boat anchor is inside its visible hull at .58,.62. The Child's Bath floor anchor is on the
  visible floor at .94,.55. These builder-selected coordinates avoid misleading water or obstructed hand targets.
- Support is checked on Done. Selecting two spots succeeds when at least one is supported, as the spec says.
  For own Analyze claims, the element must belong to the chosen first spot and the second spot must differ.
- Rounds lock when advancing. Undo remains available in the current round. Finish locks Judge and opens the record.
- Small layouts page through floor claims. Menus collapse to receipts after an own claim; Add claim reopens them.
  Receipts expose the full sentence in their title and accessible name. Open Record to read all student sentences.
- Record reseeds while its text is unedited. Once edited, the text survives further panel visits. Only an edited
  product triggers the New panel discard confirmation. Printing is never blocked by length checks.

#### Open questions resolved

1. The Gulf Stream and race: retain the spec's visible-evidence claims. Do not add the optional curator claim or
   introduce a new historical interpretation. Teacher notes acknowledge the topic without asserting a new source claim.
2. Support tables: use the supplied tables. All listed objects and general regions were visible in the originals;
   no rows or claims were dropped. The tables are explicitly described as bounded teaching judgments in teacher notes.

#### Spec and implementation notes

- The missing family document and engine prevent a literal shared-engine import. The existing sibling's adapter
  provides the precedent for a local workaround. It is embedded in src.html to keep this folder within the allowed file list.
- No painted portraits are used. The three legacy portrait assets and prompts are retained untouched as required;
  all active speaker images are the newly generated object emblems. The five generated assets contain no people.
- Museum paintings were already present at long side 1400 pixels. They were inspected against every spot before building.
- The computed longest sentence among all panel-only Curator seed sentences is 14 words, rather than the spec's 16.
  Work totals are 98/101/95 supported words and 45/55/41 Curator seed words, matching the spec. No spec was edited.
- The exact product sentence and counts remain available on Record. Compact menus use accessible names and the
  current option text; the full own sentence appears in the hint while pinning.
- No voice recordings were made. The calm-professor voice manifest is ready; the kit falls back to browser speech.
- The user's stop instruction requires codex-report.md to be written last. Intermediate evidence stays in Scratch.

#### Engine changes wanted

- File: kit/art-museum.js (absent). Functions: frame, zoomTo, unzoom, pins, label, pair and dispose.
  Add the shared engine specified by art-style-match, promoting its existing adapter after review.
- Function: pins(frame, spots, opts). Add an explicit selectable mode with autoZoom:false, selection state and onPin,
  so evidence selection can preserve the whole picture and choose up to two targets. Current sibling pins always zooms.
- File: docs/families/art-museum.md (absent). Document those APIs and the 44-pixel pin behavior, including label targets.
  The Gallery Critique build did not create or edit either shared file.

#### Evidence

All temporary scripts, shots, contact sheets, Chrome profiles, arithmetic output, the bar-tool bundles and comparison
frames are in _scratch/gallery-critique/. The report names the final audit and any remaining limits.

#### Audit closure

The one full audit completed in 1186.7 seconds with 104 leads. Its Motion off, resize recovery, held-click runtime,
five-click repetition and quick-tap checks were clean. All 47 audit frames were inspected.

Repairs explicitly hide closed disclosure content and the content covered by the challenge chooser, give the museum
link a 44-pixel target, name the editable product, keep Print/Back/New panel in a fixed Record toolbar, retain focus
when the compact pager reaches its end, freeze the finished lens, and stabilize utility-button widths.

Additional native hit testing found overlapping Gulf Stream phone centers and a compact Child's Bath center.
Adaptive ring layout and the corrected evidence anchors now pass all 72 center checks across the three paintings
at compact, laptop and phone sizes. Resizing preserves the selected spot and its focus; resizing during zoom also passes.

Each original audit row is answered in Scratch audit-disposition.md. The full audit was not repeated after repairs.
Only affected frames and regression checks were rerun. The Record's long text deliberately scrolls; its action
toolbar stays in view. Requiring the entire product textarea in the initial compact transcript frame was removed
from audit keep regions because a complete transcript and its editor cannot occupy that short viewport together.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
