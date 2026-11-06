# Codex report: neighborhood-issue-play

## Built
- Five reached steps: Street, Characters, Theater, Scenes and Perform. Offline single HTML, local saving, confirmed reset and problem changes.
- Three problems, six viewpoints each, two or three human characters, wants and blockers, voice/movement choices, scenery, props, costumes, three editable scenes, live checks, flat preview, role reading, Auto, bow and reflection.
- Owner decision applied: the third problem is neighbors who cannot yet talk to each other after a new family moves in. The family is never framed as the problem. All six human puppets are people: true for the next painter.
- Stage is built in tool.draft.json. No commits or polish round. No kit or other tool source edits.
- Final file: 1212.6 KB on disk, under 2 MB. No host.html remains. Assigned Chrome and host ports are closed.

## Numbers check
- Scratch numbers.txt recomputes all seven supplied contrasts: 6.18, 5.18, 13.20, 5.56, 15.75, 12.21 and 6.02 to one. They agree with the spec.
- Six neighbors give 15 unordered pairs. Suggested clashes: A has two mutual pairs; B has three one-way pairs; restored C has one mutual pair, Rufus and Councilor Bramble. Every neighbor is helped by at least one listed fix in each issue.
- The Art list enumerates 27 assets, despite saying 30: five scenes/fronts, four wings, six props, six puppets and six costumes.
- Auto uses 1500 + 60 times character count milliseconds. The flat preview lasts six seconds with either Motion setting. Bibliographic dates are not a numerical model.

## Feel check
- Best moment: opening the painted curtain on the student's own costumed cast, seeing the selected role's line turn gold, then bowing and writing a closing answer about their street.
- Flattest moment 1: a tall character form hid the important want/blocker choices. Moved them first, retained readable cast cards and kept card Edit buttons visible at 680x425, even with three characters and a long want.
- Flattest moment 2: equal prop sizes and long theater shelves weakened the miniature stage. Sized props by type, kept them opaque in Perform, spaced new props, and moved category buttons below the stage so all six props or costumes fit in compact and phone views.
- Full student-style run covered all six views, cast editing, scenery, a failed check, a repaired clash, custom lines, performance, bow, reflection, reload and resets. Real held clicks and a jittered prop drag were used.
- Looked at Snowy Mail Route and Beat Lab, bundled into Scratch without changing their folders. feel-comparison.png places this theater beside Beat Lab. The painted street and theater have comparable visual care; the temporary people silhouettes remain deliberately simple.

## Done when
1. PASS: street and theater dominate their steps at 1366x768, 680x425 and 375 wide. Next line remains visible in Perform. Final closing answer is visible at 680 and 375, with focus in its textarea.
2. PASS: two Nobody blockers fail the clash check and show the six-second Okay/ drooping audience preview. Choosing a character blocker passes immediately. playtest.txt and postcheck.txt.
3. PASS: final templates-final.json checks 1620 sentence variants across six neighbors, three issues, nine blocker choices, four clash slots and both helped states. Wants include noun, full sentence and reported forms. Reviewed the generated wording and corrected first-person pronouns in read-backs.
4. PASS: role gold, speaker movement, Motion-off outline, entrance skip, scene cards, manual Next, Space/Enter, Auto and From the top checked. Bow and reflection checked with held input at compact, laptop and phone sizes.
5. PASS: backdrop, wing, prop and costume changes were ready on the first requestAnimationFrame after the change in targeted browser checks.
6. PASS: authored state survives reload, including reflection. Cancel preserves work; confirmed New play clears its storage key. A new problem retains theater and costumes only.
7. PASS: at two-second held-tap pace the how-to line starts once across five edits. checkFail and flat each start twice on separate preview runs. Read interrupts other speech and queued instructions wait. Dialogs suppress welcomes.
8. PASS: no recording, microphone, print or share features, and no external resource requests in the bundle. Saving is explicitly on this device.

## Wave lessons
- PASS, hint and voice: immediate hints name the next action. Full scenes name Edit instead of disabled Add line; editing names Save line. Twenty-one fixed lines match allLines exactly. Curio.voice handles the queue.
- PASS, focus and layout: explicit fallback focus after replaced step actions, focus preserved after flat preview, named textareas, closing answer moved first. Targeted input verifies these repairs.
- PASS, sizes: all eight required sizes covered, including the 375 iframe. Audit found no small-target or tiny-text leads. Main actions and short theater choice sets are visible. Add/Save line stays beside Stage check and Perform; action rows stick while phone editors scroll. Secondary editor fields still scroll, as described below.
- PASS, no giveaways: this is an authoring tool, not a hidden-answer quiz. The check shows its structural rule openly.
- PASS, honest numbers: heard/cast/line counts match state; all numerical definitions and contrast calculations checked.
- PASS, standards: student choices invent characters and a world, design scenery/costumes, perform roles and connect a saved reflection to their community.
- PASS, Motion off: no infinite animation in the audit or targeted performance check. Auto and preview timing are preserved.
- PASS, short choices: three problem cards and six theater choices are visible in their checked views. Long character/script editors are forms with secondary scrolling, not concealed answer-card groups.
- PASS, resize mid-animation: the audit found no exceptions or stuck disabled controls while resizing every listed state after input.
- PASS, first-tap welcome: a problem tap invalidates the Street welcome as the spec requires, and now speaks the next listening instruction. No welcome plays behind the confirmation dialog.
- PASS, unknown stays unknown: unheard views remain unrevealed until their neighbor is selected. Heard markers reflect actual selections only.
- PASS, one look/one meaning and truthful badges: check/cross icons accompany color; checks describe authored wants, blockers and the fix. No success label substitutes for a performance-quality judgment.
- PASS, changing hints: tabs, scenes, edits, full scenes, curtain state, final line and bow update the instruction at once. Read uses that instruction.
- PASS, no answer by copying words: suggestions are the student's script material. There is no diagnosis answer bank or score to obtain by text matching.

