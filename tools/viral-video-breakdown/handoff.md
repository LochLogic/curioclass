# Viral Video Breakdown build handoff

## Structure

src.html starts from the kit starter and retains its kit stylesheet, script, modes and shared controls. Tool CSS lays out at actual viewport size. Content tables are SHOTS, CARDS, CAPTIONS and NINA. Rendering, playback, evidence, claims and verdict logic follow those tables. All student text is escaped before insertion. The built HTML embeds every asset.

The case has no family engine. Curio.voice owns narration, and the Curio Class kit supplies motion, sound settings, the audio context and tones. Noise effects are original synthesis through that shared context.

## Decisions and ambiguities

- The user requires image-tool artwork. The spec's local FLUX preference is superseded by that instruction; all eight paintings use OpenAI gpt-image, with people:false.
- The original is called a 5 a.m. video while its caption says Grandpa gets up at four. Both are retained: waking and baking can occur at different times.
- The final graphic has no shot size or angle. The label controls offer graphic and n/a on shot 8 rather than require a false camera label.
- Four frames need a frame rate, which the spec leaves unspecified. Assume 30 fps, so the inherited sticker edge is present for 0.1333 original seconds. Scrub at 0.00 s to inspect it.
- The spec asks for voice/lines.json and says not to record. All 14 lines are listed for curious-librarian/Aoede; browser speech is the current fallback.
- The copy tree is a student hypothesis, not a scored check. An earlier but wrong parent can be drawn; claim proof still needs the specified evidence pair and types.
- A claim attaches exactly two findings. This prevents a pile of unrelated clues from counting as proof; adding a third requires removing one first.
- Music waveforms are illustrative envelopes of the synthesized tracks, explicitly labeled. R5 is aligned in original time, with its shorter clip time shown separately.
- The tiny preview cards show five caption lines with an ellipsis. The full caption is in the title and in the Captions comparison. This reserves room for the six cards and the tree together.
- Miniature film graphics are proportionally scaled and presentational. The card's accessible name includes the full account, caption and views. Compare contains the readable full-size watermark, stickers, banner and logo.
- At phone width the verdict list scrolls above the closing chips. The closing chips and Copy remain on screen; all five verdict records remain in the list.
- Repeated refusal and claim events use immediate kit narration so a prior how-to cannot swallow them. Read first stops content and updates the hint to the stopped state.
- Choose findings opens a three-column picker. Up to twelve saved chips fit without scrolling at 680x425; longer evidence collections scroll. The panel lists the two attached findings after the picker closes.
- The compact header keeps Reset and the device-only privacy notice visible. The phone header has a small device-only notice beside its title.
- Fairness is open judgment. Copy remains available for drafts and explicitly labels missing calls or reasons, with no completion award.
- No open-question section appears in the spec. Unattended choices are documented here rather than sent as questions.

## Sensitivity

The case concerns a fictional 13-year-old maker, a grandfather and misleading commercial use. No people appear in the art. Review the false RIP caption as misinformation, not as a true death announcement. Permission and credit are discussed as ethical factors, without presenting this exercise as a legal fair-use ruling. Review the bakery setting for ordinary, respectful representation of family work.

## Engine changes wanted

No kit change. Shared audit suggestion only: in scripts/audit_tool.py, Audit.steps, surface the audit_error returned by Audit.ev for a failed custom JS step and stop that state, instead of continuing into misleading focus/disabled-control leads. The reviewer did not edit shared scripts.

## Art still to paint

None. All eight requested images are present. Prompts, generation credit and people flags are in art/prompts.json; originals are in art/raw/.

## Evidence

Build evidence, number recomputation, art contact sheet, bar-tool copies, commands, frames and mechanical audit live in _scratch/viral-video-breakdown/. See codex-report.md for final check outcomes and limitations. No shared files, commits, branch changes or polish round are part of this build.

## Cold review changes, 2026-11-07

