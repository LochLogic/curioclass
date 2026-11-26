# Recital Practice Plan: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: recital-practice-plan

#### Built

Built the offline grade 9 to 12 tool in Set, Rubric, Practice and Recital modes. The program, rubric, four-week budget, seeded piano takes, ear ratings, gated meter, venue introductions, recital and printable personal sheet are connected. Five original paintings supply the rooms and metronome. Device-only saving uses curio-recital-plan.

The final bundle is 816875 bytes, 797.73 KiB. Source is readable, 1612 lines, maximum 160 characters. Node syntax check passed. Required files and JSON checked. No network API or remote runtime source exists in the tool. No commits, branch changes or polish round. Task Chrome processes and ports 9980, 9981 and 8785 are closed; host.html is absent.

Final functional run: 49/49 assertions passed. Additional closing checks: 16/16 passed. Independent model and boundary checks: 172/172 passed. Runtime driver logs report no console errors, warnings or exceptions. Test-harness mistakes were corrected before the passing runs: wrong selected passage, a nonexistent test selector, and reused localStorage between independent scenarios.

#### Numbers check

Independent Python evidence: _scratch/recital-practice-plan/calc-evidence.py and numbers.json. Runtime comparison: model-results.json.

- Five lengths round to 1:39, 2:07, 3:15, 4:00 and 1:14. Exhaustive default-tempo subset checks find exactly the three legal sets: 9:54, 9:29 and 9:35, including 20 seconds per introduction.
- Four-week hard-passage percentages for the four-piece set, in piece order: 30x5 gives 73.665/61.859/69.134/56.360; 45x6 gives 89.173/78.912/85.593/73.127; 60x6 gives 94.441/86.479/91.864/81.319; 60x7 gives 94.316/86.277/91.707/81.092. Runtime results match independent calculation within 0.001 percentage points.
- 60x7 is slightly below 60x6: 420x0.85 = 357 effective minutes, versus 360. It is close, not identical.
- Three-piece Entertainer even split gives 63.01%, not 64%; 35% allocation gives 87.91%, not 85%. Other hard passages give 84.96% and 72.38%, not both 72 to 79%. The specified formula and difficulties win; spec.md is unchanged.
- Exact even splits across nine units at 150, 360 or 420 minutes cannot be entered with 15 minute slider steps. The 270-minute split is achievable at 30 minutes per unit. Fractional model checks exercise the formula separately.
- At readiness .5/.85/.95: expected wrong notes in 40 are 3.5355/.58095/.11180; tempo is 87.5/96.25/98.75%; wobble distribution SD is 30/9/3 ms; velocity spread .55/.725/.775. The actual beat meter measures saved root mean square offsets, not an asserted finite-sample SD. Dynamics span is normalized to the stated model.
- Computed contrast: brass on panel 10.745:1; brass on section 10.182:1; dark ink on brass 11.463:1; theme text on panel 14.704:1; muted text on section 7.706:1.
- Source checks counted 78 Gymnopédie bars and Entertainer's 152 performed bars with repeats. Score and source evidence are in Scratch. Gymnopédie's full excerpt takes 20 seconds clean; Entertainer takes 6.32 seconds. The overview's 8 to 15 second range conflicts with the required complete passages.

#### Feel check

Best moment: replaying a stored first read beside a practiced take, then seeing the first ear judgment meet the meter. The final sheet makes the student's allocation, repertoire, reflection and first judgments worth showing.

Flat moment 1: the early phone Set hid Add below the fold. The layout now opens with all five Add controls visible and a selected-program strip above them. Flat moment 2: immediate Listen hid the board's earned growth. Practice now holds its readiness result for 850 milliseconds before opening Listen, with the same timing under Motion off. Playback also contracts the wide board so the piano roll gets the main space.

Played the complete tool using actual Tab, Enter and arrow keys: four-piece set, three criteria, nine units, four weeks, listening and rating, natural recital completion, sheet and print preview. The natural recital took 80.7595 seconds. This is deliberate planning and listening, with a specific earned record, rather than a speed reward.

Viewed feel-comparison.jpg beside Beat Lab. Layered painted architecture, walnut, brass, paper and light meet the bar for visual finish. All five art assets were made during this build, not left as placeholders.

#### Done when

