# Body Thermostat: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: body-thermostat

#### Built

Lab, Experiment and Fever, using the written one-second Euler model, Curio.voice, theme-912 and Plane.
Eight generated paintings are embedded. Thermal color, sweat, shivering, insulation and the four response gauges follow model data.
The notebook retains immutable trial conditions, early stops, sampled temperatures, extrema and two selected traces.
All writes stayed in the assigned tool and Scratch folders. No commits, shared-engine changes, audio recording or polish round.
The report was finalized last to honor the user's stop instruction rather than writing the report at the first bundle.
Cleanup caught LibreOffice Python launcher descendants left by parent-only termination. Matched and closed this tool's
five host process trees; HTTP then refused port 8775. Used Chrome/host ports are closed, and host.html is absent.

#### Numbers check

Independent Python recomputation: `_scratch/body-thermostat/check_model.py`, `numbers.json`.
Extracted implementation functions checked in Node: `verify.js`, `model-verification.json`.
PASS: all 16 worked/worst cases; 2,560 condition/response combinations stay finite and honor stop boundaries.
A: 37.00000 at 10, 30, 60 min. B: 37.44342 at 30; 37.44360 at 60. C: 38.38598 at 60.
E: 38.5 crossing at 30.4833 min; 39.49719 at 60. I stops at 1226 s / 20.4333 min; J at 763 s / 12.7167 min.
K: 38.29295 at 30; L: 37.00004 at 60. Worst hot cases stop at 980 and 1439 s.
C = 208,200 J/°C. MET conversion is 69.733 W using 4184 J/kcal; the spec's 69.8 W is an approximation.
Exercise watts round to 195, 391, 547. Evaporating 600 W corresponds to 0.890 L/h, rounded to 0.9.
Used exact 70/15 conductance rather than rounding to 4.667, preserving the stated exact resting balance.
Source mismatch found: ASHRAE F21 SI chapter 9 gives 3490 J/(kg K), not the spec's 3470, and 2.43 million J/kg at 30°C,
not exactly 2.426 million. Kept the written, explicitly labeled model constants so its worked cases remain reproducible.
WCAG ratios recomputed: rose/panel 4.94, rose/section 4.68, dark ink/rose 5.19, hot/stage 8.91, cold/stage 8.76.

#### Facts checked

- Average normal 37°C / 98.6°F: NIH MedlinePlus, Body temperature norms, checked live 2026-11-07.
  https://medlineplus.gov/ency/article/001982.htm
- Fever 38°C / 100.4°F: CDC, Definitions of Signs, Symptoms, and Conditions of Ill Travelers.
  https://www.cdc.gov/port-health/php/definitions-symptoms-reportable-illness/
- Hypothermia below 35°C / 95°F, warmth/dryness and help: CDC, Preventing Hypothermia.
  https://www.cdc.gov/winter-weather/prevention/index.html
- 103°F or higher as a heat stroke sign, cooling and help: CDC, Heat Related Illnesses poster.
  https://www.cdc.gov/extreme-heat/media/pdf/Heat_Related_Illness.pdf
  UI says "sign"; the number is not presented as a standalone diagnosis. Forty degrees is the model stop limit.
- Negative feedback, hypothalamic sensor, evaporation, humidity, skin blood flow, shivering as heat production:
  OpenStax Anatomy and Physiology 2e 24.6, Energy and Heat Balance, checked live.
  https://openstax.org/books/anatomy-and-physiology-2e/pages/24-6-energy-and-heat-balance
- Fever's raised target: the specified OpenStax section does not directly cover this. Cross-checked the same teaching
  claim with NCBI Bookshelf, StatPearls, Physiology, Fever: https://www.ncbi.nlm.nih.gov/books/NBK562334/
- Sixty kg, watts, capacity, gains, limits, clothing, wind, and all trial numbers are explicitly model assumptions/outputs.
  ASHRAE was retrieved, with the numerical differences above: https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch09/F21_Ch09_si.aspx
  The exact exercise heat fraction is not
  supported by the specified OpenStax section. The 2024 Compendium is an adult reference, not teen calibration.
  These are reported provenance limitations; no exact percent or MET claim is taught on screen.
- The three thermostat parts and omitted losses are the simplified model described in the spec.

#### Break it

