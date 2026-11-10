# Star Lanterns

## One idea
On a dark field at night two identical lanterns sit at the student's feet with a light meter, and the student carries one lantern 1, 2, 4 and 8 steps away and measures how bright it looks, finding that at twice the distance it looks about a quarter as bright; then a challenge puts a big lantern far away and a small one close, and the student finds that a lantern can look dim because it's far, not because it's weak; finally the field turns into the night sky, and the student places the sun and several real stars (Sirius, Alpha Centauri, Vega, Betelgeuse) at their distances on a scale that keeps shrinking to fit, sees that the sun is hundreds of thousands of times closer than any other star, and builds an argument card: the sun looks brightest because it is the closest star, even though some stars give off more light than the sun does; at the end the argument holds a claim, two pieces of evidence from the lanterns and the sky, and a reason, so a fifth grader learns to support an argument that the sun looks brighter than other stars because of how close it is to Earth.

## Not like
- shadow-clock (5, concept): shadows and sky patterns. Here brightness and distance.
- sky-diary (1, spec): what the sky does each day. Here why the sun outshines the stars.
- moon-phase-model (6-8, live): the moon's light and shape. Here stars' light and distance.
- secret-code-signals (4, spec): light as a signal. Here light fading with distance.

## Who and how
- Grade 5, Science, module "Star Brightness". Standards: 5-ESS1-1 (support an argument that differences in the apparent brightness of the sun compared to other stars is due to their relative distances from the Earth).
- Format: lab. Driver: one student alone, or the class on the projector (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- Two identical lanterns at four distances, the light meter and table, the big-far and small-close challenge, the sky scale with the sun and four stars, the argument card. Extra: Class field (the class predicts each meter reading). tool.json `modes: ["Field", "Class field"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5-ESS1-1 (evidence: lanterns) | Move a lantern to four distances and read the meter | the meter; the table | 2 |
| 5-ESS1-1 (evidence: real stars) | Place the sun and four stars at their distances | the shrinking sky scale | 3 |
| 5-ESS1-1 (argument) | Build a claim with two pieces of evidence and a reason | the argument card | 4 |

## Screens and modes
Header (kit): title "Star Lanterns"; `Field`, `Class field`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A dark field under stars, two identical lanterns and a light meter. The welcome is queued (`welcomeAfter: true`): "These two lanterns are exactly the same. Carry one farther away. What happens? Drag a lantern to step 2." First hint: "Drag a lantern to step 2."

**The field (focus: the lanterns).** At 1366x768 the field fills the left with the meter and table right; at 680x425 the table is a sheet. Step marks at 1, 2, 4 and 8. The meter reads the far lantern compared with the near one (100 at step 1). The table fills: at step 2 about 25, at step 4 about 6, at step 8 about 2. A card asks for the pattern: "Twice as far looks about ___ as bright."

**Big and small.** A big lantern (four times the light) is placed at step 4 and a small one at step 1. The student predicts which looks brighter, then measures: the small close one wins. A card: "A light can look dim because it's far away."

**The sky (focus: the scale).** The field becomes the sky. The student drags the sun and four stars onto a distance line that keeps zooming out to fit: the sun at about 8 light-minutes, Alpha Centauri at about 4.4 light-years, Sirius at about 8.6, Vega at about 25, Betelgeuse at hundreds. A side card says Sirius gives off about 25 times as much light as the sun, yet looks far dimmer because it is so far away.

**The argument (the aha).** "Claim: The sun looks brightest because ___. Evidence 1 (lanterns): ___. Evidence 2 (stars): ___. Reason: ___." Narrator: "The sun isn't the biggest or brightest star out there. It's just ours, and it's close."

**The end.** The table and argument card. `Print` prints them.

**Class field (extra).** The class predicts each reading.

## Content
- Two identical lanterns, one big lantern, four step distances, the meter with a stated rule (brightness falls with the square of the distance), the sun and four stars with real distances, the argument card.
- Distances use light-minutes and light-years with a short explanation card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Lanterns snap to step marks; the meter updates at once.
- Keyboard: Tab to lanterns, step marks, the meter, the sky line and the argument card; Enter places.
- With Motion off the sky scale jumps between zoom levels.

## Look
- Accent `--brand` #283a7a night indigo (header, the table, the sky line); gold #f4c542 (the lantern in hand, the sun); paper #f0f2fa; ink #0d1430; muted #535868.
- Contrast (WCAG 2.1, computed): white on brand 10.62:1; brand on paper 9.50:1; ink on paper 16.20:1; muted on paper 6.34:1; ink on gold 11.13:1.
- Never color alone: the meter shows a number; stars carry names and distances.
- Different from this batch (globe blue, tea amber, bakery rose, river green).

## Art
- Local FLUX (`scripts/localart.py`): the dark field (1, 16:9), the lanterns (2, 1:1), the night sky (1, 16:9).
- Drawn in code: step marks, the glow, the meter, the table, the sky line and stars.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the night guide; `upbeat-guide` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.star + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `move`: "Drag the lantern to the next step."
- how `pattern`: "Finish the pattern card."
- event, whole, the big and small result.
- how `sky`: "Drag each star to its distance."
- how `argue`: "Fill in the claim, evidence and reason."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the meter rule, the field, the sky scale, the argument card. Star data sits in a marked block `/* STARS DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Table | Skip steps | The pattern card needs all four readings. |
| Sky | Drop stars anywhere | Each star snaps only to its real distance and asks again. |
| Argument | Say "the sun is the biggest star" | The checker points to Sirius's card and asks again. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `move`; `pattern`.
2. Big and small (whole), waits.
3. `sky`; `argue`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 5-ESS1-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Brightness falls with the square of the distance | NASA Imagine the Universe, "Inverse square law" | The Physics Classroom, "Light intensity" | yes |
| Sunlight takes about 8 minutes to reach Earth | NASA Space Place, "How far away is the sun" | NASA Solar System Exploration, "Sun" | yes |
| Alpha Centauri about 4.4 light-years; Sirius about 8.6; Vega about 25 | NASA, "Alpha Centauri" and "Sirius" (Space Place and Imagine the Universe) | European Space Agency, Hipparcos and Gaia catalogs | yes |
| Sirius gives off about 25 times the sun's light | NASA Imagine the Universe, "Sirius" | European Southern Observatory, "Sirius" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r30, 2026-11-09): with brightness falling by the square of the distance, steps 2, 4 and 8 read 25, about 6 and about 2 when step 1 reads 100; a lantern four times as bright at step 4 reads 25, below the small one's 100 at step 1; Alpha Centauri at 4.4 light-years is about 278,000 times farther than the sun; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 field and table; at 680x425 sheet.
2. A lantern at four distances shows brightness falling by the square of the distance. (5-ESS1-1)
3. The sun and four stars are placed at their real distances. (5-ESS1-1)
4. The argument has a claim, two pieces of evidence and a reason. (5-ESS1-1)
5. The big and small challenge shows dim does not mean weak.
6. Star facts match the cited sources.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: scale jumps; no network requests.

## Open questions
None.
