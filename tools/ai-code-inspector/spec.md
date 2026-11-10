# AI Code Inspector

## One idea
A friend, Leo (made up, labeled "illustration"), asked an AI helper for a five-question quiz game and wants to share it with the class tonight, and the child opens it in a code editor beside a reference docs panel, a test runner and an empty fix log: in level 1 the child hovers each function the program calls and looks it up, and `shuffle()` is in the docs but `randomQuestion()` and `scoreAll()` are not, so the program crashes the moment they run, and the child swaps each for a real function from the docs; in level 2 the child plans test inputs (all right, all wrong, a blank answer, an answer typed in capitals) and runs them, and the tests show the score is off by one and that "paris" is marked wrong against "Paris", so a player who gets all five right scores 4; in level 3 every fix goes in the fix log with what changed, why, and which test proves it; in level 4 the child adds credits before sharing, one for the AI help and one for a buzzer sound from a CC BY library, picking the credit line that names the title, the author, the source and the license; at the end the child sees that code you did not write becomes yours the moment you share it, so you check every call against the docs, test it, log your changes and give credit, so a student in grades 6 to 8 learns to read and check AI-written code against documentation and tests, keep a change log and credit sources.

## Not like
- code-tracer (4, live): tracing values in a program. Here checking a program someone else made.
- game-remix (5, live): remixing a game with credit. Here inspecting AI code before sharing.
- code-kitchen (Grades 6-8, spec): writing procedures. Here reading and fixing code.
- ai-fit-check (Grades 6-8, spec): when to use AI. Here what to do with AI's output.

## Who and how
- Grades 6-8, Computer Science, module "Code You Did Not Write". Standards: MS-PRO-RD-18, MS-PRO-TR-19, MS-PRO-PD-13, MS-PRO-PD-14 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Check AI-written code against docs and tests, log changes and credit sources").
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every panel and log line. Controls 48 px or more.
- Four levels, a 30-line program, eight docs entries, a test planner, the fix log, two credit lines. Extra: Pair inspect (one reads the docs, one runs tests; one device). tool.json `modes: ["Inspect", "Pair inspect"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PRO-RD-18 | Look up each call in the docs; replace the two that do not exist | "not in the docs" | 2 |
| MS-PRO-TR-19 | Plan test inputs; run them; confirm fixes | 4 out of 5 becoming 5 out of 5 | 3 |
| MS-PRO-PD-13 | Log what, why and which test | the fix log | 4 |
| MS-PRO-PD-14 | Credit the AI help and the CC BY sound | two credit lines | 4 |

## Screens and modes
Header (kit): title "AI Code Inspector"; `Inspect`, `Pair inspect`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The editor with the quiz program, a docs panel, a test runner and an empty fix log, and a message from Leo: "Can you check this before I share it tonight?" The welcome is queued (`welcomeAfter: true`): "Code you share is yours. Check it first. Tap a function name to look it up." First hint: "Tap a function name."

**Look it up (focus: the editor).** At 1366x768 editor left, docs and tests right; at 680x425 docs and tests are tabs. Tapping a call opens its docs page or "not in the docs". Running the quiz crashes at the first missing function with the error line shown.

**Test it.** The child picks inputs from a planner (or types one), predicts the score, runs, and compares. Failures turn the line red with the input that caused it.

**Log it.** Each change asks for what, why and the test that proves it; the log refuses a fix with no test.

**Credit it.** Three credit lines for the sound; one names title, author, source and license. Two for the AI help; one says which tool helped and how.

**Yours now (the aha).** Narrator: "You didn't write it, but you're sharing it. Now it's checked, tested, logged and credited."

**The end.** The fixed program, the fix log and the credits. `Print` prints them.

**Pair inspect (extra).** Two roles.

## Content
- A simple made-up language that reads like JavaScript; the docs list eight real functions in it.
- The AI helper is scripted with planted errors; no live AI is called. The sound library and license are labeled "made up, works like CC BY".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Code can be edited freely; tests can be rerun any time.
- Keyboard: Tab through calls, docs, the test planner, run, log fields and credit choices; Enter looks up or runs.
- With Motion off errors appear without the shake.

## Look
- Accent `--brand` #7a4a00 debugger amber (header, line markers, buttons); gold #f4c542 (the line in focus, a passing test); paper #fbf4e8; ink #2a1800; muted #5e5240.
- Contrast (WCAG 2.1, computed): white on brand 7.48:1; brand on paper 6.84:1; ink on paper 15.63:1; muted on paper 6.97:1; ink on gold 10.51:1.
- Never color alone: failing lines show an X and the input; passing tests show a check.
- Different from this batch (timeline navy, factory red-orange, x-ray plum, test-kit green).

## Art
- People (illustrated): Leo, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the quiz game's title screen (1, 16:9).
- Drawn in code: the editor, docs panel, test runner, log and credits.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Leo; `calm-professor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.line + ':' + state.say`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `lookup`: "Tap a function name."
- how `replace`: "Pick a real function from the docs."
- how `plan`: "Pick a test input, then tap Run."
- how `log`: "Fill in what, why and the test."
- how `credit`: "Pick the credit line with title, author, source and license."
- event, whole, yours now.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: a tiny interpreter for the made-up language, docs lookup, the test planner and runner, the fix log, credit choices.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Look up | Delete the broken lines | The quiz must still run all five questions. |
| Test | Run one input | The capitals and blank tests must pass too. |
| Credit | Pick the shortest line | Only the full line names all four parts. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `lookup`; `replace`.
2. `plan`.
3. `log`; `credit`.
4. Yours now (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| AI code helpers sometimes call functions or packages that do not exist | Spracklen and others (2025), "We Have a Package for You!", USENIX Security Symposium | National Institute of Standards and Technology (2024), "AI Risk Management Framework: Generative AI Profile", confabulation | yes |
| A CC BY credit names the title, author, source and license | Creative Commons, "Recommended practices for attribution" (TASL) | Creative Commons Attribution 4.0 legal code, section 3(a) | yes |
| AI help should be acknowledged when work is shared | MLA Style Center (2023), "How do I cite generative AI" | APA Style (2023), "How to cite ChatGPT" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s25, 2026-11-10): with a strict compare "paris" against "Paris" scores 4 of 5, with a case-blind compare 5 of 5; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 editor with docs and tests; at 680x425 docs and tests as tabs.
2. Both missing functions are found and replaced from the docs. (MS-PRO-RD-18)
3. Planned tests expose the off-by-one and capitals bugs and confirm the fixes. (MS-PRO-TR-19)
4. Every fix is logged with a test, and both credits are complete. (MS-PRO-PD-13, MS-PRO-PD-14)
5. The AI is scripted; nothing is sent anywhere.
6. `Read` reads every panel and log line; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no shake; no network requests.

## Open questions
None.
