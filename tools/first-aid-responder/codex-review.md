# Codex review: first-aid-responder
## Played
- Cold as a grade 9-12 solo student: all six scenes, wrong and unsafe choices, reversed shared ranks, five guide cards, full real-time CPR round. Then checked projection and keyboard paths. Read builder notes/source only afterward.
- Strong setting and central decisions; weak card transit and the lost CPR payoff were lifted. One review pass, no commits, edits confined to this tool and its scratch folder.
## Findings fixed
- Should fix, general, CPR: continuing taps erased a completed summary. Results now survive free practice, mode returns and clearing records; Start replaces them. Read includes the result.
- Should fix, general, voice: stale coaching could name the wrong correction. Queued coaching now checks its exact current state and Coach voice; disabling coaching stops its current line.
- Should fix, general, Scenes phone: clock, ghost, Timer, Restart and All scenes were below the deck. The same controls now sit above the rail; deck and actions fit without scrolling.
- Should fix, general, CPR layout: results pushed the certification footer off the laptop panel. Compact paired controls preserve the summary and footer.
- Should fix, general, voice: rounded results and fixed card/guide Read text were missing from the manifest. allLines and voice/lines.json now match.
- Should fix, general, Craft: fixed focus from guide practice to chest, timer hints naming nonexistent cards, clock minute rollover, compact trace-label collisions and continuous trace lines through long pauses.
- Should fix, general, Art: added painted fa-manikin; corrected fa-field with sled/shade and fa-kitchen with pan; removed cafeteria sign lettering. Existing palette, equipment and other scenes retained.
- Polish, general, Scenes: accepted cards now travel visibly to the rail with immediate state and sound feedback; Motion off skips movement and keeps timing.
- Should fix, general, audit-confirmed: phone finish buttons were partly cut off; all six finish cards now fit, maximum bottom 806.4 px in the 375x812 host. Compact free-practice hint no longer collides with controls. Gauge spacing and explicit rail ellipsis corrected.
- Should fix, general, dialog: Clear could speak the stale picker welcome. It now speaks its own valid instruction, restores the prior hint on cancel, and suppresses the picker welcome while open. Sound reserves its header width to prevent shifts.
## Findings left
- Blocker, general, spec/content: broad repeated add-cloth instruction needs reconciliation with the Red Cross qualification: retain the original dressing and avoid stacking multiple pads. The review brief forbids changing a disputed spec. See notes.md, handoff.md and [Red Cross bleeding guidance](https://www.redcross.org/take-a-class/resources/learn-first-aid/bleeding-life-threatening-external).
- Should fix, general, spec/numbers: the prescribed five-interval median cannot guarantee every 30 ms-jitter reading stays inside 100-120. Keep the honest median; change the spec's guarantee. Practical scoring passes 200 seeded rounds at a minimum 99.09 percent in band.
- Should fix, general, spec/scope: CDC names additional seizure 911 triggers. The specified scene and guide teach the duration trigger; their list is not comprehensive. Expansion requires a spec decision. [CDC seizure first aid](https://www.cdc.gov/epilepsy/first-aid-for-seizures/index.html).
## Flattest moment left
- The text-only When to call 911 and Good to know guide cards remain quiet reference reading. Their Practice it links provide the next action; adding a new challenge would exceed the spec.
## Graphics
- All nine finished assets and their placement inspected. One missing painting added, two backdrops corrected, one sign cleaned. Manikin body form marked people:true; no face, skin-tone coding, stereotypes, injury imagery or protected red-cross emblem.
- Built-in OpenAI image tool used; prompts/provenance in art/prompts.json and raw originals in art/raw/. Final art: 309,658 bytes (302.4 KiB). Bundle: 560,078 bytes (547.0 KiB).
## Audit
- One full audit completed in about 23 minutes, inside the 40-minute limit, Chrome 9941 and host 8745: 37 leads, 98 frames inspected through 27 sheets. No runtime errors, resize exceptions, stuck controls or infinite calm animations.
- Audit accounting: corrected 4 gauge-boundary groups, 3 compact rail-ellipsis rows and 3 phone finish keep-region rows. Retained 12 intentional caption-over-pad hit-area rows, 8 secondary fold rows, 6 correctly skipped picker welcomes, and 1 inert background-hint row behind the clear dialog.
- Fold rows: Clear is a secondary record utility; the picker Timer is also available above the rail before the first timed card. All frequently used scene and CPR controls fit. Captions do not intercept the pad. Full rail actions remain in titles and the completion list.
- Post-audit targeted checks: seven phone states and four desktop states, zero console errors. Both phone finish actions fully visible in every scene; compact hint has a 5 px gap before controls; dialog speaks only its own how line; Sound moves no header controls.
- Focused evidence: 37 assertions pass; all six counts and both shared-rank directions, penalties, timer eligibility, save/clear, 220 compression round, 90/min, 3.5 s pause, metronome 220 timestamps, retained summary and blocked storage.
- Held pointer counts once; repeated Space keydowns count once; grayscale stays legible; Motion off keeps clocks and has zero loops.
- Voice counts, from review-voice-results.json:

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| brief0, five restarts after initial | event | 5 | 5 |
| order | how | 1 | 1 |
| wCpr, fresh mode tap | welcome | 1 | 1 |
| First Read | read | 1, no welcome | 1, no welcome |
| First Sound | welcome | 0 | 0 |
| Sound back on | welcome | 1 | 1 |
| Push faster, slow-rate sequence | event | 1 | 1 |
| Pause after Coach voice off | event | 0 | 0 |
| Clear, fresh first tap after repair | how | 1, no picker welcome | 1, no picker welcome |

- Evidence: review-cold/, review-fixed/, review-final/, review-phone-final/, review-voice/, review-exit/, review-audit/ and review-audit-sheets/ in _scratch/first-aid-responder/. All claimed frames opened.
## Left open
- The content/spec findings above prevent an unqualified release recommendation. No spec, shared kit, other tool, or site changes made.
- Narration remains browser fallback: recordings are absent and recording is prohibited by the build rules. No new topic, certification claim or overdose scene added.
- One oversized browser probe hit its 60-second evaluation limit; the single smaller retry passed. Initial host favicon 404 was removed; final hosted checks were clean.
- Final voice manifest matches all 167 declared lines. No listeners remain on 8745 or 9940-9947; host.html is absent.
- Final audit precedes its bounded confirmed-lead repairs, which receive targeted frames only. No second full audit or polish round.
