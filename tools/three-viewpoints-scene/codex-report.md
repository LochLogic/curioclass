# Codex report: three-viewpoints-scene
## Built
Built 2026-11-02 in S:/CurioClass-codex. Build only: no commits, branch changes or polish round.

Offline Devise, Tighten and Perform modes; all 40 line options; four partner offers; six beats; live tension/timing; four director checks; live-role cues; local saving and confirmed Reset. Uses the kit frame, Curio.voice, motion and tones. No family engine is specified.

Final bundle: 361,242 bytes (352.8 KiB), below 2 MB. No active remote references. host.html was deleted. All Chrome and host processes started for this build were closed. Source lines are at most 161 characters. No em dashes in the tool's text files.

## Numbers check
PASS. Independently parsed and recomputed the full catalog in Scratch before implementation. Forty options, 39 voiced options, silent offer 2 s, shortest 1.2 s, longest 6.0 s. No differences from the spec.

Passing scene tensions: 1, 2, 3, 3, 2, 0. Beat times with a 1.5 s turn pause: 10.1, 10.1, 10.9, 10.5, 13.1, 3.7 s. Total 58.4 s. Crowded beat example: 20.0 s of dialogue, 20.5 s including its default pause. A 30.0 s boundary also passed after adding a small floating-point tolerance.

WCAG ratios recomputed: ink/paper 14.407, ink/white 16.108, muted/paper 5.692, muted/white 6.364, brand/paper 4.945, white/brand 5.529. Selected-role hover now stays white on dark teal.

Evidence: numbers.json, functional.json (24 assertions, all passed), student-built.json, followups.json, phone-flow.json in Scratch.

## Feel check
Best moment: the turn gets a breath, all four checks become green, then the live cue becomes a large teal script card and the appropriate prop lights up. The student built the 58.4 s example through held clicks, rather than only loading a fixture.

Flattest moment 1: the early preview hid later beats, making scene building feel like searching through a form. Changed it to two rows of three, with 44 px plus controls and a curve that draws at the actual pixel size. Tighten now exposes a full first card in all six beats at 680x425.

Flattest moment 2: Ms. Dale's first painting added unrelated desk accessories and weakened the prop-to-role connection. Rejected it and redrew the single folding chair, clipboard and lanyard. The large cue, prop light and immediate edit tones make role changes visible.

A full twelve-cue student-path simulation completed in 48.2 s against the 58.4 s plan, with all three roles live and realistic delivery delays. This was a scripted reading/interaction check, not a classroom or by-ear trial. A separate phone run checked every live wait and completion, using rapid Done taps for state coverage.

Both bar tools were bundled into Scratch and opened before implementation. Compared the live-cue frame beside Beat Lab in feel-comparison.png. The painted stage and script desk hold their own visually while leaving the dialogue readable.

![Tool beside Beat Lab](S:/CurioClass-codex/_scratch/three-viewpoints-scene/feel-comparison.png)

## Done when
1. PASS. Devise board, Tighten curve and Perform cue are the central focus at 1366x768 and 680x425. Six beat headings, curve and Play remain visible. Dense card lists use inner scrolling.
2. PASS. The exact example produces four green checks and 58.4 s. The no-turn variant and a clash after the turn produce the appropriate amber message. See functional.json and student-built-green.png.
3. PASS. Real placements triggered offers at 3, 6, 9 and 12. Accept unlocks and places; pass stores; Offers reopens. Duplicate and full-beat guards passed. Playback hides offers until stopped.
4. PASS. Placement, Cut and pause handlers redraw synchronously. Tested the crowded beat, 0 and 3 s limits, reordered cards and pacing boundary.
5. PASS. A held card tap jumped to 5-Dale-a immediately; Stop cleared playback and queue. A pause change kept playback running. Token cancellation prevents stale continuations, and the jumped card becomes selected for subsequent edits.
6. PASS. All three live waits at each cue; Space advances. Mixed-role testing logged Ortiz and Dale as spoken while Maya waited. Phone real-input flow built all six beats, waited at each cue and reached the timing recap. The live cue was 32.8 px at 1366x768. Actual speech quality depends on available browser voices.
7. PASS for queue behavior. No narrator entries during character/live playback in checked logs. Welcomes/how lines use the kit's heard state; event IDs are explicit. Five-repeat audit checks were clean. Same-mode rapid taps no longer hush the welcome. Bank timbres are not verified because recordings are prohibited in Build.
8. PASS. Reload restored the board, pauses and a passing scene. Reset cancellation preserved work; confirmed Reset cleared board, pauses, offer answers and stored work.

