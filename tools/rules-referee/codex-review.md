# Codex review: rules-referee
Status: blocked by the required elimination design; the S1 catalog alignment also remains open.
## Played
Cold grade-7 solo play of all twelve clips before reading source or builder notes; also inspected the projector path and both bar tools. Rich lockers and the split clocks are strong; confirmations felt detached from the lock.
## Findings fixed
- Should fix, general, source/notes/metadata: FIBA 2024 was stale. Verified 2026 v1.1 clauses and updated all current references.
- Blocker, family:replay, volleyball clip 8: the main drawing touched the band at 0.8 s although contact and zoom began at 1.0 s. The hand now stays visibly short until contact at every size.
- Should fix, family:replay, softball clip 10: shortstop and third baseman occupied effectively the same position. Separated them without changing arrival times or the call.
- Should fix, general, voice: locker-open speech preceded its painting; moved it to the locker-room reveal. Added short Next/Open locker/library instructions, synchronized the manifest, and restored the appropriate hint after timer continuation.
- Should fix, general, Read: call labels, citation speech, key-frame and opened-locker hints were absent from the manifest. Registered all 88 fixed lines, gave citations spoken number forms, and stopped naming the locked door after an early locker revisit.
- Should fix, general, graphics: right-aligned counters painted their backing beyond the canvas; the phone volleyball legend and floor labels collided. Corrected backing alignment and label positions, checked at 1366 and 375.
- Polish, family:replay: the flat correct-call payoff had no visible lock feedback in the booth. Added a three-light metal lock readout to the replay header after each Escape call.
- Should fix, general, art: net cutout had green and magenta residue. Redrew it; rejected the first transparent attempt and selected a clean magenta-keyed second image through art.py --rekey.
- Should fix, general, phone ending: direct follow-up to the audit iframe failure found Start over focused below the viewport. Compacted only the phone ending and its duplicate sidebar heading; rechecked the recap, last entries and held-click reset with focus visible.
## Findings left
- Blocker, family:quiz: free elimination still opens every locker. The specification mandates free wrong calls, permanent elimination and automatic Key moment; fixing the learning check needs a spec change, prohibited in this review.
- Should fix, general, standards: SHAPE.S1 is a motor-skill standard, not taught by solo replay judging. Catalog edits and a new physical activity are outside the allowed files and spec.
## Break it
Choosing the first available card, then Key moment and one step when needed, solved 12/12 and opened 4/4 both before and after fixes, without rule knowledge. This remains a blocker, not a passing learning check.
Early and penultimate calls failed; duplicate correct submits added zero progress. Replay farming left Escape progress unchanged. Reload cleared progress. No saved best score exists.
100 browser assertions passed: all twelve call gates, step/touch chronology, exact pass positions, clocks and both timer continuations. All 256 keypad strings were tried; only net, glove, flag, hoop opened it and the other 255 cleared. Timer deadlines were accelerated, not left running fifteen minutes.
## Voice walk
Full cold log: review-play/voice-main-cold.json. Final held-click, 2 s main walk: Soccer, Basketball, Volleyball, Softball; Play, call, Next/Open locker; door; net, glove, flag, hoop; Replay booth.
Started in order: howWatch, howCall, line, wrong.1, howTool, good, next, good, tumbler, good, back, open; then good/tumbler/open for the remaining sports, door, out, wBooth. Room welcome was skipped by the first locker tap, permitted by BASELINE 16; its premise remains in hint/Read.
| Line | Kind | Expected | Started |
|---|---|---|---|
| howWatch, howCall, howTool, next, back, door, wBooth | how/welcome | once each | once each |
| good, main | event | 12 | 12 |
| open, main | event | 4 | 4 |
| good and wrong.4, side | event | 5 each | 5 each |
| library, side | how | 1 | 1 |
One of eight tumbler lines was dropped by navigation before starting; seven started. No stale line followed navigation. Read worked with Sound off, included the rule's named source, and yielded promptly on a mode switch. All 88 manifest lines match allLines. Evidence: review-final-voice/voice.json and review-side/voice.json; browser speech fallback, no recordings made.
## Facts checked
- Clips 1-2, pass-time offside and level exemption: [IFAB 2026/27 Law 11](https://theifab.com/laws/latest/offside/).
- Clip 3, defender last touch and wholly over the goal line outside the goal: [IFAB Law 17](https://theifab.com/laws/latest/the-corner-kick/).
- Clips 4, 5 and 6, moving gather/two steps, second dribble exceptions and two free throws for the missed two-point attempt: [FIBA 2026 v1.1, Articles 25.2.1, 24.2, 34.2.2](https://assets.fiba.basketball/image/upload/documents-corporate-fiba-official-rules-2026-v1-1.pdf).
- Clips 7-9, three team hits plus block, net contact during the playing action, floor contact including the boundary: [FIVB 2025-2028 Rules 9.1, 11.3.1, 8.3](https://www.fivb.com/wp-content/uploads/2025/01/FIVB-Volleyball_Rules2025_2028-EN-v05.pdf).
- Clips 10-12, out at first, fair beyond the base, legally caught foul fly; 60-foot bases: [WBSC 2026-2029, 5.5.2 a) iii, 5.1.16 b), 5.5.2 a) ii and Appendix 1](https://static.wbsc.org/uploads/federations/8/cms/documents/e044bf0e-5318-23e3-9d48-32fda7d42482.pdf).
- Motor-skill versus rule-knowledge alignment: [SHAPE America 2024 Standards 1 and 2](https://shapeamerica.org/standards/pe/new-pe-standards/).
- Recomputed fictional replay data from spec: second-last x=36, offside x=39, level x=36; shooter 3.716 m inside 6.75 m; three steps and four touches; ball 3.1 s versus runner 3.3 s; 60 ft=18.288 m. Actual goal geometry uses 7.32 m, already correcting the spec's rounded 7.40 m: [IFAB Law 1.10](https://theifab.com/laws/latest/the-field-of-play/).
- Contrast recomputed: amber/paper 9.814, amber/panel 8.975, dark/amber 9.908, ink/panel 14.229, muted/panel 7.371, white/red 5.622 and white/grass 7.607.
## Sensitivity
None: fictional international sports plays, no cultural, religious, historical or body-health topic. Paintings contain no people; exact-position numbered player tokens are specifically required. A sports reviewer should inspect the simplified contact drawings.
## Flattest moment left
The door code is a direct symbol lookup after twelve fixed cases. The booth lock lights now connect each call to the reward; expanding replay depth or redesigning the final puzzle would change the spec.
## Graphics
All twelve used assets inspected in their scenes; no people missing from the deliberately empty room or schematic fields. Redrawn `art/rr-sym-net.webp` now 180x91, keyed without visible colored residue; original and rejected candidate preserved in Scratch. Built-in imagegen, with the saved prompt in `art/prompts.json`. Both bar tools opened; the painted locker scene retains its richer finish. Used art 467.8 KiB; bundle 734,406 bytes (717.2 KiB).
Inspected all 90 pre-audit frames through 15 contact sheets and individual full-size fault/recheck frames. All eight required sizes passed lock-header geometry; keyboard-only navigation, jittered offside drag, live transport, grayscale and Motion off were exercised. The only direct-host log error was its missing favicon, not a tool request. One browser layout batch lost Chrome; smaller batches completed.
## Audit
Ran once, last, with a 40-minute cap, Chrome 9941 and host 8745; completed. `review-audit/audit.md` has 33 leads; all 78 saved frames were inspected through 13 sheets and full-size compact frames.
- 27 canvas/caption/legend overlap leads: intended overlays, with pointer events disabled and no evidence or controls hidden. Kept the labels.
- Four first-locker welcome leads: permitted by BASELINE 16; the immediate howWatch replaces the first-tap welcome, and the premise stays in hint/Read.
- Two phone leads: the audit could not attach to its iframe, so the claimed missing hint is not an app diagnosis. Direct-host room, library, wrong-call, keypad and timeout checks passed. The ending focus fault was fixed and three targeted ending/reset frames passed; #hint is present. The audit itself did not verify phone contexts.
- Control walks, five repeats, rapid taps, Motion off and resizing during actions: no exceptions, lost focus, moving controls or stuck enabled states.
Wave checks: immediate/reversible hints and Read; stable focus; 44 px controls; short choice sets; correctly timed unknown/outcome labels; honest counters/badges; distinct team styles; no deferred welcome; neutral clip titles and scene clues checked against call cards. Free elimination and S1 are the exceptions named above. No kit changes or second audit. The final post-audit change is only two phone-ending CSS rules; the audited snapshot and review-post-audit.diff preserve that boundary.
## Left open
No questions asked in this unattended run. Followed the specified default Escape, real-time replay, Sound on, Timer off and existing painted style. No shared source files or commits. Owned browsers/servers are closed and host.html is removed.
Two initial read-only commands lacked hard subprocess deadlines; subsequent commands use explicit tree-killing caps. Initial automation mis-selected Goal kick and later clicked obscured locker text behind the keypad; these harness mistakes are not counted as passing outcomes.

The cold path reached the keypad before builder notes; its first exit automation was invalid. The complete asserted escape was verified on the final voice walk. All 78 audit frames and nine direct-phone frames were inspected.
