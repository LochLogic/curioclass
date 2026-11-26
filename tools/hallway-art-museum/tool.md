# Hallway Art Museum: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: hallway-art-museum

#### Built

Built 2026-11-01 in S:\CurioClass-codex. Build only, no commit, no polish round.
Choose, Set up, and Opening day are implemented with all twelve artworks, three themes, five display homes,
height controls, Kid eyes, fifteen checks, four museum jobs, reasons, swapping, and confirmed reset.
All required build files exist. The offline bundle is 1,029,267 bytes, below 2 MB. Source is readable, 935 lines.
Only the tool folder and its Scratch folder were intentionally written. No shared kit or engine was changed.
Chrome used 9970 and 9971, with host 8775. All were confirmed closed. Tool-folder host.html was removed.

#### Numbers check

Evidence: Scratch numbers.json, mechanics.json, final-numbers.json, and final-stats.json.
- 57 inches = 144.78 cm; 60 inches = 152.4 cm. The 145 cm starting center deliberately misses the kid band.
- atan(35 / 120) = 16.2602 degrees, matching the spec's rounded 16.3 degrees.
- Kid estimates: 115.7 minus 10 = 105.7 cm; 115.0 minus 10 = 105.0 cm. The classroom setting remains 105 cm.
- Adult estimate: 169 minus 11 = 158 cm. The band is 105 plus or minus 35, inclusive 70 to 140 cm.
- Robot Stand centers: 60, 90, 120 cm. Case centers for a 15 cm work: 57.5, 82.5, 107.5 cm.
- Actual content table counts: Animals 4, Weather 4, Things That Grow 4. Five picks therefore require justification.
- Computed contrast: white/brand 6.237:1; brand/paper 5.681:1; ink/paper 14.610:1; muted/paper 6.209:1.
No numerical disagreement with the spec was found. Artwork is enlarged when needed for legibility; it is not a scale drawing.

#### Feel check

Played the complete choose, explain, place, protect, lower, check, and opening-day path using the K-2 controls.
Best moment: dragging the fox from the blurry 145 cm position into the clear band at 105 cm while Kid eyes stayed on.
Flattest moment 1: the picked card was crowded at 680x425. Its reason chips now share a horizontal row there.
Flattest moment 2: frames stretched across empty bay space. They now hug the artwork; supports meet its bottom.
The robot also visibly protrudes from an unsuitable glass case instead of appearing to fit it perfectly.
The collection feels earned and specific to the class. The later material and height choices differ from the first paper work.
Both bar tools were bundled in Scratch and opened. bar-comparison.png places this hallway beside Snowy Mail Route.
The painted room, material textures, glass highlights, and large close-ups meet the visual bar in my assessment.
This was a desktop student-path play-through, not a timed session with children; actual classroom pacing remains untested.

#### Done when

1. PASS. Cart grid and five-bay wall checked at 1366x768 and 680x425; final support frames show both layouts.
2. PASS. Independent expected-home matrix checked all 60 piece/home combinations. Alternative homes retain checks and notes.
   The framed tree's Home badge includes the sun mark. Exact safety and light notes were verified after repair.
3. PASS. Placement starts at 145 cm. Kid eyes marks it high. Real dragging reached 105 cm, with blur removed and Kid eyes still on.
4. PASS. Robot and case centers matched the independent calculations. Real Low, Middle, Tall clicks ended at 107.5 cm for the turtle.
5. PASS. Window is offered only for selected bay 3. Moving the tree out clears its Window home; occupied-bay swapping was checked.
6. PASS. All fifteen checks earned the ribbon. Two earned events started the ready line twice after a height change and recheck.
7. PASS. All eight role prompts appeared and started their event lines. Five Next piece actions wrapped the glow back to bay 1.
8. PASS. Held taps interrupted the ribbon, with zero remaining finite animations after Read. New checks and closing notes hush stale speech.
9. PASS for target dimensions and main-control visibility. Repaired pedestal buttons measured exactly 60x60 at 680x425.
   Homes and the bar remained visible at every required size. Scene cards use artwork, numbers, and accessible word labels.
10. PASS in targeted checks. Motion off had zero running infinite animations; repeated reason guidance spoke once; resource checks found zero HTTP requests.

