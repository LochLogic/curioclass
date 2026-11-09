# Which Way Is Down? Build handoff

## Source map

src.html starts with the kit frame, responsive control desk and argument card. The script contains the school and test
place tables, line manifest, local save/restore, actions, responsive canvas renderer, orthographic projection and pointer/keyboard input.
land.json is loaded through the bundler's json token. It contains longitude/latitude rings recovered by inverting the
repository's Natural Earth Equal Earth map. All pictures use art tokens. The bundle works offline.

## Tricky parts

The angle convention is counterclockwise from screen right, with screen-down 270 degrees. Edge views preserve a school's
latitude and requested side. Claim gaps are three-dimensional analytic vector angles. Displayed dashed arrows are the
projection of each rule; the degree verdict is computed in three dimensions.

Physics integrates real elapsed time and changes speed continuously when Slow motion changes. Motion off holds the object
until its landing time. Test attempts are spent before animation or narration; another Predict cannot add another row.
The Strong status waits until the result sequence completes. Changing any evidence invalidates Fits and the current streak.
Restored test rows are historical and cannot restore a streak. An unfinished test resumes after mode changes, so students
cannot skip hard places to preserve a streak. Punctuation does not count as reasoning words. Start over preserves Globe kids.

## Spec decisions and contradictions

- The open people/sensitivity question takes the brief's permitted people option. All eight child assets have people:true.
  A fresh agent inspected the people sheet and yards. Representation, clothing and anatomy passed. Minor pose differences
  in Jonah's undershirt/backpack and Valentina's hat/scarf/backpack remain. The contact sheet is in Scratch for owner review.
- The initial Quito skyline added a statue and church spires outside the requested backdrop. An image edit removes them.
- Anchorage's numeric view longitude 120.1 E places it on the right under the usual orthographic convention.
  Use 59.9 W for its specified left edge. The parenthetical left/right longitude signs are also reversed.
  The other three numeric view longitudes and all four listed true arrow angles are preserved.
- The table rounds Moon/Mars gravity to 1.6/3.7, while its fall times use 1.62/3.71. Physics uses the precise values,
  shows the requested rounded table and states this in notes. Earth 9.81 follows Interactions; 9.8 is the rounded table.
- Inclusive 8-degree integer tolerance admits 16 settings for fractional true angles and 17 for integer true angles.
  Cairo admits 17; the other seven test places admit 16. The spec's 0.0088 percent three-guess figure is a close
  approximation, not an exact value for this mixed pool. No probability claim is shown to students.
- The rounded Sydney latitude gives a South Pole gap of 61.95 degrees, displayed as 62.0, rather than 61.9 in Sources.
- Claim texts are preserved exactly, despite the stated equal-length range. Cards have equal size and color and shuffled order.
- The model treats every school as mean radius 6,371 km. Real elevations, flattening and local gravity variations are in notes.
- The review resolves the result/Next place wording conflict with separate lines. The result finishes before Next
  enables; nextReady then names the enabled control. No result line now tells a student to press a disabled Next.
- The supplied four school locations represent towns/base, not verified individual school coordinates. The yards and pupils
  are explicitly described in notes as illustrations. No school names or pupil identities are invented.

## Sensitivity

Four fictional pupils represent Alaska, Ecuador, Australia and an Argentine research base in Antarctica. No claim about
Antarctic territory is made. No Indigenous identity is assigned from appearance or location. Fresh representation review
passed, with the minor pose consistency notes above. This is Build only; owner contact-sheet review remains before shipping.

## Engine changes wanted

None. The tool uses Curio.voice, Curio.init, Curio.wait, Curio.tone and Curio.yes without changing shared kit files.

## Build boundary

No commits, shared-file edits, deployment, paid art service or narration recording. Evidence, raw test scripts, frames,
art and people contact sheets and the mechanical audit are under _scratch/which-way-is-down/.
The full audit froze its own HTML before the final mode-resume, punctuation-count, minimum tab-width, partial-record
title, focus, 760-wide layout, reset-reveal and handle-only drag fixes. Focused final proofs cover those changes;
the full audit is a documented snapshot, not final certification.
The first audit-state drag fixture evaluated a point array without returning it. The published audit-states.json now
returns real drag points. The frozen audit did not reach its intended evidence/test states. The separate functional
runner did reach all four records and Strong using real pointer drags.