1. PASS. Set program, Rubric table and Practice board dominate their modes. During wide playback the board measures 300x484 and the piano roll 995x241. At 680x425, Listen covers the board and the roll is the main visual. Targeted final frames and rectangle checks passed.
2. PASS. All three default programs match 9:54, 9:29 and 9:35. Functional checks verify immediate tempo length and over-budget warning changes.
3. FAIL for literal identity with every engraved note. Minuet intentionally omits engraved ornaments to follow the explicit right-hand sequence. Prelude follows the explicit attack patterns. Minuet left hand, Satie and Joplin were cross-checked against public-domain scores; tied notes are sustained, not re-attacked. Night Bus follows the spec. The conflicting score-versus-explicit-sequence requirement is documented in handoff.md.
4. FAIL for the contradictory narrative examples; PASS for the written formula. All 172 runtime model, threshold, normalization and boundary assertions pass. The differing source examples and unreachable fractional UI splits are listed above.
5. FAIL for completed auditory verification. Seeded wrong pitches, timing, captured tempo, velocity, audio scheduling and identical replay pass mechanical checks. All required Chrome sessions were muted. Headphone judgment of low/95% takes and piano timbre remains open.
6. PASS. Stop clears all oscillators synchronously. Take/week changes interrupt and start immediately. Wide-screen future-week sliders remain usable during an old take; closing Listen keeps playback and restores the full board. Sound off leaves visual playback running. Functional and closing assertions passed.
7. PASS. Hearing completion gates ratings; complete ratings gate meter reveal. First ear persists after changed ratings. Sheet does not reveal an unrated take. Both functional and boundary checks passed.
8. FAIL for roughly one minute. The complete four-piece keyboard recital took 80.7595 seconds with three-second introductions and modeled Flow pauses. Music, target tempo and Flow rule were retained. Stop and Skip act synchronously and passed assertions.
9. PASS for fixed-line dispatch and stale behavior. Held 120 ms clicks at two-second pace show one-time how lines; genuine fits repeat setFits; tired and agree events speak. Read drops an unstarted how line, which speaks on a valid return. A complete four-week plus First read keyboard session covered the sequence. No recorded Umbriel clips were made; browser fallback remains a voice-quality limitation.
10. PASS. Five loaded, original, text-free paintings contain no people. The metronome's code pendulum follows take BPM. Motion off freezes it while keeping tempo text and playback timing. Finished WebPs, native frames and calm playback were inspected.

#### Wave lessons

- Hint and voice: PASS. Hints change immediately and name valid controls. First action is not delayed. Held-click and keyboard logs cover how/event dispatch and Read. Early First read routes to Rubric and focuses its first criterion.
- Focus and layout: PASS for checked paths. Retained controls keep focus; no load autofocus. Native dialogs restore focus, including close/Escape. Narrow Listen moves covered focus to Play. Reset focuses the new Practice week. Real pointer drag with whole-pixel jitter passed after replacing native HTML dragging.
- Sizes: FAIL for complete no-scroll coverage. All eight STANDARDS sizes and four modes were viewed, including 375 via host 8785. Four-piece compact rows and order controls are 44 pixels and fit; all six recital controls fit at 680, 800 and 375. Phone program ordering, long rubric editing and prose dialogs scroll; five-piece boards may scroll on short screens.
- No giveaways: PASS. No meter before hearing and ratings; first judgments stay recorded. The printable sheet respects the gate. Readiness predicts the simulated practice model openly; it is not an answer key to an ear rating.
- Honest numbers: PASS. The screen says A simple model, not a law. The model dialog names invented assumptions and measured RMS wobble. Actual and captured target BPM are shown together during playback. Old takes never change under future tempo edits.
- Standards: PASS. MU:Pr4 selection/tempo/introductions; Pr5 four-week allocation and revision; Pr6 recital; Re9 authored rubric and listening judgment; Cn10 personal program reflection. Each is a student action. No family engine applies.
- Motion off: PASS. Audit found no infinite loops. Calm playback keeps timing, stops decorative movement and shows the numerical tempo.
- Short choices visible: FAIL under a strict reading for phone program-order controls. All five repertoire Add choices, all three venues and all six rubric criteria are visible. Existing program order scrolls on phones. Descriptor and introduction editors are long editable content, not concealed answer choices.
- Resize mid-animation: PASS. Audit resized each state/action and found no exceptions or controls left disabled. Running playback state survives redraw.
- No late welcome: PASS. Adding the first piece explicitly makes welcomeSet stale, as the spec requires. No delayed premise lands after an Add action.
- Unknown as unknown: PASS. Unheard takes cannot be rated. A newly added piece has no fabricated week 4 take; recital and sheet label its absence.
- One look, one meaning: PASS. Gold is RH, blue LH, salmon x marks wrong pitches, the grid tick marks intended timing. Legend is visible and in the canvas accessible name. Readiness also has numbers and words.
- Badge truth: PASS. Budget, readiness, week status and missing-take statements derive from saved state. Readiness is floored for display so a below-50 value does not say 50% Rough.
- Hint changes back: PASS. Mode, playback, stop, week and sheet transitions update the next action synchronously. Returning to the week board restores its planning hint.
- No answer by copied words: PASS. Listening judgments require a completed take and the student's criterion interpretation. Musical facts and descriptors are teaching material, not a word-matching puzzle.

