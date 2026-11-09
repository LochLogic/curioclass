# Mini Documentary Crew handoff

Build only. No commits, publication, uploads or polish round.

## Source map

`src.html` starts from the kit starter structure and loads the kit and grade 9 to 12 theme, then overrides it with the specified production-whiteboard palette. Responsive CSS comes first. The script defines art, shoot rules, source clips, voice lines, persistence, calendar validation, editing, the attention model, playback, premiere and input handlers. `window.__tool` exposes live state, data, rule functions, model and voice log for review.

Images occur once in the ART table so the bundle does not repeat their data. Painted frames fill the viewer; exact calendar, timeline, subtitles, lower thirds, poster type and line chart are code. All 15 images are embedded; the 12 place/object frames are active and the three portraits are held behind the approval switch. Raw originals and generated WebP files are under art; review sheets and discarded candidates stay in Scratch or the generator's own cache.

## Rules and tricky parts

- Calendar validation checks occupancy, time, availability, weather, crew and form chronology at once. Moving or removing forms cannot invalidate an existing interview. The producer can fill exactly one missing role. Wrap freezes the production record.
- `placement` is a pure query; `place` owns feedback and persistence. Clip creation checks that its shoot exists. Missing shoots never enter the bin.
- Each timeline instance has a stable uid. In and out are whole source seconds. Editing during playback retains the playhead. Playback generations prevent an old animation loop from joining a restarted run. Motion off removes panning, not elapsed time.
- Selecting a bin clip while stopped previews its source frame and clears timeline selection. Editing actions then require a timeline selection. Subtitles follow the original source time through trims rather than squeezing all testimony into a shorter cut.
- A low point at a clip boundary selects the outgoing responsible interview. Structural edits reveal the selected clip inside the timeline only. An edited cut hides the stale low-point marker until screened again.
- Compact Saturday cells reserve extra width for two crew assignments. Phone bin and timeline accept native horizontal touch scrolling. At short heights, Trim shows all four numeric/range controls together.
- A covered interview has B-roll visual kind, resets the continuous uncovered interview streak and retains interview text. Covers may hold a painted frame longer than its standalone source duration, as permitted by the spec's interview-minus-three-second limit.
- Identification requires the actual speaker and role; captions require the source year and a place. Punctuation-only and wrong-person inputs are rejected. Empty text removes an identification and restores its model penalty.
- Completed screenings snapshot the cut and line. Partial tests are not saved. A changed cut needs a new screening before locking a plan. Five comparisons are retained.
- Wrapping without any footage exposes the existing Start over action in Edit and a matching voice line. This recovery avoids a dead end when Screen and Premiere cannot open. It does not add a new production mode.
- The attention model measures its literal formula, not documentary competence. Repeated B-roll is an explicit blind spot. Free-text invite and audience fields are completeness checks, not automated judgments of good reasoning.
- The user's anti-cheat instruction takes precedence for saved best lines: overlapping reuse of the same source seconds is flagged, cannot set a saved best screening and cannot trigger the clean narration. Its actual attention trace remains the unmodified formula. Cover and standalone overlaps both count toward the reuse warning. A single held frame remains permitted within one cover.
- Every storage operation is guarded. The footer states device-only persistence. All student text is escaped before HTML rendering or assigned with textContent.

## Decisions and spec questions

