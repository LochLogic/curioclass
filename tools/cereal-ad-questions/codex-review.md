# Codex review: cereal-ad-questions

## Played

- Cold K-2 solo exploration and teacher/projector walk before reading codex-report.md, handoff.md, notes.md or src.html. Played all comparisons, five truths, three clips and eighteen objects. The loud ad becoming a quiet bowl is strong; the chart initially felt flat.
- One review pass, followed by repair checks. Workspace S:\CurioClass-codex; writes confined to this tool and its Scratch; no commits.

## Findings fixed

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

## Findings left

- Blocker, general, spec-bound hunt: tapping every object reaches 4 of 4 without recognizing an ad. Ran the sweep before and after fixes. The specified reveal-on-tap interaction cannot resist that route without a new prediction/check step, which this review may not add. Treat it as discovery, never a knowledge pass.
- Should fix, spec conflict: a three-second Words clip cannot clearly say all five slogans. Kept three-second timing and the explicitly labeled opening-only sample; full ad retains all five.
- Should fix, spec/source conflict: a free-event poster can still advertise an event. The spec calls this library poster Not an ad. Notes explain the narrower selling-message convention; changing the classification needs a spec decision.
- Should fix before final audio release: specified news-reader and excited-announcer recordings remain absent. Browser fallback works, but identity, performance and complete last-slogan pacing are not acoustically verified. Recording is prohibited in this workflow.

## Break it

- Vote gate: attempted both pluses and minus before watching; counts stayed zero and no chart was created.
- Bounds: 45 held clicks per plus stopped at 40 each; repeated subtraction stopped at zero. Both 40s are allowed by the spec, not a class-size estimate or achievement.
- Ownership/chart: changed switches, voted during a replay, and replayed the same version. Old-poll edits stayed with their completed owner; the new poll reset to zero; a replay replaced its own prior bars. Keep it preserved work; confirmed reset cleared votes/chart and restored switches.
- Timing/parts: all eight real-time runs ended at 15000 ms with the correct owner and words/pictures. Music node mute observed in 0.8 ms, immediate plain picture, Words restored next shot, Stop cleared playback/nodes. Acoustic latency was not measured.
- Hunt: non-ads added zero; five repeated taps on one ad added one; sweeping six objects reached four. No saved best, accuracy score or timer exists. The sweep remains the named spec blocker above.
- Message/truth cards: tried every card and all fifteen part paths. Each clip stopped at 3000 ms; truths opened for all five. This mode offers discussion evidence, not a correctness pass. The strength question asks conditionally and assumes no mistake.
- Reflection: unchanged/zero Want it votes are permitted. No prescribed decrease, percent badge, right-option position or reflection gate forces a desired answer.

## Voice walk

- Final: Play, vote, Music off, Play, vote, Pictures off, Play, vote, Words off, Play, vote; repeat plain-bowl poll; What it wants, card, three clips, True?, close; Ads in my day and all six breakfast objects. Held 120 ms; two-second gaps between actions, full waits for ad/clip playback; Sound on, Motion on.
- Heard in order: vote, remove Music how-to, Music off, vote, Pictures off, vote, Words off, vote, big question; new poll vote/big question; message welcome, card title/part instruction, clip-done how-to; truth; day welcome and each current discovery. First Play may skip the welcome under BASELINE 16; hint and Read retain it.
- Counts: remove how-to 1; clip-done how-to 1 then silent repeats; big question 2 for 2 polls, not 3 for 3 button taps; repeated same hotspot event 5 for 5 taps. No host line starts during the ad. Changed safety lines separately shown and spoken.
- Read works with Sound off, interrupts playback before speaking, and mode changes clear its stale context. Final allLines and voice/lines.json match exactly. Logs: voice-checked-flow-result.json, hunt-repeat-and-misses-review-result.json, read-off-and-mode-review-result.json.

## Facts checked

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

## Sensitivity

- No cultural, religious, Indigenous or historical claim. Review the new family portrait for respectful representation; it shows one family, not a norm for all families. It has varied skin tones and no stereotype noted. Asset people:true; review-family-contact.png includes asset and phone context. Avoid shaming food preferences or unchanged votes.

