# Polish: first-aid-responder (Codex fix, round 1)

Root: `S:\CurioClass-codex`. Only the tool folder and its scratch folder were written. No commits; refine.md and refine/ untouched.
Evidence below is under `_scratch/first-aid-responder/`: `fix-before/`, `fix-after/`, `fix-voice/`, `fix-audit/` and `fix-exit/`.
Each blocker and should-fix was reproduced with drive.py at 1366x768 before its code changed. Additional sizes are named below.

## Blocker

1. FIXED: Time-based scoring replaces tap percentage. The original five-tap/pause pattern fell from 98.75% at 40/min to 29.09%. A gap clears the needle and rolling window; an 11 s gap cannot save a ghost. Old tap-score ghosts are ignored. Proof: before/after `01-paused-score.png/.json`, after `14-cheats.json`, `16-pause-zero.json`, and voice `main.json` (pauseResult spoken). Two further burst/wait patterns revealed a falsely in-band median needle even though the new scores were low. Repeated outliers now expose the five-interval mean to the gauge and coach; one stray tap retains median smoothing. Before both read 110.092; after they read 73.529 and 163.488. Proof: `fix-before/guard-before.json` and `fix-exit/final-cheats.json`.

## Should fix

2. FIXED: All Don't cards now have a short title and a different body; Heat Call 911 has a body. Duplicate title/body counts fell from 12 Don'ts plus Heat to zero across all decks. Proof: before/after `02-deck-shape-case`, final `15-shape-and-sequences.json`; cheap format filter and brute force below.
3. FIXED: Pause speech requires a running round and a compression; free-practice pauses stay silent and modal dialogs suppress coaching. Before: 4 idle repeats, 2 before the first compression, 2 over Clear. After: zero in the same 31/19/19 s windows. Proof: before/after `11-idle-coach`, `12-no-first-tap-coach`, `13-dialog-coach`; a real running pause speaks once in `fix-voice/main.json`.
4. FIXED: Pointer choices do not move focus to another card. Read prioritizes lastFeedback after every choice, with spoken penalty units. Proof: before/after `05-pointer-feedback-read`; final `read-correct.json` and `read-not-yet.json`. All three read the chosen move's reason; none reads an unrelated card or keyboard instruction.
5. FIXED: Entry, key 2 and Stop send focus to the chest with preventScroll. Space counts on entry; Space after Stop preserves the summary. Proof: before/after `06-entry-space` (0 taps versus counted taps, chest focus), `07-stop-space` (new running round versus stopped summary), `summary-after-mode-return.json` (Space and Enter retain it).
6. FIXED: A finished summary and its trace remain until Start, including reflex taps and mode returns. Before 219 trace points became 1; after they remain 219. Proof: before/after `08-reflex-trace`; `summary-after-mode-return.json`.
7. FIXED: Read uses purpose-built summaryRead and finishRead strings, full action text, spoken units and sentence boundaries. No DOM button labels or plus/slash shorthand. Proof: before/after `09-finish-read.json` and `10-summary-read.json`; e.g. "Average rate 60.0 a minute" and "Longest pause 1.7 seconds".
8. FIXED: The three lower-case action bodies are capitalized on cards, tooltips and Read. Proof: before `02-deck-shape-case.json` reports 3; final `15-shape-and-sequences.json` reports zero in all six scenes. Runtime manifest equality is checked below.
9. FIXED: Sending someone to call 911 shares rank 2 with gloves and explains why help is sent immediately. Before this path made 1 mistake; after 0. Proof: before/after `03-call-before-gloves`, all reverse shared-rank runs in `15-shape-and-sequences.json`. Source: Red Cross bleeding page below.
10. FIXED: Keep the original pad, allow one more, press harder, and do not stack pads. The contrary open notes are removed from notes.md and handoff.md. Proof: final wood-shop deck `rail-1366x768.png`, `finish-scene-2.png`, and Read data in the runtime manifest. Sources: Red Cross bleeding and AHA/Red Cross 2024 below.
11. FIXED: Seizure scene and guide name first seizure, injury, breathing/waking trouble, recurrence and duration; unknown history prompts an immediate call. The first step also sends someone for the nurse while staying. Guide adds CDC's water, pregnancy and diabetes conditions. Proof: before/after `04-seizure-and-heat`, `fix-voice/main-guide-read.png` and `fix-voice/main.json`, `guide-911-680x425.png` (Practice it bottom 394 px). Sources below.
12. FIXED: Every perfect finish includes both Don'ts and their reasons. All six checks return 2 reasons. Proof: `15-shape-and-sequences.json` and `finish-scene-0.png` through `finish-scene-5.png`. Compact finish buttons fit at 680x425 (bottom 388 px), 800x500 (375 px); the 375-wide finish puts them before the longer reading. Frames: `finish-680x425`, `finish-800x500`, `finish-375x812`.
13. FIXED: Before, Heat text was recorded in `fix-before/04-seizure-and-heat.json`; that PNG is the seizure screen, so there is no separate Heat before PNG. Heat now uses neck-down cold-water immersion when available, with cold towels and ice packs as fallback, matching AHA/Red Cross 2024. Proof: inspected `heat-cooling.png/.json`, `finish-scene-4.png`. The existing 2024 guideline source is explicitly applied to this correction in notes.md and handoff.md.
14. FIXED: Metronome defaults on. Strong full rounds suggest a round with it off, in text and speech. The welcome is no longer cut by the first free-practice press. Proof: `06-entry-space.json` metro true; `08-reflex-trace.png` nudge; `voice-entry-and-repeat.json` one uncut wCpr; scheduler 220 clicks in 120 s.

