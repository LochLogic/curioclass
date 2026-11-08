# Polish: bus-stop (Codex fix, round 1)

Curiosity precedence applied throughout. No welcome, goal, score, level, quiz layer, finish screen or kit header was added.
The inherited scene, art and arithmetic remain; the kit frame became a full-width bus dashboard and lower-left Manual.
Drive on is freely available. School returns to the fork; Express and Fill up continue with rolling tickets.
Voice gives at most one first-use hint, then waits for Read, including the sentence-card Read buttons.
These override the lesson-shaped welcome, two-kept-way quota, automatic narration and fixed ride endings in the older spec.
No questions were asked during this unattended run. Missing plate number is left unassigned, rather than invented.

Evidence below is relative to `_scratch/bus-stop/`. Each listed frame was opened and inspected.
`before/` holds reproductions; `proof/`, `polish-proof/`, `extra/`, `final-frames/` and `phone/` hold after checks.
Numeric JSON beside a frame gives its exact state. `reproduce.py`, `verify.py`, and shots JSON preserve the steps.

## Blocker
1. **FIXED: miscount seats.** Before `before/b1-off-miscount.png`, the removed seat 0 was numbered 1. The loop now selects occupied objects. `proof/b1-every-seat-pattern.json`: remove [0] counts [1,2,3,4]; remove [4] counts [0,1,2,3]; remove [1,3] counts [0,2,4]. No removed seat counted in any case. 1366x768.
2. **FIXED: Express giveaway and riders.** Before `before/b2-express-before.png`: three solids plus two leaving rings. After `final-frames/express.png` and `after/b2-express-minus.json`: five plain starting counters, leavers facing out at the open door. Consecutive facts advance rider identities. Rings appear only after reveal, as `extra/cheats-and-resume.png` shows. 1366x768.

## Should fix
1. **FIXED: same-total Ten and School cards and relevant counting.** `before/s1-ten-cards.png` and `before/s1-school-count.png` reproduce distinct totals and counting zero objects. `proof/s1-ten-blue-count.png`: 7+3=10, 7+2=10, 7+4=10, numbering blue counters only. `proof/s1-school-rings-count.png`: all totals zero, numbering dashed rings. The final hint names the actual change. 1366x768. Automatic counting speech is replaced by Read-accessible feedback under Curiosity precedence.
2. **FIXED: Fill up range.** `before/s2-fill-missing.json` has no Fill up control and starts only 4 through 8. Shared Ten-stop machinery now draws from a shuffled nine-start bag. `proof/s2-fill-two-rides.json`: [8,7,9,3,2] then [5,4,6,1,8], covering every integer 1 through 9; all 30 cards end in 10. `final-frames/fill-cards.png`, 1366x768; `phone/phone-fill.png`, 375x812. Five buses continue into another set, without a finish screen.
3. **FIXED: Express Read.** Before `before/s3-express-read.json` contains only the generic action. `proof/s3-read-express.json` logs Read repeating the entire five-riders/two-off story before the action. `proof/s3-read-express.png`, 1366x768.
4. **FIXED: first story timing.** Before `before/s4-first-walk.json`, riders are already moving while only the road line has started. The redundant intro queue is removed. `proof/s4-first-walk.json`: story starts at 1324 ms; walk starts at 1324.5 ms. The story is also in the current Read hint. 1366x768.
5. **FIXED: Express second walk and closed door.** `before/s5-express-rewalk.png` reproduces the reset. `proof/s5-one-express-walk.json` at 2 s: shown=true, zero active walk classes, all three boarders at opacity 0, door open. `proof/s5-one-express-walk.png`, 1366x768.
6. **FIXED: full Split list action.** `before/s6-split-all.png` retains Keep it. `proof/s6-split-all.json` names More, Fewer and a place after all three ways of two. `extra/drive-all-ways-last-kept.json` says only Tap Drive on after all eight ways of seven. 1366x768.
7. **FIXED: Split discs and five-column rows.** Before compact discs measure 35 px in `before/s7-s8-split-ten-1000.json` and `before/s7-s8-split-ten-680.json`. After: 60 px at 1366x768 and 1000x625, 44 px at 680x425, two rows of five. `proof/s7-s8-split-ten-*.json` and final frames prove this. The extra 800x500 regression is fixed and measured at 60 px in `extra/split-ten-800.json`. Phone counters are 60 px: `phone/phone-split-ten.json`.
8. **FIXED: way-list marks and curves.** `before/s7-s8-split-ten-680.png` and its 1366 counterpart reproduce cramped marks. Dedicated arrow padding and outer-margin links replace overlays; compact layouts omit curves. Inspected `proof/s7-s8-split-ten-1366.png`, `final-frames/split-ten-680.png`, and `phone/split-ten-1000.png`. Mark glyph is U+2194, including at 680x425; the 1000-wide equations also stay on one line.
9. **FIXED: duplicate Split instruction.** `before/s9-split-voice.json` logs welcome at 1355 ms and repeated how at 6928 ms. `proof/s9-split-voice.json`, after a 14 s wait, contains one first-use hint and no second instruction. No welcome remains. 1366x768.