#### Wave lessons

- Hint and voice: PASS. Immediate hints, scoped Curio.voice, valid checks, Read context, and once-only how lines.
  The held 2-second reason run spoke reasonDone once, then logged silent/heard repeats. Pedestals name Low, Middle, Tall.
- Focus and layout: PASS. Stable button nodes; no focus on load. Whole keyboard path ended on m-choose after Back to cart.
  Pick and Put back move focus deliberately, and reset now restores the neutral role prompt.
- Sizes: PASS in inspected frames. All required widths, including the real 375 px iframe, were covered; target checks found no small buttons in repaired states.
- No giveaways: PASS for this transparent builder. No hidden-answer puzzle, score, or prediction meter was introduced.
- Honest numbers: PASS. Child eye height is labeled an estimate; center math uses the supplied artwork sizes, not painted dimensions.
- Standards: PASS. Selection practices Pr4, homes and heights Pr5, roleplay Pr6, and reasons for inclusion Re9.
- Motion off: PASS. Explicit animation:none and transition:none rules remove the daylight loop, slides, fades, and ribbon roll.
- Short choices stay visible: PASS. Twelve cart tiles, themes, homes, reasons, and roles are not hidden in short-choice scroll panels.
- Resize mid-animation: PASS in targeted real-input checks. Ribbon, height movement, and kid fade survived 1366 to 760 and back without exceptions.
- Deferred welcome: PASS by helper use and logs. No welcomeAfter; the first artwork tap speaks its own description, and mode welcomes are scoped.
- Unknown stays unknown: PASS. Empty bays show placement instructions or Coming soon, without a fabricated home or success badge.
- One look, one meaning: PASS. Eye markers, dashed edges, arrows, checks, question marks, and text work in the inspected grayscale frame.
- Badge says what is true: PASS. Theme justification is distinct from a literal match; Home and Height are evaluated separately.
- Hint changes back: PASS. Mode entry updates immediately; Start over clears the prior role prompt; pedestal hints name the available controls.
- No answer by copying: PASS for scope. This is display preparation and roleplay, not a diagnosis quiz with a concealed answer.

#### Audit leads

AUDIT NOT FINISHED. The single audit was stopped automatically at 40 minutes, as instructed.
No audit.md or aggregate lead list was produced, so a clean mechanical audit is not claimed.
It left 67 size/state/calm PNGs, all inspected. The full walk/repeat/stress results were not recovered and remain unverified.
The default Set up mode snapshots remain Choose because five picks are required; the real-input setup states show the actual hallway.
Visible and independently found issues repaired during this build: cramped reason chips, narrow pedestal targets,
stretched frames, floating supports, oversized-case visuals, inactive opening bays, empty spot affordances,
Back to cart focus, reset's stale role prompt, pedestal instructions, and accepted-home notes.
After repairs, targeted drive batches reported no console errors or exceptions. The full audit was not rerun.
The upper-limit audit state was added afterward, and the lower-limit phone filter corrected to 375x812 for the next reviewer.
The upper limit itself was verified with real taps at 200 cm; the repaired phone filter was not re-audited.

#### Frames looked at

All paths below are under _scratch/hallway-art-museum/.
- early/, setup-early/, setup-fixed/: initial cart, close-up, picked card, five-piece setup, and Kid eyes; faults were repaired.
- bar-shots/: both bar tools. bar-comparison.png: hallway and Snowy Mail Route side by side.
- full-0/, full-1/: all three modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, and 760x900.
- phone/: Choose, Set up, Opening day in the 375x812 iframe. The parent test host's favicon request returned 404; this was not a tool request.
- special/, ribbon-fixed/, fit/, last-checks/: limits, gray view, real drag, keyboard movement, reasons, sixth pick, roles, theme change, ribbon re-earning.
- targeted-final/: twelve repaired/extreme states, including a whole keyboard path, 60 px controls, kid drag, ribbon interruption, and the oversized robot.
- support/: final 680, 760, 1366 support alignment. resize-final.png: state after three mid-animation resize checks.
- reset-checks/: confirmed clear, neutral role prompt, and Put back removing one bay while keeping the other four.
- audit/: all 67 PNGs, inspected through audit-sheet-* and audit-rest-sheet-* contact sheets.