## Audit leads
One audit completed: _scratch/neighborhood-issue-play/audit/audit.md, 75 leads and 73 frames. It was not repeated after repairs. Targeted checks followed the fixes.
- Fixed: focus loss after Make the play, Theater, Scenes and Perform transitions, after a disabled add-prop control, and at Bow. Common render fallback and explicit reflection focus were checked with real input. Flat-preview completion also preserves Stage check focus.
- Fixed: unnamed custom-line and reflection textarea leads. Both now have explicit aria-labels in addition to labels.
- Fixed: default bench/ball overlap across sizes. New props choose separated available floor slots. Final compact rectangles have clear gaps. Deliberate student overlap remains allowed.
- Fixed: short theater shelves/categories hidden by scrolling. Category buttons moved to the stage edge; all six prop and costume choices are visible in targeted 680 and 375 checks.
- Fixed: reflection hidden at the end. It moves to the top of the editor and is fully visible and focused at 680, 1366 and 375.
- Answered, remains: character voice/movement/management controls and script editor fields can extend below compact or phone viewports. Wants/blockers and main action buttons come first. These are long editable forms; the report does not claim the entire form fits without scrolling.
- Answered, remains: New play, sign wording and Remove selected can require phone scrolling. They are secondary controls, not the frequent play action.
- Answered: six modal coverage leads at 375 are the intended dialog covering an inert page, not accidental collisions.
- Fixed/answered: the dropped yourLine in the fast closing-state audit was stale after advancing. The first own-role instruction now takes priority over an outdated welcome, while Read keeps priority. A held two-second Perform/Curtain/Next run confirms its start; later stale line removal is intended.
- Answered: the Street welcome is stale once a problem is picked. The next listening instruction now plays instead. The automatic audit discovers zero modes because the reached step tabs sit outside the header; explicit real-input states cover all five steps.
- Audit Motion off, resizing, repeat speech and rapid tap sections were clean. No console errors, warnings or exceptions in the student, final voice or targeted repair runs.

## Frames looked at
- Bar frames: snowy-mail-route and beat-lab, 1366x768.
- All six early frames, five full-play frames, 28 full-size/mode/phone frames and the compact character repair frame.
- All 73 audit PNGs inspected through seven contact sheets, with individual compact and phone frames opened where needed.
- All three final voice frames, four postcheck frames, eight final repair/phone frames, three final keyboard/registry frames, two sticky action-row frames and the final own-role voice frame.
- Art contact sheet inspected before and after redraws, plus finished art in the actual street and theater. Evidence is only in _scratch/neighborhood-issue-play/.

## Art made
- 21 finished nonpeople WebP assets, 838.4 KB total. Built-in image generation used, with prompts in art/prompts.json, raw PNGs in art/raw/, and free art.py --rekey processing only.
- Redrew the school and lot to replace magenta skies, the ball to remove an unwanted stage, and the sash to replace an incorrect garment. Improved key cleanup on bench, wheelbarrow and glasses.
- Final offline bundle is 1212.6 KB. Source has normal line breaks, no lines over 160 characters and no em dashes.

## Art still to paint
- people: true: puppet-shell, puppet-rufus, puppet-gail, puppet-nutmeg, puppet-bramble and puppet-fern. No people, faces or body parts were generated in this build.
- Faceless code paper silhouettes and art tokens are in place. The next painter should review all six human puppets, then set paintedPeople and adjust costume anchors.

## Engine changes wanted
None.

## Left open
- Restored language-barrier scenario awaits the cold teaching/sensitivity review. Notes explicitly avoid assigning a language, ethnicity or accent, and ask whose view is missing.
- Human puppet art and recorded narration are deferred by instruction. The bank metadata is friendly-dad / Achird; current narration uses the browser's available voice. Sound was checked mechanically, not by an external listening reviewer.
- Secondary compact/phone editor scrolling remains. Scenes uses one scene tab at a time at every width. Theater categories sit below the stage rather than in the panel to preserve short-choice visibility.
- The full mechanical audit was not rerun after targeted repairs. This is Build only; no polish round was started.
