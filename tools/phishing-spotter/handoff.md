# Phishing Spotter handoff

## Structure
`src.html` starts from the kit starter. The CSS draws a cabinet at real pixel size around the security engine's email, text and sign-in artifacts. The panel comes before the artifact in keyboard order. Compact landscape keeps the controls beside the screen; narrow portrait puts them below it. The address book becomes a dialog button where the full book would crowd the message.

`content.json` is loaded through the bundler's JSON token. It preserves all 20 specified messages and their tell-to-spot mappings. `Sec.world`, `Sec.artifact` and two `Sec.clock` instances supply the family behavior. No shared engine or kit file changed. The tool's stylesheet moves after the engine's injected stylesheet once, so its responsive overrides take effect.

State phases are `call`, `tell`, `why`, `ready`, `result`, `end`, and `explore`. Practice never scores. Arcade commits its first tell attempt, counts a message once, and cancels pending callbacks with a round serial on mode changes. The round clock resets before the first message, including after a natural timeout. At clock expiry, a pending phish report gets one point. Keep and Report during a result immediately answer the next message.

`window.__tool` exposes the required state, security engine, mode, message, answer and round hooks. It also exposes the clocks, artifact, message pool and voice log for reproducible tests. `show` refuses messages already scored in a running round.

## Decisions and contradictions
- No open questions appear in this spec. Kept the spec's cyan accent, reserved fictional phone numbers and corrected S8 explanation.
- The older Art section names local FLUX and white backgrounds. The user's image-tool requirement and CODEX-BUILD key instructions take precedence: made 15 separate OpenAI gpt-image paintings on green or magenta where keyed. Every asset is marked `people: false`.
- BUILD.md says not to draw or record; the user and CODEX-BUILD explicitly require art. Made the paintings, authored all eight voice lines, and did not record audio. Browser narration is the Build-only fallback; Sadachbia is specified for later recording.
- CODEX-BUILD says to start the report at first bundle, while the user says to stop when it is written. Kept running evidence in Scratch and wrote the final report only after the checks, following the user's stop condition.
- The spec says no free option sweeping and also prescribes one point for reporting a phish without identifying a tell. Preserved that scoring, but the first wrong tell commits the message; later taps cannot recover the second point. Spam tests cannot reach 30. Tells-page ticks are visits, not mastery.
- At compact sizes, messages scroll within the screen because six 44-pixel spots, the status bar and a readable address cannot all fit at once. Keep, Report and the current step's control remain outside that scroller. Long sign-in addresses wrap. Tells definitions remain in accessible card names on the smallest layouts, with titles and mini examples visible.
- The address book remains accessible during Arcade; opening it does not pause either clock.
- Tell icons enlarge to 108 or 144 pixels on spacious screens, and stay 72 pixels in compact cards. This follows the build brief's art-first finish while preserving the spec's eight tells and examples.
- Current CISA URLs returned HTTP 403 during the source check. FTC, RFC and NANPA sources were reachable; NIST's current phishing guidance corroborated urgency, look-alike addresses, bad links and suspicious files without adding student topics.

## Sensitivity
No real people are depicted. The masks are objects. All names, messages, places and phone numbers are fictional. No culture, religion, hard history, bodies or attack instructions are introduced. Phishing safety guidance is limited to recognition, reporting and independent checking. Teacher notes explain that a matching sender or saved contact is context, not a universal guarantee of safety.

## Art
One full-stage painted arcade room, six emblems and eight tell icons. All are placed in the tool. The real and fake sign-in pages share the exact same painted logo. The cardboard storefront was redrawn once to make its prop brace visible. Prompts, people flags and provenance are in `art/prompts.json`; generated-path records and inspection sheets are in Scratch. Raw PNGs are retained under `art/raw/` as required by the brief.

## Engine changes wanted
None. The tool works with the existing security engine. The injected-style ordering workaround is local to this file.

## Cold review repairs
The link status node now sits directly before the result strip, outside the artifact scroller. Its engine event handlers and status handle are unchanged. Only one of link status and result is shown at once, preserving message space and making hovered, focused or pressed destinations visible in compact previews.

