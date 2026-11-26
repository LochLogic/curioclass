# Recital Stage Directions: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: recital-stage-directions

#### Built

Built the offline grades 3-5 tool with Stage map, Recital and Your turn. Draft stage is built.
It uses the shared dance engine, Curio Class settings and Curio.voice. No shared files were edited intentionally,
no git operations were performed, no audio was recorded and no polish round was started.

Features include both viewpoints, nine areas, three identifiable dancers, drag/tap/keyboard placement,
eight optional calls, live costumes and lights, two 24-count pieces, clue replay, main ideas,
the eight-trait Compare board, three spoken room phrases and guarded device-only saving/reset.

Final bundle: 475,933 bytes, 464.78 KiB, below 2 MB. All owned browsers and servers are closed; host.html is absent.

#### Numbers check

Independent calculations are in `_scratch/recital-stage-directions/numbers.py` and `numbers.txt`.

- 24 counts at 72 beats a minute = 20 seconds; at 104 = 13.846154 seconds.
- Followed the detailed Content value of 20 seconds for Autumn Leaves, rather than the earlier 15-18 second summary.
- Room phrases: 28 movement counts + 16 lead-in counts = 26.4 seconds at 100, or 33 seconds at 80, plus calls.
- Stage right mirrors from x 0-33.3333 to screen x 66.6667-100. Call 8 accepts UL, CL and DL, including shared areas.
- Spec contrast ratios recompute to 10.32, 15.59, 8.45, 12.87, 8.52 and 12.21 to one.
- All six dancer phrases total 24 counts. Sampled positions remain finite.
- Final sink samples decrease from head height 1.0173 to 0.5742 body heights without rising again.
- Jazz jump samples have one airborne star shape, then grounded landing and freezes. Anticipations precede 12 and 16.

#### Feel check

Played the cycle through placement, calls, both full recital runs, clues, ideas, Compare and a complete slower room phrase.
Best moment: flipping a populated stage and seeing the guide's own hand identity and the dancer badges stay attached.
The student's lights and costumes also remain live while the recital continues.

Two flattest moments and changes:

- Both initially showed a small sample. It now presents two troupes of three, with each piece's saved production choices.
- Phone clue reading felt like scrolling through homework. Its shorter stage and fixed actions now keep all eight clues visible.

The bar comparison exposed a flat floor. Added shaded floorboards, seams, fasteners, velvet shading and actor contact shadows.
The theater uses both paintings prominently. The temporary kit figures remain the main visual limitation.

![Tool beside the bar tools](S:/CurioClass-codex/_scratch/recital-stage-directions/bar-comparison.png)

#### Done when

1. FAIL under a strict always-visible-plan reading. Initial Stage map focus, toggle and plan pass at 1366, 680 and 375.
   Phone clue/idea reading deliberately hides the plan to fit the answer choices. See responsive limits in handoff.md.
2. PASS. Seats put stage left on screen right; reverse puts it on screen left. Geometry checks confirm hand identity
   and unchanged canonical dancer positions. The 800 ms camera transition is an approximation, not full 3D.
3. PASS. All eight reference calls pass; negative cases reject audience-left placements for call 8 and invalid call 4 counts.
   Straight center and diagonal formations retain exact area centers. Shared areas hold up to three dancers.
4. PASS. Held clicks changed costume, light, view and clue selection during Watch while its clock continued beyond count 15.
5. PASS. Correct clues replay into their count and freeze; wrong clues identify their absence. Both idea choices give feedback.
6. PASS. All eight traits were placed and checked. Each plays two counts; Both displays six figures in two groups.
7. PASS for sequencing and timing. Calls are awaited before lead-ins; a complete silent Slower run finished at 80.
   A sound change continued into count 3; Read stopped counting before speaking. Acoustic review remains open.
8. PASS. Five held selections at a two-second pace produced one spoken how line and four heard/silent repeats.
   Five correct checks produced five spoken event lines. Mode/step welcome validity is guarded.
9. PASS. Costume, light color, unlit UR, clue choices and a partial Compare board survived fresh tabs.
   Start over removed the storage item and reset choices; storage failures and malformed values are guarded.

