# Pool Repair Vote

## One idea
The Brookdale town pool has a cracked floor and can't open this summer; the child walks the fix along a path board (the problem, the staff report with the cost of $300,000, the choices, a public hearing, the council vote), listens at the hearing to a grandparent, a swim team parent, a hardware store owner and a teen lifeguard and finds what is behind each view (a need, a value, an experience), sets a slider that splits the cost between property taxes and pool entry fees, watches the five council members vote on that plan, and sees a summer later who swims and who pays, so a third grader learns how a town turns a public problem into a plan, why neighbors see it differently, and how the town pays for what it provides.

## Not like
- town-council (2, spec): one choice about land, three speakers, a show of hands. Here the full path from problem to vote, and who pays.
- ripple-street (3, concept, next batch): one family's choices and incentives. Here a whole town's choice.
- promise-check (3, spec, this batch): what each level of government is responsible for. Here how one government decides and pays.
- bill-to-law-board-game (4, concept): how a state bill becomes law. Here a town council and one local problem.

## Who and how
- Grade 3, Social Studies (Civics and Economics), module "Pool Repair Vote". Standards: D2.Civ.13.3-5 (explain how policies are developed to address public problems), D2.Civ.10.3-5 (identify the beliefs, experiences, perspectives, and values that underlie their own and others' points of view about civic issues), D2.Eco.12.3-5 (explain the ways in which the government pays for the goods and services it provides).
- Driver: one child alone, or the teacher on the projector; `Read` reads every line (tool.json `driver: "either"`). Controls 44 px or more.
- One story in five path steps, then a summer later. Extra: Class hearing (four students read the speakers' cards). tool.json `modes: ["Story", "Class hearing"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.13.3-5 | Move the town's token along the path board, doing each step: read the problem, open the staff report, sort the three choices, hold the hearing, call the vote | the path board lighting step by step: Problem, Staff report, Choices, Hearing, Vote | 2 |
| D2.Civ.10.3-5 | After each speaker, pick what is behind their view from three "because" cards, then tag it Need, Value or Experience; finally add their own view and tag it | four speaker cards with a "because" line and a tag; the child's own card | 3 |
| D2.Eco.12.3-5 | Slide the split between property taxes and entry fees and read what each neighbor pays | the slider in five steps; a bill card for each of the four speakers; the council's five votes | 4, 5 |

## Screens and modes
Header (kit): title "Pool Repair Vote"; `Story`, `Class hearing`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The Brookdale pool behind a fence with a "Closed for repairs" sign, empty and cracked. Under it the path board with five steps, the first lit. The welcome is queued (`welcomeAfter: true`): "Brookdale's town pool is closed. The town has a problem to solve. Tap the sign to see what's wrong." First hint: "Tap the sign."

**1. Problem.** The sign opens: the pool's floor cracked over the winter, water leaks out, and it isn't safe. The town owns the pool, so the town has to decide. Token moves on.

**2. Staff report.** A one-page report from the town's parks director, in large words: "Fixing the floor will cost $300,000. It will last 30 years." Three choices on cards to sort into the report: Fix it all ($300,000, opens next summer); Patch it ($80,000, opens next summer, cracks again in about 2 years); Close the pool (no cost, no pool). The child taps each card to hear it. The council will vote on fixing it all; the patch and closing are heard at the hearing.

**3. Hearing (focus: the speaker's podium).** At 1366x768 the podium and speaker sit left, the "because" cards right; at 680x425 the cards open as a sheet under the speaker.
- Four neighbors speak, one at a time:
  - Grandma Rosa: "My doctor told me to swim for my knees. The pool is the only place in town I can do it. But I live on a small, fixed income, so a big entry fee would be hard."
  - Mr. Patel, swim team parent: "Every kid should learn to swim. It keeps them safe around water. Our swim team has 60 kids with nowhere to practice."
  - Ms. Greer, hardware store owner: "Last year my taxes went up and sales were slow. I want the pool fixed, but I don't want everyone's taxes to go up for a pool some people never use."
  - Kayla, teen lifeguard: "Lifeguarding is my summer job. I'm saving for college. Last summer I taught 20 little kids to swim. If the pool is closed, that's gone."
- After each speech, three "because" cards: one true to the speech, two from other speakers. Then three tags: `Need`, `Value`, `Experience`. Answers: Rosa, Need (her knees); Mr. Patel, Value (every kid should learn to swim); Ms. Greer, Experience (last year's taxes and slow sales); Kayla, Need or Experience (both accepted: her job, and teaching kids). Wrong "because": "Listen again. What did [name] say about themselves?" and the key sentence replays.
- Last: "What do you think?" The child picks their own view (fix it all, patch it, close it) and a tag for why. Any answer is fine.

**4. Paying for it (focus: the slider and four bill cards).** A slider in five steps splits the $300,000 between property taxes (every home and shop in town pays, about 3,000 of them) and a higher entry fee (paid each time someone swims, about 20,000 swims a summer). The cost is paid over five years.
- All taxes: each home or shop pays $20 more a year; the entry fee stays the same.
- All fees: the entry fee goes up $3 a swim; taxes stay the same.
- In between (25, 50, 75 percent taxes): taxes $5, $10, $15 a year and fees $2.25, $1.50, $0.75 a swim.
- Four bill cards show what each speaker pays each year under the chosen split: Grandma Rosa swims 60 times a summer (one home); the Patel family swims 80 times (one home); Ms. Greer never swims (one home and one shop); Kayla's family swims 10 times (one home, and Kayla is paid to be there).
- Narrator after the first move: "Taxes spread the cost over everyone. Fees charge the people who use the pool."

**5. Vote (focus: the council table).** Five council members vote on the child's split, each with a reason card the child can tap:
- Mr. Lam: "Fix the pool, whatever way we pay." Always yes.
- Ms. Kim: yes if the fee goes up $2 or less a swim.
- Mr. Adler: yes if taxes go up $15 or less a year.
- Ms. Bell: yes if taxes go up $10 or less a year.
- Mr. Shaw: yes if the fee goes up $1 or less a swim.
- Every split passes, but the counts differ: all fees 3-2, 25 percent taxes 3-2, half and half 4-1, 75 percent taxes 4-1, all taxes 3-2. The narrator reads the count and the no votes' reasons. The child can slide and call the vote again (`Vote again`).

**A summer later.** The pool open and full. Cards show who swims (Grandma Rosa doing laps, the swim team, Kayla in the chair) and what each speaker paid that year under the plan. Narrator: "The town fixed a problem, heard its neighbors and chose how to pay. Someone always pays. The question is who." `Print` prints the path board, the four speaker cards, the plan and the vote.

**Class hearing (extra).** Four printable speaker cards for four students to read aloud; the projector shows the podium, the "because" cards for the class to vote on, then the slider and vote as in Story.

## Content
- One town (made up), a five-step path, three choices, four speakers with three "because" cards each, a five-step slider, four bill cards, five council members with yes rules.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The path board lights only the step in play; finished steps can be tapped to replay. `Vote again` shows only after the first vote.
- Keyboard: arrow keys move the slider; Tab moves between cards.
- With Motion off the token jumps between steps and the votes appear at once.

## Look
- Accent `--brand` #00677f pool aqua (header, the path board, slider track); gold #f4c542 (the lit step, the chosen card, yes votes have a check mark); paper #eef7f9; ink #03222a; muted #4a5c61.
- Contrast (WCAG 2.1, computed): white on brand 6.47:1; brand on paper 5.95:1; ink on paper 15.25:1; muted on paper 6.45:1; ink on gold 10.20:1.
- Never color alone: votes show "Yes" with a check and "No" with a cross; tags carry their words.
- Different from this batch (promise navy, day-in-the-life clay, overlay sepia, map-maker forest green).

## Art
- People art goes to Gemini with `people: true`: Grandma Rosa, Mr. Patel, Ms. Greer, Kayla (2 poses each: speaking, listening; cutout yes); the five council members (1 pose each, at the table; cutout yes).
- Local FLUX (`scripts/localart.py`): the closed, cracked pool (1, 16:9); the pool open and full, a summer later, people small and far off (1, 16:9); the hardware store front (1, 1:1).
- Drawn in code: the path board and token, report page, cards, slider, bill cards, vote markers.
About 16 images.

## Voice
Six bank voices, each unique in this batch: `calm-professor` as the narrator and council clerk; `warm-teacher` as Grandma Rosa; `hero-coach` as Mr. Patel; `gravel-ranger` as Ms. Greer; `playful-friend` as Kayla; `lively-host` reads the council votes. `Curio.voice` with `scope: () => state.step + ':' + state.speaker + ':' + state.split`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, `problem`, `report` and each choice card.
- event, whole, each speech (in the speaker's voice).
- how `because`: "What is behind this view? Tap a because card."
- how `tag`: "Is it a need, a value or an experience? Tap one."
- how `yours`: "What do you think? Tap your choice."
- how `slide`: "Slide to split the cost between taxes and fees."
- event, whole, `spread`: "Taxes spread the cost over everyone. Fees charge the people who use the pool."
- how `vote`: "Tap Call the vote."
- event, whole, the count and each no reason.
- event, whole, `later`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the path board, speaker and "because" cards, the five-step cost split, bill cards and council yes rules.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Because cards | Tap the first card | Card order shuffles per speaker; wrong taps replay the key sentence. |
| Tags | Tap Need for all | Mr. Patel and Ms. Greer don't accept Need; the reason line names the right kind. |
| Paying | Leave the slider still | The vote waits until the child moves it once and reads one bill card. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Sign: `problem` (whole); report and choices (whole).
2. Hearing: each speech (whole), waits; `because`; `tag`; then `yours`.
3. Paying: `slide`; first move: `spread` (whole).
4. Vote: `vote`; count and no reasons (whole); `later` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.13, D2.Civ.10 and D2.Eco.12 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Local governments make policy through staff reports, public hearings and council votes | National League of Cities, "Cities 101: Forms of municipal government" and council meetings | iCivics, "Local government" lesson materials | yes |
| Town parks and pools are paid for mainly by property taxes, with user fees covering part | National Recreation and Park Association, Agency Performance Review (revenue sources) | U.S. Census Bureau, Annual Survey of State and Local Government Finances (parks and recreation, charges) | yes |
| Water exercise helps people with knee and joint pain | CDC, "Health benefits of water-based exercise" | Arthritis Foundation, water exercise guide | yes |
| Teens can work as lifeguards (Red Cross certification from age 15) | American Red Cross, Lifeguarding course requirements | Wikipedia, Lifeguard (checked 2026-11-09) | yes |
| Learning to swim lowers children's drowning risk | CDC, "Drowning facts" | American Academy of Pediatrics, drowning prevention policy | yes |
Backed twice: 6. Cut: 0. The $300,000 cost, the town and its people are made up for the story.

Checks run (Python, scratchpad r5, 2026-11-09): 3,000 properties times $20 for five years and 20,000 swims times $3 for five years both make $300,000, and every slider step sums to $300,000; the vote counts per step are 3-2, 3-2, 4-1, 4-1, 3-2 under the five yes rules; bill cards per step for the four speakers; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 podium and cards fit side by side; at 680x425 the cards open as a sheet.
2. The path board moves through all five steps in order. (D2.Civ.13.3-5)
3. Each speaker's "because" and tag accept only the true answers; the child's own view is taken. (D2.Civ.10.3-5)
4. Every slider step covers $300,000 and the bill cards update. (D2.Eco.12.3-5)
5. The council's votes follow their rules and read their reasons. (D2.Eco.12.3-5)
6. `Vote again` is never named before the first vote.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no token or vote animations; no network requests.

## Open questions
- None for Cory.
