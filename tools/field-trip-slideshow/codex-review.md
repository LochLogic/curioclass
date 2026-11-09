# Codex review: field-trip-slideshow

## Played

Cold K-2 solo and teacher/projector paths completed before reading builder notes or source. Comparing paintings and
watching the room become usable are strong. Rehearsal and the full eight-slide presentation were played.
One review pass, scope kept to this tool and Scratch, no commits. Evidence is in _scratch/field-trip-slideshow.

## Findings fixed

- Blocker, general, Sound: an interrupted loud test followed by Softer twice granted readiness. A complete six-second
  Sound-on test at one unchanged level is now required. Changes still alter live gain immediately; re-test to confirm.
- Should fix, general, Camera: old-animal praise played against the next animal without identifying the saved slide.
  Feedback now begins "Slide N saved" and the take screen labels the saved subject separately.
- Should fix, general, Room: correct intermediate settings had only a chime, leaving non-readers without spoken state.
  Added setting events, with validity checks; the final ready event remains distinct.
- Should fix, general, sources: BBC WHP 324 does not establish the numeric threshold attributed to it. Notes now
  distinguish illustrative gain and room settings from measured intelligibility and AVIXA compliance.
- Polish, general, Speaker: the flattest moment was passive text-to-picture tapping. Wrong captions visibly return;
  correct ones arrive with a warm stamp. Calm keeps the feedback without motion. Practice events cancel stale speech.
- Should fix, general, Room frames: the screen stretched vertically in portrait layouts. Projection and screen now
  preserve the painted fabric's proportions as the stage resizes; all seven non-phone sizes and the isolated phone recheck pass.
- Polish, general, art: redrew the green-fringed screen-down prop, with richer wall brackets, fabric and metal detail,
  and aligned the live projection with its surface. Preserved the twelve-image style and large paintings.

## Findings left

- Blocker, general, spec conflict: Camera's prescribed pre-use feedback, Sound's prescribed faces, Speaker's immediate matching
  feedback, and Room's prescribed defaults/checks permit answer-following or trial-and-error completion. See Break it.
  Preventing these shortcuts requires changing the specified learning/assessment design; no new quiz was added.
- Should fix, general, voice: no fixed recordings exist, so the requested Charon voice is not delivered. Recording is
  forbidden in this build/review brief. Browser speech works, but acoustic balance and clock-based word highlights
  cannot be certified as synchronized or calibrated.
- Should fix, general, standard scope: MA:Cn10 is not independently established by a fixed fictional aquarium trip.
  Notes ask the teacher to connect an actual shared experience; a deeper fix needs a spec or catalog decision.
- Polish, general: portrait Camera letterboxes heavily. Three simultaneous takes and 60 px controls were retained.

## Break it

- Camera: repeat A for all six and sweep A/B/C while always keeping the last take fail. Adaptive search using only the pre-use notes passes.
- Sound: held-click Test, switch mode, return, Softer twice passed before and fails after. Cancel-then-sweep fails.
  Muted testing and last-second level changes fail. Full steady tests pass only at levels 1-3; re-testing works.
  Reading the prescribed face then waiting out a steady test still passes without demonstrating listening skill.
- Speaker: every sentence against every picture, then We practiced, passes before and after. Self-report practice
  cannot establish actual speaking without violating the no-recording rule. Wrong matches never persist as correct.
- Room: one tap on each of the five initially wrong toggles passes. This is mandated by the spec's defaults.
  Repeated cycling changes the actual room, not a stored score. All 108 combinations tested: only the two specified setups pass.
- Rehearsal: no separate score or best score; rows derive from current crew states. Present and End show work even
  unfinished, as required. New show confirms; Keep it preserves work and reset clears every job. No reflection gate exists.

## Voice walk

