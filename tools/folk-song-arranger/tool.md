# Folk Song Arranger: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: folk-song-arranger

#### Built

- Built a working draft of Arrange and Concert card, with seven instrument choices, nine section choices, three occasions,
  live playback, four checks, Solo, live tempo, reasons, Undo, per-occasion storage and confirmed Reset.
- Eleven original generated paintings are placed. The desk, grid, playhead, role blocks, check lights and labels are code.
- Final standalone bundle: 1,275,590 bytes, about 1,246 KB. Stage is built; status remains beta in tool.draft.json.
- No git commits, branch changes, shared-kit edits or polish round. Working folder was S:/CurioClass-codex.
- IMPORTANT: this is not release-ready content. The matching public-domain chorus printing was not verified. See Left open.
- Process exception: PyMuPDF was installed in the user Python environment during source inspection, exceeding the folder-only
  write constraint. That package was subsequently uninstalled. Generated-image default storage was used as the brief requires.

#### Numbers check

- PASS: Scratch preflight recomputed the supplied duration, balance and contrast examples before implementation.
- Default: 21 bars × 240 ÷ 72 = 70 seconds. One added A makes 29 bars and 96.6667 seconds.
- Lullaby, 40 bars: 141.1765 seconds at 68 BPM; 160 at 60; 126.3158 at 76.
- Dance, hypothetical 70 bars: 150 seconds at 112 BPM; 140 at 120; 131.25 at 128.
- Spec discrepancy: its two-bar dance Outro is not in the palette. That example becomes 69 bars with Hold or 72 with Last line twice.
- Walk, 72 bars: 180 seconds at 96 BPM; 187.8261 at 92; 172.8 at 100; 205.7143 at 84.
- Spec discrepancy: 74 bars at 100 BPM is 177.6 seconds. At least 75 bars, not 74, are needed for 180 seconds.
- 120 × 1.5 seconds = 180 seconds. The model implements the formula rather than the erroneous 74-bar suggestion.
- Balance: 12 ÷ 2 = 6, buried. Backing 5 against melody 4.5 passes the backing-at-most-twice-melody rule.
- Base contrast: ink/paper 13.51:1; muted/paper 5.65:1; white/brand 5.92:1.
- White/role contrast: Melody 5.46:1, Chords 6.74:1, Bass 8.63:1, Beat 5.06:1. Rest uses dark text.
- FAIL, source gate: the present F-major 32-beat chorus sketch is provisional, not a printing-verified transcription.
  Current A range is F4 to C5. Range is derived from events and must be rechecked after the source transcription changes.
- The inspected Wolford 1916 printing, p. 89, is a different 3/4 verse variant. It was not substituted for the specified chorus.
- CALLERLAB's cited 1994 guide gives 128 to 132 BPM, not the spec's 112 to 128. The implemented window remains a labeled
  Curio Class model. The source and discrepancy are recorded in notes.md.

#### Feel check

- Exercised a full 96.7-second Intro, A, A, Minor turn, Hold performance through natural completion, plus the edit-and-reason flow.
- Best moment: the last amber check becomes green, then the concert program preserves the student's own revision reason.
- Flattest moment 1: early blocks looked like large plain slabs. Added painted instruments, a detailed venue, wood and paper
  surfaces, shaded role blocks and restrained musical marks; enlarged the instrument paintings.
- Flattest moment 2: revision choices fell below the compact panel. Added a compact native reason editor with all six choices
  and the text field visible together. Both 680 and the phone iframe were inspected.
- Live role, dynamic, Solo and tempo dispatch were exercised. Current-note gains now react to dynamics, Solo and Sound.
- Chrome was muted throughout as required. This is a visual and interaction feel assessment, not a claim of an acoustic listening test.
- Compared with both bar tools. Their bundles were made in Scratch, preserving the write boundary for their tool folders.

![Folk Song Arranger beside Beat Lab](S:/CurioClass-codex/_scratch/folk-song-arranger/feel-comparison.jpg)

