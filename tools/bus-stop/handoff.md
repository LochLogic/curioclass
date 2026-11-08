# Bus Stop handoff: Curiosity fix round 1

## Current structure
The current source uses a full-width painted scene, working counter chart and bus dashboard. It uses kit JavaScript
for voice, tones and Motion/Sound/Read, with its own CSS and controls. No kit stylesheet, header or right-side lesson
panel remains. The lower-left Manual has a closed topic index, sources/licences and keyboard focus return.
New road stays reachable in the console on phones. Read always repeats the current story/action; card Read buttons
temporarily supply their own sentence to the same kit Read mechanism. At most one first-use hint speaks automatically.

Drive, Split, Express and Fill up retain state in memory. Fill up temporarily swaps in its own bus object and restores
the Drive object when leaving. Its shuffled bag covers starts 1 through 9 across the first two five-bus sets.
Express mixes two or three additions per five-story set and advances rider identities. Before reveal its counters
are plain starting riders; leavers wait facing out at the open door. Reveal has one walk, then static end positions.
Ten-stop/Fill-up redraws retain boarded riders as hidden, avoiding a second walk or reappearance after a mode switch.

The occupied-seat count selects solid/new objects; Ten feedback selects new counters; School selects gone rings.
Full cups retain focus on Done even under repeated pointer presses. Full hints describe the current full bus; partial
Ten hints identify the starting seats as starting seats. Split records ordered pairs and uses its last kept way on a
ticket. Five fixed columns and responsive areas preserve 60 px discs, except the explicitly allowed 44 px preview.
Resize handling responds to both height and width changes.

## Curiosity precedence
The user explicitly classified this as a Curiosity. No welcome, grade, goal, score, level, finish screen or quiz layer
was added. Drive on does not require two recorded ways or a chosen card. School returns to the fork; Express and
Fill up continue into fresh sets with rolling recent tickets. The inherited sentence/number exploration is optional.
The older spec's teacher flow, automatic narration and ending instructions yield to CODEX-CURIOSITY.md.
No Bus Stop plate number exists in the spec or Curiosities catalog. The plate is deliberately unnumbered and metadata
has plate=null. Assignment remains for the owner; do not invent a number from another Curiosity.

## Real material and art
content.json contains all original routes and all 25 Express facts. Stories, data and original illustrations carry
the project's CC BY 4.0 content licence; code is MIT. The Manual and tool.draft.json name these sources and licences.
The CCSS/SAP links are curriculum references only; their text or examples are not bundled as open data.
The ten-seat bus and all places are explicitly fictional. All arithmetic is independently checked in Scratch.
All existing painted assets are retained. No new painted images or recordings were generated.
Six of the 16 active scene images have differently positioned sign faces. The tool maps each face in image
coordinates and pans the scene to retain it; Scratch sign-coordinates.json records the source and measurement method.
Foreground road/curb drawing keeps wheels and riders grounded without covering the right-hand sign.

## Evidence and maintenance
polish.md is the current item-level report; refine.md and refine/ are unchanged. Earlier build/review reports are
history. Scratch contains original-src.html, before/, proof/, polish-proof/, extra/, final-frames/, phone/, post-audit/,
sign-proof/ and the one fix-audit/. Audit contact pages/index cover all 75 mechanical frames.
The one audit finished, followed by focused repairs and frames. Its original 166-lead report is retained rather
than overwritten. polish.md resolves the real leads and explains preview/modal/description false positives.
number-check.py is a repeatable independent arithmetic/syntax extraction check. manifest-sync.py regenerates the
voice manifest from the current constructors without changing source. bundle.py is time bounded and saves its log.
Historical mutation helpers in Scratch were single-application edits; do not rerun them on the final source.

## Sensitivity
People art was not redrawn or assigned new identities or stereotypes. Its original varied rider set and provenance
remain. This fix does not claim a new independent representation review or a recorded-clip listening review.

## Engine changes wanted
None. No shared kit, script or document was edited.

## Left open
The maker's plate number is unassigned. Existing browser speech is used until the separately authorised recording
stage; no clip-quality or offline recorded narration claim is made. See polish.md for the exact checked limits.
