# Checks and Balances

## One idea
Three seats sit at a table, Congress, the President and the Supreme Court, with a made-up policy in the middle (a national rule on how apps may collect personal data), and the student takes one seat and plays its real powers as cards against the other two, played by the computer: pass a bill, veto, override with two-thirds, sign, issue an executive order, fund or defund, appoint, confirm or reject, hear a case and strike a law down; each card cites its place in the Constitution and one real example (Marbury v. Madison in 1803, the War Powers Resolution passed over a veto in 1973, the steel mill seizure struck down in 1952, a nominee rejected by the Senate in 1987); when the policy ends (as a law, an order, a ruling or dead), a purposes scoreboard rates the route on speed, how long it lasts, how many voices were heard and how well rights were protected; then the student replays the same policy by another route (law, executive order, court case), through a state legislature, and through an international agreement that needs two-thirds of the Senate, and compares the scoreboards, with a note on powers that grew or shrank over time, so a twelfth grader learns how the Constitution sets powers and limits that have changed and are still argued over, and evaluates decision procedures at several levels by the civic purposes they achieve.

## Not like
- bill-to-law-board-game (4, spec): a state bill's path, grade 4. Here three federal branches checking each other.
- supreme-court-simulator (12, spec): ruling on rights cases. Here every branch's moves.
- build-a-government (12, spec): designing a new constitution. Here playing the U.S. one.
- campaign-manager (12, spec): winning office. Here using it.