#### Done when

1. PASS: grid is the largest central element at 1366x768 and 680x425; check lights sit below it.
   Measured grid box/stage height at 1366: 55.54%. See sizes-frames and size-1366.json in Scratch.
2. PASS: default Length amber at 70 seconds; adding A produces green at 96.7 seconds, matching bars × 240 ÷ BPM.
3. PASS for current data: Flute Melody down flags F3 below C4; Octave up passes. This must be repeated after the real transcription.
4. PASS: buried example gives melody 2 against backing 12; passing example gives 4.5 against 5.
   Flagged Balance cell lists contain A columns, not Intro or Outro.
5. PASS: first visit to an occasion carries the plan; at 120 BPM Square dance reports missing Bass or Beat in A.
   Returning to an already saved occasion restores its separate plan, as documented in handoff.md.
6. FAIL for complete verification: live role/dynamic/Solo/Tempo behavior and uninterrupted playing-section removal work.
   Dispatch uses the kit's 150 ms horizon; gains update directly. Actual heard-within-150-ms latency was not measured.
7. PASS: no reason strip before the gate; a later change opens it. Chip and typed reasons save; Undo reverses the change.
   Undo also works after reload. Compact choice visibility was probed and visually checked.
8. PASS in exercised runs: music has no queued narration; Read stops music before speaking the updated hint.
   The audit's five-click how tests were clean. A real revision sequence logged four separate allGreen events.
   Same-mode double taps no longer hush the active line; the targeted Concert card check recorded one uncut line.
9. PASS for the card mechanism: occasion, traditional-song credit, players, plan and revision reasons appear;
   amber checks appear under Still to solve. The edition-level credit remains part of the failed source gate.

#### Wave lessons

- PASS, hint and voice: hints update synchronously, name the next action, and Read uses the current hint.
  Card-play and live-tempo hints were corrected to name controls present in those states.
- PASS, focus and layout: no focus on load; panel controls precede the grid; cell buttons update in place.
  Modal return focus uses the replacement element's ID when necessary; Back to Arrange focuses Play without scrolling.
  Hint space is reserved, and repeated mode taps are idempotent.
- PASS, sizes: every STANDARDS size was shot once in the full matrix. Confirmed Read width and singular-label faults were repaired.
  Targeted 680 layout probe reports no small targets, clipping, overlap, tiny text, unnamed controls or horizontal page scroll.
- PASS, no giveaways: this is a studio, not a hidden-answer quiz. Check feedback is the intended arranging mechanic.
- PASS, honest numbers: occasion windows are labeled Model, school ranges are identified in the editor, and loudness is a tool scale.
  Length formula and balance assumptions are stated on screen or in the relevant inspection hint.
- PASS, standards through action: organize a band/plan for Cr2; revise and explain for Cr3; choose interpretation for Pr4.
  The unresolved tune source prevents release, independently of that activity mapping.
- PASS, Motion off: the audit found no infinite animation. Beat timing remains; the playhead jumps instead of gliding.
- PASS, short choice sets: seven instruments, nine sections and six reasons fit their native dialogs at the tested extremes.
- PASS in the audit, resize mid-action: no exceptions or actual stuck controls; the reported generated-ID comparison is addressed below.
- PASS, no late welcome: no welcomeAfter; first-tap own instructions suppress the generic welcome as STANDARDS requires.
- PASS, unknown as unknown: no hidden diagnostic state is presented as established knowledge.
- PASS, one look/one meaning: roles have persistent words and colors; check status uses both symbols and color.
- PASS, truthful badges: checks derive from the current plan and their stated teaching rules, not a saved badge.
- PASS, hints change back: closing editors, stopping, changing modes and returning to Arrange reset the hint.
- PASS, no answer by copying words: no clue/answer matching puzzle or answer-position cue is used.

#### Audit leads

