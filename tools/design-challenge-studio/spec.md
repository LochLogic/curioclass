# Design Challenge Studio

## One idea
A big problem gets solvable in four moves, and the studio has a station for each: break it into smaller problems on
a tree, decide what "better" means (criteria you weigh, constraints you must pass), test ideas in a simulator, then
lay the designs side by side in a weighted table where nudging one weight can flip the winner, so the choice is
yours and you can say exactly what it rests on.

## Not like
- prototype-lab (wave 2, CTE): iterates one physical product against a client's brief, one variable at a time; here
  the problem is a system with many causes, and the work is deciding what matters before choosing.
- Up the Watershed (this group): finds pollution sources from evidence, then funds fixes; here no detective work, and
  the trade-off table with weights is the centerpiece.
- Grid Operator (this group): one fixed scorecard for an energy fleet; here students build their own criteria and
  weights.
- emerging-tech-pitch (wave 2): who a new technology reaches in a town; no simulation or weighted decision there.
- community-project-planner (live): managing volunteers over six weeks; nothing about people management here.
- hand-warmer-lab and hot-meets-cold (wave 3): heat flow as chemistry and physics; here heat is one cause in a
  design problem, and the classroom model is a tool, not the lesson.

## Who and how
- Grade 12, Engineering, Engineering for Global Challenges. Students drive, in pairs or teams of three; a teacher can
  run Trade-offs on a projector as a class vote. 30 to 50 minutes per challenge.
- Topic line: "engineering design for global challenges".
- Standards (module): HS-ETS1-1 (analyze a major global challenge, specify criteria and constraints: Criteria
  station, with the challenge card's facts), HS-ETS1-2 (break a complex problem into smaller manageable problems:
  Break it down), HS-ETS1-3 (evaluate solutions on prioritized criteria and trade-offs: Trade-offs), HS-ETS1-4 (use a
  computer simulation to model the impact of proposed solutions: Prototype).
- tool.json: driver "students", minutes "30-50", modes ["Break it down", "Criteria", "Prototype", "Trade-offs"],
  grades_label "Grade 12".

## Screens and modes
Start screen: three painted challenge cards side by side, **Cool classroom**, **Safe water at home**, **Your own
challenge**, each with **Start**. Inside a challenge, the four stations are tabs in order with a progress dot each;
any tab can be opened at any time (explore first), and the dots only report. Layout: stage left (about 62 percent),
panel right. At 1366x768 each station's main controls fit without scrolling; at 760 wide and below the stage stacks
above the panel and the station tabs become a compact row of four icons with labels.

**Break it down.** Focus: the tree, filling the stage, with the big problem at the top and three branch boxes. Panel:
a deck of sub-problem cards. Drag a card (or tap a card, then tap a branch) onto a branch; **Check tree** says per
card whether it fits that branch, belongs on another, or is not part of this problem (with one line why). Cards that
fit light the option chips that address them ("Sun through west windows: shades, trees"). **Add my own card** (text,
40 characters) adds a blank card the check does not grade.

**Criteria.** Focus: the sort list, moved onto the stage. Each item has two buttons, **Criterion** (more or less is
better) or **Constraint** (must pass). Criteria get a weight slider 0 to 5 (default 3) and a direction label;
constraints get their limit, which the student can edit within a range. **Check sort** gives feedback on the
suggested sort, but any sort is allowed downstream (a different sort changes Trade-offs, and that is fine).

**Prototype.** Focus: the simulator's result, the biggest thing on the stage. Cool classroom: the hottest-day chart
fills the stage; the panel holds the eight option toggles as painted thumbnail tiles (Art) with name and cost, and
the **Comfort line** slider. Safe water: the four protection bars fill the stage with the chosen steps as a row of
painted tiles above them; the panel holds the **Source** chips (painted) and the six step tiles. Your own challenge:
the value table fills the stage. **Save design** stores the current settings as Design 1 to 4 with its results. A
results card under the chart shows every criterion's value and every constraint as pass or fail in words.

**Trade-offs.** Focus: the table, filling the stage. Saved designs as rows, the student's criteria as columns, each
with its weight slider in the header. Each cell shows the raw value and a 0 to 10 score (best passing design in that
column = 10, worst passing = 0, linear between; all equal = 10). Total = sum of weight x score. A design that fails
a constraint is greyed out with the reason and left out of the scaling and the winner. The winner row gets a "top"
tag in words; equal totals read "tie, no top design". **Flip finder** lists, for each criterion, the smallest weight
change (in steps of 1, within 0 to 5) that changes the top design (a tie counts as a change), or "no single change
flips it". A **Why** box with sentence starters ("We chose Design 2 because ..., even though ...") stays on screen
for the session; nothing typed there is saved.

