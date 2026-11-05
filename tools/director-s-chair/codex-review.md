# Codex review: director-s-chair

## Played

Cold as a grade 10 student, with projector layouts checked. Played all five houses before reading
the builder's report, handoff, notes or source. The venue tour invites exploration; changing seats is strongest.
All eight beats completed in each full playback, including the 95.22-second Noh entrance/bridge-exit production.

## Findings fixed

- Blocker, general, Adjust: selected actor survived a house switch and could name a missing chorus member.
  Reset selection on arrival; keyboard and turn-button checks now keep a valid actor.
- Blocker, general, compact Adjust: controls covered the ground plan. Reflowed controls above the plan; gave the phone workbench more height.
  Kept the front-seat marker visible and linked crowded initials/pose labels to their exact tokens.
- Should fix, general, Program note: intrinsic panel width could push navigation sideways. Constrained panel
  and decision widths; opened program measured zero horizontal overflow at 680x425.
- Should fix, family:stage, Compare: costume gestures read the last Tour beat. Pass the displayed beat explicitly.
- Should fix, general, voice: queued Seat guidance could outlive its beat or seat. Bind it to house/beat/seat.
- Should fix, teaching, Arrival: historical adaptations were not identified on the student screen. Added context.
- Polish, general: start keyboard focus at the offered choice; label carried notices with their original beat;
  explain hidden/dashed blocking and name Seat as the next action. Program toggle now answers with sound and hint.
- Polish, family:stage: gave code figures shoulders, sleeves, robe folds, belts, trousers and zanni costume detail.
  Hidden copying gestures remain explanatory dashed marks. Turning during playback now stops the tween first.

## Findings left

- Should fix, spec conflict: the Noh rules overgeneralize masking and bridgeway entrances. Shite roles are
  usually masked; chorus/attendants also use kiridoguchi. Exact spec text retained, as CODEX-REVIEW requires.
- Should fix, spec conflict: the commedia mock positions hide the zanni from the front seat, although the
  supplied notice describes him stealing focus. Coordinates and intended notice retained; visibility feedback
  and Seat guidance expose the difference. See the source/spec decisions in handoff.md.
- Polish, family:stage: lower-body/furniture depth remains schematic in the realist room. Shared depth-sort
  and decoration-hook requests remain in handoff.md; no kit files changed.

## Flattest moment left

The long Noh bridge cross asks for patience. Its slow movement teaches the convention; Seat, Next and Stop
remain live. The weakest object art and the counter-like figures were lifted without simplifying the venues.

## Graphics

All ten used images checked in their final exports and in Arrival/Scene. Five venue paintings retained.
Painted five new mask objects with built-in imagegen, processed only with free art.py --rekey, and inspected:
art/mask-{greek,noh,zanni,capitano,dottore}-review.webp. All are people:false; actors stay figures in code.
Full prompts/provenance: art/prompts.json. Fresh cultural image recheck found no offensive representation.
Final bundle: 1,071,875 bytes (1046.8 KiB); ten used images total 634.6 KiB.

## Audit

Audit finished once within 40 minutes: 38 leads, 29 fixed and 9 explained. Chrome 9961, host 8765.
The nine retained leads are specified narrow Tour scrolling (2), a disabled Compare probe (1), and
specified canvas insets (6). Every row is answered in _scratch/director-s-chair/review-audit-dispositions.json.
Scoped repair checks used the audit geometry checks at six affected widths; Greek/Noh label checks and
a real compact-plan drag were clean. Only repair frames were re-shot; the full audit was not rerun.
Independent checks: 426 assertions over 40 choice combinations; mask points 2/1.5/0/0/0; matching voice manifest.
Scene and five-house Compare inspected at every STANDARDS size, including the 375x812 iframe; grayscale,
Motion off, keyboard-only choice, plan arrow keys, jittered real drag and the full eight-beat playbacks checked.
Motion-on Greek playback 18.08 s; Motion-off 18.08 s. No narration during any full playback.
600-character note and choices saved/reloaded; Clear removed the saved item and current work.

| Voice line | Kind | Expected in five choice changes | Spoken |
|---|---|---:|---:|
| choiceHow | how | 1 | 1 |
| programNote | event | 5 | 5 |

Held 120 ms inputs at a two-second pace checked stale speech and Read. App checks had no console exceptions.
The temporary iframe host alone returned a favicon 404; file-based tool checks were clean.

## Left open

- Noh direct exit is 14.534 or 14.970 m, depending on the prior choice, rather than the spec's 14.0 m estimate.
  Engine easing and the bridge bend make the full long version about 95 seconds. Coordinates retained.
- Some supplied notices have one sentence despite the generic two-sentence requirement. Exact text retained.
- Recorded narration is absent because recording was excluded. Browser speech remains the fallback.
- Fresh cultural evidence and exact source links: _scratch/director-s-chair/review-sensitivity.md.
- Only allowed tool/Scratch folders changed; no commits. Every owned Chrome/server closed; host.html removed.
