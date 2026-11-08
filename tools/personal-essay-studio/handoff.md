# Personal Essay Studio handoff

## Source map

src.html starts from the kit starter and uses kit:curio plus kit:theme-912 with the spec's light rose palette. Its sections are responsive styles, stable HTML controls, word/sentence analysis, persistence, editor mirroring, version diff, sequence board and handlers. content.json is loaded by the bundle token and holds the spec prompts, samples, lists and fixed voice lines. No network requests occur in the bundled tool.

The writing surface is a native textarea with an identically laid-out, aria-hidden text mirror behind it. The mirror draws sentence outlines, finder underlines and grey note text without rebuilding the input or moving its caret. Sentence offsets select the original text; lens answers are stored by sentence text. Note blocks remain plain editable draft text when their anchor changes.

Cold review fixes: changing the selected sentence reloads its own lens answers; Drop notes reveals the inserted block and returns focus to Draft. Editing reflection fields updates the ending preview. Any draft edit invalidates the opening preview; a source-text guard also protects application. Dragging or rebuilding the sequence clears its old preview. Jobs follow unchanged paragraph text across insertion, rather than drifting by index. Unicode words retain their complete spelling. Compare trims common prefixes and suffixes before its exact word LCS, and identical versions skip the matrix. Very long unrelated texts still have quadratic LCS cost.

The side panel comes before the workspace in DOM order, with explicit grid positions retaining the same visual layout. Its controls precede the ten Spark cards for keyboard users. currentHint restores the actual open revision, lens, finder or ending instruction when leaving the example. The post-card writing instruction and note handoff are now spoken once.

Audit-confirmed follow-ups: Add spark reveals/focuses its new checks, and completing both checks reveals Use this spark. A compact three-column panel layout at short landscape keeps the required half-height sheet usable. Ending and opening generation focus their visible application actions; opening previews scroll internally when long. Try this order reveals its preview and keeps the sticky application action available. hint() only interrupts for a not-yet-heard how-to, so repeated prompt taps cannot cut the same instruction and silence its remainder. Finder-off and completed checks hush only their obsolete active how-to; Read remains under the kit's priority rules.

At narrow widths, the same hint moves into a strip above the workspace. It also moves there while the desktop lens hides the panel. The native input remains stable. The phone lens scrolls its five fields internally and keeps Drop notes visible. In short landscape frames, all five questions fit across the bottom sheet. Sequence reordering moves existing DOM cards; job chips update without rebuilding the focused controls.

## Decisions and contradictions

- No open questions remain in the spec. Its settled ten neutral cards and prompt 7 wording are retained.
- The user's image-tool instruction overrides the spec's local FLUX method. Both requested photographs were made with the built-in OpenAI image tool. Both have people:false.
- The requested seven-line preview supersedes older memory notes about five lines.
- The user's instruction to stop when codex-report.md is written conflicts with CODEX-BUILD's early-report instruction. Evidence and report notes were accumulated in Scratch; the final report is written last and ends Build.
- The current Common App prompts page does not expose a current word-range statement in its readable text. The official available interface PDF is for 2025-2026. Following the spec's fallback, omit the generic college-limit claim and retain the 250/500/650/none picker.
- Recomputed sample counts match. Contrast ratios vary slightly: brand/paper 6.78, ink/paper 14.52, muted/paper 6.30, focus/paper 5.61. All meet AA for the uses here.
- Ten named versions are protected. When no unnamed version can be dropped, saving and destructive revision application stop with a clear instruction to unname a version. This resolves the unspecified all-named capacity case.
- Spark size ticks and read-aloud ticks are self-reports. A student can tick them without doing the thinking; they are labeled as the student's checks and have no score or verified skill claim. A private memory's time and place cannot be verified by this offline interface.
- At mobile widths the panel and lens use half-height bottom sheets. Long forms and the ten-card wall scroll, as the phone spec requires. The main mode controls remain visible.
- Done when 8 conflicts with the mobile sheet requirement at 680x425. A 212.5-pixel-high sheet plus header, privacy and hint leaves a paper region shorter than the sheet. The default Draft paper is the largest work region, and the selected sentence remains above the open sheet. The literal largest-region condition with that sheet open is not met.
- Revision tabs sit above the work so they stay directly reachable when the narrow panel becomes a bottom sheet. The open revision tool remains the sole main work area.

## Sensitivity

The original example names Mr. Ortega and makes flour tortillas in a community kitchen. Check that the fictional experience and images remain ordinary and respectful, without implying a universal cultural cooking method. Student prompts are neutral and do not solicit health, trauma or family conflict. No generated people are shown.

## Engine changes wanted

No kit engine changes. Shared kit and scripts were not edited. Existing Python lacks NumPy; the free art.py --rekey command was run with the existing S:/AI/tts/.venv/Lib/site-packages on sys.path, using the permitted Python executable.

scripts/audit_tool.py, Audit.steps, the `elif 'js' in s` branch: retain the return value of self.ev and surface an `audit_error` as a state-step failure. It currently ignores JavaScript syntax errors. The first sequence fixture contained literal newlines in a single-quoted JavaScript string, so that audit frame was empty. The fixture now uses JSON-escaped text; the working three-paragraph board is covered by direct tests.

## Art

art/prompts.json contains the full house style and prompts. Cold review redrew pes-kitchen-wide with the built-in imagegen tool to show the shared room and camera distance more clearly, preserving the warm photographic style and the strong tortilla close-up. The selected raw images are in art/raw and the free converter produced the two WebP files. Voice uses browser fallback via Curio.voice; calm-professor and every fixed line are listed for later recording. No audio was recorded.

The current bank maps calm-professor to Schedar and marks it kept. The spec's delivery style is retained in voice/lines.json.

## Evidence

Build evidence, bounded command runner, computations, screenshots, functional checks, voice walks and audit output are under _scratch/personal-essay-studio/. The bar tools were copied and bundled only inside Scratch to preserve the two-folder write restriction. No git commits or polish round.

The single audit reads its initial bundle snapshot. Later repairs are covered by targeted frames and functional assertions, not a second full audit. Two orphan test host processes caused the audit's original 375-pixel iframe failures. Their exact command lines were verified and both owned processes were terminated. Subsequent phone lens, panel and example frames pass. The host runner now terminates its own process handle and waits for exit.

## Cold review verification

The one review audit completed within 40 minutes: 32 mechanical leads, 41 inspected frames. The audit's initial 375 host failed because owned test-host processes survived cleanup; those exact processes were verified and closed. Do not treat the missing phone-audit rows as passes. Independent real 375 iframe checks and the post-fix Spark action check pass, with no horizontal overflow.

Confirmed audit fixes were re-shot only in their affected states at 1366, 680 and 375. Rapid repeated prompt taps now produce one uninterrupted how-to start. The complete main writing path was rewalked after the narration change; all mode instructions are reached in order through the applicable post-card instruction, with no student prose spoken and no console errors. Real whole-pixel pointer dragging correctly reorders paragraphs. The final inline file is 312044 bytes.

The complete finding list, named factual sources, spec conflicts and verification limits are in codex-review.md. Scratch holds audit-disposition.md, review-validation.json and all retained failed fixtures, screenshots and logs. All owned Chrome and host ports are closed, and host.html is absent. No kit changes or git commits were made.
