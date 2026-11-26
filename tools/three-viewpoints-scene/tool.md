# Three Viewpoints Scene: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: three-viewpoints-scene
#### Built
Built 2026-11-02 in S:/CurioClass-codex. Build only: no commits, branch changes or polish round.

Offline Devise, Tighten and Perform modes; all 40 line options; four partner offers; six beats; live tension/timing; four director checks; live-role cues; local saving and confirmed Reset. Uses the kit frame, Curio.voice, motion and tones. No family engine is specified.

Final bundle: 361,242 bytes (352.8 KiB), below 2 MB. No active remote references. host.html was deleted. All Chrome and host processes started for this build were closed. Source lines are at most 161 characters. No em dashes in the tool's text files.

#### Numbers check
PASS. Independently parsed and recomputed the full catalog in Scratch before implementation. Forty options, 39 voiced options, silent offer 2 s, shortest 1.2 s, longest 6.0 s. No differences from the spec.

Passing scene tensions: 1, 2, 3, 3, 2, 0. Beat times with a 1.5 s turn pause: 10.1, 10.1, 10.9, 10.5, 13.1, 3.7 s. Total 58.4 s. Crowded beat example: 20.0 s of dialogue, 20.5 s including its default pause. A 30.0 s boundary also passed after adding a small floating-point tolerance.

WCAG ratios recomputed: ink/paper 14.407, ink/white 16.108, muted/paper 5.692, muted/white 6.364, brand/paper 4.945, white/brand 5.529. Selected-role hover now stays white on dark teal.

Evidence: numbers.json, functional.json (24 assertions, all passed), student-built.json, followups.json, phone-flow.json in Scratch.

#### Feel check
Best moment: the turn gets a breath, all four checks become green, then the live cue becomes a large teal script card and the appropriate prop lights up. The student built the 58.4 s example through held clicks, rather than only loading a fixture.

Flattest moment 1: the early preview hid later beats, making scene building feel like searching through a form. Changed it to two rows of three, with 44 px plus controls and a curve that draws at the actual pixel size. Tighten now exposes a full first card in all six beats at 680x425.

Flattest moment 2: Ms. Dale's first painting added unrelated desk accessories and weakened the prop-to-role connection. Rejected it and redrew the single folding chair, clipboard and lanyard. The large cue, prop light and immediate edit tones make role changes visible.

A full twelve-cue student-path simulation completed in 48.2 s against the 58.4 s plan, with all three roles live and realistic delivery delays. This was a scripted reading/interaction check, not a classroom or by-ear trial. A separate phone run checked every live wait and completion, using rapid Done taps for state coverage.

Both bar tools were bundled into Scratch and opened before implementation. Compared the live-cue frame beside Beat Lab in feel-comparison.png. The painted stage and script desk hold their own visually while leaving the dialogue readable.

![Tool beside Beat Lab](S:/CurioClass-codex/_scratch/three-viewpoints-scene/feel-comparison.png)

#### Done when
1. PASS. Devise board, Tighten curve and Perform cue are the central focus at 1366x768 and 680x425. Six beat headings, curve and Play remain visible. Dense card lists use inner scrolling.
2. PASS. The exact example produces four green checks and 58.4 s. The no-turn variant and a clash after the turn produce the appropriate amber message. See functional.json and student-built-green.png.
3. PASS. Real placements triggered offers at 3, 6, 9 and 12. Accept unlocks and places; pass stores; Offers reopens. Duplicate and full-beat guards passed. Playback hides offers until stopped.
4. PASS. Placement, Cut and pause handlers redraw synchronously. Tested the crowded beat, 0 and 3 s limits, reordered cards and pacing boundary.
5. PASS. A held card tap jumped to 5-Dale-a immediately; Stop cleared playback and queue. A pause change kept playback running. Token cancellation prevents stale continuations, and the jumped card becomes selected for subsequent edits.
6. PASS. All three live waits at each cue; Space advances. Mixed-role testing logged Ortiz and Dale as spoken while Maya waited. Phone real-input flow built all six beats, waited at each cue and reached the timing recap. The live cue was 32.8 px at 1366x768. Actual speech quality depends on available browser voices.
7. PASS for queue behavior. No narrator entries during character/live playback in checked logs. Welcomes/how lines use the kit's heard state; event IDs are explicit. Five-repeat audit checks were clean. Same-mode rapid taps no longer hush the welcome. Bank timbres are not verified because recordings are prohibited in Build.
8. PASS. Reload restored the board, pauses and a passing scene. Reset cancellation preserved work; confirmed Reset cleared board, pauses, offer answers and stored work.