Held 120 ms clicks, two-second action pace with full listening pauses: Camera, all six clear takes; Sound, loud test,
Softer twice and a full re-test; Speaker, six matches and practice; Room, all five toggles; Show, rehearsal and Present.
The first connection dropped; one checkpointed retry completed with four ready crews and zero runtime exceptions.
Spoken order: wCamera, per-take notes/saved events, cameraDone, wSound, sample, loud result, softer, sample, clear result,
wSpeaker, card/match events, allMatched, practiced, wRoom, four setting events, roomReady, wShow, ready, six captions, end.
All five mode how-to welcomes started exactly once. hTake and hPicture each started once. No late mode welcome.
Voice log and six frames: voice-main/result.json and voice-main/*.png. Side path: five card events spoken, hPicture once.

| Line | Kind | Expected | Started |
|---|---|---|---|
| Mode welcomes | how | 1 each | 1 each |
| hTake / hPicture, main | how | 1 each | 1 each |
| Five sentence selections, side | event | 5 | 5 |
| hPicture, side | how | 1 | 1 |

## Facts checked

Sources retrieved live on 2026-11-06; numbers independently recomputed.

- Jellyfish lack a brain and bones; nerve-net explanation: [NOAA Ocean Service](https://oceanservice.noaa.gov/facts/jellyfish.html)
  and [Smithsonian Ocean](https://ocean.si.edu/ocean-life/invertebrates/jellyfish-and-comb-jellies).
- Eight octopus arms and color change: [Monterey Bay Aquarium](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/giant-pacific-octopus).
- Sea turtles surface to breathe: [NOAA Fisheries, Green Turtle](https://www.fisheries.noaa.gov/species/green-turtle).
- Sharks replace teeth throughout life: [Florida Museum, Sharks FAQ](https://www.floridamuseum.ufl.edu/discover-fish/sharks/faq/).
- Male seahorses carry developing young in a pouch: [Smithsonian Ocean](https://ocean.si.edu/ocean-life/invertebrates/pregnant-seahorse).
- Penguins are flightless birds and swim swiftly: [Australian Antarctic Program](https://www.antarctica.gov.au/about-antarctica/animals/penguins/)
  and [Monterey Bay Aquarium](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/african-penguin).
- Speech/background mixing context: [BBC R&D WHP 324, Mike Armstrong, September 2016](https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP324.pdf).
  Five gains independently recomputed: 0.063096, 0.125893, 0.251189, 0.501187, 1. These are not measured speech ratios.
- Ambient light reduces projection contrast: [AVIXA Image System Contrast Ratio, 2021](https://www.avixa.org/resources/standards/image-system-contrast-ratio).
  Illustrative ratios recomputed: 2.461538, 4.166667, 10.5. Passing this model does not imply AVIXA compliance.
- WCAG palette ratios recomputed: 7.267, 6.713, 14.463, 5.946. Eight bars at 72 bpm in 4/4 last 26.667 seconds.
- Roles, presentation and experience connection checked against [NCAS Media Arts K-2](https://www.nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance.pdf).
  MA:Pr5 and Pr6 are enacted. Cn10 depends on the teacher connecting this model to an actual shared experience.

## Sensitivity

No cultural, Indigenous, religious or hard-history content. Seahorse father care is animal biology, not a human-family
claim. Families includes caregivers. Notes explicitly allow seated speaking practice. All people flags are false;
empty Room is a setup scene with the specified star/microphone surrogate, so no person is missing from an active role.

## Flattest moment left

Practice is still an adult-mediated physical activity, confirmed by a button. A solitary child can skip the speaking.

## Graphics

All twelve assets inspected as a set; six animal paintings, entrance, classroom and equipment retain one painted style.
Screen-down redrawn once with built-in imagegen, prompt in art/prompts.json, raw and finished files in art/.
No placeholders or missing art tokens. Art 1,002,206 bytes; bundle 1,435,522 bytes (1,402 KiB).
No external resources or media capture calls. All six Camera paintings were inspected at final use size.
Runtime line inventory matches voice/lines.json exactly, 152 lines. Every authored source line is under 160 characters.

## Audit

One audit only, Chrome 9951 and host 8755. The process hit its 40-minute cap; Windows denied the stop request.
Audit not finished within the limit: the final diagnostic report arrived about 43 seconds later during cleanup.
Final report: review-audit/audit.md, 85 leads. Seven non-phone sizes, modes/states, Motion off, focus, five-click
repetition, quick taps and the eventual resize section were clean. The cap overrun is not a within-limit PASS.
82 phone leads were invalid: 127.0.0.1:8755 served Box Plot Builder, confirmed by frame and directory listing.
The other 3 leads are permitted first-tap Camera welcome skips (BASELINE 16); the hint and Read retain the instruction.
All 91 audit frames opened on 16 sheets. Scoped repairs then re-shot Room at all seven non-phone sizes; a live
1366 to 760 to 1366 resize during the light change kept screen proportions and readiness, with zero exceptions.
An isolated 127.0.0.2:8755 host verified twelve actual-tool phone states: all targets at least 60 px, no below-fold
controls, clipped hints or sideways scroll. Frames in phone-check/ and room-proportions/ were opened and inspected.
No second full audit. Review Chrome instances and the isolated server are closed; the unrelated server was untouched.

## Left open

Spec-level shortcut/self-report conflicts and MA:Cn10 scope; unrecorded narration and a physical-device listening check.
Chose the specified teacher-led preparation flow over adding an assessment or topic, per the unattended brief.
The octopus crop follows the required 70 percent shift; it shows three arm sections rather than literally two.
No spec edit, kit change, new topic, upload, recording, or git commit. Audit cap/stop failure documented above.