#### Audit leads

Ran the full audit once, within its 40-minute limit: 217 leads, 83 frames. Completed Motion off, mid-action resize, single held controls, five held clicks and quick-tap checks. Every frame was viewed. Detailed one-to-one dispositions: _scratch/recital-practice-plan/audit-dispositions.json, with original audit line numbers for all 212 bullet leads and five first-Add welcome leads.

- Tempo-label overlaps (8 leads): fixed separate label and BPM lines.
- Order-button targets (16 leads across program and notes states): 44 pixels; compact program reflow. Four-row landscape visibility checked again after the last padding repair.
- Rubric targets (30 leads): editors now at least 44 pixels. Count/word lead: hint reworded to levels 4 and 1.
- Program landscape scroll leads (2): repaired proportions/padding. Phone program scroll leads (2): left open as documented above.
- Rubric-table scroll leads (3) and prose-dialog scroll leads (3): accepted long editable content. Choices remain available outside those editors.
- Listen/playing leads (124): covered narrow controls are hidden and inert; focus enters the sheet. Two canvas-caption hit-test leads within this group are false positives addressed with an accessible canvas legend. Wide playing board contracts. Final targeted frames and focus assertions passed.
- Recital action scroll leads (3): fixed with compact action-row reflow; all six actions measured in view at each affected size.
- Notes editor names (5): explicit aria-labels. Notes-background overlap leads (13): explicitly inert native-dialog background, with restored focus.
- Disabled Practice/Recital focus leads (2): expected on the fresh page before prerequisites, not a broken enabled route. Real advanced routes passed actual keyboard use and functional checks.
- First-Add welcome leads (5): expected stale behavior specified explicitly by the spec. Forcing the welcome later would be wrong.

Disposition totals: 200 repaired leads, 2 caption false positives addressed, 7 expected behavior leads, 6 accepted long-editor scroll leads, 2 phone-order scroll leads left open. These are reasoned dispositions, not a claim of a second clean audit. The full audit was not rerun after repairs. Its default walker could not enter prerequisite-locked Practice/Recital; custom states, the actual keyboard run and functional checks cover those paths.

#### Frames looked at

All PNGs shot were opened through contact sheets, with native-size checks of compact Set/Listen/Recital, the phone, print sheet, paintings and metronome. Evidence is under _scratch/recital-practice-plan/.

- Baselines: bar-beat and bar-snow, one frame each; side-by-side feel-comparison.jpg.
- Early and detail work: early (3), details (4), phone (5), edges (8), functional/fixed/final (one each), model (1), gate (1), drag/fixed (one each), voice (1), voice-fixed (2).
- Full late sweep: full (32), four modes at all eight STANDARDS sizes. No console findings.
- Actual keyboard session: keyboard (6), including completed recital and print preview; natural runtime and error log saved separately.
- Full audit: audit (83), viewed in seven contact sheets.
- Targeted post-audit: final-frames (23), close-frames (4), close-narrow-frames (1), functional-closing (1). Successful reruns replace test-harness failures; even failure snapshots were viewed.

#### Art made