- One full audit completed, with 40 leads: S:/CurioClass-codex/_scratch/folk-song-arranger/audit/audit.md.
- Small Read target at 680 and 800: fixed with min-width 44 px; targeted 680 probe is clean.
- Every '1 bars' lead: fixed with one singular/plural helper for headings, palette, duration and program.
- Play keep-region leads in cell/player/section dialogs: intentional native modal behavior. The background is inert.
  The global Play keep requirement was removed from audit-states; active-dialog states keep the picker instead.
- Reason-text no-name lead: the associated label already existed; explicit aria-labels were added to both reason fields.
- Revised-plan resize 'disabled' IDs: these were timestamp-generated IDs differing between fresh runs, not disabled controls.
  Replaced timestamps with collision-checked stable IDs. Two fresh native add-section runs both produce s10 and clean layout probes.
- Back to Arrange focus lost: fixed. Targeted result records focus on Play.
- First-tap welcome-not-heard rows for Card, Play, occasion changes, Add, Reset, section headings, instruments and cells:
  intentional own-line suppression, or music hush, required by the standing voice rules. No late generic welcome was added.
- Same-mode Arrange/Card quick-tap cuts: fixed by returning early when the requested mode is already active.
  Targeted Card double tap recorded one spoken welcomeCard with no cut marker.
- 'Others moved' rows: mode/header changes are expected. Reserved hint height and shortened inspection hints reduce panel jumps.
- Additional frame finding: compact reasons were below the fold. Fixed with the compact editor; all six choices and its text field fit.
  Its probe may still list underlying Why/Undo/Reset as scrolled panel controls while the modal is active; they are inert background controls.
- Targeted repairs were checked. The full audit was not rerun, following the once-only build instruction.

#### Frames looked at

- Scratch root: S:/CurioClass-codex/_scratch/folk-song-arranger/.
- Individually inspected every produced tool shot in first-frames, check-frames, recheck-frames, sizes-frames, extras-frames,
  small-recheck-frames, post-frames, why-retry-frames, post-phone-frames, fix-frames and finish-frames.
- Inspected reason-text.png, concert-playing.png, full-playback-end.png and both maximum-fixed frames.
- Inspected all 47 audit frames through four contact sheets; opened the compact revised-plan and phone picker/editor frames individually.
- Inspected the art contact sheet, placed artwork, both bar frames, and the side-by-side comparison.
- Early hosted checks had a host-page favicon 404, not an application exception. Final hosted checks use a data favicon and reported no errors.
- Final functional and targeted repair runs reported no application console errors. Full-play resource probe found no HTTP resources.

#### Art made

- 11 images, 754,696 bytes total, about 737 KB: seven instrument cutouts, three venues and one paper texture.
- All generated during this build with the image tool, copied to art/raw, then processed only with art.py --rekey.
- No people. Zero redraws. All assets have drawn_by: codex and are used in the source.
- Final bundle: 1,275,590 bytes. Final artifact and metadata checks pass; no em dash in the authored required files.

#### Art still to paint

None. Narration recordings were not made; the listed Kore lines fall back to browser speech.

#### Engine changes wanted

No shared files were changed. handoff.md specifies exact proposed changes to kit/music-studio.js and its family doc:
accordion reed, accented frame-drum hit, chord-strum/live-dispatch support, per-player gain access and blow brightness.

#### Left open

- Matching public-domain 4/4 chorus printing and same-printing chord verification. Current melody is explicitly provisional.
- Instrument reference ranges follow the supplied spec; they were not independently reconciled against a particular Adler edition.
- Call-and-answer duration/singing ambiguity and bass-walk-up bar ambiguity use documented local resolutions. See handoff.md.
- Acoustic latency, timbral quality and browser/platform listening checks remain unverified. No audio was recorded.
- Kore recordings are absent, as the Build-only instructions prohibit recording.
- The full audit was not repeated after targeted fixes. This report does not claim a final clean audit.
- Reset/history and a long concert program can require scrolling in compact layouts; the frequent arranging controls remain initially visible.
- host.html was removed. Owned Chrome ports 9970/9971 and host port 8775 were confirmed closed before this report.
- The report is written last to honor the user's explicit stop condition; no polish round follows.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: folk-song-arranger