- Use friendly-dad as the spec leans toward, despite its younger bank label. It represents a patient retired producer; interview testimony stays as subtitles. The no-recording build instruction means the kit's browser fallback is used.
- All three people portraits are generated and marked `people: true`. The spec separately requires owner approval before display. `PORTRAITS_APPROVED` therefore starts false; `paintedFrame` uses mdc-set for interview cards, thumbnails and viewers until that review. The actual speaker metadata and model remain unchanged. The contact sheet is in Scratch for review.
- Use the written attention formula when its worked example differs. Independent results are in Scratch `numbers.json`; the final report lists the conflicts. Continuous interview means no visual-kind break, even across different interview clips.
- Apply kind-change bonuses at the first second of the incoming visual kind, then that second's gain or penalty. Recovery uses the formula's explicit cap of 90. The end bonus replaces the last second's point for averaging. These conventions make the otherwise underspecified discrete model reproducible.
- Wednesday historian slots and week 2 Friday morning Ana slots pass the guest's availability rule but fail the stated crew rules because both camera and sound are absent. Do not silently extend the crew's availability. Thursday historian and Saturday morning noisy Ana are fully feasible alternatives. The full Sources schedule is accepted.
- The archive scan includes requesting the license. The spec has no separate request card or control; the shoot label makes that linkage explicit.
- Keep all 15 images at the requested 1280-pixel long side and quality 72. The bundle exceeds the 2 MB goal. No image was dropped to meet a size target.
- The early-report instruction conflicts with the user's stop-on-report instruction. Evidence was accumulated in Scratch `report-draft.md`; the final tool report is written only after checks finish.
- The written model forgives noisy-audio attention loss during a cover although interview sound continues. This assumption is disclosed; a cover does not repair audio.
- Existing bar bundles were opened rather than rebuilt in their tool folders, which would violate this run's write boundary.

## Sensitivity

Fictional occupational and community story with older adults and a shoe repairer named Ana Ruiz. Nothing depicts a real family or town. Review the three portraits for respectful age, cultural and occupational representation, natural anatomy and stereotypes. The story's economic changes and shoe-repair claims are invented testimony, not historical or technical generalizations. A fresh cultural review remains part of the later cold review, not this build-only session.

## Engine changes wanted

No kit changes. No shared scripts, docs or another tool was edited. These test-helper changes would improve later runs:

- `scripts/drive.py`, `host`: expose the actual server PID or a controlled shutdown endpoint, and reject an occupied host port. On this Windows Python launcher, terminating the wrapper left a worker listening on 8795. This build closed only processes whose full arguments identified this tool and that port.
- `scripts/audit_tool.py`, `Audit.size`: include the host response and a diagnostic capture when the iframe execution context is missing. The 375-wide audit could not inspect its iframe; separate genuine iframe tests passed after the stale host was closed.
- `scripts/audit_tool.py`, `Audit.stress`: compare generated control IDs within the same project run, or match their semantic positions. Fresh projects generate different clip UIDs, producing false disabled-after-resize leads. A same-project resize probe retained all 15 enabled clips and the playhead.

## Evidence

All test scripts, independent numbers, generated-image contact sheets, bar frames, functional results, screenshots, voice walks and the partial audit are in `_scratch/mini-documentary-crew/`. Final checks passed 79 functional assertions and 396 independent scheduling cases. A public-control run completed all nine shoots, a 330-second edit, a real screening and a locked premiere. Same-project resize and native phone touch probes reported no exceptions.

The single audit reached its 2400-second limit during stress checks, through trim-handles. It preserved 56 leads and 44 frames; it is not a completed clean audit. Its frozen bundle SHA-256 is `144425596c0e0a347c3c8bb37f3caa6268ece1ae587d48014d7f8ba593c5c8ff`. Later scoped repairs and direct probes are recorded in the final report. The modal audit-state keep region now names its dialog, without requiring the inert background hint to be unobscured. Do not infer that the whole audit was rerun after those repairs.

## Build completion provenance

The source, 15 images and extensive Scratch evidence already existed when this completion pass began. They were preserved. The report distinguishes retained evidence from checks rerun now. The empty interview setup was redrawn with the built-in OpenAI image tool, its full prompt saved in prompts.json, its raw PNG copied locally, and art.py run only with --rekey. The earlier version is retained in Scratch. The completed WebP was inspected at 1280 by 720 pixels.

The default shell Python lacks NumPy and Pillow. The available AI environment's interpreter could not launch under this session's restrictions. Running the same required art.py script through the shell Python with that environment's read-only site-packages on sys.path succeeded. No dependency installation or shared-file change was made.

