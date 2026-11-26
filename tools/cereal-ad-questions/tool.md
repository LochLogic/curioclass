# Cereal Ad Questions: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: cereal-ad-questions

#### Built

- Built the three modes, eight switch combinations, original synthesized jingle, live part switches, class votes, SVG comparison chart, five message cards and eighteen day-scene hotspots.
- Added all required build files and ten generated paintings. The bundle is self-contained. No commits, branch changes, recordings or polish round.
- Source uses the kit controls, AudioContext and Curio.voice. Activity data stays in memory.
- All working commands after the initial read used a bounded child-process runner: bundle 120 seconds, drive batches 300 seconds, audit 2400 seconds.
- Only this tool and its Scratch were authored. Bar tools were copied and bundled in Scratch to avoid writing their folders.

#### Numbers check

- Evidence: `_scratch/cereal-ad-questions/numbers.json`, recomputed with Python before the first bundle.
- Five shots times three seconds = 15 seconds. Sixteen beats at 132 beats per minute = 7.272727 seconds; two loops = 14.545455 seconds.
- The exact remaining tail is 0.454545 seconds, rather than the spec's rounded 0.4 seconds.
- Three scenes times four ads = 12 ads; three times two non-ads = 6. Vote bounds are zero through forty per bar; chart scale has a floor of ten.
- Supplied shelf heights convert to 58.42 and 121.92 centimeters. No extra height claim was added to the interface.
- Contrast: white/brand 7.3071, brand/paper 6.9331, ink/paper 16.2211, muted/paper 6.6131. All match the listed rounded values.
- The spec says eleven images but names ten. All ten named assets are present and used.

#### Feel check

- Played the whole sequence through the ad comparisons, all five message interpretations and all eighteen discoveries using muted Chrome and real held input where narration races matter.
- Best moment: the bright selling scene becomes a quiet painted bowl while the class's own pairs of bars remain. The illustrative test poll used 28/4, 17/15 and 5/27, not a built-in result.
- Flat moment one: the box name initially floated off its blank panel. Repositioned it onto the package so the opening reads as one convincing product.
- Flat moment two: the portrait message TV made Comet too small and left a large gap above the trampoline. Stacked the scene and all five cards at 760 wide; the final frame is `postfix-frames/portrait-messages.png`.
- Also preserved whole bowls in wide TVs with contained paintings over a blurred painted surround, removed sign-covering discovery badges, and fixed compact sign wrapping.
- Compared with both bar tools. `_scratch/cereal-ad-questions/bar-comparison.png` places the Comet shot beside Beat Lab. This build has comparable visual depth for its younger audience; its replay value comes from changing reactions rather than a music sequencer's open-ended composition.
- Audio was muted for testing. No claim of headphone listening or a real K-2 classroom trial.

#### Done when

1. PASS: TV is the largest object at 1366x768 and 680x425. Switches and voting controls remain visible. Default audit sizes are all clean.
2. PASS: all eight combinations completed at an elapsed 15000 milliseconds. See the eight `finished-*` checks in `functional-results.json`.
3. PASS at the browser node/state level: music disconnects synchronously and starts at the current beat, pictures swap immediately, Words returns on the next line, and Stop clears nodes. See `functional-rest-results.json` and `words-next-line.json`. Acoustic latency was not measured.
4. PASS: bounds, ownership and labeled SVG bars checked. A completed replay starts a fresh zero-count poll and replaces its previous bars; edits to the previous poll during playback are committed. See `replay-check.json`.
5. PASS: two completed Plain bowl polls each started the big-question event. `voice-behavior.json` records first=1, second=2 and no host speech during either ad interval.
6. FAIL in one content requirement: all fifteen part-button paths run three seconds and all five True? cards show/speak, but the Words clip contains only the opening slogan. Five complete spoken slogans cannot fit clearly into the required three seconds. The full ad contains all five.
7. PASS: all eighteen objects tested, four ads per scene, non-ads excluded from the counter, targets at least sixty pixels. The phone counter now has its own row.
8. PASS: host narration is gated during playback, Read stops playback first, how-to lines use the kit heard set, and two-second held-click checks are clean. Requested recorded performances remain unmade under the Build rule.
9. PASS: sixty-pixel controls, icons and words, visible focus and object names for intentionally hidden hotspots. Default and explicit message states were mechanically clean for target size.
10. PASS for offline operation, still shots with unchanged timing, and no activity saving. FAIL literally for "nothing is saved": the required shared kit persists only the Motion preference. Standing STANDARDS.md takes precedence.

