# Codex report: director-s-chair

## Built

- Build only in S:\CurioClass-codex. No commits, branch operations, shared-engine edits or polish round.
- One offline tool: five painted house cards, rules and mask casts, eight script beats, 30 directing options,
  three seats per house, live plan, Adjust, realist room lights, program notes, Compare and local saving.
- All required source, metadata, teacher notes, voice lines, audit states and handoff files are present.
- Browser speech is the fallback. science-narrator / Charon is declared in voice/lines.json; no clips were recorded.

## Numbers check

- `_scratch/director-s-chair/numbers.py` recomputes the spec's geometric distances and contrast ratios.
- Orange on panel 8.493:1; on section 8.048:1; brand ink on orange 9.061:1. Ink on panel 14.704:1;
  muted on section 7.706:1. The spec's rounded contrast values agree.
- 133 numerical checks passed, using exported snapshots for every house's eight choice combinations.
  They include all specified option endpoints, Greek entrance carry-forward and mask body-position points.
- Mask positions at 0, 45, 90, 135 and 180 degrees score 2, 1.5, 0, 0 and 0.
- Address terms are 0, 0, 2, 2, 0 for Greek, Noh, commedia, Globe, realist. Only realist lights affect focus.
- Difference: the direct Noh exit is 14.534 or 14.970 m, depending on the previous choice, not 14.0 m.
  Following the bridge junction makes the route longer. The measured whole-bridge entrance and exit run was
  95.05 seconds. Coordinates and the 0.4 m/s timing rule were retained. See handoff.md for the full calculation.
- Difference: the eye-pillar spot is 0.922 m from the pillar center; 0.6 m describes its horizontal separation.

## Feel check

- Played all five complete productions. Each reached beats 1 through 8 in order and stopped at beat 8.
- Best moment: changing to the Greek side wedge reveals how the chorus shapes attention and how a Guard can
  become partly hidden. The same words read as a different relationship from that seat.
- Flattest moment 1: the first house views were generic engine solids. Added projected masonry, pine painting,
  beams, painted town cloth, oak framing, wallpaper, window, door, lamp and shaded code figures.
- Flattest moment 2: the small plan initially drowned the action in labels. Made it a quiet seat inset by default;
  Adjust enlarges it and restores editing. Enlarged the Globe's useful camera framing around the performance.
- Compared our Tour with Beat Lab and inspected Snowy Mail Route. The side-by-side frame is
  `_scratch/director-s-chair/feel-comparison.png`. The painted invitation carries its own visual identity;
  production views remain movable geometry rather than pretending the paintings can test sightlines.
- A 95-second Noh pass deliberately asks for patience. Seat, Next beat and Stop keep it responsive.

## Done when

1. PASS: all five full playback records contain beats 0 through 7 in order, final playing=false, last=7.
   Five matching end frames were inspected in `verified-playback/`.
2. PASS: 133 numerical assertions passed over every choice combination; entrance positions carry forward.
3. PASS: exact supplied notices and current-seat focus. At Noh (-2.4, 5.4), the Guard was clear from the
   front and hidden by pillar2 from the side, with four of five rays blocked. A wider final search and the
   corresponding side-seat frame confirmed the example.
4. PASS: mask body-position points, address-house gating and realist-only light terms were computed directly
   from the running bundle in `mechanics.json` and `edge.json`.
5. PASS: three choices populate a program note; two completed houses enable Compare; all five staged views
   and beats 1, 4, 6, 8 are supported. Audit states stage two houses through real inputs.
6. PASS: a real jittered drag outside the Greek orchestra kept the move and displayed the house-rule note.
   Noh standing-chorus and realist full-front warnings were also checked.
7. PASS: House view width 887.9 px at 1366 px, or 65 percent. Choice beside it; five Tour paintings fill the
   stage; all five mask objects are visible beside their roles in Arrival and in the scene legend.
8. PASS: held-input Noh Play, Seat, Next immediately changed seat and reached beat 2 with the entry completed.
   Play scene again stops; generation-token cancellation protects every subsequent action.
9. PASS: saved choices and note equaled the reloaded values; Clear removed the storage key, current choices
   and note; a second reload stayed empty. Evidence: saved.json, reloaded.json, cleared.json, reloaded-clear.json.
10. PASS: scene view, Next and both choice buttons were inspected at every STANDARDS size, including the
    375x812 iframe on host 8795. No sideways overflow. Preview script text is 11 px; small script boxes scroll.
11. PASS: 120 ms held taps at a two-second pace produced no repeated spoken how-to key. Full Noh, Globe and
    realist records show no speech during Play. Read during calm playback returned empty speech. No em dashes
    in generated HTML, notes or metadata. Calm playback kept all beats and took 17.91 s for the Greek default.

## Wave lessons

