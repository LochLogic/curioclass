# Campaign Manager

## One idea
The student runs a made-up presidential candidate's campaign from Labor Day to November (a budget, three issue positions, a calendar, a staff) on a U.S. map with the real 538 electoral votes, spending each week on ads, rallies and field offices and choosing messages for voter groups whose interests differ (retirees, students, farmers, union members, small business owners, new citizens), while polls move with realistic error and made-up interest groups and news outlets react; then the student replays the same race under other rules, a national popular vote, ranked-choice voting, and compulsory voting as in Australia, and watches the map, the spending and the voters courted change; a turnout panel shows real U.S. turnout over time and who could vote when (women from 1920, the Voting Rights Act of 1965, eighteen-year-olds from 1971), and the student chooses a theory of democracy (majority rule, broad participation, protecting minorities) and writes which system best fits it, so a twelfth grader learns the role of citizens in the political system with attention to theories of democracy, changes in participation, and models from other countries, and how personal interests shape political choices and appeals.

## Not like
- who-decides (12, spec): local action. Here a national race.
- checks-and-balances (12, spec): governing. Here campaigning.
- two-parties (8, spec): how parties formed. Here how rules shape campaigns.
- empire-debate (11, spec): arguing a vote in 1899. Here winning votes now.

## Who and how
- Grade 12, Social Studies (Government), module "Elections, Parties and Media". Standards: D2.Civ.2.9-12 (analyze the role of citizens in the U.S. political system, with attention to various theories of democracy, changes in Americans' participation over time, and alternative models from other countries, past and present), D2.Civ.10.9-12 (analyze the impact and the appropriate roles of personal interests and perspectives on the application of civic virtues, democratic principles, constitutional rights, and human rights).
- Format: tycoon. Driver: one student alone, or rival campaigns on one map (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Ten campaign weeks, six voter groups, the electoral map, four rule systems, the turnout panel, the theory note. Extra: Rival campaigns (two students or teams run rival made-up candidates on one map). tool.json `modes: ["Campaign", "Rival campaigns"]`, `minutes: "40-50"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.10.9-12 | Match messages to voter groups by their interests and see how appeals shift support | the voter groups with interests; message cards; the polls | 2 |
| D2.Civ.2.9-12 (alternative models) | Replay under a popular vote, ranked choice and compulsory voting and compare where the campaign went | four maps and spending charts side by side | 3 |
| D2.Civ.2.9-12 (participation and theory) | Read the turnout panel, pick a theory of democracy and write which system fits it | the turnout chart with who could vote; the theory note | 4 |

## Screens and modes
Header (kit): title "Campaign Manager"; `Campaign`, `Rival campaigns`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A campaign office: a wall map of the U.S. with electoral votes per state, a budget board, a calendar from Labor Day to Election Day, and the candidate card: "Jordan Reyes, Harbor Party (made up for this game)" with three issue positions. The opponent, from the made-up Prairie Party, is shown the same way. The welcome is queued (`welcomeAfter: true`): "You have ten weeks and a budget. Where you spend it depends on the rules. Tap the map." First hint: "Tap the map to see where the votes are."

**Campaign weeks (focus: the map and the budget).** At 1366x768 the map fills the left with the week card right; at 680x425 the card is a sheet. Each week: spend on ads (by market), rallies (by city) and field offices (by state), and pick one message for each voter group. Polls update with a stated margin of error (about plus or minus 3 points for 1,000 people). Made-up interest groups endorse or attack; made-up outlets cover rallies.
- Voter groups have stated interests (retirees: health costs and Social Security; students: tuition and jobs; farmers: trade and weather; union members: wages and plant jobs; small business owners: taxes and rules; new citizens: family and opportunity). Messages that fit an interest move support; mismatched ones cost it.
- Under the Electoral College, 538 votes and 270 to win, most spending goes to a few close states.

**Rules switch (D2.Civ.2.9-12).** Replay the same race under:
- A national popular vote: every vote counts the same anywhere; the map's spending spreads to big populations.
- Ranked-choice voting (as used in Maine since 2018 and Alaska since 2022): a third made-up candidate joins; second choices matter.
- Compulsory voting (as in Australia since 1924, where turnout is about 90 percent): the campaign stops spending on getting people to vote and spends on persuading them.
- A side panel notes the five elections where the popular-vote winner didn't become president (1824, 1876, 1888, 2000, 2016), stated as fact without party commentary.

**Turnout panel (D2.Civ.2.9-12).** Real presidential-year turnout of eligible voters from 1900 to 2024 with markers for who could vote: the Nineteenth Amendment (1920), the Voting Rights Act (1965), the Twenty-sixth Amendment (1971).

**The theory note (the aha).** The student picks a theory (majority rule, broad participation, protecting minorities) and writes: "Under ___, the voters who mattered most were ___. The system that best fits ___ is ___, because ___. A cost of that system is ___." Narrator: "Change the rules and you change who gets a phone call."

**The end.** The four maps, the spending charts, the turnout panel and the note. `Print` prints them.

**Rival campaigns (extra).** Two made-up candidates run by rival teams on one map.

## Content
- Two made-up candidates and parties with balanced, mixed issue positions; six voter groups; ten weeks of stated poll and spending rules; four rule systems; real electoral votes and turnout data.
- No real candidates, parties, slogans or current officials appear; a fresh-agent read checks partisan balance before build.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each week waits for spending and messages; polls update after.
- Keyboard: Tab to the map, the budget, groups, messages and the rules switch; Enter to spend and choose.
- With Motion off poll lines jump to their values and the map recolors without fading.

## Look
- Accent `--brand` #005f8f campaign blue (header, the budget, polls); gold #f4c542 (the state in focus, the message picked); paper #eef5fa; ink #04192a; muted #4c5862.
- Contrast (WCAG 2.1, computed): white on brand 6.92:1; brand on paper 6.29:1; ink on paper 16.20:1; muted on paper 6.62:1; ink on gold 10.96:1.
- Never color alone: made-up parties use patterns and names, not red and blue; the map carries numbers.
- Different from this batch (court purple, branch amber, charter green, jury brown).

## Art
- People (illustrated) for the made-up candidates, staff and six voter groups, labeled "illustration" (Gemini, `people: true`, 10; cutout yes).
- Local FLUX (`scripts/localart.py`): the campaign office (1, 16:9).
- Drawn in code: the map, polls, spending and turnout charts.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the made-up news coverage and poll reports; `casual-peer` as the campaign aide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.rules + ':' + state.week + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `spend`: "Spend this week's budget on the map."
- how `message`: "Pick a message for each voter group."
- event, whole, each week's coverage and poll.
- how `rules`: "Switch the rules and replay."
- how `turnout`: "Read who could vote, and who did."
- how `theory`: "Pick a theory and write which system fits it."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
election (no engine doc yet). This tool builds the electoral map, poll model with stated error and the four rule systems as plain data (`/* ELECTION DATA: begin */ ... /* end */`) so later election-family tools can reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Messages | Send one message to everyone | Mismatched messages cost support with groups whose interests differ. |
| Rules | Replay only once | The note needs all four systems compared. |
| Note | Pick a theory with no cost | It must name a cost of the chosen system. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `spend`; `message`; coverage and poll (whole).
2. `rules`.
3. `turnout`.
4. `theory`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.2.9-12 and D2.Civ.10.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| 538 electoral votes, 270 to win, by state after the 2020 census | National Archives, "Distribution of Electoral Votes" | U.S. Census Bureau, 2020 apportionment | yes |
| Popular-vote winner did not become president in 1824, 1876, 1888, 2000, 2016 | National Archives, Electoral College history | U.S. House, History, Art and Archives | yes |
| Ranked-choice voting in Maine (from 2018) and Alaska (from 2022) | Maine Secretary of State | Alaska Division of Elections | yes |
| Compulsory voting in Australia since 1924, turnout about 90 percent | Australian Electoral Commission | Parliament of Australia, research papers | yes |
| Turnout of eligible voters, 1900 to 2024 | University of Florida Election Lab (McDonald) | U.S. Census Bureau, Voting and Registration tables | yes |
| The Nineteenth (1920) and Twenty-sixth (1971) Amendments; the Voting Rights Act (1965) | National Archives | U.S. Department of Justice, Voting Section | yes |
| A sample of 1,000 has a margin of error near 3 points | Pew Research Center, "5 key things to know about the margin of error" | American Association for Public Opinion Research | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: partisan balance. Candidates, parties, outlets and groups are made up; party colors avoid red and blue; issue positions mix across parties; historical facts about the Electoral College are stated without commentary. A fresh-agent read is needed before build.

Checks run (Python, scratchpad r22, 2026-11-09): 270 is a majority of 538; 1 over the square root of 1,000 is about 3.2 points; the vote reached 18-year-olds 51 years after women won it nationally; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and week card; at 680x425 sheet.
2. Messages match voter groups' interests and move the polls. (D2.Civ.10.9-12)
3. Four rule systems are replayed and compared. (D2.Civ.2.9-12)
4. The turnout panel and theory note name a fit and a cost. (D2.Civ.2.9-12)
5. No real candidates, parties or current officials; no red and blue party colors.
6. Polls show their margin of error.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: polls jump; no network requests.

## Open questions
- Sensitivity flag: partisan balance (default used: made-up candidates, parties, outlets and groups, no red and blue, mixed issue positions, facts without commentary, fresh-agent read before build).