See codex-report.md for every lead group's disposition, final bundle hash, resource cleanup and unresolved numerical contradictions. The next step is the separate cold review, not a polish round in this session.

Current completion checks: 75 functional assertions and 396 independent schedule cases passed; a real-control nine-shoot, 15-clip, 330-second screening and locked premiere passed before the final visual-only approval fallback. Final 1366 and 680 fallback checks passed with no broken images or console errors. See completion-*.json, portrait-gate-*.json and completion-bar-comparison.jpg in Scratch. Final bundle SHA-256: c910af574001da986483e392721debaec740521ae4770239d98c118059ed9589.

## Cold review repairs

- Uncaptioned archive frames no longer receive automatic date subtitles. Bin descriptions remain reference metadata; the viewer uses the student's Caption. B5 retains an explicit door-bell and machines caption.
- Cover now previews its covered tail immediately after Apply when stopped. It does not move an active playhead. The dialog and model note explicitly say that B-roll does not repair noisy interview sound.
- The source-reuse guard now includes cover source seconds. A held frame is counted once within a cover, but reuse in another cover or standalone instance cannot set a saved best or trigger clean narration. Previously saved screenings are rechecked on load. The spec's numeric attention formula is unchanged.
- Editing transport and inspector controls precede the long bin in keyboard order. Add to end precedes bin items in DOM order while retaining its familiar visual position.
- mdc-main was redrawn in the same house style to show bare vacant windows beside the active repair shop. Full review prompt and provenance are in art/prompts.json; the prior WebP is preserved in Scratch.
- The explicit portrait-approval switch remains false, as the spec requires. This unattended review does not infer owner approval. The three completed respectful portraits remain available for that review.
- Independent review calculations confirm material 469 s, good sample 330 s / low75 / average90.4788, bad sample299 s / low0 / average24.5753, noisy good low30.5, and first-three-Ana103 s / end33.5. The contradictory spec examples remain a spec correction request.
- Current fact checks: W3C SC1.2.2 supports prerecorded captions, including meaningful sounds and speaker identification; CMSI confirms fair use may avoid licensing. Gallaudet Schuchman Documentary Center documents informed consent and releases before interviews. NCAS Media Arts at a Glance supports the four broad production anchors. The fictional dates, characters, testimony, schedule and audience formula come from spec.md.
- The viewer now maintains its 16:9 image-and-overlay rectangle inside tall narrow monitors. All seven desktop dimensions and the genuine 375-wide host were checked after the change.
- Lock hushes a readiness instruction immediately before the finished-sheet event. A clean screening invites review of its low point, rather than assuming that the student must fix a mistake.
- Repeated filler in Invite and audience text, and punctuation-only titles, do not satisfy completion. These remain field-completeness checks; they do not grade the meaning of free prose.

Comparison curves now use actual elapsed seconds rather than stretching an earlier runtime onto the current axis. The review verified a 280-second earlier line ending at its true time beneath a 330-second current cut. Adjacent no-op drops and Stop in empty Edit also retain truthful, usable feedback.

The final cold-review audit reached its single 2400-second deadline with a preserved partial report, 69 leads and 59 frames. Confirmed phone action-bar spacing, heading hitboxes and an explicit caption-field name were repaired. Named-identity and exact-date boundaries now reject substring/all-options cheats. Saved screening curves are recomputed with the repaired validators, preserving each original label. See codex-review.md and review-audit-disposition.md in Scratch for completion limits and targeted rechecks.

Final cold-review bundle SHA-256: 66fb34756a977ebb0a0fc0c2905174a13cd84a1ba0b7762942178b0ad7d8829b. Metadata boundary probes, historical-score refresh, phone layout/accessibility and stable-ID resize checks passed. All review-owned browser/server ports are closed and the temporary host is removed. The audit remains explicitly partial; it was not repeated.