## Flattest moment left

- The silent fifteen-second plain-bowl replay intentionally waits for class observation. Its clock makes the wait legible. The chart now responds and identifies the current poll; extending this with new gameplay would change the brief.

## Graphics

- All ten named paintings inspected in contact sheets and final-size scenes, including all five ad shots, three day scenes, both mascot poses and toy card. Spec says eleven but names ten; no art token is missing.
- Redrew day-breakfast with built-in imagegen; final raw tools/cereal-ad-questions/art/raw/day-breakfast.png, final art/day-breakfast.webp. Full prompt/provenance in art/prompts.json. Existing art retained. One coherent glossy commercial set and deliberately quieter painted day/bowl set.
- 807312 art bytes; final bundle 1156037 bytes, about 1129 KiB. review-bar-comparison.png compares current art with the existing local Beat Lab reference frame.
- Looked at all review-matrix frames/contact sheets, review-target, review-phone-final, review-final-frames, review-last-targets, review-checks, review-live and cold-play frames. Every STANDARDS size covered, including 375 inside host 8745; grayscale, Motion off, extreme counts and keyboard-only flow checked.

## Audit

- One audit completed within its 2400-second limit: review-audit/audit.md, 62 raw leads. All 51 saved frames were opened in review-contact/review-audit-0.png through -8.png; the compact caption finding was also checked full size.
- Two real caption-overlap rows concerned the same 680-wide final shot at ordinary and maximum votes. Reserved caption headroom with readable package lettering; focused 680/800/1366/375 re-shoots and geometry checks cover the final fix.
- Fifty-one sign/hotspot overlap rows are intentional labels on their objects. Labels remain legible above the glow and have pointer-events:none. No tappable choices are hidden.
- Two covered-hint rows are the background hint behind open dialogs. The dialog supplies the current answer/confirmation; Read speaks it. Confirmed in frames and keyboard/Read checks.
- Two phone-harness rows mean iframe context not found and consequently no hint detected. Audit phone coverage is unavailable; separate 375-wide host runs cover all modes, charts and repaired art. No claim the audit passed its phone check. Orphan preview-server children were found and closed later; their possible effect on that harness is unverified.
- Five first-action welcome skips are permitted by BASELINE 16: three part switches, Play and Start over have their own action/context. No delayed welcome was added.
- Seven desktop opening sizes, focus/targets, Motion off, held-click repetitions, quick taps and completed resize stress had no other mechanical failures. All listed work states were exercised at their requested desktop sizes.
- The audit does not discover mode navigation outside a header; its per-control walk covers the opening controls/mode entries. Explicit states and independent clip/hotspot/keyboard walks cover both other modes. Shared scripts were not edited.
- The final bundle contains two focused post-audit corrections: caption placement and switch-event priority found by the separate main-path log. Re-shot only affected frames and repeated the main-path voice walk; no second audit or full review.

## Left open

- Spec decisions: sweepable discovery counter, five slogans versus three seconds, free-event classification, and the flakes/rings change when Pictures is removed. The latter changes the pictured food as well as presentation, so the class comparison does not isolate presentation perfectly.
- Default browser voice is a fallback, not a verified Rasalgethi/excited performance. No audio was recorded. The plain-bowl-start host line stays unspoken because host speech must not overlap an ad.
- Shared Motion preference persists under STANDARDS; votes/discoveries do not. No shared engine or audit script was changed.
- Driver's 60-second evaluation limit interrupted a combined timing batch; the smaller 3/3/2-run batch verified every version. One harness favicon 404 was not a tool request; subsequent targeted host batch had zero errors.
- Preview cleanup initially missed seven Python server children behind the launcher. Exact tool/host process matching closed them; final assigned ports are closed.
- Procedural deviation: initial brief reads/search lacked an explicit process timeout and returned promptly. Subsequent commands used bounded runners. Restarted interrupted cold flows and did not claim their missing output as evidence.
- Owned Chrome/server sessions are closed; host.html is absent. No commits. Evidence and final hashes: _scratch/cereal-ad-questions/review-validation.json.
