# Museum Courtyard Performance: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: museum-courtyard-performance

#### Built

Built the offline Site, Week and Opening night modes: draggable zones and floors, sampled sightlines, two seat views, twelve production actions, six weeks, rehearsal adaptation, dancer load, rain, undo, saving, a 40-second show and printable program sheet.

Final bundle: **1,020,229 bytes**, under 2 MB. Source is 1,604 readable lines, maximum 159 characters. Draft metadata says built. Work stayed inside this tool and its Scratch folder. No commits, branch operations, shared-engine edits or polish round.

The report was started at the first successful bundle and completed after verification. Evidence paths below are under `_scratch/museum-courtyard-performance/`.

#### Numbers check

- Independent computation: `numbers.txt`, `prepare.py` and `manual-sample-result.json`.
- The 9 by 9 grid clipped to the ellipse has 49 samples. Arcade ground visibility is 78.50%; balcony examples are 100%, 59.18% and 26.53%.
- Source discrepancy: (10,8) gives 97.96% without spray and 83.13% with spray. At (10,13), spray gives 33.54%, rather than the stated 37%; without spray gives 92.45%. The specified ray model is retained and spec.md is unchanged.
- All actions once plus six rehearsals: $6,300 and 45 h. Sample production: $2,900 and 25 h, leaving $100 and 35 total crew hours.
- Loads: stone full 216, warm 172.8, half 108; marley full 144, warm 115.2; sprung full 72. Marked stone jumps give 64.8.
- Contrast ratios: brand/paper 5.34:1; white/brand 6.12:1; ink/paper 14.01:1; muted/paper 5.98:1.
- Independent sample ground Seen: 99.0136%, 63.2313%, 78.5034%, 89.1837%. All four match the browser model. Balcony Seen and Lit are 100%; Heard is 100% ground, 95% balcony.

#### Feel check

Played a six-week held-click student run, an independently checked planned production, and the complete opening-night show. Best moment: comparing low Pool work from the ground and balcony, then seeing the final sheet connect that difference to the production choices.

Flattest moment 1: the initial plan sat in a large empty surround. Added the painted courtyard behind the drawing board, textured stone, directional column shadows, pathways and live fountain ripples.

Flattest moment 2: the first procession camera lost dancers at the edge, and the finale felt static. Cameras now aim at each section; Arrival travels as a procession; Rise shows jump choices and two sequential lifts. The finale camera was widened and raised after a lift frame exposed cropping.

Compared `feel-comparison.jpg` with Beat Lab; Snowy Mail Route was also bundled into Scratch and opened. The painted setting and production desk have comparable visual care. The dancers remain visibly provisional by the owner's decision. Quiet final weeks have less activity when the student has already completed rehearsals; no extra events were invented.

#### Done when

1. **PASS, primary layout.** Site plan, Week board and Opening night with both seats dominate at 1366x768 and 680x425. Main controls remain visible. Some secondary report text or floor selection can require panel scrolling in short previews.
2. **FAIL against every printed example.** Most examples match within two points; the behind-fountain spray result differs by 3.46 points. Independent ray computation supports the implemented value above.
3. **PASS.** Crew and money caps, one-time cards and undo verified in `functional-result.json`. Undo restores budget, bookings and the pre-week plan.
4. **PASS for stated load cases.** Two full stone weeks produce injury; warm-up changes loads as computed. Sheet reports five in Rise. `normal-voice-result.json` confirms the injured line plays when the report remains open. Floor-edge landings are a documented limitation.
5. **PASS.** Rain cancels all site dots without backup; backup gives only the first selected section a dot. Both paths passed functional assertions.
6. **PASS, with audio listening still open.** Complete show measured 40.13 s. Skip measured 5.6 ms and Stop 2.4 ms. Seat selection redraws synchronously through the pointer/menu handlers. Clock, music and noise stop together. Muted Chrome cannot establish perceived audio quality.
7. **PASS.** The independent Python sample matches all four program-sheet ground values and both audiences' light and sound tables.
8. **FAIL for an unqualified rapid-event requirement.** Five-week held-click test spoke welcomeWeek once, sore five times and rain once. Advancing weeks at two-second pace dropped the queued injured line under its stale-week rule. Normal pace spoke sore and injured. Repeated siteAll audio was not fully verified.
9. **PASS.** All nine requested non-people paintings are present and embedded. Every finished asset was visually inspected; no lettering or people. One still-fountain redraw removed an unwanted spray.

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