#### Wave lessons

- Hint and voice: PASS. Hints update synchronously, name current controls, and Read includes an active stage call.
- Focus and layout: PASS in targeted runs. Persistent controls retain focus; natural Tab/Enter/arrows solved call 1.
  Reverse arrows retained dancer focus. The guide moves within C and shrinks when it shares the area.
- Sizes: FAIL for the strict universal target/scrolling rule. Main actions fit; some perspective tiles are under 44 pixels,
  with 44-pixel plan alternatives. Phone production options and setup details still require page scrolling.
- No giveaways: FAIL for the specified main-idea title cue described below. Badge shapes and grid IDs reveal no call answers.
- Honest numbers: PASS. Beat rates and count totals are explicit; calculations and coordinate rules were recomputed.
- Standards: PASS. Solo actions teach area use/timing, production choices, movement evidence and comparison of the two pieces.
- Motion off: PASS in frames and source checks. Idle glow stops; the engine retains count pacing and steps poses by count.
- Short choices visible: FAIL for phone production choices. Clues and main-idea choices fit; secondary dress/light options scroll.
- Resize mid-animation: FAIL as a completed verification claim. Relayout preserves world state, but the mechanical audit
  did not finish its report. Live view/costume/light changes were checked separately; a cold resize recheck remains.
- Welcome put off past first action: PASS. No welcomeAfter; valid/needs guards prevent hidden-step and Compare welcomes.
- Unknown shown as unknown: PASS. Calls have no ticks before Check; unplaced Compare traits remain unassigned.
- One look, one meaning: PASS. Circle, square and triangle retain identity; ticks/crosses also carry words.
- Badge says what is true: PASS. Area status comes from placement; old call verdicts clear on Next call and reset.
- Hint changes back: PASS. Mode, step, piece and phrase changes update current hints/captions and clear stale results.
- No answer by copying words: FAIL. Autumn Leaves and its correct idea share leaves. Preserved the spec and documented it.

#### Audit leads

Audit not finished. The single command reached its 40-minute limit during the control/voice walk.
It produced 81 PNGs but no audit.md, so there is no completed mechanical lead list to claim or dismiss.
Evidence and timeout record are in `_scratch/recital-stage-directions/audit/`.

Frame/source issues repaired during this build included mirrored negative-width rectangles, guide/actor collisions,
compact primary buttons below the fold, tiny setup-diagram text, phone action overlap, stale captions/hints,
looping sink/jump keyframes and hidden-control welcomes. Final targeted batches had zero console errors.
The full size sweep and audit were not repeated after these targeted repairs.

#### Frames looked at

All manual shot batches were viewed as full frames or labeled contact sheets; all 81 audit PNGs were viewed in 14 sheets.
Scratch contains `early`, `early-fixed`, `checks`, `late-checks`, `sizes`, `phone-early`, `phone-final`,
`targeted`, `phone-targeted`, `final-checks`, `extra-targets`, `phone-last`, `phone-last-fixed`,
`phone-last-final`, `keyboard-only`, the audit frames and the two bar frames.

The size sweep covers 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a 375x812 iframe.
It includes all modes, reverse view, calls, clues, ideas, Compare, Motion off and grayscale.
Later shots rechecked only affected layouts or behavior. Both full recital completions preceded the final keyframe repair;
the repaired keyframes were then sampled independently and the final floor curl was rendered and inspected.

#### Art made

Two images generated with the built-in imagegen tool: house-from-stage and recital-backdrop.
Both are used, copied into art/raw, processed only with free art.py --rekey, and inspected at 1400 pixels wide.
Total finished art: 217,670 bytes, 212.57 KiB. No redraws were needed. No people were generated.
Full prompts, house style and provenance are in art/prompts.json. Credit is in tool.draft.json and the source comment.

#### Art still to paint

Fifteen deferred people:true pose sets cover the guide and recital dancers, including facings, sides, gait keyframes,
badges and costume variants. Detailed movement requirements include the one-way sink and pre-beat clap.
POSE_ART tokens and the renderer adapter keep the current kit figures replaceable. Painted dancers are the owner's final choice.

