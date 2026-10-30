# Body Thermostat

## One idea
Your body holds its core near 37 C by comparing it to a set point and switching on sweating, flushed skin,
tight skin vessels or shivering to close the gap, and you run experiments on that thermostat: push it with a run, a
humid day or a windy winter, switch one response off to see what it was quietly doing, and raise the set point to
see that a fever is the thermostat turned up, not broken.

## Not like
- body-systems-tour (health 9-12): every body system changes pace together on a tour. Here one loop, one number
  (core temperature), and controlled experiments with responses switched on and off.
- feedback-loop-builder (sci 9, earth): you build causal loops for climate. Here the loop is fixed physiology and you
  test it by changing conditions, never by drawing arrows.
- hot-meets-cold (sci 11): objects drift to the same temperature. Here a living body refuses to drift, and you
  see the energy it spends refusing (shivering watts, sweat).
- fitness-program-designer and game-day-fuel (health/PE): training load and food. No plans or meals here.
- energy-accountant (same group): where a cell's energy comes from. Here only the heat that energy leaves behind.

## Who and how
Grade 9, science (Life Science module Homeostasis: "Feedback mechanisms maintain stability"). Driver: students on
laptops. 15 to 30 minutes. Standards: HS-LS1-3 (plan and conduct an investigation to provide evidence that feedback
mechanisms maintain homeostasis).
Topic line: homeostasis and feedback loops.
9-12 dark theme (`kit:curio`, `kit:theme-912`). No confetti, no score. Header: title, `.seg` modes **Lab**,
**Experiment**, **Fever**, kit buttons `motion`, `sound`, `read`.

## Screens and modes
Shared layout: stage left (painted setting with the body figure, the loop diagram, the live graph), panel right
(controls, readouts, `hint`, `tip`). Wide: stage about 62 percent. Under 900 px tall or in the 16:10 preview: graph
shrinks to 140 px, panel controls first, the four response gauges become one row.

