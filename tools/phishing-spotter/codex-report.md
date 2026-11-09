# Codex report: phishing-spotter

## Built
- Build only in S:\CurioClass-codex. No commits, deployment or polish round.
- Three modes, all 20 specified messages, engine-rendered emails/texts/sign-in pages, clickable evidence, address book, timed Arcade and local Best.
- Required source, draft metadata, teacher notes, eight voice lines, audit states, preview, handoff and 15 painted assets are present.
- Final offline bundle: 410,018 bytes, 400.4 KB. SHA-256: adfb072169bba0c19972648f40c68d3680bd29f2ab60a3e4bdfd59df815e41d6.
- Source has normal line breaks, maximum 151 characters per line, and no em dashes.
- Evidence below lives in ../../_scratch/phishing-spotter/.

## Numbers check
- content.py independently parsed the spec and checked the pool, spot mappings, domains, fictional phone range and contrast.
- 20 messages: 10 phishing and 10 safe. Maximum score = 10 × 2 + 10 × 1 = 30.
- Actual maximum is five spots, within the spec's six-or-fewer bound. All are reachable with keys 1 to 8.
- Clocks: 60,000 ms round, 4,000 ms tell, 1,500 ms wrong-call result. The tell clock runs inside the round.
- Contrast ratios reproduced exactly: 12.22, 10.93, 10.61, 16.23, 7.29, 15.91, 6.47, 6.39, 7.43, 10.27, 11.38, 6.34. All exceed AA for ordinary text.
- Evidence: numbers.json, functional-results.json, build-stats.json. No numerical contradiction with the spec.