Practice clears selection marks before revealing the actual evidence, marks extra selections as Not a tell, and counts distinct tell types found and extra parts selected. Finding each tell type without extra parts receives the evidence-success wording. P1 subject and body both express T3 urgency; P9 repeats T5 in subject and body, so duplicate phrases are not required. Why buttons also explain the comparison in the result strip. Safe-case explanations include a caution that matching senders alone are not proof.

The round record keeps its point sequence, adds its key and a next step based on this player's missed phish, false alarms or reports without tells. Tells uses Opened labels for visits. The false storefront icon was redrawn with a larger cardboard back and two visible braces. Scoring rules are unchanged; P1's previously rejected urgency subject is now a valid tell. Two dialog how-to lines and three Read-only Arcade hints bring the authored total to 13. Dialogs restore the live game hint on close and suppress automatic narration during a running Arcade clock. The close handler preserves the Time line if a round expires with the book open.

## Standards scope left open
The current CSTA 2026 PDF, printed page 80, defines MS-SYS-SE-32 as explaining failures of the whole CIA triad. There is no student activity for integrity or availability here. Notes now state the limit instead of claiming coverage. The shared module mapping and spec need correction or another tool for that standard; neither can be changed within this review's authorized folders. MS-SYS-SE-33 is practiced here through phishing and social-engineering prevention, not its entire range of attack types.

## Original build validation (historical)
All scripts, frame batches, numeric checks, functional assertions, voice logs and audit evidence live under `_scratch/phishing-spotter/`. The two bar tools were copied and bundled there, so their actual folders were untouched. No commits, deployment or polish round were made.

The functional suite passed 159 assertions; five additional regressions and all eight link long-press checks passed. A held-click main and side voice walk heard all eight lines; Go and Time repeated in two later rounds. Default mode frames cover every specified size, including the 375-pixel iframe. The round's actual 60-second expiry was observed.

The single final audit failed before its first size check with a Chrome/CDP ConnectionResetError, Windows error 64. It produced no audit.md or page-level leads. It was not rerun, as CODEX-BUILD requires one audit. The next reviewer should run the mechanical audit. A final phone-header grid adjustment has static review but no new phone frame; earlier phone frames and measurements cover all three modes. After the audit attempt, the idle round's text was made neutral so zero answers receive no implied praise.

Cleanup verified: all assigned Chrome ports and host port 8785 are closed, no scoped Chrome remains, and host.html is absent. Three lingering background host processes were terminated only after their exact phishing-spotter server command lines were verified. The Scratch host helper now uses process termination directly because taskkill did not reliably close those servers in this sandbox.

## Cold review validation, 2026-11-08
The current review used Chrome 9960/9961 and host 8765. All 129 functional assertions, 15 touch/resize checks, six keyboard checks and 23 dialog checks passed. The default-Sound main path ran to a natural 60-second expiry, then was repeated with Motion on after the dialog repairs. Book and Clear each narrated once across repeated opens. All 13 authored lines match allLines; browser fallback was exercised without making recordings.

One 40-minute-bounded audit finished with 16 leads. Seven confirmed layout leads were repaired and re-shot at their failing sizes. Five welcome skips/cuts are permitted by BASELINE rule 16; an inert demo Sign in button is inside the intentional message scroller. Three resize comparisons used different shuffled messages; deterministic live-input resize checks passed. All 87 audit frames were inspected. Only affected states were rechecked afterward; no second audit or review pass was run.

The final bundle is 416,525 bytes, SHA-256 e7ee2821a4100e40f6cc963f91300e38ae9a662e163c56fed0c71e464aaf4305. Art totals 207,054 bytes. All assigned Chrome ports 9960-9967 and host 8765 are closed; host.html is absent. Final evidence is in review-verification.json, review-functional.json, review-touch.json, review-keyboard.json, review-walk-repair/, review-scope-recheck/ and review-audit/ under Scratch. The shared standards-mapping issue above remains outside this review's authorized folders. No commits or shared-kit changes.
