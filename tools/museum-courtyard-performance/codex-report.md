# Codex report: museum-courtyard-performance

## Built

Built the offline Site, Week and Opening night modes: draggable zones and floors, sampled sightlines, two seat views, twelve production actions, six weeks, rehearsal adaptation, dancer load, rain, undo, saving, a 40-second show and printable program sheet.

Final bundle: **1,020,229 bytes**, under 2 MB. Source is 1,604 readable lines, maximum 159 characters. Draft metadata says built. Work stayed inside this tool and its Scratch folder. No commits, branch operations, shared-engine edits or polish round.

The report was started at the first successful bundle and completed after verification. Evidence paths below are under `_scratch/museum-courtyard-performance/`.

## Numbers check

- Independent computation: `numbers.txt`, `prepare.py` and `manual-sample-result.json`.
- The 9 by 9 grid clipped to the ellipse has 49 samples. Arcade ground visibility is 78.50%; balcony examples are 100%, 59.18% and 26.53%.
- Source discrepancy: (10,8) gives 97.96% without spray and 83.13% with spray. At (10,13), spray gives 33.54%, rather than the stated 37%; without spray gives 92.45%. The specified ray model is retained and spec.md is unchanged.
- All actions once plus six rehearsals: $6,300 and 45 h. Sample production: $2,900 and 25 h, leaving $100 and 35 total crew hours.
- Loads: stone full 216, warm 172.8, half 108; marley full 144, warm 115.2; sprung full 72. Marked stone jumps give 64.8.
- Contrast ratios: brand/paper 5.34:1; white/brand 6.12:1; ink/paper 14.01:1; muted/paper 5.98:1.
- Independent sample ground Seen: 99.0136%, 63.2313%, 78.5034%, 89.1837%. All four match the browser model. Balcony Seen and Lit are 100%; Heard is 100% ground, 95% balcony.

## Feel check

Played a six-week held-click student run, an independently checked planned production, and the complete opening-night show. Best moment: comparing low Pool work from the ground and balcony, then seeing the final sheet connect that difference to the production choices.

Flattest moment 1: the initial plan sat in a large empty surround. Added the painted courtyard behind the drawing board, textured stone, directional column shadows, pathways and live fountain ripples.

Flattest moment 2: the first procession camera lost dancers at the edge, and the finale felt static. Cameras now aim at each section; Arrival travels as a procession; Rise shows jump choices and two sequential lifts. The finale camera was widened and raised after a lift frame exposed cropping.

Compared `feel-comparison.jpg` with Beat Lab; Snowy Mail Route was also bundled into Scratch and opened. The painted setting and production desk have comparable visual care. The dancers remain visibly provisional by the owner's decision. Quiet final weeks have less activity when the student has already completed rehearsals; no extra events were invented.

## Done when

1. **PASS, primary layout.** Site plan, Week board and Opening night with both seats dominate at 1366x768 and 680x425. Main controls remain visible. Some secondary report text or floor selection can require panel scrolling in short previews.
2. **FAIL against every printed example.** Most examples match within two points; the behind-fountain spray result differs by 3.46 points. Independent ray computation supports the implemented value above.
3. **PASS.** Crew and money caps, one-time cards and undo verified in `functional-result.json`. Undo restores budget, bookings and the pre-week plan.
4. **PASS for stated load cases.** Two full stone weeks produce injury; warm-up changes loads as computed. Sheet reports five in Rise. `normal-voice-result.json` confirms the injured line plays when the report remains open. Floor-edge landings are a documented limitation.
5. **PASS.** Rain cancels all site dots without backup; backup gives only the first selected section a dot. Both paths passed functional assertions.
6. **PASS, with audio listening still open.** Complete show measured 40.13 s. Skip measured 5.6 ms and Stop 2.4 ms. Seat selection redraws synchronously through the pointer/menu handlers. Clock, music and noise stop together. Muted Chrome cannot establish perceived audio quality.
7. **PASS.** The independent Python sample matches all four program-sheet ground values and both audiences' light and sound tables.
8. **FAIL for an unqualified rapid-event requirement.** Five-week held-click test spoke welcomeWeek once, sore five times and rain once. Advancing weeks at two-second pace dropped the queued injured line under its stale-week rule. Normal pace spoke sore and injured. Repeated siteAll audio was not fully verified.
9. **PASS.** All nine requested non-people paintings are present and embedded. Every finished asset was visually inspected; no lettering or people. One still-fountain redraw removed an unwanted spray.

## Wave lessons

- **Hint and voice: PARTIAL.** Hints change immediately and name the next control; Read uses them. End-week instructions now use a report-specific how line. Rapid simultaneous sore/injury speech remains the limitation in item 8.
- **Focus and layout: PASS after targeted repairs.** Controls are built once. Plan week focuses its mode tab; End week focuses the next week or Opening night; Begin focuses Stop; Stop focuses Begin. No focus on load. Transfers use preventScroll.
- **Sizes: PASS for primary controls.** All eight STANDARDS sizes checked, including a 375 iframe. Standard controls are at least 44 px; hints remain visible. Final phone width is 375 with a fully visible seat menu.
- **No giveaways: PASS / not a hidden-answer activity.** The model exposes consequences of production choices. No answer badges, points or puzzle sweep mechanic.
- **Honest numbers: PASS with limitations stated.** Fictional museum and device-only saving appear on screen. Model note explains factors, sampling, basin radius and the Rise-center floor assumption.
- **Standards: PASS.** Students adapt space and movement for DA:Pr4, manage rehearsal safety for DA:Pr5, and produce sound/light/audience presentation for DA:Pr6.
- **Motion off: PASS.** Audit found nothing running forever. Pose positions quantize while the show clock retains its duration.
- **Short choices: spec exception retained.** All twelve cards are visible on desktop and compact landscape. Phone cards deliberately scroll sideways, as the spec directs; End week stays pinned.
- **Resize mid-animation: PASS.** Full audit found no exceptions or controls left disabled. Camera and plan use current dimensions.
- **Delayed welcome: PASS.** No welcomeAfter queue. Same-mode taps preserve narration. Audit quick-tap checks were clean.
- **Unknown shown as unknown: not applicable.** The courtyard and given dance are known, with no hidden evidence states.
- **One look, one meaning: PASS.** Numbered section colors persist across plan, card, figure and sheet. Warnings also use words and a triangle. Grayscale frame reviewed.
- **Badge says what is true: PASS after repair.** Production reservations are distinguished from applied cards. Plan edits reset completed-show status.
- **Hints change back: PASS.** Site, Week, report and show transitions restore their current action hints.
- **No answer by word copying: not applicable.** Students weigh measured consequences rather than match a correct phrase.