## Content
**Challenge 1, Cool classroom.** Card facts: "In 2020 the US Government Accountability Office estimated that about 41
percent of school districts need to update or replace heating, ventilation and air conditioning in at least half of
their schools." Problem: "A top-floor classroom with west windows reaches 38.6 °C on a heat-wave afternoon. Make it
safer to learn in without using more electricity."
Tree branches: Heat comes in / Heat made inside / Heat stays in. Cards (correct branch): Sun on a dark roof (in); Sun
through west windows (in); Hot outdoor air through open windows (in); 30 students' body heat (inside); Lights and
screens (inside); Hot air trapped overnight (stays); Still air, no breeze (stays). Not part of it: Students are too
loud; The hallway is cold in winter.
Criteria items (suggested sort): Hours over the comfort line in school (criterion, fewer); Hottest feels-like
temperature (criterion, lower); Cost (criterion, lower); Electricity per school day (constraint: no more than today's
7.30 kWh); Budget (constraint: $5,000, editable 2,000 to 15,000); Ready this summer (criterion, yes better); Vents safe
to leave open at night (constraint, yes).
Simulator: eight option toggles with cost: Exterior west shades $1,200; Cool white roof coating $2,500; Roof insulation
$6,000; Night vents, lockable $1,500; Ceiling fans $1,200; Lights and screens off when not needed $0; Shade trees $900
(work in about 15 years, so "Ready this summer: no"); Window air conditioner units $6,000. A **Comfort line** slider 25
to 29 °C (default 27). Stage: the hottest school day as a line chart, 0:00 to 24:00: outdoor temperature (dashed),
indoor (accent), feels-like with fans (dotted), school hours 8:00 to 15:00 shaded, comfort line across.
Model (one room, 3 days from 30 °C, day 3 reported, 60 s steps):
- Outdoor T = 28.5 + 6.5 cos(2 pi (t - 16) / 24): 22 °C at 4:00, 35 °C at 16:00.
- Walls and windows 200 W/K. Roof 72 m², U 1.0 W/m²K (0.35 insulated) against sol-air T = outdoor + a x I / 20, with
  a 0.9 dark or 0.3 cool roof and I = 900 sin(pi (t - 6) / 13) W/m² from 6:00 to 19:00.
- West windows 8 m² x 0.6 x west sun (700 sin(pi (t - 12) / 7) from 12:00 to 19:00, at least 80; 80 from 6:00 to
  12:00); shades cut it 77 percent, trees 50 percent.
- School hours 8:00 to 15:00: open-window air exchange 216 W/K, 30 students x 70 W, lights and screens 800 W (500 when
  off); otherwise 100 W. Fans add 240 W and lower feels-like by 2.5 °C. Night vents add 576 W/K from 19:00 to 7:00
  when outdoors is cooler. Air conditioning: 10.5 kW of cooling, 3.5 kW of electricity, 7:00 to 15:00, set to 26 °C.
  Heat capacity of the room 20 MJ/K. Electricity counted for 24 hours. CO2 shown as 0.367 kg per kWh (US average).
Results (hottest indoor in school hours, hottest feels-like, hours over 27 in school, kWh per day): nothing 38.64, 38.64, 7.0, 7.30;
shades 37.04, 37.04, 7.0, 7.30; cool roof 36.26, 7.0, 7.30; insulation 37.09, 7.0; night vents 34.98, 6.5, 7.30; fans
38.93, 36.43, 7.0, 8.98; lights off 38.28, 7.0, 5.20; trees 37.60, 7.0; air conditioning 26.54, 0, 31.01. Within
both constraints and ready this summer, fewest hours over: shades + vents + fans + lights off ($3,900) 33.82, 31.32, 3.55, 6.88; vents + fans
+ lights off ($2,700) 34.92, 32.42, 3.95, 6.88. Adding the cool roof ($6,400, over budget) gives 2.35 hours. Adding shade trees instead ($4,800) gives 3.50 hours
(33.66, 31.16) but is not ready this summer.
Model note: "One room, one heat-wave day shape. Leaves out humidity, walls heating differently on each side, students
moving, and how hot is unsafe for each person."