- Quality bars: `bars/bar-snow.png`, `bars/bar-beat.png`, and `feel-comparison.jpg`.
- First playable and repaired frames: `first/`, `first-fixed/`, `checks/`, including the complete show and sample sheet.
- Full size/mode sweep: `full/`, reviewed through three contact sheets and key full-size frames. Includes grayscale and Motion off.
- Keyboard, jittered drag, five weeks and injured sheet: `targeted/`; narration follow-up: `normal-voice/`.
- All 53 audit frames: `audit-contact-0.jpg` through `audit-contact-4.jpg`.
- Final corrections: `post-audit/`, `lead-checks/`, `last-layout/`, `phone-leads/`, `last-phone-confirmed/` and `last-contact.jpg`.
- Expired host attempts and the first host favicon warning are preserved in Scratch as failed attempts, not claimed as successful checks. Final hosted runs are clean.

#### Art made

Nine WebP images, **324,384 bytes (316.8 KiB)** total. Final bundle is about 996.3 KiB. Generated with the built-in image tool during this build and processed only with art.py --rekey. Still fountain redrawn once; cutout assets received hole and spill cleanup. Prompts and provenance are in art/prompts.json; raw PNGs are in art/raw. The final images are saved in this tool, not referenced from the generator's cache.

#### Art still to paint

Six people:true pose assets describe procession, floor rolling, kneeling/sitting, standing Pool, weaving, and Rise landing/jump/lift poses, including audience-facing variants. The owner wants painted dancers. The kit figure remains temporary; makeDancer and PAINTED_POSES isolate its replacement. No people images were generated.

#### Engine changes wanted

None. No kit or family documentation was edited. The family documentation can register this consumer later.

#### Left open

- The printed spray sightline example differs from the independently computed model.
- Simultaneous sore and injury announcements can lose the queued injury line when the week changes rapidly. Repeated siteAll playback needs a dedicated listening/voice review.
- The Rise-center floor factor does not model individual landings across an installed floor edge. This assumption is stated in the on-screen Model note and handoff.
- Browser speech is the authorized fallback; no recordings were made. The requested Sadaltager timbre is metadata, not an achieved recording. Human headphone, music balance and narration-quality review remain open.
- Secondary rehearsal report text or an installed-floor selector can require scrolling at compact sizes. The main actions remain visible.
- The final audit is the pre-repair snapshot; only affected states were rechecked afterward.