#### Engine changes wanted

- kit/dance.js, floor().resize: make x0/x1 describe actual front-edge pixels for stage's d0=140 projection.
- kit/dance.js, floor projection/inverse and figure projection: add a documented orbit/mirror interface that retains
  hand identity and avoids negative-width decoration. The build uses a local adapter; details are in handoff.md.

#### Left open

- The mechanical audit did not finish. This is a build, not a clean audit or a post-build review.
- Painted dancers remain intentionally deferred; the authorized kit figures are temporary.
- Browser speech is the current fallback for easy-coach/Umbriel. No recordings or human headphone review were made.
- Phone production/setup scrolling, small perspective hit regions and the hidden phone evidence plan need cold review.
- The camera orbit is approximated; the family catalog question remains outside the allowed write scope.
- The main-idea word cue needs a spec/teaching decision. A fresh content review passed the history and jazz study,
  with pre-beat accents and a clearly low ending pose implemented as requested.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: recital-stage-directions

#### Played

Cold as a grade 4 student, then as a projecting teacher: camera flips and production choices were strong; code figures and answer hunting were weak.
Played calls, both full pieces, clue replays, all idea choices, Compare and a full room phrase before opening builder notes/source.

#### Findings fixed

- Blocker, general, Recital: any two guesses opened Compare without watching. Require completed watches, four fitting movement clues and supported ideas.
- Blocker, general, clues: separate answer columns and replay verdicts disclosed the set. Shuffle cards; replay actual movement without naming the right cards.
- Blocker, general, idea checks: answer sweeping could earn praise. A wrong idea needs another complete watch; retry survives reload; all-card selection fails.
- Blocker, general, Compare: incremental N-of-8 feedback allowed hill climbing. Use collective feedback; clear stale results on edits.
- Should fix, general, people art: painted three varied dancers in front/back sheets; articulated paint replaces every visible kit figure and icon.
- Should fix, family:dance, arabesque: the rear leg disappeared from the seats. Turn that dancer sideways; retain the long balanced line.
- Should fix, general, phone: production/setup scrolling and hidden evidence plan. Compact header/desk, visible inset, full-sized plan targets and all short choices in view.
- Should fix, general, Compare clips: hidden bin controls lost their usefulness during replay. Keep bins and source traits live, with movement visible between them.
- Should fix, general, speech: long wrong-result speech lost one of five events at 2-second spacing. Shortened it; five now start, with fuller teaching text in the hint.
- Should fix, general, feedback: unnamed dancers got Right badges in single-dancer calls. Say not called; manual Bow gives no earned-performance praise.
- Should fix, family:dance, camera: a pending flip could overwrite a newly entered mode. Invalidate its token on mode/reset.
- Should fix, general, hover: primary buttons became dark text on dark fill. Light hover fill keeps navy text readable.
- Should fix, general, terminology: soft-shoe releve is a rise onto the balls of the feet, rather than pointe work. Corrected the trait and notes.
- Polish, general, Compare: moved the real hint into the board and replaced duplicate tiny editing buttons with placement labels; source cards stay full-sized.
- Should fix, general, voice context: tab changes cut stale instructions, and returning from Your turn now gives map guidance that fits the retained viewpoint.
- Blocker, family:dance, Rush Hour: the routes were parallel despite the crossing-path clue. Changed endpoints and collinear midpoints to create actual crossings, with distinct arrival times.
- Should fix, general, audit layouts: caption/inset overlap at 760; reset below the short preview/720 setup; hidden Reset under Compare; verdict text crossing tile edges. Reflowed the compact desk, setup and caption, and kept verdicts on the area label.
- Should fix, general, evidence feedback: a fitting subset was called wrong. Explicitly ask for four clues and use a neutral evidence prompt for incomplete/unsupported sets.
- Should fix, general, first tap: tapping the already-selected seats view suppressed all welcome speech. Removed its deferred-speech flag.
- Should fix, general, painted rig: clamped each sprite clip to its own cast column, removing neighbouring fingertips.
- Should fix, general, audit voice: rapid Calls toggling cut its event before completion. Ignore a second tap within one second; later toggles work normally.
- Should fix, general, audit stage taps: the decorative guide intercepted the upstage-center tile. Made the guide transparent to pointer input.
- Should fix, general, replay frame: full-width controls covered dancers on the narrow stage. Expanded the stage and fitted clips between headers and cards; kept all eight cards live. Checked low/high/one-leg extremes, including 375/680/800.
- Should fix, general, voice transitions: Start and first trait placement cut setup/how-to speech. Preserve the current instruction; wait for each movement call before counting. Shortened the acknowledgment and spoken idea prompt; retained the full evidence hint.

