# Shaping Our Week

## One idea
The child follows the Reyes family (made for this game) through one week on a calendar and a cutaway of their neighborhood where groups glow: the city council that runs the bus line Mom takes to the warehouse, the company she works for, her union, the landlord's lease, the food bank's Saturday pantry, the youth soccer league where Teo plays, and the court and labor office that enforce the rules; tapping a group tells what kind it is (government, company, union, nonprofit, club, court), who runs it and what it does; then the child switches one off and replays the week to see what changes for each person (no late bus; no contract rule on schedules; no Saturday pantry; a lease no one has to honor); at the end a web shows which group touches which family member and how, and a sentence explains how companies, unions, nonprofits, clear property rights and the rule of law each work in a market economy, so an eighth grader learns the roles political, civil and economic organizations play in people's lives and the institutions a market economy depends on.

## Not like
- levers-of-power (8, spec): acting on one problem. Here the groups already shaping a week.
- community-helpers-village (1, spec): community helpers. Here organizations and institutions.
- motion-on-the-floor (8, spec): how one group decides. Here what many groups do.
- mill-town (8, spec): one worker's story in 1830s. Here one family's week today.

## Who and how
- Grade 8, Social Studies (Civics and Economics), module "Shaping Our Week". Standards: D2.Civ.6.6-8 (describe the roles of political, civil, and economic organizations in shaping people's lives), D2.Eco.9.6-8 (describe the roles of institutions such as clearly defined property rights and the rule of law in a market economy).
- Format: explorer. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Seven days, eight groups, four switch-off replays, the web and the sentence. Extra: My week (the child maps groups in their own week from tiles, kept on the device only). tool.json `modes: ["The Reyes family", "My week"]`, `minutes: "20-30"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.6.6-8 | Tap each glowing group and sort it by kind (government, company, union, nonprofit, club, court) | the group card: kind, who runs it, what it does | 2 |
| D2.Civ.6.6-8 (replay) | Switch one group off and replay the week | the family members' day cards changing, with reasons | 3 |
| D2.Eco.9.6-8 | Answer the lease and paycheck questions: what makes a promise stick when someone breaks it | the property-rights and rule-of-law cards; the replay with no enforcement | 3, 4 |
| D2.Civ.6.6-8 (web) | Complete the web linking groups to family members, and write the sentence | the web; the sentence card | 4 |

## Screens and modes
Header (kit): title "Shaping Our Week"; `The Reyes family`, `My week`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A week calendar across the top (Monday to Sunday) and a cutaway of the neighborhood: an apartment building, a bus stop, a warehouse, a union hall, a city hall, a church basement food pantry, a soccer field, a courthouse. Four family members: Mom (Ana, a warehouse worker), Dad (Luis, who drives for a delivery company and is looking for steadier work), Teo (13, plays soccer), Grandma Rosa (on a fixed income). Groups glow softly. The welcome is queued (`welcomeAfter: true`): "Meet the Reyes family. Lots of groups shape their week, some you'd never notice. Tap Monday to start." First hint: "Tap Monday."

**The week (focus: the day and the neighborhood).** At 1366x768 the neighborhood fills the screen with the day card at the side; at 680x425 the day card is a sheet.
- Each day shows a few moments: Monday Ana takes the 6:10 bus (the city council funds the route); Tuesday her union contract sets her shift schedule two weeks ahead; Wednesday rent is due (the lease says what each side owes); Thursday Luis's paycheck (state and federal law require overtime pay over 40 hours for many workers); Friday the landlord fixes the heater (the lease and city code require it); Saturday Rosa visits the food bank pantry (a nonprofit run by volunteers and donations); Sunday Teo's league game (a club run by parent volunteers and fees).
- Tapping a glowing group opens its card: kind, who runs it (voters elect the council; owners and managers run the company; members elect union leaders; a board and volunteers run the food bank; parents run the league; judges and the labor office enforce rules), and what it does here. The child sorts it into its kind.

**Switch off and replay (focus: the replay).** The child picks one group to switch off, then replays the week:
- No evening bus: Ana leaves work early or pays for rides; her pay falls.
- No union contract: her schedule can change with a day's notice; Teo's rides to practice fall apart.
- No food pantry: Rosa skips meals at month's end.
- No courts or labor office (the rule of law): Luis's unpaid overtime has nowhere to go; the landlord ignores the broken heater; the lease is just paper.
- Each change appears on the day card with a reason line.

**Property rights and the rule of law (D2.Eco.9.6-8).** Two cards: the lease (who owns the apartment, what renting it gives the family, what each side must do) and the paycheck (a promise of pay for work). A question: "If someone breaks the promise, what makes it stick?" (courts, labor offices, laws everyone must follow). The replay with no enforcement shows why markets need it: the landlord and the company also count on the family keeping their side.

**The web (the aha).** The child links each group to the family members it touches and writes how ("the union sets Ana's schedule"). Then the sentence card: "In a market economy, companies ___, unions ___, nonprofits ___, and laws and courts ___." (tiles plus a free line). Narrator: "No one in this family runs these groups alone, but every one of them shapes the week."

**The end.** The web, the sentence and the replay the child found most surprising. `Print` prints them.

**My week (extra).** The child places groups in their own week from tiles; nothing leaves the device.

## Content
- Seven days with moments, eight group cards, four replays with day-card changes, two institution cards, the web, the sentence tiles, My week tiles.
- The family and neighborhood are made up and labeled; how each kind of group works and the overtime rule are real and sourced.
- Unions and companies are shown evenly: the company provides jobs and pay; the union bargains for its members; both have costs and benefits named.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Only one group can be off at a time; switching another turns the first back on.
- My week stores nothing beyond the page and prints only on request.
- Keyboard: Tab to days, groups, switches and the web; Enter to open, sort, switch and link.
- With Motion off groups don't glow-pulse; replays cut between days.

## Look
- Accent `--brand` #0c6b78 transit teal (header, the calendar, group cards); gold #f4c542 (the glowing group, a linked line); paper #eef6f7; ink #03222a; muted #4a5a5d.
- Contrast (WCAG 2.1, computed): white on brand 6.19:1; brand on paper 5.65:1; ink on paper 15.13:1; muted on paper 6.58:1; ink on gold 10.20:1.
- Never color alone: switched-off groups are grayed and labeled "off" with a slash icon; group kinds carry icons and words.
- Different from this batch (committee green, amendment indigo, mill brick, colonial leather).

## Art
- Local FLUX (`scripts/localart.py`): the neighborhood cutaway (1, 16:9); seven day scenes (7, 3:2).
- People art goes to Gemini with `people: true`: Ana, Luis, Teo, Rosa, a bus driver, a union steward, a food bank volunteer, a coach (8; cutout yes).
- Drawn in code: the calendar, glowing groups, switches, day cards, the web.
About 16 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as the narrator; `playful-friend` as Teo, who tells his family's week. `Curio.voice` with `scope: () => state.mode + ':' + state.day + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each day's moments.
- how `group`: "Tap a glowing group, then sort it by kind."
- event, whole, each group card.
- how `switch`: "Switch one group off, then tap Replay the week."
- event, whole, each replay change.
- how `web`: "Link each group to the people it touches."
- how `sentence`: "Finish the sentence about each group's role."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the week calendar, the neighborhood with group hotspots, switches and replays, institution cards, the web, the sentence.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Call every group government | Each kind checks; the union as government plays "Who elects the union's leaders?" |
| Replay | Skip replays | The web opens after two replays. |
| Web | Link every group to everyone | Each link needs a how line, and links check against the week. |
| Sentence | Leave blanks | Print waits for them. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Day moments (whole), each waits.
2. `group`; group cards (whole).
3. `switch`; replay changes (whole).
4. `web`; `sentence`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.6.6-8 and D2.Eco.9.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Federal law requires overtime at time and a half over 40 hours for many workers | U.S. Department of Labor, "Overtime Pay" (Fair Labor Standards Act) | Cornell Legal Information Institute, 29 U.S.C. 207 | yes |
| Unions bargain contracts covering pay and schedules; members elect leaders | National Labor Relations Board, "Collective bargaining rights" | U.S. Department of Labor, Office of Labor-Management Standards, "Union member rights" | yes |
| About one in ten U.S. wage and salary workers belong to a union | Bureau of Labor Statistics, "Union Members Summary" (2024) | Pew Research Center, union membership fact sheet | yes |
| Food banks are nonprofits run by boards, staff, volunteers and donations | Feeding America, "How food banks work" | IRS, "Exempt purposes, Internal Revenue Code Section 501(c)(3)" | yes |
| Property rights and the rule of law support markets | Federal Reserve Bank of St. Louis, Page One Economics, "Property rights" | Council for Economic Education, Voluntary National Content Standards in Economics, Standard 10 | yes |
| City councils fund and set local services like bus routes | National League of Cities, "Cities 101: Forms of municipal government" | American Public Transportation Association, "Public transportation funding" | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r15, 2026-11-09): eight groups across six kinds with at least one of each; every switch-off changes at least two family members' days; overtime at 1.5 times $18 an hour is $27; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 neighborhood and day card; at 680x425 sheet.
2. Each group's card opens and sorts by kind. (D2.Civ.6.6-8)
3. Switching off a group replays the week with reasons. (D2.Civ.6.6-8, D2.Eco.9.6-8)
4. The web and sentence check and print. (D2.Civ.6.6-8, D2.Eco.9.6-8)
5. Unions and companies are shown evenly.
6. My week stays on the device.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no pulsing; no network requests.

## Open questions
- D2.Eco.9.6-8 is about property rights and the rule of law, which the idea card didn't name; the lease, the paycheck and courts were added to cover it (default used: added as two institution cards and one replay).
