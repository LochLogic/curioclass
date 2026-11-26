# Feeling Scarf Dance: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: feeling-scarf-dance

#### Built

Four modes: Build, Watch, Your turn and Share. Five feeling tracks and patterned scarves, five start/end shapes, six middle moves, 4+8+4 engine phrases, live edits, Slow, Mirror, quiet Freeze and audience observations. Uses the kit starter, Curio.voice and Dance engine. Build only, no git commit or polish round. All repository writes are within the tool folder and its Scratch folder.

#### Numbers check

Scratch compute_numbers.py recomputed all spec numbers. Sixteen counts / with four-count introduction, seconds: Happy 8.571 / 10.714; Sad 14.545 / 18.182; Calm 13.333 / 16.667; Mad 9.600 / 12.000; Surprised 10.000 / 12.500. Normal runs match the rounded spec values.

Contrast ratios: white/brand 7.155, brand/paper 6.713, ink/paper 15.873, muted/paper 6.428. All match the spec rounding. Twenty-four points have 23 segments, so spacing is 1.1 / 23 = 0.047826 body heights; the spec's 0.046 value assumes 24 links. The implementation preserves the required 24 points and total length. All named shape/gait references resolve in the actual engine.

#### Feel check

Best moment: Zap whips the patterned silk across the sky, then Your turn removes the figure so the same scarf is the class's movement cue. The full Happy performance ends in a high held shape with a quiet Freeze.

Two flat moments repaired during this Build: the cloth originally fell below the stage, so it now settles on the painted grass; compact cards originally had tiny figures in large empty boxes, so their figure area grew and their height is capped. Build's middle/end prompts now name the part card to tap. The temporary kit figure remains visibly simpler than the intended painted dancer.

Played all four modes through Build, Watch, Your turn, audience chips and Swap. Five real-time Watch runs and a full Your turn run completed. Compared the Zap frame against Snowy Mail Route in Scratch feel-comparison.png; opened Beat Lab as the second quality bar. The landscape, silk sheen, patterns and physical response carry the finish; the owner's painted figure is the remaining art step. No ten-minute super-tool claim is made.

#### Done when

1. PASS: Watch centers the figure and scarf; Your turn hides the figure and leaves a large scarf with readable part word. Inspected 1366x768 and 680x425 frames.
2. PASS: all 750 feeling/start/move/end combinations sampled at all 16 counts, no invalid pose values; five real-time feeling runs ended at count 16 without console errors. Combination sampling is not 750 real-time runs.
3. PASS: six focused motion frames show Float's arc, Swirl's turn, Zap's snap, Melt's low drape, Shiver's flutter and Leap's trailing cloth.
4. PASS: held-click live edits changed Middle to Zap, feeling to Sad and Slow to 46.2 bpm on the next count. The phrase proxy blends edits over 180 ms. Mirror flips immediately; Stop's scarf remained byte-for-byte unchanged after 350 ms.
5. PASS: real-time logs contain only end narration after the music. Read stops an active run before speaking. Sound off/on during a run did not queue a welcome.
6. PASS: both modes use the same phrase and scarf simulation. Your turn hides the figure and retains a 12 percent hand marker. End showed Freeze, a still scarf and no speech for the sampled quiet hold; full-run log started the freeze reminder after three quiet seconds.
7. PASS: chips check/uncheck, five repeated Start chip taps produced five event lines, and Swap clears observations. Other chip lines are also declared event keys.
8. PASS: at two-second held-click pace, the Middle how-to started once across five taps, then was silent as heard. Stale queued copies were dropped.
9. PASS: 28 full size/mode frames plus four 375-pixel iframe frames. Measurements found zero controls below 60 px, zero horizontal overflow and zero below-viewport buttons. Play and Go remain visible. All controls combine an icon/figure/trace with a word.
10. PASS with shared-setting exception: Motion off keeps count timing and a straight scarf (measured horizontal spread zero); no infinite CSS movement. Static bundle scan found no fetch, remote resource, unresolved art or network library. Dance and observations are memory-only; the required shared kit remembers Motion preference.

#### Wave lessons