- No score, badge, saved best, quiz verdict or reflection gate exists. Sweeping sliders earns nothing.
- Compared zero and one row: refused. Two identical rows: explicitly labeled identical, without a causal conclusion.
- Changed multiple variables: comparison says how many changed and asks for one. This prevents a fake controlled-pair claim.
- Edited conditions after trial: old data unchanged. No later sample is invented beyond a safety stop.
- Rapidly started 23 trials, including 20 at 17 ms intervals: found an animation timestamp race and fixed it by clamping
  reveal and sample index. Repeat stress passed. Interrupted rows remain complete and independently selectable.
- Cold stop: attempted Play and changed air, then advanced: stayed locked at 35 until Reset. Reset restored 37 and time zero.
- Fever Reset at a 40 target is the spec's reset/safety corner case. It now locks immediately and directs lowering the target before Reset.
- Re-tapping the active mode cannot reset away a lock; actual mode changes reset the clock as the spec explicitly requires.
- Real drag to 45°C at 5 min/s, then changed clothes: background and rates changed; core did not jump at the edit.
- Five trials at 2.1 s gaps: five completion events started. Earlier version dropped the first behind teaching speech;
  completion now takes priority. How lines remain once per page load; pending Compare guidance retries until heard or used.

#### Voice walk

Held 120 ms clicks, main-path actions about 2 s apart. Chrome was muted. Evidence is queue-start logs, not an audio-quality review.
Lab main/side path: welcomeLab, sweatOn, humidHint; humidHint started once and the park backdrop was active.
Experiment: welcomeExp, sweatOn, trialDone, trialDone. Compare guidance correctly became stale when Compare was already used.
Five-trial side path: welcomeExp, five trialDone events, then compareHow. No repeated spoken how line.
Fever: welcomeFever, chills, shiverOn; dropping the target at a warmed core started breaks and immediately showed sweating/flushing.
State validity prevents repeated Fever starts from claiming a normal core when warm, and Fever breaks from claiming cooling at a still-normal core.
Welcome cuts after action are allowed by BASELINE 16. Fast trial results can cut response narration; the response remains visible in the figure/tip.
All 21 fixed lines are in voice/lines.json. Recordings are absent by build instruction; browser voice is the fallback.

#### Feel check

Best moment: T1 bends toward 37.44 while the dotted T2 keeps climbing toward 38.39 when sweating is removed.
The model produces this separation from the same rule, rather than a scripted win animation.
Flattest moment 1: resting balance is a flat trace. Activity now answers immediately in the heat gauge and net-heat box,
and the first running seconds visibly warm the body and bring up sweat beads.
Flattest moment 2: the trial notebook originally exposed too little of a paired result. Expanded it so both rows stay visible
at the compact size, and enlarged the experiment plot while preserving the transport controls.
The phone originally put scrolling details before the art. Details now follow the scene; controls, thermal view and graph fit the first screen.
Compared the tool against freshly bundled Scratch copies of Beat Lab and Snowy Mail Route. See the side-by-side frame `_scratch/body-thermostat/feel-comparison.jpg`.
The tool has a distinct rose thermal-instrument identity, rich painted depth and an earned student-specific evidence table.

#### Done when

1. PASS: A holds 37.00 for the hour; B 37.44342 at 30 min, independently checked.
2. PASS: E crosses 38.5 at 30.4833; steamy park and one humidHint start verified in the browser side path.
3. PASS: I 20.4333 min, J 12.7167; I calm pause and locked Play verified through the browser.
4. PASS: B/C rows and overlay verified with held clicks; C 38.38598 rounds to 38.39.
5. PASS: Fever at 22°C immediately shivers/tightens, chills starts, K gives 38.29295 at 30 min.
6. PASS: mode-specific figure/graph/loop layouts; Fever Compare moved toward the stage center.
7. PASS: live real drag and clothes edit; rapid trials interrupt without losing rows or mutating live time.
8. PASS: native sliders/buttons, pressed states, visible focus; keyboard-only entry and complete trial verified.
9. PASS: primary controls and hint fit 1366x768, 1000x625, 680x425; phone iframe is truly 375 wide.
10. PASS with limitation: five completion starts and at most one start per how line. Fast results can cut earlier speech;
    stale Compare guidance is intentionally skipped after the student has already used Compare.
11. PASS: all eight painted assets load, no src.html em dashes or network resources; safety wording calm and CDC-attributed.

#### Wave lessons