## Polish accepted

15. FIXED: Seizure's fallen-student briefing now pairs with "Move hard or sharp things away", not lowering them again. Proof: `04-seizure-and-heat.png/.json`, `finish-scene-5.png`.
16. FIXED: Early teacher/nurse notification shares rank 2 with cooling and ring removal. The provider check stays last. The accepted change makes the burn rail six slots. Proof: `finish-scene-3.png`, `15-shape-and-sequences.json` (six steps, reverse shared ranks 0 mistakes).
17. FIXED: The heavy-bleeding finish says a trained adult can use a tourniquet on an arm or leg if pressure fails. Proof: inspected `finish-scene-2.png`; AHA/Red Cross 2024 below.
18. FIXED: Both unsupported "explain why" skill claims in notes.md now say "read why". Talk questions still invite explanations. Proof: notes.md first two sections.
19. FIXED: notes.md names witnessed emergencies/death and offers Field guide or rhythm practice. Proof: notes.md, Good to know.
20. FIXED: Trace uses 80 to 140, a taller band, a warning-colored out-of-band line and explicit Too slow/Too fast words. The 1366 trace is 94 px tall; its target band is 25 px rather than about 12 px. Proof: `10-summary-read.png`, `14-cheats.png`, `cpr-slow-1920.png`.
21. FIXED: One bracket spans each desktop rank group. A seven-pixel label shift removes the audit-confirmed compact overlap: 23 by 5 px becomes zero. Final overlap is zero at 680x425, 1366x768, 1920x1080 and 375x812. Phone groups repeat their eligible positions, including the burn group split between rows. Proof: `fix-exit/bracket-*.png/.json` and `bracket-burn-375x812.png`. Corrected bleeding is "2 or 3" and burn is "2 or 3 or 4".
22. FIXED: Ghost is now a labeled moving badge on the active rail, without crowding the heading. First best says "Ghost set: race it next time". Proof: inspected `ghost-step-3.png/.json`, showing Ghost 3 on slot 3 at its stored 6 s stamp; first-best proof `fix-voice/main-scene.png`.
23. FIXED: At 1920x1080 the rail is 167 px tall and deck 535 px, with cards 396 by 262 px and text 20/16 px. Proof: `rail-1920x1080.png/.json`; the same active scene was checked at 1366, all preview sizes, 760 and 375.
24. FIXED: Picker says "Six situations. Beat your own best time." Proof: `scenes-1366x768.png` and every other picker size.

## Settled calls

- Applied the merged health-neutral rule 5 call. No sensitivity.md exists in refine/; no fresh cultural review was required.
- Kept the existing painted art, manikin people flag, kit, privacy statement and certification/911 footer.
- No new mode or topic. The spec's overdose and timer-default questions remain open; this fix does not decide them.
- Unattended choices follow the accepted refine text. The burn gets a distinct early adult card while the provider check remains last; old five-step burn ghosts no longer validate. Nurse notification is included in the existing first seizure step, avoiding a seventh card. Bleeding phone labels reflect its corrected rank.

## Cheats tried

