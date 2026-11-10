# AI Fit Check

## One idea
At a small tech help desk the lead, Dr. Amara Singh (made up, labeled "illustration"), hands the child a deck of job cards (total a lunch bill, enforce a board game's rules, suggest the next song, group lost-and-found photos, translate a note to a new classmate's family) and three bins, fixed steps, written rules, or a model learned from data, and the child sorts each job and picks the reason (the answer is always exact; the rules are known and few; the pattern is too fuzzy to write down); then the child runs a pretend AI helper on two jobs and checks every answer: on the lunch bill it sometimes gets the $7.10 total wrong by a few cents and says it with confidence, while on the lost-and-found photos it groups most items well but files a blue mitten with the socks; a cost card compares each approach's energy per answer, a calculator's tiny fraction against published estimates of about 0.2 to 3 watt-hours for one large-model answer, and its mistake rate, and asks who is hurt when it is wrong; at the end the child sees that AI fits jobs with fuzzy patterns and lots of examples, exact jobs are better done with steps or rules, and every answer still needs checking, so a student in grades 6 to 8 learns to choose between steps, rules and data-driven models, use and check an AI helper, and judge when AI fits.

## Not like
- ai-evaluator (Grades 9-12, spec): testing a vendor's model. Here choosing whether to use AI at all.
- dice-in-the-chatbot (Grades 9-12, spec): randomness in chatbots. Here fit and cost.
- spot-the-ai (1, spec): what uses AI. Here when AI should be used.
- leaf-sorter-ai (5, spec): training a classifier. Here comparing approaches.

## Who and how
- Grades 6-8, Computer Science, module "Choosing AI or Not". Standards: MS-ALG-PS-04, MS-ALG-PS-05, MS-SOC-ET-40 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Steps, rules or data: pick the approach, try an AI helper and judge when AI fits").
- Format: sort. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twelve job cards, three bins with reason chips, two helper trials, the cost card, a final fit memo. Extra: Debate (the class argues one card's bin on the projector). tool.json `modes: ["Sort", "Debate"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ALG-PS-04 | Sort jobs into steps, rules or data; give a reason | three bins | 2 |
| MS-ALG-PS-05 | Run the helper; check every answer | a wrong total said with confidence; a misfiled mitten | 3 |
| MS-SOC-ET-40 | Weigh accuracy, energy and who is hurt | the cost card | 4 |

## Screens and modes
Header (kit): title "AI Fit Check"; `Sort`, `Debate`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A tidy help desk with three labeled bins, a deck of job cards, a laptop showing "Helper (pretend AI)", and Dr. Singh with a mug. The welcome is queued (`welcomeAfter: true`): "Not every job needs AI. Drag the first card to a bin." First hint: "Drag the card to a bin."

**Sort (focus: the deck).** At 1366x768 the deck and bins fill the left with the reason panel right; at 680x425 the panel is a sheet. Each drop asks for a reason chip. Wrong bins get a counter-example ("A model might total $7.09. Is close enough for money?").

**Try the helper.** Lunch bill: three items ($3.25, $2.10, $1.75); the helper answers five bills and is off by a few cents on one, said as confidently as the rest. The child checks each with a calculator. Lost and found: twenty photos grouped; the child spots the misfiled ones.

**Cost card.** For each approach: energy per answer (shown as ranges with dates), mistake rate from the trials, and who is affected if it is wrong (a family overcharged; a mitten lost).

**Fit memo.** The child writes a two-line memo for two jobs from chips: which approach, and how answers will be checked.

**Fit, then check (the aha).** Dr. Singh: "AI fits fuzzy patterns with lots of examples. Exact jobs want steps or rules. And every answer still gets checked."

**The end.** The bins, the trial results and the memo. `Print` prints them.

**Debate (extra).** Class play.

## Content
- The helper is a scripted pretend AI with seeded errors; no live AI is called.
- Energy figures are published estimates shown as ranges with their dates, labeled "estimates vary".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can move between bins until `Check sort`; helper runs can be repeated.
- Keyboard: Tab to the deck, bins, reason chips, helper runs, answer checks and memo chips; Enter drops or picks.
- With Motion off cards drop at once.

## Look
- Accent `--brand` #0b6378 helper teal (header, bins, buttons); gold #f4c542 (the card in hand, a caught error); paper #eaf5f8; ink #032029; muted #49585c.
- Contrast (WCAG 2.1, computed): white on brand 6.84:1; brand on paper 6.16:1; ink on paper 15.22:1; muted on paper 6.67:1; ink on gold 10.39:1.
- Never color alone: bins carry icons and names; caught errors carry an X and the right answer.
- Different from this batch (circuit blue, kitchen-table rust, corkboard violet, ramp green).

## Art
- People (illustrated): Dr. Singh, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the help desk (1, 16:9), twelve job card scenes (12, 4:3), lost-and-found items (20, 1:1).
- Drawn in code: bins, the cost scale and the memo.
About 34 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as Dr. Singh; `news-reader` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `sort`: "Drag the card to a bin, then pick a reason."
- how `run`: "Tap Run helper."
- how `check`: "Check the answer, then tap right or wrong."
- how `cost`: "Tap each part of the cost card."
- how `memo`: "Pick chips to write your memo."
- event, whole, fit, then check.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the job deck with bins and reasons, the scripted helper with seeded errors, answer checking, the cost card, the memo builder.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Put everything in "learned from data" | Exact jobs have counter-examples and must move. |
| Helper | Trust every answer | The seeded errors must be caught to go on. |
| Memo | Skip how answers get checked | The memo needs a check line. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `sort`.
2. `run`; `check`.
3. `cost`; `memo`.
4. Fit, then check (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| One large-model text answer uses roughly 0.2 to 3 watt-hours (estimates vary by model and year) | International Energy Agency (2024), "Electricity 2024" (about 2.9 Wh per request) | Google (2025), "Measuring the environmental impact of AI inference" (median 0.24 Wh per text prompt); Epoch AI (2025) estimate of about 0.3 Wh | yes |
| AI language models can state wrong answers confidently and should be checked | National Institute of Standards and Technology (2024), "AI Risk Management Framework: Generative AI Profile" | AI4K12 (2020), "Five Big Ideas in AI", Big Idea 5 | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s24, 2026-11-10): $3.25 + $2.10 + $1.75 = $7.10; 0.24 Wh and 2.9 Wh bound the shown range; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 deck, bins and panel; at 680x425 panel as a sheet.
2. Twelve jobs are sorted with reasons. (MS-ALG-PS-04)
3. The helper is run on two jobs and every answer checked. (MS-ALG-PS-05)
4. The cost card is weighed and a fit memo written. (MS-SOC-ET-40)
5. The helper is scripted; energy figures are dated ranges.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: cards drop at once; no network requests.

## Open questions
- Energy figures for the cost card (default used: a dated range of about 0.2 to 3 Wh per large-model answer from IEA 2024, Google 2025 and Epoch AI 2025; refresh at Build).