- PASS, hint and voice: hints update in the action handler; Curio.voice owns heard-state behavior and Read.
  The held-tap log shows a stale seat hint dropped when Seat was already used, then spoken on a later notice.
- PASS, focus and layout: no focus taken on load; page transitions move focus deliberately; scene controls
  stay mounted and endpoint navigation moves focus off a newly disabled button.
- PASS, sizes: 44 px main controls; preview and laptop layouts stay side by side, phone controls stack.
- PASS, no giveaways: interpretive choices have no correct-answer badge, score or win state.
- PASS, honest numbers: the eye is labeled a rough guide; geometric dimensions and weights are described as
  the tool's own simplification. No invented claim of an 80-second Noh run appears on screen.
- PASS, standards: students use historical conventions to direct, observe, compare and justify a note.
- PASS, Motion off: no infinite animation remained in the grayscale calm frame; movement stops, pacing stays.
- PASS, short choices: the two directing options remain together and outside the script scroller.
- Resize during animation: covered by the single mechanical audit's state and resize checks.
- PASS, first-tap welcome: separate valid welcomes for Tour, each Arrival and Compare; no welcomeAfter delay.
- PASS, unknown state: Tour labels a house not staged until all three choices are actually made.
- PASS, one look / one meaning: fixed actor colors also have initials; selected seats have rings and names;
  hidden actors are dashed code outlines.
- PASS, truthful badges: staged status follows the three choices and clears on Restart house.
- PASS, reversible hints: seat, page, beat, choice and Adjust handlers set the new hint immediately.
- PASS, no copying an answer: no scored diagnosis or correct option; the student's final claim needs staging
  evidence, and different choices support different readings.

## Audit leads

- Audit ran once and finished: 79 leads; no resize exceptions, disabled locks or infinite calm animations.
- All 79 rows are individually answered in _scratch/director-s-chair/audit-dispositions.json.
- Fixed: Tour width (4 leads), Arrival focus (17), miniature-plan label clutter (45), hidden program
  controls (1), explicit note name (1), interrupted Tour welcome (1).
- Accepted: scrolling Tour cards required by the narrow-layout spec (2), disabled Compare probe (1),
  specified inset / legend coverage of the canvas (6), long program text scrolling in the preview (1).
- Scoped rechecks measured Tour at 44 px; Begin received focus; Seat retained focus after a tween; both
  program buttons stayed visible at 680x425; note name and 600-character cap matched; a 0.7-second Tour
  double tap spoke one uncut welcome. A real drag also proved Adjust edits survive Play and Next.
- The full audit was not rerun after these targeted repairs. Final scoped batches had zero console errors.
- Every started Chrome and server was closed. Ports 8795, 9990 and 9991 are closed; host.html was removed.

## Frames looked at

- Bar tools: Snowy Mail Route and Beat Lab, 1366x768, bundled into Scratch and opened before implementation.
- Initial Tour, Noh Arrival, Greek and Noh scenes, compact commedia; subsequent architectural fixes.
- All eight size conditions across Scene and Compare: 680x425, 800x500, 1000x625, 1280x720, 1366x768,
  1920x1080, 760x900 and 375x812 inside the iframe host.
- Every house, all five complete endings, choices, notices, program notes, mask casts, seats, Adjust drag,
  keyboard focus, saved work, cleared work, grayscale and Motion off.
- Primary size frames were opened individually. Repeated and audit frames were inspected in QA contact sheets;
  confirmed leads were opened at their native size. See Scratch for the frame folders and contact sheets.

## Art made

- Eight images generated during this build: five object masks and three architectural redraws, using the
  built-in image tool. Ten images used, 615.35 KiB. Thirteen retained WebPs total, 921.82 KiB.
- Replaced the Greek raised orchestra, Noh missing bridgeway and Globe covered yard with newly painted
  sibling assets. Original files remain unused. Every final WebP was inspected after the free rekey step.
- Bundle: 1036919 bytes (1012.62 KiB). All images and code inline; no automatic network requests.

## Art still to paint

None. The owner explicitly authorized the five masks as objects. All actors stay code figures.

## Engine changes wanted

Four precise requests in handoff.md: blocker depth order, directional masks, waypoint / linear-speed playback,
and a camera-aware scene-decoration callback. No shared engine file was changed.

## Left open

- Some supplied notices contain one sentence despite the generic two-sentence instruction. Their exact text
  was preserved rather than adding interpretation.
- The supplied commedia mock position can hide the zanni from the front seat while its fixed notice says he
  steals focus. Coordinates and notice were preserved; the focus line honestly reports the obstruction.
- Complete non-Noh runs measured roughly 18 to 21 seconds, near the low end of the spec's approximate 20 to
  30-second range. The Noh bend produces 95 seconds rather than the spec's approximate 80.
- No recorded narration was generated, as instructed. Compact Compare uses a scrollable grid; small scene
  scripts scroll independently. No cold review or polish was performed.