- PASS: Hint/voice: state-owned hint changes synchronously; Read uses it. Queue uses V.heard and contextual validity.
- PASS: Focus/layout: stable controls and notebook pick buttons, no focus on load, reserved hint height, focus before notebook history.
- PASS: Sizes: all standard widths/heights inspected; 44 px native controls, phone layout and compact paired notebook checked.
- PASS: No giveaways: no hidden-answer puzzle. Identical and confounded comparisons cannot masquerade as a controlled result.
- PASS: Honest numbers: model label, mass, capacity and limitations visible; negative skin heat flow explicitly says gained.
- PASS: Standards: students actually manipulate a response, hold conditions fixed and overlay their own evidence for HS-LS1-3.
- PASS: Motion off: scan, arrows, shiver lines and wind stop; physical clock speed is retained. Zero infinite running animations measured.
- PASS: Short choice sets: all weather, clothing, activity and response choices remain visible. History is a scrollable evidence table.
- PASS: Resize mid-animation: model and reveal live outside graph geometry; audit checks the resizing path.
- PASS: Welcome timing: no welcomeAfter; action wins and the premise remains in hint/Read.
- PASS: Unknowns: stop rows show "stopped" after the boundary, not extrapolated invented measurements.
- PASS: One meaning: solid trial 1, dotted trial 2 and thin dashed target distinguish traces without color.
- PASS: Truthful badges: no success badges; all gauges come from rates at the displayed sample.
- PASS: Reversible hints: mode/reset/run/compare/set-point actions replace the hint immediately.
- PASS: No word-copy solution: no answer cards or matching quiz.

#### Audit leads

Audit completed once, with 59 saved leads. The audited bundle preceded the small fixes below; it was not audited again.

- 4 small-target leads for Lab: fixed with a 44 px minimum width for segmented buttons; final compact and phone checks verify targets.
- 3 arrow/text-overlap leads: fixed compact/mobile arrow size, line height and vertical gap positioning.
- 9 heading/tick-overlap leads: moved graph heading clear of the left tick column.
- 2 tiny Off-label leads: set the notebook's small text to an explicit 10 px minimum.
- 30 tick-hidden-under-SVG leads: false positives confirmed in every frame. Tick text is painted inside its own SVG;
  the SVG bounding rectangle is not an opaque overlay obscuring its descendants.
- 2 phone iframe/no-hint leads: audit could not obtain its iframe context. Separate real 375 px drive.py host frames and
  DOM measurements verify the hint, primary controls and graph. Read is wired to that hint through Curio.voice.
- 1 dropped Compare-how lead: student had already pressed Compare before the queue reached it; valid intentionally rejects stale guidance.
  A separate five-trial walk heard compareHow after the final completion line when Compare had not yet been used.
- 1 skipped-Play-welcome lead: permitted by BASELINE 16 and the spec's stale-on-Play welcome. Hint and Read retain the instructions.
- 3 no-change leads: Reset in already-reset Experiment/Fever and Clear notebook when empty are valid idempotent actions.
- 4 welcome-cut leads: three active-tab repeats now preserve state/voice rather than resetting. Reset deliberately hushes speech;
  its premise remains in hint/Read, as permitted by BASELINE 16.

All control-walk error columns were empty and all settled Enter-twice paths were OK. Five-click checks were clean.
Motion-off and the complete resize-stress stages found no infinite running animation, exceptions or stuck controls.
The audit's air-extreme states initially used the drive.py expression form, while audit_tool.py expects a function body.
Corrected audit-states.json for future reviews. Separate real drags to both slider endpoints provide the build evidence.

#### Frames looked at

Both bar-tool frames, all eight art assets on art-sheet.png, first desktop/compact/Lab/Experiment/Fever frames,
all twelve size/extreme/grayscale frames on size-frames-sheet-0/1.jpg, and all held-input paths on play-frames sheets.
Individual full frames inspected for compact pair, full pair, phone, cold safety and Motion off.
All 32 audit PNGs inspected on audit-sheet-0 through 3; individual Fever and paired compact frames also opened.
Final seven focused frames inspected after fixes, including phone, the 40°C reset boundary and real cold drag.
A final phone-only retake confirms the full Experiment label fits after widening its button.
Final focused drive batch: zero console errors, warnings or exceptions. feel-comparison.jpg places the final desktop beside Beat Lab.

#### Art made