## Facts checked
- Fictional names, message bodies, subjects, dollar fee, gem prize, dates, deadlines and safe-message reasons come from spec.md, Content. They describe invented scenarios.
- T1 look-alike sender, T2 wrong destination and T7 copied sign-in appearance: [NIST phishing guidance](https://www.nist.gov/itl/smallbusinesscyber/guidance-topic/phishing) and [FTC phishing guidance](https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams).
- T3 urgency/threat: NIST phishing guidance above; [FTC fake emergency guidance](https://consumer.ftc.gov/articles/scammers-use-fake-emergencies-steal-your-money).
- T4 requests to send passwords or codes: FTC phishing guidance and [FTC verification-code guidance](https://consumer.ftc.gov/consumer-alerts/2024/03/whats-verification-code-why-would-someone-ask-me-it).
- T5 unexpected rewards and T6 unexpected files: FTC phishing guidance above.
- T8 secrecy: FTC fake emergency guidance above and [FTC scam warning signs](https://consumer.ftc.gov/consumer-alerts/2025/05/avoid-gift-card-scams-mothers-day).
- Inspect links, avoid suspicious replies/files, report and check by a known independent route: FTC and NIST guidance above. Trusted-adult wording follows the spec's middle-school response.
- Normal deadlines, an expected teacher file and opening an app yourself: the spec's safe examples apply those contextual checks. Teacher notes explicitly avoid treating a matching sender as universal proof of safety.
- Reserved .example and .test domains: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606), updated by RFC 6761. Every actual pool address passed Sec.safeDomain; evil.com was rejected in the test harness.
- Fictional 555-01xx local numbers: [NANPA reserved range](https://nanpa.com/numbering/555-line-numbers).
- Standards MS-SYS-SE-32 and MS-SYS-SE-33 exist at data/standards/csta-2026-ids.txt:195-196. The solo activity recognizes attacks and chooses a defensive response; the 2017 crosswalk is the spec's 2-NI-05.
- Both specified CISA URLs returned HTTP 403. Reachable FTC and NIST primary sources corroborated the teaching; no extra student topics were added.
- Current source checks were made during this run.

## Break it
- 159 functional assertions passed, plus eight long-press checks and five additional regression assertions.
- Blind Keep spam: 10/30. Report plus first-spot spam: 14/30. Neither sets a full score.
- Report, tap a wrong spot, then sweep correct spots: stays +1 with no tell bonus.
- Passing multiple spots to answer(): only the first is evaluated. A wrong first spot cannot be rescued.
- Repeated taps on a finished message add nothing. show() refuses an already-scored message during a round.
- All five scoring outcomes checked: safe Keep +1; phish Report/right tell +2; wrong tell/timeout +1; phish Keep 0; safe Report 0.
- Pending phish report when the round clock expires: +1, one answered message, then round ends.
- Perfect round: 30 points, 20 right calls, 10 tells, 20 unique messages, early time remaining.
- Keep during Missed answered a controlled next safe message immediately. Report during False alarm answered the next phish and its tell immediately.
- Mode switch mid-round left no card and saved no Best. Yes/No clearing worked. Blocked storage did not crash scoring or clearing.
- Found and fixed: Play again after a timed-out round examined the old expired clock before resetting it. Reset now precedes the first message.
- Practice has no score or mastery gate. Selecting every spot only opens the explanation. Tells ticks record visits, not correctness.
- Best is bounded to 30 and saved only on a completed round. It remains a practice score, not a security certification.
- The required developer hooks expose test state. This is a local practice tool, not a tamper-proof assessment.
- Evidence: functional-results.json, extra-regressions.json, longpress.json, extremes.json.

## Voice walk
- Real held clicks, approximately two seconds apart, with default Sound: inspect first link, Report, select sender, Done, Next, Arcade, Start round, one call, natural 60-second expiry, Tells, fake-page example, keyboard Report/tell/Done, Read.
- Spoken starts in order: w-practice, tell, next, w-arcade, go, end, best, w-tells.
- Each how-to started once. First taps can cut speech; current instructions remain in the hint and Read.
- Side keyboard path reached the fake-page Why card. Read spoke the current Next hint.
- A further two-round test logged go, end, go, end. No automatic message or result narration played during the clock.
- The book dialog closed when time expired, exposing the round card and Play again.
- Main walk: zero console errors and zero network resources. Evidence: walk/voice-walk.json, repeat-voice.json.
- No voice audio was recorded in this Build-only run. Eight authored Sadachbia/lively-host lines use the kit's browser fallback.

## Feel check
- Best moment: the convincing Pebble Quest page stays visually identical to the real page; catching its address produces the tell glow, painted facade icon and +2.
- First flat moment: replay after a timeout could end immediately. Fixed the clock reset order and tested expiry/replay.
- Second flat moment: compact Tells captions spilled beyond their cards. Rebuilt compact card grids, widened the 760-pixel layout to two columns and enlarged spacious-screen art.
- The storefront first looked like a real shop. Redrew it with a visible cardboard brace.
- Played the main and side student paths across all modes, including an actual 60-second round. The first link tap reveals its destination immediately.
- Opened Scratch bundles of Snowy Mail Route and Beat Lab before implementation.
- Looked at feel-comparison.png and cabinet-comparison.png beside Beat Lab. Painted objects, cabinet lighting, readable evidence and responsive feedback provide the intended finish.
- Reward is a record of this player's calls and tells. No confetti or invented certification.

## Done when
1. PASS: all 20 messages render and all pool addresses pass the security engine. Fictional content fields and every tell mapping checked.
2. PASS: all eight links show actual destinations on hover, focus and long-press; clicks remain inside the page.
3. PASS: all five Arcade outcomes and expiry during a pending report checked through the specified hooks.
4. PASS: unique 20-message round, early finish, exact totals, saved Best and Yes/No clearing checked.
5. PASS: every listed tell appears in Practice Why; all safe reasons match Content, including S8's site-name explanation.
6. PASS: fields are non-editable, read-only textboxes. A real held field click displays the lock note; typing cannot enter data.
7. PASS for targeted layouts: central message screen, readable text and main controls measured in every specified size and mode, including the 375-pixel host.
8. PASS: immediate next-message input during both wrong-call pauses; abandoning a round saves nothing.
9. PARTIAL verification: real R, 1 and Enter path passed with visible focus. K and remaining spot-key mappings were checked in source; the full keyboard audit did not run.
10. PASS: room, six emblems and eight tell icons load; real/fake pages use the identical painted logo.
11. PASS in targeted walks: welcomes/how lines, repeated Go/Time, Read, clean console and offline resources. Browser voice remains the Build-only fallback.

## Wave lessons
- Hint and voice: PASS in held-click main/side walks. Hints change synchronously; no stale automatic Arcade chatter.
- Focus and layout: PASS in targeted student paths. Static action buttons survive artifact changes; focus returns with preventScroll.
- Sizes: PASS main controls at all eight sizes. Generic all-target overlap/clipping audit remains unverified.
- No giveaways: PASS by DOM/source review and spam tests. No P/S ids, correctness badges or tell labels appear before commitment.
- Honest numbers: PASS. Maximum 30, first tell attempt, four-second window, streak without multiplier and local-only Best are stated.
- Standards: PASS within the spec's phishing scope. Students inspect evidence and choose a defensive response; family engine unchanged.
- Motion off: PASS. No running infinite animation; ring becomes a count and clock timing remains real.
- Short choices in view: PASS targeted Tells frames and geometry, all eight cards visible at every size.
- Resize mid-animation: PARTIAL. Layout is CSS and does not rebuild artifacts; automated resize stress was unavailable after audit failure.
- Deferred welcome: PASS. First action is immediate; three mode welcomes start on the real path.
- Unknown shown as unknown: PASS. Link destination is inspected through the engine's status bar; no premature correctness marks.
- One look, one meaning: PASS in color and grayscale. Result words, icons and outlines accompany colors.
- Badge truth: PASS. Right calls, tell count and Best derive from committed history; no mastery badge.
- Hint changes back: PASS through Next, mode changes, tell selection, result and replay paths.
- No copying answer words: PASS. Initial clues are the specified messages; tell names arrive after a call or in the explicit Tells reference.

## Audit leads
- FAIL / audit not finished. The single required audit was attempted last using Chrome 9981 and host 8785, with a 40-minute command bound.
- It exited after about 2.5 seconds with ConnectionResetError, Windows error 64, while opening the first CDP WebSocket.
- No first size result, audit.md or page-level leads were produced. See audit/failure.txt.
- No workaround or second audit was run. The next reviewer should run the mechanical audit.
- After the failed attempt, neutralized the idle round's wording so zero answers receive no implied praise; re-bundled and syntax checked.

## Frames looked at
- bar-frames/: both references. first-frames/: laptop, preview and Tells.
- test-frames/, retry-frames/, functional-frames/ and focus-debug/: all diagnostic and final frames, including failed-test states.
- size-frames/: Practice, Arcade and Tells at 680×425, 800×500, 1000×625, 1280×720, 1366×768, 1920×1080 and 760×900.
- phone-frames/: all three modes at an actual 375×812 iframe.
- walk/: evidence payoff, Arcade feedback, natural expiry, Tells and keyboard Why.
- extreme-frames/: all six, including +2, perfect record, grayscale and Motion off.
- targeted-frames/: all six enlarged-art, compact Why and book frames. last-frames/: all three.
- All generated PNGs in these evidence groups were opened and inspected; both comparison sheets and final art sheet were inspected.
- Earlier 800-pixel clipping and compact Why overflow were fixed and re-shot only where touched.
- The final phone-header grid adjustment has static review but no new phone frame because the audit failed before it could capture one.

## Art made
- 15 final paintings from 16 image-tool generations: one arcade room, six emblems, eight tell icons; one storefront redraw.
- Full prompts and provenance: art/prompts.json. Built-in OpenAI gpt-image, followed by art.py --rekey for every finished WebP.
- Final art: 207,476 bytes, 202.6 KB. Voice: 0 KB recorded. Bundle: 410,018 bytes, 400.4 KB against the 2,048 KB goal.
- Initial budget was 220 KB art plus 350 KB voice. Build-only browser narration leaves that voice allowance unused.
- All people flags are false. The theater mask is an object, not a person. Finished images were inspected in cards and the contact sheet.
- Generated-path evidence and comparison frames stay in Scratch; required raw PNGs stay in art/raw/.

## Art still to paint
None. No placeholders or missing people art.

## Engine changes wanted
None. The injected stylesheet ordering workaround is local to this tool.

## Left open
- Full mechanical size/state/resize/walk audit: unavailable due the initial Chrome/CDP connection reset.
- Fresh frame for the last phone-header grid adjustment and a complete real-key sweep.
- Fixed Sadachbia recordings belong to the later voice pass; browser fallback is active now.
- Both CISA pages returned 403; reachable primary FTC/NIST guidance was used for corroboration.
- Initial quick file reads lacked explicit deadlines. All build processing, bundles, browser batches and the audit were bounded.
- One early host run failed; the smaller retry worked. An initial host favicon 404 was fixed in the temporary host fixture; subsequent host shots were console-clean.
- Some background host processes survived taskkill. Identified three exact phishing-spotter server command lines and terminated only those processes with psutil.
- Final cleanup verified: assigned ports 9980 through 9987 and 8785 closed; no scoped Chrome remained; host.html absent. Evidence: final-verification.json.
- No unanswered spec questions, commits or polish work. Stop at this report.
