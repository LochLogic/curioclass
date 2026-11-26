# First Aid Responder: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: first-aid-responder
#### Built
- Local Build only: six school response scenes, CPR rhythm, five-card Field guide, optional timer, saved scene ghosts and a best CPR trace.
- The self-contained bundle is 460,755 bytes (450.0 KiB), under 2 MB. No commits, shared kit edits, audio recording or deployment.
- Scope and both open questions are resolved in handoff.md: six scenes, no overdose addition, Timer On by default.
#### Numbers check
- Recomputed all source simulation settings, rail counts, timing constants and contrast ratios in Scratch/recompute.py and numbers.json.
- Slots: 6, 5, 6, 5, 5, 6. Five-second penalty, two-second pause threshold, two-minute round, 110/minute = 545.45 ms and 220 clicks.
- Contrast: mint/panel 10.30:1, mint/section 9.76:1, dark ink/mint 9.14:1, warning/section 9.90:1.
- Spec simulation claims do not fully reproduce. At 30 ms jitter, median scoring minimum after five warm-up intervals is 99.54%, but needle range reaches 122.23.
  At 50 ms minimum is 94.91%, at 80 ms 84.26%. Alternating extreme 30 ms errors can yield 99.10 or 123.60.
  The implementation keeps the actual median; it does not clamp the answer into the band.
- Current Red Cross gauze guidance is more qualified than the supplied scene. See handoff.md and linked sources in notes.md.
#### Feel check
- Played all six scenes with held real clicks, including one unsafe choice in each, reversed shared ranks, and a clean ghost replay.
  Best moment: snapping the final step into place and earning an 8.2-second improvement over the earlier gym run.
- Flattest moment 1: the compact guide's Practice it link fell below the preview. Reduced its preview art height and spacing; final link bottom is 401 px at 680x425.
- Flattest moment 2: the 1920-wide CPR equipment looked small inside its instrument bay. Increased torso and dial sizing with viewport height.
- Full two-minute real-time run: 220 compressions, 110/min average, 98.6% in band, longest interval 0.6 s. The saved faint ghost trace reappeared next load.
- Side-by-side frame: Scratch/bar-comparison.png, First Aid Responder beside Beat Lab. Six painted settings and textured equipment hold up well.
  The code training silhouette is intentionally temporary and visibly less rich than the equipment paintings.
#### Done when
1. PASS: all six briefings, correct rail counts and step count plus two unsafe cards, verified in 91 functional assertions.
2. PASS: reversed shared-rank pairs, rejected later ranks, five-second penalties, cross/reason and Never tray.
3. PASS: starts on first action, saves and reloads scene stamps, clear removes both records, Timer Off then On never saves that attempt.
4. FAIL on the always-in-band clause; PASS on the practical checks: at 110 with jitter, in-band fraction exceeds 95%; 90 is below target and a 3.5 s interval is counted as a pause.
   The spec's always-in-band requirement is mathematically inconsistent with its prescribed five-interval median.
5. PASS: the actual scheduler generates 220 audio-clock timestamps in 120 seconds; Sound Off stops the scheduler and all scheduled oscillators.
   The live full-round log contains 222 scheduled clicks including metronome warm-up before Start, not a windowed 120-second count.
6. PASS: a 120 ms pointer press counts once. Held-Space repeat events add only one compression; the keyboard-only run reaches and activates the chest.
7. PASS: rail/deck dominate scenes; chest/dial dominate CPR at 1366x768 and 680x425. See final-scene and final-cpr frames.
8. PASS: first card cuts its stale briefing and acts immediately; Stop ends the round; the chest accepts 220 timed inputs with the metronome active.
9. PASS: all modes include the certification and 911 panel footer. Art plate inspected: no people or red cross emblems.
10. PASS: laptop rail/deck/clock fit; phone chest is 169 px, metronome bottom 806.4 px in the 375x812 iframe. Phone scene deck is two columns.
11. PASS: Curio.voice event/how behavior, stale predicates and Read priority; held 2-second pace log is in Scratch/voice-log.json.
#### Wave lessons
- Hint/voice: PASS: immediate tool-owned hints, focus-card full text, Read context, valid checks, how-line memory from V.heard, action never waits for speech.
- Focus/layout: PASS: no load focus; card DOM stays in place; focus moves deliberately with preventScroll; hint has reserved space on laptops.
- Sizes: PASS for primary controls; every required size inspected, Read enlarged to 44 px, gauge labels at least 10 px. Phone utility controls remain below the fold.
- No giveaways: PASS: shuffled uniform cards, ranks absent from visible choices, wrong choices cost time and show their reason.
- Honest numbers: PASS: penalty labeled, real median retained, average includes pauses; method described in teacher notes. Rate displayed to one decimal near boundaries.
- Standards/family: PASS: NHES.S7 is practiced through safe response decisions and corrections; no family engine specified.
- Motion off: PASS: standby light stops, card/chest animations stop; clocks and training duration remain unchanged. Zero infinite animations in the calm probe.
- Short choices: PASS: full deck remains visible on laptop and preview; phone uses the prescribed two-column list.
- Resize mid-animation: PASS in the single audit, no exceptions or stuck controls. Later pointer-drag changes have targeted drag coverage.
- Welcome timing: PASS: mode-specific welcomes and first-tap actions use the kit; stale briefings are hushed on the first action.
- Unknown as unknown: PASS: unfilled slots and missing rate display no invented answer; no responder outcomes are simulated beyond the spec.
- One look, one meaning: PASS: target band has words, success has a check, unsafe moves have a cross and Never tray.
- Badge truth: PASS: only accepted steps fill the rail; partial CPR rounds are labeled and cannot win a best.
- Hint changes back: PASS: each mode/scene re-establishes its current instructions immediately.
- No answer by copying: PASS: situation describes the event; it does not name the first required action.
#### Audit leads
- One audit completed in about 21 minutes: 47 leads, 82 frames. No tool runtime errors, resize exceptions, stuck controls or infinite calm animations.
- All 47 leads are accounted for below. The full audit was not repeated after these bounded build fixes.
- 17 phone utility-control leads: retained with explanation. Timer, Restart, All scenes and Clear follow the primary two-column scene list.
  Clear also follows CPR results. These secondary controls require phone scrolling; this remains a cold-review layout tradeoff.
- 5 phone hint leads: fixed by moving the existing hint into a reserved header row. Guide hint top 158.4 px, bottom 192.4 px.
- 9 chest/caption overlap leads: intentional caption over the full pad hit area in compact layouts. Caption now has pointer-events:none.
  It does not cover the chest target or intercept taps.
- 3 clipped rail-label leads: intentional two-line shortening. Full action title is now on the actual label; the finish explanation remains available.
- 3 compact finish keep-region leads: fixed. Next bottom is 406 px at 680x425; both finish buttons and the full finish card fit.
- 1 phone-summary keep-region lead: fixed. Completion brings the summary into view, measured top 677.4 px, bottom 811.5 px.
- 6 scene-entry welcome leads: intended kit behavior. Opening a scene skips the stale picker welcome and speaks that scene's briefing and order instruction.
- 3 rapid same-mode welcome cuts: fixed by preserving an already open mode. Three held double-tap checks, 0.7 s apart, finished with zero welcome cuts.
- Additional visual/functional fixes: pointer-capture dragging passes correct and wrong real drags; focused hint clears the clock by 5 px;
  gauge labels measure 10.42 px in preview and 11.16 px at 760 wide; unknown rate has no needle until measurable.
