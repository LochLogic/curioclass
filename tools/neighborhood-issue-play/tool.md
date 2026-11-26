# Neighborhood Issue Play: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: neighborhood-issue-play

#### Built
- Five reached steps: Street, Characters, Theater, Scenes and Perform. Offline single HTML, local saving, confirmed reset and problem changes.
- Three problems, six viewpoints each, two or three human characters, wants and blockers, voice/movement choices, scenery, props, costumes, three editable scenes, live checks, flat preview, role reading, Auto, bow and reflection.
- Owner decision applied: the third problem is neighbors who cannot yet talk to each other after a new family moves in. The family is never framed as the problem. All six human puppets are people: true for the next painter.
- Stage is built in tool.draft.json. No commits or polish round. No kit or other tool source edits.
- Final file: 1212.6 KB on disk, under 2 MB. No host.html remains. Assigned Chrome and host ports are closed.

#### Numbers check
- Scratch numbers.txt recomputes all seven supplied contrasts: 6.18, 5.18, 13.20, 5.56, 15.75, 12.21 and 6.02 to one. They agree with the spec.
- Six neighbors give 15 unordered pairs. Suggested clashes: A has two mutual pairs; B has three one-way pairs; restored C has one mutual pair, Rufus and Councilor Bramble. Every neighbor is helped by at least one listed fix in each issue.
- The Art list enumerates 27 assets, despite saying 30: five scenes/fronts, four wings, six props, six puppets and six costumes.
- Auto uses 1500 + 60 times character count milliseconds. The flat preview lasts six seconds with either Motion setting. Bibliographic dates are not a numerical model.

#### Feel check
- Best moment: opening the painted curtain on the student's own costumed cast, seeing the selected role's line turn gold, then bowing and writing a closing answer about their street.
- Flattest moment 1: a tall character form hid the important want/blocker choices. Moved them first, retained readable cast cards and kept card Edit buttons visible at 680x425, even with three characters and a long want.
- Flattest moment 2: equal prop sizes and long theater shelves weakened the miniature stage. Sized props by type, kept them opaque in Perform, spaced new props, and moved category buttons below the stage so all six props or costumes fit in compact and phone views.
- Full student-style run covered all six views, cast editing, scenery, a failed check, a repaired clash, custom lines, performance, bow, reflection, reload and resets. Real held clicks and a jittered prop drag were used.
- Looked at Snowy Mail Route and Beat Lab, bundled into Scratch without changing their folders. feel-comparison.png places this theater beside Beat Lab. The painted street and theater have comparable visual care; the temporary people silhouettes remain deliberately simple.

#### Done when
1. PASS: street and theater dominate their steps at 1366x768, 680x425 and 375 wide. Next line remains visible in Perform. Final closing answer is visible at 680 and 375, with focus in its textarea.
2. PASS: two Nobody blockers fail the clash check and show the six-second Okay/ drooping audience preview. Choosing a character blocker passes immediately. playtest.txt and postcheck.txt.
3. PASS: final templates-final.json checks 1620 sentence variants across six neighbors, three issues, nine blocker choices, four clash slots and both helped states. Wants include noun, full sentence and reported forms. Reviewed the generated wording and corrected first-person pronouns in read-backs.
4. PASS: role gold, speaker movement, Motion-off outline, entrance skip, scene cards, manual Next, Space/Enter, Auto and From the top checked. Bow and reflection checked with held input at compact, laptop and phone sizes.
5. PASS: backdrop, wing, prop and costume changes were ready on the first requestAnimationFrame after the change in targeted browser checks.
6. PASS: authored state survives reload, including reflection. Cancel preserves work; confirmed New play clears its storage key. A new problem retains theater and costumes only.
7. PASS: at two-second held-tap pace the how-to line starts once across five edits. checkFail and flat each start twice on separate preview runs. Read interrupts other speech and queued instructions wait. Dialogs suppress welcomes.
8. PASS: no recording, microphone, print or share features, and no external resource requests in the bundle. Saving is explicitly on this device.

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
- Bar frames: snowy-mail-route and beat-lab, 1366x768.
- All six early frames, five full-play frames, 28 full-size/mode/phone frames and the compact character repair frame.
- All 73 audit PNGs inspected through seven contact sheets, with individual compact and phone frames opened where needed.
- All three final voice frames, four postcheck frames, eight final repair/phone frames, three final keyboard/registry frames, two sticky action-row frames and the final own-role voice frame.
- Art contact sheet inspected before and after redraws, plus finished art in the actual street and theater. Evidence is only in _scratch/neighborhood-issue-play/.