All started Chrome instances and servers are closed. No assigned test port remains listening. host.html is removed. Build only ends here.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: museum-courtyard-performance
#### Played
Cold grade 9-12 play before builder reports or source: Site, seat inset, Week bookings, six weeks, complete show and program sheet.
Then walked the default rehearsal path with voice and tested budget/floor plans, injury, rain, empty weeks, keyboard and projector views.
It feels like a production desk with real tradeoffs; the audience comparison is its strongest idea. Kept the limestone world and twelve-card board.
Evidence below is relative to `_scratch/museum-courtyard-performance/`. Review stays one pass, with targeted rechecks.
#### Findings fixed
- **Blocker, general, weekLoad:** center-only floor credit let landings beyond a sprung edge claim load 72. Checks all six planned landings, hardest surface wins. Same real arrow-key exploit now returns 216 (`review-before/`, `review-after/`).
- **Should fix, general, load preview:** green low load could read as medical clearance. Labels now say model; visible advice distinguishes grip, cushioning and warm-up. Fictional numerical rules stay intact.
- **Should fix, general, narration:** soreness delayed the first injury announcement until it could go stale. Injury now starts first and includes its two-sore-week cause. Seat view and rehearsal booking speak their current how-to once.
- **Should fix, general, dialog speech:** leaving the sheet let the old event occupy speech; repeated openings lost one event. Sheet entry/exit now stop stale speech; five openings produce five events.
- **Should fix, family:dance, graphics:** temporary same-body code figures and unsupported floating lifts. Painted six varied dancers in five essential poses, plus supported pair lifts; all assets people:true. A small adapter keeps the cast swappable.
- **Should fix, general, pathway:** arcade weaving passed through column centers. The pathway bends around their coordinates.
- **Should fix, general, small screens:** gave phone status an extra row and restored keyboard-accessible opening-night seat menus in the scrolling secondary panel.
- **Should fix, general, compact Week:** the load estimate was below the fold. Plan and load now share the top row; all four section choices remain visible, and historical reports replace disabled rehearsal inputs.
- **Should fix, general, pointer stability:** opening Seat view moved its own button. Site actions are anchored after the secondary controls; exact before/open/close positions match in the targeted laptop and compact tests.
- **Should fix, general, duplicate state:** a Site map seat tap moved the camera but left its seat menu stale. The menu now follows the rendered viewpoint; a real row-three tap confirmed menu g40 and the row-three caption in the same pointer event.
- **Should fix, family:dance, cast assignment:** the sixth painted person always rested after injury. The rest slot is now selected independently of appearance; lifts use two complete remaining pairs. All six rest cases still show five people.
- **Polish, general, flat show:** live audience-average receipts now connect the performance to Seen, Heard and Lit. The sheet leads with this production's most limited view. Figures have more space to read.
- **Should fix, general, source credits:** the brief's precise IADMS Dance Floors title could not be verified. Public flooring credit now names the directly checked Ausdance guidance; notes preserve the source uncertainty.
#### Findings left
- **Should fix, specification:** spray examples and sunset chronology are inconsistent with the spec's own rule/times. Computed geometry and the required scripted light model remain; notes name both conflicts. See Left open.
- **Polish:** painted people are three-quarter billboards, with discrete key poses, rather than articulated rear views. Deliberate few-pose compromise, documented for swapping.
- **Polish:** the requested narrator timbre and final music mix need listening with headphones. No recordings were made under the build rules; browser speech remains the fallback.
#### Break it
- **Budget / crew / one-time cards:** spammed purchases, spent exactly 10 h, attempted unaffordable additions, then changed weeks. No overspend, negative money or repeat purchase; $300 remained in the tested $2,700 floor plan.
- **Adaptation dots / undo:** booked and unbooked repeatedly, ended, undid and ended again. Only actual rehearsals earn dots; undo removes the previous result and spending. Six empty weeks unlock a low-readiness sheet, with no score or success badge.
- **Load / injury:** slid Rise's center onto a panel edge with a real key. Exploit blocked after repair. Full stone 216, warm stone 172.8, half stone 108, marley 144 / 115.2 warm, sprung 72, marked stone 64.8. Two sore weeks injure; undo reverses the injury.
- **Rain:** tried no backup, backup, Rise first and Rise second. No backup gives zero dots/load; backup gives one dot, only the first section. Rise-first lobby full-jump load is 72; Rise-second is zero.
- **Seen / Heard / Lit / patterns / site use:** swept Pool adaptations and fountain modes, tested risers, lamps and unadapted spacing. Independent rays and all six sound-table cases agree. Open-floor Columns cannot claim weaving; running-only water cannot claim score use.
- These are exposed planning consequences, not a hidden-answer quiz: moving a zone to a better view is the intended skill, not a sweep-to-win gate. No best score or reflection gate exists.
- `review-functional.json`: 45 assertions passed; adversarial real-input paths in `review-after/` have zero console errors.
#### Voice walk
Final main path: real zone drag, Seat view, Plan week, default rehearsal selection, End week/current week through six Mondays, Opening night, Begin, all forty seconds, sheet.
Held clicks 0.12 s, gaps 2 s, default sound/motion. Heard order (`review-main-voice-final.json`):
`seatHow`, `chooseSeat`, `welcomeWeek`, `rehearsalHow`, `sore`, `injured`, `sore`, `sore`, `sore`, `rain`, `welcomeNight`.
The drag's first-tap instruction may replace the Site welcome under BASELINE 16; the welcome remains in hint/Read. No mode how-to is lost.
Later report-only how lines drop when the student has already opened another week, as required. Injury is heard before that transition.

| Line / kind | Expected | Spoken |
|---|---:|---:|
| Week welcome / how, five weeks | 1 | 1 |
| Rehearsal / how, five bookings | 1 | 1 |
| Seat selection / how, repeated toggles | 1 | 1 |
| Five sore-week results | 5 total | 4 sore + 1 injury/cause |
| New injury / event | 1 | 1 |
| Rain / event, main path | 1 | 1 |
| Site use / event, five sheet openings | 5 | 5 |

