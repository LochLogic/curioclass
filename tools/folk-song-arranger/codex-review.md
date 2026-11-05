# Codex review: folk-song-arranger

## Played

Played cold as a grade 7 student, before reading the builder's report, handoff, notes or source: Play, cell/player/section editors, all occasions, checks, revision reasons and Concert card, including a naturally completed 97-second arrangement. Rechecked the corrected tune through its 70-second natural ending. Chrome stayed muted as required.
The venue paintings, large role grid and actionable checks were strong. The opening accompaniment and generic instructions were the flattest parts. Also inspected the projector layouts and both bar-tool frames.

## Findings fixed

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

## Findings left

- **Blocker, general, source provenance:** the exact historical public-domain printing required by the spec remains unverified. The identified chorus engraving is dated 2007, although the publisher lists the underlying music as public domain and permits redistribution. Older inspected printings are different variants. The wrong melody is repaired, but this stricter provenance gate is not passed; status stays beta.
- **Spec ambiguities, left unchanged:** eight-bar instrumental Call and answer versus singing/full-phrase wording, the four-bar bass walk-up allocation, and restoring separate saved occasions versus always carrying the current plan. Existing resolutions are explicit in handoff.md; changing them would need a spec decision.

## Flattest moment left

Long runs of repeated A sections remain the simplest musical texture. The new note response makes their activity legible; students still supply variety through the existing New sections, roles and dynamics. No extra mode or topic was added.

## Graphics

All 11 images checked independently at their placed sizes, including the large-screen venue and palette views; one coherent warm wood/lamplight set. No people, stereotypes, missing art tokens or placeholders. Seven cutouts cleaned; paper-card redrawn using the built-in imagegen tool, with its full prompt in art/prompts.json and final asset at art/paper-card.webp.
Final standalone HTML: **1,239,452 bytes, about 1,210 KiB**. White-on-role contrast recomputed as 5.46, 6.74, 8.63 and 5.06 to one. Fresh cultural review: PASS for the instrumental classroom scope; evidence is in _scratch/folk-song-arranger/sensitivity-review.md.

## Audit

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

## Left open

Historical-printing provenance above remains a release blocker. No historic lyrics, downloaded artwork or recorded audio were introduced.
Acoustic timbre and heard-within-150-ms latency were not measured with Chrome muted; dispatch/gain behavior was exercised. Narration uses browser fallback because recording is prohibited in this run.
Spec arithmetic discrepancies remain documented: its dance example uses an unavailable two-bar Outro; 74 bars at 100 BPM is 177.6 seconds, so 75 bars are needed for 180 seconds. The implemented formula is correct; spec.md was not edited.
Shared engine proposals remain in handoff.md; no kit changes. Owned Chrome ports 9960/9961/9967 and host 8765 are closed, and host.html is absent. Product writes stayed in this tool, review evidence in its Scratch subtree. No git commits or second full review.
