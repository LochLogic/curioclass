# Paper Plane Assembly Line

## One idea
Same three friends, same hour, same paper: move them from each making whole planes to a line where each does the job
they are quickest at, and watch more planes come out, a pile grow at the slow station, and the whole line stop dead
the day one friend is out sick.

## Not like
- learn-and-earn (gr 4, tycoon, concept): one kid's own skills, tools and income over a year. Here a team: who does which job, where the pile forms, and what happens when one person is missing.
- teddy-bear-makers (gr 1, builder, concept): puts steps in order and adds up one bear's cost. Here the steps are fixed; the play is splitting them between people and watching output per hour.
- piggy-bank-planner (gr 2, tycoon, concept): saving and banks. Here no saving or bank; money is only sales minus paper.
- barter-bay (gr 4, simulator, concept): money, prices and inflation across a town. Here prices are given by the contest; the student only responds to them.
- ripple-street (gr 3, story, concept): one kid's choices, incentives and neighbors. Here a shop and its workers.
- trade-island (gr 12, tycoon, spec): comparative advantage and trade between islands. Here one shop, no trade, no opportunity-cost math: each friend's minutes are on their card.
- egg-carton-factory (gr 4 math, built spec): a packing shed for factor pairs. Here no number puzzles about the product; a kraft-paper and sky-blue art room, not a green farm shed.
- leaf-factory (gr 7 science, same batch): a leaf as a factory of sugar. Different subject; here people, jobs and money.

## Who and how
Grade 3 social studies, module social-studies-3-business-and-specialization. Driver: students (solo by default) or
teacher on a projector with the class calling out plans. 20 to 35 minutes (the week about 15, the puzzles about 10).
Standards: D2.Eco.3.3-5, D2.Eco.7.3-5, D2.Eco.13.3-5, D2.Civ.6.3-5. No personal prompts. The shop, its friends,
times and prices are made up; the week report footer says "The shop, the friends and the prices are made up for
practice." Out sick is shown as an empty stool with a get-well card, never a sick child.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.3.3-5 resources | Puzzle 5: sort 8 cards into Natural resources, Tools and machines, Skills; in the week, every item bought wears its kind tag | three bins; tags "Tool: physical capital", "Training: human capital"; paper stack tag "Paper is made from trees: a natural resource" | Puzzle 5 passes only with all 8 in place; June's training in Tools plays sortSkill |
| D2.Eco.7.3-5 profit | Thursday: prices change; the student picks Plain or Decorated and sees profit; Puzzle 3 picks the plane that leaves more profit on three boards | day card: sales, paper, profit; Thursday decorated line 18 planes $8.10, plain line 29 planes $25.70 | Puzzle 3a passes only with Plain, Decorated, Plain; the $80 goal cannot be met without switching (best never-switch week $77.80) |
| D2.Eco.13.3-5 productivity | Wednesday store: buy a tool or a training for a station; Puzzle 2 spends one tool and one training | the pile at the slow station shrinks; "Planes per worker" goes from about 6 to about 9 | stencil on Wednesday: 18 to 28 planes; folding board instead: 19; Puzzle 2a passes only with stencil plus June's training |
| D2.Civ.6.3-5 working together | Tuesday: each on their own vs a line; Friday: Omar out; Puzzles 1 and 4 | Tuesday 12 vs 18 planes; Friday an empty station makes 0 while each-on-their-own makes 8 | Puzzle 1 passes only with the fastest jobs; Puzzle 4a passes only with None, Fewer, Fewer |

## Screens and modes
Header: title, mode buttons **Contest Week**, **Shop Floor**, **Puzzles**, then kit Motion, Sound, Read.

On load: Contest Week, Monday. The stage shows the art-room shop: Lena alone at her table with a paper stack, the
done box beside her, the clock strip "3:00 to 4:00" at 3:00. Panel: Monday card "Monday: Lena makes every plane by
herself. Press Start the day and count her planes.", the price strip, the goal strip "Goal: $80 profit by Friday for
the flying contest", money "$0.00". Nothing plays before the first tap. Hint: "Press Start the day and count Lena's
planes." The first tap on **Start the day** runs Monday (the main path) and speaks monStart; a first tap anywhere
else queues wWeek, which may be cut (rule 16); its premise (you run the shop, goal $80) stays in the goal strip and Read.