#### Art made

22 finished WebP images, 715,562 bytes total, about 698.8 KiB. Final bundle: 1,029,267 bytes, about 1005.1 KiB.
Hallway, cart, twelve artworks, four display-home assets, and four role props were made with the built-in image tool.
Full house style and prompts are in art/prompts.json; originals are in art/raw/. All carry drawn_by: codex provenance.
Every finished asset was inspected. No image needed a full redraw. The cart and snowman received edge despill through free rekeying.
The glass, bays, ruler, eye markers, badges, ribbon, labels, and ticket word are drawn in code.

#### Art still to paint

None. No people were generated. No painted asset is missing or represented by a labeled placeholder.
Narration recordings were not made, as instructed. The 48-line bank/style inventory is complete and uses browser speech fallback.

#### Engine changes wanted

None. No family engine applies and no shared source was edited.

#### Left open

- The mechanical audit did not finish. Cold review should obtain its own leads; these targeted results are not a substitute for its full suite.
- No audible review of Zephyr recordings was possible because recordings were intentionally not made. Browser speech was tested through logs in muted Chrome.
- The illustrated object/support sizes are adjusted for legibility. Numeric center heights and checks are authoritative; the room is not a measurement activity.
- On first success, the ribbon is shown directly over the wall. A subsequent unchanged Check opens the fifteen badge rows. This presentation choice is noted in handoff.md.
- Short check dialogs can scroll through informational rows. Their Back to wall control starts at the top; the choice sets and main hallway controls fit their views.
- The report was written last to honor the user's explicit stop-on-report instruction. The first bar-frame open attempt failed on file-URI formatting and was corrected.
- No real classroom session, touch smartboard, Safari, or Firefox run was performed. No git commit and no polish round were started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: hallway-art-museum

#### Played

Played cold as a K-2 learner: five picks with reasons, unsuitable homes, heights, Kid eyes, all 15 checks, and all eight role prompts. Strong tactile art and a clear child-height reveal.
#### Findings fixed

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
#### Findings left

No known blocker or should-fix remains within the completed checks. Polish, general: recorded narration is absent under the no-recording rule. Full mechanical verification remains incomplete as detailed below.

#### Flattest moment left

Opening day's second prompt is still a quiet invitation to speak or act. This is the specified class roleplay, now anchored to a named, highlighted piece; it has no automatic judgment.

#### Graphics

All 22 finished assets inspected on contrasting sheets and in play; no people, missing tokens, or style mismatch found. Kept the cart, tactile artworks, room, display supports, and Kid eyes reveal.
Redrew S:\CurioClass-codex\tools\hallway-art-museum\art\guide.webp with the built-in imagegen tool. Full house style and revised guide prompt are in art/prompts.json; free rekey includes spill removal.
Art: 714,042 bytes. Bundle: 1,034,963 bytes (1010.7 KiB), below 2 MB. Both existing bar-tool bundles were opened without modifying their folders.

#### Audit

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

#### Left open

Recorded narration is absent and may not be recorded in this review. Browser fallback needs a classroom listening check; no real classroom, smartboard, Safari, or Firefox trial occurred.
The art remains enlarged for legibility, as documented in notes/handoff; numerical center heights are authoritative. This is not a scale-measuring activity.
All four standards have direct activities: collection selection, material/height preparation, museum jobs, and reasons for inclusion. Notes retain the required three opening sections.
Evidence: Scratch cold-frames/, review-sizes/, review-special/, review-final/, review-voice/, post-audit-frames/, numbers-review.json, mechanics-final.json, voice-counts.json, resize-recheck.json. One pass; no shared source edits, git commits, or second audit. All started Chrome and host processes were closed; host.html is absent.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Hallway Art Museum build handoff

Built 2026-11-01, Build only. No commit and no polish round.

#### Layout and code

`src.html` starts from the kit starter and uses the shared kit CSS, controls, tones, and `Curio.voice`.
The three views share one live wall element, moved into the Opening day view without duplicating its state.
Controls are created once. `render()` updates their attributes and artwork interiors while preserving button focus.
The content table, home rules, center calculations, checking, narration, rendering, and pointer handling are separate
sections in the script. `window.__tool` exposes state, calculations, actions, and voice logs for review.