## Wave lessons
- Hint and voice: PASS. Hints update immediately and name the next control. Read uses the hint. Empty Perform now directs the student back to Devise and cannot queue an unavailable Start instruction. The kit owns heard state, Read priority and sound-off behavior.
- Focus and layout: PASS with the documented dense-list limitation. Stable board signatures preserve card nodes during playback. Explicit focus changes prevent scrolling. Hints have reserved height; desktop hint and Play stay visible while secondary controls scroll.
- Sizes: PASS for the required primary controls. Checked all STANDARDS sizes, with 375 through an iframe. Read has a 44 px minimum; a complete 44 px card fits each compact Tighten beat. Further cards may need inner scrolling.
- No giveaways: PASS. This is an open devising exercise, with transparent rules and no concealed answer or score.
- Honest numbers: PASS. The speech-rate estimate is stated on screen. Live elapsed time and planned time are reported separately.
- Standards: PASS. Solo students choose character needs, develop Jules's offers, revise pacing, perform, and connect a viewpoint with their community through the Devise prompt. Notes explain each standard.
- Motion off: PASS. The audit found no infinite animation. Timing and live waits remain unchanged. Used art is real, with no placeholders.
- Short choice sets visible: PASS after repair. All seven phone picker options fit, verified by their rectangles and a real click on the offered seventh option. Compact offer response buttons both fit in view.
- Resize mid-animation: PASS in the audit. No exceptions or stuck controls across states and held-click resize checks.
- Welcome delayed after first action: PASS. No welcomeAfter. Opening a picker makes the slot instruction stale, so the welcome is skipped unmarked.
- Unknown shown as unknown: PASS. Empty beats are marked empty with outlined tension points.
- One look, one meaning: PASS. Character colors always accompany names; checks use a check or exclamation as well as color.
- Badges say what is true: PASS. Checks are computed from the exact exercise rules, with empty beats flagged separately. The allGreen spoken prompt also waits for every beat to contain a line.
- Hint changes back: PASS. Mode changes, Stop, Reset and dialog return restore the current instruction.
- No answer by copying words: PASS. The choices devise a scene; no diagnostic or quiz answer is exposed by wording.

## Audit leads
Ran audit_tool.py once with ports 9991 and 8795, inside its 40-minute limit. It completed with 223 repeated leads and 97 frames. The complete audit was not rerun after repairs. Focused follow-ups checked the affected paths instead.

- Read targets: fixed at 44 px minimum, measured at compact sizes.
- Add controls reported as 0 px text: intentional icon presentation. Their visible plus is a 20 px pseudo-element, their target is 44 px, and their full accessible label names the beat.
- Phone fold/overlap, missing picker steps and cascading missing line/cue states: fixed by reserving a separate transport area outside the main scroll viewport. Real phone input then opened the picker, placed all six lines, answered offers and completed six live cues. No cue/transport overlap remained.
- Phone board controls below the fold: retained as the specified vertical list, now within a scroll region. They are reachable by normal scrolling and keyboard focus. A single phone screen cannot display the entire six-beat board.
- Abbreviated card text: intentional. Full text is in the title, selected-card panel, picker and live cue. Added explicit text-overflow to identify the designed ellipsis. Dialogue content was not removed.
- Offer buttons below a compact panel edge: fixed by moving the offer above secondary editing controls. Both response buttons measured fully in view at 680x425.
- Tighten card viewports too small at 1000 and 760: enlarged/rebalanced the board and hid Add in narrow Tighten. Final first-card measurements: 44 px card inside 59 px at 1000, 84 px at 760, and 49 px at 680. Multiple/dense cards still scroll.
- Compact hint scrolling away: desktop hints and Play now stick within the panel. Final checked hint rectangles remained in view at 1366, 1000, 760 and 680. Phone hints can scroll away with their introductory panel; Read and transport remain available.
- Reset or editing controls past a panel edge: secondary controls retain panel scrolling. These are not a hidden short set of answer options. Offers and core playback controls take priority.
- Underlay text reported hidden by reset/offers dialogs: intentional native modal behavior; the background is inert and the dialog supplies the current controls.
- "1 arrives" grammar lead: false positive. This is the numbered label "Offer 1 arrives", not a plural noun error.
- Slot-first welcome not heard: intentional stale-line handling, as the spec makes that welcome stale when a slot is tapped. Picker instructions are shown immediately; no late welcome interrupts the new action.
- Rapid same-mode welcome cuts: fixed by preserving the current mode's speech instead of hushing it again. Follow-up log contains one spoken welcome with no cut.
- Controls moving on a mode switch: expected layout/focus change. Initialized Sound with its kit icon to avoid its first label-width change. Sound off cutting speech is expected kit behavior.
- Motion off, resize exceptions/stuck controls, held-click keyboard checks and five-repeat voice checks: clean in the completed audit.

The audit's original 223 count is not presented as a count for the repaired bundle. No full post-repair audit was run.

Harness notes: two early selectors containing quotes failed in drive.py and were retried with unquoted attribute selectors. An outer test host favicon request returned 404; later host frames use a data icon and have no errors. These were not tool JavaScript exceptions.

## Frames looked at
Looked at both bar frames; three early layout frames; seven functional frames; keyboard, voice, live-wait and full-live frames; all twelve size frames; eight targeted frames including grayscale, seven-option picker and 24-card crowding; all 97 audit PNGs through 17 contact sheets; six focused repair frames; final Tighten frames at 1366, 1000, 760 and 680; same-mode, spacing, compact-card and hover checks. Inspected all four finished images and the rejected/replaced Dale candidate. Evidence stays in _scratch/three-viewpoints-scene/.

## Art made
Four used generated illustrations, 202,982 bytes (198.2 KiB) in WebP. One Dale redraw. All three cutouts rekeyed with despill through the free art.py --rekey path. Full prompts and raw originals retained. No people in the used art.

## Art still to paint
None. Browser speech is a separate limitation, not missing art.

## Engine changes wanted
kit/curio.js, speakOne and Curio.voice item options: allow a supported optional role/bank voice selector per line while retaining queue cancellation and Read priority. No kit files were changed. Details are in handoff.md.

## Left open
- No bank recordings, by Build instruction. Browser voice quality, distinct role timbres and actual delivery duration need a later by-ear review.
- Dense and compact multi-card beats use inner scrolling. The cold review should assess that tradeoff, especially four-line beats at 680x425.
- Phone board/hint content requires vertical scrolling. Main transport and live Done/Back are kept outside that scroll region.
- The completed full audit predates the focused repairs. A cold reviewer can run a fresh audit; this build did not start a polish round.