- Hint and voice: PASS. Direct synchronous hint updates; Read uses the current hint; incomplete Watch/Your turn names Build; how-to keys use Curio.voice heard tracking. Music never waits behind a stale line.
- Focus and layout: PASS. Stable outer controls, no focus on load, preventScroll on deliberate focus; keyboard-only Build-to-Watch and Play/Stop ended with focus on Play. Hint space is reserved.
- Sizes: PASS. Every standing size, every mode and a 375-pixel hosted iframe were inspected; all control targets measured at least 60 px.
- No giveaways: PASS, expressive creation has no hidden answer, ranking, score or correct-feeling association.
- Honest numbers: PASS. Counts and tempos use the engine clock; Slow is 70 percent. Number/contrast recomputation is in Scratch.
- Standards: PASS for the teacher-led spec. Building three parts practices DA:Cr2; Your turn performance and audience observation support DA:Pr6; teacher notes invite a lived-experience feeling connection for DA:Cn10.
- Motion off: PASS. One pose per count, straight scarf, same real-time clock; idle drawing and CSS breeze stop.
- Short choices visible: PASS. Only the selected part's complete choice set is shown; no choice scroll panels. The choice menu shows all five or six options.
- Resize mid-animation: PASS. The one full audit reports no exception and no control left disabled after resizing every explicit reached state and changed walked control.
- Deferred welcome: PASS. Multiple modes use the standard welcome mechanism; first action lines supersede stale welcomes, with no welcomeAfter.
- Unknown as unknown: PASS. Incomplete part cards say Choose; Play/Go are disabled and Build is named in the hint. Incomplete performance says Build first and Choose a feeling.
- One look, one meaning: PASS. Pattern and face/word accompany every scarf color; selected cards and running parts have distinct context.
- Badge truth: PASS. Part names and feeling labels update from current state; no score or success badge.
- Reversible hints: PASS. Changes between modes, dialogs, stop and missing choices update Read's current hint.
- No copying-word answer: PASS, no diagnostic quiz or hidden answer exists.

#### Audit leads

The one full audit completed within its 40-minute limit and produced 27 leads. All eight base sizes are clean; Motion off is clean; resize stress reports no exceptions or stuck disabled controls. All 47 audit frames were reviewed in twelve contact sheets. The audit was not rerun after the focused repairs below.

- Built-dance stale how-to: intentional. Feeling idea fills the start shape, so the previously queued "Tap a start shape" instruction is obsolete and is dropped. No line is marked heard by hand. Feeling idea as the very first tap now avoids queuing that obsolete instruction at all.
- Live-editor #hint keep region: native modal backdrop intentionally makes the background footer inert. It stays visually legible; the current menu has a clear heading, all options and an in-menu Read control. The added Read control stops music and reads the current choice hint. Focused checks cover 680x425, 1366x768 and a 375-pixel iframe.
- Welcome skips on m-watch and m-turn: intentional while the dance is incomplete. Their Play/Go welcomes would name disabled controls; the available Build control is voiced instead.
- Welcome skips on feelings 0 to 4, Start/Middle/End, shape options 0 to 4 and Feeling idea: intentional first-action behavior. Each tap has its own relevant event or how-to and suppresses the obsolete welcome. End's first instruction was repaired so it always speaks an enabled action.
- The Middle card shifts four option buttons when it replaces five shapes with six moves. That is the intended change of choice set; the part strip, hint and action bar remain stable and nothing rebuilds under the clicked card.
- Four repeated-name leads (Happy, Sad, Calm, Mad): repaired with unique event queue keys. The follow-up tests check all five feeling names, five held taps each at two-second pace, without replacing an earlier same-name event.
- Four quick-mode cuts (Build, Watch, Your turn, Share): repaired. Tapping the current mode no longer hushes its own instruction or restarts a run. Focused quick-tap checks exercise all four.
- Follow-up results: all 25 feeling events spoke, zero event drops; all four quick-mode logs had zero cuts. End-first spoke its enabled instruction and Feeling idea first spoke only its relevant event. Narrow-stage checks sampled 330 frames across six moves with zero scarf-center points outside the stage, with an added inset for the ribbon width. This is a sampled bound check, not exhaustive trajectory proof.
- No runtime, focus-loss or control-jump failure was reported. Sound's cut welcome is the intended Sound-off hush, and Read is allowed to skip the welcome.
- Audit coverage limitation: automatic mode discovery only searches header, whereas this tool has a separate nav. Explicit reached-state checks cover all four modes; the automatic default walk does not exhaustively walk the other three. Manual held-click runs cover their main interactions.

