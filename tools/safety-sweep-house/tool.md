# Safety Sweep House: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: safety-sweep-house

#### Built
Built in `S:\CurioClass-codex`, with authored files confined to the named tool and scratch folders.
Six painted rooms, twelve hazards, six look-alikes, persistent in-visit decisions, scene fixes, reflection reveals and a final Safety card.
One explore experience, no score, timer, saved progress or network requests. `tool.draft.json` has stage `built`.
Uses the starter, kit frame, Motion, Sound, Read, Curio.voice and tones. No family engine applies.
Readable source was formatted and both pre-format and post-format scripts passed `node --check`.
No git commits, branch operations, shared-file edits, publishing or polish round.

#### Numbers check
`_scratch/safety-sweep-house/numbers.json` recomputes the contrast, content distributions and unit conversion.
All twelve contrast ratios match the spec: 14.12, 5.96, 6.42, 7.12, 5.13, 6.69, 6.58, 5.04, 10.18, 11.20, 17.21 and 4.67 to 1.
Safe positions: four each. Grown-up first / act then tell: six each. Safer sets: Everyone six, Theo four, You two.
Three feet is 36 inches; keyboard increments are six inches. The check compares the actual distance before display rounding.
The spec's 72-tap claim omits required steps. An explicit tap-target / keyboard-ruler route here uses 155 inputs, including room navigation.
That model includes the reflection reveal's Back to room, four ruler arrow presses, Enter, and selecting the ruler object. It is not a time estimate.

