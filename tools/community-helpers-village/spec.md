# Community Helpers Village

## One idea
The class places six helpers around a quiet village (a baker, a mail carrier, a firefighter, a librarian, a crossing guard and a neighbor who shovels walks) and watches the village wake up, then takes any one helper away and watches the same day replay without them (no bread, letters piling up, a dark library), so first graders see that everyone, not just the mayor, keeps a community running, and how each helper is paid for the work.

## Not like
- town-council (2, concept): a council deciding as a government. Here everyday helpers, and what breaks without one.
- storm-helpers (2, concept): one storm and how kids can help. Here an ordinary day and a snow day shared by everyone.
- teddy-bear-makers (1, concept, this batch): the steps of making one product. Here many jobs that keep a town going.
- market-day (1, concept, this batch): buying goods and services with tokens. Here who does the work and who pays them.
- playground-rules (K, spec): rules for a group. Here roles in a community.

## Who and how
- Grade 1, Social Studies (Civics and Economics), module "Families and Communities". Standards: D2.Civ.2.K-2 (all people, not just official leaders, play important roles in a community), D2.Civ.6.K-2 (how communities accomplish common tasks, set responsibilities and fill roles of authority), D2.Eco.12.K-2 (goods and services that governments provide), D2.Eco.6.K-2 (how people earn income; moved here from backpack-pack).
- Driver: teacher on the projector with the class choosing, or one child alone; every helper, card and line is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Three parts: Village (place and remove), Helper cards (work and pay), Snow day. tool.json `modes: ["Village", "Helper cards", "Snow day"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.
- Nothing is saved; `Print` prints the six helper cards.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.2.K-2 | Take one helper away and watch the day replay without them, for any helper, including the volunteer neighbor | the replay with that helper's spot gone wrong | 3 |
| D2.Eco.6.K-2 | Tap a helper card's coin to hear how they earn money for their work and one thing that pay buys at home | the card's pay side | 4 |
| D2.Eco.12.K-2 | Sort helpers onto "The town pays" (a town hall icon) or not | the town hall tags | 5 |
| D2.Civ.6.K-2 | On snow day, give each task to a helper and see who is in charge of what, with the mayor as one helper | the snow day jobs board and the cleared village | 6 |

## Screens and modes
Header (kit): title "Community Helpers Village"; `Village`, `Helper cards`, `Snow day`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** Early morning in a small village: a bakery, a post office, a fire station, a library, a school crossing and a row of houses, all quiet, with six glowing empty spots. Six helpers wait in a row at the bottom. The welcome is queued (`welcomeAfter: true`): "Good morning, village! Nobody's at work yet. Drag a helper to their place in town." First hint: "Drag a helper to a glowing spot." The first tap on a helper says their name and cuts the welcome.

**Village (focus: the village scene).** At 1366x768 the village fills the screen with the helper row at the bottom; after all six are placed, `Play the day` and a `Take one away` picker appear under the scene. At 680x425 the helper row becomes a scrolling strip of faces.
- Drag a helper to a spot (or tap the helper, then the spot). The right spot: the place comes alive (bread in the window, mail in boxes, the fire truck shiny, library lights on, kids crossing safely, a shoveled sidewalk) and the helper says one line. A wrong spot: the helper shakes their head ("I don't bake bread! I bring the mail.") and goes back.
- `Play the day`: a 12-second day plays with all six at work: morning bread, kids crossing, mail delivered, a story time, a small kitchen fire put out, a snowy walk shoveled for an older neighbor.
- `Take one away`: tap a helper's face. Their spot goes empty and the day replays without them. Each has its own painted outcome:
  - Baker: an empty bakery window and a sign drawn in code ("No bread today"); families with empty bags.
  - Mail carrier: letters and boxes piling up at the post office; a birthday card never reaches Grandpa.
  - Firefighter: the smoke from the kitchen fire grows and neighbors wait outside worried (no flames shown at people; kind, not scary).
  - Librarian: a dark library with the door locked at story time.
  - Crossing guard: kids waiting at the curb, unable to cross.
  - Shoveling neighbor: an older neighbor at her door, unable to walk out on the icy steps.
  After each: "Everyone helps the village. What happens without them? Put them back with Put back."

**Helper cards (focus: one big card).** Six cards in a row; tap one to open it. Front: the helper at work and what they do. Back (tap the coin): how they earn money and one thing it buys at home. Each card also has a town hall tag: "The town pays" (firefighter, librarian, crossing guard), or how else they are paid (baker: people buy her bread; mail carrier: the Post Office pays, from stamps people buy; neighbor: no pay, helps for free). The class sorts the six onto two mats, "The town pays" and "Paid another way or helps for free", before the tags show; the tags then confirm.

**Snow day (focus: the snowy village and a jobs board).** Snow covers everything. Four tasks on the board: plow the streets, shovel the walks by the school, check on Mrs. Lee next door, keep the library open as a warm place. The mayor appears as a seventh helper: "I'm the mayor. I make sure the plows go out. But I can't do it all!" The class drags a helper to each task (road crew for plowing; the shoveling neighbor; the mail carrier who checks on Mrs. Lee on the route; the librarian). Any reasonable match is accepted with a line; a mismatch (the baker plows) gets a friendly "Can a baker drive a plow? Who does that job?" When all four are filled, the village clears and the mayor thanks everyone.

## Content
- Helpers, places, one-line work, pay and buy lines:
  - Baker (Rosa, a Mexican American woman in her forties) at the bakery: "I bake bread before the sun is up." Pay: "People buy my bread, and that money is my pay." Buys: "shoes for my kids."
  - Mail carrier (Mr. Thomas, a Black man in his fifties) at the post office: "I bring letters and boxes to every house." Pay: "The Post Office pays me, from the stamps people buy." Buys: "groceries."
  - Firefighter (Captain Sato, a Japanese American woman in her thirties) at the fire station: "I put out fires and keep people safe." Pay: "In our village, the town pays firefighters with money everyone shares, called taxes. In some towns, firefighters are volunteers." Buys: "our rent."
  - Librarian (Mr. Aziz, an Egyptian American man in his sixties) at the library: "I help you find books and run story time." Pay: "The town pays me." Buys: "a bike for my grandson."
  - Crossing guard (Ms. Nguyen, a Vietnamese American woman in her seventies) at the school crossing: "I help kids cross the street safely." Pay: "The town pays me." Buys: "seeds for my garden."
  - Shoveling neighbor (Jake, a white teenager with a shovel) by the houses: "I shovel walks for neighbors who can't." Pay: "Nobody pays me. I help because we're neighbors."
- Snow day: the road crew (two workers in a plow, painted) is the town's; the mayor (Mayor Begay, a Diné woman in her fifties) is one of the helpers.
- Teacher note: who pays for what differs by town; in many U.S. towns firefighters are volunteers, and some librarians work for a county.

## Interactions in detail
- Every tap acts at once; a new line stops the old one; taking away another helper during a replay restarts the day without that one.
- `Play the day` and `Take one away` show only after all six are placed; before that the hint says "Drag a helper to a glowing spot." and never names them.
- `Put back` restores the helper at once.
- With Motion off the day shows as four still pictures (morning, midday, afternoon, evening) with the same outcomes.

## Look
- Accent `--brand` #a14a0b warm brick orange (header, card frames, the jobs board); gold #f4c542 (glowing spots, the coin); paper #fdf4ec; ink #2e1503; muted #6b5546. Scene: a small village in morning light, then in snow.
- Contrast (WCAG 2.1, computed): white on brand 6.00:1; brand on paper 5.52:1; ink on paper 15.78:1; muted on paper 6.41:1; ink on gold 10.54:1.
- Never color alone: mats have icons and words; empty spots show an outline and a missing-person picture.
- Different from this batch (market teal, map navy, capsule slate, workshop raspberry).

## Art
- Local FLUX (`scripts/localart.py`): the village in morning, all quiet (1, 16:9); each of six places in "working" and "without" states (12, 4:3); the snowy village and the cleared snowy village (2, 16:9).
- People art goes to Gemini (`people: true`): the six helpers, the mayor and two road crew workers, each 3 poses (standing, at work, waving), Mrs. Lee (a Korean American woman in her eighties) at her door, kids crossing (3); "illustrated community helper <name, work clothes> <pose>, soft gouache, plain white background, friendly face"; 3:4; cutout yes. Helpers are cutouts placed on their spots so each shows whole.
About 47 images. Drawn in code: spots, mats, tags, the jobs board, sign text.

## Voice
Bank voice `friendly-dad` as the narrator (unique in this batch); each helper's lines are read by the narrator in a light character style (one voice keeps the K-2 pacing simple). `Curio.voice` with `scope: () => state.mode + ':' + state.helper + ':' + state.removed`, `welcomeAfter: true`.
- how `welcome`: "Good morning, village! Nobody's at work yet. Drag a helper to their place in town."
- event `name`: the helper's name and job.
- event `placed`: the helper's work line.
- event `wrong-spot`: the helper's head-shake line.
- how `all-placed` (once): "Everyone's at work! Tap Play the day."
- event, whole, `without`: the outcome line for the removed helper ("No bread today! The baker is the one who bakes it.").
- how `without-tip` (first two times): "Everyone helps the village. Tap Put back."
- how `cards`: "Tap a card to open it. Then drag it: does the town pay, or not?"
- event `pay`: the pay and buy lines.
- how `snow`: "It snowed! Drag a helper to each job."
- event `mayor`: the mayor's line (whole, once).
- event `task-ok`, `task-no`: the match lines.
- event, whole, `cleared`: "The village is clear! The mayor didn't do it alone. Everyone helped."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: spots that accept one helper, a day replay with one helper removed, two-sided cards with a pay sort, the snow day jobs board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Place | Drag helpers anywhere | Each spot takes only its helper; others shake their heads and say their job. |
| Take away | Never remove anyone | `Play the day` alone shows everything fine; the Village hint keeps naming `Take one away` until one is removed, and the cards mode opens anyway (it's an explorer). |
| Pay sort | All to "The town pays" | Tags show after the sort, and the baker, mail carrier and neighbor each say how they are really paid. |
| Snow day | Drag anyone anywhere | Mismatches get a question naming the job; the village clears only with matches. |
| Snow day | The mayor does every job | The mayor can't be dragged to a task; she says "I can't do it all!" |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a helper: `name`. Drop: `placed` or `wrong-spot`.
2. Sixth placed: `all-placed`. Play the day: the day plays (no speech except the fire bell sound).
3. Take one away: `without` (whole), then `without-tip` (first two times).
4. Cards: `cards` (first time); coin: `pay`. Sort: each drop waits for the last line.
5. Snow day: `snow`, then `mayor` (whole); each drop `task-ok` or `task-no`; done: `cleared` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.2, D2.Civ.6, D2.Eco.6, D2.Eco.12 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The U.S. Postal Service pays its workers from postage and products, not from taxpayer funding | Wikipedia, United States Postal Service (checked 2026-11-09) | USPS, "Postal Facts" (no tax dollars for operating expenses) | yes |
| About half or more of U.S. firefighters are volunteers; many towns pay career firefighters | Wikipedia, Volunteer fire department (NFPA figure: 54 percent volunteer, checked 2026-11-09) | National Fire Protection Association, U.S. Fire Department Profile | yes |
| Public libraries in the U.S. are mostly paid for by local government | Institute of Museum and Library Services, Public Libraries Survey | American Library Association, library funding facts | yes |
| Towns and cities pay for snow plowing of public streets and for school crossing guards | National League of Cities, municipal services | a sample city budget (for example, City of Minneapolis Public Works budget) | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-09): the saved pages contain "no longer received taxpayer funding" and "54 percent of firefighters"; each of six spots accepts exactly one helper; the pay sort keys three helpers to "The town pays" and three not; each snow task has at least one accepted helper and the mayor is never a draggable answer; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the village fills with the helper row; at 680x425 the row becomes a strip.
2. Each helper fits only their spot and the place comes alive.
3. Taking away any helper, including the volunteer, replays the day with that helper's own painted outcome. (D2.Civ.2.K-2)
4. Each card's coin tells how the helper earns money and what it buys. (D2.Eco.6.K-2)
5. The pay sort and town hall tags show what the town provides. (D2.Eco.12.K-2)
6. Snow day fills four tasks with helpers and the mayor as one of them. (D2.Civ.6.K-2)
7. Play the day and Take one away are never named before they show.
8. Tap while it plays: any tap during the day acts at once; no older line plays after a newer one.
9. Motion off: four stills; no network requests.

## Open questions
- None for Cory.