## Who and how
- Grade 12, Social Studies (Government), module "Congress, the President and the Courts". Standards: D2.Civ.4.9-12 (explain how the U.S. Constitution establishes a system of government that has powers, responsibilities, and limits that have changed over time and that are still contested), D2.Civ.11.9-12 (evaluate multiple procedures for making governmental decisions at the local, state, national, and international levels in terms of the civic purposes achieved).
- Format: cards. Driver: one student alone against two computer branches, or three students or teams in the three seats (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- About thirty power cards, one policy played to its end, three replay routes plus a state and an international route, the scoreboard, the balance note. Extra: Three seats (students or teams play all three branches). tool.json `modes: ["One seat", "Three seats"]`, `minutes: "35-45"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.4.9-12 | Play power cards and answer checks, each citing its article and a real example | the cards with article and example; the table | 2 |
| D2.Civ.4.9-12 (change over time) | Read the balance note and mark one power that grew and one that shrank | the timeline of shifts | 3 |
| D2.Civ.11.9-12 | Replay the policy by other routes and levels and compare the scoreboards | the scoreboards side by side | 4 |

## Screens and modes
Header (kit): title "Checks and Balances"; `One seat`, `Three seats`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A round table with three seats and a policy folder in the middle: "A national rule on how apps may collect personal data (made up for this game)". The welcome is queued (`welcomeAfter: true`): "Three branches, one policy. Each can push it forward or stop it. Pick a seat." First hint: "Tap a seat to choose your branch."

**Play (focus: the table and the hand).** At 1366x768 the table fills the left with the hand and log right; at 680x425 the hand is a sheet. Each turn the student plays a card from their branch; the other branches answer by stated rules. Cards (each with article and one real example):
- Congress (Article I): introduce and pass (simple majorities in both houses); override a veto (two-thirds of both houses; the War Powers Resolution, 1973); the power of the purse (Article I, Section 9); confirm or reject nominees (Senate, Article II; Robert Bork rejected 58 to 42 in 1987); approve treaties (two-thirds of the Senate); impeach.
- President (Article II): sign or veto (presidents have vetoed more than 2,500 bills, and about 110 were overridden); executive orders (not named in the Constitution; limited by Youngstown Sheet and Tube v. Sawyer, 1952); nominate judges; negotiate treaties.
- Court (Article III and judicial review): hear a case and strike down a law or order (Marbury v. Madison, 1803; INS v. Chadha, 1983, ended the "legislative veto"); a later Court can overrule (Brown overruling Plessy).
- The rules come from the bill-to-law path and vote data, reused at federal scale.

**The scoreboard (D2.Civ.11.9-12).** When the policy ends, four rows: speed (turns taken), durability (what it would take to undo: a new law, the next president, a later Court or an amendment), voices heard (hearings, votes, briefs), rights protected (does a court check it). Each row has a stated rule.

**Replays (the aha, D2.Civ.11.9-12).** The same policy by an executive order, by a court case, by a state legislature (as when California passed its consumer privacy law in 2018), and by an international agreement (needing two-thirds of the Senate). Scoreboards line up; the student writes which route best fits which purpose. Narrator: "The fastest route isn't the one that lasts. The Constitution made sure of that."

**The balance note (D2.Civ.4.9-12).** A short timeline of shifts: senators chosen by voters after the Seventeenth Amendment (1913); the growth of executive orders and of presidential war powers; the War Powers Resolution (1973); judicial review's growth from 1803. The student marks one power that grew and one that shrank and says who still contests it.

**The end.** The play log, the scoreboards, the route note and the marks. `Print` prints them.

**Three seats (extra).** Three students or teams play the branches against each other.

## Content
- About thirty cards with real articles and examples, stated computer rules, the made-up policy (labeled), the scoreboard rules, five routes, the balance timeline.
- The policy is made up; every power, article, case and figure is real and sourced.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Only cards the branch really holds are playable; an unplayable card says which branch holds that power.
- Keyboard: Tab to seats, the hand, the table, the scoreboard and routes; Enter plays a card.
- With Motion off cards appear on the table without sliding.

## Look
- Accent `--brand` #8a4b00 branch amber (header, cards, the table); gold #f4c542 (the card in play, a scored row); paper #fbf4ea; ink #241300; muted #5f564b.
- Contrast (WCAG 2.1, computed): white on brand 6.80:1; brand on paper 6.23:1; ink on paper 16.46:1; muted on paper 6.59:1; ink on gold 11.05:1.
- Never color alone: branches carry names and icons; scoreboard rows carry numbers and words.
- Different from this batch (court purple, campaign blue, charter green, jury brown).

## Art
- Local FLUX (`scripts/localart.py`): the Capitol, the White House and the Supreme Court building (3, 16:9).
- Designed card faces drawn in code with branch icons.
- People (illustrated) for generic branch figures (a senator, a president, a justice), never real officials, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
About 6 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the table host announcing plays; `clear-teacher` as the explainer of each card and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.route + ':' + state.turn + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `play`: "Play a card your branch really holds."
- event, whole, each card played (by any branch).
- event, whole, the policy's end.
- how `score`: "Read the scoreboard for this route."
- how `replay`: "Replay by another route and compare."
- how `balance`: "Mark one power that grew and one that shrank."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
bill-to-law (no engine doc; shared with bill-to-law-board-game). This tool reuses that spec's plain-data path and vote rules (step cards, vote counts, veto and override) at federal scale and adds: three branch hands, judicial review, appointments, executive orders, the scoreboard and route replays. Keep cards and rules as plain data.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Play | Play any card | Only the branch's real powers are playable, and each shows its article. |
| Routes | Replay one route | The note opens only after three routes plus a state or international route. |
| Balance | Mark at random | Each mark needs the date of the shift. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `play`; card (whole), waits.
2. Policy's end (whole); `score`.
3. `replay`.
4. `balance`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.4.9-12 and D2.Civ.11.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Powers in Articles I, II and III; two-thirds for overrides and treaties | National Archives, "The Constitution of the United States" | Congress.gov, "Constitution Annotated" | yes |
| More than 2,500 vetoes, about 110 overridden | U.S. Senate, "Summary of Bills Vetoed, 1789-present" | U.S. House, History, Art and Archives, "Presidential Vetoes" | yes |
| Marbury v. Madison (1803) | National Archives, "Marbury v. Madison" | U.S. Courts, "Marbury v. Madison" | yes |
| Youngstown Sheet and Tube v. Sawyer (1952) | Oyez, "Youngstown Sheet and Tube Company v. Sawyer" | Congress.gov, Constitution Annotated, Article II | yes |
| The War Powers Resolution passed over a veto (1973) | U.S. House, History, Art and Archives | Office of the Historian, U.S. Department of State | yes |
| Bork rejected 58 to 42 (1987) | U.S. Senate, "Nominations" | Senate Historical Office | yes |
| INS v. Chadha (1983) | Oyez, "INS v. Chadha" | Congress.gov, Constitution Annotated | yes |
| The Seventeenth Amendment (1913); the California Consumer Privacy Act (2018) | National Archives | California Attorney General, CCPA | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r22, 2026-11-09): about 110 of 2,500 vetoes is about 4 percent overridden; two-thirds of 100 senators is 67; Marbury came 14 years after the Constitution took effect in 1789; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and hand; at 680x425 sheet.
2. Every card cites its article and one real example. (D2.Civ.4.9-12)
3. The balance note marks a power that grew and one that shrank, with dates. (D2.Civ.4.9-12)
4. Scoreboards compare at least three routes plus a state or international route. (D2.Civ.11.9-12)
5. Only a branch's real powers are playable.
6. No real current officials are shown.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
None.
