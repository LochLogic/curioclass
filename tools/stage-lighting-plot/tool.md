# Stage Lighting Plot: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: stage-lighting-plot

#### Built

Four-mode, offline lighting-design sandbox for grades 9-12: period research, an instrument plot, live faders and cue stack, and a 40-second rehearsal with relit scenery and a three-line graph. Includes inventory limits, half-meter hanging, editable channels and gels, gobos, Fresnel focus, PAR rotation, boom height, practicals, fades, story-turn editing, device storage and confirmed clearing.

Build only. No commits, deployment or polish round. Work is confined to tools/stage-lighting-plot/ and _scratch/stage-lighting-plot/. The image tool used its own generated-image cache before copying originals into this tool.

#### Numbers check

Recomputed in Scratch prepare.py and numbers.json before implementation. Levels use fractions of full, not raw percent.

- FOH ERS 19: throw 11.37190 m, diameter 3.80601 m, energy 0.8790, shown 0.5848.
- First-electric ERS 36 to Nora's chair: throw 5.33198 m, diameter 3.46493 m, energy 1.0605, shown 0.6537.
- First-electric Fresnel: flood diameter 4.97269 m, shown 0.4024; spot diameter 1.88034 m, shown 0.9727.
- Straight-down PAR: throw 4.9 m, axes 1.03002 by 2.44341 m, shown 0.99916.
- The first-electric examples in spec.md omit Nora's x offset. PAR example axes also differ slightly. The computed geometry wins; spec.md is unchanged.
- NOAA approximation: sunrise 09:19.48 CET, sunset 15:14.83 CET, daylight 5.92254 hours, consistent with the research card.
- Contrast: brand/panel 6.732:1; brand/section 6.379:1; brand-ink/brand 7.182:1.
- All 24 instruments at 100 with Fresnels on spot: tested floor mean 0.67395, while seated faces approach 1. The spec's floor-mean-near-1 expectation does not follow from its finite pools.

#### Feel check

Played the full design/rehearsal loop, including a keyboard-only two-cue design and three complete 40-second rehearsals across the sparse, turning and six-instrument plots. Best moment: Nora steps away from the table into a separate pool, and the face line turns while the room loses its warm center.

Flattest moment 1: the initial drawing spent too much space on the empty house between stage and FOH. Compressed that drawn gap with an explicit label, kept real throw geometry, centered the plan and enlarged the waiting lantern portrait.

Flattest moment 2: compact settings and the cue inset made revision feel like hunting for controls. Combined settings into a compact grid and reserved preview space beside the horizontally scrolling faders. Moved Edit turns into the transport so it cannot cover graph labels.

Compared a rendered frame against Beat Lab and inspected Snowy Mail Route before implementation. Scratch bar-comparison.jpg places the painted room beside Beat Lab. The scene is intentionally a dim period interior, with a detailed set and responsive pools rather than a decorative backdrop. The plan remains technical and legible. No score or celebration was added.

#### Done when

