# Shadow Clock

## One idea
In a schoolyard seen from above, the student plants a one-meter stick, picks a latitude band from a list (no location access) and a date from a calendar with the solstices and equinoxes flagged, then scrubs the clock from sunrise to sunset and taps to chalk the shadow tip every hour; the tool logs each mark's length and compass direction in a table, and the student builds a line graph of length against time and a direction fan, then repeats on the other three dates and sees the noon shadow shortest in June and longest in December; after dark the same yard shows the evening sky on each date and the student logs which star groups are up (Orion on winter evenings, Scorpius on summer evenings in the north); at the end a split view puts the yard beside Earth spinning and orbiting the sun, and dragging time moves both together, so a fifth grader learns to represent data in graphs that reveal daily changes in shadow length and direction, day and night, and the seasonal appearance of some stars in the night sky.

## Not like
- sky-diary (1, spec): predicting where the sun and moon will be, no measuring. Here measured shadows and graphs, same family.
- star-lanterns (5, spec): why the sun looks brighter than other stars. Here the patterns Earth's motion makes.
- moon-phase-model (6 to 8, live): moon phases and eclipses. Here shadows and star groups.
- orbit-lab (9, spec): gravity and orbit shapes. Here what a spinning, orbiting Earth looks like from the ground.

## Who and how
- Grade 5, Science, module "Sun, Stars and Shadows". Standard: 5-ESS1-2 (represent data in graphical displays to reveal patterns of daily changes in length and direction of shadows, day and night, and the seasonal appearance of some stars in the night sky).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- One stick, four dates (March equinox, June solstice, September equinox, December solstice), three latitude bands, 13 hourly marks per date from 6 am to 6 pm (52 marks in all, fewer where the sun is down), the evening sky for each date, the split view. Extra: Three yards (compare a northern yard, a yard near the equator and a southern yard). tool.json `modes: ["Yard", "Three yards"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5-ESS1-2 (daily shadows) | Chalk the tip every hour and graph length and direction | the chalk marks; the length line graph; the direction fan | 2 |
| 5-ESS1-2 (seasons) | Repeat on four dates and compare the noon shadows | four lines on one graph | 3 |
| 5-ESS1-2 (day, night, stars) | Log which star groups are up on each date's evening | the evening sky; the star log | 4 |

## Screens and modes
Header (kit): title "Shadow Clock"; `Yard`, `Three yards`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A schoolyard from above at sunrise: blacktop, a painted compass on the ground, a stick in the middle, chalk in a bucket. A calendar strip with four flagged dates and a latitude list (default "Middle of the United States, about 40 degrees north"). The welcome is queued (`welcomeAfter: true`): "The sun just came up, and the stick has a shadow. Let's track it all day. Drag the clock, then tap the chalk at the shadow's tip." First hint: "Drag the clock to 6 am, then tap the tip of the shadow."

**The yard (focus: the shadow).** At 1366x768 the yard fills the left with the table and graph right; at 680x425 the table and graph are a sheet that slides up. Dragging the clock moves the shadow around the stick. Each hour the student taps the tip; a chalk dot and the hour appear on the ground, and the table logs length (to the centimeter) and direction (one of 16 compass points). A tap far from the tip says "Not yet. Tap where the shadow ends."

**Graphs.** After the last mark the student plots length against time; the tool checks each dot against the table. A direction fan draws a ray to each chalk mark. Then the next date. On one graph the four lines show the June noon shadow shortest (about 0.30 m at 40 degrees north) and the December noon shadow longest (about 2.00 m), the equinoxes between (about 0.84 m).

**After dark (day and night, stars).** The clock rolls past sunset; the yard goes dark and the evening sky (9 pm) fills the screen. The student taps star groups that are up and the log fills: Orion on December evenings, Scorpius on June evenings, the Big Dipper all year in the north. A note says the stars are still there in the day, the sun's light hides them.

**The split view (the aha).** The yard on the left, Earth spinning and orbiting the sun on the right. Dragging time spins Earth 15 degrees each hour and moves it along its orbit by date. Narrator: "One spin makes the shadow sweep around the stick. One trip around the sun tilts the noon shadow short and long, and turns the night side toward different stars."

**The end.** The table, the four-line graph, the direction fan and the star log on one page. `Print` prints it.

**Three yards (extra).** The same date in three yards side by side, including one south of the equator, where the noon shadow points south and Orion stands upside down.

## Content
- Sun position from date, hour and latitude (simple solar model, solar time, no daylight saving), three latitude bands (40 degrees north, the equator, 35 degrees south), four dates, six star groups with simple outlines (Orion, Scorpius, Big Dipper, Cassiopeia, Leo, Southern Cross).
- A model note: "Times are sun time. Clock time can be off by an hour."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The clock drags or steps with arrow keys one hour at a time; chalk is placed only at the tip.
- Keyboard: Tab to the clock, chalk, date, latitude, graph points and stars; Enter places and logs.
- With Motion off the shadow jumps hour to hour and Earth shows still frames.

## Look
- Accent `--brand` #9a4a12 schoolyard brick (header, chalk marks, the graph lines); gold #f4c542 (the shadow tip under the cursor, the current hour); paper #fbf6f0; ink #24140a; muted #5e5248.
- Contrast (WCAG 2.1, computed): white on brand 6.25:1; brand on paper 5.81:1; ink on paper 16.57:1; muted on paper 7.04:1; ink on gold 10.95:1.
- Never color alone: graph lines carry date labels and dash styles; star groups carry names.
- Different from this batch (cell green, current blue, strata plum, magma red).

## Art
- Local FLUX (`scripts/localart.py`): the schoolyard by day from above (1, 16:9), the schoolyard at night (1, 16:9).
- Drawn in code: the stick, shadow, chalk marks, the table, the graph, the direction fan, the star field, Earth and its orbit.
About 2 images; the rest is drawn so the angles stay exact.

## Voice
Two bank voices, each unique in this batch: `clear-teacher` as the science teacher in the yard; `friendly-dad` as the stargazer after dark and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.date + ':' + state.hour + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `chalk`: "Drag the clock to the next hour, then tap the shadow's tip."
- how `graph`: "Tap the graph to place a dot for each hour."
- how `date`: "Tap the next date on the calendar."
- event, whole, the four-line graph pattern.
- how `stars`: "Tap a star group that is up tonight."
- event, whole, `split`.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
sky. Copies sky-diary's `/* SKY DATA: begin */ ... /* end */` block unchanged (sun position and day length from latitude and date, the star field) and adds shadow length and direction from sun altitude and azimuth and the six star group outlines, so the block can move to `kit/sky.js` for the whole family.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Chalk | Tap anywhere | Only a tap near the tip logs; others get "Not yet". |
| Graph | Copy one line four times | Each dot is checked against that date's table. |
| Stars | Tap every group | The log only accepts groups above the horizon that evening. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `chalk`; `graph`; `date`.
2. Four-line pattern (whole), waits.
3. `stars`.
4. `split` (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 5-ESS1-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Noon sun altitude is 90 minus latitude plus the sun's declination (about 23.4 degrees at the solstices) | NOAA Global Monitoring Laboratory, "Solar Calculation Details" | NASA, "What Causes the Seasons?" (Space Place) | yes |
| Earth turns 15 degrees each hour | NASA, "Earth's Rotation" (Space Place) | Lunar and Planetary Institute, "Sun and Shadows" | yes |
| Orion is up on winter evenings and Scorpius on summer evenings in the Northern Hemisphere | NASA, "What's Up" monthly skywatching | Royal Museums Greenwich, "Constellations" | yes |
| Stars are in the sky during the day, hidden by sunlight | NASA, "Why can't we see stars in the daytime?" (Space Place) | Lunar and Planetary Institute, "Sky Tellers" | yes |
| South of the equator the noon sun is to the north and shadows point south | NOAA Global Monitoring Laboratory, "Solar Calculation Details" | NASA, "Seasons" (Earth Observatory) | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r1, 2026-11-10): a 1 m stick at 40 degrees north casts noon shadows of 0.30 m in June, 0.84 m at the equinoxes and 2.00 m in December; 360 degrees in 24 hours is 15 an hour; four dates of 13 marks is 52; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 yard with table and graph; at 680x425 sheet.
2. Hourly marks are chalked and graphed by length and direction for one date. (5-ESS1-2)
3. Four dates are graphed together and the noon shadows compared. (5-ESS1-2)
4. Star groups are logged for each date's evening, with the day-and-night note. (5-ESS1-2)
5. Shadow lengths match the solar model within 2 centimeters.
6. No location access is asked for; latitude comes from the list.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: hour-to-hour jumps and still frames; no network requests.

## Open questions
- Code move: the idea card moves 5-ESS1-1 to star-lanterns (default used: this tool teaches 5-ESS1-2 only).