#### Wave lessons

- PASS, Hint and voice: hints change synchronously; Read uses the hint/open card; first actions proceed immediately. Two-second switch test started all five events.
- PASS, Focus and layout: stable controls, no load focus, held-click audit has no focus losses. Stop moves focus to Play; Escape restores the next-action hint. Sign-covering checkmarks were removed.
- PASS, Sizes: all eight required sizes across the three modes, including 375 in an iframe. Only affected portrait, phone and compact states were re-shot after repairs.
- PASS, No giveaways: object names do not reveal ad classification. Classification appears after a tap. This is an explorer and discussion tool, not a hidden-answer scoring game.
- PASS, Honest numbers: actual entered hands, shared chart scale with a floor of ten, no expected downward trend, no assumed class total.
- PASS, Standards: part switches teach Re7, message/evidence cards teach Re8, own-vote comparisons teach Re9, and daily scenes teach Cn11.
- PASS, Motion off: the audit found no endless animation; the still Comet frame retains the regular shot clock.
- PASS, Short choice groups: all five message choices and all three part controls are in view; no short-choice scroll panel.
- PASS, Resize mid-animation: audit stress produced no exceptions or stuck disabled controls. Subsequent portrait art fitting was checked in targeted frames.
- PASS, Welcome after first tap: an action's own event skips the welcome as required. Re-tapping an active mode no longer cuts its playing welcome.
- PASS, Unknown as unknown: unexplored objects have no discovered classification; the four-ad total is an explicit hunt goal from the spec.
- PASS, One look, one meaning: the glow means explored for either kind of object. Only ad discoveries affect the ad counter; the card states An ad! or Not an ad.
- PASS, Badge says what is true: current version changes live and Stop clears the playing badge. Votes name their completed owner in the hint when the parts change.
- PASS, Hint changes back: mode, place and modal-close paths restore appropriate instructions. Escape was checked with real keyboard input.
- PASS, No answer by copying: evidence and True? discussion do not use a matching-words scoring mechanic; daily classifications are revealed only after inspecting an object.

#### Audit leads

- One full audit completed: `_scratch/cereal-ad-questions/audit/audit.md`, 53 leads. All eight initial sizes, Motion off, resize stress and five-click voice repetitions were clean. No full post-repair audit was run.
- 38 sign/hotspot overlap leads: intentional labels on their tappable objects. Labels have no pointer interception and now paint above the glow. Final compact Street and Store frames show legible signs.
- 5 phone counter overlap leads: FIXED with a separate counter row. `phone-counter-check.json` confirms its top is below the place buttons; final phone frame inspected.
- 2 covered-hint keep-region leads: intentional modal coverage. The modal contains the current answer or confirmation, and Read speaks that content. Both dialogs and their Close/Keep paths remain reachable.
- 5 first-action welcome-not-heard leads: correct standing-rule behavior for Music, Pictures, Words, Play and Start over, each of which has its own action or line. No late welcome was added.
- 3 quick same-mode welcome cuts: FIXED by preserving the active mode on a repeated tap. `same-mode-check.json` records one uncut welcome.
- Audit limitation: its MODES_JS only recognizes controls under a header. This tool's separate navigation was not auto-detected, so the automatic per-control walk covered the initial mode. Explicit state frames, the size matrix, fifteen clip paths and eighteen hotspot inputs covered the other modes independently.
- Other build fixes after the audit: stale card welcome interruption, Stop label/focus, Escape hints, portrait painting proportions, sign badges/wrapping, and fresh replay vote ownership. Targeted checks passed; this is not a second full audit.
- The first live-music-off probe failed and was repaired by disconnecting the audio bus. A later host-speech test window extended beyond the ad boundary; correcting it to the actual start time produced an empty during-ad host log.
- An initial phone harness favicon 404 was eliminated with a data favicon. Final phone and targeted batches report zero errors.