#### Wave lessons
- Hint and voice: PASS. Hints update immediately and name the next control. Read uses the hint. Empty Perform now directs the student back to Devise and cannot queue an unavailable Start instruction. The kit owns heard state, Read priority and sound-off behavior.
- Focus and layout: PASS with the documented dense-list limitation. Stable board signatures preserve card nodes during playback. Explicit focus changes prevent scrolling. Hints have reserved height; desktop hint and Play stay visible while secondary controls scroll.
- Sizes: PASS for the required primary controls. Checked all STANDARDS sizes, with 375 through an iframe. Read has a 44 px minimum; a complete 44 px card fits each compact Tighten beat. Further cards may need inner scrolling.
- No giveaways: PASS. This is an open devising exercise, with transparent rules and no concealed answer or score.
- Honest numbers: PASS. The speech-rate estimate is stated on screen. Live elapsed time and planned time are reported separately.
- Standards: PASS. Solo students choose character needs, develop Jules's offers, revise pacing, perform, and connect a viewpoint with their community through the Devise prompt. Notes explain each standard.
- Motion off: PASS. The audit found no infinite animation. Timing and live waits remain unchanged. Used art is real, with no placeholders.
- Short choice sets visible: PASS after repair. All seven phone picker options fit, verified by their rectangles and a real click on the offered seventh option. Compact offer response buttons both fit in view.
- Resize mid-animation: PASS in the audit. No exceptions or stuck controls across states and held-click resize checks.
- Welcome delayed after first action: PASS. No welcomeAfter. Opening a picker makes the slot instruction stale, so the welcome is skipped unmarked.
- Unknown shown as unknown: PASS. Empty beats are marked empty with outlined tension points.
- One look, one meaning: PASS. Character colors always accompany names; checks use a check or exclamation as well as color.
- Badges say what is true: PASS. Checks are computed from the exact exercise rules, with empty beats flagged separately. The allGreen spoken prompt also waits for every beat to contain a line.
- Hint changes back: PASS. Mode changes, Stop, Reset and dialog return restore the current instruction.
- No answer by copying words: PASS. The choices devise a scene; no diagnostic or quiz answer is exposed by wording.

#### Audit leads
Ran audit_tool.py once with ports 9991 and 8795, inside its 40-minute limit. It completed with 223 repeated leads and 97 frames. The complete audit was not rerun after repairs. Focused follow-ups checked the affected paths instead.

- Read targets: fixed at 44 px minimum, measured at compact sizes.
- Add controls reported as 0 px text: intentional icon presentation. Their visible plus is a 20 px pseudo-element, their target is 44 px, and their full accessible label names the beat.
- Phone fold/overlap, missing picker steps and cascading missing line/cue states: fixed by reserving a separate transport area outside the main scroll viewport. Real phone input then opened the picker, placed all six lines, answered offers and completed six live cues. No cue/transport overlap remained.
- Phone board controls below the fold: retained as the specified vertical list, now within a scroll region. They are reachable by normal scrolling and keyboard focus. A single phone screen cannot display the entire six-beat board.
- Abbreviated card text: intentional. Full text is in the title, selected-card panel, picker and live cue. Added explicit text-overflow to identify the designed ellipsis. Dialogue content was not removed.
- Offer buttons below a compact panel edge: fixed by moving the offer above secondary editing controls. Both response buttons measured fully in view at 680x425.
- Tighten card viewports too small at 1000 and 760: enlarged/rebalanced the board and hid Add in narrow Tighten. Final first-card measurements: 44 px card inside 59 px at 1000, 84 px at 760, and 49 px at 680. Multiple/dense cards still scroll.
- Compact hint scrolling away: desktop hints and Play now stick within the panel. Final checked hint rectangles remained in view at 1366, 1000, 760 and 680. Phone hints can scroll away with their introductory panel; Read and transport remain available.
- Reset or editing controls past a panel edge: secondary controls retain panel scrolling. These are not a hidden short set of answer options. Offers and core playback controls take priority.
- Underlay text reported hidden by reset/offers dialogs: intentional native modal behavior; the background is inert and the dialog supplies the current controls.
- "1 arrives" grammar lead: false positive. This is the numbered label "Offer 1 arrives", not a plural noun error.
- Slot-first welcome not heard: intentional stale-line handling, as the spec makes that welcome stale when a slot is tapped. Picker instructions are shown immediately; no late welcome interrupts the new action.
- Rapid same-mode welcome cuts: fixed by preserving the current mode's speech instead of hushing it again. Follow-up log contains one spoken welcome with no cut.
- Controls moving on a mode switch: expected layout/focus change. Initialized Sound with its kit icon to avoid its first label-width change. Sound off cutting speech is expected kit behavior.
- Motion off, resize exceptions/stuck controls, held-click keyboard checks and five-repeat voice checks: clean in the completed audit.