**Challenge 2, Safe water at home.** Card facts: "In 2022, 2.2 billion people did not have safely managed drinking
water (WHO and UNICEF)." Problem: "A family of four collects water from a source that may carry germs. Pick a way to
make it safe to drink every day." Safety note on the card: "This is a simulation. For real water, follow your local
health department or the product label."
Tree branches: Germs / Dirt and cloudiness / Daily life. Cards: Parasites like Giardia and Cryptosporidium (germs);
Bacteria (germs); Viruses (germs); Cloudy water hides germs from chemicals (dirt); Filters clog (dirt); Fuel or power
costs money (daily life); Taste puts people off (daily life); Time every day (daily life). Not part of it: Chemicals like
nitrate or lead ("needs testing and different treatment; none of these steps remove them").
Criteria items: Germ protection, weakest of the four groups (suggested: constraint, at least High); Time per 4 L
batch (criterion, less); Cost level (criterion, lower); Needs fuel (criterion, no better); Taste (criterion).
Simulator: **Source** chips: Clear stream, Cloudy river after rain, Rain barrel. Up to three **Steps** in order, from:
Let it settle and pour off (30 min); Cloth filter (2 min); Microfilter, 0.2 micron (8 min, device cost medium); Boil 1
minute (15 min, fuel, flat taste until aired; 3 minutes above 2,000 m); Chlorine drops or tablets (30 min wait, cost
low, chlorine taste); Chlorine dioxide tablets (30 min wait, up to 4 hours for Cryptosporidium per label, cost
low to medium, slight taste). Protection by germ group (Giardia, Cryptosporidium, bacteria, viruses) on CDC's scale
Very high / High / Moderate / Low to moderate / Not effective:
- Boil: Very high for all four.
- Microfilter: High, High, Moderate, Not effective.
- Chlorine: Low to moderate, Not effective, High, High.
- Chlorine dioxide: High, Low to moderate, High, High.
- Settle and cloth filter: no protection (they only reduce cloudiness).
Combining: each group takes the best step; a microfilter plus chlorine or chlorine dioxide gives Very high for all
four (CDC). Cloudy river: chlorine and chlorine dioxide drop one level unless settling or a filter comes before them.
Stage: four horizontal protection bars, the steps as a row of tiles in order, the totals (time, cost level, fuel,
taste).

**Trade-offs worked example** (Cool classroom, default sort, criteria hours, feels-like, cost, ready): Design 1
nothing; Design 2 shades + vents + fans + lights off; Design 3 vents + fans + lights off; Design 4 cool roof + vents +
trees ($4,900; 32.41, 5.35 hours; not ready). At weights 3, 3, 3, 3 the totals are 60.0, 96.1, 95.5, 39.9: Design 2
is top. Flips: hours 3 to 2, feels-like 3 to 2, or cost 3 to 4 each make Design 3 top; Ready never flips it (both
are ready).

**Challenge 3, Your own challenge.** Blank tree with three branches the student names; typed cards (40 characters);
typed criteria and constraints; no simulator, so Prototype becomes a table where the student types up to four design
names and gives each criterion a value 0 to 10. Trade-offs works the same. Saved in localStorage under
`design-challenge-studio` with **Clear my challenge**.

## Interactions in detail
- Drag and drop has a tap-then-tap equivalent and keyboard support (Enter picks a card, arrows choose a branch, Enter
  drops). Cards snap into a branch list; a wrong placement is allowed until Check tree.
- Option toggles update the classroom chart within 100 ms (the model runs 4,320 steps); water steps update at once.
  Nothing plays on its own; a toggle or slider move during a redraw or a highlight replaces it at once.
  Adding a fourth water step is blocked with "Three steps is the limit here".
- Save design over 4 opens "Replace which design?". Changing challenge clears saved designs after a confirm.
- Trade-off scores recompute on every weight move; Flip finder recomputes too. A flip highlights the new top row
  for 300 ms. With one design, the table says "Save
  at least two designs to compare."
- Constraint edits in Criteria re-check every saved design.
- Reset (kit) returns to the start screen; challenge 3 data stays until Clear my challenge.
- `window.__tool`: `{challenge, station, tree, criteria, designs, scores, winner, flips}`.

## Look
Accent `--brand #00f28d` (cutting-mat mint), `--brand-ink #10161f`. Stage like a design studio wall: `#111820` with a
faint 24 px grid `#1a2430`; cards `#1c2532` with `--btn-line` borders. Tree lines `#62789a`. Classroom chart: outdoor
`--gr-4` dashed, indoor accent, feels-like `--gr-1` dotted, school hours band `#ffffff` at 5 percent. Water bars use
`--gr-1` to `--gr-3`, each labeled with its rating in words. Contrast (computed): brand on --panel 11.61:1, on --sec-bg
11.00:1; brand-ink on brand 12.18:1. Nearest accents on any spec are #3ddc97 and #2ff0b0 (dE 20.1); the closest in this
group is Biome Atlas's #5cbf2a (dE 34.2).

