# Phishing Spotter: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: phishing-spotter

#### Built
- Build only in S:\CurioClass-codex. No commits, deployment or polish round.
- Three modes, all 20 specified messages, engine-rendered emails/texts/sign-in pages, clickable evidence, address book, timed Arcade and local Best.
- Required source, draft metadata, teacher notes, eight voice lines, audit states, preview, handoff and 15 painted assets are present.
- Final offline bundle: 410,018 bytes, 400.4 KB. SHA-256: adfb072169bba0c19972648f40c68d3680bd29f2ab60a3e4bdfd59df815e41d6.
- Source has normal line breaks, maximum 151 characters per line, and no em dashes.
- Evidence below lives in ../../_scratch/phishing-spotter/.

#### Numbers check
- content.py independently parsed the spec and checked the pool, spot mappings, domains, fictional phone range and contrast.
- 20 messages: 10 phishing and 10 safe. Maximum score = 10 × 2 + 10 × 1 = 30.
- Actual maximum is five spots, within the spec's six-or-fewer bound. All are reachable with keys 1 to 8.
- Clocks: 60,000 ms round, 4,000 ms tell, 1,500 ms wrong-call result. The tell clock runs inside the round.
- Contrast ratios reproduced exactly: 12.22, 10.93, 10.61, 16.23, 7.29, 15.91, 6.47, 6.39, 7.43, 10.27, 11.38, 6.34. All exceed AA for ordinary text.
- Evidence: numbers.json, functional-results.json, build-stats.json. No numerical contradiction with the spec.

#### Facts checked
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

#### Break it
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

#### Voice walk
- Real held clicks, approximately two seconds apart, with default Sound: inspect first link, Report, select sender, Done, Next, Arcade, Start round, one call, natural 60-second expiry, Tells, fake-page example, keyboard Report/tell/Done, Read.
- Spoken starts in order: w-practice, tell, next, w-arcade, go, end, best, w-tells.
- Each how-to started once. First taps can cut speech; current instructions remain in the hint and Read.
- Side keyboard path reached the fake-page Why card. Read spoke the current Next hint.
- A further two-round test logged go, end, go, end. No automatic message or result narration played during the clock.
- The book dialog closed when time expired, exposing the round card and Play again.
- Main walk: zero console errors and zero network resources. Evidence: walk/voice-walk.json, repeat-voice.json.
- No voice audio was recorded in this Build-only run. Eight authored Sadachbia/lively-host lines use the kit's browser fallback.

#### Feel check
- Best moment: the convincing Pebble Quest page stays visually identical to the real page; catching its address produces the tell glow, painted facade icon and +2.
- First flat moment: replay after a timeout could end immediately. Fixed the clock reset order and tested expiry/replay.
- Second flat moment: compact Tells captions spilled beyond their cards. Rebuilt compact card grids, widened the 760-pixel layout to two columns and enlarged spacious-screen art.
- The storefront first looked like a real shop. Redrew it with a visible cardboard brace.
- Played the main and side student paths across all modes, including an actual 60-second round. The first link tap reveals its destination immediately.
- Opened Scratch bundles of Snowy Mail Route and Beat Lab before implementation.
- Looked at feel-comparison.png and cabinet-comparison.png beside Beat Lab. Painted objects, cabinet lighting, readable evidence and responsive feedback provide the intended finish.
- Reward is a record of this player's calls and tells. No confetti or invented certification.

#### Done when
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

#### Wave lessons
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

#### Audit leads
- FAIL / audit not finished. The single required audit was attempted last using Chrome 9981 and host 8785, with a 40-minute command bound.
- It exited after about 2.5 seconds with ConnectionResetError, Windows error 64, while opening the first CDP WebSocket.
- No first size result, audit.md or page-level leads were produced. See audit/failure.txt.
- No workaround or second audit was run. The next reviewer should run the mechanical audit.
- After the failed attempt, neutralized the idle round's wording so zero answers receive no implied praise; re-bundled and syntax checked.

#### Frames looked at
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

#### Art made
- 15 final paintings from 16 image-tool generations: one arcade room, six emblems, eight tell icons; one storefront redraw.
- Full prompts and provenance: art/prompts.json. Built-in OpenAI gpt-image, followed by art.py --rekey for every finished WebP.
- Final art: 207,476 bytes, 202.6 KB. Voice: 0 KB recorded. Bundle: 410,018 bytes, 400.4 KB against the 2,048 KB goal.
- Initial budget was 220 KB art plus 350 KB voice. Build-only browser narration leaves that voice allowance unused.
- All people flags are false. The theater mask is an object, not a person. Finished images were inspected in cards and the contact sheet.
- Generated-path evidence and comparison frames stay in Scratch; required raw PNGs stay in art/raw/.