## Next review priorities

### Cold review repairs, 2026-11-06 to 2026-11-07

The short Record confirmation now leaves time for hNext/hZoom to start at a two-second action pace; sync runs before
the newly visible Zoom control is tested. A completed reveal queues the Globe how-to once. Argue entry checks the
number of available records, rather than the number already attached, before asking for more observations.
The first landing says "Straight down." so hMarkBtn can start before the next two-second tap. The plumb-line term
remains on the landing tag, in the diagram, the marking instruction and the teacher notes.
Test result speech does not name Next place while disabled; nextReady speaks after it enables. Strong speech uses
the reasoning gate too, and entering reasoning after the third hit can announce the newly completed card.
Predict moves keyboard focus onto the canvas, then to Next place only if the student has not moved focus elsewhere.

The feather tube was redrawn with the built-in OpenAI image tool. Its source prompt and content band are in prompts.json;
raw/wwd-feather-tube.png is processed with art.py --rekey. vacuumTube keeps the brass shell stationary and moves the
painted feather/apple band together inside it. Other worlds retains all its painted surfaces and gains shaded lane
frames, height ticks, contact shadows and brief landing rings. All moving additions stop with Motion off.
The radius label now says it belongs to the model. Notes link the independently checked geography sources.
At narrow widths six evidence choices use three columns; compact claim cards keep the hint in view. On phones the
school badge sits in the upper-right sky rather than over the child's face. The one-meter ruler has a dark backing
so the Antarctic snow cannot hide its white scale or label. These were checked at the actual affected sizes.
The review audit confirmed a landed-state speech bubble crossing the face at 1000x625. Bubbles now stay in the
left margin, with a separate phone height, and were rechecked in the landed states rather than only the opening yard.
The empty-notebook request uses the same how-to key for its welcome and card taps, once per Argue entry. Repeated
unrecorded-card taps therefore keep the hint available without nagging the same instruction as a fresh event.
The audit also found Go to Drop losing focus as its button disappeared. It now focuses Drop with preventScroll.
Passive yard/world/evidence pictures use role img and stay out of the tab order; only the interactive globe and
Mark/Test arrow expose an application keyboard surface. The label describes the actual mode.
The reveal's canvas arrows had escaped the default-screen calm audit. With Motion off they now hold their short
length through each 800 ms beat and appear extended at its end. Timing and narration order are retained; a pixel
stability check during an active reveal verifies that this is not merely the absence of CSS animation.
The old Pick a claim / Attach evidence headings now hide with their choices during Test, so the prediction controls
are not introduced by obsolete instructions. Laptop and phone prediction frames verify the resulting layout.
Removing reasoning after Strong also reverses the hint and interrupts an obsolete award announcement with the
missing-reasoning event. This is transition feedback, not a repeated how-to on every keystroke.

### Review cleanup limitation

The temporary host.html is removed and Chrome ports 9940 through 9947 are closed. Six verified Python HTTP listeners
remain on the assigned host port 8745: PIDs 6524, 44320, 44824, 47396, 49844 and 50820. Native process termination
returned Access denied under this permission profile. The server was verified by matching its served tool bytes to
the reviewed bundle before attempting termination. No elevation or policy change was attempted. Close these hosts
outside this permission profile before reusing 8745; see _scratch/which-way-is-down/review-host-cleanup.json.

The build's rapid browser-speech navigation concern was resolved in the cold review. The final two-second main path
heard hMarkBtn, hMark, hNext, hZoom, the three reveal lines, wGlobe, wArgue, hCheck, hTest and wWorlds.
Fixed recordings are not present and recording is outside this brief. Recorded takes will need their own timing check.
The test view resumes after mode changes. Start over clears the argument; it also resets X-ray/reveal state while
preserving added Globe kids. Reloaded test rows are deliberately historical, so a saved card must earn a fresh streak.
Globe rotation uses yaw and pitch, with pitch limited near the poles; it does not offer free roll.