1. PASS: plan, cue board and Run view/graph dominate their modes at 1366x768 and 680x425. Reviewed the full-size frames and all eight sizes.
2. PASS with source corrections: 29 core functional checks include all five specified setups, gel transmission, PAR rotation, low-angle projection, inventory, snapping and unique cue numbering. See post-functional-result.json.
3. PASS within the disclosed simple model: the floor/back wall are mapped to the painting; paired plan/Run frames show the pool at Nora and the corresponding head brightness. Furniture has no independent shadow geometry.
4. PASS: complete two-cue run produces the beat-5 observation and spoken noTurn4. Cues at 1, 2, 5 and 8 produce allTurns. The event check filters changes to cue-bearing beats so blocking alone cannot claim a designer's turn; handoff explains the spec ambiguity.
5. PASS: Stop, Step, Back and beat jumps act in their handler. A live fader was reflected in run levels within 50 ms; seven additional checks verify independent fades, live board tracking, channel remapping, next-cue takeover and blackout. Stop preserves crossing positions and exit opacity; latest-freeze-result.json confirms pixel-identical stopped canvas frames.
6. PASS for blackout, dark narration and finite all-up rendering. All-zero mean is ambient 0.02955 and shows the warning. All-up never errors. FAIL for the separate mean-near-1 expectation; the honest result is 0.67395 for the tested concentrated plot.
7. PASS: keyboard design restored one instrument and two cues in a fresh tab. A held Clear design / confirm sequence empties storage and retains focus on Clear design. Clear and Remove reset obsolete channel readouts; clear also resets the label/fade editor. Storage calls are guarded and its status is visible.
8. PASS: five held hangs at a 2-second pace start aimHow once. noTurn4 and allTurns each start again when their event repeats; dark starts on repeated dark beats. Queued lines carry mode/beat validity through Curio.voice.
9. PASS for the provided cut: all eight beats are taken verbatim from spec.md; dialogue compared against [Project Gutenberg 2542](https://www.gutenberg.org/cache/epub/2542/pg2542-images.html). Parenthetical directions and omissions follow the supplied adaptation.
10. PASS: nine images load, inspected individually and in contact sheets. No generated people or lettering; actors are code silhouettes.

#### Wave lessons

- PASS, hint and voice: mode hints change synchronously; Read uses the current hint; Curio.voice owns heard state, stale checks, Read priority and event repetition. Held-click evidence is in run-test-log.txt and voice-five-result.json.
- PASS, focus and layout: no focus on load; board rebuilding restores focus with preventScroll; record/update do not replace their controls. Dialog removal focuses Add turn deliberately.
- PASS, sizes: all eight required sizes, with 375 through port 8775's iframe. Header and primary controls use 44 px targets; compact settings remain in view. Secondary script/cue lists scroll.
- PASS, no giveaways: a sandbox with no hidden correct answer, score or success meter.
- PASS, honest numbers: visible model/gel qualifications, numeric graph ranges and a How the light works note. Computed spec discrepancies are reported.
- PASS, standards: a solo student researches motivated sources, plots technical choices, rehearses, reads the result and revises, covering TH:Cr1, TH:Cr3 and TH:Pr5.
- PASS, Motion off: no infinite animations remain; the 3.53-second check was still in beat 1 and running. Pacing uses the same five-second beat clock.
- PASS, short choice sets: all five research cards, four motivations, four shelf types and eight beat buttons stay visible. Faders intentionally scroll horizontally as the spec requires.
- PASS, resize mid-animation: full audit stress found no exceptions or controls left disabled. Runtime state is independent of canvas size.
- PASS, late welcomes: each mode uses a scoped welcome; no welcomeAfter; a Run welcome becomes stale after Run or Step.
- PASS, unknown as unknown: there is no concealed-state diagnosis. No cue means black/ambient, and its observation says so.
- PASS, one look/one meaning: graph lines differ by color, dash and label; gel choices retain names; actors keep N/H labels.
- PASS, truthful badges: inventory, selected channel, saved state and run status derive from current state. The tool does not award readiness or achievement badges.
- PASS, hints change back: mode changes, hanging, cue loading and clearing update the hint immediately; Read reads that state.
- PASS, no answer by copying: the student composes and evaluates a design; research offers evidence rather than a correct cue recipe.

#### Audit leads

The one full audit finished in 1,584.04 seconds (26 minutes 24 seconds), exit 0, with seven leads. All default sizes and mode states were clean. No runtime errors, Motion-off loops, resize failures, repeated-how failures, lost events or quick-tap lost lines were found. All 45 audit PNGs were reviewed in twelve contact sheets.

1. Plan / LIVE BEAT overlap: intentional corner preview, explicitly requested by the spec. Toggle Preview off to use that plan area.
2. Plan / hpBeat number overlap: the same intentional inset caption; no text is clipped.
3. Run canvas keep-region covered at 680: the specified script caption at the bottom of the view.
4. Graph keep-region covered: transparent, real keyboard/tap targets over the beat numbers. They do not obscure the drawing.
5. Hint covered in turn editor: intended native modal backdrop. The dialog supplies its own instructions and controls.
6. Hang on pipe welcome not heard: correct STANDARDS behavior. That first tap speaks aimHow; welcomeHang becomes stale as soon as the light exists. It must not arrive late.
7. Back changes nothing at beat 1: fixed with visible boundary feedback naming Run scene and Step. A held-click recheck passed.

Final targeted changes after the audited bundle also repair independent live faders, channel preservation, repeated-beat cue numbering, actor/turn labels and cleared readouts. Final checks passed 29 core assertions plus seven live-board/fade assertions; targeted layouts and clear/remove checks had no console errors. No full audit was repeated. Scratch audit-dispositions.md records every lead and the final snapshot limits.

#### Frames looked at

Scratch bar-frames (2), early-frames (5), sizes-1/2/3-frames (32), run-frames (3), functional-frames, extras-frames (5), keyboard-frames (2), feel-frames (4), targeted-frames (11), final-core-frames (4), final-layout-1/2-frames (14), late-frames (6), graph-final-frames (2), post-audit-frames (3), post-layout-frames (8), and readout-final-frames (2). Contact sheets cover every retained frame in those groups; key laptop, compact and phone views were also opened at full size. Superseded failed setup frames were replaced during the size run. All 45 audit frames were reviewed in contact-audit-1 through contact-audit-12.

#### Art made

Nine images, 622,114 bytes (607.53 KiB) total WebP. No redraws were needed; the three lantern cutouts were rekeyed with despill and the PAR resized to a 900 px long side. Final prompts and provenance are in art/prompts.json. Source has 1,980 readable lines, longest line 159 characters. Bundle: 1,158,298 bytes (1,131.15 KiB), under 2 MB. Final node syntax check passed.

Illustrations were made with the built-in image tool; the complete prompt set is tools/stage-lighting-plot/art/prompts.json. No external artwork was downloaded.

#### Art still to paint

None.

#### Engine changes wanted

None required. Kept the specialized light model local, following the spec's engine direction.

#### Left open

- The all-up floor-average expectation is contradicted by the model calculation, as described above.
- The turn-feedback interpretation, simplified projection and furniture lighting remain explicit cold-review topics in handoff.md.
- Gravel-ranger / Algenib narration remains unrecorded under Build's no-recording instruction; browser speech is the fallback. Headphone delivery remains for cold review.
- Pipe names and coordinates follow the supplied table; their SL/SR convention is noted for cold review.
- The kit Sound label changes header widths; the audit noted six controls shifting, with no overlap or lost focus. This remains a cold-review layout choice.

All owned Chrome processes and servers are closed; ports 9970, 9971 and 8775 are clear. host.html is removed. The report is the final build action.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: stage-lighting-plot

#### Played

Cold as a grade 10 solo designer and a projecting teacher: hung and aimed a real drag, explored research, recorded cues, ran all eight beats, stopped, stepped, went back and edited turns before reading builder files. The plan is compelling; the first cue-board visit was flat.

#### Findings fixed

- Blocker, general, turn feedback: unchanged cues plus fixed blocking could earn allTurns. Compare cue looks at identical blocking; observations and voice now share the same criterion.
- Blocker, general, empty turns: removing every mark earned allTurns. It now invites Edit turns.
- Should fix, general, voice: the real two-second path dropped aimHow behind the welcome and cut gel/Research instructions. Shortened those instructions and advance to aiming/gel narration when the preceding physical step is complete. The final real-input walk starts every relevant line in order; Read retains priority.
- Should fix, general, dark narration: a lit cue fading from black could trigger a stale warning. Wait through the initial crossing and validate actual light when speech starts.
- Should fix, general, modal voice: the cold turn-editor side-path frame and log showed Run instructions continuing behind the dialog. Dialogs now hush background narration; welcomes/results cannot start under a modal, and closing can recover an unheard welcome. Post-audit checks confirm quiet dialogs and welcome recovery; Run narration is cut when Edit turns opens.
- Should fix, general, facts: cool window light was presented as the only possible nighttime source color. Identify it as this design's interpretation; street lamps can differ.
- Should fix, general, source observation: position matching sounded like an evaluation of aim. State its 2 m/30-level assumption and point to Preview.
- Should fix, general, gel hint: it suggested recording a gel in a cue. Explain that gels apply throughout the design; cues record levels.
- Should fix, general, art: daytime Run window, oversized central table, bare-chimney lamp and standing-shaped seated adults. Edited the set, moved practical glow anchors and drew seated poses.
- Should fix, general, instrument art: ERS pictured external barn doors. Redrew it with framing shutters and gobo gate; rekeyed cutouts to reduce green fringe.
- Polish, general, flattest moment: Cues now opens its existing live Preview unless the student chose otherwise; recording highlights the earned cue in the stack.
- Should fix, general, phone Cues: four recorded cues pushed Window backing gel partly out of view. Pinned the gel control below the scrolling cue stack; confirmed at 375 px.
- Should fix, general, header: the audit confirmed six controls shifted when Sound changed its label. Reserved its label width, including a compact phone width; targeted checks measure zero control movement at 1366 and 375 px, with no clipping in compact frames.
- Polish, general, notes: added named links, model/feedback assumptions, compact keyboard instructions, unhurried Step reading and sensitive-content guidance.

#### Findings left

- Specification: SL/SR names and house-right coordinates conflict with normal actor-facing audience usage. Kept the specified coordinates and named the correction in handoff.
- Specification: concentrated all-up pools do not imply a floor mean near 1. Preserved honest saturation and model assumptions.
- Polish: the compact 680x425 observation strip scrolls. Kept the specified dominant Run view and 120 px graph; full laptop observations fit.

#### Break it

- Unchanged ERS cues at 2, 5 and 8 after one true change: before, allTurns; after, only beat 2 counts and beat 5 gets noTurn. Both runs used the full 40-second transport.
- Delete all story turns, leave no cues: before, allTurns; after, noTurns and eight repeatable blackout events. No score, saved best, quiz or reflection gate exists.
- Twenty-two functional assertions pass: five optical setups, transmission and gobo behavior, inventory/slot limits, unchanged-cue rejection, held cues, real cue turns, blackout/visibility, Stop freeze, 24-instrument all-up finite saturation, Preview, persistence and fixed voice inventory. Keyboard-only input at 760 px hung, aimed and recorded a cue with focus retained on Record cue.
- All-zero/no-cue runs remain dark; a real amber on/off cue design produces changes at 2, 5 and 8 and allTurns after its full run. Endpoint settings never award a score; the observations describe the chosen design.
- Graphs retain their units, ranges and distinct dash patterns. Position-based source matching explicitly does not assess dramatic quality.

#### Voice walk

Real held input (0.12 s, 2 s pace), using drive.py's CDP primitives: welcome tap, shelf-to-pipe drag, ring drag, Gel, Cues, beat 1, Record cue, Research, window, motivation, Run, Run scene, complete scene.
Final order: welcomeHang, aimHow, gelHow, welcomeCues, researchHow, welcomeRun, dark, noTurn1. Each relevant how-to starts once. Completing hanging/aiming cuts the now-obsolete preceding instruction, rather than leaving the next instruction queued until it is stale. Main-path log: Scratch voice-main/completed.json.

| Line / kind | Expected | Spoken |
|---|---:|---:|
| Main-path six instructions | 1 each | 1 each |
| aimHow / five hangs | 1 | 1; four silent |
| dark / five separate dark steps | 5 | 5 |
| noTurn / unchanged-cue full run | 1 | 1 |
| allTurns / actual-change full run | 1 | 1 |
| noTurns / removed marks full run | 1 | 1 |

Sound-off Read speaks the current hint. Selected audit repeats and quick taps are clean. Final dialog tests have empty speech queues while open, and closing recovers an unheard welcome. No recording was made; browser speech is the fallback.

#### Facts checked

- All eight dialogue excerpts, attribution, lamp on table, open hall, stove/fire/winter, upstairs party, cloak, ring exchange and last door sound: [Ibsen, Sharp, Project Gutenberg 2542](https://www.gutenberg.org/cache/epub/2542/pg2542-images.html), Acts I/III. Corrected beat 1's changed capitalization after a substituted dash. Cuts and directions are identified as excerpts.
- 1879 Copenhagen premiere, Royal Danish Theatre, 21 December: [University of Oslo, Virtual Ibsen Centre](https://www.hf.uio.no/is/english/services/virtual-ibsen-centre/on-ibsen-s-work/du/).
- Gas-era stage lighting and Savoy electric stage in 1881: [The Times, 29 December 1881, contemporary account](https://gsarchive.net/carte/savoy/electric.html).
- 1870s kerosene lighting: [Smithsonian, Spencer lamp patent model, 1878](https://americanhistory.si.edu/collections/object/nmah_305002). Candle/flame and daylight temperatures: [the spec's Color temperature source table](https://en.wikipedia.org/wiki/Color_temperature); values are approximate, not every flame or sky. Cross-checks: [IES D65](https://ies.org/definitions/standard-illuminant-d65/) gives about 6500 K; [Chautauqua lighting guidelines, glossary](https://www.chautauqua.com/wp-content/uploads/2021/07/Colorado-Chautauqua-Lighting-Design-Guidelines.pdf) gives candlelight 2000 K and daylight/flash 5500 K.
- Oslo late-December sunset about 15:15, about six daylight hours: [NOAA equations](https://gml.noaa.gov/grad/solcalc/calcdetails.html), cross-check [Oslo December 2026](https://www.timeanddate.com/sun/norway/oslo?month=12): 26 Dec 09:19 to 15:15, 5 h 55 m 52 s. Nighttime source choices and dramatic readings are interpretations.
- Rosco gel names: [Roscolux manufacturer sheet](https://us.rosco.com/sites/default/files/content/resource/2016-09/rosco_roscolux.pdf); [LEE 201](https://leefilters.com/colour/201-full-c-t-blue/) and [204](https://leefilters.com/colour/204-full-c-t-orange/). Display RGB, warmth, transmission and output are stated model assumptions.
- ERS lens choices/shutters and Fresnel focus: [ETC Source Four documentation](https://www.etcconnect.com/Products/Entertainment-Fixtures/Source-Four-LED-Series-2/Documentation.aspx), [ETC spot/flood control](https://www.etcconnect.com/webdocs/Fixtures/fos4_Fresnel/Content/fos4/Overview_Fresnel.htm). PAR oval/rotation follows the specified educational model.
- Independently computed: FOH ERS19 throw 11.37190 m/pool 3.80601 m; first electric at table, 5.25547/3.41521 m, Fresnel flood 4.90133 m/spot 1.85336 m; PAR 1.03002 by 2.44341 m. Including Nora's x offset independently gives throw 5.33198 m, ERS pool 3.46493 m, Fresnel flood 4.97269 m and spot 1.88034 m. Computed coordinates take precedence over the spec's inconsistent examples.
- NCAS TH:Cr1, Cr3, Pr5: catalog module matches the spec; research motivates a plot, rehearsal supports revision, and instrument/focus/gel/cue work supplies technical practice. [NCAS](https://www.nationalartsstandards.org/).

#### Sensitivity

Historical Norwegian marriage roles, identity, separation and parenting need the fresh sensitivity review. Examine whether the fictional period silhouettes and directions respect Nora's agency. Notes discourage disclosure of personal family circumstances. No painted people, no claim to represent all Norwegian families.

#### Flattest moment left

Reading long script excerpts at a fixed five-second beat can feel rushed. Kept the specified 40-second run; notes point to Step for an unhurried reading. No extra topic or mode added.

#### Graphics

All nine images inspected individually and in context, one coherent detailed period style. Built-in imagegen edited the set twice and ERS once; prompts are in art/prompts.json, outputs art/slp-set.webp and art/slp-ers.webp. Original set retained in Scratch. No people images or missing art tokens. Final bundle 1,109,769 bytes (1,083.76 KiB); WebP art 584,866 bytes. Recomputed AA contrast: magenta/panel 6.732:1, magenta/section 6.379:1, dark text/magenta 7.182:1, body text/cue panel 14.369:1. Motion-off and grayscale frames inspected; graph patterns survive grayscale.

#### Audit

Completed once with the required 40-minute bound, Chrome 9941 and host 8745. All 48 audit PNGs were opened in 12 contact sheets, with relevant compact/phone frames also inspected at full size.

- Leads 1/4: horizontal phone faders are explicitly required by the spec; the main Record control and separate window gel remain visible.
- Leads 2/3: LIVE preview caption intentionally overlays the plan in the requested corner inset.
- Leads 5/6/9: the caption overlays the bottom of the Run canvas; transparent 44 px beat buttons overlay graph labels without hiding them.
- Lead 7: native modal backdrop covers the footer hint; the dialog has its own instructions and focus trap.
- Lead 8: new seated-state test clicked Hang on pipe where compact CSS hides it. Corrected the fixture to plan/Enter; scoped real-input checks pass at all three sizes with focus on the plan.
- Lead 10: a first Hang on pipe tap speaks aimHow and makes the empty-stage welcome stale. This follows the first-tap rule; no late welcome was added.

The audit also confirmed Sound's header shift; fixed locally and measured zero shift. Modal speech, discovered in the cold side path, is also fixed. The frozen audit snapshot predates those two fixes and the fixture correction; eight laptop/compact shots, three phone shots, the final main voice walk and verify_post.py confirm them. No full audit was repeated.

No runtime exceptions, Motion-off loops, resize failures or selected repeat/quick-tap defects. The 22 functional checks and keyboard-only path pass. All latest targeted shots report zero errors. Early driver/host fixture failures were retried in smaller batches; a phone lexical-global lookup was repaired, rather than counted as a tool failure.

Wave lessons checked: state-matched hints/Read, once-only how-to/event repetition, focus retained, all eight sizes and 44 px controls, honest model assumptions, no hidden-answer game, real standards practice, Motion-off timing, intended choice scrolling, resize, truthful labels and no copied-answer route.

Owned Chrome/host ports are closed and host.html is removed. Final source syntax passes; no kit edits, commits, uploads or publication.

#### Left open

No additional implementation blocker or should-fix remains. The spec-owned SL/SR convention and all-up floor-average expectation need a spec decision; the disclosed surface-mapped furniture/no-shadow approximation and browser narration remain explicit limits. No kit change, no commit, no external publishing. No unattended question was left pending; source-backed and spec-leaning choices are stated above.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Stage Lighting Plot build handoff

#### Structure

src.html starts from the kit starter and theme-912. It contains responsive workspaces, source and script tables, persistence, the instrument model, cue transport, the plan painter, room relighting and the graph. Curio.voice owns narration; no kit file or engine was changed. window.__tool exposes geometry, samples, completed looks, pose and transport for independent checks.

All nine generated paintings are in art/. Full prompts, provenance and keying settings are in art/prompts.json. Original generated PNGs are in art/raw/. The set is neutral-lit for multiplication. Actors are code silhouettes, as specified.

#### Model and rendering

- Instrument output and transmission use the stated radius and energy formula. Level is divided by 100. ERS, Fresnel and PAR use different edge widths; Fresnel smooths its outer half. Gobos mask the beam. PAR rotation changes its oval axis.
- Oblique plan pools stretch along the throw direction, capped at six times to keep very low boom angles tractable. Focus rings project onto the floor in this simple model. Head height changes received energy. This is not a full three-dimensional cone-intersection or shadow solver.
- Light buffers are 160 by 90. The painting's floor corners in its 1600 by 900 frame are [0,891], [1600,891], [1280,508.5], [320,508.5]. The back wall occupies [320,67.5], [1280,67.5], [1280,508.5], [320,508.5]. The mask is blurred 2 px and multiplied; practical glows are added separately.
- The floor uses a four-corner trapezoid mapping. Furniture inherits its mapped surface light, without cast shadows. This limitation is stated in How the light works.
- Graph brightness samples the floor on a 20 by 14 grid. Warmth is energy weighted over that floor; the face line samples the specified head points. Each line shows its own numeric range and line pattern. Nora counts as offstage at beat 8.
- The physical FOH gap is compressed only in the plan drawing, and labeled. Throw calculations retain y = -6 m.

#### Cues and transport

Cues store levels, with gels belonging to instruments throughout the scene. The last cue at or before a scrubbed beat gives its completed look. Multiple cues on the same beat have decimal numbers; the last defines that beat's target. Fades can continue into a beat without a new cue. A new cue starts from the current live fade levels.

Stop snapshots light levels, actor positions, exit opacity and the practical flicker phase. Step, Back and the graph's accessible beat buttons stop and jump. Switching to Cues can leave the scene running; its board follows the live look, and a fader overrides only its own channel until the next cue. Other channels keep fading. A complete run keeps eight five-second beats, regardless of Motion.

All design storage uses curio-lighting-plot in try/catch. A visible footer reports device-only storage and storage failure. Clear design confirms before removing work. Runtime pose, mode and current beat are not persisted.

#### Open questions and spec reconciliations

- Family engine question: keep the model local, following the spec's explicit None direction. Moving a reusable beam model into kit/stage.js is a later architecture decision, not a dependency of this build.
- Source numbers: including Nora's x offset gives first-electric throw 5.33198 m, ERS 36 pool 3.46493 m, Fresnel flood 4.97269 m and spot 1.88034 m. Spec examples appear to omit the offset. At 4.9 m throw, the PAR axes are 1.03002 by 2.44341 m. The implementation follows recomputation; spec.md is unchanged.
- All-up brightness: 24 instruments at 100 with Fresnels on spot produce local face brightness near 1, but a floor mean of 0.67395 in the tested concentrated plot. The spec's mean-near-1 expectation does not follow from its finite pools. No artificial boost was added.
- Turn feedback, repaired in cold review: the descriptive graph includes fixed actor movement. `designChanges()` compares current and previous cue looks at the same actor marks, excluding blocking-only differences. Observations and narration use the same within-one-beat comparison and 0.08 threshold. An empty turn list prompts Edit turns rather than allTurns. This preserves the two-cue noTurn example without pretending that unchanged cues are design changes.
- Cue numbers: ordinary cue-bearing beats count 1, 2, 3; additional cues on a beat add 0.5 in record order. The next beat starts at the next unused whole number, so three repeated cues cannot collide with the next beat's number. All cues at a beat fire as one target because the scene has one trigger per beat; the final snapshot wins.
- Pipe coordinates and SL/SR names follow the supplied table exactly. Confirm that the intended naming convention agrees with +x toward house right and SL at x = -6 in the cold review.
- The script uses the provided eight-beat cut verbatim. Dialogue was compared with Project Gutenberg 2542. Its parenthetical directions and omitted material follow the supplied adaptation, rather than claiming to reproduce all original stage directions.

#### Review next

Read codex-report.md and Scratch evidence. The recording bank voice is specified as gravel-ranger / Algenib, but no speech was recorded, per Build instructions. Browser speech is the current fallback. Review headphone delivery and the simplified wall/furniture mapping in a cold review.

Secondary long script and cue stacks scroll. Cues intentionally scrolls faders horizontally, including at 375 px. Preview reserves space beside those faders. Compact Hang combines settings into a grid; keys 1 to 5 select a pipe on the plan and Enter hangs, including where the separate pipe picker is hidden.

#### Engine changes wanted

None required. No changes to kit/stage.js, kit/curio.js or kit/curio.css were made.

#### Final build checks

The one full audit completed in 1,584.04 seconds with seven leads. All default sizes/modes, Motion off, resize stress, held-click runtime checks, repeat speech and quick taps were clean. Six leads are the intentional preview/caption/scrubber/modal layers or the required first-tap welcome skip. Back at beat 1 now gives visible boundary feedback. All 45 audit frames were reviewed. Scratch audit-dispositions.md addresses every lead.

Final targeted changes after that audited bundle keep independent live faders and channel remapping coherent, preserve a normalized channel, keep cue numbers unique, make turn numbers and actor labels legible, and store the native Algenib name with its gravel-ranger bank id. The final core check passed 29 of 29 assertions, plus seven independent live-board/fade checks. Confirmed clearing left the saved design empty and focus on Clear design. Clear and last-instrument removal also reset the obsolete channel readout; clearing resets the cue label and fade editor. Post-audit, post-layout and final readout frames were inspected; no full audit rerun was made.

#### Build scope

Build only. No commits, deployment or polish round. Writes are confined to this tool and _scratch/stage-lighting-plot, apart from the image tool's own generated-image cache. The final report records the one audit run and any remaining leads.

#### Cold review changes, 2026-11-05

The reviewer played the entire tool before opening this handoff, codex-report.md, notes.md or src.html. All new evidence is in Scratch folders with cold, play, break, voice-main, fix-frames, phone and review-audit names; the original builder evidence remains separate.

Cue feedback now rejects both confirmed cheap passes: unchanged cues where blocking changes the face line, and deleting all story turns. Source matching explicitly names its position/level assumption rather than claiming that it assesses aiming. Blackout narration waits through the initial crossing and rechecks actual light before playing. Gels are described as instrument-wide settings, never cue snapshots.

The Hang, aiming, gel and Research instructions are shorter so the actual two-second held-click path can hear each relevant how-to. Completing hanging or aiming advances the next instruction at once, cutting the instruction for the completed action. `voice/lines.json` mirrors those changes and adds the empty-turn event. Dialogs hush background speech and gate welcomes/results while open; closing recovers an unheard welcome. Browser speech remains the fallback; no audio was recorded.

Cues opens its existing Preview unless the student has explicitly chosen a setting, so moving a fader visibly changes the room. Newly recorded cues receive a restrained recording highlight and scroll into the cue stack view. Motion off retains a static highlight. The window gel selector stays pinned beneath the independently scrolling cue list, including on phones.

The room painting was edited twice with imagegen: winter night, a white glass lamp shade and a smaller table aligned with the plan. Practical glow anchors were updated. ERS art was repaired to show internal framing shutters and a gobo gate instead of external barn doors; the three cutouts were rekeyed to reduce green fringe. Seated actors now have adult seated poses instead of shortened standing silhouettes. Paintings remain empty; the spec's fictional actors remain code silhouettes.

#### Sensitivity

A fresh sensitivity reviewer should examine the historical Norwegian setting, representation of unequal marriage roles, and the treatment of separation and parenting. Notes frame the excerpt as historical fiction and avoid asking students to disclose family situations. The named fictional silhouettes are intentionally faceless, in period clothing, with no generated people images. No claim about all Norwegian families is intended.

#### Review boundaries

The specified SL/SR names conflict with the usual actor-facing audience convention when +x is house right. No coordinates or names were silently changed; spec correction remains open. The simplified model does not create cast shadows or a full three-dimensional furniture solver. An all-up floor average need not approach 1 for a concentrated plot; no fake boost was added. These are specification/model limits, not reported as passing a more exact physical simulation.

#### Cold review verification

The single full review audit completed inside its 40-minute bound on Chrome 9941 and host 8745. All 48 PNGs were inspected. Its ten leads are the specified fader scroller, intentional preview/caption/scrubber/modal layers, the correct first-tap replacement of the obsolete Hang welcome, and a compact seated-state fixture that used a hidden Hang button. That fixture now uses the visible plan and Enter. The audit found no runtime exception, infinite Motion-off animation, resize failure or selected repeat/quick-tap defect.

The audited snapshot preceded the final modal-voice guard, fixed Sound width and corrected seated-state fixture. Scoped post-audit checks cover quiet/recovered dialog narration, Sound-off Read, zero header movement, and visible-plan seated input at 1366, 680 and 375 widths. The final two-second real-input main voice walk starts all six relevant instructions once, in order. All post-audit driver shots have zero tool console errors. Twenty-two functional checks and the keyboard-only hang/aim/record path pass. No full audit was repeated.

The final report names specification-owned limits and the remaining compact observation scrolling. All owned debugging/host ports are closed and the temporary tool host page is removed. No git commit or publication was made.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