Read interrupted speech, worked with Sound off, and mode changes released it. Fourteen source lines match fourteen manifest lines exactly.
Main show reached position 64 and saved showFinished:true; injured lift frame contains five people, including the two-person painted pair.
The mid-show real seat tap updated its caption inside the same pointer event while running; real Skip and Stop then acted immediately (`review-midshow-seat.json`).
#### Facts checked
- **Venue dimensions, seats, piece, prices, crew, weather and all percentages/load rules:** fictional spec Content/Model, explicitly labeled. Independent `review-numbers.json`: all purchases $6,300 / 45 h; sample $2,900 / 25 h; 49 ellipse samples; 60 ground / 40 balcony seats.
- **Sightlines:** own independent 60-seat rays against the specified 0.3 m columns and 1.5 m spray. Arcade 78.50%; balcony 100%, 59.18%, 26.53%. Behind spray 33.54%, not printed 37%; (10,8) 83.13% with spray / 97.96% without.
- **Surface grip versus shock absorption and hard-floor caution:** [Ausdance National, Safe dance floors](https://ausdance.org.au/articles/details/safe-dance-floors), live checked 2026-11-06. Fictional floor multipliers do not imply measured cushioning.
- **Warm-up/cool-down preparation, authors and date:** [Human Kinetics, Safe Dance Practice](https://us.humankinetics.com/products/safe-dance-practice) and [publisher excerpt](https://us.humankinetics.com/blogs/excerpt/structure-and-content-of-individual-dance-sessions), Quin, Rafferty, Tomlinson, 2015. No guidance supports the invented 20% reduction or 120 threshold; these remain clearly identified model choices.
- **Site-specific form and credit:** [Kloetzel and Pavlik, Site Dance, 2009](https://doi.org/10.5744/florida/9780813034003.001.0001), publisher-hosted record. Original Water Over Stone is credited to Curio Class, not represented as a traditional dance.
- **Standards:** [NCAS Dance performing standards](https://www.nationalartsstandards.org/customize-handbook). Students adapt levels/pathways (Pr4), compare rehearsal/floors/load (Pr5), and allocate sound, light and audience production (Pr6). The simulator does not assess physical technique.
- **Contrast:** independent WCAG computation gives brand/paper 5.34:1, white/brand 6.12:1, ink/paper 14.01:1, muted/paper 5.98:1.
#### Sensitivity
Bodies and injury require fresh sensitivity review. Check that the cast's skin tones, apparent ages and body shapes read naturally, the supported lifts remain clear, and injury is treated as care rather than a score penalty. No named cultural tradition is represented.
All people images are tagged people:true; the contact sheet is `review-art-contact.jpg`. Check partner-lift role assignments as well as cast variety. No actual disability, health or dance competence is inferred from appearance. Images are illustrative, not a lift tutorial.
#### Flattest moment left
Late quiet weeks can be short if the production is already planned. The spec explicitly permits quiet weeks; no extra event or topic was invented. The lifted show now gives an immediate audience comparison and a specific final result.
#### Graphics
Kept all nine architectural paintings; inspected every finished asset, both painted atlases, cutouts on a contrasting sheet, and final-size ground/balcony poses. Added 30 individual pose cells plus three paired lifts in two swappable assets, not 33 separate files.
Eleven WebPs total 589,396 bytes. Final bundle: 1,379,345 bytes (1,347.0 KiB). Artwork, source and voice are embedded; no tool network references. Original limestone palette and layered production board remain.
Compared fresh Beat Lab and Snowy Mail Route frames; `review-painted/`, `review-phone/`, `review-after/`, `review-checks/` and contact sheets hold the targeted evidence. Keyboard-only plan movement, grayscale and calm frames were opened and inspected.
#### Audit
Completed once in 1,670.98 s (27 min 51 s), exit 0, under the 2,400 s cap. Chrome 9961, host 8765; 52 saved frames opened through contact sheets 00-08. No full audit repeated.
All 25 reported leads are accounted for:
- Ten map/warning/instruction overlaps and two inset-caption overlaps are intentional nonblocking labels on the canvas; inspected at each reported size.
- Two phone leads came from a failed iframe attachment, not a missing tool hint. Leftover localhost helpers may have interfered. Targeted 375 iframe checks covered Site, seat inset, Week booking/report, Opening night and sheet: no small targets, page overflow, clipped text or console errors.
- One grouped Opening night focus lead clicks the locked fresh-page tab. The unlocked six-week route, Begin, Stop, Skip and seat controls were tested separately.
- Three Model-dialog background/keep leads and one sheet keep lead are deliberate modal coverage of the inactive background.
- Four receipt keep leads are hit-testing artifacts from passive overlays; the audience receipts are visibly present in both views at 680 and 1366.
- Two first-tap welcome leads are permitted by BASELINE 16: Seat view speaks its own action; Model opens its text. The premise remains in Site hint/Read.
The frame review additionally found the compact load/report fold fault and the Site action-button shift. Fixed and re-shot only those layouts. Phone sideways action cards follow the explicit spec; keyboard focus deliberately scrolls secondary night seat menus into view.
Motion off, held-click focus/Enter, five repeats, quick taps and resize recovery were clean. Final targeted frame/measurement files are `review-post-audit/`, `review-extra-checks/` and `review-final-phone-status/`.
Final socket preflight found four orphan host children from this review. Their exact tool/port command lines were verified and all four closed; no unrelated process was stopped. Evidence: `review-owned-processes.json` and final validation.
Done when: layout, spending/undo, injury/load, rain, forty-second show and sheet checks pass. Printed sightline examples remain a spec discrepancy. The injury event combines its sore-week cause. The owner's painted-people direction overrides the old no-people art item.
#### Left open
- Correct the spec's spray worked examples and dusk timetable. Six minutes starting thirty before sunset ends twenty-four before sunset, not after dusk. The required scripted dusk rule is retained, with the conflict visible in teacher notes.
- Exact IADMS Dance Floors paper/title was not located; old IADMS media URLs redirect. Checked public flooring credit uses Ausdance instead.
- Unattended choices retain the brief's direction: 0.75 m assumed basin radius, later-week warm-up, 75% kneeling factor, first-selected lobby section and inherited sprung-lobby assumption. None is presented as a real venue rule.
- Headphone listening, named recorded timbre and the fresh sensitivity/owner people contact-sheet review remain pre-publication work. No outside contact, upload, commit or shared-file change was made.

Final cleanup: all assigned Chrome/host ports closed, temporary host removed, source lines at most 160 characters. No commits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Museum Courtyard Performance handoff

#### Structure

The source contains the light limestone production desk, content tables, ray model, weekly state and undo,
canvas plan, perspective seat renderer, show clock/music, local saving and dialogs. The kit is unchanged.
All review evidence is in `_scratch/museum-courtyard-performance/review-*` plus the cold-play folders.
The builder report remains a historical record of the earlier build, not the review verdict.

#### Cold review repairs

- A purchased floor once benefited Rise whenever its center was on the floor. `weekLoad` now checks all six planned
  Rise landing spots and uses the hardest surface. This closes a real keyboard edge-placement exploit, 72 to 216.
  New floor reservations use the same geometry as applied floors. The model note explains the assumption.
- The load preview says model, and the weekly advice makes clear that a low bar is not safety clearance. Vinyl gives
  grip, not sprung-floor cushioning. The fictional factors remain those required by the spec.
- On the first injured week, the injury event starts immediately instead of waiting behind soreness. Its line also
  names the two sore weeks. The next week may stop speech when its moment has passed, as the kit requires.
- Rehearsal booking and Seat view now speak their own how-to once and keep their hint current.
- S3's arcade pathway now bends around column coordinates instead of passing through their centers.
- Opening night shows each audience's model averages while the dancers perform. The sheet leads with this production's
  most limited audience/section. It remains a production exploration with no points or success gate.

#### Painted dancers and swapping

`makeDancer` is now a small image renderer, not a code body. It receives world coordinates and an art row.
`PAINTED_POSES` supplies two art tokens. `DANCER_ATLAS` supplies original pixel dimensions and whole-body crop rectangles.
Replace those tokens and rectangles together to swap the cast without touching sightlines, load or weekly logic.
All six cast members have walking, floor, kneeling, lateral and airborne poses. Standing Pool uses the walking/middle
pose. A separate three-pair strip teaches supported low lifts. The show uses two sequential pairs, hides the corresponding
second individual while the paired picture is shown, and still shows only five people in an injured finale.
These are illustrative three-quarter billboards, not fully articulated bodies or a survey-accurate rear view.
Motion off holds count-boundary states and preserves the forty-second clock.

The resting cast slot is selected once at the modeled injury, independently of appearance, and saved with the
production. Lift selection uses the two complete pairs still available. All six possible resting slots were checked:
four visible image groups represent three individuals and one painted pair, hence five people. All three lift cells
can be used. Older saved productions without a slot retain their original sixth-person rest assignment.

The final audit frame review also exposed a compact load display below the fold and a moving Seat view button.
The compact meeting panel now puts plan, load and four section buttons above the jump menu; historical weeks replace
disabled rehearsal inputs with the report. Site actions sit after the secondary menus, anchored at the bottom.
Phone status has space for the show-ready forecast, and secondary opening-night seat menus remain keyboard reachable.
The Site seat dropdown is synchronized in drawSeat, including when a map tap changes the viewpoint.
Arcade paths are constrained to their moved ellipse and keep 0.5 m center clearance from columns. The geometric
site-use check remains the spec's zone-overlap simplification, rather than a full choreographic assessment.

Both new assets have people:true, generated by Codex with OpenAI gpt-image. The nine architectural paintings remain.
The atlas is keyed without trimming the overall margins, so cell coordinates remain stable. Raw originals and WebPs
live in art/. The cast sheet in Scratch supports the owner's pre-publication contact-sheet review.

#### Model assumptions and spec discrepancies

The basin radius is unspecified; the inherited 0.75 m choice stays labeled. Rays sample 49 points on the prescribed
9 by 9 ellipse grid and all 60 ground seats. Individual seat illustrations are separate from audience-average metrics.
The simplified balcony model sees samples south of y=13. Rehearsal always has the fountain running; show-off permission
does not apply to Mondays. Week-six backup gives the first selected section one lobby dot, with the inherited sprung
lobby floor assumption. Warm-up affects later weeks, not its booking week. Money and hours reserve immediately.

The spec's spray examples differ from independent computation: (10,8) is 83.13% with spray, 97.96% without;
(10,13) is 33.54% with spray instead of 37%. Preserve the stated ray rule, not the mistaken worked example.
Its six-minute show starting 30 minutes before sunset cannot have its last three minutes after dusk. Preserve the
requested scripted light model and expose this contradiction in teacher notes until the spec is corrected.

#### Sources

NCAS Dance performing standards: https://www.nationalartsstandards.org/customize-handbook
Floor principles: Ausdance National, https://ausdance.org.au/articles/details/safe-dance-floors
Warm-up/cool-down: Quin, Rafferty and Tomlinson, Safe Dance Practice, Human Kinetics, 2015,
https://us.humankinetics.com/products/safe-dance-practice
Site-specific dance context and credits: Melanie Kloetzel and Carolyn Pavlik (eds.), Site Dance, 2009,
https://doi.org/10.5744/florida/9780813034003.001.0001
The brief's exact IADMS Dance Floors resource title could not be located. Old IADMS media links redirect; indexed
warm-up guidance was cross-checked against the publisher. No medical provenance is claimed for the fictional factors.

#### Sensitivity

Fresh sensitivity review should check bodies, injury language, safe-practice framing and the six-person painted cast.
The cast varies skin tone, apparent age and body shape without assigning ability or injury by appearance. Lift images
show secure support and modest rehearsal clothing. This is an original contemporary piece, not a named cultural tradition.
The paintings do not offer a lifting tutorial. The injury is a care issue, not a score penalty.

#### Engine changes wanted

None. All repairs are tool-local. No shared files or git history were changed.

#### Review evidence

Final results, voice counts, targeted frames and the single final audit are summarized in codex-review.md.
Browser voice is still the allowed fallback; no audio was recorded. A muted automated run establishes triggers and
timing, not the perceived voice timbre or music mix. Source contradictions above need the spec owner's decision.

The single review audit finished in 1,670.98 seconds, exit 0, with 25 lead groups and 52 saved frames. Its phone
execution-context attachment failed; leftover host helpers may have interfered. Targeted iframe checks measured every phone mode without changing
the shared audit script. Main controls are in view; secondary seat menus scroll into view for keyboard selection.
The specified horizontal phone action-card list remains. Audit resize, repeated-tap and runtime checks were clean.
Only the confirmed layouts, path boundaries and cast substitutions were checked after the audit, not a second full pass.
Final socket checks caught four orphan server children from this review's host helpers. Their exact tool/port command
lines were verified before terminating them. Future Windows helpers should verify the actual host child stops, rather
than trusting only a launcher taskkill result. No unrelated process was stopped.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
