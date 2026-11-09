# Codex report: body-thermostat

## Built

Lab, Experiment and Fever, using the written one-second Euler model, Curio.voice, theme-912 and Plane.
Eight generated paintings are embedded. Thermal color, sweat, shivering, insulation and the four response gauges follow model data.
The notebook retains immutable trial conditions, early stops, sampled temperatures, extrema and two selected traces.
All writes stayed in the assigned tool and Scratch folders. No commits, shared-engine changes, audio recording or polish round.
The report was finalized last to honor the user's stop instruction rather than writing the report at the first bundle.
Cleanup caught LibreOffice Python launcher descendants left by parent-only termination. Matched and closed this tool's
five host process trees; HTTP then refused port 8775. Used Chrome/host ports are closed, and host.html is absent.

## Numbers check

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

## Facts checked

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

## Break it

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

## Voice walk

Held 120 ms clicks, main-path actions about 2 s apart. Chrome was muted. Evidence is queue-start logs, not an audio-quality review.
Lab main/side path: welcomeLab, sweatOn, humidHint; humidHint started once and the park backdrop was active.
Experiment: welcomeExp, sweatOn, trialDone, trialDone. Compare guidance correctly became stale when Compare was already used.
Five-trial side path: welcomeExp, five trialDone events, then compareHow. No repeated spoken how line.
Fever: welcomeFever, chills, shiverOn; dropping the target at a warmed core started breaks and immediately showed sweating/flushing.
State validity prevents repeated Fever starts from claiming a normal core when warm, and Fever breaks from claiming cooling at a still-normal core.
Welcome cuts after action are allowed by BASELINE 16. Fast trial results can cut response narration; the response remains visible in the figure/tip.
All 21 fixed lines are in voice/lines.json. Recordings are absent by build instruction; browser voice is the fallback.

## Feel check

Best moment: T1 bends toward 37.44 while the dotted T2 keeps climbing toward 38.39 when sweating is removed.
The model produces this separation from the same rule, rather than a scripted win animation.
Flattest moment 1: resting balance is a flat trace. Activity now answers immediately in the heat gauge and net-heat box,
and the first running seconds visibly warm the body and bring up sweat beads.
Flattest moment 2: the trial notebook originally exposed too little of a paired result. Expanded it so both rows stay visible
at the compact size, and enlarged the experiment plot while preserving the transport controls.
The phone originally put scrolling details before the art. Details now follow the scene; controls, thermal view and graph fit the first screen.
Compared the tool against freshly bundled Scratch copies of Beat Lab and Snowy Mail Route. See the side-by-side frame `_scratch/body-thermostat/feel-comparison.jpg`.
The tool has a distinct rose thermal-instrument identity, rich painted depth and an earned student-specific evidence table.

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

Both bar-tool frames, all eight art assets on art-sheet.png, first desktop/compact/Lab/Experiment/Fever frames,
all twelve size/extreme/grayscale frames on size-frames-sheet-0/1.jpg, and all held-input paths on play-frames sheets.
Individual full frames inspected for compact pair, full pair, phone, cold safety and Motion off.
All 32 audit PNGs inspected on audit-sheet-0 through 3; individual Fever and paired compact frames also opened.
Final seven focused frames inspected after fixes, including phone, the 40°C reset boundary and real cold drag.
A final phone-only retake confirms the full Experiment label fits after widening its button.
Final focused drive batch: zero console errors, warnings or exceptions. feel-comparison.jpg places the final desktop beside Beat Lab.

## Art made

Eight images, 443.5 KB of final WebP. No redraws were needed after inspecting all subjects and cutouts.
The two generated sheets were cropped into eight raw PNGs. Only art.py --rekey processed them.
Final bundle 704.6 KB; recorded voice 0 KB. Both are comfortably inside the 2 MB goal.
Prompts, house style, drawn_by=codex and people=false are in art/prompts.json. Images are embedded, with no external media.

## Art still to paint

None. The thermal silhouette intentionally stays in code. No generated asset contains a person.

## Engine changes wanted

None.

## Left open

Fixed voice recordings and the fresh bodies/safety sensitivity review remain for the subsequent review/media workflow.
The ASHRAE attribution differs from the written model; exercise heat watts are transparent model assumptions.
Optional suggested-trial buttons were omitted. No claim of a calibrated model for any individual teen is made.
Audit completed once; its 59 pre-fix leads are answered above. The audit iframe-context limitation was covered by a separate 375 px host run.
The full size/state audit was not repeated after the small fixes; only touched views and the reset edge case were re-shot.