Eight images, 443.5 KB of final WebP. No redraws were needed after inspecting all subjects and cutouts.
The two generated sheets were cropped into eight raw PNGs. Only art.py --rekey processed them.
Final bundle 704.6 KB; recorded voice 0 KB. Both are comfortably inside the 2 MB goal.
Prompts, house style, drawn_by=codex and people=false are in art/prompts.json. Images are embedded, with no external media.

#### Art still to paint

None. The thermal silhouette intentionally stays in code. No generated asset contains a person.

#### Engine changes wanted

None.

#### Left open

Fixed voice recordings and the fresh bodies/safety sensitivity review remain for the subsequent review/media workflow.
The ASHRAE attribution differs from the written model; exercise heat watts are transparent model assumptions.
Optional suggested-trial buttons were omitted. No claim of a calibrated model for any individual teen is made.
Audit completed once; its 59 pre-fix leads are answered above. The audit iframe-context limitation was covered by a separate 375 px host run.
The full size/state audit was not repeated after the small fixes; only touched views and the reset edge case were re-shot.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: body-thermostat


#### Played

Played all three modes as a grade 9 student before reading the builder's report, handoff, notes or source. Strong thermal scene; comparing my own curves was the best moment. Also checked projector readability.

#### Findings fixed

- Blocker, general, Experiment: all responses off could say Balanced at 40 C while heat accumulated. Balanced now requires net heat near zero; otherwise it says No response active.
- Should fix, general, Experiment: Run trial left a hidden live clock advancing behind recorded evidence. It now pauses that clock without changing its temperature or elapsed time.
- Should fix, general, safety: stopped trials lacked the calm medical context; comparing a normal first row could hide a stopped second row. Both paths now show the stopped trial's warning.
- Should fix, general, safety: separated model limits from diagnosis, labeled the fever number as screening, and made CDC urgency explicit: suspected heat stroke requires emergency care and cooling; hypothermia needs urgent medical help.
- Should fix, general, Fever: live edits, remembered targets and Reset could leave an inappropriate fixed hint; a running clock was told to press Play. Hints now track target/running/locked state; retargeting stops stale speech.
- Should fix, general, Experiment: the off/on recipe assumed a response was on. Its on-or-off wording also fits an all-off return state, with the same controlled-pair task.
- Should fix, general, 375 px Experiment: the fourth loop box was clipped and Compare was below the first screen. All four boxes fit; the notebook toolbar precedes the strip and graph on phones.
- Polish, general, comparison: the flat overlay now gives the measured temperature difference at the last time BOTH trials reached, with a once-per-load spoken guide to reading solid/dotted traces.
- Polish, general, graphics: lifted the weaker code-drawn loop panels with directional highlights, inset shading, depth and small hardware details. Kept the rich paintings and live thermal colors.
- Polish, general, provenance: removed an outdated OpenStax license claim from source credits; documented current Compendium discrepancies without silently changing the prescribed model.

#### Findings left

No known product blocker or should-fix remains. Recorded soft-breath clips are still absent; the supported browser-speech fallback was exercised, not an audio-quality review.
Nit: the notebook's additional numeric columns scroll horizontally in compact views. This is evidence history, not a hidden set of choices.

#### Break it

- Scores, saved bests, quizzes and reflection gates: none exist. Sweeping settings earns no badge or claim of mastery.
- Compare with zero/one row: refused. Two identical trials: explicitly identified as identical. Three changed variables: explicitly identified as a confounded comparison.
- All response switches off during a hot run: reaches the real computed stop, never a false Balanced label. Replayed after the fix.
- Hot/cold trials: stop at 980/1226 simulated seconds; no later measurements are invented. Warning appears at the revealed boundary, including a stopped second comparison row.
- Trial while live: now freezes the separate live clock; trial snapshots remain unchanged after control edits. The hint identifies the controls as settings for the next trial.
- Cold lock: Play, an activity edit, an active-mode tap and another advance cannot move beyond 35 C. Reset is required. Fever Reset at a 40 C target stays locked and explains lowering the target first.
- Rapid trials, Compare, Clear notebook, then another trial: no exception, lost row or disabled control. Interrupted reveals retain the computed evidence.
- Comparison delta uses the shared endpoint, including an early stop; it never compares an extrapolated 60-minute value with a stopped trial.
Evidence: review-cheats.json, review-recheck-frames, review-final-frames and the saved cheap-*.json results in Scratch.

#### Voice walk