## Polish accepted
1. **FIXED:** Tell first rejects cup, counter and Done edits; See again also waits for Go. `polish-proof/p1-tell-first.json`: hold, changed=[], cup disabled, Done disabled, Go shown. 1366x768.
2. **FIXED:** Express separate welcome removed. One fact-plus-action line includes saying the answer aloud. `polish-proof/p2-express-first-hint.json`, 1366x768; final manifest contains no old welcome.
3. **FIXED with Curiosity override:** no Express end screen. Five tickets stay visible while a fresh story arrives. `polish-proof/p3-express-ticket-roll.json`: five tickets, done=false, tiles visible, no finish overlay. Its 1366x768 frame shows the continuing instrument.
4. **FIXED:** stop names sit on each actual painted face. All 16 used scene images were inspected; six rural/stand scenes need different coordinates and vertical camera positions. `sign-coordinates.json` records the original-art source and measurements. Inspected all seven `sign-proof/sign-*.png` desktop frames and `sign-proof/sign-corn-phone.png` at 375x812. Final `sign-proof/grounded-orchard.png` and `grounded-corn-phone.png` retain a code-drawn foreground street while the camera keeps the original sign visible. Route frames exposed the differing orchard face before this final correction.
5. **FIXED:** driver's chart mark moved right. `polish-proof/p4-p5-maple-sign-driver.json`: right=5px; same frame and `final-frames/drive-cards-680.png` show it.
6. **FIXED:** ten waiting riders stand in two perspective rows, clear of the sign. `extra/crowded-curb.png/json`, 680x425: ten boxes, same-row horizontal gaps over 3 px and vertical row gap over 3 px; start=1 is genuinely generated by Fill up.
7. **FIXED:** Split says “Tap a rider counter to send it to the other side.” `proof/s9-split-voice.json` and `extra/calm.png`, 1366x768; old wording removed from source and voice manifest.
8. **FIXED:** Split equation uses one baseline. `final-frames/split-ten.png`, 1366x768; `final-frames/split-ten-680.png`; `phone/phone-split-ten.png`.
9. **FIXED:** fork medallions are on the actual branches at (165,63) and (165,136), with no selected stop on the trunk. The settled over-road question mark remains a separate junction marker when no branch is chosen (`post-audit/fork-junction.png`, 1366x768). `polish-proof/p9-fork-map.png/json`, 1366x768.
10. **FIXED:** each kept addend owns its dot picture; dots measure 5x5 px. Empty slots have no text. `proof/s7-s8-split-ten-1366.json/png`, `final-frames/split-ten-680.png`; 1000-wide spacing rechecked in `phone/split-ten-1000.png`.
11. **FIXED:** notes remove build talk and the old fallback-stage claim; the situation-types link is correctly named; Fill up is documented. `notes.md` Modes, Good to know, Standards and sources.
12. **FIXED:** idle-light element and styling removed. `final-frames/split-ten.png` and `extra/calm.png`, 1366x768.
13. **FIXED:** “Yes! Seven plus three…” is capitalised in the actual departure/Read hint. `extra/ten-capital-read.json/png`, 1366x768; expansions in the manifest use the same constructor.
14. **FIXED:** 80 generated Express sets produced both 2-add and 3-add mixes, each with five distinct facts. `polish-proof/p14-express-mix.json`: [2,3].
15. **FIXED:** Tell first uses a drawn speech-bubble SVG. Inspected `fix-audit/size-1366x768.png` and `post-audit/default-1366.png`; the final bubble is also visible in the scene-coordinate frames.
16. **FIXED:** cup label is Full when full, unavailable when disabled otherwise; Split equation is polite/atomic live text. `polish-proof/p16-cup-full.json`: Full, disabled=true, aria-live=polite. `proof/s6-split-all.json` confirms live updates. Full-bus hints name Done instead of the disabled cup, and drop the obsolete starting-seat readout. `post-audit/verified-full-focus.json` proves focus stays on Done after repeated full-cup presses and the exact current hint is “Every seat is full! Tap Done to explore the number sentences.”
17. **FIXED:** Drive Split ticket uses the last kept way. `polish-proof/p17-last-kept-ticket.json`: kept 7=6+1, then moved counters to 4+3, ticket remains 7=6+1. All-ways variant records 7=0+7 after another unsaved move: `extra/drive-all-ways-last-kept.json`.