- Five taps plus five-second pauses: original 98.75%, corrected 29.09%, so it cannot masquerade as a strong round.
- Five / 5 s, ten / 4 s, three / 3 s patterns: 35.879%, 58.588%, 34.971%.
- Four normal intervals then 1.9 s wait: 1.363%; short pauses cannot hide behind the median. Displayed rate also falls from the misleading 110.092 to 73.529.
- Two very fast taps in each burst: 0%, with displayed rate corrected from 110.092 to 163.488; constant 110 ms spam: 0%.
- Steady 90 and 150 per minute: 0% each; the summary and trace also name slow/fast.
- Eleven-second pauses: 13.171%, no ghost saved. Partial rounds also cannot set a ghost.
- Control check: twenty complete 110/min rounds with independent 30 ms tap jitter score 99.083% to 99.126%.
- Metronome scheduler: 220 clicks in 120 s. Source-clock scheduling is unchanged.
- Title/body duplication as a Don't detector: the old rule rejects all 12 Don'ts; the new rule rejects zero cards.
- Tap every card repeatedly in all six shuffled decks: 6 to 10 mistakes and 30 to 50 penalty seconds. It can finish as correction practice, but never as a clean zero-penalty result.
- Reverse every shared-rank group: six completed runs, zero mistakes. Non-shared order still costs five seconds.
- Toggle Timer off and on mid-run to try saving a faster ghost: eligible false, no best saved, despite zero mistakes (`timer-toggle-cheat.json`).
- Post-round mouse taps, Space, Enter and a mode return cannot erase the result or start another round. Only Start replaces it.
- Full numeric results and validation assertions: `fix-after/14-cheats.json`, `15-shape-and-sequences.json`, and `fix-validation.json`.

## Voice walk

Held presses 0.12 s, ordinary actions two seconds apart, with a reading pause after the scene briefing and time to hear the paused result.
Main route: Scenes welcome, Collapse briefing, order how-to, six correct steps, best/done, CPR welcome, free practice, Start, a compression, pause, Stop, Field guide, 911 card, Read.
`fix-voice/main.json` records the actual starts in that order: wScenes, brief0, order, best, done, wCpr, round, coachPause, roundEnd0, pauseResult, noGhost, wGuide, Read.
Some navigation cuts still-valid reading short as logged; no queued line arrives from a prior mode. The CPR welcome's first-press cut was separately repaired and checked below.
Side paths: Don't choice plus Read, a correct choice plus Read, wrong-order choice plus Read, and five held free-practice taps followed by idle.

| Line/check | Expected | Observed |
|---|---:|---:|
| wCpr, final entry/free-practice walk | 1, uncut | 1, uncut |
| coachPause, free practice / no first round tap / Clear dialog | 0 / 0 / 0 | 0 / 0 / 0 |
| coachPause, actual running pause | 1 | 1 |
| roundEnd0 then pauseResult on paused Stop | 1 each | 1 each |
| wGuide on main route | 1 | 1 |
| Read after each of three kinds of choice | chosen reason | chosen reason |
| Fixed manifest equals allLines() | exact | 170 unique strings, exact |

Fixed lines are in voice/lines.json; numeric summaries use browser speech with spoken units. No recordings were made.

## Engine changes wanted

None.

## Audit

Finished once within 40 minutes: `fix-audit/audit.md`, 42 leads, 98 frames inspected. No runtime/resize errors, nothing left disabled, Motion off clean, five-held-click and two-quick-tap voice checks clean.
The full audit used the unchanged 567503-byte bundle. It predates the compact label/summary repairs and the additional repeated-outlier meter guard; those have final targeted proof in `fix-exit/`. The full audit was not repeated.
All 42 leads are answered below, in the audit's order. Caption overlays and pointer focus retirement are intentional and confirmed on frames; secondary utilities and phone result scrolling are distinguished from learning choices.

