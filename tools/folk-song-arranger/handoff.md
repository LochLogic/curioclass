# Folk Song Arranger build handoff

Build only, 2026-11-01. No commits or polish round. All work is inside this tool and `_scratch/folk-song-arranger/`.

## Layout and code

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

## Choices and ambiguities resolved

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

## Content needing attention

Cold review replaced the provisional sketch with the actual chorus from Zebra Keys (2007 engraving), p. 1,
https://www.zebrakeys.com/pdf/skip_to_my_lou.pdf . Rhythm is unchanged; C is transposed to F. The same source's
C/C/G/G/C/C/G/C symbols match F/F/C/C/F/F/C/F exactly. TUNE is 32 beats and E4 to C5; flute down flags E3 below C4.
The publisher identifies the collection as public-domain songs and permits redistribution, but the engraving carries
copyright 2007. The traditional melody and chord symbols are used; no accompaniment or score image is embedded.
The strict historical public-domain printing requirement remains unresolved after inspecting different older verse variants.
Do not relabel the modern engraving as a historical source or mark that requirement passed.
Fresh cultural/source review is in _scratch/folk-song-arranger/sensitivity-review.md.

## Art and voice

Eleven generated paintings are in `art/`, with raw originals, prompts and drawn_by provenance. No people were generated.
All are placed: seven cutouts, three venue paintings and program paper. The palette offers the largest instrument view in small previews.
Kore/hs-narrator lines are listed, but no recordings were made. The kit uses browser speech. `__tool.vlog` is the test log.
No speech should overlap music; Read stops the arrangement first. All how lines use `V.how`; results use `V.say` and revision validity.

## Engine changes wanted

- `kit/music-studio.js`, `INSTR`/sound exports: add a reedy accordion voice with detuned sawtooths through a lowpass.
  Current local implementation is `reed(f,t,d,b)` in this tool.
- `kit/music-studio.js`, sound exports: add a short noise-and-tone frame-drum hit with an accent argument.
  Current local implementation is `drum(t,b,accent)`.
- `kit/music-studio.js`, `play()` event dispatch: support chord events and timed strums, plus a public live event callback
  and per-player gain access. The current local adapter registers small pulse dispatches in `MS.INSTR` and creates gain sends.
- `MS.blow`: accept brightness/timbre options. The current fiddle uses a different output filter, but the stock flute harmonic
  source limits the amount of authentic fiddle brightness available without changing the engine.
- `docs/families/music-studio.md`: document those APIs, live gain/Solo behavior and Sound changes after implementation.

## Validation record

Evidence, commands, frames, probes and the one final audit are in Scratch. See codex-report.md for final outcomes and open leads.
The host server and every Chrome started for checks must be closed before delivery; `host.html` is temporary and removed.
The audit finished with 40 leads. Confirmed target, plural, focus and mode-repeat faults were fixed with targeted checks.
Native-modal coverage and first-tap own-line welcome suppression are intentional. Timestamp-based IDs were replaced with
stable unique IDs so the resize comparison does not mistake a new section's generated ID for a disabled control.
The full audit was not rerun after these repairs. Compact reasons were also repaired after inspecting the audit frames.


## Cold review repairs, 2026-11-04

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


## Cold review final audit

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