## Settled calls
- Same-total cards, concealed Express leavers and all nine Fill up starts applied.
- Cup stops at ten; no buzz, score, timer, first-try reward or new assessment gate. Plain Split counters retained.
- Curiosity precedence removes welcome sequences, the two-way travel quota and all ride-end overlays. A road can be explored without selecting a card.
- The over-road question-mark circle is retained at the junction, while both branch stops are separate, as item 9 requires.
- Existing painted art retained, with no new generated assets or downloads. Bundle is about 2.7 MB, under the 6 MB threshold; no Size line is required.
- No `refine.md` or `refine/` file was edited. No git commits. All writes stayed in this tool and its Scratch directory.

## Cheats tried
- Done with 0, 1, 3, and ten cup taps at an on-2 stop: all remained show; ten taps stopped at seven changed seats. `extra/cheats-and-resume.json`.
- Both false cards in succession: no ticket added; remained tell. Selection by elimination remains allowed as the Refine settled, with no mastery claim.
- Repeated Keep without a move: one recorded way. Sweeping all groupings records real decompositions, not a grade.
- Rapid Express 0 through 5: first value 0 stayed selected; one reveal followed. Show me remains a deliberate exploration control.
- Picking a card just because it ends in ten or zero no longer identifies one candidate: all three totals match.
- Skipping via Drive on is intentional open navigation, not a success result. Fill up preserves the paused Drive state.

## Voice walk
- Held clicks at 0.12 s, 2 s pace. Curiosity uses one first hint, then explicit Read; no unsolicited story/how queue remains.
- First Drive: Maple Street story-plus-action once; walk onset within 1 ms (`proof/s4-first-walk.json`).
- First Split: rider-counter instruction once, still once after 14 s (`proof/s9-split-voice.json`).
- First Express: fact then “Listen, say the answer out loud…” once (`polish-proof/p2-express-first-hint.json`).
- Read repeats the current full Express fact (`proof/s3-read-express.json`). Card Read speaks “Three plus two equals five” (`extra/card-read.json`). Keyboard Read is logged in `extra/keyboard-only.json`.
- The final runtime allLines array equals voice/lines.json exactly: 703 unique lines, verified from `post-audit/verified-full-focus.json`. No recordings were made; browser speech remains the existing fallback. Tests used muted Chrome and prove narration starts/logs, not recorded-clip listening quality.

## The real material
- Complete original route data and 25 Express facts: `content.json`, Curio Class, CC BY 4.0 under repository `LICENSE-CONTENT.md`; code MIT under `LICENSE`. No sampling or external dataset added. `number-check.py` independently checks every route, all 25 facts and every fill partner; `numbers.json` records results.
- Named curriculum reference: NGA Center/CCSSO, https://www.thecorestandards.org/Math/Content/K/OA/, public licence https://www.thecorestandards.org/public-license/, rechecked 2026-11-06. Its licence is not CC BY/CC0; therefore no standards text or examples were copied into the instrument.
- Independent range/context check: Student Achievement Partners, https://achievethecore.org/page/932/situation-types-for-operations-in-word-problems, rechecked 2026-11-06. Reference only; no resource content incorporated. Arithmetic is additionally recomputed independently in Python and executed in JavaScript.
- Existing illustrations: generated with OpenAI gpt-image, edited for Curio Class; original project art under CC BY 4.0. No new painted art or outside art downloaded. Foreground street/curb surfaces are drawn in code to keep riders and wheels grounded under the adaptive scene camera. Manual and tool.draft.json name the material and licences.
- Ten-seat capacity and route places are explicitly fiction. No claim about an actual school bus or locality is made.