#### Findings left

- Should fix, general, standards/spec decision: DA:Re9 evaluation is not fully taught by this prescribed trait comparison. Notes disclose the gap; shared catalog/new activity are outside scope.
- Polish, family:dance: the existing camera transition approximates an orbit. Hand identity, world positions and mirrored areas are retained.

#### Break it

- Eight calls: 8,000 independent combinations, including wings, shared areas and audience-right traps; no mismatches. Optional checks award no cumulative score.
- Ideas: fresh-profile no-watch sweep left both answers empty and Compare closed. Correct title alone and selecting all eight clues fail the evidence check.
- Retry: wrong then remaining ideas leaves the wrong answer/retry flag; no praise or Compare unlock. Correct observed readings reach Compare.
- Board: sweeping all traits into one column, then changing one, gives collective feedback with no gradient. Correct board earns its specific eight-trait recap.
- Room phrase: tapping Bow early gives a neutral bow. Only the timed sequence reaches the closing encouragement; execution is not sensed or graded.

#### Voice walk

Held presses for 120 ms, 2-second tap spacing, Sound on/default tempo: activate speech on the title, reverse, seats, dancer, area, Calls, Check;
Recital, costume/light, watch, clues, Show me, idea; second piece; Compare and eight traits; Your turn and Start.
Heard: welcomeMap, flipHow, call0, checkRight, welcomeRecital, cluesHow, ideaHow, ideaRight twice, compareHow,
welcomeTurn, turn0_0, turn0_1, turn0_2, turn0_3, bow. Calls precede lead-ins; none over counts. All mode/how-to lines finish; final spoken log has no cuts or console exceptions.

| Line | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| placeHow, five selections | how | 1 | 1 |
| checkRight, five checks | event | 5 | 5 |
| checkWrong, five checks | event | 5 | 5 |

All 37 fixed runtime lines exactly match voice/lines.json. Browser narration remains the recording fallback.

#### Facts checked