Held 120 ms clicks, about 2 seconds apart, Sound on. Followed welcome instructions: change activity/clothes, Play; enter Experiment, switch sweating off, run, switch it on, run, Compare; restore rest/indoor conditions, enter Fever, Fever starts, Play, Fever breaks.
Actual starts in the last replay: welcomeLab, welcomeExp, trialDone, trialDone, compareRead, welcomeFever, chills, breaks, sweatOn. Each mode how-to started once. Welcomes cut by actions remain available through the hint and Read.
Persistent side paths also heard shiverOn, vesselsTight and sweatOn. compareHow becomes stale once Compare is used; the immediate compareRead line takes over. BASELINE 16 permits first-action welcome cuts.
| Line | Kind | Expected | Heard |
| --- | --- | --- | --- |
| welcomeLab / welcomeExp / welcomeFever | how-to | once each | once each |
| trialDone, five trials at 2.2 s gaps | event | 5 | 5 |
| compareHow, five-trial side path | how-to | 1 | 1 |
| humidHint, default-speed humid jog | how-to | 1 | 1 |
| compareRead, comparison path | how-to | 1 | 1 |
Read interrupts speech and reads the current hint with Sound off; switching mode releases Read. Retargeting drops obsolete chills. Fixed text matches voice/lines.json exactly: 24 lines.

#### Facts checked