- A1. 375x812 (iframe host): control below the fold: #timer "Timer: On" top 972 | Confirmed secondary utility below the phone fold; the merged refine explicitly leaves this as an optional nit. Main scene and CPR controls fit.
- A2. 375x812 (iframe host): control below the fold: #clear "Clear best times" top 1025 | Confirmed secondary utility below the phone fold; the merged refine explicitly leaves this as an optional nit. Main scene and CPR controls fit.
- A3. mode CPR rhythm: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 232x20 [680x425] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A4. mode CPR rhythm: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 292x20 [800x500] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A5. mode CPR rhythm: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 392x20 [1000x625] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A6. scene-open: overlap: span "Either order" / span "Choose your next move" 23x5 [680x425] | FIXED: final overlap zero at 680, 1366, 1920 and 375 wide; fix-exit/bracket-*.
- A7. scene-open: control below the fold: #clear "Clear best times" top 851 [375x812] | Confirmed secondary utility below the phone fold; the merged refine explicitly leaves this as an optional nit. Main scene and CPR controls fit.
- A8. scene-error: focus fell to the page after clicking #card-d0 (click 1) [every size] | Expected pointer retirement, required by item 4. Last feedback remains readable. Native Enter focus retention is confirmed in fix-exit/keyboard-card.
- A9. scene-error: control below the fold: #clear "Clear best times" top 909 [375x812] | Confirmed secondary utility below the phone fold; the merged refine explicitly leaves this as an optional nit. Main scene and CPR controls fit.
- A10. scene-finish: focus fell to the page after clicking #card-s0 (click 1) [every size] | Expected pointer retirement, required by item 4. Last feedback remains readable. Native Enter focus retention is confirmed in fix-exit/keyboard-card.
- A11. scene-finish: focus fell to the page after clicking #card-s1 (click 1) [every size] | Expected pointer retirement, required by item 4. Last feedback remains readable. Native Enter focus retention is confirmed in fix-exit/keyboard-card.
- A12. scene-finish: focus fell to the page after clicking #card-s2 (click 1) [every size] | Expected pointer retirement, required by item 4. Last feedback remains readable. Native Enter focus retention is confirmed in fix-exit/keyboard-card.
- A13. scene-finish: focus fell to the page after clicking #card-s3 (click 1) [every size] | Expected pointer retirement, required by item 4. Last feedback remains readable. Native Enter focus retention is confirmed in fix-exit/keyboard-card.
- A14. scene-finish: focus fell to the page after clicking #card-s4 (click 1) [every size] | Expected pointer retirement, required by item 4. Last feedback remains readable. Native Enter focus retention is confirmed in fix-exit/keyboard-card.
- A15. scene-finish: focus fell to the page after clicking #card-s5 (click 1) [every size] | Expected pointer retirement, required by item 4. Last feedback remains readable. Native Enter focus retention is confirmed in fix-exit/keyboard-card.
- A16. scene-finish: control below the fold: #clear "Clear best times" top 812 [375x812] | Confirmed secondary utility below the phone fold; the merged refine explicitly leaves this as an optional nit. Main scene and CPR controls fit.
- A17. cpr-running: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 232x20 [680x425] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A18. cpr-running: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 292x20 [800x500] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A19. cpr-running: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 392x20 [1000x625] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A20. cpr-summary: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 232x20 [680x425] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A21. cpr-summary: keep region: #summary: 86% inside the window [680x425] | FIXED: finished-round clock and coach boxes yield space; summary visibility 86% to 100%, bottom 394 at 680x425. Start stays visible; fix-exit/summary-*.
- A22. cpr-summary: choices cut short by a scroll panel: aside.panel "Rate training Review your rate summary. " (1 of 5 controls out of view): #clear "Clear best times" [680x425] | Only secondary Clear still requires panel scrolling. All result metrics and repeated controls fit after the compact correction; this is not a short answer set.
- A23. cpr-summary: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 292x20 [800x500] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A24. cpr-summary: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 392x20 [1000x625] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A25. cpr-summary: control below the fold: #clear "Clear best times" top 821 [375x812] | Confirmed secondary utility below the phone fold; the merged refine explicitly leaves this as an optional nit. Main scene and CPR controls fit.
- A26. cpr-summary: hint out of view: "Review your rate summary. Tap Start 2-minute round to try again." [375x812] | Expected automatic phone scroll to the completed summary. The result and Start remain visible; the header hint stays available above.
- A27. clear-confirmation: hint out of view: "Choose Keep them to return, or Clear both to erase the saved records." [375x812] | Expected page scroll behind a modal; the dialog itself shows both actions and its own explanation.
- A28. summary-after-tap: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 232x20 [680x425] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A29. summary-after-tap: keep region: #summary: 86% inside the window [680x425] | FIXED: finished-round clock and coach boxes yield space; summary visibility 86% to 100%, bottom 394 at 680x425. Start stays visible; fix-exit/summary-*.
- A30. summary-after-tap: choices cut short by a scroll panel: aside.panel "Rate training Review your rate summary. " (1 of 5 controls out of view): #clear "Clear best times" [680x425] | Only secondary Clear still requires panel scrolling. All result metrics and repeated controls fit after the compact correction; this is not a short answer set.
- A31. summary-after-tap: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 292x20 [800x500] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A32. summary-after-tap: overlap: #chest "Chest pad: press once for one compressio" / div.pad-label "CENTER OF CHEST · PRESS SPACE" 392x20 [1000x625] | Intentional caption over the transparent chest tap area, not over other text; inspected at the named size. Caption ignores pointer input.
- A33. summary-after-tap: control below the fold: #clear "Clear best times" top 821 [375x812] | Confirmed secondary utility below the phone fold; the merged refine explicitly leaves this as an optional nit. Main scene and CPR controls fit.
- A34. summary-after-tap: hint out of view: "Review your rate summary. Tap Start 2-minute round to try again." [375x812] | Expected automatic phone scroll to the completed summary. The result and Start remain visible; the header hint stays available above.
- A35. timer-off-scene: control below the fold: #clear "Clear best times" top 829 [375x812] | Confirmed secondary utility below the phone fold; the merged refine explicitly leaves this as an optional nit. Main scene and CPR controls fit.
- A36. First-tap welcome: #scene-0 did not play the picker welcome | Expected: the scene briefing or Clear explanation takes priority. The picker instruction is stale after the scene opens or the modal appears; standard voice rules require skipping it unmarked.
- A37. First-tap welcome: #scene-1 did not play the picker welcome | Expected: the scene briefing or Clear explanation takes priority. The picker instruction is stale after the scene opens or the modal appears; standard voice rules require skipping it unmarked.
- A38. First-tap welcome: #scene-2 did not play the picker welcome | Expected: the scene briefing or Clear explanation takes priority. The picker instruction is stale after the scene opens or the modal appears; standard voice rules require skipping it unmarked.
- A39. First-tap welcome: #scene-3 did not play the picker welcome | Expected: the scene briefing or Clear explanation takes priority. The picker instruction is stale after the scene opens or the modal appears; standard voice rules require skipping it unmarked.
- A40. First-tap welcome: #scene-4 did not play the picker welcome | Expected: the scene briefing or Clear explanation takes priority. The picker instruction is stale after the scene opens or the modal appears; standard voice rules require skipping it unmarked.
- A41. First-tap welcome: #scene-5 did not play the picker welcome | Expected: the scene briefing or Clear explanation takes priority. The picker instruction is stale after the scene opens or the modal appears; standard voice rules require skipping it unmarked.
- A42. First-tap welcome: #clear did not play the picker welcome | Expected: the scene briefing or Clear explanation takes priority. The picker instruction is stale after the scene opens or the modal appears; standard voice rules require skipping it unmarked.