Choose has a real 4 by 3 grid over the painted cart. Compact landscapes retain a side height panel and a full-width
home tray and bar. The phone uses a three-row header, a wall above the height controls, and a two-row home tray.
The wall uses real pixel layout with a centimeter-to-position mapping; it is not a scaled fixed desktop canvas.
Artwork has a minimum drawn size to keep little clay and rock pieces recognizable in previews. Center calculations
always use the spec's actual artwork sizes, including fractional centimeter centers on cases.
The painted support meets the displayed artwork's bottom after that visual size adjustment. Do not measure the
illustrated object or pedestal against the ruler to infer its physical dimensions; the center value is authoritative.

#### Important behavior

- Reasons belong to pieces. A theme change keeps the collection and recomputes literal matches.
- Only colors and story reasons justify a nonmatching piece. The theme reason does not falsely make it match.
- A selected tray piece can be placed by tap or drag. A displayed piece swaps with the destination bay.
- Window homes clear for every piece moved outside bay 3, including the other half of a swap.
- Wall height clamps to 40 through 200 in 5 cm steps. Stand and case centers derive from level and half the piece size.
- Kid eyes is view state only and remains on through dragging. It evaluates centers in the inclusive 70 through 140 band.
- A change invalidates the ribbon. A successful check earns and speaks it again. A repeated unchanged check opens the rows.
- Opening day accepts unfinished work and has no score or win gate. Next piece wraps through all five bays.
- Start over confirms and clears the collection and hallway. Nothing is saved between visits.

#### Narration and motion

The bank is upbeat-guide, Zephyr, with the specified bright tour-guide style. `voice/lines.json` contains the complete
fixed narration inventory. No audio was recorded, as required for this build, so actual playback uses browser speech.
How-to lines use `V.how`; piece descriptions, role prompts, check notes, and ribbon results use events.
Checks and mode changes hush obsolete speech. Queued notes are tied to the hallway revision and open check dialog.
Read takes its content from the card, check notes, role prompt, or current next-action hint.
The Stand and Glass case have their own Low/Middle/Tall instruction so their hint names the controls actually present.
Tap or key input finishes running finite animations immediately. Motion off explicitly removes all tool loops and transitions.

#### Art

All 22 specified assets were generated with the built-in image tool in one gouache and colored-pencil house style.
Full prompts, size budgets, provenance, and keying options are in `art/prompts.json`. Raw originals are in `art/raw/`.
The free `scripts/art.py hallway-art-museum --rekey <name>` path made every finished WebP.
The art cart and snowman received edge despill. No people were generated and no art remains to paint.
The tree is translucent tissue collage; the glass case, ruler, band, badges, ribbon, and labels are code.

#### Checks and evidence

Scratch is `_scratch/hallway-art-museum/`. It contains numeric recomputation, image provenance paths, art and frame
contact sheets, the two bar-tool bundles and frames, real-input shots and logs, functional checks, and the one audit.
`audit-states.json` uses real inputs for the picked card, kid view, lower height limit, check rows, ready opening, and reset.
The report is the final record of audit leads and any remaining limits. The full audit is not rerun after targeted repairs.

The single mechanical audit reached its 40-minute cap without writing audit.md. It left 67 frames, all inspected.
Its completed state images are evidence, but its full repeated-input and resize suite is not certified complete.
Afterward, targeted checks passed for 60 px pedestal controls, the longest selected name, alternative-home notes,
keyboard return focus, the upper limit, ribbon interruption, Kid eyes dragging, and the oversized robot's case.
A separate real-input CDP check resized during the ribbon, height movement, and kid fade with no exceptions.
The final support-alignment change was re-shot at 680, 760, and 1366. The upper-limit audit state was added for
the next reviewer, and the lower-limit phone-size filter corrected, after the timed audit; those edits were not re-audited.
Final reset checks confirmed that Keep it preserves the work, Yes clears picks and bays, the role prompt resets,
and Put back removes only its piece and bay. The shipped bundle is 1,029,267 bytes with 48 browser-narration lines.
All launched Chrome and host processes were closed; ports 9970, 9971, and 8775 were confirmed no longer listening.