- Average normal about 37 C / 98.6 F and variation: [NIH MedlinePlus, Body temperature norms](https://medlineplus.gov/ency/article/001982.htm).
- Fever screening threshold 38 C / 100.4 F: [CDC Port Health, Definitions of Signs, Symptoms, and Conditions of Ill Travelers](https://www.cdc.gov/port-health/php/definitions-symptoms-reportable-illness/). Measurement and context still matter.
- Hypothermia below 35 C / 95 F; warmth, dryness and urgent medical attention: [CDC, Preventing Hypothermia](https://www.cdc.gov/winter-weather/prevention/index.html).
- 103 F, about 39.4 C, as ONE heat stroke sign: [CDC, Heat-related Illnesses poster](https://www.cdc.gov/extreme-heat/media/pdf/Heat_Related_Illness.pdf). Emergency help, cooling and possible sweating: [CDC/NIOSH, Heat-related Illnesses](https://www.cdc.gov/niosh/heat-stress/about/illnesses.html).
- Negative feedback, hypothalamic control, sweating/evaporation, humidity and shivering: [OpenStax A&P 2e, 24.6](https://openstax.org/books/anatomy-and-physiology-2e/pages/24-6-energy-and-heat-balance). Skin blood flow and vasoconstriction also checked against [ASHRAE F21, chapter 9](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch09/F21_Ch09_si.aspx).
- Fever's raised target: [StatPearls, Physiology, Fever, PubMed record](https://pubmed.ncbi.nlm.nih.gov/32966005/). Chills: [Clinical Methods, Fever, Chills, and Night Sweats](https://pubmed.ncbi.nlm.nih.gov/21250166/). The specified OpenStax section alone does not support the raised-target claim.
- Heat capacity: model 60 x 3470 = 208,200 J/C. ASHRAE gives 3490 J/(kg K), not 3470. Evaporation: ASHRAE rounds to 2.43 MJ/kg; spec uses 2.426. At 600 W the latter gives 0.890 L/hour. These remain explicitly labeled model constants.
- MET conversion: 60 x 4184 / 3600 = 69.733 W per MET; [Adult Compendium](https://pacompendium.com/) defines 1 kcal/kg/hour. Its [current running table](https://pacompendium.com/running/) lists general jogging 7.5 MET and running 6-6.3 mph 9.3, versus the spec's 7/9.8. The prescribed watts and 80 percent exercise heat factor remain model assumptions, not measured teen physiology.
- Independent Python plus extracted-source Node check reproduced A-L and four extremes. A stays 37.00000; B at 30 min 37.44342; C at 60 min 38.38598; E crosses 38.5 at 30.4833 min; I/J stop at 20.4333/12.7167 min; K at 30 min 38.29295.
- Response gains, clothes/wind factors, one-second Euler steps, model omissions and stop limits are the spec's simplifying assumptions. Model time is expressly not a safe exposure time. Sources checked live 2026-11-08.

#### Sensitivity

Bodies, fever and heat/cold illness require the next sensitivity lens to check neutral wording, urgency, and the distinction between model settings and real bodies. Sixty kg is a model parameter, not an ideal body. The faceless thermal figure represents data; no painted asset depicts a person. No physical heat/cold experiment is proposed.

#### Flattest moment left

Rest at 22 C is intentionally quiet and flat. The first activity change immediately changes heat made/net heat; Play reveals the response. Optional suggested-trial buttons remain omitted as the spec allows.

#### Graphics

Inspected all eight coherent paintings, including clothes at 28/56 px and scene-sized backdrops. No missing art tokens or people-marking errors. No painted image needed replacement; the weaker loop artwork was lifted in code.
Final bundle 708.5 KiB; eight WebP assets 443.5 KiB; no fixed voice audio. Preserved rose/thermal identity and painted depth. Compared a current frame with the existing Beat Lab bundle in review-bar-comparison.jpg.
Recomputed contrast ratios: rose/panel 4.94, rose/section 4.68, dark ink/rose 5.19, hot/stage 8.91, cold/stage 8.76; all exceed 4.5:1.

#### Audit

Completed once within the 40-minute limit: `_scratch/body-thermostat/review-audit/audit.md`. All 39 audit frames inspected. No console errors, lost settled focus, stuck controls, or infinite Motion-off animation; repeat-input and resize checks completed.
All 56 leads resolved: 36 SVG ticks visibly readable beneath their own SVG container; 14 intentional safety overlays over the stopped miniature scene; 3 idempotent Reset/Clear actions; 2 permitted Play/Reset welcome interruptions; 1 voice timing-window lead.
The voice lead is not lost: the focused quiet walk heard vesselsTight at 22.239 s, after trialDone, trialCold and shiverOn, with an empty final queue. The audit's quiet wait is capped at 15 s.
The single audit preceded narrow remembered-target, screening-label and on-or-off recipe refinements. Rechecked their compact/desktop/375 px frames and the full main voice path; no second audit. Latest focused batches: zero console errors, warnings or exceptions.
Every BUILD wave lesson was checked: honest/unknown values, no giveaways, stable controls/focus, all sizes, state-owned hints/Read, once-only how lines, repeated result events, Motion off, and resize during action. All three native response switches passed the audit's Enter-key checks.
Cleanup verified Chrome ports 9940-9947 and host 8745 closed; host.html absent. Notes retain the required three opening sections. Scope and no-commit rules held.

#### Left open

The spec's ASHRAE/MET attributions differ from current sources; changing the prescribed numerical model would change its worked cases. Kept it, documented the discrepancy, and made no teen-calibration claim.
Unattended choices followed the brief: retained the data-driven silhouette and existing art, kept notebook data page-only, added no topics or scores, and did not record audio. Clinical urgency was corrected to named CDC guidance.
No commits or shared-kit changes. Writes stayed in tools/body-thermostat and _scratch/body-thermostat. Initial document reads lacked a hard kill timer and completed immediately; subsequent commands used explicit subprocess limits.
Final report is written only at completion to honor the user's stop-on-write instruction; this working draft and audit evidence were saved in Scratch as work progressed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Body Thermostat handoff

#### Structure

src.html starts from the kit starter, uses curio, theme-912 and Plane. CSS lays out an outdoor thermal instrument,
with separate Lab, Experiment and Fever emphases. The single rates function feeds one-second Euler integration,
the body colors, sweat beads, insulation band, vessel state, gauges and notebook trials. Trial snapshots are copied
before integration; they never mutate the live clock. ResizeObserver rebuilds the Plane at real pixel dimensions.
The trial animation is a reveal of completed evidence. New trials and Compare interrupt it without losing a row.
The notebook persists only in memory. No score, grading, accuracy badges or saves exist.

#### Decisions and open questions

- Safety copy follows CDC urgency: suspected heat stroke needs emergency care (911) and cooling; hypothermia needs urgent medical help.
  The model stop is explicitly separated from a diagnosis.
- Kept the code-drawn, faceless thermal silhouette because its colors and effects are live model data.
- Used the requested image tool rather than the spec's older local-FLUX route. Art was made in two four-panel sheets,
  cropped to individual raw PNGs, then processed only with art.py --rekey. All eight prompts and provenance are in art/prompts.json.
- Fever has its specified target and clock controls. It holds Lab's environment; return to Lab to edit those conditions.
- Reset in Fever follows the spec's detailed reset rule: after Fever starts, Reset sets core to the current fever target.
  Mode changes always reset core to 37; they remember Fever's target, settings and the page notebook.
- The overview says Reset returns to 37, while the detailed rule allows the current fever target. That includes 40°C,
  which is also the safety boundary. The detailed reset wins; at 40°C it immediately safety-locks. The hint says to lower
  Set point before Reset so this cannot bypass the boundary.
- The spec says shivering starts 0.2°C below target "after vessels have tightened". The formula, rather than a separate delay,
  determines timing. The whole loop uses its written formula without new physiological mechanisms.
- On a phone, controls precede the scene. Experiment puts the notebook toolbar above the thermal strip and graph so Compare stays in view.
  Evidence rows and details can scroll. Short landscape keeps controls and scene side by side.
- The spec's exact exercise heat percentage is not supported by its cited OpenStax section. Activity watts remain labeled model values.
- Live source verification found ASHRAE F21 SI chapter 9 uses 3490 J/(kg K), not the spec's 3470, and rounds evaporation
  heat to 2.43 million J/kg rather than 2.426 million. Kept the explicitly labeled model constants and worked-case behavior;
  flagged the attribution mismatch instead of silently changing the specified model.
- Heat stroke temperature is worded as a "sign", not a standalone diagnosis. The model's 40°C stop remains as specified.
- OpenStax 24.6 covers the feedback responses, but does not directly cover fever's raised target. A source cross-check
  for that already-specified teaching claim is NCBI Bookshelf, StatPearls, Physiology, Fever (NBK562334).
- Chills and fever-break speech have state validity checks: repeated taps cannot claim a normal core when it is already warm,
  or claim sweating when the core is still at 37°C. The hint always gives the next action.
- Optional Suggested trials list omitted. The teacher start gives one controlled pair without introducing a new feature.
- Trial reveals are instant with Motion off, following the spec's explicit trial instruction; the live physical clock keeps its chosen speed.

#### Sensitivity

This tool discusses people's bodies, fever, heat illness and cold exposure. A fresh reviewer should check the calm
safety copy, threshold context, and absence of body-size or fitness judgments. The 60 kg mass is a model assumption.
The thermal silhouette is faceless and not a body ideal. No people appear in any generated asset.
The simulation is educational, with deliberately simplified constants; students must not perform the extreme scenarios physically.

#### Engine changes wanted

None. No shared engine files changed.

#### Media readiness

Eight images are painted and placed. Voice text is ready for soft-breath, but the fixed recordings remain for the later media pipeline.

#### Build test cleanup

This machine's LibreOffice Python launcher left host child processes after the parent was closed.
Scratch/close_owned.py matches only body-thermostat with --host 8775, or this tool's exact Chrome profile path.
It closed the five retained host process trees. HTTP then refused the host connection; host.html was removed.

#### Cold review, 2026-11-08

- Run trial pauses the live clock so a hidden simulation cannot raise a safety stop over a trial.
- Trial safety panels appear only when the boundary sample is revealed, with their own recorded-trial wording.
- No response active is distinct from Balanced; balance now requires net heat near zero.
- Set-point hints track the actual target and name Pause while the clock is running.
- Re-entering Fever or resetting at a remembered high target uses that target's hint rather than asking to raise an already high target.
- The CDC fever figure is explicitly a screening threshold; high temperature after exercise does not establish a fever diagnosis.
- Experiment's recipe says on or off so it still fits when the student returns with every response already off.
- Compare gives a shared-time temperature difference and a once-per-load spoken guide to reading the traces.
- CDC-based copy names emergency heat care without diagnosing heat stroke from a number; no physical exposure time is implied.
- Kept the eight coherent paintings and enhanced the weaker loop panels with instrument shading and hardware details.
- Current Compendium jogging/running METs differ from the spec. Kept prescribed watts, documented the discrepancy in notes.
- Chrome uses 9940 to 9947; host uses 8745. Review evidence stays in Scratch.

#### Cold review verification

One complete audit finished within its 40-minute limit. Its 56 leads are classified in codex-review.md.
All 39 audit frames were inspected. Post-audit checks cover the small copy/hint refinements and a fresh main voice walk.
The apparent dropped cold-response line plays at 22.239 seconds; the audit's quiet window is only 15 seconds.
The final 24 fixed lines match voice/lines.json; no recordings were made. Independent cases A-L and four extremes match.
All assigned review Chrome ports and host 8745 are closed; host.html is absent. No shared-engine changes or git commits.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