## Curiosity short test and lesson creep
- Kid would open it unassigned: yes in my judgment, for moving the riders and choosing the roads. Adult play: the groupings and alternate branches support short exploratory play; no audience study or month-long-use claim is made.
- Real material is the interface: counters, finite arithmetic and conserved groups directly drive the scene. No score or finish is needed: every mode remains open.
- Reference frames opened and used: `before/model-beat-lab.png`, `before/model-elements-inspector.png`, `before/model-span-and-spire.png`, `before/model-pocket-universe.png`. Compare `extra/default.png` and `final-frames/split-ten.png` beside the Beat Lab frame: subject fills the screen, physical controls, no kit header or right-hand lesson panel.
- Search for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done: only the internal wrong-tile CSS class remains; welcome callback returns null. No student-facing ladder or success screen. The inherited optional sentence/number exploration is not a new quiz layer.
- Motion off: zero running animations in `extra/calm.json`. Keyboard-only mode entry and Read work. Phone iframe width and document scroll width both 375; cards bottom 487 px in an 812 px viewport.

## Engine changes wanted
None. Shared kit, scripts and docs were not edited.

## Audit
Completed once on port 9911, host 8715, within the 40-minute limit: `fix-audit/audit.md`, 166 mechanical leads. This is the preserved pre-targeted-repair snapshot, not a claim that every lead was a tool defect. No full audit was rerun.

- All 75 size/state/Motion frames were inspected through `audit-contact-0.png` to `audit-contact-9.png`, indexed by `audit-contact-index.txt`; problem frames and the final targeted frames were also opened at full size.
- The repeated 44 px flags at 680x425 are the explicit preview exception. The audit's “every size” text for some 44 px Split targets comes from duplicate identical findings in its aggregation; direct frames and measurements show 60 px outside the preview, including 375x812.
- Real 800x500 overlap repaired: chart bottom 254.09 px, cards top 259.98 px, replay bottom 246.08 px (`post-audit/cards-800.json`, `final-fill-800.json`). Express strip bottom 149.58, result top 154.58 and tiles top 189.58 px (`express-800.json`). All associated frames were inspected.
- Real compact Split label overlap repaired: label bottom 70.5 px, first counter top 72.5 px (`post-audit/split-680.json`).
- Real sign clipping repaired: tall 760-wide label stays within x=660.86 to 720.33; final phone choice label within x=292.73 to 342.08, with the bus ending at x=277.5. The small Corn Stand face is 45x40 px, with scrollHeight=clientHeight=36 (`sign-proof/corn-phone.json`). Every differing source face was rechecked as item 4 records.
- Real full-cup focus loss repaired by moving focus to Done and preventing disabled-cup pointer presses from dropping it. Repeated real held presses finish on Done (`post-audit/verified-full-focus.json`).
- Manual target and title leads repaired: topic summaries 60 px; phone source links 81 and 60 px; title right 227 px, Close left 240.39 px. All four topic headings fit initially, closed, with no title collision (`post-audit/manual-phone.json`, `manual-680.json`). Opening a long field-guide entry intentionally makes the drawer scroll.
- The hint being covered by an open modal Manual is intentional. The Manual's prose is scrollable; it is not a hidden short choice menu. The disabled “empty seat” matches are descriptive nouns in “Tap the cup to fill every empty seat”, not instructions to tap a disabled seat. Cup and Done remain the named actionable controls.
- All 13 held-click rows have no errors or lost keyboard focus. Five-click 2 s repeats and two quick-tap checks for Split, Express, Fill up, Read and all three roads are clean. No welcome is expected under the Curiosity brief.
- Original resize stress is clean: no exceptions or controls left disabled. An additional height-only resize from an 800x900 iframe to 800x500 keeps all ten 60 px counters within their painted area (`post-audit/height-only-resize.json`). Height changes now trigger layout updates as width changes do.
- Fill up also retains its visible waiting rider and three blue counters after a mode round trip, with zero restarted walks (`post-audit/ten-resume.json`).
- All six actual route paths were exercised through their controls and returned to the fork: `post-audit/route-park.json`, `route-library.json`, `route-farm.json`. Every observed count agrees with `numbers.json`; no finish overlay is present.
- Final bundle: 2,717,876 bytes (about 2.7 MB). JavaScript syntax and independent arithmetic checks pass. Focused drive batches report zero console warnings/errors. Scripts, styles, images and data are inline; no external runtime data loader is present. Source/reference links in the Manual do not fetch themselves. All owned Chrome processes and host servers were closed.

## Left open
- Plate number: absent from this spec and the Curiosities catalog. `plate` is null and the engraved family plate is unnumbered.
- No recording generation was authorised by the applicable Ground rules. Fixed-line synthesis quality awaits the separate voice stage; this fix does not claim clips were heard.
- Two screenshot harness attempts timed out in DevTools; smaller batches succeeded. One earlier artificial Ten test produced undefined art because its fixture omitted rider IDs; corrected fixtures and all later batches had zero console errors.
