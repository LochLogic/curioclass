# Codex review: phishing-spotter
## Played
- Cold as a grade 7 student: Practice, the full 20-message pool, a blind Arcade round and Tells before reading the builder's report, handoff, notes or source. Then a teacher-style evidence comparison and a natural 60-second voice walk. The cabinet and convincing fake pages are strong; the original recap felt flat.
- Root verified as S:\CurioClass-codex. One review pass, scoped repairs and rechecks; no commits or shared-kit changes. Evidence below is in ../../_scratch/phishing-spotter/.
- Teaching, Play and Craft lenses covered evidence accuracy and transfer, cheap scoring paths and the recap, then art, layout, keyboard and voice. Findings below name their rule scope and severity.
## Findings fixed
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
## Findings left
- Should fix, spec/catalog: MS-SYS-SE-32 requires explaining failures of confidentiality, integrity and availability. There is no integrity/availability activity here. The spec or module needs another tool for that code; adding one here or editing shared metadata exceeds this review's scope. MS-SYS-SE-33 is practiced through phishing/social engineering, not every attack type in its boundary statement.
## Break it
- Arcade score/right-call/streak: blind Keep = 10/30, blind Report plus first spot = 15/30 and 5 tells. Neither reaches the full result. The specified base point for a phish report remains intentional; these are practice scores, not certification.
- All outcomes: safe Keep +1; phish Report with a correct first tell +2; wrong first tell or real four-second timeout +1; phish Keep 0; safe Report 0. A wrong-first then every-spot sweep stays +1. Repeated taps cannot add points to a committed message.
- Round/Best: perfect responses = 30, 20 right calls, 10 tells, 20 unique messages; early finish preserves time. A pending report gets +1 at expiry. Leaving mid-round saves no Best; Clear No preserves it and Clear Yes removes it. Keep/Report during wrong-result pauses answer the next message immediately.
- Practice: empty, wrong-only and select-all evidence receive comparison feedback without evidence-success styling. Each tell type without extras receives success; repeated phrases for one type are not required. Extra selections are explicitly marked, so sweeping cannot mimic an explanation.
- Tells: opening every card earns only Opened labels. No quiz, reflection gate, multiplier or mastery badge exists. The mandated developer hooks remain test hooks, not a tamper-proof assessment.
- Evidence: review-functional.json; links-after-real-tap.json; review-keyboard.json. Eight initial programmatic-focus checks ran in an inactive document; all eight passed after a real held tap. Their earlier failures are retained, not counted as product passes.
- Final checks: 129 functional assertions, 15 touch/resize checks and six keyboard checks passed. All eight held-touch links expose their true destination without navigating; sign-in fields reject typing. The first resize fixture dispatched mouse input before the viewport settled; with input modes separated and a render wait, live evidence scores and next-message controls survive both resizes. Earlier results remain in review-touch-before-final.json.
## Voice walk
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
## Facts checked
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
## Sensitivity
- None requiring a cultural lens: this is a fictional message simulator, not a cultural, religious, historical or body topic. No people are pictured; teacher names do not stand for a cultural tradition. All 15 art assets carry people:false; the theater mask is an object. An empty arcade backdrop is appropriate to the cabinet view.
## Flattest moment left
- After several rounds, the fixed pool of 20 becomes familiar. Kept the specified pool and the quick reading/reasoning mechanic; more messages would exceed scope. The record now points to the student's actual next practice need.
## Graphics
- Checked room, all six logos and all eight tell icons, plus the fake/real sign-in pairs. Redrew only the false storefront with the built-in imagegen tool; full prompt and provenance are in art/prompts.json, raw in art/raw/ps-tell-7.png, finished in art/ps-tell-7.webp. Checked the replacement at 72/108/144-pixel display sizes.
- Art 202.2 KiB; final bundle 406.8 KiB (416,525 bytes). No missing art tokens. Compared the retained cabinet and tell cards with Beat Lab in review-comparison.png; no simplification of the painted scene or evidence glow.
- Looked at cold, all eight size layouts, compact Tells/Why, phone modes/book/record, correct/wrong evidence, perfect and partial records, grayscale/Motion off, keyboard focus and the main voice-walk frames. Initial phone-script context errors and favicon 404 belonged to the fixture; corrected phone shots are console-clean.
## Audit
- The one 40-minute-bounded audit finished: 16 leads. Confirmed and fixed seven layout leads: two narrow Tells targets, three clipped Address book entries, clipped safe Why, and clipped 1280x720 recap. Reserved Sound width too, because its first toggle moved the header.
- Five welcome-skip/cut leads are permitted by BASELINE rule 16, with hints and Read retained. The hidden demo Sign in button is inert, inside the deliberately scrollable fake page, not an answer choice. Three resize leads compare different shuffled message labels; the deterministic live-control resize recheck passed. Sound's remaining movement is at most 2.46 pixels.
- All 87 audit frames were inspected in review-audit-sheets/, with confirmed leads opened at native size. Scoped rechecks use the same geometry checks on changed states only; the full audit was not rerun.
## Left open
- Shared standards mapping as described above. Authored bank-voice recordings belong to the later voice pass; browser narration was tested here.
- Unattended choices followed the spec: retained the scoring formula, 20-message pool, fast Arcade and matching real/fake logos; kept standard-mapping changes outside the authorized folders.
- The first quick read commands used the execution tool's wait bound, not a hard process deadline. All subsequent commands used explicit 30/120/180/300/330/2400-second limits; failed long scripts were retried smaller.
- Cleanup verified: Chrome ports 9960-9967 and host 8765 closed; host.html absent. All final checks passed in review-verification.json. No commits. Bundle SHA-256: e7ee2821a4100e40f6cc963f91300e38ae9a662e163c56fed0c71e464aaf4305.