#### Frames looked at

All paths below are under `S:/CurioClass-codex/_scratch/cereal-ad-questions/`.

- `bar-frames/`: Snowy Mail Route and Beat Lab. `first-frames/`: laptop and compact initial builds.
- `frames/`: all 24 desktop/iframe mode-size frames, individually or in `contact/0.png` through `3.png`.
- `extra-frames/`: calm Comet, grayscale, keyboard, class-chart payoff, both compact dialogs, Street, Store and voice pace.
- `final-frames/`: SVG payoff, plain compact, painted toy card and clean phone harness.
- `audit/`: all 57 frames, reviewed in `contact-audit/0.png` through `9.png`; compact vote and phone-limit frames also opened full size.
- `postfix-frames/`: portrait messages/day, compact and phone Store, Stop label, Escape, same-mode double tap and card interruption.
- `sign-frames/`: final compact Store and Street. `voice-frames/`: repeated Plain bowl question and next-line Words. `replay-frames/`: replay vote replacement. `asset-frames/`: final edge-cleaned Comet and toy reveal.
- Every final painting was inspected, including keyed cutouts with edge despill. Rejected animal-filled splash/table drafts and the store safety pictogram were replaced.

#### Art made

- Ten generated images, 841370 bytes total, about 821.7 KiB. No people in the final paintings.
- Final bundle is about 1169.1 KiB, under two million bytes; exact size is in `static-results.json`.
- Three redraws: splash and table to remove unintended animals; Store edit to remove the human safety pictogram.
- Source credits OpenAI gpt-image. Exact prompts, provenance and redraw counts are in `art/prompts.json`; originals are under `art/raw/`.

#### Art still to paint

None of the ten named assets. The spec's unnamed eleventh image is a count discrepancy, not a placeholder.

#### Engine changes wanted

- No required kit change. Optional `kit/curio.js` Motion initialization/handler option for in-memory preferences would resolve future no-persistence specs.
- `scripts/audit_tool.py`, MODES_JS: support mode navigation outside a header so automatic walks include these modes. No shared file was changed.

#### Left open

- Owner decision on five spoken slogans versus a three-second Words clip. Current clip uses the opening line, and part controls share a persistent evidence strip rather than appearing inside each selected card.
- The plain-bowl-start host line is not spoken, to honor the higher-priority rule that host speech never overlaps an ad. The after-vote big question is implemented and tested.
- Requested news-reader and excited-announcer recordings were not made. Browser voice identity, offline voice availability and the final long slogan's pacing need listening review.
- The shared Motion preference persists, as required by the standing standard; votes and discoveries do not.
- The full audit predates the listed targeted repairs. Cold review remains the next step.
- Procedural deviations: numeric recomputation and bar-tool opening occurred after initial source authoring, before the first playable checks. The first read used the tool wait rather than the later child-process timeout wrapper. The report is intentionally last under the user's stop-on-report instruction.
- Owned Chrome sessions and host server were closed; tool-folder host.html was removed. No git commits and no polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: cereal-ad-questions

#### Played

- Cold K-2 solo exploration and teacher/projector walk before reading codex-report.md, handoff.md, notes.md or src.html. Played all comparisons, five truths, three clips and eighteen objects. The loud ad becoming a quiet bowl is strong; the chart initially felt flat.
- One review pass, followed by repair checks. Workspace S:\CurioClass-codex; writes confined to this tool and its Scratch; no commits.

#### Findings fixed