#### Played

Played cold as a grade 7 student, before reading the builder's report, handoff, notes or source: Play, cell/player/section editors, all occasions, checks, revision reasons and Concert card, including a naturally completed 97-second arrangement. Rechecked the corrected tune through its 70-second natural ending. Chrome stayed muted as required.
The venue paintings, large role grid and actionable checks were strong. The opening accompaniment and generic instructions were the flattest parts. Also inspected the projector layouts and both bar-tool frames.

#### Findings fixed

- **Blocker, general, src.html TUNE_TEXT:** the provisional notes were not the familiar chorus. Replaced them with the visually verified [Zebra Keys chorus score](https://www.zebrakeys.com/pdf/skip_to_my_lou.pdf), transposed C to F. Eight bars total 32 beats; sounding range is E4 to C5. Its printed harmony transposes exactly to F/F/C/C/F/F/C/F. Added accurate modern-edition credit in source, notes and metadata.
- **Blocker, general, notesFor/dispatch:** Range counted bass notes that the Intro and Hold never sounded. It now checks the actual walk-up and held F2. A flute Hold now sustains one F4 instead of an impossible triad; fiddle Chords use a double stop.
- **Should fix, general, grid/editor:** Chords-only Intro displayed a silent Melody block. Preset roles now show their true Rest, restrict incompatible choices and label first/last two-bar entrances. Saved plans remain readable.
- **Should fix, general, Balance:** Call and answer could pass with no answering player. Fewer than two Melody players now gives an actionable amber check.
- **Should fix, general, Tempo:** rewriting the unchanged native slider value interfered with change events; green transitions also compared against the already-updated checks. Preserved native events and the pre-change result, restoring keyboard revision logs, Undo snapshots and success events.
- **Should fix, general, hints/voice:** boundary instructions named disabled Move/Remove controls; closing a live editor said Play while Stop was showing. Fixed both. Intro presets now receive their own instruction without unavailable Octave controls, and editor instructions stop when the editor closes. All 15 fixed lines match voice/lines.json.
- **Should fix, general, resize/focus:** non-phone resizing did not recompute grid dimensions/type. It now does. Pinned the landscape hint, prevented keyboard focus from scrolling the whole page, and tightened dense-column padding/headings.
- **Polish, general, revision persistence:** the newest saved reason remains editable after reload.
- **Polish, general, flattest moment:** scheduled note light and restrained instrument response now show who actually sounds during the long opening. Motion off keeps beat timing/outline without those pulses.
- **Polish, general, weakest art:** regenerated the program paper with a quieter center and tactile edges, retaining the warm painted finish. Rekeyed all seven instrument cutouts to remove green spill and clean inner gaps.
- **Should fix, general, audit-states.json:** compact revised plans open a reason dialog; their keep region now names that active dialog rather than the deliberately covered background checks.

#### Findings left

- **Blocker, general, source provenance:** the exact historical public-domain printing required by the spec remains unverified. The identified chorus engraving is dated 2007, although the publisher lists the underlying music as public domain and permits redistribution. Older inspected printings are different variants. The wrong melody is repaired, but this stricter provenance gate is not passed; status stays beta.
- **Spec ambiguities, left unchanged:** eight-bar instrumental Call and answer versus singing/full-phrase wording, the four-bar bass walk-up allocation, and restoring separate saved occasions versus always carrying the current plan. Existing resolutions are explicit in handoff.md; changing them would need a spec decision.

#### Flattest moment left

Long runs of repeated A sections remain the simplest musical texture. The new note response makes their activity legible; students still supply variety through the existing New sections, roles and dynamics. No extra mode or topic was added.

#### Graphics

All 11 images checked independently at their placed sizes, including the large-screen venue and palette views; one coherent warm wood/lamplight set. No people, stereotypes, missing art tokens or placeholders. Seven cutouts cleaned; paper-card redrawn using the built-in imagegen tool, with its full prompt in art/prompts.json and final asset at art/paper-card.webp.
Final standalone HTML: **1,239,452 bytes, about 1,210 KiB**. White-on-role contrast recomputed as 5.46, 6.74, 8.63 and 5.06 to one. Fresh cultural review: PASS for the instrumental classroom scope; evidence is in _scratch/folk-song-arranger/sensitivity-review.md.

#### Audit

The required single final audit completed with exit 0 inside its 40-minute limit: _scratch/folk-song-arranger/review-audit/audit.md. All 58 audit PNGs were inspected on eight contact sheets, with lead frames opened separately.
All eight opening sizes, Concert card sizes, listed editor/playing states, Motion off, click/Enter focus, five-click and quick-tap checks, and resize stress completed. No application exceptions or stuck controls were reported.
Its **24 leads** were answered: 21 are required own-line/music suppression of the generic welcome; two concern inert background controls beneath the compact reason dialog; one concerns the specified internally scrolling phone grid beneath a player dialog. Active dialog choices are visible. Corrected the erroneous compact keep region.
Audit frames additionally confirmed the Intro instruction problem. After that narrow voice/editor and manifest repair, re-shot 680, 1366 and hosted 375 widths: zero errors. The full audit was not repeated.

| Voice check | Kind | Expected | Observed |
|---|---|---|---|
| presetHow, five held editor opens | how | 1 spoken, 4 silent | 1 spoken, 4 silent; first intentionally hushed on close |
| reasonHow, revision sequence | how | 1 spoken | 1 spoken |
| allGreen, five transitions at a 2-second action pace | event | speak while current; drop stale queued results | 4 spoken, 1 stale result dropped behind first reason instruction |
| Music playback | narration | none during Play | none in exercised live runs |

Thirteen independent numerical/behavior assertions passed: default and added-section duration, 32-beat/range transcription, flute octave recovery, buried/passing balance, Intro/Outro exclusions, occasion carry, dance pulse and tempo extremes. Checked minimum/maximum grids, grayscale, keyboard editing and all STANDARDS sizes. Notes' first three headings pass. Fixed-line manifest, art, punctuation and offline resource checks pass.

#### Left open

Historical-printing provenance above remains a release blocker. No historic lyrics, downloaded artwork or recorded audio were introduced.
Acoustic timbre and heard-within-150-ms latency were not measured with Chrome muted; dispatch/gain behavior was exercised. Narration uses browser fallback because recording is prohibited in this run.
Spec arithmetic discrepancies remain documented: its dance example uses an unavailable two-bar Outro; 74 bars at 100 BPM is 177.6 seconds, so 75 bars are needed for 180 seconds. The implemented formula is correct; spec.md was not edited.
Shared engine proposals remain in handoff.md; no kit changes. Owned Chrome ports 9960/9961/9967 and host 8765 are closed, and host.html is absent. Product writes stayed in this tool, review evidence in its Scratch subtree. No git commits or second full review.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Folk Song Arranger build handoff

Build only, 2026-11-01. No commits or polish round. All work is inside this tool and `_scratch/folk-song-arranger/`.

#### Layout and code

`src.html` starts with the kit starter's document/header/panel conventions and borrows `kit:curio` and `kit:music-studio`.
It has readable inline CSS and JavaScript. Tables define instruments, occasions, section types, voice lines and role colors.
`checks()` is the model. `change()` owns revision snapshots, reasons, validation, redraw and persistence.
The newest Undo snapshot is persisted with each occasion so reload does not strand its log.
`gridRender()` keeps cell and header buttons in place except for structural edits or the phone orientation change.
The panel comes first in DOM tab order. Native dialogs contain the short choice sets and restore focus with preventScroll.

At 1366x768 the grid box is 55.54% of the stage height. The painted venue sits over the parchment desk.
At short landscape sizes the occasion buttons sit in one row. The panel scrolls only for secondary controls and revision history.
At 375 the grid transposes, with fixed player headings and an internal grid scroll region. It does not scale a fixed-size scene.

`start()` creates one `MS.play(..., exclusive:false)` per player. Local instrument dispatch entries read the current cell
inside the engine's 150 ms lookahead. `syncVoices()` updates current note gains for dynamics, Solo and Sound.
The engine retains clock, tempo setter, per-player buses and the 50 ms Stop fade. Structural edits restart at the current
section/local beat; deleting that section chooses the next section. No shared engine files were edited.

#### Choices and ambiguities resolved

- There is no explicit Open questions section. These ambiguities were resolved locally and are recorded for review.
- Reason gating follows the explicit all-four-checks language: four different lights, or a naturally completed Play.
  The strip appears on the next change, not immediately when the fourth light is inspected.
- First visit to an occasion carries the plan. Revisiting a saved occasion restores its separate saved plan and log.
  This resolves the tension between keep the plan on switching and save an arrangement per occasion.
- Bass walk-up repeats the four-note walk over the first two bars, then two bars of chords, to honor the specified four-bar total.
- Call and answer is eight bars: the first two two-bar A phrases each get a two-bar response by another Melody player an octave up.
  Answering every phrase of a complete eight-bar A would require sixteen bars, contrary to the stated palette duration.
  No singing is synthesized. This instrumental rendering is a spec deviation to review.
- Counter-line assigns A to the first Melody row and the slower line to additional Melody rows. Two players are needed to hear both.
- With only one Melody row, Counter-line plays the slower line by itself, so choosing it still changes the music.
- In short previews and phones, the optional Why strip opens its six choices and text field together in a native dialog.
  The regular panel keeps the revision log and a Why this change button. This adapts the same controls to the smaller area.
- Cold review: sectionRoles and soundingRole now expose preset constraints. Incompatible saved roles draw as Rest. The editor disables roles the preset cannot sound; walk-up/drum/chord cells show their two-bar entrance.
- Cold review: Hold sounds a single F4 for Melody, an F chord for Chords (fiddle double stop), and F2 for Bass, with the Melody/Bass octave applied. notesFor uses exactly those pitches.
- Nominal length follows the required formula; final-bar slowing in Last line twice adds a little actual listening time.
- The spec's square-dance example counts a nonexistent two-bar Outro. With Hold it is 69 bars; with Last line twice it is 72.
- The walk example needs 75 bars at 100 BPM, not 74: 74 bars is only 177.6 seconds. The formula is implemented, not the erroneous suggestion.
- CALLERLAB's cited guide says 128 to 132 BPM, not 112 to 128. Keep the specified classroom window, labeled as a tool model.
- The user says stop as soon as codex-report.md is written, so that final report is written last instead of drafting it early.

#### Content needing attention

Cold review replaced the provisional sketch with the actual chorus from Zebra Keys (2007 engraving), p. 1,
https://www.zebrakeys.com/pdf/skip_to_my_lou.pdf . Rhythm is unchanged; C is transposed to F. The same source's
C/C/G/G/C/C/G/C symbols match F/F/C/C/F/F/C/F exactly. TUNE is 32 beats and E4 to C5; flute down flags E3 below C4.
The publisher identifies the collection as public-domain songs and permits redistribution, but the engraving carries
copyright 2007. The traditional melody and chord symbols are used; no accompaniment or score image is embedded.
The strict historical public-domain printing requirement remains unresolved after inspecting different older verse variants.
Do not relabel the modern engraving as a historical source or mark that requirement passed.
Fresh cultural/source review is in _scratch/folk-song-arranger/sensitivity-review.md.

#### Art and voice

Eleven generated paintings are in `art/`, with raw originals, prompts and drawn_by provenance. No people were generated.
All are placed: seven cutouts, three venue paintings and program paper. The palette offers the largest instrument view in small previews.
Kore/hs-narrator lines are listed, but no recordings were made. The kit uses browser speech. `__tool.vlog` is the test log.
No speech should overlap music; Read stops the arrangement first. All how lines use `V.how`; results use `V.say` and revision validity.

#### Engine changes wanted

- `kit/music-studio.js`, `INSTR`/sound exports: add a reedy accordion voice with detuned sawtooths through a lowpass.
  Current local implementation is `reed(f,t,d,b)` in this tool.
- `kit/music-studio.js`, sound exports: add a short noise-and-tone frame-drum hit with an accent argument.
  Current local implementation is `drum(t,b,accent)`.
- `kit/music-studio.js`, `play()` event dispatch: support chord events and timed strums, plus a public live event callback
  and per-player gain access. The current local adapter registers small pulse dispatches in `MS.INSTR` and creates gain sends.
- `MS.blow`: accept brightness/timbre options. The current fiddle uses a different output filter, but the stock flute harmonic
  source limits the amount of authentic fiddle brightness available without changing the engine.
- `docs/families/music-studio.md`: document those APIs, live gain/Solo behavior and Sound changes after implementation.

#### Validation record

Evidence, commands, frames, probes and the one final audit are in Scratch. See codex-report.md for final outcomes and open leads.
The host server and every Chrome started for checks must be closed before delivery; `host.html` is temporary and removed.
The audit finished with 40 leads. Confirmed target, plural, focus and mode-repeat faults were fixed with targeted checks.
Native-modal coverage and first-tap own-line welcome suppression are intentional. Timestamp-based IDs were replaced with
stable unique IDs so the resize comparison does not mistake a new section's generated ID for a disabled control.
The full audit was not rerun after these repairs. Compact reasons were also repaired after inspecting the audit frames.


#### Cold review repairs, 2026-11-04

- Range no longer checks phantom bass notes in the Intro or Hold. A flute Melody Hold is one sustained F, not a triad.
- The grid shows preset silence as Rest. Editor role options and first/last two-bar cues explain the prescribed texture.
- Balance flags a missing answering player in Call and answer.
- Tempo rendering leaves an unchanged native input value alone. This preserves change events, reason logging and Undo.
  Green transitions compare the pre-change check result, including keyboard tempo changes.
- Boundary instructions now name available actions, and closing a live editor keeps a Stop instruction.
- Per-note light/instrument feedback follows scheduled sound. Motion off leaves the beat outline and removes the pulse.
- Program paper was redrawn with the built-in imagegen tool. Its full prompt is in art/prompts.json; the final asset is
  art/paper-card.webp. Seven cutouts were rekeyed with spill and inner-hole cleanup, preserving the original drawings.
- A saved latest reason remains editable on reload.
- Cold-review evidence and final audit are under _scratch/folk-song-arranger/review-*; see codex-review.md for the outcome.


#### Cold review final audit

The once-only review audit completed with exit 0 and 24 leads. All eight opening sizes, editor palettes,
Motion off, per-control click/Enter focus checks, five-click/quick-tap checks and resize stress completed.
No application exceptions or stuck controls were reported. Its 58 PNGs were inspected on eight contact sheets,
with the modal leads opened individually. See _scratch/folk-song-arranger/review-audit/audit.md.

Twenty-one welcome leads are intentional first-tap own-line suppression or music hush. The remaining three
concern inert background controls under native dialogs and the phone grid's specified internal scrolling.
The revised-plan manifest now keeps the active reason dialog at compact sizes instead of the covered checks.

Audit frames also confirmed that Intro instructions named unavailable Octave controls. Added presetHow,
matched voice/lines.json, and stopped editor instructions when their dialog closes. The targeted 680, 1366 and
hosted-phone recheck reported no errors; five opens spoke presetHow once and were silent four times afterward.
The first was intentionally hushed when the user closed its editor. All 15 fixed lines match allLines().
The full audit was not rerun after these narrow repairs. Final bundle: 1,239,452 bytes, about 1,210 KiB.
Owned Chrome and host processes were closed. The historical-printing source requirement remains open.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