The audit's original 223 count is not presented as a count for the repaired bundle. No full post-repair audit was run.

Harness notes: two early selectors containing quotes failed in drive.py and were retried with unquoted attribute selectors. An outer test host favicon request returned 404; later host frames use a data icon and have no errors. These were not tool JavaScript exceptions.

#### Frames looked at
Looked at both bar frames; three early layout frames; seven functional frames; keyboard, voice, live-wait and full-live frames; all twelve size frames; eight targeted frames including grayscale, seven-option picker and 24-card crowding; all 97 audit PNGs through 17 contact sheets; six focused repair frames; final Tighten frames at 1366, 1000, 760 and 680; same-mode, spacing, compact-card and hover checks. Inspected all four finished images and the rejected/replaced Dale candidate. Evidence stays in _scratch/three-viewpoints-scene/.

#### Art made
Four used generated illustrations, 202,982 bytes (198.2 KiB) in WebP. One Dale redraw. All three cutouts rekeyed with despill through the free art.py --rekey path. Full prompts and raw originals retained. No people in the used art.

#### Art still to paint
None. Browser speech is a separate limitation, not missing art.

#### Engine changes wanted
kit/curio.js, speakOne and Curio.voice item options: allow a supported optional role/bank voice selector per line while retaining queue cancellation and Read priority. No kit files were changed. Details are in handoff.md.