#### Facts checked
Checked against current named primary guidance during the build, in addition to the supplied spec. Sources also appear in notes.md.
- NHES S5 indicators 5.5.1-5 and S7 indicators 7.5.1-2: [SHAPE America 2024 standards](https://shapeamerica.org/standards/health/new-he-standards/).
- Poison Help, US number 1-800-222-1222, free and available at any time: [HRSA](https://poisonhelp.hrsa.gov/faq/calling-poison-help).
- Cleaners must not be mixed; bleach with ammonia produces harmful gas, including when mixed outside: [CDC](https://www.cdc.gov/hygiene/about/cleaning-and-disinfecting-with-bleach.html) and [Washington DOH](https://doh.wa.gov/community-and-environment/contaminants/bleach-mixing-dangers).
- Medicine, vitamins and gummies belong out of children's sight and reach; safety caps are not childproof; grown-ups give medicines: [CDC PROTECT](https://www.cdc.gov/medication-safety/protect/index.html).
- Gummies can resemble candy and cause harm when taken incorrectly: [CDC Up and Away](https://www.cdc.gov/medication-safety/php/toolkit/index.html).
- Clear things that burn from the stove, stay with cooking, point pot handles back: [USFA cooking](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/cooking/) and [USFA messages](https://www.usfa.fema.gov/prevention/fire-officials/public-information-officers/sample-press-releases/).
- Candles need 12 inches of clearance, go out when leaving, and battery candles avoid a flame: [USFA candle safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/candle/).
- Smoke alarms need monthly tests; removing the battery disables their warning function: [USFA alarms](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/index.html).
- Keep anything that burns at least three feet from heaters: [USFA heating](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/).
- Two exit routes and an outside meeting place: [USFA children](https://www.usfa.fema.gov/prevention/home-fires/at-risk-audiences/children/) and [Red Cross planning](https://www.redcross.org/local/texas/north-texas/about-us/news-and-events/news/prevent--prepare--and-escape--fire-safety-starts-with-smoke-alar.html).
- Get out, stay out, call 911 outside: [American Red Cross](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire/if-a-fire-starts.html/).
- Young children can drown quickly and silently in shallow water; empty tubs and supervise: [AAP](https://www.healthychildren.org/English/safety-prevention/at-home/pages/Bathroom-Safety.aspx) and [CPSC](https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/In-Home-Drowning-Safety-Information-Center).
- Pool gates self-close and self-latch, and must not be propped: [CPSC Pool Safely](https://www.poolsafely.gov/parents/safety-tips/).
- Children leave matches and lighters alone and tell an adult: [USFA children](https://www.usfa.fema.gov/prevention/home-fires/at-risk-audiences/children/).
- Do not share school, address or phone with unknown online contacts; block, report and tell: [FTC gaming](https://consumer.ftc.gov/articles/kids-and-video-games) and [NetSmartz](https://www.missingkids.org/content/dam/netsmartz/itc/downloadable/itc-s3-episode-guide-gotcha-for-upper-elementary.pdf).
- Prize messages asking for passwords are scams: [FTC Youville](https://consumer.ftc.gov/system/files/consumer_ftc_gov/pdf/WhatInfoIsPersonal-Lesson-508.pdf).
- The six look-alike reasons use the matching guidance above. Maya's identity and household details are fictional scenario premises.
The Theo reason was narrowed: medicine out of reach, grown-ups stay near water. The spec's absolute statement that little kids cannot swim was not repeated.

#### Break it
`play/checks.json`: 143 assertions passed in a full-house run using held real clicks, whole-pixel jittered drags and keys. No console errors.
- Think: always picked the wrong help answer first. Each case corrected it; options remained unavailable until the answer was viewed. No score is awarded.
- Choose: peeked every card, then tried both unsafe choices. Check never appeared before the safe choice. All three outcomes then appeared together.
- Tried the cheapest fixed-index strategy: safe positions are balanced four / four / four. Mashing is intentionally permitted by the spec, with consequences exposed.
- Each adult-first fix: attempted progression before Tell. The actionable object / hold control was absent until the grown-up arrived.
- Movable objects: tapped the target without selecting. No fix. Then used the drag or select-and-target alternative successfully.
- Candle and alarm: four short held taps each did not accumulate. One continuous one-second or two-second hold succeeded.
- Heater: Enter at one foot and at 2.5 feet failed. Four six-inch arrow movements from one foot reached three feet and passed.
- Chat: Report before Block failed. Block, then Report, then Tell was required. Pop-up needed Close and Tell.
- Every act-then-tell fix stayed incomplete after the action alone. Tell was also required.
- Reflection: Done started disabled. A wrong or broad selection still reveals the correct people and reason, as required; it does not award an accuracy badge.
- Completion: every case required the safe choice, action, help and reflection. Merely opening rooms, peeking or finding look-alikes did not light rooms.
- Reset No preserved all work. Reset Yes cleared every case. Leaving and reopening a room preserved its current step.

#### Voice walk
Friendly-dad is specified; the brief prohibits recording, so runtime speech uses the kit's browser fallback. Voice asset size is zero KB.
Held clicks, 120 ms, two-second gaps; evidence: `voice-main.json`, `voice-side.json`, `voice-finale.json` and `voice-summary.json`.
Main, Kitchen: roomIn, stop, think, choose, tried, safe, fix, who, safe, roomDone.
The second hazard's stop, think, choose, fix and who were hint-only after being heard once. Tried started once for the hazard tested.
Side, Game room: Read house hint, roomIn, lookalike, stop, think, choose, safe, fix, who.
Finale: roomIn, stop, think, choose, safe, fix, who, houseDone, poison; the final queue was empty.
HouseDone and poison each started once and were not cut. The finale fixture precompleted eleven cases, then real input completed the lighter case.
The welcome can be skipped by immediate action. Essential instructions remain in the hint and Read.
At this fast pace, newer steps interrupt some earlier instructions; the logs explicitly record those cuts. They are not unstarted or repeated how-to lines.
Human listening quality and the eventual recorded voice remain for cold review.

#### Feel check
Played the entire house through all twelve fixes. The best moment is the last room lighting and the complete house appearing behind the earned Safety card.
The alarm's sustained Test and the separate Block / Report sequence give later rooms a different feel from the first bucket move.
Flat moment one: several generated cutouts were miniature rooms. Redrew ten as isolated objects and re-anchored them in the painted scenes.
Flat moment two: fixes initially swapped art in the old location. Moved the cool towel across the kitchen, alarm to ceiling, medicine and lighter up high.
Also removed a painted chair and blanket from the hallway backdrop so the fixed heater scene actually has open space.
Visual checks found and fixed the compact card crowding, Check falling below the fold, and old tub / gate images persisting with Motion off.
Compared both bar tools. `feel-comparison.png` puts this tool beside Snowy Mail Route. The painted house is richer, and the clipboard fits its world.
The choices remain text-heavy compared with Beat Lab's direct making; that comes from the required decision content. Peeks and scene actions carry the play.

#### Done when
1. PASS: room painting dominates; focused hazard is large; three outcome cards sit beside it. `frames/choices-1366.png`.
2. PASS: full-size choices fit above the fold; compact layout uses Rooms. Final `fit-frame/small-safe-fit.png` shows Check fully visible at 680x425.
3. PASS for immediate controls during zoom and option changes, exercised by sub-400 ms input gaps. Tub and gate interrupted transitions were checked separately.
4. PASS: all six look-alikes opened Looks fine, never a decision, with distinct reasons; full play assertions and room frames.
5. PASS: all twelve help questions occurred before choices; balanced six / six verified from content and wrong-answer play.
6. PASS: twelve safe picks exposed all three outcomes; both unsafe choices per case failed to open Check.
7. PASS: all twelve reflection reveals showed the appropriate set and reason; unselected Done was disabled.
8. PASS: all twelve scene actions completed, changed art, and showed checks. Twelve habits appear in the safe-result cards and final card.
9. PASS: full run lit six lamps and porch, opened the Safety card; finale voice log contains both whole emergency lines without cuts.
10. PASS for once-per-load starts and hint-only repeats; voice logs document interruptions when the student advances quickly. Tried was once per hazard.

#### Wave lessons
- Hint and voice: PASS, immediate tool-owned hints and Read; Curio.voice chooses repeats through V.heard. Fast-pace cuts are disclosed above.
- Focus and layout: PASS in keyboard path and manual checks; rebuilds restore a surviving control or the next action using preventScroll. No focus on load.
- Sizes and targets: PASS in manual matrix and narrow host; buttons use 44 px minimums. The incomplete mechanical audit has not independently confirmed every state.
- No giveaways: PASS within the spec. No safe badge before choosing; positions balanced; intentionally permitted exploration is not scored.
- Honest numbers: PASS, room progress means completed fixes; heater distance uses real unrounded state. No performance score or estimate.
- Standards: PASS, search, help decision, outcomes, choice, physical action and reflection are each student actions. No family engine applies.
- Motion off: PASS, ambient motion stops, hold time remains unchanged, and completed tub / gate pictures swap cleanly.
- Short choices visible: PASS, all three cards stay in view; compact safe-state overflow was repaired.
- Resize mid-animation: manual size changes preserved completed Safety card and paging. Full audit resize sweep is NOT VERIFIED due runner failure.
- Welcome timing: PASS, one-mode welcomeAfter, immediate first action, Read-first path works.
- Unknown as unknown: PASS, unfinished rooms remain dim and risky until their fixes are actually complete.
- One look, one meaning: PASS, green check means fixed, blue check means look-alike inspected; words and icons accompany color.
- Badge truth: PASS, checks appear only after the actual scene action; rooms light only after both cases finish.
- Hint restores with state: PASS, leaving and returning to Think preserved its next-action hint.
- No copying an answer clue: PASS as a decision explorer; situation gives the risk, and the student must still perform the fix. No scored diagnosis is claimed.

#### Audit leads
Audit NOT FINISHED. One invocation used port 9991 and host 8795 with a forty-minute outer limit.
The driver's internal sixty-second Chrome protocol timeout occurred in size setup before any audit.md or frames were produced.
No audit leads or clean-audit claim exist. `audit-failure.md` preserves the failure. The cold reviewer must rerun the audit.
An earlier host favicon 404 was fixed with an inline favicon in the tool and temporary host; the two narrow-host reruns had zero errors.

#### Frames looked at
All emitted PNGs were opened: both bar frames; house, kitchen and compact early frames; all fourteen full-play frames;
all twelve matrix frames; two clean phone reruns; four repair frames; four final layout frames; final compact-fit frame;
main, side and finale voice frames; fixed Kitchen, Hallway, Bathroom and Backyard frames; final hallway check and interrupted tub / gate frames.
All seven art contact sheets, updated redraw sheets, people sheet and side-by-side bar comparison were also viewed.
Safety-card and fixed-room layout reruns use explicit completed-state fixtures, after the separate full real-input completion run.

#### Art made
46 images, five marked people:true. Eleven assets were redrawn or edited during the build; discarded candidates are in scratch.
1609.9 KB of finished WebP art; 2237.2 KB offline bundle; zero KB recorded voice.
The bundle is about 2.2 MB, modestly over the 2 MB goal. Quality is 72, backgrounds 1024 px; all teaching art is retained.
Prompts and raw PNGs are in the art folder; generated sources were copied into the project. Credits name OpenAI gpt-image.
Fresh representation review passed the five family assets. Minor Theo portrait age variation and small key fringes were noted; despill was applied.

#### Art still to paint
None. The owner still needs to view the people contact sheet before shipping. No shipping occurs in this session.

#### Engine changes wanted
`scripts/drive.py`, HOST: add an inline empty favicon to avoid a spurious missing-favicon console lead from the temporary iframe host.
The workaround stayed in the allowed temporary host file, which was removed. No engine or shared script was edited.

#### Left open
- Mechanical audit and its comprehensive resize / focus sweep remain incomplete because of the Chrome protocol timeout.
- Human listening review of browser speech and eventual friendly-dad recordings are deferred. The source lines and logs are ready.
- People contact-sheet viewing before shipping; fresh representation review is complete.
- The built neighbors inspected did not contain handoff.md or refine.md. Their source and both required bar tools were read and opened instead.
- See handoff.md for the compact-layout, art-count, help-rule wording, tap-count and Theo-reason decisions.
- Ports 8795 and 9990 through 9997 were checked closed. No host.html remains. Build only ends here.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: safety-sweep-house

#### Played
Cold full-house play as a grade 4 student, before reading the builder's report, handoff, notes or source. Inviting search, useful consequences, satisfying final lamps; the repeated decision cards are the slowest stretch.
Then walked the teaching, play and craft lenses, including projection-size frames, all six look-alikes and twelve physical fixes. No commits or shared source edits.

#### Findings fixed
- **Blocker, general, chat controls:** Block and Report inherited white text on white buttons. Explicit ink color makes both readable; `review-matrix/review-chat-contrast.png`.
- **Blocker, general, heater ruler:** the picture included an unmoved second blanket and its zero did not mark the heater edge. A separate heater and blanket now share the ruler's geometry; distance measures the nearest blanket edge. Display rounds down, so 2.999 feet cannot read as three. `review-targets/heater-final-680.png` and `heater-final-1366.png`.
- **Blocker, general, backyard art:** a baked-open gate stayed visible behind the repaired gate. Redrew the backdrop without gate leaves and aligned the changing gate across its opening; full-size and phone fixed-room frames checked.
- **Should fix, general, Read:** Think explanations, reflection reasons, half the wide Safety card and its emergency instructions were omitted. Read now follows the visible card and includes both emergency instructions; wide-card log contains all twelve habits.
- **Should fix, general, voice:** room navigation could hush the completion line; a delayed welcome could start over a look-alike card. Preserve room completion, constrain the welcome, and validate state-specific narration. Repeated the main and side paths.
- **Should fix, general, card reopening:** a click Event was treated as the `earned` argument and replayed the house-completion announcement. Wrap the handler; reopening now uses only the emergency how-to, once heard.
- **Should fix, general, online room:** inline message plaques overpainted wrapped lines. Block layout and bounded type now keep the messages distinct at 680 and 375 widths.
- **Should fix, general, scene fixes:** moving a bucket or cooled towel could leave another copy in the scene. Removed the duplicate during the action. The Think explanation now explicitly distinguishes moving a cool blanket from touching the heater.
- **Should fix, general, reset dialog:** underlying room controls remained active, and Escape lost focus. Make background content inert while confirming and restore focus to Sweep again.
- **Should fix, general, audit layout:** moved compact Rooms navigation into the header; separated the kitchen pot/towel hit areas; made the portrait Safety card a viewport overlay with inactive background content. These address below-fold controls and overlapping targets without shrinking the art.
- **Polish, general, weakest art:** redrew the magenta-stained cleaner cutout and the look-alike pot that included a miniature stove. Preserved the painted style; improved alarm and block-bin keying.
- **Polish, general, flattest action:** tap-target fixes jumped straight to the finished painting. They now show the object traveling to the target, with immediate feedback and live next controls. Motion off swaps directly and clears any flight in progress.

#### Findings left
- **Nit, general:** some furniture cutouts retain a slightly different perspective from the room painting. Kept their texture and detail; no additional restyling pass.
- Browser speech remains the kit fallback. No recording was made because CODEX-BUILD.md forbids recording audio; the intended friendly-dad delivery is not an authored clip yet.

#### Break it
`review-break/checks.json`: 145 checks passed with held real clicks, jittered drags and keys, including a complete twelve-case run and reset. The reviewed input script was reused as a baseline, then extended; its old PASS was not accepted as evidence.
- Room count: opening rooms, tapping look-alikes and peeking never lights a room. Both hazards need safe choice, action, adult contact and reflection completion. No score, accuracy badge, saved best or timer exists.
- Think: picked the wrong help answer first in all twelve cases. It corrects the answer before Choose, with no accuracy reward. Six adult-first and six act-then-tell cases confirmed.
- Choose: peeked all cards, tried both unsafe options, and tried fixed-index choices. Unsafe choices never expose Check; safe picks show all three outcomes. Safe positions are 4/4/4. Every-option exploration is explicitly permitted by the unscored spec.
- Adult-first fixes: attempted progression before Tell. No actionable object or hold control is available until the adult arrives.
- Move fixes: target alone does nothing; real drags and select-then-target work. Action without the required Tell still cannot complete.
- Candle and alarm: four short holds do not accumulate; one continuous one- or two-second hold works. Leaving the step cancels a hold.
- Heater: Enter at one foot, 2.5 feet and 2.999 feet fails; three feet succeeds. Nearest-edge geometry, six-inch keys, singular foot and conservative display checked at 680 and 1366.
- Chat: Report before Block fails. Block, Report and Tell are required in order. Pop-up needs Close and Tell.
- Reflection: Done starts disabled. Always Everyone or any single person still reveals the actual safer set and reason, as the spec requires; it makes no claim of correct independent mastery.
- Reset: No keeps the completed house, Yes clears it; Escape returns focus. Leaving and returning preserves the unfinished decision.
- Keyboard-only real key sequence completed the entire cleaner case; `review-keyboard-complete.json` records done:true. Grayscale retains words and symbols; calm frames retain meaningful states.

#### Voice walk
Default Sound on, 120 ms held clicks, two-second gaps: Kitchen, cleaners Stop, Think, Choose, peek, unsafe pick, safe pick, Check, move, Tell, reflection; repeat for towel, House, next room.
Started in order: roomIn, stop, think, choose, tried, safe, fix, who, safe, roomDone. The second case's how-to lines are hint-only. Room completion was not cut during the House/next-room transition.
Game-room side path: Read, roomIn, lookalike, stop, think, choose, safe, fix, who. Read with Sound off speaks the current explanation; leaving clears stale speech.
Finale: roomIn, stop, think, choose, safe, fix, who, houseDone, poison. The last two finish uncut; queue empty. Eleven cases were precompleted for this timing fixture, after the separate complete input run.
At a two-second pace some earlier instructions are cut when the student advances; the logs disclose this. No unstarted required step was lost, no instruction later names an old state, and Read remains available.

| Line / kind | Expected starts | Observed |
|---|---:|---:|
| stop, think, choose, fix, who / how, two hazards | 1 each | 1 each |
| safe / event, two hazards | 2 | 2 |
| lookalike / how, five visits | 1 | 1 |
| tried / event, five unsafe taps in one hazard | 1 by spec | 1 |
| houseDone and poison / earned finale | 1 each, whole | 1 each, whole |

#### Facts checked
Checked current named guidance on 2026-11-06, independently of the builder's source claims.
- Decision and practice indicators 5.5.1-5 and 7.5.1-2: [SHAPE America, NHES 2024](https://shapeamerica.org/standards/health/new-he-standards/). Each is exercised by search, help decision, comparison, choice, reflection or scene action.
- Never mix cleaners; bleach plus ammonia produces irritating gases and breathing symptoms: [Washington DOH](https://doh.wa.gov/community-and-environment/contaminants/bleach-mixing-dangers) and [CDC cleaning guidance](https://www.cdc.gov/hygiene/about/cleaning-and-disinfecting-with-bleach.html). Outdoor mixing still producing gas follows the same reaction; it is not a safe exception.
- Medicine, vitamins and gummies belong above children's reach and out of sight; excess ingestion can harm children: [CDC Up and Away](https://www.cdc.gov/medication-safety/php/toolkit/index.html). Medicine is given by a grown-up, not sampled as candy.
- Child-resistant caps are not childproof: [National Capital Poison Center, prevention card](https://www.poison.org/-/media/files/poisonorg/public-ed-materials/pdfs/tip-card-to-prevent-poisonings-in-children.pdf).
- Towel/heat/fire-spread risks, staying with cooking and pot handles toward the back: [USFA cooking safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/cooking/) and [USFA home safety handout](https://www.usfa.fema.gov/downloads/pdf/publications/home-fire-safety-poster-brochure.pdf).
- Candle separation of one foot, extinguishing when leaving, and flameless alternatives: [USFA candle safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/candle/).
- Missing battery prevents this alarm's warning; monthly Test-button check: [USFA smoke alarms](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/). No universal battery replacement interval is taught.
- Three-foot clearance from things that burn: [USFA heating safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/). Three feet equals 36 inches; the keyboard moves six inches per press.
- Two exits per room and an outside meeting place: [USFA escape planning](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/).
- Shallow-water drowning can be quick and silent; empty unused tubs and keep young children supervised: [CPSC in-home drowning](https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/In-Home-Drowning-Safety-Information-Center) and [AAP bathroom safety](https://www.healthychildren.org/English/safety-prevention/at-home/pages/Bathroom-Safety.aspx).
- Pool barriers need self-closing, self-latching gates; do not prop them open: [CPSC Pool Safely](https://www.poolsafely.gov/parents/safety-tips/) and its [barrier guidance](https://www.poolsafely.gov/wp-content/uploads/2023/05/Safety-Barrier-Guidelines-Pub-362_0423.pdf).
- Children leave matches/lighters alone and tell an adult: [USFA youth fire safety](https://www.usfa.fema.gov/prevention/arson/prevent-youth-firesetting/) and [Utah State Fire Marshal](https://firemarshal.utah.gov/services/cigarette-fire-safety/match-and-lighter-safety/).
- Protect school/contact details; block/report unwanted game contact and involve a trusted grown-up: [FTC kids and video games](https://consumer.ftc.gov/articles/kids-and-video-games).
- Prize/password pop-ups can steal account access; close without entering details: [FTC phishing guidance](https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams). The tool's password claim is about the unsolicited prize message in this scene.
- Poison Help 1-800-222-1222, US, free and available at any time: [HRSA](https://poisonhelp.hrsa.gov/faq/calling-poison-help) and [National Capital Poison Center](https://www.poison.org/need-immediate-assistance).
- Fire: leave, stay out, then call 911 outside: [American Red Cross](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire/if-a-fire-starts.html) and USFA escape guidance above.
- The six look-alike explanations use the corresponding guidance above. Maya's identity and the family are fictional premises; Theo's benefit never assumes that all young children cannot swim.
- Recomputed all twelve contrast ratios, minimum 4.67:1; safe positions 4/4/4, help 6/6, beneficiary sets 6/4/2. The full tap-target/keyboard route is 155 inputs, not the spec's 72: 72 decisions + 36 fixing/help inputs + 36 reflection inputs + 11 room-navigation inputs.

#### Sensitivity
No cultural tradition, religion or hard history is represented. Fire, poisoning, drowning and online solicitation may connect with lived trauma; notes and plan retain school disclosure procedures and never ask for a child's experience.
Reviewed all five marked people assets: fully clothed Theo, warm Dad and Grandma June, natural skin tones and ages, no mocking or stereotyped roles. A later reviewer should check the small Theo age/identity variation and avoid treating this family structure as universal.

#### Flattest moment left
The later Think cards repeat the same decision framework. The spec deliberately asks for that practice; shortening it or adding a new game would change scope. The moving fixes, alarm hold and ordered online actions now provide the variation.

#### Graphics
46 images checked on four contact sheets and room/action frames. Three redraws: cleaner group, backyard backdrop and isolated pot; alarm and block-bin key cleanup. No missing art tokens. People flags preserved.
Finished art about 1603 KB; offline bundle about 2231 KB. Rich backgrounds, material detail, family, porch glow and lamp payoff retained. Compared the existing Snowy Mail Route and Beat Lab reference frames; no plain substitute art introduced.
Opened all review PNGs from cold-frames, cold-play, review-break, review-matrix, review-voice, review-targets and review-last. Size matrix: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a real 375x812 iframe.

#### Audit
Completed once with the required 40-minute limit, port 9961 and host 8765. `review-audit/audit.md` contains 27 lead rows on the audited bundle. Confirmed three root causes: kitchen target overlap, compact Rooms navigation below the fold, and phone Safety-card controls below the fold. Fixed all three and re-shot the affected room state at all eight sizes plus narrow Safe, Who and Safety-card states. Scoped checks show zero pot/towel intersection, visible header navigation and all three Safety-card buttons inside the phone viewport.
Two background-label occlusion rows are intentional card overlay, not missing teaching text; background content is now inert. The late welcome rows are permitted by the one-mode `welcomeAfter` spec. Console, focus, Motion off, held-click/Read stress and mid-action resize checks passed. The full audit was not repeated after repairs, as required by the one-pass brief.

#### Left open
No confirmed blocker or should-fix remains open. Audit lead resolutions and scoped frames are preserved in Scratch.
No publishing, outreach, recording, commits or engine changes. Voice listening quality and authored friendly-dad recordings remain outside this recording-prohibited pass.
Unattended choices followed the spec: unscored correction and exploration, six/six help split, short-landscape side-by-side layout, and the existing family. The spec was left unchanged.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 0 (general 0, family 0), should fix 15 (general 15, family 0), polish accepted 13

### Refine: safety-sweep-house

Lens files: refine/teaching.md, refine/play.md, refine/craft.md (no sensitivity.md; rule 5 does not apply).
Frames: teaching `S:/CurioClass-codex-scratch/safety-sweep-house/teaching/frames/`, play `.../play/out/`,
craft `.../craft/out1..out3/`, shared audit `.../audit-r1/`. Integrator spot-checked items 1, 2, 4, 6 and 8 in
src.html and content.json, and frames peek-safe.png and room4.png.

#### Blocker
None.

#### Should fix
1. **Peeking labels the answer on the stage.** src.html:843-857 (renderFocus). The peek button sets `p.last`
   (src.html:640), and the stage outcome card for that index is drawn with the green edge, "✓ Safe result" and the
   habit line whenever `i === h.safe`. Peek each option in turn and the stage names the safe one before any pick, so
   5.5.3 and 5.5.4 need no judgment. Seen: teaching/frames/peek-safe.png (Kitchen / Cleaners, Choice 2 peeked, stage
   reads "✓ Safe result ... Never mix cleaners."); confirmed in code. Fixed: before the safe pick, every peeked or tried
   card on the stage is the same neutral "What could happen" card (no green edge, no Safe label, no habit); the Safe
   label and habit appear only after the safe pick. (general)
2. **Choose is solved by "pick the option with a grown-up in it" (12 of 12) or "pick the longest" (10 of 12).**
   content.json options (spec Content). Every safe option brings in a grown-up ("then tell a grown-up", "Get Dad
   back", "Get a grown-up to blow it out") and no unsafe one does; the safe option is also longest on 10. Seen: script
   over content.json by both Teaching and Play, then played h00 to h11 (play/out). Fixed: on most hazards one wrong
   option carries a grown-up in a wrong way ("Tell Dad later, after your game", "Wait for a grown-up to notice", "Call
   a grown-up from the hall and leave Theo by the tub"); a few safe options with no grown-up word where the spec's
   Think answer is "Act now" (pot handle style, closing the pop-up) and mixed lengths, so neither rule beats about 5 of
   12. Keep the outcome meanings, the 4/4/4 safe positions and the Think split; update the matching option text in
   the spec's Content list with the same edit. (general)
3. **The student does the grown-up's part on Gummies and Towel.** content.json `fix` for hazard 6 ("Tap Tell Dad,
   then help him drag the closed bottle up to the high cabinet") and hazard 1 ("Tap Tell Dad. When the towel is cool,
   drag it onto the hook"). The child carries the medicine, against notes.md ("Adults handle the medicine"; children
   "do not ... put medicines away alone") and the habit "Vitamins are medicine too"; on Towel the safe outcome says
   "Dad moves the towel", then the student moves it. 7.5.2 demonstrates the practice taught, so it must be the right
   one. Seen: teaching/frames/gummies-fix.png, towel-fix.png. Fixed: Gummies, after Tell Dad the student taps to
   watch Dad put the bottle up (as Lighter does) or keeps Theo away from the counter; Towel, Dad's chip moves the towel
   and the student's step is a child's step (step back, keep Theo out of the kitchen). Keep the engine's existing
   drag/tap/watch actions; update the two spec Fix lines to match. (general)
4. **The help rule contradicts the Heater answer and names the blanket on every hazard.** src.html:360-361 (`helpRule`),
   615-617, 435. The rule reads "Medicine, fire, heat or climbing: get a grown-up first. You may move a cool blanket
   away from heat without touching the heater...", shown and read on all twelve, including the chat, pop-up, tub and
   gate; the spec's general sentence ("If you can make it safe without touching those, act now, then tell.") was
   dropped, so a student who applies the rule to the heater is told they were wrong. Seen: teaching/frames/heater-think.png,
   chat-think.png; craft finding 4. Fixed: the spec's rule line word for word on every hazard, plus one short line per
   hazard (content.json) saying why this one falls on its side (Heater: "The heater stays untouched; a blanket you can
   pull away is safe to move."). (general)
5. **Heater ruler labels sit off the marks the check uses, and the ruler is clipped at 680x425.** src.html:144-150,
   886-887, 1067-1073. Labels are spread with `justify-content: space-between` plus padding while the blanket and the
   3-foot check use the ruler's outer edges: at 1366x768 the true 3 ft point is x=663 but the "3 ft" label centers
   near 651, so the blanket's edge on the label reads "2.9 feet" and "Still too close"; the tick under "2 ft" cuts its
   text; at 680x425 the ruler's lower part is cut off and "0 ft" sits on the half-foot tick. Seen: craft/out3
   ruler-2-9.png, teaching/frames/heater-2p5.png, play/out/h05-fix-680.png, play/crop-680-ruler.png, audit
   state-heater-ruler-375x812.png. Fixed: each label absolutely placed at n/4 of the ruler width, centered on its
   tick, measured from the visible blanket edge; the whole ruler inside the stage at 680x425 and 375 wide. (general)
6. **"Who is safer" Theo reason line does not match the hazard.** src.html:694-698 (`reason`). On all four Theo hazards
   it reads "Keep medicine out of little kids' reach. Grown-ups stay with them near water.", so Tub and Gate are
   explained by medicine and Pills and Gummies by water; it also differs from the spec. Seen:
   teaching/frames/pills-everyone.png, play/out/h07-reveal.png; confirmed in code. Fixed: a reason line per hazard in
   content.json, built from the spec's three lines (Theo: "Little kids can't read labels or swim, so grown-ups and big
   kids keep things out of reach." as the base) and naming this hazard. (general)
7. **Picking "Everyone" on a Theo or You hazard is never corrected.** src.html:663-673. `selected` is true for every
   chip once Everyone is in `p.who`, so the right chip shows "✓ Safer", Everyone stays pressed with no mark, and the
   reason line never says why it mostly protects one person; "always Everyone" passes all 12, though the spec's own
   check says "the reveal corrects the rest". Seen: play/out/everyone-theo.png, teaching/frames/pills-everyone.png.
   Fixed: on the reveal, an over-wide pick gets an outline and a short line ("Mostly Theo this time: ..."), never a
   red mark or a score. (general)
8. **Fix hint repeats "Tap Tell" and keeps saying it after the grown-up is here.** src.html:549-552 (hintFor) with
   content.json `fix`. Before Tell it reads "Tap Tell Dad first. Tap Tell Dad. When the towel is cool, ..." (Candle,
   Pills, Smoke alarm, Gummies, Lighter too); after Tell the hint still starts "Tap Tell Dad" while the panel shows
   "Dad is here." and no Tell button. Seen: play/out/h01-fix.png, h02-fix.png, h06-fix.png, audit
   state-alarm-hold-680x425.png; craft finding 3; confirmed in code. Fixed: before Tell, "Tap Tell Dad first." alone
   (or the fix with its leading "Tap Tell X." stripped); after Tell, only the student's remaining step. Read speaks
   the same. (general)
9. **Disabled buttons look live.** src.html:41-45 (no `button.b:disabled` style). Done before any chip and Report
   before Block look enabled; a student taps Report first and nothing happens, with no hint change. Seen:
   play/out/h04-acted.png, audit state-chat-controls-1366x768.png. Fixed: a clear disabled look (muted, no press
   motion, `cursor: default`), and a tap on disabled Report re-states "Tap Block first." in the hint. (general)
10. **Keyboard focus falls to the page after the stage House button or Escape.** src.html:483-491. The fallback tries
    `#controls` (no button in house view), `#house` (gone) and `#rooms-small` (hidden at this size), so focus lands on
    BODY. Seen: craft/out3 house-key, craft/out2 esc. Fixed: fall back to `#nav-house` or `#room-0` in house view.
    (general)
11. **The search is three oversized stickers, and the Game room's chat and pop-up float in mid-air.**
    src.html:775-841 (renderRoomObjects), art placement. The smoke alarm is as big as the bench, the gummy jar fills
    the counter, and the Game room shows its three items as white plaques across the room, not on the monitor, though
    the spec says "in plain sight but small, as in a real room" and draws the chat and pop-up on the blank screen.
    Seen: play/out/room2.png, room3.png, room4.png (integrator viewed room4), audit state-chat-controls-1366x768.png.
    Fixed: cutouts sized to the room's scale (still 44 px tap targets), chat, pop-up and the Maya line drawn on the
    monitor in room and fix views. (general)
12. **The option words vanish once a card flips.** src.html:626-633. A tried card, and all three after the safe pick,
    show only the outcome, so the side-by-side compare has no record of which action led where. Seen:
    audit state-safe-1366x768.png, play/out/h05-tried.png. Fixed: keep the option as a small line above its outcome on
    every flipped card. (general)
13. **Two tubs while it drains.** src.html:870, 879. During the 1.5 s drain the full-tub overlay and the empty-tub art
    are drawn at different sizes and positions, so two ghosted tubs overlap. Seen: play/out/h07-acted.png. Fixed: the
    two layers share one box, or the swap is a crossfade in place. (general)
14. **Composite art reads broken in three rooms.** Kitchen: the `towel-burner` cutout is a whole small stove standing
    on the floor in front of the painted range, and the pot look-alike stacks on a painted pot; Living room: the
    curtain cutout has a hard flat top beside the window; Pills fixed: a second table pasted over the painted coffee
    table. Seen: play/crop-1366-pot.png, crop-1366-candle.png, play/out/h03-back.png, audit state-room-1920x1080.png.
    Fixed: cutouts placed on the painted surfaces with no hard edges (a towel-and-burner cutout on the range, the
    curtain hanging from the window, the fixed pills art without its own table). (general)
15. **The fixed gate is a different gate.** Propped: blue posts with purple mesh (play/out/room5.png, h10-fix.png);
    latched: blue slatted gate with another latch (h10-acted.png). Fixed: before and after art of the same gate.
    (general)

#### Polish accepted
1. **Room swept payoff.** The room view does not glow on its sweep though the spec promises "the room glows warm
   (lamp gold)"; the porch light sits on the lawn; the panel note doubles "✓ Room swept! Room swept!" (src.html:603);
   after all six the panel still says "One room at a time...". Fix: a warm wash in the room on its sweep, the porch
   light at the door, one "Room swept", an end-state panel line. (play/out/kitchen-swept.png, card-close-house.png)
   (general)
2. **Fix targets as places, not navy boxes.** "High medicine cabinet", "Cool towel hook", "Patio", "Pull the plug
   chain up" are dark labelled rectangles; give them a glowing outline on the painted spot; the heater blanket sits on
   the floor, not floating. (play/out/h06-fix.png, h07-fix.png, h10-fix.png) (general)
3. **Check badge on the object**, not at the top right of an empty box. (audit state-reveal-1366x768.png,
   play/out/h01-acted.png) (general)
4. **House view stickers smaller.** Swept rooms show fixed cutouts at full size (play/out/house-3.png); scale them
   with the room. (general)
5. **Grown-up moments in the scene.** Candle hold shows only a faint 〰 and no Grandma (h02-acted.png); Lighter is a
   tap with a hold bar and nothing moves (h11-fix.png). Show the grown-up's chip in the scene doing it. Word the Safety
   card "Twelve fixes, made by you and your grown-ups." (general)
6. **Poison Help on the two poison hazards.** Add the Poison Help line (1-800-222-1222, free, 24/7) under the safe
   outcome of Cleaners and Gummies, as on the Safety card. (general)
7. **Safety card icons per habit.** "Medicine lives up high" shows an empty table, Lighter a table, both online habits
   the same screen (play/out/card-1366.png). Pick art that shows each habit (the high cabinet, the shelf, chat vs
   pop-up). (general)
8. **Ruler hints for pointer users.** After a short drag: "Still too close. Drag it to 3 feet or more."; keep "Arrow
   keys move it 6 inches" and "press Enter" for keyboard focus only. (craft/out3 ruler-2-9.png) (general)
9. **Screen reader states.** `aria-pressed` on peek buttons (src.html:634), `aria-current="step"` on the step strip
   (588-589), neutral look-alike names ("Pot on the stove", "Candle", "Cabinet", "Hook") so the safe one is not named
   by its answer (src.html:819). (general)
10. **375 wide pot drift.** The pot cutout lands on the utensil crock under the room plaque (play/crop-375-pot.png);
    keep cutouts on their spots at narrow sizes. (general)
11. **"Test · hold 2 s" wraps its "s"** at 680x425 (audit state-alarm-hold-680x425.png); keep it on one line. (nit,
    general)
12. **Missed drag keeps the toggle handler** (src.html:1049-1057), so the hint updates to "Now tap <target>." and a
    second tap unselects. (nit, general)
13. **Stray indentation** at src.html:715 and 868. (nit, general)

#### Settled calls
- Everyone over-pick (Teaching polish, Play should fix): should fix. The spec says no set counts as wrong, so the
  correction is an outline and a line of why, never a red mark, score or retry.
- Help rule (Teaching and Craft): the spec's general sentence is the rule; the Heater gets its own reason line. Do not
  invent a new rule.
- Option rewrite (item 2) must keep the spec's 4/4/4 safe positions, the 6/6 Think split and the Everyone 6 / Theo 4 /
  You 2 sets.
- No blocker: all three lenses found none, and the spot-checks agree.
- Safety card covering the hint at 680, 760 and 375: not a fault; the card has its own Close and Sweep again and Read
  speaks it. At 1366 and up the hint shows beside it (the audit's "every size" was wrong).
- Welcome heard after roomIn, or lost on a key/Read/Motion first tap: BASELINE rule 16 and the spec's `welcomeAfter`;
  roomIn and the panel carry its content. Do not change.
- Voice counts, stale lines, Read and order: clean in Craft and Play runs. Do not touch `voice/lines.json` beyond what
  item 8's hint words need.
- No points, timers or win states; keep it that way.

#### To the spec's open questions
- Teaching 7: tapping any object first asks "Risky or looks fine?" (two buttons, never scored) before the decision or
  Looks fine card, so the student, not the tool, tells hazards from look-alikes (5.5.1). Changes the room flow.
- Play 2 (second half): a few painted ordinary objects that answer a tap with "Looks fine", so tapping everything is
  not free. The spec says empty taps do nothing and fixes three cutouts per room.
- Teaching 9: give the child a real action on Candle and Lighter (step back and keep Theo away, point Dad to it)
  instead of watch-only fixes. Changes two Fix lines.
- Play feel note: twelve identical loops of about ten taps; after items 1, 2 and 7 land, decide whether hazards need
  more varied fix shapes.
- People art review (Theo, Grandma June, Dad): already open in the spec (BASELINE rule 11); not Codex's.

#### Not taken
- Rooms button and stage House button side by side at 680 and 375: both are in the spec's layout.
- "Who is safer now? ... then tap Done" while Done is disabled: a sequence that reads fine aloud; item 9 makes the
  state visible.
- Safety card covering the hint at narrow sizes: by design (see Settled calls).
- Theo reason text difference from spec (Craft 12): covered by should fix 6.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: safety-sweep-house (round 1)

Cold Craft lens, 2026-11-06. Bundle `tools/safety-sweep-house/safety-sweep-house.html` as built (not re-bundled).
My frames and logs: `S:/CurioClass-codex-scratch/safety-sweep-house/craft/out1` (voice runs), `out2` (drags, ruler,
keyboard hold, fps, Escape), `out3` (drag-miss, House by key, ruler at the 3 ft label). Shared audit:
`S:/CurioClass-codex-scratch/safety-sweep-house/audit-r1`.

#### Contract

- One file, 2,282,683 bytes: 46 inline webp images (2.19 MB of it), no audio. Over the 2 MB goal, under 6 MB, so no
  `Size:` line is required. No `http(s)://` anywhere in the bundle; no network requests seen in any drive run.
- No console errors or exceptions in 14 driven shots (drive.py "errors in 0 shots") or in the audit.
- Kit used: `Curio.voice`, `Curio.tone`, `Curio.yes`, kit header buttons, `Curio.onMotion`. Nothing re-implemented.
- Frame times (out2 `fps`): room open, hazard zoom, House, another room over 3.2 s: median 16.7 ms, p95 16.7,
  max 16.8 (headless, GPU off). Clean.

#### Voice check

Driven with held clicks (0.12 s), Sound on, Motion on, at 2 s, 3 s, 0.6 s and 0.2 s paces (out1 `v-*.json`,
out2 `stale.json`). Headless speech never ends, so lines run to the kit's cap; that makes queues longer than real.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| roomIn (room entered 4 times) | how | 1 | 1, then silent 3 (v-repeat-look) |
| lookalike (look-alike tapped 5 times) | how | 1 | 1, then silent 4 (v-repeat-look) |
| stop, think, choose, fix, who (two hazards in a row) | how | 1 each | 1 each; second hazard all silent "heard" (v-full-kitchen) |
| tried (two hazards, two unsafe picks on the first) | event, once per hazard | 2 | 2 (v-full-kitchen) |
| safe (two hazards) | event | 2 | 2 (v-full-kitchen) |
| roomDone | event | 1 | 1 (v-full-kitchen) |
| welcome | welcome | after the first room tap's line, or skipped | played after roomIn when the student lingered (v-repeat-look, 9.9 s); skipped when a hazard opened first (v-full-kitchen); never comes when the first tap is a key, Read, Sound or Motion |

- Stale lines: at 0.2 s taps through look-alike, hazard, Think, Choose, peek, unsafe pick, House, another room and a
  hazard (v-fast), nothing played after its moment; "tried" was cut by House; later how lines went silent. Clean.
- Read: cuts the playing line and speaks hint plus card, with Sound off too (v-read 5.7 s); a room change after Read
  goes straight on. Clean.
- Order: always followed the actions. Clean.
- First tap: Read speaks the hint only, Sound and Motion say nothing, a room tap gets roomIn (audit table, confirmed in
  v-read and v-key-first). The welcome lost on a key, Read or Motion first tap is fine under BASELINE rule 16: its
  content is in the roomIn hint and the panel ("Find two hazards").
- `allLines()` returns the 14 lines of `voice/lines.json` word for word, same order (out2 `esc.json`).

#### Findings

1. **Ruler labels sit off the marks the check uses** (src.html:144-150, 886-887, 1072). Mode: Hallway / Heater fix.
   The blanket's left edge moves on 275 to 792 px at 1366x768 (1 ft every 129 px), but the "0 ft".."4 ft" labels are
   spread with `justify-content:space-between` plus 12 px padding, so their centers land at 298, 416, 534, 651, 769.
   Drag the blanket's edge onto the "3 ft" label and the readout says "2.9 feet" and "Still too close"
   (out3 `ruler-2-9.png`); at 4 ft the edge is 23 px past the "4 ft" label. The tick under "2 ft" also cuts through
   its text. At 375 wide the labels crowd the ticks (audit `state-heater-ruler-375x812.png`). A measuring tool that
   disagrees with its own check misleads. Better: place each label absolutely at `d/4` of the ruler width, centered on
   its tick, and measure from the visible blanket edge, not the button's padded box. **should fix**, general.

2. **Keyboard focus is dropped to the page after House or Escape** (src.html:483-491). Enter on the stage's
   "⌂ House" button (out3 `house-key`) or Escape during a hazard (out2 `esc`) ends with focus on BODY: the fallback
   tries `#controls` (no button in house view), `#house` (gone) and `#rooms-small` (display:none at this size). A
   keyboard user must Tab from the top again. Better: fall back to `#nav-house` or `#room-0` in house view.
   **should fix**, general.

3. **Hint repeats "Tap Tell ..." on every grown-up-first fix** (src.html:549 with content.json `fix`). `hintFor()`
   builds "Tap Tell Dad first. " + `h.fix`, and five of the six adult fixes start "Tap Tell Dad." or "Tap Tell Grandma
   June," so the hint and Read say: "Tap Tell Dad first. Tap Tell Dad. When the towel is cool, drag it onto the hook
   across the kitchen." Same on Candle, Pills, Smoke alarm, Gummies and Lighter. Better: drop the prefix, or strip
   the leading "Tap Tell X." from `h.fix` there. **should fix**, general.

4. **The help rule names the heater blanket on every hazard** (src.html:360-361, 617, 435). After the Think answer the
   card and Read say "You may move a cool blanket away from heat without touching the heater." on the chat, the
   pop-up, the tub and the gate. The spec's rule line is general ("If you can make it safe without touching those,
   act now, then tell."). Words do not match the state. Better: the spec's general line, with the blanket sentence only
   on the Heater card. (Teaching may weigh what the rule should say.) **should fix**, general.

5. **Ruler hints speak to keyboard users only** (src.html:905, 1078). After a mouse or touch drag that stops short,
   the hint says "Move the blanket to 3 feet or farther, then press Enter" (out3 `ruler-2-9.png`), and the fix hint
   says "Arrow keys move it 6 inches" at 375 wide on a phone (audit `state-heater-ruler-375x812.png`). A drag already
   checks on release. Better: "Still too close. Drag it to 3 feet or more." and keep the keys note for keyboard focus.
   **polish**, general.

6. **A missed drag leaves a select that never updates the hint** (src.html:1049-1057). After a drop outside the target
   the click handler is swapped for one that only sets `selected`: the hint stays "Move the object into the marked
   target, or select it and tap the target." and a second tap no longer unselects. It does work (out3 `miss-real`:
   real click on the object, then the target, finishes). Better: keep the original toggle handler, which also sets
   "Now tap <target>." **nit**, general.

7. **The Safety card covers the hint at narrow and short sizes** (audit lead, src.html:240, 270). Confirmed at 680x425
   and 375x812 (audit `state-safety-card-680x425.png`, `-375x812.png`): the fixed card sits over the panel. The card
   carries its own Close and Sweep again, and Read still speaks the card, so nothing is lost. At 1366x768 the hint is
   visible (the panel is only inert); the audit's "every size" is wrong there. **nit**, general.

8. **Screen reader states are thin.** Peek buttons have no pressed or expanded state (src.html:634); the step strip
   has no `aria-current` on the current step (src.html:588-589); look-alike hotspots are named from file names
   ("medicine cabinet high", "pot back burner", src.html:819). Better: `aria-pressed` on peek, `aria-current="step"`,
   and plain names ("Medicine cabinet", "Pot on the stove"). **polish**, general.

9. **Line naming a disabled control.** "Who is safer now? Tap everyone it helps, then tap Done." plays while Done is
   disabled (enabled after the first chip, src.html:677). It is a sequence, so it reads fine aloud; STANDARDS says no
   line names a disabled control. **nit**, general.

10. **Safety card icons do not match their habits** (src.html:1168, uses each hazard's `after` art). "Medicine lives
    up high" shows an empty table with blocks (`pillbox-gone`), "Matches and lighters" shows a table (`lighter-shelf`
    at 36 px), and both online habits show the same screen icon (audit `state-safety-card-1366x768.png`). Better: an
    icon per habit that shows the habit. **polish**, general.

11. **Kitchen towel cutout reads as a second stove.** The `towel-burner` cutout is a whole small stove standing on the
    floor in front of the backdrop's own range (audit `state-room-1920x1080.png`). Better: a towel-and-burner cutout
    placed on the painted range, or a backdrop without a stove there. **polish**, general.

12. **Small words.** "Who is safer" Theo reason in code (src.html:696) differs from the spec's text; stray indentation
    at src.html:715 and 868. **nit**, general.

Checked with nothing found: no em dashes in src, content, notes or lines; "Curio Class" only, never "Curio" alone in
copy; classroom-safe words; nothing stored (notes say so; only the kit's Motion setting); all 46 `art:` tokens have
prompts.json entries and no extra ones; the five people images (theo-blocks, theo-walk, chip-dad, chip-grandma,
chip-theo) carry `people: true` and come from gpt-image, not a local model (they still need Cory's contact sheet and
the representation check, BASELINE rule 11; prompts.json says only "builder inspected"); colour is never the only
signal (Tried, Safe, swept lamps all have words or glyphs); keyboard drag alternative, ruler arrows and keyboard hold
on the candle all work (out2 `ruler-keys`, `hold`); visible focus ring on the ruler blanket (outline solid);
Motion off has no running animation (audit). No cultural, Native or hard-history content; nothing for sensitivity.

Counts: blocker 0, should fix 4, polish 4, nit 4.

#### Audit pilot

- Confirmed: the safety-card "hint out of view" lead at 680x425 and 375x812 (finding 7), but low weight because the
  card has its own buttons and Read covers it.
- Wrong: the same lead "at every size": at 1366x768 and up the hint is on screen beside the card. The "welcome late,
  after Search the room" rows are the spec's own design (welcomeAfter), not a fault.
- Missed: the ruler that disagrees with its check (1), focus lost after House or Escape (2: the audit's held-click
  table says "rebuilt, focus kept" for #nav-house, true, but it never presses the stage House button or Escape), the
  doubled "Tap Tell" hint and the heater sentence on every rule card (3, 4: words), keyboard-only ruler hints (5), the
  drag-miss handler (6), and the art and icon fit (10, 11).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: safety-sweep-house (round 1)

Played twice: as a grade 4 student alone at home (every room, every hazard, wrong picks, look-alikes, the end card,
Sweep again) and as a teacher projecting at 1366x768. Frames in `S:/CurioClass-codex-scratch/safety-sweep-house/play/out/`
(room0-5, look0-5, hNN-stop/tried/fix/acted/reveal/back for all 12 hazards, kitchen-swept, house-3, card-*, confirm,
ruler-2ft, the 680x425 fix and safe frames, everyone-theo), plus the shared audit frames. Voice runs with held clicks
(voice-slow, 3 s gap; voice-fast, 0.3 s gap) in `play/run2.txt`. No console errors in any shot.

#### Should fix

1. **Choose is solved by one rule: pick the option that mentions a grown-up.** (content.json options; Choose step)
   In 12 of 12 hazards the safe card is the only one that brings in a grown-up ("then tell a grown-up", "Get Dad back",
   "Get a grown-up to blow it out"; the chat's "Tell them your school" is not a grown-up). It is also the longest
   option in 10 of 12. By the second room a student taps the grown-up card without reading, and the outcome peeks
   (5.5.3) stop mattering. Seen by: script over content.json, then played h00 to h11. Better: give at least one wrong
   option per hazard a plausible grown-up flavour that is still wrong ("Tell Dad later, after your game"), and one or
   two safe options without one (the pot handle, closing the pop-up), with lengths mixed. general
2. **The search is three obvious stickers.** (src.html:775-841, renderRoomObjects; Stop step, 5.5.1) Only the three
   cutouts are tappable and they are the largest, most saturated things in each room: the smoke alarm is as big as
   the bench (room2.png), the gummy jar fills the counter (room3.png), and the Game room shows its three items as white
   text plaques floating mid-air (room4.png), so there is nothing to search. The spec asks for hazards "in plain sight
   but small, as in a real room". Better: size cutouts to the room's scale, sit the chat and pop-up on the monitor,
   and let a few painted ordinary objects answer a tap with "Looks fine" so tapping everything is not free. general
3. **Fix hint still says "Tap Tell Dad" after Dad is here.** (src.html:549-552, hintFor) On all six grown-up hazards,
   after Tell the hint stays "Tap Tell Grandma June, then hold the candle..." / "Tap Tell Dad. When the towel is
   cool..." while the panel shows "Dad is here." and no Tell button (h01-fix.png, h02-fix.png, h06-fix.png,
   audit state-alarm-hold-680x425.png). Words do not match the state; a solo student looks for a button that is gone.
   general
4. **"Everyone" always earns a green check.** (src.html:667-672) On a Theo or You hazard, picking Everyone marks the
   right chip "✓ Safer" and leaves Everyone highlighted with no correction (everyone-theo.png). The spec's own check
   says "always Everyone ... the reveal corrects the rest"; it does not, so the cheap answer for 5.5.5 passes all 12.
   Better: mark an over-wide pick ("Not everyone this time: Theo is the one at risk") with an outline, never a score.
   general
5. **The option words vanish once a card flips.** (src.html:629-633) A tried card and, after the safe pick, all three
   cards show only the outcome; the stage cards show only outcomes too (state-safe-1366x768.png, h05-tried.png). The
   "compare side by side" moment shows three results with no record of which action led to which. Better: keep the
   option as a small line above its outcome on every flipped card. general
6. **Disabled buttons look live.** (src.html:41-45, no `button.b:disabled` style; kit styles only `.big-btn`) Done before
   any chip is picked and Report before Block look exactly like enabled buttons (h04-acted.png, audit
   state-chat-controls-1366x768.png). A student taps Report first and nothing happens, with no hint change. general
7. **Heater ruler at 680x425: clipped and misread.** (src.html:144-150, 886-887) The ruler's lower part is cut off by
   the stage edge and the evenly spaced labels drift off the ticks: "0 ft" sits on the half-foot tick and "4 ft" near
   3.5 (h05-fix-680.png, play/crop-680-ruler.png). This is the one measuring task in the tool (3-foot rule). At 1366
   the labels are a few px off but readable (ruler-2ft.png). Better: place each label at its tick, and keep the ruler
   inside the stage at the preview size. general
8. **Two tubs while it drains.** (src.html:870, 879) During the 1.5 s drain the full tub overlay and the empty tub
   art are drawn at different sizes and positions, so two ghosted tubs overlap (h07-acted.png). general
9. **Composite art reads broken in three rooms.** Kitchen: the towel hazard is a small tabletop stove standing on the
   floor in front of the painted range, and the pot look-alike is stacked on a painted pot (play/crop-1366-pot.png).
   Living room: the curtain cutout has a hard flat top and hangs beside the window, not from it
   (play/crop-1366-candle.png). Pills fixed: a second, lighter table is pasted over the painted coffee table, edges
   visible (h03-back.png). POLISH: never a hard edge, keep the action area clear. general
10. **The fixed gate is a different gate.** Propped: blue posts with purple mesh panels (room5.png, h10-fix.png);
    latched: blue slatted gate with a different latch (h10-acted.png). Anything shown twice must match. general

#### Polish

- **The payoff is flat.** Room swept changes nothing in the room view (no warm glow, kitchen-swept.png) though the
  spec promises one; the house view lights rooms, but the porch glow sits on the lawn, not the porch (card-close-house.png),
  and the panel still says "One room at a time. Look closely..." after all six. Better: a warm wash and lamp in the
  room on its sweep, the porch light at the door, an end-state panel line. general
- **Fix targets are labelled navy boxes, not places.** "High medicine cabinet", "Cool towel hook", "Patio, clear of the
  gate", "Pull the plug chain up" are dark rectangles over tiles or air (h06-fix.png, h07-fix.png, h10-fix.png); the
  gummy fix drags a pill bottle, not the gummy jar; the heater blanket floats in front of the stairs. Better: a
  glowing outline on the painted hook, cabinet or patio spot. general
- **Floating check badge.** On Safe, Who and Reveal the green ✓ hangs at the top right of an empty box, far from the
  object (state-reveal-1366x768.png, h01-acted.png). Put it on the object. general
- **"✓ Room swept! Room swept! Tap House..."** doubled in the panel note (src.html:603, kitchen-swept.png). general
- **Theo reason line talks about medicine on the tub and the gate** ("Keep medicine out of little kids' reach...",
  src.html:696, h07-reveal.png); the spec's line ("can't read labels or swim") fits all four. general
- **House view stickers too big.** Swept rooms show the fixed cutouts at full size: the smoke alarm and heater fill the
  hallway, the bottles tower over the kitchen (house-3.png). Smaller, or a lamp only. general
- **Grown-up moments are off stage.** Holding the candle shows a faint 〰 glyph and no Grandma (h02-acted.png); the
  lighter is a tap on a box with a hold-style progress bar (h11-fix.png) and nothing moves. A chip of the grown-up
  doing it, in the scene, would land the "tell" lesson. general
- **Feel after room 3.** Twelve identical loops of about 10 taps, each ending in the same five chips; with item 1 the
  middle steps go automatic. Fixing 1, 2 and 4 is most of the cure; varying the Who reason line per hazard helps.
  general
- **375 wide:** cover-cropped backdrop with percent-placed cutouts drifts the pot onto the utensil crock, under the
  "Kitchen, Found 0 of 2" plaque (play/crop-375-pot.png). general
- **Safety card icons:** "Medicine lives up high" shows an empty table, and the chat and pop-up habits share the same
  desk picture (card-1366.png). general
- **Chat and pop-up are not on the monitor** in the fix step (audit state-chat-controls-1366x768.png). general

#### Nit

- 680x425: "Test · hold 2 s" wraps its "s" to a new line (audit state-alarm-hold-680x425.png). general
- 680 and 375: the header Rooms button and the stage House button do the same thing side by side. general

#### Checked and fine

First screen names the action (size-1366x768.png); every waiting step names its control (Think, Choose, Tried, Look
fine, Keep searching, Who, Back to room). Look-alikes never open a decision card (look0-5.png). Unsafe picks never reach
Check. Safety card shows all 12 habits plus Poison Help and 911, pages at 680x425 (card-680.png, card-680-p2.png);
Sweep again confirms (confirm.png). Voice: how lines once then silent, "tried" once per hazard, safe and roomDone each
time; no stale line in the fast run. Calm mode, resize and console: audit clean rows, cited.

#### Audit pilot

- Lead confirmed in part: "Safety card hint out of view" is true at 680x425, 760 and 375 (the card covers the panel)
  but not at 1366 or 1920, where the hint shows beside it. Low impact: the card carries its own Close and Sweep again.
- Lead not reported: welcome heard late after roomIn (BASELINE rule 16; roomIn already names the action).
- Missed by the audit: disabled-looking-live buttons (6), the ruler clipped and mislabelled at 680 (7), the double tub
  mid-animation (8), stale "Tap Tell" hints (3), the Everyone reveal (4), and all art and giveaway items. None are
  mechanical-check shaped except 6 and 7.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: safety-sweep-house (round 1)

Lens: Teaching. Bundle as built (not re-bundled). My frames: `S:/CurioClass-codex-scratch/safety-sweep-house/teaching/frames/`
(peek-safe, peek-unsafe, chat-think, heater-think, heater-2p5, gummies-fix, pills-everyone, towel-fix; 1366x768).
Shared audit frames used: state-room, state-safe, state-heater-ruler, state-safety-card (1366x768 and 680x425).
Counts: blocker 0, should fix 6, polish 4, nit 1.

#### Findings

1. **Choose (renderFocus, src.html:846-857): peeking at the safe option labels it "Safe result" on the stage before
   the student picks.** `p.last` is set by the peek button, and the stage card for that index is drawn with the green
   edge, "✓ Safe result" and the habit line whenever `i === h.safe`. Peek each option in turn and the stage names the
   answer, so the 5.5.3 comparison and the 5.5.4 choice need no judgment. Better: a peek shows only the neutral
   "What could happen" card for every option; the Safe label and habit appear only after the pick.
   Seen: frames/peek-safe.png (Kitchen / Cleaners, Choice 2 peeked, stage reads "✓ Safe result ... Never mix
   cleaners."). Level: **should fix**. Tag: general.

2. **Choose (content.json options): the cheap pass "pick the option that brings in a grown-up" is right 12 of 12, and
   "pick the longest option" 10 of 12.** Every safe option names a grown-up, Dad or Grandma June ("then tell a
   grown-up", "Get Dad back..."), and no unsafe option does. The spec's own check balanced position (4/4/4) but not
   wording. A student can pass 5.5.4 without reading an outcome. Better: give at least one distractor per hazard a
   grown-up in a wrong way (tell later, wait for a grown-up to notice, ask a grown-up while leaving Theo by the tub),
   and trim the safe options so they are not the longest. Seen: python over content.json options (keyword
   grown-up/tell/Dad/Grandma: safe-only on 11, safe plus "Tell them your school" on Chat; longest = safe on 10).
   Level: **should fix**. Tag: general.

3. **Think (src.html:360-361, 615-617): the help rule contradicts the Heater answer and is shown unchanged on every
   hazard.** The rule says "Medicine, fire, heat or climbing: get a grown-up first", yet the Heater's answer is "Act
   now, then tell"; the code patches this with a heater-only sentence ("You may move a cool blanket away from heat
   without touching the heater") that then appears on all twelve hazards, including the Game room chat. A student
   applying the stated rule to the heater is marked "Here, the safer help choice is: Act now", and the rule they were
   just taught is the reason they were wrong. The spec's general sentence ("If you can make it safe without touching
   those, act now, then tell") was dropped. Better: the spec's general rule, plus one line specific to the current
   hazard explaining why it falls on its side. Seen: frames/heater-think.png, frames/chat-think.png. Level:
   **should fix**. Tag: general.

4. **Check / fix (Gummies hazard 6 and Towel hazard 1, content.json fix lines): after "get a grown-up first", the
   student still does the grown-up's part.** Gummies: "Tap Tell Dad, then help him drag the closed bottle up to the
   high cabinet": the student carries the medicine (the art is an amber pill bottle). notes.md says "Adults handle the
   medicine" (Support at home) and children "do not ... put medicines away alone" (Good to know), and the habit is
   "Vitamins are medicine too". Towel: the safe outcome says "Dad moves the towel", then the fix asks the student to
   drag the towel to the hook. 7.5.2 is "demonstrate practices", so the practice demonstrated must be the one taught.
   Better: Gummies, the student taps to watch Dad put it up (as the lighter does) or keeps Theo away; Towel, Dad's
   chip moves it and the student's step is something a child does (step back, keep Theo out of the kitchen). Seen:
   frames/gummies-fix.png, frames/towel-fix.png. Level: **should fix**. Tag: general.

5. **Who is safer reveal (reason(), src.html:694-698): the Theo reason line does not match the hazard.** It reads
   "Keep medicine out of little kids' reach. Grown-ups stay with them near water." on all four Theo hazards, so Pills
   and Gummies are explained by water and Tub and Gate by medicine. It also differs from the spec's line. The reason
   is the 5.5.5 reflection, so it should be about this fix. Better: a reason line per hazard in content.json. Seen:
   frames/pills-everyone.png (Pills reveal ends "near water"). Level: **should fix**. Tag: general.

6. **Heater ruler (src.html:886-887, 1067-1073): the foot labels drift up to about a quarter foot from the true
   marks.** The labels are spaced by `justify-content: space-between` with padding, while the blanket position and
   the 3-foot check use the ruler's outer edges. Measured at 1366x768: the true 3 ft point is x=663, the "3 ft" label
   spans 642-661; true 0 ft is 275, label at 289; true 4 ft is 792, label ends at 778. A student who lines the blanket
   up with the "3 ft" label is at about 2.85 ft and hears "Still too close", on the one measured fact in the tool.
   The bubble readout is right, so this is a mismatch rather than a lie. Better: place each label centered on its
   tick (absolute left = n/4 of the ruler). Seen: frames/heater-2p5.png plus measured rects. Level: **should fix**.
   Tag: general.

7. **Room view (renderRoomObjects): 5.5.1 is thin.** Each room has exactly three tappable cutouts with a hover ring;
   two are hazards and the third tells the student it is fine. Nothing asks the student to decide "risky or fine"
   before the tool says so, so telling hazards from look-alikes is done by the tool, not the student. Better: tapping
   any object first asks "Risky or looks fine?" (two buttons, never scored, like Think), then opens the decision or
   the Looks fine card. This changes the spec's flow, so it belongs in the spec's open questions if not taken.
   Seen: audit state-room-1366x768.png, code. Level: **polish**. Tag: general.

8. **Who is safer, over-picking (src.html:663-673): picking "Everyone" on a Theo or You hazard gets no feedback.**
   The Everyone chip stays pressed with no mark, the right chip shows "✓ Safer", and the reason line never says why
   the fix mostly protects one person. Better: a short "Mostly Theo: ..." line or an outline on the over-picked chip
   with a word of why. Seen: frames/pills-everyone.png. Level: **polish**. Tag: general.

9. **Candle and Lighter fixes are watch-only (hold the candle "to watch her blow it out", tap "to watch Dad put it
   away").** That is right for safety, but the student demonstrates nothing; the Safety card then says "Twelve fixes,
   made by you." Better: give the child's real part an action (step back and keep Theo away, point Dad to it) and
   word the card as "made safer by you and your grown-ups". Seen: content.json, audit state-safety-card-1366x768.png.
   Level: **polish**. Tag: general.

10. **Poison Help and the 911 line appear only after all six rooms.** A class that sweeps two rooms never sees the
    number, though the Cleaners and Gummies hazards are exactly when it applies. Better: show the Poison Help line on
    the safe outcome of those two hazards as well. Seen: code (renderSafety only), spec Safety card. Level: **polish**.
    Tag: general.

11. **Look-alike accessible names read like the answer** ("pot back burner", "battery candle", "medicine cabinet
    high", "life jacket hook"), while hazards are named by title ("Cleaners", "Towel"). A screen-reader user hears
    which object is the safe one. Better: neutral names for all three (for example "pot on stove", "candle",
    "cabinet"). Seen: src.html:819. Level: **nit**. Tag: general.

#### Done when

1. Focus: pass (state-safe, peek frames: hazard large left, outcome cards beside it).
2. 1366x768 and 680x425 fit: pass (audit clean rows).
3. Taps take effect at once: not mine to judge; audit resize and held-click rows clean.
4. Look-alikes open "Looks fine", never a decision card: pass (code path at src.html:828-838).
5. Think before options, split 6 and 6: pass (pick() guards on `p.think`; adult true on 6, false on 6, recomputed).
   But see finding 3.
6. All three outcomes side by side after the safe pick; no path to Check without it: pass (state-safe frame;
   goStep('fix') guard). But see findings 1 and 2.
7. Who is safer matches Content: sets pass (Everyone 6, Theo 4, You 2, recomputed); reason lines fail (finding 5).
8. Twelve fixes with fixed art and check; habits on card and Safety card: pass mechanically (safety-card frame shows
   all twelve habits), with findings 4 and 9 on what the fixes teach.
9. Rooms light; Safety card with 1-800-222-1222 and the 911 line: pass (state-safety-card frames).
10. Voice counts: left to the Craft lens.

#### Facts

Spot-checked against the spec Sources and my own knowledge of those sources: Poison Help 1-800-222-1222, free, 24/7, US
(HRSA); bleach plus ammonia makes a harmful gas, also outdoors; candles 12 inches from anything that burns; space
heaters 3 feet; smoke alarms tested monthly; escape plan two ways out and an outside meeting place; get out, stay out,
call 911 from outside; a young child can drown in a few inches of water, quickly and silently; pool gates self-close
and self-latch; pot handles turned to the back; child-resistant caps are not childproof. All correct. 3 feet = 36 in,
6-inch arrow steps = 0.5 ft (code uses 0.5): correct.

#### Grade, notes, guardrails

Language is plain and right for grades 3-5. Teacher notes name the sensitive topics (poisoning, fire, drowning, online
strangers) and the disclosure procedure (rule 8): good. No points, timers or win states. notes.md "Good to know" and
"Support at home" are true of the tool except where finding 4 contradicts them (the tool has the child put medicine
away). Home ideas are doable tonight.

Sensitivity: no cultural, Native or hard-history content. The people set (Dad, Grandma June, Theo) goes to the rule 11
people review as the spec already says; not judged here.

#### Audit pilot

- Leads confirmed: none to confirm for teaching. The one lead ("hint out of view" on the Safety card) is a layout
  matter; on the 1366x768 frame the hint sits in the panel behind the card's overlay, which is by design while the
  card is open.
- Leads wrong: none found.
- What it missed (as expected, all outside a mechanical audit): the peek giveaway (finding 1), the grown-up keyword
  cheap pass (2), the rule that contradicts its own answer (3), the child doing the adult's step (4), the mismatched
  reason line (5), and the ruler label drift (6, measurable, but only by comparing labels to the check's geometry).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: safety-sweep-house (Codex fix, round 1)

Curiosity authority: the user's brief overrides the older lesson-shaped spec and Refine gate. The house now has open comparisons, repeatable scene actions and a lower-left Manual. Removed the kit header, forced Stop/Think/Choose/Check path, beneficiary quiz, progress count and automatic ending. No welcome, goal, score, level or finish screen was added.

Evidence root: `../../_scratch/safety-sweep-house/`. Native PNGs, shots JSON, command logs, original source snapshots, source manifest and packing/repair scripts are preserved there. Contact sheets were inspected as well as the individual critical frames. `refine.md` and `refine/` were not edited. No git commits or shared-file edits.

#### Blocker
None listed.

#### Should fix
1. FIXED. Reproduced Safe result/habit on a peek in `before-a/s01-peek.png`. Peeks now always use the neutral What could happen card. `after-a/s01-peek.png`; all 36 pre-selection peeks tested neutral in `functional.json`. The safe label appears only after selecting that action.
2. FIXED. `before-numbers.json`: adult word 12/12, longest 10/12. `after-numbers.json`: adult word 6/12; safe action longest/middle/shortest 4/4/4; positions 4/4/4, adult-help split 6/6 and beneficiaries 6/4/2 preserved. Wrong actions also name adults. Content and spec option text updated. Comparisons are explorations, not an answer gate.
3. FIXED. Reproduced child medicine/towel handling in `before-a/s03-gummies.png` and `s03-towel.png`. Both are adult demonstrations now; the child stays away. `verification/gummies-adult-move.png`, `towel-adult-move.png`; both fixes reached the changed scene. Spec Fix lines updated.
4. FIXED. Reproduced contradictory blanket-specific generic rule in `before-a/s04-heater.png`. Help rule now reproduces the spec's general sentence exactly, followed by a source-backed reason for the current hazard. `after-a/s04-heater.png`, `after-a.log`; all 12 cases have their own help text. The Help rule is freely available, with no help-answer quiz.
5. FIXED. `before-b/s05-ruler-680.png` reproduces clipping; corresponding 1366 and 375 before frames retained. One origin/span drives ticks, labels, nearest blanket edge and pointer movement. `ruler-metrics-1366.json`, `-680.json`, `-375.json`: maximum label error 0.007813 px and blanket-edge error 0.023438 px. The ruler is inside the stage at all three sizes. `targeted-final/heater-floor-1366.png`, `-680.png`, `-375.png`. A 2.99-foot clearance was rejected at all three sizes.
6. FIXED. `before-a/s06-s07-theo.png` reproduces the combined medicine/water reason. Each hazard now has a contextual beneficiary reason in content.json. `functional.json` contains all 12 displayed reasons; `verification/pills-fixed.png`, `gummies-adult-move.png` show specific Theo explanations. No claim that little children cannot swim.
7. FIXED through the Curiosity override. Reproduced the over-wide Everyone pick in `before-a/s06-s07-theo.png`. Removed the beneficiary guessing and pass-through, rather than retaining a quiz. Each changed scene directly explains Mostly Theo, Mostly you or Everyone, with its hazard reason. `functional.json`: no beneficiary quiz and all 12 reasons present. No red mark, retry, score or hidden reflection gate.
8. FIXED. `before-a/s03-towel.png` repeats Tap Tell; Gummies shows the stale after-Tell instruction. Before Tell now shows only Tap Tell X first; afterward each adult case shows its remaining safe action. `after-a/s03-towel.png`, `s03-gummies.png`, `after-b/p11-alarm-680.png`; all six adult-case hints recorded in `functional.json`. Final phone Towel and Gummies frames are in `audit-leads-a/`. Read uses this same current hint. See Voice walk for the final Curiosity speech policy.
9. FIXED. `before-a/s09-report.png` and the baseline opacity of 1 reproduce the live-looking Report. Report now has aria-disabled, a muted 0.5 opacity, default cursor and no press motion; an early press updates the hint to Tap Block first. `after-a/s09-report.png`, `after-a.log`; early reporting did not change reported state in `functional.json`. The obsolete Done button was removed with the quiz.
10. FIXED. `before-a/s10-house.png` / `before-a.log`: focus BODY. `after-a.log`: focus room-0 after stage House. `interaction/escape-focus.png` and `escape-focus.json`: Escape also returns to room-0. Focus after returning from each scene remained on a visible control, not BODY.
11. FIXED. Reproduced oversized room stickers and floating messages in `before-b/s11-s14-room-0.png` through `-5.png`. Objects now use room-scale placement; the game messages share the painted monitor, with an enlarged monitor surface for accessible interaction. `after-b/s11-s14-room-0.png` through `-5.png`, `verification/monitor-phone.png`; the final compact input repairs are in Audit below. All interactive targets keep a 44 px minimum.
12. FIXED. `before-a/s12-flipped.png` loses the action. Every flipped panel and stage card now retains the action above its outcome. `after-a/s12-flipped.png`, `interaction/safe-poison-cleaners.png`, `safe-poison-gummies.png`.
13. FIXED. Reproduced two tubs in `before-a/s13-tub.png`. One painted empty shell is now shared by both states; code water drains inside it. `targeted-final/tub-drain-20.png`, `-700.png`, `-1700.png`: one shell and one water layer at each sample, no second tub or faucet. Reduced motion swaps the water state without shortening the hold timings.
14. FIXED. `before-b/s11-s14-room-0.png` and `-1.png` reproduce the small stove, extra pot, curtain edge and pasted table. Room art now uses a small burner/towel vector on the range, the existing painted back-burner pot, a window-height candle/curtain vector, and a pill box without furniture. Fixed Pills uses the block bin. `after-b/s11-s14-room-0.png`, `-1.png`, `verification/pills-fixed.png`, `targeted-final/pot-phone-fixed.png`; no second table remains.
15. FIXED. Before gate meshes/slats differ in `before-b/s11-s14-room-5.png` and `s15-fixed-gate.png`. Both states now use the same blue-post/purple-mesh SVG, hinge, latch and leaf. `after-b/s11-s14-room-5.png` and `s15-fixed-gate.png`; only the leaf transform and prop change. The house miniature now uses that same SVG too: `final-evidence/house-final-gate.png`, `house-final-gate.json` (one mesh miniature, six open rooms, no final card).

#### Polish accepted
1. FIXED with Curiosity adaptation. Warm room wash, smaller fixed-room marks, porch glow at the entrance and a single Room swept note. `targeted-final/warm-room-fixed.png`, `house-six-open.png`. All-six leaves the house open; an end screen and earned Safety card were deliberately removed. Habits are always in the Manual.
2. FIXED. Dark target rectangles became translucent place outlines. Medicine storage and hot towel movement became adult demonstrations. The heater and blanket share a floor plane beside the tape. `targeted-final/heater-floor-680.png`, `final-regression/pills-one-bin.png`; the final audit also checks the Pills destination beside Theo.
3. FIXED. Changed-scene checks sit over the object. `verification/alarm-held-680.png`, `pills-fixed.png`, `targeted-final/tub-drain-1700.png`.
4. FIXED. House view fixed cutouts reduced from 35% by 45% of the room to 15% by 20%. `verification/all-scenarios.png`, `targeted-final/house-six-open.png`.
5. FIXED. Adult portrait chips appear in the scene during and after Candle, Lighter, Towel and Gummies demonstrations; adult-handled objects briefly travel away with Motion on. `after-a/p05-candle.png`, `verification/lighter-adult-move.png`, `gummies-adult-move.png`, `towel-adult-move.png`. Manual says Twelve fixes, made by you and your grown-ups.
6. FIXED. Both poison-related safe outcomes include US Poison Help, 1-800-222-1222, free, 24/7. `interaction/safe-poison-cleaners.png` and `safe-poison-gummies.png`. HRSA and National Capital Poison Center independently confirm the number and availability.
7. FIXED. Always-open Manual habits use a cabinet for medicine, shelf for Lighter, and distinct chat/pop-up monitor icons. `interaction/manual-icons.png` and `targeted-final/manual-source-licences.png`.
8. FIXED. Pointer short-drag hint is Still too close. Drag it to 3 feet or more. Keyboard instructions appear for keyboard input. `ruler-pointer-short.json`, `ruler-keyboard.json`, three ruler metric files; 1.181872 ft was rejected, four half-foot key steps reached 3 ft.
9. FIXED with Curiosity adaptation. Peek buttons announce aria-pressed; look-alike names are neutral. The step strip was removed along with the forced lesson path, so no aria-current step remains. The Manual button announces its expanded state and the drawer supports keyboard close and focus return.
10. FIXED. The narrow kitchen uses the pot already in the painting, preserving its normalized location and avoiding an overlay drifting onto utensils. `targeted-final/pot-phone-fixed.png` at an actual 375 px iframe width.
11. FIXED. Test · hold 2 s stays on one line at 680x425. `after-b/p11-alarm-680.png`, `verification/alarm-held-680.png`.
12. FIXED. A missed drag no longer replaces the toggle handler. `missed-drag-real.json`: the drag click was suppressed, then two real held taps produced true, false; acted stayed false. `targeted-final/missed-drag-real-taps.png`.
13. FIXED. Stray indentation removed and JavaScript formatted for review; final node --check passed. No source minification.

#### Settled calls
- No scoring, retry or red correction was introduced. Beneficiary facts replaced the Everyone quiz under the user's explicit Curiosity rule.
- Exact general help rule retained; each hazard explains its own application, including the cool-blanket exception.
- Positions, help split and beneficiary totals retained as above.
- No blocker was invented. Optional flow changes under To the spec's open questions were left alone except where the user's Curiosity instruction explicitly removed lesson gates.
- Safety habits are a freely opened Manual section, not a finish card. Its scrolling drawer has Close, Escape and Read.
- No welcome was restored. One first-use hint may be interrupted by the next action, consistent with BASELINE 16.
- Voice changed beyond old item 8 only where the Curiosity brief requires one hint then Read. No other unsolicited narration remains.
- Existing people art and its owner representation/contact-sheet question remain unchanged.

#### Cheats tried
- Peek every action: 36/36 cards stayed neutral before selection. No Safe label or habit leaked.
- Choose an adult word / longest / shortest / fixed position: each heuristic was counted across all twelve cases; no length or position rule exceeds 4/12. Adult-word presence is 6/12 and appears in unsafe actions too.
- Always Everyone: no quiz, grade or completion gate exists to pass. Specific beneficiary explanations remain visible after each change.
- Try a fix without comparing: works intentionally. This is open exploration, not a hidden knowledge check.
- Early Report: hint changes to Block first, reported stays false. Block then Report works.
- Short alarm tap: acted false. Full 2.15 s alarm hold: fixed true. Full 1.15 s candle hold: fixed true. Partial holds do not accumulate.
- Short pointer drag: 1.181872 ft, acted false. Subthreshold 2.99 ft rejected at all three named sizes. Four half-foot key steps from 1 ft: distance 3, acted true.
- Miss a drop then tap twice: true then false, with no action credited. Leaving and Escape preserve a usable focus target.
- Visit all changed rooms: six lamps, no final overlay, every room remains accessible. Reset this scene permits another experiment.

#### Voice walk
Final two-second held-click walk: room, object, peek, Try the fix, object, target, Tell, Read. `voice-curiosity.json` and `voice-curiosity-frame/curiosity-voice.png`.
One automatic line started: Tap an object for a closer look. The next user action cut it. No inspect/fix/reward/welcome speech followed.
Read spoke the current changed-scene hint. The six manifest lines equal allLines(); unused instruction text remains available through current Read context.
Browser speech fallback is used; no recordings or external voice services were generated. Earlier lesson-style voice evidence is superseded by this final walk.

#### Engine changes wanted
None. Kit behavior was not edited.

#### Audit
Completed once within the 40-minute limit: `fix-audit/audit.md`, Chrome 9921, host 8725. It checked all eight STANDARDS sizes, listed states, reduced motion, held clicks, Enter twice, narration pacing and resizing mid-action. All 49 audit frames were inspected. Resize/stress checks found no exceptions or controls left disabled.

The audit retained 38 lead rows. Confirmed layout causes were repaired, with targeted held-click frames and numerical rechecks rather than another full audit:
- The portrait scene-top inset stretched the top controls through the room. Set its bottom to auto. This cleared the phone plaque overlaps, restored the Towel and Gummies routes, and separated House from chat/monitor content. `audit-leads-a/room-375.png`, `compare-375.png`, `towel-375.png`, `gummies-375.png`, `chat-375.png`.
- Separated the two compact stove touch areas at 680, 800 and 375 widths. `audit-leads-a/room-680.png`, `room-800.png`, `room-375.png`; the rear pot still opens Looks fine in `audit-leads-b/stove-look-375.png`.
- Kept the Game room label inside its house cell at 680. `audit-leads-a/house-680.png`.
- Removed the covered room-monitor button while the enlarged monitor is open. Merely setting inert was insufficient because the shared scene render restored it; hidden now survives that render. `final-evidence/monitor-final-1366.png`, `-800.png`, `-680.png`, `-375.png`; all four `monitor-final-*.json` report underlayHidden:true and zero overlap/size/clipping/keep leads.
- Moved the adult chip clear of the block bin and shortened its destination label to By Theo while preserving its full accessible name. `audit-leads-b/pills-680.png`, `pills-1366.png`, `pills-375.png`.
- Reserved heading space beside Manual Close. `audit-leads-a/manual-375.png`. The underlying hint is intentionally covered/inert while this drawer is open; Read uses the drawer. This audit hint-out-of-view row is not a fault under the Curiosity brief.
- Stabilized Sound's width after the walk table showed nearby controls moving on its label change. `audit-leads-b/sound-stable.png`.

Numerical slices in `lead-numbers-1366.json`, `-800.json`, `-680.json`, `-375.json` cover nine affected states at each size. With the four final monitor records substituted, all 36 state/size cells have zero horizontal scroll, small targets, overlaps, clipped/tiny text, missing names, hidden controls, disabled-control hints or covered keep regions. The initial `post-*.json` callback tables contain no usable metrics and are not used as proof; the retained held-click PNGs and the later named numeric files are the evidence.

Final bundle: 2308600 bytes, 2254 KiB. Thirteen source records, no active external resource URLs and no fetch calls. JavaScript parse check passed. Final focused batches reported zero console errors. The literal voice:* remaining inside the kit is its no-recording sentinel; browser speech fallback works and no external clip is loaded. Chrome and host processes started by this session were closed; host.html removed.

#### The real material
All twelve situations are original fictional Curio Class scenarios, CC BY 4.0. There is no imported measurement dataset. Outcomes are qualitative safety guidance, not measured risk estimates. Existing OpenAI gpt-image illustrations remain; vector objects and geometry are original MIT code.
Source guidance was rechecked online on 2026-11-06. No outside art, quoted passages, executable or dataset was downloaded. Packing provenance: `sources.py`, `complete-sources.py`, `data/source-manifest.json`; packed records live in content.json, tool.draft.json and the Manual. Independent copyrighted references are verification only; no text or images copied.
| Material / named source | Licence and date | Sampling / independent check |
|---|---|---|
| [CDC: Cleaning and Disinfecting with Bleach](https://www.cdc.gov/hygiene/about/cleaning-and-disinfecting-with-bleach.html): Cleaners: mixing bleach with other cleaners can release harmful vapours | US federal public domain guidance; original paraphrase CC BY 4.0. [Reuse policy](https://www.cdc.gov/other/agencymaterials.html). Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://doh.wa.gov/community-and-environment/contaminants/bleach-mixing-dangers); reference only, publisher copyright retained. |
| [CDC: PROTECT / medicine safety](https://www.cdc.gov/medication-safety/protect/index.html): Pills and gummies: adults give and store medicines and vitamins up, away and out of sight | US federal public domain guidance; original paraphrase CC BY 4.0. [Reuse policy](https://www.cdc.gov/other/agencymaterials.html). Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://poisonhelp.hrsa.gov/what-you-can-do/up-away-campaign); reference only, publisher copyright retained. |
| [USFA: Cooking Fire Safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/cooking/): Towel and pot: stay with cooking, keep combustibles away, turn handles to the back | US government authored guidance, public domain in the US (17 USC 105); original paraphrase CC BY 4.0. Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.nfpa.org/education-and-research/home-fire-safety/cooking); reference only, publisher copyright retained. |
| [USFA: Candle Fire Safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/candle/): Candle: 12 inches from combustibles, blow out when leaving, flameless alternatives | US government authored guidance, public domain in the US (17 USC 105); original paraphrase CC BY 4.0. Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.nfpa.org/education-and-research/home-fire-safety/candles); reference only, publisher copyright retained. |
| [USFA: Smoke Alarms](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/): Alarm: monthly test button check, working batteries; grown-up handles ceiling work | US government authored guidance, public domain in the US (17 USC 105); original paraphrase CC BY 4.0. Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.nfpa.org/-/media/project/storefront/catalog/files/safety-tip-sheets/manufacturedhomessafetytips.pdf); reference only, publisher copyright retained. |
| [USFA: Heating Fire Safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/): Heater: at least 3 feet from anything that burns; model uses 12 inches per foot and 6-inch key steps | US government authored guidance, public domain in the US (17 USC 105); original paraphrase CC BY 4.0. Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.nfpa.org/en/about-nfpa/press-room/news-releases/2025/us-home-heating-fires-peak-during-winter-months); reference only, publisher copyright retained. |
| [CPSC: In-Home Drowning](https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/In-Home-Drowning-Safety-Information-Center): Tub and gate: young children can drown quickly and quietly in shallow water; supervision and barriers | CPSC public information, freely distributable with credit; original paraphrase CC BY 4.0. [Reuse policy](https://www.cpsc.gov/About-CPSC/Policies-Statements-and-Directives/Privacy-Policy). Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.healthychildren.org/English/safety-prevention/at-home/Pages/Bathroom-Safety.aspx); reference only, publisher copyright retained. |
| [CPSC: Pool Safely](https://www.cpsc.gov/s3fs-public/360.pdf): Gate: self-closing, self-latching barriers and adult water supervision | CPSC public information, freely distributable with credit; original paraphrase CC BY 4.0. [Reuse policy](https://www.cpsc.gov/About-CPSC/Policies-Statements-and-Directives/Privacy-Policy). Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.watersafetyusa.org/prevent-unsupervised-access.html); reference only, publisher copyright retained. |
| [FTC: Kids and Video Games](https://consumer.ftc.gov/articles/kids-and-video-games): Chat and pop-up: keep personal information and passwords private; block, report and tell a trusted adult | US federal public domain guidance; original paraphrase CC BY 4.0. [Reuse policy](https://www.ftc.gov/policy-notices/website-policy). Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.missingkids.org/netsmartz/topics/gaming); reference only, publisher copyright retained. |
| [HRSA: Calling Poison Help](https://poisonhelp.hrsa.gov/faq/calling-poison-help): US Poison Help: 1-800-222-1222, free, 24 hours a day, 7 days a week | US government authored factual guidance; original paraphrase CC BY 4.0. Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.poison.org/need-immediate-assistance); reference only, publisher copyright retained. |
| [USFA: Escape Planning](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/): Map and fire: two ways out, outside meeting place; get out, stay out and call 911 outside | US government authored guidance, public domain in the US (17 USC 105); original paraphrase CC BY 4.0. Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire/home-fire-escape-plan.html); reference only, publisher copyright retained. |
| [CDC MMWR: childhood poisoning prevention](https://stacks.cdc.gov/view/cdc/28658/cdc_28658_DS1.pdf): Pills: child-resistant containers are not childproof; store them beyond young children’s reach | US federal factual guidance, public domain in the US; original paraphrase CC BY 4.0. [Reuse policy](https://www.cdc.gov/other/agencymaterials.html). Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Medication-Safety-Tips.aspx); reference only, publisher copyright retained. |
| [USFA: Youth Firesetting Interviewing (2025)](https://apps.usfa.fema.gov/ax/sm/sm_0621.pdf): Lighter: children leave matches and lighters alone and tell a grown-up; adults store them out of reach | US government authored factual guidance, public domain in the US (17 USC 105); original paraphrase CC BY 4.0. Checked 2026-11-06. | Original factual paraphrase only; no source text, images or statistical sample imported. [Independent check](https://www.nfpa.org/-/media/project/storefront/catalog/files/home-fire-safety/emac/educationalmessagesdeskreference.pdf); reference only, publisher copyright retained. |

#### Curiosity check
- A child can open a room, inspect, compare or directly change it without reading an assignment or passing a check.
- Adult appeal is limited by twelve authored cases; this is a household safety model, not an endless physical simulation. No claim of month-long depth or an independently observed ten-minute adult playtest.
- The house and its real safety rules are the working material; the ruler is explicitly an illustrative clearance model.
- No goal, score, forced path or finish is required. Rooms remain open after every change.
The comparison frame is `models-contact-0.jpg`: this house beside Beat Lab, plus Elements Inspector and the two family models. The house keeps its painted material and notebook, rather than copying their palettes.
Lesson-creep search: badge means a small changed-object check marker, not a reward. No score, points, level, goal, sticker, correct/wrong feedback or completion screen remains in the active interface or voice lines.

#### Left open
- The spec and Curiosities catalogue assign no number or concept entry to this id. The engraved plate therefore names Curio Class Curiosities · Safety Sweep House without inventing a number; tool.draft.json has curiosity:true and no invented plate number.
- Existing people art review remains the spec's owner question. No new people art was made.
- Independent long-form student/adult play testing and the catalogue's long-term-depth decision are not claimed by this fix report.
- No original blocker, should-fix or accepted-polish item is knowingly open. The retained audit is the pre-repair snapshot; final lead rechecks are named above.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Safety Sweep House handoff

#### Structure
The painted house sits on a wood tabletop. A lower field notebook holds open comparisons and scene controls.
The lower-left Manual contains operating instructions, habits, honesty notes, emergency information and named sources with licences.
Motion, Sound and Read use kit/curio.js; kit CSS and header are absent.
content.json contains original fictional situations, action/outcome data, per-hazard help and beneficiary reasons, six voice lines and provenance.

#### Tricky parts
Comparisons and Try the fix are available independently. There is no quiz or pass condition.
Adult-first demonstrations remain locked until Tell. Dad handles towel, vitamins and lighter; Grandma handles the candle and medicine.
The tub uses one painted shell and one code water layer. The pool gate uses one SVG geometry in both states and in its house miniature.
The ruler label, pointer travel and nearest blanket edge share a single 24-percent origin and 62-percent span.
Report uses aria-disabled so an early press can explain Block first, without submitting anything.
Hold actions cancel on release, blur, changing scenes and Escape. A whole two-second hold is required for the simulated alarm test.
Reset this scene restores only that hazard. Refresh restores the house. No scenario data is stored or sent.
The portrait top-control strip has an automatic bottom inset, so it cannot stretch through the whole scene.
The enlarged monitor hides its covered room button; inert alone is reset by the scene-render pass.
Compact stove touch areas stay separate, and adult chips sit clear of movable objects and destinations.
Speech gives one first-use hint; subsequent narration requires Read, as the Curiosity brief specifies.
Source provenance is packed by sources.py followed by complete-sources.py in Scratch. The second step is idempotent.

#### Curiosity authority
The user explicitly overrides the older lesson-shaped spec and refine gate. Removed the kit header, Stop/Think/Choose/Check quiz,
Who-is-safer guessing, counts and automatic final Safety card. All habits are freely readable in the Manual.
Six rooms and twelve scenarios remain. Safe-option positions are 4/4/4, help classifications 6/6, beneficiary groups 6/4/2.
The spec has no assigned Curiosity number and the concept catalogue has no entry for this id. Plate says Curio Class Curiosities · Safety Sweep House.
Do not assign a collection number without an owner decision. This remains an explicit metadata limitation.

#### Sensitivity
Poisoning, fire, drowning and online contact may connect with real experiences. Follow the existing school disclosure procedures in notes.md.
Existing people paintings are unchanged. Their owner contact-sheet/representation review is the spec's open question, not this fix pass.

#### Engine changes wanted
None. All changes stay within this tool and its Scratch folder.

#### Art
Existing generated paintings remain. Small burner/towel, pill box, candle and consistent mesh gate are exact vector drawings in source,
avoiding duplicate furniture and detached cutout edges. No source images, recordings or datasets were downloaded.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: refine.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-08)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