**Contest Week** (story tycoon, five days). Focus: the shop table, center of the stage, about 880 by 480 px at
1366x768. Line layout: one long table left to right: paper stack, **Fold**, **Crease**, **Decorate**, done box; each
station is a big tap target with its friend standing behind it, a tool spot on the table, and a pile spot before it
with a count badge ("4 waiting"). Each-on-their-own layout: three small tables side by side, each with one friend,
paper and a done box. Above the table: the clock strip and a plane counter "Planes done: 12". Panel (about 440 px):
the day card (title, one-line task), **Line** / **Each on their own** toggle, **Plain** / **Decorated** toggle with
prices, three friend cards (portrait, name, minutes per job: "Fold 2 min, Crease 3 min, Decorate 5 min", and the
stations they hold), the store (from Wednesday), **Start the day**, **Next day**, money, goal strip. After a run the
day card shows: planes, half-done, sales, paper, profit, "Planes per worker: about 6", and a list of today's runs.
- Monday: one friend, no toggles; only Start the day. Next day appears after the run.
- Tuesday: Omar and June arrive. Default plan: Each on their own (so doing nothing gives 12). Line: tap a friend card,
  then a station (or drag a portrait onto a station). Plain / Decorated opens.
- Wednesday: the store opens: **Folding board** (Fold), **Crease roller** (Crease), **Stencil** (Decorate), $5 each,
  and **Training** $3 (pick a friend, then a job). Each item is a toggle for today; it is paid when Next day is
  tapped and then owned for the week. A tool shows on its station; a trained friend's card shows the new minutes.
- Thursday: the news card (whole line) changes prices: Plain 50 cents to $1.00, Decorated $1.00 to 60 cents.
- Friday: Omar's stool is empty with a get-well card; his card reads "Out sick today" and cannot be placed.
- Each day can be run again as often as the student likes; Next day keeps the last run. After Friday, the week
  report: daily profit bars drawn in code, the week total against the $80 goal, the pin-shop card, **Play the week
  again** and **Go to Puzzles**.

**Shop Floor** (explore). The same table and panel with everything open: both layouts, Plain / Decorated, price
steppers for each plane (10 cents to $2.00 in 10 cent steps; defaults 50 cents and $1.00), the three tools and any
training as toggles (no money limit; the card notes "Tools $5 each, once"), and an **Out sick** toggle on each friend
card. Readouts as the day card, plus a "Slow spot" label under the station with the biggest pile (or "Fold" when no
pile forms and the later friends wait). **Start the day**; no Next day.

**Puzzles** (optional checks). Five cards with a pager and dots; counter "Puzzles solved 3 of 5 (2 on your own)".
Each card: plan, then **Check**, which runs the plan once (5 s, fast clock). Right: right line, a stamp. First miss:
its reason, then the card re-rolls to another variant (the one least tried). Second miss: shown, the right plan
runs, and the card counts "with help". The day card readouts, Slow spot label and the week's runs are never on screen.
1. Right jobs: three friend cards (times for a new plane design) and the empty line. Put one friend on each station.
2. Fix the pile: the line already set, with a 5 s preview run that ends showing piles and waiting friends; pick one
   tool and one training (training happened last week, so no time is lost).
3. Profit pick: three boards from "another class's shop", each with Plain and Decorated bars for Sold and Costs (whole
   dollars, labels in code); tap the plane that leaves more profit on each board.
4. Sick day: one friend is out. Three mini shops, each with its normal-day number; for each, tap **About the same**,
   **Fewer** or **None**. Check runs all three side by side.
5. What went in: 8 cards in a tray, three bins; tap a card, then a bin (a card in a bin can be tapped back).

What the picture shows for every outcome: a run: planes slide station to station and drop into the done box; a pile:
planes stack before a station with its badge, and friends who cannot pass a plane on take the wait pose; table full
(4 waiting): the friend before it waits; empty station: planes stack before it, nothing reaches the done box, the
counter stays 0 and the station glows dashed red; a good day: all friends cheer at the end; a goal week: bunting
drops on the report; a missed goal: the report shows "$76.40 of $80" with the gap drawn on the meter.

1366x768: header 52 px; stage about 900 px wide; panel 440 px; the table, every station, friend cards, toggles,
store, Start the day and Next day sit above the fold (the store folds into a 2 by 2 grid). 680x425: stage and panel
side by side, panel 250 px; friend cards become portrait chips with minutes as "F2 C3 D5"; the price and goal strips
merge into one line; the week report chart shrinks to 5 bars with values. Puzzle 5's tray pages 4 cards at a time
there.

