# Town Council

## One idea
The child takes a seat on the town council as Mayor Brooks opens a meeting about the empty lot next to the school, which could become a park or a parking lot; three neighbors speak (a grandfather who wants benches and shade, a shop owner whose customers have nowhere to park, a kid who wants a soccer field), and after each the child waits for the gavel, picks a reply that truly answers what that person said, and marks how their own view compares; role cards show what the mayor, the council and the town staff each are allowed to do, and the vote ends with the child hearing who is glad and who is disappointed and why, so a second grader learns what a town government is for, who decides what, and how to take part in a meeting.

## Not like
- pool-repair-vote (3, concept): a grade 3 policy choice and how to pay for it. Here who does what in a town and how to speak at a meeting.
- school-fix-it-meeting (3, concept): a school problem with surveys. Here a town council and its roles.
- community-helpers-village (1, spec): which helpers a town needs. Here how a town decides.
- playground-rules (K, spec): a class vote on one rule. Here a council meeting with roles and turns.
- wonder-kite, how-do-you-know, changemaker-cards, my-life-timeline (this batch): questions, sources and timelines. Here a meeting.

## Who and how
- Grade 2, Social Studies (Civics), module "Community Helpers and Government". Standards: D2.Civ.1.K-2 (describe roles and responsibilities of people in authority), D2.Civ.5.K-2 (explain what governments are and some of their functions), D2.Civ.9.K-2 (follow agreed-upon rules for discussions while responding attentively to others), D2.Civ.10.K-2 (compare their own point of view with others' perspectives). D2.Civ.11.K-2 and D4.8.K-2 moved to playground-rules (idea card).
- Driver: one child alone, or the teacher on the projector with the class choosing replies; every line, card and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- One meeting with three speakers, role cards, and a vote. tool.json `modes: ["Meeting", "Who decides"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.5.K-2 | Hear the mayor open the meeting and sort town jobs into "We can do it alone" or "We need the town" | the jobs sorted under a house icon or a town hall icon | 2 |
| D2.Civ.1.K-2 | Match each decision to who is allowed to make it: Mayor, Council or Town staff | the role cards with their decisions pinned on | 3 |
| D2.Civ.9.K-2 | Raise your hand, wait for the gavel, and pick the reply that answers the last speaker | the hand, the gavel, the three reply cards | 4, 5 |
| D2.Civ.10.K-2 | After each speaker, slide your view: "Same as theirs", "Some the same", "Different" | the view meter beside each speaker's face | 6 |

## Screens and modes
Header (kit): title "Town Council"; `Meeting`, `Who decides`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** The council room: a long table with five seats, Mayor Brooks in the middle with a gavel, a big screen showing the empty lot by the school. The child's seat has a blank name plate and three name choices with pictures (Council Member Star, Council Member Oak, Council Member River). The welcome is queued (`welcomeAfter: true`): "Welcome to the town council! You have a seat at the table. Tap a name for your name plate." First hint: "Tap a name for your name plate." The first tap sets the plate and cuts the welcome.

**Opening (focus: the mayor).** Mayor Brooks taps the gavel: "This meeting is open. A town government does jobs that people can't do alone. Let's sort some jobs." Six job cards, each a picture: build a park, fix a big road, mow my own yard, keep the water clean, make my lunch, put out a fire. Two bins: "We can do it alone" (a house) and "We need the town" (a town hall). Wrong drop: "Could one family fix a whole road?" When sorted: "Tonight's job: the empty lot. Park or parking lot? Let's hear from our neighbors."

**Meeting (focus: the speaker at the podium).** At 1366x768 the podium and speaker are center, the child's seat and hand button are bottom center, the view meter is at the right, and the lot on the screen is at the top. At 680x425 the lot screen hides behind a `Lot` button.
- Each speaker walks to the podium and talks (whole):
  1. Mr. Ellis, a grandfather: "I walk to the school to pick up my granddaughter. There's nowhere to sit, and there's no shade. Please make a park with benches and trees."
  2. Ms. Rivera, who owns the shoe shop: "My customers drive around and around because there's nowhere to park. Some give up and go home. My shop needs parking."
  3. Dev, a third grader: "We play soccer on the sidewalk. It isn't safe. Can we have a field?"
- Turn: a `Raise hand` button. When the child taps it, the hand rises; Mayor Brooks taps the gavel and says "Council Member [name], you have the floor." Then three reply cards show (spoken on tap, picked with `Say it`). If the child taps a reply card before the gavel, Mayor Brooks says "Please wait for your turn," and the hand stays up.
- Reply cards for each speaker: one answers what they said, one is about something else, one is unkind. For Mr. Ellis: "You need a place to sit and some shade. Could benches go by the path?" / "I like ice cream." / "Grandpas can stand." The answer card earns a nod from the speaker and a gold mark; the others get Mayor Brooks: "Did that answer what Mr. Ellis said? Try again."
- View meter: after each speaker, a three-step slider: "Same as theirs", "Some the same", "Different", with faces. The child's choice is noted beside the speaker's picture. There is no right answer.

**Who decides (focus: three role cards).** Opens after the three speakers (also from the header). Cards: Mayor (leads the town and runs meetings; a gavel icon), Council (votes on town rules and how town money is spent; a raised hands icon), Town staff (do the town's work: the parks crew builds parks, the traffic engineer plans streets and parking; a hard hat icon). Six decisions to drag to the right card: "Who runs this meeting?" (Mayor), "Who votes on the lot?" (Council), "Who plants the trees?" (Town staff, parks crew), "Who draws where cars park?" (Town staff, traffic engineer), "Who decides how much money to spend?" (Council), "Who says 'This meeting is open'?" (Mayor). Wrong drop: the card shakes and its job line plays again.

**The vote (focus: three plan pictures).** Mayor Brooks: "Any ideas?" Three plans with pictures: All park (benches, trees and a small field); All parking (30 spots); Some of both (a small park with benches and trees, a field, and 10 parking spots by the shop). The child taps one and `Propose`. Then the five council members vote; the four illustrated members always split two for park and two for parking on the first two plans, so the child's vote decides those; for "Some of both", one from each side joins the child, so it passes 3 to 2. Each result shows the lot built, then the three neighbors say how they feel:
- All park: Mr. Ellis and Dev glad; Ms. Rivera disappointed: "My shop still has nowhere for customers to park."
- All parking: Ms. Rivera glad; Mr. Ellis and Dev disappointed.
- Some of both: "Nobody got everything. Everybody got something." Each speaker says one glad and one wish line.
- Mayor Brooks closes: "Thank you, neighbors. That's how a town decides together." `Meet again` restarts with the same speakers. `Print` prints the child's replies, view meter and vote.

## Content
- Six town job cards; three speakers each with one speech, three reply cards and three outcome lines; three role cards; six decisions; three plans.
- Council members (illustrated, non-speaking except their vote): two lean park, two lean parking.

## Interactions in detail
- Every tap acts at once; a new line stops the old one; tapping `Raise hand` during a speech queues the gavel to follow the speech's end, because the speech is whole.
- `Say it` shows only after a reply card is tapped. `Propose` shows only after a plan is tapped. `Who decides` opens after the third speaker; before that the hint names the next speaker.
- With Motion off speakers appear at the podium without walking, and the lot changes without building.

## Look
- Accent `--brand` #2f6a33 town green (header, the table, role card frames); gold #f4c542 (the gavel's ring, the answer mark, the passing plan); paper #f1f7ef; ink #0e2410; muted #4f5c4d.
- Contrast (WCAG 2.1, computed): white on brand 6.50:1; brand on paper 5.97:1; ink on paper 15.09:1; muted on paper 6.49:1; ink on gold 10.10:1.
- Never color alone: view meter steps carry faces and words; role cards carry icons and words; votes are hands with counts.
- Different from this batch (timeline terracotta, kite sky blue, changemaker purple, backpack mustard).

## Art
- People art goes to Gemini with `people: true`: Mayor Brooks (4 poses: gavel, listening, pointing, closing; cutout yes); Mr. Ellis, Ms. Rivera and Dev (4 poses each: speaking, nodding, glad, disappointed; cutout yes); four council members (2 poses each: sitting, hand raised; cutout yes); the child's seat seen from behind (no face).
- Local FLUX (`scripts/localart.py`): the council room (16:9); the empty lot and its three built versions (4, 16:9); six job cards (6, 1:1).
- Drawn in code: the gavel, hand, reply cards, view meter, role cards, vote tally, bins.
About 39 images.

## Voice
Four bank voices, each unique in this batch: `firm-captain` as Mayor Brooks and narrator; `calm-professor` as Mr. Ellis; `smooth-narrator` as Ms. Rivera; `casual-peer` as Dev. `Curio.voice` with `scope: () => state.mode + ':' + state.speaker + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Welcome to the town council! You have a seat at the table. Tap a name for your name plate."
- event, whole, `open`: "This meeting is open. A town government does jobs that people can't do alone. Let's sort some jobs."
- event `sort-no`: the job's question line.
- event, whole, `lot`: "Tonight's job: the empty lot. Park or parking lot? Let's hear from our neighbors."
- event, whole, each speech.
- how `hand`: "Tap Raise hand when you want to speak."
- event, whole, `floor`: "Council Member [name], you have the floor."
- event `wait`: "Please wait for your turn."
- event `reply`: the reply card's words, then the speaker's nod or "Did that answer what [speaker] said? Try again."
- how `meter`: "Is your view the same as theirs, some the same, or different? Slide it."
- how `roles`: "Drag each question to who decides."
- event, whole, `ideas`: "Any ideas? Tap a plan, then Propose."
- event, whole, vote count and each neighbor's outcome line; `close`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the turn system (hand, gavel, floor), reply cards, view meter, role-card drag, and the vote with fixed council leanings.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Turn | Tap reply cards right away | Before the gavel, the mayor asks the child to wait and nothing is said. |
| Reply | Try all three | The unkind and off-topic replies play the "Did that answer" line naming the speaker's point; the gold mark comes only from the answer card. |
| Roles | Drag at random | Six decisions; wrong drops replay each role's job line. |
| Vote | Always pick the same plan | Every plan is allowed; each result shows who is glad and disappointed, which is the lesson. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a name: the plate sets.
2. `open` (whole); sort: chimes or `sort-no`; `lot` (whole).
3. Each speaker: speech (whole), waits; `hand` (once); `Raise hand`: `floor` (whole); reply: `reply`; then `meter`.
4. Who decides: `roles`; drops.
5. Vote: `ideas` (whole); `Propose`: vote count, three outcome lines (whole, in turn), `close` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.1, 5, 9 and 10 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| In a mayor-council town, an elected mayor leads the town and an elected council votes on local laws and the budget | Wikipedia, Mayor-council government (checked 2026-11-09) | National League of Cities, "Forms of Municipal Government" | yes |
| Town staff (such as a parks department and traffic engineers) carry out the town's work | National League of Cities, "Cities 101: Municipal services" | International City/County Management Association (ICMA), local government services | yes |
| Local governments provide services people can't easily provide alone, such as roads, parks, water and fire protection | iCivics, "Why Government?" and local government lessons | National League of Cities, "Cities 101" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r3, 2026-11-09): with council leanings 2 park and 2 parking, All park passes only with the child's yes (3 to 2), All parking likewise, Some of both passes 3 to 2 with one member from each side; each speaker has exactly one answer card; six decisions split 2 Mayor, 2 Council, 2 Town staff; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 podium, seat, meter and lot screen fit; at 680x425 the lot hides behind `Lot`.
2. The job sort puts park, road, water and fire under "We need the town". (D2.Civ.5.K-2)
3. Six decisions land on Mayor, Council and Town staff correctly. (D2.Civ.1.K-2)
4. A reply before the gavel is held with "Please wait for your turn." (D2.Civ.9.K-2)
5. Only the reply that answers the speaker earns the mark. (D2.Civ.9.K-2)
6. The view meter records a view for each speaker. (D2.Civ.10.K-2)
7. All three plans can pass, and each plays who is glad and who is disappointed.
8. `Say it`, `Propose` and `Meet again` are never named before they show.
9. Tap while it plays: a tap during a line acts at once except whole speeches; no older line plays after a newer one.
10. Motion off: no walking or building; no network requests.

## Open questions
- None for Cory.