#### Art made
- 21 finished nonpeople WebP assets, 838.4 KB total. Built-in image generation used, with prompts in art/prompts.json, raw PNGs in art/raw/, and free art.py --rekey processing only.
- Redrew the school and lot to replace magenta skies, the ball to remove an unwanted stage, and the sash to replace an incorrect garment. Improved key cleanup on bench, wheelbarrow and glasses.
- Final offline bundle is 1212.6 KB. Source has normal line breaks, no lines over 160 characters and no em dashes.

#### Art still to paint
- people: true: puppet-shell, puppet-rufus, puppet-gail, puppet-nutmeg, puppet-bramble and puppet-fern. No people, faces or body parts were generated in this build.
- Faceless code paper silhouettes and art tokens are in place. The next painter should review all six human puppets, then set paintedPeople and adjust costume anchors.

#### Engine changes wanted
None.

#### Left open
- Restored language-barrier scenario awaits the cold teaching/sensitivity review. Notes explicitly avoid assigning a language, ethnicity or accent, and ask whose view is missing.
- Human puppet art and recorded narration are deferred by instruction. The bank metadata is friendly-dad / Achird; current narration uses the browser's available voice. Sound was checked mechanically, not by an external listening reviewer.
- Secondary compact/phone editor scrolling remains. Scenes uses one scene tab at a time at every width. Theater categories sit below the stage rather than in the panel to preserve short-choice visibility.
- The full mechanical audit was not rerun after targeted repairs. This is Build only; no polish round was started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: neighborhood-issue-play

#### Played

- Cold Grade 4 solo play through Street, Characters, Theater, all three scenes, Perform, Bow and reflection before reading builder notes/source. Also considered the projected class path. The handmade theater and live role reading are strong.
- Kept the street, proscenium, paper palette, set building, student pacing, flat preview and saved play. One review pass; no commits or shared-file edits.

#### Findings fixed

- Should fix, general, art/prompts.json and all modes: six placeholders replaced by individually painted human puppets, all people: true. Tuned costume anchors, removed magenta fringes, and corrected Gail's blank paddle to an octagon.
- Should fix, general, restored story: Fern now speaks as a member of the newly arrived family, with ideas to share. Communication is reciprocal; a painted courtyard replaces the empty-lot set choice. The family is never the problem.
- Should fix, general, Street (school): removed the claims that a guard cannot stop cars without paint and that every town must count cars before painting. Proposals now ask the town to study crossings and traffic conditions.
- Blocker, general, misleading checks: blank/punctuation wants and fixes no longer pass. On-screen reasons and a note explain that these are plan-choice checks, not a judgment of custom dialogue or real-world effectiveness. The counter now reports views opened, not comprehension.
- Should fix, general, Characters/Scenes: removing a character could leave one-line scenes and no proposal. Restored the two-line starter minimum while preserving a setup/proposal before a reply.
- Should fix, general, Perform/Theater voice: removed the automatic preview over Perform's welcome; shortened the theater welcome; stopped the first role line cutting the Perform welcome; invalidated role speech on curtain-close. Category hints speak once and current-tab re-taps preserve speech. Own-role speech stops when another role or a scene card takes over; closed and bowed stages have no stale speaker cue.
- Should fix, general, craft: costumes sit on the painted heads/bodies; small ball artwork scales separately from its 44-pixel target; long unbroken text wraps; wheelchair movement labels describe rolling.
- Polish, general, flattest moment: the blank casting screen is now a painted audition lineup. The closing card names the student's issue.
- Should fix, general, phone Street and compact Scene 3: compacted problem-card spacing; hid the duplicate custom-fix field until needed; grouped beneficiaries. The fix and all three 44-pixel beneficiary inputs now fit together, including 375 wide. Custom fix reveal, editing and restoration passed.
- Should fix, general, Perform keyboard: Space after Curtain closed it instead of advancing. Curtain now focuses Next line without scrolling; Space then Enter advances two lines at 680 and 1366. The closing hint names the visible answer field.
- Should fix, general, Flat Preview: explicitly labeled the forced Okay-only example so it does not claim to evaluate the student's custom scene. Kept its three bubbles inside the proscenium; 680, 1366 and phone rechecks passed.