The **setting** is a painted backdrop chosen by the air (Art): snowy field below 10 C, school track 10 to 29 C, dry
desert trail at 30 C and up when Dry, steamy summer park at 30 C and up when Humid. It crossfades over 0.5 s when the
band changes (instant with Motion off) and sits under a dark scrim so the figure and numbers stay readable. Wind on
adds code-drawn streaks across it.
The **body figure** stays drawn in code as a thermal-camera style silhouette (no face): its colors are live data, not
decoration. A core dot shifts from blue to red with core temperature, the skin tints with blood flow (darker rim when
vessels are tight, warmer fill when flushed), sweat beads appear (count follows sweat watts), and small shake lines
show shivering. The chosen clothes show as an insulation band whose thickness follows the clothes factor, with the
painted clothes icon (Art) as a badge beside the figure. Beside it the **loop diagram**: four boxes in a ring, Sensor
(brain's temperature center), Compare (set point), Responses, Body heat, with arrows that pulse when a response is
working. Under both, the **graph**: core temperature (C) against minutes, last 60 minutes, with the set point as a
dashed accent line and a 35 to 40 C band.

**Lab** (explore, opens first). Focus: the body figure and its core dot, with the live graph right under it; they are
the largest thing on the stage. Controls:
- **Air** slider minus 10 to 45 C (step 1), default 22.
- **Air feels** `.seg` **Dry** / **Humid**.
- **Wind** toggle (off by default).
- **Clothes** `.seg` **Swimsuit**, **Shorts**, **Indoor clothes**, **Winter coat** (each with its painted icon).
- **Activity** `.seg` **Rest**, **Walk**, **Jog**, **Run**.
- **Play** / **Pause**, **Speed** `.seg` **1 min/s**, **5 min/s**, **Reset** (core back to 37.0, clock to 0).
- Readouts (`dl.readouts`): Core temperature (2 decimals), Set point, Heat made (W), Heat lost through skin (W, minus
  means gained), Sweat cooling (W), Shivering (W), Skin vessels ("tight 0.5x" to "wide 3.0x").
Every change applies at once while the clock runs: the next simulated second uses it and the figure, backdrop and
readouts redraw on that frame. The clock runs until paused (an hour takes 60 s at 1 min/s, 12 s at 5 min/s); it is a
live simulation the student steers, not an auto-play, so it may run past 30 s.

**Experiment** (the investigation). Focus: the Lab notebook and the Compare overlay. The graph widens to the full
stage width and grows to about half the stage height; the body figure and loop diagram shrink to a strip above it.
Same controls, plus a row of three response switches, **Sweating**, **Skin vessels**, **Shivering** (all on), and a
**Lab notebook** table: **Run trial** plays 60 simulated minutes from 37.0 C with the current settings and adds a row:
trial number, conditions, responses off, core at 10, 30 and 60 minutes, highest and lowest core. **Compare** picks two
rows and overlays their curves. **Clear notebook**. Notebook lives only in the page (gone on reload). A **Suggested
trials** list (optional) offers three pairs: run with and without sweating; humid versus dry jog at 35 C; windy minus
10 C in a swimsuit with and without shivering.

**Fever** (the set point moves). Focus: the loop diagram's Compare box ("core 1.5 C below set point") and the graph's
dashed set point line; the loop diagram moves to the center of the stage and grows, the body figure sits to its left.
**Set point** slider 37.0 to 40.0 (step 0.1) and buttons **Fever starts** (sets 38.5) and **Fever breaks** (back to
37.0). The clock runs as in Lab (Play, Pause, Speed, Reset). With the body at 37.0 and the set point at 38.5 the body
shivers and tightens its vessels in a warm room: the hint explains this is the chills. When the set point drops back,
the body sweats and flushes while still above 37.

## Content
Model (one source of truth; all values are model values, rounded from the sources, labeled "model" in the tool):
- Body: 60 kg, heat capacity C = 60 x 3470 = 208,200 J per C.
- Heat made M (W): Rest 70, Walk 195, Jog 391, Run 547. From METs for a 60 kg teen (1 MET about 69.8 W): rest 1,
  walk 3.5, jog 7, run 9.8 METs, and about 80 percent of exercise energy ending as heat (rest counted whole).
- Skin heat flow Q = G (core minus air), G = G0 x clothes x vessels x wind, G0 = 70/15 = 4.667 W per C (so a resting
  body in indoor clothes at 22 C loses exactly the 70 W it makes). Clothes: Swimsuit 2.8, Shorts 2.2, Indoor 1.0,
  Winter coat 0.35. Wind on: x2.
- Error e = core minus set point.
- Skin vessels v = clamp(1 + 3e, 0.5, 3.0) (switched off: v = 1).
- Sweat cooling E = min(Emax, 400 x max(0, e)) W; Emax 600 W dry (about 0.9 L of sweat evaporated per hour, at
  2,426 kJ per kg), 150 W humid. Switched off: 0.
- Shivering S = min(250, 300 x max(0, -e - 0.2)) W: shivering starts only 0.2 C below the set point, after the
  vessels have tightened. Switched off: 0.
- Step: every simulated second, core += (M + S - Q - E) / C. (Euler, dt = 1 s.)
Model limits shown on screen in Lab: "This model leaves out breathing losses, sunshine, hands and feet, and water
lost from the body. Real bodies differ."

Real thresholds on screen (all cited): normal about 37 C (98.6 F) on average; fever 38 C (100.4 F) or higher;
hypothermia below 35 C (95 F); heat stroke 39.4 C (103 F) or higher.

Safety pauses: if core reaches 40.0 the clock stops with "Heat stroke range in real life. Stop, cool down, get
help: tell an adult, call for help. Press Reset to start again." If core falls to 35.0: "Hypothermia range in real
life. Get warm and dry, get help. Press Reset to start again." Both link nowhere; they cite CDC in the tooltip. Calm
wording, no alarms. After a pause, Play is disabled (with the reason "Press Reset first") until Reset.

Hint texts:
- Lab: "<b>Lab.</b> Change the air, clothes or activity, then press Play. Watch which response switches on."
- Experiment: "<b>Experiment.</b> Switch one response off, press Run trial, then switch it back on and press Run
  trial again. Then press Compare."
- Fever: "<b>Fever.</b> Press Fever starts, then Play. The body is not too cold, but the set point says it is."
Tips (rotate): "Sweat only cools when it evaporates. Humid air slows that down." / "Tight skin vessels keep warm
blood in the core, so the skin gets cold first." / "A thermostat needs three parts: a sensor, a set point, a switch."
/ "Shivering is muscles working only to make heat."

Worked cases (60 simulated minutes from 37.00, responses on unless named; core at 10, 30, 60 min):
- A Rest, indoor, 22 C, dry: 37.00, 37.00, 37.00.
- B Run, shorts, 22 C, dry: 37.41, 37.44, 37.44 (sweat 177 W, vessels 2.33x at the end).
- C Same as B, sweating off: 37.61, 37.97, 38.39.
- D Jog, shorts, 35 C, dry: 37.57, 37.75, 37.76. E Same, humid: 37.64, 38.48, 39.50 (passes 38.5 at minute 30.5).
- F Rest, shorts, 40 C, dry: 37.19, 37.29, 37.31 (skin gains 53 W from the air; sweat 123 W).
- G Rest, winter coat, minus 10 C: 36.99, 36.97, 36.97.
- H Rest, shorts, minus 10 C: 36.54, 36.29, 36.25 (shivering 166 W).
- I Rest, swimsuit, minus 10 C, wind: 35.82 at 10 minutes; reaches 35.0 at minute 20.4 (safety pause there; the trial
  row records "stopped at minute 20.4").
- J Same as I, shivering off: 35.41 at 10 minutes; reaches 35.0 at minute 12.7.
- K Fever, set point 38.5, rest indoor 22 C: 37.76, 38.29, 38.45. L Fever breaks (start 38.5, set point 37.0):
  37.27, 37.01, 37.00.
Worst cases (checked): Run, swimsuit, 45 C, humid reaches 40.0 at minute 16.3 (heat pause); Run, winter coat, 45 C,
humid at minute 24.0; Run, swimsuit, minus 10 C, wind holds 36.60 (no pause); set point 40.0 at rest indoors climbs to
39.87 at 60 minutes and never reaches the 40.0 pause.

## Interactions in detail
- Play advances the clock at the chosen speed; the graph scrolls after 60 minutes. Pause holds. Reset returns
  core to 37.0 (or to the set point in Fever when Fever starts was pressed before Reset) and clears the graph.
- Run trial (Experiment) computes the whole hour at once, then draws the curve over 2 s (instant with Motion off).
  While it draws, every control stays live: a new Run trial or Compare stops the drawing, finishes the row at once and
  starts the new action. It never touches the Lab clock.
- Safety pause: in Lab and Fever the clock stops at 40.0 or 35.0; in a trial the row stops there and records
  "stopped at minute 20.4".
- Changing a setting mid-run changes the next step only; no jumps in core temperature.
- All sliders and `.seg` groups keyboard operable; switches are buttons with `aria-pressed`. Readouts update in an
  `aria-live="polite"` region no more than once per simulated minute.
- Mode change: `V.hush()`, keep settings, reset the clock. Fever's set point stays when leaving and returning.
- Sound starts on (kit). A soft tick when a response switches on (first time per run), silent with Sound off.

## Look
Accent `--brand #e25a7e` (warm rose, the flushed-skin color), `--brand-ink #10161f`. Stage `#0e1418`; the painted
backdrop sits under a `#0e1418` scrim at 70 percent so every contrast below holds over it. Hot side of the core dot
and graph above set point `#ff9a6b`, cold side `#6ab8ff`; band 35 to 40 C as a faint fill.
Contrast (computed): brand on --panel 4.94:1, on --sec-bg 4.68:1, on the stage 5.37:1 or more; brand-ink on brand
5.19:1; hot #ff9a6b on stage 8.91:1, cold #6ab8ff on stage 8.76:1; ink on stage 15.76:1. Never color alone: the core
dot carries its number, gauges carry words ("tight", "wide"). Nearest 9-12 accents #ff8ab6, #ff4d6d, #ff8f9e (all
dE about 19), and the group's other accents are 30 or more away.