#### Frames looked at

Scratch barframes: both quality bars. early-frames: five initial size/layout frames. focused-frames: ten move, editor, calm and audience frames. run-frames: five complete feeling endings. special-frames: seven live-edit, Freeze, Mirror, grayscale, voice, keyboard and combination frames. extra-frames: four keyboard, full Your turn, repeated how-to and Read frames. matrix-frames: all 28 mode/size frames, reviewed in seven contact sheets. phone-frames: four modes in a true 375x812 iframe. final-focused-frames: six compact, incomplete, Sound and Motion-off frames. Audit: 47 frames in twelve contact sheets. Post-audit: menu Read at three sizes, narrow Swirl, and targeted voice repairs; 11 repair frames, three final narrow-stage frames, three menu/narrow frames and one menu frame in a true 375-pixel iframe were inspected.

#### Art made

Two images made with the built-in image tool, no people: hilltop (1500x844) and silk (384x384), selected without a redraw. Full prompts and house style are in art/prompts.json, originals in art/raw, processed with art.py --rekey only. Final WebP art is 92,626 bytes (90.5 KiB). Final offline bundle: 399,221 bytes (389.9 KiB), below 2 MB.

#### Art still to paint

Eleven people:true manifest entries cover five held shapes and six multi-phase moves. The next painter needs consistent facings, full bodies, pose phases and right-hand registration. createDancerRenderer is the swap boundary. Current kit figure is temporary by owner decision. No people, faces or body parts were generated.

#### Engine changes wanted

See handoff.md for the exact dance.md table row, an optional full-height square backdrop without the platform, and optional in-memory-only kit Motion preference. No kit or shared doc was edited.

#### Left open

- Painted dancer assets are intentionally deferred to the next painter.
- Forty-four narration lines use browser speech; the requested soft-breath / Enceladus bank is declared, with no recordings made in Build.
- Muted browser checks verify scheduling and state, not headphone timbre or classroom loudness. Calm's soft chime uses the engine's high-register piano.
- The tool-local grass contact constraint and reduced-motion camera adjustment are documented specification interpretations.
- The full audit predates the focused narration, menu Read and narrow-scarf repairs. Those received targeted rechecks; no full post-repair audit or cold review was run.

Final checks: required files present; stage built; tool-owned Chrome and host ports closed; host.html absent. No commit, deployment, shared-file edit or polish round was performed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: feeling-scarf-dance

#### Played

Cold as a K-2 child at home, then as a projecting teacher: Build, Watch, Your turn, Share and Swap, before builder notes/source. The flowing cloth is worth copying with a real hand or scarf. Preserved its hilltop, music, patterns and simulation.
#### Findings fixed

- Should fix, general, src.html/startRun: Play and Go cut off mode instructions at two-second held-tap pace. A cancellable pending start finishes the fitting introduction before music; Stop, Read, mode changes and opening an editor cancel stale work.
- Should fix, family:dance, choosePart/setMode: an idle edit froze at the first instant of its transition, showing the old pose beneath new labels. Idle edits and mode entry now show the selected start pose; running edits retain their 180 ms transition.
- Should fix, general, Share: removing a chip still praised that observation, and checked observations survived a changed dance. Chips now record observations consistently; Swap or changed feeling/parts clears them. Unique event keys preserve repeat speech; revision checks discard old observation, reflection and Freeze lines.
- Should fix, general, Build: choosing all parts before the feeling left the next step unspoken. Guidance now follows the missing choice in any order, then announces Watch it when the feeling completes the dance. Idle previews label their actual part and clear old count dots.
- Should fix, general, Build: the personal-experience connection lived only in teacher notes. The feeling hint/how-to now invites a remembered experience without asking for disclosure.
- Owner art decision, family:dance: replaced the code figure and its small icons with three painted articulated children, one pose plus reverse per child. Engine joints, clock and right-hand scarf attachment remain authoritative; Again rotates the demonstrator independently of feelings.
- Should fix, family:dance, art integration: fixed atlas leakage with explicit SVG clip paths, preserved head proportions, gave the torso a side-profile width and expanded icon bounds to show whole painted heads. Checked five shapes, six moves, three children and reverse/quarter/side views; repaired cards re-shot at 680, 1366 and 1920 widths.
- Should fix, general, voice: Idea, Watch reflection, Freeze, Share and Swap now name the next control or action; manifest and on-screen hints agree with their purpose.
- Polish, general, Share: replaced the generic visual finish with the actual chosen shapes and movement trace inside its existing four observation chips.
#### Findings left

