# Community Project Planner

## One idea
Lead a six-week neighborhood project where the scarce resource is not money but your volunteers: match people to work they're good at, ask what they need, let them rest, and see whether the project and the team both make it to the finish.

## Not like
- resilience-map (9-12, explorer): there a student explores stress and builds a personal coping plan. Here nothing is about the student's own feelings; the plan is a team project, and the "energy" belongs to fictional volunteers.
- decision-tree (6-8, builder): there you map one choice into branching consequences. Here there is no tree; choices repeat every week and add up over time, tycoon style, with three resources (hours, dollars, team energy) running at once.
- conflict-coach (6-8, roleplay): there the skill is the wording of one hard conversation. Here there is no dialogue to pick; leadership is what you do (who works where, which lead move, rest or push).
- first-apartment-budget, savings-plan, corner-store (money tycoons and planners): there money is the point. Here money is the smallest of the three resources, and the outcome depends mostly on how people are treated.

## Who and how
- Grade 9-12, Social and Emotional Learning, module "Leadership and Community (SEL)".
- Driver: students (one laptop each or in pairs). A teacher can run one project on a projector during advisory and let the class vote on each week's lead move. 20 to 35 minutes for one project; Plan Your Own is a second period or homework.
- Standards: CASEL Relationship Skills ("Showing leadership in groups", "Practicing teamwork and collaborative problem-solving", "Seeking or offering support and help when needed"). Also CASEL Responsible Decision-Making ("Reflecting on one's role to promote personal, family, and community well-being").
- Sensitive by default: the projects, neighborhood and volunteers are made up. Run a Project has no text input. Plan Your Own takes text about a project only (never about a person): roles, not names. Nothing is stored unless the student presses Save.

## Screens and modes
Header: title "Community Project Planner", mode tabs `Run a Project`, `Plan Your Own` (`.seg`), icon buttons `Motion`, `Sound`, `Read`. Links `kit:curio` then `kit:theme-912`, own `--brand`. Opens in Run a Project on the project picker. Stage left, panel right (`.panel`, hint id `hint`).