The reviewer played first, then read this handoff. Claim nudges now describe the observation to make instead of supplying exact answer-pair recipes. The eight-checked event describes inspection rather than claiming mastery after wrong labels. Laptop verdict rows put call and reason beside one another, and the closing card echoes the student's selected obligations. Short landscape hides that extra echo to keep Copy visible. The crust painting was redrawn with a tighter, blistered outside surface in the existing amber/blue style, through the imagegen skill; its full prompt is in art/prompts.json and its raw image remains in art/raw/shot-crust.png.

The final audit confirmed a narrow via-sticker/annotation collision, a clipped compact claim button, undersized summary timings and phone watermark text, and a clipped phone end-card name. These received local layout/type repairs. The opaque summary now makes covered film controls inert, closes the old note, and returns the phone to the top; visible label actions return to the film. Back to film focuses Play. Copy clears stale status after edits, identifies drafts with no closing choices, and gives a selected read-only fallback that remains usable in the phone's scrolling panel.

Two added audit-state scripts incorrectly assigned both selector values before dispatching Change; the first event reset the second selector. Their setup is now sequential and duplicate state names are removed. Affected states received focused drive checks after the single audit; the full audit was not repeated.

There is a remaining assessment blocker: opening the two specified evidence tools and cycling card choices can produce a supported claim without explaining the evidence. This was reproduced through the UI, not inferred from code. The spec explicitly awards clue chips on opening and defines the check as card plus two clues. Requiring an independently interpreted observation or explanation would add a response mechanic, so the reviewer left that change open rather than altering the spec. Teacher notes now state the limit. Do not use supported-claim counts as mastery scores.

## Test harness notes

Keep the tree SVG as a block with a fixed 60 px phone height. Its auto-height layout initially fed back into ResizeObserver; the final phone height remains 346 px across a five-second stability test, with Draw arrow fully visible. Voice-over captions belong only to shots 1, 2, 6 and 7, matching their Sound entries.

The single audit finished with 169 leads on its pre-fix snapshot. Geometry, singular finding counts and repeated-mode welcome cuts were fixed with targeted checks. The phone audit did not attach to its iframe. Three orphan drive.py host processes sharing port 8785 were found during final cleanup; a port collision is a likely cause of that attachment failure. They were terminated only after their exact tool and host-port command lines were matched. A clean, separately hosted final phone run passed all three modes and the finding picker.

The scratch responsive helper now closes the actual matching host children rather than relying only on the launcher's PID. No shared scripts were changed. All assigned ports were checked closed before the final report. The audit was not rerun, following the one-audit instruction. Full lead dispositions are in _scratch/viral-video-breakdown/audit-dispositions.md.

The final phone claim view compacts the selected case card and hides the investigation tree while attaching evidence; Make the claim ends at y749.7 in a 375x812 viewport. The footer remains reachable by normal document scrolling. Reset now resynchronizes the visible mode, timeline, selectors, feedback and copied output. Retapping the active mode preserves its welcome instead of restarting it.

The final summary hint-only reshoot failed by CDP timeout and then connection reset. Its earlier layout and full student path were captured. A separate final caption capture timed out; the exact source renderer was checked in Node instead, confirming caption presence only on shots 1, 2, 6 and 7. Neither failed capture is claimed as a visual pass.

## Cold review validation, 2026-11-07

The separate cold-review audit completed once with 154 leads and 100 frames, with no console errors, resize exceptions or stuck controls. Its full lead register is _scratch/viral-video-breakdown/review-audit-dispositions.md; this supersedes none of the historical build audit records above. Focused repair evidence is in audit-fixed/ and phone/, with current JSON geometry and voice-event logs alongside. The 680 summary is reachable by scrolling to How it works; Back restores Play, and covered controls are inert. The corrected ad-trace fixture displays R3 and R5, and the supported-claim fixture reaches all three accepted claims. The claim-guessing blocker remains open.