- The test HTTP server logged a connection reset during shutdown. This is a test-host teardown message, not a tool exception.
#### Frames looked at
- Beat Lab and Snowy Mail Route reference frames, 1366x768, bundled only in Scratch.
- All seven desktop/preview sizes in each mode, plus 375x812 hosted in Chrome; calm, grayscale and keyboard frames.
- Six completed student scenes, compact completion and CPR partial summary, real-time two-minute summary, ghost replay, blocked-storage run.
- New equipment and all six retained backgrounds in Scratch/art-plate.png. All generated screenshot contact sheets were inspected.
- All 82 audit PNGs inspected through the 21 sheets in Scratch/audit-sheets; targeted build-fixes, last, phone and footer-probe PNGs inspected individually.
#### Art made
- Two new equipment images from the built-in image tool, six retained painted school backgrounds, eight placed paintings total.
- Finished art: 238,670 bytes (233.1 KiB). Bundle: 450.0 KiB. Prompts/provenance in art/prompts.json; new raw originals in art/raw/.
- No redraws. Both new cutouts were rekeyed with holes and despill to remove magenta edging.
#### Art still to paint
- fa-manikin, owner-reviewed body-form image. The asset is marked people: true and its token is reserved; a faceless code training silhouette is used.
- Retained field painting has a school lawn and cooler rather than the specified blocking sled/shade tent. Retained kitchen has no pan.
#### Engine changes wanted
None.
#### Left open
- The full audit predates the final targeted fixes. Its original leads and the later evidence are preserved for cold review.
- Current Red Cross add-gauze qualification needs spec-owner reconciliation before release. Source wording was preserved.
- AHA's full 2024 first aid page and the supplied CDC heat URL were not retrievable. Red Cross heat guidance and the other named pages were checked.
- No recordings: firm-captain is specified in voice/lines.json; narration currently uses the kit's browser-voice fallback.
- All owned Chrome/server processes closed; no listeners on 8795 or 9990 through 9997. host.html is absent.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: first-aid-responder
#### Played
- Cold as a grade 9-12 solo student: all six scenes, wrong and unsafe choices, reversed shared ranks, five guide cards, full real-time CPR round. Then checked projection and keyboard paths. Read builder notes/source only afterward.
- Strong setting and central decisions; weak card transit and the lost CPR payoff were lifted. One review pass, no commits, edits confined to this tool and its scratch folder.
#### Findings fixed
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
#### Findings left
- Blocker, general, spec/content: broad repeated add-cloth instruction needs reconciliation with the Red Cross qualification: retain the original dressing and avoid stacking multiple pads. The review brief forbids changing a disputed spec. See notes.md, handoff.md and [Red Cross bleeding guidance](https://www.redcross.org/take-a-class/resources/learn-first-aid/bleeding-life-threatening-external).
- Should fix, general, spec/numbers: the prescribed five-interval median cannot guarantee every 30 ms-jitter reading stays inside 100-120. Keep the honest median; change the spec's guarantee. Practical scoring passes 200 seeded rounds at a minimum 99.09 percent in band.
- Should fix, general, spec/scope: CDC names additional seizure 911 triggers. The specified scene and guide teach the duration trigger; their list is not comprehensive. Expansion requires a spec decision. [CDC seizure first aid](https://www.cdc.gov/epilepsy/first-aid-for-seizures/index.html).
#### Flattest moment left
- The text-only When to call 911 and Good to know guide cards remain quiet reference reading. Their Practice it links provide the next action; adding a new challenge would exceed the spec.
#### Graphics
- All nine finished assets and their placement inspected. One missing painting added, two backdrops corrected, one sign cleaned. Manikin body form marked people:true; no face, skin-tone coding, stereotypes, injury imagery or protected red-cross emblem.
- Built-in OpenAI image tool used; prompts/provenance in art/prompts.json and raw originals in art/raw/. Final art: 309,658 bytes (302.4 KiB). Bundle: 560,078 bytes (547.0 KiB).
#### Audit
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
#### Left open
- The content/spec findings above prevent an unqualified release recommendation. No spec, shared kit, other tool, or site changes made.
- Narration remains browser fallback: recordings are absent and recording is prohibited by the build rules. No new topic, certification claim or overdose scene added.
- One oversized browser probe hit its 60-second evaluation limit; the single smaller retry passed. Initial host favicon 404 was removed; final hosted checks were clean.
- Final voice manifest matches all 167 declared lines. No listeners remain on 8745 or 9940-9947; host.html is absent.
- Final audit precedes its bounded confirmed-lead repairs, which receive targeted frames only. No second full audit or polish round.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1 merged 2026-11-04, polish not started)
Counts: blockers 1 (general 1, family 0), should fix 13 (general 13, family 0), polish accepted 10

### Refine: first-aid-responder (round 2026-11-04)

Lenses: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit: 28 leads. Measure-first run: no lens read
codex-report.md or codex-review.md. Facts were checked against AHA 2025 BLS, AHA/ARC 2024 First Aid, Red Cross and CDC
guidance as published (pages not re-fetched); the polish agent re-checks each changed fact at its source.

#### Blocker

1. **The CPR score rewards stopping.** "On target" uses the 5-interval median per compression, so 5 taps at 110 then
   a 5 s stop, repeated, scores 98.8% (real rate 42.5 a minute), is spoken "99 percent on target" and saved as the
   ghost best. Pausing is the habit hands-only CPR most needs to break, and the tool's own Don't card says so. Score
   time in band with no gap over 2 s (a pause zeroes the needle), never let a round with a pause over 10 s become the
   ghost, and name pauses in the spoken result. (Teaching B1) general

#### Should fix

2. **Every Don't card repeats its title as its body**, while 32 of 33 real steps have a short title and a different
   body: the traps are spotted without reading. Same title-plus-body shape for Don'ts; give Heat's "Call 911" a body.
   (Teaching S1, Play 1) general
3. **The coach says "Keep going. Don't stop." every 8 to 9 s forever** after one tap in free practice, before the first
   compression in a round, and over the Clear dialog. Pause line only during a round after a compression; free practice
   says it at most once; not while the dialog is open. (Play 3, Craft 1) general
4. **After a mouse tap the hint becomes the keyboard line and Read speaks a random card** (focus moves to the first
   unused card), so the reason for a mistake is never read. Move focus only on keyboard taps; Read speaks lastFeedback
   after a choice. (Play 2, Craft 3) general
5. **Space never reaches the chest after the mouse picks CPR rhythm, and Space after Stop starts a new round** and
   wipes the summary. Move focus to the chest on entry and after Stop, or count Space on those buttons as compressions.
   (Craft 2) general
6. **Reflex taps after 2:00 wipe the round's trace** while the panel still shows the round. Ignore taps about 1.5 s
   after the round ends, or keep the trace until Start. (Play 6) general
7. **Read speaks run-together and symbol text** ("rate63.9", "slash min", "plus", button labels). Build spoken strings
   for the summary and the finish card. (Craft 4) general
8. **Three cards start in lower case** (send someone to call 911, gently take off rings, start timing the seizure),
   on cards, tooltips and Read lines. (Teaching S2, Craft 5, Play nit 12) general
9. **Deep cut marks "Send someone to call 911" wrong until gloves are on**; Red Cross puts the call first. Share rank
   with gloves, with a reason that help is sent the moment heavy bleeding is seen. (Teaching S3) general
10. **Deep cut's "add cloth on top" is an open source conflict shipped as fact** (notes.md says it needs a decision).
    Settle against AHA/ARC 2024 and the Red Cross page ("Don't lift it. If blood soaks through, put one more pad on
    top and press harder") and remove the open note. (Teaching S4) general
11. **Seizure teaches "call 911 if over 5 minutes" as the whole rule**: add first seizure, hurt, trouble breathing (if
    you don't know their history, call), on the card and the Field guide; consider "Send someone for the nurse" at rank
    2. (Teaching S5) general
12. **A perfect run never shows why the Don'ts are wrong**: a short "Never do" block with both Don'ts and reasons on
    every finish card. (Teaching S6) general
13. **Heat at practice teaches cool cloths for exertional heat stroke**; AHA/ARC 2024 recommends cold-water immersion
    to the neck when available. Reword, and add the guideline to Sources. (Teaching S7) general
14. **"Tap the chest to the beat" with the Metronome off by default**: Metronome on by default, with the summary
    nudging "Try a round with the Metronome off" once the band holds (or reword the welcome). (Play 4, Craft 6)
    general

#### Polish accepted

15. Seizure briefing says they fall to the floor, then a step eases them down: "Move hard or sharp things away".
    (Teaching P1)
16. Burn: "Tell the teacher" shares rank 2; the health care provider check stays last. (Teaching P2)
17. Heavy bleeding: one line that a trained adult can use a tourniquet on an arm or leg when pressure fails.
    (Teaching P3)
18. notes.md "explain why" becomes "read why", or a Talk question asks for it. (Teaching P4)
19. Teacher note: some students may have witnessed an emergency or a death; offer Field guide or rhythm practice
    instead. (Teaching P5)
20. Rate trace: plot 80 to 140 with a taller band; out-of-band words, not color alone. (Play 7)
21. "Either order" drawn as one bracket at readable size; at 375 wide mark both slots "3 or 4". (Play 8, Craft 7)
22. Ghost race visible (a marker stepping along the rail), and "Ghost set: race it next time" after the first best.
    (Play 9)
23. Rail and deck grow with the stage at 1920x1080. (Play 10)
24. First screen: "Beat your own best time" instead of "Your own ghost". (Play 11)

#### To the spec's open questions (already open, for Cory)

- Open question 1 (an overdose scene) and 2 (Timer on by default) are still open.

#### Nits (optional)

- "5-INTERVAL MEDIAN" label is jargon (Teaching N1); "at least 2 inches" could add "not more than 2.4" (Teaching N2);
  "(either order)" in a reason text (Teaching N3)
- Voice rounds 99.5% to "100 percent" (Play 13); Field guide Practice it opens Heat with no reason (Play 14); key 1
  mid-scene throws the run away silently (Play 15); 375 picker controls below the cards (Play 16); Scenes welcome lost
  after Clear and Keep (Play 17)
- Unused roundEnd line would be recorded for nothing (Craft 8); Read is inert while the Clear dialog is open (Craft 9)

#### Settled calls

- Rule 5 does not apply (health topics neutral, checked). Contract clean, 547 KB, no console errors.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: first-aid-responder (round 1)

Counts: blockers 0, should fix 5 (general 5, family 0), polish 2, nit 2

Bundle looked at: `tools/first-aid-responder/first-aid-responder.html` (CURIO_DRAFT=1, 560,078 bytes). My frames and
voice logs: `<scratch>/refine/first-aid-responder/craft/v1` to `v5` (`*.png`, `*.log.json`, `out.txt`), held clicks
(0.12 s), Sound on, Motion on, 1366x768, a fresh Chrome profile per run (port 9751). Shared audit:
`<scratch>/refine/first-aid-responder/audit-r1`.

#### Contract

- One file, 0.56 MB (under the 2 MB goal). No network requests: `performance.getEntriesByType('resource')` is empty
  (v1 `allLines.json`). No console errors or exceptions in any of my 33 shots or in the audit.
- Kit used: `Curio.voice`, `Curio.tone`, `Curio.yes`, `Curio.audio`, `Curio.onSound`, `Curio.onMotion`, kit
  `.calm` and `:focus-visible`. The metronome (Web Audio on the kit's context) and the card drag are tool code; the
  kit has neither, so nothing is re-implemented.
- Metronome: `__tool.testMetro()` gives 220 clicks in 120 s, 0.5455 s apart (Done when 5).

#### Findings

##### Should fix

1. **The coach nags an idle student forever: "Keep going. Don't stop." every 9 s.** (general)
   Where: `coachKey()` and `coach()`, src.html:1471-1488. In free practice (no round running) any single chest tap
   makes `coachKey` return `coachPause` once the student goes quiet for 2 s, and `coach()` re-says it every 8 s with
   no end. How I saw it: v2 `idle-nag` (3 taps, then 40 s idle): spoken at 12.2, 21.5, 30.7 and 39.9 s and still
   going. v2 `idle-dialog`: it keeps playing while the Clear best times dialog is open (21.4 s), over the dialog's
   own line. v3 `kb-cpr-held`: 5 taps, then the same line. A student who taps once and reads the rate note, or a
   teacher who taps to demo and starts talking, gets a scolding loop. During a running round the pause line is right
   (v2 `cpr-rep`, `slow-round`). Better: speak `coachPause` only while a round runs (in free practice show it, at
   most say it once), and add `!$('clear-dialog').open` to its `valid`.

2. **Space does not press the chest after the mouse picks CPR rhythm, and Space after Stop starts a new round and
   wipes the summary.** (general)
   Where: keydown handler src.html:1664-1669 (`if (active?.closest('button') && active.id!=='chest') return;`),
   Stop handler src.html:1608-1611, key "2" path src.html:1661. Focus sits on the CPR rhythm button after a click or
   the 2 key, so Space re-clicks that button. After Stop, focus moves to Start, so the next Space starts a round.
   How I saw it: v3 `kb-cpr-click-space`: click CPR rhythm, Space five times: `total 0`, focus `m-cpr`, while the
   welcome line and hint say "Press Space or tap the chest". v5 `stop-space`: Start, 3 taps, Stop, Space three
   times: `running true, summary false`, the round-over line cut. Better: in CPR rhythm, Space and Enter on the
   mode buttons, Start and Stop count as compressions (or move focus to the chest after a mode entry and after Stop),
   so the key the line names always works and a summary is never lost to the next keypress.

3. **After every mouse tap on a card the hint turns into keyboard text and Read speaks a card the student never
   chose.** (general)
   Where: `choose()` src.html:1173-1175 moves focus to the first unused card after any placed or Never card, and
   that card's `onfocus` (src.html:1098-1102) sets `state.readCard` and the hint "Enter places this card. Read gives
   its full text." The hint "Tap the next step. Read can explain your last move." is overwritten at once, and
   `read()` (src.html:967) prefers `state.readCard` over `state.lastFeedback`. How I saw it: v3 `hint-after-tap`
   (tap Make the scene safe with the mouse: hint is the Enter line, focus on `card-d1`); v4 `r-wrong` (tap the
   "Wait a minute" Don't card, Read says "When the AED arrives, turn it on and follow its voice prompts. Press Enter
   to place this card."); v4 `r-right` (a correct tap, Read says "Stop every few compressions to check them. Press
   Enter to place this card."). The why behind a mistake, the thing Read promises, is never spoken. Better: move
   focus only when the tap came from the keyboard (or with `preventScroll` and without touching the hint and
   readCard when the pointer was used), and let Read speak `lastFeedback` after a choice.

4. **Read speaks run-together and symbol text.** (general)
   Where: `read()` src.html:964-968 uses `textContent` of `#summary` (src.html:1433-1437) and `#finish`
   (src.html:1216-1222). How I saw it, v4 logs, word for word:
   - summary: "Partial round Average rate63.9/min In target band0.0%Longest pause0.9 s Compressions4 ..."
   - finish: "Response complete.0:05.2 · 0 mistakes · Your first best run is set.Why this order Make the scene
     safe: ... Check response + breathing, at most 10 s: ... Push hard + fast, 100 to 120/min: ... Run it again
     Next scene ▶"
   The voice gets "rate63.9", "slash min", "plus", "10 s" and the two button labels. STANDARDS asks for nothing a
   voice would misread. Better: build a spoken string for each ("Average rate 64 a minute. 0 percent in the target
   band. Longest pause 0.9 seconds. 4 compressions.") and for the finish use each step's `text` with its reason, not
   the short titles, and leave out the buttons.

5. **Three step cards start in lower case.** (general)
   Where: src.html:660 "send someone to call 911", src.html:712 "gently take off rings or anything tight near the
   burn", src.html:816 "start timing the seizure" (the spec's "and 3." split carried over). It shows as the small
   line on the card at 1280x720 and up (audit `state-scene-open-1366x768.png`, Send someone to call 911), in each
   card's tooltip and slot title, and in three Read lines in `voice/lines.json`. Better: capitalize the three `text`
   values (the lines file follows from `allLines()`).

##### Polish

6. **"to the beat" when there is no beat.** (general) src.html:863 `wCpr`: "Press Space or tap the chest to the
   beat." The metronome is Off by default, so a first-time student hears about a beat that isn't playing. Better:
   "Press Space or tap the chest at a steady pace. Keep the needle in the shaded band." (or name Metronome).
7. **At 375 wide the "either order" pair splits across rows.** (general) Scene 3 (Deep cut) slots 3 and 4 share a
   rank; in the 3-column phone rail slot 3 sits at the end of row 1 with "either order" under it and slot 4 starts
   row 2 with only a thicker bottom border, so the pair no longer reads as joined (audit
   `state-scene-open-375x812.png`). Better: mark both slots (for example "3 or 4" on each) rather than a label
   under the first.

##### Nit

8. **A line that never plays.** src.html:868 `roundEnd: 'Round over. Check your rate summary.'` is in `L` and
   `voice/lines.json` but every round end says `roundEnd<percent>`. It would be recorded for nothing.
9. **Read can't be pressed while the Clear dialog is open** (the modal makes the header inert; v3 `read-dialog`
   logs no read). The dialog's own line still plays once, so this is minor.

#### Access

- Keyboard: Tab reaches the mode buttons, the six scene cards, More, every step card, the panel and the Field guide
  cards; Enter places a focused card and focus moves to the next one (v4 `kb-place.png`, focus ring clearly visible
  in the kit's 4 px outline). The audit's "settled, then Enter twice" column is clean for every control. Keys 1 to 3
  change modes. The two keyboard breaks are in finding 2.
- Targets: 44 px everywhere (audit, all sizes clean).
- Color is never the only signal: ✓ and ✗ glyphs with words, "Not yet:" text, the gauge band labeled "Target 100 to
  120", the in-band tone differs in pitch as an extra.
- Motion: `.calm` stops the standby dot, shake, land and squash; the needle snaps; the card flight is skipped when
  `Curio.reduce` (audit Motion off clean). Sound: Sound off stops the metronome (`Curio.onSound`) and lines go
  silent (v3 `read-soundoff`). Read: works with Sound off and cuts a playing line (v3 `read-midbrief`); its content
  is findings 3 and 4.

#### Lines

`__tool.allLines()` (167 lines) and `voice/lines.json` (167 lines) match word for word, both ways (v1
`allLines.json`). Each spoken line I logged matched its frame and state, except the idle coach line (finding 1) and
the Read texts (findings 3, 4).

#### Standard voice check

All held clicks (0.12 s), Sound on, Motion on. Logs in `v1` to `v5`.

| Line | Kind | Expected | Spoken | Run |
|---|---|---|---|---|
| brief0 (scene opened, then Restart x4, 10 s apart) | event | 5 | 5 | v1 rep-brief |
| order "Tap the step you would do first..." | how | 1 | 1, then silent (heard) x4 | v1 rep-brief |
| done "Scene complete..." (5 finishes, Run it again 0.9 s later) | event | 5 | 5 | v1 rep-finish |
| best "New best time." (first finish on a fresh profile) | event | 1 | 1 | v1 first run, v3 read-finish |
| wCpr (CPR rhythm entered 5 times) | welcome/how | 1 | 1 | v2 mode-rep |
| wGuide (Field guide entered 5 times) | welcome/how | 1 | 1 | v2 mode-rep |
| round "Tap Start 2-minute round..." (24 free taps, two visits) | how | 1 | 1 | v2 round-how |
| roundEnd percent (5 rounds, Stop, 4.5 s apart) | event | 5 | 5 | v2 cpr-rep |
| coachPause in a running round with real pauses | event | about every 8 s | every 9 s | v2 cpr-rep, slow-round |
| coachPause in free practice, idle 40 s | event | 0 (or 1) | **4, unending** | v2 idle-nag |
| coachPause with the Clear dialog open | event | 0 | **2** | v2 idle-dialog |
| clearHow (dialog) | how | 1 | 1 | v2 idle-dialog |

1. Repeats: right for every line but `coachPause` (finding 1). Wrong-move feedback is on screen only, as the spec
   says (v1 rep-wrong).
2. Stale lines: v3 `stale-fast` (0.2 s taps through a scene, CPR, Scenes, a second scene, All scenes): every line
   was cut or dropped as its moment passed; nothing played late. The `order` line is dropped (not marked heard)
   when the first card is tapped during the briefing, so it can come back later, as the rules want.
3. First tap (fresh page each): stage heading, welcome within about 0.2 s (v4 `ft-stage2`); scene card, only its
   briefing (v3 `ft-scene`, `ft-stage`); mode button, that mode's welcome (v3 `ft-mode`); Read, the hint only
   (`ft-read`); Sound, nothing (`ft-sound`); Sound off then on, the welcome once (`ft-sound-offon`); a key (Tab),
   the welcome (`ft-key`). All pass.
4. Read: stops a playing line and speaks (v3 `read-midbrief`), works with Sound off (`read-soundoff`); a mode
   change right after Read starts its welcome at once (`read-then-mode`, 0.75 s later). What it says is findings 3
   and 4.
5. Order: lines follow the actions in every log.

#### Art

Every `art:` token (fa-gym, fa-cafeteria, fa-shop, fa-kitchen, fa-field, fa-hallway, fa-kit, fa-aed, fa-manikin)
has a `prompts.json` entry. The three local FLUX backdrops (gym, shop, hallway) show empty rooms, no people (checked
at full size). The other six are gpt-image; fa-manikin carries `people: true`, which is cautious but harmless.

#### Words

No em dashes in src.html, notes.md or lines.json. "Curio Class" is written in full. Language is classroom safe.
Privacy: "Saved only on this device." shows on all three modes, under the only control that stores anything.
Lower-case card text is finding 5.

#### Audit pilot

Leads confirmed on my own frames:
- 375x812: Timer: On and Clear best times sit below the fold on the picker and in scenes (audit size and state
  frames). Confirmed, but not a finding: neither is a main control, and the cards, rail and deck are in view.
- 375x812 clear-confirmation: the hint is out of view (it lives in the header, the page is scrolled to the Clear
  button). Confirmed; the dialog itself says what to do, so I did not report it.

Leads that were wrong:
- The 12 "overlap #chest / div.pad-label" rows (680x425, 800x500, 1000x625, four states): the label is placed under
  the torso inside the same bay by design, `pointer-events:none`; on `state-cpr-running-800x500.png` it sits below
  the torso with no clash.
- "Welcome not heard" after a first tap on the six scene cards and on Clear best times: correct behavior. The tap's
  own line plays (the briefing, or the dialog's how line), and "Tap a scene card to open it." would be stale once a
  scene or the dialog is open.

What it missed (none of these show in a single click or a 2 s, five-click pace):
- The free-practice coach loop that needs 9 s of idle time to show (finding 1).
- Space and Enter following focus to the mode button or Start instead of the chest (finding 2): the audit presses
  Enter on whatever holds focus, not the key the line names.
- What Read says after a mouse tap and how it reads a summary or finish card (findings 3 and 4).
- Lower-case card text (finding 5) and the "to the beat" wording (finding 6).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: first-aid-responder (round 1)

Counts: blockers 0, should fix 6, polish 5, nit 6

Played twice: as a grade 9-12 student alone at home (mouse, then Space key), and as a teacher projecting at 1920x1080.
Bundle as given (CURIO_DRAFT=1). My frames and scripts are in
`C:\Users\Cory\AppData\Local\Temp\claude\912539a76ace91d0\c55c8920-4b50-4aa7-8632-31d061e89e76\scratchpad\refine\first-aid-responder\play\`
(`f1/*.png`, shot lists `s1.json` to `s4.json`). Every drive used held clicks (0.12 s) or real Space keys and logged
`__tool.vlog`. No console errors in any shot.

#### Should fix

1. **Don't cards give themselves away by their format.** (Scenes, every scene; `src.html` scene data)
   All 12 Don't cards repeat their title word for word as the small text ("Hold them down" / "Hold them down"). 32 of
   the 33 correct steps have a short title, often with a "+", and a longer, different small text ("Ease down + clear the
   area" / "Ease them to the floor and move hard or sharp things away"). A student can spot the two traps in every scene
   without reading them, which skips the part of the lesson that says what not to do. Seen in frames `02`, `12`, `18`,
   `19` and checked over all six scenes with a script. Better: give Don't cards the same short-title plus fuller-text
   shape as real steps (e.g. "Ice it" / "Put ice on the burn to cool it fast"), and drop the one real step whose text
   equals its title ("Call 911" in Heat at practice). Missed BUILD wave lesson (no giveaways by option length or form).
   **general**

2. **After a mouse tap, the hint and Read jump to a random card.** (Scenes, `choose()` focus move plus card `onfocus`)
   When a tap retires a card (a correct step or a Don't), `choose` moves focus to the first unused card even for a mouse
   tap; that card's `onfocus` then sets the hint to "Enter places this card. Read gives its full text." and
   `state.readCard` to that card. In `02` and `15` a correct tap in Choking at lunch left the hint on the keyboard line,
   and Read then spoke "Give 5 back blows ... Press Enter to place this card." (in `02` the focused card was the Don't
   "Reach blindly into their mouth"). The hint a moment earlier promised "Read can explain your last move." Better: move
   focus only when the tap came from the keyboard (`e.detail===0`), or keep the feedback line as Read's text after a tap.
   **general**

3. **The coach nags while nobody is tapping.** (CPR rhythm, `coachKey()` / `coach()`)
   In free practice, after six taps and then no input, "Keep going. Don't stop." was spoken at 9.1 s, 18.2 s and 27.4 s
   and keeps going every 9 s for as long as the student sits on the mode (`06-idle-nag`). After Start with no taps yet
   it says "Keep going. Don't stop." at about 4.8 s, before the first compression (`07-round-no-taps`). Better: the pause
   line plays only during a round and only after at least one compression, and free practice goes quiet after one pause
   line (back to "Find your rhythm"). STANDARDS: don't nag; the line matches the state. **general**

4. **"Tap the chest to the beat" with no beat.** (CPR rhythm welcome `wCpr` and hint; `state.cpr.metro=false`)
   The welcome and the hint say "Press Space or tap the chest to the beat", but the Metronome starts Off (`03`, `08`:
   metro false, no clicks). A solo student has no beat and no idea what 110 a minute feels like. The spec's arc is to
   learn the rhythm and then hold it without the metronome. Better: Metronome On by default (Sound on), with the
   "round" or summary line nudging "Try a round with the Metronome off" once they hold the band; or reword the welcome.
   **general**

5. **The chest pad's focus ring strikes through its label.** (CPR rhythm, `#chest` focus outline and `.pad-label`)
   Start moves focus to the chest, so for the whole round a light blue focus bar runs straight through "CENTER OF CHEST ·
   PRESS SPACE" (`09`, `10`, zoom `z-padlabel.png`, at 1366x768; the audit flagged the same boxes at 680 to 1000).
   Better: keep the label outside the button's outline (more bottom padding on `.pad-bay`, or an outline offset inward).
   **general**

6. **Reflex taps after 2:00 wipe the round's trace.** (CPR rhythm, `compress()` with `practiceAfterSummary`)
   A student tapping at 110 does not stop exactly at 2:00. In `09` the next few Space presses after the round switched the
   strip chart to a new free-practice trace ("RATE TRACE · 0:06 / 2:00", "7 compressions") while the panel still shows
   "Two-minute round ... 219 compressions"; the coach box shows "Keep going. Don't stop." beside the summary. The trace
   they just earned is gone (it survives only if it was a new best, as the faint ghost). Anything shown twice must match.
   Better: ignore taps for about 1.5 s after the round ends, or keep the round trace until Start or a deliberate tap
   after a pause. **general**

#### Polish

7. **The rate trace is too flat to read.** (CPR rhythm, `drawTrace()`)
   60 to 160 fits into about 60 px at 1366x768 and 1920x1080, so the band is about 12 px and a steady 90 a minute sits
   just under it, looking almost on target (`10`, zoom `z-trace.png`, `21`). Better: plot 80 to 140 (clamp beyond),
   give the band more height, and color the line out of band (warn color plus the words "too slow"/"too fast" in the
   summary so color is not the only signal). **general**

8. **"Either order" is hard to see.** (Scenes, shared-rank slots)
   The shared slots carry a thin bar and a 9 px "↔ either order" under the first slot only (`timed-laptop` audit
   frame, `19`, `20`); at 375 wide the pair even splits across rows. The spec says the slots are "drawn joined". Better:
   one bracket spanning both slots with the label at readable size. **general**

9. **The ghost race barely shows.** (Scenes, `updateScenePanel()` ghost)
   The ghost is a 16 px hollow ring on a slot's corner (`12`), easy to miss, and right after a first timed finish the
   panel still says "Ghost: finish a timed scene to set one." next to "Your first best run is set." (`scene-finish`
   audit frame, `11`). Better: a visible marker that steps along the rail while racing, and "Ghost set: race it next
   time" after the first best. **general**

10. **Big screens leave the deck small.** (Scenes at 1920x1080, teacher projecting)
    In `18` the cards keep 12 to 13 px small text and about 300 px of empty field sits under the deck. Better: let the
    rail and deck grow with the stage height so a class can read the cards from the back. **general**

11. **"Your own ghost" means nothing yet.** (Picker first screen, "Six situations. Your decisions. Your own ghost.")
    A solo student meets "ghost" with no explanation on the first screen. Better: "Beat your own best time" or one line
    on what the ghost is. **general**

#### Nit

12. Small texts that start lowercase: "send someone to call 911", "start timing the seizure", "gently take off rings
    ..." (`timed-laptop`, `19`), and the finish feedback "✓ stopping stops the blood flow." (`scene-finish`). **general**
13. The round-end voice rounds: screen "In target band 99.5%", voice "100 percent" (`09` log `roundEnd100`). **general**
14. Field guide "When to call 911" Practice it opens Heat at practice with no reason given (`16`). **general**
15. Pressing 1 in the middle of a scene returns to the picker and throws the run away without a word. **general**
16. At 375 wide the picker's Timer and Clear best times sit below the six cards (audit lead; confirmed, harmless: they
    move above the rail once a scene opens, `state-scene-open-375x812`). **general**
17. After a first tap on Clear best times and Keep them, the Scenes welcome never plays; the hint is restored, so this
    is minor (audit lead). **general**

#### What it is like (feel)

- **Scenes** feel quick and clear: the briefing is short, the rail and deck are the biggest thing, and a wrong step
  explains itself with the earlier step's reason. Run 2 of the same scene becomes memory, and the ghost is too faint to
  make it a race (item 9). The Don't format tell (item 1) is the moment that went flat: I could finish every scene with
  no mistakes without reading the traps.
- **CPR rhythm** works well with Space at 110: needle steady, 99.5 percent in band over a real 2-minute round (219
  compressions, `09`), "Push faster" at 90 (`10`). It lands less than it could at the end: no beat to start (item 4), and
  the round's picture disappears under the next taps (item 6). The coach nag (item 3) is the moment I would close the
  tab.
- **Field guide** is plain and readable at every size I looked at (`16`, `17`, `state-guide-aed-*`).
- **POLISH.md:** calm mode keeps the clock and skips only the card flight (`22`); no timing is shortened. Words and
  state disagree in items 3, 4, 6, 9, 13.

#### Frames looked at

Mine: `f1/01` to `f1/22`, `z-padlabel.png`, `z-trace.png`. Audit: `size-1366x768`, `state-scene-error-1366x768` and
`-680x425`, `state-scene-finish-1366x768` and `-680x425`, `state-timed-laptop-1366x768`, `state-cpr-running-1366x768`,
`state-cpr-summary-680x425`, `state-scene-open-375x812`, `state-clear-confirmation-375x812`.

#### Audit pilot

- **Confirmed:** chest / pad-label overlap (and it is worse than the lead says: the focus ring strikes through the label
  at 1366x768 and 1920x1080 too, item 5); Timer and Clear below the fold on the 375 picker (real, harmless, item 16);
  welcome not heard after a first tap on Clear best times (minor, item 17).
- **Wrong or harmless:** "welcome not heard" after a first tap on any scene card: once a scene is open the picker's
  welcome is stale, and the briefing plus the "order" line are the right lines. "Hint out of view" with the Clear dialog
  at 375: the dialog itself names both choices.
- **Missed by the audit:** the Don't card format tell (item 1); hint and Read hijacked by the focus move after a mouse
  tap (item 2, the audit's "focus kept" row hides it); the idle coach nag (item 3: its five-click runs never wait 10 s
  with no input); "to the beat" with the Metronome off (item 4); the round trace wiped by post-round taps (item 6); the
  flat strip chart and faint ghost (items 7, 9); stale ghost text after a first best (item 9).

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: first-aid-responder (round 1)

Counts: blockers 1, should fix 7, polish 5, nit 3

Read: spec.md, src.html, notes.md, tool.draft.json, voice/lines.json, the module row (data/modules.csv:
health-pe-9-12-first-aid-and-cpr, NHES.S7 only), BUILD.md wave lessons, the shared audit (audit-r1/audit.md) and its
frames. Own runs (drive.py, port 9731, profile in my scratch folder): scratch `teaching/f1` (CPR and scene checks),
`f2` (pause-pattern round), `f3` (ghost and Timer Off). Fact check against AHA 2025 Adult BLS, AHA/ARC 2024 First Aid,
Red Cross CPR Steps and Learn First Aid, CDC heat and seizure first aid, from the spec's Sources and the guidance as
published; pages were not re-fetched in this run.

#### Blocker

**B1. The CPR score rewards stopping.** general (Honest numbers lesson)
- Where: CPR rhythm, `compress()` and `endRound()` in src.html (in-band = the 5-interval median rate, per compression).
- What: a compression counts "on target" whenever the median of the last 5 intervals is 100 to 120, so one long pause
  per 5 intervals never moves the median. A round of 5 compressions at 110, then a 5 s stop, repeated for 2 minutes,
  scores **98.8% in target band**, is spoken as "Round over. 99 percent of your compressions were on target.", and is
  saved as **New best. Ghost best: 98.8%.** The real compression rate in that round is 42.5 a minute (shown above it as
  Average rate, but the headline, the spoken line and the ghost all use the in-band percent). Python, same rule:
  10 on / 4 s off gives 99.3% at 69 a minute; 3 on / 3 s off gives 98.9% at 45 a minute.
- Why it is a blocker: the one habit hands-only CPR training most needs to break is pausing ("Don't stop", "minimize
  pauses", AHA 2025). The tool's own Don't card in Collapse in the gym says "Stop every few compressions to check them"
  is wrong, and then the CPR mode scores that exact habit at 99 percent and makes it the ghost to beat. REFINE: a meter
  that misleads when its assumption does not hold is a blocker.
- How seen: drive.py `f2/cpr-pause-pattern.png` (summary panel), `__tool.state.cpr.summary` = {average 42.5, percent
  98.8, longest 5.0}, vlog key `roundEnd99`.
- Better: score time, not taps. For example "on target" = share of the 2 minutes in which the current rate is 100 to
  120 and no gap is over 2 s (a pause zeroes the needle until compressions resume), or count a compression in band only
  when its own interval is also under 2 s and the median is in band; and let a round with any pause over 10 s never
  become the ghost. The spoken result should name pauses when there were any ("...on target, with 17 pauses").

#### Should fix

**S1. Every Don't card gives itself away by its text.** general (No giveaways lesson)
- Where: Scenes, all six decks (the `dont` entries in `scenes`).
- What: on all 12 Don't cards the small body text repeats the bold title word for word ("Take off the soaked cloth and
  start over / Take off the soaked cloth and start over"). Of the 33 real steps, 32 have a short headline in "+"
  shorthand and a longer, different body. A student can skip the thinking and avoid the Don'ts by spotting the doubled
  line. Seen on `audit-r1/state-scene-open-1366x768.png` (wood shop deck: both Don'ts doubled) and
  `state-scene-error-1366x768.png`; tabulated from src.html.
- Better: give each Don't a short headline and a fuller body in the same style as the steps ("Wait before calling /
  Wait a minute to see if they wake up, then call"), and give "Call 911" in Heat at practice a body of its own.

**S2. Three step cards start with a lower-case word.** general
- Where: Deep cut ("send someone to call 911"), Burn ("gently take off rings or anything tight near the burn"),
  Seizure ("start timing the seizure"). These came from splitting the spec's "and 3." joined steps.
- What: the lower-case text shows on the card body (`state-scene-open-1366x768.png`, bottom right card), on the slot
  tooltip, and in the Read line for the focused card (voice/lines.json lines 37, 44, 60).
- Better: capitalize the three texts.

**S3. Deep cut: sending someone to call 911 is marked wrong until gloves are on.** general
- Where: Scene 3 ranks (gloves rank 2, "Send someone to call 911" rank 3).
- What: a student who taps "Send someone to call 911" right after "Make the scene safe" is told "Not yet: they protect
  you both" and loses 5 s. Red Cross life-threatening bleeding puts calling 911 before gloves, and sending a bystander
  to call costs the rescuer nothing. The tool teaches that help waits on gloves.
- Better: make "Send someone to call 911" share rank with gloves (or rank 2 with gloves, pressure rank 3), with a reason
  that says help can be sent the moment you see heavy bleeding.

**S4. Deep cut: the "add cloth on top" wording is an open source conflict, shipped as fact.** general
- Where: Scene 3 step "If blood soaks through, add more cloth on top and keep pressing" and the Don't "Take off the soaked
  cloth and start over / Add more on top instead".
- What: notes.md says twice (Oct 31 and Nov 3 source checks) that the current Red Cross page differs (keep the first
  dressing, one added pad, avoid stacking) and that it "needs a spec-owner decision before release". A fact the build
  itself marks unsettled cannot go to Cory as taught content.
- Better: settle it against the AHA/ARC 2024 First Aid text and the Red Cross page, word the step to match ("Don't
  lift it. If blood soaks through, put one more pad on top and press harder"), and remove the open note.

**S5. Seizure: "Call 911 only if longer than 5 minutes" is taught as the whole rule.** general
- Where: Scene 6 step "Call 911 if the seizure lasts longer than 5 minutes" and the Field guide "When to call 911" card.
- What: CDC also says call 911 when it is the person's first seizure, they have trouble breathing or waking afterward,
  another seizure follows, they are hurt, or it happens in water. In the scene the student does not know whether this
  classmate has a seizure history, so "only after 5 minutes" is the rule a student would carry away. notes.md knows
  ("the specified scene teaches only the duration trigger"). In a school the first move is also to get an adult or the
  nurse, which no step says.
- Better: card text "Call 911 if it lasts over 5 minutes, it's their first seizure, or they're hurt or have trouble
  breathing" (reason: "these are emergencies; if you don't know their history, call"), and the same clause on the
  Field guide card. Consider "Send someone for the nurse" sharing rank 2.

**S6. A perfect run never shows why the Don'ts are wrong.** general
- Where: finish card (`finishScene()`: "Why this order" lists only `state.placed`).
- What: a student who never taps a Don't card finishes without ever seeing "Ice can damage the skin more", "You can push
  the object deeper", "people can't swallow their tongue". The "avoid health risks" half of NHES.S7 is taught only to
  the students who get it wrong. Seen on `audit-r1/state-scene-finish-1366x768.png` (no Don'ts on the card).
- Better: add a short "Never do" block under Why this order with both Don'ts and their reasons, every run.

**S7. Heat at practice teaches the weaker cooling method for exertional heat stroke.** general
- Where: Scene 5 step "Cool them fast with cool, wet cloths or a cool bath".
- What: the scene is exertional heat stroke at football practice. AHA/ARC 2024 First Aid recommends whole-body (neck
  down) cold-water immersion as soon as possible for exertional heat stroke, with other active cooling only when
  immersion is not available. The CDC wording (general heat illness) is correct but not what athletic heat stroke
  calls for, and many schools keep an ice tub at practice for exactly this.
- Better: "Cool them fast: cold-water tub up to the neck if there is one, or cold wet towels and ice", reason "cooling
  in the first minutes is what saves lives". Add the 2024 First Aid guideline to the Sources line for this scene.

#### Polish

**P1. Seizure briefing and first step disagree.** general. The briefing says "A student falls to the floor", then a
step is "Ease them to the floor and move hard or sharp things away". Better: "Move hard or sharp things away" as the
card (or a briefing where the student is starting to fall).

**P2. Burn: "Tell the teacher and school nurse" can only come last.** general. In a teaching kitchen the teacher is in
the room; ranking telling an adult after 10 minutes of cooling and dressing reads as "wait to tell an adult". Better:
let "Tell the teacher" share rank 2 with cooling and rings, and keep "a hand burn should be checked by a health care
provider" as the final step.

**P3. Heavy bleeding has no "if pressure doesn't stop it" step.** general. The scene is a forearm wound "bleeding a
lot"; AHA/ARC 2024 and Stop the Bleed (commonly taught in high school) add a tourniquet for life-threatening limb
bleeding that firm pressure does not control. A line in the reason or the Field guide "When to call 911" card ("an
adult trained with a tourniquet can use one on an arm or leg") would close it without a new step.

**P4. notes.md claims more than the tool does.** general. "What it teaches" says students "explain why each step belongs
there"; the tool shows the reasons, and students never explain. Better: "...and read why each step belongs there" or
add a Talk question that asks for it. The rest (Key skills, Support at home) is true of the tool and doable tonight.

**P5. Teacher notes need a content note.** general (rule 8). Collapse, choking and seizures may be hard for a student
who has seen one or lost someone. "Good to know" names the scope (no overdose, no graphic injuries) but not this.
Better: one line: "Some students may have witnessed an emergency or a death; let them choose Field guide or the rhythm
practice instead of a scene." Also note that spec open questions 1 (overdose scene) and 2 (Timer default) are still
open; not a teaching finding, but they belong to the integrator before Cory.

#### Nit

- **N1.** Rate readout label "RATE / MIN · 5-INTERVAL MEDIAN" is jargon for grade 9. "RATE / MIN (last 5 presses)".
- **N2.** Field guide and the CPR note say "at least 2 inches"; AHA's adult range is 2 to 2.4 inches. Fine for
  hands-only messaging; optional "about 2 inches, not more than 2.4".
- **N3.** The "Not yet" line for a shared-rank step reads "Not yet: heavy bleeding needs pressure now and help on the way
  (either order). +5 s." The "(either order)" is the slot's label, not a reason; drop it from the reason text.

#### Checks that passed

- Standards: NHES.S7 is the only code. It is taught by what a solo student does: choosing safe actions in order,
  getting each unsafe Don't corrected with a reason, and holding a rate (once B1 and S6 are fixed, both halves of
  "practice health-enhancing behaviors and avoid or reduce health risks" are taught). No move needed.
- Facts that match the sources: Collapse order (scene safe, shout-tap and breathing check of at most 10 s, gasping not
  normal, call 911 on speaker and get the AED, compressions 100 to 120 in the center of the chest, AED as soon as it
  arrives, keep going) matches Red Cross CPR Steps and AHA 2025 lay-rescuer sequence. Choking: consent question, have
  someone call, 5 back blows then 5 abdominal thrusts above the navel, repeat, CPR if unresponsive, no blind sweeps
  (AHA 2025 order). Burn: cool running water at least 10 minutes (inside the 2024 range), rings off, loose clean
  dressing, no ice, no popping, hand burns get care. Heat: signs, call 911, move, cool, no drink, never alone (CDC).
  Seizure: stay, time it, clear area, soft under head, on one side, never hold down, nothing in the mouth (CDC).
  Field guide Hands-only CPR card is accurate, including breaths for infants and young children. No red cross emblem.
- Gauge geometry: band arc endpoints (116.74, 26.85) and (203.26, 26.85) recomputed for 100 and 120 on the 60 to 160
  semicircle: correct.

#### Done when (spec)

1. Pass. Slots 6, 5, 6, 5, 5, 6; decks 8, 7, 8, 7, 7, 8 (steps plus 2 Don'ts); "either order" on scenes 3, 4, 6 (f1).
2. Pass. Shared-rank steps placed in either order; an out-of-order tap gave "Not yet: ... +5 s"; a Don't went to Never
   with ✗, reason and +5 s; mistakes 2 (f1).
3. Pass. A timed run saved a best and the reopened scene showed the ghost; a Timer Off run and a run with Timer turned
   off mid-way both said "Untimed run. Nothing recorded." (f3). Clear by code (confirm-clear empties `far-best`).
4. Pass as written: steady 110 with up to 30 ms jitter, needle 102.8 to 115.4, 99.5% in band (first tap has no rate);
   90 reads coachFast; a 3 s gap counts one pause, longest 3.5 s (f1). But see B1: the check does not cover a student
   who pauses often, and that case fails.
5. Pass for scheduling: 220 clicks over 120 s, 545.5 ms apart (`testMetro`). Sound Off stops it by code
   (`Curio.onSound`); not heard in a muted Chrome.
6. Pass by code and the audit's held click on #chest ("ok"); `e.repeat` keys are ignored.
7, 9, 10, 11. Play and Craft own these; the audit frames show the rail and deck central at 1366x768 and the footer on
   all three modes. Not re-tested here.
8. Not re-tested here (Play and Craft); the audit's quick-tap rows are clean.

#### Audit pilot

- Confirmed: the #chest / pad-label overlap at 680x425, 800x500 and 1000x625. On `state-mode-cpr-rhythm-800x500.png`
  "CENTER OF CHEST · PRESS SPACE" sits on the bottom edge of the chest pad; readable, cosmetic (Play/Craft).
- Wrong or benign: "welcome not heard" after a first tap on a scene card and on Clear best times. The scene card plays
  its briefing and the "order" how line instead, and the picker welcome ("Tap a scene card") no longer fits once a
  scene is open (`welcome()` returns null with a scene open). Not a teaching gap.
- Not checked by me: the 375x812 below-the-fold rows for Timer and Clear best times (Play/Craft).
- Missed (outside what it can see): the pause-pattern score (B1), the doubled-text Don't giveaway (S1), lower-case card
  text (S2), and every fact and order finding (S3 to S7, P1 to P3).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: first-aid-responder (Codex fix, round 1)

Root: `S:\CurioClass-codex`. Only the tool folder and its scratch folder were written. No commits; refine.md and refine/ untouched.
Evidence below is under `_scratch/first-aid-responder/`: `fix-before/`, `fix-after/`, `fix-voice/`, `fix-audit/` and `fix-exit/`.
Each blocker and should-fix was reproduced with drive.py at 1366x768 before its code changed. Additional sizes are named below.

#### Blocker

1. FIXED: Time-based scoring replaces tap percentage. The original five-tap/pause pattern fell from 98.75% at 40/min to 29.09%. A gap clears the needle and rolling window; an 11 s gap cannot save a ghost. Old tap-score ghosts are ignored. Proof: before/after `01-paused-score.png/.json`, after `14-cheats.json`, `16-pause-zero.json`, and voice `main.json` (pauseResult spoken). Two further burst/wait patterns revealed a falsely in-band median needle even though the new scores were low. Repeated outliers now expose the five-interval mean to the gauge and coach; one stray tap retains median smoothing. Before both read 110.092; after they read 73.529 and 163.488. Proof: `fix-before/guard-before.json` and `fix-exit/final-cheats.json`.

#### Should fix

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

#### Polish accepted

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

#### Settled calls

- Applied the merged health-neutral rule 5 call. No sensitivity.md exists in refine/; no fresh cultural review was required.
- Kept the existing painted art, manikin people flag, kit, privacy statement and certification/911 footer.
- No new mode or topic. The spec's overdose and timer-default questions remain open; this fix does not decide them.
- Unattended choices follow the accepted refine text. The burn gets a distinct early adult card while the provider check remains last; old five-step burn ghosts no longer validate. Nurse notification is included in the existing first seizure step, avoiding a seventh card. Bleeding phone labels reflect its corrected rank.

#### Cheats tried

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

#### Voice walk

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

#### Engine changes wanted

None.

#### Audit

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

#### Left open

- The spec's two open questions remain open. Optional nits left: the upper depth bound, Field guide's Heat practice link, silent key 1 reset, phone picker utilities, welcome after Keep, and Read being inert behind the modal dialog.
- Prior initial HTTP host shots logged two favicon 404s from drive.py's wrapper, with zero iframe resource requests. The temporary host was given a data favicon; the two affected shots were retried. Tool code makes no requests.
- No blocker or should-fix remains open. Three scoped follow-ups were verified after the one full audit; no second full audit was run. Clear may still need scrolling in the compact summary panel; the complete result and Start are visible. All final PNGs were inspected.

#### Facts checked

Live source checks on November 4, 2026:

- [AHA 2025 Adult BLS](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support): target rate, minimizing pauses and adult CPR context. Scoring tolerances are explicitly tool rules, not clinical standards.
- [AHA/Red Cross 2024 First Aid](https://cpr.heart.org/en/resuscitation-science/2024-first-aid-guidelines): rapid neck-down water cooling for exertional heat stroke, alternatives if immersion is unavailable, and tourniquets for life-threatening limb bleeding.
- [Red Cross bleeding](https://www.redcross.org/take-a-class/resources/learn-first-aid/bleeding-life-threatening-external): early emergency help, retaining the first pad, one additional pad and no stacking.
- [CDC seizure first aid](https://www.cdc.gov/epilepsy/first-aid-for-seizures/index.html): first seizure, injury, breathing/waking problems, recurrence, duration, water, pregnancy and diabetes. The accepted unknown-history instruction errs toward getting help promptly.
- [Red Cross burns](https://www.redcross.org/take-a-class/resources/learn-first-aid/burns): cooling and medical assessment; early school-adult notification is the accepted refinement.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### First Aid Responder handoff

#### Current fix, November 4, 2026
The merged round 1 list is refine.md. This fix changes only this tool and its scratch folder.
Before and after evidence is in _scratch/first-aid-responder/fix-before and fix-after.
See polish.md for per-item outcomes, cheats and the single final audit.

#### Source map
src.html contains the CSS, six scene data records, mode renderers and interactions.
openScene shuffles once; choose accepts the lowest remaining rank, retires cards in place and adds mistake penalties.
railMarkup sorts ranks for slot grouping, with a single bracket on desktop and repeated position labels on phones.
The burn now has six steps because the accepted refine adds early adult notification while keeping the provider check last.
finishScene shows both Never do reasons even for perfect runs. updateScenePanel replays the prior ghost's stamps.
The more visible Ghost marker is labeled and advances along the rail; a first best says it is ready for the next race.

#### CPR scoring and state
The gauge normally keeps the median of five intervals for jitter tolerance. Two outliers in the last ten intervals
(outside 440 to 700 milliseconds) expose a repeated burst/wait pattern: if the five-interval mean is outside the band,
the gauge and coach use that mean. One stray tap still gets median smoothing. A pause over two seconds clears the needle and window.
The round score uses elapsed time, not compression count: median and mean rates must be in band, each credited interval
must be 440 to 700 milliseconds and receives at most 600 milliseconds. These are tool scoring guards, not clinical thresholds.
Leading and trailing inactivity reduce the score; pauses over ten seconds disqualify a ghost. Partial rounds cannot save.
Saved CPR ghosts use scoring: time-v2; old tap-based scores are ignored. Scene records retain their existing format.
Only Start replaces a finished round's summary and trace. Reflex taps and mode returns preserve both.
Space works on entry and after Stop because focus goes to the chest, with preventScroll.
Coach pause speech requires a running round and at least one compression. It is silent during free-practice pauses and dialogs.
Metronome starts on; a strong completed round suggests turning it off next time. Sound Off stops scheduled oscillators.
The trace covers 80 to 140, with explicit too-slow/too-fast words and a taller band.

#### Narration and access
Curio.voice supplies welcome priority, how-line memory, Read and stale checks. Fixed lines come from L and allLines().
voice/lines.json must match allLines word for word. No audio was recorded during this fix; browser fallback remains.
Pointer choices keep their feedback. Keyboard choices can move focus, but Read still explains the last choice.
finishRead uses full action sentences and reasons; summaryRead uses spoken units and names pauses, without DOM text concatenation.
window.__tool exposes the state, actions, scene data, line manifest, voice log and deterministic metronome probe for checks.

#### Facts settled from live sources
Red Cross bleeding guidance keeps the original pad, allows one more and rejects stacking multiple pads.
AHA/Red Cross 2024 supports direct pressure and trained tourniquet use for life-threatening limb bleeding.
Calling for help shares rank with gloves. Seizure unknown history calls immediately; first seizure, injury, breathing
or waking difficulty, recurrence and duration also appear in the scene and guide. The nurse is requested while staying.
The guide additionally names water, pregnancy and diabetes with loss of consciousness, following CDC.
Exertional heat stroke uses neck-down cold-water immersion when available, with cold towels and ice packs as fallback.
Links and the live source-check date are in notes.md and polish.md. Earlier report conflicts are historical, now settled.

#### Sensitivity
Health practice is neutral and non-graphic. The merged settled call says baseline rule 5 does not apply.
Teacher notes acknowledge students who have witnessed an emergency or death and offer the other modes.
The tool is practice and awareness, not certification; its existing footer and local-storage privacy statement remain.

#### Art
The existing nine painted assets are retained. Their prompts and provenance are in art/prompts.json, originals in art/raw.
The painted manikin remains marked people: true because it depicts a body form. No new people or art were generated.
The chest target, gauge, trace, cards, ghost and rails are drawn in code. Motion off removes movement, not time.

#### Open questions
The spec's overdose scene and timer-default questions remain open. This fix adds no seventh scene and keeps Timer on.
There was no unattended question needing an answer: accepted refine instructions settled the content changes.

#### Engine changes wanted
None.

#### Final verification
The single mechanical audit finished with 42 leads and no runtime, resize or repetition failures.
It predates three scoped follow-ups: compact bracket spacing, compact completed-summary space, and the repeated-outlier
gauge guard confirmed by two more meter cheats. Targeted final evidence for all three is in fix-exit/.
The bracket has zero measured overlap at 680, 1366, 1920 and 375 wide, including the phone burn's split shared group.
At 680x425, completed summaries hide the redundant clock and coach box so the entire result fits. Active rounds keep them.
Pointer retirement deliberately lets focus leave a used card; native Enter still transfers focus to another usable card.
polish.md records every audit lead, the final bundle size, retained optional nits and the exact before/after numbers.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: refine.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-04)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