#### Art still to paint
None. No placeholders or missing people art.

#### Engine changes wanted
None. The injected stylesheet ordering workaround is local to this tool.

#### Left open
- Full mechanical size/state/resize/walk audit: unavailable due the initial Chrome/CDP connection reset.
- Fresh frame for the last phone-header grid adjustment and a complete real-key sweep.
- Fixed Sadachbia recordings belong to the later voice pass; browser fallback is active now.
- Both CISA pages returned 403; reachable primary FTC/NIST guidance was used for corroboration.
- Initial quick file reads lacked explicit deadlines. All build processing, bundles, browser batches and the audit were bounded.
- One early host run failed; the smaller retry worked. An initial host favicon 404 was fixed in the temporary host fixture; subsequent host shots were console-clean.
- Some background host processes survived taskkill. Identified three exact phishing-spotter server command lines and terminated only those processes with psutil.
- Final cleanup verified: assigned ports 9980 through 9987 and 8785 closed; no scoped Chrome remained; host.html absent. Evidence: final-verification.json.
- No unanswered spec questions, commits or polish work. Stop at this report.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: phishing-spotter
#### Played
- Cold as a grade 7 student: Practice, the full 20-message pool, a blind Arcade round and Tells before reading the builder's report, handoff, notes or source. Then a teacher-style evidence comparison and a natural 60-second voice walk. The cabinet and convincing fake pages are strong; the original recap felt flat.
- Root verified as S:\CurioClass-codex. One review pass, scoped repairs and rechecks; no commits or shared-kit changes. Evidence below is in ../../_scratch/phishing-spotter/.
- Teaching, Play and Craft lenses covered evidence accuracy and transfer, cheap scoring paths and the recap, then art, layout, keyboard and voice. Findings below name their rule scope and severity.
#### Findings fixed
- Should fix, family:security, compact Practice: the 680x425 preview hid the link and its destination bar. Pinned the engine's existing status node outside the message scroller, shared its row with results, and reclaimed cabinet-header space. Kept 44-pixel spots and the painted scene.
- Blocker, general, Practice evidence success: Done accepted no evidence or every spot with the same green success. Success now requires each distinct tell type and no extras; extras have a dashed warning and Not a tell label. Why reports missing/extra evidence without preventing learning.
- Should fix, family:security, Why: tell names alone did little explaining. Why arrows now show the actual sender/site comparison or the tell's explanation in the result strip.
- Should fix, general, safety wording: safe-case feedback could make matching senders sound conclusive. Added the independent-check caveat beside safe explanations and scoped the result to this fictional case; preserved the specified cases.
- Should fix, general, Tells: unexplained ticks resembled achievement marks. They now say Opened and only record visits.
- Polish, general, flattest moment: added a key and a personal next step to the round record, based on actual missed phish, false alarms or reports lacking tells. Compact records put that guidance in view. Partial runs receive counts, not full-set praise; count labels work at zero and one.
- Should fix, general, phone: the Best privacy note inherited display:none. Restored the visible local-only note beside the phone's Clear best control.
- Polish, graphics: redrew ps-tell-7 with a broad cardboard back, thin front and two visible braces. Kept the rest of the illustrated set and cabinet finish.
- Should fix, general, documentation: removed the unsupported claim of whole-standard CIA-triad coverage; teacher notes now state the actual phishing scope. Shared mapping remains below.
- Should fix, general, dialogs: Address book and Clear best now replace the underlying hint with their own how-to, restore the live game hint on close, and suppress automatic speech during a running Arcade clock.
- Should fix, general, audit: raised the compact Tells target to 44 pixels, fitted Address book beside the compact Why instruction, and shortened the safe-page explanation while retaining both domain comparisons.
- Blocker, family:security, evidence mapping: the account-closing subject is valid T3 urgency, but was scored as a wrong tell. Accepted it; Practice now counts distinct tell types, so repeated urgency/prize phrases are not a pixel hunt. A blind first-spot strategy consequently rises from 14 to 15/30, still below a full score.
#### Findings left
- Should fix, spec/catalog: MS-SYS-SE-32 requires explaining failures of confidentiality, integrity and availability. There is no integrity/availability activity here. The spec or module needs another tool for that code; adding one here or editing shared metadata exceeds this review's scope. MS-SYS-SE-33 is practiced through phishing/social engineering, not every attack type in its boundary statement.
#### Break it
- Arcade score/right-call/streak: blind Keep = 10/30, blind Report plus first spot = 15/30 and 5 tells. Neither reaches the full result. The specified base point for a phish report remains intentional; these are practice scores, not certification.
- All outcomes: safe Keep +1; phish Report with a correct first tell +2; wrong first tell or real four-second timeout +1; phish Keep 0; safe Report 0. A wrong-first then every-spot sweep stays +1. Repeated taps cannot add points to a committed message.
- Round/Best: perfect responses = 30, 20 right calls, 10 tells, 20 unique messages; early finish preserves time. A pending report gets +1 at expiry. Leaving mid-round saves no Best; Clear No preserves it and Clear Yes removes it. Keep/Report during wrong-result pauses answer the next message immediately.
- Practice: empty, wrong-only and select-all evidence receive comparison feedback without evidence-success styling. Each tell type without extras receives success; repeated phrases for one type are not required. Extra selections are explicitly marked, so sweeping cannot mimic an explanation.
- Tells: opening every card earns only Opened labels. No quiz, reflection gate, multiplier or mastery badge exists. The mandated developer hooks remain test hooks, not a tamper-proof assessment.
- Evidence: review-functional.json; links-after-real-tap.json; review-keyboard.json. Eight initial programmatic-focus checks ran in an inactive document; all eight passed after a real held tap. Their earlier failures are retained, not counted as product passes.
- Final checks: 129 functional assertions, 15 touch/resize checks and six keyboard checks passed. All eight held-touch links expose their true destination without navigating; sign-in fields reject typing. The first resize fixture dispatched mouse input before the viewport settled; with input modes separated and a render wait, live evidence scores and next-message controls survive both resizes. Earlier results remain in review-touch-before-final.json.
#### Voice walk
- Held 120 ms clicks at about two-second gaps: inspect link, Report, sender, Done, Why comparison, Next, Arcade, Start round, Keep, natural expiry, Tells, fake-page example, keyboard R/1/Enter, Read. Default Sound stayed on; current Motion preference was off. Separate frames/audit cover Motion on.
- Spoken starts: w-practice, tell, next, w-arcade, go, end, best, w-tells. No automatic message/result speech occurred inside the round. Read spoke the current Next hint; the repeated Practice how-to lines stayed silent with reason heard.
| Line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| w-practice | welcome | 1 | 1 |
| tell | how | 1 | 1 |
| next | how | 1 | 1 |
| w-arcade | welcome | 1 | 1 |
| go | event | 6 | 6 |
| end | event | 6 | 6 |
| best | event, new best only | 1 | 1 |
| w-tells | welcome | 1 | 1 |
- The five extra event rounds used shortened clock fixtures; the main round actually ran 60 seconds. Sound-off Read and a mode change were also exercised. No console errors or resource requests in the main walk. No recorded audio was made, as required by CODEX-BUILD; the kit browser fallback remains.
- Keyboard-only fresh-load path: Tab/Enter to Report, numeric evidence, Done, Next, K, Arcade start, Tells example, R/1/Enter. All six assertions passed, including no focus on load and visible focus on live Next. Evidence: review-walk/, review-keyboard.png.
- After dialog repairs, repeated the main path with Motion on. All 23 dialog assertions passed: five Book opens/closes, five Clear No choices, Clear Yes and expiry with Book open. Book and Clear each spoke once, then stayed silent as heard. Three Read-only Arcade hints and two dialog lines bring the authored total to 13; every line matches allLines. See review-walk-repair/.
#### Facts checked
- T1 look-alike sender, T2 wrong destination and T7 copied sign-in appearance: [NIST phishing guidance](https://www.nist.gov/itl/smallbusinesscyber/guidance-topic/phishing) and [CISA phishing/spoofing tip sheet](https://www.cisa.gov/sites/default/files/publications/phishing_and_spoofing_tip_sheet_2022_092022.pdf). Compared full site names, including pebblequest.example.signin-help.test; matching senders alone are not proof.
- T3 urgency/threat: NIST guidance above. T4 requests to send passwords or sign-in codes: [FTC verification-code guidance](https://consumer.ftc.gov/consumer-alerts/2024/03/whats-verification-code-why-would-someone-ask-me-it) and [FTC phishing guidance](https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams).
- T5 unexpected prizes and T6 unexpected files, including the suspicious invoice: FTC phishing guidance above. File extensions are warning context, not a claim that PDFs are universally safe.
- T8 secrecy: [FTC scam warning signs](https://consumer.ftc.gov/consumer-alerts/2025/05/avoid-gift-card-scams-mothers-day), which explains the attempt to isolate a target from trusted people.
- Hover/focus/press to inspect a destination, avoid suspicious replies/files, report, and check by a known independent route: CISA tip sheet and FTC phishing guidance above. Both original CISA pages returned 403; searchable official CISA text and reachable FTC/NIST corroborated the guidance.
- Normal deadlines, expected teacher files, saved contacts and opening an app yourself: the spec's S1-S10 contexts, checked against FTC's independent-contact advice. These remain invented examples, with an explicit caution against treating familiarity as proof.
- Every fictional organization, message, title, fee, prize, time and deadline: spec.md Content, P1-P10/S1-S10; independently checked rendered fields and spot mappings. Removed the unexplained P4 identifier from S8's explanation without changing its domain lesson.
- Reserved .example/.test domains: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) and [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761.html). Every pool address passes Sec.safeDomain; a real domain is rejected. Fictional 555-01xx numbers: [NANPA](https://nanpa.com/numbering/555-line-numbers).
- Numbers: 10 phishing + 10 safe = 20; maximum 10*2 + 10*1 = 30; at most five spots, within keys 1-8. Clocks 60/4 seconds and wrong-result pause 1.5 seconds match the spec. All 12 contrast ratios independently reproduced, minimum 6.34:1. Evidence: review-static.json.
- Standards: [CSTA 2026 PDF](https://csteachers.org/2026-csta-pk-12-computer-science-standards/), printed page 80. Confirmed the CIA-triad gap and narrowed local coverage claims; the spec's 2017 crosswalk is broader than this tool's digital-message activity.
#### Sensitivity
- None requiring a cultural lens: this is a fictional message simulator, not a cultural, religious, historical or body topic. No people are pictured; teacher names do not stand for a cultural tradition. All 15 art assets carry people:false; the theater mask is an object. An empty arcade backdrop is appropriate to the cabinet view.
#### Flattest moment left
- After several rounds, the fixed pool of 20 becomes familiar. Kept the specified pool and the quick reading/reasoning mechanic; more messages would exceed scope. The record now points to the student's actual next practice need.
#### Graphics
- Checked room, all six logos and all eight tell icons, plus the fake/real sign-in pairs. Redrew only the false storefront with the built-in imagegen tool; full prompt and provenance are in art/prompts.json, raw in art/raw/ps-tell-7.png, finished in art/ps-tell-7.webp. Checked the replacement at 72/108/144-pixel display sizes.
- Art 202.2 KiB; final bundle 406.8 KiB (416,525 bytes). No missing art tokens. Compared the retained cabinet and tell cards with Beat Lab in review-comparison.png; no simplification of the painted scene or evidence glow.
- Looked at cold, all eight size layouts, compact Tells/Why, phone modes/book/record, correct/wrong evidence, perfect and partial records, grayscale/Motion off, keyboard focus and the main voice-walk frames. Initial phone-script context errors and favicon 404 belonged to the fixture; corrected phone shots are console-clean.
#### Audit
- The one 40-minute-bounded audit finished: 16 leads. Confirmed and fixed seven layout leads: two narrow Tells targets, three clipped Address book entries, clipped safe Why, and clipped 1280x720 recap. Reserved Sound width too, because its first toggle moved the header.
- Five welcome-skip/cut leads are permitted by BASELINE rule 16, with hints and Read retained. The hidden demo Sign in button is inert, inside the deliberately scrollable fake page, not an answer choice. Three resize leads compare different shuffled message labels; the deterministic live-control resize recheck passed. Sound's remaining movement is at most 2.46 pixels.
- All 87 audit frames were inspected in review-audit-sheets/, with confirmed leads opened at native size. Scoped rechecks use the same geometry checks on changed states only; the full audit was not rerun.
#### Left open
- Shared standards mapping as described above. Authored bank-voice recordings belong to the later voice pass; browser narration was tested here.
- Unattended choices followed the spec: retained the scoring formula, 20-message pool, fast Arcade and matching real/fake logos; kept standard-mapping changes outside the authorized folders.
- The first quick read commands used the execution tool's wait bound, not a hard process deadline. All subsequent commands used explicit 30/120/180/300/330/2400-second limits; failed long scripts were retried smaller.
- Cleanup verified: Chrome ports 9960-9967 and host 8765 closed; host.html absent. All final checks passed in review-verification.json. No commits. Bundle SHA-256: e7ee2821a4100e40f6cc963f91300e38ae9a662e163c56fed0c71e464aaf4305.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Phishing Spotter handoff

#### Structure
`src.html` starts from the kit starter. The CSS draws a cabinet at real pixel size around the security engine's email, text and sign-in artifacts. The panel comes before the artifact in keyboard order. Compact landscape keeps the controls beside the screen; narrow portrait puts them below it. The address book becomes a dialog button where the full book would crowd the message.

`content.json` is loaded through the bundler's JSON token. It preserves all 20 specified messages and their tell-to-spot mappings. `Sec.world`, `Sec.artifact` and two `Sec.clock` instances supply the family behavior. No shared engine or kit file changed. The tool's stylesheet moves after the engine's injected stylesheet once, so its responsive overrides take effect.

State phases are `call`, `tell`, `why`, `ready`, `result`, `end`, and `explore`. Practice never scores. Arcade commits its first tell attempt, counts a message once, and cancels pending callbacks with a round serial on mode changes. The round clock resets before the first message, including after a natural timeout. At clock expiry, a pending phish report gets one point. Keep and Report during a result immediately answer the next message.

`window.__tool` exposes the required state, security engine, mode, message, answer and round hooks. It also exposes the clocks, artifact, message pool and voice log for reproducible tests. `show` refuses messages already scored in a running round.

#### Decisions and contradictions
- No open questions appear in this spec. Kept the spec's cyan accent, reserved fictional phone numbers and corrected S8 explanation.
- The older Art section names local FLUX and white backgrounds. The user's image-tool requirement and CODEX-BUILD key instructions take precedence: made 15 separate OpenAI gpt-image paintings on green or magenta where keyed. Every asset is marked `people: false`.
- BUILD.md says not to draw or record; the user and CODEX-BUILD explicitly require art. Made the paintings, authored all eight voice lines, and did not record audio. Browser narration is the Build-only fallback; Sadachbia is specified for later recording.
- CODEX-BUILD says to start the report at first bundle, while the user says to stop when it is written. Kept running evidence in Scratch and wrote the final report only after the checks, following the user's stop condition.
- The spec says no free option sweeping and also prescribes one point for reporting a phish without identifying a tell. Preserved that scoring, but the first wrong tell commits the message; later taps cannot recover the second point. Spam tests cannot reach 30. Tells-page ticks are visits, not mastery.
- At compact sizes, messages scroll within the screen because six 44-pixel spots, the status bar and a readable address cannot all fit at once. Keep, Report and the current step's control remain outside that scroller. Long sign-in addresses wrap. Tells definitions remain in accessible card names on the smallest layouts, with titles and mini examples visible.
- The address book remains accessible during Arcade; opening it does not pause either clock.
- Tell icons enlarge to 108 or 144 pixels on spacious screens, and stay 72 pixels in compact cards. This follows the build brief's art-first finish while preserving the spec's eight tells and examples.
- Current CISA URLs returned HTTP 403 during the source check. FTC, RFC and NANPA sources were reachable; NIST's current phishing guidance corroborated urgency, look-alike addresses, bad links and suspicious files without adding student topics.

#### Sensitivity
No real people are depicted. The masks are objects. All names, messages, places and phone numbers are fictional. No culture, religion, hard history, bodies or attack instructions are introduced. Phishing safety guidance is limited to recognition, reporting and independent checking. Teacher notes explain that a matching sender or saved contact is context, not a universal guarantee of safety.

#### Art
One full-stage painted arcade room, six emblems and eight tell icons. All are placed in the tool. The real and fake sign-in pages share the exact same painted logo. The cardboard storefront was redrawn once to make its prop brace visible. Prompts, people flags and provenance are in `art/prompts.json`; generated-path records and inspection sheets are in Scratch. Raw PNGs are retained under `art/raw/` as required by the brief.

#### Engine changes wanted
None. The tool works with the existing security engine. The injected-style ordering workaround is local to this file.

#### Cold review repairs
The link status node now sits directly before the result strip, outside the artifact scroller. Its engine event handlers and status handle are unchanged. Only one of link status and result is shown at once, preserving message space and making hovered, focused or pressed destinations visible in compact previews.

Practice clears selection marks before revealing the actual evidence, marks extra selections as Not a tell, and counts distinct tell types found and extra parts selected. Finding each tell type without extra parts receives the evidence-success wording. P1 subject and body both express T3 urgency; P9 repeats T5 in subject and body, so duplicate phrases are not required. Why buttons also explain the comparison in the result strip. Safe-case explanations include a caution that matching senders alone are not proof.

The round record keeps its point sequence, adds its key and a next step based on this player's missed phish, false alarms or reports without tells. Tells uses Opened labels for visits. The false storefront icon was redrawn with a larger cardboard back and two visible braces. Scoring rules are unchanged; P1's previously rejected urgency subject is now a valid tell. Two dialog how-to lines and three Read-only Arcade hints bring the authored total to 13. Dialogs restore the live game hint on close and suppress automatic narration during a running Arcade clock. The close handler preserves the Time line if a round expires with the book open.

#### Standards scope left open
The current CSTA 2026 PDF, printed page 80, defines MS-SYS-SE-32 as explaining failures of the whole CIA triad. There is no student activity for integrity or availability here. Notes now state the limit instead of claiming coverage. The shared module mapping and spec need correction or another tool for that standard; neither can be changed within this review's authorized folders. MS-SYS-SE-33 is practiced here through phishing and social-engineering prevention, not its entire range of attack types.

#### Original build validation (historical)
All scripts, frame batches, numeric checks, functional assertions, voice logs and audit evidence live under `_scratch/phishing-spotter/`. The two bar tools were copied and bundled there, so their actual folders were untouched. No commits, deployment or polish round were made.

The functional suite passed 159 assertions; five additional regressions and all eight link long-press checks passed. A held-click main and side voice walk heard all eight lines; Go and Time repeated in two later rounds. Default mode frames cover every specified size, including the 375-pixel iframe. The round's actual 60-second expiry was observed.

The single final audit failed before its first size check with a Chrome/CDP ConnectionResetError, Windows error 64. It produced no audit.md or page-level leads. It was not rerun, as CODEX-BUILD requires one audit. The next reviewer should run the mechanical audit. A final phone-header grid adjustment has static review but no new phone frame; earlier phone frames and measurements cover all three modes. After the audit attempt, the idle round's text was made neutral so zero answers receive no implied praise.

Cleanup verified: all assigned Chrome ports and host port 8785 are closed, no scoped Chrome remains, and host.html is absent. Three lingering background host processes were terminated only after their exact phishing-spotter server command lines were verified. The Scratch host helper now uses process termination directly because taskkill did not reliably close those servers in this sandbox.

#### Cold review validation, 2026-11-08
The current review used Chrome 9960/9961 and host 8765. All 129 functional assertions, 15 touch/resize checks, six keyboard checks and 23 dialog checks passed. The default-Sound main path ran to a natural 60-second expiry, then was repeated with Motion on after the dialog repairs. Book and Clear each narrated once across repeated opens. All 13 authored lines match allLines; browser fallback was exercised without making recordings.

One 40-minute-bounded audit finished with 16 leads. Seven confirmed layout leads were repaired and re-shot at their failing sizes. Five welcome skips/cuts are permitted by BASELINE rule 16; an inert demo Sign in button is inside the intentional message scroller. Three resize comparisons used different shuffled messages; deterministic live-input resize checks passed. All 87 audit frames were inspected. Only affected states were rechecked afterward; no second audit or review pass was run.

The final bundle is 416,525 bytes, SHA-256 e7ee2821a4100e40f6cc963f91300e38ae9a662e163c56fed0c71e464aaf4305. Art totals 207,054 bytes. All assigned Chrome ports 9960-9967 and host 8765 are closed; host.html is absent. Final evidence is in review-verification.json, review-functional.json, review-touch.json, review-keyboard.json, review-walk-repair/, review-scope-recheck/ and review-audit/ under Scratch. The shared standards-mapping issue above remains outside this review's authorized folders. No commits or shared-kit changes.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
