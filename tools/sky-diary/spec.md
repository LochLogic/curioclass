# Sky Diary

## One idea
The student stands in a backyard at dawn with a house, a tree and a compass rose on the ground, and keeps a sky diary: in the day view the student taps where the sun will be at lunchtime, then drags the clock and sees the sun rise in the east, climb and set in the west, and stars come out and seem to turn around one point at night; in the month view the moon shows each night at the same time and its shape changes in a pattern that repeats about every 29 and a half days, and the student predicts the next shape; in the year view the student picks a winter day and a summer day and light bars on the diary page show daylight hours (about 9 hours and about 15 hours at the middle of the United States), computed for the chosen place; each prediction is stamped in the diary with a check or a "not yet", and at the end the diary's patterns are written in (the sun rises in the east every day, the moon's shape repeats each month, summer days are longer than winter days), so a first grader learns to use observations of the sun, moon and stars to describe patterns that can be predicted, and relates daylight to the time of year.

## Not like
- shadow-clock (5, concept): shadows explained by Earth's spin and orbit, same engine. Here what a child sees from the yard.
- moon-phase-model (6, live): the view from space. Here the view from the ground.
- weather-wardrobe (K, spec): the weather. Here the sky's lights.
- shadow-puppet-studio (1, spec): light and materials. Here the sun's path.

## Who and how
- Grade 1, Science, module "Sun, Moon and Stars". Standards: 1-ESS1-1 (use observations of the sun, moon, and stars to describe patterns that can be predicted), 1-ESS1-2 (make observations at different times of year to relate the amount of daylight to the time of year).
- Format: explorer. Driver: one child with a grown-up nearby, or the class on the projector (tool.json `driver: "either"`). Every card is spoken. Controls 56 px or more.
- Day, month and year views, six predictions, the diary with stamps and patterns. Extra: My town (pick a town from a bundled list to see its sky). tool.json `modes: ["Diary", "My town"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1-ESS1-1 (sun, stars) | Predict where the sun will be, then play the day and night | the sun's path; the turning stars | 2 |
| 1-ESS1-1 (moon) | Predict the next moon shape, then play the month | the moon's shapes in order | 3 |
| 1-ESS1-2 | Compare daylight on a winter day and a summer day | the light bars | 4 |

## Screens and modes
Header (kit): title "Sky Diary"; `Diary`, `My town`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A backyard at dawn: a house, a tree, a compass rose on the grass with East, South, West, North, and a diary page. A card: "Where will the sun be at lunchtime?" The welcome is queued (`welcomeAfter: true`): "Let's watch the sky and write down what we see. First, guess! Tap where the sun will be at lunchtime." First hint: "Tap the sky where you think the sun will be."

**Day view (focus: the sky).** At 1366x768 the sky fills the screen with the diary at the side; at 680x425 the diary is a sheet. The student taps a guess, then drags the clock (or taps `Play`). The sun rises low on the east side, climbs to its highest around midday in the south, and sets on the west side. At night the stars come out and slowly turn around one star near the North Star. Two predictions: lunchtime sun, sunset side.

**Month view.** The same yard at the same evening time, night after night. The moon grows from a thin crescent to full and back; the student taps the next shape from four choices, twice. A strip shows about 29 and a half days to repeat.

**Year view (1-ESS1-2).** A winter day and a summer day side by side. Light bars on the diary page: about 9 hours of daylight in late December and about 15 in late June at 40 degrees north (computed from the place's latitude). The student predicts which is longer first, then sees the bars and the dark-at-dinner and light-at-bedtime pictures.

**The diary (the aha).** Each prediction is stamped with a check or "not yet". Three pattern sentences fill in with pictures: "The sun rises in the east every day." "The moon's shape repeats every month." "Summer days have more daylight than winter days." Narrator: "The sky follows patterns, so you can predict it. That's what you just did."

**The end.** The diary page. `Print` prints it.

**My town (extra).** Pick a state capital from a bundled list; the sky and light bars are computed for it.

## Content
- One backyard in winter and summer looks; the sun path, star turning and moon shapes drawn in code from real astronomy; six predictions; a bundled list of 50 state capitals with latitude and longitude.
- Positions are computed in the tool; no data source and no network.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each view waits for a prediction before time plays.
- Keyboard: Tab to the sky, the clock, choices and the diary; arrow keys move the clock.
- With Motion off the sun and moon jump between times and stars show without turning.

## Look
- Accent `--brand` #283f8f dusk blue (header, the diary, the clock); gold #f4c542 (the sun, the guess); paper #f0f2fb; ink #0b1330; muted #525871.
- Contrast (WCAG 2.1, computed): white on brand 9.55:1; brand on paper 8.55:1; ink on paper 16.35:1; muted on paper 6.28:1; ink on gold 11.23:1.
- Never color alone: stamps carry a check or "not yet" in words; light bars carry hour counts and sun and moon icons.
- Different from this batch (berry, gadget green, canyon rust, lagoon).

## Art
- Local FLUX (`scripts/localart.py`): the backyard in summer and winter (2, 16:9).
- Drawn in code from real astronomy: the sky, the sun path, the stars, the moon shapes, the light bars, the compass rose.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the diary narrator; `bright-teacher` as the sky guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.view + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `guess`: "Tap where you think it will be."
- how `play`: "Drag the clock or tap Play."
- event, whole, each prediction's check.
- how `moon`: "Tap the moon shape that comes next."
- how `bars`: "Tap the day you think is longer."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
sky (family "sky"; no engine file yet). This tool builds the sky family's shared pieces first, in a marked block `/* SKY DATA: begin */ ... /* end */`: sun position and day length from latitude and date, moon phase from date, the star field and the capitals list; shadow-clock reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Tap anywhere | Wrong guesses get "not yet" and the play shows the answer; the pattern sentence still needs the view finished. |
| Moon | Pick at random | The next shape follows the pattern; a wrong pick shows the strip. |
| Year | Skip | The diary's third pattern fills only after the bars. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `guess`; `play`.
2. Check (whole), waits.
3. `moon`; `bars`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 1-ESS1-1, 1-ESS1-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| The sun rises in the east and sets in the west; highest near midday in the south (northern mid-latitudes) | NASA Space Place, "Why does the sun rise in the east?" | National Weather Service, "The Seasons" | yes |
| The moon's shapes repeat about every 29.5 days | NASA Science, "Moon Phases" | U.S. Naval Observatory, "Phases of the Moon" | yes |
| About 9 and 15 hours of daylight at 40 degrees north at the solstices | U.S. Naval Observatory, "Duration of Daylight" tables | NOAA Global Monitoring Laboratory, "Solar Calculator" | yes |
| Stars seem to turn around a point near Polaris | NASA Space Place, "The North Star" | Griffith Observatory, "Sky report: circumpolar stars" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r26, 2026-11-09): day length at 40 degrees north is 14.84 hours at the June solstice and 9.16 at the December solstice (geometric, no refraction); six predictions; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 sky and diary; at 680x425 sheet.
2. Sun and star predictions are checked against the played day and night. (1-ESS1-1)
3. Moon shape predictions follow the repeating pattern. (1-ESS1-1)
4. Winter and summer daylight are compared with computed light bars. (1-ESS1-2)
5. Positions are computed in the tool for the chosen place.
6. Every card is spoken; controls are 56 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps between times; no network requests.

## Open questions
None.