- Blocker, general, voice: first-vote Music instruction could wait behind the answered vote prompt and be dropped. The relevant instruction now starts immediately; the final held-click voice walk hears it.
- Should fix, general, voice: switch announcements now supersede obsolete how-to speech, so Music off is heard at the two-second pace. Identical hint text no longer re-triggers its live region.
- Should fix, general, voice: the plain-bowl question could be lost, then nag on every counted hand. It now starts on the first nonzero vote, once per completed poll, and returns on a new poll.
- Should fix, general, day mode: speech could describe the previous object while another explanation was visible. New discoveries preempt old speech; completion also requires the same selected object.
- Should fix, general, day art: the Family photo target was a landscape. Replaced only that picture inside the rich kitchen illustration with a family portrait; marked people:true.
- Should fix, general, teaching/art: blank game, billboard and bus banners offered no visible selling evidence. Added fictional selling copy and a cereal-box image to the billboard.
- Should fix, general, phone chart: eight versions squeezed labels and joined adjacent 40s. Dense phone charts now use readable horizontal pairs; all eight remain reachable by ordinary page scrolling.
- Should fix, general, compact caption: the audit confirmed the box name intersected the final slogan at 680 wide. Reserved headroom while retaining the full painting and readable package type.
- Should fix, general, product art: at 760 wide the box lettering drifted onto its edge. Painting and lettering now share SVG coordinates and resize together. Re-shot 760, 1366, 680 and phone.
- Should fix, general, animation: Comet's ears/bowl could cross the TV boundary at the top of a bounce. Reserved headroom during playback; retained the large idle mascot and trampoline.
- Should fix, general, facts: corrected CSPI's date to August 2015 and made sign descriptions precise: STOP directs drivers to stop; WET FLOOR warns of a slippery floor. Updated notes, metadata, voice lines and handoff.
- Polish, general: lifted the flat vote payoff with current-poll highlighting, a brief counted-hand response and bar movement. Motion off suppresses the movement. Kept the paintings, rust/paper palette, rainbow TV and original jingle.

#### Findings left

- Blocker, general, spec-bound hunt: tapping every object reaches 4 of 4 without recognizing an ad. Ran the sweep before and after fixes. The specified reveal-on-tap interaction cannot resist that route without a new prediction/check step, which this review may not add. Treat it as discovery, never a knowledge pass.
- Should fix, spec conflict: a three-second Words clip cannot clearly say all five slogans. Kept three-second timing and the explicitly labeled opening-only sample; full ad retains all five.
- Should fix, spec/source conflict: a free-event poster can still advertise an event. The spec calls this library poster Not an ad. Notes explain the narrower selling-message convention; changing the classification needs a spec decision.
- Should fix before final audio release: specified news-reader and excited-announcer recordings remain absent. Browser fallback works, but identity, performance and complete last-slogan pacing are not acoustically verified. Recording is prohibited in this workflow.

#### Break it

- Vote gate: attempted both pluses and minus before watching; counts stayed zero and no chart was created.
- Bounds: 45 held clicks per plus stopped at 40 each; repeated subtraction stopped at zero. Both 40s are allowed by the spec, not a class-size estimate or achievement.
- Ownership/chart: changed switches, voted during a replay, and replayed the same version. Old-poll edits stayed with their completed owner; the new poll reset to zero; a replay replaced its own prior bars. Keep it preserved work; confirmed reset cleared votes/chart and restored switches.
- Timing/parts: all eight real-time runs ended at 15000 ms with the correct owner and words/pictures. Music node mute observed in 0.8 ms, immediate plain picture, Words restored next shot, Stop cleared playback/nodes. Acoustic latency was not measured.
- Hunt: non-ads added zero; five repeated taps on one ad added one; sweeping six objects reached four. No saved best, accuracy score or timer exists. The sweep remains the named spec blocker above.
- Message/truth cards: tried every card and all fifteen part paths. Each clip stopped at 3000 ms; truths opened for all five. This mode offers discussion evidence, not a correctness pass. The strength question asks conditionally and assumes no mistake.
- Reflection: unchanged/zero Want it votes are permitted. No prescribed decrease, percent badge, right-option position or reflection gate forces a desired answer.

