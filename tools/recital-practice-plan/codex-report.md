# Codex report: recital-practice-plan

## Built

Built the offline grade 9 to 12 tool in Set, Rubric, Practice and Recital modes. The program, rubric, four-week budget, seeded piano takes, ear ratings, gated meter, venue introductions, recital and printable personal sheet are connected. Five original paintings supply the rooms and metronome. Device-only saving uses curio-recital-plan.

The final bundle is 816875 bytes, 797.73 KiB. Source is readable, 1612 lines, maximum 160 characters. Node syntax check passed. Required files and JSON checked. No network API or remote runtime source exists in the tool. No commits, branch changes or polish round. Task Chrome processes and ports 9980, 9981 and 8785 are closed; host.html is absent.

Final functional run: 49/49 assertions passed. Additional closing checks: 16/16 passed. Independent model and boundary checks: 172/172 passed. Runtime driver logs report no console errors, warnings or exceptions. Test-harness mistakes were corrected before the passing runs: wrong selected passage, a nonexistent test selector, and reused localStorage between independent scenarios.

## Numbers check

Independent Python evidence: _scratch/recital-practice-plan/calc-evidence.py and numbers.json. Runtime comparison: model-results.json.

- Five lengths round to 1:39, 2:07, 3:15, 4:00 and 1:14. Exhaustive default-tempo subset checks find exactly the three legal sets: 9:54, 9:29 and 9:35, including 20 seconds per introduction.
- Four-week hard-passage percentages for the four-piece set, in piece order: 30x5 gives 73.665/61.859/69.134/56.360; 45x6 gives 89.173/78.912/85.593/73.127; 60x6 gives 94.441/86.479/91.864/81.319; 60x7 gives 94.316/86.277/91.707/81.092. Runtime results match independent calculation within 0.001 percentage points.
- 60x7 is slightly below 60x6: 420x0.85 = 357 effective minutes, versus 360. It is close, not identical.
- Three-piece Entertainer even split gives 63.01%, not 64%; 35% allocation gives 87.91%, not 85%. Other hard passages give 84.96% and 72.38%, not both 72 to 79%. The specified formula and difficulties win; spec.md is unchanged.
- Exact even splits across nine units at 150, 360 or 420 minutes cannot be entered with 15 minute slider steps. The 270-minute split is achievable at 30 minutes per unit. Fractional model checks exercise the formula separately.
- At readiness .5/.85/.95: expected wrong notes in 40 are 3.5355/.58095/.11180; tempo is 87.5/96.25/98.75%; wobble distribution SD is 30/9/3 ms; velocity spread .55/.725/.775. The actual beat meter measures saved root mean square offsets, not an asserted finite-sample SD. Dynamics span is normalized to the stated model.
- Computed contrast: brass on panel 10.745:1; brass on section 10.182:1; dark ink on brass 11.463:1; theme text on panel 14.704:1; muted text on section 7.706:1.
- Source checks counted 78 Gymnopédie bars and Entertainer's 152 performed bars with repeats. Score and source evidence are in Scratch. Gymnopédie's full excerpt takes 20 seconds clean; Entertainer takes 6.32 seconds. The overview's 8 to 15 second range conflicts with the required complete passages.

## Feel check

Best moment: replaying a stored first read beside a practiced take, then seeing the first ear judgment meet the meter. The final sheet makes the student's allocation, repertoire, reflection and first judgments worth showing.

Flat moment 1: the early phone Set hid Add below the fold. The layout now opens with all five Add controls visible and a selected-program strip above them. Flat moment 2: immediate Listen hid the board's earned growth. Practice now holds its readiness result for 850 milliseconds before opening Listen, with the same timing under Motion off. Playback also contracts the wide board so the piano roll gets the main space.

Played the complete tool using actual Tab, Enter and arrow keys: four-piece set, three criteria, nine units, four weeks, listening and rating, natural recital completion, sheet and print preview. The natural recital took 80.7595 seconds. This is deliberate planning and listening, with a specific earned record, rather than a speed reward.

Viewed feel-comparison.jpg beside Beat Lab. Layered painted architecture, walnut, brass, paper and light meet the bar for visual finish. All five art assets were made during this build, not left as placeholders.

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

All PNGs shot were opened through contact sheets, with native-size checks of compact Set/Listen/Recital, the phone, print sheet, paintings and metronome. Evidence is under _scratch/recital-practice-plan/.

- Baselines: bar-beat and bar-snow, one frame each; side-by-side feel-comparison.jpg.
- Early and detail work: early (3), details (4), phone (5), edges (8), functional/fixed/final (one each), model (1), gate (1), drag/fixed (one each), voice (1), voice-fixed (2).
- Full late sweep: full (32), four modes at all eight STANDARDS sizes. No console findings.
- Actual keyboard session: keyboard (6), including completed recital and print preview; natural runtime and error log saved separately.
- Full audit: audit (83), viewed in seven contact sheets.
- Targeted post-audit: final-frames (23), close-frames (4), close-narrow-frames (1), functional-closing (1). Successful reruns replace test-harness failures; even failure snapshots were viewed.

## Art made

Five generated images, no people, faces, body parts, lettering or logos. Total finished art 492054 bytes, 480.52 KiB. Final bundle 797.73 KiB. Practice/library/senior/cafe are 1200x675; metronome is a 400x680 cutout. Full house style, prompts, raw PNGs and codex provenance are included. All finished images were inspected.

No redraw was needed. Senior and cafe were recompressed at quality 65 to meet the 120 KiB per-image ceiling. The green-key metronome uses despill; its tiny native-edge fringe is unobtrusive at its actual display size. Only free art.py --rekey processing was used. Generated-image credit is in tool.draft.json.

## Art still to paint

None. All five specified paintings are present. Recital audience silhouettes are simple code shapes as specified.

## Engine changes wanted

None. Kit files were not edited. The local implementation uses the kit theme, voice, motion, sound state and audio context. The spec explicitly exempts this read-only take viewer from music-studio.js.

## Left open

- Written model versus narrative example conflicts; literal score ornament conflict; 8 to 15 second passage range; four-piece recital duration. Details and chosen interpretation are in handoff.md. Spec was not changed.
- Headphone comparison of low and high readiness and the piano-like timbre remains unverified. Recorded Umbriel narration is absent under the no-recording instruction; browser voice quality varies.
- Phone program ordering and long editors scroll. Five-piece boards can scroll on compact screens. No full post-repair audit was run, only targeted affected-size and functional checks.
- A newly added piece after week 4 is explicitly unprepared. A fresh four-week cycle is required to obtain its week 4 take.
- Scope mistake: required baseline bundle commands refreshed ignored generated HTML outputs for Beat Lab and Snowy Mail Route outside the two authorized write folders. Their sources were untouched. This was disclosed during the build. All authored content and evidence stayed in the authorized tool/Scratch folders.
- The report was assembled in Scratch until completion, honoring the user's instruction to stop when codex-report.md is written rather than the generic brief's early-report instruction.