The functional matrix covered all 60 piece/home pairs, band boundaries, fractional case centers, swaps, the window reset,
height clamping, and argued themes. Separate input runs covered real dragging, keyboard height movement, all eight role
prompts, a sixth pick, theme changes, and two earned ribbon speech events. Frames cover every required size and all modes.

#### Spec questions and implementation choices

The spec lists no open questions. No subject matter, modes, or export/save features were added.
The favorable Stand options for the two clay pieces are accepted with their safety note, following the explicit piece table.
On the first successful check the ribbon appears directly over the wall. A subsequent unchanged check opens the fifteen
badge rows, so the success moment is visible instead of being covered immediately by a dialog.

#### Engine changes wanted

None. No kit, engine, shared script, documentation, or other tool was edited.

#### Next review

Use the cold review in a separate chat. Check browser narration by listening on the intended classroom device, and
assess the small-art minimum sizing and classroom pacing with a real K-2 group. No polish round was started here.

#### Cold review repairs, 2026-11-04

The cold reviewer played the full student path before reading this handoff. Source changes keep the cart, original
collection, hallway, Kid eyes reveal, support art, and check rules. The pointer prop was redrawn with a slender
shaft and modest grip; its full prompt and cutout settings are in art/prompts.json, using the built-in image tool.

Set up now uses CSS grid so DOM order is tray, bays, homes, height controls, then the bar. The worktop contains
only the wall. Mode switching returns the wall to that worktop. Reopened cards always show a next action, Read
uses individual registered lines, and the fifth-pick event waits until the look-closer card closes. Five picks
keep the Set up instruction when returning to Choose or cancelling Start over. Limits name the enabled arrow.
Each native dialog has its own Read control because the header is inert while a dialog is open. Card and check
Read use individual registered narration parts. Boundary arrows transfer keyboard focus to the enabled direction.

Low pedestal warnings name Tall or Middle. Opening day names the glowing artwork, responds visibly to Next piece,
and supplies a useful action instead of an art-looking prompt when its bay is empty. The existing eight prompts
remain unchanged for occupied bays. The role label is informational; the class still supplies every explanation.

Review evidence lives in Scratch: cold-frames, review-sizes, review-special, review-voice, mechanics-final.json,
numbers-review.json, and review-audit. The final audit result is recorded in codex-review.md. Recordings remain
absent under the no-recording rule. No shared kit edits or git commits were made.
The 63-line inventory matches allLines(). Held-click counts: reason guidance 1/1, repeated piece descriptions 5/5,
repeated role events 5/5, re-earned ribbon events 2/2, fifth-pick event 1/1. Read works during speech and with Sound
off. The keyboard-only path chose five pieces, placed and framed one, changed height, checked, and returned focus.

The review audit hit its 40-minute limit with 77 frames and 71 aggregate leads. Its stress suite did not finish.
The partial report's clean stress rows do not establish coverage. All saved frames were inspected. Confirmed
repairs: compact ruler callouts/ticks no longer collide; tick marks remain, with only colliding numbers suppressed.
The ribbon is click-through, clears the ruler, and stays above the art in compact views. The checklist header
stays visible while scrolling. The child-eye estimate note stays visible on phones. Active-mode re-entry leaves
its current welcome running. Reset opening/dismissal hushes obsolete speech. Empty-gallery guidance is a how-to
spoken once; moving between an empty and occupied bay stops stale guidance and restores the relevant prompt.
Removed the global #hint keep-region because native dialogs intentionally cover that underlying hint.

Remaining audit leads were expected pointer-transparent/behind-dialog hit-test results and first-tap welcome
suppression required by STANDARDS. The two real rapid-mode welcome cuts were fixed and directly re-tested.
Post-audit evidence is in post-audit-frames/ and its JSON results. Nine direct resizes during the ribbon, height
motion, and Kid eyes fade passed without runtime errors; resize-recheck.json records their scope. This targeted
check is not a completion or rerun of the full stress audit. All review Chrome and host processes were closed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