#### Left open
- No bank recordings, by Build instruction. Browser voice quality, distinct role timbres and actual delivery duration need a later by-ear review.
- Dense and compact multi-card beats use inner scrolling. The cold review should assess that tradeoff, especially four-line beats at 680x425.
- Phone board/hint content requires vertical scrolling. Main transport and live Done/Back are kept outside that scroll region.
- The completed full audit predates the focused repairs. A cold reviewer can run a fresh audit; this build did not start a polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: three-viewpoints-scene
#### Played
Cold grade-7 solo run through Devise, Tighten and mixed-role Perform before reading builder notes or source. Built the twelve-line example with held input, then reached its live-cue recap. Also assessed projector use, keyboard input, full/empty boards, narrow layouts, grayscale and Motion off. The rehearsal art and live spotlight are strong; the old ending felt like a generic timer.
#### Findings fixed
- **Blocker, general, Tighten:** a 48.8-second scene without setup or ending got four green lights. Empty beats now keep Pacing amber. The same cheap scene fails after repair.
- **Blocker, general, Perform:** jumping to the final line earned “rehearsal complete” and a full-plan comparison in 4.3 seconds. Track covered cues and jumps; show a partial/replayed run instead. The same jump now reports 1 of 12 cues.
- **Should fix, general, Perform:** live silence could be dismissed immediately and its instruction said to speak. Hold the specified two seconds, then enable Done; silence and stopped cues now say what is happening.
- **Should fix, general, phone Perform:** the live cue sat below the fixed transport. Put the cue first within the stage. Both live cue and recap now fit above the transport at 375×812.
- **Should fix, general, preview Devise:** the squeezed SVG flattened the tension curve. Move beat times onto the ruler and give the curve real height at 680×425 and 800×500, preserving 44-pixel Add/card controls.
- **Should fix, general, compact Tighten:** the audit confirmed Cut below the fold despite the hint naming it. Put edit buttons before the selected-line text and reduce compact spacing; preserve focus on visible Devise after a compact Cut, and Play after an offer response. Recheck the affected sizes only.
- **Should fix, general, voice/hints:** first-slot input was silent. Add a short once-only picker how-to. Selected-card hints name enabled move directions; compact Cut routes through Devise for the hidden Add control. Stale offers are invalid inside the offers dialog.
- **Should fix, general, first-tap dialogs:** the audit heard the Devise welcome over Offers and Reset. Block mode welcomes behind dialogs, give each dialog its current action line, and cancel it on closure. Stopped Perform cards retain the Perform instruction rather than naming hidden editing controls.
- **Should fix, general, sources:** the linked NCVS homepage did not substantiate 150 words/minute. Keep the spec's arithmetic but name 2.5 words/second as this exercise's planning assumption in source credit and notes.
- **Polish, general:** replace the generic recap question with this student's speaker counts and chosen turn. A fast Done rhythm is explicitly timing-only and does not claim to verify speech or acting.
- **Polish, general, art:** redraw Ms. Dale's prop with a clearly separated burgundy lanyard and blank badge. Keep the other three paintings, texture, palette and warm light.
- **Polish, general, picker:** tighten compact dialog spacing so its note and all seven options fit together at 680×425.
#### Findings left
All observed blockers and should fix findings are repaired.
- **Polish, general:** dense selected-card lists scroll in compact beats. The short picker choice set is fully visible; the six-beat preview and 44-pixel editing targets take priority. Showing all 24 cards simultaneously would require a different specified layout.
- **Verification limit:** browser fallback timbres and actual pronunciation remain a by-ear check. Recording audio is prohibited by CODEX-BUILD.md; no kit files changed.
#### Break it
- Three sides: omit the driver's need, or use only one character's needs. Amber names a missing role. Tags support open composition; they are not hidden quiz answers.
- Rising: keep the clash below tension 3. Amber stays on even with an otherwise passing scene.
- The turn: sweep every 0–3-second pause without a turn line; all seven fail. A tension-3 line after the turn fails; moving it before the turn passes. Only 1, 1.5 and 2 seconds pass the breath rule.
- Pacing: empty opening/ending, 14.8-second total, 79.6-second total with every beat under 15, and a 20.5-second crowded beat all fail. The original passing example remains 58.4 seconds.
- Offers: repeat place/remove twelve times. Offers unlock by the spec's cumulative-placement rule, but no scene check or success is earned. Locked offer, duplicate line and fifth card are rejected. Passing, reopening and accepting adds the offered line.
- Perform: skip to last, hammer Done, and tap Done during live silence. Skips are partial; fast full cue traversal reports timing only; silence cannot be skipped early. No score, saved best, reflection gate or claim to detect speech exists.
- Evidence: `review-rule-results.json` has 26/26 assertions; `review-skip-after.json`, `review-silence-after.json`, `review-timing-extremes.json` and held-input frames are in Scratch.
#### Voice walk
Fresh default board; Add/pick twelve lines at two-second intervals, pass offers 1–4, Tighten, two pause increments, Perform, Start, Done at the same pace. Default Maya role; other roles voiced. Final post-fix walk: 12/12 cues, 43.0 seconds against 58.4 planned, with no cut or dropped lines.
Started in order: pickerHow; offer1/pass; offer2/pass; offer3/pass; offer4/pass; welcomeTighten; allGreen; welcomePerform; Ortiz/Dale scene lines in board order; runDone. No narrator starts during character playback. Opening the picker intentionally replaces the stale Devise welcome with its current how-to.
| Line/kind | Expected starts | Observed |
| --- | --- | --- |
| Picker how, twelve openings | 1 | 1 |
| Tighten welcome, five same-mode taps | 1 | 1 |
| Hear Ortiz, five held taps | 5 | 5 |
| Passed-offer event, main run | 4 | 4 |
| Reset dialog how, five openings | 1 | 1 |
| Empty / passed Offers dialog how | 1 each | 1 each |
Read with Sound off, rapid mode/reset changes, card jump, pause edit and edit-to-stop were checked. First-tap Offers/Reset speak only their own how-to; closure restores the board hint. Earlier rapid runs recorded expected cancellation when actions made lines stale; the final main walk had no cuts or drops. This is muted log verification, not a listening claim.
#### Facts checked
- Fictional bus time 5:00, Friday cutoff, Maya's grade/trumpet role, Ortiz's twelve years, Dale's $40,000, family circumstances and all 40 lines: the spec's **Characters**, **Lines** and **Sources**, authored for Curio Class. Transport proposals, including “half the fuel,” are fictional dialogue, not verified savings.
- Six beats, 0–3 tension, highest-line aggregation, need/turn rules, 0–3-second pauses, 15-second beat and 30–75-second total limits: the spec's named **Scene checks**. Independent arithmetic confirms all 39 spoken estimates, two-second silence, and the 58.4-second example.
- Creating/refining choices (TH:Cr2), interpreting needs/pacing (TH:Pr4), speaking live (TH:Pr6), community viewpoints (TH:Cn10): [NCAS Theatre at a Glance](https://nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf). Each has a student action; notes retain practical home activities and required opening headings.
- Improvisation and rehearsal: [Viola Spolin, Northwestern University Press](https://nupress.northwestern.edu/9780810140080/improvisation-for-the-theater/). Offers/acceptance/blocking: Keith Johnstone, *Impro*, with [author/title checked at Bloomsbury](https://www.bloomsbury.com/uk/impro-9781350069039/), plus the book's Spontaneity discussion.
- Speech rate: [NCVS](https://ncvs.org/) does not verify the number on the linked homepage. It is now explicitly a planning assumption, with actual delivery varying.
- Contrast: independent [W3C WCAG calculation](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) gives ink/paper 14.41, ink/white 16.11, muted/paper 5.69, muted/white 6.36, brand/paper 4.95, white/brand 5.53. Grayscale retains names and check/exclamation symbols.
#### Sensitivity
Fictional access to extracurricular activities, household work schedules and a driver's livelihood merit care. A cultural reviewer should check casting and classroom discussion for stereotypes; Chen and Ortiz are names, not evidence of cultural traits. No traditions, hard history or people images are represented. The empty rehearsal room and props are deliberate, with students supplying the actors.
#### Flattest moment left
Reading and choosing the middle dialogue remains quieter than performing. It is the specified devising work, not a score chase. The improved recap now points back to the student's particular turn, rather than asking a generic mistake-assuming question.
#### Graphics
Inspected every used WebP, the redraw at final size, every targeted PNG, all seven standard desktop sizes, the 375-pixel iframe, maximum 24-card board and saved bar-reference frames. Four assets, no people, all `people` flags explicit. Art: 203,768 bytes; final bundle: 366,531 bytes. No placeholders or automatic external references.
#### Audit
Completed once within the 40-minute limit, Chrome 9961 and host 8765: **30 leads, 86 PNGs**, all inspected through 15 contact sheets, with confirmed compact leads also opened full size. Motion off, resize exceptions/stuck controls, held-click keyboard checks, five-tap repeats and quick taps were clean.
- Twelve tiny-text rows are the compact Add buttons' zero-sized text, replaced by visible 20-pixel plus glyphs inside 44-pixel targets.
- Two rows are an audit iframe-context attachment failure, not tool behavior. Independent 375-pixel main, live-cue, recap and seven-option-picker checks supply the phone evidence; the audit's phone coverage remains unverified.
- Nine scroll rows cover selected-line controls, Offers and Reset. The confirmed compact Cut/Hear problem is repaired with buttons-first ordering and visible focus targets. Offer answers remain fully visible; secondary Offers/Reset and long selected text retain scrolling. The “Hear it” hint match was actually “Play scene to hear it.”
- Seven welcome rows are expected: six first-slot taps speak pickerHow instead of the stale welcome; empty Perform cannot name disabled Start. The walk also exposed the separate Offers/Reset welcome mismatch, repaired with modal-specific how lines.
Final verification: 17/17 focused checks and 11/11 structural checks passed; all 57 allLines strings match the voice manifest. Temporary host removed and no listeners on the assigned ports. The audit precedes these last narrow repairs. Only affected frames and voice paths were rechecked afterward; no second full audit or polish round was run.
Wave lessons checked: immediate hints/Read, heard-state how lines, stable controls/focus, required sizes and targets, transparent composition rules, honest timing, standards actions, calm timing, visible picker choices, resize safety, unknown/empty marking, names plus symbols, truthful checks and returning hints.
#### Left open
- Keep proposed bank assignments; browser voices vary. No audio was recorded and no new paid service used.
- The spec requests a narrated first-live-cue how-to while also banning narrator speech during Perform. Chose its no-overlap rule: welcome explains Done; the waiting cue and Read carry the instruction. No narrator speaks over a performance.
- Initial oversized driver JS wait, a failed Chrome batch and a final main-path driver timeout were retried smaller; the final walk passed. A numeric CSS selector was corrected. Earlier host-only favicon 404 did not come from the self-contained tool, which has a data icon; the final phone harness also uses one.
- One review/fix pass, scoped rechecks only. No commits, shared-kit changes or deployment. Final artifact stays in the authorized tool folder; evidence stays in its Scratch folder.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Three Viewpoints Scene build handoff

#### Cold review changes, 2026-11-05
The cold reviewer played all three modes before reading this handoff. Empty beats now keep Pacing amber, so four green lights cannot conceal a missing setup or ending. Timing remains the spec's 58.4-second example. The 2.5-word-per-second rate is labeled as an exercise assumption; the NCVS homepage did not verify it.

Performance tracks covered cues and card jumps. Skipping to the last line or replaying a cue produces a partial/replayed recap, without treating the time as a full-run comparison. A full cue run measures timing only; it cannot verify live speech. The recap recalls the student's cast balance and chosen turn. Live silence holds for two seconds before Done works. Stop labels the cue as stopped.

The first picker has a short, once-only spoken instruction. Card-selection hints name only enabled move directions; compact Cut instructions route back to Devise for the hidden Add buttons. The principal's prop was redrawn with a readable burgundy lanyard and blank badge, preserving the other paintings and warm rehearsal style. New voice strings are in lines.json, with browser fallback retained under the no-recording rule.

On phones, Perform puts the live cue and recap before the curve and painted props so they remain above the fixed transport. At short two-row preview sizes, beat times move to the ruler and the curve gains height instead of flattening. Compact picker spacing retains all seven options and its note. The full original six-beat layout and painted scene remain.

The single review audit completed with 30 leads and 86 frames. Its iframe attachment failed, so phone evidence comes from separate drive checks. Compact Tighten exposed Cut/Hear below the panel edge; the follow-up repair puts edit buttons before line text, with all four 44-pixel controls visible at 680x425 and 800x500. Compact Cut focuses visible Devise; offer answers focus Play. Stopped Perform card taps retain the Perform instruction.

First-tap Offers/Reset could previously narrate the Devise welcome behind their modal. Welcomes now require no open dialog, and dialogs have once-only action lines, canceled on closure or confirmation. The dialog voice follow-up heard the appropriate line only, with resetHow spoken once across five openings. The final bundle was not subjected to a second full audit; only affected states and voice paths were rechecked. Read `codex-review.md` for the final disposition.

Review evidence and the final audit are under `_scratch/three-viewpoints-scene/review-*`. No shared kit changes or commits.

#### Sensitivity
This is fictional school-access and employment conflict, not a depiction of a cultural tradition. Maya Chen and Mr. Ortiz's names do not establish cultural traits. A sensitivity reviewer should check that casting and discussion do not turn financial access, family working hours, or a driver's livelihood into stereotypes. The prop-only rehearsal room intentionally has no people images.

#### Structure
`src.html` starts from the kit starter. CSS defines the rehearsal room, beat board and each mode's responsive focus. The script loads `scene-lines.json`, restores validated local work, initializes Curio.voice, computes checks, renders the board and curve, then wires editing, offers and the cue runner. Stable board signatures preserve card elements during playback and pause updates. `window.__tool` exposes state, analysis, editing and playback hooks for checks.

`scene-lines.json` contains exactly the spec's 40 options, their estimates, tensions, need/turn tags and offer locks. It is inlined by the bundler. `voice/lines.json` has every allLines string and character bank assignments. All runtime assets are bundled and offline.

#### Timing and tricky parts
Playback uses a cancellation token so Stop, a card jump or an edit cancels a pending pause, voice or cue without a stale continuation. A pause value is read on entry to each beat, including empty beats in Play scene. Editing stops playback; pause changes keep it running. Perform requires all six beats populated and waits on the chosen role, or every role in All three live. Run time includes live waits and pauses, measured from Start to the final Done. Planned time is captured at Start.

The narrator is hushed before playback. Character lines use V.say events with hint false. The live-cue instruction remains on screen and in Read, with no narrator interrupting a performance. Read first stops playback, then reads the current stopped-state hint. Browser speech is held to at least the estimated duration when it returns early. Motion off changes no timing.

Offers are triggered by cumulative successful placements, including an auto-placed accepted offer. A full target beat still unlocks its offer, with instructions to cut a line and add it from the picker. Passed offers reopen in Offers. Reset asks before clearing local work. Corrupt or inaccessible storage does not prevent play.

#### Open question decisions
- Took the spec's proposed character bank voices: Maya `big-sister`, Mr. Ortiz `friendly-dad`, Ms. Dale `firm-captain`; Jules is `casual-peer`. Did not choose the pitched-browser alternative. Build forbids recording, so these assignments are recorded in the manifest for future clips. Unrecorded lines use available English browser voices at pitch one. The tool routes roles to different available names where possible. A machine with one English voice cannot supply three distinct timbres.

#### Art
Four illustrations generated during this build with the image tool, not FLUX. Warm painted black-box stage and three keyed prop cutouts. Ms. Dale's first candidate added a desk and theatrical accessories; rejected it and generated the single-chair version. All finished assets inspected at their final sizes. Despill applied through `scripts/art.py --rekey`. No people in the used images. Prompts and raw originals are retained.

#### Responsive choices
At laptop widths the six beats, curve and Play remain in view. Under 900 px the board is two rows of three. At 680x425 the props become a slim strip and Add becomes a 44 px plus button in each beat heading. Tighten uses compact headings and puts beat times on the curve; its card lists scroll within their beat. At 375 px the board is a vertical list, the curve is above it, and Play/Stop stays fixed at the bottom. Perform's Done and Back controls also stay at the bottom on phones. Long dialogue is abbreviated on board cards with the full line in its title and selected-card panel; the picker and live cue show it fully.

#### Verification pointers
Scratch contains `numbers.json`, 24 rule/state assertions, held-input scene building, reload/reset evidence, playback jump/Stop evidence, keyboard building, two-second voice logs, twelve size frames, targeted rechecks, grayscale/Motion-off, seven-option picker, crowded-board and full twelve-cue live-run evidence. The full live test used simulated delivery intervals and completed in 48.2 s against a 58.4 s plan. Headless Chrome was muted, so this is not a by-ear review.

#### Engine changes wanted
- `kit/curio.js`, `speakOne` and Curio.voice item options: support an optional bank/role voice assignment on each line, preserving queue cancellation and Read priority. This tool currently routes browser utterances while waiting for role-specific bank clips. A shared supported selector would remove that workaround.

#### Remaining review attention
- Bank recordings are absent by Build instruction; available browser voices and durations vary. Review actual character delivery by ear later.
- Compact and maximally crowded boards deliberately use inner card scrolling. A full four-line beat cannot expose every 44 px card plus its controls in the 680x425 two-row layout. Check this tradeoff in the cold review.
- The phone picker keeps all seven options in three readable columns. The narrow board uses a vertical scroll region as specified; its header and transport stay outside that region. The hint and earlier character cards can require scrolling back into view.
- The school's transport and budget figures are fictional circumstances. Dialogue about fuel savings is not a measured transport model.

Build only. No commits, no branch changes, no polish round.

#### Audit outcome and targeted repairs
The single mechanical audit completed with 223 repeated leads, 97 PNGs, clean Motion off and clean resize/stuck-control checks. The full audit was not rerun after repairs. Every lead is answered by category in codex-report.md.

Post-audit repairs reserve space outside the phone scroll area for Play and Done/Back, expose all seven phone picker options, move Jules's offer above secondary editing controls, keep desktop hints and Play sticky, enlarge the Tighten card area, and give Read a 44 px minimum width. Intentional card abbreviations now declare text-overflow and retain their full title. Repeated taps on the active mode no longer cut the welcome. Empty Perform cannot queue the Start instruction. Repeated Hear uses a token to prevent stale light/voice cleanup. Card jumps update the selected card so subsequent edits affect that line. The allGreen event waits for a populated board as well as four green checks. A tiny numerical tolerance protects the exact pacing limits.

Targeted real-input checks confirmed visible compact offer buttons, all seven phone choices, six phone placements and six live cues through the recap with no transport overlap, mixed live/voiced roles, a valid 30-second boundary, same-mode welcome continuity, and selected-role hover contrast. Final Tighten checks at 1366, 1000, 760 and 680 retain the hint and expose a complete 44 px card in each populated beat. Multiple cards still scroll in dense or compact beats. All targeted browser checks were free of console errors and exceptions.

#### Final review verification
The final main voice walk completed all twelve cues in 43.0 seconds against the 58.4-second plan, with no cut or dropped lines. All seven phone picker options were visible, with no console errors in the final phone harness. Seventeen focused assertions and eleven structural checks passed. Final bundle: 366,531 bytes. The temporary host was removed, and all assigned ports were clear before the review report was written. No commits.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