## Art
Local FLUX (`scripts/localart.py`), no people. 8 images. House style: soft painterly outdoor scenes, natural light,
calm, empty of people and animals, no lettering.
- bt-scene-cold: a wide treeless snowy prairie in winter with a wooden fence line, drifts blown into ridges, a low
  gray sky and a trampled snow path across the foreground; 16:9; cutout no; people no; backdrop when the air is below
  10 C.
- bt-scene-mild: a school running track curving past a grassy field and leafy trees on a mild spring day, soft
  daylight; 16:9; cutout no; people no; backdrop from 10 to 29 C.
- bt-scene-hot-dry: a dusty desert trail between red rocks and dry scrub under a hard bright sun and a pale washed-out
  sky; 16:9; cutout no; people no; backdrop at 30 C and up with Dry.
- bt-scene-hot-humid: a steamy green summer park after rain, hazy white sky, a wet shining path between lush trees;
  16:9; cutout no; people no; backdrop at 30 C and up with Humid.
- Clothes kit (one shared prompt: "a single piece of clothing laid flat and neatly folded, seen from above, soft
  studio light", one cutout per piece): bt-clothes-swimsuit (a plain blue one-piece swimsuit), bt-clothes-shorts
  (running shorts with a plain t-shirt), bt-clothes-indoor (blue jeans with a plain gray sweatshirt),
  bt-clothes-coat (a thick puffy winter coat with a hood); 1:1; cutout yes; people no. Sizing: all four drawn at the
  same height, 28 px in the `.seg` buttons and 56 px as the badge beside the body figure.
The body figure, loop ring, gauges and graph stay in code: the figure is a thermal-style data display whose colors,
sweat beads and shake lines follow the model every frame.

## Voice
Bank `soft-breath` ("Say softly and calmly, like a mindfulness teacher"): a steady, unhurried body voice, unlike any
9-12 science neighbor. Uses `Curio.voice`, scope = mode. How lines speak once per page load, then only update the
hint; event lines speak each time.
- welcomeLab (how; on entering Lab; stale once Play has been pressed): "Welcome to Body Thermostat. Change the air,
  clothes or activity, then press Play and watch the core temperature hold."
- welcomeExp (how; on entering Experiment; stale once a trial has run): "Experiment. Switch one response off, press
  Run trial, then switch it back on and run it again."
- welcomeFever (how; on entering Fever; stale once Fever starts is pressed): "Fever. Press Fever starts, then Play,
  and watch the body warm itself up to a new set point."
- sweatOn (how; first time sweating starts while the clock or a trial runs; stale when sweat is 0): "Sweating
  switched on. Sweat cools you only as it evaporates."
- shiverOn (how; first time shivering starts; stale when shivering is 0): "Shivering switched on. Muscles are working
  just to make heat."
- vesselsTight (how; first time v drops below 1; stale when v is back to 1 or more): "Skin vessels tightened. Warm
  blood stays in the core."
- humidHint (how; first Humid run with sweat at its 150 W limit; stale if Dry is picked): "The air is humid, so sweat
  can't evaporate fast enough."
- trialDone (event; each finished trial; stale if another trial starts): "Trial added. Now change one thing and press
  Run trial again."
- compareHow (how; the second row lands in the notebook; stale once Compare is used): "Two trials. Press Compare to
  lay their curves on top of each other."
- chills (event; Fever starts; stale on Fever breaks): "Chills. The core is normal, but the set point says it is
  too cold."
- breaks (event; Fever breaks; stale on Fever starts): "Fever breaks. The set point drops, so the body sweats and
  flushes."
- hotPause (event; each 40 C pause; stale on Reset): "Heat stroke range in real life. Stop, cool down, and get help.
  Press Reset to start again."
- coldPause (event; each 35 C pause; stale on Reset): "Hypothermia range in real life. Get warm and dry, and get help.
  Press Reset to start again."

## Family engine
none. Plots with `kit/graphing.js` (`Plane`, `g.fn` style trace drawn from the sample array, dashed set point
via `g.segment`).

## Sources
- Normal temperature about 98.6 F (37 C): NIH MedlinePlus, "Body temperature norms",
  https://medlineplus.gov/ency/article/001982.htm (checked 2026-10-27).
- Fever 100.4 F (38 C) or higher: CDC, "Definitions of Symptoms for Reportable Illnesses",
  https://www.cdc.gov/quarantine/air/reporting-deaths-illness/definitions-symptoms-reportable-illnesses.html
- Hypothermia below 95 F (35 C): CDC, "Preventing Hypothermia", https://www.cdc.gov/winter-weather/
- Heat stroke 103 F (39.4 C) or higher: CDC, "Heat and Health: heat-related illnesses",
  https://www.cdc.gov/heat-health/ (verify confirms the three CDC pages and figures; checked as titles 2026-10-27).
- Thermoregulation, set point, sweating, vasodilation and constriction, shivering, fever as a raised set point:
  OpenStax Anatomy and Physiology 2e, section 24.6 "Energy and Heat Balance" (CC BY 4.0),
  https://openstax.org/books/anatomy-and-physiology-2e/pages/24-6-energy-and-heat-balance
- Body specific heat about 3.47 kJ per kg per C: ASHRAE Handbook Fundamentals (2021), ch. 9 "Thermal Comfort"
  (verify checks the figure; textbooks give 3.47 to 3.5).
- Latent heat of evaporation of sweat about 2,426 kJ per kg at 30 C: ASHRAE Handbook Fundamentals ch. 9.
- METs (rest 1, walking 3.5, jogging 7, running 6 mph 9.8) and 1 MET = 1 kcal per kg per hour: 2024 Adult
  Compendium of Physical Activities, https://pacompendium.com
- Muscle efficiency about 20 to 25 percent (so about 80 percent ends as heat): OpenStax A&P 2e 24.6.
- All loop gains, clothing and wind factors: model values chosen so case A balances exactly; labeled as model.
- Number checks (Python, 2026-10-29, the model above stepped every second): cases A to L reproduce to 0.01 C; case E
  passes 38.5 at minute 30.48; case I reaches 35.0 at minute 20.43, J at 12.72. Fixed: case I's old 30 and 60 minute
  values (34.27, 32.16) could never show, because the safety pause stops the run at 35.0; the case now ends at the
  pause. Worst cases as listed under Content.

## Done when
1. Case A holds 37.00 for 60 minutes; case B reads 37.44 at 30 minutes (within 0.02).
2. Case E (humid jog) passes 38.5 near minute 30.5 over the steamy park backdrop, and the humid line plays once.
3. Case I pauses at 35.0 near minute 20.4 with the calm hypothermia message and Play disabled until Reset; case J
   pauses near 12.7.
4. In Experiment, two trials (B and C) land as rows and Compare overlays them; C ends at 38.39.
5. Fever starts at rest indoor shows shivering in a 22 C room with the chills line; core reads 38.29 at 30 minutes.
6. Focus: in Lab the body figure and graph are the largest thing on the stage; in Experiment the overlay graph is; in
   Fever the loop diagram's Compare box sits centered and reads the gap.
7. A tap while anything plays: moving Air or Clothes while the clock runs at 5 min/s changes the backdrop, figure and
   readouts on the next frame; Run trial pressed while a curve draws starts the new trial at once.
8. Every response switch, slider and `.seg` works by keyboard; no color-only signal.
9. The main controls are visible without scrolling at 1366x768, 1000x625 and 680x425.
10. Five actions in a row speak each how-to line at most once; the trial line speaks every trial; no line names a
    control that is disabled at that moment.
11. The four backdrops and four clothes icons load; no network, no em dashes; every safety message is calm and cites
    CDC.

## Open questions
- [body-thermostat] The safety pauses say "get help" without a phone number (no crisis line applies). Fine?
- [body-thermostat] The body figure stays a code-drawn thermal silhouette because its colors are live data. A painted
  person (Gemini, people: true, your review) per activity would look warmer but cannot tint with blood flow. Keep the
  silhouette?
