# Choreography for a Cause handoff

## Implementation
src.html starts from the kit starter and loads kit:curio plus kit:dance. Its sections are styling, four permanent workspace shells, source card data, voice, persistence, authoring, performer adapter, source phrases, shared transport, viewer model and event wiring. Data stays in the single bundled HTML. No external requests or libraries are needed.

The open folder uses five evidence cards. The five source choices in Motifs stay visible in a left rail. Primary Make, Play and Stop controls sit outside the secondary editor. Structure has a pinned transport and six slots that fit at phone width, each at least 44 px wide. Viewers has four readings around the stage and a version panel. Compact fact folders scroll their evidence area so full source text remains accessible.

## Movement and timing
Dance.floor uses stage projection. Its stage view ignores the backdrop option, so resizeStage clears decoration layers and inserts the studio painting, keeping the engine's floor projection. No shared file was changed. Floor contact is at a projected front edge of 88 percent, with performers at z 38. The painting is stretched to the real stage bounds to keep all floor edges visible.

motifPhrase makes eight one-count Dance.phrase steps and uses source-specific phrasing for the cards whose rule needs different dancer roles, pauses or a particular count. Pose edits switch to the student's chosen A/B shapes. Dynamics use Dance.dyn through the phrase engine. Devices change pose reach, pathway amplitude, sampled time or time direction. Low floor poses retain their native shape to avoid applying the kit's extra squat to an already grounded body.

compose caches per-slot phrases. One Dance.clock at 100 bpm drives all three performers, Lantern and the dots. Per-slot canon is sampled with two-count offsets inside each eight-count phrase, holding a delayed entry and truncating at the slot end so total dance counts stay exact. Slot dancer count wins over motif count. Empty slots are skipped. A slot tap replaces the old run synchronously without another count-in. stop drops the play handle, music output, clock and voice immediately.

## Model and storage
model is a pure function over motifs, slots and issue. Presence sums eight times repeat times slot dancer count per motif id. The kid's size is absolute start/end level span plus pathway travel. The level pair counts as one contrast feature, and dancer comparison uses the actual slot count. Empty entries are skipped, so the first and second filled slots stand in for A and B if a strip contains holes. Ties remaining after the stated rules use first encountered motif.

Viewers reveal after their dependent slot: teacher after B, stranger after the last, friend after the last, kid after the last occurrence of its chosen motif. Cards explicitly identify the model. Devices and edited prose never change the source card's viewer words. Real viewer prose is escaped and saved locally. Conditional craft notes appear before recognition readings. If holes mean the first two played phrases are not A and B, the teacher's contrast note names the played phrases rather than inventing a B.

localStorage key curio-choreo-cause contains the current draft and up to eight immutable version snapshots with full motifs, slots, completed model results and real readings. Opening a version with unsaved work asks first. Changing issue keeps old motifs grayed, replaces the current strip and asks first. A six-motif limit applies across issues. Clear all confirms. All storage operations are caught; the hint reports inability to save. All eight versions fit in a fixed grid outside the notes scroller; full metadata remains in accessible names and titles. An unshown reading is marked ?, with a visible legend, never zero.

## Owner's painted dancers decision
Three painted performers are live through createPerformer, paintedDancer and paintPerformer. CAST_ART and CAST_REG, plus FLOOR_ART and FLOOR_RECTS, are the swap boundary; preserve the Dance.play set/render interface, timing, floor registration, per-slot visibility and shape badges. art/prompts.json marks both atlases people:true. One neutral painted pose per individual supplies articulated pieces; kneel, curl and lie add nine floor keys. The 21 older pose requests are retained as superseded records. Movement is still interpolated by the dance engine.

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
The cold review repairs below supersede the original build's open artwork and compact-editor limitations. No commit, branch change or shared-engine edit was made. Read codex-review.md for the final checks and remaining limitations.

## Verification and compact layout limits
The cold review's single final full audit completed with 13 leads and no runtime, initial-size, resize or infinite calm-animation failures. Eleven actionable rows were fixed: compact sidebar overflow (seven rows), hidden version choices (two), hidden narrative slots (one), and the unnamed meaning field (one). Two leads intentionally report the modal backdrop covering the page hint; each modal provides its own instruction. Targeted checks followed these corrections; there was no second full audit. Evidence lives in _scratch/choreography-for-a-cause/review-audit/ and the post-audit frame folders. The builder's earlier audit is separate historical evidence.

