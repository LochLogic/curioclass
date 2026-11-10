# Fridge Goal Chart

## One idea
A kitchen fridge covered in magnets has a blank chart in the middle, and Grandma Pearl (made up, labeled "illustration") asks the child to pick one health goal for the week, more water, an earlier bedtime, a fruit at snack, or an hour of play outside, then build the chart: the child drags helper magnets onto it (a water bottle by the door, a bedtime song, a fruit bowl at kid height, a jump rope by the shoes) and picks who can help (a grown-up at home, the school nurse, a big sister, the doctor); next comes a pretend week, and seven days play out on the chart, and on Tuesday a cartoon ad on TV says a sugary drink makes you strong, and on Thursday soccer runs late; a chart with a helper for that problem keeps its star, a chart without one misses the day, and the child adds a fix and tries again; then the real week begins, and each day the child taps a star, while a line on screen says the stars stay on this device and never leave it; at the end of the week the child looks back at the stars and says what helped; at the end the child sees that goals hold when you plan for what gets in the way and know who can help, so a child in kindergarten to grade 2 learns to pick a health goal, notice what helps or gets in the way, and name who can help.

## Not like
- habit-hero (Grades K-2, live): caring for a hero's habits. Here one goal of the child's own.
- lunch-tray-builder (Grades K-2, live): food groups on a tray. Here a week-long plan.
- game-day-fuel (Grades 9-12, spec): meal planning for athletes. Here a first goal chart.
- parachute-teamwork (K, spec): group games. Here a home goal.

## Who and how
- Grades K-2, Health, module "Health Goals at Home". Standards: NHES.S2 (analyze influences), NHES.S3 (access valid and reliable resources), NHES.S6 (goal-setting), NHES 3rd edition (2024).
- Format: builder. Driver: one child alone, with a grown-up at home for the real week (tool.json `driver: "student"`). Every word is spoken. Controls 60 px or more.
- Four goals, eight helper magnets, four helpers, the pretend week with two problems, the real week tracker. Extra: Class chart (each child picks a goal; the board shows the goal pictures, no names). tool.json `modes: ["My chart", "Class chart"]`, `minutes: "10-15, then 1 a day"`, `grades_label: "Grades K-2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| NHES.S2 | Spot what pulls on the goal and say helps or gets in the way | the ad; the late night | 3 |
| NHES.S3 | Pick who can help | helper faces on the chart | 2 |
| NHES.S6 | Choose a goal, plan, track a week, look back | the stars | 4 |

## Screens and modes
Header (kit): title "Fridge Goal Chart"; `My chart`, `Class chart`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more.

**On load and first tap.** A warm kitchen, the fridge with a blank chart, and Grandma Pearl with a mug. The welcome is queued (`welcomeAfter: true`): "Let's pick one goal for this week. Tap a goal picture." First hint: "Tap a goal picture."

**Build (focus: the fridge).** At 1366x768 the fridge is center with magnets left and helpers right; at 680x425 magnets and helpers are trays. The child drags magnets onto the chart and taps who can help; each is spoken.

**Pretend week.** Seven days light up in turn. Tuesday: the ad plays (a cartoon can with muscles); the child taps "helps" or "gets in the way". Thursday: soccer runs late. A missing helper loses that day's star; the child adds a fix and replays.

**Real week.** Each day the child taps that day's star. A spoken line: "Your stars stay on this device and never leave it."

**Look back.** On day seven the child taps the stars and says what helped most.

**Plan for the bumps (the aha).** Grandma Pearl: "You planned for the bumps, and you knew who could help. That's how goals stick."

**The end.** The chart with stars. `Print` prints a paper chart to hang on a real fridge.

**Class chart (extra).** Goal pictures only.

## Content
- Every word is spoken; homes and families vary in shape, size and look.
- Stars are saved in this browser's storage on this device only; `Clear stars` removes them, and nothing is sent anywhere.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The goal can be changed until the real week starts; magnets can be moved any time.
- Keyboard: Tab to goals, magnets, chart spots, helpers, days and stars; Enter picks or places.
- With Motion off magnets drop at once.

## Look
- Accent `--brand` #1f5d99 fridge blue (header, the chart, buttons); gold #f4c542 (stars, the day in focus); paper #eef4fb; ink #0a1b2e; muted #4a5462.
- Contrast (WCAG 2.1, computed): white on brand 6.81:1; brand on paper 6.15:1; ink on paper 15.69:1; muted on paper 6.93:1; ink on gold 10.68:1.
- Never color alone: stars are filled or empty outlines; helps and gets-in-the-way carry thumbs.
- Different from this batch (range sage, parachute red, playground orange, gym purple).

## Art
- People (illustrated): Grandma Pearl and four helpers, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): the kitchen (1, 16:9), four goal pictures (4, 1:1), eight magnets (8, 1:1).
- Drawn in code: the chart, stars, days and the cartoon ad.
About 18 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as Grandma Pearl; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.week + ':' + state.day + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `goal`: "Tap a goal picture."
- how `magnet`: "Drag a magnet onto the chart."
- how `helper`: "Tap who can help."
- how `pull`: "Tap helps or gets in the way."
- how `star`: "Tap today's star."
- event, whole, plan for the bumps.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the chart builder, the pretend week with two problems matched to helpers, the real-week tracker in local storage.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Build | Skip helpers | The pretend week misses stars without them. |
| Pulls | Tap "helps" for the ad | The ad's day shows the sugary drink's effect and asks again. |
| Real week | Tap all seven stars at once | Only today's star can be tapped. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `goal`; `magnet`; `helper`.
2. `pull`.
3. `star`.
4. Plan for the bumps (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NHES 2024 S2, S3 and S6 wording | data/standards/nhes-2024.txt | data/modules.csv module line | yes |
| Children 6 to 12 need 9 to 12 hours of sleep and an hour of activity a day | American Academy of Sleep Medicine (2016), pediatric sleep consensus; U.S. Department of Health and Human Services (2018), Physical Activity Guidelines | Centers for Disease Control and Prevention, "About Sleep" and "Physical Activity Basics" | yes |
| Food and drink ads aimed at children push sugary drinks | Federal Trade Commission (2012), "A Review of Food Marketing to Children and Adolescents" | American Academy of Pediatrics (2021), policy statement on marketing to children | yes |
| Planning for obstacles helps goals stick | Gollwitzer and Sheeran (2006), implementation intentions meta-analysis | CDC Healthy Schools, goal-setting guidance in HECAT | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s26, 2026-11-10): an 8 p.m. bedtime and a 7 a.m. wake-up is 11 hours, inside 9 to 12; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 fridge, magnets and helpers; at 680x425 trays.
2. A goal is chosen with helpers and people who can help. (NHES.S3)
3. The pretend week's ad and late night are spotted and fixed. (NHES.S2)
4. The real week is tracked and looked back on. (NHES.S6)
5. Stars stay on the device; `Clear stars` removes them.
6. `Read` reads every card; every control is 60 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: magnets drop at once; no network requests.

## Open questions
None.
