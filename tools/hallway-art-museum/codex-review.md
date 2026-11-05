# Codex review: hallway-art-museum

## Played

Played cold as a K-2 learner: five picks with reasons, unsuitable homes, heights, Kid eyes, all 15 checks, and all eight role prompts. Strong tactile art and a clear child-height reveal.
## Findings fixed

- Blocker, general, dialogs: the modal made header Read unreachable. Added in-dialog Read to artwork, checks, and confirmation; verified held clicks, keyboard, Sound off, and interruption.
- Should fix, general, artwork cards: reopening gave only a description. Cards now show and narrate the next action; Read uses registered parts rather than unmatched combined text.
- Should fix, general, fifth pick: its event could be dropped by the reason tap or direct students toward a modal-blocked mode. It now speaks after closing the card; five-piece guidance survives mode return and Keep it.
- Should fix, general, height feedback: a low pedestal said Slide it up despite having Low/Middle/Tall controls. It now names those buttons; limit hints name the enabled arrow and boundary focus follows it.
- Should fix, general, keyboard: height preceded homes. CSS grid preserves the scene while DOM order becomes tray, bays, homes, height, bar.
- Should fix, general, empty Opening day: Guide/Visitor asked about nonexistent art. Occupied art is selected on role entry when possible; empty bays give usable next actions.
- Should fix, general, compact ruler: eye callouts crowded each other and tick numbers. Compact callouts use two lines and separate eye markers; only colliding tick numbers are suppressed, with all marks retained. Phone estimate text is visible.
- Should fix, general, ribbon: the decoration intercepted bay taps and covered the phone ruler. It now accepts taps through it and clears the ruler and art, including compact views. A real tap through the ribbon successfully swapped pieces.
- Should fix, general, rapid mode taps: re-entering the active mode hushed its only welcome. Active-mode taps now preserve the playing line; both quick-tap cases passed with one uncut welcome.
- Polish, general, checklist: Read and Back to wall could scroll away in a short preview. The checklist header now stays visible. Dismissing Start over also stops obsolete speech.
- Polish, general, empty-bay narration: guidance is a once-only how-to, remains uninterrupted on repeated empty-role taps, and gives way to the relevant prompt when returning to occupied art.
- Polish, general, flattest moment: Next piece only changed a faint glow. A gold artwork label and brief bay emphasis connect each role prompt to this class's piece, with no added score or topic.
- Polish, general, weakest art: the pointer resembled a rolling pin. Redrew a slender wooden pointer in the existing gouache style, retaining all 22 assets. Fixed the compact ticket-label overlap.
## Findings left

No known blocker or should-fix remains within the completed checks. Polish, general: recorded narration is absent under the no-recording rule. Full mechanical verification remains incomplete as detailed below.

## Flattest moment left

Opening day's second prompt is still a quiet invitation to speak or act. This is the specified class roleplay, now anchored to a named, highlighted piece; it has no automatic judgment.

## Graphics

All 22 finished assets inspected on contrasting sheets and in play; no people, missing tokens, or style mismatch found. Kept the cart, tactile artworks, room, display supports, and Kid eyes reveal.
Redrew S:\CurioClass-codex\tools\hallway-art-museum\art\guide.webp with the built-in imagegen tool. Full house style and revised guide prompt are in art/prompts.json; free rekey includes spill removal.
Art: 714,042 bytes. Bundle: 1,034,963 bytes (1010.7 KiB), below 2 MB. Both existing bar-tool bundles were opened without modifying their folders.

## Audit

**Audit not finished.** The one audit stopped at its 40-minute limit, Chrome 9931, host 8735. Partial report: _scratch/hallway-art-museum/review-audit/audit.md; 77 saved frames, all inspected, and 71 aggregate leads.
Confirmed lead groups fixed: ruler crowding, ribbon interference, and the two cut mode welcomes. Removed the manifest's global #hint keep-region because native dialogs intentionally cover it; dialog controls retain their own keep-regions.
Other groups: pointer-transparent callouts remain visibly drawn despite hit-test leads; text behind native dialogs is intentionally covered. The 16 first-tap welcome leads are expected under STANDARDS: an action that speaks its own line skips the welcome, unmarked. Plain stage/key taps and Sound re-entry were separately checked.
Completed audit stages: all sizes, listed states, Motion off, control walks, and the ten repeat/quick-tap cases saved in the report. The full stress stage did not finish; its partial "clean" rows are not coverage. The default Set up probe is gated; listed real-input states cover the actual hallway.
Only repaired areas were re-shot afterward. No ruler-label collisions, small controls, ribbon/art overlap, or ruler/ribbon overlap occurred at 680, 800, 1366, and 375 iframe widths. Scrolled checklist controls stayed visible; ribbon taps passed through. Nine focused resizes during ribbon, height, and Kid eyes animations passed with no runtime errors. This is not a rerun or completion of the full audit.
Independent checks: 84/84, including all 60 home pairs, band boundaries, centers, clamping, themes, swaps, and window reset. Recomputed angle 16.2602 degrees, 57 inches 144.78 cm, and all four contrast ratios match the spec.
All seven desktop sizes and the 375x812 iframe were inspected in all three modes; measured controls remain at least 60 px and above the fold. Motion off, grayscale, keyboard, real jittered dragging to 105 cm, 40/200 cm limits, long cards, empty bays, and pedestal notes were inspected.
Voice inventory: 63 exact lines. Held clicks at 2-second pace: reason how 1/1, repeated description 5/5, role event 5/5, re-earned ribbon 2/2, fifth-pick event 1/1. Read interrupts, works with Sound off, and releases on mode change. No tool console errors or external resource requests; the temporary host's favicon 404 is unrelated to the bundle.
Wave lessons: next-action hints, Read, stable focus, visible short choices, honest badges, unknown empty bays, calm motion, and scoped welcomes were checked. This is a transparent builder, with no hidden-answer meter or word-matching quiz. Full stress coverage remains the audit limitation above.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Reason guidance | how | 1 | 1 |
| Piece description | event | 5 | 5 |
| Guard prompt | event | 5 | 5 |
| Re-earned ribbon | event | 2 | 2 |
| Fifth pick | event | 1 | 1 |
| Empty-gallery guidance over ten taps | how | 1 | 1 |
| Choose welcome over two quick taps | welcome | 1, uncut | 1, uncut |
| Opening welcome over two quick taps | welcome | 1, uncut | 1, uncut |

## Left open

Recorded narration is absent and may not be recorded in this review. Browser fallback needs a classroom listening check; no real classroom, smartboard, Safari, or Firefox trial occurred.
The art remains enlarged for legibility, as documented in notes/handoff; numerical center heights are authoritative. This is not a scale-measuring activity.
All four standards have direct activities: collection selection, material/height preparation, museum jobs, and reasons for inclusion. Notes retain the required three opening sections.
Evidence: Scratch cold-frames/, review-sizes/, review-special/, review-final/, review-voice/, post-audit-frames/, numbers-review.json, mechanics-final.json, voice-counts.json, resize-recheck.json. One pass; no shared source edits, git commits, or second audit. All started Chrome and host processes were closed; host.html is absent.