#### Findings left

- No confirmed blocker or should-fix remains. Nit, voice: browser narration has no recordings and does not guarantee the voice-bank timbre; this review did not record audio.
- Nits: secondary fields in long compact editors require scrolling. Main actions stay visible; authoring is still slower than performance.

#### Break it

- Repeated the same neighbor five times: one distinct view, Make the play stays disabled. Rapidly opening three different views opens material, not a claimed listening/comprehension score.
- Wants: empty, spaces and punctuation fail. Self, Nobody and Time-only blockers fail the interpersonal-clash rule. A real character blocker changes the plan check immediately.
- Fix: empty/punctuation, no beneficiary, or a beneficiary outside the cast fail. Arbitrary custom dialogue can satisfy a declared plan, explicitly labeled as such; the tool awards no writing/mastery score or best score.
- Repeated Add line stops at six; costumes stop at two; props and cast stop at three. Early Bow is disabled. The final reflection is an open question, not a scored gate or an assumed mistake.
- 1,459 browser assertions covered the check cases, all 1,440 template combinations, fix coverage and voice registry; held-input limit checks, prop keys and character removal were also run. See behavior-results.json and recheck-frames in Scratch.
- Actual reload, cancel reset, confirmed New play, problem-change retention, entrance skip, curtain-close and From the top passed in persistence/results.json.

#### Voice walk

- Real held input at a two-second action pace: welcome tap, problem C, six views, Make the play, two characters, blocker, Theater, backdrop, prop and costume, Scenes, three scenes/fix/help, Stage check, Perform, Curtain, Next line, Bow.
- Expected spoken order: welcomeStreet, heardHow, welcomeCharacters, blockerHow, welcomeTheater, propsHow, costumesHow, welcomeScenes, writeFix, checkPass, welcomePerform, yourLine, bow. Log: voice-check/walk-progress.json.
- Final main-path mode welcomes: each once, with no cuts. Other how lines stopped after the student completed their action or left an own-role line. These are deliberate stale-state interruptions.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Five mode welcomes | welcome | 1 each | 1 each |
| yourLine | how | 1 | 1 |
| Props after five tab taps | how | 1 | 1 |
| checkFail | event | 5 | 5 |
| flat after five completed previews | event | 5 | 5 |

- Neighbors and the student's script remain silent for live reading. Read, Sound off/on, rapid mode changes and closed-curtain stale speech were exercised.

#### Facts checked