## Art
Local FLUX (`scripts/localart.py`), no people anywhere (the classroom is empty on purpose: the heat is the subject).
21 images. Prompts say only what is in the picture.
Cards and backdrops (cutout no; people no):
- dc-classroom: empty high school classroom on a hot afternoon, sunlight streaming through west windows, rows of
  desks, warm light; 16:9; the Cool classroom card and the Prototype backdrop at 20 percent behind the chart.
- dc-water-jug: a clear plastic jug of water and a dented metal cooking pot on a wooden table by a window, soft
  light; 16:9; the Safe water at home card.
- dc-own: a large blank sketchbook open on a drafting table with pencils, a ruler and sticky notes, top view; 16:9;
  the Your own challenge card.
- dc-stream: clear mountain stream over stones in a forest; 4:3; Source chip.
- dc-river: muddy brown river after rain, swollen banks; 4:3; Source chip.
- dc-rain-barrel: blue rain barrel under a house downspout in a garden; 4:3; Source chip.
Option and step kit: one shared prompt, "a single <piece>, three-quarter view, centered, clean product illustration,
soft studio light, on a plain flat light grey background"; 1:1; cutout yes; people no; shown about 72 px on the
option and step tiles and about 96 px in the chosen-steps row.
- Classroom options (8): dc-o-shades (an exterior roller shade on a window frame, half lowered); dc-o-cool-roof (a
  section of flat roof half painted bright white, with a paint roller); dc-o-insulation (a stack of pink insulation
  batts); dc-o-vents (a small lockable louvered wall vent); dc-o-fan (a white ceiling fan); dc-o-switch (a light
  switch beside a laptop with its lid closed); dc-o-tree (a young leafy shade tree in a planting ring); dc-o-ac (a
  window air conditioner unit).
- Water steps (6): dc-s-settle (a bucket of water with a layer of silt at the bottom beside a clean jar); dc-s-cloth
  (a folded cotton cloth tied over the mouth of a jug); dc-s-microfilter (a hand-pump water microfilter with its
  tubes); dc-s-boil (a metal pot of water at a rolling boil on a small stove flame); dc-s-chlorine (a small dropper
  bottle and a strip of white tablets); dc-s-dioxide (a foil blister pack of round tablets).
Sizing rule: every kit piece sits centered in its tile at 80 percent of the tile, bottom-aligned.
Drawn in code: the tree, cards, sort list, the hottest-day chart, protection bars, tables, preview.svg.

## Voice
Bank voice `wise-mentor` (Gacrux, "Say thoughtfully and warmly, like a design studio mentor"). Changed from
easy-coach, which neighbor curling-stones already uses; no neighbor and no other spec in this batch uses
wise-mentor. `Curio.voice`, `scope: () => state.station`.
- wStart (how; start screen; stale once Start is pressed): "Pick a challenge card and press Start."
- wTree (how; Break it down welcome; stale once a card is placed): "Drag each card onto the branch where it belongs,
  or tap a card and then a branch. Then press Check tree."
- wCriteria (how; Criteria welcome; stale once an item is sorted): "Sort each item with Criterion or Constraint.
  Then use each criterion's slider to say how much it matters."
- wProtoRoom (how; Prototype welcome in Cool classroom; stale once an option is toggled): "Turn the option tiles on
  and off and watch the hottest day change. Press Save design to keep one."
- wProtoWater (how; Prototype welcome in Safe water; stale once a step is added): "Pick a Source, then tap up to
  three Steps in order. Press Save design to keep one."
- wProtoOwn (how; Prototype welcome in Your own challenge; stale once a value is typed): "Type your design names,
  then give each one a score for every criterion. Press Save design when done."
- wTradeEmpty (how; Trade-offs opened with fewer than two saved designs; stale once two exist): "Save at least two
  designs in Prototype first. Then come back here to compare them."
- wTrade (how; Trade-offs opened with two or more designs; stale once a weight moves): "Move the weight sliders in
  the column headers. Watch whether the top design changes."
- flip (event; the top design changes during a weight move; stale on the next move): "The top design just changed.
  That weight is doing a lot of work."
- fail (event; a design is saved that fails a constraint; stale when the constraint changes): "That design breaks a
  constraint. It can't win until you change it."