- Should fix, general, voice: 44 authored lines have browser speech but no Enceladus recordings. CODEX-BUILD.md Ground rules says "Do not download anything or record audio", so this pass did not record them. Scheduling is verified; bank timbre/classroom loudness is not.
- Polish, family:dance: the exact side-on instant of Swirl remains a narrow articulated illustration. The quarter and reverse views read more naturally; a future side-profile painting could improve that instant.
#### Break it

- Empty dance: pressed Watch, Play, Again, Your turn and Go. Play/Again/Go stayed disabled, no clock started, and the hint named Build. Choosing arbitrary valid parts is expressive creation, not a hidden-answer test.
- Counts/run lifecycle: rapid Play/Again/Again/Again/Stop left no running or pending clock, held the cloth unchanged, and emitted no false completion. Counts measure time, never the child's movement or skill. Live edits, Slow and Mirror were also exercised during an actual run.
- Audience observations: tried all four chips before any on-screen performance and repeatedly tapped one. They only annotate observations, with no score, best, win or pass. Five taps spoke five events, stayed selected, and Swap cleared all four.
- Stale success: selected all four observations, changed feeling and middle move, and returned to Share. Before repair all four stayed checked; afterward all four were clear. Parts-first construction now speaks the missing feeling and its eventual Watch it completion.
- Reflection: Watch's question asks what the scarf expressed; it presumes no mistake and has no answer gate. No guessing, elimination, percent or slider shortcut exists.
- 750 combinations, 12,000 sampled count poses: zero nonfinite values. This is sampled pose validation, not 750 real-time performances. Evidence: combinations-result.json, walk/results.json and final-focused frames in Scratch.
#### Voice walk

Real held clicks, default Sound on, two-second gaps between Build and mode actions: Happy, Wide star, Middle, Leap, End, Tall tower, Watch it, Play; wait for the run; Your turn, Go; wait through Freeze; Share and four chips with time for their speech. Read __tool.vlog after the walk; repeated after the audit repairs.
Heard in action order: Happy; middle-selection instruction; end-choice instruction as the End row opened; Watch introduction; Watch reflection; Your turn introduction; Freeze reminder after its quiet hold; Share introduction; clear start; middle move; clear end; felt it.
Build's welcome was correctly skipped by the first feeling event. Superseded Build prompts dropped as their action passed. Watch/Your turn introductions each finished without cuts; older Build/result lines cut on explicit mode changes. No narration started over music.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Watch introduction | how/welcome | 1 | 1 |
| Your turn introduction | how/welcome | 1 | 1 |
| Share introduction | welcome | 1 | 1 |
| Repeated Middle-row how-to | how | 1 in 5 taps | 1 |
| Repeated clear-start observation | event | 5 in 5 taps | 5 |

Read with Sound off and a subsequent mode change used the current hint. Source allLines and voice/lines.json match exactly, 44 unique lines. Chrome was muted; no claim of listening to recorded takes.
#### Facts checked

