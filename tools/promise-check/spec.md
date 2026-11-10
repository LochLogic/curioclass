# Promise Check

## One idea
Two elections run side by side, one for class president in Room 12 and one for mayor of the town, and the child checks every campaign promise against what that job can really do: each promise sorts into "This job can do it", "A different job does that" (and names which one: the teacher, the principal, the school board, the governor, Congress) or "Nobody can do that" ("I'll make summer longer"); then the child helps a class candidate fix a speech so it is honest and kind, votes by secret ballot in both races, replays the town race as if only half the voters came, and fills a card comparing how a class, a school and a town make decisions, so a third grader learns what officials at each level are allowed to do and why taking part matters.

## Not like
- campaign-manager (12, concept, same election family): running a campaign's strategy at grade 12. Here checking promises against real powers at grade 3.
- town-council (2, spec): a council meeting about one lot. Here elections and the limits of each office.
- pool-repair-vote (3, spec, this batch): one policy from problem to vote. Here who holds which power.
- school-fix-it-meeting (3, concept): talking a school problem through. Here voting and promises.

## Who and how
- Grade 3, Social Studies (Civics), module "Local Government and Voting". Standards: D2.Civ.1.3-5 (distinguish the responsibilities and powers of government officials at various levels and branches of government), D2.Civ.11.3-5 (compare procedures for making decisions in a variety of settings, including classroom, school, government), D2.Civ.2.3-5 (explain how a democracy relies on people's responsible participation), D2.Civ.7.3-5 (apply civic virtues and democratic principles in school settings).
- Driver: one child alone by default (the idea card's fit note: simulated candidates); or the teacher on the projector. Text is read aloud by `Read`; grade 3 lines are short. Controls 44 px or more.
- Four parts: Check promises, Fix the speech, Vote, How we decide. Extra: Real class election (projector ballot). tool.json `modes: ["Promises", "Speech", "Vote", "How we decide", "Class election"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.1.3-5 | Sort 12 promises into This job / A different job (and name it) / Nobody, and read who really holds each power | the three bins and a "Who really does this" card per promise | 2, 3 |
| D2.Civ.7.3-5 | Fix Priya's class speech: swap a put-down for a fair line and a promise she can't keep for one she can | the speech before and after, with the swapped lines marked | 4 |
| D2.Civ.2.3-5 | Vote in both races, then replay the town race with half the voters | the full count and the half-turnout count, with a different winner | 5 |
| D2.Civ.11.3-5 | Fill the How we decide card: class (vote), school (principal decides, with input), town (people elect, council votes) | the three-column card | 6 |

## Screens and modes
Header (kit): title "Promise Check"; `Promises`, `Speech`, `Vote`, `How we decide`, `Class election`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Two ballot boxes side by side: one on a classroom table (Room 12, class president) and one in the town hall lobby (Mayor of Pine Hollow). Each has two candidate posters. The welcome is queued (`welcomeAfter: true`): "Two elections, four candidates, lots of promises. But can each job really do what they promise? Tap a poster to read a promise." First hint: "Tap a poster to read a promise."

**Promises (focus: the promise card).** Candidates: class: Priya and Marcus; mayor: Ms. Hale and Mr. Ortiz. Each poster holds three promises (12 in all). At 1366x768 the posters are at the left, the promise card center, and three bins at the right: "This job can do it" (a check), "A different job does that" (an arrow), "Nobody can do that" (a cloud). At 680x425 the posters become a list.
- Promises and answers:
  - Priya: "I'll start a class book swap." (This job, with the teacher's OK); "I'll get rid of homework forever." (Different job: the teacher); "I'll make the bell ring later." (Different job: the principal or school board)
  - Marcus: "I'll ask the principal for a longer recess." (This job: a class president can ask); "I'll give everyone a new tablet." (Different job: the school board pays for school things); "I'll make every day sunny." (Nobody)
  - Ms. Hale: "I'll fix the potholes on Elm Street." (This job: the mayor runs the town's road crew); "I'll lower the speed limit on the state highway." (Different job: the state; the governor and state lawmakers); "I'll make summer longer." (Nobody)
  - Mr. Ortiz: "I'll ask the council to build a new library." (This job: the mayor can propose, and the council votes on the money); "I'll print new dollar bills for our town." (Different job: Congress and the U.S. Treasury); "I'll keep the pool open later in summer." (This job: the town runs the pool)
- "A different job" opens a picker of five jobs with icons: Teacher, Principal, School board, Governor (and state lawmakers), Congress. A right drop shows the "Who really does this" card (one sentence). A wrong bin or job: "Think: is this a class, school, town, state or country job?" and a level ladder (class, school, town, state, country) lights.

**Speech (focus: Priya's speech).** Priya's draft has five lines; two are problems. The child taps a line to flag it and picks a replacement from three:
- Problem 1, a put-down: "Marcus is too silly to be president." Replacements: "I'll listen to everyone, even people who don't vote for me." (fair) / "Marcus can't even tie his shoes." (still a put-down) / "Vote for me or else." (unfair)
- Problem 2, a promise she can't keep: "I'll get rid of homework forever." Replacements: "I'll ask our teacher if we can have one homework-free Friday a month." (can do: ask) / "I'll make homework illegal." (nobody) / "I'll do everyone's homework." (not honest)
- Flagging a fine line ("I love our class.") says "That one is fine. Look for a put-down or a promise she can't keep." When both are fixed, Priya reads the new speech aloud.

**Vote (focus: the two ballots).** A secret ballot screen: a booth curtain closes, the child marks one name in each race and drops the ballots. "Nobody sees how you voted. That's a secret ballot." Results:
- Class (24 students, all vote): the child's vote plus 23 set votes; the race is close (12 to 11 before the child votes), so the child's vote decides it.
- Town (1,000 voters, 600 turn out): Ms. Hale 310, Mr. Ortiz 290 (the child's one vote shown as a dot).
- `What if only half voted?` replays the town race with 300 voters, where many of Ms. Hale's supporters stayed home: Ms. Hale 130, Mr. Ortiz 170. "The winner changed because of who came to vote."

**How we decide (focus: the card).** Three columns: Our class, Our school, Our town. The child drags a decision method to each from four: "Everyone votes", "The principal decides after listening", "People elect leaders, and the council votes", "One person decides alone without listening". The last fits none: "Is that fair in any of these places?" Then a one-sentence summary for each column plays.

**Class election (extra).** A projector ballot: the teacher types two to four names; each student taps a name in turn behind a privacy screen (the screen blanks between voters); `Count` shows totals. Nothing is saved after the page closes.

## Content
- Four candidates, twelve promises with answers and "Who really does this" lines; five jobs; a five-line speech with two problems and three replacements each; two races with set vote counts; four decision methods.
- Pine Hollow and all people are made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `What if only half voted?` shows only after the town results. `Count` shows only in Class election after one vote.
- Keyboard: Tab to a promise, Enter to pick up, Tab to a bin, Enter to drop.
- With Motion off the curtain and ballots appear without moving.

## Look
- Accent `--brand` #2e4a7a ballot navy (header, bins, ballot frames); gold #f4c542 (the check, the winning bar, the lit level); paper #f1f4f9; ink #0d1729; muted #4f5868.
- Contrast (WCAG 2.1, computed): white on brand 8.84:1; brand on paper 8.01:1; ink on paper 16.26:1; muted on paper 6.51:1; ink on gold 11.02:1.
- Never color alone: bins and jobs carry icons and words; vote bars carry numbers.
- Different from this batch (day-in-the-life clay, overlay sepia, map-maker forest green, pool aqua).

## Art
- People art goes to Gemini with `people: true`: Priya and Marcus (third graders, 3 poses each: on a poster, speaking, waving); Ms. Hale and Mr. Ortiz (adults, 3 poses each); cutout yes.
- Local FLUX (`scripts/localart.py`): the classroom table and the town hall lobby (2, 16:9); the voting booth (1); five job icons drawn in code instead.
- Drawn in code: posters, bins, the job picker, the level ladder, ballots, bars, the decision card.
About 15 images.

## Voice
Bank voices, each unique in this batch: `news-reader` as the narrator; `bright-teacher` as Priya; `casual-peer` as Marcus; `firm-captain` as Ms. Hale; `smooth-narrator` as Mr. Ortiz. `Curio.voice` with `scope: () => state.mode + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event `promise`: the promise in the candidate's voice.
- event, whole, `who`: each "Who really does this" line.
- event `bin-no`: "Think: is this a class, school, town, state or country job?"
- how `speech`: "Find a put-down or a promise Priya can't keep. Tap the line."
- event, whole, `new-speech`: Priya's fixed speech.
- event, whole, `secret`: "Nobody sees how you voted. That's a secret ballot."
- event, whole, `half`: "The winner changed because of who came to vote."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
election has no family doc or engine yet; campaign-manager (grade 12) is the other member. Tool-only code: promise sort with a job picker, the speech editor, a ballot with a secret booth, vote counts with a turnout replay. Keep the ballot and count as one plain object so campaign-manager can lift it.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Promises | Put everything in "This job" | Only five of twelve belong there; wrong drops light the level ladder. |
| Promises | Pick jobs at random | Five jobs; the wrong one names the level to think about. |
| Speech | Flag every line | Fine lines say so; replacements that are still unfair are refused with a reason. |
| Vote | Vote for anyone | Any vote counts; the lesson is the turnout replay. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Tap a poster: `promise`; drop: `who` (whole) or `bin-no`.
2. Speech: `speech`; fixes; `new-speech` (whole).
3. Vote: `secret` (whole); results; `half` (whole) after the replay.
4. How we decide: each column's summary (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.1, 2, 7 and 11 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Mayors run town services such as road repair and pools; councils vote on town budgets | National League of Cities, "Forms of Municipal Government" and "Cities 101" | Wikipedia, Mayor-council government (checked 2026-11-09) | yes |
| State highway speed limits are set by the state, not towns | Federal Highway Administration, "Methods and practices for setting speed limits" | Insurance Institute for Highway Safety, "Speed limit laws by state" | yes |
| Only the federal government prints money (Congress's power; the Bureau of Engraving and Printing, part of the Treasury) | U.S. Constitution, Article I, Section 8 (National Archives) | Bureau of Engraving and Printing, "About us" | yes |
| School boards make district decisions such as school hours and buying school equipment | National School Boards Association, "About school boards" | Ballotpedia, "School board" | yes |
| A secret ballot means no one can see how a person voted | Wikipedia, Secret ballot (checked 2026-11-09) | U.S. Election Assistance Commission, voter guides | yes |
| Who turns out can change an election result | U.S. Census Bureau, "Voting and registration" turnout data | Ballotpedia, "Close elections" and turnout | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r5, 2026-11-09): twelve promises split 5 This job, 5 Different job, 2 Nobody; class race 12 to 11 before the child's vote; town 310 to 290 with 600 voters and 130 to 170 with 300, so the replay flips the winner; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 posters, card and bins fit; at 680x425 posters become a list.
2. Twelve promises take only their bins. (D2.Civ.1.3-5)
3. "A different job" takes only the right job, and its card plays. (D2.Civ.1.3-5)
4. Both speech problems are fixed only with fair, keepable lines. (D2.Civ.7.3-5)
5. The town replay with half the voters flips the winner. (D2.Civ.2.3-5)
6. The How we decide card matches each place to its method. (D2.Civ.11.3-5)
7. The secret booth hides the ballot; Class election blanks between voters and keeps nothing after closing.
8. `What if only half voted?` and `Count` are never named before they show.
9. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
10. Motion off: no curtain or ballot motion; no network requests.

## Open questions
- None for Cory.