- Performer left/right, house-right reversal and downstage: [National Park Service, Wolf Trap](https://www.nps.gov/wotr/learn/historyculture/language-of-the-theater.htm).
- Nine named areas: [The Music Center, Stage Geography, pp. 11-13](https://www.musiccenter.org/media/xabhrvnf/theatre-glossary-assessment.pdf).
- Italian/French courts in the 1500s/1600s and later French development: [Paris Opera, Court Ballets](https://www.operadeparis.fr/en/visits/exhibitions/a-certain-air-of-italy-the-paris-opera-from-louis-xiv-to-the-revolution/11-how-it-all-started-court-ballets).
- French terms, releve and port de bras: [Pittsburgh Ballet Theatre, Ballet Vocabulary](https://pbt.org/community/resources-audience-members/ballet-101/ballet-vocabulary/). Arabesque: San Francisco Ballet, Nutcracker Family Guide vocabulary (indexed primary PDF; live URL returned 404).
- African American roots, musical connection and syncopation: [Jacob's Pillow, Jazz Dance, Music, and the Importance of Swing](https://danceinteractive.jacobspillow.org/themes-essays/african-diaspora/jazz-dance-music-and-the-importance-of-swing/).
- Broader jazz movement variety: [Jacob's Pillow, Uncovering Jazz Elements](https://danceinteractive.jacobspillow.org/themes-essays/what-is-dance/uncovering-jazz-elements-in-the-work-of-contemporary-choreographers/). The two studies are original, not complete style definitions.
- Responding and performing claims: [National Core Arts Standards, Dance handbook](https://www.nationalartsstandards.org/customize-handbook?discipline=Dance&display_options=eq_el%2Cprocess_components&grade_level=3rd%2C4th%2C5th&process=Performing%2FPresenting%2FProducing%2CResponding). Re9 gap recorded above.
- Arithmetic: 24 counts at 72/104 = 20.000/13.846 seconds; 28 movement + 16 lead-in counts = 26.4 seconds at 100, 33 at 80, plus calls. Source: spec Content and independent numbers-review.json.
- Straight crossing routes: independent segment intersection/arrival calculations in crossings-review.json; two real crossings with 3.575/0.504 second arrival gaps.
- Contrast, independent WCAG formula: brand/navy 10.32, ink/navy 15.59, muted/navy 8.45, ink/panel 12.87, brand/panel 8.52, gold/navy 12.21 to one.

#### Sensitivity

Review the short theatrical-jazz study against the broader African American tradition, retaining its explicit credit.
Review the people contact sheet and animated bodies for dignified movement/representation. All cast members dance both pieces; no identity determines style.
Three children vary in skin tone, hair and build. Notes support smaller/seated student movement. Fresh cultural signoff is not claimed by this review.

#### Flattest moment left

The history footnotes are quiet reading after the Compare clips. The board's earned arrangement is the payoff; no new topic/game was added.
The flattest teaching moment, an unreadable front-on arabesque, now shows the extended leg; the weakest art, code people, is painted.

#### Graphics

Kept both original theater paintings and the rich floor, curtains, light pools and camera flip. Added two people:true painted sheets, one articulated pose per facing/cast member.
Originals and full prompts are in art/raw and art/prompts.json; all final assets used art.py --rekey. All four finished images and difficult rendered poses were inspected.
Contact sheet: [painted cast](../../_scratch/recital-stage-directions/people-contact-sheet.png). Adapter/source landmarks are documented in handoff.md.
Finished art 561,328 bytes (548 KiB); final bundle 946,702 bytes.
Resize counts advanced 5, 7, 10 at 760/680/1366 while costume, light and camera stayed live; keyboard and real dragging passed.
Saved choices survived fresh tabs, including one dimmed area; Start over stayed cleared after another fresh tab.
The 375 host alone requested a missing favicon; the offline tool generated no external requests.

#### Audit

AUDIT_TIMEOUT: the sole audit reached its 40-minute limit on Chrome 9961/host 8765. No rerun. Saved report: [review-audit/audit.md](../../_scratch/recital-stage-directions/review-audit/audit.md) (430 leads).
Inspected all 64 captured frames across seven direct sizes; the audit could not discover its 375 iframe context. Separate 375 host frames cover the phone fixes.
Saved sections cover Motion off, mid-action resizing, all three mode control walks, ten five-click controls and ten quick-tap controls. Later stress coverage is incomplete.
Confirmed caption/inset overlap, compact/setup overflow, hidden Reset, verdict placement, guide interception, silent seats-first tap and Calls interruption were fixed and re-shot.
Polygon bounding-box overlaps, labels inside their own tiles, painted folds, and stage labels intentionally covered by Compare are false leads, not reasons to strip the art.
Own action speech replaces welcome on dancer/Calls/Clear/reverse first taps, per STANDARDS; no late welcome is added.
Final targeted evidence: post-audit/, compare-final/, compare-extremes-final/, 800-final/, phone-final/, phone-extremes/ and final-verification.json in Scratch. No owned listeners or host file remain.

#### Left open

Spec/catalog Re9 decision and approximate camera orbit remain. Browser speech is intentional: CODEX-BUILD says not to record audio. No shared files or commits.
Unattended decisions followed the detailed Content timing, owner-painted cast and existing engine; preserved the named titles/options but required independent movement evidence.
Tiny perspective areas use full-sized plan alternatives; undersized floor targets are actually noninteractive, while drag placement still works.
Procedure deviation: the initial folder/read/search call had no explicit process-kill timeout. Later shell commands were bounded.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Recital Stage Directions handoff

Cold review in the authorized S:/CurioClass-codex checkout. No commits or shared kit edits.
The original builder report is historical. `codex-review.md` records the current review result.

#### Structure

The kit supplies settings, narration, geometry, joint poses, phrases, clocks and synthesized music.
The tool keeps canonical stage coordinates from the seats and maps the camera independently of the dancer's body.
The two floors crossfade over an 800 ms camera transformation. Motion off cuts to the same endpoint.
The current transformation approximates an orbit; it is not a full three-dimensional camera.

`renderer.frame`, `renderer.rebuild`, `renderer.icon`, `renderer.extra` and `makeFigure` remain the figure boundary.
`makeFigure` delegates skeleton projection to the engine, then `paintFigure` draws the painted skin over the joints.
The original code drawing is hidden. Shadows, badges and hand arrows retain the engine's projected coordinates.
The whole figure can still be replaced at this boundary without changing choreography or interaction.

#### Painted dancers

`art/dancer-cast.webp` and `art/dancer-backs.webp` are self-painted gouache source sheets, generated during review
with the built-in OpenAI image tool. Both are marked `people: true`, `drawn_by: codex` in `art/prompts.json`.
Original PNGs are in `art/raw/`. Only `scripts/art.py --rekey <name>` processed the final WebPs.
The front and back view of one neutral T pose per dancer supply all the articulated moves.
Three cast members have different skin tones, hair, builds and clothing. All perform both pieces.
The fourth image on each sheet duplicates the guide's back view and is unused; it is not an extra character.
Fifteen old proposed pose sets are preserved as `replaced_pose_requirements`, rather than missing active assets.

To swap art: replace `PAINT_SOURCES`, the sheet placement and `castLandmarks` near `paintFigure`.
The clip rectangles divide head, shirt, waist, sleeves, limbs and shoes. Keep source joint landmarks aligned.
Clothing-only filters preserve paint texture while making live costume changes. Skin and hair are never recolored.
Each crop is clamped to its own cast column to exclude neighbouring fingertips.
The head keeps its volume under a nod, and the arabesque faces sideways so its extended back leg is visible.
The inset icons, guide, main troupe and six-figure Both excerpt all use this same painted adapter.

The two original theater paintings remain in place. Their rich curtains, floorboards, light and depth were retained.
People sheet: `_scratch/recital-stage-directions/people-contact-sheet.png`.
Full prompts and provenance are in `art/prompts.json`; OpenAI illustration credit is in the source and draft metadata.

#### Reading and checking

Each piece needs a complete watch, exactly the four supported clue cards and its intended idea before Compare opens.
Clue cards shuffle across positions on a fresh page. Neither column nor card metadata tells the student the owner.
Show me plays actual movement, including for a card that does not fit, and asks the student to judge the evidence.
It does not name which cards are right. Selecting every card fails the reading check.
A wrong idea requires a new complete watch before another guess. The retry flag survives reload.
Changing selected clues clears that piece's accepted idea, so the board cannot inherit a stale reading.

Compare retains all eight source cards and live bin buttons during its two-count excerpts.
Column labels summarize placements; the source cards remain the full-sized editing controls.
Wrong boards get collective feedback without an incremental count that reveals one correct placement at a time.
Each clip uses its source piece's saved production choices. Both shows three dancers from each piece side by side.
The real hint and privacy disclosure move into the board and return to the panel on exit or mode change.
Reset is hidden while that overlay is open; Back restores the original accessible control.
Compare uses the seats view and full floor width, with four explicit grid rows during playback.
Short landscape displays concise versions of the same eight traits, retaining full names as accessible labels.
The six painted dancers remain visible during the high/middle/low Both excerpt.
Replay projection fits between the bin headers and source cards at each viewport, and scales single-piece clips
to that space. The backdrop follows the floor edge. Header controls remain outside the overlay.

A rapid second Calls tap within one second is ignored so the first call can finish; later taps toggle normally.
The decorative guide does not intercept stage taps.
Calls are optional practice, without a cumulative score. The first three check only the named dancer;
the feedback explicitly identifies the other dancers as not called. Calls four through eight check whole formations.
Manual Bow is a neutral action; only completing the timed counts earns the closing encouragement.
The tool does not observe or grade a student's physical execution.

Rush Hour's first routes cross in canonical floor coordinates. Midpoints stay on each straight route.
The two intersections have staggered arrivals; see Scratch crossings-review.json for independent geometry.
The first ballet block resets facing, so repeated watches do not inherit an arabesque's sideways view.

#### Timing, voice and saving

Every interrupt invalidates the playback token. Mode changes also cancel an unfinished camera flip.
Your turn awaits each spoken call before its four-count lead-in. Sound off preserves the estimated reading time.
Starting from setup lets its current welcome finish before the first call. Compare's first placement also preserves
its current how-to line. Mode changes, Stop, Read and a mid-phrase restart still interrupt obsolete speech.
Read stops a room phrase before speaking. Stop cancels pending calls, music and the count clock.
Slower restarts at 80 beats a minute. The regular phrase tempo is 100.
The full held-click voice walk is `_scratch/recital-stage-directions/voice-walk.json`.
`voice/lines.json` has the same fixed line set as `__tool.allLines()`; browser speech remains the recording fallback.

Saved settings include costumes, lights, lit areas, clues, answers, watched/retry flags and the Compare board.
The on-screen privacy line states that choices remain on this device. Start over removes this storage item.

#### Responsive behavior

The phone uses one compact header row, an inset plan, and a production desk with all short choice sets visible.
The plan remains visible during clue and idea reading. Main phone actions remain fixed at the bottom.
Undersized perspective cells are noninteractive pictures; the inset provides full-sized named touch and keyboard
targets. Larger floor cells accept taps, and dancers can still be dragged onto every area of the floor. No tiny floor tile enters the Tab sequence.
Compact Compare uses the full viewport width. Long history footnotes may scroll inside columns.
The full-sized source trait controls stay visible; the duplicated placement labels are not extra small buttons.

#### Sources and standards decisions

The Content timing wins over the earlier screen summary: Autumn Leaves is 20 seconds; Rush Hour is 13.846 seconds.
Room phrases have 28 movement counts and 16 lead-in counts: 26.4 seconds at 100, 33 seconds at 80, plus calls.
The stage geography matches National Park Service and Music Center teaching material.
Ballet court history matches Paris Opera; terms match San Francisco Ballet's Nutcracker Family Guide and Pittsburgh Ballet Theatre's Ballet Vocabulary.
Jazz origins and rhythmic variety match Jacob's Pillow essays. These two original studies do not define whole styles.

The spec's DA:Re9 claim is broader than this comparison activity. The NCAS handbook chiefly puts identifying style
traits under DA:Re7; DA:Re9 asks for evaluation with criteria and reasons. Notes no longer claim full Re9 coverage.
Changing the shared catalog or adding an evaluation activity exceeds this review's write and topic scope.
The specified title and long main-idea choices remain; movement evidence is independently required to pass.

#### Sensitivity

A fresh cultural reviewer should check the short jazz history and the original theatrical-jazz study against the
broader African American vernacular tradition. The history retains African American credit.
Inspect the people contact sheet and animated cast for representation and readable, dignified movement.
No style is assigned by skin tone, hair, body or gender. Smaller and seated student movements are supported in notes.

#### Engine changes wanted

- `kit/dance.js`, `floor().resize`: make x0/x1 describe actual front-edge pixels for the stage's d0=140 projection.
- `kit/dance.js`, floor projection/inverse and figure projection: add an orbit/mirror interface with a correct inverse,
  preserving hand identity and avoiding negative-width decoration. The tool currently uses a local adapter.

#### Review evidence

Scratch holds cold play, no-watch guessing before/after, evidence and board sweeps, exhaustive 8,000-case call checks,
voice walks/repeats, keyboard and drag checks, phone and compact frames, arithmetic and the one final review audit.
See `codex-review.md` for the audit's actual disposition and any remaining limitations.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