### Run a Project
1. **Picker** (stage): three project cards, each with its banner image, name, one-line goal, budget, and a difficulty word: "Riverside Cleanup (start here)", "Library Lot Garden", "Winter Coat Drive (tight budget)". A line under them: "Maple Street is a made-up neighborhood. The volunteers are made up too." Button on each card: `Lead this project`.
2. **Week board** (stage), top to bottom:
   - Banner strip (the project's 4:1 image) with the project name and "Week N of 6".
   - Task board: a grid of task cards (3 columns wide at 1366 px, 2 under 1000 px). Each card: skill color stripe plus skill icon and word, task name, a progress bar "18 / 50", state label, a "This week: +N" preview, and the names of volunteers assigned. Core tasks carry "Core"; the bonus task carries "Bonus". A `Fundraise` card is always present (Outreach skill, never Done).
   - Team row: six volunteer cards (painted portraits, see Art and Interactions). Each: face, name, strong skill (filled icon), okay skill (outline icon), "5 h a week", energy bar with a band word, "Cares about: ?" (revealed after the first Check in), and a select "Working on" (Rest, then every Open task, then Fundraise).
3. **Panel**: section WEEK ("Week 3 of 6", money "$412", total hours this week); section LEAD MOVE (six `.btn` toggles, one pressed at a time: `Thank the team`, `Ask for ideas`, `Check in`, `Planning meeting`, `Push harder`, `No lead move`, default `No lead move`); the hint; buttons `Clear assignments`, big `Run week 3`; small `Restart project` and `Pick another project` at the bottom.
4. **Event card**: at the start of weeks 2, 4 and 5, a card over the board (not a browser dialog) with the event text and two buttons (the two options, with their costs written on them). The board is inert until one is chosen. An option the team cannot afford is disabled with "Not enough money".
5. **Week summary** (replaces the task board until dismissed): per task "+N" (and "Done" if finished), per volunteer energy change with a reason ("-6, worked on a strong skill", "+20, rested", "+8, thanked"), any check-in notes, money in and out. Button `Start week N+1` (after week 6: `See how it went`).
6. **Report** (stage): outcome sentence (tiers in Content), core tasks done "4 of 5", bonus done or not, money left, hours given, what it means lines for each Done task, team row with final energy words, and three discussion questions. Buttons `Try it again`, `Pick another project`, `Print report`.

### Plan Your Own
Stage: a one-page plan form above a timeline chart. Panel: hint, budget readout, gentle notes, buttons.
- Fields: `Project name` (60 chars), `Who it helps` (80), `What done looks like` (120), `Budget we have` (number, $0 to $10,000).
- Task table, up to 8 rows (`Add task`, a remove `x` per row, start with 3 empty rows): Task (50 chars), Skill (select: Hands-on, Outreach, Logistics, Design), Role (select: Project lead, Outreach lead, Build lead, Logistics lead, Design lead, Anyone), Weeks (six toggles W1 to W6), Supplies $ (number).
- "How I'll keep the team going" checkboxes: Thank people in public, Ask for ideas, Check in one by one, Hold a planning meeting, Plan rest weeks.
- Timeline: drawn in code, one row per task with a name, a bar on each chosen week, filled in its skill color with its skill's pattern (hatch, dots, solid, stripes) so color is not the only signal.
- Panel: readout "Supplies $X of $Y" then "$Z left" (ok) or "Over by $Z" (warn, with a "!" glyph); notes (Content); buttons `Start from an example` (opens three choices: the three projects), `Print plan`, `Save on this device`, `Clear`. A line in the panel: "This stays on this computer. Nothing is sent anywhere. Save keeps it here until you press Clear."

## Content

### Volunteers (same six in every project)
| Name | Strong | Okay | Hours a week | Cares about | Look (portrait) |
|---|---|---|---|---|---|
| Dana Okafor | Hands-on | Logistics | 6 | Thanks | skin #6b3f26, short coily black hair, green hoodie |
| Luis Herrera | Outreach | Design | 5 | Having a say | skin #b07a50, wavy dark hair, blue jacket |
| Mei Chen | Logistics | Outreach | 4 | A clear plan | skin #e9c39c, black bob with bangs, yellow sweater |
| Tariq Haddad | Design | Hands-on | 5 | Having a say | skin #c08b5c, short black hair, glasses, gray shirt |
| Grace Whitehorse | Outreach | Logistics | 3 | Check-ins | skin #9a6440, long straight black hair, red flannel |
| Ben Novak | Hands-on | Design | 6 | Check-ins | skin #f3cfae, short red-brown hair, freckles, purple tee |
Team total 29 hours a week. Names and looks are mixed on purpose; no trait is tied to a group.

### Skills (color, icon, timeline pattern)
Hands-on #e8b04a hammer, hatch. Outreach #7cc7ff megaphone, dots. Logistics #ff9ad5 (pink) clipboard, solid. Design #c9a0ff pencil, stripes.

### Projects (made up; prices are round made-up numbers)
Task format: name, skill, need (points), supply and cost, lock, what it means.

**Riverside Cleanup** (start here). Goal: "Clean a mile of the river trail and keep it clean." Budget $400.
1. Map the trash hot spots: Logistics, 20, no supply. Core. "You know where the worst spots are."
2. Sign up cleanup volunteers: Outreach, 35, no supply. Core. "About 40 neighbors signed up for cleanup day."
3. Cleanup day: Hands-on, 50, gloves, bags and grabbers $150, locked until Map is Done. Core. "A mile of riverbank is clean."
4. Sort the recycling: Hands-on, 20, no supply. Core. "Cans and bottles went to recycling, not the landfill."
5. Keep It Clean trail signs: Design, 25, signboards $90. Core. "Signs at each trail entrance."
6. Bonus, Before-and-after photo show: Design, 20, prints $40. "The library shows the photos for a month."

**Library Lot Garden**. Goal: "Turn the empty lot beside the library into a garden anyone can use." Budget $600.
1. Get permission and plan the beds: Logistics, 20, no supply. Core. "The city said yes, and the plan fits the lot."
2. Build six raised beds: Hands-on, 50, lumber $240, locked until task 1 is Done. Core. "Six raised beds stand in the lot."
3. Fill and plant: Hands-on, 30, soil and seedlings $180, locked until task 2 is Done. Core. "The beds are planted."
4. Recruit neighbors to water: Outreach, 30, no supply. Core. "A watering schedule with a name for every day."
5. Signs and a garden map: Design, 20, paint and boards $60. Core. "Anyone can find their way around."
6. Bonus, Opening day: Logistics, 25, snacks and tables $50. "Neighbors came to see it open."

**Winter Coat Drive** (tight budget). Goal: "Collect, clean and hand out warm coats before the cold." Budget $300.
1. Flyer and poster design: Design, 15, no supply. Core. "A flyer people actually read."
2. Spread the word: Outreach, 40, flyer printing $60, locked until task 1 is Done. Core. "The whole neighborhood heard about it."
3. Drop-off boxes at five places: Logistics, 20, boxes $40. Core. "Five places to drop off a coat."
4. Sort and wash coats: Hands-on, 45, laundromat $120. Core. "About 120 coats are clean and sorted by size."
5. Hand-out day: Logistics, 30, racks and hangers $50, locked until task 4 is Done. Core. "Families picked out coats that fit."
6. Bonus, Hat and glove table: Outreach, 20, no supply. "Stores gave hats and gloves to go with the coats."

Fundraise (all projects): Outreach, earns $6 per point, never Done.

### Events (start of the week; option costs as written)
Riverside Cleanup
- Week 2, "Rain raised the river and moved the trash." A `Re-map the hot spots`: Map need +10. B `Wait a week to look`: Map and Cleanup day take no hours this week.
- Week 4, "A local news station asks for an interview." A `Send Luis`: Luis has 4 fewer hours this week; Sign-up need -15 (if Sign-up is Done, a viewer donates $30 instead). B `Skip it`: nothing.
- Week 5, "Half the grabbers broke." A `Buy more ($40)`: -$40. B `Borrow from the parks department`: Grace has 3 fewer hours this week.
Library Lot Garden
- Week 2, "Lumber went up $40." A `Pay the new price`: lumber +$40 if not bought yet, else -$40 now. B `Ask the hardware store for a deal`: Luis has 3 fewer hours this week; price stays.
- Week 4, "A heat wave is coming." A `Keep the usual hours`: everyone who works this week loses 8 more energy. B `Work early mornings`: Hands-on progress x0.8 this week.
- Week 5, "A neighbor says a bed blocks the sidewalk path." A `Listen and redraw the map`: Signs need +8, everyone +4 energy. B `Say it's approved and move on`: Recruit neighbors need +10 (word gets around).
Winter Coat Drive
- Week 2, "A store offers 40 coats if someone picks them up." A `Send Dana with a car`: Dana has 3 fewer hours this week; Sort need +10; the report counts about 160 coats. B `Say thanks, not now`: nothing.
- Week 4, "Snow closes the community center this week." A `Move to the library meeting room ($25)`: -$25. B `Take the week off`: no task takes hours this week; everyone rests (+20).
- Week 5, "Mei and Luis disagree about who should get coats first." A `Hear both, then set a fair rule together`: this week's lead move is used up (set to No lead move, toggles disabled); Mei and Luis +6 energy. B `Decide it yourself, fast`: Mei and Luis -10 energy.

### Lead moves (one per week)
- Thank the team: everyone +6; "Thanks" people +8 more.
- Ask for ideas: everyone +3; "Having a say" people +10 more; the team's idea cuts 8 points from the Open core task with the most need left (ties: first in list).
- Check in: everyone +3; "Check-ins" people +10 more; reveals "Cares about" on every card for the rest of the project; each volunteer gives a note by band (below).
- Planning meeting: "A clear plan" people +10; all progress this week x1.15.
- Push harder: everyone who works gives x1.5 hours and loses 10 more energy.
- No lead move: nothing.
- Repeat rule: the same move two weeks in a row gives half its energy bonuses (round down). Summary says "Same move as last week: it lands a little softer."

### Check-in notes (by energy band at week start)
Fired up: "I'm good. Keep it coming." Steady: "Doing fine. A thank-you goes a long way." Tired: "I could use a lighter week." Running on empty: "Honestly, I need a week off." Stepping back: "I'll be back. I just need a break."

### Energy bands (word plus glyph, never color alone)
Fired up 80 to 100, #b8e986, up arrow. Steady 55 to 79, #ffd166, dash. Tired 30 to 54, #ffb8a8, down arrow. Running on empty 1 to 29, #ff8a8a, double down arrow. Stepping back 0, muted gray, pause glyph.

### Outcome tiers (report)
- All core Done, average energy 55 or more, nobody stepped back: "Finished, and the team wants to do another one."
- All core Done otherwise: "Finished, but the team is worn out."
- At least 3 of 5 core Done: "Partly done. The neighborhood still got something real."
- Fewer: "Not this time. Try leading it a different way."
Discussion questions (all projects): "Which week did the team feel best, and what did you do that week?" "Who did you learn about by checking in, and what changed after?" "If you led it again, what is one thing you would do sooner?"

### Plan Your Own notes (shown only when true, gentle wording)
- Over budget: "Over budget by $Z. Cut a supply, or plan a Fundraise task."
- A week with 4 or more tasks: "Week N has M tasks at once. That's a lot for one team."
- No task in week 6: "Nothing in the last week. A wrap-up or thank-you event fits there."
- No "keep the team going" box checked: "How will people want to keep showing up?"
Examples: each of the three projects loads its name, goal, budget, its six tasks with skill, a role (by skill: Build lead, Outreach lead, Logistics lead, Design lead), weeks from the play path in Interactions, and its supply costs.

## Interactions in detail
- Assign: click a volunteer card then a task card, or use the volunteer's "Working on" select. One task per volunteer per week; unassigned means Rest. Clicking an assigned volunteer then the same task unassigns. Only Open tasks and Fundraise accept people. Locked cards show "Needs: <task> done first"; supply cards show `Buy <supply> $X` (disabled with "Need $N more" if short); buying makes the task Open.
- Points per volunteer per week = round(hours x match x energy factor x push), match strong 2, okay 1.5, other 1; energy factor from the band at week start: Fired up and Steady 1, Tired 0.75, Running on empty 0.5. Per task: sum, then x1.15 for a Planning meeting, x0.8 for the heat wave on Hands-on, round half up. Capped at the need left: preview says "This week: +N (M extra hours wasted)" in warn when over.
- Energy per week: worked a strong skill -6, okay skill -10, other -14; rest +20; then lead move and event effects; clamp 0 to 100. Start 80. A volunteer who starts a week at 0 is Stepping back for that week and the next (card greyed, select disabled), then returns at 40. Stepping back is shown kindly, never as quitting.
- Need changes: a need increase on a Done task reopens it with that many points left; a decrease never goes below 0. Locks only block starting; a task with progress stays Open.
- Fundraise points x $6 are added to money in the summary. Money can't go below 0; there is no loan.
- Run week is always allowed (even with nobody assigned). Week 6 ends the project and goes to the report.
- Keys: 1 to 6 select a volunteer, then Q, W, E, A, S, D pick the task cards in order, F Fundraise, R Rest; L cycles the lead move; Enter runs the week; Escape cancels a selection. All controls are reachable by Tab with visible focus.
- Restart project and Pick another project ask on the event-card overlay ("Start over? This week's plan is lost.") with `Start over` and `Keep going`.
- Faces: each volunteer's portrait follows the band: Fired up and Steady show the base painting (Fired up with a slow bob), Tired the tired painting, Running on empty the tired painting tilted and a little desaturated, Stepping back the tired painting in grey at .45 with a pause badge. The band word, glyph and bar still carry the meaning. Motion off: no bob, changes are instant. Portraits show in the meet row (72 px), the volunteer cards (42 px, down to 19 px in the tiny layout, zoomed to the face), the week summary and the report's team row.
- Verified play path (builder: confirm numbers in Python): Riverside, all core done by week 5 with Map/Sign-up week 1, signs week 1-2, Cleanup weeks 2 to 3, recycling week 4, using strong skills, Check in week 1 then alternating Thank and Ask for ideas. Naive play (everyone on one task, Push harder every week) must drive someone to Stepping back by week 4. Both must hold for all three projects; tune needs by at most 10 if not, and update this spec's numbers in notes.md.
- Plan Your Own: typing updates the timeline and budget live. Nothing is written to localStorage until `Save on this device` (key `curio-community-project-planner-plan`, JSON, try/catch, a "Saved" status for 3 s). On load, a saved plan is restored and the panel says "Loaded your saved plan." `Clear` asks (inline, `Clear everything` / `Keep it`), then empties the form and removes the key. `Print plan` prints the form and timeline on one page in light colors (print stylesheet: white paper, dark ink, patterns kept). `Print report` likewise for the report.
- localStorage holds only the saved plan (when Saved) and the kit Motion key. No game progress is stored.

## Look
- 9-12 band: `kit:theme-912` dark instrument look, own accent `--brand: #56c7b8` (harbor teal, civic and calm), `--brand-ink #1c1203`. Taken by siblings: mustard #8a5a10, violet #5a2fb8, burnt orange #b3471d, dawn rose #f2a0b8 (resilience-map), moss olive #4a6417 (decision-tree). Other 9-12 tools: amber #f2a93b, cyan #3cc8dc / #36c9dd, teal #3ec9b6 (imaginary-island, not a neighbor; ours is greener and softer), green #2fa37a, oranges #ff9442 / #e98a4c.
- Contrast (computed): brand on --panel #141b25 8.45:1, on --sec-bg #18202b 8.01:1, on --paper #0d1219 9.18:1, on cards #202a38 7.08:1; brand-ink on brand 9.02:1. Task and volunteer cards #202a38: ink #e8edf3 12.31:1, muted #a6b3c4 6.81:1; skill colors on cards: Hands-on 7.41:1, Outreach 7.91:1, Logistics #ff9ad5 7.47:1, Design 6.87:1. Energy colors on --sec-bg: Fired up #b8e986 11.75:1, #ffd166 11.38:1, #ffb8a8 9.90:1, #ff8a8a 7.23:1.
- Clash fixes: the Logistics skill color is pink #ff9ad5 (was mint) and Fired up is lime #b8e986 (was mint #6fdca6), so nothing on the board shares the accent's teal. Outreach stays sky blue #7cc7ff, a clearly bluer, lighter hue, and always carries its megaphone icon and word.
- Banner images sit under a dark gradient (left 75% #0d1219 to transparent) so the title text keeps 12:1 or more.
- Minimal celebration: finishing a task shows "Done" and a check, no confetti.

## Art
Banners: local FLUX, no people or figures. Volunteers: gpt-image-2 portraits through Codex (people, reviewed), see below. Each banner is a 4:1 banner across the top of the week board and on the picker card (cropped to 16:10 there, so keep the middle interesting).
- banner-river: "a quiet river trail at morning, a dirt path along a grassy bank, trees and soft light, a few litter pieces near reeds, soft painted illustration"; 4:1; cutout no; people no; Riverside Cleanup.
- banner-garden: "an empty grassy lot beside a small brick library building, a chain-link fence, afternoon sun, soft painted illustration, blank walls"; 4:1; cutout no; people no; Library Lot Garden.
- banner-coats: "a community center room with rolling racks of colorful winter coats and cardboard boxes, plain blank boxes, window with falling snow, soft painted illustration"; 4:1; cutout no; people no; Winter Coat Drive.
Fallback if an image fails: a flat teal-to-panel gradient with the project name.

Volunteer portraits (added 2026-10-26 after Cory's review, "needs better graphics for the people"): gpt-image-2 through Codex, editorial graphic-novel style (own `house_style` in prompts.json), head-and-shoulders bust, cut out, 192 px WebP, about 7 KB each, 12 in all (89 KB). `vol-<id>` is the base (Fired up, Steady, meet row) and `vol-<id>-tired` the low-energy variant (Tired, Running on empty, Stepping back). vol-dana was drawn first as the style anchor; the other five used it as a style-only reference. Ages: Dana early 40s, Luis 17, Mei about 27, Tariq 19, Grace late 50s, Ben 16. If a portrait fails to load, the old face drawn in code takes its place. Full plan: art-plan.md. Plan Your Own has no images (timeline drawn in code). These three are not used by any batch sibling.

## Voice
Bank voice `wise-mentor` (Gacrux): "Say thoughtfully and warmly, like a wise high school mentor." A mentor talking to a teen who's leading for the first time; different from siblings (gentle-storyteller, upbeat-guide, big-sister). Narration only for welcomes, project intros, hints and the report tier line; task and event text is on screen only. Fixed lines:
- Welcome, Run a Project: "You're leading a neighborhood project. Pick one. Your volunteers are your biggest resource."
- Welcome, Plan Your Own: "Plan a project of your own. Use roles, not names. It stays on this computer."
- Intro, Riverside Cleanup: "Riverside Cleanup. A good first project. Start by finding where the trash is."
- Intro, Library Lot Garden: "The library garden. Some jobs have to wait for others. Plan the order."
- Intro, Winter Coat Drive: "The coat drive. Money is tight, so every dollar and every hour counts."
- Hint, assigning: "Pick a volunteer, then a task. People do best on their strong skill."
- Hint, lead move: "Pick one lead move for the week. You won't know what people care about until you check in."
- Hint, someone Tired: "Someone is tired. A rest week now can save the project later."
- Hint, after an event: "Things change. Choose, then plan the week around it."
- Hint, week 6: "Last week. Finish what you can, and thank the people who showed up."
- Hint, Plan Your Own: "Give each task a skill, a role and the weeks it runs. Watch the budget on the right."
- Report tiers: the four outcome sentences in Content.
Voice behavior follows STANDARDS.md (collision-lab pattern): one welcome per mode, intro on picking a project, Read speaks the current hint.

## Family engine
none

## Sources
- CASEL, "What Is the CASEL Framework?" (Relationship Skills: "Showing leadership in groups", "Practicing teamwork and collaborative problem-solving", "Seeking or offering support and help when needed"; Responsible Decision-Making: "Reflecting on one's role to promote personal, family, and community well-being"), checked 2026-10-26: https://casel.org/fundamentals-of-sel/what-is-the-casel-framework/
- Matching volunteers to their skills, recognizing them and checking in as practices linked to volunteers staying: Eisner, Grimm, Maynard and Washburn, "The New Volunteer Workforce", Stanford Social Innovation Review, Winter 2009: https://ssir.org/articles/entry/the_new_volunteer_workforce (builder: verify this article and its claims before quoting it in notes.md, or drop it; put no numbers from it on screen).
- Everything in the game (projects, prices, needs, energy) is a made-up model, labeled on screen as made up. The tool says "usually" and "can", never "proven". notes.md says the model is a simplification for discussion, not a measurement, and that the school counselor is the right next step if a student is upset.

## Done when
1. All three projects can be finished with every core task Done and the top outcome tier using the verified play path, and naive play (all on one task, Push harder every week) sends a volunteer to Stepping back by week 4, recomputed in Python.
2. Points and energy in the week summary match the formulas in Interactions for a hand-checked week (strong, okay, other match; Tired factor; Planning meeting x1.15; Push x1.5), including the "extra hours wasted" preview.
3. Locks, supply purchases, money floor, event options (including disabled "Not enough money") and need reopening all behave as written for every event in Content.
4. "Cares about" shows "?" until the first Check in, then stays revealed; the repeat-move rule halves bonuses.
5. A volunteer at 0 is Stepping back for two weeks and returns at 40; every energy band shows a word and glyph, not only color.
6. Plan Your Own: timeline and budget update live; the four notes appear only when true; nothing in localStorage until Save; Clear removes the key; Print plan fits one light page.
7. Run a Project has no text input anywhere; localStorage holds only the saved plan and the kit Motion key.
8. Task cards, the lead-move toggles and Run week are visible without scrolling at 1366x768, 1280x720 and 800x500; works at 760 and 375 wide; keyboard shortcuts and Tab order work.
9. Welcomes play once per mode, the project intro plays on picking, Read speaks the current hint, mode switches stop speech.
10. No em dashes anywhere; always "Curio Class".