- Beginning/middle/end, movement choices expressing a feeling: [National Core Arts Standards Dance, DA:Cr2 K-2](https://www.nationalartsstandards.org/customize-handbook?discipline=Dance&grade_level=PK-2%2CPK%2CK%2C1st%2C2nd%2C3+-+5%2C3rd%2C4th%2C5th&process=Creating%2CPerforming%2FPresenting%2FProducing%2CResponding%2CConnecting). Children compose the three parts.
- Perform for an audience and link a dance to lived experience: the same NCAS handbook, DA:Pr6 and DA:Cn10. Your turn performs; Share supports observation; Build now makes the life connection on screen. A solo child can use a toy or imagined audience as notes suggest.
- Movement energy, space, time and individual variation: [NDEO, organization of its Early Childhood Standards](https://www.ndeo.org/Learn/Dance-Education-Standards/Early-Childhood-Dance-Standards/How-the-Standards-are-Organized). The six move names are accessible tool labels, not a claim of a complete Laban taxonomy.
- Scarves as creative/sensory props and room for safe movement: [NDEO Opportunity-to-Learn Standards](https://www.ndeo.org/Portals/NDEO/Standards%20Documents/NDEO_Opportunity_to_Learn_Standards_2-22-18%281%29.pdf). Notes retain own-space, seated/small-motion and empty-hand options.
- Gilbert, Anne Green, second edition, 2015: [Human Kinetics publisher catalog](https://www.humankinetics.com/AcuCustom/Sitename/DAM/158/Human_Kinetics_2017_Product_Guide.pdf). Full book pages were unavailable; its specific wording was not independently verified or quoted.
- Counts and tempo, recomputed in Scratch/recompute_numbers.py: 16 = 4+8+4; with four-count introduction, Happy 10.714 s, Sad 18.182 s, Calm 16.667 s, Mad 12 s, Surprised 12.5 s. Slow = 70%, observed Sad 46.2 bpm; slow Sad exceeds 20 s.
- Scarf geometry, spec plus computation: 24 points, 23 segments, each 1.1/23 = 0.047826 engine body units. The spec's 0.046 assumes 24 links; total length stays 1.1. Contrast recomputation: white/brand 7.155, brand/paper 6.713, ink/paper 15.873, muted/paper 6.428; these match spec rounding.
- Music tracks/patterns are original authored choices, checked in trackFor and Dance.music: Happy's claps on 2/4, Calm's triple meter, Mad's stamps on 1/3, Surprised's fourth-count stop. Colors, tempos and suggested moves are not universal facts about feelings.
#### Sensitivity

No named cultural tradition, religion or hard history. Bodies are represented: a fresh reviewer should inspect skin/body variation, the right lower-leg prosthesis through turns, articulated low poses and access through seated/small-motion options. People are not assigned to feelings. Keep the invitation to personal meaning optional; a face or movement does not diagnose a child's feelings.
#### Flattest moment left

The first Your turn setup waits for its spoken instruction to finish. That time lets the class find its start shape, but it is still the least active screen moment. The final audience discussion is strongest with a partner; personalized pose chips now give it something specific to discuss.
#### Graphics

Preserved hilltop and silk. Generated one dancers-rig atlas with the built-in imagegen tool; people:true and drawn_by:codex. Full prompt, cast and registration are in art/prompts.json; source PNG is art/raw/dancers-rig.png; processed WebP is art/dancers-rig.webp. Three children, six front/reverse tiles replace eleven proposed separate pose assets; prior plan preserved in Scratch. Engine motion and scarf remain live code.
Inspected the art in actual scenes, all moves/shapes, grayscale, Motion off, phone and all eight STANDARDS sizes. Beat Lab and Snowy Mail Route were opened without modifying their folders; final comparison is in Scratch. Bundle: 702,164 bytes, about 686 KiB; all art tokens resolve. No art still to paint.
#### Audit

One audit completed within its 40-minute limit on Chrome 9941, host 8745. Its 44 frames were opened. It reported 20 mechanical leads: 16 suppressed first-tap welcomes (correct replacement by an action's line or incomplete-dance guidance under STANDARDS); one obsolete Start prompt after Feeling idea (correct stale drop); one hint under the native modal backdrop (legible, intentionally inert; modal Read speaks it); two phone-host context/hint failures (harness coverage failure).
Seven desktop sizes, Motion off, resize stress, held-control/keyboard checks and sampled repeated/quick taps were mechanically clean otherwise. Automatic mode discovery saw zero kit-header modes; eight explicit audit states and manual four-mode runs supplied coverage. The actual 375x812 iframe was separately driven through all four modes plus its editor, then rechecked after repairs, with zero errors.
Frame inspection confirmed clipped painted icon heads; fixed and re-shot. Audit voice inspection led to clearer next-control lines, then the stale-observation and parts-first repairs above. Only those paths, their affected frames, rapid run cancellation and the main voice walk were repeated afterward, with zero errors. No second full audit. Evidence: review-audit/audit.md, audit-repair/, walk/results.json, phone/ and verification-summary.json in Scratch.
#### Left open

- Recorded voice and the narrow side-profile polish above. Fresh people/sensitivity review remains part of the normal release workflow.
- Full Gilbert page-level attribution was unavailable; official NCAS/NDEO sources independently support the actual teaching claims.
- Shared dance.md table/platform/Motion-persistence suggestions remain in handoff.md because this run cannot edit shared files.
- No questions were asked in this unattended run. Kept the spec's three silent Freeze seconds before its spoken reminder; used an articulated atlas to minimize poses; interpreted observation chips as teacher annotations.
- No git commits. Writes confined to tools/feeling-scarf-dance/ and _scratch/feeling-scarf-dance/.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Feeling Scarf Dance handoff

Cold review November 5, 2026, in S:/CurioClass-codex. No commit, upload or shared-file edit.

#### Structure

src.html uses kit:curio, Curio.voice and kit:dance for four modes, original music, a 4+8+4 phrase and a tool-owned textured scarf. The engine owns joint positions, projection, root motion, clock and music. The 24-point scarf stays attached to world('rHa'). Nothing about the dance or audience feedback is persisted. The kit remembers Motion preference.

#### Painted dancers

The owner's painted-people direction overrides the old code-figure Art section of spec.md. The engine model remains hidden. createDancerRenderer and paintedFigure are the replacement boundary: a single generated atlas has three children, each with one articulated pose plus a reverse view for turns. CAST holds registration coordinates. Every crop maps to engine screen joints; the original ribbon remains independent. Again rotates the demonstrator without associating any body or skin tone with a feeling. Shape buttons and audience chips use the same painted renderer.

art/prompts.json retains the hilltop and silk and replaces the unpainted eleven-pose proposal with the smaller articulated atlas. All people artwork is marked people true and drawn_by codex. The previous pose proposal is preserved in Scratch/original-pose-plan.json. The raw atlas is art/raw/dancers-rig.png; the processed asset is art/dancers-rig.webp. Built-in imagegen was used with the full manifest prompt and house style. Only art.py --rekey processed the chosen PNG; no paid art CLI or external image download was used.

The atlas contains brown skin and straight hair, deep brown skin and a fuller build with curls, and light freckled skin and red hair with a right lower-leg prosthesis. Front and reverse views preserve anatomical sides. The atlas and final contact sheet in Scratch need the normal owner/fresh sensitivity review before release. This review does not claim to be that independent review.

#### Review repairs

- Further audit-path checks found stale audience ticks surviving changes to the dance. Changed feelings, parts and suggestions now clear those observations and invalidate old reflection/Freeze lines. Same-choice taps preserve observations. Idle edits label the part actually being previewed.
- Building parts before choosing a feeling now voices the missing feeling and then Watch it when the feeling completes the dance. Hints and how-to lines both follow the actual missing choices, including out-of-order construction.

- At a two-second tap pace Play and Go cut off their mode introductions. A pending start now keeps a fitting introduction intact, then starts the clock. Repeated Play/Go cancels a pending start. Stop, Read and mode changes invalidate the pending token. Opening a menu during preparation cancels it. No pending callback can launch an obsolete dance.
- Idle part edits previously displayed the first instant of a blend forever. Idle edits and mode entry now set their selected pose immediately; live edits retain their 180 ms transition.
- Audience chips record an observation, including on repeated taps; Swap clears them. Each event has a unique queue key and an observation-version validity check. No score, best score or automatic pass exists.
- Audience chips now echo the class's chosen shapes and movement trace. This lifts the generic final checklist without adding a mode or assessment.
- Choosing a feeling now invites a remembered experience on the screen and in its how-to line. No personal disclosure is required.

#### Timing and specification interpretations

- One clock, play and music object; Stop holds the pose and scarf. Live changes keep count position; feeling and Slow update tempo on the next count. Mirror flips actor and ribbon layers together in Your turn.
- Sixteen counts plus four count-in clicks match the recomputed normal durations. Slow is 70 percent, so the slow Sad run can exceed twenty seconds; the spec's under-twenty statement applies to normal tempo.
- Twenty-four points have twenty-three segments. Each is 1.1/23 body heights, preserving the required total scarf length. The spec's 0.046 figure instead assumes twenty-four links.
- A grass contact constraint and edge inset keep the cloth in the painted view. Motion off uses one pose per count, a straight cloth and unchanged timing. Its shared layer translation keeps a low pose's long cloth visible.
- Your turn uses the same phrase and scarf renderer as Watch, with a four-count introduction, hidden painted dancer and faint hand marker. Freeze appears at the end and holds three silent seconds; its spoken reminder follows the quiet hold. This preserves the spec's quiet interval. The eventual reviewer should judge whether the spoken cue should precede that interval instead.
- The Calm track uses a high piano register for chimes because the engine has no chime instrument. Music and feeling suggestions are authored expressive options, never universal emotion rules.

#### Voice

The audit-frame check found painted icon heads clipped by the code figure's old viewBox; icon bounds now include their full painted head. The final targeted frames cover filled Build cards and their small counterparts. The audit voice check also prompted clearer next-control wording for Feeling idea, Watch's reflection, Share, Swap and Freeze; voice/lines.json matches those changes. These get focused rechecks after the single audit, not a second full audit.

Curio.voice chooses how-to lines by heard state and drops stale lines. Hints update synchronously. The mode welcomes, event lines and every authored line are in voice/lines.json and allLines(). Read stops a run or pending start, then reads the current hint, including with Sound off. No narration is scheduled over music.

The 44 lines still use browser fallback. soft-breath / Enceladus is declared, but no recordings exist. CODEX-BUILD explicitly says not to record audio, so the cold review did not make them. Scheduling tests use muted Chrome with real timing; they do not verify Enceladus timbre or classroom loudness.

#### Sensitivity

No named cultural dance, religion or historical tradition is represented. A fresh reviewer should inspect the people set for natural body representation, prosthetic-side continuity during turns, respectful articulated poses and the availability of seated or smaller versions. The suggested feeling-to-movement associations are optional; a child may use any shape or movement for any feeling. Faces do not diagnose feelings. Invite a life connection without requiring a disclosure.

#### Named sources

- National Core Arts Standards Dance K-2, DA:Cr2, DA:Pr6 and DA:Cn10: https://www.nationalartsstandards.org/customize-handbook?discipline=Dance&grade_level=PK-2%2CPK%2CK%2C1st%2C2nd
- NDEO, How the Early Childhood Standards are Organized, movement analysis and individual developmental variation: https://www.ndeo.org/Learn/Dance-Education-Standards/Early-Childhood-Dance-Standards/How-the-Standards-are-Organized
- NDEO, Opportunity-to-Learn Standards for Dance, safe props and scarves as creative/sensory materials: https://www.ndeo.org/Portals/NDEO/Standards%20Documents/NDEO_Opportunity_to_Learn_Standards_2-22-18%281%29.pdf
- Gilbert's author, title, second edition and 2015 date are confirmed in Human Kinetics' 2017 publisher catalog: https://www.humankinetics.com/AcuCustom/Sitename/DAM/158/Human_Kinetics_2017_Product_Guide.pdf . The full book was not available for page-level verification; no quotes or unique book-specific claims were added.

#### Engine changes wanted

- docs/families/dance.md, What each tool brings: add feeling-scarf-dance, K-2, square floor, poses/level/dyn, leap, phrase, clock, play, music, counts, icon; class-created 4+8+4 feeling dances, a 24-point textured hand scarf, scarf-only performance and audience observations. The write boundary forbids editing that shared file here.
- kit/dance.js, floor: consider a full-height square backdrop without its platform. This tool hides .dz-floor and sets backdrop height after resize, keeping the engine geometry.
- kit/curio.js, init: an optional memory-only Motion setting would reconcile literal no-storage specs with shared Motion preference. Standing STANDARDS takes priority here.

#### Evidence

All review evidence is in _scratch/feeling-scarf-dance/: cold/ and cold-whole-result.json preserve the play before reading builder notes; numbers.json and facts-sources.json record recomputation and named sources; walk/results.json contains held-input voice and cheap-path checks; moves-shapes/, matrix-*/, special/, phone/ and review-audit/ contain the inspected frames. codex-review.md is the final one-pass review record.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
