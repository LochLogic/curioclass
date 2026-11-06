# Codex report: safety-sweep-house

## Built
Built in `S:\CurioClass-codex`, with authored files confined to the named tool and scratch folders.
Six painted rooms, twelve hazards, six look-alikes, persistent in-visit decisions, scene fixes, reflection reveals and a final Safety card.
One explore experience, no score, timer, saved progress or network requests. `tool.draft.json` has stage `built`.
Uses the starter, kit frame, Motion, Sound, Read, Curio.voice and tones. No family engine applies.
Readable source was formatted and both pre-format and post-format scripts passed `node --check`.
No git commits, branch operations, shared-file edits, publishing or polish round.

## Numbers check
`_scratch/safety-sweep-house/numbers.json` recomputes the contrast, content distributions and unit conversion.
All twelve contrast ratios match the spec: 14.12, 5.96, 6.42, 7.12, 5.13, 6.69, 6.58, 5.04, 10.18, 11.20, 17.21 and 4.67 to 1.
Safe positions: four each. Grown-up first / act then tell: six each. Safer sets: Everyone six, Theo four, You two.
Three feet is 36 inches; keyboard increments are six inches. The check compares the actual distance before display rounding.
The spec's 72-tap claim omits required steps. An explicit tap-target / keyboard-ruler route here uses 155 inputs, including room navigation.
That model includes the reflection reveal's Back to room, four ruler arrow presses, Enter, and selecting the ruler object. It is not a time estimate.

## Facts checked
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

## Break it
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

## Voice walk
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

## Feel check
Played the entire house through all twelve fixes. The best moment is the last room lighting and the complete house appearing behind the earned Safety card.
The alarm's sustained Test and the separate Block / Report sequence give later rooms a different feel from the first bucket move.
Flat moment one: several generated cutouts were miniature rooms. Redrew ten as isolated objects and re-anchored them in the painted scenes.
Flat moment two: fixes initially swapped art in the old location. Moved the cool towel across the kitchen, alarm to ceiling, medicine and lighter up high.
Also removed a painted chair and blanket from the hallway backdrop so the fixed heater scene actually has open space.
Visual checks found and fixed the compact card crowding, Check falling below the fold, and old tub / gate images persisting with Motion off.
Compared both bar tools. `feel-comparison.png` puts this tool beside Snowy Mail Route. The painted house is richer, and the clipboard fits its world.
The choices remain text-heavy compared with Beat Lab's direct making; that comes from the required decision content. Peeks and scene actions carry the play.

## Done when
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

## Wave lessons
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

## Audit leads
Audit NOT FINISHED. One invocation used port 9991 and host 8795 with a forty-minute outer limit.
The driver's internal sixty-second Chrome protocol timeout occurred in size setup before any audit.md or frames were produced.
No audit leads or clean-audit claim exist. `audit-failure.md` preserves the failure. The cold reviewer must rerun the audit.
An earlier host favicon 404 was fixed with an inline favicon in the tool and temporary host; the two narrow-host reruns had zero errors.

## Frames looked at
All emitted PNGs were opened: both bar frames; house, kitchen and compact early frames; all fourteen full-play frames;
all twelve matrix frames; two clean phone reruns; four repair frames; four final layout frames; final compact-fit frame;
main, side and finale voice frames; fixed Kitchen, Hallway, Bathroom and Backyard frames; final hallway check and interrupted tub / gate frames.
All seven art contact sheets, updated redraw sheets, people sheet and side-by-side bar comparison were also viewed.
Safety-card and fixed-room layout reruns use explicit completed-state fixtures, after the separate full real-input completion run.

## Art made
46 images, five marked people:true. Eleven assets were redrawn or edited during the build; discarded candidates are in scratch.
1609.9 KB of finished WebP art; 2237.2 KB offline bundle; zero KB recorded voice.
The bundle is about 2.2 MB, modestly over the 2 MB goal. Quality is 72, backgrounds 1024 px; all teaching art is retained.
Prompts and raw PNGs are in the art folder; generated sources were copied into the project. Credits name OpenAI gpt-image.
Fresh representation review passed the five family assets. Minor Theo portrait age variation and small key fringes were noted; despill was applied.

## Art still to paint
None. The owner still needs to view the people contact sheet before shipping. No shipping occurs in this session.

## Engine changes wanted
`scripts/drive.py`, HOST: add an inline empty favicon to avoid a spurious missing-favicon console lead from the temporary iframe host.
The workaround stayed in the allowed temporary host file, which was removed. No engine or shared script was edited.

## Left open
- Mechanical audit and its comprehensive resize / focus sweep remain incomplete because of the Chrome protocol timeout.
- Human listening review of browser speech and eventual friendly-dad recordings are deferred. The source lines and logs are ready.
- People contact-sheet viewing before shipping; fresh representation review is complete.
- The built neighbors inspected did not contain handoff.md or refine.md. Their source and both required bar tools were read and opened instead.
- See handoff.md for the compact-layout, art-count, help-rule wording, tap-count and Theo-reason decisions.
- Ports 8795 and 9990 through 9997 were checked closed. No host.html remains. Build only ends here.