The cold review replaced the scrolling parameter stacks with named editor pages. Both six-motif libraries and every short parameter group have dedicated views. Full evidence cards and long real-viewer notes still scroll at short heights and on phones. Clear all now stays beside Back to Structure, stacking below it at compact desktop widths. Six slots and all eight version buttons remain visible, with targets at least 44 px. This follows STANDARDS' visible-short-choices rule over the spec's sideways phone strip; overflow remains available if needed.

The modal backdrop intentionally covers the page hint while a dialog is open. The dialog supplies its own instruction. Both real-viewer fields and the Name/What it shows editor have explicit accessible names. First held taps on each of the three folders start welcomeFile immediately. The final Chrome instances and host are closed and host.html removed at review closeout.

Audio was exercised in muted Chrome, including narration logs, transport replacement and timing. Human headphone review of timbre, music balance and narration pacing remains open. Browser speech remains the fallback. Seven existing paintings were preserved, and the built-in image tool made two performer atlases during review, for nine runtime images. No voice recordings were made.


## Cold review repairs (2026-11-05)
The painted cast is live. CAST_ART and CAST_REG plus paintedDancer are the replaceable skin adapter. cc-cast is one neutral T pose per performer, not a static replacement: clipped painted pieces follow Dance.dancer's projected joints on every render. The engine continues to own poses, paths, clocks, canon, devices and calm timing. Three shape badges preserve non-color identities. All people art is people:true. The 21 earlier unmade pose requests are retained as superseded records, not required runtime assets. Source image, prompt and contact sheet are retained.

Editors use an Edit selector to expose complete small groups without hiding short choice sets below a scroll edge. Libraries, Shape/Space/Meaning, Slot settings and Form checks retain the same authoring capabilities. The main transport stays pinned. Old-issue motifs remain gray and cannot be placed or edited, but can be selected in Your motifs and deleted through Meaning, preventing a full-library dead end.

Save version preserves only readings actually completed, never computes a score behind a skipped replay. Unwatched drafts say Viewers not shown. A revision clears current model and real readings; old snapshots retain their own readings. Loading a version restores its card, issue and reveal state. Switching ABA/Rondo normalizes repeated-letter motif identity. The viewer summary states that recognition reads source cues, not artistic quality, and that each motif keeps its source meaning after edits.

Slot changes while playing rebuild the selected slot's editor before restarting, so edits cannot target the previous slot. Fix variations stops the previous transport. Narrative add/remove recovers focus at its limits. End-of-play dots hold the final eighth count rather than wrapping to count one. The local low kneel now sits on the heels; the reservoir phrase descends through all four measured stages.

The first tuning line now starts with Make's immediate movement instead of waiting behind an eight-count take. Source selection and placement preserve still-relevant instructions. Voice manifest matches the fixed lines. No recordings were generated.

## Sensitivity
Review the three painted individuals for respectful, natural representation and anatomical clarity in motion. They do not stand for cultures or a preferred dancer body. Source voices remain explicitly invented. River allocation uses Upper and Lower Basin names and beneficial use; teacher notes state that the card is not a full history of Tribal rights or Mexico's share. The water issue should not be read as solely a farmer's concern.

Floor artwork: FLOOR_ART and FLOOR_RECTS add nine key poses (kneel, curl and lie for each of the three people). Painted-upright pieces follow the projected joints; painted-floor key poses blend from the same joint angles and remain anchored to the engine floor. Motion off still jumps only on counts. The two atlases contain twelve source poses total, replacing the earlier request for 21 poses times identities times levels. Crouch, sit, traveling, asymmetry and devices continue through the articulated cast. The river convergence and split leave enough space to read each body.

Storage schema 2 records only completed replay readings. Schema 1 is accepted without losing motifs, versions or typed notes, but its unverified computed recognition entries are cleared and must be replayed. This prevents old shortcut results from surviving the save repair.

## Left open after cold review
- Blocker, prescribed recognition model: one Glow dome placed once into Rondo fills the three A slots, leaves B/C empty and still earns 4/4 after replay. No original movement or meaning is required. The spec explicitly demands the source-word heuristic and same-motif extreme; replacing that model would contradict it. The UI now describes the limitation and foregrounds craft feedback, but this does not establish learning or clear the blocker. An owner/spec decision is needed before treating recognition as a success gate.
- Unattended decisions: use the owner's painted cast and minimal pose atlases; preserve the prescribed scoring model under CODEX-REVIEW section 3; prioritize the STANDARDS visible short-choice rule on phones. No external action or shared-kit change was made.