Final bundle: 567840 bytes; SHA256 `93846ace7c1bed1d98b9689b3843a83597a57d9ce459f46af2c2255e49a22ee9`. Final targeted batch: 0 error shots, manifest exactly 170 strings, nine cheap CPR patterns below 95%, normal jittered rounds above 99%. Chrome ports 9920/9921/9922 and host 8725 were checked closed; temporary host.html removed. Bundle commands were capped at 120 seconds, browser batches at 300 seconds and the audit at 2400 seconds; none timed out.

## Left open

- The spec's two open questions remain open. Optional nits left: the upper depth bound, Field guide's Heat practice link, silent key 1 reset, phone picker utilities, welcome after Keep, and Read being inert behind the modal dialog.
- Prior initial HTTP host shots logged two favicon 404s from drive.py's wrapper, with zero iframe resource requests. The temporary host was given a data favicon; the two affected shots were retried. Tool code makes no requests.
- No blocker or should-fix remains open. Three scoped follow-ups were verified after the one full audit; no second full audit was run. Clear may still need scrolling in the compact summary panel; the complete result and Start are visible. All final PNGs were inspected.

## Facts checked

Live source checks on November 4, 2026:

- [AHA 2025 Adult BLS](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support): target rate, minimizing pauses and adult CPR context. Scoring tolerances are explicitly tool rules, not clinical standards.
- [AHA/Red Cross 2024 First Aid](https://cpr.heart.org/en/resuscitation-science/2024-first-aid-guidelines): rapid neck-down water cooling for exertional heat stroke, alternatives if immersion is unavailable, and tourniquets for life-threatening limb bleeding.
- [Red Cross bleeding](https://www.redcross.org/take-a-class/resources/learn-first-aid/bleeding-life-threatening-external): early emergency help, retaining the first pad, one additional pad and no stacking.
- [CDC seizure first aid](https://www.cdc.gov/epilepsy/first-aid-for-seizures/index.html): first seizure, injury, breathing/waking problems, recurrence, duration, water, pregnancy and diabetes. The accepted unknown-history instruction errs toward getting help promptly.
- [Red Cross burns](https://www.redcross.org/take-a-class/resources/learn-first-aid/burns): cooling and medical assessment; early school-adult notification is the accepted refinement.