## Audit leads

Ran the full audit **once**, last among the broad checks: 1,421.91 s, exit 0, **28 leads**, 53 frames. See `audit/audit.md`. Runtime, Motion off, resize recovery, five held clicks and two quick taps were clean. No full audit was repeated after repairs.

Every lead is covered by these dispositions, including repeated size instances:

- **12 base-size canvas/label overlaps:** intentional instruction and warning overlays with pointer-events disabled. Compact instruction text was shortened to keep the dimension label clear.
- **1 phone Week choices lead:** retained, because the spec explicitly requires sideways phone cards.
- **1 fresh-page Opening night focus lead:** the button is locked before week 6, so this automatic audit click is not a reachable student action. The unlocked route is verified separately.
- **1 pool-seat canvas/caption overlap:** intentional corner seat inset over the plan, as specified.
- **1 pool-seat Model control below the scroll edge:** fixed by moving Model into the persistent footer. Verified at 680 and 375.
- **1 pool-seat warning/caption overlap:** fixed by hiding the plan warning while the compact seat inset replaces it.
- **1 phone week-booking choices lead:** retained, same explicit horizontal-card requirement.
- **1 sore-week disabled-control speech lead:** fixed by dropping stale queued instruction and stopping an obsolete playing instruction while preserving Read, then queuing the report-specific how line. `quiet-week-voice-result.json` verifies current instructions.
- **1 phone sore-week choices lead:** retained, same horizontal-card requirement; historical cards are disabled.
- **1 final End week focus lead:** fixed by capturing focus before disabling the button, then focusing Opening night. `week-six-focus-result.json` passes.
- **1 Begin focus lead:** fixed by transferring focus to Stop before the run starts.
- **1 Stop focus lead:** fixed by returning focus to Begin. `show-focus-result.json` passes.
- **3 model-modal background/keep-region leads:** expected. The dialog deliberately covers the inactive map, instruction and footer hint. Its Close control remains visible.
- **2 Plan week walk focus leads:** fixed by transferring focus to the visible mode tab. `mode-focus-result.json` passes.

Additional targeted repairs verified direct floor dragging, keyboard floor movement, two sequential uncropped lifts, plan-change status reset, the populated 1280 seat panel, compact Sound off and the final phone seat menu. Final targeted batches report no console errors, warnings or exceptions.

## Frames looked at

- Quality bars: `bars/bar-snow.png`, `bars/bar-beat.png`, and `feel-comparison.jpg`.
- First playable and repaired frames: `first/`, `first-fixed/`, `checks/`, including the complete show and sample sheet.
- Full size/mode sweep: `full/`, reviewed through three contact sheets and key full-size frames. Includes grayscale and Motion off.
- Keyboard, jittered drag, five weeks and injured sheet: `targeted/`; narration follow-up: `normal-voice/`.
- All 53 audit frames: `audit-contact-0.jpg` through `audit-contact-4.jpg`.
- Final corrections: `post-audit/`, `lead-checks/`, `last-layout/`, `phone-leads/`, `last-phone-confirmed/` and `last-contact.jpg`.
- Expired host attempts and the first host favicon warning are preserved in Scratch as failed attempts, not claimed as successful checks. Final hosted runs are clean.

## Art made

Nine WebP images, **324,384 bytes (316.8 KiB)** total. Final bundle is about 996.3 KiB. Generated with the built-in image tool during this build and processed only with art.py --rekey. Still fountain redrawn once; cutout assets received hole and spill cleanup. Prompts and provenance are in art/prompts.json; raw PNGs are in art/raw. The final images are saved in this tool, not referenced from the generator's cache.

## Art still to paint

Six people:true pose assets describe procession, floor rolling, kneeling/sitting, standing Pool, weaving, and Rise landing/jump/lift poses, including audience-facing variants. The owner wants painted dancers. The kit figure remains temporary; makeDancer and PAINTED_POSES isolate its replacement. No people images were generated.

## Engine changes wanted

None. No kit or family documentation was edited. The family documentation can register this consumer later.

## Left open

- The printed spray sightline example differs from the independently computed model.
- Simultaneous sore and injury announcements can lose the queued injury line when the week changes rapidly. Repeated siteAll playback needs a dedicated listening/voice review.
- The Rise-center floor factor does not model individual landings across an installed floor edge. This assumption is stated in the on-screen Model note and handoff.
- Browser speech is the authorized fallback; no recordings were made. The requested Sadaltager timbre is metadata, not an achieved recording. Human headphone, music balance and narration-quality review remain open.
- Secondary rehearsal report text or an installed-floor selector can require scrolling at compact sizes. The main actions remain visible.
- The final audit is the pre-repair snapshot; only affected states were rechecked afterward.

All started Chrome instances and servers are closed. No assigned test port remains listening. host.html is removed. Build only ends here.
