# Choreography for a Cause handoff

## Implementation
src.html starts from the kit starter and loads kit:curio plus kit:dance. Its sections are styling, four permanent workspace shells, source card data, voice, persistence, authoring, performer adapter, source phrases, shared transport, viewer model and event wiring. Data stays in the single bundled HTML. No external requests or libraries are needed.

The open folder uses five evidence cards. The five source choices in Motifs stay visible in a left rail. Primary Make, Play and Stop controls sit outside the scrolling secondary editor. Structure has a pinned transport and a sideways scrolling form strip on phones. Viewers has four readings around the stage and a version panel. Compact fact folders scroll their evidence area so full source text remains accessible.

## Movement and timing
Dance.floor uses stage projection. Its stage view ignores the backdrop option, so resizeStage clears decoration layers and inserts the studio painting, keeping the engine's floor projection. No shared file was changed. Floor contact is at a projected front edge of 88 percent, with performers at z 38. The painting is stretched to the real stage bounds to keep all floor edges visible.

motifPhrase makes eight one-count Dance.phrase steps and uses source-specific phrasing for the cards whose rule needs different dancer roles, pauses or a particular count. Pose edits switch to the student's chosen A/B shapes. Dynamics use Dance.dyn through the phrase engine. Devices change pose reach, pathway amplitude, sampled time or time direction. Low floor poses retain their native shape to avoid applying the kit's extra squat to an already grounded body.

compose caches per-slot phrases. One Dance.clock at 100 bpm drives all three performers, Lantern and the dots. Per-slot canon is sampled with two-count offsets inside each eight-count phrase, holding a delayed entry and truncating at the slot end so total dance counts stay exact. Slot dancer count wins over motif count. Empty slots are skipped. A slot tap replaces the old run synchronously without another count-in. stop drops the play handle, music output, clock and voice immediately.

## Model and storage
model is a pure function over motifs, slots and issue. Presence sums eight times repeat times slot dancer count per motif id. The kid's size is absolute start/end level span plus pathway travel. The level pair counts as one contrast feature, and dancer comparison uses the actual slot count. Empty entries are skipped, so the first and second filled slots stand in for A and B if a strip contains holes. Ties remaining after the stated rules use first encountered motif.

Viewers reveal after their dependent slot: teacher after B, stranger after the last, friend after the last, kid after the last occurrence of its chosen motif. Cards explicitly identify the model. Devices and edited prose never change the source card's viewer words. Real viewer prose is escaped and saved locally.

localStorage key curio-choreo-cause contains the current draft and up to eight immutable version snapshots with full motifs, slots, model results and real readings. Opening a version with unsaved work asks first. Changing issue keeps old motifs grayed, replaces the current strip and asks first. A six-motif limit applies across issues. Clear all confirms. All storage operations are caught; the hint reports inability to save.

## Owner's painted dancers decision
The kit figure is temporary. Final art direction is painted dancers. createPerformer and paintPerformer are the swap boundary; preserve the Dance.play set/render interface, timing, floor registration, per-slot visibility and shape badges. art/prompts.json lists all 21 used poses with people:true and requirements for three identities, levels, mirroring and transition poses. None of these people assets was generated in this build. Do not replace movement with a single static painting.

Seven non-person paintings were made with the built-in image tool. Full prompts are in art/prompts.json, raw originals in art/raw, finished images in art/*.webp. No people or lettering appears in them. The larger issue images remain at 1200 pixels; all seven are used by the tool.

## Open questions resolved
- Voice: the spec proposes adding a grown-up voice because the existing bank has no free one. Bank edits are outside this build's allowed folders, so the manifest retains the specified lively-host / Sadachbia while recording the desired future grown-up replacement here. No recordings were made, as required. Browser speech does not select Sadachbia by name and is a fallback, not the final voice.
- Timing clarification: 96 dance counts are 57.6 seconds. Four count-in clicks add 2.4 seconds, so the entire longest run is exactly 60 seconds, rather than under 60 including the count-in. UI and notes say this explicitly.
- Default dancer counts unspecified in several proposals use two, or one for an individual voice. Explicit three-dancer and two-dancer rules win. This makes the Sources example's B presence 16.

## Engine changes wanted
- kit/dance.js, floor.draw: honor backdrop for stage and provide an option to suppress stage fill and curtains. resizeStage currently replaces only those decoration layers locally.
- kit/dance.js, level: add native low variants for floor shapes so applying low does not double-bend a sitting, lying or crouching dancer. safeLevel preserves native floor shapes locally.
- kit/dance.js, music: allow instrument-specific volume and long pad duration. Lantern currently repeats overlapping engine pad notes to hold its eight-count harmonies; a soft pluck uses the shared track volume.

## Next
Build only. A cold review is next. No polish round, commit, branch change or shared-engine edit was made. The final report records the actual checks and remaining limitations; it is not an approval of the final painted performer art.

## Verification and compact layout limits
The single full audit completed with 16 leads and no runtime, target-size, resize or infinite calm-animation failures. Its bundle predates the final pinned-library layout, dialog aria-labels, folder welcome correction and source-phrase refinements. Targeted checks followed those corrections; there was no second full audit. Evidence lives in _scratch/choreography-for-a-cause/.

Both six-motif libraries are now outside the secondary scroll panels. All six choices remain visible at 680x425, 1366x768 and the actual 375x812 iframe. Secondary editing parameters, Delete, Clear all and long version lists still scroll in compact layouts. Full evidence cards scroll at short heights and on phones. This is a remaining strict short-choice/layout limitation for cold review, rather than a claim that every control fits simultaneously.

The modal backdrop intentionally covers the page hint while a dialog is open. The dialog supplies its own instruction. The audit's unnamed real-viewer input findings were addressed with explicit aria-labels in addition to the enclosing labels. First held taps on each of the three folders now start welcomeFile immediately. The final Chrome instances and host were closed and host.html removed.

Audio was exercised in muted Chrome, including narration logs, transport replacement and timing. Human headphone review of timbre, music balance and narration pacing remains open. Browser speech remains the specified build fallback. The built-in image tool made every non-person painting; no generated people or voice recordings were made.