## Content
Friends (Dart, the week's plane), minutes per plane: Lena Fold 2, Crease 3, Decorate 5; Omar Fold 4, Crease 2,
Decorate 4; June Fold 4, Crease 3, Decorate 3. Plain planes skip Decorate (a friend left there waits all day).
Rules: switching jobs costs 1 minute each time; a tool takes 1 minute off its job for anyone at that station; a
training takes 1 minute off one friend's one job, and that friend misses the first 15 minutes of that day. No job
goes below 1 minute. The day is 60 minutes. Paper is 10 cents a sheet, charged for every sheet started (finished
or half-done). Each day starts with an empty table; half-done planes go to the practice pile for test flights.
Prices: Monday to Wednesday Plain 50 cents, Decorated $1.00; Thursday and Friday Plain $1.00, Decorated 60 cents.

Worked days (all checked): Monday Lena alone, Decorated: 4 planes, 1 half-done, sales $4.00, paper $0.50, profit
$3.50. Tuesday Decorated: each on their own 12 planes (3 half-done) $10.50; line Lena Fold, Omar Crease, June
Decorate 18 planes (9 half-done) $15.30; other lines 13, 13, 13, 10, 10. Tuesday Plain line Lena Fold, Omar Crease:
29 planes, $11.50. Wednesday line with Stencil: 28 planes, $25.00; with Folding board or Crease roller: 19, $16.30;
training June on Decorate: 22, $19.00 (28 from Thursday). Thursday line Decorated 18, $8.10; Plain line Lena Fold,
June Fold, Omar Crease 29, $25.70; with Crease roller 43, $38.50; each on their own Plain 21, $18.60. Friday (Omar out):
Decorated line with his station empty 0 planes, minus $0.40; Lena on Fold and Crease, June Decorate 8, $3.90; each on
their own 8, $3.80; Plain line Lena Fold, June Crease 19, $16.60; Plain each on their own 14, $12.40.

Week totals: each on their own all week, Decorated, no buys $34.00; line, never switching, no buys $46.10; line,
switch to Plain Thursday, cover Friday, no buys $76.40; the same plus Stencil on Wednesday $81.10; plus Crease roller on
Thursday as well $98.30. Best possible: each on their own only $63.50; never Plain $77.80; no buys $83.80; any $147.70.

Tags: Folding board, Crease roller, Stencil: "Tool: physical capital. Made by people to help make more." Training:
"Training: human capital. A skill a person keeps." Paper stack: "Paper is made from trees: a natural resource."

Pin-shop card (week report): "In 1776 Adam Smith wrote about a small pin workshop. Ten workers, each doing a few
steps, made about 48,000 pins in a day. Working alone, he wrote, each might not have made even 20."

Puzzle 1 variants (Fold, Crease, Decorate minutes; right jobs; output, others):
- 1a Glider: Lena 4, 2, 5; Omar 5, 4, 2; June 2, 4, 4. Right: June Fold, Lena Crease, Omar Decorate: 28 (others 13 or 10).
- 1b Stunt: Lena 4, 5, 2; Omar 2, 4, 5; June 5, 2, 4. Right: Omar Fold, June Crease, Lena Decorate: 28 (others 13 or 10).
- 1c Dart (the week's table): Lena Fold, Omar Crease, June Decorate: 18 (others 13 or 10). Used last.
Card order of friends is shuffled each time. Prompt: "Put one friend on each station to make the most planes. Then tap Check."

Puzzle 2 variants (line Lena Fold, Omar Crease, June Decorate; minutes at their station; preview 10 planes):
- 2a Big Glider 3, 3, 5: pile before Decorate. Right: Stencil + train June: 18 planes (other pairs 13 or 11).
- 2b Twin-Wing 3, 5, 3: pile before Crease. Right: Crease roller + train Omar: 18.
- 2c Loop Plane 5, 3, 3: no pile; Omar and June wait. Right: Folding board + train Lena: 18.
Prompt: "You have $8. Pick one tool and one training to make the most planes. Then tap Check."

Puzzle 3 variants (Plain sold, cost; Decorated sold, cost; answer):
- 3a: $15, $3 vs $18, $9 Plain; $10, $2 vs $20, $6 Decorated; $24, $4 vs $22, $6 Plain.
- 3b: $12, $3 vs $16, $4 Decorated; $20, $4 vs $25, $12 Plain; $9, $2 vs $14, $5 Decorated.
- 3c: $18, $3 vs $21, $9 Plain; $14, $7 vs $12, $2 Decorated; $16, $5 vs $20, $6 Decorated.
Prompt: "On each board, tap the plane that leaves more money after costs. Then tap Check." After a pass the card
adds: "Sellers make more of what leaves the most profit."

Puzzle 4 variants (normal day: line 18, each on their own 12; answers):
- 4a Omar out: line with his station empty (None, 0); each on their own (Fewer, 8); line with Lena on Fold and Crease (Fewer, 8).
- 4b June out: each on their own (Fewer, 8); a normal line day, nobody out (About the same, 18); line with her station empty (None, 0).
- 4c Lena out: a normal each-on-their-own day (About the same, 12); line with her station empty (None, 0); line with Omar on Fold and Crease, June Decorate (Fewer, 7).
Prompt: "One friend is out. For each shop, tap About the same, Fewer or None. Then tap Check."

Puzzle 5 cards (shuffled): Trees (wood for paper), Water (paper mills use it) in Natural resources; Folding board,
Crease roller, Markers in Tools and machines; Lena's quick folding, Omar's neat creasing, What June learned in
training in Skills. Bins: **Natural resources**, **Tools and machines** (physical capital), **Skills** (human capital).

## Interactions in detail
- The run (Contest Week, Shop Floor, Puzzle checks): 60 shop minutes in 15 s (0.25 s a minute; Puzzle checks 5 s).
  Each minute, friends act in this order: the one whose furthest station is latest in the line goes first, ties in
  roster order Lena, Omar, June. A free friend looks at their stations from the latest back and takes a plane from
  the first one that has a plane waiting (Fold always has paper) and room after it (fewer than 4 waiting at the next
  station; the done box has no limit). The job then takes its minutes, plus 1 when the friend holds two or more
  stations. Each on their own: each friend makes whole planes (all jobs plus 1 minute per job for switching), so
  planes = floor(available minutes / minutes per plane), plus one half-done when minutes are left over. Every worked
  day in Content follows these rules exactly.
- A tap that changes the plan during a run (a toggle, a friend placed, a store item, a price) restarts the day at
  once from 3:00 with the new plan. **Start the day** reads **Finish now** during a run and jumps to 4:00. Mode
  switch stops the run. Motion off: planes jump between spots instead of sliding; the clock keeps its 15 s.
- A friend can hold up to three stations (tap again to remove one). A station can hold several friends. A friend at
  Decorate on a Plain day waits all day, card note "Not needed for plain planes".
- Store: an item is disabled with "Need $5" (or $3) when money before today is short. Training needs a friend and a
  job picked; one training per day. Untoggling before Next day refunds nothing because nothing was paid yet.
- Money starts at $0; each day adds that day's profit when Next day is tapped, minus what the store charged. It can
  go below zero (a 0-plane day costs its paper); then the store waits until it is $5 again.
- Play the week again resets the week (not the best week or puzzles). Saved on this device (localStorage, try/catch):
  best week total, puzzles solved and how. "Saved on this device only." shows on the report and the Puzzles counter.
- Puzzles: Check is disabled until the plan is complete (every station filled; one tool and one training; all three
  boards; all three shops; all 8 cards placed). Puzzle 5 miss reason, first that applies: a skill card in Tools or
  Natural (sortSkill); a tool card in Natural or Skills (sortTool); a natural card elsewhere (sortNature).

## Look
Paper `#f7f4ec`, ink `#1e2633` (13.84:1), muted `#5a6170` (5.66:1). Accent `--brand #1d5fa6` sky blue (5.9:1 on paper,
white on it 6.48:1): mode buttons, Start the day, Check, the line toggle. Kraft table `#d9c7a3` with ink labels
(9.16:1). Decorated chip `#b44a0a` orange with white text (5.35:1; 4.87:1 on paper as an outline); Plain chip white
with an ink outline. Profit `#2e6b30` (5.86:1) and loss `#b3261e` (5.95:1), always with a plus or minus sign, so color is
never the only signal. Empty station: dashed `#b3261e` ring plus the "Empty" label. Contest bunting `#f2b632` with
ink (8.34:1). Different from egg-carton-factory's meadow green and the-buyout's newsroom look.

## Art
- shop-bg: a sunny elementary school art room after school, long low wooden table along the bottom, tall windows, a blank corkboard, paper bunting; 16:9; no cutout; no people; Contest Week and Shop Floor backdrop.
- lena-work, lena-wait, lena-cheer: Lena, a girl about 9 with light brown skin, dark curly hair in a yellow headband, a green T-shirt; standing at a table folding paper with both hands; standing with arms crossed looking to the side; both arms up cheering; 3:4; cutouts; people: true.
- omar-work, omar-wait, omar-cheer: Omar, a boy about 9 with dark brown skin, short black hair, a blue hoodie; same three poses (pressing a crease with one hand); 3:4; cutouts; people: true.
- june-work, june-wait, june-cheer: June, a girl about 9 with pale skin, freckles, straight red hair in two braids, glasses, an orange sweater; same three poses (drawing with a marker); 3:4; cutouts; people: true.
- empty-stool: a wooden stool with a blank folded greeting card standing on it; 3:4; cutout; Friday and Puzzle 4 (card text "Get well!" in code).
- paper-stack, done-box: a neat stack of white paper; an open cardboard box with a blank front label; 1:1; cutouts.
- plane-folded, plane-creased, plane-decorated: a white paper dart with soft folds; the same dart with crisp sharp creases; the same dart with bright orange and blue stripes and a star; 4:3; cutouts; sprites on the table (creased is the finished plain plane).
- tool-board, tool-roller, tool-stencil, markers: a wooden folding board with guide grooves; a small hand roller with a wooden handle; a clear plastic stencil sheet with star cutouts; a cup of colored markers; 1:1; cutouts; on their stations and on Puzzle 5 cards.
- trees, water: a stand of tall green trees; a clear river over smooth stones; 1:1; no cutout; Puzzle 5 cards.
Drawn in code: stations, piles' badges, clock strip, toggles, friend card text, store, day card, price and goal strips,
the week chart, Puzzle 3 bars, bins. 22 images. Skill cards in Puzzle 5 use a head crop of the work pose. Each friend
is shown whole (head to knees) behind their station at about 170 px tall; at 680x425 friends shrink to 110 px, never
cropped. The three friends must differ clearly at 60 px chips (hair color and shirt color).

## Voice
Bank voice `big-sister` (style: "Say in a friendly, youthful way, like a fifth grader who ran the plane shop last
year"). No close neighbor uses it (resource-detective gravel-ranger, the-buyout news-reader, trade-island
wise-mentor, egg-carton-factory friendly-dad; the others are unbuilt). `Curio.voice`, scope = mode + day (or puzzle
card). No line carries a number; numbers are on screen and Read speaks the hint plus the day card.
- wWeek (how, Contest Week welcome; stale once Monday has run): "You run the paper plane shop for the flying contest. Press Start the day and count Lena's planes."
- monStart (how, Monday's first Start): "Lena folds, creases and decorates every plane herself. Watch her switch jobs."
- monDone (event, whole, Monday run ends): "That's how many one person makes alone. Tap Next day."
- tueIntro (event, whole, entering Tuesday): "Omar and June join the shop. They can each make their own planes, or you can make a line."
- tueHow (how, after tueIntro; needs Start the day): "Tap a friend's card, then a station. Then press Start the day."
- lineMore (event, a line run beats today's best each-on-their-own run): "Same three friends, more planes. Each one does the job they're quickest at, and nobody switches."
- lineLess (event, a line run makes fewer than that): "That line made fewer. Check each friend's card for their quickest job."
- pileHow (how, first time a pile reaches 4): "Planes are piling up. That's the slow spot, and the friends before it have to wait."
- wedIntro (event, whole, entering Wednesday): "The shop store is open. A tool or a training can speed up a station."
- buyTool (how, first tool toggled on): "A tool is physical capital. People made it so they can make more."
- buyTrain (how, first training toggled on): "Training builds skill. That's human capital. It costs time today and pays back later."
- noHelp (event, a run where every item bought today sits away from the slow spot; once per day): "That didn't help much. The planes still wait at the slow spot."
- thuIntro (event, whole, entering Thursday): "News from the contest! The distance race wants plain planes. Check the new prices."
- profitHow (how, after thuIntro; needs Start the day): "Profit is what's left after paying for paper. Make the plane that leaves more."
- friIntro (event, whole, entering Friday): "Oh no, Omar is home sick today. Plan the shop without him."
- emptyStation (event, a run with an empty needed station; once per day): "Nothing gets past an empty station. A line needs every job."
- coverHow (how, first friend on two stations): "A friend can cover two jobs, but switching slows them down."
- weekGoal (event, whole, report with goal met): "Goal met! The flying contest has its money."
- weekShort (event, whole, report short of goal): "The week is done. Try a new plan and play it again."
- wFloor (how, Shop Floor welcome): "Everything is open here. Change anything, then press Start the day."
- wPuzzles (how, Puzzles welcome): "Five shop puzzles. Plan first, then tap Check. You get one run."
- p1How, p2How, p3How, p4How, p5How (how, first time each card opens): the card prompts in Content, word for word.
- right (event, whole): "Yes! That plan works."
- jobsMiss (event, whole): "Look at each friend's card. Who is quickest at each job?"
- pileMiss (event, whole): "Find the slow spot first: the station everyone waits for."
- profitMiss (event, whole): "Bigger sales don't always mean more profit. Take away the costs."
- sickMiss (event, whole): "Think about which shops need every station."
- sortSkill (event, whole): "A skill lives in a person, not on a shelf."
- sortTool (event, whole): "Tools and machines are made by people."
- sortNature (event, whole): "Natural resources come from nature."
- shown (event, whole): "Here's a plan that works. Watch."
- allDone (event, whole): "Every puzzle solved. You could run a real shop."
How lines play once, then live in the hint. Miss lines play once per miss. Day intros play once per day entered.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Week goal $80 | do nothing (Start each day with defaults); each on their own all week; buy everything; line but never switch; mash Next day; rerun days at random | defaults give $34.00; each on their own peaks at $63.50 with any buys; never Plain peaks at $77.80; Next day without a run is disabled; reruns are exploring with the pile and day card in view, which is the lesson. The goal is a pull, not the Civ.6 check: a week with Friday left empty can still pass with big buys, so Puzzle 4 checks that idea |
| Puzzle 1 Right jobs | guess (1 in 6); keep the week's jobs (Lena Fold, Omar Crease, June Decorate); fastest friend first; card order; elimination after a miss | 1a and 1b come first and the week's jobs give 13 there; cards are shuffled; a miss re-rolls to a new table; a second miss is "with help" |
| Puzzle 2 Fix the pile | guess (1 in 9); spend at the first station; always the station with the pile; split tool and training | only both at the slow station pass (18 vs 13 or 11); Fold-first fails 2a and 2b; 2c has no pile (friends wait), so "where the pile is" fails; split pairs give 13 |
| Puzzle 3 Profit pick | guess (1 in 8); bigger Sold bar; smaller Costs bar; always Plain or always Decorated; copy the week's Thursday | every variant has a board where bigger sales lose and one where smaller costs lose (checked); each variant mixes answers; profit bars are never drawn before Check |
| Puzzle 4 Sick day | guess (1 in 27); "someone is out, so Fewer" for all; "line is better, so About the same" | every variant has a None (empty station) and 4b and 4c have an About the same, so all-Fewer fails every variant; answers move between rows across variants |
| Puzzle 5 What went in | guess (1 in 6561); count per bin; card color or position; elimination by checks | bins show no capacity; all cards share one frame; tray order shuffles; a miss names a kind, not a card, and the second miss is "with help" |
| Counter "on your own" | let every card be shown; replay a solved card | shown cards count "with help"; each card counts once |
| Shop Floor | none (explore) | its Slow spot label and readouts never appear in Puzzles |

## Heard in order
Grade 3: not every tap speaks, but story beats are whole and come before the next action.
1. Load: first tap on Start the day: monStart, then the run; first tap elsewhere: wWeek (may be cut). Run end: monDone (whole); hint "Tap Next day."
2. Next day to Tuesday: tueIntro (whole), then tueHow; Start the day waits for neither. A run end: lineMore or lineLess, then pileHow if a pile formed and pileHow was never heard.
3. Wednesday: wedIntro (whole); the first store toggle: buyTool or buyTrain; run end: noHelp (when it applies) before any how line.
4. Thursday: thuIntro (whole), then profitHow. Friday: friIntro (whole); run end: emptyStation, then coverHow on the first two-station placement.
5. Report: weekGoal or weekShort (whole) after the bars finish drawing.
6. Puzzles: the card's how line on open; Check: the run, then right or the miss line (whole), then the card resets or re-rolls; shown (whole) plays before the right plan runs; allDone after the last right line.
A plan tap during a line drops queued lines from the earlier run (stale); a mode switch hushes.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Standards text: D2.Eco.3.3-5 (kinds of resources: human capital, physical capital, natural resources), D2.Eco.7.3-5 (how profits influence sellers), D2.Eco.13.3-5 (raise productivity with better capital goods and human capital), D2.Civ.6.3-5 (benefits and challenges of working together, including workplaces) | C3 Framework, NCSS 2013 (rev. 2017 PDF, data/standards/c3-indicators.txt) | Smithsonian Learning Lab standards pages (Eco.13, Civ.6, found by search); Junior Achievement C3 correlations (Eco.7, Civ.6) | yes; Eco.3 wording from the C3 PDF only, second source not fetched (see Open questions) |
| Adam Smith (1776): ten workers made upwards of 48,000 pins a day; alone each could not have made 20, perhaps not one | Smith, The Wealth of Nations, Book I ch. 1 (Project Gutenberg) | Library of Economics and Liberty (Econlib), Wealth of Nations I.1 | yes |
| Paper is made mostly from wood fiber from trees | Britannica, "paper" | Wikipedia, "Paper" | yes |
| Making paper uses water (fibers are mixed with water) | Britannica, "papermaking" | Wikipedia, "Papermaking" | yes |
| Natural resources, physical capital (tools and machines made by people), human capital (skills and knowledge) | Federal Reserve Bank of St. Louis, Econ Lowdown glossary | EconEdLink / GPB Econ Express, "Productive resources" | yes |
| Productivity: output per worker (per hour) | U.S. Bureau of Labor Statistics, "Productivity" overview | St. Louis Fed Econ Lowdown glossary | yes |
| Profit is revenue (sales) minus costs | St. Louis Fed Econ Lowdown glossary | EconEdLink, profit lesson glossary | yes |
Cut: a real paper-plane distance claim ("plain darts fly farther"); Thursday's reason is the contest's own rule.

Number checks (Python, run 2026-11-07, scratch sim of the exact run rules above): every worked day and week total in
Content; all six Tuesday lines; each tool and training on Wednesday; Friday covers; brute force over every plan (each
friend on any set of stations, both layouts, both planes) for the week bounds (defaults $34.00, each on their own
best $63.50, never Plain best $77.80, no buys best $83.80); Puzzle 1 unique best per variant (28, 28, 18; next 13);
Puzzle 2 all nine pairs per variant (only the slow-station pair reaches 18); Puzzle 3 profits and the bigger-sales and
smaller-costs rules (each fails every variant; no ties); Puzzle 4 outcomes (line 18, each on their own 12, empty
station 0, covers 7 or 8, each on their own minus one 8); contrast ratios in Look.

## Done when
1. Focus: in every mode the shop table (or the puzzle's plan) is the biggest central thing; at 1366x768 every station, friend card, toggle, store item, Start the day, Next day and Check is above the fold; at 680x425 stage and panel stay side by side.
2. Monday makes 4 planes with 1 half-done and $3.50 profit; Tuesday's defaults make 12; the line Lena Fold, Omar Crease, June Decorate makes 18, a pile of 4 shows before Decorate, and lineMore plays.
3. Wednesday: the Stencil makes 28 and "Planes per worker" reads about 9; the Folding board alone makes 19 and noHelp plays.
4. Thursday: the same line Decorated shows $8.10; Plain with June on Fold shows $25.70.
5. Friday: Omar's station empty makes 0 planes, the station glows dashed red with "Empty", and emptyStation plays; Lena on Fold and Crease makes 8.
6. A plan tap during a run restarts the day at once; Finish now jumps to 4:00; a mode switch stops the run.
7. The week reaches $80 only with a line plus switching (the $81.10 path passes; $76.40 shows "of $80").
8. Puzzle 1a passes only with June Fold, Lena Crease, Omar Decorate; Puzzle 2c passes only with Folding board plus Lena's training.
9. Puzzle 3a passes only with Plain, Decorated, Plain; Puzzle 4a only with None, Fewer, Fewer; Puzzle 5 with June's training in Tools plays sortSkill.
10. Voice: each how line speaks once in five repeats; day intros, results and miss lines play every time and finish before the next card or day; no line names a disabled control.

## Open questions
- D2.Eco.3.3-5 wording is backed by the C3 PDF the repo cites; a second source page could not be fetched. The Refine Teaching lens should confirm it against any state copy of C3.