- Fictional neighbors, feelings, wants, dates and proposed fixes are authored material, not empirical promises; notes state this. The school proposals are ideas for town review, not crossing-safety instructions.
- Crossing studies consider traffic/pedestrian volumes, speed and road conditions, and paint alone is insufficient: [FHWA STEP guide](https://highways.dot.gov/safety/data-analysis-tools/rsdp/rsdp-tools/guide-improving-pedestrian-safety-uncontrolled-crossing), [FHWA STEP Studio](https://highways.dot.gov/sites/fhwa.dot.gov/files/2022-06/step_studio.pdf).
- Crossing guard and paddle framing: [FHWA current MUTCD, 11th edition with Revision 1, December 2025](https://mutcd.fhwa.dot.gov/kno_11th_Editionr1.htm), Part 7D. The paddle is a blank toy prop, not a usable traffic sign.
- Authorized temporary play streets: [NACTO, Temporary Street Closures](https://nacto.org/publication/urban-street-design-guide/interim-design-strategies/temporary-street-closures/).
- Paper theater tradition and credit: [V&A, The story of pantomime](https://www.vam.ac.uk/articles/the-story-of-pantomime), [Pollock's Toy Museum history](https://www.pollockstoymuseum.co.uk/about-us/the-history-of-pollocks-toy-museum/). Replaced the inaccessible museum citation with its current route.
- Spolin's book/date: [Viola Spolin's publications](https://spolin.com/?page_id=212), Theater Games for the Classroom, Northwestern University Press, 1986. Conflict is this exercise's focus, not a universal claim that agreement is dull.
- TH:Cr1, Pr6, Cn10 and Cn11: [NCAS Theatre at a Glance](https://www.nationalartsstandards.org/sites/default/files/Theater_resources/Theatre%20at%20a%20Glance.pdf). Practiced through character/set choices, live performance, the community issue and personal reflection.
- Reciprocal family communication and interpreter support: [Office of Head Start, Creating Father-friendly Environments](https://headstart.gov/family-engagement/birth-5-father-engagement-guide/creating-father-friendly-environments-early-childhood-programs). Specific welcome ideas remain fictional options.
- Independent contrast calculation matches all seven spec ratios: 6.18, 5.18, 13.20, 5.56, 15.75, 12.21, 6.02. Six neighbors give 15 unordered pairs; every neighbor appears in at least one proposed fix per problem. No numerical scoring model.

#### Sensitivity

- Review the reciprocal language framing, Fern's family viewpoint, and whether character blockers encourage blame. No language, nation, ethnicity or accent is assigned; appearance is not a language clue. Notes forbid accent imitation and asking students to represent a community.
- All six people were inspected, including hands, faces, wheelchair and stroller. The contact sheet is art-contact.png in Scratch. Walking stick, wheelchair and stroller are ordinary cast details. Bramble's movement choices describe rolling.
- Owner's decision overrides the animal/empty-lot passages in the unchanged spec. No unattended question was needed; choices followed that decision and the brief.

#### Flattest moment left

- Drafting Scene 2 remains the slowest part. Starter lines support revision; the student still has to make the clash worth performing.

#### Graphics

- Six people plus the courtyard painted; Gail's paddle redrawn once; several old cutouts re-keyed. All 28 preserved WebP files inspected on the contact sheet and active images in stage frames. Six people assets are marked people: true.
- Final art 1,234.8 KB; final bundle 1,636.0 KB, below 2 MB. Compared against opened Snowy Mail Route and Beat Lab frames; feel-comparison.png places the finished theater beside Beat Lab. Strong painted settings remain intact.
- Looked at all cold, repair, calm, grayscale, phone, long-text, audition, storage and bar frames. Audit frames/disposition below.

#### Audit

- One audit completed in under 23 minutes, within the 40-minute limit: review-audit/audit.md, 50 leads, 76 frames. All frames inspected through ten sheets, with native-size lead frames opened.
- Fixed from the frames: phone Street's partly cut third card, Scene 3's hidden chosen fix/beneficiaries, and the closing hint naming a hidden restart control. Targeted post-audit frames cover 680, 800, 1000, 1280, 1366 and 375 for the editor, plus long phone views. No second audit was run.
- Retained/answered: secondary editor fields, sign wording, removal, optional cast management and New play can scroll; main actions and short scenery shelves remain visible. Modal coverage of an inert page is intentional.
- Voice leads answered: a problem tap speaks the next listening action instead of the stale Street welcome; New play suppresses speech behind its dialog. The fast closing script drops a stale own-line prompt; the two-second main walk hears it. Reached tabs sit outside the header, so explicit states cover all five modes despite zero automatic mode discoveries.
- Audit Motion off, resize, button errors, focus, repeats and quick-tap checks were clean. Tool checks had no console errors/warnings; the optional phone host alone requests a missing favicon, a harness 404.

#### Left open

- No semantic grader for arbitrary student writing was added. The spec defines structural plan checks; performance and discussion test the meaning.
- No recordings, uploads, deployment or commits. Initial documentation/memory reads returned immediately but lacked an explicit subprocess deadline; subsequent shell commands used hard limits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Neighborhood Issue Play: handoff after cold review

#### Scope
One cold review, with repairs and targeted rechecks. No commits. Writes stayed in this tool and its Scratch folder. The builder report remains historical evidence; codex-review.md records the current review.

#### Owner decision and sensitivity
Problem C is neighbors who cannot yet talk to one another after a family moves in. The family is never the problem. Fern speaks as a member of the new family, with her own ideas to share. Greetings and pictures work both ways; interpreter help is an option. No language, nationality or accent is assigned, and appearance does not identify language. Do not invite accent imitation or ask students to represent a community.

Six human puppets are painted, people: true, and enabled. The set includes different ages and skin tones, a walking stick, wheelchair and stroller. These are ordinary parts of the cast. The courtyard replaces the empty-lot set selection; old lot art remains preserved. A future fresh cultural lens should check the reciprocal communication, the family viewpoint, and whether the chosen character blocker encourages blame despite the framing.

#### Source map
src.html contains the responsive paper scenery, neighbor/problem data, asset tokens, voice table, saved authoring state, plan checks, and a render/bind pair for each step. window.__tool exposes state, run, data, checks, suggestion, lineText, readback, render and the voice log.

state is the saved authored play. run is temporary performance state. Scene lines store a suggestion slot or custom text; suggestions follow changes to wants, blockers and the fix. Custom dialogue stays unchanged. If removing a character leaves a scene short, ensureScenes restores a two-line starter and preserves a setup/proposal line.

#### Checks and content
The three checks verify declared plan choices. They do not assess the meaning of custom dialogue or whether a proposed fix actually works. This is stated beside the checks; reasons name the chosen blocker and proposed beneficiaries. Blank or punctuation-only wants/fixes fail. The street counter says Views opened, because opening material does not establish understanding. There is no mastery score or saved best score.

The school issue now asks the town to study crossings, traffic, speeds and pedestrian needs. The removed claims that crossing guards cannot stop cars without paint, or that every town must count cars before painting, are not safe general rules. Notes link FHWA guidance. All park dates, neighbors, reasons and proposed local fixes are fictional.

#### Layout and art
The stage remains the focus. Short landscapes keep the workbench alongside it; phones stack it below. Main actions stay visible; long editors scroll. An empty casting stage now shows a painted audition lineup. Costume anchors correspond to the reviewed full cutouts, including their wooden sticks. Ball artwork scales with the theater independently of its 44-pixel tap target. Props stay within normalized floor bounds and support pointer capture and arrow keys.

The original street, proscenium, scenery and paper shelves are retained. Six people and a courtyard were generated with the built-in image tool, inspected, copied to art/raw, and processed with art.py --rekey. Gail's blank paddle was redrawn as an octagon. Several older cutouts were re-keyed to remove magenta fringes. art/prompts.json records prompts, source and anchors. The contact sheet is _scratch/neighborhood-issue-play/art-contact.png.

#### Voice and timing
Curio.voice scopes speech to the step. Read speaks the current hint. The neighbors and script are read by the student. Each theater category has an instruction; repeated selection of the current category leaves its speech running. Perform entry no longer starts a flat preview over its welcome. Closing the curtain, changing roles or leaving an own-role line stops stale role narration. All fixed hints are in voice/lines.json and allLines().

No recordings were made. Browser speech is the current fallback, so bank metadata does not guarantee Achird's timbre. Main-path starts, repeats, Read, Sound and stale-line behavior are logged in Scratch. A cut in that log may be a deliberate later action, not a failed clip. The kit watchdog also bounds headless fallback speech.

Flat Preview lasts six seconds. Auto uses 1500 + 60 times the current line's character count milliseconds. Motion off removes movement and retains these times. Curtain focuses Next line, so Space and Enter advance immediately; other buttons retain their native keyboard actions. Next skips an entrance; Curtain closes during it; From the top clears run timers. The closing question is accompanied by the student's selected issue title.

#### Verification
See codex-review.md and the Scratch evidence it names. The single final audit completed in under 23 minutes with a 40-minute limit: 50 leads and 76 frames. Phone card spacing, the compact fix/beneficiary group, and the closing hint were repaired afterward and re-shot at the affected sizes. The full audit was not repeated. audit-states.json reaches all five steps with real input and adds a people/costume state for the restored language scenario. An automatic discovery count of zero modes is expected because reached tabs are outside the header.

#### Engine changes wanted
None. No kit or shared-script edits were made.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