Five generated images, no people, faces, body parts, lettering or logos. Total finished art 492054 bytes, 480.52 KiB. Final bundle 797.73 KiB. Practice/library/senior/cafe are 1200x675; metronome is a 400x680 cutout. Full house style, prompts, raw PNGs and codex provenance are included. All finished images were inspected.

No redraw was needed. Senior and cafe were recompressed at quality 65 to meet the 120 KiB per-image ceiling. The green-key metronome uses despill; its tiny native-edge fringe is unobtrusive at its actual display size. Only free art.py --rekey processing was used. Generated-image credit is in tool.draft.json.

#### Art still to paint

None. All five specified paintings are present. Recital audience silhouettes are simple code shapes as specified.

#### Engine changes wanted

None. Kit files were not edited. The local implementation uses the kit theme, voice, motion, sound state and audio context. The spec explicitly exempts this read-only take viewer from music-studio.js.

#### Left open

- Written model versus narrative example conflicts; literal score ornament conflict; 8 to 15 second passage range; four-piece recital duration. Details and chosen interpretation are in handoff.md. Spec was not changed.
- Headphone comparison of low and high readiness and the piano-like timbre remains unverified. Recorded Umbriel narration is absent under the no-recording instruction; browser voice quality varies.
- Phone program ordering and long editors scroll. Five-piece boards can scroll on compact screens. No full post-repair audit was run, only targeted affected-size and functional checks.
- A newly added piece after week 4 is explicitly unprepared. A fresh four-week cycle is required to obtain its week 4 take.
- Scope mistake: required baseline bundle commands refreshed ignored generated HTML outputs for Beat Lab and Snowy Mail Route outside the two authorized write folders. Their sources were untouched. This was disclosed during the build. All authored content and evidence stayed in the authorized tool/Scratch folders.
- The report was assembled in Scratch until completion, honoring the user's instruction to stop when codex-report.md is written rather than the generic brief's early-report instruction.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: recital-practice-plan
#### Played
Reviewed as a grade 9-12 student and a projected classroom tool. The painted rooms, brass program board and audible practice budget feel worth keeping.
Cold play covered Set, Rubric, four weeks and the final recital piece before reading builder materials. Its 75-second wait ended before the automatic sheet; the later keyboard-only recheck reached natural completion in about 98 seconds with no exceptions.
#### Findings fixed
- **Blocker, general, Listen/Recital:** x marks, timing references and measured BPM exposed ear-rating answers. Diagnostics, velocity shading and readiness readouts now wait for judgment and reveal; unplayed notes stay unknown. Recital shows captured target BPM until its tempo judgment is revealed.
- **Blocker, general, rubric changes:** a global reveal exposed newly added criteria before rating. Each criterion now has its own reveal record and gate.
- **Blocker, general, agreement:** copying the revealed answer could masquerade as hearing correctly. Feedback compares immutable first ear; the same reveal cannot be farmed.
- **Blocker, general, recital:** skipping every passage could claim completion. Skips/missing takes are named; changes invalidate the record; old completion-only saves lose that badge; fewer than two pieces cannot begin.
- **Should fix, general, voice:** the main path dropped Listen's how line. Shorter Practice/Listen/Recital instructions and a completion-time rating instruction now start in the proper sequence.
- **Should fix, general, compact Listen:** five revealed criteria overlapped. Content-height feedback rows and a shared toolbar keep the controls clear; all five initial rating groups fit at 680x425 and 375x812.
- **Should fix, general, long introductions:** 200 wide characters covered the title/program/keyboard. Long text now scrolls in its own bounded area, with the presentation controls visible.
- **Should fix, general, focus:** revealing the meter disabled its focused button. Focus now goes to the scrollable comparisons; stale meter instructions are hushed.
- **Should fix, general, hints:** a fitted set and finished week 4 did not clearly lead onward. Hints now name Rubric/Notes or Recital as appropriate.
- **Should fix, general, final audit frames:** phone programs hid reorder buttons; the 1280x720 board clipped Flow. Program rows now expand, Notes moves to the phone header, and compact practice spacing exposes Flow. Venue paintings remain in the choices/full recital scene.
- **Polish, general, numbers:** a 0.257-second overrun said Over by 0:00. It now says Just over 10:00; the under-limit counterpart is also handled.
- **Polish, general, words:** one wrong note is singular; rating endpoints recall the student's descriptions; the discussion question no longer assumes neglect.
- **Polish, graphics/play:** rekeyed the metronome's green fringe and added a shaded, pitch-accurate recital keyboard driven by the saved audio events. No new mode, topic or score.
#### Findings left
- **Spec conflicts:** exact note-for-note engraving versus the explicit ornament-free Minuet; approximate model examples versus the written equation; full passages versus 8-15 seconds/about one minute. The explicit content/formula remains unchanged.
- **Judgment calls:** the senior-center notes assume childhood/film familiarity. These fictional venue suggestions need the cultural review named below.
#### Break it
- Right notes/beat/tempo/dynamics: tried no-listen clicks, partial play then Stop, constant guesses, option sweeps, copying revealed answers, repeat reveal, swapping criteria and opening the sheet. Completion gates hold; first judgments survive; new meters remain hidden; copied revisions earn no first-ear agreement.
- Readiness/minutes/method/Flow: swept every allocation to maximum, tried zero-minute weeks and replayed old takes. Budget never exceeded 270 minutes; a zero-minute week applies an 8% readiness reduction; a replay is immutable; the sheet labels the simple simulation assumptions. No best score exists.
- Recital: Skip-all, Skip mid-take, Stop, changed program and an unrated sheet. Audio stops immediately; skip-all records four skips and no completion; an unrated sheet reveals no meter.
- Final shortcut regression: **28/28 passed**, `_scratch/recital-practice-plan/break-final-results.json`.
- Keyboard-only Tab/Enter/arrow run: program, rubric, allocation, four weeks, take/rating/meter and uninterrupted recital to the sheet passed, with no runtime exceptions.
#### Voice walk
Sound on, Motion on, held 120 ms clicks at a two-second action pace: venue, four Add buttons, Rubric/three criteria, Practice/sliders, practice week, Play take, ratings, meter, next three weeks, Recital/Begin.
Started in order: welcomeSet, setFits, welcomeRubric, welcomePractice, listenHow, rateHow, meterHow, welcomeRecital. Each how started once. Some completed actions cut their instruction; none of these how lines was lost unstarted on this path.
| Side-path line | Expected | Spoken |
|---|---:|---:|
| setFits, genuine fit entries | 5 | 5 |
| listenHow, five Listen entries | 1 | 1 |
| tired, five matching budgets | 5 | 5 |
| agree, five known-correct first judgments | 5 | 5 |
Evidence: `review-voice/recital-skipped.json`, `review-events/results.json`, `review-keyboard/result.json` in Scratch. The fatigue line names a budget/model assumption, including when minutes are unused.
All ten fixed strings match voice/lines.json and allLines. Chrome was muted as required; these are utterance-start/scheduling checks, not a headphone judgment. Umbriel recordings remain absent under the no-recording rule.
#### Facts checked
- **Petzold/Minuet:** Christian Petzold attribution, former Bach credit and the circa-1725 notebook context: [IMSLP work record](https://imslp.org/wiki/Minuet_(Pezold,_Christian)). Checked both-hand attacks against the saved Waldersee score and explicit spec sequence; omitted ornaments remain a stated conflict.
- **Bach/Prelude:** BWV 846, 1722, WTC Book I: [IMSLP work record](https://imslp.org/wiki/Prelude_and_Fugue_in_C_major,_BWV_846_(Bach,_Johann_Sebastian)). The four attack shapes match the explicit brief; no claim of literal engraved sustain durations.
- **Satie:** 1888, Lent et douloureux, 78 bars in 3/4, bars 5-12 including the tied F sharp: [IMSLP score](https://vmirror.imslp.org/files/imglnks/usimg/0/0d/IMSLP08284-Satie_-_Trois_Gymnopedies_%28typeset%29.pdf), compared with saved page 1.
- **Joplin:** 1902, Not fast, both hands of A-section bars 5-8/printed bars 9-12 and 152 performed bars: [first-edition score](https://s9.imslp.org/files/imglnks/usimg/8/80/IMSLP02607-Joplin_-_The_Entertainer.pdf). The 1973 film association is confirmed by [AFI](https://catalog.afi.com/Film/54391-THE-STING).
- **Invented content:** Night Bus notes, dates, venues/audience size, difficulties, targets and numerical model are defined by the spec and labeled fictional/model content. They are not research findings about a musician.
- **Numbers:** independent Python gives piece lengths 1:39, 2:07, 3:15, 4:00, 1:14 and exactly the three listed-tempo sets 9:54, 9:29, 9:35, including 20 seconds per introduction. Four-week ranges match the equation; 60x7 has 357 effective minutes, slightly less than 60x6's 360.
- **Contradictory examples:** Entertainer even allocation gives 63.01%, 35% allocation gives 87.91%, and the other hard passages give 84.96%/72.38%. The spec's 64%/85%/72-79% narrative is approximate or wrong; formula wins. Evidence: numbers.json and review-math.json in Scratch.
- **Contrast:** independently recomputed brass/panel 10.74:1, brass/section 10.18:1, dark/brass 11.46:1, body/panel 14.70:1, muted/section 7.71:1. Grayscale frame inspected.
- **Practice rest:** [BAPAM](https://www.bapam.org.uk/when-the-curtain-goes-up-again-building-our-fitness-to-perform/) supports practice breaks; it does not validate this tool's invented seven-day/0.85 rule. The spoken line now makes that distinction.
- **Standards:** selection/context/introductions, allocation/revision, presentation, authored criteria/listening and personal reflection provide actions for Pr4, Pr5, Pr6, Re9 and Cn10: [NCAS Harmonizing Instruments](https://nationalartsstandards.org/content/harmonizing-instruments-introduction). This is a simulation, not evidence of actual instrumental performance proficiency.
#### Sensitivity
European/American piano examples do not represent all music cultures. A cultural reviewer should check Petzold/Bach attribution, Joplin's authorship before the later film, and assumptions about older audiences. Five paintings have no people; the code audience uses faceless silhouettes. No Native, religious or hard-history content.
#### Flattest moment left
Writing rubric descriptors is deliberately quiet. The recital's long listening stretches now have a synchronized keyboard; full required passages and modeled slow tempos still make neglected programs take longer.
#### Graphics
All five finished WebPs inspected; the four warm interiors were retained. The metronome was reprocessed from its raw painting with free art.py --rekey and holes:true. No raster redraw/addition or people asset was needed.
Compared frames with existing Beat Lab and Snowy Mail Route bundles without rebundling or changing them. The recital retains depth, material, light and its brass accent. Final bundle size: 827 kB (826,598 bytes).
#### Audit
Single final audit completed within 40 minutes: all STANDARDS sizes/states, Motion off, held/repeat/quick clicks and mid-action resize; no exceptions or stuck controls. All 100 frames inspected through nine contact sheets, with native frames for confirmed faults. Evidence: `review-audit/audit.md` in Scratch.
Its 16 leads: one phone reorder defect repaired; three rubric-table and three program-notes editor scroll leads are intentional long editors; the hidden background hint is inert behind the modal; two disabled prerequisite mode buttons are expected; five first-Add welcomes are deliberately canceled as stale per spec; the Recital disabled-Begin lead refers to canceled narration (runtime cancellation rechecked). No short choice list remains clipped.
After the audit, twelve focused frames passed with zero console errors: phone programs with 0/1/2/4/5 pieces (all Add/order/venue/Notes targets visible, at least 44 px, no scroll); Notes resize/modal focus restoration; unjudged recital BPM at 680/1366/375 and revealed BPM; 1280 board/Listen. All twelve opened at native size. `review-close-checks.json` records assertions. No second audit or broad review was run.
#### Left open
No kit or spec edits, commits, external uploads or registrations. All authored changes/evidence are inside the two permitted folders. All browser/server commands exited; the temporary host is removed and ports 8755/9950-9957 are closed. WMI process inventory was denied, so cleanup verification uses command exit/driver cleanup and port checks.
Procedural limits: the cold run stopped before its automatic sheet; later full keyboard validation completed it. The first required-doc read used the tool's wait bound rather than an explicit subprocess timeout; subsequent commands have explicit limits. A long drive evaluation timed out at its 60-second CDP cap; the uninterrupted recital was then checked with bounded separate polling.
The formula/example, engraving/explicit-sequence and recital-duration conflicts require spec decisions, not an improvised new feature. Recorded-voice naturalness and piano timbre remain unverified acoustically.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Recital Practice Plan build handoff

#### Cold review changes

Preserved the painted rooms, brass program board, model and deterministic takes. Listen now withholds diagnostic x marks, timing ticks, velocity shading, actual BPM and readiness readouts until meter reveal. Reveals are tracked per criterion, so swapping the rubric cannot expose a new meter without a judgment. Agreement uses immutable first ear values, and each meter can be revealed only once per criterion. The sheet follows the same rule.

Shortened Practice, Listen and Recital how lines and added the rating instruction at take completion. Listen entry drops stale planning narration before its short how line. Match voice/lines.json to the source before recording.

Added a shaded SVG keyboard inside the existing recital program card. It lights actual saved pitches using the existing playback frame, resets between pieces and on Stop, and adds no scoring or input. The metronome was processed again with art.py --rekey and holes:true to remove the green fringe.

Skip-all no longer marks a recital complete. The last finished playback records skipped and missing passages on the sheet. Program changes invalidate that record, fewer than two pieces cannot begin, and old saves without this playback record cannot retain a legacy completion badge. Takes and practice progress remain intact.

Compact Listen uses one toolbar so five first-ear rows fit. Revealed comparisons use content-height rows in a keyboard-scrollable region. Phone recital cards use a compact grid; long introductions scroll inside their own area without covering the program or keyboard. Subsecond timing overruns say Just over rather than Over by 0:00.

The final audit confirmed hidden phone reorder buttons. Selected programs now expand to all rows; Notes moves into the phone header with its full accessible name and keeps focus across resizing. The venue paintings remain in the choice cards and full recital scene. Empty/one-piece panels use less blank height. At 1280x720, tighter practice spacing keeps the Flow control visible. Recital BPM stays labeled as the captured target until that take's tempo judgment has been revealed, closing a side path around Listen's blind comparison.

#### Structure

src.html starts from the kit starter, with kit:curio and kit:theme-912. CSS lays out four responsive views at real pixel sizes. content.json is bundled through json:content and holds piece facts, note attacks, hand labels, criteria, venue notes and score provenance. The script contains state, model, deterministic takes, program editor, rubric, weekly board, piano-roll renderer, Web Audio voice, recital scheduler and device-only persistence. window.__tool exposes the model, state and principal actions for review.

Recorded takes are stored as immutable note events with a seed, captured tempo, readiness and metrics. Future plans do not regenerate them. Audio schedules oscillator onsets against AudioContext time rather than animation frames. Two detuned triangles have a fast decay. Stop disconnects every oscillator synchronously. Sound off disconnects audio without changing visual timing; Sound on schedules only future notes.

While a take plays on a wide screen, the board contracts to 300 pixels so the piano roll becomes the main view. Closing Listen restores the full board while playback continues. Narrow Listen hides and makes covered controls inert, moving covered keyboard focus to Play take. Native dialogs make the background inert and restore focus on close, including Escape. Start over focuses the new Practice week.

Curio.voice owns fixed narration and Read. Hints change synchronously and lines have validity checks. voice/lines.json names easy-coach, Umbriel. No speech is recorded in this build, so narration uses the browser fallback. Introductions are displayed, not spoken.

#### Open questions and resolved ambiguities

The spec has no explicit open-question list. These conflicts or unspecified choices follow its stated direction:

- The user requests image-tool art during the build. All five assets were made with the built-in OpenAI image tool, despite the older Art paragraph naming local FLUX. No generated people or body parts. Audience silhouettes are code shapes as specified.
- The report is assembled in Scratch and written to codex-report.md only at the end. The user's instruction to stop as soon as that file is written takes precedence over the brief's request to start it early.
- The written exponential formula wins over narrative approximations. Four-piece, nine-unit even-split results are 56.36 to 73.67% at 30x5; 73.13 to 89.17% at 45x6; 81.32 to 94.44% at 60x6; and 81.09 to 94.32% at 60x7. The last case is slightly below 60x6 because 420x0.85 is 357, not 360 effective minutes.
- Three-piece Entertainer reaches 63.01% with 270/7 minutes per unit for four weeks. At 35% of each week's minutes it reaches 87.91%, rather than the spec's 85%. The other 65% divided across six units gives Gymnopédie hard 84.96% and Night Bus hard 72.38%, rather than both being 72 to 79%. Formula and difficulties are retained; spec.md is unchanged.
- Exact even splits of 150, 360 and 420 minutes across nine units cannot use the required 15 minute slider step. Formula checks use exact fractions. The 270-minute even split is achievable in the UI at 30 minutes per unit.
- Gymnopédie's complete eight-bar passage takes 20 seconds at the listed tempo even at full readiness. The Entertainer's four 2/4 bars take 6.32 seconds. Neither can meet the overview's 8 to 15 second range without changing music or tempo. Full notes and model tempo win. The complete four-piece keyboard run took 80.7595 seconds, exceeding the roughly one-minute target.
- The Flow rule's one-to-four-second pause takes precedence over the overview's fixed one-second pause.
- The beat meter measures actual root mean square timing offsets from the saved take. The stated standard deviation is a distribution parameter, not a finite-sample guarantee; the model note explains the measurement.
- Fixed meter thresholds remain fixed when descriptors are edited. Shape and Keeps going remain ears-only.
- Practice and First read require three chosen rubric criteria. An early First read routes to Rubric and focuses the first criterion, so a student establishes criteria before hearing a take. The intermediate level 3 and 2 descriptions are fixed neutral scaffolding; the specified level 4 and 1 fields are editable.
- Playback reports actual BPM beside the take's captured target BPM. Later tempo changes affect future takes only. A newly added piece without a selected week's take falls back to its First read.
- Minuet's explicit right-hand sequence wins over engraved ornaments. Satie ties are merged, including the F sharp across bars 9 to 12. Joplin A-section bars 5 to 8 mean printed bars 9 to 12 after the introduction. Mutopia public-domain original-edition sources cross-check the IMSLP scans.
- The compact board uses two columns of 44 pixel rows to preserve the standing target-size rule. A four-piece set keeps nine units visible. Readiness words and numbers move into the unit name block. Five pieces may need board scrolling on short screens.
- All five Add choices remain visible on phones. The selected program's ordering controls scroll inside its shorter strip there. The editable rubric and long introduction dialog also scroll on compact screens. These are documented limitations, not hidden answer choices.
- Venue notes, reflection and introductions are under Venue notes & introductions immediately beneath the program. Its dialog preserves the large program and repertoire choices.
- A piece added after week 4 has no week 4 practiced take. Recital and sheet label the missing take and invite a new practice cycle. No performance is fabricated.
- Recorded weeks are read-only. Their takes can replay while an unplayed week's sliders are edited. Week board closes the listening sheet without stopping the take; First read or Listen returns to Stop.

#### Engine changes wanted

None. No kit engine changes are required.

#### Sensitivity

This is a small European and American piano selection, not a survey of musical cultures. Keep Christian Petzold's authorship distinct from Bach's notebook and credit Scott Joplin as the composer of The Entertainer, rather than treating the later film as its origin. A cultural reviewer should consider the senior-center notes' assumptions about listeners' childhood repertoire and film familiarity. The fictional venue notes are guidance, not facts about older adults. All five paintings contain no people; the audience uses code silhouettes.

#### Art

Five paintings are in art/raw with finished WebP assets in art/. Full prompts and codex provenance are in art/prompts.json. Backgrounds are 1200 pixels wide. Senior and cafe were recompressed at quality 65 to stay below 120 KB each. The metronome uses a green-key cutout with despill and a code pendulum.

#### Review next

Read codex-report.md for final checks and audit dispositions. The full audit finished once with 217 leads and 83 frames. _scratch/recital-practice-plan/audit-dispositions.json accounts for 212 bullet leads and the five first-Add welcome leads. Targeted repairs address tempo labels, 44 pixel targets, covered controls, dialog names, compact recital actions and focus. The full audit was not repeated after those repairs. The final functional run passed 49 checks; 16 additional closing assertions passed. Earlier model and boundary checks passed 172 assertions.

Evidence lives at _scratch/recital-practice-plan/ in the repository. This is Build only, with no commits or polish round. Headphone review of the piano and naturalness of browser narration remain human review tasks. Browser voice is a fallback, not a recording of Umbriel.

The required baseline bundle commands refreshed two ignored generated HTML files outside the authorized folders. Their sources were untouched. That was a scope mistake and was disclosed during the build. All authored content and evidence are in the authorized tool and Scratch folders.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