#### Voice walk

- Final: Play, vote, Music off, Play, vote, Pictures off, Play, vote, Words off, Play, vote; repeat plain-bowl poll; What it wants, card, three clips, True?, close; Ads in my day and all six breakfast objects. Held 120 ms; two-second gaps between actions, full waits for ad/clip playback; Sound on, Motion on.
- Heard in order: vote, remove Music how-to, Music off, vote, Pictures off, vote, Words off, vote, big question; new poll vote/big question; message welcome, card title/part instruction, clip-done how-to; truth; day welcome and each current discovery. First Play may skip the welcome under BASELINE 16; hint and Read retain it.
- Counts: remove how-to 1; clip-done how-to 1 then silent repeats; big question 2 for 2 polls, not 3 for 3 button taps; repeated same hotspot event 5 for 5 taps. No host line starts during the ad. Changed safety lines separately shown and spoken.
- Read works with Sound off, interrupts playback before speaking, and mode changes clear its stale context. Final allLines and voice/lines.json match exactly. Logs: voice-checked-flow-result.json, hunt-repeat-and-misses-review-result.json, read-off-and-mode-review-result.json.

#### Facts checked

- Music/pictures/words can persuade, mascots attract attention, and young children need adult help with intent: [APA, Advertising and Children, 2004](https://www.apa.org/pubs/reports/advertising-children). No claim this activity makes children immune to ads.
- Selling intent and interpreting media: [Common Sense, Understanding Ads, Grade 1, July 2025](https://www.commonsense.org/education/digital-literacy/understanding-ads); [K-5 Family Tips](https://www.commonsense.org/education/family-tips/k-5-news-and-media-literacy). Broader definition motivates the library-poster issue above.
- Box/yogurt mascots, game banner, pizza magnet, bus/billboard, shirt logo and shop sign are fictional examples of those selling messages. Their visible evidence and explanations were checked; no real company or product claim appears.
- Low cereal shelf: [Musicus, Tal and Wansink, Eyes in the Aisles](https://doi.org/10.1177/0013916514528793), 2015 issue, online April 2014. Study sampled 86 characters in ten Eastern U.S. stores; 23/48 inches are historical sample averages, not universal heights. UI adds no height claim.
- Checkout candy, mascot display and two-for-one promotion: [CSPI, Temptation at Checkout](https://www.cspi.org/resource/temptation-checkout); [report copyright August 2015, PDF p. 2](https://www.cspi.org/sites/default/files/media/documents/resource/report.pdf). The spec's 2016 date was wrong.
- STOP's purpose: [FHWA MUTCD, Section 2B](https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/mutcd11thedition.pdf). Wet-floor warning: [OSHA, Clean-up](https://www.osha.gov/etools/young-workers-restaurant-safety/clean-up). Safety signs are information, not sales pitches in these scenes.
- Lunch menu, family photo and aisle number serve the shown information/memory/navigation roles. The library example is qualified above. These are authored scene examples, not claims that all menus, photographs or free events are noncommercial.
- Five truth cards checked against the authored ad: fun comes from its production, toy is separate, everybody is unsupported, strength is never said, and an ad cannot establish personal taste. No nutrition benefit or tasting task is asserted.
- Standards: [NCAS Media Arts](https://www.nationalartsstandards.org/content/media-arts): Re7 components through switches, Re8 interpretations through cards, Re9 changed-ad comparisons through votes, Cn11 daily-life purposes through scenes. Notes retain the three required opening headings and usable home activities.
- Independent arithmetic: 5 x 3 = 15 seconds; 16 beats at 132 bpm = 7.272727 seconds, two loops leave 0.454545 seconds; 8 combinations; 12 ads/6 non-ads; counts 0-40, scale floor 10. Contrast white/brand 7.307, brand/paper 6.933, ink/paper 16.221, muted/paper 6.613.

#### Sensitivity

- No cultural, religious, Indigenous or historical claim. Review the new family portrait for respectful representation; it shows one family, not a norm for all families. It has varied skin tones and no stereotype noted. Asset people:true; review-family-contact.png includes asset and phone context. Avoid shaming food preferences or unchanged votes.

#### Flattest moment left

- The silent fifteen-second plain-bowl replay intentionally waits for class observation. Its clock makes the wait legible. The chart now responds and identifies the current poll; extending this with new gameplay would change the brief.

#### Graphics

- All ten named paintings inspected in contact sheets and final-size scenes, including all five ad shots, three day scenes, both mascot poses and toy card. Spec says eleven but names ten; no art token is missing.
- Redrew day-breakfast with built-in imagegen; final raw tools/cereal-ad-questions/art/raw/day-breakfast.png, final art/day-breakfast.webp. Full prompt/provenance in art/prompts.json. Existing art retained. One coherent glossy commercial set and deliberately quieter painted day/bowl set.
- 807312 art bytes; final bundle 1156037 bytes, about 1129 KiB. review-bar-comparison.png compares current art with the existing local Beat Lab reference frame.
- Looked at all review-matrix frames/contact sheets, review-target, review-phone-final, review-final-frames, review-last-targets, review-checks, review-live and cold-play frames. Every STANDARDS size covered, including 375 inside host 8745; grayscale, Motion off, extreme counts and keyboard-only flow checked.

#### Audit

- One audit completed within its 2400-second limit: review-audit/audit.md, 62 raw leads. All 51 saved frames were opened in review-contact/review-audit-0.png through -8.png; the compact caption finding was also checked full size.
- Two real caption-overlap rows concerned the same 680-wide final shot at ordinary and maximum votes. Reserved caption headroom with readable package lettering; focused 680/800/1366/375 re-shoots and geometry checks cover the final fix.
- Fifty-one sign/hotspot overlap rows are intentional labels on their objects. Labels remain legible above the glow and have pointer-events:none. No tappable choices are hidden.
- Two covered-hint rows are the background hint behind open dialogs. The dialog supplies the current answer/confirmation; Read speaks it. Confirmed in frames and keyboard/Read checks.
- Two phone-harness rows mean iframe context not found and consequently no hint detected. Audit phone coverage is unavailable; separate 375-wide host runs cover all modes, charts and repaired art. No claim the audit passed its phone check. Orphan preview-server children were found and closed later; their possible effect on that harness is unverified.
- Five first-action welcome skips are permitted by BASELINE 16: three part switches, Play and Start over have their own action/context. No delayed welcome was added.
- Seven desktop opening sizes, focus/targets, Motion off, held-click repetitions, quick taps and completed resize stress had no other mechanical failures. All listed work states were exercised at their requested desktop sizes.
- The audit does not discover mode navigation outside a header; its per-control walk covers the opening controls/mode entries. Explicit states and independent clip/hotspot/keyboard walks cover both other modes. Shared scripts were not edited.
- The final bundle contains two focused post-audit corrections: caption placement and switch-event priority found by the separate main-path log. Re-shot only affected frames and repeated the main-path voice walk; no second audit or full review.

#### Left open

- Spec decisions: sweepable discovery counter, five slogans versus three seconds, free-event classification, and the flakes/rings change when Pictures is removed. The latter changes the pictured food as well as presentation, so the class comparison does not isolate presentation perfectly.
- Default browser voice is a fallback, not a verified Rasalgethi/excited performance. No audio was recorded. The plain-bowl-start host line stays unspoken because host speech must not overlap an ad.
- Shared Motion preference persists under STANDARDS; votes/discoveries do not. No shared engine or audit script was changed.
- Driver's 60-second evaluation limit interrupted a combined timing batch; the smaller 3/3/2-run batch verified every version. One harness favicon 404 was not a tool request; subsequent targeted host batch had zero errors.
- Preview cleanup initially missed seven Python server children behind the launcher. Exact tool/host process matching closed them; final assigned ports are closed.
- Procedural deviation: initial brief reads/search lacked an explicit process timeout and returned promptly. Subsequent commands used bounded runners. Restarted interrupted cold flows and did not claim their missing output as evidence.
- Owned Chrome/server sessions are closed; host.html is absent. No commits. Evidence and final hashes: _scratch/cereal-ad-questions/review-validation.json.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Cereal Ad Questions build handoff

#### Structure

`src.html` uses the kit starter's header, kit controls, palette variables and Curio.voice. All activity code is in one readable IIFE.
The three mode containers and every frequent control retain their DOM identities. Only TV paintings, chart bars and day-scene objects rebuild.
The ART table contains each bundled image token once. There are ten named paintings, including two Comet poses.
`paintTV` places paintings over a softly blurred copy so the entire bowl remains visible in unusually wide TVs.
`frame` owns the fifteen-second ad and three-second clip clocks. Motion changes transformations, never elapsed time.
The jingle uses the kit AudioContext with a dedicated, disconnectable bus. No audio was recorded.

#### Votes and interruption

`finishedKey` identifies the last completed switch combination. Live switch changes label the current run; its final combination owns the next votes.
Votes during a new run still belong to the previous completed version. New playback and post-play switch changes commit that pair.
Finishing the new run commits any edits made during playback, then starts its fresh poll at zero. Replayed versions replace their earlier poll.
`chartOrder` preserves first-play order despite numeric-looking object keys. The latest count overwrites a version's old bars.
Both vote steppers clamp zero through forty. When a stepper disables under focus, focus moves to its enabled opposite with preventScroll.
Switches and Stop act synchronously. Turning Words on mid-shot waits for the next shot's line. Turning it off cancels speech immediately.
Host events have a not-playing validity guard. Read stops the ad before speaking. Mode switches and resets hush the voice queue.
How-to lines use Curio.voice's heard set, while results, switch announcements, truth cards and hotspot discoveries are events.

#### Spec decisions and ambiguities

- There are no explicit open-question choices in this spec.
- The Art section says eleven images but names ten. All ten named assets were generated and used. No extra unnamed image was invented.
- The three-second Words clip cannot contain all five clearly spoken slogans. It plays the opening slogan over the plain bowl for three seconds. The full ad contains all five. This is a reported spec limitation.
- Message part controls use one persistent evidence strip beneath the TV and cards, enabled for the selected card. This keeps all five choices and all sixty-pixel controls visible in compact frames rather than expanding a card over its neighbors.
- The plain-bowl start host line conflicts with the rule that host lines never play during an ad. The plain bowl appears immediately; that start line is not automatically spoken. The big question is an event after voting.
- Cold review restored a genuine family portrait inside the breakfast frame, marked people:true. The three scenes otherwise retain their painted style.
- Pictures-off and Words-off contain no in-ad marketing text. The TV casing retains its fictional-ad label, which is an interface label.
- The Sources timing rounds the loop tail to 0.4 seconds. The exact remainder is 0.454545 seconds. Other supplied contrast values match to rounding.
- Nothing saves votes, discoveries or message selections. The shared kit remembers Motion as required by STANDARDS.md.
- News-reader Rasalgethi and the separate announcer performance are specified in voice/lines.json. Build forbids recording, so the browser fallback is used and does not reproduce those performances.
- The report is written last because the user's explicit instruction requires stopping as soon as it is written.

#### Engine changes wanted

- No kit change is required. Optional future kit capability in `kit/curio.js`, Motion initialization and `init` handler: allow an in-memory preference when a spec requests no persistence. This build follows the standing requirement to remember Motion.
- Audit helper improvement, `scripts/audit_tool.py`, `MODES_JS`: recognize `.seg button` inside a navigation region without requiring a header ancestor. The current selector misses this tool's separate mode navigation. Explicit states and manual input checks covered both other modes, but the automatic per-control walk covered the initial mode only.

#### Checks and next owner

Scratch is `S:/CurioClass-codex/_scratch/cereal-ad-questions`. All child commands have bounded runtimes.
Muted Chrome uses ports 9970 through 9973; host port 8775. The host is stopped after its frames and host.html removed.
The full seven desktop sizes plus 375-wide iframe were shot once across all three modes. Targeted repairs may have newer frames.
Functional evidence covers all eight fifteen-second combinations, live audio and picture switches, both count bounds, fifteen clips, five truth cards, eighteen hotspots and reset.
See the final report for audit leads and visual evidence. The cold review is documented in codex-review.md. No commits or additional polish round.

#### Final build repairs and audit limits

The one full audit completed with 53 leads. Its initial sizes, Motion off, resize stress and repeated-click voice checks were clean.
Thirty-eight leads concern intentional labels drawn on tappable signs; two concern the background hint behind an open modal; five concern correctly skipped first-tap welcomes.
Five phone counter overlaps and three same-mode welcome cuts were fixed after that audit. No full audit was rerun.
Additional targeted repairs clear the playing badge on Stop, restore hints after Escape, hush stale card welcomes, remove sign-covering checkmarks,
and preserve painting proportions in portrait layouts. Targeted frames and JSON assertions in Scratch document those changes.
The news-reader and announcer recordings, the all-five-lines Words clip conflict, and the unspoken plain-bowl start line remain for owner review.

#### Cold review repairs

The first-vote how-to and first plain-bowl question now start immediately, superseding the already-answered vote prompt. The big question repeats on a new completed plain-bowl poll, once per poll. Hotspot narration switches immediately to the selected object; the completion line drops if that object is no longer selected.
The chart highlights the current completed poll and gives a small count/bar response, suppressed with Motion off. Fictional selling copy now appears on the tablet banner, billboard and bus poster. The breakfast family-photo asset has been redrawn and marked people:true in prompts.json.
Source URLs and the corrected 2015 CSPI date are in notes.md. Review evidence uses Chrome 9940-9947 and host 8745, all owned sessions closed after checks.

#### Sensitivity

The breakfast keepsake now shows a family with varied skin tones. Review its warmth, representation and clarity at final size; it is one family, not a template for all families. Avoid judging children or families by their food choices or whether an ad changes their opinion. No nutrition or body-health claim is made.

#### Review limits needing a spec decision

Five spoken slogans cannot fit a clear three-second Words clip. The existing opening-only clip remains explicit. The day hunt is specified as reveal-on-tap exploration, so sweeping all targets completes the discovery counter without proving ad recognition; adding a prediction gate would change the interaction spec. The plain-bowl artwork also changes rings to flakes as specified, so it does not isolate presentation perfectly.

Additional review repairs: the dense eight-version phone chart uses horizontal bar pairs with readable counts; sparse charts retain their vertical bars. Box text and painting now share one SVG coordinate system, with measured fitting on resize, so lettering stays on the blank panel at 760 wide and during motion. Safety-sign explanations now name their function precisely, matching FHWA and OSHA guidance; voice/lines.json matches.

#### Final cold review verification

One review audit completed with 62 raw leads. Its desktop states, Motion off, repeated input and resize checks completed; its phone execution-context discovery failed. Independent drive.py iframe checks cover the phone. The retained audit snapshot predates two narrow corrections: compact final-shot caption headroom and immediate switch-event priority. Focused frames and the final held-click voice walk verify those corrections without another audit.

Review harness limit: the phone audit returned no iframe execution context. Cleanup later discovered seven preview-server children that survived termination of the LibreOffice Python launcher. They were closed by an exact tool/host command match, and every assigned port was verified closed. Whether those surviving servers interfered with the audit host is unverified. Do not infer a tool defect or change Audit.size from this result alone. Independent phone frames and metrics are retained. The scratch preview helper now closes the matched host children as well as its launcher.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
