# Choreography Board build handoff

## Layout and data
src.html starts from the kit starter structure and uses kit:curio and kit:dance. Styles, movement data, devices, persistence, voice, sampling, stage rendering, playback, editing and UI wiring are in that order. The panel appears before the timeline in DOM order for keyboard access. The theater and floor are laid out in real pixels on resize, with a cover-cropped 1600 by 900 painting.

The painting's floor seam is y 59%, front contact limit y 94%; the cyc is x 22.3% to 77.1%, y 9% to 59%. fitView recomputes its crop and the floor projection together. All theater art uses art:cb-blackbox. Art prompt, source and placement geometry are in art/prompts.json.

## Tricky parts
transformFrames applies Level, Size, Dynamics, Mirror and Retrograde. sample maps time through Tempo, Repeat and per-dancer Canon delays, holds completed dancers and walks formation changes for two counts. Dance.phrase interpolates keyframes; Dance.clock and Dance.play own time. Compare attaches two play handles to a single clock, using the current track. The composed phrases map per-block canon offsets because canon can change on every block.

History is capped at 40. Undo and Redo move the current pointer. An edit after Undo appends, preserving intervening versions. Reasons annotate versions directly. All persistence is wrapped in try/catch and uses choreography-board. Clear saved returns to a fresh unsaved starter; the next edit enables saving again.

Line spreads dancers across the floor instead of putting neighboring outstretched arms through one another. Three and four dancers use a smaller presentation scale; Cluster deliberately overlaps. These are presentation choices, separate from the Size device, which changes joint reach and travel. Future paintings must preserve this spacing and floor contact.

poseFor preserves already-low floor shapes and raises floor phrases onto the toes for Higher. The generic kit modifier alone can fold an already-low shape past its support or label a lying figure High. The local workaround keeps the level readout meaningful.

All repeated refusal events get unique queue keys. This prevents the shared queue from replacing a still-waiting identical event during two-second taps. How lines retain stable keys and speak once. Read stops music before reading. The final five-tap refusal check recorded all five events starting.

The four backing tracks use the shared engine's synthesized instruments. Storm's low drum and string-pad colors, and Strut's snap sound, are synthesized approximations, not recordings.

## Painted dancers after cold review
Owner's final direction is implemented. art:cb-dancer-cast is three people:true atlases: four upright articulated dancers front/back, plus seven complete grounded/bending poses for each dancer (curl, kneel reach, crouch, sit, lie, roll, bow). These replace the unmade 56-pose plan. Whole-body poses are selected by groundedKey and registered in groundedPoses; upright joints remain in addPaintedRig. Atlas images are shared SVG references, avoiding repeated base64 strings in cached icons. addPaintedRig uses clipped affine pieces registered to Dance's screen joints, so all existing transforms, timing, facings and levels remain data driven. paintedRig holds the atlas URL, dimensions and registration. createPerformer, paintPerformer and paintIcon remain the swap boundaries. Ghost uses faint painted-silhouette outlines. Unique clip IDs are essential when cached icons repeat.

Fresh people-art check: _scratch/choreography-board/people-review.md. Source representation passed; initial neck and cached-thumbnail registration issues were fixed and the same reviewer confirmed the scoped repairs.

Build sections are persistent Devices, Cast, Phrases and History views. Compact screens use native short-set pickers. The editor shows one move group at a time. Audit states include the section navigation; do not target hidden controls directly. Show's closing title includes phrase/count/device choices. Push now has extended arms, and Leap across alternates running legs.

## Open questions resolved
The spec leans toward hero-coach (Puck), so the voice manifest uses hero-coach. No recorded voice was created, per Build-only rules; browser speech is the fallback.

The move list says four groups but names five groups. All five named groups and all 24 listed moves are included. No moves were dropped.

## Engine changes wanted
- kit/dance.js, floor.draw: add explicit options to suppress the stage background, floor fill and curtains. The tool currently clears those layers after each resize to align the painting.
- kit/dance.js, level: give crouch, sit, lie and roll native low variants. Applying the generic low modifier to an already low floor shape bends it past its support. poseFor works around this locally by preserving those native floor shapes at Low.
- kit/dance.js, level: give floor shapes meaningful high variants that rise from the floor. poseFor supplies an upright tiptoe version locally.

## Next
The cold review is documented in codex-review.md. The owner requested complete paintings for low and waist-bent poses; those are implemented. See codex-report.md for actual verification and remaining limits.

## Build verification and audit dispositions
The full mechanical audit ran once and completed: 461 leads, no console errors, no resize exceptions or stuck controls, and no infinite Motion-off animation. Its 81 frames were inspected in eleven contact sheets.

The original audit is in _scratch/choreography-board/audit/audit.md. dispositions.json beside it answers all 447 listed bullet rows and the additional walk warnings. Most retained rows describe secondary controls below the fold in the required stacked layout, the intentionally scrolling timeline, or an intentionally covering confirmation dialog.

Fixes after that audit: explicit input labels; a fixed transport/hint head above a separate scrolling authoring body; editor scroll reset and Try focus; keyed history focus; sensible focus after Show, Save, placement, deletion and history boundaries; inert modal background; persistent phrase/timeline controls; no stale device instruction in Compare; no welcome cut on repeated taps of an active mode. Targeted post-audit frames and browser logs verify those corrections. The entire mechanical audit was not rerun.

Long authoring panels still require vertical scrolling on 375 and 760 wide screens. The eight primary device buttons and Play fit initially; all 24 palette moves and the whole history/library cannot fit beside a large stage. Advanced device options and secondary controls remain a cold-review ergonomics question.

The build-time bundle was 298171 bytes. Cold review added the three painted cast atlases; see codex-review.md for final size. The host page was removed and every Chrome/server started by the build was closed. Recorded voice remains intentionally deferred; painted dancers were completed during cold review.

## Whole-body pose registration
Dedicated low and bending paintings preserve natural anatomy instead of warping an upright torso. There are seven core poses per dancer, used on count boundaries; upright poses retain continuous joint interpolation. The fourth bow cell is mirrored once to correct the source prosthesis side, and fourth-dancer whole-body sprites do not mirror their physical prosthesis with the Mirror device. The other dancers demonstrate the side change. Further facing-specific floor illustrations could improve fidelity.

## Cold review verification (current)
The single cold-review audit completed with 113 grouped leads and 97 inspected frames, using Chrome 9931 and host 8735 with a 40-minute limit. No console errors, infinite Motion-off animations, resize exceptions or stuck controls. All held-click focus/Enter paths and all speaking-control repeat/quick checks passed. Dispositions: _scratch/choreography-board/review-audit/dispositions.json.

Confirmed fixes after that audit: separate Before, Measures and Reasons views in Compare; collapsed version lists explicitly hidden; compact reason picker; compact Device and Device option pickers; preserved option focus; tab-specific hints and speech validity. Native compact choices expose every option without scrolling a short choice set. Stage and Play remain in view. Updated audit-states include these paths.

Targeted checks passed at all eight Compare sizes and selected Reasons/device sizes, including a 375-wide iframe. Twenty latest layout inspections leave only intentional proportional timeline scrolling. Reasons and notes survive reload. Returning to an identical Before still records a new version. Clear saved removes storage and returns focus to Play. Empty-stage guidance names Phrases. The 31 fixed voice lines exactly match allLines(). The full audit was not rerun after these scoped repairs.

People-art review passed for all three cast atlases and the grounded stage frames: _scratch/choreography-board/people-review.md. The real Lie palette path also updates its count thumbnail. The final offline bundle is about 1.77 MiB. No kit changes, git commits or deployment. All test Chrome/server processes were closed and host.html removed.