## Family engine
none.

## Sources
- School HVAC needs: US GAO (2020), K-12 Education: School Districts Frequently Identified Multiple Building Systems
  Needing Updates or Replacement, GAO-20-494.
- People without safely managed drinking water, 2.2 billion in 2022: WHO and UNICEF Joint Monitoring Programme (2023),
  Progress on household drinking water, sanitation and hygiene 2000 to 2022, https://washdata.org/
- Water treatment ratings, filter then disinfect, cloudy water, boiling 1 minute (3 above 6,500 ft): CDC, A Guide to
  Drinking Water Treatment and Sanitation for Backcountry and Travel Use (page dated 2025-01-30),
  https://www.cdc.gov/healthywater/drinking/travel/backcountry_water_treatment.html
- Exterior shades on west windows: US DOE Energy Saver, Energy Efficient Window Attachments,
  https://www.energy.gov/energysaver/energy-efficient-window-attachments
- Cool roofs: US DOE Energy Saver, Cool Roofs, https://www.energy.gov/energysaver/cool-roofs
- Body heat about 70 W sensible per seated person: ASHRAE Handbook, Fundamentals (2021), chapter 18.
- Fans and feels-like: ASHRAE Standard 55-2020, elevated air speed.
- Electricity CO2 0.81 lb per kWh (US 2023): EIA FAQ, https://www.eia.gov/tools/faqs/faq.php?id=74&t=11
- Room size, option costs and the heat-wave day shape: made up for this tool, rounded.
- Number checks (Python, 2026-10-29, scratch room.py, room2.py, trade.py): the room model (60 s steps, 3 days from
  30 °C, day 3, hottest values over school hours, AC capped so it never cools below 26) reproduces every Results line
  to 0.01 (insulation 37.10 against the listed 37.09). A search of all 256 option sets found shades + vents + fans +
  lights off + trees ($4,800) at 3.50 hours, under the listed "fewest" 3.55, so that claim now says "and ready this
  summer". The comfort slider at 25 and 29 leaves the no-option day at 7.0 hours (indoor stays above 29 all school
  day). Trade-offs: the worked example and its flips were computed with the scoring rule above; all weights 0 gives a
  tie, now handled ("tie, no top design").

## Done when
1. Cool classroom, nothing on: hottest indoor 38.64 °C, 7.0 hours over 27, 7.30 kWh.
2. Air conditioning alone shows 0 hours over but fails the electricity constraint (31.01 kWh) and the row greys out in
   Trade-offs.
3. Shades + vents + fans + lights off: $3,900, 33.82 °C, feels 31.32, 3.55 hours, 6.88 kWh, both constraints pass;
   adding shade trees gives 3.50 hours and "Ready this summer: no".
4. Fans alone fail the electricity constraint (8.98 kWh); fans plus lights off pass (6.88).
5. Water: Cloudy river with chlorine alone reads Not effective / Not effective / Moderate / Moderate; with settle
   first, Low to moderate / Not effective / High / High; microfilter then chlorine reads Very high for all four.
6. Trade-offs with the four designs in Content's worked example at weights 3, 3, 3, 3: Design 2 is top (96.1 against
   95.5); Flip finder lists hours 3 to 2, feels-like 3 to 2 and cost 3 to 4 as flips to Design 3, and "no single
   change flips it" for Ready; each listed change really flips it. All weights at 0 reads "tie, no top design".
7. Check tree marks "Students are too loud" as not part of the problem.
8. Focus: at 1366x768 and 680x425 the tree, the sort list, the simulator result and the table are each the biggest
   thing on the stage in their station.
9. A tap while anything moves: toggling an option while the chart redraws shows the new result within 100 ms;
   moving a weight while a flip highlight runs recomputes at once.
10. Your own challenge survives a reload and Clear my challenge wipes it.
11. At 1366x768 and 375 wide, the station tabs and each station's main buttons are visible without scrolling; all 21
    images load and none shows a person.
12. Each how-to line speaks once in five actions; flip and fail speak every time; Trade-offs with one design plays
    wTradeEmpty, never wTrade.

## Open questions
- [design-challenge-studio] Challenge 3 saves typed text in localStorage on the device. OK, or keep it unsaved like
  the Why box?
- [design-challenge-studio] Option costs and the room are made up and rounded. Fine, or source real school cost data?
- [design-challenge-studio] The water challenge teaches real treatment steps, framed as a simulation with a "follow
  local guidance" note. Is that framing enough?
