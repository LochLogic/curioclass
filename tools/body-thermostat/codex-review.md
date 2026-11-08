# Codex review: body-thermostat


## Played

Played all three modes as a grade 9 student before reading the builder's report, handoff, notes or source. Strong thermal scene; comparing my own curves was the best moment. Also checked projector readability.

## Findings fixed

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

## Findings left

No known product blocker or should-fix remains. Recorded soft-breath clips are still absent; the supported browser-speech fallback was exercised, not an audio-quality review.
Nit: the notebook's additional numeric columns scroll horizontally in compact views. This is evidence history, not a hidden set of choices.

## Break it

- Scores, saved bests, quizzes and reflection gates: none exist. Sweeping settings earns no badge or claim of mastery.
- Compare with zero/one row: refused. Two identical trials: explicitly identified as identical. Three changed variables: explicitly identified as a confounded comparison.
- All response switches off during a hot run: reaches the real computed stop, never a false Balanced label. Replayed after the fix.
- Hot/cold trials: stop at 980/1226 simulated seconds; no later measurements are invented. Warning appears at the revealed boundary, including a stopped second comparison row.
- Trial while live: now freezes the separate live clock; trial snapshots remain unchanged after control edits. The hint identifies the controls as settings for the next trial.
- Cold lock: Play, an activity edit, an active-mode tap and another advance cannot move beyond 35 C. Reset is required. Fever Reset at a 40 C target stays locked and explains lowering the target first.
- Rapid trials, Compare, Clear notebook, then another trial: no exception, lost row or disabled control. Interrupted reveals retain the computed evidence.
- Comparison delta uses the shared endpoint, including an early stop; it never compares an extrapolated 60-minute value with a stopped trial.
Evidence: review-cheats.json, review-recheck-frames, review-final-frames and the saved cheap-*.json results in Scratch.

## Voice walk

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

## Facts checked

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

## Sensitivity

Bodies, fever and heat/cold illness require the next sensitivity lens to check neutral wording, urgency, and the distinction between model settings and real bodies. Sixty kg is a model parameter, not an ideal body. The faceless thermal figure represents data; no painted asset depicts a person. No physical heat/cold experiment is proposed.

## Flattest moment left

Rest at 22 C is intentionally quiet and flat. The first activity change immediately changes heat made/net heat; Play reveals the response. Optional suggested-trial buttons remain omitted as the spec allows.

## Graphics

Inspected all eight coherent paintings, including clothes at 28/56 px and scene-sized backdrops. No missing art tokens or people-marking errors. No painted image needed replacement; the weaker loop artwork was lifted in code.
Final bundle 708.5 KiB; eight WebP assets 443.5 KiB; no fixed voice audio. Preserved rose/thermal identity and painted depth. Compared a current frame with the existing Beat Lab bundle in review-bar-comparison.jpg.
Recomputed contrast ratios: rose/panel 4.94, rose/section 4.68, dark ink/rose 5.19, hot/stage 8.91, cold/stage 8.76; all exceed 4.5:1.

## Audit

Completed once within the 40-minute limit: `_scratch/body-thermostat/review-audit/audit.md`. All 39 audit frames inspected. No console errors, lost settled focus, stuck controls, or infinite Motion-off animation; repeat-input and resize checks completed.
All 56 leads resolved: 36 SVG ticks visibly readable beneath their own SVG container; 14 intentional safety overlays over the stopped miniature scene; 3 idempotent Reset/Clear actions; 2 permitted Play/Reset welcome interruptions; 1 voice timing-window lead.
The voice lead is not lost: the focused quiet walk heard vesselsTight at 22.239 s, after trialDone, trialCold and shiverOn, with an empty final queue. The audit's quiet wait is capped at 15 s.
The single audit preceded narrow remembered-target, screening-label and on-or-off recipe refinements. Rechecked their compact/desktop/375 px frames and the full main voice path; no second audit. Latest focused batches: zero console errors, warnings or exceptions.
Every BUILD wave lesson was checked: honest/unknown values, no giveaways, stable controls/focus, all sizes, state-owned hints/Read, once-only how lines, repeated result events, Motion off, and resize during action. All three native response switches passed the audit's Enter-key checks.
Cleanup verified Chrome ports 9940-9947 and host 8745 closed; host.html absent. Notes retain the required three opening sections. Scope and no-commit rules held.

## Left open

The spec's ASHRAE/MET attributions differ from current sources; changing the prescribed numerical model would change its worked cases. Kept it, documented the discrepancy, and made no teen-calibration claim.
Unattended choices followed the brief: retained the data-driven silhouette and existing art, kept notebook data page-only, added no topics or scores, and did not record audio. Clinical urgency was corrected to named CDC guidance.
No commits or shared-kit changes. Writes stayed in tools/body-thermostat and _scratch/body-thermostat. Initial document reads lacked a hard kill timer and completed immediately; subsequent commands used explicit subprocess limits.
Final report is written only at completion to honor the user's stop-on-write instruction; this working draft and audit evidence were saved in Scratch as work progressed.
